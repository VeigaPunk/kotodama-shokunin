# R10-F12 — drift shard 12: SCORECARD.md re-run commands, first half

Assignment: R10-F12 (freshness drift shard 12). Scope: every runnable command cited in
`SCORECARD.md` **lines 1–105** (round-5 axis table, capabilities table, round-6 axis table,
round-7 declaration, round-8 acceptance sentence). Lines 106–210 (round-8 axis table
onward) are shard 13's; they are not re-run here (boundary list below).

Date: 2026-10-17. Revision re-run against: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (HEAD,
immutable clone). Lane working tree was dirty and moving while this shard ran (see Concurrency).

## Method

- Every command re-run inside disposable clones of HEAD (`git clone --local --no-hardlinks`),
  never in the lane working tree: `.scratch/f12/{iso, fresh5, fresh6, fresh7, fresh8, fresh9,
  fresh10, pin5, pin6, pin8}`. Nothing outside `.scratch/f12/` was written by this shard.
- `TMPDIR=$PWD/.scratch/f12/tmp` and `PYTHONDONTWRITEBYTECODE=1` for every run.
- Per run recorded: exit code, stdout/stderr sha256, wall seconds — raw rows in
  `.scratch/f12/out/results.jsonl`, `results-fresh.jsonl`, `results-pinned.jsonl`; outputs in
  `.scratch/f12/out/<label>.{out,err}`.
- Hash caveat: several outputs embed the absolute clone path (e.g. the battery's mirror root),
  so stdout sha256 is run-location dependent. Hashes below are canonical for the clone named;
  exit code and failure text are stable across clone roots (verified for r5/r6/r7/r8).
- Web citations in lines 1–105: **zero**. Sweep `sed -n '1,105p' SCORECARD.md | grep -oE
  'https?://[^ )`,]*'` → no matches, so no access attempt was required for this half.
- Pinned-revision controls (to separate pin drift from breakage): round-5 @ `9c52635`
  (its work commit), round-6 @ `b815bf4`, round-8 @ `e1694ba` (its admission commit).

## Table 1 — command re-run ledger (HEAD e3a1ec9, clean clone)

| # | command | SCORECARD.md line | exit | stdout sha256 | verdict |
|---|---|---|---|---|---|
| 1 | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 30, 65 | 0 | `18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650` | current |
| 2 | `python3 tools/check-craft-exercise.py --selftest` | 32, 50, 53 | 0 | `77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32` | current (10/10 + 18/18) |
| 3 | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 31, 34, 66 | 0 | `c83dac8f8bab0feaa55b853a43a96562d0ccb9dd6477d24b995d2331577d5c02` | current at :31/:66; :34 counts drifted (F12-07) |
| 4 | `python3 tools/source-audit-inventory.py --json --summary` | 48 | 0 | `d48d80d35e3f4e8652124c4c6f03125a76d9c5983c1db979722b6bd9450e9c20` | current (identical totals to #3) |
| 5 | `python3 tools/source-audit-inventory.py --selftest` | 48 | 0 | `1496ebf7b9ed578422d6294aecba6f9b3ad273a280bbcd34bc8882d6a89f37a9` | current |
| 6 | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | 35, 70 | 0 | `7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685` | current (`fields=16/16 glossary-entries=20 findings=0`) |
| 7 | `python3 tools/assemble-d2.py --selftest` | 46 | 0 | `a81294c0347660d9b46952146bac967fc80c79c9d629d7f34e69d0411bec0336` | current (42/42) |
| 8 | `python3 tools/assemble-d2.py --check` | 46 | 0 | `2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386` | current (byte-identical assembly) |
| 9 | `python3 tools/replay-frozen.py --selftest` | 47 | 0 | `4d6aaea127ad99737b53ce50a7378efad5562b6fa01da88e9ca8610aa604ea16` | current |
| 10 | `python3 tools/assemble-culture-d3.py --check` | 93 | 0 | `e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a` | current (byte-identical assembly) |
| 11 | `python3 tools/check-evidence-coupling.py --selftest` | 93 | 0 | `cf62bc50e303b793b6b930c83a5ddd7d462c39cc39fef133385db830c1d380ce` | current |
| 12 | `python3 tools/check-gate-battery.py --selftest` | 32, 52 | 0 | `8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28` | current (28/28; :32's "10/10" drifted, F12-07) |
| 13 | `python3 tools/check-gate-battery.py` | 52 | **2** | `9b382adf80ab56dfaa662ed7833f9f376f550146ca10e873cd9c972652f4957f` | **stale-documented** (F12-01) |
| 14 | `python3 tools/gates/costume-era-consistency-gate.py --selftest` | 45 | 0 | `d45a9add4c616d584ce08bd77135d912d31e8d3c1fb7f4bfc2d8f83772ddd851` | current (10/10, 21 IDs) |
| 15 | `python3 tools/gates/handoff-packet-check.py --selftest` | 45 | 0 | `be1ef058b2cfc67a564003917fd39125121755ae66960bd9ea5feb04c0c7ef2f` | current (11 findings / 9 ids) |
| 16 | `python3 tools/gates/lexicon-coverage-audit.py --selftest` | 45 | 0 | `fd731b1423443238cb5c1fc75dfd350244cc611295c9713b129252b251478658` | current (14/14) |
| 17 | `python3 tools/gates/myth-consistency-gate.py --selftest` | 45 | 0 | `80e7d9dc86a29cf56591cfa0cf5bd8fab82a84d4b9d67f03200f1bd689c5aa53` | current |
| 18 | `python3 tools/gates/naming-collision-gate.py --selftest` | 45 | 0 | `d3566a9cad69f956fd7a4274cb80ad4b95a92bb63a9cf689e45338d05ca5c7da` | current (12 findings / 11 ids) |
| 19 | `python3 tools/gates/phonology-sanity-gate.py --selftest` | 45 | 0 | `3e9a1209afa352902922a64df1d0bf7a48c25cf09126aa62b70855bd3b447843` | current (15/15 IDs, 29 cases) |
| 20 | `python3 tools/gates/provenance-audit.py --selftest` | 45 | 0 | `66ac915b83e4ba2eff10c63e4ea7a2a283ddf9b58b59aa7200f6c797c8f9208b` | current |
| 21 | `python3 reports/round-5/run-validation.py` | 30, 32, 33, 34, 35 | **1** | `dd65e422c40337b31962730c44fbac5d0fafa39d9c008b61feb9c2559b69efc9` (fresh clone; shared clone `fdf734fe576939cc9f8ca5496bae17f8fc4cca9ca9995c845a185dbaf5bc5e13`) | **stale-documented** (F12-02) |
| 22 | `python3 reports/round-6/run-validation.py` | 65, 66, 67, 68, 69, 70 | **1** | `79440ea7395873dd2cf9e7cde55dc9217ddd61c994579728fd667ab243ca9b9d` | **stale-documented** (F12-03) |
| 23 | `python3 reports/round-7/run-validation.py` | 92, 93 | **1** | `3ffc98f636827ba13a9743dbabc19e0977c0722887847879bd8c71789bc790ea` | **stale-documented** (F12-04) |
| 24 | `python3 reports/round-8/run-validation.py` | 104 | **1** | `b2fb989333a06f0c095731fcb5e77e7843b442a14d41156f9fee4f37bc66781e` | **stale** (F12-05) |
| 25 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json` (claim at :32 "both round-3 manifests reproduce 7/7") | 32 | **2** | `45537a5e815c9732f66e3ffea6f61b6b8dbba424ef0a0dd01d3df83629df2a96` | **stale-documented** (F12-06) |
| 26 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv --json` | 32 | **2** | `915233ea24d531c38c963b58a6f0cf11bdd3b16cf66910e1c6f491e87274d9bc` | **stale-documented** (F12-06) |

Pinned-revision controls (same commands, checked-out revision instead of HEAD):

| command | checkout | exit | stdout sha256 | reading |
|---|---|---|---|---|
| `python3 reports/round-5/run-validation.py` | `9c52635` (round-5 work commit) | 0 | `8cc7b0fe688a9bab3a3ae8bc811cc72427c4a1ffda2456318f7e693b2b59abcd` | green at its own revision → HEAD red is pin drift |
| `python3 reports/round-6/run-validation.py` | `b815bf4` (round-6 work commit) | 0 | `46c98f4ec4c9fc86af82a950909fca74d4009aed2842322a363dc1d3e0247ce7` | green at its own revision → HEAD red is pin drift |
| `python3 reports/round-8/run-validation.py` | `e1694ba` (round-8 admission commit) | **1** | `b2fb989333a06f0c095731fcb5e77e7843b442a14d41156f9fee4f37bc66781e` | **byte-identical to the HEAD run** → not reproducible from any committed revision |

## Table 2 — SCORECARD assertion vs observed

| SCORECARD.md line | assertion | observed at HEAD | reading |
|---|---|---|---|
| 30 | positive craft example exit 0 | exit 0, `OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)` | holds |
| 30 | "D2 still 20 findings" | not re-derivable: the 20 came from the round-3 replay, which is now exit 2 (F12-06); filed round-5 validation records `d2_findings: 20` | **to-verify / blocked** (F12-06) |
| 31, 66 | 179 knowledge entries; partitions 16/16/16/24/13/94 | `files: 179`; partition counts `{civilizations: 94, culture-material: 16, linguistics: 16, myth-symbol: 16, synthesis: 24, verification: 13}` | holds |
| 32 | seven legacy gate selftests pass | 7/7 exit 0 (rows 14–20) | holds |
| 32 | "battery 10/10 controls" | battery selftest reports **28/28 controls** | **count drifted** (F12-07) |
| 32 | "craft 10/10 domain + 18/18 CLI controls" | `SELFTEST OK 10/10 tamper cases detected`; `CLI-SELFTEST OK 18/18 cases passed` | holds |
| 32, 67 | "both round-3 manifests reproduce 7/7" | both exit 2, `{rows: 7, reproduced: 0, could_not_evaluate: 7}` | **no longer reproduces live** (F12-06) |
| 33, 34, 35 | round-5 F/O acceptance true (`reports/round-5/validation.json`) | committed blob `78444f4c…` is green (F/O true); live re-run exit 1 (F/O false) | **revision-scoped** (F12-02) |
| 34 | "22 rows / 20 IDs" | recorded in the filed round-5 validation (`worker_rows: 22`, `distinct_original_claims: 20`); not re-derived (runner fails before that check) | recorded, not re-derived |
| 34 | "592 raw marker-bearing lines, 598 raw occurrences" | inventory now reports `raw_lines 610, raw_occurrences 616, ci_occurrences 618, marker_occurrences 584, marker_lines 581`; no current field reproduces 592/598 | **numbers drifted** (F12-07) |
| 35, 70 | handoff "16 fields and 20 glossary entries, exit 0" | `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0 | holds |
| 45 | seven isolated legacy selftests | 7/7 exit 0 | holds |
| 46, 47 | D2 assembler + replay selftests | both exit 0 (42/42 for the assembler) | holds |
| 49 | "13 supplemental ledgers / 148 audits" | 13 named ledgers in `corpus/lessons/supplement-opencode-1/sources/` sum to **148** audits (excluded: `02-connector.json` 7, `06-coupling-table.json` 6 → 161 across all 15 files) | holds (exact) |
| 51 | `corpus/lessons/round-4-audit/` (16 reports) | 16 entries (13 civ shards + culture-material, linguistics, myth-symbol) | holds |
| 52 | isolated gate battery runner (no caveat) | selftests 7/7 pass but the command exits 2 (baselines 5/7 covered) | **stale-documented** (F12-01) |
| 65–70 | round-6 F acceptance + counts (`F true`, 24-row/≥6-passage/≥4-entry/≥3-parent) | command exit 1 at HEAD ("append-only prefix lost: SKILL.md"); green at `b815bf4` | **revision-scoped** (F12-03) |
| 92, 93 | round-7 declaration commands | round-7 runner exit 1 (red at filing too, 2 failures; 4 at HEAD); `assemble-culture-d3.py --check` and `check-evidence-coupling.py --selftest` exit 0 | mixed: tools hold, runner pin-drifted (F12-04) |
| 93 | D3 packet counts (20 lexemes, 6 replayed names, 2 variants, 4 costume cases, 5 bridges) | packet regenerates byte-identical (`--check` exit 0) | counts not re-derived (byte-identical by construction) |
| 104 | round-8 acceptance "exits 0" | exit 1 at HEAD **and** at `e1694ba`; F pass, O pass, D fail | **stale** (F12-05) |

## Findings

**F12-01 — no-arg gate battery exits 2 (2 of 7 gates have no committed baseline).**
`python3 tools/check-gate-battery.py` → exit 2; duty 1 `pass 7 / fail 0 / unevaluable 0`,
`originals preserved: true`; duty 2 `baselines_found 5, pinned 5, gates_covered 5`,
`gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]`, two
`BASELINE-GATE-UNCOVERED` findings (fail-closed per contract §6). The two missing pins exist
only under `reports/round-9/baselines/<gate>/expected.json`, outside both declared roots
(`tools/gates/expected`, `tools/gates/frozen`) — `find . -name expected.json` sweep lists
exactly 5 in-root pins plus those two out-of-root files.
**Already documented**: `reports/round-9/baselines/registry.md:173` records this exact exit-2
invocation and cause. **Gap**: `SCORECARD.md:52` presents the command with no caveat, and
`SCORECARD.md:144` ("7/7 with expected.json baselines", shard 13's row) is not what the
committed no-arg command shows. Disposition: document the caveat in the row, or commit the
two pins under a declared root (then re-run #13 must be exit 0).

**F12-02 — round-5 acceptance command is revision-scoped.**
Exit 1 at HEAD: `F: "non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')"`,
`O: "['/usr/bin/python3', 'tools/check-gate-battery.py']: expected 0, got 2"` (cascade of F12-01).
Green at its own work commit `9c52635` (exit 0). The committed `reports/round-5/validation.json`
is the green run (blob `78444f4cca7497da34f9f8b3dfbe54998b1bace6b8e22731cf11bbd9f2e7ae44`), so
`SCORECARD.md:30–35`'s "re-run command" is only valid at that revision. Disposition: document
(revision-scoped re-run; the pinned path is the isolated export round-6's runner builds).

**F12-03 — round-6 acceptance command is revision-scoped.**
Exit 1 at HEAD: `"append-only prefix lost: SKILL.md"` — `SKILL.md` is in round-6's
`APPEND_ONLY` set (`reports/round-6/run-validation.py:25`), and later rounds edited it in place
(round-8's label-typing table, round-9's additions). Green at `b815bf4` (exit 0). Committed
`reports/round-6/validation.json` is green. Disposition: document; do not rewrite the filed
bytes.

**F12-04 — round-7 acceptance is red at filing and accumulates more failures at HEAD.**
Filed `reports/round-7/validation.json` (red) lists 2 failures; the HEAD re-run lists 4:
the same 2 (`claim F: wrong rejection for duplicate-parent-receipt-does-not-inflate: parent
check identity collision`; `previous_acceptance: previous round-6 acceptance failed`) **plus**
`preservation: append-only prefix lost: SKILL.md` and `inventory: historical knowledge totals
changed: {files 179, raw_lines 610, raw_occurrences 616, ci_occurrences 618, marker_occurrences 584}`.
So round-7's runner red is honest, but its failure set grows each round. Disposition: document
(pin-scoped), no repair of filed bytes.

**F12-05 — round-8 acceptance does not reproduce from any committed revision (strongest finding).**
At HEAD and at its own admission commit `e1694ba` the runner emits **byte-identical** output
(`b2fb9893…`): `claim F: PASS`, `claim O: PASS`, `claim D: FAIL` —
`"no D2 frozen replay without digest drift: … {rows: 7, reproduced: 0, mismatch: 0,
could_not_evaluate: 7, exit: 2}"`.
Mechanism, verified by hash: the D check (`replay_isolated()`,
`reports/round-8/run-validation.py:1224`, body to `:1240`) restores `tools/gates/*.py` **from HEAD** and
replays `tools/gates/frozen/round-3/MANIFEST.tsv`, whose pinned gate sha256s equal the
pre-repair bytes at `30caac6`:

| gate | round-3 pin (= `30caac6`) | `e1694ba` = HEAD |
|---|---|---|
| costume-era-consistency-gate.py | `29a9361c…` | `e6bffd70…` |
| myth-consistency-gate.py | `26d246e9…` | `5368b135…` |
| naming-collision-gate.py | `8c5afb0a…` | `d9e4e8f4…` |
| phonology-sanity-gate.py | `fb05c644…` | `d5fe087f…` |

The filed green `reports/round-8/validation.json` recorded `accepted: "isolated-pinned-revisions"`,
`gates_restored_from_head: 7`, `reproduced: 7/7` — reproducible only while HEAD still held the
pre-repair gate bytes, i.e. from a working tree whose HEAD predated the repair commit that
shipped the same validation file. The underlying pin drift is documented
(`reports/round-9/d3/replay.md:19`, `reports/round-9/d3/findings.md:95`,
`reports/round-9/report-draft.md:167`), but the consequence for round-8's own acceptance
command — `SCORECARD.md:104` "exits 0" is false at every committed revision — is not recorded
anywhere. Disposition: fix-with-control (a pinned-revision re-run path, e.g. restore gates from
a named pre-repair revision) or documented wont-fix with that reason; either way `SCORECARD.md:104`
needs the caveat.

**F12-06 — "both round-3 manifests reproduce 7/7" no longer holds live.**
`python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json` → exit 2,
`{rows: 7, reproduced: 0, mismatch: 0, could_not_evaluate: 7}`; `attempt-1` identical.
Same cause as F12-05 (round-8 gate repairs vs round-3 gate pins). Green at `9c52635`.
Filed round-5 validation records `round3_replay: "7/7"`. **Already documented**:
`reports/round-9/d3/replay.md:19` ("round-3 7/7 `gate_digest_mismatch` exit 2; attempt-1 same
… fail-closed; round-8 gate repairs drifted those pins") and
`reports/round-8/operability/neg-controls/neg-09/` ("the replay tool correctly refuses (exit 2)
instead of replaying unpinned code"). **Gap**: `SCORECARD.md:32`'s capability-row claim carries
no revision scope, and `SCORECARD.md:30`'s "D2 still 20 findings" is unverifiable while this
replay is red. Disposition: document (superseded by the r9-pre pin system).

**F12-07 — stale counts in the round-5/round-6 rows.**
(a) `SCORECARD.md:32` "battery 10/10 controls" → battery selftest now reports **28/28**
(round-9's battery extension; `reports/round-9/baselines/battery-extension.md`).
(b) `SCORECARD.md:34` "592 raw marker-bearing lines, 598 raw occurrences" → current inventory
`raw_lines 610 / raw_occurrences 616 / marker_occurrences 584`; the same drift is already
recorded in `reports/round-9/metadata/audit.md:129` (`raw_lines=610 raw_occurrences=616
markers=584`) and is what makes round-7's runner fail (F12-04). Disposition: document; the
round-5 numbers are a historical snapshot, not a current observation.

## Concurrency and boundaries

- The lane working tree was being written by other round-10 workers during this shard:
  observed ` M corpus/README.md`, ` M reports/round-5/validation.json`,
  ` M reports/round-9/validation.json`, plus untracked `reports/round-10/coverage/` and
  `reports/round-10/findings-tracker.json`. An in-tree re-run of `reports/round-5/run-validation.py`
  by another worker (mtime 18:27) left the same two failure messages this shard reproduced in
  isolation; by 18:29 the file was back to the committed blob `78444f4c…`. All evidence here
  therefore comes from immutable clones of `e3a1ec9`, not from the moving working tree.
- Contamination control: in the first (shared) clone, round-8's O claim failed only because the
  earlier round-7 run had rewritten `reports/round-7/validation.json` ("round-7 filed artifacts
  were edited"). The per-round fresh-clone runs are the canonical ones; that O failure is an
  artifact of sequential runs, not drift.
- Out of this shard (lines 106–210 → shard 13): round-8 table commands (`tools/d2-typed-labels.py
  --selftest`, `tools/assemble-d2.py --check`, `source-audit-inventory --json --summary --root`,
  `check-gate-battery.py --selftest`, `reports/round-8/run-validation.py`, `git status` scope
  read), round-9 table commands (`assemble-culture-d3.py --check`, `check-evidence-coupling.py
  --selftest`, round-9 validation, `read reconciliation.json`), the round-5 routing-history
  `python3 -c` one-liner (line 201), and `reports/round-9/baselines/registry.md`.
- Related out-of-shard datum gathered here as a control: `python3 reports/round-9/run-validation.py`
  in a fresh clone of HEAD exits **0** (`claim F: PASS / O: PASS / D: PASS`), i.e. the current
  r9-pre pin system is green while the legacy round-3 pins are red.
- Limits: this shard re-runs commands and compares outputs; it does not re-derive the round-5/6/7
  research verdicts, does not certify source truth, and does not fix anything (F15–F18 own the
  stale items). Output sha256 values embed clone paths for path-bearing outputs (documented above).

## Cross-references (added after this fragment landed)

- `reports/round-10/drift/ledger.json` was written at 18:34, before this fragment (18:36), and
  already carries rows for the same commands from shards 11/13 and fixer R10-F15-battery:
  `SCORECARD.md:30,32-35` (round-5 runner), `:65-70` (round-6), `:92-93` (round-7), `:104`
  (round-8), `:52` (no-arg battery) — all `stale-documented` — plus shard-13's
  `SCORECARD.md:114,115,116` row for the round-8 runner as `stale-fixed` (pre-fix observation,
  stale item S13-1). This fragment corroborates those rows independently; it contradicts none.
- Delta this fragment adds: the round-8 runner's failure is byte-identical at its **own admission
  commit** `e1694ba` (`b2fb9893…`), not only at HEAD — its filed green `validation.json` was
  never reproducible from a committed revision — and the pin-hash table above names the four
  gates whose repair invalidated the round-3 pins.
- A fixer has since modified `reports/round-8/run-validation.py` in the lane working tree
  (` M reports/round-8/run-validation.py` at 18:36). Every measurement here is of the committed
  bytes at `e3a1ec9`; post-fix behavior must be re-measured by the verifier, not assumed.
- Also in the lane tree at 18:36: ` M SKILL.md`, ` M corpus/README.md`, ` M reports/round-9/validation.json`
  and nine new untracked `corpus/knowledge/**` entries — concurrent round-10 work, not this shard's.
