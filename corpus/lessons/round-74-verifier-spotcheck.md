author: hyaku closure (non-author integrator, @m_opus)

# Round 74 — non-author closure spot-check (kotodama)

Base `f7104cbce186bc2e1522abf0cfd619cc834628bb` → lane HEAD `5c5c9d327c0102b7104cdf28aaa249224604c53f`. Driver digest (`.ufo/watchdog.log`, mutable; copied here):
`2026-10-25T20:48:59-03:00 launch kotodama round=74 pgid=510969 driver=hyaku-inline attempt=1` ·
`2026-10-26T01:03:32-03:00 complete kotodama round=74; hyaku-inline attempt=1`.
Closed 2026-10-26T04:10Z. Everything below was run by me over committed bytes or live sources; no lane gate was executed (PROTOCOL §Gate standard, Closure consequence).

## 1. Step-1 conformance

- Report `.ufo/reports/round-74/kotodama.md` committed by the lane identity: `git log --format='%an %H' -- .ufo/reports/round-74/kotodama.md` → `kotodama-shokunin 3a7401609325341eb3fe0efd42d0eec29d06be3c` (2026-10-25 23:47:02 -03, after lane commit `6ec552b3` at 23:42:02 — lands-last holds). `## SHONEN` heading present, four box lines, all `[~]` with pointers.
- Every lane hash cited in the report (`de93d91c 3595c919 00c408a0 5e4796c0 d7a38405 c4bf61a8 1d7add3f 9d4d478b 6ec552b3`, base `f7104cb`) resolves and passes `git merge-base --is-ancestor <h> main`.
- `scripts/hyaku/jj-lane.sh state …/kotodama-shokunin` → `branch=main local=5c5c9d32… remote=5c5c9d32… ahead=0 behind=0 head=detached tracked=0 untracked=0`; `git status --porcelain` → 0 lines. No uncommitted round work (the round-73 leftovers routed last closure are now committed, see Ca).
- Prompt `.ufo/prompts/kotodama-round-74.md` (committed by the lane identity in fleet `4840136b`): section headings of §1–§5 are identical to `templates/round-prompt.md` (heading diff empty); against the kotoba r74 rendering, §1–§5 differ only in lane id, axes line, census lane and report path. Round-level items (i)–(v) present in §1–§3/§5; child-lane items: report path (§4), commit-before-report and pushed-hash citation (§6 item "The report lands last and cites the pushed lane hash"), SHONEN heading (§4), hash citation (§6), write scope (§6 item 3). The run-7 route map quoted in §6 diverges from `MISSION.md` §L2 buckets (critic/sentinel/simplifier/revenger on the fast route, connector on its own alias), but MISSION states that grouping is "advisory to host routing" — not a defect.
- Defects (status-neutral, notes only):
  - D1 — the report says "Lane pushed hash: see the closing line below", and no closing line carries it; the pushed hash at filing (`6ec552b3`) appears only as "head measurements".
  - D2 — `5c5c9d32` (wrap-up, ConnectorAdjacency.md, 289 lines) and `92b8d4b8` (532-file in-flight snapshot) are orchestrator commits under the lane identity; the report names neither. The w2 dead-seat count at filing (43/44) is honest; the 44th report landed after filing.
  - D3 — §6 run-7 shape directives missed by the lane's own count (lesson `## Corrections` item 6): wave-1 attack share 24% (< 25%); strict executor/scribe/simplifier share 40.5% (< 50%).

## 2. Per-claim re-check

Re-measured = plain git/grep/wc/jq/sha256 over committed bytes, by me. Evidence-verified = committed gate output read, not re-executed.

### Claim C (coverage, assimilation-sourced) — re-measured

| measure | command | f7104cb | 5e4796c (Ca only) | c4bf61a (C lands) | 5c5c9d3 (HEAD) | reported |
|---|---|---|---|---|---|---|
| (a) setting files | `git ls-tree -r --name-only <r> corpus/knowledge \| grep -ic worldbuilding-setting` | 0 | 0 | 2 | 2 | 0 → 2 ✔ |
| (b) registry rows | `git show <r>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 804 | 804 | 808 | 808 | 804 → 808 ✔ |
| (b) rows naming litmemo/tuduku/chinawriter | same rows `\| grep -cE 'litmemo\.com\|tuduku\.space\|chinawriter\.com\.cn'` | 0 | 0 | 4 | 4 | 0 → 4 ✔ |
| (c) CJK term files | `git grep -lE '設定ノート\|世界観\|世界观' <r> -- corpus/knowledge \| wc -l` | 0 | 0 | 2 | 2 | 0 → 2 ✔ |
| (d) knowledge `.md` | `git ls-tree -r --name-only <r> corpus/knowledge \| grep -c '\.md$'` | 247 | 247 | 249 | 249 | 247 → 249 ✔ |

- Both entries open with `source:` lines citing S877/S881/S882 (base) and S883/S884 (amendment), then `verified-at: 2026-10-25`, `recheck: 180d — …`. S881–S884 are `mined`, `opened 2026-10-25`, `used-by` = the two entries (`awk -F'|'` over the rows).
- S877 change: `git diff f7104cb 5c5c9d3 --word-diff=porcelain -- corpus/SOURCES.md` shows one in-place change, the `used-by` cell (`…/conlang-scholarship.md` → `…/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`). That cell is allowed to change in place (SOURCES contract rule 2).
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, last line `kotodama ok …/corpus/SOURCES.md`; W01 ×3 (S881, S882, S884 tier-C mined) and the standing W04 duplicate-URL warnings.
- Gate evidence-verified: `telemetry/measures-c.txt` stamps lands `c4bf61a8…`, freeze `00c408a0…`, counter self-sha256 `8d30487f…`, which equals `sha256sum reports/round-74/accept-c.py`; the counter blob is identical at freeze and HEAD (`458820e9…`); `ACCEPT-C-74: PASS legs=13/13`; `measures-c-head.txt` PASS 13/13 at `9d4d478b`; `selftest-c.txt` `SELFTEST: 69/69 scenarios`; `controls-c.txt` do-nothing FAIL 4/13 and base-refused 0/13.
- Separability: Ca's landing (`git diff --name-only 00c408a 5e4796c`) touches only SCORECARD/SKILL/QUALITY/controls; `grep -n 'SCORECARD\|SKILL\.md\|ledger' accept-c.py` finds no read of those paths. C does not depend on Ca [INFERENCE from the read paths; C was never measured on a Ca-free tree].
- **Verdict: verifies.**

### Claim Ca (calibration, records) — re-measured

| item | command | observed | agrees |
|---|---|---|---|
| 12 ANNOTATE rows | `git show 5c5c9d3:SCORECARD.md \| sed -n '/^## Corrections — round 74/,/^## Axes — round 74/p' \| grep -cE '^\| LC-[0-9]+'` | 12 (LC-01…03, 06–08, 11, 12, 15–18) | ✔ |
| LC-09 REPAIR `SKILL.md:594` | `git show <r>:SKILL.md \| sed -n 594p` at f7104cb / 5e4796c / HEAD; `git ls-tree … corpus/knowledge/civilizations \| grep -c '\.md$'` | `94 entries` → `95 entries` → `95 entries`; 95 files | ✔ |
| LC-01 re-derivation | `git grep -c -E '^. S[0-9]{3}' f7104cb -- corpus/SOURCES.md`; `SHONEN.md:6` | 804; SHONEN still says "412 rows after round 56" (ANNOTATE, not repaired) | ✔ |
| LC-06 / LC-08 | `git diff --shortstat 4b825dc… f7104cb -- 'corpus/knowledge/*/*.md'` and `…/linguistics/*.md`; README `:732`, `:344` | 247 files vs `Total knowledge entries: 243.`; 32 files vs `30` | ✔ |
| six round-73 w2 files tracked | `git rev-parse <r>:<path>` at f7104cb / 00c408a / 5e4796c / HEAD | five tracked files changed blob at the freeze (worktree bytes committed), then identical at freeze, Ca lands and HEAD; `RevengerOrigins.md` absent at base, `2c1c9cd8…` after | ✔ |
| ledger sha256 pins | `git show 5c5c9d3:<path> \| sha256sum` vs `jq .must_track` | 6/6 equal (`290a6ccd…`, `dfc8fe0d…`, `db254d88…`, `9469d4d6…`, `079728a5…`, `7d145919…`) | ✔ |
| round-73 PASS receipts | `git grep -c -E '^ACCEPT-(C\|CA)-73: PASS' f7104cb -- reports/round-73/telemetry` → none; `grep '^ACCEPT' telemetry/accept-c*-73-at-lands.txt` | base 0 lines → `ACCEPT-C-73: PASS legs=11/11`, `ACCEPT-CA-73: PASS legs=9/9` at stamped `2d1cd9140d3a` | ✔ |

- Gate evidence-verified: `measures-ca.txt` stamped=evaluated=measured `5e4796c0cb6a`, counter `8052f1e25c36` = `sha256sum accept-ca.py`, blob unchanged freeze→HEAD (`bb69fb04…`), `ACCEPT-CA-74: PASS legs=11/11`; `selftest-ca.txt` `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0`; `controls-ca.txt` do-nothing FAIL 7/11, base-refused 0/11.
- **Combined-tree red, ruled.** `measures-ca-head.txt` (at `9d4d478b`) prints `FAIL legs=10/11`. The only failing leg is APPENDONLY, and its only problem is `corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]`, i.e. claim C's S877 `used-by` edit. SOURCES contract rule 2 permits that edit, and the other ten legs pass at the combined tree. Ca was frozen as measured at its own `<lands>` and passes there. AXES requires each claim to verify without the others having landed, so measuring Ca at `5e4796c` is the correct test, and the substance re-measured above still holds at HEAD. Ruling: **Ca verifies**. APPENDONLY over-protects a contract-permitted cell, and that is a counter-scope defect, routed (R1 below), not a harm.

### Axis integrity

`git diff f7104cb 5c5c9d3 -- SCORECARD.md`: +32/−0 (two appended sections). Outside `.ufo/` and `reports/`, deletions are `SKILL.md` 2 (the `:594` repair and the wave-2 sha256-pin repair in the lane's own registry row) and `corpus/SOURCES.md` 1 (the S877 `used-by` cell). LOG, QUALITY and README are append-only (+17, +46, +45). No existing knowledge entry was modified.

| axis | verdict | reason |
|---|---|---|
| coverage | improved | claim C re-measured: 0→2 entries on new ground, 804→808 rows, 0→4 host rows |
| calibration | improved | claim Ca re-measured: 12 annotations + 1 repair, 6/6 pins tracked, round-73 receipts committed |
| depth | unchanged | no existing entry deepened |
| operability | unchanged | SKILL.md additions are gate-registry rows; no checklist/table changed |
| freshness | unchanged | paused under the open L0 round-11 row (`.ufo/l0-questions.md:47`) |
| adjacency | unchanged | no cross-lane writes in the lane diff; sibling scans are lane-internal |

No axis harmed. No exploratory claim.

## 3. Discernment spot-check (LEARNING.md)

Sample from `corpus/lessons/round-74.md` `## Gate`. I re-opened every source with a plain `curl -sL` (browser-shaped UA, no automation) on 2026-10-26.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S881 LitMemo | admit (C) | `https://litmemo.com/ja/blog/novel-worldbuilding-guide` → 200, 101615 B, sha256 `441fc921…` (= recorded) | agree | quote 「自然環境が社会の仕組みを決め、…価値観を作る。」 present verbatim, 52 chars after h3 「3. 外側の層へ因果をつなぐ」 as located; tier C used as method evidence only |
| S883 chinawriter 2025 | admit (B, narrow scope) | `…/n1/2025/0605/c404024-40494534.html` → 200, 48536 B, sha256 `a3b6640c…` (= recorded) | agree | both row quotes (「整个过程里，我先做的是世界观…」, 「既然万事万物都从最初造物主而来…」) are in `p` #68 under `div.end_article`, as the locator says; the scope is testimony about his own process |
| S884 chinawriter 2022 | admit (C) | `…/n1/2022/1207/c404024-32582252.html` → 200, 62604 B, sha256 `344de345…` (= recorded) | agree | 「把它放在前面大概20章之内慢慢来，我觉得是问题不大的。」 present; the hedge is kept in `teaches` |
| S877 Sidorova/Shuvalova | admit (B; reused row) | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` → 200, 1055723 B, sha256 `e512a20d…` (= recorded) | agree | `pdftotext -f 7 -l 7` finds «Язык – главный инструмент построения вымышленных миров»; the scope-cell caveat (wave-2) stands, routed by the lane |
| staged S882 (same PDF) | reject (not appended) | same PDF; staged URL = S877 URL | agree | appending would register one document twice; the in-place `used-by` change is the right move |
| staged S895 (王昕玥, 《龙族》) | reject (dropped) | `…/n1/2025/1030/c404027-40592897.html` → 200, 45262 B; 「世界观的预设缺陷」 and 叙事驱动机制 present | agree (as deferral) | the source is live and its section exists. The reject is a scope deferral (no lane row, not re-quoted this round) and claims nothing false about the source |
| staged S899 (2025 page) | reject ("quoted span absent from the page it was bound to") | 2025 page above: 非凡特性来自最初造物主 1 hit, 先做的是世界观 1 hit; 这个我肯定考虑过 0 hits | **disagree** | the staged S899 row's anchor (「非凡特性来自最初造物主」答问) and its recheck span are both on its own page. The mispairing belongs to register S816 (census-adjudication S758), as the lesson's own R74-M5 says. The Gate row puts the register defect on the staged row |
| staged S900 (2022 page) | reject ("quoted span was the Sowers-Wills clause") | 2022 page above: 这个我肯定考虑过 1 hit, 20章之内慢慢来 1 hit, `Sowers` 0 | **disagree** | the staged S900 row's anchor (「这个我肯定考虑过。我自己就是资深读者…」) is on its own page, and the Sowers-Wills span is register S817's. In substance S899/S900 were adopted under new ids (lesson map: S899→S883, S900→S884, "append, re-quoted"), so two of the four "probed rejects" are not rejects |

New-row quote check: S883's `anchor` cell quotes are 32 and 40 characters, located (P68) and found verbatim. S881/S882/S884 Gate quotes are found on the live bytes (S882 after tag-stripping). All are under 25 tokens.

Result: 6 of 8 sampled decisions agree, including all four admits and both rejects whose reasons hold. 2 disagree: the reasons for the two staged-row rejects are false as written, though the outcome (re-quote as new rows) is sound.

## 4. Trend verdicts

- **expansion: improved.** Two admitted entries on ground absent at base (0 → 2 files, 0 → 2 CJK-term files), citing mined rows S877/S881–S884, all re-opened above. The lane's caveats stand: base + amendment is one ground, and S877 is cited partly outside its scope cell. The practitioner content is framed as "what the pages prescribe", so the tier-C rows are not sole support for a claim about the world.
- **quality: unchanged.** No pre-existing entry was re-verified, deepened or superseded. Wave-2 found false sentences in this round's own entries and repaired and marked them in the committed head (lesson `## Corrections`), so not harmed.
- **discernment: unchanged.** The outside check agrees on every admit. It disagrees on the reasons for two rejects, so `improved` is not earned. This is the first time the disagreement is recorded, so it is not yet "left unlearned"; it is routed below (R2). QUALITY 26 is lane-authored and cites a lesson.

## 5. Routed defects (lane must fix next round)

1. R1 — `accept-ca.py` APPENDONLY treats a contract-permitted SOURCES `used-by` edit as a violation. Next counter generation: exempt rule-2 cells (`status`/`recheck`/`used-by`), or name the sibling claim's in-place lines in its frozen exemptions, so a combined tree can be green.
2. R2 — `corpus/lessons/round-74.md` `## Gate` reject rows for staged S899/S900 give false reasons: the staged anchors are present on their pages, and the mispairing is register S816/S817. Append a correction in round 75 that reclassifies them as adopt-with-renumber, not rejects. Add or extend a QUALITY criterion: a reject reason names the artifact it was observed on (staged row vs register row).
3. R3 — The report's dangling "see the closing line below" pushed-hash pointer (D1). Future reports cite the pushed lane hash inline.
4. R4 — The carried-over items the lane routed itself stay open: S877 scope cell (superseding row), the `SHONEN.md:6` "412 rows" REPAIR, README index 245 vs 247, `sweep.py` first-footer read, the junk receipts post-dating the freeze, `accept-c.py` passing at `--lands == --freeze`.

## 6. Operator note (promotion is operator-owned)

All four SHONEN boxes remain `[~]`. Box 2 (end-to-end task) and box 3 (executable without oral context) were in effect exercised by this closure: sources re-opened from the committed pointers, and counts re-derived from committed commands with no oral context. Boxes 1 and 4 need a dedicated non-author read of `SKILL.md` and `PROVINCE.md`, which this closure did not do. I write no `[x]`.
