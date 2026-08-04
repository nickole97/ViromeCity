# data/

Source of truth for anything the book's figures read. Edit here, not in the
generated file.

## studies.csv — the reading list behind the sampling map

One row per paper. Opens in any editor, and in Numbers or Excel if that is
easier. `quarto render` folds it into `components/sampling-map.html`; you never
edit that file by hand.

| column | what goes in it |
|---|---|
| `id` | short slug, unique. `author + year` works: `shkoporov2019` |
| `verified` | `yes` or `no` — see below |
| `countries` | ISO-3166 alpha-2, `;`-separated for multi-country studies: `CN;PK` |
| `year` | year of **publication**, not of sample collection |
| `site` | `gut`, `vaginal`, `blood`, `gut, oropharynx` … |
| `n` | as the paper states it, with its unit: `647 one-year-olds`, `12 samples` |
| `label` | the title, or a short faithful version of it |
| `url` | DOI link, or a PMC/PubMed link if there is no DOI |

### The country is where the samples came from

Not where the authors work. A Boston group publishing on a Malawian cohort is
`MW`. This is the field most likely to be wrong and the one the script cannot
check for you.

### verified

`no` means nobody has resolved the identifier and read the record. **A row
marked `no` does not appear on the published map** — it stays in the CSV and
`quarto render` lists it as held back.

This is not bureaucracy. Of the first seventeen rows, three were wrong: one
carried the title and year of one paper and the DOI of a different one from the
same cohort, so a reader clicking through would have landed somewhere other than
where they were sent. Verifying means opening the identifier and checking the
title, the authors, the journal, the year, the sample count and the country
against the row.

The full record of that pass is in `_incoming/tabla-muestreo-virome.md`.

### What adding rows does and does not change

It adds papers to the panel that opens when a reader clicks a country. **It does
not change the map's colouring.** The shading comes from a measured dataset
(Abdill, Adamowicz & Blekhman, *PLOS Biology* 2022) and is not ours to move.
Changing the shading would mean recomputing the index from virome-specific
sample metadata — a different job.

### If the build fails

The script refuses to rebuild the map rather than shipping a broken one. It
prints the CSV line number and what is wrong: a duplicate id, a missing URL, a
country code that does not exist on the map.
