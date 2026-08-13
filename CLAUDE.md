# Virome City — project context

An illustrated guide that walks a researcher from a human-virome sample *idea* to
the analysis. Mixed audience: PhD/postdoc researchers and beginning students.

**Not a book about viromes — a tool for doing virome analysis.** That distinction
decides everything else. A reader arrives with a sample and a question, not to be
taught virology. Explain biology only where it changes what they should do.

**But it is still a book, not documentation.** It is read in order, it has a
narrative arc, and it has a guide character (Fivi, a bacteriophage). Design and
tone decisions should follow from that, not from docs-site conventions.

It will also exist **in print**. Anything that only works on a screen — the sidebar,
the scroll reveal, wide figures — is a screen affordance, not a design decision.

## Chapters are districts

The reader is navigating Virome City, so each chapter is a district: District 1 is
"How should I think about viruses?", and the city is the structure, not a metaphor
sprinkled on top.

**There are five, not four.** "How to recover them" was one chapter until it was
split at Fivi's Kitchen: District 4 is the bench and District 5 is the screen.
They are different trades, done by different people on different days, and one
chapter carrying both was two reading sessions pretending to be one.

**Chapter titles are questions.** Not "What is a virus?" but "How should I think
about viruses?" — a title states the question the reader arrived with, and the
chapter answers it. This applies to every chapter from here on.

The name is **Virome City**. Not "Viral City".

## Stack

Quarto book project. Source `.qmd` at the repo root, rendered output in `docs/`,
served by GitHub Pages from `main` / `/docs`.

`docs/` is **build output**. Never edit it by hand — `quarto render` overwrites it.

## Decisions already made — do not revisit without asking

These were settled deliberately. If something here looks like a mistake, ask
before changing it.

**Light mode only.** No dark mode, no theme toggle.

**The design system is version B of the handoff** (`Portada_Virome_City.zip`,
`Virome-City-Design-System-B.html`), adopted on 2 August. Version A — warm paper,
Fraunces and Nunito Sans, a red voice — was implemented first and rejected: on the
page it read as undifferentiated, because the chapter was written in one register
and three of the six components had no content. B is the cold, scientific
direction. Both are marked high-fidelity, so the values are implemented exactly.

**Colour identifies the type of component, never the chapter.** A reader learns
"cyan is a Figure" once and it holds everywhere. Districts are structural, not
chromatic — they carry no colour of their own.

| Token | Hex | Role |
|---|---|---|
| `--page` / `--paper` | `#ffffff` | lab white; cards are white too, the border separates them |
| `--ink` | `#14213d` | navy — text, headings |
| `--muted` / `--ink-secondary` | `#5c6b82` | captions, metadata, secondary copy |
| `--line` | `#e2e6ec` | card borders and separators |
| `--line-strong` | `#c7cdd7` | dotted borders |
| `--c-figure` (structure) | `#0891b2` | Figure and technical data |
| `--c-question` (voice) | `#e85d4e` | Question, Fivi Note, links |
| `--c-methodology` (method) | `#d99a1b` | Methodology Tip |
| `--c-insight` | `#6c63c9` | Insight, on `#eef0fb` |
| Research Note | `#5c6b82` | neutral, dotted `#c7cdd7`, no accent |

**The shell is navy; the paper is white.** The sidebar and the page footer are
one surface, and they share `--sb-ink #ffffff`, `--sb-ink-soft #9aa8bd`,
`--sb-line #2a3854` and `--sb-rule rgba(255,255,255,.12)` from `:root`. Anything
cyan on that navy uses `--c-figure-on-dark #3fc3de`, not the page cyan: `#0891b2`
reads at 4.34:1 on navy and fails AA at kicker size. The page value is unchanged.

**The footer has two tiers**, because one row reads as a strip and two read as a
close: identity and credit on the first row — both built as a mono kicker over
its text, so they read as a pair — then a hairline, then the colophon. Only the
left kicker is cyan; one accent, not two.

**Three faces, all geometric.** Space Grotesk 500–700 for headings and Fivi's
voice. IBM Plex Sans 400–700 for body and labels. IBM Plex Mono 500 for technical
data and for every kicker: `ssRNA`, `dsDNA`, family names, component labels.

Scale: H1 600 40px, H2 27px, body 400 18px/1.6, kicker 700 11px mono with 1.5px
tracking, technical 500 14px mono.

**Spacing is an 8px scale**, one step below what the handoff specifies. It asks
for 80 / 48 / 32 / 24; the book uses **56 / 40 / 28 / 20**, because at 18px body
an 80px section opening reads as four blank lines and the page felt aired rather
than composed. Same rhythm, less of it — a deliberate departure from the
high-fidelity brief, and the only one. Radius 8px.

*Replaced twice:* first a two-layer scheme where a five-colour figure palette
carried meaning — blue meant *decision* — with a `#3550C9` accent and Spline Sans;
then version A. The retired green `#0F6E56` stays retired.

**The six components.** Question, Figure, Insight, Fivi Note, Methodology Tip,
Research Note. Each has one colour, fixed book-wide. A chapter that uses only one
or two of them will read as flat no matter how good the palette is — that is what
sank version A, and it was a content problem, not a colour one. Figures are
line-art technical diagrams, never photorealistic. Fivi appears only in the margin
of a note, never inside a diagram.

**One stylesheet: `assets/styles.scss`.** No inline `style="..."`, no `<style>`
blocks in chapters. New visual patterns become classes there.

**Images are files.** Never base64. (The legacy `what.html` has Fivi embedded as a
base64 PNG inside its CSS — that is a known defect to fix during migration, not a
pattern to copy.)

**Fivi appears once per screen.** She is a character, not a banner. She speaks in
first person. Her aside block is `::: fivi`. The cover hero is cover-only.

**Fivi is a scientific guide, not comic relief.** She appears only to flag a common
misconception, or an idea readers are likely to underestimate. If an aside is not
correcting something, it should not be Fivi.

**Figures belong to the reading flow**, not to a plate section. They keep their
number (Quarto generates it). The design system asks for a caption on every figure;
the chapter text was written to explain each figure in the prose beside it. Where
both are true, keep the caption short and factual — it names what the figure shows,
it does not re-argue the paragraph.

**Two scaffolding patterns that are not components.** `::: fig-pending` holds the
slot of a figure that is written but not drawn: dashed, colourless, and with **no
figure number** — Quarto numbers real figures, and a placeholder that consumed one
would renumber everything after it when the art lands. `::: launch` is the door to
an interactive that lives on its own page (`components/`, `kitchen/`); it is
bordered and kicked in the figure colour, because being interactive does not make
it a new kind of thing, and its links stay coral like every other link.

## Language

English is the source of truth. Other languages will live in subfolders (`/es/`,
`/pt/`) so English URLs never change.

**Figure labels stay in English in every language.** `capsid`, `dsDNA`, `prophage`
are the vocabulary readers meet in papers and tools. Only prose gets translated —
which is what keeps translation cheap. Do not translate text inside SVGs.

## Figure widths

**Do not use Quarto's `.column-*` classes.** They place an element into Quarto's
page grid, and the moment one appears Quarto stamps `page-columns page-full` on
`<main>` and on every section containing one, spans it screen-start/screen-end with
`!important`, and re-resolves a nested grid inside each section. That put figures on
top of the sidebar, slid the reading column underneath it, and made section
backgrounds unable to contain their own figures. Removing them removed the whole
class of bug.

Width is one class, `.wide`, in ordinary CSS. Anything too wide for the column
becomes its own page, linked from the chapter.

## Not Quarto

`kitchen/` (Fivi's Kitchen wizard) and `components/` (body heatmaps) are
hand-written HTML, declared as `resources` in `_quarto.yml` and copied to the build
untouched. Don't convert them to markdown.

**They stay their own pages, and a chapter shows one in an `<iframe>`** — `::: embed`.
Never inline one: their CSS is global (`body`, `h1`, `:root`), so pasting a widget
into a chapter restyles the chapter. The iframe isolates it completely and still
puts the figure in the reading flow rather than behind a click.

An iframe has no natural height, so each widget measures itself and posts it to the
page (`postMessage`); `assets/embed.js`, wired in through `include-after-body`, sets
it. Each widget also hides its own title and dek when it is not the top-level
document, because the chapter card already carries both. In print the iframe is
hidden and the card falls back to its title, its description and the figure's URL.

`::: launch` is still there for a widget too large to sit in a chapter at all —
Fivi's Kitchen is a whole wizard, not a figure. That one gets a door, not a frame.

**Data a figure reads lives in `data/`, never inside the widget.** The sampling
map's reading list is `data/studies.csv`; `scripts/sync-map-studies.py` folds it
in as a Quarto `pre-render` hook. Nobody hand-edits minified JSON inside a 145 KB
file. Stdlib only, so a fresh clone renders without installing anything, and the
output is byte-stable so an unchanged CSV produces no diff. A row marked
`verified: no` is held back from the published map and named at build time —
three of the first seventeen entries were wrong, so "checked" is a state a row
reaches, not a promise.

The same hook writes `data/references.json`, a manifest for Scott's
`verify-references` skill (<https://github.com/shandley/washu-claude-skills>),
which resolves every DOI and checks the record against the row. `EXISTS` is not
enough — without an expectation anchored to it, the tool can only say an
identifier is real, not that it is the paper claimed. The manifest anchors the
title and the year, which is exactly the failure that occurred. Run it before
publishing new rows. See `data/README.md`.

They cannot import `assets/styles.scss`, so each one **restates the version B
tokens in its own `:root`** — `--paper`, `--ink`, `--muted`, `--line`, `--surface`,
`--accent`, `--purple`, `--coral`, `--star` and the three faces. Change a value in
the stylesheet and change it in all three. Their data ramps use colours the reader
already knows: cyan is what you are looking for, slate is the host it is buried in,
violet is biomass, coral is risk. The active toggle is navy rather than the ramp
colour, because white on the cyan and coral ends reads at 3.7:1 and 3.4:1.

They each carried a `prefers-color-scheme: dark` block. **Removed** — the book is
light only, and a widget that inverted on a dark OS was the one place that broke it.

## Current state

District 1 — "How should I think about viruses?" — is written, migrated and live.
District 3 — "Where do viruses hide?" — is migrated, with one figure still
`fig-pending`. Districts 4 and 5 — the bench and the screen — are migrated from
the old draft, with the pipeline figure pending. **District 2, "Why the virome
matters", is still a three-line stub, and it is the one that tells the reader why
any of the rest matters.** Fivi's Kitchen is a stub too. The hand-written drafts
are in `_archive/sections-html/` and stay published at `/legacy/`.

The three defects the legacy HTML carried are fixed: Fivi is no longer a base64 PNG
inside the CSS, the broken `#how` link resolves to the How-to district, and the
fonts load from the document head.

Cover art and the city motif are still to come. The design system defines the
editorial language; it does not draw the cover.
