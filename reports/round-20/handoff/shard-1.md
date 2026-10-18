# shard-1 — v3 exercise surface and profiles (R20-D05..D12)

- topic: `tools/exercise-handoff-e2e.py` is extended to the profile surface
  `design.md` §6 specifies: v1 (default, the filed round-11 path), v2 (verify
  the filed round-15 surfaces), v3 (the D2/D3/D4 triple drill). This shard
  records the interface as implemented and the commands that measured it.
- date: 2026-10-18; lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

## 1. Interface as implemented

```
python3 tools/exercise-handoff-e2e.py                          # v1 path (round-11 baseline), default
python3 tools/exercise-handoff-e2e.py --profile v2             # v2 path (filed round-15 surfaces)
python3 tools/exercise-handoff-e2e.py --profile v3             # assemble -> links -> uncertainty -> gate -> v3 baseline
python3 tools/exercise-handoff-e2e.py --profile v3 --selftest  # positive + control matrix
python3 tools/exercise-handoff-e2e.py --profile v3 --root DIR --baseline PATH
```

- The default stays v1: `--profile` defaults to `v1`, the read set is v1's
  21 files and the baseline is `reports/round-11/handoff/expected.json`; no
  filed round-11 path was re-pointed.
- Exit codes: `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC`
  (uncertainty findings), `E2E-LINK` (link findings), `E2E-ARTIFACT`,
  `E2E-BASELINE`, `E2E-DATA`; no traceback on any path.
- Stable summary lines:
  - v1: `handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 packet_sha256=…`
  - v2: `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)`
  - v3: `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=…`

## 2. Measured (2026-10-18)

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --quiet                    # v1 path
python3 tools/exercise-handoff-e2e.py --profile v2               # v2 path
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet       # v3 path
python3 tools/exercise-handoff-e2e.py --selftest                 # v1 control matrix
python3 tools/exercise-handoff-e2e.py --profile v3 --selftest    # v3 control matrix
```

- v3: exit 0 — `fields=16/16 glossary=20/20 findings=0 links=105/105
  claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b`.
- v2: exit 0 — `claims=15 links=50/50`, two named drift rows (shard-8).
- v1: exit 1 — `E2E-DIGEST` naming `tools/d2-typed-labels.py` (the O seat's
  round-20 change moved a file the filed round-11 baseline pins; shard-8).
  The v1 code path itself is preserved verbatim in behaviour and passes its
  own control matrix on a fresh fixture.
- v1 selftest: `selftest: OK — positive run (exit 0, fields=16/16,
  glossary-entries=20, findings=0) plus 17 controls`.
- v3 selftest: `selftest: OK — positive run (exit 0, fields=16/16,
  glossary-entries=20, findings=0, links=105/105, claims=27,
  statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 28 controls`.

## 3. Footprint

- `tools/exercise-handoff-e2e.py` (single writer: this seat; v1 section
  preserved, v2 section added, v3 section added, `main()` dispatches by
  profile).
- No filed round-8..19 artifact was edited; `reports/round-15/handoff/**` is
  read-only in every profile.
