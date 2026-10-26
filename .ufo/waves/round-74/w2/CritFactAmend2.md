# CritFactAmend2 — falsification of `worldbuilding-setting-practice.amend-2026-10-23.md`, second half

- seat: CritFactAmend2 (leaf; no dispatch, no background jobs)
- target: `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` (91 lines, 16,227 B at `c4bf61a`), sections in my scope: §4 (delivery schedule), the `contested` calibration paragraph, `couples:`, `scope:`, `sources:`; the 2022 page's paragraph numbering is the assigned axis.
- revision read: `c4bf61a8d722f9168ce0fd8021a6261c000610c5` (claim C lands); tree also carries `1d7add3` (receipts only).
- verdict: 2 HIGH (F1 sits outside the letter of my assigned spans but contradicts a surface landed by the same claim), 3 MEDIUM, 2 LOW. The schedule's *wording* as one practitioner's tolerance survives every test I ran; two sentences — one reading the interview for readers, one overstating the evidence base — do not.
- scratch: `/tmp/CritFactAmend2/` (page copies, paragraph dumps, scripts). Nothing written outside this report file in the lane.

## 1. Fetch record (QUALITY 21/22/24)

User-Agent sent on every fetch, verbatim (the same browser-shaped UA the entry's rows record):

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
```

```
$ UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
$ curl -sS -A "$UA" -o p2022.html -w 'HTTP %{http_code} bytes %{size_download} type %{content_type}\n' 'https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html'
HTTP 200 bytes 62604 type text/html
$ curl -sS -A "$UA" -o p2025.html -w 'HTTP %{http_code} bytes %{size_download} type %{content_type}\n' 'https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html'
HTTP 200 bytes 48536 type text/html
$ sha256sum p2022.html p2025.html
344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659  p2022.html
a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d  p2025.html
```

automation: `curl` only (my own plain requests); no browser automation, no challenge, no cookie, no login. Both sha256 values equal the bytes the entry's two `source:` rows record, so the served page did not drift between the entry's fetch and mine.

Control with curl's own default UA (curl 8.23.0; the implicit UA is `curl/8.23.0`):

```
$ curl -sS -o c22.html -w 'UA curl/8.23.0 -> HTTP %{http_code}, %{size_download} B\n' 'https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html'
UA curl/8.23.0 -> HTTP 200, 62604 B
$ curl -sS -o c25.html -w 'UA curl/8.23.0 -> HTTP %{http_code}, %{size_download} B\n' 'https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html'
UA curl/8.23.0 -> HTTP 200, 48536 B
$ sha256sum c22.html c25.html
344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659  c22.html
a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d  c25.html
```

`no capture` rulings: none needed. Neither page was walled — 200 and identical bytes under both the browser-shaped UA and curl's default UA — so no CDX probe or positive control was required by QUALITY 21/24. No Wayback capture was relied on for any span in this report.

## 2. Locator scheme — reproduced, and the numbers in the entry's cross-check are correct

Extraction: raw source, `script`/`style` removed, every `<p ...>...</p>` in document order, tag-stripped, whitespace-collapsed, empties dropped (`/tmp/CritFactAmend2/parse22.py`; regex `<p\b([^>]*)>(.*?)</p>` with `re.S`).

```
nonempty doc p (2022): 74        p in div.end_article: 69 (all text-indent:2em)
doc para 1  = 您在使用一个 旧版本的 浏览器，请 更新你的浏览器 来更好的体验本网站。
doc para 32 = 李：很多网文在第一、二章就会基本上给出一个很明确的世界观…
doc para 33 = 乌贼：因为当时我这本书的设定做得比较多…
doc para 34 = 李：看来您是很坚定地相信这样的方式是没有问题的…
doc para 35 = 乌贼：这个我肯定考虑过。…
doc para 51 = 乌贼：对，一开始就设定好了。…
```

2025 page: `div.end_article` holds 93 `<p>` elements plus the commented-out `<p>(责编：虞婧)</p>` at source line 241 (inside the div, last), i.e. 94 as the entry says; 92 of them carry `text-indent: 2em`; P68 is the 67th of those and P69 the 68th. The 2022 tolerance paragraph is the 34th of the 69 in `div.end_article`. Every number in the entry's `recheck:` cross-check sentence therefore checks out, and the cross-check does pin the scheme to a DOM-parsable anchor.

The paragraph-numbering axis itself is sound: all spans I checked land where the entry says. But the scheme is only reproducible from raw bytes, not from a DOM — see F6.

## 3. Per-span table — second half (every quoted span and every in-scope header claim)

`ch` = characters (CJK, no internal whitespace; each quote is 1 whitespace token). Location = `para n` under the entry's scheme unless stated.

| line | span / claim | ch | claimed loc | found | speaker | verdict |
|---|---|---|---|---|---|---|
| 53 | 「它的第一章就是抛设定，把世界观、整个修炼体系抛给你。」 | 26 | para 35 | para 35 | 乌贼 | verbatim ✓ — gloss false (F3) |
| 54 | 「但如果一开始前面两三章都是设定，那我大概是不会看下去了」 | 27 | para 35 | para 35 | 乌贼 | ✓ |
| 55 | 「很多一开始设定不明确的小说我也是看不下去的」 | 21 | para 35 | para 35 | 乌贼 | ✓ |
| 56 | 「如果开头足够有趣，有钩子，有悬念」 | 16 | para 35 | para 35 | 乌贼 | ✓ |
| 57 | 「那么你把整个世界观和设定逐渐地抛入」 | 17 | para 35 | para 35 | 乌贼 | ✓ |
| 58 | 「把它放在前面大概20章之内慢慢来，我觉得是问题不大的。」 | 27 | para 35 | para 35 | 乌贼 | ✓, hedge intact |
| 59 | 「用悬念作钩子吸引人读下去」 | 12 | para 33 | para 33 | 乌贼 | ✓ |
| 59 | 「然后在整个故事的推进中一点点地把设定给抛出来」 | 22 | para 33 | para 33 | 乌贼 | ✓ |
| 60 | 「如果我一开始就把这个设定给你们，肯定是比现在这个版本更不友好」 | 30 | para 33 | para 33 | 乌贼 | ✓ |
| 61 | 「我对不同的小说有不同的容忍度」 | 14 | para 35 | para 35 | 乌贼 | ✓ |
| 63 | 「到几十章后」 | 5 | para 32 | para 32 | 李 (question) | quote ✓ — the sentence around it does not (F2) |
| 89 | 「我觉得是问题不大的。」 | 10 | para 35 | para 35 | 乌贼 | ✓ (sentence-closing check correct) |
| 4 | S884 row: 200/62,604 B/sha256, byline, 责编 | — | — | reproduced | — | ✓ except the 责编 line is commented out (F6) |
| 6 | `recheck:` scheme + cross-check numbers | — | — | 74/69/94/92/67/68/34 all correct | — | ✓; raw-count only (F6) |
| 11 | `sources:` tier B / tier C, 编者按, 来源：《青春》, no pairing | — | — | registry S883=B, S884=C; P2 says 十二位作家 and 《创作者说…》(北京大学出版社); byline `来源：《青春》`; no 第N期 anywhere | — | ✓ (one scope ambiguity, §4 note) |
| 12 | `couples:` hands a derived ladder and a disclosure plan to the contract | — | — | contract has no disclosure-plan payload; its only "ladder" is a refusal | — | F5 |
| 13 | `scope:` refusal of "a reading of either interview as evidence about readers" | — | — | contradicted by line 63 | — | F2 |

First-half spans I re-opened while collecting the 2025 evidence, all verbatim at the locators named (appendix, not my assigned attack): P2 编者按 / P3–P6 credit lines / P8 谭天 praise (28 ch) / P61 22-card quote (25 ch) + 推导 quote (16 ch) / P62 越贴近现实就越有代入感 (11 ch), 等级很高以后，再用现实职业会很违和 (17 ch), 贴近现实、来源于现实、又能在现实中展现出神秘学魅力 (25 ch) / P66 扮演法 quote (35 ch) / P68 order + premise + inference quotes / P69 three quotes. The headline 「我先设定世界观，再考虑怎么升级」 (15 ch) occurs twice in the raw page (`<title>`, `#newstit`, both prefixed 爱潜水的乌贼：) and in **no** `div.end_article` `<p>` — the entry's no-P-number statement is correct. 乌贼's credit lines use the exact printed affiliations.

## 4. Findings

### F1 — HIGH — the `gap filled:` line is falsified by the entry it amends, and by the index landed with it

Line 10 says the entry it amends *"does not say which part is built first, which part is derived from which, or when in a serial the reader is shown any of it."*

The entry it amends (`worldbuilding-setting-practice.md`, same claim, same revision) says exactly that, twice:

```
$ grep -n '^## §4 Build order' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
72:## §4 Build order — the five steps, and the two orders they allow
$ grep -n 'the first artefact is a one-sentence premise' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
46:That is the scholarly counterpart of the practitioners' first step, and it is the strongest single design rule in this entry: the first artefact is a one-sentence premise, and everything else is derived from it.
$ grep -n '^| in what order to fill the parts' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
53:| in what order to fill the parts | not addressed | five steps, five elements, five note sections |
```

Clause 1 ("which part is built first") and clause 2 ("which part is derived from which") are answered by that entry's own §4 heading, its step 1 (`①物語の核になるルールを決める`), and line 46. Clause 3 is partly answered too — the same entry's failure list carries `setting overload | an opening that explains the world before the story starts | show the setting inside a conflict`, and §5 says the reader sees the world through the character's eyes. The *only* genuinely absent thing is a chapter-scale schedule; the amendment's §2/§3 do add a specific author's three-step order and the material-carrier inference, so the amendment has a real gap to fill — the claim about the gap is just written far too wide.

The same landing's own index contradicts the gap line in public:

```
$ grep -n 'five-step build order' corpus/README.md
446:- `worldbuilding-setting-practice.md` — … a five-step build order, a four-layer causal chain …
```

This is outside the letter of my assigned sections (the `gap filled:` field is not `sources`/`couples`/`scope`); I report it once because a re-opener comparing two surfaces landed by the same claim sees a contradiction, and because "records those three things and nothing more" is the sentence the rest of the amendment hangs on.

Smallest safe correction (line 10): *"the entry this amends states a five-step order from two practitioner pages (premise, near field, causal chain, depth, record) and an opening rule against setting overload, but it does not say which of the world-view, the progression and the expression of the progression comes first for a single author, nor that the ladder is derived from the laws the world-view fixes. This amendment records those two decisions, plus one author's stated tolerance for when the world's rules reach the reader."*

### F2 — HIGH — line 63 reads the interview as evidence about readers, which the file's own `scope:` refuses, and its contrast is a category error

Line 63: *"The bound is his tolerance, not his book's schedule: the interviewer notes that readers of 《诡秘之主》 understand the setting only 「到几十章后」 (loc: para 32) — dozens of chapters, not twenty (S884)."*

Line 13: *"It refuses: … a reading of either interview as evidence about readers."*
Line 87: *"Nothing here measures readers."*

The sentence is exactly such a reading, and three things are added to the source. The operative clause of para 32 (a 李 question) is 「我也看到很多人评论说《诡秘之主》到几十章后大体上知道您的设定是什么」 (33 ch, loc: para 32).

(a) *"the interviewer notes that readers … understand"* → the source is the interviewer relaying *other people's comments* (「我也看到很多人评论说」) and saying readers **大体上知道** (broadly know), not understand. (b) *"only"* has no counterpart in the source. (c) *"dozens of chapters, not twenty"* opposes two different quantities: the 20-chapter sentence at para 35 is a **release window** (「把它放在前面大概20章之内慢慢来」, 27 ch) — which is what §4 itself says the section records ("when a serial releases the world's rules") — while 几十章后 is a **comprehension** report. Both can be true at once (rules released within ~20 chapters, grasped over dozens), so presenting the second as correcting the first is an inference the page does not support, made in the one section whose purpose is to bound the claim downward. It also sits outside §4's own frame at line 51 ("what one author says he tolerates"), because the words are the interviewer's.

Smallest safe correction (line 63): *"The bound is his tolerance, not his book's schedule: the interviewer relays readers' comments that 《诡秘之主》's setting is broadly known 「到几十章后」 (loc: para 32) — a different quantity from the release window, and a reported comment, not a measurement (S884)."* Line 87 then needs no change.

### F3 — MEDIUM — line 53 calls a case the author says he can tolerate "the first failure mode"

Line 53: *"The first failure mode is a first chapter that dumps the system: 「它的第一章就是抛设定，把世界观、整个修炼体系抛给你。」"*

The same paragraph continues, unquoted, with the concession that governs it: 「如果一部书刚开始抛给我的这个东西还算有意思，那我是能够读下去的。」 (32 ch, loc: para 35), and only then 「但如果一开始前面两三章都是设定，那我大概是不会看下去了」 (quoted by the entry at line 54).

So the source's structure is: a chapter-one dump is **tolerable when the dumped material is interesting**; a dump that runs through chapters two and three is what he abandons. Line 54 captures the second correctly; line 53 promotes the first to a failure mode of equal standing and drops the condition. The entry's line 56 ("the condition precedes the schedule") quotes the condition from the *later* sentence and does not restore the concession for this case. The mislabel then propagates to §5 line 79, whose warning cell reads `a first chapter that explains the world` — stronger than the source for the reason given at para 35 (it does have support from para 33, his own counterfactual, but not from this passage).

Smallest safe correction: line 53 → *"The opening he describes in other authors' early web novels is a dump he tolerates only when the dump itself is interesting: 「它的第一章就是抛设定，把世界观、整个修炼体系抛给你。」 (26 ch; loc: para 35), immediately qualified — 「如果一部书刚开始抛给我的这个东西还算有意思，那我是能够读下去的。」 (32 ch; loc: para 35) (S884)."* And line 79's third cell → `a first chapter that explains the world and is not otherwise interesting`.

### F4 — MEDIUM — line 90 says "different books"; both statements are about 《诡秘之主》

Line 90: *"…only to be one working method, stated twice by the same author about different books."*

The §2 second row's statement answers a question that names the book: 「《诡秘之主》的升级序列是开始就设定好的吗？」 (21 ch, loc: para 50), and the answer's own first clause is 「首先想的是，我的背景设定既然已经明确了」 (19 ch, loc: para 51). Every §2 quote from the first row is also inside the 2025 interview's 《诡秘之主》 discussion (P50 asks about its inspiration; P60 about its 序列途径; P65 about 魔药; P61/P62/P66/P68/P69 are the answers). The two statements are two interviews about **the same book**, which is weaker corroboration than the sentence claims — and the sentence sits in "what this amendment does not establish", i.e. it exists to bound the claim.

Smallest safe correction: *"stated twice by the same author — in two interviews and about the same book, 《诡秘之主》 —"*.

### F5 — MEDIUM — `couples:` and the handoff name a disclosure-plan home the contract does not have

Line 12: *"`synthesis/worldbible-integration-contract.md` (where a derived ladder and a disclosure plan become world-bible records that lore owns)"*; line 91 repeats it (*"the derived ladder, the laws behind it and any disclosure plan are records for a world bible, which `synthesis/worldbible-integration-contract.md` hands to lore"*).

That file defines its delivered artifacts as a payload table (System specification, Diachronic specification, Lexicon, Naming ledger, Myth-symbol register, Era-costume matrix, Coupling register) plus a handoff envelope. It has no disclosure-plan, pacing or schedule payload, and no fiction-reader field at all:

```
$ grep -n -i 'disclos' corpus/knowledge/synthesis/worldbible-integration-contract.md
180:- This contract is not a civilization survey: … A received civilization dossier must disclose which languages, periods and source traditions its compiler cannot assess.
$ grep -n -i 'ladder' corpus/knowledge/synthesis/worldbible-integration-contract.md
108:## 7. Era staging: align records without a universal ladder
```

The single line with "disclose" is a provenance caution about a dossier's blind spots, not a delivery schedule; the single line with "ladder" is the contract **refusing** a universal ladder. A reader following the couples line to file a disclosure plan finds no slot, and a reader checking "derived ladder" meets a heading that says the opposite. A derived progression ladder can defensibly travel as the System-specification payload; a disclosure plan cannot travel as anything the contract names.

Smallest safe correction: line 12 → *"`synthesis/worldbible-integration-contract.md` (the handoff envelope and System-specification payload through which a derived ladder is submitted; the contract defines no disclosure-plan payload at 1.0.0)"*; line 91 → *"…are records for a world bible, which `synthesis/worldbible-integration-contract.md` hands to lore — the ladder as a System specification, the disclosure plan as free-form design metadata the contract does not yet define"*. (Also on line 12: "dates and orders" — the amendment assigns no dates to the layers or tables, only an order; drop "dates".)

### F6 — LOW — the 2022 locator scheme counts a paragraph that lives in a conditional HTML comment, and the S884 `责编` is likewise a commented line

Line 6 defines `para n` as *"the nth non-empty p of the served 2022 page, para 1 = the browser-upgrade notice"*. The notice exists only inside an IE conditional comment:

```
line 52: <!--[if lt IE 9]>
line 53: <p class="browserupgrade">您在使用一个 <strong>旧版本的</strong> 浏览器，请 <a href="…">更新你的浏览器</a> 来更好的体验本网站。</p>
line 54: <![endif]-->
```

A raw count of `<p>…</p>` blocks reproduces the entry's numbering exactly (74 non-empty in the served bytes, notice = para 1). A DOM parse does not: `lxml` returns 72 non-empty p — it drops both commented blocks, the notice and the 责编 line — so para 1 becomes the article lede and every entry number is one above its DOM ordinal: the entry's "para 35" is DOM `p` 34 (the tolerance answer), the entry's "para 51" is DOM `p` 50 (乌贼's answer). A re-opener who counts to 35 in the DOM inspects raw para 36 — 李's question about the Victorian era — where none of the quoted spans is present, and must notice the off-by-one to recover. The cross-check sentence saves it (the 34th of 69 in `div.end_article` is the tolerance paragraph, verified), so this is recoverable, not fatal. Unlike the 2025 scheme, which explicitly flags its commented-out `责编` line, the 2022 scheme does not say its para 1 is commented — and the S884 `source:` row's *"责编 虞婧"* is itself only present as `<!--<p>(责编：虞婧)</p>-->` (source line 293), so a re-opener using a DOM sees neither.

Smallest safe correction (line 6): *"…**para n** = the nth non-empty `p` of the served 2022 page in raw source order, counted with the browser-upgrade paragraph at `<!--[if lt IE 9]>…<![endif]-->` (a DOM parse omits it, so counting to n inspects the paragraph after the intended one); **para 1** = that notice. The S884 责编 line is likewise commented out in the source."*

### F7 — LOW — the calibration says the interviewer "states" a competing prescription that the body, and the page, attribute to unnamed authors

Line 18–19: *"`contested`, and the reason is on the page — the interviewer states the opposing prescription in the same interview…"*. The source is a question, and the view is attributed: `有的网文作者会认为网络文学一开始就应该让大家明确世界观` (27 ch, para 34). The entry's own line 24 gets this right ("he attributes to unnamed authors"), so the calibration sentence is one word stronger than the entry's own evidence. The label `contested` itself survives (QUALITY 2 §2 needs only a label and a reason, and the entry scopes the contest "inside the second source itself"); the reason's verb does not.

Smallest safe correction: *"the interviewer puts a competing prescription attributed to unnamed authors"*.

## 5. Attacks that failed (the claim survived), with evidence

1. **Schedule-as-rule.** Title, preamble (line 51), §6 (lines 88–89) and `scope:` (line 13) all frame it as one practitioner's tolerance and a lead; §5 asks it as a question ("inside roughly the first twenty chapters, **if the hook holds**"); the figure is kept as his 大概 and his closing 我觉得是问题不大的 (10 ch). No sentence converts it into a rule. Only F1's over-wide gap line touches this, and it does not strengthen the schedule.
2. **All §4 quotes verbatim at the claimed paragraphs.** Nine bullets carrying ten quoted spans, plus one quoted span in the closing paragraph (eleven in all) across paras 32/33/34/35 — exact character-for-character match against the served bytes, including CJK punctuation; every bullet's speaker is right (paras 33, 35, 51 are 乌贼 answers; 32 and 34 are 李's questions). The 20-chapter sentence is his, inside his own answer, and the hedge is inside the quotation.
3. **Nothing says the two rows pair to support the schedule.** Every span in §4 and every citation in §5's disclosure table and §6 is S884; S883 appears only in §2/§3 and the §5 gate table. The nearest pairing sentence (line 90) is about the *build order*, not the schedule. Line 11's "no pairing of the two rows is claimed" is therefore true as scoped to §4 — though as written it reads globally, while §2 does pair the rows for the order; a two-word tightening ("supports §4") would remove the ambiguity. I did not raise this as a finding.
4. **`sources:` tier and provenance claims.** S883 is tier B, S884 tier C in `corpus/SOURCES.md` (rows 838–839); P2 does say 北京大学网络文学研究团队 and 十二位作家 and that the full series 将收入《创作者说：网络文学代表性作家访谈录》（北京大学出版社）; the 2022 byline is `来源：《青春》　|　李玮 爱潜水的乌贼　　2022年12月07日10:07` (full-width spaces as printed); the page carries no 第N期 anywhere, and 李玮 carries no affiliation. "Plain request … no challenge, paywall or automation" is consistent with my own plain requests.
5. **"nothing else in either row supports it".** I searched both pages for a disclosure schedule (抛/逐渐/一点点/几章/开头/章). The 2025 page has no passage about when world rules reach a reader; its nearest is P87 (线索 release order at a climax), a different subject. The 2022 page's other candidates are para 30 (the suspense opening — supports the *mechanism* already quoted at para 33, not the schedule) and para 45 (unclear early 升级/爽点 cadence, again not setting disclosure). The negative stands.
6. **Locators exist and resolve.** Every locator used in the second half is present under the scheme, and the `recheck:` cross-check numbers (94/92/67/68, 69/34) are all exactly right.
7. **Ground line at base.** `git show f7104cb…:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` = 804; `… | grep -c chinawriter` = 0; `git ls-tree -r --name-only f7104cb… corpus/knowledge | grep -ciE 'worldbuilding|setting'` = 0. (Outside my span; checked green.)
8. **`contested` label.** Survives QUALITY 2's vocabulary requirement (label + reason on the page); only the reason's verb is wrong (F7).

## 6. Smallest safe correction set, in priority order

1. Narrow line 10's gap claim (F1) — it is the only finding a re-opener can falsify with a two-line grep inside the lane.
2. Reword line 63 so the reader-comment stays a reported comment, drop "only", and drop the "not twenty" contrast (F2).
3. Restore the concession at line 53 and soften line 79's warning cell (F3).
4. Fix "different books" at line 90 (F4).
5. Correct the couples/handoff description of the contract (F5).
6. Disclose the conditional-comment paragraph and the commented 责编 line at line 6 (F6); tighten "states" to "attributes" at line 18 (F7).

No finding requires touching a quotation, a locator, a tier, or the schedule's hedge — the entry's evidence layer is intact at this revision.
