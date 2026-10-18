# R18-O10 — re-pin cascade: before/after pin table (all surfaces)

- round: 18 (operator loop 2 of 3, build round 2 of 4) · shard: **O07..O10**
  (re-pin ×4) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R18-O07..O10 (re-pin x4): execute the cascade as NEW
  pins only: round-11 frozen manifest row for the revised gate (new snapshot dir,
  manifest append), round-9 baseline pins (new baseline revision), round-16 v2-07
  expected.json helper re-pin; before/after pin table each;
  reports/round-18/repin/{r11,r9,v207,table}.md."
- date: 2026-10-18. Baseline revision `3dd3754…`; HEAD `c66ac3c`. Readings stamped
  `2026-10-18T10:2x–10:4xZ`; every row names its command and time.
- canon: NON-CANON engineering evidence. Reproduction is not clearance: several of
  the verdicts below are red findings verdicts, and a reproduced red stays red.
- writes: this file plus the pin artifacts the three per-surface reports name.
  **No filed byte of rounds 8–17 is edited** (§3 re-hashes prove it).
- **status: cascade executed.** Three re-pins landed as new files/dirs; the
  round-11 row's green reading is time-dependent while peer workers still edit the
  gate (§5 states that exposure and the one-line re-pin command).

## 1. The cascade at a glance

| # | surface | before | after | movement | report |
|---|---|---|---|---|---|
| 1 | round-11 frozen generation, typed-pipeline row (design §5 P1/P2) | filed manifest `aad230bf…`, row gate cell `d102fd1d…` | new manifest `6f445739…` (row gate cell re-pointed), new snapshot dir, replay 11/11 green | **gate cell only** | `r11.md` |
| 2 | round-9 baselines (P4) | 8 files / 7 ids `r9-pre`, battery 8 pinned | revision `r18-post`: 7 new baselines, battery 15 files / 15 pinned | **+7 pins, no pin value moved** | `r9.md` |
| 3 | round-16 v2-07 helper baseline (P5) | filed `expected-v2-07.json` `dc75c5d7…` | new `expected-v2-07-r18.json` `d5fda399…`, verify exit 0 | **file/revision only; 0 of 28 input pins moved** | `v207.md` |
| 4 | controls P3/P6/P7 (tools, packets, filed references) | §2 table 4 | identical | **none** | this file §2 |

## 2. Because the gate revision moved, the surfaces this seat re-pinned

| surface | before pin (command + time) | after pin | movement |
|---|---|---|---|
| `tools/gates/typed-pipeline-gate.py` (P10) | `sha256sum` 10:20Z → `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` (the round-11 frozen revision, equal to the filed row cell) | `sha256sum` 10:50Z → `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617` (the revision the re-pin names; unchanged across the freeze run). Earlier in the window the gate also read `ea95e2a1…`, `a201afee…`, `286d6e82…`, `7ec051df…` | **changed** (this is the round-18 generalization; §5) |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `sha256sum` 10:20Z → `aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063` | identical at 10:37Z (after the re-pin build) | **none** (filed byte preserved) |
| `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json` | `sha256sum` 10:37Z → `c49ebc9e71ce870af621604bb0e00886b45ad8f4028777f202ec845ede6cc902` | identical after the build | **none** |
| `tools/gates/frozen/round-11/typed-pipeline/run.log` | `sha256sum` → `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` | identical; the revised gate reproduces it byte-for-byte | **none** |
| `tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` | `sha256sum` → `1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3` (= live `examples/culture-d2/packet.d2.typed.yml`) | identical | **none** |
| round-9 `r9-pre` expected.json set (8 files) | `sha256sum reports/round-9/baselines/*/expected.json tools/gates/expected/*/r9-pre/expected.json tools/gates/frozen/*/r9-pre/expected.json` 10:28Z: `9dc21cd5…`, `a87edc53…`, `2f34ee18…`, `7ec01a1d…`, `2763614f…`, `0fad58ba…`, `425c74c0…` (dual home ×1) | identical at 10:29Z and 10:38Z | **none** |
| the seven reader/legacy gates (P4) | `sha256sum` 10:37Z → naming `d9e4e8f4…`, phonology `d5fe087f…`, costume `e6bffd70…`, lexicon `2c4dd397…`, myth `5368b135…`; handoff `e2fa3223…`; provenance `8a96aaf4…` | identical (they are also the `r18-post` gate pins) | **none** |
| `reports/round-16/handoff/expected-v2-07.json` (P5) | `sha256sum` 10:33Z → `dc75c5d7e347987e81efe6f6fe17314e8f6a2ce26a12a1ca7ec3567a21dcaad1`; helper verify exit 0 | identical at 10:35Z; helper verify exit 0 both before and after | **none** |
| v2-07 helper read set, 28 input pins (P5) | pinned in the filed baseline | key-by-key identical, 0 moved | **none** |
| `tools/assemble-d2.py` (P3, serializer) | `sha256sum` → `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` | identical | **none** |
| `examples/culture-d3/handoff.md` (P3 input) | `sha256sum` → `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc` | identical | **none** |
| `tools/assemble-d2-typed.py` (P6, adapter) | `sha256sum` → `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` | identical; still the pin in the frozen packet's `assembly.adapter_sha256` | **none** |
| `tools/d2-typed-labels.py` (P6, projector) | `sha256sum` → `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | identical; still the `projector_sha256` in `examples/culture-d2/expected-holds.json` | **none** |
| `examples/culture-d2/packet.d2.yml`, `typed-labels.d2.yml` (P6) | `sha256sum` → `e0f21509…`, `a3aa452c…` | identical; both still equal the pins inside `expected-holds.json` | **none** |
| prose references to the superseded gate sha (P7) | `git grep -l d102fd1d` over rounds 8–17 + `corpus/` 10:38Z → **11 files**, 0 modified (`git status --porcelain` over the same paths → 0 lines) | identical sweep | **none** (supersession is signalled only by the round-18 receipts) |
| battery reading (P4) | default roots 10:29Z → `baselines_found 8, pinned 8, gates_uncovered [], exit 0` (pre-change reading reproduced from a mirror with the new dirs removed) | 10:38Z → `baselines_found 15, pinned 15, gates_uncovered [], exit 0` | **+7 baselines**, both readings exit 0 |
| D2 gate behaviour (`--selftest`, default, `--json`, frozen packet) | pre-change (R18-O11 receipts): selftest 12/12, default `15cdfbda…`, `--json` `19765ddf…`, frozen packet `9a69985a…` | post-change: selftest 12/12, default `15cdfbda…` (16/16 legs), `--json` `19765ddf…` (10:41Z), frozen packet `9a69985a…` | **none** — the default path is byte-identical |

## 3. Append-only controls (re-hashed before and after the cascade)

```sh
sha256sum tools/gates/frozen/round-11/MANIFEST.tsv      # aad230bf… → aad230bf…
sha256sum tools/gates/frozen/round-11/typed-pipeline/run-receipt.json   # c49ebc9e… → c49ebc9e…
sha256sum reports/round-9/baselines/*/expected.json …   # the eight r9-pre files, unchanged
sha256sum reports/round-16/handoff/expected-v2-07.json  # dc75c5d7… → dc75c5d7…
git status --porcelain reports/round-8 … reports/round-17   # 0 lines
git grep -l d102fd1d -- reports/round-8 … reports/round-17 corpus  # 11 files, none edited
git status --porcelain tools/gates/frozen/               # only new ?? directories
```

The new pins are new files: `tools/gates/frozen/round-18/repin-d2/**` (the
design's path; re-pin manifest
`sha256 6f44573916ba97f33412c9193fa4dc98fe4cf366733cbdd42c181c609cb7ea6a`, one home
on purpose — §5), `tools/gates/frozen/<gate>/r18-post/**` for the seven gates,
and `reports/round-18/repin/expected-v2-07-r18.json`.

## 4. The full reading command set (one block, re-runnable)

```sh
TMPDIR=/var/tmp/kotodama-r18-repin python3 tools/replay-frozen.py \
  tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv          # 11/11 reproduced
TMPDIR=/var/tmp/kotodama-r18-repin python3 tools/replay-frozen.py \
  tools/gates/frozen/round-11/MANIFEST.tsv                   # filed row 1: could-not-evaluate
python3 reports/round-18/run-validation.py --check           # read-only; no receipt written
python3 tools/check-gate-battery.py                          # 15 files, 15 pinned, exit 0
python3 .scratch/o07/freeze-r18-baselines.py --check         # check: OK
python3 reports/round-15/handoff/frozen-verify.py --baseline \
  reports/round-16/handoff/expected-v2-07.json               # exit 0 (filed)
python3 reports/round-15/handoff/frozen-verify.py --baseline \
  reports/round-18/repin/expected-v2-07-r18.json             # exit 0 (round-18)
```

## 5. Open exposure: the pinned gate revision is a moving target during the wave

Observed gate shas this seat measured between 10:29Z and 10:50Z:
`bba60bc18ebc…` → `edfec5f37a51…` → `3897833101be…` → `5b4501a9dd8c…` →
`d4785d9afc03…` → `ea95e2a1452e…` → `a201afeeb5fa…` → `286d6e827114…` (quiet
10:40–10:44Z) → `7ec051df3429…` → `d96958b6a642…` (the revision this delivery
pins, frozen 10:50Z). Each move makes the re-pin row read `gate_digest_mismatch`
(could-not-evaluate) until the row is re-pointed — the standard's "revised gate"
class, not a re-pin defect. The verdict side never moved: at `ea95e2a1…`,
`286d6e82…` and `d96958b6…` the re-pin reproduced exit 0, 15 findings and stdout
`9a69985a…` byte-identical to the filed round-11 `run.log`.

What this means, stated plainly:

- The re-pin row in this delivery pins `d96958b6…`, the live revision at freeze
  time (10:50Z), which reproduced the filed round-11 verdict byte for byte. If the
  gate settles on a later revision, the cell must be re-pointed before the round's
  counting command is run — one value, one command, §5 below.
- **The runner discovers the re-pin** (`run-validation.py:137-145` globs
  `tools/gates/frozen/round-18*/**/MANIFEST.tsv`) and requires every discovered
  round-18 manifest to replay green (`run-validation.py:884-893`). At 10:48Z it
  read the re-pin as **11/11 reproduced, exit 0**. That also means this leg goes
  red if the gate revision moves before integration — the re-pin cell (above) is
  the answer, and the D4 seat's report records the same exposure for its own
  generation (its copy of a gate-pinned row was dropped for that reason,
  `reports/round-18/d4/manifest.md` §4).
- Re-pin is one cell and is scripted; the manual form is:

```sh
NEW=$(sha256sum tools/gates/typed-pipeline-gate.py | cut -d' ' -f1)
for f in tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv; do
  python3 - "$f" "$NEW" <<'EOF'
import sys, pathlib
path, new = pathlib.Path(sys.argv[1]), sys.argv[2]
text = path.read_text(encoding="utf-8").splitlines()
for index, line in enumerate(text):
    if line.startswith("tools/gates/typed-pipeline-gate.py\t"):
        cells = line.split("\t"); cells[1] = new
        text[index] = "\t".join(cells)
path.write_text("\n".join(text) + "\n", encoding="utf-8")
EOF
done
TMPDIR=/var/tmp/kotodama-r18-repin python3 tools/replay-frozen.py \
  tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv     # must read 11/11
```

- The re-pin is safe to repeat because it is a substitution in **this seat's own
  new files**: the filed round-11 generation is never touched, and the recorded
  exit (0), finding count (15), output bytes (`9a69985a…`) and the other ten rows
  stay byte-equal. A later revision that changed the D2 verdict would show up as a
  replay mismatch — that is the control, and it is the reason the row is replayed
  rather than assumed.
- The builder used here is `.scratch/o07/build-repin-d2.py --build|--verify`
  (gitignored scratch, single-writer, no filed path opened for writing).
- The runner's own reading of the cascade (10:43Z and 10:44Z,
  `python3 reports/round-18/run-validation.py --check`, read-only, no receipt
  written): `round18_revision_pins` 7 baselines / problems `[]`;
  `round9_pins` 5 / `[]`; `round16_v207` 28 pins all `ok` with
  `filed_byte_identical: true`; `pin_ledger[tools/gates/typed-pipeline-gate.py]`
  `before d102fd1d… after d96958b6…` recorded in this seat's `r11.md`, the new
  receipt and `freeze.txt`; `d2_path` default / `--json` / frozen-row stdout
  `stdout_identical: true`; every regression exit 0. The only claim-O failures at
  that stamp were the D4 legs (`assemble-d4-typed.py` missing) — claim-D
  dependencies, not the cascade.

## 6. Limits

- The cascade re-pins **pins**, not policy: a green replay says the frozen input,
  under the pinned revision, produced the recorded verdict. Four of the seven
  round-9 revisions are red findings verdicts and the D2 typed packet still emits
  15 open holds.
- Only the surfaces named in design §5 are in scope here. A surface not pinned by
  these files (a new D4 profile file, the D4 adapter) is another seat's pin.
- The v2-07 helper pins its own constant read set; the round-18 re-pin does not
  widen it, so a value the helper never reads is not covered by that file.
- Nothing here certifies that the final gate revision is the right design or that
  the round-18 gate work is complete; it records which bytes were pinned when, and
  what reproduced.

| tools/gates/typed-pipeline-gate.py | d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617 | 04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48 | 2026-10-18 | integrator L2 completion: D4-family channel accounting — removed-artifact count compares against costumes whose field actually moved (6), not the routing-row count (12); D2 default behavior byte-identical (16/16 legs pre- and post-) |
