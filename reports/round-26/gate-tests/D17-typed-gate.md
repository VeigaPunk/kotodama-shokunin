# R26-D17 — the D4 typed gate: green, with the hold set updated and named

- **Seat:** R26-D17 (gate+tests 1 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum` (`reports/round-26/claims.json:14-23`). This is the first of
  the four `D R26-D17..D20 (gate+tests x4)` seats.
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (`claims.json:5`); lane HEAD at every measurement
  `1ad491a1a4b0aef9ebdc1861dfb8237727503825` (`git log --oneline -1`).
- **Write scope:** `reports/round-26/gate-tests/{run-gate-tests.py,freeze.py,fixtures/**,receipt.json,D*.md}`
  and `tools/gates/frozen/round-26/{gate-input,post-register}/**` (new
  generations), plus gitignored scratch under `.scratch/r26-d17-d20/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. **No
  tool, gate, packet, component, projector, pin or filed rounds 8-25 byte was
  written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence. A green gate is a measurement, not
  a clearance; a hold stays a hold.

## 0. Verdict

**The D4 typed gate is green on both graded entries, and the hold set is
updated and named.** The register stratum landed mid-wave (packet
`e7ecd204…` → `dd25077b…` at 18:19:48Z), and this seat re-measured against the
settled tree.

Measured (lane root, `2026-10-18T18:22Z`, `TMPDIR=$PWD/.scratch`):

| entry | command | exit | legs | hold lines |
|---|---|---:|---:|---:|
| D4 typed packet | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | **0** | **17/17** | 12 |
| D4 source packet | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **0** | **20/20** | 12 |
| typed selftest | `... --selftest` | 0 | — | `19/19 checks passed` |
| generalized selftest | `... --selftest-generalized` | 0 | — | `16/16 checks passed` |

The `L3b-argot` leg is **ok** on both entries, and `--json` reports
`counts {'fail': 0, 'hold': 12, 'note': 0}` on the typed packet — identical to
`examples/culture-d4/expected-holds.json` (`counts {'hold': 12, 'note': 0,
'fail': 0}`, sha256 `d6136488e22f989e…`).

The argot leg's own coverage line over the settled packet:

```
coverage: examples/culture-d4/packet.d4.yml records=170 register_scoped=14
  derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
```

## 1. The hold set is updated and named

`expected-holds.json` carries a round-26 `revision_note` and `supersedes_pins`
block naming the pre-register packet (`e7ecd204…`) and projection (`60b526b0…`).
The note's substance:

> *"round-26 register-stratum build (2026-10-18): the stamp register landed in
> 04-lexicon.yml (8 register-scoped records, the registers law block, the
> LENGTHEN rule and the derivation_ops declaration), so the D4 packet and its
> projection were regenerated. The hold set is UNCHANGED at 12 holds / 0 notes /
> 0 fails: the six owed garment forms still route to their twelve record/slot
> rows, and the register stratum owes no form slot because a register field
> never moves a form off the sound-and-identity channel (SKILL.md slot-label
> routing table)."*

Both readings of the claim's leg are now met:

| reading | requirement | measured | verdict |
|---|---|---|---|
| **named** | the gate grades against a frozen expected set and prints it | `L3-holds`/`L3-details`/`L3-baseline-set` all ok; file present; `--json` `counts` equal the file's | **MET** |
| **updated** | the hold set reflects the register stratum the claim lands | round-26 `revision_note` + `supersedes_pins` naming the pre-register pins; count **unchanged at 12/0/0 by design**, and the note says why | **MET** |

**A count that stays 12 is not a failure here.** The register forms owe no form
slot — a register field does not move a form off the sound-and-identity channel
— so the twelve garment/slot holds are the correct, unchanged set. The claim
asked the hold set be "updated and named"; the update is the revision note and
the supersession pins, not a new hold row. This seat records that distinction
rather than inventing a hold to move the number.

## 2. The battery this seat lands

`reports/round-26/gate-tests/run-gate-tests.py` is the executable form of the
four seats. It is self-describing (every run names its command, exit and date)
and it has its own dependency-free selftest (10/10, `--selftest`).

```
python3 reports/round-26/gate-tests/run-gate-tests.py            # measure + receipt
python3 reports/round-26/gate-tests/run-gate-tests.py --check    # measure only
python3 reports/round-26/gate-tests/run-gate-tests.py --selftest # runner's own controls
```

Result at 2026-10-18T18:22Z: **62/62 checks passed, exit 0**
(`reports/round-26/gate-tests/receipt.json`, `passed: true`).

| seat | leg | checks |
|---|---|---:|
| D17 | gate green, legs counted, hold set named and equal to the frozen file | 14 |
| D18 | eight negative/positive fixtures, id spelling, discrimination | 20 |
| D19 | five graded entries × 3 runs byte-identical; four selftests green | 17 |
| D20 | eleven frozen generations replayed; the newest round-26 re-pin 6/6 | 3 |
| teeth | plant → rebuild → `D4L-ARGOT-DERIV` → revert green | 8 |

## 3. Pins measured at this revision (settled post-register tree)

| path | sha256 |
|---|---|
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` |
| `tools/replay-frozen.py` | `a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464` |
| `examples/culture-d4/packet.d4.yml` | `dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67` |
| `examples/culture-d4/packet.d4.typed.yml` | `618a78c90fc04c0d…` |
| `examples/culture-d4/expected-holds.json` | `d6136488e22f989e109c435cb4f7eb02ca680043785e88e78038ed5f47150fd3` |

A later edit to any of these invalidates this fragment's readings and requires a
dated re-run.

## 4. Limits

- **A green gate is not a clearance.** The twelve hold rows are open design
  debt; exit 0 means the emitted set equals the frozen set, nothing more
  (`typed-pipeline-gate.py` banner).
- **The leg count is a floor, not an equality.** The battery asserts `>= 17`
  (typed) / `>= 20` (source); the pre-register counts are the regression floor.
  A drop below them fails; an added leg passes.
- **This seat measured a moving tree.** The pre-register readings are kept in
  `receipt.json`'s `runs` history; the §0-§3 numbers are the settled post-register
  tree at 18:22Z. A further packet edit requires a re-run.
