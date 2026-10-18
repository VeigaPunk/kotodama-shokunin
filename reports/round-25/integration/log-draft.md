# R25-D24 — LOG integration draft (proposed round-25 append)

Prepared **2026-10-18** by seat **R25-D24** (integration drafts, claim D). The
parent appends the proposed checkpoint to `LOG.md`; this worker changes only its
assigned `reports/round-25/integration/` files. Nothing here edits a filed round
8–24, admits round 25, or asserts any round-25 claim is met — every status line
below is a parent-fill slot until the declared counting command
(`python3 reports/round-25/run-validation.py`) has a dated receipt.

Sources used (read-only): `reports/round-25/claims.json` (baseline
`e06581b7fc2b50050a336f7f38a7e2baebcc6abc`, state `declared-before-dispatch`),
`reports/round-25/targets.json` (64 workers: O-gate-input 10,
O-v3-supersession 10, D-argot 24, C-lessons 12, X 8),
`reports/round-25/argot/{forecast,current-state,delta,execution-1..4}.md`,
`reports/round-25/rule/skill-draft.md`, `reports/round-25/docs/derivation-relation-docs.md`,
`reports/round-25/scribe/capability-row.md`, and this seat's receipt
`.scratch/r25-d21/receipt.sh` (2026-10-18T17:30:24Z).

## Proposed LOG append

### 2026-10-18 — Round 25 dispatched (loop 3, build 1 of 4; DeepSeek on devin)

- **Trigger:** regimen; claims O/D/C in `reports/round-25/claims.json`; baseline
  `e06581b7…` (round-24 close, loop 2 complete); declaration commit `f74fc940`.
  64 declared workers on `devin/deepseek-v4-1-flash-high` (operator provider
  test, LOG.md provider directive). Three claims: O = the two round-24 cold-run
  hazards (typed-packet gate-input false red; v3 stale D4 claim prose); D = the
  argot-derivation checking leg (the round-17 Δ3 forecast); C = the reconciled
  `corpus/lessons/README.md` index.
- **O (parent-fill — verified / failed as declared):** two required tails.
  (a) *Gate input:* feeding the derived typed packet back into
  `tools/gates/typed-pipeline-gate.py` must no longer manufacture findings —
  either a named input-class diagnostic (exit 2) or correct null-`owed_slots`
  handling on the L2/L3 legs; the documented source-packet entry stays 19/19 and
  all regressions green. (b) *v3 supersession:* handoff v3 claim prose
  (D4-CL05/06/07/09, OQ-V3-05) corrected to the family-clean present state and
  re-pinned as a **new** revision (`declared-in-r4`). Evidence slot: ⟨PARENT:
  gate-input fix + control + regression command/date; v3 new-revision row +
  before/after digests⟩. Design and diagnosis at
  `reports/round-25/gate-input/{design.md,diagnosis.md}` (design only — the real
  gate was not edited by the design seat).
- **D (parent-fill — verified / failed as declared):** the argot-derivation
  checking leg. Round 25 **measured** the round-17 forecast and found it a
  **schema + engine delta on a culture that did not ship**, not a missing gate
  alone: the shipped D4 is the furnace-league (FIRE × MARK), the forecast was
  written for a weigh-court quote-register D4, and the concatenation-only lexicon
  engine makes a correct `reverse` derivation read as a false red. The
  implementation seats then **landed the leg mid-wave**:
  `tools/gates/argot-derivation-gate.py` (sha `07db6e9b…`, `--selftest` 18/18,
  this seat 2026-10-18T17:34:01Z) dispatches on `derived_from`/`derivation`,
  computes `head2`/`reverse`, emits `D4L-ARGOT-DERIV` FAIL, and its paired
  control discriminates (correct pair exit 0; the same pair mutated to `min2`
  emits `D4L-ARGOT-DERIV`, exit 1). **But the domain is empty**: on the delivered
  packet the gate exits 0 with `derived_pairs=0`, because the register-scoped
  argot data was never shipped. Also delivered and green: the `CX-01..CX-03`
  machine-readable rule table and its two live replay legs (naming gate 0 `DERIV`
  lines over the source packet; lexicon audit exit 0; both controls fire). The
  rule drafted for `SKILL.md` is at `reports/round-25/rule/skill-draft.md`
  (orchestrator lands); the docs draft at
  `reports/round-25/docs/derivation-relation-docs.md`; the delta is named
  element-by-element at `reports/round-25/argot/delta.md`. **Landing the SKILL
  rule and the gate does not fully satisfy the claim's "implemented and executed
  on D4" clause** — a green leg over `derived_pairs=0` is a mechanism with no
  domain; the D status is "rule drafted, gate landed, domain empty". Evidence
  slot: ⟨PARENT: landed SKILL subsection + the gate's frozen row + the named
  delta⟩.
- **C (parent-fill — verified / failed as declared):** the reconciled
  `corpus/lessons/README.md` index (per-round row, open-question queue with
  owners, the three census formats). A sibling C seat landed the README
  (untracked at this seat's read); an independent census verified its 24-row
  index clean, and flagged its queue table as a live-moving surface
  (`reports/round-25/lessons/C25-C30.md`). Evidence slot: ⟨PARENT: README path +
  census command/date + the queue table's frozen stamp⟩.
- **Counting command:** `python3 reports/round-25/run-validation.py` (declared in
  `reports/round-25/claims.json`). Parent prerequisite: the runner must exist in
  the round tree and run isolated (clone of the delivered tree, historical
  writers not executed live), with command, date and exit status recorded.
  Evidence slot: ⟨PARENT: receipt path + N/N checks + timestamp⟩. No admission
  wording before a green dated receipt.
- **Claim-D measurement receipt (this seat, 2026-10-18T17:30:24Z, plus the
  17:34:01Z landing read):** `packet.d4.yml` sha256 `e7ecd204…`;
  `04-lexicon.yml` `74c2561b…`; naming gate `d9e4e8f4…`; lexicon audit
  `2c4dd397…`; argot gate `07db6e9b…`; `SKILL.md` (pre-landing) `2d85bfea…`.
  Token census (packet data): `ARGOT`/`argot`/`head2`/`derived_forms`/`derived_ok`/
  `doublet_of` → **0 files** in `examples/`; `D4L-ARGOT-DERIV` → **0 files** under
  `examples/` (the id lives only in the new gate, its fixture and the round-17
  design text). Controls: `NM-01 tumhai→tumhei` → `DERIV-REPLAY` FAIL;
  `L-46 mesar→mesor` → `D-form-mismatch`; argot gate correct pair exit 0, mutated
  pair `D4L-ARGOT-DERIV` exit 1.
- **Limits:** no canon, lore acceptance, historical-truth certification, rights,
  permission or cultural-authenticity clearance is implied. Filed rounds 8–24
  artifacts are untouched; corrections and pins are new files/new rows only. The
  argot gate **landed mid-wave**, so the D status is "rule drafted, gate landed,
  domain empty" (`derived_pairs=0`), not "delivered and executed on D4"; the
  claim's stronger clause is recorded as not fully met at this stamp.
