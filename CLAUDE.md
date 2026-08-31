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

## Kalshi integration (both sites)

- `kalshi-live.js` + `kalshi.css` (in `web/` and mirrored in `court/`): "Presented by
  Kalshi" ticker, featured-market ledger with outcome rows (under the vote button on
  bills/cases, above the share row on the score page) and the midterms-hub CTA.
- **One schedule file: `web/kalshi-schedule.txt`** — one line per ET date
  (`YYYY-MM-DD  EVENT-TICKER  [url]  [| custom question]  # note`); today's line, else
  the latest past line. Append a line and redeploy the senate site; the court worker
  fetches that file from playyeaornay.com (`KALSHI_SCHEDULE_URL`, 5-min cache) and
  serves it as its own `/kalshi-schedule.txt`, so the court needs no redeploy.
  `?kdate=YYYY-MM-DD` previews a day on either site.
- `web/_worker.js` and `court/_worker.js` (Pages advanced-mode workers — all traffic
  passes through them, static assets via `env.ASSETS`) proxy `/api/kalshi?event=…` for
  schedule-listed tickers only, signing requests with the Kalshi API key held as Pages
  secrets `KALSHI_KEY_ID` / `KALSHI_PRIVATE_KEY` (PKCS#8 PEM) on BOTH environments of
  BOTH projects (`roll-call-game`, `court-yea-or-nay`).
- Local key material lives in `kalshikeys/` (gitignored) — never commit it. Retired
  prototype variants are in `kalshi-archive/` (gitignored). Kalshi's market-data
  endpoints reject browser-origin requests and rate-limit unsigned ones, hence the proxy.
- Finding tickers: signed `GET /trade-api/v2/series?category=Elections`, then
  `/events?series_ticker=…&status=open&with_nested_markets=true`.

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
- Firestore security rules live in `firestore.rules` (deploy with
  `firebase deploy --only firestore:rules`; `firebase.json` / `.firebaserc` point at the
  project). Both dev and prod sites share the one Firebase project, so a rules deploy is
  a production change — get approval first.
- Crowd comparison: collection `daily`, one doc per game per day
  (`senate-YYYY-MM-DD`, `court-YYYY-MM-DD`; dev hosts write `senate-dev-…` /
  `court-dev-…`). Flat counters `n`, `s0..s15` (score histogram), `v0..v14`
  (per-vote correct counts; court `v9` = split call), `t1..t30` (current-streak
  histogram, `t30` = 30+). Anyone may read; rules allow only +1 increments, so
  numbers are never hand-edited from a client. Tracking writes went live on prod
  2026-08-31 (silent — no UI); the streak/crowd UI ships separately.
- `web/firebase-config.js` / `court/firebase-config.js` are publishable client
  configs (safe in repo).
- Contact form (playyeaornay.com/contact → agoddard256@gmail.com) and advertise form
  (playyeaornay.com/advertise → afg53@cornell.edu) use formsubmit.co; both activated.
  The Court links to the main site's forms.
