# Filler36 — round 71 wave 2: claim D counting command re-run in a fresh clone (variant 35)

Seat: sentinel / falsify. Findings only; nothing in the lane was written except this report.
Tools installed or updated: none.

## Verdict

**Claim D: PASS as declared.** The frozen counting command meets every target in a fresh clone at both lane HEADs that existed during this seat's run:

- the in-repo selftest prints `SELFTEST: 2/2`;
- the no-git leg prints `SELFTEST: COULD-NOT-EVALUATE (no git)` and `EXIT=2`;
- the frozen data predicate prints `ACCEPT-D-69: PASS legs=8/8` and exits 0.

**The no-git leg does not measure the clone (MEDIUM, reproducibility defect, new finding F1).** The command hardcodes the live lane path as its `tar` source. From a fresh clone, that leg therefore grades the live worktree, which carries 19,957 files that are not in the clone, rather than the bytes at HEAD.

## Command (frozen at 65ff151 and byte-identical at HEAD; `claims[id=D].counting_command`)

```
python3 -B reports/round-71/accept-d.py --selftest; bash -c 'T=$(mktemp -d); tar --exclude=.git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin -cf - . | tar -C $T -xf -; cd $T; python3 -B reports/round-71/accept-d.py --selftest; echo EXIT=$?'; python3 -B reports/round-69/accept-d.py --root .
```

The command was extracted from `reports/round-71/claims.json` with `json.load` and executed as `bash -c "<command>"`. Its bytes were not retyped.

## Run 1: fresh clone at 14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6

```
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/f36-clone.JqXz/k   # dirty=0
Python 3.14.8, git version 2.56.0
459cfa9da53fe3c4b44cfa5be4f82a2794298cc3b79c7f4e0f330f0977945930  reports/round-71/accept-d.py
c41ffbc8244f5ed1acf35a82299e80c9a9a3cf988774dd068963b993bb4cf821  reports/round-69/accept-d.py
```

Exact output:

```
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2
SELFTEST: COULD-NOT-EVALUATE (no git)
EXIT=2
LEG PASS STAMP self=c41ffbc8244f committed=c41ffbc8244f
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
```

The whole command exited with **0**. Per-leg exit codes, each run separately in the clone:

| Leg | Command | Exit |
|---|---|---|
| 1 | `accept-d.py --selftest` (in repo) | 0 |
| 2 | no-git copy taken from the **clone**, not from the hardcoded path | 2, `COULD-NOT-EVALUATE (no git)` |
| 3 | `round-69/accept-d.py --root .` | 0 |

## Run 2: fresh clone at baf3b6a65aef9bacc6319e8904c423b788dc8af6

During this seat's run, lane HEAD advanced through `ccadb59`, `c21213a`, `2166e45`, `cb77200` and `baf3b6a`. None of those commits touches `accept-d.py`, either counter, or `claims.json`; both counter sha256 values are unchanged. The second clone was clean (dirty=0), and its output was **byte-identical** to Run 1. The whole command again exited with **0**.

## Findings

### F1 (MEDIUM): the no-git leg grades the live worktree, not the measured revision

**Exploit path.** The fresh clone runs the frozen command. Leg 2 copies `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (the live, mutating worktree), not `$PWD`. The receipt's "no-git" result therefore depends on whatever is on the lane disk at that moment, including:
- ignored files;
- untracked files;
- other seats' half-written edits;
- a jj (jujutsu) store, which `--exclude=.git` does not strip.

**Evidence** (`LC_ALL=C` sorted `find -type f`, excluding `.git`, `.jj` and `__pycache__`):
- The live tree has 26,851 files and the clone has 6,894.
- 19,957 files exist only in the live tree; 19,934 of them are gitignored (`git check-ignore --stdin`).
- 0 files exist only in the clone.
- The live tar copy also carries `.jj/` with 4,814 files.
- At clone time, the live tree held untracked `reports/round-71/telemetry/measures-c.txt` and tracked files differing from the cloned HEAD (`corpus/lessons/round-71.md`, `reports/round-71/telemetry/census-end.txt`), because HEAD moved mid-run.

**Impact.**
- The leg passes today only because the `accept-d.py` bytes happen to agree between the live tree and HEAD. A dirty or uncommitted `accept-d.py` in the live tree would be graded instead of the committed bytes.
- On any other host or checkout path, the leg cannot run as written. Probe, with the source path replaced by `/nonexistent/kotodama-shokunin`:

  ```
  tar: /nonexistent/kotodama-shokunin: Cannot open: No such file or directory
  ...
  python3: can't open file '/tmp/tmp.Ivqo6KrIGx/reports/round-71/accept-d.py': [Errno 2] No such file or directory
  EXIT=2
  ```

  That probe exits 2, the same code as the target. Only the declared kill rule's `COULD-NOT-EVALUATE` line check separates it from a pass, so a grader that checks exit codes alone would false-pass it.

**Smallest remediation (for a later round; the frozen command stays frozen).** Source the no-git copy from the measured revision instead of a host path, for example `git archive <measured-rev> | tar -C $T -xf -`, or at minimum `tar -C "$PWD"`. Have the receipt print the source revision.

### F2 (LOW): the command's exit status masks legs 1 and 2

The three legs are joined with `;`, so the command's exit status is leg 3's alone. A failing leg 1 (`SELFTEST: 1/2`, exit 1) or leg 2 would still yield an overall exit of 0. The kill rule is enforced only by reading the output text.

**Smallest remediation:** emit an explicit per-leg `EXIT=` line for legs 1 and 3, or chain the legs with `&&`.

### Corroborated, already reported by other seats (independently reproduced here)

- **Nested no-git copy reproduces the V70-6 false red (RevCounterDM finding 2).**
  - Probe: `git -C $P init -q; tar --exclude=.git -cf - . | tar -C $P/sub -xf -; cd $P/sub; python3 -B reports/round-71/accept-d.py --selftest`.
  - Output: `GREEN FIXTURE: PASS (legs 8/8)` / `DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)` / `SELFTEST: 1/2`, with **exit 1**.
  - Cause: `_git_available()` uses `git -C LANE rev-parse --is-inside-work-tree`, and git discovery walks up into the parent repo. The "never a craft red" intent of the claim D surface fails for this layout. The declared command avoids it only because `mktemp -d` resolves to `/tmp`.
- **The receipt's no-git leg did not run the declared command (RevCounterDM).** `reports/round-71/telemetry/measures-d.txt` line 9 records `no-git leg (git archive of 1d1b432…)`. Correction (1) in `claims.json` replaced `git archive` with the `tar --exclude=.git` copy, so the receipt's output is not the declared command's output. The outcomes agree (exit 2, `COULD-NOT-EVALUATE`).

## Commands for a reviewer to re-check

```
C=$(mktemp -d); git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin $C/k; cd $C/k
bash -c "$(python3 -c 'import json;print([c["counting_command"] for c in json.load(open("reports/round-71/claims.json"))["claims"] if c["id"]=="D"][0])')"; echo VERBATIM_EXIT=$?
```

Scratch clones under `/tmp/f36-clone*` were removed. The `mktemp -d` directories created by the frozen command itself are left behind, because the command never cleans them up.
