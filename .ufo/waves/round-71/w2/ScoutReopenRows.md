# ScoutReopenRows — wave-2 re-open of 5 quarantine rows (round 71)

Ticket: re-open 3 quarantine PRESENT rows (S795, S804, S823) and 2 REFUSED rows (S779,
S814) from the evidence in `ScoutQuarantineFetch{1,2,3}.md`, and re-confirm each verdict
against the frozen table `reports/round-71/telemetry/quarantine-verdicts.md`.

Method: each cited URL re-fetched live (curl), payload text extracted, and the register's
quoted span searched under (a) exact match, (b) whitespace-normalised match, (c) whitespace
+ page-number-stripped match. Every live payload was also cross-checked against the
read-only capture cache `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache`
(SHA-256(URL) prefix). Row identity, URLs and spans were taken from the register itself
(`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`),
not from the lane's `corpus/SOURCES.md`, whose S-numbers are a different id space (lane
S795 is an incense-clock article, lane S804 a Smithsonian object record, lane S823 a
barber-surgeon paper — the verdict table's ids are register ids). No lane bytes were
written; no tools installed. Scratch dir `/tmp/r71reopen`.

## Re-confirmation summary

| row | table verdict | re-derived | verdict holds | note fidelity |
|---|---|---|---|---|
| S779 | REFUSED | REFUSED | **PASS** | PASS — plus root cause found (quote belongs to a different document) |
| S795 | PRESENT | PRESENT | **PASS** | **FAIL (precision)** — enumerated span is in the 目次, not the §II body; page number interleaved at the break |
| S804 | PRESENT | PRESENT | **PASS** | **FAIL (precision)** — source uses `，` not the register's `、`; quote is in the 世界大百科事典（旧版）mention block, not the headword |
| S814 | REFUSED | REFUSED | **PASS** | PASS — plus root cause found (quote is an NDC10 classification note) |
| S823 | PRESENT | PRESENT | **PASS** | PASS — but live fetch is flaky (HTTP 400) and the page is GB18030 |

Net: **5/5 verdicts re-confirm**; **2/5 table notes carry anchor/punctuation imprecision**
that a downstream adoption round would inherit verbatim if not fixed.

## Per-row evidence

### S779 — REFUSED (PASS)

```sh
curl -sSL --max-time 60 -A 'Mozilla/5.0' -o s779.html \
  'https://www.nao.ac.jp/news/topics/2026/20260202-rekiyoko.html'
# 200 22950 text/html
sha256sum s779.html  # 65b55e3b8652378dda088d7e6ae7b121160910d16aaa51c298fb591243d32366
# == .qcache/be01c59af8a7f28f50c450ab.raw (byte-identical, 22950 B)
```

Spans from the register, tested on whitespace-stripped body (2,622 chars of text):
`国务院先后于2006年` → False; `国家级名录将非物质文化遗产` → False; `十大门类` → False.
Page title is `令和9（2027）年暦要項の発表 | 国立天文台(NAOJ)`; content is Japanese calendar
publications (国民の祝日 / 二十四節気 / 朔弦望). Outbound links are only
`eco.mtk.nao.ac.jp/koyomi/` and NAOJ site links — no document carrying the Chinese spans.
The fetched body has 169 distinct Han characters, all Japanese-kanji usage, and no Chinese
sentence from the register.

Root cause (new, beyond wave 1): the register's spans belong to a **different document**.
Verbatim first span located on
`https://wlt.hubei.gov.cn/hbsfwzwhycw/mtgz/xwdt/202403/t20240325_5132510.shtml` (200, 35555 B):

> 国务院先后于2006年、2008年、2011年、2014年和2021公布了五个批次的国家级非物质文化遗产代表性项目名录，共含1557个国家级非物质文化遗产代表性项目 … 国家级项目分为十大门类

(`十大门类` → True on that page; the register's second span `国家级名录将非物质文化遗产分为十大门类…`
is a paraphrase, not verbatim, of `国家级项目分为十大门类`.) So S779 is a URL↔quote mispairing,
not a source that lost its payload. REFUSED is the correct verdict for the cited URL.

### S795 — PRESENT (PASS on verdict; table note imprecise)

```sh
curl -sSL --max-time 90 -A 'Mozilla/5.0' -o s795.pdf \
  'https://www.obirin.ac.jp/academics/postgraduate/international_studies/course_humanities/u1ta3s000005vara-att/BC-2-1-5-2-4_02.pdf'
# 200 357913 application/pdf
sha256sum s795.pdf  # dae5bef18532545ec43db3088a38620ff7433024d82c973ed61bca2f9c96adae
# == .qcache/7a469fff89b3d7825253e10e.pdf (byte-identical)
pdftotext -enc UTF-8 s795.pdf s795.txt   # 52751 B; qcache .txt is 55599 B (second extractor)
```

Register span: `一、生前の名前 （一）幼名 （二）実名 （三）通称 （四）字 （五）別号 （六）法名`

Match behaviour (identical result from both extractors):

| normalisation | match |
|---|---|
| exact | False |
| whitespace-stripped (`\s+`→``) | **False** |
| whitespace + standalone page-number lines stripped | **True** |

Extracted form at byte 364 of `s795.txt`:

```
第二節 日本の個人名の種類
一、生前の名前
（一）幼名
（二）実名
（三）通称
（四）字
（五）別号

1

\x0c（六）法名
二、死後の名前
（一）諡
（二）追号
```

Two precision defects in the table note *"Obirin PDF, chapter II §II names taxonomy; quote
located across the layout break"*:

1. **The enumerated string exists only in the 目次 (table of contents)**, offsets 364–406;
   `（一）幼名` occurs exactly once in the whole document. The chapter-II §II **body**
   (offset 6304) states the taxonomy only in prose:
   `生前の名前には、幼名・実名・通称・字・別号・法名などがあり、死後の名前には、諡・追号などがある。`
   The note therefore credits the quote to a body section that does not carry the quoted form.
2. The layout break is not empty: a **page number `1`** sits between `（五）別号` and
   `（六）法名`. Whitespace normalisation alone still fails; page-number stripping is
   required. The note says only "across the layout break".

Verdict unaffected: the span is genuine document text and the prose body corroborates the
same six-item taxonomy, so PRESENT stands. The original `payload-absent` classification is
explained by (1)+(2), i.e. an extraction artifact, not missing payload.

### S804 — PRESENT (PASS on verdict; punctuation variance is real)

```sh
curl -sSL --max-time 60 -A 'Mozilla/5.0' -o s804.html 'https://kotobank.jp/word/%E8%8B%97%E5%AD%97-392782'
# 200 212464 text/html; charset=UTF-8
sha256sum s804.html  # 7e2687f658b7d9438d260228ae120d30ec140ec06e83a40a020380599d51ebe2
# .qcache/9f755a332db9c6e632490fe2.raw is 212464 B but 6296c465… (dynamic page bytes)
```

| variant | present |
|---|---|
| `日本人が名のる苗字は、決して中国人の考える姓ではない。` (register, `、`) | **False** |
| `日本人が名のる苗字は，決して中国人の考える姓ではない。` (source, `，`) | **True** |

Verified in the live fetch *and* in the qcache capture (same result both), with context:

> …日本には受け入れられなかった。日本人が名のる苗字は，決して中国人の考える姓ではない。それは本質的には〈いえ〉という社会的構成体の名であり，個人は自己の所属する〈いえ〉の名を称する。…

Precision defects in the table note *"Kotobank 苗字 entry quote located (Japanese comma/ellipsis
variation)"*:

1. The register span as written (with `、`) is **not** present in the source; only the `，`
   form is. A literal-string checker (what produced `payload-absent`) must fail, and any
   adoption round that re-checks the register string verbatim will fail again unless the
   register quote is corrected to `，`.
2. The span sits in the `世界大百科事典（旧版）内の苗字の言及【家族法】より` mention block of the
   kotobank page (tertiary encyclopedia, 家族法 article), not in the 苗字 headword definition
   body. The note's "Kotobank 苗字 entry" reads as the headword; the anchor should name the
   mention block. This matters for `teaches` attribution, not for presence.
3. The note's "ellipsis variation" is not exercised by this span — the register quote ends at
   `姓ではない。`; the source ellipsis (`…`) follows the sentence, outside the quote.

### S814 — REFUSED (PASS)

```sh
curl -sSL --max-time 60 -A 'Mozilla/5.0' -o s814.html \
  'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
# 200 143252 text/html
sha256sum s814.html  # f14f7a5c03cb187f50870a8702a88505da0aea58427a829ea197e66909a11d5c
# == .qcache/e4996396c5be34433078d7ea.raw (byte-identical)
```

Article body fully rendered (28,815 chars after tag strip); title
`魏斌:單名與雙名：漢晉南方人名的變遷及其意義-中国社会科学院历史研究所`.

| probe | result |
|---|---|
| `次のように細分してもよい` | absent (0) |
| `中世` | absent (0) |
| `近代` | 2 — both in footnotes (`《近代湖南人中之蠻族血統》`, `[41]近代臺灣泰雅人命名`) |
| `細分` | 1 — `而且仔細分析，可以發現不少人名…` (unrelated) |

So the body is real article content, and the quoted classification passage is not in it.
REFUSED confirmed.

Root cause (new, beyond wave 1): the fragment is a **library-classification note**. The NDL
`「日本十進分類法(NDC)新訂10版」分類基準` PDF
(`https://www.ndl.go.jp/file/data/catstandards/classification_subject/NDC10code202206.pdf`,
200, 1,659,829 B, pdftotext) contains it 4 times, e.g. at 960.2 / 970.2 / 980.2:

> ＊次のように細分してもよい－.24 中世，＜.25／.27 近代＞.25 15―17世紀，.26 18―19世紀，.27 20世紀―

(`次のように細分してもよい` ×4; `中世，＜.25／.27近代＞` ×3 in whitespace-stripped text.)
The register's S814 quote is an NDC10 classification note mispaired with a CSSN article URL.

### S823 — PRESENT (PASS; live fetch is unreliable)

```sh
curl -sSL --max-time 60 -A 'Mozilla/5.0' -o s823.html \
  'https://www.chinafolklore.org/web/index.php?NewsID=10867'
# attempt 1: 400, 3 bytes
# attempt 2 (with browser UA + Accept-Language): 400, 3 bytes
# http:// variant: 301 → https://www.chinafolklore.org:443/web/index.php?NewsID=10867
# attempt 3 (plain, after 5 s): 400, 3 bytes
# attempt 4 (after 3 s): 200, 41259 text/html   ← matches wave-1 evidence exactly
```

The 200 body is **GB18030-encoded, not UTF-8** (UTF-8 decode yields mojibake; gb18030 decode
yields `[谢玉娥]人名·性别·文化 · 中国民俗学网-中国民俗学会 · 主办 ·`). Decoded and
whitespace-stripped, the register span matches exactly:

> …人名，作为人的一种特殊的称谓符号，从广义上讲包括许多种，诸如小名、正名、字、号、笔名、艺名、室名等，狭义则单指人的名。本文为论述的方便不再细分…

Exact span present: **True**; fragment counts 小名×3, 正名×2, 笔名/艺名/室名×1 each.
Independently re-confirmed in the qcache capture
`.qcache/666feaec93c74b86fc21e5ea.raw` (41259 B, exact span True) — the live 200 payload and
the capture differ in bytes (1cc3b498… vs 5a47f625…, same size) but both carry the span.

Two operational notes the table omits:

1. The endpoint **intermittently returns HTTP 400 with a 3-byte body**: 4 https GETs in this
   session gave 400, 400, 400, 200 (plus one `http://` GET that 301s to the same https path,
   which then 400s). The 400 is a WAF/rate-limit shape, not a redirect. A single-shot fetch can
   misclassify this row.
2. The page is GB18030. A UTF-8-only span search returns false absence — a second mechanism
   that can manufacture `payload-absent` for Chinese-locale sources.

## Counting re-derivation

Register slice (read-only source), exact awk from `RevQuarantineCrossCheck.md`:

```sh
awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $3, $4, $5}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
# 21 lines
# class split: 18 `payload-absent` + 3 "the cited source could not be fetched, so no quote was checked"
```

Verdict table tally (`reports/round-71/telemetry/quarantine-verdicts.md`, rows parsed with
`^\|\s*(S\d+)\s*\|\s*(PRESENT|REFUSED|UNVERIFIABLE)\s*\|`):

```text
rows 21
{'PRESENT': 10, 'UNVERIFIABLE': 5, 'REFUSED': 6}  sum 21
```

ID-set equality against the awk output: 21 vs 21, **identical after stripping the trailing
backtick** the register emits on the three unreachable rows (`S807`/`S812`/`S835`). No
duplicate, no missing, no extra id. Tally arithmetic in the table header
("PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5 = 21") and in `reports/round-71/claims.json`
item10 (`21 data rows (18 payload-absent + 3 unreachable)`) both re-derive correctly: **PASS**.

Row-level agreement of the table against wave-1 evidence docs: S795/S804 (Fetch2),
S823 (Fetch3), S779 (Fetch1), S814 (Fetch2) all carry the same label as the table. No
verdict drift between wave-1 evidence and the frozen table.

## Defects (ranked, for the wave-2 reviewer/critic seats)

- **D1 (medium, note fidelity)** — S795 note credits the quoted enumeration to "chapter II §II";
  the enumerated form exists only in the 目次, and the break injects a page number `1` between
  `（五）別号` and `（六）法名`. Whitespace normalisation alone does not recover the span.
- **D2 (medium, adoption-blocking)** — S804's register quote uses `、` where the source and both
  captures use `，`; a literal re-check at adoption will fail again. Quote should be corrected,
  and the anchor should name the 世界大百科事典（旧版）【家族法】 mention block.
- **D3 (low, infra)** — S823 live endpoint returns 400 intermittently and serves GB18030; PRESENT
  needs a retry + correct charset. Same charset hazard applies to every zh-locale row in the slice.
- **D4 (informational, root cause)** — S779 and S814 are URL↔quote mispairings, not payload
  losses: the S779 spans live on the Hubei 文旅厅 ICH page, the S814 fragment lives in the NDL
  NDC10 classification PDF. REFUSED is correct, but the remediation is re-pairing, not
  re-fetching the cited URL.

## Remaining unknowns

- Whether D4's mispairing pattern extends to the other 16 slice rows (out of this ticket;
  RevQuarantine / RevCensus / RevRows own it). My 5 rows show 2 of 2 REFUSED rows are
  mispairs, which is a non-trivial prior for the other four REFUSED rows (S786, S787, S792, S817).
- `https://www.ihchina.cn/project` (the canonical home of the S779 span) returned **504** twice
  during this check, so the S779 corroboration rests on the Hubei 文旅厅 mirror, which carries
  the span verbatim but with `五个批次` where the register has `五批`.
- Wayback was unreachable from this host (`web.archive.org:443` connection refused), so the S823
  archive fallback could not be re-tested; the local `.qcache` capture was used instead and
  agrees with the live 200 payload.
- No verdict here changes the round's standing: item-10 adoption stays CLOSED; nothing adopted,
  appended or renumbered by this seat.
