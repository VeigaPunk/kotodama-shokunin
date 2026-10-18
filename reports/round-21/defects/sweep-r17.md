# Round-17 conformance defect sweep — R21-O01..O02

- **Audit date:** 2026-10-18.
- **Scope:** round-17 claims, acceptance receipt, target arithmetic, and the round-17 closure records in `LOG.md` and `SCORECARD.md`.
- **Mode:** read-only. I did not execute `reports/round-17/run-validation.py` or any historical validator, and did not modify round-8..20 artifacts. A lane-local `reports/round-17/kotodama.md` and `.ufo/reports/**/*.md` were not found; this audit does not establish whether a report exists outside this repository.
- **Round state:** the filed receipt says acceptance failed; `LOG.md` and `SCORECARD.md` record C/O pass and D rejected. This is consistent with the rejected-round result, not itself a defect.

## Findings

### O01 — Closure records label the declaration commit as the baseline (medium)

`reports/round-17/claims.json:5` and `reports/round-17/validation.json:3` give the baseline as `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; the round-local draft identifies it as the round-16 admit (`report-draft.md:5-7`). In contrast, `LOG.md:3225-3226` and `SCORECARD.md:152-155` label `9b49a4a` as the baseline. The recorded command `git show -s --format='%H %s' 9b49a4a` (audit date 2026-10-18) identifies that revision as **the round-17 claims declaration**, not the declared baseline. Reproduce by comparing the `baseline_revision` fields in claims/receipt with those two closure records and resolving each short revision with `git show -s` (2026-10-18).

This is a factual traceability mismatch in the closure metadata. Preserve the historical files; any correction belongs in a new authorized integration record. The local final-report search also found only a draft (`report-draft.md:12-15` says the parent owns the final report); any external filing remains unverified.

### O02 — Declared worker count and target seats do not reconcile (low / informational in receipt)

`reports/round-17/claims.json:8` declares 64 workers, while `reports/round-17/targets.json` allocates 60 seats. The round-17 scope audit enumerates the allocation as `4+12+4+4+8+3+5+2+12+4+2 = 60` and records a difference of four (`reports/round-17/scope.md:77-88`); it repeats the finding at `:157-159`. The filed measurement records `python3 reports/round-17/run-validation.py`, date `2026-10-18`, and explicitly notes that the counting contract treats the arithmetic mismatch as informational (`validation.json:1910-1915`). The command was not re-run during this sweep.

The dispatch map and declared workforce therefore disagree even though the receipt does not fail acceptance on this condition. Carry the discrepancy as an operator/declaration conformance issue; do not silently alter either filed declaration.

## Preservation and verification boundary

Read-only preservation check on 2026-10-18: `git merge-base --is-ancestor f30b6f8188937632bbedd0e7b29aeefff6f8b07b HEAD` exited 0; `git diff --name-only f30b6f8188937632bbedd0e7b29aeefff6f8b07b HEAD -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 reports/round-15 reports/round-16` returned no paths. This is a current Git-tree comparison, not evidence about any transient historical worktree state. No round validator was executed.

FILES: reports/round-21/defects/sweep-r17.md
SUMMARY: R17 remains rejected on D; the closure baseline is mislabeled and the declared worker/seat arithmetic is off by four.
