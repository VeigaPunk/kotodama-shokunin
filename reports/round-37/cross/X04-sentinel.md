- Seat: X04 | critic | cross | date 2026-10-19 | baseline 57c8409

# Sentinel: preserve round-36's D rejection

**Verdict:** Round 36 remains rejected on claim D. Its recorded D1 evidence must not be upgraded, rewritten, or backfilled as an r36 pass using round-37 checks. Round 37 declares only calibration, operability, and adjacency claims; it declares no depth/D claim (`reports/round-37/claims.json:9-30`). Any new D-adjacent observation in r37 is a new observation, not retroactive evidence that changes r36's verdict.

## Evidence boundary

- R36 claim D's declared before-state is the empty register-form domain (`reports/round-36/claims.json:16-21`). The filed validation explicitly records the premise as stale: eight register forms and a five-row law already existed, and the argot/law legs were green (`reports/round-36/validation.json:49-78`). That is evidence against the declared before-state, not evidence that r36 newly delivered its after-state.
- The D1 leg is `failed`, claim D `passed: false`; its failure says the true residue was routed to a future round under a corrected claim, and nothing was landed under the failed claim (`reports/round-36/validation.json:52-78`). The round-level receipt records `acceptance_checks_passed: false`, the D failure, and `round_status: REJECTED on D` (`reports/round-36/validation.json:144-168`). Keep these filed outcomes intact.
- The receipt names the residue as F-6 counters, the `head2` domain, RL-8 era leg, and the 13-vs-12 component read-set asymmetry, routed to a future round under a corrected claim (`reports/round-36/validation.json:53-59`). Round-37 claim A's freeze-drift audit may report relevant evidence about the read-set asymmetry, but that cannot close or reclassify r36 D1.
- The r36 receipt itself says rejection is an honest outcome and the D premise was falsified (`reports/round-36/validation.json:157-165`). Regimen rules admit a round only when every claim verifies and require rejection rather than forcing a pass (`REGIMEN.md:37-43`).
- R37's non-goals prohibit filed-byte rewrites and in-tree runner execution (`reports/round-37/claims.json:32-34`); shared rules additionally forbid editing rounds 1–36 and executing any in-tree round runner (`reports/round-37/targets.json:3-8`). I did not run a runner or edit prior-round bytes.

**Sentinel rule for integration:** keep r36 D marked failed/rejected. A recheck, recount, freeze comparison, or other r37 observation may only be described as r37 evidence with its own scope and timestamp. Do not substitute it for r36's failed D1 measurement, alter r36's receipt, or claim that it repairs the stale before-state or completes the unlanded D claim. Any future attempt to work on the residue needs a separately declared, corrected claim and its own verdict.

## Owed

- Final cross-artifact check by the round-37 integrator before close: the current `reports/round-37/` snapshot contains only `claims.json`, `targets.json`, and `telemetry/` (`ls reports/round-37`); no r37 seat fragments are present yet to inspect for accidental regrading of r36 D. Owner: round-37 integrator. The r36 receipt remains rejected regardless of that later check.

## Citations

- `reports/round-36/claims.json:16-21` — D declaration and stale-before target.
- `reports/round-36/validation.json:49-78,144-168` — D1 failure, measured legs, aggregate rejection.
- `reports/round-37/claims.json:9-30,32-34` — r37 claims and non-goals; no D claim.
- `reports/round-37/targets.json:3-8` — shared boundaries; `:74` — X04 sentinel assignment.
- `REGIMEN.md:37-43` — no forced pass; reject if a claim fails.
- Command output: `ls reports/round-37` → `calib claims.json targets.json telemetry` (only setup artifacts present at this seat's inspection).
