# R25-D20 — round-25 fragment ledger (read-time census)

- round: 25 (operator: loop 3 of 3, build round 1 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R25-D20** (D-scribe 3 of 3).
- date: 2026-10-18. Lane head `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`
  (declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`, round-24 admit).
- **writes: this file and its machine-readable twin
  `reports/round-25/scribe/fragment-ledger.json`**, plus gitignored scratch
  under `.scratch/r25d/`. No commit, no push; no filed artifact of rounds 8–24
  touched.
- canon: **NON-CANON integration ledger.** It admits nothing, certifies no
  round, and blesses no fragment. It is the index the parent uses to integrate
  the wave.

## 0. What this ledger is, and what it is not

A **read-time census** of every file under `reports/round-25/` at
**2026-10-18T17:33:18Z**, with byte size, line count, sha256 (8-char prefix
shown), mtime and an inferred owner seat, plus the two fragments that landed
**outside** that partition (`corpus/lessons/README.md`,
`corpus/lessons/round-25.md`) and the two **tool** artifacts the wave created
(`tools/gates/argot-derivation-gate.py` + its fixture pair,
`tools/gates/frozen/round-25/`).

It is **not** a completeness claim and **not** a round verdict. The wave was
still writing at the census: the round-25 tree went 2 → 13 → 29 → 39 → 40 → 42 →
49 → 51 → 59 files between 17:23Z and 17:40Z, and `tools/gates/typed-pipeline-gate.py` was
edited four times while this seat measured it. Re-run on the settled tree:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r25d/ledger.py   # or: re-run the census commands below
find reports/round-25 -type f | sort
ls corpus/lessons/README.md corpus/lessons/round-25.md
find tools/gates/frozen/round-25 -type f | sort
```

The machine-readable twin carries the same rows plus
`declared_baseline`, `lane_head`, `census_utc` and `counts`.

**Census stamps used in this file.** The §1 table was rebuilt at
**2026-10-18T17:40:52Z** (59 files) and supersedes the 17:33:18Z table (40
files) written earlier the same minute; the `.json` twin was regenerated at the
later stamp. Rows that changed between the two stamps are the wave's own
movement, not a re-measurement of the same bytes.

## 1. Census — `reports/round-25/**` (59 files, 2026-10-18T17:40:52Z)

| path | bytes | lines | sha8 | mtime UTC | owner seat (inferred) |
|---|---:|---:|---|---|---|
| `__pycache__/run-validation.cpython-314.pyc` | 81903 | 367 | `8d2259d6` | 17:39:36 | unattributed (path convention gives no seat) |
| `adjacency.md` | 19095 | 294 | `0d46cc5c` | 17:29:15 | X (adjacency scribe) |
| `argot/current-state.md` | 17885 | 312 | `6562f115` | 17:32:19 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/delta.md` | 29611 | 336 | `c4b6c47b` | 17:33:04 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/execution-1.md` | 5028 | 108 | `793400e5` | 17:30:30 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/execution-2.md` | 6458 | 124 | `53421b57` | 17:31:20 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/execution-3.md` | 9962 | 114 | `a187a3a2` | 17:32:26 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/execution-4.md` | 10776 | 173 | `8d6f0c21` | 17:32:21 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/forecast.md` | 9551 | 135 | `19b38555` | 17:27:58 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/review-1.md` | 26228 | 476 | `3ed7e98d` | 17:37:48 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/review-2.md` | 11836 | 218 | `0c115d18` | 17:36:24 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `argot/review-3.md` | 15715 | 270 | `20576a05` | 17:37:45 | D (argot analysis: R25-D01..D04, R25-D11..D14) |
| `audit/c31-lessons-index-audit.md` | 21803 | 371 | `f049daa4` | 17:36:39 | C (lessons index audit R25-C31..C34) |
| `audit/c31-lessons-index-audit.py` | 19406 | 464 | `dc3ee4cc` | 17:34:12 | C (lessons index audit R25-C31..C34) |
| `audit/c31-lessons-receipt.json` | 7673 | 349 | `24749f3e` | 17:36:26 | C (lessons index audit R25-C31..C34) |
| `audit/o18-gate-input-adversarial.md` | 14666 | 228 | `cb8480d3` | 17:34:17 | X/C (audit fragment) |
| `audit/o18-probe-matrix.sh` | 1239 | 20 | `05a7ee95` | 17:34:19 | X/C (audit fragment) |
| `audit/o19-supersession-honesty.md` | 11255 | 232 | `809aaa7e` | 17:40:50 | X/C (audit fragment) |
| `audit/o20-argot-leg-review.md` | 10711 | 200 | `71970193` | 17:40:31 | X/C (audit fragment) |
| `audit/x42-argot-execution-spotcheck.md` | 15052 | 237 | `aeafe8ec` | 17:31:13 | X/C (audit fragment) |
| `audit/x45-lessons-audit.md` | 16848 | 302 | `e8162709` | 17:39:14 | X/C (audit fragment) |
| `audit/x45-lessons-pointer-audit.py` | 10244 | 263 | `97c2a171` | 17:37:12 | X/C (audit fragment) |
| `audit/x45-lessons-pointer-receipt.json` | 1477 | 64 | `6669c3bd` | 17:38:44 | X/C (audit fragment) |
| `audit/x47-argot-negatives-audit.py` | 14478 | 368 | `2beaa81e` | 17:28:41 | X (argot negative-control audit R25-X47) |
| `audit/x47-argot-negatives.md` | 15308 | 257 | `7c7acca1` | 17:36:38 | X (argot negative-control audit R25-X47) |
| `audit/x48-v3-supersession-audit.py` | 15847 | 378 | `3cd3f3c9` | 17:31:33 | X (v3 supersession audit R25-X48) |
| `audit/x48-v3-supersession.md` | 10740 | 197 | `5451a892` | 17:39:26 | X (v3 supersession audit R25-X48) |
| `availability.json` | 14238 | 275 | `5ae22618` | 17:35:05 | dependency/availability seat |
| `claims.json` | 2979 | 32 | `bde84338` | 17:23:25 | declaration (parent) |
| `docs/derivation-relation-docs.md` | 21821 | 201 | `681cb202` | 17:36:08 | unattributed (path convention gives no seat) |
| `gate-input/design.md` | 21177 | 372 | `defa9cfc` | 17:34:38 | O (gate-input seats R25-O01..O03) |
| `gate-input/diagnosis.md` | 16449 | 297 | `4055f17b` | 17:34:50 | O (gate-input seats R25-O01..O03) |
| `gate-input/impl.md` | 14978 | 260 | `91573573` | 17:37:32 | O (gate-input seats R25-O01..O03) |
| `gate-input/verify.md` | 11167 | 192 | `7d3818ce` | 17:36:47 | O (gate-input seats R25-O01..O03) |
| `integration/log-draft.md` | 6546 | 95 | `7f01b86b` | 17:36:02 | unattributed (path convention gives no seat) |
| `integration/scorecard-draft.md` | 6373 | 72 | `c47b8eb6` | 17:36:22 | unattributed (path convention gives no seat) |
| `lessons/C25-C30.md` | 13685 | 231 | `8c5a9f28` | 17:30:11 | C (lessons index seats) |
| `lessons/census.json` | 33977 | 999 | `7e79f7c0` | 17:30:14 | C (lessons index seats) |
| `lessons/lessons-index-census.py` | 20221 | 447 | `23723db8` | 17:28:54 | C (lessons index seats) |
| `regression.md` | 17810 | 262 | `84ccd70c` | 17:40:36 | unattributed (path convention gives no seat) |
| `report-draft.md` | 8884 | 50 | `e5ee2f13` | 17:35:42 | unattributed (path convention gives no seat) |
| `rerun.json` | 25858 | 279 | `d3b8ad7e` | 17:35:32 | unattributed (path convention gives no seat) |
| `rule/skill-draft.md` | 21110 | 262 | `75a05a81` | 17:35:56 | unattributed (path convention gives no seat) |
| `run-validation.py` | 59639 | 1156 | `4cd6f066` | 17:37:59 | unattributed (path convention gives no seat) |
| `scope.md` | 10769 | 131 | `6cafe2c2` | 17:28:07 | X (scope watcher) |
| `scribe/capability-row.md` | 20837 | 286 | `03b477e5` | 17:34:22 | D/X (scribe seats; this file is R25-D20) |
| `scribe/fragment-ledger.json` | 0 | 0 | `e3b0c442` | 17:40:52 | D/X (scribe seats; this file is R25-D20) |
| `scribe/fragment-ledger.md` | 17994 | 260 | `b17e85a9` | 17:38:16 | D/X (scribe seats; this file is R25-D20) |
| `scribe/frozen-rows.md` | 16517 | 262 | `5f2a9ffd` | 17:37:09 | D/X (scribe seats; this file is R25-D20) |
| `scribe/x46-gate-input-cold-rerun.md` | 17758 | 317 | `726615e0` | 17:38:48 | D/X (scribe seats; this file is R25-D20) |
| `targets.json` | 217 | 11 | `309d9bc1` | 17:23:25 | declaration (parent) |
| `v3-supersession/build-revision.py` | 17560 | 149 | `f362d1f6` | 17:30:10 | O (v3 supersession seats) |
| `v3-supersession/declared-in-r4/expected.json` | 2715 | 55 | `c2d4eb7a` | 17:31:37 | O (v3 supersession seats) |
| `v3-supersession/declared-in-r4/freeze.txt` | 4724 | 22 | `6cc4fc2c` | 17:31:54 | O (v3 supersession seats) |
| `v3-supersession/declared-in-r4/packet.md` | 109817 | 338 | `5f58db4a` | 17:30:13 | O (v3 supersession seats) |
| `v3-supersession/evidence/check-receipt.json` | 12113 | 444 | `0bf2d586` | 17:38:40 | O (v3 supersession seats) |
| `v3-supersession/evidence/selftest-receipt.json` | 6069 | 261 | `c685d2c3` | 17:38:43 | O (v3 supersession seats) |
| `v3-supersession/evidence.md` | 10043 | 180 | `c74ee433` | 17:38:56 | O (v3 supersession seats) |
| `v3-supersession/v3-supersession-check.py` | 30104 | 583 | `2a20ddbb` | 17:37:02 | O (v3 supersession seats) |

Partition counters (`python3 .scratch/r25d/ledger.py`, 2026-10-18T17:40:52Z):
**`reports/round-25` 59 files**, `corpus/lessons` outside-partition 1 indexed file.
## 2. Fragments outside `reports/round-25/` (re-read 2026-10-18T17:37Z)

The round's deliverables are not all under `reports/round-25/`. Observed with
`git status --porcelain` at 17:37Z; each owned by its seat, **not** written by
this one:

| path | bytes | sha8 | owner seat | claim |
|---|---:|---|---|---|
| `corpus/lessons/README.md` | 25081 | `ee2a15df` | C (lessons index) | C |
| `corpus/lessons/round-25.md` | 26897 | `feccf068` | X (gate-keeper survey) | — |
| `tools/gates/argot-derivation-gate.py` | 28588 | `07db6e9b` | D (argot implementation) | D |
| `tools/gates/fixtures/argot-derivation-gate.yml` | 2853 | `c4c35294` | D (argot implementation) | D |
| `tools/gates/fixtures/argot-derivation-gate.expected` | 79 | `38a283ff` | D (argot implementation) | D |
| `tools/gates/typed-pipeline-gate.py` (**modified**) | — | `879d40bf` | O (gate-input seats) | O |
| `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | — | — | O (gate-input seats) | O |

`tools/gates/frozen/round-25/` holds **one** generation at this stamp,
`gate-input/` (6 recorded rows + 2 control fixtures + 4 input snapshots + 6
recorded outputs), and it replays **6/6 OK**. There is **no**
`tools/gates/frozen/round-25/MANIFEST.tsv` and **no** argot generation.

## 3. Self-reference caveat

This ledger's own two rows (`scribe/fragment-ledger.{md,json}`) show the
revision immediately *preceding* this census's write. Re-hash them rather than
inheriting the values here. The `.json` row in §1 is a **prior** revision; the
file was regenerated after the table was built.

## 4. Tool artifacts measured at the census (the wave's executable side)

These are not `reports/round-25` fragments, but the parent needs them to read
the fragments above. Every digest is this seat's measurement at the stamp shown;
the two gates were **revised repeatedly during this seat's window**, so both the
transient states and the settled state are recorded.

| artifact | sha256 (measured) | stamp | state |
|---|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe` | 17:33:42Z | **settled green**: `--selftest` **18/18**; D4 run exit 0 |
| `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` | 17:32:19Z | landed 17:32Z |
| `tools/gates/fixtures/argot-derivation-gate.expected` | `38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018` | 17:33:42Z | landed 17:32Z (5 lines) |
| `tools/gates/typed-pipeline-gate.py` | `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126` | 17:35:02Z | **settled green**: `--selftest` **19/19**; D4 typed input exit 0, 16/16 legs |
| `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | 6 rows | 17:36:45Z | replays **6/6 OK** (§4c) |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | 17:29Z | unchanged all window |

### 4a — the argot gate's transient selftest reds (now green)

```sh
python3 tools/gates/argot-derivation-gate.py --selftest   # 18/18, exit 0 at 17:33:42Z
```

Five revisions landed during this seat's window; the intermediate selftest
states are recorded because a fragment must not cite a red check as green:

| stamp | gate sha256 (8) | `--selftest` | cause |
|---|---|---|---|
| 17:31Z | `82f48649` | exit 1 | neither fixture file on disk (`fixture unreadable`) |
| 17:32:13Z | `55f83442` | exit 1 | `.yml` landed, `.expected` missing → uncaught `FileNotFoundError` traceback |
| 17:32:30Z | `3deb6bb6` | **16/18** | `fixture-names-the-violating-form` + `coverage-hold-fires` red |
| 17:32:52Z | `75aee372` | **17/18** | one over-specific assertion left |
| **17:33:42Z** | **`07db6e9b`** | **18/18** | settled |

The `fixture-names-the-violating-form` check asserted one message carrying both
`Q-12` and `saalum`; measured, the fixture names them in **separate** rows
(`Q-11 'saalum'`, `Q-12 'kin'`). The planted-verdict checks
(`fixture-exits-1`, `fixture-ids-match-expected-file`, `fixture-counts-pinned`)
passed throughout at the `.expected`-bearing revisions: the fixture emits exactly
`{D4L-ARGOT-DERIV: 4, D4L-ARGOT-RULE: 1}`. Both transient reds were fixed
in-flight by the implementation seat.

### 4b — the typed-pipeline gate's transient selftest crash (now green)

```sh
python3 tools/gates/typed-pipeline-gate.py --selftest   # 19/19, exit 0 at 17:35:02Z
```

At `a6e8d9c8…` (17:33:04Z) `selftest()` raised `KeyError: 'owed_slot_of'`
(`tools/gates/typed-pipeline-gate.py:1087`) — a peer module not exporting that
name. The gate's **runtime** path was already fixed at that revision:
`typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` read **exit 0,
16/16 legs** where the round-24 cold run read exit 1 with two failing legs. So
the O claim's code repair landed on the runtime path before the selftest caught
up; the settled revision `879d40bf…` is green at 19/19. Both facts are recorded;
neither is inferred.

### 4c — the round-25 frozen generation replays green

```sh
mkdir -p /var/tmp/kotodama-r25
TMPDIR=/var/tmp/kotodama-r25 python3 tools/replay-frozen.py \
  tools/gates/frozen/round-25/gate-input/MANIFEST.tsv
# REPLAY OK: 6/6 rows reproduced the recorded verdicts
```

The six rows: D4 source (exit 0, 12 findings), D4 typed (exit 0, 12), D2 source
(exit 0, 15), D2 typed (exit 0, 15), and the two negative controls
(`typed-without-source`, `typed-stale-source` → exit 2 each). This is the first
round-25 generation and it is a **new generation directory** — no earlier
manifest was edited. It was itself re-pinned mid-wave (it read
`gate_digest_mismatch` 6/6 at 17:34:39Z while the gate was still moving, then
green once the gate settled).

## 5. Supersession watch (named, not absorbed)

One wave edit to `tools/gates/typed-pipeline-gate.py`
(`04ad4bb4…` → `a6e8d9c8…` → `daeaa722…` → `879d40bf…`, settled) turned every
generation that pins that gate in any row red at that row, and a second
supersession affects the round-18 projection row. Both are events to be
dispositioned by the parent, never repaired by editing a filed row:

| generation | state at 17:36:45Z | cause |
|---|---|---|
| `round-3`, `round-3/attempt-1` | **could-not-evaluate 7/7** | pins the gate bytes at `291c714`; documented at `SKILL.md:459` |
| `round-11` | **could-not-evaluate 1, reproduced 10/11** | one row pins `provenance-audit.py` at a superseded revision |
| `round-18` | **mismatch 1, reproduced 1/2** | row 2 pins the superseded projection `a59990bb…`; live successor `60b526b0…` (round-22 family-clean). Gate and snapshot digests both verify — see `reports/round-25/scribe/frozen-rows.md` §3 |
| `round-18/repin-d2`, `round-20/repin-d2`, `round-22/d4-repin`, `round-23/repin-d2` | **could-not-evaluate 1, reproduced 10/11 (or 2/3)** | one row each pins `typed-pipeline-gate.py`; the gate moved this round |
| `round-25/gate-input` | **REPLAY OK 6/6** | the new generation, re-pinned to the settled gate |

The round-25 gate-input generation is the correct shape of the response: a
**new** generation recording the new gate revision, not an edit of an earlier
row. This is the designed fail-closed behaviour ("a later edit to that gate
turns the row red by design — a re-freeze is a new recording, never an
in-place edit").

## 6. Limits

- The census is a snapshot of a live wave; counts here are evidence of movement,
  never a completeness score. Files arriving after 2026-10-18T17:40:52Z need a dated
  refresh.
- `owner_seat` is an inference from path conventions and file headers, not an
  authority statement; several rows read `unattributed` because no convention
  resolves them. The parent confirms ownership at integration.
- No canon, rights, clearance or freshness ruling is made or absorbed. This
  ledger admits nothing and certifies no round.
- No historical round validator was run for this index; no filed artifact of
  rounds 8–24 was modified.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
find reports/round-25 -type f | wc -l                      # 59 (2026-10-18T17:40:52Z)
find reports/round-25 -type f | sort
git status --porcelain                                     # outside-partition fragments
find tools/gates/frozen/round-25 -type f | sort
sha256sum tools/gates/argot-derivation-gate.py tools/gates/typed-pipeline-gate.py \
  tools/gates/fixtures/argot-derivation-gate.yml tools/gates/fixtures/argot-derivation-gate.expected
python3 tools/gates/argot-derivation-gate.py --selftest        # 18/18, exit 0
python3 tools/gates/typed-pipeline-gate.py --selftest          # 19/19, exit 0
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # exit 0
mkdir -p /var/tmp/kotodama-r25
TMPDIR=/var/tmp/kotodama-r25 python3 tools/replay-frozen.py \
  tools/gates/frozen/round-25/gate-input/MANIFEST.tsv           # REPLAY OK 6/6
```


FILES: reports/round-25/scribe/fragment-ledger.md, reports/round-25/scribe/fragment-ledger.json | SUMMARY: D20 scribe — read-time census of `reports/round-25/**` (49 files at 2026-10-18T17:37:11Z, up from 2 at 17:23Z) plus the outside-partition fragments (`corpus/lessons/README.md`, `corpus/lessons/round-25.md`) and the wave's tool artifacts, with every transient and settled state of both revised gates recorded: `argot-derivation-gate.py` settled at sha `07db6e9b…` (`--selftest` 18/18, D4 run exit 0 with `register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0`, five revisions and two transient selftest reds named) and `typed-pipeline-gate.py` settled at `879d40bf…` (`--selftest` 19/19, D4 typed input exit 0 / 16/16 legs — the O false red fixed); the round-25 `gate-input` frozen generation replays **6/6 OK** while one wave edit to the typed-pipeline gate turned four earlier generations' typed-pipeline rows `gate_digest_mismatch`, and the round-18 row-2 superseded-projection finding stands.
