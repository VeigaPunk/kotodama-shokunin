# RevEntryAmendFinal — round 74 wave 2 (falsify), hyaku run 7

**Seat:** RevEntryAmendFinal (leaf; no subagents, no background jobs, no repo mutation outside this file)
**Target:** `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` (91 lines,
2219 words; blob `f1ecf7f6c6989b1010ef2c700aa9ad5190f0630c` = `c4bf61a8d722f9168ce0fd8021a6261c000610c5:…`, equal
to the worktree file; added on main at `d7a3840`).
**Revisions:** base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; freeze `00c408a0af2fa5ddf65af2224152ce258b26d896`;
Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`.
**Claim read first:** `git show 00c408a0…:reports/round-74/claims.json` (claim C legs ENTRIES/ROWS/REPOINTED/GATE/
EVIDENCE/REJECTS/INDEX; corrections A1–A3, E1), plus `reports/round-74/claims.json` in the tree (byte-identical fields).
**Staged comparator (read-only):** `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`
(sha256 `39ac34ea…baf174588`; landed `cdab71c6…9369dd4529`).

## Verdict

**The attack FAILS: the landed amendment is a round-74 entry built on page text that is actually on the two pages,
the staged schedule/rule sentences are recovered (or explicitly reversed), the S895 superseded passage is absent, and
the single-source tier-C material is written as a tolerance, not a rule.** I record **1 MEDIUM + 5 LOW** fidelity
findings, all fixable in-place without touching any leg; none of them removes the support of a quoted claim.

## Fetch record (QUALITY 21/22/24)

Both pages were re-fetched by me, plain request, one attempt each, no challenge wall, no automation bypass:

```
$ curl -sS -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
    -o s883.html -w 'http=%{http_code} bytes=%{size_download} url=%{url_effective}\n' \
    'https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html'
http=200 bytes=48536 url=https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
$ … (same UA) … -o s884.html … 'https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html'
http=200 bytes=62604 url=https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html
$ sha256sum s883.html s884.html
a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d  s883.html
344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659  s884.html
```

Both hashes equal the amendment's own source-line hashes (`:3`, `:4`) and
`reports/round-74/evidence/S883.txt` / `S884.txt` — the pages did not move since the round-74 capture. No CDX probe is
needed here (both URLs answered live); no "unreachable" ruling is made.

## What I re-derived

1. **Every quoted span, at the locator the entry names.** I parsed the served HTML (`html.parser`, comments dropped,
   `div.end_article` scoped for the 2025 page; raw `<p>` order for the 2022 page) and searched each of the 34 `「…」`
   spans (33 distinct) against both pages:

   ```
   33 distinct spans: 16 resolve on the 2025 page — P8, P61, P62, P66, P68, P69 — 16 on the 2022 page —
   paras 32, 33, 34, 35, 51 — and 1 (the headline) only in <title>/<#newstit>.
   ```

   Every non-headline span was found **verbatim, once, at the stated locator**; the headline span
   `我先设定世界观，再考虑怎么升级` is absent from body `<p>` and present in
   `<title>爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”--网络文学--中国作家网</title>` and in `#newstit` — the
   entry says exactly that (`:21`). Full-paragraph checks (raw): P68 carries the order sentence, the premise, the
   inference, the material carrier and the laws sentence; P69 the iterative/pruning/one-path sentences; P61 the
   22-card and top-down sentences; P62 the realism/senior-rank/aim sentences; P66 the 扮演法 rejection; P8 the praise
   clause; 2022 paras 32/34 the interviewer's statements; 33 the hook/staged-release/reader-friendliness sentences;
   35 all six tolerance sentences; 51 the "setting already settled" pair.
2. **Locator schemes are the real ones.** 2025: 94 raw `<p>` in `div.end_article` (93 in the DOM; the commented-out
   `<!--<p>(责编：虞婧)</p>-->` is the last `<p>` in the region and is disclosed at `:6`), P1 = the lead-image `<p>`
   (`<p style="text-align: center;"><img …>`), 92 `text-indent:2em` paragraphs, **P68 = the 67th and P69 = the 68th**
   of them. 2022: 69 `text-indent:2em` paragraphs, **para 35 = the 34th**. The `:6` cross-check sentence reproduces
   exactly.
3. **Evidence windows.** Recomputed `window-sha256` from the stored window lines: S883 `b38075d3…456c18` over 4104
   chars, S884 `1618972c…c0cf81` over 4103 chars — both match the files' headers; each header quote is inside its own
   window. Window containment of the amendment's spans: **15/16 (2025)** and **14/16 (2022)** spans are carried by the
   round-74 windows; the three outside are `作为一位“理工男”…` (P8) and the two para-51 spans — those three rest on the
   live re-open only (residual risk, below).

## Findings

### F1 — MEDIUM — `:53` (and `:79`) turn a *tolerated* pattern into "the first failure mode"

`corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md:53`:

```
- The first failure mode is a first chapter that dumps the system: 「它的第一章就是抛设定，把世界观、整个修炼体系抛给你。」 (loc: para 35) (S884).
```

The sentence immediately after that quote on the page says the opposite about tolerance. Raw para-35 text
(2022 page, para 35 = 34th `text-indent:2em` `<p>`, verified by my parse):

```
乌贼：这个我肯定考虑过。我自己就是资深读者，作为读者，我对不同的小说有不同的容忍度，以前看早期的一些网络小说，它的第一章就是抛设定，把世界观、整个修炼体系抛给你。如果一部书刚开始抛给我的这个东西还算有意思，那我是能够读下去的。但如果一开始前面两三章都是设定，那我大概是不会看下去了，觉得信息量太大会阻碍我后面的阅读。但是反过来说，很多一开始设定不明确的小说我也是看不下去的，就是我不知道这是一个什么样的世界，需要做什么样的事情。但我这么多年的阅读经验和写作经验告诉我，如果开头足够有趣，有钩子，有悬念，那么你把…
```

`「如果一部书刚开始抛给我的这个东西还算有意思，那我是能够读下去的。」` is the practitioner's stated tolerance for
exactly the pattern F1's bullet calls a failure mode; the *stated* failure is the dump that **continues** (the entry's
next bullet, which is correct). The mislabel propagates to the §5 table (`:79`, "what it warns against: a first chapter
that explains the world"). This sits in the one section that must not overstate the tier-C row — the same defect class
the round is clearing for S899/S900 — though it overstates *severity*, not the source's existence.
**Fix:** relabel `:53` as the pattern he says he can still read, quoting the conditional
(`「如果一部书刚开始抛给我的这个东西还算有意思，那我是能够读下去的。」`, loc: para 35) and leave "the second" as the
stated stop-condition; adjust `:79`'s warning cell to "a first chapter that explains the world and is not interesting
on its own".

### F2 — LOW — `:3` and `:22` call P2 an `编者按`; the page has no such element

```
$ grep -c "编者" /tmp/RevEntryAmendFinal/s883.html
0
```

P2 is the untitled editorial intro (it really does name 北京大学网络文学研究团队, 十二位作家 and 将收入《创作者说：网络文学代表性作家访谈录》（北京大学出版社）, all verified). But the word `编者按` (and `编者`) never occurs on the page, so the
header field at `:3` ("编者按 at P2 names the series host…") and the §1 bullet at `:22` bind a page label that a
re-opener cannot find — the failure class the round's quarantine language is about, at label level.
**Fix:** "the editorial intro at P2".

### F3 — LOW — `:23` says 谭天's question "opens" the praise clause; it does not

```
谭天：据我们观察，从2018年开始，网络文学出现了新的变化。… (P8 offset 8764)
作为一位“理工男”网文作家，您最擅长构建缜密恢宏的世界观 (P8 offset 8971)
```

P8 opens with the observation clause; the praise sits mid-paragraph, before the closing question. The quoted span is
verbatim at P8, and the claim it supports ("the praise is framing, not a finding") stands.
**Fix:** "谭天's question says/contains".

### F4 — LOW — `:90` "about different books" is not supported; both quoted statements are about 《诡秘之主》

2025 P68 is the 诡秘之主 design answer (P60–P69 are the 序列途径/塔罗 discussion). The 2022 statement is elicited by
`李：《诡秘之主》的升级序列是开始就设定好的吗？` (para 50) and answered `乌贼：对，一开始就设定好了。…首先想的是，我的背景设定既然已经明确了，在《一世之尊》的时候就有雏形了…然后根据塔罗牌做一个力量体系设定` (para 51) —
the "setting settled first, ladder from tarot" order is about 诡秘之主 (with the setting's 雏形 inherited from
《一世之尊》). §2 already frames it as "the same order on its own" (`:35`); §6's "stated twice … about different books"
is the entry's own overstatement in its limits list.
**Fix:** "stated twice by the same author about his own working method (2022 para 51 also records the setting's 雏形
in 《一世之尊》)". Do not claim a second book's order — the entry's own §6 first line correctly refuses that.

### F5 — LOW — the 2022 locator scheme's "para 1 = the browser-upgrade notice" is a *conditional-comment* paragraph

The notice is at raw offset 3014, inside the IE conditional comment:

```
<!--[if lt IE 9]> … <p class="browserupgrade">您在使用一个 <旧版本的> 浏览器，请 … 更新你的浏览器 …</p> <![endif]-->
```

Browsers do not render it and an extractor that drops comments (the rule the round-74 evidence files record) does not
see it. Consequence: under the entry's scheme the anchor is **para 35** (verified); under the evidence files' own
extract rule it is **para 34**, yet `reports/round-74/evidence/S884.txt` carries `locator: para 35 (14th 乌贼 answer)`
— the label is consistent with `:6` but not with that file's stated extraction. The `:6` cross-check ("that scheme
sits one below every locator used here") makes the discrepancy recoverable, so this is a fragility note, not a
mispairing.
**Fix:** add to `:6` that the notice is inside an `<!--[if lt IE 9]>` conditional comment and is counted, or define
para n as the nth non-empty `<p>` *after* the notice (= extraction order), and update the evidence `locator:` label
accordingly.

### F6 — LOW (informational) — `:17` "Both pages open each answer with the speaker's name" has two cited counterexamples

```
P62 starts-with-name: False   (设计的时候，我尽可能在中、低序列使用现实职业的名称…)
P69 starts-with-name: False   (一开始其实不是所有设定都想好了。…)
```

Both are continuation paragraphs of the preceding 乌贼 answer (P61, P68), so attribution is **correct** and every span
still binds to the author; the sentence is true only if "answer" means one speaker turn, not one paragraph.
**Fix:** "each speaker turn opens with the name; P62 and P69 are continuations of the 乌贼 answer that begins at P61/P68".

### F7 — LOW (cross-file consistency) — `corpus/SOURCES.md:839` says "never sole support" while the entry's `:11` says §4 rests on that row alone

```
S884 tier cell: … tier C: one practitioner's hedged tolerance (问题不大), a lead never a measured rule and never sole support …
amend :11: … §4 rests on that tier-C row alone and is therefore written as one practitioner's stated tolerance, a lead …
```

Read together they contradict. `:11` is the defensible one (a lead resting on one row, never a rule about the world);
the cell's unqualified "never sole support" is what a re-opener will quote against §4.
**Fix:** cell → "never sole support of a claim about the world; the disclosed-tolerance lead rests on it alone, as a
lead".

## Attacks that FAILED (the claim survived)

1. **"Is it a round-74 entry built on page text actually carried?" — PASS.** Live bytes equal the round-74 capture
   hashes (above); all 33 distinct spans verbatim at their stated locators (above); evidence `window-sha256` recomputes
   (above); the file's mainline add is `d7a3840` and its C-lands blob equals the worktree blob
   `f1ecf7f6c6989b1010ef2c700aa9ad5190f0630c`. Blob differs from the staged file (`cdab71c6…` vs `39ac34ea…`).
2. **"Does any staged sentence survive unrecovered?" — PASS.** Sentence-level diff: of 44 staged sentences >25 chars,
   6 match landed text and every one is a URL fragment or the generic header prefixes
   (`- couples: \`culture-material/worldbuilding-setting-practice.`, `- scope: an amendment to the worldbuilding-practice
   entry.`); the only fuzzy verbatim blocks ≥40 chars are the two URLs. Every staged *claim* is either corrected or
   reversed: "delivery schedule" → tolerance with "it is never the entry's rule" (`:11`), and §4's lead-in at `:51`
   ("It is a lead for designing a disclosure plan; it is not a rule of serial fiction"); "paired so that neither is the
   sole support" → "no pairing of the two rows is claimed" (`:11`); staged ground/recheck (round-3 CANNOT-ANSWER,
   S754/S742/S743, round-4 recheck commands) → replaced, and those ids/strings occur 0 times.
3. **"Is the staged superseded passage (S895) absent?" — PASS.**

   ```
   $ grep -n "S895\|Superseded\|预设缺陷\|叙事驱动机制\|价值共识框架\|S-A-B-C\|王昕玥\|2025/1030" \
       corpus/knowledge/culture-material/worldbuilding-setting-practice.md \
       corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md corpus/README.md
   (no output)
   ```
   The only occurrences in the tree are the declared reject (`corpus/lessons/round-74.md:36`) and the map note
   (`:88`); the two entries and the README index carry none of S895, the 2025/1030 URL, or its terms.
4. **"Is the single-source tier-C schedule stated as a rule?" — PASS.** §4 is titled "One practitioner's stated
   tolerance, on a single tier-C row" (`:49`), opens "It is a lead … it is not a rule of serial fiction" (`:51`), the
   20-chapter quote is given with its hedge (`:58`, `:89`), and §6 says "never quotable as a rule of serial fiction"
   and "nothing in either row supports a hard boundary at twenty or at any other number" (`:88`–`:89`). The only numeric
   survival is §5's *question* "…inside roughly the first twenty chapters, if the hook holds?" (`:80`), under the
   "three prompts … not as a test anyone passes" heading (`:78`) — conditional, attributed, and disclaimed at `:89`.
   Recorded as residual risk, not a violation.
5. **Quarantine clearing (all four conditions at `corpus/lessons/round-74.md:146-151`):**
   - S816/S817 refused and not edited: the registry diff base..lands changes only S877's line plus S881..S884
     (`git diff --stat f7104cb…c4bf61a -- corpus/SOURCES.md` → `5 insertions(+), 1 deletion(-)`; changed rows = S877,
     S881, S882, S883, S884). The lane rows numbered S816/S817 are unrelated medicine rows — the "register S816/S817"
     naming is the round-71 quarantine-slice register, and the lesson's bridging is by document, which is sound.
   - Documents re-opened as new rows S883/S884: `corpus/SOURCES.md:838-839`, tier cells B and C, `mined`,
     `2026-10-25`, `180d`, used-by exactly the amendment path.
   - Quote located this round from the round-74 capture: verified above, including the two mispaired classes —
     `这个我肯定考虑过` occurs **0** times on the 2025 page and **1** time on the 2022 page (para 35); the Sowers-Wills
     clause occurs 0/0 on either page.
   - Admitted bytes are a round-74 entry, not the staged text: blob compare above, plus (2).
6. **Staged ids never cited as lane rows — PASS.** Inline ids in the amendment: `S883` ×20, `S884` ×16, nothing else;
   `S899/S900/S816/S817` and `S729/S730/S742/S743/S754/S895` occur 0 times in either entry.
7. **Same entry criteria as the base entry — PASS.** Header fields first and in claim order (`source` ×2,
   `verified-at`, `recheck`, `ground`, `topic`, `gap filled`, `sources`, `couples`, `scope`), no placeholder value, no
   `<…>` in a header field, 6 `## §` sections, 2219 words (body > the 478-word floor). Every line containing a `「…」`
   span also carries `loc:` and `(S883)`/`(S884)`; longest span 37 characters. `python3 -B tools/check-cited-lines.py`
   → `CITED-LINES: 0 finding(s) in 1 file(s)`. `corpus/README.md:445` carries the entry's `- topic:` text verbatim.

## Residual risk and verification gaps

- **Three spans are outside the stored 4096-char windows** (P8 praise; the two para-51 spans). A purely offline
  counter cannot re-confirm them from the round-74 capture; my live re-open (byte-identical body) is the bridge.
  Compounding, `first`-order only: these three are exactly the spans F3/F4 touch, so their capture support and their
  prose framing are both thin spots.
- **F5 fragility:** the 2022 locator scheme counts an unrendered conditional-comment paragraph as para 1; any future
  re-opener using an extractor lands one paragraph early (34 vs 35). The `:6` cross-check recovers it, but a re-quote
  gate should not depend on that inference.
- **F7 consistency:** the registry tier cell and §4 say different things about sole support; neither breaks a claim
  leg, but a reader quoting the cell can call §4 unsupported.
- I did not run `accept-c.py` / `accept-ca.py`: the amendment's support was testable directly, and the counters are not
  this seat's instrument. Nothing in this report depends on a counter result.
- One stray (non-blocking, not on any branch): `b261eab` (empty subject; parent = Ca lands `5e4796c0`) adds the same
  two entries and is not an ancestor of `main`; the C-lands blob and the worktree agree, so it changes nothing graded.
- Tool installs: none. Fetch hygiene: one plain request per URL under the recorded browser-shaped UA; no wall, no
  automation bypass, no "unreachable" ruling claimed.
