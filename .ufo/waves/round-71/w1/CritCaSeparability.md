# CritCaSeparability — claim Ca causal separability review (round 71, wave 1)

Seat: `L1Kotodama71.CritCaSeparability` (leaf, read-only).
Read: `reports/round-71/claims.json` (claim Ca surface/predicate/counting_command), the
round-70 verifier spot-check `corpus/lessons/round-70-verifier-spotcheck.md` §6 (the routed
defects V70-1..V70-6), and the current lane tree (pre-landing state, checked 2026-10-25).

## Verdict

**The five V70-1..V70-5 landings are NOT pairwise file-disjoint.** Two overlaps exist:

1. **`corpus/lessons/round-71.md`** (round-71 lesson, does not exist yet) is written by
   **V70-2** and **V70-5**.
2. **`.ufo/reports/round-71/kotodama.md`** (the round-71 fleet report, does not exist yet) is
   written by **V70-3**, **V70-4** and **V70-5**.

**Claim D is disjoint from every file claim Ca touches**: D writes only the new counter
`reports/round-71/accept-d.py` (plus its own receipts inside `reports/round-71/telemetry/`,
distinct filenames) and reads the frozen `reports/round-69/accept-d.py` via importlib. No
same-file write with any Ca file.

## Per-landing write maps (evidence-grounded)

| landing | files written | basis |
|---|---|---|
| V70-1 (receipt headers) | `reports/round-70/telemetry/measures-o.txt`, `measures-ca.txt`, `measures-d.txt`, `controls-o.txt`, `controls-ca.txt`, `controls-d.txt` (6 in-place edits) | claims.json:31(1); spotcheck:126. Current state: all six carry only the single-line header `# after-state receipt … measured at lane 6cb51a4+landed edits` — no 17/19 block (read). |
| V70-2 (S860 repoint) | `corpus/SOURCES.md` (S860 anchor cell, in-place repoint to acc2d614) + `corpus/lessons/round-71.md` (old→new log, new file) | claims.json:31(2),33,34; spotcheck:127 ("log old→new in the next lesson"). Current state: S860 row (`SOURCES.md:815`) still pairs blob `6a314e9c…` with "lane revision 6cb51a44…". |
| V70-3 (quote discipline) | `corpus/lessons/round-70.md` (trim 27-word Gate quote to ≤25) + `.ufo/reports/round-71/kotodama.md` (report must stop calling it "25 words") | claims.json:31(3); spotcheck:128. Current state: round-70.md:13 quote = **27 words** (verified by whitespace split); round-70 fleet report `.ufo/reports/round-70/kotodama.md:101` says "a 25-word located quote". |
| V70-4 (trend verdicts) | `SCORECARD.md` (append trend-correction row) + `.ufo/reports/round-71/kotodama.md` (trend-correction section) | claims.json:31(4); spotcheck:129. Current state: `grep -c trend SCORECARD.md` = 0 (unlanded). |
| V70-5 (Gate completeness + item-10) | `corpus/lessons/round-71.md` (reject-sweep statement + ≥1 frontier-refusable candidate with reason+flip) + `reports/round-71/telemetry/quarantine-verdicts.md` (21-row verdict table, new) + `.ufo/reports/round-71/kotodama.md` (item-10 verdicts "land in the lesson and report") | claims.json:31(5),33,34; spotcheck:130. Current state: no round-71 lesson, no verdict table. |

Shared files:
- `corpus/lessons/round-71.md`: **V70-2 ∩ V70-5**
- `.ufo/reports/round-71/kotodama.md`: **V70-3 ∩ V70-4 ∩ V70-5**

## Discrepancy with the dispatched mapping

The dispatched task text maps "V70-3 and V70-5 touch corpus/lessons/round-71.md". Ground truth
(claim surface + verifier fix column) says V70-3's lesson write is **corpus/lessons/round-70.md**
(trim the round-70 Gate quote) — not round-71.md — and that V70-3's second write is the round-71
fleet report. Either mapping yields an overlap (dispatched: V70-3∩V70-5 on round-71.md;
ground truth: V70-2∩V70-5 on round-71.md and a three-way overlap on the report), so the
separability attack stands regardless.

## Claim D vs claim Ca — disjointness

- D writes: `reports/round-71/accept-d.py` (new counter; verified, currently present as the
  scaffold), plus its own after-state receipt under `reports/round-71/telemetry/` (e.g.
  `measures-d.txt`; `controls-d.txt` already committed at declaration). Its selftest/no-git
  reproduction writes only to `mktemp -d` scratch.
- D reads `reports/round-69/accept-d.py` (frozen counter, importlib import — no write) and
  never touches any of Ca's six files (round-70 receipts, SOURCES.md, lessons, SCORECARD.md,
  fleet report, quarantine-verdicts.md).
- Shared directory `reports/round-71/telemetry/` contains both claims' receipts, but all
  filenames are distinct (`measures-{o,ca,d}.txt`, `controls-{o,ca,d}.txt`, `quarantine-verdicts.md`).
  **No same-file write.** D ⊥ Ca holds.

## Secondary observations (verification-command gaps, not separability)

1. Ca's counting leg 1 greps `reports/round-71/telemetry/measures-{o,ca,d}.txt` and
   `controls-{o,ca,d}.txt` for the six-line headers — but V70-1's landing edits the **round-70**
   receipts. The declared leg cannot observe the landing; it would pass if round-71's own (new)
   measure receipts carry headers, even if the round-70 receipts stay unstamped. This is a
   vacuous-pass vector on the V70-1 leg (sibling seat `CritVacuousCounters` covers the class).
2. The check-gate-quotes leg scans only `corpus/lessons/round-71.md`; the V70-3 trim target is
   `corpus/lessons/round-70.md`, so the trimmed quote is not directly verified by the declared
   command.

## Smallest safe corrections

- Move V70-2's old→new log out of the lesson into **`reports/round-71/corrections-r70.md`**
  (exact precedent: round-70's per-defect dispositions live in `reports/round-70/corrections-r69.md`).
  Lesson then only cross-references. This removes the V70-2∩V70-5 overlap on round-71.md.
- Keep the round-71 fleet report as a **single-writer summary**: per-defect record bodies go in
  per-defect files (SCORECARD row, corrections-r70.md, quarantine-verdicts.md, the six round-70
  receipts, SOURCES.md), and the report only summarizes/cross-references — authored once, not
  three concurrent writers. If V70-3/4/5 must each contribute report sections, they must be
  sequenced under one owner (the L1 main), never fan out to parallel executors/wave seats.

## Evidence

- `reports/round-71/claims.json:31-35` (Ca surface/predicate/counting_command)
- `corpus/lessons/round-70-verifier-spotcheck.md:126-131` (V70-1..V70-5 required fixes)
- `corpus/lessons/round-70.md:13` (Gate quote, 27 words — whitespace split)
- `corpus/SOURCES.md:815` (raw S860 row; blob/revision pairing still `6a314e9c…`@`6cb51a44…`)
- `reports/round-70/telemetry/{measures,controls}-{o,ca,d}.txt` (single-line headers, no 17/19 block)
- `reports/round-71/telemetry/controls-ca.txt`, `controls-d.txt` (pre-data controls: 0 matches,
  no lesson/verdict table, no measures-* yet)
- `SCORECARD.md` (0 `trend` matches)
- `.ufo/reports/round-70/kotodama.md:101,109-121` ("a 25-word located quote"; Trend verdicts
  expansion/quality/discernment improved)
- `reports/round-71/accept-d.py` (imports frozen `reports/round-69/accept-d.py`; no writes)
- `.ufo/waves/round-71/w1/plan.json:304,309,329,414` (dispatched task texts)
