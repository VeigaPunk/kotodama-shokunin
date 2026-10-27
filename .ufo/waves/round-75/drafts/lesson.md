# Round 75 — kotodama: the narrative-structure thread closes (structuralist sources + CJK narratology)

**Status: DRAFT, pre-freeze, pre-data.** Quotes below were located by this seat on 2026-10-27; the committed
capture pointers (`reports/round-75/evidence/<id>.txt`) are written by `ExecEvidence` from its own fetch, and the
two must agree on the quote. Nothing here is frozen until the freeze commit adds these bytes to
`reports/round-75/claims.json` + `ledger.json` + `id-renumber-map.json` + both counters + the controls.

**Claims line.** Lane `kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`, hyaku run 10, one v1
wave of 42 seats (15 scout · 2 connector · 6 scribe · 8 executor · 3 reviewer · 4 critic · 2 mutation-tester ·
1 sentinel · 1 simplifier). At base: 808 registry rows (last id S884), 249 knowledge files, 0 files whose path
matches `narrative`. **C (coverage, sourced):** eight rows S885–S892 opened and mined (plus S893, the re-opened
S870 document), two entries (the base entry and its dated amendment) over ground no lane file governs, and
`reports/round-75/accept-c.py` printing `ACCEPT-C-75: PASS legs=13/13`. **Ca (calibration):** eleven ledger pairs
(4 REPAIR, 7 ANNOTATE) over the round-74 closure defects R1–R4 and this lesson's routed items, with the R1
append-only exemption demonstrated both ways, and `reports/round-75/accept-ca.py` printing
`ACCEPT-CA-75: PASS legs=12/12`. No seat had scored landed data when this draft was written; the freeze revision
is recorded by the L1 and is not guessed here.

## Gate

Access date for all nine rows: 2026-10-27, browser UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/130.0 Safari/537.36`, one plain `curl -L` request per URL (HTTP status and byte counts
in the capture column; the seat's own fetch records are in `.ufo/waves/round-75/w1/ScribeLesson.md`). Every quote
is at most 25 whitespace tokens and at most 80 characters and occurs in the stored text after NFKC and whitespace
folding; the lengths are given per row.

| source | access date | quote (≤25 words) | locator | evidence capture | verdict |
|---|---|---|---|---|---|
| S885 — Roland Barthes, «Introduction à l'analyse structurale des récits», *Communications* 8 (1966), pp. 1–27 — https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 | 2026-10-27 | «Innombrables sont les récits du monde.» (38 chars, 6 tokens) | notice body, opening sentence of the article (article p. 1) | `reports/round-75/evidence/S885.txt` (pending ExecEvidence); seat fetch 13:56 local, HTTP 200, 111487 B, sha256 `9be2c68d1b969364f581d6bed2648dc1289b6ad42cc05b8a25f455605a780f26` | admitted |
| S886 — Tzvetan Todorov, «Les catégories du récit littéraire», *Communications* 8 (1966), pp. 125–151 — https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 | 2026-10-27 | «Étudier la « littérarité » et non la littérature» (48 chars, 9 tokens) | notice body, first sentence (article p. 125) | `reports/round-75/evidence/S886.txt` (pending); seat fetch 13:56, HTTP 200, 111234 B, sha256 `70e5327944e34654e1f73b09f9237e61c9bf7fe5e134ed604c6c4f6bd6a127ac` | admitted |
| S887 — A. J. Greimas, «Éléments pour une théorie de l'interprétation du récit mythique», *Communications* 8 (1966), pp. 28–59 — https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 | 2026-10-27 | «Loin de se limiter à l'interprétation des énoncés, la théorie sémantique» (72 chars, 11 tokens) | notice body, §I opening paragraph (article p. 28) | `reports/round-75/evidence/S887.txt` (pending); seat fetch 13:56, HTTP 200, 116879 B, sha256 `71ab57f04ba1ed8af3bd81abcccc0b83685968a0185f3e100cac1ae3c2f44a8b` | admitted |
| S888 — 中国社会科学院大学 新闻传播学 叙事学课程 syllabus (PDF) — https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf | 2026-10-27 | 故事是一种深层的抽象结构，必须通过话语呈现 (21 chars, 1 token) | PDF p. 3, §课程教学计划「第二讲 故事：事件（一）」, item 一 | `reports/round-75/evidence/S888.txt` (pending); seat fetch 13:56, HTTP 200, 225123 B, sha256 `62a13e92e23d764c88d1e58f64cde00eb90a6aee900d52fa431bde9ca89334d1` | admitted |
| S889 — 小方孝「物語生成の物語論あるいはポストナラトロジー」, *認知科学* 25(2), 200–217 (2018) — https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf | 2026-10-27 | "a new research area called “narratology of narrative generation”" (64 chars, 9 tokens) | PDF p. 1, English abstract (「解 説」) | `reports/round-75/evidence/S889.txt` (pending); seat fetch 13:56, HTTP 200, 1085244 B, sha256 `fdf60d276b3f31cded2a40b8a12085f4b88e7f645062e3e2c9d9f8c647072b58` | admitted |
| S890 — 村井源「物語構造の階層的記述方式の提案」, *情報知識学会誌* 32(2) (2022), 第30回年次大会予稿 — https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf | 2026-10-27 | "describe a story as a hierarchical structure consisting of three major layers" (77 chars, 12 tokens) | PDF p. 1, English abstract | `reports/round-75/evidence/S890.txt` (pending); seat fetch 13:56, HTTP 200, 697092 B, sha256 `1dccf9d1427defb0e07e99461301cfd0ef5b5734716783a8ba0bb782de422272` | admitted |
| S891 — «BARTHES, Roland (1970) S/Z», fiche de lecture, CeRNET (Université de Genève) — live https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html ; durable copy https://web.archive.org/web/20041220223357/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html | 2026-10-27 | «les premières lexies suscitent l'établissement des cinq grands codes» (68 chars, 9 tokens) | archived capture body, the paragraph on the five codes (*S/Z* fiche) | `reports/round-75/evidence/S891.txt` (pending, from the capture); seat fetch of the capture 13:58, HTTP 200, 5693 B, sha256 `be01bc0e40a00f8bc9168abf54fdd409e6631e87b869cb0a7a9174599b56d9e4` | admitted on the archive copy; the live URL met an anti-bot challenge and was not passed (see rejects) |
| S892 — Marrone, «L'âge d'or du récit» (dépôt IRIS UniPa), 25 pp. — live https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf ; durable copy https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf | 2026-10-27 | «Mais combien, et de quelle nature, sont ces codes ?» (51 chars, 10 tokens) | archived capture, PDF p. 7 of 25 (the passage on Barthes's five-code typology) | `reports/round-75/evidence/S892.txt` (pending, from the capture); seat fetch of the capture 13:58, HTTP 200, 763802 B, sha256 `8c0303670ff5db8625d034be958ad5729a2c79fa77f3642efc5f6341fb25a19a` | admitted on the archive copy; the live URL answered HTTP 403 (see rejects) |
| S893 — 三九音域「世界观是打开小说幻想屋的钥匙」, 中国作家网 2023-09-22 (the document staged row S870 names, re-opened) — https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | 2026-10-27 | 网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则 (39 chars, 1 token) | §世界观是打开小说幻想屋的钥匙, byline □三九音域, paragraph 1, sentence 2 (inside 《我是怎样创作网络小说的——网络文学名家六人谈》) | `reports/round-75/evidence/S893.txt` (pending); seat fetch 13:56, HTTP 200, 45238 B, sha256 `51251e22c617617af797d164684e8927dc792a06140ff35fbaebc158515415f0` | admitted, **conditional on row_set amendment R75-M4** — S893 is outside the drafted row_set S885–S892 |

Rejections — the three probed rows this round, each with its reason, its re-test output and its flip:

| reason | flip | probed URL | verdict |
|---|---|---|---|
| staged S870 is not appended as staged: its register span `作品中的人物名字和地名也一样…` is absent from the served page. Re-test on the 45238 B body (2026-10-27): `grep -c '作品中的人物名字和地名'` → 0, and the three shorter fragments `人物的名字` / `名字和地名` / `地名也一样` each → 0, while the page's own 世界观 section is present (1 hit). The round-71 reason class ("quoted span absent") is confirmed on the page; what is wrong is the row text, not the page | a fresh quote located on the same page this round, which is what S893 carries | https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | refused as staged; document re-opened as S893 |
| the live URL of S891 is not an openable anchor by ordinary means: the 200 response (46013 B, sha256 `c08372f1…dab96f`) is an anti-bot shell that sets a `bobcmn` script and asks for a code — a challenge met and not passed, and no attempt was made to pass it | the same page's Wayback capture (2004-12-22) answers 200 with the fiche's body text; the row must name live URL + capture and say the challenge was met and not passed (QUALITY 10/18/22) | https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html | refused as a live-only anchor |
| the live URL of S892 answers HTTP 403 with a Cloudflare interstitial (`<title>Just a moment...</title>`, 5867 B, sha256 `92a72928…f7a81`) — a challenge met and not passed | the Wayback capture of the identical retrieve path answers 200 (763802 B, 25 pages) and carries the quote on PDF p. 7 | https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf | refused as a live-only anchor |

Gate notes, each one a decision a reader can re-check:

- **The persee page-level transcription is open, and the staged caveat is false.** Three page URLs were requested
  the same plain way: `…/doc/page/comm_0588-8018_1966_num_8_1_1113/…_T1_0011_0000` (p. 11, 4061 B, sha256
  `9cbf7c94…5143`), `…/1120/…_T1_0139_0000` (p. 139, 3939 B, `16992c94…d724`), `…/1114/…_T1_0030_0000` (p. 30,
  3737 B, `25027682…082f`). All three answer HTTP 200 with article text and no login, paywall or challenge; the
  located spans «ce sont des données pures, immédiatement signifiantes» (p. 11), «Le temps du discours est, dans
  un certain sens, un temps linéaire» (p. 139) and «possèdent une autre propriété qui consiste à comporter une
  séquence initiale» (p. 30) fold-match their pages. The staged base entry's claim that "the full French text is
  served through a JavaScript viewer, so this entry's Western claims rest on the notice and the opening paragraph
  only" is therefore retired (R75-M5); the deeper page locators are citable with their own captures.
- **Row anchors stay on the notice page, not the page transcription.** S885–S887 carry notice-body quotes so that
  the row's own anchor (live URL + same-page capture) is the artifact the quote was observed on. The page-level
  observations above are locator evidence for the entries, cited separately.
- **Challenge rows say so.** S891 and S892 are admitted on archive copies and must record "challenge met and not
  passed" in the row, per QUALITY 10 (a challenge met and routed around by an ordinary copy is not a bypass).
- **The S892 sha256 is over the Wayback response body**, i.e. the archived PDF bytes; the live URL never served
  those bytes to this seat.
- **S893 sits outside the drafted row_set.** `reports/round-75/claims.json` row_set ends at S892 (8 rows) while the
  seat scope and this Gate name S893. If the freeze keeps 8 rows, claim C's ROWS leg ("adds exactly the frozen
  row_set") cannot admit S893 and the entry cannot cite it (R75-M4). The fix is pre-data, not post-hoc.

## Triage (40 staged knowledge files)

Measured 2026-10-27: 40 staged `.md` files under `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge`;
40 family-classified, **2 adopted / 6 path-present with differing staged bytes / 32 refused** (2 + 6 + 32 = 40).
Path presence and byte equality were re-measured against the lane tree (249 files), not taken from round 74.

- **Adopted (2):** `myth-symbol/narrative-structure-frameworks.md` and `…amend-2026-10-23.md` — the two entry paths
  claim C names; both land quoted against S885–S890.
- **Path-present with differing staged bytes (6), decision owed (routed item 2):**
  `culture-material/heritage-taxonomy-models.md` (`b17223b9a04b` staged vs `09175b1849fb` lane),
  `…heritage-taxonomy-models.amend-2026-10-24-r13.md` (`9ed5ceefe5b1` vs `8544fe1ec531`),
  `culture-material/worldbuilding-setting-practice.md` (`44a0899c5054` vs `990e667c34bf`),
  `…worldbuilding-setting-practice.amend-2026-10-23.md` (`39ac34ea0292` vs `49a4432ae83b`),
  `linguistics/conlang-scholarship.md` (`ce666a2bf15d` vs `fe7e214adb04`),
  `…conlang-scholarship.amend-2026-10-23.md` (`8f889666b32c` vs `01029a642c9f`). Round 74 named four; the two
  worldbuilding files round 74 adopted also differ, because the landed entry is an edited adopt, not the staged
  bytes. Every one of the six is the same class: a diff for new claims, or a recorded supersession, per file.
- **Refused (32), by family, each with reason and flip:**

| family | files | why not adopted | flip / clearing condition |
|---|---|---|---|
| narrative-structure-frameworks amendments b / c / 2026-10-24 (3) | `…amend-2026-10-23b.md`, `…amend-2026-10-23c.md`, `…amend-2026-10-24.md` | their cited documents now open — S891 (S/Z fiche, b), the persee p. 11 text (c, via S917's URL class), S892 + the persee p. 6 text (2026-10-24) — but claim C's frozen entry set is two files, and an amendment needs its parent row plus its own located quote per cited document | land as appended amendments citing S891/S892 and the page-level URLs with their own captures; one round per parent |
| naming-systems amendments (11) | `…naming-systems.amend-2026-10-23.md`, `-2026-10-23b`, `-23c`, `-2026-10-24`, `-24-r10` … `-24-r16` | no lane row holds the document; the amendment chain re-states one topic without a located quote per claim | one row per document, each with a round-N capture and a located quote |
| calendar-festival-systems amendments (3) | `…calendar-festival-systems.amend-2026-10-23c.md`, `-2026-10-24.md`, `-2026-10-24-r10.md` | parent entry and sources are not lane rows; dates asserted from memory of the text | register the parent and the calendar sources, then re-quote |
| era-periodization-models amendments (2) | `…era-periodization-models.amend-2026-10-23.md`, `-2026-10-23b.md` | same class as calendar: no parent row, no located span | register the parent and its sources first |
| verification amendments (9) | `…citation-format-and-source-registry.amend-2026-10-24-r10` … `-r16` (7), `…journal-serial-catalogue-records.amend-2026-10-24-r16.md`, `…reopen-gate.amend-2026-10-24.md` | lane-internal process texts, not source-backed domain knowledge; no registry row can support them | an own-work `source:` path with a lane-relative locator, or leave them as lessons |
| conlang-scholarship amendments b / c / 2026-10-24 + conlang-methodology 2026-10-24 (4) | `linguistics/conlang-scholarship.amend-2026-10-23b.md`, `-23c`, `-2026-10-24.md`, `linguistics/conlang-methodology.amend-2026-10-24.md` | amendments to entries the lane holds; their quoted spans were not re-opened this round and the staged bytes differ from the lane's | re-open each amend's quotes against the parent entry's rows and land as appended amendments |

**S870's disposition, stated once.** The staged row stays REFUSED (its register span is absent from the page, 0
hits, re-test above). The *document* is re-opened as S893 with a fresh located quote — a re-opened document, not a
reversal of the round-71/72 verdict.

## Mistakes

Rules: `CORPUS.md` §"Rules added from the kaika campaign" — one row per mistake, class · evidence pointer ·
captured-by · fix; a fix counts only once shown able to fail.

| id | class | evidence | captured-by | fix | state |
|---|---|---|---|---|---|
| R75-M1 | attribution | A Gate reject reason names an artifact it was **not** observed on: the round-72 lesson's S870 row files "register S787" as the artifact whose span was absent, but at base lane registry S787 is the Koiso fragrance paper (`corpus/SOURCES.md:741`), while the observation was made on the China Writers page (register S787 in `reports/round-71/telemetry/quarantine-verdicts.md:18`; reason text `corpus/lessons/round-72.md:31`). Both id namespaces are in play and only one is the lane's | **none** — spotted by this seat on 2026-10-27 while re-testing the span against the page | QUALITY 27 (owed this round): a reject reason names the URL whose response it was observed on, plus that response's fetch record; and the L75-05/L75-06 corrections bind each reclassification to a `git grep -c` on the named capture. Shown able to fail: the counter re-runs the command on the named capture, and a reason bound to the wrong page's capture returns 0 | open — criterion not yet written |
| R75-M2 | instrument | The corpus README sweep grades the **first** `Counts checked` footer: `reports/round-28/readme/sweep.py:108` runs `FOOTER_RE.search(text)`, which returns the block at `corpus/README.md:751-753` (total 243, directory totals 30/29/36/29/24/95) and never the last one (`:815`, total 249, 32/29/40/29/24/95), so a tree whose last footer is right exits red. The stale `## linguistics/ (30)` (`:344`, live 32) and `## culture-material/ (36)` (`:407`, live 40) are the same defect seen twice | **none** before this round — round-74 routed item 3/M3; this seat read the code and both footers | the L75-04 repair: the sweep reads the **last** footer and lands with two committed receipts the counter re-runs in clones — `sweep-red-before.txt` (base tree, exit 1) and `sweep-green-after.txt`. Shown able to fail: the before-tree run exits 1 on the same instrument in the same round | fix routed to L75-04; counter leg pending |
| R75-M3 | instrument | A staged recheck cell asserts a count its own span fails: `myth-symbol/narrative-structure-frameworks.md:34` records `S870 → 1 (ran 2026-10-23)`, while the register span `作品中的人物名字和地名…` returns 0 on the 2026-10-27 fetch of the same URL (four fragment probes also 0; the page's own 世界观 passage returns 1). The recheck "1" cannot be reproduced from any byte this seat can fetch | this seat (2026-10-27), on the fetched body | the Gate carries the re-test output (QUALITY 12), the recheck cell lands cadence-only like the round-74 rows, and the located quote lives on the evidence file. Shown able to fail: the recheck-count check recomputes `grep -c` over the capture and a 0 fails it | open |
| R75-M4 | reference-drift | Claim C's drafted row_set ends at S892 (8 ids) while the seat scope, the scout brief and this Gate name S893: an S893 landing would fall outside the frozen ROWS leg ("adds exactly the frozen row_set"), so the row could be neither counted nor cited, and the by-document map would have no S870 → S893 entry | this seat, pre-data (claims.json `row_set`; `w1/spec.json` ScribeChinawriter2023/ScribeLesson) | the freeze adds S893 to the row_set with its map entry (`staged S870 → S893`, joined by document, never by arithmetic), or the entries cite no S893. Shown able to fail: the map sha256 is pinned in the frozen claims and the COLLCHECK leg joins staged→lane by document, so a missing target fails the join | open — pre-freeze decision, L1 |
| R75-M5 | scope | The staged base entry retires the Western primary source to the notice only: "the full French text is served through a JavaScript viewer, so this entry's Western claims rest on the notice and the opening paragraph only". Falsified 2026-10-27: the three page-level transcription URLs answer a plain browser-UA request with HTTP 200 and article text (4061 / 3939 / 3737 B) and no login, paywall or challenge, and the p. 11 / p. 139 / p. 30 spans fold-match their pages | this seat (2026-10-27), four requests, records in `.ufo/waves/round-75/w1/ScribeLesson.md` | cite the page-level URLs for the deeper locators and delete the caveat; the entry's scope widens only through those captures. Shown able to fail: a page URL that answers a challenge, an empty body or a login page fails the same fetch check | open — the entry's text is not this seat's |

## Quarantine

**The standing register verdicts, re-derived, not re-fetched.** `reports/round-71/telemetry/quarantine-verdicts.md`
holds 21 data rows (18 `payload-absent` + 3 unreachable-class): re-counted 2026-10-27 with
`grep -c '| PRESENT |'` → 10, `grep -c '| REFUSED |'` → 7, `grep -c '| UNVERIFIABLE |'` → 4, rows matching
`^| S[0-9]{3} |` → 21.

- **PRESENT 10:** S776, S778, S795, S796, S804, S820, S823, S824, S825, S827.
- **REFUSED 7:** S779, S786, S787, S792, S814, S816, S817.
- **UNVERIFIABLE 4:** S791, S807, S812, S835.

Register S816 and S817 stay REFUSED as register rows: their verdicts are about the *register's* URL↔quote binding,
not about the documents, which were re-opened as lane rows S883/S884 in round 74 (see Corrections). The register's
ids are not lane ids: register S787 is the China Writers page while lane row S787 at base is the Koiso fragrance
paper (`corpus/SOURCES.md:741`) — the namespace drift that R75-M1 records. No verdict above is upgraded or
retired by this round's S893 admission; that admission is a different document, quoted fresh.

## Corrections

**L75-05 / L75-06 — the round-74 Gate reject rows reclassified (adopt-with-renumber, not rejects).** The round-74
lesson filed two rows whose reject reason was observed on the *wrong* artifact: the staged rows' own spans are
present on their own pages. The filed bytes stand (append-only); the annotation lands as SCORECARD
`## Corrections — round 75` rows L75-05/L75-06 and as this section. QUALITY 27 is the criterion this round owes
(`corpus/QUALITY.md` ends at criterion 26 at base; `git show <base>:corpus/QUALITY.md | grep -c '^27\.'` → 0).

| where | old (as filed) | new (reclassified) | re-derivation command | output 2026-10-27 |
|---|---|---|---|---|
| `corpus/lessons/round-74.md:37` (staged S899 → lane S883) | "staged S899's quoted span was absent from the page it was bound to (register S816 mispairing; the span belongs to the 2022 interview) — the row stays refused and the document is re-opened as the new S883" | the staged span `非凡特性来自最初造物主` is present once on its own 2025 page in the committed round-74 capture; the absent span (`这个我肯定考虑过`) is register S816's, bound to that page. Disposition: adopt-with-renumber (S899 → S883), not a reject; the mispairing belongs to register S816 | `git grep -c '非凡特性来自最初造物主' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S883.txt` | `1` |
| `corpus/lessons/round-74.md:38` (staged S900 → lane S884) | "staged S900's quoted span was the Sowers-Wills clause, absent from this page (register S817 mispairing) — the row stays refused and the document is re-opened as the new S884" | the staged span `这个我肯定考虑过` is present once on its own 2022 page in the committed round-74 capture; the Sowers-Wills clause is register S817's and belongs to lane S880's document. Disposition: adopt-with-renumber (S900 → S884); the mispairing belongs to register S817 | `git grep -c '这个我肯定考虑过' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S884.txt` | `1` |

**Routed-on items, carried, none silently closed:**

1. **S877 scope-cell supersede row** (round-74 routed item 5): the round-74 entries cite S877 (a classification
   monograph) outside its registered scope cell, and the append-only rule forbids widening the cell. A superseding
   row with its own scope and window is owed. Status: open; the drafted row_set contains no S877 successor, so this
   round does not close it.
2. **Path-present byte decisions** (round-74 routed item 2): six files, sha256 pairs in Triage above. Status:
   measured this round, decision open (diff-for-new-claims vs recorded-supersession, per file).
3. **Register adjacency guard, R74-M5** (round-74 routed item 5): the checker that pairs a register row's URL with
   its quote needs an adjacency guard, because the register's rows S816/S817 bind each URL to the next row's quote.
   Status: open; R75-M1 above is the same class reaching a Gate reject reason.

