# ExecRecordsFix — round 65

## Result

Drafted R1–R7 records corrections under `.ufo/waves/round-65/stage/records-fix/`. No source target was edited and no patch was applied.

Artifacts: `final-measures-ca.txt.replacement`, `revisions.txt.append`, `lesson-64.append`, `lesson-final.patch`, `verified-at.patch`, `claims-json.patch`, `control-o-binding.txt`, `log-score-entries.md`, and `fixes.md`.

## Behavior captured

- R1: receipt wrapper re-stamps the Ca run to `8bab271c691c6b1006da95316a24ae1958ec01e2`, pins its tree, and retains the complete original receipt below `--- original receipt bytes ---`; LOG/SCORECARD and LessonFinal correction drafts distinguish that read-path revision from later land `95c9194e`.
- R2: append-only correction says the receipt was added by `0c892ce`, was absent at `8d2041fa`, and does not invent a replacement measured revision.
- R3: lane-record drafts name `.ufo/waves/round-64/w1/ReviewerCa.md`; they identify the filed report's `w2/ReviewerCa.md` citation as an erratum target and the SCORECARD Ca row's `w2/` path as wrong.
- R4: claims JSON patch adds a `statement_correction` to claim O only; it preserves the frozen statement and predicate bytes and records the honest at-least-pinned-leg wording plus m1/m2 extra failures.
- R5: binding record names `control-o.txt` as O counter revision 3, sha256 `c27a9fef…`, measured at `b7d22703…`, not final revision 5; LOG append names the binding.
- R6: append after R64-M12 identifies its status sentence as pre-land and records the S687 flip committed in `95c9194e`.
- R7: proposed `verified-at:` line names round-64 blind-support verification of all 26 cited claims as SUPPORTED after repairs.

## Exact retained evidence

- Read `corpus/lessons/round-64-verifier-spotcheck.md` §6: R1–R7 facts at lines 84–90; R2 identifies `0c892ce` and missing path at `8d2041fa`, R3 the `w1/ReviewerCa.md` actual path, R4 the m1/m2 extra EDGE failures, R5 the control revision/hash binding, R6 the S687 commit, and R7 the stale metadata.
- Read original `reports/round-64/telemetry/final-measures-ca.txt`: 15 lines, counter sha `d0787979…`, original header stamp `95c9194e`, seven PASS legs, `ACCEPT-CA-64: PASS`, `exit=0`. Those original bytes are reproduced below the required delimiter in the replacement draft.
- Read `reports/round-64/telemetry/control-o.txt`: header binds counter revision 3 / sha256 `c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18` at measured revision `b7d22703dfb684713826a4064e614264867e8cd`.
- The required tree value was measured with `git rev-parse '8bab271c691c6b1006da95316a24ae1958ec01e2^{tree}'` → `0ec0e50ea828ca6d8e20298f72af49414692e9e4`.
- Read the actual report at `.ufo/waves/round-64/w1/ReviewerCa.md`; the path exists. `SCORECARD.md:1235` currently points to `w2/ReviewerCa.md`, so the R3 scorecard correction explicitly covers that reachable defect.
- `glob` reported `.ufo/reports/round-64/` not found. Therefore the filed report named by the round-65 correction record (`.ufo/reports/round-64/kotodama.md`) is unavailable in this lane; its R1 repeat and R3 citation remain an external erratum dependency, not completed here.

## Risks and blockers

- The absent filed report is the blocker for correcting its own R1/R3 statements. The stage bundle and lane-record notes do not repair that external file; L1 must obtain/apply the report erratum in its owning location.
- The claims patch is additive by design: the original O statement and predicate remain frozen; the correction object records the honest successor wording.
- No acceptance gate, build, lint, test, or formatter was run. Only the required read-only tree-resolution command was executed; the parent owns post-integration verification.
- No tool was installed or updated.
