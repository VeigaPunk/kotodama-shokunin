# CriticO99 — attack report (round 99, w1)

Attack seat on claim O (operability, grader v10 → v11). Nothing here repairs the grader, edits a
driver or changes a pin. Detail and the full 77-class table: `stage/CriticO99/attacks.md`;
pre-landing recipes and their resolution: `stage/CriticO99/EARLY.md`; driver:
`stage/CriticO99/attacks_critic99.py`.

## Objects under test (read-only)

| object | sha256 |
|---|---|
| v11 final `tools/check-advance-evidence.py` | `717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2` (matches `V11-READY`) |
| v10 baseline `stage/ExecGraderV11/v10-base.py` | `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` (`git show 527df3fe:…` verified) |
| frozen battery `reports/round-99/controls/battery99.py` | `87f426aa3333a573ec2fa39cdd75c554d804401ecd903573f1831aef89c7a26d` |

Two intermediate v11 byte-sets (`a56965b5…`, `73b0355c…`) were superseded during the round and
are not re-runnable; their measurements are the EARLY.md record only.

## Commands and measured numbers

```
sha256sum tools/check-advance-evidence.py                                  # rc 0 -> 717341dc…
git show 527df3fe:tools/check-advance-evidence.py | sha256sum              # rc 0 -> d35b13c9…
sha256sum reports/round-99/controls/battery99.py                           # rc 0 -> 87f426aa…

CRIT_WORK=<scratch>/work-v10 CRIT_BATTERY=<lane>/reports/round-99/controls/battery99.py \
CRIT_TOOL=<lane>/.ufo/waves/round-99/w1/stage/ExecGraderV11/v10-base.py \
CRIT_OUT_JSON=<scratch>/v10.json python3 -B attacks_critic99.py             # rc 0
CRITIC-O99 survivors=26 unnamed=0 refused=20 traceback=0 overrefusal=23

CRIT_WORK=<scratch>/work-v11c CRIT_TOOL=<lane>/tools/check-advance-evidence.py \
CRIT_OUT_JSON=<scratch>/v11c.json python3 -B attacks_critic99.py            # rc 0
CRITIC-O99 survivors=32 unnamed=0 refused=14 traceback=0 overrefusal=0
OVERREFUSAL-PROBE n=0 ids=none

python3 -B reports/round-99/controls/battery99.py --tool <lane>/tools/check-advance-evidence.py \
--work <scratch>/battery-work                                              # rc 0
BATTERY-SUMMARY survivors=0 unnamed=0 refused=37 traceback=0 clean=9 not-clean=0

probe_twins.py / probe_suffix3.py / probe_nomark.py / probe_cyr.py on v10 and v11 final  # rc 0 each
```

75 assigned classes (28 benign, 47 attack) + 2 extra probes. The attack population includes the
25 CriticO98b attack classes re-run unchanged and the PLAINMOVE positive control. ExecGraderV11's
independent run of the same driver on the same bytes (`stage/ExecGraderV11/critic99-v11.txt`)
gives the identical line: `survivors=32 unnamed=0 refused=14 traceback=0 overrefusal=0`, benign
28/28 CLEAN, probe 2/2 CLEAN.

## Tallies

| tool | survivors | unnamed | refused | traceback | overrefusal (assigned benign) | probe overrefusal |
|---|---|---|---|---|---|---|
| v10 d35b13c9 | 26 | 0 | 20 | 0 | 23 | 2 |
| **v11 final 717341dc** | **32** | **0** | **14** | **0** | **0** | **0** |

Delta v10 → v11 final: 23 benign over-refusals repaired, 6 attacks newly surviving, 0 newly
refused, 0 unnamed, 0 traceback. CriticO98b set identical on both (24 survivors, same ids;
`V-MATHL` refused `VERDICT-COMBINE`; PLAINMOVE refused `APPENDONLY`). The five bare-numbering
benign classes (`## ⅻ.`, `## ①`, `## Ⅳ`, `## ４．`, `## ４`) are CLEAN on v11 final (F1
repaired).

## Over-refusals on v11 final

- Assigned benign set: **0**. All 28 CLEAN, including NFD Vietnamese, IPA, decomposed kana, the
  Indic scripts (Mc, nukta, anusvara, chandrabindu, virama, hasanta), Arabic harakat, Hebrew
  niqqud and the bare numbering headings.
- Extra probes: **0**. Decomposed Cyrillic `\u0435\u0301` and NFD French `pe\u0301titionnaire`
  were over-refused on the intermediate bytes and are CLEAN on the final bytes.

## Reopened forgeries

- **Load-bearing: none.** The dash forgery found on the first v11 bytes
  (`## 1. address <U+2014><U+093E>` x5: span 1 without the mark, span 5 with it) is refused on
  the final bytes (`HEADING-COMBINING` U+093E), as is the roman-numeral variant
  `## I<U+0301>. address` x5 (mark rc 1; mark-deleted twin rc 1, span 1 < 3).
- **Six new survivors vs v10, all measured anchor-neutral** (mark vs mark-deleted twins both
  rc 0): A-LATMARKINDIC, A-DEVLETTERMARK, A-MARKTOK-NUM, A-MARKTOK-FIRST, A-SUFFIX-MC,
  A-SUFFIX-VIS. In each fixture the heading anchors identically with and without the mark, so
  the mark forges nothing; the reopened surface is the v10 blanket refusal, not a forged anchor.
- **My proposed fix was refuted by measurement.** EARLY.md's "treat U+0300–U+036F as neutral on
  any letter base" would accept `## I<U+0301>. address` x5 while the mark-free twin fails
  span 1 < 3 (ExecGraderV11's ROMANMARK counterexample; reproduced here on the final bytes).
  The landed invariant — a mark must not change `(head_anchors, head_span_anchors)` — is the
  correct fix. The second correction (whole-token phrase match instead of substring) was
  adopted.

## Pre-existing residuals (v10 and v11 final; not regressions)

- `A-DEVLETTERDIGIT` `## 1<U+0930>. address` x5: a Devanagari letter after a digit defeats the
  number strip and supplies the second content token.
- `A-ZWJDIGIT` `## 1<U+200D>. address` x5: Cf on the digit; v10 refused it only through the
  removed HEADING-NUMBER loop, so its survival is a consequence of the F1 fix, not the mark rule.
- The 24 CriticO98b survivors (14 verdict-window, 10 heading list-mark), unchanged.

## Three most dangerous residuals (route to round 100; not implemented)

1. **V-SPACE-MID** — a plain space inside the verdict token (`LOCA TED`) survives both tools and
   needs no exotic byte. Fix: extend the verdict window to whitespace-split `LOCA`/`TED` and
   refuse `VERDICT-WHITESPACE`.
2. **A-DEVLETTERDIGIT** — a digit + letter numbering token counts as content. Fix: a token whose
   first character is a digit is a numbering token, never a content token.
3. **H-LETTER / H-COLON** — ASCII list marks still anchor phrase-only headings (`## A. address`,
   `## 1: address`). Fix: strip an ASCII letter or digit+colon list mark in `_content_toks` the
   same way `_NUM2` strips digits and dashes.

## Axis and claim impact

Operability only. The frozen legs are unaffected on the landed bytes (battery99 `0/0/37/0/9/0`
measured here rc 0; critic98 `survivors=24 overrefusal=0`; critic97 and the 34 REG lines
unchanged; selftest `PASS 175/175` per ExecGraderV11 receipts), so the canonical counter passes
v11 final and claim O is not failed by this artifact. The two probes, the six anchor-neutral
survivors and the pre-existing residuals sit outside the frozen class sets — the
residual_honesty gap CriticO99 exists to measure — and are routed to round 100. The v10 → v11
mark/numbering repair is sound on the assigned benign set (23/23 over-refusals repaired) and
reopens no load-bearing forgery.

Tooling installed or upgraded: none. Scratch `/fast/scratch/hyaku/kotodama-r99/CriticO99/`
removed before yield. Nothing committed.
