# R25-D24 — docs drafts: the derivation-relation verification entry and the round-25 lesson fragment

- **Seat:** D R25-D24 (docs, the fourth of R25-D21..D24). Round 25, loop 3 build
  1 of 4, claim **D** `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  worktree HEAD at measurement `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Status: DRAFT ONLY.** This file is paste-ready draft text for
  `corpus/knowledge/verification/derivation-relation-verification.md` and a
  round-25 lesson fragment. **This seat wrote no `corpus/**` byte**; the parent
  owns placement, wording and admission. Companion: `../rule/skill-draft.md`
  (the SKILL.md subsection, R25-D21..D23). No commit, no push.
- **Canon:** NON-CANON engineering draft. No real language, script, institution
  or argot is described, cited or approximated.
- **Measurements:** this seat's receipt `.scratch/r25-d21/receipt.sh` (run
  2026-10-18T17:30:24Z, cwd = lane root); peer measurements in
  `reports/round-25/argot/` are re-cited, not re-run.

---

## Part 1 — draft `corpus/knowledge/verification/derivation-relation-verification.md`

Header (follows the `QUALITY.md` bar: provenance, calibration, coupling,
usability, canon hygiene):

```markdown
# Derivation-relation verification — check a claimed derivation only when the schema and the engine can carry it

- topic: The verification procedure for a **derivation relation** between two records of one packet: a form claimed to come from another record by a declared operation. Covers what makes the relation checkable (a schema field naming the base, an operation the engine can compute, stated inputs that replay), the failure modes (a prose rule that cannot be re-run, a correct non-concatenative derivation that reads as a false red, a missing relation that reads as clean), and the control that proves the leg discriminates. Reference method and lane policy only; canon belongs to lore-shokunin.
- gap filled: the partition carries `generated-artifact-roundtrip-verification.md` (byte-identity, `--check`, the corruption class) and `label-channel-routing-verification.md` (which channel a record's string is graded on), but no entry states the **cross-record derivation check** — when a base→form relation is representable at all, and what makes its replay honest. Absence sweep 2026-10-18: `grep -rln "derivation replay\|pattern/output pair\|derived_from" corpus/knowledge/` → 0 files.
- sources:
  - KTD-DR-S-0001 — `SKILL.md` §"Derivation replay — replay the family's own build, by text transform" (`:189-242`): the machine-readable pattern/output-pairs row, the named-inputs row, the pre-registration row, and thresholds T1–T4. Lane policy, not a published standard.
  - KTD-DR-S-0002 — `tools/gates/naming-collision-gate.py` (sha256 `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`, measured 2026-10-18): rule table `:1206-1220`, name-formation replay `:1359-1494`, ids `DERIV-AFFIX` / `DERIV-REPLAY` / `DERIV-HOLD`. The executable that replays a **name's** stated chain.
  - KTD-DR-S-0003 — `tools/gates/lexicon-coverage-audit.py` (sha256 `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287`, measured 2026-10-18): `constructions` read `:664`, leg D `:740-876`, ids `D-route-missing` / `D-rule-underspecified` / `D-form-mismatch` / `D-rule-violation` / `D-meaning-mismatch` / `D-exception-unlicensed` / `D-stage-mismatch`. The executable that replays a **lexicon record's** stated bases, and whose model is concatenation-only.
  - KTD-DR-S-0004 — `examples/culture-d4/packet.d4.yml` (sha256 `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3`, measured 2026-10-18) `morphology.derivation_rules` (`:205-226`): the delivered machine-readable rule table — `CX-01` compound `^(?P<a>.+)\+(?P<b>.+)$` → `{a}{b}`, `CX-02` suffix → `{stem}ar`, `CX-03` suffix → `{stem}en`, with `derivation_note` pre-registering "the three rules replay the four derived or compound records in this file and the eight names in 05-naming". NON-CANON drill artifact.
  - KTD-DR-S-0005 — `reports/round-25/argot/` (R25-D01..D04, R25-D11..D14): the forecast enumeration (`forecast.md`), the delivered-state measurement (`current-state.md`), the element-by-element delta (`delta.md`), and the four executions (`execution-1.md`..`-4.md`) including the controls that show a correct `reverse` derivation and a wrong one produce the *same* finding under the concatenation-only replayer (`current-state.md` §6.2 N-2/N-3/N-4). Lane evidence, NON-CANON.
  - KTD-DR-S-0006 — `reports/round-17/d4/design-brief.md` §6 Δ3 (`:296-310`) and `reports/round-17/d4/design-language.md` §5 (`:186-217`): the forecast the check was designed for — two operations with **stated algorithms** (`head2` maximal-onset; `reverse` character-level), a control-only defect id (`D4L-ARGOT-DERIV`), and the spellability law. Design intent; the culture it was written for did not ship, so its data surface is undelivered while its mechanism landed in round 25.
  - KTD-DR-S-0011 — `tools/gates/argot-derivation-gate.py` (sha256 `07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe`, measured 2026-10-18T17:34:01Z): the round-25 operation-aware replay leg — embeds the two declared operations (`head2` maximal-onset, `reverse`), dispatches on `derived_from`/`derivation` rather than a concatenation model, emits `D4L-ARGOT-DERIV` FAIL / `D4L-ARGOT-RULE` HOLD / `D4L-ARGOT-DATA` (exit 2), prints a `coverage:` domain line, and is flagless/single-input so `tools/replay-frozen.py` can pin a row. `--selftest` → `18/18 checks passed`. Its fixtures `tools/gates/fixtures/argot-derivation-gate.{yml,expected}` carry four planted FAILs and one planted HOLD. NON-CANON.
  - KTD-DR-S-0007 — `corpus/knowledge/verification/verification-method-overview.md` §2–§3 (epistemic type; the minimal claim card: a failing case fixed before review) and `verification-independence-anti-circularity.md` §1 (independence is a property of failure sources, not job titles). They supply the record shape; this entry supplies the cross-record derivation rule they do not state.
  - KTD-DR-S-0008 — `corpus/knowledge/verification/generated-artifact-roundtrip-verification.md` §2–§3 (the re-serialization corruption class and the digest pin) — the sibling check this one presupposes: a derivation built by re-serializing the packet can corrupt the very regex the replay runs.
  - KTD-DR-S-0009 — Yue Jia and Mark Harman (2011), “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering* 37(5): 649–678, [doi:10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62). A control is worth what it can catch; cited as a design rule for the leg's controls, not as a law. Calibration: a survey of a contested technique.
  - KTD-DR-S-0010 — Ken Thompson (1984), “Reflections on Trusting Trust,” *Communications of the ACM* 27(8): 761–763, doi:10.1145/358198.358210. The replayer and the rule table belong to the trusted base: a green replay proves the stated rule reproduces the stated form, not that the form's real derivation was found.
- calibration: the derivation-relation rule is this lane's house policy read off `SKILL.md`, the two gates and the D4 packet, not a published standard; Jia–Harman (a survey of a contested technique) and Thompson are engineering references cited as design rules for controls and the trusted base, never as linguistic evidence; no real language, script or community is described.
- couples: verification — `generated-artifact-roundtrip-verification.md`, `label-channel-routing-verification.md`, `verification-method-overview.md`, `verification-independence-anti-circularity.md`, `naming-collision-gate.md`, `lexicon-coverage-audit.md`, `gate-frozen-run-standard.md`; synthesis — `../synthesis/typed-label-routing-workflow.md`, `../synthesis/generated-artifact-lifecycle.md`, `../synthesis/hold-set-contract-in-brief.md`; linguistics — `../linguistics/morphological-typology.md`, `../linguistics/naming-systems.md`, `../linguistics/phonology-sanity.md`; tooling — `tools/gates/naming-collision-gate.py`, `tools/gates/lexicon-coverage-audit.py`, `examples/culture-d4/packet.d4.yml`; siblings — lore-shokunin owns canon; chousa-shokunin owns general source-research method.
- source: the `SKILL.md` derivation-replay table, the two gates' replay legs measured 2026-10-18, and the round-25 argot forecast/delta; the rule and its controls are this lane's house method, not findings attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `f74fc940`, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` → exit 1, 14 findings, `grep -ci deriv` → 0 (all 8 name chains replay clean); `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml` → exit 0, no output; `python3 tools/gates/argot-derivation-gate.py --selftest` → 18/18 (2026-10-18T17:34:01Z); the tamper controls fire (`NM-01 tumhai→tumhei` → `DERIV-REPLAY`; `L-46 mesar→mesor` → `D-form-mismatch`; argot correct pair exit 0 vs mutated pair `D4L-ARGOT-DERIV` exit 1). Header fields and every cross-reference target checked for resolution; all cited repo paths exist. Peer receipts in `reports/round-25/argot/` were read by path, not re-executed.
- recheck: whenever any gate, the `morphology.derivation_rules` table, the D4 packet, or the `SKILL.md` derivation-replay table changes; before quoting any derivation count into a handoff; and whenever the argot domain is populated or the culture decision is revisited (corrections are new entries, never rewrites of this one).

## 1. What this entry licenses

- A **check**, not a generator: given a record that claims a derivation, this entry tells a reviewer whether the claim is checkable at all, and how to prove the check discriminates. It does not name the real derivation of any form.
- The relation is a **cross-record** relation — the only one the lane grades. Single-record checks (a form against an inventory, a label against a channel) are `label-channel-routing-verification.md` and `phonology-sanity-gate.md`.
- The rule is **lane policy** derived from `SKILL.md` and the gates. It is not a claim about any real language, and passing it is not canon.

## 2. The checkability decision procedure

Apply in order; the first row that fires fixes the verdict. `E` = the record's declared evidence status.

| # | Condition | Verdict | What the checker does | Wrong handling produces |
|---|---|---|---|---|
| R1 | The packet declares a machine-readable rule table (`pattern` + `output` per rule id) and the record names its base(s) + rule | **checkable — replay** | recompute `output` from the stated inputs under the named rule and compare to the delivered form | grading the form by inspection, or trusting the record's own `expected` field, makes the replay a tautology |
| R2 | The record claims a derivation but names no base, or the packet declares no rule table | **HOLD** | emit a hold naming the missing input or the missing rule table | a silent pass is forbidden; the record is un-replayed, not clean |
| R3 | The declared rule's `pattern` is a packet-authored regex that does not compile, or whose match exceeds the budget | **HOLD** | refuse as `DERIV-HOLD` (over-budget) — `re.error` is not enough against catastrophic backtracking | an unbounded match hangs the checker; a non-compiling pattern is a false red on a correct form |
| R4 | The declared rule's `output` is a template outside the accepted subset | **HOLD** | refuse to render; do not fall back to a guess | rendering an arbitrary template is arbitrary code execution inside the checker |
| R5 | The operation the record needs is **not computable** by the engine (the replayer models every rule as concatenation) | **not checkable — report** | state the gap: the engine must dispatch on an `operation` field; do not grade the record | a *correct* non-concatenative derivation is a **false FAIL** and a non-derivation passes — the leg manufactures findings instead of catching them. The round-25 operation-aware gate `tools/gates/argot-derivation-gate.py` is the fix for this row (correct pair exit 0, mutated pair `D4L-ARGOT-DERIV` exit 1, this seat 2026-10-18T17:34:12Z) |
| R6 | The relation has no delivered instances | **vacuous — say so** | report "zero fails" as vacuous, never as a delivery, and print the domain size | "zero fails" reads as "the packet is clean" when the domain is empty. Measured: the argot gate exits 0 on the D4 packet with `derived_pairs=0` (2026-10-18T17:34:01Z) |

T1–T4 are the thresholds that make the rows actionable; they are stated in
`SKILL.md` §"Derivation replay" and restated for this relation in
`../round-25/rule/skill-draft.md` §2 (T1 self-consistency is not correctness;
T2 a vacuous signature is not a delivery; T3 a forecast for a culture that did
not ship is absent by that decision; T4 the un-representable half is reported,
not forced).

## 3. The control that proves the leg discriminates

A green replay is capability, not measurement. The leg earns its standing only
with a paired control — the untouched relation passes, and a mutated relation is
named:

| # | control | must show |
|---|---|---|
| C-1 | mutate the delivered **form** of a replayed record (the rule and the stated base untouched) | the leg names the record, the rule, and the disagreeing pair; the untouched copy still passes |
| C-2 | mutate the **rule** (`output` template) while the records are untouched | every record that used the rule goes red — proving the rule is load-bearing, not decorative |
| C-3 | a record whose **form equals its base** (not a derivation at all) | the leg must not accept it as a derivation (under the concatenation model it passes — the measured false green) |

C-1 and C-2 are the round-25 measured controls
(`reports/round-25/rule/skill-draft.md` §0 reading 3; `../round-25/argot/execution-2.md`
§1–§3). C-3 is the measured false-green of the concatenation-only engine
(`reports/round-25/argot/current-state.md` §6.2 N-4) and is the reason R5 exists.

## 4. What this entry never licenses

- **A replay is not a proof of etymology.** It proves the stated rule reproduces the stated form; a wrong-but-self-consistent rule set passes (`SKILL.md` §Derivation replay, T1).
- **A control-only id is not a delivered pass.** An id specified to fire only in the negative control is absent from the delivered packet *by design*; its absence is not a clearance (`reports/round-17/d4/design-brief.md:308-310`).
- **A green leg over an empty domain is not an implemented leg.** Name the domain size with every verdict.
- **A derivation check is not canon.** It grades the packet's internal arithmetic, not the culture.

## 5. Decision record — the rules this entry adopts

1. **Adopted:** a cross-record derivation is checkable only when the schema names the base and the rule table declares the operation; otherwise the verdict is HOLD or not-checkable, never a pass (§2 R1/R2/R5).
2. **Adopted:** the replayer must dispatch on the operation; a concatenation-only model silently converts a correct non-concatenative derivation into a false red (§2 R5).
3. **Adopted:** the leg carries a paired control, and a control-only id is expected to be absent from the delivered packet (§3).
4. **Adopted:** a signature with no delivered instances is reported as vacuous, with the domain size named (§2 R6).
5. **Rejected:** implementing a new operation by adding its name to the existing rule table alone. Reason: measured — it manufactures a false red on a correct packet and a false green on a missing derivation (`reports/round-25/argot/delta.md` §3).
6. **Open (to-verify):** whether the cross-record derivation check belongs in the lexicon audit's leg D, in the naming gate's Gate C, or in a new `tools/gates/` checker. Owner: this lane's D/O boundary; not disposed here.
```

---

## Part 2 — draft round-25 lesson fragment (`corpus/lessons/round-25.md`, D-section)

```markdown
## D — depth: the argot-derivation forecast is a schema+engine delta on a culture that did not ship

The round-17 D4 design forecast a derivation-checked argot — quote forms derived
from plain bases by two declared operations, checked through `derived_from` +
`derivation` fields, a control-only `D4L-ARGOT-DERIV` FAIL
(`reports/round-17/d4/design-brief.md:296-310`). Round 25 measured the delta and
found it wider than "an unimplemented leg":

- **The culture the forecast was written for did not ship.** The forecast
  describes a **weigh-court quote-register** D4 (COUNT × QUOTE); the delivered D4
  is the **furnace-league** (FIRE × MARK,
  `examples/culture-d4/components/01-brief.yml:59,79,85`). Round 17 carried
  mutually divergent design documents and its brief seat routed the choice to the
  parent (`reports/round-17/d4/design-brief.md:653-663`); the landed registry is
  reconciliation path A. Every register/quote surface is therefore absent **by
  that decision**, not by an oversight in the argot leg
  (`reports/round-25/argot/execution-3.md` §1).
- **The mechanism landed, the domain did not.** Round 25 shipped
  `tools/gates/argot-derivation-gate.py` (sha256 `07db6e9b…`, `--selftest`
  18/18, this seat 2026-10-18T17:34:01Z): it dispatches on `derived_from`/
  `derivation`, computes `head2`/`reverse` instead of concatenating, and its
  paired control discriminates (a correct `reverse` pair exits 0; the same pair
  mutated to `min2` emits `D4L-ARGOT-DERIV` and exits 1). But on the delivered
  packet it exits 0 with `derived_pairs=0`: no delivered record declares an argot
  relation, so the leg is a **mechanism with no domain** — `derived_from` as a
  delivered relation, `head2`, `derived_forms`, `derived_ok`, `doublet_of` → 0
  files in `examples/` (`reports/round-25/argot/current-state.md` §4-§5.1).
- **A naive "add the operation to `constructions`" would still regress the
  *lexicon audit*.** That engine is concatenation-only: under it a *correct*
  `reverse` derivation (`min`→`nim`) and a *wrong* one produce the same
  `D-form-mismatch`, and a non-derivation (`form == base`) passes
  (`reports/round-25/argot/current-state.md` §6.2 N-2/N-3/N-4). The new gate
  avoids this by never consulting `constructions` for the argot ops.
- **What is delivered is real and green, and must not be understated.** The
  packet's `morphology.derivation_rules` (`CX-01..CX-03`,
  `examples/culture-d4/packet.d4.yml:205-226`) is a machine-readable rule table;
  the naming gate replays all eight name formations with zero `DERIV` lines, and
  the lexicon audit replays the four derived/compound records with exit 0
  (measured 2026-10-18T17:30:24Z). That surface is replayable and is *not* the
  forecast's argot relation (`reports/round-25/argot/execution-1.md`).

**The lesson, in one line:** a derivation is replayable only when the schema can
express the relation *and* the engine can compute the declared operation — a
prose rule cannot be replayed, and a rule the engine cannot compute turns a
correct derivation into a false red. When the forecast was written for a culture
that did not ship, the honest record names the culture decision first and the
missing leg second; a green leg over an empty domain (`derived_pairs=0`) is a
**mechanism with no domain**, and "zero fails in the delivered packet" over that
empty domain is a vacuous signature, not a delivery.
```

---

## Part 3 — placement, limits, and counting commands

**Proposed placement.** Part 1 lands as a new entry under
`corpus/knowledge/verification/`; it is a sibling of
`generated-artifact-roundtrip-verification.md` and
`label-channel-routing-verification.md`, which it couples to. Part 2 is the
D-section of the round-25 lesson file; a peer C seat already holds
`corpus/lessons/README.md` and the X gate-keeper holds the survey — the parent
reconciles which seat lands the round-25 lesson file (the round-19 precedent
recorded exactly this kind of collision, `reports/round-19/integration/d4-lessons-entry.md`).

**Limits.**

- Draft text only; no `corpus/**` byte was written by this seat.
- The digest pins in Part 1's header are worktree digests at `f74fc940`, taken
  while sibling seats were editing the tree; re-hash at integration before
  quoting. The argot gate and the typed gate both moved inside this seat's write
  window, so every citation of them names its own stamp.
- The argot leg's status is **mechanism landed, domain empty**: the gate is on
  disk and green, but `derived_pairs=0` on the delivered packet, because the
  culture that hosts the argot did not ship. Part 2's lesson states that plainly
  and does not claim the claim's "implemented and executed on D4" clause is fully
  met.

**Counting commands.**

```sh
export TMPDIR=$PWD/.scratch
grep -rln "derivation replay\|pattern/output pair\|derived_from" corpus/knowledge/ || echo "0 files (the gap this entry fills)"
grep -c "ARGOT" examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml   # 0 0
python3 tools/gates/argot-derivation-gate.py --selftest 2>&1 | tail -1                     # 18/18
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml ; echo "exit=$?"  # 0, derived_pairs=0
python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml ; echo "exit=$?"  # 1, 4 FAIL + 1 HOLD
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | grep -ci deriv   # 0
python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml ; echo "exit=$?"    # 0
```
