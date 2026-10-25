# RevCounterDM — round 71 wave 2 — claim D counter (reports/round-71/accept-d.py)

Seat: falsify / reviewer. Lane HEAD `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`. All runs were in a
fresh clone at `/tmp/revdm-2qEk/clone` (`git clone -q <lane> clone`); no lane bytes were written
except this report. Counter sha256 `459cfa9d…5930` matches `measures-d.txt`; frozen
`reports/round-69/accept-d.py` sha256 `c41ffbc8…f821`, unchanged vs `453676a2`
(`git diff --quiet 453676a2 HEAD -- reports/round-69/accept-d.py` → UNCHANGED).

## Verdict on the declared predicate (ACCEPT-D-71): PASS (0/2/0 reproduced)

| Leg | Command (cwd) | Output | Exit | Target |
|---|---|---|---|---|
| in-repo | `python3 -B reports/round-71/accept-d.py --selftest` (clone, .git present) | `GREEN FIXTURE: PASS (legs 8/8)` / `DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)` / `SELFTEST: 2/2` | 0 | PASS |
| no-git | `tar -C clone --exclude=.git -cf - . \| tar -C nogit -xf -; cd nogit; python3 -B reports/round-71/accept-d.py --selftest` | `SELFTEST: COULD-NOT-EVALUATE (no git)` (stdout) | 2 | PASS |
| frozen data | `python3 -B reports/round-69/accept-d.py --root .` (clone) | 8× `LEG PASS …`, `ACCEPT-D-69: PASS legs=8/8` | 0 | PASS |

Supporting runs (all as expected):
- Frozen data predicate in the git-less copy: `ACCEPT-D-69: PASS legs=8/8`, exit 0.
- New counter data path `reports/round-71/accept-d.py --root .` in the git-less copy: byte-identical 8/8 output, exit 0; `--lands HEAD` is accepted and not forwarded (exit 0).
- `git archive HEAD` export: `SELFTEST: COULD-NOT-EVALUATE (no git)`, exit 2.
- `GIT_DIR=/nonexistent` with .git present: `SELFTEST: COULD-NOT-EVALUATE (git unavailable: fatal: not a git repository: '/nonexistent')`, exit 2.
- git binary absent from PATH: `SELFTEST: COULD-NOT-EVALUATE (git unavailable: [Errno 2] No such file or directory: 'git')`, exit 2.
- Run from cwd `/` against the clone path: `SELFTEST: 2/2`, exit 0 (LANE comes from `__file__`).
- Baseline false red confirmed: frozen `reports/round-69/accept-d.py --selftest` in the git-less copy → `DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)`, `SELFTEST: 1/2`, exit 1.

## Findings (by severity)

### MEDIUM-1 — The guard tests "inside some work tree", not "can produce 793f797:SKILL.md"; the false red survives in two realistic layouts

`reports/round-71/accept-d.py:51-57` (`_git_available`) uses `git -C LANE rev-parse --is-inside-work-tree`.
The frozen fixture builder (`reports/round-69/accept-d.py:203-210`) still silently swallows any
`git show 793f797:SKILL.md` failure and falls back to the live, table-carrying SKILL.md. So
whenever the probe says yes but the show fails, the old false red returns with exit 1 — the
exact outcome the claim surface (`claims.json:47`) says can never happen ("never a craft red").

Reproductions:
1. **Shallow clone** (`.git` present, 793f797 absent):
   `git clone -q --depth 1 file://<lane> shallow; cd shallow; python3 -B reports/round-71/accept-d.py --selftest`
   → `fatal: Not a valid object name 793f797` (from `git cat-file -t`), then
   `DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)` / `SELFTEST: 1/2`, **exit 1**.
   Shallow clones are the default in many CI systems (e.g. `actions/checkout` uses depth 1).
2. **Git-less copy nested inside an unrelated work tree** (`.git` absent from the lane):
   `git -C parent init -q; tar … --exclude=.git | tar -C parent/lane -xf -; cd parent/lane; python3 -B reports/round-71/accept-d.py --selftest`
   → `rev-parse --is-inside-work-tree` = `true` (toplevel `/tmp/revdm-2qEk/parent`), then
   `SELFTEST: 1/2`, **exit 1**. On this host both `/home/vgpnk` and
   `/home/vgpnk/Projects/shokunin` are git work trees (`git -C … rev-parse --show-toplevel`
   returns each), so a `tar --exclude=.git` copy placed anywhere under `$HOME` reproduces this
   [INFERENCE: not run under $HOME to avoid writing outside the seat's scope; mechanism proven by the synthetic parent].
   The declared counting command passes only because `mktemp -d` resolves to `/tmp`, which
   is not inside a git tree; with `TMPDIR` under `$HOME` the declared no-git leg would exit 1.

Fix direction (for the lane owner; not applied): probe the exact object the frozen selftest
needs, e.g. `git -C LANE cat-file -e 793f797^{commit}` (fails on both layouts above; succeeds
in the full clone), and/or require `rev-parse --show-toplevel` == LANE. Then grade a missing
commit as `COULD-NOT-EVALUATE`.

Scope note: the declared target legs and kill rule do not include these layouts, so ACCEPT-D-71
as frozen still PASSes. What is falsified is the surface claim's guarantee ("when the object store
is genuinely absent … never a craft red") and the docstring at `accept-d.py:44-49` ("Only a genuine
absence of the object store … is graded as `no git`").

### LOW-1 — The measured no-git leg did not use the declared method

`claims.json:51` and correction (1) at `claims.json:56` declare the no-git leg as
`tar --exclude=.git` of the measured worktree. `reports/round-71/telemetry/measures-d.txt:9` records
`no-git leg (git archive of 1d1b432…)`. The outcomes match (I re-ran both: exit 2 with the
`(no git)` line), but the receipt documents a different command than the frozen counting command.

### LOW-2 — On its own, the no-git leg's exit code cannot tell the target apart from a missing file

`telemetry/controls-d.txt:3`: on the base tree the counter does not exist, so Python exits **2**
(`can't open file … [Errno 2]`). I re-ran this on a `git archive b94a543c` → exit 2. That is the same
exit code as the target. The control is only rejected because the `COULD-NOT-EVALUATE` line is
missing (the kill rule requires both, so the predicate holds). Any re-grader who checks only `EXIT=2`
would wrongly pass the do-nothing control.

## Residual risk / verification gaps
- The tar copy and archive runs were on `/tmp` (xfs, a separate filesystem from `/home` on btrfs). Git's discovery stopped at the filesystem boundary, so the git-less result there does not depend on any parent repo.
- I did not test a worktree created with `git worktree add`, where `.git` is a file rather than a directory. The `os.path.exists(".git")` branch would treat it as present, which is correct for messages.
- Tool installs/updates: none.
