# RevengerGuardIntent — receipt_guard.py original intent, invariants, committed_sha census (round-50, claim O intent leg)

Seat: ChousaR27R2.RevengerGuardIntent-4, lane base 4ad26836552462d28a946ca3b067cab0b5ce3532. Read-only; no lane file touched; no installs (none needed).

## 1. Original intent (reconstructed)

Root cause being guarded: the **receipt-clobber mechanism** — live rechecks invoked validators that
unconditionally rewrote their own *filed* `validation.json` (rounds 8/9 clobbers; exposure routed at
`reports/round-12/defects/routed.md:10-16`, ledger `FRR-12a`/`FRR-12b`; unconditional writes at
`reports/round-8/run-validation.py:1485-1487` and `reports/round-9/run-validation.py:1909-1911` per
`reports/round-14/guard/design.md:9-14`).

Round-14 declaration, `LOG.md:3148-3155`: "Round 14 declares a successor guard at
`tools/harness/receipt_guard.py`: refuse a committed receipt overwrite with exit 3 and a named
diagnostic unless `REFRESH_RECEIPTS=1` is explicitly set." Required control:
`python3 tools/harness/receipt_guard.py --selftest` plus the guarded round-14 runner and negative
controls. `SCORECARD.md:110` records the admitted capability: "overwrites of committed validation.json
refused unless REFRESH_RECEIPTS=1 (exit 3, named diagnostic); selftest both modes; retro-tests prove it
catches the r8/r9 clobber pattern; rounds 8-11 runners untouched".

History: exactly one commit touches the file — `git log --follow -- tools/harness/receipt_guard.py`
→ `b02cfbc 2026-10-17 round-14: admit O/D/C … receipt-guard capability`, 373 insertions, zero later
modifications. The design contract `reports/round-14/guard/design.md` (R14-D01, same date) is therefore
the authoritative statement of intent, not a stale draft.

Canonical contract (design.md "Decision semantics", verified present in code):
- **Committed predicate**: a blob at the exact repository-relative pathname in the *current HEAD commit
  tree* — `git --literal-pathspecs -C ROOT ls-tree -z --full-tree HEAD -- RELATIVE_PATH`
  (`receipt_guard.py:129`), head from `rev-parse --verify --quiet HEAD^{commit}` (`:67-69`). Explicitly
  NOT `git ls-files`, the index, disk existence, mtime, or dirty status (`design.md:60-66`).
- **Override**: only the exact env value `REFRESH_RECEIPTS=1` permits; `""`, `0`, `true`, `yes`, `01`,
  `" 1"`, `"1 "` all refuse (`:144-149`; selftest nonexact-refresh controls `:236-238`).
- **Fail closed**: git failure, timeout, non-repo root, corrupt/unreadable HEAD, failed tree query →
  exit 3 `RECEIPT-GUARD-GIT` "cannot determine committed status", never treated as uncommitted
  (`design.md:68-70`; controls `missing-git-fails-closed`, `corrupt-head-fails-closed`,
  `git-environment-cannot-rebind-root`).
- **Path safety** (`_check_receipt`, `:82-127`): bind root vs git toplevel agreement, reject
  outside-root, symlink target/ancestor, hardlink (nlink≠1), non-regular, `.git` component; override
  does not waive these. Unborn repo (no commits) → allow (`_head_commit` returns None, `:72-76`).
- **Diagnostic shape** (`:141-148`): `receipt_guard: refusing overwrite path=<rel>
  committed_sha=<full HEAD commit OID> committed_blob=<full blob OID>; explicit REFRESH_RECEIPTS=1
  required [RECEIPT-GUARD-COMMITTED]`; permit line `[RECEIPT-GUARD-REFRESH]` on the override path.
  design.md:127-134: `committed_sha` "identifies the exact committed snapshot checked", never truncate;
  "A failed identity lookup has no known committed SHA; say status is undetermined rather than inventing
  one."
- **Two-phase runner hook** `round_runner_main` (`:161-168`): guard before `runner()` and again before
  `write_receipt()` (a commit made during measurement is rechecked); refusal propagates as SystemExit(3)
  and the callback must not run.
- **Inert import; guard never writes the receipt** (`design.md:33-38,46-47`).

## 2. Invariants a jj fix must preserve (from design.md "Controls required" + live selftest)

The selftest at base is 45/45 controls (`JjAuditKotodama.md`, "Selftests under colocated jj" table);
claim O requires "all prior controls retained". Non-negotiable, per design.md:112-141 and the control
names in `selftest_receipt` (`:203-341`): committed-refused; committed-refresh-allowed; the seven
nonexact-refresh refusals; dirty-committed-refused; staged-dirty/staged-deletion refused;
deleted-committed-refused; new/staged-new/untracked allowed; relative-receipt-refused;
destination-root-discovery; literal-pathspec-no-wildcard-match / no-magic; GIT_DIR cannot rebind root;
outside-repo / directory / symlink-alias / symlink-ancestor / symlink-dotdot / hardlink refused with
and without override; unborn-receipt-allowed; explicit-root-cannot-discover-parent-repo;
missing-git-fails-closed; linked-worktree-refused; runner-refusal-before-callback;
runner-refresh-preserves-exit; runner-rechecks-before-publisher; corrupt-head-fails-closed. Before ==
after byte comparison on every refusal (`:234`).

Design-documented limits that the O fix is explicitly licensed to extend
(`design.md:186-191` "Limits and handoff"): "The commit predicate is the current checkout's `HEAD` tree,
**not all branches**, reflogs, or deleted historical pathnames … Commit identity and blob identity must
stay separate in any later broader-history implementation." So: multi-ref probing (HEAD +
`refs/heads/main` + `refs/remotes/origin/main`) is the anticipated "broader-history implementation",
with the constraint that the sha printed as `committed_sha` be the ref commit actually probed (or a
separate `landed_sha` per JjAudit recommendation 1), never conflated with the blob OID.

## 3. Divergence under jj colocation (JjAuditKotodama R1–R3, mapped to code)

- **R1 (high)** — `_head_commit` (`receipt_guard.py:67-69`) resolves jj's `@-` working-copy-parent
  commit; `committed_sha` (`:142`) then cites a commit on neither `refs/heads/main` nor
  `refs/remotes/origin/main` (observed: HEAD `f0e826a8…` vs `origin/main 4ad26836…`, 1 ahead, same
  tree). The refusal still fires, but every cited sha string becomes unlanded evidence. State-dependent:
  right after a helper commit HEAD == pushed tip (correct steady state); it diverges exactly in the
  state receipts are written in.
- **R2 (high, reproduced)** — `ls-tree <head>` (`:129`) is head-only. With the working copy anchored
  below the tip (`jj new <older-change>`), a receipt committed on `main`/`origin/main` is invisible →
  exit 0, overwrite allowed (sandbox case6 reproduction; JjAudit "R2"). The assumption HEAD == branch
  tip was implicit and git-only true by construction; the r14 design named it as a limit.
- **R3 (medium)** — sibling gate `tools/check-readme-revisions.py`: `skip()` (`:233-235`) does not clear
  `ok`; control 9 (`:302-321`) prints `SKIP control: base c42d675 README flagged (r49 defect) (base
  object unreachable)` and still exits 0 — the one lane gate that can silently degrade to a pass when
  the pinned `BASE_COMMIT` (`:67`) object is missing. Contrast: `claims-freshness.py` raises
  `GateInputError` and exits 2 on the same condition.

## 4. Which callers cite `committed_sha`?

**Producer (only definition)**: `tools/harness/receipt_guard.py:141-143` — `committed_sha={head}` from
`_head_commit`; consumed at `:144-149` (COMMITTED refusal / REFRESH permit) and asserted by the
selftest at `:235` (`f"committed_sha={head}" in result.stderr`).

**In-lane programmatic consumers: none beyond the guard itself.** `grep committed_sha tools/` matches
only `receipt_guard.py:142,235`. `tools/harness/receipt_guard_adoption.py` loads the guard namespace and
calls `guard_receipt(OUTPUT)` (`:877-878, 925-926, 974-975, 993-994` — embedded fixture-runner strings)
and so re-emits the line, but never parses the sha. `tools/harness/round_runner_conformance.py:23` and
`receipt_guard_adoption.py:64` reference only the entry-point names (`guard_receipt`,
`round_runner_main`) statically. `tools/harness/claims-freshness.py` does not cite it.

**Indirect emitters**: the guarded-refresh runners `reports/round-*/run-validation.py` (17→18 adopted of
28→29 filed, 11 unguarded-in-place; `SCORECARD.md:3604-3607` r34 census, `:3633-3636` erratum after
r26 became guard-adopted) funnel guard stderr lines into their filed `validation.json` receipts.

**Citation census, `grep -rn committed_sha reports/` → 26 files:**
- `reports/round-14/`: `rerun.json:214`; `validation.json:4206,4213,4220,4227,…` (fixture sha
  `bc6240a7…`, the r14 selftest receipt); `guard/design.md:128,131-133` (contract text);
  `guard/neg-04.md:24`; `guard/retro-tests.json:192,208,244,260,338,354,390,406` (r8 `e1694bad…`,
  r9 `9dc18ec1…`); `guard/retro-tests.md:37`; `guard/scribe.md:251`.
- `reports/round-17/civ/muisca.md:256` (`9b49a4a0…`, cited as filed-receipt protection evidence).
- `reports/round-21/validation.json:362,384,418` (`8115eaae…`).
- `reports/round-25/validation.json:819`, `round-26/validation.json:1874`,
  `round-27/validation.json:2157,2166,…`, `round-28/validation.json:2251,2260,…` (selftest receipt
  embeds).
- `reports/round-34/`: `cross/X02-conformance.md:109`; `op/O05-routing.md:180,182`;
  `op/O06-scribe.md:155`; `op/O07-verify-tool.md:243`; `op/O09-verify-routing.md:144`;
  `plan/P02-oc-plan.md:34` (all `da68a6d7…` = the then-HEAD, cited as operational evidence).
- `reports/round-36/`: `cov/C05-scribe.md:309` (`ce103bf…`); `cross/X02-conformance.md:435`;
  `scout/K03-recount-scout.md:320`.
- `reports/round-37/calib/Ca04-r36.md:14` (a REFRESH-permit line, `57c8409b…`).
- `reports/round-39/calib/Ca01-protocol.md:186,297`.
- `reports/round-50/claims.json:34-35` and `reports/round-50/telemetry/declaration-freshness.json:70`
  (this round's own claim text describing the defect).

Consequence for R1: files that copy `committed_sha` as operational evidence (r17 `muisca.md`, r34
`op/*`, r36 rows, r37/r39 calib protocols) were correct only while HEAD == landed tip; under jj the
same copy habit records an unlanded `@-` commit. The guard's fix should keep emitting a full, distinct
sha for whatever ref proved committedness (and/or a `landed_sha`), because 26 filed artifacts already
treat the field as citable identity — the field label may be extended, not omitted (`design.md:127`).

## 5. Constraints / notes for the O executor [INFERENCE unless cited]

- The selftest computes `head = _head_commit(root)` (`:231`) and asserts the diagnostic carries exactly
  that sha (`:235`); fixture commits live on `refs/heads/control` with no `origin/*`. Any change to the
  committed-predicate or the identity field must update this coupling coherently (e.g. probe all local
  branch refs, not literally `main` only, or teach the fixture a remote), or 45 retained controls break.
  [INFERENCE from code structure + JjAudit selftest observation]
- design.md `:186-191` pre-authorizes broader-history probing; deletion semantics must stay per-ref
  ("a path removed by a later committed deletion is not protected" remains true per probed ref).
- R2 fix direction per JjAudit recommendation 1: refuse if the path exists in HEAD **or**
  `refs/heads/main` **or** `refs/remotes/origin/main`; print the pushed/landed commit as the cited sha.
  R1 fix: same change makes the cited sha a landed one in the steady states observed.
- R3 fix direction: `check-readme-revisions.py` must assert `git cat-file -e <sha>^{commit}` before
  `git show` and turn unreachable-base into a FAIL (nonzero exit), not `skip()` (`:302-321, :233-235`).
  The selftest's own "(SKIP, not FAIL, when the object is unreachable)" comment (`:66`) documents the
  old intended behavior — the fix intentionally reverses this control, and the selftest's skip-path
  control must become a fail-closed control without deleting it.
- Claim O's counting probe needs base-tool bytes to show 3/3 false negatives; base bytes are exactly
  `b02cfbc`'s blob — single-commit history makes the base fixture trivially reproducible from
  `git show 4ad26836552462d28a946ca3b067cab0b5ce3532:tools/harness/receipt_guard.py`.

## 6. Unrun checks

No code was executed this session; all findings are read-only file/git evidence. Not run:
`receipt_guard --selftest` (45/45 status cited from JjAuditKotodama's sandbox observation, not
re-verified at base), the ExecGuard probe, any jj command (mutating jj banned in the lane; no jj
observation of my own).
