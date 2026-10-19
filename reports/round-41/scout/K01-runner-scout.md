- Seat: K01 | scout | O | date 2026-10-19 | baseline 456674d

## Runner contract evidence and census

Read-only source review covered r33–r40 (8 runner inputs, never executed). The O claim’s measured census population is specifically r34–r40 (7); r33 is included here as prior art per this seat’s mission. The five contract points are evidenced by r40: its `ROOT` derives from the runner file via `pathlib.Path(__file__).resolve().parents[2]` (stringified); there is no `chdir`; `guard_receipt()` is called before the `validation.json` write; its receipt hashes the runner; and it emits `named_findings` plus `limits`. The source and filed receipt agree on the digest (`reports/round-40/run-validation.py:3-5,68-72,197,204-209,227-244`; `reports/round-40/validation.json:143`).

| Round | ROOT / cwd | Receipt guard vs write | Runner digest | Findings / limits |
|---|---|---|---|---|
| r33 | Relative `Path(__file__).resolve().parents[2]`; main changes cwd (`:23,1454`). | Guard on publish path; second guard immediately precedes write (`:1441-1471`). | `evidence.inputs.get(RUNNER)`; filed non-null (`:1161,1293-1295`; validation `:1283`). | No `named_findings` field; round-specific limits are present (`:1293-1311`). |
| r34 | Absolute ROOT; `os.chdir(ROOT)` (`:10,26`). | `guard_receipt()` before the write (`:514-518,522-538`). | `record(RUNNER)`; filed non-null (`:389`; validation `:196`). | No `named_findings`; round-specific limits (`:398-403`). |
| r35 | Absolute ROOT; `os.chdir(ROOT)` (`:9,36`). | Guard immediately before write (`:379-383,492-508`). | `record(RUNNER)`; filed non-null (`:412`; validation `:222`). | No `named_findings`; round-specific limits (`:421-426`). |
| r36 | Absolute ROOT; `os.chdir(ROOT)` (`:8,13`). | Guard before receipt write (`:250-254,256-270`). | `rec()` has no return, so `runner_sha256: rec(...)` is null; filed null (`:63-67,210`; validation `:167`). | No `named_findings`; `round_status` and round-specific limits (`:217-220`). |
| r37 | Absolute ROOT; `os.chdir(ROOT)` (`:5,10`). | Guard before receipt write (`:216-220,222-236`). | `rec()` inserts into `inputs` but has no return, so its receipt field is null; filed null (`:67-70,187`; validation `:148`). | No `named_findings`; round-specific limits (`:194-197`). |
| r38 | Absolute ROOT; `os.chdir(ROOT)` (`:5,13`). | Guard before write (`:218-222,224-238`). | `rec()` has no return; filed null (`:68-72,188`; validation `:130`). | `named_findings` and limits (`:195-200`). |
| r39 | Absolute ROOT; `os.chdir(ROOT)` (`:5,13`). | Guard before write (`:218-222,224-238`). | `rec()` has no return; filed null (`:68-72,188`; validation `:126`). | `named_findings` and limits (`:195-200`) duplicate r38’s strings verbatim. The source identifies r39 as `glm-5.3-flash` with 16 seats while the copied route finding says xai/grok → devin (`:78-88,195-200`). |
| r40 | Relative `pathlib.Path(__file__).resolve().parents[2]`; no `chdir` (static scan output below; `:3-5`). | Guard in publish branch before `open(...validation.json...)` (`:227-244`). | `rec()` returns digest; filed field is non-null (`:68-72,197`; validation `:143`). | `named_findings` and limits exist; first finding names the r40 ROOT cure (`:204-209`). |

The field-level receipt census confirms the four nulls are r36–r39; r33–35 and r40 are non-null (`reports/round-36/validation.json:167`; `reports/round-37/validation.json:148`; `reports/round-38/validation.json:130`; `reports/round-39/validation.json:126`; compare r33 `:1283`, r34 `:196`, r35 `:222`, r40 `:143`).

## Prior art: receipt guard adoption

`receipt_guard.py` documents the adoption rule: guard before measurement and again before a publisher; without a publisher, the runner callback must guard immediately before writing (`tools/harness/receipt_guard.py:10-14,161-168`). Its selftest checks refusal before callback and re-check before publisher (`:303-340`). The adoption census’s embedded conformant example uses a file-relative ROOT, resolves the guard from ROOT, then guards before `safe_path(OUTPUT).write_text(...)` (`tools/harness/receipt_guard_adoption.py:867-893`). r33 is the relevant earlier relative-ROOT example, although its main still changes cwd (`reports/round-33/run-validation.py:23,1454`).

## Owed

- None for this scout fragment. The runner files and filed receipts were read statically; no round runner was executed.

## Citations

- `reports/round-41/claims.json:14-18` — O claim, seven-runner census and contract requirements.
- `reports/round-41/targets.json:13-17` — K01 assignment to inspect r33–r40 and receipt-guard prior art.
- Per-runner and receipt line anchors are given in the census above.
- Read-only static scanner command (not a runner): `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 && python3 -c '<line scan over run-validation.py files 33..40>'`; output for r40: `root=5 chdir=none guard=227,242 sha=197 findings=204 limits=208`. Output rows for all rounds: r33 `root=23 chdir=876,889,1454 guard=1441,1459,1470 sha=1294 findings=none limits=1135,1306`; r34 `root=10 chdir=26 guard=514,533 sha=389 findings=none limits=347,398`; r35 `root=9 chdir=36 guard=379,503 sha=412 findings=none limits=355,421`; r36 `root=8 chdir=13 guard=250,265 sha=210 findings=none limits=218`; r37 `root=5 chdir=10 guard=216,231 sha=187 findings=none limits=194`; r38 `root=5 chdir=13 guard=218,233 sha=188 findings=195 limits=199`; r39 `root=5 chdir=13 guard=218,233 sha=188 findings=195 limits=199`; r40 as above. The same scan read, but did not execute, each runner.
