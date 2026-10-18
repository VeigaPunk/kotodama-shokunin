# R25-D24 — SCORECARD integration draft (proposed round-25 axes checkpoint)

Prepared **2026-10-18** by seat **R25-D24** (integration drafts, claim D).
Parent-owned append proposal only: this worker does not edit `SCORECARD.md`,
admit round 25, or change filed rounds 8–24. Statuses are parent-fill slots —
fill them only from a dated receipt of the declared counting command
(`python3 reports/round-25/run-validation.py`), never from fragment existence.

## Proposed SCORECARD append

### Round 25 — loop 3, build 1 of 4 (2026-10-18)

| axis | claimed before → required after | status | command/date and evidence |
|---|---|---|---|
| O operability | two round-24 cold-run hazards: (a) the typed-packet gate input exits 1 on a false red (nullish `routed_slots` guard + an unfaithful `yaml_lines` rebuild manufacturing `DERIV-REPLAY`); (b) handoff v3 still carries pre-family-clean D4 claim prose (D4-CL05/06/07/09, OQ-V3-05) → a named input-class diagnostic or correct null-`owed_slots` handling, pins as **new** rows; v3 claims corrected and re-pinned as `declared-in-r4`; documented source entry still 19/19; regressions green | ⟨to-verify: parent fills from receipt. This seat measured (a) **fixed mid-wave**: `tools/gates/typed-pipeline-gate.py` (sha `879d40bf…`) now exits **0 / 16/16 legs** on `packet.d4.typed.yml` and **0 / 19/19** on the source packet, `--selftest` 19/19 (2026-10-18T17:34:01Z); (b) v3 revision files landing under `reports/round-25/v3-supersession/`⟩ | `python3 reports/round-25/run-validation.py`, **2026-10-18**, isolated; design/diagnosis `reports/round-25/gate-input/`, v3 revision `reports/round-25/v3-supersession/` |
| D depth | the round-17 argot-derivation forecast (Δ3) was never implemented — round 19 marked it design-forecast → the leg implemented and executed on D4: derivation rules replayed against stated inputs, a violating form `D4L-ARGOT-DERIV`, the D4 typed gate grows the leg with selftest controls, and the delivered-vs-forecast delta recorded | ⟨to-verify: **rule drafted; gate landed mid-wave (sha `07db6e9b…`, selftest 18/18); domain empty (`derived_pairs=0`)** — the "executed on D4" clause is not fully met; landing is orchestrator-owned⟩ | `python3 reports/round-25/run-validation.py`, **2026-10-18**; measured delta `reports/round-25/argot/delta.md`; SKILL rule draft `reports/round-25/rule/skill-draft.md`; docs draft `reports/round-25/docs/derivation-relation-docs.md`; gate `tools/gates/argot-derivation-gate.py` |
| C coverage | `corpus/lessons/` holds 24 round files in three census formats with no reconciled index; several standing open-question rows never folded back → `corpus/lessons/README.md` lands as the reconciled index (per-round row: file, gate-format, open-questions carried, disposition pointer; the open-question queue with an owner per item; the three census formats documented; counting command reproduces the file count) | ⟨to-verify: parent fills from receipt⟩ | `python3 reports/round-25/run-validation.py`, **2026-10-18**; independent census `reports/round-25/lessons/`, index audit `reports/round-25/audit/c31-lessons-index-audit.py` |

### What the D row must not be read as

- **The argot gate landed mid-wave; the domain is still empty.** The round-17 Δ3
  forecast was written for a **weigh-court quote-register** D4; the shipped D4 is
  the **furnace-league** (FIRE × MARK). Round 17's own brief seat routed the
  culture choice to the parent and the landed registry is path A, so every
  register/quote surface is absent **by that decision**
  (`reports/round-25/argot/execution-3.md` §1).
- **The mechanism landed; the domain did not.** `tools/gates/argot-derivation-gate.py`
  (sha `07db6e9b…`, `--selftest` 18/18, this seat 2026-10-18T17:34:01Z) is the
  operation-aware leg; its paired control discriminates (correct pair exit 0; the
  same pair mutated to `min2` emits `D4L-ARGOT-DERIV`, exit 1). But on the
  delivered packet it exits 0 with `derived_pairs=0`, so **"zero fails in the
  delivered packet" is vacuous, not a delivery** — there is no argot form to fail
  on, because the register-scoped data was never shipped.
- **What is delivered must not be understated.** The `CX-01..CX-03`
  machine-readable rule table (`examples/culture-d4/packet.d4.yml:205-226`) and
  its two live replay legs are green over D4 — the naming gate replays all 8 name
  formations with 0 `DERIV` lines; the lexicon audit exits 0 — and both tamper
  controls fire (`reports/round-25/rule/skill-draft.md` §0).

### Capabilities row (landing-ready, orchestrator admits)

A separate capability-row draft is filed at
`reports/round-25/scribe/capability-row.md` (R25-D18), with its proposed
`SCORECARD.md` §Capabilities row and its frozen-row proposals. It carries the
same **zero-rows-by-design** clause this checkpoint carries, and it is likewise
gated on the implementation seats landing the leg.

### Filling rules the parent should enforce before any status leaves ⟨to-verify⟩

- **All three claims share one counting command.** Run it isolated (clone of the
  delivered tree, not historical writers in the live lane), record command, date,
  exit status and check totals; a missing runner is a missing receipt.
- **The D rule is landed, not just drafted.** The claim requires the `SKILL.md`
  landing by the orchestrator (append after `<!-- END R23-D SKILL SUBSECTION -->`,
  `SKILL.md:352`, before `## Error patterns`, `:354`). "Drafted" alone is not the
  declared after-state; until the landing, quote it as open.
- **Pins are new rows only.** Every successor pin (gate-input, v3 revision)
  carries before/after digests; stale pins refuse; a tampered digest fails before
  replay; regressions stay green on the same run.
- **No filed-round edits.** Rounds 8–24 artifacts, receipts and manifests are
  immutable; corrections land as new files/rows.

This checkpoint is not a freshness threshold change, not a loop-3 completion
statement (the loop runs rounds 25–32), and carries no canon, lore acceptance,
rights or cultural-authenticity clearance.

## Limits

- Parent-fill slots only; no admission, no status, no digest is asserted here.
- The digest pins cited in the companion drafts are worktree digests at
  `f74fc940`, taken while sibling seats were editing the tree; re-hash at
  integration before quoting any of them.
