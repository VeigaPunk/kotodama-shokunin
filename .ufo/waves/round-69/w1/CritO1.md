# CritO1 — attack on claim O2's predicate (round 69, v1 wave, hyaku run 6)

- Seat: CritO1 (attack role, judged on operability). Date: 2026-10-24.
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, base revision
  793f79746712a79f915bb481215e54bbea8b5e7a. Production bytes untouched; every
  mutation below was done on copies under /tmp/r69crit-o1/.
- Question assigned: could a do-nothing control reach "every leg of
  reports/round-69/accept-o.py prints PASS"?
- Provenance (sha256, live lane): `reports/round-69/accept-o.py` =
  `8724f9a08911661c099092606b7f058ba94a2ea7af00a7a26309d954e49ba121`,
  `tools/check-settlement-fixture.py` =
  `f7adb4ba52e0db1a1c20ee33a5b52a0e2288b287866493ed43d800967712f7f8`,
  `tools/check-supersession-settlement.py` =
  `05214b3d7618b47c7ff9c8d9127647b7b7832c0ed748b3271b0266c7f343ad74`,
  `reports/round-69/claims.json` =
  `8880ebc1e5474d35c4616814e725f6efa524045582e2691d6ea664950528908d`.
- Copies: `rsync -a --exclude=.git --exclude=.jj --exclude=.scratch
  --exclude=out <lane>/ /tmp/r69crit-o1/tree{A,B,C}/`. The counter's seven
  legs read only `reports/round-68/`, `reports/round-69/`, `tools/` and
  `corpus/SOURCES.md` — all fully present in the copies (out/.scratch hold no
  bytes any leg reads).

## Baseline — committed instruments at the live lane (read-only)

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ python3 -B reports/round-69/accept-o.py --selftest; echo "exit=$?"
GREEN FIXTURE: PASS (legs 7/7)
DO-NOTHING FIXTURE: FAIL (as required) (legs 6/7)
SELFTEST: 2/2
exit=0
$ python3 -B reports/round-69/accept-o.py --root .; echo "exit=$?"
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

The selftest output is byte-identical to the accept-o section of the committed
receipt `reports/round-69/telemetry/controls.txt` (generated
2026-10-24T23:15:56-03:00) — the pre-data green/do-nothing controls reproduce
at the lane today.

## Probe A — do-nothing control, harness deleted (copy of the tree)

```
$ rm /tmp/r69crit-o1/treeA/tools/check-settlement-fixture.py
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-o.py \
    --root /tmp/r69crit-o1/treeA; echo "exit=$?"
LEG PASS STAMP self=8724f9a08911 committed=8724f9a08911
LEG FAIL TOOL tools/check-settlement-fixture.py
LEG FAIL FIXTURE tool absent
LEG FAIL NEGCASE tool absent
LEG FAIL LANE tool absent
LEG PASS NEGPROBE missing_paths=1 present=True
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: FAIL legs=3/7
exit=1
```

(The copy's own counter against itself gives the identical 3/7 FAIL.)
VERDICT: FAIL — deletion alone cannot reach the predicate; TOOL, FIXTURE,
NEGCASE and LANE all hard-fail on the missing file.

## Probe B — harness kept, negative case broken (copy of the tree)

One-line mutation in the COPY's `tools/check-settlement-fixture.py` (line 85):
`if create_usedby:` → `if True:` — the negative fixture can no longer omit the
used-by file, so the harness stops exercising the missing-used-by defect class
(the exact polarity the round-68 fixture got wrong).

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-o.py \
    --root /tmp/r69crit-o1/treeB; echo "exit=$?"
LEG PASS STAMP self=8724f9a08911 committed=8724f9a08911
LEG PASS TOOL tools/check-settlement-fixture.py
LEG FAIL FIXTURE rc=1 False
LEG FAIL NEGCASE no fixture-negative line
LEG FAIL LANE rc=1 True
LEG PASS NEGPROBE missing_paths=1 present=True
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: FAIL legs=4/7
exit=1

$ python3 -B /tmp/r69crit-o1/treeB/tools/check-settlement-fixture.py --selftest
PASS fixture-green rc=0 pending=0 missing_paths=0
FAIL fixture-negative rc=0 pending=0 missing_paths=0
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 2/3
exit=1
```

VERDICT: FAIL — a broken negative case cannot reach the predicate: FIXTURE
sees 2/3, NEGCASE finds no `PASS fixture-negative` line, and LANE fails even
though the tree scan itself is clean (`rc=1 True` — the leg requires rc=0, so
the broken fixture cases poison it; a cascading failure, not a lane defect).

## Probe C — strongest do-nothing: harness present, performs zero checks

The counter's FIXTURE/NEGCASE/LANE legs judge the harness only by its own
printed lines and exit code. Replacing the COPY's harness with a no-op that
merely prints the expected strings (full content below) tests whether the
predicate proves that any check actually ran:

```python
#!/usr/bin/env python3
import sys
print("PASS fixture-green rc=0 pending=0 missing_paths=0")
print("PASS fixture-negative rc=1 pending=0 missing_paths=1")
print("PASS fixture-pending rc=1 pending=1 missing_paths=0")
print("FIXTURE: 3/3")
if "--root" in sys.argv:
    print("LANE: pending=0 missing_paths=0")
sys.exit(0)
```

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-o.py \
    --root /tmp/r69crit-o1/treeC; echo "exit=$?"
LEG PASS STAMP self=8724f9a08911 committed=8724f9a08911
LEG PASS TOOL tools/check-settlement-fixture.py
LEG PASS FIXTURE rc=0 True
LEG PASS NEGCASE PASS fixture-negative rc=1 pending=0 missing_paths=1
LEG PASS LANE rc=0 True
LEG PASS NEGPROBE missing_paths=1 present=True
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: PASS legs=7/7
exit=0
```

VERDICT: PASS — an adversarial no-op harness reaches ACCEPT-O-69: PASS 7/7
without running a single fixture or scanning a single path.

## Leg-anchor analysis

| Leg | Anchor | Depends on the harness's self-report? |
|---|---|---|
| STAMP | sha256 of the counter vs its committed copy | no |
| TOOL | file existence | no |
| FIXTURE | harness output `FIXTURE: 3/3` + rc | **yes** |
| NEGCASE | harness output `PASS fixture-negative … missing_paths=1` | **yes** |
| LANE | harness output `LANE: pending=0 missing_paths=0` + rc | **yes** |
| NEGPROBE | base checker run by the counter itself on a fresh fixture | no |
| R68FROZEN | sha256 of the three round-68 counters vs their receipts | no |

NEGPROBE (accept-o.py:139-156) is the structural backstop: it re-derives the
missing-used-by defect class with the unmodified base checker, independent of
the harness — which is why the spoof cannot hide the defect class itself. But
no leg ties NEGPROBE's evidence to the harness: three of seven legs (four,
counting the harness-only part of LANE) are adjudicated on the harness's own
say-so.

## Answer to the assigned question

Could a do-nothing control reach "every leg of accept-o.py prints PASS"?

- **By omission (deletion): no — 3/7.** The predicate requires the claimed
  work to exist; the honest do-nothing control fails exactly as the committed
  receipt predicts.
- **By breakage (negative case disabled): no — 4/7.** FIXTURE, NEGCASE and
  LANE all fail; the missing-used-by class is still caught.
- **By spoofing (harness that prints PASS without checking): yes — 7/7.** The
  committed counter cannot distinguish the real harness from a no-op with the
  expected echo. The predicate is reachable without the *substance* of the
  claimed work, though not without a file literally named
  `tools/check-settlement-fixture.py` whose bytes were swapped — the freeze
  rule protects the counter, not the tool under test.

Findings for the L1 (integration owner):

- F1 (attack result): deletion and breakage do-nothing controls both fail as
  designed; the claim's negative case is genuinely exercised.
  VERDICT: FAIL (do-nothing cannot pass by omission or breakage).
- F2 (counter-strength finding): the spoof probe passes 7/7. Because the
  counter is frozen post-data, this cannot be patched this round; it is a
  named residual weakness, not a claim-killer — the harness bytes are
  committed at
  `f7adb4ba52e0db1a1c20ee33a5b52a0e2288b287866493ed43d800967712f7f8` and any
  post-data swap of the live tool is detectable against that digest today.
  A future NEW counter (not an edit of this one) could give FIXTURE/NEGCASE
  the NEGPROBE treatment: rebuild the harness's three cases in the counter and
  adjudicate on the base checker's output, not the tool's.
- F3 (corroboration): the live lane's `corpus/SOURCES.md` is currently settled
  (baseline LANE leg clean), so the LANE leg has real discriminative power
  right now; and R68FROZEN held in all three mutated trees, so the round-68
  freeze evidence is robust to anything done under tools/.

VERDICT summary:

- VERDICT: PASS — committed green control reproduces (selftest 2/2, counter 7/7
  at the live lane, byte-identical to controls.txt).
- VERDICT: FAIL — deletion do-nothing reaches the predicate (3/7).
- VERDICT: FAIL — broken-negative-case do-nothing reaches the predicate (4/7).
- VERDICT: PASS — spoofed no-op harness reaches the predicate (7/7): the
  predicate is spoofable, though not reachable by any honest do-nothing
  control.

Reproduction (all scratch under /tmp, disposable):

```
rsync -a --exclude=.git --exclude=.jj --exclude=.scratch --exclude=out \
  /home/vgpnk/Projects/shokunin/kotodama-shokunin/ /tmp/r69crit-o1/treeA/
rm /tmp/r69crit-o1/treeA/tools/check-settlement-fixture.py
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-o.py \
  --root /tmp/r69crit-o1/treeA
```

(Probes B and C as documented above; trees left in place for inspection.)
