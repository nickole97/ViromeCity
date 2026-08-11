# Virome City — "What's in the sample?" figure set

Handoff for integration. Everything here is self-contained: no build step, no
dependencies, no data fetching. Each figure is a single HTML file with its CSS
and JS inline, plus Google Fonts from CDN.

---

## Where each file goes

| File | Chapter | Section |
|---|---|---|
| `figures/fig1-whats-in-the-sample.html` | Where do viruses hide? | **Why isn't most of it viral?** |
| `figures/fig1-whats-in-the-sample.svg` | same | static fallback (PDF, social, print) |
| `figures/body-heatmap.html` | Where do viruses hide? | **Does it change with the body site?** — replaces the existing component |
| `figures/fig2-what-enrichment-does.html` | How to recover them | **B · Enrich** — replaces the `Plot style in prep` placeholder |

`icons/` holds the four site icons used by fig 1, normalised to a shared
`viewBox="0 0 48 48"` so they are drop-in interchangeable. They are currently
**inlined** in fig 1; the folder is the editable source of truth.

`data/virome-composition-by-site.json` backs the new heatmap variable.

`_archive/` is earlier iterations. Not for production — kept only so design
decisions can be retraced.

---

## Integration notes

**Embed as iframes.** Each figure sets its own `body` background, font stack and
CSS custom properties on `:root`. Dropping the markup straight into the page will
leak variables into the surrounding stylesheet. Iframes with
`loading="lazy"` are the safe path, matching how `body-heatmap.html` is already
embedded.

**Suggested heights:** fig 1 ≈ 900 px, fig 2 ≈ 820 px, heatmap unchanged. All three
reflow below 640 px; fig 2 rotates its arrow and stacks the before/after pair.

**Fonts.** Space Grotesk (display), IBM Plex Sans (body), IBM Plex Mono (data),
loaded per-file from Google Fonts. If the site already self-hosts these, strip the
`<link>` tags and let them inherit.

**Accessibility already handled:** every control is a real `<button>` with
`aria-pressed`, visible focus rings, and `prefers-reduced-motion` disables the bar
transitions. The static SVG carries `<title>` and `<desc>`.

---

## What changed in `body-heatmap.html`

The existing four toggles are untouched. One was added:

- **New fifth variable, `Which viruses`** — phage-dominant ↔ eukaryote-dominant.
  Diverging scale (burnt orange → warm neutral → teal), deliberately unlike the four
  sequential scales already there.
- **Brain and milk render as explicit no-data dots** — white fill, dashed grey
  stroke — because ViroForge has no collection for those compartments. The tooltip
  says so.
- **Throat is flagged as a proxy** (nasopharynx) in its own tooltip.
- **Tooltips on this variable cite a paper** — expected band plus first author, year
  and PMID.

This is the only variable in the figure that returns a citation, which is why the
existing "estimated & schematic" footer under-describes it. Worth revisiting that
caption.

---

## Where the numbers come from

Provenance is mixed on purpose and labelled per value. Nothing here is a direct
measurement of a single cohort.

**Host fraction** — Human Microbiome Project via Marotz et al. 2018, *Microbiome*
(PMID 29482639), which reports % human-aligned reads by sample type with n per site.
Cross-checked against Pereira-Marques et al. 2019, *Front Microbiol*, and the
respiratory depletion study in *Commun Biol* 2024 (`s42003-024-07290-3`).

**Viral fraction, bulk vs enriched** — bioRxiv `2025.10.23.683462`, a VLP method
optimisation study using a synthetic community. Stool 2.4% (bulk DNA-seq) → 63–73%
(protocols VP1–VP3). Saliva 2.1% → 34.8% (VP4). BAL: no viral contigs recovered.
All three comparisons are internal to that study, on common samples — which is why
fig 2 uses it alone rather than mixing sources.

**Phage vs eukaryotic virus per site** — ViroForge's literature layer
(`virome_composition.yaml` + `validation/dossiers/*.json`), extracted into
`data/virome-composition-by-site.json` with PMID and DOI per compartment.

**Dietary DNA in stool** — Diener & Gibbons, *Nat Metab* 2025 (MEDI): food reads are
0.007–1.3% of total reads, detected in 99% of adult samples, varying across three
orders of magnitude between people. This is why diet is **not** a bar in any figure.

**Biomass ordering** — follows the existing heatmap's `biomass` variable, supported
by the recovery failures reported in the bioRxiv study.

---

## Known conflicts, deliberately left visible

These are marked in the figures rather than silently resolved. Do not "fix" them by
picking a side.

1. **Vaginal and skin host fraction.** The figures show the body-compartment
   estimates (`low–med`, `20–50%`); HMP swab data put both above 90%. Marked with †
   and explained in the footnote.
2. **Stool host fraction.** HMP says under 10%; the respiratory depletion paper says
   under 0.5%. The figures use the lower framing (`<1%`).
3. **ViroForge is a model, not a measurement.** Its `contamination_defaults.tsv` is
   expert-set modelling parameters with no per-cell citation, and its viral remainder
   (17.4% for gut) is an artefact of it being a virome generator. It is used **only**
   for the phage-vs-eukaryote layer, which does carry citations.
4. **ViroForge catalogue verdicts.** `catalog_verdict` in the JSON flags skin as
   `NOT PLAUSIBLE` (0% phage observed against an 80–95% expectation), with throat and
   lung as `MISMATCH`. The literature expectations are sound and are what the figure
   draws; the generated data at those sites are not. Three issues worth filing
   upstream.

---

## Design rules these figures follow

- **Cyan `#0891B2` is the virus, everywhere, always.** It is the anchor tying fig 1,
  fig 2 and the heatmap together. Changing it in one place breaks the sequence.
- **Only the virus is saturated in fig 1.** Everything else is warm and muted.
- **No textures in fig 1; textures arrive in fig 2.** The figure gains detail at the
  same moment the method gains signal. Adding pattern fills to fig 1 undoes that.
- **Radial spiky icons are reserved for virions.** Any other icon drawn that way will
  read as a virus.
- **Declared gaps beat invented numbers.** Dashed borders, em dashes and
  `no data` labels are load-bearing, not placeholders.

---

## Still open

- **Fig 2 has no static SVG fallback** — fig 1 has one, fig 2 does not.
- **The skin icon is a hand**, which sits at a different biological scale from the
  colon (organ) and erythrocyte (cell), and can read as "stop". Alternative
  erythrocyte icon for blood is in `icons/blood-alt-erythrocyte.svg` if the
  haemoglobin-style icon ever gets confused with a coccus cluster.
- **Copy errors in the original chapter draft** that these figures do not fix:
  `prtozoans` → protozoans; "Depending the type of sample" → "Depending on the type
  of sample"; inconsistent trailing periods across the panel chips.
- **Blood is the least well-sourced column** in fig 1 — `80–95%` is consistent with
  mNGS literature (~97% plasma, 99.9% whole blood) but does not come from HMP like
  the other three.
- **Icons are inlined**, adding a few KB per figure. If more figures start using
  them, move to a shared sprite or external files and cache once.
