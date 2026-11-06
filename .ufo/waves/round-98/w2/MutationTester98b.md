# MutationTester98b — round-98 mutation probe of grader v10

Seat: MutationTester98b (attack seat; never repairs the grader). Wave: round-98/w2 (residual,
replacing the dead MutationTester98). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Dependency: none. v10 verified before start: `tools/check-advance-evidence.py` sha256
`d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` — equal to the frozen value.

## Verdict

- Frozen driver: `.ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py`, 23340 B, sha256
  `dd88caec75b86b0174d63521a6796c682675cc6ba50a2233862afb04057efb0f`; pin
  `reports/round-98/controls/mutants98.sha256` = `dd88caec…  mutants98.py` (pin file sha256
  `59fa209148352e3487dda444b22a9d2f67ee503de9037873bc2369d13d3563d3`).
- Official first measurement (lane v10, sha `d35b13c9…`):
  `MUTATION-SCORE: 128/128 killed, 0 survived, 0 broken-pattern`, driver rc=0.
  Receipt `reports/round-98/controls/mutation98-first.txt`, sha256
  `62278cccaef61632aa41e19e9fefea1e99fb2de98bc220c8d6b065a6b522a28c`, 132 lines: line 1
  `DRIVER-SHA256 dd88caec…`, line 2 `TOOL sha256=d35b13c9…`, line 3
  `CLEAN-FIRST selftest_rc=0 SELFTEST-PASS-line=True`, 128 KILLED rows, final MUTATION-SCORE.
- Red-before-v9 (v9 bytes `1021dc9d…`, exported from `bcf664aa`):
  `MUTATION-SCORE: 117/128 killed, 0 survived, 11 broken-pattern`, driver rc=1.
  `.ufo/waves/round-98/w2/stage/MutationTester98b/red-before-v9.txt`, sha256
  `fce35a4254f94ac9b26a7a0dfe8997dc27e8b24b9ad99acfc11806db536ede8a`, 132 lines, line 2
  `TOOL sha256=1021dc9d…`, line 3 `CLEAN-FIRST selftest_rc=0 SELFTEST-PASS-line=True`.
- Survivors: none on v10 and none on v9; there is no survivor to name. No grader repair was made
  or attempted (ExecGraderV10 owns the grader).
- Kill oracle: the grader's own `--selftest`. The driver runs the clean tool first (must be
  rc 0 with a `SELFTEST PASS n/n` line, else no mutant is scored); a mutant is KILLED iff its
  selftest rc != 0 or the PASS line disappears. battery98 was not used as an oracle.

## Driver construction

The dead seat's pre-pin draft was re-read in full against the v10 bytes and the step list. It
needed no edits: 128 tuples, every `old` pattern matched v10, every `exactly-once` entry matched
exactly once (0 broken) before the first measurement. Its `__pycache__` was deleted (twice: once
on takeover, once after my importlib verification loads recreated it).

- 121 round-97 tuples carried in the same order; 5 updated where v10 rewrote their anchors:
  `combining-refuse-off` (re-slanted to drop `and not m`; the plain-off variant is shadowed by
  v10's new window M-branch), `verdict-ctrl-off` (now the category-Cc branch),
  `heading-combining-off`, `cm1-mark-lasttoken-only`, `cmw2-mark-numbering-only` (v10 uses
  `category(_c)[0] == 'M'`).
- 7 new tuples, at least one per round-98 refusal class; total 128 >= 126.
- CLI unchanged (`--tool <path> --work <dir>`, optional `--only`); first stdout line
  `DRIVER-SHA256 <sha256 of own bytes>`; summary line unchanged.

## New round-98 mutants (all `matches=1`, `exactly-once`, KILLED on v10)

| name | v10 line | refusal class | mutation |
|---|---|---|---|
| `verdict-ctrl-cc-narrow` | 318 | DEL1 (Cc/DEL) | `if unicodedata.category(c) == 'Cc':` → `if o < 0x20:` — U+007F escapes, CR1/US1/NUL1 still refused |
| `verdict-combine-window-off` | 321 | ENC1 (Mn/Mc/Me) | new `if unicodedata.category(c)[0] == 'M' and o != 0x200c:` VERDICT-COMBINE branch → `if False:` — U+20DD escapes the window; the `_refuse_disguised` fallback still says VERDICT-COMBINE but cannot name U+20DD, so the selftest check fails |
| `nonascii-number-off` | 752 | ROMAN1+SUP1 (non-ASCII numeral) | insert `return False` before `core = tok.strip('…')` in `_nonascii_number` — roman/superscript numbering tokens become content tokens |
| `fullwidth-stop-strip-off` | 758 | FWPER1 (fullwidth stop) | last disjunct `(tok and tok[-1] in '\uFF0E\u3002\uFE52\uFF61' and …)` → `(tok and False and …)` — `1．` escapes |
| `selftest-g98-del1-fixture-off` | 1972 | DEL1 selftest-only branch | fixture token `LOCA\u007fTED` → `LOCATED` |
| `selftest-g98-enc1-fixture-off` | 1973 | ENC1 selftest-only branch | fixture token `LOCA\u20ddTED` → `LOCATED` |
| `selftest-g98-heading-rc-off` | 1987 | ROMAN1/SUP1/FWPER1 selftest-only branch | expected rc `1` → `0` on the `round-98 {_c}: non-ASCII numbering token refused` check |

## Broken-pattern list (v9 only; none on v10)

11 names, all `matches=0 semantics=exactly-once` against v9, i.e. their anchors are v10-only
bytes; the 117 anchored mutants all kill on v9:

`verdict-ctrl-off` (318), `heading-combining-off` (741), `cm1-mark-lasttoken-only` (742),
`cmw2-mark-numbering-only` (742), `verdict-ctrl-cc-narrow` (318),
`verdict-combine-window-off` (321), `nonascii-number-off` (752),
`fullwidth-stop-strip-off` (758), `selftest-g98-del1-fixture-off` (1972),
`selftest-g98-enc1-fixture-off` (1973), `selftest-g98-heading-rc-off` (1987).

## Commands and rc (chronological)

1. `sha256sum tools/check-advance-evidence.py` — rc 0, `d35b13c9…` (v10 verified).
2. `git -C <lane> show bcf664aa…:tools/check-advance-evidence.py > $S/v9.py` — rc 0;
   `sha256sum $S/v9.py` — rc 0, `1021dc9d…`.
3. `python3 -B tools/check-advance-evidence.py --selftest --work $S/t1` — rc 0;
   `grep -c '^  ok'` = 161, rc 0 (`SELFTEST PASS 161/161`).
4. `python3 -B $S/v9.py --selftest --work $S/t9` — rc 0, `SELFTEST PASS 155/155`.
5. Pattern count, importlib `src.count(old)` over all 128 tuples — rc 0: v10 broken=0,
   v9 broken=11 (names above).
6. Pre-pin dev run (scratch only, not evidence): `python3 -B mutants98.py --tool
   tools/check-advance-evidence.py --work $S/w-pre` — rc 0,
   `128/128 killed, 0 survived, 0 broken-pattern`.
7. Pin write: `printf '%s  mutants98.py\n' dd88caec… > reports/round-98/controls/mutants98.sha256`
   — rc 0; `sha256sum` of the pin — rc 0, `59fa2091…`.
8. **First measurement (run once, lane v10):** `python3 -B
   .ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py --tool
   tools/check-advance-evidence.py --work $S/first >
   reports/round-98/controls/mutation98-first.txt` — driver rc 0; receipt 132 lines,
   `128/128 killed, 0 survived, 0 broken-pattern`; `grep -c KILLED`=128, `grep -c SURVIVED`=0,
   `grep -c BROKEN`=0 (each rc 0).
9. **Red run:** same frozen driver, `--tool $S/v9.py --work $S/red9 >
   .ufo/waves/round-98/w2/stage/MutationTester98b/red-before-v9.txt` — driver rc 1;
   `117/128 killed, 0 survived, 11 broken-pattern`.
10. Final integrity: `sha256sum mutants98.py` — rc 0, still `dd88caec…`;
    `sha256sum tools/check-advance-evidence.py` — rc 0, still `d35b13c9…` (the probe writes only
    its `--work` copies; no lane byte was modified).
11. `rm -rf .ufo/waves/round-98/w1/stage/MutationTester98/__pycache__` — rc 0.
12. Scratch `rm -rf /fast/scratch/hyaku/kotodama-r98/MutationTester98b` — rc 0 (before yield).

## Notes

- Tooling installs/updates: none; pacman untouched; no host sysctl touched.
- The driver sha equals the pin and the first receipt's `DRIVER-SHA256` line
  (`dd88caec…`), and the red receipt carries the same line; the driver was not edited after the
  pin.
- The 25-word/quote/evidence rules do not apply to this seat (no web source was fetched).
- Scratch deleted before yield; the only files left are the driver, the pin, the first receipt,
  the red receipt, this report and the DONE marker.
