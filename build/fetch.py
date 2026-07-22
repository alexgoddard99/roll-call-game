#!/usr/bin/env python3
"""Build web/puzzles.json from official roll-call records.

Two verified sources:
  - senate.gov roll-call XML (101st Congress, 1989 -> present), the default
  - voteview.com roll-call CSVs (pre-1989), for bills marked "source": "voteview"

Downloads each roll-call vote named in puzzles_source.py, extracts the real
vote cast by each featured senator, and emits the game data file. Also
downloads member photos from bioguide.congress.gov.

Every answer in the game comes from this pipeline — nothing is hand-entered.

Usage:
  python3 fetch.py                 # full build -> web/puzzles.json + puzzles.js
  python3 fetch.py batches/b1.py   # dry-run verify a batch module (no web writes)
"""
import csv
import importlib.util
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date as _date
from pathlib import Path

from puzzles_source import SENATORS, PUZZLES

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "build" / "cache"
WEB = ROOT / "web"
PHOTOS = WEB / "photos"

VOTE_URL = ("https://www.senate.gov/legislative/LIS/roll_call_votes/"
            "vote{c}{s}/vote_{c}_{s}_{n:05d}.xml")
VOTEVIEW_URL = "https://voteview.com/static/data/out/{kind}/S{c:03d}_{kind2}.csv"
PHOTO_URL = "https://bioguide.congress.gov/photo/{letter}/{bioguide}.jpg"

UA = {"User-Agent": "yea-or-nay-game-builder/1.0 (personal project)"}

# senate.gov vote_cast values -> game marks ("Guilty" appears in impeachment trials)
CAST_XML = {"Yea": "yea", "Nay": "nay", "Guilty": "yea", "Not Guilty": "nay"}
# voteview cast_code -> game marks (2-5 are paired/announced positions)
CAST_VV = {"1": "yea", "2": "yea", "3": "yea", "4": "nay", "5": "nay", "6": "nay"}
VV_SOFT = {"2", "3", "4", "5"}
VV_NOTE = ("Position recorded by announcement or pairing rather than a floor "
           "vote — the Congressional Record counts it as a {side}.")


def get(url: str, dest: Path, binary: bool = False) -> bytes:
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_bytes()
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    dest.write_bytes(data)
    time.sleep(0.5)  # be polite to senate.gov
    return data


def parse_vote(xml_bytes: bytes) -> dict:
    root = ET.fromstring(xml_bytes)
    members = {}
    for m in root.iter("member"):
        last = (m.findtext("last_name") or "").strip()
        state = (m.findtext("state") or "").strip()
        members[(last, state)] = {
            "cast": (m.findtext("vote_cast") or "").strip(),
            "party": (m.findtext("party") or "").strip(),
        }
    count = root.find("count")
    return {
        "date": (root.findtext("vote_date") or "").split(",  ")[0].strip(),
        "question": (root.findtext("vote_question_text") or "").strip(),
        "result": (root.findtext("vote_result") or "").strip(),
        "yeas": int(count.findtext("yeas") or 0) if count is not None else 0,
        "nays": int(count.findtext("nays") or 0) if count is not None else 0,
        "members": members,
    }


def fetch_voteview(congress: int) -> dict:
    """Load voteview rollcalls/members/votes for one congress (cached)."""
    files = {}
    for kind in ("rollcalls", "members", "votes"):
        dest = CACHE / f"vv_S{congress:03d}_{kind}.csv"
        get(VOTEVIEW_URL.format(kind=kind, kind2=kind, c=congress), dest)
        files[kind] = dest
    rolls = {int(r["rollnumber"]): r
             for r in csv.DictReader(open(files["rollcalls"], encoding="utf-8"))}
    icpsr_by_bioguide = {}
    for m in csv.DictReader(open(files["members"], encoding="utf-8")):
        if m.get("bioguide_id"):
            icpsr_by_bioguide[m["bioguide_id"]] = m["icpsr"]
    casts = {}  # (rollnumber, icpsr) -> cast_code
    for v in csv.DictReader(open(files["votes"], encoding="utf-8")):
        casts[(int(v["rollnumber"]), v["icpsr"])] = v["cast_code"]
    return {"rolls": rolls, "icpsr": icpsr_by_bioguide, "casts": casts}


def pretty_vv_date(iso: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    return _date(y, m, d).strftime("%B %-d, %Y")


def resolve_bill_votes(bill, sen_keys, senators, vv_cache):
    """Return (b_out, problems) for one bill from the appropriate source."""
    problems = []
    overrides = bill.get("overrides", {})
    b_out = {
        "name": bill["name"], "desc": bill["desc"],
        "votes": {}, "notes": {},
    }
    if bill.get("labels"):
        b_out["labels"] = bill["labels"]

    if bill.get("source") == "voteview":
        c, n = bill["congress"], bill["roll"]
        vv_cache.setdefault(c, None)
        if vv_cache[c] is None:
            vv_cache[c] = fetch_voteview(c)
        vv = vv_cache[c]
        r = vv["rolls"][n]
        b_out.update({
            "date": pretty_vv_date(r["date"]),
            "question": bill.get("question", (r.get("vote_question") or "On the Question").strip()),
            "result": bill.get("result") or (r.get("vote_result") or "").strip()
                      or ("Agreed to" if int(r["yea_count"]) > int(r["nay_count"]) else "Rejected"),
            "yeas": int(r["yea_count"]), "nays": int(r["nay_count"]),
        })
        for key in sen_keys:
            bioguide, name, party, state = senators[key]
            icpsr = vv["icpsr"].get(bioguide)
            code = vv["casts"].get((n, icpsr)) if icpsr else None
            if icpsr is None or code is None:
                problems.append(f"{bill['name']}: {name} not found in voteview roll {c}/{n}")
                continue
            mark = CAST_VV.get(code)
            if mark is None and key in overrides:
                mark, note = overrides[key]
                b_out["notes"][key] = note
            elif mark is None:
                problems.append(f"{bill['name']}: {name} voteview cast_code '{code}'")
            elif code in VV_SOFT and key not in b_out["notes"]:
                b_out["notes"][key] = VV_NOTE.format(side=mark.capitalize())
            b_out["votes"][key] = mark
        return b_out, problems

    c, s, n = bill["congress"], bill["session"], bill["vote"]
    cache_file = CACHE / f"vote_{c}_{s}_{n:05d}.xml"
    data = get(VOTE_URL.format(c=c, s=s, n=n), cache_file)
    v = parse_vote(data)
    b_out.update({
        "date": v["date"], "question": bill.get("question", v["question"]),
        "result": bill.get("result", v["result"]),
        "yeas": v["yeas"], "nays": v["nays"],
    })
    for key in sen_keys:
        bioguide, name, party, state = senators[key]
        last = name.split()[-1]
        rec = v["members"].get((last, state))
        if rec is None:
            problems.append(f"{bill['name']}: {name} ({state}) NOT FOUND in roll call")
            continue
        cast = rec["cast"]
        mark = CAST_XML.get(cast)
        if mark is None and key in overrides:
            mark, note = overrides[key]
            b_out["notes"][key] = note
        elif mark is None:
            problems.append(f"{bill['name']}: {name} cast '{cast}'")
        b_out["votes"][key] = mark
    return b_out, problems


def load_batch(path: str):
    spec = importlib.util.spec_from_file_location("batch", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    senators = dict(SENATORS)
    senators.update(getattr(mod, "SENATORS_EXTRA", {}))
    return senators, mod.PUZZLES


def main() -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    PHOTOS.mkdir(parents=True, exist_ok=True)
    problems = []
    out = {"gameName": "Yea or Nay", "epoch": "2026-07-08", "puzzles": []}

    dry_run = len(sys.argv) > 1
    if dry_run:
        senators_all, puzzles_all = load_batch(sys.argv[1])
    else:
        # base puzzles keep their rotation slots; batch packs are appended in a
        # deterministic id-hash order so eras interleave day to day
        import hashlib
        senators_all = dict(SENATORS)
        puzzles_all = list(PUZZLES)
        extra = []
        for path in sorted((ROOT / "build" / "batches").glob("batch_*.py")):
            b_sens, b_puzzles = load_batch(str(path))
            for k, v in b_sens.items():
                if k in senators_all and senators_all[k] != v:
                    raise SystemExit(f"senator key conflict '{k}': {senators_all[k]} vs {v} ({path.name})")
                senators_all[k] = v
            extra.extend(b_puzzles)
        seen = {p["id"] for p in puzzles_all}
        for p in extra:
            if p["id"] in seen:
                raise SystemExit(f"duplicate puzzle id: {p['id']}")
            seen.add(p["id"])
        extra.sort(key=lambda p: hashlib.md5(p["id"].encode()).hexdigest())
        puzzles_all += extra
    vv_cache = {}

    for pz in puzzles_all:
        print(f"\n=== {pz['title']} ({pz['era']}) ===")
        sen_keys = [k for k, _ in pz["senators"]]
        p_out = {
            "id": pz["id"],
            "title": pz["title"],
            "era": pz["era"],
            "intro": pz["intro"],
            "senators": [],
            "bills": [],
        }
        for key, blurb in pz["senators"]:
            bioguide, name, party, state = senators_all[key]
            p_out["senators"].append({
                "key": key, "name": name, "party": party, "state": state,
                "blurb": blurb, "photo": f"photos/{bioguide}.jpg",
            })

        for bill in pz["bills"]:
            b_out, bill_problems = resolve_bill_votes(bill, sen_keys, senators_all, vv_cache)
            problems.extend(f"{pz['id']}/{p}" for p in bill_problems)
            print(f"  {bill['name']}  [{b_out['result']} {b_out['yeas']}-{b_out['nays']}]  ({b_out['date']})")
            for key in sen_keys:
                mark = b_out["votes"].get(key)
                note = " (note)" if key in b_out["notes"] else ""
                print(f"    {senators_all[key][1]:26s} {mark or '*** PROBLEM ***'}{note}")
            p_out["bills"].append(b_out)
        out["puzzles"].append(p_out)

    # Photos
    print("\n=== Photos ===")
    needed = {senators_all[k][0] for pz in puzzles_all for k, _ in pz["senators"]}
    for bioguide in sorted(needed):
        dest = PHOTOS / f"{bioguide}.jpg"
        try:
            data = get(PHOTO_URL.format(letter=bioguide[0], bioguide=bioguide), dest, binary=True)
            if not data.startswith(b"\xff\xd8"):
                dest.unlink(missing_ok=True)
                problems.append(f"photo {bioguide}: not a JPEG")
                print(f"  {bioguide}: BAD CONTENT")
            else:
                print(f"  {bioguide}: ok ({len(data)//1024} KB)")
        except Exception as e:  # noqa: BLE001
            problems.append(f"photo {bioguide}: {e}")
            print(f"  {bioguide}: FAILED {e}")

    if not dry_run:
        (WEB / "puzzles.json").write_text(json.dumps(out, indent=1))
        (WEB / "puzzles.js").write_text("window.ROLLCALL_DATA = " + json.dumps(out) + ";")
        print(f"\nWrote {WEB / 'puzzles.json'} and puzzles.js")

    if problems:
        print("\n!!! PROBLEMS !!!")
        for p in problems:
            print(" -", p)
        return 1
    print("All votes verified Yea/Nay for all featured senators.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
