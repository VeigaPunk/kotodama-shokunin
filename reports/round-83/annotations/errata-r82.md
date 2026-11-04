# Erratum — R82-M2 line number (round 83)

**Filed at round 82.** The round-82 report's R82-M2 parenthetical and `corpus/lessons/round-82.md` `## Mistakes` row R82-M2 say the malformed 12-cell probe answered `RECHECK-ERROR line 7: row has 12 cells, expected 11`.

**Committed.** The tracked probe `.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt` prints `RECHECK-ERROR line 5: row has 12 cells, expected 11` (exit 2) for the 12-cell fixture and `line 5` for the 10-cell fixture; the committed fixture `.ufo/waves/round-82/w1/stage/ExecEvidence/probes/12-cell-row.md` places the malformed row at line 5. No receipt under `reports/round-82/telemetry/` prints a `RECHECK-ERROR` line (measured at base `3088bd7fe2a55a123214abba7008dcddf12b301c`), so `line 7` has no committed support.

**Disposition.** The filed bytes stand as history: this erratum names the discrepancy and does not edit the round-82 report, the lesson row, or the probe. The authoritative reading is the committed probe's `line 5`.

**Routed item 7 (claim-O before-wording).** The round-82 spot-check's seventh routed item asked that claim O's before-state read "no tool derived a due date or queue" rather than "nothing read the registry's `recheck` cells". Round 83 carries the narrower wording forward in every claim-O artifact it files: `reports/round-83/claims.json` claim O's `before` names the missing rows and the absent `GATE-REGISTRY` reader, and the round report states the claim as "no committed instrument derives the registry's coverage". The round-82 report's broader sentence stands as history, not as a re-measured claim.
