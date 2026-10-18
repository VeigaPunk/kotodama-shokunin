# Round-19 D4 baselines — index (claim O, R29-O07..O12)

- seat: the round-19 O-baselines group (six seats, R29-O07..O12) writing the two D4 baselines and their
  author / rerun / tamper fragments. Write scope: `tools/gates/expected/<gate>/r19-pre/` and this
  directory. No gate, fixture, battery, corpus, or filed-round-8..18 byte was written by these seats;
  nothing was committed (the orchestrator integrates once per round).
- date: 2026-10-18 (local -03:00). Lane revision at every measurement:
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` (`git rev-parse HEAD`, the round-19 declare commit).
  The round-19 declared `baseline_revision` `e5718945a1ab0a0c3db955338d2cae77d68fd348` grades the same
  bytes: `git diff --stat e571894..HEAD` lists only `reports/round-19/{claims,targets}.json` (+46), and
  `git diff --stat e571894..HEAD -- tools examples corpus` is empty (0 lines).
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (layout), §4
  (`expected.json` fields), §5 (freeze procedure), §6 (verify order, tamper semantics, class map).
  Self-test = capability, frozen run = measurement.

## 1. The two baselines

| gate | baseline root | gate_sha256 | inputs pinned | expected | run.log sha256 | expected.json sha256 |
|---|---|---|---|---|---|---|
| `d4-typed-labels-check-gate` | `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | 6 | exit 0, class clean, findings `[]` | `3aa553930235d77bee021c044fdf4d626ab2389012c751cc8d5ad00d8cb7599a` | `93b84da0cbd3b2a8531319555c9848c0fb85a79e675a4fc8768096e2b22f776a` |
| `d4-assembly-check-gate` | `tools/gates/expected/d4-assembly-check-gate/r19-pre/` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | 16 | exit 0, class clean, findings `[]` | `5f14c09a0128dbed113877fe85b4ce72f0cccc4b5b46c126263c9137a00bdfb6` | `fb59f03d6e32d8d664ba513dda2d671606032ebc7e58d577fa06957d35c0fc30` |

Both `expected.json` sha256 values above are the values the round-19 validator itself computed
(`reports/round-19/run-validation.py --check` → `input_sha256`), i.e. the filed bytes, not a re-hash
of a working copy.

Each baseline directory holds: the graded snapshot (role-named at top level), an `expected.json` digest
pin, `run.log` (the observed stdout verbatim), `freeze.txt`, and byte copies of **every** file the gate
reads, at the gate's own relative path inside the baseline (`examples/…`, `tools/…`).

## 2. Why the input maps are larger than a legacy packet baseline

Both D4 gates are thin read-only adapters: `d4-typed-labels-check-gate.py` wraps
`tools/d2-typed-labels.py --check`, and `d4-assembly-check-gate.py` wraps
`tools/assemble-culture-d4.py` (loaded with `runpy`). The verdict therefore depends on bytes the
adapter itself never names, so `gate_sha256` alone would not pin the run. The read sets were
**measured**, not assumed, with a `sys.addaudithook("open")` trace over each graded command (scratch
script, not committed):

- typed-labels: the projection (`examples/culture-d4/typed-labels.d4.yml`), the packet
  (`examples/culture-d4/packet.d4.yml`), the peer tool, the frozen reader
  (`tools/gates/costume-era-consistency-gate.py`), and two D2 component files it consults
  (`examples/culture-d2/components/11-costumes.yml`, `12-rank-rules.yml`) — 6 entries.
- assembly: the packet, the 12 D4 component files, `tools/assemble-culture-d4.py`,
  `tools/assemble-d2.py`, and the frozen reader — 16 entries.

Every pinned copy equals its pin **and** the live file it was copied from: 22/22 measured
(`copy == live == pin`). Both gates' stdout was stable over three reruns and equal to `run.log`.

## 3. Battery reading (the lane's own validator, default roots)

`python3 tools/check-gate-battery.py`, 2026-10-18, after the sibling round-19 battery extension
(`tools/check-gate-battery.py`, modified in the worktree by that seat) registered the two D4 adapters
for baseline discovery:

- `baselines.summary`: `coverage "9/9"`, `baselines_found 17`, `pinned 17`, `unevaluable 0`,
  `readings {"pinned": 17}`, `baseline_exit 0`.
- measured 08:36 the default run exited 0 (`summary.pass 7`). Re-measured **2026-10-18T08:40**, while the
  sibling O-battery seat was mid-edit on `tools/check-gate-battery.py`, the default run exited 2 with
  `summary {"pass": 8, "fail": 0, "unevaluable": 1}` and both D4 adapters present in `gates`; the one
  unevaluable gate is `d4-assembly-check-gate.py --selftest`. The **baseline duty stayed green in both
  readings** (coverage "9/9", pinned 17, unevaluable 0). The gate-selftest numbers are quoted with their
  timestamp and must be re-read after that seat lands.
- this baseline pair reads `pinned`, `inputs_checked` 6 and 16, `gate_sha256 match`,
  `stdout_pin match`, `findings []`.
- `python3 tools/check-gate-battery.py --selftest` → `SELFTEST OK 29/29 controls behaved as expected`,
  exit 0.

## 4. Controls — full class map, every reading exit 2 where the standard says so

| control | action (on copies only) | reading | exit |
|---|---|---|---|
| positive | untouched baseline pair, default roots | `pinned` ×17 | 0 |
| snapshot tamper | one comment line appended to each graded snapshot in a copied baseline root, read with `--baselines-root` | `snapshot_tampered`, `BASELINE-TAMPERED` for both | 2 |
| gate revision | gate copies + one appended comment, read through the committed validator with a mirror `gates_dir` | `gate_revised`, `BASELINE-GATE-REVISED` for both | 2 |
| legacy shape | `inputs` emptied in both copies | `unpinned (legacy)`, `BASELINE-UNPINNED` for both | 2 |
| drift verdict | snapshot copy edited, gate re-run | exit 1 (both gates) | 1 |
| component drift (assembly) | one component file edited, committed packet re-run | exit 1 while the packet's own digest is unchanged | 1 |
| could-not-evaluate | assembly gate with a missing input path | `assembly error: …`, exit 2 | 2 |
| usage | `--help` / extra path argument | exit 2 | 2 |

## 5. Dependency status the orchestrator must settle (reported, not absorbed)

Measured 2026-10-18 with `python3 reports/round-19/run-validation.py --check` (exit 1). The **baseline
leg (O3) is green**: both D4 `expected.json` are discovered under `tools/gates/expected/`, their
`gate_sha256` pins match the live adapters, and every `inputs` key resolves to a byte-identical copy
inside the baseline — no `D4/standard baseline pin broken` and no missing-baseline failure is reported.

Two O legs outside this shard's write scope are still open at the 08:40 measurement (both belong to the
round-19 O-battery seats — `tools/gates/*.py`, `tools/check-gate-battery.py`):

1. the battery's gate-selftest duty now runs the nine registered gates (both D4 adapter ids appear in
   `gates`) but reads `pass 8 / unevaluable 1 / exit 2`: the unevaluable gate is
   `d4-assembly-check-gate.py --selftest`, which exits 2 (`assembly error: … '--selftest'`). The
   validator wants `summary.pass == 9` and battery exit 0. The typed-labels adapter reads 39/39 exit 0
   only because `--check --selftest` falls through to the peer's own selftest mode via argparse's
   optional-argument handling; that is a property of the peer's CLI, not a selftest the adapter
   implements.
2. at the same moment the battery's own `--selftest` was mid-edit and not green (it printed
   `SELFTEST OK 34/34` while the validator read `exit None`), so that reading must be re-taken by that
   seat before the round's O claim is counted.

No gate byte was touched by the baseline seats: `git hash-object` equals `git rev-parse HEAD:<path>` for
both adapters. The only trees these seats wrote are `tools/gates/expected/d4-*/r19-pre/` and this
directory.

## 6. Registry rows (draft for the round-19 registry scribe — do not treat as landed)

| field | `d4-typed-labels-check-gate` | `d4-assembly-check-gate` |
|---|---|---|
| class | gate (exit 1 on drift; a probe would not) | gate (exit 1 on drift) |
| entry command | `python3 tools/gates/d4-typed-labels-check-gate.py <projection.yml>` | `python3 tools/gates/d4-assembly-check-gate.py <packet.yml>` |
| capability evidence | wrapped peer: `python3 tools/d2-typed-labels.py --selftest` → 39/39 exit 0 | wrapped peer: `python3 tools/assemble-culture-d4.py --selftest` → 81/81 exit 0 |
| frozen baseline | `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` (`93b84da0…`) | `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json` (`fb59f03d…`) |
| verdict map | 0 clean / 1 drift / 2 could-not-evaluate (usage error; broken live packet) | 0 clean / 1 drift / 2 could-not-evaluate (usage error, missing input, assembler error) |
| pin coverage | `gate_sha256` + 6 input digests + advisory `stdout_sha256` | `gate_sha256` + 16 input digests + advisory `stdout_sha256` |
| drift readings | digest differs → `snapshot_tampered`; gate digest differs → `gate_revised` (both exit 2) | same |

## 7. Limits

- **Integrity, not truth.** Both frozen runs exit 0 on NON-CANON artifacts. Exit 0 asserts byte-identity
  of a projection / assembly, never a design PASS, never a canon ruling.
- **Live-tree reads.** Both adapters read their packet / component tree from the live repo; the baseline
  pins those bytes by copy, so a later live edit is caught by the pin recomputation and the re-run
  receipt, not by the battery's digest step alone (that step compares the copy to the pin).
- **`run.log` is gitignored** (`.gitignore:3:*.log`): the orchestrator must `git add -f` both `run.log`
  files or the baselines land without their verbatim stdout.
- Round 18 recorded the same gate/input pairs in `tools/gates/frozen/round-18/MANIFEST.tsv` (a
  replay-frozen manifest, not a battery-discovered `expected.json`); those bytes are untouched here.
