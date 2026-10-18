# R29-O16 — `--check` writes a filed gate-test receipt

- Date: 2026-10-18.
- Status: **open process/tool defect; route to R30.** No historical runner was executed in the live lane.

## Defect and control

R28 regression recorded that `reports/round-27/gate-tests/run-gate-tests.py --check` rewrote its own filed `receipt.json`; the change was detected and the original byte restored. The report's dated direct-run evidence (`reports/round-28/regression.md` §§52–110) gives the command, the transient changed receipt, and the baseline digest restored. This is an actual side effect, not an expected old-pin refusal. The R28 runner has the same shape: its current source writes `receipt.json` unconditionally at `reports/round-28/gate-tests/run-gate-tests.py:1117–1119`, after the parser exposes a `--check` option.

I did **not** rerun either `--check` command: doing so against the lane could alter a filed artifact, and the task forbids modifying rounds 8–28. The historical change-and-restore is the control; no claim is made that the defect has been fixed. The present source inspection confirms the unguarded write remains.

## Route

R30 owner: make measurement-only mode avoid the write, or require an explicit new receipt destination; add a negative control that hashes the protected receipt before and after `--check`. Run that control in an isolated clone, then compare the live filed receipt without rewriting it. Keep the round-27 and round-28 receipts immutable.

Separate but related replay-tool isolation/classification work is recorded in `fix-14.md`; do not collapse that independent root cause into this receipt-write defect.