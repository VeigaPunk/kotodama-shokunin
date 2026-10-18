# R25-D21..D23 — SKILL.md derivation-relation rule: consolidated draft

- **Seats:** D R25-D21..D23 (rule drafters x3, SKILL + docs). Round 25, loop 3
  build 1 of 4, claim **D** `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Assignment (verbatim):** "D R25-D21..D24 (SKILL+docs x4): the argot rule
  drafted for SKILL.md (orchestrator lands); docs; LOG/SCORECARD drafts."
- **Date:** 2026-10-18 (stamps UTC). Baseline revision
  `e06581b7fc2b50050a336f7f38a7e2baebcc6abc` (declared); worktree HEAD at
  measurement `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Status: DRAFT ONLY — `SKILL.md` is not edited by workers.** The orchestrator
  lands the subsection below. This seat wrote no `SKILL.md`, `LOG.md`,
  `SCORECARD.md`, `corpus/**`, `tools/**`, `examples/**` or filed round-8..24
  byte. Scratch under `.scratch/r25-d21/` only (`TMPDIR=$PWD/.scratch` preceded
  every scratch write). No commit, no push.
- **Canon:** NON-CANON engineering draft. No real language, script, institution
  or argot is described, cited or approximated anywhere in it.
- **Consolidates:** `reports/round-25/argot/forecast.md` (R25-D01),
  `current-state.md` (R25-D02), `delta.md` (R25-D03), `execution-1.md`..`-4.md`
  (R25-D11..D14), `reports/round-25/scribe/capability-row.md` (R25-D18), and this
  seat's own dated receipt (`.scratch/r25-d21/receipt.sh`, run
  2026-10-18T17:30:24Z). It re-derives none of them; where it cites a peer
  measurement it says so.

## 0. Verdict, and what the rule must and must not claim

**The round-17 argot-derivation forecast was undelivered at this seat's first
measurement (2026-10-18T17:30:24Z); the implementation seats then landed the
argot gate mid-wave (first present 17:31Z, settled green 17:34Z), so the leg is
now on disk and the honest craft rule is a *derivation-relation* rule stated over
what the bytes actually carry, plus the delta that still stands.** The rule below
codifies the delivered, measured replay discipline (machine-readable
pattern/output pairs replayed against stated inputs, and an operation the engine
can compute) and adds the *boundary* the forecast exposes: a derivation relation
between two records is only checkable when the schema can express it and the
engine can compute the declared operation. Every row cites a committed path or a
dated command.

Five measured readings carry the subsection (this seat, 2026-10-18, cwd = lane
root; the first four at 17:30:24Z via `.scratch/r25-d21/receipt.sh`, the landing
at 17:34:01Z):

1. **The delivered derivation surface is real and green.** The D4 packet
   declares exactly three machine-readable rules — `CX-01` compound
   `^(?P<a>.+)\+(?P<b>.+)$` → `{a}{b}`, `CX-02` suffix → `{stem}ar`, `CX-03`
   suffix → `{stem}en` (`examples/culture-d4/packet.d4.yml:205-226`, digest
   `e7ecd204…`). The naming gate replays all eight name formations with **zero**
   `DERIV` lines (`python3 tools/gates/naming-collision-gate.py
   examples/culture-d4/packet.d4.yml` → exit 1, 14 findings, `grep -ci deriv` →
   **0**); the lexicon audit replays the four derived/compound records with exit
   **0** and no output.
2. **The argot gate landed mid-wave, and the leg is now on disk.** Measured
   2026-10-18T17:34:01Z: `tools/gates/argot-derivation-gate.py` sha256
   `07db6e9b…`, `--selftest` → `18/18 checks passed`; on the D4 source packet →
   exit **0**, `coverage: … records=156 register_scoped=6 derived_pairs=0
   borrow_pairs=6 violations=0 rule_holds=0`. Its **paired control** discriminates:
   a scratch packet carrying a correct pair (`nim` = `reverse(min)`) exits 0,
   while the same pair mutated to `min2` emits `D4L-ARGOT-DERIV` and exits 1
   (this seat, 17:34:12Z). **But the delivered packet has `derived_pairs=0`** — the
   argot has no domain, because the culture that hosts it did not ship (reading 4).
3. **The forecast's two operations are absent from the delivered packet's own
   data, and the gap is a schema gap.** `ARGOT`, `argot`, `head2`,
   `derived_forms`, `derived_ok`, `doublet_of` → **0 files** in `examples/` and in
   `tools/` *as packet data* (the new gate carries `head2`/`reverse` as its own
   embedded algorithm table, which is the leg, not the packet's schema);
   `D4L-ARGOT-DERIV` → **0 files** in `examples/` (only `reports/round-17/` design
   text and the new gate's fixture/`.expected`). `derived_from` occurs in
   `examples/` in **one** unrelated file (`examples/handoff-packet.sample.yml`, a
   revision pointer), never as a delivered derivation relation.
4. **The culture the forecast was written for did not ship.** The forecast
   describes a weigh-court quote-register D4 (COUNT × QUOTE); the delivered D4 is
   the furnace-league (FIRE × MARK, `examples/culture-d4/components/01-brief.yml:59,79,85`).
   Round 17 carried divergent design documents and its brief seat routed the
   choice to the parent (`reports/round-17/d4/design-brief.md:653-663`); the
   landed registry is reconciliation path A, so the register surface is absent
   **by that decision** (`reports/round-25/argot/execution-3.md` §1).
5. **A naive "add `reverse` to `constructions`" is still a regression for the
   *lexicon audit*.** That engine is concatenation-only; under it a *correct*
   `reverse` derivation and a *wrong* one produce the same `D-form-mismatch`
   (peer controls N-2/N-3, `reports/round-25/argot/current-state.md` §6.2,
   re-cited not re-run). The new argot gate avoids this by keying on
   `derived_from`/`derivation` and never consulting `constructions` for the argot
   ops (`reports/round-25/argot/delta.md` §8.2, corrected there).

## 1. Proposed placement

Insert the subsection at the end of the typed-pipeline block, **after**
`<!-- END R23-D SKILL SUBSECTION -->` (`SKILL.md:352`) and **before**
`## Error patterns` (`SKILL.md:354`). This continues the existing sequence
(Label typing → Claim uncertainty → Slot-label routing → Derivation replay →
Family-clean projection) with the *relation* the derivation-replay section
presupposes: replay grades one record's stated chain; this rule grades a
derivation between **two** records, and says when that is checkable at all.

## 2. The exact SKILL.md subsection (verbatim, paste-ready)

<!-- BEGIN R25-D SKILL SUBSECTION — lift verbatim from "### Derivation relations" through the last caution -->

### Derivation relations — a form is checkable against its base only when the schema and the engine can carry the operation

A derivation *relation* — a record whose form is claimed to come from another
record of the same packet by a declared operation — is checkable only when three
things are true at once: the packet's **schema can express** the relation (a
field naming the base, and a declared operation), the **engine can compute** the
declared operation (not merely concatenate), and the **stated inputs replay** to
the delivered form. The D4 chain is the worked instance; its argot half landed in
round 25 and its register domain is the named gap. Executable authorities
`tools/gates/naming-collision-gate.py` (rule table `:1206-1220`, formation
replay `:1359-1494`, ids `DERIV-AFFIX`/`DERIV-REPLAY`/`DERIV-HOLD`),
`tools/gates/lexicon-coverage-audit.py` (`constructions` read `:664`, leg D
`:740-876`, ids `D-route-missing`/`D-rule-underspecified`/`D-form-mismatch`/
`D-rule-violation`/`D-meaning-mismatch`/`D-exception-unlicensed`/
`D-stage-mismatch`), and the operation-aware argot leg
`tools/gates/argot-derivation-gate.py` (ids `D4L-ARGOT-DERIV` FAIL /
`D4L-ARGOT-RULE` HOLD / `D4L-ARGOT-DATA` exit 2; `--selftest` 18/18; flagless
and single-input so `tools/replay-frozen.py` can pin a row); design authority
`reports/round-17/d4/design-brief.md` §6 Δ3 (`:296-310`) and
`reports/round-17/d4/design-language.md` §5 (`:186-217`); measured instance and
delta `reports/round-25/argot/` (`forecast.md`, `current-state.md`, `delta.md`,
`execution-1.md`..`-4.md`).

| Derivation requirement | Correct shape | Never | Consequence if violated | Citation |
|---|---|---|---|---|
| Machine-readable pattern/output pairs | the rule set is a machine-readable table: each rule carries an id, a `pattern`, and an `output` template the checker replays against the record's stated inputs | a prose rule ("the first two syllables", "reverse it") with no executable pair | the derivation cannot be re-run by a stranger; the "check" is a re-reading of the same prose | `examples/culture-d4/packet.d4.yml:205-226` (`CX-01` `^(?P<a>.+)\+(?P<b>.+)$`→`{a}{b}`, `CX-02`→`{stem}ar`, `CX-03`→`{stem}en`); `SKILL.md:209` |
| Stated inputs, replayed | the record names its base(s) and its rule, and the checker recomputes `output` from them and compares to the delivered form | grade the form by inspection, or trust the record's own `expected` field | a record that disagrees with itself passes; the replay is a tautology | `examples/culture-d4/components/04-lexicon.yml:192-196`; naming gate `tools/gates/naming-collision-gate.py:1359-1494`; lexicon audit leg D `tools/gates/lexicon-coverage-audit.py:740-876` |
| Relation expressible in the schema | a cross-record derivation needs a field naming the base record (`derived_from` / `bases`) **and** an operation the rule table declares | assume the relation exists because the design prose says so; let the operation be implied by the rule's name | the relation is uncheckable: no code path can read two records and compare one as a derivation of the other | measured gap: `derived_from` → 0 as a relation in `examples/`; the delivered `contract.record_fields.lexicon` (`examples/culture-d4/packet.d4.yml`) carries `bases` + `construction`, not `derived_from` + `derivation` |
| Operation computable by the engine | the replay engine **dispatches on the operation**: concatenation for the compound/suffix class, a computed function for `head2`/`reverse` | add an operation name to the rule table and let a concatenation-only replayer grade it | a *correct* non-concatenative derivation is a **false FAIL**, and a non-derivation passes — the leg manufactures findings instead of catching them | measured: on the concatenation-only lexicon audit a correct `reverse` (`min`→`nim`) and a wrong one (`min2`) both yield `D-form-mismatch … (expected 'min')`, exit 1 (`reports/round-25/argot/current-state.md` §6.2 N-2/N-3/N-4); the operation-aware `tools/gates/argot-derivation-gate.py` (landed round 25) dispatches instead — correct pair exit 0, mutated pair `D4L-ARGOT-DERIV` exit 1 (this seat, 2026-10-18T17:34:12Z) |
| Operation determinism | where two readings of an algorithm disagree, the declared rule fixes one and carries a worked pair as its own selftest constant | leave "the first two syllables" to the implementer | a derivation that is not deterministic cannot be checked; two implementations disagree on the same packet | `reports/round-17/d4/design-language.md:191-196` — maximal-onset `saalumi`→`saa.lu.mi`→`saalu`, explicitly **not** `saalum` |
| Control-only defect id | a violating form is a FAIL-class id emitted **only** in the negative control; the delivered packet's own debt set stays free of it | wire the id so the delivered packet carries it, or let the packet's absence of the id read as a clearance | "zero rows in the delivered packet" is read as "no defect exists" when the id was never wired | `reports/round-17/d4/design-brief.md:308-310` (`D4L-ARGOT-DERIV`, control-only); measured 2026-10-18T17:34Z: the id occurs in the gate `tools/gates/argot-derivation-gate.py` and its fixture `.expected`, and in **0** files under `examples/` — the delivered packet carries no such row, as the design requires |
| The leg discriminates | a control mutates the *relation* (base, rule, or delivered form) and the leg names the record, the rule, and the disagreeing pair; the untouched pair passes | a control that only re-runs the green path | a leg that always passes is capability, not measurement | this seat, 2026-10-18T17:30:24Z: `NM-01` `tumhai`→`tumhei` → `DERIV-REPLAY: FAIL — … declared chain 'CX-01' applied to 'tum+hai' yields 'tumhai'`; `L-46` `mesar`→`mesor` → `D-form-mismatch: 'mesor' does not reproduce from bases mes under construction 'CRAFT-AGENT' (expected 'mesar')` |

Thresholds and cautions that are part of the rule:

- **T1 — a stated rule that replays is not a rule that is *right*.** The replay
  grades self-consistency: a rule set that is wrong but self-consistent passes.
  That is the discipline's known bound, not a defect; naming a form's real
  derivation is a different question (`reports/round-25/argot/execution-1.md`
  §4).
- **T2 — "zero fails in the delivered packet" can be vacuous.** Where the
  relation has no delivered instances, the signature is satisfied trivially, and
  must be recorded as vacuous rather than as a delivery
  (`reports/round-25/argot/delta.md` §1 F-5).
- **T3 — the culture a forecast was written for is part of the forecast.** The
  round-17 argot design was written against a **weigh-court quote-register** D4
  (COUNT × QUOTE, argot loans, owed plain doublets); the **shipped** D4 is the
  **furnace-league** (FIRE × MARK, `examples/culture-d4/components/01-brief.yml:59,79,85`;
  `examples/culture-d4/brief.md:15-18`). Round 17 carried mutually divergent
  design documents and its brief seat routed the choice to the parent
  (`reports/round-17/d4/design-brief.md:653-663`); the landed registry is
  reconciliation path A, so the register surface was never built. A forecast
  element that depends on a culture that did not ship is **absent by that
  decision**, not by an oversight in the leg — name it that way.
- **T4 — the un-representable half is reported, not forced.** Where the honest
  leg cannot be built (no schema field, no computable operation), the rule
  requires the gap be **named** with its blocking step, never simulated by a
  green run over an empty domain. The round-25 argot gate is the live instance:
  it is on disk, its selftest is 18/18, and it exits 0 on the D4 packet — but
  with `derived_pairs=0`, because no delivered record declares an argot relation.
  A gate over an empty domain is a **landed mechanism with no domain**, not a
  demonstrated capability; report it that way. The round-17 brief seat's own
  honesty clause stands: "exit 0 from the D4 gate is a structural pass with open
  holds printed verbatim — never a clearance"
  (`reports/round-17/d4/design-language.md:580-581`).
- Cautions that are part of the rule: a green derivation leg is **not** canon,
  lore acceptance, or a real-world etymology check; and where a *shared* replay
  engine is reused across families, the family-clean boundary above still
  governs which records the relation may name
  (`SKILL.md:243-352`, the family-clean projection rule).

<!-- END R25-D SKILL SUBSECTION -->

## 3. The citation ledger (every row's source, resolved)

Measured 2026-10-18T17:30:24Z (`.scratch/r25-d21/receipt.sh`), cwd = lane root;
the landed-gate row at 17:34:01Z:

| cited path | sha256 | resolves |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | yes |
| `examples/culture-d4/components/04-lexicon.yml` | `74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5` | yes |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | yes |
| `tools/gates/lexicon-coverage-audit.py` | `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287` | yes |
| `tools/gates/argot-derivation-gate.py` (landed mid-wave) | `07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe` | yes |
| `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` | yes |
| `tools/gates/fixtures/argot-derivation-gate.expected` | `38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018` | yes |
| `tools/gates/typed-pipeline-gate.py` (patched mid-wave) | `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126` | yes |
| `SKILL.md` (at draft time, pre-landing) | `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048` | yes |

Line anchors used above, re-checked at draft time: `SKILL.md:209` (machine-readable
pattern/output pairs row), `SKILL.md:352` (R23-D subsection end), `SKILL.md:354`
(`## Error patterns`), `tools/gates/naming-collision-gate.py:1206-1220` (rule
table), `:1359-1494` (formation replay), `tools/gates/lexicon-coverage-audit.py:664`
(`constructions` read), `:740-876` (leg D), `examples/culture-d4/packet.d4.yml:205-226`
(`morphology.derivation_rules` + `derivation_note`).

## 4. Review findings (the three drafters)

- **F1 (placement verified).** `grep -n "END R23-D SKILL SUBSECTION\|^## Error
  patterns"` → `352`, `354`. The proposed insertion point is unambiguous and
  leaves the R23-D block byte-intact.
- **F2 (the rule must not overclaim the leg, and the leg landed mid-wave).** The
  claim's `after_required` reads "the argot-derivation checking leg implemented
  and executed on D4". At this seat's **first** measurement (17:30:24Z) the leg
  was **not on disk**; the implementation seats landed it between 17:31Z and
  17:34Z (`tools/gates/argot-derivation-gate.py`, settled sha `07db6e9b…`,
  `--selftest` 18/18, paired control discriminating at 17:34:12Z). So the
  drafted subsection now cites the landed gate — but the claim's **stronger**
  clause is still not met: the delivered packet has `derived_pairs=0`, because
  the register-scoped argot data was never shipped (reading 4). Landing the
  subsection does not itself satisfy the claim; the LOG/SCORECARD drafts carry
  the status as **gate landed / domain empty**. Any reading of that gate must
  carry its own timestamp — the file moved twice inside this seat's write window
  (18 → 6 `register_scoped`, selftest red → green), and a third-party snapshot of
  a moving target is `to-verify` by construction.
- **F3 (citations are revision-bound).** Every digest in §3 is a worktree
  digest at `f74fc940`; sibling seats were editing the tree during this wave
  (`git status --porcelain` showed untracked `reports/round-25/**` and
  `corpus/lessons/README.md` at 17:29Z). A pin taken from a moving revision is
  `to-verify` by construction, and the orchestrator should re-hash at
  integration before quoting any digest above.
- **F4 (the delta is named, not absorbed).** The subsection's T3 carries the
  culture root cause and points at `reports/round-25/argot/delta.md`, which names
  F-1..F-8, the Δ1-class-2 register slots, Δ2 cardinality, AL-01..AL-06, the
  name-side argot and the eleven worked derivations, each with a source line. The
  draft does not restate them (that would be a second, drifting copy).
- **F5 (no filed-round edit).** This seat wrote only this file and
  `reports/round-25/docs/**` + `reports/round-25/integration/**`. Filed rounds
  8–24 are byte-untouched; the pins and rows the docs propose are **new rows**,
  never in-place edits of a filed receipt.

## 5. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/components/04-lexicon.yml \
  tools/gates/naming-collision-gate.py tools/gates/lexicon-coverage-audit.py \
  tools/gates/argot-derivation-gate.py tools/gates/typed-pipeline-gate.py SKILL.md
grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md
for t in ARGOT argot head2 derived_from derived_forms derived_ok doublet_of; do
  printf "%-14s examples=%s tools=%s\n" "$t" \
    "$(grep -rl -- "$t" examples/ 2>/dev/null | wc -l)" \
    "$(grep -rl -- "$t" tools/ 2>/dev/null | wc -l)"; done
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | grep -ci deriv   # 0
python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml ; echo "exit=$?"    # 0
python3 tools/gates/argot-derivation-gate.py --selftest 2>&1 | tail -1                       # 18/18
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml ; echo "exit=$?"  # 0, derived_pairs=0
python3 tools/gates/typed-pipeline-gate.py --selftest 2>&1 | tail -1                         # 19/19
bash .scratch/r25-d21/receipt.sh                                                                   # this seat's receipt
```

## 6. Limits

- Draft text only; the orchestrator owns placement, wording and admission. No
  `SKILL.md` byte was written by this seat.
- Readings bind to the digests and stamps above; a later edit to the packet, the
  gates or `SKILL.md` is a re-read event. The argot gate and the typed gate both
  moved inside this seat's write window, so every citation of them names its own
  stamp.
- The argot leg's status is **gate landed mid-wave, domain empty**: the mechanism
  is on disk and green over an empty set (`derived_pairs=0`), because the culture
  that hosts the argot did not ship. This file makes no claim that the claim's
  "implemented and executed on D4" clause is fully met, and the docs and
  integration drafts say so plainly.
