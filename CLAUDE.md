# Yea or Nay — working rules

## Deployment (IMPORTANT — site has live users)

Never deploy directly to production. Required flow for ALL changes:

1. Deploy to dev first: `./deploy_dev.sh web` (senate game) or `./deploy_dev.sh court`
   (The Court). The script stages the site dir plus the dev-only pages in
   `web-dev/` / `court-dev/` (e.g. /tomorrow, which previews tomorrow's puzzle
   with answers) — always use it for dev deploys so those pages stay present.
   → review at https://dev.roll-call-game.pages.dev / https://dev.court-yea-or-nay.pages.dev
2. Wait for the user to explicitly approve the dev preview.
3. Only after approval: commit, push, then deploy production:
   `npx wrangler pages deploy web --project-name roll-call-game --branch main`
   → serves https://playyeaornay.com
   `npx wrangler pages deploy court --project-name court-yea-or-nay --branch main`
   → serves https://court.playyeaornay.com
   Production deploys ship ONLY the site dir — the dev-only pages in
   `web-dev/` / `court-dev/` must never be copied into `web/` or `court/`.

Both sites are Cloudflare Pages projects (`roll-call-game`, `court-yea-or-nay`),
direct upload — git pushes do NOT auto-deploy. Zone caching respects origin
headers, so production updates appear within seconds.

## Data pipeline

- Senate puzzles: `build/puzzles_source.py` (base) + `build/batches/batch_*.py` (packs);
  rebuild via `cd build && python3 fetch.py` (verifies vs senate.gov / voteview.com).
- Court cases: `build_court/batches/court_batch_*.py`; rebuild via
  `cd build_court && python3 fetch_court.py` (verifies vs SCDB).
- Vote answers are NEVER hand-entered — both fetch scripts fail loudly on mismatches.
- Dry-run verify a single pack: `python3 fetch.py batches/<file>.py` (same for court).
- Daily editions flip at midnight US Eastern; epochs live in the fetch scripts.
  Don't reorder or rename existing puzzle ids — it shifts the daily rotation.

## Integrations

- Firebase project `yea-or-nay-ff4e1` serves BOTH games: Google sign-in, Firestore
  per-user results (`results` = senate, `courtResults` = court; rules: users
  read/write only their own docs), GA4 (G-D9Q2Z66JKG) via cloud.js. Court events
  carry `game: "court"`; senate events have no `game` param.
- `web/firebase-config.js` / `court/firebase-config.js` are publishable client
  configs (safe in repo).
- Contact form (playyeaornay.com/contact → agoddard256@gmail.com) and advertise form
  (playyeaornay.com/advertise → afg53@cornell.edu) use formsubmit.co; both activated.
  The Court links to the main site's forms.
