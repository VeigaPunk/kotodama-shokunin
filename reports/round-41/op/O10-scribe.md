- Seat: O10 | scribe | claim O | date 2026-10-19 | baseline 456674d

# O10 — landed-changes material

**Snapshot: 2026-10-19T15:43:07Z.** The requested template and checker were not present (`template=false`, `checker=false`); only 11/32 declared seat outputs existed at this census. O08, O09, and O11 had supplied gap-fill/reference material, and O12 had supplied a receipt-fold snapshot at 15:42:19Z. This is an in-flight observation, not a final round census or verdict.

**Report-ready material at this cut:** no round-41 runner template or conformance checker is available to describe as landed, and the claim's after-state remains unverified. O09's static inspection records the r40 reference indicators (relative ROOT expression, receipt-guard call, runner digest, findings/limits), but explicitly says it is not checker verification (`op/O09-r40-verify.md:3-9`). O08 identifies an unresolved interpretation risk: r40 declares ROOT but uses cwd-relative paths; it marks behavior from a non-repository cwd `to-verify` and advises against adding ROOT-use as a required point without confirming the invocation contract (`op/O08-gap-fill.md:5-11`). O11 proposes guard-dominance tests that distinguish reachable pre-write checks from mere token presence (`op/O11-gap-fill.md:5-11`). These are evidence and test recommendations, not landed implementation changes.

The declared acceptance remains the template plus checker, green selftest, complete r34–r40 census, and evidence-backed queue-v2 update; none is established by this snapshot (`claims.json:13-18`). Integrator should re-census at close and reconcile the ROOT-use question against the five declared contract points before judging the checker.

## Owed

- Landed template and checker; selftest and JSON census outputs; independent verifier and adversarial checks (`targets.json:41-73`).
- O07 receipt, O09 checker-based r40 verification, and the final O12 post-review fold (`targets.json:82-108,118-123`).
- Evidence-backed queue-v2 update and final review dispositions (`claims.json:13-18`; `targets.json:76-87,195-207,229-234`).
- Recompute the output census and all measurements on the delivered revision. The in-tree round-validation command remains prohibited by the shared rules (`targets.json:3-9`).

## Citations

- Assignment and output boundary: `reports/round-41/targets.json:3-9,104-109`; declared claim/threshold: `reports/round-41/claims.json:13-18`.
- Census command, run with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, at `2026-10-19T15:43:07Z`: read `targets.json` and tested declared `out` paths plus the two implementation paths. Output: `seat_outputs=11/32`; present `scout/K01-runner-scout.md`, `scout/K02-pin-scout.md`, `op/O08-gap-fill.md`, `op/O09-r40-verify.md`, `op/O11-gap-fill.md`, `op/O12-final.md`, `calib/Ca02-skill-delta.md`, `calib/Ca03-scorecard-delta.md`, `calib/Ca05-verify.md`, `calib/Ca07-gap-fill.md`, `calib/Ca09-scribe.md`; `template=false`; `checker=false`.
- Reference precheck and its limitation: `reports/round-41/op/O09-r40-verify.md:3-9`; r40 source: `reports/round-40/run-validation.py:5,197,204-209,227-247`.
- ROOT-use concern and limitation: `reports/round-41/op/O08-gap-fill.md:5-11`.
- Guard-dominance test recommendation: `reports/round-41/op/O11-gap-fill.md:5-11`.
- Receipt-fold snapshot is time-bound at 15:42:19Z: `reports/round-41/op/O12-final.md:3-12`.
