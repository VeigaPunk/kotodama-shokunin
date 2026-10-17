# R11-O15 — frozen rerun: independent baseline re-validation in a copied tree

- shard: round-11 claim O, target **R11-O15** (`frozen rerun`; the verification half of
  R11-O14's frozen baseline). Round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17.
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; worktree HEAD `e3ef171`
  (`git log --oneline -1`, 22:14Z) plus the round's untracked worker output. No commit was made.
- measurement window: **22:07–22:24Z** (local 19:07–19:24, UTC−3); every stamp below is UTC
  unless marked local. **Two phases**, because the round was still moving: §§1–9 measure the
  first committed baseline (at `tools/gates/expected/handoff-exercise/r11/`, tool revision
  `38d1cba4…`); §10 re-runs the same legs on the **re-homed, current** baseline
  (`reports/round-11/handoff/expected.json`, tool revision `a21934ad…`) after the O-shard
  relocated it and rewrote the tool mid-round. The phase-1 record is retained because it is the
  evidence for findings F1–F6 and for the class mapping that changed in phase 2 (§10.3).
- owns: **this file only**. No tool, baseline, packet, gate, corpus or LOG byte was edited by this
  shard. Scratch (including the copied trees) lives in `.scratch/r11-o15/` (gitignored); the
  receipts quoted here are retained there (§9). `TMPDIR=$PWD/.scratch` (copy-local) was exported
  for every scratch-writing command, per the operator rule.
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §6 — digest check
  first, then the executor-revision check, then the verdict comparison, with tamper drills on
  copies (`§6` rows in §5 below). That standard scopes to `tools/gates/**`; this baseline is a
  **tool** baseline, so the standard is applied by analogy, and the two places where the analogy
  does not hold are named as findings (§7, F3/F4) rather than smoothed over.
- assignment sentence tested: *"frozen rerun: independent baseline re-validation in a copied tree"*,
  against the O-claim's `after_required` clause ("committed expected.json baseline; selftest with
  positive + malformed controls", `reports/round-11/claims.json:27`).

## 0. Verdict — read this first

| leg | command (all in the copied tree unless stated) | observed | status |
|---|---|---|---|
| A copied-tree replay | `python3 tools/exercise-handoff-e2e.py` | exit 0; 11 × `OK`; `exercise-handoff-e2e: PASS — fields=16/16 glossary-entries=20 findings=0` | **PASS** |
| B1 independent field/glossary count | `python3 <scratch>/independent-envelope.py tools/gates/expected/handoff-exercise/r11/packet.md` | `fields=16/16`, one glossary table, **20** data rows | **PASS** |
| B2 independent cross-reference resolution | `python3 <scratch>/independent-contract-refs.py . <packet>` | contract digest present and equal to the live contract `5f4c02bf…`; **18/18** per-path digest claims match; 0 unresolved | **PASS** |
| B3 independent gate run (my own isolation) | gate + frozen packet copied to a separate scratch dir, run from that foreign cwd | exit 0; `INFO scan: fields=16/16 glossary-entries=20 findings=0` | **PASS** |
| B4 independent re-freeze | `python3 tools/exercise-handoff-e2e.py --freeze .scratch/r11-o15/frozen-independent` | exit 0; all four frozen files reproduce **byte-identically** (`expected.json 1ab17670…`, `packet.md 2a058f78…`, `run.log 2346783b…`, `freeze.txt 003fe548…`); `diff` of the JSON modulo `frozen_at` empty | **PASS** (freeze determinism, not independent derivation — §4) |
| C tamper/falsifiability drills T1–T10 | see §5 | every intended class fired; two silent cases found (T4, T8) | **mixed by design** |
| D regression | gate `--selftest`; `replay-frozen.py` over the round-9 `r9-pre` baseline; `check-gate-battery.py` | exit 0 / exit 0 with the recorded stdout pin reproduced / 7/7 gate selftests pass, 5 baselines `pinned` | **PASS**, with the battery finding F2 |
| E determinism | three exercise runs, two with `--emit` | packet digest `2a058f78…` identical every time and equal to the frozen packet | **PASS** |
| F exercise self-test | `python3 tools/exercise-handoff-e2e.py --selftest` | **exit 1** — `AssertionError: ["evaluated: cannot hash examples/culture-d2/components/02-phonology.yml: … No such file or directory"]`; reproduced in the lane tree and in the copy at tool revision `38d1cba4…` | **RED — finding F1** |

The frozen baseline itself replays clean in a tree that is not the author's: the copied-tree run,
my own counter, my own gate run and my own re-freeze all reproduce the committed verdict and the
committed bytes. The two reds belong to the surrounding claim, not to the baseline: the exercise's
`--selftest` is broken at the measured revision (F1), and the baseline's home trips the gate
battery's default root scan (F2).

**Both reds were repaired in-flight while this shard ran, and the baseline has since moved.** The
current state — re-homed baseline, rewritten tool, green selftest — is measured in **§10**; the
table above stands as the phase-1 record, and §10.3 lists what changed between the phases
(including one drill whose class changed and one executor gap that opened).

## 1. Method — the copied tree

```sh
S=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/r11-o15
sh $S/copy-tree.sh $S/tree          # rsync -a; excludes .git/, .scratch/,
                                    # reports/supplement-opencode-1/scratch/ (383M, no round-11 input)
cd $S/tree && export TMPDIR=$PWD/.scratch-tmp && mkdir -p $TMPDIR
```

- Copy made at 22:09Z (22M, 0.07s), after the baseline landed (22:08Z) and the tool stopped
  changing (last revision `38d1cba4…` seen from ~22:09Z; the tool was revised at least three times
  inside the window — `c202927e…` at 22:07:13Z, `9135e1fb…` at 22:08Z, `38d1cba4…` at 22:09Z —
  so every receipt below names its revision, and the digest check in §2 re-ran at the end).
- The exercise itself copies the assembled packet into an isolated directory under `TMPDIR` and runs
  the committed gate there from that foreign working directory (`tools/exercise-handoff-e2e.py:34-44`,
  observed path `.scratch-tmp/handoff-exercise-*/isolated` in leg A). That isolation is the tool's
  own; legs B3 and C add a second, this-shard-owned isolation so the result does not rest on it.
- Nothing was run against the lane tree except read-only commands (`sha256sum`, `--selftest` with
  `TMPDIR=$PWD/.scratch`, `check-gate-battery.py`, `git status`).

## 2. Verified bytes (sha256, measured 22:07–22:14Z; final re-check 22:14Z)

| object | sha256 | note |
|---|---|---|
| `tools/exercise-handoff-e2e.py` (revision at measurement) | `38d1cba429d98af79a14201d6cdf44150dd935314f4536003253f8f576b4f4c1` | 67,205 B; the digest the committed baseline itself records for this tool |
| `tools/gates/handoff-packet-check.py` | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` | unchanged since the r9-pre freeze |
| `tools/gates/expected/handoff-exercise/r11/expected.json` | `1ab17670c113bf5f10a80f5ba564b252d948a836c3793efe641c68154d286b33` | the frozen baseline under test (4,354 B, mtime 19:08 local) |
| `tools/gates/expected/handoff-exercise/r11/packet.md` | `2a058f7858127b98592439594c55974d93e6e672a600dd2036b47e21e71c8a63` | equal to the baseline's `packet_sha256` |
| `tools/gates/expected/handoff-exercise/r11/run.log` | `2346783b8d6b76058324a66b56658f07c4fb5d3b80fdc8523fa40b64a60db35a` | frozen gate stdout (`INFO scan: fields=16/16 glossary-entries=20 findings=0`) |
| `tools/gates/expected/handoff-exercise/r11/freeze.txt` | `003fe548222a9315046dde149152be8f92a4be1f882f1c0e03cc17fac2ca4230` | freeze record |
| `examples/culture-d2/packet.d2.yml` · `typed-labels.d2.yml` | `e0f21509…` · `e70ba147…` | baseline `inputs` rows, re-measured in the copy, match |
| `examples/culture-d3/packet.json` · `packet.gates.yml` | `bdf635ce…` · `306bcac7…` | baseline `inputs` rows, match |
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` | baseline `inputs` row, match; equal to the `contract_ref` digest inside the packet |
| `tools/assemble-d2.py` · `assemble-culture-d3.py` | `8ea6bdde…` · `ba8d19d5…` | baseline `tools` rows, match |

Baseline shape (read at 22:11Z, `expected.json`): `profile kotodama-handoff-exercise/1`,
`declared {expected_exit: 0, fields_expected: 16, glossary_entries_expected: 20, finding_ids: []}`,
`inputs` (5 sources), `tools` (gate + exercise tool + two assemblers), `packet_sha256`,
`field_values_sha256` (16), `glossary_ids` (20, `L01`–`L20`), `counts`, `cross_refs`
(`gate_exit 0`, `gate_fields "16/16"`, `gate_glossary_entries 20`, `contract_digest …5f4c02bf…`,
`component_digests 13/13`). All `inputs` and `tools` digests currently equal the live bytes.

## 3. Leg A — the copied-tree replay

`python3 tools/exercise-handoff-e2e.py` in `$S/tree` (22:09Z, 22:12Z), exit 0, stdout 12 lines,
receipt `run-primary.out` (`4793c0d3…`), stderr empty (`e3b0c442…`):

```
OK   declared-expectations: baseline and exercise agree on the declared expectations
OK   frozen-input: 5 frozen input digests match the live bytes
OK   preflight: 16 fields, non-canon marker, glossary vocabulary and no floating version
OK   gate-exit: exit 0 (expected 0) from …/.scratch-tmp/handoff-exercise-…/isolated
OK   gate-scan: fields=16/16 glossary-entries=20 findings=0
OK   gate-findings: no findings
OK   frozen-packet: assembled sha256 2a058f785812… vs frozen 2a058f785812…
OK   frozen-fields: all 16 field digests match the frozen baseline
OK   frozen-glossary: 20 glossary ids match the frozen baseline
OK   contract-crossref: kotodama-lore-adjacency 1.0.0 sha256:5f4c02bfc4e6…
OK   component-digests: 13/13 component digests re-measured and matched
exercise-handoff-e2e: PASS — fields=16/16 glossary-entries=20 findings=0
```

Leg E (determinism): two further runs with `--emit` wrote `emit-2.md` and `emit-3.md`, both
`2a058f78…`, equal to the frozen `packet.md`; the two stdout receipts (`run2.out` `b11ed62b…`,
`run3.out` `75abc2d2…`) differ only in the isolated-directory path embedded in the `gate-exit`
line, which is why the tool's own comparison is field-set-based rather than stdout-byte-based.

## 4. Leg B — independence, and what "independent" does and does not mean here

- **B1 envelope/glossary** — `independent-envelope.py` (this shard; 3.8 KB) implements the §4
  16-field list and the glossary-table shape from the contract text, not by importing the gate:
  `fields=16/16`, `missing=(none)`, one glossary table at line 127 with **20** data rows and an
  `etymology` column. First version of the script counted 0 entries for the D3-shaped header
  `| entry_id | E0 form | E1 form | gloss (packet) | etymology |`; the shipped gate counts it as 20
  because its content test is `cell in GLOSSARY_CONTENT_HEADERS or cell.startswith("etymology")`
  (`tools/gates/handoff-packet-check.py:363-373`). The script was corrected to the same rule and
  re-validated against two known-20 packets (r9-pre, the sample) before being used here. This is
  the one place where a second opinion had to adopt the first opinion's recognition rule to agree —
  recorded because it bounds the independence claim.
- **B2 cross-references** — every `sha256:` claim next to a `corpus/…`, `examples/…`, `tools/…`
  path was re-resolved against the copied bytes: 18 claims, 18 matches, 0 unresolved, and the
  contract digest in the packet equals the live contract file. The same script over the **r9-pre**
  packet returns 3 intentional mismatches (the round-8 contract repair and the round-9 expected.json
  refresh), which is the control that the script can fail.
- **B3 own gate run** — the gate and the frozen `packet.md` were copied into
  `$S/iso-direct/` (no tool involvement) and run from there: exit 0, `INFO scan: fields=16/16
  glossary-entries=20 findings=0`. The stdout digest is `7c581047…` — byte-identical to the
  round-9 `r9-pre` stdout pin, because a clean run's entire stdout is that one `INFO` line.
- **B4 independent re-freeze** — `--freeze` into a fresh directory reproduced **all four** frozen
  files byte-for-byte: packet, run.log, freeze.txt and `expected.json` (`1ab17670…`); the JSON diff
  modulo the `frozen_at` date field is empty. Because the freeze was executed by the same tool
  revision, §5-style independence is not claimed for it: it proves the baseline is *reproducible
  from the live bytes*, not that it is right. The genuinely independent legs are B1–B3 and the
  digest recomputations in §2.

## 5. Leg C — tamper and falsifiability drills (copies of the copied tree, one mutation each)

| # | mutation | observed | reading |
|---|---|---|---|
| T1 | append a line to `examples/culture-d2/packet.d2.yml` | exit **2**; `FAIL frozen-input: … frozen e0f21509… live 9f4cb44a…`; `CANNOT EVALUATE — gate not reached` | source drift fail-closed before any verdict |
| T2 | baseline `packet_sha256` → `000…0` | exit **1**; gate still exit 0; `FAIL frozen-packet: assembled sha256 2a058f78… vs frozen 000000000000…` | the packet pin bites |
| T3 | baseline `declared.glossary_entries` 20 → 19 | exit **1**; `FAIL declared-expectations: baseline declares {…19…}, the exercise declares {…20…}` | baseline/declaration disagreement caught |
| T4 | append a comment to frozen `packet.md` | exit **0**, PASS | **silent** — see F3 |
| T5 | append a comment to `tools/gates/handoff-packet-check.py` | exit **1**; `FAIL frozen-packet` + `FAIL frozen-fields: drifted fields: artifact_manifest` | executor revision surfaces through the packet's manifest row |
| T6 | append a comment to the contract | exit **2**; `FAIL frozen-input: … frozen 5f4c02bf… live 80d3e0cc…` | contract drift fail-closed |
| T7 | append a comment to `tools/exercise-handoff-e2e.py` (the executor itself) | exit **1**; `FAIL frozen-packet` + `frozen-fields: artifact_manifest` (row `A-TOOL-EXERCISE` carries the self-digest) | executor edit caught — but as a verdict mismatch, not a revision class |
| T8 | delete frozen `packet.md` | exit **0**, PASS | **silent** — same class as T4 |
| T9 | delete `packet_sha256` from the baseline | exit **2**; `frozen baseline is missing 'packet_sha256'` | malformed baseline fail-closed |
| T10 | baseline → `{ not json` | exit **2**; `frozen baseline is not valid JSON: …` | malformed baseline fail-closed |

Class mapping observed: source/contract drift → 2 (gate not reached); frozen-packet/field/glossary
mismatch and a `declared`-block disagreement → 1; absent/malformed baseline → 2. The two 1-classes
are exactly the standard's `failed` row for "digests match; observed differs from expected", while
its `gate_revised` row would want 2 for T5/T7 (see F4).

## 6. Leg D — regression legs in the same copy

| leg | command | observed |
|---|---|---|
| gate self-test | `python3 tools/gates/handoff-packet-check.py --selftest` | exit 0, `selftest: OK — fixture findings 11 across 9 ids (…)` |
| round-9 frozen baseline still replays | my `verify.py` (digest → pin → verdict) over `reports/round-9/baselines/handoff-packet-check/expected.json`, run in the copy with the baseline-local `packet.md` | step 1 OK, step 2 `gate_sha256` match, step 3 exit 0, finding set `[]`, stdout `7c581047…` equal to the pin (`smoke-r9pre.json`) |
| gate battery | `python3 tools/check-gate-battery.py` (copy and lane) | `{'battery_exit': 2, 'fail': 0, 'pass': 7, 'unevaluable': 0}`; five baselines `pinned`; `BASELINE-GATE-UNCOVERED` ×2 (myth, naming — pre-existing); **seven findings on `expected/handoff-exercise/r11/expected.json`** → reading `no baseline` (F2) |

## 7. Findings and dispositions (this shard reports; it repairs nothing)

- **F1 — the exercise's `--selftest` is red at revision `38d1cba4…` (defect).** Reproduced in the
  lane tree (22:10Z) and in the copied tree (22:09Z): exit 1 with
  `AssertionError: ["evaluated: cannot hash examples/culture-d2/components/02-phonology.yml: [Errno 2]
  No such file or directory: …/handoff-selftest-*/fixture/examples/culture-d2/components/02-phonology.yml"]`.
  The fixture root the selftest builds does not contain the D2 component that the digest step then
  reads (`build_fixture_root`, `tools/exercise-handoff-e2e.py:1244`). The O-claim's
  "selftest with positive + malformed controls" leg is therefore not met at this revision, even
  though the plain run is clean. Owner: the O02–O05 single writer. Corroborates the round-11 draft's
  O row (`reports/round-11/report-draft.md`, "selftest still broken (fixture missing
  `02-phonology.yml")`). **Status at phase-2 revision `a21934ad…`: fixed — `--selftest` exits 0 with
  "positive run … plus 17 controls" (§10.1).**
- **F2 — the baseline's home is inside a gate-battery default root (integration hazard).**
  `tools/gates/expected/handoff-exercise/r11/expected.json` is discovered by
  `tools/check-gate-battery.py` and yields `BASELINE-GATE-UNKNOWN` ×1 (`declared gate None`),
  `BASELINE-EXTERNAL-INPUT` ×5 (its `inputs` resolve outside the baseline directory) and
  `BASELINE-EXPECTED-ABSENT` ×1 (it uses `declared`, not an `expected` block) → the battery reads
  `no baseline` for it. Measured on the **final** baseline bytes (digest `1ab17670…`, mtime
  22:08:52Z) in both the lane (22:11Z, `battery-live.out`) and the copy. `reports/round-11/handoff/design.md`
  §8 explicitly warned against this home, and `reports/round-11/depth/design-review.md` DR-16
  reported the same mechanism while the file was still being written; this receipt confirms it on
  the frozen bytes. Disposition options for the integrator: re-home the baseline to a non-gate root
  (the design's own first choice), give it a gate-conformant schema, or teach the battery to skip
  non-gate baselines. Not repaired here — the file belongs to the O02–O15 owners and the battery to
  the D/O integration chain. **Status at phase-2 revision `a21934ad…`: fixed in-flight — the baseline
  was re-homed to `reports/round-11/handoff/expected.json`, and the battery's baseline block is back
  to the pre-existing two `BASELINE-GATE-UNCOVERED` findings (§10.1, battery row).**
- **F3 — the frozen record artifact is not digest-enforced by the run (limit, not a defect).**
  Editing (T4) or deleting (T8) `tools/gates/expected/handoff-exercise/r11/packet.md` leaves the
  exercise at exit 0: the run pins the *assembled* packet against `expected.json.packet_sha256` and
  never reads the record copy. The closing check is external and trivial —
  `sha256sum packet.md` must equal `expected.json.packet_sha256` (today `2a058f78…`, verified) — and
  it is the check this rerun would run as the reviewer. If the lane wants the record protected at
  run time, the baseline would have to pin `packet.md`/`run.log` as inputs of the exercise.
- **F4 — revision drift is classified as a verdict failure, not a could-not-evaluate (observation).**
  T5 (gate edit) and T7 (executor edit) exit **1** with `frozen-fields: artifact_manifest`, because
  both digests are carried inside the assembled packet; the standard's §6 would read a changed
  executor as `gate_revised`, exit 2. The baseline does record `tools` digests, so a reviewer can
  re-classify; the author may want the run to compare `tools` before the verdict and raise the
  revision class explicitly. Reported, not asserted as wrong: the tool's docstring documents exit 1
  for "digest mismatch against the frozen packet".
- **F5 — `TMPDIR` must already exist (minor robustness).** With `TMPDIR` pointing at a non-existent
  directory the tool's isolation falls back under `/tmp` (observed in drill T7:
  `gate-exit: exit 0 … from /tmp/handoff-exercise-v9sweu5i/isolated`), which on this host is
  inode-exhausted; the operator rule's convention is only safe when the directory is created first.
  Both of this shard's loops created it; the note is for the tool's docs.
- **F6 — adjacent, cited not absorbed.** Seven filed receipt files of earlier rounds are rewritten in
  the worktree during round 11 (`reports/round-10/coverage/index-update-22.md`; `reports/round-{5,6,7,8,9}/validation.json`;
  `reports/round-6/checkpoint-validation.json`), mtimes 19:01–19:03 local; cross-checked by
  `git status --porcelain` + `git diff --stat` at 22:11Z (e.g. round-5 `−361` lines net). It is
  already logged, with the same file list, in `reports/round-11/report-draft.md` §"Known integration
  hazards" 1; this shard repeats it only so the frozen-rerun record is not read as endorsing those
  bytes, and makes no repair (filed bytes are not this shard's to touch).

## 8. What this establishes — and its limits

Establishes (each with the command in §§3–6):

- the committed baseline is **replayable outside its author's tree**: a copied tree, a second
  (this-shard-owned) isolation, my own field/glossary counter and my own digest resolution all
  reproduce exit 0, `fields=16/16`, `glossary-entries=20`, `findings=0`, packet `2a058f78…`,
  `contract_ref …5f4c02bf…`, 13/13 component digests;
- the baseline is **falsifiable**: ten single-mutation drills fire the intended classes, including
  four that stop before the gate (source, contract, missing key, malformed JSON);
- the exercise baseline does **not** survive round-11's own battery default roots (F2), and the
  exercise's own self-test is red (F1) — both are findings, not caveats.

Limits, stated so the reading cannot be laundered:

- **Trusted base.** A digest chain proves bytes, never the tool that reads them (the standard's
  KTD-FR-S-0007). The exercise tool and the gate were authored by lane peers in this round; my
  re-execution cannot certify their internals, only their reproducibility. The same machine, the
  same Python, the same clock: this is re-execution, not reproduction on foreign hardware.
- **Bounded independence.** B1/B2 are shallow second implementations of rules the lane itself fixed
  (contract §4 field names; the gate's glossary recognition); B3 re-runs the same gate; B4 re-runs
  the same tool. The D2/D3 artifact contents are not re-derived here — their correctness is the
  D-claim's business, and the record counts above are copied from the exercise's manifest, not
  independently recounted.
- **No design or canon claim.** A replayed green says these bytes produced this verdict. It says
  nothing about whether the packet is a good design, whether its sources are real, or whether lore
  should accept anything; canon standing remains lore-shokunin's alone (`PROVINCE.md`).
- **Time-bounded.** Every digest above is a measurement at 22:07–22:14Z on worktree HEAD `e3ef171`
  plus untracked round-11 output. If any named byte changes after that, this rerun's claim lapses
  and the rerun must be repeated (the tool alone was revised three times inside the window).

## 9. Receipts retained (`.scratch/r11-o15/`, gitignored; sha256 of each)

| receipt | sha256 |
|---|---|
| `run-primary.out` / `run-primary.err` | `4793c0d3…` / `e3b0c442…` (empty) |
| `run2.out` / `run3.out` (determinism) | `b11ed62b…` / `75abc2d2…` |
| `selftest-run2.txt` (copy) / `selftest-lane-2.txt` (lane) | `3031b260…` / in F1 |
| `freeze-ind.out` + `tree/.scratch/r11-o15/frozen-independent/{expected.json,packet.md,run.log,freeze.txt}` | `c7708106…`; `1ab17670…`, `2a058f78…`, `2346783b…`, `003fe548…` |
| `drills/{t1..t10}*.out`, `drills.sh` | `673f9f3f…`, `6cb84128…`, `bed2982c…`, `f883926a…`, `f32ce8ea…`, `74563ed4…`, `a2cd3998…`, `ae6813ec…`, `82acf075…`, `720f5402…`; script `a3268b9a…` |
| `battery-live.out` / `battery-with-exercise-baseline.out` | `6c9bab02…` / `d81608c9…` |
| `smoke-r9pre.json` (round-9 baseline replay) | `7a8dbf22…` |
| tooling: `copy-tree.sh`, `verify.py`, `independent-envelope.py`, `independent-contract-refs.py` | `9cf81305…`, `aa70fa0c…`, `23709e89…`, `adce9aea…` |

FILES: reports/round-11/handoff/frozen-rerun.md
SUMMARY: The round-11 handoff exercise baseline replays clean in an independently copied tree (exit 0, 16/16 fields, 20/20 glossary entries, 18/18 digest claims, re-freeze byte-identical), with ten tamper drills firing as intended; two reds reported — the exercise `--selftest` fails at revision `38d1cba4…` (missing `02-phonology.yml` in its fixture root) and its baseline's home under `tools/gates/expected/**` trips seven gate-battery findings.

## 10. Phase 2 — the re-homed baseline, re-measured (current state, 22:19–22:21Z)

The round moved while this shard ran: the O-shard removed the phase-1 baseline home, rewrote the
exercise tool (new CLI: `--baseline PATH`, `--root DIR`, `--keep DIR`, `--json`, `--quiet`) and
re-froze a baseline at the design's declared home. The legs of §§3–6 were therefore re-run in a
**fresh copy** (`$S/tree2`, made 22:19Z) against the new bytes. Nothing in phase 1 was re-written;
this section is additional evidence.

### 10.1 Current bytes and legs

| object | sha256 (22:19–22:21Z) |
|---|---|
| `tools/exercise-handoff-e2e.py` (revision under test) | `a21934ade22b2cda338645ee389c7f848256348446d8a79f38a9c9ff827d2005` |
| `reports/round-11/handoff/expected.json` | `a94f9ded9d0938ec1510a1834b83162635c9e94a04b70461d5db0b98a0031d7a` (`baseline_digest 19f39f84…`) |
| `reports/round-11/handoff/packet.md` | `6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f` |
| `reports/round-11/handoff/run.log` | `60d2965858c1f25c6d76f44bafdabbb2ea512fb271154274b943d7f6de21047e` |
| `reports/round-11/handoff/freeze.txt` | `56607f29e7e83eccc6f05d7760f8246066e11a5de4bd8943d37022868627e3d1` |
| gate (unchanged) | `e2fa3223…` |

| leg | observed | status |
|---|---|---|
| A replay in the fresh copy (`--json`) | exit 0; 8 × `OK` — `input-digest` (21 read-set files), `preflight`, `cross-references`, `gate-exit`, `gate-scan fields=16/16 glossary-entries=20 findings=0`, `frozen-packet 6583b6bd…`, `frozen-glossary` (20 ids), `preservation` (21 files byte-identical before/after) | **PASS** (`p2-run-plain.out` `0c6f6c83…`) |
| B1 my counter over the new frozen packet | `fields=16/16`, 1 glossary table, 20 rows | **PASS** |
| B2 my cross-reference resolution | contract digest == live `5f4c02bf…`; **33/33** per-path digest claims match; 0 unresolved | **PASS** |
| B3 my own gate run (own isolation, foreign cwd) | exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0` | **PASS** |
| B4 my own re-freeze | `expected.json`, `packet.md`, `run.log` reproduce byte-identically; `freeze.txt` differed only in its diff line (theirs recorded `re-frozen packet_sha256: 72739729… -> 6583b6bd…`, mine `no tracked value changed since the previous freeze`) — the lane's `freeze.txt` at 22:20Z equals mine (`56607f29…`) | **PASS** |
| F `--selftest` | **exit 0** — `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0) plus 17 controls`, including ten malformed-packet controls with named gate findings, a dropped-glossary-row control that fails preflight (the gate alone counts 19 silently), `tamper baseline` → exit 2 `E2E-BASELINE`, `tamper read-set` → exit 1 `E2E-DIGEST`, `tamper scan expectation` → exit 2 `E2E-BASELINE`, `missing artifact` → exit 2 `E2E-ARTIFACT` (`p2-selftest.out` `3ffc034e…`) | **PASS — F1 fixed in-flight** |
| D battery (fresh copy) | `{'battery_exit': 2, 'fail': 0, 'pass': 7, 'unevaluable': 0}`; findings back to the pre-existing `BASELINE-GATE-UNCOVERED` ×2 (myth, naming); five baselines `pinned`; **the exercise baseline is no longer discovered** (`p2-battery.out` `c5f68d15…`) | **F2 fixed in-flight** |

### 10.2 Phase-2 tamper drills (fresh copies, one mutation each; `drills2/`)

| # | mutation | observed |
|---|---|---|
| p2t1 | append to `examples/culture-d2/packet.d2.yml` | exit **1**; `FAIL input-digest: … frozen e0f21509… live 9f4cb44a…`; `E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen` |
| p2t2 | baseline `packet_sha256` → `000…0` | exit **2**; `E2E-BASELINE: baseline integrity digest mismatch — the baseline file was edited without re-freezing` |
| p2t4 | append a comment to `reports/round-11/handoff/packet.md` | exit **0**, PASS — silent (F3 persists; an external `sha256sum packet.md` vs `packet_sha256` is the closing check) |
| p2t5 | append a comment to the gate | exit **1**; `FAIL input-digest: tools/gates/handoff-packet-check.py: frozen e2fa3223… live e45b3f14…`; `E2E-DIGEST` names the file |
| p2t7 | append a comment to `tools/exercise-handoff-e2e.py` (the executor) | exit **0**, PASS — **silent (new finding F7)** |
| p2t9 | baseline → `{ not json` | exit **2**; `E2E-BASELINE: frozen baseline is not valid JSON: …` |

### 10.3 Deltas phase 1 → phase 2, and the new gap

- **Class changes (observed, for the reviewers to rule on):** an edited *input* moved from exit 2
  (`frozen-input`, gate not reached — `gate-frozen-run-standard.md` §6's `snapshot_tampered` class)
  to exit **1** (`E2E-DIGEST`, a verdict failure). An edited *baseline* moved from exit 1
  (`frozen-packet`) to exit **2** (`E2E-BASELINE`, refused by the baseline's own integrity digest) —
  strictly stronger. A gate edit is now caught earlier and named precisely (`E2E-DIGEST` on the read
  set) instead of surfacing through the packet's `artifact_manifest`.
- **F7 (new, phase 2) — the executor is not pinned anywhere.** `p2t7` shows a tool edit leaving the
  run at exit 0. The tool is not in the 21-file read set, the new packet carries no
  `A-TOOL-EXERCISE` manifest row (`grep -n "A-TOOL\|exercise-tool" reports/round-11/handoff/packet.md`
  → no match), and the baseline has no `tools` map; neither `expected.json` nor `freeze.txt` records
  the tool digest. Under the phase-1 schema the same edit was caught (T7, exit 1, via
  `artifact_manifest`), so this is a removed guard, not a pre-existing hole. Recommended closure
  (owner: the O02–O05 writer): put the tool's digest into the read set or into the baseline next to
  `baseline_digest`, with the self-digest recorded (a tool cannot enforce its own hash at run time,
  but a reviewer can).
- **F3 persists in phase 2**: the frozen `packet.md` record is still editable/deletable without
  moving the run (p2t4 exit 0). Same closing check, run here:
  `sha256sum reports/round-11/handoff/packet.md` = `6583b6bd…` = baseline `packet_sha256` (verified
  22:20Z).
- **Tool churn observed across the window** (one sample per revision seen, 12-hex):
  `c202927e` (22:07:13Z) → `9135e1fb` (22:08) → `38d1cba4` (22:09) → `6d3a34d0` (22:12) →
  `d7f26a6a` (22:14:09) → `e74e5aea` (22:14:29) → `d5b346b8` (22:16:09) → `a21934ad` (22:17:29,
  stable through 22:24Z at 20-second sampling). The frozen baseline names the revision it was frozen
  under only in the phase-1 schema; in phase 2 it does not (F7).

### 10.4 Phase-2 receipts (`.scratch/r11-o15/`, sha256)

`p2-run-plain.out` `0c6f6c83…` · `p2-run1.json` `da53a6a8…` · `p2-selftest.out` `3ffc034e…` ·
`p2-freeze.out` `490bff60…` · `p2-battery.out` `c5f68d15…` · `phase2-digests.txt` `d0a210bd…` ·
`drills2.sh` `6d1dc67d…` · drills `p2t1 7aa33263…`, `p2t2 ab1bc5be…`, `p2t4 0b11daa2…`,
`p2t5 3e9a0327…`, `p2t7 160affa1…`, `p2t9 121561c2…`.

**Phase-2 verdict, stated with its clock:** on tool `a21934ad…` and baseline `a94f9ded…` the exercise
replays clean in a copied tree, its self-test is green, the re-homed baseline no longer trips the
gate battery, and an independent freeze reproduces the baseline bytes; the opens are F3 (record
artifact unprotected), F4-style class questions and the new F7 (executor unpinned). If any named byte
changes after 22:21Z, this phase-2 claim lapses and the rerun must be repeated.
