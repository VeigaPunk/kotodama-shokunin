# R11-D25 — scribe: frozen-manifest records (claim D, `d2-typed-pipeline`)

- seat: **R11-D25** (scribe, frozen-manifest records), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D25 (scribe): frozen-manifest records; reports/round-11/depth/frozen-records.md."
- writes: **this file only** (scratch under `.scratch/d25/`, gitignored). No tool, gate, packet, component, baseline, manifest or earlier-round byte is edited by this seat. `reports/round-{8,9,10}/**` are filed and read-only here.
- clock: all stamps UTC (`date -u +"%FT%TZ"`); local time is UTC-03:00. Measurement window **2026-10-17T22:00–22:05Z**; lane revision `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (`e3ef171`, the round-11 claims commit; `git rev-parse HEAD` 22:04Z) with the wave's untracked worker output present.
- canon: NON-CANON engineering record. Nothing here admits a round, a capability, or a canon fact. This file records bytes and verdicts; it does not bless a re-pin — that is the parent's integration decision.
- prior record this file supersedes for round-11 purposes: `reports/round-8/depth/test-replay.md` §6 named the re-pin shape and left it to the round's scribes; `reports/round-10/drift/fix-18.md` recorded the live `exit 2` state. This file re-measures both and inventories **every** frozen surface in the lane.

## 0. State at a glance (readings 2026-10-17T22:00–22:17Z at rev `e3ef171`; each row names its time — the wave wrote throughout, §9)

| # | surface | family | reading | class |
|---|---|---|---|---|
| 1 | `tools/gates/frozen/round-3/MANIFEST.tsv` (7 rows) | legacy TSV replay | `replay exit 2`, 7/7 `gate_digest_mismatch`, 0 gates launched | **RED-could-not-evaluate** — gate pins name round-1 bytes; snapshots and outputs intact |
| 2 | `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` (7 rows) | legacy TSV replay | same, exit 2, 7/7 `gate_digest_mismatch` | **RED-could-not-evaluate** |
| 3 | `tools/gates/frozen/round-4/` (5 `.out`, no manifest) | unpinned outputs | `replay exit 2`, `manifest_unreadable` | **no manifest** |
| 4 | 7 × `expected.json` baselines `r9-pre` (8 files, dual home ×1) | standard §3 frozen run | all gate pins + input pins **digit-match**; battery `pinned 8/8` with the round-9 root, `5/5` on default roots | **GREEN-pinned** |
| 5 | `examples/culture-d3/expected.json` (guard freeze, 24 entries) | evidence-coupling snapshot | 24/24 entries match; `--frozen` replay exit 0, findings `[]` | **GREEN** (round-9 refresh at `9dc18ec`) |
| 6 | typed-label projection `examples/culture-d2/typed-labels.d2.yml` | re-emitted mid-flight | at the first stamp `--check` **exit 1** (embedded `8da90b07…` ≠ packet `e0f21509…`); after the D worker re-emitted it (22:13Z) `--check` **exit 0**, digest now `a3aa452c…` | **RESOLVED mid-flight** (see §5, §9) |
| 7 | `tools/gates/frozen/README.md` index | standard §3 index | **absent** (`ls` 22:02Z) | **gap** |
| 8 | handoff-exercise freeze (**landed 22:08Z at `tools/gates/expected/handoff-exercise/r11/`, relocated 22:13Z to `reports/round-11/handoff/expected.json`**) | exercise baseline, profile `kotodama-handoff-exercise/1` | own freeze.txt: gate exit 0, `fields=16/16 glossary-entries=20 findings=0`; while it sat under `tools/gates/expected/` the battery read it `no baseline` + 7 findings and the 3-root battery exit moved 0 → 2; **after the move the battery reads its old 8/8-pinned / exit 0 again** | **relocated — record in §3.2** |
| 9 | `tools/gates/frozen/round-11/` (**the D8 re-pin generation, landed 22:13:56Z**) | legacy TSV replay, new generation | `MANIFEST.tsv` `4ddb911c…`, 10 rows; replay **10/10 reproduced, exit 0** — but **only with `TMPDIR` outside the repo**; with the lane's `TMPDIR=$PWD/.scratch` all 10 rows read `mirror_unsafe`, exit 2 | **GREEN (conditional) — §6.5** |
| 10 | `examples/culture-d2/packet.d2.typed.yml` (new live artifact, untracked at 22:15Z) | typed packet, replay input of row-set 9 | live digest `e8a83445…` = generation snapshot pin; `tools/typed-gate-flow.py --check` exit 0 ("byte-identical deterministic derivation") | **new input surface — §6.5** |

Claim D (`reports/round-11/claims.json`) requires "frozen replay re-pinned and green". At the first stamp **no re-pin generation existed**: `find tools/gates/frozen -mindepth 1 -maxdepth 1 -type d` → `round-3  round-4  handoff-packet-check  lexicon-coverage-audit  provenance-audit` (22:02Z). Mid-flight the wiring, its freeze entry point and then the generation itself landed: `tools/typed-gate-flow.py` (`--freeze [DIR]`, default `tools/gates/frozen/round-11`) and `tools/gates/frozen/round-11/MANIFEST.tsv` (`4ddb911c…`, written 22:13:56Z; `reports/round-11/depth/design.md` §5.2 had fixed this shape). First replay of it: **10/10 rows reproduced, exit 0** with an out-of-repo `TMPDIR` (`TMPDIR=/home/vgpnk/k11d25-scratch python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv`, 22:14Z) and **10/10 `mirror_unsafe`, exit 2** with the in-repo scratch root (§6.5) — the claim-D "green" therefore carries a condition the round must state. Re-pin worksheet, the landed-generation record and the green-verification protocol: §6, §6.5, §7.

## 1. Sweep — every frozen surface in the lane (commands + results)

### 1.1 The sweeps

```sh
find tools/gates/frozen tools/gates/expected -name 'MANIFEST*.tsv' -o -name 'expected.json' | sort   # 22:01Z
find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path './.scratch/*' | sort                 # 22:04Z
find . -name 'expected.json' -not -path './.git/*' -not -path './.scratch/*' | sort                 # 22:04Z
grep -rln 'typed-labels\|typed_labels' tools/gates/frozen tools/gates/expected reports/round-9/baselines   # 22:03Z
ls tools/gates/frozen/README.md                                                                      # 22:02Z — absent
```

### 1.2 The inventory

- **Legacy replay manifests** (`replay-frozen.py` TSV schema): exactly two — `tools/gates/frozen/round-3/MANIFEST.tsv` (`d5337590…`, 3587 B) and `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` (`613e5945…`, 3726 B). Both grade `examples/culture-d2/packet.d2.yml` (5 rows) + `provenance-audit` over two corpus files (2 rows).
- **Standard §3 baselines** (`expected.json`, schema `kotodama-frozen-run-v1`): 8 files, 7 ids (all `r9-pre`) at the 22:02Z stamp; homes: `tools/gates/expected/{costume-era-consistency-gate,phonology-sanity-gate}/r9-pre/`, `tools/gates/frozen/{handoff-packet-check,lexicon-coverage-audit,provenance-audit}/r9-pre/`, `reports/round-9/baselines/{handoff-packet-check,myth-consistency-gate,naming-collision-gate}/` — details §3. Mid-window the exercise shard added a ninth `expected.json` under a §3 root that is **not** this schema (`tools/gates/expected/handoff-exercise/r11/`, profile `kotodama-handoff-exercise/1`) — recorded in §3.2, not counted in §3's 8/8.
- **Guard freeze**: `examples/culture-d3/expected.json` (schema `kotodama-d3-evidence-coupling/1`) — §4.
- **Unpinned historical outputs** (no manifest, no `expected.json`, read-only records): `tools/gates/frozen/round-4/*.out` (5 files; §2.4) and `tools/gates/frozen/round-3/selftests/*.out` (6 files, the round-3 capability receipts: costume `0c2ed631…`, lexicon `fd731b14…`, myth `befd8c18…`, naming `d3566a9c…`, phonology `3b6ad32a…`, provenance `972306c1…`).
- **Index**: `tools/gates/frozen/README.md` does **not** exist, though the standard §3 layout requires an index (“baseline id → gate, revision, verdict class”). Recorded as a standing gap, not created here (not this seat's file).

### 1.3 Scratch duplicates (not live surfaces)

`reports/supplement-opencode-1/scratch/29-local-boundaries/{baseline,exp-asm,exp-selftest}/tools/gates/frozen/round-3/…` each carry copies of both round-3 manifests; digests equal the lane files (`d5337590…`, `613e5945…`) when checked for the `baseline` tree (22:04Z). The directory is gitignored (`/reports/supplement-opencode-1/scratch/` in `.gitignore:5`). They change no reading above; they are named here so a later sweep is not surprised by them.

## 2. Legacy replay manifests — records

### 2.1 Schema and mechanics (as implemented)

Columns (`tools/gates/frozen/round-3/MANIFEST.tsv:1`): `gate  gate_sha256  input  input_sha256  exit_code  finding_count  output  output_sha256  input_snapshot  command`. `tools/replay-frozen.py` (`a2fb5c98…`) verifies `gate_sha256`, the snapshot's `input_sha256` and the output's `output_sha256` **before** launching; it never parses the `command` column; it runs `[python3, <pinned gate>, <input>]` from a verified temp mirror and compares observed exit code, `^FINDING ` count and output bytes; exit 0 = reproduced, 1 = mismatch, 2 = could-not-evaluate (`tools/replay-frozen.py:1-50` docstring). Tool selftest: `python3 tools/replay-frozen.py --selftest` → `selftest: 79/79 checks passed`, exit 0 (22:01Z).

### 2.2 `round-3/MANIFEST.tsv` — per-row pin record (measured 22:01Z)

Gate pins all name the round-1 bytes: each pinned digest equals `git show 291c714:tools/gates/<gate>.py | sha256sum` (verified for all six gates; `291c714` = "round 1 (admitted): 6 verification gates executable + 463 to-verify flags triaged", 2026-10-17 10:54:46 −0300). Manifest committed at `c610e0a` (round 3, 12:01:50 −0300).

| row | gate | pinned `gate_sha256` (round-1) | on-disk now | snapshot pin (`input_sha256`) | snapshot intact | recorded verdict | output pin intact |
|---|---|---|---|---|---|---|---|
| 2 | `phonology-sanity-gate.py` | `fb05c644cafb0855…` | `d5fe087ffb2342e5…` | `54be6319e4907d20…` (144270 B packet) | yes | exit 1 / 3 findings | yes (`1ce5f0cd…`, 654 B) |
| 3 | `lexicon-coverage-audit.py` | `63ee4ec6b15188fe…` | `2c4dd39702a15ea3…` | `54be6319e4907d20…` | yes | exit 0 / 0 | yes (`e3b0c442…`, 0 B) |
| 4 | `myth-consistency-gate.py` | `26d246e9936db437…` | `5368b13542cd4b8a…` | `54be6319e4907d20…` | yes | exit 1 / 1 | yes (`ea56c2d36…`, 852 B) |
| 5 | `costume-era-consistency-gate.py` | `29a9361c7b96a354…` | `e6bffd7020c0b116…` | `54be6319e4907d20…` | yes | exit 1 / 10 | yes (`129c4f5a…`, 990 B) |
| 6 | `naming-collision-gate.py` | `8c5afb0a5abc8b00…` | `d9e4e8f4f93a21b3…` | `54be6319e4907d20…` | yes | exit 1 / 20 | yes (`e81bab66…`, 4213 B) |
| 7 | `provenance-audit.py` | `4aaea6e98b977692…` | `8a96aaf4ccd14ef4…` | `a916a4c2dd30d1a8…` (mesoamerica, 32633 B) | yes | exit 0 / 0 | yes (`57a537ae…`, 173 B) |
| 8 | `provenance-audit.py` | `4aaea6e98b977692…` | `8a96aaf4ccd14ef4…` | `7b3bdc80a12ba509…` (standard, 21446 B) | yes | exit 0 / 0 | yes (`1b8bf0b8…`, 165 B) |

Snapshot and output pins verify 7/7 and 14/14 respectively (digest comparison, `.scratch/d25/inventory.txt`; the out/excerpt digests above are the record verifying). The **only** stale pins are the six gate pins. Full digests live in the manifest and in `.scratch/d25/inventory.txt`; ellipses above are display-only.

**Live-input drift (targets, not pins):** `examples/culture-d2/packet.d2.yml` now `e0f21509…` (156071 B) vs pinned snapshot `54be6319…`; `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` now `6d40a97d2b02…` vs pin `a916a4c2…`; `corpus/knowledge/verification/gate-frozen-run-standard.md` now `7eb2635b…` vs pin `7b3bdc80…`. The replay design never reads the live input (proved by round-8 control C4, `reports/round-8/depth/test-replay.md` §4), so these do not move any verdict; they matter only to a future re-pin, which must copy the **current** bytes.

### 2.3 `round-3/attempt-1/MANIFEST.tsv` — per-row record

Same gate pins and same output pins as round-3 for six of seven rows; differences:

| item | round-3 | attempt-1 |
|---|---|---|
| packet snapshot | `54be6319…` (144270 B) | `f424fcf1…` (144164 B) |
| costume row verdict | exit 1 / 10 findings, `129c4f5a…` | **exit 2 / 1** finding, `b496f820…` (65 B) |
| commit | `c610e0a` (12:01:50 −0300) | `c610e0a` (same commit, `git log -1` 22:04Z) |

Both manifests replay identically today: **exit 2, 7/7 `could-not-evaluate reason=gate_digest_mismatch`, 0 gates launched** (`python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv [--json]`, 22:01Z, 22:04Z and 22:07Z; receipts `.scratch/d25/replay-round3.json`, `.scratch/d25/replay-attempt1.json`, `.scratch/d25/replay-{round3,attempt1}.stdout`). The plain-text stdout is **byte-identical to the round-10 record**: round-3 stdout sha256 `76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80`, attempt-1 stdout sha256 `409db5ab8b68ebc3da9a8360879db71c01e58b40ea4a8311e3818efe289c8452` — both equal the ledger entries `R10-F18-01`/`R10-F18-02` (`reports/round-10/drift/ledger.json`, re-quoted in `reports/round-10/drift/fix-18.md:21,25`), so the reading is stable across ~3.5h and two rounds. Note for the record's own limits: sha equality here is comparison, not endorsement; the round's re-pin (§6) is still owed.

### 2.4 `round-3/…` is not the only legacy state — `frozen/round-4/` has no manifest

```sh
python3 tools/replay-frozen.py tools/gates/frozen/round-4/MANIFEST.tsv   # 22:01Z
# COULD-NOT-EVALUATE manifest_unreadable: manifest: [Errno 2] No such file or directory: ...   → exit 2
```

`tools/gates/frozen/round-4/` holds five outputs and nothing else (commit `fe34faa`, round 4): `naming-collision-gate.out` `4d70252b…` (4072 B), `phonology-sanity-gate.out` `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` (654 B — byte-identical to the round-3 phonology output pin), and three zero-byte outputs (`costume-era-consistency-gate.out`, `lexicon-coverage-audit.out`, `myth-consistency-gate.out`, all `e3b0c442…`). No pins, no revision, no verdict record: these files are historical output bytes only, admissible to nothing.

## 3. Standard §3 baselines (`expected.json` family) — records (22:02Z)

All eight files were read field-by-field; gate pins compared to on-disk digests; every `inputs` entry re-hashed at its baseline home. **Result: 8/8 gate pins match, 100% of input pins match** (`.scratch/d25/inventory.txt`).

| baseline home | `expected.json` sha256 | gate | `revision` | gate pin | inputs | expected verdict | `stdout_sha256` |
|---|---|---|---|---|---|---|---|
| `tools/gates/frozen/handoff-packet-check/r9-pre/` **and** `reports/round-9/baselines/handoff-packet-check/` (byte-identical dual home) | `9dc21cd508e3dcfb225564cdccf65a8f88d9768029e876ac7e47d4c55f21c690` | handoff-packet-check | `a7bb205d…` | `e2fa3223…` = disk | `packet.md 0d8d660b…` | clean, exit 0, `[]` | `7c581047…` |
| `reports/round-9/baselines/myth-consistency-gate/` | `a87edc5327112367e310c6ff3b24bf099e704e0109e278f1c04e0443db5215b4` | myth-consistency-gate | `a7bb205d…` | `5368b135…` = disk | `packet.yml e0f21509…` | clean, exit 0, `[]` | `e3b0c442…` (empty run.log) |
| `reports/round-9/baselines/naming-collision-gate/` | `2f34ee1802b37df195e3e05fc7647a6506843d8e74d1cf74d7b32217ec4b9a45` | naming-collision-gate | `e1694bad…` | `d9e4e8f4…` = disk | `packet.yml e0f21509…` | findings, exit 1, `[CROSS-HOLD, NAME-NEAR, PHON-INVENTORY]` | `ebc8850d…` |
| `tools/gates/expected/costume-era-consistency-gate/r9-pre/` | `7ec01a1dce6182db329233594563dc31d52ce9d4c4cb9c89bc64e693e992c689` | costume-era-consistency-gate | `a7bb205d…` | `e6bffd70…` = disk | `packet.yml 36d92113…` | findings, exit 1, 21 ids | `482c1597…` |
| `tools/gates/expected/phonology-sanity-gate/r9-pre/` | `2763614ff26959e6b7fa7d96471e8d5e9e93616e37d47e3f0bec99b5caa62cde` | phonology-sanity-gate | `e1694bad…` | `d5fe087f…` = disk | `packet.yml e0f21509…` | findings, exit 1, `[A-NEUTRAL]` | `1ce5f0cd…` |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/` | `0fad58ba70d545328d015990de5184bdd371e575810eb7e79c96bcc7c8a4ff9c` | lexicon-coverage-audit | `e1694bad…` | `2c4dd397…` = disk | `packet.yml a1b8ed7c…` (+`digests.sha256`) | findings, exit 1, 18 ids | `af579495…` |
| `tools/gates/frozen/provenance-audit/r9-pre/` | `425c74c084bb53bdf8aff8d4f143a6cbe062421e1362f234e5fe702463f95e87` | provenance-audit | `a7bb205d…` | `8a96aaf4…` = disk | 20 files, all match | findings, exit 1, 6 ids | `26f21741…` |

Notes recorded with the table:

- The **dual home** is one baseline id, not two freezes: both copies of the handoff baseline verify byte-identical (`expected.json` `9dc21cd5…` and `freeze.txt` `f83ac075…` in both roots; 22:04Z). Round-9's `freeze.txt` states the never-divide rule verbatim.
- `run.log` files are gitignored (`.gitignore:3` → `*.log`); any later commit of a re-pin's `run.log` needs `git add -f` (noted in round-9's handoff `freeze.txt` and still true).
- The two `reports/round-9/baselines/`-only homes (myth, naming) are the reason the battery's default roots leave two gates uncovered (§3.1).

### 3.1 Battery readings — both root sets (22:02Z)

```sh
python3 tools/check-gate-battery.py                                                            # default roots, 22:02Z
#   summary: baselines_found 5, pinned 5, gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py], baseline_exit 2
python3 tools/check-gate-battery.py --baselines-root tools/gates/expected \
  --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines              # 22:02Z
#   summary: baselines_found 8, pinned 8, gates_uncovered [], baseline_exit 0; all 7 gate selftests pass
```

Receipts: `.scratch/d25/battery-default.json`, `.scratch/d25/battery-3roots.json`. The battery verifies digests and pins **only** (`verdict_replay: "not-run"` in both receipts); the verdict half of each baseline is its own re-run record, not the battery's.

**Re-measured at 22:16Z, after `tools/gates/expected/handoff-exercise/r11/` landed (see §3.2):**

```sh
python3 tools/check-gate-battery.py                                     # default roots, 22:16Z
#   baselines_found 6, pinned 5, readings {pinned: 5, no baseline: 1}, unevaluable 1, gates_uncovered [myth, naming], baseline_exit 2
python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen \
  --baselines-root reports/round-9/baselines                            # 22:16Z
#   baselines_found 9, pinned 8, readings {pinned: 8, no baseline: 1}, unevaluable 1, gates_uncovered [], baseline_exit 2
```

The 3-root reading moved **0 → 2** solely because the new exercise baseline is not a `kotodama-frozen-run-v1` document (`readings: {"no baseline": 1}`); receipts `.scratch/d25/battery-default2.json`, `.scratch/d25/battery-3roots2.json`.

### 3.2 Mid-flight: the handoff-exercise freeze (`tools/gates/expected/handoff-exercise/r11/`, landed 22:08Z)

Landed by the O-claim exercise shard while this record was being written; recorded here as a frozen surface because it sits at a standard §3 root and pins live artifacts. Facts only — its design and verdict belong to claim O and the parent, not this seat.

| file | sha256 |
|---|---|
| `expected.json` (4 354 B) | `1ab17670c113bf5f10a80f5ba564b252d948a836c3793efe641c68154d286b33` |
| `freeze.txt` (280 B) | `003fe548222a9315046dde149152be8f92a4be1f882f1c0e03cc17fac2ca4230` |
| `packet.md` (22 975 B) | `2a058f7858127b98592439594c55974d93e6e672a600dd2036b47e21e71c8a63` |
| `run.log` (421 B) | `2346783b8d6b76058324a66b56658f07c4fb5d3b80fdc8523fa40b64a60db35a` |

What it recorded at that home (read 22:16Z): profile `kotodama-handoff-exercise/1`; frozen by `tools/exercise-handoff-e2e.py` (`38d1cba4…` at freeze time); `declared.expected_exit 0`, `fields_expected 16`, `glossary_entries_expected 20`, `finding_ids []`; `cross_refs.gate_exit 0`, `gate_fields 16/16`, `gate_glossary_entries 20`, 13/13 component digests matched; per-field digests for all 16 envelope fields; `inputs` pin `examples/culture-d2/packet.d2.yml e0f21509…`, `examples/culture-d2/typed-labels.d2.yml e70ba147…`, both D3 artifacts, and the worldbible contract `5f4c02bf…`; `packet_sha256 2a058f78…`.

Battery view while it sat under the §3 root (22:16Z, default and 3-root): **`no baseline`**, findings — `BASELINE-GATE-UNKNOWN` ("declared gate None is not one of the seven registered gates"), 5 × `BASELINE-EXTERNAL-INPUT` (its `inputs` resolve to live repo paths; §3 requires byte copies inside the baseline), `BASELINE-EXPECTED-ABSENT` ("no `expected` block") — and the 3-root battery exit moved **0 → 2** on this artifact alone (`.scratch/d25/battery-3roots2.json`).

**Relocation (22:13Z, recorded):** the directory no longer exists at the §3 root; the shard re-froze under its own evidence home as `reports/round-11/handoff/expected.json` (`c8abc7990bded965b376e85999224a67d349c5b2fdd81070a7c05eda6c09ad0b`, 5 338 B, `baseline_digest 751f36f6…`, packet.md 31 509 B, `packet_sha256 87523e3d…`) with sibling fragments (`design.md`, `contract-check.md`, `frozen-rerun.md`, tamper controls). Consequence, measured: the battery returns to its pre-episode readings — default roots `5 found / pinned 5 / exit 2 (2 uncovered)` (22:15Z, `.scratch/d25/battery-default3.json`); 3 roots `8 found / pinned 8 / uncovered 0 / baseline_exit 0` (22:15Z, `.scratch/d25/battery-3roots3.json`). The transient episode is recorded rather than erased: for ~5 minutes the lane's 3-root battery exit was 2 because of it, and any receipt from that window should be read with that knowledge.

One live-pin fact at hand-off: the relocated baseline's `inputs` still pin `typed-labels.d2.yml e70ba147…`, while the live artifact was re-emitted at 22:13Z to `a3aa452c…` (§5). That is standard freeze behaviour (the pin names the frozen bytes), but a re-run of the exercise against the live tree will see the input move; the exercise's `--freeze` “prints the old→new differences” by design (`--help`), so the O side can refresh deliberately. Recorded for the parent; not this seat's call.

## 4. Guard freeze — `examples/culture-d3/expected.json` (22:03Z)

- File sha256 `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc`; schema `kotodama-d3-evidence-coupling/1`; 24 manifest entries; `expected_exit: 0`, `finding_ids: []`.
- Entry check (this seat, per-entry loop): **24 entries, 24 match, 0 mismatch**.
- Replay: `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` → exit 0, `counts.total 0`, `findings []` (22:03Z).
- History: the round-9 replay record (`reports/round-9/d3/replay.md` §4) found the committed freeze **RED — 3 of 24 pins drifted** (worldbible contract, costume gate, naming gate, all edited by `e1694ba`). The current file was refreshed at `9dc18ec` ("round-9: admit F/O/D", 18:17:00 −0300) — `git log -1 -- examples/culture-d3/expected.json` (22:04Z). This is the lane's in-repo precedent for a **documented refresh** of a freeze after named input edits.

## 5. D2 typed-pipeline freeze surface (the claim-D target)

**Negative sweep (22:03Z):** `grep -rln 'typed-labels\|typed_labels' tools/gates/frozen tools/gates/expected reports/round-9/baselines` → **no hits**. No `MANIFEST.tsv` row and no `expected.json` input names the typed projection or `tools/d2-typed-labels.py`; the typed pipeline is frozen by nothing today. Also structural: `replay-frozen.py` whitelists gates as Python files directly under `tools/gates/`, so `tools/d2-typed-labels.py` **cannot be a replay row**; the replayable D2 object is the packet (`reports/round-8/depth/test-replay.md:121`).

**Stale embedded pin (measured 22:00Z):**

```sh
sha256sum examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml tools/d2-typed-labels.py
# e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643  packet.d2.yml      (156071 B)
# e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f  typed-labels.d2.yml (84614 B)
# 0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802  tools/d2-typed-labels.py
grep -n 'packet_sha256' examples/culture-d2/typed-labels.d2.yml   # line 9: "packet_sha256": "8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e"
python3 tools/d2-typed-labels.py --check examples/culture-d2/typed-labels.d2.yml   # exit 1 — differs from the deterministic projection
python3 tools/d2-typed-labels.py --emit .scratch/d25/typed-labels.fresh.yml       # exit 0; diff vs committed = the packet_sha256 line only; both files 84614 B
python3 tools/assemble-d2.py --check                                              # exit 0 — packet.d2.yml byte-identical deterministic assembly
```

Record: the committed projection embeds the **pre-`e1694ba`** packet hash `8da90b07…`; the packet itself was regenerated in `e1694ba` (2026-10-17 17:44:17 −0300, "re-pin repaired costume-gate reader") and the projection added in the same commit carried the older pin. A fresh `--emit` differs in exactly that one line. **Resolution observed mid-flight (22:13Z):** the D worker re-emitted the projection against the current packet — live digest now `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`, embedded `packet_sha256 e0f21509…`, and `python3 tools/d2-typed-labels.py --check` **exit 0** ("byte-identical deterministic projection", re-verified by this seat 22:14Z). The stale-pin defect is therefore closed on the working tree; it remains **uncommitted** (`git status` shows ` M examples/culture-d2/typed-labels.d2.yml` at 22:15Z), so the parent's commit carries the fix. This was also visible from the record side in `reports/round-11/depth/scribe.md` §1.2.

## 6. Re-pin worksheet — what a legitimate round-11 generation must pin

The lane's rules fix the *shape*: standard §3 “Append-only. A later gate revision or input edit produces a **new** baseline. Existing baselines are never rewritten”; round-8 §6 demonstrated the candidate build in scratch and named the target shape (new generation directory; old generations stay legible). Both the standard and `reports/round-8/depth/test-replay.md` §6 forbid editing `round-3`/`attempt-1` in place. So a round-11 re-pin is a **new generation** (e.g. `tools/gates/frozen/round-11/`), carrying:

**B1. Current on-disk digests to pin (measured 22:01–22:04Z; re-measure at freeze time — the wave is live):**

Round-11's intended generation is fixed in `reports/round-11/depth/design.md` §5.2 (22:12Z): a **new manifest** `tools/gates/frozen/round-11/MANIFEST.tsv` whose replay row runs the typed pipeline's gate-shaped entry point (the design says the entry point must sit directly under `tools/gates/` — satisfied by `tools/typed-gate-flow.py` per its usage text) over a frozen copy of the derived typed packet; green = `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` exits 0 (`design.md:330-349`). The build path exists: `python3 tools/typed-gate-flow.py --freeze [DIR]` writes a frozen replay generation, default `tools/gates/frozen/round-11` (`--help`, 22:12Z); **the generation was then written at 22:13:56Z — its record is §6.5**. design.md:410 assigns the artifacts to shard D08.

| artifact to pin | sha256 @ 22:0xZ |
|---|---|
| `tools/gates/phonology-sanity-gate.py` | `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230` |
| `tools/gates/lexicon-coverage-audit.py` | `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287` |
| `tools/gates/myth-consistency-gate.py` | `5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08` |
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `tools/gates/provenance-audit.py` | `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a` |
| input snapshot candidate — `examples/culture-d2/packet.d2.yml` (current bytes) | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `tools/replay-frozen.py` | `a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e436c79464` |
| `tools/check-gate-battery.py` | `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` |
| `examples/culture-d2/typed-labels.d2.yml` **(only after re-emit; currently fails `--check`)** | fresh emit at 22:03Z would carry `packet_sha256 e0f21509…`; the committed file is `e70ba147…` |
| `examples/culture-d3/expected.json` (if the re-pin touches the guard path) | `562b76cb…` |

**B2. Two admissible re-pin shapes** (pick one; record which):

1. **Snapshot-preserving re-pin** — new generation re-plays the *existing* round-3/attempt-1 snapshots (`54be6319…` / `f424fcf1…`) under the current gates, re-recording observed exit/count/output bytes; gate pins renamed to B1. This is round-8 §6's demonstrated candidate shape ("copying the round-3 manifest and rewriting only the `gate_sha256` column"; scratch run `REPLAY OK: 7/7`, exit 0, 20:17Z round-8). It answers "do the repaired gates reproduce the historical verdicts on the historical bytes?" — a verdict-preservation claim, not a current-bytes claim.
2. **Current-bytes re-pin** — new generation snapshots the *current* `packet.d2.yml` (`e0f21509…`) and the current gate revisions, records the observed verdicts fresh. This answers "what does the current D2 artifact produce under the current gates?" and is the version to cite for claim D if the typed wiring changes packet bytes. Its rows must record what is **observed** at freeze time (standard §5 step 5), not a hoped-for hold set.

**B3. Failure modes the new generation must not exhibit** (each already demonstrated caught by `replay-frozen.py`/`check-gate-battery.py` controls, replay record `reports/round-9/d3/replay.md` §2 controls C1–C4 and `reports/round-8/depth/test-replay.md` §4): snapshot tamper → exit 2 `snapshot_tampered`, no launch; output tamper → `expected_output_tampered`; gate tamper → `gate_digest_mismatch`; a row whose recorded verdict was edited to look clean while the gate still finds the hold → `exit 1` mismatch (exit 1 wins over 0; exit 2 wins over both).

**B4. Commit hygiene**: `run.log` needs `git add -f` (`*.log` ignored); the new generation needs its `tools/gates/frozen/README.md` index row (currently absent — creating the index is the integrator's write, not this seat's); the old `round-3`/`round-4`/`r9-pre` files stay byte-untouched (that is the anti-circularity pivot reviewed by R11-D22).

### 6.5 The landed generation — `tools/gates/frozen/round-11/` (first record, 22:14–22:15Z)

Written 22:13:56Z by the D8 build (`--freeze`), after this record's §6 worksheet. Freshness at recording: **every member is untracked at 22:15Z** (`git status --porcelain` → `?? tools/gates/frozen/round-11/`, `?? examples/culture-d2/packet.d2.typed.yml`, `?? examples/culture-d2/typed-gate.expected.json`, `?? tools/typed-gate-flow.py`), so the carrying commit does not exist yet and the "revision" the generation names is the working tree.

**Members (sha256):**

| path | sha256 |
|---|---|
| `MANIFEST.tsv` (3 760 B, 10 data rows) | `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376` |
| `inputs/examples/culture-d2/packet.d2.typed.yml` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` (= live `examples/culture-d2/packet.d2.typed.yml`, 158 129 B — byte-copy verified) |
| `inputs/examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `naming-collision-gate.out` (typed) | `feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9` |
| `phonology-sanity-gate.out` (typed) | `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` (byte-identical to the legacy phonology output) |
| `costume-era-consistency-gate.out`, `lexicon-coverage-audit.out`, `myth-consistency-gate.out` (typed) | `e3b0c442…` ×3 (zero bytes — clean at exit 0) |
| `legacy/naming-collision-gate.out` | `ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b` (byte-identical to the r9-pre naming baseline's `stdout_sha256`) |
| `legacy/phonology…`, `legacy/costume…`, `legacy/lexicon…`, `legacy/myth….out` | `1ce5f0cd…`, `e3b0c442…` ×3 |
| `typed-gate-flow.out` (2 197 B) | `4aa752b98b7ab9dbd8eaf4909ccefa6531c25ee31d99f9f7e474a91c5bf75db7` — **not referenced by any MANIFEST row** (unpinned output; it carries the typed pipeline's own finding set: 16 `FINDING` lines = 15 `[hold]` + 1 `[note]`, none `[fail]`) |

**Rows and replay.** 10 rows, all with `gate_sha256` equal to the on-disk gate digests recorded in §6 B1: five **typed** rows (`examples/culture-d2/packet.d2.typed.yml`, `e8a83445…`) — naming exit 1 / 7 findings, phonology exit 1 / 3, costume / lexicon / myth exit 0 / 0 — and five **legacy** rows (`examples/culture-d2/packet.d2.yml`, `e0f21509…`) — naming exit 1 / 17, phonology exit 1 / 3, costume / lexicon / myth exit 0 / 0. No `provenance-audit` row, and no row gate is `typed-gate-flow.py` (only the seven registered gates exist under `tools/gates/`; `ls tools/gates/*.py` 22:15Z). Both replays of this manifest were run by this seat:

```sh
# A — external TMPDIR (required):  GREEN
mkdir -p /home/vgpnk/k11d25-scratch
TMPDIR=/home/vgpnk/k11d25-scratch python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv    # 22:14Z
# REPLAY OK: 10/10 rows reproduced the recorded verdicts ... exit 0 — every row bytes=match, launched=yes
# B — the lane's scratch convention:  COULD-NOT-EVALUATE
TMPDIR=$PWD/.scratch python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv                # 22:14Z
# REPLAY COULD-NOT-EVALUATE: 10 could-not-evaluate, 0 mismatch, 0 reproduced — reason=mirror_unsafe on every row,
#   detail "mirror: temporary root is inside the repo: …/.scratch/replay-frozen-…", no gate launched, exit 2
```

Receipts: `.scratch/d25/replay-round11.json` (run A transcript captured to JSON; run B's rows are in the same file's first capture note) and the two command transcripts quoted above. **This is the single most operational finding of the record:** `replay-frozen.py` refuses a mirror inside the repo by design (round-8 history), while this round's worker instruction says `export TMPDIR=$PWD/.scratch` for scratch-writing commands. For manifests whose rows *could not evaluate* on pins (round-3), the difference is invisible — the run dies before the mirror. For a **green** manifest like round-11 it is decisive: the same command reads exit 0 or exit 2 depending only on `TMPDIR`. Claim D's "green" must therefore name its `TMPDIR` (an out-of-repo path), or the counting command will read exit 2.

Also measured: `python3 tools/typed-gate-flow.py --check` → exit 0, "typed gate artifacts: byte-identical deterministic derivation" (22:14Z); `examples/culture-d2/typed-gate.expected.json` exists (untracked) as the derived expected set with `expected_delta` naming the typed-vs-legacy differential (e.g. naming: typed 17 / legacy 17 with the ten `PHON-INVENTORY` legacy lines absent from typed). Whether the typed-pipeline output should itself be pinned by a row (design §5.2's wording) or the unpinned `typed-gate-flow.out` suffices is a D8/integrator call — recorded, not decided here.

## 7. Green-verification protocol (for the parent, once a re-pin lands)

Run, in order, on the settled tree; each leg states the reading that counts as green:

0. **Run replays with `TMPDIR` outside the repo** (e.g. `TMPDIR=$HOME/k11-scratch`); with the in-repo scratch root a green manifest reads exit 2 `mirror_unsafe` (§6.5 run B). Nothing else in this protocol is affected by that variable.
1. `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv [--repo-root <iso>]` → **exit 0** and `10/10 rows reproduced` (measured: true at 22:14Z, run A). A reproduced red row stays red: the claim is reproduction, not cleanliness.
2. Controls on an **isolated copy** (never the committed generation): append one byte to the snapshot → exit 2 `snapshot_tampered`, 0 launched; append a FINDING to one `.out` → exit 2 `expected_output_tampered`; edit one pinned gate → exit 2 `gate_digest_mismatch`.
3. `python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines` → as of 22:15Z: `baselines_found 8, pinned 8, gates_uncovered [], baseline_exit 0` (the exercise baseline's transient §3-root episode is over, §3.2). Default roots alone: `5 found / pinned 5 / 2 uncovered / exit 2` — unchanged since round 9 (§3.1).
4. `python3 tools/replay-frozen.py --selftest` → `79/79`, exit 0 (the checker itself unmodified; if it changed, the R11-D22 C4 co-change branch applies).
5. `python3 tools/d2-typed-labels.py --check` → exit 0 (measured true at 22:14Z after the D worker re-emitted the projection, §5).
6. `python3 reports/round-11/run-validation.py` (X03's file — now present, untracked at 22:15Z) carries claim D's counting command; its frozen leg should call leg 1 with leg 0's `TMPDIR`.
7. The D08 generation exists (§6.5): confirm its rows' `gate_sha256` still equal on-disk digests on the settled tree and that nothing in it is rewritten after this stamp; a rewritten row set is a new generation by the standard's append-only rule, not an edit.

## 8. Open items this record hands to the parent

| id | item | evidence | owner |
|---|---|---|---|
| FR-1 | ~~No re-pin generation exists yet~~ **Resolved mid-flight**: `tools/gates/frozen/round-11/` landed 22:13:56Z and replays 10/10 exit 0 with an external `TMPDIR` (§6.5). Remaining: commit it (all members untracked), add the `frozen/README.md` index row, and state the `TMPDIR` condition in the claim | §0, §6.5 | integrator + D08 |
| FR-2 | ~~Stale `packet_sha256` in the projection~~ **Resolved mid-flight**: re-emitted 22:13Z, `a3aa452c…`, `--check` exit 0 | §5, §9 | D implementation |
| FR-3 | The pipeline's own output (`typed-gate-flow.out`, 15 holds + 1 note) sits in the generation **unpinned by any row**; no gate-shaped `tools/gates/typed-gate-flow.py` exists, so the pipeline is not itself a replay row | §6.5 | D08 + integrator (pin it, or record the design choice) |
| FR-4 | `round-4/` frozen dir has outputs but no manifest → any replay attempt exits 2 `manifest_unreadable` | §2.4 | parent (leave as historical, or add a manifest generation) |
| FR-5 | Default-root battery leaves `myth` + `naming` uncovered (baselines live only under `reports/round-9/baselines/`) | §3.1 | parent |
| FR-6 | `tools/gates/frozen/README.md` index absent (standard §3 requires one); now also needed for the round-11 row set | §1.2, §6.5 | integrator write |
| FR-7 | `run.log` is `*.log`-ignored; re-pin commits need `git add -f` | §3 notes | integrator |
| FR-8 | Exercise baseline episode (§3.2): the transient §3-root copy read `no baseline` + 7 battery findings and moved the 3-root exit 0 → 2 for ~5 min; the relocated home `reports/round-11/handoff/expected.json` is outside the battery roots, so no current finding — but its input pin `typed-labels e70ba147…` now trails the live `a3aa452c…` (its own `--freeze` prints the diff by design) | §3.2 | claim O + parent |
| FR-9 | Every reading in this record was taken while the wave wrote; re-run §7 before citing claim D anywhere. The record's own §0/§3.2 carry three battery receipts (22:02Z, 22:16Z, 22:15Z) because the tree moved under them | §9 | integrator |
| FR-10 | **`TMPDIR` decides the replay verdict**: in-repo scratch root → `mirror_unsafe` exit 2 on all 10 rows; out-of-repo → 10/10 exit 0. Round-11's counting command and any replay receipt must name the `TMPDIR` used | §6.5 runs A/B | integrator + X03 (run-validation.py) |

## 9. Provenance

- Measurement window 2026-10-17T22:00–22:17Z at rev `e3ef171`, lane worktree with the wave's in-flight untracked output. Scratch receipts (gitignored, `.scratch/d25/`): `inventory.txt` (per-row/per-baseline digest comparison), `battery-default.json` / `battery-3roots.json` (22:02Z pre-exercise), `battery-default2.json` / `battery-3roots2.json` (22:16Z during the exercise-baseline episode), `battery-default3.json` / `battery-3roots3.json` (22:15Z post-relocation), `replay-round3.json` / `replay-attempt1.json` and the two stdout captures (sha `76c00a6b…`, `409db5ab…`), `replay-round11.json` (run A), `typed-labels.fresh.yml`, `marker` (poll reference). Scratch-writing commands ran with `export TMPDIR=$PWD/.scratch`; the one replay that needs an external mirror ran with `TMPDIR=/home/vgpnk/k11d25-scratch` (self-cleaning; created for that run, §6.5 run A).
- Live artifact digests at stamp: packet.d2.yml `e0f21509…`; packet.d2.typed.yml `e8a83445…`; typed-labels.d2.yml `a3aa452c…` (after re-emit); typed-gate.expected.json and typed-gate-flow.py present/untracked; d2-typed-labels.py `0da0015f…`; typed-gate-flow.py `--check` exit 0. Gate digests as in §6 B1; all seven gates unchanged from those pins at 22:15Z.
- Commands quoted verbatim above were each executed at the stamp shown; digests shown truncated with `…` are display-shortened only — full digests are in the cited files/manifests. Where a claim is another round's, it is cited by path (`reports/round-8/depth/test-replay.md` §4/§6, `reports/round-9/d3/replay.md` §2/§4, `reports/round-10/drift/fix-18.md`), not restated as this seat's measurement.
- The wave was live for the whole window: the D8 generation, the O baseline and the projection re-emit all landed while this record was being written, and the record says so at each point rather than presenting a settled tree. Every reading names its time; the parent must re-measure on the settled tree before admission, and re-read §6.5 if the generation changes after 22:14Z (the append-only rule makes any such change a new generation).
- This file is new; no earlier-round byte was touched (verified: `git status --porcelain` shows only the wave's untracked `reports/round-11/**` and new tools, plus pre-existing round-5..10 validation drift, none caused by this seat). File sha256 of this record is reported by the parent's integration step (it cannot name its own hash without self-reference).
