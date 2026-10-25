# Round 72 — verifier spot-check (hyaku closure)

author: hyaku closure (non-author integrator, @m_kfc)
date: 2026-10-25
lane-round: kotodama 72 · base `b60c7b1` · graded HEAD `3adbd4ab` (= origin/main, ahead=0 behind=0)

## Step-1 conformance

| check | command | observed | verdict |
|---|---|---|---|
| report authored by lane identity | `git log --format='%an %ae %H' -- .ufo/reports/round-72/kotodama.md` (fleet) | 7 commits, all `kotodama-shokunin <kotodama@shokunin.local>`: a151ec38 (report) + 406c4e9e, da70b66f, 6efd7f4e, e7cdde73, a62f700e, 80d8c9b5 (six errata) | pass |
| SHONEN heading, one line per box | read | `## SHONEN` with 4 `[~]` lines, each with pointer | pass (author assertions; see operator note) |
| cited commits exist + ancestor of branch | `git cat-file -e` + `git merge-base --is-ancestor <h> refs/heads/main` for 21 cited hashes | all ok; `f47ad6ba` is a *fleet* commit (exists there: protocol-shokunin tree-restore); `f0a4e98` was a provisional name corrected to `82e9e680` by erratum-2's own correction line | pass |
| lane pushed, no round work uncommitted | `scripts/hyaku/jj-lane.sh state` | ahead=0 behind=0; **but** 2 untracked files: `.ufo/waves/round-72/w1/ScoutMergeScan.md`, `ScribeLesson.md` | defect R1 |
| prompt carries template contract | grep `.ufo/prompts/kotodama-round-72.md` (committed a02268ca, lane identity) | SHONEN-heading rule, report-lands-last + hash citation, write scope present | pass |
| errata append-only | `git log --numstat` + hunk positions for all 7 report commits | 61 additions / 0 deletions; every erratum hunk EOF-positioned (lines 48→58 of 59) | pass |
| report real, not marker | read | work performed, evidence pointers, per-commit landed list, hash citations, trend verdicts, Sources & frontier | pass |

## Claim re-checks

**Ca — calibration (K71-1..K71-8 append-only corrections). Re-measured independently of the lane gate:**

- QUALITY criteria: `git show b60c7b1:corpus/QUALITY.md | grep -c '^20\. '` = 0, `^21\. ` = 0 → `git grep -c` at HEAD = 1 each. ✔
- w2 files: at HEAD `CritTrends/Filler28/Filler36/RevCounterCa/RevEntry/Filler30/RevReceipts.md` all tracked (7/7); the lane's base control receipt lists the same 5 as missing at base. ✔
- Append-only: `git diff --numstat b60c7b1..3adbd4a` — LOG.md 14/0; corpus/lessons/round-71.md 15/0; corpus/QUALITY.md 4/0; fleet report 61/0. Whole-tree deletions confined to the two *modified* w2 wave working files (Filler30, RevReceipts), outside the filed set. ✔
- MAPCORR: `corpus/lessons/round-71.md` `## Corrections (round 72)` names 65ff151 (784 rows/2 collisions/S861) → 99e3d63 (797/15/S874). ✔
- CASTAMP: `reports/round-71/telemetry/measures-ca-restamp-64da9e14.txt` appended (1417 B), names `1ce25fb9@64da9e14 → f706aacd@64da9e14`, prior bytes unchanged. ✔
- QUAL21: criterion 21 committed; text requires a canonical-slug CDX probe + probed-URL filing per Gate reject. ✔
- CAPOEIRA: correction names `capoeira-circle-00892` and earliest capture `20170513162348`; LOG round-72 entry names both. CDX corroboration probed by me for the S874 row's captures; the Capoeira CDX counts are lane evidence, committed. ✔ (evidence-verified, not re-executed)
- NOHARM: census `validate kotodama` exit 0 run by me; SCORECARD diff appends the round-72 section only — no owned axis row harmed. ✔
- Gate evidence: `reports/round-72/telemetry/measures-ca.txt` is stamped at 21ad3088 and reads `ACCEPT-CA-72: FAIL` with REPORTCORR/REPORTLAST failing (structural: the fleet report had not landed). The report claims both legs PASS on a post-report rerun — **no committed rerun receipt exists** (tree+history searched). Defect R2. Claim substance (8/8 defects landed, all before→after numbers) re-measured above; the missing receipt does not falsify the axis-move but leaves the gate's final verdict unevidenced and the SCORECARD row ("12/12 PASS") overstated against the committed receipt.
- **Axis verdict: calibration improved (re-measured).**

**C — coverage (first shokuknow adoption, rows S874/S875 by document). Re-measured + gate evidence:**

- heritage-taxonomy files: 0 at base (`git ls-tree`) → 2 at HEAD (`heritage-taxonomy-models.md` + `.amend-2026-10-24-r13.md`). ✔
- registry rows: 797 → 799 (`grep -cE '^\| *S[0-9]+'`); S874/S875 rows present, mined, used-by = the two admitted entries. ✔
- staged re-point by document: entries cite only S874/S875 (no S863/S867/S967 anywhere in the entries); `reg-to-staged.txt` + ScoutRegisterMap erratum (map verified 21/21, two +82 rows prove document-derived) corroborate. ✔
- gap sweep receipt: 0 ihchina/bunka matches at base. ✔
- Gate evidence: `measures-c.txt` reads `ACCEPT-C-72: PASS legs=10/10` at 21ad3088 (committed); `controls-c.txt` FAIL at base; `--selftest` mode exists in the counter. Evidence-verified, not executed (closure consequence). ✔
- refuses: both staged entries refused with reason+flip; my reject re-open below agrees.
- **Axis verdict: coverage improved.**

**Other owned axes (depth / quality / operability / freshness / adjacency): unchanged** — no existing entry re-verified or deepened; no SCORECARD row harmed; the amendment co-admitted with its base is one admission event, not a deepening. SCORECARD + connector seat record the heritage-taxonomy surface in-lane and uncontested.

## Discernment spot-check (LEARNING.md — non-author, sources re-opened live 2026-10-25)

| item | gate decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S874 (ihchina 国家级名录 清单页) | admit | `https://www.ihchina.cn/project.html` live, browser UA | **agree** | HTTP 200 (43255 B); quote 「国家级名录将非物质文化遗产分为十大门类」 present verbatim; 十大门类 enumeration matches the entry's claims; CDX shows captures back to 2019 incl. 20200216023423 |
| S875 (bunka 文化財検索) | admit | `https://online.bunka.go.jp/db/heritages/search` live | **agree** | HTTP 200, **231736 B exactly as the report states**; 「安土・桃山」 present in the 時代 select |
| S870 (chinawriter, staged narrative-structure entry) | reject (quote absent) | `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` live | **agree** | HTTP 200, 45238 B (matches the seat's fetch byte-for-byte), title 我是怎样创作网络小说的; staged quoted span 「作品中的人物名字和地名」 **0 hits** — fabrication-class reject stands; the flip (re-opened source carrying the span) is the correct remedy |
| SOURCES.md S874/S875 quote length (≤25 words) | new rows | registry rows + census W04 | **agree** | `sources-census.sh validate kotodama` exit 0; no W04 quote-length findings on S874/S875 |

Note: the 20261020183948id_ capture fetch answered HTTP 200 but served 10370 B without the quote span (redirect/shell page) — the amendment's capture-specific readings (四批→五批) rest on lane-committed evidence; live evidence alone carries both admits.

## Trend verdicts

- **expansion: improved** — two entries on ground my re-measurement confirms uncovered (gap sweep 0 matches at base; 0 heritage files), each citing a mined row admitted this round.
- **quality: unchanged** — agreed; nothing re-verified/deepened, nothing found false and left unmarked.
- **discernment: improved** — QUALITY criterion 21 committed, grounded in the falsified K71-8 Capoeira reject (composed URL never reconciled with the canonical slug); my outside spot-check agrees with both admits and the sampled reject, so the disagreement became a grounded criterion.

## Routed defects (lane must fix next round)

- **R1** Commit or disposition the two untracked wave-1 seat reports (`.ufo/waves/round-72/w1/ScoutMergeScan.md`, `ScribeLesson.md`); their findings landed via errata/LOG, the files did not.
- **R2** Commit the ACCEPT-CA-72 post-report rerun receipt (REPORTCORR+REPORTLAST PASS at the measured revision) or append a correction; the SCORECARD round-72 calibration row asserts "12/12 PASS" against a receipt that reads FAIL.
- **R3** `SKILL.md` §Gates and probes registry stops at accept-\*-69 — no rows for accept-ca-70..72 / accept-c-70..72; add round-72 rows (and backfill or explain 70/71).
- **R4 (carried, lane already self-routed to r73 in errata 1–5):** stale round-71 id-renumber-map.json (regenerate from S876 before further staged rows land); staged S934/S936 fabrication-class rows + companion re-verification; S869 correction-chain re-verification; shokuknow SOURCES-PROPOSED.md Gate headings off-by-one; per-citation by-document check for staged era amendments; check-gate-quotes pipe-row blind spot.

## Operator note

All four SHONEN boxes present as `[~]` with resolvable pointers and are fully checkable by a non-author (this closure re-derived box 1 controls, box 2 end-to-end adoption, box 3 append-only discipline, box 4 trend verdicts). Promotion is operator-owned; no `[x]` was written.
