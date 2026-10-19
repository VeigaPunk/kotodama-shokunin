# R31-D14 — jin'i-ryu patch draft: "freeze follows re-point"

**Status: DRAFT. The orchestrator lands this patch; this seat (R31-D14 worker)
wrote only this file and edited no operating file.**
Seat: D R31-D14 (round 31, loop 3, GLM round 1 of 2 — regimen close-out).
Date: 2026-10-18. Baseline at drafting: `71cd9d3` (round-30 admit baseline per
`reports/round-31/claims.json`); declaration commit `e8d2d0d` = lane HEAD.

## 1. Selection — which telemetry class, and why

`reports/round-31/claims.json` (claim D) names three candidate classes from
regimen telemetry: (a) the telemetry-persistence rule generalized, (b) the
"freeze follows re-point" pin discipline codified, (c) the mirror-safety
TMPDIR rule promoted to a checklist item.

**Chosen: (b), with (c) folded in as its executable premise.** Grounding:

- (c) is already codified twice — the prose rule at `SKILL.md:456-462` and the
  implemented guard (`tools/replay-frozen.py:172-182`, `mirror_unsafe` exit 2),
  re-measured today (§6, leg 1). A new row would duplicate existing text.
- (a) already exists as an AGENTS.md rule section; no measured failure of it
  surfaced this regimen.
- (b) is practiced only piecemeal and has **no operating-file rule anywhere**:
  `tools/gates/frozen/round-25/gate-input/freeze.txt` carries a hand-written
  cascade note (round-18/repin-d2, round-20/repin-d2, round-22/d4-repin,
  round-23/repin-d2: one refused row each), but the **next** cascade — the
  post-r25 edits to `tools/gates/typed-pipeline-gate.py` (r29/r30 defect
  fixes) — left the round-25 and round-26 generations red with **no
  disposition recorded anywhere** (§6 census). The routed defects
  `R28-FROZEN-REPLAY-USES-LIVE-TREE` and
  `R28-VALIDATION-CLAUSE-OMITS-FROZEN-MANIFEST-REPLAY`
  (`reports/round-29/defects/routed.md:75-81`, the latter already recording
  "11 of 12 manifest generations as nonzero" at r28) plus
  `reports/round-29/defects/fix-14.md` ("per-generation replay status is
  therefore **to-verify**, not claimed green") name the class but impose no
  same-round obligation. Meanwhile `SKILL.md:294` still asserts the r22
  d4-repin manifest replays "3 rows, exit 0" — falsified by today's
  measurement (§6): the lane's own SKILL.md carries a stale replay verdict.

The improvement: one executable checklist row that makes the cascade
disposition a same-round obligation with a runnable census, plus the
consistency erratum to the one evidence cell the census falsified.

## 2. Patch 1 (the improvement) — SKILL.md checklist row

**File:** `SKILL.md`. **Anchor:** in `## Checklist (executable where a tool
exists)`, insert after the row ending "`handoff-packet-check` enforces per
packet; no canon here." and before the blank line preceding `## Corpus map`
(`SKILL.md:535-536`). The anchor string `no canon here.` occurs exactly once
in `SKILL.md` (grep count 1, 2026-10-18). **Exact new text:**

```markdown
- [ ] Freeze follows re-point: a round that re-points any byte a frozen
      manifest pins (`tools/gates/frozen/**/MANIFEST.tsv` rows bind gate and
      input sha256) records a cascade disposition in the same round — in each
      affected generation's own `freeze.txt`, naming the affected generations
      and the restore-blob control or dated successor generation; filed
      manifests are never edited. Census (executable): replay every
      generation with `TMPDIR=$(mktemp -d) python3 -B tools/replay-frozen.py
      <MANIFEST.tsv> --json` (in-repo `TMPDIR` is refused `mirror_unsafe`
      exit 2) and match each non-reproduced row to a dated disposition or an
      open route — a red row with neither is a defect. Evidence cells citing
      replay verdicts keep their measurement stamp only until the next
      re-pin invalidates it, then read `to-verify`.
```

## 3. Patch 2 (consistency erratum, same single D move) — SKILL.md:294 cell

Leaving the stale cell in place while adding the row would make SKILL.md
self-contradicting. **File:** `SKILL.md`, the Propagation/tamper row of the
decision table. Replace the exact substring (occurs once, grep count 1,
2026-10-18):

```
frozen generation `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (3 rows, exit 0 — requires TMPDIR outside the repo, `mirror_unsafe` exit 2 otherwise, measured 2026-10-18 round-24 cold run; deployed replay 33 peer pairs, 2026-10-18T14:56:01Z)
```

with:

```
frozen generation `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (3 rows; replayed exit 0 at the 2026-10-18 round-24 cold run — requires TMPDIR outside the repo, `mirror_unsafe` exit 2 otherwise; deployed replay 33 peer pairs, 2026-10-18T14:56:01Z; re-measured 2026-10-18T22:46Z exit 2 = 2 `replay_mismatch` + 1 `gate_digest_mismatch` after the round-25 typed-pipeline re-pin cascade and the routed live-coupling class `R28-FROZEN-REPLAY-USES-LIVE-TREE` — status `to-verify` per `reports/round-29/defects/fix-14.md`; restore-blob control in `tools/gates/frozen/round-25/gate-input/freeze.txt`)
```

This is an erratum to a living operating file, not a rewrite of a filed round
receipt; the original verdict stays visible with its stamp.

## 4. LOG.md entry text (drafted for the orchestrator to append)

```markdown
## 2026-10-18 — Round 31 admitted (loop 3, GLM round 1 of 2 — regimen close-out)

- **Trigger:** regimen; claims C/O/D in `reports/round-31/claims.json`;
  baseline `71cd9d3`; <orchestrator fills completion counts>.
- **C (verified):** <closure-ledger outcome, orchestrator>.
- **O (verified):** <final-sweep outcome, orchestrator>.
- **D (jin'i-ryu self-improvement, landed):** SKILL.md checklist row "freeze
  follows re-point" — a round re-pointing bytes pinned by a frozen manifest
  owes a same-round cascade disposition in each affected generation's own
  `freeze.txt` (filed manifests never edited), with an executable census
  (`tools/replay-frozen.py` per generation, external TMPDIR); SKILL.md:294's
  r22 d4-repin cell re-stamped to `to-verify` (exit 0 at the round-24 cold
  run; re-measured exit 2 after the round-25 re-pin cascade + routed
  `R28-FROZEN-REPLAY-USES-LIVE-TREE`). Motivating census 2026-10-18T22:46Z:
  11/11 generations red, incl. r25 (0/6 `gate_digest_mismatch`) and r26 pair
  (4/6 each) with no recorded disposition. **Falsification condition:** (i)
  guard leg — an in-repo-TMPDIR replay that no longer refuses
  `mirror_unsafe` exit 2 breaks the row's executable premise → revert the
  row; (ii) vacuity leg — a census reporting zero disposition-owed rows on
  the motivating tree (measured: ≥9 owed rows) → the row is vacuous →
  revert; (iii) malformed-rule leg — if compliance ever requires editing a
  filed manifest (no freeze.txt/successor path suffices), the row
  contradicts itself → reword or revert. Non-compliance by a later round is
  not rule falsification: it fails that round's audit, the row stays.
- **Evidence:** `reports/round-31/jinii/patch-draft.md` (exact patches,
  census commands + stamps); `reports/round-31/validation.json` acceptance
  <orchestrator>.
```

## 5. Falsification condition (per the jin'i-ryu gate) — exact commands

All commands run from the lane root. Stamps are 2026-10-18 UTC.

1. **Guard leg** (premise must hold):
   `TMPDIR=$PWD/.scratch python3 -B tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv --json`
   must exit 2 with rows `could-not-evaluate` / `mirror_unsafe`.
   **Falsifies the row** if it exits 0 (guard gone).
   Measured 2026-10-18 (22:0xZ): exit 2, 3/3 rows `mirror_unsafe`
   ("temporary root is inside the repo").
2. **Vacuity leg** (the census must catch real violations): run the §2 census
   over all 11 `MANIFEST.tsv` generations with external `TMPDIR`. On the
   motivating tree it must report red rows **without** dispositions (measured
   §6: r25 6 rows, r26 pair 4 rows each, r18-original 2 rows — the r29/r30
   gate/packet moves are dispositioned nowhere in those generations'
   `freeze.txt` files). **Falsifies the row** if the census reports zero
   disposition-owed rows on this same tree.
3. **Malformed-rule leg** (compliance must be possible without rewriting
   history): the disposition path is `freeze.txt` notes and dated successor
   generations only — exactly what r25's note and the r18→r22 re-pin
   generations already did. **Falsifies the row** if a compliance case exists
   only via editing a filed `MANIFEST.tsv`/receipt.

A later round that re-points pinned bytes without a same-round disposition
fails that round's audit; that is enforcement, not falsification.

## 6. Measured evidence (commands + stamps; nothing reconstructed)

Census 2026-10-18T22:46:26Z–22:46:31Z,
`TMPDIR=$(mktemp -d /var/tmp/kotodama-r31-census.XXXXXX)`, for each
`$(find tools/gates/frozen -name MANIFEST.tsv | sort)` (11 total):
`python3 -B tools/replay-frozen.py <M> --json`:

| generation | exit | rows | reproduced | mismatch | could-not-evaluate | disposition status |
|---|---|---|---|---|---|---|
| round-3/attempt-1 | 2 | 7 | 0 | 0 | 7 (`gate_digest_mismatch`) | none recorded — owed |
| round-3 | 2 | 7 | 0 | 0 | 7 (`gate_digest_mismatch`) | none recorded — owed |
| round-11 | 2 | 11 | 10 | 0 | 1 (`gate_digest_mismatch`) | none recorded — owed |
| round-18 (original) | 1 | 2 | 0 | 2 (`replay_mismatch`) | 0 | none recorded — owed |
| round-18/repin-d2 | 2 | 11 | 10 | 0 | 1 (`gate_digest_mismatch`) | dispositioned by r25 `freeze.txt` cascade note |
| round-20/repin-d2 | 2 | 11 | 10 | 0 | 1 (`gate_digest_mismatch`) | dispositioned by r25 `freeze.txt` cascade note |
| round-22/d4-repin | 2 | 3 | 0 | 2 (`replay_mismatch`) | 1 (`gate_digest_mismatch`) | partially: r25 note covers the refused row; the 2 mismatches are the routed live-coupling class (`to-verify`, fix-14.md) |
| round-23/repin-d2 | 2 | 11 | 10 | 0 | 1 (`gate_digest_mismatch`) | dispositioned by r25 `freeze.txt` cascade note |
| round-25/gate-input | 2 | 6 | 0 | 0 | 6 (`gate_digest_mismatch`) | **none — the live violation** (its own `freeze.txt` observed 6/6 at 17:33Z; the later gate move is undispositioned) |
| round-26/gate-input | 1 | 6 | 4 | 2 (`replay_mismatch`) | 0 | classified stale-snapshot by fix-14.md A/B, replay isolation still routed |
| round-26/post-register | 1 | 6 | 4 | 2 (`replay_mismatch`) | 0 | same class (routed.md:77 measured it 2026-10-18) |

Guard leg 2026-10-18 (~22:0xZ):
`TMPDIR=$PWD/.scratch python3 -B tools/replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv --json`
→ exit 2, rows 2-4 all `could-not-evaluate` / `mirror_unsafe`
("mirror: temporary root is inside the repo: …/.scratch/replay-frozen-*").
External-`TMPDIR` counterpart → gates launch (rows classified, not refused).

Corroboration that the class predates today: r28's sweep already recorded
"11 of 12 manifest generations as nonzero"
(`reports/round-29/defects/routed.md:79-81`).

## 7. Cross-claim note for the orchestrator (D↔O interplay, no O files touched)

The O claim's final sweep is declared as "all validators + frozen replays —
100% exit 0". Today 11/11 frozen generations replay non-zero (§6). The sweep
cannot honestly record green replays; it should either scope its replay leg to
selftests + the dispositioned-refusal distinction this patch introduces, or
record the census with per-row reasons under the routed classes. Silence or a
green stamp here would be exactly the stale-verdict pattern Patch 2 repairs.

## 8. Non-goals

- No historical manifest, receipt, or filed-round artifact is edited; the
  patch adds an operating rule and re-stamps one living SKILL.md cell.
- Replay-tool isolation (`R28-FROZEN-REPLAY-USES-LIVE-TREE`) stays routed —
  this patch does not attempt to fix the tool, only to make freeze-lag visible
  and obligated.
- No canon, promotion-rank, or ownership claims; PROVINCE.md untouched.
