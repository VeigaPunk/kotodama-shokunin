# CriticO95 — round-95 report (operability attack, routed findings)

Scope: invent fresh counterfeit classes beyond the frozen 14 and attack the v6 candidate. Survivors do NOT
fail claim O; they feed round 96. Full detail: `stage/CriticO95/attacks.md` (per-class table with v5 and v6
columns, minimal survivor recipes, controls, do-nothing note, re-runnable commands).

## Numbers (each with its command, rc 0)

- Fixtures: 15 fresh classes + G0 control + ZWNJ1 control, built under scratch only.
  Driver: `stage/CriticO95/attacks_critic95.py`; battery shape = battery95.py's own
  `configure()/grade()` imported read-only (battery95.py sha256 342237cd…; it landed mid-wait and served
  both runs).
- v6 candidate: `stage/ExecGraderV6/v6-candidate.py`, sha256 f7981ba2… (== stage/ExecGraderV6/DONE line).
  Wait for ../ExecGraderV6/DONE: bounded loop, DONE appeared at iteration 32 (of 45x60s). No BLOCKED.
- v6 run: `CRIT_TOOL=<v6-candidate.py> python3 -B stage/CriticO95/attacks_critic95.py` → rc 0,
  `BATTERY-SUMMARY survivors=10 refused=6 unnamed=0 traceback=0 clean=1 traceback-classes=0`
  (10 includes the ZWNJ1 control; fresh-class survivors = 9).
- v5 do-nothing baseline (frozen bytes 7957945d… over the identical fixtures): rc 0,
  `survivors=14 refused=2 unnamed=0 traceback=0 clean=1` → v6 closes exactly 4 of the 13 v5 survivors
  (RTL2, RTL3 via new `VERDICT-FORMAT` rc 2; FW3, LR2 via hardened TOPIC span), leaves 9 unchanged.
- Traceback evidence: `grep -c Traceback transcript-v5.txt` → 0; `grep -c Traceback transcript-v6.txt` → 0.
- G0: rc 0, `ENTRY-EVIDENCE: PASS legs=9/9` on both v5 and v6.

## Round-96 feed: the nine v6 survivors

1. Splitlines-severing verdict channels — VT1 (U+000B), FF1 (U+000C), LS1 (U+2028), NEL1 (U+0085): a forged
   gained `S001 LOCA<x>TED` line is severed by `str.splitlines()` in `dispositions()`; APPENDONLY never sees
   the gain. One mechanism, four codepoints.
2. Token-breakers NFKC cannot rejoin — NB1 (NBSP U+00A0, folds to a space inside the token), ANSI1 (ESC
   U+001B + `[31m` inside the token). Invisible to both the match path and the refused-probe path.
3. CYR1 (Cyrillic small-a U+0430 as the id letter): `_refuse_disguised` gates on `[Ss]\d{3,}` before the
   homoglyph probe, so a lookalike-id line is never probed.
4. BR1 (`## (1) address`) and DASH1 (`## - address`): v6's heading number-strip is enumerative (ASCII/roman/
   fullwidth dot-forms); any other leading token — `(1)`, `-`, and by extension `*`, `+`, `a)` — still rides
   along as a token and anchors the span floor.

Controls: RTL1 (U+202B before the id) refused on v5 and v6 via APPENDONLY — the inside-the-id variants were
the real channel and v6 closed them; FW2 (`## １. address`) refused on both via TOPIC (Python `\d` is
unicode-aware); ZWNJ1 (U+200C in a table-cell phrase) rc 0 on both — ZWNJ is in the disposition strip sets
(control confirmed), with a routed note that the TOPIC anchor path never strips zero-width characters
(false-refusal vector only).

Smallest safe corrections for a v7: refuse verdict-carrying id lines whose verdict token still contains a
non-letter byte after NFKC + strip + homoglyph folding (extends VERDICT-FORMAT to the whitespace/ESC family
and stops the splitlines blind spot if applied before line-severing); fold HOMOGLYPH_MAP before the
`_refuse_disguised` gate; replace the enumerated heading number-strip with a "leading token must be an
alphabetic word" rule.

## Discipline record

- Writes: stage dir only (`attacks_critic95.py`, `attacks.md`, `DONE`) + this trailer. No lane production
  files touched; no sibling lane; no fleet-root writes; no ~/.local/bin writes.
- No git/jj mutations (read-only `git show` for the v5 bytes into scratch); no pacman (guard active), no
  sysctl writes. Tooling installed/upgraded: none.
- Sources opened: none needed (no web evidence in this item). Scratch
  `/fast/scratch/hyaku/kotodama-r95/CriticO95` deleted before yield; recipes.txt sha256
  2e07c21b8d55666cd7a7e171f96a55e15bd8307896f94990ff0648d18ec241d5 (regenerable from the driver).
- What I could not measure: nothing material; both counting commands completed rc 0.
