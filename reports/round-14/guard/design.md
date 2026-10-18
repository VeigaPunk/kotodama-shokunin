# R14-D01 — receipt guard design

Date: 2026-10-17. Assignment: design only; implementation, runner wiring,
negative-control execution, and the historical-exposure erratum belong to the
other round-14 seats. This file does not certify those deliverables.

Axes: **D / preservation of committed receipts**, **O / predictable runner
operation**, **C / explicit identity, failure modes, and limits**.

## Evidence and defect

Read-only inspection on 2026-10-17 found unconditional filed-output writes at
`reports/round-8/run-validation.py:1485-1487` and
`reports/round-9/run-validation.py:1909-1911`. The historical record
`reports/round-11/recheck/row-131.json:15-28` binds its live-worktree context to
the round-8 receipt rewrite. The routed exposure is recorded at
`reports/round-12/defects/routed.md:10-16`.

The round-12 runner already avoids historical runner invocation, but still
writes its own output at `reports/round-12/run-validation.py:1069-1072`.
A stable stdout digest is not evidence of receipt-file preservation.

Dated identity commands, run from this lane with
`export TMPDIR="$PWD/.scratch"`:

```text
2026-10-17T23:57:29Z
command: git rev-parse --show-toplevel
result: /home/vgpnk/Projects/shokunin/kotodama-shokunin
command: git rev-parse HEAD
result: a7bc9e9ff05a57515c5efaaa7e50116eb30938ff
command: git log -1 --format='%H %cI %s' -- reports/round-8/validation.json
result: 44070b4a6038f54e78d8d5be551e549fe202b0ee 2026-10-17T20:37:36-03:00 round-12: admit C/O/A — recount ledger, defect queue (7 fixed/8 routed), adjacency audit
command: git log -1 --format='%H %cI %s' -- reports/round-9/validation.json
result: 44070b4a6038f54e78d8d5be551e549fe202b0ee 2026-10-17T20:37:36-03:00 round-12: admit C/O/A — recount ledger, defect queue (7 fixed/8 routed), adjacency audit

2026-10-17T23:57:41Z
command: git rev-parse HEAD:reports/round-8/validation.json
result: ca49c2e81c0215abd334bfa4073f907be7fe579e
command: git rev-parse HEAD:reports/round-9/validation.json
result: 303d26872c27f3f393b602a8446b6c90a4a97d98
command: git ls-tree -z --full-tree HEAD -- reports/round-14/validation.json
result: successful command, empty output (not committed at this snapshot)
command: git diff --name-only -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12
result: successful command, empty output (tracked worktree differences only)
```

The hexadecimal `HEAD:path` results above are Git blob object IDs, not commit
IDs or SHA-256 file digests. The diagnostic must identify its commit separately.
These observations describe the inspected checkout, not the declaration's
`baseline_revision`, and do not assert historical byte restoration.

## Import and CLI contract

Recommended public entry point in `tools/harness/receipt_guard.py`:

```python
def guard_receipt(output_path, *, repo_root=None) -> None:
    ...
```

Importing the module has no side effects: no filesystem writes, Git mutations,
argument parsing, subprocess execution, or process exit. Calling the function
returns normally only when the proposed write is permitted. On refusal it emits
one `receipt_guard` diagnostic to stderr and raises `SystemExit(3)`, so a runner
cannot accidentally proceed by ignoring a false return value. It never creates,
opens for writing, truncates, renames, or deletes the receipt itself.

CLI forms use the same function and policy, not a second implementation:

```text
python3 tools/harness/receipt_guard.py PATH [--repo-root ROOT]
python3 tools/harness/receipt_guard.py --selftest
```

Normal probe: exit 0 means permitted, exit 3 means refused or unable to establish
safe status. CLI syntax errors may exit 2. Selftest: exit 0 only when all controls
pass; exit 1 for a failed control. The probe is not a writer. A shell caller must
chain it with `&&`, never `;`, before a writer. The import API is preferred for
round runners because a detached CLI probe leaves a larger check/write gap.

## Decision semantics

- Bind the output to this Git worktree, not the enclosing fleet repository.
  A runner passes its existing absolute `ROOT` as `repo_root`. Resolve relative
  destinations against that root; require the normalized destination to remain
  inside it. An omitted root is discovered from the destination's nearest
  existing directory, not from an unrelated caller working directory. Git's
  reported top-level must agree with the bound root. Linked worktrees are valid;
  do not require `.git` to be a directory.
- Reject symlink destinations and symlinked ancestors, outside-root paths,
  directories, and other non-regular existing destinations. This avoids a
  mismatch between the Git pathname checked and the file actually overwritten.
  `REFRESH_RECEIPTS=1` does not waive these path checks.
- For this contract, committed means a blob at the exact repository-relative
  pathname in the current `HEAD` commit. Capture the full commit object ID,
  inspect that immutable tree, and retain the blob ID for the diagnostic.
  Do not substitute `git ls-files`, the index, existence on disk, mtime, or a
  clean/dirty status result for committed-tree membership.
- Consequently, an untracked receipt and a newly staged receipt absent from
  `HEAD` may be written repeatedly while a round is in flight. A committed
  receipt is protected whether its worktree bytes are identical, dirty, staged
  differently, missing, or staged for deletion. Equal bytes are not an override:
  opening with truncation is still an overwrite attempt.
- A genuinely unborn Git repository has no committed receipt and may permit a
  valid in-root target. A Git executable failure, timeout, non-repository root,
  corrupt/unreadable `HEAD`, or failed tree query is not evidence of absence:
  refuse with exit 3 and `receipt_guard: cannot determine committed status`.
- If the destination is committed, allow only when
  `os.environ.get("REFRESH_RECEIPTS") == "1"`. Unset, empty, `0`, `true`, `yes`,
  `01`, and whitespace-padded values all refuse. No truthiness conversion,
  implicit default, command-line force flag, or runner-local automatic setting.
  The override does not turn Git/path errors into permission to write.
- On the override path, emit a named stderr warning with the same path and
  committed identity. Permission to refresh is not evidence that a historical
  round is authorized for editing; the rounds 8-12 preservation instruction
  remains independently binding.

Use argument-vector subprocess calls, `git -C ROOT`, literal pathspecs, and exact
path matching; no shell interpolation or wildcard membership tests. A suitable
committed-tree lookup is `git --literal-pathspecs -C ROOT ls-tree -z --full-tree
COMMIT -- RELATIVE_PATH`, with command failure distinguished from a successful
empty result. Test unusual path characters and paths with missing parents.

Required refusal diagnostic shape (field labels may be extended, not omitted):

```text
receipt_guard: refusing overwrite path=reports/round-14/validation.json committed_sha=<full HEAD commit object ID> committed_blob=<full blob object ID>; explicit REFRESH_RECEIPTS=1 required
```

`committed_sha` identifies the exact committed snapshot checked, not necessarily
the commit that first filed or last changed this path. Do not truncate it or
report only the blob ID. A failed identity lookup has no known committed SHA;
say status is undetermined rather than inventing one.

## Round-runner integration

For round 14 and successors, call `guard_receipt(ROOT / OUTPUT_REL,
repo_root=ROOT)` at the start of `main()`, before measurements, scratch setup,
child processes, directory creation, or any other writer. Call again immediately
before the final receipt open/write, so a commit made during measurement is
rechecked. Propagate `SystemExit(3)` unchanged; it is preservation refusal, not
an acceptance failure to serialize into `validation.json`.

A successful guard call must not change the existing receipt schema, claim
thresholds, stdout measurements, or the runner's existing acceptance exit codes.
Before first filing, repeated ordinary runs remain possible; after filing, the
same invocation without the override refuses instead of refreshing its receipt.

Do not edit or import-and-run the filed rounds 8-12 validators as an integration
technique. Do not set `REFRESH_RECEIPTS` inside a runner. Historical exposure
requires the separately assigned append-only erratum, plus disposable isolated
rechecks rather than in-place live-root validation. A round-14 parent that would
invoke any legacy writer must instead isolate it or refuse that live invocation;
protecting only its own final output cannot protect a child's filed output.

## Controls required of implementation and integration seats

All controls run in an isolated disposable Git fixture below the lane's
`.scratch`, with `TMPDIR` exported before scratch-writing commands and bytecode
writes disabled. Reuse existing commits in a temporary local clone; no lane
`git commit`/push and no live filed-receipt writes. Capture command, date,
exit status, stderr, and before/after byte digests in the assigned control
receipts. A proposed control below is not a claim of an executed pass.

- **G-new:** target absent from `HEAD`, absent or already present in worktree;
  no override. Guard returns 0, caller can write. Repeating remains permitted.
- **G-staged-new:** index-only new target. Returns 0; tracked is not committed.
- **G-committed:** existing committed target, env unset. Import caller and CLI
  exit 3; stderr names `receipt_guard`, path, full committed SHA, and override.
  Receipt bytes remain unchanged.
- **G-dirty-or-missing:** committed target with dirty/staged bytes or a missing
  worktree file. Exit 3; preserve dirty bytes or absence exactly as found.
- **G-exact-env:** exercise the listed non-`1` values; all exit 3. Literal `1`
  permits the caller's isolated write and emits the committed-identity warning.
  The guard itself writes nothing in either mode.
- **G-boundary:** out-of-root, symlink target/ancestor, non-regular target, and
  invalid repository all refuse, including with the override set. Use only
  fixture-owned boundary paths; do not write a planted path outside the lane.
- **G-git-error:** controlled Git failure or timeout refuses rather than acting
  like an uncommitted target. Also test a genuine unborn fixture separately.
- **G-import-and-root:** importing alone is inert; the API and CLI agree;
  explicit root works from another working directory; linked-worktree discovery
  is not confused by a `.git` file. Literal pathname controls cannot be bypassed
  with Git pathspec metacharacters.
- **G-runner-before-effects:** execute a miniature wired runner against a
  committed fixture receipt. Without override: exit 3, unchanged receipt, and
  no measurement sentinel/child side effect. With literal `1`: sentinel and
  intended fixture receipt write occur with the runner's normal exit semantics.
- **G-real-integration:** inspect and exercise the actual round-14 runner in a
  disposable checkout. Verify it calls the guard before work and before output,
  cannot swallow refusal, and cannot run an unguarded historical writer on the
  live tree. Demonstrate the ordinary pre-filing path separately from the
  committed-target refusal control; retain actual command/date evidence.

## Limits and handoff

This is cooperative writer protection, not an operating-system sandbox or a
Git hook. Importing without calling the guard protects nothing; old runners,
direct `Path.write_text`, malicious callers, and explicit overrides can still
write. The guard does not repair earlier clobbers or certify admission.

The commit predicate is the current checkout's `HEAD` tree, not all branches,
reflogs, or deleted historical pathnames. A path removed by a later committed
deletion is not protected by this snapshot predicate; deletion is not an
approved receipt-refresh workflow. Commit identity and blob identity must stay
separate in any later broader-history implementation.

A second check narrows but does not eliminate a concurrent commit or filesystem
replacement between check and write. Do not claim race-proof locking. Serialize
receipt publication and filing operationally; evaluate stronger transactional
writing separately if concurrency becomes an observed defect.

R14-D01 acceptance is this design file only. Runtime claims remain pending the
implementation's `python3 tools/harness/receipt_guard.py --selftest`, independent
negative controls, real round-14 wiring controls, and integrated regression
receipts. Parent integration records this fragment in append-only `LOG.md`;
this worker does not edit shared bookkeeping or earlier-round artifacts.
