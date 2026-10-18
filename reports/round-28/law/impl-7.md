# R28-D11 — the leg's own limits, and the wiring decision

- **Seat:** R28-D11 (D axis, law-replay implementation 7 of 8). Round 28, loop 3
  build 4 of 4, claim **D** `register-law-replay`. Integrator: `impl-1.md`.
- **Date:** 2026-10-18. Baseline `6c0ac448…`; lane HEAD `69cecbc`.
- **Write scope:** this file only; scratch under `.scratch/r28-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. Declared limits of the replay leg

The design declared nine (`LD-1..LD-9`). This implementation's own limits, with
the measurement that fixes each:

| id | limit | measured |
|---|---|---|
| LL-1 | the `force` vocabulary is the **gate's own** closed set, not the packet's | the packet declares no `force` vocabulary (round-28 audit X59-F5: `force_vocabulary=0`); a packet-only resolution could never fire |
| LL-2 | a **bare office name** with no `(ID)` token is not resolved | there is no roster block to resolve it against; `AGENT_ID_RE` reads the `Name (ID)` shape only |
| LL-3 | `consequence` is a **stem** match, and the stem list is the gate's contract | printed in the finding text so a reader can disagree; `LD-4` |
| LL-4 | cross-row delegation is not followed | `RGL-04`/`RGL-05`'s `"any speaker admitted by RGL-01 or RGL-03"` is prose; `LD-1` |
| LL-5 | the `act` text is not resolved | free prose; `LD-3` |
| LL-6 | `CONSEQUENCE` and `DANGLING` are **saturated** on the clean packet | a further tamper adds a *line*, not a *class* — which is why the round runner grades lines |
| LL-7 | every class is a **hold or fail**, and the split is the gate's declaration | `SPEAKER`/`FORCE`/`CONSEQUENCE`/`REGISTER`/`AXIS` are FAIL; `ROW`/`KIND`/`DANGLING` are HOLD. The design made all six holds (`LD-8`); this implementation upgrades the five *contradiction* classes to FAIL because a row naming an unresolvable id or an undeclared force is a malformed record, not an open question. Declared so the difference is visible. |
| LL-8 | the leg is **not registered** in the battery | see §2 |
| LL-9 | the leg is **not wired** into the typed pipeline | see §2 |
| LL-10 | the leg reads the packet, never the components | it cannot see a law row the assembler dropped; that is the assembler's own `--check` surface |

## 2. The wiring decision, and why it is the cheap one

**The leg is deliberately standalone.** It is not invoked by
`tools/gates/typed-pipeline-gate.py` and is not registered in
`tools/check-gate-battery.py`'s nine-gate set. Three measured reasons:

**(a) Wiring it into the typed gate would drift a frozen surface.**
`tools/gates/typed-pipeline-gate.py` is byte-pinned in the filed round-26
manifests, and those rows are currently **GREEN**:

```
tools/gates/frozen/round-26/gate-input/MANIFEST.tsv       gate=b749ad07cf17… GREEN
tools/gates/frozen/round-26/post-register/MANIFEST.tsv    gate=b749ad07cf17… GREEN
```

Editing that file would drift all six rows, and the O seat's sweep would owe a
re-pin for a change that buys nothing the standalone leg does not already give.
The sibling argot gate is wired because it was wired in round 25, when the
manifest pin was already moving; the pin is not moving now.

**(b) Registering it in the battery would fail closed.** The battery's own rule
is explicit: "Registering a gate makes the battery *ask* for its baseline: without
a committed `expected.json` it reads `BASELINE-GATE-UNCOVERED`, exit 2." So
registering the gate *without* also committing a baseline pair would turn a green
battery red. Committing a baseline pair is a legitimate move — but it is a
different claim's work (the O sweep owns the baseline roots), and doing it inside
a D seat would move the battery's `coverage 9/9` count as a side effect.

**(c) The leg is discovered anyway.** The round runner walks every `*.py` under
`tools/` **and** `reports/round-28/` that names the class
(`law_finding_producers()`), and runs the discovered legs on the clean packet and
on its three tampers. So the leg is measured by the round's own acceptance
surface without being wired into a frozen one:

```
$ python3 reports/round-28/run-validation.py --check | … law_finding_producers
['tools/gates/register-law-gate.py', 'reports/round-28/gate-tests/run-gate-tests.py',
 'reports/round-28/scribe/x54-law-negatives-spotcheck.py']
```

**The trade is stated, not hidden:** the leg fires only when invoked directly or
by the round runner. A later round that wants it always-on owes the baseline pair
and the manifest re-pin, and both are named here.

## 3. The gate's contract, for a reader who wants to disagree with it

Every set the leg resolves against is a module-level constant with a comment
naming its authority:

| constant | value | authority |
|---|---|---|
| `LAW_DECLARED_ROWS` | `RGL-01..RGL-05` | `reports/round-27/law/impl-1.md` |
| `DECLARED_FORCE_CLASSES` | `assertive/directive/commissive/expressive/declarative` | `design.md` §3; Searle's five |
| `DECLARED_FORCE_MODIFIERS` | `binding/refused/not-rollable/none/attested/witnessed/naming/constraint` | the landed rows' own qualifiers |
| `DECLARED_KINDS` | `admissibility/exclusion/asymmetry/no-segment/era/enforcement/procedure` | `design.md` §3, `impl-2.md` §1 |
| `SPINE_AXES` | `mark/fire/cloth/wind/word/knot/water/both/neutral` | `01-brief.yml` |
| `CONSEQUENCE_STEMS` | `roll/rk-/rank/tally/rite/rit-/entry/written/record/void/binds/binding/no entry` | the delivered packet's own machinery |
| `NON_FORCE_RE` | `^\s*none\s*(?:[—–\-:,]|$)` | the landed rows' `none — …` shape |

A reader who disagrees with a set can read it off the file, change it, and see
which findings move — because the sets are data, not control flow.

## 4. What the leg proves, and what it does not

**Proves:** the law's own fields resolve against the packet's own blocks, and a
tampered row produces a named finding the clean packet does not. That is the
claim's `after_required` clause, measured by behaviour.

**Does not prove:** that the law is *complete*, *correct*, or *enforced*. The leg
resolves a row's internal consistency and its references. It does not decide
whether the four acts are the right acts, whether the speaker sets are the right
sets, or whether the register should exist at E1. Those are the design's declared
open questions (`design.md` §5, `review.md`), and the law remains a NON-CANON
design statement with **zero** enforcement in the delivered pipeline.

**Exit 0 is not a clearance.** It means "every resolution the leg performs found
nothing to report". On the delivered packet the leg exits **1** with four honest
holds, and that is the correct reading.

## 5. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
grep -n "DECLARED_FORCE_CLASSES\|DECLARED_FORCE_MODIFIERS\|DECLARED_KINDS\|SPINE_AXES\|CONSEQUENCE_STEMS\|NON_FORCE_RE\|LAW_DECLARED_ROWS" tools/gates/register-law-gate.py
grep -c "register-law-gate" tools/gates/typed-pipeline-gate.py tools/check-gate-battery.py   # 0 and 0
python3 reports/round-28/run-validation.py --check | python3 -c "import json,sys;print(json.load(sys.stdin)['claims']['D']['measurement']['law_finding_producers'])"
python3 tools/check-gate-battery.py 2>&1 | grep -o '"coverage": "[^"]*"'
```
