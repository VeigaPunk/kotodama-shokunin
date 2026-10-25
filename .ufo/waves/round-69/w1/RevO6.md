# RevO6 — attack: the OVERREACH detector of `reports/round-69/accept-ca.py`

Round 69, wave 1 (r69-v1), seat RevO6, axis calibration. Date 2026-10-24.
Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `793f79746712a79f915bb481215e54bbea8b5e7a`.
Read-only on production bytes: every mutation below is on a copy under `/tmp/rev-o6/`.
No tool installs were needed; `python3` on PATH was used as-is.

## Target

`detect_overreach` at `reports/round-69/accept-ca.py:165-176`. Its entire live
trigger is (line 173):

```python
if verdict.startswith("improved") and ca_verdict != "PASS":
```

where `verdict` is cell 3 of the `| calibration |` row inside the SCORECARD
section matched by `^## Axes — round 68` (claims.json `calibration_pairs`,
OVERREACH entry), and `ca_verdict` is `"PASS"` iff the committed receipt
`reports/round-68/telemetry/final-measures-ca.txt` contains the literal string
`ACCEPT-CA-68: PASS`, else `"FAIL"` (lines 120-126). That receipt **crashed**
(R68-M9 NameError, no verdict line), so `observed_ca_verdict` returns `FAIL`.

## Provenance

| artifact | sha256 (prefix) |
|---|---|
| lane `SCORECARD.md` = `/tmp/rev-o6/tree/SCORECARD.md` | `58017c9ff797f034` |
| lane `reports/round-69/accept-ca.py` = copy | `091074c5c054e1ed` |
| receipt `reports/round-68/telemetry/final-measures-ca.txt` | crashed receipt, 17 lines, ends `NameError: name 'git_bytes' is not defined` |
| receipt `reports/round-68/telemetry/final-measures-o.txt` | `o-legs=(8, 9)` per counter (9 LEG lines, EXEC FAIL) |

Fixture tree `/tmp/rev-o6/tree` mirrors the counter's own `build_fixture_root`
copies (counter + claims.json + round-68 counter + both round-68 receipts +
SCORECARD.md + LOG.md + lessons r68; fleet report copied from
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md`).
`corpus/lessons/round-69.md` was ABSENT (not landed yet) — recorded, not
fabricated. Mutated copies kept at `/tmp/rev-o6/SCORECARD.V*.md` (disposable;
every mutation is reproducible from the exact commands below).

## Baselines

Live lane (read-only run of the frozen counter):

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
```

Identical on the pristine /tmp copy (P0). `corrections-r68.md` does not exist
yet, so every leg shows `covered=False`; that is the pre-data state by design.
The detector DOES catch the real round-68 overreach: filed `improved` vs a
crashed (non-PASS) receipt.

Controls re-run: `--selftest` → `GREEN FIXTURE: PASS (legs 8/8)`,
`DO-NOTHING FIXTURE: FAIL (as required) (legs 2/8)`, `SELFTEST: 2/2`, exit 0.

## The assignment's two mutations (single-variable: verdict cell of the round-68 row only)

Anchor used for both (unique; the string `improved (claim Ca, records)` also
occurs in the round-64 row at SCORECARD:1256, so the `| R67-D1:` prefix
disambiguates):

```
python3 - <<'EOF'
import pathlib
p = pathlib.Path('/tmp/rev-o6/tree/SCORECARD.md')
t = p.read_text()
old = "| calibration | improved (claim Ca, records) | R67-D1:"
new = "| calibration | <VARIANT> (claim Ca, records) | R67-D1:"
assert t.count(old) == 1, "anchor count=%d" % t.count(old)
p.write_text(t.replace(old, new))
EOF
python3 -B /tmp/rev-o6/tree/reports/round-69/accept-ca.py --root /tmp/rev-o6/tree --fleet-root /tmp/rev-o6/tree/fleet
```

V1 `<VARIANT> = not verified as declared` (both runs below on the identical
method; only the leg lines that move are quoted, all other legs byte-identical
to P0):

```
V1 EVAL OVERREACH|SCORECARD.md live=False covered=False remedy=False hits=none
V1 MISMATCHES live_mismatches=4 unannotated_mismatches=4
V1 ACCEPT-CA-69: FAIL legs=2/8        (exit=1)
```

V2 `<VARIANT> = harmed`:

```
V2 EVAL OVERREACH|SCORECARD.md live=False covered=False remedy=False hits=none
V2 MISMATCHES live_mismatches=4 unannotated_mismatches=4
V2 ACCEPT-CA-69: FAIL legs=2/8        (exit=1)
```

### VERDICT lines for the assignment's two steps

- VERDICT: PASS — step 1 reproduced: rewording the verdict cell from
  `improved ...` to `not verified as declared ...` stops the OVERREACH
  live-detection (`live=True ... hits=["...vs receipt FAIL"]` → `live=False
  hits=none`; unannotated 5 → 4).
- VERDICT: FAIL — step 2 NOT reproduced: with `harmed`, the live detector does
  NOT still fire. V2 is behaviorally identical to V1 (`live=False hits=none`,
  unannotated=4). The only thing that "still fires" is the counter-level FAIL,
  and its cause is `covered=False` (no appended correction row) — a reason
  untouched by the verdict wording; the leg's `live=` field is the only signal
  distinguishing a silenced detector from a closed one. Root cause: the
  trigger is the single literal predicate `startswith("improved")`
  (accept-ca.py:173); no branch models any other verdict-vs-receipt
  contradiction, so `harmed` can never fire under any receipt.

## Completing probes

V3 — prefix escape (wording still asserts improvement, prefix moved off the
literal): `<VARIANT> = asserted improved` →
`EVAL OVERREACH|SCORECARD.md live=False covered=False remedy=False hits=none`,
unannotated 5 → 4. One word defeats live detection while the row still claims
the improvement.

V4 — receipt-side forge, pristine SCORECARD, one line appended to the /tmp copy
of `final-measures-ca.txt` (`t + "ACCEPT-CA-68: PASS\n"`):

```
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=PASS
LEG FAIL EVAL OVERREACH|SCORECARD.md live=False covered=False remedy=False hits=none
ACCEPT-CA-69: FAIL legs=2/8
```

The detector is silenced with the genuine `improved` filing, and R68FROZEN
stays green: it hashes `reports/round-68/accept-ca.py` against the sha line
*inside the same receipt* (lines 222-227) and never binds the receipt bytes
themselves. No leg of this counter integrity-locks the receipt the verdict is
read from.

H1/H2 — covered state, fixture built by the counter's own
`build_fixture_root(with_corrections=True)` from a pristine-receipt source
(first build accidentally inherited V4's forged receipt — rebuilt clean,
receipt grep `ACCEPT-CA-68` count = 0, `ca-verdict=FAIL`):

```
H1 (pristine 'improved' + corrections + R68-M9 backfill):
LEG PASS EVAL OVERREACH|SCORECARD.md live=True covered=True remedy=True hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG PASS MISMATCHES live_mismatches=4 unannotated_mismatches=0
ACCEPT-CA-69: PASS legs=8/8            (exit=0)

H2 ('harmed' + same covered fixture):
LEG PASS EVAL OVERREACH|SCORECARD.md live=False covered=True remedy=True hits=none
LEG PASS MISMATCHES live_mismatches=3 unannotated_mismatches=0
ACCEPT-CA-69: PASS legs=8/8            (exit=0)
```

H1 is the designed remedy path working: the real, live overreach is closed to
`unannotated=0` by the appended correction row. H2 shows that post-coverage the
verdict cell is wording-independent — the pair can never fail again once
covered, whatever the cell says.

## Findings

1. VERDICT: PARTIAL — the OVERREACH detector catches exactly its one declared
   real-world case (P0: filed `improved` vs the crashed round-68 receipt) and
   the appended-row remedy closes it (H1), but its live-detection is defeated
   by any verdict rewording (V1, V2, V3) or by a single forged PASS line in the
   receipt copy (V4, with R68FROZEN unaffected).
2. VERDICT: FAIL (as an attack expectation from the tasking) — `harmed` does
   not keep the live detector firing; it is indistinguishable from `not
   verified as declared`. The detector models one direction only:
   `improved ∧ ¬PASS`. A `harmed`/`not verified` verdict against a PASS
   receipt (overclaim in the other direction) can never fire either.
3. The live key comes from the same writer as the filing, so it is
   self-attestable: lane precedent already uses silencing verdicts
   (`not verified as declared` SCORECARD:1004, `unprovable` SCORECARD:1284,
   `not claimed; recorded` SCORECARD:1020+). V3 shows even
   `asserted improved` — an improvement claim — goes undetected.
4. Observed-receipt default: `observed_ca_verdict` reads `"PASS"` only on the
   literal string, so a crashed/verdict-less receipt silently reads as FAIL.
   That conflation is what makes P0's correct catch possible, but the OBSERVED
   leg cannot distinguish "crashed" from "explicit FAIL verdict".
5. Counter-level FAIL persistence across V1/V2 is the coverage machinery
   working as declared (kill rule: "any declared pair that is live or
   uncovered -> the claim fails"). Correct per the frozen claim; the hazard is
   that it makes a silenced detector look identical to an honest closure at
   the ACCEPT line — only the `live=` field tells them apart.

Advisory (no code changed; L1 owns integration): key the trigger on a closed
verdict vocabulary rather than one prefix (e.g. fire on `improved ∧ ¬PASS` and
on `harmed ∧ PASS`), and bind the receipt bytes with a digest leg the way
R68FROZEN binds the counter file.

VERDICT: DONE — all five pre-data runs, both controls, and both covered-state
probes executed with outputs above; nothing fabricated, no production file
touched.
