# R18-O05 — The D4 path: identity verified against `assemble-culture-d4.py --check`

- round: 18 · shard: **O05** (impl, single writer of `tools/gates/typed-pipeline-gate.py`)
  · claim O `gate-generalization` (`reports/round-18/claims.json:8-14`).
- assignment (verbatim): "O R18-O03..O06 (impl x4, single writer owns the gate
  file): implement the generalization so the DEFAULT D2 path is byte-identical in
  behavior; the D4 path verifies against assemble-culture-d4.py --check output
  identity; fragments + integration evidence reports/round-18/gate/impl-{1..4}.md."
- date: 2026-10-18. Evidence window 10:20–11:2xZ. Gate revision
  `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617` (1349 lines),
  profile `tools/gates/typed-pipelines.json`
  `434e90509a1c5e25d639dfb8b6027ab5c8a6045340c9b81f46a5ecb3b04af004`.
- canon: NON-CANON engineering evidence. The D4 tree is a design drill; its holds
  are open design debt, never a clearance.
- writes: **this fragment only**; scratch under `.scratch/r18-o03/d4/**`
  (`export TMPDIR=$PWD/.scratch` before every scratch write). No commit, no push.
- **status: the identity leg is green on the delivered D4 bytes and agrees with the
  assembler's own `--check` in the positive and the tampered state; the full D4 run
  is blocked only on `tools/assemble-d4-typed.py`, which does not exist yet (a
  D-seat artifact).**

## 0. Verdict

1. `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
   resolves the D4 pipeline through the sha-pinned profile, prints the resolution
   line, and reports `ok L1-profile`, `ok L1-assembler`, `ok L1-expected-holds`,
   then `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` — exit 2 with
   the identity and expected-file legs green on the delivered bytes
   (`gate-d4-text3.out`, 11:1xZ).
2. The flag-declared form (`--assembler … --projection … --expected …`) reaches the
   same verdicts; the `--json` `resolved` block reports the profile, its digest and
   the flag set that was passed.
3. Behavioral equality with `assemble-culture-d4.py --check` was measured on
   isolated mirrors in both configurations:
   - **with the profile** in place, one appended comment line is refused by the
     profile's `packet` pin (`FAIL L1-profile: packet: pins e7ecd2045ef0, live
     cba8622d53b0`), and the same mirror's `--check` exits 1;
   - **without** the profile file (family/flags only), the same tamper is refused
     by the identity leg itself (`FAIL L1-assembler: packet bytes cba8622d53b0 are
     not tools/assemble-culture-d4.py's deterministic assembly (e7ecd2045ef0)`),
     and the same mirror's `--check` exits 1.
   Both mechanisms refuse with the same verdicts the assembler's own comparison
   produces, and the restored tree goes green again in both.
4. `--selftest-generalized` (14 checks) drives the whole mechanism over a fixture
   family in one temporary directory: a fully green declared run at exit 0, plus
   the tamper/drift/self-pin/missing-expected/stale-pin controls.

## 1. Subjects (measured, 10:20–11:20Z)

| path | sha256 | note |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617` | the generalized gate (this shard's write) |
| `tools/gates/typed-pipelines.json` | `434e90509a1c5e25d639dfb8b6027ab5c8a6045340c9b81f46a5ecb3b04af004` | profile `d4`, matched on `assembly.generator`; packet/assembler/projection/expected pinned, adapter pinned `null` until it lands |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | legacy packet; declares `assembly.generator: tools/assemble-culture-d4.py`, `assembly.assembler_sha256: 943f487b…` |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | the declared assembler; its `assemble()` is the build path the gate calls |
| `examples/culture-d4/typed-labels.d4.yml` | `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d` | the projection the profile pins |
| `examples/culture-d4/expected-holds.json` | `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98` | `schema kotodama-typed-pipeline-holds-v1`, `counts {hold:15, note:1, fail:0}`, 15 holds + 1 note |

## 2. The receipts

### 2.1 Flagless (`gate-d4-text3.out`, `gate-d4.json`)

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
declared pipeline: family d4; profile tools/gates/typed-pipelines.json (sha256 434e90509a1c);
assembler tools/assemble-culture-d4.py (sha256 943f487ba991); adapter tools/assemble-d4-typed.py (sha256 absent);
projection examples/culture-d4/typed-labels.d4.yml (sha256 a59990bbfe5a);
expected examples/culture-d4/expected-holds.json (sha256 09490a2756d1)
ok   L1-profile:
ok   L1-assembler:
ok   L1-expected-holds:
FAIL L1-build: adapter missing: tools/assemble-d4-typed.py
exit=2
```

The resolution line is printed on the exit-2 path as well, which is what the
validator's D leg reads (`resolution_line {assembler_named: true,
assembler_sha_named: true}`), and the `--json` `resolved` block carries
`profile`, `profile_file`, `profile_sha256`, and each resolved path.

### 2.2 Flag-declared (`gate-d4-flagged.json`)

```
$ python3 tools/gates/typed-pipeline-gate.py --json \
    --assembler tools/assemble-culture-d4.py \
    --projection examples/culture-d4/typed-labels.d4.yml \
    --expected examples/culture-d4/expected-holds.json \
    examples/culture-d4/packet.d4.yml
exit 2 — L1-profile ok, L1-assembler ok, L1-expected-holds ok,
         L1-build FAIL "adapter missing: tools/assemble-d4-typed.py"
         resolved.flags = ["assembler", "expected", "projection"]
```
The flags and the declarations agree; the flag form does not change the verdicts.

### 2.3 The assembler's own check

```
$ python3 tools/assemble-culture-d4.py --check
packet.d4.yml: byte-identical deterministic assembly
exit=0
```

### 2.4 Mirror controls (no delivered byte touched)

Mirrors were composed under `.scratch/r18-o03/d4/mirror{,2,3}/` (gate,
`assemble-culture-d4.py`, `assemble-d2.py`, `d2-typed-labels.py`, the five culture
gates, `examples/culture-d4/**`; mirror 2 additionally carries
`tools/gates/typed-pipelines.json`, mirror 3 does not).

| mirror | state | gate | assembler `--check` |
|---|---|---|---|
| 2 (with profile) | positive | exit 2 — `L1-profile` ok, `L1-assembler` ok, `L1-expected-holds` ok, `L1-build` adapter missing | exit 0 — byte-identical |
| 2 (with profile) | one comment line appended | exit 2 — `FAIL L1-profile: packet: pins e7ecd2045ef0, live cba8622d53b0 (examples/culture-d4/packet.d4.yml)` | exit 1 — differs |
| 3 (no profile, flags) | positive | exit 2 — `L1-assembler` ok, `L1-expected-holds` ok, `L1-build` adapter missing | (not run) |
| 3 (no profile, flags) | one comment line appended | exit 2 — `FAIL L1-assembler: packet bytes cba8622d53b0 are not tools/assemble-culture-d4.py's deterministic assembly (e7ecd2045ef0)` | exit 1 — differs |
| 2/3 | restored | green again on the identity legs | exit 0 |

The profile's pin leg and the identity leg are two independent refusals of the
same tamper; both match the assembler's own verdict, and neither ever accepts a
drifted packet.

### 2.5 Independently measured by other seats

Those receipts were taken against the earlier revision of this shard
(`286d6e82…`, before the profile channel landed), and their recorded legs are
still green — the later revision adds `L1-profile` and the resolution line above
the same checks:

- `reports/round-18/d4/scribe-1.md` row A3 (10:37Z): `ok L1-assembler`, `ok
  L1-expected-holds`, `FAIL L1-build: adapter missing …` on the delivered tree.
- `reports/round-18/gate/tests-3.md` (O13) rows C/A/A2/B: untouched mirror, forged
  assembler bytes, a forged **constant** self-pin (the case where the packet bytes
  match the build and the self-pin leg alone refuses), and a one-line stale packet
  — all exit 2 with the landed detail strings.
- `reports/round-18/d4/review-4.md` §29/§85: the same reading, naming the adapter
  as the single outstanding artifact.

## 3. `--selftest-generalized` (14/14, exit 0; `post2/selftest-generalized.out`)

Fixture: a tiny `culture-d9` family inside one temporary directory (fixture
assembler with its own `assemble()` and `--check`, one component, projection and
adapter stubs, the assembler's own packet, a committed expected set, and a typed
packet whose single routing row stays on channel). Controls:

| # | control | assertion |
|---|---|---|
| 1-2 | default resolution | `resolve_config` lands on all seven `D2_DEFAULTS` values and `generalized=False` for the D2 packet and the D2 typed packet |
| 3 | declaration resolution | a `typed_pipeline.assembler` declaration resolves family `d4` to `tools/assemble-culture-d4.py` and `examples/culture-d4/expected-holds.json` |
| 4 | fixture build | the fixture assembler built its packet |
| 5 | declared identity, positive | the typed fixture **grades green at exit 0** (identity, channel, holds, pins) |
| 6 | declared identity, legs | `L1-assembler` ok and `L4-pins` ok (all four declared pins re-verified against live bytes) |
| 7 | resolved block | `--json` reports the resolved assembler |
| 8 | determinism | two runs byte-identical |
| 9 | tamper | gate `L1-assembler` FAIL **and** the fixture's own `--check` exit 1 (equality) |
| 10 | assembler drift | identity leg breaks, exit 2 |
| 11 | self-pin | a stale declared `assembler_sha256` is refused ("self-pin broken") |
| 12 | restored tree | the identity leg agrees with `--check` again (`(True, "")`) |
| 13 | missing expected file | exit 2, `L1-expected-holds` names the missing file |
| 14 | stale declared pin | exit 2, `L4-pins` fires on an edited `adapter_sha256` |

## 4. What remains for the D4 end-to-end run (not this shard's write)

- `tools/assemble-d4-typed.py` — the D4 adapter (R17 brief §9.1; the design seat's
  `gate/design.md` §5.1 expects the module interface
  `build(packet_path, projection_path) → {exit, problems, inputs, payload, doc}`,
  which is the call the gate makes, the D2 idiom). Until it lands, `L1-build` is
  the only failing leg on the D4 path.
- `examples/culture-d4/packet.d4.typed.yml` — the adapter's product; the validator's
  D discovery requires it.
- Once both land, the D4 run reads: profile pins → identity → adapter build →
  channel differential over the moved rows → hold set equal to the delivered
  `expected-holds.json` (15 holds + 1 note) → the four re-verified pins.
- The profile's `adapter.sha256` is `null` on purpose (see `impl-4.md` §4.3);
  re-pin it at the first freeze after the adapter lands.

## 5. Compliance

Writes: this fragment (plus `impl-1/2/4.md`), scratch under `.scratch/r18-o03/**`,
and the two tool files (before/after digests in `impl-1.md` §5). No D4 artifact,
no filed receipt, and no earlier-round byte was written by this shard; the mirror
controls ran entirely inside `.scratch`. No commit, no push.
