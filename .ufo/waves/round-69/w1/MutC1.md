# MutC1 — mutation test of the DEADPOINTER remedy rule in `reports/round-69/accept-ca.py`

Round 69 v1 wave, kotodama lane, 2026-10-24. Read-only against the lane and fleet trees; all
mutation demonstrated under `/tmp/mutc1/` (disposable scratch). No production byte was edited.

## Target

`reports/round-69/accept-ca.py:252-254` — the remedy rule for the DEADPOINTER class:

```python
if cls == "DEADPOINTER":
    # the pointer must also resolve: an appended R68-M<n> row
    remedy = is_covered and not is_live
```

Mutation C1 (the task's prescription): make the remedy ignore whether the referenced row exists —
`remedy = is_covered` only. Applied to the COPY at `/tmp/mutc1/mutated/reports/round-69/accept-ca.py`;
original sha256 `091074c5c054e1ed214204efee8ac25d12c7697414f2e8ea16aac9ec483b405e`. Full diff
(saved at `/tmp/mutc1/mutation.diff`, pasted here since /tmp is disposable):

```diff
--- /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-ca.py	2026-10-24 23:15:43
+++ /tmp/mutc1/mutated/reports/round-69/accept-ca.py	2026-10-24 23:38:31
@@ -250,8 +250,9 @@
             live_count += 1
         is_covered = (cls, key) in covered
         if cls == "DEADPOINTER":
-            # the pointer must also resolve: an appended R68-M<n> row
-            remedy = is_covered and not is_live
+            # MUTATION C1: remedy = covered only; the referenced R68-M<n>
+            # row's existence is no longer required for the remedy to hold
+            remedy = is_covered
         else:
             # the filed bytes are frozen and append-only; the appended
             # correction row is the remedy
```

## Environments

- **Lane tree** (untouched): `--root /home/vgpnk/Projects/shokunin/kotodama-shokunin --fleet-root /home/vgpnk/Projects/shokunin`. Today `reports/round-69/corrections-r68.md` and `corpus/lessons/round-69.md` do not exist (the round's data is not landed), so `covered = ∅`.
- **Mirror tree** `/tmp/mutc1/lanemirror/`: copies of only the bytes the counter reads (claims.json, round-68 accept-ca.py + both final-measures receipts, SCORECARD.md, LOG.md, corpus/lessons/round-68.md), PLUS an appended `reports/round-69/corrections-r68.md` covering all five declared pairs, and deliberately NO backfill of the `R68-M9` row into LOG/lessons — the adversarial "correction row exists, pointer still dead" state. Fleet report copied verbatim to `/tmp/mutc1/lanemirror-fleet/.ufo/reports/round-68/kotodama.md`.

Commands: `python3 -B <counter> --root <tree> --fleet-root <fleet>` (and `--selftest`). Exit codes shown.

## A. Original counter vs the real lane tree (baseline truth today)

```
$ python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
LEG FAIL EVAL LEGCOUNT|SCORECARD.md live=True covered=False remedy=False hits=['9/10']
LEG FAIL EVAL LEGCOUNT|LOG.md live=True covered=False remedy=False hits=['9/10']
LEG FAIL EVAL LEGCOUNT|.ufo/reports/round-68/kotodama.md live=True covered=False remedy=False hits=['9/10', '9/10']
LEG FAIL EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=True covered=False remedy=False hits=['R68-M9']
LEG FAIL EVAL OVERREACH|SCORECARD.md live=True covered=False remedy=False hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG FAIL MISMATCHES live_mismatches=5 unannotated_mismatches=5
ACCEPT-CA-69: FAIL legs=2/8
EXIT=1
```

## B. Mutated counter vs the real lane tree

Output is byte-identical to A (`ACCEPT-CA-69: FAIL legs=2/8`, `unannotated_mismatches=5`, EXIT=1).
With `covered = ∅`, the mutated `remedy = is_covered` is indistinguishable from the original. The
mutation is **dormant on today's tree**; it activates exactly when the L1 lands the corrections file.

## C vs D — the discriminating scenario (mirror: corrections appended, R68-M9 still absent)

Side by side, the legs that differ; everything else identical (R68FROZEN/OBSERVED PASS; the three
LEGCOUNT legs and OVERREACH leg PASS via `remedy = is_covered` in both counters):

| Leg | C: ORIGINAL counter | D: MUTATED counter |
|---|---|---|
| `EVAL DEADPOINTER\|.ufo/reports/round-68/kotodama.md` | `FAIL live=True covered=True remedy=False hits=['R68-M9']` | `PASS live=True covered=True remedy=True hits=['R68-M9']` |
| `MISMATCHES` | `FAIL live_mismatches=5 unannotated_mismatches=1` | `PASS live_mismatches=5 unannotated_mismatches=0` |
| **Verdict** | **`ACCEPT-CA-69: FAIL legs=6/8` EXIT=1** | **`ACCEPT-CA-69: PASS legs=8/8` EXIT=0** |

Full original output (C):

```
$ python3 -B /home/.../reports/round-69/accept-ca.py --root /tmp/mutc1/lanemirror --fleet-root /tmp/mutc1/lanemirror-fleet
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
LEG PASS EVAL LEGCOUNT|SCORECARD.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|LOG.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|.ufo/reports/round-68/kotodama.md live=True covered=True remedy=True hits=['9/10', '9/10']
LEG FAIL EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=True covered=True remedy=False hits=['R68-M9']
LEG PASS EVAL OVERREACH|SCORECARD.md live=True covered=True remedy=True hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG FAIL MISMATCHES live_mismatches=5 unannotated_mismatches=1
ACCEPT-CA-69: FAIL legs=6/8
EXIT=1
```

Full mutated output (D):

```
$ python3 -B /tmp/mutc1/mutated/reports/round-69/accept-ca.py --root /tmp/mutc1/lanemirror --fleet-root /tmp/mutc1/lanemirror-fleet
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
LEG PASS EVAL LEGCOUNT|SCORECARD.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|LOG.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|.ufo/reports/round-68/kotodama.md live=True covered=True remedy=True hits=['9/10', '9/10']
LEG PASS EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=True covered=True remedy=True hits=['R68-M9']
LEG PASS EVAL OVERREACH|SCORECARD.md live=True covered=True remedy=True hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG PASS MISMATCHES live_mismatches=5 unannotated_mismatches=0
ACCEPT-CA-69: PASS legs=8/8
EXIT=0
```

The counter's verdict **changes**: FAIL→PASS on identical facts, where the only difference is
whether the counter still demands that the pointed-to `R68-M9` row actually exist.

## E. Do the committed pre-data controls catch the mutation?

```
$ python3 -B /tmp/mutc1/mutated/reports/round-69/accept-ca.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 2/8)
SELFTEST: 2/2
EXIT=0
```

Identical to the original's selftest (`GREEN 8/8`, `DO-NOTHING FAIL 2/8 as required`, `2/2`).
The controls are **blind to this mutation**: the DO-NOTHING fixture removes coverage entirely
(`covered=False`, so both remedy rules give `False`), and the GREEN fixture backfills the `R68-M9`
row (so `is_live=False` and both rules give `True`). Neither exercises the one case where the two
rules diverge: *correction row present, referenced mistake row still absent*.

## Which behaviour the lane depends on

The lane's Ca2 predicate (`unannotated_mismatches=0` printed by the MISMATCHES leg) depends on the
conjunct `remedy = is_covered and not is_live` for DEADPOINTER: **an appended correction row naming
(class, surface) does not by itself settle a mismatch — the referenced `R68-M<n>` row must also
exist somewhere in the lane's LOG.md or corpus/lessons/round-{68,69}.md.** Without that conjunct, a
later seat could satisfy Ca2 by appending the corrections row while the fleet report still points at
a mistake row that exists nowhere — a paper settlement of a live defect, accepted as `PASS 8/8`.
This is the same missing-used-by defect class that O2's settlement-fixture negative case exercises,
transplanted into the calibration counter. Corollary for the L1's integration: landing
`corrections-r68.md` alone leaves Ca2 red (run C); the `R68-M9` row must land in the lane's
LOG/lessons for the DEADPOINTER pointer to resolve.

## Findings

1. VERDICT: PASS — the DEADPOINTER remedy guard is live and load-bearing: mutation C1 flips the
   counter's verdict from `ACCEPT-CA-69: FAIL legs=6/8` to `ACCEPT-CA-69: PASS legs=8/8` on a
   tree where the correction row exists but the pointed-to `R68-M9` row does not (runs C vs D).
2. VERDICT: FAIL — the committed pre-data controls do not discriminate this mutation: the mutated
   counter's `--selftest` still prints `SELFTEST: 2/2` (run E). The GREEN/DO-NOTHING pair never
   builds the covered-but-still-live state; a third control with that shape would.
3. Observation (no verdict): the mutation is dormant on today's lane tree — runs A and B are
   byte-identical (`FAIL legs=2/8`, `unannotated_mismatches=5`) because
   `reports/round-69/corrections-r68.md` is not landed; the guard only matters once the Ca2 data
   lands, i.e. exactly at integration time.
4. Observation (no verdict): `git rev-parse HEAD` in the lane returned `6a98d7d042b6c58d2165773b1585069798111035`, while `claims.json` declares `base_revision: 793f79746712a79f915bb481215e54bbea8b5e7a` — consistent with the pre-data instruments being committed after the declaration, per the round brief. Not evaluated further (no scope).
5. Integrity note: all mutation was confined to `/tmp/mutc1/`; the lane tree, fleet tree and the
   committed counter (sha256 `091074c5…`) are unmodified. Mirror corrections rows were generated
   from `claims.json` in the same shape as the counter's own fixture generator.
