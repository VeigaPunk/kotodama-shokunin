# ScoutLitmemo — re-open of staged S883 (LitMemo worldbuilding guide; tentative lane id S881)

Seat: scout, leaf, read-only. Wrote only this file and /tmp/ScoutLitmemo/. Date of fetch: Mon 26 Oct 2026 00:09 UTC (= 2026-10-25 local).
No tool installed. Fleet repo, shokuknow, claims.json not written.

## Verdict: ADMIT (tier C), with a MANDATORY re-anchor of the row — flip condition below

Reason: the page is live (HTTP 200, browser UA), and it carries all three contents the staged row claims: (a) the 5-step build order, (b) the 自然環境→社会の仕組み→文化→個人の経験 four-layer block with the causal chain written out, (c) the one-place / 正本 single-source practice. BUT the staged row's *anchor*, *title* and one *section name* do NOT match the page as served now (details §4). The staged row as written cannot be adopted verbatim; the re-anchored row in §7 can. The staged entry (worldbuilding-setting-practice.md) quotes no span at all (its "Proposed body" is a prose outline), so no quote span there is absent; the only quoted spans are the three anchors inside SOURCES.append.md row S883 cell 7, and two of them are absent/misattributed.

Flip to REFUSE if: a re-fetch shows the three located spans in §3 gone, or the lane owner insists on keeping the staged anchor strings (「小説の世界観はどう作る？」節, 3ステップ 節) unchanged — those strings are not on the page as a section.
Flip to UNVERIFIABLE: n/a for the live page (it is verified); but the claim "page as served 2026-10-23" cannot be verified (no archive capture, §6): the page's own `dateModified` is 2026-10-23T11:50:12Z, so what shokuknow served earlier that day may have been a pre-rewrite version. [INFERENCE]

## 1. Commands and raw outputs

UA used for every live fetch (exact): `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
mkdir -p /tmp/ScoutLitmemo && cd /tmp/ScoutLitmemo
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
curl -sS -L -A "$UA" -o page.html -D headers.txt -w 'HTTP %{http_code} bytes %{size_download} url %{url_effective}\n' https://litmemo.com/ja/blog/novel-worldbuilding-guide
sha256sum page.html ; wc -c page.html
```
raw output:
```
HTTP 200 bytes 101615 url https://litmemo.com/ja/blog/novel-worldbuilding-guide
441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64  page.html
101615 page.html
```
Response headers (headers.txt): `HTTP/2 200`, `content-type: text/html;charset=UTF-8`, `content-length: 101615`, `date: Mon, 26 Oct 2026 00:09:12 GMT`, `cache-control: no-cache, no-store, max-age=0, must-revalidate`, `via: 1.1 google`. No redirect (url_effective = request URL). No challenge wall.

Visible-text extraction (python3: drop script/style/noscript, block tags -> newline, strip tags, html.unescape, collapse blank lines) -> /tmp/ScoutLitmemo/visible.txt, 33311 bytes, sha256 `82454e6c15b0c45f5b344df5cd1741305906a1e72b823750596d51d6145d50bf`. (HTML comments are not stripped, so visible.txt contains some template-comment noise at the head; the located spans below are all in article body lines.) Files: /tmp/ScoutLitmemo/{page.html, page.html.keep (identical copy), headers.txt, visible.txt}.

## 2. Page metadata (from the served HTML)

| field | value | where |
|---|---|---|
| `<title>` | 世界観の作り方｜小説の世界観設定5ステップと架空の国・魔法の例 — LitMemo ブログ | `<title>` |
| h1 | 世界観の作り方｜小説の世界観設定5ステップと架空の国・魔法の例 | page |
| published | 2026年07月16日 (JSON-LD datePublished 2026-07-16T20:50:36.613281Z; also `article:published_time`) | byline + JSON-LD |
| updated | 最終更新 2026年10月23日 (JSON-LD dateModified 2026-10-23T11:50:12.82078Z) | byline + JSON-LD |
| author | none shown as a person; JSON-LD `author` = `@type Organization`, name `LitMemo`, url https://litmemo.com | JSON-LD Article |
| tags | 世界観設定 / 小説創作 / ファンタジー小説 / 設定資料集 | byline + `article:tag` |
| lang | UI language JA (ja path); `content-language: en` header is the site default, not the article | headers |
| also present | JSON-LD FAQPage (6 Q&A); vendor product CTAs (LitMemo templates/features) — a vendor blog, i.e. commercial practitioner publication | page |

## 3. Located spans (all checked with `grep -c -F` on visible.txt = 1 each; NFKC-normalised match also true; no normalisation was needed — exact byte match after tag strip + html.unescape; one trailing-whitespace/newline collapse only)

Word count: `wc -w` counts whitespace tokens; Japanese has no spaces, so a single sentence = 1 token. Character counts from `wc -m`. Both given; the ≤25-word cap is met in token terms and each span is a single sentence or two.

(b) four-layer causal chain — RECOMMENDED primary quote:
> 自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。
- location: section 「世界観の作り方：5つのステップ」 (h2) → h3 「3. 外側の層へ因果をつなぐ」, 2nd sentence of the paragraph.
- `printf '%s' "$q" | wc -w -m` -> `1  43` (1 whitespace token, 43 characters). Verbatim: yes.

(b) four-layer block itself (diagram, section h2 「世界観の4つの層」), 4 lines as served:
`自然環境（地理・気候・生き物・資源）` / `└→ 社会の仕組み（政治・経済・身分・法）` / `└→ 文化（言語・信仰・習慣・タブー）` / `└→ 個人の経験（登場人物がこの世界をどう感じるか）`; followed by 「ポイントは外側の層が内側の層を決めることです。」 (23 chars, 1 token). The h3 headings 第1層：自然環境 / 第2層：社会の仕組み / 第3層：文化 / 第4層：個人の経験 under 「世界観設定で決めることチェックリスト」 repeat the four layers. Note: the layer names are exactly the four in the staged row (自然環境 / 社会の仕組み / 文化 / 個人の経験): verbatim.

(a) five-step build order, lead sentence (visible paragraph before first h2), 103 chars:
> 世界観の作り方は、①物語の核になるルールを決める ②主人公の生活圏から作る ③自然→社会→文化→個人の順に因果をつなぐ ④物語で使う分だけ掘り下げる ⑤一か所にまとめて書きながら更新する、の5ステップです。
- `wc -w -m` on the full sentence -> `5  103` (5 whitespace tokens, 103 chars; run). Verbatim: yes. A ≤25-token cut (first three steps): `世界観の作り方は、①物語の核になるルールを決める ②主人公の生活圏から作る ③自然→社会→文化→個人の順に因果をつなぐ` -> `3 tokens, 59 chars`, verbatim (grep -c -F = 1).
- The h2 「世界観の作り方：5つのステップ」 lists h3 steps 1-5: 1.物語の核になるルールを1〜3個決める / 2.主人公の生活圏から作る / 3.外側の層へ因果をつなぐ / 4.物語で使う分だけ掘り下げる / 5.一か所にまとめ、書きながら更新する.
- The staged entry §3 order 物語の核になるルール → 生活圏 → 自然環境 → 社会の仕組み → 文化 → 個人の経験 matches steps 1-3 of the page (steps 4-5 are 掘り下げ and 一か所にまとめ); the entry's §3 omits steps 4-5 in that line, which is fine but §5 should cite step 5.

(c) single-source practice — three on-page loci (the dedicated 「3ステップ」 article is a DIFFERENT page, see §4):
1. step 5 (h3 「5. 一か所にまとめ、書きながら更新する」), `wc -w -m` -> `1  56`:
> 決めた設定は一つの場所に集め、本文を書くたびに参照します。本文で設定を変えたら、その場で設定資料も書き換えます。
   (that is 2 sentences, 56 chars, 1 token; the following sentence 「ここを怠ると、長編の後半で矛盾が出ます。」 gives the consequence.)
2. FAQ answer to 「合作やTRPGなど、複数人で世界観を作るときはどう管理しますか？」 (also in JSON-LD FAQPage), first sentence — the closest on-page statement of "single source of truth":
> 全員が同じ設定資料を一つだけ使い、それを正本にします。
   `wc -w -m` -> `1  27`. Verbatim: yes. Continues: 「誰かが設定を変えたら必ずその正本を書き換え、各自の頭の中や個人のメモに設定を散らばらせないことが、矛盾を防ぐいちばんの方法です。」
3. section 「世界観づくりのよくある失敗」 → h3 「設定同士が食い違う」: 「防ぐには、大事な設定を一か所にまとめ、関係する場面を書く前に必ず見返すことです。」 (40 chars). And section 「世界観設定のまとめ方」: 「世界観でいちばん困るのは、設定が散らばることです。」, then the per-item record fields 種類／説明／ルール／関連.
The literal phrase 設定資料集 appears as: tag; CTA 「世界観を、自分だけの設定資料集に」 (x2); template link 「設定資料集（シリーズバイブル）テンプレート」; the definition 「まとめた資料が設定資料（設定資料集）です」; and the related-post card title/blurb. `grep -o 設定資料集 visible.txt | wc -l` was not run as a total; do not rely on a count.

Support caveat for the practice (c): the phrase 信頼できる唯一の情報源 ("single trustworthy source") occurs ONCE on this page, but only inside the blurb of the related-article card for another URL (長編は後半で設定が矛盾しはじめる？設定資料集を本文とズレさせない3ステップ). It is not the page's own text and must not be quoted as this page's teaching. I did not fetch that other article (not assigned; its URL slug is not in the served HTML text I inspected — [UNRESOLVED], a candidate for a separate row if the lane wants the "per series" claim).
"One authoritative 設定資料集 per series" (staged row/entry wording): on this page it is supported for "複数人で / 一つだけ / 正本" (FAQ) and "一つの場所に集め" (step 5); "for a series" is NOT stated as such in this page's own body (the series is mentioned only in a product sentence about sharing 世界観設定 across works). The entry §5 should say "one authoritative settings document" and not attribute "per series" to S881.

## 4. Staged quoted spans vs. page as served

Staged row S883 (SOURCES.append.md line 31) quoted/anchored strings. `grep -o` counts on raw page.html and visible.txt both:

| staged string | where in staged row | on page? | note |
|---|---|---|---|
| 小説の世界観はどう作る？ ゼロから説得力のある架空世界を… (row title) | cell 2 title | ABSENT (0/0; also 小説の世界観はどう作る=0, ゼロから説得力=0, 説得力のある架空世界=0) | served title is 世界観の作り方｜小説の世界観設定5ステップと架空の国・魔法の例 |
| 創作ノート (publisher label "LitMemo 創作ノート") | cell 2 | ABSENT (0/0). The site section is labelled ブログ ("LitMemo ブログ" in `<title>`; breadcrumb ブログ). | misattributed section name |
| 「小説の世界観はどう作る？」節 | cell 7 anchor | ABSENT — no heading with that text; real headings: 世界観とは：物語の舞台とルールのまとめ / 世界観の作り方：5つのステップ / 世界観の4つの層 … | not a section on the page |
| 自然環境/社会の仕組み/文化/個人の経験 block | cell 7 anchor | PRESENT, verbatim (h2 世界観の4つの層; h3 第1層..第4層; diagram) | OK |
| 設定資料集 を本文とズレさせない3ステップ 節 | cell 7 anchor | PRESENT ONLY as link text / related-card title (2 occurrences, `grep -o` = 2 raw, 2 visible) — NOT a section of this page; it is the title of ANOTHER article. | mis-anchored: re-anchor to 5つのステップ step 5 + FAQ 正本 + 設定同士が食い違う |
| five-step order (cell 6 "a five-step order") | cell 6 teaches | PRESENT (lead sentence + h2 5つのステップ) | OK |
| recheck `grep -c '自然環境'` -> 4 | cell 12 | re-run on the served page: `grep -o 自然環境 page.html | wc -l` = 4 raw, 4 visible; `grep -c 自然環境 page.html` = 4 lines. Still 4. | passes, but weak: it would also pass on the wrong-page; propose a stronger recheck (§7) |

Staged entry (knowledge/.../worldbuilding-setting-practice.md): carries NO quoted span from S883 (source line `世界観の作り方 4層の節` names a heading that matches nothing exactly; the nearest real headings are 世界観の4つの層 and 世界観の作り方：5つのステップ). Its claims about S883: five-step order (supported), 自然環境→社会の仕組み→文化→個人の経験 causal chain "written explicitly" (supported: step 3 sentence), single-source / 一つの設定資料集 (supported as 一か所にまとめ/正本, not "per series"). The `source:` line should be re-anchored to 世界観の4つの層 / 5つのステップ.

Replacement quotes for the absent spans: because the absent strings are titles/headings (anchors), not teachable quotes, replace them with the §3 verbatim quotes: primary = `自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。` (1 token / 43 chars); for the 設定資料集 practice = `全員が同じ設定資料を一つだけ使い、それを正本にします。` (1 token / 27 chars), second = step 5 two-sentence span (1 token / 56 chars). Replacement row title = the served title (§7).

## 5. Tier

C. Reason: a commercial writing-app vendor's blog (LitMemo), authored by the organisation, no named practitioner or credentials, no citations except one named academic reference (Tolkien "On Fairy-Stories" 1939, stated on page); it is community/practitioner craft evidence for the Japanese register, so "community is never A" and a practitioner post is C. Not sole support: the entry already pairs it with tier-B S877 (philol.msu.ru conlangs.pdf). Page has product-promotion blocks (templates, AI 整合性チェック); the three located spans are advice, not product claims — flag the commercial interest in the row.

## 6. Wayback CDX probe (QUALITY 21/24)

Commands (UA as above; CDX endpoint https://web.archive.org/cdx/search/cdx?url=<U>&output=txt&limit=20&fl=timestamp,statuscode,digest,original — the later calls used fl=timestamp,statuscode,original):

| probed URL | result |
|---|---|
| litmemo.com/ja/blog/novel-worldbuilding-guide (exact) | HTTP 200, EMPTY body (0 captures) |
| litmemo.com/ja/blog/novel-worldbuilding-guide* (prefix by wildcard) | HTTP 200, EMPTY |
| litmemo.com/ja/blog/novel-worldbuilding-guide&matchType=prefix | HTTP 200, EMPTY |
| www.litmemo.com/ja/blog/novel-worldbuilding-guide | HTTP 200, EMPTY |
| positive control A (same host, subtree): litmemo.com/ja/blog/* | HTTP 200, 1 row: `20260911102425 200 LN5SCSPMMLK5O3P5453YVM6JTWGOQARJ https://litmemo.com/ja/blog/novel-character-relationship-map` |
| positive control B (same slug family, exact): litmemo.com/ja/blog/novel-character-relationship-map | HTTP 200, 1 row `20260911102425 200 https://litmemo.com/ja/blog/novel-character-relationship-map` |
| positive control C (host): litmemo.com&matchType=host&limit=5 | HTTP 200, 5 rows: litmemo.com/ at 20260911102443, 20260911102629, 20261010230039; /.well-known/ai-plugin.json 20261010230340; /.well-known/assetlinks.json 20261010230443 (status -) |
| positive control D (tool sanity): example.com | HTTP 200, rows from 20020120142510 onward |

Also `https://archive.org/wayback/available?url=litmemo.com/ja/blog/novel-worldbuilding-guide` -> HTTP 429 (rate limited; not used as evidence). Reading: the CDX responds and indexes this host (controls return rows), and has no capture of the canonical slug → "no Wayback capture" for this slug as of 2026-10-26 00:1x UTC. Consequence: there is no archived copy to confirm the earlier "page as served 2026-10-23" state; the live fetch above is the only evidence. Also `sibling-slug live 200` and `https://litmemo.com/robots.txt` HTTP 200 (robots content not read).

## 6b. What changed / what to tell the claim

- The staged row's title, publisher label (創作ノート) and two of three anchors do not match the page now. The page's `dateModified` (2026-10-23T11:50Z) is the same day as the staged "fetched 2026-10-23", which makes a post-fetch rewrite plausible but unprovable [INFERENCE]. Whatever the cause, the lane row must carry the served title and be re-anchored; citing the staged strings would reproduce the round-68/71 pattern (quote/anchor absent from the page).
- Lane row recheck: the staged `grep -c '自然環境'` → 4 holds today, but add a content-bearing check; a recheck command inside a pipe-delimited cell must contain no ASCII pipe (the staged one is escaped), so the safe form below uses only `;` and no `|`.

## 7. PROPOSED lane registry row (11 columns; no ASCII pipe inside any cell)

Columns: | id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |

```
| S881 | LitMemo ブログ「世界観の作り方｜小説の世界観設定5ステップと架空の国・魔法の例」(published 2026-07-16, last updated 2026-10-23, author LitMemo organisation) — https://litmemo.com/ja/blog/novel-worldbuilding-guide | community | C | Tier C: Japanese writing-app vendor blog, organisation-authored, practitioner craft advice for the Japanese register on specifying a setting; method evidence only, never factual authority for any culture; never the sole support (paired with tier-B S877) | h2「世界観の作り方：5つのステップ」(lead sentence and h3 1-5); h2「世界観の4つの層」and h3 第1層..第4層; h3「5. 一か所にまとめ、書きながら更新する」; FAQ「合作やTRPGなど、複数人で世界観を作るときはどう管理しますか？」 — page as served 2026-10-26 00:09 UTC, HTTP 200, 101615 bytes, sha256 441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64, UA Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 | Five-step build order (core rules, protagonist living area, causal chain outward, dig only what the story uses, one place updated while writing) and the four-layer causal chain stated as 自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る (43 chars); and the single-source practice: all collaborators use one settings document as 正本 and change it whenever the text changes | mined | 2026-10-25 | 2027-04-23 — re-fetch with the browser UA and confirm the 43-char span: curl -fsSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -o /tmp/litmemo.html https://litmemo.com/ja/blog/novel-worldbuilding-guide; grep -c -F '自然環境が社会の仕組みを決め、社会の仕組みが文化を生み' /tmp/litmemo.html -> 1 (ran 2026-10-26 against the served page.html: 1) | corpus/knowledge/culture-material/worldbuilding-setting-practice.md |
```
Cell checks: the row contains `｜` (U+FF5C FULLWIDTH VERTICAL LINE) in the quoted title — NOT an ASCII pipe, but a lane census regex splitting on ASCII `|` is unaffected; if the census tool is Unicode-naive, replace with a space and say "title as served" in the anchor (no other change). `->` and `;` appear in the recheck cell; no ASCII `|` anywhere. The recheck grep was run in a follow-up command against BOTH files: `grep -c -F '自然環境が社会の仕組みを決め、社会の仕組みが文化を生み' page.html` -> 1 and `... visible.txt` -> 1. The two follow-up `wc -w -m` runs: five-step full sentence -> `5  103`; FAQ 正本 sentence -> `1  27`.
used-by: only the base entry cites S883's content in the staged package; if the amend-2026-10-23 entry also cites it, append `; corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`. I did not read the amend entry (not assigned); the claim set names both entries, so confirm before freezing.

## 8. Unresolved / not exercised

- Separate article 「設定資料集を本文とズレさせない3ステップ」 not fetched; it is the only page text carrying 信頼できる唯一の情報源 as its own prose. Not needed for S881.
- Wayback `available` API was 429; CDX (the authoritative probe) answered.
- robots.txt content not read; no scraping restriction was exercised beyond one GET of the article.
- The `used-by` for the amend entry and whether the lane census treats `｜` specially: not checked.
