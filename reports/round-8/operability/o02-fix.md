# R8-O02 — parent-check receipt identity fix (`tools/harness/r8_checks.py`)

- **Shard:** R8-O02 (claim O, operability). Implements the R8-O01 fix as new code; filed round-7 artifacts are not edited.
- **Date:** 2026-10-17 (all commands below run this date).
- **Baseline:** round-8 claims baseline `e7ca0faeb6680fa9891b907be628d9db578c28f4` (`reports/round-8/claims.json`); HEAD `cf338a713060f274269cdacb18cdc0085bb06aeb`. The worktree also carries concurrent workers' edits (e.g. `tools/gates/phonology-sanity-gate.py`); none are mine.
- **Spec source:** `reports/round-8/operability/o01-diagnosis.md` (R8-O01, landed during this shard's work). My first draft used whole-payload identity (canonical JSON), which would have flagged reworded prose as a collision; §2 below is aligned to O01's normative S1–S7, and the final control set includes the two S7-required controls.

## 1. Defect (reproduced independently; matches O01 §1)

Filed symptom: `reports/round-7/validation.json:6` and `:166` —

```
"error": "wrong rejection for duplicate-parent-receipt-does-not-inflate: parent check identity collision"
```

Code path: `reports/round-7/run-validation.py:313-315` requires check labels to be pairwise unique and fires **before** the distinct-passage rule at `:336-337`; the control at `:435-438` duplicates the first receipt under one label (`PX99`), so the expected distinctness diagnostic is unreachable.

Reproduction (round-7 runner imported read-only, exact filed mutation):

```
$ python3 - <<'EOF'
import copy, importlib.util
spec = importlib.util.spec_from_file_location("r7", "reports/round-7/run-validation.py")
r7 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r7)
recon = r7.load("reports/round-7/parent-reconciliation.json")
spot  = r7.load("reports/round-7/parent-source-spotchecks.json")
bundle = r7.f_bundle_with(recon, spot)
altered = copy.deepcopy(bundle)
clone = dict(altered["spotchecks"]["checks"][0]); clone["id"] = "PX99"
altered["spotchecks"]["checks"] = [clone, dict(clone)]
try:
    r7.measure_f_parents(altered["reconciliation"], altered["spotchecks"],
                         altered["targets"], altered["ledgers"])
except ValueError as e:
    print("REJECTED:", e)
EOF
REJECTED: parent check identity collision
```

## 2. Corrected semantics (O01 §4, rules S1–S7)

- **Receipt identity** `R = (row_id, normalized source_url, source_kind, normalized locator, normalized excerpt)` — binding-relevant fields only; `basis`, `limits`, `accessed_at`, `retrieval_method`, `language_and_mediation`, `excerpt_form`, `citation` never enter `R` (S1 definition).
- **S1** — group by label; >1 distinct `R` in a group → reject `parent check identity collision: <label>` (label named for attribution, O01 RC-4).
- **S2** — repeated labels sharing one `R` are not a collision; deduplicate to the first member per label and record the rest as `parent_benign_duplicate_receipts`.
- **S3** — counting unchanged: `parent_keys` / `parent_urls` stay sets; `fewer than two distinct parent passage receipts` / `fewer than two distinct bound parent refetch URLs` keep their diagnostics; anti-inflation is enforced there, never by label counting.
- **S4** — per-check binding checks (row id, result flags, URL/kind vs bound ledger row, required text fields) run over the deduplicated representatives, unchanged.
- **S5** — label groups iterate in sorted order; diagnostics are reproducible.
- **S6** — positive measurement on the real inputs must not drift.
- **S7** — both required controls ship: `duplicate-parent-receipt-does-not-inflate` (filed shape) and `genuine-parent-check-identity-collision`.

Normalization: identity reuses this module's `url()`/`text()`/`excerpt_of()`, i.e. the same NFKC + casefold + whitespace normalization that `passage_key()` uses, so identity and counting cannot drift apart. These helpers are local, semantics-identical copies of the round-7 helpers (`reports/round-7/run-validation.py:119-138`); the fixed path does not import the filed runner at runtime.

## 3. Implementation

`tools/harness/r8_checks.py` — new file, stdlib only, read-only over repository inputs, receipts to stdout only. No write call exists in the module: `grep -n "write_text\|write_bytes\|open(" tools/harness/r8_checks.py` returns only `read_text`/`read_bytes` reads.

- `measure_parent_receipts(...)` — round-7 parent-leg semantics (rows/dispositions `reports/round-7/run-validation.py:282-312`, receipt/URL/kind binding `:318-339`) with the corrected label grouping; returns `parent_checks_raw`, `parent_checks_unique`, `parent_benign_duplicate_receipts`, `parent_distinct_passage_keys`, `parent_distinct_refetch_urls`.
- `receipt_identity(check)` — the S1 tuple.
- Fail-before reference: the filed round-7 implementation is imported read-only (`importlib`, never edited) under `sys.dont_write_bytecode = True`.
- Modes: `--selftest` (exit 0 all-pass / 1 any-fail), `--measure` (real round-7 inputs), no args → usage, exit 2; `--selftest --measure` → exit 2.

O01 §6 secondary findings are addressed in this harness: each control record carries the guard it pins (`guard`) and the guard that actually fired (`guard_fired`, e.g. `S1-identity-collision`, `S3-counting`, `S4-binding`, `malformed-input`, `None` on acceptance), and accepted measurements are recorded in full alongside diagnostics rather than discarded on the error path.

Incident found and remediated during verification: the first implementation imported the round-7 runner with bytecode caching enabled, creating `reports/round-7/__pycache__/run-validation.cpython-314.pyc` inside the filed tree. Removed, and the import now runs with `dont_write_bytecode`; verified not recreated (`ls reports/round-7/ | grep -c pycache` → `0` after reruns).

## 4. Evidence

### 4.1 Selftest — 14/14 controls, exit 0, deterministic

```
$ python3 tools/harness/r8_checks.py --selftest | sha256sum
25bf2315e6c2f3403a3fc9028720225284b1848f1a91e62ae3808543b0f5ce58  -
EXIT=0            # second run: identical sha256 and exit; foreign-cwd run: identical sha256
$ sha256sum tools/harness/r8_checks.py
0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe  tools/harness/r8_checks.py
$ python3 tools/harness/r8_checks.py --measure | sha256sum
a8c5af092ec3aef0e289c3b2c34e4652e98370ce7dbfbbd24834fd9f4aaba8a7  -    (exit 0)
```

The receipt binds `tool_sha256` (`0fb21d8e…`) and the SHA-256 of every input read: reconciliation `5034d0a6…`, spotchecks `d77c8cd8…`, targets `4ac4e531…`, baseline `c930ae6e…`, ledgers `08..12` = `292d0ad7…`/`1d19b6d1…`/`5c95f78a…`/`2c9ef83b…`/`ef76391f…`.

| control | guard pinned | guard fired | observed | pass |
|---|---|---|---|---|
| real-inputs-accepted | S6-no-drift | None | accepted: 2 checks, 2 distinct keys, 2 distinct URLs, mix `{scoped-support: 3, partial-support: 2}`, 0 benign duplicates | True |
| fail-before-round7-verbatim-duplicate | S1-identity-collision | S1-identity-collision | `parent check identity collision` (pre-fix mis-rejection) | True |
| benign-duplicate-not-misdiagnosed | S3-counting | S3-counting | `fewer than two distinct parent passage receipts: 1` | True |
| benign-duplicate-receipt-accepted | S2-dedupe | None | accepted: 3 raw / 2 unique checks, 1 benign duplicate, 2 distinct keys | True |
| fail-before-round7-benign-duplicate-valid-set | S1-identity-collision | S1-identity-collision | `parent check identity collision` (valid set wrongly rejected pre-fix) | True |
| genuine-parent-check-identity-collision | S1-identity-collision | S1-identity-collision | `parent check identity collision: P01` (S7 required) | True |
| genuine-collision-differing-url | S1-identity-collision | S1-identity-collision | `parent check identity collision: P01` | True |
| genuine-collision-mixed-group | S1-identity-collision | S1-identity-collision | `parent check identity collision: P01` | True |
| nonbinding-prose-difference-is-benign | S2-dedupe | None | accepted: reworded basis/limits/accessed_at = 1 benign duplicate, 2 distinct keys | True |
| duplicate-parent-receipt-does-not-inflate | S3-counting | S3-counting | `fewer than two distinct parent passage receipts: 1` (exact filed mutation; S7 kept) | True |
| re-ided-duplicates-do-not-inflate | S3-counting | S3-counting | `fewer than two distinct parent passage receipts: 1` | True |
| malformed-checks-not-a-list | malformed-input | malformed-input | `parent checks must be a list` (no traceback) | True |
| malformed-check-missing-id | malformed-input | malformed-input | `parent check missing id` (no traceback) | True |
| malformed-check-missing-url | malformed-input | malformed-input | `not a single URL: P01` (no traceback) | True |

Fail-before/pass-after pairs (same mutation, isolated): `fail-before-round7-verbatim-duplicate` → `benign-duplicate-not-misdiagnosed`; `fail-before-round7-benign-duplicate-valid-set` → `benign-duplicate-receipt-accepted`; the S1 direction is pinned by `genuine-parent-check-identity-collision` / `genuine-collision-differing-url` (no such control existed in round 7 — O01 §5).

S6 check: the real-input measurement is `parent_checks_raw=2`, `parent_checks_unique=2`, `parent_benign_duplicate_receipts=0`, `parent_distinct_passage_keys=2`, `parent_distinct_refetch_urls=2`, `parent_dispositions={scoped-support: 3, partial-support: 2}` — identical to the clean round-7 baseline measurement (`reports/round-8/operability/o01-diagnosis.md` §1 output `A`).

### 4.2 No-write sweeps (negative claims, with sweep commands)

```
$ find reports/round-7 corpus/lessons/round-7-sources -type f -printf '%p %T@\n' | sort | sha256sum
cc444b000dcf5277a39e39443d1d05e451162173d0f8e1af12c32f67d0493880  -
# identical before and after running --selftest and --measure (paths + mtimes)
$ ls reports/round-7/ | grep -c pycache        → 0
$ git status --porcelain reports/round-7/ corpus/lessons/round-7-sources/ | wc -l   → 0
$ git diff --stat -- reports/round-7/ corpus/lessons/round-7-sources/ | wc -l      → 0
```

### 4.3 Battery/craft selftests (context; O14 owns the filed rerun)

In a temp copy including `tools/ corpus/ examples/ reports/` (copy discarded, path not recorded):

```
$ python3 tools/check-gate-battery.py --selftest ; echo $?    → 0, stdout sha256 03f14e3d2d16fd7b0203631b8031a84e216fed1568e55ba257ad1596e96569cf
$ python3 tools/check-craft-exercise.py --selftest ; echo $? → 0, stdout sha256 77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32
```

An earlier copy missing `reports/` made the craft CLI case fail (`CRAFT-CLI-REPORT-OPEN` on `reports/supplement-opencode-1/32-craft-exercise.md`); that was the copy's incompleteness, not a defect — the full copy is green. `reports/round-8/operability/battery-rerun.json` (O14) is the authoritative battery receipt.

## 5. Limits / to-verify

- This harness re-measures the **parent-check identity leg** of round-7 claim F; it does not re-run the round-7 acceptance runner end-to-end and decides nothing about quotation truth, historical authenticity, promotion or canon. O01's shadow run already demonstrated the full 10-control round-7 parent battery passing under the corrected semantics (`o01-diagnosis.md` §5); wiring the shipped fix into the round-8 acceptance runner is O15's scope (`reports/round-8/run-validation.py`).
- Divergence note vs my first draft: whole-payload identity (canonical JSON) was replaced by O01's binding-tuple identity after the spec landed; the final control set pins both directions, including `nonbinding-prose-difference-is-benign`.
- Legacy selftest/parser defects from supplemental reviews 26/29 (`reports/supplement-opencode-1/26-parser-controls.md`, `29-local-boundaries.md`) are out of this shard's scope (O03/O04..O13) and untouched here.
- `to-verify`: none pending for the fix itself; the selftest is deterministic and rerunnable with the commands above.

FILES: tools/harness/r8_checks.py, reports/round-8/operability/o02-fix.md
