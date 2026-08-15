#!/bin/bash
# Deploy to the DEV environment, including dev-only pages (web-dev/, court-dev/)
# that must never reach production. Production deploys keep using the plain
# `npx wrangler pages deploy web|court --branch main`, which ships only the
# site directory — so the dev-only pages physically cannot leak to prod.
#
# Usage: ./deploy_dev.sh web | court
set -euo pipefail
cd "$(dirname "$0")"

case "${1:-}" in
  web)   SRC=web;   EXTRA=web-dev;   PROJECT=roll-call-game ;;
  court) SRC=court; EXTRA=court-dev; PROJECT=court-yea-or-nay ;;
  *) echo "usage: $0 web|court" >&2; exit 1 ;;
esac

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
cp -R "$SRC"/. "$STAGE"/
[ -d "$EXTRA" ] && cp -R "$EXTRA"/. "$STAGE"/

npx -y wrangler pages deploy "$STAGE" --project-name "$PROJECT" --branch dev
