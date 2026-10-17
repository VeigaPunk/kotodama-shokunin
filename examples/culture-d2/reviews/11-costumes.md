# Review — component 11-costumes (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/11-costumes.yml` (522 lines, 56,971 bytes; final revision 2026-10-17 11:40:28 local)
- reviewed revision: sha256 `d9da1382d4a144b498c95b4e654d9d86b8047f5842efecd6d7f4702937cac43e`
- status: **CLEAN** — no corpus-forbidden violation found
- canon: not canonized (D2 design drill)

## Delivery history (why the revision is pinned)

- Look 1 (~11:24): `examples/culture-d2/` did not exist; the 60 s
  wait-and-retry per assignment protocol still found nothing (11:26:37).
  The grace window was kept open while sibling components landed in a wave
  (11:27–11:35; 13 components on disk before 11-costumes).
- Delivered ~11:34. While under review the file was revised three more times
  (11:36:03, 11:38:01, 11:38:54–11:40:28): material ids re-lettered MAT→CMAT
  against 10-materials' MAT-01..22 space, the contract era space extended to
  E0–E3 with an alias rule and a slot-level `era_reconciliation` table added,
  the storm-slate dye withdrawn in favour of CMAT-09 hearth-dark (mapped to
  10-materials MAT-10), and OQ-3/OQ-6/OQ-7 opened.
- Intermediate revision `c6f66e1d…` (11:38) failed its own gate with two
  MAT-04 holds (GAR-02/GAR-05 dye availability in E0). The final revision's
  `validation` block claims a clean re-run; that claim is **verified below on
  the final bytes**, not taken on trust. Intermediate states are history, not
  findings against this revision.
- Final revision stopped changing at 11:40:28 and was byte-stable across four
  checks to 11:45:11. Reviewed on those bytes.

## Violations

None. No entry of the form
`11-costumes | <violation> | <corpus path:section that forbids it>` was found.
One seed-level residue is recorded in its own section below (not a corpus
violation).

## What I checked

Corpus read in <=80-line chunks: `corpus/knowledge/culture-material/dress-through-eras.md`
(full), `textile-technology.md` (full), `sumptuary-law-rank-display.md` (full),
`costume-semiotics.md` lines 1–75 (§1–§6), `ritual-garments.md` (full),
`garment-lexicon-crosslinguistic.md` (full),
`corpus/knowledge/verification/costume-era-consistency-gate.md` (full).

1. **Executable gate on the reviewed bytes** —
   `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d2/components/11-costumes.yml`
   → **exit 0, no FINDING lines**, matching `validation.exit_code: "0 (clean)"`
   and `validation.findings`. (The same command on the 11:38 intermediate gave
   exit 1 / two MAT-04 holds; the final bytes pass.)

2. **Material availability, garment by garment** (the assignment's first check;
   `textile-technology.md:§1` four gates, `:§2` fiber hierarchy;
   `dress-through-eras.md:§11.2` "no dye or fiber without a supply chain";
   `costume-era-consistency-gate.md:§4` MAT-02/MAT-03 import staging):

   | Record | Material (id) | Declared route | Era gate | Verdict |
   |---|---|---|---|---|
   | GAR-01 | felt (CMAT-02) | local: fleece → felt table CS-03 → cut/sew | E0 | plausible; non-woven, bound by CS-03 not a loom |
   | GAR-02 | felt + hearth-dark (CMAT-02/09) | local, first shear, fulled twice; local smoke-darkening | E0 | plausible; chemistry deferred to 10-materials MAT-10 |
   | GAR-03 | felt (CMAT-02) | local + hem-cord manufacture | E0 | plausible |
   | GAR-04 | lowland plant-thread cloth (CMAT-06) | import stage=cloth, excluded E0 | E1–E2 | plausible as declared import; no D2 fiber stage claimed |
   | GAR-05 | wool (CMAT-01) | local band warp on CS-02 + hearth-dark | E0 | plausible |
   | GAR-06 | silk (CMAT-08) | import stage=cloth, E2 only; never reared/reeled/spun/woven in D2 | E2 | plausible late treaty grade; flagged by the file as unmapped in 10-materials (OQ-3) |
   | GAR-07 | felt (CMAT-02) | local, deliberately unfinished | E0 | plausible |
   | GAR-08 | lowland cord (CMAT-07) | import stage=trim, E1–E2; never worn as dress | E1–E2 | plausible; the exception channel is in-world law, not a material stretch |
   | GAR-09 | pack-ox down (CMAT-03) | local fiber → hand-spin → CS-01 narrow weave → pieced panels | E0 | plausible within the declared herd; finest-fiber role matches `textile-technology.md:§2` minor-fibre lever; flagged unmapped (OQ-3) |
   | GAR-10 | leather (CMAT-04) | local hide → smoke cure → cut to piece, no yarn/cloth stage | E0 | plausible; route honest about the missing stages |

   No garment claims a fibre or a dye without a declared kind+stage route;
   imports name their stage (cloth/trim) and carry era gates, so no local
   manufacture is smuggled (`costume-era-consistency-gate.md:§4`).

3. **rank/rite/era completeness** (the assignment's second check) — a
   line-parser ran over the reviewed bytes: all 10 costume records carry
   `garment`, `material`, `wearer_rank`, `rite`, `era` (plus route, axis,
   evidence, follows); all 9 material records carry composition, `maps_to`,
   axis, evidence, follows, routes; all 3 cloth sources carry `max_width_m`,
   eras, axis, evidence, follows. Counts 10/9/3 match `validation.counts`.
   No rank/rite/era field is empty. `dress-through-eras.md:§10` ledger columns
   are readable per record: who-may-wear = `wearer_rank`, occasion = `rite`,
   enforcement = `penalty` + the `enforcement` block, era-of-change =
   `era_seam` / `reading_ledger.era_of_change`. The silhouette slot is not a
   named field but is carried in `rank_mark`/construction (hem-cords,
   wind-flap, placket, no inner seam) — noted, no violation.

4. **Loom and felt ceilings** — CS-01 0.65 m / CS-02 1.25 m bound the woven
   records; GAR-01's 1.7 m seamless felt panel is bounded by CS-03 (1.9 m felt
   table) under the file's own `loom_note`; GAR-09 pieces panels because CS-01
   cannot span a body (`textile-technology.md:§4` width = loom width, `:§5`
   finishing; `costume-era-consistency-gate.md:§5` seamless-panel test).

5. **Wearer-rule mechanics** — `dress-through-eras.md:§10` requires >=2
   enforcement mechanisms: the file names three (rite; rank institution;
   market/monopoly) with per-row corpus cites, and delegates all rule text to
   12-rank-rules by id (no duplication). The regulated marks are assayable
   (cord count/position, flat hem, cut-back cords), matching
   `sumptuary-law-rank-display.md:§2` ("laws regulate a measurable surrogate";
   a ban with no assay is decorative).

6. **Dye/colour division of labour** — CMAT-09 hearth-dark declares
   makeability only, explicitly disclaims the tannin-iron wool-black and the
   traded indigo, and defers hue meaning to 08-symbols S1 — the division the
   corpus assigns (`textile-technology.md:§3` dye classes; colour meaning owned
   by `myth-symbol/color-symbolism.md`, cited by the file as S1's owner).

7. **Rite/lifecycle** — `ritual-garments.md:§1` garment-as-office (GAR-05 sash
   issued and surrendered with the standard), `:§6` mourning year as a
   liminal, time-locked sequence (GAR-07, CAL-5) with a deliberate inversion
   of the cord count.

8. **Misread test** — `dress-through-eras.md:§11.7` and
   `costume-semiotics.md:§1`: five misread scenes (MRS-1..5), each with a
   payoff; the hem device of `dress-through-eras.md:§9` is re-read vertically
   (MRS-1, "answers by unrolling the hem").

9. **Drift and era legibility** — `drift_plan` DR-1..4 with a dated founding
   fight; the debunk shelf of `dress-through-eras.md:§12` ("no timeless
   costume without a dated founding scandal") is satisfied. Era names and
   dates are deferred to 09-eras-calendar (`era_note`), so no date is asserted
   here (`costume-era-consistency-gate.md:§7` clocks kept separate).

10. **Provenance / canon hygiene** — `canon: not canonized (D2 design drill)`
    present; every record carries `follows` (RG-02 stated in
    `follows_scope_note`); all citations resolve to repo corpus path+section
    (`follows_index`) or named contract fields; no external scholarship
    invented; the calibration block separates design-choice / corpus-derived /
    bounded analogy; `canon_boundary` closes to lore-shokunin
    (`corpus/QUALITY.md:§1` provenance, `:§5` canon hygiene).

11. **Spine coupling and D1 anti-import** (authority: round D2 seed + the
    file's own `anti_import` claim, not a corpus path) — `spine_coupling`
    SPC-1/SPC-2 name the two axes with record ids; every record carries
    `axis`, and the neutral records carry explicit coupling notes (CMAT-05,
    CMAT-07, GAR-08). One residue found, below.

## Seed-level residue (not a corpus violation)

- `11-costumes | GAR-08 wearer_rank says "counts bales at the mooring" — a
  water/vessel word in a file that declares "No river, bank, tide, ford or
  flood imagery" (line 26) | authority: round D2 seed + the file's own
  anti_import line; no corpus path forbids it.`
  Severity: low (one word in a role description). Fix: one word
  ("caravan yard" / "loading line"), or mark the partner's berth explicitly
  and amend the anti_import sentence. The rest of the grep sweep is clean:
  no river/bank/tide/ford/flood vocabulary (the "ford" hit inside "afford" is
  a substring artifact); "bind" appears only as manufacture/design prose; no
  knot metaphor; obligations are pasture rights, never ties.

## Review-class observations (not violations, for the assembler)

- **OQ-1 era-label plurality** — siblings label eras differently (12-rank-rules
  era-1..3; 08-symbols / 10-materials E1..E4; 05-lexicon Nalne/Pertne;
  14-kin-address ES0-ES3). The file's `era_reconciliation` proposes the
  slot-level mapping and warns against numeric merge (its ERX-W). The
  integrator should adopt that table or publish its own before assembly.
- **OQ-3 material conflicts with 10-materials** — pack-ox down (CMAT-03) and
  silk (CMAT-08) have no counterpart in that component's inventory; the file
  carries them as REPORT-don't-merge. From the material-availability side both
  routes are declared and plausible, so this component passes on either
  resolution (extend the inventory, or re-letter GAR-06 to broadcloth).
- **OQ-6 felt-grade slots** — 12-rank-rules licenses "felt grades through G3";
  the records say "heavy winter grade" / "fine first-shear" without stamping
  G1/G3. Integration stamping owed.
- **OQ-7 packet-key overlap** — both this file and 10-materials supply
  `materials` / `cloth_sources`; merge by the CMAT→MAT slot mapping per the
  file's own instruction.
- **RCN-02 registration** — supplied in-file for the integrator (CMAT- and
  LEX-GAR- prefixes declared as new).
- **Not verified here (scope)** — sibling components were not opened except
  where this file cites them; the `era_reconciliation` rows and OQ items are
  the file's proposals, flagged (to-verify), for the integrator.

## Re-run condition

Pinned to sha256 `d9da1382…`. If a further revision is delivered
(supersede-by-new-file), re-dispatch a review against the new bytes; nothing
here is a finding about any later revision. The component was not edited; this
review file is the only artifact written.