# MutD — mutation probe of the round-71 claim-D counter (no-git guard)

Seat: L1Kotodama71.MutD (mutation-tester, round 71 wave 2). Lane untouched; probe ran in disposable scratch copies under `/tmp/mutd-r71`.

## Verdict

**KILLED** (both readings of "guard returns 0"), by the claim's no-git leg only.

**Tasking premise FALSE:** the mutant does **not** print `SELFTEST: 2/2` in a git-less copy. With the guard bypassed it prints `SELFTEST: 1/2` and exits 1. That is the V70-6 false red, the exact failure the guard exists to stop. The in-repo leg (`2/2`, exit 0) does not kill either mutant. Only the no-git leg does.

## Target under test

- `reports/round-71/accept-d.py`, sha256 `459cfa9da53fe3c4b44cfa5be4f82a2794298cc3b79c7f4e0f330f0977945930`. The lane copy is byte-identical to the scratch pristine (`cmp` OK).
- The frozen `reports/round-69/accept-d.py` was not mutated. Its sha256 is `c41ffbc8244f5ed1acf35a82299e80c9a9a3cf988774dd068963b993bb4cf821`.
- Claim D target, from `reports/round-71/claims.json`: in-repo exit 0 + `SELFTEST: 2/2`; no-git exit 2 + `COULD-NOT-EVALUATE`.

## Scratch copies

Built with the claim's own copy recipe:

```
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin; R=/tmp/mutd-r71
tar --exclude=.git -C $L -cf - . | tar -C $R/nogit -xf -   # git-less copy, no .git entry
tar -C $L -cf - . | tar -C $R/git -xf -                    # git-bearing copy
```

Checks on the copies:
- `git -C $R/nogit rev-parse --is-inside-work-tree` prints `fatal: not a git repository (or any parent up to mount point /)`.
- `$R/git` gives `true`.
- `/tmp` is not inside any repo.
- `GIT_DIR` and `GIT_WORK_TREE` are unset.

## Detector

The detector is the same bounded script for every state (`$R/detect.sh`), using the claim-D legs:

```
for d in git nogit; do
  out=$(cd $R/$d && timeout 120 python3 -B reports/round-71/accept-d.py --selftest 2>&1); rc=$?
  git leg  : PASS iff rc==0 && line == "SELFTEST: 2/2"
  nogit leg: PASS iff rc==2 && output contains "COULD-NOT-EVALUATE"
done
```

## Results

| State | Diff vs pristine | sha256 (both copies) | git leg | no-git leg | Verdict |
|---|---|---|---|---|---|
| pristine | — | `459cfa9d…5930` | EXIT=0, `SELFTEST: 2/2` → PASS | EXIT=2, `SELFTEST: COULD-NOT-EVALUATE (no git)` → PASS | baseline green (conclusive) |
| M1 guard always reports git | L55 `return rc == 0` → `return True` | `4c36dd6b…ffab` | EXIT=0, `SELFTEST: 2/2` → PASS | EXIT=1, `GREEN FIXTURE: PASS (legs 8/8)` / `DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)` / `SELFTEST: 1/2` → FAIL | **KILLED** (no-git leg) |
| M2 guard exits 0 | L80 `return 2` → `return 0` | `d2752a3a…ae07` | EXIT=0, `SELFTEST: 2/2` → PASS | EXIT=0, `SELFTEST: COULD-NOT-EVALUATE (no git)` → FAIL (rc≠2) | **KILLED** (no-git leg) |
| restored | none | `459cfa9d…5930` | EXIT=0, `SELFTEST: 2/2` → PASS | EXIT=2, `SELFTEST: COULD-NOT-EVALUATE (no git)` → PASS | restored green |

Control in the git-less copy, with the pristine frozen counter:
- `python3 -B reports/round-69/accept-d.py --selftest` prints `DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)` / `SELFTEST: 1/2`, EXIT=1. This reproduces V70-6.
- `python3 -B reports/round-69/accept-d.py --root .` prints `ACCEPT-D-69: PASS legs=8/8`, EXIT=0.

## Findings

1. **PASS (the guard is load-bearing).** Bypass the guard (M1) and the counter falls into the frozen `git show 793f797:SKILL.md` fallback. In the git-less copy that fallback seeds the do-nothing fixture from the live SKILL.md, which carries `### Registry correction chains`. The result is a false red: `1/2`, exit 1. The no-git leg catches it.
2. **PASS (the exit code is graded).** M2 keeps the `COULD-NOT-EVALUATE` text but exits 0. The no-git leg's `rc==2` check kills it, so the text alone cannot satisfy the target.
3. **Coverage finding: the in-repo leg is blind to both mutants.** Inside a working repo the guard is never entered. If the kill rule ran only `python3 -B reports/round-71/accept-d.py --selftest` in the repo, either mutant would survive. The kill rule as declared includes the no-git leg, so the claim holds. Do not drop or weaken that leg in any future rewrite of the counting command.
4. **Tasking expectation corrected.** "Mutant prints SELFTEST: 2/2 in a git-less copy" is not what happens. The observed output is `SELFTEST: 1/2`, exit 1 (M1). The mutant is still killed by the target, as the tasking expected.
5. **Not probed, outside this assignment.** No mutant reached the `git unavailable: …` branch, where `.git` exists but rev-parse fails.

## Restoration evidence

- The scratch counter was restored with `cp -p` from the saved pristine bytes after each mutant. Restored sha256 is `459cfa9da53fe3c4b44cfa5be4f82a2794298cc3b79c7f4e0f330f0977945930` in both copies, equal to the lane copy.
- The restored state re-ran the same detector green.
- Lane `git status --short` after the probe showed only other seats' untracked files (`.ufo/waves/round-71/w2/RevCensus.md`, `reports/round-71/telemetry/measures-c.txt`). This seat made no lane writes apart from this report.
- The scratch directory `/tmp/mutd-r71` is disposable and was removed after the report.

## Tooling

No installs or updates.
