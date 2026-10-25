# Round-69 corrections — the filed round-68 self-assessment

Append-only corrections to the filed round-68 self-assessment. The filed
round-68 bytes are never rewritten (append-only discipline, CORPUS.md rule 2):
every correction below is a NEW row that names the class and the surface it
corrects, and each row carries the command that re-derives the observation.
`reports/round-69/accept-ca.py` counts the mismatches that no row here
covers; its `MISMATCHES` leg must print `unannotated_mismatches=0`.

Declared classes (frozen at `reports/round-69/claims.json`, `calibration_pairs`):
LEGCOUNT — a filed surface claims a legs-pass count the committed receipt does
not support; DEADPOINTER — a filed surface points at a mistake row that does
not exist; OVERREACH — a filed surface claims an improved axis verdict the
committed receipt contradicts.

| class | surface | filed text | observed text | re-derivation command | correction appended where |
|---|---|---|---|---|---|
| LEGCOUNT | SCORECARD.md | `ACCEPT-O-68 9/10 legs PASS at A_c` (round-68 operability row) | the committed receipt prints 9 legs: 8 PASS and 1 FAIL (EXEC) — the claim says 9 of 10 | `grep -cE '^[A-Z0-9_]+ (PASS\|FAIL) ' reports/round-68/telemetry/final-measures-o.txt` → 9; the same grep with `PASS` → 8 | `SCORECARD.md` round-69 corrections table; `LOG.md` round-69 entry; `corpus/lessons/round-69.md` `## Corrections` |
| LEGCOUNT | LOG.md | `ACCEPT-O-68 prints 9/10 legs PASS at A_c` (round-68 LOG entry) | the committed receipt prints 9 legs: 8 PASS and 1 FAIL (EXEC) — the claim says 9 of 10 | `grep -cE '^[A-Z0-9_]+ (PASS\|FAIL) ' reports/round-68/telemetry/final-measures-o.txt` → 9; the same grep with `PASS` → 8 | `LOG.md` round-69 entry; `corpus/lessons/round-69.md` `## Corrections` |
| LEGCOUNT | .ufo/reports/round-68/kotodama.md | `ACCEPT-O-68 prints 9/10 legs PASS` (line 10) and `9/10 legs PASS, exit 1` (line 29) | the committed receipt prints 9 legs: 8 PASS and 1 FAIL (EXEC) — the claim says 9 of 10 | `grep -cE '^[A-Z0-9_]+ (PASS\|FAIL) ' reports/round-68/telemetry/final-measures-o.txt` → 9; the same grep with `PASS` → 8 | `LOG.md` round-69 entry; `corpus/lessons/round-69.md` `## Corrections` (the fleet report is outside the lane's write scope and is not edited) |
| DEADPOINTER | .ufo/reports/round-68/kotodama.md | `## Mistakes` R68-M1..M8 (+M9 in LOG) (line 35) and `Ca fails as declared` (R68-M9) (line 11) | no R68-M9 row existed in `LOG.md` or `corpus/lessons/round-68.md` — the pointer never resolved | `grep -c 'R68-M9' LOG.md corpus/lessons/round-68.md` → 0 before this round | the missing R68-M9 row is appended in `corpus/lessons/round-69.md` `## Mistakes` and named in the `LOG.md` round-69 entry (the fleet report is outside the lane's write scope and is not edited) |
| OVERREACH | SCORECARD.md | `\| calibration \| improved (claim Ca, records) \|` (round-68 calibration row) | the committed round-68 calibration receipt carries a `NameError: name 'git_bytes' is not defined` traceback and never prints `ACCEPT-CA-68: PASS` — the claim did not verify | `grep -c 'ACCEPT-CA-68: PASS' reports/round-68/telemetry/final-measures-ca.txt` → 0 | `SCORECARD.md` round-69 corrections table; `LOG.md` round-69 entry; `corpus/lessons/round-69.md` `## Corrections` |

## Why the r68 counters are not amended

The round-68 calibration counter crashed at `accept-ca.py:224` on an undefined
`git_bytes` helper and was frozen post-data (kumitate r42 class). This round
does not amend it: `reports/round-69/accept-ca.py` is a NEW counter and its
`R68FROZEN` leg re-derives the round-68 counters' sha256 against the sha256
their own receipts recorded. The same holds for the round-68 operability
counter, whose EXEC fixture never created the used-by file (R68-M1): the
repair is the new counter `reports/round-69/accept-o.py` plus the new harness
`tools/check-settlement-fixture.py`, and the `R68FROZEN` leg of
`reports/round-69/accept-o.py` proves the round-68 bytes are unchanged.
