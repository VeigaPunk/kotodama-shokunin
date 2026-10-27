# ScoutCoverageSweep — claim C coverage map and negative sweeps (round 76, wave 1)

Base `B=98c486bdb4650ba5b8e651d332910e8ee60ad121`; lane `L=/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Lane HEAD at read time: `git -C $L rev-parse HEAD` -> `98c486bdb4650ba5b8e651d332910e8ee60ad121` (untracked: `.ufo/waves/round-76/`, `reports/round-76/` only). Nothing in the lane or fleet was written except this file; the scratch dir was deleted.

## 1. Negative sweeps at base, `corpus` tree (git grep -l, tracked bytes at B)

| # | pattern | exit | output (verbatim) |
|---|---|---|---|
| 1 | `GB/T 33661\|33661-2017\|农历的编算` | 0 | `B:corpus/lessons/round-68.md` and `B:corpus/lessons/round-69.md` |
| 2 | `digital\.archives\.go\.jp\|元号名称` | 0 | `B:corpus/lessons/round-68.md` |
| 3 | `openstd\.samr\|国家标准全文公开` (-i) | 0 | `B:corpus/lessons/round-68.md` |
| 4 | `gmw\.cn` | 1 | (nothing) |

IMPORTANT: sweeps 1-3 exit 0, not 1 — the draft's "Before" line (`git grep -l -E 'GB/T 33661' 98c486b -- corpus` and `digital\.archives\.go\.jp` "each print nothing (exit 1)") is FALSE as a whole-`corpus` sweep. Every hit is a round lesson, none in `corpus/knowledge/**` and none in `corpus/SOURCES.md`. Located with `git grep -n` (same patterns):

- `corpus/lessons/round-68.md:111` — quarantine verdict "present … S776 (openstd.samr.gov.cn GB/T 33661-2017 page, HTTP 200)" — a CAMPAIGN-namespace id; the lane's own S776 is Pearson, Mancala (`SOURCES.md:732`).
- `corpus/lessons/round-68.md:112` — "refused … S825 (digital.archives.go.jp/search is a portal landing, not the table page)" — campaign S825; lane S825 is Gregis, Asclepius (`SOURCES.md:779`).
- `corpus/lessons/round-69.md:39,111` — R69-M13 and quarantine addendum: staged id S859 = "the package's GB/T 33661-2017 row" collided with lane S859.

Consequence for the frozen claim: the Before sweep MUST be scoped to what the claim means — `git grep -l ... B -- corpus/knowledge corpus/SOURCES.md` — or it exits 0 at base and the "does not hold" premise reads as refuted. Run for that scope (same four patterns, `-- corpus/knowledge`): see the table below.

Scoped sweeps (re-run, B, `-- corpus/knowledge corpus/SOURCES.md`, exit and output):
(Commands were run per pattern over `corpus/SOURCES.md` via `git show B:corpus/SOURCES.md | grep -n -iE <pattern>`: all four exit 1, no output. `corpus/knowledge` was covered by the whole-`corpus` runs above, whose only hits are under `corpus/lessons/`, so `corpus/knowledge` has 0 hits for all four.)

SOURCES.md rows: all four patterns -> `grep` exit 1, nothing. Registry row count `git show B:corpus/SOURCES.md | grep -c -E '^\| S[0-9]+ '` -> `817` (matches the draft's 817). Last row S893 (chinawriter.com.cn).

Synonym sweep (a hit could hide behind): `git grep -n -iE 'xingzuobaike|archives\.go\.jp|National Archives of Japan|国立公文書館' B -- corpus` -> only the `round-68.md:112` line above. Entry-level sweep in the two held entries (`git show B:corpus/knowledge/culture-material/{calendar-festival-systems,era-periodization-models}.md | grep -n -i -E '农历|GB/T|国家标准|紫金山|dingshuo|定朔|公文書|archives|国立|National Archives'`): zero hits for GB/T, 国家标准, 紫金山, 定朔, 公文書, archives; the only 农历/lunisolar words are generic (below). `wareki|和暦` hits only `era-periodization-models.md:58` (JIS X 0301). `Calendrical Calculations` is cited in `calendar-festival-systems.md` lines 5 and 20 (a method book, not a standard's clause).

## 2. README coverage map and what a claim-C landing touches

`corpus/README.md` is 831 lines at B. It has NO heading literally `## Frontier`: the frontier section is `## Known gaps (frontier)` at line 608 (`grep -n -E '^## Frontier|^#+ .*[Ff]rontier'` printed only that). `Counts checked` occurs 5 times (`grep -c`): lines 239 (prose inside a revision note), 756, 799, 820, 831. First real footer: line 756 (`Counts checked 2026-10-25 …` total 243); last footer: line 831 `Counts checked 2026-10-27 from the repo root: \`find corpus/knowledge -type f -name '*.md' | wc -l\` (total 252 files; directory totals 32/32/40/29/24/95).` preceded by line 829 `Total knowledge entries: 252.`

`## culture-material/ (40)` at line 410: the heading (40) = section rows 40 (`sed -n 410,451p | grep -c '^- \`'` -> 40) = files 40 (`git ls-tree --name-only B corpus/knowledge/culture-material/ | wc -l` -> 40) = footer vector third slot 40. Total files `git ls-tree -r --name-only B corpus/knowledge | wc -l` -> 252. The round-75 Ca landing (012e8d3) moved the heading 36 -> 40 and indexed the two heritage files; the round-75 C landing (4f5e3b2) appended three myth-symbol rows, the heading 29 -> 32 edit was Ca's, and appended lines 829-831 (`Total knowledge entries: 252.` + the footer). That diff is the template (`git show 4f5e3b2 -- corpus/README.md`).

A claim-C landing of n admitted files from {a,b,c,d} appends/changes, under the r75 counter's INDEX rules (`reports/round-75/accept-c.py` H4 doc, lines 64-71, 96-100):

APPENDED (graded):
1. n index rows in the `## culture-material/` section, shape ``- `name.md` — <entry's own `- topic:` text verbatim>`` (multi-line staged `- topic:` blocks, e.g. a at staged lines 13-14, must be joined as one row line). ASCII filename order (computed: `sorted()` of the six names -> `calendar-festival-systems.amend-2026-10-23c.md`, `calendar-festival-systems.amend-2026-10-24-r10.md`, `calendar-festival-systems.amend-2026-10-24.md`, `calendar-festival-systems.md`, `era-periodization-models.amend-2026-10-23b.md`, `era-periodization-models.md`): so rows go immediately BEFORE the existing `calendar-festival-systems.md` row (README line ~418) and before `era-periodization-models.md` (~422). Note `-r10` sorts before `.md`/`.` (0x2D < 0x2E): d, b, a, then base.
2. A new `Total knowledge entries: <252+n>.` line and a new last `Counts checked 2026-10-27 …` footer with `(total <252+n> files; directory totals 32/32/<40+n>/29/24/95)`, appended after line 831. Older footers (756, 799, 820, 831) stay byte-identical (the 831 footer becomes an older footer once the new one is appended).
3. No row-shaped README line may carry an S-id (README never asserts registry rows).

IN-PLACE (needs an owner): the heading parenthetical `## culture-material/ (40)` -> `(40+n)`. In r75 this was exempted because Ca owned it; in r76 Ca's pairs (F1-F13 etc.) do not name it, so the frozen claim text must either say claim C owns this heading edit (`owned_inplace` in the counter config, as r75's D6) or the landing leaves it stale and names it (the r74 precedent, `README.md:810-812`). Either way, it must be said in the freeze, or the counter's "any other changed README line fails" rule fires.

EXEMPT/UNTOUCHED: the revision header block (lines 3-~335: `revision: 2.21` top block; r72-r75 landings did NOT add a revision block — r73/r74/r75 used appended sections or footers instead), the other five partition headings and rows, the `## Known gaps (frontier)` bullets (a bullet like r74's at line 738 is optional, not graded by the r75 counter), every older footer. The r75 H4 rule bars changing/removing any README line outside "the base's last footer block" except the exempt heading lines.

Footer caveat: `reports/round-28/readme/sweep.py` still parses the FIRST footer (README:821-826 says so), so its totals legs stay red regardless.

## 3. Expansion-credit argument (what is new vs held)

Held, with lines (B):
- `calendar-festival-systems.md` (175 lines): lunisolar as a class (line 31); the Chinese leap month = the month lacking a major solar term (line 43); the 24 solar terms / jieqi as a "solar spine" (46, 136); Meiji 6 Gregorian adoption (69); nengō as a statute-of-the-count (119, 142, 168). Sources line 5 cites Reingold & Dershowitz 4th ed. (method book). No standard's clause text, no 农历 compilation rule, no GB/T, no registry/publication mechanics.
- `era-periodization-models.md` (143 lines): nianhao / nengō family and selection rules (45-52), the Gengō-hō 1979 and the 2019 criteria ("248th era", lines 6, 31, 50), the seam logistics incl. JIS X 0301 wareki (58), zhengshuo as loyalty (61-63), lexicon (105). It cites no archival era table, no archive.
- Registry: S919 (Marrone) is lane S892 and S921 (Barthes, Persée) is lane S885 — already held (`SOURCES.md` r75 rows).

New ground claim C can honestly credit (each needs its located quote, per the staged amendments):
- Standards-level: GB/T 33661-2017 *农历的编算和颁行* — the 编排规则 clause (4) and rules (1)-(5) text, calculation model, the 颁行 publication requirements (c: S916, tier C reproduction — cannot be sole support), the promulgation-day account of the technical content (a: S937 gmw.cn), registry ownership fields (a: S932, b: S938), and the access-mechanics point that the authoritative copy is not downloadable as text (b). The held entries hold the astronomy-in-general of intercalation but never the codified compilation rule.
- Archival era-name table: 元号名称／開始西暦年 as an institution's search vocabulary (c: S908; a: S935). The held era entry holds era rules and selection criteria, not an archival table.

Where the credit is thin or contested (state honestly):
- Entry a (staged `calendar-festival-systems.amend-2026-10-24.md`, 98 lines) concatenates TWO documents: the main amendment (lines 1-51, S937/S935/S932) and a "Superseded passage" at lines 52-98 about S919/S921 (Marrone, Barthes) — an off-theme "contrast case" built on rows the lane already holds (S892, S885). That block adds 0 coverage and the draft lists S919/S921 as a cite of a; the landing must not count it and the 'k' row count must not add rows for it.
- Entry c overlaps held `era-periodization-models.md`: it is a single-row tier-A amend (S908) covering the era table as a search instrument, and the held entry already carries the era-name lexicon; its new ground is the table's span and the institution's own use, not era theory. Entry c cites S908 live form only; S935 is the same page (draft merges to one row S894, correct).
- Entry d is tier-C-only (S916 xingzuobaike reproduction) — the draft's own rule "no tier-C row is the sole support of an admitted entry" EXCLUDES d unless a second, tier-A/B row supports it. Since d is the clause-text entry, the standard's clause text has no tier-A/B support in the draft: S937 (gmw) is the state press's report of the technical content, not the clause; S932/S938 are registry metadata fields. [INFERENCE] d likely fails admission, leaving a, b, c: n >= 2 still reachable only if a admits.
- Entry b (S938, openstd showGb 标准信息表) is registry metadata plus an access-mechanics note: thin for "standards-level coverage"; real but narrow.

Probes run (plain requests; browser UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; each line is one `curl -L -A <UA>` request; counts are `grep -c` lines in the body; body not retained, scratch deleted):
- `https://www.digital.archives.go.jp/search` -> `200 311308`; `元号名称` lines=3 (the string IS in the served bytes; contrast `round-68.md:112` refusing campaign S825 on the same host as a "portal landing" for a different quote — the campaign S908 anchor must be re-located in a committed window, not trusted).
- `https://news.gmw.cn/2017-05/23/content_24559485.htm` -> `200`, served gzip (`Content-Encoding: gzip`, 8076 wire bytes, 25250 decoded; a first run without `--compressed` mis-read it as having no 农历 and is void). Decoded (`--compressed`, utf-8): 农历 29, 国家标准 8, 编算 12, 节气 3, 公历 2, 33661 0, `2017-05-23` 3. The report names the standard by title, not number: a Gate quote about "GB/T 33661" cannot be quoted from this page; the quote must be a span about the standard's content. Evidence tool must send `Accept-Encoding` handling (a gzip body not decoded = a spurious "quote absent").
- `https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296` -> `200 24144`, effective URL redirected to `…/newGbInfo?hcno=…&refer=outter`; `农历的编算` 1, `33661` 2, `国家标准全文公开` 0. So S896 (newGbInfo) and S897 (showGb) are the same served document after the redirect (draft's "two URLs one document" caveat applies: draft keeps both rows; the lane's one-row-per-document rule suggests merging S896+S897 unless the Wayback capture of newGbInfo differs from the live showGb).
- `https://www.xingzuobaike.com/huangli/wannianli/d165803.html` -> `200 33179`; `农历的编算` 4, `33661` 3, `编排规则` 1.
- `https://web.archive.org/web/20260422145052id_/…` and `…/20260424031027id_/…` -> `curl: (7) Failed to connect to web.archive.org:443` both times from this host. UNRUN: whether the Wayback captures (S935, S932) are reachable; the live forms above answer, so S894/S896 can be satisfied by the live pages if the Wayback host stays unreachable. No access-control challenge was met on any request.

Installs: none.

Unrun / unresolved: whether 编排规则 clause (4) quote windows exist in the evidence tool's window rules (S916 live page has 编排规则 once — not checked for the 4096-char window shape); Wayback reachability; the `reports/round-76` counter (not built here).

Report: .ufo/waves/round-76/w1/ScoutCoverageSweep.md
