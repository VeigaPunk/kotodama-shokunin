# Round-65 Ca R1–R7 correction drafts

Drafts only; no target file was edited or patch applied.

| Fix | Draft artifact | Target / disposition |
|---|---|---|
| R1 | `final-measures-ca.txt.replacement` | Re-stamps the Ca receipt to `8bab271c691c6b1006da95316a24ae1958ec01e2`, pins tree `0ec0e50ea828ca6d8e20298f72af49414692e9e4`, states the correction, and preserves the complete original receipt bytes verbatim below the required delimiter, including its original `95c9194e` stamp. |
| R1 | `log-score-entries.md` | Supplies the LOG.md and SCORECARD.md R1 correction entries, with measured revision and tree. |
| R1 | `lesson-final.patch` | Minimal correction of the false all-receipts-at-`95c9194e` sentence in `.ufo/waves/round-64/w2/LessonFinal.md`. |
| R2 | `revisions.txt.append` | Append-only named correction; retains the original claim and does not infer a replacement measured revision. |
| R3 | `log-score-entries.md` | Names `.ufo/waves/round-64/w1/ReviewerCa.md` as actual and the filed report's `w2/ReviewerCa.md` citation as erratum target. The SCORECARD row's own wrong `w2/` path is explicitly identified. |
| R4 | `claims-json.patch` | Adds only a `statement_correction` object to claim O with the honest “at least their pinned leg” wording and m1/m2 extra failures. Existing claim/predicate bytes are kept unchanged; the predicate member remains byte-for-byte the same. |
| R5 | `control-o-binding.txt`; `log-score-entries.md` | Records control-o.txt as revision 3 / sha256 `c27a9fef…` measured at `b7d22703…`, not final revision 5; the LOG append names the binding. |
| R6 | `lesson-64.append` | Adds the correction immediately after R64-M12: the quoted status was a pre-land snapshot and S687's flip is committed in `95c9194e`. |
| R7 | `verified-at.patch` | Replaces the stale skeleton metadata with the round-64 blind-support verification result for all 26 cited claims. |

## Cross-lane dependency

The filed report at `.ufo/reports/round-64/kotodama.md` is absent from this lane (`.ufo/reports/round-64/` was not found). Its R1 “After at `95c9194e`” repeat and R3 `w2/ReviewerCa.md` citation cannot be edited here; their report erratum remains an external integration dependency. The available `corpus/lessons/round-64-verifier-spotcheck.md` supplies the routed findings, but is not that filed report. Do not mark the filed-report erratum complete from these drafts.
