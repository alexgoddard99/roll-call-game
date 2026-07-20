# Yea or Nay 🏛️

**The daily congressional vote game.** Each day presents a real bill that came
to the U.S. Senate floor, and five senators with short profiles of their
politics. Stamp each senator's ballot **Yea** or **Nay**, then see how the
roll call actually went. Three bills per day, same five senators — 15 votes
to call.

Every answer is a **real recorded vote**, extracted from the official
roll-call XML published by the [United States Senate](https://www.senate.gov/legislative/votes_new.htm).
Portraits come from the Biographical Directory of the U.S. Congress.

## Play locally

Open `web/index.html` in a browser, or:

```sh
cd web && python3 -m http.server 8642
# → http://localhost:8642
```

Add `?p=N` to the URL to play any puzzle in the archive (N = 0–13).

## How it's built

- `build/puzzles_source.py` — puzzle definitions: eras, senator groups,
  hand-written bill context and senator profiles. **No vote answers live here.**
- `build/fetch.py` — downloads each named roll-call vote from senate.gov,
  extracts the featured senators' actual votes, verifies everyone cast a
  Yea/Nay (flagging absences and "present" votes), downloads portraits, and
  emits `web/puzzles.json` + `web/puzzles.js`.

To rebuild the data (e.g. after adding a puzzle):

```sh
cd build && python3 fetch.py
```

The site itself (`web/`) is fully static — no backend, no build step.
Daily puzzle selection is date-based (days since epoch, modulo puzzle count),
and progress is saved in `localStorage`.

## Current puzzle bank

| Era | Title | Bills |
|---|---|---|
| 111th · 2009–10 | The Obama Wave | ACA · Dodd-Frank · DADT repeal |
| 107th · 2001–02 | After September 11 | PATRIOT Act · No Child Left Behind · Iraq AUMF |
| 110th · 2007–08 | The Class of 2008 | Minimum wage · Iraq funding · TARP |
| 113th · 2013 | Guns & Borders | Manchin-Toomey · Gang of Eight · Shutdown deal |
| 115th · 2017–18 | Three Votes to Lose | Skinny repeal · Trump tax cuts · Kavanaugh |
| 103rd · 1993 | November 1993 | Assault weapons ban · Brady Bill · NAFTA |
| 102nd · 1991 | Line in the Sand | Gulf War · Clarence Thomas · Civil Rights Act of 1991 |
| 104th · 1996 | The Republican Revolution | Welfare reform · DOMA · Minimum wage |
| 105th–106th · 1997–2000 | America & the World | Chemical weapons treaty · NATO expansion · China trade |
| 108th · 2003 | The Bush Majority | Partial-birth ban · $87B for Iraq · Medicare Part D |
| 109th · 2005–06 | Second-Term Blues | Bankruptcy bill · Secure Fence · Military Commissions |
| 112th · 2011–12 | The Tea Party Senate | Debt-ceiling deal · VAWA · Buffett Rule |
| 116th · 2020 | Election Year Fever | USMCA · Iran war powers · Amy Coney Barrett |
| 117th · 2021–22 | The Fifty-Fifty Senate | American Rescue Plan · Infrastructure · Respect for Marriage |
