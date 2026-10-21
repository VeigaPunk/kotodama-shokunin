# Round 50 attempt1 — receipt_guard mutation probe
## Scoped result
- **Item attacked:** claim O, the new ref-probing and landed-identity logic in `tools/harness/receipt_guard.py` at `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`.
- **Verdict: PARTIAL — detector sensitivity, not a round-admission judgment.** Of 12 isolated single-point mutants, the unchanged 69-control `--selftest` killed 9 and missed 3. There were no inconclusive trials. The pristine implementation passed 69/69 initially and after each of the 12 restorations. This probe does **not** demonstrate a defect in the pristine guard; it demonstrates three missing regression detectors.
- **Axes named:** operability (assigned claim); measurement dimensions were ref coverage, fail-closed behavior, identity accuracy, detector sensitivity, and exact restoration/isolation. No coverage-entry, source-row, calibration-checker, README-gate, or round-admission verdict is offered.
- **Survivors:** M08 (stop skipping symbolic refs), M09 (omit remote holders from `hit_refs`), M11 (derive `landed_blob` from HEAD). A surviving mutant is a coverage finding, not permission to weaken the contract.
All file:line references below refer to the immutable landed revision, not the lane working tree.
## Isolation, source, and detector
The lane was read using `git show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:tools/harness/receipt_guard.py`; no mutable lane tool bytes were used as the baseline. Reproduction used one private shared clone, checked out to the exact landed revision:
```sh
mktemp -d /tmp/kotodama-r50-mutateguard-21-XXXXXX
# actual result: /tmp/kotodama-r50-mutateguard-21-l0w53L
env GIT_CEILING_DIRECTORIES=/tmp git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/kotodama-r50-mutateguard-21-l0w53L
env GIT_CEILING_DIRECTORIES=/tmp git -C /tmp/kotodama-r50-mutateguard-21-l0w53L checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
```
Clone and checkout each exited 0 without stdout/stderr. Each mutation changed only the listed behavior-bearing point in that clone’s guard. The detector, its 69 controls, and all other source bytes were left unchanged; no mutants were combined. Trials were necessarily serialized on the same file, with restoration and a green pristine-byte detector run between trials. Independent prerequisite reads and source/runtime discovery were batched concurrently. No subagents, background jobs, other runtime/orchestrator, credentials, network fetch, or live-process probes were used.
Actual detector invocation on every trial:
```text
cwd = /tmp/kotodama-r50-mutateguard-21-l0w53L
argv = ["python3", "-B", "tools/harness/receipt_guard.py", "--selftest"]
environment overrides: GIT_CEILING_DIRECTORIES=/tmp; PYTHONDONTWRITEBYTECODE=1
REFRESH_RECEIPTS removed from the outer environment
outer subprocess timeout = 60 seconds
```
The guard’s selftest creates its own disposable fixtures under the private clone’s `.scratch`. Its internally invoked receipt processes test both ordinary and refresh environments. All 25 detector invocations completed before the bound. Outer stderr was empty on all 25 runs. Child receipt stderr is captured in the JSON control records and is quoted below.
Pristine SHA-256 (both `git show` bytes and the checked-out target):

```text
5a61c35016b61c71071d774773b329a4bb6646f9959bd3b82a15528b328cef14
```
For M01 the pre-mutation pristine detector is P00; for M02–M12 it is the preceding restoration run. Every restored run also reran the same detector. A kill requires green pristine/restored bytes plus a red mutated run; no baseline failures were counted as kills.
## Mutation matrix
| Mutant | Landed file:line | Single-point defect | Outer exit | Passed controls | Verdict |
|---|---|---|---:|---:|---|
| M01 | `tools/harness/receipt_guard.py:105` | Skip every remote-tracking ref | 1 | 56/69 | **KILLED** |
| M02 | `tools/harness/receipt_guard.py:105` | Skip every local branch ref | 1 | 65/69 | **KILLED** |
| M03 | `tools/harness/receipt_guard.py:106` | Ignore for-each-ref stderr on successful exit | 1 | 67/69 | **KILLED** |
| M04 | `tools/harness/receipt_guard.py:207` | Derive landed identity from local heads, not remotes | 1 | 57/69 | **KILLED** |
| M05 | `tools/harness/receipt_guard.py:194 (insert before)` | Return early for REFRESH_RECEIPTS=1 before probing refs | 1 | 65/69 | **KILLED** |
| M06 | `tools/harness/receipt_guard.py:125` | Accept non-commit objects in enumerated refs | 1 | 68/69 | **KILLED** |
| M07 | `tools/harness/receipt_guard.py:199` | Remove the explicit HEAD tip from committed probes | 1 | 62/69 | **KILLED** |
| M08 | `tools/harness/receipt_guard.py:123-124` | Stop skipping symbolic refs | 0 | 69/69 | **SURVIVED** |
| M09 | `tools/harness/receipt_guard.py:214` | Suppress remote holders from hit_refs diagnostics | 0 | 69/69 | **SURVIVED** |
| M10 | `tools/harness/receipt_guard.py:212` | Report HEAD as landed_sha | 1 | 65/69 | **KILLED** |
| M11 | `tools/harness/receipt_guard.py:213` | Report HEAD receipt blob as landed_blob | 0 | 69/69 | **SURVIVED** |
| M12 | `tools/harness/receipt_guard.py:105` | Limit remote enumeration to origin | 1 | 68/69 | **KILLED** |

## Per-mutant edits and actual outputs
The JSON excerpts preserve the actual stdout values. All failed control records are included for killed mutants. For survivors, selected passing control records expose the missed condition; uninteresting passing rows are omitted. `outer_stderr` is the real selftest process’s stderr, distinct from each fixture child’s captured `stderr`.

### M01 — Skip every remote-tracking ref — KILLED

Location: `tools/harness/receipt_guard.py:105`.

Original:

```python
                  "refs/heads", "refs/remotes")
```

Mutation:

```python
                  "refs/heads")
```

**Expected detector:** r50-detached-below-remote must still refuse the receipt (exit 3), so --selftest must go red.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-detached-below-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-local-over-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=df711e6281bf65e24541854816f59865b23bf630 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=none landed_sha=none landed_blob=none hit_refs=HEAD; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-unborn-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-other-branch-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-other-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-head-is-remote-tip",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=none landed_sha=none landed_blob=none hit_refs=HEAD,refs/heads/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-corrupt-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-missing-object-ref",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-tree-typed-ref",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-refresh-landed",
      "exit": 0,
      "expected_exit": 0,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-refresh-corrupt-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-refresh-nonexact-landed",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-env-scrub",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 56,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

### M02 — Skip every local branch ref — KILLED

Location: `tools/harness/receipt_guard.py:105`.

Original:

```python
                  "refs/heads", "refs/remotes")
```

Mutation:

```python
                  "refs/remotes")
```

**Expected detector:** unborn-local-branch-refused and other-local-branch-refused must still refuse, so --selftest must go red.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-local-branch-not-landed",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=df711e6281bf65e24541854816f59865b23bf630 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=none landed_sha=none landed_blob=none hit_refs=HEAD; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-nonutf8-refname",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "unborn-local-branch-refused",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "other-local-branch-refused",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 65,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

### M03 — Ignore for-each-ref stderr on successful exit — KILLED

Location: `tools/harness/receipt_guard.py:106`.

Original:

```python
    if result.returncode or result.stderr:
```

Mutation:

```python
    if result.returncode:
```

**Expected detector:** r50-corrupt-remote and r50-refresh-corrupt-remote must fail closed with RECEIPT-GUARD-GIT, so --selftest must go red.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-corrupt-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-refresh-corrupt-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 67,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

### M04 — Derive landed identity from local heads, not remotes — KILLED

Location: `tools/harness/receipt_guard.py:207`.

Original:

```python
    landed = next((hit for hit in hits if hit[0].startswith("refs/remotes/")), None)
```

Mutation:

```python
    landed = next((hit for hit in hits if hit[0].startswith("refs/heads/")), None)
```

**Expected detector:** r50-local-branch-not-landed must report landed_ref=none and landed_sha=none; remote controls must retain their remote identities.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-detached-below-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=none landed_sha=none landed_blob=none hit_refs=refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-local-over-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=df711e6281bf65e24541854816f59865b23bf630 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=none landed_sha=none landed_blob=none hit_refs=HEAD,refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-unborn-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=none committed_blob=none landed_ref=none landed_sha=none landed_blob=none hit_refs=refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-other-branch-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=reports/round-50/validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=none landed_sha=none landed_blob=none hit_refs=refs/remotes/origin/kotodama; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-other-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=reports/up/validation.json committed_sha=3748e84d32e6bba0c1870d655d6c5a575ebe9b4f committed_blob=none landed_ref=none landed_sha=none landed_blob=none hit_refs=refs/remotes/upstream/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-local-branch-not-landed",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=df711e6281bf65e24541854816f59865b23bf630 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=refs/heads/main landed_sha=df711e6281bf65e24541854816f59865b23bf630 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=HEAD,refs/heads/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-head-is-remote-tip",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=refs/heads/main landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=HEAD,refs/heads/main,refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-refresh-landed",
      "exit": 0,
      "expected_exit": 0,
      "passed": false,
      "stderr": "receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=none landed_sha=none landed_blob=none hit_refs=refs/remotes/origin/main [RECEIPT-GUARD-REFRESH]"
    },
    {
      "control": "r50-refresh-local",
      "exit": 0,
      "expected_exit": 0,
      "passed": false,
      "stderr": "receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=validation.json committed_sha=df711e6281bf65e24541854816f59865b23bf630 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=refs/heads/main landed_sha=df711e6281bf65e24541854816f59865b23bf630 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=HEAD,refs/heads/main [RECEIPT-GUARD-REFRESH]"
    },
    {
      "control": "attached-head-holds-refused",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=refs/heads/main landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=HEAD,refs/heads/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "unborn-local-branch-refused",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=none committed_blob=none landed_ref=refs/heads/side landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=refs/heads/side; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "other-local-branch-refused",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/heads/side landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=refs/heads/side; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 57,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

### M05 — Return early for REFRESH_RECEIPTS=1 before probing refs — KILLED

Location: `tools/harness/receipt_guard.py:194 (insert before)`.

Original:

```python
(no early return; proceed to head, branch = _head_state(root))
```

Mutation:

```python
    if os.environ.get(REFRESH_ENV) == "1":
        return
```

**Expected detector:** r50-refresh-corrupt-remote must still exit 3 with RECEIPT-GUARD-GIT, and valid refresh cases must print their identity diagnostics.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "committed-refresh-allowed",
      "exit": 0,
      "expected_exit": 0,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-refresh-landed",
      "exit": 0,
      "expected_exit": 0,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-refresh-local",
      "exit": 0,
      "expected_exit": 0,
      "passed": false,
      "stderr": ""
    },
    {
      "control": "r50-refresh-corrupt-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 65,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

### M06 — Accept non-commit objects in enumerated refs — KILLED

Location: `tools/harness/receipt_guard.py:125`.

Original:

```python
        if not OID_RE.fullmatch(commit) or kind != b"commit":
```

Mutation:

```python
        if not OID_RE.fullmatch(commit):
```

**Expected detector:** r50-tree-typed-ref must identify a Git error, not a committed receipt, even if ls-tree can read that tree object.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-tree-typed-ref",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=3c7779458a63262d1d86c69e6abed6e2aea65a6f landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 68,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

The child still exits 3, but reports `RECEIPT-GUARD-COMMITTED` with a tree OID as `landed_sha`; the detector kills the diagnostic/identity error rather than relying only on exit status.

### M07 — Remove the explicit HEAD tip from committed probes — KILLED

Location: `tools/harness/receipt_guard.py:199`.

Original:

```python
    tips = ([("HEAD", head)] if head is not None else []) + refs
```

Mutation:

```python
    tips = refs
```

**Expected detector:** r50-detached-below-remote must preserve the HEAD identity while probing the remote; hit_refs must still include HEAD when it holds the receipt.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-detached-below-remote",
      "exit": 1,
      "expected_exit": 3,
      "passed": false,
      "stderr": "Traceback (most recent call last):\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 716, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 711, in main\n    guard_receipt(args.receipt, repo_root=args.repo_root)\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 226, in guard_receipt\n    _check_receipt(receipt_path, repo_root)\n    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 208, in _check_receipt\n    committed_blob = blobs[head] if head is not None else None\n                     ~~~~~^^^^^^\nKeyError: '9489a228e7ba5f9fec3febe81277204e03cd9ff4'"
    },
    {
      "control": "r50-local-over-remote",
      "exit": 1,
      "expected_exit": 3,
      "passed": false,
      "stderr": "Traceback (most recent call last):\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 716, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 711, in main\n    guard_receipt(args.receipt, repo_root=args.repo_root)\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 226, in guard_receipt\n    _check_receipt(receipt_path, repo_root)\n    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 208, in _check_receipt\n    committed_blob = blobs[head] if head is not None else None\n                     ~~~~~^^^^^^\nKeyError: 'df711e6281bf65e24541854816f59865b23bf630'"
    },
    {
      "control": "r50-other-remote",
      "exit": 1,
      "expected_exit": 3,
      "passed": false,
      "stderr": "Traceback (most recent call last):\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 716, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 711, in main\n    guard_receipt(args.receipt, repo_root=args.repo_root)\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 226, in guard_receipt\n    _check_receipt(receipt_path, repo_root)\n    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 208, in _check_receipt\n    committed_blob = blobs[head] if head is not None else None\n                     ~~~~~^^^^^^\nKeyError: '3748e84d32e6bba0c1870d655d6c5a575ebe9b4f'"
    },
    {
      "control": "r50-local-branch-not-landed",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=df711e6281bf65e24541854816f59865b23bf630 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=none landed_sha=none landed_blob=none hit_refs=refs/heads/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-refresh-landed",
      "exit": 1,
      "expected_exit": 0,
      "passed": false,
      "stderr": "Traceback (most recent call last):\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 716, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 711, in main\n    guard_receipt(args.receipt, repo_root=args.repo_root)\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 226, in guard_receipt\n    _check_receipt(receipt_path, repo_root)\n    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 208, in _check_receipt\n    committed_blob = blobs[head] if head is not None else None\n                     ~~~~~^^^^^^\nKeyError: '9489a228e7ba5f9fec3febe81277204e03cd9ff4'"
    },
    {
      "control": "r50-refresh-nonexact-landed",
      "exit": 1,
      "expected_exit": 3,
      "passed": false,
      "stderr": "Traceback (most recent call last):\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 716, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 711, in main\n    guard_receipt(args.receipt, repo_root=args.repo_root)\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 226, in guard_receipt\n    _check_receipt(receipt_path, repo_root)\n    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 208, in _check_receipt\n    committed_blob = blobs[head] if head is not None else None\n                     ~~~~~^^^^^^\nKeyError: '9489a228e7ba5f9fec3febe81277204e03cd9ff4'"
    },
    {
      "control": "r50-env-scrub",
      "exit": 1,
      "expected_exit": 3,
      "passed": false,
      "stderr": "Traceback (most recent call last):\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 716, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 711, in main\n    guard_receipt(args.receipt, repo_root=args.repo_root)\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 226, in guard_receipt\n    _check_receipt(receipt_path, repo_root)\n    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/tmp/kotodama-r50-mutateguard-21-l0w53L/tools/harness/receipt_guard.py\", line 208, in _check_receipt\n    committed_blob = blobs[head] if head is not None else None\n                     ~~~~~^^^^^^\nKeyError: '9489a228e7ba5f9fec3febe81277204e03cd9ff4'"
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 62,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

This is not a syntax/startup kill: the mutated selftest ran all 69 controls. Several fixture children raise `KeyError` because detached HEAD was removed from the probed blob map, and the unchanged detector detects their wrong exits.

### M08 — Stop skipping symbolic refs — SURVIVED

Location: `tools/harness/receipt_guard.py:123-124`.

Original:

```python
        if symref:
            continue
```

Mutation:

```python
(delete the two-line skip)
```

**Expected detector:** The direct-ref contract at lines 10-12 calls for exclusion of resolving symbolic aliases. A valid-symbolic-ref fixture would be needed; the existing dangling-origin-head control is not such a fixture.

**Actual output:**

```json
{
  "outer_exit": 0,
  "outer_stderr": "",
  "selected_passing_controls": [
    {
      "control": "r50-dangling-origin-head",
      "exit": 0,
      "expected_exit": 0,
      "passed": true,
      "stderr": ""
    }
  ],
  "stdout_fields": {
    "controls_passed": 69,
    "controls_total": 69,
    "selftest_passed": true
  }
}
```

Observed: deletion of the symbolic-ref skip leaves all 69 controls green. The only explicit remote symbolic-head case at lines 465–469 is dangling. [INFERENCE] A resolving symbolic alias would now be included among direct holders instead of skipped, potentially changing `landed_ref`/`hit_refs`. No additional valid-symbolic-ref reproduction was run; the observed finding here is the detector gap.

### M09 — Suppress remote holders from hit_refs diagnostics — SURVIVED

Location: `tools/harness/receipt_guard.py:214`.

Original:

```python
                f"hit_refs={','.join(name for name, _, _ in hits)}")
```

Mutation:

```python
                f"hit_refs={','.join(name for name, _, _ in hits if not name.startswith('refs/remotes/'))}")
```

**Expected detector:** r50-detached-below-remote should assert its remote holder in hit_refs, and r50-head-is-remote-tip should assert every HEAD/local/remote holder.

**Actual output:**

```json
{
  "outer_exit": 0,
  "outer_stderr": "",
  "selected_passing_controls": [
    {
      "control": "r50-detached-below-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": true,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-refresh-landed",
      "exit": 0,
      "expected_exit": 0,
      "passed": true,
      "stderr": "receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs= [RECEIPT-GUARD-REFRESH]"
    }
  ],
  "stdout_fields": {
    "controls_passed": 69,
    "controls_total": 69,
    "selftest_passed": true
  }
}
```

Observed wrong metadata remains `passed: true`: the detached remote-held receipt prints an empty `hit_refs=` despite its populated `landed_ref`. The contract at lines 14–15 says every holder is listed.

### M10 — Report HEAD as landed_sha — KILLED

Location: `tools/harness/receipt_guard.py:212`.

Original:

```python
                f"landed_sha={landed[1] if landed else 'none'} "
```

Mutation:

```python
                f"landed_sha={head if landed else 'none'} "
```

**Expected detector:** r50-detached-below-remote, r50-local-over-remote, and r50-unborn-remote must distinguish remote identity from HEAD.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-detached-below-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-local-over-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=df711e6281bf65e24541854816f59865b23bf630 committed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f landed_ref=refs/remotes/origin/main landed_sha=df711e6281bf65e24541854816f59865b23bf630 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=HEAD,refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-unborn-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": false,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=none committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=None landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-refresh-landed",
      "exit": 0,
      "expected_exit": 0,
      "passed": false,
      "stderr": "receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=refs/remotes/origin/main [RECEIPT-GUARD-REFRESH]"
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 65,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

### M11 — Report HEAD receipt blob as landed_blob — SURVIVED

Location: `tools/harness/receipt_guard.py:213`.

Original:

```python
                f"landed_blob={landed[2] if landed else 'none'} "
```

Mutation:

```python
                f"landed_blob={(committed_blob or 'none') if landed else 'none'} "
```

**Expected detector:** r50-detached-below-remote and r50-refresh-landed should assert the remote receipt blob, not HEAD's absent receipt blob.

**Actual output:**

```json
{
  "outer_exit": 0,
  "outer_stderr": "",
  "selected_passing_controls": [
    {
      "control": "r50-detached-below-remote",
      "exit": 3,
      "expected_exit": 3,
      "passed": true,
      "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=none hit_refs=refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
    },
    {
      "control": "r50-refresh-landed",
      "exit": 0,
      "expected_exit": 0,
      "passed": true,
      "stderr": "receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=none hit_refs=refs/remotes/origin/main [RECEIPT-GUARD-REFRESH]"
    }
  ],
  "stdout_fields": {
    "controls_passed": 69,
    "controls_total": 69,
    "selftest_passed": true
  }
}
```

Observed wrong metadata remains `passed: true`: the remote-held receipt reports `landed_blob=none` even though the pristine run reports `landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f`. Its remote `landed_sha` remains unchanged; the detector never checks this blob field.

### M12 — Limit remote enumeration to origin — KILLED

Location: `tools/harness/receipt_guard.py:105`.

Original:

```python
                  "refs/heads", "refs/remotes")
```

Mutation:

```python
                  "refs/heads", "refs/remotes/origin")
```

**Expected detector:** r50-other-remote must still refuse the upstream-held receipt, so --selftest must go red.

**Actual output:**

```json
{
  "failed_controls": [
    {
      "control": "r50-other-remote",
      "exit": 0,
      "expected_exit": 3,
      "passed": false,
      "stderr": ""
    }
  ],
  "outer_exit": 1,
  "outer_stderr": "",
  "stdout_fields": {
    "controls_passed": 68,
    "controls_total": 69,
    "selftest_passed": false
  }
}
```

## Survivors and smallest author-lane fixes
1. **M08 — symbolic-ref exclusion is not exercised.** Contract: `tools/harness/receipt_guard.py:10-12`; implementation: `:123-124`; existing dangling-only case: `:465-469`. Add one fixture with `refs/remotes/origin/HEAD` resolving to a receipt-holding `refs/remotes/origin/main`. Assert that `landed_ref` is the direct target and that the symbolic alias is absent from `hit_refs`. This is test-only advice; the pristine skip is already present.
2. **M09 — remote holder completeness is not asserted.** Contract: `tools/harness/receipt_guard.py:14-15`; formatting: `:214`; insufficient assertions: `:383-388` and `:436-441`. Assert the exact remote holder list in `r50-detached-below-remote`, and assert `HEAD,refs/heads/main,refs/remotes/origin/main` in `r50-head-is-remote-tip` (including termination of the field, not merely a permissive prefix). Existing local-only `hit_refs` assertions at `:428-434` do not catch suppression of remote holders.
3. **M11 — landed receipt blob provenance is not asserted.** Formatting: `tools/harness/receipt_guard.py:213`; insufficient remote-only/refresh assertions: `:383-388` and `:471-475`. Add `landed_blob` equality to the fixture’s known remote blob in those existing cases. Their HEAD has no receipt, so the current fixtures already distinguish the correct remote blob from the mutant’s `none`; no new production logic is needed.
These are scoped regression-control recommendations, not implementation changes or round admission. This probe leaves the contract unchanged.
## Pristine comparison for the two observed bad-metadata survivors
The same `r50-detached-below-remote` fixture on pristine bytes produced:

```json
{
  "control": "r50-detached-below-remote",
  "exit": 3,
  "expected_exit": 3,
  "passed": true,
  "stderr": "receipt_guard: refusing overwrite path=validation.json committed_sha=9489a228e7ba5f9fec3febe81277204e03cd9ff4 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112 landed_blob=203e7040e2403ebf33b440ca1c851cb8f744893f hit_refs=refs/remotes/origin/main; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]"
}
```
## Hashes and restoration evidence
Every invocation’s source hash was measured immediately before and after running the detector. The detector never changed its own source. `H` abbreviates the full pristine SHA-256 shown above; all mutant hashes below are full SHA-256 values. The following compact records are actual run observations (selected stdout fields, not a second detector).

| Run | Source SHA-256 before = after | Exit | Passed / total | selftest_passed |
|---|---|---:|---:|---|
| P00-pristine | `H` | 0 | 69/69 | true |
| M01-skip-remotes | `56c3e5be82be5bc6aff790d755623de4f315be9ef56371ad8119bf1c977ed93a` | 1 | 56/69 | false |
| R01-restored | `H` | 0 | 69/69 | true |
| M02-skip-heads | `3c00aef3dff59cb337d3f3dd617100f1e2d7e5a6f668a8cfa65262af1030670d` | 1 | 65/69 | false |
| R02-restored | `H` | 0 | 69/69 | true |
| M03-ignore-enumeration-stderr | `cf2d66e1cabad643629cfe873ce1793a787362f6857622a0cb0f2749ca3ca24f` | 1 | 67/69 | false |
| R03-restored | `H` | 0 | 69/69 | true |
| M04-landed-from-heads | `2bb23c1526e4ae84d27a07251167f534a0c3793bd6942de75840142957482362` | 1 | 57/69 | false |
| R04-restored | `H` | 0 | 69/69 | true |
| M05-refresh-before-probes | `aff953988f375fd17662b324b6649f9c1fdc5d0535a0f65875b1a308f1bf711b` | 1 | 65/69 | false |
| R05-restored | `H` | 0 | 69/69 | true |
| M06-allow-noncommit-ref | `51fb660184190ea024e5f0eca0357e7f7b58385cba89c9cfaee5322d1e411bf0` | 1 | 68/69 | false |
| R06-restored | `H` | 0 | 69/69 | true |
| M07-skip-HEAD-tip | `bc884719e85981231c8eb8bb482d6d5e72e95e4e0b51a183e335398872c38a75` | 1 | 62/69 | false |
| R07-restored | `H` | 0 | 69/69 | true |
| M08-include-symbolic-refs | `c13b9b911ba4d49c7f18eb77b60afb40278ac1881c2b01228e489de826b888c5` | 0 | 69/69 | true |
| R08-restored | `H` | 0 | 69/69 | true |
| M09-omit-remotes-from-hit-refs | `a1edb89fbfdba91af6b1da84648c77abb319725fe352960fb711bfb857250a62` | 0 | 69/69 | true |
| R09-restored | `H` | 0 | 69/69 | true |
| M10-landed-sha-from-HEAD | `7fc4659b0be77eacea6bb00194e1e381e43ede5891a422c778003199c8e8391f` | 1 | 65/69 | false |
| R10-restored | `H` | 0 | 69/69 | true |
| M11-landed-blob-from-HEAD | `69c41bb29826714a67ca71ded6d9a0f32930d3009a2a570d84edabb74b0803f5` | 0 | 69/69 | true |
| R11-restored | `H` | 0 | 69/69 | true |
| M12-only-origin-remote | `74665a416ebdb3d4abc2e9eb5b2130f3195691a837352bd52c790882f5fed5c0` | 1 | 68/69 | false |
| R12-restored | `H` | 0 | 69/69 | true |

Each R01–R12 record is an exact-pristine-hash restoration and an independently executed 69/69 pass. Final byte-for-byte comparison used the original `git show` byte buffer, not only its hash:

```json
{
  "command": "cmp -s tools/harness/receipt_guard.py - (stdin = git show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:tools/harness/receipt_guard.py)",
  "exit": 0,
  "stderr": ""
}
```
The private clone, including all temporary fixtures and mutant bytes, was then deleted:

```json
{
  "clone_exists_after": false,
  "command": "rm -rf -- /tmp/kotodama-r50-mutateguard-21-l0w53L",
  "exit": 0,
  "stderr": "",
  "stdout": ""
}
```
## Tooling and write scope
- Read `/home/vgpnk/.omp/agent/RULES.md` before experiments. **Installs/updates: none.** No package-manager transactions were attempted.
- Existing runtimes observed: `git version 2.56.0`; `Python 3.14.8`.
- The only persistent write was this assigned report, `.ufo/waves/round-50/falsify/MutateGuard.md`, under the lane repo. Lane source, index, jj state, refs, filed receipts, fleet files, siblings, MANIFEST, watchdog log, and `.ufo/state` were not modified. Mutant edits, fixture writes, and cleanup were confined to the private `/tmp` clone.
- **Final tally:** 12 single-point mutants; **9 killed, 3 survived, 0 inconclusive**; initial pristine plus all 12 restored runs **69/69**; final exact-byte comparison exit **0**; private clone absent after cleanup.
