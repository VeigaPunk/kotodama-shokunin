# SURVIVORS — mutants100 pre-flight against tools/check-table-support.py

Tool sha256 at pre-flight: `ecd27fcd5f1cd152372db9ccdee2f2ce64d5e7a07f932eed186fc9034de644c6`
(574 lines). Driver not yet frozen; this file names every mutant that survived BOTH oracles
(battery100 rc 0 AND the tool's own `--selftest` rc 0) so the tool owner can add the missing pins.

Command (rc 0 = all killed, rc 1 = survivors; this pre-flight ran rc 1):

    python3 /fast/scratch/hyaku/kotodama-r100/MutationTester100/preflight.py \
        /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-table-support.py \
        /fast/scratch/hyaku/kotodama-r100/MutationTester100/pf-tool

Result: 29 killed (26 by battery100, 2 by selftest: N1, R4; 1 by both-path R2), 7 survived,
0 broken-pattern, of 36 mutants.

## Survivors (each needs ONE selftest pin; battery100 is frozen and must not change)

| id | mutation | line | why it survives |
|---|---|---|---|
| W1 | `WINDOW = 80` -> `79` | 54 | no fixture puts two cell stems exactly 79 tokens apart |
| W2 | `WINDOW = 80` -> `81` | 54 | no fixture puts two cell stems exactly 80 tokens apart |
| A2 | `best * 4 < len(stems) * 3` -> `best * 3 < len(stems) * 2` | 223 | no fixture sits at best/total = 2/3 (B9 is 3/4, F13 is 2/4) |
| L1 | label-token `len(t) >= 3` -> `>= 4` | 104 | no fixture has a 3-char label token that must bind (`Ewe` in F10 is expected UNBOUND either way) |
| L2 | label-token `len(t) >= 3` -> `>= 2` | 104 | no fixture has a 2-char label token that must not bind |
| L4 | ` and t != 'and'` removed | 104 | no fixture label contains the word `and` |
| C4 | caption loop stops after one line (`and not cap`) | 128 | every caption paragraph in the battery and the selftest is a single line |

## Exact pins that kill them (paste-ready for the tool owner)

All use the existing `st_json_pin(work, name, text, rc, keys, ..., scoped=)` helper and
`st_entry(caption, header, sep, rows, bind)`. Captures are added through `evid={...}`.

1. **W1 + W2** (one pin kills both; capture `S9101`):
   `S9101 = 'alpha ' + ' '.join(['lorem'] * 78) + ' beta gamma ' + ' '.join(['lorem'] * 79) + ' delta'`
   -> token indices: alpha 0, lorem 1..78, beta 79, gamma 80, lorem 81..159, delta 160.
   entry: caption `REC`, header `| tradition | practice |`, sep `|---|---|`,
   rows `['| Alpha | alpha beta |', '| Gamma | gamma delta |']`,
   bind `['The Alpha and Gamma rows report the cases (S9101).']`.
   Expected: rc 1, keys `[('UNSUPPORTED-CELL', 'Gamma', 'practice')]`, best `(1, 2)`, scoped 1.
   * At WINDOW 79 the Alpha cell also fails (extra finding) -> pin FAILS.
   * At WINDOW 81 the Gamma cell passes (no finding, rc 0) -> pin FAILS.
   * At WINDOW 80 exactly one finding -> pin PASSES.

2. **A2** (capture `S9102 = 'alpha beta lorem lorem lorem'`):
   entry: caption `REC`, header `| tradition | practice |`, sep `|---|---|`,
   row `| Alpha | alpha beta zulu |`, bind `['The Alpha row reports the case (S9102).']`.
   Expected: rc 1, `[('UNSUPPORTED-CELL', 'Alpha', 'practice')]`, best `(2, 3)`.
   * At 2/3 the cell is supported (2*3 >= 3*2) -> no finding -> pin FAILS.

3. **L1** (capture `S9103 = 'alpha beta'`):
   entry: caption `REC`, header `| tradition | practice |`, sep `|---|---|`,
   row `| Ewe | alpha beta |`, bind `['The Ewe row reports the case (S9103).']`.
   Expected: rc 0, no findings.
   * At `len(t) >= 4` the label `Ewe` yields no token -> UNBOUND-ROW -> pin FAILS.

4. **L2** (capture `S9104 = 'alpha beta'`):
   entry: caption `REC`, header `| tradition | practice |`, sep `|---|---|`,
   row `| If | alpha beta |`, bind `['The If row reports the case (S9104).']`.
   Expected: rc 1, `[('UNBOUND-ROW', 'If', '')]`.
   * At `len(t) >= 2` the token `if` binds the line -> cell supported -> no finding -> pin FAILS.

5. **L4** (capture `S9105 = 'alpha beta'`):
   entry: caption `REC`, header `| tradition | practice |`, sep `|---|---|`,
   row `| Salt and iron | alpha beta |`, bind `['The wind and rain report the case (S9105).']`.
   Expected: rc 1, `[('UNBOUND-ROW', 'Salt and iron', '')]`.
   * Without the `and` exclusion the token `and` binds the line -> cell supported -> no finding -> pin FAILS.

6. **C4** (capture `S9106 = 'alpha beta'`):
   entry: caption `'The recorded cases fill this table.\nDesign notes follow.'` (two lines),
   header `| tradition | practice |`, sep `|---|---|`, row `| Alpha | alpha beta |`,
   bind `['The Alpha row reports the case (S9106).']`.
   Expected: rc 0, no findings, scoped 1.
   * With a one-line caption extent the caption is `Design notes follow.` -> scoped 0 -> pin FAILS.

## Non-observable clause (recorded, not a survivor)

A single-point mutant cannot produce a traceback on a bad-UTF-8 entry: the inner
`except UnicodeDecodeError` prints the error and the outer `except Exception` net catches anything
else, so `R4` was expressed as the ToolError handler re-raising (killed by the E7 pin) and `R5` as
the UTF-8 path returning 0 (killed by battery E2). The double net is a design property, not a gap.
