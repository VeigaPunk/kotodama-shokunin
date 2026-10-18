# R26-D19 — determinism: consecutive runs byte-identical on every graded entry

- **Seat:** R26-D19 (gate+tests 3 of 4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum`.
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **Write scope:** this fragment plus `reports/round-26/gate-tests/**` and
  gitignored scratch. No tool, gate, packet, pin or filed 8-25 byte written.
- **Canon:** NON-CANON engineering evidence. Determinism is a reproduction
  property, not a verdict about the design.

## 0. Verdict

**Every graded entry is byte-deterministic across three consecutive runs, with a
stable exit code, and every tool's own selftest is green.** Five entries, three
runs each, stdout sha256 compared (`TMPDIR=$PWD/.scratch`, settled post-register
tree, 2026-10-18T18:22Z):

| entry | command | exits | distinct digests | stdout sha256 (16) |
|---|---|---:|---:|---|
| D4 typed packet | `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 0/0/0 | **1** | `67056bb9090e437d` |
| D4 source packet | `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0/0/0 | **1** | `3eb9042e066426fd` |
| D2 typed packet | `typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml` | 0/0/0 | **1** | `9a69985aabdf3e9b` |
| D2 source packet | `typed-pipeline-gate.py examples/culture-d2/packet.d2.yml` | 0/0/0 | **1** | `15cdfbda73cd56cb` |
| argot D4 | `argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0/0/0 | **1** | `4c29a83965f38254` |

The D4 digests moved from their pre-register values when the register stratum
landed (`packet.d4.yml e7ecd204… → dd25077b…` at 18:19:48Z); the D2 digests did
not, which is the cross-family control — the register landing touched D4 only.

The D2 typed-packet digest `9a69985aabdf3e9b…` is the same value the round-18
determinism seat recorded as the pre-generalization baseline
(`reports/round-18/d4/determinism.md` §2) — the D2 path still reproduces the
pre-generalization bytes, which is the regression the round-18 seat was
guarding.

## 1. The tools' own selftests

A green selftest is the deterministic-regression floor: each tool re-derives its
own controls from committed bytes every run.

| selftest | command | exit | summary |
|---|---|---:|---|
| typed | `typed-pipeline-gate.py --selftest` | 0 | `19/19 checks passed` |
| typed generalized | `typed-pipeline-gate.py --selftest-generalized` | 0 | `16/16 checks passed` |
| argot | `argot-derivation-gate.py --selftest` | 0 | `21/21 checks passed` |
| replay | `replay-frozen.py --selftest` | 0 | `79/79 checks passed` |

## 2. What "byte-identical" does and does not assert

- **Asserts:** the two/three runs of the *same* command at the *same* revision
  produce identical stdout bytes and identical exit codes. A gate whose
  interface is stdout plus an exit code is deterministic exactly when those
  bytes repeat.
- **Does not assert:** that the output is *correct*, that a green entry should
  be green, or that a later revision reproduces these bytes. A gate edit moves
  the digest and requires a dated re-run — which is precisely what happened to
  the frozen generations this round (see `D20-replay-frozen.md` §2).

## 3. Limits

- **Three runs, not a soak.** Three consecutive runs catch flapping and
  hash-order nondeterminism; they do not prove determinism under concurrency or
  across machines.
- **The readings bind to the pins in `D17-typed-gate.md` §3.** A later edit to
  any pinned path invalidates them.
- **No entry was measured under a modified tree.** The teeth control (a planted
  violation) runs in a clone, never the lane worktree, so the deterministic
  readings above are the lane's own bytes.
