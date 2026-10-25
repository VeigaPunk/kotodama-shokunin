# ExecRenumber — round-72 w1 report (leaf seat L1Kotodama72.ExecRenumber)

Date: 2026-10-25. Assignment: re-point the two staged heritage-taxonomy entries' citations by
document (no arithmetic id shift), fix foreign references, re-run the canonical's gap sweep at
HEAD, rewrite its recheck field from the normalized rows, and verify every staged body claim
against the round-72 re-open evidence (/tmp/ihchina-2020.html, /tmp/ihchina-2026.html,
/tmp/bunka.html — all three present; no scout ask needed).

## Files produced
- /tmp/r72-entries/heritage-taxonomy-models.md (re-pointed canonical draft)
- /tmp/r72-entries/heritage-taxonomy-models.amend-2026-10-24-r13.md (re-pointed amendment draft)

No lane or fleet files were written; the drafts live only under /tmp/r72-entries/. No tools were
installed (built-ins only; pacman untouched).

## Re-point mapping (by document)
- S863 → **S874** (ihchina register page). Canonical source line now cites S874 with the row's
  parameterless URL https://www.ihchina.cn/project.html (the staged `?tid=4` view was dropped:
  the normalized row flags it as intermittently truncating for plain clients and declares the
  parameterless URL the stable one).
- S867 → **S875** (bunka search page). Canonical source line cites S875.
- S967 (capture) → **S874** with the capture timestamp named in text: the amendment's source line
  and body ("From S967:" → "From S874:") name the Internet Archive's 2020-02-16 capture of the
  ihchina register page. The body's timestamp "2020-02-16" is retained.

## Foreign-reference fixes
- Amendment's "the lane's row S837" (both in `gap filled` and §N+1) → "the ihchina live page".
  Confirmed in our lane S837 is BBC Sikhism ("BBC Religions, Sikhism: The Five Ks", round-69
  guard-proof reg-no-s002.md row 791), so the staged reference pointed at the campaign mirror's
  row; the document is named instead.
- Amendment couples line `culture-material/calendar-festival-systems.amend-2026-10-24-r10.md` →
  `culture-material/calendar-festival-systems.md` (exists at
  corpus/knowledge/culture-material/calendar-festival-systems.md).
- Canonical couples line `myth-symbol/calendar-festival-systems.md` → `culture-material/calendar-festival-systems.md`
  (the myth-symbol path does not exist in our lane — the file lives under culture-material/;
  same document family as the amendment's re-point target). Both couples files checked to exist.

## Gap sweep (re-run at HEAD) and registry count
- HEAD = b60c7b140c5350caa7d1073711f14092541533f0 (matches claims base).
- `grep -inE 'ihchina|非物质|非物質|文化遺産|heritage online|bunka'` over corpus/SOURCES.md at HEAD
  returns **0 matches** (real number recorded). Registry rows counted: **797** (matches claim C's
  "registry is 797 rows").
- Canonical `gap filled` updated: "over the 643-row registry" → "over the 797-row registry at HEAD
  (b60c7b1)", result 0.

## Recheck field rewrite (canonical)
Replaced the campaign `SOURCES-PROPOSED.md` reference with the two normalized row commands:
- S874 (180d): `curl -fsSL 'https://www.ihchina.cn/project.html' | grep -c '编号中的罗马数字代表所属门类'` → 1
- S875 (90d): `curl -fsSL 'https://online.bunka.go.jp/db/heritages/search' | grep -c '安土・桃山'` → 3
including each row's parenthetical (parameterless URL stable; ladder repeats across option groups).
The amendment's recheck was already the real command and is retained.

## Body claims verified against re-open evidence (kept)
- Capture (ihchina-2020.html): 国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录 ×1
  (verbatim), 国家级名录将非物质文化遗产分为十大门类 ×1, 编号中的罗马数字代表所属门类 ×1, no "2021" (×0);
  amendment recheck string 公布了四批国家级项目名录 ×1. → four-batch + taxonomy/code claims verified.
- Live (ihchina-2026.html): 五批国家级项目名录 ×1 with wording "2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录"
  (fifth = 2021 batch), 十大门类 ×1, code rule ×1, 扩展项目 ×3. → five-batch claim verified.
- bunka.html: 安土・桃山 ×3 (row recheck expects 3), 材質・構造・技法 ×14, サイズ ×7, 所在地 ×12,
  指定区分 ×1, 時代 ×12, 分野 ×1, 朝鮮半島 ×15, plus outline items 絵画 ×3, 版画 ×7, 彫刻 ×3, 工芸 ×9,
  考古 ×6, 歴史 ×9, 民俗 ×13. → Japan taxonomy/fields claims verified.

## Body claims marked [UNVERIFIED-CLAIM:] (L1 to cut or source)
1. Amendment ground: round 12's CANNOT-ANSWER §4.3 holding the register unreachable with nil Archive
   coverage — no such section exists in our lane's round-12 artifacts (searched corpus/lessons/round-12.md,
   reports/round-12/*; grep for CANNOT-ANSWER/ihchina/4.3 found nothing).
2. Amendment `gap filled`: "round 12 recorded the register's ten categories … from a single reading
   of the live page" — not recorded in our lane's round-11/12 artifacts (the staged S837 belongs to
   the campaign mirror).
3. Amendment §N+1: "the live page answered neither round 11's probe nor round 12's gate, and round
   11's CDX query for it returned nothing that was re-checkable" — no ihchina gate record in our
   lane's round-11/12 artifacts; outside the round-72 re-open evidence.
4. Amendment §N+1: "it is a fast, stable host" — operational claim, not verifiable from static captures.

All other staged body claims are kept and verified as above.

## Risks / blockers
- No blockers. Evidence files were present at /tmp (also mirrored in /tmp/r72-entries/); drafts
  written; the three unverifiable historical claims are flagged for the L1.
- Note: canonical recheck cadence now reflects the rows (S874 180d / S875 90d); the staged draft's
  single "180d" covered both, which was not faithful to the normalized rows.
