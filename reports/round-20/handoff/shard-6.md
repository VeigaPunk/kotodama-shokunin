# shard-6 — gate, twin, frozen v3 baseline (R20-D05..D12)

- topic: the frozen v3 record: the shape gate over an isolated copy, the
  machine twin judged by both harnesses, and the new baseline sited under
  `reports/round-20/handoff/`.
- date: 2026-10-18.

## 1. Freeze

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-20/handoff
```

Observed (freeze output):

```
frozen: 2026-10-18 by tools/exercise-handoff-e2e.py --profile v3
packet_sha256: e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b
twin_sha256:   58cb246081e03e351dc35c4c13ae7961ee9e046e569f0cc7081d76813de88628
gate: exit 0, fields=16/16, glossary-entries=20, findings=0
semantics: uncertainty exit 0, links 105/105 resolved
claims: 27 statuses 16/7/4; v2-subset ad35c860acf3b452…; alias leg landed
read set: 58 files; component digests 25/25; d4 pins 8/8
```

## 2. What the baseline pins (reports/round-20/handoff/expected.json)

- profile `kotodama-handoff-e2e/3`, packet `kotodama.handoff.d2d3d4-e2e`
  `3.0.0`, frozen 2026-10-18.
- packet + twin sha256; claim-id list (27); glossary entry ids (20);
  `inputs` over the full 58-file read set; per-field digests.
- uncertainty census (27; 16/7/4; exit 0; require-oq findings 0) and links
  (exit 0; findings 0; 105/105).
- `v2_subset_digest` (ad35c860…), `alias_state` (landed).
- `cross_refs`: contract digest `5f4c02bf…`, component digests 25/25, D4 pins
  8/8, gate scan + `gate_stdout_sha256`
  `7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685` (byte-
  equal to the v2 baseline's gate stdout digest — the gate is deterministic
  over both packets' scans), counts block.
- Siting: under `reports/round-20/handoff/`, never under
  `tools/gates/expected/**` or `tools/gates/frozen/**` (the battery reads
  every `expected.json` there); the battery is untouched.

## 3. Freeze outputs (all new files)

- `reports/round-20/handoff/expected.json` (the baseline),
  `packet.md` (the frozen packet, 27 claim rows / 88 edge rows / 20 glossary
  rows), `twin.json` (the machine twin), `run.log` (gate + semantic + D4 leg
  observations), `freeze.txt` (the tracked-value diff, including the re-freeze
  from the earlier same-round freeze).

## 4. Gate and harness commands (as recorded in the packet's validation)

- `python3 tools/gates/handoff-packet-check.py packet.md` (isolated copy,
  foreign cwd) → exit 0, `fields=16/16 glossary-entries=20 findings=0`.
- `python3 tools/harness/packet_uncertainty.py --packet twin.json
  --require-oq --json` → exit 0, claims 27, findings 0.
- `python3 tools/harness/packet_links.py --packet twin.json
  --repo-root <repo> --json` → exit 0, 105/105 resolved, findings 0.
