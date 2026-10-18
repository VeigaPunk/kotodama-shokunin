# R27-D23 — SKILL register-law rule draft

- round: 27 (operator: loop 3 of 3, build round 3 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R27-D23** (D-scribe 3 of 4).
- claim under draft: `reports/round-27/claims.json` claim **D**, axis `depth`,
  capability `register-law`.
- date: 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`.
  Lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- **final stamp 2026-10-18T19:23:26Z.** The tree moved twice in this seat's
  window (the syllabify fix and the register-law merge); every citation below is
  re-measured at the final stamp.
- **status: DRAFT ONLY — `SKILL.md` is not edited by workers.** The orchestrator
  lands the row below. This seat wrote no `SKILL.md`, `LOG.md`, `SCORECARD.md`,
  `corpus/**`, `tools/**`, `examples/**` or filed round-8–26 byte. Scratch under
  `.scratch/` only (`export TMPDIR=$PWD/.scratch` preceded every scratch write).
  No commit, no push.
- canon: **NON-CANON engineering draft.** No real language, script, institution
  or register is described, cited or approximated in it.

## 0. The finding that shapes this draft: the round-25 rule still never landed

**Measured 2026-10-18T19:23:26Z: `SKILL.md` carries no derivation-relations
rule.** `grep -c "Derivation relations" SKILL.md` → **0**. The file is byte-still
at `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048`, 598
lines, last written at `e06581b` (round-24 admit). The round-25 D seat drafted
the subsection verbatim and paste-ready; round 26 re-measured it absent and
supplied two landing shapes; **this is the third round it is absent and nothing
has changed in the file.** The last heading is still `### Family-clean
projection` (`SKILL.md:243`), ending at `<!-- END R23-D SKILL SUBSECTION -->`
(`SKILL.md:352`) before `## Error patterns` (`:354`).

Three consequences for this seat's row:

1. **The insertion point is unchanged and unambiguous.**
   `grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md` → `352`,
   `354`. Nothing has to be re-derived.
2. **This round's law is a delivered artifact, so the rule now describes bytes
   rather than a forecast.** Round 26 refused to land a register rule on top of
   an absent general one. The objection is moot for the *register law* (it is on
   disk) and live for the *derivation-relations* subsection (still absent), so
   §3 carries the general conditions inline.
3. **The recommended landing shape is §3** — a standalone register-law block
   whose content is the delivered law, with the general derivation conditions
   folded in as a sub-clause. If the round-25 subsection lands at the same time,
   §2 is the addition to it; land one, not both.

## 1. What the rule must say, and what it must not

The register law's craft content is now **five distinctions**, and the first four
are demonstrated by delivered bytes:

- **A register is a named social/stylistic variety, not a semantic field.** The
  component states it (`04-lexicon.yml:245-249`): "`register:` on a lexicon
  record is the scope, `field:` is the domain." A reader who conflated them would
  file the six `trade`/`craft` loan records as register members — and the argot
  gate would agree, because it scopes by loan layer.
- **A register law is a declaration about speech acts, not a lexicon
  annotation.** `QREG-02`'s `law` names the admissible slots and the holder;
  `13-register-law.yml`'s `RGL-01..05` state `act` / `holder` / `consequence`
  per row, with `kind` distinguishing `admissibility`, `exclusion`, `asymmetry`,
  `no-segment`, `era`. A law row that said only "the register exists" would be a
  label.
- **A register-scoped form stays on the checked channel.** `QREG-02` says it in
  its own words: "The register owns no segment: a stamp form is inventory-checked
  exactly as a plain form." `SKILL.md:149` and `:176-182` (T4) already teach the
  routing rule; the delivered law is its positive instance.
- **A law is declared and merged, never enforced — and the artifact must say
  so.** `13-register-law.yml`'s `law_binding.enforcement` states in its own
  words: "no gate executes these rows … The rows are a declared law with named
  non-execution, not a claim of enforcement." Measured: `grep -n "register_law"
  tools/assemble-culture-d4.py` → **no hits**; no lane gate reads either block.
  This is the distinction the round-26 draft could not make because the law did
  not exist.
- **A declared operation is not an exercised one.** `head2` is declared in
  `morphology.derivation_ops` and is an identity over the delivered tree; the
  leg never exercises it. A row that cited `head2` as a demonstrated capability
  would be false.

The rule must **not** claim that the law is enforced, that the register rule
substitutes for the derivation-relations rule, that a green argot run implies a
complete register system, or that a register hold is a defect to repair.

## 2. LANDING-READY — the register row, as an addition to a derivation subsection

If the orchestrator lands a derivation-relations subsection (round 25's draft is
paste-ready), append this row to its table. Columns match round 26's proposed
table (`Derivation requirement | Correct shape | Never | Consequence if violated | Citation`).

```markdown
| Register law declaration | a component declares the register's identity and class (`registers`: `register`, `class`, and a `law` naming the admissible slots and the holder) **and** its speech-act rows (`register_law`: `act`, `holder`, `consequence`, `kind`), each row carrying its own `kind` so admissibility, exclusion, asymmetry, no-segment and era are distinguishable; the assembler honors the component's per-file `packet_keys` and merges both blocks deterministically | declare a register by annotating a `field:` value; leave the law with no owning component while the gate grades register-scoped records; state an operation rule without its domain | the register is unowned: the gate scopes records it cannot explain, and a reader takes a `field` for a `register` | `examples/culture-d4/components/13-register-law.yml` (`RGL-01..05`) and `04-lexicon.yml:244-253` (`QREG-01..04`); `tools/assemble-culture-d4.py:74-79` (the per-file `packet_keys` path); measured `reports/round-27/scribe/capability-row.md` §3.1 |
| Register-scoped *slot* obligation | a supplied, inventory-clean form in one slot leaves the sibling slot owed as a **hold** naming the owed slot; the pair relation is a packet fact (`doublet_of`), and one owed pair yields exactly one hold | count one obligation twice because the projection keys it twice; launder the owed slot into a note to make a count green | an under- or over-counted obligation set; the gate's slot comparison fails | `SKILL.md:149-166` (the routing table's register row and T3); `examples/culture-d4/expected-holds.json` (hold:12 / note:0 / fail:0) |
```

And these two cautions, which are part of the rule:

- **T5 — a register law is declared and merged, never enforced.** Measured: no
  gate reads `registers:` or `register_law:`, and the assembler's `PACKET_KEYS`
  does not even list `register_law` (the block arrives by the per-file
  `packet_keys` path). The register law's checker in round 27 is an **audit
  instrument, not a lane gate**
  (`reports/round-27/audit/x59-register-law-negatives.py`), and its surviving
  finding is exactly that a tampered law value changes no delivered gate's
  findings.
- **T6 — the register domain can be empty while the mechanism is green, and the
  delivered instance is the opposite case.** Round 26 measured the argot leg
  green over an **empty** domain (`register_scoped=6 derived_pairs=0`); the
  delivered tree reads `register_scoped=14 derived_pairs=8`. Both are facts about
  the *domain*, never about the mechanism's soundness. The landing gate a
  capability row must carry is `derived_pairs > 0`, and it is now met.

## 3. LANDING-READY — the register-law rule standalone (recommended shape)

Insert after `<!-- END R23-D SKILL SUBSECTION -->` (`SKILL.md:352`), before
`## Error patterns` (`SKILL.md:354`). Self-contained: it repeats the general
derivation conditions the register case inherits.

```markdown
### Register law — a register is a speech-act scope, and a register form is a declared relation

A **register** is a named social/stylistic variety of one language, not a
semantic field: `register:` on a record is the **scope**, `field:` is the
**domain**, and a reader who conflates them will file every loan of a trade layer
as a register member. A register stratum is **declared by a component**, not
inferred from annotations, and it takes **two blocks**: the identity rows
(`registers`: the register's name and class, and a `law` naming the admissible
slots and the holder) and the **speech-act rows** (`register_law`: `act` — what
may be said, `holder` — by whom, `consequence` — the record consequence, and
`kind` — admissibility / exclusion / asymmetry / no-segment / era). The
assembler must whitelist and merge the blocks deterministically, or the law is a
design note with no carrier. Executable authority `tools/assemble-culture-d4.py`
(the per-file `packet_keys` path and `RECORD_FIELDS`; `--check` byte-identical,
`--selftest` 81/81); worked instance
`examples/culture-d4/components/13-register-law.yml` (`RGL-01..05`) with
`examples/culture-d4/components/04-lexicon.yml:244-253` (`QREG-01..04`), merged
at `examples/culture-d4/packet.d4.yml` (`registers:` and `register_law:`).

A **register-scoped form** carries two independent obligations. First, its
register value is a claim about **social distribution**, never about whether the
string is a form: a register-scoped form stays on the sound and identity channel
exactly as a plain form does, and a register label never licenses moving a string
off it (the round-8 T1 discipline read in the new direction — `SKILL.md:47`;
`SKILL.md:149,176-182`). Second, a register-scoped form that **claims a
derivation** from a base is a cross-record relation, and it is checkable only
when the packet's schema can express it (a base field plus a declared operation),
the replay engine can **compute** the declared operation rather than concatenate,
and the stated inputs replay to the delivered form. The D4 stamp stratum is the
worked instance: `mark -> reverse`, `fire -> lengthen`, eight delivered pairs,
replay clean. Executable authorities `tools/gates/argot-derivation-gate.py` (ids
`D4L-ARGOT-DERIV` FAIL / `D4L-ARGOT-RULE` HOLD / `D4L-ARGOT-COVERAGE` HOLD /
`D4L-ARGOT-DATA` exit 2; `--selftest` 27/27; flagless and single-input so
`tools/replay-frozen.py` can pin a row) and `tools/gates/typed-pipeline-gate.py`
(`L3b-argot`, which folds an argot FAIL into the D4 verdict); design authority
`reports/round-17/d4/design-brief.md` §6 and
`reports/round-17/d4/design-language.md` §5; measured instance
`reports/round-26/register/`, `reports/round-27/law/` and
`reports/round-27/scribe/capability-row.md`.

| Register requirement | Correct shape | Never | Consequence if violated | Citation |
|---|---|---|---|---|
| Register is scope, not field, and not channel | a register-scoped form keeps its checked form; the register value is a scope fact, and the routing table gains **no** row from it | declare a register by annotating a `field:` value; promote the register value into `off_channel_field`; let a register label remove a string from the checked channel | a register-scoped exemption is the round-8 T1 violation at a new address; the naming kernel then grades a form that should not have been moved, or skips one that should | `SKILL.md:47,149,176-182`; `examples/culture-d4/components/04-lexicon.yml:245-249` |
| The law has an owner and two blocks | a component declares the identity rows **and** the speech-act rows, each speech-act row carrying `act`/`holder`/`consequence`/`kind`; the assembler honors the component's `packet_keys` and merges deterministically | leave the law as prose in a round report while the gate grades register-scoped records; merge an identity block and call it a law | the register is unowned: the gate scopes records it cannot explain, and the law is unfalsifiable | `examples/culture-d4/components/13-register-law.yml`; `tools/assemble-culture-d4.py:74-79`; `reports/round-26/register/design.md` §6.3 (the gap this closes) |
| A declared law is not an enforced law | the component states its own non-execution (`law_binding.enforcement`), and the capability row repeats it | claim the law is checked when no gate reads it; cite an audit instrument as a lane gate | a reader treats a declaration as a clearance; a tampered law value changes no verdict and nobody notices | `examples/culture-d4/components/13-register-law.yml` (`law_binding.enforcement`); `reports/round-27/audit/x59-register-law-negatives.py` |
| An operation rule carries its domain | the rule is stated **and** its non-totality is stated in the same cell ("13 of the 54 delivered records yield an unusable form") | state an operation rule as if it were productive over the whole lexicon | a reader concludes the register is total; a form the rule cannot produce is read as a defect instead of a domain limit | `examples/culture-d4/components/04-lexicon.yml:252` (`QREG-03`) |
| Register-scoped derivation | the base and the operation are declared in the schema (`derived_from` + `derivation`, or a packet rule id) and the replay dispatches on the operation | infer the relation from the `register` field, from a rule's *name*, or from prose; let a concatenation-only replayer grade a non-concatenative operation | the relation is uncheckable: a correct non-concatenative derivation is a false FAIL and a non-derivation passes | `tools/gates/argot-derivation-gate.py`; `reports/round-25/argot/current-state.md` §6.2 (controls N-2/N-3/N-4) |
| The leg discriminates | a control mutates the relation and the leg names the record, the rule and the disagreeing pair; the untouched pair passes | a control that only re-runs the green path | a leg that always passes is capability, not measurement | `reports/round-26/scribe/capability-row.md` §5 (CTL-A exit 0 / CTL-B `D4L-ARGOT-DERIV` exit 1 / CTL-C `D4L-ARGOT-RULE` exit 1) |
| An empty domain is reported, not simulated | where the delivered packet carries no register-scoped derivation, the leg's own coverage line (`derived_pairs=0`) is reported as a landed mechanism with no domain | present a green run over an empty set as a demonstrated register capability | the signature "zero fails" is satisfied vacuously and read as a delivery | measured `reports/round-26/scribe/capability-row.md` §0/§4; round-25 T4 |
| A declared operation is not an exercised one | where an operation is declared but unused (`head2` over the delivered tree is an identity), say so and say the leg never exercises it | cite a declared operation as a demonstrated capability | a stratum appears exercised when the leg's coverage line says otherwise | `examples/culture-d4/packet.d4.yml:250`; `reports/round-26/register/review.md` §4 |
| One algorithm, stated once | the leg's `syllabify` and the design's stated algorithm are the same algorithm, and a third witness inside the artifact (the packet's own author-declared `syllables:`) adjudicates a disagreement | let the engine implement a reading its own cited authority rejects; count divergences with an instrument whose splitter violates the stated legality clause | the leg grades a form against an algorithm no design declared, and the count of divergences becomes instrument-dependent | `reports/round-17/d4/design-language.md:191-196`; `reports/round-27/scribe/x54-syllabify-spotcheck.py` |
| Register history is a fourth clock | a register's emergence is a dated fact (`era_rule`, `available_from`), and form / sense / object / register histories stay separate | synthesize a CE date or intersect the clocks to manufacture one | a register claimed before its emergence is a `D4L-ERA`-class failure, and a prose-only span must hold with the raw text retained | `examples/culture-d4/components/04-lexicon.yml:253` (`QREG-04`); `reports/round-17/d4/design-brief.md` §6 Δ5; `corpus/knowledge/synthesis/era-language-staging.md:139` |

Cautions that are part of the rule: a **declared** law is not an **enforced**
law — no lane gate reads `registers:` or `register_law:`, and the round-27
checker that does is an audit instrument, not a gate; a green register leg is not
canon, lore acceptance or a real-world register claim; a register-scoped *hold*
is owed design debt, never a defect to repair into a pass; and where a shared
replay engine is reused across families, the family-clean projection rule above
still governs which records a register relation may name (`SKILL.md:243-352`).
```

## 4. Row placement and the citation ledger

**Placement.** `grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md`
→ `352`, `354`. The insertion point is unambiguous and leaves the R23-D block
byte-intact.

**Citation ledger.** Every cited path resolves; digests are worktree digests at
`b95fca1e`, measured 2026-10-18T19:23:26Z.

| cited path | sha256 | resolves |
|---|---|---|
| `SKILL.md` (at draft time) | `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048` | yes |
| `examples/culture-d4/components/13-register-law.yml` | `40f774cb7a69abae9d5914abad54d4c8b6bf63b30003b151c48ae3fbfb7dad7a` | yes |
| `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240` | yes |
| `examples/culture-d4/components/01-brief.yml` | `feca7bda25beb6ec7cecd2569fe8f8d6d802ff492f40c79cb6c58fdf5ac18d7d` | yes |
| `examples/culture-d4/packet.d4.yml` | `c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a` | yes |
| `examples/culture-d4/expected-holds.json` | `b9f98381f382cbff13a1b0d2ac6edaba901ff43aef68d385305edc313997cd96` | yes |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | yes |
| `tools/gates/argot-derivation-gate.py` | `d7a3ad1a6ad1c4c5993b7d74bf8bc96326916f113a07e6472d90ceecd7faf1aa` | yes |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | yes |
| `reports/round-17/d4/design-language.md` | `cfc2d698559ed552c85b527c3a34e32e4fe308cfd093137483f9d3c782b462cc` | yes |
| `reports/round-26/register/design.md` | `27d23fa67d0bb920d1841d25c82b09919419ef58ef3b2f75494d950f3b5bb55a` | yes |
| `reports/round-26/register/review.md` | `0082f08b62986ab2091a07acee464888fd68fa5312f19ef1b3817111a05f96e1` | yes |
| `reports/round-27/audit/x59-register-law-negatives.py` | `e86f630319c646e3aec0588d8683d78844c4d34e9b25ded34c36e98e1bf9d8ba` | yes |
| `reports/round-27/scribe/x54-syllabify-spotcheck.py` | `ee370f782c02b36b2333aaf79224a0047393d5ce3c2008b285a3eeab985165e2` | yes |

Line anchors re-checked at draft time (19:23Z): `SKILL.md:47`, `:149`,
`:176-182`, `:243-352`, `:352`/`:354`; `04-lexicon.yml:244-253`, `:262-263`;
`13-register-law.yml:18` (`packet_keys: [register_law]`), `:24-32` (`register_law`
rows), `:34-40` (`law_binding`, incl. `enforcement`); `packet.d4.yml:250`
(`derivation_ops_note`); `tools/assemble-culture-d4.py:74-79` (the per-file
`packet_keys` path) and `:118` (`RECORD_FIELDS["registers"]`).

## 5. The counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum SKILL.md examples/culture-d4/components/13-register-law.yml \
  examples/culture-d4/components/04-lexicon.yml examples/culture-d4/packet.d4.yml \
  tools/assemble-culture-d4.py tools/gates/argot-derivation-gate.py
grep -c "Derivation relations" SKILL.md                             # 0 — the round-25 rule never landed
grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md   # 352 / 354
grep -c "^registers:"     examples/culture-d4/packet.d4.yml         # 1
grep -c "^register_law:"  examples/culture-d4/packet.d4.yml         # 1
grep -rn "register_law" tools/assemble-culture-d4.py                # 0 — merged via the per-file packet_keys path
grep -n "enforcement" examples/culture-d4/components/13-register-law.yml  # the law states its own non-execution
python3 tools/assemble-culture-d4.py --check                        # exit 0, byte-identical
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | head -1
  # coverage: records=175 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=0
python3 tools/gates/argot-derivation-gate.py --selftest 2>&1 | tail -1   # 27/27
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1  # 20/20
python3 reports/round-27/audit/x59-register-law-negatives.py --controls                  # 7/7 caught
```

## 6. Limits

- Draft text only; the orchestrator owns placement, wording and admission. No
  `SKILL.md` byte was written by this seat, and this draft admits nothing.
- The rule describes a **delivered** law and a **delivered** derivation leg. It
  does **not** describe an enforced law: no lane gate reads `registers:` or
  `register_law:`, and the artifact says so in its own `law_binding`.
- The rule carries the general derivation conditions inline because the
  derivation-relations subsection has now been absent for three rounds. If that
  subsection lands, §2 is the addition to it and §3 becomes redundant.
- Readings bind to the digests and stamps above, and **the tree moved twice in
  this seat's window**; a successor seat must re-hash before quoting.
- This file makes no claim that the round-27 D claim is met. It supplies the
  rule text and names the insertion point.
