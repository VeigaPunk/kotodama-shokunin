# Round-58 outside-verifier spot-check routing

## Spot-check intake (round-58 outside verifier)

| Item (round-58-verifier-spotcheck.md:line) | Finding | Route | Status |
|---|---|---|---|
| §5 item 1 (round-58-verifier-spotcheck.md:142–145) | Eleven lane-root strays were attributed to ExecReasonSweep58: `carriers.txt`, `flagged_rows.txt`, `locator_diff.txt`, `met_check.txt`, `plwiki_check.txt`, `s313_check.txt`, `s435_entry.txt`, `s452_locate.txt`, `tier_rule.txt`, `uncited_terms.txt`, and `wayback_rows.txt`. Round-59 records their removal and the wave-directory/scratch write boundary. | Round-59 deleted-stray-files record and the seat wave-containment rule. | pending |
| §5 item 2 (round-58-verifier-spotcheck.md:146) | The revision count was six, not five; `31cf8b6` added the TOPIC leg and was omitted from the round-58 report, SCORECARD, and `claims.json` revision note. | Round-59 lesson erratum and SCORECARD correction row. | pending |
| §5 item 3 (round-58-verifier-spotcheck.md:147) | The declaration/freeze account overstated that no seat had scored; distinguish the initial declaration, control-forced revisions, and final freeze. | Round-59 `claims.json` fields `declared_at`, `revision_note`, and `freeze_note`, plus the lesson erratum. | pending |
| §5 item 4 (round-58-verifier-spotcheck.md:148–150) | “123 controls, 0 pass” overstates discrimination where a control can fail only because reviewer evidence is missing; retain the per-leg split and distinguish controls that met a counter. | Round-59 lesson erratum and `reports/round-59/telemetry/controls-c.txt` per-leg classification. | pending |
| §5 item 5 (round-58-verifier-spotcheck.md:151) | Two live 403s sank the no-slack predicate; round 59 froze FETCH-59 before data, including the same-page capture rule, and routed the lesson to QUALITY criterion 13. | `reports/round-59/rowcheck.py` FETCH-59 contract and QUALITY criterion 13. | pending |
| §5 item 6 (round-58-verifier-spotcheck.md:152) | The old C lands omitted SUPPORT inputs; round-59 C's declared lands list the support registry, planted evidence, hashes, reviewer reports, and packets. | Claim C's declared lands in `reports/round-59/claims.json` and `reports/round-59/separability-manifest.json`. | pending |
| §5 item 7 (round-58-verifier-spotcheck.md:153) | Twelve Kongo lines had verified fixes carried for a third round; round-59 claim D declares the frozen Kongo substitutions (and the separate speech-surrogate remaps). | Claim D and `reports/round-59/d-fixes.json`. | pending |
| §5 item 8 (round-58-verifier-spotcheck.md:154) | Round 58's census was late; the round-59 start census receipt records a census at 2026-10-23T02:33:32Z against lane tip `1542f7a2…`, with `exit=0`. | `reports/round-59/telemetry/census-start.txt`. | pending |
| §4 quality verdict (round-58-verifier-spotcheck.md:134–137) | Quality was graded harmed because the verified Kongo fixes remained unapplied for a third round; do not change that verdict based on routing alone. | Claim D's Kongo fix set and predicate (`reports/round-59/d-fixes.json`, `reports/round-59/claims.json`). | pending |

## Evidence and limits

- Read the complete round-58 outside-verifier spot-check (lines 1–158) before drafting. Read the round-59 frozen `claims.json` first, then the D fixes, rowcheck FETCH-59 contract, C lands/separability manifest, control-C receipt, and start-census receipt.
- The start-census artifact itself records command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`, output `kotodama ok …/corpus/SOURCES.md`, and `exit=0`; this is receipt evidence, not a command run by this seat. The control receipt records the requested per-leg split; no controls were run here.
- `corpus/lessons/round-59.md` was not present when checked. This file is the scoped draft for the L1 to integrate; no lesson, SCORECARD, claim, source, or product file was edited by this seat.
- No acceptance gate, test, network fetch, or census command was run for this assignment. Every row is deliberately `pending` for the L1; this report does not assert that any repair landed or any round-59 predicate passed.

## Touched surfaces

- Created only this assigned report: `.ufo/waves/round-59/build/ScribeSpotcheckRouting59.md`.
- Read-only inputs: `corpus/lessons/round-58-verifier-spotcheck.md`; `reports/round-59/claims.json`; `reports/round-59/d-fixes.json`; `reports/round-59/rowcheck.py`; `reports/round-59/separability-manifest.json`; `reports/round-59/telemetry/controls-c.txt`; `reports/round-59/telemetry/census-start.txt`.

## Out of scope

No source-row research or rowcheck, claim C/D execution, lesson/SCORECARD integration, edits beyond this report, tool installation, or commit operations.
