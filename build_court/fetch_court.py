#!/usr/bin/env python3
"""Build court/puzzles.js from the Supreme Court Database (SCDB).

Every justice's vote comes from SCDB (scdb.wustl.edu) justice-centered data —
nothing hand-entered. Puzzle definitions (in batches/court_batch_*.py) supply
the case framing: a yes/no question and which way the majority answered it;
this script maps each justice's verified majority/dissent membership onto that
answer and fails loudly on any mismatch.

Usage:
  python3 fetch_court.py                      # full build -> court/puzzles.js
  python3 fetch_court.py batches/<file>.py    # dry-run verify one batch
"""
import csv
import importlib.util
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "build_court" / "cache"
OUT = ROOT / "court"
PHOTOS = OUT / "photos"
SCDB_CSV = CACHE / "SCDB_2024_01_justiceCentered_Citation.csv"
SCDB_URL = ("http://scdb.wustl.edu/_brickFiles/2024_01/"
            "SCDB_2024_01_justiceCentered_Citation.csv.zip")

UA = {"User-Agent": "yea-or-nay-court-builder/1.0 (personal project)"}

# Appointing president and party, keyed by SCDB justiceName. Public record
# (Federal Judicial Center); every justice used in a puzzle must appear here.
APPOINTED = {
    "HLBlack":      ("Franklin Roosevelt", "D"),
    "SFReed":       ("Franklin Roosevelt", "D"),
    "FFrankfurter": ("Franklin Roosevelt", "D"),
    "WODouglas":    ("Franklin Roosevelt", "D"),
    "RHJackson":    ("Franklin Roosevelt", "D"),
    "HHBurton":     ("Truman", "D"),
    "TCClark":      ("Truman", "D"),
    "SMinton":      ("Truman", "D"),
    "EWarren":      ("Eisenhower", "R"),
    "JHarlan2":     ("Eisenhower", "R"),
    "WJBrennan":    ("Eisenhower", "R"),
    "CEWhittaker":  ("Eisenhower", "R"),
    "PStewart":     ("Eisenhower", "R"),
    "BRWhite":      ("Kennedy", "D"),
    "AJGoldberg":   ("Kennedy", "D"),
    "AFortas":      ("Lyndon Johnson", "D"),
    "TMarshall":    ("Lyndon Johnson", "D"),
    "WEBurger":     ("Nixon", "R"),
    "HABlackmun":   ("Nixon", "R"),
    "LFPowell":     ("Nixon", "R"),
    "WHRehnquist":  ("Nixon", "R"),
    "JPStevens":    ("Ford", "R"),
    "SDOConnor":    ("Reagan", "R"),
    "AScalia":      ("Reagan", "R"),
    "AMKennedy":    ("Reagan", "R"),
    "DHSouter":     ("George H. W. Bush", "R"),
    "CThomas":      ("George H. W. Bush", "R"),
    "RBGinsburg":   ("Clinton", "D"),
    "SGBreyer":     ("Clinton", "D"),
    "JGRoberts":    ("George W. Bush", "R"),
    "SAAlito":      ("George W. Bush", "R"),
    "SSotomayor":   ("Obama", "D"),
    "EKagan":       ("Obama", "D"),
    "NMGorsuch":    ("Trump", "R"),
    "BMKavanaugh":  ("Trump", "R"),
    "ACBarrett":    ("Trump", "R"),
    "KBJackson":    ("Biden", "D"),
}


def load_scdb():
    if not SCDB_CSV.exists():
        raise SystemExit(f"SCDB csv missing — download {SCDB_URL} and unzip into {CACHE}")
    by_case = {}
    for r in csv.DictReader(open(SCDB_CSV, encoding="latin-1")):
        by_case.setdefault(r["caseId"], []).append(r)
    return by_case


def load_batches(single=None):
    justices, puzzles = {}, []
    paths = ([Path(single)] if single
             else sorted((ROOT / "build_court" / "batches").glob("court_batch_*.py")))
    for path in paths:
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for k, v in getattr(mod, "JUSTICES_EXTRA", {}).items():
            if k in justices and justices[k] != v:
                raise SystemExit(f"justice key conflict '{k}' in {path.name}")
            justices[k] = v
        puzzles.extend(mod.PUZZLES)
    return justices, puzzles


def fetch_photo(key, wiki_title, problems):
    """Resolve a portrait via the Wikipedia page-summary API (registry stores the
    page title, e.g. 'Antonin Scalia', not a raw file URL)."""
    import time
    dest = PHOTOS / f"{key}.jpg"
    if dest.exists() and dest.stat().st_size > 5000:
        return
    last_err = None
    for attempt in range(3):
        time.sleep(1.2)
        try:
            api = ("https://en.wikipedia.org/api/rest_v1/page/summary/"
                   + urllib.parse.quote(wiki_title.replace(" ", "_")))
            req = urllib.request.Request(api, headers=UA)
            meta = json.loads(urllib.request.urlopen(req, timeout=30).read())
            src = (meta.get("thumbnail") or {}).get("source")
            if not src:
                problems.append(f"photo {key}: no image on wiki page '{wiki_title}'")
                return
            src = src.replace("/320px-", "/480px-")
            req = urllib.request.Request(src, headers=UA)
            data = urllib.request.urlopen(req, timeout=30).read()
            if len(data) < 5000 or not (data[:2] == b"\xff\xd8" or data[:8].startswith(b"\x89PNG")):
                problems.append(f"photo {key}: not a usable image ({len(data)}b)")
                return
            dest.write_bytes(data)
            return
        except Exception as e:  # noqa: BLE001
            last_err = e
            if "429" in str(e):
                time.sleep(8)
                continue
            break
    problems.append(f"photo {key}: {last_err}")


def main() -> int:
    single = sys.argv[1] if len(sys.argv) > 1 else None
    dry = single is not None
    scdb = load_scdb()
    justices, puzzles = load_batches(single)
    if not dry:
        # deterministic era-interleave, with a marquee case pinned to day 1
        import hashlib
        pin = [p for p in puzzles if p["id"] == "texas-v-johnson"]
        rest = sorted((p for p in puzzles if p["id"] != "texas-v-johnson"),
                      key=lambda p: hashlib.md5(p["id"].encode()).hexdigest())
        puzzles = pin + rest
    problems = []
    seen_ids = set()
    out = {"gameName": "Yea or Nay: Split Decision", "epoch": "2026-08-12", "puzzles": []}

    for pz in puzzles:
        if pz["id"] in seen_ids:
            problems.append(f"duplicate puzzle id {pz['id']}")
        seen_ids.add(pz["id"])
        rows = scdb.get(pz["scdb"])
        print(f"\n=== {pz['caseTitle']} ({pz['era']}) ===")
        if not rows:
            problems.append(f"{pz['id']}: SCDB caseId '{pz['scdb']}' not found")
            continue
        r0 = rows[0]
        split = f"{r0['majVotes']}–{r0['minVotes']}"
        try:
            decided = datetime.strptime(r0["dateDecision"], "%m/%d/%Y").strftime("%B %-d, %Y")
        except ValueError:
            decided = r0["dateDecision"]
        ans, opp = pz["answer"], ("no" if pz["answer"] == "yes" else "yes")
        if ans not in ("yes", "no"):
            problems.append(f"{pz['id']}: answer must be yes/no")
            continue

        scdb_votes, nonvoters = {}, set()
        for r in rows:
            if r["majority"] == "2":
                scdb_votes[r["justiceName"]] = ans
            elif r["majority"] == "1":
                scdb_votes[r["justiceName"]] = opp
            else:
                # empty/other codes = did not participate (recusal etc.) — fine
                # as long as the puzzle doesn't list this justice
                nonvoters.add(r["justiceName"])

        p_out = {"id": pz["id"], "era": pz["era"], "caseTitle": pz["caseTitle"],
                 "question": pz["question"], "desc": pz["desc"], "intro": pz["intro"],
                 "decided": decided, "split": split, "answer": ans,
                 "justices": [], "votes": {}}
        listed = set()
        for key, blurb in pz["justices"]:
            scdb_name, display, url = justices[key]
            listed.add(scdb_name)
            if scdb_name in nonvoters:
                problems.append(f"{pz['id']}: {display} did not participate in this "
                                f"case — remove them from this puzzle's justices")
                continue
            if scdb_name not in scdb_votes:
                problems.append(f"{pz['id']}: {display} not among this case's voters "
                                f"(wrong bench?) — remove from this puzzle")
                continue
            if scdb_name not in APPOINTED:
                problems.append(f"{pz['id']}: no APPOINTED entry for {scdb_name}")
                continue
            pres, party = APPOINTED[scdb_name]
            p_out["justices"].append({"key": key, "name": display,
                                      "meta": f"{pres} appointee ({party})",
                                      "blurb": blurb, "photo": f"photos/{key}.jpg"})
            p_out["votes"][key] = scdb_votes[scdb_name]
            print(f"  {display:22s} {scdb_votes[scdb_name]}")
        extra = set(scdb_votes) - listed
        if extra:
            problems.append(f"{pz['id']}: case has voters not in the puzzle: {sorted(extra)}")
        print(f"  -> held {ans.upper()}, {split}, decided {decided}")
        out["puzzles"].append(p_out)

    print("\n=== Photos ===")
    needed = {k for pz in puzzles for k, _ in pz["justices"]}
    for key in sorted(needed):
        fetch_photo(key, justices[key][2], problems)
        print(f"  {key}: {'ok' if (PHOTOS / (key + '.jpg')).exists() else 'MISSING'}")

    if not dry:
        (OUT / "puzzles.js").write_text(
            "window.COURT_DATA = " + json.dumps(out) + ";")
        print(f"\nWrote {OUT / 'puzzles.js'} ({len(out['puzzles'])} cases)")

    if problems:
        print("\n!!! PROBLEMS !!!")
        for p in problems:
            print(" -", p)
        return 1
    print("All votes verified against SCDB.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
