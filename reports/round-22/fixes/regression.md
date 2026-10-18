# R22-O12 — regression sweep

**Operational regression verdict: GREEN on the closing snapshot. Semantic handoff follow-up: OPEN.** Battery, craft, every runnable typed/assembly selftest and production check, handoff v2/v3, and current frozen successors pass. This is not round acceptance, canon clearance, or a claim that historical manifests all exit zero. The newly delivered v3 packet still copies obsolete D4 claim wording; see the final section before using the structural pass as semantic integration evidence.

## Isolation, revision and evidence

- Observation date: **2026-10-18**. All times below are **UTC−03:00**; each table row's time is its command start, not a claimed completion time.
- Before scratch-writing commands: `export TMPDIR=$PWD/.scratch; export PYTHONDONTWRITEBYTECODE=1` from the lane root.
- Closing driver: `python3 .scratch/r22-o12-regression/sweep.py closing`; clone/snapshot started **11:56:57**, matrix completed **11:57:33**. The real Git clone is `.scratch/r22-o12-regression/closing/repo`. Measured live working-tree bytes and manifest-referenced ignored receipts are copied into it; this is not an archive-only replay missing `run.log`.
- Binding: lane `HEAD=cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13`; declared baseline `46a03257ee75dd8f685a105e47da3f45a0154172`. The report measures the uncommitted integration overlay, not an assertion that HEAD contains those changes.
- Snapshot copies **1,894** inputs; manifest SHA-256 `e733fdcf340d4a1477a760a6a3127f08f8e553793b8a0c97e01b555faba87b0b`. The closing driver records **41** commands, **37** exit-zero results and **four** nonzero historical controls; no unexplained current-command failure. Command/date for these totals: closing driver above.
- Raw evidence: `.scratch/r22-o12-regression/closing/{snapshot,source-manifest,results}.json` and per-command `*.stdout.txt` / `*.stderr.txt`. Each command has argv, dated start/end, exit and stream hashes. The filed evidence is this report alone; no shared bookkeeping or source file is this seat's write.
- Ordinary replay temporary roots are outside the isolated clone but inside this lane. The peer-pinned replay requires the clone's `.scratch` and itself creates a nested disposable clone with sibling mirrors. No round validator was executed by this seat, in the live lane or otherwise.

## Battery and craft — all exit 0

| Command | Start | Measured result |
|---|---|---|
| `python3 tools/check-gate-battery.py` | 11:56:57 | seven structural selftests pass; fail 0 / unevaluable 0; **19/19** discovered baselines pinned; registered-gate baseline coverage **9/9**; originals preserved, 30 files hashed before/after, zero modified/added/deleted |
| `python3 tools/check-gate-battery.py --selftest` | 11:56:57 | **35/35** controls |
| `python3 tools/check-craft-exercise.py --selftest` | 11:56:57 | **10/10** tamper + **18/18** CLI cases |
| `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --report reports/supplement-opencode-1/32-craft-exercise.md` | 11:56:57 | all checks pass; audits 7, mechanical cases 11, derivations 9, approximate runner checks 37 |
| `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --counts` | 11:56:57 | audit census 7: five supported / two unresolved / zero contradicted; six full-text / one blocked |

Baseline pin/coverage counts are not verdict replay counts. The battery executes seven structural selftests, not nine: the two D4 adapters are baseline-covered separately and exercised below.

## All runnable typed / assembly selftests — all exit 0

| Command | Start | Checks passed |
|---|---|---|
| `python3 tools/assemble-d2.py --selftest` | 11:56:57 | **42/42** |
| `python3 tools/assemble-d2-typed.py --selftest` | 11:56:57 | **11/11** |
| `python3 tools/assemble-culture-d3.py --selftest` | 11:56:57 | **85/85** |
| `python3 tools/assemble-culture-d4.py --selftest` | 11:56:57 | **81/81** |
| `python3 tools/d2-typed-labels.py --selftest` | 11:56:57 | **163/163** |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 11:56:58 | **12/12** |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | 11:56:58 | **14/14** |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | 11:56:58 | **163/163**, delegates to the projector suite; not a second independent family-control inventory |
| `python3 tools/assemble-d4-typed.py --selftest` | 11:56:58 | **12/12**, including the D4-only mirror |

The combined projector suite includes the existing controls, malformed-alias rejection, and family-boundary controls: D2 fixture poison leaves D4 unchanged while D2 responds, local D4 rank mutations are observed, foreign ownership/citations refuse, valid D4 loan/form data survive, and D2 retains its exact baseline bytes. The assembly/gate suites pair clean rebuilds with stale projection, missing/duplicate/malformed data, dropped routing, tampered packets and stale pins. `d4-assembly-check-gate.py` has no selftest mode; its real packet check is used below rather than inventing a flag.

## Production typed / assembly checks — all exit 0

All byte-identity readings compare the delivered artifacts with their actual generators, not only imports or compilations.

| Command | Start | Result |
|---|---|---|
| `python3 tools/assemble-d2.py --check` | 11:56:57 | D2 assembly byte-identical |
| `python3 tools/assemble-d2-typed.py --check` | 11:56:57 | D2 typed packet byte-identical |
| `python3 tools/assemble-culture-d3.py --check` | 11:56:57 | `packet.json` and `packet.gates.yml` byte-identical |
| `python3 tools/assemble-culture-d4.py --check` | 11:56:57 | D4 assembly byte-identical |
| `python3 tools/d2-typed-labels.py --check` | 11:56:58 | D2 projection byte-identical |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 11:56:58 | D4 projection byte-identical |
| `python3 tools/gates/typed-pipeline-gate.py` | 11:56:58 | D2 **16/16** legs |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 11:56:58 | D4 **19/19** legs |
| `python3 tools/gates/d4-typed-labels-check-gate.py` | 11:56:58 | D4 projection byte-identical |
| `python3 tools/assemble-d4-typed.py --check` | 11:56:58 | D4 typed packet byte-identical |
| `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 11:56:58 | D4 assembly byte-identical |

## Handoff and supporting harnesses — all exit 0

| Command | Start | Result |
|---|---|---|
| `python3 tools/exercise-handoff-e2e.py --profile v2` | 11:56:58 | **15** claims; links **50/50**; shape **16/16**, glossary **20**, zero findings; original v2 packet/twin pins match |
| `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` | 11:56:58 | positive end-to-end run plus **39** controls; includes provenance drop/change/truncation negatives in both Markdown and twin and an alternate-root positive |
| `python3 tools/exercise-handoff-e2e.py --profile v3` | 11:56:59 | fields **16/16**, glossary **20/20**, findings 0, links **105/105**, claims **27**, statuses **16/7/4**, v2 subset equal, alias leg landed; **58** read-set inputs preserved |
| `python3 tools/check-evidence-coupling.py --selftest` | 11:56:58 | five positive / sixteen domain / four malformed / five frozen controls pass |
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 11:56:58 | zero findings |
| `python3 tools/harness/packet_links.py --selftest` | 11:56:58 | **38** controls |
| `python3 tools/harness/packet_uncertainty.py --selftest` | 11:56:58 | **19** controls |

The v2 run explicitly reports its existing named tool-digest allowances (`tools/d2-typed-labels.py`, `tools/harness/packet_links.py`); the links leg runs with `--no-digests`, and the digest leg rejects any finding outside that named set. This is not a claim that the historical v2 tool pins equal today's tools. The v3 default in the closing snapshot is **`reports/round-22/handoff/declared-in-r2/expected.json`**, not the obsolete round-20 baseline or the first round-22 generation. Packet SHA-256: `a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e`.

## Current frozen successors — green, with peer binding

Replay command for each manifest row: `python3 tools/replay-frozen.py <manifest> --json`. Dates are **2026-10-18**, as above.

| Manifest / command | Start | Result |
|---|---|---|
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | 11:57:00 | exit 0; **11/11** recorded verdicts reproduced |
| `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` | 11:57:00 | exit 0; **11/11** recorded verdicts reproduced |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 11:57:00 | exit 0; **3/3** reproduced: projection check, assembly check and full typed-pipeline row |
| `python3 reports/round-22/bleed/replay.py --require-live` | 11:56:59 | exit 0; **33** live-peer/snapshot pairs verified; restored pinned peers into a nested isolated clone; **3/3** reproduced, zero mismatch/unevaluable |
| `python3 tools/replay-frozen.py --selftest` | 11:56:59 | exit 0; **79/79** controls, including bad pins/paths, tampered input/output and expected-red reproduction |

The peer-bound replay is important: the generic adapter replay alone cannot prove its live projector/component peers still equal a named revision. Reproduction remains reproduction; even a reproduced red design verdict would not become a clean design. The twelve legitimate D4 form holds remain open.

## Historical negative controls — explicitly nonzero, never rewritten

These four commands account for **all** nonzero results in the closing matrix. They are diagnostic historical controls, not current successor failures. Each uses `python3 tools/replay-frozen.py <manifest> --json` on **2026-10-18**.

| Manifest | Start | Observed result |
|---|---|---|
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 11:56:59 | exit **1**; **1/2** reproduced, row 2 `replay_mismatch`, row 3 assembly reproduces. Old projection `a59990bb…` is not the new `60b526b0…` family-clean projection. |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | 11:56:59 | exit **2**; **10/11** reproduced; row 2 refuses obsolete typed-pipeline `gate_digest_mismatch` before launch. |
| `tools/gates/frozen/round-3/MANIFEST.tsv` | 11:57:00 | exit **2**; **0/7** reproduced; seven historical gate revisions refuse `gate_digest_mismatch` before launch. |
| `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 11:57:00 | exit **2**; **0/7** reproduced; the same seven obsolete gate pins refuse before launch. |

The new named historical disposition is `reports/round-22/fixes/r18-supersession.md`: it binds the R18→R20 transition to an immutable revision, not to the later R22 moving tree. The current R22 D4 successor above is a further generation, not an edit of that historical record. The D2 re-pins do not by themselves supersede the old D4 row. It would be false to summarize the original historical manifests as all green.

## Before/after controls and preservation

- **11:40:55 initial driver:** `python3 .scratch/r22-o12-regression/sweep.py initial` captured the in-flight alias/projector change. Battery/craft/typed/assembly checks pass, but production v3 and its selftest refuse the stale projector pin (`76536a924280…` versus measured `51bff2848d19…`). These nonzeros are preserved under `.scratch/r22-o12-regression/initial/`, not used as final passes.
- **11:50:54 candidate driver:** `python3 .scratch/r22-o12-regression/sweep.py integrated-candidate` captures the family-clean source and **163/163** projector suite plus passing v3 selftest. Production D4 gate refuses the intermediate expected-hold profile pin (`88c21ff3cd31…` versus `3826ba68d705…`, exit 2 / `L1-profile`); production v3 refuses the final projector/expected-holds baseline input changes (exit 1 / `E2E-DIGEST`). The required re-pin was not bypassed. The fresh closing driver then passes both actual production commands with the landed new pins.
- **Dependency wait:** the first manual 60-second checks and the one-minute watcher stayed within the operator's 20-minute bound. The watcher observed the new D4 manifest and verification receipt at **11:56:43**, then exited; no background task remains.
- **Closing preservation:** the closing driver compares every copied input before/after execution: **zero clone-input changes**, **zero source-input changes during the matrix**, and **zero changes among 1,156 historical report/frozen paths**. These are command-dated counts from `results.json`, not an assumption that a clone is faithful.
- **Filed baseline:** at **11:58:10**, `git ls-tree -rz 46a03257ee75dd8f685a105e47da3f45a0154172 -- reports/round-{8..21}` followed by per-path Git-blob recomputation checks **1,018** filed report paths against the declared baseline: **zero changed**. The earlier independent comparison at **11:45:30** agrees. Ignored receipts are runtime prerequisites, not asserted to have a committed Git baseline.
- No filed round-8–21 artifact, old frozen manifest, shared LOG/SCORECARD/SKILL, or source tool was edited by this seat. No commit or push.

Closing source bindings, read with `sha256sum <path>` in the closing clone on **2026-10-18**, and also pinned in its source manifest:

| Path | SHA-256 |
|---|---|
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `tools/exercise-handoff-e2e.py` | `c185500e173e1095c0d34f60a0a3a5e2bd11bfafbf5c52d7c7e9077fe8dae452` |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` |
| `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` |
| `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` |
| `tools/gates/typed-pipelines.json` | `396f4678133ad3223752c27d7153fdff06945abfa49137a307e10ef6e29b44d0` |
| `reports/round-22/handoff/declared-in-r2/expected.json` | `4879e7602efcbc57f134b0e1604d38ca54d837bcbf8407d1667ef9bf30e238b7` |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | `dc4d5be2d33b5791cbcd11afce163019d4d6222bdf1596ed10ec1de59abb7435` |

## Open semantic handoff finding — parent integration follow-up

**R22-O12-SEM-1: structural v3 passes while copied D4 claims remain stale.** Independently re-read after the closing sweep at **11:57**: `reports/round-22/handoff/declared-in-r2/packet.md:148-152` still describes 16 findings / 15 holds / one note, four conflicts, three quarantine handles and thirteen inherited unresolved rank items. Its `OQ-V3-05` at line 307 repeats that inherited debt as present in D4. The first `declared-in` generation has the same issue. The generator still selects the immutable round-20 `CLAIMS_MAP` (`tools/exercise-handoff-e2e.py:184`). This agrees with the re-pin owner's separate finding in `reports/round-22/bleed/repin.md:26-37`.

The independent delivered-byte census at **2026-10-18T11:54:18−03:00** used:

```bash
python3 -c 'import datetime,json,pathlib; p=json.loads(pathlib.Path("examples/culture-d4/typed-labels.d4.yml").read_text()); h=json.loads(pathlib.Path("examples/culture-d4/expected-holds.json").read_text()); print(json.dumps({"date":datetime.datetime.now().astimezone().isoformat(),"coverage":p["coverage"],"expected_counts":h["counts"]},indent=1))'
```

Measured actual values: **12** total/hold findings, **0** notes/fails, **0** rank unresolved items/quarantine/conflicts, **4** component/normalized/gate rank rules, **74** labels (56 native / 12 translated / 6 borrowed), and **6** reconciliation records. The six garment-form obligations remain represented by twelve record/slot holds. An earlier ad hoc census used a nonexistent nested `component_rows` key and raised `KeyError`; it was corrected to the delivered root `coverage` contract before any census was claimed.

**Required follow-up:** the assigned handoff/integration owner must issue a new D4 claim map and superseding packet/twin/baseline, bind the generator to it, and add a control comparing the current claim numbers/ownership with the actual projection rather than only resolving their links. Preserve historical round-20 claims, both existing round-22 generations, and the unchanged v2 carried subset. Re-run handoff v3 and the closing regression matrix after those source/baseline changes. This seat does not race that sole writer. The operational task's measured commands are green; **semantic integration and round admission are not certified by this report**.
