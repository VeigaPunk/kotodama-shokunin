# S03 — SHONEN section draft (round 48, loop 2, position 2)

- Seat: `S03` | role: scribe | claim: `cross` | round 48
- Mission (`reports/round-48/targets.json:50`): "SHONEN scribe: draft the four-box
  SHONEN with named non-author verifiers + evidence pointers."
- Out path: `reports/round-48/scribe/S03-shonen.md` — the only write by this seat.
- Baseline: lane HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`,
  measured at this cut), equal to the `a01405d` prefix declared at
  `reports/round-48/claims.json:7`.
- Observation cut: **2026-10-19T19:39Z** (UTC; local clock `16:39 -03`). Wave census at
  this cut: **3 files** under `reports/round-48/` — `claims.json`, `targets.json`,
  `telemetry/dispatch-declared.json` (`find reports/round-48 -type f | wc -l` → `3`).
  No verifier or reviewer seat had filed at that instant. A second snapshot at
  **19:40:36Z** found **27 files** (§3, §6); the wave kept growing after that, so both
  counts are snapshots, not closes.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  run from the lane root.
- Boundary: read-only probes plus this file. No filed byte edited; no corpus staging or
  write; no `reports/round-*/run-validation.py` executed (the r48 runner does not exist at
  this cut: `ls reports/round-48/run-validation.py` → No such file); no git commit, push,
  install or network call. `git status --porcelain` listed only the pre-existing
  `?? reports/round-46/review/` and `?? reports/round-48/`; `git status --porcelain --
  corpus/` is empty.
- Canon: NON-CANON engineering evidence. Nothing here asserts promotion, canon, clearance
  or closure. Box marks are operator-owned (`SHONEN.md:10-11`).

---

## §0 — Headline for the integrator

1. **All four boxes are carried `[~]`, not re-verified this round.** Round 48 declares
   coverage (C: one right-sized cartography entry) and calibration (Ca: README
   duplicate-heading fix + over-build defect disposition). Neither claim edits `SKILL.md`,
   executes an end-to-end D2→D3→D4 chain, runs a cold execution of SKILL instructions, or
   proposes a `PROVINCE.md` correction. No box-grade survey exists for r48.
2. **r47 moved no box either.** Its `validation.json` records C as
   `unchanged-blocked` — the 790-line assembled cartography draft carried nine blocking
   defects (`reports/round-47/validation.json:9`; R03's B1–B9 at
   `reports/round-47/review/R03-c-content.md:188-196`) — with O and Ca improved. A
   rejected C leaves the four boxes exactly where r47 found them.
3. **The r48 C claim is a coverage event, not box 2.** A landed corpus entry is not an
   *end-to-end domain task executed and logged*; the claim declares no chain and `LOG.md`
   has no r48 entry at this cut (last entry is r47 at `LOG.md:3895`).
4. **The r48 Ca claim is index hygiene, not a box move.** Removing the duplicate H1 at
   `corpus/README.md:3` and repairing the rev-2.4 prose vector is a correction to the
   corpus index; it neither strengthens nor weakens a promotion box.
5. **`SHONEN.md` itself is untouched and stays `[ ]` on all four lines.**
   `sha256sum SHONEN.md` → `7999d09b6b8e6f891947390207f171987bf662fb2bd91b2d1c7719ae1cf765ce`,
   11 lines, last (and only) touch `a527120`; `grep -n '^- \[' SHONEN.md` returns lines
   5–8, all `[ ]`. This seat did not edit the file.
6. **No `[x]` is recommended.** `[x]` requires a named non-author verifier per box
   (`SHONEN.md:10-11`; `reports/round-32/dossier-d11-shonen-boxes.md:210-212`). At the
   19:39Z first cut only the contract and dispatch files existed (3); by the 19:40:36Z
   snapshot 27 files had filed, all claim-level — none is a box sign-off. Absence is
   `could-not-evaluate`, never green.

---

## §1 — Paste-ready SHONEN block

Paste under the `SHONEN` heading of `.ufo/reports/round-48/kotodama.md`. One line per
`SHONEN.md` box; each `[~]` carries a resolvable pointer; no `[x]` is claimed.

```text
## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  carried, not re-verified this round: `SKILL.md` sha256
  `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` (732 lines,
  unchanged since r33 `da68a6d`); r34 durable box-1 survey 28/28 at the same digest
  (`reports/round-34/craft/box1-resurvey-durable.json`, exit 0); N1 expected-verdict block
  live at `SKILL.md:709`; the r33 citation conditions are diff-verified closed
  (`reports/round-35/adj/A10-gap-fill.md:161-164`). r48 edits no SKILL byte.
- [~] At least one end-to-end domain task executed and logged in LOG.md — carried: last
  chain evidence is the r31 50/50 green sweep (`reports/round-31/final-sweep.md:21`);
  r48's C claim lands at most one corpus entry, not a D2→D3→D4 chain, and has no `LOG.md`
  entry at this cut (`LOG.md:3895` is r47). Standing debts named: 12 D4 garment holds
  (`examples/culture-d4/expected-holds.json` `counts.hold = 12`), `head2`
  (`reports/round-26/register/design.md:228`), RL-3
  (`corpus/knowledge/linguistics/register-lexicon-ceilings.md:6`).
- [~] Instructions executable by an agent without oral context — carried: N1/N4/N5 closed
  by the r33 SKILL diff (`reports/round-35/adj/A10-gap-fill.md:161-164`), N3/N6 closed
  earlier; N7 still carried (`reports/round-37/scout/K02-defect-census.md:34`). No cold
  run this round. r48's Ca heading-count control is a sibling index control (not a sweep
  edit, not a cold run of the SKILL instructions); the freshness gate's first live use at
  declaration is process evidence, not box-3 evidence.
- [~] No cross-domain bleed; PROVINCE.md still accurate — carried plus live probes:
  `PROVINCE.md` sha256
  `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` (31 lines, last
  touch `c53782a`); live index sweep green 223 rows vs 223 files, partitions
  25/26/25/29/24/94 (`python3 -B reports/round-28/readme/sweep.py`, exit 0);
  `git status --porcelain -- corpus/` empty. r48's C target is inside
  `culture-material/`; Ca touches `corpus/README.md` (the index). A02 and A03 have filed
  (no second owner at file level; no corpus write, 0 undeclared paths), but A01/A04/X02/
  Q01 have not, so the round-level box-4 contribution is `could-not-evaluate`, not green.
  Claim verifiers do not sign the box.

No `[x]` is awarded; marks are operator-owned (`SHONEN.md:10-11`) and no named non-author
verifier has signed a box this round.
```

**Mark reading.** `[~]` here means "carried, asserted by the lane, pointer resolves" —
not "re-verified this round". If the integrator prefers the strict "untouched = `[ ]`"
reading, the same four lines stand with `[ ]`; the pointers and the no-`[x]` rule are
unchanged. Do **not** copy these lines into `SHONEN.md`: the checklist file is the
operator's promotion surface, not the round report.

---

## §2 — Per-box evidence

### Box 1 — SKILL.md decision tables / error patterns / checklists / cited sources

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-box1a`,
`r24-box1b` (`reports/round-24/promotion-review.md:26`). Re-surveyed r32-D11
(`reports/round-32/dossier-d11-shonen-boxes.md:201-208`); the r33 SKILL diff closed the
citation conditions and r35 diff-verified the closures
(`reports/round-35/adj/A10-gap-fill.md:161-164`). The r34 durable receipt pins the
executable inventory at 28/28 on the live digest
(`reports/round-34/craft/box1-resurvey-durable.json`).

**Live re-measurement at `a01405d` (2026-10-19T19:39Z):**

| probe | command | measured |
|---|---|---|
| digest | `sha256sum SKILL.md` | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` |
| size | `wc -l SKILL.md` | 732 |
| last touch | `git log --oneline -1 -- SKILL.md` | `da68a6d round-33: admit O/C/A — regimen-2 opening round …` |
| executable inventory | `python3 -B reports/round-30/craft/box1-survey.py` | `named 28, resolvable 28`, exit 0, `skill_sha256 = f9bd07c2…` |
| N1 block | `grep -c 'Expected verdicts at HEAD' SKILL.md` | 1 (anchor at `:709`) |
| SHONEN marks | `grep -n '^- \[' SHONEN.md` | 4 × `[ ]` |

The r34 receipt's `skill_sha256` is field-equal to the live digest, so it still describes
the live bytes (digest equality, not an assertion).

**Round-48 delta:** none. No r48 seat owns `SKILL.md`; C is corpus prose and Ca is an
index edit plus a successor record. `SKILL.md` is byte-identical to the r33 landing.

**Named non-author verifiers:** historical — `r24-box1a`, `r24-box1b` (r24), D11 (r32),
C07 (r34). r48 — R01/R02/R05 are round reviewers, not box sign-offs, and none has filed
at this cut.

**Recommended mark:** `[~]` carried. No fresh box evidence this round; no `[x]`.

### Box 2 — at least one end-to-end domain task executed and logged in LOG.md

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-box2a`,
`r24-box2b` (`reports/round-24/promotion-review.md:27`). The r31 final sweep re-executed
the capability surface in one deterministic pass: **50/50 green rows, exit 0**
(`reports/round-31/final-sweep.md:21`). The r24 conditions were dispositioned in the
r32-D11 survey (`reports/round-32/dossier-d11-shonen-boxes.md:201-208`).

**Standing debts, re-measured live:**

| debt | probe | measured |
|---|---|---|
| 12 D4 garment-form holds | `python3 -c "import json; …expected-holds.json"` | `hold 12 / note 0 / fail 0` |
| `head2` empty proper domain (RL-2) | `sed -n '226,230p' reports/round-26/register/design.md` | RL-2 row at `:228`, 59/62 forms ≤2 syllables |
| RL-3 register-lexicon ceiling | `sed -n '1,8p' corpus/knowledge/linguistics/register-lexicon-ceilings.md` | RL-3 citation record at `:6` |

**Round-48 delta:** none to the box. The C claim may land **one** corpus entry
(`corpus/knowledge/culture-material/cartography-and-mapmaking.md`) if the integrator
applies the fenced draft. At this cut the path is absent — `ls` returns No such file and
`find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' | wc -l` → `0`. Even
a landing would be a coverage event: the claim declares no D2→D3→D4 execution, and
`LOG.md` ends at the r47 entry (`LOG.md:3895`; 3916 lines).

**Named non-author verifiers:** historical — `r24-box2a`, `r24-box2b` (r24), R31-O11
(r31 sweep). r48 — V01 and F01 are the planned post-landing seats; neither has filed.
V01 would verify landing arithmetic and ownership, not a chain.

**Recommended mark:** `[~]` carried. The box is evidenced by the r31 sweep, not by r48.

### Box 3 — instructions executable by an agent without oral context

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-coldrun-a`,
`r24-coldrun-b`, `r24-coldrun-4`, `r24-coldrun-3`
(`reports/round-24/promotion-review.md:28`). Condition status:

| condition | status | live pointer |
|---|---|---|
| N1 — expected-verdict errata for r5/r6/r7 | **closed at r33** | `SKILL.md:709` (block live; `grep -c` → 1) |
| N3 — typed-input direction / pinned bytes | closed at r25 | `reports/round-32/dossier-d11-shonen-boxes.md:133` |
| N4 — no real costume/era artifact set named | **closed at r33** | `reports/round-35/adj/A10-gap-fill.md:161-164` |
| N5 — "history-retaining export" wording | **closed at r33** | `reports/round-35/adj/A10-gap-fill.md:161-164` |
| N6 — D3 snapshot-mode option | closed in SKILL text | `reports/round-32/dossier-d11-shonen-boxes.md:138` |
| N7 — executable-surface reading pin | **still carried** | `reports/round-37/scout/K02-defect-census.md:34`; `reports/round-33/calib/open-items-ledger.json` OI-07 |

**Round-48 delta:** none. Two r48 items are adjacent but do not move this box:

- **Ca's heading-count control** (targets seat Ca05) is a **sibling tool**
  (`tools/check-readme-heading.py`, fenced for the integrator) asserting exactly one
  `^# ` heading in `corpus/README.md`; R04 rules out editing the filed r28 sweep. Measured
  red (exit 1, `H1-COUNT lines=[1,3]`) on live, green (exit 0, `h1_lines [1]`) on the
  staged fix. That is a durable index control, not a cold execution of the SKILL
  instructions.
- **The freshness gate** now exists durably (`tools/harness/claims-freshness.py`, 105,529
  bytes, sha256 `466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d`) and
  was used at r48 declaration for the first time (`reports/round-48/telemetry/
  dispatch-declared.json` `freshness_gate_first_live_use`), where it flagged the O
  candidate premise stale and dropped it. That is process/operability evidence, not a
  cold run, and the gate is not named from `SKILL.md` as a cold-run instruction.

**Named non-author verifiers:** historical — the four `r24-coldrun-*` seats; A10 (r35,
diff verification of the N1/N4/N5 closures). r48 — O01/O04 are the planned gate-live
seats; R05 is the planned gate reviewer. None has filed, and none would sign a cold-run
box without a cold-run execution.

**Recommended mark:** `[~]` carried. N7 remains the named open condition.

### Box 4 — no cross-domain bleed; PROVINCE.md still accurate

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-box4-bleed`,
`r24-box4-province` (`reports/round-24/promotion-review.md:29`). Subsequent evidence:
r29 adjacency PASS inside its declared slice, with `PROVINCE.md` byte-unchanged
(`reports/round-29/adjacency/A09-A12-handoff.md:9,20`); r31 closure ledger re-verified
22/22 filed reports commit-ancestor-valid (`reports/round-31/closure-ledger.json`).

**Live re-measurement at `a01405d`:**

| probe | command | measured |
|---|---|---|
| PROVINCE digest | `sha256sum PROVINCE.md` | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` |
| size | `wc -l PROVINCE.md` | 31 |
| last touch | `git log --oneline -1 -- PROVINCE.md` | `c53782a supplement-opencode-1: recheck sources and harden reproducible evidence` |
| declared partitions resolve | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`; partitions `25/26/25/29/24/94`; exit 0 |
| r48 corpus writes | `git status --porcelain -- corpus/` | empty (no seat has staged under `corpus/`) |
| cartography path | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | absent (A, not M, if landed) |

**Round-48 delta:** the C landing is in-province (`culture-material/`); Ca edits the
in-province index `corpus/README.md` and files a queue successor under `reports/`. The
r48 non-goals forbid canon, packet-surface, filed-byte and promotion moves
(`reports/round-48/claims.json:54`); `non_goals` explicitly bars seat-level corpus
staging. No bleed class is introduced on disk at this cut.

**Named non-author verifiers:** historical — `r24-box4-bleed`, `r24-box4-province` (r24);
r29 adjacency (A09–A12); r31 closure audit. r48 — A02 (ownership) and A03 (write
surface) have filed: A02 finds no second owner at file level, A03 finds no corpus write
and 0 undeclared paths at its cut. Neither signs the box. A01 (scope/bleed), A04
(post-landing surface), X02 (honesty) and Q01 (final gate) have not filed. The live
probes above are this scribe's own; they support the no-write and PROVINCE-digest legs
only, not a full box-4 re-survey.

**Recommended mark:** `[~]` carried; round-level contribution `could-not-evaluate` until
A01/A04/X02/Q01 file. No `[x]`.

---

## §3 — Named non-author verifier ledger

Historical box-grade reviewers are named in `reports/round-24/promotion-review.md:20-33`
and re-surveyed in `reports/round-32/dossier-d11-shonen-boxes.md`. The r48 column is the
planned set; status is a **second snapshot at 19:40:36Z** (27 files; the first cut at
19:39Z had 3). The wave is in flight — this table is a snapshot, not a close reading.

| box | box-grade named reviewer(s) on record | r48 seats whose artifact would bear on the box | status at snapshot |
|---|---|---|---|
| 1 | `r24-box1a`, `r24-box1b` (r24); D11 (r32); C07 (r34) | R01, R02, R05 (round reviewers, not box sign-offs) | absent |
| 2 | `r24-box2a`, `r24-box2b` (r24); R31-O11 (r31 sweep) | V01 (post-landing), F01 (final census), R03 (C content) | absent; N03 filed pre-landing landing-safety only, not a chain |
| 3 | `r24-coldrun-a`, `r24-coldrun-b`, `r24-coldrun-4`, `r24-coldrun-3` (r24); A10 (r35) | O01, O04, R05, Ca05 (control author) | absent; Ca05 filed a control, not a cold run |
| 4 | `r24-box4-bleed`, `r24-box4-province` (r24); r29 A09–A12; r31 closure | A01, A04, X02, Q01, A02, A03 | A02 filed: no second owner at file level; A03 filed: no corpus write, 0 undeclared seat paths at its cut; A01/A04/X02/Q01 absent |

**Rule applied:** a seat is named only when its filed artifact states a verdict on the
box's subject. A round reviewer's general judgment is not a box sign-off, and a verifier
of a claim is not a verifier of a promotion box. A02 and A03 support the two box-4 legs
this scribe also measured (ownership, no corpus write); they do not sign the box, and no
`[x]` follows from them.

---

## §4 — Close-time checklist for the integrator

1. **Re-run the box probes at close** and replace every "at this cut" value:
   `sha256sum SKILL.md PROVINCE.md SHONEN.md`;
   `python3 -B reports/round-30/craft/box1-survey.py`;
   `find corpus/knowledge -name '*.md' | wc -l`;
   `ls corpus/knowledge/culture-material/*.md | wc -l`;
   `python3 -B reports/round-28/readme/sweep.py`;
   `grep -c '^# ' corpus/README.md`.
2. **Do not upgrade a box to `[x]`** unless a named non-author verifier signs *that box*.
   A claim verifier (C03–C09, C14–C18, V01, F01, N01–N03, Ca03/Ca04/Ca07, …) is not a
   box verifier. An absent seat is `could-not-evaluate`, never green.
3. **If C lands:** box 1 stays carried (`SKILL.md` unchanged); box 2 stays carried (one
   corpus entry is not an end-to-end chain); box 4 may cite A01/A03/A04 only after they
   file and pass. Record the landed line count against the right-sized threshold
   (<=~250 lines; live culture-material max is 221 at this cut,
   `wc -l corpus/knowledge/culture-material/*.md | sort -n | tail -2 | head -1` → 221
   `corpus/knowledge/culture-material/funerary-material-culture.md`, the `3756 total` row
   sorts last) and do not treat a landing as a box move.
4. **If Ca lands:** the README heading count must go 2 → 1 and the sweep must stay green
   (223 rows vs 223 files before the C landing; 224 after). The rev-2.4 prose vector at
   `corpus/README.md:10-11` sums **217** today while the footer at `:546-548` sums
   **223**; a rev-2.5 repair that makes the vector sum 224 is an index correction, not a
   box move.
5. **If a heading-count control lands** (Ca05), it must be a **sibling tool under
   `tools/`**, not an edit to `reports/round-28/readme/sweep.py` — the sweep is filed
   bytes and R04 records that route as inadmissible (`reports/round-48/review/
   R04-readme.md`, F-2). Record the tool's path and digest. That is box-3-adjacent
   process evidence only; box 3 still needs a cold execution of the SKILL instructions.
   Ca05's own measurement: `tools/check-readme-heading.py` exits 1 with `H1-COUNT
   lines=[1,3]` on the live README and 0 with `h1_lines [1]` on the staged fix.
6. **Keep the four-line block above**; do not edit `SHONEN.md`. The promotion decision
   remains operator-owned (`SHONEN.md:10-11`).

---

## §5 — Owed / to-verify

- **Box 1:** no r48 box-grade verifier. R01/R02/R05 absent; their round reviews cannot
  cure that.
- **Box 2:** V01/F01 post-landing legs are owed; at this cut the cartography path is
  absent and the r48 runner does not exist (`ls reports/round-48/run-validation.py` → No
  such file), so no r48 measurement can be cited. No r48 chain exists to log.
- **Box 3:** N7 remains carried (`reports/round-37/scout/K02-defect-census.md:34`). No
  cold run, no durable executable-surface pin change. O rests this round by declaration
  (freshness gate flagged its candidate premise stale); the gate's first live use is
  process evidence only.
- **Box 4:** A01/A04/X02/Q01 absent. A02 and A03 have filed: A02 finds no second owner
  at file level and three statement-level adjacencies the right-sized draft must fix;
  A03 finds no corpus write, no tracked/staged modification, and 0 undeclared seat paths
  at its cut (`reports/round-48/adj/A02-ownership.md`,
  `adj/A03-write-surface.md`). The live probes in §2 plus A02/A03 support the ownership
  and no-write legs only; neither seat signs the box.
- **Wave-level:** at the 19:40:36Z snapshot **27 files** had filed. Present: A02, A03,
  Ca02, Ca03, Ca05, W02, C02, C04, C07, C09, C11, C14, C15, M01, M02, N03, N01, X00,
  P01, R04, K01, K02, S02, and this scribe. Still absent: R01, R02, R03, R05, X01–X05
  (except X00), A01, A04, O01–O04, S01, W01, V01, F01, Q01, C01, C03, C05, C06, C08,
  C10, C12, C13, C16–C18, Ca01, Ca04, Ca06, Ca07. Absence is `could-not-evaluate`, not
  a pass.
- **Ca wording debts recorded by R04 (`to-verify`):** the claim's third counting command
  is `python3 reports/round-48/run-validation.py`, which the shared rules forbid running
  in-tree; the delivery certificate must be the post-apply sweep plus the heading
  control, not that command. R04's F-2 also bars editing the filed r28 sweep
  (`reports/round-48/review/R04-readme.md` §0).
- **Declaration clock drift (`to-verify`):** `reports/round-48/claims.json` and
  `telemetry/dispatch-declared.json` carry `declared_at_utc` / `recorded_at_utc` =
  `2026-10-19T19:45:00Z`, while the files' mtimes are `19:36:19Z` and `19:37:31Z`
  (`stat -c '%y'` → `16:36:19 -0300`, `16:37:31 -0300`) and this seat's clock read
  `19:39Z` at the cut. The declared stamp is ~6–9 minutes ahead of the artifacts it
  describes. Likely a planned stamp; the integrator should reconcile it at close or
  record it as a dispatch-metadata note. It does not affect the box marks.
- **README live state:** rev 2.4 (`corpus/README.md:5`); duplicate H1 at `:1` and `:3`
  (`grep -c '^# kotodama-shokunin corpus index'` → 2); prose vector at `:10-11` reads
  `25/23/26/25/24/94` (sum 217) against the footer `25/26/25/29/24/94` (sum 223) at
  `:546-548`. **Second live duplicate, independently measured:** `revision: 2.0` appears
  twice (`:42` and `:44`; `grep -c '^revision: 2\.0'` → 2), and `:42` is an orphan header
  with no body — the revision text resumes at `:44`. N01 reports the same finding
  (`reports/round-48/cross/N01-numbers.md` §4.1). The Ca claim names only the H1; the
  integrator must either extend the fix to `:42` or file it as a successor row.
  Neither the Ca fix nor the C landing is applied at this cut, so no box may cite a 224
  index or a one-heading README.

---

## §6 — Wave census and citations

**Wave census at 2026-10-19T19:40:36Z — 27 files** (`find reports/round-48 -type f | sort`):
`adj/{A02-ownership,A03-write-surface}.md`, `calib/{Ca02-overbuild,Ca03-readme-verify,Ca05-heading-control,W02-landing-spec}.md`,
`claims.json`, `cov/{C02-header,C04-citations,C07-boundary,C09-couples,C11-sweep,C14-example,C15-neighbors,M01-example,M02-calibration,N03-landing-safety}.md`,
`cross/{N01-numbers,X00-connector}.md`, `plan/P01-plan.md`,
`review/R04-readme.md`, `scout/{K01-rightsized-spec,K02-readme-defect}.md`,
`scribe/{S02-telemetry-draft,S03-shonen}.md`, `targets.json`,
`telemetry/dispatch-declared.json`.

At the first cut (`19:39Z`) the census was **3 files**. The integrator must recompute
the census at close; this list is the snapshot, not the close.

**Citations**

- `SHONEN.md:5-11` — the four boxes and the `[~]` / `[x]` rule; live digest
  `7999d09b…`, 11 lines, last touch `a527120`.
- `reports/round-48/targets.json:50` — this seat's mission and out path.
- `reports/round-48/claims.json:7` — baseline `a01405d`; `:20` freshness pause;
  `:27` C; `:41` Ca; `:54` `non_goals`.
- `reports/round-48/telemetry/dispatch-declared.json` — provider/model/key, declared
  stamps, first live use of the freshness gate.
- `reports/round-48/adj/A02-ownership.md` §0 — no second owner at file level; three
  statement-level adjacencies for the right-sized draft.
- `reports/round-48/adj/A03-write-surface.md` §0 — 0 undeclared paths, no corpus write,
  no tracked/staged modification at its cut.
- `reports/round-48/calib/Ca05-heading-control.md` §0 — control red (exit 1,
  `H1-COUNT lines=[1,3]`) on live, green (exit 0, `h1_lines [1]`) on the staged fix.
- `reports/round-48/review/R04-readme.md` §0 — F-1 (in-tree runner command) and F-2
  (no sweep edit) findings.
- `reports/round-48/cross/N01-numbers.md` §4.1 — the second live duplicate,
  `revision: 2.0` at `:42`/`:44`; independently re-measured here.
- `reports/round-24/promotion-review.md:20-33` — merged box verdicts and reviewer
  labels; `:26` box 1, `:27` box 2, `:28` box 3, `:29` box 4.
- `reports/round-32/dossier-d11-shonen-boxes.md:201-208` — summary table;
  `:210-212` — marks operator-owned.
- `reports/round-35/adj/A10-gap-fill.md:161-164` — OI-04/OI-05/OI-06/OI-07 closures by
  diff.
- `reports/round-34/craft/box1-resurvey-durable.json` — 28/28 at `f9bd07c2…`, exit 0.
- `reports/round-37/scout/K02-defect-census.md:34` — OI-07, N7 carried.
- `reports/round-33/calib/open-items-ledger.json` — OI-07 row.
- `reports/round-31/final-sweep.md:21` — 50/50 green rows.
- `reports/round-31/closure-ledger.json` — `counts_summary.commit_ancestry_ok = 22`.
- `reports/round-29/adjacency/A09-A12-handoff.md:9,20` — adjacency PASS and PROVINCE
  digest.
- `reports/round-26/register/design.md:228` — RL-2 row.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` — RL-3 citation record.
- `examples/culture-d4/expected-holds.json` — `counts.hold = 12` (measured).
- `reports/round-47/validation.json:9` — C `unchanged-blocked`, 790 assembled lines, nine
  blocking defects; no corpus delta, 223 holds.
- `reports/round-47/review/R03-c-content.md:188-196` — B1–B9 blocking defects.
- `reports/round-44/scout/K02-gap-scout.md:5,8,91-105` — cartography gap sweep and
  recommended landing path.
- `tools/harness/claims-freshness.py` — sha256 `466aa60d…`, 105,529 bytes.
- `LOG.md:3895` — r47 entry heading; 3916 lines at the cut.

**Commands measured by this seat** (lane root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`;
`sha256sum SKILL.md PROVINCE.md SHONEN.md corpus/README.md`;
`wc -l SKILL.md PROVINCE.md SHONEN.md LOG.md`;
`git log --oneline -1 -- SKILL.md PROVINCE.md SHONEN.md`;
`grep -n '^- \[' SHONEN.md`; `python3 -B reports/round-30/craft/box1-survey.py`;
`grep -c 'Expected verdicts at HEAD' SKILL.md`;
`python3 -B reports/round-28/readme/sweep.py`;
`grep -c '^# kotodama-shokunin corpus index' corpus/README.md`;
`grep -n '^# \|^revision:\|Counts checked 2026-10-19' corpus/README.md`;
`find corpus/knowledge -name '*.md' | wc -l`;
`ls corpus/knowledge/culture-material/*.md | wc -l`;
`wc -l corpus/knowledge/culture-material/*.md | sort -n`;
`find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' | wc -l`;
`git status --porcelain` and `git status --porcelain -- corpus/`;
`find reports/round-48 -type f | wc -l`; `date -u`; `stat -c '%y' reports/round-48/*.json`;
`sha256sum tools/harness/claims-freshness.py`.

**Write surface:** this file only — `reports/round-48/scribe/S03-shonen.md`. No
`corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`,
`tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git
commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.

**No axis is harmed by anything on disk at this cut.** The r48 C target is the same
verified-fresh cartography gap r47 correctly refused to force; its successor is a
right-sized draft, not a rollback and not a second topic.
