# R26-D21 — adversarial review 1 of 4: a replay that should fail, passing

- **Seat:** R26-D21 (reviewer 1 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (round-25 admit); worktree HEAD at measurement `1ad491a`
  (`git log --oneline -1` → `1ad491a round-26: declare claims D/O/C …`).
- **Review target:** `tools/gates/argot-derivation-gate.py`, sha256
  `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211`, 840 lines,
  `--selftest` **21/21** (measured below). This is the artifact the round-25
  admit committed (`git show fc13cd2:tools/gates/argot-derivation-gate.py |
  sha256sum` → the same digest, 840 lines) — **not** the `07db6e9b…`/748-line
  bytes the round-25 review files (`reports/round-25/argot/review-1.md:6A`)
  quote. The gate moved between the r25 review and the r25 admit; §0 measures
  that and re-verifies the r25 review's three findings against the committed
  bytes.
- **Write scope:** this file, plus gitignored scratch under `.scratch/r26-d21/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write). No tool, gate,
  fixture, packet, component, pin file, or filed rounds 8–25 byte was written;
  no commit, no push.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script, or argot is described, cited, or approximated.

**Assignment.** Reviewer 1 of 4, adversarial: *a replay that should fail
passing?* The target is the register-stratum leg as it stands at the round-26
baseline. The **register stratum has not landed** at this seat's measurement
(§0.2): the claim's own artifact — components declaring register-scoped forms
with machine-readable derivation rules — does not exist on disk yet, and
`grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/` → 0 files. So this review
attacks the *checking* surface that the stratum will be graded by, which is the
whole of what can be attacked today.

**Verdict in one line.** The leg's positive result is real and reproduces
(`violations=0` on the delivered D4), and it inherits the naming gate's four
guards — but **three classes of a replay that should fail pass green**, and two
of them are the *same* classes the round-25 review measured (`review-1.md`
6A.1–6A.3), still open on the committed bytes: a dangling base reads clean, a
self-derivation reads clean, and deleting one field launders a violation. A
fourth, new here, is that **no inventory check exists**: an out-of-inventory
form replays clean while every sibling gate refuses it.

## 0. Baseline, artifact identity, and the register stratum's state

### 0.1 The gate the round-26 baseline carries

```
$ export TMPDIR=$PWD/.scratch
$ sha256sum tools/gates/argot-derivation-gate.py
5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211  tools/gates/argot-derivation-gate.py
$ git show fc13cd2:tools/gates/argot-derivation-gate.py | sha256sum
5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211  -
$ wc -l tools/gates/argot-derivation-gate.py
840 tools/gates/argot-derivation-gate.py
$ python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
selftest: 21/21 checks passed
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

(2026-10-18, lane root, `TMPDIR=$PWD/.scratch`.)

The three r25 review files (`reports/round-25/argot/review-1.md:6`,
`review-2.md:6`, `review-3.md:6`; `grep -l "07db6e9b"
reports/round-25/argot/*.md`) quote `07db6e9b…`, 748 lines, `--selftest` 18/18.
The **committed** gate is `5b5abe78…`, 840 lines, 21/21, as `impl-6.md` §1
already records (`grep -l "5b5abe78" reports/round-25/argot/*.md` →
`impl-6.md`). So the r25 review's findings are about superseded bytes unless
re-measured; §1–§3 below re-measure all three against `5b5abe78…` and they
**all still reproduce**.

### 0.2 The register stratum is not on disk

```
$ grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/ | wc -l
0
$ grep -c "derived_from\|derived_forms\|derived_ok\|doublet_of" examples/culture-d4/packet.d4.yml
0
$ grep -c "register:" examples/culture-d4/components/*.yml | grep -v ":0"
examples/culture-d4/components/03-orthography.yml:1      # `numeral_register`, not a form's register
examples/culture-d4/components/04-lexicon.yml:2          # the two layer rows LY-01/LY-02
examples/culture-d4/components/07-symbolism.yml:8        # prose registers on symbols records
examples/culture-d4/components/11-contact-history.yml:2  # the same two layers restated
```

(2026-10-18, lane root.) No `register:` sits on a **lexicon form record**: the
two in `04-lexicon.yml` are the layer rows (`:103` `trade`, `:117` `craft`), and
the eight in `07-symbolism.yml` are prose registers on symbols. The D4 packet's
54 lexicon records carry no `register` field, no `derived_from`, no
`derivation`. The `register_scoped=6` the gate reports are the six **loans**
`L-49..L-54`, scoped only because their *layer* carries a `register`
(`04-lexicon.yml:103,117`); §D22 measures that conflation. So claim D's
`after_required` — "components declare register-scoped forms with
machine-readable derivation rules" — is **not yet met** at this seat's sample,
and the delta is named in `D24-forecast-closure.md`, not silently absorbed.

## 1. Attack A1 — a dangling base reads clean (measured PASS, should FAIL)

The forecast's F-4 (`reports/round-17/d4/design-brief.md:304`) fixes the
relation as one "between **two records of the same packet**". The gate never
resolves `derived_from` to a record; it compares `apply(op, base_string)`
against the form.

```
# fixture .scratch/r26-d21/fix/A1-dangling-base.yml
name: A1
lexicon:
  - {id: Q-01, term: nim, register: quote, derived_from: min, derivation: reverse}
```
```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/fix/A1-dangling-base.yml
coverage: .scratch/r26-d21/fix/A1-dangling-base.yml records=1 register_scoped=1 derived_pairs=1 claimed_chains=0 borrow_pairs=0 violations=0 rule_holds=0
exit 0
```

There is **no record `min`** in the fixture, yet the leg counts a `derived_pair`
and reports zero violations. The control — the same derivation with the base
*also* present as a record — reads identically:

```
# .scratch/r26-d21/fix/A1b-linked-base-control.yml — adds {id: B-01, term: min}
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/fix/A1b-linked-base-control.yml
coverage: … records=2 register_scoped=1 derived_pairs=1 … violations=0
exit 0
```

The two are indistinguishable to the leg, which is the defect: "derived from the
lexeme the language has" and "derived from a string the writer typed" are the
same input. A `derived_from` naming a **nonexistent** record is a defective
derivation, not a clean one. The D3 precedent resolves each base against the
lexicon index (`tools/check-evidence-coupling.py:879-882`, `any(b not in lex
for b in bases)`), so the discipline is already in the lane and was not carried
over.

**Fix shape.** A `derived_from` that resolves to no record in the packet is
`D4L-ARGOT-RULE` (HOLD — the chain is not replayable because its input is not a
record), or a FAIL if the design holds base identity to be part of Δ3's claim.
Either way it must not be a silent `derived_pairs` increment.

## 2. Attack A2 — a self-derivation is accepted as correct (measured PASS, should FAIL)

A record whose form equals its own base passes whenever the operation is an
identity on that string.

```
# .scratch/r26-d21/fix/A2-self-derivation-palindrome.yml
  - {id: Q-01, term: naman, register: quote, derived_from: naman, derivation: reverse}
$ python3 tools/gates/argot-derivation-gate.py … A2-self-derivation-palindrome.yml
coverage: … derived_pairs=1 … violations=0     exit 0

# .scratch/r26-d21/fix/A2b-self-derivation-head2.yml
  - {id: Q-01, term: kin, register: quote, derived_from: kin, derivation: head2}
$ python3 tools/gates/argot-derivation-gate.py … A2b-self-derivation-head2.yml
coverage: … derived_pairs=1 … violations=0     exit 0
```

`reverse("naman") == "naman"` and `head2("kin") == "kin"` (one syllable), so
`apply(op, base) == form` holds trivially. The control proves the leg is
otherwise discriminating:

```
# .scratch/r26-d21/fix/A2c-control-bad-pair.yml — {term: suk, derived_from: sun, derivation: reverse}
$ python3 tools/gates/argot-derivation-gate.py … A2c-control-bad-pair.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-01 'suk' (register 'quote'): declared chain 'reverse' applied to 'sun' yields 'nus'; …
exit 1
```

So this is not "the gate is asleep": it is that a record declaring **itself** its
own derivation is not a derivation, and no check exists for it. The D3 precedent
has exactly this check (`check-evidence-coupling.py:904-908`: "name equals its
base lexeme" → `D3-DERIVATION`).

## 3. Attack A3 — a violation is laundered by deleting one field (measured PASS, should FAIL)

The gate's scope predicate is "declares `derived_from` **and** `derivation` (or a
register)". Deleting one field of a failing record removes it from the replay:

| fixture | record | exit | findings | `derived_pairs` |
|---|---|---:|---|---:|
| `.scratch/r26-d21/fix/A3-launder-keep-pair.yml` | `{term: suk, register: quote, derived_from: sun, derivation: reverse}` | **1** | `D4L-ARGOT-DERIV` ×1 | 1 |
| `.scratch/r26-d21/fix/A3b-launder-drop-derivation.yml` | same, `derivation` deleted | **0** | none | 0 |
| `.scratch/r26-d21/fix/A3c-launder-drop-both.yml` | same, both deleted | **0** | none | 0 |
| `.scratch/r26-d21/fix/A3-drop-register-control.yml` | same, `register` deleted (pair kept) | **1** | `D4L-ARGOT-DERIV` ×1 | 1 |

(Commands: `python3 tools/gates/argot-derivation-gate.py <fixture>`, 2026-10-18.)

The record is still in the packet, still wrong, and now **ungraded**. Dropping
the register is caught (the fourth row), which isolates the laundering channel to
the pair fields. This is the "laundered hold" class the SKILL names
(`SKILL.md:149`: "adding typing fields cannot exempt a string"; T2 "a `return
True` branch for non-default input is a laundering channel") reached by a
different route: not a skip branch but a **scope predicate a writer can leave**.

**Fix shape.** A register-scoped record that declares **exactly one** of
`derived_from`/`derivation` is a malformed pair → `D4L-ARGOT-RULE` HOLD. The gate
already has that id and uses it for the unlicensed-operation case.

## 4. Attack A4 — no inventory check (measured PASS, should FAIL)

A register form carrying a segment outside the declared inventory replays clean:

```
# .scratch/r26-d21/fix/C4-out-of-inventory.yml
name: C4
phonology: {consonants: [p, t, k, m, n, s, r, l], vowels: [a, e, i, o, u]}
lexicon:
  - {id: Q-01, term: xxq, register: quote, derived_from: qxx, derivation: reverse}
$ python3 tools/gates/argot-derivation-gate.py … C4-out-of-inventory.yml
coverage: … register_scoped=1 derived_pairs=1 … violations=0     exit 0
```

The forecast's **required control C-02's sibling C-01** (`design-brief.md:456`)
is explicit: "quote form given a private segment (a segment outside 02's
inventory) → FAIL `D4L-NATIVE`-class; **a register never licenses an inventory**".
The label-typing table says the same in its own words (`SKILL.md:47`, T1: a
label signature "is sufficient to route off the sound channel"). The argot gate
has no inventory leg, so an out-of-inventory register form is a green row here.

Cross-check, same fixture, the sibling gates that *do* check inventory:

| gate | command | exit |
|---|---|---:|
| argot-derivation-gate | `… C4-out-of-inventory.yml` | **0** |
| naming-collision-gate | `… C4-out-of-inventory.yml` | 1 (`PHON-PROFILE` HOLD — needs a full phonology) |
| lexicon-coverage-audit | `… C4-out-of-inventory.yml` | 1 (`C-entry-unevaluable`) |
| phonology-sanity-gate | `… C4-out-of-inventory.yml` | 1 (`P-PATTERN` REVIEW — phonotactics missing) |

The three siblings exit 1 for *other* missing evidence, so this row is not by
itself proof that a *properly-phonologised* packet would catch `xxq` — but it
is proof that the **argot leg is the only one that reads the form at all** and
it reads it as clean. The load-bearing measurement is the delivered-tree one
(§0.1: `violations=0` with no inventory leg in the gate's `--help`-level
vocabulary; `grep -n "inventory\|scheme" tools/gates/argot-derivation-gate.py`
→ **0 hits**).

**Fix shape.** The register form must pass the packet's own inventory before its
derivation is graded, exactly as the label-typing table's native-form row
requires; a private segment is a FAIL (`D4L-NATIVE`-class) *before* the
derivation arithmetic is reached.

## 5. What the leg gets right (recorded so it is not lost)

- The positive replay is real: `records=156 register_scoped=6 derived_pairs=0
  claimed_chains=8 borrow_pairs=6 violations=0`, exit 0, reproduced above.
- It inherits the naming gate's four guards by path — `_match_with_budget`,
  `_catastrophic_pattern`, `_template_problem`, `_MatchBudgetExceeded` — and
  prints the dependency digest on every run (`dependency: … sha256 d9e4e8f4…`),
  so a replay names the bytes it used.
- `D4L-ARGOT-COVERAGE` is real and fires when ops are declared but no pair
  exists; the selftest asserts the exact id list (`coverage-hold-fires`).
- Every finding names the record id, form, register, rule, input, computed value
  and delivered value — the four `D4L-ARGOT-DERIV` + one `D4L-ARGOT-RULE` fixture
  set reproduces exactly (`fixture-counts-pinned`).
- The `head2` maximal-onset trap (`saalum` vs `saalu`) is the fixture's own
  planted violation (`fixture-names-the-violating-form`), so the design's named
  ambiguity is tested.

## 6. Controls carried by this fragment

Every attack above carries a same-shape control that reads the other way:
A1 ↔ A1b (linked base), A2 ↔ A2c (bad pair), A3 ↔ A3-drop-register, A4 ↔ the
sibling-gate comparison. The receipt with all cases is
`.scratch/r26-d21/attacks.json` (scratch, not promoted); the fixtures are under
`.scratch/r26-d21/fix/`. None was written to the delivered tree.

## 7. Counting commands for this file

```
export TMPDIR=$PWD/.scratch
sha256sum tools/gates/argot-derivation-gate.py
git show fc13cd2:tools/gates/argot-derivation-gate.py | sha256sum
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | tail -2
python3 .scratch/r26-d21/attacks.py
grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/ | wc -l
```
