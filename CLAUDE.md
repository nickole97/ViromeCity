# Virome City — project context

An illustrated guide that walks a researcher from a human-virome sample *idea* to
the analysis. Mixed audience: PhD/postdoc researchers and beginning students.

**This is a book, not documentation.** It is read in order, it has a narrative arc,
and it has a guide character (Fivi, a bacteriophage). Design and tone decisions
should follow from that, not from docs-site conventions.

## Stack

Quarto book project. Source `.qmd` at the repo root, rendered output in `docs/`,
served by GitHub Pages from `main` / `/docs`.

`docs/` is **build output**. Never edit it by hand — `quarto render` overwrites it.

## Decisions already made — do not revisit without asking

These were settled deliberately. If something here looks like a mistake, ask
before changing it.

**Light mode only.** No dark mode, no theme toggle. The figure palette is yellow,
pink and lavender; it does not survive inversion, and there is no dark yellow that
still reads as yellow. Maintaining two palettes is not worth it.

**Two colour layers, and they never mix.**
- *Page layer* — `--ink`, `--muted`, `--line`, `--accent` (`#3550C9`). Text, links,
  rules, navigation.
- *Figure layer* — `--fig-decision`, `--fig-process`, `--fig-branch`, `--fig-aside`,
  `--fig-output`. **Only ever inside a figure.** Never behind body text, never as a
  section background, never in the nav.

Every figure colour has a paired ink (`--fig-process-ink` etc.). Use the pair.
Never black on yellow or on pink.

The accent is blue because it is the only colour in the palette dark enough to
work as link text, and because blue means *decision* in the figures — which is the
thesis of the book. The old green `#0F6E56` was retired; don't reintroduce it.

**Body text is sans** (Spline Sans); headings are serif (Fraunces). Since the body
is sans, the "book" feeling comes from measure, leading and whitespace — roughly
680px column, 17.5px, line-height 1.65. Don't tighten these to fit more on screen.

**One stylesheet: `assets/styles.scss`.** No inline `style="..."`, no `<style>`
blocks in chapters. New visual patterns become classes there.

**Images are files.** Never base64. (The legacy `what.html` has Fivi embedded as a
base64 PNG inside its CSS — that is a known defect to fix during migration, not a
pattern to copy.)

**Fivi appears once per screen.** She is a character, not a banner. She speaks in
first person. Her aside block is `::: fivi`. The cover hero is cover-only.

## Language

English is the source of truth. Other languages will live in subfolders (`/es/`,
`/pt/`) so English URLs never change.

**Figure labels stay in English in every language.** `capsid`, `dsDNA`, `prophage`
are the vocabulary readers meet in papers and tools. Only prose gets translated —
which is what keeps translation cheap. Do not translate text inside SVGs.

## Figure widths

The reading column is deliberately narrow; wide figures break out of it.

| Figure | Class |
|---|---|
| Small diagrams, virion anatomy | *(default)* |
| Classification cards, gene-content matrix | `.column-body-outset` |
| Decision tree, body heatmap | `.column-page` |
| Fivi's asides, side notes | `.column-margin` |

Decide the width when migrating a figure, not afterwards — retrofitting means
reworking every chapter.

## Not Quarto

`kitchen/` (Fivi's Kitchen wizard) and `components/` (body heatmaps) are
hand-written HTML, declared as `resources` in `_quarto.yml` and copied to the build
untouched. Don't convert them to markdown. Heavy interactive widgets live as their
own pages, linked from chapters — not embedded inside them.

## Design identity is deferred on purpose

The Virome City visual identity — watercolor, city-street motif, cover art — is
deliberately postponed until the writing is done, so design serves finished content
instead of forcing it. Don't invent it early.

## Current state

Skeleton and cover are built. The four chapters are stubs. Their real drafts are
the legacy HTML in `_archive/sections-html/`, not yet migrated.

Known defects in the legacy HTML, to fix on migration:
- `what.html` — Fivi embedded as base64 in the CSS; replace with a file reference
- `what.html` — link to `#how` is broken; should point to the How-to chapter
- All legacy pages request Fraunces and Spline Sans but never load them
