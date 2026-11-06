# MutationTester100 — mutation attack on tools/check-table-support.py (round 100, claim O leg O4)

Attack seat. I never edited the tool, battery100, claims.json, predispatch.py or any control
receipt. I wrote only my stage dir, `reports/round-100/controls/mutants100.sha256` and
`reports/round-100/controls/mutation100-first.txt`.

## Driver

`stage/MutationTester100/mutants100.py`, sha256
`18dbcf3b02ef57625b8593a7a514e35b3055e6ad2838fb2d81ec5e9175903424` (pinned; never edited after the
pin).

CLI `--tool <path> --work <dir>`. First stdout line `DRIVER-SHA256 <sha of its own bytes>`.
36 mutants, each one `(regex pattern, replacement, expected match count)` applied to a scratch
copy of the tool; a count mismatch is `broken-pattern` (never counted as killed). Kill oracle:
battery100 (`python3 -B .../battery100.py --tool <mutant> --work <dir>`) rc != 0, else the
mutant's own `--selftest --work <dir>` rc != 0; the driver names the oracle per mutant. The
selftest oracle is used only when the pristine tool's selftest passes.

## Pre-flight loop (before freeze; not the receipt)

First pre-flight on tool sha `ecd27fcd…` (574 lines, SELFTEST 32/32): 29/36 killed, 7 survived,
0 broken — rc 1. Survivors, with their mutation and pre-flight line:

| id | mutation | line |
|---|---|---|
| W1 | `WINDOW = 80` -> `79` | 54 |
| W2 | `WINDOW = 80` -> `81` | 54 |
| A2 | `best * 4 < len(stems) * 3` -> `best * 3 < len(stems) * 2` | 223 |
| L1 | label-token `len(t) >= 3` -> `>= 4` | 104 |
| L2 | label-token `len(t) >= 3` -> `>= 2` | 104 |
| L4 | ` and t != 'and'` removed | 104 |
| C4 | caption loop stops after one line | 128 |

Named in `stage/MutationTester100/SURVIVORS.md` (written immediately) and reported to
ExecTableSupport100 with six paste-ready pins in `stage/MutationTester100/PINS-FOR-OWNER.md`.
Every pin was validated before the request: PASS on pristine bytes, FAIL on its target mutant
(`validate_pins.py`, rc 0). The owner added the six pins; re-pre-flight on sha `271c42fa…`:
0 survivors, 0 broken, rc 0. Only then was the driver frozen.

## Frozen run (the receipt)

Commands, in order, with rc:

1. `sha256sum tools/check-table-support.py` -> `271c42fa…` rc 0
2. `python3 -B tools/check-table-support.py --selftest --work …/v-sw` -> `SELFTEST PASS 39/39` rc 0
3. `python3 -B reports/round-100/controls/battery100.py --tool tools/check-table-support.py --work …/v-bw`
   -> `BATTERY-SUMMARY cases=28 pass=28 fail=0 traceback=0` rc 0
4. `sha256sum stage/MutationTester100/mutants100.py` -> `18dbcf3b…`; pin written as
   `18dbcf3b…  mutants100.py` rc 0
5. `python3 -B stage/MutationTester100/mutants100.py --tool tools/check-table-support.py --work …/run1
   > reports/round-100/controls/mutation100-first.txt` -> driver rc 0, stderr 0 bytes

Receipt (`reports/round-100/controls/mutation100-first.txt`, 41 lines):
`DRIVER-SHA256 18dbcf3b…`, `TOOL-SHA256 271c42fa…`, `BATTERY-SHA256 b78176e3…`,
`SELFTEST-ORACLE available (pristine rc=0)`, 36 `MUTANT` lines, and
`MUTATION-SCORE: 36/36 killed, 0 survived, 0 broken-pattern`.

Oracle split: 27 killed by battery100, 9 by the tool's own selftest (W1, W2, A2, L1, L2, L4, C4,
N1, R4). Pin == receipt first line == driver sha (`18dbcf3b…`), verified by `cut`/`sha256sum`, rc 0.

Coverage of the contract clauses: window size 80->79/81/10000; threshold `>=`->`>`, 3/4->2/3,
3/4->1/2; each stem rule removed (ies, es, trailing s); STOP emptied and STOP losing `them`;
label-token min length 3->4 and 3->2; token binding->substring; `and` exclusion removed; caption
regex widened/narrowed/case-sensitive; caption extent one line and emptied; binding extent crossing
blanks; union support across rows; NO-CAPTURE dedup removed; NO-PATH skipped; path range off by one;
UNBOUND citation requirement dropped; rc 1<->0 and rc 2->1; TABLE_SUPPORT_ERROR text; traceback on a
refused input; bad UTF-8 accepted; JSON keys `findings`/`scoped_tables`; header column off by one;
content-word min length 4->3; `words` compared as words not stems.

## Post-freeze tool drift (recorded, not hidden)

The tool owner kept editing after the receipt. The counter's O4 leg re-runs the driver against the
landed tool (seen in the owner's `counter4.out`), so the landed bytes must also score 36/36. I
re-ran the frozen driver on each landed version (driver unchanged; these runs are information, the
first receipt is untouched):

| run | tool sha | result | file |
|---|---|---|---|
| receipt | `271c42fa…` | 36/36 killed, 0 survived, 0 broken, rc 0 | `reports/round-100/controls/mutation100-first.txt` |
| second | `3ad56147…` | 35/36, R4 SURVIVED (its `_e7` had become a directory test that no longer reaches ToolError) | `stage/…/mutation100-second.txt` |
| third | `53441488…` | 35/36, R3 BROKEN-PATTERN matches=15 expected=13 | `stage/…/mutation100-third.txt` |
| fourth | `972cefea…` | 36/36 killed, 0 survived, 0 broken, rc 0 | `stage/…/mutation100-fourth.txt` |

Landed state verified at `972cefea2b429a9d9ca3d9efc1acf3a63391e7c6ba2da576a1225fda6258b73a`
(32808 B, mtime 08:56:19, stable over 45 s): `SELFTEST PASS 40/40` rc 0, battery 28/28 rc 0,
frozen driver `MUTATION-SCORE: 36/36 killed, 0 survived, 0 broken-pattern` rc 0. The owner was told
to freeze these bytes; the frozen driver tolerates no further edit to the error-string count
(exactly 13 `TABLE_SUPPORT_ERROR`, exactly 7 `return 2`, and the exact `except ToolError` and UTF-8
handler blocks).

The receipt's `TOOL-SHA256` line names the bytes measured at freeze (`271c42fa…`), not the landed
`972cefea…`. The driver sha (the pin and receipt binding O4 declares) is unchanged. If the L1 reads
"first-receipt-bound" as binding the tool sha too, this drift is the honest reason it would fail;
I cannot rewrite the first receipt without breaking the one-run rule.

## Feasibility reference (information only)

`stage/MutationTester100/on-ref.txt` (driver against `table_support_ref.py` copied to scratch,
sha `24fd73f4…`, 203 lines, no selftest): `SELFTEST-ORACLE unavailable (pristine rc=2)`,
`MUTATION-SCORE: 24/36 killed, 8 survived, 4 broken-pattern`, rc 1.
Survivors: W1, W2, A2, L1, L2, L4, C4, N1 — the same seven the lane tool needed pins for, plus N1
(dedup, selftest-only). Broken patterns on the reference are structural, not defects: R2/R3
(`matches=3`, the reference has 3 `return 2`/`TABLE_SUPPORT_ERROR` sites, not 7/13) and R4/R5
(`matches=0`, the reference has no ToolError layer and no UTF-8 handler). This is why the lane tool
is the measured target and the reference is not.

## Notes

- A single-point mutant cannot make a bad-UTF-8 entry print a traceback: the inner
  `except UnicodeDecodeError` prints the error and the outer `except Exception` net catches
  anything else. R4 was therefore expressed as the ToolError handler re-raising (killed by the E7
  pin) and R5 as the UTF-8 path returning 0 (killed by battery E2). Recorded in SURVIVORS.md.
- Tooling installed: none. No pacman, no network access, no sysctl change.
- Scratch `/fast/scratch/hyaku/kotodama-r100/MutationTester100/` deleted before yield; no `/tmp`
  file is cited. Post-freeze verification used `/fast/scratch/hyaku/kotodama-r100/mt-run*`.
- Nothing committed; no git/jj mutation run.

## Files

- `stage/MutationTester100/mutants100.py` (driver, 36 mutants, pinned)
- `stage/MutationTester100/SURVIVORS.md` (pre-freeze survivors + validated pins)
- `stage/MutationTester100/PINS-FOR-OWNER.md` (paste-ready pin block)
- `stage/MutationTester100/on-ref.txt` (reference run)
- `stage/MutationTester100/mutation100-second.txt`, `-third.txt`, `-fourth.txt` (drift evidence)
- `stage/MutationTester100/DONE` (sha256 of mutants100.py)
- `reports/round-100/controls/mutants100.sha256`
- `reports/round-100/controls/mutation100-first.txt`
