- Seat: R03 | reviewer | claim O | date 2026-10-19 | baseline `57c8409ba16d9f9e692297198d95e8f2ce5a1937`

# R03 — adversarial review of the O defect queue

## Result

**Could not evaluate the queue or its dispositions.** The source census, queue draft, and queue JSON are absent, so there are no row IDs/classes to compare against this independent source skim. This is not a queue pass, a confirmed omission, or an item-count estimate. Claim O requires census-to-ledger equality, fresh non-author evidence for every `fixed-with-evidence` row, and owner/reason/next-touch plus round-38+ routing for every carried row (`reports/round-37/claims.json:19-24`; `reports/round-37/targets.json:12,36-47,64-65`).

At `HEAD 57c8409ba16d9f9e692297198d95e8f2ce5a1937`, the following repository-root path check returned:

```text
MISSING reports/round-37/scout/K02-defect-census.md
MISSING reports/round-37/op/O01-queue-draft.md
MISSING reports/round-37/defect-queue.json
MISSING reports/round-37/op/defect-queue.json
MISSING reports/round-37/op/O02-fix-verify.md
PRESENT reports/round-37/op/O02-controls-verify.md
PRESENT reports/round-37/op/O03-carry-verify.md
PRESENT reports/round-37/op/O09-routing.md
MISSING reports/round-37/review/R03-o-review.md
```

O02 reports zero fix-control commands and `could-not-evaluate`, not a pass (`reports/round-37/op/O02-controls-verify.md:5-9,23-29`). O03 is present but explicitly partial / `could-not-evaluate` without the queue and census (`reports/round-37/op/O03-carry-verify.md:3,15-19`). O09 labels its routes provisional and says census/queue/carry inputs are required for reconciliation (`reports/round-37/op/O09-routing.md:3-5,18-23`). Thus 100% coverage and zero unowned rows remain unmeasured.

## Independent omission and wrong-class checks

These are reconciliation leads from primary records and filed reviews, not a substitute complete census. Since no queue exists here, I do not claim any candidate is absent from it.

1. **Separate the receipt breach, adoption debt, r26 correction, and clone-isolation defect.** Round 33 records the r5/r6/r7 receipt rewrite-and-restore and leaves writer attribution `to-verify`; restoration is not prevention (`LOG.md:3548-3567`). The r34 census corrects r26 to guarded and reports eight additional unguarded writers (RGA-1 / RGA-2), with eleven unguarded runners total (`reports/round-34/op/adoption-inventory.json:43-84,94-99`; `reports/round-34/op/O05-routing.md:99-117,239-257`). The current census tool still declares r26 as an unguarded hazard and emits the RGA correction rows (`tools/harness/receipt_guard_adoption.py:71-78,716-754`): do not classify r26 as a live unguarded runner; reconcile the correction/reporting behavior explicitly. Separately, r34/r35 hard-code the live root and `chdir` there, defeating plain clone/archive isolation on publish; O08 and O12 describe the same candidate, not two rows, and it is distinct from the original unguarded cohort (`reports/round-37/op/O08-gap-fill.md:5-19`; `O12-gap-fill.md:5-17`; `reports/round-36/cross/X02-conformance.md:187-234`). Do not mark either the historic breach/prevention debt or this isolation defect fixed merely because receipts were restored.

2. **Keep the r34 adoption-count contradiction separate from later population growth.** The filed inventory says 28 runners / 17 guarded / 11 unguarded (`reports/round-34/op/adoption-inventory.json:1-6`), while the r34 validation and SCORECARD report 29 / 18 / 11 (`reports/round-34/validation.json:53-60`; `SCORECARD.md:616`). R36's RC-2 explains 29-to-30 later growth after r35, but does not resolve the within-r34 inventory conflict (`reports/round-36/calib/recount-ledger.json:224-230`; `reports/round-36/cross/X01-trades.md:150-170`). Require an explicit disposition or alias for that mismatch; do not use the later runner addition to make the r34 inventory agree.

3. **Do not collapse R34-N1 into every renderer/read-set issue.** R34-N1's superseded-row `KeyError` was hardened in r35 and recorded closed (`SCORECARD.md:641`; `LOG.md:3662-3667`), but this-round `fixed-with-evidence` still requires O02's non-author check, which has not run. The r35 review separately left F-R05-6 open: a 57-member baseline against a 58-member live roster returned exit 0 while claiming 58 matches (`reports/round-35/review/R05-o-review.md:169-174`; `reports/round-35/scribe/S02-o-receipt.md:104-121,303-312`). R37 O07/S02 also preserve it as a separate unresolved candidate (`reports/round-37/op/O07-scribe.md:17-21`; `reports/round-37/scribe/S02-o-receipt.md:19`). A green R34-N1 replay does not close this reverse-direction gap. Also reconcile R35 O05 F1-F5 / R34-N1 subfindings or their explicit closure records; a single R34-N1 row must not silently absorb them (`reports/round-35/op/O05-verify.md:326-360`; R04 review `reports/round-37/review/R04-o-review.md:17-18`).

4. **Include the round-36 runner-digest candidate, without claiming a queue omission.** R36's receipt has `runner_sha256: null` although the runner digest is present in `input_sha256`; `rec(p)` populates `inputs` but returns no value to the receipt assignment (`reports/round-36/validation.json:149-168`; `reports/round-36/run-validation.py:63-67,210`). O10 identifies the candidate and proposes a carried correction rather than rewriting filed bytes (`reports/round-37/op/O10-gap-fill.md:5-15,19-24`). Require a census row or an explicit not-a-defect adjudication; any `fixed` class still needs O02 evidence.

5. **Reconcile all timekeeping and README findings, including cross-source aliases and unknown counts.** R36 C01 names six timekeeping findings: F1 stager mis-target, F2 unnamed reading, F3 28-vs-26 term count, F4 stale counts, F5 missing target path, and F6 pointer-leg undercount (`reports/round-36/cov/C01-audit.md:256-263`). F1/F5 may be one root cause but retain both source IDs if consolidated. The README audit separately records the internal blank line, row order, and sweep blind spot (`reports/round-36/cov/C02-audit-delta.md:153-175`). C03 adds a false statement that rows were in filename order (F3), and repeats the stale-count / term-count concerns (F4/F5); record aliases rather than duplicate rows, and verify the later rev-2.1 landing before assigning a class (`reports/round-36/cov/C03-verify.md:236-281,347-385`; `SCORECARD.md:660`). Preserve the three-way couples-count disagreement (24 / 25 / 31) as `unprovable-as-stated`, not an averaged or invented count (`reports/round-36/scout/K02-timekeeping-scout.md:337-365`). R04 correctly calls out C01 F1-F6; a queue sourced only from SCORECARD shorthand risks dropping F6 (`reports/round-37/review/R04-o-review.md:21`).

6. **Preserve the rejected r36 D boundary and keep recount findings linked, not double-owned.** The D claim failed on its stale before-state; nothing landed under that claim, and the round remains rejected (`reports/round-36/validation.json:49-78,145-168`; `SCORECARD.md:659,664-666`). Route the genuine residue under a truthful future claim; do not relabel the rejected D leg as fixed. Keep RC-1 (receipt drift / conformance incident, cause and writer `to-verify`), RC-2 (later stale wording), RC-3 (`no-action`, not a defect), and RC-4 (the self-invalidating A3 literal-2655 gate) distinct as X00 directs; link recount observations to a single queue defect rather than duplicating them (`reports/round-36/calib/recount-ledger.json:211-246`; `reports/round-37/cross/X00-connector.md:18-24,28-32`). RC-2's later growth is not the r34 28-vs-29 inconsistency above.

7. **Reconcile named round-33 findings without flattening their status.** The scorecard names F-C13-1, F-C13-4, and F-C15-1 (`SCORECARD.md:593-600`). F-C13-4 was recorded as a membership ruling, while F-C15-1's reconstructed “12” remains `to-verify` in the r34 review; distinguish decided/out-of-set readings from open provenance rather than treating both as identical open defects or silently dropping either (`reports/round-33/calib/C13-consistency.md:178-184,242-244`; `reports/round-34/cross/X04-honesty.md:42-46`). The r33 F-X16-3 disposition also contains separate D-1..D-4 treatments: D-1 was a fix draft pending application/control, D-3 is a carried lesson-key correction, and D-4 is an adjacent routed defect, not absorbed into D-1 (`reports/round-33/op/O05-falsifier-disposition.md:217-240`). Apply the current queue contract and fresh O02 evidence; historical labels alone do not satisfy it.

8. **Keep scope and routing honest.** O09's round-38 table is explicitly provisional, has no census-to-queue reconciliation, and includes a r37 A01 freeze-read-set finding plus a newly observed README title/placeholder issue (`reports/round-37/op/O09-routing.md:5,9-16`). Those may be routed separately, but they are not automatically members of the stated rounds-33–36 census; do not use them to pad or satisfy equality. Conversely, O09's partial route table is not proof that every eventual carried row has a route. R35 route/allocation deviations are named in the SCORECARD and require explicit census classification, but a recorded provider 402 by itself must not be invented into a product defect (`SCORECARD.md:631-649`).

## Owed

- K02: file `reports/round-37/scout/K02-defect-census.md` with origin pointers and current states across the required source classes.
- O01: file the queue draft and JSON, preserve source aliases, link recount records, and reconcile the candidates above; do not assert set equality until K02 and O01 exist.
- O02: the target path `reports/round-37/op/O02-fix-verify.md` is absent; the existing `O02-controls-verify.md` says no controls ran. Verify each claimed fixed item as a non-author before relying on that class.
- O03/O09: after O01 lands, verify every carried row's owner/reason/next-touch and complete round-38+ routing; current O03 is partial and O09 provisional.
- Integrator: rerun O05/O06 and fold this review into a new final receipt only after these inputs land. No round validation runner was executed for this review.

## Citations

- `reports/round-37/claims.json:19-24`; `reports/round-37/targets.json:12,36-47,64-65` — acceptance contract, census/queue/verifier/reviewer assignments.
- Read-only path check from repository root (with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): exact HEAD and PRESENT/MISSING output recorded above.
- `reports/round-37/op/O02-controls-verify.md:5-9,23-29`; `reports/round-37/op/O03-carry-verify.md:3,15-19`; `reports/round-37/op/O09-routing.md:3-5,18-23` — current limitations.
- `reports/round-37/review/R04-o-review.md:11-23` — complementary high-risk checks; no queue verdict due missing inputs.
- All other source pointers are embedded beside the relevant candidate above.
