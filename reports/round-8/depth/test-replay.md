# R8-D08 — replay-frozen compatibility test over the regenerated D2 artifacts

- round: 8 (loop 1 of 3, build round 1 of 4) · shard: D08 (tests) · date: 2026-10-17 (all stamps UTC)
- baseline revision: `e7ca0faeb6680fa9891b907be628d9db578c28f4` (declared, `reports/round-8/claims.json:5`); measurement HEAD `cf338a713060f274269cdacb18cdc0085bb06aeb`
- owns: **this file only**. No tool, manifest, packet, component, gate or LOG edit is made by this shard. Every scratch tree below lives outside the repo (`/home/vgpnk/r8d08-scratch/`).
- tested object: `python3 tools/replay-frozen.py` over the regenerated D2 artifacts (`tools/d2-typed-labels.py` + `examples/culture-d2/typed-labels.d2.yml`) and over the D2 packet rows of the frozen round-3 manifests.
- requirement tested: "no digest drift allowed" (assignment R8-D08; claim D `after_required`, `reports/round-8/claims.json`).

## 0. Verdict (read this first)

| leg | command | result | status |
|---|---|---|---|
| tool selftest | `python3 tools/replay-frozen.py --selftest` | `selftest: 79/79 checks passed`, exit 0 | **PASS** |
| baseline replay (pinned gates, pre-repair) | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | `REPLAY OK: 7/7 rows reproduced`, exit 0 | **PASS** (20:13Z; corroborated by `reports/round-8/depth/docs.md` §2.4 Obs. A) |
| drift-detector battery C0–C5 (isolated) | see §4 | every drift class detected; live-artifact change does not affect the replay | **PASS** |
| **replay over the regenerated D2 artifacts** (pinned gate revisions, isolated tree containing `typed-labels.d2.yml`) | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <iso>` and the `attempt-1` manifest | both manifests `7/7 reproduced`, exit 0 | **PASS — no drift attributable to the D2 artifacts** |
| live lane tree at measurement stamps | same command in the lane | exit 2, **7/7 rows could-not-evaluate `gate_digest_mismatch`** (20:19:57Z) | **FAIL-CLOSED — cause is the O-shard's in-flight gate repairs, not the D2 work**; remediation demonstrated in §6 |
| cross-check, not this shard's fix | `python3 tools/d2-typed-labels.py --selftest` | `26/30 checks passed`, exit 1, the same 4 failures at three complete tool revisions → `32/32`, exit 0 at `623b5b1f…` (20:23Z) | **DEFECT FOUND, then FIXED upstream during the shard** (§7) |

The D2 artifacts themselves are replay-compatible: a tree carrying the regenerated artifact replays 7/7 on both frozen manifests when the round-3 pinned gate bytes are in place. The live tree cannot replay at this revision because six gate files have been edited by concurrent O-shard repairs; the pins are doing exactly what `corpus/knowledge/verification/gate-frozen-run-standard.md` requires — refusing to re-bless an edited gate. §6 shows the repairs are verdict-preserving on the frozen snapshot and that a re-pin restores 7/7 exit 0.

## 1. Method

The round-3 frozen manifests pin, per row: gate path + `gate_sha256`, input path + `input_sha256`, exit code, finding count, output path + `output_sha256`, and an immutable input snapshot. `tools/replay-frozen.py` verifies every pin before launching, then runs `[python3, <pinned gate>, <input>]` in a temp mirror holding a verified copy of the snapshot, and compares observed exit code, `^FINDING ` count and output bytes against the record (`tools/replay-frozen.py:1-50, 171-200`). Exit 0 = reproduced, 1 = mismatch, 2 = could-not-evaluate (`tools/replay-frozen.py:19-30`).

Manifest facts used throughout (command: `python3 -c "import csv;print(len(list(csv.DictReader(open('tools/gates/frozen/round-3/MANIFEST.tsv'),delimiter='\t'))))"`, 2026-10-17): **7 data rows** — 5 packet rows (`examples/culture-d2/packet.d2.yml`, gates phonology-sanity / lexicon-coverage-audit / myth-consistency / costume-era-consistency / naming-collision) and 2 provenance rows. `replay-frozen.py` numbers rows from 2 (line 1 is the header); "7/7" means the seven data rows. A second, independent manifest exists at `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` and was replayed for every leg.

Digest pins (from the manifest, re-verified 2026-10-17):

| artifact | sha256 |
|---|---|
| `tools/gates/frozen/round-3/MANIFEST.tsv` | `d5337590b343c65b42fd6e55457862fa325c138ad652e59c81b887daf9971399` |
| frozen packet snapshot (`inputs/examples/culture-d2/packet.d2.yml`) | `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4` |
| `tools/gates/phonology-sanity-gate.py` (pin) | `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655` |
| `tools/gates/lexicon-coverage-audit.py` (pin) | `63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80` |
| `tools/gates/myth-consistency-gate.py` (pin) | `26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5` |
| `tools/gates/costume-era-consistency-gate.py` (pin) | `29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03` |
| `tools/gates/naming-collision-gate.py` (pin) | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` |
| `tools/gates/provenance-audit.py` (pin) | `4aaea6e98b9776922708692e6e0f38f76ef7323e3c748cbdf82c789eb77e1e7a` |
| `tools/replay-frozen.py` (test tool, this run) | `a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464` |

Command for the table: `sha256sum tools/gates/frozen/round-3/MANIFEST.tsv tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml tools/gates/*.py tools/replay-frozen.py` (2026-10-17T20:14:06Z; full output `/home/vgpnk/r8d08-scratch/baseline-digests.txt`).

## 2. Baseline receipts (before the concurrent gate repairs)

1. **Tool selftest** — `python3 tools/replay-frozen.py --selftest` → `selftest: 79/79 checks passed`, **exit 0** (2026-10-17T20:14Z; sha256 of captured output `4d6aaea127ad99737b53ce50a7378efad5562b6fa01da88e9ca8610aa604ea16`). The 15 selftest scenarios include `clean-green`, `expected-red`, `mismatch-bytes` and `mismatch-exit` (exit 1), `snapshot-tampered`, `gate-digest-mismatch`, `output-tampered`, `record-inconsistent` (exit 2) and the path-safety refusals (`tools/replay-frozen.py:509-560`); this covers the exit-1 mismatch path without needing a live fixture.
2. **In-lane replay, pre-repair** — `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` → `REPLAY OK: 7/7 rows reproduced the recorded verdicts`, every row `bytes=match`, **exit 0**; the `attempt-1` manifest likewise 7/7, exit 0 (observed ~20:13Z, before the first gate edit was visible in the worktree; independently recorded as Observation A in `reports/round-8/depth/docs.md` §2.4 at ~20:10Z).
3. **Durable clean-baseline control (C0)** — because the lane tree no longer holds the pinned gate revisions, the reproducible baseline lives in an isolated tree: `/home/vgpnk/r8d08-scratch/iso-clean/` = `tools/replay-frozen.py` + all six gates restored to `git show HEAD:tools/gates/<gate>.py` (HEAD = the pinned revisions) + a copy of `tools/gates/frozen/`. `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <iso> --json` → `{'rows': 7, 'reproduced': 7, 'mismatch': 0, 'could_not_evaluate': 0, 'exit': 0}` (2026-10-17T20:15Z; `/home/vgpnk/r8d08-scratch/c0.json`). This isolates "the tool + pins + records are self-consistent" from "the live worktree has drifted".

## 3. Drift ledger — the live tree moved under the test

Six gate files were edited by concurrent round-8 O-shard repairs while this shard ran (the same repair stream documented in `reports/round-8/operability/o01-diagnosis.md` and `reports/round-8/depth/docs.md` §2.4). Time series (`/home/vgpnk/r8d08-scratch/timeseries.log` and the probe stamps below; gates in the order phonology, lexicon, myth, costume, naming, provenance, first 12 hex chars):

| stamp | gate digests (live) | lane replay |
|---|---|---|
| 20:14:06Z | phonology `660278f22d9f` drifted; other five = pins | 6 reproduced / 1 could-not-evaluate (`gate_digest_mismatch`) |
| 20:17:12Z | `970e69002a6b b227d7ad8582 750604ab24e0 20735a9cb9e6 7aaaf7180e89 4aaea6e98b97` (5 drifted, provenance = pin) | — |
| 20:17:27Z | `17773f3f274a bf43122d3198 5c9fc2ee4dfe 20735a9cb9e6 ab98fe1ad71b 4aaea6e98b97` | — |
| 20:18:02Z | provenance also edited (`972859cebb4b`) | **7/7 could-not-evaluate**, exit 2 |
| 20:18:27Z | `722ff91bd0d4 989b129535f2 9ae43989a050 590e7f65df46 ab98fe1ad71b 972859cebb4b` | 7/7 could-not-evaluate, exit 2 |
| 20:19:22Z | `722ff91bd0d4 989b129535f2 270e4e0fc503 590e7f65df46 ab98fe1ad71b 8a96aaf4ccd1` | 7/7 could-not-evaluate, exit 2 |
| 20:19:57Z | as above | `{'rows': 7, 'reproduced': 0, 'mismatch': 0, 'could_not_evaluate': 7, 'exit': 2}`, sole reason `gate_digest_mismatch` |
| 20:23:04Z (final lane stamp) | all six drifted again (`3eee41a6cf27 989b129535f2 48477d38dfa1 6be04578fc21 4906c34ca843 8a96aaf4ccd1`) | 7/7 could-not-evaluate, exit 2 |

The frozen snapshot, the expected outputs and the manifests themselves were **not** touched: every could-not-evaluate row reports `gate: on-disk bytes are not the pinned revision` and none reports `snapshot_tampered` or `expected_output_tampered`. The frozen input copy still equals its pin (`54be6319…`, re-verified 20:19Z). The drift is entirely in the gate revisions.

## 4. Isolated drift-detector battery (negative controls C1–C5)

Each case is a fresh copy of the C0 clean tree with exactly one mutation; the mutation script is `/home/vgpnk/r8d08-scratch/apply.py`, the JSON receipts `/home/vgpnk/r8d08-scratch/iso-c*.json`. All five ran with `TMPDIR=/home/vgpnk/r8d08-scratch/tmp` (isolated from the contended shared `/tmp`, see §8).

| case | mutation | expected | observed |
|---|---|---|---|
| C1 | append a byte to `tools/gates/myth-consistency-gate.py` | exit 2, `gate_digest_mismatch`, gate not launched | `{'reproduced': 6, 'could_not_evaluate': 1, 'exit': 2}`; reason `gate_digest_mismatch`; `launched=no` |
| C2 | append a byte to the frozen packet snapshot | exit 2, `snapshot_tampered`, no gate runs | `{'reproduced': 2, 'could_not_evaluate': 5, 'exit': 2}`; all 5 packet rows `snapshot_tampered`, `launched=no` |
| C3 | append a `FINDING X` line to the recorded `naming-collision-gate.out` | exit 2, `expected_output_tampered` | `{'reproduced': 6, 'could_not_evaluate': 1, 'exit': 2}`; reason `expected_output_tampered` |
| C4 | replace the live `examples/culture-d2/packet.d2.yml` and add a new `tools/d2-typed-labels.py` | replay unaffected (the frozen snapshot governs) | `{'reproduced': 7, 'could_not_evaluate': 0, 'exit': 0}` |
| C5 | replace the phonology gate with the then-live drifted revision | exit 2, `gate_digest_mismatch` | `{'reproduced': 6, 'could_not_evaluate': 1, 'exit': 2}`; reason `gate_digest_mismatch` |

C4 is the control that matters for this shard: regenerating or replacing live D2 artifacts — including adding the new tool — cannot by itself break the frozen replay, because the replay runs against the pinned snapshot, never the live file. C5 reproduces the live drift in isolation and shows the failure is reported, not blessed.

## 5. The D08 test proper — replay over the regenerated D2 artifacts

The regenerated artifacts (stamps 2026-10-17T20:19–20:22Z):

- `tools/d2-typed-labels.py` — the file was rewritten repeatedly while this shard ran: observed revisions `d9e084a8…` (60,088 bytes, 20:19Z), `13e82857…` (20:21Z), `37060dd1…` (63,780 bytes, 20:22Z), `623b5b1f…` (20:23Z, the selftest repair, §7); one capture in between (`da86132e…`) caught a mid-write state (`selftest: 0/2`) and is not counted as a revision. §7's failure was stable across the three complete pre-repair revisions and is green at `623b5b1f…`.
- `examples/culture-d2/typed-labels.d2.yml` — the regenerated artifact, byte-identical between the lane and independent isolated builds at each tested revision: 68,223 bytes sha256 `08de5a88ff93b42c59909ee04d028eda9526800b6955ca58db89dd33225479dd` (20:19Z, revision `d9e084a8…`) and 68,643 bytes sha256 `820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778` (20:22-20:23Z, revisions `37060dd1…`/`623b5b1f…`). `python3 tools/d2-typed-labels.py --check` in an isolated tree → `examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic build`, exit 0 at each tested revision.

Test tree: `/home/vgpnk/r8d08-scratch/d2leg/` = the lane's `tools/d2-typed-labels.py` + `examples/culture-d2/{components,packet.d2.yml}` + the **regenerated `typed-labels.d2.yml`** + `tools/replay-frozen.py` + a copy of `tools/gates/frozen/`, with all six gates restored to `git show HEAD:…` (the pinned round-3 revisions). Commands and results (2026-10-17T20:19-20:20Z):

```sh
cd /home/vgpnk/r8d08-scratch/d2leg
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root "$PWD" --json
# {'rows': 7, 'reproduced': 7, 'mismatch': 0, 'could_not_evaluate': 0, 'exit': 0}
python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv --repo-root "$PWD" --json
# {'rows': 7, 'reproduced': 7, 'mismatch': 0, 'could_not_evaluate': 0, 'exit': 0}
```

Same tree, same artifact, gates replaced by the live repaired revisions → `{'reproduced': 0, 'could_not_evaluate': 7, 'exit': 2}`. The variable that moves the verdict is the gate revision, not the D2 artifact.

**Live-artifact independence, with the real regeneration procedure** (not the C4 simulation): the isolated end-to-end tree `/home/vgpnk/r8d08-scratch/e2e/` ran the real assembler, `python3 tools/assemble-d2.py` → `Wrote examples/culture-d2/packet.d2.yml (156071 bytes)`, exit 0. The regenerated packet's digest differed from the lane packet (`111eda0d24f0…` vs `8da90b0788f8…`) in **exactly one field**: `reader_sha256` at `packet.d2.yml:3322` — the assembler hashes the costume gate's reader it reuses, so the O-shard's repair of that gate changes the deterministic assembly. (`diff` over the two packets: 2 changed lines, both sides of that one field.)

Related consequence in the lane, stated because it is the D2 claim's "regenerates deterministically" clause touching this shard: `python3 tools/assemble-d2.py --check` in the lane now prints `packet.d2.yml differs from deterministic assembly` and exits 1 (20:19:57Z), because the committed packet records the pre-repair `reader_sha256: "29a9361c…"` while the repaired costume gate is no longer that digest. The D2 worker must regenerate the packet (or the orchestrator must decide the reader pin policy); this shard only reports it. `--check` was still byte-identical at 20:16Z, so the staleness arrived with the gate repair, not with the D2 work.

## 6. Remediation evidence — the drift is real but verdict-preserving

**Probe** (`/home/vgpnk/r8d08-scratch/refreeze-probe.py`, 2026-10-17T20:17:27Z): every manifest row was re-executed with its **live (repaired) gate** over its **frozen snapshot**, and compared to the recorded exit code, finding count and output bytes:

| gate | live digest | exit rec/obs | findings rec/obs | bytes | pin |
|---|---|---|---|---|---|
| phonology-sanity | `17773f3f274a` | 1/1 | 3/3 | IDENTICAL | DRIFTED |
| lexicon-coverage-audit | `bf43122d3198` | 0/0 | 0/0 | IDENTICAL | DRIFTED |
| myth-consistency | `5c9fc2ee4dfe` | 1/1 | 1/1 | IDENTICAL | DRIFTED |
| costume-era-consistency | `20735a9cb9e6` | 1/1 | 10/10 | IDENTICAL | DRIFTED |
| naming-collision | `ab98fe1ad71b` | 1/1 | 20/20 | IDENTICAL | DRIFTED |
| provenance-audit (×2 rows) | `4aaea6e98b97` | 0/0 | 0/0 | IDENTICAL | matched at this stamp |

All seven rows reproduce their recorded verdicts **byte-identically** with the repaired gates. The repairs change the gate bytes, not the frozen verdicts.

**Re-pin demonstration** (`/home/vgpnk/r8d08-scratch/refreeze/`, 20:17Z): a candidate manifest was produced by copying the round-3 manifest and rewriting only the `gate_sha256` column to the digest of each frozen gate copy (everything else — snapshot pins, exit codes, counts, output pins, commands — unchanged). `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root "$PWD"` → `REPLAY OK: 7/7 rows reproduced the recorded verdicts`, **exit 0**, every row `bytes=match`.

That is the remediation path for the parent (the round's scribes own the frozen-manifest records, shard R8-D18): re-freeze a manifest whose gate pins name the repaired revisions, under a new generation directory (`tools/gates/frozen/round-8/`), leaving the round-3 manifest as the historical record of the pre-repair run. `reports/round-8/depth/scribe.md` §2-3 reaches the same shape from the record-format side and additionally establishes that `tools/d2-typed-labels.py` cannot itself be a `replay-frozen.py` row (the tool whitelists only `*.py` directly under `tools/gates`, `tools/replay-frozen.py:130-140`), so the D2 capability's replay leg is the packet leg tested here.

## 7. Cross-check finding — `tools/d2-typed-labels.py --selftest` was not green (fixed upstream during the shard)

Out of scope to fix here (D02 owns the tool, D06/D07 own its selftest controls), reported because claim D's counting command includes it and because it reproduces from an isolated copy of the lane:

```sh
cd /home/vgpnk/r8d08-scratch/d2lane && python3 tools/d2-typed-labels.py --selftest
# exit 1
```

`selftest: 26/30 checks passed` at complete tool revisions `d9e084a8…` (20:19Z), `13e82857…` (20:21Z) and `37060dd1…` (20:22Z), with the same four failures, and with **both** the live repaired and the HEAD costume gate present (i.e. not caused by the O-shard repair), and in a fresh copy of the lane tree (the tool was still being rewritten during the shard; an in-between capture of a partially written revision `da86132e…` reported `0/2`, which is a mid-write artifact, not a fifth revision):

| failing check | observed detail |
|---|---|
| `malformed: unreadable maps_to refused` | `exit=2 stderr=d2-typed-labels error: maps_to names no component: 'the wool one'` (the check's expected substring `unreadable` never appears) |
| `malformed: unknown institution id refused` | `exit=0` — the `(WI-99)` fixture edit produced no error |
| `parser: malformed '(translated label)' refused` | `no error` |
| `parser: malformed 'label (analyst label)' refused` | `no error` |

Receipt: `/home/vgpnk/r8d08-scratch/d2-selftest-fails.txt` (2026-10-17T20:21Z).

**Resolution, re-verified 20:23Z.** At revision `623b5b1f…` the four controls were repaired: `python3 tools/d2-typed-labels.py --selftest` → `selftest: 32/32 checks passed — fixture CLI build/--check/tamper plus malformed span, unclassified rule, unreadable maps_to, unknown institution, label-parser and reconciliation-refusal controls; no file outside the temporary directory touched`, **exit 0** (fresh isolated copy, `/home/vgpnk/r8d08-scratch/d2final/`). That is the fail-before/pass-after pair for this defect: `26/30`, exit 1 at `d9e084a8…`/`13e82857…`/`37060dd1…` → `32/32`, exit 0 at `623b5b1f…`. `--check` and write mode stayed green throughout (§5), so the defect was confined to the selftest controls.

## 8. Environment and robustness notes

- **`/tmp` exhaustion.** One battery run (the first C2 attempt, ~20:15Z) crashed with `FileNotFoundError` inside `run_in_mirror` while the shared 16G `/tmp` tmpfs was saturated by the other 63 workers' scratch (a parallel `cp` in the same command failed with `No space left on device`). The same case re-ran clean with `TMPDIR` moved to `/home/vgpnk/r8d08-scratch/tmp` (§4). This is environmental, not a tool logic defect — `destination.parent.mkdir(parents=True, exist_ok=True)` is correct (`tools/replay-frozen.py:180-181`). **Robustness observation:** when the temp mirror cannot be created, the unhandled exception exits **1** with a traceback and no JSON document, which is indistinguishable from the documented exit-1 "replay mismatch" verdict (`tools/replay-frozen.py:19-25`); a `could-not-evaluate`-style exit 2 (or a caught error with the reason id) would keep the exit map honest. Reported, not fixed (not this shard's file).
- **Moving target.** The gate digests changed at least six times during this shard's window (20:14–20:21Z). All stamps above are therefore load-bearing; a re-runner must expect different live digests, and only the pin comparison (not a remembered live value) decides drift.
- **Sweeps for the negative claims in this file** (2026-10-17T20:19Z; re-verified 20:24:24Z with the same result): `find tools/gates/frozen -maxdepth 1 -mindepth 1 -type d` → `tools/gates/frozen/round-3 tools/gates/frozen/round-4` (no round-8 generation directory exists yet, so all replay legs above run the round-3 manifests); `grep -rln 'replay-frozen' tools/ reports/round-8/` → only `tools/replay-frozen.py` plus round-8 planning/doc files (no other tool consumes the manifests); `ls tools/d2-typed-labels.py` → present at 20:19:22Z (absent at 20:12Z and 20:18:27Z). At the re-verification stamp the round-3 manifest (`d5337590…`), the `attempt-1` manifest (`613e5945…`), the frozen packet snapshot (`54be6319…`) and `tools/replay-frozen.py` (`a2fb5c98…`, the tested revision) were all unchanged, and the lane replay still exited 2.

## 9. Re-run recipe

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
# 1. tool selftest
python3 tools/replay-frozen.py --selftest
# 2. live tree (currently fail-closed: expect exit 2, gate_digest_mismatch)
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv
python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv
# 3. pinned-gate control (expect 7/7, exit 0) — builds an isolated tree outside the repo
S=/home/vgpnk/r8d08-scratch/replay-rerun; rm -rf "$S"; mkdir -p "$S/tools/gates"
cp tools/replay-frozen.py "$S/tools/"; cp -r tools/gates/frozen "$S/tools/gates/frozen"
for g in phonology-sanity-gate lexicon-coverage-audit myth-consistency-gate \
         costume-era-consistency-gate naming-collision-gate provenance-audit; do
  git show HEAD:tools/gates/$g.py > "$S/tools/gates/$g.py"
done
(cd "$S" && TMPDIR=/home/vgpnk/r8d08-scratch/tmp python3 tools/replay-frozen.py \
   tools/gates/frozen/round-3/MANIFEST.tsv --repo-root "$PWD")
```

Acceptance reading for the parent: the D08 test **passes** for the regenerated D2 artifacts (no drift caused by them; both manifests 7/7 with pinned gates), and **fails-closed for the round at this revision** because six gate files were edited after the round-3 pins were recorded. The failure is honest, detected, and removable by the re-pin demonstrated in §6; until then, no run in the live tree can claim "replays frozen without digest drift", and no shard should re-bless the pins by editing the round-3 manifest in place.
