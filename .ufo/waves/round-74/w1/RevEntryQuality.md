# RevEntryQuality — staged entries as admission candidates (round 74, wave 1)

Seat: `RevEntryQuality-3`, leaf. Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`. Read-only seat: every
repo write is this file; nothing else was written, no `task` spawned, no background job, no install.
Repo reads under `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, staged package reads under
`/home/vgpnk/Projects/shokuknow/merge/kotodama` (read-only; no campaign tool was run there).

Objects judged (the two staged files named in the item):

- **A** = `…/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/worldbuilding-setting-practice.md`
  (26 lines; source lines 4–6, proposed body 19–24)
- **B** = `…/worldbuilding-setting-practice.amend-2026-10-23.md`
  (44 lines; source lines 4–5, proposed body 18–19, and a retained third entry at lines 24–44
  citing S895)

The wave's replacement drafts were also read and spot-checked (they are the admission candidates that
would actually land): `.ufo/waves/round-74/drafts/worldbuilding-setting-practice.md` and
`…amend-2026-10-23.md`. §6 records what the drafts already fix and the three residual defects.

## 1. Verdicts

| Staged file | Verdict | Reason (one line) |
|---|---|---|
| A `worldbuilding-setting-practice.md` | **REFUSE-AS-IS** | every cited id resolves to a different lane document, the coupling line names a file the lane does not hold, no calibration status, and the file is a proposal outline, not an entry (no table, checklist or worked example) |
| B `worldbuilding-setting-practice.amend-2026-10-23.md` | **REFUSE-AS-IS** | both source ids are unknown in the lane, the retained "Superseded passage" cites S895 which no row_set lands, the tier-C delivery schedule is stated unhedged and as "paired" when it is single-sourced, and the body is two bullets |

Neither is REFUSE-FOR-FACTS: **every factual sentence I could locate in the five sources is true of
the page I fetched** (§4). The refusals rest on citation namespace, calibration, form and scope — the
classes the round's kill rule names. The flip is the drafts (§6): they renumber by document, rebuild
the entry as tables, and re-verify at 2026-10-25. They clear everything A and B fail except three
residuals.

## 2. Findings, by severity

### HIGH-1 — every cited id names a different lane document (three namespaces, joined by nothing in these files)

The ids in both files are **staged** (`shokuknow` S-space), never joined to the lane registry. At base
the lane holds 804 rows, last id `S880`, and **0** rows naming litmemo.com, tuduku.space or
chinawriter.com.cn (`grep -cE 'litmemo|tuduku|chinawriter' corpus/SOURCES.md` → `0`). Post-adoption numbers below follow the wave's `w1/id-map-draft.json` (a hypothesis, joined by document,
not arithmetic); at base none of the four new ids exists, and the base lane's 804 rows already occupy
S001–S880, so the same numbers name other documents:

| Staged file:line | id as written | document it means | what that number names in the lane | effect |
|---|---|---|---|---|
| A:4 | S882 | philol.msu.ru conlangs.pdf (Сидорова/Шувалова 2006) | post-adoption lane **S882 = tuduku.space** | wrong document |
| A:5 | S883 | litmemo.com/ja/blog/novel-worldbuilding-guide | post-adoption lane **S883 = chinawriter 2025/0605** | wrong document |
| A:6 | S884 | tuduku.space/column/novel-worldbuilding | post-adoption lane **S884 = chinawriter 2022/1207** | wrong document |
| A:9, A:12 | S729, S730 | by document (draft map): staged S870 (chinawriter 2023-09-22, 六人谈), staged S871 (douban writing guide) | lane **S729 = Neer et al. 2025** (infant-directed speech); **S730 = Genesee & Nicoladis 2007** | wrong documents, both unrelated |
| A:8 | "S882 -> 2, S883 -> 4, S884 -> 1" | campaign recheck outputs | no lane command | un-runnable recheck |
| B:4, B:7, B:12 | S899 | chinawriter 2025/0605 | **absent from the lane** (next free after adoption is S885); correct target is **S883** | unknown id |
| B:5, B:7, B:12 | S900 | chinawriter 2022/1207 | **absent**; correct target is **S884** | unknown id |
| B:11 | S742, S743, S754 | staged S883/S884/S895 | lane **S742 = Shields-Lysiak et al. 2020**; **S743 = Akita 2012**; **S754 = UNESCO ICH 01080 "Tugging rituals and games"** | wrong documents |
| B:31, B:33, B:39, B:44 | S895 | chinawriter 2025/1030 (王昕玥) | **absent from the lane** and **not in the row_set** (draft id map: "not_assigned … S895 — keep staged ids, campaign-local") | unknown id |

Evidence for the lane numbers: `grep -E '^\| *S(729|730|742|743|754) *\|' corpus/SOURCES.md` returns the five
unrelated rows quoted above; `grep -E '^\| *S(895|899|900) *\|' corpus/SOURCES.md` returns nothing.
This is the round's kill rule verbatim — "any admitted entry cites a refused/unknown staged id or an id
naming an unrelated lane document" — and it fires on every one of the **11 distinct staged ids** the two
files cite (A: S882, S883, S884, S729, S730; B: S899, S900, S742, S743, S754, S895).

### HIGH-2 — a tier-C row carries each admitted claim, and the "paired" sentence is false

`SOURCES.md:18` defines the tier that both files invoke: "**C — lead only, never sole support for
an admitted entry**" (11 words). `QUALITY.md` repeats it ("a tier-C row is a lead, never sole support
for an admitted claim").

- **A:13** — "S883 and S884 are tier C and are never the sole support: S882, a tier-B row, states the
  scholarly framing that the practitioner guides elaborate." The five-step order, the four layers, the
  five elements, the note sections and the single-source rule each rest on **one** tier-C page. The
  tier-B book supports none of them: it is a taxonomy of constructed languages (its chapter 2 is
  "вымышленные языки в мире"), and A §2 takes the only "modelling" sentence from its **back-cover
  annotation, phrased as a question** (see MEDIUM-4). The pairing is nominal, not support.
- **B:12** — "paired so that neither is the sole support." The build order is sourced twice (¶67 of the
  2025 page, ¶50 of the 2022 one); the **delivery schedule is sourced once**, from the tier-C 2022
  interview alone (¶34). A claim stated as a rule in B §N+1 therefore has a tier-C sole support, which
  the registry forbids.

### HIGH-3 — the files are proposals, not entries (QUALITY 4)

Both files carry a literal `### Proposed body` heading and numbered/bulleted intentions, not an entry:
A lines 19–24 are six one-line bullets ("**§3 The build order and the four layers** — from S883: …"),
B lines 18–19 are two. There is no decision table, typology table, checklist or worked example anywhere
in either file (`grep -c '^|' <files>` → `0`, `0`; the drafts carry 15 and 2 tables, 100 + 10 table
rows). QUALITY 4 requires exactly those and refuses essays; an outline is weaker than an essay,
because it makes claims without stating them. This is a form defect of the staged files only.

### MEDIUM-1 — criterion 15 fails mechanically on both files, passes on the drafts

`tools/check-cited-lines.py` (lane tool, read-only run):

```
A: MULTI-ID …:8 S882,S883,S884
   MULTI-ID …:9 S729,S730
   MULTI-ID …:12 S729,S730
   MULTI-ID …:13 S882,S883,S884
   CITED-LINES: 4 finding(s) in 1 file(s)      exit=1
B: MULTI-ID …:7 S899,S900
   MULTI-ID …:11 S742,S743,S754
   CITED-LINES: 2 finding(s) in 1 file(s)      exit=1
drafts: CITED-LINES: 0 finding(s) in 2 file(s) exit=0
```

Three of A's four findings are on header lines that a reader would take as one citation each (the
`recheck` line with a triple arrow-map, the `ground` line, the `sources` line). Criterion 15's lint
covers only MULTI-ID/TABLE-ID, so the remaining clause-scope judgment is review-only — and it also
fails by eye: A:13's one line carries "S883 and S884 are tier C … S882, a tier-B row" (two clauses,
three ids).

### MEDIUM-2 — the coupling lines name a file the lane does not have (QUALITY 3)

- A:14 couples `myth-symbol/narrative-structure-frameworks.md`.
- B:13 couples `myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md`.
- B:39 couples the same missing path.

Verified absent: `git ls-tree -r --name-only <base> -- corpus/knowledge | grep -cE 'narrative-structure'`
→ **0**; a filesystem `find` hits only the staged package and this round's drafts. The merge package
plans that path for other rounds (`MERGE-REPORT.md` "Target-path conflicts"), but **this round's
row_set does not land it**, so in the lane the coupling is an invented file. The other paths exist:
`synthesis/coupling-model.md`, `linguistics/naming-systems.md`,
`culture-material/cartography-and-mapmaking.md`, `synthesis/worldbible-integration-contract.md`,
`synthesis/consistency-verification-checklist.md`.

Consequence beyond the criterion: the staged entry's natural home for its narrative-side content (the
four-layer chain's "individual experience", B's whole delivery schedule) is exactly the missing file,
so a coupling to it would also be the wrong partition if the file existed.

### MEDIUM-3 — no calibration status in QUALITY 2's vocabulary (both files)

`grep -cE 'mainstream|contested|discredited'` → A **0**, B **0**. A:19 offers "Calibration key — tier C
as method evidence" — a source **tier**, which is a different axis from calibration status. B offers
nothing at all. The lane's convention (e.g. `linguistics/conlang-scholarship.md:17-25`) is a
"| Framework | Status | Why it is placed there |" table; both staged files lack it. The drafts have the
table; the amend draft also names `contested` in QUALITY 2's words.

### MEDIUM-4 — provenance is by id only, and A's one scholarly sentence is an annotation question read as an assertion

QUALITY 1 requires a checkable locator (author + year, edition, or stable ID). The staged source lines
carry **no author and no year** (A:4–6, B:4–5) and **no quotation**; the only locator for A §2 is the
word "аннотация". What the annotation actually says, PDF p. 2:

> "Чем является лингвоконструирование для человека рубежа тысячелетий – игрой, опытом моделирования
> иных реальностей, попыткой решения внешних … проблем …?"

`опытом моделирования иных реальностей` (5 words) — this is the book's **question**, not its finding.
A §2 ("linguistic construction as modelling of other realities") turns it into an assertion. The
sentence that would support the claim is on **p. 7**:

> "Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и
> социальных реалий" (15 words)

and A never cites p. 7. Same class in B: B:4 labels the 2025 article 「非凡特性来自最初造物主」答问 —
that is a clause from a body answer (¶67), not the document's title, which is
「爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”」 (`<title>` and `em#newstit`, both fetched). B:5's "答问"
is likewise not the title (「爱潜水的乌贼：网络文学不断“升级”的“奥术”」, 来源：《青春》, 李玮). A reader
cannot match either citation to its row.

### MEDIUM-5 — the recheck and ground lines point into the campaign tree, not the lane

A:8 "re-run the three row recheck commands in round 2's `SOURCES-PROPOSED.md` (S882 -> 2, S883 -> 4,
S884 -> 1)"; A:9 "round 1's CANNOT-ANSWER §5"; B:7 "round 4's `SOURCES-PROPOSED.md`"; B:8 and B:34
"round 2's/round 3's CANNOT-ANSWER".

The pointer does resolve — but only in the campaign tree, never in the lane. That file is
`/home/vgpnk/Projects/shokuknow/lanes/kotodama/round{2,4}/SOURCES-PROPOSED.md`, untracked by the lane
repo, and its expected outputs are exactly the three numbers A:8 quotes (S882 `grep -c
'Классификация искусственных языков'` → 2, S883 `grep -c '自然環境'` → 4, S884 `grep -c
'設定ノートの構成例'` → 1). The lane itself holds **no** `SOURCES-PROPOSED.md` and **no**
`CANNOT-ANSWER.md` (`find` under the lane root → nothing), so a lane re-opener has no such path, and the
arrow notation reads like a renumber map while being a list of `grep -c` counts. The campaign's own Gate
quote for S883 is valid — 「自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観
を作る」is on the live page — so this is a citation-locality defect, not a fabricated anchor.

### MEDIUM-6 — B's retained "Superseded passage" is a third entry whose row no claim lands

Lines 24–44 keep the round-3 entry and cite **S895** (chinawriter 2025/1030). That row is not in the
row_set; the draft id map rules it "keep staged ids, campaign-local". On landing it is an unknown id
(kill rule), and the passage's own `recheck` (B:33) is un-runnable for the same reason as MEDIUM-5.

The facts themselves check out — I opened the page (my fetch, §3) and found every element of the
passage: 「完整周密、规律清晰的世界体系」; the 拟真（应然）原则 rule; 「建立叙事驱动机制、价值共识框架与
类型标识系统」; the 「S-A-B-C级」混血种 classification 「因缺乏量化标准与逻辑约束，导致文本内部规则逐渐
走向崩塌」; 「仍然需要如程序般精密的设定」. So the fix is a row (with its own Gate record and re-quote),
not a rewrite of the prose — or a cut of the passage.

### MEDIUM-7 — B drops the source's own hedges on the twenty-chapter figure

B:19 states "release gradually, early, **within roughly twenty chapters**". The page's sentence (¶34)
carries 「大概」 before the number and closes with 「我觉得是问题不大的。」 (10 chars). B keeps the
approximation adverb and drops the speaker's own uncertainty marker — the difference between an
author's estimate and a measured-looking schedule. The draft keeps both (§4: "大概 and the closing
hedge … keep this an estimate, not a threshold").

### MEDIUM-8 — canon hygiene / scope: A §5 takes retcon territory; B ends nowhere

- A:23 — "**§5 Single-source discipline** — one authoritative 設定資料集 per series; **what happens
  when a setting changes mid-draft**." The second clause is retcon policy:
  `synthesis/worldbible-integration-contract.md:138` owns "Versioning, invalidation, and retcon safety"
  and `:156` reserves the retcon ruling to lore. QUALITY 5 says entries "end at the handoff"; an
  outline that announces a retcon procedure before the handoff crosses PROVINCE's "kotodama *hands
  off* systems; lore records and verifies them".
- The "per series" scoping is not the page's advice: its body states the capability in a product
  paragraph — 「同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有できます。」
  (41 chars, 世界観設定のまとめ方 section) — while the *rule* (one 正本, rewrite it the same day) is in
  the FAQ and step 5. A collapses a vendor capability into a method rule.
- B has no handoff at all: its six header bullets (lines 10–14) and two body bullets (18–19) name no
  `worldbible-integration-contract.md` coupling and no stop line; only "it decides no world's canon".

### LOW-1 — A's own count contradicts itself and the page

A:22 "**§4 The five elements and the six tables** — from S884: 地理・環境, 歴史・背景, 魔法・技術システム,
社会制度・文化, 勢力図; and the settings note that holds 世界地図・地名一覧, 年表, 能力一覧, 人物一覧,
制度・用語集." The label says **six tables**; the list that follows is **five**; the page's 「設定ノートの
構成例」 box holds exactly **five** `<li>` (世界地図・地名一覧 / 年表・歴史 / 魔法・能力一覧 / 人物一覧 /
社会制度・用語集). The error is inherited from the staged row: `SOURCES.append.md` S884's `teaches`
cell also says "the six tables a settings note should hold". The draft's S882 row and §6 say five
sections + four fields, which is what the page holds.

### LOW-2 — A §3's arrow is not the page's build order

A:21 renders the order as one six-node arrow (核になるルール → 生活圏 → 自然環境 → 社会の仕組み → 文化 →
個人の経験) and calls it "the build order and the four layers". The page keeps these in **two separate
sections** — h2「世界観の作り方：5つのステップ」 with h3 1–5 (step 3 is the causal chain, steps 4–5 are
depth and recording), and h2「世界観の4つの層」 — and its five-step sentence names steps 4 (「物語で使う
分だけ掘り下げる」) and 5 (「一か所にまとめ、書きながら更新する」) that the arrow silently drops. The
entry then claims the depth rule and the single-source rule as §4/§5 content without ever sourcing them
to the section that states them.

### LOW-3 — dates and captures

Both files say `fetched 2026-10-23` / `verified-at: 2026-10-23`. This round's appraisal is a 2026-10-25
re-open (claim C's row condition: opened date must be 2026-10-25, and the kill rule requires every cited
source to carry a round-74 Gate record with a committed evidence window), and the entries name no
archived capture for durability even where one exists (both chinawriter pages have status-200 captures;
the two Japanese pages have none — QUALITY 21/24, `ScoutWayback.md` §1–§2). The staged files therefore
cannot supply their own Gate/durability legs; the drafts do (row-level).

## 3. Sources opened for this review (own fetches)

UA for every request: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
(curl 8.23.0). Downloads in `/tmp/RevEntryQuality/`. No wall, no challenge, no automation. All four theme
pages are byte-identical to the L1's `/tmp/q74/` captures (same size and sha256), so the two independent
fetches agree.

| URL | HTTP | bytes | sha256 | note |
|---|---|---|---|---|
| `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1,055,723 | `e512a20d…ca595a9` | `pdfinfo`: 185 pages, Title `verstka`; the complete typeset book (184 с.), **not** a "series announcement booklet" |
| `https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 101,615 | `441fc921…34ca64` | article dated 2026年07月16日; h1 「世界観の作り方｜小説の世界観設定5ステップと架空の国・魔法の例」 |
| `https://tuduku.space/column/novel-worldbuilding` | 200 | 17,068 | `754f504c…cfc1b7` | `つづく編集室`; h1 「Web小説の世界観・設定の作り方｜…」; self-count 「約1,100文字」 |
| `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | 200 | 48,536 | `a3b6640c…bee94d` | title 爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”; 文汇报, 邵燕君/谭天/项蕾, 2025-06-10; 92 body `<p>` |
| `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | 200 | 62,604 | `344de345…bdd3d659` | title 爱潜水的乌贼：网络文学不断“升级”的“奥术”; 《青春》, 李玮, 2022-12-07; 69 body `<p>` |
| `https://www.chinawriter.com.cn/n1/2025/1030/c404027-40592897.html` (S895) | 200 | 45,262 | `95b688fc…b09b58ceb` | title 王昕玥：论《龙族》的叙事失控与世界观危机; 「二、世界观的预设缺陷」 present |

Notes that touch the entries' facts:

- The PDF's p. 2 is the book's annotation (УДК/ББК/ISBN + the "Первая книга в серии…" paragraph).
- litmemo's section skeleton (h2/h3, enumerated from the bytes): 世界観とは / 世界観の作り方：5つのステップ
  with h3 1–5 / 設定から作るか、物語から作るか / 世界観の4つの層 with h3 第1層–第4層 / 世界観設定で決めること
 チェックリスト / 霧の港町 / 架空の国の作り方 / ファンタジーの設定：ジャンル別 / 魔法の設定の作り方 / 世界観は
  どこまで決める？ / 役立つテンプレートと機能 / よくある失敗 (4 h3) / 世界観設定のまとめ方 / おわりに / FAQ.
- tuduku's three labelled boxes: 「世界観設定の5要素」(5 `<li>`), 「設定ノートの構成例」(**5** `<li>`),
  「注意点」; the failure table has 4 rows; one `KEY POINT` box.
- B's claims verified against the fetched bytes: paragraph numbering by the draft's rule
  (`<p style="text-indent: 2em…">` in document order) reproduces exactly — 92 on the 2025 page, 69 on
  the 2022 page: ¶67 carries 「我先做的是世界观，再考虑怎么升级，再考虑升级的表现。」 (1 token, 26 chars),
  ¶68 the iteration sentence, ¶65 the rejected mechanics, ¶60/¶61 the tarot derivation and the realism
  ladder, ¶7 谭天's framing, ¶31/¶33 李玮's competing prescriptions, ¶32 the suspense hook, ¶34
  「把它放在前面大概20章之内慢慢来」 (1 token, 16 chars) and 「我觉得是问题不大的。」 (10 chars), ¶50 the
  earlier statement of the same order.

## 4. Per-claim check of the staged bodies

Legend: ✔ supported at the named locator · ◐ supported only after re-locating/rewording · ✘ not
supported as written.

**A (`worldbuilding-setting-practice.md`)**

| Body line | Claim | Result |
|---|---|---|
| 19 | calibration key = tier C | ✘ tier is not calibration status (MEDIUM-3) |
| 20 | "linguistic construction as modelling of other realities" from the annotation | ◐ annotation poses it as a question; assertion is at p. 7 (MEDIUM-4) |
| 21 | build order as a six-node arrow | ◐ five-step order exists, but steps 4–5 dropped and the 4 layers merged in (LOW-2) |
| 22 | five elements ✔ / "six tables" ✘ | ✔ elements (5 `<li>`), ✘ note sections (5, not 6) (LOW-1) |
| 23 | single-source discipline, per series, mid-draft change | ◐ rule ✔ (step 5 + FAQ 「全員が同じ設定資料を一つだけ使い、それを正本にします。」); "per series" is a product capability, not advice; mid-draft retcon is lore's (MEDIUM-8) |
| 24 | handoff to lore | ✔ exists as a bullet, but contradicts line 23's retcon claim |

**B (`…amend-2026-10-23.md`)**

| Body line | Claim | Result |
|---|---|---|
| 18 | world-view → progression → expression; premise implies mechanics | ✔ ¶67 for the order and the inference chain (万事万物 → 合理的推论 → 物质性的表现 → 非凡特性定律 → 服食魔药/扮演法); the "rather than mechanics assumed" half is the entry's inference and is unmarked as such |
| 19 | gradual, early, ~20 chapters, behind a hook | ✔ ¶34 in full, but hedges dropped (MEDIUM-7) |
| 44 | S895's three requirements, the S-A-B-C collapse, "precise as a program" | ✔ page content (¶170–175); ✘ the citation has no lane row (MEDIUM-6) |

## 5. The cuts (what ADMIT-WITH-CUTS would require of these exact files)

Every line-level cut is a rewrite, which is why the verdict is REFUSE-AS-IS; recorded for completeness
and because the drafts implement almost all of them.

**A**: cut recheck/ground (lines 8–9) and replace with a lane-runnable re-open; renumber S882→S877,
S883→S881, S884→S882 **simultaneously** (a chained map: staged S884→lane S882 while staged S882→lane
S877); delete `S729`/`S730` (prose only, no admission); replace the `couples` line's narrative path
with existing lane files; add the calibration table in QUALITY 2's vocabulary; cut "per series" to the
page's own advice plus a `(to-verify)` on the capability; cut the mid-draft retcon clause to the
`worldbible-integration-contract.md` handoff; rebuild the six bullets as tables; cut "six" to five;
re-source §2 from p. 7 (or drop the claim).

**B**: renumber S899→S883, S900→S884; cut the S895 passage **or** land S895 as its own row with its own
Gate record and re-quote (it is a live, quotable tier-B page); delete `S742`/`S743`/`S754`; replace the
`couples` line (missing narrative path) with `synthesis/worldbible-integration-contract.md` and the base
entry; add the calibration status (`contested`, with the interviewer's competing prescription at ¶33 as
the reason); restore 「大概」/「我觉得是问题不大的」 and demote the schedule to a lead; add the handoff stop.

## 6. The wave's replacement drafts — spot-check results and 3 residual defects

What I ran and what passed:

- `tools/check-cited-lines.py` on both drafts → `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0.
- `tools/check-draft-ids.py` on both drafts → `DRAFT_IDS: 0 findings`, exit 0.
- **31/31** quoted spans of the amend draft resolve to the exact paragraph its source line names
  (¶7, 31, 32, 33, 34, 50 on the 2022 page; ¶60, 61, 65, 67, 68 on the 2025 page). No drift.
- The draft's four Russian quotes were re-located in the PDF at the printed pages it names: p. 7
  (Язык – главный инструмент…), p. 16 (classification 2.3 Фикциональные), p. 35 (связь … неразрывна),
  p. 36 (научное или не совсем научное допущение). Its recheck note is accurate: plain `pdftotext`
  de-hyphenates (6 × `лингвоконструирование`, 0 × line-end `лингво-`), `-layout` keeps one
  (5 × joined, 1 × `лингво-`).
- The draft's counts hold against the bytes: 8-field country table (+header), 7 magic questions, the
  page's own 「見落とされやすいのは最後の二つです。」 (18 chars) for the last two, 3-row distance table,
  4 failure h3s, three depths, 4-row 霧の港町 table, tuduku's 5 elements and 5 note sections, its
  4-row failure table, and the `KEY POINT` box quote.
- All draft coupling paths exist in the lane (cartography, naming-systems, conlang-scholarship,
  coupling-model, consistency-verification-checklist, worldbible-integration-contract).

Three residuals for the landing bytes:

1. **MEDIUM (QUALITY 2 vocabulary)** — `drafts/worldbuilding-setting-practice.md` contains **0**
   occurrences of `mainstream|contested|discredited`; its calibration table uses "practitioner
   convention, unmeasured", "descriptive scholarship, single monograph, one school", "(to-verify)".
   The lane's convention permits descriptive statuses (`conlang-scholarship.md:17-25`), but criterion 2
   names the three-term vocabulary, so add the mapping (e.g. "not mainstream — unmeasured practitioner
   convention; nothing here is contested or discredited"). The amend draft already says `contested`.
2. **LOW (accuracy of a calibration parenthetical)** — base draft §9 marks the per-series reading
   "(to-verify)" with the reason "the linked article's promise, **not this page's own body**". The
   per-series capability *is* in this page's body, in the まとめ方 section:
   「同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有できます。」 (41 chars).
   The `(to-verify)` is still right — it is a vendor capability paragraph, not advice — but the reason
   should say so rather than deny the location.
3. **LOW (row-level, seen while checking A)** — the staged row `SOURCES.append.md` S883 must not be
   appended as-is: its title 「小説の世界観はどう作る？ ゼロから説得力のある架空世界を…」 has **0 hits**
   on the live page (both fragments), and its anchor cell names 「設定資料集 を本文とズレさせない3ステップ」,
   which is a *linked article* title (related-card h3 on the page), not a section of it. Also
   `S882` calls the PDF a "series announcement booklet" while the URL serves the complete book, and
   `S884` repeats the "six tables" count. The draft's source lines replace all three (S877 reused with
   printed-page locators; new rows S881/S882 with section anchors that exist); the fix belongs to
   whoever appends the registry.

## 7. Residual risk and verification gaps

- **Scope judgment (review-only).** Whether a whole-setting method is in-province at all is not
  mechanical. My reading: PROVINCE owns "linguistic-cultural worldbuilding" generative craft and the
  sibling sweep found no other owner, so the theme is in scope; but B's delivery schedule is serial
  pacing, and its natural coupling partner (narrative structure) does not exist in this lane. The
  draft's handoff to the world-bible contract is what keeps that content on the right side; a stricter
  reviewer could still route the schedule to a narrative-craft lane if one ever owns it.
- **Not re-derived by me**: the two chinawriter captures' byte identity was taken from
  `ScoutWayback.md` §3/§5 and `ScoutQuarantine816817.md` §2 (they name `20250611013901id_` with sha
  `a3b6640c…` and `20221207080111`), not re-probed by this seat; I confirmed only that today's live
  bytes equal those two stated sizes/shas.
- **Not checked**: the litmemo/tuduku "no capture" rulings are QUALITY 21/24 row/Gate work
  (`ScoutWayback.md` §2 probed 13 shapes with a positive control); I did not re-run CDX.
- **Not checked**: whether the two Japanese pages' content changed between 2026-10-23 (staged fetch)
  and today. Both were fetched by the L1 on 2026-10-25 and by me today with identical bytes; the
  staged 10-23 bytes were not preserved, so a silent edit between 10-23 and 10-25 is
  indistinguishable from no edit. It does not change any verdict, since every claim was checked
  against today's bytes.
- **Quotes**: all ≤25 words; Chinese/Japanese spans counted with `wc`-style whitespace tokens and
  character counts given above (CJK) per the round's convention.
- **Tooling**: none installed or upgraded (nothing was needed; `pdftotext`/`pdfinfo` and curl 8.23.0
  were already present).
