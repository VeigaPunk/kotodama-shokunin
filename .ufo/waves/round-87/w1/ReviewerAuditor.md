# ReviewerAuditor — round87 w1

## Findings by severity

No actionable candidate defect found within the frozen finite O predicate. Recommendation only: the reviewed staged implementation satisfies the assigned 12-case discrimination predicate; this is author-side evidence, not admission or an integration claim.

**Retained classification discrepancy (non-killing):** three independently prepared held-outs (`array-solutions`, `array-editorial`, `array-translation`) expected exit2 `ATTESTATION_ERROR`; observed exit1 `RECORD_FIELD`, records=6, empty stderr. Candidate lines93–95 explicitly classify malformed optional relationship types as structural findings. Frozen claims do not prescribe an error ID for these optional nested shapes. JSON syntax/top-level decoding errors still return exit2; therefore these three original expectation misses are preserved, not silently counted as passes or elevated into a new kill rule. If “malformed input” is intended to include every nested schema violation, that wording is ambiguous with the structural-findings exit1 contract.

## Code and contract evidence

Reviewed actual `.ufo/waves/round-87/w1/stage/ExecAuditor/check-attestation-packet.py` lines1–240, not merely its selftest receipt. Reviewed bytes retained as `stage/ReviewerAuditor/candidate-reviewed.py`, SHA256 `4abcbbd058c33b95cc7c8acc4840493ccaeda0bdf01cb3947d074c3352c497aa`.

Also inspected `ExecAuditor.md` lines1–41 after L1's ready notification. Its design lines13–16 explicitly distinguish malformed packet containers (exit2) from malformed optional relationship objects (exit1 RECORD_FIELD), matching implementation and retained outputs. The three held-out expectation discrepancies are therefore not deviations from the candidate's stated CLI contract; the original expectations remain unaltered.

- Lines55–60 validate root/record container types; lines63–78 validate IDs and textual fields. Identity is checked as text before set membership, avoiding unhashable invalid-ID crashes. Count is computed from actual records, not fixed at six.
- Lines79–91 require each clock object, explicit value (including null), valid non-null calendar date, nonblank reason and scope. Invalid dates are checked before chronology comparisons.
- Lines93–118 guard nested relationships before access, prohibit unresolved selected answers, distinguish conjectured from transmitted wording, and reject target attestation earlier than a valid translation date. Unknown target dates are not invented.
- Lines42–52 reject duplicate keys at every JSON-object depth and non-JSON constants. Lines214–236 implement the public CLI and deterministic JSON error path. Normal packet audit is read-only; only explicitly selected selftest mode writes beneath existing --work.
- Actual affected caller is frozen `reports/round-87/measure87.py`: `evaluate` launches the same public `--packet PATH --json` process and compares exit/finding IDs; positive cases require records=6 and empty findings. `main` materializes supplied candidate bytes. No alternative gate/runtime or import-based surrogate was used.
- At base `83846a22ee1e9da7aa52ac505ccebf4455169247`, the production path is absent from the explicit immutable tree listing. Read the existing r86 `ExecCraftLedger/check-craft.py`: it already checks completeness **and the relevant relationships** (solutions, conjectures, translations). The honest delta is a production, variable-count JSON-diagnostics CLI with isolated CLI selftests, not first completeness checking or first relationship knowledge.

LSP prerequisite: `xd://lsp` returned “No such tool”; no server/status/references/definition/diagnostics device is mounted. Text inspection above is a fallback, not semantic-reference proof.

## Executed receipts

All relative paths below are under `.ufo/waves/round-87/w1/stage/ReviewerAuditor/`.

1. `frozen-battery.json` and `frozen-battery-process.json`: exact frozen counter from `2a3b5643899c3520867ae930593cafef6ef19cad`, supplied candidate SHA above; observed exit0, **12/12**. Counter SHA256 `131b29e84d39c2cbd22993aaadd469b5a96602651927730c980503cc74738e62`; baseline packet SHA256 `4f631b60b5ea5d5cf42b2ef394d548ff557e4ccaa52f176d7327fead8f34c982`. Counter copy `measure87.frozen.py` is unedited.
2. `heldout.py`, `heldout-expectations.json`, `heldout-receipt.json`, and `packets/*.json`: **26** independent public-CLI probes, **23/26 original expectations matched**, three classification discrepancies above. Covered reverse order; one/seven actual record counts; explicit null dates; missing/null/array clocks; integer/boolean/object dates; null/array/Unicode-blank reasons; missing value; blank/duplicate IDs; null text; translation earlier/equal/later/unknown dates and invalid translation date; optional nested arrays; duplicate JSON keys; top-level null. No traceback observed in retained outputs.

Reproduce after explicitly recreating own scratch:

```sh
mkdir -p /fast/scratch/hyaku/kotodama-r87/ReviewerAuditor
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-87/w1/stage/ReviewerAuditor/heldout.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-87/w1/stage/ReviewerAuditor/candidate-reviewed.py
```

Frozen-battery exact invocation is retained in `frozen-battery-process.json`; it uses explicit immutable Git revision and existing own scratch, not a production integration claim.

## Residual risk and verification gaps

- Finite structural discrimination only. No semantic truth, quotation support, authenticity, cultural canon, universal tool-substitution rejection, or general saturation result follows.
- Not every optional field/subfield is schema-validated: for example solution candidate contents are outside this finite predicate. No external evidence verification is attempted.
- Reviewed staged bytes, not a later L1 production commit; final integration/committed-byte measurement remains L1's responsibility. Did not run sibling gates or candidate selftest broadly; only assigned independent candidate probes and exact frozen battery ran.
- L1 canonical planning remains; unresolved L2 planner-policy conflict and lowest-axis calibration debt are not waived. Source IDs and counter history unchanged.
- Canonical-runtime rerouting and `resume_continuity_v1` are not changed by this standalone auditor candidate; no resume/rerouting claim is made. No alternate runtime invoked.

## Scope and self-evaluation

No production edits, Git/jj mutations, installs, delegation, intentional background jobs, or writes outside own stage/report/scratch. The shell tool automatically backgrounded the held-out command to deliver an incoming message; completion was delivered without polling. Scratch packets were copied into own stage; scratch removed before yielding. No tools installed/updated.

Accuracy4 (hash-bound candidate and raw receipts; nested-error wording ambiguous); completeness4 (all assigned held-out families covered, final integration deliberately unverified); clarity4 (three expectation misses explicit rather than hidden); actionability4 (reproducible driver/packets and immutable counter, scratch must be recreated); conciseness4 (longer evidence retained to distinguish finite O from broader truth). Mean4.0. Highest-value limitation to preserve: exact bytes/finite predicate only, not admission.

Report: .ufo/waves/round-87/w1/ReviewerAuditor.md
