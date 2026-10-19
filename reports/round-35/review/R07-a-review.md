- Seat: R07 | reviewer | claim A | date 2026-10-19 | baseline 4a7aede

# R07 — second A pass: completeness review of the PROVINCE re-verification

**Mission** (`reports/round-35/targets.json`, seat R07): "Second A pass: the
PROVINCE re-verification's completeness." Out: `reports/round-35/review/R07-a-review.md`.

**Dependency state at write time.** `adj/A06-province.md` landed (snapshot
`2026-10-19T08:17:02Z`); `adj/A11-verify-2.md` landed but ran **before** A06
existed (`A11-verify-2.md:6-8`) and left the A06-vs-A11 reconciliation owed
(`A11-verify-2.md:321-326`). This fragment performs that reconciliation (§4)
and reviews A06's completeness against an explicit criterion set (§1–§3).
`scout/K04-touched-census.md` is still absent; R06 filed the same owed path
(`review/R06-a-review.md:182-187`) and supplied the independent diff census
(`R06-a-review.md:36-51`). All my commands are read-only, lane root, HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; my only write is this fragment.

## 1. Completeness criteria for a PROVINCE re-verification (C1–C6)

Derived from PROVINCE's four claim blocks (`PROVINCE.md:9-11` owns, `:16-20`
refuses, `:22-25` adjacent contract, `:27-29` write scope), the r33-A01
precedent check set (`reports/round-33/adj/A01-province.md:1-198`, checks
A01-1…A01-5), and the A-claim's `after_required` (`reports/round-35/claims.json:60`):

- **C1** PROVINCE byte-stability at the new baseline (blob identity + empty diff
  since last touch + live digest/line count).
- **C2** owns-list resolution: every named partition/path live, **plus** the
  negative (no partition exists that the list does not name).
- **C3** refuses-list resolution: sibling lanes exist with matching provinces,
  and no in-lane surface decides a refused matter.
- **C4** adjacent-contract anchor: `PROVINCE.md:24`'s cited contract file
  resolves at HEAD, and its digest is the one the newest handoff artifact pins.
- **C5** write-scope statement vs observed surfaces (fleet round report, L0 rows).
- **C6** every r33/r34-touched live surface placed on an owns/write-scope line —
  the claim's `after_required` names three surfaces (new tool, r7 packet,
  repointed renderer) but its before-list enumerates more
  (`claims.json:56`): packet+claims-map+repin, tool+inventory, examples
  repoints, SKILL/AGENTS/ceilings, box-1/reissue records.

## 2. My independent re-run (second pass at HEAD)

| # | probe | command / result | criterion |
|---|---|---|---|
| M1 | blob identity | `git rev-parse HEAD:PROVINCE.md` and `c53782a:PROVINCE.md` → both `313b182f251564b7997b06996b4f063370778f11`; `git diff c53782a HEAD -- PROVINCE.md` → empty (exit 0); `git rev-list --count c53782a..HEAD` → 81 | C1 PASS |
| M2 | live bytes | `sha256sum PROVINCE.md` → `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`; `wc -c -l` → 31 lines / 1636 bytes | C1 PASS |
| M3 | partitions | `for p in …; do ls corpus/knowledge/$p/*.md \| wc -l; done` → 21/19/18/29/20/94; `ls corpus/knowledge/*/*.md \| wc -l` → 201; exactly six partition dirs | C2 PASS |
| M4 | refuses probes (r33-A01-3's whole-tree pair, not restated by A06) | `git ls-files \| grep -cE '\.(html\|css\|js)$'` → 0; `git ls-files \| grep -ciE 'game\|rpg\|mechanic'` → 0 | C3 PASS |
| M5 | contract anchor | `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bf…`; last move `e1694ba` (round 8, untouched by r33/r34); the r7 packet pins the same digest (`declared-in-r7/packet.md:14`) | C4 PASS |
| M6 | r33 worktree-digest continuity (not checked by A06 or A11) | `git show HEAD:<p> \| sha256sum` equals the r33 audit's recorded worktree digests: `SKILL.md` `f9bd07c2…` (`audit-assembled.md` §Fresh checks), `AGENTS.md` `5ae7a9c8…`, `corpus/lessons/README.md` `f752e1d7…`, contract `5f4c02bf…` — all four equal, so the r33 verdicts apply to committed bytes | C6 PASS (4 surfaces) |
| M7 | post-edit ceilings bytes | `git show HEAD:…/register-lexicon-ceilings.md \| sha256sum` → `afe8bf22…`, 317 lines; `git show 139e3b6:…` → `bb579d51…`, 289 lines; `git show --numstat da68a6d -- …` → +28/−0 | C6 finding R07-F2 |
| M8 | examples r33 repoint targets | HEAD digests: `culture-d3/README.md` `946053ee…`, `culture-d3/handoff.md` `c4fabccb…`, `handoff-packet.sample.md` `adfd7895…`, `handoff-packet.sample.yml` `751be044…` (each r33 numstat 1-2 lines) | C6 finding R07-F2 |
| M9 | fleet / L0 | `.ufo/reports/round-33/` and `round-34/` both contain `kotodama.md`; `.ufo/l0-questions.md` still exactly 4 kotodama rows, lines 44-47 (rounds 2, 8, 9, 11) | C5 PASS |
| M10 | language scan on r34 artifacts | every `canon/clearance/promot` hit is a negation or routing: `claims-map.md:22,60,162,172`; `repin.json:5,53` | C3 PASS |

## 3. A06's coverage against C1–C6

| criterion | A06 coverage | my verdict on completeness |
|---|---|---|
| C1 | A06-1 (`A06-province.md:20-32`): blob `313b182f…`, empty diff, 31/1636 | **complete**; M1/M2 reproduce |
| C2 | A06-2 (`:34-48`): partitions + gates + source records + examples + reports + caveat | **complete in substance**; A06's "exactly those six" (`:42`) establishes the negative implicitly, A11 states it explicitly (`:40-42`); probe width note R07-F4 |
| C3 | A06-4 (`:126-152`): all six siblings + roster rows + "no in-lane artifact decides a refused matter" | **complete**; my M4 restores the two r33 whole-tree probes A06 dropped, both 0 |
| C4 | not run as a separate check | **gap in A06**; closed by M5 (anchor live, digest pinned identically by the r7 packet) |
| C5 | A06-5 (`:154-167`): fleet r34 report present, 4 L0 rows | **complete**; M9 reproduces |
| C6 | A06-3 (`:50-124`): the three surfaces named by `claims.json:60` | **partial** — see R07-F2/F4; the claim's before-list has more surfaces, and the lessons-README/REGIMEN mapping exists only in A09's receipt table (`A09-receipt.md:51,61`), which A08 must carry |

No A06 verdict is contradicted by my re-run or by A11.

## 4. A06 ↔ A11 reconciliation (the owed item, performed)

| value | A06 | A11 | my re-run | agree |
|---|---|---|---|---|
| PROVINCE blob / last touch | `313b182f…`; `c53782a` (`A06-province.md:24-27`) | only `c53782a`/`a527120` (`A11-verify-2.md:99-100`) | M1 | **yes** |
| partition census | 201 (21/19/18/29/20/94) (`A06:43`) | 201 (`A11:30-38`) | M3 | **yes** |
| packet/twin/claims-map/expected digests | `45f57132…`/`0e229138…`/`d181de28…`/`bbe15887…` (`A06:95-99`) | same five incl. `freeze.txt` `3969954b…` (`A11:136-140`) | spot M5/C4; `sha256sum` of the dir matches | **yes** |
| new-tool digest | `5858abcd…` (`A06:56`) | — | `sha256sum` → `5858abcd…` | **yes** |
| renderer digest | `34c85f57…` (`A06:114`) | `34c85f57…` (`A11:151`) | `sha256sum` → `34c85f57…` | **yes** |
| r6-row refusal mechanism | quoted (`A06:106-119`) | reproduced, `KeyError` at `tools/exercise-handoff-e2e.py:3822` (`A11:170-193`) | not re-run by me (O-claim leg) | **yes** |

A11 strengthens the joint result twice: the **negative owns check** ("no
knowledge partition exists that the owns list does not name", `A11:40-42` —
A06 states this only implicitly via "exactly those six", `A06:42`) and **A11-F1** (filed `reports/round-34/op/adoption-inventory.json`
says 28 runners/17 guarded-refresh; live census 29/18, `A11:241-283`). A06 and
A11 do not disagree anywhere they overlap.

## 5. Findings (with owners)

- **R07-F1 — A06 citation errata, precision only.** `A06-province.md:133-134`
  cites `lore-shokunin/PROVINCE.md:10` for the Refuses line; it is at **:9**
  (`grep -n "Refuses" lore-shokunin/PROVINCE.md` → `9:`). `A06:136` cites the
  chousa mint note at `MANIFEST.json:2312`; the note is at **:2314** (`:2312` is
  the `"chousa"` array element). Both verdicts unchanged. Owner: integrator/A08
  to carry the corrected pointers. (Same defect class as r33-A11's D1/D1b/D3
  against r33-A01, `reports/round-33/adj/audit-assembled.md` §findings.)
- **R07-F2 — continuity pin owed for post-edit corpus/example bytes.** The r33
  audit's ceilings reading (`bb579d51…`, 289 lines, `A07-history.md:76,112`;
  `A10-receipt.md:78`) is the **pre-edit** (`139e3b6`) reading; HEAD is
  `afe8bf22…`, 317 lines (M7). A05 audits the post-edit §12
  (`A05-records.md:46,222`, citing `:291-317`) but no durable digest pin for the
  post-edit bytes exists in r35, and the four r33 example repoint targets (M8)
  are pinned nowhere. Owner: integrator — add the M7/M8 digests as a pin row or
  in A08's table so a later drift is detectable. Also: no r35 text should
  restate `bb579d51…` as current.
- **R07-F3 — frozen packet misdescribes its own claims-map source (named
  finding, unfiled by A06 and A11).** `declared-in-r7/packet.md:3` says "the
  twelve D4 rows are carried from `reports/round-20/handoff/claims-map.md`",
  while the same file's manifest row A-57 (`:95`), §reads (`:113`) and §claims
  (`:125`) name `reports/round-34/handoff/declared-in-r7/claims-map.md`. The two
  files are different revisions (`sha256sum`: r20 `4b1b9a35…`, 275 lines; r34
  `d181de28…`, 259 lines). Root cause: the hard-coded literal at
  `tools/exercise-handoff-e2e.py:2700` was not repointed by `4a7aede`, which
  moved `:184`, `:1933-1934` and the manifest label `:2566`. Owner:
  renderer/packet owner (r34 D-block) — remedy is a new packet revision or a
  named-errata row, never an in-place edit; re-freeze is a round-35 non-goal
  (`claims.json:70`). A01's slice is the natural filer; A08 must carry it.
- **R07-F4 — owns-list probe width (note).** A06-2's "own gates" probe is
  `ls tools/gates/` (`A06:44`, unchanged from r33-A01-2), while the r34 surface
  lives in `tools/harness/`; A11-N1 already files the wording ambiguity
  (`A11:303`). My independent position: substance green, wording optional,
  integrator/operator-owned. Root governance files (REGIMEN.md, LOG.md,
  SCORECARD.md) are mapped by A09 rows 12-14 (`A09-receipt.md:59-61`) onto
  `PROVINCE.md:27-29` / `REGIMEN.md:44-46`; A06 alone is not that mapping.
- **Closed by the A-block receipt:** R06-F1's "unfiled" complaint about
  `corpus/lessons/README.md` (`R06-a-review.md:62-83`) is answered by
  `A09-receipt.md:51` (row 4, GREEN, mapped to `PROVINCE.md:9-11`); R06-F2's
  untracked `run.log` is recorded as an accepted gitignored class
  (`A06-province.md:100-101`, `.gitignore:3`). Integrator: do not carry either
  as open.

## 6. Verdict

**The PROVINCE re-verification is complete for C1–C5 and partial on C6.**
C1–C5: A06's five checks all PASS, independently reproduced by A11 and by my
M1–M10; the only additions are negative checks and two citation errata
(R07-F1). C6: the three surfaces `claims.json:60` names are covered with
evidence; the wider before-list is covered by A09's receipt table plus my M6–M8
pins, and A08 must assemble both, or the audit's "every touched surface"
threshold (`claims.json:64`) rests on fragments it does not cite.

**Net: `PROVINCE.md` needs no edit at HEAD; zero unfiled cross-domain bleed
found by any of the three passes (A06, A11, this one); zero A06-vs-A11
contradictions.**

## Limits / to-verify

- I did not re-run the O-claim mechanism (r6-row `KeyError` reproduction,
  `--selftest`) — that is A11 §2d and the O-block's leg.
- A06's sibling-roster reads (`MANIFEST.json` roster rows) were spot-checked
  only at the two corrected pointers (R07-F1); the remaining roster rows are
  A11/A07's leg.
- `run.log`-class untracked artifacts: whether the class is accepted or fixed
  is the integrator's call (`R06-a-review.md:96-105`), not filed here.

## Owed

- `reports/round-35/scout/K04-touched-census.md` — absent at write time; the
  integrator must diff K04's touch list against R06 §2 and this fragment's C6
  mapping, and file any no-net-change touch neither can see.
- `reports/round-35/adj/A08-audit-draft.md` — must carry R07-F1 (corrected
  pointers), R07-F2 (post-edit digest pins), R07-F3 (packet self-description
  drift), and A11-F1 (stale adoption-inventory census), or record each as an
  explicit exclusion with a reason.

## Citations

- `reports/round-35/targets.json` (seat R07 mission), `shared_rules`;
  `reports/round-35/claims.json:56,60,64,70` (A-claim before-list, after_required,
  thresholds, non-goals), `:8-9` (baseline)
- `reports/round-35/adj/A06-province.md:20-32,34-48,50-124,126-152,154-167,100-101,133-136,114`
- `reports/round-35/adj/A11-verify-2.md:6-8,30-42,99-100,136-140,151,170-193,241-283,303,321-326`
- `reports/round-35/adj/A05-records.md:46,222`; `reports/round-35/adj/A09-receipt.md:51,59-61`
- `reports/round-35/review/R06-a-review.md:36-51,62-83,96-105,182-187`
- `PROVINCE.md:9-11,16-20,22-25,27-29`; `REGIMEN.md:44-46`
- `reports/round-33/adj/A01-province.md:1-198`; `reports/round-33/adj/audit-assembled.md`
  (§Fresh checks digest list; §findings D1/D1b/D3); `reports/round-33/adj/A07-history.md:76,112`;
  `reports/round-33/adj/A10-receipt.md:78`
- `reports/round-34/handoff/declared-in-r7/packet.md:3,14,95,113,125`; `repin.json:5,53`;
  `claims-map.md:22,60,162,172`; `reports/round-34/op/adoption-inventory.json` (via A11-F1)
- `tools/exercise-handoff-e2e.py:184,2700,1933-1934,2566`; `tools/harness/receipt_guard_adoption.py`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md` (digest); `.gitignore:3`
- Siblings read-only: `lore-shokunin/PROVINCE.md:9` (Refuses line),
  `chousa-shokunin/PROVINCE.md:3`, `kake-shokunin/PROVINCE.md:3`,
  `kotoba-shokunin/PROVINCE.md:3`, `game-dev-2d-shokunin/PROVINCE.md:3`,
  `game-dev-3d-shokunin/PROVINCE.md:3-4`; `/home/vgpnk/Projects/shokunin/MANIFEST.json:2314,2890`
- Commands (lane root unless noted, snapshot `2026-10-19T08:19:34Z`, HEAD `4a7aede`):
  - `git rev-parse HEAD:PROVINCE.md c53782a:PROVINCE.md`; `git diff c53782a HEAD -- PROVINCE.md` (empty, exit 0); `git rev-list --count c53782a..HEAD` → 81
  - `sha256sum PROVINCE.md`; `wc -c -l PROVINCE.md` → 31/1636
  - `for p in …; do ls corpus/knowledge/$p/*.md | wc -l; done`; `ls corpus/knowledge/*/*.md | wc -l` → 201
  - `git ls-files | grep -cE '\.(html|css|js)$'` → 0; `git ls-files | grep -ciE 'game|rpg|mechanic'` → 0
  - `git show HEAD:<9 paths> | sha256sum`; `git log -1 --format=%h -- <paths>`
  - `git show HEAD:corpus/knowledge/linguistics/register-lexicon-ceilings.md | sha256sum` → `afe8bf22…`, 317 lines; same at `139e3b6` → `bb579d51…`, 289; `git show --numstat da68a6d -- <that path>` → +28/−0
  - `sha256sum reports/round-20/handoff/claims-map.md reports/round-34/handoff/declared-in-r7/claims-map.md` → `4b1b9a35…` (275 lines) / `d181de28…` (259)
  - `grep -n "are carried from" tools/exercise-handoff-e2e.py` → `:2934` (variable) and hard-coded literal at `:2700`
  - `grep -n "Refuses" ../lore-shokunin/PROVINCE.md` → `9:`; `sed -n '2308,2318p' ../MANIFEST.json`; `grep -n "source-research method" ../MANIFEST.json` → `2314`
  - `ls -d reports/round-* | wc -l` → 31; `ls corpus/lessons/`; per-file `grep -ciE 'non-canon|not canonized'` on 7 example stamps (1-7 hits each)
  - `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-3{3,4}/`; `grep -n -i kotodama /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → 44-47
  - `sha256sum tools/harness/receipt_guard_adoption.py` → `5858abcd…`; `sha256sum tools/exercise-handoff-e2e.py` → `34c85f57…`
  - `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-19T08:19:34Z`
