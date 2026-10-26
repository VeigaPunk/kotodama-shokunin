# ScoutReopenS884 — independent re-open of registry row S884 (round 74 wave 2)

Lane main at dispatch: 1d7add3 (`git rev-parse main`); freeze F3 00c408a0…; row/entry/evidence files re-read from the tree (the diff F3..main touches only report-side files, plus the landed entries). Scratch: /tmp/ScoutReopenS884/ (page.html, wb.html, ps.json, ext.py). No counters were needed for this attack; none run.

## 1. Re-fetch lines (QUALITY 21/22/24)

UA (both fetches): `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
curl -sS -A "$UA" -o page.html -w 'status=%{http_code} size=%{size_download} ct=%{content_type}\n' https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html
status=200 size=62604 ct=text/html
sha256sum page.html -> 344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659   (62604 B)
```
Wayback carrier (second fetch, same UA, `-L`):
```
curl ... 'https://web.archive.org/web/20221207080111id_/http://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html'
status=200 size=62623 ; x-archive-orig-date: Wed, 07 Dec 2022 08:01:12 GMT
sha256 a0b48f21c9ebc41686da8a73ef315041e387cdb647b464e1a9d23247fd3107d6 (62623 B)
```

## 2. Hash equality — SURVIVED

Live page sha256 = evidence file sha256 = Gate cell sha256 = amendment header sha256 = `344de345…d659`, 62,604 B = recorded bytes. Nothing moved. The evidence `window-sha256` also recomputes: the stored window line is 4103 chars / 12226 UTF-8 B, sha256 `1618972ce51e2323740ebb609b2cf2af28b6368566948bfe63c832f175c0cf81` (equal to the recorded value), and the quote sits in the window at char offset 2038 (before=2038 as recorded).

Wayback `20221207080111`: exists, timestamp matches the capture's own `x-archive-orig-date` (08:01:12Z). It is NOT byte-identical to live (62,623 vs 62,604 B): diff = `http://`↔`https://` in nav/search/vip hrefs plus one extra `portamento.js` script tag in the capture. Text body identical; the quote is present at para 35 by the same scheme. The amendment (line 6) claims only "carries every span quoted from it" for this capture (and byte-identical only for the 2025 one) — claim SURVIVES; the 19-byte difference is simply unstated (LOW, see F5).

## 3. Quote found — Y

Verbatim `把它放在前面大概20章之内慢慢来，我觉得是问题不大的。` (27 characters, per the evidence file) occurs exactly once in the raw HTML. Location: the 乌贼 answer beginning 这个我肯定考虑过, the FINAL sentence of that paragraph (the paragraph ends with this sentence; preceded by `如果开头足够有趣，有钩子，有悬念，那么你把整个世界观和设定逐渐地抛入，`). It is the 14th 乌贼 answer (counted: 14, matches row/Gate "14th 乌贼 answer"), and the 34th of the page's 69 `p` elements carrying `text-indent: 2em` (matches the amendment's "34th of 69" cross-check).

## 4. Para-35 numbering scheme — reproducible only one way (F1)

- `para n = nth non-empty <p> of the served page, para 1 = the browser-upgrade notice`. Raw bytes line 50-54: the notice `<p class="browserupgrade">…</p>` sits INSIDE an IE conditional comment `<!--[if lt IE 9] … <![endif]-->`. A regex over raw bytes (`<p[ >].*?</p>`, non-empty, comments NOT stripped) yields 78 non-empty p's with the notice = 1 and the quote para = 35; paras 32/33/34/35/51 land exactly where the amendment says (checked each by text). The 责编 `<!--<p>(责编：虞婧)</p>-->` is the 78th (last) and shifts nothing.
- Under ANY DOM/browser/HTMLParser reading (comments are not elements, the notice never renders) the same paragraph is **34** (my `html.parser` pass: 72 non-empty p's, quote in #34, the first p being the lead 爱潜水的乌贼，2018年后…). The evidence file's own stated extractor drops comments ("comments … dropped"), so the evidence text cannot reproduce 35 either.

Verdict: the scheme is stated (the amendment line 6 states it) and is internally consistent, but it counts a hidden IE-conditional element; the row cell (SOURCES.md cell 5 "paragraph 35 of the page (the 乌贼 answer beginning 这个我肯定考虑过)") gives no scheme, and only the anchor phrase saves a re-opener. Not a mis-location; a fragile locator.

## 5. Row line vs page (corpus/SOURCES.md:839) — tier verdict

Row: kind `community`, tier `C`, mined, 2026-10-25, 180d, used-by = the amend file only.
- Facts that the page carries: title ✓ (`<title>`/`#newstit`), 中国作家网 ✓, 中国作家协会主管 ✓ (`<b>` in header logo), 网络文学 breadcrumb ✓, 访谈 nav ✓, `来源：《青春》 | 李玮 爱潜水的乌贼 2022年12月07日10:07` ✓ (line 146), 李玮 printed without affiliation ✓, no issue number ✓.
- **F2: `责编 虞婧` is NOT printed.** Only occurrence in the entire page (and in the capture): `<!--<p>(责编：虞婧)</p>-->` (line 293), commented out; 0 hits in the comment-stripped markup. The row (cell 1: "…2022年12月07日10:07, 责编 虞婧") and the amendment header (`byline as printed … ; 责编 虞婧;`) present it alongside printed fields. The amendment does acknowledge the commented-out 责编 line for the 2025 page (S883), never for S884.
- Tier: **agree with C** — one author, one interview, hedge `问题不大`, `大概`; the interviewer's own framing; used as a lead only. The row's own teaches cell says "tier C: one practitioner's hedged tolerance, never sole support" — consistent. Note (F6, LOW): S883 (same author, same host, same genre of interview, similarly self-reported) is `docs`/`B` while S884 is `community`/`C`; the C is the defensible conservative call, but the kind/tier split between the two sibling rows is not explained by any page-observable difference (S883 has an 编者按 and a named series host; S884 has a magazine source line).
- Row carrier: wayback `20221207080111id_` named and live (see §2).

## 6. Every entry sentence citing S884 vs the page

Entry: corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md (the base entry cites no S884; grep over corpus finds S884 only here, the row, README line 807, and the lesson). All 15 quoted spans were programmatically matched verbatim to the paragraph named (`span in ps[n-1]`, all True, each unique to its paragraph): paras 32, 33, 34, 35, 51. Locators all correct under the entry's own scheme.

Sentences whose NON-quote framing the page does not carry:

- **F3 (MEDIUM-HIGH) — §4 line 53 "The first failure mode is a first chapter that dumps the system: 「它的第一章就是抛设定，把世界观、整个修炼体系抛给你。」"**. On the page this clause describes what 以前看早期的一些网络小说 did ("the first chapter of early web novels is a setting dump"), and is IMMEDIATELY followed by `如果一部书刚开始抛给我的这个东西还算有意思，那我是能够读下去的。` — i.e. he says he CAN keep reading a front-loaded opening if it is interesting. His stop-reading sentence is the 两三章都是设定 one (line 54, correctly cited). So the page does not name "a first-chapter dump" as a failure mode; the entry omits the very next sentence that reverses it. The same misreading propagates into the §5 table row 1 "what it warns against: a first chapter that explains the world" (line 79; the page does not carry it). Fix: rewrite line 53 as the description it is (`early web novels opened by dumping the system`) and add the carried follow-up 「如果一部书刚开始抛给我的这个东西还算有意思，那我是能够读下去的」 (para 35); change table line 79's warn-against to "two or three opening chapters that are all setting".
- **F4 (MEDIUM) — §2 line 35 "The earlier interview states the same order on its own … the ladder was then built from the chosen register 「然后根据塔罗牌做一个力量体系设定」 (loc: para 51)".** Para 51 (the answer to whether the ladder was 一开始就设定好) says: background already settled → tarot → power system setting, `除此之外，其他方面都还很空白`, and only THEN, because a tarot-only system would 写到中期就会缺乏变化, he wanted `有升级过程的设定` and the 序列 idea arose, with names after. So the page's order is background → tarot power-system → (added) progression ladder → naming; the entry's "same order" (world-view → progression → expression, S883's order) and "ladder … built from the chosen register" collapses the tarot power-system step and the later added ladder into one, and drops the 其他方面都还很空白 limiter. The §6 bullet "stated twice by the same author about different books" inherits the overstatement. Fix: quote 「所以知道自己如果只是做一个塔罗牌体系的话，那么写到中期就会缺乏变化，就希望做一个有升级过程的设定」 (para 51) and say the 2022 order is world-background → register-system → a ladder added to avoid mid-book stasis → names; mark it as similar to, not identical to, S883's.
- **F5 (LOW) — §4 line 63 "readers of 《诡秘之主》 understand the setting only 「到几十章后」 … The bound is his tolerance, not his book's schedule".** The page: 李 says `我也看到很多人评论说《诡秘之主》到几十章后大体上知道您的设定是什么，就会觉得很精彩了` — "大体上" (broadly) and "commenters say"; "only" is added and the 几十章 vs 20 inference is the entry's, not the page's (the author never states his own book's schedule). Soften: "commenters, per the interviewer, broadly know the setting by 到几十章后". Also line 63 says "dozens of chapters, not twenty" — 几十 is a loose interviewer figure; the entry's contrast is an inference marked as fact.
- LOW: line 51 "at paras 32–35 of one magazine interview" — fine (source line 《青春》); but the 2022 page is a web re-print on 中国作家网; the issue is not printed (row says so) — consistent.
- No S884 sentence carries the 20-chapter figure as a rule: line 58, line 80 ("roughly the first twenty chapters, if the hook holds") and line 89 (`大概`, `问题不大`, "nothing … supports a hard boundary") all keep the hedge. Line 80 "chapters two and three still exposition" paraphrases `前面两三章都是设定` ("the first two or three chapters all setting") — slight shift (chapters 2–3 vs the first 2–3), LOW.

## 7. Amendment states the schedule only as ONE practitioner's tolerance? — Y (with the F3/F4 caveats)

Checked: §4 opener (line 51: "what one author says he tolerates … It is a lead … not a rule of serial fiction, and nothing else in either row supports it"); line 61 (tolerance grounded in his own reading, not measurement); line 75 ("offered on one practitioner's say-so … not as a test anyone passes"); §6 lines 87–89 (tolerance is the author's own; row is a lead, "never quotable as a rule of serial fiction"; twenty is his 大概, "nothing … supports a hard boundary"). The table's "the third is this entry's extension of 逐渐地" disclosure is present. The ATTACK on that claim FAILED. The row's cell 6 also holds the hedge (`a hedged personal tolerance (问题不大)`).

## 8. Gate record (corpus/lessons/round-74.md:22) — SURVIVED

Gate row cites url, date 2026-10-25, the quote verbatim, locator `para 35 (the 14th 乌贼 answer), final sentence tail` (all re-verified), evidence path, 62604 B, sha256 `344de345…`, window 4103 chars (verified). Rejection line 38 and clearing conditions are consistent with the page: the re-opened quote was located on this 2022 page, not the Sowers-Wills span (not searched here; not part of this attack). Evidence file header values (http 200, ua exactly browser-shaped, fetch-attempts 1) are as I reproduced.

## 9. Findings summary

| id | severity | where | finding |
|---|---|---|---|
| F1 | MEDIUM | row cell 5, entry loc scheme, evidence extractor | para 35 counts a `<p>` inside an IE conditional comment; every DOM/HTMLParser and the evidence file's own comment-dropping extractor give para 34; scheme stated only in the amendment, not in the row. Fix: add to the row cell "(ordinal over raw bytes incl. the IE-comment notice; 34th in a rendered/DOM count; 14th 乌贼 answer)" — the answer-anchor and the 14th-answer count are already the robust locators. |
| F2 | MEDIUM | row cell 1; amendment header line 4 | `责编 虞婧` exists only inside `<!--<p>(责编：虞婧)</p>-->` (line 293), not printed. Fix: say "责编 虞婧 appears only in a commented-out line in the page source". |
| F3 | MEDIUM-HIGH | amendment line 53 and table line 79 | "first chapter dump = failure mode" is not what the page says; the next sentence says he can read on if the dump is interesting. |
| F4 | MEDIUM | amendment line 35 (and §6 line 90) | para 51 does not state the same order as S883; the ladder is a later addition to a tarot power-system; `其他方面都还很空白` omitted. |
| F5 | LOW | amendment line 63; line 80 | "only" / "not twenty" inference and 2–3 chapters paraphrase. |
| F6 | LOW | row S884 vs S883 | kind/tier split (community/C vs docs/B) for same-author same-host interviews unexplained; C itself agreed. Wayback capture differs from live by 19 B (http/https hrefs + one script) — carriers claim is true but unqualified. |

Survived: the quote's existence/verbatimness/location; live sha256/bytes equal to every recorded value; window hash; wayback capture existence, timestamp and carrying of the quote; the "one practitioner's hedged tolerance" framing; all 15 quoted spans verbatim at the stated paragraphs.

Exact reproduction: `python3` regex scan `re.finditer(r'<p[ >].*?</p>',raw,flags=re.S)` over /tmp/ScoutReopenS884/page.html, non-empty by stripped text → 78 items, quote in #35; same with `html.parser` (comments dropped) → 72 items, quote in #34. `grep -n 虞婧 page.html` → line 293 only, inside `<!-- -->`.
