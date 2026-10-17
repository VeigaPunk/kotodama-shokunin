# Round-9 gate & harness registry (R9-O17)

- seat: R9-O17 registry scribe. This file is the seat's only write; no gate,
  fixture, battery, baseline or corpus byte was written by it.
- date: 2026-10-17. Measurement clock: `2026-10-17T20:48:52Z` (UTC) unless a
  row names its own timestamp; local time is UTC-03:00.
- lane revision at measurement: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (`git rev-parse HEAD`). The round's declared `baseline_revision` is
  `e1694bad6ac96aca45a11ca5746582b275929355` = `e1694ba` (HEAD~1).
  Cross-revision sweep (2026-10-17): `git diff --stat e1694ba..HEAD` →
  only `reports/round-9/claims.json` (34 +) and `reports/round-9/targets.json`
  (125 +), 159 insertions, 0 deletions; `git diff --stat e1694ba..HEAD --
  tools/gates examples tools` → empty. Every script byte named below is
  therefore identical under both revisions. Measured, not assumed.
- measured where: an isolated mirror `<repo>/.scratch/r9o17/` (`cp -r
  tools/gates …`; never the live tree). `/tmp` was unusable: `df -i /tmp` →
  `1048576 1048576 0 100%` (inode-exhausted); `mkdir /tmp/r9o17` → `No space
  left on device`. Scratch is untracked and disposable.
- what this file is: the two-evidences bookkeeping surface for round 9 — for
  every registered gate and harness: name, kind, entry command, verdict map,
  self-test spelling, pinned-value path, write scope, owner. It records where
  the round-9 `expected.json` baselines landed; it does not bless any gate,
  run, or design.

## 1. Sources this registry reproduces

- `corpus/knowledge/verification/gate-frozen-run-standard.md` — §3 baseline
  directory shape (`tools/gates/frozen/<gate-name>/<baseline-id>/`), §4
  `expected.json` required fields (`schema`, `gate`, `gate_sha256`,
  `revision`, `frozen_at`, `frozen_by`, `inputs`, `expected.exit`,
  `expected.class`, `expected.findings`, optional `stdout_sha256`), §5 freeze
  procedure, §6 verify procedure and class map (`match` / `failed` /
  `snapshot_tampered` exit 2 / `gate_revised` exit 2 / `unpinned (legacy)`
  exit 2 / `no baseline` exit 2), §11 contested-scope stop rule.
- `SKILL.md` §Gates and probes (`SKILL.md:164`; legacy table header
  `SKILL.md:181`, drill table header `SKILL.md:248`) — the lane's existing
  registry home whose rows this file re-measures and extends.
- Counting and probe commands, verbatim, all 2026-10-17 in the mirror
  `<repo>/.scratch/r9o17/` unless noted. Every count in this file is
  re-runnable from the lane root; raw receipts from this seat sit in that
  scratch directory (`transcript.txt` selftest spellings and exits,
  `counts.txt` finding-line/ID/set-equality counts, `runs.txt` fixture-run
  verdicts, `battery.json`/`battery3.json` battery reports,
  `gate_sha256.txt`/`fixture_sha256.txt` digests, `rv*.out|err` runner runs,
  `poll.log` the baseline-landing sweep). The scratch tree is untracked
  disposable evidence, not a deliverable:
  - selftest spellings: `for s in --selftest --self-test; do python3
    gates/<gate>.py $s; echo $?; done`
  - fixture verdicts and ID sets: `python3 gates/<gate>.py
    gates/fixtures/<fixture>`; `grep -c '^FINDING' out.txt`;
    `grep -o '^FINDING [^:]*' out.txt | sed 's/^FINDING //' | sort -u | wc
    -l`; set equality by `diff` of sorted IDs against `sort -u
    gates/fixtures/<fixture>.expected`
  - digests: `sha256sum tools/gates/*.py` and `sha256sum
    tools/gates/fixtures/*.{yml,md,expected}`
  - battery: `python3 check-gate-battery.py` (JSON report) and `python3
    check-gate-battery.py --selftest`
  - replay: `python3 replay-frozen.py --selftest`
  - harness: `python3 tools/harness/r8_checks.py --selftest` (live tree,
    read-only by its own header; prints `selftest_passed` + `tool_sha256`)
  - revision sweeps: `git diff --stat
    e1694bad6ac96aca45a11ca5746582b275929355..HEAD` and the same with `--
    tools/gates examples tools`
  - pin sweeps: `find tools/gates reports/round-9 -name expected.json |
    sort`; pin verification (this seat, read-only): for each `inputs` entry,
    recompute `sha256(<baseline>/<rel>)` and compare; compare `gate_sha256`
    against `sha256sum` of the live gate

## 2. The seven structural gates

All seven share the lane-wide verdict map **0 clean / 1 findings / 2
could-not-evaluate**, print one finding per stdout line, and grade exactly one
input class each. Blocks below give the row fields; the block heading is the
registry row name.

### phonology-sanity-gate

- kind: gate
- entry command: `python3 tools/gates/phonology-sanity-gate.py <culture-packet.yml>` (`-` reads the packet from stdin)
- verdict map: 0 clean / 1 findings (message opens `FAIL` or `REVIEW`) / 2 could-not-evaluate (unreadable/unparseable packet or no usable `phonology` block → one `G-DATA` finding)
- self-test spelling: `--selftest`, alias `--self-test` (both measured exit 0)
- pinned-value path: `tools/gates/fixtures/phonology-sanity-gate.{yml,expected}`
- write scope: gate run read-only; `--selftest` writes only inside `tools/gates/fixtures/`, regenerating a file atomically only when absent and refusing to overwrite divergent bytes (`phonology-sanity-gate.py:1268-1293`)
- owner: kotodama-shokunin lane; round-9 pair R9-O01..O14 (author + rerunner)
- measured: script sha256 `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230`; fixture sha256 `96dfa97e87c85a5c52145d6b9aa1b16572b2906b76ee6dee1591290a7ecb7421`, `.expected` `165bcc61fe4f3d0478613ef691d39e71afae0f7b32c5cfc1b44f9a6e393a54c6`; fixture run exit 1, 16 `FINDING` lines / 15 unique IDs, ID set identical to `.expected` (15 IDs: A-CLASS, A-NEUTRAL, A-ORDER, A-PARSE, A-TONE, I-DUPLICATE, I-UNKNOWN, M-EJECT, M-NASAL, M-ROUND, M-SONORITY, M-VOICE, T-C, T-SYL, X-NAME)
- selftest receipt: `selftest: fixture exit 1; 15/15 planted finding IDs present; 29 control cases passed` (exit 0)

### lexicon-coverage-audit

- kind: gate
- entry command: `python3 tools/gates/lexicon-coverage-audit.py <culture-packet.yml>`
- verdict map: 0 clean / 1 findings (`FINDING <id>: <message>`, id families `C-` coverage, `D-` derivation, `L-` loan layers) / 2 could-not-evaluate (missing or malformed input; reason on stderr as `ERROR:` lines, no `FINDING` printed)
- self-test spelling: `--selftest`, alias `--self-test` (both measured exit 0)
- pinned-value path: `tools/gates/fixtures/lexicon-coverage-audit.{yml,expected}`
- write scope: gate run read-only; `--selftest` regenerates absent fixtures atomically and never overwrites (`lexicon-coverage-audit.py:1443-1468`; fixture header "generated by `--selftest`; do not edit by hand")
- owner: kotodama-shokunin lane; round-9 pair R9-O01..O14
- measured: script sha256 `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287`; fixture sha256 `a1b8ed7c3548ace7a631b6b2752673f6a65a44896caecef170e373d67ec59187`, `.expected` `bd20bb40a9b7f53c81428ba1b33649966ae39cbac0d178efb7c94e4a371afac2`; fixture run exit 1, 20 `FINDING` lines / 18 unique IDs, set identical to `.expected` (18 IDs across C-/D-/L-)
- selftest receipt: `selftest: 14/14 checks passed` (exit 0)

### myth-consistency-gate

- kind: gate
- entry command: `python3 tools/gates/myth-consistency-gate.py <culture-packet.yml>`
- verdict map: 0 clean / 1 findings (`FINDING <id>: <message>`, ids `MC-P*`/`MC-M*`/`MC-S*`) / 2 could-not-evaluate (input missing/unreadable, or root is not a YAML mapping carrying a nonempty `name`)
- self-test spelling: `--selftest`, alias `--self-test` (both measured exit 0)
- pinned-value path: `tools/gates/fixtures/myth-consistency-gate.{yml,expected}`
- write scope: evaluator never writes to the packet; `--selftest` writes only inside `tools/gates/fixtures/`, absent-only, atomic (`myth-consistency-gate.py:91-92`, `:1059-1084`)
- owner: kotodama-shokunin lane; round-9 pair R9-O01..O14
- measured: script sha256 `5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08`; fixture sha256 `f94a700cc2d6cfadf91d8c96493fdc1e87dd50e53aa117d7598f12f524197086`, `.expected` `c871b6d33c2a29f74d17ce7642c73e328a0b212fddd618699c4a3c8464f45abb`; fixture run exit 1, 6 `FINDING` lines / 6 IDs, set identical to `.expected` (MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02)
- selftest receipt: `selftest: OK — fixture exit 1; planted IDs present: MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02; clean control exit 0 (0 findings)` (exit 0)

### costume-era-consistency-gate

- kind: gate
- entry command: `python3 tools/gates/costume-era-consistency-gate.py <culture-packet.yml>`
- verdict map: 0 clean / 1 findings (`FINDING <id>: [<severity>] <message>`; severity vocabulary `[reject]` demonstrated contradiction with the packet's own inputs, `[hold]` essential input unresolved, `[note]` declared departure kept visible) / 2 could-not-evaluate (unreadable/unparseable packet; e.g. `FINDING G-DATA: [could-not-evaluate] costumes must be a list`)
- self-test spelling: `--selftest`, alias `--self-test` (both measured exit 0)
- pinned-value path: `tools/gates/fixtures/costume-era-consistency-gate.{yml,expected}`
- write scope: read-only at run time; `--selftest` re-pins fixtures only when absent, atomically (`costume-era-consistency-gate.py:1481-1506`)
- owner: kotodama-shokunin lane; round-9 pair R9-O01..O14
- measured: script sha256 `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f`; fixture sha256 `36d92113d0cb8e04687c36694b507e93f25ca08c04003d75b7b537de65c1ea0e`, `.expected` `4b0724f9038d8a6a7a6189e91bdfdbf6e04beb101bac2b2ef37a708e704d0279`; fixture run exit 1, 25 `FINDING` lines / 21 unique IDs, set identical to `.expected` (21 IDs: E-01, EAR-01, EAR-04, G-ERA, MAT-01..MAT-07, R-01..R-07, T-01..T-03)
- selftest receipt: `self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs` (exit 0)

### naming-collision-gate

- kind: gate
- entry command: `python3 tools/gates/naming-collision-gate.py <culture-packet.yml>`
- verdict map: 0 clean / 1 findings (`FINDING <id>: <LEVEL> — <message>`, LEVEL ∈ FAIL / HOLD / REVIEW) / 2 could-not-evaluate (unreadable file, YAML outside the declared subset, root neither mapping nor list of mappings, or packet without `name`); missing sections stay exit 1 as HOLD findings (`G-DATA` only for uninterpretable input)
- self-test spelling: `--selftest`, alias `--self-test` (both measured exit 0)
- pinned-value path: `tools/gates/fixtures/naming-collision-gate.{yml,expected}`
- write scope: no network, no writes at run time; `--selftest` reads the two committed fixture files (`naming-collision-gate.py:106`)
- owner: kotodama-shokunin lane; round-9 pair R9-O01..O14
- measured: script sha256 `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`; fixture sha256 `c2ef97decc788802fa6266805731929f7f921f22e00c9fe6e0ec82dc6450f0fa`, `.expected` `805ea6cda67230d52c80ada8a5e904c7cc49c9983c0b1dba5355d7303e423404`; fixture run exit 1, 12 `FINDING` lines / 11 unique IDs, set identical to `.expected` (11 IDs: CROSS-HOLD, DERIV-AFFIX, DERIV-HOLD, DERIV-REPLAY, NAME-LEXEME, NAME-NEAR, NAME-REUSE, NAME-VISUAL, PHON-CODA, PHON-INVENTORY, PHON-ONSET)
- selftest receipt: `selftest: OK — fixture findings 12 across 11 ids (…); positive control clean; malformed inputs exit 2; missing profile held; case policy routed` (exit 0)

### provenance-audit

- kind: gate (corpus scanner)
- entry command: `python3 tools/gates/provenance-audit.py <corpus-file> [more files ...]` / `<directory> [more ...]` (`*.md`, sorted)
- verdict map: 0 clean / 1 findings / 2 could-not-evaluate for at least one path (missing, unreadable, not UTF-8 text, not an entry document) and also for argparse usage errors. Finding vocabulary: `FINDING missing-topic|missing-sources|empty-sources|missing-couples|empty-couples|missing-calibration: <path>: <detail>`; observation lines `INFO to-verify-count`, `INFO calibration-prose-only`, `INFO scan`; `CANNOT-EVALUATE: <path>: <reason>`
- self-test spelling: **`--selftest` only** — `--self-test` is an unrecognized argument and exits 2 (measured: `provenance-audit.py: error: unrecognized arguments: --self-test`)
- pinned-value path: fixture tree `tools/gates/fixtures/provenance/` (1 clean + 6 defect entries) and the committed ID lists `tools/gates/fixtures/provenance.expected` and `tools/gates/fixtures/provenance-audit.expected` (byte-identical today)
- write scope: read-only: never writes to the corpus (`provenance-audit.py:23`); `--selftest` verifies the fixture tree against embedded constants and regenerates absent files atomically (`:407-435`)
- owner: kotodama-shokunin lane; round-9 pair R9-O01..O14
- measured: script sha256 `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a`; fixture-tree run over `tools/gates/fixtures/provenance` exit 1, 6 `FINDING` lines / 6 unique IDs (missing-topic, missing-sources, empty-sources, missing-couples, empty-couples, missing-calibration), set identical to `.expected` (6 lines), plus `INFO scan: files=7 marks=2 mark-lines=2 findings=6 blocked=0`
- selftest receipt: `SELFTEST OK: 7 fixture file(s), planted IDs missing-topic, missing-sources, empty-sources, missing-couples, empty-couples, missing-calibration, exit 1 on the defect tree, exit 0 on the clean entry, exit 2 on a missing path` (exit 0)

### handoff-packet-check

- kind: gate (adjacency)
- entry command: `python3 tools/gates/handoff-packet-check.py <packet.md>` (`-` reads the packet from stdin)
- verdict map: 0 clean / 1 findings (`FINDING <id>: <LEVEL> — <message>`, ids `HO-*`, e.g. `HO-EMPTY`, `HO-MISSING`) / 2 could-not-evaluate (unreadable/malformed packet, `HO-DATA`, or argparse usage error)
- self-test spelling: **`--selftest` only** — `--self-test` exits 2 with `unrecognized arguments` (measured)
- pinned-value path: `tools/gates/fixtures/handoff-packet-check.{md,expected}` — note the `.expected` file has **no trailing newline**: it carries 9 IDs while `wc -l` reports 8; compare as an ID set (standard §4), never by line count
- write scope: read-only: never edits a packet, never writes to the corpus (`handoff-packet-check.py:27`)
- owner: kotodama-shokunin lane; round-9 pair R9-O01..O14
- measured: script sha256 `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575`; fixture sha256 `da066ec0e97b348e196e6b058a5a5179dfb7380339cd018324de6e9ae70ff0c8`, `.expected` `1aab55f27838f8a8a24c9a27cfb5813f4b224c0e7970fbf50ea2df8f85b97892`; fixture run exit 1, 11 `FINDING` lines / 9 unique IDs, set identical to `.expected` (HO-BASELINE, HO-CANON-CLAIM, HO-CANON-MARKER, HO-CONTRACT-REF, HO-DEP-FLOAT, HO-EMPTY, HO-GLOSS-ETYM, HO-MANIFEST-DIGEST, HO-MISSING)
- selftest receipt: `selftest: OK — fixture findings 11 across 9 ids (…); clean control exit 0; probes cover canon, baseline, dependency, contract_ref and glossary vocabulary; malformed inputs exit 2; CLI verified from another cwd` (exit 0)

## 3. Round-9 harness entries

### isolated legacy selftest battery (`tools/check-gate-battery.py`)

- kind: gate (harness; two duties, one report: the seven isolated selftests, plus the committed-baseline check added by round-9 claim O15)
- entry command: `python3 tools/check-gate-battery.py [--timeout S] [--keep-mirror] [--baselines-root PATH ...]`
- verdict map, duty 1 (selftests): 0 all seven selftests exit 0 **and** the live gates tree is preserved (per-file sha256 and path set) / 1 a selftest exited 1 with recognizable stable failure evidence (`SELFTEST FAIL`, `FAIL <token>`, `failed: <token>`) / 2 could-not-evaluate: gate file missing, copy mismatch, live tree changed, launch error, timeout, abnormal exit, or an exit-1 child without recognizable evidence (`GATE-CRASH-EXIT1`). Documented consequence: five of the seven gates assert with bare `assert`, so a genuine selftest failure there is crash-shaped and classifies exit 2, not 1.
- verdict map, duty 2 (baselines): every discovered baseline verified as `pinned` → contributes 0; any of `BASELINE-TAMPERED` (a snapshot byte differs from its `inputs` pin), `BASELINE-GATE-REVISED`, `BASELINE-UNPINNED` / `BASELINE-GATE-UNPINNED` (`inputs` empty/absent → `unpinned (legacy)`), `BASELINE-MALFORMED*` (schema/gate/expected-block shape), `BASELINE-PATH-ESCAPE`, `BASELINE-EXTERNAL-INPUT`, `BASELINE-INPUT-MISSING`, `BASELINE-GATE-UNKNOWN`, `BASELINE-GATE-UNCOVERED` → could-not-evaluate, exit 2. A baseline is **never re-executed** here: `pinned` means the digests and pins hold, not that the verdict was compared (`verdict_replay: "not-run: …"` in the report). Battery exit is the worse of the two duties.
- self-test spelling: `--selftest` (measured `SELFTEST OK 28/28 controls behaved as expected`, exit 0); `--timeout` must be positive finite or usage error exit 2; `--baselines-root` is repeatable (`action="append"`) and replaces the committed roots for one run
- pinned-value path: fixed `GATE_NAMES` tuple and control expectations in the script; no manifest is executed and no shell string is built (children launched as `[sys.executable, <gate>, "--selftest"]`, `shell=False`). Committed baseline roots: `BASELINE_ROOTS = tools/gates/expected/` and `tools/gates/frozen/`
- write scope: writes only a disposable mirror under the system temp root (measured this run: `/var/tmp/gate-battery-…`, `removed: true`); `--keep-mirror` retains it; a gate is never invoked on a live path
- owner: kotodama-shokunin lane; round-9 duty-2 extension owner **R9-O15** (landed during this wave)
- measured at script sha256 `9ad0ef9516852c0f55b43edc3d3cf41795b2bd3c295b04c0b93946064bf2093c` (2026-10-17T20:52-20:53Z):
  - committed invocation `python3 tools/check-gate-battery.py` → **exit 2**. Duty 1: `pass 7 / fail 0 / unevaluable 0`; `originals {preserved: true, modified 0, added 0, deleted 0, files_hashed_before 28, files_hashed_after 28}`. Duty 2: `baselines_found 5, pinned 5, readings {pinned: 5}, gates_covered 5`, `gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]`, two `BASELINE-GATE-UNCOVERED` findings. Cause: those two pins live only under `reports/round-9/baselines/`, outside both committed roots.
  - three-root invocation `python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines` → **exit 0**; `baselines_found 8, pinned 8, readings {pinned: 8}, gates_uncovered []` — 7/7 gates covered; handoff's pin is found twice (two byte-identical copies, sha256 `9dc21cd5…`, both read `pinned`). This is the invocation that satisfies the O-claim baseline duty today; the committed default does not (see §5 item 1).
- limit inherited from the battery's own header: matching hashes prove byte preservation, not absence of writes — a rewrite with identical bytes passes, a new file or a deletion does not; and `pinned` proves digests and pins, never the verdict.

### round-9 validation runner (`reports/round-9/run-validation.py`)

- kind: harness (round claim checker; the round's counted command `python3 reports/round-9/run-validation.py`, named in `reports/round-9/claims.json`)
- entry command: `python3 reports/round-9/run-validation.py` (no flags; writes `reports/round-9/validation.json`; deterministic receipt — sorted keys, no wall-clock timestamps, child output path/timestamp-normalized)
- verdict map: 0 `acceptance_checks_passed: true` (every declared F/O/D threshold met) / 1 one or more claim failures recorded (missing worker evidence is a failing dependency naming the exact missing paths, never synthesized). Measured 2026-10-17T20:54Z at script sha256 `58e8fa4f2b11758b…`: **exit 1**, `acceptance_checks_passed: false`, 13 failures — F 11 (missing `reports/round-9/freshness/*R9-R8-F02*` and `*F04*` receipts), O 1 (`tools/check-gate-battery.py exit 2 on the delivered tree … uncovered gates ['myth-consistency-gate.py', 'naming-collision-gate.py']`), D 1 (`tools/check-evidence-coupling.py --frozen examples/culture-d3/expected.json` exit 2: `D3-SNAPSHOT` manifest digest mismatch for `corpus/knowledge/synthesis/worldbible-integration-contract.md`, declared `50c4c2f2…`, actual `5f4c02bf…`). The F/O/D content of those failures is the shards' measured state, quoted here as the runner reported it — not this seat's verdict on any claim.
- self-test spelling: none — no `--selftest` in the CLI at revision `58e8fa4f…`; the runner instead invokes the batteries'/gates' own selftests and records their exit and stdout digests
- pinned-value path: `input_sha256` per consumed input and a `runner_sha256` self-pin inside `validation.json`. Stale-receipt hazard, measured: the `validation.json` on disk at 20:53Z declared `runner_sha256 c08bae4d…` while the script's own digest was `5717dfb4…`/`58e8fa4f…` — always compare `runner_sha256` against `sha256sum reports/round-9/run-validation.py` before quoting the receipt.
- write scope: "Writes ONLY reports/round-9/validation.json in this repository (no scratch, no network)" (module docstring); every other tool it needs is invoked as a subprocess
- owner: kotodama-shokunin lane; round-9 seat **R9-O16**
- in-flight defect observed, then resolved within the wave (recorded because a crashed runner is not a failing claim): at script digest `5717dfb4…` (mtime 2026-10-17 17:53:29-03:00) the runner crashed — `NameError: name 'resolver' is not defined` at `run-validation.py:1011` (`read_baseline` ← `measure_o_baselines` `:1164` ← `main` `:1463`), exit 1 with an empty stdout. Re-run at `58e8fa4f…` exits 1 cleanly with the failures listed above and no traceback.
- revision churn observed after the clean measurement: at digest `2b5f6e70…` (mtime 17:54:46-03:00) the runner crashed again — `ValueError: too many values to unpack (expected 2, got 4)` at `run-validation.py:802` (`f_measure` ← `measure_f` `:922` ← `main` `:1540`), exit 1, and it did **not** rewrite `validation.json` (the on-disk receipt still declares `runner_sha256 58e8fa4f…`). The file is under active edit by its owner (R9-O16); any quoted run must name the digest it was measured at, and a crashed run must never be read as a claim failure.

### round-8 parent-check fix harness (`tools/harness/r8_checks.py`)

- kind: gate (bounded regression harness; new code for the round-7 F-leg defect, never imports the filed runner)
- entry command: `python3 tools/harness/r8_checks.py --selftest` | `--measure` (exactly one required; neither → usage error to stderr)
- verdict map: 0 all-pass selftest / 1 any-fail (`--measure` prints the corrected measurement as JSON)
- self-test spelling: `--selftest` (measured exit 0, JSON `"selftest_passed": true`, `"tool_sha256": "0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe"`)
- pinned-value path: regression controls embedded in the script (real round-7 inputs, benign-duplicate, genuine-collision, fail-before, malformed-input controls)
- write scope: read-only over repository inputs; stdout receipts only, no file writes (header, `r8_checks.py:34`)
- owner: kotodama-shokunin lane; round-8 seat R8-O02 (defect fix for the round-7 F leg)

### frozen replay (`tools/replay-frozen.py`)

- kind: gate (frozen-manifest replay; executes snapshots, never the manifest command string)
- entry command: `python3 tools/replay-frozen.py <MANIFEST.tsv> [--repo-root DIR] [--json]`
- verdict map: 0 recorded verdict reproduced (including expected red verdicts) / 1 mismatch / 2 could-not-evaluate, including `snapshot_tampered`; refuses unsafe paths (absolute, `~`, any `..`, flag-like components such as `--selftest`/`./--selftest`/`-`, symlinks, outside-repo), and requires the gate to be a Python file directly under `tools/gates`; argparse usage errors exit 2
- self-test spelling: `--selftest` (measured `selftest: 79/79 checks passed`, exit 0)
- pinned-value path: manifest columns `gate_sha256`, `input_sha256`, `output_sha256` (verified before any gate runs) plus selftest constants in the script
- write scope: auto-cleaned scratch only (isolated temporary mirror for the pinned snapshot)
- owner: kotodama-shokunin lane (rounds 3-4 layout; round-9 D-leg replay)
- round-9 D-leg uses it for the D3 frozen replay (`reports/round-9/targets.json` R9-D04) — the D3 row itself is owned by the D shards and is not re-measured by this seat.

### D3 acceptance entries (cited from `SKILL.md:248-251`, not re-measured by this seat)

- `D3 assembly drift` — gate, bounded profile — `python3 tools/assemble-culture-d3.py --check` — 0 byte-identical / 1 drift / 2 could-not-evaluate — self-test `--selftest`, isolated actual CLI — pinned: four component hashes and the committed packet/projection — write scope: default rebuilds only two derived outputs; check read-only; selftest scratch — owner: kotodama-shokunin lane (round-9 shards R9-D01..D12).
- `D3 evidence coupling` — gate, bounded profile — `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` — 0 consistent supplied model / 1 profile contradiction / 2 could-not-evaluate — self-test `--selftest`, independent committed controls and isolated subprocesses — pinned: closed source tuples/digests; optional `--frozen examples/culture-d3/expected.json` — write scope: normal run read-only; selftest disposable scratch — owner: kotodama-shokunin lane (round-9 shards R9-D01..D12).
- These two rows are reproduced from the lane's own registry table because round 9's D claim re-runs them; their exit codes are the D shards' evidence, not this seat's. Quote the D fragments for measured values.

## 4. Round-9 `expected.json` baseline pins — final sweep

All seven gates carry a committed pin. Sweep command and time — `find
tools/gates reports/round-9 -name expected.json | sort`, 2026-10-17T20:53:12Z
→ 8 files (handoff is pinned twice, byte-identical). Verification evidence is
the extended battery's own per-baseline reading (`pinned` = every `inputs`
digest recomputed against the snapshot bytes, `gate_sha256` matched against
the live gate script, `expected` block shape valid; tamper/revision/unpinned
readings would force exit 2), measured in the three-root run at
2026-10-17T20:53:35Z (§3). The battery does **not** re-run verdicts
(`verdict_replay: not-run`); the verdict comparison lives in each baseline's
own re-run receipt, which the R9-O18..O20 auditors own.

| gate | baseline id | `expected.json` path (landed) | pin file sha256 | `gate_sha256` (declared = live) | `inputs` pin | expected verdict | battery reading |
|---|---|---|---|---|---|---|---|
| costume-era-consistency-gate | r9-pre | `tools/gates/expected/costume-era-consistency-gate/r9-pre/expected.json` | `7ec01a1d…` | `e6bffd70…478f` | `packet.yml` `36d92113…ea0e` (byte copy of the fixture) | exit 1, findings, 21 IDs (`E-01`, `EAR-01`, `EAR-04`, `G-ERA`, `MAT-01..07`, `R-01..07`, `T-01..03`); `stdout_sha256 482c1597…08b3` | pinned |
| phonology-sanity-gate | r9-pre | `tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json` | `2763614f…` | `d5fe087f…4230` | `packet.yml` (1 input) | exit 1, findings, IDs `[A-NEUTRAL]`; `stdout_sha256 1ce5f0cd…66dd2` | pinned |
| handoff-packet-check | r9-pre | `tools/gates/frozen/handoff-packet-check/r9-pre/expected.json` **and** a byte-identical copy at `reports/round-9/baselines/handoff-packet-check/expected.json` (both `9dc21cd5…`) | `9dc21cd5…` | `e2fa3223…ad575` | `packet.md` `0d8d660b…d2fc` | exit 0, class clean, `findings: []`; `stdout_sha256 7c581047…4685` | pinned (twice) |
| lexicon-coverage-audit | r9-pre | `tools/gates/frozen/lexicon-coverage-audit/r9-pre/expected.json` | `0fad58ba…` | `2c4dd397…d4287` | `packet.yml` (1 input) | exit 1, findings, 18 IDs (C-/D-/L- families) | pinned |
| provenance-audit | r9-pre | `tools/gates/frozen/provenance-audit/r9-pre/expected.json` | `ba4b2994…` | `8a96aaf4…4e3a` | 20 corpus-entry inputs | exit 1, findings, IDs {empty-couples, empty-sources, missing-calibration, missing-couples, missing-sources, missing-topic} | pinned |
| myth-consistency-gate | r9-pre | `reports/round-9/baselines/myth-consistency-gate/expected.json` | `a87edc53…` | `5368b135…5f08` | `packet.yml` `e0f21509…b643` (= `examples/culture-d2/packet.d2.yml`) | exit 0, class clean, `findings: []` | pinned |
| naming-collision-gate | r9-pre | `reports/round-9/baselines/naming-collision-gate/expected.json` | `2f34ee18…` | `d9e4e8f4…0a1d` | `packet.yml` `e0f21509…b643` (byte copy of `examples/culture-d2/packet.d2.yml`; 17 FINDING lines) | exit 1, findings, IDs {CROSS-HOLD, NAME-NEAR, PHON-INVENTORY} | pinned |

- Coverage caveat, measured: the committed default battery invocation reaches
  only the five pins under `tools/gates/expected|frozen`; myth and naming are
  reachable only via the third root (§3, §5 item 1). Both roots and all eight
  pins are `pinned`; the gap is discovery, not pin validity.
- Two revision values are declared across the set (costume/handoff/myth:
  `a7bb205d…`; naming: `e1694bad…` with a supersession note) — see §5 item 2.

## 5. Divergences and contested scope (reported, not absorbed)

1. **Three baseline roots are in flight.** `gate-frozen-run-standard.md` §3
   names `tools/gates/frozen/<gate-name>/<baseline-id>/`; the costume seat's
   own `freeze.txt` records its root as `tools/gates/expected/…` "per the
   round-9 assignment"; the naming seat's `expected.json` `layout_note`
   names `reports/round-9/baselines/<gate-name>/` and proposes battery
   discovery via `reports/round-9/baselines/*/expected.json`. The standard §3
   also requires a bare baseline id to resolve under exactly one gate
   directory. With three roots, the R9-O15 battery extension cannot honour
   that rule without a declared root list or an orchestrator reconciliation —
   **decision needed from the orchestrator/integrator; the registry records
   the observed paths without endorsing one root.**
2. **Two `revision` values across one round's baselines.** The costume
   baseline pins `revision a7bb205d…` (HEAD at freeze); the naming baseline
   pins `e1694bad…` (the claims' `baseline_revision`) with a `revision_note`
   that the integration commit supersedes it. The standard §5 step 6 expects
   the commit that carries the baseline. Both are legible as declared; the
   orchestrator's single round-9 commit is the reconciliation point.
3. **`run.log` is ignored by `.gitignore`.** `.gitignore` line 3 carries
   `*.log`; the costume `freeze.txt` records that `run.log` needs `git add -f`
   at integration or the baseline commits without its verbatim stdout.
4. **`handoff-packet-check.expected` has no trailing newline** — 9 IDs, `wc
   -l` = 8. Line-count comparisons will mis-read it; use finding-ID sets
   (standard §4).
5. **`/tmp` inode exhaustion** (measured this seat and independently by the
   phonology rerunner seat): every worker that needs scratch should assume
   `/tmp` is unusable and use in-repo `.scratch/` (untracked).
6. **Battery discovery mechanism is now measured, and the committed default is short of green.** The extended battery's roots are `tools/gates/expected/` + `tools/gates/frozen/`; the committed running of `python3 tools/check-gate-battery.py` (2026-10-17T20:52Z, script `9ad0ef95…`) reads **exit 2** with `gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]` because those two pins live only under `reports/round-9/baselines/`. Passing the third root explicitly (`--baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines`, 20:53:35Z) reads **exit 0** with `baselines_found 8, pinned 8, gates_uncovered []`. The `--baselines-root` help text says it "is not a way to silence a committed baseline defect" — so either the missing pins get copies under `tools/gates/{expected,frozen}/`, or the third committed root is adopted for round 10 and the durable convention is fixed. Decision for the orchestrator; the registry states both readings. The round runner (R9-O16) currently records this as its single O failure, so O is **not green** on the delivered tree as of 20:54Z.
7. **A duplicated baseline id resolves in two gate directories.** handoff's `r9-pre` is present under `tools/gates/frozen/handoff-packet-check/` and `reports/round-9/baselines/handoff-packet-check/` with byte-identical `expected.json` (`9dc21cd5…`). The standard §3 says a bare baseline id must resolve under exactly one gate directory — fail closed on two candidates. In the three-root battery run the duplicate was silently counted as two `pinned` baselines, not flagged. Either remove one copy before the integration commit or declare (in the registry row and the standard's own text) that identical duplicate copies dedupe by digest.
8. **Stale `validation.json` receipt (runner revision hazard).** At 20:53Z the committed `reports/round-9/validation.json` declared `runner_sha256 c08bae4d…` while the script on disk was `5717dfb4…` (and later `58e8fa4f…`). The receipt is regenerated by each run, but nothing in the file's own text says which revision is current — always re-run the runner and compare `runner_sha256` before quoting it. The runner's in-flight `NameError` crash and its resolution are recorded in §3.
9. **Cross-leg state visible in the runner receipt (not this seat's claim).** The runner's D failure — `check-evidence-coupling.py --frozen` reading `D3-SNAPSHOT` digest mismatch for `corpus/knowledge/synthesis/worldbible-integration-contract.md` (declared `50c4c2f2…`, actual `5f4c02bf…`) — and its F failures (missing `R9-R8-F02`/`F04` receipts at 20:54Z) are quoted here only because the registry must not present O alone as green while the round's own runner says otherwise. The D and F shards own those findings.

## 6. What this registry does not claim

- Not a judgment that any gate is correct, that any baseline is good design,
  or that any culture/design artifact passes. A baseline pins bytes and a
  verdict; it never blesses content (standard §2, §10).
- Not a completion claim for round 9. Measured at the final sweep
  (2026-10-17T20:53-20:54Z): 8 pin files covering 7/7 gates, all reading
  `pinned`; but the committed battery invocation still exits 2 on discovery
  coverage (§5 items 1, 6), and the round runner exits 1 with 13 recorded
  failures (§3). Those are the shards' and the orchestrator's to close; the
  registry reports the readings and does not upgrade them.
- Not a verdict comparison: the battery never re-executes a baseline, and the
  auditors' R9-O18..O20 seats own re-running baselines and tamper rejection.
- Not a re-measurement of the D-leg tools; those rows are cited from
  `SKILL.md` and owned by the D shards.
- Not authoritative over the fleet: the two-evidences obligation is fleet
  policy, the layout and schema here are lane conventions, and a fleet
  amendment wins (standard §10).
