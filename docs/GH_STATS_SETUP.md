# Language statistics secret

The workflow [`.github/workflows/update-language-stats.yml`](../.github/workflows/update-language-stats.yml) aggregates **language byte counts** from all repositories **you own** (public, private, archived, and forks). It never writes repository names or URLs—only `assets/language-distribution.svg`.

## Recommended: `GH_STATS_TOKEN`

The default `GITHUB_TOKEN` in Actions can read private repos in the **same** repository, but often cannot list language data for **other** private repositories you own. For full coverage:

1. Create a **fine-grained** personal access token (read-only):
   - Repository access: **All repositories** owned by you, or select repos explicitly.
   - Permissions: **Metadata** = Read-only, **Contents** = Read-only (languages API uses metadata).
2. In this repository: **Settings → Secrets and variables → Actions → New repository secret**
   - Name: `GH_STATS_TOKEN`
   - Value: the token
3. Run **Actions → Update language distribution → Run workflow** once to verify.

If the secret is missing, the workflow falls back to `github.token` (public repos only).

Do not commit tokens or echo them in logs.
