# ScribeEntryD — round 76 / W1 — candidate d (calendar-festival-systems.amend-2026-10-23c.md)

Seat: scribe, leaf. Lane base: `98c486bdb4650ba5b8e651d332910e8ee60ad121`. Repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Scratch `/fast/scratch/hyaku/kotodama-r76/ScribeEntryD/` removed after receipts were copied to `.ufo/waves/round-76/w1/stage/ScribeEntryD/`.

## Verdict

**REFUSE candidate d.** The staged body's central claim — that the lane can now quote *the standard's own clause text* — cannot be carried by any A/B row, and the page it cites does not contain the standard's text at all. The refusal record is at `.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md` and is marked `status: REFUSED` on line 3; it must not be installed.

Two independent located reasons:

1. **The page has no 原文 block.** The cited page's title promises 原文及解读材料, but its body is a 解读-shaped explanation; the sweep below returns 0 for every structural heading a Chinese standard's text carries. The rules it prints are introduced in the drafting voice (「本标准沿用规则如下」), not as clauses.
2. **No A/B carrier repeats the load-bearing sentences.** The state press carries two of the five compilation rules, the model, the 1-second precision, the publication duty and the drafter; it carries none of the leap rule, none of the naming methods, and not the source-labelling duty (sweep counts 0). The registry record carries metadata only.

## Commands and raw output

### Base state

```
$ git grep -l -E "GB/T 33661" 98c486b -- corpus
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/lessons/round-68.md
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/lessons/round-69.md
exit=0

$ git grep -l -E "digital\.archives\.go\.jp" 98c486b -- corpus
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/lessons/round-68.md
exit=0

$ git grep -l -E "GB/T 33661" 98c486b -- corpus/knowledge
exit=1

$ git grep -l -E "digital\.archives\.go\.jp" 98c486b -- corpus/knowledge
exit=1

$ git grep -l -E "农历的编算" 98c486b -- corpus
exit=1

$ git grep -l -E "紫金山" 98c486b -- corpus
exit=1

$ git grep -c -E "GB/T 33661" 98c486b -- corpus/lessons/round-68.md corpus/lessons/round-69.md
98c486b…:corpus/lessons/round-68.md:1
98c486b…:corpus/lessons/round-69.md:2
```

So the lane **holds no knowledge file** that names the standard (0 — `git grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge`, exit 1) and **no file at all** that prints its Chinese title or its drafter (0 and 0 — the two greps above, both exit 1). The gap is real; the carrier is not.

Couples check for the three paths the staged entry names:

```
$ git cat-file -e 98c486b:corpus/knowledge/culture-material/<path>; echo exit=$?
calendar-festival-systems.amend-2026-10-23.md          -> exit=128
era-periodization-models.amend-2026-10-23b.md          -> exit=128
calendar-festival-systems.md                           -> exit=0
```

1 of 3 resolve — `calendar-festival-systems.md`. The other 2 do not exist at base.

### Fetches (2026-10-27, plain curl, browser-shaped UA)

UA used for every request: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`.

```
S895 https://www.xingzuobaike.com/huangli/wannianli/d165803.html
  http=200 bytes=33179 ct=text/html; charset=utf-8
  sha256 830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e

S896 (live) https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296
  http=200 bytes=7334 (raw compressed; 24144 B after decoding) ct=text/html;charset=utf-8
  sha256 80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9

S896 (bound capture) https://web.archive.org/web/20260424031027id_/…newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296
  four attempts, all: curl: (7) Failed to connect to web.archive.org:443 after ~190 ms: Could not connect to server
  http=000 bytes=0
  curl -sS -I https://web.archive.org/            -> same exit 7
  timetravel.mementoweb.org                        -> curl: (6) Could not resolve host

S898 https://news.gmw.cn/2017-05/23/content_24559485.htm
  http=200 bytes=8076 (raw compressed; 25250 B after decoding) ct=text/html
  sha256 670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1
```

### openstd probes — the full text is not served

```
showGb?type=online&hcno=…    -> HTTP/1.1 302  Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=…&refer=outter
showGb?type=download&hcno=…  -> HTTP/1.1 302  Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=…&refer=outter
/bzgk/gb/showGb?type=online  -> HTTP/1.1 301  Location: https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=…
/bzgk/gb/newGbInfo?hcno=…    -> HTTP/1.1 301  Content-Length: 162
```

The record page itself prints 「当前浏览器暂不支持标准全文在线预览服务」 and carries no rule text (48 extracted lines: number, both titles, status 现行, CCS A46, ICS 07.040, 发布日期 2017-05-12, 实施日期 2017-09-01, 主管部门/归口部门 中国科学院, 发布单位 国家质检总局 + 国家标准化管理委员会).

### Negative sweeps

S895, counts over the served text:

```
前言 0 | 范围 0 | 规范性引用文件 0 | 术语和定义 0 | 原文 2 (both in the title lines, neither in the body)
编排规则 5 (all inside the 解读 body)
```

S898, counts over the served text:

```
闰 0 | 置闰 0 | 干支 0 | 生肖 0 | 中气 0 | 资料 0 | 北京时间 0 | 334 1
```

Exact strings confirmed present on S898 (`grep -o`): 「朔日为农历月的第一个农历日」「包含冬至在内的农历月为农历十一月」「精度应达到1秒」「必须包含公历和农历的日期对照以及二十四节气」「中国科学院紫金山天文台起草编制」.

Exact strings confirmed present on S895: 「本标准沿用规则如下」「公开发行的农历日历应注明资料来源」「取其中最先出现的一个不包含中气的农历月为农历闰月」.

### Draft checks

```
$ python3 -B tools/check-cited-lines.py .ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md
CITED-LINES: 0 finding(s) in 1 file(s)
exit=0
```

(First run reported `MULTI-ID …:14 S895,S896,S898`, exit 1 — the `- sources:` bullet carried three ids on one line; it was split into three bullets, one id each. The output above is the post-repair run.)

```
body words from "## §1": 1600
table rows carrying an id: 0
```

## What the counts mean for the entry

Load-bearing sentence → A/B carrier → result, in full, is in the draft's §2. Summed: 6 of 11 staged statements are carried by S898 and 5 are not; S896 carries none; S895 is tier C and is the only carrier of the five.

## Findings

- **F1 — HIGH — the claim's declared before-state is false at base.** Claim C says `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` each print nothing (exit 1). Both print files and exit 0: the first prints 2 (`corpus/lessons/round-68.md`, `corpus/lessons/round-69.md`), the second prints 1 (`corpus/lessons/round-68.md`). Smallest fix that keeps the claim's intent: scope both to `corpus/knowledge` — under that path both exit 1 (shown above). As frozen, the claim's own before-leg fails on its first check.
- **F2 — HIGH — candidate d's premise is false.** The cited page carries no 原文: 0 hits for 前言, 范围, 规范性引用文件, 术语和定义; `原文` occurs only in the title lines. The rules are the drafter's description inside 标准主要内容, introduced by 「本标准沿用规则如下」. Whether the document is a 编制说明 or an official-style 解读 is `[INFERENCE]` from that heading shape and first-person drafting voice; either way it is not the standard's text, i.e. the same carrier class the entry said it would replace.
- **F3 — HIGH — the admission rule fails.** No A/B row carries the leap rule, the four naming methods, rule (1), rule (5), or the source-labelling duty (S898 sweep 0 for 闰, 置闰, 干支, 生肖, 资料, 北京时间; S896 has no rules). A tier-C-only clause text would also be the sole support of an admitted entry, which the claim's kill rule forbids.
- **F4 — MEDIUM — S896's bound capture does not open from this host.** Four attempts, `curl: (7) … Could not connect to server`, http=000. The live document at the same `hcno` does open (HTTP 200, 24,144 B decoded). If the row is kept, re-point it to the live URL and re-test the capture later; if the capture is required as the bound form, the row is unopenable here and must be refused on that ground alone.
- **F5 — MEDIUM — S897 and S896 are one document today.** `showGb?type=online` 302s to `newGbInfo?…&refer=outter`, and `showGb?type=download` 302s the same way; the `/bzgk/gb/` variants 301 into `/bzgk/std/`. The plan's two registry rows resolve to one page, which the by-document id map must record (else the row count inflates by one and the "one row per document" leg breaks).
- **F6 — MEDIUM — the staged file's couples line names 2 files that do not exist at base.** `calendar-festival-systems.amend-2026-10-23.md` and `era-periodization-models.amend-2026-10-23b.md` both exit 128 under `git cat-file -e 98c486b:…`; only `calendar-festival-systems.md` resolves. An as-is install fails QUALITY 5 on the couples line alone.
- **F7 — LOW — the staged file uses campaign ids in a lane-shaped field.** Its `gap filled:` bullet calls S718 "the standard's registry record" and S719 "the interpretation". At base, lane `corpus/SOURCES.md:673` is S718 = Farran et al. 2016 (infant-directed speech, PLOS ONE) and `:674` is S719 = Cristia 2013 (input to language). The numbers there are campaign ids; the entry would have cited two unrelated papers by number. This is the exact id-space collision the round's collision guard exists for, and it survives into the staged text.
- **F8 — LOW — the staged provenance trio is stale and points at a command it does not give.** `fetched 2026-10-23`, `verified-at: 2026-10-23`, and `recheck: 180d — re-run the row recheck command in round 6's SOURCES-PROPOSED.md (S916 -> 1)`. The seat requires `verified-at: 2026-10-27` and a recheck that is a command or a cadence; a pointer to another round's file is neither, and the round-6 file is not in this round's package.

## Out of scope, unrun, and untouched

- `CLAIMS-DRAFT.md` not edited. The registry not edited. No other seat's files touched. No writes outside `.ufo/waves/round-76/w1/` and my scratch.
- Not run by me, reported as unrun: the census (`tools/census.py` or the round's census counter), `reports/round-76/accept-c.py`, and any counter. This seat produced a draft and its gate record only.
- Installs: **none**. No pacman invocation of any kind; no tool installed or upgraded; nothing written to `~/.local/bin`.
- Fixture repos: none created (no git mutation was needed; all git use was read-only `git grep` / `git cat-file` / `git ls-tree` / `git show` against `98c486b`).
- Scratch: `/fast/scratch/hyaku/kotodama-r76/ScribeEntryD/` deleted after the receipts below were copied.

## Artifacts

- Refusal record (draft path, NOT installable): `.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md`
- Gate notes (per-source, quote + location + status + verdict + flip): `.ufo/waves/round-76/w1/stage/ScribeEntryD/gate-notes.md`
- Fetch log: `.ufo/waves/round-76/w1/stage/ScribeEntryD/fetches.txt`
- Served bytes, as fetched today: `.ufo/waves/round-76/w1/stage/ScribeEntryD/s895.html`, `s898.html`, `newgb.html` (sha256 in `fetches.txt`), with their tag-stripped text extrusions `s895.txt`, `s898.txt`, `newgb.txt`
