# Round 23 — Adjacency / connector (SCRIBE X06)

- **Date:** 2026-10-18. All timestamps are UTC command observations from this seat's
  own runs; two batches are anchored by `date -u` at **15:07:13Z** and **15:13:15Z**,
  and the observations between them were taken in that window (bounded, not
  individually stamped).
- **Axes:** adjacency (boundary invariants) + connector-surface evidence for claim O's
  two tails (wording disposition; combined-source successor pins).
- **Write scope:** only this fragment. No source fixes, no packet/validator/pin edits,
  no shared bookkeeping, no historical validator run, no Git mutation, no commit/push,
  no sibling writes. `export TMPDIR=$PWD/.scratch` was set before the two gate
  invocations; no other scratch files were written.
- **Baseline binding:** declared baseline `0e81d9d99514631d6717e1ff354d5a5a759aa980`
  (`reports/round-23/claims.json:5`); observed lane HEAD `7b181a52eb74319e5e5c40cdb1f0a1a1dc652079`;
  `git merge-base --is-ancestor 0e81d9d… HEAD` → success (15:07:13Z).

## Verdict (scoped to this seat's observations)

**Adjacency: clean at the recorded observations.** No out-of-lane write by this seat;
fleet root clean; PROVINCE blob-identical across baseline/HEAD/worktree; the handoff
interface contract bytes unmoved; the newest v3 packet passes the structural envelope
gate; the live D4 gate is green against the combined-source pins.

**Connector state for claim O: one leg already landed at baseline, two legs open.**
The D4 profile rows are bound to the final combined sources (round-22 close commit);
the alias-only v2 row and the round-20 D2 frozen receipt still bind earlier projector
digests, so their combined-source successors must land as **new rows**. The newest v3
packet still carries obsolete D4 claim wording (measured) — routed to the round-25
recipe, not absorbed here.

## Boundary observations (corroborating X02)

Batch at **15:07:13Z**, from the lane root:

- `git ls-files reports/round-{8..22} | wc -l` → **1,094** tracked filed paths.
- `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..22}` → exactly
  **one** row: ` M reports/round-22/fixes/regression.md`. This is a true-positive
  control for the detector: it demonstrably reports a deviation, so the remaining
  1,093 clean paths are a positive observation, not a blind pass.
- `git diff --name-status 0e81d9d… HEAD -- reports/round-{8..22}` → empty (no
  committed filed-surface change baseline→HEAD); fleet
  `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 --untracked-files=all`
  → empty.
- The deviation: `os.lstat('reports/round-22/fixes/regression.md')` at **15:13:15Z** →
  size **16,646**, mode **0644**, `mtime_ns 1792335572822711470` — identical to the
  three watch samples in `reports/round-23/scope.md` (X02), which adjudicates it as a
  **round-22 straggler** predating round-23 dispatch. This seat concurs with that
  adjudication as an observation and **does not certify the content** of the
  uncommitted closing verdict; disposition (commit as a late round-22 fragment vs
  restore filed bytes `fb73108…`) belongs to the parent integrator. HEAD/index blob
  remains `fb731082859d355daadcdb29d55e13b09d6b182c` (`git ls-files -s`, 15:07:13Z).

**PROVINCE accuracy:** `git rev-parse <baseline>:PROVINCE.md`, `git rev-parse
HEAD:PROVINCE.md`, and `git hash-object PROVINCE.md` all returned
`313b182f251564b7997b06996b4f063370778f11` (15:13:15Z batch) — the province file is
unchanged since the baseline and its boundary statements were read against the live
tree (own-repo write scope; refuses list matches the sibling lanes' existence; the
adjacent-contract path exists and is digest-stable below).

## Connector invariants (interface + envelopes)

- **Handoff interface contract unmoved:** `git rev-parse` at baseline and HEAD plus
  `git hash-object` on the worktree all give blob `66987ff3ef921bffe6d497608b2bc049f3b5ed9e`
  for `corpus/knowledge/synthesis/worldbible-integration-contract.md` (15:13:15Z batch);
  its SHA-256 is `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`
  (`sha256sum`, 15:07:13Z batch) — byte-equal to the same file's pin in the alias-only
  v2 baseline's read set (`reports/round-22/fixes/alias-coercion-v2-07.json` →
  `inputs`, read ~15:10Z). The interface bytes the interim v2 row pinned are the live
  bytes: no contract drift across the boundary the successor pins must bridge. The
  L0 contract-digest ratification question (SCORECARD round-8 row; fleet
  `.ufo/l0-questions.md`) remains open and escalated — not absorbed here.
- **Structural envelope green (control for the wording finding below):**
  `python3 tools/gates/handoff-packet-check.py reports/round-22/handoff/declared-in-r2/packet.md`
  → exit **0**, `fields=16/16 glossary-entries=20 findings=0` (~15:09Z, TMPDIR set).
- **Live D4 gate green against combined pins:** `python3 tools/gates/typed-pipeline-gate.py
  examples/culture-d4/packet.d4.yml` → exit **0**, **19/19** legs, self-declared pins
  projection `60b526b0…`, expected `3826ba68…`, adapter `92f5460b…` (~15:10Z, TMPDIR
  set). No tamper control was re-run by this seat; the stale-pin refusal control is
  filed round-22 evidence, and pin bytes were not modified to re-demonstrate it.

## Claim O tail (b) — combined-source successor pins: measured state

Facts as read at ~15:08–15:11Z; landings belong to the O-successor-pins seats, not
this fragment:

- **D4 profile rows: already bound to the final combined sources at baseline.**
  `tools/gates/typed-pipelines.json` → `profiles[0].expected.note` binds combined
  projector `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3`;
  `repin_history[2]` (round 22, `2026-10-18T14:53:59Z`, `reason`:
  "Final combined-source binding after the provisional projector pin became stale…")
  carries projector `2819f687…`, adapter `92f5460b…`, expected `3826ba68…`;
  `tools/gates/frozen/round-22/d4-repin/` holds the freeze receipt (14:55:28Z) and a
  3-row `MANIFEST.tsv` of exit-0 gate runs; `tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json`
  was frozen `2026-10-18T14:55:28.399348+00:00` with a `revision_note` binding hashes,
  not the base commit alone. All of this landed in the round-22 close commit `0e81d9d`
  (`git log --1 --format=%h -- tools/gates/typed-pipelines.json`, 15:07:13Z).
- **Alias-only v2 row: still interim.** `alias-coercion-v2-07.json` →
  `inputs["tools/d2-typed-labels.py"] = a10861f039f7e80a2f38a11fe1d72d4ef6fa5f48987f5fff96185b1875924a7b`,
  while the live source is `2819f687…` (`sha256sum`, 15:07:13Z batch). The live digest
  differing from the pinned digest is the measured control that the successor row is
  required rather than inheritable; the filed alias-only row stays untouched.
- **Round-20 D2 frozen receipt: binds the round-20 projector.**
  `tools/gates/frozen/round-20/repin-d2/run-receipt-repin.json` references projector
  `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb` (grep, ~15:11Z).
  Its combined-source successor must also be a new row; this fragment claims neither.
- Per `corpus/lessons/round-23.md:22`, the required new rows are the D2 live + frozen
  rows and the v2 row (the D4 profile leg being already landed); each needs before/after
  digests and a stale-pin refusal control.

## Claim O tail (a) — PLACEHOLDER_RE phrase class (evidence, not disposition)

- Detector: `reports/round-20/run-validation.py:87-89` — `PLACEHOLDER_RE` includes the
  alternative `\bunchanged\b` (case-insensitive), which matches inside the legitimate
  phrase `unchanged-foreign-path control` (hyphen is a non-word character, so the
  trailing `\b` fires).
- The phrase occurs in the filed claim wording: `grep -c "unchanged-foreign-path"`
  returns **1** in `reports/round-22/handoff/declared-in-r2/packet.md` (line 151,
  D4-CL08 basis) and **1** in `reports/round-20/handoff/packet.md` (~15:11Z). The
  disposition (accept the documented phrase class with a control in a successor
  validator, or re-word D4-CL08 in a new packet revision) belongs to the O-wording
  seats/orchestrator; no packet or validator byte was touched by this seat.

## Routed, not absorbed: v3 stale claim wording (measured)

The **newest** v3 packet (`reports/round-22/handoff/declared-in-r2/`, frozen per its
`freeze.txt`: packet sha `a97a0f0a…`, gate exit 0, links 105/105, 27 claims 16/7/4)
still carries the pre-family-clean D4 wording:

- `packet.md:149` — D4-CL06 grounds on `expected-holds.json#counts (hold 15, note 1,
  fail 0)`; the live file measures `{'hold': 12, 'note': 0, 'fail': 0}`
  (`python3 -c json.load(...)['counts']`, **15:13:15Z**).
- `packet.md:307` — OQ-V3-05 still lists "three rank holds + one note, thirteen
  unresolved rank items, three quarantine handles and four conflicts" for D4; the
  family-clean expectation and landed pins declare 12 form holds / 0 notes with the
  D2 passengers removed from D4 ownership (`reports/round-22/bleed/design.md`,
  `reports/round-22/bleed/repin.md` §dependency).

The structural envelope pass above is therefore **not** semantic integration evidence
for these rows — the same asymmetry the round-12 contract audit recorded
(`reports/round-12/adjacency/contract.md:9-10,23`). The claim-map/renderer supersession
is owned by the round-25 bleed recipe; this seat files the measured contrast and
changes nothing.

## Limits and non-claims

- No round acceptance, no promotion claim, no canon/rights/freshness certification.
  `reports/round-23/run-validation.py` did **not** exist at 15:13:15Z (`ls`:
  No such file) — the counting command is `to-verify` until its owner lands it.
- Fragments written by other seats this round (`reports/round-23/scope.md`,
  `audit/x05-pins-spotcheck.md`, `audit/x09-lessons-*`, `integration/fragment-ledger.*`,
  `fragment-index-x08.md`, `rule/fragment-D0*.md`, `rule/skill-draft.md`,
  `corpus/lessons/round-23.md`) were read for coordination only; all are untracked
  working-tree files at observation time and their content is not re-certified here.
- Parallel live-tree work was visible mid-round: `examples/culture-d2/expected-holds.json`
  was worktree-modified at **15:15:50Z** (`git status --porcelain=v1 --` on the path)
  after being clean at 15:07:13Z — a live examples/ surface outside the filed rounds,
  consistent with the D2-side successor-pin work; this seat neither wrote nor certified it.
- No historical round validator was executed; no filed rounds 8–22 byte was written by
  this seat; the only lane write is this fragment.
