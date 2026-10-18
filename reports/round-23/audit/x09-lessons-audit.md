# X09 — lessons-partition audit (round 23)

- round 23 (operator: loop 2, GLM round 1 of 2; 16 workers on
  `zai-coding-plan/glm-5.3-flash-low` per `reports/round-23/claims.json`) ·
  seat **X09** (SCRIBE X09 — lessons audit) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X09: lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  claims `baseline_revision` `0e81d9d…` (round-22 close, committed 11:59:16−03:00);
  HEAD `7b181a52eb74319e5e5c40cdb1f0a1a1dc652079` (round-23 declaration,
  12:00:40−03:00). HEAD is one commit past the declared baseline; that commit
  is the declaration itself, so the baseline binding is correct (none of the
  R19/R22 receipt-vs-baseline drift).
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies
  no round, blesses no lesson, and grants no promotion.
- writes: this file, its siblings `x09-lessons-audit.py` and
  `x09-lessons-receipt.json`, all under `reports/round-23/audit/`. No
  `corpus/**` byte, no filed round-8–22 byte, no tool or gate is edited by
  this seat. No commit, no push.
- measurement window: 2026-10-18T15:09:29Z–15:11:53Z UTC. The wave was live
  throughout (see X09-1 and X09-3); every reading names its stamp and is
  re-measurable.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | lesson census: **24 lesson files**, rounds 1–12 and 14–23 (round 5 twice; round 13 operator-skipped, no work landed per `LOG.md:3077-3078`; `supplement-opencode-1.md` non-round) | measured |
| 2 | every loop-era lesson (rounds 8–12, 14–23 + supplement) carries all four contract lines and a `## Gate`; rounds 1–4 lack them (pre-contract seed lessons) and round 16 has a Gate-less body — the round-19 audit's known state, unchanged | measured |
| 3 | **the round-23 lesson landed inside this audit's window** (23 files at 15:09:29Z → 24 at 15:10:58Z; `round-23.md` mtime 15:09:13.963905Z, sha8 `b567a60a`, 51 lines) — contract-complete, Gate shape matching the round-21/22 norm | measured / finding X09-1 |
| 4 | path sweep: **399 backticked repo refs, 12 unresolved** — 11 historical/aspirational in filed read-only lessons (same set as the round-19 X28-2 census, stable since) + 1 pending (`reports/round-23/run-validation.py`, declared in the claims, not yet written) | finding X09-2 |
| 5 | `round_23_mentioned_in_log: false` at the receipt stamp — LOG integration belongs to the parent; a sequence fact, not a defect | measured |
| 6 | worktree not clean at every stamp: ` M reports/round-22/fixes/regression.md` (+122/−54, in-place rewrite of a round-22-close-committed file) — corroborates the round-23 lesson's own 15:06:46Z dated observation | environment, X09-3 |

## 1. Method

Read-only tool `reports/round-23/audit/x09-lessons-audit.py` (stdlib only;
schema `kotodama-lessons-audit-v3`), run from the lane root on 2026-10-18:

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-23/audit/x09-lessons-audit.py --selftest   # 20/20 PASS
python3 reports/round-23/audit/x09-lessons-audit.py              # census summary
python3 reports/round-23/audit/x09-lessons-audit.py --json > reports/round-23/audit/x09-lessons-receipt.json
```

The tool extracts each lesson's `## Gate` block (bounded by the next `## `
heading), counts opening-reading lines (`Opening <axis> reading:`),
`Admitted`/`Rejected` markers and a `spot-check` mention, checks the four
contract lines (`source:`, `verified-at:`, `recheck:`, `scope:`), resolves
every backticked repo path against the live tree, and cross-checks lesson
rounds against LOG.md's `Round N admitted` / `Round N REJECTED` records. The
process opens no file for writing; the receipt is the caller's stdout
redirect. Selftest: **20/20 checks PASS** (`SELFTEST OK`, 15:10:57Z), including
new v3 controls (REJECTED-regex vs admitted headings; line-range refs
resolving to clean paths; ISO-UTC mtime format).

v3 deltas over the round-20 v2 tool (`reports/round-20/audit/x24-lessons-audit.py`):
per-row `mtime_utc` (live-wave re-reads become comparable); LOG.md REJECTED
rounds extracted separately so a rejected round's lesson is not conflated with
an admission; the round probe parameterized (`--round`, default 23). The
backticked-path resolver is unchanged on purpose — the documented contract
that a pending path is listed as missing until it lands.

## 2. Census (2026-10-18T15:11:17Z, `x09-lessons-receipt.json`)

- Lesson files: **24**. Rounds with lessons: **1–12, 14–23** (round 5 twice;
  round 13 operator-skipped; `supplement-opencode-1.md` is not round-numbered).
- Contract lines (`source:` / `verified-at:` / `recheck:` / `scope:`) and a
  `## Gate` section: present in **all 20 loop-era files** (rounds 8–12,
  14–23 + supplement). Absent only in rounds **1–4** (pre-contract seeds) and
  **round 16** (Gate-less — the state the round-19 audit already recorded,
  unchanged since; filed, read-only).
- Gate marker vocabulary: rounds **19 and 20** carry the older shape (3
  `Opening <axis> reading:` candidates each; round 20 also a spot-check and a
  Rejected marker). Rounds **21, 22 and 23** carry the newer shape
  (`Axes as declared` + `### Rule` + per-axis sections; no marker vocabulary).
  The round-23 lesson therefore matches the **current norm** (round-21/22
  shape), not a contract regression. This audit counts both shapes as a Gate.
- LOG.md cross-check: `Round N admitted` headings — **8, 9, 10, 12, 15, 16,
  18, 19, 20, 21**; `Round N REJECTED` — **11, 17, 22**. Every admitted or
  rejected loop round has a lesson. Round 13 (skipped) has none; round 14 has
  a lesson whose LOG record is an integration-checkpoint heading
  (`LOG.md:3090`, `### 2026-10-17 — Round 14 integration…`), which the
  admitted/rejected regexes do not match by design — a record-shape fact, not
  a contradiction.
- `round_23_lessons: ["round-23.md"]`; `round_23_mentioned_in_log: false`.
  Under `AGENTS.md`, shared LOG integration belongs to the parent after the
  batch — the probe moving to true is the parent's act, not this seat's.
- `corpus/README.md` sha256 at stamp: `1a359d55387eef1aebd79316a7bf19d53a2ac6f0bcacb1cd109bdeff1294e7ce`
  (recorded for later byte-comparison; the README's knowledge-partition counts
  are the coverage auditor's surface, not this one).

## 3. Findings

### X09-1 — the round-23 lesson landed inside the audit window (finding)

The first `ls corpus/lessons/*.md | wc -l` at **15:09:29Z** read **23**; the
census at **15:10:58Z** read **24** with `round-23.md` present (mtime
**15:09:13.963905Z** — landed between the two observations, while this seat
was surveying). Pinned row: sha256
`b567a60acd09e19469af8331e7a385daaf8406ab342178ef06db09d00af56c3f`,
14179 bytes, 51 lines, all four contract lines + Gate present.

- The lesson is **contract-complete** and sets the round's acceptance boundary
  (axes O and D pending at its own stamp; closeout rules and rejected readings
  declared). It cites this round's tooling family and this audit's emerging
  artifacts; both sides measured a moving wave — its `Status at the opening
  stamp` names `reports/round-23/integration/` appearing during *its* survey,
  and this census caught the lesson landing during *ours*.
- Its **one unresolved path ref** is `reports/round-23/run-validation.py` —
  the counting command both claims declare, not yet written at 15:11:53Z. That
  is the documented **pending** class, not a stale reference: the resolver is
  literal by contract, and the lesson's own `recheck:` line declares the
  poll discipline (60 s interval, 15-minute bound). Contrast with the
  round-20 lesson, which wrote its then-pending runner *unbackticked* to keep
  it out of this census; X01's round-23 lesson chose to backtick it and accept
  the pending flag. Both behaviors are documented; neither is a defect. The
  flag clears when the runner lands — exactly as round-19's backticked
  `reports/round-19/validation.json` ref cleared after landing (see X09-2).

### X09-2 — path sweep: 12 unresolved refs, 11 historical + 1 pending (finding)

Sweep over all 24 lessons at 15:11:17Z: **399** distinct backticked repo refs,
**12** unresolved.

| lesson | unresolved ref | class |
|---|---|---|
| `round-9.md` | `reports/round-9/rerun.json` | historical (never written under that name) |
| `round-11.md` | `examples/culture-d2/typed-gate.expected.json`; `tools/typed-gate-flow.py` | historical (superseded / never landed) |
| `round-14.md` | `reports/round-12/adjacency/entries.md` | historical (round-12 layout differs) |
| `round-15.md` | `reports/round-15/handoff/packet-v2.yml`; `tools/build-handoff-v2.py` | historical (live file is `packet-v2-05.yml`) |
| `round-17.md` | `reports/round-17/civ-map.json` | historical (civ output under `reports/round-17/civ/`) |
| `round-18.md` | `reports/round-18/repin/MANIFEST.tsv`; `tools/gates/frozen/round-18-repin/MANIFEST.tsv` | historical (manifest path differs) |
| `round-19.md` | `corpus/lessons/round-19-d4-craft.md`; `reports/round-19/entries/R19-C1x.md` | aspirational (proposed path / glob) |
| `round-23.md` | `reports/round-23/run-validation.py` | **pending** (declared counting command, not yet written) |

Continuity control: this is byte-for-byte the same historical set the round-19
lessons audit recorded (`reports/round-19/audit/x28-lessons-audit.md` §X28-2),
with one demonstrated difference in the right direction — round-19's third
entry, `reports/round-19/validation.json`, **no longer appears** because the
runner landed and the pending ref cleared. Rounds 20–22 read **zero missing**:
their then-pending refs resolved after landing, and no filed lesson has rotted
since. All 11 historical rows live in filed lessons of rounds 8–19, which are
read-only; per the lane's rule their resolutions are carried in dated records
(round-19's audit did this), never by editing filed bytes.

### X09-3 — live-wave environment observations (recorded, not adjudicated)

- At all three stamps (**15:09:29Z**, **15:10:58Z**, **15:11:53Z**),
  `git status --porcelain` showed ` M reports/round-22/fixes/regression.md`,
  `git diff --stat` reading **+122/−54** — an in-place rewrite of a file
  committed in the round-22 close `0e81d9d`, visible while the wave ran.
  The round-23 lesson's own §"Dated observations" (X01, 15:06:46Z) records the
  same modification and declines to adjudicate it; this seat **corroborates it
  as a second independent observer** and likewise decides nothing. The
  decision point remains the parent's closeout protection check
  (`git diff --exit-code -- reports/round-{8..22}`), and the file must be
  re-read at its final revision before any round-23 admission quotes it.
- `reports/round-23/integration/` (R23-D04's fragment ledger, census
  15:08:18Z) and `reports/round-23/scope.md` appeared during the window;
  `reports/round-23/run-validation.py` was still absent at 15:11:53Z. Per the
  claims and the lesson's recheck line: a missing dependency is **pending, not
  green**; O and D are not verifiable from this seat.
- No validator was executed, no receipt refreshed, no scratch write made by
  this seat beyond `export TMPDIR=$PWD/.scratch` as a guard on the shell.

## 4. Cross-reference

- The round-23 lesson (`corpus/lessons/round-23.md`, pinned `b567a60a…`) is
  the gate-keeper survey this audit censuses; its acceptance boundary
  (wording disposition vs weakening; successor pins vs inheritance; landed
  rule vs repair) is the reading this audit's §2 Gate-shape and pending-ref
  notes must not be confused with.
- `reports/round-23/integration/fragment-ledger.md` (R23-D04) is the same
  wave's fragment index; it indexes this audit's files read-time. No conflict:
  different artifacts, one census each, both stamped.
- Round-19 continuity: `reports/round-19/audit/x28-lessons-audit.md` §X28-2 —
  the historical missing-ref set this audit reproduces unchanged.

## 5. Limits

- This is a structural, contract-shape and path-resolution audit. It does not
  re-execute any lesson's census commands, does not re-verify any lesson's
  domain claims, does not adjudicate prose correctness, and does not run any
  round validator.
- Gate-shape readings bind to the receipt stamp 15:11:17Z; the partition is a
  live wave surface and any later re-read is a new measurement (the round-23
  lesson itself proved this by landing mid-window).
- Counts are point-in-time (2026-10-18) and are re-measured, never inherited,
  before being quoted. This audit admits nothing and grants no promotion.
