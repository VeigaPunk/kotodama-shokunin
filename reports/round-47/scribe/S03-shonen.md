# S03 — SHONEN section draft (round 47, loop 2, position 1)

- Seat: `S03` | role: scribe | claim: `cross` | round 47
- Out path: `reports/round-47/scribe/S03-shonen.md` — the only write by this seat.
- Mission (`reports/round-47/targets.json`, id `S03`): "SHONEN scribe: draft the
  four-box SHONEN section with named non-author verifiers + evidence pointers for the
  integration."
- Baseline: lane HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`),
  equal to `reports/round-47/claims.json:7`; declared at `2026-10-19T17:46:52Z`
  (`reports/round-47/claims.json:6`).
- Observation cut: **2026-10-19T18:03:10Z** (UTC). Wave census at this cut: **33 files**
  under `reports/round-47/` (`find reports/round-47 -type f | wc -l`); the list is in §6.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  run from the lane root.
- Boundary: read-only probes plus this file. No filed byte edited; no corpus staging or
  write; no `reports/round-*/run-validation.py` executed; no git commit, push, install or
  network call. `git status --porcelain` at the cut listed only `?? reports/round-46/review/`
  and `?? reports/round-47/`.
- Canon: NON-CANON engineering evidence. Nothing here asserts promotion, canon, clearance
  or closure; the box marks are operator-owned (`SHONEN.md:10-11`).

---

## §0 — Headline for the integrator

1. **All four boxes are carried `[~]`, not re-verified this round.** Round 47 declares
   coverage / operability / calibration claims; it touches no `SKILL.md` byte, runs no
   end-to-end domain chain, executes no cold run, and proposes no `PROVINCE.md` correction.
   The last box-grade survey on record is r32-D11, carried through r33-A16 and every
   integration draft since; no later round re-surveyed the boxes.
2. **`SHONEN.md` itself is untouched and stays `[ ]` on all four lines.**
   `sha256sum SHONEN.md` → `7999d09b6b8e6f891947390207f171987bf662fb2bd91b2d1c7719ae1cf765ce`,
   11 lines, last (and only) commit `a527120 mint: kotodama-shokunin seed kit`; `grep -n '^- \[' SHONEN.md`
   returns lines 5-8, all `[ ]`. This seat did not edit the file.
3. **Round 47's contribution to the boxes is verifier evidence, not a box move.**
   - C05 (`reports/round-47/cov/C05-freshness.md`) and C07
     (`reports/round-47/cov/C07-contract-audit.md`) filed: the C landing is absent, the
     worktree has no `corpus/` change, and the proposed path is an addition (A), not a
     modification (M).
   - V01 (`reports/round-47/cov/V01-post-landing.md`) filed `PRE-LANDING /
     could-not-evaluate` on live bytes; the staged 224 proof is scratch-only.
   - O10 (`reports/round-47/op/O10-exit-codes.md`) and O13
     (`reports/round-47/op/O13-probe-coverage.md`) filed: `tools/harness/claims-freshness.py`
     **does not exist** at this cut, so the O deliverable is `could-not-evaluate`, not green.
   - The box-4 named seats A01/A03/X02/Q01 and the box-1/2/3 box-grade verifiers have not
     filed at this cut. Absence is `could-not-evaluate`, never green.
4. **No `[x]` is recommended.** `[x]` requires a named non-author verifier per box
   (`SHONEN.md:10-11`; `reports/round-32/dossier-d11-shonen-boxes.md:210-212`), and no
   r47 seat has signed a box this round. The four lines below use `[~]` (asserted by the
   lane, pointer required); the pointers resolve to filed artifacts.
5. **A `+1` corpus entry does not move box 2.** Box 2 requires an *end-to-end domain task
   executed and logged*; a landed knowledge entry is a corpus-coverage event, not a
   D2→D3→D4→handoff chain. The claim's own `after_required` names no chain, and `LOG.md`
   has no r47 entry at this cut.

---

## §1 — Paste-ready SHONEN block

Paste under the `SHONEN` heading of `.ufo/reports/round-47/kotodama.md`. One line per
`SHONEN.md` box; each `[~]` carries a resolvable pointer; no `[x]` is claimed.

```text
## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  carried, not re-verified this round: `SKILL.md` sha256
  `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` (732 lines,
  unchanged since r33 `da68a6d`); r34 durable box-1 survey 28/28 at the same digest
  (`reports/round-34/craft/box1-resurvey-durable.json`); the three r33 citation conditions
  are diff-verified closed (`reports/round-35/adj/A10-gap-fill.md:161-164`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — carried: last
  chain evidence is the r31 50/50 green sweep (`reports/round-31/final-sweep.md:21`); r47
  lands at most one corpus entry (C), not a D2→D3→D4 chain, and has no `LOG.md` entry at
  this cut (last entry is r46). Standing debts named: 12 D4 garment holds
  (`examples/culture-d4/expected-holds.json` `counts.hold = 12`), `head2`
  (`reports/round-26/register/design.md:228`), RL-3
  (`corpus/knowledge/linguistics/register-lexicon-ceilings.md:6`).
- [~] Instructions executable by an agent without oral context — carried: N1/N4/N5 closed
  by the r33 SKILL diff (`SKILL.md:709-721`;
  `reports/round-35/adj/A10-gap-fill.md:164`), N3/N6 closed earlier; N7 still carried
  (`reports/round-37/scout/K02-defect-census.md:34`). No cold run this round; the r47 O
  gate is absent at this cut (`reports/round-47/op/O10-exit-codes.md:1`,
  `op/O13-probe-coverage.md:1`), so it is not box-3 evidence.
- [~] No cross-domain bleed; PROVINCE.md still accurate — carried: `PROVINCE.md` sha256
  `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` (31 lines, last
  commit `c53782a`); r47's C landing stays inside `culture-material/` and two filed
  non-author verifiers record no corpus write (`reports/round-47/cov/C05-freshness.md`,
  `cov/C07-contract-audit.md`); the box-4 named seats A01/A03/X02/Q01 have not filed at
  this cut, so the round-level box-4 contribution is `could-not-evaluate`, not green.

No `[x]` is awarded; marks are operator-owned (`SHONEN.md:10-11`) and no named non-author
verifier has signed a box this round.
```

**Mark reading.** `[~]` here means "carried, asserted by the lane, pointer resolves" — not
"re-verified this round". If the integrator prefers the strict "untouched = `[ ]`"
reading, the same four lines stand with `[ ]`; the pointers and the no-`[x]` rule are
unchanged. Do **not** copy these lines into `SHONEN.md`: the checklist file is the
operator's promotion surface, not the round report.

---

## §2 — Per-box evidence

### Box 1 — SKILL.md decision tables / error patterns / checklists / cited sources

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-box1a`,
`r24-box1b` (`reports/round-24/promotion-review.md:26,39-40`). Re-surveyed r32-D11 with
conditions 2-4 still open (`reports/round-32/dossier-d11-shonen-boxes.md:28-79,201-208`);
conditions 2-4 were then closed by the r33 SKILL diff and diff-verified at r35
(`reports/round-35/adj/A10-gap-fill.md:161-164`). The r34 durable receipt pins the
executable inventory at 28/28 on the live digest
(`reports/round-34/craft/box1-resurvey-durable.json`).

**Live re-measurement at `6e9a30d` (2026-10-19T18:03Z):**

| probe | command | measured |
|---|---|---|
| digest | `sha256sum SKILL.md` | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` |
| size | `wc -l SKILL.md` | 732 |
| last touch | `git log --oneline -1 -- SKILL.md` | `da68a6d round-33: admit O/C/A — regimen-2 opening round …` |
| executable inventory | `python3 -B reports/round-30/craft/box1-survey.py` | `named 28, resolvable 28`, exit 0 |
| loanword cites | `grep -n "loanword-material-dating.md" SKILL.md` | `:486` cites `:30-31,63`; `:488` cites `:59,63` |
| worldbible erratum | `grep -n "erratum 2026-10-19" SKILL.md` | 6 clauses, incl. `:128`, `:501` |
| retired anchors | `grep -n "retired anchor" SKILL.md` | 4 rows (`:479`, `:481`, `:483`, `:491`) |
| SHONEN marks | `grep -n '^- \[' SHONEN.md` | 4 × `[ ]` |

**Round-47 delta:** none. No r47 seat owns `SKILL.md`; the C draft is corpus prose and
the O draft is a tool body. `SKILL.md` is byte-identical to the r33 landing, so the r34
receipt still describes the live bytes (digest equality, not an assertion).

**Named non-author verifiers:** historical — `r24-box1a`, `r24-box1b` (r24), D11 (r32,
non-author survey), C07 (r34, verifier). r47 — none at box grade; R01/R02 are round
reviewers, not box sign-offs, and both are absent at this cut.

**Recommended mark:** `[~]` carried. No fresh box evidence this round; no `[x]`.

### Box 2 — at least one end-to-end domain task executed and logged in LOG.md

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-box2a`,
`r24-box2b` (`reports/round-24/promotion-review.md:27,93-94`). The r31 final sweep
re-executed the capability surface in one deterministic pass: **50/50 green rows, exit 0**
(`reports/round-31/final-sweep.md:21`). The r24 conditions were dispositioned in the
r32-D11 survey (`reports/round-32/dossier-d11-shonen-boxes.md:81-122`).

**Standing debts, re-measured live:**

| debt | probe | measured |
|---|---|---|
| 12 D4 garment-form holds | `python3 -c "import json; …expected-holds.json"` | `{"hold": 12, "note": 0, "fail": 0}` |
| `head2` empty proper domain (RL-2) | `sed -n '224,232p' reports/round-26/register/design.md` | row RL-2 at `:228`, 59/62 forms ≤2 syllables |
| RL-3 register-lexicon ceiling | `ls corpus/knowledge/linguistics/register-lexicon-ceilings.md` | present; ceiling recorded at `:6` |

**Round-47 delta:** none to the box. The C claim may land **one** corpus entry
(`corpus/knowledge/culture-material/cartography-and-mapmaking.md`) if the integrator
applies the fenced draft; at this cut the path is absent (K01 §2; C05 §2; C07 §0). Even a
landing would be a coverage event, not an end-to-end chain: the claim declares no
D2→D3→D4 execution, and `LOG.md` ends at the r46 entry (`wc -l LOG.md` → 3893).

**Named non-author verifiers:** historical — `r24-box2a`, `r24-box2b` (r24), R31-O11
(r31 sweep). r47 — V01 is filed but `PRE-LANDING / could-not-evaluate` on live bytes
(`reports/round-47/cov/V01-post-landing.md:1`) and would verify the landing arithmetic,
not a chain; R03 has not filed.

**Recommended mark:** `[~]` carried. The box is evidenced by the r31 sweep, not by r47.

### Box 3 — instructions executable by an agent without oral context

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-coldrun-a`,
`r24-coldrun-b`, `r24-coldrun-4`, `r24-coldrun-3`
(`reports/round-24/promotion-review.md:28,137-140`). Condition status at the r32 survey:

| condition | status | live pointer |
|---|---|---|
| N1 — expected-verdict errata for r5/r6/r7 | **closed at r33** | `SKILL.md:709-721`; `reports/round-35/adj/A10-gap-fill.md:164` |
| N3 — typed-input direction / pinned bytes | closed at r25 | `reports/round-32/dossier-d11-shonen-boxes.md:133-137` |
| N4 — no real costume/era artifact set named | **closed at r33** | `reports/round-35/adj/A10-gap-fill.md:164` |
| N5 — "history-retaining export" wording | **closed at r33** | `reports/round-35/adj/A10-gap-fill.md:164` |
| N6 — D3 snapshot-mode option | closed in SKILL text | `reports/round-32/dossier-d11-shonen-boxes.md:138-140` |
| N7 — executable-surface reading pin | **still carried** | `reports/round-37/scout/K02-defect-census.md:34`; `reports/round-33/calib/open-items-ledger.json` OI-07 |

Probe at this cut: `grep -c "Expected verdicts at HEAD" SKILL.md` → **1** (line 709), so
the N1 block is live in the current bytes.

**Round-47 delta:** none. The O claim would add a durable executable
(`tools/harness/claims-freshness.py`), but at this cut the path is absent
(`reports/round-47/op/O10-exit-codes.md:1`, `op/O13-probe-coverage.md:1`) and no cold-run
seat declares an execution of the SKILL instructions. A tool selftest is not a cold run,
and the O gate is not named from `SKILL.md`, so it cannot move this box.

**Named non-author verifiers:** historical — the four `r24-coldrun-*` seats; A10 (r35,
diff verification of the N1/N4/N5 closures). r47 — O08/O11/V02/R04 have not filed; O10
and O13 filed but report `could-not-evaluate` on the absent deliverable, so they do not
sign the box.

**Recommended mark:** `[~]` carried. N7 remains the named open condition.

### Box 4 — no cross-domain bleed; PROVINCE.md still accurate

**Last box-grade verdict:** verified-with-conditions, r24; reviewers `r24-box4-bleed`,
`r24-box4-province` (`reports/round-24/promotion-review.md:29,201-202`). Subsequent
evidence: r29 adjacency PASS inside its declared slice, with `PROVINCE.md` byte-unchanged
(`reports/round-29/adjacency/A09-A12-handoff.md:9,20`); r31 closure ledger re-verified
22/22 filed reports commit-ancestor-valid
(`reports/round-31/closure-ledger.json` `counts_summary.commit_ancestry_ok = 22`;
`reports/round-32/dossier-d11-shonen-boxes.md:195`).

**Live re-measurement at `6e9a30d`:**

| probe | command | measured |
|---|---|---|
| PROVINCE digest | `sha256sum PROVINCE.md` | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` |
| size | `wc -l PROVINCE.md` | 31 |
| last touch | `git log --oneline -1 -- PROVINCE.md` | `c53782a supplement-opencode-1: recheck sources and harden reproducible evidence` |
| declared partitions resolve | `ls corpus/knowledge/*/` | six partitions present; live vector 25/26/25/29/24/94 = 223 (`python3 -B reports/round-28/readme/sweep.py`, exit 0) |
| r47 corpus writes | `git status --porcelain -- corpus/` | empty; C05 §2 and C07 §0 record no corpus byte written |

**Round-47 delta:** the C landing is in-province (`culture-material/`); the Ca claim files
successor records only; the O claim is a lane harness tool. The r47 non-goals forbid canon,
packet-surface, filed-byte and promotion moves (`reports/round-47/claims.json`
`non_goals`). No bleed class is introduced on disk at this cut.

**Named non-author verifiers:** historical — `r24-box4-bleed`, `r24-box4-province` (r24);
r29 adjacency (A09-A12); r31 closure audit. r47 — A01 (scope/bleed), A03 (write-surface),
X02 (honesty), Q01 (final gate) have not filed; C05 and C07 are filed and support the
no-corpus-write leg only, not a full box-4 re-survey.

**Recommended mark:** `[~]` carried; round-level contribution `could-not-evaluate` until
A01/A03/X02/Q01 file. No `[x]`.

---

## §3 — Named non-author verifier ledger

Historical box-grade reviewers are named in `reports/round-24/promotion-review.md:20-33`
and re-surveyed in `reports/round-32/dossier-d11-shonen-boxes.md`. The r47 column is the
integration's pending set; status is measured at `18:03:10Z`.

| box | box-grade named reviewer(s) on record | r47 seats whose artifact bears on the box | status at cut |
|---|---|---|---|
| 1 | `r24-box1a`, `r24-box1b`; D11 (r32); C07 (r34) | R01, R02 (round reviewers, not box sign-offs) | absent |
| 2 | `r24-box2a`, `r24-box2b`; R31-O11 (sweep) | V01 (post-landing), R03 (content) | V01 filed `PRE-LANDING / could-not-evaluate`; R03 absent |
| 3 | `r24-coldrun-a`, `r24-coldrun-b`, `r24-coldrun-4`, `r24-coldrun-3`; A10 (r35) | O08, O11, V02, R04 | absent; O10/O13 filed but do not sign the box |
| 4 | `r24-box4-bleed`, `r24-box4-province`; r29 A09-A12; r31 closure | A01, A03, X02, Q01 | absent; C05/C07 filed as partial (no corpus write) |

**Rule applied:** a seat is named only when its filed artifact states a verdict on the
box's subject. A round reviewer's general judgment is not a box sign-off, and a verifier
of a claim is not a verifier of a promotion box.

---

## §4 — Close-time checklist for the integrator

1. **Re-run the four box probes at close** and replace every "at this cut" value:
   `sha256sum SKILL.md PROVINCE.md SHONEN.md`;
   `python3 -B reports/round-30/craft/box1-survey.py`;
   `find corpus/knowledge -name '*.md' | wc -l`;
   `python3 -B reports/round-28/readme/sweep.py`.
2. **Do not upgrade a box to `[x]`** unless a named non-author verifier signs *that box*.
   A claim verifier (C05/C07/V01/O10/O13/…) is not a box verifier. An absent seat is
   `could-not-evaluate`, never green.
3. **If C lands:** box 1 stays carried (`SKILL.md` unchanged), box 2 stays carried (one
   corpus entry is not an end-to-end chain), box 4 may cite V01 + A01/A03/X02 only after
   they pass; the README rev-2.5 prose-vector repair is a corpus-index correction, not a
   box move.
4. **If O lands:** box 3 still needs a cold-run execution of the SKILL instructions; the
   tool's `--selftest` and exit-code suite are not a cold run. Record the durable path and
   its digest, then re-run O10/O13/V02 against the landed bytes.
5. **Keep the four-line block above**; do not edit `SHONEN.md`. The promotion decision
   remains operator-owned (`SHONEN.md:10-11`).

---

## §5 — Owed / to-verify

- **Box 1:** no r47 box-grade verifier. R01/R02 absent; their round reviews cannot cure
  that.
- **Box 2:** V01's real post-landing leg is owed (`PRE-LANDING / could-not-evaluate` on
  live bytes); R03 absent. No r47 chain exists to log.
- **Box 3:** N7 remains carried; no durable executable-surface pin is on record
  (`reports/round-37/scout/K02-defect-census.md:34`). O08/O11/V02/R04 absent. The O
  deliverable is absent at this cut, so the box-3 contribution is `could-not-evaluate`.
- **Box 4:** A01/A03/X02/Q01 absent. C05/C07 cover only the no-corpus-write leg.
- **Wave-level (not exhaustive):** C06, C08, C11, C12, C14, W01, W02, Ca07, R01-R05,
  X01-X03, A02, S01, V02, Q01 were absent at the cut. Their absence is recorded here as
  `could-not-evaluate`, not as a pass.
- **README live state:** rev 2.4; the prose vector still reads `25/23/26/25/24/94`
  (sum **217**) while the footer reads `25/26/25/29/24/94` (sum **223**)
  (`corpus/README.md:11`, `:548`). The rev-2.5 draft (C09) is not applied at this cut, so
  no box may cite a 224 index.
- **Ca successor:** `reports/round-47/calib/Ca06-queue-successor.md` is filed; its
  acceptance is Ca07's, not this seat's.

---

## §6 — Wave census and citations

**Wave census at `2026-10-19T18:03:10Z` — 33 files** (`find reports/round-47 -type f | sort`):
`calib/{Ca01-stale-premises,Ca02-resolver-edge,Ca03-manifest-schemas,Ca04-provider-amendments,Ca05-verify,Ca06-queue-successor}.md`,
`claims.json`, `cov/{C01-entry-a,C02-entry-b,C03-entry-c,C04-entry-header,C05-freshness,C07-contract-audit,C09-readme,C10-sweep,C13-couples,V01-post-landing}.md`,
`cross/{X00-connector,X04-coverage-critic,X05-baseline-drift}.md`,
`op/{O05-r43-demo,O06-negative-control,O10-exit-codes,O13-probe-coverage}.md`,
`plan/{P01-plan,P02-c-plan,P03-o-plan}.md`,
`scout/{K01-gap-recheck,K02-seed-extract,K03-gate-spec}.md`,
`scribe/S02-telemetry-draft.md`, `targets.json`,
`telemetry/dispatch-declared.json`.

The integrator must recompute the census at close; this list is the cut, not the close.

**Citations**

- `SHONEN.md:5-11` — the four boxes and the `[~]` / `[x]` rule; live digest
  `7999d09b…`, 11 lines, last commit `a527120`.
- `reports/round-24/promotion-review.md:20-33` — merged box verdicts and reviewer labels;
  `:26` box 1, `:27` box 2, `:28` box 3, `:29` box 4; bodies at `:35-62`, `:89-131`,
  `:133-196`, `:197-232`.
- `reports/round-32/dossier-d11-shonen-boxes.md:28-79` — box-1 conditions; `:124-167` —
  box 3; `:169-199` — box 4; `:201-208` — summary table; `:210-212` — marks operator-owned.
- `reports/round-35/adj/A10-gap-fill.md:161-164` — OI-04/OI-05/OI-06/OI-07 closures by
  diff.
- `reports/round-34/craft/box1-resurvey-durable.json` — 28/28 at `f9bd07c2…`, exit 0.
- `reports/round-37/scout/K02-defect-census.md:34` — OI-07, N7 carried.
- `reports/round-33/calib/open-items-ledger.json` — OI-07 row (N1/N4/N5/N7 cluster).
- `reports/round-31/final-sweep.md:21` — 50/50 green rows.
- `reports/round-31/closure-ledger.json` — `counts_summary.commit_ancestry_ok = 22`.
- `reports/round-29/adjacency/A09-A12-handoff.md:9,20` — adjacency PASS and PROVINCE
  digest.
- `reports/round-26/register/design.md:224-232` — RL-2 at `:228`.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` — RL-3 ceiling.
- `examples/culture-d4/expected-holds.json` — `counts.hold = 12` (measured).
- `reports/round-47/cov/C05-freshness.md` §0/§2 — freshness PASS at `6e9a30d`; no corpus
  byte written.
- `reports/round-47/cov/C07-contract-audit.md` §0 — contract audit; no corpus byte
  written; draft absent at its cut.
- `reports/round-47/cov/V01-post-landing.md` §0 — `PRE-LANDING / could-not-evaluate` on
  live bytes.
- `reports/round-47/op/O10-exit-codes.md:1` — durable tool absent; `could-not-evaluate`.
- `reports/round-47/op/O13-probe-coverage.md:1` — durable tool absent; prototype fails
  coverage.
- `reports/round-47/scout/K01-gap-recheck.md` — 0 owners at `6e9a30d`; 223 / 25.
- `reports/round-47/cross/X05-baseline-drift.md` §1 — baseline identity PASS.
- `reports/round-47/claims.json:6-7,24-47` — baseline, claims, thresholds; `non_goals`.
- Commands measured by this seat (from the lane root, `TMPDIR=$PWD/.scratch`,
  `PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`; `sha256sum SKILL.md PROVINCE.md
  SHONEN.md`; `wc -l SKILL.md PROVINCE.md SHONEN.md LOG.md`;
  `git log --oneline -1 -- SKILL.md PROVINCE.md`; `git log --oneline -- SHONEN.md`;
  `python3 -B reports/round-30/craft/box1-survey.py`;
  `find corpus/knowledge -name '*.md' | wc -l`;
  `ls corpus/knowledge/culture-material/*.md | wc -l`;
  `python3 -B reports/round-28/readme/sweep.py`; `grep -n '^- \[' SHONEN.md`;
  `grep -n "Expected verdicts at HEAD\|retired anchor\|erratum 2026-10-19" SKILL.md`.
