# R18-O13 — D4-path negatives: forged assembler and stale packet are rejected

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers) · shard:
  **O13** (tests ×4, claim O `gate-generalization`) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "O R18-O11..O14 (tests x4): … D4-path negatives
  (forged assembler pin rejected, stale packet rejected); selftest additions;
  reports/round-18/gate/tests-{1..4}.md."
- date: 2026-10-18. Evidence window 10:31–10:34Z, against the generalized gate
  as it landed (the file was still being written by the O seats during the
  window; every receipt records the gate sha it measured).
- canon: NON-CANON engineering evidence.
- writes: **this file only** plus gitignored scratch under `.scratch/r18-o11/`
  (`export TMPDIR=$PWD/.scratch` before every scratch-writing command). Every
  control runs in an isolated tar mirror under `.scratch/`; no filed byte is
  touched, no commit, no push.
- **status: COMPLETE — all four controls behave as required** (the typed-packet
  pin control is recorded as *absent*, not as passed; see §4).

## 1. What is measured

Claim O: "the assembler-identity leg accepts a declared assembler pin
(packet-declared or flag)" and, from the task brief, "D4-path negatives (forged
assembler pin rejected, stale packet rejected)". A gate that accepts a declared
assembler is only worth its salt if the declaration cannot be forged and if a
packet whose bytes are not that assembler's output is refused. This shard
measures the refusal side on the D4 path.

## 2. Method

Driver `.scratch/r18-o11/negatives.py <label>`: compose one tar mirror of the
lane (`.git`, `.scratch`, `out`, `__pycache__` excluded), then run the mirror's
own gate over the mirror's own D4 packet so the controls need **no CLI flags** —
the D4 pipeline resolves by family convention from the gate's ROOT
(`family_paths("d4")`: assembler `tools/assemble-culture-d4.py`, projection
`examples/culture-d4/typed-labels.d4.yml`, expected
`examples/culture-d4/expected-holds.json`). Receipts:
`.scratch/r18-o11/negatives-receipt-<label>.json`, raw stdout per control
`.scratch/r18-o11/neg-<label>-<name>.out`.

## 3. Receipts (2026-10-18, 10:31–10:34Z)

| control | mutation (mirror only) | exit | verdict line |
|---|---:|---|---|
| **C** untouched mirror | none | 2 | `ok L1-assembler`, `ok L1-expected-holds`, `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` — the identity and expected-file legs are green on the delivered D4 bytes; the run stops at the one artifact the D4 tree does not yet carry |
| **A** forged assembler bytes | `# r18-o11 forged assembler bytes` appended to `tools/assemble-culture-d4.py` | **2** | `FAIL L1-assembler: packet bytes e7ecd2045ef0 are not tools/assemble-culture-d4.py's deterministic assembly (9653de575277)` — the assembler's own build embeds its file digest, so a tampered assembler no longer reproduces the packet |
| **A2** forged self-pin | the mirror assembler patched so its build embeds a **constant** `assembly.assembler_sha256` (`be6d9c8f241d…`), then re-run to rebuild the mirror packet | **2** | `FAIL L1-assembler: assembler self-pin broken: packet pins be6d9c8f241d, live tools/assemble-culture-d4.py hashes e8942393ac94` — with the packet bytes *matching* the build, the **self-pin leg alone** is what rejects the forgery |
| **B** stale packet | one comment line appended to a copy at `examples/culture-d4/packet.d4.stale.yml` | **2** | `FAIL L1-assembler: packet bytes 5614ba50f180 are not tools/assemble-culture-d4.py's deterministic assembly (e7ecd2045ef0)` — drift of one line is refused, and the run does not reach L2/L3 |

Gate revision measured for these rows: sha256
`5b4501a9dd8c1dfb3c6bcd444a6ee50b97138fc37087093224b781fdfd5419c8`
(`negatives-receipt-probe2.json`; the file changed repeatedly during the window —
`2a08fb2d…`, `b4232690…`, `a2948ebb…`, `edfec5f3…`, `3897833101…`, `d4785d9a…` —
so the final re-run at the settled revision is §5).

Why A and A2 are different controls: in A the tamper changes the assembler's
*output*, so the packet/build comparison fires; in A2 the tamper is built to
leave the output equal to the packet while the file bytes diverge, so the
`assembly.assembler_sha256` pin is the only leg that can reject it. Both exit 2.

Also measured on the D2 side, for symmetry (this is the mechanism the D4 controls
mirror): `tools/gates/typed-pipeline-gate.py --selftest`'s hazard control 4 —
"adapter drift: the frozen packet's adapter pin breaks (exit 1)" — is green in
the baseline selftest (`tests-4.md` §3), i.e. the typed-packet pin leg still
rejects a drifted adapter exactly as before the generalization.

## 4. The typed-packet pin control (absent, recorded as absent)

`examples/culture-d4/packet.d4.typed.yml` does not exist in the tree at this
stamp (`ls` → no such file), so the frozen-typed-packet variant of the forged-pin
control could not run: a scratch copy of a typed packet whose
`assembly.adapter_sha256` / `assembly.assembler_sha256` cell is rewritten would
be the D4 analogue of the D2 selftest's hazard control 4. The driver reports it
as `D-typed-packet-forged-pin: {"status": "absent"}` and excludes it from the
pass count rather than counting it green. When that artifact lands, the control
is one command:

```sh
# in a mirror, with the typed packet present
cp examples/culture-d4/packet.d4.typed.yml examples/culture-d4/packet.d4.typed.forged.yml
# rewrite one pin cell to a wrong 64-hex digest, then:
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.forged.yml
# expect exit 1 (L4-pins) or exit 2 (L1-assembler self-pin), never 0
```

## 5. Final re-run at the settled revision

`.scratch/r18-o11/negatives.py final`, at gate sha256
`84dc177e79688e0ed7f323ead42233205b7df7c68183d434bd32a906d647bad4`
(receipt `.scratch/r18-o11/negatives-receipt-final.json`, `all_ok: true`):

| control | exit | verdict line (verbatim) |
|---|---:|---|
| **A** forged assembler bytes | 2 | `FAIL L1-assembler: packet bytes e7ecd2045ef0 are not tools/assemble-culture-d4.py's deterministic assembly (9…)` |
| **A2** forged self-pin | 2 | `FAIL L1-assembler: assembler self-pin broken: packet pins be6d9c8f241d, live tools/assemble-culture-d4.py hashes e8…` |
| **B** stale packet | 2 | `FAIL L1-assembler: packet bytes 5614ba50f180 are not tools/assemble-culture-d4.py's deterministic assembly (e7…)` |
| **C** untouched mirror | 2 | `ok L1-assembler`, `ok L1-expected-holds`, `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` |
| **D** typed-packet forged pin | — | `absent` (the typed packet has not landed; §4) — excluded from the pass count, never counted green |

Every required verdict is reproduced at the settled revision; the only red line
in the table is the *missing adapter*, which is the pre-existing gap named in
`tests-2.md` §4, not a negative-control failure. The flag path named in §6 was
re-verified in the same window: `--assembler` / `--projection` / `--expected`
were accepted by the CLI from revision `ea95e2a1…` onward (`--help`, 10:35Z).

## 6. What this does not say

- Exit 2 on a forged declaration is a **could-not-evaluate**, not a clearance:
  the gate refuses to grade a packet it cannot attribute. It says nothing about
  the D4 design content.
- These controls exercise the declared-assembler legs through the family
  convention. The flag path (`--assembler` / `--projection` / `--expected`) was
  exercised separately in `tests-2.md` §4; a control that bypasses resolution
  entirely would not be covered here.
