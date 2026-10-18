# R26-D26 — SKILL register-rule row draft: the register stratum

- round: 26 (operator: loop 3 of 3, build round 2 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R26-D26** (D-scribe 2 of 4).
- claim under draft: `reports/round-26/claims.json` claim **D**, axis `depth`,
  capability `register-stratum`.
- date: 2026-10-18. Declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`.
  Lane HEAD at every measurement `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **status: DRAFT ONLY — `SKILL.md` is not edited by workers.** The orchestrator
  lands the row below. This seat wrote no `SKILL.md`, `LOG.md`, `SCORECARD.md`,
  `corpus/**`, `tools/**`, `examples/**` or filed round-8–25 byte. Scratch under
  `.scratch/r26d/` only (`export TMPDIR=$PWD/.scratch` preceded every scratch
  write). No commit, no push.
- canon: **NON-CANON engineering draft.** No real language, script, institution
  or argot is described, cited or approximated in it.

## 0. The finding that shapes this draft: the round-25 rule never landed

**Measured 2026-10-18T18:05:45Z: `SKILL.md` carries no derivation-relations
rule.** `grep -c "Derivation relations" SKILL.md` → **0**. The file is byte-still
at `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048`, 598
lines, last written at `e06581b` (round-24 admit). The round-25 D seat drafted
the subsection verbatim and paste-ready
(`reports/round-25/rule/skill-draft.md`, `### Derivation relations …`, ending
`<!-- END R25-D SKILL SUBSECTION -->`), and the round-25 integration draft named
the landing as the orchestrator's job with a parent-fill slot
(`reports/round-25/integration/scorecard-draft.md:53-55`: "**The D rule is
landed, not just drafted** … 'Drafted' alone is not the [claim]"). **It did not
land.** The last `SKILL.md` heading is `### Family-clean projection`
(`SKILL.md:243`), whose block ends at the `<!-- END R23-D SKILL SUBSECTION -->`
marker (`SKILL.md:352`) before `## Error patterns` (`:354`).

Two consequences for this seat's row:

1. **The insertion point is still exactly where round 25 said it was.**
   `grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md` → `352`,
   `354`. The round-25 draft's placement finding reproduces; nothing has to be
   re-derived.
2. **This round cannot honestly land a *register-stratum* rule on top of an
   absent *derivation-relations* rule.** The register rule is the special case;
   the derivation rule is the general one. A SKILL that teaches "a
   register-scoped form is checkable only when its operation is declared and
   computable" without first teaching "a derivation relation is checkable only
   when the schema and the engine can carry the operation" would invert the
   craft's own layering. **§2 therefore supplies the register row as an addition
   to the round-25 subsection text, and §3 supplies it standalone** so the
   orchestrator can land either shape.

## 1. What the rule must say, and what it must not

The register stratum's craft content is **one distinction**, and it is the
distinction the round-17 Δ1 forecast drew and the round-25 delta measured as
unbuilt:

- A **register field is a claim about who says a form** — its social
  distribution. It is never a claim about whether the string is a form, and it
  never licenses moving a string off the checked channel. `SKILL.md:149` already
  states this for the *routing* table ("promote the register value into
  `off_channel_field`" is the named anti-pattern), and `SKILL.md:176-182` states
  it as T4.
- A **register-scoped slot is a second obligation on the same record**, not a
  second record: the quote slot can be supplied and inventory-clean while the
  plain slot it must also fill stays owed, and the owed side is a **hold**, never
  a pass and never a note.
- A **register-scoped derivation** (the argot case) is a cross-record relation
  and inherits every condition of the derivation-relations rule: a base field, a
  declared operation, an engine that can compute it, and a replay that names the
  disagreeing pair.

The rule must **not** claim: that the register stratum is implemented in D4
(it is not — §0 and `reports/round-26/scribe/capability-row.md` §0); that a
green argot run implies a complete register system (the leg's own docstring
refuses that reading); that a register hold is a defect to repair (it is owed
design debt, like the six garment slots); or that a register label is a channel.

## 2. LANDING-READY — the register row, as an addition to the round-25 subsection

If the orchestrator lands `reports/round-25/rule/skill-draft.md`'s subsection
first (it is paste-ready and its citations are still resolvable), append this
row to that subsection's table and these cautions to its list. The row's columns
match the round-25 table exactly
(`Derivation requirement | Correct shape | Never | Consequence if violated | Citation`).

```markdown
| Register-scoped derivation | a register-scoped form's base and operation are declared in the packet's own schema (`derived_from` + `derivation`, or a packet rule id), and the replay dispatches on the operation; a form the stated inputs and rules do not yield is `D4L-ARGOT-DERIV` FAIL, an unreplayable declaration is `D4L-ARGOT-RULE` HOLD, and a declared-but-undelivered relation is `D4L-ARGOT-COVERAGE` HOLD | infer the relation from the record's `register` field, from a rule's *name*, or from prose ("the quote form reverses the plain one"); let a register label exempt a string from the checked channel | the relation is uncheckable and a correct non-concatenative derivation is a false FAIL while a non-derivation passes; a register-scoped exemption is the round-8 T1 violation at a new address (`SKILL.md:47`) | `tools/gates/argot-derivation-gate.py` (`OPS` `:121-133`, `record_register` `:293-317`, `declared_derivation` `:320`, `evaluate_packet` `:470-597`; flagless and single-input so `tools/replay-frozen.py` can pin a row); `tools/gates/typed-pipeline-gate.py:517-541` (`L3b-argot`, folds a FAIL into the verdict); design authority `reports/round-17/d4/design-brief.md` §6 Δ1-Δ3 (`:254-310`); measured controls `reports/round-26/scribe/capability-row.md` §5 |
| Register-scoped *slot* obligation | a supplied, inventory-clean form in one slot leaves the sibling slot owed as a **hold** naming the owed slot; the pair relation is a packet fact (`doublet_of`), and one owed pair yields exactly one hold | count one obligation twice because the projection keys it twice (the slot record and the owner record are one obligation seen from two sides); launder the owed slot into a note to make a count green | an under- or over-counted obligation set; the gate's slot comparison fails | `SKILL.md:149-166` (the routing table's register row and T3); `reports/round-17/d4/design-brief.md` §6 Δ1-Δ2 (`:254-295`); `reports/round-18/d4/holds.md` §4; worked instance `examples/culture-d4/expected-holds.json` (counts hold:12 / note:0 / fail:0, all twelve rows the owed garment/slot form holds) |
```

And these two cautions, which are part of the rule:

- **T5 — the register stratum's domain can be empty while its mechanism is
  green.** Measured: the argot leg exits **0** over the delivered D4 packet with
  `register_scoped=6 derived_pairs=0` — it is green because it has no register
  derivation to grade, and the six register-scoped records it finds are six
  *loan* records reached through their layer, not quote-register forms
  (`reports/round-26/scribe/capability-row.md` §4). A green register leg over an
  empty domain is a **landed mechanism with no domain** — the round-25 T4
  wording, restated for this stratum — never a demonstrated register capability.
  The landing gate for any capability row is `derived_pairs > 0`.
- **T6 — a register-scoped form is checked exactly as a native form is.** The
  round-17 Δ1 signature: "every quote form appears in the sound gate's inventory
  exactly as a native form does (same finding class, same field read)". A
  register rule that produces a *different* finding class for a register-scoped
  form has changed the channel, not added a scope. The delivered bytes are the
  negative instance: `examples/culture-d4/typed-labels.d4.yml` types 74 labels as
  56 `native-form` / 12 `translated-label` / 6 `borrowed-strata` with **no
  register-scoped kind**, so a reader cannot see a register scope in the
  projection at all.

## 3. LANDING-READY — the register rule standalone (if the round-25 subsection does not land)

If the orchestrator decides to land only the register rule, use this block. It
is self-contained and repeats the general conditions the register case inherits,
so it does not depend on the absent subsection. Insert after
`<!-- END R23-D SKILL SUBSECTION -->` (`SKILL.md:352`), before
`## Error patterns` (`SKILL.md:354`).

```markdown
### Register-scoped forms — a register is a claim about who says a form, and a derivation is a relation the schema must carry

A **register-scoped form** is a record whose use is limited to a declared
register (quote, trade, craft, ritual, taboo, sacred, …). Two rules govern it and
they are independent. First, a `register` field is a claim about **social
distribution**, never about whether the string is a form: a register-scoped form
stays on the sound and identity channel exactly as a native form does, and a
register label never licenses moving a string off it (the round-8 T1 discipline
read in the new direction — `SKILL.md:47`; `SKILL.md:149,176-182`). Second, a
register-scoped form that **claims a derivation** from a base is a cross-record
relation, and it is checkable only when the packet's schema can express it (a
base field plus a declared operation), the replay engine can **compute** the
declared operation rather than concatenate, and the stated inputs replay to the
delivered form. The D4 chain is the worked instance; the argot half landed in
round 25 and its register domain is the named gap. Executable authorities
`tools/gates/argot-derivation-gate.py` (ids `D4L-ARGOT-DERIV` FAIL /
`D4L-ARGOT-RULE` HOLD / `D4L-ARGOT-COVERAGE` HOLD / `D4L-ARGOT-DATA` exit 2;
`OPS` `:121-133`; `--selftest` 21/21; flagless and single-input so
`tools/replay-frozen.py` can pin a row), `tools/gates/typed-pipeline-gate.py`
(`L3b-argot` `:517-541`, which folds an argot FAIL into the D4 verdict), and the
routing table above; design authority `reports/round-17/d4/design-brief.md` §6
Δ1-Δ3 (`:254-310`) and `reports/round-17/d4/design-language.md` §5 (`:186-217`);
measured instance and delta `reports/round-25/argot/`; round-26 measurements
`reports/round-26/scribe/capability-row.md`.

| Register requirement | Correct shape | Never | Consequence if violated | Citation |
|---|---|---|---|---|
| Register is scope, not channel | a register-scoped form keeps its checked form; the register value is a scope fact, and the routing table gains **no** row from it | promote the register value into `off_channel_field`; let a register label remove a string from the checked channel | a register-scoped exemption is the round-8 T1 violation at a new address; the naming kernel then grades a form that should not have been moved, or skips one that should | `SKILL.md:47,149,176-182`; `reports/round-17/d4/design-brief.md` §6 Δ1 signature (`:262-266`) |
| The sibling slot is an obligation, not a gap | a supplied form in one slot leaves the sibling slot owed as a **hold** naming the owed slot; one owed pair yields exactly one hold | count one obligation twice because the projection keys it twice; launder the owed slot into a note | an under- or over-counted obligation set; the gate's slot comparison fails | `SKILL.md:149-166`; `reports/round-17/d4/design-brief.md` §6 Δ2 (`:283-295`); `examples/culture-d4/expected-holds.json` (hold:12 / note:0 / fail:0) |
| Register-scoped derivation | the base and the operation are declared in the schema (`derived_from` + `derivation`, or a packet rule id) and the replay dispatches on the operation | infer the relation from the `register` field, from a rule's *name*, or from prose; let a concatenation-only replayer grade a non-concatenative operation | the relation is uncheckable: a correct non-concatenative derivation is a false FAIL and a non-derivation passes | `tools/gates/argot-derivation-gate.py:320-460`; `reports/round-25/argot/current-state.md` §6.2 (controls N-2/N-3/N-4) |
| The leg discriminates | a control mutates the relation and the leg names the record, the rule and the disagreeing pair; the untouched pair passes | a control that only re-runs the green path | a leg that always passes is capability, not measurement | `reports/round-26/scribe/capability-row.md` §5 (CTL-A exit 0 / CTL-B `D4L-ARGOT-DERIV` exit 1 / CTL-C `D4L-ARGOT-RULE` exit 1) |
| An empty domain is reported, not simulated | where the delivered packet carries no register-scoped derivation, the leg's own coverage line (`derived_pairs=0`) is reported as a landed mechanism with no domain | present a green run over an empty set as a demonstrated register capability | the signature "zero fails" is satisfied vacuously and read as a delivery | measured `reports/round-26/scribe/capability-row.md` §0/§4; `reports/round-25/argot/delta.md` §1 F-5; round-25 T4 |
| Register history is a fourth clock | a register's emergence is a dated fact (`available_from`), and form / sense / object / register histories stay separate | synthesize a CE date or intersect the clocks to manufacture one | a register claimed before its emergence is a `D4L-ERA`-class failure, and a prose-only span must hold with the raw text retained | `reports/round-17/d4/design-brief.md` §6 Δ5 (`:328-341`); `corpus/knowledge/synthesis/era-language-staging.md:139` |

Cautions that are part of the rule: a green register leg is **not** canon, lore
acceptance, or a real-world register claim; a register-scoped *hold* is owed
design debt, never a defect to repair into a pass; and where a shared replay
engine is reused across families, the family-clean projection rule above still
governs which records a register relation may name (`SKILL.md:243-352`).
```

## 4. Row placement and the citation ledger

**Placement.** `grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md`
→ `352`, `354`. The insertion point is unambiguous and leaves the R23-D block
byte-intact. The proposed heading continues the existing sequence (Label typing
→ Claim uncertainty → Slot-label routing → Derivation replay → Family-clean
projection) with the stratum the routing table's register row already points at.

**Citation ledger.** Every cited path resolves; digests are worktree digests at
`1ad491a1`, measured 2026-10-18T18:05:08Z.

| cited path | sha256 | resolves |
|---|---|---|
| `SKILL.md` (at draft time) | `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048` | yes |
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` | yes |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | yes |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | yes |
| `tools/gates/lexicon-coverage-audit.py` | `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287` | yes |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | yes |
| `examples/culture-d4/components/04-lexicon.yml` | `74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5` | yes |
| `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` | yes |
| `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` | yes |

Line anchors re-checked at draft time (18:05Z): `SKILL.md:47` (T1 "adding typing
fields cannot exempt a string"), `:149` (the routing table's register row),
`:176-182` (routing T4), `:243-352` (family-clean block), `:352`/`:354` (insertion
point), `tools/gates/argot-derivation-gate.py:121-133` (`OPS`),
`:293-317` (`record_register`), `:320` (`declared_derivation`), `:470-597`
(`evaluate_packet`), `tools/gates/typed-pipeline-gate.py:517-541` (`L3b-argot`),
`examples/culture-d4/packet.d4.yml:205-226` (`morphology.derivation_rules`).

## 5. The counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum SKILL.md tools/gates/argot-derivation-gate.py tools/gates/typed-pipeline-gate.py \
  examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml \
  examples/culture-d4/expected-holds.json
grep -c "Derivation relations" SKILL.md                       # 0 — the round-25 rule never landed
grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md   # 352 / 354
grep -rn "registers:\|doublets:\|doublet_of\|#plain\|#quote" examples/ tools/   # 0 — the stratum is not on disk
python3 tools/gates/argot-derivation-gate.py --selftest 2>&1 | tail -1   # 21/21
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
  # exit 0, coverage: records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1   # 20/20 legs
```

## 6. Limits

- Draft text only; the orchestrator owns placement, wording and admission. No
  `SKILL.md` byte was written by this seat, and this draft admits nothing.
- The rule is drafted for a stratum that is **not implemented**: the register
  schema, the slot pairs and the derivation pairs are all absent from the
  delivered bytes (§0, and `reports/round-26/scribe/capability-row.md` §4). The
  rule is written to be true **when** they land, and every row's citation is to
  a mechanism that exists today or a design document that specifies the missing
  part.
- Readings bind to the digests and stamps above. The argot gate and the typed
  gate both moved between round 25 and this seat's measurement
  (`07db6e9b…`→`5b5abe78…` and `879d40bf…`→`b749ad07…`), so every citation of
  them names its own stamp; a successor seat must re-hash before quoting.
- This file makes no claim that the round-26 D claim is met. It supplies the
  rule text and names the two shapes the orchestrator can land.
