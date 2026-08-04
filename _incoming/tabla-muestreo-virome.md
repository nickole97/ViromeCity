# Sampling of the human virome by country — curated table v0

**For:** *Virome City*, ch. 3 "Where do viruses hide?" → "Why is so much of it unclassified?"
**Purpose:** data behind the interactive world map. A reader should find their own
population, see how much of it has been sampled, and click through to the paper.

---

## ⚠ Read this before using the table

**1. This is a curated, non-exhaustive set — not a systematic survey.**
Rows were assembled by hand from the literature. A country with `n_studies: 0`
means *"no study in this curated set"*, **not** *"no study exists"*. Germany, the
UK, the Netherlands, Sweden, Australia and others certainly have published human
virome work that this pass did not catch. The map must say this in plain words,
or it will make a false claim to exactly the reader it is trying to serve.

**2. The load-bearing numbers are the two anchors below, not the row counts.**
The section's argument — *reference databases are built from a handful of
regions, so an under-sampled population yields a larger unclassified fraction* —
rests on the two published aggregate statistics in `anchors`. The per-country
rows are the *browsable* layer that lets a reader locate themselves and reach a
paper. Don't let the ramp imply a precision the curation doesn't have.

**Fix, when you want it:** real per-country counts exist in BioSample/ENA
metadata (this is exactly what Abdill et al. did). That query can't run from my
sandbox — outbound network here is limited to package registries. If you pull the
metadata for virome BioProjects, or hand me an export, I can replace the curated
counts with measured ones and the map becomes a genuine census.

---

## Anchors (the numbers that carry the argument)

| # | Claim | Source |
|---|---|---|
| A1 | Over 71% of public human microbiome samples with a known origin come from Europe, the US and Canada — 46.8% from the US alone, a country holding 4.3% of the world's population. Central and southern Asia (India, Pakistan, Bangladesh and neighbours) hold over a quarter of the world's people but supply 1.8% of samples. Based on 444,829 samples across 2,592 studies and 19 body sites. | Abdill, Adamowicz & Blekhman, *PLOS Biology* 2022. doi:10.1371/journal.pbio.3001536 |
| A2 | Europe, North America and Asia together account for 73.6%–94.5% of the samples behind GPD, MGV, CHVD and GVD — the four major gut virome catalogues. Africa and South America together supply 1.5% of GPD's samples (n = 410). | Li, Yang, Xiao & Li, *Cell Host & Microbe* 2022; 30(7):908–916. doi:10.1016/j.chom.2022.06.003 |

A1 is microbiome-wide (16S + shotgun), not virome-specific — say so. A2 is the
virome-specific version and is the one that speaks directly to *reference*
composition, which is the mechanism the section is about.

---

## Reference catalogues (the databases themselves)

These are what a pipeline actually classifies against. Listed separately from
primary studies because they are aggregations, not sampling events.

| id | catalogue | scope | year | doi |
|---|---|---|---|---|
| `gvd` | Gut Virome Database | 2,697 metagenomes, 1,986 individuals, 16 countries → 33,242 vOTUs | 2020 | 10.1016/j.chom.2020.08.003 |
| `gpd` | Gut Phage Database | 28,060 gut metagenomes from 28 countries across 6 continents → ~142,000 genomes | 2021 | 10.1016/j.cell.2021.01.029 |
| `chvd` | Cenote Human Virome Database | ~5,996 metagenomes; gut, saliva, skin, vagina → 45,033 vOTUs | 2021 | 10.1073/pnas.2023202118 |
| `mgv` | Metagenomic Gut Virus catalogue | included in the A2 comparison; sample count not verified in this pass | 2021 | — |
| `chgv` | Chinese Gut Virus catalogue | 67,096 non-redundant viral genomes, Chinese cohorts | 2025 | 10.1186/s13073-025-01460-6 |
| `avrc` | Aggregated Gut Viral Catalogue | unifies 8 prior catalogues + IMG/VR; adds infant samples from 9 countries; states the western-adult bias explicitly | 2025 | 10.1371/journal.pcbi.1012268 |

**Correction, this pass:** A2 was first cited here as “Cao et al., doi:10.1016/j.chom.2022.07.005”. Both the author name and the DOI were wrong; the statistic itself is verbatim correct and appears in Figure 1D of the Li et al. paper above.

`avrc` is worth a pointer in the caption: it is a catalogue whose own authors
name the geographic bias as a limitation of the resource. That is the section's
claim stated from inside the reference, which is the strongest form of it.

---

## Primary studies (curated)

| id | study | countries | body site | n | year | doi / id |
|---|---|---|---|---|---|---|
| `rampelli2017` | DNA gut virome across subsistence strategies and geographic origin — reanalysis of public metagenomes | USA, Italy, Tanzania (Hadza), Peru (Matses, Tunapuco) | gut | — | 2017 | PMID 28967228 |
| `zuo2020` | Gut DNA virome across geography, ethnicity, urbanization — Hong Kong + Yunnan, 6 ethnicities, urban & rural | China | gut | 930 | 2020 | 10.1016/j.chom.2020.08.005 |
| `nishijima2022` | Gut dsDNA virome in the Japanese 4D cohort | Japan | gut | 4,198 | 2022 | 10.1038/s41467-022-32832-w |
| `reyes2015` | Gut DNA viromes of Malawian twins discordant for severe acute malnutrition; VLP, 0–30 months | Malawi | gut | 40 (20 twin pairs) | 2015 | 10.1073/pnas.1514285112 |
| `malawi_eed2020` | Growth velocity & environmental enteric dysfunction — bacterial and viral taxa | Malawi | gut | — | 2020 | 10.1371/journal.pntd.0008387 |
| `yan2021` | Gut DNA and RNA viromes of Chinese residents and visiting Pakistanis in the same city | China, Pakistan | gut | 60 (30 + 30) | 2021 | Virus Evol. veab022 |
| `ethiopia_amhara` | Enteric virome of children in a clean-water intervention trial, Amhara region; 29 pools | Ethiopia | gut | 269 children | 2018/2019 | 10.1186/s12879-019-3674-3 |
| `southafrica2020` | Enteric RNA virome of infants, Oukasie clinic, North West Province | South Africa | gut | 4 infants / 12 samples | 2020 | PMC7694487 |
| `mexico2023` | Fecal and oropharyngeal eukaryotic viromes of healthy infants, first year of life, Morelos | Mexico | gut, oropharynx | 9 infants / 187 samples | 2023 | 10.1038/s41598-022-26707-9 |
| `brazil2024` | Microbial diversity in children with gastroenteritis, Amazon region | Brazil | gut | 27 samples | 2024 | PMC11024607 |
| `nigeria2020` | Cosavirus genotypes in feces of children with non-polio acute flaccid paralysis | Nigeria | gut | — | 2020 | PMC12197622 |
| `china_diarrhea2023` | Gut virome of diarrheal children with rotavirus A, Shanghai & Taizhou | China | gut | 162 | 2023 | PMC10351451 |
| `copsac2023` | Viral diversity in the healthy infant gut, COPSAC cohort → 10,000 viral species | Denmark | gut | 647 | 2023 | 10.1038/s41564-023-01345-7 |
| `shkoporov2019` | Human gut virome is diverse, stable and individual-specific; VLP, longitudinal | Ireland | gut | 10 | 2019 | 10.1016/j.chom.2019.09.009 |
| `spain_blood2021` | Diversity of the human blood virome, pooled plasma from healthy donors, Valencia | Spain | blood | 587 pooled | 2021 | 10.3390/v13112322 |
| `denmark_vaginal2020` | Vaginal DNA virome in health and dysbiosis; VLP | Denmark | vaginal | 48 | 2020 | 10.3390/v12101143 |
| `china_vaginitis` | Vaginal virome and vaginitis; 24 pooled libraries | China | vaginal | 267 | — | PMC12003417 |

Entries below the line in the JSON marked `"provenance": "prior-pass"` come from
the reference file we built earlier in this project rather than from this
literature pass — same standard of care, but flagged so you can re-verify.

---

## Country aggregate (what the map colours)

| iso3 | country | region | studies | individuals (approx) |
|---|---|---|---|---|
| JPN | Japan | Eastern Asia | 1 | 4,198 |
| CHN | China | Eastern Asia | 4 | 1,389 |
| DNK | Denmark | Northern Europe | 2 | 695 |
| ESP | Spain | Southern Europe | 1 | 587 (pooled) |
| ETH | Ethiopia | Eastern Africa | 1 | 269 |
| MWI | Malawi | Eastern Africa | 2 | 40+ |
| PAK | Pakistan | Southern Asia | 1 | 30 |
| BRA | Brazil | South America | 1 | 27 samples |
| IRL | Ireland | Northern Europe | 1 | 10 |
| MEX | Mexico | Central America | 1 | 9 |
| ZAF | South Africa | Southern Africa | 1 | 4 |
| USA | United States | North America | 1 | — |
| ITA | Italy | Southern Europe | 1 | — |
| TZA | Tanzania | Eastern Africa | 1 | — |
| PER | Peru | South America | 1 | — |
| NGA | Nigeria | Western Africa | 1 | — |

Note the shape of it: the US and Italy carry a single curated row each, yet they
dominate every catalogue in the table above. That gap is the curation's, not the
field's — another reason the caption has to be honest about what the ramp means.

---

## Suggested ramp

Drive the cyan ramp with **`n_studies`**, not sample counts. Study counts are
commensurable across rows; sample counts mix individuals, pooled libraries,
timepoints and samples, and would encode a fake precision. Keep `n_individuals`
as tooltip text only, with its unit spelled out per row.

Countries with no row need a visually distinct "no data in this set" fill — not
the bottom of the cyan ramp, which would read as "sampled a little".

---

## Verification pass — all 17 primary studies, checked one by one

Every DOI, PMC ID and PubMed ID below was resolved and the title, authors,
journal, year and sample count read off the record. **No entry was fabricated.**
Three needed correcting.

| id | verdict |
|---|---|
| `rampelli2017` | Confirmed. PubMed 28967228. US, Italy, Tanzania (Hadza), Peru (Matses, Tunapuco) — all four countries correct. |
| `zuo2020` | Confirmed. *Cell Host Microbe* 28(5):741–751.e4. 930 adults, Hong Kong + Yunnan, six ethnicities. |
| `nishijima2022` | Confirmed. *Nat Commun*, 6 Sep 2022. 4,198 individuals, Japanese 4D cohort. |
| `reyes2015` | Confirmed. *PNAS* 112(38):11941. 8 concordant + 12 discordant twin pairs = 40 children, Malawi. |
| `malawi_eed2020` | Confirmed. *PLoS Negl Trop Dis*, 23 Jun 2020, Malawi. |
| `yan2021` | Confirmed. *Virus Evol* 7(1):veab022. Chinese residents and visiting Pakistanis, one city. |
| `ethiopia_amhara` | **Corrected.** The title and year described *Enteric virome of Ethiopian children participating in a clean water intervention trial* (PLOS ONE 2018, doi:10.1371/journal.pone.0202054), but the DOI and n = 269 belong to *Viral species richness and composition in young children with loose or watery stool in Ethiopia* (BMC Infect Dis 2019, doi:10.1186/s12879-019-3674-3). Same Amhara cohort, two different papers. Title and year now match the link. |
| `southafrica2020` | Confirmed. *Viruses*, Nov 2020, PMC7694487. 4 infants, 12 samples, Oukasie clinic, North West Province. |
| `mexico2023` | Confirmed. *Sci Rep*, 17 Jan 2023. 9 infants, Morelos; 90 oropharyngeal + 97 faecal samples. |
| `brazil2024` | Confirmed. PMC11024607, 27 inpatients, Amazon region, samples 2012–2016. |
| `nigeria2020` | **Corrected.** The paper is real (PMC12197622) but was published **June 2025**, not 2020 — "2020" in the title is the year the samples were collected. Year fixed and the label now says so. |
| `china_diarrhea2023` | Confirmed. *Gut Microbes*, 13 Jul 2023, PMC10351451. 76 + 27 diarrhoeal/healthy in Shanghai and 40 + 19 in Taizhou = 162. |
| `copsac2023` | Confirmed. *Nat Microbiol*, Apr 2023. 647 one-year-olds, COPSAC, Denmark; 10,021 viral species in 248 families. |
| `shkoporov2019` | Confirmed. *Cell Host Microbe*, 9 Oct 2019. 10 individuals, longitudinal, Ireland. |
| `spain_blood2021` | Confirmed. *Viruses*, 21 Nov 2021. Pooled plasma from 587 healthy donors, Spain. |
| `denmark_vaginal2020` | Confirmed. *Viruses* 12(10):1143. 48 patients in a Danish IVF setting. |
| `china_vaginitis` | **Corrected.** Year was `null`. It is *Front Cell Infect Microbiol*, 3 Apr 2025, doi:10.3389/fcimb.2025.1582553, PMC12003417 — 24 pooled libraries from 267 women, Nantong. |

**Still unverified:** the figure "Africa and South America together supply 1.5% of
GPD's samples (n = 410)", which is stated to come from Figure 1D of Li et al.
2022. It could not be read from the abstract; check it in the PDF before quoting
it in prose.

---

## Figure 1D of Li et al. 2022 — read off the panel

Both anchors resolved against the figure itself, so nothing here is inferred.

**GPD pie (n = 28,060 metagenomes).** Segments 8,501 Europe (30.3%), 9,829
North America (35.0%), 2,321 Asia (8.3%), 3,842 combined (13.7%) and 3,567
unknown origin (12.7%). The 3,842 breaks out as Oceania 3,432 (12.2%), Africa
184 (0.7%) and South America 226 (0.8%). Segments sum to 28,060 exactly.

- **Africa + South America = 184 + 226 = 410**, which is 1.46% of 28,060 →
  **1.5%**. Confirmed as written.
- **Europe + North America + Asia in GPD = 30.3 + 35.0 + 8.3 = 73.6%.**
  In CHVD = 23.6 + 52.1 + 18.8 = **94.5%**. MGV = 93.0%, GVD = 80.0%.

**So 73.6–94.5% is the spread across the four catalogues, not an uncertainty
interval.** The map's wording was ambiguous on this and has been rewritten to
name all four values.

**The percentages include the unknown-origin samples.** In GPD that is 12.7%
(3,567), so these are shares of everything deposited, not of everything placed.
Added to the map's notes.

## The finding worth using

GVD is **18.7% African (504 of 2,697)** — by a distance the most geographically
balanced of the four — and it is the smallest, at 33,242 vOTUs. GPD is the
largest at 142,809 genomes and **0.7% African**.

The reference with the most detection power is the one that represents that
population worst; the one that represents it best gives the least power. That is
a trade the reader has to resolve when choosing a database, not an absence to be
lamented — and it fits the chapter's thesis (the unclassified fraction is a
property of the reference, decided at design time) far better than a flat claim
that Africa is missing. It is now a Methodology Tip in the chapter.
