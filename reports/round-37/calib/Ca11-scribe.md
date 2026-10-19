- Seat: Ca11 | scribe | claim Ca | date 2026-10-19 | baseline 57c8409

# Ca11 — calibration landed-changes material

## Landed changes

Report-ready snapshot at the final Ca11 scan: the round-37 calibration directory contained `Ca09-coverage.md`, `Ca10-receipt.md`, `Ca15-final.md`, and `Ca16-final-verify.md`; the scout directory had no matching files. These are blocker/evidence-status fragments, not a completed recount ledger: Ca09/Ca10/Ca15/Ca16 report that the K01 command inventory and Ca06 ledger were unavailable, so command coverage, observed dispositions, and independent verifier samples remain unverified. Do not report these artifacts as calibration acceptance or substitute round-36's historical result for this round's recount. Ca's declared deliverable is a one-row-per-filed-command recount across rounds 33–36, with named mismatch causes and two independent samples at the stated threshold (`claims.json:13-18`; `targets.json:24-27`).

Ca11 makes no source, corpus, frozen-gate, or prior-round change; this fragment is report material only. No round-validation runner was executed.

## Owed

- `reports/round-37/scout/K01-command-inventory.md`, `reports/round-37/calib/Ca01-r33.md` through `Ca08-verify.md`, and `reports/round-37/calib/Ca06-ledger-draft.md`: land the inventory, recounts, ledger, and independent samples; then Ca11's status snapshot must be refreshed by the integrator from the completed evidence. Assignments: `targets.json:11,19-27`.
- Integrator: reconcile the final landed artifact paths and evidence in the report after the missing inputs arrive; this fragment does not establish Ca acceptance.

## Citations

- `reports/round-37/claims.json:7,13-18` — declared baseline and Ca's recount deliverable, disposition requirements, and sampling threshold.
- `reports/round-37/targets.json:4-8,11,19-34,62-63` — shared constraints, K01/Ca assignments, scribe output path, and reviewers.
- `reports/round-37/calib/Ca09-coverage.md:3-11` — coverage could-not-evaluate; inventory and ledger dependencies absent at its inspection.
- `reports/round-37/calib/Ca10-receipt.md:11-23` — recount, coverage, and verifier evidence not available at its inspection; Ca not evaluated.
- `reports/round-37/calib/Ca15-final.md:5-13` — post-review fold blocked and inputs owed.
- `reports/round-37/calib/Ca16-final-verify.md:3-10` — strict parse, count comparison, and digest checks remain to-verify.
- Command output, 2026-10-19T09:56:27Z: `ls reports/round-37` showed `calib`, `claims.json`, `op`, `targets.json`, `telemetry`; scoped `git status` showed Ca09/Ca15/Ca16 and other round fragments. Final scan: `Glob reports/round-37/scout/*` returned no matches; `Glob reports/round-37/calib/*` returned Ca09, Ca10, Ca15, and Ca16 only.
- `reports/round-37/targets.json:7` — no in-tree round-validation runner execution.
