# Fivi's Kitchen — path audit

Complete review of every recipe the wizard can produce.

| | |
|---|---|
| Source | `docs/kitchen/index.html`, ViromeCity |
| Paths audited | 60 (10 samples × 6 branches) |
| Distinct recipes | 4 destinations |
| Sample-driven conditions | 3 numeric gates |
| Generated | 2026-08-14 |

All recipe text below is produced by running the file's own logic, unmodified. Nothing here is a paraphrase.

---

## 1. What the tree actually looks like

Three questions, but only two of them branch. The genome question changes one row of text and nothing else, and the sample never picks a branch at all — it only flips three numeric gates that add or drop rows inside the recipe already chosen.

```
sample (10)  ─ does not branch, only flips gates
   │
   ├── target = one  ─────────────────────►  targeted PCR          10 paths
   │
   └── target = free
         ├── state = pro   ────────────────►  bulk, no VLP          10 paths
         ├── state = free
         │     ├── genome = dna  ──────────►  VLP + shotgun         10 paths
         │     └── genome = both ──────────►  VLP + shotgun + RT    10 paths
         └── state = both
               ├── genome = dna  ──────────►  split A + B           10 paths
               └── genome = both ──────────►  split A + B + RT      10 paths
```

So the 60 paths are 4 recipes × 15 gate combinations. If the 4 base recipes are right and the 3 thresholds sit in the right place, the other 56 paths follow by construction.

---

## 2. The three gates

| Sample | Viral load | `bm` | `bm ≥ 0.4` keeps filter | `host` | `host ≥ 0.6` adds Deplete | `ct` | `ct ≥ 0.6` adds Controls |
|---|---|---|---|---|---|---|---|
| gut / stool | ~1-5% | 1.00 | **yes** | 0.05 | no | 0.12 | no |
| oral / saliva | ~0.1-1% | 0.85 | **yes** | 0.20 | no | 0.40 | no |
| upper airway | ~0.1-1% | 0.80 | **yes** | 0.30 | no | 0.45 | no |
| vaginal tract | ~1-5% | 0.85 | **yes** | 0.35 | no | 0.35 | no |
| breast milk | ~0.1-1% | 0.50 | **yes** | 0.45 | no | 0.50 | no |
| skin | ~0.1-2% | 0.40 | **yes** | 0.50 | no | 0.72 | **yes** |
| blood / plasma | <0.1% | 0.10 | no | 0.90 | **yes** | 0.78 | **yes** |
| urine | <0.1-0.5% | 0.12 | no | 0.60 | **yes** | 0.60 | **yes** |
| lung | <0.01-0.1% | 0.08 | no | 0.90 | **yes** | 0.92 | **yes** |
| brain / CSF | <0.01% | 0.05 | no | 0.88 | **yes** | 0.97 | **yes** |

Edge cases worth a second look: skin sits exactly on `bm = 0.40` (keeps the filter by equality) and on `host = 0.50`, just under the depletion gate. Breast milk sits on `ct = 0.50`, just under the controls gate.

---

## 3. The four recipes, row by row

Each row below is listed with the samples it fires for and every wording it can take. Between them these cover all 60 paths.

### Branch 1 — targeted PCR

`target = one`

Length: 6–6 rows depending on sample.

**`Skip it`** — identical in all 10 samples

> You don't need metagenomics. Sequencing everything to find one known virus is the expensive way to answer a cheap question.


**`Method`** — identical in all 10 samples

> **qPCR** — or **RT-qPCR** if your virus has an RNA genome. Orders of magnitude cheaper than shotgun, and far more sensitive for a known target. If you need *absolute* quantification at low copy number rather than a yes/no, reach for **ddPCR** instead.


**`Catch`** — identical in all 10 samples

> This only works if you already have the sequence and validated primers — and a strain that diverges at the primer site will read as a false negative. If discovery matters, you're back to metagenomics.
>
> *(shown as a warning row)*


**`Controls`** — all 10 samples, 4 wordings

> *gut / stool, oral / saliva, upper airway, vaginal tract, breast milk*
>
> Run no-template controls, extraction blanks, and a positive control. PCR is sensitive enough that a contaminant reads as a real hit.

> *skin, blood / plasma* *(shown as a warning row)*
>
> Contamination risk here is high, and PCR is sensitive enough to amplify a contaminant into a confident false positive. Run no-template controls, extraction blanks, and a positive control every time.

> *urine* *(shown as a warning row)*
>
> Contamination risk here is med-high, and PCR is sensitive enough to amplify a contaminant into a confident false positive. Run no-template controls, extraction blanks, and a positive control every time.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Contamination risk here is very high, and PCR is sensitive enough to amplify a contaminant into a confident false positive. Run no-template controls, extraction blanks, and a positive control every time.


**`Extraction`** — all 10 samples, 9 wordings

> *gut / stool*
>
> Viral load here is ~1-5% and biomass is very high — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *oral / saliva, upper airway*
>
> Viral load here is ~0.1-1% and biomass is high — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *vaginal tract*
>
> Viral load here is ~1-5% and biomass is high — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *breast milk*
>
> Viral load here is ~0.1-1% and biomass is medium — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *skin*
>
> Viral load here is ~0.1-2% and biomass is low-med — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *blood / plasma*
>
> Viral load here is <0.1% and biomass is very low — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *urine*
>
> Viral load here is <0.1-0.5% and biomass is very low — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *lung*
>
> Viral load here is <0.01-0.1% and biomass is very low — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).

> *brain / CSF*
>
> Viral load here is <0.01% and biomass is very low — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).


**`If you need more`** — identical in all 10 samples

> Want the strain, or many known viruses at once? A targeted capture panel or amplicon sequencing sits between PCR and full shotgun — cheaper than metagenomics, richer than a Ct value.


---

### Branch 2 — integrated prophages

`target = free › state = pro`

Length: 5–6 rows depending on sample.

**`Base`** — identical in all 10 samples

> Bulk (total) metagenomics — sequence the whole community. Prophages live inside bacterial genomes, so they come along with the bacterial DNA.


**`No VLP`** — identical in all 10 samples

> Do NOT do VLP. The filter and nuclease exist to isolate free capsids — they'd throw away the integrated prophages you're actually after.
>
> *(shown as a warning row)*


**`Convert`** — identical in all 10 samples

> DNA workflow — prophages are DNA in the host chromosome. No RT needed.


**`Analysis`** — identical in all 10 samples

> Bioinformatics: assemble the community, then hunt prophages inside bacterial contigs (integrated-element / prophage prediction tools).


**`Platform`** — identical in all 10 samples

> Start with **short-read** — it's the standard, well-trodden choice and it detects prophages inside bacterial contigs perfectly well. **Long-read** is an interesting avenue to explore here, since a read spanning the phage–host junction can confirm a prophage is genuinely integrated and show where — but treat that as exploratory, not the default.


**`Deplete`** — fires for 4/10 samples

> *blood / plasma* *(shown as a warning row)*
>
> Host reads are 80-95% — but careful: aggressive host depletion can strip the very bacteria your prophages are sitting in. Deplete lightly, or not at all, and remove host reads in silico instead.

> *urine* *(shown as a warning row)*
>
> Host reads are med-high — but careful: aggressive host depletion can strip the very bacteria your prophages are sitting in. Deplete lightly, or not at all, and remove host reads in silico instead.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Host reads are very high — but careful: aggressive host depletion can strip the very bacteria your prophages are sitting in. Deplete lightly, or not at all, and remove host reads in silico instead.


---

### Branch 3a — free virions, DNA only

`target = free › state = free › genome = dna`

Length: 6–8 rows depending on sample.

**`Base`** — identical in all 10 samples

> Shotgun metagenomics on a VLP-enriched library.


**`Convert`** — identical in all 10 samples

> DNA only — most phages are dsDNA, so no RT needed. Just know what you're trading away: any RNA phage here is invisible to you.


**`Enrich · VLP`** — identical in all 10 samples

> Free virions only — so VLP prep isn't optional, it's the whole point. The **nuclease** does the real work: it digests every genome not sealed inside a capsid, turning a viral needle into a viral signal.


**`Filter`** — all 10 samples, 6 wordings

> *gut / stool*
>
> Biomass is very high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *oral / saliva, upper airway*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *vaginal tract*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *breast milk*
>
> Biomass is medium — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *skin*
>
> Biomass is low-med — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-2% viral fraction into something worth sequencing.

> *blood / plasma, urine, lung, brain / CSF* *(shown as a warning row)*
>
> Biomass is very low — **drop the 0.22 µm filter** (barely any bacteria to remove, and it would cost you virions you can't spare). Clarify gently, concentrate, and keep the nuclease. Still VLP — just without filtration.


**`Platform`** — identical in all 10 samples

> Go with **short-read** — cheaper, deeper, and the pipelines are well established for finding what's there and how much. **Long-read** can be worth exploring if you want to finish whole phage genomes or resolve structure, but it's still more of an exploratory add-on than the standard route.


**`Analysis`** — identical in all 10 samples

> Bioinformatics: host-read removal → assembly → viral identification.


**`Controls`** — fires for 5/10 samples

> *skin, blood / plasma* *(shown as a warning row)*
>
> Contamination risk is high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates.

> *urine* *(shown as a warning row)*
>
> Contamination risk is med-high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Contamination risk is very high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates.


**`Deplete`** — fires for 4/10 samples

> *blood / plasma*
>
> Host reads are 80-95% — add host depletion at the bench and remove host reads in silico.

> *urine*
>
> Host reads are med-high — add host depletion at the bench and remove host reads in silico.

> *lung, brain / CSF*
>
> Host reads are very high — add host depletion at the bench and remove host reads in silico.


---

### Branch 3b — free virions, DNA + RNA

`target = free › state = free › genome = both`

Length: 6–8 rows depending on sample.

**`Base`** — identical in all 10 samples

> Shotgun metagenomics on a VLP-enriched library.


**`Convert`** — identical in all 10 samples

> Add reverse transcription (RT). RNA phages exist — Fiersviridae, Cystoviridae — and a DNA-only protocol is blind to every one of them.


**`Enrich · VLP`** — identical in all 10 samples

> Free virions only — so VLP prep isn't optional, it's the whole point. The **nuclease** does the real work: it digests every genome not sealed inside a capsid, turning a viral needle into a viral signal.


**`Filter`** — all 10 samples, 6 wordings

> *gut / stool*
>
> Biomass is very high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *oral / saliva, upper airway*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *vaginal tract*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *breast milk*
>
> Biomass is medium — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *skin*
>
> Biomass is low-med — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-2% viral fraction into something worth sequencing.

> *blood / plasma, urine, lung, brain / CSF* *(shown as a warning row)*
>
> Biomass is very low — **drop the 0.22 µm filter** (barely any bacteria to remove, and it would cost you virions you can't spare). Clarify gently, concentrate, and keep the nuclease. Still VLP — just without filtration.


**`Platform`** — identical in all 10 samples

> Go with **short-read** — cheaper, deeper, and the pipelines are well established for finding what's there and how much. **Long-read** can be worth exploring if you want to finish whole phage genomes or resolve structure, but it's still more of an exploratory add-on than the standard route.


**`Analysis`** — identical in all 10 samples

> Bioinformatics: host-read removal → assembly → viral identification.


**`Controls`** — fires for 5/10 samples

> *skin, blood / plasma* *(shown as a warning row)*
>
> Contamination risk is high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates.

> *urine* *(shown as a warning row)*
>
> Contamination risk is med-high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Contamination risk is very high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates.


**`Deplete`** — fires for 4/10 samples

> *blood / plasma*
>
> Host reads are 80-95% — add host depletion at the bench and remove host reads in silico.

> *urine*
>
> Host reads are med-high — add host depletion at the bench and remove host reads in silico.

> *lung, brain / CSF*
>
> Host reads are very high — add host depletion at the bench and remove host reads in silico.


---

### Branch 4a — both fractions, DNA only

`target = free › state = both › genome = dna`

This branch returns a split view: two parallel methods, sequenced as two libraries.

**Framing note shown above both arms**

> Free and integrated phages sit in different physical fractions, and no single prep captures both. So you split the sample and run these two methods in parallel, sequenced as two libraries — roughly twice the work and budget, but the only honest way to see both.

**Extra caution appended for blood / plasma, urine, lung, brain / CSF**

> One caution: biomass here is very low. Splitting an already thin sample between two preps may leave neither arm with enough — bring more input material if you can, or run one arm and say which, and why, in your methods.

#### Method A — integrated prophages (bulk, no VLP)

**`Base`** — identical in all 10 samples

> Bulk (total) metagenomics — sequence the whole community. Prophages live inside bacterial genomes, so they come along with the bacterial DNA; there's nothing to enrich for separately.


**`No VLP`** — identical in all 10 samples

> Do NOT do VLP on this arm. The 0.22 µm filter and the nuclease exist to isolate free capsids — they would discard the integrated prophages you're after here.
>
> *(shown as a warning row)*


**`Convert`** — identical in all 10 samples

> DNA workflow, no reverse transcription — a prophage is DNA sitting in the host chromosome.


**`Platform`** — identical in all 10 samples

> **Short-read** is the standard call and detects prophages inside bacterial contigs reliably. **Long-read** is an interesting thing to explore on this arm — a read spanning the phage–host junction can prove genuine integration and show exactly where — but keep it exploratory rather than the default.


**`Analysis`** — identical in all 10 samples

> Assemble the community, then predict prophages inside bacterial contigs (integrated-element / prophage-finding tools).


**`Deplete`** — fires for 4/10 samples

> *blood / plasma* *(shown as a warning row)*
>
> Host reads are 80-95%, so it's tempting to deplete — but be careful: aggressive host depletion strips the very bacteria your prophages are integrated into. Deplete lightly, or skip it at the bench and remove host reads in silico instead.

> *urine* *(shown as a warning row)*
>
> Host reads are med-high, so it's tempting to deplete — but be careful: aggressive host depletion strips the very bacteria your prophages are integrated into. Deplete lightly, or skip it at the bench and remove host reads in silico instead.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Host reads are very high, so it's tempting to deplete — but be careful: aggressive host depletion strips the very bacteria your prophages are integrated into. Deplete lightly, or skip it at the bench and remove host reads in silico instead.

#### Method B — free virions (VLP-enriched)

**`Base`** — identical in all 10 samples

> Shotgun metagenomics on a VLP-enriched library — this arm goes after the free particles.


**`Convert`** — identical in all 10 samples

> DNA only — most phages are dsDNA, so no RT needed. Just know what you're trading away: any RNA phage here is invisible to you.


**`Enrich · VLP`** — identical in all 10 samples

> VLP prep is the whole point of this arm. The **nuclease** does the real work: it digests every genome that isn't sealed inside a capsid, turning a viral needle into a viral signal.


**`Filter`** — all 10 samples, 6 wordings

> *gut / stool*
>
> Biomass is very high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *oral / saliva, upper airway*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *vaginal tract*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *breast milk*
>
> Biomass is medium — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *skin*
>
> Biomass is low-med — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-2% viral fraction into something worth sequencing.

> *blood / plasma, urine, lung, brain / CSF* *(shown as a warning row)*
>
> Biomass is very low — **drop the 0.22 µm filter** (barely any bacteria to remove, and it would cost you virions you can't spare). Clarify gently, concentrate, and keep the nuclease. Still VLP — just without filtration.


**`Platform`** — identical in all 10 samples

> **Short-read** for what's there and how much — the go-to on this arm. **Long-read** is worth exploring to finish whole phage genomes or resolve structure, but treat it as an exploratory add-on rather than the default.


**`Analysis`** — identical in all 10 samples

> Bioinformatics: host-read removal → assembly → viral identification.


**`Controls`** — fires for 5/10 samples

> *skin, blood / plasma* *(shown as a warning row)*
>
> Contamination risk is high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates on this arm especially.

> *urine* *(shown as a warning row)*
>
> Contamination risk is med-high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates on this arm especially.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Contamination risk is very high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates on this arm especially.


**`Deplete`** — fires for 4/10 samples

> *blood / plasma*
>
> Host reads are 80-95% — add host depletion at the bench and remove host reads in silico.

> *urine*
>
> Host reads are med-high — add host depletion at the bench and remove host reads in silico.

> *lung, brain / CSF*
>
> Host reads are very high — add host depletion at the bench and remove host reads in silico.


---

### Branch 4b — both fractions, DNA + RNA

`target = free › state = both › genome = both`

This branch returns a split view: two parallel methods, sequenced as two libraries.

**Framing note shown above both arms**

> Free and integrated phages sit in different physical fractions, and no single prep captures both. So you split the sample and run these two methods in parallel, sequenced as two libraries — roughly twice the work and budget, but the only honest way to see both.

**Extra caution appended for blood / plasma, urine, lung, brain / CSF**

> One caution: biomass here is very low. Splitting an already thin sample between two preps may leave neither arm with enough — bring more input material if you can, or run one arm and say which, and why, in your methods.

#### Method A — integrated prophages (bulk, no VLP)

**`Base`** — identical in all 10 samples

> Bulk (total) metagenomics — sequence the whole community. Prophages live inside bacterial genomes, so they come along with the bacterial DNA; there's nothing to enrich for separately.


**`No VLP`** — identical in all 10 samples

> Do NOT do VLP on this arm. The 0.22 µm filter and the nuclease exist to isolate free capsids — they would discard the integrated prophages you're after here.
>
> *(shown as a warning row)*


**`Convert`** — identical in all 10 samples

> DNA workflow, no reverse transcription — a prophage is DNA sitting in the host chromosome.


**`Platform`** — identical in all 10 samples

> **Short-read** is the standard call and detects prophages inside bacterial contigs reliably. **Long-read** is an interesting thing to explore on this arm — a read spanning the phage–host junction can prove genuine integration and show exactly where — but keep it exploratory rather than the default.


**`Analysis`** — identical in all 10 samples

> Assemble the community, then predict prophages inside bacterial contigs (integrated-element / prophage-finding tools).


**`Deplete`** — fires for 4/10 samples

> *blood / plasma* *(shown as a warning row)*
>
> Host reads are 80-95%, so it's tempting to deplete — but be careful: aggressive host depletion strips the very bacteria your prophages are integrated into. Deplete lightly, or skip it at the bench and remove host reads in silico instead.

> *urine* *(shown as a warning row)*
>
> Host reads are med-high, so it's tempting to deplete — but be careful: aggressive host depletion strips the very bacteria your prophages are integrated into. Deplete lightly, or skip it at the bench and remove host reads in silico instead.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Host reads are very high, so it's tempting to deplete — but be careful: aggressive host depletion strips the very bacteria your prophages are integrated into. Deplete lightly, or skip it at the bench and remove host reads in silico instead.

#### Method B — free virions (VLP-enriched)

**`Base`** — identical in all 10 samples

> Shotgun metagenomics on a VLP-enriched library — this arm goes after the free particles.


**`Convert`** — identical in all 10 samples

> Add reverse transcription (RT). RNA phages exist — Fiersviridae, Cystoviridae — and a DNA-only protocol is blind to every one of them.


**`Enrich · VLP`** — identical in all 10 samples

> VLP prep is the whole point of this arm. The **nuclease** does the real work: it digests every genome that isn't sealed inside a capsid, turning a viral needle into a viral signal.


**`Filter`** — all 10 samples, 6 wordings

> *gut / stool*
>
> Biomass is very high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *oral / saliva, upper airway*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *vaginal tract*
>
> Biomass is high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.

> *breast milk*
>
> Biomass is medium — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-1% viral fraction into something worth sequencing.

> *skin*
>
> Biomass is low-med — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~0.1-2% viral fraction into something worth sequencing.

> *blood / plasma, urine, lung, brain / CSF* *(shown as a warning row)*
>
> Biomass is very low — **drop the 0.22 µm filter** (barely any bacteria to remove, and it would cost you virions you can't spare). Clarify gently, concentrate, and keep the nuclease. Still VLP — just without filtration.


**`Platform`** — identical in all 10 samples

> **Short-read** for what's there and how much — the go-to on this arm. **Long-read** is worth exploring to finish whole phage genomes or resolve structure, but treat it as an exploratory add-on rather than the default.


**`Analysis`** — identical in all 10 samples

> Bioinformatics: host-read removal → assembly → viral identification.


**`Controls`** — fires for 5/10 samples

> *skin, blood / plasma* *(shown as a warning row)*
>
> Contamination risk is high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates on this arm especially.

> *urine* *(shown as a warning row)*
>
> Contamination risk is med-high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates on this arm especially.

> *lung, brain / CSF* *(shown as a warning row)*
>
> Contamination risk is very high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates on this arm especially.


**`Deplete`** — fires for 4/10 samples

> *blood / plasma*
>
> Host reads are 80-95% — add host depletion at the bench and remove host reads in silico.

> *urine*
>
> Host reads are med-high — add host depletion at the bench and remove host reads in silico.

> *lung, brain / CSF*
>
> Host reads are very high — add host depletion at the bench and remove host reads in silico.


---

## 4. Worked examples, end to end

Eight complete paths, printed exactly as a user would meet them: the two extremes of the sample range (gut, the easiest; brain/CSF, the hardest) through each of the four recipes.

### gut / stool

#### Targeted PCR

> Fivi: Stool — my favourite pantry! Packed with phages, and viruses are actually findable here.
>
> Fivi: Just one virus, present or absent? Then don't cook the whole banquet — PCR is far cheaper, and more sensitive.

Legend shown: host DNA <1% · contamination low · viral fraction medium

- **Skip it** — You don't need metagenomics. Sequencing everything to find one known virus is the expensive way to answer a cheap question.
- **Method** — **qPCR** — or **RT-qPCR** if your virus has an RNA genome. Orders of magnitude cheaper than shotgun, and far more sensitive for a known target. If you need *absolute* quantification at low copy number rather than a yes/no, reach for **ddPCR** instead.
- **Catch** ⚠ — This only works if you already have the sequence and validated primers — and a strain that diverges at the primer site will read as a false negative. If discovery matters, you're back to metagenomics.
- **Controls** — Run no-template controls, extraction blanks, and a positive control. PCR is sensitive enough that a contaminant reads as a real hit.
- **Extraction** — Viral load here is ~1-5% and biomass is very high — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).
- **If you need more** — Want the strain, or many known viruses at once? A targeted capture panel or amplicon sequencing sits between PCR and full shotgun — cheaper than metagenomics, richer than a Ct value.

#### Integrated prophages

> Fivi: Stool — my favourite pantry! Packed with phages, and viruses are actually findable here.
>
> Fivi: Communities! Now — are you after the free ones floating around, the ones integrated into bacterial genomes, or both? That changes everything.
>
> Fivi: Just the prophages — genomes tucked into bacterial chromosomes. No VLP for these; they'd be filtered right out.

Legend shown: host DNA <1% · contamination low · viral fraction medium

- **Base** — Bulk (total) metagenomics — sequence the whole community. Prophages live inside bacterial genomes, so they come along with the bacterial DNA.
- **No VLP** ⚠ — Do NOT do VLP. The filter and nuclease exist to isolate free capsids — they'd throw away the integrated prophages you're actually after.
- **Convert** — DNA workflow — prophages are DNA in the host chromosome. No RT needed.
- **Analysis** — Bioinformatics: assemble the community, then hunt prophages inside bacterial contigs (integrated-element / prophage prediction tools).
- **Platform** — Start with **short-read** — it's the standard, well-trodden choice and it detects prophages inside bacterial contigs perfectly well. **Long-read** is an interesting avenue to explore here, since a read spanning the phage–host junction can confirm a prophage is genuinely integrated and show where — but treat that as exploratory, not the default.

#### Free virions, DNA + RNA

> Fivi: Stool — my favourite pantry! Packed with phages, and viruses are actually findable here.
>
> Fivi: Communities! Now — are you after the free ones floating around, the ones integrated into bacterial genomes, or both? That changes everything.
>
> Fivi: Free virions only — then VLP prep is the whole game.
>
> Fivi: Good call — RNA phages are real (Fiersviridae, Cystoviridae) and most surveys quietly miss them. We'll add reverse transcription.

Legend shown: host DNA <1% · contamination low · viral fraction high (VLP ceiling)

- **Base** — Shotgun metagenomics on a VLP-enriched library.
- **Convert** — Add reverse transcription (RT). RNA phages exist — Fiersviridae, Cystoviridae — and a DNA-only protocol is blind to every one of them.
- **Enrich · VLP** — Free virions only — so VLP prep isn't optional, it's the whole point. The **nuclease** does the real work: it digests every genome not sealed inside a capsid, turning a viral needle into a viral signal.
- **Filter** — Biomass is very high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.
- **Platform** — Go with **short-read** — cheaper, deeper, and the pipelines are well established for finding what's there and how much. **Long-read** can be worth exploring if you want to finish whole phage genomes or resolve structure, but it's still more of an exploratory add-on than the standard route.
- **Analysis** — Bioinformatics: host-read removal → assembly → viral identification.

#### Both fractions, DNA + RNA

> Fivi: Stool — my favourite pantry! Packed with phages, and viruses are actually findable here.
>
> Fivi: Communities! Now — are you after the free ones floating around, the ones integrated into bacterial genomes, or both? That changes everything.
>
> Fivi: Both?! Free and integrated live in different fractions — that means two separate methods, not one. I'll lay out each.
>
> Fivi: Good call — RNA phages are real (Fiersviridae, Cystoviridae) and most surveys quietly miss them. We'll add reverse transcription.

Legend shown: host DNA <1% · contamination low · viral fraction high (VLP ceiling)

Free and integrated phages sit in different physical fractions, and no single prep captures both. So you split the sample and run these two methods in parallel, sequenced as two libraries — roughly twice the work and budget, but the only honest way to see both.

**Method A — integrated prophages**

- **Base** — Bulk (total) metagenomics — sequence the whole community. Prophages live inside bacterial genomes, so they come along with the bacterial DNA; there's nothing to enrich for separately.
- **No VLP** ⚠ — Do NOT do VLP on this arm. The 0.22 µm filter and the nuclease exist to isolate free capsids — they would discard the integrated prophages you're after here.
- **Convert** — DNA workflow, no reverse transcription — a prophage is DNA sitting in the host chromosome.
- **Platform** — **Short-read** is the standard call and detects prophages inside bacterial contigs reliably. **Long-read** is an interesting thing to explore on this arm — a read spanning the phage–host junction can prove genuine integration and show exactly where — but keep it exploratory rather than the default.
- **Analysis** — Assemble the community, then predict prophages inside bacterial contigs (integrated-element / prophage-finding tools).

**Method B — free virions**

- **Base** — Shotgun metagenomics on a VLP-enriched library — this arm goes after the free particles.
- **Convert** — Add reverse transcription (RT). RNA phages exist — Fiersviridae, Cystoviridae — and a DNA-only protocol is blind to every one of them.
- **Enrich · VLP** — VLP prep is the whole point of this arm. The **nuclease** does the real work: it digests every genome that isn't sealed inside a capsid, turning a viral needle into a viral signal.
- **Filter** — Biomass is very high — keep the **0.22 µm filter**. There are plenty of bacteria to remove, and removing them is what lifts your ~1-5% viral fraction into something worth sequencing.
- **Platform** — **Short-read** for what's there and how much — the go-to on this arm. **Long-read** is worth exploring to finish whole phage genomes or resolve structure, but treat it as an exploratory add-on rather than the default.
- **Analysis** — Bioinformatics: host-read removal → assembly → viral identification.

### brain / CSF

#### Targeted PCR

> Fivi: Brain / CSF?! The hardest kitchen there is — nearly no biomass, huge contamination risk.
>
> Fivi: Just one virus, present or absent? Then don't cook the whole banquet — PCR is far cheaper, and more sensitive.

Legend shown: host DNA very high · contamination very high · viral fraction low

- **Skip it** — You don't need metagenomics. Sequencing everything to find one known virus is the expensive way to answer a cheap question.
- **Method** — **qPCR** — or **RT-qPCR** if your virus has an RNA genome. Orders of magnitude cheaper than shotgun, and far more sensitive for a known target. If you need *absolute* quantification at low copy number rather than a yes/no, reach for **ddPCR** instead.
- **Catch** ⚠ — This only works if you already have the sequence and validated primers — and a strain that diverges at the primer site will read as a false negative. If discovery matters, you're back to metagenomics.
- **Controls** ⚠ — Contamination risk here is very high, and PCR is sensitive enough to amplify a contaminant into a confident false positive. Run no-template controls, extraction blanks, and a positive control every time.
- **Extraction** — Viral load here is <0.01% and biomass is very low — that shapes your extraction and input volume, even though you're skipping VLP prep entirely (PCR is already specific; filtering would only lose you material).
- **If you need more** — Want the strain, or many known viruses at once? A targeted capture panel or amplicon sequencing sits between PCR and full shotgun — cheaper than metagenomics, richer than a Ct value.

#### Integrated prophages

> Fivi: Brain / CSF?! The hardest kitchen there is — nearly no biomass, huge contamination risk.
>
> Fivi: Communities! Now — are you after the free ones floating around, the ones integrated into bacterial genomes, or both? That changes everything.
>
> Fivi: Just the prophages — genomes tucked into bacterial chromosomes. No VLP for these; they'd be filtered right out.

Legend shown: host DNA very high · contamination very high · viral fraction low

- **Base** — Bulk (total) metagenomics — sequence the whole community. Prophages live inside bacterial genomes, so they come along with the bacterial DNA.
- **No VLP** ⚠ — Do NOT do VLP. The filter and nuclease exist to isolate free capsids — they'd throw away the integrated prophages you're actually after.
- **Convert** — DNA workflow — prophages are DNA in the host chromosome. No RT needed.
- **Deplete** ⚠ — Host reads are very high — but careful: aggressive host depletion can strip the very bacteria your prophages are sitting in. Deplete lightly, or not at all, and remove host reads in silico instead.
- **Analysis** — Bioinformatics: assemble the community, then hunt prophages inside bacterial contigs (integrated-element / prophage prediction tools).
- **Platform** — Start with **short-read** — it's the standard, well-trodden choice and it detects prophages inside bacterial contigs perfectly well. **Long-read** is an interesting avenue to explore here, since a read spanning the phage–host junction can confirm a prophage is genuinely integrated and show where — but treat that as exploratory, not the default.

#### Free virions, DNA + RNA

> Fivi: Brain / CSF?! The hardest kitchen there is — nearly no biomass, huge contamination risk.
>
> Fivi: Communities! Now — are you after the free ones floating around, the ones integrated into bacterial genomes, or both? That changes everything.
>
> Fivi: Free virions only — then VLP prep is the whole game.
>
> Fivi: Good call — RNA phages are real (Fiersviridae, Cystoviridae) and most surveys quietly miss them. We'll add reverse transcription.

Legend shown: host DNA very high · contamination very high · viral fraction low (VLP ceiling)

- **Base** — Shotgun metagenomics on a VLP-enriched library.
- **Convert** — Add reverse transcription (RT). RNA phages exist — Fiersviridae, Cystoviridae — and a DNA-only protocol is blind to every one of them.
- **Enrich · VLP** — Free virions only — so VLP prep isn't optional, it's the whole point. The **nuclease** does the real work: it digests every genome not sealed inside a capsid, turning a viral needle into a viral signal.
- **Filter** ⚠ — Biomass is very low — **drop the 0.22 µm filter** (barely any bacteria to remove, and it would cost you virions you can't spare). Clarify gently, concentrate, and keep the nuclease. Still VLP — just without filtration.
- **Deplete** — Host reads are very high — add host depletion at the bench and remove host reads in silico.
- **Controls** ⚠ — Contamination risk is very high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates.
- **Platform** — Go with **short-read** — cheaper, deeper, and the pipelines are well established for finding what's there and how much. **Long-read** can be worth exploring if you want to finish whole phage genomes or resolve structure, but it's still more of an exploratory add-on than the standard route.
- **Analysis** — Bioinformatics: host-read removal → assembly → viral identification.

#### Both fractions, DNA + RNA

> Fivi: Brain / CSF?! The hardest kitchen there is — nearly no biomass, huge contamination risk.
>
> Fivi: Communities! Now — are you after the free ones floating around, the ones integrated into bacterial genomes, or both? That changes everything.
>
> Fivi: Both?! Free and integrated live in different fractions — that means two separate methods, not one. I'll lay out each.
>
> Fivi: Good call — RNA phages are real (Fiersviridae, Cystoviridae) and most surveys quietly miss them. We'll add reverse transcription.

Legend shown: host DNA very high · contamination very high · viral fraction low (VLP ceiling)

Free and integrated phages sit in different physical fractions, and no single prep captures both. So you split the sample and run these two methods in parallel, sequenced as two libraries — roughly twice the work and budget, but the only honest way to see both. One caution: biomass here is very low. Splitting an already thin sample between two preps may leave neither arm with enough — bring more input material if you can, or run one arm and say which, and why, in your methods.

**Method A — integrated prophages**

- **Base** — Bulk (total) metagenomics — sequence the whole community. Prophages live inside bacterial genomes, so they come along with the bacterial DNA; there's nothing to enrich for separately.
- **No VLP** ⚠ — Do NOT do VLP on this arm. The 0.22 µm filter and the nuclease exist to isolate free capsids — they would discard the integrated prophages you're after here.
- **Convert** — DNA workflow, no reverse transcription — a prophage is DNA sitting in the host chromosome.
- **Deplete** ⚠ — Host reads are very high, so it's tempting to deplete — but be careful: aggressive host depletion strips the very bacteria your prophages are integrated into. Deplete lightly, or skip it at the bench and remove host reads in silico instead.
- **Platform** — **Short-read** is the standard call and detects prophages inside bacterial contigs reliably. **Long-read** is an interesting thing to explore on this arm — a read spanning the phage–host junction can prove genuine integration and show exactly where — but keep it exploratory rather than the default.
- **Analysis** — Assemble the community, then predict prophages inside bacterial contigs (integrated-element / prophage-finding tools).

**Method B — free virions**

- **Base** — Shotgun metagenomics on a VLP-enriched library — this arm goes after the free particles.
- **Convert** — Add reverse transcription (RT). RNA phages exist — Fiersviridae, Cystoviridae — and a DNA-only protocol is blind to every one of them.
- **Enrich · VLP** — VLP prep is the whole point of this arm. The **nuclease** does the real work: it digests every genome that isn't sealed inside a capsid, turning a viral needle into a viral signal.
- **Filter** ⚠ — Biomass is very low — **drop the 0.22 µm filter** (barely any bacteria to remove, and it would cost you virions you can't spare). Clarify gently, concentrate, and keep the nuclease. Still VLP — just without filtration.
- **Deplete** — Host reads are very high — add host depletion at the bench and remove host reads in silico.
- **Controls** ⚠ — Contamination risk is very high — reagent and kit contaminants can outnumber real signal at this biomass. Run negative controls, blanks and replicates on this arm especially.
- **Platform** — **Short-read** for what's there and how much — the go-to on this arm. **Long-read** is worth exploring to finish whole phage genomes or resolve structure, but treat it as an exploratory add-on rather than the default.
- **Analysis** — Bioinformatics: host-read removal → assembly → viral identification.

⚠ marks rows the interface styles as a warning.

---

## 5. Findings

Six things surfaced by reading the logic against its own output. None is confirmed wrong — each is a decision worth confirming.

### 5.1 Three blocks of code can never run — *dead code*

The `target === "euk"` and `target === "all"` branches (lines 324–340) are unreachable: `TARGETS` only defines `one` and `free`. And because all four live cases `return` before reaching it, the shared tail at lines 342–350 — Deplete, Controls, Platform, Analysis — never runs either. That is roughly thirty lines, including a genuinely good passage on why no single prep captures both the eukaryotic and the free-particle fractions. Either delete them or bring the eukaryotic-virus option back into `TARGETS`.

### 5.2 The genome icon in the PCR recipe is unreachable — *dead code*

`recipeIcon()` returns `dna` or `rna` based on `ans.genome` for the targeted branch, but the genome question only appears when `target === "free"`. In the PCR branch `genome` is always `null`, so the generic phage icon shows every time.

### 5.3 The prophage branch ignores contamination — *needs a decision*

`state === "pro"` never reads `S.ct`. Brain/CSF (`ct 0.97`) and lung (`ct 0.92`) therefore receive a recipe without a single line about controls. It ignores `S.bm` too, recommending total metagenomics on a sample with `bm 0.05` without comment. Is it intentional that controls only appear when VLP is in play? At these biomass levels, contamination is the dominant failure mode regardless of prep.

### 5.4 Skin and breast milk fall just below every threshold — *needs a decision*

Skin: `bm 0.40` keeps the filter by exact equality, and `host 0.50` means no depletion is suggested even though the label reads 20–50% host. Breast milk: `ct 0.50` means no controls row, despite contamination labelled medium and mid-range biomass. If both should get those warnings, the host and contamination gates need to drop to 0.45.

### 5.5 The legend promises the VLP ceiling in the split view — *judgement call*

`recipeUsesVLP()` returns true when `state === "both"`, so the viral-fraction pill shows `viralVLP` for the whole recipe. Only Method B is VLP-enriched; Method A will see the lower base fraction. Consider showing both numbers in the split view, or attaching the pill to each arm.

### 5.6 The value `free` means two different things — *readability*

`free` is both a `target` value (communities) and a `state` value (free virions). It works, but `target === "free" && state === "free"` reads confusingly, and it already forced a manual reset of `state` at line 213. Renaming the state values to `integrated` / `virions` / `both` would remove the ambiguity.

---

## 6. Proposal on the table: mucosal vs tissue

**The question.** Should the ten samples be split in two — mucosal versus tissue — with mucosal samples always getting VLP prep and tissue samples never getting it?

**Verdict: worth adding as a label, not as the logic.**

The instinct is right. What actually decides whether VLP prep helps is whether there is a resident microbial community to filter out. Mucosal surfaces have one; sterile sites do not. That distinction is real, and users would understand the recipe better if the kitchen named it. It is also, in effect, already implemented — every mucosal sample clears `bm ≥ 0.4` and every sterile-site sample fails it. The threshold is the proposal, written numerically.

Three reasons not to promote it to the logic:

**It collides with the prophage branch.** "Mucosal always gets VLP" is false for gut plus prophages, where the filter and nuclease destroy exactly what the user came for. Whether VLP applies depends on `state` first and sample second.

**VLP is two operations, not one.** The filter removes bacteria; the nuclease removes everything not sealed in a capsid. In blood and CSF the nuclease is the single most valuable step in the protocol, because host DNA is 80–95% of the material and digesting it is the cheapest way to lift viral signal. "Tissue never gets VLP" would discard the part that helps most. The current code already handles this correctly — it drops the filter and keeps the nuclease.

**Three of ten samples fit neither bucket.** Skin is external epithelium, breast milk is a secretion, urine is an excretion from a near-sterile tract. A binary forces a wrong answer for three of ten.

### Sample classification

| Sample | Group | Why | `bm` | Agrees with current gate |
|---|---|---|---|---|
| gut / stool | mucosal | Luminal community, very high microbial load | 1.00 | same |
| oral / saliva | mucosal | Luminal community, high biomass | 0.85 | same |
| upper airway | mucosal | Luminal community, high biomass | 0.80 | same |
| vaginal tract | mucosal | Luminal community, high biomass | 0.85 | same |
| breast milk | in between | Secretion — neither mucosa nor tissue | 0.50 | — |
| skin | in between | External epithelium — not mucosal, not sterile | 0.40 | — |
| urine | in between | Excretion from a near-sterile tract | 0.12 | — |
| blood / plasma | tissue / sterile | Host-dominated, no resident community | 0.10 | same |
| lung | tissue / sterile | Host-dominated, low biomass | 0.08 | same |
| brain / CSF | tissue / sterile | Host-dominated, lowest biomass | 0.05 | same |

### Suggested middle path

Keep the numeric gate as the logic, and surface the group as a visible label: a chip reading `mucosal surface` or `sterile site` next to the sample name in the recipe header, plus one line in the Filter row saying which it is and why that decides the filter. Right now the wizard tells the user the filter was dropped but never says the reason is the absence of a community to remove — that is the teaching moment currently missing. The three in-between samples get their own honest label rather than being forced to a side.
