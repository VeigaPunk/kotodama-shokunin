# Seat ScribeEntryAmend — amendment draft for `worldbuilding-setting-practice`

Round 74 (hyaku run 7), wave 1, kotodama lane at base `f7104cbce186bc2e1522abf0cfd619cc834628bb`.
Role: scribe (leaf). No delegation, no background jobs, no `task` spawns, no mutations.

## 1. Deliverable

- Draft: `.ufo/waves/round-74/drafts/worldbuilding-setting-practice.amend-2026-10-23.md`
  — 87 lines, 1,989 words (`wc -w`), sha256 `bb5504e21a2a29583841df18ab3eee4c8a9fb7d21b6f38a642e01d2d80d8673e`.
- Built from the staged `merge/kotodama/knowledge/corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`, rebuilt on text I opened myself; it cites only the tentative lane ids S883 (chinawriter 2025 interview) and S884 (chinawriter 2022 reprint), one per cited line.
- The staged file's **second half** (the `# Amendment — world-view design analysed, not just advised` block citing staged S895, chinawriter 2025/1030) is **not carried**: S895 is outside claim C's four-row set, so shipping it would make the entry cite an id that resolves to no admitted lane row (claim C kill rule). It is a separate staged amendment for a later round.
- Writes outside this draft and this report: none. The parent directory `.ufo/waves/round-74/drafts/` did not exist and was created. The six inherited uncommitted round-73 w2 files were not touched; no git state, index, fleet path, sibling lane or shokuknow byte was written.

## 2. Fetch log (fetch hygiene 21/22/24)

Both pages opened by a plain `curl` request under **exactly** this User-Agent (the browser-shaped one):

```
UA = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
automation: none
```

| URL | response | bytes | sha256 |
|---|---|---|---|
| `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | HTTP 200, no wall | 48,536 | `a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d` |
| `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | HTTP 200, no wall | 62,604 | `344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659` |

Files: `/tmp/ScribeEntryAmend/page-40494534.html`, `/tmp/ScribeEntryAmend/page-32582252.html`. Both UTF-8 (`charset=UTF-8` in the document head), article body in `<p style="text-indent: 2em;…">` elements; nav/footer excluded from every quote source.

Scratch-directory note: `/tmp/ScribeEntryAmend/` already held `S878-*`, `S879-*`, `S880-*`, `rc878.pdf`, `rc880.pdf` from 19:08–19:10 that same day, left by an earlier seat (round-73 conlang rows). They are not mine, I did not read or use them, and no quote or count in this report or in the draft rests on them.

Carrier probe (QUALITY 21/24; positive control in the same query shape):

| probed URL | result |
|---|---|
| `https://web.archive.org/cdx/search/cdx?url=https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html&output=json&filter=statuscode:200&limit=5` | HTTP 200; three status-200 captures `20250610015519`, `20250611013901`, `20250813004013` |
| `https://web.archive.org/cdx/search/cdx?url=https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html&output=json&filter=statuscode:200&limit=5` | HTTP 200; one status-200 capture `20221207080111` |
| `https://web.archive.org/cdx/search/cdx?url=http://example.com/&output=json&filter=statuscode:200&limit=5` (positive control) | HTTP 200; 2002 captures returned (control not empty) |
| same three queries over `http://web.archive.org/…` (port 80) | `curl: (7) Failed to connect … after N ms` for all three (host blocks port 80; the control fails identically, so this is not an absence finding) |

Capture bodies fetched and tested against every span the draft quotes:

| capture URL | response | bytes | sha256 | spans found |
|---|---|---|---|---|
| `https://web.archive.org/web/20250813004013id_/http://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | HTTP 302 → followed to `…/20250611013901id_/…` → HTTP 200 | 48,536 | `a3b6640c…` (identical to the live fetch) | 20/20 |
| `https://web.archive.org/web/20221207080111id_/http://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | HTTP 200 | 62,623 | `a0b48f21c9ebc41686da8a73ef315041e387cdb647b464e1a9d23247fd3107d6` | 17/17 |

The 2022 capture is 19 bytes larger than the live page but paragraph-identical: both yield 69 body paragraphs and zero differing indices under the extraction rule below, so the draft's ¶ numbers hold on both carriers.

## 3. Re-test of the rounds-68/71 refusal (blocker hand-check)

The register's refused spans are `payload-absent` for these two URLs (`absent-defect-register.md` rows S816/S817). Direct tests against the two live bodies, character for character:

| span named by the register | on the 2025 page | on the 2022 page |
|---|---|---|
| `这个我肯定考虑过。我自己就是资深读者` (register S816, filed against the **2025** URL) | **absent** | **present** (¶34) |
| `Sowers-Wills's 'Phonology from the inside out…'` (register S817, filed against the 2022 URL) | absent | absent |
| `非凡特性来自最初造物主` — staged row S899's own anchor text | present (¶67) | absent |
| `20章之内慢慢来` — staged row S900's own recheck grep | absent | present (¶34) |

So the refusal class is reproduced exactly as a **URL↔quote mispairing, not a dead payload**: register S816's span belongs to the other page and register S817's span belongs to neither page (it is the conlang citation named in the round-72/73 lessons). Both staged rows' own recheck cells are green today — `grep -c '先做的是世界观' <2025 page>` = 1 and `grep -c '20章之内慢慢来' <2022 page>` = 1. Both pages carry the material this amendment uses.

## 4. What the draft records, and where it stands on the staged text

Sections and their single-row support:

- **§1 Whose words these are** (S883, S884): the headline in `<title>`/`em#newstit` is the outlet's compression (`我先设定世界观，再考虑怎么升级`) of the author's body sentence at ¶67; 谭天's praise (¶7, S883) and 李玮's statements of the received practice and of a competing prescription (¶31, ¶33, S884) are interviewers' words, quoted and marked as such, never as evidence. Everything else quoted is the author's own answer. Status line: `contested`, reason on the page.
- **§2 Build order** (S883): world-view → progression → its expression, at ¶67; iterative and pruned at ¶68; a mechanic rejected when it conflicts with the already-fixed method at ¶65; the expression fitted to tone at ¶67. **New corroboration not present in the staged draft**: the 2022 interview states the same order independently — `首先想的是，我的背景设定既然已经明确了` (¶50), `然后根据塔罗牌做一个力量体系设定` (¶50).
- **§3 Derivation rule** (S883): origin premise ¶67 → stated inference ¶67 → required material manifestation ¶67 → derived laws ¶67 → mechanics chosen to fit the laws ¶67; the same shape top-down from a chosen register in the tarot instance at ¶60; the realism ladder graded by rank at ¶61. One formulation is labelled as the entry's own reading, not the author's.
- **§4 Delivery schedule** (S884): the dump failure ¶34, the continued-dump failure ¶34, the concealment failure ¶34; the condition (`如果开头足够有趣，有钩子，有悬念` ¶34) preceding the release (`那么你把整个世界观和设定逐渐地抛入` ¶34) and its window (`把它放在前面大概20章之内慢慢来` ¶34), with the author's own 大概 and his closing `我觉得是问题不大的。` (¶34) preserved so the figure cannot be read as a threshold; the implementation on his own book at ¶32; the reason and the tolerance claim at ¶34.
- **§5 What to do with it**: two id-free tables (build-order gate list; three-question delivery test, third question labelled as the entry's extension) plus a hypothetical, canon-free worked example. No table row carries an S-id (QUALITY 15).
- **§6 Does not establish / handoff**: no reader measurement, S884 recorded as a lead, no boundary at twenty, no second author compared; handoff to `synthesis/worldbible-integration-contract.md`; no canon decided.

Changes made against the staged text, and why:

| staged text | draft | reason |
|---|---|---|
| `gap filled` cites lane ids S754, S742, S743 | rewritten from the base-revision gap sweep, no ids | those ids are another round's rows; a cited line may carry only S883/S884 here, and the check («0 worldbuilding files, 0 CJK-term files, 0 host rows at a 804-row base registry») is the re-runnable ground |
| `couples:` names `myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` | `synthesis/worldbible-integration-contract.md` | no `narrative-structure-frameworks` file exists at base (`git cat-file -e` = absent) and the family is listed as refused in claim C; coupling to a path that never lands would dangle |
| `sources: … paired so that neither is the sole support` | S884's schedule recorded as a **lead**, S883's build order as the tier-B support; the one overlap (¶50) named | the 2025 tier-B interview does not carry the delivery schedule, so the pairing is not a support relation for it; QUALITY 5 bars a tier-C row as sole support of an admitted claim |
| second half (staged S895) carried as "superseded passage" | dropped from the draft | S895 is outside claim C's four rows; the entry would cite an id resolving to no admitted lane row |
| `verified-at: 2026-10-23` with `recheck … round 4's SOURCES-PROPOSED.md` | `verified-at: 2026-10-25`, carrier-based recheck | the staged cells predate this round's opening; the recheck now names the two captures and the paragraph rule a re-opener needs |

## 5. Checks I exercised on the draft (and what I did not run)

Exercised, with output:

1. **Span/locator/id check (my own script, /tmp/ScribeEntryAmend)** — extracts every 「…」 span with its line's single S-id, counts occurrences on that page, and finds the paragraph index: **37 spans, 0 problems**. Every span is 10–35 characters, 1 whitespace token under `wc -w`, unique on its page (one exception, documented), and lands in the ¶ the line names. The exception is the headline span, which occurs twice (in `<title>` and `em#newstit`) and in no body paragraph; the line that quotes it says exactly that.
2. **`python3 -B tools/check-cited-lines.py .ufo/waves/round-74/drafts/worldbuilding-setting-practice.amend-2026-10-23.md`** → `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0 (no MULTI-ID, no TABLE-ID).
3. **Length against the ENTRIES leg** — draft 1,989 words; smallest `corpus/knowledge` file at base by `git show <base>:<path> | wc -w` is `culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` at 478 words.
4. **Base-revision ground re-derived** — `git ls-tree -r --name-only <base> corpus/knowledge | grep -ciE 'worldbuilding|setting'` = 0; `git show <base>:corpus/SOURCES.md | grep -c chinawriter` = 0; registry rows = 804.
5. **Couple-path existence** — `git cat-file -e <base>:corpus/knowledge/synthesis/worldbible-integration-contract.md` present; `<base>:corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` and `<base>:corpus/knowledge/culture-material/worldbuilding-setting-practice.md` absent at base (the second is the entry this amendment lands with).

Not run, and not claimed: any round acceptance counter (`reports/round-74/accept-c.py` does not exist yet), the census, the Gate-record check, any evidence-file check, and anything on the graded tree. No tool was installed.

## 6. Open items for the Gate, the base-entry seat and the counter authors

1. **Header field order.** The draft follows claim C's ENTRIES leg literally — `source`, `verified-at`, `recheck`, `ground`, `topic`, `gap filled`, `sources`, `couples`, `scope` — then a `refuses:` line. Note that the landed `heritage-taxonomy-models.md` puts `ground` **before** `recheck`; if the counter parses a fixed order, it should accept the claim's order (the claim is the frozen contract) or the claim should be corrected before freeze. Flagging, not deciding.
2. **S884's tier.** The draft states tier B for S883 and tier C for S884 (the staged tiers) and therefore frames the delivery schedule as a recorded lead. If the Gate re-files S884 as B with a claim-scoped reason, the framing still stands; if it files it C, no sentence in the draft needs to change.
3. **Row anchors must use a body span, not the headline.** For S883 the anchor should be a ¶67 span (e.g. `我先做的是世界观，再考虑怎么升级，再考虑升级的表现。`); the headline is an editor's compression and sits outside every body `<p>`.
4. **Evidence windows.** The Gate's `reports/round-74/evidence/S883.txt` / `S884.txt` must store the body window around the quote it records, and the counter checks the Gate quote occurs inside that window. All 37 spans the entry quotes are present in the two capture files named in §2 (20 from S883, 17 from S884, none missing), so any of them is available to the evidence records.
5. **The `(loc: ¶N)` convention has no precedent** — `grep -rn "(loc:" corpus/knowledge | wc -l` = 0. I introduced it as the seat brief requires, and pinned the numbering rule inside the entry's `recheck:` line so a re-opener reproduces the same numbers: body `<p style="text-indent: 2em;…">` elements in document order, centred section headings included, 92 paragraphs on the 2025 page and 69 on the 2022 page, empty ones dropped.
6. **Landing order.** The draft's `couples:` names `culture-material/worldbuilding-setting-practice.md`, which lands only with the sibling base entry; both entries and rows S881–S884 are one claim's lands, so they must land in the same commit for the coupling to resolve.

## Appendix — the 37 quoted spans as checked

Columns: #, row, paragraph on that page (`headline` = outside every body `<p>`, documented in the line), span, characters, whitespace tokens (`wc -w`).

| # | row | ¶ | span | chars | tokens |
|---|---|---|---|---|---|
| 1 | S883 | ¶67 | 我先做的是世界观，再考虑怎么升级，再考虑升级的表现。 | 26 | 1 |
| 2 | S884 | ¶34 | 把它放在前面大概20章之内慢慢来 | 16 | 1 |
| 3 | S883 | headline | 我先设定世界观，再考虑怎么升级 | 15 | 1 |
| 4 | S883 | ¶67 | 我先做的是世界观，再考虑怎么升级，再考虑升级的表现。 | 26 | 1 |
| 5 | S883 | ¶7 | 作为一位“理工男”网文作家，您最擅长构建缜密恢宏的世界观 | 28 | 1 |
| 6 | S884 | ¶31 | 很多网文在第一、二章就会基本上给出一个很明确的世界观 | 26 | 1 |
| 7 | S884 | ¶33 | 有的网文作者会认为网络文学一开始就应该让大家明确世界观 | 27 | 1 |
| 8 | S883 | ¶67 | 我先做的是世界观，再考虑怎么升级，再考虑升级的表现。 | 26 | 1 |
| 9 | S883 | ¶68 | 一开始其实不是所有设定都想好了。 | 16 | 1 |
| 10 | S883 | ¶68 | 是通过一次次的尝试、推导确定下来的。 | 18 | 1 |
| 11 | S883 | ¶68 | 最后找到一条合适的路径，那就是唯一的答案。 | 21 | 1 |
| 12 | S883 | ¶65 | 既然有了扮演法，那么晋升的过程就不能采用吸收灵气、冥想这种传统的方式。 | 35 | 1 |
| 13 | S883 | ¶67 | 服食魔药和扮演法是符合世界观调性的升级方式 | 21 | 1 |
| 14 | S884 | ¶50 | 首先想的是，我的背景设定既然已经明确了 | 19 | 1 |
| 15 | S884 | ¶50 | 然后根据塔罗牌做一个力量体系设定 | 16 | 1 |
| 16 | S883 | ¶67 | 万事万物都从最初造物主而来 | 13 | 1 |
| 17 | S883 | ¶67 | “所有的非凡力量也从他而来”是个合理的推论 | 21 | 1 |
| 18 | S883 | ¶67 | 这个推论要有物质性的表现 | 12 | 1 |
| 19 | S883 | ¶67 | 并推导出一系列非凡特性定律 | 13 | 1 |
| 20 | S883 | ¶67 | 有了这些定律，我就觉得，服食魔药和扮演法是符合世界观调性的升级方式。 | 34 | 1 |
| 21 | S883 | ¶60 | 我先把22张大牌拿来，看哪些可以用，哪些需要修改。 | 25 | 1 |
| 22 | S883 | ¶60 | 然后从上往下推导出整个序列途径。 | 16 | 1 |
| 23 | S883 | ¶61 | 越贴近现实就越有代入感 | 11 | 1 |
| 24 | S883 | ¶61 | 等级很高以后，再用现实职业会很违和 | 17 | 1 |
| 25 | S883 | ¶61 | 贴近现实、来源于现实、又能在现实中展现出神秘学魅力 | 25 | 1 |
| 26 | S884 | ¶34 | 它的第一章就是抛设定，把世界观、整个修炼体系抛给你。 | 26 | 1 |
| 27 | S884 | ¶34 | 但如果一开始前面两三章都是设定，那我大概是不会看下去了 | 27 | 1 |
| 28 | S884 | ¶34 | 很多一开始设定不明确的小说我也是看不下去的 | 21 | 1 |
| 29 | S884 | ¶34 | 如果开头足够有趣，有钩子，有悬念 | 16 | 1 |
| 30 | S884 | ¶34 | 那么你把整个世界观和设定逐渐地抛入 | 17 | 1 |
| 31 | S884 | ¶34 | 把它放在前面大概20章之内慢慢来 | 16 | 1 |
| 32 | S884 | ¶34 | 我觉得是问题不大的。 | 10 | 1 |
| 33 | S884 | ¶32 | 用悬念作钩子吸引人读下去 | 12 | 1 |
| 34 | S884 | ¶32 | 然后在整个故事的推进中一点点地把设定给抛出来 | 22 | 1 |
| 35 | S884 | ¶32 | 如果我一开始就把这个设定给你们，肯定是比现在这个版本更不友好 | 30 | 1 |
| 36 | S884 | ¶34 | 我对不同的小说有不同的容忍度 | 14 | 1 |
| 37 | S884 | ¶34 | 我觉得是问题不大的。 | 10 | 1 |

Staged-anchor note: staged row S899's own anchor text names 「非凡特性来自最初造物主」, and that string is on the 2025 page at ¶67 (`非凡特性来自最初造物主`, one occurrence) — so the staged row's anchor was present even though the register's refused span was not. The draft quotes the page's characters.

Tools installed: none. Tested with `git` (read-only), `curl`, `python3` stdlib, `wc`, `sha256sum`.

## Post-wave update — L1 re-check (round 74 follow-up, same seat)

L1 instruction: re-check the amend draft against `.ufo/waves/round-74/w1/RevEntryQuality.md`, `ScoutChinawriter2022.md` finding 3 and the scouts' attribution findings; cite only lane ids S883/S884; no S895 and no folded `Superseded passage`; header `source:`/`verified-at:`/`recheck:` first; body ≥ 478 words; one S-id per cited line; no table row carrying an id; word the delivery schedule as ONE practitioner's stated tolerance, a lead, never a rule; byline/publication chain exactly as printed; paste the lint output. Lints pasted below; nothing else was written.

### What I changed in the draft

1. **Sole-support and the false pairing** (`ScoutChinawriter2022.md` finding 3; `RevEntryQuality.md` HIGH-2). The `sources:` line no longer implies the two rows cover each other: it now records that §4 rests on the tier-C row **alone** and is therefore written as one practitioner's stated tolerance, a lead, never the entry's rule. §4's heading is now "One practitioner's stated tolerance, on a single tier-C row"; its opening sentence states the tier-C limit; its closing sentence records that the bound is his tolerance and not his book's schedule — the interviewer notes 《诡秘之主》 readers understand the setting only 「到几十章后」 (para 32).
2. **Locator scheme — the earlier draft's numbers were one below the Gate's.** The earlier draft numbered paragraphs by the `<p style="text-indent: 2em;…">` subset, which excludes the lead image and one non-indented paragraph, so every locator sat one under the scouts' and the L1's numbering. Every locator is now in the Gate's scheme: **P68** for the build-order sentence (L1's "P68 under 确定风格、设定世界、推导故事") and **para 35** for the delivery sentence (L1's "para 35"). The `recheck:` line now defines both schemes and gives the 2em cross-check, so a re-opener needs no inference. **The ¶ numbers in §4 and the appendix of this report are the superseded scheme — add 1 (2025 page) and 1 (2022 page) to get the current locator** (measured: div-ordinal and all-`<p>` ordinal are each exactly the 2em ordinal + 1 for all 33 spans).
3. **Gate quotes now verbatim as specified.** S883 「整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。」 at P68 under 确定风格、设定世界、推导故事 (32 chars); S884 「把它放在前面大概20章之内慢慢来，我觉得是问题不大的。」 at para 35 (27 chars). The earlier draft quoted a shorter fragment of the S883 sentence and split the S884 sentence; both are now the whole specified span.
4. **Attribution exactly as printed** (`ScoutChinawriter2025.md` §4; `ScoutChinawriter2022.md` §2), re-read in my own fetches:

| element | printed on the page | earlier draft said | now |
|---|---|---|---|
| 2025 byline | `来源：文汇报　\|　邵燕君 谭天 项蕾　　2025年06月10日09:01` | `网络文学“破壁者”访谈 (邵燕君、谭天、项蕾), 来源：文汇报, … 2025-06-10` | byline quoted as printed, with breadcrumb 网络文学>>访谈 and the URL path date 0605 ≠ printed 06-10 |
| interviewers | credits P3–P6: 邵燕君（北京大学中文系教授）, 谭天（北京大学中文系博士生）, 项蕾（中国社会科学院文学研究所助理研究员） | "three named academic interviewers" | roles as printed; the correction names the doctoral student and the non-university affiliation |
| volume | 编者按 P2: 将收入《创作者说：网络文学代表性作家访谈录》(北京大学出版社) | "will be collected in an interview volume (¶1)" | 将收入 = forthcoming, at P2 |
| 2022 byline | `来源：《青春》　\|　李玮 爱潜水的乌贼　　2022年12月07日10:07`; 责编 虞婧 | "a magazine interview reprinted by an industry outlet" | byline and 责编 as printed; no characterisation the page does not print, no issue number, no interviewer affiliation |

5. **Header shape.** The earlier draft's extra `refuses:` field is folded into `scope:` so the header carries exactly the nine documented fields in order.

### Lint results (read-only, run 2026-10-25)

```
$ python3 -B tools/check-cited-lines.py .ufo/waves/round-74/drafts/worldbuilding-setting-practice.amend-2026-10-23.md
CITED-LINES: 0 finding(s) in 1 file(s)
exit 0

$ python3 -B tools/check-draft-ids.py .ufo/waves/round-74/drafts/worldbuilding-setting-practice.amend-2026-10-23.md
DRAFT_IDS: 0 findings
exit 0
```

### Verification exercised

- **33 located quoted spans** checked against my own fetches in the paragraph each locator names: **0 failures**. One further span is headline-only and labelled as such (the `<title>`/`#newstit` string, which has no P-number by construction).
- Both Gate quotes are substrings of their paragraph; the longest quoted span is 37 characters (limit 80); every CJK span counts 1 whitespace token.
- Structure: header fields in order `source, source, verified-at, recheck, ground, topic, gap filled, sources, couples, scope`; `S895` absent; `Superseded` absent; ids in the file = {S883, S884}; 10 table rows, **0** carrying an id; 2,215 words total (body from §1: 1,487 ≥ 478); no placeholder token. Final bytes: 91 lines, sha256 `0b2e06dcd9638ab181ef61126bb5199165e9fa1f211184de7591dcb0b2790d31`, id counts 20 × S883 / 16 × S884.
- Fetch identity: both pages re-fetched by me this wave — sha256 `a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d` (48,536 B) and `344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659` (62,604 B) — identical to the scouts' bytes, so the spans were checked against the same document.
- Ground re-derived at base `f7104cbce186bc2e1522abf0cfd619cc834628bb`: 0 worldbuilding/setting files, 0 `chinawriter` rows in the 804-row registry, 0 CJK term hits.

### Residual, not claimed

- §4 stays single-sourced on a tier-C row by design; this draft strengthens nothing, and a later round must re-open the row (its own re-quote) before any rule-shaped use.
- The headline string is quoted as metadata and labelled as such, not as body evidence; a strict QUALITY 16 reading would drop it, and dropping it changes no claim.
- I did not re-open S895, the two Japanese pages, or the base entry; the registry `used-by` outcome belongs to the append, and the Gate/evidence windows are the lesson seat's.
- Downloads this wave went to `/tmp/ScribeEntryAmend/r74/` only (`p2025.html`, `p2022.html`, `paras.json`); no tool installed, PACMAN untouched.
