# ReviewGuardSemantics: Claim O (receipt_guard R1/R2)

Seat: ReviewGuardSemantics (reviewer, leaf, no delegation). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `4ad26836552462d28a946ca3b067cab0b5ce3532` (lane HEAD unchanged). Target bytes `tools/harness/receipt_guard.py` sha256 `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` (tag B367, git blob `4610b23b…`).

Method: read the whole guard (lines 1–373, in ranges), `.ufo/waves/hyaku/jj-w1/reports/JjAuditKotodama.md`, the guard design contract `reports/round-14/guard/design.md`, the planned ExecGuard spec, and the round-14 caller handlers. All executed probes ran in disposable `/tmp` copies (removed after the run). The lane was not written, and no git or jj mutation ran in it.

Tooling: nothing installed or upgraded. Host tools used as-is: git 2.56.0, jj 0.45.1 (`~/.local/bin/jj`), Python 3.14.8.

Axes: coverage = every state the task names plus the fail-open classes; operability = a runnable oracle with a mutation kill set; calibration = each claim tagged observed, predicted, or inferred.

## 1. Verdict

1. The plan's direction (probe refs as well as HEAD) is right. Three of its details are wrong and would ship a fail-open or contract-breaking guard if followed:
   - **"branch from symbolic-ref when attached, else main" is fail-open.** A receipt committed on another local branch or another remote is allowed (observed rc 0 for both; §2 S7, S8).
   - **The `head_sha=` rename is incompatible.** It fails 17 of the 45 existing controls (measured; §7.5 MU-15) and breaks the design's required shape `committed_sha=<HEAD>` (`design.md:128`). Keep `committed_sha=` and add `landed_*` fields.
   - **"landed (branch/remote)" is wrong under jj.** Local branch refs can point at uncommitted working-copy commits (observed). Landed evidence comes only from `refs/remotes/*`.
2. A live false negative the audit does not list: **unborn HEAD plus a fetched `origin/main` that holds the receipt is allowed today** (S3, rc 0, plain git). The audit's class-A verdict "No change needed" (`JjAuditKotodama.md:41-42`) is wrong for this state.
3. R2 is a refusal-level false negative (reproduced under jj 0.45.1, rc 0). Keep it high. R1 produced no false pass in any tested state (rc 3 each time); it mislabels evidence, since `committed_sha` names a local-only commit. Calibrated: medium on safety, high on evidence integrity.
4. The fix is acceptable only when the §7 oracle is green on fixed bytes and every §7.5 mutant is killed. The existing 45 controls cannot detect R1, R2, or S3 (base passes 45/45), so passing them is not evidence for the fix.

## 2. Observed behavior on base bytes

Sandbox graph G1: `C1` (no receipt); `C2` (receipt `reports/validation.json`, blob `203e7040…`); `L` (local-only empty child of C2, same tree); `C4` on branch `kotodama` (adds `reports/round-50/validation.json`); remote `upstream` with `U2` (adds `reports/up/validation.json`). rc is from `python3 -B <copy>/tools/harness/receipt_guard.py --repo-root <repo> <path>`.

| ID | state | base rc | base stderr | required by §5 |
|---|---|---|---|---|
| S1 | R2: detached at C1; `refs/remotes/origin/main`=C2 holds receipt | 0 | none | 3; `landed_sha=C2` |
| S2 | R1: detached at L; `origin/main`=C2 holds same blob | 3 | `committed_sha=L` (local only) | 3; `committed_sha=L`, `landed_sha=C2` |
| S3 | unborn `main`; `origin/main`=C2 holds receipt | 0 | none | 3; `committed_sha=none`, `landed_sha=C2` |
| S4 | unborn, no refs | 0 | none | 0 |
| S5 | unborn; `origin` configured, never fetched | 0 | none | 0 |
| S6 | detached at clean commit, no remotes | 0 | none | 0 |
| S7 | attached to `scratch`=C1; `origin/kotodama`=C4 holds receipt | 0 | none | 3; `landed_ref=refs/remotes/origin/kotodama` |
| S8 | detached at U1; only `upstream/main` holds receipt | 0 | none | 3; `landed_ref=refs/remotes/upstream/main` |
| S9 | HEAD clean; `refs/remotes/origin/main` corrupt (`garbage`) | 0 | none | 3; RECEIPT-GUARD-GIT |
| S10 | HEAD file corrupt | 3 | RECEIPT-GUARD-GIT (locating tree) | 3 (unchanged) |
| S11 | attached to corrupt `refs/heads/scratch` | 3 | RECEIPT-GUARD-GIT (reading HEAD) | 3 (unchanged) |
| S12 | `refs/remotes/origin/HEAD` is a dangling symref | 0 | none | 0 |
| S13 | S1 + `REFRESH_RECEIPTS=1` | 0 | none (no permit line) | 0; RECEIPT-GUARD-REFRESH; `landed_sha=C2` |
| S14 | S2 + `REFRESH_RECEIPTS=1` | 0 | permit line prints `committed_sha=L` | 0; `landed_ref=refs/remotes/origin/main` |
| S15 | S9 + `REFRESH_RECEIPTS=1` | 0 | none | 3; RECEIPT-GUARD-GIT |
| S16 | detached HEAD file holds a tree oid | 3 | RECEIPT-GUARD-GIT (reading HEAD failed) | 3 (unchanged) |
| neg | S1 with `reports/new/validation.json`; S3 with `reports/never/validation.json`; S4 with `reports/new/validation.json` | 0 | none | 0 |

Selftest baseline on base bytes (copy): `controls_passed=45`, `controls_total=45`. Digest of the 45 control names joined by LF: sha256 `d7a05f268c90e1d2eeb994678bef000d09dd9ccb69d5d39b9ee58f2bf269bf37`. No fixture creates a `refs/remotes/*` ref, which is why the base passes 45/45 despite S1, S3, S7, S8.

jj 0.45.1, colocated temp clone of a copy of the origin:
- `jj git init --colocate`: HEAD attached to `refs/heads/main` (= `origin/main`; symbolic-ref rc 0).
- `jj new C1`: HEAD detached at C1 (symbolic-ref rc 1); `origin/main`=C2. Base guard **rc 0** (R2 reproduced).
- `jj new C2 && jj new`: HEAD = local empty E; `merge-base --is-ancestor E origin/main` rc 1. Base guard **rc 3** with `committed_sha=E` (R1 reproduced).
- `jj bookmark set main -r @` (with a new file in `@`): `refs/heads/main` moved to working-copy commit `7d2ff908…`, which no remote held. Local branch refs are not landed evidence.
- `jj git push --bookmark main` before tracking fails ("Non-tracking remote bookmark main@origin exists"). After `jj bookmark track main@origin` it returns rc 0 and `refs/remotes/origin/main` advances to the pushed commit. `refs/remotes/*` is therefore a valid landed source under jj.

## 3. Git facts the fix depends on (git 2.56.0, observed)

- `show-ref --verify --quiet <ref>`: rc 1 for a missing ref **and** for a broken loose ref (empty stderr). rc 1 is not proof of absence. A ref whose object is missing gives rc 128 "bad ref".
- `rev-parse --verify --quiet X^{commit}`: rc 1 for missing; rc 1 plus `warning: ignoring broken ref` for broken; rc 1 plus `expected commit type` for a tree-typed HEAD (`--quiet` does not suppress it).
- `for-each-ref refs/heads refs/remotes`: a broken loose ref gives **rc 0, `warning: ignoring broken ref <name>` on stderr, and the ref silently omitted from stdout**. A missing object with `%(objecttype)` gives rc 128 fatal. A dangling symref is omitted with rc 0 and no warning. A tree-typed ref lists with rc 0 and `objecttype=tree`, no warning.
- `ls-tree -z --full-tree <missing object>` gives rc 128 "not a tree object". The current code already fails closed here (`RG:129-131`). `ls-tree` on a tree-typed ref still finds the path (rc 0), so membership from a corrupt ref is still evidence the contract must refuse on.
- Corrupt `packed-refs`: `for-each-ref`, `show-ref`, and `rev-parse` all give rc 128 "unexpected line in .git/packed-refs". Loud, not silent.
- `symbolic-ref --quiet HEAD` gives rc 128 when HEAD names a broken branch. The current unborn path is safe only because of this (FO-05).

## 4. Corrections to the audit and the wave plan

- **C-1 Audit class A** (`JjAuditKotodama.md:41-42`; recommendation 2 at `:225-226`). "No change needed" and "documentation-only" are wrong for unborn HEAD with a fetched origin receipt (S3). `RG:126-128` must change.
- **C-2 R2 family.** State it as: any receipt absent from HEAD's tree but present in any `refs/heads/*` or `refs/remotes/*` tip is allowed today (S1, S3, S7, S8, jj R2).
- **C-3 R1 mechanism.** The guard refuses correctly. The defect is the label: `committed_sha` is a local commit and reads as landed. Severity as in §1.3.
- **C-4 Plan `ExecGuard`** (`.ufo/waves/round-50/gen-build-spec.py:39`; `build-spec.json:15`):
  - (a) `head_sha=` → keep `committed_sha=` (MU-15).
  - (b) "branch from symbolic-ref else main" → enumerate all `refs/heads/*` and `refs/remotes/*` (FO-03, FO-09).
  - (c) "landed (the branch/remote commit)" → remote-tracking only (FO-14).
  - (d) "missing refs tolerated" → absence is decided by a successful enumeration, never by `show-ref` rc 1 (FO-05).
- **C-5 Contract docs.** These describe the HEAD-only contract and must be amended in the same change as the code, or the code contradicts a filed contract:
  - `design.md:95-97` ("committed means a blob … in the current HEAD commit");
  - `design.md:105-108` ("genuinely unborn … may permit");
  - `design.md:127-134` (diagnostic shape);
  - module docstring line 2 ("against HEAD, not the mutable Git index").
- **C-6 Round-49 lesson.** `corpus/lessons/round-49.md:232-233` says `receipt_guard.py:178` "guards only validation.json". That is wrong: `:178` is fixture code (`receipt = root / "validation.json"` inside `_fixture_repo`), and `_check_receipt` has no filename test. Only the adoption census is scoped to `validation.json` (`receipt_guard_adoption.py:65`).
- **C-7 `committed_sha=none`.** The design says "a failed identity lookup has no known committed SHA" (`design.md:131-134`). Extend it: an unborn HEAD gives `committed_sha=none` because no HEAD commit exists. A failed lookup is RECEIPT-GUARD-GIT and is distinct.

## 5. Refusal semantics (the contract the fix implements)

### 5.1 Evidence set

- **H**: HEAD's commit when it resolves, attached or detached. Absent when HEAD is unborn.
- **Direct refs under `refs/heads/*`** (local branches; jj bookmarks are exported here) and **`refs/remotes/*`** (remote-tracking; the only landed evidence). Symrefs are skipped because they duplicate their targets.
- **Excluded** (documented limit): `refs/jj/*`, `refs/stash`, `refs/notes/*`, `refs/replace/*`, `refs/original/*`, `refs/bisect/*`, `refs/tags/*`. [INFERENCE] no lane tool creates tags; not grepped.

### 5.2 Algorithm (fail-closed wherever it says GIT)

```text
guard(P, root):
  pathsafety(P, root)                  # unchanged; RECEIPT-GUARD-PATH; REFRESH never waives
  bind(root)                           # unchanged; --show-toplevel must equal root
  H, branch = head_state(root)         # rev-parse HEAD^{commit} ok -> (oid, None)
                                       # rc 1 -> symbolic-ref: rc 0 -> (None, branch); rc 1 or other -> GIT
  refs = enumerate(root)               # for-each-ref refs/heads refs/remotes
                                       #   rc != 0, or ANY stderr -> GIT (include stderr text)
                                       #   skip non-empty symref; objectname must be OID; objecttype must be commit
  if branch and branch in names(refs): GIT    # HEAD names a branch that exists but does not resolve
  tips = ([("HEAD", H)] if H) + sorted(refs)  # probe every tip; never return ALLOW inside this loop
  blob = {oid: ls_tree(root, oid, P) for oid in distinct(tips)}   # None | blob oid | GIT
  hits = [(name, oid, blob[oid]) for name, oid in tips if blob[oid]]
  if not hits: return ALLOW                    # silent, rc 0
  landed = first(h for h in hits if h.name.startswith("refs/remotes/"))
  identity = committed_sha=(H or none) committed_blob=(blob[H] or none)
             landed_ref=(landed.name or none) landed_sha=(landed.oid or none)
             landed_blob=(landed.blob or none) hit_refs=(HEAD first, then sorted names)
  if env[REFRESH_RECEIPTS] == "1": stderr permit(identity) [RECEIPT-GUARD-REFRESH]; return ALLOW
  stderr refusal(identity) [RECEIPT-GUARD-COMMITTED]; exit 3
```

Implementation notes:
- `ls_tree`: rc ≠ 0 is GIT; empty stdout is absent; otherwise exactly one entry, type `blob`, exact name, else GIT. Keep the existing parse rules (`RG:134-141`).
- Dedupe by oid to limit subprocesses, but keep the name list per oid. Otherwise `HEAD == origin tip` loses `landed_*` (FO-11).
- Keep the existing `_git` dispatcher and env scrub (`RG:48-58`).

### 5.3 Required outcome per state

| State | Result | Tokens required |
|---|---|---|
| Attached; HEAD holds path | refuse (REFRESH → permit) | `committed_sha=H`, `committed_blob=B` |
| Detached at clean commit; remote tip holds path (S1) | refuse | `committed_sha=H`, `committed_blob=none`, `landed_ref=refs/remotes/…`, `landed_sha=tip` |
| Detached at local-only commit holding path; remote tip holds same blob (S2) | refuse | `committed_sha=L` ≠ `landed_sha=tip` |
| Detached at local-only commit holding path; no remote holds it | refuse | `landed_ref=none`, `landed_sha=none` |
| Unborn; remote tip holds path (S3) | refuse | `committed_sha=none`, `landed_sha=tip` |
| Unborn; a local branch holds path | refuse | `committed_sha=none`, `landed_ref=none`, `hit_refs=refs/heads/…` |
| Unborn; no refs hold path (S4) | allow | none |
| `origin` configured; `refs/remotes/origin/*` missing (S5) | allow; never GIT | none. Absence is local-only (§5.6) |
| Dangling `refs/remotes/origin/HEAD` (S12) | allow | none |
| Detached to tree, blob, or missing object | GIT | RECEIPT-GUARD-GIT, "reading HEAD failed" |
| Attached to a broken branch (S11) | GIT | RECEIPT-GUARD-GIT |
| Broken loose ref, HEAD clean (S9) | GIT | RECEIPT-GUARD-GIT, stderr names the ref |
| Ref to a missing object, or tree-typed ref | GIT | RECEIPT-GUARD-GIT |

### 5.4 REFRESH_RECEIPTS=1

- Exact value `"1"` only (unchanged). `""`, `0`, `true`, `yes`, `01`, `" 1"`, and `"1 "` all refuse.
- Consulted only after §5.2 finishes. Never before the path, bind, or GIT probes.
- Waives only RECEIPT-GUARD-COMMITTED. RECEIPT-GUARD-PATH and RECEIPT-GUARD-GIT remain refusals.
- The permit identity carries the same `landed_*` fields as a refusal. No HEAD-only identity.
- Writes nothing and sets no environment. A permit is not a refreshed receipt.

### 5.5 Diagnostic invariants (checked by the oracle)

- `committed_sha` is H or `none`. Never a branch or remote tip.
- `landed_sha`, when not `none`, equals the current tip of `landed_ref` (`git rev-parse <ref>`).
- `landed_*` never names HEAD or a local branch.
- Every GIT error includes git's stderr (truncated), so the operator sees the broken ref.

### 5.6 Limits (documented; the fix does not close them)

- Local evidence only. No `fetch` or `ls-remote`: a writer, and a failed network call would be a silent skip. A receipt on a remote this clone never fetched is invisible (pre-existing).
- `landed_sha` is the last remote tip this clone recorded. That approximates "pushed", and is verified for `jj git push`.
- Local branches holding the path refuse overwrites (over-refusal by design). Under jj, a bookmark moved onto a working-copy commit that contains the path refuses until it moves or REFRESH is used.
- TOCTOU between probe and write, and case sensitivity, are pre-existing (docstring; `design.md`).

## 6. Fail-open paths

Live in base (the fix must close each):

| ID | path | evidence | killed by |
|---|---|---|---|
| FO-01 | unborn short-circuit: `_head_commit` None → `return` (`RG:126-128`) | S3 rc 0. The same return also allows an unborn HEAD with a local branch holding the path (source-derived from `RG:126-128`; not run) | r50-unborn-remote; MU-01 |
| FO-02 | HEAD-only tree probe (`RG:129`) | S1, S7, S8, jj R2 rc 0 | r50-detached-below-remote; r50-unborn-remote |
| FO-03 | named-branch-only or origin-only probing | S7, S8 rc 0 under such a fix | r50-other-branch-remote; r50-other-remote; MU-02 |
| FO-04 | corrupt ref never probed | S9 rc 0 | r50-corrupt-remote |

Traps a fix introduces (each is a silent pass unless noted):

| ID | trap | observed basis | killed by |
|---|---|---|---|
| FO-05 | rc-only absence: `show-ref` or `rev-parse` rc 1 read as "missing" | broken loose ref gives rc 1 with empty stderr (§3). Current code is safe only because `symbolic-ref` also fails (S11) | r50-corrupt-remote; r50-corrupt-branch; MU-03; MU-14 |
| FO-06 | `for-each-ref` stderr ignored | rc 0 plus warning; ref omitted | r50-corrupt-remote; MU-04 |
| FO-07 | non-zero (missing object, rc 128) mapped to "absent" | ls-tree rc 128; for-each-ref without `%(objecttype)` lists a ghost ref with rc 0 | r50-missing-object-ref; MU-05 |
| FO-08 | non-commit objecttype accepted | tree-typed ref rc 0 in for-each-ref | r50-tree-typed-ref; MU-06 |
| FO-09 | hard-coded `main`, `origin`, or "else main" | S7, S8 | r50-other-branch-remote; r50-other-remote; MU-02 |
| FO-10 | early ALLOW from inside the ref loop | first clean tip returns | r50-detached-below-remote; MU-16 |
| FO-11 | dedupe by oid drops remote names (HEAD == origin tip) | hides `landed_*` (false "not landed") | r50-head-is-remote-tip; MU-08 |
| FO-12 | REFRESH consulted before probes, or REFRESH waives GIT or PATH | S15 pattern | r50-refresh-corrupt-remote; r50-refresh-path-refused; MU-09 |
| FO-13 | permit line prints HEAD-only identity | S14 | r50-refresh-landed; r50-refresh-local; MU-10 |
| FO-14 | landed derived from `refs/heads/*` | jj `bookmark set` moved `main` to an uncommitted `@` | r50-local-branch-not-landed; MU-07 |
| FO-15 | `GIT_*` passthrough (`GIT_DIR`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`), or `GIT_NO_REPLACE_OBJECTS` dropped | env scrub at `RG:49-51` | r50-env-scrub; MU-11 |
| FO-16 | probe without `-C ROOT` or `--literal-pathspecs` (binds to cwd repo) | the only dispatcher is `RG:54` | existing destination-root-discovery and cli controls (cli runs with cwd ≠ root); §7.4 |
| FO-17 | index or status as authority (`ls-files`, `diff --cached`, `status`) | jj resets the index on every mutation (audit class C); `status` writes the index | existing staged-new-receipt-allowed; §7.4 |
| FO-18 | network refresh (`fetch`, `ls-remote`, `update-ref`) | writer; ignored failure = silent skip | §7.4 static; invariant that `.git` is unchanged |
| FO-19 | ancestry landing (`merge-base --is-ancestor`, `rev-list`) with rc 128 read as "not ancestor" | [INFERENCE] grafts and shallow are not disabled by `GIT_NO_REPLACE_OBJECTS` | do not use ancestry; §7.4 static |
| FO-20 | parse errors escape the guard (`UnicodeDecodeError`, `IndexError`), exit 1 instead of 3 | source read: the parse code sits outside the try (`RG:126-149`) | predicted: r50-nonutf8-refname (§7.3 note) |
| FO-21 | a memoized first decision skips the publisher recheck | `round_runner_main` two-phase contract | existing runner-rechecks-before-publisher |
| FO-22 | public names renamed (`guard_receipt`, `round_runner_main`, `ReceiptGuardError`) | adoption census keys on them (`receipt_guard_adoption.py:64`); conformance (`round_runner_conformance.py:23`); round-14 `guard_preflight` (`reports/round-14/run-validation.py:419-425`) | gate failure, not a bypass; keep the names |
| FO-23 | dangling symref or missing remote treated as corruption (over-refusal) | S5, S12 | r50-missing-origin-ref; r50-dangling-origin-head; MU-12; MU-13 |
| FO-24 | `committed_sha` renamed (`head_sha=`) | 17 of 45 existing controls fail | existing controls; MU-15 |

Swallowed-exception check: the round-14, 15, 16, 17, 18, and 20 `guard_preflight`-style handlers catch `Exception`, convert `ReceiptGuardError` to exit 3, and re-raise everything else (round-14 `run-validation.py:419-425`; the other five share the first four lines of that handler and were not read to their end). Rounds 21–33 were not inspected.

## 7. Acceptance oracle

### 7.1 Setup (disposable copy under `<clone>/.scratch`; never in the lane)

- Copy the fixed tree. `export TMPDIR=$PWD/.scratch`; `PYTHONDONTWRITEBYTECODE=1`.
- Build fixtures with the existing hand-written object helper (`_fixture_repo` and `store`, `RG:171-198`). Graph G1 is as in §2.
- Refs not listed for a control are absent.
- Remote-tracking refs are loose files under `.git/refs/remotes/`. HEAD edits write `.git/HEAD`. Corrupt refs write `garbage\n`. A ghost ref writes an absent oid. A tree-typed ref writes C2's root tree oid.

### 7.2 Existing controls (must not change)

- `python3 -B tools/harness/receipt_guard.py --selftest` returns rc 0, `selftest_passed: true`, and `controls_passed == controls_total`.
- The first 45 control names, in order, digest to `d7a05f268c90e1d2eeb994678bef000d09dd9ccb69d5d39b9ee58f2bf269bf37`. Their expectations are not edited (weakening is forbidden).

### 7.3 New controls (`r50-*`)

"Base" is the result of B367 on the same fixture. A red base row is the proof that the control can fail.

| ID | HEAD | other refs | path | REFRESH | exit | must contain | must not contain | base |
|---|---|---|---|---|---|---|---|---|
| r50-detached-below-remote | detached C1 | `origin/main`=C2 | `reports/validation.json` | unset | 3 | RECEIPT-GUARD-COMMITTED; `committed_sha=C1`; `committed_blob=none`; `landed_ref=refs/remotes/origin/main`; `landed_sha=C2` | — | rc 0, red |
| r50-local-over-remote | detached L | `origin/main`=C2 | validation.json | unset | 3 | `committed_sha=L`; `landed_ref=refs/remotes/origin/main`; `landed_sha=C2` | `landed_sha=L` | rc 3 without landed tokens, red |
| r50-unborn-remote | unborn `refs/heads/main` | `origin/main`=C2 | validation.json | unset | 3 | `committed_sha=none`; `landed_sha=C2` | — | rc 0, red |
| r50-unborn-empty | unborn | none | validation.json | unset | 0 | — | RECEIPT-GUARD | green |
| r50-missing-origin-ref | unborn; `origin` configured, no refs | none | validation.json | unset | 0 | — | RECEIPT-GUARD-GIT; RECEIPT-GUARD-COMMITTED | green |
| r50-other-branch-remote | attached `refs/heads/scratch`=C1 | `origin/kotodama`=C4 | `reports/round-50/validation.json` | unset | 3 | `landed_ref=refs/remotes/origin/kotodama` | — | rc 0, red |
| r50-other-remote | detached U1 | `upstream/main`=U2 | `reports/up/validation.json` | unset | 3 | `landed_ref=refs/remotes/upstream/main` | — | rc 0, red |
| r50-local-branch-not-landed | attached `refs/heads/main`=L | `origin/main`=C1 (no receipt) | validation.json | unset | 3 | `committed_sha=L`; `landed_ref=none`; `landed_sha=none`; `hit_refs=HEAD,refs/heads/main` | `landed_sha=L` | rc 3 without landed tokens, red |
| r50-head-is-remote-tip | attached `refs/heads/main`=C2 | `origin/main`=C2 | validation.json | unset | 3 | `committed_sha=C2`; `landed_ref=refs/remotes/origin/main`; `landed_sha=C2` | — | red (no landed tokens) |
| r50-corrupt-remote | detached C1 | `origin/main`=`garbage` | validation.json | unset | 3 | RECEIPT-GUARD-GIT; names `refs/remotes/origin/main` | RECEIPT-GUARD-COMMITTED | rc 0, red |
| r50-missing-object-ref | detached C1 | `origin/ghost`=absent oid | validation.json | unset | 3 | RECEIPT-GUARD-GIT | — | rc 0, red |
| r50-tree-typed-ref | detached C1 | `origin/main`=C2 root tree oid | validation.json | unset | 3 | RECEIPT-GUARD-GIT | — | rc 0, red |
| r50-corrupt-branch | attached `refs/heads/scratch`=`garbage` | — | validation.json | unset | 3 | RECEIPT-GUARD-GIT | — | rc 3, green (regression) |
| r50-dangling-origin-head | detached C1 | `origin/HEAD`→`origin/nope`; `origin/main`=C1 | validation.json | unset | 0 | — | RECEIPT-GUARD | green |
| r50-refresh-landed | detached C1 | `origin/main`=C2 | validation.json | `1` | 0 | RECEIPT-GUARD-REFRESH; `committed_sha=C1`; `landed_sha=C2` | — | rc 0, red (no permit line) |
| r50-refresh-local | attached `refs/heads/main`=L | `origin/main`=C1 | validation.json | `1` | 0 | RECEIPT-GUARD-REFRESH; `landed_ref=none` | — | red (no landed tokens) |
| r50-refresh-corrupt-remote | detached C1 | `origin/main`=`garbage` | validation.json | `1` | 3 | RECEIPT-GUARD-GIT | RECEIPT-GUARD-REFRESH | rc 0, red |
| r50-refresh-nonexact-landed | detached C1 | `origin/main`=C2 | validation.json | `yes` | 3 | RECEIPT-GUARD-COMMITTED | — | rc 0, red |
| r50-refresh-path-refused | detached C1; symlink alias to the landed target | `origin/main`=C2 | alias path | `1` | 3 | RECEIPT-GUARD-PATH | — | green (path checks first) |
| r50-env-scrub | detached C1; `GIT_DIR` env set to an empty repo | `origin/main`=C2 | validation.json | unset | 3 | RECEIPT-GUARD-COMMITTED | — | rc 0, red |

Note (predicted, not executed): add `r50-nonutf8-refname`, a loose ref whose name contains a 0xFF byte. Expected rc 3 with RECEIPT-GUARD-GIT, never exit 1. This covers FO-20.

Invariants for every new control:
- receipt bytes identical before and after;
- `.git` file listing and sha256 identical before and after (read-only probe);
- no refs created;
- exit code and tokens as listed.

### 7.4 Static checks (on the fixed file)

- In `_head_commit`, the new enumerator, the `ls_tree` helper, and `_check_receipt` (not `selftest_receipt`), no git verb from `fetch|push|ls-remote|update-ref|add|commit|status|checkout|reset|gc|stash|worktree|ls-files|diff`.
- Every git call goes through `_git(root, …)`, which gives `-C ROOT`, `--literal-pathspecs`, and the GIT_* scrub. No `os.environ` passthrough into git.
- No absence decision made by `show-ref` or `symbolic-ref` alone. Absence is set membership in the successful enumeration.

### 7.5 Mutation kill set (each mutant applied to the fixed copy must fail at least one control)

| ID | mutant | must fail |
|---|---|---|
| MU-01 | keep the unborn `return` before enumeration | r50-unborn-remote |
| MU-02 | probe only `refs/heads/<branch or main>` and `refs/remotes/origin/<same>` | r50-other-branch-remote; r50-other-remote |
| MU-03 | absence by `show-ref --verify` rc 1 | r50-corrupt-remote |
| MU-04 | ignore for-each-ref stderr | r50-corrupt-remote |
| MU-05 | non-zero ls-tree or for-each-ref treated as absent | r50-missing-object-ref |
| MU-06 | accept objecttype other than commit | r50-tree-typed-ref |
| MU-07 | landed derived from `refs/heads/*` | r50-local-branch-not-landed |
| MU-08 | dedupe by oid, losing names | r50-head-is-remote-tip |
| MU-09 | REFRESH early return before probes | r50-refresh-corrupt-remote |
| MU-10 | permit line HEAD-only | r50-refresh-landed |
| MU-11 | GIT_* passthrough | r50-env-scrub |
| MU-12 | missing remote ref treated as error | r50-missing-origin-ref |
| MU-13 | dangling symref treated as error | r50-dangling-origin-head |
| MU-14 | rc 1 from rev-parse treated as unborn without the symbolic-ref and absence proof | r50-corrupt-branch |
| MU-15 | `committed_sha=` renamed to `head_sha=` | existing controls (**measured: 17 of 45 fail**) |
| MU-16 | ALLOW from inside the ref loop at the first clean tip | r50-detached-below-remote |

MU-01 to MU-14 and MU-16 are predicted by construction and not executed. MU-15 was executed on a copy of base bytes.

### 7.6 Counting probe (`reports/round-50/jj-colocation-probe.py`)

- Must evaluate the 20 `r50-*` fixtures plus R1, R2, and R3 on both trees. Base must be red on every must-refuse fixture; the fixed tree must be green on all.
- "0/3 false negatives" alone is circular. The 20 fixtures and the §7.5 mutation set are the anti-circularity evidence.

### 7.7 Optional jj leg (run only if `jj` is present; record the reason if skipped)

- `jj git init --colocate` in a temp clone. `jj new <older>` must refuse (r50-detached-below-remote shape).
- `jj new <remote-tip> && jj new` must report `landed_ref=refs/remotes/origin/main` and `committed_sha` = the local empty commit.

## 8. Calibration

Observed in this session (sandbox commands described above):
- Base bytes equal the lane file (sha256 `d2297da4…`). Base selftest 45/45 (names digest `d7a05f26…`).
- S1, S3, S7, S8, S9, S12–S16 and the negatives return the rc values in §2. jj R2 rc 0; jj R1 rc 3 with local `committed_sha`.
- jj push advances `refs/remotes/origin/main`. `jj bookmark set` moves `refs/heads/main` onto an uncommitted working-copy commit.
- Git probe return codes as in §3.
- Renaming `committed_sha` to `head_sha` fails 17 of 45 existing controls.

Predicted, not executed:
- §7.5 MU-01 to MU-14 and MU-16.
- §7.3 expectations on fixed bytes (no fixed bytes exist).
- The `r50-nonutf8-refname` control.

Inferred [INFERENCE]:
- The lane's live `refs/remotes/*` state after the helper's commit and push flow (not exercised in the live lane).
- A jj-colocated unborn-with-fetched-origin state (only the plain-git analog was exercised).
- No lane tool creates tags (not grepped).
- Performance is not measured. Expected cost is at most distinct tips + 2 subprocesses.
- FO-19 grafts and shallow behavior.

Unrun:
- The fixed-bytes oracle.
- `check-readme-revisions` (R3; outside this seat).
- Guard handlers in rounds 21–33.
- Any in-lane selftest (forbidden for this seat).

## 9. Order for the integrator

1. Amend `design.md` (C-5, C-7) and the docstring in the same change as the code.
2. Implement §5.2 exactly. Keep names, exit codes, `committed_sha=`, and the REFRESH rule.
3. Add the 20 `r50-*` fixtures and the §7.4 static checks. Keep the 45 existing controls byte-identical.
4. Run the §7.5 mutation set on the fixed copy. Any surviving mutant blocks the change.
5. Run the counting probe on base and on fixed (§7.6). Claim O only after both.
