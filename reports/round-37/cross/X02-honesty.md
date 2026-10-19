- Seat: X02 | critic | cross | date 2026-10-19 | baseline 57c8409

## Honesty audit

This is a bounded audit of the filed validation receipts for rounds 33–36 and the round-37 fragments available in the live workspace at this read. The round-37 artifact set is still in flight; no final `validation.json` was present in the latest round-37 enumeration. No round runner was executed.

### Filed uncertainty and rejected status

- The prior receipts explicitly mark their private-prompt / lead leg `could-not-evaluate`: round 33 CO6 (validation.json:1095-1104,1274), round 34 CO6 (122-129,184), round 35 CO-godspeed (100-108,213), and round 36 CO-godspeed (98-105). These are not evidence of a green result. Rounds 33–35 separately record acceptance, and round 36 remains rejected on D; keep those scopes distinct (`reports/round-{33,34,35,36}/validation.json:2,49-78,136-167`; round-36 rejection also `SCORECARD.md:651-666`).
- Round 34 openly records two missing target outputs, X00 and D17, despite `acceptance_checks_passed: true` (`reports/round-34/validation.json:190-200`). The SCORECARD says those seats did not land and that the gap was recorded, not repaired (`SCORECARD.md:620-624`). Preserve this as a disclosed dependency gap; do not represent it as delivered seat evidence.
- The round-33 receipt preserves F-C15-1 as `to-verify`: “12” is reconstructed rather than quoted, with the reconstruction rule cited for checking (`reports/round-33/validation.json:651-655`; `SCORECARD.md:593-600`).
- Round 35's C leg reports `to_verify_count: 102` while its status is green (`reports/round-35/validation.json:29-64`). The receipt field does not enumerate or disposition those 102 marks here. Do not turn the count into either “zero unresolved” or “102 defects”; its meaning/disposition is to-verify for this audit.
- Round 36's rejection is not ambiguous: the receipt records D failed, `acceptance_checks_passed: false`, and `round_status: REJECTED on D` (`reports/round-36/validation.json:49-78,145-168`). Its `runner_sha256` field is nevertheless null at line 167 while `input_sha256` gives the runner digest at line 152. A read-only `sha256sum reports/round-36/run-validation.py` returned the same `dd52c5806f5cfd88bb10816b98c4559dd7bf72873d13bdf2836427010a85a4d3`. This is a recoverable receipt-field inconsistency, not evidence that the runner was unavailable; do not alter the filed receipt.
- The r36 recount ledger still has specific unresolved findings, including RC-1 cause `to-verify` (`reports/round-36/calib/recount-ledger.json:211-222`). The r37 connector correctly keeps RC-1 attribution, RC-3 classification, and the README-nuance owner unresolved rather than inferring them (`reports/round-37/cross/X00-connector.md:12,18,20,23,36-38`).

### Round-37 live fragment status

- Ca remains unverified. Ca06 is explicitly `could-not-assemble` because Ca01–Ca05 were absent at its check (`reports/round-37/calib/Ca06-ledger-draft.md:3-15`). Ca09 and Ca16 explicitly make no pass claim and mark the missing-input checks `could-not-evaluate` / `to-verify` (`reports/round-37/calib/Ca09-coverage.md:3-11`; `Ca16-final-verify.md:3-17`). Ca10, Ca13, Ca15, Ca11 and S01 likewise treat the receipt/fold as partial or blocked, not acceptance (`reports/round-37/calib/Ca10-receipt.md:5,13-23,27-34`; `Ca13-audit.md:5-7,31`; `Ca15-final.md:5-13`; `Ca11-scribe.md:7-14`; `reports/round-37/scribe/S01-ca-receipt.md:7,15-20`).
- There is a stale-snapshot warning: current round-37 inventory contains `scout/K01-command-inventory.md`, but Ca10 line 17 says “K01 remains absent now.” Ca10 gives no observation timestamp with which to resolve whether K01 landed after its scan. Its statement cannot be treated as current; refresh Ca10 and rerun Ca09/Ca16 against the current K01 and Ca06 state. K01 itself clearly limits its scope to filed-result inventory, says it did not infer shell exit codes, and does not claim replay (`reports/round-37/scout/K01-command-inventory.md:5,44-47`; current path is also in the latest `Glob reports/round-37/**/*` output).
- A remains unverified: A05 marks each required A01–A04 result `to-verify`, says zero unfiled bleed is not established, and does not promote the r36 scout's lead to an adjudication (`reports/round-37/adj/A05-receipt.md:10-24,28-32`).
- O remains unverified: O05/O06 and O11 explicitly report `could-not-evaluate`; O05's candidate list is expressly incomplete, and O12's isolation-hazard candidate keeps per-write actor attribution `to-verify` pending census/queue reconciliation (`reports/round-37/op/O05-verify.md:5-12`; `O06-verify.md:3-7`; `O11-final.md:7,13-19,27-32`; `O12-gap-fill.md:7-17`). Do not count missing queue inputs as zero defects or call O12 a finalized queue disposition.
- S05 identifies itself as a telemetry draft and does not claim launch, completion, failure, route, or runtime concurrency observations (`reports/round-37/scribe/S05-telemetry-draft.md:3,7,94`).

No inspected round-37 fragment asserts that Ca, O, or A has met its required after-state. The major audit risk at this cut is stale snapshot language: refresh current-state statements and keep every missing dependency, uncertain attribution, and unverified leg explicit. The round-37 workspace listing did not contain `validation.json` or `telemetry/observed-dispatch.json`; no final acceptance or observed-dispatch conclusion is made here (latest `Glob reports/round-37/**/*`; `reports/round-37/telemetry/dispatch-declared.json:14-16`).

## Owed

- Round-37 integrator: refresh stale current-state statements against the final tree, especially Ca10's K01-absence statement; then obtain Ca01–Ca05 recounts, assemble Ca06, and rerun Ca09/Ca16 plus Ca07/Ca08 independent samples and Ca13 mismatch audit before any Ca verdict.
- Round-37 integrator: complete K02/O01 census-to-queue reconciliation, O02/O03 checks and O06/O09 verification; complete A01–A04 and independent A verifications. Keep the current CNE/to-verify items unscored until supported.
- Round-37 integrator: retain r36 D rejection and its filed bytes; if correcting the null runner-hash field is warranted, document a new erratum rather than edit the receipt. Reconcile the round-35 `to_verify_count: 102` semantics from its underlying audit evidence before making any resolution claim.
- Final validation and telemetry must be created/measured only through the permitted isolated-copy procedure; do not execute any in-tree `reports/round-*/run-validation.py`.

## Citations

- `reports/round-33/validation.json:651-655,1095-1104,1274` and `SCORECARD.md:593-600` — CNE lead and F-C15-1 reconstruction caveat.
- `reports/round-34/validation.json:122-129,184,190-200`; `SCORECARD.md:620-624` — CNE and the recorded missing outputs.
- `reports/round-35/validation.json:29-64,100-108,213` — C leg count and CNE status.
- `reports/round-36/validation.json:49-78,98-105,145-168`; `reports/round-36/calib/recount-ledger.json:211-222` — rejection, CNE, digest-field discrepancy, and to-verify cause.
- Command output: `sha256sum reports/round-36/run-validation.py` → `dd52c5806f5cfd88bb10816b98c4559dd7bf72873d13bdf2836427010a85a4d3`.
- `reports/round-37/calib/Ca06-ledger-draft.md:3-22`; `Ca09-coverage.md:3-11`; `Ca10-receipt.md:13-23`; `Ca13-audit.md:5-7,31`; `Ca16-final-verify.md:3-17`; `Ca15-final.md:5-13`; `Ca11-scribe.md:7-14`; `reports/round-37/scribe/S01-ca-receipt.md:7-20` — blocked Ca evidence and explicit uncertainty labels.
- `reports/round-37/scout/K01-command-inventory.md:5,44-47` — filed-result-only scope and no inferred runner exit status.
- `reports/round-37/adj/A05-receipt.md:10-24,28-32` — adjacency `to-verify` rows and no zero-bleed claim.
- `reports/round-37/op/O05-verify.md:5-12`; `O06-verify.md:3-7`; `O11-final.md:7,13-19,27-32`; `O12-gap-fill.md:7-17` — incomplete queue evidence and attribution uncertainty.
- `reports/round-37/cross/X00-connector.md:12,18,20,23,36-38`; `cross/X04-sentinel.md:5-15` — unresolved ownership/census questions and r36 rejection boundary.
- `reports/round-37/scribe/S05-telemetry-draft.md:3,7,94`; `reports/round-37/telemetry/dispatch-declared.json:14-16` — declared-only telemetry state.
- Command/tool output: latest `Glob(path="reports/round-37", pattern="**/*")` listed current fragments and no `reports/round-37/validation.json` or `telemetry/observed-dispatch.json`.
