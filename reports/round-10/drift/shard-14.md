# R10-F14 — drift shard 14: `reports/round-9/baselines/registry.md` rows vs live gate files

- seat: **R10-F14** (freshness claim F, drift shard 14). Assignment: match every
  registry entry command against the live gate files — exists? runs? verdict map
  accurate? This file is the seat's only write; no gate, fixture, battery,
  baseline, corpus or shared-bookkeeping byte was edited by it.
- date: 2026-10-17. Measurement clock: `2026-10-17T21:25:58Z`–`21:29:14Z` (UTC),
  local UTC-03:00. Lane revision: `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
  (`git rev-parse HEAD`).
- scope: the registry's own executable claims — §2 seven structural gates,
  §3 five harness entries, §4 pin sweep, §5 divergences. `SKILL.md` and
  `SCORECARD.md` rows belong to other shards; `run-validation.py` (round-10) and
  the C/O legs are out of this shard.
- scratch: `TMPDIR=$PWD/.scratch` exported for every command (`.scratch/r10f14/`
  holds the raw receipts: per-gate stdout captures, ID lists, battery JSON,
  runner stdout). `/tmp` remains unusable: `df -i /tmp` →
  `1048576 1048576 0 100%` — re-measured today, registry §5 item 5 still true.
- classification vocabulary: **current** (live agrees with the registry row),
  **stale-documented** (live differs; the divergence is recorded here with the
  live value and a reason; nothing in this shard rewrites filed bytes — the
  round-10 F15+ fixers own any repair).

## 1. Verdict summary

| layer | rows | current | stale-documented | broken |
|---|---|---|---|---|
| 7 gate scripts (sha256, selftest, fixture verdict, ID set, verdict map) | 7 | 7 | 0 | 0 |
| 7 fixtures + 7 `.expected` (sha256) | 14 | 14 | 0 | 0 |
| 8 `expected.json` pins (digest, `gate_sha256`, `inputs`) | 8 | 7 | 1 (provenance pin file digest) | 0 |
| 5 harness entries (battery, runner, r8_checks, replay-frozen, D3 rows) | 5 | 2 | 3 (battery digest, runner digest+state, D3 coupling state) | 0 |
| registry §5 divergences 1–9 | 9 | 8 | 1 (item 8 resolved: runner now green) | 0 |

Nothing in the registry's command layer fails today. All four stale items are
digest/state quotes from mid-wave revisions; every behavior the registry
describes is reproduced by the live tree.

## 2. The seven structural gates — every row current

Commands re-run 2026-10-17 (local), from the lane root, `TMPDIR` set:

- script digests: `sha256sum tools/gates/*.py` — all seven match the registry
  §2 `measured:` lines exactly (costume `e6bffd70…478f`, handoff `e2fa3223…ad575`,
  lexicon `2c4dd397…d4287`, myth `5368b135…5f08`, naming `d9e4e8f4…0a1d`,
  phonology `d5fe087f…4230`, provenance `8a96aaf4…4e3a`).
- fixture + `.expected` digests: `sha256sum tools/gates/fixtures/*.{yml,md,expected}`
  — all match the registry rows (e.g. costume fixture `36d92113…ea0e`,
  handoff `.expected` `1aab55f2…7892`, provenance `provenance.expected` ≡
  `provenance-audit.expected`, both `7ba4fa5c…1cbc`).
- self-test spellings, both flags: `for s in --selftest --self-test; do python3
  tools/gates/<gate>.py $s; echo $?; done` — exit 0 for the five dual-spelling
  gates (receipts byte-for-byte the registry's quoted strings); **provenance and
  handoff exit 2 on `--self-test`** with `unrecognized arguments`, exactly as
  the registry's `--selftest`-only rows state.
- fixture verdicts: `python3 tools/gates/<gate>.py tools/gates/fixtures/<fixture>`
  — exit 1 for all six file-graded gates; line/ID counts and ID-set equality
  against `.expected` all reproduce:

| gate | fixture run exit | FINDING lines | unique IDs | set vs `.expected` | fixture stdout sha256 |
|---|---|---|---|---|---|
| phonology-sanity-gate | 1 | 16 | 15 | equal | `b3843b2a5f50809ffe43fd55212cb9ab320f4ac98c2a59c6f57c7bcc61617018` |
| lexicon-coverage-audit | 1 | 20 | 18 | equal | `af5794955b60b455b433a570434bf0ab69c110b66c891eab567d5addef0be4f4` |
| myth-consistency-gate | 1 | 6 | 6 | equal | `88385088ca2ee13192b9669a02cbe44aebf9c22df752a2af76138a13e1cf77d2` |
| costume-era-consistency-gate | 1 | 25 | 21 | equal | `482c1597a22096b2a0a09f09ce476f6ae5bbd6db70baf50df128fb0c1ed608b3` |
| naming-collision-gate | 1 | 12 | 11 | equal | `bea0fd3925c2745ecf6333733d1118deb9831241cf2d12e3742c571ec88a52ac` |
| handoff-packet-check | 1 | 11 | 9 | equal | `ec1ec331a820f5eaa4dd916c99a404fa92223c06566ffe8c1e1b6f92a01064b3` |
| provenance-audit (dir) | 1 | 6 | 6 | equal | `89cf4b3cb4ba617a13a849ec07e89acc0ea4d931f446eaefc9ffb769bbede07f` |

- **bonus cross-check:** the costume fixture stdout digest measured here is
  byte-identical to the `stdout_sha256 482c1597…08b3` that the registry's §4
  baseline table pins — the fixture run and the frozen baseline agree today.
- verdict maps, probed beyond the fixture: phonology messages open `FAIL` or
  `REVIEW` (15/15 verified); naming levels present `FAIL` 7 / `HOLD` 5 /
  `REVIEW` 3; costume severities present `[reject]` 8 / `[hold]` 16 / `[note]` 1;
  lexicon missing input → exit 2, stderr `ERROR: cannot read …`, no `FINDING`
  line; provenance missing path → exit 2 `CANNOT-EVALUATE: …: not a readable file`;
  myth non-mapping root → exit 2 `FINDING G-DATA`; naming malformed YAML → exit 2
  (with the sectionless-packet HOLD behavior: `name: empty-packet` → exit 1,
  `NAME-INVENTORY: HOLD`, `PHON-PROFILE: HOLD`, `CROSS-HOLD: HOLD`).
- stdin modes: `cat fixtures/phonology-sanity-gate.yml | … -` → exit 1;
  `cat fixtures/handoff-packet-check.md | … -` → exit 1 (both documented as
  `-` reads stdin).
- provenance multi-path/dir modes and the clean-entry control:
  `provenance-audit.py fixtures/provenance/good-entry.md` → exit 0;
  the directory run prints `INFO scan: files=7 marks=2 mark-lines=2 findings=6 blocked=0`
  — the registry's quoted scan line, verbatim.
- write-scope claims spot-checked by absence of change: after every run the
  seven gate scripts and the fixture tree still carry their pre-run mtimes and
  digests; `git status --porcelain` shows no modification under `tools/gates/`.

**Row verdict: all seven gates current.** Exists ✔, runs ✔, verdict map ✔,
self-test spellings ✔, pinned-value paths ✔.

## 3. Round-9 harness entries

### 3.1 `tools/check-gate-battery.py` — runs as documented, **digest stale**

- live digest `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1`
  (committed at HEAD `9dc18ec`); registry §3 quotes `9ad0ef9516852c0f…`.
- **stale-documented.** The registry's own sibling evidence settles it:
  `reports/round-9/baselines/battery-extension.md:15` records `9ad0ef95…` as the
  17:53 revision and `0a126b70…` as its 17:55 successor ("differs only in the
  `BASELINE-GATE-UNCOVERED` detail text"), and `audit-18.md:18-21` /
  `audit-20.md:10` bind `0a126b70…`. The registry's §5 item 6 decision record
  therefore quotes a digest its own referenced evidence already superseded.
  No repair attempted here (filed bytes are not rewritten; F15+ owns fixes).
- behavior re-measured at the live digest:
  - `--selftest` → exit 0, `SELFTEST OK 28/28 controls behaved as expected`.
  - committed default `python3 tools/check-gate-battery.py` → **exit 2**;
    duty 1 `pass 7 / fail 0 / unevaluable 0`, `originals {preserved: true,
    modified 0, added 0, deleted 0, files_hashed_before 28, files_hashed_after 28}`;
    duty 2 `baselines_found 5, pinned 5, readings {pinned: 5}`,
    `gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]` —
    exactly the registry's §3/§5 reading.
  - three-root invocation (same argv as the registry's) → **exit 0**;
    `baselines_found 8, pinned 8, readings {pinned: 8}, gates_uncovered []`;
    handoff's pin still counted twice (both byte-identical `9dc21cd5…`) —
    registry §5 item 7 reproduced.
  - `--timeout 0` → usage error exit 2 (positive-finite requirement holds).
  - `verdict_replay: "not-run: …"` present in both reports — the "never
    re-executes a baseline" caveat holds.
  - `BASELINE_ROOTS = (GATES_DIR/"expected", GATES_DIR/"frozen")` at
    `tools/check-gate-battery.py:114` — the three-root split (registry §5 item 1)
    is still live and still the orchestrator's to reconcile.

### 3.2 `reports/round-9/run-validation.py` — **stale-documented, now green**

- live digest `8e4881309afaacc96f8f6e68f0c31041a9b2accc1c26bb1b20403f563364f5dd`
  (committed at HEAD); registry §3 last quotes `58e8fa4f…` and 13 failures.
- re-run today (`python3 reports/round-9/run-validation.py`, ~21:27Z) → **exit 0**,
  stdout `claim F: PASS / claim O: PASS / claim D: PASS /
  acceptance_checks_passed: True`; the regenerated
  `reports/round-9/validation.json` carries `runner_sha256 8e488130…`,
  `acceptance_checks_passed: true`, `failures: []`, `missing_dependencies: []`.
- the committed receipt at HEAD already read the same (checked with
  `git show HEAD:reports/round-9/validation.json`), so the registry's "O is not
  green on the delivered tree as of 20:54Z" statement was true at its clock and
  is **superseded**: the runner owner landed the fix before the round-9 commit.
- side effect, recorded: the re-run rewrote the tracked
  `reports/round-9/validation.json` (its child stdout digests and `git_status`
  fields reflect today's tree; `git diff --numstat` = 4 insertions / 14
  deletions). The file is the runner's own declared output, regenerated
  deterministically; no gate/fixture/corpus byte was touched. This is the only
  tracked byte this seat's commands changed.
- registry §3's stale-receipt hazard warning (`runner_sha256` vs live
  `sha256sum`) is confirmed good practice: today they agree.

### 3.3 `tools/harness/r8_checks.py` — current

- digest `0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe`
  = registry's pinned `tool_sha256` exactly.
- `--selftest` → exit 0, `"selftest_passed": true`, `controls_passed 14 /
  controls_total 14`, printed `tool_sha256` matches the live digest;
  `--measure` → exit 0 with the corrected measurement; neither flag → usage
  error exit 2. All three registry claims hold.

### 3.4 `tools/replay-frozen.py` — current (behavior), digest unquoted in registry

- digest `a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464`
  (committed at HEAD; the registry names no digest for this row, so no drift is
  claimable — recording the live value here as the round-10 anchor).
- `--selftest` → exit 0, `selftest: 79/79 checks passed` (registry's receipt
  reproduced); usage error (no manifest) → exit 2. The selftest controls cover
  the registry's verdict map end-to-end: `clean-green`/`expected-red`
  reproduced, `mismatch-bytes`/`mismatch-exit` exit 1, `snapshot-tampered`,
  `gate-digest-mismatch`, `output-tampered`, `record-inconsistent`,
  `gate_unsafe_path`, `gate_not_whitelisted`, `snapshot_unsafe_path`,
  `input_unsafe_path` (incl. flag-like `--selftest`/`./--selftest`/`-` inputs
  never triggering the gate's own selftest) all exit 2.

### 3.5 D3 acceptance rows (`SKILL.md:248-251`, cited by the registry) — state drift, now green

- `python3 tools/assemble-culture-d3.py --check` → **exit 0**, both projections
  byte-identical — registry row's 0-verdict reproduced.
- `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` →
  **exit 0**, `findings: []`. The registry §3 quote of the runner's D failure
  (`--frozen` `D3-SNAPSHOT` digest mismatch, declared `50c4c2f2…` vs actual
  `5f4c02bf…`) is **stale-documented**: the plain-packet run and the round-9
  runner's D: PASS agree that the mismatch is resolved on the delivered tree.
  The `--frozen` variant itself is a D-shard surface and was not re-run here.

## 4. §4 pin sweep — 8 pins, 7 digest-current, 1 stale-documented

`find tools/gates reports/round-9 -name expected.json | sort` → the same 8 files
as the registry's sweep, at the same paths (the three-root split persists).

| gate | pin file sha256 (live) | registry | `gate_sha256` declared = live | `inputs` recomputed | verdict |
|---|---|---|---|---|---|
| costume-era-consistency-gate | `7ec01a1d…` | `7ec01a1d…` | ✔ `e6bffd70…` | battery `pinned` | current |
| phonology-sanity-gate | `2763614f…` | `2763614f…` | ✔ `d5fe087f…` | battery `pinned` | current |
| handoff-packet-check (×2, identical) | `9dc21cd5…` | `9dc21cd5…` | ✔ `e2fa3223…` | battery `pinned` twice | current |
| lexicon-coverage-audit | `0fad58ba…` | `0fad58ba…` | ✔ `2c4dd397…` | battery `pinned` | current |
| **provenance-audit** | **`425c74c0…`** | **`ba4b2994…`** | ✔ `8a96aaf4…` | 20/20 match (independent recompute) | **stale-documented** |
| myth-consistency-gate | `a87edc53…` | `a87edc53…` | ✔ `5368b135…` | battery `pinned` | current |
| naming-collision-gate | `2f34ee18…` | `2f34ee18…` | ✔ `d9e4e8f4…` | battery `pinned` | current |

- **provenance pin, the one digest drift.** The registry §4 table records the
  pin file as `ba4b2994…`; the live (and HEAD-committed) file is
  `425c74c084bb53bdf8aff8d4f143a6cbe062421e1362f234e5fe702463f95e87`. The file's
  mtime is 17:54:17 local — **after** the registry's own sweep clocks
  (17:53:12Z–17:53:35Z = 20:53Z), so the registry measured an earlier revision
  of the pin. The registry's peer fragments already carry the live value
  (`audit-18.md:87`, `audit-20.md:121`, and `reports/round-9/validation.json`
  `input_sha256`), so the fix is a registry-row correction, not a pin defect.
- **the live pin is valid**: recomputed all 20 `inputs` digests against the
  snapshot bytes → 20 match / 0 mismatch; `stdout_sha256 26f217410f220b…` equals
  `sha256sum tools/gates/frozen/provenance-audit/r9-pre/run.log`; the battery
  reads it `pinned`. The registry's §6 caveat (pins prove bytes, never verdicts)
  still stands — no verdict re-execution was attempted here.
- registry §4's caveat that the committed default battery reaches only the five
  `tools/gates/{expected,frozen}` pins is reproduced exactly (5 pinned / 2 gates
  uncovered), as is the two-revision split (§5 item 2) and the duplicate handoff
  id (§5 item 7).

## 5. §5 divergences 1–9 — status today

1. three baseline roots in flight — **still true** (`BASELINE_ROOTS` unchanged,
   myth/naming pins still only under `reports/round-9/baselines/`). Open for the
   orchestrator; not this shard's to decide.
2. two `revision` values across baselines — still present in the pin files
   (costume/handoff/myth `a7bb205d…`; naming `e1694bad…` + supersession note).
3. `run.log` ignored by `.gitignore` — **still true**: `git check-ignore -v`
   matches `*.log` (`.gitignore:3`) for both the provenance and handoff
   `run.log` files.
4. `handoff-packet-check.expected` no trailing newline — **still true**:
   `wc -l` → 8, tail byte `G` (no LF), 9 unique IDs.
5. `/tmp` inode exhaustion — **still true** (`df -i /tmp` → 100%).
6. battery discovery short of green on the committed default — **still true**
   (exit 2, same two uncovered gates; three-root exit 0) — only the quoted
   script digest is stale (§3.1).
7. duplicated baseline id under two directories — **still true** (two
   byte-identical `9dc21cd5…` copies, both read `pinned`, not flagged).
8. stale `validation.json` receipt / runner revision hazard — **resolved on the
   delivered tree**: runner digest `8e488130…`, receipt self-pin agrees, exit 0,
   0 failures (§3.2). The *hazard* remains valid advice.
9. cross-leg state in the runner receipt — **superseded**: runner now reports
   F/O/D all PASS; the D `D3-SNAPSHOT` mismatch it named is resolved (§3.5).

## 6. What this shard does not claim

- Not a re-measurement of `SKILL.md` / `SCORECARD.md` rows (other F shards),
  nor of the C (coverage) or O (operability) legs.
- Not a verdict re-execution: the battery and this shard verify digests and
  pins; a baseline's verdict comparison belongs to the baseline's own re-run
  receipt. The one verdict-shaped check done here is the *fixture* run vs
  `.expected` ID sets (§2).
- Not a repair: all four stale items are recorded, not edited; filed report
  bytes are never rewritten. Repairs belong to the F15+ stale-fixers and the
  orchestrator's reconciliation of §5 items 1/6/7.
- Not a judgment on any gate's design or any culture artifact's content.

## 7. Raw receipts (untracked scratch, disposable)

`.scratch/r10f14/`: `<gate>.out` (stdout captures), `<gate>.ids` /
`<gate>.exp.ids` (ID-set diffs), `battery-default.json`, `battery-3root.json`,
`rv9.out`/`rv9.err` (runner re-run), `lex-err.*`, `myth-nm.out`,
`notmap.yml`/`empty.yml`/`malformed.yml` (negative-control inputs).
