# Corrections — round 70 (2026-10-25, applied in round 71)

Per-defect dispositions for the round-70 verifier spot-check defects V70-1..V70-5
(`corpus/lessons/round-70-verifier-spotcheck.md` §6). Each row: id · class ·
surface · old state · landing.

| id | class | surface | old → new | landing |
|---|---|---|---|---|
| V70-1 | receipts vs the lane's own bar | the six round-70 telemetry receipts (`measures-{o,ca,d}.txt`, `controls-{o,ca,d}.txt`) | single-line header `# after-state receipt … measured at lane 6cb51a4+landed edits` (no QUALITY 17/19 block) → each file now opens with the six-line 17/19 header (`# counter sha256 (self):`, `# stamped revision:`, `# evaluated revision:`, `# measured revision (lane main):`, `# tree:`, `# worktree dirty (tracked):`) and the original bytes preserved below `# original bytes preserved below` | re-stamped in place, round 71 |
| V70-2 | evidence pointer accuracy | `corpus/SOURCES.md:815` (S860 verify-at cell) | paired hardened blob 6a314e9c… with lane revision 6cb51a4 (blob first exists at acc2d614) → cell names `acc2d614a097484d8dc41230229dc4ead07d8a19` | in-place recheck-class change, round 71; old → new logged here |
| V70-3 | quote discipline | `corpus/lessons/round-70.md` `## Gate` S860 quote | 27-word quote (…not globally...)") → 25-word contiguous prefix (…for the frozen ruling set,") | trimmed in place, round 71; claim the round-71 report calls it a 25-word located quote |
| V70-4 | trend verdicts vs observables | `.ufo/reports/round-70/kotodama.md` §Trend verdicts | `expansion: improved`, `discernment: improved` contradicted LEARNING.md observables (no knowledge entry; no gate decision/new criterion) → correct verdicts per LEARNING.md: expansion `unchanged`, quality `unchanged`, discernment `unchanged` (CritTrendObservables wave-1 seat) | recorded as a SCORECARD correction row (round-71); the filed round-70 report bytes are untouched |
| V70-5 | gate completeness | `corpus/lessons/round-70.md` `## Gate` | one candidate admitted, no reject row and no "rejected this round: none" statement → the round-71 lesson `## Gate` states `rejected this round: <sweep>` and opens ≥1 frontier-refusable candidate with reason + flip | landed in `corpus/lessons/round-71.md` |
