# R25-X48 — shard audit: the v3 supersession prose diffs

- Seat **R25-X48** (SCRIBE X48: shard auditor — v3 supersession prose diffs).
  Round 25 (operator: loop 3 of 3, build 1 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` — `reports/round-25/targets.json`).
- Date: **2026-10-18**. Counts carry command and date; raw receipts in
  `.scratch/r25-x48/` (gitignored); only this fragment is filed.
- Declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`; lane HEAD
  `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope: this fragment and `reports/round-25/audit/x48-v3-supersession-audit.py`
  only.** No filed round-8–24 byte is edited; no source or gate is changed; no
  Git mutation. NON-CANON engineering evidence.

## What this shard audits

The claim's before-clause (b): handoff v3 carries stale D4 claim prose — the
verbatim/supersession distinction is unresolved. This seat **measures** the
delta instead of asserting it: for each stale claim row, whether the prose
*asserts* a stale number as present, asserts the live number, or names the old
number as **removed**.

The seat's tool is `reports/round-25/audit/x48-v3-supersession-audit.py`
(stdlib only; `--selftest` **14/14** controls, exit 0).

## R25-X48-1 — the live present state (the comparator)

Measured 2026-10-18 from the delivered bytes:

| surface | live value |
|---|---|
| `examples/culture-d4/expected-holds.json#counts` | `{hold: 12, note: 0, fail: 0}` |
| `typed-labels.d4.yml#coverage.typed_labels` | 74 |
| `…#coverage.labels_by_kind` | native-form 56 / translated-label 12 / borrowed-strata 6 |
| `…#coverage.findings_total` | **12** |
| `…#coverage.findings_hold_or_fail` | **12** |
| `…#coverage.label_findings_fail` | 0 |
| `…#coverage.conflicts` | **0** |
| `…#coverage.rank_rules_unresolved_items` | **0** |
| `…#coverage.rank_quarantine_handles` | **0** |
| `…#coverage.reconciliation_records` | 6 |

Digests: `typed-labels.d4.yml` = `60b526b0b3d07141…`,
`expected-holds.json` = `3826ba68d705b3c3…`. There is **no `stats` block** in
the projection; the stale rows cite one (`typed-labels.d4.yml#stats (fail 0,
hold 12, labels 74)`) that the delivered file does not carry. The post-fix state
is exactly the round-22 family-clean delta: 12 form holds, 0 notes, 0 rank
findings, 0 conflicts.

## R25-X48-2 — the supersession-aware census

The audit distinguishes three row states, because a corrected row still
*contains* the old numbers:

- **stale** — the row asserts the old value as present;
- **corrected** — the row asserts the live value, **or** names the old value as
  removed/superseded (markers: `no longer D4-owned`, `removed from D4
  ownership`, `pre-family-clean generation`, `stay open in D2`, `are D2-owned`,
  `superseded for D4 ownership`, …).

| revision | sha256 | stale assertions |
|---|---|---|
| `reports/round-20/handoff/packet.md` | `e92f5e6775b657c2…` | **8** |
| `reports/round-22/handoff/declared-in/packet.md` | `ba3d0deed2b0dfea…` | **8** |
| `reports/round-22/handoff/declared-in-r2/packet.md` | `a97a0f0a0a497cb4…` | **8** |
| `reports/round-23/wording/declared-in-r3/packet.md` | `084dc5db9a8d923b…` | **8** |
| `reports/round-25/v3-supersession/declared-in-r4/packet.md` | `5f58db4a52b68856…` | **0** |

The eight in the four pre-r4 revisions, with both values named:

| claim | asserts | asserted | live |
|---|---|---|---|
| D4-CL05 | `findings_total` | 16 | **12** |
| D4-CL05 | `findings_hold_or_fail` | 15 | **12** |
| D4-CL06 | `counts.hold` | 15 | **12** |
| D4-CL06 | `counts.note` | 1 | **0** |
| D4-CL07 | `coverage.conflicts` | 4 | **0** |
| D4-CL09 | `rank_rules_unresolved_items` | 13 | **0** |
| D4-CL09 | `rank_quarantine_handles` | 3 | **0** |
| OQ-V3-05 | rank passengers | 13 | **0** |

This seat's census agrees with `reports/round-22/bleed/repin.md` §"Additional
handoff content dependency" (which first reported the defect) and with
`SKILL.md:340-341` (which commits round 25 to the superseding map).

## R25-X48-3 — the supersession chain, and the successor that corrects it

| revision | D4-CL05 | D4-CL06 | D4-CL07 | D4-CL09 | OQ-V3-05 |
|---|---|---|---|---|---|
| r20 packet | stale | stale | stale | stale | stale |
| r22 declared-in | stale | stale | stale | stale | stale |
| r22 declared-in-r2 | stale | stale | stale | stale | stale |
| r23 declared-in-r3 | stale | stale | stale | stale | stale |
| **r25 declared-in-r4** | **corrected** | **corrected** | **corrected** | **corrected** | **corrected** |

The round-23 wording revision is a **supersession of D4-CL08 only** (its
`unchanged-foreign-path` basis reworded); it copied the four stale rows and
`OQ-V3-05` forward verbatim. So the pre-r4 chain has three successors and
**zero** corrections of the rank-passenger prose.

**The round-25 r4 successor (`declared-in-r4`) corrects all five lines.** This
seat verified the corrected text on the bytes, not on the header's claim:

- `D4-CL05` now reads `findings_total 12, findings_hold_or_fail 12,
  label_findings_hold 12, label_findings_fail 0, conflicts 0`.
- `D4-CL06` now reads `counts (hold 12, note 0, fail 0) … D2L-RANK population is
  zero`.
- `D4-CL07` now reads `six reconciliation records with zero conflicts and zero
  quarantine handles`.
- `D4-CL09` now reads `zero unresolved rank items, zero quarantine handles and
  zero conflicts`, and names the old numbers as removed: "the thirteen
  unresolved rank items … the pre-family-clean generation inherited are no
  longer D4-owned and were not resolved in D2, where they stay open (OQ-V2-03)".
- `OQ-V3-05` now reads "twelve form holds, zero rank holds, zero notes and zero
  fails; the thirteen unresolved rank items … are D2-owned residuals, removed
  from D4 ownership by the round-22 family-clean repair and still open in D2
  (OQ-V2-03)".

The r4 revision also re-points the surviving D2 residual to its **correct**
carrier: the thirteen items / three handles / four conflicts are D2-owned and
tracked by `OQ-V2-03`, not deleted. This is the honest form of the supersession
— the numbers are not erased, they are reassigned.

## R25-X48-4 — the passenger disposition, and the successor's own gaps

**Disposition: RESOLVED by `declared-in-r4`** — the first revision in the chain
with no stale claim row. `OQ-V3-05` is stale in the four pre-r4 revisions only.

Two gaps in the successor this seat measured, both worth the parent's attention:

1. **The declared companion script landed during this audit — and passes.** At
   the first measurement `reports/round-25/v3-supersession/v3-supersession-check.py`
   **did not exist**, so `declared-in-r4/expected.json`'s own counting command
   could not run. It has since landed (`29336` bytes, 14:35). This seat ran it in
   its own isolated clone
   (`python3 … --root .scratch/r25-x48/clone --check`, 2026-10-18T17:39:17Z):
   **exit 0, `passed: true`, 52/52 controls**, and its own stale-prose detector
   reports **13 parent hits (r3) / 0 revision hits (r4)** — an independent
   confirmation of this seat's census by a different method. The pinned
   `packet_sha256` (`5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03`)
   also re-verifies byte-for-byte against the landed packet.
2. **The successor lands packet-only, with no companion `twin.json`.** The r4
   directory holds `packet.md`, `expected.json` and `freeze.txt`; there is no
   `twin.json` alongside, unlike the r22 revisions. The round-23 r3 revision has
   the same gap. A v3 revision that changes claim prose should land the packet
   and its twin together, or the ledger surface stays unauditable for that
   revision. **This remainder stands.**

**One residual the successor does not close, named not hidden.** Its checker's
`positive` and `negative` runs both still carry the two *sibling* tails declared
open since round 23 — the stale combined-source v2 successor pin
(`reports/round-20/wart/expected-v2-07-r20.json`, `V2F-DIGEST: 1 pinned file(s)
changed since the freeze: tools/d2-typed-labels.py`) and the stale v3
packet-baseline pin (`reports/round-20/handoff/expected.json` pins
`e92f5e6775b6…` but the run assembles `a97a0f0a0a49…`). The r4 revision is a
**claim-prose** supersession and does not touch them; they are the
combined-source pin work, and the checker reports `passed: true` on its own
control set while surfacing them. The parent should read the r4 success as
"the stale D4 claim prose is superseded", not as "the v3 pin surface is green".

The r4 header states its own scope precisely — "exactly five ledger lines are
corrected … plus the declared-in-r4 provenance note after the renderer
paragraph; no other byte differs". This seat's `diff` against r3 confirms it:
**11 changed lines** (5 removed, 6 added — the five rows, the provenance note,
and one net line from the note's paragraph).

## Verdict of this seat (scoped)

**Eight stale assertions in each of the four pre-r4 filed revisions; the live
state is `hold 12 / note 0 / fail 0`, `findings_total 12`, `conflicts 0`,
`rank_rules_unresolved_items 0`; the round-23 wording successor corrected none
of them; and the round-25 successor `declared-in-r4` corrects all five lines,
reassigning the removed passengers to their true D2 carrier `OQ-V2-03` rather
than deleting them.** The claim's before-clause (b) is confirmed and quantified,
and its `after_required` — a superseding claim map re-pinned as a new revision —
**is met at this audit's stamp**, with three named remainders: the r4 checker
landed late but passes (52/52), the successor still lands without a companion
`twin.json`, and the two sibling pin tails remain open and untouched.

This is scribe evidence, not round admission; the parent owns integration and
the verdict.

## Limits and handoff

- The audit compares *asserted numbers in prose* to *live numbers on the
  referenced surface*. It does not judge whether the prose is otherwise
  well-formed, nor whether the live numbers are themselves correct — those are
  the D seats' and the runner's business.
- **The supersession detector is the load-bearing control.** Without it the
  audit would report r4 as stale (its corrected rows still contain the old
  numbers); the `--selftest` includes `removed-naming-row-not-stale` and
  `stale-row-has-no-removal-marker` to pin that behaviour in both directions.
- The audit is order-sensitive: `REVISIONS` lists the family oldest-first, and a
  revision landing after this stamp needs a dated refresh.
- Receipt: `.scratch/r25-x48/audit.json` (`--json`). Scratch
  `.scratch/r25-x48/stale-rows.json` holds the extracted pre-r4 stale rows
  verbatim.
- This seat did not edit any packet, twin, expected file, or filed round.
