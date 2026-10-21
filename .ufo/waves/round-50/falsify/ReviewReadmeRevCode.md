# ReviewReadmeRevCode — falsify wave, Round 50 attempt 1

**Item attacked:** Claim O (operability), second gate — `tools/check-readme-revisions.py` at
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`.
**Verdict:** **PARTIAL** — the primary contract (unreachable pin → nonzero, `SKIP` deleted) HOLDS;
two secondary defects survive, one of them squarely inside the claim's own wording.

Attacked bytes (never the working tree):
`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:tools/check-readme-revisions.py`
→ sha256 `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4`, 560 lines.
Private clones: `/tmp/rrc-XXXX` (`--shared`, checked out at the landed sha) and `/tmp/rrc-full`
(`--no-hardlinks`, full clone at the landed sha). Both deleted after the run.

---

## 1. What HOLDS (verified, not assumed)

### 1.1 Unreachable pin → exit 2 (the core claim) — **HOLDS**

The `SKIP` path is genuinely deleted, not merely made louder. `git diff 4ad2683 1c779e4` on this
file shows the base's `skip(name, "(base object unreachable)")` branch and the trailing
`print("selftest skips: %d" % len(skips))` line removed, replaced by `base_readme_verdict()`
returning `ERROR` and `selftest()` returning `2` when `errored` is non-empty
(`tools/check-readme-revisions.py:411-414`, `:462-468`).

The claim text (`reports/round-50/claims.json`, claim O) is *"fails closed (nonzero) when its pinned
BASE_COMMIT is unresolvable instead of SKIP+exit0"*. That holds in every seam I could construct:

| # | Seam | Command | Exit | Observed line |
|---|---|---|---|---|
| T1 | all-zero pin | `--selftest --base-commit 000…0` | **2** | `ERROR control: base 0000000 README flagged (r49 defect) … unreachable in /tmp/rrc-XXXX: fatal: Not a valid object name` |
| T2 | `--lane` = git-free tree | `--selftest --lane /tmp/rrc-gf` | **2** | `ERROR … fatal: not a git repository (or any parent up to mount point /)` |
| T3 | `--lane` = nonexistent path | `--selftest --lane /tmp/does-not-exist-xyz` | **2** | `ERROR … fatal: cannot change to '/tmp/does-not-exist-xyz': No such file or directory` |
| T6 | shallow clone (depth 1) | `--selftest` in `/tmp/rrc-shallow` | **2** | `ERROR … fatal: Not a valid object name c42d675…^{commit}` |
| M1 | `GIT_DIR` → repo *with* the pin, lane = repo *without* | `--selftest --lane /tmp/m1/lane` | **2** | `ERROR … Not a valid object name` |
| M2 | `GIT_OBJECT_DIRECTORY` → the pin's objects | same | **2** | `ERROR … Not a valid object name` |
| M3 | `GIT_ALTERNATE_OBJECT_DIRECTORIES` → the pin's objects | same | **2** | `ERROR … Not a valid object name` |

The `GIT_*` scrub at `:236-243` is real and load-bearing, not decorative: I removed the
`if not key.startswith("GIT_")` filter in a scratch copy and control 15 immediately broke —
`FAIL control: GIT_DIR override cannot mask an unreachable pin []`, exit 1. So the scrub is
genuinely exercised by a control, and it genuinely holds against `GIT_DIR`,
`GIT_OBJECT_DIRECTORY` and `GIT_ALTERNATE_OBJECT_DIRECTORIES` (M1/M2/M3 above: all still exit 2).

### 1.2 Default and `--readme` modes unchanged — **HOLDS**

Byte-identical behaviour against the base commit for the same input file:

```
python3 tools/check-readme-revisions.py --json --readme <same README>   # landed
python3 /tmp/rrc-base/tools/check-readme-revisions.py --json --readme <same README>  # base 4ad2683
→ JSON_IDENTICAL   (diff of the two JSON receipts is empty)
```
Text mode also identical (`README_MODE_IDENTICAL`; the only diff in the default-mode run was the
`readme <path>` echo line, because I ran the base copy from a different directory).

Exit-code semantics preserved exactly: clean → 0, finding present → 1 (both versions:
`NEW_DIRTY=1 OLD_DIRTY=1` on a duplicate-label fixture), missing file → 2, unreadable file → 2,
`--readme` pointing at a directory → 2, usage error → 2. `--json` receipt keys (`ok`, `findings`,
`warnings`, `labels`, `revision_lines`, `readme`, `sha256`) unchanged.

### 1.3 Controls 1–11 retained — **HOLDS**

Base control set (11 names, extracted from `git show 4ad2683:…`) vs landed (15). All 11 base names
are present in the landed file, plus 4 new seam controls (unreachable pin, git-free tree, shallow
clone, `GIT_DIR` override). The 11 retained controls produce identical verdicts and identical
finding detail. Selftest in the full clone: **15 PASS, 0 FAIL, 0 ERROR, exit 0**.

Note the one intentional output change: the base printed `selftest skips: 1` and `SKIP …` lines;
the landed tool prints neither. `reports/round-50/jj-colocation-probe.py:308` still scans for
`SKIP ` lines to build R3 evidence — that scan now finds nothing, which is correct (there are no
skips to find) and does not break the probe (verified below).

### 1.4 Full clone and shallow clone — **HOLDS**

```
/tmp/rrc-full   (git clone --no-hardlinks, checkout 1c779e4):  --selftest → exit 0, 15 PASS
/tmp/rrc-shallow (git clone --depth 1 file://…/kotodama-shokunin):
                                              --selftest → exit 2 (ERROR, pin unreachable)
```
The shallow-clone behaviour is the intended fail-closed one: the pinned `c42d675…` is genuinely
absent from a depth-1 clone (`git cat-file -e c42d675…^{commit}` → `fatal: Not a valid object name`),
so exit 2 with an explicit `ERROR` line is correct, not a regression. Contrast: the *base* tool
would have printed `SKIP` and exited 0 here.

### 1.5 Sibling probe corroboration — **HOLDS**

`python3 reports/round-50/jj-colocation-probe.py --tools-root .` in the full clone:
`JJ_COLOCATION_FALSE_NEGATIVES=0/3`, `JJ_COLOCATION_FALSE_POSITIVES=0/4`. R3 reads
`selftest exits 2 with the pin absent (fails closed)`; P3 reads `selftest exits 0 and PASSes the
control for pinned c42d675`.

### 1.6 Round-50 acceptance command — **HOLDS (in the default environment)**

`reports/round-50/separability/r50-manifest.json:36`:
```
sh -c "python3 -B tools/harness/receipt_guard.py --selftest >/dev/null && python3 -B tools/check-readme-revisions.py --selftest >/dev/null"
→ ACCEPTANCE_EXIT=0
```
Also runs green in place in the real lane (`REAL_LANE_INPLACE_EXIT=0`; the lane worktree stayed
clean for this file afterwards — `git status --short tools/check-readme-revisions.py` empty).

---

## 2. Finding A (severity: high) — the `GIT_*` scrub does **not** prevent an *enclosing
repository* from satisfying the pin, so the "lane's own object store" guarantee in the docstring
is false, and control 13 can invert into a false PASS

### Where

`tools/check-readme-revisions.py:246-254` (`_git_run`) — `git -C <lane> …` with only the *env*
scrubbed. `:470-477` — control 13, "git-free tree fails closed". Docstring `:42-46` and the
`_git_env`/`_git_run` docstrings `:237-239`, `:247-248` all assert the pin is read "in the lane's
own object store".

### The defect

The scrub removes `GIT_DIR`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES` and
friends from the *environment*. It does nothing about git's own **repository discovery**: `git -C
<dir>` walks *upward* from `<dir>` until it finds a `.git`. When the lane directory is not itself a
repository but is nested inside one, the pin is read from the **enclosing** repository's object
store — the exact thing the docstring promises cannot happen.

### Evidence

F1 — a git-free tree nested inside a repository that holds the pin resolves the pin anyway:
```
$ git -C /tmp/rrc-outer/sub/gf rev-parse --absolute-git-dir
/tmp/rrc-outer/.git
$ git -C /tmp/rrc-outer/sub/gf cat-file -e c42d675…^{commit} && echo RESOLVED
RESOLVED
```
Calling the landed `base_readme_verdict()` on that same git-free tree:
```
base_readme_verdict("/tmp/rrc-outer/sub/gf", BASE_COMMIT)
→ STATUS: PASS          # ← expected ERROR
→ DETAIL: [{"class":"REVISION-DUP","lines":[55,57]},{"class":"REVISION-STUB","lines":[55]}]
```
The verdict is computed from the *outer* repository's copy of `corpus/README.md`.

F2 — the sharpest form, and the one that matters for the claim's own words: the **default**
`--lane` (the tool's own parent directory) being a git-free tree nested inside a pinning repo
makes the whole selftest exit 0 while the lane has no object store at all:
```
$ cd /tmp/rrc-outer3/plain          # git-free; git -C walks up to /tmp/rrc-outer3/.git
$ git -C /tmp/rrc-outer3/plain rev-parse --absolute-git-dir
/tmp/rrc-outer3/.git
$ python3 tools/check-readme-revisions.py --selftest
PASS control: base c42d675 README flagged (r49 defect) [{"class":"REVISION-DUP",…}]
selftest: all checks passed
EXIT=0                    # ← GITFREE_DEFAULT_LANE_EXIT=0
```
The lane here holds *no* git objects and the pin is *not* in its store — yet control 9 PASSes and
the selftest reports green. The `ERROR`-on-unresolvable-pin contract is satisfied only
*accidentally*, when the ambient filesystem happens to place the lane outside any repository.

F3 — control 13 is the control that was supposed to catch this, and it inverts into a **false
PASS** whenever `TMPDIR` is inside a git work tree that holds the pin. `TemporaryDirectory()`
inherits `TMPDIR`, so the "git-free tree" it builds is not git-free — it inherits the enclosing
repository by upward discovery, and control 13's `status == "ERROR" and "unreachable" in detail`
assertion becomes unsatisfiable in a *false-positive-free but FAIL-producing* way, and the
enclosing repo's README findings leak into the detail string:
```
$ TMPDIR=/tmp/rrc-XXXX/tmpdir python3 tools/check-readme-revisions.py --selftest
FAIL control: git-free tree fails closed (never skips) [{"class":"REVISION-DUP",…,"lines":[55,57]},…]
selftest: FAILED
EXIT=1
```
The same failure reproduces with `TMPDIR=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo` and
with `TMPDIR=$PWD/.scratch` — and **that last one is the lane's own documented convention**:
- `tools/harness/round_runner_conformance.py:521` — `scratch = Path(os.environ.get("TMPDIR", ROOT / ".scratch"))`
- `corpus/knowledge/linguistics/register-strata-attestation.md:27` — *"Measured at write time with `export TMPDIR=$PWD/.scratch`"*
- `.ufo/waves/round-50/build/ScribeLesson.md:88`, `.ufo/waves/round-50/build/ReviewGuardSemantics.md:200` — same convention, this round
- `tools/gates/frozen/round-11/README.md:35` — the lane *knows* the hazard: *"`TMPDIR` must be outside the repo … the lane's usual `$PWD/.scratch` is inside it"*

Under the lane's own convention the round-50 acceptance command fails:
```
$ TMPDIR=$PWD/.scratch sh -c "python3 -B tools/harness/receipt_guard.py --selftest >/dev/null && python3 -B tools/check-readme-revisions.py --selftest >/dev/null"
ACCEPTANCE_SCRATCH_EXIT=1
```
The build wave itself flagged this as a known risk in
`.ufo/waves/round-50/build/ExecReadmeRev.md:65`: *"A TMPDIR nested inside a git work tree that
holds the pin would break control 13 (the pin would resolve). This holds here (`/tmp`, …)."*
That is a self-acknowledged precondition, not a fix — and the precondition is violated by the
lane's own `$PWD/.scratch` convention.

### Smallest fix

One line in `_git_run` (`:246-254`) — ceiling git's upward discovery at the lane's own parent so
the lane's store is the *only* candidate:

```python
def _git_run(lane, *args):
    env = _git_env()
    env["GIT_CEILING_DIRECTORIES"] = os.path.dirname(os.path.abspath(str(lane)))
    return subprocess.run(["git", "-C", str(lane), *args],
                          capture_output=True, env=env, timeout=30)
```

Validated on a scratch copy patched in-clone (`/tmp/rrc-XXXX/tools/check-readme-revisions.fixed.py`):

| Case | unpatched | patched |
|---|---|---|
| full clone, default TMPDIR | exit 0 | **exit 0** (unchanged) |
| `--lane` = real jj-colocated lane | exit 0 | **exit 0** (unchanged) |
| `--lane` = shallow clone | exit 2 | **exit 2** (unchanged) |
| `--lane` = git-free tree | exit 2 | **exit 2** (unchanged) |
| `TMPDIR=$PWD/.scratch` (lane convention) | **exit 1** | **exit 0** (fixed) |
| default `--lane` = git-free dir nested in a pinning repo | **exit 0 (false green)** | **exit 2** (fixed) |

The ceiling does not break the real lane: `GIT_CEILING_DIRECTORIES=/home/vgpnk/Projects/shokunin
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin cat-file -e c42d675…^{commit}` → OK.
The sibling probe already applies exactly this guard
(`reports/round-50/jj-colocation-probe.py:6`, `:90` — `GIT_CEILING_DIRECTORIES=SANDBOX_PARENT`); the
gate it measures does not.

Alternative, if the author prefers to keep the tool environment-free: assert the lane *is* a
repository before probing (`git -C lane rev-parse --absolute-git-dir`, and require the result to
be lane/`.git` or a lane-internal path), and treat a lane whose discovery walks upward as
`ERROR`.

---

## 3. Finding B (severity: medium) — an unreachable pin yields exit 1 in two of the new seam
controls instead of exit 2, because the ERROR-detail string does not contain the substring the
controls assert on

### Where

`tools/check-readme-revisions.py:463-468` (control 12) and `:471-477` (control 13) both assert
`status == "ERROR" and "unreachable" in detail`. The `ERROR` detail text is built in
`base_readme_verdict()` at `:285-291` (git's own stderr) and `:293-298` (the `OSError` path,
whose text is `"pinned BASE_COMMIT %s could not be read in %s: %r"` — note: **"could not be
read"**, not "unreachable").

### Evidence

With `git` absent from `PATH` (a perfectly ordinary CI/container condition — the tool is
"stdlib only" and shells out to `git` without checking availability):
```
$ PATH=/tmp/rrc-emptybin python3 tools/check-readme-revisions.py --selftest
ERROR control: base c42d675 README flagged (r49 defect) … could not be read in /tmp/rrc-XXXX: FileNotFoundError(2, 'No such file or directory')
FAIL control: unreachable base pin fails closed (never skips) … could not be read in /tmp/rrc-XXXX: FileNotFoundError(2, 'No such file or directory')
FAIL control: git-free tree fails closed (never skips) … could not be read in /tmp/tmpmarsp6nu: FileNotFoundError(2, 'No such file or directory')
ERROR control: shallow clone with unreachable pin fails closed (never skips) fixture could not be built: FileNotFoundError(2, 'No such file or directory')
ERROR control: GIT_DIR override cannot mask an unreachable pin fixture could not be built: FileNotFoundError(2, 'No such file or directory')
selftest: could not evaluate (ERROR)
EXIT=2
```
The aggregate exit is still 2 (the `errored` list is non-empty, `:411-414`), so the *overall*
fail-closed contract holds. But two controls print **`FAIL`** — semantically "a control assertion
did not hold", i.e. the tool's guarantee is broken — when the truth is "could not evaluate",
which is what `ERROR` exists for. A reader (or a CI log parser) sees a control *failure* where
there is only an environmental condition.

The same asymmetry applies to control 14 and 15's `error(name, "fixture could not be built: %r")`
paths (`:486-487`, `:509-510`): a missing `git` produces "could not be built", which is accurate,
but the two `check(...)`-based controls in the same file treat the identical condition as a
failure.

### Smallest fix

Do not key the assertion on a prose substring; key it on the status alone, and make the
`OSError` branch use the same "unreachable" wording so the two paths agree:

```python
# base_readme_verdict(), the OSError branch
return (name, "ERROR",
        "pinned BASE_COMMIT %s unreachable in %s: %r" % (base_commit, lane, exc))

# controls 12 and 13
check("control: …", status == "ERROR", detail)   # drop `and "unreachable" in detail`
```
(or keep the substring assertion and normalise the `OSError` message to contain "unreachable").

---

## 4. Residual risk / verification gaps

1. **`git` availability is assumed, never probed.** The tool shells out to `git` (`:249-254`)
   and only catches `OSError` at the `base_readme_verdict` level (`:291-299`). There is no
   preflight that reports "git is not installed" as a distinct, typed condition. Finding B is
   the visible symptom.
2. **`GIT_CEILING_DIRECTORIES` is not in the scrub's scope.** `_git_env()` (`:236-243`) strips
   every `GIT_*` variable — *including* a `GIT_CEILING_DIRECTORIES` the operator may have set
   deliberately to protect against exactly this. That is the right call for isolation, but it
   means the tool can never inherit the protection; it must set its own (Finding A's fix).
3. **`refs/jj/*` is not excluded from pin resolution.** `git cat-file -e <sha>^{commit}`
   resolves the pin from *any* reachable ref, and in the real lane the pin is carried by
   `refs/heads/main`, `refs/remotes/origin/main` **and** ~18 `refs/jj/keep/*` refs
   (`git for-each-ref --contains c42d675…` lists all of them). The claim's stated intent
   (per `.ufo/waves/round-50/build/ConnectSiblingJj.md:53`) was *"durable reachability
   (heads|tags|remotes, never `refs/jj`)"*. The landed implementation does **not** implement
   durable reachability — it implements *object existence*. A pin reachable only via
   `refs/jj/keep/*` (i.e. not landed on a branch) would still PASS control 9. I did not build a
   fixture for the jj-only-pin case (it would need a jj-colocated repo with the pin on a
   `refs/jj/keep/*` only), so this is **[INFERENCE] from the ref listing, not measured**.
4. **Control 13 is not hermetic by construction.** Even with Finding A's fix, control 13 depends
   on `TMPDIR` being outside every git work tree. The fix makes it *fail* correctly rather than
   *pass* incorrectly in that case, which is the right failure direction, but a belt-and-braces
   `git init` inside the temp tree (making it unambiguously a repo, not merely a non-repo) would
   remove the dependence entirely.
5. **`--readme` and `--selftest` are mutually exclusive but not enforced.** Passing both
   silently ignores `--readme` (exit 0, selftest output) — pre-existing behaviour, unchanged by
   this commit, and not a defect, but worth a note since `--readme` now takes a real path.
6. **Not verified:** the `receipt_guard.py` half of claim O is a sibling seat
   (`KotodamaR50-2.ReviewGuardCode-21` / `…GuardControls45-21`); I only exercised
   `receipt_guard.py --selftest` incidentally, via the manifest acceptance command, where it
   passed. The `tools/harness/receipt_guard.py` controls themselves are out of my scope.
7. **Not verified:** whether the `jj-colocation-probe.py` R3 leg would still report 0/3 after
   Finding A's fix. The probe already ceilings discovery at `/tmp`
   (`jj-colocation-probe.py:6`, `:90`), so its R3 fixture is already isolated — but I did not
   re-run the probe against a patched gate.

---

## 5. Bottom line

The **named** behaviour of claim O holds: the `SKIP` path is deleted, an unresolvable pin exits
**2** in every seam I could construct (bogus pin, git-free tree, nonexistent path, shallow clone,
`GIT_DIR`/`GIT_OBJECT_DIRECTORY`/`GIT_ALTERNATE_OBJECT_DIRECTORIES` masking), the `GIT_*` scrub is
load-bearing and verified against a mutated copy, default and `--readme` modes are byte-identical
to the base, all 11 prior controls are retained (15 PASS in the full clone), and the shallow clone
fails closed with an explicit `ERROR` rather than skipping.

The **stated** behaviour — *"resolves `<BASE_COMMIT>^{commit}` in the lane's own object store"*
(`:43-44`, `:237-239`, `:247-248`) — does **not** hold, because the scrub covers the environment
but not git's upward repository discovery. Under the lane's own documented `TMPDIR=$PWD/.scratch`
convention the round-50 acceptance command exits 1, and a git-free lane nested inside a pinning
repository makes the selftest exit 0 with a pin the lane does not hold. One line
(`GIT_CEILING_DIRECTORIES` = the lane's parent, mirroring what the sibling probe already does at
`jj-colocation-probe.py:90`) closes both, with the real lane and every other case unchanged.

Author-lane advice: land the one-line ceiling in `_git_run` (`:246-254`) and normalise the
`OSError` detail wording in `base_readme_verdict()` (`:293-298`); consider replacing control 13's
`TemporaryDirectory()` with an explicit `git init` so the control no longer depends on where
`TMPDIR` points. Do not treat the current selftest green as proof that the "lane's own object
store" guarantee is enforced — it is not.

**Tooling:** no installs. `git 2.56.0` (system), `python3` (system), `uv` not used. All
reproduction ran in private clones under `/tmp` (`GIT_CEILING_DIRECTORIES=/tmp` honoured for the
shared clone); the lane repo was only ever read (`git show`, `git cat-file`, `git for-each-ref`)
and was never mutated, staged, committed or checked out. Temporary clones deleted after the run.
