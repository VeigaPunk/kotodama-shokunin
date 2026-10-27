# ScribeEntryC — round 76, wave 1: candidate c, `era-periodization-models.amend-2026-10-23b`

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base `98c486bdb4650ba5b8e651d332910e8ee60ad121`).
Seat: leaf scribe. No delegation, no background jobs, no `task` spawns, no pacman. **No tool installed or upgraded this seat.**

## Verdict

**ADMIT.** The draft entry is written and staged; it is carried by one opened page (lane id **S894**), and
`check-cited-lines.py` returns 0 findings. Two legs of the staged plan were dropped rather than softened (the Wayback
capture, and the "four period axes" outline), and two factual errors in the staged text were removed rather than
repeated. One earlier lane verdict about the same URL is contradicted by the served bytes and is filed for the round's
collision guard (§F1).

## 1. Behavior — what was opened and what it carries

The one source is the National Archives of Japan's detailed-search page. Fetched by a plain `curl` GET with the
browser-shaped UA, no cookie, no challenge:

```
HTTP/2 200 | content-type: text/html;charset=UTF-8 | content-language: ja | 311308 bytes
date: Tue, 27 Oct 2026 21:35:49 GMT | server: Apache | x-cache: Miss from cloudfront
sha256 204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8
```
— `curl -sS -D headers.txt -o na-search2.html -w 'HTTP %{http_code} bytes %{size_download}' -A '<browser UA>' 'https://www.digital.archives.go.jp/search'`,
and `sha256sum na-search.html na-search2.html`; the two same-day fetches compared `IDENTICAL` — `cmp -s na-search.html na-search2.html && echo IDENTICAL`.

The three era tables are **server-rendered** in the served bytes inside `#gengo-modal` (no script execution, no
cookie, no second request). Extracted with a stdlib-only Python pass over the raw bytes; the extraction and every
span are in the window.

| measurement | value | command |
|---|---|---|
| 和暦元号 rows | 248 | `python3` extraction of `<tr class="gengo-modal__tr">` under `data-gengo-type="wa"` (window.txt) |
| 中国元号 rows | 94 | same, `data-gengo-type="chu"` |
| 朝鮮元号 rows | 8 | same, `data-gengo-type="cho"` |
| 令和 / 大化 boundaries | 2019 / 645 | window.txt rows 000 and 247 |
| 文治 | 1185, index 141, 106 names after it | window.txt row 141 |
| 康徳 / 金収国 boundaries | 1934 / 1115 | window.txt chu rows 000 and 093 |
| 朝鮮乾隆 / 朝鮮永楽 boundaries | 1736 / 1403 | window.txt cho rows 000 and 007 |
| 元至元 duplicate | 1335 (row 37) and 1264 (row 48) | window.txt chu rows 37, 48 |
| 清乾隆 vs 朝鮮乾隆 | both 1736, different tabs | window.txt chu/cho |
| tab labels | `和暦元号` / `中国元号` / `朝鮮元号` | raw offsets 110546 / 110729 / 110912 |
| column headings | `元号名称` / `開始西暦年`, 3 occurrences each | raw offsets 111269 / 111337 |
| form values | `date_e_from_era`, `date_y_from_era` | raw offsets 70602 / 71307 |

Findings the campaign rows did not record and the draft now uses: the picker has **three** tabs, not one — sizes 248 /
94 / 8; the 中国元号 tab is dynasty-grouped (康徳 1, 大同 1, 民国 1, 清 13, 明 20, 元 14, 南宋 23, 金 21 = 94) and stops
at 1115; the 和暦元号 tab carries an out-of-order eight-row block at indices 83–90 (`元中 1384` … `延元 1336`) between
`暦応 1338` and `建武 1334`.

## 2. Deliverables

| path | what |
|---|---|
| `.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md` | the entry draft (lane form: provenance trio, ground/topic/gap-filled/sources/couples/scope, six dated body sections, decision table, checklist, worked example, calibration, limits) |
| `.ufo/waves/round-76/w1/stage/ScribeEntryC/gate-notes.md` | per-source gate: URL, access date, located quote + location, status/bytes/UA, ADMIT/REFUSE, reason and flip |
| `.ufo/waves/round-76/w1/stage/ScribeEntryC/window.txt` | the committed evidence window: receipt, located spans with byte offsets, and all three tables as text (248 + 94 + 8 rows) |
| `.ufo/waves/round-76/w1/stage/ScribeEntryC/na-search.html` | the raw 311,308 bytes the window was extracted from |

Draft size: **2258 words whole file, 1690 words body** — `len(t.split())` and `len(t[t.index('\n## 1.'):].split())`
on the draft. Requirement was ≥478 body words. Sections: §1 form-not-reference-list, §2 three tabs, §3 collisions,
§4 decision table + checklist + worked example, §5 calibration, §6 limits and handoff. Body carries exactly one S-id,
`S894` — `sorted(set(re.findall(r'\bS\d{3,}\b', t)))` → `['S894']`.

## 3. Gates

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-cited-lines.py \
    .ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md
CITED-LINES: 0 finding(s) in 1 file(s)
exit=0
```

- **No table row carries an S-id**, no line carries two ids — `[r for r in lines if r.lstrip().startswith('|') and re.search(r'S\d{3,}', r)]` → `[]`; same for 2+-id lines.
- **Couples exist at base**: `git cat-file -e 98c486b:<path>` returned OK for all five —
  `culture-material/era-periodization-models.md`, `culture-material/calendar-festival-systems.md`,
  `linguistics/naming-systems.md`, `myth-symbol/celestial-symbolism-calendars.md`,
  `synthesis/worldbible-integration-contract.md`.
- **Ground leg**: `git grep -c '元号名称\|開始西暦年\|国立公文書館' 98c486b -- corpus/knowledge` → no output, **exit 1**.
  `git ls-tree -r --name-only 98c486b -- corpus/knowledge | grep -ci 'era-period'` → **1**.
  Knowledge `.md` files at base **252** — `git ls-tree -r --name-only 98c486b -- corpus/knowledge | grep -c '\.md$'`.
  Registry rows **817** — `git show 98c486b:corpus/SOURCES.md | grep -c '^| S[0-9]'`; id **S894** is free —
  `grep -c '| S894 ' corpus/SOURCES.md` → **0**.
- **Every quote in the draft is inside the window**: each of the 20 spans checked with `q in window` → all `IN`
  (`元号名称`, `開始西暦年`, `令和 2019`, `文治 1185`, `大化 645`, `中国元号`, `朝鮮乾隆 1736`, `朝鮮永楽 1403`,
  `元至元 1335`, `元至元 1264`, `清乾隆 1736`, `康徳 1934`, `金収国 1115`, `暦応 1338`, `元中 1384`, `延元 1336`,
  `建武 1334`, `date_e_from_era`, `date_y_from_era`, `年月日(元号)`).
- **Unopened, stated as unopened**: the site's English surface (`/en/search` → HTTP 404, so the `enHideArea` class's
  effect is recorded as unobserved, not asserted); which holdings each list serves (page states none → `(to-verify)`);
  the identification of the eight-row block as the Southern Court's count (not on the page → `(to-verify)`); the
  ordinal of 令和 (the page states none; the draft prints the row count instead).

## 4. Touched surfaces

Wrote only: the four paths in §2 (`drafts/…` and `stage/ScribeEntryC/…`). No lane file edited, no `git` state touched
(read-only `git grep` / `git show` / `cat-file` only), no fleet-root write, no `SOURCES.md` edit, no `CLAIMS-DRAFT.md`
edit, no `reports/round-76/**` write. Scratch was `/fast/scratch/hyaku/kotodama-r76/ScribeEntryC/` and was removed at
exit.

## 5. Out of scope, and what the L1 still needs

- **Registry row**: `corpus/SOURCES.md` is not in this seat's write list, so **no row was appended**. Proposed row text
  (for the seat that owns the registry), one row, `mined`, `opened 2026-10-27`, `used-by` =
  `corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md`:
  > `| S894 | 国立公文書館デジタルアーカイブ「詳細検索」— the 元号選択 tables (和暦元号 / 中国元号 / 朝鮮元号; columns 元号名称, 開始西暦年) — https://www.digital.archives.go.jp/search | dataset | A | the archive's own era-name picker as a search instrument | #gengo-modal tables — page as served 2026-10-27 (HTTP/2 200, 311,308 B, sha256 204b7188…) | an era table offered as a search key (name + year, 248/94/8 rows, two collision rules) rather than as a taxonomy; tier A only for what this archive's form offers | mined | 2026-10-27 | 180d — curl -fsSL '<url>' \| grep -c '開始西暦年' -> 3 | corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md |`
- The evidence files are under `w1/stage/ScribeEntryC/`; the claims want quotes inside a **committed** window, so
  `window.txt` (and optionally `na-search.html`) should be copied to `reports/round-76/evidence/` at the freeze.
- `corpus/lessons/round-76.md` `## Collision guard` should carry §F1 and §F2; `## Gate` should carry the S894 admit.

## 6. Findings

**F1 — the claim's declared before-state leg is false as printed.** CLAIMS-DRAFT says *"`git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` … print nothing (exit 1)"*.
> `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` → `98c486b:corpus/lessons/round-68.md`, **exit 0**.
The host is already in the corpus, in a lesson line. The true negative is the narrower one the draft's ground line uses:
`git grep -c '元号名称\|開始西暦年\|国立公文書館' 98c486b -- corpus/knowledge` → exit 1. **The claim must either narrow
that leg to `corpus/knowledge` or restate it; as printed it fails before any data.**

**F2 — round 68's refusal of this URL does not hold for this scope, and the campaign's own rows contradict each other.**
`corpus/lessons/round-68.md:112` records *"S825 (digital.archives.go.jp/search is a portal landing, not the table page)"*,
and campaign S935 (`SOURCES.append.md`) states *"the live search page no longer serves this text; the archived capture
does"*. Both are contradicted by the 2026-10-27 bytes: the page is 詳細検索 and serves three era tables. Campaign S908's
own recheck in the same file already reported `grep -c '元号名称'` → 3 live. Likely cause is **check shape**: the
campaign's quote is a concatenation (`元号名称 開始西暦年 令和 2019 …`) and the tokens are separated by `<th>` markup in
raw bytes, so a raw-span test fails where a tag-stripped test passes. The entry therefore locates each token separately
and names the surface. Recorded for `## Collision guard`; the draft's §6 states it in one sentence.

**F3 — the staged text's couplings were wrong twice.** (a) `culture-material/era-periodization-models.amend-2026-10-23.md`
**does not exist** — `git ls-tree -r --name-only 98c486b | grep -i era-period` returns only
`corpus/knowledge/culture-material/era-periodization-models.md` and a round-74 assimilation copy; the draft couples to the
five paths verified with `git cat-file -e`. (b) The staged "round 4's library-classification amendment (S757)" is
misattributed — the lane's **S757 is Huizinga, *Homo Ludens*** (`corpus/SOURCES.md:713`); the draft repeats neither the
path nor the attribution.

**F4 — the "four period axes" outline is not writable from this source.** Only the archival axis is carried. Library
classification, museum exhibition periods and the heritage filing ladder are unopened this round; `grep -rniE
'日本十進|NDC|NDL|国立国会図書館|library classification' corpus/knowledge --include=*.md` returned no
classification-ladder material (its hits are substring noise: `Sandler`, `Benrath`, `Lipták`). The draft writes one
instrument and says so in §6 rather than staging four axes with three unsourced.

**F5 — Wayback was unreachable from this host (unrun, not absent).** Three attempts: CDX API → `curl: (7) Failed to
connect to web.archive.org:443`, 0 bytes; `/web/2024/<url>` → HTTP 302, 0 bytes; same with `-L` → curl (7), 0 bytes.
The planned S935 capture leg is dropped, not softened; the entry rests on the live response and says so.

**F6 — the served page hides its era row behind a class named `enHideArea`.** `t.count('enHideArea')` → **10** in the
served bytes, two of them wrapping the `年月日` and `年月日(元号)` rows. The English surface was not opened
(`https://www.digital.archives.go.jp/en/search` → HTTP 404), so the draft records the class and asserts nothing about its
effect. A later round can open the English surface and settle it.

## 7. Self-check during the pass

Three sentences were corrected against the bytes before this report: "two-column table" → the rows carry a third
`選択` cell; "row order is by start year within each tab" → false for both tabs (和暦 has the eight-row block, 中国 is
dynasty-grouped); "three attempts, connection failures, no bytes" → two connection failures plus one HTTP 302 with no
body. Each correction is visible in the staged bytes and in the window.
