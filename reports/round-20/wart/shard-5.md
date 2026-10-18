# R20-O09 — shard 5/6: the green surface table (d2 / d3 / d4, gates, adapters, the runner)

- round 20, seat **R20-O05..O10**, claim **O**. Fragment 5 of 6.
- date 2026-10-18; the table was re-taken at `2026-10-18T13:12Z`, after every
  cascade row in shard 4 landed. Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  `export TMPDIR=$PWD/.scratch` before every scratch-writing command.
- canon: NON-CANON. Green here means the named command exited 0 (or the named
  documented exit); it is not a clearance and not a canon ruling.
- writes: this fragment (plus the artifacts shard 4 names).

## 1. The table

| # | command | observed | exit |
|---|---|---|---|
| 1 | `python3 tools/d2-typed-labels.py --check examples/culture-d2/typed-labels.d2.yml` | `examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic projection` | 0 |
| 2 | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | `examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic projection` | 0 |
| 3 | `python3 tools/d2-typed-labels.py --packet examples/culture-d3/packet.json --json` | documented refusal: `{"exit_code": 2, …, "code": "P-UNTERMINATED-FLOW", "detail": "content '{' is not a mapping line", …}` | 2 (as before) |
| 4 | `python3 tools/d2-typed-labels.py --selftest` | `selftest: 50/50 checks passed — …` | 0 |
| 5 | `python3 tools/gates/typed-pipeline-gate.py` | `summary: 16/16 legs passed` | 0 |
| 6 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 19/19 legs passed` | 0 |
| 7 | `python3 tools/assemble-d2-typed.py --selftest` | `selftest: 11/11 checks passed — …` | 0 |
| 8 | `python3 tools/assemble-d4-typed.py --selftest` | `selftest: 12/12 checks passed — …` (mirror no longer copies `examples/culture-d2`) | 0 |
| 9 | `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | `… byte-identical deterministic typed packet` | 0 |
| 10 | `python3 tools/gates/d4-typed-labels-check-gate.py` | `examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic projection` | 0 |
| 11 | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | `examples/culture-d4/packet.d4.yml: byte-identical deterministic assembly` | 0 |
| 12 | `python3 tools/check-gate-battery.py` | `summary {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}`; `baselines_found 18, pinned 18, coverage "9/9", gates_uncovered []`; `originals preserved true, modified 0, added 0, deleted 0` | 0 |
| 13 | `python3 reports/round-15/handoff/frozen-verify.py --baseline reports/round-20/wart/expected-v2-07-r20.json` | `frozen-v2: exit=0 fields=16/16 glossary=20/20 findings=0 claims=15/15 statuses={'supported': 8, 'unresolved': 2, 'partial': 5} links=50/50 packet_sha256=24f9dd39bdad…` | 0 |
| 14 | `python3 tools/d2-typed-labels.py --emit .scratch/o05/d2-rebuild.yml && cmp .scratch/o05/d2-rebuild.yml examples/culture-d2/typed-labels.d2.yml` | `cmp` clean, both `a3aa452cd5ae…` | 0 |
| 15 | `python3 reports/round-20/run-validation.py` | `claim O: PASS`; claim C PASS; claim D another seat's (missing v3 artifacts) | 1 (D open) |

Row 12's baseline counter moved 17 → 18 against the round-19 reading: the new
`r20-post` row (shard 4 §2). Nothing else in the battery moved.

## 2. What the round's counting command measured for claim O

From `reports/round-20/validation.json` `claims.O.measurement` (read at 13:12Z):

| field | reading |
|---|---|
| `gate_scan` | `summary: 19/19 legs passed` |
| `adapter_selftest` | `selftest: 12/12 checks passed` |
| `foreign_tree_copy_in_adapter` | `false` |
| `d2_byte_identical` | `true` |
| `wart_mirror.culture_d2_present` | `false` |
| `wart_mirror.d4_projection_check` / `d4_adapter_check` | exit 0 / exit 0 |
| `pins.expected_holds` | `projector_sha256` ok, `projection_sha256` ok, `packet_sha256` ok |
| `pins.typed_packet` | `packet_sha256` ok, `projection_sha256` ok, `adapter_sha256` ok |
| `pins.typed_pipelines` | every field ok |
| `runs` | every leg exit 0; `d3-projector-probe` exit 2 (the documented D3 refusal, informational) |
| `filed_bytes` | 897 filed files compared against the baseline revision, 0 failures |

The runner's own `wart_mirror` is a second, independent mirror (all `tools/*.py`
plus the reader gate plus `examples/culture-d4`), so the no-foreign-tree property
is measured by two different mirrors — the projector's selftest section 5 and the
round validator's.

## 3. One line that is **not** a regression, recorded so nobody re-reads it as one

`python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.typed.yml`
→ exit 1, "differs from the deterministic assembly". This is the correct answer:
that gate compares `tools/assemble-culture-d4.py`'s build of the **source**
packet against the path it is given, and the typed packet is the *adapter's*
output, not the assembler's (its own check is row 9, green). The declared input
is the source packet (row 11, green). Recorded because the wrong invocation
looks exactly like a red.

## 4. The D3 reading, in context

The projector cannot read the D3 packet: `examples/culture-d3/packet.json` starts
with `{` and the strict loader refuses JSON-shaped input by design
(`P-UNTERMINATED-FLOW`, exit 2, stable message, no traceback) — the same reading
as before the change (measured pre-change in this seat's scratch,
`stats {"fail": 1, "hold": 0, "labels": 0}` both times). The D3 family's typed
pipeline is served by its own tools, not by this projector; the claim's "d2/d3/d4
projector runs" therefore reads as: D2 green (rows 1, 5, 7, 14), D4 green (rows
2, 6, 8–11, 15), D3 an unchanged documented refusal (row 3).

## 5. Controls behind the table

| control | command | observed |
|---|---|---|
| every surface was re-run after the cascade, not before | all rows run at 13:12Z, after the last cascade edit (13:10Z) | as tabulated |
| the tree did not move while the table was taken | `python3 tools/check-gate-battery.py` `originals` block | `preserved true`, 30 files hashed before and after, 0 modified/added/deleted |
| the D4 legs are green *because of* the re-pin, not despite it | same command before the re-pin | `FAIL L1-profile: projection: pins a59990bbfe5a, live cbcf997f5f38`, exit 2 (shard 4 §6) |
| the D2 path is byte-identical, two ways | `--check` (row 1) and a fresh rebuild compared with `cmp` (row 14) | identical |

## 6. Limits

- Rows 6 and 11 read the **live** component tree (the adapters resolve `ROOT`
  from their own file); they are green for the bytes in the tree at 13:12Z.
- The battery verifies digests and pins; it never re-runs a baseline's verdict.
  Green there means "pinned", not "the verdict was re-observed".
- Row 15's claim D failure belongs to another seat's unfinished work (the v3
  handoff artifacts are not on disk yet); it is not attributable to this claim,
  and the runner names the missing dependencies in its receipt.
