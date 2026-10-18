# R28-D13 — the argot gate on the amended packet: green, deterministic, and the register block it grades

- **Seat:** R28-D13 (gate runs 1 of 4), round 28, loop 3 build 4 of 4, claim **D**
  `register-law-replay` (`reports/round-28/claims.json:9-18`).
- **Date:** 2026-10-18 (measurements 20:1xZ). Declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (`claims.json:5`); lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86` at every measurement.
- **Write scope:** `reports/round-28/gate-tests/{run-gate-tests.py,receipt.json,D13..D16*.md}`
  plus gitignored scratch under `.scratch/r28-d13/`. `export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command. **No tool, gate, packet, component,
  projector, pin, fixture or filed rounds 8–27 byte was written; no commit, no
  push.**
- **Canon:** NON-CANON engineering evidence. A green gate is a measurement, not a
  clearance; a hold stays a hold.

## 0. Verdict

**The argot gate is green on the amended packet, three runs byte-identical, and
the register block it grades has landed.** The round's own claim is that the
*packet surface moved again* (RL-4), and this seat is the first of the four to
re-measure the surface after the move.

| check | command | exit | evidence |
|---|---|---:|---|
| the graded run | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **0** | `records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| determinism | the same, 3× | 0,0,0 | **1** distinct stdout digest |
| the gate's own controls | `... --selftest` | **0** | `selftest: 27/27 checks passed` |
| the whole battery | `python3 reports/round-28/gate-tests/run-gate-tests.py` | **0** | `summary: 57/57 checks passed` — all four seats green after the law leg and the re-pin landed |
| the runner's controls | `... --selftest` | **0** | `selftest: 31/31 checks passed` |
| the register **identity** block | `grep -n '^registers:' …` | — | present; `QREG-01..04` |
| the register **law** block | `grep -n '^register_law:' …` | — | present; `RGL-01..05` |

Pinned at the measurement:

```
tools/gates/argot-derivation-gate.py   sha256 b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb
examples/culture-d4/packet.d4.yml      sha256 543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f
examples/culture-d4/components/13-register-law.yml
                                       sha256 c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7
examples/culture-d4/components/03-orthography.yml
                                       sha256 0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b
examples/culture-d4/components/09-costumes.yml
                                       sha256 f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23
```

**The packet digest moved from round 27's `86079a67…` to `543d68a8…`**, and that
move is the whole reason this build round exists: the RL-4 fix added the
`records`, `literacy_institutions` and `enforcement` blocks to the packet. The
argot gate reads the packet and is unaffected by the addition — its record count
rises (`170` → `175` → **`183`**, +8 for the newly-reachable records), and every
counter that decides a verdict stays at zero.

## 1. What the coverage line means, and what it does not

| counter | value | reading |
|---|---:|---|
| `records` | **183** | every packet record the gate walked. It was 170 before round 27's law landed, 175 after it, and **183 now**: the RL-4 fix landed OR-01..03, LI-01..03 and EN-01..02 as packet records, +8. |
| `register_scoped` | 14 | 8 register forms + 6 borrow pairs on declared register layers. Unchanged: the fix added no register form. |
| `derived_pairs` | 8 | the eight `stamp` forms replay their base under the axis rule. Unchanged. |
| `claimed_chains` | 8 | the same eight, declared as chains. |
| `borrow_pairs` | 6 | the loan-layer pairs. |
| `violations` | **0** | no derivation disagrees with the design. |
| `rule_holds` | **0** | no rule is stated but unexecutable. |

The `records` rise is the honest signature of the RL-4 fix, and it is the one
counter a reader should expect to move. **A fix that declared the `packet_keys`
but dropped the records would leave `records` at 175** — which is why D16 grades
the records **by id**, not by the counter.

The coverage line's own dependency row names the peer the gate loaded, so the
replay says which bytes it used rather than assuming them:

```
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

## 2. The register block: present, and law rows included

The claim's D surface is the register law. Both blocks the law lives in are on
the packet:

```
registers:      QREG-01, QREG-02, QREG-03, QREG-04     (identity rows, round 26)
register_law:   RGL-01..RGL-05                          (speech-act rows, round 27)
```

The argot gate does not read the law rows — the law has no owner in that gate
(`reports/round-27/law/rules.md` §1: `RLAW-04`/`RLAW-05` are unowned) — so this
seat records their presence as a packet fact and grades their *teeth* under D15.
**Presence is not enforcement**, and this file does not claim it is.

## 3. The runner's own controls

`--selftest` is dependency-free and covers the parsers and the discovery logic,
including the three bugs this runner shipped with and fixed (see D15 §2):

```
selftest: 31/31 checks passed
```

The controls include the usage-error reader: a probe that cannot tell an argparse
rejection from a verdict is the failure mode that made D15 grade its own typo.
It is measured against a real flagless instrument on disk
(`reports/round-28/audit/x60-sweep-completeness.py`), not a fixture.

## 4. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
python3 reports/round-28/gate-tests/run-gate-tests.py --selftest | tail -1
grep -c 'id: "QREG-' examples/culture-d4/packet.d4.yml
grep -c 'id: "RGL-' examples/culture-d4/packet.d4.yml
sha256sum examples/culture-d4/packet.d4.yml tools/gates/argot-derivation-gate.py
```
