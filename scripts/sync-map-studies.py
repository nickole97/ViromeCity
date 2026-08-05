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
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "studies.csv"
MAP_PATH = ROOT / "components" / "sampling-map.html"
MANIFEST_PATH = ROOT / "data" / "references.json"
ISO_PATH = ROOT / "data" / "iso-3166.csv"
PAYLOAD_RE = re.compile(
    r'(<script id="payload" type="application/json">)(.*?)(</script>)', re.S
)


def fail(msg):
    print(f"sync-map-studies: {msg}", file=sys.stderr)
    sys.exit(1)


MONTHS = ("January February March April May June July August September October "
          "November December").split()


def list_last_updated():
    """The date the reading list last changed, from git.

    Deliberately not the build date. A stamp that reads "today" every time the
    site rebuilds tells a reader nothing; what they want to know is when a paper
    was last added. Returns None outside a git checkout, and the map then omits
    the line rather than showing a date it cannot stand behind.
    """
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(CSV_PATH.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        )
    except Exception:
        return None
    stamp = out.stdout.strip()
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", stamp)
    if not m:
        return None
    y, mo, d = (int(x) for x in m.groups())
    return f"{d} {MONTHS[mo - 1]} {y}"


def write_manifest(rows):
    """Emit data/references.json for the verify-references skill.

    The skill can only tell you an identifier *exists* unless something anchors
    an expectation to it. This states one: the DOI must resolve to a record whose
    title matches the title in the CSV, and whose year matches. That turns
    "this DOI is real" into "this DOI is the paper we said it was" — the failure
    that actually bit us, when one row carried the title of one paper and the DOI
    of another from the same cohort.

    Generated, so it can never drift from the CSV. Run:
        python3 ~/.claude/skills/verify-references/verifier.py verify data/references.json
    """
    refs = []
    for row in rows:
        url = (row.get("url") or "").strip()
        m = re.search(r"doi\.org/(10\.[^\s)]+)", url)
        if not m:
            continue
        expected = {}
        title = (row.get("title") or "").strip()
        if title:
            # A distinctive stretch of the real title, not a keyword: substring
            # matching on six words is specific enough to catch a swapped paper
            # and loose enough to survive a publisher's punctuation.
            expected["title_contains"] = " ".join(title.split()[:6]).lower()
        year = (row.get("year") or "").strip()
        if year.isdigit():
            expected["year"] = int(year)
        refs.append({"id": row["id"], "type": "doi", "value": m.group(1), "expected": expected})

    MANIFEST_PATH.write_text(
        json.dumps({"references": refs}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return refs


def main():
    if not CSV_PATH.exists():
        fail(f"missing {CSV_PATH.relative_to(ROOT)}")

    html = MAP_PATH.read_text(encoding="utf-8")
    match = PAYLOAD_RE.search(html)
    if not match:
        fail("no payload block in components/sampling-map.html")
    payload = json.loads(match.group(2))

    # The map arrived with an alpha-2 code only on the 112 countries that have
    # samples in the Abdill dataset; the other 123 were drawn but unnamed, so a
    # paper could not be attached to them. That is backwards for this figure —
    # "no public samples, and here is the one study" is the case most worth
    # showing. Fill the rest from data/iso-3166.csv, joined on the numeric code
    # the boundaries already carry.
    iso = {}
    if ISO_PATH.exists():
        for r in csv.DictReader(ISO_PATH.open(encoding="utf-8")):
            if r["numeric"].isdigit():
                iso[int(r["numeric"])] = r["alpha2"]
    for c in payload["countries"]:
        if not c.get("a2") and c.get("n") in iso:
            c["a2"] = iso[c["n"]]

    known = {c["a2"] for c in payload["countries"] if c.get("a2")}

    # restkey/restval so a row with the wrong number of fields is visible rather
    # than silently shifting every column left. An unquoted comma inside `n` or
    # `label` is the common way that happens, and it used to sail through with
    # the title landing in the url column.
    reader = csv.DictReader(CSV_PATH.open(encoding="utf-8"), restkey="_extra", restval=None)
    fields = reader.fieldnames or []
    rows = list(reader)
    studies, held, errors, seen = [], [], [], set()

    for i, row in enumerate(rows, start=2):  # row 1 is the header
        sid = (row.get("id") or "").strip()
        where = f"{CSV_PATH.name}:{i}"

        if row.get("_extra"):
            errors.append(
                f"{where}: {len(fields) + len(row['_extra'])} fields, expected {len(fields)}"
                " — a comma inside a field must be wrapped in double quotes"
            )
            continue
        missing = [f for f in fields if row.get(f) is None]
        if missing:
            errors.append(f"{where}: missing column(s) {', '.join(missing)}")
            continue

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
        elif not url.startswith("http"):
            errors.append(f"{where}: '{sid}' — url is not a link: '{url[:48]}'")

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

    meta = payload.setdefault("meta", {})
    meta["list_count"] = len(studies)
    updated = list_last_updated()
    if updated:
        meta["list_updated"] = updated
    else:
        meta.pop("list_updated", None)

    # Compact and stable, so an unchanged CSV produces an unchanged file and the
    # map does not churn in git on every render.
    new = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
    rebuilt = html[: match.start(2)] + new + html[match.end(2) :]

    if rebuilt != html:
        MAP_PATH.write_text(rebuilt, encoding="utf-8")

    write_manifest(rows)

    print(f"sync-map-studies: {len(studies)} studies across {len(by_country)} countries")
    if held:
        print(f"sync-map-studies: HELD BACK, not verified — {', '.join(held)}")


if __name__ == "__main__":
    main()
