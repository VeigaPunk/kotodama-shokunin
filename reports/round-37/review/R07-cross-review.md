- Seat: R07 | reviewer | cross | date 2026-10-19 | baseline 57c8409

# R07 — Cross-claim review: recount and defect queue

Review scope is calibration × operability, especially the shared round-36 evidence. **Queue-to-ledger reconciliation could not be completed:** K02's census, O01's queue, and Ca04's round-36 recount were absent at this review cut; Ca06 reports it could not assemble a ledger because its recount inputs were missing. This is a dependency gap, not evidence of zero overlap or successful coverage.

## Findings

1. **Keep the two ledgers' row units distinct.** K01 enumerates claim-level runner records separately even when the command text repeats; it also inventories nested commands. In round 36 the same runner command is filed under C, Ca, D, and cross, with different results. Those are four claim records, not one command row to collapse: C and Ca passed; D failed; cross passed with a CO-godspeed subleg marked could-not-evaluate. Ca04/Ca06 should preserve all four filed results, keyed by round + claim + command. The O queue should instead use one row per underlying defect and link the related recount row(s); it must not clone a defect for each claim, artifact, or corroborating fragment. (`reports/round-37/scout/K01-command-inventory.md:5-26,42-47`; `reports/round-36/validation.json:4-47,49-79,80-136,144-165`; `reports/round-37/cross/X00-connector.md:7-12,28-32`.)

2. **The rejected D result is not repairable by this recount.** Filed r36 evidence says the D premise was stale, D failed, and nothing landed under it; the aggregate receipt is rejected on D, although C/Ca/cross passed. The O queue may carry the stale-claim/depth-residue finding to a corrected future claim, but must not mark it fixed because an r37 audit can confirm existing register forms or inspect the related freeze asymmetry. Keep the original D failure and r36 rejection intact; do not backfill r36 from r37 evidence. X04 states this boundary correctly. (`reports/round-36/validation.json:49-78,144-168`; `SCORECARD.md:651-665`; `reports/round-37/cross/X04-sentinel.md:5-15`; `reports/round-37/targets.json:74`.)

3. **RC-1 / F-C13-1 needs both the event and mechanism represented without multiplying rows.** The r36 recount-ledger's RC-1 records r35 receipt drift and leaves the writer attribution `to-verify`; the r36 LOG describes a runner execution and restoration. Later r36 evidence documents repeated r34/r35 receipt writes, an r35 receipt still divergent at X02's close, and the absolute-root mechanism that defeats plain-clone isolation. Do not close the incident as fixed on the strength of a later clean sample or the shorter LOG summary. If K02 treats both as defects, retain linked but distinct identities for the observed breach and the systemic absolute-root/chdir hazard; do not create one per transient write or observer. O08 and O12 describe the same absolute-root hazard and must merge into one canonical queue item, not two. Keep actor attribution `to-verify`; restoration is not a fix for the runner design. (`reports/round-36/calib/recount-ledger.json:211-221`; `LOG.md:3695-3701`; `reports/round-36/cross/X02-conformance.md:37-63,126-176,187-234`; `reports/round-36/calib/Ca05-receipt.md:145-174`; `reports/round-37/op/O08-gap-fill.md:5-19`; `reports/round-37/op/O12-gap-fill.md:5-17`; `reports/round-37/op/O11-final.md:13-15,21-27`.)

4. **Do not turn recount dispositions into defects by default.** RC-2's later live-count observation is separate from the r34 historical 29/18/11 reading; if K02 includes the present-tense SCORECARD wording, give it one wording/clarification row, not another row for the same historical mismatch. RC-3 is explicitly `no-action`, not a defect. RC-4 is a candidate A3 self-invalidating-gate defect: link the recount evidence to one carried queue row, not an extra row for the same gate under a second label. RC-34-3's scoped reconstruction artifact and RC-34-5's environmental growth are Ca dispositions, not product defects absent separate evidence. (`reports/round-36/calib/recount-ledger.json:117-145,211-245`; `reports/round-36/calib/Ca03-ledger-draft.md:92-105,124-143`; `reports/round-36/scout/K03-recount-scout.md:341-348`; `reports/round-37/cross/X00-connector.md:19-23`.)

5. **The connector's model is sound but needs a final delta reconciliation.** X00 correctly separates command truth from defect lifecycle, preserves the D rejection, and cautions against treating RC-3 or the recount mismatches as defects. Its matrix predates the available O08/O12 fragments and K01 inventory; update the final crosswalk to include the single absolute-root candidate and preserve the per-claim r36 command records. K02/O01 set equality remains unproven until both land. (`reports/round-37/cross/X00-connector.md:7-32,34-49`; `reports/round-37/op/O08-gap-fill.md:15-19`; `reports/round-37/op/O12-gap-fill.md:14-17`.)

## Review disposition

**Partial; overall cross-claim reconciliation could-not-evaluate.** The source-level rules above are supported, but I cannot certify actual recount-to-queue row equality or O01's dispositions without the missing census, queue, and Ca04 recount. No round runner was executed and no prior-round byte was changed.

## Owed

- `reports/round-37/scout/K02-defect-census.md` — K02 census absent; needed to decide the exact defect identities and census membership.
- `reports/round-37/op/O01-queue-draft.md` — O01 queue absent; needed to inspect owners/dispositions, detect duplicate or missing rows, and reconcile O08/O12.
- `reports/round-37/calib/Ca04-r36.md` and a completed `reports/round-37/calib/Ca06-ledger-draft.md` — required to check the r36 claim-level recount, especially D's failed result, against the queue.
- Re-run this crosswalk after those inputs land; this fragment does not establish either claim's threshold.

## Citations

- `reports/round-37/claims.json:13-24` — Ca/O requirements and thresholds.
- `reports/round-37/targets.json:11-12,17,19-24,36-47,68,74` — inventory, connector, recount, queue, review, and D-sentinel assignments.
- `reports/round-37/scout/K01-command-inventory.md:5-26,28-46` — claim-level command inventory and duplicate-command convention.
- `reports/round-37/calib/Ca06-ledger-draft.md:5-15` — assembly blocked; Ca04 input owed.
- `reports/round-37/cross/X00-connector.md:7-32,34-49` and `reports/round-37/cross/X04-sentinel.md:5-15` — prior collision model and rejection boundary reviewed here.
- `reports/round-36/validation.json:31-47,49-79,80-136,144-168` — r36 claim outcomes and aggregate rejection.
- `reports/round-36/calib/recount-ledger.json:117-145,211-252` — historical recount dispositions and RC-1..RC-4 findings.
- `SCORECARD.md:651-666`; `LOG.md:3682-3701` — r36 rejection, carried residue, conformance summary, and README nuance.
- `reports/round-36/cross/X02-conformance.md:37-63,126-176,187-234` and `reports/round-36/calib/Ca05-receipt.md:145-174` — recurrence, isolation mechanism, and attribution limits.
- `reports/round-37/op/O08-gap-fill.md:5-19`; `reports/round-37/op/O12-gap-fill.md:5-17` — duplicate descriptions of the absolute-root candidate.
- Command output (repository root, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`): existence check returned `MISSING` for `reports/round-37/scout/K02-defect-census.md`, `reports/round-37/op/O01-queue-draft.md`, and `reports/round-37/calib/Ca04-r36.md` when this review was written.
