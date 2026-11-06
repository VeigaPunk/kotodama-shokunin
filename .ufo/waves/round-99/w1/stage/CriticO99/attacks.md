# CriticO99 — fresh counterfeit classes against v11 (round 99, w1)

Attack seat. Nothing here repairs the grader, edits a driver or changes a pin. battery99
remains the frozen predicate; this artifact is outside its coverage by construction. EARLY.md
carries the defects ExecGraderV11 acted on before landing; this file is the final table over the
landed bytes.

## Objects under test (all read-only)

| object | sha256 | source |
|---|---|---|
| **v11 final** `tools/check-advance-evidence.py` | `717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2` | lane file; matches `V11-READY` |
| v10 baseline `.ufo/waves/round-99/w1/stage/ExecGraderV11/v10-base.py` | `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` | `git show 527df3fe:tools/check-advance-evidence.py` (verified) |
| frozen battery `reports/round-99/controls/battery99.py` | `87f426aa3333a573ec2fa39cdd75c554d804401ecd903573f1831aef89c7a26d` | matches the control receipt |

Two intermediate v11 byte-sets (`a56965b5…`, `73b0355c…`) were superseded during the round and
are not re-runnable; their measurements are the EARLY.md record only.

Driver: `attacks_critic99.py` (this stage). It imports battery99 read-only via importlib and
uses the battery's own `configure/grade/standard/_reps/_heads97/_dispo97/mc/GAINED_TAIL`, so
every fixture is byte-for-byte the battery's shape: the standard mini-lane whose entry is
`mc.body(None)` with the five anchoring h2 headings, graded with battery99's exact argv
(`--min-topic-phrases 4 --min-anchor-span 3 --min-headings 4 ...`). 77 classes: 28 benign
(must be CLEAN), 47 attack (must be REFUSED; includes the 25 CriticO98b attack classes and the
PLAINMOVE positive control), 2 extra probes (valid orthography outside the assigned benign set,
tallied separately).

## Commands and tallies

```
sha256sum tools/check-advance-evidence.py                                    # rc 0 -> 717341dc…
git show 527df3fe:tools/check-advance-evidence.py | sha256sum                # rc 0 -> d35b13c9…
sha256sum reports/round-99/controls/battery99.py                             # rc 0 -> 87f426aa…

CRIT_WORK=<scratch>/work-v10 CRIT_BATTERY=<lane>/reports/round-99/controls/battery99.py \
CRIT_TOOL=<lane>/.ufo/waves/round-99/w1/stage/ExecGraderV11/v10-base.py \
CRIT_OUT_JSON=<scratch>/v10.json python3 -B attacks_critic99.py               # rc 0
CRITIC-O99 survivors=26 unnamed=0 refused=20 traceback=0 overrefusal=23

CRIT_WORK=<scratch>/work-v11c CRIT_BATTERY=… CRIT_TOOL=<lane>/tools/check-advance-evidence.py \
CRIT_OUT_JSON=<scratch>/v11c.json python3 -B attacks_critic99.py              # rc 0
CRITIC-O99 survivors=32 unnamed=0 refused=14 traceback=0 overrefusal=0
OVERREFUSAL-PROBE n=0 ids=none

python3 -B reports/round-99/controls/battery99.py --tool <lane>/tools/check-advance-evidence.py \
--work <scratch>/battery-work                                                 # rc 0
BATTERY-SUMMARY survivors=0 unnamed=0 refused=37 traceback=0 clean=9 not-clean=0
```

ExecGraderV11's independent run of the same driver on the same bytes
(`stage/ExecGraderV11/critic99-v11.txt`) gives the identical line:
`CRITIC-O99 survivors=32 unnamed=0 refused=14 traceback=0 overrefusal=0`, benign 28/28 CLEAN,
probe 2/2 CLEAN.

Population subtallies (same runs):

| population | n | v10 survivors / refused / clean / overrefusal | v11 final |
|---|---|---|---|
| benign (assigned) | 28 | 0 / 0 / 5 / **23** | 0 / 0 / **28** / **0** |
| attack | 47 | 26 / 21 / 0 / 0 | 32 / 15 / 0 / 0 |
| probe (extra) | 2 | 0 / 0 / 0 / 2 | 0 / 0 / **2** / **0** |

Delta v10 → v11 final over the 75 assigned classes: **23 benign over-refusals repaired, 6
attacks newly surviving, 0 classes newly refused, 0 unnamed, 0 traceback.** All six new
survivors are measured anchor-neutral (below); none is a forgery.

- **CriticO98b replay is unchanged:** the 25 attack classes give 24 survivors on v10 and the
  same 24 on v11 final (identical id set), `V-MATHL` refused on both (`VERDICT-COMBINE`),
  PLAINMOVE refused on both (`APPENDONLY`). No new survivor among them.
- **F1 is repaired:** all five bare-numbering benign classes (`## ⅻ.`, `## ①`, `## Ⅳ`,
  `## ４．`, `## ４`) are CLEAN on v11 final and were HEADING-NUMBER over-refusals on v10.
- **F4 is repaired:** every assigned benign class is CLEAN on v11 final (0 over-refusals),
  including NFD Vietnamese, IPA, decomposed kana, the Indic scripts, Arabic harakat, Hebrew
  niqqud and the bare numbering headings. The two extra probes (decomposed Cyrillic, NFD French
  `pétitionnaire`) are also CLEAN.

## Benign set (28 assigned; must be CLEAN on a correct v11)

| id | v10 d35b13c9 | v11 final 717341dc |
|---|---|---|
| G0C | 0 / CLEAN / none | 0 / CLEAN / none |
| OK-CIRC | 0 / CLEAN / none | 0 / CLEAN / none |
| OK-LETTER | 0 / CLEAN / none | 0 / CLEAN / none |
| OK-NUMERO | 0 / CLEAN / none | 0 / CLEAN / none |
| OK-MCWORD | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-DEVAHEAD | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-BENG | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-BENG-HASANTA | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-TAMIL | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-THAI | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-KHMER | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-MYANMAR | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-TIBETAN | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-JAPAN-NFD | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-ARABIC | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-HEBREW | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-VIETNFC | 0 / CLEAN / none | 0 / CLEAN / none |
| OK-VIETNFD | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-IPA | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-DEVANUKTA | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-DEVANUSVARA | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-DEVACHANDRA | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |
| OK-BAREROMAN | 1 / OVERREFUSAL / HEADING-NUMBER,TOPIC | 0 / CLEAN / none |
| OK-BARECIRC | 1 / OVERREFUSAL / HEADING-NUMBER,TOPIC | 0 / CLEAN / none |
| OK-BARENODOT | 1 / OVERREFUSAL / HEADING-NUMBER,TOPIC | 0 / CLEAN / none |
| OK-BAREFW-NODOT | 1 / OVERREFUSAL / HEADING-NUMBER,TOPIC | 0 / CLEAN / none |
| OK-BAREFW | 1 / OVERREFUSAL / HEADING-NUMBER,TOPIC | 0 / CLEAN / none |
| OK-MCWORD-DEVAA | 1 / OVERREFUSAL / HEADING-COMBINING,TOPIC | 0 / CLEAN / none |

Byte recipes (all appended to, or substituted into, the standard body):

- Script words appended to `## 4. Efficacy` as `## 4. Efficacy — <word>`: OK-BENG
  `\u09ac\u09be\u0982\u09b2\u09be`, OK-BENG-HASANTA `\u0995\u09cd\u09b7`, OK-TAMIL
  `\u0ba4\u0bae\u0bbf\u0bb4\u0bcd`, OK-THAI `\u0e19\u0e49\u0e33`, OK-KHMER
  `\u1781\u17d2\u1798\u17c2\u179a`, OK-MYANMAR `\u1019\u103c\u1014\u103a\u1019\u102c`,
  OK-TIBETAN `\u0f56\u0f7c\u0f51`, OK-ARABIC `\u0643\u0650\u062a\u064e\u0627\u0628` (harakat),
  OK-HEBREW `\u05e1\u05b5\u05e4\u05b6\u05e8` (niqqud), OK-VIETNFC `ti\u1ebfng Vi\u1ec7t`,
  OK-VIETNFD `tie\u0302\u0301ng Vie\u0302\u0323t`, OK-IPA `n\u0325 a\u0303`,
  OK-DEVANUKTA `\u0915\u093c\u0932\u092e`, OK-DEVANUSVARA `\u0938\u0902\u0938\u094d\u0915\u0943\u0924`,
  OK-DEVACHANDRA `\u0939\u0901\u0938\u0940`, OK-JAPAN-NFD `\u304b\u3099`.
- Bare numbering headings appended after the body (NUMOK1/NUMOK2 pattern): OK-BAREROMAN
  `## \u217b.`, OK-BARECIRC `## \u2460`, OK-BARENODOT `## \u2163`, OK-BAREFW-NODOT `## \uff14`,
  OK-BAREFW `## \uff14\uff0e`.
- OK-MCWORD-DEVAA: `## addre\u093ess address` style on all five heads (the OK-MCWORD shape
  with Mc U+093E instead of visarga).

## Extra probes (2; valid orthography outside the assigned set)

| id | recipe | v10 | v11 final |
|---|---|---|---|
| OK-CYR-NFD | `## 4. Efficacy — \u0435\u0301` (Cyrillic ie + combining acute, decomposed stress) | 1 / OVERREFUSAL | **0 / CLEAN / none** |
| OK-FR-PETITION | `## 4. Efficacy — pe\u0301titionnaire` (French NFD; the mark-free token contains `petition` as a proper substring) | 1 / OVERREFUSAL | **0 / CLEAN / none** |

## Attack set (47; must be REFUSED)

| id | v10 d35b13c9 | v11 final 717341dc |
|---|---|---|
| A-MCONDIGIT | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-VISARGADIGIT | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-NUKTADIGIT | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-MARKTOK | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-MARKTOK-LAT | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-DEVLETTERDIGIT | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| A-LATMARKINDIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 0 / SURVIVOR / none |
| A-DEVLETTERMARK | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 0 / SURVIVOR / none |
| A-MIXROMANDIGIT | 1 / REFUSED-NAMED / TOPIC | 1 / REFUSED-NAMED / TOPIC |
| A-MIXCIRCDIGIT | 1 / REFUSED-NAMED / TOPIC | 1 / REFUSED-NAMED / TOPIC |
| A-FWPERMARK | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / TOPIC |
| A-MARKTOK-NUM | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 0 / SURVIVOR / none |
| A-MARKTOK-FIRST | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 0 / SURVIVOR / none |
| A-ZWJDIGIT | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| A-DASH-MC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-DASH-VIS | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-DASH-LAT | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| A-DASH-NOMARK | 1 / REFUSED-NAMED / TOPIC | 1 / REFUSED-NAMED / TOPIC |
| A-SUFFIX-MC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 0 / SURVIVOR / none |
| A-SUFFIX-VIS | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 0 / SURVIVOR / none |
| A-SUFFIX-LAT | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC | 1 / REFUSED-NAMED / HEADING-COMBINING,TOPIC |
| PLAINMOVE | 1 / REFUSED-CONTROL / APPENDONLY | 1 / REFUSED-CONTROL / APPENDONLY |
| V-PO-MIDDOT | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-PO-BULLET | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-PO-DOTLEAD | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-SO-COPY | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-SO-REG | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-SK-CIRC | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-LM-SUPH | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-CO-PUA | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-CN-UNASSIGNED | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-LU-OSTROKE | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-LU-LSTROKE | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-LU-ETH | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-TAB-MID | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-SPACE-MID | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| V-MATHL | 2 / REFUSED-NAMED / VERDICT-COMBINE | 2 / REFUSED-NAMED / VERDICT-COMBINE |
| H-LETTER | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-COLON | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-BULLET | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-SECTION | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-NUMERO | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-DEGNUM | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-PARENLETTER | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-TRIPLENUM | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-CIRCLEDLETTER | 0 / SURVIVOR / none | 0 / SURVIVOR / none |
| H-HASH | 0 / SURVIVOR / none | 0 / SURVIVOR / none |

Byte recipes for the classes this round adds (all five heads, phrase-only unless stated):

- A-MCONDIGIT `## 1<U+093E>. address` … ; A-VISARGADIGIT `## 1<U+0903>. address` … ;
  A-NUKTADIGIT `## 1<U+093C>. address` … ; A-FWPERMARK `## 1<U+093E><U+FF0E> address` ….
- A-MARKTOK `## address <U+093E>` … ; A-MARKTOK-LAT `## address <U+0301>` … ;
  A-MARKTOK-FIRST `## <U+093E>. address` … ; A-MARKTOK-NUM `## 1. address <U+093E>` ….
- A-LATMARKINDIC `## address <U+0930><U+0301>` … ; A-DEVLETTERMARK `## 1<U+0930><U+0301>. address` … ;
  A-DEVLETTERDIGIT `## 1<U+0930>. address` … (no mark).
- A-MIXROMANDIGIT `## <U+2163>1. address` … ; A-MIXCIRCDIGIT `## 1<U+2460>. address` ….
- A-ZWJDIGIT `## 1<U+200D>. address` … (ZWJ, Cf, no mark).
- A-DASH-MC `## 1. address <U+2014><U+093E>` … ; A-DASH-VIS with U+0903 ; A-DASH-LAT with
  U+0301 ; A-DASH-NOMARK `## 1. address <U+2014>` ….
- A-SUFFIX-MC `## 1. address<U+093E> Notes` … ; A-SUFFIX-VIS with U+0903 ; A-SUFFIX-LAT with
  U+0301.

## The six new survivors are anchor-neutral (measured twins)

`probe_twins.py` / `probe_suffix3.py` (rc 0 each) grade each fixture with the mark and with the
mark deleted (`entry.replace(mark, '')`), same bytes otherwise:

| id | mark rc | mark-deleted rc | load-bearing? |
|---|---|---|---|
| A-LATMARKINDIC `## <U+0930><U+0301> address` | 0 | 0 | no |
| A-DEVLETTERMARK `## 1<U+0930><U+0301>. address` | 0 | 0 | no |
| A-MARKTOK-NUM `## 1. address <U+093E> address` | 0 | 0 | no |
| A-MARKTOK-FIRST `## <U+093E>. address address` | 0 | 0 | no |
| A-SUFFIX-MC `## 1. address<U+093E> Notes` | 0 | 0 | no |
| A-SUFFIX-VIS `## 1. address<U+0903> Notes` | 0 | 0 | no |

The load-bearing twins stay refused: A-MARKTOK `## <U+093E> address` mark rc 1 (mark-deleted
rc 1 on the phrase count), A-DASH-MC mark rc 1 (mark-deleted rc 1, span 1 < 3), and the new
ROMANMARK pin `## I<U+0301>. address` mark rc 1 (mark-deleted rc 1, span 1 < 3). The invariant
ExecGraderV11 landed — a mark must not change `(head_anchors, head_span_anchors)` — is what
makes the six survivors harmless: in each, the heading anchors identically with and without the
mark, so the mark forges nothing.

## My proposed fix was refuted (recorded)

EARLY.md's first correction proposed treating U+0300–U+036F as neutral on any letter base.
ExecGraderV11 measured that this accepts `## I<U+0301>. address` x5 (rc 0) while the mark-free
twin `## I. address` x5 fails span 1 < 3 — the CM1 family with a roman numeral instead of a
digit. I reproduced the twin on the final bytes: ROMANMARK mark rc 1 `HEADING-COMBINING`,
mark-deleted rc 1 `span 1 < 3`. The anchor-invariance rule is the correct fix; the base/mark
taxonomy I proposed was not. The second correction (whole-token phrase match instead of
substring) was adopted and OK-FR-PETITION is CLEAN.

## Pre-existing residuals (v10 and v11 final; not regressions)

- A-DEVLETTERDIGIT `## 1<U+0930>. address` x5 (digit + Devanagari letter, no mark): rc 0 on
  both. A token that starts with a digit but carries a letter is not classified as a number, so
  it supplies the second content token.
- A-ZWJDIGIT `## 1<U+200D>. address` x5 (ZWJ U+200D, Cf): rc 0 on both. v10 refused it only
  through the now-removed HEADING-NUMBER loop, which fired on the token shape, not on a mark;
  with the loop gone there is no Cf heading check. A consequence of the F1 fix, not a mark-rule
  regression.
- The 24 CriticO98b attack classes (14 verdict-window, 10 heading list-mark): identical
  survivor set on v10 and v11 final, as claim O4 bounds them (`survivors <= 24`).

## Three most dangerous residuals (route to round 100; not implemented here)

1. **V-SPACE-MID — a plain space inside the verdict token (`LOCA TED`) survives.** It needs no
   exotic byte at all and survives both tools. One-line fix: extend the verdict window to
   whitespace-split `LOCA`/`TED` and refuse `VERDICT-WHITESPACE`.
2. **A-DEVLETTERDIGIT — a digit + letter numbering token counts as content.** One-line fix: a
   token whose first character is a digit is a numbering token, never a content token.
3. **H-LETTER / H-COLON — ASCII list marks still anchor phrase-only headings** (`## A. address`,
   `## 1: address`). One-line fix: strip an ASCII letter or digit+colon list mark from
   `_content_toks` the same way `_NUM2` strips digits and dashes.

## Axis and claim impact

Impacted axis: operability only. On the landed bytes the frozen legs are unaffected — battery99
`0/0/37/0/9/0` (measured here, rc 0), critic98 `survivors=24 overrefusal=0`, critic97 and the 34
REG lines unchanged, selftest `PASS 175/175` (ExecGraderV11 receipts) — so the canonical counter
passes v11 final and claim O is not failed by this artifact. The two probes, the six
anchor-neutral survivors and the pre-existing residuals sit outside the frozen class sets: they
are the residual_honesty gap CriticO99 exists to measure, routed to round 100. The v10 → v11
mark/numbering repair is sound on the assigned benign set (23/23 over-refusals repaired) and
reopens no load-bearing forgery.
