# ScribeEntries — round-72 w1 (leaf seat L1Kotodama72.ScribeEntries)

Date: 2026-10-25. Assignment: draft the two FINAL adopted entries at `/tmp/r72-entries-scribe/`
from the read-only staged entries under `/home/vgpnk/Projects/shokuknow/merge/kotodama/`, with the
re-point rules of claims.json leg REPOINTED, in the lane house style of
`corpus/knowledge/culture-material/dance-performance-movement-codes.md`; `verified-at: 2026-10-25`;
canonical body §1–§7 as staged; amendment body as staged but with every live-2026 claim restated as
capture-verified (2026-10-20 capture). Drafts are advisory — the L1 integrates.

## Files produced (drafts only, advisory)

- `/tmp/r72-entries-scribe/heritage-taxonomy-models.md`
- `/tmp/r72-entries-scribe/heritage-taxonomy-models.amend-2026-10-24-r13.md`

No lane file was created or modified by this seat. The two entries already present in the lane
worktree (`corpus/knowledge/culture-material/heritage-taxonomy-models.md` and its `.amend-2026-10-24-r13.md`,
both untracked as of this seat's reading) are the L1's integration, not mine; my drafts are a
second, independently derived pair for the L1 to choose from. No tool was installed or upgraded
(no pacman, no uv/npm/cargo) — only stock `curl`, `python3`, `git`, `grep`, `find` were used.

## Re-pointing applied (leg REPOINTED: by document, never by arithmetic id shift)

| staged row | staged document | lane id | carrier cited in the draft's `source:` line |
|---|---|---|---|
| S863 | ihchina register 清单页 (live) | **S874** | `https://www.ihchina.cn/project.html` |
| S967 | Internet Archive capture 2020-02-16 of the same 清单页 | **S874** | `https://web.archive.org/web/20200216023423id_/http://www.ihchina.cn/project.html` |
| S967 | Internet Archive capture 2026-10-20 of the same 清单页 | **S874** | `https://web.archive.org/web/20261020183948id_/https://www.ihchina.cn/project.html` |
| S867 | 文化遺産データベース 文化財検索 | **S875** | `https://online.bunka.go.jp/db/heritages/search` |

Every `source:` line in both drafts names exactly one id, both ≥ S874, and every URL it names is a
URL present in that id's registry row (checked mechanically against
`.ufo/waves/round-72/assimilation/validate/rows-inserted.txt` with the drafted counter's own
`parse_rows` / `urls_in` / `norm_url` helpers — see "counter dry-run" below). The staged ids
S863/S867/S967 appear nowhere in the drafts' `source:` lines.

Foreign references repaired (the staged text pointed at the campaign mirror, not at this lane):
- staged "the lane's row S837" → the ihchina live page / the register's 清单页 (in this lane S837 is
  BBC Sikhism — "BBC Religions, Sikhism: The Five Ks"); the reference is rewritten to name the
  document, and the residual round-11/12-history claim is marked `[UNVERIFIED-CLAIM]` (see below).
- staged couples `culture-material/calendar-festival-systems.amend-2026-10-24-r10.md` → the
  existing `culture-material/calendar-festival-systems.md` (that amend file does not exist in this
  lane; the base file does).
- staged couples `myth-symbol/calendar-festival-systems.md` → `culture-material/calendar-festival-systems.md`
  (the myth-symbol path does not exist; `git ls-tree` confirms the culture-material one does).
- staged canonical `gap filled` sweep "over the 643-row registry" → the real registry at base
  `b60c7b1` is **797 rows**; the sweep was re-run and returns **0** (see commands below).
- staged canonical `recheck` pointing at the campaign `SOURCES-PROPOSED.md` → the two normalized
  rows' real recheck commands, with the counts I measured (1 / 1 / 3).

## Header fields (all nine present, in the required order)

Both drafts carry `source` / `verified-at` / `recheck` / `ground` / `topic` / `gap filled` /
`sources` / `couples` / `scope`, `verified-at: 2026-10-25`, in the house style of the dance entry
(`- field:` bullets, `##`-numbered body sections). Verified mechanically: the drafted counter's
`header_field_names()` + `HEADER_FIELDS` reports **no missing field** for either file. Note the
counter's `HEADER_FIELDS` spells the field `gap-filled`; `norm_label()` strips punctuation, so
`gap filled` matches — no action needed, and the house style (`gap filled`) is kept.

## Canonical body §1–§7 (as staged)

The staged canonical body is a seven-item outline (calibration key / state-grade category model /
state-grade domain taxonomy / two period ladders / record-level fields / building an invented
culture's taxonomy / coupling to the world bible). The draft expands exactly those seven sections,
§1–§7, with content drawn only from the round-72 re-open evidence.

Verified against the re-open evidence (files `/tmp/ihchina-2020.html`, `/tmp/ihchina-2026.html`,
`/tmp/bunka.html`, all present; no scout ask was needed):

- §2 — the ten 门类 sentence, the ten names (民间文学 … 民俗), the code rule
  `编号中的罗马数字代表所属门类` (example Ⅱ-28), and the extension rule
  `从第二批国家级项目名录开始，设立了扩展项目名录` are each present **verbatim and identical** in
  the 2020 capture, the 2026 capture and the live page (sentence-level equality checked by
  extraction, not by eye).
- §3 — the 分野 tree's top level, as served: **16** top-level options (建造物, 伝統的建造物群, 絵画,
  版画, 彫刻, 工芸, 考古, 歴史, その他の美術, 民俗, 伝統芸能, 工芸技術, 文化財保存技術, 史跡, 名勝,
  天然記念物) with 建造物 → 宗教建築 / 城郭建築 / 住居建築 / 近世以前その他 / 近代その他 beneath it.
  The served tree nests sub-options by indentation, and 記念物 is **not** a 分野 of its own — it
  appears only inside the 指定区分 facet (記念物(史跡) / 記念物(名勝) / 記念物(天然記念物)); the
  staged canonical's §3 phrasing that listed "記念物 / 天然記念物" as domain-tree members is
  therefore corrected in the draft, not copied.
- §4 — the 時代 select's three served branches verbatim ([日本] 18 options ending 令和 with both
  昭和以降 and 昭和 present; [中国] 21 options 旧石器…近現代; [朝鮮半島] 10 options
  旧石器…近現代). The staged entry named only the [日本] and [中国] branches; the [朝鮮半島]
  branch is served and is recorded.
- §5 — 材質・構造・技法, サイズ and 所在地 are per-record labels in the served record rows;
  指定区分 is a **search-form facet** with 29 served options (国宝 … 重要文化的景観), not a
  per-record field. The staged canonical called all four "record-level fields"; the draft
  distinguishes facet from record label and enumerates the 29 served classes.
- §6 — the stability claim ("category system and code rule word-for-word identical in the 2020 and
  2026 captures; the batch count grew four → five") is carried by the captures themselves.
- §1 — the "counters are dated readings, not anchors" calibration is grounded in the register's own
  moving inventory (1372 国家级项目 / 3145 子项 in the 2020 capture; 1557 / 3610 in the 2026
  capture). The Japanese page's own result counter is named but deliberately not quoted as an
  anchor.

## Amendment body: live-2026 claims restated as capture-verified (2026-10-20 capture)

The staged amendment's §N contrasted "the 2020 capture" against "the live page today". Per the
assignment that live-2026 claim is restated as capture-verified, so the draft contrasts the
**2020-02-16 capture** against the **2026-10-20 capture** (`20261020183948id_`), with both dated
states quoted from the captures:

- 2020 capture: `国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录`, plus 共计1372个国家级
  非物质文化遗产代表性项目 / 共计3145个子项 / 涉及…保护单位3154个.
- 2026-10-20 capture: `国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录`, plus
  共计1557个…项目 / 共计3610个子项.
- The taxonomy sentence, the ten names, the code rule and the extension rule are word-for-word
  identical across the two captures (checked by extraction).
- The live page as served 2026-10-25 carries the **2026** state, byte-identical to the
  2026-10-20 capture on all four sentences checked — so the live page is named as the carrier for
  "anything newer" while every dated claim in the body rests on a capture.

### Claims cut or marked `[UNVERIFIED-CLAIM]` (not carried by the re-open evidence)

Four staged claims have no support in this lane's artifacts; per the instruction ("cut or mark
[UNVERIFIED-CLAIM] anything the re-open evidence does not carry") they are **marked, not
asserted**, so the L1 can cut them in one edit:

1. amendment `ground`: the attribution to "round 12's CANNOT-ANSWER §4.3" — no `CANNOT-ANSWER`
   heading and no ihchina record exists in this lane's `corpus/lessons/round-11.md`,
   `corpus/lessons/round-12.md`, `reports/round-11.md` or `reports/round-12.md`
   (`grep -rin 'ihchina\|非物质文化遗产'` over those four files → 0 hits; `grep -rn 'CANNOT-ANSWER'`
   over `corpus/` and `reports/` → 0 hits). The draft's `ground` instead states the ground the
   evidence does carry (797-row registry sweep = 0 owners), and marks the round-12 attribution.
2. amendment `gap filled`: "round 12 recorded the register's ten categories … from a single reading
   of the live page (row S837)" — no such reading is recorded here, and S837 in this lane is BBC
   Sikhism; marked.
3. amendment §N+1: "the live page answered neither round 11's probe nor round 12's gate, and round
   11's CDX query for it returned nothing that was re-checkable, so the row had no substitute
   carrier" — no such probe or CDX record survives in this lane's round-11/12 artifacts; marked.
   (Its *contradictory* live-2026 reading is also visible: the live page answered HTTP 200 from this
   host on 2026-10-25, repeatedly.)
4. amendment §N+1 (staged): "it is a fast, stable host" — an operational claim not derivable from
   static captures; **cut outright** from the draft rather than marked.

Note for the L1: item 3's premise is also contradicted by this round's own fetch (live HTTP 200,
43255 bytes, 四批/五批 sentence present), so the marked sentence and the live-2026 evidence point
opposite ways. Cutting it is the cleaner resolution.

## Commands run and their exact outputs (2026-10-25)

```
$ grep -inE 'ihchina|非物质|非物質|文化遺産|heritage online|bunka' corpus/SOURCES.md | wc -l      # base b60c7b1: 0
$ git show b60c7b1:corpus/SOURCES.md | grep -c '^| S'                                          # 797
$ git ls-tree -r --name-only b60c7b1 corpus/knowledge | grep -ci 'heritage-taxonomy'           # 0
$ curl -fsSL --compressed 'https://web.archive.org/web/20200216023423id_/http://www.ihchina.cn/project.html' | grep -c '公布了四批国家级项目名录'   # 1
$ curl -fsSL --compressed 'https://web.archive.org/web/20261020183948id_/https://www.ihchina.cn/project.html' | grep -c '公布了五批国家级项目名录' # 1
$ curl -fsSL --compressed 'https://online.bunka.go.jp/db/heritages/search' | grep -c '安土・桃山' # 3
$ curl -fsSL 'https://www.ihchina.cn/project.html' -o live3.html -w 'status=%{http_code}'       # status=200 size=43255
$ grep -c '编号中的罗马数字代表所属门类' live3.html                                            # 1
```
Sentence-level extraction over the two captures + live page confirmed: batch sentence differs
between 2020 and 2026 captures and is identical between the 2026 capture and the live page; the
ten-category sentence, the ten names, the code rule and the extension rule are identical across all
three. From `bunka.html`: `id_list_era` parsed into three branches (18 / 21 / 10 options);
`id_list_genre` parsed into 16 top-level options with indented sub-options; `id_list_classification`
parsed into 29 指定区分 options; per-record labels 材質・構造・技法 ×14, サイズ ×7, 所在地 ×12.

## Counter dry-run against the drafted counter (`.ufo/waves/round-72/counters/accept-c.py`)

I imported the drafted counter as a module and applied its own parsers to my two drafts against
`.ufo/waves/round-72/assimilation/validate/rows-inserted.txt`:

- `header_field_names()` → no missing field for either draft.
- `source_lines()` → canonical: `['S874']` (1 URL) and `['S875']` (1 URL); amendment: `['S874']`
  (2 URLs, both the 2020 and 2026 capture URLs). Every cited URL normalizes to a URL present in that
  id's registry row — leg REPOINTED's URL condition holds.
- `python3 -B tools/check-cited-lines.py` over both drafts → `CITED-LINES: 0 finding(s) in 2 file(s)`,
  exit 0 (leg CITEDLINES).

I did not run the counter end-to-end: it requires a committed `<lands>` revision, which does not
exist yet, and committing is the L1's step.

## Known limits / out of scope

- The drafts are advisory; the L1 chooses between my pair and the pair already in the worktree.
  Where the two differ materially: (a) my canonical lists the 16 served 分野 top-level options and
  the 29 指定区分 classes explicitly, and separates facet from record label; (b) my amendment
  contrasts the two **captures** (as the assignment requires) rather than capture-versus-live;
  (c) my amendment's `ground`/`gap filled` are re-grounded on the 797-row sweep instead of the
  unlocatable round-12 attribution, with the latter marked.
- I did not touch `corpus/SOURCES.md`, the lesson, the registry rows, the counter, or the lane's
  git/jj state. The two rows' `used-by` cells and the lesson's Gate tables remain the
  executor's/scribe-lesson's surfaces.
- The 2026-10-20 capture's `20261020183948id_` timestamp was supplied by the wave spec; I re-fetched
  that exact URL and it served the 五批 wording, so the timestamp is corroborated by fetch, not
  merely inherited.
- §4's claim that the 時代 ladder is "a different vocabulary" from political era names is a
  comparative reading of two catalogues in this lane (`era-periodization-models.md` vs the served
  時代 select), not a claim about either real institution.

## Suggested L1 follow-ups (one line each)

1. Cut the three marked `[UNVERIFIED-CLAIM]` sentences in the amendment's `ground`, `gap filled` and
   §N+1, or replace them with located text.
2. Decide the canonical pair to land: mine (`/tmp/r72-entries-scribe/`) versus the worktree copy.
3. If the worktree copy lands, apply my three §-level corrections (16 分野 top-level options;
   指定区分 as facet with 29 classes; 記念物 not a 分野) and the 時代 [朝鮮半島] branch.

Artifact paths: `/tmp/r72-entries-scribe/heritage-taxonomy-models.md`,
`/tmp/r72-entries-scribe/heritage-taxonomy-models.amend-2026-10-24-r13.md`,
`/tmp/ihchina-2020.html`, `/tmp/ihchina-2026.html`, `/tmp/bunka.html` (re-open evidence, fetched
2026-10-25 by the lane; not fetched by this seat except the live ihchina and bunka re-checks).
