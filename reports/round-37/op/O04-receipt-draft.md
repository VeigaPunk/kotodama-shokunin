- Seat: O04 | executor | claim O | date 2026-10-19 | baseline 57c8409

# O04 — operability receipt draft (provisional)

## Result

**Could not evaluate / not certified.** Claim O requires one defect queue covering 100% of the census, non-author evidence for every `fixed` item, owner+reason+next-touch for every carried item, and round-38+ routing (`reports/round-37/claims.json:19-24`). The required census, queue draft, fixed-item check, and carry-routing check were absent in the current existence check below. O05 separately reports census-to-queue equality as `could not evaluate` and does not infer an item count or zero-gap result (`reports/round-37/op/O05-verify.md:3-12`). O06 reports disposition-class sanity as `could-not-evaluate`; it does not validate or reject any `fixed` row (`reports/round-37/op/O06-verify.md:3-7`). Therefore this draft asserts **no complete census coverage, no queue-wide disposition pass, and no `fixed` row**.

The independent skim O05 could make is explicitly non-exhaustive: it names r33 F-C13-1/F-C13-4/F-C15-1; r34 R34-N1 and the CO4 seat-count deviation; r35 F1-F13, route/allocation deviations, and a timekeeping spare; and r36's rejected D premise, F1-F5, conformance incident, and README prediction-vs-delivery nuance. O05 says these categories can overlap and are not asserted as distinct queue rows (`reports/round-37/op/O05-verify.md:7`). They are reconciliation leads, not a census or row count.

## Evidence to reconcile; dispositions still pending

- **R34-N1 replay:** the r35 receipt records replay exit 1, named failure, member named, no traceback, and 44 v3 controls (`reports/round-35/validation.json:69-92`). This is prior-round evidence only; because O02's required non-author re-run is absent, do not count R34-N1 as `fixed` in this receipt (`reports/round-37/targets.json:36-41`).
- **Round-36 D leg and residue:** r36 was rejected on D because its “register-form domain empty” before-state was stale; 8 forms and a five-row law were already present, and “nothing was landed under this failed claim” (`reports/round-36/validation.json:49-78,146-165`). The named residue is F-6 coverage counters, declared-but-unused `head2`, unimplemented RL-8 era leg, standing RL-3 ceiling, and the 13-versus-12 freeze/read-set asymmetry (`reports/round-36/scout/K01-register-scout.md:103-142,145-176`). Keep these as pending queue-class/routing items; do not present the rejected D claim as a fix.
- **Timekeeping spare and README delta:** the r36 scout found the r35 spare's sweep stale (`curfew` now appears once; other measured counts changed) and recorded the couples-count disagreement as unprovable-as-stated (24/25/31) (`reports/round-36/scout/K02-timekeeping-scout.md:28-86,335-365`). C02's rev-2.1 candidate repaired README order/contiguity in a scratch measurement, but that seat states it wrote no corpus/tool bytes and leaves the timekeeping entry to the integrator (`reports/round-36/cov/C02-audit-delta.md:382-417,419-442`). The r36 receipt separately records C passed with 25 culture-material files and 212 total (`reports/round-36/validation.json:15-29`); without O01/O02, these sources do not establish a queue row's present `fixed` disposition.
- **Absolute-root runner hazard:** O12 files a candidate `carried` row for the r34/r35 runners' hard-coded live-repository root, with reason, proposed owners, and a round-38+ next touch (`reports/round-37/op/O12-gap-fill.md:5-12`). O12 also asks the integrator to reconcile/deduplicate it against O01 and says no r37 queue existed at its write time (`reports/round-37/op/O12-gap-fill.md:14-17`). Treat this as a route candidate, not O03-verified or confirmed as a distinct queue row.

## Owed

- `reports/round-37/scout/K02-defect-census.md`, `reports/round-37/op/O01-queue-draft.md`, `reports/round-37/op/O02-fix-verify.md`, and `reports/round-37/op/O03-carry-verify.md` — absent in the current existence check. Reconcile census and rows, then include only O02-supported fixed items and O03-verified carried routes.
- `reports/round-37/op/O09-routing.md` and `reports/round-37/op/defect-queue.json` — absent in the current existence check; required routing and queue artifact remain unverified (`reports/round-37/targets.json:36-45`).
- After these inputs land, rerun O05 set equality and O06 disposition-class sanity, reconcile their outcomes into this receipt, and only then assess the 100% / zero-unowned thresholds (`reports/round-37/claims.json:20-24`; `reports/round-37/targets.json:36-45`).

## Citations

- Current dependency check, run from repository root:
  `for p in reports/round-37/scout/K02-defect-census.md reports/round-37/op/O01-queue-draft.md reports/round-37/op/O02-fix-verify.md reports/round-37/op/O03-carry-verify.md reports/round-37/op/O09-routing.md reports/round-37/op/defect-queue.json; do if test -f "$p"; then printf 'PRESENT %s\n' "$p"; else printf 'MISSING %s\n' "$p"; fi; done`
  → all six paths returned `MISSING`.
- `reports/round-37/claims.json:19-24` — claim O outcome and thresholds.
- `reports/round-37/targets.json:36-45` — O01–O04, O05–O06, and O09 responsibilities and output paths.
- `reports/round-37/op/O05-verify.md:3-12,16-22`; `reports/round-37/op/O06-verify.md:3-11` — independent verifier results and missing dependencies.
- No `reports/round-*/run-validation.py` was executed for this receipt.
