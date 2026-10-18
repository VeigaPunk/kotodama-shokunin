# Round-19 conformance defect sweep — R21-O05..O06

- **Audit date:** 2026-10-18.
- **Scope:** round-19 final-report status and binding between the declared baseline, acceptance receipt, and admission records.
- **Mode:** read-only. No round validator or historical validator was run; no round-8..20 artifact was modified. The search was limited to this repository, not the external fleet root.
- **Round state:** the receipt and parent admission records say round 19 was admitted; this sweep does not re-run its measurements.

## Findings

### O05 — The lane-local report remains an explicitly non-final draft (open / external filing unverified)

`reports/round-19/report-draft.md:17-20` says the draft is not an admission and that the parent owns the final report and LOG/SCORECARD append. `reports/round-19/fragment-index.md:99-105` independently labels the draft as “not authorized final filing.” The path check `test -e reports/round-19/kotodama.md` was false and the in-repository `.ufo/reports/**/*.md` search returned no matches (audit date 2026-10-18). `LOG.md:3258-3271` and `SHONEN.md:192-209` record the admitted state, but no lane-local final report supersedes the draft. An external report may exist; this repo-only audit does not establish that.

Disposition: preserve the stamped draft as historical evidence and have the integrator point to or file the authorized final report through the proper destination. No round-19 artifact was rewritten.

### O06 — Acceptance receipt binds to the declaration revision, not the declared baseline (high)

`reports/round-19/claims.json:5` declares baseline `e5718945a1ab0a0c3db955338d2cae77d68fd348`. The draft correctly calls this the round-18 admit and distinguishes HEAD `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` as the round-19 declaration (`report-draft.md:6-10`). However, the primary receipt has `baseline_revision: 169c616` (`reports/round-19/validation.json:3`), and `LOG.md:3261` / `SHONEN.md:194-197` repeat that value as the baseline. `git show -s --format='%H %s' e571894 169c616` (audit date 2026-10-18) resolves the former as the round-18 admit and the latter as the round-19 declaration. Reproduce by comparing claims and receipt baselines, then resolving the revisions with `git show -s` (2026-10-18).

The receipt says acceptance true and failures empty (`validation.json:38-41`), but this identifier mismatch means the receipt does not bind to the baseline declared in `claims.json` as filed. The validator was not executed during this sweep. Preserve the receipt and route a new authorized remeasurement/correction; do not rewrite historical acceptance evidence.

## Preservation and verification boundary

Read-only preservation check on 2026-10-18: `git merge-base --is-ancestor e5718945a1ab0a0c3db955338d2cae77d68fd348 HEAD` exited 0; `git diff --name-only e5718945a1ab0a0c3db955338d2cae77d68fd348 HEAD -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17 reports/round-18` returned no paths. This is a current Git-tree comparison, not evidence about any transient historical worktree state. No round validator was executed.

FILES: reports/round-21/defects/sweep-r19.md
SUMMARY: R19 is recorded admitted, but its report remains unfinalized and its acceptance receipt names the declaration commit instead of the declared baseline.
