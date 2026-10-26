# ScoutReopenS882 — independent re-open of lane row S882 (tuduku.space) and its Gate record

Seat: kotodama round 74 wave 2, falsify. Scope read-only; scratch at /tmp/ScoutReopenS882/ (body.html, headers.txt, text2.txt, window.txt, ext.py). Landed bytes checked: `git diff --stat c4bf61a8… main -- corpus/SOURCES.md corpus/knowledge/culture-material/worldbuilding-setting-practice.md reports/round-74/evidence/S882.txt` printed nothing (no drift since claim C lands); evidence file sha256 at c4bf61a = working tree = `e6030849c25eabb7ee742ba4f100977d8b02599191d21cf4c440d4b58e9f7da7`.

## 1. Re-fetch lines (QUALITY 21/22/24)

UA (every fetch of the page): `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
date -u → 2026-10-26T02:00:01Z
curl -sS -L --compressed --connect-timeout 20 --max-time 90 -A "<UA>" -o body.html -D headers.txt -w "%{http_code}\n%{url_effective}\n%{size_download}\n" https://tuduku.space/column/novel-worldbuilding
→ 200 / https://tuduku.space/column/novel-worldbuilding / 6260   (size_download on the wire; gzip)
wc -c body.html → 17068 body.html
sha256sum body.html → 754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7
headers: HTTP/2 200; content-type text/html; content-length 6260; content-encoding gzip; last-modified Wed, 24 Jun 2026 14:05:19 GMT; server Apache
```

First attempt succeeded (no SSL reset this time; fetch-attempts=1).

**Hash equality: YES.** 17,068 bytes, sha256 754f504c… equals the evidence file (`bytes: 17068`, `sha256: 754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7`), the row (17068 bytes), the entry header and the lesson Gate line. Nothing moved between the 2026-10-25 capture and mine. `Last-Modified: 24 Jun 2026` matches the row's "Last-Modified 2026-06-24". JSON-LD `datePublished` 2026-02-25 matches; the visible dates 2026年3月12日 (published) and 最終更新 2026年3月12日 match the row's "visible date".

## 2. Quote located verbatim: **Y**

Quote «勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか» = 33 characters (`python3 len()` = 33), 1 whitespace token (no ASCII space inside). Location in the raw HTML: `<ul>` of `<div class="info-box blue">`, label `<div class="ib-label">世界観設定の5要素</div>`, under `<h2>世界観設定に必要な5つの要素</h2>`, 5th `<li>`: `<li><strong>勢力図・人間関係の構造</strong>：誰が権力を持ち、何が対立の軸になっているか</li>` (occurs once in the page, `b.count('勢力図')` = 1). In the extracted visible text it begins at offset 631 (631 + 33 = 664) of the 2,953-char window. The quote crosses a `<strong>` boundary, so it is contiguous only after inline tags are removed; the lane's extractor keeps inline tags inline (correct), and mine matched it at the same offset.

The row's second anchor quote 「世界地図・地名一覧：手書きでよいので地図を描いておく」 = 26 characters (`len()` = 26), 1 token, found once, 1st `<li>` of the `info-box gold` list labelled 設定ノートの構成例 under `<h2>設定ノートの作り方｜管理と整理の実践法</h2>`. Row anchors confirmed.

## 3. Window equality (whole document, 2953 chars)

- Stored window (between `--- window ---` and `--- quote ---` in evidence/S882.txt): 2953 characters, 8410 UTF-8 bytes, sha256 `a055a24ce2ced7714cea69b342cd2f40c09d85d14c985c3ddc30c1a74d82289f` = the file's `window-sha256:` (recomputed: equal). `window-bytes: 8410` equal.
- My extractor (stdlib html.parser, the evidence file's stated rule: drop comments/script/style/noscript/template/svg/head, block tags → newline, blank lines dropped, ASCII-space runs collapsed) → 2953 characters when the surviving lines are joined by one space; `window == ' '.join(lines)` → **True**. (Joined by `\n` the same text is also 2953 characters; the stored window is the space-joined form.)
- Independent second extractor (BeautifulSoup 4.15.0, `decompose()` of the same dropped tags, `get_text('\n')`): non-whitespace characters 2826; stored window non-whitespace characters 2826; the whitespace-stripped strings are **identical**. So the window is the whole extracted page, nav, footer, CTA and related-links included, not a body-only slice.
- Geometry: before 631 + quote 33 + after 2289 = 2953 (header: `before=631 after=2289 pad=400`). `window-scope: whole-document` is correct. Hidden-content check: no `display:none`, `aria-hidden`, `hidden` or `visibility:hidden` in the HTML; HTML comments are only the gtag, Yahoo tag and `/.article-body` closer. The only text excluded from the window is head metadata and scripts.
- Body-only count for context: lines 18-113 of the extracted text (lead paragraph through 注意点 box) = 2,580 characters including newlines, 2,471 non-whitespace.

Attack on the window FAILED: the window equals the visible text.

## 4. Counts the entry states

| Count | Page | Entry | Verdict |
|---|---|---|---|
| five elements | `info-box blue` has 5 `<li>`: 地理・環境 / 歴史・背景 / 魔法・技術システム / 社会制度・文化 / 勢力図・人間関係の構造 | line 126 "five elements", table at 128-134 (5 rows, same order) | carried |
| five note sections | `info-box gold` has 5 `<li>`: 世界地図・地名一覧 / 年表・歴史 / 魔法・能力一覧 / 人物一覧 / 社会制度・用語集 | table at 140-146 (5 rows, same order); line 53 "five note sections"; row cell "five-item settings note" | carried |
| five steps | `<ol>` with 5 `<li>` | line 78 "five-step order" (S882) | carried |
| four fields | **not on the S882 page.** The page's note has sections, not a per-entry field set. Per-section content varies: 魔法・能力一覧 names 能力・制約・習得条件 (3), 人物一覧 names 名前・年齢・外見・性格・役割・他キャラとの関係 (6) | line 150 attributes 種類 / 説明 / ルール / 関連 to **S881** (LitMemo); line 159 "five sheets, and four fields inside every entry" has no id | The count is correct as attributed (S881). It is NOT an S882 count. See F4. |
| four failures | failure table `<tbody>` has 4 rows: 設定過多, 設定不足, 設定の押し付け, 設定の未活用 | line 220 "four ways" (S882) | carried (but see F5) |
| five genre rows | table has 5 rows: 異世界ファンタジー, 現代恋愛, SF・近未来, 歴史改変, 学園もの | table at 210-216 under line 208 (S882) | carried; the cells match: 魔法システム・身分制度・地理 / 高め（矛盾が目立ちやすい）, 低め（現実世界ベース）, 高め（読者の検証が厳しい）, 中程度（史実知識が下支え）, 低〜中程度 |

## 5. Tier verdict: **AGREE with kind `community`, tier C.**

Reasons observed: JSON-LD `author` and `publisher` are both the Organization つづく編集室, so there is no named person; the page ends in a CTA ("無料相談フォームへ →", "FEEDBACK & SUPPORT") and a 特定商取引法 footer, so it is a company marketing column; it gives no source, data or method for any of its lists; the page's own length claim (約1,100文字) is wrong against the measured 2,953 characters (F5), which is weak evidence of editorial care. SOURCES.md line 17-19 defines C as "lead only, never sole support for an admitted entry"; the row's scope cell says "so a lead and never sole support", and the entry's calibration table (line 21) and `sources:` line (11) say the same. B would be unsupportable: no named expert, no reproducible detail. The entry's own reporting stance ("what the page prescribes") fits tier C. `mined` status is consistent with `used-by` naming the entry that cites S882.

## 6. Every entry sentence that cites S882 (grep of the tree: the only landed file with the id is corpus/knowledge/culture-material/worldbuilding-setting-practice.md; the other `S882` hits in corpus/lessons/round-72/73 are the older numbering for other documents)

| Line | Sentence (shortened) | Carried by page? |
|---|---|---|
| 5 | header: 17,068 bytes, sha256, "no capture of this slug or host in CDX"; lists 5要素 and 構成例 list boxes, failure table, key-point box | bytes/hash Y; CDX claim Y (§7); **list of locators incomplete** (F2) |
| 78 | five-step order: core concept in one sentence; protagonist's day waking to sleeping; deepen only story-relevant parts; contradiction check against past episodes; reader's "why not just…" objection | Y — all five `<li>`s (コアコンセプトを一文で決める / 主人公の日常… 起きてから寝るまで / 物語に関わる部分だけ深掘り / 矛盾チェック… 過去のエピソードと照合 / 読者からのツッコミ… 「なぜ〇〇しないのか」) |
| 126 | opens its list with five elements; fifth in full form "勢力図・…か" | Y, verbatim |
| 136 | "特に重要なのは魔法・技術システムの「制約」です。" | Y, verbatim (`特に重要なのは<em>魔法・技術システムの「制約」</em>です。`) |
| 138 | "魔法・技術システム：何ができて何ができないか。ルール（制約）が重要" | Y, verbatim (third `<li>`) |
| 148 | "世界地図・地名一覧：手書きでよいので地図を描いておく" | Y, verbatim |
| 208 | "calibrates the same axis by genre" | Y (h2 ジャンル別：設定の深さの目安 and its table) |
| 218 | "世界観設定は「作者が知っていること」と「読者に伝えること」を分けて考えましょう。" | Y, verbatim, inside `class="key-point"` box labelled KEY POINT |
| 220 | failure table names four ways: too much at opening; too little so contradictions appear; spoken aloud by characters; built and never used | Y (rows 1-4; symptom cells 冒頭から世界観説明が続く / 物語の途中で矛盾が発生する / キャラが世界の説明をわざとらしく語る / 作り込んだ設定が物語に活かされていない) |

Lines that name the tuduku page without an id, and what the page does and does not carry:

- 80 "they differ at the outward-causal step, which only the LitMemo page has, and at the last, where tuduku adds the objection check": consistent with the five steps (tuduku has no causal step; its 5th is the objection check). Interpretive, uncited.
- Table 82-88, tuduku column: every cell matches a step/element on the page (see line 78). Row 3's "its 歴史・背景 element asks why the present is as it is" = page "現在の状況がなぜそうなっているか".
- 128-134 column 2 "What the page puts in it": matches the page glosses (terrain, how many states or regions, climate / why the present is as it is, what happened / what is possible and impossible; the constraints / status, religion, money economy, custom / who holds power, what the conflict axis is).
- 140-146 column 2 "What it holds": matches the page (dated events in sequence; each ability with its constraint and acquisition condition; name, age, appearance, temperament, role, relations; invented trades, ranks, religions, currency units).
- 21 "marketing column of about 1,100 characters by its own count, no byline beyond the service name, checklists with one-clause glosses": the page prints 約1,100文字; the byline is the service name つづく編集室. The word "one-clause" is loose: 魔法・技術システム gloss is two sentences ("何ができて何ができないか。ルール（制約）が重要"). Harmless.

**Sentences citing S882 that the page does NOT carry: none.** Every S882-tagged sentence is carried. The page-uncarried material is in the untagged table columns (F1) and in the SOURCES row's "six-item" phrase (F3).

## 7. "No capture" ruling (QUALITY 21/24): holds

Probes (CDX, browser-shaped UA, http://web.archive.org/cdx/search/cdx, 2026-10-26):

```
url=tuduku.space/column/novel-worldbuilding&output=json&limit=5&matchType=exact → [] HTTP 200
url=tuduku.space/column/novel-worldbuilding&matchType=prefix&limit=5&output=json → [] HTTP 200
url=tuduku.space&matchType=domain&limit=5&output=json → [] HTTP 200
url=www.tuduku.space/column/novel-worldbuilding&limit=5&output=json → [] HTTP 200
url=tuduku.space/column/novel-worldbuilding.html&limit=5&output=json → [] HTTP 200
positive control: url=example.com&output=json&limit=5&matchType=exact → header row + 5 rows, first ["com,example)/","20020120142510","http://example.com:80/","text/html","200","HT2DYGA5UKZCPBSFVCV3JOBXGW2G5UUA","1792"] HTTP 200
positive control (domain mode, the same query form as the host probe): url=example.com&matchType=domain&limit=2&output=json → 2 rows HTTP 200
availability API https://archive.org/wayback/available?url=… → HTTP 429 (rate limited; not used)
```

(One `matchType=domain` call returned HTTP 503 "Temporarily Offline" earlier in the session and was repeated; the repeat answered 200 `[]`.) Ruling: no capture of the slug or the host, with live controls. The attack on the row's "no Wayback capture" and the entry's "no capture of this slug or host in CDX" FAILED. The lane's own probe is in .ufo/waves/round-74/w1/ScoutTuduku.md §6 and ScoutWayback.md (seven tuduku URL forms, controls present), and my results agree.

Recheck command (lesson Gate line 106): `grep -c '設定ノートの構成例' body.html` → 1; `grep -o … | wc -l` → 1. Still returns the stated 1.

## FINDINGS

**F1 — MEDIUM — uncited authorial claims sit in the S882 tables.** Entry lines 128 and 140 add the third columns "Artefact it forces" and "Why it is a separate sheet" to tables whose first two columns are the page's content. Column 3 is not on the page and has no S-id: "a faction and relation diagram" (the page says only 勢力図), "the map is the cheapest consistency check there is" (142), "chronology is the first thing to drift in a long work" (143), "powers inflate unless their ceiling is written down" (144), "relations are the facts readers catch first" (145), "one glossary prevents one object acquiring three names" (146). Command: `grep -n -E "cheapest consistency|first thing to drift|powers inflate|readers catch first|three names" corpus/knowledge/culture-material/worldbuilding-setting-practice.md` → lines 142-146; `grep -c -E 'ドリフト|インフレ|ブレ|別名' text2.txt` (page text) → 0. The page does say in general that a settings note keeps consistency (extracted-text lines 57, 67) but gives no per-sheet reason of this kind. A reader of line 126/148 ("the page …") takes the table as the page's. Proposed fix: relabel column 3 "Design reason (this entry's inference, not the page's)", or add one sentence before each table saying the third column is inference, or cite a source that supports each reason.

**F2 — LOW — the entry's `source:` line for S882 (line 5) omits three S882-cited locations.** It names the two list boxes, the failure table and the key-point box. It does not name: the 実践ステップ `<ol>` under h2「世界観構築の実践ステップ｜何から始めるか」 (cited at line 78 and in the table at 82-88), the genre table under h2「ジャンル別：設定の深さの目安」 (cited at 208, table 210-216), and the `<em>` paragraph 特に重要なのは…「制約」です (cited at 136). The `recheck:` line (7) tells the re-checker to "re-check the h2 and box labels named on the source lines", so those three citation sites have no label to re-check. Proposed fix: add the three locators to line 5 (a dated amendment; the `source:` line is provenance, not an append-only row).

**F3 — LOW — the SOURCES.md S882 teaches cell (line 837, column `teaches`) carries a phrase the page cannot support.** "…not six; … the five- and six-item counts are the page's own, not a standard". The page has no six-item list (the page counts are 5 elements, 5 note sections, 5 steps, 4 failure rows, 5 genre rows); `grep -n -E '6|六|６'` of the extracted text matches only the dates 2026年3月12日 (twice) and © 2026. The word "six" appears nowhere in the entry (`grep -n six worldbuilding-setting-practice.md` → no output). It is a leftover of the staged text. The row is append-only (only status/recheck/used-by change in place), so the fix is a dated correction in the next lesson plus, if the lane permits, a superseding row; at minimum a lesson line saying "six" in row S882 refers to nothing on the page.

**F4 — LOW — "four fields" is an S881 count, not an S882 one.** The task's count of four fields is carried by LitMemo (line 150, S881). S882's note has five sections and no per-entry field set. Entry line 159 ("five sheets, and four fields inside every entry") and the `topic:` line (9) join the two counts without an id. Not an error, because line 150 attributes the field set to S881 and the sentence is design consequence, but anyone checking "four fields" against the tuduku page will find none. Proposed fix: in line 159 write "five sheets (S882) and four fields inside every entry (S881)".

**F5 — LOW — two page-internal inconsistencies the entry does not flag.** (a) The page's intro to the failure table says 失敗は大きく2種類 and then the table lists four types; entry line 220 says "four ways", which is the table's count and is correct, but a reader checking the page's prose finds "2". (b) Entry line 21 carries the page's "about 1,100 characters" as the page's own count; the measured extraction is 2,953 characters (2,826 non-whitespace; 2,471 in the article body lines 18-113), about 2.3–2.7 times the claim. The phrase "by its own count" is accurate; the measured number is not recorded anywhere in the entry, although it is the number the evidence file already holds. Proposed fix: add "(measured 2,953 characters extracted, 2026-10-25)" to the line-21 cell, and a clause on the 2-vs-4 inconsistency in line 220.

**F6 — LOW — the CDX probe for S882 is recorded only in a wave-1 scout file.** The S881 source line says "the Internet Archive CDX holds no capture of this slug, probed 2026-10-25"; the S882 line says "no capture of this slug or host in CDX" with no probe date, and neither evidence/S882.txt nor the lesson Gate row names the probe. The probes are in .ufo/waves/round-74/w1/ScoutTuduku.md §6 and ScoutWayback.md, and my re-run agrees (§7), so the claim is true, but the entry's durable carrier lacks the date. Proposed fix: add "probed 2026-10-25" to line 5, as the S881 line does.

## Attacks that FAILED (the claim survived)

1. Hash/bytes: page unchanged, 17068 B, sha256 754f504c… equal in four places.
2. Quote found verbatim, once, at the stated locator; second row quote also verbatim.
3. Window = whole document: 2953 characters, recomputed window-sha256 equal, equal to a second independent extractor on non-whitespace characters; 631 + 33 + 2289 = 2953.
4. Every S882-tagged entry sentence is carried by the page (8 cited sentences plus the header, §6 table).
5. Counts: five elements, five note sections, five steps, four failures, five genre rows all match the page.
6. Tier C / community: agreed.
7. No-capture ruling: holds under a canonical-slug probe plus positive controls.
8. Landed files unchanged from c4bf61a to main for the entry, the registry and the evidence file.

I did not run the counters accept-c.py/accept-ca.py (outside this seat's attack). Tools installed: none (BeautifulSoup 4.15.0 was already present).
