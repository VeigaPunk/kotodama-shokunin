# R11-D15 — test interop-d3: d3 path untouched and green

Shard: DEPTH R11-D15 (test interop with the d3 path). Axis: depth.
Measured 2026-10-17T22:01–22:03Z at HEAD `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`,
round baseline `94ca098b8ab03be52ec80f6925538e5e2c0ed327`, Python 3.14.7,
`TMPDIR=$PWD/.scratch`. Every command below was re-run by this shard; stdout
hashes are sha256 of raw stdout, a method calibrated against
`reports/round-10/drift/ledger.json` (raw-stdout hashing reproduces its
recorded `output_sha256` values 1:1).

## 1. Untouched — d3 path byte-identical to baseline and to the frozen pin set

- `git diff --stat 94ca098b..HEAD -- tools/ examples/` → empty output (no
  changes to either tree in the commit range).
- `git status --porcelain -- tools/ examples/` → empty at 22:03:36Z (other
  round-11 workers were concurrently modifying only `reports/**`).
- Disk digests at 22:01:30Z (`sha256sum`) against the frozen r9-pre manifest
  `tools/gates/frozen/handoff-packet-check/r9-pre/packet.md:66-68` (frozen
  2026-10-17T17:49:02-03:00):

| artifact | frozen digest (manifest) | current disk | match |
|---|---|---|---|
| `tools/assemble-culture-d3.py` (A-TOOL-ASSEMBLE) | `ba8d19d5…d17f014` | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` | yes |
| `tools/check-evidence-coupling.py` (A-TOOL-GUARD) | `849494b0…b2197e` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` | yes |
| `tools/assemble-d2.py` (A-SERIALIZER) | `8ea6bdde…c8655d` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` | yes |
| `examples/culture-d3/packet.json` (A-PACKET) | `bdf635ce…af4829` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` | yes |
| `examples/culture-d3/packet.gates.yml` (A-GATES) | `306bcac7…4c70425` | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` | yes |
| `examples/culture-d3/expected.json` (A-FROZEN) | `74496aa8…df5080` | `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` | superseded-since-freeze (see note) |

The four `examples/culture-d3/components/*.json` need no separate digest row:
`--check` re-assembles from them and compares bytes (row 115 below).

Note on the A-FROZEN row: the r9-pre freeze (17:49:02-03:00) recorded
`74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` for
`expected.json`, but that revision was never committed (`git cat-file -e`
→ NO_BLOB); the committed revision is `562b76cb…` (last changed in `9dc18ec`,
round-9, 18:17:00-03:00, unchanged through baseline `94ca098b`). The frozen
baseline replays its own `packet.md` copy, so this text digest is a historical
record, not a live pin — the live `--frozen` run (row 148) reads the `562b76cb…`
file and is green against the current packet.

## 2. Green — 7/7 d3 ledger rows re-run 1:1, hash-stable

Ledger: `reports/round-10/drift/ledger.json` (rows 115, 135, 136, 148, 159,
160, 191 — the complete set of d3-path rows in the 192-row ledger). All
re-runs exited as recorded and produced byte-identical stdout:

| row | command (`python3 …`) | ledger `output_sha256` | re-run sha256 | exit | verdict |
|---|---|---|---|---|---|
| 115 | `tools/assemble-culture-d3.py --check` | `e20620fa…b560a` | `e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a` | 0 | stable |
| 159 | `tools/assemble-culture-d3.py --check` (same) | `e20620fa…b560a` | same | 0 | stable |
| 135 | `tools/check-evidence-coupling.py examples/culture-d3/packet.json` | `e282a068…3669d` | `e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d` | 0 | stable |
| 148 | `tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | `e282a068…3669d` | same | 0 | stable |
| 136 | `tools/check-evidence-coupling.py --selftest` | `cf62bc50…380ce` | `cf62bc50e303b793b6b930c83a5ddd7d462c39cc39fef133385db830c1d380ce` | 0 | stable |
| 160 | `tools/check-evidence-coupling.py --selftest` (same) | `cf62bc50…380ce` | same | 0 | stable |
| 191 | `tools/assemble-culture-d3.py --selftest` | `91a06539…eac2b` | `91a0653948d48a10f6bd84af7adb3dd4cda3b25e8a15a77a3bf2cd92a4deac2b` | 0 | stable |

Key readings:

- `assemble-culture-d3.py --check` prints
  `packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly` (exit 0).
- `check-evidence-coupling.py --selftest` prints a JSON receipt ending
  `"note": "all committed-input selftest cases passed"` with 16/16 domain
  controls, 5/5 positive, 4/4 malformed, 5/5 frozen checks.
- `assemble-culture-d3.py --selftest` prints
  `selftest: 85/85 checks passed — … real naming gate (CROSS-HOLD, no PHON/DERIV FAIL) and real costume gate (R-01 note, no R-02) run read-only; no file outside the temporary directory touched` (exit 0).
- `check-evidence-coupling.py examples/culture-d3/packet.json` (plain and
  `--frozen`) exits 0 with `"findings": []`, `"counts": {"total": 0}`.

Drift disposition: none — 7/7 stable, zero dispositions required.

## 3. Interop probes — what breaks the d3 path (isolated byte-copy tree)

Method: `tar` copy of the repo (excl. `.git`, `.scratch`, `__pycache__`) into
`.scratch/d15/interop-sim/`, probes applied only there. Pristine copy re-ran
`--check` exit 0 first, so the copy is representative.

The d3 packet embeds `serializer_sha256` — the sha256 of the whole file
`tools/assemble-d2.py` — at `examples/culture-d3/packet.json:199` (written by
`tools/assemble-culture-d3.py:391-392`; serializer loaded read-only via
`runpy.run_path`, line 144). This is the coupling point to the round-11 D2
wiring, which must edit that file.

- **Probe A — comment-only byte change** (append one `#` line to
  `tools/assemble-d2.py`; digest `8ea6bdde…` → `c6197356…`):
  `assemble-culture-d3.py --check` → **exit 1**,
  stderr `examples/culture-d3/packet.json differs from deterministic assembly`.
  Regenerating in-process and diffing against the committed packet shows the
  difference is a single line, `serializer_sha256` (line 199); `packet.gates.yml`
  stays byte-identical. So even a whitespace/comment edit to the serializer
  file reds the d3 check.
- **Probe B — behavioral serializer change** (indent step `indent + 2` →
  `indent + 4` in `yaml_lines`): `--check` → exit 1 naming **both**
  `packet.json` and `packet.gates.yml`; but `assemble-culture-d3.py --selftest`
  still exits 0 at 85/85 — the selftest builds fixtures from its own copy of
  the serializer and cannot detect cross-repo serializer drift. Only
  `--check` catches it.
- **Probe C — serializer absent** (`mv tools/assemble-d2.py` away):
  `--check` → **exit 2**, `assembly error: yaml serializer not found: tools/assemble-d2.py` (fail-closed, no traceback).
- **Probe D — mechanical re-pin chain.** Bumping only `serializer_sha256`
  (regenerated packet digest `bdf635ce…` → `853df26a…`) and overwriting only
  `examples/culture-d3/packet.json`: plain coupling check exit 0; live handoff
  gate `tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md`
  exit 0 (`INFO scan: fields=16/16 glossary-entries=20 findings=0`); but
  `check-evidence-coupling.py … --frozen examples/culture-d3/expected.json`
  → **exit 2, D3-SNAPSHOT ×2**: `manifest digest mismatch for
  'examples/culture-d3/packet.json': declared bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829, actual 853df26aa8eb1e1b55b33186411a5df1882938e8589153778f9dd8ecfbea454f`.
  `examples/culture-d3/expected.json` is a second committed pin of the packet
  bytes, so a re-pin cannot stop at `packet.json`.

Insulation confirmed — same sim, after the Probe A edit: the coupling guard
reads only packet/closed-ledger content — its closed ledger paths are the
round-6 corpus files `corpus/lessons/round-6-sources/{03,05,09,13}.json`
(`tools/check-evidence-coupling.py:115-143`) — and stays exit 0, while the
gate battery (three-root invocation) stays exit 0, pass 7.

Battery receipts on the real repo (this shard, 22:05Z, TMPDIR set): the
committed-default invocation reads **exit 2** with
`gates_uncovered ['myth-consistency-gate.py', 'naming-collision-gate.py']`
while all 7 gate selftests individually pass; the three-root invocation
(`--baselines-root tools/gates/expected --baselines-root tools/gates/frozen
--baselines-root reports/round-9/baselines`) reads **exit 0**, pass 7, fail 0,
unevaluable 0. That default-invocation exit 2 is the already-registered
round-9 discovery defect (`reports/round-9/baselines/registry.md` §5 item 6),
not d3-specific; the three-root invocation is the green reading in both the
clean repo and the probe sim.

## 4. Consequence for the round-11 D2 wiring (reported, not decided)

Because `serializer_sha256` is a whole-file digest:

1. **Any byte change to `tools/assemble-d2.py` turns d3 `--check` red** (Probe
   A), i.e., it breaks this shard's "d3 untouched and green" reading, however
   functionally inert the change.
2. Therefore the D2 typed-pipeline wiring can keep the target "d3 untouched"
   only if `tools/assemble-d2.py` stays byte-frozen at
   `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` — e.g.
   the adapter lives in a new module and imports `yaml_lines` from the frozen
   file — with the constraint that the loader runs the whole module
   (`runpy.run_path`), so module level must stay stdlib-only and side-effect
   free, and `yaml_lines` must stay a module-level callable.
3. Otherwise the alternative is an explicit amendment of the target to allow
   re-pinning d3 bytes, and the re-pin chain is `packet.json` **and**
   `examples/culture-d3/expected.json` (Probe D, both gate-enforced), plus the
   text digest references in `examples/culture-d3/handoff.md`,
   `examples/culture-d3/README.md`, and the frozen r9-pre manifest's A-FROZEN
   row — the r9-pre A-FROZEN digest was already superseded once (17:49 freeze
   → 18:17 commit) without breaking the frozen replay or the battery, so the
   text references are historical records, not live pins; the two JSON pins
   are the enforcement. This shard reports the chain; the decision is the
   orchestrator's, since it is a target-scope call.
4. Timing caveat: at measurement time the D2 wiring had **not** landed
   (`tools/` byte-identical to baseline). Re-run §2 as a gate immediately
   after the wiring commit; the pins in §1 are the ones it must not move.

## 5. Re-run recipe

```
export TMPDIR=$PWD/.scratch
sha256sum tools/assemble-culture-d3.py tools/check-evidence-coupling.py \
  tools/assemble-d2.py examples/culture-d3/packet.json \
  examples/culture-d3/packet.gates.yml examples/culture-d3/expected.json
python3 tools/assemble-culture-d3.py --check
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
  --frozen examples/culture-d3/expected.json
python3 tools/check-evidence-coupling.py --selftest
python3 tools/assemble-culture-d3.py --selftest
```

Expected: digests as in §1; check exit 0 with the byte-identical line; coupling
exit 0 findings []; selftests 16/16+5/4/5 checks and 85/85. Probe artifacts
(including the interop-sim tree) stayed under `.scratch/d15/` (untracked).

## 6. Not claimed

- Not a claim that the D2 wiring is complete or correct — only that, as of
  22:01–22:03Z, it had not touched the d3 path and that path was green.
- Not a canon, acceptance, or clearance reading: the d3 selftest's CROSS-HOLD
  and R-01 are the declared expected legacy outcomes.
- The probe tree is a byte copy; probes were never applied to tracked files
  (post-run `git status` shows only `reports/**` concurrent worker edits).
