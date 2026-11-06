# ExecBattery97 — round-97 battery driver, sha pin, v8 control receipt

Seat: ExecBattery97 (wave round-97/w1). Task: build `battery97.py` (battery96 + the seven
CriticO96 survivor classes), its sha pin, and its control receipt over the exported v8
grader. No dependency; done first pass, control matched on the first run.

## Deliverables

| file | sha256 / content |
|---|---|
| `.ufo/waves/round-97/w1/stage/ExecBattery97/battery97.py` | `79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c` |
| `reports/round-97/controls/battery97.sha256` | `79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c  battery97.py` |
| `reports/round-97/controls/battery97-control-v8.txt` | complete stdout of the v8 control run (105 lines; contains `BATTERY-SHA256 79efb67c...`, `TOOL-SHA256 f29ab013...`, `BATTERY-SUMMARY survivors=7 unnamed=0 refused=24 traceback=0 clean=2 not-clean=0`, 34 `REG` lines) |

Driver sha == pin sha == receipt `BATTERY-SHA256` (checked byte-for-byte). battery97.py was
not edited after the control run.

## Construction

`cp battery96.py battery97.py` (source sha verified `9f80f59481861b104f166a838222fcdf300e55a27fc841b5217e1980b5e91c21`
before copy), then edited in place:

- docstring rewritten for round-97 (copy provenance, 31+2 classes, output contract);
- seven builders ported from `.ufo/waves/round-96/w1/stage/CriticO96/attacks_critic96.py`
  byte-for-byte (`lesson_gain` → `_dispo97`, `heads_with` → `_heads97`; same codepoints
  CR=chr(0x000D), US=chr(0x001F), OGH=chr(0x1680), ISPACE=chr(0x3000), NUL=chr(0x0000),
  CM=chr(0x0301)); no import of the critic driver;
- seven expected-REFUSE `CLASSES` entries appended after F1, controls G0/ZWNJ1 kept last;
- `main()` prints `BATTERY-SHA256 <sha of its own file bytes>` as line 1 and
  `TOOL-SHA256 <sha of the --tool bytes>` as line 2 (battery96's `TOOL sha256=... path=...`
  line kept as line 3 for receipt continuity);
- CLI, the 24 existing class rows, REG lines, summary format, grade() and run_regression()
  unchanged; `--emit` manifest strings renamed to round-97/battery97 (cosmetic).

## Class table (33 classes: 31 expected-REFUSE + 2 CLEAN controls)

Recipes: L = lesson channel, gained S001 line `- S001 <token> recheck moved` + GAINED_TAIL;
H = heading channel, five `## N. The X` → `## <prefix> phrase` replacements.

| class | recipe | expected | v8 outcome | v8 named diagnostic |
|---|---|---|---|---|
| A1 | Cyrillic O U+041E in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-NONASCII |
| B1 | soft hyphen U+00AD in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-SOFTHYPHEN |
| G1 | `## 1. address` numbered phrase heads x5 (H) | REFUSE | REFUSED rc=1 | TOPIC |
| H1 | manifest row value = JSON list | REFUSE | REFUSED rc=2 | MANIFEST-ROW-TYPE |
| I1 | lands row S955 truncated to 4 cells | REFUSE | REFUSED rc=1 | NEWIDS |
| J1 | en-dash U+2013 in NOT–LOCATED (L) | REFUSE | REFUSED rc=1 | gained_a_NOT-LOCATED_line |
| K1 | lowercase unanchored `located` verdict (L) | REFUSE | REFUSED rc=2 | VERDICT-LOWERCASE |
| CD1 | combining acute U+0301 in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-COMBINE |
| LR1 | LRM U+200E in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-FORMAT |
| TAB1 | literal tab in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-TAB |
| ID1 | small-cap S U+A731 in id token (L) | REFUSE | REFUSED rc=2 | ID-NONASCII |
| NUM1 | `## 1.1 address` nested numbers x5 (H) | REFUSE | REFUSED rc=1 | TOPIC |
| RM1 | `## I. address` roman numbers x5 (H) | REFUSE | REFUSED rc=1 | TOPIC |
| NUM2 | `## Notes 1) address` x5 (H) | REFUSE | REFUSED rc=1 | TOPIC |
| NB1 | NBSP U+00A0 in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-NBSP |
| VT1 | vertical tab U+000B in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-VT |
| FF1 | form feed U+000C in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-FF |
| LS1 | line separator U+2028 in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-LINESEP |
| NEL1 | NEL U+0085 in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-NEL |
| ANSI1 | ESC U+001B + [31m in LOCATED (L) | REFUSE | REFUSED rc=2 | VERDICT-ANSI |
| CYR1 | Cyrillic a U+0430 as id letter (L) | REFUSE | REFUSED rc=2 | ID-NONASCII |
| BR1 | `## (1) address` bracketed x5 (H) | REFUSE | REFUSED rc=1 | TOPIC |
| DASH1 | `## - address` dash x5 (H) | REFUSE | REFUSED rc=1 | TOPIC |
| F1 | non-numbered content-free heads x5 (H) | REFUSE | REFUSED rc=1 | TOPIC |
| **CR1** | lone CR U+000D in LOCATED (L): `- S001 LOCA<U+000D>TED recheck moved…` | REFUSE (v9) | **SURVIVOR** rc=0 | none |
| **US1** | unit separator U+001F in LOCATED (L) | REFUSE (v9) | **SURVIVOR** rc=0 | none |
| **OGH1** | ogham space mark U+1680 in LOCATED (L) | REFUSE (v9) | **SURVIVOR** rc=0 | none |
| **IS1** | ideographic space U+3000 in LOCATED (L) | REFUSE (v9) | **SURVIVOR** rc=0 | none |
| **NUL1** | NUL U+0000 in LOCATED (L) | REFUSE (v9) | **SURVIVOR** rc=0 | none |
| **CM1** | `## 1<U+0301>. address` … x5 (H, numbering token) | REFUSE (v9) | **SURVIVOR** rc=0 | none |
| **CMW2** | combining acute inside heading phrase word (`## addre<U+0301>ss` style) x5 (H) | REFUSE (v9) | **SURVIVOR** rc=0 | none |
| G0 | unmodified mini-lane | CLEAN | CLEAN rc=0 | — |
| ZWNJ1 | ZWNJ U+200C in table-cell phrase | CLEAN | CLEAN rc=0 | — |

The seven new classes' token lists (a correct v9 must print at least one): lesson channel
`VERDICT-LINESEP | VERDICT-SEPARATOR | VERDICT-CTRL | VERDICT-WS | VERDICT-NFKC |
VERDICT-NONASCII | NON-ASCII-VERDICT | LEG FAIL APPENDONLY`; heading channel
`LEG FAIL TOPIC | HEADING-COMBINING | COMBINING | HEAD-NONASCII | TOPIC-HEADING |
HEADING-NONASCII` — the v8 diagnostic families plus plausible v9 extensions, so the refusal
is credited through either a dedicated diagnostic or the APPENDONLY/TOPIC leg.

## Control over v8 (first and only run; nothing fixed)

Commands, all rc=0:

1. `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1ffc5a83d2c70e3bc581594efbcf32c562ba2569:tools/check-advance-evidence.py > <scratch>/v8/check-advance-evidence.py`
   → `sha256sum` = `f29ab0139b4590fa8da7232a7372574675ef60763c475eea003006eb1dbcd9c0` (v8 sha confirmed).
2. `python3 -B battery97.py --tool <scratch>/v8/check-advance-evidence.py --work <scratch>/v8run`
   → rc=0, stderr 0 bytes; stdout copied verbatim to `reports/round-97/controls/battery97-control-v8.txt`.
   Receipt: `BATTERY-SHA256 79efb67c...` (line 1), `TOOL-SHA256 f29ab013...` (line 2),
   `BATTERY-SUMMARY survivors=7 unnamed=0 refused=24 traceback=0 clean=2 not-clean=0` —
   exactly the frozen `CONTROL_SUMMARY (7, 0, 24)` of predispatch.py; the seven survivors
   are CR1, US1, OGH1, IS1, NUL1, CM1, CMW2; 0 traceback anywhere in the receipt.
3. REG parity: `grep -c '^REG '` on the receipt = 34; `diff <(grep '^REG ' receipt)
   reports/round-95/controls/reg-v5.txt` → empty diff (rc=0): all 34 REG lines byte-identical
   (26 R93 + 8 R92, including `REG R92 G0 ... outcome=clean`).
4. Pin written: `79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c  battery97.py`;
   re-verified `sha256sum battery97.py` == pin == receipt `BATTERY-SHA256`.
5. Predispatch receipt contract re-checked with its own regexes (`^BATTERY-SHA256 <64hex>$`,
   `^TOOL-SHA256 <64hex>$` == V8_SHA, summary triple == (7,0,24)): satisfied.

Expected v9 behavior encoded in the driver (claims.json O2): `survivors=0 unnamed=0
refused=31`, traceback-free, driver sha == pin == receipt.

## Numbers (each with command and rc)

- battery96.py source sha: `sha256sum` rc=0 → `9f80f594...` (matches assignment).
- battery97.py syntax: `python3 -B -c "compile(open(...).read(),...)"` rc=0.
- class count: module load → `CLASSES total 33 refuse-expected 31 controls ['G0','ZWNJ1']` rc=0.
- v8 export sha: `sha256sum` rc=0 → `f29ab013...`.
- control run: `python3 -B battery97.py --tool ... --work ...` rc=0, stderr 0 bytes.
- receipt summary: `survivors=7 unnamed=0 refused=24 traceback=0 clean=2 not-clean=0` (grep rc=0).
- Traceback occurrences in receipt: `grep -c Traceback` → 0.
- REG lines in receipt: 34 (`grep -c '^REG '` rc=0); `diff` vs `reports/round-95/controls/reg-v5.txt` → identical rc=0.
- driver sha on disk after run: `79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c`.

## Tooling authorization

No tools installed or upgraded (none needed; pacman untouched).

## Scope notes

- Only files written: `battery97.py` (stage), `reports/round-97/controls/battery97.sha256`,
  `reports/round-97/controls/battery97-control-v8.txt`, this Report, stage `DONE`. Frozen
  files (claims.json, predispatch.py, predispatch-base.txt, sweep-control.*, controls/
  forgery-sha-only.txt, controls/critic96-on-v8.txt, round-96-and-earlier reports) untouched;
  battery96.py untouched; no git/jj mutations.
- Scratch `/fast/scratch/hyaku/kotodama-r97/ExecBattery97/` deleted before yield.
- Note for the L1: the receipt's `TOOL ... path=` line records the scratch v8 export path
  (per assignment, the control runs against the exported copy, not the lane file).
