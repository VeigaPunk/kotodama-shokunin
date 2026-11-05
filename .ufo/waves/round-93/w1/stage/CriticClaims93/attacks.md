# CriticClaims93 — claim O refusal-predicate attacks (frozen v4 entry mode)

Tool: tools/check-advance-evidence.py sha256 9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7 (verified before the run). Grading arguments copied from reports/round-93/battery93.py grade(); fixture constants from the frozen round-92 builder reports/round-92/controls/make-counterfeits.py (imported read-only). All fixtures built under /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work; no lane file touched. Run date: 2026-11-05.

## Harness controls

### G0 control (harness)

- Recipe: battery93 G0 fixture, unmodified
- rc: 0
- Outcome: harness ok

### A5d harness check (bold disposition)

- Recipe: battery93 A5d shape: **S001 LOCATED** lesson extra
- rc: 1
- Outcome: refused on named leg APPENDONLY (rc=1)

## Counterfeits

### A1 — cyrillic-lookalike LOCATED in a lesson disposition line

- Named leg (what the class games / should be pinned to): APPENDONLY
- rc: 0
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/A1_cyr_located entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/A1_cyr_located/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/A1_cyr_located/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/A1_cyr_located/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/A1_cyr_located/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/A1_cyr_located/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/A1_cyr_located/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean`
  - `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean`
  - `LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean`
  - `ENTRY-EVIDENCE: PASS legs=9/9`
- Outcome: **SURVIVED (rc 0)**

### B1 — soft-hyphen LOCATED in a lesson disposition line

- Named leg (what the class games / should be pinned to): APPENDONLY
- rc: 0
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/B1_shy_located entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/B1_shy_located/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/B1_shy_located/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/B1_shy_located/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/B1_shy_located/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/B1_shy_located/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/B1_shy_located/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean`
  - `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean`
  - `LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean`
  - `ENTRY-EVIDENCE: PASS legs=9/9`
- Outcome: **SURVIVED (rc 0)**

### C1 — disposition line hidden in a fenced code block

- Named leg (what the class games / should be pinned to): APPENDONLY
- rc: 1
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/C1_fenced_dispo entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/C1_fenced_dispo/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/C1_fenced_dispo/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/C1_fenced_dispo/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/C1_fenced_dispo/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/C1_fenced_dispo/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/C1_fenced_dispo/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean`
  - `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean`
  - `LEG FAIL APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=S001: gained a LOCATED line not present at base`
  - `ENTRY-EVIDENCE: FAIL legs=8/9 failed=APPENDONLY`
- Outcome: **refused on named leg APPENDONLY (rc=1)**

### D1 — manifest http_status as string "200"

- Named leg (what the class games / should be pinned to): CAPTURE
- rc: 1
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/D1_http_status_string entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/D1_http_status_string/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/D1_http_status_string/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/D1_http_status_string/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/D1_http_status_string/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/D1_http_status_string/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/D1_http_status_string/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean`
  - `LEG FAIL CAPTURE expected=each gate quote occurs in its committed capture observed=S955: capture http_status not 2xx: reports/round-90/evidence/S955.txt`
  - `LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean`
  - `ENTRY-EVIDENCE: FAIL legs=8/9 failed=CAPTURE`
- Outcome: **refused on named leg CAPTURE (rc=1)**

### E1 — gate quote equal to teaches only after NFKC (ﬁ ligature)

- Named leg (what the class games / should be pinned to): GATE
- rc: 1
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/E1_nfkc_selfquote entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/E1_nfkc_selfquote/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/E1_nfkc_selfquote/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/E1_nfkc_selfquote/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/E1_nfkc_selfquote/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/E1_nfkc_selfquote/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/E1_nfkc_selfquote/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG FAIL GATE expected=each new id has a located gate line bound to the row teaching observed=S955: gate quote is the row teaching cell (self-quote)`
  - `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean`
  - `LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean`
  - `ENTRY-EVIDENCE: FAIL legs=8/9 failed=GATE`
- Outcome: **refused on named leg GATE (rc=1)**

### F1 — numbered-but-empty h2 headings gaming ENTRY

- Named leg (what the class games / should be pinned to): ENTRY
- rc: 1
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/F1_empty_numbered_heads entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/F1_empty_numbered_heads/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/F1_empty_numbered_heads/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/F1_empty_numbered_heads/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/F1_empty_numbered_heads/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/F1_empty_numbered_heads/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/F1_empty_numbered_heads/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG FAIL TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=2 of 4 sub-topic phrases in headings/table cells < 4; phrase anchors span 1 heading/table surfaces < 3; phrase anchors 2/4 spanning 1 heading/table surfaces`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean`
  - `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean`
  - `LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean`
  - `ENTRY-EVIDENCE: FAIL legs=8/9 failed=TOPIC`
- Outcome: **refused NOT on named leg: expected ENTRY, got TOPIC (rc=1)**

### G1 — numbered phrase-only h2 headings gaming the anchor-span guard

- Named leg (what the class games / should be pinned to): TOPIC
- rc: 0
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/G1_numbered_phrase_heads entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/G1_numbered_phrase_heads/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/G1_numbered_phrase_heads/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/G1_numbered_phrase_heads/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/G1_numbered_phrase_heads/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/G1_numbered_phrase_heads/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/G1_numbered_phrase_heads/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean`
  - `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean`
  - `LEG PASS APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=clean`
  - `ENTRY-EVIDENCE: PASS legs=9/9`
- Outcome: **SURVIVED (rc 0)**

### H1 — manifest row value is a JSON list

- Named leg (what the class games / should be pinned to): CAPTURE
- rc: 1
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/H1_manifest_row_list entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/H1_manifest_row_list/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/H1_manifest_row_list/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/H1_manifest_row_list/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/H1_manifest_row_list/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/H1_manifest_row_list/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/H1_manifest_row_list/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `Traceback (most recent call last):`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 1609, in <module>`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 1602, in main`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 787, in cli`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 710, in grade_entry`
  - `AttributeError: 'list' object has no attribute 'get'`
- Outcome: **REFUSED WITH TRACEBACK (unnamed crash, rc=1)**

### I1 — truncated lands registry row (4 cells)

- Named leg (what the class games / should be pinned to): NEWIDS
- rc: 1
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/I1_truncated_row entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/I1_truncated_row/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/I1_truncated_row/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/I1_truncated_row/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/I1_truncated_row/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/I1_truncated_row/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/I1_truncated_row/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `Traceback (most recent call last):`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 1609, in <module>`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 1602, in main`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 787, in cli`
  - `  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py", line 615, in grade_entry`
  - `IndexError: list index out of range`
- Outcome: **REFUSED WITH TRACEBACK (unnamed crash, rc=1)**

### J1 — en-dash NOT–LOCATED flips the read verdict

- Named leg (what the class games / should be pinned to): APPENDONLY
- rc: 1
- Command: `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py --root /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/J1_endash_notlocated entry --entry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/J1_endash_notlocated/corpus/knowledge/myth-symbol/prayer-register.md --base-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/J1_endash_notlocated/base.md --lands-registry /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/J1_endash_notlocated/lands.md --lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/J1_endash_notlocated/lesson.md --manifest /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/J1_endash_notlocated/manifest.json --capture-dir reports/round-90/evidence --as-of 2026-11-05 --topic 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims' --topic-phrases 'address;petition;efficacy;table' --min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 --table-min-rows 5 --table-min-cols 3 --base-lesson /fast/scratch/hyaku/kotodama-r93/CriticClaims93/work/J1_endash_notlocated/base-lesson.md --graded corpus/SOURCES.md --graded lesson.md --min-anchor-span 3 --min-gate-overlap 3`
- Verdict lines:
  - `LEG PASS ENTRY expected=>=1200B, >=4 h2, header keys observed=clean`
  - `LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean`
  - `LEG PASS TOPIC expected=>=8 shared content words with the declared topic; >=4 phrase anchors in headings/table observed=clean`
  - `LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-05 and cited observed=clean`
  - `LEG PASS UNIQUENESS expected=no duplicate lands id, no base-url shadow, no shared new url observed=clean`
  - `LEG PASS BASEROWS expected=no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged observed=clean`
  - `LEG PASS GATE expected=each new id has a located gate line bound to the row teaching observed=clean`
  - `LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean`
  - `LEG FAIL APPENDONLY expected=no old id gains or flips a disposition in the round lesson observed=S001: disposition NOT-LOCATED -> LOCATED`
  - `ENTRY-EVIDENCE: FAIL legs=8/9 failed=APPENDONLY`
- Outcome: **refused on named leg APPENDONLY (rc=1)**

