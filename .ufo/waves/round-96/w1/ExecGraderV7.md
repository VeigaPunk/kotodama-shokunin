# ExecGraderV7 report (round-96, ops O-legs feeder)

v6 sha256 (unchanged copy): `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` (matches frozen v6; staged as `stage/ExecGraderV7/v6-base.py`, rc=0 via `sha256sum`).
v7 sha256: `2e28a289746812b14a07a0645e568f0cee9dfb1789af6cfe6ce88f80c8f053ec` (rc=0 via `git diff --stat` + `sha256sum tools/check-advance-evidence.py`).

Lane file changed: `tools/check-advance-evidence.py` — v6 → v7. Diff stat (rc=0): `1 file changed, 71 insertions(+), 2 deletions(-)`.

## selftest (O1 leg equivalent)
Command: `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --selftest --work /fast/scratch/hyaku/kotodama-r96/ExecGraderV7/st-v7` (rc=0).
Summary line: `SELFTEST PASS 145/145` (was 134/134 on v6; +11 pins, rc=0).
Staged: `stage/ExecGraderV7/selftest.txt`.

## battery96 (O2 leg equivalent)
Command: `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-96/w1/stage/ExecBattery96/battery96.py --tool /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --work /fast/scratch/hyaku/kotodama-r96/ExecGraderV7/battery` (rc=0, no traceback, 0 occurrences of `Traceback` in output).
Summary line: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=24 traceback=0 clean=2 not-clean=0` (rc=0).
Per-class exits: NB1 rc=2, VT1 rc=2, FF1 rc=2, LS1 rc=2, NEL1 rc=2, ANSI1 rc=2, CYR1 rc=2, BR1 rc=1 (TOPIC), DASH1 rc=1 (TOPIC), F1 rc=1 (TOPIC, unchanged), G0 rc=0 (CLEAN), ZWNJ1 rc=0 (CLEAN, benign ZWNJ not refused).
Staged: `stage/ExecGraderV7/battery-v7.txt`.

## REG check (O4 leg equivalent)
34 REG lines in `reports/round-95/controls/reg-v5.txt`; every line occurs verbatim in battery96 output over v7 — 0 missing (rc=0). Additionally the 34 REG lines in battery96's REG section are byte-identical to `control-v6.txt`'s REG section (rc=0, diff empty).
F1 is refused by v6/v7 on TOPIC (8/9 legs, `phrase anchors 2/4` in control-v6's F1 detail); v7 does not touch that behaviour.

## New named diagnostics (line numbers in v7 file)
- `_refuse_verdict_channel(n, line)` — line 264. Raises before the `splitlines` severing loop in `dispositions()` (line 354), which first walks `lesson.split('\n')` (line 366); raw text is refused, so U+000B/U+000C/U+2028/U+0085 severing never hides them.
  - line 282: `verdict token carries a non-breaking space (VERDICT-NBSP)` — NB1 (U+00A0)
  - line 284: `verdict token carries a vertical tab (VERDICT-VT)` — VT1 (U+000B)
  - line 286: `verdict token carries a form feed (VERDICT-FF)` — FF1 (U+000C)
  - line 289: `verdict token carries a line separator (VERDICT-LINESEP)` — LS1 (U+2028), plus U+2029 and U+001C-U+001E same family
  - line 291: `verdict token carries a NEL (VERDICT-NEL)` — NEL1 (U+0085)
  - line 293: `verdict token carries an ANSI escape (VERDICT-ANSI)` — ANSI1 (ESC U+001B + CSI)
  - line 300: `id token carries a non-ASCII lookalike letter (ID-NONASCII)` — CYR1 (Cyrillic/Greek homoglyph in the S position; checked before the ASCII-id `[Ss]\d{3,}` gate)
- TOPIC heading-anchor fix — `_content_toks.isnum()` regex at line 729, extended with bracketed numbers `\(?\d+[.)]?\)?` and dash tokens `[\u2010-\u2015-]+` (BR1 `## (1) x`, DASH1 `## - x`): the list mark drains from the span count, so a numbered phrase-only heading still anchors only a single surface and fails TOPIC. F1 behaviour is untouched (v7 battery: F1 rc=1 TOPIC).
- ZWNJ (U+200C) is on no blocklist anywhere: the ZWNJ1 control passes CLEAN rc=0 on v7.

## Selftest pins added (11, 145−134)
- 6 token-codepoint pins (NB1/VT1/FF1/LS1/NEL1/ANSI1) + 2 family pins (U+2029, U+001C) + 1 CYR1 homoglyph pin + 1 BR1 + 1 DASH1 pin. All v6 pins retained, all rc=0.

## Commands (all rc=0)
- `cp tools/check-advance-evidence.py /fast/scratch/.../v6-base.py` — rc=0
- `sha256sum v6-base.py` → f7981b… (rc=0); `sha256sum tools/check-advance-evidence.py` → 2e28a2… (rc=0)
- selftest (rc=0), battery96 (rc=0), `grep -c Traceback battery-v7.txt` → 0 (rc=1 for no match, expected)
- REG verbatim check (rc=0, missing=0); `git diff --stat` (rc=0); `git status --porcelain` shows only `M tools/check-advance-evidence.py` (rc=0)
- Every v6 refusal retained: battery REG section identical and battery96 survivors=0/unnamed=0/refused=24 (no weakened refusal).

## Classes not closed
None. All 10 round-96 classes (9 fresh + F1) are refused by name; no class was left unclosed.

## Tools installed
None.
