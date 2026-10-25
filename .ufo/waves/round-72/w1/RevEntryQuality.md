# RevEntryQuality — round-72 w1 (seat L1Kotodama72.RevEntryQuality)

Date: 2026-10-25. Scope: judge the two staged heritage-taxonomy entries against
`corpus/QUALITY.md` and `PROVINCE.md`; verdict per entry
(admit-as-is / admit-with-cuts / refuse); (d) claims the two re-opened sources cannot support.
Leaf seat: no subagents, no background jobs, no lane mutations — this report is my only write.

## Object under judgment

Drafts are mutable files under `/tmp/r72-entries/`; they changed twice during this review
(11:26 → 11:27:42 → 11:33:48). Verdicts are pinned to the bytes I read last:

| file | sha256 | mtime |
|---|---|---|
| heritage-taxonomy-models.md (canonical) | `e30ac84475a5c88fbc09caf785575d1a589b3af4cb952d7a581edf3703d3d783` | 11:33:48 |
| heritage-taxonomy-models.amend-2026-10-24-r13.md | `89b747a7fa540d3b6ea0074843557f4effa7db6fda53c2ab54c96619ec1a84a3` | 11:27:42 |

Evidence relied on (this round's re-open artifacts, /tmp): `ihchina-2020.html` (sha `d3274d85…`),
`ihchina-2026.html` (`c0f46caa…`), `ihchina-live.html` (`1510bc63…`; md5-identical to
`/tmp/scoutihchina/live-project.html` `ef9a8659…` — the live fetch is real, one file two copies),
`bunka.html` (`729ca601…`), `ScoutBunkaReopen/genre_options.txt` (`e70dd9f2…`),
`ScoutBunkaReopen/era_options.txt` (`54d89116…`).

Tooling: no installs (python3 system build; lane's own `tools/check-cited-lines.py`; pacman untouched).
Checks run on the pinned bytes: `check-cited-lines.py` — canonical exit 0 (0 findings),
amendment exit 0 (0 findings). All quoted spans below were grepped/extracted directly from the
evidence files (body contexts inspected, not captions/attributes).

## (a) In-province? — YES for both

- **Partition**: PROVINCE owns "costume & material-culture terminology" and "era/period models";
  both entries are classification references (state filing taxonomies for material and intangible
  culture; a period ladder) landing in `corpus/knowledge/culture-material/`. The amendment is
  dating/citation practice for one corpus entry — craft records, not general research method.
- **No canon**: canonical scope cell ("decides no world's canon") + `refuses` cell; amendment
  scope cell ("it decides no world's canon"). No world-specific fact is asserted anywhere; the
  registers' own counters (1372/1557) are correctly *not* cited ("not used as anchors").
- **Lore handoff respected**: canonical couples and §7 name
  `synthesis/worldbible-integration-contract.md` (exists, 28,421 bytes) and §7 states "Kotodama
  hands off systems; lore records and verifies them" — mirroring PROVINCE's adjacent contract,
  not absorbing it. Borderline noted and ruled in-province: the amendment's second section teaches
  capture-as-stand-in citation for *this corpus's* entry — entry-citation craft, not chousa's
  general source-research trade.

## (b) QUALITY bar

**Canonical** — header complete per claim leg ENTRIES: source ×2 / verified-at / ground / recheck /
gap-filled / topic / sources / couples / scope (+ `refuses`). Provenance: every §1–§5 factual claim
checks against the pinned evidence (verified spans listed under (d)); no laundered
unverifiables except the cuts named below. Calibration (criterion 2): no explicit
mainstream/contested cell — consistent with lane practice (`era-periodization-models.md`, a
comparable admitted reference, has none); §1 "Calibration key" plus the state-primary nature of
both sources performs the duty; no pop-mythography involved. Observation, not a defect.
Coupling (criterion 3): four targets, all exist on disk. Usability (criterion 4): §5 field→decision
map and §6 build order; not an essay. Canon hygiene (criterion 5): clean. Criterion 15 lint: exit 0.
Criterion 10: both rows opened by ordinary means (plain fetch; Internet Archive captures; one
initial 25 s timeout recorded honestly); no access-control bypass anywhere in the evidence.

**Amendment** — header complete: source / verified-at / recheck / ground / topic / gap-filled /
sources / couples / scope. Its factual spine verifies exactly: the 2020 capture reads
「国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录」 (×1 verbatim), the
2026 capture and the live page read 「…2014年和2021公布了五批国家级项目名录」 (×1, without 年 —
the source page's own wording; the entry quotes it faithfully), 十大门类 sentence and code rule
word-for-word identical across 2020/2026/live, and "wording identical to the 2026-10-20 capture"
holds for the live page on the quoted spans. No overreach found; lint exit 0.

## (c) §6/§7 — inside "reference method, no canon"? YES

§6 is a build order over state-shaped fields, explicitly "take the state-shaped fields, not the
labels"; §7 is a pure handoff ("lore decides the invented category names, code rules, and which
bodies keep the register"). Nothing in either section records or decides world canon. The one §6
defect is evidentiary, not canonical (cut C2 below).

## (d) Claims the two re-opened sources cannot support

**Canonical, open cuts (the evidence contradicts or does not reach the sentence as written):**

- **C1 (§5)** — "(national / prefectural / municipal)" protection-tier triad. The served page
  carries only the 指定区分 facet label (`<dt>指定区分</dt>`, ×1) and the page title
  国指定文化財等データベース; strings 都道府県 (×0) / 市町村 (×0) appear nowhere in the captured
  bytes — the facet's option values load via JS (`open_float('classification')`) and were not
  captured. Cut the triad or mark `(to-verify)`.
- **C2 (§6)** — "Both registers show the category system outliving batch updates". The evidence is
  PRC-only (two ihchina captures); the bunka pages carry no batch/update mechanism at all.
  Restrict to "The PRC register shows…".
- **C3 (§6)** — "扩展項目-style" uses 項目 (JP graph); the register's own term, used correctly twice
  elsewhere in the entry, is 扩展项目. Graph fix.
- **C4 (§4)** — the [日本] ladder omits the served option 昭和以降 (value 15, sitting between 大正
  and 昭和 in `era_options.txt`); and "[中国] (旧石器 … 清)" reads 清 as terminal while the branch
  continues to 近現代 (value 36). Insert 昭和以降; restate the 中国 branch as non-terminal.

**Already fixed in the pinned bytes** (present in the 11:27:42 revision, gone at 11:33:48; recorded
because I verified against both): §3's earlier "top level … runs [10 options]" (the form serves 16
top-level 分野 options; the ten-option list presented a subset as exhaustive) and §5's "present in
the served form **and record pages**" (the fetched detail pages `d_*.html`/`detail*.html` are empty
DB shells, title only, ×0 for all four fields; the fields are evidenced on the search page's
per-record result rows, e.g. 材質・構造・技法：紙本木版色摺 / サイズ：22.8×34.1 /
所在地：富山県高岡市古城1-5). Both corrections match the evidence and stay.

**Verified as supported (no action):** four-batch and five-batch sentences verbatim (incl. the
page's own 「和2021公布」 spelling); 十大门类 sentence + all ten category names ×3 in each capture;
code rule 编号中的罗马数字代表所属门类 with the Ⅱ-28 侗族大歌 example; the 2008 five-name
adjustment sentence 「其中五个门类的名称在2008年有所调整，并沿用至今」 (the "page says so verbatim"
claim holds, body text, all three ihchina files); 扩展项目 ×4; all 16 top-level 分野 options and
sub-vocabulary-by-leading-whitespace, 建造物 subs exactly as listed; 時代 arrays for
[日本]/[中国]/[朝鮮半島]; record-row fields 材質・構造・技法/サイズ/所在地; 指定区分 as a search
facet; 安土・桃山 ×3 (matches the declared S875 recheck command's expectation).

**Amendment**: no unsupported claims found. Its recheck duty, live-200 statement, dated-capture
practice, and "categories stable / batch count moves" thesis all verify against the pinned bytes.

## Verdicts

- **heritage-taxonomy-models.md — admit-with-cuts.** Cuts C1–C4 above (C1 and C2 are content cuts;
  C3, C4 are precision fixes). Plus the pre-landing items in the next section.
- **heritage-taxonomy-models.amend-2026-10-24-r13.md — admit-as-is**, subject only to the
  lands-dependencies below (all referenced artifacts land with the round per claim C's legs).

## Pre-landing coordination (outside entry bytes, but the entries assert it)

1. **S874 row cell contradiction (must fix before lands).** The drafted row text
   (`.ufo/waves/round-72/assimilation/` rows-inserted.txt / sources-md.diff) records "live page
   unreachable from the lane host 2026-10-25", while both entries state the live page answered
   (HTTP 200 after one initial 25 s timeout) and the evidence file exists
   (`/tmp/ihchina-live.html` == `/tmp/scoutihchina/live-project.html`). The canonical's sources
   cell even says "and the row says so". Update the row cell to record the late live-200 fetch
   (the truth), or cut the live-open claims from the entries. As drafted, corpus and registry
   contradict each other.
2. **Recheck cadence.** Canonical recheck cell is a single "180d" for both rows; the drafted S875
   row carries 90d (rows-inserted.txt). ExecRenumber's report claims the cadence was rewritten
   "S874 180d / S875 90d" — the pinned bytes do not show it (report-vs-bytes mismatch). Align the
   entry recheck with the rows (per-row or shortest).
3. **Lands dependencies named inside the entries** (must exist at `<lands>`): 
   `reports/round-72/telemetry/gap-sweep.txt` (canonical gap-filled cell — not on disk yet),
   `reports/round-72/telemetry/measures-c.txt` (amendment recheck cell — not on disk yet), and the
   round-72 lesson Gate's located quotes (both entries' sources/ground cells defer to it;
   `corpus/lessons/round-72.md` not yet written at review time).

## Residual risk and verification gaps

- The drafts changed twice during review; my verdicts cover only the pinned hashes. Any further
  byte change to §3/§4/§5/§6 or the header cells invalidates the corresponding cuts and needs a
  re-pass on the changed sections (QUALITY 14 spirit: the judged object is the hashed bytes).
- I verified against this round's on-disk evidence, not by re-fetching the network; the live
  page's provenance rests on the scout's fetch record plus byte-identity of the two live copies
  and span-identity with the 2026-10-20 capture. The rows' recheck cells make re-opening the
  closure's duty.
- The two named lane ids S874/S875 collide numerically with *staged*-space ids S874/S875 (psych
  journals in the package) — different id spaces, no corpus conflict, but cross-reading the
  package against the registry invites confusion; the entries' ground cell correctly avoids
  staging ids and defers to the lesson Gate.
- Round-mechanics criteria (receipts, controls, row shapes, used-by exactness) are the counters'
  legs, not judged here; CITEDLINES at `<lands>` must be re-run on landed bytes.
