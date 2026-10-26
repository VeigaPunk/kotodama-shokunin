# CritFactBase1 — falsification of `worldbuilding-setting-practice.md`, §1–§5

- seat: CritFactBase1 (leaf; no delegation, no background jobs, no `task` spawns)
- round: kotodama 74, WAVE 2 (falsify; hyaku run 7)
- target: `corpus/knowledge/culture-material/worldbuilding-setting-practice.md`, **§1–§5** (split at the `## §` headings; §6–§10 read only where a §1–§5 statement needed a counterexample, and their named table counts checked as the assignment requires)
- frozen claim read first: `git show 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/claims.json` (claims C and Ca; C's legs ENTRIES/ROWS/GATE/EVIDENCE; Ca's SEPARABLE excludes `corpus/knowledge/**`)
- revisions: base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; freeze F3 `00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; `git diff --stat c4bf61a8..main -- corpus/knowledge/culture-material/worldbuilding-setting-practice.md corpus/SOURCES.md reports/round-74/evidence/S877.txt reports/round-74/evidence/S881.txt reports/round-74/evidence/S882.txt` is empty (exit 0), so the entry, its rows and the evidence windows are unchanged from the lands commit to `main`
- lane repo untouched (read-only git/reads); scratch `/tmp/CritFactBase1/`; the only file written is this report
- counters `accept-c.py` / `accept-ca.py` **not run**: they are not part of this seat's attack (the assignment is the entry's sources, not the claim's counter)

## Verdict (one line)

**The citation apparatus survives every quote and every table count I could test — but one table cell about the monograph is false, and the entry's S877 use is (a) outside the reused row's recorded scope and (b) almost entirely un-anchored by page locators or committed evidence.** No fabricated quote, no wrong page for the four Cyrillic quotes, no wrong Japanese quote, no wrong table count. 0 BLOCKER, 1 HIGH (scope; already filed as ScoutReopenS877 F1, independently reproduced here), 3 MEDIUM (F1–F3), 7 LOW (F4–F10), 1 observation.

## 1. Fetch record (per fetch, exact UA)

UA used for every fetch:
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
$ curl -sS -o conlangs.pdf -w '%{http_code} %{size_download}\n' -A "<UA>" \
    http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
200 1055723
$ sha256sum conlangs.pdf
e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9  conlangs.pdf
$ pdfinfo conlangs.pdf | grep -E 'Pages|Page size'
Pages:           185
Page size:       595 x 842 pts (A4)
```
(185 PDF pages = cover + 184 numbered; the imprint on p. 2 reads `2006, с.184`. The entry's "184-page monograph" and the row's "185-page typeset text" are both defensible; see F11.)

```
$ curl -sS -L -o s881.html -w 'S881 %{http_code} %{size_download} %{content_type}\n' -A "<UA>" \
    https://litmemo.com/ja/blog/novel-worldbuilding-guide
S881 200 101615 text/html;charset=UTF-8
$ curl -sS -L -o s882.html -w 'S882 %{http_code} %{size_download} %{content_type}\n' -A "<UA>" \
    https://tuduku.space/column/novel-worldbuilding
S882 200 17068 text/html
$ sha256sum s881.html s882.html
441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64  s881.html
754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7  s882.html
```

All three byte/hash values equal the entry's source lines, the evidence windows and the registry rows. No wall, no challenge, one attempt each. Extraction: `pdftotext -enc UTF-8 conlangs.pdf conlangs.txt` (828,078 chars, 186 form-feed chunks, last empty); the two Japanese pages with a stdlib `html.parser` (drop script/style/noscript, block tags → newline), giving 9,958 visible chars for S881 and 3,025 for S882 (the evidence file records 9,855 and 2,953 with its own normaliser — same document, different whitespace collapse).

## 2. Locator audit — the entry has **zero** `(loc: …)` locators

```
$ grep -c '(loc:' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
0
$ grep -c '(loc:' corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
29
$ grep -n '(S877)' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
36: … (S877).
38: … (S877).
42: … (S877).
44: … (S877).
```

The same round's companion amendment gives every quote a `(loc: P68)` / `(loc: para 32)` / `(loc: P2 and P3–P6)`; the older S877 consumer gives a page per sentence:

```
$ grep -n 'S877 p' corpus/knowledge/linguistics/conlang-scholarship.md | head -4
69: … (S877 pp. 16–17, 19–20).
70: … (S877 p. 19)
71: … (S877 pp. 19–20).
72: … (S877 p. 21)
```

The target entry instead carries a single page list in the header ("printed pages 7, 35, 36, 139 and 140") for four quotes. Which page belongs to which sentence is recoverable only by re-fetching the book. See F3.

Page mapping I re-derived (folded search, so line breaks inside the PDF do not hide a quote):

```
ru1 (p.7?) -> PDF pages [7]     page label present: 7
ru2        -> PDF pages [139]   page label present: 139
ru3        -> PDF pages [35]    page label present: 35
ru4        -> PDF pages [36]    page label present: 36
```

## 3. Sentence-by-sentence table, §1–§5

`✓` carried; `~` paraphrase-beyond-source; `✗` not carried. Page/section is where I found the span on the served artefact.

### §1 Calibration key (rows sourced by the header's three source lines)

| line | claim | source evidence | verdict |
|---|---|---|---|
| 20 | LitMemo: vendor blog, organisation-authored, no named practitioner, no cohort, **no citation**, product CTAs beside the advice | JSON-LD `"author": {"@type": "Organization", "name": "LitMemo"}`; CTAs 「世界観設定シートを作ってみる」/「無料で始める」; but the page does cite Tolkien (1939 lecture), Sanderson and Hemingway for other claims | ~ (F5) |
| 21 | tuduku: editorial-service marketing column, ~1,100 chars by its own count, no byline beyond the service name, **checklists with one-clause glosses** | page prints 「約1,100文字」 and the byline つづく編集室; the five element glosses run 2–3 clauses (「地理・環境：どんな地形か、複数の国や地域があるか、気候や自然環境はどうか」) | ~ (F6) |
| 22 | four-layer chain: one page's causal assertion, no evidence, heuristic not finding | page states the chain and gives an illustration, no evidence | ✓ |
| 23 | Sidorova & Shuvalova 2006: taxonomy, no authoring order, reports rather than tests | p. 2 imprint `2006, с.184`; TOC (p. 3) has no authoring chapter; p. 139–140 argue the activity is useful, they do not prescribe an order | ✓ |
| 24 | hard/soft: page names ブランドン・サンダースン, cites no edition, (to-verify) | 「ファンタジー作家ブランドン・サンダースンは、魔法を「ハードマジック」と「ソフトマジック」に分けて論じ…」; no edition/link | ✓ |
| 26 | "Status vocabulary, in QUALITY 2's terms: not mainstream …" | `corpus/QUALITY.md:9` defines the statuses as "mainstream / contested / discredited"; "not mainstream — unmeasured" is a fourth label | ~ (F9) |
| 30 | LitMemo advice inseparable from the product it sells | CTAs and templates section | ✓ |

### §2 What the scholarly source adds (S877)

| line | claim | page | verdict |
|---|---|---|---|
| 36 | "Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и социальных реалий" | p. 7: `…эскапизма. Язык – главный / инструмент построения вымышленных миров, дающий названия для их / природных и социальных реалий, собственные имена, позволяющий создать…` | ✓ (fragment ends mid-sentence without an ellipsis; translation correct) |
| 38 | "ВЯ в общем случае не служит средством коммуникации, он является предметом, темой коммуникации" | p. 139, item 14: identical; continues `…то есть вокруг него формируется особый набор коммуникативных ситуаций…` | ✓ (gloss "a constructed language" overgeneralises ВЯ → F2, corroborating ScoutReopenS877 F2) |
| 40 | "Design consequence: a world's language layer is sized to what the world must carry, not to a need for talk — the same volume rule … records" | conlang-scholarship §4: "the required size and detail of lexicon and grammar follow from what the language is for (S877)" | ~ (F7) |
| 42 | "связь между лингвоконструированием и моделированием миров неразрывна" + either direction | p. 35: `Важно то, что, как бы ни двигался создатель ВЯ (от языка к вымышленному миру или наоборот) связь … неразрывна.` | ✓ |
| 44 | "некое научное или не совсем научное допущение" then the world-picture | p. 36: `…автор предлагает читателю некое научное или не совсем научное допущение и далее строит вокруг него ту картину мира, которая, по его мнению, сложится при существовании данного допущения.` | ✓ quote; the promotion "states the rule" / "strongest single design rule" is the entry's (F4, corroborating ScoutReopenS877 F3) |
| 50 | what a constructed world is | p. 7 (`моделирование миров`) + p. 139 (`предмет, тема коммуникации`) | ✓ |
| 51 | why a world needs a language layer | p. 7 + p. 139 | ✓ |
| 52 | where to start: a premise, then the world picture | p. 36 | ✓ |
| 53 | in what order to fill the parts: not addressed | p. 35 gives two free directions, no order | ✓ |
| 54 | **how to keep it consistent: not addressed** | p. 140: `их эволюция, межъязыковые контакты и заимствования, формирование диалектов и литературного языка, возникновение социальных и прочих жаргонов должны быть логично связаны с историей мира` | **✗ (F1)** |

### §3 What a setting is (S881)

| line | claim | page | verdict |
|---|---|---|---|
| 58 | "物語が起きる世界の決まりごとの総体です"; 世界観設定 vs 設定資料（設定資料集） | h2「世界観とは：物語の舞台とルールのまとめ」: `…物語が起きる世界の決まりごとの総体です。…書き出して整理したものが世界観設定、まとめた資料が設定資料（設定資料集）です。` | ✓ |
| 60 | "a contemporary novel needs no magic system and no political constitution, but … the town, the workplace or school, and the invented company or district, decided once" | FAQ 「現代が舞台の恋愛ものでも世界観は必要ですか？」: `必要ですが、決める量はずっと少なくなります。政治制度や魔法のルールは要りません。物語の舞台になる町、登場人物の職場や学校の仕組み、人間関係の輪、そして作者が作った架空の会社・地名・学科…`; the page's own table also has a 現代もの＋非日常 row (「現実と違う部分と、それが隠れている理由」— 退魔師, 能力者がいる高校) | ~ (F2) |
| 62 | how much to decide is a function of distance from the real world | h2「架空世界の作り込み度合い」: `どこまで現実から離れるかで、作る量が変わります。` | ✓ |
| 66 | complete other world: geography, history, species self-made; most; proper-noun warning | table row 完全な異世界: `地理・歴史・種族まで自分で作る` / `多い` / `固有名詞を一度に出しすぎると読者が覚えられない` | ✓ |
| 67 | alternate history: one divergence; medium; research to the divergence | row 歴史改変（IFもの）: `実在の歴史が、ある時点から別の道を進む` / `中くらい` / `分岐点までは史実を調べ、分岐後の変化は理屈で積み上げる` | ✓ |
| 68 | real world + local lie: few invented elements; least; explain the secrecy | row 現実＋局所的な嘘: `現実の世界に、いくつかの架空の要素を足す` / `少ない` / `なぜ世間にその秘密がばれないのかを説明できるようにする` | ✓ |

### §4 Build order (S881, S882)

| line | claim | page | verdict |
|---|---|---|---|
| 74 | five-step quote | h2「世界観の作り方：5つのステップ」lead sentence, exact | ✓ |
| 76 | "決めておくのは、展開に直接かかわる核の設定だけで十分です。" | FAQ 「書き始める前に世界観をすべて決めておくべきですか？」, exact | ✓ |
| 78 | tuduku five-step order: core concept one sentence; day wake→sleep; deepen story parts; contradiction check vs past episodes; reader "why not just…" | tuduku `<ol>`: `コアコンセプトを一文で決める` / `主人公の日常を想像する：起きてから寝るまで` / `物語に関わる部分だけ深掘りする` / `矛盾チェック…過去のエピソードと照合` / `読者からのツッコミを想定する：「なぜ〇〇しないのか」` | ✓ |
| 84 | premise row: 1–3 rules + temperature / core concept in one sentence | S881 step 1 (`1〜3個`, `作品の空気`) + S882 step 1 | ✓ |
| 85 | near field: town, daily route, organisations / day wake→sleep | S881 step 2 (`住んでいる町、通う場所、顔を合わせる組織`) + S882 step 2 | ✓ |
| 86 | outward cause: environment→society→culture→person / no separate step | S881 step 3 + S882 element 2 (`現在の状況がなぜそうなっているか`) | ✓ |
| 87 | depth: story questions only, blank fields allowed / story-relevant parts | S881 step 4 (`空欄のままで構いません`) + S882 step 3 | ✓ |
| 88 | recording: one place / note + past episodes + objection | S881 step 5 + S882 steps 4–5 | ✓ |
| 90 | the fork: scene/character or world | h2「設定から作るか、物語から作るか」, two table rows | ✓ |
| 94 | scene/character → core rule + scene settings; serialised, short/medium, contests | row 1: `核のルールを決め、物語に必要な設定だけを外へ足していく` / `Web小説の連載、短編・中編、新人賞への応募作` | ✓ |
| 95 | world → coarse map, town, powers; long fantasy, series, tabletop/game | row 2: `粗い地図を描き、主人公の町と周りの勢力を決めてから…` / `長編ファンタジー、シリーズもの、TRPGやゲームの企画` | ✓ |
| 97 | the endpoint is "how a character lives in that world", "which is the four-layer chain's last layer" | page: `最後は「登場人物がその世界でどう暮らしているか」にたどり着く必要があります。`; last layer: `個人の経験（登場人物がこの世界をどう感じるか）` | ~ (F8) |

### §5 The four-layer chain (S881)

| line | claim | page | verdict |
|---|---|---|---|
| 101 | chain quote | h3「3. 外側の層へ因果をつなぐ」2nd sentence and the 4-layer list, exact | ✓ |
| 103 | "外側の層が内側の層を決める" | `ポイントは外側の層が内側の層を決めることです。` | ✓ |
| 107 | 自然環境: geography, climate, creatures, resources | 4-layer list: `自然環境（地理・気候・生き物・資源）` | ✓ |
| 108 | 社会の仕組み: politics, economy, status, law; checklist adds military and judgment | list `（政治・経済・身分・法）`; checklist 第2層 adds `軍事` and `法と裁き` | ✓ |
| 109 | 文化: language, faith, habit, taboo | `文化（言語・信仰・習慣・タブー）` | ✓ |
| 110 | 個人の経験: how a character feels this world | `個人の経験（登場人物がこの世界をどう感じるか）` | ✓ |
| 112 | micro-chain: sea trade → merchants' voice → oath-breaker most hated | `海に囲まれた土地では海運と交易が育ち、交易で栄えた町では商人の発言力が強くなり、商人が強い町では「約束を破る者」がもっとも嫌われる` | ✓ |
| 116 | worked town: fog harbour; guild stronger than the crown's deputy; fire taboo; protagonist knows the fog-beast is the guild's story | table 霧隠: `崖下の港…一年中濃い霧`; `灯台守ギルド…王国から派遣された代官より強い力`; `日没後に屋外で火を灯すことを禁じている`; `霧獣の言い伝えがギルドの作り話だと幼いころから知っている` | ✓ ("crown's" is an addition for 王国's 代官 — harmless) |
| 118 | "読者は登場人物の目を通して世界を見ます。" | exact | ✓ |
| 120 | a detailed political system no character suffers under does not exist for the reader | `緻密に作った政治制度も、登場人物がそれで悩んだり怒ったりしなければ、読者にとっては存在しないのと同じです。` | ✓ ("suffers under" intensifies 悩む/怒る — low) |

**Every one of the 11 verbatim spans (4 Russian, 7 Japanese) is present at the page/section the entry's prose implies.** The only fully false factual statement I found in §1–§5 is line 54 (F1). Everything else is a gloss or a locator problem.

## 4. Table/count audit (assignment list, including the §6–§7 tables named)

| item | page count | entry count | verdict |
|---|---|---|---|
| five steps (S881 h2 → h3 1–5) | 5 | 5 (line 74; move table 84–88) | ✓ |
| four layers (S881 h2 + 4 checklist h3) | 4 | 4 (lines 107–110) | ✓ |
| five elements (S882 `info-box blue` `<li>`) | 5 | 5 (lines 130–134) | ✓ |
| note sections (S882 `info-box gold` `<li>`) | 5 | 5 (lines 142–146) | ✓ |
| magic questions (S881「魔法の設定で決めること」) | 7 | 7 (lines 182–188); "last two" = 社会への影響 / 権力との関係; page: `見落とされやすいのは最後の二つです。` | ✓ |
| distance table (S881 作り込み度合い) | 3 rows | 3 (66–68) | ✓ |
| country sheet (S881 架空の国の作り方) | 8 fields | 8 (167–174) | ✓ |
| magic/technology sheet (S881) | 7 | 7 (182–188) | ✓ |
| genre depth (S882 ジャンル別) | 5 rows | 5 (210–216) | ✓ |
| failure tables (S882 4; S881 4) | 4 / 4 | 4 / 4 (220; 222; table 224–229) | ✓ |
| depths (S881 核/背景/彩り) | 3 | 3 (202–206) | ✓ |
| per-entry fields (S881 種類/説明/ルール/関連) | 4 | 4 (154–157) | ✓ (the S882 page has no field set; the entry attributes the four to S881 — ScoutReopenS882 F4 already says this) |

No count is wrong. The only count-shaped inaccuracy is the characterisation "one-clause glosses" (F6).

## 5. FINDINGS

### F1 — MEDIUM — §2 table says the monograph does not address consistency; p. 140 states a consistency rule

- Entry line 54: `| how to keep it consistent | not addressed | one document, updated in place |`, under the table header `| Question | The scholarly source answers it | The practitioner pages answer it |` (line 48).
- The cited source says the opposite on the page the entry's own header lists (p. 140, second paragraph): `Причем их эволюция, межъязыковые контакты и заимствования, формирование диалектов и литературного языка, возникновение социальных и прочих жаргонов должны быть логично связаны с историей мира.` — the language's evolution, contacts, borrowings, dialects, literary language and jargons **must be logically connected with the world's history**. That is a setting-consistency requirement for the language layer (and p. 140 goes on: `Жизнеспособный фантастический язык не может быть не окрашен культурно`).
- Why it matters: the row is the entry's comparison of what each source adds; "not addressed" understates the monograph and, together with line 11 (F4), supports the false header claim that the book supplies "what a constructed world is, not how to build one".
- Smallest safe correction: `| how to keep it consistent | one rule, not a document practice: the language's history must be logically tied to the world's history (p. 140) | one document, updated in place |`.
- Scope/limits: does not falsify claim C (no leg reads table cells); entry-side fix.

### F2 — MEDIUM — §3 line 60 overgeneralises the page's FAQ and drops/misrenders items; "constitution" is not 政治制度

- Entry line 60: "a contemporary novel needs no magic system and no political constitution, but it still needs the town, the workplace or school, and the invented company or district, decided once".
- Page: the FAQ question is 「**現代が舞台の恋愛もの**でも世界観は必要ですか？」 and the answer is `政治制度や魔法のルールは要りません。物語の舞台になる町、登場人物の職場や学校の仕組み、人間関係の輪、そして作者が作った架空の会社・地名・学科を決めておけば…`. The same page's table has a separate 現代もの＋非日常 row `現実と違う部分と、それが隠れている理由` (例: 退魔師が働く現代の東京、能力者がいる高校), i.e. a contemporary novel **with** a power system.
- Three defects in one sentence: (a) the absolute "a contemporary novel" generalises from the FAQ's romance case and is contradicted by the page's own 現代もの＋非日常 row; (b) 政治制度 = political system/institutions, not "constitution"; (c) the list omits 人間関係の輪 and renders 地名・学科 as "district".
- Smallest safe correction: "a contemporary romance (the page's case) needs no political institutions or magic rules, but it still needs the town, the workplace or school, the web of relationships, and the invented company, place names and school departments — decided in advance".
- Corroborates ScoutReopenS881 line-60 finding (LOW there); I raise it because the 現代もの＋非日常 row is a direct counterexample on the same page.

### F3 — MEDIUM — no per-sentence page locators; the header's page list includes a page no sentence uses; committed evidence anchors only p. 7 and the row anchor is p. 10

- Entry: `grep -c '(loc:'` = 0 (section 2 above); the four S877 sentences are bare `(S877)`; the header (line 3) lists `printed pages 7, 35, 36, 139 and 140`.
- Actual mapping (section 2): 36→p. 7, 38→p. 139, 42→p. 35, 44→p. 36. **Page 140 is used by no sentence** — although p. 140 is the page whose rule F1 says the table misses.
- Simultaneously, the committed record does not cover three of the four quotes: `reports/round-74/evidence/S877.txt` is an `excerpt` window of 4,098 chars around the p. 7 quote (`before=2019 after=2025`), and the registry anchor (`corpus/SOURCES.md:832`) is the p. 10 sentence from `conlang-scholarship.md`. So the p. 35, 36 and 139 quotes are outside both the anchor and the window. Claim C's legs do not require more (EVIDENCE only requires the Gate quote; ROWS allows the reused row to change only `used-by`), but a verifier of the entry must re-fetch the 1 MB PDF to check three of its four Russian quotes.
- Smallest safe correction, entry side: append the page to each cite — `(S877 p. 7)`, `(S877 p. 139)`, `(S877 p. 35)`, `(S877 p. 36)` — and change the header list to `7, 35, 36 and 139` (or cite the p. 140 rule added by F1). Record side is append-only: no in-place anchor edit is available; a later round can add a committed window carrying pp. 35/36/139.
- Corroborates ScoutReopenS877 F6 (p. 140 unused) and the EVIDENCE-coverage concern in ScoutReopenS881 F4; the locator-convention angle (the entry vs its own amend file and vs `conlang-scholarship.md`) is this seat's.

### F4 — LOW — the header's scope sentence "the monograph … supplies what a constructed world is, not how to build one" contradicts §2

- Entry line 11: "…the monograph is tier B and supplies what a constructed world is, not how to build one".
- Entry lines 44–46 take from the same monograph "the rule the two practitioner guides open with" and call it "the strongest single design rule in this entry: the first artefact is a one-sentence premise"; line 40 takes a volume rule through the monograph's account. A source that supplies the entry's strongest build rule is not a source that supplies "not how to build one".
- Fix: "supplies what a constructed world is and one build rule (a premise precedes the picture), not a build order".
- Partly overlaps ScoutReopenS877 F3 (which treats the same tension from the "rule" side); this finding is the header sentence, not the §2 promotion.

### F5 — LOW — §1 line 20 "no citation" is true of the five-step order only, false of the page

- Entry line 20: "…no named practitioner, no cohort and no citation; the page's own product calls to action sit beside the advice".
- Page: `『指輪物語』のJ.R.R.トールキンは1939年の講演「On Fairy-Stories」で…`; `ファンタジー作家ブランドン・サンダースンは、魔法を…と述べています`; `ヘミングウェイの「氷山理論」は…`. The five-step order and the layer chain are indeed uncited.
- Fix: "no citation for the order or the chain (the page's outside references are name-drops without editions)".
- Corroborates ScoutReopenS881 F1's line-20 note.

### F6 — LOW — §1 line 21 "checklists with one-clause glosses" does not match the list items

- The five element glosses: `地理・環境：どんな地形か、複数の国や地域があるか、気候や自然環境はどうか` (3 clauses), `歴史・背景：現在の状況がなぜそうなっているか、過去にどんな出来事があったか` (2), `魔法・技術システム：何ができて何ができないか。ルール（制約）が重要` (2 sentences), `社会制度・文化：身分制度、宗教、貨幣経済、習慣など日常生活の仕組み` (1), `勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか` (2).
- Fix: "single-line glosses" (the point — no method, no citations — is unaffected). ScoutReopenS882 called the same phrase "loose … harmless"; I file it because the phrase is the calibration row's stated reason.

### F7 — LOW — §2 line 40 restates Henning's rule with a different criterion

- Entry: "a world's language layer is sized to **what the world must carry**, not to a need for talk — the same volume rule `linguistics/conlang-scholarship.md` records".
- That file: "the required size and detail of lexicon and grammar follow from **what the language is for** (S877)" (its §4, quoting Henning via the book). Use (jargon / naming / communication-literature) is the criterion there; "what the world must carry" shifts it to the world's demands while claiming to be "the same" rule.
- Fix: "sized to what the language is for (names, jargon, real talk), as the volume rule in `conlang-scholarship.md` records".

### F8 — LOW — §4 line 97 equates the page's endpoint with the chain's last layer

- Page: `最後は「登場人物がその世界でどう暮らしているか」にたどり着く必要があります。` (how a character **lives**); last layer: `個人の経験（登場人物がこの世界をどう感じるか）` (how a character **feels**).
- The entry: "how a character lives in that world — which is the four-layer chain's last layer".
- Fix: "which is what the chain's last layer, 個人の経験, is for" (or drop the identification).

### F9 — LOW — "in QUALITY 2's terms" cites a vocabulary the rule does not define

- Entry line 26: "Status vocabulary, in QUALITY 2's terms: **not mainstream — unmeasured practitioner convention; nothing here is contested or discredited**."
- `corpus/QUALITY.md:9`: "**Calibration** — every framework entry names its status: mainstream / contested / discredited, with the reason."
- "Not mainstream" is the negation of one label, and "unmeasured" is not in the set; the entry does give the reason, so the substance is honest, but the appeal to "QUALITY 2's terms" is inaccurate.
- Fix: "Status: not mainstream (unmeasured practitioner convention); none of QUALITY 2's contested/discredited applies, and no source opened here disputes another."

### F10 — LOW — the recheck line's extraction claim is false

- Entry line 7: "…re-find each quote on the printed page its sentence cites (plain mode de-hyphenates; `-layout` keeps end-of-line hyphens)".
- Observed: plain mode keeps end-of-line hyphens and the line break. `grep -c -- '-$' conlangs.txt` = 40, e.g. line 318 `…творческой деятельности огромного количе-`. This is why the p. 7 quote needed a whitespace fold (`quote-found-verbatim: no` in the evidence file) and why a re-checker who searches a de-hyphenated string will miss a hyphen-broken word.
- Fix: "plain mode keeps line breaks and end-of-line hyphens; fold whitespace and join a hyphen-broken word before matching (`-layout` only changes spacing)".

### F11 — observation (no severity) — 184 vs 185 pages

- The entry line 3 says "the whole 184-page monograph"; `pdfinfo` says `Pages: 185` (cover + 184 numbered; p. 2 imprint `2006, с.184`; registry says "185-page typeset text"). Both are true of different objects; if precision is wanted, "the 184 numbered pages of a 185-page PDF".

## 6. Corroborated peer findings I verified independently (not new)

- **HIGH — S877 cited outside the reused row's scope** (ScoutReopenS877 F1). I reproduce the evidence: the row's scope cell (`SOURCES.md:832`) reads "Tier B for the book's own framing: the classification of artificial languages (конланги), the vocabulary separating вымышленные языки …, the special status of Tolkien's languages, Klingon and D'ni, and the survey of the literature on imaginary languages"; its `teaches` cell adds "a volume rule for how much language a world needs". The entry's four S877 sentences (pp. 7, 139, 35, 36) are about world-building (language as the instrument of building worlds; ВЯ as the topic not a means of talk; the language–world modelling link; the SF premise). None of those is in the scope cell. `SOURCES.md:17-19`: "Tiers are scoped to the row's `scope`, never global." Claim C's kill rule does not read scope, so this is an entry/QUALITY defect, not a claim kill; the fix is a superseding row or an explicit out-of-scope statement in the entry (the row cannot be widened in place).
- **MEDIUM — "a constructed language" for ВЯ** (ScoutReopenS877 F2): p. 139 speaks of ВЯ (fictional languages, class 2); auxlangs (class 1) *are* means of communication in the book's own terms. Entry lines 32 and 38 both generalise.
- **MEDIUM — the premise promoted to "the rule"/"the strongest single design rule"** (ScoutReopenS877 F3): p. 36 describes a genre feature ("по его мнению"), p. 35 says the direction is free, and the entry's own line 42 reports that. "One-sentence" is not on the page.
- **LOW — the evidence window cannot re-verify most of the entry's S881/S882 citations** (ScoutReopenS881 F4): I confirm the S877 window is an excerpt around p. 7 and the S882 window is whole-document (2,953 chars); the S881 4,098-char excerpt is confirmed by its header and the sibling report.

## 7. Attacks that FAILED (the claim survived)

1. **Hash/bytes drift** — all three artefacts byte-identical to the entry, the rows and the evidence files (1,055,723 / 101,615 / 17,068 bytes; three sha256s).
2. **Quote absent or altered** — 11/11 verbatim (after a whitespace fold for the two line-broken Russian spans); each of the four Cyrillic quotes occurs on exactly one PDF page, matching the implied page (7/139/35/36).
3. **Wrong page/heading for a Japanese quote** — every S881 quote is on the section the sentence names (h2 世界観とは; h2 5つのステップ; h3 5; h3 3; h2 4つの層; 第4層; FAQ); every S882 quote is in the box/list the source line names.
4. **Wrong table counts** — 5 steps, 4 layers, 5 elements, 5 note sections, 7 magic questions, 3 distance rows, 8 country fields, 5 genre rows, 4+4 failures, 3 depths: all match.
5. **Misattribution between the three sources** — none: S877 carries only §2, S881 §3–§5, S882 §4 and §1; no S882 claim is sourced to S881 or vice versa.
6. **Author/date/byline** — S881 JSON-LD author is the Organization LitMemo (no person), visible 2026-07-16 / 最終更新 2026-10-23; S882 author is つづく編集室, 約1,100文字, 2026年3月12日. All carried.
7. **No-capture claim (CDX)** — reproduced: `litmemo.com/ja/blog/novel-worldbuilding-guide` exact → `[]`; `tuduku.space/column/novel-worldbuilding` exact → `[]`; `tuduku.space/*` → `[]`; positive control on the same endpoint, `litmemo.com/ja/blog/` prefix → one row (`novel-character-relationship-map` @ 20260911102425). The probes were run with the browser-shaped UA; one `tuduku.space` domain call timed out once and the retry answered `[]`. (The host-level litmemo `worldbuilding-cr8k19h0.js` control is in ScoutReopenS881 §5, not re-run by me.)
8. **Ground claims** — re-derived at base: `git ls-tree -r --name-only f7104cb corpus/knowledge | grep -ciE 'worldbuilding|setting-practice'` = 0; `git grep -lE '設定ノート|世界観|世界观' f7104cb -- corpus/knowledge | wc -l` = 0; `git show f7104cb:corpus/SOURCES.md | grep -c 'litmemo.com\|tuduku.space\|chinawriter.com.cn'` = 0.
9. **The LitMemo FAQ sentence is absent** (attack on §3) — it is present: `決めておくのは、展開に直接かかわる核の設定だけで十分です。` in the FAQ, and the "現代が舞台の恋愛もの" answer carries 政治制度や魔法のルールは要りません. The §3 sentence is only over-broad, not invented (F2).
10. **The p. 140 page is not about consistency** (attack on F1) — it is: the quoted `должны быть логично связаны с историей мира` is on printed p. 140, second paragraph.

## 8. Impacted axes and smallest safe corrections

- **Coverage (claim C's entries):** no quote or count fails; the entry's content fidelity holds for §1–§5 except F1/F2. F1 and F2 are one-cell/one-sentence edits.
- **Calibration:** F7/F9 are wording; F3/F4 are provenance/scope. The HIGH (section 6) is a scope statement, not a data error.
- **Claim status:** none of this falsifies claim C's declared legs (ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX). The HIGH is a QUALITY/scope defect in the entry, not a claim-counter failure; the canonical judge can accept C while the next round routes the entry fix through the append-only route (new superseding S877 row scoping pp. 7/35/36/139–140, or the entry's own qualification).
- **Fix order:** F1 (one cell) → F2 (one sentence) → F3 (four parentheticals + header list) → F4 (one header clause) → F5–F10 (wording).

## 9. Scope, tools, limits

- Read: the frozen claims, the entry, the registry rows S877/S881/S882, the evidence windows, `corpus/QUALITY.md`, `conlang-scholarship.md`; fetched the three artefacts fresh with the UA above.
- §6–§10 were read only for the named table counts (five elements, note sections, magic questions, country sheet, genre table, failures); their sentences were not audited sentence-by-sentence by this seat. §1–§5 is the assignment.
- The S877 PDF text extraction used `pdftotext -enc UTF-8` (poppler) and a folded search; `-layout` was used once as a cross-check.
- Tools installed: none. No pacman, no package manager, no background job, no subagent.
- Not exercised: `accept-c.py`, `accept-ca.py` (not this seat's attack); the S877 Wayback carrier (`20260208005339`) was not re-fetched because the live bytes already equal the recorded hash (the sibling seat did re-fetch it byte-identically).

## 10. Raw evidence commands (for the findings)

F1 — the p. 140 rule:

```
$ python3 - <<'EOF'
pages=open('conlangs.txt',encoding='utf-8').read().split('\f')
p=pages[139]; i=p.find('должны быть логично')
print(p[max(0,i-60):i+190])
EOF
Историю имеют и фантастические языки.
Причем их эволюция, межъязыковые контакты и заимствования, формирование диалектов и литературного языка, возникновение социальных и
прочих жаргонов должны быть логично связаны с историей мира34. Таким
```

F2 — the FAQ answer and the page's own 現代もの＋非日常 row:

```
$ python3 - <<'EOF'
t=open('s881.txt',encoding='utf-8').read()
i=t.find('政治制度や魔法のルールは要りません')
print(t[i-140:i+200].replace('\n',' | '))
EOF
？ | 決めておくのは、展開に直接かかわる核の設定だけで十分です。… | 現代が舞台の恋愛ものでも世界観は必要ですか？ | 必要ですが、決める量はずっと少なくなります。政治制度や魔法のルールは要りません。物語の舞台になる町、登場人物の職場や学校の仕組み、人間関係の輪、そして作者が作った架空の会社・地名・学科を決めておけば、前後の食い違いを防げます。 | 読者は設定の整合性をそんなに気にしますか？ | 気…

$ python3 - <<'EOF'
t=open('s881.txt',encoding='utf-8').read()
i=t.find('現代もの＋非日常'); print(t[i-40:i+140])
EOF
もの
地理・歴史・政治・魔法までほぼすべて
剣と魔法の王国、異世界転生先の世界
現代もの＋非日常
現実と違う部分と、それが隠れている理由
退魔師が裏で働く現代の東京、能力者がいる高校
現代もの
作者が手を加えた部分
架空の会社、架空の町、実在しない部活や学科
```
(the first line is the tail of 「異世界もの」; the table cells are one per line in the plain extraction)

F3 — locators (section 2 above for the commands) and the exact page mapping:

```
$ python3 - <<'EOF'
import re
pages=open('conlangs.txt',encoding='utf-8').read().split('\f')
def n(s): return re.sub(r'\s+',' ',s).strip()
for q in ['Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и социальных реалий',
          'ВЯ в общем случае не служит средством коммуникации, он является предметом, темой коммуникации',
          'связь между лингвоконструированием и моделированием миров неразрывна',
          'некое научное или не совсем научное допущение']:
    print([i+1 for i,p in enumerate(pages) if n(q) in n(p)])
EOF
[7]
[139]
[35]
[36]
```

F5 — the page's outside references (against "no citation"):

```
$ grep -o 'トールキンは1939年の講演[^。]*' s881.txt
トールキンは1939年の講演「On Fairy-Stories」で、作者が創る世界を「第二の世界（Secondary World）」と呼びました
$ grep -o 'ブランドン・サンダースンは[^。]*' s881.txt
ブランドン・サンダースンは、魔法を「ハードマジック」と「ソフトマジック」に分けて論じ、「作者が魔法で対立を解決してよい度合いは、読者がその魔法をどれだけ理解しているかに比例する」と述べています
$ grep -o 'ヘミングウェイの「氷山理論」[^。]*' s881.txt
ヘミングウェイの「氷山理論」は世界観にも当てはまります
```

F6 — the five element glosses:

```
$ sed -n '21,26p' s882.txt
世界観設定の5要素
地理・環境：どんな地形か、複数の国や地域があるか、気候や自然環境はどうか
歴史・背景：現在の状況がなぜそうなっているか、過去にどんな出来事があったか
魔法・技術システム：何ができて何ができないか。ルール（制約）が重要
社会制度・文化：身分制度、宗教、貨幣経済、習慣など日常生活の仕組み
勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか
```

F10 — plain-mode hyphen retention:

```
$ grep -c -- '-$' conlangs.txt
40
$ sed -n '318p' conlangs.txt
образованию, дали импульс творческой деятельности огромного количе-
```

Counts audit — the seven magic questions and the eight country fields on the page:

```
$ grep -n '源：力はどこから\|できること・できないこと：\|代償：使うと\|使える人：\|段階と上限：\|社会への影響：\|権力との関係：' s881.txt
225:源：力はどこから来るか。生まれつき、修行、契約、道具
226:できること・できないこと：先に「できないこと」を決めるほうが早い
227:代償：使うと何を失うか
228:使える人：どのくらいの人が使えるか。生まれで決まるか
229:段階と上限：力に段階はあるか、上がる条件は何か、最強の使い手でもできないことは何か。長編では、これを決めないまま進むと中盤以降に強さのインフレが起きます
230:社会への影響：治癒魔法があるなら医者はいるのか、空を飛べるなら城壁に意味はあるのか
231:権力との関係：使い手は敬われているか、恐れられているか。管理する組織はあるか
$ sed -n '/架空の国の作り方/,/架空世界の作り込み度合い/p' s881.txt | grep -cE '^(国名と由来|位置と地形|政体|隣国との関係|産業と通貨|信仰|言語と名前|国の傷)$'
8
```


