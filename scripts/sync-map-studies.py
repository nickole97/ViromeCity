#!/usr/bin/env python3
"""Fold data/studies.csv into the sampling map.

The reading list behind components/sampling-map.html is edited as a CSV, not as
JSON inside a 145 KB HTML file. This runs as a Quarto pre-render hook, so the
built map always matches the CSV and nobody has to hand-edit minified JSON.

The map has to stay self-contained — no network at runtime — so the studies are
injected at build time rather than fetched.

Rules it enforces, and why:

  * A study with verified = no does NOT ship. Of the first seventeen entries,
    three were wrong (one pointed at two different papers at once), so "checked"
    is a state a row has to reach, not a promise. Unverified rows stay in the
    CSV and are listed at build time.
  * Country codes must exist on the map. A typo would otherwise attach a paper
    to nothing and fail silently.
  * Ids must be unique and every row needs a URL.

Stdlib only, on purpose: `quarto render` should work on a fresh clone.
"""

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "studies.csv"
MAP_PATH = ROOT / "components" / "sampling-map.html"
PAYLOAD_RE = re.compile(
    r'(<script id="payload" type="application/json">)(.*?)(</script>)', re.S
)


def fail(msg):
    print(f"sync-map-studies: {msg}", file=sys.stderr)
    sys.exit(1)


def main():
    if not CSV_PATH.exists():
        fail(f"missing {CSV_PATH.relative_to(ROOT)}")

    html = MAP_PATH.read_text(encoding="utf-8")
    match = PAYLOAD_RE.search(html)
    if not match:
        fail("no payload block in components/sampling-map.html")
    payload = json.loads(match.group(2))

    known = {c["a2"] for c in payload["countries"] if c.get("a2")}

    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    studies, held, errors, seen = [], [], [], set()

    for i, row in enumerate(rows, start=2):  # row 1 is the header
        sid = (row.get("id") or "").strip()
        where = f"{CSV_PATH.name}:{i}"

        if not sid:
            errors.append(f"{where}: no id")
            continue
        if sid in seen:
            errors.append(f"{where}: duplicate id '{sid}'")
            continue
        seen.add(sid)

        url = (row.get("url") or "").strip()
        if not url:
            errors.append(f"{where}: '{sid}' has no url — a DOI or PMC link is required")

        codes = [c.strip().upper() for c in (row.get("countries") or "").split(";") if c.strip()]
        if not codes:
            errors.append(f"{where}: '{sid}' lists no country")
        for code in codes:
            if code not in known:
                errors.append(f"{where}: '{sid}' — '{code}' is not a country on the map")

        verified = (row.get("verified") or "").strip().lower()
        if verified not in {"yes", "no"}:
            errors.append(f"{where}: '{sid}' — verified must be yes or no, got '{verified}'")
            continue
        if verified == "no":
            held.append(sid)
            continue

        year = (row.get("year") or "").strip()
        studies.append({
            "id": sid,
            "label": (row.get("label") or "").strip(),
            "year": int(year) if year.isdigit() else None,
            "site": (row.get("site") or "").strip() or None,
            "n": (row.get("n") or "").strip() or None,
            "countries_a2": codes,
            "url": url,
        })

    if errors:
        for e in errors:
            print(f"sync-map-studies: {e}", file=sys.stderr)
        fail(f"{len(errors)} problem(s) in {CSV_PATH.relative_to(ROOT)} — map not rebuilt")

    by_country = {}
    for s in studies:
        for code in s["countries_a2"]:
            by_country.setdefault(code, []).append(s["id"])

    payload["studies"] = studies
    for c in payload["countries"]:
        c["papers"] = by_country.get(c.get("a2"), [])

    # Compact and stable, so an unchanged CSV produces an unchanged file and the
    # map does not churn in git on every render.
    new = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
    rebuilt = html[: match.start(2)] + new + html[match.end(2) :]

    if rebuilt != html:
        MAP_PATH.write_text(rebuilt, encoding="utf-8")

    print(f"sync-map-studies: {len(studies)} studies across {len(by_country)} countries")
    if held:
        print(f"sync-map-studies: HELD BACK, not verified — {', '.join(held)}")


if __name__ == "__main__":
    main()
