# R27-D19 — adversarial review 3 of 4: a register form on the wrong channel

- **Seat:** R27-D19 (reviewer 3 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`;
  lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`. Measurement stamp
  **2026-10-18T19:33:47Z**.
- **Review target:** the register leg's **cross-check against the label-typing
  table** (`SKILL.md:31-84`), whose executable authority is
  `tools/d2-typed-labels.py` (sha256 `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3`),
  measured against the landed gate (`b5406bcdaf41c595…`).
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r27-d19/`. `export TMPDIR=$PWD/.scratch` preceded every scratch
  write. **No tool, gate, packet, component, projector, pin or filed rounds
  8–26 byte was written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 3 of 4, cross-checking the register leg **against the
label-typing table**. Round 26's reviewer 2 (`reports/round-26/argot/D22-label-typing-crosscheck.md`)
measured three consequences of the leg having no concept of a label kind. This
file **re-measures all three against the landed bytes** and asks the one
question round 26 could not: has the round-27 law landing changed them?

**Verdict in one line.** **No — all three round-26 classes still reproduce
exactly.** The leg still has no label kind, still counts **every** non-`plain`
register value as an argot register, and its `register_scoped` headline count
still measures the loan-layer scope rather than the `stamp` stratum the round-27
claim is about. The round-27 law landing **added** register-scoped rows to the
leg's domain (`register_scoped` 14, of which **8** are the new `stamp` forms)
without adding the typing leg, so the law's forms are now graded by a leg that
would equally grade a gloss.

## 1. The three round-26 classes, re-measured on the landed tree

The controls are the round-26 reviewer's own shapes, rebuilt here as full-packet
mutations (the round-26 probes were minimal packets; these are the delivered
packet plus one record, so the finding cannot be blamed on a degenerate input).

**C1 — a reader-facing English gloss on a register-scoped slot reads green.**
`SKILL.md:41`: a gloss is `translated-label`, "**never** — not on the sound or
identity channel".

```
# .scratch/r27-d19/C1-full-gloss-on-register-slot.yml  (delivered packet + one record)
  - {id: Q-01, term: "wool coat", register: stamp, gloss: "a coat",
     axis: mark, evidence: design-choice}

$ python3 -B tools/gates/argot-derivation-gate.py …C1-full-gloss-on-register-slot.yml
coverage: … records=171 register_scoped=15 derived_pairs=8 … violations=0 rule_holds=0
exit 0

$ python3 -B tools/d2-typed-labels.py --packet …C1-full-gloss-on-register-slot.yml
FINDING D2L-NATIVE: [fail] Q-01 — supplied form 'wool coat' carries symbols outside
  the declared inventory: ['c']
```

**Same bytes, two gates, opposite verdicts**: the projector **fails** the gloss
and names the offending segments; the argot leg **passes** it and counts it as a
register-scoped form (`register_scoped` 14 → 15). The label-typing table is the
governing rule and the argot leg does not implement it.

**C2 — every register value is treated as an argot register.**

```
# .scratch/r27-d19/C2-full-prose-register.yml
  - {id: Q-02, term: "taoc loow", register: "craft and law", gloss: "probe",
     axis: mark, evidence: design-choice, derived_from: "wool coat", derivation: reverse}

$ python3 -B tools/gates/argot-derivation-gate.py …C2-full-prose-register.yml
coverage: … register_scoped=15 derived_pairs=9 … violations=0 rule_holds=0
exit 0
```

A **prose medium register** (`"craft and law"`, the string the packet's own
`symbols` records carry at `SYM-01`) is counted as a register scope and its
"derivation" is **replayed and passed**. Measured directly on the gate's own
scope predicate:

```
$ python3 - <<'PY'   # the gate's own record_register() over every block
  contact      CT-01   register='trade'
  layers       LY-01   register='trade'
  lexicon      L-49    register='trade'          # the six loans
  lexicon      L-56    register='stamp'          # the eight register forms
  register_law RGL-01  register='stamp'          # the five law rows
  registers    QREG-02 register='stamp'
  symbols      SYM-01  register='craft and law'  # a MEDIUM register, not a form register
  symbols      SYM-05  register='ritual'
  …
total: 34 scoped rows across 6 blocks
```

`symbols` records carry `form:` fields describing a **medium** (the mold-mark,
the tally face), not language forms — `is_form_record` (`:343`) is supposed to
route them off the channel. They are still scoped, and `"craft and law"` is
still treated as an argot register. Round 26 measured this as its finding (2);
it is unchanged.

**C3 — the headline `register_scoped` measures the loan layer, not the stratum.**
Measured by the gate's own scope function over the delivered packet, the 14
scoped rows the coverage line reports are:

```
lexicon L-49..L-54   register='trade'/'craft'   (the six LOANS, scoped via their layer)
lexicon L-55..L-62   register='stamp'           (the eight round-26 register forms)
```

So `register_scoped=14` is **6 loans + 8 register forms**. A consumer reading the
coverage line as "the register stratum's domain" reads a number that is 43% loan
layer. Round 26's finding (3) said the same of its `register_scoped=6`; the
landing added the 8 forms without separating the two populations in the count.

## 2. What the round-27 law landing did and did not change here

| # | round-26 class | state on the landed tree | evidence |
|---|---|---|---|
| 1 | a gloss reads green on a register slot | **unchanged** | C1: argot exit 0, projector `D2L-NATIVE [fail]` |
| 2 | every register value counted as an argot register | **unchanged** | C2: `"craft and law"` replayed and passed; 34 scoped rows over 6 blocks |
| 3 | `register_scoped` measures the loan layer | **worsened by one population** | 14 = 6 loans + 8 `stamp` forms; the law's 5 `RGL-*` rows are scoped too |

And the law landing added a **new** instance of class 2, which is worth naming
because it is the round's own deliverable:

```
register_law RGL-01..RGL-05   register='stamp'
registers    QREG-02..QREG-04 register='stamp'
```

The law rows carry `register: stamp` — correctly, they are law **about** the
register — but the gate's scope predicate reads that field as "this record is a
form in the register", so five law rows and three identity rows are now counted
in the same domain as the eight forms. Measured: the coverage line's
`records` moved `170 → 175` when the law landed (five `RGL-*` rows), while
`register_scoped` stayed at 14 (the law rows are not `is_form_record`, so they
do not add to the scoped count — they add to the **records** count only). That
is the correct outcome, and it is correct by accident of `is_form_record`, not
by the scope predicate knowing the difference.

## 3. Is this a defect of the claim, or a known limit?

Both, and the distinction matters for the round.

**It is a known limit, named.** The round-26 review's `RD-5a` and the round-27
law's own `law_binding.enforcement` state that no gate executes the law rows.
The typing leg's absence is the same family: the argot leg grades the
**arithmetic** of a derivation and has no kind concept.

**It is also a live hole in the round-27 claim's coverage.** The claim's
`after_required` requires "the argot gate + typed gate + assemblers all green
with the amended packet". All three **are** green (measured: argot exit 0
`violations=0`; typed gate `20/20 legs`; `assemble-culture-d4.py --check`
byte-identical). But "green" here means the arithmetic leg passes — it does not
mean the register forms are typed. A later stratum record that is a gloss, or
that carries a medium register, would pass the same way. This is the class
round 26 named and the round-27 claim did not take.

## 4. Named limits of this review

| id | limit | statement |
|---|---|---|
| **D19-L1** | the label-typing table is a **SKILL rule**, and its executable authority is the projector | this file measures the **disagreement** between two delivered gates; it does not adjudicate which is right. The table's own row 1 is the governing text, and it says the gloss is never on the sound channel. |
| **D19-L2** | the controls are **mutations of a NON-CANON packet** | `Q-01`/`Q-02` are probes. No claim about any language, register or label is made or implied. |
| **D19-L3** | the round-26 reviewer's shapes were **rebuilt, not copied** | the round-26 files were read for the class, then re-implemented as full-packet mutations so the finding survives a "degenerate minimal packet" objection. The reproductions are this seat's own runs. |
| **D19-L4** | the leg's typing absence is **reported, not repaired** | the gate is not this reviewer's file. |

## 5. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d19/C1-full-gloss-on-register-slot.yml  # exit 0
python3 -B tools/d2-typed-labels.py --packet .scratch/r27-d19/C1-full-gloss-on-register-slot.yml   # D2L-NATIVE fail
python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d19/C2-full-prose-register.yml        # exit 0
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml                  # register_scoped=14
grep -n "def record_register" -A 20 tools/gates/argot-derivation-gate.py
grep -n "def is_form_record" -A 12 tools/gates/argot-derivation-gate.py
```
