# CriticClaims93 — claim O attack results (2026-11-05)

Target: frozen v4 entry mode of tools/check-advance-evidence.py (sha256
9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7, verified
before the run; matches claims.json O.tool_sha256). Ten counterfeit mini-lanes
built in scratch, each graded with the argument shape of
reports/round-93/battery93.py grade(). Full per-counterfeit records with rc,
verdict lines and commands: .ufo/waves/round-93/w1/stage/CriticClaims93/attacks.md.

## Counts

- Survivor count (rc 0, legs 9/9): **3** — A1, B1, G1.
- Unnamed-refusal count: **3** — 2 tracebacks (H1, I1: rc 1, Python traceback,
  no LEG lines, no named diagnostic) + 1 refusal not on the named leg (F1:
  gamed ENTRY, refused on TOPIC).
- Refused on the named leg: 4 — C1 (APPENDONLY), D1 (CAPTURE), E1 (GATE),
  J1 (APPENDONLY, but via a wrong-direction parse, see below).
- Harness controls: battery93 G0 fixture rc 0 (PASS legs=9/9); A5d bold-wrapped
  disposition rc 1 refused on APPENDONLY — harness reproduces frozen battery
  behavior.

## Survivor recipes

1. **A1 — Cyrillic lookalike in the verdict token.** Round lesson gains
   `- S001 LОCATED recheck moved — https://registry-example.org/base-old accessed 2026-11-05: "another old base row about dye plants"`
   with U+041E (Cyrillic О) inside LOCATED. dispositions() matches the verdict
   with `\b(NOT[ _-]?LOCATED|LOCATED)\b` on both the anchored rule and the v4
   case-sensitive fallback; the v4 zero-width strip (ZW_MAP =
   U+200B/200C/200D/2060/FEFF) does not fold lookalike scripts, so the gained
   line is invisible to APPENDONLY. rc 0, PASS legs=9/9.
2. **B1 — soft hyphen inside the verdict token.** Same line with
   `LOCA<U+00AD>TED`. U+00AD is not in ZW_MAP, so the token never matches.
   rc 0, PASS legs=9/9.
3. **G1 — numbered phrase-only headings defeat the v4 anchor guard.** Entry
   headings renamed to `## 1. address`, `## 2. petition`, `## 3. efficacy`,
   `## 4. table`, `## 5. Rites`. head_anchors() counts raw whitespace tokens
   after `#`; the list number (`1.`) is the second token, so a heading carrying
   nothing but a number and one bare sub-topic phrase anchors. Phrase anchors
   4/4 spanning 5 surfaces → TOPIC passes; nothing else changes. rc 0,
   PASS legs=9/9. This is the round-92 A4a span-gaming class surviving the v4
   countermeasure.

## Tracebacks (unnamed refusals)

- **H1** — manifest `rows` maps S955 to a JSON list: AttributeError
  `'list' object has no attribute 'get'` at check-advance-evidence.py:710
  (grade_entry GATE/CAPTURE loop; capture_error's `isinstance(m, dict)` guard
  is reached only after the unguarded `.get('url')` call). rc 1, traceback.
  The A6g fix pinned `rows` as list and manifest as array, not row values.
- **I1** — lands registry row truncated to 4 cells (`| S955 | <url> | docs | A |`):
  IndexError `list index out of range` at check-advance-evidence.py:615
  (NEWIDS `cells[3], cells[7], cells[8], cells[10]` has no length guard for
  new rows; BASEROWS guards only base rows). rc 1, traceback.

## Off-leg refusal and wrong-direction parse

- **F1** — entry with 8 content-free numbered h2 (`## 1.` … `## 8.`): ENTRY
  PASS (the heading counter reads `startswith('## ')` only); refusal came on
  TOPIC (anchors 2/4, span 1 < 3). Refused, but not on the leg the class games.
- **J1** — `- S001 NOT–LOCATED recheck unchanged …` (en-dash U+2013): the
  checker reads the verdict as LOCATED (`\bLOCATED\b` after the dash) and
  flags `disposition NOT-LOCATED -> LOCATED`. Refusal is on the named leg, but
  the line never asserts LOCATED — the flip detection misfires on a
  typographic dash.

## Smallest safe corrections (for the router; nothing changed by me)

- A1/B1: strip U+00AD and NFKC-fold the stripped line in dispositions() before
  matching, and refuse (named diagnostic) an id line whose verdict token
  contains non-ASCII letters, instead of silently not seeing it.
- G1: in head_anchors(), strip a leading list number (`^\d+[.)]`) before
  counting tokens, or require a non-numeric word in addition to the phrase.
- H1: guard `isinstance(man_rows[rid], dict)` with the A6g-style named refusal.
- I1: length-guard new-row cells (`< 11`) with a named refusal.

## Files written

- /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/CriticClaims93/attacks.md
- /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/CriticClaims93.md (this file)

## Numbers and commands (all 2026-11-05)

- `sha256sum tools/check-advance-evidence.py` → 9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7, rc 0.
- `R93_WORK=/fast/scratch/hyaku/kotodama-r93/CriticClaims93 python3 -B <scratch>/driver.py` → rc 0; graded 12 mini-lanes (10 counterfeits + 2 controls), one subprocess grader call each, 12 tool invocations total (10 rc 0/rc 1 as listed above, controls rc 0/rc 1).
- Fixture ground-truth greps (forged inputs present, rc 0): A1 lesson 1 hit, B1 lesson 1 hit, G1 entry 5 headings, J1 lesson 1 hit, I1 lands 1 short row, H1 manifest row type `list`.
- Tooling record: no installs or upgrades performed (none needed); no pacman transactions; no sysctl changes; no lane repo writes; no git mutations.
- Scratch /fast/scratch/hyaku/kotodama-r93/CriticClaims93 deleted before yield.
