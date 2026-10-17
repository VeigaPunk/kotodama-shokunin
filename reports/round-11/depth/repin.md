# R11-D08 — frozen re-pin for the wiring change: before/after pins and the mechanics

- round: 11 (loop 1 of 3, build round 4 of 4) · shard: D08 (frozen re-pin mechanics) · claim **D (depth)**
- date: 2026-10-17 (all stamps UTC; local = UTC-03:00) · lane revision at first measurement: `94ca098b8ab03be52ec80f6925538e5e2c0ed327` (`git rev-parse HEAD`, round-11 declared baseline)
- write scope: **this file only** (`reports/round-11/depth/repin.md`). Nothing under `tools/**`, `examples/**`, `corpus/**` or `reports/round-{8,9,10}/**` was written by this seat; no commit was made. All mirrors, generations and receipts quoted below live under `.scratch/r11-d08/` (gitignored) and are reproduced by the commands in §9.
- measurement stamps are load-bearing: sibling round-11 seats were writing `tools/**` while this shard ran. Every pin below names the digest *as read at its stamp*; a later re-read is a new measurement, never a silent continuation.

## 0. Verdict (read this first)

| surface | before (measured) | after (measured) | state |
|---|---|---|---|
| legacy D2 replay manifests (`tools/gates/frozen/round-3/MANIFEST.tsv` `d5337590…`, `attempt-1` `613e5945…`) | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` → `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate`, **exit 2**, every row `gate_digest_mismatch` (22:01:09Z) | re-pin demonstrated: new generation `round-11-pre` (manifest `53229af6…`), **7/7 rows `pin-only`, every verdict byte-identical**, `replay-frozen` → `REPLAY OK: 7/7`, exit 0 | mechanics **PROVEN**; the generation itself is a candidate, not committed (§3, §7) |
| legacy `attempt-1` manifest | same 7/7 `gate_digest_mismatch` | generation `round-11-pre/attempt-1` (manifest `69695e6f…`), 7/7 `pin-only`, replay 7/7 exit 0 | mechanics **PROVEN** |
| the `r9-pre` baselines the battery reads (8 files across the 7 gates) | battery over the three baseline roots: 8 baselines found, **8 `pinned`**, 7 gates covered, exit 0 in a mirror at 22:0xZ | re-pin demonstrated against a simulated gate edit: one baseline per gate re-pinned `pin-only` into a current-generation root, battery on that root 7 `pinned`, exit 0 | mechanics **PROVEN**; pins are valid today and unbroken (§4) |
| wired generation for the typed run, `tools/gates/frozen/round-11/MANIFEST.tsv` (D05's `--freeze`; **landed in the lane at 22:14Z**, manifest `4ddb911c…`) | before the wiring the round-3 pins name gate revisions that no longer exist (§1.4 of `reports/round-11/depth/design.md`) | 10 rows (5 gates × typed/legacy) — replay from **lane bytes** in a mirror root: **10/10 reproduced, exit 0**; replay *in place* reads 10/10 `mirror_unsafe` only because `TMPDIR` was inside the repo root (§5, §6.5) | **GREEN** |
| `check-gate-battery.py` in the live lane | — | **exit 2**, 9 baselines found, 8 `pinned`, 1 `no baseline` — the O-shard's in-flight `tools/gates/expected/handoff-exercise/r11/expected.json`, not a gate baseline (§6.2) | **RED, cause named, not this seam's fix** |

Reproduction only. `REPLAY OK` asserts that a recorded verdict re-observed identically — never that a design passed; one re-pinned row reproduces a recorded **exit 2** verdict and stays red (§3).

## 1. What "the D2 frozen manifests" resolves to

Measured sweep (2026-10-17T22:0xZ, `find tools/gates/frozen -name MANIFEST.tsv`; `find tools reports -name expected.json -not -path "*/scratch/*"`):

| generation | file | digest | rows | what it pins |
|---|---|---|---|---|
| round-3 | `tools/gates/frozen/round-3/MANIFEST.tsv` | `d5337590b343c65b42fd6e55457862fa325c138ad652e59c81b887daf9971399` | 7 | 5 packet gates over `examples/culture-d2/packet.d2.yml` (5 rows) + `provenance-audit` over two corpus files |
| round-3 `attempt-1` | `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | `613e59452bf76422e85ce4586cc00b85588e03b974a67e3ad1897f589f7b06a1` | 7 | same gates, a divergent packet snapshot (`f424fcf1…`) |
| round-4 | — | **no `MANIFEST.tsv`** | 0 | five `.out` files only, no pins; re-measured 2026-10-17T22:20Z: `python3 tools/replay-frozen.py tools/gates/frozen/round-4/MANIFEST.tsv` → exit 2, `COULD-NOT-EVALUATE manifest_unreadable`, output `sha256 1dc089cc51958f5435b2fd720a8ce8d92ddd337107f21910794b911b1624882b` — **byte-identical to the round-10 drift ledger's recorded row** (`reports/round-10/drift/ledger.json`, `shard-09`), so the negative claim and one ledger row are hash-stable |
| r9-pre baselines | 8 `expected.json` files across the 7 gates under `tools/gates/expected/`, `tools/gates/frozen/`, `reports/round-9/baselines/` | e.g. `tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json` | 8 | one `gate_sha256` pin + `inputs` digest map + finding-ID set each |
| round-11 (wired) | `tools/gates/frozen/round-11/MANIFEST.tsv` (written by `python3 tools/typed-gate-flow.py --freeze`) | `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376` | 10 | the same five gates over the **typed** packet (5 rows) and the raw packet (5 rows) |

Before-pin table (round-3 rows; `awk -F'\t'`, 2026-10-17T22:01Z):

| gate | round-3 pin (`gate_sha256`) | live gate at 22:09:56Z | snapshot (`input_sha256`) | recorded verdict |
|---|---|---|---|---|
| `phonology-sanity-gate.py` | `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655` | `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230` | `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4` | exit 1, 3 findings |
| `lexicon-coverage-audit.py` | `63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80` | `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287` | `54be6319…` | exit 0, 0 |
| `myth-consistency-gate.py` | `26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5` | `5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08` | `54be6319…` | exit 1, 1 |
| `costume-era-consistency-gate.py` | `29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` | `54be6319…` | exit 1, 10 |
| `naming-collision-gate.py` | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | `54be6319…` | exit 1, 20 |
| `provenance-audit.py` ×2 | `4aaea6e98b9776922708692e6e0f38f76ef7323e3c748cbdf82c789eb77e1e7a` | `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a` | `a916a4c2…` (mesoamerica), `7b3bdc80…` (gate-frozen-run-standard) | exit 0, 0 (both) |

The `attempt-1` rows differ only in the packet snapshot (`f424fcf1b9613eb21d2901b19819a7e6c2a998cbcbd492a1a210d94eaae400cd`) and in row 5's recorded verdict (**exit 2**, 1 finding — a recorded could-not-evaluate that must be reproduced, not cured). Corpus rows are identical to round-3's.

Live readings at 22:01:09Z: both manifests `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced`, exit 2, sole reason `gate_digest_mismatch` on all six gate paths. Nothing reports `snapshot_tampered` or `expected_output_tampered`: the frozen snapshots and the recorded outputs still equal their pins; only the gate revisions moved on. This is the state the design's §1.4 names, and the reason a re-pin must produce a **new generation** rather than edit round-3's pins.

## 2. Mechanics — what a re-pin may and may not do

The standard (`corpus/knowledge/verification/gate-frozen-run-standard.md` §3, §6) fixes the shape: a later gate revision or input edit produces a **new** baseline; existing baselines are never rewritten. A re-pin therefore has exactly one legitimate liberty — refresh `gate_sha256` to the live gate bytes — and must prove everything else held:

1. **Verify the source record first.** Snapshot bytes against `input_sha256`; recorded output bytes against `output_sha256`; recorded `finding_count` against the `FINDING ` lines of that recorded output. A source row that fails its own pins is `unrepinnable` — a tampered record is never carried forward (exit 2, nothing written).
2. **Re-run the live gate over the frozen snapshot** (never over the live input), in an isolated mirror, and compare exit code, finding count and stdout bytes against the record.
3. **Classify.** Byte-identical verdict → `pin-only`, carry it. Any difference → `verdict-delta` — **refused** (exit 1, nothing written) unless `--allow-verdict-change`, which records the observed verdict as a new measurement and prints both verdicts. A re-pin that could bless its own change is exactly the circularity the round's D22 review targets; this is the guard.
4. **Emit append-only.** A new generation directory: copied snapshots under `inputs/<input path>`, one `.out` per row (disambiguated by input stem when a gate has several rows), a rewritten `MANIFEST.tsv`, plus `repin.json` (per-row before/after pins and verdicts) and `freeze.txt`. An existing destination is refused; `..`, absolute and flag-like paths are refused before normalization; a duplicate `(gate, baseline-id)` across the three known baseline roots is refused so a re-pin cannot create an ambiguous id.
5. **Self-verify.** The emitted generation is fed back through `python3 tools/replay-frozen.py <new MANIFEST.tsv> --repo-root <tree>`; the tool exits 0 only on `REPLAY OK: n/n … exit 0`.

The implementation is `repin-frozen.py` (scratch, `sha256 0b06c9baa14f77a90fe8740119f26d922fc22a05fd5a6edb16558e77d8d2b79f`, `.scratch/r11-d08/repin-frozen.py`), stdlib-only, two modes: `--manifest … --generation …` for replay generations and `--baseline … --target-dir … --target-id …` for `expected.json` baselines (finding-ID **set** comparison, `^FINDING ([^\s:]+)`, the standard's §4 contract). Its own selftest is `python3 .scratch/r11-d08/repin-frozen.py --selftest` → **31/31 checks passed, exit 0** (receipt `.scratch/r11-d08/selftest-r11-d08.txt`, `sha256 4ed93bdc14938b25454a91b92c405a5478e5c1245531311624dd9c95ffaded95`). Controls, each with a positive and a negative leg: pin-only → written and replay-verified green; verdict-delta → exit 1, nothing written; delta accepted explicitly → recorded as a new measurement; tampered snapshot / recorded output → exit 2 `snapshot_tampered` / `expected_output_tampered`; existing generation or baseline → exit 2; traversal and flag-like paths → exit 2; duplicate baseline id → exit 2. The extraction contract was validated independently against every committed baseline: for all 8 `expected.json` files, the committed `run.log` FINDING-ID set equals `expected.findings` exactly (`tools/gates/expected/*/r9-pre/run.log`, `tools/gates/frozen/*/r9-pre/run.log`, `reports/round-9/baselines/*/run.log`, 22:12Z).

## 3. Demonstrated re-pin — the replay-manifest surface

Mirror `.scratch/r11-d08/mirror/` = byte copies of the seven live gates + `tools/replay-frozen.py` + `tools/gates/frozen/round-3/` (verified: every mirror gate digest equal to its lane digest at 22:05:26Z). Both manifests were re-pinned with the live gate bytes:

| step | command (cwd = mirror) | observed |
|---|---|---|
| before | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | 0 reproduced, 7 could-not-evaluate `gate_digest_mismatch`, exit 2 |
| re-pin | `python3 .scratch/r11-d08/repin-frozen.py --manifest tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <mirror> --generation tools/gates/frozen/round-11-pre --json` | **7/7 `pin-only`**, `verdict_delta` 0, `unrepinnable` 0, generation written, `verified_green: true`, exit 0 |
| after | `python3 tools/replay-frozen.py tools/gates/frozen/round-11-pre/MANIFEST.tsv` | `REPLAY OK: 7/7 rows reproduced`, exit 0 |
| `attempt-1` | same tool, `--manifest …/attempt-1/MANIFEST.tsv --generation tools/gates/frozen/round-11-pre/attempt-1` | 7/7 `pin-only`, replay `7/7`, exit 0 |
| revision-specificity | append one comment line to the mirror's `phonology-sanity-gate.py`, replay `round-11-pre` again | 6 reproduced, 1 `gate_digest_mismatch`, exit 2 — the generation pins *its* gate bytes, not "the current ones" |

After-pin table (generation `round-11-pre`, manifest `sha256 53229af65633a18a2e26fbd0a6fdc6c24f32d31fea4cff9eb30698b41c09a94a`; `attempt-1` `69695e6f1266ccdb037d9591131ea9b301281427fdde468a466d09a4ed1463f4`):

| row | gate | pin before → after | verdict carried (exit / findings / stdout sha) |
|---|---|---|---|
| 2 | phonology-sanity | `fb05c644cafb…` → `d5fe087ffb23…` | 1 / 3 / `1ce5f0cdabad…` |
| 3 | lexicon-coverage-audit | `63ee4ec6b151…` → `2c4dd39702a1…` | 0 / 0 / `e3b0c44298fc…` (empty) |
| 4 | myth-consistency | `26d246e9936d…` → `5368b13542cd…` | 1 / 1 / `ea56c2d3cd71…` |
| 5 | costume-era-consistency | `29a9361c7b96…` → `e6bffd7020c0…` | 1 / 10 / `129c4f5a293f…` |
| 6 | naming-collision | `8c5afb0a5abc…` → `d9e4e8f4f93a…` | 1 / 20 / `e81bab661a99…` |
| 7 | provenance-audit | `4aaea6e98b97…` → `8a96aaf4ccd1…` | 0 / 0 / `57a537aeeea2…` |
| 8 | provenance-audit | `4aaea6e98b97…` → `8a96aaf4ccd1…` | 0 / 0 / `1b8bf0b83b96…` |

Two emitter defects were found and fixed by running this loop, both of the kind a hand re-pin hits: the two `provenance-audit` rows initially collided on one `.out` filename (fixed: input-stem disambiguation, matching round-3's own `provenance-mesoamerica-primary-sources.out` naming), and the emitted `inputs/` tree initially nested the full snapshot path instead of the graded input path (fixed: `inputs/<input>`), which the replay then refused as `expected_output_tampered` — the fail-before/pass-after pair is in the receipts `.scratch/r11-d08/repin-round3.json` (final run) versus the discarded first run.

`attempt-1` row 5 carries a **recorded exit 2** verdict (costume gate could-not-evaluate over the attempt-1 packet). The re-pin reproduced it byte-identically and the generation replays 7/7 — reproduction does not launder a red verdict into a green one, and no leg here should be read as the packet passing.

## 4. Demonstrated re-pin — the baseline surface the battery reads

The wiring change must keep `python3 tools/check-gate-battery.py` green, and that tool verifies every discovered `expected.json`'s `gate_sha256` against the live gate. Sequence measured in `.scratch/r11-d08/mirror2/` (a full `tools/` copy plus `reports/round-9/baselines/`, with the O-shard's in-flight `tools/gates/expected/handoff-exercise/` removed to isolate this measurement):

| step | command | observed |
|---|---|---|
| A — pre-edit | `python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines` | exit **0**; 8 baselines found, **8 `pinned`**, 7 gates covered, `gates_uncovered: []`; selftests `pass: 7, fail: 0` |
| B — simulated wiring edit | append one comment line to the `phonology-sanity-gate.py` copy; same command | exit **2**; 8 found, 7 `pinned`, 1 **`gate_revised`** (`expected/phonology-sanity-gate/r9-pre/expected.json`), `unevaluable: 1` |
| C — re-pin to a current-generation root | `repin-frozen.py --baseline <each of 7 r9-pre baselines> --target-dir tools/gates/r11-baselines/<gate>/r11-pre --target-id r11-pre` | 7/7 **`pin-only`**, each written; verdicts carried: 21 / 1 / 0 / 18 / 6 / 0 / 3 finding IDs, exits 1/1/0/1/1/0/1 |
| C — battery on the new root | `python3 tools/check-gate-battery.py --baselines-root tools/gates/r11-baselines` | exit **0**; 7 found, **7 `pinned`**, 7 gates covered, `unevaluable: 0` |
| D — old roots after the re-pin | battery over the original three roots | exit **2**, 7 `pinned`, 1 `gate_revised` — the superseded `r9-pre` baseline stays red **by design** (append-only: it is not edited to match) |
| E — second gate edit | edit the phonology gate again; battery on the `r11-baselines` root | exit **2**, `gate_revised` on `r11-pre` — a re-pin pins *bytes*, so it must be re-run whenever the gate moves again |

Reading: after any gate byte changes, the superseded baseline is *supposed* to read `gate_revised`; "battery remains green" therefore has to be scored against a **current generation root**, not against every baseline ever committed — or the wiring must not touch gate bytes at all. Both remain open decisions for the integrator (§7).

## 5. The wired generation — the after-pins for this round's change

Measured in `.scratch/r11-d08/mirror4/` (isolated copy of `tools/{typed-gate-flow,d2-typed-labels,assemble-d2,replay-frozen}.py`, `tools/gates/*.py`, `examples/culture-d2/**`), at `tools/typed-gate-flow.py` `sha256 7bff2edf1c23dc6d10915e41581dcbea6c9b1344f5c5204246c85967bdb39496` (22:10:59Z revision). **Moving target:** the same file read `ae55e6fa423d6d6a2574933d75402cafcba3f77e25164755eaf159da838a77d2` at 22:21Z — a sibling seat edited it while this file was written, so the generation below pins the 22:10:59Z revision and `--freeze` must be re-run after the flow settles (the re-pin machine is revision-agnostic; only the pins move).

| step | command (cwd = mirror) | observed |
|---|---|---|
| e2e | `python3 tools/typed-gate-flow.py --json` (after `--emit`) | exit **0**, `ok: true`; findings **16** = `{hold: 15, note: 1}`, ids `D2L-FORM-UNRESOLVED` / `D2L-NATIVE` / `D2L-RANK`; checks `typed-packet-pinned`, `no-untyped-records`, `sound-channel-clean`, `differential-exact`, `owed-slots-crosscheck` all `true`; `sound_channel.off` = `GAR-01..GAR-10`, `on: []` |
| channel differential | same run | naming-collision `legacy_findings 17 → typed_findings 7`, `removed 10` = off-records 10, `added 0`; phonology 3→3, costume/lexicon/myth 0→0, `added 0` everywhere |
| freeze | `python3 tools/typed-gate-flow.py --freeze tools/gates/frozen/round-11` | `froze 10 row(s) into tools/gates/frozen/round-11`; manifest `sha256 4ddb911c…` |
| verify | `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv --repo-root <mirror>` | **`REPLAY OK: 10/10 rows reproduced`, exit 0** |

The lane then landed its own `tools/gates/frozen/round-11/MANIFEST.tsv` at 22:14Z — **byte-identical to the mirror's** (`sha256 4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376`), with every snapshot and `.out` digest equal to the recorded pins (checked row-wise). Replaying *that* generation from lane bytes in a clean mirror root: **10/10 reproduced, exit 0** (`.scratch/r11-d08/mirror5/`, receipt `replay-round11-lane-bytes.json`). Replaying it *in place* in the lane reads 10/10 `mirror_unsafe` and exit 2 — an artefact of `TMPDIR` sitting inside the repo root, not drift (§6.5).

After-pins in the wired generation (manifest rows; typed packet snapshot `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb`, raw packet `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`):

| rows | input | gate pins (`gate_sha256`) | recorded verdicts |
|---|---|---|---|
| 1–5 (typed) | `examples/culture-d2/packet.d2.typed.yml` | naming `d9e4e8f4…`, phonology `d5fe087f…`, costume `e6bffd70…`, lexicon `2c4dd397…`, myth `5368b135…` | naming exit 1 / 7 · phonology exit 1 / 3 · costume, lexicon, myth exit 0 / 0 |
| 6–10 (legacy) | `examples/culture-d2/packet.d2.yml` | identical five pins | naming exit 1 / **17** · phonology exit 1 / 3 · costume, lexicon, myth exit 0 / 0 |

The typed row's 7 naming findings and 3 phonology findings are the *gate-level* bodies of the change: the ten `PHON-INVENTORY` lines that named translated glosses are gone from the typed run and remain on the legacy rows, which is the same differential the flow asserts internally (17→7, removed 10 = off-records 10, `added 0`). The pipeline's own holds (`D2L-FORM-UNRESOLVED` ×10, `D2L-NATIVE` ×2, `D2L-RANK` ×3, note ×1) are carried by the flow's findings and its `--check` against `examples/culture-d2/typed-gate.expected.yml`, not by these rows — the replay rows assert reproduction of the gate verdicts, nothing about hold quality.

Division of labour, stated plainly: D05's `--freeze` is the generation builder for this round; this shard supplies the re-pin mechanics, the before/after pin record and the verification that the generation replays. A later re-freeze after further gate edits re-runs the same machine.

## 6. Mechanical constraints the wiring must respect (all measured)

1. **`replay-frozen.py` whitelists only `*.py` directly under `tools/gates/`** (`tools/replay-frozen.py`, `gate_path`). `tools/typed-gate-flow.py` is therefore **not replayable itself**; the round-11 manifest's rows can only be the gates it drives. This is why the wired generation has gate rows, not a flow row — and why the flow's own e2e (`--check`, findings == expected set) carries the pipeline contract.
2. **A "baseline" under a battery root whose `gate` is not one of the seven registered gates reads `no baseline`.** Measured twice: (a) with a stand-in at the design's §5.2 path `tools/gates/expected/typed-pipeline/r11/` — battery 9 found, 7 `pinned`, 1 `gate_revised`, 1 `no baseline` (`BASELINE-GATE-UNKNOWN`, `BASELINE-MALFORMED-INPUTS` ×2), **exit 2**; (b) live in the lane at 22:10:14Z from `tools/gates/expected/handoff-exercise/r11/expected.json` (O-shard, in flight): 9 found, 8 `pinned`, 1 `no baseline` (`BASELINE-GATE-UNKNOWN`, `BASELINE-EXTERNAL-INPUT` ×5, `BASELINE-EXPECTED-ABSENT`), **exit 2**. Consequence: any new frozen revision placed under `tools/gates/expected/**` must either carry one of the seven gate names (a thin gate under `tools/gates/` that drives the pipeline) or be rooted outside the battery's scanned roots. This must be decided before the D claim's "battery remain green" leg is scored; the live exit-2 is *not* attributable to the re-pin work.
3. **Append-only vs "every discovered baseline pinned".** Once a gate is edited, its superseded baseline reads `gate_revised` (exit 2) forever — editing it to match is exactly what the standard forbids (steps B and D above). The battery's own help says `--baselines-root` "is not a way to silence a committed baseline defect"; selecting a *current generation* root is a different act and should be named as such in the round's validation, with the superseded red reading kept in the record.
4. **The wiring need not touch gate bytes at all.** The adapter design (`reports/round-11/depth/design.md` §2.1, §5.3) keeps the five gates and the assembler byte-frozen; the measured live digests of all seven gates were still the round-9 revisions at 22:14:34Z. If that holds to integration, the r9-pre pins stay valid and the only new frozen surface is the round-11 generation — no re-pin of round-3 or r9-pre is needed, and this file's mechanics remain the fallback for any gate edit that does land.
5. **`replay-frozen.py` refuses a temp root inside `--repo-root`.** `run_in_mirror` reads `mirror_unsafe: temporary root is inside the repo` and maps the row to could-not-evaluate (exit 2) *before any gate runs*. With the round's prescribed `TMPDIR=$PWD/.scratch/...` and the lane as `--repo-root`, **every** row of every manifest reads `mirror_unsafe` — a green generation looks red. Measured: lane `round-11` generation replayed in place → 10/10 `mirror_unsafe`, exit 2; the identical bytes replayed with `--repo-root <mirror>` → 10/10 reproduced, exit 0. Recipe for any in-lane replay: copy the generation and the gates into a mirror and pass `--repo-root` the mirror (then an in-repo `TMPDIR` is fine), or point `TMPDIR` outside the repo root. This is an operational trap, not an artifact defect; worth naming in the round's validation so no leg scores a `mirror_unsafe` as drift.

## 7. What this shard did not do

- No file outside `.scratch/r11-d08/` and this report was written. The re-pinned `round-11-pre` generations and the seven `r11-pre` baselines are **candidates in mirrors**; committing them is a single-writer integration act. The design's §5.2 assigns D08 `tools/gates/expected/typed-pipeline/r11/**` and `tools/gates/frozen/round-11/MANIFEST.tsv`; the latter **landed in the lane at 22:14Z** (written by D05's `--freeze`, verified byte-identical to the generation measured here), while the typed-pipeline baseline path is still unclaimed — and §6.2 shows that placing a baseline there as specified costs the battery its green reading unless the gate-name contract is extended. The mechanics and the lift are ready: `.scratch/r11-d08/repin-frozen.py` (`0b06c9ba…`), exact commands in §9.
- `tools/gates/frozen/round-3/**` is untouched and stays red at exit 2; that divergence is reported, not repaired (design §5.3, standard §3).
- Verdict comparison for the wired rows' *hold semantics* (15 holds / 1 note / 0 fails) is the flow's and the test shards' contract, not this file's; the 16 findings measured here are quoted as the flow's own output.
- Out of province → report only: whether the ten garment glosses' owed forms are canon (lore), whether `packet.d2.typed.yml` should be committed as a build product or regenerated per run (integrator), and the O-shard's baseline placement under a battery root (§6.2).
- Concurrent tree state observed at 22:1xZ (for the round's scribes, not this seat's work): `git status --porcelain` shows modified `reports/round-{5,6,7,8,9}/validation.json`, `reports/round-10/coverage/index-update-22.md`, and untracked `tools/exercise-handoff-e2e.py`, `tools/typed-gate-flow.py`, `tools/gates/expected/handoff-exercise/`, `reports/round-11/**`.

## 8. Re-run recipe

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch/r11-d08/tmp           # never /tmp (inode-exhausted this round)

# 1. tool selftest (must print 31/31, exit 0)
python3 .scratch/r11-d08/repin-frozen.py --selftest

# 2. before-state readings (fail-closed today: 7/7 gate_digest_mismatch, exit 2)
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv
python3 tools/check-gate-battery.py --baselines-root tools/gates/expected \
  --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines

# 3. manifest re-pin into an isolated mirror (never the lane, never in place)
M=.scratch/r11-d08/mirror; rm -rf "$M"; mkdir -p "$M/tools/gates"
cp tools/replay-frozen.py "$M/tools/"; cp tools/gates/*.py "$M/tools/gates/"
cp -r tools/gates/frozen/round-3 "$M/tools/gates/frozen/round-3"
python3 .scratch/r11-d08/repin-frozen.py --manifest tools/gates/frozen/round-3/MANIFEST.tsv \
  --repo-root "$M" --generation tools/gates/frozen/round-11-pre --date 2026-10-17 --json
(cd "$M" && python3 tools/replay-frozen.py tools/gates/frozen/round-11-pre/MANIFEST.tsv)

# 4. baseline re-pin (repeat per gate; REFUSES any changed verdict)
python3 .scratch/r11-d08/repin-frozen.py --repo-root "$PWD" \
  --baseline tools/gates/expected/phonology-sanity-gate/r9-pre \
  --target-dir tools/gates/r11-baselines/phonology-sanity-gate/r11-pre \
  --target-id r11-pre --date 2026-10-17 --json

# 5. the wired generation (D05 builder) + its replay verification, in a mirror
python3 tools/typed-gate-flow.py --freeze tools/gates/frozen/round-11
python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv --repo-root "$PWD"
```

## 9. Sources

Every claim above is a command output, a repo file or a digest-pinned scratch receipt (all stamps 2026-10-17 UTC; `TMPDIR=$PWD/.scratch/r11-d08/tmp` for every run):

- lane: `tools/gates/frozen/round-3/{MANIFEST.tsv,attempt-1/MANIFEST.tsv,inputs/**}`, `tools/gates/{expected,frozen}/**/r9-pre/**`, `reports/round-9/baselines/**/expected.json`, `tools/replay-frozen.py` `a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464`, `tools/check-gate-battery.py` `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` (as read 22:21Z), `tools/typed-gate-flow.py` `7bff2edf…` (22:10:59Z) → `ae55e6fa…` (22:21Z), `examples/culture-d2/{packet.d2.yml,typed-labels.d2.yml}`, `corpus/knowledge/verification/gate-frozen-run-standard.md` §3/§4/§6, `reports/round-10/drift/ledger.json` (round-4 row `1dc089cc…`).
- receipts (all under `.scratch/r11-d08/`): `selftest-r11-d08.txt` `4ed93bdc…`; `repin-round3.json` (7/7 pin-only + `manifest_sha256 53229af6…`); `repin-attempt1.json` (`69695e6f…`); `repin-baselines.json` (7 baselines, before/after pins); `battery-A-pre.json` (exit 0, 8 pinned); `battery-B-gate-edited.json` (exit 2, `gate_revised`); `battery-C-repinned-root.json` (exit 0, 7 pinned); `battery-D-old-roots-after-repin.json` (exit 2, superseded); `battery-E-second-edit.json` (exit 2); `battery-F-typed-baseline-standin.json` (exit 2, `BASELINE-GATE-UNKNOWN`); `battery-live-preedit.json` / `battery-live-now.json` (live lane, 22:0xZ, 8 pinned + 1 `no baseline`, exit 2); `flow-e2e2.json` (wired flow, exit 0, 16 findings); `flow-freeze.out` (`froze 10 row(s)`); `replay-round11-wired.json` (`10/10`, exit 0); `replay-round11-lane.json` (lane generation in place: 10/10 `mirror_unsafe`, exit 2); `replay-round11-lane-bytes.json` (lane bytes in a mirror root: `10/10`, exit 0); `round4-replay.out` (`1dc089cc…`, matching the round-10 ledger row); `mirror/`, `mirror2/`, `mirror3/`, `mirror4/`, `mirror5/` trees; `.scratch/battery-r11-prewire.txt` (a sibling seat's pre-wire battery JSON, cited for agreement, not reused as evidence).
- sibling round-11 files read for alignment (not edited): `reports/round-11/depth/design.md` §1.4, §4, §5.2–§5.4, §7 (shard map); `tools/typed-gate-flow.py` module docstring + `--freeze`.
