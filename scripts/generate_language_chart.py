#!/usr/bin/env python3
"""Aggregate language bytes across owned repos and write language-distribution.svg."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any

API_VERSION = "2022-11-28"
API_BASE = "https://api.github.com"
OUTPUT_PATH = os.environ.get(
    "LANGUAGE_CHART_OUTPUT",
    os.path.join(os.path.dirname(__file__), "..", "assets", "language-distribution.svg"),
)
OTHER_THRESHOLD = 0.02  # Languages below 2% roll into "Other"
BAR_COLORS = {
    "Java": "#b07219",
    "Python": "#3572A5",
    "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Shell": "#89e051",
    "Dockerfile": "#384d54",
    "Other": "#6e7681",
}


def token() -> str:
    stats = os.environ.get("GH_STATS_TOKEN", "").strip()
    if stats:
        return stats
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(
            "GH_STATS_TOKEN is not set; keeping existing language-distribution.svg.",
            file=sys.stderr,
        )
        sys.exit(0)
    for key in ("GITHUB_TOKEN",):
        value = os.environ.get(key, "").strip()
        if value:
            return value
    print("No GH_STATS_TOKEN or GITHUB_TOKEN set.", file=sys.stderr)
    sys.exit(1)


def api_request(path: str, auth: str) -> Any:
    request = urllib.request.Request(
        f"{API_BASE}{path}",
        headers={
            "Authorization": f"Bearer {auth}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "profile-language-stats",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        print(f"GitHub API error {exc.code} for {path}", file=sys.stderr)
        sys.exit(1)


def list_owned_repositories(auth: str) -> list[dict[str, Any]]:
    repos: list[dict[str, Any]] = []
    page = 1
    while True:
        batch = api_request(
            f"/user/repos?type=owner&per_page=100&page={page}&sort=updated",
            auth,
        )
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def aggregate_languages(auth: str, repos: list[dict[str, Any]]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for repo in repos:
        owner = repo["owner"]["login"]
        name = repo["name"]
        languages = api_request(f"/repos/{owner}/{name}/languages", auth)
        for lang, nbytes in languages.items():
            totals[lang] = totals.get(lang, 0) + int(nbytes)
    return totals


def normalize(totals: dict[str, int]) -> list[tuple[str, float]]:
    grand = sum(totals.values())
    if grand == 0:
        return [("Other", 100.0)]

    sorted_langs = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    main: list[tuple[str, float]] = []
    other_bytes = 0
    for lang, nbytes in sorted_langs:
        pct = nbytes / grand
        if pct >= OTHER_THRESHOLD:
            main.append((lang, pct * 100.0))
        else:
            other_bytes += nbytes

    if other_bytes:
        main.append(("Other", (other_bytes / grand) * 100.0))

    return main


def color_for(language: str) -> str:
    return BAR_COLORS.get(language, "#58a6ff")


def build_svg(distribution: list[tuple[str, float]]) -> str:
    width = 640
    bar_height = 28
    label_height = 22
    pad = 12
    total_height = pad * 2 + bar_height + label_height + 8
    x = pad
    segments: list[str] = []

    for lang, pct in distribution:
        seg_w = max((width - pad * 2) * (pct / 100.0), 1 if pct > 0 else 0)
        segments.append(
            f'<rect x="{x:.2f}" y="{pad}" width="{seg_w:.2f}" height="{bar_height}" '
            f'fill="{color_for(lang)}" rx="4"><title>{lang}: {pct:.1f}%</title></rect>'
        )
        x += seg_w

    legend_y = pad + bar_height + label_height
    legend_parts = []
    lx = pad
    for lang, pct in distribution:
        legend_parts.append(
            f'<text x="{lx}" y="{legend_y}" fill="#c9d1d9" font-family="Segoe UI, sans-serif" '
            f'font-size="13">{lang} {pct:.1f}%</text>'
        )
        lx += 88

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{total_height}" role="img" aria-label="Programming language distribution">
  <rect width="100%" height="100%" fill="#0d1117"/>
  {''.join(segments)}
  {''.join(legend_parts)}
</svg>
"""


def main() -> None:
    auth = token()
    repos = list_owned_repositories(auth)
    totals = aggregate_languages(auth, repos)
    distribution = normalize(totals)
    svg = build_svg(distribution)

    out = os.path.abspath(OUTPUT_PATH)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(svg)
    print(f"Wrote {out} ({len(repos)} repositories aggregated, no repo names in output).")


if __name__ == "__main__":
    main()
