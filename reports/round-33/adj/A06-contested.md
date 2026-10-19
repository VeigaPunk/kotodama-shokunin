- Seat: A06 | executor | claim A (adjacency) | date 2026-10-19 | baseline 139e3b6

# Round 33 — contested-scope posture (A06)

- **Mission:** restate the contested-scope items with current pointers and
  confirm nothing in round-33 work absorbs them.
- **Write scope:** this file only (`reports/round-33/adj/A06-contested.md`).
  No git commit/push, no filed-round bytes touched, no corpus or gate edits,
  no fleet `.ufo/**` write. Scratch via `TMPDIR=$PWD/.scratch`,
  `PYTHONDONTWRITEBYTECODE=1`. All commands below are read-only.
- **Cut:** round-33 tree at lane HEAD `139e3b662900557afe54f632b468619593dc9fcb`
  (baseline declared in `reports/round-33/claims.json:5`), observations stamped
  **2026-10-19T03:55–04:04Z** (the tree kept growing during the run; every count
  below carries its own stamp).
- **Standing rule applied:** `AGENTS.md:13` ("reports contested scope instead of
  absorbing it") and `PROVINCE.md:25` ("Contested scope → report to the
  integrator, never absorb"), `PROVINCE.md:31` ("Out of province → report,
  never absorb"). This seat decides nothing, closes nothing, and clears nothing.

## Verdict

**CONTESTED-SCOPE POSTURE RESTATED — ROUTED, NOT ABSORBED.** Two lore/integrator-owned
items plus one operator-gated item are restated below with pointers re-verified at
the round-33 cut. Every round-33 artifact that mentions them does so as a
routed-not-absorbed statement or a negation; **no round-33 artifact closes,
ratifies, clears, or absorbs any of them** (§2 scan, §7 limits). No scope
correction is proposed by this seat.

## 1. Contested items, restated with current pointers

| # | item | current status | current pointers (re-verified at this cut) | owner / route |
|---|---|---|---|---|
| CS-1 | **Contract §1 bilateral same-revision read** (the `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer` record each lane must file before a transfer) | **pending** — "Initial bilateral acknowledgement is **pending** until those records exist; writing this file is not a substitute for lore's read" | contract `corpus/knowledge/synthesis/worldbible-integration-contract.md:14-15` (gate + pending), `:16` (later-transfer re-read rule), `:127` (§8 step 2: "Both lanes satisfy §1's same-revision read gate"), `:150` ("bilateral acknowledgement is still required"), `:209` (division of labor); packet-side record still pending at `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`; earlier packet instances `reports/round-20/handoff/packet-v3-16.md:13,305,311` and `reports/round-15/handoff/contract-v2-audit.md:31,48`; lane question rows `corpus/lessons/README.md:154` (Q-02-3, owner `operator`, open) and `:155` (Q-02-4, owner `parent`, open); disposition ledger `reports/round-26/open-questions/dispositions.json` rows `Q-02-3`, `OQ-E2E-02`, `OQ-V3-01`, `OQ-V3-03` (all `carried`, reason "lore-owned; bilateral" / "cannot be closed unilaterally") | **lore + both lanes** (kotodama orchestrator for its own read record); routed via the fleet L0 queue `.ufo/l0-questions.md:44` (kotodama \| round-2). Not kotodama's to close |
| CS-2 | **L0 contract-digest ratification** (round-8 digest drift vs lore's open round-93 ratification: who owns the digest update, and whether lore's r93 subsumes it) | **open** — no ruling on record; the L0 row is unchanged | fleet L0 row `.ufo/l0-questions.md:45` (kotodama \| round-8, evidence `reports/round-8/adjacency.md`); escalation and the `50c4c2f2… -> 5f4c02bf…` hash chain at `reports/round-8/adjacency.md:125-131` ("2.4 Escalation to the orchestrator (report, not absorbed)"), `:134`, `:153`, `:299`; the two-orchestrator options (accept as documented PATCH vs revert + revision bump) are stated at `:139-153`; live digest re-measured this cut = `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (28421 bytes, 209 lines), unchanged since commit `e1694ba` (2026-10-17T17:44:17-03:00); disposition row `reports/round-26/open-questions/dispositions.json` `OQ-V3-02` (`carried`, owner `integrator/lore`, non-blocking); restated as standing debt at `reports/round-32/dossier-d13-operator-decisions.md:135` and `reports/round-32/final-dossier.md:109` | **integrator / lore**; routed via L0 row `:45`. Round 33 does not answer it |
| CS-3 | **Freshness-threshold recalibration** (operator ruling; the axis-move pause rides on it) | **open** — pause in force; round 33 declares no freshness axis-move | fleet L0 row `.ufo/l0-questions.md:47` (kotodama \| round-11, "Freshness axis-move claims are paused until ruled"); pause recorded `reports/round-33/claims.json:18` (`freshness_pause_in_force: true`) and `REGIMEN.md` ("Freshness axis-move claims stay paused … unless the operator lifts the pause") | **operator**; routed via L0 row `:47`. Declared as a non-goal at `reports/round-33/claims.json:68` |

Notes on the pointers above:

- The three items are the ones the round-33 method scout independently enumerated
  for this seat (`reports/round-33/adj/K04-method-scout.md:253-257`), and the
  round-33 claim A requirement itself restates them as routed-not-absorbed
  (`reports/round-33/claims.json:59`).
- The contract's own arbitration route is on record and unchanged:
  `worldbible-integration-contract.md:148` (integrator ruling where contested),
  `:165` (both lanes claiming ownership → report to the fleet integrator),
  `:170-172` (scope-report fields; re-flag if no ruling by the next completed
  round; "Silence, elapsed time, first authorship, and a passing local check
  never award scope"), `:171` (scope ruling vs canon ruling are distinct).
- Contract revision remains `1.0.0`; this seat asserts no revision bump and no
  canon standing for any artifact (`:12`, `:129` "Submission, delivery, and
  silence are never acceptance").

## 2. Non-absorption confirmation for round-33 work

**Scan (pre-write, 2026-10-19T03:57:16Z).** Command and date:

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
date -u '+OBS_UTC=%Y-%m-%dT%H:%M:%SZ'
grep -rn -i -E "bilateral (same-revision )?read (is|as) (closed|complete|done|acknowledged)|ratif(y|ied|ication)[^a-z]" reports/round-33/
```

Hits (exit 0), each read in full and dispositioned. These are the five sources
present at **03:57:16Z**; peer fragments have been rewritten since, so the
current line numbers are given in parentheses where they moved:

| hit | what it says | verdict |
|---|---|---|
| `reports/round-33/calib/C16-receipt.md:69` (unchanged) | C-09 row: "**not this lane's to fix** — contested scope, routed-not-absorbed (AGENTS.md); disposition must be carried-with-owner=lore" | routed-not-absorbed |
| `reports/round-33/calib/K03-open-items.md:70` (unchanged) | OI-09 row: "lore-owned — L0 contract-digest ratification … lore-owned-routing" | routed-not-absorbed |
| `reports/round-33/adj/A10-receipt.md:30` (now `:44`) | A06 row (then pre-drafted, now fragment-backed): restates both items as routed, "Nothing in round 33 absorbs any of the three" | routed-not-absorbed |
| `reports/round-33/adj/A15-audit-draft.md:200,202,206` (now `:239-240`, row at `:38`) | audit-draft contested-posture section, quoting the items and the D13 row | routed-not-absorbed |
| `reports/round-33/adj/K04-method-scout.md:256` (unchanged) | "all routed-not-absorbed" | routed-not-absorbed |

**No hit asserts a completed bilateral read, a ratification, or an ownership
transfer.** The wider language scan over the same tree
(`grep -rn -i -E "\b(canon(ized|ical)?|clearance|promotion|promote|closure)\b" reports/round-33/`
→ 152 lines at the same stamp) resolves, on inspection of the sampled hits, to
mission text, negations, and routed references — e.g.
`reports/round-33/adj/A16-shonen-material.md:161` ("round 33 awards no
promotion, canon, clearance or closure verdict") and
`reports/round-33/adj/A01-province.md:70` ("routed, not absorbed — PASS"); the
full language verdict belongs to A08 and the assembled audit, not to this seat.

**Post-write re-scan (2026-10-19T04:01:21Z).** Re-run after this file landed —
and, unavoidably, after further peer fragments landed too: the round-33 tree grew
from 24 files at 03:57:16Z to 50 files at 04:01:07Z while this seat worked, so the
post-write counts are snapshot values over a moving tree, not an isolated
before/after of this file. Commands and measured output:

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
date -u '+OBS_UTC=%Y-%m-%dT%H:%M:%SZ'                                        # 2026-10-19T04:01:21Z
grep -rn -i -E "bilateral (same-revision )?read (is|as) (closed|complete|done|acknowledged)|ratif(y|ied|ication)[^a-z]" reports/round-33/ > .scratch/a06/scanA.txt
wc -l < .scratch/a06/scanA.txt                                               # 23
grep -rn -i -E "\b(canon(ized|ical)?|clearance|promotion|promote|closure)\b" reports/round-33/ | wc -l        # 335
grep -rn -i -E "\b(canon(ized|ical)?|clearance|promotion|promote|closure)\b" reports/round-33/ | grep -v "A06-contested.md" | wc -l   # 324
```

Of the **23** absorption-pattern lines, exactly **3** are this file's own
(`:33` the CS-2 row, status `open`; `:68` a quoted K03 row; `:73` the negation
sentence). The other **20** sit in peer fragments — `calib/C08-item-08.md:177`,
`calib/C11-item-11.md:25`, `calib/C14-fix-drafts.md:391`, `calib/C16-receipt.md:69`,
`calib/K03-open-items.md:70`, `adj/A04-bleed.md:76,87,90`, `adj/A10-receipt.md:44`,
`adj/A12-verify-a04-a06.md:30,36,42,85,87`, `adj/A15-audit-draft.md:239,240`,
`adj/K04-method-scout.md:256`, `review/R04-calib-review.md:78`,
`review/R07-adj-review.md:207`, `scribe/S02-calib-receipt.md:75` — and every one of
the 23 was inspected: each names the items as `pending`, `open`, `lore-owned`,
`routed` or `owed`, and **none asserts a completed read, a ratification, or an
ownership transfer.** This file's **11** language-scan lines
(`:47,49,75,79,91,97,105,109,159,193,227`) are contract quotations, quoted scan
commands, routed/operator-owned references, and negations — **this seat added no
absorption claim and no affirmative promotion/canon/clearance/closure language to
the round-33 tree** (335 − 324 = 11, all accounted for above).

**Independent corroboration (non-author).** Verifier A12 executed this check
class itself at 2026-10-19T03:54:34Z and 03:56:17Z, before this fragment existed,
and reached the same verdict on the same three items with the same live digest
(`reports/round-33/adj/A12-verify-a04-a06.md:22-46,83-88`). Its run is an
independent measurement, not a re-run of the commands above; the two agreeing is
the strongest evidence available at this cut. A10's receipt row for this seat now
reads "RESTATED — ROUTED, NOT ABSORBED; one stale-pointer finding —
fragment-backed" (`reports/round-33/adj/A10-receipt.md:44`).

**Verdict:** zero round-33 absorption observed at the recorded instants. The two
lore-owned items stay with lore/the integrator and the freshness item stays with
the operator.

## 3. Adjacent-but-distinct routed items (named, not claimed as contested scope)

- **Promotion of the lane (SHONEN marks)** — operator-owned, not contested scope.
  Restated on record at `reports/round-32/dossier-d13-operator-decisions.md`
  Decision 1 (`:19-56` region) with the unmet `[x]` conditions; the r32 close
  routed it to the operator (`SCORECARD.md:443`, "Routed debt recorded for the
  operator"). Round 33 declares no promotion verdict
  (`reports/round-33/claims.json:68`). No action by this seat.
- **Round-32 routed operability/calibration debt** (falsifier filename mismatch,
  7 unindexed lessons, 12 standing open items) is this round's claims O and C
  (`reports/round-33/claims.json:26-52`) and is owned by the O/C seats, not by
  the contested-scope posture. Named here only so the audit's contested section
  is not read as covering them.
- **`A21-D4-XF-01`** (the round-21 filed D4 fixture-bleed finding) and
  **`A29-ADJ-EVID-01`** (round-29 evidence defect) remain filed findings with
  their own owners; this seat neither re-evaluates nor closes them
  (`reports/round-29/adjacency/A09-A12-handoff.md`, "Disposition and limits").

## 4. Stale-pointer finding (reported, not fixed by any seat)

Several **non-filed, lane-owned example surfaces still cite the superseded
contract digest** `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1`:

- `examples/handoff-packet.sample.md:21` (`contract_ref` row),
- `examples/handoff-packet.sample.yml:45,78`,
- `examples/culture-d3/handoff.md:27,74`.

The live contract digest is `5f4c02bf…` and has been since commit `e1694ba`
(2026-10-17); the supersession chain is on record at
`reports/round-8/adjacency.md:125-128`, and the later packet generations
re-measured and pinned the current digest (`reports/round-15/handoff/contract-v2-audit.md:31`,
`reports/round-20/handoff/packet-v3-16.md:13`,
`reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`). The `examples/` paths
are not filed-round bytes and not this seat's write scope: **recorded as a
finding for the integrator/example owner**, not repaired here. It is a pointer
staleness, not evidence that any lane accepted a superseded pin — no transfer
has occurred, so no lane holds a stale *accepted* pin
(`reports/round-8/adjacency.md:145-149`).

## 5. Boundary notes for the assembled audit

- **This seat's footprint:** one new file under `reports/round-33/adj/`. No
  other path was written by this seat; `git status --porcelain=v1 -uall` at
  2026-10-19T03:57:30Z showed, outside the round-33 tree, only ` M LOG.md` and
  `?? REGIMEN.md` (integrator-owned append/declaration surfaces), plus the
  round-33 seat fragments. At an earlier observation in the same session
  (2026-10-19T03:5xZ) ` M reports/round-5/validation.json` and
  ` M reports/round-7/validation.json` also appeared; they were absent from the
  03:57:30Z read. This seat did not write, revert or stage any of those paths —
  recorded here as an observed transient for the scope watch (A03) and the
  verifiers, with no attribution claimed.
- **Fleet L0 surface untouched by this round:** `.ufo/l0-questions.md`
  sha256 `60ccdc9e9a0a7179d97d82349a34e0cc53f1520c6f69c6db624f4f72beac51a6`,
  mtime `2026-10-18 17:14:10.592827730 -0300` (pre-round), 49 lines, four
  kotodama rows (`:44`, `:45`, `:46`, `:47`) — none added, edited or resolved.
  Read-only access only; this seat holds no fleet write scope.
- **No canon/clearance/closure language** is added by this file; the CS rows
  carry only `pending`/`open` statuses and the contract's own routing clauses.

## 6. Re-check commands (for A12 and any later verifier)

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# (1) live contract digest + revision (expect 5f4c02bf…)
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md
git log -1 --format='%H %cI %s' -- corpus/knowledge/synthesis/worldbible-integration-contract.md   # expect e1694ba…
# (2) §1 pending clause + routing clauses still at the cited lines
sed -n '14,16p;127p;148p;150p;165p;209p' corpus/knowledge/synthesis/worldbible-integration-contract.md
# (3) L0 rows still open and unmodified
sha256sum /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md   # expect 60ccdc9e…
sed -n '44,47p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
# (4) packet-side record still pending
sed -n '14p' reports/round-28/pinsweep/v3-baseline-r28/packet.md
# (5) non-absorption re-scan over the whole round-33 tree
grep -rn -i -E "bilateral (same-revision )?read (is|as) (closed|complete|done|acknowledged)|ratif(y|ied|ication)[^a-z]" reports/round-33/
# (6) stale example pointers still present (finding §4, unrepaired)
grep -rn "50c4c2f2" examples/handoff-packet.sample.md examples/handoff-packet.sample.yml examples/culture-d3/handoff.md
```

A12 independently re-running these and getting different output should file the
defect against this fragment rather than adjust the verdict.

## 7. Limits

- Snapshot-bounded: the non-absorption result covers the recorded instants and
  the paths present then; it cannot prove no write-and-restore occurred between
  samples, and it does not audit sibling repositories, the world bible, or
  lore-side surfaces (none were read).
- The round-33 tree was still being written by peer seats throughout this seat's
  run (24 files at 03:57:16Z → 50 at 04:01:07Z). Every count in §2 is therefore a
  stamped snapshot over a moving tree, and the post-write figures reflect
  concurrent landings by other seats, not only this file. Peer fragment line
  numbers cited here were re-checked at the last read; a verifier finding one
  moved should treat the quoted text as the citation of record.
- The verdict is a scope/routing posture, not round acceptance, not a semantic
  review of peer claims O/C, not a canon or rights ruling, and not a promotion
  verdict. A12's independent agreement (§2) is corroboration of the measurements
  above, not a second promotion or closure verdict.
- Pointer staleness in §4 is measured against the live digest; whether the
  example owner prefers a re-pin or a note is the integrator's call.
- This seat authored no filed-round byte and applied no fix; the §4 finding and
  the CS-1/CS-2 routing are for the integrator, lore, and the operator.

## Owed

none

## Citations

Paths (all read-only at 2026-10-19T03:55–04:02Z unless a commit is named; peer
fragment line numbers are as of the last read and several moved mid-round):

- `reports/round-33/claims.json:5,18,26-52,59,68`; `reports/round-33/targets.json` (A06 seat object, shared rules); `reports/round-33/telemetry/dispatch-declared.json`
- `reports/round-33/adj/K04-method-scout.md:253-257`; `reports/round-33/adj/A10-receipt.md:44` (A06 row; was `:30` when first read); `reports/round-33/adj/A15-audit-draft.md:36,168-169` (check-table row 7 and the contested-posture section; were `:38,239-240` at first read and `:31,200-206` before that); `reports/round-33/adj/A16-shonen-material.md:161` (was `:160`); `reports/round-33/adj/A01-province.md:70,154`
- `reports/round-33/adj/A12-verify-a04-a06.md:22-46,83-88` (independent run of this check class, pre-dating this fragment); `reports/round-33/adj/A04-bleed.md:76,87,90`
- Status of the peer rows that point at this seat at the last read (2026-10-19T04:03Z): A10's row is fragment-backed (`A10-receipt.md:44`); A15's check-table row 7 still reads `owed | provisional GREEN (A10 row)` (`A15-audit-draft.md:36`) and its A12 row reads `pending` (`:42`) — flipping those is the A15/integrator's call, not this seat's
- `reports/round-33/calib/K03-open-items.md:69-70`; `reports/round-33/calib/C16-receipt.md:69,102`; `reports/round-33/calib/C08-item-08.md:177`; `reports/round-33/calib/C11-item-11.md:25`; `reports/round-33/calib/C14-fix-drafts.md:391`; `reports/round-33/op/O01-row-drafts.md:124,224`; `reports/round-33/review/R04-calib-review.md:78`; `reports/round-33/review/R07-adj-review.md:207`; `reports/round-33/scribe/S02-calib-receipt.md:75`
- `PROVINCE.md:22-25,31`; `AGENTS.md:13`; `REGIMEN.md` (freshness pause clause, per-round contract)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:11-19,126-129,148-151,163-172,205-209`
- `corpus/lessons/README.md:154-155`
- `reports/round-26/open-questions/dispositions.json` rows `Q-02-3`, `Q-02-4`, `OQ-E2E-02`, `OQ-V3-01`, `OQ-V3-02`, `OQ-V3-03`
- `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`; `reports/round-20/handoff/packet-v3-16.md:13,305,311`; `reports/round-15/handoff/contract-v2-audit.md:31,48`; `reports/round-11/handoff/packet.md:12,142`
- `reports/round-8/adjacency.md:125-131,134,139-153,299`; `reports/round-29/adjacency/A09-A12-handoff.md` (disposition and limits)
- `reports/round-32/dossier-d13-operator-decisions.md:15-71,135`; `reports/round-32/final-dossier.md:108-110`; `SCORECARD.md:443`
- `examples/handoff-packet.sample.md:21`; `examples/handoff-packet.sample.yml:45,78`; `examples/culture-d3/handoff.md:27,74`
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45,46,47` (fleet, read-only)

Commands / measured values:

- `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (28421 bytes, 209 lines)
- `git log -1 --format='%H %cI %s' -- corpus/knowledge/synthesis/worldbible-integration-contract.md` → `e1694bad6ac96aca45a11ca5746582b275929355 2026-10-17T17:44:17-03:00 round-8: admit F/O/D …`
- `sha256sum /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → `60ccdc9e9a0a7179d97d82349a34e0cc53f1520c6f69c6db624f4f72beac51a6`; `stat -c '%y'` → `2026-10-18 17:14:10.592827730 -0300`; `wc -l` → 49
- `sha256sum PROVINCE.md` → `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`; `AGENTS.md` → `1afaf106f20b440ad263ab231c215773436c7f42ab106848f5550b87ecf41035`
- `git log -1 --format='%H'` → `139e3b662900557afe54f632b468619593dc9fcb`; `git status --porcelain=v1 -uall` (03:57:30Z) → ` M LOG.md`, `?? REGIMEN.md`, plus round-33 fragments
- `grep -rn -i -E "bilateral (same-revision )?read (is|as) (closed|complete|done|acknowledged)|ratif(y|ied|ication)[^a-z]" reports/round-33/` → **5** lines at 2026-10-19T03:57:16Z; **23** lines at 04:01:21Z (raw output kept at `.scratch/a06/scanA.txt` during this seat's run), of which **3** are this file's own and **20** are peer fragments — all routed/negation/pending
- `grep -rn -i -E "\b(canon(ized|ical)?|clearance|promotion|promote|closure)\b" reports/round-33/ | wc -l` → `152` at 03:57:16Z; `335` at 04:01:21Z including this file, `324` excluding it (this file's 11 matching lines are quotations, quoted commands, routed references and negations)
- `find reports/round-33 -type f | wc -l` → **24** files at 03:57:16Z, **50** at 04:01:07Z (the tree grew while this seat worked; every count above is a snapshot, not a stable invariant)
- `sha256sum reports/round-33/adj/A06-contested.md` → `79da93b812d36519362791bc3f4b183d5b53897b8a2e7b6472fb9f64e508ed2b` (267 lines, at the 2026-10-19T04:03:54Z read; the `0327d8b9…` value measured at 04:01:07Z is this same file before the §2/§7 accuracy corrections, recorded here so the two readings are not confused)
- `grep -rn "50c4c2f2" examples/handoff-packet.sample.md examples/handoff-packet.sample.yml examples/culture-d3/handoff.md` → 1 + 2 + 2 hits, re-confirmed 2026-10-19T04:03:54Z (finding §4 still open)
