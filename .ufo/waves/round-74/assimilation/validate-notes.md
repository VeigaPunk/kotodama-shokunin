# Scratch-mirror validation notes — claim C leg SCRATCHMIRROR (round 74, w1)

> **Superseded (2026-10-25, post-wave update).** §2–§5 below describe the earlier rehearsal built from the *staged* rows
> (staged anchors, staged recheck prose). The current mirror is built from
> `.ufo/waves/round-74/drafts/rows-S881-S884.md` (scout-derived rows with the Gate quotes, `recheck 180d`, tier/scope limits in
> `teaches`) and `.ufo/waves/round-74/drafts/s877-usedby-change.md`; its receipt is `A/validate-receipt.txt` (exit 0, no E-code,
> `--today 2026-10-25`), and `A/validate-receipt-draft.txt` is the superseded draft. §1 (mirror layout) and §6–§7 (pitfalls,
> limits) still apply. Nothing in the lane `corpus/` was written.

Seat: ExecScratchMirror. Date: 2026-10-25. Lane base f7104cbce186bc2e1522abf0cfd619cc834628bb.
Mirror root `A` = `.ufo/waves/round-74/assimilation`; mirror tree `A/validate/` (corpus copy + `SKILL.md`).
Scratch only: nothing under the lane's `corpus/` was written; the lane git index and jj/git state were not touched.

## 1 What the mirror is

- `A/validate/corpus/` — full copy of lane `corpus/` (`du -sh corpus` = 13M: SOURCES.md 957,543 B, QUALITY.md 31,017 B, README.md 169,575 B, knowledge/ 7.8M, lessons/ 3.7M).
- `A/validate/SKILL.md` — copied from the lane root **only** because the pre-existing registry's `used-by` cells name `SKILL.md`; census `E11` resolves used-by paths against the parent of `corpus/`, so the mirror needs it to be a faithful used-by resolver. Not part of the assigned copy list.
- `A/validate/corpus/knowledge/culture-material/worldbuilding-setting-practice.md` and `…amend-2026-10-23.md` — byte copies of the wave-1 draft entries (`sha256 658a8fa4…b00b` and `bb5504e2…673e`).
- Four normalized rows appended to the mirror Registry table: 804 base rows → 808, contiguous S881..S884, plus one in-place change to S877's used-by cell. No other registry byte differs from base.

## 2 Normalization applied (staged → lane)

| lane | staged | document | entry (used-by) |
|---|---|---|---|
| S881 | S883 | https://litmemo.com/ja/blog/novel-worldbuilding-guide | corpus/knowledge/culture-material/worldbuilding-setting-practice.md |
| S882 | S884 | https://tuduku.space/column/novel-worldbuilding | corpus/knowledge/culture-material/worldbuilding-setting-practice.md |
| S883 | S899 | https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md |
| S884 | S900 | https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md |

Applied to every row:

1. id renumbered to the lane namespace (the staged rows carried S883/S884/S899/S900, which collide with lane S883/S884 and with the staged-only S899/S900).
2. `opened` 2026-10-23 → **2026-10-25** (the round that opens them).
3. `recheck` prose cell → **`180d`** (cadence only). The prose that was stripped is kept verbatim in §3.
4. Escaped pipes (`\|`) only ever occurred inside the stripped recheck prose, so no cell carries a literal or escaped pipe now. Verified: every appended row splits to NF=13 with `awk -F'|'`.
5. `status` = `mined`; `used-by` = exactly the entry paths whose `source:` lines cite the row (base entry for S877/S881/S882, amendment for S883/S884).
6. Anchor (quote) cells were kept **as staged** — see the `rehearsal-only` flag in §4.

In-place S877 change (mirror only; the lane row is round-74 business, logged old→new in the round lesson):

- old used-by: `corpus/knowledge/linguistics/conlang-scholarship.md`
- new used-by: `corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`

## 3 Recheck prose moved out of the cells (verbatim, `\|` shown as it was written)

- S881 (staged S883): ``180d — `curl -fsSL 'https://litmemo.com/ja/blog/novel-worldbuilding-guide' \| grep -c '自然環境'` -> 4 (ran 2026-10-23)``
- S882 (staged S884): ``180d — `curl -fsSL 'https://tuduku.space/column/novel-worldbuilding' \| grep -c '設定ノートの構成例'` -> 1 (ran 2026-10-23)``
- S883 (staged S899): ``180d — `curl -fsSL 'https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html' \| grep -c '先做的是世界观'` -> 1 (ran 2026-10-23)``
- S884 (staged S900): ``180d — `curl -fsSL 'https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html' \| grep -c '20章之内慢慢来'` -> 1 (ran 2026-10-23)``

Why this matters: `sources-census.sh` splits rows with `gawk -F'|'`, which does **not** honour `\|`. Each escaped pipe adds a field, so an as-is staged row reports `E01 … fields=12` on top of `E09` for the prose recheck, and its used-by cell is mis-parsed into a fragment (see the mutant control, §5).

## 4 Rehearsal-only quote/anchor cells (NOT evidence)

These anchor cells are exactly as staged. They are placeholders until the scouts' page-side re-quote lands: staged S899/S900 were **REFUSED in rounds 68/71 (register S816/S817)** because the staged quoted spans were absent from the live pages (URL↔quote mispairing), and the staged S883/S884 anchors are section locators, not verbatim spans.

- S881 anchor — **rehearsal-only**: `「小説の世界観はどう作る？」節, the 自然環境/社会の仕組み/文化/個人の経験 block and the 設定資料集 を本文とズレさせない3ステップ 節 — page as served 2026-10-23`
- S882 anchor — **rehearsal-only**: `「世界観設定の5要素」節 + 「設定ノートの構成例」節 — page as served 2026-10-23`
- S883 anchor — **rehearsal-only**: `the 「非凡特性来自最初造物主」 answer of 爱潜水的乌贼 — page as served 2026-10-23`
- S884 anchor — **rehearsal-only**: `the 「这个我肯定考虑过。我自己就是资深读者…」 answer of 爱潜水的乌贼 — page as served 2026-10-23`

No word counts, no locators and no fetch evidence are claimed for these strings here. The claim's ROWS leg (quote inside the anchor cell, evidence window per `EVIDENCE` leg) must be re-checked after the re-quote; this rehearsal only exercises the mechanical registry shape.

## 5 Findings — census run on the mirror

Command and full output: `A/validate-receipt-draft.txt`. Result: **exit 0**, zero `E`-codes, 3 × `W01` (tier-C mined, expected and documented by the census: warnings never change status) and 28 inherited `W04` rows that already exist at base (S127…S830), none touching S877–S884.

E03/E04/E11/E12 control (does the clean run mean anything?): a mutant copy of the mirror registry was validated in the same directory so used-by resolution is identical, then deleted.

- staged row as-is (escaped pipe, staged id, 2026-10-23) → `E01 S883 fields=12`, `E03 S883 duplicate id`, `E11 S883 missing used-by grep -c '自然環境'` … `` -> 4 (ran 2026-10-23)`` (the escaped pipe smeared the used-by cell)
- normalized row with prose recheck → `E04 … duplicate url … within scope …`, `E09 S883 recheck=180d — re-open the URL and re-locate the span`
- normalized row with a bogus used-by → `E11 S881 missing used-by corpus/knowledge/missing-control.md`
- valid row placed after `## Paths` → `E12 S890 row outside Registry section`
- mutant exit **1** vs mirror exit **0**.

So every code the assignment asks about is live in this script at this path; the clean exit is a real negative, not a dead check.

## 6 Pitfalls carried by the staged rows (named, with fix)

| pitfall | where | fix applied |
|---|---|---|
| escaped `\|` inside the recheck cell | all four staged rows | recheck replaced by `180d`; prose moved here (§3) |
| prose recheck cell (` -> 4 (ran 2026-10-23)`) | all four staged rows | same |
| staged ids colliding with lane ids S883/S884 | staged S883/S884 | renumbered to S881/S882 |
| staged-only ids S899/S900 cited as if lane rows | staged S899/S900 | renumbered to S883/S884 |
| anchor cell is a locator, not a quote (S883/S884) | staged S899/S900 | flagged rehearsal-only (§4); must be replaced by the re-quote |
| used-by naming only one entry when two cite the row | staged S877 (base entry added) | in-place used-by carries both citing entries for S877 only |

## 7 Limits of this rehearsal (honest scope)

- The claim's sequencing clause — the `validate --file` receipt must sit **strictly before the registry-append commit** — is **not exercised**: this seat may not commit, so `A/validate-receipt-draft.txt` is a draft whose commit position is a later wave's job.
- The mirror is scratch; the lane `corpus/` and the lane index are untouched (`git status` of the lane was not used to assert cleanliness — the seat wrote only under `.ufo/waves/round-74/`).
- The four row payloads are staged-derived, not page-derived: the URL/quote pairing is exactly what rounds 68/71 refused for S899/S900, so a clean census here proves registry shape, never evidentiary truth.
