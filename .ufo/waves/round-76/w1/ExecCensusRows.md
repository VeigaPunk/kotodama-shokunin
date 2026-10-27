# ExecCensusRows — round 76, wave 1 (claim C, SOURCES.md rows)

Verdict: the append block for claim C is built, normalized to the lane's registry schema and validated in a
scratch mirror — `validate` exit 0 with no E-code, `census` 817 → 821 rows, four anchor quotes each located
verbatim in a body fetched this round, all four recheck commands run and returning non-zero. One planned pair of
rows collapses to one document (openstd `showGb` 302s onto `newGbInfo` with a byte-identical body), so the block
carries four rows S894–S897 and S898 is unused. Two drafted-claim premises are contradicted by today's
measurements (§6) and one candidate entry is tier-C-only (§6.3); those are L1 decisions, not mine.

Nothing in the lane was written. No tool was installed.

## 1. Deliverables (lane-relative paths, under `.ufo/waves/round-76/w1/`)

| path | what |
|---|---|
| `stage/ExecCensusRows/rows-block.md` | the append block, 4 rows, 4 lines, md5 `a6f5c4b6312059f3e3e529927ee5519b` — `md5sum rows-block.md` |
| `stage/ExecCensusRows/validate-receipt-draft.txt` | 150 lines: fetch log, showGb/newGbInfo identity measurement, quote check, `validate`, `census`, the seven manual census commands, the four recheck commands with their outputs |
| `stage/ExecCensusRows/window/` | 7 fetched bodies (752K — `du -sh window`) + `MANIFEST.md5`, the evidence windows a Gate can re-check the quotes against |
| `w1/ExecCensusRows.md` | this report |

## 2. The four rows

| id | document | kind/tier | used-by | anchor quote (≤25 tokens, ≤80 chars) |
|---|---|---|---|---|
| S894 | 国立公文書館デジタルアーカイブ 詳細検索, live + Internet Archive capture 2026-04-22 | dataset / A | `calendar-festival-systems.amend-2026-10-24.md`, `era-periodization-models.amend-2026-10-23b.md` | 「元号名称 開始西暦年 令和 2019」 (18 chars, 4 tokens) |
| S895 | GB/T 33661-2017 原文及解读材料 on 星座百科网 (third-party republication) | spec / C | `calendar-festival-systems.amend-2026-10-23c.md`, `calendar-festival-systems.amend-2026-10-24.md` | 「置闰规则为：取其中最先出现的一个不包含中气的农历月为农历闰月」 (30 chars, 1 token) |
| S896 | 国家标准全文公开系统 record page for GB/T 33661-2017 — live `newGbInfo`, the `showGb?type=online` route, and the capture of 2026-04-24 | docs / A | `calendar-festival-systems.amend-2026-10-24-r10.md`, `calendar-festival-systems.amend-2026-10-24.md` | 「标准号：GB/T 33661-2017」「中文标准名称： 农历的编算和颁行」 (19 + 16 chars) |
| S897 | 光明日报,「农历编算有了国家标准 春节端午等假期与其密切相关」, 2017-05-23 | docs / A | `calendar-festival-systems.amend-2026-10-24.md` | 「首次明确了农历的编排规则、计算模型和精度等」 (21 chars, 1 token) |

Every cell: 11 columns (NF=13), no `|` and no `\|` inside any cell, `status mined`, `opened 2026-10-27`,
`recheck 180d` (the curl commands stripped out of the cell and kept in the receipt §7, because a cell holding a
pipeline is what the staged rows got wrong). Counts — `awk -F'|' '{print "NF="NF}' rows-block.md` → NF=13 four
times; `awk '{print gsub(/\|/,"|")}' rows-block.md` → 12 four times.

## 3. Scratch validation (mirror = a copy of the lane, `.git`/`.ufo` excluded, block appended after row S893,
the four candidate entry stubs copied to their proposed lane-relative paths so used-by resolves)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-27
file	W01	S895 tierC mined used-by=corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md, corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md
file	ok	/fast/scratch/hyaku/kotodama-r76/ExecCensusRows/mirror/corpus/SOURCES.md
VALIDATE_EXIT=0
```
E-codes: `grep -cE '\tE[0-9]+' validate-mirror.txt` → 0. (The warnings the task allows: `grep -c 'W04' validate-mirror.txt` → 28 and `grep -c 'W01'` → 5, one of the five
being S895; the W04 lines are on rows S127…S830, not mine — `grep -E 'S89[4-7]' validate-mirror.txt | wc -l` → 1.)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --file corpus/SOURCES.md --today 2026-10-27
file	rows	821
file	tier.A	494
file	tier.B	310
file	tier.C	17
file	status.mined	726
file	status.queued	58
file	status.rejected	37
FLEET	missing	0
CENSUS_EXIT=0
```
Before, on the lane's own file: `file rows 817 · tier.A 491 · tier.B 310 · tier.C 16 · mined 722 · queued 58 ·
rejected 37` — same command with `--file corpus/SOURCES.md` from the lane root. So 821 − 817 = 4 rows added
(`821 — census rows`; `817 — census rows`), tier A 494 − 491 = 3, tier C 17 − 16 = 1, mined 726 − 722 = 4.

The seven `CORPUS.md` manual commands, from the mirror root: rows `821`, malformed `0`, tier `A=494 B=310 C=17`,
status `mined=726 queued=58 rejected=37`, duplicate ids: nothing, enum violations / tier inflation: nothing,
mined rows with a missing used-by path: nothing (verbatim in receipt §6).

## 4. Quotes and rechecks (all run 2026-10-27, browser UA, plain GET, no login or challenge)

Quote check (`python3` over the fetched bodies, whitespace-normalised): all five spans `OK`, e.g.
`OK S895 chars=30 tokens=1 | 置闰规则为：取其中最先出现的一个不包含中气的农历月为农历闰月 | hit: fetchlog/S895-c6fb2ac5.body`,
final line `ALL QUOTES PRESENT: True`. Note this catches a real defect: the first draft of the S895 anchor omitted
`月为` (`…中气的农历闰月`), which greps 0 against the page — `grep -ac '取其中最先出现的一个不包含中气的农历闰月'` → 0,
the page's sentence is `…中气的农历月为农历闰月` → 1.

Rechecks, each `curl -fsSL --compressed -A "$UA" <url> | grep -c <needle>`:
S894 → 3 (`元号名称`), S895 → 1, S896 → 2 (`GB/T 33661-2017`), S897 → 1. Fetches: every URL answered
`http=200` except the `showGb` route, which answered `302` with `Location: …/newGbInfo?…&refer=outter` and a
followed body byte-identical to the direct route (`24144 bytes, md5 e866bfd61a16f4c4fcdc1fc3a16bdf89` on both —
receipt §2). Captures are dated by `x-archive-orig-date`: `Wed, 22 Apr 2026 14:50:52 GMT` (archives) and
`Fri, 24 Apr 2026 03:10:28 GMT` (openstd).

## 5. Normalization and refusals

- The staged rows in `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` were **not** copied. Their
  `recheck` cells hold whole curl pipelines with escaped pipes (`180d — \`curl … \| iconv …\` -> 1`), which the
  lane's cells do not carry and which the contract's E09 check reads as prose; and their ids S894–S898 already
  name *different* documents (Sowers-Wills 2024, 王昕玥, a Korean KCI paper, 魏斌, NDL NDC10) — none of which any
  candidate entry cites. The block was rebuilt from the six campaign rows that the candidate entries actually
  cite (S908, S916, S932, S935, S937, S938) and re-pointed by document.
- Ids: archives → S894, xingzuobaike → S895, openstd record → S896, gmw → S897. The plan's S896 (newGbInfo
  capture) and S897 (showGb page) are one document by measurement, so they share S896 and S898 is not used.
- No row was written for a source that could not be opened: all four documents returned HTTP 200 (the 302 lands
  on the same document). Nothing was recorded as UNVERIFIABLE.
- `S894`/`S896` carry both a live address and an archive capture of the same page in one cell, in the lane's
  existing style (cf. S885–S892, which were written this round).

## 6. Findings the L1 needs

1. **S932's premise is stale.** The drafted row says "the live record page no longer serves this text; the
   archived capture does". Today the live page serves the whole record:
   `curl -sS --compressed -A "$UA" https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=… → http=200, 24144 bytes,
   md5 e866bfd61a16f4c4fcdc1fc3a16bdf89`, and the 标准信息表 fields are all present (`标准号：GB/T 33661-2017`,
   `标准状态： 现行`, `发布日期 2017-05-12`, `实施日期 2017-09-01`, `CCS A46`, `ICS 07.040`, 主管部门/归口部门 中国科学院).
   My row leads with the live page and keeps the capture as corroboration. If the frozen claim repeats
   "the live page no longer serves", it is wrong as of 2026-10-27.
2. **S935's premise is stale in the same way.** The live archives search page serves the 元号 table today
   (`grep -c '元号名称'` → 3 on the live page, 3 on the capture); the capture is not the only carrier.
3. **Tier-C sole support.** `calendar-festival-systems.amend-2026-10-23c.md` cites S916 (→ S895, tier C) alone.
   If it is admitted it needs an authoritative row beside it (S896/S897), otherwise the Gate must reject it —
   the claim's after-state forbids a tier-C row as the sole support of an admitted entry. The validator says the
   same thing with `W01 S895`.
4. **Campaign-id re-pointing before landing** (kill rule): S937→S897, S935→S894, S908→S894, S932→S896,
   S938→S896, S750→S896, S718→S896, S916→S895, S919→S892, S921→S885. S750/S718 are the openstd record by
   document (their descriptions in the entries name "the official registry record"); S807 is unresolved — see the
   next item.
5. **S807 is an inference.** The retained round-7 passage in `calendar-festival-systems.amend-2026-10-24.md` cites
   campaign S807 for "a third-party reproduction" of the standard. `grep -rn 'S807' /home/vgpnk/Projects/shokuknow/merge/kotodama`
   hits only that entry file; no S807 row ships in the package, and the only reproduction URL in the package is
   xingzuobaike (`grep -rl 'xingzuobaike'` → `SOURCES.append.md` and that same entry). [INFERENCE] S807 → S895.
   If the L1 resolves S807 to another URL, trim `calendar-festival-systems.amend-2026-10-24.md` from S895's
   used-by and add a fifth row (which would take S898).
6. **Two in-place updates outside my block** (append-only, logged old→new in the round lesson): S885 and S892
   should gain `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` in `used-by` if
   that entry is admitted — it cites both (S921→S885, S919→S892). I did not touch them.
7. **The claim's "before" sweep is imprecise.** `git -C …/kotodama-shokunin grep -l -E 'GB/T 33661' 98c486b -- corpus`
   prints `corpus/lessons/round-68.md` and `corpus/lessons/round-69.md` (exit 0), and the same for
   `digital\.archives\.go\.jp` → `corpus/lessons/round-68.md`. Restricted to the registry
   (`-- corpus/SOURCES.md`) both print nothing and exit 1. So "each print nothing (exit 1)" holds only for
   `corpus/SOURCES.md`, not for `corpus` — the frozen claim should say which.

## 7. Unrun / limits

- No build, lint, formatter or test beyond the census was run (editing wave in flight; the parent owns the gate).
- Nothing was landed in `corpus/SOURCES.md`; the block is a stage artifact, only the L1 commits.
- The scratch mirror and fetched bodies under `/fast/scratch/hyaku/kotodama-r76/ExecCensusRows/` are deleted before
  this seat exits; the citable copies are `stage/ExecCensusRows/window/` (with `MANIFEST.md5`) and the receipt.
- The Gate still has to re-locate each quote inside a committed evidence window at freeze; the windows are
  provided so that check is mechanical.
