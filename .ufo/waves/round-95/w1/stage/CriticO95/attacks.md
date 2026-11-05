# CriticO95 — routed-findings attack on grader v6 candidate (round 95)

Summary: **v6 SURVIVORS 9 of 15 fresh classes; REFUSED-NAMED 6; UNNAMED 0; TRACEBACK 0; G0 CLEAN rc 0.**
This is a routed-findings attack: survivors do NOT fail claim O (its predicate is the frozen 14); they feed round 96.
v5 baseline run on the same fixtures: 13 of 15 fresh classes survive v5; v6 closes exactly 4 (RTL2, RTL3, FW3, LR2) and leaves the other 9 byte-for-byte identical.

Candidate tested in place (never copied into the lane):
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ExecGraderV6/v6-candidate.py`,
sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` (matches `stage/ExecGraderV6/DONE`).
v5 baseline bytes: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 19aa4dd03dfd37b435d0b8ea5b313635d9d51592:tools/check-advance-evidence.py`,
sha256 `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff` (frozen v5).

Driver: `stage/CriticO95/attacks_critic95.py`. It imports the wave battery driver
`.ufo/waves/round-95/w1/stage/ExecBattery95/battery95.py` (sha256 `342237cdcc980d6e9eea7e281671e9a7eb168e7731d799ecd4b32ddd7d00fd38`)
read-only for `configure()`/`grade()`, so the invocation shape is battery95's own (entry mode, set B
`--min-anchor-span 3 --min-gate-overlap 3`, builder floors). battery95.py landed mid-wait and was used for
both the v5 baseline and the v6 run. Fixtures live only under scratch; nothing outside the stage dir is written.

Commands (both rc 0; counts are data):
```
S=/fast/scratch/hyaku/kotodama-r95/CriticO95
# v5 do-nothing baseline
CRIT_WORK=$S CRIT_BATTERY=<battery95.py> CRIT_TOOL=$S/grader_v5.py \
  CRIT_OUT_JSON=$S/results-v5.json python3 -B stage/CriticO95/attacks_critic95.py   # rc 0
# v6 candidate run (after ../ExecGraderV6/DONE appeared at wait iteration 32)
CRIT_WORK=$S CRIT_BATTERY=<battery95.py> CRIT_TOOL=<v6-candidate.py> \
  CRIT_OUT_JSON=$S/results-v6.json python3 -B stage/CriticO95/attacks_critic95.py   # rc 0
grep -c Traceback $S/transcript-v5.txt   # -> 0
grep -c Traceback $S/transcript-v6.txt   # -> 0
```

## Per-class results (15 fresh classes + G0 + ZWNJ1 control)

Fresh = not carried by the frozen battery (round-94 A1/B1/G1/H1/I1/J1/K1; round-95 adds CD1/LR1/TAB1/ID1/NUM1/RM1/NUM2)
nor by CriticO94's thirteen (FW1, MA1, CD1, LR1, TAB1, ID1, ZWJ1, CRLF1, NUM1, RM1, NUM2, SP1, MN1).

| id | bytes recipe (forged element on the G0 mini-lane) | v5 rc | v5 outcome | v6 rc | v6 outcome | v6 named diagnostic | verdict |
|---|---|---|---|---|---|---|---|
| G0 | clean control, no forgery | 0 | CLEAN (PASS 9/9) | 0 | CLEAN (PASS 9/9) | — | control ok |
| NB1 | NBSP U+00A0 in verdict: `S001 LOCA<U+00A0>TED recheck moved` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| VT1 | vertical tab U+000B in verdict: `S001 LOCA<U+000B>TED` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| FF1 | form feed U+000C in verdict: `S001 LOCA<U+000C>TED` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| LS1 | line separator U+2028 in verdict: `S001 LOCA<U+2028>TED` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| NEL1 | NEL U+0085 in verdict: `S001 LOCA<U+0085>TED` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| ANSI1 | ANSI CSI in verdict: `S001 LOCA<U+001B>[31mTED` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| RTL1 | RTL marking U+202B before the id: `<U+202B>S001 LOCATED ...` | 1 | REFUSED-NAMED | 1 | REFUSED-NAMED | `LEG FAIL APPENDONLY ... S001: gained a LOCATED line not present at base` | refused both (fallback reads it) |
| RTL2 | RTL marking U+202B inside the id: `S<U+202B>001 LOCATED` | 0 | SURVIVOR | 2 | REFUSED-NAMED | `line 4: verdict token carries a format character (VERDICT-FORMAT)` | **closed by v6** |
| RTL3 | RLO U+202E inside the id: `S<U+202E>001 LOCATED` | 0 | SURVIVOR | 2 | REFUSED-NAMED | `VERDICT-FORMAT` (same) | **closed by v6** |
| CYR1 | Cyrillic small-a U+0430 as the id letter: `<U+0430>001 LOCATED` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| FW2 | fullwidth dot-form heads `## １. address` (U+FF11 + `.`) | 1 | REFUSED-NAMED | 1 | REFUSED-NAMED | `LEG FAIL TOPIC ... phrase anchors span 1 heading/table surfaces < 3` | refused both (unicode `\d` strips it) |
| FW3 | fullwidth dotless heads `## １ address` | 0 | SURVIVOR | 1 | REFUSED-NAMED | `LEG FAIL TOPIC ... span 1 < 3` | **closed by v6** |
| LR2 | lowercase roman heads `## ii. address` / `iii.` / `iv.` / `v.` | 0 | SURVIVOR | 1 | REFUSED-NAMED | `LEG FAIL TOPIC ... span 1 < 3` | **closed by v6** |
| BR1 | bracketed heads `## (1) address` ... `## (4) table` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| DASH1 | separator-dash heads `## - address` ... `## - table` | 0 | SURVIVOR | 0 | SURVIVOR | none | **r96 survivor** |
| ZWNJ1 | control: ZWNJ U+200C inside a table-cell phrase `addr<U+200C>ess` | 0 | (rc 0) | 0 | (rc 0) | none | control, see below |

v6 tally line: `BATTERY-SUMMARY survivors=10 refused=6 unnamed=0 traceback=0 clean=1 traceback-classes=0`
(the 10 includes the ZWNJ1 control; fresh-class survivors on v6 are the 9 marked r96 above).
v5 tally line: `BATTERY-SUMMARY survivors=14 refused=2 unnamed=0 traceback=0 clean=1 traceback-classes=0`.

## Survivor recipes on v6 (minimal added bytes)

All are one forged element on the G0 fixture (`battery95.standard()` mini-lane; gained S001 lesson line tail:
` — https://registry-example.org/base-old accessed 2026-11-05: “another old base row about dye plants”`).
"Minimal" means as built, not proven minimal.

- **NB1**: lesson line `- S001 LOCA<U+00A0>TED recheck moved`. NFKC (the probe's normalizer) folds U+00A0 to a
  plain space, so even the refused-probe path sees `LOCA TED` — no contiguous LOCATED; the line is invisible.
- **VT1 / FF1 / LS1 / NEL1**: `- S001 LOCA<U+000B>TED` (likewise U+000C, U+2028, U+0085). Python `splitlines()`
  in `dispositions()` severs the gained line into `- S001 LOCA` + `TED recheck moved ...`; neither fragment
  matches, `_refuse_disguised`'s `[Ss]\d{3,}` gate sees `S001` but no verdict on the fragment. Four distinct
  codepoints, one mechanism.
- **ANSI1**: `- S001 LOCA<U+001B>[31mTED recheck moved`. ESC is not stripped, not NFKC-folded, not a homoglyph.
- **CYR1**: `- <U+0430>001 LOCATED recheck moved`. The `_refuse_disguised` gate requires `[Ss]\d{3,}` before it
  probes, so the Cyrillic-id line is never probed at all (HOMOGLYPH_MAP maps U+0430 to `a`, not to `S`).
- **BR1**: entry h2s `## (1) address`, `## (2) petition`, `## (3) efficacy`, `## (4) table`. `head_span_anchors`
  strips only `^\d+[.)]$`; `(1)` is not matched, so the number rides along as a token and all four heads anchor.
- **DASH1**: entry h2s `## - address`, `## - petition`, `## - efficacy`, `## - table`. A bare dash token plus a
  phrase word is two raw tokens and is never stripped — a rendered-separator look passes the span floor.

## G0 control

`CLASS G0 rc=0 ... outcome=CLEAN`, last line `ENTRY-EVIDENCE: PASS legs=9/9` on v5 and on v6. The fixture
machinery itself does not move the outcome.

## ZWNJ1 control (strip-set check, per assignment)

U+200C is in the disposition strip sets (`ZW_ONLY` and `ZW_MAP` in v5, carried by v6), so per the assignment
this fixture is a control, not a class. Observed: rc 0, PASS 9/9 on both v5 and v6 — the ZWNJ'd cell phrase
does not break the set-B floors because the heading carriers cover the phrase anchors. Two routed notes:
the strip only applies on the disposition path — the TOPIC anchor path (`norm()`) never strips zero-width
characters, so a ZWNJ in a phrase's *sole* carrier would be a false-refusal vector for honest entries; and a
ZWNJ-disguised verdict is read through on the disposition path (the battery's own ZWJ-family cases cover this).

## Do-nothing note (same fixtures against the v5 bytes)

The v5 run over the identical fixtures: 13 of 15 fresh classes survive v5 (NB1, VT1, FF1, LS1, NEL1, ANSI1,
RTL2, RTL3, CYR1, FW3, LR2, BR1, DASH1), 2 are refused-named on v5 too (RTL1 via APPENDONLY — the case-sensitive
fallback reads an RLE-prefixed line; FW2 via TOPIC — Python `\d` is unicode-aware, so `１.` already strips).
v6 closes exactly four of the thirteen (RTL2, RTL3 via the new VERDICT-FORMAT diagnostic; FW3, LR2 via the
hardened heading rule) and leaves the other nine with byte-identical outcomes (same rc, same 9/9 PASS).

## Traceback check

`grep -c Traceback transcript-v5.txt` → 0; `grep -c Traceback transcript-v6.txt` → 0. Per-class
`traceback-classes=0` in both tally lines. UNNAMED is 0 on both versions.

## Findings for the router (round 96 feed)

1. **The whitespace/format survivors share two mechanisms.** (a) `splitlines()` line-severing (VT1, FF1, LS1,
   NEL1): any of U+000B/U+000C/U+2028/U+0085 inside a forged gained line makes APPENDONLY blind while a human
   still reads `S001 LOCATED`. (b) token-breakers that NFKC cannot rejoin (NB1, ANSI1): U+00A0 folds to a space
   and U+001B stays, so neither the match path nor the refused-probe path sees `LOCATED`. A v7 candidate should
   refuse verdict-carrying id lines whose token, after NFKC + strip + homoglyph folding, still contains a
   non-letter byte between letters (VERDICT-FORMAT extension), or grade line-severed fragments as suspect.
2. **CYR1 exploits the refusal gate's order.** `_refuse_disguised` gates on `[Ss]\d{3,}` before probing, so a
   lookalike id never reaches the homoglyph probe. A pre-probe that folds HOMOGLYPH_MAP *before* the gate (or a
   gate that accepts the folded id) would catch `<U+0430>001 LOCATED`; as-is, a forger can publish dispositions
   under lookalike ids the grader cannot see.
3. **BR1/DASH1 show the heading rule is enumerative, not principled.** v6's head number-strip now accepts ASCII
   dot-forms, roman, and fullwidth digits (FW3/LR2 refused), but any first token that is not one of those
   enumerated shapes — `(1)`, `-`, and by extension `*`, `+`, `a)`, `一、` — still rides along as a token and
   anchors. A "leading token must be an alphabetic word" rule would close the whole family at once.
4. RTL1 was already refused on v5 (fallback reads prefix-marked lines); it is listed only to keep the family
   complete — the *inside-the-id* variants were the real channel, and v6 closed them.
5. The ZWNJ asymmetry (strip on the disposition path only, none on the TOPIC anchor path) is a false-refusal
   vector, not a forgery vector; low priority for r96.

## Tooling and writes

- Installed or upgraded tools: none. Tooling record: none. No pacman, no sysctl, no git/jj mutations; the v5
  bytes came from a read-only `git show` into scratch. Nothing outside the stage dir was written by this seat.
- Scratch `/fast/scratch/hyaku/kotodama-r95/CriticO95` (fixtures, transcripts, results-v5.json, results-v6.json,
  recipes.txt with per-fixture repr bytes, sha256 2e07c21b8d55666cd7a7e171f96a55e15bd8307896f94990ff0648d18ec241d5)
  is deleted before yield; the re-runnable commands above regenerate everything.
- Stage writes: `stage/CriticO95/attacks_critic95.py`, `stage/CriticO95/attacks.md` (this file),
  `stage/CriticO95/DONE`, plus the Report trailer `.ufo/waves/round-95/w1/CriticO95.md`.
