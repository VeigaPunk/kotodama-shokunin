# RevReceipts — attack on the D2 receipt leg (round 66, wave 1)

- Target: `reports/round-66/accept-ca.py` D2 (lines 110–143), `claims.json` Ca leg D2/frozen predicate.
- Base: lane `main` = `94209e8f80969dbac48d56c5d0e2e623635b8616`; lane is jj-colocated (`.jj` present).
- Method: copied the three real counters byte-for-byte into a scratch git repo (`/tmp/r66-d2`) and ran the **real** `accept-ca.py` there (`--root` = scratch) against crafted receipts. D2 is pure git+text, so fidelity is high. Live lane state is pre-data: `D2 FAIL bad=[...final-measures-c/o/ca.txt:absent]` (run read-only at the lane tip).
- Tools installed: none (pacman paused; nothing needed).

Verdict: **the three named commit orders are not equal.** "Committed twice in different commits" is caught (fail-closed, except when it degenerates to an amend); "receipt amended" and "receipt carried by a merge" **pass**. The deeper defect is that D2's expected value is **self-asserted by the receipt**, so a receipt measured *before* the record lands also passes — R65-D2 is narrowed, not closed.

## Results matrix (real D2 leg, scratch repo)

| # | Commit order | D2 | Note |
|---|---|---|---|
| A | lands L, receipt committed as its child (control) | PASS | intended shape |
| B | receipt committed at C1, then edited in a **new commit** C2 | FAIL | `parent=a79dffd7 stamped=aa4040f4` — caught |
| E | receipt committed, deleted, then **restored byte-identical** | FAIL | `parent=… stamped=…` — conservative, caught |
| G | two receipt versions both children of L, merged (`--no-ff`), merge keeps one | FAIL | carrier becomes the merge, `M^=C1≠L` — caught |
| C | receipt commit **amended**, body rewritten ("D1 PASS fabricated…"), parent preserved | **PASS** | F2 |
| D | receipts introduced **by a merge commit** whose first parent is L (`commit-tree tree -p L -p B`) | **PASS** | F4 |
| F | receipt stamped at BASE, committed **as BASE's child**, lands committed afterwards | **PASS** | F1 |
| F2 | same as F, with a fabricated all-PASS body | **PASS** | F1+F2 |
| T5 | counter edited **in the same commit** as the receipts (clean tree, all committed) | **PASS** | receipt sha `7205e996` ≠ counter at stamped `0726b4bc` — F3 |
| T6 | receipts whose body says `ACCEPT-CA-66: FAIL` / `D1 FAIL` / `exit=1` | **PASS** | body never read — F2 |
| T1 | `cwd=/tmp` (non-repo), `--root=/tmp/r66-d2` | D2 PASS, header `measured revision: unresolvable` | F6 |
| T3 | receipt carries two `measured revision` lines (first = carrier parent, second = older) | **PASS** | only first occurrence parsed — F7 |
| T4 | extra `final-measures-c-extra.txt` present | PASS, file ignored | fixed list, not a glob — F7 |

## HIGH

### F1 — D2 is circular: the expected parent is the receipt's own text, so a pre-data/stale receipt passes

`accept-ca.py:115-116` parses `stamped` **out of the receipt**, then `:127` asserts `carrier^ == stamped`. Any receipt that names its own parent passes, whatever its measurement covers. Nothing ties `stamped` to the round's lands (no `git cat-file -e <stamped>:reports/round-66/...`, no diff between `stamped` and `carrier`).

Repro (F): commit a receipt stamped `BASE`, as a child of `BASE`; commit the lands afterwards → `D2 PASS bad=[]`.

Consequence for calibration: round-65's routed defect was a receipt committed **later** than the revision it measured. The new leg forbids *late* and is silent on *early*, so the same failure mode (receipt that proves nothing about the record state) is reachable by committing the receipt first. The orchestrator's suggestion quoted in `claims.json` review_only — "make the expected lands hash the actual parent at run time" — is not implemented; the expected hash is the receipt's self-report. **This is the answer to that open question: the re-derivation is not the right generalization as written.**

Minimal repair (one line closes it): require `git diff --name-only <stamped> <carrier>` to equal exactly the three receipt paths — i.e. the receipt commit adds only receipts to the measured tree. Plus require the claim's land paths to exist at `stamped`.

## MEDIUM

### F2 — An amended receipt commit passes with arbitrarily rewritten bytes; the body is never validated

`git commit --amend` (or `jj squash`/`jj describe`/`jj edit`, routine in a **jj-colocated** lane) preserves the parent, so `carrier^ == stamped` still holds. D2 reads only the stamp, `tree:`, and counter-sha lines — it never looks at the receipt body.

Repro: C (append `D1 PASS fabricated` / `D2 PASS fabricated` / `D3 PASS fabricated` inside the receipt commit via amend) → `D2 PASS bad=[]`. T6: body `ACCEPT-CA-66: FAIL … exit=1` → `D2 PASS bad=[]` (carrier `32ffdffb`, `carrier^=f591b663`, stamped `f591b663`).
Only the stamp is protected by the amend route: C2 (amend that changes the stamp only) → FAIL `parent=… stamped=…, tree`.

Consequence: the receipts are the only record of the final counter runs (no other `.py` consumes `reports/round-66/telemetry/final-measures-*`), and their content is not bound to the run at all. Any post-hoc edit — honest typo fix or fabricated verdict — is indistinguishable. Because the lane's default VCS operation rewrites commits, this is not an exotic author.

Repair: have each counter emit a machine footer (`tree:`, `dirty:`, leg names, `exit=`, `ACCEPT-<id>-66: PASS|FAIL`) and have D2 require the receipt to end with the counter's PASS footer and to contain exactly the current leg-name set.

### F3 — `counter sha256` resolves against the working tree, not the stamped/carrier revision

`accept-ca.py:134-141` reads the counter with `read(root, counter_path)` (worktree bytes). The docstring (`:16`) claims the counter sha line "resolve[s] against the stamped revision" — it does not.

Repro T5 (clean tree, everything committed): counter edited in the same commit as the receipts; receipt records `7205e996`, counter at `stamped` is `0726b4bc`; `D2 PASS bad=[]`. T2b: with an uncommitted counter tweak, receipt sha matches the dirty bytes; `D2 PASS`, `git status` shows `M reports/round-66/accept-c.py`.

Consequence both directions: a receipt can certify a counter version that never existed at the measured revision; and any counter fix committed *after* the receipts retroactively fails D2 until the receipts are regenerated (so any repair from this report must land **before** the final measurement commit, not after).

Repair: hash `git show <carrier>:<counter>` and require the same blob at `<stamped>`.

### F4 — A receipt "carried by a merge" passes because `carrier^` is the first parent

`accept-ca.py:126` uses `rev-parse <carrier>^` = first parent. A merge commit therefore satisfies "that commit's parent equals the stamped revision" even when the receipt bytes exist in no single-parent child of the measured revision.

Repro D: `M = commit-tree <tree-with-receipts> -p L -p B`, where `L` is stamped and `B` is a side commit; receipt bytes exist only in `M` → `D2 PASS bad=[]`, parents printed `(M, L, B)`.
Also asymmetric: G shows `git log -1 -- path` selects a **side-branch** commit when the merge is TREESAME to its second parent (`carrier=C2`, `C2^=L` would pass) or the merge itself when it is TREESAME to neither (`carrier=M`, `M^=C1` → FAIL). The leg's carrier model is git-log-simplification-dependent in both directions and is not stated anywhere.

Practical risk today: low (linear jj integration). Spec risk: "parent" is under-defined; a merge record commit would pass.

Repair: `git rev-list --parents -1 <carrier>` must yield one parent, or state and test the first-parent rule explicitly.

### F5 — "Committed twice in different commits": handled, with one degenerate case

Caught: B (edit in a new commit), E (delete + byte-identical restore), G (second version off stamped, merge). All fail on `carrier^ != stamped`. So this specific order is fail-closed **as long as the second commit is a new commit**; it degenerates into F2 when "the second commit" is the same commit rewritten. Note E's conservative behavior: a receipt cannot be re-added after accidental deletion — it must be regenerated, which is correct but should be documented for the integrator.

## LOW

### F6 — The receipt's revision header is cwd-derived in C and Ca (O already fixed)

`accept-ca.py:78` and `accept-c.py:137` run `git rev-parse main` **without `-C root`**; `accept-o.py:109-114` does it correctly and hard-fails (`REVISION FAIL`, exit 2) when unresolvable. Ca has no such guard.

Repro T1: `cwd=/tmp`, `--root=/tmp/r66-d2` → header `measured revision (lane main): unresolvable` while D2 still evaluates the root correctly.
Consequence: a run inside a `needs_git` clone / fixture lane with `cwd` at the lane stamps the **lane's** main into the receipt while measuring the clone — exactly the separability workflow that generates these receipts.

Repair: add `-C root` at both sites, and copy O's `REVISION FAIL` exit-2 guard into Ca.

### F7 — Receipt set hardcoded; only the first stamp is parsed; the tree line is hand-written

- `RECEIPTS` (`accept-ca.py:39-43`) is a fixed three-item list while the claim's D2 leg says "for each `final-measures-*.txt`"; T4 shows an extra matching file is ignored and untracked.
- `re.search` (`:115-116`) takes the first `measured revision` occurrence; T3 (two stamps, first = carrier parent, second = older) → `D2 PASS`.
- No counter emits a `tree:` line (`dry-run-ca.txt`, `dry-run-c.txt`, `dry-run-o.txt` headers are two lines). The `tree:` value D2 checks (`:130-133`) is therefore hand-written: it proves the author could run `git rev-parse <stamped>^{tree}`, not that the run saw that tree.

Repair: glob the receipts; `re.findall` + require exactly one stamp; emit `# measured tree:` and `# dirty:` from the counters.

## Does the miss matter?

- **Against the frozen predicate as worded:** no. The claim's D2 leg ("`git log -1 main -- <receipt>` names the commit carrying it, that commit's parent equals the receipt's stamped measured revision, and tree + counter sha256 lines match") is implemented literally, and a truthful integrator satisfies it. The other Ca legs (D1/D3/D4/CRITERION/QUOTES) run live on the current tree, so they do not inherit the receipts' weakness.
- **Against the routed defect R65-D2 (calibration):** yes. F1 leaves the original failure mode reachable by committing the receipt *early* instead of *late*; F2/F3 let the receipt's content and the counter version be changed after the fact while the leg stays green; F4 leaves "parent" first-parent-only. Net effect: D2 narrows R65-D2 to "no delay on the linear line, content unverified" — a real improvement over round 65, but not a closure, and the claim should not be read as proving the receipts describe the final state.

## Residual risk / verification gaps

- All attacks ran in `/tmp/r66-d2` with byte-identical copies of the three counters and hand-authored receipts; **no live round-66 receipt exists yet** (`final-measures-*` absent at the lane tip, `D2 FAIL ...:absent`), so no attack was carried out on real receipts.
- `git log -- path` simplification behavior was measured on this git version only; jj was used only as an argument that amend-style rewriting is routine (no jj-level test — mutating the lane is out of scope for this seat).
- Untested: `main` bookmark lagging the jj working-copy commit; `main` missing (code path returns `no_carrier`, read not run); worktrees/submodules.
- If any repair from R1–R4 or R5 lands after the receipts are produced, D2 will fail on the frozen counters (F3) — land repairs before the final measurement commit.

## Appendix — reproduction

```python
# scratch = git repo seeded with one commit BASE; copy the three real counters to
# reports/round-66/{accept-c,accept-o,accept-ca}.py; receipts are hand-written as
#   # counter sha256 (self): <sha of the counter>
#   # measured revision (lane main): <S>
#   tree: <git rev-parse S^{tree}>
#   ACCEPT-CA-66: PASS / exit=0
# then: python3 -B reports/round-66/accept-ca.py --root <scratch>, read the D2 line.
# A: lands L; write receipts(S=L); commit            -> PASS
# B: ...; edit receipt in a new commit               -> FAIL parent
# C: ...; amend the receipt commit with new body     -> PASS            (F2)
# D: M = commit-tree tree -p L -p B (receipts only in M) -> PASS        (F4)
# E: delete receipts, commit, restore identical, commit -> FAIL parent
# F: write receipts(S=BASE); commit; then commit lands -> PASS          (F1)
# T5: edit counter, write receipts(S=L) with new sha, one commit -> PASS (F3)
# T3: two `measured revision` lines, first = L        -> PASS            (F7)
```
