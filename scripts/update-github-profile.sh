#!/usr/bin/env bash
set -euo pipefail

# Updates GitHub account header fields (bio, location, company, website/LinkedIn).
# Requires: gh auth refresh -h github.com -s user

LINKEDIN_URL="${LINKEDIN_URL:-https://www.linkedin.com/in/zaid-mushtaq-software-engineer/}"

gh auth refresh -h github.com -s user

gh api -X PATCH user \
  -f name='Zaid Mushtaq' \
  -f bio='Software Developer | Backend Engineering | AI Enthusiast' \
  -f location='Bengaluru, India' \
  -f company='OneBill Software Private Limited' \
  -f blog="$LINKEDIN_URL"

gh api user --jq '{login,name,bio,company,location,blog}'
