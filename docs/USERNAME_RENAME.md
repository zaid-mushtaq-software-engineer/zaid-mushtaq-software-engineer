# Rename GitHub username to `zaid-mushtaq-software-engineer`

`zaid-mushtaq-software-engineer` is **available** (matches your LinkedIn handle). GitHub cannot rename the account from this environment without the **`user`** OAuth scope on `gh`.

## 1. Rename in GitHub (required)

1. Open [Account settings → Change username](https://github.com/settings/admin).
2. Change **`zaid-mushtaq-data-engineer`** → **`zaid-mushtaq-software-engineer`**.
3. Confirm GitHub’s warnings (existing clone URLs redirect for a while).

Your profile README repo becomes `zaid-mushtaq-software-engineer/zaid-mushtaq-software-engineer` automatically.

## 2. Refresh local git remote

```bash
cd /home/zaid/MyWorkspace/Github/zaid-mushtaq-data-engineer
gh auth login -h github.com   # if needed after rename
git remote set-url origin https://github.com/zaid-mushtaq-software-engineer/zaid-mushtaq-software-engineer.git
```

## 3. Update README URLs (one-shot)

After the rename propagates, replace the old handle in the profile README:

```bash
sed -i 's/zaid-mushtaq-data-engineer/zaid-mushtaq-software-engineer/g' README.md
git add README.md && git commit -m "chore: point profile links at new GitHub username" && git push
```

Then set the GitHub badge link to `https://github.com/zaid-mushtaq-software-engineer` (the badge label already shows `zaid-mushtaq-software-engineer`).

## 4. Optional: rename via CLI (instead of step 1 UI)

```bash
gh auth refresh -h github.com -s user
gh api -X PATCH user -f login='zaid-mushtaq-software-engineer'
```

## 5. Other places to check

- **Fine-grained PAT / `GH_STATS_TOKEN`**: still valid; no change unless tied to a deleted token.
- **Repository clones**: `git remote -v` on KINNOTE, redis-engineering-lab, etc. — GitHub redirects, but updating remotes avoids confusion.
- **LinkedIn / email signatures**: point to `https://github.com/zaid-mushtaq-software-engineer` when ready.

## Statistics widgets (why they broke)

The previous README used `github-readme-stats.vercel.app`, `github-readme-activity-graph.vercel.app`, and `github-readme-streak-stats.demolab.com`. Those endpoints were returning **402/503** or timing out.

The profile README now uses:

| Section | Source |
|---------|--------|
| Contribution activity | `github.com/users/…/contributions` (GitHub-hosted) |
| Stats | `github-profile-summary-cards.vercel.app` |
| Streak | `streak-stats.demolab.com` |

After username rename, update the `user=` / `username=` parameters in `README.md` as in step 3.
