# ExecCaCounterStub — scoped findings

Implemented `reports/round-71/accept-ca.py` as a read-only draft acceptance counter. It accepts `--root` and optional `--lands`, reports named V70-1 through V70-5 legs plus the quarantine-table leg, prints observed PASS/FAIL evidence, exits 0 only when all legs pass, and otherwise exits 1. It does not claim pass states without checking source records; missing evidence fails its leg. No corpus, scorecard, or telemetry files were modified. No tools were installed.

The implementation covers six round-70 receipt header/marker checks, S860's acc2d614 value, the specified quote checker invocation and zero-findings output, the scorecard correction row, Gate reject-sweep and candidate reason/flip text, and 21 quarantine rows with recognized nonempty verdicts.

Verification intentionally not run; the parent owns post-integration checks. Draft risks: original-byte preservation is evidenced by marker plus nonempty subsequent bytes, not a cryptographic comparison to a prior receipt snapshot; the lesson candidate phrase parser is intentionally simple and expects `candidate`, `reason:`, and `flip:` on one Gate line. `--lands` is shown in the summary and is not used to infer revisions.
