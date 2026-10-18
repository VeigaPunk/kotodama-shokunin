# R18-O06 — Integration evidence: the counting command read, the cascade, the handoff

- round: 18 · shard: **O06** (impl, single writer of `tools/gates/typed-pipeline-gate.py`
  and `tools/gates/typed-pipelines.json`) · claim O `gate-generalization`
  (`reports/round-18/claims.json:8-14`).
- assignment (verbatim): "O R18-O03..O06 (impl x4, single writer owns the gate
  file): implement the generalization so the DEFAULT D2 path is byte-identical in
  behavior; the D4 path verifies against assemble-culture-d4.py --check output
  identity; fragments + integration evidence reports/round-18/gate/impl-{1..4}.md."
- date: 2026-10-18. Evidence window 10:18–11:2xZ. Gate before
  `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d`, gate after
  `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617` (1349 lines).
- canon: NON-CANON engineering evidence.
- writes: **this fragment only**; scratch under `.scratch/r18-o03/**`
  (`export TMPDIR=$PWD/.scratch` before every scratch write; the frozen replays use
  `env -u TMPDIR`, because `tools/replay-frozen.py` refuses an in-repo mirror root
  by design). No commit, no push.
- **status: every leg this shard owns is green; the round's remaining D/O failures
  are all one missing artifact — `tools/assemble-d4-typed.py` (a D-seat write).**

## 0. Verdict

1. `python3 reports/round-18/run-validation.py --check` was read three times
   against the live tree (10:4xZ, 10:5xZ, 11:0xZ). The progression is the audit
   trail: claim C 0 failures throughout; claim D 5 → 2; claim O 4 → 2, and the
   three failures the D legs added at 10:44Z — "the D4 gate run names no declared
   assembler in its resolution line", "…names no assembler digest…", and
   `tools/gates/typed-pipelines.json` missing — are all cleared
   (`resolution_line {assembler_named: True, assembler_sha_named: True}`,
   `profile schema kotodama-typed-pipelines-v1, profiles 1, adapter
   tools/assemble-d4-typed.py`).
2. The two remaining claim-O failures and both remaining claim-D failures are the
   same single blocker: `tools/assemble-d4-typed.py` does not exist yet, so the
   D4 run stops at `FAIL L1-build: adapter missing` and the D4 typed packet is not
   on disk. Nothing on the gate side blocks them.
3. The pin ledger leg is satisfied: `d102fd1d…` (before) → `d96958b6…` (after) are
   named in this set and in the re-pin seats' frozen records; the round-11 file is
   byte-identical to the baseline; the derived round-18 manifest replays 11/11 on
   the live digest.
4. `tools/gates/typed-pipelines.json`'s `adapter.sha256` is deliberately `null`
   until the adapter lands; the profile's other four fields are pinned to live
   digests and are re-verified on every non-default run.

## 1. The counting command, read three times

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-18/run-validation.py --check > .scratch/r18-o03/regress/validation-check-N.json
```

| reading | claim C | claim D | claim O | note |
|---|---|---|---|---|
| 10:4xZ | 0 failures | 2 | 4 | O: D4 packet-run exit 2, flag-run exit 2, round-18 manifest 10/11 (the re-pin seat was mid-flight), no ledger record naming the gate's before/after digests |
| 10:5xZ | 0 | 5 | 2 | the D legs grew the resolution-line and profile-file requirements (validator updated 10:44Z); the manifest and ledger legs cleared |
| 11:0xZ | 0 | 2 | 2 | D: typed artifact missing + D4 gate run exit 2; O: D4 gate run exit 2 + flag-run exit 2 — **all four are the missing adapter** |

Readings 3's D/O failures, verbatim (excerpted):

```
claim D  F: D4 typed artifact not found under examples/culture-d4
claim D  F: the D4 gate run exited 2: declared pipeline: family d4; profile tools/gates/typed-pipelines.json
            (sha256 434e90509a1c); assembler tools/assemble-culture-d4.py (sha256 943f487ba991); …
            ok L1-profile / ok L1-assembler / ok L1-expected-holds / FAIL L1-build: adapter missing: tools/assemble-d4-typed.py
claim O  F: the generalized gate does not accept the D4 packet at exit 0: (same run)
claim O  F: the flag-declared assembler path is not green at exit 0
```

and the two legs that read green in the same run:

```
resolution_line: {"assembler_named": true, "assembler_sha_named": true,
                  "assembler_sha256": "943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2"}
profile:         {"profile_file": "tools/gates/typed-pipelines.json",
                  "schema": "kotodama-typed-pipelines-v1", "profiles": 1,
                  "adapter": "tools/assemble-d4-typed.py"}
```

## 2. The cascade (filed bytes untouched; new rows only)

| evidence | reading |
|---|---|
| `tools/gates/frozen/round-11/MANIFEST.tsv` | replayed with the new gate: **10 rows reproduced + row 2 `could-not-evaluate reason=gate_digest_mismatch`** — the filed pin separating the generations, exactly the class the round-17 design record names (`.scratch/r18-o03/regress/replay-round11-post.out`) |
| round-11 filed bytes | not edited by this shard; the validator's `round11_filed_pins` leg reads them byte-identical to the baseline |
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (re-pin seats) | row 2 pins the live gate `d96958b6…`; replay **11/11 reproduced** (`REPLAY OK`, 11:0xZ) |
| `tools/gates/frozen/round-18/MANIFEST.tsv` (D4 check gates) | replay **2/2 reproduced** |
| `reports/round-18/repin/**` (re-pin seats) | the round-9/round-16/v2-07 re-pins; the validator's ledger leg records the gate's before/after digests in `tools/gates/frozen/round-18/repin-d2/freeze.txt` and `run-receipt-repin.json` |

The first gate revision of this shard (`286d6e82…`) was pinned and superseded
inside the same round; its records stay filed and are named here so the sequence
is readable: `d102fd1d…` (baseline) → `286d6e82…` (resolver + identity leg) →
`d96958b6…` (profile channel + resolution line).

## 3. Regression set re-run at the final revision (11:1xZ)

| command | exit |
|---|---|
| `python3 tools/gates/typed-pipeline-gate.py` (default) | 0 — byte-identical to the pre-edit baseline |
| `… --json` | 0 — byte-identical |
| `… --selftest` | 0 — 12/12, byte-identical |
| `… examples/culture-d2/packet.d2.typed.yml` (frozen-row command) | 0 — `9a69985a…`, the round-11 filed pin |
| `… --selftest-generalized` | 0 — 14/14 |
| `python3 tools/check-gate-battery.py` / `--selftest` | 0 / 0 |
| `python3 tools/check-craft-exercise.py --selftest` | 0 |
| `python3 tools/check-evidence-coupling.py --selftest` | 0 |
| `python3 tools/assemble-d2-typed.py --selftest` | 0 |
| `python3 tools/assemble-d2.py --check`, `assemble-culture-d3.py --check`, `assemble-culture-d4.py --check` | 0, 0, 0 |
| `python3 tools/replay-frozen.py --selftest` | 0 |

Receipts: `.scratch/r18-o03/post2/**`, `.scratch/r18-o03/regress/**`.

## 4. What remains, and who owns it

1. **`tools/assemble-d4-typed.py`** (D seat, R17 brief §9.1; the design seat's
   `gate/design.md` §5.1 expects the module interface
   `build(packet_path, projection_path) → {exit, problems, inputs, payload, doc}`,
   which is the call this gate makes). When it lands, the D4 run reads:
   `L1-profile` → `L1-assembler` → `L1-expected-holds` → adapter build → the
   channel differential → the hold set equal to
   `examples/culture-d4/expected-holds.json` (15 holds + 1 note) → the four pins.
   Every leg before the adapter is already green on the delivered bytes, and
   `--selftest-generalized` control 5 exercises the whole chain green on a fixture
   of the same shape.
2. **`examples/culture-d4/packet.d4.typed.yml`** (the adapter's product; the
   validator's D discovery requires it).
3. **Re-pin the profile's adapter field** (`tools/gates/typed-pipelines.json`,
   `profiles[0].adapter.sha256`, currently `null`) at the first freeze after the
   adapter lands — one command, one date, a new value in that file (no filed
   receipt is edited).
4. **Re-run the counting command** after 1–3: the four remaining O/D failures are
   all downstream of the adapter. If the D4 packet or projection is revised again,
   the profile's `packet`/`projection` pins will refuse the run with
   `FAIL L1-profile` naming both digests — that is the intended behaviour, and the
   fix is a re-pin, not an edit of a filed receipt.
5. Cosmetic, for the D4 adapter owner: when the adapter reports its own
   `inputs.assembler_identity`, the D4 run will carry both `L1-assembler` (the
   gate's resolver leg) and the adapter's `L1-assembler_identity` arm. They check
   different things (the gate checks the packet against the declared assembler's
   build; the adapter checks its own wiring), so both are kept; a future revision
   may rename one if the duplication proves confusing.

## 5. File inventory of this shard

| path | sha256 / state |
|---|---|
| `tools/gates/typed-pipeline-gate.py` | `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617` (1349 lines) |
| `tools/gates/typed-pipelines.json` | `434e90509a1c5e25d639dfb8b6027ab5c8a6045340c9b81f46a5ecb3b04af004` |
| `reports/round-18/gate/impl-1.md` | this shard's design/code map + pin ledger |
| `reports/round-18/gate/impl-2.md` | byte-identity + regression battery |
| `reports/round-18/gate/impl-3.md` | the D4 identity leg and the `--check` equality controls |
| `reports/round-18/gate/impl-4.md` | this file |
| `.scratch/r18-o03/**` | gitignored scratch receipts (baseline, post, post2, d4, regress) |

## 6. Compliance

Writes: the two tool files above, `reports/round-18/gate/impl-{1..4}.md`, and
scratch under `.scratch/r18-o03/**`. No packet, projection, component, manifest,
baseline or earlier-round byte was written; no filed receipt was edited; the
re-pin cascade runs on new files written by the re-pin seats. No commit, no push.
