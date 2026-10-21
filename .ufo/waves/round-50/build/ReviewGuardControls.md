# ReviewGuardControls: Claim O control enumeration (round 50, attempt 1)

Seat: ReviewGuardControls (reviewer, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base: `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Scope: enumerate the existing `tools/harness/receipt_guard.py --selftest` controls, their order, and a sha256, so the integrator can prove all 45 survive. Advice for the author lane, not an admission.

## Verdict

- Base selftest: **45 controls, 45 passed**, exit 0, `selftest_passed: true`, no duplicate names, identical order across two runs. Matches the O premise "all 45".
- Ordered-list sha256 (serialization in section 1): **`5955a0545d479002de144588e44a88ccd745f4a8d548a313b2296189269a4237`** (1221 bytes, 45 LF-terminated lines).
- Lane working file equals base blob: `tools/harness/receipt_guard.py`, 373 lines, sha256 `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` in both (`git show 4ad2683:…` and `sha256sum` of the lane file).
- One design hazard for O that no existing control covers (F1), and one test-coupling risk (F2).

## 1. Method (lane not mutated)

- `git clone -q <lane> /tmp/rgc-r50-O-8b72vgv4/tree`, then `git -C <clone> checkout -q 4ad2683…`; `rev-parse HEAD` = `4ad2683…`.
- `python3 -B tools/harness/receipt_guard.py --selftest` run inside the clone (the selftest writes `.scratch/` into its repo root). rc 0.
- Names read from `controls[].control` in JSON array order. `sort_keys=True` sorts dict keys, not the array, so array order is the append order.
- Hash serialization: `"\n".join(names) + "\n"`, UTF-8. Cross-checked with `sha256sum` on the written file (same digest).
- Lane touched only by read-only commands: `git cat-file -t`, `git show <base>:path | sha256sum`, `sha256sum`, `read`/`grep`. No git add/commit/stash/checkout/reset, no jj.
- Reproduce (inside a temp clone, never the lane):
  `python3 -B tools/harness/receipt_guard.py --selftest | python3 -c 'import json,sys; print("\n".join(c["control"] for c in json.load(sys.stdin)["controls"]))' | sha256sum`

## 2. Ordered control list at base (45)

Source: `tools/harness/receipt_guard.py` at 4ad2683. "Expected exit" and "diagnostic" come from the selftest JSON (`expected_exit`, `stderr`). "fixture" rows are `controls.append` plumbing checks with no exit field. Runner rows use `passed` expressions (L316-340).

| # | control | expected exit | stderr diagnostic | base source line(s) |
|---|---|---|---|---|
| 1 | `committed-refused` | 3 | RECEIPT-GUARD-COMMITTED | 240 |
| 2 | `committed-refresh-allowed` | 0 | RECEIPT-GUARD-REFRESH | 241 |
| 3 | `nonexact-refresh-''-refused` | 3 | RECEIPT-GUARD-COMMITTED | 242-244 |
| 4 | `nonexact-refresh-'0'-refused` | 3 | RECEIPT-GUARD-COMMITTED | 242-244 |
| 5 | `nonexact-refresh-'true'-refused` | 3 | RECEIPT-GUARD-COMMITTED | 242-244 |
| 6 | `nonexact-refresh-'yes'-refused` | 3 | RECEIPT-GUARD-COMMITTED | 242-244 |
| 7 | `nonexact-refresh-'01'-refused` | 3 | RECEIPT-GUARD-COMMITTED | 242-244 |
| 8 | `nonexact-refresh-' 1'-refused` | 3 | RECEIPT-GUARD-COMMITTED | 242-244 |
| 9 | `nonexact-refresh-'1 '-refused` | 3 | RECEIPT-GUARD-COMMITTED | 242-244 |
| 10 | `dirty-committed-refused` | 3 | RECEIPT-GUARD-COMMITTED | 246 |
| 11 | `fixture-stage-dirty` | fixture | - | 247-248 |
| 12 | `staged-dirty-committed-refused` | 3 | RECEIPT-GUARD-COMMITTED | 249 |
| 13 | `deleted-committed-refused` | 3 | RECEIPT-GUARD-COMMITTED | 251 |
| 14 | `fixture-stage-deletion` | fixture | - | 252-253 |
| 15 | `staged-deletion-refused` | 3 | RECEIPT-GUARD-COMMITTED | 254 |
| 16 | `new-receipt-missing-parents-allowed` | 0 | - | 256 |
| 17 | `untracked-receipt-allowed` | 0 | - | 259 |
| 18 | `fixture-stage-new` | fixture | - | 260-261 |
| 19 | `staged-new-receipt-allowed` | 0 | - | 262 |
| 20 | `relative-receipt-refused` | 3 | RECEIPT-GUARD-COMMITTED | 263 |
| 21 | `destination-root-discovery` | 3 | RECEIPT-GUARD-COMMITTED | 264 |
| 22 | `literal-pathspec-no-wildcard-match` | 0 | - | 265 |
| 23 | `literal-pathspec-no-magic` | 0 | - | 266 |
| 24 | `git-environment-cannot-rebind-root` | 3 | RECEIPT-GUARD-COMMITTED | 267-268 |
| 25 | `outside-repo-refused-None` | 3 | RECEIPT-GUARD-PATH | 269-271 (loop L269) |
| 26 | `directory-refused-None` | 3 | RECEIPT-GUARD-PATH | 272-273 |
| 27 | `symlink-alias-refused-None` | 3 | RECEIPT-GUARD-PATH | 276-277 |
| 28 | `symlink-ancestor-refused-None` | 3 | RECEIPT-GUARD-PATH | 280-281 |
| 29 | `symlink-dotdot-refused-None` | 3 | RECEIPT-GUARD-PATH | 282-283 |
| 30 | `hardlink-alias-refused-None` | 3 | RECEIPT-GUARD-PATH | 286-287 |
| 31 | `outside-repo-refused-1` | 3 | RECEIPT-GUARD-PATH | 269-271 (loop L269) |
| 32 | `directory-refused-1` | 3 | RECEIPT-GUARD-PATH | 272-273 |
| 33 | `symlink-alias-refused-1` | 3 | RECEIPT-GUARD-PATH | 276-277 |
| 34 | `symlink-ancestor-refused-1` | 3 | RECEIPT-GUARD-PATH | 280-281 |
| 35 | `symlink-dotdot-refused-1` | 3 | RECEIPT-GUARD-PATH | 282-283 |
| 36 | `hardlink-alias-refused-1` | 3 | RECEIPT-GUARD-PATH | 286-287 |
| 37 | `unborn-receipt-allowed` | 0 | - | 291 |
| 38 | `explicit-root-cannot-discover-parent-repo` | 3 | RECEIPT-GUARD-GIT | 294-295 |
| 39 | `missing-git-fails-closed` | 3 | RECEIPT-GUARD-GIT | 296-297 |
| 40 | `fixture-linked-worktree` | fixture | - | 299-300 |
| 41 | `linked-worktree-refused` | 3 | RECEIPT-GUARD-COMMITTED | 301-302 |
| 42 | `runner-refusal-before-callback` | 3 | - | 316-318, 325 |
| 43 | `runner-refresh-preserves-exit` | 7 | - | 316-318, 325 |
| 44 | `runner-rechecks-before-publisher` | 3 | - | 338-340 |
| 45 | `corrupt-head-fails-closed` | 3 | RECEIPT-GUARD-GIT | 342 |

Counts by diagnostic: COMMITTED 16, REFRESH 1, PATH 12, GIT 3, no diagnostic 13 (6 allow-exit controls #16, 17, 19, 22, 23, 37; 4 fixture rows #11, 14, 18, 40; 3 runner rows #42-44). Total 45.

## 3. Survival check for the integrator

Save outside the lane (for example `/tmp/verify_controls.py`):

```python
import hashlib, json, pathlib, sys
rep = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
base = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").split("\n")[:-1]
landed = [c["control"] for c in rep["controls"]]
base_set = set(base)
missing = [n for n in base if n not in set(landed)]
failing = sorted({c["control"] for c in rep["controls"] if c["control"] in base_set and c["passed"] is not True})
it = iter(landed)
subsequence = all(any(n == m for m in it) for n in base)
prefix = landed[:len(base)] == base
prefix_sha = hashlib.sha256(("\n".join(landed[:len(base)]) + "\n").encode("utf-8")).hexdigest()
ok = not missing and not failing and subsequence
print(f"base={len(base)} landed={len(landed)} missing={missing} failing={failing}")
print(f"order_preserving_subsequence={subsequence} exact_prefix={prefix} prefix_sha256={prefix_sha}")
print("VERDICT", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
```

Use: write the 45 names of section 2 (LF-terminated) to `base-names.txt`; run the selftest in a temp copy of the landed tree to `landed.json`; then `python3 /tmp/verify_controls.py landed.json base-names.txt`. Required: `VERDICT PASS`, exit 0, `selftest_passed: true`, and `controls_total` = 45 + (new controls).

Acceptance rule: every base name present, in the same relative order, passing. The exact-prefix hash `5955a054…` holds only when new controls are appended after #45.

Calibration of the checker (temp copies; each mutation applied to a copy, not the lane):

| case | mutation | selftest rc | verifier | evidence |
|---|---|---|---|---|
| base | none | 0 | PASS | exact_prefix=True, prefix sha `5955a054…` |
| neg-a | drop `"1 "` from loop tuple (L242) | 0 | FAIL | missing `nonexact-refresh-'1 '-refused` (landed 44) |
| neg-b | `corrupt-head-fails-closed` expected exit 3→4 (L342) | 1 | FAIL | failing `corrupt-head-fails-closed` |
| ext | new `cli("synthetic-extra-control", …)` inserted before L341 | 0 | PASS | subsequence=True, exact_prefix=False (landed 46) |

So the checker catches removal and pass-to-fail, and tolerates additions, but a mid-list insertion breaks the exact-prefix hash. Recommend appending new controls after #45.

## 4. Findings (severity order)

### F1 (HIGH for O's design; no base defect): a broken ref looks like a missing ref

Evidence (git 2.56.0, temp repos):
- `git show-ref --verify --quiet refs/remotes/origin/nope` (missing) → rc 1 silent; `…refs/remotes/origin/main` and `refs/heads/main` when broken → rc 1 silent. Indistinguishable.
- `git rev-parse --verify --quiet <ref>^{commit}`: missing → rc 1 silent; broken → rc 1 plus stderr `warning: ignoring broken ref …`. Stderr-text dependent.
- `git for-each-ref <ref>`: missing → rc 0, empty; broken → rc 0, empty stdout plus the same warning.
- `git show-ref <ref>` (no `--verify`): missing → rc 1; broken → **rc 128** (`fatal: git show-ref: bad ref …`); healthy → rc 0 with `<sha> <ref>`. This separates all three states. show-ref matches by trailing path components, so the executor must compare the exact refname in the output.
- Base control #45 fails closed through the fall-through `raise` at L79: with HEAD → `refs/heads/control` corrupt, `rev-parse` rc 1 and `symbolic-ref --quiet HEAD` rc 128 (`fatal: No such ref: HEAD`), so the `show-ref` branch (L76-78) is never reached. Replayed on the fixture: `_head_commit` raised RECEIPT-GUARD-GIT. The fail-closed result rests on `symbolic-ref` behaviour, not on an explicit check of the corrupt ref.

Risk: if O implements the ExecGuard assignment's "missing refs tolerated" as `returncode == 1` on `refs/heads/<branch>` or `refs/remotes/origin/<branch>`, a corrupt one is silently skipped and a committed receipt can be overwritten. No existing control corrupts a non-HEAD ref.

Advice: treat rc 1 as missing only from `git show-ref <exact-ref>` (no `--verify`) and compare the exact name; any other nonzero rc → `RECEIPT-GUARD-GIT`. Add controls: corrupt `refs/heads/main` → GIT; corrupt `refs/remotes/origin/main` → GIT; healthy-but-absent remote → allowed. Append them after #45.

### F2 (MEDIUM, test coupling): 17 controls pin the identity string

`tools/harness/receipt_guard.py` L234-235 require `committed_sha=<HEAD>` and `committed_blob=<blob>` in stderr for every refusal or refresh whose stderr carries RECEIPT-GUARD-COMMITTED or RECEIPT-GUARD-REFRESH. Affected: #1–10, 12, 13, 15, 20, 21, 24, 41. The current identity is built at L142-143 with `committed_sha={head}` (HEAD). Any O change that renames that field, or reports a landed sha in that slot when it differs from HEAD, breaks all 17 at once. Keep `committed_sha=<HEAD>` for HEAD-committed fixtures and add landed fields additively (for example `landed_sha=`).

### F3 (MEDIUM): fail-closed pins a patch must keep

- #38, #39, #45 pin RECEIPT-GUARD-GIT. #39 removes git from PATH; #45 corrupts the HEAD branch.
- #24 pins GIT_* scrubbing performed by `_git` (L48-58).
- #37 pins unborn HEAD → allowed (the `None` path, L77-78).
- #40, #41 pin linked-worktree refusal.
- Every new git call must go through `_git` (literal pathspecs, GIT_* scrubbing, GIT diagnostic on failure). A direct `subprocess` call would bypass #24 and #39 semantics.

### F4 (INFO): base is clean

- 45/45 pass, rc 0, no duplicate names, deterministic across two runs.
- `.scratch/` is ignored by `.gitignore:6`, so in-lane runs do not dirty status. The selftest still writes into the repo root, so run it only in temp copies.
- The output JSON carries a `date` field, so hash the names only, never the whole output.
- `refs/remotes/origin` has 0 hits in base `receipt_guard.py` (`git show 4ad2683:… | grep -c refs/remotes/origin` = 0), matching claims.json before-check `guard-head-only` (expect absent).

### F5 (coverage gap for O's new behaviour)

None of #1–45 covers: committed on `refs/heads/<branch>` while HEAD is anchored below it; committed on `refs/remotes/origin/<branch>`; detached HEAD with a newer branch tip; corrupt non-HEAD refs (F1). Each needs a new control, appended after #45.

## 5. Unrun checks and limits

- Not run: lane `check-readme-revisions.py --selftest` and the jj probe (other seats); ExecGuard's in-flight work clone (`.ufo/waves/round-50/work/ExecGuard`; `patches/` empty). Per the verification rule, mid-flight checks belong to the integrator after landing.
- The probes (F1) were run on git 2.56.0 only; the exit-code behaviour may vary across git versions. The executor should re-run them on the lane's git.
- No `lsp` device is exposed to this seat. Line mapping is literal grep of the base source (fallback, not semantic proof).
- Did not inspect a landed O patch; F1/F2/F3 are conditions on any patch, not findings about one.

## 6. Tooling and environment

- No installs or updates. Tools used (pre-existing): git 2.56.0, Python 3.14.8, coreutils `sha256sum` 0.8.0.
- Temporary artifacts outside the lane: `/tmp/rgc-r50-O-8b72vgv4` (base clone, JSON outputs, base-names file, verifier, mutated copies) and `/tmp/rgc-ref-probe-*`, `/tmp/rgc-c45-*`, `/tmp/rgc-probe2-*`, `/tmp/rgc-probe3-*`. Removed after this report was written.
