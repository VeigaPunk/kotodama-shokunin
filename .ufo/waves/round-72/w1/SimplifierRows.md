# SimplifierRows — minimal registry row count for the round-72 heritage-taxonomy adoption

Seat: L1Kotodama72.SimplifierRows (wave 1, round 72, hyaku run 6)
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
Read-only seat: no corpus, entry, lesson, or counter bytes were mutated. Every check below ran
in `/tmp/simplifierrows/` against a scratch clone; the two commits named "landed" were made by
other seats before this report was written.

---

## Verdict

**Option (b) — two rows (S874, S875) — is the minimal and honest count, and it is what the lane
landed.** Options (a) three rows and (c) four rows are not merely inferior; they are *uncitable in
the shape they require* and *excluded by the frozen claim*. One in-round correction to the landed
S875 anchor cell is recommended (below, cut **B**); one in-round correction to the landed amendment
body is recommended (below, cut **A**). Both are single-cell edits that leave every counter leg
green.

---

## 1. The lane's landed state (as measured, not as briefed)

The brief assumed the row count was still open. It is not:

| commit | what it did |
|---|---|
| `770100f` | "round-72 C: heritage-taxonomy assimilation — two entries admitted, registry S874/S875 appended (797->799), lesson round-72" |
| `868107e` | "move S874/S875 rows into the Registry table (E12 fix — they were appended after Leads)" |
| `ba8ad3a` | "canonical entry review cuts C1-C4 (tier triad, PRC-only stability claim, 扩展项目 graph, era-ladder completeness) + per-row recheck cadence (RevEntryQuality)" |

The counter as it now stands:

```
$ python3 -B reports/round-72/accept-c.py --root . --lands 21ad3088cb64f7275e5541804e168f15d21d26d0
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / REJECTS / GROUND / CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK
ACCEPT-C-72: PASS legs=10/10
```

Registry is 799 rows; `corpus/SOURCES.md:829-830` hold S874 and S875 inside the `## Registry`
section (Registry spans lines 26–831). Census on the real tree exits 0 with no S874/S875 finding.

So this report is the argued verdict on (b) plus the two cuts the landed text still needs — not a
proposal to re-open the row count.

---

## 2. Why (a) three rows and (c) four rows fail

### 2.1 The frozen claim excludes them mechanically

`reports/round-72/claims.json` (frozen at `a7ab3bd`, `"frozen": "2026-10-25"`, pre-data
corrections F1–F9 + SCOUT-LIVE already applied) states leg ROWS:

> exactly two new registry rows S874 and S875 exist at `<lands>`, both status mined, both used-by
> the two admitted entries, **no other registry row added or removed**

and `reports/round-72/accept-c.py` hard-codes `NEW_IDS = ("S874", "S875")` with
`if added != set(NEW_IDS): bad.append("added=%s (want S874/S875)")`. I simulated both alternative
trees against the counter's own parsing code:

| tree | counter ROWS leg |
|---|---|
| (b) 2 rows (landed) | `added=[]` → PASS |
| (a) 3 rows (+ S876) | `added=['S876']` → **FAIL** ("want S874/S875") |
| (c) 4 rows (+ S876,S877) | `added=['S876','S877']` → **FAIL** |

A claim leg cannot be widened after the freeze; the alternatives are off the board as data.

### 2.2 Criterion 18 makes a capture a *carrier*, not a source — so the split duplicates one page

Criterion 18 (`corpus/QUALITY.md:57`) is the structural reason, and it is decisive:

> A registry row's source cell names **one live URL plus a wayback capture of that same page**;
> the capture's embedded original must normalize (query-aware) to the live URL, and the row's
> anchor quote must be findable in at least one named anchor's body text. **A capture of a
> different page than the live URL is not evidence for the row's own anchor — it is a second page,
> cited only if the row says so.**

A capture is the row's durability carrier. Splitting one page's dated captures into their own rows
manufactures two authorities over one document — the exact thing a curated registry exists to
prevent. The staged artifact says so in its own words: staged S967's source cell reads *"the
Internet Archive's capture of 2020-02-16, with the live page shown — … (live original:
https://www.ihchina.cn/project.html)"*. Staged S967 is not a second document; it declares itself a
dated state of staged S863's page.

I verified the identity from the archive's own record rather than from the staged prose:

- Wayback CDX for the 2020 capture: `urlkey cn,ihchina)/project.html`, `original
  http://www.ihchina.cn:80/project.html`, status 200 — the same urlkey the live URL normalizes to.
- The 2020 replay is **byte-identical** under both embedded-original spellings:
  `sha256 d3274d85ea5433f0ff7871d8668db3f2bdd87e0995ae933f14ea73a57268c1b4` for
  `…/20200216023423id_/http://www.ihchina.cn/project.html`,
  `…/20200216023423id_/https://www.ihchina.cn/project.html`, and the lane's own
  `/tmp/ihchina-2020.html`.
- The register's **content** is identical across all three carriers. The taxonomy sentence and the
  code-rule sentence are byte-identical in the 2020 capture, the 2026 capture and the live page:

  | carrier | `国家级名录将非物质文化遗产分为十大门类` | `编号中的罗马数字代表所属门类` | `公布了四批` | `公布了五批` |
  |---|---|---|---|---|
  | 2020 capture | identical | identical | 1 | 0 |
  | 2026 capture | identical | identical | 0 | 1 |
  | live 2026-10-25 | identical | identical | 0 | 1 |

The *only* difference between the two dated states is the batch-count sentence. That is a claim
about **one page over time** — the amendment's actual thesis — and it is not a claim about two
documents.

### 2.3 The census sees the duplicate

A separate 2020-capture row that names the live URL first (the only shape in which it is a
same-page row under criterion 18) trips the census:

```
$ scripts/sources-census.sh validate --file <mirror>/corpus/SOURCES.md --today 2026-10-25
file  W04  S876 duplicate url www.ihchina.cn/project.html across scopes
```

The archive-first spelling (the staged S967 shape) is census-quiet but is the worse outcome: that
row's *live* URL is then an archive URL and its live original survives only in prose, so the row
claims a page it does not open — criterion 18's "second page" hazard, and the shape 55 legacy rows
have only because their live pages were unreachable (S142, S182, S217, S239, S240, S274 …).

### 2.4 The split makes the amendment's central claim uncitable

This is the sharpest argument, and it is about honesty rather than bookkeeping. Under (a) or (c),
the amendment's comparative claim — "the categories are stable, the batch count moves" — spans two
rows, so one sentence must carry two ids. The lane's own clause-scoping lint forbids that:

```
$ tools/check-cited-lines.py <(a): one comparative line citing S874+S876>
MULTI-ID opta2/a.md:4 S874,S876        → CITEDLINES: 1 finding(s), exit 1
$ tools/check-cited-lines.py <(c): one comparative line citing S876+S877>
MULTI-ID optc/c.md:4 S876,S877          → CITEDLINES: 1 finding(s), exit 1
```

The counter's CITEDLINES leg requires `"0 finding(s)"` in that tool's output, so both alternatives
fail a frozen leg on their citation shape alone. Under (b) both carriers live in one row, the
comparison is one claim about one row, and it needs exactly one id — which is what landed.

---

## 3. The citability question the brief asks

> *if the 2026 capture is only a carrier inside S874's row, can the amendment cite "the register's
> 2026 state" precisely (anchor cell naming both captures)?*

**Yes — the mechanism is sound, and it is what landed.** S874's anchor cell names both carriers
*and* the state each carries:

> … — as served live 2026-10-25 (HTTP 200 after one initial timeout) and as captured 2020-02-16
> (四批) and 2026-10-20 (五批)

So "the register's 2026 state" resolves to one carrier and one span: S874 → capture
`https://web.archive.org/web/20261020183948id_/https://www.ihchina.cn/project.html` →
`国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录`. I re-fetched that capture
independently: HTTP 200, 10 370 bytes, `公布了五批` = 1, `公布了四批` = 0.

**But the landed amendment does not actually make that citation.** Two of its body lines carry no id
at all:

```
16: From the 2020-02-16 capture of S874: the register reads 国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录.
17: From the 2026-10-20 capture of the same page: 国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录.
18: Between the two readings the taxonomy itself did not move: … word-for-word the same in the 2020 capture and in the 2026 capture.
```

Line 16 is scoped to S874; lines 17 and 18 are scoped to nothing. The 2026-state claim — the exact
claim under review — is therefore unattributed in the entry body. This is the round-71 F2 shape
verbatim ("S873 appeared 0 times outside the header"), and it is **invisible to the gate**:
`tools/check-cited-lines.py` only flags MULTI-ID and TABLE-ID, so it reports 0 findings on the
landed amendment.

---

## 4. Cuts — exact texts

### CUT A (required) — scope the amendment's dated-state claims to S874

`corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`, lines 17–18.
Replace:

```
17: From the 2026-10-20 capture of the same page: 国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录.
18: Between the two readings the taxonomy itself did not move: 国家级名录将非物质文化遗产分为十大门类 and the code rule 编号中的罗马数字代表所属门类 are word-for-word the same in the 2020 capture and in the 2026 capture.
```

with:

```
17: From the 2026-10-20 capture of the same page (S874): 国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录.
18: Between the two readings the taxonomy itself did not move (S874): 国家级名录将非物质文化遗产分为十大门类 and the code rule 编号中的罗马数字代表所属门类 are word-for-word the same in the 2020 capture and in the 2026 capture.
```

**Verified counter-neutral.** In a scratch clone of the lane I committed the fix and ran the real
counter against it: `ACCEPT-C-72: PASS legs=10/10`, including CITEDLINES. The control (same clone,
fix reverted) also passes 10/10 — so the fix changes no leg verdict and repairs a defect the gate
cannot see. `tools/check-cited-lines.py` on the fixed file: 0 findings, exit 0 (one id per line,
no MULTI-ID).

Why the id must land on line 17 and not only line 16: line 17 asserts the 2026 state and line 18
asserts the cross-capture identity. Neither is a continuation of line 16's clause; they are
separate claims about separate carriers, and each must name the row that carries them.

### CUT B (required) — S875's anchor cell names two era-branch terminals that are not terminal

`corpus/SOURCES.md:830`, S875 anchor cell. The served `時代` select has three branches; I extracted
every option from the live page (231 736 B, HTTP 200):

| branch | options | first | **last** | branch terminal? |
|---|---|---|---|---|
| `[日本]` | 18 | 旧石器 | 令和 | yes — `旧石器…令和` is correct |
| `[中国]` | 21 | 旧石器 | **近現代** | no — `清` sits at index 19 of 21 |
| `[朝鮮半島]` | 10 | 旧石器 | **近現代** | no — `李氏朝鮮` sits at index 8 of 10 |

The landed cell ends those two ranges on `清` and `李氏朝鮮`, so a reader of the row takes them as
the branch ends. Replace:

```
検索フォーム「時代」選択肢（旧石器…令和 [日本]; 旧石器…清 [中国]; 旧石器…李氏朝鮮 [朝鮮半島]) + 「分野」選択肢（16 top-level: …） + 検索条件「指定区分」 + 記録行「材質・構造・技法」「サイズ」「所在地」 — page as served 2026-10-25
```

with:

```
検索フォーム「時代」選択肢（旧石器…令和 [日本]; 旧石器…近現代 [中国]; 旧石器…近現代 [朝鮮半島]) + 「分野」選択肢（16 top-level: …） + 検索条件「指定区分」 + 記録行「材質・構造・技法」「サイズ」「所在地」 — page as served 2026-10-25
```

Only the two bracketed terminals change; the rest of the cell is byte-identical.

**This is the row-side half of a cut the lane already routed and did not land.** RevEntryQuality's
report lists cut **C4** — *"the [日本] ladder omits the served option 昭和以降 (value 15, sitting
between 大正 and 昭和); and '[中国] (旧石器 … 清)' reads 清 as terminal while the branch continues
to 近現代 (value 36). Insert 昭和以降; restate the 中国 branch as non-terminal."* — and commit
`ba8ad3a` is titled "cuts C1–C4", but its diff contains no `§4` hunk, and **no committed version
of the entry contains `昭和以降` or `近現代`** (checked across every commit touching the file).
C1, C2 and C3 landed; C4 did not. The same non-terminal reading sits in the canonical entry's §4
and in S875's anchor cell.

Route: `ba8ad3a` is already committed, and the lane edits just-landed corpus bytes in place
within the same round before it closes (precedent: `64da9e1` "round-71: S861 anchor ¶2 fix", and
`868107e` moving S874/S875 into the Registry table this round). So the fix is an in-round append to
the round-72 lesson naming the superseded text, not a new row — CORPUS rule 2's "a correction is a
new row whose `teaches` opens `supersedes S0NN —`" applies to *closed* rounds, not to a row still
open in the round that landed it.

### CUT C (recommended, same cell as B) — the canonical entry's §4 ladder list

`corpus/knowledge/culture-material/heritage-taxonomy-models.md` §4. The served `[日本]` branch has
18 options; the entry enumerates 17, omitting `昭和以降` (index 14, between `大正` and `昭和`).
Restate as a range, which is both complete and shorter:

```
whose [日本] branch runs 旧石器 … 令和 (18 options, 昭和以降 included between 大正 and 昭和) …
```

and restate the `[中国]` branch as non-terminal: `[中国] (旧石器 … 近現代)`.

### CUT D (not recommended — for the record)

The amendment's `source:` line names only the live URL, describing the captures in prose
("as captured by the Internet Archive 2020-02-16 (四批) and 2026-10-20 (五批)"). A reader wanting the
2026 capture must go to the row to find its URL. Naming all three URLs on that line is **also
counter-legal** — I verified the counter's REPOINTED leg accepts it, since all three keys are
registered on S874:

```
cited urls: 3 | any unregistered: none -> OK   (ids on line: ['S874'] — exactly one, as required)
```

I do **not** recommend it: it adds URL weight to the entry header for no loss of resolution, and
the round-71 house shape is one URL per `source:` line with the carriers held in the row. Flagged
as available, declined.

---

## 5. Rows and rows to keep, verbatim

**KEEP S874 as landed** (`corpus/SOURCES.md:829`), including its two carriers:

```
| S874 | 中国非物质文化遗产网 · 中国非物质文化遗产数字博物馆（文化和旅游部主管）,「国家级非物质文化遗产代表性项目名录」清单页 — https://www.ihchina.cn/project.html ; https://web.archive.org/web/20200216023423id_/http://www.ihchina.cn/project.html ; https://web.archive.org/web/20261020183948id_/https://www.ihchina.cn/project.html . | dataset | A | Tier A for the PRC state's ten-category taxonomy of intangible cultural heritage and its project-numbering scheme (十大门类; 罗马数字门类码, e.g. 侗族大歌 = Ⅱ-28; 扩展项目名录). Not tier A for live record counters (unstable, not used as anchors) | 清单页「国务院先后于2006年…公布了…批国家级项目名录」段 + 「国家级名录将非物质文化遗产分为十大门类」段 + 编号中的罗马数字代表所属门类 — as served live 2026-10-25 (HTTP 200 after one initial timeout) and as captured 2020-02-16 (四批) and 2026-10-20 (五批) | A state-grade material-culture category model with one stable code per project, usable directly as a craft and ritual taxonomy for an invented culture | mined | 2026-10-25 | 180d | corpus/knowledge/culture-material/heritage-taxonomy-models.md, corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md |
```

**KEEP S875 as landed** (`corpus/SOURCES.md:830`), with CUT B applied to its anchor cell only:

```
| S875 | 文化遺産データベース（文化庁, Agency for Cultural Affairs）, 文化財検索 — https://online.bunka.go.jp/db/heritages/search | dataset | A | Tier A for the Japanese state's official cultural-property classification: the 分野 domain tree and the 時代 period ladder used to date and file objects | 検索フォーム「時代」選択肢（旧石器…令和 [日本]; 旧石器…近現代 [中国]; 旧石器…近現代 [朝鮮半島]) + 「分野」選択肢（16 top-level: 建造物, 伝統的建造物群, 絵画, 版画, 彫刻, 工芸, 考古, 歴史, その他の美術, 民俗, 伝統芸能, 工芸技術, 文化財保存技術, 史跡, 名勝, 天然記念物) + 検索条件「指定区分」 + 記録行「材質・構造・技法」「サイズ」「所在地」 — page as served 2026-10-25 | An official period vocabulary and material-domain taxonomy a state uses to date and file its own objects — a ready-made emic ladder for an invented culture's museum-era coupling | mined | 2026-10-25 | 90d | corpus/knowledge/culture-material/heritage-taxonomy-models.md |
```

**CUT ENTIRELY:** the option-(a) S876 row and the option-(c) S876 + S877 rows. Neither is written.
If either were written it would (i) fail the frozen ROWS leg, (ii) duplicate the live URL across
scopes in the census, and (iii) make the amendment's comparative claim uncitable under the lane's
own cited-lines lint.

---

## 6. Preserved contract — what the 2-row design keeps

- **Criterion 18 (same-page capture).** S874's source cell names one live URL plus two captures of
  *that same page*; the capture embedded originals normalize to the live URL, and the row's anchor
  quote is present in every named carrier's body text. I checked the scheme-preserving reading
  too: `check-row-fragments.py`'s `norm_url` is scheme-preserving, and round-65's
  `CAPTURE_RE` is end-anchored, so it reads the *last* carrier (2026, `https://` embedded) — the
  strict same-page test **passes** (`True`). S874 therefore clears both the round-72 counter's
  scheme-blind normalizer and the historical scheme-preserving one. Note the ordering dependency
  (see finding F2 below).
- **Criterion 10 (ordinary access).** No bypass marker anywhere: `tools/check-source-access.py`
  reports `ACCESS: 3 flagged rows, 0 findings` on the tree.
- **CORPUS rule 1 (a row is a claim).** Both rows were opened in the round that wrote them, both
  `mined`, both tier A with an honest scope note (`Not tier A for live record counters (unstable,
  not used as anchors)`) — and I confirmed the unstable counters (1372/1557/3145/3610/308473) are
  cited nowhere in either entry.
- **CORPUS rule 2 (append-only).** Unbroken: 797 → 799 rows, two additions, no removals, no
  in-place edit of a closed round's row.
- **used-by honesty.** S874 names both entries; S875 names only the canonical entry — correct,
  because the amendment cites S875 zero times (grep: 0) and the canonical entry cites it five
  times. The counter's ROWS leg checks the *union* of both rows' used-by against the two admitted
  entries, which holds.
- **Claim C's REPOINTED leg.** Every `source:` citation names id ≥ S874 whose row URL matches.
  All three of S874's URLs are registered on S874, so the amendment and the canonical entry both
  re-point by document; no arithmetic id shift was used.

---

## 7. Findings routed to the L1 (not my lane to fix)

**F1 — C4 was routed and not landed.** `ba8ad3a` is titled "cuts C1–C4" but its diff has no `§4`
hunk; no committed version of the canonical entry contains `昭和以降` or `近現代`. The served
`[日本]` branch has 18 options and the entry enumerates 17. This is RevEntryQuality's cut, and it
needs landing this round alongside CUT C.

**F2 — S874's carrier order is load-bearing for the strict same-page check.** The 2020 carrier's
embedded original is `http://www.ihchina.cn/project.html` (the archive's own record for that
timestamp is `http://www.ihchina.cn:80/project.html`), while the live URL is `https://`. Under a
scheme-preserving normalizer the *first* carrier does not normalize equal to the live URL; only the
2026 carrier does. Because `CAPTURE_RE` is end-anchored, the check currently reads the 2026
carrier and passes. The round-72 counter's own `norm_url` (netloc+path) is scheme-blind, so both
carriers pass there. **Consequence: if a later edit appends or reorders a carrier, the strict check
flips to FAIL.** The archive serves the 2020 capture byte-identically under the `https://`
spelling (sha256 `d3274d85…` for both, measured), so if this is ever re-spelled, the `https://`
spelling is the one that keeps the strict check green — but that is a re-spelling of the archive's
own record and should not be done silently. Leave S874 as landed and note the dependency.

**F3 — "wording identical to the 2026-10-20 capture" is true of the register, not of the page.**
The amendment (§2, last paragraph) says the live page served *"wording identical to the 2026-10-20
capture"*. Diffing the two bodies: they are identical except for the page's own date widget
(`2026-10-25 星期日 农历九月十六` live vs `2026-10-21 星期三 农历九月十二` in the capture — the capture
timestamp 2026-10-20 18:39 UTC is 2026-10-21 02:39 in the site's UTC+8 clock). The register's
content is identical, which is the substantive claim; the page's date line is not. LOW severity —
consider *"register wording identical"*.

**F4 — the CJK anchor cells are not reopen-tool-extractable (pre-existing, not a round-72
regression).** `tools/reopen-row.py S874` and `S875` both return `NO_QUOTE attempts=0`: the anchor
cells use CJK corner brackets 「」 and `cell_quote()` recognises only `"` / `“` / `„` / `‟`. Even
with an ASCII-quoted span a CJK quote normalizes to 1 word against `MIN_QUOTE_WORDS = 8`, so it
could never pass. **158 of 799 registry rows are in the same state**, including the whole round-71
S861–S873 batch and the pre-existing CJK rows S330/S331/S576, so this is a lane-wide condition and
no round-72 gate requires a quoted span in a row's anchor cell. Noted so it is not mistaken for a
new defect; a lane-wide fix (CJK-aware quote extraction) is a separate round's work.

---

## 8. Evidence index

Everything below was produced on 2026-10-25 from the lane's committed bytes and live fetches; no
lane byte was written.

| claim | how it was checked | result |
|---|---|---|
| 2-row design is the landed one | `git log --oneline -- corpus/SOURCES.md` | `770100f`, `868107e`, `ba8ad3a` |
| counter green at HEAD | `python3 -B reports/round-72/accept-c.py --root . --lands 21ad3088…` | `ACCEPT-C-72: PASS legs=10/10` |
| census clean | `scripts/sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-25` | exit 0, no S874/S875 finding |
| (a)/(c) fail the frozen ROWS leg | counter's `parse_rows` + `NEW_IDS` on simulated 3- and 4-row trees | `added=['S876']` / `added=['S876','S877']` → FAIL |
| capture is the same page | Wayback CDX `url=www.ihchina.cn/project.html` | both timestamps `urlkey cn,ihchina)/project.html`; 2020 original `http://www.ihchina.cn:80/project.html` |
| 2020 replay is one payload | `curl` both embedded-original spellings, `sha256sum` | `d3274d85ea5433f0ff7871d8668db3f2bdd87e0995ae933f14ea73a57268c1b4` for both, and for `/tmp/ihchina-2020.html` |
| register content identical across carriers | `grep -c` per carrier | taxonomy + code-rule sentences identical; only 四批/五批 differ |
| (a) duplicates the live URL | census validate on a 3-row mirror | `W04 S876 duplicate url www.ihchina.cn/project.html across scopes` |
| (a)/(c) make the claim uncitable | `tools/check-cited-lines.py` on one comparative line with two ids | `MULTI-ID … S874,S876` / `S876,S877`, exit 1 |
| CUT A is counter-neutral | real counter in a scratch clone, fix applied then reverted | 10/10 with fix, 10/10 control |
| CUT A keeps the lint clean | `tools/check-cited-lines.py` on the fixed amendment | 0 findings, exit 0 |
| CUT B terminals | parsed `<option>` list of the live `時代` select | `[中国]` last = 近現代 (清 at 19/21); `[朝鮮半島]` last = 近現代 (李氏朝鮮 at 8/10) |
| C4 not landed | `git show ba8ad3a` diff + `git show <each rev>` for `昭和以降`/`近現代` | no `§4` hunk; 0 occurrences in every committed version |
| strict same-page check on S874 | `check-row-fragments.py` `norm_url` + round-65 `CAPTURE_RE` | `True` (last carrier is `https://`-embedded) |
| no access-control bypass | `tools/check-source-access.py --root .` | `ACCESS: 3 flagged rows, 0 findings` |
| unstable counters not cited | `grep` for 1372/1557/3145/3610/308473 in both entries | 0 hits in the entries |
| used-by honesty | `grep -c S875` in each entry | amendment 0, canonical 5 → S875's used-by correctly omits the amendment |
| live page reachable | `curl` ×5 + browser UA | 200 on all; one initial 25 s timeout; live body == 2026 capture body except the date widget |

Tooling: no installs. `python3` (system 3.14), `curl`, `git`, `bash`, and the lane's own tools
(`accept-c.py`, `check-cited-lines.py`, `check-source-access.py`, `reopen-row.py`,
`check-row-fragments.py`) plus `scripts/sources-census.sh`. `pacman` untouched (host-wide pause in
force). Scratch artifacts under `/tmp/simplifierrows/` only; the scratch clone
`/tmp/simplifierrows/clone` and the fake fleet `/tmp/simplifierrows/fakefleet{,2}` were used for
the counter runs and are throwaway.

---

## 9. One-line summary for the L1

Keep two rows (S874 with both captures as carriers, S875); land CUT A (scope the amendment's
2026-state and cross-capture claims to S874 — counter-neutral, fixes a defect the gate cannot see)
and CUT B (S875's two era-branch terminals are `近現代`, not `清`/`李氏朝鮮` — the row-side half of
RevEntryQuality's unlanded C4); leave S874's carrier order alone but note that F2 depends on it.
