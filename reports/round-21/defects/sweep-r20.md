# Round-20 conformance defect sweep — R21-O07..O08

- **Audit date:** 2026-10-18.
- **Scope:** round-20 final-report integration and the documented filed-artifact preservation incident.
- **Mode:** read-only. No round or historical validator was run; no round-8..20 artifact was modified. Searches were limited to this repository; external fleet-root filing remains unverified.
- **Round state:** the primary receipt and the parent admission records say round 20 was admitted. This sweep does not repeat the acceptance measurement.

## Findings

### O07 — The local closure package lacks an authorized final report and disagrees on baseline identity (medium / external filing unverified)

`reports/round-20/report-draft.md:22-30` explicitly labels the artifact an in-flight draft and says the parent owns the final report; `reports/round-20/fragment-index-x24.md:102-108` calls it “not authorized final filing.” The path check `test -e reports/round-20/kotodama.md` was false and the in-repository `.ufo/reports/**/*.md` search returned no matches (audit date 2026-10-18). The parent does record admission (`LOG.md:3273-3284`; `SHONEN.md:211-226`), but its baseline is listed as `122086b` (`LOG.md:3275-3276`; `SHONEN.md:213-215`), while `reports/round-20/claims.json:5` and `validation.json:3` use `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`. `git show -s --format='%H %s' 122086b caf1beac` (audit date 2026-10-18) identifies `122086b` as the **round-20 declaration** and `caf1beac` as the **round-19 admission**.

Thus the in-repository closure lacks a final report and the surviving summary misbinds the baseline. This does not overturn the recorded admitted verdict or green receipt. Whether an external final report exists remains unverified. Preserve filed records and resolve both points only in a new authorized integration artifact.

### O08 — A live historical-validator run transiently rewrote a protected round-9 receipt (high)

`reports/round-20/adjacency.md:74-99` documents that a live gap-measurement run executed historical counting commands and transiently rewrote `reports/round-9/validation.json`: the recorded `acceptance_checks_passed` value flipped from true to false. The same evidence records restoration by 13:03:17Z after the change observed at 13:00:55Z; the measurement method is recorded as `stat -c %y` plus the captured Git diffs (`adjacency.md:76-99`). `reports/round-20/report-draft.md:161-172` independently describes the R9 change and restoration. These are attributed round-20 observations, not re-enacted here; no historical validator was run. Round 9 is within the protected 8–19 range declared by round 20.

A current read-only tree check on 2026-10-18 (`git diff --name-only caf1beac19b55f3bbce47e4a9e7e8710cc1c581d HEAD -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17 reports/round-18 reports/round-19`) returned no paths. That confirms only the present committed tree; it does not negate the documented transient write. Keep the receipt untouched and retain the incident as a process defect.

## Preservation and verification boundary

`git merge-base --is-ancestor caf1beac19b55f3bbce47e4a9e7e8710cc1c581d HEAD` exited 0 on 2026-10-18. The current protected range comparison above returned no paths. No round validator was executed.

FILES: reports/round-21/defects/sweep-r20.md
SUMMARY: R20's final report is not present in this checkout, its closure baseline is mislabeled, and its evidence records a transient R9 receipt rewrite that was later restored.
