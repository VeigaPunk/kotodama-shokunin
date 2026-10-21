# ExecGuard — claim O, R1+R2 (receipt_guard jj colocation), round 50 — final

Seat: ChousaR27R2.ExecGuard-4. Base 4ad26836552462d28a946ca3b067cab0b5ce3532. All edits in the private clone
`.ufo/waves/round-50/work/ExecGuard`. Lane production files, lane git and jj state: untouched.
Governing spec: `.ufo/waves/round-50/build/ReviewGuardSemantics.md` (§5.2 algorithm, §7.3 fixtures, §7.5 mutants).

## Result

- File changed: `tools/harness/receipt_guard.py` (only).
- Patch: `.ufo/waves/round-50/patches/ExecGuard.patch`, 24377 bytes, sha256 `ea8b7ea07c6a653b4851b470e481bba486db0c21b26585800f37d2208fd32b40`.
- Selftest (clone, `python3 -B tools/harness/receipt_guard.py --selftest`): exit 0, `controls_passed` 69 / `controls_total` 69, `selftest_passed` true.
- Prior 45 control names and order: identical to base. sha256 of the 45 names joined by LF is `d7a05f268c90e1d2eeb994678bef000d09dd9ccb69d5d39b9ee58f2bf269bf37` (ReviewGuardSemantics §7.2).
- Applied-tree check: fresh clone at base, `git apply --check` OK, applied file byte-identical to the clone file, selftest 69/69.

## Behavior (receipt_guard.py, patched tree)

- `_head_state` (line 76): `symbolic-ref --quiet HEAD`. rc 0 gives the attached branch; rc 1 with empty stderr gives detached; anything else is GIT. Then `rev-parse --verify HEAD^{commit}`: rc 0 gives the HEAD oid; rc 1 with empty stderr on an attached branch gives unborn; anything else is GIT.
- `_enumerate_refs` (line 96): one `for-each-ref --format=%(refname)%00%(objectname)%00%(objecttype)%00%(symref)` over `refs/heads` and `refs/remotes`. Non-zero rc, any stderr, a non-UTF-8 name, an OID that does not match, or objecttype other than `commit` are all GIT. Symrefs are skipped as duplicates but still count toward the unborn check.
- `_check_receipt` tail (lines 194-220): if HEAD is unborn and its branch is listed, GIT. Tips are HEAD plus sorted refs. `ls-tree` runs once per distinct commit, and hits keep every tip name. No hits: allow. Otherwise the identity is `path= committed_sha=<HEAD or none> committed_blob=<HEAD blob or none> landed_ref=<first refs/remotes/* hit, else none> landed_sha= landed_blob= hit_refs=<comma list, HEAD first>`.
- REFRESH_RECEIPTS=1 is consulted after every probe. It waives only the COMMITTED refusal and prints the same identity with `[RECEIPT-GUARD-REFRESH]`.
- Path checks, bind, and env scrub are unchanged.

## Deviations to confirm (L1 decision)

1. `committed_sha` is HEAD's commit (or `none`), per ReviewGuardSemantics §5.5 and §7.3. My earlier "commit where found" reading conflicts with §7.3 `r50-detached-below-remote`, which expects `committed_sha=C1` while origin holds C2. The holder is reported in `landed_ref` and `hit_refs`. I dropped `head_sha=` and `holding_sha=`.
2. `landed_sha` comes from the first `refs/remotes/*` hit in sorted refname order, not an origin/<branch> preference. This follows the addendum's "landed from refs/remotes/* only".
3. The `runner-rechecks-before-publisher` control keeps its name, order, and expectation. Its fixture changed: `refs/heads/control` is removed before the first check, and the callback recreates HEAD and the ref. It now also asserts `RUNNER-CALLED` on stdout, so the first check is shown to allow.

## Measured git 2.56.0 facts that drove the design

| probe | absent | valid | corrupt loose ref | dangling (missing object) | tree-typed |
|---|---|---|---|---|---|
| `show-ref --verify --quiet R` | rc 1 | rc 0 | rc 1, silent (**collapses; not used**) | rc 128 | — |
| `show-ref R` (no verify) | rc 1 | rc 0 | rc 128 | rc 128 | — |
| `rev-parse --verify --quiet R` | rc 1 | rc 0 | rc 1 + "ignoring broken ref" | rc 0 (no object check) | — |
| `for-each-ref ... %(objecttype)` | omitted, rc 0 | listed | omitted, rc 0 + warning | rc 128 "missing object" | rc 0, `tree` |

- `rev-parse HEAD^{commit}`: attached-unborn gives rc 1 silent. A corrupt HEAD target also gives rc 1 silent, so `symbolic-ref` must run first; it gives rc 128 "No such ref: HEAD" in that case.
- `symbolic-ref --quiet HEAD`: detached gives rc 1 silent.
- A dangling symref is omitted from `for-each-ref` with rc 0 and no warning. It is skipped, as §5.2 requires.
- Unrelated corrupt refs do not disturb a direct `rev-parse` or a `for-each-ref` restricted to other names. The enumeration covers every `refs/heads` and `refs/remotes` ref, so an unrelated corrupt ref there does fail closed.

Why not `show-ref`: `--verify --quiet` collapses corruption into absence (exit 1), which is the FO-05 trap. Plain `show-ref` cannot enumerate every tip.

## Controls

- Appended 24 controls: 21 from ReviewGuardSemantics §7.3 (`r50-*`, including the predicted `r50-nonutf8-refname`, now executed) plus `attached-head-holds-refused`, `unborn-local-branch-refused`, and `other-local-branch-refused`.
- Every new control asserts the receipt bytes and a sha256 of the `.git` tree are unchanged, per §7.3 invariants.
- Verified stderr of a few controls: `r50-corrupt-remote` names `refs/remotes/origin/main` (git warning). `r50-missing-object-ref` gives rc 128 "missing object …ghost". `r50-tree-typed-ref` gives "does not resolve to a commit (tree)". `r50-corrupt-branch` gives "reading the symbolic HEAD failed (exit 128)". `r50-nonutf8-refname` gives "ref name is not UTF-8: b'refs/heads/x\xff'". `r50-missing-origin-ref` and `r50-dangling-origin-head` both exit 0 with no diagnostic.

## Live smoke (clone; detached at base; origin/main holds reports/round-49/validation.json)

- No REFRESH: exit 3, `committed_sha=4ad2683… committed_blob=bd762a89… landed_ref=refs/remotes/origin/main landed_sha=4ad2683… hit_refs=HEAD,refs/heads/main,refs/remotes/origin/main`.
- REFRESH_RECEIPTS=1: exit 0, the permit line carries the same identity.
- Nonexistent receipt path: exit 0.

## Operability consequences (disclosed, not hidden)

- Any broken ref under `refs/heads` or `refs/remotes` now blocks every receipt write with RECEIPT-GUARD-GIT, even when unrelated to the receipt. This is what §5.2 requires.
- Any stderr from `for-each-ref` is treated as fail-closed. A noisy global git config would therefore block writes loudly rather than pass silently.
- Cost per guard call: one `for-each-ref` plus one `ls-tree` per distinct tip commit.

## Static checks

- Regex over the production code (everything before `def selftest_receipt`): no `fetch|push|ls-remote|update-ref|add|commit|status|checkout|reset|gc|stash|worktree|ls-files|diff|show-ref` inside `_git(...)`. Hits: none.
- Every git call goes through `_git(root, …)`, which keeps `-C ROOT`, `--literal-pathspecs`, and the GIT_* scrub.
- No absence decision uses `show-ref`. Unborn is decided by enumeration membership.

## Unrun and out of scope

- Mutation kill set MU-01..MU-16 (§7.5): not executed by me. That is the reviewer's oracle.
- Base-red evidence for the new fixtures: not executed.
- jj leg (§7.7) and the counting probe `reports/round-50/jj-colocation-probe.py`: not run, not in this seat's assignment.
- R3 (`check-readme-revisions`): not touched.
- Contract docs (ReviewGuardSemantics §C-5): `reports/round-14/guard/design.md` (lines 95-97, 105-108, 127-134) and the module docstring need same-change amendments. These are outside this seat's paths; I did not edit them. Flagged for L1.

## Tooling

No installs or upgrades. Host git 2.56.0, Python 3.14.8. pacman paused, not touched.
