# ExecDCounterStub — round-71 claim D counter scaffold (wave 1)

Seat: `L1Kotodama71.ExecDCounterStub` (leaf executor). Draft only; the L1 freezes the final.

## Deliverable

- **Created/refined (draft):** `reports/round-71/accept-d.py` (untracked; 83 lines, `#!/usr/bin/env python3`).
- **Frozen file untouched:** `reports/round-69/accept-d.py` — bytes identical to revision 453676a2 (`sha256` `c41ffbc8244f5ed1acf35a82299e80c9a9a3cf988774dd068963b993bb4cf821` on both live tree and `git show 453676a2:reports/round-69/accept-d.py`).
- **Nothing else touched.** No tools installed (python3/git/tar already present; pacman untouched per gate).

## Behavior (as built)

- Imports the frozen round-69 counter via `importlib.util.spec_from_file_location` with an **absolute path** (`FROZEN = <lane>/reports/round-69/accept-d.py`); top-level code only, `main()` never runs at import.
- `--selftest`:
  1. Guard first: `git -C <lane> rev-parse --git-dir` (stdout/stderr to DEVNULL). On failure → prints `SELFTEST: COULD-NOT-EVALUATE (no git)`, exits **2**.
  2. Otherwise runs the frozen `selftest()` unchanged (same output, exit 0/1).
- `--root` / data predicate: delegates to the frozen `main()` with `sys.argv` rewritten to `[argv0, "--root", <root>]` so only frozen-known flags are forwarded; frozen output/exit semantics preserved byte-identically.
- `--lands`: accepted (reserved for receipt-protocol parity) but never forwarded — the frozen round-69 counter has no lands concept and would error on an unknown flag.
- No mutation of the lane, no network.

## Evidence — exact observed output

All run on 2026-10-25 from `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (A/B/D) and scratch (C).

### A. In-repo selftest (repo has `.git`)

```
$ python3 -B reports/round-71/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2
$ echo $?
0
```

### B. Frozen data predicate (unchanged contract)

```
$ python3 -B reports/round-69/accept-d.py --root .
LEG PASS STAMP self=c41ffbc8244f committed=c41ffbc8244f
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
$ echo $?
0
```

### C. No-git mode — git-archive copy of lane revision 453676a2

Scratch: `T=$(mktemp -d /tmp/d71-nogit-XXXXXX)`; `git archive 453676a2363c97e158cb112c9588906564d95a21 | tar -x -C "$T"` (archive of 453676a2 contains `reports/round-69/accept-d.py`; no `.git`; the round-71 counter file does not exist at that revision — see note below, so the draft counter was seeded at `$T/reports/round-71/accept-d.py`).

```
$ git -C "$T" rev-parse --git-dir
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
$ echo $?
128

$ cd "$T" && python3 -B reports/round-71/accept-d.py --selftest
SELFTEST: COULD-NOT-EVALUATE (no git)
$ echo $?
2
```

Matches claim-D target: no-git exit 2 + `COULD-NOT-EVALUATE`; in-repo exit 0 + `SELFTEST: 2/2`; frozen predicate 8/8 exit 0.

### D. Reserved `--lands` accepted without breaking delegation

```
$ python3 -B reports/round-71/accept-d.py --root . --lands 0000000000000000000000000000000000000000
LEG PASS STAMP self=c41ffbc8244f committed=c41ffbc8244f
... (same 8 PASS legs as B)
ACCEPT-D-69: PASS legs=8/8
$ echo $?
0
```

## Note for the L1 (claim command wiring)

The claim's counting command archives **453676a2** and runs `reports/round-71/accept-d.py` inside the extract, but that revision (round-70 records) does not contain the round-71 counter file — it is untracked today, so the verbatim command would end in file-not-found until the counter is committed. Proof C therefore seeds the draft counter into the extracted tree (the layout the freeze commit will produce). When the L1 freezes the counter into a commit, the archived command works unchanged if the archive revision is that freeze commit (or any descendant containing the file); a self-consistent revision reference is a freeze-time call.

## Risks / blockers

- None blocking. Guard is exactly `git -C <lane> rev-parse --git-dir`; a scratch dir **outside** any git tree is required for the no-git reproduction (an ancestor `.git` would make the guard pass) — `/tmp` used, verified RC=128 above.
- `--lands` is currently a no-op/reserved flag; it exists for argparse parity and will not affect verdicts.
