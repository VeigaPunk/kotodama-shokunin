# R26-D22 — adversarial review 2 of 4: a register form on the wrong channel

- **Seat:** R26-D22 (reviewer 2 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a`.
- **Review target:** `tools/gates/argot-derivation-gate.py` sha256
  `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` (840 lines,
  `--selftest` 21/21), and its **cross-check against the label-typing table**
  (`SKILL.md:31-84`), whose executable authority is `tools/d2-typed-labels.py`.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r26-d21/` (`TMPDIR=$PWD/.scratch` preceded every scratch write). No
  tool, gate, packet, component, pin file, or filed rounds 8–25 byte touched; no
  commit, no push.
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 2 of 4, adversarial: *a register form smuggled onto the
wrong channel?* This file asks whether the register-stratum leg lets a form sit
on a channel it is not entitled to — a gloss on a sound channel, a prose
register counted as an argot register, or a register value treated as an
exemption. The label-typing table (`SKILL.md:31-84`) is the rule it is checked
against.

**Verdict in one line.** The leg has **no concept of a label kind at all** — it
reads `register` as a free-text string and never asks whether the form is a
native form, a translated label, or a borrowed stratum. Three consequences,
each measured with a control: (1) a reader-facing English gloss on a
register-scoped slot reads **green** where the label-typing table's row 1 and
`tools/d2-typed-labels.py` both refuse it; (2) **every** register value is
treated as an argot register — `sacred`, `taboo`, `"craft and law"` all count;
(3) the delivered `register_scoped=6` is the six **loan-layer** loans, so the
leg's own headline count measures the label table's *borrowed-strata* row, not
the forecast's quote register. The table's T4 caution — "a register label is not
a channel" — is the exact rule the first two findings violate.

## 1. Attack B1 — a gloss on a register-scoped slot reads green (measured PASS, should FAIL)

The label-typing table's first row (`SKILL.md:41`): a reader-facing gloss is
`translated-label`, "**never** — not on the sound or identity channel". The leg
grades a register-scoped form by its derivation arithmetic alone:

```
# .scratch/r26-d21/fix/C1-gloss-on-register-slot.yml
name: C1
lexicon:
  - {id: Q-01, term: "wool coat", register: quote}
$ python3 tools/gates/argot-derivation-gate.py … C1-gloss-on-register-slot.yml
coverage: … records=1 register_scoped=1 derived_pairs=0 claimed_chains=0 borrow_pairs=0 violations=0 rule_holds=0
exit 0
```

A whitespace-bearing English gloss is counted as a register-scoped form and
produces **no finding**. The same record, when its gloss happens to be
`reverse`-consistent with its base, replays "clean" too:

```
# .scratch/r26-d21/fix/D1-gloss-derived.yml
  - {id: Q-01, term: "taoc loow", register: quote, derived_from: "wool coat", derivation: reverse}
$ python3 tools/gates/argot-derivation-gate.py … D1-gloss-derived.yml
coverage: … derived_pairs=1 … violations=0     exit 0
```

`reverse("wool coat")` is `taoc loow` (`python3 -c "print(repr('wool coat'[::-1]))"`
→ `'taoc loow'`), so the leg reports a clean replayed pair **over an English
gloss**. That is a register form smuggled onto the sound-and-identity channel
and graded as if it belonged there — the label table's row-1 wrong-typing
consequence, "grading a gloss against native phonotactics manufactures
representation artifacts", at a new address.

**Control — the executable label-typing authority refuses the same record.** A
copy of the delivered D4 packet with one register-scoped gloss record injected
(`.scratch/r26-d21/cross/injected.yml`, `{id: L-99, term: "wool coat", register:
quote, …}`):

```
$ python3 tools/d2-typed-labels.py --packet .scratch/r26-d21/cross/injected.yml | grep L-99
FINDING D2L-NATIVE: [fail] L-99 — supplied form 'wool coat' carries symbols outside the declared inventory: ['c']
FINDING D2L-BORROW: [fail] L-99 — layer_ref 'null' does not resolve to a declared layer
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/cross/injected.yml | tail -2
coverage: … records=157 register_scoped=7 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit 0
```

Same bytes, two gates: the projector **fails** the gloss (`D2L-NATIVE`, the
inventory leg), the argot leg **passes** it and simply adds it to
`register_scoped`. The label-typing table is the governing rule, and the argot
leg does not implement it.

**Fix shape.** The register-scoped scope predicate must consult a label kind
before grading a derivation: a form whose signature is a gloss (whitespace,
gloss punctuation, out-of-inventory segment) is `translated-label` and belongs
off the checked channel — it is a `D4L-ARGOT-RULE` HOLD at best, never a
replayed pair. The label table already states the signature (`SKILL.md:47`,
T1: "a label signature (whitespace, gloss punctuation, out-of-inventory
segment, declared gloss provenance) is sufficient to route off the sound
channel").

## 2. Attack B2 — every register value is an argot register (measured PASS, should FAIL)

**Timing note (added at 18:08Z, after the D-design seats filed).** The D-design
seats have since fixed the register vocabulary this finding is about:
`reports/round-26/register/rules.md` §1 names `stamp` as "the single marked
value this stratum introduces" and **adopts `UNMARKED_REGISTERS` unchanged**.
That is the right shape and it answers the *design* half of this finding. It does
not yet answer the *gate* half: `tools/gates/argot-derivation-gate.py` still
reads any non-plain string as a register (`record_register`, `:293-317`), so
until the gate's predicate is narrowed to the design's vocabulary, the
measurement below stands as the gap between design and checker. Re-run §2's
fixture after the stratum lands.

The leg's `record_register` (`:293-317`) excludes only `UNMARKED_REGISTERS =
("plain", "neutral", "standard", "ordinary")`; every other string is a register.
Measured:

```
# .scratch/r26-d21/fix/C3-register-vocabulary-conflation.yml
name: C3
lexicon:
  - {id: A-01, term: kal, register: sacred}
  - {id: A-02, term: nir, register: taboo}
  - {id: A-03, term: mun, register: ritual}
  - {id: A-04, term: som, register: "craft and law"}
  - {id: A-05, term: wek, register: quote}
  - {id: A-06, term: tup, register: trade}
$ python3 tools/gates/argot-derivation-gate.py … C3-register-vocabulary-conflation.yml
coverage: … records=6 register_scoped=6 derived_pairs=0 claimed_chains=0 borrow_pairs=0 violations=0 rule_holds=0
exit 0
```

Six of six are counted as register-scoped, including `"craft and law"` — a
string the delivered D4 packet uses for **symbols**, not for forms
(`07-symbolism.yml:28-35`). The forecast's argot register is specifically the
**quote** register (`design-language.md` §7.3: "used only inside the quote
register and never written on the rod"), a register-scoped *slot* the design
gives a pair `<id>#plain`/`<id>#quote`. Conflating `sacred`, `taboo`, `ritual`,
`trade` and prose strings with it means a `register_scoped` count can never be
read as "the argot's domain size".

**This is not merely a wording issue — it is the reason the delivered
`register_scoped=6` is a misreading.** The six records are the loans
`L-49..L-54`, scoped only through their layer's register
(`04-lexicon.yml:103` `register: trade`, `:117` `register: craft`):

```
$ python3 .scratch/r26-d21/probe3.py    # enumerates the gate's own register_scoped set
  lexicon/L-49 term='sal' register='trade' route='borrowed' layer='Salt-road trade layer'
  lexicon/L-50 term='kar' register='trade' route='borrowed' layer='Salt-road trade layer'
  lexicon/L-51 term='gul' register='trade' route='borrowed' layer='Salt-road trade layer'
  lexicon/L-52 term='res' register='trade' route='borrowed' layer='Salt-road trade layer'
  lexicon/L-53 term='gal' register='craft' route='borrowed' layer='North-road kin layer'
  lexicon/L-54 term='mar' register='craft' route='borrowed' layer='North-road kin layer'
```

Every one is `route: borrowed` with a declared `layer` and a `donor_form`. Under
the label-typing table these are the **borrowed-strata** row (`SKILL.md:45`),
whose checked channel is "the recipient-adapted form against the recipient
inventory, plus borrow-ledger checks" — not the argot's quote register. So the
leg's `register_scoped` counter is measuring the label table's loan row and
calling it the argot domain. The two are different rows of the same table, and
the leg merges them.

**Fix shape.** `register_scoped` must be defined by the design's own register
vocabulary (the quote register and its declared siblings), not by "any
non-plain string". A borrowed record whose layer carries `register: trade` is a
borrowed-strata record; if it is also argot-scoped, that must be declared, not
inferred from the layer's trade register.

## 3. Attack B3 — prose registers on non-form records are correctly skipped, and that is the one place the leg is right

For symmetry, the leg does **not** manufacture findings from prose `form:`/`name:`
records (`record_register` returns `None` for a `symbols` record whose `form:` is
prose, because `is_form_record` refuses it):

```
# .scratch/r26-d21/fix/C2-prose-register.yml
symbols:
  - {id: SYM-01, form: "a woven mark", register: "craft and law"}
$ python3 tools/gates/argot-derivation-gate.py … C2-prose-register.yml
coverage: … register_scoped=0 …
exit 0
```

This is correct and is recorded so the review is not read as a blanket
indictment: the leg avoids the false-positive class the O claim repairs
(`reports/round-25/argot/impl-2.md` §1.1). The finding in §2 is that the *same*
prose register, when it sits on a **lexicon** record instead of a `symbols`
record, is counted — so the discrimination is by block, not by the register
vocabulary the design fixes.

## 4. What the cross-check establishes

| label-typing table rule (`SKILL.md`) | argot leg behaviour | verdict |
|---|---|---|
| Row 1 — a gloss is never on the sound/identity channel (`:41`) | a gloss on a register slot replays clean (§1) | **violated** |
| T1 — a label signature routes off the sound channel (`:47`) | no inventory/gloss signature is read (`grep -n "inventory\|scheme\|gloss" tools/gates/argot-derivation-gate.py` → 0) | **not implemented** |
| T4 — a register field is not a channel; a register-scoped slot never licenses moving a form (`:176-180`) | register is read as a free-text string; every non-plain value is an argot register (§2) | **violated** |
| Borrowed-strata row — a loan's checked channel is the recipient inventory + ledger (`:45`) | the six loans are counted as `register_scoped` via their layer's register (§2) | **conflated** |
| The untyped-legacy caution — "adding typing fields cannot exempt a string" (`:47`) | the leg adds `register_scoped` for any register string without a kind (§1-§2) | **at risk** |

## 5. Controls carried by this fragment

- §1: the projector control on the same bytes (`D2L-NATIVE` FAIL vs the leg's
  exit 0) is the decisive one.
- §2: the `probe3.py` enumeration shows the six records are loans, so the
  conflation is measured, not inferred.
- §3: the `symbols`-prose control shows the leg is not indiscriminate, which
  scopes the finding to the register-vocabulary definition.

Receipt: `.scratch/r26-d21/attacks.json`; fixtures `.scratch/r26-d21/fix/`,
`.scratch/r26-d21/cross/`.

## 6. Counting commands for this file

```
export TMPDIR=$PWD/.scratch
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/fix/C1-gloss-on-register-slot.yml
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/fix/D1-gloss-derived.yml
python3 tools/d2-typed-labels.py --packet .scratch/r26-d21/cross/injected.yml | grep L-99
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/fix/C3-register-vocabulary-conflation.yml
python3 .scratch/r26-d21/probe3.py
grep -n "inventory\|scheme\|gloss" tools/gates/argot-derivation-gate.py
```
