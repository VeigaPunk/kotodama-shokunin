# ScoutRejectProbes — attack on the round-74 reject rows, family table and Quarantine

Seat: ScoutRejectProbes-2 (scout, leaf, wave 2). Lane main at dispatch: `1d7add3f7b9eaf6f3349c56c36f6d06325d74236`; operative freeze `00c408a0…`; claim C lands `c4bf61a8…`.
Attacked file: `corpus/lessons/round-74.md` (`## Gate` rejects, family table, `## Quarantine`).
Nothing in the lane or fleet was written; scratch in `/tmp/ScoutRejectProbes/` (fetch bodies, `rc.py`), plus a throwaway `--shared` clone under `~/.cache` (deleted). `/tmp` is 98 % full (`df -h /tmp`: 3.1G free), the first `git clone` into `mktemp -d` died with "No space left on device"; I redid it on `/` with `git clone --shared` (no tool installed).

## Fetch log (QUALITY 21/22/24)

Browser UA = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; curl UA = default `curl/8.x`. Fetched 2026-10-26 02:00 UTC (the lesson's access date is 2026-10-25). `curl -sSL -m 60`:

| URL | browser UA | curl UA | sha256 (both UAs equal) |
|---|---|---|---|
| http://www.philol.msu.ru/~sidorova/files/conlangs.pdf | 200, 1055723 B | 200, 1055723 B | e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9 (= S877 capture) |
| https://www.chinawriter.com.cn/n1/2025/1030/c404027-40592897.html (S895) | 200, 45262 B | 200, 45262 B | 95b688fc20fa1b2996c59f1bd365af714c04c26322efc45dbdb8087c09b58ceb |
| https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | 200, 48536 B | 200, 48536 B | a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d (= S883 capture) |
| https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | 200, 62604 B | 200, 62604 B | 344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659 (= S884 capture) |

No wall, no retry needed, no "no capture" ruling made (so no CDX probe owed). All four pages are byte-identical to the lesson's captures, so the probes are live and the pages did not drift.

## Verdict table (what survived, what did not)

| attacked item | result |
|---|---|
| S882 reject (same document as S877) | **SURVIVES** (F9 note: staged label wrong, reason stronger) |
| S895 reject reason text | **FAILS** (F1) |
| S899 / S900 reject reasons + "re-quote" | **FAILS** as worded for the staged package (F2) |
| counts 2 / 4 / 34 of 40 | **SURVIVES** (recount below) |
| 4 path-present sha256 pairs "differ" | **SURVIVES** but no hash is printed in the lesson (F8) |
| family table reasons | verification row **FAILS** (F3); calendar/naming "from memory / no located quote" **unprobed and contradicted** (F5); conlang row partly false (F6); 4 `amendments/` files never triaged (F4) |
| Quarantine S816/S817 | **SURVIVES** on the pages; mispairing attribution is right only if read as the register's, which the Gate reject rows contradict (F2) |
| REJECTS leg of `accept-c.py` | presence-only, certifies false reasons (F7) |

## Recount, 40 staged files by family

`find …/merge/kotodama/knowledge …/merge/kotodama/amendments -name '*.md' | wc -l` per dir → `knowledge` 40, `amendments` 4 (so 44 staged `.md` files; MERGE-REPORT says "proposed knowledge entries: 56" including folded passages).

`knowledge/` (40): worldbuilding-setting-practice 2 (adopted); path-present 4 = heritage-taxonomy-models (base + r13 amend) 2, conlang-scholarship (base + amend-2026-10-23) 2; refused 34 = narrative-structure-frameworks 5 (base + 4 amends), naming-systems 11 (**11 `.amend-*` files, no base file in `knowledge/`**), calendar-festival-systems 3, era-periodization-models 2, verification 9 (citation-format r10..r16 = 7, journal-serial r16 = 1, reopen-gate = 1), conlang 3 (scholarship 23b/23c/2026-10-24) + 1 (methodology amend) = 34. 2 + 4 + 34 = 40. **Counts reproduce.**

Path-present sha256 pairs (staged vs lane; lane bytes identical at base `f7104cb`, freeze `00c408a` and main — `git show <rev>:corpus/knowledge/<f> | sha256sum`):

| file | staged sha256 (B) | lane sha256 (B) |
|---|---|---|
| culture-material/heritage-taxonomy-models.md | b17223b9a04b0b16b020b4ed58f03898dc7e8c97cff03739cf62b0077b08f99b (3339) | 09175b1849fb1b6d80f3d6a313aa21dc318e9d3227ea789163a48054be61562c (8748) |
| culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md | 9ed5ceefe5b1e70f59d2c57d3d9f6223d24f09d872ee362b0188eebbc190206b (3192) | 8544fe1ec5315e7d2d3f77d848ba7fdc35f41c7751280a90d12cba850bc406c7 (3367) |
| linguistics/conlang-scholarship.md | ce666a2bf15d97531545acafb88b559f239819ab11aad1883dd2f9d2d6854891 (2631) | fe7e214adb04d149cab965da0c04c20c1c42a150d084047f0fd949210b8a55b2 (13960) |
| linguistics/conlang-scholarship.amend-2026-10-23.md | 8f889666b32c81a9ea4eb8905e79c6e3c992e70e6f0e49debd22cda86b86a8d6 (5635) | 01029a642c9f2c8af1db3c1540f0a30a6bac94786c102c3459758866e558d3a2 (12940) |

All four differ — **claim survives.** Only these 4 (+ the 2 adopted worldbuilding files, which the round itself wrote) are path-present in `knowledge/`; no other staged `knowledge/` file exists in the lane.

## FINDINGS

### F1 — HIGH — S895 reject reason is false for the staged row set; the drop is an unauthorised trim, and the page supports the passage
Lesson `## Gate` reject row: "staged S895's folded passage … is dropped: the amend file's superseded section cites a row that is not in the row set"; id-map prose: "`S754`/`S895` are not in the row set". Observed:
```
$ grep -n -E '^ {0,3}\|[[:space:]]*S895' /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md
43:| S895 | 王昕玥《论〈龙族〉的叙事失控与世界观危机》, 中国作家网《网络文学》专栏, 2025-10-30 — https://www.chinawriter.com.cn/n1/2025/1030/c404027-40592897.html | paper | B | …
$ grep -n S895 .ufo/waves/round-74/assimilation/staged-ids   → 37:S895      (the round's own staged id list)
$ grep -c -E '^ {0,3}\|[[:space:]]*S895' corpus/SOURCES.md  → 0   (lane)
```
So S895 IS in the staged 132-row set; it is absent from the **lane** registry only. "Row set" in the claim is the claim's own `row_set = S881..S884` (ROWS leg "exactly S881..S884"), i.e. the reason is circular: the claim's constants forbid a fifth row, then cite that as the reason. The page is live and carries the passage once: after whitespace/tag stripping `拟真`, `完整周密`, `叙事驱动机制`, `价值共识框架`, `类型标识系统`, `S-A-B-C`, `量化` = 1 hit each (page 11381 chars, 200, sha256 above). `MERGE-REPORT.md:17`: "The operator may trim the folded passage if the later entry supersedes it outright" — the passage is a *different document* from the build-order/delivery amend (staged amend `source:` lines 4–6, S895 failure-analysis vs S899/S900 order/schedule), so it is not superseded, and no operator approval is recorded anywhere in the lesson. W1 flagged this as RevAssimilationContract F7; the landed reject row still states the false reason. The `probed URL` for this row is not backed by any committed capture (`reports/round-74/evidence/` holds S877/S881–S884 only); the 200/45262/`95b688fc…` probe exists only in W1 scratch (`RevEntryQuality.md:251`).
Fix: reword to "no lane row for S895; the claim's closed row set S881..S884 cannot carry a fifth row; the drop is a trim the package reserves to the operator" and record the operator ruling or adopt S895 as S885 with a captured quote; commit a status/UA/sha capture for the probed URL. Flip is fine as written.

### F2 — HIGH — S899/S900 reject reasons ("staged span absent from its page") are false for the staged package; only the register/census pairing was off by one, and the lesson contradicts itself
Reject rows: "staged S899's quoted span was absent from the page it was bound to"; "staged S900's quoted span was the Sowers-Wills clause, absent from this page"; Gate admit cells S883/S884: "re-quote: the staged span was absent from its own page". Staged rows themselves (`SOURCES.append.md:47,48`, round-4 `SOURCES-PROPOSED.md:37-50` Gate blocks) are correctly paired:
```
S899 anchor 「非凡特性来自最初造物主」: on 2025/0605 page = 1 ; on 2022/1207 page = 0
S899 round-4 Gate quote 「整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。」: on 2025 page = 1
S900 anchor 「这个我肯定考虑过。我自己就是资深读者…」: on 2022/1207 page = 1
S900 round-4 Gate quote …把它放在前面大概20章之内慢慢来: on 2022 page = 1
staged recheck cells: S899 grep -c '先做的是世界观' -> 1 ; S900 grep -c '20章之内慢慢来' -> 1  (both reproduce live: 1 / 1)
```
The Sowers-Wills clause is the anchor of staged **S901** (`SOURCES.append.md:49`, "the paragraph on 'Sowers-Wills's 'Phonology from the inside out…''"), i.e. the *next* row: `census-adjudication.json` (shokuknow `.ufo/waves/corpus-expansion-1/`) entries S758/S759 carry `url` of row N with `quote` of row N+1 (the entry's own `line` field prints the next row, `S759 | …`, `S760 | …`). The lesson says this itself in R74-M5 ("not the pages and not the staged row text"), which contradicts the reject rows. Consequences: (a) the S883 "re-quote" is not a re-quote — its Gate quote is character-identical to the round-4 staged Gate quote; S884's final-sentence quote is a substring of the round-4 staged Gate quote (both located exactly once); (b) round 72's "REFUSED set → staged S899, S900 not adoptable" was a wrong refusal of correctly-paired rows, and round 74 re-propagates it; (c) the flip "a fresh quote located on the 2025 page" is satisfiable by the staged quote.
Fix: replace the two reject reasons with "register/census URL↔quote off-by-one (S758/S759); staged row text is correct and located once; adopted as S883/S884 with the staged Gate quote at the round-74 capture", and delete "re-quote … staged span absent" from the S883/S884 Gate cells (claim C's GATE leg wording "staged quotes absent" is itself false and cannot be amended after scoring — record it as a claim-text defect).

### F3 — MEDIUM — "verification amendments (9) … no registry row can support them" is false for 5 of 9
Lesson row: "lane-internal process texts, not source-backed domain knowledge; no registry row can support them"; clearing condition: "an own-work `source:` path". Only 4 are own-work (r10, r11, r12 citation-format, S945/S946/S955/S956/S961/S962 absolute shokuknow paths; reopen-gate S928). The other **5** (citation-format r13, r14, r15, r16, journal-serial r16) cite staged rows with external URLs:
```
S968 cir.nii.ac.jp/crid/1010000782292879748.json (CiNii)   S970 …/1010000781908173825.json   S971 play.google.com/store/books/details?id=xz9BEQAAQBAJ
S975 zgsdmzyjjk.zazhi.com.cn   S976/977/982-985 book.douban.com/subject/…   S979 mr.imnu.edu.cn/info/1012/1584.htm   S980 …yuezazhi.com   S981 newcnki.net/info/6820.html
S986 book.douban.com/j/subject_suggest   S987 m.mzzyk.com   S989 sdms.zjdata.net   S990 sru.k10plus.de/gvk?…marcxml
```
(staged `recheck` counts 1–6, `->` values; none 0.) Subject is the catalogue records of one Chinese serial — domain knowledge, source-backed. The own-work clearing condition would not clear them. Also `journal-serial-catalogue-records.md` and `reopen-gate.md` have no parent in the lane (`ls corpus/knowledge/verification` → only `citation-format-and-source-registry.md`), a different blocking reason the lesson never states. Fix: split the row: 4 own-work (cond. as written) + 5 external-source amendments (cond.: register S968..S990 rows with captured quotes; parent for journal-serial is missing → new-file entry).

### F4 — HIGH — four staged files under `amendments/` are never triaged ("40 of 40" is really 40 of 44)
`MERGE-REPORT.md:109` Adopt checklist item 5: "For every file under `amendments/`, append its content to the lane's existing … Do not replace the file". Present in staged and lane (sha256 prefixes differ): calendar-festival-systems.md (staged 5572 B / lane 30406 B), era-periodization-models.md (4312 / 32709), conlang-methodology.md (2426 / 19947), naming-systems.md (8069 / 27066). The lesson mentions `amendments/` zero times (`grep -n 'amendments/' corpus/lessons/round-74.md` → only prose, no file), the 2/4/34/40 triage and the claim's `total_staged_files: 40` exclude them, and the table row "naming-systems (base plus 10 amendments) | 11" miscounts the label (11 `.amend-*` files; the "base" is an `amendments/` file outside the 40). W1 filed this as RevAssimilationContract F17 (LOW); it is a silently unadopted/undisposed set with append instructions, not a labelling nit. Fix: add a row (4 files, "append-targets of existing lane paths; not adopted because the staged text cites staged rows S859+ not in the lane registry; clearing condition …") and state the 44-file universe, or say the claim's 40 is `knowledge/` only.

### F5 — MEDIUM — calendar/era/naming reasons ("dates asserted from memory of the text, not from a located span"; "no located quote per claim") are unprobed, and the staged rows' own located-span checks reproduce live
No URL of any refused family appears in a probe column. I re-ran the staged `recheck` greps for the calendar/era/conlang-methodology rows (script `/tmp/ScoutRejectProbes/rc.py`, browser UA, then curl UA):
```
S916 xingzuobaike…d165803.html 200 staged 1 now 1   S919 iris.unipa.it (web.archive) staged 1 now 1   S921 persee.fr staged 1 now 1
S935 archive.org digital.arch… staged 1 now 3(lines)  S937 news.gmw.cn staged 1 now 1   S887 kotobank 平安時代 staged 2 now 2
S898 ndl.go.jp NDC10 pdf staged 10 now 10   S908 digital.archives.go.jp staged 3 now 3   S920 cambridge (web.archive) staged 1 now 1   S923 crossref staged 1 now 1
S932 openstd.samr.gov.cn (web.archive) staged 1 : 0 via my --compressed parse, but `curl -fsSL -A <browser> <url> -o f; grep -c '主管部门'` on the uncompressed live URL = 1 (the archive body is gzip without Content-Encoding, so a bare `curl|grep` reads garbage)
S922 crossref journals?query=constructed+language staged 1 now 1 (`grep -c '"total-results":0'`)
```
The refusal may be correct for other reasons (no lane parent rows: `grep -c 'calendar-festival-systems.md' corpus/SOURCES.md` → 0, era → 0, naming → 1, conlang-methodology → 3), but the stated *reason* "from memory, not from a located span" is an unevidenced characterisation that the staged rows' reproducible recheck counts argue against (naming rows S951/S952 are the only staged `-> 0`; S938 has no recheck). Fix: state the actual blocking condition (no lane registry row, quotes not captured under round-74 grammar) and drop "from memory"; or probe and show a failing span. Also the "parent entry … not lane rows" wording conflates *entry file* with *registry row*: the calendar and era parent **entries exist in the lane** (`corpus/knowledge/culture-material/calendar-festival-systems.md` 30406 B, era 32709 B) with book citations and 0 registry used-by rows.

### F6 — LOW/MEDIUM — conlang row: "the staged bytes differ from the lane's" is meaningless for those 4 files, and the clearing condition is incoherent
`conlang-scholarship.amend-2026-10-23b/-23c/-2026-10-24` and `conlang-methodology.amend-2026-10-24` have **no lane counterpart at those paths** (`[ -e corpus/knowledge/linguistics/<f> ]` false; only `knowledge/…conlang-scholarship.md` + `.amend-2026-10-23.md` are path-present), so "bytes differ" is not a measured fact for them. Clearing condition "re-open each amend's quotes against the parent entry's rows": the amends cite staged rows S909, S910, S915, S929, S930, S920, S922, S923 (all URLs absent from the lane registry), not the parent's rows, so the condition cannot be executed as written.

### F7 — MEDIUM — the REJECTS leg certifies false reasons (unfalsifiable claim)
Clone at lands `c4bf61a8` : `ACCEPT-C-74: PASS legs=13/13` (reproduced). Mutation in the clone (commit, `--lands <mutant>`): S895 reason → "is dropped: the moon was blue that day"; S899 reason → "staged S899's quoted span was perfectly fine (mispair)":
```
LEG PASS GATE … LEG PASS REJECTS … LEG PASS FROZENCFG … ACCEPT-C-74: PASS legs=13/13
```
`leg_rejects` (`accept-c.py:1279-1355`) greps for named ids plus `refus|fold|dropped|rejected`, `REQUOTE_RE|MISPAIR_RE`, the counts triple and the words "reason"/"flip"; it never checks a reason's truth, a probed URL's status, or a family's file count. So "each reject carries probed URL, reason and flip" is satisfied by form. Fix (next round, legs are frozen now): a REJECTS limb that re-derives each cited reason fact (id-in-staged-set, URL status/hash vs capture).

### F8 — LOW — "staged vs lane sha256 differ in all four; measured this round" prints no hash
Unfalsifiable as written; table above supplies the 8 hashes. The lesson states the 4 lane files "were left untouched" — true (`git show f7104cb`/`00c408a`/main blobs identical). Add hashes to the lesson.

### F9 — LOW — S882 reject: survives; extra facts
URL identity with S877 holds (lane row S877 and staged S882 carry the same `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf`; `git show f7104cb:corpus/SOURCES.md | grep -n philol.msu.ru` → 832). The staged row calls it a "series announcement booklet"; the PDF has 185 pages (`pdfinfo`), 186 form-feed blocks, i.e. the complete monograph (RevEntryQuality already found this) — so the "same document" reason is *stronger* than stated and the staged S882 `teaches`/scope text is wrong; the lesson should say so. S877's admitted quote re-verified: `Язык – главный инструмент построения вымышленных миров` occurs once (`pdftotext`, whitespace-folded; PDF page 7; source text has hyphenation `соз- дать` later in the sentence).

### F10 — LOW — Quarantine: wrong S792 reason still sits in the "record"
Lesson: "S792's stated reason was wrong (the four headings are present; only the reason was) … the committed table is the record". `reports/round-71/telemetry/quarantine-verdicts.md:20`: `| S792 | REFUSED | journal page is the English article; the four Chinese headings absent |` — still the wrong reason (the correction lives only in `corpus/lessons/round-72.md:63-68`). Tally 10/7/4=21 reproduces. S816/S817 page facts reproduce (A: `这个我肯定考虑过` 0 hits on 2025 page, 1 on 2022 page; `Sowers`/`Phonology` 0 on both pages — consistent with Quarantine text and with F2's S901 attribution; the lesson's "belongs to the lane's S880 document" is right: staged S901 = lane S880 `anderson-etal-cjl-sotl.pdf`).

### F11 — LOW — S895's id-map prose lists S729/S730/S742/S743/S754 as "not in the row set" while the lane registry holds all five as unrelated documents
`grep -n '^| S729' corpus/SOURCES.md` → 684 (infant-directed speech, PLOS ONE), S730 685 (Genesee), S742 697 (Shields-Lysiak), S743 698 (Akita), S754 710 (UNESCO tugging). The lesson's phrase "not in the row set" is wrong for the lane registry and for S895 for the staged one (see F1); say "campaign-namespace ids, collide with unrelated lane documents; not keys".

## What was attacked and held

- All four probed URLs are 200 for both UAs and byte-identical to the lesson's captures; the S881–S884/S877 admitted quotes each occur exactly once in the round-74 captures' text (S877 via pdftotext p.7; S883 `…先做的是世界观…` 1; S884 `把它放在前面大概20章之内慢慢来，我觉得是问题不大的` 1).
- 2 / 4 / 34 / 40, the family counts (5 / 11 / 3 / 2 / 9 / 3+1) and the four "differ" sha256 pairs reproduce.
- S882 not-appended reason (same document as S877) holds.
- Quarantine tally 10+7+4 = 21 and the committed round-71 verdict ids reproduce.

## Verification not run / out of scope
I did not re-run `accept-ca.py` (not in this seat's attack); I did not check the 22 collision pairs or the 808-row census (other seats). The "no capture" ruling was never made, so no CDX probe owed. No tool installed or updated.
