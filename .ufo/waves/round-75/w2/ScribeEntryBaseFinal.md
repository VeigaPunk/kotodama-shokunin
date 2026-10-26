# ScribeEntryBaseFinal — final canonical claim-C entry, round 75 wave 2

Seat: ScribeEntryBaseFinal (leaf scribe, no delegation). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`. Wrote exactly two files: the staged entry below and this report. No lane git/jj state, registry, README, lesson, counter, fleet file or shokuknow byte was touched; claims.json and ledger.json were read only.

## 1 Behaviour — what is staged

| Item | Value |
|---|---|
| staged path | `.ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` |
| sha256 | `3ea4d6f80715460423fada252499dac9a95010a3bb4dd292c7ea834eab78fc13` |
| size | 30,920 bytes, 199 lines |
| words | 5,014 total (`wc -w`); 4,247 from the first `## ` heading, against the 478-word ENTRIES floor |
| `## ` sections | 12 |
| ids cited | `S885`, `S888`, `S889`, `S890`, `S893` — and nothing else (no staged/campaign id, no base registry id) |
| header | provenance block first, order `source` (five lines, one id each) / `verified-at` / `recheck` / `ground` / `topic` / `gap filled` / `sources` / `couples` / `scope` |

The entry is one file with one `- topic:` line (the INDEX leg takes the first match; there is only one). It is a rewrite, not a copy: every fact-bearing sentence was checked against a page I fetched this session, and every sentence the staged draft carried that the page did not carry was cut rather than cited.

## 2 Re-opens — the execution evidence this seat produced

UA used for every request: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. `curl -sS -L`, ordinary GET, no challenge encountered on any of the five documents.

| row | request | result | quote I located |
|---|---|---|---|
| S885 notice | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` | HTTP 200, **111,487 B** `text/html;charset=UTF-8` | «Innombrables sont les récits du monde.» in the body, and the genre/substance list that follows it |
| S885 p. 1 transcription | `…/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0001_0000` | HTTP 200, 3,231 B | article opening, same sentence |
| S885 p. 5 | `…T1_0005_0000` | HTTP 200, 4,286 B | «aucun niveau ne peut à lui seul produire du sens»; «ne prend de sens que si elle peut s'intégrer dans un niveau supérieur» |
| S885 p. 6 | `…T1_0006_0000` | HTTP 200, 3,811 B | «trois niveaux de description» with the three names; «ces trois niveaux sont liés entre eux selon un mode d'intégration progressive»; «le sens n'est pas « au bout » du récit, il le traverse» |
| S885 p. 11 | `…T1_0011_0000` | HTTP 200, 4,061 B | «Noyaux et catalyses, indices et informants … les premières classes»; «certaines unités peuvent être mixtes»; «le récit est infiniment catalysable» |
| S888 | `https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf` | HTTP 200, 225,123 B `application/pdf` (identical to the row) | PDF p. 3, 课程教学计划, 第二讲 故事：事件（一）, 一： 「故事是一种深层的抽象结构，必须通过话语呈现」 |
| S889 | `https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf` | HTTP 200, 1,085,244 B (identical to the row) | p. 200 English abstract: `a new research area called “narratology of narrative generation”` |
| S890 | `https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf` | HTTP 200, 697,092 B (identical to the row) | p. 246 English abstract: `describe a story as a hierarchical structure consisting of three major layers` |
| S893 | `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` | HTTP 200, 45,238 B (identical to the row) | 「网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则」 |

Page numbers were mapped from each PDF's own printed markers, not guessed: S889 pdf p. 1/4/8/10 = printed 200/203/207/209; S890 pdf p. 1/2/3 = printed 246/247/248.

Locators the entry actually uses: S885 notice body and pp. 5, 6, 11; S888 PDF p. 3 (第二讲, 第三讲) and p. 4 (三个维度, 查特曼的六种参与者); S889 pp. 200, 203, 207, 209; S890 pp. 246–248; S893 the section headed 世界观是打开小说幻想屋的钥匙.

## 3 Gates run

| Check | Command | Verbatim outcome |
|---|---|---|
| CITEDLINES (criterion 15) | `python3 -B tools/check-cited-lines.py <staged entry>` | first run `MULTI-ID …:61 S888,S890` / `CITED-LINES: 1 finding(s) in 1 file(s)` exit 1; after the split, `CITED-LINES: 0 finding(s) in 1 file(s)` exit 0 |
| body floor | `wc -w` and a body-only count from the first `## ` | 5,014 total, 4,247 body |
| ENTRIES helpers (round-74 counter imported read-only in scratch) | `header_field_names`, `HEADER_FIELDS`, placeholder and `ANGLE_RE` scan over `header_block`, body-word count | `missing header fields: []`; `placeholder scan:` with no PLACEHOLDER or ANGLE line; `body words 4247` |
| REPOINTED helpers, same import | `source_lines`, `TOKEN_RE`, `urls_in`, `norm_url` against the staged 817-row registry (`parse_rows` → `rows parsed 817`) | `S885 ids ['S885'] urls 1 all-in-row True`; `S888 … True`; `S889 … True`; `S890 … True`; `S893 … True`; `not-in-row []` for every one |
| id census | `grep -oE '\bS[0-9]{3,}\b' <entry> \| sort \| uniq -c` | `13 S885 / 13 S888 / 10 S889 / 15 S890 / 5 S893` |
| banned wording | `grep -inE 'axes\|grid\|序説\|PENDING'` | 0 hits for axes/grid/序説; the single `pending` hit is the word "depending" in body prose |
| hygiene | trailing whitespace and final newline | 0 trailing-whitespace lines, file ends with a newline |

No build, test suite, formatter or lane-git command was run; nothing was installed (no tool, no channel), so there is no install row to record.

## 4 Findings from wave 1 that were reachable — applied, and why

`RevEntryQuality.md` **does not exist** in the wave tree. `grep -rln RevEntryQuality .ufo/waves/round-75` returns only `w1/spec.json`, `w1/dispatch.json`, `w1/swarm-registry.json`, `w1/w1-results.json`, `build-w1.py`, `build-w2.py`, `w1.ready.dispatched`, two peer reports (`ConnectorPatterns.md:56`, `ScribeEntryBase.md` §) and two unrelated lessons; `find .ufo/waves/round-75 -name 'RevEntry*'` is empty. The F1–F13 list its task was to produce is therefore unreachable, and I did not invent it. What I could reach and did apply:

| Source | Item | Disposition |
|---|---|---|
| SimplifierRows §5 | S889/S890 were **swapped** in the draft | **Applied.** S890 (jsik) carries the three-layer format and 起承転結; S889 (jcss) carries narrative generation. Verified on the pages: `クエスト`/`シーン` occur 15/19 times in S890 and 0/0 in S889; `起承転結` occurs 2 times in S890 and 0 in S889 |
| SimplifierRows §5 | "three time axes", "participant grid" are glosses, not the page's words | **Applied.** 三个维度 and 六种参与者 are used verbatim; "axes"/"grid" appear nowhere in the file |
| SimplifierRows §5 | S885's premise sentence may cite the article for a QUALITY-10 rule | **Applied.** No sentence cites any row for an access rule; the route is stated in the header as method, id-free |
| SimplifierRows §3 | cut the Barthes p. 26 "two readings" quotes (duplicate of Greimas, outside S885's window) | **Applied.** Not used; p. 26 is not quoted at all |
| SimplifierRows §3/§6 | the five S/Z codes are not recoverable from S885 and must not be attributed to the 1966 article | **Applied as a verified negative.** Grep over the four served texts: `code` 0, `cinq` 0. The entry says so with the check's date and defers the codes to the amendments |
| SimplifierRows §4 | one row = one window; do not quote pages outside it | **Applied.** Every S885 quotation I use is on pp. 5, 6 or 11 (or the notice), and the entry states no claim from a page it does not quote |
| SimplifierRows §2.1 | with S893 adopted the block is contiguous S885–S893 | **Confirmed against the staged registry** (`parse_rows` → 817 rows, all nine present) |
| SentinelScope S-75-9 | fetch `/doc/page/…` only; `docAsPDF` is altcha-protected | **Applied.** No `docAsPDF` request was made; the notice links the page URLs and I fetched from them |
| SentinelScope S-75-5 | staged recheck cells carry `/tmp` paths and pipelines; entry `recheck:` must be a cadence | **Applied.** One `recheck: 180d — …` line, no command, no `/tmp`, no multi-id list |
| SentinelScope §5 | the staged base entry's "Superseded passage … Trim it" editorial block must not ship | **Applied.** Absent; the entry has no editorial instruction |
| SentinelScope S-75-6 | entry `source:` lines must each carry one lane id | **Applied and machine-checked** (§3, REPOINTED helpers) |
| RevAssimilationContract F6 | staged header prose with multi-id `recheck:`/`ground:` lines is CITEDLINES-red | **Applied.** `recheck`/`ground`/`sources` carry no id at all; the five ids sit only on `source:` lines and in prose with one id each |
| RevAssimilationContract F5 | a single window cannot carry extra locators; name them | **Applied by scoping**: the entry states only what is on the pages it quotes and marks the rest queued (§12) |
| ScribeEntryBase §3.2 | a tree-wide "no such names" claim would be false | **Applied.** `ground:` makes only the base counts (808 rows, 249 files, 0 narrative-named paths) and a file-scoped statement about the two framework files |
| ScribeEntryBase §3.5/§3.7 | one `- topic:` per file; `verified-at` honesty | **Applied.** One topic line; `verified-at: 2026-10-27` with the fetch facts stated |

## 5 Conflicts, and interface obligations I cannot discharge myself

**5.1 The S885 notice served different bytes today than the row's evidence records.** Row/evidence: `109588` B (`sha256 20b571d7…25de034`, fetched 2026-10-27T19:48:02Z). My GET of the same URL with the same browser-shaped UA: **111,487 B**. The page is dynamic (SentinelScope saw the same class at S891, 48,789 vs 49,529 B). The EVIDENCE leg recomputes the window sha from the stored body, so this is not a leg conflict — but a reviewer re-opening the source will not see 109,588 B and should not read the difference as a wall or a wrong page.

**5.2 The `- topic:` text changed from the wave-1 draft, so the README index row is now stale.** INDEX requires the README row to carry the entry's own `- topic:` text verbatim. The draft topic (946-char README row) says "the three time axes (次序, 时长, 频率)" and "查特曼's participant grid", which are the two glosses SimplifiedRows struck, and it calls 起承転結 a "completable minimal unit" without naming its layer. The final topic is **978 characters** and the required README row is **1,018 characters**, beginning `- \`narrative-structure-frameworks.md\` — how narrative structure is theorised …` and ending `…; decision tables and calibration statuses, never a ruling on any culture's story`. Whoever lands `corpus/README.md` must rebuild that row from the entry (`.ufo/waves/round-75/drafts/readme-rows.md:117` is superseded). If the row is copied from the wave-1 draft instead, INDEX fails on this entry alone.

**5.3 Where 起承転結 actually sits — reported verbatim for the judge.** The draft said "起承転結 as a completable minimal unit" without naming a layer. S890 p. 248 says: 「クエストは特定の目標や，ハプニング・障害等を中心とした起承転結の構造の最小単位に相当する」 — the **quest** is the minimal unit of the 起承転結 structure. The same page also says a 起承転結 can complete inside one scene, which is the reason the scene splits on function change. The entry states both, and places 起承転結 at the quest layer in its tables. A reviewer who has the draft's wording in mind will read the entry as narrower; it is the page that is narrower.

**5.4 S889 does not name 起承転結.** `grep -c 起承転結` over the extracted text of the whole 18-page article: 0. The entry therefore takes the term from S890 alone and records the check in §12. This agrees with SimplifierRows §5 cut 8 ("if ScoutJstageJsik does not locate the term either, cut §6") in substance: the term survives, but on the other paper's row.

**5.5 S885 p. 6 carries the article's own three-level list, which the wave-1 draft treated as not served.** The draft's §2 said the level inventory was "a question for the Gate". The transcription of p. 6 carries 「On propose de distinguer dans l'œuvre narrative trois niveaux de description : le niveau des « fonctions » … le niveau des « actions » … et le niveau de la « narration »」 plus the progressive-integration sentence. The entry uses it. Consequence for the amendment: its Barthes section can cite pp. 5–6 rather than deferring the inventory.

**5.6 `couples:` names two files that land in the same round.** `myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` and `…amend-2026-10-23b.md` are in claim C's `entries` and are not in the tree at base (`[ -f ]` fails today). The five other couples were verified present at base. If either amendment is refused at triage, that clause is deleted with it; no other clause depends on it.

**5.7 Transcription quality, stated so no one re-quotes a garbled span.** The Persée per-page text is OCR-garbled and truncated at roughly 3.3–3.8 KB per page: p. 5 reads "Introduction à V analyse" for "l'analyse", p. 6 reads "Préfetoi'" for "Préfet n'omettait", the notice reads "l'bomme" for "l'homme". The entry quotes only clean spans and never a garbled one; a re-opener must expect the same truncation and must not treat a sentence beyond the ellipsis as absent from the page.

**5.8 S888 has no printed page numbers.** Its locator is structural (PDF p. 3, 课程教学计划, 第二讲 故事：事件（一）, item 一), which is what the row's anchor cell already says. The syllabus's lecture numbering is itself inconsistent (two lectures numbered 第六讲, two numbered 第七讲); the entry cites headings and item text, not lecture numbers alone.

## 6 Out of scope — not done, not claimed

- I did not write, and did not verify, the other claim-C leg surfaces: `corpus/SOURCES.md` appends, `corpus/README.md`, `corpus/lessons/round-75.md` `## Gate`, the two amendments, the counters, the renumber map, any telemetry or evidence file.
- I did not re-open `S886`, `S887`, `S891` or `S892`; those are other seats' rows and this entry cites none of them.
- I did not grade any leg. The helper simulation in §3 imports the round-74 counter's pure functions; it is not the round-75 counter, which does not exist in the tree yet.
- I did not edit claims.json, ledger.json, any draft, any w1 report, or anything under `/home/vgpnk/Projects/shokuknow`.

## 7 Scratch, tools, provenance

Scratch `/fast/scratch/hyaku/kotodama-r75/ScribeEntryBaseFinal/` — created for the fetch bodies, the PDF text extractions and the counter-helper import; **the directory disappeared mid-run** (present for the fetches at 16:49, gone when the helper import was first attempted; other seats' directories under the same root survived), so it was recreated for the helper run and is removed before this report is final. No citable evidence rests on a scratch path: every fetch receipt and quote is reproduced in §2 and §3 above, and the round's committed evidence files under `.ufo/waves/round-75/w2/stage/reports/round-75/evidence/` carry the stored windows.

Tools installed: **none**. Used `curl`, `pdftotext`, `pdfinfo`, `python3`, `git` (read-only), `grep`, `wc`; pacman was not invoked.

Files I wrote:

| path | sha256 |
|---|---|
| `.ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` | `3ea4d6f80715460423fada252499dac9a95010a3bb4dd292c7ea834eab78fc13` |
| `.ufo/waves/round-75/w2/ScribeEntryBaseFinal.md` | this report |
