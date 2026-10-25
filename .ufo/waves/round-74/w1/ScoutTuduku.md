# ScoutTuduku — re-open of staged S884 (tuduku.space, 世界観設定の5要素 / 設定ノートの構成例)

Seat: leaf scout, wave 1, round 74. Writes only this file and /tmp/ScoutTuduku/. No tool installed (none needed). No fleet/lane state mutated; staged package and claims.json read only.

## VERDICT: ADMIT (tier C, community)

Reason: the page is live, openly served (HTTP 200 under a browser UA), and carries both sections the staged row names; every substantive term in the staged row is on the page. Two staged-text defects must be corrected on landing: (1) the staged row and staged entry say "six tables" but the page's 設定ノートの構成例 lists FIVE items; (2) the staged row/entry shorten four labels and the fifth element (勢力図 for 勢力図・人間関係の構造; 年表 for 年表・歴史; 能力一覧 for 魔法・能力一覧; 制度・用語集 for 社会制度・用語集) — fine as paraphrase, not as verbatim quotes. The staged row's only quoted spans (the two section labels) ARE verbatim; there is no URL↔quote mispairing on this row (unlike staged S899/S900).

Flip conditions: ADMIT → REFUSE if the page at landing time no longer contains `世界観設定の5要素` and `設定ノートの構成例` (re-run the recheck below), or if the admitted entry/row keeps "six tables"; ADMIT → UNVERIFIABLE if the host starts walling the browser UA. Tier stays C: a company-run editorial-service marketing column (つづく編集室, CTA "無料相談フォームへ →"), no named author, page self-declares 約1,100文字 — a practitioner lead, never sole support.

## 1. Fetch (exact commands and raw output)

UA used (exact): `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` (I did not try the plain-curl UA; the browser UA succeeded first try, so no wall to rule on).

```
$ mkdir -p /tmp/ScoutTuduku && cd /tmp/ScoutTuduku
$ curl -sS -L -A "$UA" -o page.html -D hdr.txt -w 'HTTP %{http_code} bytes=%{size_download} url=%{url_effective}\n' https://tuduku.space/column/novel-worldbuilding
HTTP 200 bytes=17068 url=https://tuduku.space/column/novel-worldbuilding
$ cat hdr.txt
HTTP/2 200
date: Mon, 26 Oct 2026 00:09:17 GMT
content-type: text/html
content-length: 17068
server: Apache
content-location: novel-worldbuilding.html
vary: negotiate,Range,Accept-Encoding
tcn: choice
last-modified: Wed, 24 Jun 2026 14:05:19 GMT
accept-ranges: none
$ sha256sum page.html
754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7  page.html
$ wc -c page.html
17068 page.html
```

Files (all /tmp/ScoutTuduku/): page.html (17068 B, raw), hdr.txt, text.txt (tag-stripped text, my own extraction, 9022 B), row.txt (proposed row). Fetch date: 2026-10-25 local (Date header 2026-10-26T00:09:17Z). No redirects (url_effective = requested URL).

Page metadata from the raw HTML: `<title>` and `<h1>` = `Web小説の世界観・設定の作り方｜読者を没入させる世界構築の手順と注意点` (title adds ` | つづく編集室`); `rel=canonical` = `https://tuduku.space/column/novel-worldbuilding`; author meta = `つづく編集室`; visible date 2026年3月12日 (updated 2026年3月12日); JSON-LD `datePublished` and `dateModified` = 2026-02-25 (mismatch with the visible date, inside the page itself); HTTP Last-Modified 2026-06-24; visible `約1,100文字`.

## 2. Section locations and the order in which the page lists the elements

Structure (h-tags from raw HTML): h2 `世界観設定に必要な5つの要素` (raw line 140) → info-box label `世界観設定の5要素` (raw line 144; list lines 146-150) → h2 `設定過多・設定不足の典型的な失敗パターン` → h2 `設定をストーリーに自然に溶け込ませる方法` → h2 `設定ノートの作り方｜管理と整理の実践法` (raw line 195) → info-box label `設定ノートの構成例` (raw line 199; list lines 201-205) → h2 `ジャンル別：設定の深さの目安` → h2 `世界観構築の実践ステップ｜何から始めるか`.

世界観設定の5要素 (page order; verbatim item text from the `<li>`):
1. 地理・環境：どんな地形か、複数の国や地域があるか、気候や自然環境はどうか
2. 歴史・背景：現在の状況がなぜそうなっているか、過去にどんな出来事があったか
3. 魔法・技術システム：何ができて何ができないか。ルール（制約）が重要
4. 社会制度・文化：身分制度、宗教、貨幣経済、習慣など日常生活の仕組み
5. 勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか

Answer to "listed as the page orders them": YES — the staged row's order 地理・環境 / 歴史・背景 / 魔法・技術システム / 社会制度・文化 / 勢力図 matches the page's order 1-5. Only the fifth label is truncated (the page's is `勢力図・人間関係の構造`).

設定ノートの構成例 (page order; verbatim):
1. 世界地図・地名一覧：手書きでよいので地図を描いておく
2. 年表・歴史：「○年前に魔王が現れた」などの時系列を整理
3. 魔法・能力一覧：各スキル・魔法の能力・制約・習得条件
4. 人物一覧：名前・年齢・外見・性格・役割・他キャラとの関係
5. 社会制度・用語集：独自の職業・身分・宗教・貨幣単位など

FIVE items, not six. The staged row's teaches cell ("the six tables a settings note should hold") and staged entry §4 heading ("The five elements and the six tables") are wrong on the count; the staged entry's own list under it names five. The page also says the note is kept in "NotionやGoogleドキュメントなどのデジタルツール" — it is a bullet list of note sections, not "tables".

Related page content: `特に重要なのは魔法・技術システムの「制約」です。` — a usable extra anchor for the constraint rule.

## 3. Per-span verdicts for the staged row (S884) and the staged entry

Method: Python `str.count` over raw HTML and over tag-stripped text, plus `grep -F` on text.txt.

Staged row S884 — quoted/bracketed spans:

| span (as in the staged row) | verbatim on page? | where | note / replacement |
|---|---|---|---|
| 「Web小説の世界観・設定の作り方｜読者を没入させる世界構築の手順と注意点」 | YES | `<title>`, `<h1>`, og:title, JSON-LD headline (5 raw hits) | exact incl. fullwidth ｜ |
| 「世界観設定の5要素」節 | YES (as a box label, not a heading) | info-box label, raw line 144; the section h2 is `世界観設定に必要な5つの要素` | call it the "5要素 box under h2 世界観設定に必要な5つの要素" |
| 「設定ノートの構成例」節 | YES (box label, not a heading) | info-box label, raw line 199; the section h2 is `設定ノートの作り方｜管理と整理の実践法` | likewise |
| 地理・環境 / 歴史・背景 / 魔法・技術システム / 社会制度・文化 | YES | element items 1-4 | exact |
| 勢力図 | substring only | item 5 is `勢力図・人間関係の構造` | write the full label |
| 世界地図・地名一覧 | YES | note item 1 | exact |
| 年表 | substring only | item 2 is `年表・歴史` | write `年表・歴史` |
| 能力一覧 | substring only | item 3 is `魔法・能力一覧` | write `魔法・能力一覧` |
| 人物一覧 | YES | note item 4 | exact |
| 制度・用語集 | substring only | item 5 is `社会制度・用語集` | write `社会制度・用語集` |
| "six tables" | NO — page lists 5 items | 構成例 box | replace with "five sections" |
| recheck `curl ... \| grep -c '設定ノートの構成例'` -> 1 | YES | I ran the equivalent line count on the saved raw file: 1 | recheck valid |
| "page as served 2026-10-23" | cannot verify the old fetch | — | today's bytes carry both sections; JSON-LD 2026-02-25 / Last-Modified 2026-06-24 predate 2026-10-23, consistent with an unchanged page |

Staged row cell hygiene problems (not page problems): the recheck cell contains an escaped pipe (`\|`) — the claim's kill_rule forbids an "escaped pipe" in an appended row; the opened cell is 2026-10-23 and must be 2026-10-25; the staged row carries no verbatim anchor quote with a word count (supplied below).

Staged entry (worldbuilding-setting-practice.md) on this source: `source: S884 — https://tuduku.space/column/novel-worldbuilding — 世界観設定の5要素・設定ノートの構成例 — fetched 2026-10-23` and §4 "The five elements and the six tables — from S884: 地理・環境, 歴史・背景, 魔法・技術システム, 社会制度・文化, 勢力図; and the settings note that holds 世界地図・地名一覧, 年表, 能力一覧, 人物一覧, 制度・用語集." Staged ids in the entry (S882, S883, S884) are staged-namespace: staged S884 → lane S882, staged S883 → lane S881, staged S882 (philol.msu.ru conlangs.pdf) → lane S877 (lane row S877 confirmed at corpus/SOURCES.md line 832: Сидорова/Шувалова, philol.msu.ru/~sidorova/files/conlangs.pdf). The entry's recheck line points to round 2's `SOURCES-PROPOSED.md` of the shokuknow campaign, not a lane artefact. The entry's claim that S884 "is never the sole support: S882, a tier-B row, states the scholarly framing" concerns a different document: lane S877 is a conlang monograph, and its row does not obviously state scholarly framing of setting method — [INFERENCE] from the row text only; I did not read that source — so treat the tier-B pairing as unverified.

The staged amend file (worldbuilding-setting-practice.amend-2026-10-23.md) does not cite S884 (it cites S899, S900, S895); it calls round 2's S742/S743 the "layers" and "notes" — those are campaign ids, not lane ids.

## 4. Located quotes (<=25 words, verbatim, with location, counts)

Japanese has no inter-word spaces, so each quote is 1 whitespace token under `wc -w`; characters from `wc -m`. Each quote was confirmed with `grep -c -F` on /tmp/ScoutTuduku/text.txt (= 1) and Python `in`.

Q1 (elements, item 5): 「勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか」
Location: info-box `世界観設定の5要素` under h2 `世界観設定に必要な5つの要素`, list item 5, raw line 150. `wc -w -m` → 1 word-token, 33 characters. (In raw HTML the label is wrapped in `<strong>…</strong>：`, so the contiguous string exists only in tag-stripped text.)

Q2 (note, item 1): 「世界地図・地名一覧：手書きでよいので地図を描いておく」
Location: info-box `設定ノートの構成例` under h2 `設定ノートの作り方｜管理と整理の実践法`, list item 1, raw line 201. `wc -w -m` → 1 token, 26 characters.

Q3 (constraint rule): 「魔法・技術システム：何ができて何ができないか。ルール（制約）が重要」
Location: info-box `世界観設定の5要素`, list item 3. `wc -w -m` → 1 token, 33 characters.

Q4 (the page's own rationale): 「これらが曖昧なままだと、物語の途中で矛盾が生じたり、読者の没入感を損なう原因になります。」
Location: first paragraph under h2 `世界観設定に必要な5つの要素`, last sentence. `wc -w -m` → 1 token, 44 characters.

## 5. PROPOSED lane registry row (11 columns)

Checked in Python: splits on ` | ` into exactly 11 cells; no ASCII pipe inside any cell (the page title uses fullwidth ｜ U+FF5C); status mined; opened 2026-10-25; recheck 180d; used-by is one admitted entry path. If the round also wants the row cited from the amend file, append ` ; corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` — but the staged amend does not cite S884, so I propose only the main entry.

```
| S882 | つづく編集室 (tuduku.space) コラム「Web小説の世界観・設定の作り方｜読者を没入させる世界構築の手順と注意点」, article page, visible date 2026年3月12日, JSON-LD datePublished 2026-02-25, Last-Modified 2026-06-24 — https://tuduku.space/column/novel-worldbuilding (direct, HTTP 200, 17068 bytes, browser-shaped UA; no Wayback capture) | community | C | Japanese web-fiction editorial-service practitioner register on the components of a setting and the settings note that carries them; a company marketing column with no author byline beyond the service name, so a lead and never sole support | 「世界観設定の5要素」 list box (under h2 世界観設定に必要な5つの要素), item 5, 33 characters, 1 whitespace token: 「勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか」; 「設定ノートの構成例」 list box (under h2 設定ノートの作り方｜管理と整理の実践法), item 1, 26 characters, 1 whitespace token: 「世界地図・地名一覧：手書きでよいので地図を描いておく」 | Names five required setting elements in the page order 地理・環境 / 歴史・背景 / 魔法・技術システム / 社会制度・文化 / 勢力図・人間関係の構造, and a five-item settings note (世界地図・地名一覧 / 年表・歴史 / 魔法・能力一覧 / 人物一覧 / 社会制度・用語集), not six; the page itself stresses that the magic or technology system needs stated limits (制約) | mined | 2026-10-25 | 180d | corpus/knowledge/culture-material/worldbuilding-setting-practice.md |
```

(same text saved at /tmp/ScoutTuduku/row.txt).

Recheck command for the round lesson's Gate (not inside the row): `curl -fsSL -A "$UA" https://tuduku.space/column/novel-worldbuilding | grep -c '設定ノートの構成例'` → expect 1; and the same with `'世界観設定の5要素'` → expect 1.

Tier C. Reasons: registry preamble — "C — lead only, never sole support for an admitted entry"; `community` is never A; the page is an editorial-service column (marketing CTA 無料相談フォームへ →, 回答は3営業日以内), no named author or credential, about 1,100 characters by its own count, and its two lists are checklists with one-clause glosses and no cited evidence. A practitioner register is C, not B. The entry must not rest on it alone or present the five-element list as a standard.

## 6. Wayback CDX probe for the canonical slug

UA as above. All probes returned HTTP 200 unless noted.

```
GET https://web.archive.org/cdx/search/cdx?url=https://tuduku.space/column/novel-worldbuilding&output=json&limit=20&fl=timestamp,original,statuscode,digest,length
 -> []
GET https://web.archive.org/cdx/search/cdx?url=tuduku.space/column/novel-worldbuilding*&output=json&limit=20&fl=timestamp,original,statuscode,digest,length
 -> []
GET .../cdx?url=https://tuduku.space/column/novel-worldbuilding.html&output=json&limit=5&fl=timestamp,original,statuscode
 -> []
GET .../cdx?url=https://www.tuduku.space/column/novel-worldbuilding&output=json&limit=5&fl=timestamp,original,statuscode
 -> []
GET .../cdx?url=tuduku.space/column/*&output=json&limit=5&fl=timestamp,original,statuscode
 -> []
GET .../cdx?url=tuduku.space&matchType=host&output=json&limit=10&fl=timestamp,original,statuscode
 -> []   (whole host has no capture)
GET https://archive.org/wayback/available?url=tuduku.space/column/novel-worldbuilding
 -> HTTP 429 Too Many Requests, twice (20 s apart); the availability API contributes nothing
```

Positive controls (CDX API answers):
```
GET .../cdx?url=example.com&output=json&limit=2&fl=timestamp,original,statuscode
 -> [["timestamp","original","statuscode"],["20020120142510","http://example.com:80/","200"],["20020328012821","http://www.example.com:80/","200"]]
GET .../cdx?url=archive.org/about/*&output=json&limit=2&fl=timestamp,original,statuscode   (path-prefix wildcard, same shape as the probe)
 -> [["timestamp","original","statuscode"],["20010413230105","http://www.archive.org:80/about/","200"],["20010808212851","http://www.archive.org:80/about/","200"]]
```

Ruling: NO CAPTURE for the canonical slug, its variants, or the host in CDX as of 2026-10-25 (the controls return rows, so the empty arrays are real). No archived-snapshot fallback exists; the row's recheck is live-only and the proposed source cell says "no Wayback capture". This does not make the source unreachable — the live page is reachable.

## 7. Issues for the claim/attack (not edits)

1. Staged text error: "six tables" (row teaches cell and entry §4 heading). The page lists five 設定ノートの構成例 items. An admitted entry repeating "six" is a verifiable factual defect.
2. Staged labels 勢力図 / 年表 / 能力一覧 / 制度・用語集 are abbreviations of 勢力図・人間関係の構造 / 年表・歴史 / 魔法・能力一覧 / 社会制度・用語集 — acceptable as paraphrase, wrong inside quotation marks or as "verbatim" evidence.
3. Date discrepancy on the page: visible 2026年3月12日 vs JSON-LD 2026-02-25 vs HTTP Last-Modified 2026-06-24. The proposed row cites all three rather than picking one.
4. The staged entry's tier-B pairing (staged S882 → lane S877, a conlang monograph) is unverified as scholarly framing of setting method.
5. Staged ids vs lane ids: the staged entry body names S882/S883/S884; an admitted copy must renumber to S877/S881/S882 or it will cite an unrelated lane document (the claim's own kill_rule: "an id naming an unrelated lane document"). Under the tentative map, lane S882 = this page.

## 8. What I did not check

- Not read at source: philol.msu.ru conlangs.pdf (lane S877) and litmemo.com (lane S881) — other seats.
- Did not try the plain-curl UA (browser UA worked first time).
- Wayback availability API was rate limited (429); only CDX results count.
- The page may have changed since the staged fetch on 2026-10-23; I can only say today's bytes (sha256 above) carry both sections.
