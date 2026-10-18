# R26-D03 — the register rules, machine-readable: the derivation-rule registry and its replay

- **Seat:** R26-D03 (D axis, register design 3 of 4), round 26, loop 3 build 2 of 4,
  claim **D** `register-stratum`.
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a`.
- **Design authority:** `reports/round-26/register/design.md` (D01);
  **forms:** `reports/round-26/register/forms.md` (D02).
- **Replay authority:** `SKILL.md:189-225` "Derivation replay — replay the
  family's own build, by text transform", row "Machine-readable pattern/output
  pairs"; `reports/round-17/d4/design-brief.md` Δ3 (`:296-310`).
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r26-d-reg/`. No tool, gate, packet, or filed 8–25 byte written.
- **Canon:** NON-CANON engineering rules.

## 1. The unmarked-register set

The gate's scope predicate must treat the unmarked register as unscoped, or it
grades the whole lexicon as argot. The delivered `argot-derivation-gate.py`
already does this (`UNMARKED_REGISTERS`, `argot-derivation-gate.py:112`); this design **adopts the set unchanged** and fixes the
marked register's name.

| register | class | in scope? |
|---|---|---|
| `plain` | unmarked baseline (the forge, the household, the road) | **no** — it is what the register is measured against |
| `stamp` | **the marked register** (attestation speech) | **yes** |

`stamp` is the single marked value this stratum introduces. The delivered
`symbols` block uses free-text register values (`"craft and law"`, `"public,
ambiguous"`, `"craft, in-ward"`); those are **medium registers** on symbol
records, not lexical registers on forms, and must not be read as argot registers
(`review.md` §6, RL-7).

## 2. The operation-selection rule (machine-readable)

```
rule REGISTER-OP-01 (design choice, round 26):
  scope:    every lexicon record with axis in {fire, mark}
  mapping:  axis == "mark"  ->  op = "reverse"
            axis == "fire"  ->  op = "lengthen"
  output:   the record's `derivation` field: {op: <op>, base: <term>}
  replay:   the gate computes apply(op, base) and compares to the record's form
```

This rule is **total by construction** over records that carry one of the two
delivered axis values, and it is **not total in effect**: 13 of the 54 lexicon
records produce a form that is illegal or colliding (`review.md` §3). The rule
is a *selection* rule; the form still has to survive the legality and collision
checks, which is why `forms.md` §1 verifies each of the 8 chosen forms
individually.

## 3. The derivation-rule registry entry (the packet bytes to add)

The registry the gate reads is `morphology.derivation_rules`
(`04-lexicon.yml:192-195`). Three entries are delivered; the stratum adds a
fourth:

```yaml
  - {id: LENGTHEN, kind: "vowel-length",
     pattern: "^(?P<onset>[^aeiou]*)(?P<vowel>[aeiou])(?P<rest>.*)$",
     output: "{onset}{vowel}{vowel}{rest}",
     note: "the register's length operation: the stressed root vowel is doubled"}
```

This is a valid `pattern`/`output` pair under the naming gate's template subset
(`_template_problem`, `naming-collision-gate.py:1259-1287`): plain `{name}`
placeholders, no conversion, no format spec, no indexing. Measured:

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-rule2.yml
coverage: … derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit 0
```

### 3.1 Why `reverse` cannot be a registry entry (RL-4)

`reverse` is a **character reversal**. The template subset accepts only
`{name}` placeholders resolving to a regex group; it refuses indexing and
format specs (`_template_problem`). A reversal is not expressible as
`"{a}{b}"`-style concatenation of the base's own characters without an index,
so `reverse` must stay a **computed operation** inside the gate (where it
already is, `OP_FUNCTIONS`, `argot-derivation-gate.py:171`) and never be moved into
`morphology.derivation_rules`. This is a real constraint, not a preference: the
r25 delta §3 measured that a `constructions`-route `ARGOT-REVERSE` row
manufactures a false red on a *correct* derivation
(`reports/round-25/argot/delta.md:3`). Keeping `reverse` computed is what avoids
that regression.

### 3.2 Why `head2` is not used (RL-2)

`head2` is retained in the gate as a declared operation (it is the forecast's,
and the gate's selftest re-derives the design's 11 worked rows from it), but
this design does **not** build any register form with it, because over the
delivered tree it is an identity, not a derivation — 59 of 62 delivered forms
are ≤2 syllables (`review.md` §4). A stratum built on `head2` would be a
stratum of unchanged words.

## 4. Declared limits of the rules

| id | limit | statement |
|---|---|---|
| **RU-1** | `lengthen` is undefined on a base whose first nucleus is a long vowel or a diphthong | `sau`, `dau`, `hai` are vowel-final delivered roots; the rule as written matches `[aeiou]` and would double only the first element. A base like `hai` under `lengthen` is **ambiguous** (`haai`? `haaai`?) and no such form is proposed. A later round using one must state its reading. |
| **RU-2** | `lengthen` targets the **first** nucleus, not "the stressed syllable" by rule | the two coincide for every delivered root because 02's stress is fixed root-initial (`STR-01`). A base with a prefix or a compound seam could separate them; no such base is proposed. |
| **RU-3** | the axis rule reads `axis`, which the contract does **not** list as a required lexicon field | `packet.d4.yml` `contract.record_fields.lexicon` = `id, term, gloss, field, route, bases, construction, layer, stage, axis, evidence, follows` — `axis` **is** present, so the rule is readable. Recorded because a contract change would silently empty the rule's domain. |
| **RU-4** | the rules are additive; no delivered rule changes | CX-01/02/03 keep their bytes; the register records use new `construction` ids (`STAMP-REVERSE`, `STAMP-LENGTHEN`) so no CX rule is overloaded. |

## 5. The era rule and its control (the Δ5 mechanism)

```
rule REGISTER-ERA-01:
  a record with register == "stamp" must carry stage >= E1
  a `stamp` record with stage E0  ->  D4L-ERA (FAIL)
```

**Control C-E1, measured:** a probe with every `stage: E1` rewritten to
`stage: E0`:

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/ctrl-early-era.yml
coverage: … records=164 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=6
era findings: NONE
exit 1
```

The gate emits **no era finding** — it has no era concept. So REGISTER-ERA-01 is
**specified here and unimplemented**; the exit-1 above is the undeclared
`lengthen` holds, not the era control. This is named, not laundered: the
mechanism's owner is whoever grows the leg (`review.md` §6, RL-8).

## 6. The machine-readable row set (what a consumer can replay)

| id | kind | pattern | output | status |
|---|---|---|---|---|
| `CX-01` | compound | `^(?P<a>.+)\+(?P<b>.+)$` | `{a}{b}` | delivered (`04-lexicon.yml:193`) |
| `CX-02` | suffix | `^(?P<stem>.+)$` | `{stem}ar` | delivered (`:194`) |
| `CX-03` | suffix | `^(?P<stem>.+)$` | `{stem}en` | delivered (`:195`) |
| `LENGTHEN` | vowel-length | `^(?P<onset>[^aeiou]*)(?P<vowel>[aeiou])(?P<rest>.*)$` | `{onset}{vowel}{vowel}{rest}` | **proposed by this design** |

`reverse` and `head2` are **computed operations**, not rows (`rules.md` §3.1,
§3.2). The row set above plus the two computed operations is the complete
derivation surface the register stratum needs.

## 7. Controls (the forecast's C-02 and this design's additions)

| # | control | command | expected | measured |
|---|---|---|---|---|
| C-02 | quote form ≠ `apply(op, base)` | `… probe-bad.yml` | `D4L-ARGOT-DERIV` FAIL | ✅ fires (`RF-02 'kat'`) |
| C-02b | the same for the **declared** `LENGTHEN` rule | `… probe-rule2-bad.yml` | `D4L-ARGOT-DERIV` FAIL | ✅ fires (`RF-06 'mis'`, `violations=1`) |
| C-02c | the rule declared with no `pattern`/`output` pair | `… probe-rule2-nopair.yml` | `D4L-ARGOT-RULE` HOLD, never silence | ✅ HOLD |
| C-02d | an undeclared operation | `… probe.yml` | `D4L-ARGOT-RULE` HOLD naming the op | ✅ 6 HOLDs naming `lengthen` |
| C-E1 | `stamp` form at E0 | `… ctrl-early-era.yml` | `D4L-ERA` FAIL | ❌ **no finding — unimplemented** |
| C-INV | an out-of-inventory register form | (reviewer D21 §2 measured) | FAIL | ❌ **no finding — unimplemented** |

The two ❌ rows are the honest state: the register stratum's *arithmetic* leg is
delivered and discriminating; its *typing* and *era* legs are not
(`review.md` §6).

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe.yml            # 6 HOLD, exit 1
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-rule2.yml     # 0 findings, exit 0
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-rule2-bad.yml # D4L-ARGOT-DERIV, exit 1
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-rule2-nopair.yml # D4L-ARGOT-RULE HOLD
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/ctrl-early-era.yml   # no era finding (gap)
grep -n "derivation_rules" -A 4 examples/culture-d4/components/04-lexicon.yml
```
