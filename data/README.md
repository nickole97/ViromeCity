# data/

Source of truth for anything the book's figures read. Edit here, not in the
generated file.

## studies.csv — the reading list behind the sampling map

One row per paper. `quarto render` folds it into `components/sampling-map.html`;
**you never edit that file by hand.**

---

## Adding a paper — the whole procedure

**1. Open `data/studies.csv`.** Any text editor. Numbers and Excel also work —
if you use one, save as CSV, not as `.numbers` or `.xlsx`.

**2. Add one row at the bottom.** Copy an existing row and change it rather than
typing a new one from scratch — it is the easiest way to get the commas right.

```
copsac2023,yes,DK,2023,gut,647 one-year-olds,Viral diversity in the healthy infant gut (COPSAC),https://doi.org/10.1038/s41564-023-01345-7
```

**3. Set `verified` honestly.** `no` if you have not opened the paper and checked
it against the row. A `no` row does not reach the published map; it waits in the
CSV. Nothing is lost, and nothing unchecked ships.

**4. Run `quarto render`.** It will print one of two things:

```
sync-map-studies: 18 studies across 17 countries
```

or, if something is wrong, the line number and the reason — and it will refuse
to rebuild the map rather than publish something quietly broken.

**4b. Fill the titles.** Leave `title` blank when you add a row — this fetches
the published title from CrossRef, so nobody transcribes one by hand and nobody
transcribes one wrong:

```bash
python3 scripts/fetch-titles.py          # fill blanks
python3 scripts/fetch-titles.py --check  # just report which rows are missing one
```

**5. Check it.** `verify-references` resolves every DOI and confirms the record
matches the row:

```bash
python3 ~/.claude/skills/verify-references/verifier.py verify data/references.json
```

`data/references.json` is generated from the CSV by the same render, so it can
never drift. `VERIFIED` means the DOI resolves *and* the title and year match.
`MISMATCH` means the DOI is real but points at a different paper — the failure
that bit us once already.

The skill is Scott's: <https://github.com/shandley/washu-claude-skills>.

**6. Commit and push.** `git add data/studies.csv data/references.json components/sampling-map.html docs`
then commit and push. Both the CSV and the rebuilt map need to go, since the map
is what the site serves.

---

## The columns

| column | what goes in it |
|---|---|
| `id` | short slug, unique. `author + year` is the convention: `shkoporov2019`. Where there is no obvious first author to name — a consortium, a report — use `place + topic`: `ethiopia_amhara`, `china_vaginitis` |
| `verified` | `yes` or `no` — see below |
| `countries` | ISO-3166 **alpha-2**, `;`-separated for multi-country studies: `CN;PK` |
| `year` | year of **publication**, not of sample collection |
| `site` | `gut`, `vaginal`, `blood`, `gut, oropharynx` … |
| `n` | as the paper states it, **with its unit**: `647 one-year-olds`, `12 samples`, `587 pooled samples`. "40" alone is not useful — forty what? |
| `label` | what the reader sees in the map panel. A short faithful version of the title is fine |
| `title` | the **exact published title**, as the DOI resolves it. This is what makes the row machine-checkable — do not paraphrase it |
| `url` | DOI link, or a PMC/PubMed link if there is no DOI |

### Commas: the one thing that breaks the file

This is CSV, so a comma inside a field must be wrapped in double quotes.

```
✗ nishijima2022,yes,JP,2022,gut,4,198 individuals,Gut dsDNA virome …
✓ nishijima2022,yes,JP,2022,gut,"4,198 individuals",Gut dsDNA virome …
```

It bites most often in `n` (thousands separators) and in `label` (subtitles after
a comma). Numbers and Excel add the quotes for you; a text editor does not. If a
row looks right but the render complains about the wrong number of columns, this
is why.

### The country is where the samples came from

Not where the authors work. A Boston group publishing on a Malawian cohort is
`MW`. **This is the field most likely to be wrong and the only one the script
cannot check for you** — it can tell that `XX` is not a country, but not that a
study you labelled `US` actually sampled in Peru.

Multi-country studies are listed under each: `US;IT;TZ;PE` puts the paper in
four countries' panels.

### verified

`no` means nobody has resolved the identifier and read the record. **A row marked
`no` does not appear on the published map** — it stays in the CSV and
`quarto render` names it as held back.

This is not bureaucracy. Of the first seventeen rows, three were wrong: one
carried the title and year of one paper and the DOI of a *different* paper from
the same cohort, so a reader clicking through would have landed somewhere other
than where they were sent.

**To verify a row:** run `verify-references` (step 5) — it checks the title and
the year for you. Then check by hand what it cannot: the authors, the journal,
the sample count, and — above all — **the country the samples came from**. Then set `verified` to `yes` and add a line to
`_incoming/tabla-muestreo-virome.md` saying what you found. The record of the
first pass is there and is the model to follow.

### What adding rows does and does not change

It adds papers to the panel that opens when a reader clicks a country. **It does
not change the map's colouring.** The shading comes from a measured dataset
(Abdill, Adamowicz & Blekhman, *PLOS Biology* 2022) and is not ours to move.
Changing the shading would mean recomputing the index from virome-specific
sample metadata — a different job, described at the top of
`_incoming/tabla-muestreo-virome.md`.

So sixteen countries currently show a paper and 235 are drawn. Adding rows is how
that gap closes.

### If the build fails

The script refuses to rebuild the map rather than shipping a broken one, and
prints the CSV line number with the reason. The four it catches:

| message | what to do |
|---|---|
| `9 fields, expected 8 — a comma inside a field must be wrapped in double quotes` | the comma problem above |
| `missing column(s) …` | the row is short; count the commas |
| `has no url` | every row needs a DOI or a PMC/PubMed link |
| `url is not a link` | it must start with `http`. `doi:10.1234/x` is an identifier, not a link — write `https://doi.org/10.1234/x` |
| `'XX' is not a country on the map` | wrong or mistyped alpha-2 code |
| `duplicate id` | two rows share an `id`; make one unique |
| `verified must be yes or no` | a typo, or a blank cell |

`quarto render` stops on any of these. It does not half-build: the map on disk
stays the last good one until the CSV is fixed.

---

## Rows added by Claude Cowork

Cowork can be scheduled to search the literature monthly and append rows here —
the task is `_incoming/tarea-cowork-papers.md`. It writes to `data/` and nothing
else, and it always writes `verified: no`.

That is the whole safety design, and it is not a convention anybody has to
remember: a `no` row cannot reach the published map. Cowork is untrusted input by
construction. It can be wrong about a paper, a country, or a DOI, and a reader
never sees it.

What it hands over still needs a person for the one thing no tool checks — that
the samples came from the country on the row. `fetch-titles.py` and
`verify-references` cover the rest; the country is yours.

It also writes `data/pendientes.md` each run: what it added, what it discarded
and why, and anything it could not resolve. Read that before flipping anything
to `yes`.
