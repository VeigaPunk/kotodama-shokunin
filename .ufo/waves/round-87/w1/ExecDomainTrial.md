# ExecDomainTrial — round87 ONE v1

Axes: operability, byte-faithful fixture retention, durable evidence, scope preservation.

## Deliverable and observation

All implementation/evidence files are under `.ufo/waves/round-87/w1/stage/ExecDomainTrial/`:
- `run-trial.py`: explicit required `--tool` and `--work`; six bounded candidate CLI invocations, isolated temporary work, 15-second per-case timeout, independent expectations, command/rc/stdout/stderr and SHA-256 receipt.
- `craft.json`: byte-faithful six-record NON-CANON r86 packet from base `83846a22ee1e9da7aa52ac505ccebf4455169247`, identical at freeze `2a3b5643899c3520867ae930593cafef6ef19cad`; SHA-256 `4f631b60b5ea5d5cf42b2ef394d548ff557e4ccaa52f176d7327fead8f34c982`.
- `candidate-under-trial.py`: retained ExecAuditor candidate snapshot, SHA-256 `4abcbbd058c33b95cc7c8acc4840493ccaeda0bdf01cb3947d074c3352c497aa`.
- `provenance.json`, `invocation.json`, `trial-receipt.json`, `trial-stderr.txt`: durable source provenance and exact retained execution outputs/digests. Commands use relative subprocess arguments and symbolic isolated-work notation, not deleted scratch evidence links.

Executed the assigned audit once against that candidate: runner exit **1**, **5/6 independently expected relationships matched**. Empty runner stderr.


CLI contract additionally read from `.ufo/waves/round-87/w1/ExecAuditor.md` and retained candidate source lines 214–240: `--packet PATH --json`; clean exit 0, findings exit 1, input/CLI error exit 2. Candidate `--work` belongs only to its selftest; this runner keeps its own required `--work` separate. ExecAuditor's reported 37/37 selftest and 12/12 frozen battery are author results, not executions by this seat.
| Case | Expected / observed rc | Observed finding | Result |
|---|---|---|---|
| inherited-six | 0 / 0 | none | matched |
| missing-origin | 1 / 1 | CLOCK_MISSING | matched |
| translation-backdated | 1 / 1 | TRANSLATION_CLOCK | matched |
| conjecture-promoted | 1 / 1 | EDITORIAL_CONFLICT | matched |
| ambiguous-answer-selected | 1 / 1 | SOLUTION_CONFLICT | matched |
| origin-promoted-from-witness | 1 / 0 | none | **miss retained** |

The last case copies the surviving witness date into the originally unknown origin while leaving its old explanation unchanged. This author-side creative-packet expectation is outside the frozen finite counter: candidate accepts a structurally valid dated origin and cannot establish its historical justification. No invented diagnostic label is required; any structured refusal would meet this independent expectation. This miss is a scope limit, not evidence that the specified finite 12/12 O claim failed. This seat did not run the frozen 12-case counter or independently establish 12/12.

## Boundaries and retained history

This is an audit of inherited hypothetical creative records, **not real historical evidence, semantic truth, source verification, lore acceptance, or outside admission**. The r86 stage already contained `check-craft.py`, including completeness and these relationship checks; provenance records its pinned digest. No first-completeness-checking claim is made. No new sources/source IDs, production files, claims, frozen counters, counter history, Git/JJ state, sibling files, external substrates or global configuration were changed. L1 canonical planning remains authoritative; the unresolved L2 planner-policy conflict is disclosed, not resolved by this trial.

No LSP tool is mounted in this seat; no existing symbols were refactored. No tools were installed or updated. Only the assigned bounded trial ran; no build/lint/formatter/broad tests. Receipts were retained in the owned stage before removal of owned scratch. L1 owns integration and post-integration gates.

## Self-evaluation

Accuracy 4/5: outputs and source digests retained; the semantic miss is explicit rather than hidden. Completeness 4/5: all assigned relationships audited; origin justification remains deliberately outside the candidate contract. Clarity 4/5: distinguishes six trial probes from six input records and frozen twelve-case battery. Actionability 4/5: runner, packet and candidate snapshot reproduce the audit with caller-owned isolated work. Conciseness 4/5: raw details are in JSON rather than repeated here. Overall 4.0/5. Improvements: L1 should retain the semantic-limit wording with any O admission; do not interpret the historical wording as real evidence. The user should agree with this narrow evidence-backed assessment.

Report: .ufo/waves/round-87/w1/ExecDomainTrial.md
