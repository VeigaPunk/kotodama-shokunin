# CriticO97 — fresh-counterfeit attack on grader v9 (round 97)

Summary: **v9 survivors=8 unnamed=0 refused=17 traceback=0** (28 fixtures: 25 attacks + 3 controls G0, H-CRLF, H-CR; v8 classifies the same 28 as 19 + 6 + 3 CLEAN).
Do-nothing baseline v8 (export of `tools/check-advance-evidence.py` at 1ffc5a83): **v8 survivors=19 unnamed=0 refused=6 traceback=0**.
CriticO96 replay over v9: **CRITIC-O96 survivors=0 unnamed=0 refused=19 traceback=0** (v8 replay of the same driver measured survivors=7 in critic96-on-v8.txt).
Frozen predicate is unchanged: battery97.py. This seat did not edit any grader, driver, or pin.

Dependency note: `stage/ExecGraderV9/DONE` never appeared inside the bounded 90x60 s loop. `stage/ExecGraderV9/V9-READY` did exist, and its sha256 (1021dc9d…) equals the current bytes of `tools/check-advance-evidence.py`. I attacked those bytes in place, through a read-only copy (`v9-snapshot.py`, sha re-checked before and after the run: unchanged). This is a deviation from the DONE-gated instruction and is flagged here and in the Report.

## Tallies (driver stdout, both runs rc 0, `Wall time` 1.2–2.7 s)

```
v8 (do-nothing baseline):  CRITIC-O97 survivors=19 unnamed=0 refused=6 traceback=0
v9 (under attack):         CRITIC-O97 survivors=8 unnamed=0 refused=17 traceback=0
CriticO96 replay on v9:    CRITIC-O96 survivors=0 unnamed=0 refused=19 traceback=0
```

## Positive controls (rc recorded; they prove the fixture reaches the verdict check)

- Plain `- S001 LOCATED recheck moved — <base-old url> accessed 2026-11-05: “another old base row about dye plants”` on v9: rc 1, `ENTRY-EVIDENCE: FAIL legs=8/9 failed=APPENDONLY` (POS-LOCATED-plain).
- Same line with `LOCA<U+007F>TED` on v9: rc 0, `ENTRY-EVIDENCE: PASS legs=9/9`. Same with `LOCA<U+20DD>TED`: rc 0, PASS 9/9. So the two verdict survivors below are real, not fixture artifacts.
- ASCII heading control on v9 (`## 1. address` … `## 5. Notes`, five phrase-only h2s): rc 1, `FAIL legs=8/9 failed=TOPIC`.
- Non-ASCII numbering on v9 (`## Ⅰ. address` … and `## 1． address` …): rc 0, PASS 9/9. The same shape with an ASCII number is refused, so the gap is the numbering token.

## Attack table (rc, outcome and named diagnostic on v9 and v8)

Recipe bytes: `<U+XXXX>` is the exact codepoint. Verdict-channel rows put the token where LOCATED stands in a gained `- S001 … recheck moved` line (battery96 GAINED_TAIL). Heading rows are five h2 lines `## <prefix> <phrase>`, one per phrase (`address`, `petition`, `efficacy`, `table`, `Notes`).

| id | byte recipe | v9 rc | v9 outcome / named | v8 rc | v8 outcome / named |
|---|---|---|---|---|---|
| G0 | clean control | 0 | CLEAN | 0 | CLEAN |
| BEL1 | verdict `LOCA<U+0007>TED` | 2 | REFUSED-NAMED `VERDICT-CTRL` | 0 | SURVIVOR |
| **DEL1** | verdict `LOCA<U+007F>TED` | **0** | **SURVIVOR (unnamed pass, PASS 9/9)** | 0 | SURVIVOR |
| SUB1 | verdict `LOCA<U+001A>TED` | 2 | REFUSED-NAMED `VERDICT-CTRL` | 0 | SURVIVOR |
| ENQ1 | verdict `LOCA<U+2000>TED` | 2 | REFUSED-NAMED `VERDICT-SEPARATOR` | 0 | SURVIVOR |
| ENSP1 | verdict `LOCA<U+2002>TED` | 2 | REFUSED-NAMED `VERDICT-SEPARATOR` | 0 | SURVIVOR |
| FIGSP1 | verdict `LOCA<U+2007>TED` | 2 | REFUSED-NAMED `VERDICT-SEPARATOR` | 0 | SURVIVOR |
| THINSP1 | verdict `LOCA<U+2009>TED` | 2 | REFUSED-NAMED `VERDICT-SEPARATOR` | 0 | SURVIVOR |
| HAIRSP1 | verdict `LOCA<U+200A>TED` | 2 | REFUSED-NAMED `VERDICT-SEPARATOR` | 0 | SURVIVOR |
| NNBP1 | verdict `LOCA<U+202F>TED` | 2 | REFUSED-NAMED `VERDICT-SEPARATOR` | 0 | SURVIVOR |
| MMSP1 | verdict `LOCA<U+205F>TED` | 2 | REFUSED-NAMED `VERDICT-SEPARATOR` | 0 | SURVIVOR |
| **ENC1** | verdict `LOCA<U+20DD>TED` | **0** | **SURVIVOR (unnamed pass, PASS 9/9)** | 0 | SURVIVOR |
| VS16VT | verdict `LOCA<U+FE0F>TED` | 2 | REFUSED-NAMED `VERDICT-COMBINE` | 2 | REFUSED-NAMED `VERDICT-COMBINE` |
| FEFFVT1 | verdict `LOCA<U+FEFF>TED` | 1 | REFUSED-NAMED `APPENDONLY` | 1 | REFUSED-NAMED `APPENDONLY` |
| BOM1 | line start `<U+FEFF>- S001 LOCATED recheck moved` | 1 | REFUSED-NAMED `APPENDONLY` | 1 | REFUSED-NAMED `APPENDONLY` |
| CMID1 | id `S00<U+0301>1 LOCATED` | 2 | REFUSED-NAMED `VERDICT-COMBINE` | 2 | REFUSED-NAMED `VERDICT-COMBINE` |
| ENCH1 | number `1<U+20DD>.` x5 | 1 | REFUSED-NAMED `HEADING-COMBINING`, `TOPIC` | 0 | SURVIVOR |
| VSH1 | number `1<U+FE0F>.` x5 | 1 | REFUSED-NAMED `HEADING-COMBINING`, `TOPIC` | 0 | SURVIVOR |
| **ROMAN1** | number `<U+2160>.`…`<U+2164>.` x5 | **0** | **SURVIVOR (span gamed: 5 phrase-only heads, PASS 9/9)** | 0 | SURVIVOR |
| **SUP1** | number `<U+00B9>.` `<U+00B2>.` `<U+00B3>.` `<U+2074>.` `<U+2075>.` x5 | **0** | **SURVIVOR (same span gap)** | 0 | SURVIVOR |
| FWNUMH1 | number `<U+FF11>.`…`<U+FF15>.` x5 | 1 | REFUSED-NAMED `TOPIC` | 1 | REFUSED-NAMED `TOPIC` |
| **FWPER1** | number `1<U+FF0E>` … `5<U+FF0E>` x5 | **0** | **SURVIVOR (same span gap)** | 0 | SURVIVOR |
| CYRH1 | `## <U+0430>ddress address` etc. (junk + clean twin) | 0 | SURVIVOR (benign: clean twin anchors the phrase) | 0 | SURVIVOR |
| ZWSH1 | `## add<U+200B>ress address` etc. (junk + clean twin) | 0 | SURVIVOR (benign: clean twin anchors the phrase) | 0 | SURVIVOR |
| BELH1 | `## 1. add<U+0007>ress address` etc. (junk + clean twin) | 0 | SURVIVOR (benign: clean twin anchors the phrase) | 0 | SURVIVOR |
| NELH1 | `## 1. add<U+0085>ress address` etc. (junk + clean twin) | 1 | REFUSED-NAMED `TOPIC` | 1 | REFUSED-NAMED `TOPIC` |
| H-CRLF | control: five h2 lines end `\r\n` | 0 | CLEAN | 0 | CLEAN |
| H-CR | control: five h2 lines joined by lone `\r` | 0 | CLEAN | 0 | CLEAN |

Named-diagnostic rule: a refusal is REFUSED-NAMED when the output carries `FAIL <LEG>` or a `(UPPER-DIAG)` token. Any traceback is TRACEBACK; no row above is TRACEBACK or REFUSED-UNNAMED.

Fixture-design note (admitted): CYRH1, ZWSH1 and BELH1 each put a clean copy of the phrase in the same heading, so they cannot gain an anchor. They count as survivors under the protocol but are not forgeries. They should be read as controls for the heading-anchor path, not as attacks.

Round-97 fresh-class coverage confirmed absent from battery97.py before the run: U+0007, U+007F, U+001A, U+2000, U+2002, U+2007, U+2009, U+200A, U+202F, U+205F, U+20DD, U+FE0F, U+FF0E, U+2160, U+00B9, U+2074, U+FF11 have zero occurrences; U+0430 occurs only in CYR1 (id letter), U+200B only in a comment.

## The three most dangerous v9 survivors (routed to round 98; NOT implemented)

1. **ENC1 — a gained LOCATED verdict with a combining enclosing circle U+20DD (category Me) passes APPENDONLY unnamed.**
   Evidence: positive control (plain LOCATED refused; `LOCA<U+20DD>TED` PASS 9/9).
   Cause [INFERENCE from the code path, not a traced run]: `VERDICT-COMBINE` in `_refuse_verdict_channel` tests `unicodedata.category(c) == 'Mn'` only, so an Me byte is never named and the span fails the DISPO match silently.
   One-line fix: in the verdict-window check, refuse any span byte whose `unicodedata.category(c)[0] in 'M'` (all combining classes, Mn/Mc/Me) as `VERDICT-COMBINE`.

2. **ROMAN1 / SUP1 / FWPER1 — non-ASCII numbering tokens count as heading content and reopen span-gaming.**
   Evidence: heading positive control (ASCII `1.` phrase-only heads refused on TOPIC; `Ⅰ.` and `1．` pass 9/9).
   Cause [INFERENCE from the code path]: `_content_toks` strips numbering with `_NUM2`, which is ASCII-only, so `Ⅰ.`, `¹.` and `1．` count as content tokens and each phrase-only heading reaches the span floor of 2.
   One-line fix: `toks = [t for t in raw if not isnum(t) and any(c.isalpha() for c in t)]` in `_content_toks`, so only alphabetic tokens count toward the span.

3. **DEL1 — a gained LOCATED verdict with U+007F DELETE passes APPENDONLY unnamed.**
   Evidence: positive control (`LOCA<U+007F>TED` PASS 9/9). Its neighbours BEL1, SUB1, NUL1, CR1 and US1 are named `VERDICT-CTRL` while DEL1 is not, which places U+007F outside the verdict-window control set [INFERENCE from the named/unnamed split; the set itself was not printed].
   One-line fix: add U+007F to the verdict-window control set (or refuse any category `Cc` byte inside the span).

Not dangerous (survivors, benign): CYRH1, ZWSH1, BELH1 (see design note).

## Replay commands (scratch paths; rc 0 each, counts are data)

```
S=/fast/scratch/hyaku/kotodama-r97/CriticO97
ST=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-97/w1/stage
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1ffc5a83d2c70e3bc581594efbcf32c562ba2569:tools/check-advance-evidence.py > $S/v8-base.py   # sha f29ab013…, rc 0
CRIT_WORK=$S CRIT_BATTERY=$ST/ExecBattery97/battery97.py CRIT_TOOL=$S/v8-base.py CRIT_OUT_JSON=$S/r8.json python3 -B $ST/CriticO97/attacks_critic97.py   # CRITIC-O97 survivors=19 unnamed=0 refused=6 traceback=0, rc 0
cp tools/check-advance-evidence.py $S/v9-snapshot.py                                                    # sha 1021dc9d…, rc 0
CRIT_WORK=$S CRIT_BATTERY=$ST/ExecBattery97/battery97.py CRIT_TOOL=$S/v9-snapshot.py CRIT_OUT_JSON=$S/r9.json python3 -B $ST/CriticO97/attacks_critic97.py   # CRITIC-O97 survivors=8 unnamed=0 refused=17 traceback=0, rc 0
CRIT_WORK=$S/replay96 CRIT_BATTERY=$ST/ExecBattery97/battery97.py CRIT_TOOL=$S/v9-snapshot.py CRIT_OUT_JSON=$S/r96.json python3 -B .ufo/waves/round-96/w1/stage/CriticO96/attacks_critic96.py   # CRITIC-O96 survivors=0 unnamed=0 refused=19 traceback=0, rc 0
```

Driver: `stage/CriticO97/attacks_critic97.py` (new this round; 28 fixtures = 25 attacks + 3 controls; attacks read-only battery97 via `configure/standard/grade`). Driver sha256 is recorded in the Report.
