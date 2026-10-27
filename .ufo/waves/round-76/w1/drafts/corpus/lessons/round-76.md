# Round 76 — kotodama: calendar compilation and era-name instruments (standards-level calendar + archival era tables, assimilated)

**FILED-AT-DRAFT.** Written 2026-10-27 by wave-1 seat `ScribeLesson-7` against the unfrozen claims at
`.ufo/waves/round-76/CLAIMS-DRAFT.md`; the freeze commit supersedes this file. `<<FILL: …>>` marks a value that
cannot exist before a landing — a landed hash, a landed count, a verdict a counter prints. No other value is
deferred: every number below is the output of the command printed beside it, and every command's raw output is
stored in `.ufo/waves/round-76/w1/stage/ScribeLesson-7/measurements.txt`.

**Claims line.** Lane `kotodama-shokunin`, base `98c486bdb4650ba5b8e651d332910e8ee60ad121` (`git -C … cat-file
-e` → exit 0), hyaku run 10, wave 1. **C (coverage, assimilation-sourced):** four documents opened at this
wave's Gate — the fifth planned row's URL turned out to be the fourth document's own redirect target (reject row 2) —
each with a located quote inside a stored window and each carrying a live or an archived carrier; the lane held
none of that ground in `corpus/knowledge` at base (`git grep -l -E 'GB/T 33661' 98c486b… -- corpus/knowledge` → no
output, exit 1; the same for `digital\.archives\.go\.jp`). **Ca (calibration):** `reports/round-76/ledger.json`,
>= 10 pairs fixed before data, `<<FILL: pair count and the REPAIR/ANNOTATE histogram as landed>>`, graded by
`reports/round-76/accept-ca.py` `<<FILL: the counter's verdict line as landed>>`.

## What the base holds, measured

Each line is one command with its raw output; the full block, including exit codes and the elapsed-order, is in
`measurements.txt`. No sentence in this lesson about the state of the repo is written without one.

- base commit present — `git -C … cat-file -e 98c486bdb4650ba5b8e651d332910e8ee60ad121` → exit 0.
- registry rows — `git -C … show 98c486b…:corpus/SOURCES.md` piped to `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` → `817`.
- registry id span — python over `.ufo/waves/round-76/assimilation/reg-ids` → `817 rows 817 unique; 76 missing: S455 S456 S457 S458 S459 S460 S461 S462 S463 S464 S465 S466 S467 S468 S469 S470 S471 S472 S473 S474 S475 S476 S477 S478 S479 S480 S492 S493 S494 S495 S496 S497 S498 S499 S544 S545 S546 S547 S548 S549 S550 S551 S552 S553 S554 S555 S556 S557 S558 S559 S563 S577 S578 S579 S580 S581 S582 S583 S584 S585 S586 S587 S588 S589 S590 S591 S592 S593 S594 S595 S596 S597 S598 S599 S777 S778`. The registry's rows are therefore *not* ids 1..N: 76 numbers in S001..S893 are absent, and S777 is one of them.
- knowledge files — `git -C … ls-tree -r --name-only 98c486b… corpus/knowledge` piped to `grep -c '\.md$'` → `252`.
- id lists — `wc -l .ufo/waves/round-76/assimilation/reg-ids .ufo/waves/round-76/assimilation/staged-ids .ufo/waves/round-76/assimilation/collisions` → `817`, `132`, `35`.
- their digests — `sha256sum` over the same three files → `97eef07a858487225118d5c2d18ceb919b8c9549a3768b9adee6a3a321dbd3a7`, `bab11d7d0ee0d84795b1ff80274fe371670fff73a477c747b2fd3cad4c25ddad`, `be203dd8b02cde5fcea89a04e882daa3f525200b8a801e324ad73cde2ebbaf47`.
- census at round start — `tail -2 reports/round-76/telemetry/census-start.txt` → `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` then `exit=0`; the same file is 34 lines, of which 28 carry `W04` and 4 carry `W01` (`grep -c`).

**The claims draft's Before leg is false as written, and this lesson does not repeat it.** It reads
`git grep -l -E 'GB/T 33661' 98c486b -- corpus` and `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus`
"each print nothing (exit 1)". At base the first prints two files (`corpus/lessons/round-68.md`,
`corpus/lessons/round-69.md`) and the second prints one (`corpus/lessons/round-68.md`), exit 0 both times. The
"no ground" claim holds only with the scope `corpus/knowledge`, which is the scope used above and in
`## Sources & frontier`. Routed to round 77 as a claim-text defect for the freeze.

## Gate

Access date for every row: **2026-10-27**. One plain request per URL under the browser-shaped UA
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, each
request's UA bound to the response that request got (QUALITY 22). Receipts: `w1/stage/ScribeLesson-7/fetch-receipts.md`
(UA, URL, status chain, wire bytes, stored bytes, sha256, server date); raw bodies:
`.ufo/waves/round-76/w1/stage/ScribeLesson-7/fetch/`; stored windows:
`.ufo/waves/round-76/w1/stage/ScribeLesson-7/windows/`, each carrying its own fetch line, its own `body-sha256:`
and an `anchor-hits-in-window:` count. The `windows/…` names in the evidence column below are relative to that
directory; the landing must copy each into `reports/round-76/evidence/S89x.txt` `<<FILL: the landed evidence
files' own fetch lines>>`. Every quoted span below is inside both caps — 25 whitespace tokens **and** 80
characters — with the measured lengths given per row (NFKC + whitespace folding).

| source | access | quote (≤25 words) | locator | evidence (this round's stored window) | verdict |
|---|---|---|---|---|---|
| **S894** — 国立公文書館デジタルアーカイブ, 詳細検索, 元号選択／和暦元号 table; live `https://www.digital.archives.go.jp/search` + capture `https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search` (one row, two carriers) | 2026-10-27 | 「元号名称 開始西暦年 令和 2019 選択 平成 1989 選択 昭和 1926 選択 大正 1912 選択 明治 1868」 (62 chars, 16 tokens) | 元号選択 → 和暦元号: the header cell and the first five era rows, cells read in document order (the 選択 buttons included) | `windows/S894-live.txt` — HTTP/2 200, 311308 B, sha256 `204b7188…`, excerpt 4096, hits=1; `windows/S894-capture.txt` — 307700 B, sha256 `c015e1dc…`, same table, same hits | admitted (tier A) |
| **S895** — 星座百科网, «国家标准《农历的编算和颁行》GB/T 33661-2017 原文及解读材料», `https://www.xingzuobaike.com/huangli/wannianli/d165803.html` | 2026-10-27 | 「取其中最先出现的一个不包含中气的农历月为农历闰月」 (24 chars, 1 token) | 标准主要内容 → 1. 农历的编排规则, clause （4） (the leap-month rule) | `windows/S895-live.txt` — HTTP/2 200, 9093 B on the wire (33179 stored), sha256 `83049559…`, excerpt 4096, hits=1 | admitted, **tier C** and declared as a reproduction; never an entry's sole support |
| **S896** — 全国标准信息公共服务平台 registry record for GB/T 33661-2017; live `https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296` (302 → `/bzgk/std/newGbInfo?hcno=…&refer=outter`) + capture `https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` | 2026-10-27 | 「当前浏览器暂不支持标准全文在线预览服务，请使用现代浏览器」 (28 chars, 1 token) | 在线预览提示 modal, following the 标准信息表 field rows (标准号 GB/T 33661-2017 … 发布单位) | `windows/S896-live.txt` — 302 → 200, 7334 B wire / 24144 stored, sha256 `80b4c781…`, whole-document 757, hits=1; `windows/S896-capture.txt` — 24174 B, sha256 `f04feb47…`, whole-document 757, the two visible texts `diff` clean | admitted (tier A); merged with the planned showGb row — reject row 2 |
| **S898** — 光明日报, «农历编算有了国家标准 春节端午等假期与其密切相关», 2017-05-23, `https://news.gmw.cn/2017-05/23/content_24559485.htm` | 2026-10-27 | 「规定了朔日为农历月的第一个农历日，包含冬至在内的农历月为农历十一月」 (33 chars, 1 token) | article paragraph 4 (01版, 记者陈海波): the sentence stating the 编排规则 | `windows/S898-live.txt` — HTTP/1.1 200, 8076 B wire / 25250 stored, sha256 `670850ea…`, whole-document 1663, hits=1 | admitted (tier A) |

Gate notes, each one a decision a reader can re-check:

1. **The planned fifth row is the fourth document.** `showGb?type=online` answers `HTTP/1.1 302` with
   `Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter`,
   which is the URL the S932 capture archives; the capture's visible text and the live page's are identical (757
   chars; `diff` prints nothing). One document, one row. **k counts documents: four.**
2. **The planned ids collide by number with five staged documents, and the collision list cannot show it.**
   `grep -E '^\| *S(894|895|896|897|898) ' …/merge/kotodama/SOURCES.append.md` returns: S894 Sowers-Wills 2024
   (doi 10.1017/cnj.2024.21), S895 王昕玥《论〈龙族〉的叙事失控与世界观危机》 (chinawriter 2025-10-30), S896 a
   Korean paper on Chinese surnames (KCI ART001409716), S897 魏斌〈單名與雙名〉 (lishisuo.cssn.cn), S898
   国立国会図書館 NDC10 (ndl.go.jp PDF). The package holds all five (`grep -cE '^S89[4-8]$' staged-ids` → 5); the
   registry holds none (`… reg-ids` → 0), so the intersection the guard prints does not contain them — the
   adoption *creates* five numeric collisions. Two honest ways out: renumber the new rows above both namespaces
   (the package's highest id is S990, so S991 onwards are free in both) `<<FILL: final lane ids as frozen>>`, or
   keep the numbers and carry the by-document map below, which names the other document per id. The claims'
   `35` is the pre-adoption intersection.
3. **The staged entry's byte claim does not reproduce.** Entry `calendar-festival-systems.amend-2026-10-24-r10.md`
   states that both routes return byte-identical 24148-byte responses, md5 `9791d9dc0f17384eeab4ff4791eed437`.
   Measured today, `type=online`, `type=download` and `/bzgk/gb/newGbInfo` all resolve to the same URL and the same
   stored body: 24144 B, sha256 `80b4c781…`, and `md5sum` printed `e866bfd61a16f4c4fcdc1fc3a16bdf89` for all three
   fetches. The *conclusion* survives — the download route serves the record page and no file (no
   `Content-Disposition`) — the number does not.
4. **Two citations in the staged entries do not resolve to the rows they name.** Entry
   `calendar-festival-systems.amend-2026-10-24.md` writes that the drafter's interpretation PDF "was already held
   (S777)": base has no S777 row (`git -C … show 98c486b…:corpus/SOURCES.md` piped to `grep -E '^\| *S777 '` → 0
   rows), no commit introduced a row in the registry's own shape (`git -C … log --oneline -S '| S777 ' --
   corpus/SOURCES.md` piped to `wc -l` → 0), and S777 is one of the 76 absent ids. Entry `era-periodization-models.amend-2026-10-23b.md` writes "the
   standard's registry record (S718)" and "round 1's S719"; base S718 is Farran et al. on infant-directed speech
   (`PLOS ONE` 11(3):e0151518) and base S719 is Cristia 2013 on the same topic. Both entries must drop or re-point
   these before landing, or they cite another document's row.
5. **Live and capture carriers drift in bytes and in unrelated text, never in the quoted span.** Archives page:
   311308 B live vs 307700 B captured, differing in form labels and one agency name
   (日本政策金融公庫 / 株式会社日本政策金融公庫); the table region from the first `元号名称` onward is 1684 folded
   characters and character-identical in both, and the quoted span occurs once in each. Registry page: 24144 B live
   vs 24174 B captured, visible text identical. No byte count here is canonical; each window carries its own.
6. **The archive host is flaky, not closed.** Two of three `web.archive.org` attempts ended before any HTTP
   response — `curl: (7) Failed to connect to web.archive.org:443`, exit 7 — and the third returned `HTTP/1.1 200`
   with 307700 B (S935). A capture-based row records its own attempt; a counter that fetches must retry, and a TCP
   failure is not a wall.
7. **No access control was met on any URL above.** No 403/429/503, no captcha (altcha, hCaptcha, reCAPTCHA), no
   `Just a moment...` interstitial, no login wall, no paywall, no geo block: every recorded response is the
   document itself. The refusals in this Gate are structural (route identity), not adversarial.

Rejections — each names one re-openable artifact, states what it found there, and binds the UA to the response
(QUALITY 22/27):

| reason | flip | probed URL (response bound to the UA above) | verdict |
|---|---|---|---|
| the `showGb?type=download` route is not a document: `HTTP/1.1 302` → `newGbInfo?hcno=…&refer=outter` → `200`, 7334 B on the wire, 24144 B stored, sha256 `80b4c781…`, byte-identical to the `type=online` body, no `Content-Disposition`, body is the record page. A row opened on it would cite the record twice and the clause text never. Receipt: `fetch-receipts.md` route-test table, second row; body: `fetch/S938-route-test-showGb-type-download.html` | the clause text is cited from the declared tier-C reproduction (S895) and identity/custodianship from S896, each declared for what it is; no row claims the standard's normative wording | `https://openstd.samr.gov.cn/bzgk/std/showGb?type=download&hcno=E107EA4DE9725EDF819F33C60A44B296` — 302 then 200 | refused as a clause-text carrier |
| staged S938 is not a second document: its `showGb?type=online` URL answers `302` with `Location: …/newGbInfo?hcno=…&refer=outter`, the S932 capture archives exactly that target, and the two visible texts are identical (757 chars, `diff` prints nothing). Receipt: `windows/S896-live.txt` header chain and `windows/S896-capture.txt` | one row (S896) carries both carriers; the id planned for the second row opens no row | `https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296` — 302 → 200 | refused as a second row (Gate note 1) |

## Quarantine

**The standing slice, re-derived, not re-fetched.** `awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~
/round[0-9]+/ && $4 ~ /S[0-9]+/' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
→ **21 lines**, every one carrying an S-id (18 `payload-absent` + 3 unreachable-class). The three
unreachable-class ids print with a trailing backtick (`S807\``, `S812\``, `S835\``) because that register cell has
no leading space before the class text; a whitespace-trimming parser keeps the backtick. The count is unaffected.

**Two of those 21 name this round's two A-tier documents, and both were graded `payload-absent` for a reason
about the quote, not about the page.**

- register line 118 (`round1`, S776) — openstd `newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296`, quote
  ``标准号：GB/T 33661-2017 … 标准状态：现行 … 发布日期 2017-05-12 … 实施日期 2017-09-01 … 主管部门 中国科学院``.
  Measured over the page's folded text: that span occurs **0** times, because it joins six non-adjacent fields
  with `…`; each of its fragments occurs — `标准号：GB/T 33661-2017` 1, `标准状态：` 1, `发布日期` 1, `2017-05-12` 1,
  `实施日期` 1, `2017-09-01` 1, `主管部门` 1, `中国科学院` 2.
- register line 134 (`round5`, S825) — `https://www.digital.archives.go.jp/search`, quote
  ``元号名称 開始西暦年 令和 2019 平成 1989 昭和 1926 大正 1912 明治 1868`` plus a second line `元号名称／開始西暦年`.
  Measured: **0** occurrences in the live page and **0** in the capture, because the table's cells read
  `令和 2019 選択 平成 1989 選択 …` — the span leaves out the 選択 cells that sit between every pair.

So both verdicts **stand exactly as filed** — the span is in none of the artifacts, which is what the register
asserts — and both documents are nevertheless openable and are quoted at this Gate with spans that do occur, once
each. The register is neither edited nor reversed: the documents are re-opened as new rows, which is clearing
condition 2. The register's id column is not the lane's: base S776 is a mancala paper (Pearson, *Expedition*
58(1)) and base S825 is an Axon paper (Gregis), so the bridge from a register row to a lane row is by document
only.

**Which of the 21 this round touches.** By id, none: the slice spans S776…S835 (`awk … {print $4}` over the
register, 21 ids) and every row this round would open is numbered S89x. By document, exactly the two rows above:
register S776 ↔ the openstd record ↔ S896, and register S825 ↔ the archives search page ↔ S894. The other 19 rows
are untouched, and no verdict — PRESENT, REFUSED or UNVERIFIABLE — is upgraded, retired or re-opened here.

The four clearing conditions that govern any future adoption touching these rows: (1) a refused register row
stays refused and is never edited in place; (2) a document is re-opened as a *new* row, never as a reversal of
the register verdict; (3) the quote is located on the page in the round that adopts it, from that round's capture;
(4) the admitted bytes are that round's entry, not the staged text.

**Class size, measured over the 21:** **7** quote cells contain `…` (`grep -c '…'` over the extracted cell) and
**5** contain `<br>`. An ellipsis-joined quote can never match a page by substring, so for a third of its
kotodama rows the register's absence test cannot fail. That is a campaign-instrument fact, recorded for the
campaign; it is not this lane's write to make.

## Collision guard (item 10)

**The guard as CORPUS item 10 specifies.** Extractor `^ {0,3}\|[[:space:]]*S[0-9]{3,}` over the lane registry and
the staged package, ids normalised, then intersected. Artifacts under `.ufo/waves/round-76/assimilation/`:

| artifact | lines | range | sha256 |
|---|---|---|---|
| `reg-ids` | 817 | S001…S893, with 76 ids absent from that span | `97eef07a8584…` |
| `staged-ids` | 132 | S859…S990 | `bab11d7d0ee0…` |
| `collisions` | 35 | S859…S893 | `be203dd8b02c…` |

Re-derived by this seat: `grep -cE '^S89[4-8]$'` over `reg-ids` → `0`, over `staged-ids` → `5`, over `collisions`
→ `0`; the headline count is `wc -l collisions` → **35**, and every one of the 35 is a staged id that is also a
lane id (S859..S893), i.e. namespace drift, not duplicate registration. **The planned adoption adds five more of
the same kind** (Gate note 2), which the intersection cannot show because the registry does not hold them yet.

**Old → new, by document** (join key: normalised URL — host lowercased without `www.`, percent-escapes decoded,
`web.archive.org` wrapper and `id_`/`if_` suffixes stripped, and a `showGb` route resolved through its 302 to the
`newGbInfo` URL it redirects to):

| staged campaign id(s) | document | row this draft opens |
|---|---|---|
| S908 (live) + S935 (capture of the same page) | digital.archives.go.jp/search | **S894**, one row, two carriers |
| S916 | xingzuobaike.com/huangli/wannianli/d165803.html | **S895** |
| S932 (capture) + S938 (live, 302 to the captured URL) | openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 | **S896**, one row, two carriers |
| S937 | news.gmw.cn/2017-05/23/content_24559485.htm | **S898** |
| S919 (cited in entry a's folded round-7 passage) | iris.unipa.it retrieve … 2014 marrone age dor---2.pdf | **lane S892**, already held |
| S921 (same passage) | persee.fr per-page transcription `comm_…_1113` page 6 | **lane S885**, already held |
| S718, S719 (cited in entry d) | — | **no lane row**: those numbers are other documents (Gate note 4) |
| S777 (cited in entry a) | — | **no row in any commit** (Gate note 4) |

The substitution must be one **simultaneous** pass over a single lookup table: staged ids S885–S893 are lane ids
as well, and S894–S898 are staged ids for other documents, so any sequential per-id replacement re-maps an
already-mapped id. `S919 → S892` and `S921 → S885` are by-document rewrites, never arithmetic neighbours.

**Guard proof.** `find …/assimilation/guard-proof -type f` returns exactly five files: three registries
(`planted-1space-registry.md`, `planted-4space-registry.md`, `col0-registry.md`) and two expected collision files
(`planted-1space.collisions` 5 B, `planted-4space.collisions` 0 B) — no `proof.txt` and no run script among them.
This seat therefore re-ran both extractors over every fixture, with the outputs recorded in `measurements.txt`:

| fixture | 0–3-space extractor | column-zero-only control | matches the expected file |
|---|---|---|---|
| `planted-1space-registry.md` | 2 ids (S001, S859) | 1 id (S001) — blind to the plant | yes: `planted-1space.collisions` reads `S859` |
| `planted-4space-registry.md` | 1 id (S001) — plant correctly not seen (4-space = code indent) | 1 id (S001) | yes: `planted-4space.collisions` is empty |
| `col0-registry.md` | 2 ids (S001, S859) | 2 ids | both extractors see a column-zero row |

## Normalization

**Recheck prose stripped, per row.** The four staged entries carry prose in their `recheck:` lines (one of them
twice); each landed row's cell is `180d` and nothing else:

| entry | staged line it replaces | cell |
|---|---|---|
| `calendar-festival-systems.amend-2026-10-24.md:8` | `recheck: 180d — re-run the three row recheck commands in round 9's SOURCES-PROPOSED.md (S937 -> 1, S935 -> 1, S932 -> 1) (ran 2026-10-24)` | `180d` |
| `calendar-festival-systems.amend-2026-10-24.md:62` (the folded round-7 passage) | `recheck: 180d — re-run the two row recheck commands in round 7's … (S919 -> 1, S921 -> 1) (ran 2026-10-24)` | `180d` |
| `calendar-festival-systems.amend-2026-10-24-r10.md:6` | `recheck: 180d — re-run the row recheck command in round 10's … (S938 -> 1) (ran 2026-10-24)` | `180d` |
| `era-periodization-models.amend-2026-10-23b.md:6` | `recheck: 180d — re-run the row recheck command in round 5's … (S908 -> 3) (ran 2026-10-23)` | `180d` |
| `calendar-festival-systems.amend-2026-10-23c.md:6` | `recheck: 180d — re-run the row recheck command in round 6's … (S916 -> 1) (ran 2026-10-23)` | `180d` |

No recheck count (`S937 -> 1`, `S908 -> 3`, `S938 -> 1`) enters a cell: a cell that asserts a count its own span
fails is worse than a cadence, and this seat re-ran none of those staged counts — no command in
`measurements.txt` re-derives them.

**`source:` lines re-pointed by document, never by number.** The four admitted entries' `source:` ids are all
campaign ids (S908, S916, S932, S935, S937, S938) and every one is rewritten to its lane id in the same pass as
the rows are written; the folded round-7 passage inside entry a adds `source: S919` and `source: S921`, which
become lane S892 and lane S885 by document. The mapping table above is the whole of it.

**Two normalization hazards the landing must not carry.**

1. Entry a keeps a whole superseded entry under a `## Superseded passage` heading, complete with its own
   `source:` lines, its own `verified-at:` and its own `recheck:` line. Landing the file whole would append the
   round-7 text *and* its two campaign ids to the lane. Strip the block or re-point both ids; a "kept as the dated
   record" paragraph is not a row.
2. Rows are 11 cells and no cell may carry a pipe. That check is a landing leg, not a wave-1 one:
   `<<FILL: awk -F'|' NF over the four landed rows, and grep -cE '^\| *S89[0-9] .*\\\|' → 0>>`.

## Census

**Before** — `reports/round-76/telemetry/census-start.txt`, produced by
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`;
34 lines, 28 `W04` duplicate-URL warnings, 4 `W01` tier-C lines (S881, S882, S884, S893), then:

```
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=0
```

**After** — `<<FILL: the round-end run of the same command with its exit code, pasted by the L1 at landing>>`.
Rows **817 → 817+k**, `k` = the number of distinct documents the admitted entries cite that the registry did not
hold; measured 2026-10-27 that is **4** documents (`<<FILL: the landed row count>>`), not 5, because two of the
five planned URLs are one document. The `W04` lines should be unchanged (none of the four documents duplicates a
held URL); a new `W01` line is expected only for S895, the tier-C reproduction, and that line is the census saying
out loud what the Gate says: the tier-C row must never be an entry's sole support.

## Mistakes

`<<FILL: R76-M1 — the L1 supplies the round's mined mistake at wave 2: class, evidence pointer, captured-by, fix,
state. A fix counts only once it has been shown able to fail.>>`

Pointers already routed into this round — **not re-derived, not re-scored here**:

- **R75-M2 (receipts bind the title, not the anchor).** The fix this round uses: every window's `anchor:` is the
  row's own Gate quote and the header carries `anchor-hits-in-window: 1`; the landed
  `reports/round-76/evidence/S89x.txt` must keep that binding rather than bind a page title.
- **R74-M5 (register adjacency guard).** Still open, and **this round does not exercise it**: the Quarantine defect
  is same-row (a register row's quote cannot match the page its own URL names), not the adjacent-row mispairing
  R74-M5 describes, so the guard that pairs a register row's URL with its quote remains untested here.

## Routed to round 77

1. **The claim's Before leg is false at base** (`## What the base holds`): restrict both greps to
   `corpus/knowledge`, or drop the sentence. `corpus/**` matches two lessons. The freeze should carry the
   corrected command, because the leg as written fails against the base it names.
2. **The planned ids collide with five staged documents** (Gate note 2). Renumber above both namespaces (highest
   staged id S990) or carry the by-document map; state which at the freeze. Otherwise the next round's collision
   list shows five pairs whose two sides are different documents.
3. **Entry `-r10`'s `24148` / md5 `9791d9dc…`** (Gate note 3): re-measure and re-stamp, or delete both numbers.
   Receipt: `w1/stage/ScribeLesson-7/fetch-receipts.md`, route-test table.
4. **Dangling S777 and mis-resolving S718/S719** (Gate note 4) — the entry owners re-point or drop before the
   freeze; the lane's registry cannot be edited to make them true.
5. **Archive flakiness** (Gate note 6): a capture step retries and records its own exit code; a TCP failure is
   not a wall and must not grade as one.
6. **The ellipsis-quote class in the register** (Quarantine, 7 of 21, plus 5 with `<br>`): a substring absence
   test cannot grade a quote that joins non-adjacent fields. Campaign instrument, not a lane edit.
7. **Round-75's open items stay pointers:** the six path-present files and their byte-level decision, the S877
   scope-cell supersede row, and R74-M3/M4/M6/M7/M8 with closure R1/R3/R4. The R75 evidence-window rule (window
   by the page the anchor names, not by the head) is exercised here: each window is built around its anchor's
   position, and each records `before:`.
8. **`considerthese/` is absent for this lane** (`ls /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese`
   → no such file, exit 2), so no proposal is mined this round and no ledger row is added on that account.

## Sources & frontier

- **Rows: 817 → 817+k** `<<FILL: landed count>>`; one row per document, `mined`, `opened 2026-10-27`,
  `recheck 180d`. Tiers verified against the documents, not taken from a report: **A ×3** — S894 the archive's
  own search table, S896 the registry's own record, S898 the state press's report; **C ×1** — S895, a declared
  third-party reproduction, which no entry may rest on alone. `<<FILL: the landed tier column>>`
- **Knowledge files: 252 → 252+n** `<<FILL: landed count and the four candidate paths' disposition>>`; the four
  staged candidates are `culture-material/calendar-festival-systems.amend-2026-10-24.md` (7571 B, sha256
  `62645c56…`), `…-2026-10-24-r10.md` (3385 B, `b924113e…`), `…era-periodization-models.amend-2026-10-23b.md`
  (1983 B, `2a855e35…`) and `…calendar-festival-systems.amend-2026-10-23c.md` (2406 B, `a9bd29d9…`), measured in
  the read-only package. All four candidate paths are **absent** at base (`git -C … cat-file -e
  98c486b…:corpus/knowledge/<path>` → `absent` for each of the four), while both parent entries exist
  (`culture-material/calendar-festival-systems.md`, `culture-material/era-periodization-models.md`), so each landed
  amendment is a new file and counts toward `n`; `n <= 4`.
- **Frontier ground entered:** what a promulgated calendar standard actually requires as its drafter and its
  registry state it (the 编排规则, the calculation model and the one-second precision, the 颁行 requirements); the
  registry record as an identity-and-custody instrument (标准号, 状态, 发布日期, 实施日期, 主管部门, 发布单位); an
  archive's era-name table as the dating instrument an institution actually searches by (令和 2019 back to 明治
  1868 and beyond); and the state press's own report of the promulgation. None of it was held in
  `corpus/knowledge` at base (`## What the base holds`).
- **Declared after-state, from the claims, restated as the target this draft is measured against:** Gate carries
  >= 1 admit and >= 1 reject from the assimilation set (this draft: 4 admits, 2 rejects); no tier-C row is the
  sole support of an admitted entry; every Gate quote sits inside a committed evidence window (`anchors.txt`
  checks the wave-1 windows: hits = 1 for each of the four anchors, `carrier-only` for the two capture windows);
  census exit 0 at start and `<<FILL: at landing>>`.
