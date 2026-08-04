#!/usr/bin/env python3
"""Fill empty `title` cells in data/studies.csv from CrossRef.

The title is what makes a row machine-checkable: verify-references compares the
DOI's record against it. So it has to be the *published* title, exactly — and the
one source that cannot mistype it is the registry itself.

Which is the point. Whoever adds a row — a person, Cowork, me — leaves `title`
blank. This fills it from the DOI. Nobody transcribes a title by hand, so nobody
can transcribe one wrong, and the check has something real to compare against.

Never overwrites a title that is already there; run it as often as you like.

    python3 scripts/fetch-titles.py            # fill blanks
    python3 scripts/fetch-titles.py --check    # report blanks, change nothing

Stdlib only. Needs network — the one step in this repo that does.
"""

import csv
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "studies.csv"
MAILTO = "nvillabo@uci.edu"          # CrossRef asks for a contact; it buys a faster pool
UA = f"ViromeCity/1.0 (+https://github.com/nickole97/ViromeCity; mailto:{MAILTO})"


def crossref_title(doi):
    req = urllib.request.Request(f"https://api.crossref.org/works/{doi}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        msg = json.loads(r.read())["message"]
    titles = msg.get("title") or []
    return " ".join(titles[0].split()) if titles else ""


def main():
    check_only = "--check" in sys.argv
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    if not rows:
        print("fetch-titles: no rows"); return

    if "title" not in rows[0]:
        print("fetch-titles: data/studies.csv has no `title` column", file=sys.stderr)
        sys.exit(1)

    blank = [r for r in rows if not (r.get("title") or "").strip()]
    if not blank:
        print("fetch-titles: every row already has a title"); return

    if check_only:
        print(f"fetch-titles: {len(blank)} row(s) without a title: "
              + ", ".join(r["id"] for r in blank))
        return

    filled, failed = 0, []
    for r in blank:
        m = re.search(r"doi\.org/(10\.[^\s)]+)", (r.get("url") or "").strip())
        if not m:
            failed.append((r["id"], "no DOI in url — a PMC or PubMed link cannot be resolved here; "
                                    "convert it with NCBI's ID converter first"))
            continue
        try:
            title = crossref_title(m.group(1))
        except urllib.error.HTTPError as e:
            failed.append((r["id"], f"HTTP {e.code} — the DOI does not resolve at CrossRef"))
            continue
        except Exception as e:
            failed.append((r["id"], f"{type(e).__name__}: {e}"))
            continue
        if not title:
            failed.append((r["id"], "CrossRef has no title for this DOI"))
            continue
        r["title"] = title
        filled += 1
        print(f"  {r['id']}: {title[:88]}")
        time.sleep(0.25)   # polite

    if filled:
        fields = list(rows[0].keys())
        with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader(); w.writerows(rows)

    print(f"fetch-titles: filled {filled}")
    for sid, why in failed:
        print(f"fetch-titles: could not fill '{sid}' — {why}", file=sys.stderr)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
