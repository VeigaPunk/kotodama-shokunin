# R25-D17 — adversarial review 3: cross-check against the D2/D3 derivation lessons

- **Seat:** R25-D17 (reviewer 3 of 3), round 25, loop 3 build 1 of 4, claim **D**
  `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  worktree HEAD at measurement `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only. Scratch under `.scratch/r25-d15/`
  (`TMPDIR=$PWD/.scratch`). No tool, gate, packet, component, or rounds 8–24
  byte touched; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 3 of 3: *cross-check vs D2/D3 lessons.* The round-25 D
claim must satisfy the round-19 lesson ("a derivation is replayable only if the
operation and its input are both machine-readable") and the D3 precedent
(`D3-DERIVATION`). This file tests the delivered leg against **four lessons the
lane already paid for** — two from D2, two from D3 — and reports where the leg
inherits the discipline and where it does not.

**Target note.** A delivered gate, `tools/gates/argot-derivation-gate.py`
(sha256 `07db6e9b…`, `--selftest` 18/18), landed during this review. It is a
much stronger artifact than the scratch harness and **does** inherit the D2
lessons fully (L-1, L-2 below) — but it reproduces two of the three D3 gaps
(L-3, L-4) measured in §3 and §4, and it adds a laundering channel (§3.1). The
cross-check therefore now covers both engines, and the delivered gate's verdicts
are the ones that matter.

**Verdict in one line.** The leg satisfies the D2 lessons it was written against
(machine-readable pairs; unreplayable ⇒ HOLD) and the D3 lesson's *first half*
(recompute, don't hand-approve), but it fails the D3 lesson's *second half* —
D3 resolves each base to a lexeme record and rejects a name that equals its own
base; the D4 leg trusts the record's own base list. The four lessons and their
verdicts are the deliverable.

## 1. Lesson L-1 (D2) — a derivation is replayable only if the operation and its input are both machine-readable

**Source.** `reports/round-19/integration/d4-lessons-entry.md:85-92`; forecast
`reports/round-17/d4/design-brief.md:296-310`.

**Test.** Does the leg read a machine-readable operation + input pair, or a
prose rule?

**Verdict: INHERITED (for the concatenation class).** The leg reads
`morphology.derivation_rules[].pattern` / `.output` (`packet.d4.yml:205-226`),
and each record states its inputs in typed fields (`formation.stem`,
`bases`). Prose is not consulted. Measured: 12/12 rows replay, 0 violations
(`review-1.md` V-0).

**Limit found.** The *operation* itself is not machine-readable as an
operation — it is encoded as a regex `pattern`/`output` pair, which can express
concatenation and suffixation but **not** `head2` or `reverse`. That is why
`reports/round-25/argot/delta.md` §3 measures a correct `reverse` derivation as
a `D-form-mismatch` FAIL and a non-derivation as a pass. So L-1 is inherited
*for the class the packet's encoding can represent*, and the encoding is the
reason the Δ3 operations remain undeliverable. This is a **scoping of the
lesson**, not a violation of it.

## 2. Lesson L-2 (D2) — an unreplayable derivation is a HOLD, never a pass

**Source.** Same lesson; the gate's `DERIV-HOLD` class.

**Test.** Four unreplayable shapes: no formation record, no stem, no rule table,
unknown rule id.

**Verdict: INHERITED, with one gap.** Measured against the delivered gate
(`adv.py` A2b, A5, A6, A10c):

| shape | gate verdict |
|---|---|
| name claims etymology, declares no formation | `DERIV-HOLD` |
| formation with no stem | `DERIV-HOLD` |
| packet declares no `derivation_rules` | `DERIV-HOLD` |
| unknown rule id | `DERIV-AFFIX` FAIL |
| catastrophic pattern | `DERIV-HOLD` ×8, 0.03 s |
| output template outside the subset | `DERIV-HOLD` |

**The gap: an underived quote form is invisible, not held.** `_gate_c` reads
only `names[]` (`naming-collision-gate.py:1356`), and `_collect_records`
(`:1152`) walks `names`, `pantheon`, `symbols`, `costumes` — **not** `lexicon`,
**not** any register block. Measured: a `doublets`-style register block appended
to the packet produces **0** additional findings, while the same bad form placed
in `names` produces `PHON-INVENTORY 6→7`. So a register-scoped form is outside
the gate's universe: the leg cannot hold what it cannot see.

**Cross-check to D2.** D2's own lesson set records the same class as "a skipped
leg is not an implementation" (`SKILL.md` T2, `reports/round-18/gate/design.md`
§1.3): a `return True` branch for non-default input is a laundering channel. The
D4 gate does not skip a leg — it never sees the block — which is the same
outcome by a different route. The honest fix is a scope declaration (the block
is not graded) rather than a silent absence.

## 3. Lesson L-3 (D3) — recompute from the bases; reject disagreement with `D3-DERIVATION`

**Source.** `tools/check-evidence-coupling.py:871` `check_names`;
`SKILL.md:563` ("A native name's displayed expected value agrees but its bases
do not derive it → Recompute concat from the two E1 base forms; reject
disagreement with `D3-DERIVATION`, not a hand-approved spelling").

**Test.** Does the D4 leg resolve each base to its lexeme record and recompute
from the base's own form, or does it trust the record's stated stem?

**Verdict: FIRST HALF INHERITED, SECOND HALF NOT — and this is the review's
principal finding.**

D3's `check_names` does four things the D4 leg does not:

```python
# tools/check-evidence-coupling.py:879-908
bases = formation.get("bases")
if not isinstance(bases, list) or len(bases) != 2 or any(b not in lex for b in bases):
    continue                                    # ← base ids must RESOLVE to lexemes
e1_forms = [lex[b]["forms"]["E1"] for b in bases]   # ← recompute from the BASE's form
computed = "".join(e1_forms)
if formation.get("expected") != computed:  f.add("D3-DERIVATION", ...)
if rec.get("native_form") != computed:     f.add("D3-DERIVATION", ...)
for b in bases:
    if rec.get("native_form") == lex[b]["forms"]["E1"]:
        f.add("D3-DERIVATION", ...)             # ← a name may not equal its own base
```

Measured against the D4 leg (`adv.py` A8/A9, `adv-d11.py` W6,
`adv-d11-decisive.py` W6c, and — for the delivered gate —
`.scratch/r25-d15/adv-gate-receipt.json`):

| D3 discipline | D4 naming gate | D4 D11 harness | **delivered argot gate** |
|---|---|---|---|
| base ids resolve to lexeme records | **no** (`bases` unread) | **no** (stem from the record's own list) | **no** — `derived_from` compared as a **string** (§3.2) |
| recompute from the base's form | no | no — from the stated stem | yes — `apply(op, base_string)` |
| name may not equal its own base | **no such check** | **no such check** | **no such check** (§3.3) |

Consequence, measured: `L-48 haitun` → `kalmes` with bases rewritten to
`kal`+`mes` **replays clean, 0 violations, exit 0** (`adv-d11-decisive.py` W6c).
The leg checks that the writer's arithmetic is self-consistent, not that the
bases are the ones the language has. `execution-1.md` §4 states this bound for
the *rule* ("a record whose stated rule is not the rule the language actually
used"); this review extends it to the **bases**, which is the D3 lesson's
substance.

### 3.1 The delivered gate adds a laundering channel (measured)

`tools/gates/argot-derivation-gate.py` reads a record as in-scope when it
declares `derived_from` **and** `derivation`. Deleting one field takes the
record out of scope, and the violation disappears:

```
fixture Q-13 {term: suk, derived_from: sun, derivation: reverse}  → D4L-ARGOT-DERIV FAIL
same record, `derivation` deleted  → 5 findings become 4, no line names Q-13,
                                     coverage derived_pairs 8 → 7
same record, both fields deleted   → 4 findings, no line names Q-13
CONTROL: pair kept                 → the FAIL reproduces
```

This is D2's "laundered hold" class (`SKILL.md` T2) reached by a scope
predicate instead of a `return True` branch: the record is still in the packet,
still wrong, and now ungraded. A half-declared pair should be
`D4L-ARGOT-RULE` — the id the gate already uses for an unlicensed operation
(measured: `derivation: NOPE` → `D4L-ARGOT-RULE ×5`).

### 3.2 `derived_from` is a string, never a record reference (measured)

```
derived_from: ZZZZ   (no such record)       → FAIL (only because reverse(ZZZZ) ≠ nim)
derived_from: Q-04   (another record's id)  → FAIL (same reason)
```

The failure is incidental: the gate compares strings, so a `derived_from` naming
nothing fails for the right reason by accident. The class that does **not** fail
is a fabricated base that happens to yield the form (§3.3).

### 3.3 A self-derivation is accepted (measured)

```
{term: qqq, derived_from: qqq, derivation: reverse}   → no line names Q-02
{term: kin, derived_from: kin, derivation: head2}     → no line names Q-02
CONTROL {term: qqq, derived_from: min, derivation: reverse} → D4L-ARGOT-DERIV FAIL
```

`apply(op, base) == form` is satisfied trivially when `form == base`. D3 rejects
exactly this (`check-evidence-coupling.py:904-908`); the delivered gate does not.

**Summary of L-3.** The D3 lesson has two halves — *recompute* and *resolve the
base*. The delivered gate has the first and neither of the second's two parts
(base resolution, self-derivation rejection), plus a laundering channel that
turns a FAIL into silence. This is the review's principal finding and it applies
to the **delivered** artifact, not only the scratch harness.

## 4. Lesson L-4 (D3) — the id names the class, and a green leg is not a clearance

**Source.** `SKILL.md:563`; `reports/round-19/integration/d4-lessons-entry.md:71-79`
("exit 0 is not a clearance — it means the emitted findings equal the frozen
expected set").

**Test.** Is `D4L-ARGOT-DERIV` emitted by an engine, and is the leg's green a
clearance?

**Verdict: INHERITED BY THE DELIVERED GATE, NOT BY THE HARNESS.** The delivered
gate supersedes the harness on this lesson — it prints the id, carries the three
real exit codes, and prints a coverage line. Measured:

- `tools/gates/argot-derivation-gate.py` **does** emit `D4L-ARGOT-DERIV`:
  `FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-11 'saalum' … declared
  chain 'head2' applied to 'saalumi' yields 'saalu'`. Exit 1 with findings, exit
  0 clean, exit 2 with `D4L-ARGOT-DATA` on malformed input — the D2/D3 discipline.
- Its coverage line names every counter
  (`records=14 register_scoped=11 derived_pairs=8 borrow_pairs=3 violations=4
  rule_holds=1`), so a green run is legible rather than a bare 0.
- The harness, by contrast, is **not inherited**: it stamps the id as a row field
  (`argot-replay.py:48-72`) but never prints it (`:77` prints `r[0..5]`), and it
  has no verdict-carrying exit code (0 violations → exit 0, 1 violation → exit 0,
  well-formed packet → always exit 0).

The remaining defect is a **counter-integrity** one, and it is the §3.1
laundering channel seen from the coverage side: when a failing record's
`derivation` is deleted, the coverage line reports `derived_pairs 8 → 7` and
`violations 4 → 3` with **no malformed-pair finding**. The counter *drops* rather
than flagging, so the coverage line is not a trustworthy census of the declared
relation — it is a census of the records that happened to be well-formed. That
is the shape D2's lesson names ("a skipped leg is not an implementation") and
D3's names ("exit 0 is not a clearance") meeting in one place.

## 5. The four lessons in one table

| # | lesson | source | harness | **delivered gate** |
|---|---|---|---|---|
| L-1 | machine-readable operation + input | D2 (r19 lesson §5) | inherited for concat; encoding cannot express `head2`/`reverse` | **inherited, and `head2`/`reverse` are built in as declared ops** (`:115-175`) |
| L-2 | unreplayable ⇒ HOLD, never a pass | D2 (r19 lesson §5) | inherited in the gate; a register/lexicon block is invisible | **inherited** — `D4L-ARGOT-RULE` on an unlicensed op, `D4L-ARGOT-COVERAGE` on declared-not-delivered (selftested) |
| L-3 | recompute from the bases; reject disagreement | D3 (`check-evidence-coupling.py:871-908`) | first half only; bases never resolved; no self-derivation check | **first half only** — recomputes, but `derived_from` is a string and a self-derivation passes (§3.1-§3.3) |
| L-4 | the id names the class; exit 0 is not a clearance | D3 (`SKILL.md:563`) | **not inherited**; id unobservable, no exit code | **inherited**; residual counter-integrity gap when a pair is half-deleted (§4) |

## 6. What the leg does better than the D2 precedent, recorded so it is not lost

- The delivered gate reads with the naming gate's **own** budgeted matcher and
  template guard, loaded read-only by path, and prints the dependency digest on
  stdout (`dependency: tools/gates/naming-collision-gate.py sha256 …`) — so a
  reader can tell exactly which bytes replayed. That is the T4/dependency-naming
  lesson applied.
- It grades **both** the lexicon-derived records and the names in one pass
  (harness `:40-72`), where the naming gate grades names only. Real coverage gain.
- The delivered gate's `head2` fixture row is the design's own named trap
  (`saalum` vs `saalu`), so the maximal-onset reading is tested, not asserted.
- Its reports state their own bounds (`execution-1.md` §4, `execution-4.md` §2-§3)
  rather than implying a clearance. The findings in §3-§4 are about the
  *mechanism*, not about the reports' honesty.

## 7. What this seat did not do

- Wrote only this file. Fixtures and receipts under `.scratch/r25-d15/`.
- Did not edit any tool, gate, packet, component, or rounds 8–24 artifact; did
  not commit or push.
- Did not adjudicate promotion, the culture fork, or whether the register half
  should be built; those are the parent's calls and are named in
  `execution-4.md` §4.
- Did not re-derive `forecast.md` / `current-state.md` / `delta.md`; this file
  consumes them and tests the leg against the D2/D3 lessons.

## 8. Receipts

`cwd = /home/vgpnk/Projects/shokunin/kotodama-shokunin`, `TMPDIR=$PWD/.scratch`,
2026-10-18T17:29–17:32Z.

| id | command | observed |
|---|---|---|
| R-1 | `grep -n "def check_names" tools/check-evidence-coupling.py` | `:871` |
| R-2 | `sed -n '871,908p' tools/check-evidence-coupling.py` | base ids resolved to `lex`; `computed = "".join(e1_forms)`; `D3-DERIVATION` on mismatch; name-equals-base rejected |
| R-3 | `python3 .scratch/r25-d15/adv-d11-decisive.py` W6c | `violations 0`, exit 0 (fabricated bases pass) |
| R-4 | `python3 .scratch/r25-d15/adv.py` A11 sweep | at 17:32Z: `D4L-ARGOT-DERIV` in 0 files under `tools/`, `examples/`; **superseded** — `tools/gates/argot-derivation-gate.py` (landed 14:33) emits it |
| R-5 | `python3 .scratch/r25-d15/adv.py` A5 | `doublets` block invisible: 14 findings with and without it; control in `names` → `PHON-INVENTORY` 6→7 |
| R-6 | `python3 .scratch/r25-d11/argot-replay.py` on baseline / tampered / malformed | exit 0 / exit 0 / exit 1 (uncaught `KeyError`) — no verdict-carrying exit code |
| R-7 | `grep -n "D4L-ARGOT-DERIV" reports/round-25/argot/forecast.md` | `:41-47` reserves the id for Δ3 and separates it from `DERIV-REPLAY` |
| R-8 | `python3 .scratch/r25-d15/adv-gate-receipt.json` (delivered gate) | F1 launder: 5→4 findings, `derived_pairs` 8→7; F2 self-derivation: no line names Q-02; F4 unlicensed op: `D4L-ARGOT-RULE ×5` |
| R-9 | `sha256sum tools/gates/argot-derivation-gate.py`; `--selftest` | `07db6e9b…`; `18/18 checks passed` |
