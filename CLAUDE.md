# Yea or Nay — working rules

## Deployment (IMPORTANT — site has live users)

Never deploy directly to production. Required flow for ALL changes:

1. Deploy to dev first: `npx wrangler pages deploy web --project-name roll-call-game --branch dev`
   → review at https://dev.roll-call-game.pages.dev
2. Wait for the user to explicitly approve the dev preview.
3. Only after approval: commit, push, then deploy production:
   `npx wrangler pages deploy web --project-name roll-call-game --branch main`
   → serves https://playyeaornay.com

Production is Cloudflare Pages project `roll-call-game` (direct upload — git pushes do
NOT auto-deploy). Custom domain playyeaornay.com; zone caching is set to respect
origin headers, so production updates appear within seconds.

## Data pipeline

- Puzzle content: `build/puzzles_source.py` (base) + `build/batches/batch_*.py` (packs).
- Vote answers are NEVER hand-entered — always rebuild via `cd build && python3 fetch.py`
  (verifies every vote against senate.gov XML / voteview.com CSVs; fails loudly on absences).
- Dry-run verify a single pack: `python3 fetch.py batches/<file>.py`.
- The daily edition flips at midnight US Eastern; epoch lives in fetch.py ("epoch" field).
  Don't reorder or rename existing puzzle ids — it shifts the daily rotation.

## Integrations

- Firebase project `yea-or-nay-ff4e1`: Google sign-in, Firestore per-user results
  (rules: users read/write only their own docs), GA4 (G-D9Q2Z66JKG) via cloud.js.
- `web/firebase-config.js` is a publishable client config (safe in repo).
