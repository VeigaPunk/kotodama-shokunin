# CriticO94 attacks — NEW counterfeit classes vs tool sha256 7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff

Battery driver imported read-only for the argument shape: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecBattery94/battery94.py` sha256 9496721a1e8a401985d6be802184acb4c03f8718c97b82dd8ce909faafe1a7ea.
Fixture base rows: S776 (base disposition), S001 (forged gain). All fixtures under /fast/scratch/hyaku/kotodama-r94/CriticO94/work; no lane file touched.

SURVIVORS 7; UNNAMED 0; REFUSED-NAMED 6

| id | family | rc | outcome | named line |
|---|---|---|---|---|
| G0 | battery green control (must pass rc 0) | 0 | CONTROL-CLEAN | `ENTRY-EVIDENCE: PASS legs=9/9` |
| FW1 | gained-disposition forgery | 2 | REFUSED-NAMED-TOK:ASCII,NONASCII,VERDICT | `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries non-ASCII letters (VERDICT-NONASCII)` |
| MA1 | gained-disposition forgery | 2 | REFUSED-NAMED-TOK:ASCII,NONASCII,VERDICT | `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries non-ASCII letters (VERDICT-NONASCII)` |
| CD1 | gained-disposition forgery | 0 | SURVIVOR | `ENTRY-EVIDENCE: PASS legs=9/9` |
| LR1 | gained-disposition forgery | 0 | SURVIVOR | `ENTRY-EVIDENCE: PASS legs=9/9` |
| TAB1 | gained-disposition forgery | 0 | SURVIVOR | `ENTRY-EVIDENCE: PASS legs=9/9` |
| ID1 | gained-disposition forgery | 0 | SURVIVOR | `ENTRY-EVIDENCE: PASS legs=9/9` |
| ZWJ1 | strip-control (expected refusal) | 1 | REFUSED-NAMED:APPENDONLY | `LEG FAIL APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=S001: gained a LOCATED line not present at base` |
| CRLF1 | gained-disposition forgery | 1 | REFUSED-NAMED:APPENDONLY | `LEG FAIL APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=S001: gained a LOCATED line not present at base` |
| NUM1 | G1-family heading forgery | 0 | SURVIVOR | `ENTRY-EVIDENCE: PASS legs=9/9` |
| RM1 | G1-family heading forgery | 0 | SURVIVOR | `ENTRY-EVIDENCE: PASS legs=9/9` |
| NUM2 | G1-family heading forgery | 0 | SURVIVOR | `ENTRY-EVIDENCE: PASS legs=9/9` |
| SP1 | registry-visability forgery | 1 | REFUSED-NAMED:NEWIDS | `LEG FAIL NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=cited ids missing from registry: S958` |
| MN1 | manifest-shape forgery | 1 | REFUSED-NAMED:CAPTURE | `LEG FAIL CAPTURE expected=each gate quote occurs in its committed capture observed=S955: manifest url is not a row url: ` |

## G0 — CONTROL-CLEAN

- Family: battery green control (must pass rc 0)
- Recipe: unmodified mini-lane
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/G0 entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/G0/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/G0/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/G0/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/G0/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/G0/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/G0/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## FW1 — REFUSED-NAMED-TOK:ASCII,NONASCII,VERDICT

- Family: gained-disposition forgery
- Recipe: lesson line "S001 ＬＯＣＡＴＥＤ recheck 90d accessed 2026-11-05" - verdict token in fullwidth Latin (NFKC-folds to LOCATED)
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/FW1_fullwidth_verdict entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/FW1_fullwidth_verdict/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/FW1_fullwidth_verdict/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/FW1_fullwidth_verdict/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/FW1_fullwidth_verdict/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/FW1_fullwidth_verdict/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/FW1_fullwidth_verdict/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 2
- Tool output:
```
ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries non-ASCII letters (VERDICT-NONASCII)
```

## MA1 — REFUSED-NAMED-TOK:ASCII,NONASCII,VERDICT

- Family: gained-disposition forgery
- Recipe: lesson line "S001 𝐋𝐎𝐂𝐀𝐓𝐄𝐃 recheck 90d accessed 2026-11-05" - verdict token in mathematical bold (NFKC-folds to LOCATED)
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MA1_mathbold_verdict entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MA1_mathbold_verdict/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MA1_mathbold_verdict/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MA1_mathbold_verdict/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MA1_mathbold_verdict/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MA1_mathbold_verdict/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MA1_mathbold_verdict/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 2
- Tool output:
```
ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries non-ASCII letters (VERDICT-NONASCII)
```

## CD1 — SURVIVOR

- Family: gained-disposition forgery
- Recipe: lesson line "S001 LOCA\u0301TED ..." - combining acute U+0301 inside the verdict token (Mn, invisible to a letters-only scan)
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CD1_combining_acute_verdict entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CD1_combining_acute_verdict/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CD1_combining_acute_verdict/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CD1_combining_acute_verdict/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CD1_combining_acute_verdict/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CD1_combining_acute_verdict/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CD1_combining_acute_verdict/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## LR1 — SURVIVOR

- Family: gained-disposition forgery
- Recipe: lesson line "S001 LO\u200eCATED ..." - LTR mark U+200E splits the verdict; zero-width but Cf, NOT in the tool's zero-width strip set
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/LR1_lrm_split_verdict entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/LR1_lrm_split_verdict/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/LR1_lrm_split_verdict/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/LR1_lrm_split_verdict/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/LR1_lrm_split_verdict/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/LR1_lrm_split_verdict/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/LR1_lrm_split_verdict/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## TAB1 — SURVIVOR

- Family: gained-disposition forgery
- Recipe: lesson line "S001 LO\tCATED ..." - horizontal tab splits the verdict token
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/TAB1_tab_in_verdict entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/TAB1_tab_in_verdict/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/TAB1_tab_in_verdict/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/TAB1_tab_in_verdict/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/TAB1_tab_in_verdict/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/TAB1_tab_in_verdict/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/TAB1_tab_in_verdict/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## ID1 — SURVIVOR

- Family: gained-disposition forgery
- Recipe: lesson line "\ua731001 LOCATED ..." - small-capital S (U+A731, category Ll) in the id token; verdict token is clean ASCII
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ID1_smallcap_id entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ID1_smallcap_id/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ID1_smallcap_id/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ID1_smallcap_id/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ID1_smallcap_id/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ID1_smallcap_id/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ID1_smallcap_id/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## ZWJ1 — REFUSED-NAMED:APPENDONLY

- Family: strip-control (expected refusal)
- Recipe: lesson line "S001 LO\u200dCATED ..." - ZWJ U+200D is in the strip set, so the tool must SEE the gain and refuse on APPENDONLY
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ZWJ1_zwj_split_verdict entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ZWJ1_zwj_split_verdict/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ZWJ1_zwj_split_verdict/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ZWJ1_zwj_split_verdict/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ZWJ1_zwj_split_verdict/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ZWJ1_zwj_split_verdict/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/ZWJ1_zwj_split_verdict/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 1
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG FAIL APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=S001: gained a LOCATED line not present at base
ENTRY-EVIDENCE: FAIL legs=8/9 failed=APPENDONLY
```

## CRLF1 — REFUSED-NAMED:APPENDONLY

- Family: gained-disposition forgery
- Recipe: whole lesson with CRLF endings; gained line "S001 LOCATED recheck 90d accessed 2026-11-05"
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CRLF1_crlf_lesson entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CRLF1_crlf_lesson/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CRLF1_crlf_lesson/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CRLF1_crlf_lesson/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CRLF1_crlf_lesson/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CRLF1_crlf_lesson/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/CRLF1_crlf_lesson/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 1
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG FAIL APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=S001: gained a LOCATED line not present at base
ENTRY-EVIDENCE: FAIL legs=8/9 failed=APPENDONLY
```

## NUM1 — SURVIVOR

- Family: G1-family heading forgery
- Recipe: all five h2 re-headed to nested-numbered phrase-only ("## 1.1 address" ...); stripping ^\d+[.)] leaves ".1" so the token floor still passes
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM1_nested_number_heads entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM1_nested_number_heads/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM1_nested_number_heads/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM1_nested_number_heads/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM1_nested_number_heads/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM1_nested_number_heads/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM1_nested_number_heads/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## RM1 — SURVIVOR

- Family: G1-family heading forgery
- Recipe: all five h2 re-headed to roman-numbered phrase-only ("## I. address" ...); ^\d+[.)] never matches roman numerals
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/RM1_roman_number_heads entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/RM1_roman_number_heads/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/RM1_roman_number_heads/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/RM1_roman_number_heads/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/RM1_roman_number_heads/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/RM1_roman_number_heads/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/RM1_roman_number_heads/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## NUM2 — SURVIVOR

- Family: G1-family heading forgery
- Recipe: second-token numbered headings with bare anchors ("## Notes 1) address" ... "## Notes 4) table"); the leading-number strip sees "Notes" first, so the anchor span passes
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM2_numbered_second_token entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM2_numbered_second_token/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM2_numbered_second_token/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM2_numbered_second_token/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM2_numbered_second_token/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM2_numbered_second_token/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/NUM2_numbered_second_token/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 0
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: PASS legs=9/9
```

## SP1 — REFUSED-NAMED:NEWIDS

- Family: registry-visability forgery
- Recipe: eleven-cell lands row for S958 indented four spaces at line start and inside the id cell; entry cites S958 with gate line, capture and manifest row
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/SP1_indented_row entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/SP1_indented_row/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/SP1_indented_row/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/SP1_indented_row/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/SP1_indented_row/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/SP1_indented_row/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/SP1_indented_row/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 1
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG FAIL NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=cited ids missing from registry: S958
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: FAIL legs=8/9 failed=NEWIDS
```

## MN1 — REFUSED-NAMED:CAPTURE

- Family: manifest-shape forgery
- Recipe: manifest row value for S955 is a dict MISSING the url key (capture/quote/sha intact)
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MN1_manifest_dict_no_url entry --entry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MN1_manifest_dict_no_url/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MN1_manifest_dict_no_url/base.md --lands-registry /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MN1_manifest_dict_no_url/lands.md --lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MN1_manifest_dict_no_url/lesson.md --manifest /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MN1_manifest_dict_no_url/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r94/CriticO94/work/MN1_manifest_dict_no_url/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- rc: 1
- Tool output:
```
LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean
LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean
LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean
LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean
LEG FAIL CAPTURE expected=each gate quote occurs in its committed capture observed=S955: manifest url is not a row url: 
LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean
ENTRY-EVIDENCE: FAIL legs=8/9 failed=CAPTURE
```

