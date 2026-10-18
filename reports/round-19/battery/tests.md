# Round-19 battery integration — controls and tests (R29-O01..O06)

- **Seat:** R29-O01..O06 (battery integration). **Date:** 2026-10-18. Commands run from the lane root
  with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` unless stated.
- **Artifact under test:** `tools/check-gate-battery.py`,
  `sha256 cd8c0ec291b6b986744ff132991abff717cbc085a86f095378189e15d6df13e5` (working tree,
  2026-10-18T12:37Z). Every reading below is bound to that digest; a later edit inherits none of it.
  (The intermediate 9-leg revision `83d9e3e5…` and its readings are recorded in `design.md` §3.)

## 1. The battery's own selftest

```text
$ python3 tools/check-gate-battery.py --selftest
…
SELFTEST OK 35/35 controls behaved as expected          # exit 0
```

35 controls, up from 29 at the declared baseline. The six added this round, as printed (transcript
`.scratch/r19-o01/selftest-final.txt`, 2026-10-18T12:37Z):

```text
control CTRL-D4-PRESTATE-7-GREEN: exit=0 outcome=pinned ids=-
control CTRL-D4-POSTSTATE-UNCOVERED: exit=2 outcome=pinned ids=BASELINE-GATE-UNCOVERED
control CTRL-D4-DEFAULT-9-OF-9: exit=0 outcome=pinned ids=-
control CTRL-D4-PRESTATE-REJECTS-D4: exit=2 outcome=no baseline,pinned ids=BASELINE-GATE-UNKNOWN
control CTRL-D4-REGISTRY: exit=0 outcome=- ids=-
control CTRL-D4-SURFACE: exit=0 outcome=- ids=-
```

Each carries an assertion beyond the exit/outcome/id triple, so a right answer for the wrong reason
fails:

| Control | Extra assertion | Why it is needed |
|---|---|---|
| `CTRL-D4-PRESTATE-7-GREEN` | `coverage == "7/7"` and `gates_uncovered == []` | exit 0 alone would also pass on an empty fixture |
| `CTRL-D4-POSTSTATE-UNCOVERED` | `gates_uncovered == list(D4_GATE_NAMES)` exactly, `coverage == "7/9"` | "some gate uncovered" is not "the D4 gates are the gap" |
| `CTRL-D4-DEFAULT-9-OF-9` | `coverage == "9/9"`, `uncovered == []`, `set(gates_covered) == set(REGISTERED_GATE_NAMES)` | proves the *default* argument, not a hand-passed set |
| `CTRL-D4-PRESTATE-REJECTS-D4` | `gates_covered == list(GATE_NAMES)` | pins the pre-state's covered set as exactly the seven |
| `CTRL-D4-REGISTRY` | nine distinct names; both D4 names present; disjoint from `GATE_NAMES`; both scripts exist | a registration naming a missing script is red |
| `CTRL-D4-SURFACE` | leg plan == the seven structural names, every leg mirror-rooted; the mirror set excludes the D4 names; registered set == `GATE_NAMES ∪ D4_GATE_NAMES`; snapshot covers all nine scripts | the surface is asserted as data, so a later edit that quietly adds a D4 leg to the mirror — a leg whose peer and packet do not exist there — fails here |

## 2. Pre-state vs post-state over the live tree

Transcript `.scratch/r19-o01/prestate-live.txt` (2026-10-18T12:37:54Z), loading the shipped module and
reading the *live* baseline roots twice:

| Gate set | `baseline_exit` | `coverage` | `gates_registered` | `gates_uncovered` | D4 rows |
|---|---|---|---|---|---|
| round-18 seven-name constant | 2 | `7/7` | 7 | `[]` | both `no baseline` (`BASELINE-GATE-UNKNOWN`) |
| round-19 registered nine | 0 | `9/9` | 9 | `[]` | both `pinned` |

Read the first row carefully: the pre-state configuration is red on today's tree and *still* reports
no uncovered gate, because the D4 rows are refused as unknown gates before coverage is counted. The
pre-state had no way to say "the D4 family is unmeasured" — that is the gap this round closes.

## 3. Pre-state default run, executed from its own source

Transcript `.scratch/r19-o01/prestate-default-run.txt` (2026-10-18T11:40:46Z). The round-18 source was
read from git, its `__file__` set to `tools/check-gate-battery.py` so it resolves the lane's live
paths exactly as the pre-state tool did, and executed as a module:

```text
$ git show e5718945a1ab0a0c3db955338d2cae77d68fd348:tools/check-gate-battery.py   # sha256 7aa898d6…
pre-state gate names (7 structural names, no D4)
pre-state 'd4' occurrences in source: 0
pre-state default run exit 2
  pass/fail/unevaluable 7 0 0
  gate ids [7 structural names]
  baseline summary {"baseline_exit": 2, "baselines_found": 17, "pinned": 15,
                    "readings": {"no baseline": 2, "pinned": 15}, "gates_uncovered": []}
```

Transcript `.scratch/r19-o01/prestate-r18-tree.txt` (2026-10-18T11:41:01Z) replays the same pre-state
source over a round-18-shaped root set (the standard root copied without the two D4 directories, plus
`tools/gates/frozen/` and `reports/round-9/baselines/`):

```text
  exit 0 pass 7 gate ids 7
  baseline summary {"baseline_exit": 0, "baselines_found": 15, "pinned": 15, "gates_uncovered": []}
```

That is the pre-state's green: 15 baselines pinned, no D4 baseline in existence, exit 0. The D4 family
was invisible, not measured-and-clean.

## 4. Default run after the change

```text
$ python3 tools/check-gate-battery.py                    # 2026-10-18T12:37Z
exit 0
summary    {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}
coverage   "9/9"   (gates_registered 9, gates_uncovered [])
baselines  baseline_exit 0, pinned 17, readings {"pinned": 17}
originals  {"files_hashed_before": 30, "files_hashed_after": 30, "preserved": true,
            "modified": 0, "added": 0, "deleted": 0}
legs       7 structural gates, all pass
findings   []
```

The D4 family is inside the battery's requirement surface (a missing D4 baseline is
`BASELINE-GATE-UNCOVERED`, exit 2) and both D4 baselines read `pinned` with their gate digests
matching live. What the run does *not* say is that the adapters executed — that is not this duty, and
the report does not imply it: `pass 7` and `coverage 9/9` are two counters naming two different
things, both printed.

## 5. Controls that must still fail (negative direction)

| Probe | Command | Expected / observed |
|---|---|---|
| tampered D4 baseline | copy the standard root to `.scratch/r19-o01/tamper/expected`, append one byte to `d4-typed-labels-check-gate/r19-pre/typed-labels.d4.yml`, then `python3 tools/check-gate-battery.py --baselines-root .scratch/r19-o01/tamper/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines` | **measured 2026-10-18T11:45Z**: exit 2, coverage `9/9`, readings `{"pinned": 16, "snapshot_tampered": 1}`, the tampered row reads `snapshot_tampered` / `BASELINE-TAMPERED`, its sibling D4 row still `pinned` (transcript `.scratch/r19-o01/tamper-drill.json`) |
| D4 gate revised | change `gate_sha256` in a copied `expected.json` to `0`×64 | `gate_revised`, exit 2 — the synthetic `CTRL-BASELINE-GATE-REVISED` control, unchanged and green in the 35/35 run |
| D4 gate uncovered | run with `--baselines-root` on a copy of the standard root with the D4 directories removed | `BASELINE-GATE-UNCOVERED` for both D4 gates, exit 2 (`CTRL-D4-POSTSTATE-UNCOVERED`, synthetic) |
| live edit during the run | `preservation_paths()` before/after diff | `GATE-BYTES-CHANGED`, exit 2 (path-set and byte-level) |

The D4 rows are read by the same code path as the seven structural rows — `verify_baseline_spec` is
unchanged by this round — so no new tamper class is introduced; the drill above is the end-to-end
check that the widened registration did not accidentally exempt them.

## 6. What these tests do not establish

- Every reading here is a point-in-time measurement of a live tree inside a 64-worker wave; re-run the
  command rather than quoting a line forward.
- The controls prove the battery's own dispatch, registration and classification. They do not prove
  any gate's verdict is correct, and `pinned` still means digests-and-pins-hold, never
  verdict-compared.
- Nothing here is evidence that the two D4 adapters run correctly over any artifact: they are not
  executed by this battery. Their runtime evidence is the round-18 frozen rows and the adapters' own
  `--selftest` where it exists.
