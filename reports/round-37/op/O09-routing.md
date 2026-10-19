- Seat: O09 | verifier | O | date 2026-10-19 | baseline 57c8409

# Round-38 routing table

This is a provisional route for the carry items supported by the currently filed evidence, not a completeness claim. The designated census, queue, and carry-verification inputs are still missing, so these rows must be reconciled and deduplicated against them before integration (`reports/round-37/op/O11-final.md:7,13-16,25-32`). Round 38 is the next scheduled build round; round 45 is the scheduled deep/hard build (`REGIMEN.md:15-16,22`).

| Item | Status at this cut | Natural next touch | Owner / required next action |
|---|---|---|---|
| r34/r35 runners hard-code the live repository root and `chdir` there, defeating plain archive/clone isolation on publish | Carried candidate; distinct from receipt restoration and from R34-N1. Mechanism is independently evidenced; per-write actor remains `to-verify`. | **Round 38, operability/build**, before any publish-mode recount/replay of those filed runners. | Round-37 integrator to assign a round-38 runner maintainer. Use a copy-relative successor runner or explicit containment for the hard-coded root; verify the successor's publish path writes only in its isolated copy. Preserve r34/r35 filed bytes; `--check` alone is not a fix (`reports/round-37/op/O08-gap-fill.md:7-13,17-19`; `reports/round-37/op/O12-gap-fill.md:7-12,16-17`). |
| r7 freeze read-set roster omits `13-register-law.yml` although the packet manifest names 13 D4 components | Round-37 A01 adjudicated this as a roster/completeness defect, not a documented skip or a demonstrated integrity bypass (`reports/round-37/adj/A01-freeze-adjudication.md:5,24-31`). | **Round 38, baseline/renderer build**, if the integrator elects to correct the direct roster; use a successor baseline, never re-freeze or edit the filed r7 pair. | Integrator / renderer owner: either add direct membership in a new baseline revision or explicitly document the transitive-read-set contract; retain the current component-digest control (`A01-freeze-adjudication.md:26-35`). |
| r36 D residue: F-6 coverage counters, declared-but-unused `head2`, and RL-8 era leg | The declared D claim was rejected on its stale premise; nothing was landed under that claim, and these items remain routed (`SCORECARD.md:659,664-666`; `LOG.md:3682-3689`). | **Round 38** for corrected claim scoping; **round 45** for implementation if the re-scoped work remains a deep/hard build. | Integrator to re-declare a truthful claim and assign the round-45 executor. Do not describe the rejected D leg or its old after-state as a fix (`reports/round-36/scout/K01-register-scout.md:103-139`; `REGIMEN.md:22,27-43`). |
| Live `corpus/README.md` has duplicate title lines and two literal `__E3_PLACEHOLDER__` lines | Newly observed, unnumbered integration-defect candidate; not yet present in the missing K02 census/O01 queue. Current bytes show the duplicate at `:1,3` and placeholders at `:214-215`; the r36 delta draft specifies actual sorted rows, not placeholders (`reports/round-36/cov/C02-audit-delta.md:223-258`). | **Round 38, corpus-index integration**, subject to adding it to the census/queue. | Integrator to assign an index editor to replace the placeholders with the intended content or remove them as appropriate, remove the redundant heading, then re-check row count/order/contiguity and the README sweep. This seat does not edit the corpus. |

**Do not re-route as open:** R34-N1's superseded-row `KeyError` was closed in r35 by the named `E2E-READSET` refusal with no traceback; it is not the r34/r35 hard-coded-root isolation defect (`SCORECARD.md:641`; `reports/round-37/op/O08-gap-fill.md:9`).

The r36 timekeeping-spare/couples findings remain for the assigned round-37 adjacency scan to re-verify; no additional round-38 route is asserted before that result (`reports/round-37/targets.json:49-50`; `reports/round-36/scout/K02-timekeeping-scout.md:132-141,381-403`).

## Owed

- `reports/round-37/scout/K02-defect-census.md` — absent at this cut; required to establish the complete origin set.
- `reports/round-37/op/O01-queue-draft.md` — absent at this cut; reconcile these provisional routes, the README candidate, and any other census items without assuming rows are distinct.
- `reports/round-37/op/O03-carry-verify.md` — absent at this cut; verify every carried row's owner, reason, and next-touch against its origin before claiming route completeness.
- Round-37 A02's scan result for the timekeeping entry — no route beyond the current-round audit is asserted until it lands.

## Citations

- `reports/round-37/targets.json:44,49-50`; `reports/round-37/claims.json:19-24` — this seat's assignment, current adjacency scan, and O-claim threshold.
- `REGIMEN.md:15-16,22,27-43` — round-38 build, round-45 deep/hard build, and no-forced-pass rule.
- `reports/round-37/op/O08-gap-fill.md:7-13,17-27`; `reports/round-37/op/O12-gap-fill.md:7-12,16-25` — isolated-runner hazard and proposed carried disposition; no runner was executed by this seat.
- `reports/round-37/adj/A01-freeze-adjudication.md:5,24-35` — re-render match, roster defect adjudication, and successor-revision route.
- `reports/round-36/scout/K01-register-scout.md:103-139`; `SCORECARD.md:659,664-666`; `LOG.md:3682-3689` — identified D residue and rejection boundary.
- `corpus/README.md:1-5,214-215`; `reports/round-36/cov/C02-audit-delta.md:223-258` — live README candidate and intended row repair material.
- `reports/round-37/op/O11-final.md:7,13-16,25-32,42` — queue/census/routing completeness is still could-not-evaluate and required inputs remain owed.
- `SCORECARD.md:641` — R34-N1 closed at r35.
- `reports/round-36/scout/K02-timekeeping-scout.md:132-141,381-403` — unresolved timekeeping/couples routing belongs first to the current-round audit.
