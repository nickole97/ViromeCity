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

**5. Commit and push.** `git add data/studies.csv components/sampling-map.html docs`
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
| `label` | the title, or a short faithful version of it |
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

**To verify a row:** open the URL and check, against the row, the title, the
authors, the journal, the year of publication, the sample count and — above all —
the country the samples came from. Then set `verified` to `yes` and add a line to
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
