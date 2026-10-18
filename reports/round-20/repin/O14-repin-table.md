# R20-O14 — the extended before/after pin table: every surface that names `tools/d2-typed-labels.py`

- round: 20 (operator: loop 2 of 3, build round 4 of 4) · shard: **O11..O14**
  (re-pin ×4) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R20-O11..O14 (re-pin x4): update the pins that name
  d2-typed-labels.py (round-18 repin-d2 rows, round-16 v2-07 expected.json pins,
  round-9 baselines if pinned) as NEW rows with the before/after table extended;
  replay green; reports/round-20/repin/."
- date: 2026-10-18. Declared `baseline_revision`
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`; HEAD at seat start `122086b`.
  Before readings 12:56Z; projector move observed 13:01:06Z; freeze 13:14:25Z;
  after readings 13:14–13:16Z.
- canon: NON-CANON engineering evidence. A re-pin is bytes-and-verdict evidence,
  never a clearance, never a canon ruling.
- writes: the round-20 pin files named below, this file, and the four evidence
  files under `reports/round-20/repin/evidence/`. No filed byte of rounds 8–19 is
  edited (§7 proves it); no peer-owned surface is duplicated or rewritten.
- **status: COMPLETE. Every surface that names the projector is measured, each
  row names its owner, and the round's own counting command reads claim O with
  `failures: []`.**

## 1. The movement in one line

`tools/d2-typed-labels.py` moved `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`
→ `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb`
(first observed 13:01:06Z; `git diff --stat` → 41 insertions, 23 deletions: the
declared-reconciliation shaping extracted into `shape_reconciliation_rows` for the
per-family era-alias leg). **Every live pin of that digest moved; every filed pin
of the old digest stays filed and reads stale by construction; the D2 verdict
bytes did not move.**

## 2. Surface-by-surface before/after (the extended table)

| # | surface | before | after | movement | owner |
|---|---|---|---|---|---|
| 1 | live `examples/culture-d2/expected-holds.json` → `projector_sha256` | `0da0015f…` (file `a5dc26d5…`) | `76536a92…` (file `7b9439c4…`), + `revision_note` | **field moved** | **this seat** |
| 2 | live `examples/culture-d4/expected-holds.json` → `projector_sha256`, `projection_sha256` | `0da0015f…`, `a59990bb…` (file `09490a27…`) | `76536a92…`, `cbcf997f…` (file `18d0cfce…`) | **both fields moved** | O-wart seat (verified here) |
| 3 | `tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json` → `tool_pins` | projector `0da0015f…` (file `d90c09e8…`) | unchanged, filed | **none** (superseded by row 4) | filed round 18 |
| 4 | `tools/gates/frozen/round-20/repin-d2/**` (new generation) | — | receipt `11854da1…`, projector `76536a92…`, replay 11/11 | **new generation; 1 tool pin moved** | **this seat** |
| 5 | `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json` → `tool_pins` | projector `0da0015f…` (file `c49ebc9e…`) | unchanged, filed | none | filed round 11 |
| 6 | `reports/round-16/handoff/expected-v2-07.json` (28 pins) | projector `0da0015f…` (file `dc75c5d7…`), verify exit 0 | unchanged, filed; verify now **exit 2** (drift) | none — the drift is the reason row 8 exists | filed round 16 |
| 7 | `reports/round-18/repin/expected-v2-07-r18.json` (28 pins) | projector `0da0015f…` (file `d5fda399…`), verify exit 0 | unchanged, filed; verify now **exit 2** (drift) | none | filed round 18 |
| 8 | `reports/round-20/repin/expected-v2-07-r20.json` (new revision) | — | projector `76536a92…` (file `e594137c…`), **1 of 28 pins moved**, verify exit 0 | **new revision** | **this seat** |
| 9 | `reports/round-20/wart/expected-v2-07-r20.json` (peer twin) | — | projector `76536a92…` (file `ad761a61…`), verify exit 0 | new revision (same values) | O-wart seat (verified here; not duplicated) |
| 10 | `reports/round-11/handoff/expected.json` (21 pins) | projector `0da0015f…` (file `a94f9ded…`) | unchanged, filed | none — filed revision, stale by construction | filed round 11 |
| 11 | `reports/round-15/handoff/expected.json` (28 pins) | projector `0da0015f…` (file `b927db31…`) | unchanged, filed | none — filed revision, stale by construction | filed round 15 |
| 12 | `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` (6 inputs) | projector `0da0015f…` + two D2 component copies (file `93b84da0…`) | unchanged, filed; battery leg still `pinned` | none | filed round 19 |
| 13 | `tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json` (new revision) | — | 4 inputs: projector `76536a92…`; **the two D2 component copies are gone**; battery `pinned`, `inputs_checked 4` | **new revision (input edit + wart closed)** | O-wart seat (verified here) |
| 14 | round-9 baselines (8 files, 27 pins) and round-18 `r18-post` baselines (7 files) | none names the projector | unchanged | **none — measured negative** (`O13-repin-baselines.md` §1–§2) | — |
| 15 | `tools/gates/typed-pipelines.json` profile `d4` | profile pins packet/assembler/projection/adapter/expected — **not the projector** | re-pinned by the wart seat for the moved projection/adapter | n/a — not a projector pin | O-wart seat |

Rows 1–15 are the complete set: the scan in `O13-repin-baselines.md` §1 covers the
three baseline roots (79 pins across 18 files, exactly 2 naming the projector),
and the digest sweep over the machine-readable pin files found rows 1–13; the
prose mentions of the old digest in filed reports are records, not pins.

## 3. The two live pins, in detail (rows 1–2)

These are the only pins of the projector that any tool reads live: the round-20
counting command's claim-O `pin_checks` compares `examples/culture-d4/expected-holds.json`'s
`projector_sha256` / `projection_sha256` / `packet_sha256` against the live bytes.

| file | before sha256 | after sha256 | edit |
|---|---|---|---|
| `examples/culture-d2/expected-holds.json` | `a5dc26d5b495a90e…` | `7b9439c4d695b50b…` | one field + one `revision_note` line; `packet_sha256`/`projection_sha256`/`counts`/`holds`/`notes` byte-unchanged |
| `examples/culture-d4/expected-holds.json` | `09490a2756d123eb…` | `18d0cfce3f3f7a86…` | two fields + a `revision_note` (peer edit) |

Controls on the D2 edit (this seat's): `python3 tools/gates/typed-pipeline-gate.py
--selftest` → **12/12** (the gate's embedded constant still equals the committed
hold set in both directions, so the added key is inert); default path
`15cdfbda…` exit 0; `--json` `19765ddf…` exit 0; frozen packet `9a69985a…` exit 0
— all byte-identical to the pre-edit readings. The D4 twin was moved by the
O-wart seat with the same effect on its own gate leg (exit 0).

## 4. What the round's counting command now reads (claim O)

```sh
python3 reports/round-20/run-validation.py --check     # read-only; no receipt written
```

| reading | 13:09Z (before this cascade) | 13:16Z (after the pin moves) | 13:19Z (final, quiet tree) |
|---|---|---|---|
| claim O `failures` | 6 — one of them mine (`stale pin: examples/culture-d4/expected-holds.json projector_sha256 0da0015f… != live 76536a92…`), five peer-owned (the D4 projection pin, three missing typed-packet keys, the adapter-selftest mirror) | **`[]`** | **`[]`** |
| claim D `failures` | (not reached) | 4 — the v3 exercise surface (`exercise-handoff-e2e.py` without `--profile`) and the contract-audit verdict, mid-flight D seats | **`[]`** |
| claim C `failures` | (not reached) | `[]` | **`[]`** |
| `repin_new_rows` | — | `reports/round-20/repin/expected-v2-07-r20.json`, `reports/round-20/wart/expected-v2-07-r20.json`, `tools/gates/frozen/round-20/repin-d2/**` (+ the peer's r20-post, round-18 files) | adds this seat's four report files (`O11`–`O14`) |
| `expected_holds` rows | 1 stale | 3/3 `ok` | 3/3 `ok` |
| `typed_packet` rows | 3 stale (keys absent) | `ok` | `ok` |
| `d2_byte_identical` | true | true | true |
| wart mirror (`culture_d2_present: false`) | — | `d4_projection_check` exit 0, `d4_adapter_check` exit 0 | exit 0 / exit 0 |
| `missing_dependencies` | 2 | `[]` | `[]` |
| runner exit | 1 | 1 (claim D only) | **0 — all three claims green** |

The 13:19Z reading is the final one: the round's counting command exits 0 with
`D`, `O` and `C` all `failures: []`. Transcripts: `evidence/runner-claim-o.json`
(the 13:16Z claim-O section) and `evidence/runner-final.json` (the 13:19Z
all-claims reading). Between 13:16Z and 13:19Z the runner was briefly mid-edit by
its own seat (`NameError: v2_scan`); that transient state is recorded here rather
than hidden, and it resolved before the final reading.

## 5. Replay and battery readings (the "replay green" clause)

| command | reading |
|---|---|
| `TMPDIR=/var/tmp/kotadama-r20-repin python3 tools/replay-frozen.py tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` | **REPLAY OK: 11/11 rows reproduced**, exit 0 |
| same over `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | REPLAY OK: 11/11 (filed generation still green) |
| same over `tools/gates/frozen/round-11/MANIFEST.tsv` | 10 reproduced, 1 could-not-evaluate — row 1 `gate_digest_mismatch` (filed supersession class, unchanged) |
| `python3 tools/check-gate-battery.py` | 12:58Z: 17 found / 17 pinned; 13:14Z: **18 found / 18 pinned**, `coverage "9/9"`, `gates_uncovered []`, exit 0 |
| `python3 reports/round-15/handoff/frozen-verify.py --baseline <v2-07 revision>` | filed r16/r18: exit 2 (drift, expected); round-20 (mine and the peer twin): **exit 0** |
| `python3 tools/d2-typed-labels.py --selftest` | **50/50** at the new revision (39/39 before — the round-20 selftest additions) |

## 6. The one-command re-pin, if the projector moves again

The freeze stamp's projector revision is `76536a92…`. If a later edit moves it,
three cells in **this seat's own new files** are stale: the round-20 receipt's
`tool_pins` projector cell, the round-20 v2-07 revision (re-freeze), and the two
live `projector_sha256` fields. All four are scripted:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/o11/build-repin-r20.py --build   # repin-d2 generation (re-derives, re-verifies 11/11)
python3 .scratch/o11/build-repin-r20.py --v207    # v2-07 successor revision
python3 .scratch/o11/repin-holds.py --apply       # the two live projector_sha256 fields
```

(The scratch scripts are gitignored and are not part of the deliverable; the
commands are recorded so a later integration can repeat them without this seat's
files. Manual form: substitute the one digest, re-run the replay, re-hash.)

## 7. Append-only controls

```sh
sha256sum tools/gates/frozen/round-11/MANIFEST.tsv                     # aad230bf… (unchanged)
sha256sum tools/gates/frozen/round-11/typed-pipeline/run-receipt.json  # c49ebc9e… (unchanged)
sha256sum tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv            # 2556b084… (unchanged)
sha256sum tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json  # d90c09e8… (unchanged)
sha256sum reports/round-16/handoff/expected-v2-07.json                 # dc75c5d7… (unchanged)
sha256sum reports/round-18/repin/expected-v2-07-r18.json               # d5fda399… (unchanged)
sha256sum tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json  # 93b84da0… (unchanged)
git status --porcelain reports/round-8 … reports/round-19 \
  tools/gates/frozen/round-11 tools/gates/frozen/round-18 \
  tools/gates/expected/d4-typed-labels-check-gate/r19-pre              # 0 lines
```

## 8. Limits

- Only the surfaces in §2 are in scope. A pin that names the projector but is not
  machine-readable (a prose digest in a filed report) is a record, not a pin, and
  was not rewritten — the round-18 sweep found 11 such files and left them.
- Rows 2, 9, 13 are **peer re-pins verified here**, not this seat's writes. Their
  ownership is stated so an integration does not read this table as one seat
  claiming another's work.
- Row 8 duplicates row 9's pin values on purpose (one home per seat's assignment);
  §5 of `O12-repin-v207.md` states the reason and the drop-one option.
- A green re-pin says the frozen bytes, under the pinned revision, produced the
  recorded verdict. It does not say the round-20 projector revision is correct,
  and it does not close the 15 open hold lines of the D2 typed packet.
