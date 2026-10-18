# R28-D14 — the typed gate and both assemblers on the amended packet: green

- **Seat:** R28-D14 (gate runs 2 of 4), round 28, loop 3 build 4 of 4, claim **D**
  `register-law-replay` (`reports/round-28/claims.json:9-18`).
- **Date:** 2026-10-18 (measurements 20:1x–20:2xZ). Declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`; lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **Write scope:** this file only; scratch under `.scratch/r28-d13/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No tool,
  gate, packet, component, pin or filed rounds 8–27 byte was written.
- **Canon:** NON-CANON engineering evidence.

## 0. Verdict

**The typed gate and both assemblers are green on the amended packet, and the
green is measured in two states.** This seat first measured the surface **before**
the O seat's re-pin landed and recorded a `L1-profile` drift; it then re-measured
**after** the re-pin. Both readings are kept, because the drift is the round's own
predicted consequence of the RL-4 fix and its resolution is claim O's evidence.

| check | command | exit | evidence |
|---|---|---:|---|
| the source assembler | `python3 tools/assemble-culture-d4.py --check` | **0** | `packet.d4.yml: byte-identical deterministic assembly` |
| the typed adapter | `python3 tools/assemble-d4-typed.py --check` | **0** | `packet.d4.typed.yml: byte-identical deterministic typed packet` |
| the assembly-check gate | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | **0** | `byte-identical deterministic assembly` |
| the typed-labels-check gate | `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | **0** | `byte-identical deterministic projection` |
| the projector's own check | `python3 tools/d2-typed-labels.py --packet … --check …` | **0** | `byte-identical deterministic projection` |
| the typed gate, source packet | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **0** | `summary: 20/20 legs passed` |
| the typed gate, typed packet | the same, on `packet.d4.typed.yml` | **0** | `summary: 17/17 legs passed` |
| the live hold counts | `… --json` | — | live `{hold: 12, note: 0, fail: 0}` == the frozen set |

Both assemblers and both adapters regenerate their outputs **byte-identically**,
and the typed gate runs its full leg count on both entries with no `FAIL` leg.

## 1. The pin drift, and its resolution

Before the re-pin landed, the typed gate exited 2 at `L1-profile` and ran only 2
legs, because two digests in the pipeline profile were still round-27's:

| surface | declared (round 27) | live (round 28) |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `86079a6708a0…` | **`543d68a82640…`** |
| `examples/culture-d4/typed-labels.d4.yml` | `88a94422b412…` | **`339bfd83bf66…`** |

The drift was **exactly the RL-4 packet change** — `reports/round-28/law/design.md`
§4 named it as "one pin-moving change" — and the live digests are the correct
ones: the assembler regenerates them byte-identically, so the remedy was the
re-pin, never a revert of the fix. **Claim O landed it**, and the re-measurement
is green:

```
tools/gates/typed-pipelines.json   sha256 7f5a9c722a5ccca51f15b704368831381a428f1b977ad75c5b88aa85704a886a
  :12   "sha256": "543d68a82640e1b0…"   ← re-pointed
  :20   "sha256": "339bfd83bf668324…"   ← re-pointed
```

The hold set was re-pinned in the same sweep:

```
examples/culture-d4/expected-holds.json
  sha256 65f5a03e092fb4bb1e04f26d73180ca411c1f91bd29d2f1912d275407e15e423
  "packet_sha256":     "543d68a82640…"   ← re-pointed
  "projection_sha256": "339bfd83bf66…"   ← re-pointed
  counts: {hold: 12, note: 0, fail: 0}   ← unchanged, as the claim predicted
  supersedes_pins: the round-27 digests, recorded as a NEW block
  revision_note: names the round-28 landing and both repairs (RL-4 and RL-1)
```

**The hold count is unchanged at 12/0/0, and the change is honest rather than
inert:** a law row is not a form, so the six garment-form obligations still route
to their twelve record/slot rows and the register stratum owes no form slot. The
`revision_note` carries both tokens claim O requires (`names_round_28`,
`names_the_fix`), and the round-27 pins are recorded under `supersedes_pins`
rather than overwritten — a re-pin is a new row, as the claim demands.

## 2. What this seat certifies

**Certified:** the two assemblers, the two gate-shaped adapters, the projector and
the typed gate — on both the source and the typed packet — are green, with the
live hold counts equal to the frozen set and no `FAIL` leg. The amended packet is
the deterministic output of its components.

**The build was never the red.** At no point in this seat's measurement did a
build step fail; the only red was the pin comparison, and it is now resolved.

## 3. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-culture-d4.py --check
python3 tools/assemble-d4-typed.py --check
python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml       # 20/20
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml # 17/17
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml \
          tools/gates/typed-pipelines.json examples/culture-d4/expected-holds.json
```
