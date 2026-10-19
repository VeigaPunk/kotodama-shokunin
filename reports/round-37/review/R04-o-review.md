- Seat: R04 | reviewer | claim O | date 2026-10-19 | baseline 57c8409

# R04 — second adversarial review of the O defect queue

## Result

**Could not evaluate the queue itself.** At the final input check, the K02 census, O01 queue, O02 fixed-item verification, and O03 carry verification were all absent. I therefore make no census-completeness, queue-class, or disposition-pass claim. The independent source skim below is a targeted omission/disposition checklist, not a complete replacement census.

## High-risk review checks for integration

1. **Keep the receipt incidents separate from the runner-design hazard, and preserve attribution limits.** The r33 F-C13-1 event was a real in-tree write/restoration; the r36 conformance incident records another breach. Restoration is not prevention, and the r33 likely-writer attribution remains `to-verify` (LOG.md:3548-3567; SCORECARD.md:664-666; LOG.md:3695-3698). Separately, r34/r35 runners hard-code the live root and `chdir` there, defeating ordinary archive/clone isolation; O08 and O12 identify this as a distinct carried mechanism, not merely the original unguarded-writer class (reports/round-37/op/O08-gap-fill.md:5-13; reports/round-37/op/O12-gap-fill.md:5-12). O08 and O12 describe the same candidate; avoid duplicating it as two queue rows. Do not mark either issue fixed on the evidence of a restored receipt.

2. **Resolve the r34 adoption-count contradiction rather than folding it into later runner growth.** The filed inventory says `runner_count: 28`, `guarded-refresh: 17`, `unguarded-in-place: 11` (reports/round-34/op/adoption-inventory.json:2-6,88-110), while r34's validation and SCORECARD say 29 / 18 / 11 (reports/round-34/validation.json:53-60; SCORECARD.md:616). R36's RC-2 describes only the later 29-to-30 live-tree growth after r35 (reports/round-36/calib/recount-ledger.json:224-230); that explanation does not adjudicate the within-r34 receipt-vs-inventory mismatch. R36 X01 independently names the disagreement and calls the 29/18 reading unprovable against the cited artifact (reports/round-36/cross/X01-trades.md:150-170). Require one explicit disposition for this mismatch, separate from harmless time-bound growth.

3. **Do not omit the adoption-inventory findings.** The r34 inventory explicitly records RGA-1 (the F-C13-1 claim that r26 is unguarded is wrong; r26 is guarded) and RGA-2 (eight additional undeclared unguarded writers) (reports/round-34/op/adoption-inventory.json:43-84). Check that they appear or are explicitly reconciled to another canonical row; do not re-label r26 as unguarded.

4. **R35's R34-N1 closure does not disposition every O finding.** R35's O verification separately names F1 (exit-code reading decision), F2 (`--quiet` visibility, reported fixed), F3 (stale docstring/prose, not fixed/out of claim), F4 (v1 latent twin), and F5 (r34 mechanism string supersession) (reports/round-35/op/O05-verify.md:326-360). Check each named item is represented or explicitly adjudicated; a green R34-N1 replay alone is not evidence those other items were all fixed. O02 evidence is required for any `fixed-with-evidence` queue class (targets.json:37,41).

5. **Preserve the r36 rejection and its separate carried residue.** The stale D premise failed and round 36 is explicitly rejected; neither later evidence nor a queue disposition may turn that D leg green or rewrite its filed evidence (reports/round-36/validation.json:49-79,157-165; reports/round-37/targets.json:74). X00 identifies the A3 literal-2655 self-invalidating gate as a distinct routed defect, and warns not to conflate it with the r36 rejection or recount rows (reports/round-37/cross/X00-connector.md:21,24,28-32; reports/round-36/calib/Ca03-ledger-draft.md:136-143).

6. **Check the full r36 finding set, including beyond the scorecard shorthand.** The r36 coverage audit's numbered findings include F1–F6: stager mis-target, count/reading precision, missing drift disclosure, absent landing target, and pointer-leg undercount (reports/round-36/cov/C01-audit.md:249-263). The SCORECARD only says “named defects filed” (SCORECARD.md:660), so a queue built from scorecard summaries alone could miss these. Some findings share a cause (F1/F5) and may be represented by one canonical row with both source IDs; the independent pointer-leg F6 must not silently disappear. Keep the r36 README prediction-vs-delivery nuance separate from the benign 211→212 later-count change (LOG.md:3690-3693; reports/round-37/cross/X00-connector.md:23).

7. **Keep recount evidence cross-referenced, not double-owned.** X00 assigns observed/filed command truth to Ca and defect lifecycle to O, and specifically calls for distinct treatment of RC-1 through RC-4 (reports/round-37/cross/X00-connector.md:9-12,18-24,28-32). Check that the queue has one defect row per underlying issue, with a Ca reference where relevant; RC-3 is identified as no-action, not a defect (X00:20), while RC-4/A3 is a carried gate-design issue (X00:21).

## Owed

- `reports/round-37/scout/K02-defect-census.md` and `reports/round-37/op/O01-queue-draft.md` — absent at final check; re-run this adversarial review against the actual census and queue before claiming the O review complete.
- `reports/round-37/op/O02-fix-verify.md` and `reports/round-37/op/O03-carry-verify.md` — absent at final check; fixed/carry classifications remain unverified here.
- Owner: R04 for the review re-read; next touch after the listed evidence lands. No round runner was executed.

## Citations

- `reports/round-37/targets.json:12,36-47,65` — K02/O01 inputs, O02/O03 verification duties, and this seat's mission.
- Command output from `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1; for f in reports/round-37/scout/K02-defect-census.md reports/round-37/op/O01-queue-draft.md reports/round-37/op/O02-fix-verify.md reports/round-37/op/O03-carry-verify.md; do if test -f "$f"; then printf 'PRESENT %s\n' "$f"; else printf 'MISSING %s\n' "$f"; fi; done`:
  `MISSING reports/round-37/scout/K02-defect-census.md`; `MISSING reports/round-37/op/O01-queue-draft.md`; `MISSING reports/round-37/op/O02-fix-verify.md`; `MISSING reports/round-37/op/O03-carry-verify.md`.
- No `reports/round-*/run-validation.py` was executed.
