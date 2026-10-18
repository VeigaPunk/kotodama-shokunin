# R27-D14 — the typed gate and both assemblers on the amended packet: green

- **Seat:** R27-D14 (gate runs 2 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law` (`reports/round-27/claims.json:14-28`).
- **Date:** 2026-10-18. Declared baseline `4f09c990…`; lane HEAD at every
  measurement `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- **Write scope:** as D13 (`reports/round-27/gate-tests/**`), plus gitignored
  scratch. No tool, gate, packet, component, projector, pin, fixture or filed
  rounds 8–26 byte written; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

## 0. Verdict

**The typed gate passes on both graded entries with no FAIL leg, the live hold
counts equal the frozen hold set, and both assemblers plus both gate-shaped
adapters are byte-identical on the amended packet.**

| entry | command | exit | legs | hold lines |
|---|---|---:|---:|---:|
| D4 typed packet | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | **0** | **17/17** | 12 |
| D4 source packet | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **0** | **20/20** | 12 |
| D4 assembler | `python3 tools/assemble-culture-d4.py --check` | **0** | — | `byte-identical deterministic assembly` |
| D4 typed adapter | `python3 tools/assemble-d4-typed.py --check` | **0** | — | `byte-identical deterministic typed packet` |
| assembly-check adapter | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | **0** | — | — |
| projection-check adapter | `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | **0** | — | — |
| projector | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | **0** | — | — |

The `L3b-argot` leg is **ok** on both entries, so the register stratum's
derivations ride the typed pipeline as well as the source packet.

**Re-measured after the round-27 landing.** The first pass of this seat ran on
the pre-law packet (`dd25077b…`, holds `d6136488…`); the register law and the
syllabify fix landed mid-wave, so the whole battery was re-run. The table above
is the **post-landing** reading, and the leg counts are unchanged at 17/17 and
20/20 — the law added five packet records and no new leg, which is the right
shape (a declaration, not a new pipeline stage).

## 1. The hold set is named and unchanged, and the runner says why that is correct

```
declared (examples/culture-d4/expected-holds.json): {'fail': 0, 'hold': 12, 'note': 0}
live    (typed-pipeline-gate.py --json)           : {'fail': 0, 'hold': 12, 'note': 0}
```

`L1-expected-holds`, `L3-holds`, `L3-notes`, `L3-fails`, `L3-counts`,
`L3-details`, `L3-baseline`, `L3-baseline-set` and `L4-pins` all read **ok**, so
the live counts are not merely printed — they are compared against the frozen
file row by row.

**A hold count that stays 12 is the correct outcome here, not a miss.** A
register field never moves a form off the sound-and-identity channel
(`SKILL.md` slot-label routing table), so the register stratum owes **no** form
slot and the twelve garment/slot obligations are the unchanged correct set. The
round-26 revision note and `supersedes_pins` block already record that reasoning
(`examples/culture-d4/expected-holds.json`); this seat re-measures it rather than
inventing a hold to move the number.

## 2. Leg counts are a floor, not an equality

The runner requires `>= 17` (typed) and `>= 20` (source) legs, not `==`. A
battery that pinned the exact count would fail an honest later improvement — the
round-26 battery made the same choice explicitly
(`reports/round-26/gate-tests/run-gate-tests.py:141-145`). A **drop** below the
floor is the regression; an addition is not.

## 3. The four entry points, and why each is measured

The two assemblers and the projector are the build path; the two adapters are
the **pinnable** form of that path (`tools/replay-frozen.py` launches a pinned
gate as exactly `[python3, tools/gates/<gate>.py, <input>]`, so a flag-shaped
check could not be pinned). Measuring both means a frozen row's verdict and the
build path's verdict are both known to be green at this stamp, rather than
inferred from one another.

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc` |
| `examples/culture-d4/typed-labels.d4.yml` | `88a94422b4123f6b…` |
| `examples/culture-d4/packet.d4.typed.yml` | `1c4b88088b696a13…` |
| `examples/culture-d4/expected-holds.json` | `857417e949fb5cb9…` |

The three truncated digests are the ones the final run pinned; the packet digest
is quoted in full because it is the graded input. **The packet was regenerated
several times during the wave** (the law landing, then a hold-set re-pin), so
these are the last-measured values, and the runner re-pins all of them on every
run — `receipt.json`'s `inputs` map is the authoritative record.

## 4. Limits

- **The adapters are not selftest legs here.** Each resolves `ROOT` from its own
  file location and loads a peer plus the `examples/culture-d4/` tree, so a
  mirrored `--selftest` launch could only report could-not-evaluate — the same
  reason `tools/check-gate-battery.py` excludes them from its selftest duty and
  grades them by committed baseline instead. This seat grades them by their own
  CLI over the live tree, which is what a pinned row does.
- **`--check` is byte-identity, not soundness.** Exit 0 asserts the projection
  is the projector's own deterministic build, not that its content is right.
- **Green at one stamp.** The packet and projection digests above are the ones
  measured; a later landing supersedes this reading and needs a dated refresh.
