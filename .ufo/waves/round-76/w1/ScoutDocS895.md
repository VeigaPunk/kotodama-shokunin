# ScoutDocS895 — xingzuobaike GB/T 33661-2017 reproduction (campaign S916 → planned lane S895, entry d)

Verdict: **ADMIT as tier C, ONLY as an interpretation-summary reproduction, and entry d MUST be amended** (drop "the standard's own words / 原文 section", hedge clause attribution; see §5). Entry d as staged is NOT admissible as written. Flip conditions in §8.

## 1. Fetch record (all from cwd /fast/scratch/hyaku/kotodama-r76/ScoutDocS895, plain `curl -sS -L -A <UA> -D <hdr> -o <body>`)
| request | UA | HTTP | bytes | sha256 | served |
|---|---|---|---|---|---|
| GET https://www.xingzuobaike.com/huangli/wannianli/d165803.html | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | 200 (HTTP/2, no redirect; url_effective unchanged) | 33179 | 830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e | date Tue, 27 Oct 2026 21:33:45 GMT, content-type text/html; charset=utf-8 |
| same URL | `curl/8.10.1` | 200 | 33179 | 830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e (identical) | date 21:33:47 GMT |
Raw: `code=200 size=33179 url=https://www.xingzuobaike.com/huangli/wannianli/d165803.html` (both). No challenge, captcha, login or paywall met; UA made no difference. Headers saved: stage/ScoutDocS895/headers-browserUA.txt, headers-curlUA.txt; body saved stage/ScoutDocS895/page.html (sha256 as above; verified by `sha256sum`).
Charset: `file` → "HTML document, Unicode text, UTF-8 text … CRLF"; `<meta charset="utf-8" />`; header charset=utf-8. Decoded as UTF-8 (no GB18030 needed). Folding (NFKC + whitespace removal) used only in comparison; stored quote below is unfolded.
Not JavaScript-rendered, not a search form: the plain GET carries the full article text in static HTML (`<h1>`, `<p>` runs); the clause text is at byte offset ~6.9k of the raw HTML. No table is claimed; the rules are a numbered list.

## 2. Page identity (what it actually is)
- `<title>`: 国家标准《农历的编算和颁行》GB/T 33661-2017 原文及解读材料 - 星座百科网 (command: python regex on page.html).
- Byline: `老黄历网 2026-01-26 10:40:03` (来源 = 老黄历网; reproduced-from-reproduction chain). Tail of article: `此文件原载：https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296`.
- Extracted text headings (text.txt, 5609 chars): 标准制定背景 / 标准制定意义 / 标准主要内容 (items 1–4) / a footer caption. **There is NO heading or section named 原文** — `grep -n '原文' text.txt` → only line 2 (title) and line 20 (h1); the word 原文 appears in the title only. The body is the drafter's 解读 (背景/意义/主要内容), whose 编排规则 list is introduced by "本标准沿用规则如下：" (standard-main-content item 1). It is a summary of the standard's content, not the standard's clause text.
- `grep -c '则需要置闰' p1.bin` → 1 (staged row's recheck command reproduces).
- Page names 紫金山天文台 as drafting body: "由国内唯一的历书编算机构中国科学院紫金山天文台承担起草工作".

## 3. Located quote (unfolded, as stored)
`取其中最先出现的一个不包含中气的农历月为农历闰月`
- 24 characters (≤80), 1 whitespace token (Chinese, no spaces), ≤25 words. Location: "标准主要内容" item 1 (农历的编排规则), clause （4）, second sentence ("置闰规则为：…"); window.txt line 19 col 51; text.txt line 44. NFKC+whitespace-folded search over window: count 1 (`fw.count(f(q))` → 1, position 1757).
- Full clause (4) as the page prints it: `（4）若从某个农历十一月开始到下一个农历十一月（不含）之间有 13 个农历月，则需要置闰。置闰规则为：取其中最先出现的一个不包含中气的农历月为农历闰月。` Folded span count 1.
Window: stage/ScoutDocS895/window.txt, 3070 chars — **shorter than 4096, so it is the WHOLE article body text** (标准制定背景 → footer caption, before 为您推荐), sha256 `902e5cc63e81a3750ea3a87ef437939efe1b449c016deaa2273a24610ca21657` (`sha256sum`).

## 4. Staged entry d — sentence-by-sentence (entry /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md; folded counts via python `fw.count(f(span))`)
| entry sentence | verdict | located span |
|---|---|---|
| source line: "the 原文 section, 编排规则 clause (4)" | **NOT carried** — no 原文 section exists; clause (4) sits in 标准主要内容 (a 解读 section) | see §2 |
| topic: 编排规则 (1)–(5) incl. leap-month rule | carried (as summary list) | （1）以北京时间为标准时间；…（5）农历十一月之后第 2 个（不计闰月）农历月为农历年的起始月 — count 1 each |
| "calculation model and its one-second precision" | carried with a scope the entry omits: precision "根据 1900年至 2100 年期间朔和节气时刻的计算结果，在用于日期判定时对它们的计算精度要求应达到 1 秒" (folded `对它们的计算精度要求应达到1秒` count 1) — the figure is tied to date-judgement use and 1900–2100; model = IERS/"国际基本天文学规范…规定的模型" | line 46 |
| representation methods: gan-zhi year naming, sequential month naming, 闰 prefix, sequential and gan-zhi day naming, date-label format | carried, but the page labels these 具体示例 ("具体示例如下") under 农历的表示方法; 闰: `闰月采用在其前一个农历月的名称前加“闰”字的方法命名` count 1; label: `日期标识方法以“农历”、农历年名称、农历月名称、农历日名称组合表示` | lines 47–51 |
| promulgation: must state source; 农历/公历对照 with 24 solar terms | carried: `公开发行的农历日历应注明资料来源；公开发行的农历日历应包含农历和公历的日期对照以及二十四节气` count 1 each | line 53 |
| "the standard's own clause text … in the standard's own words" / "so the leap-month rule can be quoted as the standard states it, not as the drafter explains it" (row + entry ground/gap) | **paraphrase-beyond-source** — the page is the drafter's (紫金山天文台-attributed) 解读 summary, same genre as S719's interpretation; it cannot distinguish verbatim clause text from summary | §2 |
| "round 1's S718 … official registry record" / "S719 … drafter's interpretation" | **ID-collision defect** — in the lane at 98c486b, S718 = Farran 2016 PLOS ONE IDS paper, S719 = Cristia 2013 IDS paper (`git show 98c486b:corpus/SOURCES.md` lines 673–674), NOT calendar sources; must be re-pointed by document or dropped |  |
| "fetched 2026-10-23 / verified-at 2026-10-23 / recheck 180d (S916 -> 1) round 6's SOURCES-PROPOSED.md" | stale provenance; this seat re-ran 2026-10-27 → 1; the amendment needs the new dates and a lane-registry recheck command | |
Sentences to DROP or HEDGE: (a) drop "原文 section" and "standard's own words/clause text"; say "the 解读 summary of the standard's main content, reproduced on a third-party page (tier C)"; (b) hedge the 1-second figure with "for date judgement, per 1900–2100 calculation results"; (c) hedge the representation items as "examples under the 表示方法 summary"; (d) re-point S718/S719 to lane documents (none exist in lane for GB/T 33661 — `git grep -n 'GB/T 33661' 98c486b -- corpus` hits only lessons/round-68.md:111 and round-69.md:39,111, no registry row; the planned S897 openstd showGb page / S896 capture would be the corroborating carriers); (e) the Declared after-state says "no tier-C row is the sole support of an admitted entry": entry d's only cited source is this tier-C row (coupling-only to others) — it violates that clause unless S897 (tier A/B publisher page) is admitted and cited alongside, or the clause text is corroborated by a non-C carrier.

## 5. Proposed lane registry row (11 columns, no pipe inside cells; no archived capture exists — §6)
`| S895 | 《农历的编算和颁行》GB/T 33661-2017 原文及解读材料 (third-party reproduction of the drafter's 解读 summary, xingzuobaike.com 星座百科网; byline 老黄历网 2026-01-26) - https://www.xingzuobaike.com/huangli/wannianli/d165803.html ; no Wayback capture exists (CDX empty 2026-10-27) | spec | C | The 编排规则 list (1)-(5) with the leap-month rule, the calculation model and 1-second date-judgement precision, the 表示方法 examples and the 颁行 requirements, as summarised in the drafter's 解读 and reproduced on a third-party page; not the standard's clause text and not the publisher's copy | 标准主要内容 item 1, clause (4): "取其中最先出现的一个不包含中气的农历月为农历闰月" | Lets worldbuilders model a fictional calendar's leap-month rule on a published modern rule (first month with no 中气 in a 13-month 冬至-to-冬至 span) rather than on a summary of it, with the reproduction's tier declared | mined | 2026-10-27 | 180d | corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md |`
(`recheck` text may also carry: curl -fsSL URL | grep -c '则需要置闰' -> 1, ran 2026-10-27; cells contain no pipe except that recheck command must be written without `\|` for the lane schema — use `grep -c 则需要置闰` after `curl … ;` or move the pipe-free form `curl -fsSL URL -o f && grep -c 则需要置闰 f`.)
Tier: **C** — third-party reproduction (a site that reprints another site's reprint; 原载 chain to openstd); community/commercial 星座 site is never A; and it reproduces a 解读 not the clause text, so even a B ("secondary summary by a drafter") does not fit a copy whose own provenance is a two-hop reprint.

## 6. Wayback CDX probe (UA `curl/8.10.1` on every request; hosts web.archive.org / archive.org)
Probes (raw):
- `https://web.archive.org/cdx/search/cdx?url=https://www.xingzuobaike.com/huangli/wannianli/d165803.html&output=json&limit=20` → `[]` code=200
- `…?url=xingzuobaike.com/huangli/wannianli/d165803.html*&output=json&limit=20` → `[]` code=200
- `…?url=https://www.xingzuobaike.com/huangli/wannianli/d165803.html*&output=json&limit=5` → `[]` code=200
- `…?url=xingzuobaike.com/huangli/wannianli/d165803.html&output=json&limit=5` → `[]` code=200 (earlier tries to web.archive.org intermittently failed `curl: (7) Failed to connect`; those are connect failures, not empty results, and were retried until a 200)
- `https://archive.org/wayback/available?url=https://www.xingzuobaike.com/huangli/wannianli/d165803.html` → `{"url": "…", "archived_snapshots": {}}` code=200; same for `xingzuobaike.com/huangli/wannianli/d165803.html`.
Positive control (same session, same UA, retry 2 of 6 after one connect failure): `…cdx/search/cdx?url=example.com&output=json&limit=2` → header row + `["com,example)/","20020120142510","http://example.com:80/","text/html","200",…]` and `20020328012821` code=200; and `archive.org/wayback/available?url=example.com` → `"available": true … 20261027205234`. Saved: stage/ScoutDocS895/cdx-control.txt (not the first-fetch empty probes; those are in this report's raw lines above, copied from the tool transcript).
Result: no Wayback capture of this page (the control proves the endpoint answers and returns rows for a known-captured URL). Registry source cell therefore carries the live URL only. Not run: domain-wide `matchType=domain` probe (connect failed, not retried to completion), archive.ph/other mirrors.

## 7. Cross-checks on the DRAFT (CLAIMS-DRAFT.md lines 20–31 read)
- Draft plan "S895 = xingzuobaike GB/T 33661 reproduction (S916)" is consistent with the single document; nothing to merge.
- Draft says "no tier-C row is the sole support of an admitted entry" — attack: entry d is sole-supported by this C row (§4e). If entry d is expected to be among n≥2 admitted, claim d needs either S897 corroboration or counts toward REFUSE.
- Entry d cites campaign ids (S916, S718, S719, "round 6's SOURCES-PROPOSED.md") in its body; draft already says citations are re-pointed by document — here the re-point is not just S916→S895 but S718/S719 collide with unrelated lane IDS papers (§4).

## 8. Verdict
**ADMIT (row S895, tier C, mined) with mandatory entry amendments** — the row and quote are real, reproducible in two UAs, located in the static HTML, and the clause (4) quote is carried verbatim as a 解读-reproduction. **Entry d as staged: REFUSE-as-is**: it presents a 解读 summary as the standard's own 原文 clause text (paraphrase-beyond-source), carries unscoped precision, cites colliding ids, and is tier-C-sole-supported. Flip to full ADMIT of entry d when: (i) the body drops "原文 section / own words" and uses the §4 hedges, (ii) S718/S719 refs are removed or re-pointed to real lane documents, and (iii) a non-C carrier (S897 openstd showGb/newGbInfo page, or S896 capture) is admitted and cited alongside so entry d is not tier-C-sole. Flip to UNVERIFIABLE if the live page changes (sha256 mismatch → re-locate clause (4)).

## 9. Housekeeping
No tool installs. Artifacts: stage/ScoutDocS895/{window.txt,page.html,headers-browserUA.txt,headers-curlUA.txt,cdx-control.txt}. Scratch /fast/scratch/hyaku/kotodama-r76/ScoutDocS895 removed at end (receipts copied).
