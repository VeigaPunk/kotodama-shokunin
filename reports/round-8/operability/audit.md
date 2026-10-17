# R8-X03 — operability audit (O axis): harness fix, negative controls, battery rerun

- **Shard:** R8-X03 (scribe, O auditor). **Round:** 8, loop 1 of 3, build round 1 of 4.
- **Date:** 2026-10-17; all commands below ran 2026-10-17 between 20:13Z and 20:32Z (UTC clock reads
  in the receipts). **Lane repo:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **Revision binding:** HEAD `cf338a713060f274269cdacb18cdc0085bb06aeb` (declared baseline
  `e7ca0faeb6680fa9891b907be628d9db578c28f4`). The O-shard repairs are **uncommitted worktree
  changes**; the pre-fix bytes therefore live at HEAD and are used as the reversal reference
  (`git show HEAD:<path>`). All five extracted pre-fix gate blobs match the review-26 §0 pins
  (`prefix_extract` in the raw receipt: `fb05c644…`, `8c5afb0a…`, `26d246e9…`, `29a9361c…`,
  `63ee4ec6…`).
- **Role limits:** this audit verifies receipts and executable behaviour; it decides no admission,
  promotion or closure, certifies no canon, and writes no repository file other than this report.

## 0. Audited artifacts (sha256 at audit time)

| artifact | sha256 |
|---|---|
| `tools/harness/r8_checks.py` | `0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe` |
| `tools/check-gate-battery.py` | `077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67` |
| `tools/check-craft-exercise.py` | `b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5` |
| `tools/gates/phonology-sanity-gate.py` | `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `tools/gates/myth-consistency-gate.py` | `5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08` |
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` |
| `tools/gates/lexicon-coverage-audit.py` | `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287` |

Command: `sha256sum tools/harness/r8_checks.py tools/gates/*.py` (2026-10-17T20:32:18Z).

## 1. Method and environment

- Driver: `/home/vgpnk/.cache/x03-scratch/tools/verify-final.py` (auditor-written, stdlib only).
  It copies the tree out of the repo, runs the harness/battery/craft selftests, runs every control
  in live mode, runs each control's own documented fail-before mode, and — where the target file is
  tracked — restores its pre-fix bytes from `git show HEAD:<path>` into a separate copy and re-runs
  the control there. The lane repo is never written by the driver or the controls.
- Independent probes (auditor-written, not the harness's own selftest):
  `harness-probe.py` (applies the mutations itself through the module API) and
  `review26-probe.py` (replays review 26's payloads through the real gate CLIs).
- **Environment deviation (documented):** `/tmp` exhausted its inode table during this window
  (`df -i /tmp` → `1048576 1048576 0 100%`, 2026-10-17T20:28Z; `ENOSPC` on any write). All copies
  therefore live in the disk-backed out-of-repo scratch `~/.cache/x03-scratch/`. The
  reversed-fix checks still ran **in a copy outside the repository**, just not literally under
  `/tmp`; the `df -i` receipt above is the reason.
- Concurrency: other O-shards were still writing during the audit (observed: `neg-06` bytes changed
  mid-run at 20:31, `neg-13` mid-write at 20:28). Final verification ran 20:29–20:32 with a
  before/after hash sweep over `tools/gates tools/harness reports/round-8/operability` (27 files);
  after the `neg-06` re-run the sweep is stable. Mid-flight observations are recorded in §5.

## 2. Verification results

### V1 — harness selftest green (pass)

```
$ cd <copy> && python3 tools/harness/r8_checks.py --selftest
exit=0  stdout sha256=25bf2315e6c2f3403a3fc9028720225284b1848f1a91e62ae3808543b0f5ce58
receipt: {"controls_passed": 12, "controls_total": 12, "defect": "reports/round-7/validation.json F: wrong rejection for duplicate-parent-receipt-does-not-inflate: parent check identity collision"}
$ python3 tools/harness/r8_checks.py --measure        # exit=0
{"parent_benign_duplicate_receipts": 0, "parent_checks_raw": 2, "parent_checks_unique": 2,
 "parent_distinct_passage_keys": 2, "parent_distinct_refetch_urls": 2}
```

The receipt's `input_sha256` covers reconciliation/spotchecks/targets/baseline and ledgers 08–12;
the harness never writes (module has no write call).

### V2 — corrected semantics, independently re-derived (pass)

`harness-probe.py` imports both `tools/harness/r8_checks.py` and the filed
`reports/round-7/run-validation.py` (read-only) and applies the mutations itself:

| mutation | round-7 runner | corrected harness |
|---|---|---|
| real round-7 inputs | accepted (2 distinct keys) | accepted (2 distinct keys, 0 benign duplicates) |
| filed control mutation (`clone` re-ided `PX99`, twice) | rejected **"parent check identity collision"** (the filed defect) | rejected **"fewer than two distinct parent passage receipts: 1"** |
| benign duplicate appended (same id, identical payload) | rejected **"parent check identity collision"** (wrong) | **accepted**, `benign_duplicate_receipts=1`, still 2 distinct keys |
| genuine collision (same id, divergent excerpt) | — | rejected "parent check identity collision: P01" |
| duplicates under fresh ids (`PX98`/`PX99`) | — | rejected "fewer than two distinct parent passage receipts: 1" |

So: benign duplicate accepted and non-inflating, genuine collision still rejected, and the filed
control shape now yields the distinctness diagnostic it declares.

### V3 — harness fix reversed in a copy (pass, fail detected)

On a copy where the grouping/dedupe block is replaced by the round-7 rule
(`require(len(ids) == len(set(ids)), "parent check identity collision")`), the harness selftest
**exits 1** (the benign-duplicate controls fail; the run ends in a `TypeError` inside the control
runner — see finding X03-F2). Detection is real: the reversed tree is not accepted.

### V4 — battery/craft rerun vs `battery-rerun.json` (pass, byte-identical)

```
python3 tools/check-gate-battery.py --selftest   -> exit 0, stdout sha256 03f14e3d2d16fd7b0203631b8031a84e216fed1568e55ba257ad1596e96569cf
python3 tools/check-craft-exercise.py --selftest -> exit 0, stdout sha256 77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32
```

Both shas and both exit codes match `summary_by_command` in
`reports/round-8/operability/battery-rerun.json` exactly (`battery_match: true`,
`craft_match: true`). Note the receipt's own caveat: it is a **pre-repair** receipt at `cf338a7`;
it still matches because the two tool files are byte-identical at `cf338a7` and in the delivered
tree (`tools_under_test.sha256_worktree` in the receipt equals the audit-time hashes in §0).
Result lines: `SELFTEST OK 10/10 controls behaved as expected` and
`SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18 cases passed`.

### V5 — negative controls: live pass, fail-before demonstrable (pass)

13 control scripts (10 shards O04–O13) plus one evidence probe. Every control exits 0 on the live
tree; every control detects its pre-fix pattern when the fix is reversed. "Tree rev" = control run
from an out-of-repo copy with the target file(s) restored from `git show HEAD:<path>`.

| control | defect (review 26 / 29) | live | own fail-before mode | tree rev |
|---|---|---|---|---|
| `neg-04/neg-04-control.py` | D1 unterminated flow | 0 | (`--gate` pre-fix copy) | **1** |
| `neg-05/neg-05-control.py` | D2 phonology duplicate keys | 0 | (`--gate` pre-fix copy) | **1** |
| `neg-06/neg-06-control.py` | D2 costume+lexicon+myth duplicate keys | 0 | `--prefix-dir` → 1, `--pre-fix-from-git HEAD` → 1 | **1** (manual re-run, §5-X03-F3) |
| `neg-07/neg-07-control.py` | D2 naming duplicate keys | 0 | (`--gate` pre-fix copy) | **1** |
| `neg-07/neg-07-d3-control.py` | D3 anchors/aliases/tags | 0 | `--prefix-dir` → 1 | **1** |
| `neg-08/neg-08-control.py` | D4 boolean/number coercion | 0 | `--pre-fix-from-git HEAD` → 1 | **1** |
| `neg-08/neg-08-d4-control.py` | D4 (same register, second leg) | 0 | `--pre-fix-from-git HEAD` → 1 | **1** |
| `neg-09/neg-09-control.py` | D5 tab/multi-document | 0 | `--baseline-rev HEAD` → 1 | **1** |
| `neg-09/probe-prefix.py` | evidence for D5 (not a pass/fail control) | 0 | — | n/a |
| `neg-10/neg-10-control.py` | D6 deep nesting | 0 (13/13) | `--rev HEAD` → 1 | **1** |
| `neg-11/neg-11-control.py` | D7 non-UTF-8 | 0 | internal (fail-before leg runs inside; see X03-F4) | **1** |
| `neg-12/neg-12-control.py` | D8 packet-controlled regex | 0 | `--pre-fix-from-git HEAD` → 1 | **1** |
| `neg-13/neg-13-control.py` | D9 `str.format` template | 0 | `--from-git HEAD` → 1 | **1** |
| `neg-13/extra-index10-fixture-pin-control.py` | F1 fixture pin semantics (index 10) | 0 | `--from-git HEAD` → 1 | **1** |

Reversal evidence is the controls' own diagnostics, e.g. `NEG-04 FAILURE: … PRE-FIX PATTERN
OBSERVED: rc=1 …` and `NEG-13 FAILURE: … PRE-FIX PATTERN OBSERVED: tampered fixtures/… silently
erased (exit 0, original bytes restored)`. For `neg-06` the restored pre-fix bytes carry the
review-26 pins (`29a9361c…`, `63ee4ec6…`, `26d246e9…`) and the reversed run exits 1 with
`PRE-FIX PATTERN OBSERVED: rc=0, no duplicate-key diagnostic`.

**Requirement check:** ≥2 controls genuinely fail when their fix is reversed — satisfied by all 13
(12 via the driver's tree reversal, `neg-06` via the manual re-run). ≥6 controls exist — 13.

### V6 — the controls write nothing into the lane repo (pass)

`git status --porcelain` before and after the full control battery is identical
(`repo_status_changed_by_control_runs: false`); every control's own isolation statement (payloads
in temp dirs, gates as subprocesses) matches the observed behaviour.

## 3. Findings

- **X03-F1 — resolved during the audit (record, not a final defect).** At 20:24Z `neg-10` failed
  on the live tree (12/13): `lexicon-coverage-audit.py` crashed with `RecursionError` (rc=1,
  traceback, no finding) on the balanced deep-nesting payload — at **both** HEAD and live bytes,
  so its docstring premise "lexicon already conformed … untouched reference" did not hold then.
  By 20:29Z the lexicon shard's repair had landed and the same control passes 13/13
  (`NEG-10 lexicon deep-bracket-nesting rc=2 PASS`). Recorded because it is the one instance in
  this window where the delivered tree was red and a rerun changed the verdict.
- **X03-F2 — open, minor (harness selftest runner).** In `tools/harness/r8_checks.py`, `observe()`
  catches `ValueError` and evaluates `expected_substring in message`; when a control that is
  *expected to be accepted* raises instead (`expected_substring=None`), this raises
  `TypeError: 'in <string>' requires string as left operand, not NoneType` and the selftest ends
  in a traceback. Reversal is still detected (exit 1), but the diagnostic is a crash rather than a
  named failed control. Fix is a two-line guard in `observe()`.
- **X03-F3 — open, minor (audit-protocol note).** Control files were still being written while
  verification ran: `neg-06` changed bytes mid-run (20:31Z, hash `f63763c6…` → `61e71dda…`) and a
  mid-write read of `neg-13` at 20:28Z produced a spurious `plain-template-mismatch-fails` FAIL
  (its predicate is satisfied by the stable bytes — re-derived by direct invocation). Consequence
  for the parent: verify the control tree is quiescent before trusting any single control verdict;
  this audit's final numbers come from the 20:29–20:32 stable sweep plus the `neg-06` re-run.
- **X03-F4 — informational.** `neg-11`'s fail-before leg is *internal*: it materialises the
  pre-fix gates itself (`--rev`, default `e7ca0fa`) and asserts the pre-fix crash **and** the
  post-fix exit 2 in one invocation, so exit 0 is its pass. Its `--rev HEAD` run in this audit
  also exits 0 and its printed C2/C3 checks observe the pre-fix `UnicodeDecodeError`.
- **X03-F5 — informational.** `reports/round-8/operability/neg-controls/neg-09/probe-prefix.py` is
  an evidence probe (prints pre-fix behaviour), not a pass/fail control; it is excluded from the
  13-control count. `battery-rerun.json` is a pre-repair receipt by its own declaration and still
  matches byte-for-byte (V4).

## 4. Limits

- Point-in-time: every verdict binds the hashes in §0; the tree was moving during the window and
  the parent should re-run the acceptance command after quiescence.
- This audit executes the controls; it does not re-derive their payloads' source-criticality, and
  it certifies no source or canon claim (F receipts are other shards' scope).
- The `TypeError` in X03-F2 was observed only on the reversed copy; the live path does not reach it.
- `df -i /tmp` exhaustion means the literal `/tmp`-copy wording of the assignment is satisfied by
  an out-of-repo disk-backed copy instead; the `df -i` receipt is the documented reason.

## 5. Receipts (raw)

- Driver raw JSON: `~/.cache/x03-scratch/final-audit-raw.json` (per-control live/fail-before/tree
  runs, artifact hashes, repo status before/after).
- `neg-06` re-run: `~/.cache/x03-scratch/neg06-live.txt` (exit 0, 17/17),
  `~/.cache/x03-scratch/neg06-rev.txt` (exit 1, PRE-FIX PATTERN OBSERVED).
- `--pre-fix-from-git HEAD` runs (auditor-initiated, exit 1 each):
  `~/.cache/x03-scratch/neg-06-prefix.txt`, `neg-08-control-prefix.txt`,
  `neg-08-d4-control-prefix.txt`, `neg-12-control-prefix.txt`.
- Probes: `~/.cache/x03-scratch/tools/harness-probe.py`, `…/review26-probe.py`
  (both exit 0; `review26-probe` output is the fixed-tree replay of review 26's payloads).
- Hash sweeps: `~/.cache/x03-scratch/hashes-before.txt`, `hashes-after.txt`, `hash-diff.txt`.
- Environment receipt: `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp` (2026-10-17T20:28Z).
