- Seat: Ca10 | executor | claim Ca | date 2026-10-19 | baseline 57c8409

# Ca10 — calibration receipt draft

Scope: draft receipt for round-37 claim Ca. This is not a recount verdict: the available round-37 fragments report an unassembled ledger and could-not-evaluate coverage; completed recount results and the two required independent samples remain unavailable.

## Declared contract

Claim Ca requires recounting every acceptance counting command filed in rounds 33–36, including rejected round 36, and dispositioning each as a match or a named mismatch with cause. The required after-state is a row for each filed command, with zero un-reproduced commands unless recorded as `could-not-reproduce` with an owner. Thresholds are 100% command coverage and two independent verifiers each sampling at least 25% (`reports/round-37/claims.json:13-18`). The assigned work is the calibration receipt draft at `reports/round-37/targets.json:28-29`.

## Evidence state at latest inspection

| Gate | Required | Observed | Status |
|---|---|---|---|
| Recount rows | Every filed acceptance command for rounds 33–36 | Ca06 is filed but says `could-not-assemble`; Ca01–Ca05 inputs were missing at its check. Current file enumeration still has no Ca01–Ca05 fragments. | to-verify |
| Dispositions | Each result matched or mismatched with a named cause; any unreproduced command has an owner | No assembled r37 ledger or recount outcomes; Ca06 explicitly did not emit a partial ledger. | to-verify |
| Coverage | 100% of inventoried commands, exactly once | Ca09 filed `could-not-evaluate` because K01 and Ca06 inputs were absent at its inspection. K01 remains absent now; Ca06 is present but unassembled. | to-verify |
| Independent samples | Two verifiers, each >=25% | Ca07/Ca08 fragments are absent from the current calibration enumeration; Ca16's earlier strict-parse/count/digest check was blocked on missing inputs. | to-verify |
| Acceptance runner | `python3 reports/round-37/run-validation.py` | Not run by this seat; in-tree round runners are prohibited. | pending |

The last filed calibration measurement reports 17 round-36 recount rows and two named mismatches; the scorecard records 15 matches and two dispositioned mismatches. Round 36 remains rejected on D, with Ca reported as verified; this recount must include its filed evidence without treating the rejection as a reason to omit or repair that evidence (`reports/round-36/validation.json:31-47,144-165`; `SCORECARD.md:651-664`). The Ca06 draft likewise says the prior ledger covers rounds 33–35 only and is historical, not a round-37 rerun (`reports/round-37/calib/Ca06-ledger-draft.md:5-7`).

The Ca claim is therefore **not evaluated by this draft**. Ca09's coverage receipt and Ca16's consistency receipt are blocked observations, not passes; Ca15 also says its post-review fold is blocked on inputs (`reports/round-37/calib/Ca09-coverage.md:3-11`; `Ca15-final.md:5-13`; `Ca16-final-verify.md:3-10`). Do not infer completion from the earlier round-36 ledger or from the existence of round-37 claims/targets. Preserve source-round filed values separately from new observed results, and retain every mismatch/could-not-reproduce disposition without smoothing.

## Owed

- `reports/round-37/scout/K01-command-inventory.md` — absent at latest enumeration; command census and filed results needed.
- `reports/round-37/calib/Ca01-r33.md`, `Ca02-r34.md`, `Ca03-r35.md`, `Ca04-r36.md`, `Ca05-cross-cutting.md` — absent at latest enumeration; Ca06 needs these to assemble recount results.
- `reports/round-37/calib/Ca06-ledger-draft.md` — filed as `could-not-assemble`; rebuild after Ca01–Ca05 land.
- `reports/round-37/calib/Ca07-verify.md`, `Ca08-verify.md` — independent samples and disagreements.
- `reports/round-37/calib/Ca09-coverage.md` — rerun exact-once inventory-to-ledger coverage after K01 and Ca06 are ready.
- `reports/round-37/calib/Ca13-audit.md` — named-cause audit for mismatches.
- `reports/round-37/review/R01-ca-review.md`, `R02-ca-review.md` — required for post-review fold; none were present at latest review enumeration.
- Integrator: rerun Ca16 consistency checks and Ca15's post-review fold after inputs land; run round-37 validation only in an isolated archive copy, never in-tree.

## Citations

- `reports/round-37/claims.json:13-18` — Ca claim, required after-state, counting command, and thresholds.
- `reports/round-37/targets.json:4-8,19-29,33-34,62-63` — shared runner constraint and Ca recount, verification, receipt, and review assignments.
- `reports/round-36/validation.json:31-47,144-165` — filed Ca result, row and named-mismatch counts, and rejected round status.
- `reports/round-36/calib/recount-ledger.json:1-16,51-58` — prior ledger census and disposition conventions.
- `SCORECARD.md:651-664` — r36 calibration summary and rejection on D.
- `reports/round-37/calib/Ca06-ledger-draft.md:5-22` — current assembly status and missing Ca01–Ca05 inputs.
- `reports/round-37/calib/Ca09-coverage.md:3-11` — coverage verifier's could-not-evaluate result at its inspection.
- `reports/round-37/calib/Ca15-final.md:5-20` — blocked post-review fold and owed inputs.
- `reports/round-37/calib/Ca16-final-verify.md:3-17` — blocked strict parse/count/digest verification at its inspection.
- Command-output observation: current `Glob(path="reports/round-37", pattern="calib/**")` returned `Ca06-ledger-draft.md`, this receipt, `Ca15-final.md`, `Ca16-final-verify.md`, and `Ca09-coverage.md`; `Glob(..., pattern="scout/**")` and `Glob(..., pattern="review/**")` returned no matches.
