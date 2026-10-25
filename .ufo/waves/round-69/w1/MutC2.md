# MutC2 — mutation test of the OBSERVED leg of reports/round-69/accept-ca.py

Seat: kotodama round-69 wave-1 leaf (judged axis: calibration). Read-only on
production bytes; all mutation work done on a /tmp copy.

## Method

1. Ran the committed counter as-is against the lane (baseline).
2. Copied `reports/round-69/accept-ca.py` to `/tmp/mut-ca/accept-ca-mut.py`
   (sha256 of the copy before mutation matched the committed file:
   `091074c5c054e1ed214204efee8ac25d12c7697414f2e8ea16aac9ec483b405e`).
3. Mutated ONLY `observed_o_legs()` to hard-code `(9, 9)` instead of deriving
   the pair from `reports/round-68/telemetry/final-measures-o.txt`
   (mutated copy sha256 `066dc3dda79b41478b641bc22553666fc19b49cd3d0e29a67c7be76d2bda356c`;
   `diff -u` against the committed file shows that one function is the entire delta).
4. Ran the mutated copy against the lane root and diffed line-by-line.
5. Built a /tmp probe fixture (`/tmp/mut-ca/probe/`) whose filed surface claims
   `9/9 legs PASS` and whose tree carries NO round-68 receipt — the scenario
   where the observed pair matters for the LEGCOUNT verdict — and ran both
   counters on it.

The mutation (entire delta of the /tmp copy):

```python
def observed_o_legs(root):
    """MUTATION (MutC2): observed legs hard-coded to (9, 9) — the receipt is
    never read, so the LEGCOUNT detector compares filed claims against an
    invented observation instead of the committed round-68 bytes."""
    return (9, 9)
```

## Outputs

### Baseline — committed counter, lane root

```
$ python3 reports/round-69/accept-ca.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
LEG FAIL EVAL LEGCOUNT|SCORECARD.md live=True covered=False remedy=False hits=['9/10']
LEG FAIL EVAL LEGCOUNT|LOG.md live=True covered=False remedy=False hits=['9/10']
LEG FAIL EVAL LEGCOUNT|.ufo/reports/round-68/kotodama.md live=True covered=False remedy=False hits=['9/10', '9/10']
LEG FAIL EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=True covered=False remedy=False hits=['R68-M9']
LEG FAIL EVAL OVERREACH|SCORECARD.md live=True covered=False remedy=False hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG FAIL MISMATCHES live_mismatches=5 unannotated_mismatches=5
ACCEPT-CA-69: FAIL legs=2/8
exit=1
```

### Mutated copy — lane root

```
$ python3 /tmp/mut-ca/accept-ca-mut.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(9, 9) ca-verdict=FAIL
LEG FAIL EVAL LEGCOUNT|SCORECARD.md live=True covered=False remedy=False hits=['9/10']
LEG FAIL EVAL LEGCOUNT|LOG.md live=True covered=False remedy=False hits=['9/10']
LEG FAIL EVAL LEGCOUNT|.ufo/reports/round-68/kotodama.md live=True covered=False remedy=False hits=['9/10', '9/10']
LEG FAIL EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=True covered=False remedy=False hits=['R68-M9']
LEG FAIL EVAL OVERREACH|SCORECARD.md live=True covered=False remedy=False hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG FAIL MISMATCHES live_mismatches=5 unannotated_mismatches=5
ACCEPT-CA-69: FAIL legs=2/8
exit=1
```

Complete diff of the two runs:

```
2c2
< LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
---
> LEG PASS OBSERVED o-legs=(9, 9) ca-verdict=FAIL
```

On the live lane tree the LEGCOUNT live/uncovered lines are byte-identical:
the filed surfaces claim `9/10 legs PASS` (SCORECARD.md:1318, LOG.md:4212,
fleet `.ufo/reports/round-68/kotodama.md:10` and `:29`), i.e. pair (9, 10),
which mismatches BOTH the true (8, 9) and the invented (9, 9) — so all three
LEGCOUNT pairs stay live and uncovered under either observation.

### Probe — filed claim equals the invented pair (9/9), receipt absent

Fixture: `/tmp/mut-ca/probe/` with `surface.md` = `ACCEPT-O-68: 9/9 legs PASS.`
and a one-pair `claims.json`; deliberately no `reports/round-68/**` receipt.

```
=== TRUE counter on probe (receipt absent -> derived obs_o=None) ===
LEG FAIL R68FROZEN live=none recorded=none
LEG FAIL OBSERVED o-legs=None ca-verdict=None
LEG FAIL EVAL LEGCOUNT|probe-surface surface unreadable
LEG FAIL MISMATCHES live_mismatches=1 unannotated_mismatches=1
ACCEPT-CA-69: FAIL legs=0/4
exit=1

=== MUTATED counter on probe (observed hard-coded (9,9)) ===
LEG FAIL R68FROZEN live=none recorded=none
LEG FAIL OBSERVED o-legs=(9, 9) ca-verdict=None
LEG FAIL EVAL LEGCOUNT|probe-surface live=False covered=False remedy=False hits=none
LEG PASS MISMATCHES live_mismatches=0 unannotated_mismatches=0
ACCEPT-CA-69: FAIL legs=1/4
exit=1
```

Here the LEGCOUNT live/uncovered output genuinely changes: `surface
unreadable` / `unannotated_mismatches=1` (true) collapses to `live=False
hits=none` / `unannotated_mismatches=0` (mutated) — a false-clean MISMATCHES
PASS. The mutation kills two guards at once: `observed_o_legs` can never
return None, so the `surface unreadable` EVAL path is unreachable, and any
filed claim matching the invented pair reads as consistent and drops out of
the unannotated count even though the receipt is gone. The pair still fails
on `covered=False` (no correction row), so the leg stays red — the false
clean shows up specifically in the MISMATCHES count, the number claim Ca2's
predicate keys on.

## The true (pass, total) pair, from the committed bytes

`reports/round-68/telemetry/final-measures-o.txt` (committed receipt), the 9
lines matching `^([A-Z0-9_]+)\s+(PASS|FAIL)\b`:

```
7:STAMP PASS stamped=44c9cc28 evaluated=44c9cc28 equal=True tree=026d342b dirty_tracked=False
8:SELFTEST PASS exit=0 count=True
9:DIFF PASS status=A
10:SHA PASS live=05214b3d7618
11:PENDING PASS exit=0 summary=pending=0 chains=47 usedby_paths=709 missing_paths=0
12:LEDGER PASS exit=0 findings=0 missing=[] dup=[] extra=2
13:EXEC FAIL base_pending_fail=True lands_pass=False
14:MUT PASS bad=[]
15:TOPO PASS parent=cb2f8caf declaration=cb2f8caf
```

Re-derivation: `total = 9` (`grep -cE '^[A-Z0-9_]+[[:space:]]+(PASS|FAIL)\b'`),
`pass = 8` (`grep -cE '^[A-Z0-9_]+[[:space:]]+PASS\b'`), EXEC is the single FAIL.

**True (pass, total) = (8, 9).** This is exactly what the unmutated counter
printed (`o-legs=(8, 9)`), i.e. the OBSERVED leg's derivation is faithful to
the committed bytes.

## Verdicts

- VERDICT: PASS — the mutation run reproduces every LEGCOUNT verdict on the
  live lane tree unchanged (all three pairs live, uncovered: claims are 9/10,
  mismatching both (8, 9) and the invented (9, 9)); the only output delta is
  the OBSERVED leg's detail line.
- VERDICT: PASS — the probe proves the OBSERVED leg is load-bearing: with the
  observation hard-coded, a filed `9/9` claim and an unreadable receipt yield
  `live=False hits=none` and a false `MISMATCHES ... unannotated_mismatches=0`
  PASS, where the true counter prints `surface unreadable` and
  `unannotated_mismatches=1`. The LEGCOUNT detector's live/uncovered output
  does depend on the derived pair; on current data the 9/10 filed claims mask
  it.
- VERDICT: PASS — true pair stated from committed bytes: **(8, 9)** (8 PASS of
  9 legs; EXEC FAIL), matching the unmutated counter's derivation.
- Baseline (pre-data) counter state, unchanged by this seat: ACCEPT-CA-69 FAIL
  legs=2/8, live_mismatches=5 unannotated_mismatches=5 — consistent with the
  declared "before" (three classes over five pairs, corrections not yet
  appended).

Bounds kept: only this report file and /tmp scratch written; lane `git status
--porcelain` after all runs shows only pre-existing untracked wave files, no
modifications; no git/jj mutating commands; no network fetches.
