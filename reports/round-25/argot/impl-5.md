# R25-D05 — argot-derivation leg, impl 5 of 6: the typed-gate binding, and D2 byte-identity

- **Seat:** R25-D05, round 25, claim **D**. Date 2026-10-18.
- **Write scope:** the round-25 binding block inside
  `tools/gates/typed-pipeline-gate.py`, and this file.
- **Canon:** NON-CANON engineering evidence.

## 1. The binding

`tools/gates/typed-pipeline-gate.py` gains one constant, one invocation block,
and two small report changes. Nothing else in the file is touched.

- **constant:** `ARGOT_GATE = GATES_DIR / "argot-derivation-gate.py"`.
- **invocation:** at the top of the L1 section, guarded on `generalized and
  ARGOT_GATE.is_file()`, the sibling is launched with the same single input
  (`packet_path`, or the typed artifact when one was named) via the gate's own
  `run_gate` (`[python3, <gate>, <input>]` — flagless, so the sibling stays
  freezable). Its stdout digest is recorded under `result["argot"]`.
- **verdict:** its `FINDING D4L-ARGOT-*` lines are captured; a `FAIL` line joins
  `result["findings"]` and fails a new `L3b-argot` leg, so a form the stated
  inputs and rules do not yield cannot read green.
- **reporting:** the captured lines are printed on **both** the exit-2 and the
  normal path, and included in the `--json` document on the exit-2 path. This
  matters: the runner's own violating-derivation probe mutates
  `derivation_rules:` and the run refuses earlier at `L1-assembler` (the mutated
  bytes are not the assembler's build). Without the both-path print the leg's
  named diagnostic would be hidden behind that refusal — the same "the gate
  reports a red it did not find" class the O claim repairs, inverted.
- **selftest:** `--selftest-generalized` mirrors the sibling and its two fixture
  files into the temp mirror and adds two named controls (`argot derivation leg:
  the mirrored sibling selftest is green`, `… the mirrored leg runs on the family
  packet`), so the runner's `names_argot_control` leg finds the leg named in the
  typed gate's own selftest output.

## 2. D2 byte-identity — the guard, measured

The invocation is guarded on `generalized`, so the D2 default run is unchanged.
Measured against the O-band's **own committed round-25 pins** (not against my own
earlier capture), which is the stronger control:

| invocation | live stdout sha256 | round-25 frozen pin (`tools/gates/frozen/round-25/gate-input/MANIFEST.tsv`) | match |
|---|---|---|---|
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml` | `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` | `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` | **yes** |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml` | `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` | `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` | **yes** |

Both are byte-identical to the pins recorded by the O-band before this leg
landed. The D2 path — assembler `--check`, `d2-typed-labels.py --check`, and the
flagless D2 default run — is unaffected:

```
$ python3 tools/assemble-d2.py --check
packet.d2.yml: byte-identical deterministic assembly                      exit 0
$ python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml --check examples/culture-d2/typed-labels.d2.yml
examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic projection   exit 0
$ python3 tools/gates/typed-pipeline-gate.py
summary: 16/16 legs passed                                               exit 0
```

## 3. D4 moves by exactly the new leg, and the pins are named

| invocation | before this leg | after | leg count |
|---|---|---|---|
| `… examples/culture-d4/packet.d4.yml` | exit 0, `b064da28…`, 19/19 | exit 0, `d36a9f9b…`, **20/20** | +`L3b-argot` |
| `… examples/culture-d4/packet.d4.typed.yml` | exit 0, `38dc76dc…`, 16/16 | exit 0, `df1bb53b…`, **17/17** | +`L3b-argot` |

The two D4 output digests move because a leg was added, not because a finding
changed: the hold set is unchanged (12 holds / 0 notes / 0 fails, `L3-holds` and
`L3-counts` green), and the new leg passes on the delivered tree
(`violations=0`). `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` pins the
typed gate's **pre-leg** bytes (`879d40bf…`) and the two pre-leg D4 outputs; a
re-pin is a **new row**, which the round-25 scribe (R25-D19) owns — this fragment
names the movement and does not edit any filed MANIFEST.

## 4. Teeth control

```
$ python3 tools/gates/typed-pipeline-gate.py .scratch/round-25/validation/argot-control/violating.d4.yml
declared pipeline: family None; profile tools/gates/typed-pipelines.json (sha256 396f4678133a); …
FINDING D4L-ARGOT-RULE: HOLD — form NM-01 'tumhai': claims formation rule 'CX-01' but the packet declares no `morphology.derivation_rules`; the chain is not replayable
…
exit 2
```

and with a *broken stem* rather than a lost rule set (a violation, not an
unreplayable chain), the leg emits `D4L-ARGOT-DERIV` FAIL and `L3b-argot` fails:

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r25-d05/controls/c2-bad-derivation.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-99 'saalum' (register 'quote'): declared chain 'head2' applied to 'saalumi' yields 'saalu'; the stated inputs and rules do not yield the candidate
exit 1
```

Both directions are asserted in the sibling's `selftest`
(`formation-control-rules-lost-held`, `formation-control-bad-stem-fails`) and the
binding's own control is measured by the round-25 runner
(`control_violating_derivation` → `argot_id_emitted: true`).
