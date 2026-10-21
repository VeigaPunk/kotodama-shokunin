# SrcZederDomestication — Zeder 2008 PNAS, livestock domestication timing (claim C frontier)

Seat: leaf source opener for claim C (`pastoralism-animal-husbandry.md`). Author-lane advice, never admission.
Access date for every opened URL below: **2026-10-21**. Tool installs: **none** (no pacman, no uv, no binaries touched).

## 1. What was actually opened (fetch order, honest)

| # | URL | Result |
|---|---|---|
| 1 | https://www.pnas.org/doi/10.1073/pnas.0801317105 | **HTTP 403** — publisher landing page refused the lane's reader. Not used as evidence. |
| 2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2575338/ | **opened, HTTP 200, full text** (`Method: native`). Published version, not an author manuscript: header reads `Proc Natl Acad Sci U S A. 2008 Aug 12;105(33):11597–11604. doi: 10.1073/pnas.0801317105`, `PMCID: PMC2575338 PMID: 18697943`. Read from Abstract through `## Future Research`, `## Acknowledgments`, `## Footnotes`; unread remainder is the reference list only. |
| 3 | https://pubmed.ncbi.nlm.nih.gov/18697943/ | opened as a bibliographic cross-check: same volume/pages/DOI, `[Indexed for MEDLINE]`, **no "Erratum in" and no "Comment in"** on the record. |

So: the article exists, is reachable at PMC, and the row's URL should be the **PMC** one (the DOI/PNAS URL is a 403 lead for this host, exactly the S032 precedent).

Duplicate check before proposing a row: `grep -rni "zeder\|pnas.0801317105\|PMC2575338" corpus/ tools/ reports/` → no hit for this work. Only `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:101` carries a *different* work, `Zeder 2006 — to-verify`; see §6.

## 2. SOURCES row — ready to paste (L1 assigns the id; next free is S048)

```markdown
| S048 | Zeder 2008, Domestication and early agriculture in the Mediterranean Basin: Origins, diffusion, and impact, PNAS 105(33):11597–11604, doi 10.1073/pnas.0801317105 — https://pmc.ncbi.nlm.nih.gov/articles/PMC2575338/ | paper | A | the 2008 published state of evidence for when and how sheep, goats, cattle and pigs came under management in the Fertile Crescent, and for how domesticates reached the Mediterranean; not transhumance or mobile-pastoralism as social forms, not post-2008 chronology, not other regions | "Initial Animal Domestication in the Fertile Crescent", paragraph beginning "Animal domestication in the Near East can then be seen…"; full text at PMC on 2026-10-21 (publisher DOI URL returned HTTP 403); no erratum on the PubMed record | domestication is an extended management process, not an event: herd management is legible ~1,000 years before any body-size or horn change; the four livestock species come under management ca. 11,000–10,000 B.P.; the domesticate package then moves by sea with local adoption and some independent local domestication | queued | 2026-10-21 | 365d | — |
```

Field notes for the integrator:
- `id` — **do not** take S048 as fixed; L1 assigns. Everything else is paste-ready.
- `status: queued` until the entry cites it; then `mined` and `used-by` gains `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`.
- The `anchor` cell is pipe-free and inside double quotes, matching S031–S034 style.
- `tier A` reason, stated the way criterion 6 asks: this is **not** a publisher blurb or abstract-only row — the full body was opened, it is the original peer-reviewed paper, and the author is the archaeozoologist whose caprine work the paper synthesizes. A is scoped to *"what this 2008 paper reports"*; it is **not** A for "current consensus dates" (see §5).

## 3. Quotes (verbatim, each ≤25 words, each located)

**Q1 — the timing passage (the row's anchor quote; 18 words):**
> "with all four major livestock species coming under management over a period from ca. 11,000 to 10,000 B.P."
Location: §"Initial Animal Domestication in the Fertile Crescent", **penultimate paragraph** (begins "Animal domestication in the Near East can then be seen as arising from a period of prolonged human interaction…"), PMC full text.

**Q2 — the management-before-morphology claim (22 words):**
> "Evidence for herd management and crop cultivation appears at least 1,000 years earlier than the morphological changes traditionally used to document domestication."
Location: **Abstract**, third sentence.

**Q3 — the herder's demographic signature (24 words):**
> "the clear signature of a managed herd of goats (harvesting of young males and prolonged survivorship of females) at the site of Ganj Dareh"
Location: §"Initial Animal Domestication in the Fertile Crescent", **third paragraph** (begins "Application of this approach to archaeological assemblages from Iraq and Iran…"), Ganj Dareh directly dated to 9,900 B.P. with **no size reduction**.

Gate block for `corpus/lessons/round-50.md` (scribe can paste): the three quotes above with their locations, the PMC URL, access date 2026-10-21, the PNAS 403, and "no erratum on PMID 18697943".

## 4. Per-species and per-region detail the entry can actually use (paraphrase, located)

All from §"Initial Animal Domestication in the Fertile Crescent" unless noted; these are **observations of the paper**, marked with the paragraph they sit in, not free-standing facts.

- **Sheep and goats**: brought under domestication "probably independently of one another and possibly multiple times" in the northern Zagros–southeastern Anatolia belt, **ca. 11,000–10,500 B.P.** (paragraph 5). The *order* is regional and reverses: goats first in the Zagros (Ganj Dareh), but **sheep are the initial focus in southeastern Anatolia, managed goats arriving there ca. 10,200 B.P.** (same paragraph). Managed goats then move fast — southern tips of both Fertile Crescent arms by ca. 9,500 B.P. — while domestic sheep arrive ≈500–1,000 years later (paragraph 5).
- **Cattle**: taurine cattle initially domesticated in the upper Euphrates valley **ca. 11,000–10,000 B.P.** (paragraph 6).
- **Pigs**: southeastern Anatolia by **10,500–10,000 B.P.** (paragraph 6).
- **Morphology lags**: clear morphological responses (horn change in bovids, tooth size in pigs) are not evident until **ca. 9,500–9,000 B.P.** (paragraph 7).
- **The old marker is wrong**: body-size reduction was believed the marker, but sex and heat/aridity drive size in these ungulates; what looked like domestication-driven dwarfing is the **culling signature of herders vs hunters** — hunters take large prime males, herders slaughter post-prime females and harvest excess young males (paragraphs 3–4). This is a calibration-grade myth to flag, not just a fact.
- **Diffusion** (§"The Diffusion of Animal Domesticates in the Mediterranean Basin"): the package moves as a package — Cyprus colonists at 10,500–9,000 B.P. brought **all four livestock species** plus fallow deer and fox, none endemic, plus einkorn/emmer/lentils/barley/figs/pistachios/flax; the animals arrived **morphologically wild but demographically managed**. Multiple seaborne waves, then selective local adoption and integration; pigs, rye and oats are the counter-case of **local** European domestication. Timing of the spread is explicitly non-uniform: Cyprus→Aegean 2,000 years, Aegean→Italy 500, Italy→Atlantic 500–600.

## 5. Scope, tier and recheck — the honest edges

- **Scope in one line**: *the 2008 published state of evidence on Fertile Crescent livestock domestication timing and Mediterranean diffusion.* Everything else is out of scope.
- **Not a source for**: transhumance, mobile pastoralism, commons/territory tenure, bridewealth, herd wealth-as-capital, pastoralist social organisation — the paper is archaeozoological and says nothing systematic about these (that is `SrcFaoPastoralism`'s and the ethnographic rows' job). Using it there would be scope creep and would break the one-owner discipline.
- **Not a source for**: the founder-crop *list* — see §6.
- **Dated by 18 years**: later aDNA and radiocarbon work has refined these numbers. The row must be cited as *"Zeder 2008 reports…"*, never as "the domestication date is". Tier A is for the paper's own content; any sentence presented as current consensus needs a post-2015 synthesis.
- **Recheck: 365d**, with a trigger rather than a clock: re-open before any in-world herding chronology becomes load-bearing in a bible, and immediately if a post-2015 aDNA survey contradicts a date used.
- **Regional trap to put in the entry's calibration bank**: these are Fertile Crescent and Mediterranean dates. They are not a template for a fictional world's herding origins, and the paper itself shows the order and tempo vary by region — which is the licence, not a defect.

## 6. What it teaches the entry, by section

The entry does not exist yet, so I map to the model outline's conventions (`hunting-foraging-subsistence.md` §1/§3/§13; `agrarian-field-system-lexicon.md` §3/§10) and give a fallback placement.

1. **§1 register property — the hunting/herding boundary.** Q2 is the load-bearing claim: herding is a *management relation* that exists for centuries while the animals still look wild. Design consequence: a world's herding origin is a **slow conversion of hunting practice**, not an invention event, and the entry should refuse "the year herding was invented". This is also the sharpest discriminator against `hunting-foraging-subsistence.md` §3 Locate/Acquire: both take live animals; only one manages the breeding stock.
2. **§3 production chain, herd-composition link — culling as the design rule.** Q3 supplies a concrete, checkable rule: keep females past prime reproductive age, harvest excess young males. That is a *herd structure* the entry can state as a table row (age/sex class → fate → product), and it doubles as the archaeological signature that distinguishes herding from hunting.
3. **Chronology / deep history (own section if the outline has one; else §1).** Q1 plus §4 gives an order-of-magnitude table by species with an explicit "regional, not universal, order" caveat.
4. **Origins and diffusion (own section; else §1 or the build-order section).** Package arrival by sea vs piecemeal adoption vs local domestication gives three distinct scenario shapes for a world's herding complex — and the paper's own Cyprus case is the worked template (full faunal package moved by boat, animals managed but morphologically wild).
5. **§13 calibration bank — three flags this row earns:**
   - *"body-size reduction marks domestication"* — **discredited** for caprines here; it is a culling signature (paper paragraphs 3–4). Flag before it reaches a bible.
   - *"domestication happened at date X"* — the paper's own thesis is that the threshold is "more a semantic issue than a substantive research question" (§"Future Research"). Flag any single-date claim.
   - *"sheep before goats"* (or the reverse) — regionally true both ways; flag any universal species order.

## 7. Cross-links inside the lane (for the integrator, not edits I made)

- `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:101` carries `Zeder 2006 — to-verify` for the founder-crop list. **This row does not discharge it**: Zeder 2008 names the Cyprus founder set (einkorn, emmer, lentils, barley, figs, pistachios, flax) but does not present "the standard list". Leave that `to-verify` standing.
- `hunting-foraging-subsistence.md` §3 (Acquire) and its §2 boundary table are the seam the new entry must cite in reverse: this row's Q2/Q3 are the *management* side of the same animals. No edit needed there this round; the new entry's §2 owns the statement.
- `corpus/knowledge/civilizations/` and `myth-symbol/animal-symbolism.md` remain untouched by this row — no herding-specific claim is made here.

## 8. Unrun checks (explicitly not done, and why)

- Did **not** open the PNAS PDF (`/doi/pdf/…`) after the landing-page 403 — same host, same block expected; PMC gave the published text.
- Did **not** verify the numbers against a post-2015 synthesis (no such row opened this round; that is the declared recheck trigger, not a gap I can close in this seat).
- Did **not** run any lane gate, sweep, or selftest — not this seat's assignment, and the entry does not exist yet.
- Did **not** open S032-style paywalled bodies; none were needed.
- No file outside this report was written; no git/jj command run at all.
