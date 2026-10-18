# R26-D23 — adversarial review 3 of 4: a derivation that over-matches

- **Seat:** R26-D23 (reviewer 3 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a`.
- **Review target:** `tools/gates/argot-derivation-gate.py` sha256
  `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` (840 lines,
  `--selftest` 21/21).
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r26-d21/` (`TMPDIR=$PWD/.scratch` preceded every scratch write). No
  tool, gate, packet, component, pin file, or filed rounds 8–25 byte touched; no
  commit, no push.
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 3 of 4, adversarial: *a derivation that over-matches?*
Where `D21` asked whether a replay that should fail passes, and `D22` whether a
form sits on the wrong channel, this file asks whether the **rule** and the
**scope** are too permissive — whether the leg accepts inputs its own
construction text forbids, or grades records it was not scoped to grade.

**Verdict in one line.** Three over-matches, each measured with a control. (1)
The **operation detector reads prose**: a rule whose `description` contains the
substring `reverse` or `head2` is read as *declaring* that argot operation,
manufacturing a `D4L-ARGOT-COVERAGE` HOLD out of a sentence about something
else — the control ("reordered"/"reversal") is clean. (2) The **borrowed
adaptation replays with no donor-side discipline**: a substitution that rewrites
an unrelated part of the donor reads clean, because the leg applies
`substitutions` as a global `str.replace` chain and never requires the
substituted segments to be donor→recipient correspondences. (3) The **`formation`
leg is scoped wider than the claim**: it grades every form record, register-scoped
or not. A fourth, recorded as inherited rather than introduced: the packet's own
`CX-02`/`CX-03` patterns (`^(?P<stem>.+)$`) accept **any** stem, so the leg cannot
fail a suffix-class derivation whose form the writer chose to match.

## 1. Attack B1 — the operation detector reads prose (measured PASS, should FAIL)

`packet_declares_ops` (`:379-405`) scans a rule's `id`, `name`, `kind`, `note`
and `description` text for the substrings `head2` and `reverse`, and treats a hit
as a declaration of the operation. Prose about reversal is therefore read as a
declaration:

```
# .scratch/r26-d21/fix/B1-prose-reversed.yml — a rule whose description is
# "the order is not reversed here", one register-scoped form, NO derived pair
$ python3 tools/gates/argot-derivation-gate.py … B1-prose-reversed.yml
FINDING D4L-ARGOT-COVERAGE: HOLD — packet declares the argot operation(s) reverse and 1 register-scoped form(s), but no record carries a derived_from/derivation pair; the forecast derivation relation is declared, not delivered
exit 1
```

The packet declares **no** argot operation; the word "reversed" in an unrelated
rule's description is the entire trigger. The control — the same fixture with the
word changed to a synonym the scanner does not carry — is clean:

| fixture | description text | exit | finding |
|---|---|---:|---|
| `.scratch/r26-d21/fix/B1-prose-reversed.yml` | "the order is not **reversed** here" | **1** | `D4L-ARGOT-COVERAGE` |
| `.scratch/r26-d21/fix/B1b-prose-reordered-ctl.yml` | "the order is not reordered here" | 0 | none |
| `.scratch/r26-d21/fix/B2-prose-head2.yml` | "a **head2** style prefix" | **1** | `D4L-ARGOT-COVERAGE` |
| `.scratch/r26-d21/fix/B2b-prose-headtwo-ctl.yml` | "a head-two style prefix" | 0 | none |
| `.scratch/r26-d21/fix/B3-prose-reverse-word.yml` | "the **reverse** order is not licensed" | **1** | `D4L-ARGOT-COVERAGE` |
| `.scratch/r26-d21/fix/B3b-prose-reversal-ctl.yml` | "the **reversal** of order is not licensed" | 0 | none |

(Commands: `python3 .scratch/r26-d21/probeB.py`, 2026-10-18.)

The asymmetry is the defect: "reverse" fires, "reversal" does not; "head2" fires,
"head-two" does not. A detector whose verdict turns on English morphology is a
false-positive generator, and its one live output — `D4L-ARGOT-COVERAGE`, a HOLD
that reads as design debt — would be **manufactured** from a sentence. The
module docstring already concedes the *false-negative* side ("A family that
declares its argot operations only in prose elsewhere is not detected"); the
measured *false-positive* side is the one that manufactures findings.

**Mitigating measurement (recorded so the finding is not overstated).** The
delivered D4 rules do **not** trip it: `grep -c "reverse\|head2"
examples/culture-d4/components/04-lexicon.yml` → **0**, so on the delivered tree
the coverage HOLD does not fire for this reason (it does not fire at all —
`derived_pairs=0` but also no declared op). The finding is about the detector's
discipline, not about a live false red.

**Fix shape.** The operation declaration must be a typed field (the top-level or
`morphology.derivation_ops` list the gate already reads, `:391-396`), never a
substring of prose. If prose must be scanned, it must be word-bounded and
anchored to a declaration-shaped field, and a hit must not by itself author a
finding.

## 2. Attack B2 — the borrowed adaptation has no donor-side discipline (measured PASS, should FAIL)

`replay_borrow` (`:444-467`) sorts the layer's `substitutions` by key length and
applies them as a global `expected.replace(donor_part, recipient_part)` chain to
the record's `donor_form`, then compares to the form. There is no requirement
that a substituted segment be a **donor-side** correspondence, that the donor be
separated into the three declared fields, or that the result be inventory-legal:

```
# .scratch/r26-d21/fix/E3-borrow-oversub.yml — the substitution rewrites the
# nucleus of the donor, unrelated to any correspondence the layer names
layers:
  - {id: LY-01, name: L, register: trade, substitutions: {a: e}}
lexicon:
  - {id: L-01, term: kher, route: borrowed, layer: LY-01, donor_form: khar}
$ python3 tools/gates/argot-derivation-gate.py … E3-borrow-oversub.yml
coverage: … borrow_pairs=1 … violations=0     exit 0
```

`khar` with `{a: e}` gives `kher` — the leg counts a clean adaptation. The
label-typing table's borrowed-strata row (`SKILL.md:45`) requires far more:
"layer resolves, **donor separated**, substitutions reproduce the form, **clocks
ordered, domain/register declared**". The leg checks the first and the third and
none of the others; the discriminating control is that a substitution which
*does* change the form in a way the declared map cannot reach still fails:

```
# .scratch/r26-d21/fix/E3b-borrow-global.yml — substitutions {sh: s}, donor sashsh, form sash
FINDING D4L-ARGOT-DERIV: FAIL — … layer 'LY-01' substitutions applied to donor form 'sashsh' yield 'sass'; …
exit 1
```

So the leg is live; it simply has no rule that the substitution set is a
declared correspondence rather than an arbitrary rewrite. Under the current leg a
writer can make any form "replay" by choosing a one-letter substitution.

## 3. Attack B3 — the `formation` leg is scoped wider than the claim (measured, named not failed)

The claim scopes the leg to **register-scoped** forms. The `formation` block
(`:535-566`) is graded for **every** form record that claims it, scoped or not —
the code comment states this is deliberate ("It is graded for every form record
that claims it — scoped or not … a packet that declares its rules and then loses
them must not read clean"). On the delivered tree that is the eight names
`NM-01..NM-08`, all `rule: CX-01`, none register-scoped — hence
`claimed_chains=8` beside `register_scoped=6`.

This is a **named scope widening, not a defect**: it is the discipline the
round-17 Δ3 lesson asks for, and it is documented. It is recorded here so the
`register_scoped`/`claimed_chains` pair is not read as "8 register chains". The
counter is not the claim's domain.

## 4. Attack B4 — inherited over-match: the packet's own suffix patterns accept any stem

The delivered `CX-02`/`CX-03` rules are `pattern: "^(?P<stem>.+)$"`,
`output: "{stem}ar"` / `"{stem}en"` (`04-lexicon.yml:192-195`). `.+` is the whole
input alphabet, so for **any** candidate ending in `-ar`/`-en` there is a stem the
pattern accepts and the output reproduces. The leg inherits this and grades it
for register-scoped records, so an out-of-inventory register form whose writer
picked a matching stem replays clean:

```
# .scratch/r26-d21/fix/E1a-digit-stem.yml
    - {id: CX-02, kind: suffix, pattern: "^(?P<stem>.+)$", output: "{stem}ar"}
  - {id: Q-01, term: ZZ9ar, register: quote, derived_from: ZZ9, derivation: CX-02}
$ python3 tools/gates/argot-derivation-gate.py … E1a-digit-stem.yml
coverage: … derived_pairs=1 … violations=0     exit 0
```

A digit-bearing register form replays clean. This is the same class `D21` §4
measures (no inventory leg); here the *rule* is the over-permissive half. It is
**inherited from the packet's own rules, not introduced by the leg** — but the
leg is the gate that would have to catch it, and it does not.

A related inherited shape: a rule whose `output` references **no** match group
(`output: "fixed"`) passes `_template_problem` (`python3 -c
"…_template_problem('fixed', {})"` → `None`) and replays any base to the
constant:

```
# .scratch/r26-d21/fix/E4-template-noop.yml
    - {id: CX-99, kind: suffix, pattern: "^(?P<stem>.+)$", output: "fixed"}
  - {id: Q-01, term: fixed, register: quote, derived_from: anything, derivation: CX-99}
$ python3 tools/gates/argot-derivation-gate.py … E4-template-noop.yml
coverage: … derived_pairs=1 … violations=0     exit 0
```

## 5. What the leg gets right (recorded so it is not lost)

- The `_catastrophic_pattern` and `_match_with_budget` guards are inherited and
  live (`replay_rule`, `:424-431`), so a hostile rule cannot hang the leg.
- The `D4L-ARGOT-RULE` HOLD class correctly catches an unlicensed operation
  (`derivation: NOPE`) and an unreplayable rule pair, which is the right
  disposition for "cannot evaluate".
- The delivered packet's own prose does not trip the prose detector (§1,
  mitigating measurement), so the finding is about discipline, not a live red.

## 6. Controls carried by this fragment

Every attack carries a same-shape control: §1's six-row synonym table, §2's
`E3b` discrimination control, §4's sibling inventory measurement in `D21`. The
receipt is `.scratch/r26-d21/attacks.json`; fixtures under
`.scratch/r26-d21/fix/`. None was written to the delivered tree.

## 7. Counting commands for this file

```
export TMPDIR=$PWD/.scratch
python3 .scratch/r26-d21/probeB.py
python3 .scratch/r26-d21/probeE.py
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/fix/E3-borrow-oversub.yml
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/fix/E4-template-noop.yml
grep -c "reverse\|head2" examples/culture-d4/components/04-lexicon.yml
python3 -c "import runpy; n=runpy.run_path('tools/gates/naming-collision-gate.py'); print(n['_template_problem']('fixed', {}))"
```
