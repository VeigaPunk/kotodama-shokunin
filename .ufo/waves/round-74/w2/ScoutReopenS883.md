# ScoutReopenS883 — independent re-open of lane row S883 (round 74 wave 2)

Seat: ScoutReopenS883 (leaf). Lane at attack time: main = 1d7add3f7b9eaf6f3349c56c36f6d06325d74236. No tool installed (python3 + bs4 already present). Scratch: /tmp/ScoutReopenS883/ (live.html, wb.html, s884.html). Nothing written in the lane tree except this file.

## Verdict in one paragraph

The ATTACK ON THE ROW AND THE GATE FAILED: the page hashes identically to the evidence file, the Gate quote is on the page exactly once at P68, the Wayback carrier is the same bytes, the staged refused span is still absent, and all 17 verbatim corner-bracket quotes in the amend that cite S883 are on the page (character-exact after whitespace removal only, no NFKC) at the locator printed beside them. The attack SUCCEEDED against the entry's *prose*: two sentences the page does not carry (F1, F2), one false cross-source statement (F3), one internal inconsistency that is cited to S883 (F4), and four LOW slips (F5–F8).

## 1. Re-fetch (browser-shaped UA)

UA used for every fetch: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
curl -sS -A "$UA" -o live.html -w 'status=%{http_code} size=%{size_download}\n' https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
status=200 size=48536
sha256sum live.html
a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d  live.html
curl -sSI -A "$UA" <same url>      -> HTTP/1.1 200 OK, Content-Length: 48536, Last-Modified: Tue, 10 Jun 2025 01:40:55 GMT, ETag "68478d27-bd98", Server: RMW-WEB/260923
curl -sS -A "$UA" -o wb.html -w 'status=%{http_code} size=%{size_download} url=%{url_effective}\n' 'https://web.archive.org/web/20250610015519id_/https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html'
status=200 size=48536 url=https://web.archive.org/web/20250610015519id_/https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
sha256sum wb.html
a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d  wb.html
```

- Evidence file `reports/round-74/evidence/S883.txt` records `bytes: 48536`, `sha256: a3b6640c…bee94d`. **Hash equality: YES (live = Wayback = evidence). Nothing moved.**
- Wayback `id_` capture `20250610015519`: fetched with no redirect (final URL == requested), status 200, byte-identical to live. CDX probe on the canonical slug (positive control = this very slug returns captures):
  `curl 'https://web.archive.org/cdx/search/cdx?url=www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html&output=json&fl=timestamp,statuscode,digest,length'` →
  `20250610015519 200 YLWQHESEMVFPYCHPECTNZ6Z7LLN7ZVTU 17039`, `20250611013901 200 (same digest) 17051`, `20250813004013 200 (same digest) 17497`. The cell's capture exists, is 200, and is the first of three captures with one digest.
- Evidence window: recomputed `sha256(window line, UTF-8, no trailing newline)` = `b38075d366952043671669222caa4673a6b8a93b072ea24de8633e09ab456c18` (matches), 4104 chars, 12184 B (matches); quote sits at window[2036:2068] (before=2036 after=2036, matches). I reimplemented the stated html.parser extraction: 8163 chars (matches the file's `extract:` line), quote count in extract = 1, in raw HTML = 1 (`grep -o … | wc -l` = 1). Quote chars = 32 (matches `quote-chars: 32`). `grep -c '先做的是世界观' live.html` = 1 (the lesson's recheck predicate still holds). Evidence `fetched: 2026-10-26T01:09:34Z` vs `access-date 2026-10-25`: host TZ is -03 (`date` printed `Sun 25 Oct 2026 11:04:34 PM -03`), so the two are the same instant; no defect.

## 2. Gate quote

«整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。» — **found: Y**, once, inside `div.end_article` p #68 (speaker 爱潜水的乌贼, sentence 4 of that paragraph), under the centred subheading p #49 `确定风格、设定世界、推导故事` (next subheading is p #70). Verbatim, no folding needed for this sentence. The row's second quote (`既然万事万物都从最初造物主而来，那么“所有的非凡力量也从他而来”是个合理的推论。`, 40 chars) is also on P68 verbatim. The answer is to P67 (项蕾：为什么会让人在服用魔药后产生剧烈的痛苦和症状呢？) — the row's "answer to 项蕾's …" is exact.

## 3. Locator scheme, byline chain, headline

- `div.end_article` count = 1; its `p` elements = **93** (html.parser and lxml agree); P1 = lead-image `p` (img, no text); P49 and P7/P70 are subheading `p`s. 92 of the 93 carry `text-indent: 2em` — the "92 p elements carrying a text-indent 2em style" cross-check is true and P68/P69 are indeed the 67th/68th of them. The 2025 page's `<p class="browserupgrade">` sits in an IE conditional comment outside `div.end_article`, so it shifts nothing.
- **F5 (LOW)**: the recheck cell says "94 such elements". There are 93 elements. 94 is what a regex `<p[\s>]` over the div gives, because it also matches the commented-out `<!--<p>(责编：虞婧)</p>-->` (confirmed at byte 20569, inside the div, last item). A re-opener who counts DOM `p` gets 93 and, reading "94 such elements", will think the page changed. Locators are unaffected.
- Byline chain as printed (raw HTML): `来源：文汇报&#12288;|&#12288;邵燕君 谭天 项蕾&#12288;&#12288;<em>2025年06月10日09:01</em>`. The entry's backticked string equals it with U+3000 (tested `by in entry_line` and `by in html` both True). Breadcrumb `网络文学>>访谈` and host 中国作家网 confirmed in the page. URL path date 0605 ≠ printed 06-10: true. The page prints no 责编 for the visible text (only the commented-out 虞婧 line); the entry does not claim one. Credit lines P3–P6 print exactly `爱潜水的乌贼（网络文学作家）`, `邵燕君（北京大学中文系教授）`, `谭天（北京大学中文系博士生）`, `项蕾（中国社会科学院文学研究所助理研究员）`.
- Headline claim: `<title>` = `爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”--网络文学--中国作家网`, `#newstit` = `爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”`; the 15-char headline phrase occurs in no body `p` (searched all 93). Entry says both "read 「我先设定世界观，再考虑怎么升级」" — true as containment, not as equality (see F8).

## 4. Staged round-68/71 refused span

Register/staged span: `这个我肯定考虑过。我自己就是资深读者…` (shokuknow census-adjudication.json id S758 / quote-lint-full-v5.json id S816, url = this 2025 page; absent-defect-register.md line 129).
```
grep -c on live.html / wb.html:  这个我肯定考虑过 = 0 / 0 ;  我自己就是资深读者 = 0 / 0 ;  资深读者 = 0 / 0 ;  肯定考虑过 = 0 / 0
grep -c on the 2022 page (s884.html, sha256 344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659, 62604 B = the S884 evidence values): 这个我肯定考虑过 = 1 ; 我自己就是资深读者 = 1
```
**Still absent from the 2025 page, live and Wayback; present on the 2022 page** — the mispairing diagnosis in the Gate is confirmed. Attack failed.

## 5. Tier verdict

**Agree with B (docs), scope-limited to his own reported practice.** Reason: the page is an edited interview transcript conducted by named scholars, with the author's own sentences (speaker-labelled; 39 of his answer paragraphs), so it is first-hand for "what he says he did" but is not verified practice, is an outlet reprint (来源：文汇报) with an 编者按, and nothing independent corroborates the process. A would overstate (QUALITY header: A = primary/authoritative for scope; the page is a reprint with unknown author review); C (as S884) is not required because §2–§3 rest on a speaker-labelled answer rather than on an interviewer paraphrase. The S883 B / S884 C asymmetry (both reprints on 中国作家网 with an outlet source line) is defensible because tier is scoped to the claim, but it is stated only in the amend's §4 prose, not in either row cell — LOW, see F7.

## 6. Entry sentences citing S883 that the page does NOT carry (grep of corpus for `S883` finds the amend only; the base entry `worldbuilding-setting-practice.md` does not cite it)

Quotes: all 17 corner-bracket quotes in cited lines 3, 21–23, 29–34, 39–45 are on the page at their stated P (line 21's headline quote is correctly stated to be outside any `p`). Not carried, in the amend file `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`:

**F1 (MEDIUM) — line 34 mislabels the quoted sentence as "the third step".** Text: "The third step is a fit to the world-view's tone, decided after the laws exist: 「服食魔药和扮演法是符合世界观调性的升级方式」 (loc: P68)". The author's three steps (P68) are 世界观 → 升级 → 升级的表现. The quoted clause says 服食魔药 and 扮演法 are the *升级方式* (the progression mechanism = step 2; the amend's own §5 table row "progression" says the same). The page puts 表现 (the symptom/排异反应) at the start of P68's answer, not in this clause. Raw: P68 = `…有了这些定律，我就觉得，服食魔药和扮演法是符合世界观调性的升级方式。` Proposed fix: relabel as the second step (progression is judged to fit the tone once the laws exist) and, if the third step is to be cited, cite the P68 sentence about 痛苦的排异反应 (`你获得它之后，它对你的身体来说是外来力量，就会有痛苦的排异反应`) for 表现.

**F2 (MEDIUM) — line 29 / row 838 generalise a sentence whose referent is the potion-pain design.** The sentence 「整个过程里…」 is the answer to P67 (why does taking a potion cause severe pain and symptoms?). 整个过程 refers to that derivation, and the same paragraph first states the pain mechanism. The entry presents it as "the three steps and their order … a sequence he followed" for the world (and §5 turns it into a world-level gate list). The row cell does name the question, but line 29 does not; a reader of the entry alone cannot see the scope. P61/P62/P66 do show world-view-before-ladder for the ladder as well, so the claim is supported in weaker form. Proposed fix: add the question to line 29's locator note ("answer to 项蕾's why-pain question, P67") and word §2's lead as "for the potion-system derivation, and by P61/P66 for the ladder".

**F3 (MEDIUM) — line 90: "stated twice by the same author about different books" is false.** Both statements are about 《诡秘之主》: S883 P61 (塔罗牌 ladder, 序列途径) and S884 para 50 on the page (para 51 in the row's scheme with the browser-upgrade notice counted; the answer follows `李：《诡秘之主》的升级序列是开始就设定好的吗？`, with `首先想的是，我的背景设定既然已经明确了，在《一世之尊》的时候就有雏形了…然后根据塔罗牌做一个力量体系设定`). Commands: parsed s884.html, `paras[48]` = that question, `paras[49]` = the answer. Also not surfaced anywhere in the amend: that S884 answer opens `乌贼：对，一开始就设定好了`, while S883 P69 says `一开始其实不是所有设定都想好了`. These are compatible only if referents differ (ladder vs every setting), and line 30 ("not a plan finished before writing began") states a stronger claim than P69 carries. Proposed fix: line 90 → "stated twice by the same author about the same book, 《诡秘之主》"; add one sentence naming the ladder-vs-all-settings difference between S884 para 51 and S883 P69.

**F4 (MEDIUM) — §3 line 47 and §5 table row "progression" contradict the page's (and line 43's) ladder derivation.** Line 47 (labelled "this entry's formulation") says "let those laws choose the ladder"; §5 row 72 asks "do the world's own laws produce this ladder?" under the heading "(S883)". On the page the ladder (序列途径) is derived top-down from the 22 tarot cards, a register chosen because it fits the Cthulhu-Europe tone (P61), and the *laws* are what P68 says selected the 升级方式 (服食魔药 / 扮演法), not the ladder; P66 even says 扮演法 existed first and potion-taking followed from it. Line 43 of the same entry states the register→ladder order, so the entry is internally inconsistent. Proposed fix: line 47 → "let those laws choose the progression mechanism, and let the chosen register shape the ladder"; row 72 → split the two questions; mark the §5 table as this entry's design extension (as the second table already does for S884).

**F6 (LOW) — line 23: "谭天's question opens 「作为一位“理工男”网文作家，您最擅长构建缜密恢宏的世界观」 (loc: P8)".** The quoted clause starts at character index 207 of a 370-character P8; the question opens with `据我们观察，从2018年开始…`. "opens" is not carried; "contains/praises" is. Fix: replace "opens" with "includes".

**F7 (LOW) — row/lesson quote cells give no CJK character count** (QUALITY rule: CJK also give characters). Row 838's quote cell and the Gate row 21 omit "32 characters"; it is present only in the evidence file (`quote-chars: 32`). S882's SOURCES row does give "33 characters, 1 whitespace token". Fix: add "32 characters, 1 whitespace token" to the quote cell and the Gate row.

**F8 (LOW, nits in line 3 and line 22, both cite S883).** (a) line 3 says P2 "names the series host 北京大学网络文学研究团队"; P2 says the series `邀请北京大学网络文学研究团队…进行长篇访谈` — the team is the invited interviewing party; the page names no host/organiser of the series. (b) line 22: "the three named interviewers' roles are printed only in the credit lines (P3–P6)" — the credit lines print titles and affiliations only; the page never prints 访谈者/采访 (searched the full extract: only `文汇报` matches among `访谈者|采访|主持|整理|文汇报|责编|编辑`); the row's "访谈者" is inferred from the speaker labels (邵燕君 4, 谭天 23, 项蕾 14 labelled paragraphs). (c) line 21: "`<title>` and `#newstit` read 「我先设定世界观，再考虑怎么升级」" — they read `爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”` (plus `--网络文学--中国作家网` for `<title>`). (d) line 44: 「越贴近现实就越有代入感」 is carried at "low ranks"; P62 says `中、低序列` (middle and low). Fix: reword each to what is printed.

## 7. What survived (attack failed)

- Page bytes/sha256, status, Content-Length: unchanged versus the Gate evidence.
- Wayback `20250610015519id_` = same page, 200, no redirect; canonical-slug CDX shows three captures.
- Gate quote found verbatim, once, at P68; subheading and speaker verified; the staged span is absent here and present on the 2022 page.
- Locator scheme as stated reproduces (P1 = image, 93 `p`, 92 text-indent 2em, P68/P69 = 67th/68th); every quoted span sits at its stated Pn.
- Byline chain, breadcrumb, credit lines, 编者按 content (twelve writers, forthcoming volume 《创作者说：网络文学代表性作家访谈录》（北京大学出版社）), URL-date discrepancy: all as printed.
- Tier B: agreed (section 5).

## 8. Tools

No install. python3 3.x with bs4/lxml/html.parser (pre-existing), curl. No pacman. No writes outside this file and /tmp/ScoutReopenS883/.
