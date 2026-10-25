# ScoutIHChinaCapture — adoption re-grounding, source 1 (ihchina.cn register 清单页)

Seat: `L1Kotodama72.ScoutIHChinaCapture` · wave 72/w1 · role: scout (leaf, no dispatch)
Date of run: 2026-10-25 · repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`

## Verdict

All three sub-questions resolve **YES/positive**, and the live fetch succeeds.

- (a) 2020 capture contains the **四批** sentence and the **十大门类** sentence — both present (count 1 each).
- (b) 2026 capture contains the **五批** variant and the **same 十大门类** sentence (count 1 each); the 四批 wording is **absent** (count 0).
- (c) The 罗马数字 category-code rule sentence (`编号中的罗马数字代表所属门类`) is present in **BOTH** captures (count 1 each), byte-identical in the two files.
- Live fetch of `https://www.ihchina.cn/project.html` → **HTTP 200**, 43255 bytes, 3.31 s; content matches the 2026 capture except for the page's own date widget and one ad link.

## Artifacts (all under `/tmp/scoutihchina/` — nothing written outside the lane except this report)

| Path | What | sha256 |
|---|---|---|
| `/tmp/ihchina-2020.html` | pre-existing lane copy of the 2020 capture (40 834 B) | `d3274d85ea5433f0ff7871d8668db3f2bdd87e0995ae933f14ea73a57268c1b4` |
| `/tmp/ihchina-2026.html` | pre-existing lane copy of the 2026 capture (43 230 B) | `c0f46caa03722fdcc8e8979811f80d3dd33dbbafe91835a86abfb980a45125e1` |
| `/tmp/scoutihchina/arch-20200216023423.html` | my re-fetch, 2020 capture | `d3274d85…68c1b4` (identical to lane copy) |
| `/tmp/scoutihchina/arch-20261020183948-dec.html` | my re-fetch, 2026 capture (gunzipped) | `c0f46caa…25e1` (identical to lane copy) |
| `/tmp/scoutihchina/live-project.html` | live fetch, 2026-10-25 | `1510bc63462fc620575da92fbea33b0dbbb38df0e487533ad4d982bf7decef33` |

Both `/tmp` files were still present, so no re-fetch was strictly required; I re-fetched anyway to
provenance-check them, and both lane copies are **byte-identical** to the live Archive objects
(`cmp` → identical for 2020; identical after `--compressed` gunzip for 2026 — the raw `id_` 2026
object is gzip-encoded and only 10 370 B on the wire, which is why a naive byte-comparison against
the lane copy fails; decompressed it matches exactly).

## Provenance

CDX (`https://web.archive.org/cdx/search/cdx?url=www.ihchina.cn/project.html`):

```
20200216023423 200 NFU5XN6B23Q7UYH5DZFTP5CUZRXP6UNU 10786
20261020183948 200 KRPZLO6WABVPI3TKQ3MBPZMTIX735PJT 11742
```

Archive response headers confirm the origin server date:
`x-archive-orig-date: Sun, 16 Feb 2020 02:36:19 GMT` (2020 capture) and
`x-archive-orig-date: Tue, 20 Oct 2026 18:39:45 GMT` (2026 capture).

## grep -c evidence table

Command shape: `grep -c -- '<pattern>' <file>`.

| pattern | 2020 capture | 2026 capture | live (2026-10-25) |
|---|---|---|---|
| `国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录` | **1** | **0** | **0** |
| `国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录` | **0** | **1** | **1** |
| `国家级名录将非物质文化遗产分为十大门类` | **1** | **1** | **1** |
| `编号中的罗马数字` | **1** | **1** | **1** |

(The prompt's abbreviated five-batch probe `2014年和2021公布了五批国家级项目名录` also returns 1 in the
2026 capture and 0 in the 2020 capture.)

Line numbers of the hits: 2020 capture → line 353 (四批), 356 (十大门类 + 罗马数字);
2026 capture → line 368 (五批), 371 (十大门类 + 罗马数字); live → line 369 (五批), 372 (十大门类 + 罗马数字).

## Quoted context

### (a) 2020 capture, line 353 — 四批 variant (present)

> 国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录（前三批名录名称为“国家级非物质文化遗产名录”，《中华人民共和国非物质文化遗产法》实施后，第四批名录名称改为“国家级非物质文化遗产代表性项目名录”），共计1372个国家级非物质文化遗产代表性项目（以下简称“国家级项目”），按照申报地区或单位进行逐一统计，共计3145个子项，涉及国家级非物质文化遗产代表性项目保护单位3154个。…

### (a) 2020 capture, line 356 — 十大门类 + 罗马数字 rule (present)

> 国家级名录将非物质文化遗产分为十大门类，其中五个门类的名称在2008年有所调整，并沿用至今。十大门类分别为：民间文学，传统音乐，传统舞蹈，传统戏剧，曲艺，传统体育、游艺与杂技，传统美术，传统技艺，传统医药，民俗。每个代表性项目都有一个专属的项目编号。编号中的罗马数字代表所属门类，如传统音乐类国家级项目“侗族大歌”的项目编号为“Ⅱ-28”。

### (b) 2026 capture, line 368 — 五批 variant (present; the 四批 wording is gone)

> 国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录（前三批名录名称为“国家级非物质文化遗产名录”，《中华人民共和国非物质文化遗产法》实施后，第四批名录名称改为“国家级非物质文化遗产代表性项目名录”），共计1557个国家级非物质文化遗产代表性项目（以下简称“国家级项目”），按照申报地区或单位进行逐一统计，共计3610个子项。…

Note the list punctuation also changed: the 2020 capture writes `…2011年和2014年…` while the 2026
capture writes `…2011年、2014年和2021…` (a 、-list, four elements + 2021), so the two sentences are
**not** substring-variants of one another — the 2026 capture really is a revised text, not a
single-character patch.

### (b) 2026 capture, line 371 — 十大门类 + 罗马数字 rule (present, byte-identical to the 2020 capture)

Verified programmatically: the 170-character 十大门类 line and the 罗马数字 rule line are
**identical strings** in `/tmp/ihchina-2020.html` and `/tmp/ihchina-2026.html`
(`identical: True` for both).

> 国家级名录将非物质文化遗产分为十大门类，其中五个门类的名称在2008年有所调整，并沿用至今。十大门类分别为：民间文学，传统音乐，传统舞蹈，传统戏剧，曲艺，传统体育、游艺与杂技，传统美术，传统技艺，传统医药，民俗。每个代表性项目都有一个专属的项目编号。编号中的罗马数字代表所属门类，如传统音乐类国家级项目“侗族大歌”的项目编号为“Ⅱ-28”。

### (c) 罗马数字 category-code rule

Present in **both** captures (grep -c = 1 each) and in the live page. The rule as stated: the Roman
numeral inside a project number denotes the owning 门类, illustrated by the 传统音乐 project
“侗族大歌” with number “Ⅱ-28”. This is the sentence that grounds the *category-code* half of the
heritage-taxonomy theme; the 十-category list in the same line grounds the *taxonomy* half.

## Structural facts useful downstream (claim C)

- The 十大门类 list has exactly **10** entries and all 10 names occur in every one of the three
  artifacts (2020 capture, 2026 capture, live): 民间文学 / 传统音乐 / 传统舞蹈 / 传统戏剧 / 曲艺 /
  传统体育、游艺与杂技 / 传统美术 / 传统技艺 / 传统医药 / 民俗.
- The 2020 capture additionally states the 扩展项目名录 rule (“从第二批国家级项目名录开始，设立了扩展项目名录”);
  the 2026 capture carries the same sentence.
- Counts that changed between the two captures (useful if any entry quotes totals): 2020 = 1372 国家级项目 /
  3145 子项 / 3154 保护单位; 2026 = 1557 国家级项目 / 3610 子项 (保护单位 figure not in the quoted
  2026 span, only in the truncated tail — not verified, see gaps).

## Live fetch attempt

```
$ curl -sS -m 10 -L -o /tmp/scoutihchina/live-project.html \
    -w 'HTTP=%{http_code} SIZE=%{size_download} TIME=%{time_total} URL=%{url_effective}\n' \
    'https://www.ihchina.cn/project.html'
HTTP=200 SIZE=43255 TIME=3.307232 URL=https://www.ihchina.cn/project.html
```

Exit 0, within the 10 s budget (3.31 s). The live page carries the **五批** wording, the 十大门类
sentence and the 罗马数字 rule — i.e. it agrees with the 2026 capture.

`diff` live vs 2026 capture (whole file) yields only:

1. `<a href=/raylink_0></a>` — an ad/placeholder anchor present live, absent in the capture (line 75);
2. the page's own calendar widget: live `2026-10-25 星期日 / 农历九月十六` vs capture
   `2026-10-21 星期三 / 农历九月十二`.

No prose difference. This independently corroborates that the 2026 capture is a faithful snapshot of
the current page text and that no content drift occurred between 2026-10-20 and 2026-10-25.

## Unknowns / gaps

- The 保护单位 count in the 2026 capture was not read (the quoted line was truncated at 768 chars by
  the reader); it is presumably 3400-ish but is **not** verified here — treat any 2026 figure for it
  as unverified.
- Whether the lane's *intended* Archive URLs were exactly the ones above is inferred from the CDX
  hit and the capture-id naming in the assignment; the objects are confirmed to exist, be status
  200, and to match the lane's local copies byte-for-byte.
- I did not check whether the 2026 Archive object is the *only* capture in that week, nor whether
  any intermediate capture (e.g. a pre-2021 batch) would show an intermediate batch count — not
  required by the assignment.

## Tooling

No installs or upgrades performed this run; all work used pre-existing tools
(`curl 8.23.0`, `grep`, `python3` 3.x stdlib, `cmp`, `sha256sum`). Nothing was written outside
`/tmp/scoutihchina/` and this report file.
