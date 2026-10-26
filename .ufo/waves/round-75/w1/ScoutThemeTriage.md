# Round 75 staged knowledge-family triage

Scope: 40 files under `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/**`. The IDs below are staged-namespace source IDs appearing on each file's `source:` lines (not incidental IDs mentioned in prose). Lane presence was checked at base `f556d1049fe651d3d63975600b13acd9fb686f15`.

## Counts and lane-presence check

| Disposition | Count |
|---|---:|
| ADOPT-THIS-ROUND | 2 |
| ALREADY-ADOPTED | 2 |
| PATH-PRESENT-DIFFERING | 4 |
| REFUSED-WITH-REASON | 32 |
| **Total** | **40** |

The six existing family paths named by the assignment are present at base: worldbuilding-setting x2, heritage x2, and conlang-scholarship x2. The round-74 lesson explicitly separates the four heritage/conlang files below as path-present with differing staged bytes. The two worldbuilding files are categorized ALREADY-ADOPTED (round 74 adoption); the staged copies also differ by SHA-256 from the lane copies at this base, consistent with their intervening landing/edit. Heritage was adopted round 72; conlang-scholarship was adopted round 73; worldbuilding-setting was adopted round 74.

## Per-file disposition

### ADOPT-THIS-ROUND — narrative-structure entries in draft claim C (2)

| Staged path | Staged source IDs | Disposition / basis |
|---|---|---|
| `myth-symbol/narrative-structure-frameworks.md` | S864, S865, S866, S870, S876 | ADOPT-THIS-ROUND — draft claim C entry. S870's earlier refusal remains conditional: only append it if a quote locates on the page this round. |
| `myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` | S885, S902, S904 | ADOPT-THIS-ROUND — draft claim C entry. |

### ALREADY-ADOPTED — worldbuilding-setting (2)

| Staged path | Staged source IDs | Disposition / basis |
|---|---|---|
| `culture-material/worldbuilding-setting-practice.md` | S882, S883, S884 | ALREADY-ADOPTED — both path and content family are in the lane at base; landed round 74. |
| `culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` | S895, S899, S900 | ALREADY-ADOPTED — path is in the lane at base; landed round 74. Round-74 Gate separately refused staged S895's superseded passage. |

### PATH-PRESENT-DIFFERING — the four round-74 files (4)

| Staged path | Staged source IDs | Disposition / basis |
|---|---|---|
| `culture-material/heritage-taxonomy-models.md` | S863, S867 | PATH-PRESENT-DIFFERING — lane path present; round-74 lesson names it among the four byte-differing staged files. |
| `culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` | S967 | PATH-PRESENT-DIFFERING — lane path present; round-74 lesson names it among the four byte-differing staged files. |
| `linguistics/conlang-scholarship.md` | S881, S882 | PATH-PRESENT-DIFFERING — lane path present; round-74 lesson names it among the four byte-differing staged files. |
| `linguistics/conlang-scholarship.amend-2026-10-23.md` | S892, S893, S894, S901 | PATH-PRESENT-DIFFERING — lane path present; round-74 lesson names it among the four byte-differing staged files. |

### REFUSED-WITH-REASON (32)

Reason classes and flips below are from the round-74 family table unless a more specific round-73 Gate refusal is also noted. Round 74's triage table refused these families; round-75 draft claim C selects only the two narrative entries above. The three remaining narrative amendments stay refused unless the claim's quote-location condition is met.

| Staged path | Staged source IDs | Refusal / reason class / flip |
|---|---|---|
| `culture-material/calendar-festival-systems.amend-2026-10-23c.md` | S916 | Refused round 74 — parent entry/sources not lane rows; dates asserted from memory, no located span. Flip: register parent and calendar sources, then re-quote. |
| `culture-material/calendar-festival-systems.amend-2026-10-24.md` | S919, S921, S932, S935, S937 | Refused round 74 — same calendar reason class. Flip: register parent and calendar sources, then re-quote. |
| `culture-material/calendar-festival-systems.amend-2026-10-24-r10.md` | S938 | Refused round 74 — same calendar reason class. Flip: register parent and calendar sources, then re-quote. |
| `culture-material/era-periodization-models.amend-2026-10-23.md` | S887, S898 | Refused round 74 — no parent lane row and no located span. Flip: register parent and sources first. |
| `culture-material/era-periodization-models.amend-2026-10-23b.md` | S908 | Refused round 74 — same era reason class. Flip: register parent and sources first. |
| `linguistics/conlang-methodology.amend-2026-10-24.md` | S920, S922, S923 | Refused round 74 — parent entry exists, but quotes were not re-opened and staged bytes differ. Round-73 specific defect: reachable/outside declared set; S920 locator should be §1.3, printed p. 310, not §2.1.2, p. 312. Flip: reopen quotes against parent rows, correct anchor, land as an appended amendment in its own round. |
| `linguistics/conlang-scholarship.amend-2026-10-23b.md` | S909, S910 | Refused round 74 — quotes not re-opened and staged bytes differ. Round-73 specific reason: reachable, but outside declared set. Flip: reopen quotes against parent rows and land as an appended amendment in its own round. |
| `linguistics/conlang-scholarship.amend-2026-10-23c.md` | S915 | Refused round 74 — quotes not re-opened and staged bytes differ. Round-73 specific reason: defective Crossref query (`Languistics` typo; container-title is a relevance query, not a filter). Flip: restage with corrected query and cited document, then reopen the quote. |
| `linguistics/conlang-scholarship.amend-2026-10-24.md` | S929, S930 | Refused round 74 — quotes not re-opened and staged bytes differ. Round-73 specific reason: reachable/outside declared set; S929's locator is printed p. 390, not p. 387. Flip: use the corrected location and real handbook citation, then reopen quotes and append in its own round. |
| `myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` | S905 | Refused round 74 — narrative family lacked a lane row and quotes were not re-located; staged S870 had previously been refused round 72 for a quote not located on its page (fabrication-class refusal). Flip: register the source with a captured, exactly-once quote and lane-frontier ground; for this amendment, meet claim C's quote-location condition before adoption. |
| `myth-symbol/narrative-structure-frameworks.amend-2026-10-23c.md` | S917 | Refused round 74 — same narrative reason class. Flip: register source with captured exactly-once quote and lane-frontier ground; satisfy claim C's quote-location condition. |
| `myth-symbol/narrative-structure-frameworks.amend-2026-10-24.md` | S919, S921 | Refused round 74 — same narrative reason class. Flip: register source with captured exactly-once quote and lane-frontier ground; satisfy claim C's quote-location condition. |
| `linguistics/naming-systems.md` | S868, S871, S874, S875 | Refused round 74 — no lane row holds the document; amendment chain repeats a topic without a located quote per claim. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-23.md` | S886, S888, S889, S890, S891, S896, S897, S903 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-23b.md` | S906, S907, S911 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-23c.md` | S912, S913, S914, S918 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24.md` | S924, S925, S926, S927, S931, S933, S934, S936 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24-r10.md` | S939, S940, S941, S943, S944 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24-r11.md` | S947, S948, S949, S950, S951, S952, S953, S954 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24-r12.md` | S957, S958, S959, S960 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24-r13.md` | S963, S964, S965, S966 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24-r14.md` | S969, S972, S973, S974 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24-r15.md` | S978 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `linguistics/naming-systems.amend-2026-10-24-r16.md` | S988 | Refused round 74 — same naming family reason class. Flip: one row per document with a round-specific capture and located quote. |
| `verification/citation-format-and-source-registry.amend-2026-10-24-r10.md` | S945, S946 | Refused round 74 — lane-internal process text, not source-backed domain knowledge; no registry row supports it. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/citation-format-and-source-registry.amend-2026-10-24-r11.md` | S955, S956 | Refused round 74 — same verification reason class. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/citation-format-and-source-registry.amend-2026-10-24-r12.md` | S961, S962 | Refused round 74 — same verification reason class. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/citation-format-and-source-registry.amend-2026-10-24-r13.md` | S968 | Refused round 74 — same verification reason class. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/citation-format-and-source-registry.amend-2026-10-24-r14.md` | S970, S971, S975 | Refused round 74 — same verification reason class. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/citation-format-and-source-registry.amend-2026-10-24-r15.md` | S976, S977, S979, S980, S981 | Refused round 74 — same verification reason class. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/citation-format-and-source-registry.amend-2026-10-24-r16.md` | S982, S983, S984, S985, S986, S987, S989 | Refused round 74 — same verification reason class. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/journal-serial-catalogue-records.amend-2026-10-24-r16.md` | S990 | Refused round 74 — lane-internal process text, not source-backed domain knowledge; no registry row supports it. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |
| `verification/reopen-gate.amend-2026-10-24.md` | S928 | Refused round 74 — same verification reason class. Flip: own-work `source:` path with lane-relative locator, or leave as lesson. |

## Evidence and limits

- Round-74 lesson `corpus/lessons/round-74.md` says its triage was 2 adopted / 4 path-present with differing staged bytes / 34 refused, and names the four differing files above.
- Base-tree `git ls-tree` confirms all six worldbuilding/heritage/conlang paths are present. The round-72, round-73, and round-74 landing commits confirm the three adoption rounds.
- Draft claim C names the base narrative entry and the `2026-10-23` amendment as its two entries; it leaves the other three narrative amendments contingent on located quotes. This report therefore does not count those three as adopted.
- No tools were installed.
