# CritCa2 — attack on Ca2 (`reports/round-69/accept-ca.py`), round 69 residual verification

Seat: `L1Kotodama69.CritCa2`. Read-only on the lane. All counter runs were made in a fresh clone
`/tmp/CritCa2-r69` (lane tip `9e82c7b`, cloned from the lane; `git status --short` empty). The
fleet report was read at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md`
(clean in the fleet repo; it is committed at `cbc87da3`, unmodified since round 68). No lane
file other than this report was written; no git mutating command ran.

The counter's own frozen bytes were checked as well: `sha256(accept-ca.py) = 091074c5c054…405e`,
identical at `6a98d7d`, at the measured data land `e86ed3e`, and at HEAD, and identical to
`# counter sha256 (self)` in `reports/round-69/telemetry/final-measures-ca.txt`; `git log` shows
`accept-ca.py` was touched only by the declaration commit. The measurement is reproducible from
committed bytes; my clone run prints the same 8 LEG lines as the committed receipt.

## Verdict

| item | verdict | evidence |
|---|---|---|
| Frozen predicate: every leg PASS and `unannotated_mismatches=0` | **PASS** | `ACCEPT-CA-69: PASS legs=8/8`, `LEG PASS MISMATCHES live_mismatches=4 unannotated_mismatches=0`, exit 0 |
| Claim **as declared**, under its own frozen `kill_rule` | **FAIL** | `kill_rule` = "any declared pair that is live or uncovered -> the claim fails as declared"; the counter's own output marks **4 of 5 pairs `live=True`** (only DEADPOINTER is clean). The frozen rule is triggered. |
| Do-nothing reproduction: delete the live fleet LEGCOUNT correction row | **PASS** (counter detects) | `unannotated_mismatches=1`, `ACCEPT-CA-69: FAIL legs=6/8`, exit 1 |
| Do-nothing reproduction: stub-only correction rows (names only, no re-derivation) | **FAIL** (counter reaches 8/8) | `ACCEPT-CA-69: PASS legs=8/8` with the same 4 live mismatches; the frozen target is reachable by appending five one-line naming rows |
| `R68FROZEN` pins the crashed round-68 counter bytes | **PASS** (`accept-ca.py`) | live `a6d1c1c2…9925` == receipt `a6d1c1c2…9925` |
| `R68FROZEN` pins the *three* round-68 counters, as `claims.json` `freeze_rule` and the round-69 SCORECARD say | **FAIL** (scope) | Ca2's leg checks only `accept-ca.py` (1 of 3). Corrupting `accept-ca.py`'s sibling `accept-o.py` in a clone leaves Ca2 at 8/8. `accept-o.py`'s own `R68FROZEN` loops over all three and passes, so the lane-level freeze holds only when both counters run. |

The two verdicts are not in tension: the predicate passes mechanically, but the claim's own
pre-data kill rule fails it. `claims.json` was frozen at `6a98d7d`; the only later edit (`52b92a6`)
changed the O2 control text and wave counters, not the Ca2 entry (verified by `git show
6a98d7d:reports/round-69/claims.json`). The canonical judge must name which authority governs —
the counter's annotation-only closure, or the declared kill rule. As written, the kill rule wins.

## Item 1 — the five declared pairs, re-derived by hand

Base `793f7974`: `git cat-file -e 793f7974:reports/round-69/corrections-r68.md` → absent;
`git show 793f7974:SCORECARD.md | grep -c '9/10 legs PASS'` → 1; same for LOG.md → 1. The
"before" state (five pairs live, no annotation) is real.

Observations read from the committed receipts:
`reports/round-68/telemetry/final-measures-o.txt` has 9 leg lines, 8 PASS and 1 FAIL (EXEC);
`final-measures-ca.txt` carries the `NameError: name 'git_bytes' is not defined` traceback and
never prints `ACCEPT-CA-68: PASS`; `final-measures-c.txt` has 12 leg lines, 12 PASS.

| # | class | surface | filed text (live file) | receipt / observed | live? |
|---|---|---|---|---|---|
| 1 | LEGCOUNT | `SCORECARD.md` `^## Axes — round 68` | row 1318: `ACCEPT-O-68 9/10 legs PASS at A_c` | 9 legs, 8 PASS, 1 FAIL | **yes** (`hits=['9/10']`) |
| 2 | LEGCOUNT | `LOG.md` `^## Round 68` | line 4212: `ACCEPT-O-68 prints 9/10 legs PASS at A_c` | same | **yes** (`['9/10']`) |
| 3 | LEGCOUNT | `.ufo/reports/round-68/kotodama.md` (fleet) | line 10 `ACCEPT-O-68 prints 9/10 legs PASS`; line 29 `9/10 legs PASS, exit 1` | same | **yes** (`['9/10','9/10']`) |
| 4 | DEADPOINTER | same fleet report | line 35 `R68-M1..M8 (+M9 in LOG)`; line 11 `Ca fails as declared (R68-M9)` | no `R68-M9` row existed in `LOG.md` or `lessons/round-68.md`; the backfill row now exists in `lessons/round-69.md` `## Mistakes` (line 26) and LOG names it (4229, 4231) | no (`hits=none`) — see U5 |
| 5 | OVERREACH | `SCORECARD.md` round-68 section | row 1319: `\| calibration \| improved (claim Ca, records) \|` | receipt is a traceback, `ACCEPT-CA-68: PASS` absent | **yes** (`['calibration verdict 'improved' vs receipt FAIL']`) |

The counter's `EVAL` lines match this table exactly. The correction rows in
`reports/round-69/corrections-r68.md` name all five (class, surface) pairs and quote the right
filed text; the SCORECARD round-69 row is also honest where `claims.json` is not: it says
"0 unannotated (4 live mismatches remain)".

## Item 2 — do-nothing / tamper reproduction matrix

Five variants of the clone; each run
`python3 -B <variant>/reports/round-69/accept-ca.py --root <variant> --fleet-root /home/vgpnk/Projects/shokunin`.

| variant | operation | result | meaning |
|---|---|---|---|
| A | delete the fleet **LEGCOUNT** correction row (a live pair) | `hits=['9/10','9/10']`, `covered=False`, `unannotated_mismatches=1`, `FAIL legs=6/8`, exit 1 | **the required reproduction: deleting a live pair's annotation makes the zero fail.** The zero is not definitional for live mismatches. |
| B | delete `corrections-r68.md` entirely | `unannotated_mismatches=4`, `FAIL legs=2/8` | all four live pairs become unannotated |
| C | delete only the **DEADPOINTER** row (pair is clean) | `unannotated_mismatches=0`, `FAIL legs=7/8` | the `MISMATCHES` number alone does **not** count a missing row for a clean pair; only the per-leg PASS catches it (U6) |
| D | replace the corrections with five one-line **stub** rows naming class+surface (`\| LEGCOUNT \| SCORECARD.md \| x \| x \| x \|`, etc.) | `ACCEPT-CA-69: PASS 8/8`, `unannotated=0`, exit 0 | **a do-nothing seat that appends naming rows reaches the frozen target with the 4 mismatches still live.** The counter cannot distinguish a correction from a stub (same class of hole that forced O2 rev 1) |
| E | corrupt `reports/round-68/accept-o.py` (`printf '\n# corrupted\n' >>`) | Ca2 still `PASS 8/8` | Ca2's `R68FROZEN` does not pin the sibling counters (item 4) |

Green-control inspection (the `--selftest` green fixture, evaluated with `quiet=False`):
`GREEN FIXTURE: PASS (legs 8/8)` — with `live=True` on SCORECARD/LOG/fleet LEGCOUNT and on
OVERREACH. `build_fixture_root` copies the **live** SCORECARD.md, LOG.md, lessons and the live
fleet report (`real = "/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md"`) and
writes the same stub-shaped correction rows as variant D. The control's declared text ("a
fixture tree that satisfies the claim", `claims.json` `controls.green`) is therefore false under
the claim's `after` (U7): the fixture satisfies the annotation-only implementation, not the
claim's "every declared pair's observation is consistent". It is also not hermetic (hardcoded
absolute fleet path).

`--selftest` itself: `GREEN FIXTURE: PASS (8/8)`, `DO-NOTHING FIXTURE: FAIL (as required) (2/8)`,
`SELFTEST: 2/2`, exit 0 — the declared controls behave as written; the gap is what they cover.

## Item 3 — mismatch classes the five pairs do not cover (uncounted, not claimed as failures)

- **U1 — LOG overreach.** `LOG.md` round-68 entry says "**Claim Ca (calibration, records):
  author-side VERIFIED**" and enumerates legs ("SEQ legs + check-receipt-seq 14/14; ... QUOTES:
  26 gate ids ... 0 findings"), while the committed receipt crashed at D2 before those legs ran.
  The declared OVERREACH pair is SCORECARD only, and `detect_overreach` is shape-limited to lines
  starting `| calibration |`: `detect_overreach(LOG r68 section, "FAIL")` → `[]`. A
  (OVERREACH, LOG.md) pair would be structurally undetectable.
- **U2 — partial annotation.** The SCORECARD round-68 calibration row also claims
  "receipt-sequencing protocol re-proven (SEQ/FIXTURES legs; receipts stamped==evaluated in
  materialized clones)". The receipt proves the opposite (crash before SEQ/FIXTURES). The
  correction row names the verdict cell only; this sub-claim is not separately named.
- **U3 — the round-69 declaration itself.** `claims.json` Ca2 `after` says "every declared pair's
  observation is consistent **and** an appended correction row … exists". Four of five
  observations are not consistent. The SCORECARD round-69 row discloses this, but the frozen
  declaration is nowhere corrected (the correction file is round-68 surfaces only). This is the
  same OVERREACH class, on a round-69 surface, uncounted by the round-68 pairs.
- **U4 — counter-docstring contradiction.** The docstring states "A pair closes only when BOTH
  hold: the underlying observation is now consistent … AND an appended correction row … exists".
  The code closes LEGCOUNT/OVERREACH on the row alone (`remedy = is_covered`), and the measured
  8/8 is exactly the annotation-only closure. Under the docstring's rule the lane would score
  FAIL today. Two authorities for one rule.
- **U5 — DEADPOINTER is substring, not row.** `mistake_rows_exist` checks only that `R68-M<n>`
  occurs anywhere in LOG.md/lessons. Unit test: a temp root whose LOG.md contains only the
  narrative sentence "the missing R68-M9 row is backfilled" (no row) and empty lessons →
  `mistake_rows_exist(root, ['9']) == []` (resolved). In the live lane the row is in
  `lessons/round-69.md`, not in LOG.md, while the filed pointer says "+M9 **in LOG**"; the
  detector cannot tell a row from a mention (see also the appendix of `corrections-r68.md`,
  whose own table cell contains "R68-M9" and would satisfy the substring on its own).
- **U6 — `unannotated=0` is not coverage.** Variant C: one declared pair has no correction row
  and `unannotated_mismatches` is still 0 because that pair's observation is clean. The claim's
  target sentence ("0 unannotated mismatches over the 5 declared pairs") is met while a declared
  pair lacks its row; only the 8/8 leg conjunction carries that requirement.
- **U7 — green control circularity / non-hermetic** (item 2).
- **U8 — checked and consistent (no mismatch).** Round-68 coverage numbers re-derived from git:
  registry `756` at `99fae308` → `780` at `A_c 44c9cc28` → `782` at `A_ca 84418e0a`; knowledge
  files `241 → 242`; culture-material `34 → 35`. SCORECARD "ACCEPT-C-68 PASS 12/12" matches the
  receipt (12 legs, 12 PASS). Freshness claims no numbers (paused under round-11 L0), so there is
  nothing to mismatch.

## Item 4 — `R68FROZEN` against `sha256sum reports/round-68/accept-*.py`

```
515fa492aac176b62dc776c16777d6f9cf1750bb31b802cdecaa4121ac7bbf7d  reports/round-68/accept-c.py
a6d1c1c24e779817a3344b063054d3c10bc09fcf466b578f38ba8008c6fc9925  reports/round-68/accept-ca.py
f409096c9167989fb56ec2830e846c282201d37e5d6a6a1752e1697418a07fae  reports/round-68/accept-o.py
```

Receipt lines `# counter sha256 (self):` in `final-measures-{c,ca,o}.txt` are byte-equal to all
three. The crashed counter (`accept-ca.py`) is therefore genuinely pinned by Ca2's leg:
`LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77`. The **scope** is the gap: Ca2's
leg re-derives one counter, while `claims.json` `freeze_rule` and the SCORECARD round-69 text say
the leg "re-derives the three round-68 counters' sha256". `accept-o.py`'s `R68FROZEN` is the one
that loops over `R68_COUNTERS` (all three). Variant E shows Ca2 alone cannot notice a mutated
sibling.

## Findings, impacted axes, smallest safe correction

**F1 (blocks the claim, not the predicate).** The frozen `kill_rule` is "any declared pair that is
live or uncovered → the claim fails as declared". Four declared pairs are live in the counter's
own `EVAL` output and in the SCORECARD's own disclosure. The counter passes because its
implemented closure is annotation-only for LEGCOUNT/OVERREACH, which is not what the kill rule
says. Impacted axis: **calibration** (the round's Ca2 verdict, SCORECARD round-69 row, LOG round-69,
`corrections-r68.md`). **Smallest safe correction:** do not edit the frozen counter or
`claims.json`; record this as the round's next mistake row (`R69-M7` is free; R69-M1..M6 are
taken) and score Ca2 "not verified as declared" under its own kill rule unless the operator
rules the annotation-only closure authoritative. Append (append-only) one correction row for the
round-69 declaration stating the measured truth: 0 unannotated, **4 live**.

**F2 (instrument).** The docstring's "closes only when BOTH hold" is false of the code; the
annotation-only closure lets a stub set reach 8/8 (variant D). Impacted: calibration instrument
and its control set. **Correction for round 70 (not this round):** either require the observation
to be clean for closure, or write the docstring/claim to the annotation rule; make the
`DEADPOINTER` check row-shaped (`^\|\s*R68-M\d+\s*\|` or `^- R68-M\d+ \|`); make the
`MISMATCHES` count `live && !covered` explicit in the target sentence; add a stub-corrections
control to `--selftest`; generate the three surfaces and the fleet report inside the fixture
instead of copying the live tree and hardcoding the fleet path; and, if the "three counters"
sentence stays, check all three in Ca2's `R68FROZEN`.

**Not a defect:** the coverage numbers (U8) and the crashed-counter bytes (item 4) are correct.

## Commands actually run (tails)

```
$ sha256sum reports/round-69/accept-ca.py
091074c5c054e1ed214204efee8ac25d12c7697414f2e8ea16aac9ec483b405e
$ grep 'counter sha256 (self)' reports/round-69/telemetry/final-measures-ca.txt
# counter sha256 (self): 091074c5c054e1ed214204efee8ac25d12c7697414f2e8ea16aac9ec483b405e
$ python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
LEG PASS EVAL LEGCOUNT|SCORECARD.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|LOG.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|.ufo/reports/round-68/kotodama.md live=True covered=True remedy=True hits=['9/10', '9/10']
LEG PASS EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=False covered=True remedy=True hits=none
LEG PASS EVAL OVERREACH|SCORECARD.md live=True covered=True remedy=True hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG PASS MISMATCHES live_mismatches=4 unannotated_mismatches=0
ACCEPT-CA-69: PASS legs=8/8        (exit 0)
$ python3 -B reports/round-69/accept-ca.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 2/8)
SELFTEST: 2/2                       (exit 0)
variant A (fleet LEGCOUNT row deleted): LEG FAIL EVAL LEGCOUNT|.ufo/... live=True covered=False remedy=False hits=['9/10','9/10']
                                        LEG FAIL MISMATCHES live_mismatches=4 unannotated_mismatches=1
                                        ACCEPT-CA-69: FAIL legs=6/8   (exit 1)
variant B (corrections file deleted):   LEG FAIL MISMATCHES ... unannotated_mismatches=4 ... FAIL legs=2/8
variant C (DEADPOINTER row deleted):    LEG FAIL EVAL DEADPOINTER|.ufo/... live=False covered=False ...
                                        LEG PASS MISMATCHES live_mismatches=4 unannotated_mismatches=0 ... FAIL legs=7/8
variant D (5 stub rows):                ACCEPT-CA-69: PASS legs=8/8   (exit 0)
variant E (accept-o.py corrupted):      LEG PASS R68FROZEN live=a6d1c1c24e77 ... ACCEPT-CA-69: PASS legs=8/8
green fixture, quiet=False:             live=True on the 3 LEGCOUNT pairs and OVERREACH; ok=True
detect_overreach(LOG r68 section, FAIL) = []
mistake_rows_exist(narrative-only LOG, ['9']) = []
```

Tool installs/updates this seat: none.
