# MutO2 — mutation test of `reports/round-69/accept-o.py` (round-69 w1, O2 seat)

Scope (as assigned): copy the O2 acceptance counter to /tmp, mutate the FIXTURE
leg to accept `FIXTURE: 2/3` and the LANE leg to accept
`LANE: pending=1 missing_paths=0`, and show each mutant goes red against the
real lane tree. All mutation was done on /tmp copies; no production byte was
written, no git/jj state touched.

## Provenance

- Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated).
- Stated base `793f79746712a79f915bb481215e54bbea8b5e7a` verified read-only:
  `git cat-file -t` → `commit`; `git merge-base --is-ancestor <base> HEAD` →
  `base is ancestor of HEAD`.
- Observed working-copy HEAD (read-only `git log -1`):
  `6a98d7d042b6c58d2165773b1585069798111035` — "round-69: declaration + three
  NEW counters ...".
- Committed counter sha256 (self-consistent with the STAMP leg):
  `8724f9a08911661c099092606b7f058ba94a2ea7af00a7a26309d954e49ba121`.
- All scratch lives under `/tmp/mut-o2/` (disposable). Lane tree untouched.

## 0. Baseline — unmutated counter on the real lane tree

```
$ python3 reports/round-69/accept-o.py            # cwd = lane root
LEG PASS STAMP self=8724f9a08911 committed=8724f9a08911
LEG PASS TOOL tools/check-settlement-fixture.py
LEG PASS FIXTURE rc=0 True
LEG PASS NEGCASE PASS fixture-negative rc=0 pending=0 missing_paths=1
LEG PASS LANE rc=0 True
LEG PASS NEGPROBE missing_paths=1 present=True
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: PASS legs=7/7
exit=0
```

## 1. Mutant M1 — FIXTURE leg accepts `FIXTURE: 2/3`

Mutation (only change; made in `/tmp/mut-o2/m1/accept-o.py`):

```
$ diff reports/round-69/accept-o.py /tmp/mut-o2/m1/accept-o.py
122c122
<         res.add("FIXTURE", rc == 0 and "FIXTURE: 3/3" in out,
---
>         res.add("FIXTURE", rc == 0 and "FIXTURE: 2/3" in out,
```

Run against the real lane tree:

```
$ python3 -B /tmp/mut-o2/m1/accept-o.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG FAIL STAMP self=a9ab43df3710 committed=8724f9a08911
LEG PASS TOOL tools/check-settlement-fixture.py
LEG FAIL FIXTURE rc=0 True
LEG PASS NEGCASE PASS fixture-negative rc=0 pending=0 missing_paths=1
LEG PASS LANE rc=0 True
LEG PASS NEGPROBE missing_paths=1 present=True
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: FAIL legs=5/7
M1 exit=1
```

Red, exit 1. Note both FAIL lines: the mutated leg rejects the real tree's
`FIXTURE: 3/3` (detail prints `False`), **and** the STAMP leg independently
flags the tampered counter itself (self-hash `a9ab43df3710` ≠ committed
`8724f9a08911`).

## 2. Mutant M2 — LANE leg accepts `pending=1 missing_paths=0`

Mutation (only change; `/tmp/mut-o2/m2/accept-o.py`):

```
$ diff reports/round-69/accept-o.py /tmp/mut-o2/m2/accept-o.py
132c132
<         res.add("LANE", rc == 0 and "LANE: pending=0 missing_paths=0" in out,
---
>         res.add("LANE", rc == 0 and "LANE: pending=1 missing_paths=0" in out,
```

Run against the real lane tree:

```
$ python3 -B /tmp/mut-o2/m2/accept-o.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG FAIL STAMP self=e6576b159306 committed=8724f9a08911
LEG PASS TOOL tools/check-settlement-fixture.py
LEG PASS FIXTURE rc=0 True
LEG PASS NEGCASE PASS fixture-negative rc=0 pending=0 missing_paths=1
LEG FAIL LANE rc=0 True
LEG PASS NEGPROBE missing_paths=1 present=True
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: FAIL legs=5/7
M2 exit=1
```

Red, exit 1; the mutated LANE leg rejects the real tree's clean
`pending=0 missing_paths=0`; STAMP again flags the tampered counter.

## 3. Isolation runs — red is caused by the mutated leg, not by STAMP

The /tmp copies above also trip STAMP (by design). To prove the mutated leg's
semantics alone turn the counter red, I built self-consistent /tmp lane trees
(`iso1`, `iso2`: real tools/, round-68 counters+receipts, real `corpus/`) in
which the mutant *is* the committed copy at `reports/round-69/accept-o.py`, so
STAMP passes:

```
$ python3 -B /tmp/mut-o2/iso1/reports/round-69/accept-o.py --root /tmp/mut-o2/iso1
LEG PASS STAMP self=a9ab43df3710 committed=a9ab43df3710
LEG FAIL FIXTURE rc=0 True          # only M1's leg fails
ACCEPT-O-69: FAIL legs=6/7          (ISO1 exit=1)

$ python3 -B /tmp/mut-o2/iso2/reports/round-69/accept-o.py --root /tmp/mut-o2/iso2
LEG PASS STAMP self=e6576b159306 committed=e6576b159306
LEG FAIL LANE rc=0 True             # only M2's leg fails
ACCEPT-O-69: FAIL legs=6/7          (ISO2 exit=1)
```

(Other legs elided for width; full output captured in session. Both mutants
red 6/7 with STAMP green — the FIXTURE and LANE strings are load-bearing.)

## 4. Adversarial probes — would a mutant admit a defective tree?

- **M1 vs a broken-harness tree** (`iso1bad`: harness copy whose green fixture
  case is broken, printing `FIXTURE: 2/3`): still **red**, because the harness
  exits 1 when its selftest is 2/3 and the leg also requires `rc == 0`
  (`LEG FAIL FIXTURE rc=1 ...`, exit 1). The single string mutation is
  neutralized by the exit-code gate.
- **M2 vs an unsettled-chain tree** (`iso2bad`: S001 `mined` + used-by file
  present → harness prints `LANE: pending=1 missing_paths=0`, exit 1): still
  **red**, same reason (`LEG FAIL LANE rc=1 ...`, exit 1).
- **M3 (two-token mutant: string + rc gate)** — `/tmp/mut-o2/m3`: LANE leg
  changed to `rc in (0, 1) and "LANE: pending=1 missing_paths=0" in out`:

  ```
  $ python3 -B /tmp/mut-o2/iso3bad/reports/round-69/accept-o.py --root /tmp/mut-o2/iso3bad
  LEG PASS LANE rc=1 False
  ACCEPT-O-69: PASS legs=7/7
  exit=0
  ```

  Green on a tree with an unsettled chain — i.e. killing a leg requires
  mutating *both* its gates; each leg's string is load-bearing given the rc
  gate, and the rc gate is load-bearing given the string.

## 5. Counter's own controls (unmutated), re-run fresh

```
$ python3 -B reports/round-69/accept-o.py --selftest
GREEN FIXTURE: PASS (legs 7/7)
DO-NOTHING FIXTURE: FAIL (as required) (legs 6/7)
SELFTEST: 2/2
selftest exit=0
```

## Verdicts

- `VERDICT: PASS` — baseline: unmutated `accept-o.py` is green 7/7, exit 0, on the real lane tree.
- `VERDICT: PASS` — M1 (FIXTURE leg accepts `FIXTURE: 2/3`) goes red (FAIL legs=5/7, exit 1) on the real lane tree.
- `VERDICT: PASS` — M2 (LANE leg accepts `pending=1 missing_paths=0`) goes red (FAIL legs=5/7, exit 1) on the real lane tree.
- `VERDICT: PASS` — the red survives STAMP neutralization (isolation trees: 6/7, exit 1, only the mutated leg fails).
- `VERDICT: PASS` — bonus tamper-evidence: the STAMP leg independently detects both mutants on the real tree (self-hash mismatch), so a modified counter cannot quietly masquerade as the committed one.
- `VERDICT: PASS` — robustness: both legs are double-gated (exit code AND string); a single-string mutant stays red even on adversarial trees, and a leg only dies to a two-token mutation (demonstrated with M3 going green on an unsettled-chain tree).
- `VERDICT: NOT-EVALUATED` — mutation-testing of the other five legs (TOOL, NEGCASE, NEGPROBE, R68FROZEN, STAMP's own sensitivity) was out of the assigned scope and was not run.

## Bounds

Wrote exactly one file (this report). No edits to SKILL.md, corpus/**, LOG.md,
SCORECARD.md, reports/round-69/**, tools/**; no git/jj mutation (only read-only
`log`, `cat-file`, `merge-base --is-ancestor`, `status`, `sha256sum`, `diff`);
all mutants, doctored harnesses and fixture trees live under `/tmp/mut-o2/`.
No network fetching, no tool installs.
