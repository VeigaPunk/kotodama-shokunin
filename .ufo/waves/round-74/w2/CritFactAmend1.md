# CritFactAmend1 — falsification of `worldbuilding-setting-practice.amend-2026-10-23.md`, first half

- seat: CritFactAmend1 (leaf; no delegation, no background jobs, no `task` spawns)
- round: kotodama 74, WAVE 2 (falsify; hyaku run 7)
- target: `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`, **header rows through §3** (§4–§6 read only where a §1 statement needed a counterexample)
- frozen claim read first: `git show 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/claims.json` (claim C, legs ENTRIES/ROWS/REPOINTED/GATE/EVIDENCE; claim Ca SEPARABLE excludes `corpus/knowledge/**`)
- lane repo untouched: every read was read-only; no write outside this report file. Scratch: `/tmp/CritFactAmend1/`.
- verdict: **the citation apparatus survives.** No fabricated quote, no wrong P-number/para number, no byline, date, credit-line, breadcrumb or locator-scheme error found. Eight defects, none BLOCKER, all in the glosses wrapped around correct quotes.

## Fetch record (per-fetch, exact UA)

UA used for every fetch below:
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
$ curl -sS -A "$UA" -o page2025.html -w 'HTTP %{http_code} bytes %{size_download}\n' \
    'https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html'
HTTP 200 bytes 48536
a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d  page2025.html

$ curl -sS -A "$UA" -o page2022.html -w 'HTTP %{http_code} bytes %{size_download}\n' \
    'https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html'
HTTP 200 bytes 62604
344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659  page2022.html
```

Both match the file's own fetch notes byte for byte (48,536 B / `a3b6640c…`; 62,604 B / `344de345…`). No challenge, paywall or wall met; no capture ruling is made, so no CDX probe is required.

Carriers (same UA):

```
$ curl -sS -A "$UA" -o cap25.html -w 'HTTP %{http_code} bytes %{size_download}\n' \
    'https://web.archive.org/web/20250610015519id_/https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html'
HTTP 200 bytes 48536
a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d  cap25.html      <- byte-identical to live, as the header claims

$ curl -sS -A "$UA" -o cap22.html -w 'HTTP %{http_code} bytes %{size_download}\n' \
    'https://web.archive.org/web/20221207080111id_/https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html'
HTTP 200 bytes 62623
a0b48f21c9ebc41686da8a73ef315041e387cdb647b464e1a9d23247fd3107d6  cap22.html      <- differs from live in the FOOTER only; every quoted span present at the same para number
```

## Locator scheme, re-derived independently

Parser: `p` elements in document order inside `<div class="end_article">` (balanced-close extraction, single occurrence of that class, 93 open/93 close tags before the comment — no unclosed `p`, so a browser DOM and the regex agree on ordering).

```
end_article inner len 12846
p count in end_article: 94          (93 live + the commented-out 责编 line, last)
text-indent-2em p count: 92
P1 raw: <p style="text-align: center;"><img src="/NMediaFile/2025/0605/MAIN1749086898909M9RJ8546KH.JPG" width="708" height="404" alt=""></p>
P94 style: <p>(责编：虞婧)</p>       (inside <!-- … -->; last, so P1..P93 shift nothing)
headline inside any body p? False
```

2022 page: `total p: 78 non-empty: 78`, `para 1 = 您在使用一个 旧版本的 浏览器…` (browser-upgrade notice), `text-indent-2em p count: 69`.

Cross-check arithmetic the header states, re-derived:

```
P2 rank 1 | P3 rank 2 | P4 rank 3 | P5 rank 4 | P6 rank 5 | P8 rank 7
P61 rank 60 | P62 rank 61 | P66 rank 65 | P68 rank 67 | P69 rank 68
one-below for every locator: True (all 11)
2022: para 32 rank 31, 33→32, 34→33, 35→34, 51→50  (rank = n-1 for every 2022 locator)
```

## Per-span table (all 22 「」 spans in the first half)

`ch` = characters; all spans are CJK with no internal whitespace (1 whitespace token), all ≤ 37 ch — inside the Gate bound of ≤25 tokens / ≤80 ch. "Speaker" is the label printed on the served page for the paragraph the span sits in.

| # | where in file | locator as stated | span (verbatim) | ch | present at that locator | speaker on page |
|---|---|---|---|---|---|---|
| 1 | §1 b1 | headline (no P-number) | 我先设定世界观，再考虑怎么升级 | 15 | not in any body `p`; in `<title>` and `#newstit` | outlet (compression) |
| 2 | §1 b1 | P68 | 整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。 | 32 | YES | 爱潜水的乌贼 |
| 3 | §1 b3 | P8 | 作为一位“理工男”网文作家，您最擅长构建缜密恢宏的世界观 | 28 | YES (char offset 207 of P8) | 谭天 (question) |
| 4 | §1 b4 | para 32 | 很多网文在第一、二章就会基本上给出一个很明确的世界观 | 26 | YES | 李 |
| 5 | §1 b4 | para 34 | 有的网文作者会认为网络文学一开始就应该让大家明确世界观 | 27 | YES | 李 |
| 6 | §2 b1 | P68 (under 确定风格、设定世界、推导故事) | 整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。 | 32 | YES | 爱潜水的乌贼 |
| 7 | §2 b2 | P69 | 一开始其实不是所有设定都想好了。 | 16 | YES | 爱潜水的乌贼 (continuation) |
| 8 | §2 b3 | P69 | 是通过一次次的尝试、推导确定下来的。 | 18 | YES | 爱潜水的乌贼 |
| 9 | §2 b4 | P69 | 最后找到一条合适的路径，那就是唯一的答案。 | 21 | YES | 爱潜水的乌贼 |
| 10 | §2 b5 | P66 | 既然有了扮演法，那么晋升的过程就不能采用吸收灵气、冥想这种传统的方式。 | 35 | YES | 爱潜水的乌贼 |
| 11 | §2 b6 | P68 | 服食魔药和扮演法是符合世界观调性的升级方式 | 21 | YES | 爱潜水的乌贼 |
| 12 | §2 b7 | para 51 | 首先想的是，我的背景设定既然已经明确了 | 19 | YES | 乌贼 |
| 13 | §2 b7 | para 51 | 然后根据塔罗牌做一个力量体系设定 | 16 | YES | 乌贼 |
| 14 | §3 b1 | P68 | 万事万物都从最初造物主而来 | 13 | YES | 爱潜水的乌贼 |
| 15 | §3 b2 | P68 | “所有的非凡力量也从他而来”是个合理的推论 | 21 | YES | 爱潜水的乌贼 |
| 16 | §3 b3 | P68 | 这个推论要有物质性的表现，然后就有了非凡特性，并推导出一系列非凡特性定律。 | 37 | YES | 爱潜水的乌贼 |
| 17 | §3 b4 | P68 | 有了这些定律，我就觉得，服食魔药和扮演法是符合世界观调性的升级方式。 | 34 | YES | 爱潜水的乌贼 |
| 18 | §3 b5 | P61 | 我先把22张大牌拿来，看哪些可以用，哪些需要修改。 | 25 | YES | 爱潜水的乌贼 |
| 19 | §3 b5 | P61 | 然后从上往下推导出整个序列途径。 | 16 | YES | 爱潜水的乌贼 |
| 20 | §3 b6 | P62 | 越贴近现实就越有代入感 | 11 | YES | 爱潜水的乌贼 (continuation of P61) |
| 21 | §3 b6 | P62 | 等级很高以后，再用现实职业会很违和 | 17 | YES | 爱潜水的乌贼 |
| 22 | §3 b7 | P62 | 贴近现实、来源于现实、又能在现实中展现出神秘学魅力 | 25 | YES | 爱潜水的乌贼 |

Span-by-span outcome: **22/22 verbatim at the stated locator; 22/22 attributed to the speaker the page prints.** Punctuation is exact, including the full-width quotes inside #15 and the trailing 。 inside #2/#8/#10/#13(no)/#16/#17/#18/#19.

Speaker check on the quoted paragraphs (page-printed prefixes):

```
P60 谭天：… (question)        P61 爱潜水的乌贼：… (answer)   P62 设计的时候，我尽可能… (no label)
P65 项蕾：… (question)        P66 爱潜水的乌贼：…
P67 项蕾：… (question)        P68 爱潜水的乌贼：…            P69 一开始其实不是所有设定都想好了。… (no label)
P8  谭天：据我们观察，… (question, opens at 据我们观察)
```

## Header-row checks (all against the served pages)

| header claim | check | result |
|---|---|---|
| S883 URL, HTTP 200, 48,536 B, sha256 `a3b6640c…` | live refetch | TRUE (exact) |
| S884 URL, HTTP 200, 62,604 B, sha256 `344de345…` | live refetch | TRUE (exact) |
| byline as printed S883 | `来源：文汇报\u3000|\u3000邵燕君 谭天 项蕾\u3000\u30002025年06月10日09:01` | TRUE (byte-exact, incl. U+3000) |
| byline as printed S884 | `来源：《青春》\u3000|\u3000李玮 爱潜水的乌贼\u3000\u30002022年12月07日10:07` | TRUE (byte-exact) |
| title/newstit S883 | `爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”` | TRUE |
| title/newstit S884 | `爱潜水的乌贼：网络文学不断“升级”的“奥术”` | TRUE |
| breadcrumb both | `中国作家网>>网络文学>>访谈` | TRUE |
| 责编 虞婧, commented out, last p | `<!--<p>(责编：虞婧)</p>-->` | TRUE (both pages) |
| credit lines P3–P6 | 爱潜水的乌贼（网络文学作家）/ 邵燕君（北京大学中文系教授）/ 谭天（北京大学中文系博士生）/ 项蕾（中国社会科学院文学研究所助理研究员） | TRUE |
| roles printed only in credit lines | `教授->[4] 博士生->[5] 助理研究员->[6]` | TRUE |
| 编者按 P2: 北京大学网络文学研究团队, 十二位作家, 本系列访谈完整版将收入《创作者说：网络文学代表性作家访谈录》（北京大学出版社） | P2 full text | TRUE |
| URL path date 0605 ≠ printed 06-10 | path `n1/2025/0605/`, printed `2025年06月10日` | TRUE |
| 2022 page: no issue number, no interviewer affiliation | `第\d+期` count 0; 李玮 only `李玮（以下简称“李”）` | TRUE |
| 94 p / 92 text-indent-2em / ranks 67,68 | parser above | TRUE |
| 2022: 69 text-indent p, anchor rank 34 | para 35 rank 34 | TRUE (but see F8) |
| Wayback 20250610015519id_ byte-identical | same bytes, same sha256 | TRUE |
| Wayback 20221207080111id_ carries every span | 13/13 2022 spans at identical para numbers | TRUE (footer differs, after the article) |
| headline not inside any body p | substring absent from all 93 body p | TRUE |

## FINDINGS

### F1 — MEDIUM — §1's universal attribution sweep is false as written (two counterexamples, one inside §1)

§1 bullet 5: "Everything else quoted in this amendment is 爱潜水的乌贼's own answer, at the locator named beside it — his statement of what he did, not a claim about what the genre requires."

Counterexample (a), in the same section: bullet 1 quotes 「我先设定世界观，再考虑怎么升级」 and states in the same breath that it is "the outlet's compression, not the author's sentence". So a span quoted in §1 is not his answer, contradicting "everything else".

Counterexample (b), in §4: the only other non-author span in the file.

```
$ python3 - <<'EOF'   # every 「」 span in the file, with its stated locator
 15ch | headline (no P-number) | 我先设定世界观，再考虑怎么升级
 …
  5ch | para 32               | 到几十章后
EOF
```

`到几十章后` sits in para 32, whose page label is `李：`:

```
para 32 (doc p 32) ---
李：很多网文在第一、二章就会基本上给出一个很明确的世界观，但是这部作品的世界观是一点一点地拨开的。我也看到很多人评论说《诡秘之主》到几十章后大体上知道您的设定是什么…
```

§4 itself attributes it correctly ("the interviewer notes …"), so the file is internally inconsistent: §1 says every remaining quote is the author's; §4 says one is the interviewer's. A reader who trusts §1 and follows the locator finds 李's byline, i.e. the sweep, not the citation, is wrong.

**Fix (smallest):** scope bullet 5 to the sections it is true of — "Everything else quoted in §2 and §3 is 爱潜水的乌贼's own answer …" — and name the two exceptions in §4/§1 if the universal reading is kept.

### F2 — MEDIUM — §2 bullet 6 assigns second-step evidence to the third step, and re-uses a sentence §3 already spends

§2 b6: "The third step is a fit to the world-view's tone, decided after the laws exist: 「服食魔药和扮演法是符合世界观调性的升级方式」 (loc: P68)".

The page's own enumeration at P68 is 世界观 → 怎么升级 → 升级的表现, and the quoted sentence names 升级**方式** — i.e. how one upgrades, the second step. §3 b4 spends the same sentence (fuller form, 34 ch) on "the laws then decide the mechanics", which is the second step. So one sentence is load-bearing for two different steps, and the third step gets no page evidence of its own. The page's actual third-step material is the symptom passage at P68 (answering P67's 「为什么会让人在服用魔药后产生剧烈的痛苦和症状呢？」):

```
P68 爱潜水的乌贼：在设定上，非凡特性来自最初造物主，是外来物。你获得它之后，它对你的身体来说是外来力量，就会有痛苦的排异反应。整个过程里，我先做的是世界观…
```

Verified replacement span (32 ch, 1 token, verbatim in P68):
`你获得它之后，它对你的身体来说是外来力量，就会有痛苦的排异反应。`

**Fix (smallest):** in §2 b6 replace the quoted span with that sentence (keeping "decided after the laws exist" only if re-glossed, since this sentence follows from 非凡特性 being 外来物), or delete §2 b6 as duplicative of §3 b4.

### F3 — LOW — §1 bullet 3: the P8 span is not where the question opens

§1 b3: "谭天's question opens 「作为一位“理工男”网文作家，您最擅长构建缜密恢宏的世界观」 (loc: P8)".

```
P8 starts: 谭天：据我们观察，从2018年开始，网络
P8 idx of span: 207
```

The question opens 「据我们观察，从2018年开始…」; the quoted praise is 207 characters in. The quote is verbatim and 谭天's — only "opens" is wrong.

**Fix:** "谭天's question says/contains".

### F4 — LOW — §1 bullet 1: `<title>` does not "read" the quoted span; it contains it

```
TITLE: '爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”--网络文学--中国作家网'
NEWSTIT: '爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”'
```

The 15-ch span is a substring of both, not their full value. The bullet's point (quote the body, not the headline) is sound and the body span is at P68; only the verb "read" overstates.

**Fix:** "the page's `<title>` and `#newstit` carry".

### F5 — LOW — §2 bullet 2 glosses a design statement into a writing timeline, and leaves the 2022 answer unreconciled

§2 b2: "The order is a dependency order, not a plan finished before writing began: 「一开始其实不是所有设定都想好了。」 (loc: P69)".

P69 says only that not all settings were thought out at the start and were fixed through attempts and derivations; it dates no moment of writing. And §2 b7 quotes para 51 of the other source, whose answer opens:

```
para 51: 乌贼：对，一开始就设定好了。我记得是在11月《武道宗师》完结的时候…首先想的是，我的背景设定既然已经明确了…然后根据塔罗牌做一个力量体系设定
```

i.e. the ladder *was* fixed up front, which qualifies "not a plan finished" in a way the entry does not state. No contradiction is forced (P69 is about 所有设定, para 51 about the 序列), but the bullet's temporal gloss is the entry's, not the page's.

**Fix:** drop "before writing began" (P69 does not date writing), or add one clause noting that the 2022 answer says the ladder itself was fixed at the start while the rest was derived.

### F6 — LOW — §1's stated attribution mechanism does not cover two of its own quoted paragraphs

§1: "Both pages open each answer with the speaker's name, so every span below binds to a speaker."

Two quoted paragraphs carry no label on the served page:

```
P62 head: 设计的时候，我尽可能在中、低序列使用现实职业的名称…
P69 head: 一开始其实不是所有设定都想好了。是通…
```

Both bind correctly — P62 continues P61's answer, P69 continues P68's — but by paragraph continuity, not by the rule stated. A re-opener applying the stated rule literally would treat a label-less paragraph as unattributable.

**Fix:** "each answer opens with the speaker's name; continuation paragraphs carry none and bind by paragraph continuity (P62→P61, P69→P68)".

### F7 — LOW — header row uses "host" twice with two different referents

Header S883: "host 中国作家网 … 编者按 at P2 names the series host 北京大学网络文学研究团队". P2 says the series *invites* that team to select and interview twelve writers; the page's own host (breadcrumb/site) is 中国作家网. One row, two "host" values.

```
P2: 网络文学“破壁者”访谈邀请北京大学网络文学研究团队，选取…十二位作家进行长篇访谈…
```

**Fix:** "the series' interviewer team 北京大学网络文学研究团队".

### F8 — LOW — header's cross-check names no 2022 paragraph, so it does not meet its own "needs no inference" bar

Header: "the two anchor paragraphs are the 67th and 68th of the 2025 page's 92 … and the 34th of the 2022 page's 69". The 2025 anchors are named by P-number; the 2022 "anchor" is not. Only one 2022 paragraph is 34th (para 35, the tolerance paragraph), so the arithmetic is consistent — but a re-opener must guess which paragraph is meant, and para 33 (also an anchor quote in §4) is 32nd.

**Fix:** "…and para 35 is the 34th of the 2022 page's 69".

## Attacks that FAILED (the claim survived, with the evidence)

- **A1 fabricated fetch record — FAILED.** Live refetch reproduces 48,536 B / `a3b6640c…` and 62,604 B / `344de345…` exactly; both HTTP 200 under the browser-shaped UA, no wall.
- **A2 mislocated quote — FAILED.** 22/22 first-half spans verbatim at the stated P-number / para number (table above), including the two 2022 anchors at para 51 and the 2025 anchors at P68/P69.
- **A3 speaker mis-attribution — FAILED for every span.** P61/P62/P66/P68/P69 and para 51 are the author's; P8 is 谭天's question; paras 32/34 are 李's. (F1 attacks the *sweep sentence*, not any span.)
- **A4 locator scheme wrong — FAILED.** 94 `p` in `div.end_article` with the commented 责编 line last (93 live, so a DOM count gives the same P1–P93); P1 is the lead-image `p`; 92 `p` carry a `text-indent: 2em` style; ranks 67/68 for P68/P69; every locator's rank is exactly n−1; 2022: 78 non-empty `p`, para 1 = browser notice, 69 text-indent `p`, para 35 rank 34, every locator rank n−1. No unclosed `p` (93/93), one `end_article`.
- **A5 byline/credit/date drift — FAILED.** Both bylines byte-exact including U+3000 ideographic spaces; roles appear only in P4–P6; 责编 虞婧 present and commented out on both pages; both breadcrumbs `中国作家网>>网络文学>>访谈`; path date 0605 vs printed 06-10 as stated; 2022 page prints no issue number (`第\d+期` count 0) and no 李玮 affiliation.
- **A6 carrier claim inflated — FAILED.** `20250610015519id_` is byte-identical to today's live fetch (same 48,536 B, same sha256). `20221207080111id_` carries all 13 spans from that page at identical para numbers; its 19-byte difference is footer-only (live footer gained a disclaimer `p` and a copyright-line rewrite), i.e. after the article, so no locator drifts.
- **A7 headline inside a body `p` — FAILED.** `我先设定世界观` occurs in no body `p`; it is in `<title>` and `#newstit` only, as the entry says.
- **A8 over-long or non-verbatim quote — FAILED.** Every span is 1 whitespace token and 5–37 characters (Gate bound: ≤25 tokens, ≤80 ch); punctuation and inner full-width quotes match the page.

## Impacted axes and smallest safe corrections

- **coverage (claim C):** F2 (one admitted entry's central build-order bullet is evidenced by the wrong step; swap the span or drop the bullet). F3–F8 are wording fixes inside the same file. Nothing here touches ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, INDEX; no cited id or locator changes, so no leg flips.
- **calibration (claim Ca):** not impacted — Ca's SEPARABLE read set excludes `corpus/knowledge/**`, and this file is C's.
- **identity/provenance:** F4, F7, F8 are header-wording defects only; the fetch record, both carriers, the byline block and the locator scheme are exact.
- **Ranking if only one fix lands:** F1 (a false universal in the calibration section), then F2, then the five wording fixes in one pass.

## Tooling

No tool installed or upgraded. Python 3 (system), curl (system), git (system) only; no pacman. Scratch left under `/tmp/CritFactAmend1/` (page2025.html, page2022.html, cap25.html, cap22.html); nothing written under the fleet root, sibling lanes, `scripts/`, `templates/`, `.ufo/state`, or any other lane path.
