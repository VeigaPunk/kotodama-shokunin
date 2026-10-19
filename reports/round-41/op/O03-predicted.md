- Seat: O03 | executor | O | date 2026-10-19 | baseline 456674d

# Read-only predicted census for the checker

Scope: the seven runners r34-r40 named by the O claim. I did not execute an in-tree round runner. I parsed each runner source and read its filed `validation.json` receipt; the JSON below is the semantic expected `--json` census. Defect labels are descriptive; the landed checker may spell them differently, but the row classifications and counts should match.

```json
{
  "class_counts": {
    "absolute-root": 6,
    "chdir": 6,
    "guard-not-dominating-publication": 0,
    "runner-sha256-null": 4,
    "duplicate-named-findings": 1
  },
  "runners": [
    {"round": 34, "path": "reports/round-34/run-validation.py", "relative_root": false, "chdir": true, "guard_dominates_publication": true, "receipt_runner_sha256": "be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9", "round_specific_limits": true, "named_findings": "absent", "defects": ["absolute-root", "chdir"]},
    {"round": 35, "path": "reports/round-35/run-validation.py", "relative_root": false, "chdir": true, "guard_dominates_publication": true, "receipt_runner_sha256": "4ed1ae59386acb8fa17e33dd4d6eba9d7a40581b85f45a33f104529e924bede0", "round_specific_limits": true, "named_findings": "absent", "defects": ["absolute-root", "chdir"]},
    {"round": 36, "path": "reports/round-36/run-validation.py", "relative_root": false, "chdir": true, "guard_dominates_publication": true, "receipt_runner_sha256": null, "round_specific_limits": true, "named_findings": "absent", "defects": ["absolute-root", "chdir", "runner-sha256-null"]},
    {"round": 37, "path": "reports/round-37/run-validation.py", "relative_root": false, "chdir": true, "guard_dominates_publication": true, "receipt_runner_sha256": null, "round_specific_limits": true, "named_findings": "absent", "defects": ["absolute-root", "chdir", "runner-sha256-null"]},
    {"round": 38, "path": "reports/round-38/run-validation.py", "relative_root": false, "chdir": true, "guard_dominates_publication": true, "receipt_runner_sha256": null, "round_specific_limits": true, "named_findings": "distinct", "defects": ["absolute-root", "chdir", "runner-sha256-null"]},
    {"round": 39, "path": "reports/round-39/run-validation.py", "relative_root": false, "chdir": true, "guard_dominates_publication": true, "receipt_runner_sha256": null, "round_specific_limits": true, "named_findings": "duplicate-of-round-38", "defects": ["absolute-root", "chdir", "runner-sha256-null", "duplicate-named-findings"]},
    {"round": 40, "path": "reports/round-40/run-validation.py", "relative_root": true, "chdir": false, "guard_dominates_publication": true, "receipt_runner_sha256": "3dee6e8cd4267934f0420e7e7801eceeb82293cd45a97e4b8a27277eb4ea03da", "round_specific_limits": true, "named_findings": "distinct", "defects": []}
  ]
}
```

The independent counting pass used Python AST checks limited to each `main()`'s `guard_receipt()` call and receipt-file write, plus JSON reads of the filed receipts. Result: all 7 guards precede publication; absolute `ROOT` plus `os.chdir` appears in r34-r39; exactly r36-r39 receipts have null `runner_sha256`; r39's `named_findings` equals r38's. The `rec()` helper in r36-r39 stores a digest but has no return, accounting for the null receipt field. r34/r35's `record()` and r40's `rec()` return the digest. `named_findings` is absent in r34-r37, whose receipts instead have round-specific `limits`; it is present in r38-r40.

## Owed

- `tools/harness/round_runner_conformance.py --json` reproduction and row-for-row comparison: to-verify; the checker did not exist when checked (Read returned “does not exist”). O02 owns the checker. No runner was executed.

## Citations

- Scope/acceptance points: `reports/round-41/claims.json:13-18`; O03 assignment: `reports/round-41/targets.json:55-59`.
- Absolute root and `chdir`: r34 `reports/round-34/run-validation.py:10,26`; r35 `reports/round-35/run-validation.py:9,36`; r36 `reports/round-36/run-validation.py:8,13`; r37 `reports/round-37/run-validation.py:5,10`; r38 `reports/round-38/run-validation.py:5,13`; r39 `reports/round-39/run-validation.py:5,13`; r40 relative root and no chdir `reports/round-40/run-validation.py:5,13`.
- Guard/publication order: r34 `reports/round-34/run-validation.py:533-535`; r35 `reports/round-35/run-validation.py:503-505`; r36 `reports/round-36/run-validation.py:265-267`; r37 `reports/round-37/run-validation.py:231-233`; r38 `reports/round-38/run-validation.py:233-235`; r39 `reports/round-39/run-validation.py:233-235`; r40 `reports/round-40/run-validation.py:242-244`.
- Filed receipt digest values: r34 `reports/round-34/validation.json:195-196`; r35 `reports/round-35/validation.json:221-222`; r36 `reports/round-36/validation.json:166-167`; r37 `reports/round-37/validation.json:147-148`; r38 `reports/round-38/validation.json:129-130`; r39 `reports/round-39/validation.json:125-126`; r40 `reports/round-40/validation.json:142-143`. The null-producing helper is `rec()` at r36 `run-validation.py:63-66`, r37 `:67-70`, r38 `:69-72`, and r39 `:69-72`; returning helpers are r34 `run-validation.py:41-45`, r35 `:51-55`, and r40 `:68-73`.
- Round-specific limits/findings and duplicate: r34 `reports/round-34/validation.json:182-188`; r35 `reports/round-35/validation.json:211-216`; r36 `reports/round-36/validation.json:157-160`; r37 `reports/round-37/validation.json:135-139`; r38 `reports/round-38/validation.json:116-126`; r39 `reports/round-39/validation.json:112-122` (same four named findings as r38); r40 `reports/round-40/validation.json:129-139` (distinct finding).
- Command-output evidence: read-only Python AST/receipt census, run after `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; source AST and receipt facts are summarized above. No `reports/round-*/run-validation.py` was run.
