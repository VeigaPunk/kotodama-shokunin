# Round-26 conformance defect sweep — R29-O03..O04

- **Audit date:** 2026-10-18.
- **Scope:** round-26 v3 baseline re-point, concurrent D4 writes, and the r4-checker supersession boundary.
- **Mode:** read-only review of `claims.json`, final runner source/receipt, the supersession note, and `reports/round-26/audit/o39-o40-remainder-fixes-adversarial.md`. No round validator was run for this sweep; execution figures below are the timestamped measurements already preserved in those artifacts.
- **Round state:** `reports/round-26/validation.json` records `acceptance_checks_passed: true`. Findings below distinguish historical snapshot drift from the final recorded state.

## Findings

### O03 — The v3 remainder row became stale during the D4 landing (historical, snapshot-dependent)

The archived command `python3 tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-26/remainders/v3-baseline-r26/expected.json` was green at **2026-10-18 18:16Z** (exit 0), then the same command was red at **18:19:16Z** with `E2E-DIGEST: 6 read-set file(s) changed` (`reports/round-26/audit/o39-o40-remainder-fixes-adversarial.md`, §2.3). The audit's **2026-10-18** `git status --porcelain` and `ls --time-style=full-iso` measurements tie the change to the D4 write at **18:18:32Z**. The measured cause was a D4 read-set change after the O seat froze its baseline, not an unmeasured or malformed row.

This is a confirmed sequencing / snapshot-stability defect at those stamps: the newly re-pointed row could be invalidated by concurrent work on its pinned inputs. It is **not** evidence that the final round-26 default remains red; the later saved `validation.json` is green. Keep the old red as historical and snapshot-dependent, not as today's result.

### O04 — The filed O contract still says “r4 checker green” while the final runner records that checker as superseded, not graded

`reports/round-26/claims.json:19-23` literally includes “the r4 checker green” in `after_required`. The final `reports/round-26/run-validation.py:1279-1285` instead makes `pin-repoint-checker` the required checker and puts `r4-checker` in `recorded_not_graded`; when reached, it records `superseded-recorded-not-graded` rather than a pass/fail verdict. This matches `reports/round-26/remainders/r4-checker-supersession.md:14-16`, which says the r4 checker is superseded, not repaired, because the r5 baseline moved.

The replacement evidence is real: `python3 reports/round-26/remainders/pin-repoint-check.py --check` is recorded on **2026-10-18** as exit 0, **17/17** controls (`r4-checker-supersession.md:9-12`). The confirmed defect is therefore a **claim/acceptance wording mismatch**, not proof that the successor checker is missing or that the old checker should be revived. Whether the filed clause should be read as referring to the successor or treated as an unmet literal criterion remains `to-verify` for the claim owner.

## Preservation boundary

Do not report the earlier r4 checker as a currently required but silently skipped leg: the final runner explicitly records its supersession. The historical v3 red and the runner/claim wording distinction are separate findings. No round-8–28 file was edited by this sweep.

FILES: reports/round-29/defects/sweep-r26.md | SUMMARY: a concurrent D4 write invalidated a v3 pin in-flight, while the r4-checker clause remains textually out of sync with its documented supersession.
