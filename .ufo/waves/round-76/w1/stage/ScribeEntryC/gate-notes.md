# Gate notes — ScribeEntryC (round 76, wave 1), candidate c: `era-periodization-models.amend-2026-10-23b`

Seat: ScribeEntryC. Target: `corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md`.
Staged text read: `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md` (a 'Proposed body' outline, not a finished entry).
Draft returned: `.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md`.
Date of every access below: **2026-10-27**.

## Verdict

**ADMIT the entry.** Every factual sentence in the draft is carried by one located span in the served bytes of the
one cited page. The entry is admitted on one row (S894), a live public search form read by a plain request. Two legs of
the staged plan were **dropped rather than softened** — the Wayback capture (unreachable, §B) and the "library's
classification ladder" / "four period axes" outline (§C) — and one earlier lane verdict about this same URL is
**corrected** (§D). If the served page stops carrying the tables, the entry's §1–§3 lose their support and the row
becomes unverifiable; that is stated in the entry's own recheck line.

## A. Source cited in the entry — S894

| field | value |
|---|---|
| lane id | S894 (planned id from CLAIMS-DRAFT; campaign ids S908 / S935 are **not** cited anywhere) |
| URL | `https://www.digital.archives.go.jp/search` |
| access date | 2026-10-27 |
| User-Agent | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` |
| response | HTTP/2 200, `content-type: text/html;charset=UTF-8`, `content-language: ja`, **311,308 bytes**, `date: Tue, 27 Oct 2026 21:35:49 GMT`, `server: Apache`, `x-cache: Miss from cloudfront` |
| sha256 | `204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8` |
| repeat | two fetches on 2026-10-27 were byte-identical (`cmp -s` → IDENTICAL) |
| access control | plain GET, no cookie sent, no login, no paywall, no captcha, no geo block, no challenge met. Nothing routed around. |
| evidence | `.ufo/waves/round-76/w1/stage/ScribeEntryC/window.txt` (extracted tables and located spans) and `.../na-search.html` (the raw 311,308 bytes) |

**Located quotes** (each ≤25 words / ≤80 chars; byte offset is into the raw served bytes; every one of these strings
also appears verbatim in `window.txt`, which is the committed window):

| quote | location | verdict |
|---|---|---|
| `元号名称` | `#gengo-modal`, first `<th class="gengo-modal__th">`; raw-byte offset 111269; 3 occurrences (one heading per tab) | ADMIT |
| `開始西暦年` | same table head, second `<th>`; raw-byte offset 111337; 3 occurrences | ADMIT |
| `和暦元号` | tab label, `<span>` inside `nav.gengo-modal__tabs`; offset 110546; 1 occurrence | ADMIT |
| `中国元号` | tab label; offset 110729; 1 occurrence | ADMIT |
| `朝鮮元号` | tab label; offset 110912; 1 occurrence | ADMIT |
| `年月日(元号)` | the form row label in the detailed-search form; offset 69809; 1 occurrence | ADMIT |
| `date_e_from_era` | hidden input, `id="date-gengo-1-from"`; offset 70602; 1 occurrence | ADMIT |
| `date_y_from_era` | hidden input, same row; offset 71307; 1 occurrence | ADMIT |
| `文治` | 和暦元号 table, row index 141, year cell `1185`; offset 189353 | ADMIT |
| `大化` | 和暦元号 table, last row (index 247), year cell `645`; offset 247643 | ADMIT |
| `金収国` | 中国元号 table, last row (index 93), year cell `1115`; offset 301158 | ADMIT |
| `朝鮮乾隆` | 朝鮮元号 table, first row (index 0), year cell `1736`; offset 302517 | ADMIT |
| `元至元` | 中国元号 table, rows 37 and 48, year cells `1335` and `1264`; offset 269647; 6 occurrences (name + the same name in 元至正/元至順 substrings are separate strings, see window) | ADMIT |
| `清乾隆` | 中国元号 table, year cell `1736`; offset 253995 | ADMIT |

**Row counts as observed** (from `window.txt`, re-derivable by the entry's recheck command): 和暦元号 **248**, 中国元号 **94**, 朝鮮元号 **8**.
**Dynasty grouping in 中国元号**: 康徳 1, 大同 1, 民国 1, 清 13, 明 20, 元 14, 南宋 23, 金 21 (sums to 94).
**Out-of-order block in 和暦元号**: indices 83–90 (`元中 1384` … `延元 1336`) sit between `暦応 1338` (index 82) and `建武 1334` (index 91).

**Reason for ADMIT**: the three tables are server-rendered inside `#gengo-modal` in the served HTML — no script
execution, no cookie and no second request were needed — and each sentence of the draft points at a span in that block.
**Flip**: a re-fetch that serves no `#gengo-modal` tables, or that serves a different set of row counts, marks the row
unverifiable and the affected entry sections unsupported; the row is never paraphrased into support.

## B. Leg that did NOT resolve — the Wayback capture (recorded, not cited)

The staged plan paired campaign S908 with campaign S935, "a Wayback capture of the SAME page". It was **not usable**
here and is **not cited**:

- `https://web.archive.org/cdx/search/cdx?url=digital.archives.go.jp/search&output=json&limit=40&filter=statuscode:200&collapse=digest` → `curl: (7) Failed to connect to web.archive.org:443`, 0 bytes.
- `https://web.archive.org/web/2024/https://www.digital.archives.go.jp/search` → HTTP 302, 0 bytes.
- same URL with `-L` (follow redirects, 40 s cap) → `curl: (7) Failed to connect to web.archive.org:443`, 0 bytes.

Verdict: **unrun / unreachable**, not "absent". No claim is made about what any capture holds, and the entry says so in
its §6. The live page served the same content, so the capture was not needed for admission.

## C. Staged sentences DROPPED (they overreach the page)

- The staged file couples to `culture-material/era-periodization-models.amend-2026-10-23.md` — **that path does not
  exist** in the lane at base 98c486b (`git ls-tree -r --name-only 98c486b | grep -i era-period` → 2 paths, neither an
  amendment). The draft's `couples:` line names only paths verified present with `git cat-file -e 98c486b:<path>`.
- The staged file calls `S757` "round 4's library-classification amendment". The lane's S757 is Huizinga, *Homo Ludens*
  (`corpus/SOURCES.md:713`). The attribution is wrong and is not repeated anywhere in the draft.
- The staged "§N+1 Four period axes" (archive, library, museum, heritage) is **not written**. Only the archival axis is
  carried by the opened page; the library, museum and heritage ladders are unopened this round. The draft instead has
  §4, one instrument's checks, and §6 states the limit.
- The staged claim that the archive's table is "the era-name sequence … onward to the earliest names" is kept only in the
  form the bytes carry: 248 rows, `令和 2019` first, `大化 645` last, `文治 1185` at index 141 — the draft prints those,
  not a claim that the sequence is complete for all of Japanese history.
- No sentence in the draft asserts the ordinal of 令和 (the page does not state one), nor which records fall under each
  list (marked `(to-verify)`), nor what the English-language surface shows (marked unobserved).

## D. Correction filed against this lane's own record

The lane's round-68 lesson (`corpus/lessons/round-68.md:112`) records a **refusal** of this same URL: "S825
(digital.archives.go.jp/search is a portal landing, not the table page)". Campaign S935's row in
`/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` goes further and states "the live search page no longer
serves this text; the archived capture does".

Both are contradicted by the 2026-10-27 served bytes: the page **is** 詳細検索 and **does** carry three era tables, and
the campaign's own S908 recheck in the same file (`grep -c '元号名称'` → 3, ran 2026-10-23) already reported the heading
present live. The likely cause is check shape, not document state: the campaign's quote is a **concatenation**
(`元号名称 開始西暦年 令和 2019 平成 1989 …`), and those tokens are separated by `<th>` markup in the raw bytes, so a
literal raw-byte span test fails while a tag-stripped text test passes. The entry therefore locates each token
separately, and says which surface (raw bytes vs extracted text) a locator means.

Verdict on the earlier refusal: **corrected for this scope** — the reason "not the table page" does not hold. This is a
finding for the round's `## Collision guard`, not a judgement on any other candidate.

## E. What was checked mechanically

- `python3 -B tools/check-cited-lines.py <draft>` → `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0.
- `git grep -c '元号名称\|開始西暦年\|国立公文書館' 98c486b -- corpus/knowledge` → no output, exit 1 (the claim's
  before-state leg, run in the lane by read-only git).
- `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` → **one** file, `corpus/lessons/round-68.md`; the
  claim's declared "each print nothing (exit 1)" is **false as printed** for this host. Reported to the L1, not edited.
