# RevO5 — attack on the DEADPOINTER detector of `reports/round-69/accept-ca.py`

Round 69 wave 1 (hyaku run 6), 2026-10-24. Lane base `793f79746712a79f915bb481215e54bbea8b5e7a`.
Scope: calibration. All mutation demonstrated on copies under `/tmp/ca69-attack`;
the lane tree and the fleet repo were never written (integrity evidence at the end).

## The detector under attack

`mistake_rows_exist()` (reports/round-69/accept-ca.py:129) concatenates
`LOG.md`, `corpus/lessons/round-68.md`, `corpus/lessons/round-69.md` from the
`--root` tree and declares id `R68-M<n>` alive iff the raw substring
`"R68-M<n>"` occurs anywhere in that concatenation — no row shape, no table
section, no word boundary. `detect_deadpointer()` (accept-ca.py:155) collects
ids from the filed fleet report via `R68-M(\d+)` and `+M(\d+)\s+in\s+LOG`, and
the DEADPOINTER leg's remedy is `covered AND NOT live` (accept-ca.py:254).

Baseline state (verified at the lane, read-only):

```
$ python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
LEG FAIL EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=True covered=False remedy=False hits=['R68-M9']
...
ACCEPT-CA-69: FAIL legs=2/8
```

The filed fleet report points at R68-M9 twice (`R68-M9` on its line 11;
`+M9 in LOG` on its line 35); lane `LOG.md` has no `R68-M9`, the round-68
lesson carries only M1–M8, `corpus/lessons/round-69.md` does not exist yet —
so `R68-M9` is the one live dead pointer.

## Method

Driver `/tmp/ca69-attack/attack.py` (scratch, not lane bytes): loads the
counter as a module, builds per-scenario fixture trees with the counter's own
`build_fixture_root()` (copies of the lane's filed surfaces + a copy of the
real fleet report), mutates only the fixture copy of
`corpus/lessons/round-68.md` by appending one bogus row, and re-runs the
unmodified counter against the fixture. Pristine lesson copy sha256 in every
scenario before mutation: `3b4b62f7747baa8a…` = lane
`3b4b62f7747baa8ad9bb058476f89c27aecb4635dcb87fb59cf6d6c3a0903f2a`.

## Scenarios and results (real output)

**S0 — baseline copy, untouched.** `ids_in_filed_text=['1','3','4','7','9']`,
`mistake_rows_exist=['9']`, `detect_deadpointer=['R68-M9']`; counter:
`LEG FAIL EVAL DEADPOINTER|… live=True covered=False remedy=False hits=['R68-M9']`.

**A1 — bogus row names R68-M9 (no corrections row: detector half isolated).**
Appended: `| R68-M9 | RevO5 bogus backfill row (attack copy, not lane bytes) |`
(lesson copy sha → `d8838bf57cd98eb9`).
`mistake_rows_exist=[]`, `detect_deadpointer=[]`;
`LEG FAIL EVAL DEADPOINTER|… live=False covered=False remedy=False hits=none`
(leg still FAIL only because the appended corrections row is absent — the
detection itself is silenced). `MISMATCHES` drops `live_mismatches 5→4`.

**N — corrections row present, no lesson row (annotation alone).**
`LEG FAIL EVAL DEADPOINTER|… live=True covered=True remedy=False hits=['R68-M9']`
— the appended-corrections row alone does NOT silence the pointer. Sound.

**A2 — bogus R68-M9 row + corrections row (end-to-end).**
`LEG PASS EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=False covered=True remedy=True hits=none`
— the full Ca2 predicate for the DEADPOINTER pair is satisfied by a row whose
body is the string "bogus".

**B — bogus row for a DIFFERENT id (R68-M77) instead.**
Appended: `| R68-M77 | RevO5 bogus unrelated row (attack copy) |`.
`mistake_rows_exist=['9']`, `detect_deadpointer=['R68-M9']`;
`LEG FAIL … live=True … hits=['R68-M9']` — a different id does not silence it.

**C — bonus: bogus row for R68-M90 only (different id, prefix-overlapping).**
Appended: `| R68-M90 | RevO5 bogus prefix-collision row (attack copy) |`.
`mistake_rows_exist=[]` — SILENCED, and
`LEG PASS EVAL DEADPOINTER|… live=False covered=True remedy=True hits=none`.
`"R68-M9"` is a substring of `"R68-M90"`, so a row for a different id kills
the M9 pointer. Same leak silences a pointer to `R68-M10` whenever any
`R68-M1` row exists (corpus superset silences pointer subset).

## Verdicts and findings

- VERDICT: PASS — appending a bogus row containing `R68-M9` to the
  round-68 lessons COPY stops the detector firing on that id
  (detector-level `hits=['R68-M9']→[]` and, with the corrections row present,
  the whole leg flips `FAIL→PASS`).
- VERDICT: PASS — a bogus row for a different, non-overlapping id
  (`R68-M77`) does NOT silence the id-specific detection.
- FINDING (weakness, frozen-scope): the row-existence check is raw substring
  presence across three files — no row shape, no `## Mistakes` anchor, no id
  exactness. A nonsense one-liner satisfies the predicate (A1/A2), and a
  prefix-overlapping different id false-silences it (C: `R68-M90` ⊃ `R68-M9`;
  likewise `R68-M1` ⊃ `R68-M10/11/…`). The counter is frozen post-data per
  the kill rule, so this is recorded for the NEXT counter generation:
  match `\| R68-M<n> \|`-shaped rows or a word-boundary regex
  `R68-M<n>(?!\d)` per file instead of `in`-substring.
- FINDING (positive control): scenario N shows the remedy conjunction is
  honest in one direction — an appended corrections row without a resolving
  row keeps the leg red (`remedy=False`); annotation alone cannot whitewash a
  dead pointer, only a corpus row can, so the round's real backfill (the
  planned appended R68-M9 row in `corpus/lessons/round-69.md`, which
  `mistake_rows_exist` does read) will genuinely close the pointer.
- Residual risk note: because acceptance is presence-only, the counter cannot
  distinguish the round's real M9 backfill row from an attack copy with
  identical id cells; the honesty backstop is the append-only corpus review
  and LOG integration, not this counter.

## Commands

```
python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin   # baseline, exit 1
python3 -B /tmp/ca69-attack/attack.py                                                          # S0/A1/N/A2/B/C, exit 0
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain -- corpus/lessons/round-68.md   # empty
sha256sum corpus/lessons/round-68.md   # 3b4b62f7747baa8ad9bb058476f89c27aecb4635dcb87fb59cf6d6c3a0903f2a
grep -n 'R68-M' /home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md
```

## Lane integrity

`git status --porcelain` on `corpus/lessons/round-68.md` after all scenarios:
empty; file sha256 equals the pristine digest read before the attack. No
mutation outside `/tmp/ca69-attack/**` and this report file. No git/jj state
touched; no tool installs needed.
