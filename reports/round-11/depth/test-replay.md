# R11-D12 — replay-frozen over the typed pipeline artifacts

- round: 11 (loop 1 of 3, build round 4 of 4) · shard: **D12 (depth / test replay)** · date: **2026-10-17**
- stamps UTC unless marked; local is UTC−03:00. Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; revision `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (`e3ef171`, the round-11 claims commit) **plus the untracked round-11 worker output present at each stamp** — the typed-pipeline artifacts landed at 22:14–22:17Z while this shard ran, so every digest below names its observation stamp and is a re-read event if a hash moved.
- owns: **this file only**. No tool, gate, packet, component, manifest, generation directory, baseline or earlier-round byte is edited by this shard; `reports/round-{8,9,10}/**` and every `tools/gates/{frozen,expected}/**` file are read-only here. No commit, no push. In-lane scratch under `.scratch/d12/`; replay mirrors need `TMPDIR` **outside** the repo root (§3.2) and used `/home/vgpnk/r11d12-scratch/`.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability or a canon fact.
- tested objects: `tools/replay-frozen.py` (`a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464`, unchanged since round 8), the **committed round-11 generation** `tools/gates/frozen/round-11/MANIFEST.tsv` (`4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376`), its typed-packet snapshot `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` and legacy-packet snapshot `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`, plus the round-3 generations and the pre-wiring artifacts.
- requirement tested (assignment R11-D12; claim D `after_required`, `reports/round-11/claims.json:15`): "frozen replay re-pinned and green", scoped to the typed pipeline artifacts.

## 0. Verdict — read this first

| leg | command | observed | status |
|---|---|---|---|
| A tool selftest | `python3 tools/replay-frozen.py --selftest` | `selftest: 79/79 checks passed`, exit 0 (22:01Z) | **PASS** |
| B **round-11 committed generation, live lane** | `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` (TMPDIR outside the repo) | **`REPLAY OK: 10/10 rows reproduced`**, exit 0, every row `bytes=match` (22:17:33Z) | **PASS — the wired re-pin leg** |
| B′ same generation, isolated tree copy | `--repo-root <isocopy>` | **10/10 reproduced**, exit 0 (22:18:01Z) | **PASS** |
| B″ controls C1–C3 over the generation | one mutation per isolated copy | C1 typed snapshot → 5 reproduced + 5 `snapshot_tampered`; C2 gate bytes → 8 + 2 `gate_digest_mismatch`; C3 recorded output → 9 + 1 `expected_output_tampered`; **all exit 2, no gate launched in any could-not-evaluate row** | **PASS (fail-closed)** |
| C typed-vs-legacy differential, from the frozen outputs | `diff` of the two recorded naming outputs | legacy 17 findings (10 × `PHON-INVENTORY` on `GAR-*`) → typed 7 (0 `PHON-INVENTORY`, 0 `GAR-`); the ten removed lines are exactly the `GAR-01..10` glosses | **PASS (the artifact class left the sound channel)** |
| D old generations stay legible | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` and `attempt-1/MANIFEST.tsv` | exit 2, 7/7 + 7/7 `gate_digest_mismatch` (round-8 gate revisions); `round-4/` → exit 2 `manifest_unreadable` | **fail-closed, expected** |
| E pinned-gate legacy control | round-3 manifests over gates restored from commit `291c7141` | **7/7 reproduced**, exit 0 (22:02Z) | **PASS** |
| F supplementary fresh generation over the legacy packet (my own, scratch) | `.scratch/d12/typedroot/tools/gates/frozen/round-11-typed-proposal/MANIFEST.tsv` | **5/5 reproduced**, exit 0 + four tamper controls fail-closed (22:02Z) | **PASS (independent cross-check)** |
| G pre-wiring projection-independence control | five gates re-run with `typed-labels.d2.yml` deleted | all five stdout digests identical | recorded: at the pre-wiring revision the gates did **not** consume the typed projection |

Read together: **claim D's replay clause is met** — the round-11 generation, recorded from the wired flow, replays 10/10 with recorded verdicts and fails closed under every tamper class tried; the ten translated glosses left the naming gate's sound channel between the legacy and typed rows; the old generations were not re-blessed. Reproduction is not endorsement: the typed rows record `naming-collision-gate` **exit 1** and the wired flow's own output still carries 15 holds (a reproduced red stays red, and the aggregate verdict stays red by design).

## 1. Method and sweep

`tools/replay-frozen.py` verifies `gate_sha256`, the snapshot's `input_sha256` and the recorded output's `output_sha256` **before** launching anything, then runs `[python3, <pinned gate>, <input>]` with `cwd` set to a temp mirror holding a verified copy of the snapshot, comparing observed exit code, `^FINDING ` count and raw output bytes against the record (`tools/replay-frozen.py:1-50, 171-290`). Exit 0 = reproduced, 1 = verdict mismatch, 2 = could-not-evaluate (`:19-30`). Only `*.py` files directly under `tools/gates` can be rows (`:130-140`).

Sweeps behind this file (lane root, 22:03:55Z and 22:17-22:18Z):

```sh
grep -rl "typed-labels" tools/gates/frozen/     # 22:03Z: none — no committed generation then
grep -rln "replay-frozen" tools/                # tools/replay-frozen.py only — no other consumer
ls tools/gates/frozen/                          # round-3 round-4 round-11 handoff-packet-check lexicon-coverage-audit provenance-audit
find tools/gates/frozen/round-11 -type f        # MANIFEST.tsv + README.md + 5 typed outs + 5 legacy outs + typed-gate-flow.out + 2 snapshots
```

Pin-matching revision discovery (leg E, script in `.scratch/d12/`): every `gate_sha256` in the round-3 manifest equals the gate blob at commit **`291c714144`** (all six gates matched; no unmatched candidate). The live gate bytes were last changed by round-8 `e1694ba` (all six gates), which is why the round-3 pins fail closed in the live tree.

## 2. Leg B — the committed round-11 generation (the re-pin)

`tools/gates/frozen/round-11/MANIFEST.tsv` (manifest `4ddb911c…`, 10 data rows) pins the five culture gates twice: **5 typed rows** over `examples/culture-d2/packet.d2.typed.yml` (snapshot `e8a83445…`) and **5 legacy rows** over `examples/culture-d2/packet.d2.yml` (snapshot `e0f21509…`). Every gate pin equals the live gate digest recorded at freeze time, i.e. the generation names *its* revisions rather than the filed round-3 ones.

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/home/vgpnk/r11d12-scratch/tmp      # must be OUTSIDE the repo root, see §3.2
python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv --json
# {'rows': 10, 'reproduced': 10, 'mismatch': 0, 'could_not_evaluate': 0, 'exit': 0}    (22:17:33Z)
```

| rows | gate | typed packet (recorded) | legacy packet (recorded) |
|---|---|---|---|
| 2, 7 | `naming-collision-gate.py` `d9e4e8f4f93a…` | exit 1, **7** findings | exit 1, **17** findings |
| 3, 8 | `phonology-sanity-gate.py` `d5fe087ffb23…` | exit 1, 3 | exit 1, 3 |
| 4, 9 | `costume-era-consistency-gate.py` `e6bffd7020c0…` | exit 0, 0 | exit 0, 0 |
| 5, 10 | `lexicon-coverage-audit.py` `2c4dd39702a1…` | exit 0, 0 | exit 0, 0 |
| 6, 11 | `myth-consistency-gate.py` `5368b13542cd…` | exit 0, 0 | exit 0, 0 |

The same command over an isolated full copy of `tools/` + `examples/` (`.scratch`-free mirror root, `--repo-root`) reproduces **10/10, exit 0** (22:18:01Z) — the generation is self-contained, not an artefact of the live working directory. Regenerating the typed packet does not break it: the replay reads the frozen snapshot, never the live build product (the live packet and the snapshot are byte-equal today, `e8a83445…`).

**Independent agreement.** `reports/round-11/depth/repin.md:15,30` (D08, the re-pin owner) records the same manifest digest `4ddb911c…`, the same 10-row shape and `10/10 reproduced, exit 0` from the lane bytes — measured separately from this seat's run.

## 3. Controls over the round-11 generation (isolated copies)

Each control is a full isolated copy of `tools/` + `examples/` with exactly one mutation, all under `TMPDIR=/home/vgpnk/r11d12-scratch/tmp` (22:18Z):

| case | mutation | observed |
|---|---|---|
| C1 | `# tampered` appended to the pinned **typed-packet** snapshot | `{'reproduced': 5, 'could_not_evaluate': 5, 'exit': 2}`, all 5 typed rows `snapshot_tampered`, **no gate launched**; the 5 legacy rows (other snapshot) reproduce |
| C2 | `# drift` appended to `tools/gates/naming-collision-gate.py` | `{'reproduced': 8, 'could_not_evaluate': 2, 'exit': 2}`, both naming rows `gate_digest_mismatch` |
| C3 | `FINDING X-9 injected` appended to the recorded typed `naming-collision-gate.out` | `{'reproduced': 9, 'could_not_evaluate': 1, 'exit': 2}`, `expected_output_tampered` |

The tamper classes the tool's own selftest proves on fixtures (79/79, leg A) reproduce here against the committed generation: a tampered snapshot, an edited gate and an edited record all leave the replay incomplete at exit 2 rather than quietly green, and the could-not-evaluate rows are exactly the rows whose pinned bytes moved.

### 3.2 One environment fact worth recording

Run with `TMPDIR=$PWD/.scratch` (the lane's standing scratch rule) **from the lane root**, all ten rows report `could-not-evaluate mirror_unsafe` — `run_in_mirror` refuses a temp mirror created inside the repo root (`tools/replay-frozen.py:174-178`). That is the tool's containment guard working as documented; the replay must run with `TMPDIR` outside the repo root (or with `--repo-root` pointing at an isolated copy). `reports/round-11/depth/repin.md:15` records the same reading independently. No row was harmed; the same manifests replay 10/10 once the mirror lands outside.

## 4. The typed-vs-legacy differential, from the frozen bytes

The generation stores both runs' outputs, so the channel claim is checkable from frozen bytes alone:

```sh
grep -c '^FINDING ' tools/gates/frozen/round-11/{legacy/,}naming-collision-gate.out     # 17 / 7
grep -c 'PHON-INVENTORY' tools/gates/frozen/round-11/{legacy/,}naming-collision-gate.out # 10 / 0
diff tools/gates/frozen/round-11/legacy/naming-collision-gate.out tools/gates/frozen/round-11/naming-collision-gate.out
```

`diff` yields exactly ten removed lines, one per `GAR-01..GAR-10`, each a `PHON-INVENTORY: FAIL` on an English gloss; everything else (6 × `NAME-NEAR`, 1 × `CROSS-HOLD` in both) is unchanged. The ten glosses are off the sound/identity channel in the typed packet, and the identity findings that legitimately remain stay. `grep -c 'GAR-'` in the typed output is 0.

The wired flow's own recorded stdout (`tools/gates/frozen/round-11/typed-gate-flow.out`, `ec57b040…`, 16 `FINDING ` lines) carries the named holds the claim requires: `D2L-FORM-UNRESOLVED` ×10 at `LEX-GAR-01..10`, `D2L-NATIVE` ×2 (`L-15`, `L-16`), `D2L-RANK` ×3 holds + ×1 note — i.e. 15 holds and 1 note, the design's expected set (`reports/round-11/depth/design.md` §4.2-4.3), and zero fails. The hold-set **equality** test is R11-D09's business; this file only records that the frozen flow bytes carry it.

## 5. Legs C–G — old generations, pinned-gate control, supplementary generation

| leg | command | result |
|---|---|---|
| round-3 manifest, live tree | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | exit 2, **7/7 `gate_digest_mismatch`** (22:01Z); manifest unchanged `d5337590…` |
| round-3 `attempt-1`, live tree | same, `attempt-1/MANIFEST.tsv` | exit 2, 7/7 `gate_digest_mismatch` (22:04Z); manifest `613e5945…` |
| `round-4` dir | `... round-4/MANIFEST.tsv` | exit 2 `manifest_unreadable` — that directory holds only `.out` files |
| pinned-gate control | round-3 manifests over gates restored from `291c7141` (isolated tree) | **7/7 reproduced, exit 0**, every row `bytes=match` |
| verdict-preservation probe | round-3 manifest with **only** the `gate_sha256` column rewritten to the live revisions | 7/7 reproduced, exit 0 — the repaired gates still emit the round-3 recorded bytes over the frozen round-3 snapshot |
| supplementary fresh generation (leg F) | `.scratch/d12/build-typed-manifest.py` + `tools/replay-frozen.py` over a scratch root containing `tools/replay-frozen.py`, the six gates and `examples/culture-d2/{packet.d2.yml,typed-labels.d2.yml}` | 5/5 reproduced, exit 0; C1 snapshot → 5/5 `snapshot_tampered`; C2 gate → `gate_digest_mismatch`; C3 output → `expected_output_tampered`; C4 live-input drift → 5/5 exit 0 with rows byte-identical; C5 the same manifest over round-3 pinned gate bytes → 5/5 `gate_digest_mismatch` (pins bite both ways) |
| pre-wiring projection independence (leg G) | five gates re-run with `typed-labels.d2.yml` deleted from the scratch root | every stdout digest identical (naming `ebc8850d…`, phonology `1ce5f0cd…`, others empty `e3b0c442…`) — at the pre-wiring revision the gates never read the typed projection |

Leg F is reported as a cross-check, not as the claim's leg: it pins the pre-wiring artifacts (the legacy packet alone, before the typed build product existed) and carries no committed weight. Its value is that it exercised the same replay instrument and all four tamper classes against the artifacts that existed at 22:02Z, independently of the generation that landed at 22:14Z.

## 6. What this shard did not test — limits and open items

1. **The wired entry point is not itself a replay row.** `tools/typed-gate-flow.py` (`a7e1224f…`) lives at `tools/`, not under `tools/gates/`, so `replay-frozen.py`'s whitelist (`:130-140`) cannot pin it; its stdout is recorded in the generation (`typed-gate-flow.out`, `ec57b040…`) but **no manifest row replays it**. The replay leg therefore covers the five gates × two packets (10 rows), which is what the committed manifest claims — a limit to state, not a defect to hide. A row for the flow's own verdict would need the flow to live at `tools/gates/<name>.py` or a second replay mechanism.
2. **Layout deviation from the design (reported, not absorbed).** Design §5.2 planned a replay row `tools/gates/typed-pipeline-gate.py` with `finding_count 15` and a freeze under `tools/gates/expected/typed-pipeline/r11/**`; the landed shape is `tools/typed-gate-flow.py` + `tools/gates/frozen/round-11/**` (10 rows) + `examples/culture-d2/typed-gate.expected.json` (`7ed59731…`). The generation's record is `tools/gates/frozen/round-11/README.md` (33 lines, written by `--freeze`) rather than the `r9-pre` `freeze.txt`/`run.log`/`expected.json` trio, and the recorded flow output has 16 `^FINDING ` lines (15 holds + 1 note), not 15 — the README itself states that `typed-gate-flow.out` is a record, not a replayed row, the same boundary this shard reports in item 1. This is a reviewer's (R11-D20/D23) call, not this shard's; recorded here because a replay row pinned to the design's name would have failed.
3. **All numbers are stamp-specific.** The artifacts landed at 22:14–22:17Z while this shard ran; the projection was re-pinned in the same window (`examples/culture-d2/typed-labels.d2.yml` = `a3aa452c…`, `python3 tools/d2-typed-labels.py --check` → byte-identical, exit 0 at 22:18Z). A later re-run must compare pins, never these remembered digests.
4. **Not claimed here:** hold-set equality (D09/D10), the wired CLI surface (D14), the negative examples D17–D19, circularity (D22), determinism of the wired entry (D11), the battery (other shards). This file asserts reproduction and the frozen differential only, and it blesses no pin — the round-11 generation was blessed by its own author (D08) and replayed by this shard; a differently-authored generation would need its own replay receipt.
5. **`/tmp` was never used**; the mirror-failure behaviour noted in `reports/round-8/depth/test-replay.md` §8 (an uncreatable mirror exits 1 with a traceback) did not occur; the in-repo `TMPDIR` case is handled explicitly as `mirror_unsafe` (§3.2).

## 7. Re-run recipe

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/home/vgpnk/r11d12-scratch/tmp     # outside the repo root; in-repo TMPDIR reads mirror_unsafe
python3 tools/replay-frozen.py --selftest                                     # 79/79, exit 0
python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv       # expect: REPLAY OK: 10/10, exit 0
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv        # expect: exit 2, 7/7 gate_digest_mismatch (old generation stays legible)
bash .scratch/d12/typed-replay.sh <tag>                                       # fresh-generation leg + C1–C4 controls over the live artifacts
```

Acceptance reading: `REPLAY OK: 10/10 rows reproduced the recorded verdicts`, exit 0, every row `bytes=match`; rounds 3/`attempt-1` unchanged byte-for-byte (`d5337590…`/`613e5945…`) and still fail-closed; the ten `PHON-INVENTORY` gloss findings present in the legacy rows and absent from the typed rows; and the generation's gate pins naming the revisions frozen at 22:14Z rather than any older or later bytes.

## Receipts

```sh
# 2026-10-17 22:01–22:18Z, lane root, Python 3.14.7, TMPDIR=/home/vgpnk/r11d12-scratch/tmp for replay runs
python3 tools/replay-frozen.py --selftest                                          # 79/79, exit 0
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv             # exit 2, 7/7 c-n-e gate_digest_mismatch
python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv   # exit 2, 7/7 c-n-e
python3 tools/replay-frozen.py tools/gates/frozen/round-4/MANIFEST.tsv             # exit 2, manifest_unreadable
python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv --json     # exit 0, 10/10 reproduced  (round11-live.json)
# isolated tree copy of tools/ + examples/:
python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv --json     # exit 0, 10/10 reproduced  (round11-base.json)
# controls, isolated copies with one mutation each:
#   round11-c1.json  snapshot_tampered ×5, exit 2      round11-c2.json  gate_digest_mismatch ×2, exit 2
#   round11-c3.json  expected_output_tampered ×1, exit 2
sha256sum tools/gates/frozen/round-11/MANIFEST.tsv                                 # 4ddb911c…  (recording stamp 22:14Z, re-read 22:18Z)
python3 tools/d2-typed-labels.py --check                                           # exit 0, byte-identical (re-pinned projection a3aa452c…)
```

Scratch retained (`.scratch/d12/`): `typed-replay.sh`, `build-typed-manifest.py`, `poll.sh` + `poll.log`, `typedroot*/`, `legacy-pinned/`, `repin-probe/`, `proj-indep/`, and the JSON receipts named above; `/home/vgpnk/r11d12-scratch/` holds the round-11 replay JSONs and the isolated tree copies whose replay mirrors must sit outside the repo.
