# ReviewGuardCode — falsify of O / `tools/harness/receipt_guard.py`

Seat: `KotodamaR50-2.ReviewGuardCode-21` (leaf, no delegation). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Landed bytes: commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
Item attacked: **claim O, operability — the `receipt_guard.py` half** (the
`check-readme-revisions.py` half and the separability checker are other seats).

Tooling: **nothing installed or upgraded** (no pacman/uv/cargo/npm transaction was
needed; the generic-rules channel order was not used). Host tools as-is: `git 2.56.0`,
`python3 3.14.8`. All execution happened in a private clone
`git clone -q --shared … /tmp/r50guard` + `checkout -q 1c779e4…` (deleted at the end);
`GIT_CEILING_DIRECTORIES=/tmp` for the probe legs. The lane was never written; the only
lane commands were read-only (`git log/for-each-ref/ls-tree`, and one read-only run of the
guard CLI, which spawns only git read verbs). The `jj` colocation probe was run from the
clone, not in the lane.

Reference contract attacked against: `.ufo/waves/round-50/build/ReviewGuardSemantics.md`
(§5.2 algorithm, §5.3 required outcome per state, §5.4 REFRESH, §5.5 diagnostic
invariants, §5.6 documented limits, §7.2 "the first 45 control names, in order, digest to
`d7a05f268c90e1d2eeb994678bef000d09dd9ccb69d5d39b9ee58f2bf269bf37`").

---

## 1. Verdict

**PARTIAL.** The landed guard is a faithful implementation of the reviewed algorithm and
holds on every state the assignment names — detached HEAD, unborn HEAD, broken refs,
in-namespace symrefs, non-UTF-8 refnames, REFRESH ordering, `GIT_*` scrubbing — with
**one fail-open** (F1: a symref under `refs/heads/*` or `refs/remotes/*` whose *target*
lies outside the two probed namespaces is skipped entirely, so a receipt committed at that
ref's tip can be overwritten with exit 0) and **two filed-contract drifts** (F2, F3, F4:
`reports/round-14/guard/design.md` and `corpus/lessons/round-49.md` still describe the
pre-round-50 HEAD-only contract and a guard scope that never existed). The acceptance
criterion of claim O reproduces independently (0/3 on the landed bytes, 3/3 on base
bytes).

Severity order: **F1 (fail-open, medium) → F2 (contract drift, medium-low) → F4 (stale
filed pointer, low) → F3 (docstring overstates coverage, low) → F5/F6 (residual limits,
no fix required)**.

---

## 2. What HOLDS (observed, with commands)

All rows below were produced by running the landed CLI as a subprocess against **real
git** fixtures built in `/tmp` (not the synthetic hand-written-object fixtures), plus the
landed `--selftest`.

| Axis / state | Result | Evidence |
|---|---|---|
| `--selftest` in a clone | **rc 0, `selftest_passed: true`, 69/69** | `python3 -B tools/harness/receipt_guard.py --selftest` in `/tmp/r50guard` |
| Base controls retained byte-identically | **45/45 name digest matches the review** | digest of the first 45 control names = `d7a05f268c90e1d2eeb994678bef000d09dd9ccb69d5d39b9ee58f2bf269bf37` (== ReviewGuardSemantics §7.2) |
| New controls | 24 `r50-*` controls added (20 from §7.3 + `r50-nonutf8-refname` + 3 extra) | `controls[45:]` list in the selftest JSON |
| **Detached HEAD** below the remote tip | refuses; `landed_*` reported from the remote only | `committed_sha=cb6203219cffe921b9420010f19045fe8d161403 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=cb62032… hit_refs=HEAD,refs/heads/main,refs/remotes/origin/main` |
| **Unborn HEAD**, remote holds the receipt | refuses; `committed_sha=none` | `committed_sha=none committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=cb62032… hit_refs=refs/remotes/origin/main` |
| Unborn HEAD, no refs hold it | allows (rc 0, silent) | landed control `r50-unborn-empty` |
| Unborn HEAD, a *local* branch holds it | refuses, `landed_ref=none` | landed control `unborn-local-branch-refused` (`hit_refs=refs/heads/side`) |
| **Broken ref**, loose garbage, `refs/heads/*` | rc 3 `RECEIPT-GUARD-GIT` + git's own warning | `…enumerating refs/heads and refs/remotes failed (exit 0): warning: ignoring broken ref refs/heads/broken` |
| **Broken ref**, empty ref file | rc 3 `RECEIPT-GUARD-GIT` | `warning: ignoring broken ref refs/heads/empty` |
| **Broken ref**, object missing (ghost oid) | rc 3 `RECEIPT-GUARD-GIT` | `fatal: missing object 0123…6789 for refs/heads/ghost` (for-each-ref rc 128) |
| **Broken ref**, corrupt `packed-refs` | rc 3 `RECEIPT-GUARD-GIT` | `fatal: unexpected line in .git/packed-refs` |
| Ref naming a **tree** / an **annotated tag** | rc 3 `RECEIPT-GUARD-GIT` | `refs/remotes/origin/main does not resolve to a commit (tag)`; tree case in the landed control `r50-tree-typed-ref` |
| Ref name containing a **newline** | rc 3 `RECEIPT-GUARD-GIT`, no traceback | `warning: ignoring ref with broken name refs/heads/we\nird` |
| **Symref** inside the probed namespaces (`refs/remotes/origin/HEAD → origin/main`) | refuses; the target is enumerated, not skipped into a hole | `landed_ref=refs/remotes/origin/main landed_sha=…` |
| Symref **chain** `refs/heads/one → two → three` | resolved by git; target enumerated | `git symbolic-ref refs/heads/one` → `refs/heads/three`; guard refuses on the receipt |
| Dangling symref (`origin/HEAD → origin/nope`) | allows, no false GIT | landed control `r50-dangling-origin-head` (rc 0) |
| **Non-UTF-8 refname** (`refs/heads/y\xff`, `refs/remotes/origin/x\xff`) | rc 3 `RECEIPT-GUARD-GIT`, **no traceback**; the guard's own `UnicodeDecodeError` branch is live (git lists the raw bytes and prints no warning) | `ref name is not UTF-8: b'refs/remotes/origin/x\xff'` |
| **REFRESH ordering**: `REFRESH_RECEIPTS=1` + broken ref | rc 3 `RECEIPT-GUARD-GIT` — REFRESH does not waive GIT | `warning: ignoring broken ref refs/heads/broken` under `REFRESH_RECEIPTS=1` |
| REFRESH + path error | rc 3 `RECEIPT-GUARD-PATH` | landed control `r50-refresh-path-refused` |
| REFRESH value must be exactly `"1"` | 10 non-exact values (`""`, `0`, `true`, `yes`, `01`, `" 1"`, `"1 "`, `"1\n"`, `"\t1"`, `yes`) all refuse with `RECEIPT-GUARD-COMMITTED` | probed individually |
| REFRESH consulted only **after** every probe | permit line appears only when a hit exists; permit carries the same `landed_*` fields | `receipt_guard: REFRESH_RECEIPTS=1 permits overwrite … landed_ref=refs/remotes/origin/main landed_sha=…` |
| **`GIT_*` scrubbing** | 8 injected variables pointing at a *real other repository* had **no** effect (`GIT_DIR`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_INDEX_FILE`, `GIT_WORK_TREE`, `GIT_COMMON_DIR`, `GIT_CONFIG_GLOBAL`, `GIT_CEILING_DIRECTORIES`): every run still reported the lane repo's own `committed_sha`/`landed_sha` | `tools/harness/receipt_guard.py:57-59` scrubs every `GIT_*` key and re-adds `GIT_OPTIONAL_LOCKS=0`, `GIT_NO_REPLACE_OBJECTS=1`, `LC_ALL=C` |
| Hostile `HOME` (`.gitconfig` with `core.bare = true`) | no effect; guard still resolved the bound repo | `… committed_sha=1f28fd1a… landed_ref=refs/remotes/origin/main` |
| Path safety unchanged (symlink dest / symlinked ancestor / hardlink / directory / outside root) | all refuse `RECEIPT-GUARD-PATH` | base controls `symlink-alias-refused`, `symlink-ancestor-refused`, `hardlink-alias-refused`, `directory-refused`, `outside-repo-refused` |
| Path oddities (tab, newline, leading `-` in the receipt name) | refuse correctly, no crash | `path=va\tlid.json`, `path=va\nlid.json`, `path=-weird.json` |
| **Claim O acceptance criterion** reproduced independently | landed bytes → `JJ_COLOCATION_FALSE_NEGATIVES=0/3`, `FALSE_POSITIVES=0/4`; base bytes (`git archive 4ad2683 tools`) → `3/3` | `python3 reports/round-50/jj-colocation-probe.py --tools-root /tmp/r50guard` and `--tools-root /tmp/r50base --history-repo /tmp/r50guard` |
| Claim O "check-readme-revisions --selftest passes" | `selftest: all checks passed`, rc 0 | `python3 -B tools/check-readme-revisions.py --selftest` in the clone |
| **Live lane** behaviour of the new semantics | the round-50 receipt write is still permitted: `python3 -B tools/harness/receipt_guard.py --repo-root . reports/round-50/validation.json` → **exit 0** (no lane ref holds that path; 48 ms) | lane is at `1c779e4`; `git ls-tree` over every `refs/heads`/`refs/remotes` tip shows `reports/round-50/validation.json` uncommitted |

Implementation faithfulness to ReviewGuardSemantics §5.2 (all confirmed in the landed
bytes): `_head_state` at `:76-93`; branch-not-listed check at `:196-197`; tip assembly
`HEAD` + sorted refs at `:199`; dedupe by oid **keeping names** (FO-11 avoided) at
`:201-204`; `landed` chosen only from `refs/remotes/*` at `:207`; any `for-each-ref`
stderr is fatal at `:106`; non-commit `objecttype` rejected at `:125`; REFRESH read only
at `:215`, after every probe.

---

## 3. Findings

### F1 — FAIL-OPEN: a symref whose target is outside the probed namespaces is skipped, and its committed receipt becomes overwritable

* **Code**: `tools/harness/receipt_guard.py:123-124`

  ```python
        if symref:
            continue
  ```

  with the docstring claim at `:10-12`: *"The committed probe covers HEAD and every direct
  refs/heads/* and refs/remotes/* ref. … symbolic refs are skipped because they duplicate
  their targets."*

* **Why it is a fail-open**: the justification ("they duplicate their targets") is false
  when the symref's target lies **outside** `refs/heads/*` and `refs/remotes/*`. The
  target is then never enumerated, so the tip the symref resolves to is never probed, and
  `git ls-tree` of that ref *does* find the receipt.

* **Reproduction** (real git, `/tmp/r50probe2.py`):

  ```
  A: refs/remotes/origin/main -> refs/tags/v1   (annotated tag of the commit holding the receipt)
  A: for-each-ref: refs/heads/main|7772f4cb…|commit|
                   refs/remotes/origin/main|4ae46e70…|tag|refs/tags/v1
  A: ls-tree via the remote ref: 100644 blob 0187f3b09d66cef7911083ad49f890f5a6589589  validation.json
  A: GUARD -> {"exit": 0, "stderr": ""}                       # overwrite ALLOWED
  A: GUARD with REFRESH=1 -> {"exit": 0, "stderr": ""}

  B: refs/heads/feature -> refs/tags/v1
  B: ls-tree via refs/heads/feature: 100644 blob 0187f3b0…  validation.json
  B: GUARD -> {"exit": 0, "stderr": ""}                       # overwrite ALLOWED
  ```

  i.e. a receipt **committed** at the tip that `refs/remotes/origin/main` resolves to is
  reported as absent, and the write is allowed.

* **Contract broken**: the module docstring (`:10-11`) and claim O's own text
  (*"detects a receipt committed on refs/heads/main or refs/remotes/origin/main"*).
  ReviewGuardSemantics §5.1 excludes `refs/tags/*` from the *evidence set*, but §5.2's
  rule is "probe every tip" — the landed code drops a tip that is inside the enumerated
  namespace because of where it points.

* **The oracle cannot see it.** I copied the tool to `/tmp/r50fix` and added a fail-closed
  branch for out-of-namespace symref targets (6 lines). Result: **`selftest_passed: true`,
  69/69** — i.e. no landed control pins the current behaviour, and the fix breaks nothing.
  The same patched copy turns A and B into `exit 3 … [RECEIPT-GUARD-GIT]`.

* **Smallest fix** (author-lane advice, not a lane edit):

  ```python
        if symref:
            target = symref.decode("utf-8", "replace")
            if not (target.startswith("refs/heads/") or target.startswith("refs/remotes/")):
                raise ReceiptGuardError("RECEIPT-GUARD-GIT",
                                        "cannot determine committed status: "
                                        f"{text} points outside the probed namespaces: "
                                        f"{target!r}")
            continue
  ```

  A regression control is needed too (the landed suite has none): a fixture with
  `refs/remotes/origin/main → refs/tags/v1` and the receipt committed on the tagged
  commit must refuse. Live-lane impact today: none — the lane's only symref is
  `refs/remotes/origin/HEAD → refs/remotes/origin/main` (inside the probed set), so the
  fix does not change lane behaviour. Realism: low (needs a hand-made symref into
  `refs/tags`/another namespace), but it is a fail-open on the exact claim wording and on
  the tool's own docstring, and it costs six lines to close.

### F2 — The filed contract was not amended: `reports/round-14/guard/design.md` still states the HEAD-only contract

* `reports/round-14/guard/design.md:95-97`: *"For this contract, committed means a blob at
  the exact repository-relative pathname in the current `HEAD` commit."*
* `reports/round-14/guard/design.md:105-106`: *"A genuinely unborn Git repository has no
  committed receipt and may permit a valid in-root target."*

Both are now false under the landed tool: an unborn HEAD whose `refs/remotes/origin/main`
holds the receipt is refused with `RECEIPT-GUARD-COMMITTED` (probe
`unborn-head-remote-holds-receipt`), and HEAD is no longer the only evidence source.

ReviewGuardSemantics **C-5** required the amendment *"in the same change as the code, or
the code contradicts a filed contract"*. The landed commit does not touch
`reports/round-14/` at all (`git log -1 -- reports/round-14/guard/design.md` → `b02cfbc`,
round-14). The diagnostic-shape section (`design.md:127-134`) is still satisfied because
it allows extended labels, so the drift is confined to the two sentences above.

* **Smallest fix**: amend `design.md:95-106` to the landed evidence set (HEAD +
  `refs/heads/*` + `refs/remotes/*`; `landed_*` only from `refs/remotes/*`; unborn HEAD
  refuses when any probed tip holds the path) and add the exclusion list the docstring
  omits (F3).

### F3 — Module docstring overstates coverage and documents no exclusions

`tools/harness/receipt_guard.py:10-17` says the probe "covers HEAD and every direct
refs/heads/* and refs/remotes/* ref" and never says which namespaces are *not* probed
(`refs/tags/*`, `refs/notes/*`, `refs/stash`, `refs/replace/*`, `refs/original/*`,
`refs/bisect/*`, `refs/jj/*`). ReviewGuardSemantics §5.1 requires exactly these to be a
*documented limit*; the landed docstring does not document them, and (F1) it also asserts a
symref coverage that does not hold. One or two sentences fix it.

### F4 — Stale and incorrect pointer in a filed lesson

`corpus/lessons/round-49.md:149`, `:232` and `:279` cite
**`tools/harness/receipt_guard.py:178` as "scopes the guard to `validation.json`"** and
`grep -n 'validation.json' tools/harness/receipt_guard.py # guard scope (:178)`. In the
landed file line 178 is `info = current.lstat()` (the path-safety loop); the guard has
**no filename scope at all** — only the adoption census
(`tools/harness/receipt_guard_adoption.py`) is scoped to `validation.json`. ReviewGuardSemantics
**C-6** flagged this exact defect (and that the base's `:178` was fixture code, not the
guard); the landed change moved the line without amending the lesson, so a filed lesson
now points at unrelated code and states a false property of the gate.

* **Smallest fix**: one line in `corpus/lessons/round-49.md` — replace the `:178` scope
  claim with the census pointer (`tools/harness/receipt_guard_adoption.py:65`) and drop
  the line-number pointer, or amend it to the new correct location.

### F5 — Residual (fail-closed, not a bypass): HEAD whose symref chain leaves `refs/heads/*`

`git symbolic-ref` resolves symref *chains* (probe D: `refs/heads/one → refs/heads/three`).
So `HEAD → refs/heads/main → refs/remotes/origin/main` makes the guard read
`HEAD names 'refs/remotes/origin/main', not a local branch` and refuse with
`RECEIPT-GUARD-GIT` (`:82-84`) even though the receipt is genuinely committed. Fail-closed
— no receipt can be overwritten — but it is a state the tool cannot answer. Worth one
sentence in the documented-limits list; no code change required.

### F6 — Residual (oracle strength, not a defect in the landed bytes): the probe's v2 R1 predicate cannot pin `landed_sha` to the tip

`reports/round-50/jj-colocation-probe.py:243-251` flags R1 only when (a) no
`landed`-labelled sha is presented, or (b) a `landed`-labelled sha is **not an ancestor**
of `refs/remotes/origin/main`. ReviewGuardSemantics §5.5 additionally requires
`landed_sha` to *equal* the current tip of `landed_ref`. A mutant that reported an
ancestor of `origin/main` as `landed_sha` would therefore pass the counting probe. The
guard's own selftest does pin the tip (`r50-detached-below-remote` asserts
`landed_sha=C2`), so the landed bytes are covered — but the counting probe alone is not a
complete oracle for the landed-sha invariant.

**Amendment provenance note (calibration, in the tool's favour):** the v1→v2 amendment of
the R1 predicate is honest and correctly explained in the probe source
(`:243-249`) and in `reports/round-50/telemetry/jj-probe-v1.txt` / `-v2.txt` (both runs
recorded). v1 flagged the contract-mandated `committed_sha=<HEAD>` field as a defect
because it is not an ancestor of `origin/main`; v2 restricts the ancestry test to
`landed`-labelled shas, which is the correct predicate. The v1 run's 1/3 on the landed
tools was a **false positive of the probe**, not a defect of the guard.

---

## 4. Residual risk / verification gaps

* **F1 is unfixed and untested by the landed suite** (69/69 stay green with the fix
  applied) — the one fail-open I found is invisible to the round's own oracle.
* I did **not** run the full ReviewGuardSemantics §7.5 mutation kill set (16 mutants);
  a sibling seat owns mutation testing. I ran one mutant (the F1 fix) purely to measure
  whether the oracle can see F1 — it cannot.
* I did not exercise the optional jj leg (`jj git init --colocate`) of §7.7: `jj` was not
  invoked, so "the landed bytes behave the same under a jj-colocated repo" is asserted
  only through the plain-git equivalents (the counting probe is jj-free by design).
* The guard's `--selftest` writes its fixture repositories under `<repo>/.scratch`
  (`.gitignore` line `.scratch/` covers it, so a jj/git status stays clean). I ran the
  selftest only in the clone, never in the lane.
* F1's realism is low (a hand-made symref into `refs/tags`); the honest severity is
  "medium on the claim text, low on expected frequency". I did not look for a way to
  create such a symref through jj (`jj bookmark` writes real refs).

## 5. Recommendation to the author lane

1. Close F1 (six lines, shown above) and add the missing regression control — the
   landed suite is otherwise blind to it.
2. Amend `reports/round-14/guard/design.md:95-106` (F2) and the module docstring `:10-17`
   (F3) in the same change, per ReviewGuardSemantics C-5; list the excluded namespaces
   and the out-of-namespace symref limit explicitly.
3. Fix the `corpus/lessons/round-49.md:149/232/279` pointer (F4) — it is a filed lesson
   that currently misstates the gate's scope.
4. No change needed for the claim's acceptance criterion: it reproduces (0/3 landed, 3/3
   base), the 45 base controls are byte-identical, and the 24 new controls are green.

**Verdict on the attacked item: PARTIAL — the refusal semantics hold on every named
state except the symref-target hole (F1), and the operator-facing contract (F2–F4) was
not brought in line with the new semantics.**
