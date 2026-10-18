# R17-D25 — assembler integration: the D4 assembler over the delivered D4 tree

- seat: **R17-D25** (assembler integration; round 17, operator loop 2 of 3,
  build round 1 of 4; 64 declared workers, `opencode-go/deepseek-v4.1-flash`).
  Date 2026-10-18, all stamps UTC (local UTC-3). Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; HEAD `9b49a4a` (round-17
  declare), baseline `f30b6f8` (round-16 admit) throughout.
- assignment (verbatim): "D4 R17-D25 (assembler integration): run the new
  assembler over the D4 tree; --check byte-identical;
  reports/round-17/assembler/integration.md."
- writes, complete list: `reports/round-17/assembler/integration.md` (this
  file). Scratch only under `.scratch/d25/` (`export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command). The integration's full assembler
  runs rewrote the assembler's own output in place; every byte of
  `examples/culture-d4/**` and every `tools/*.py` file is snapshot-compared
  before/after and **unchanged** (§3.3). No other file written; no commit, no
  push; no filed round-8–16 byte touched.
- canon: NON-CANON engineering evidence. A green `--check` is a structural
  reproduction result, not clearance, canon, a handoff or a design verdict.

## 0. Verdict

`tools/assemble-culture-d4.py` (final revision measured: sha256
`03a0754eec5565aad76598be53de4ba26e0199c81a30814ec88e87e31951f466`) was run
over the delivered `examples/culture-d4/` tree at **09:43:58–09:43:59Z**:

1. `--check` on the delivered tree → **exit 0, "packet.d4.yml: byte-identical
   deterministic assembly"** (three times: before regeneration, after each of
   two full builds, and once from outside the repo).
2. Two consecutive full builds → **byte-identical output**
   (`examples/culture-d4/packet.d4.yml`, sha256
   `39c2d56a2ac357e2e8baf06eae94dc6c6c07740d39f4e85ee69ed1723c565038`,
   80509 bytes, both runs).
3. `--selftest` → **exit 0, 81/81 checks**.
4. Snapshot control: 38 sha256 lines (the 14-file D4 tree + the assembler +
   all 23 `tools/*.py`) **identical before/after** the full runs; the whole-run
   `git status --porcelain` delta is empty — the runs wrote nothing anywhere
   else.
5. The packet's own pin block re-verifies against delivered bytes:
   `assembler_sha256`, `reader_sha256`, `serializer_sha256` and **12/12**
   `source_sha256` component entries match (§3.4). The packet declares
   NON-CANON and carries no clearance/rights token.

Claim-O caveat reported, not absorbed: at measurement time the D4 **typed**
artifacts (`typed-labels.d4.yml`, `packet.d4.typed.yml`, `expected-holds.json`)
had **not yet landed** — they are other seats' deliverables still in flight
(§5.2). This seat's integration covers the assembler and its one owned output,
exactly as assigned.

## 1. Dependency wait record

Two 60 s-cadence polls from the lane root (logs kept at
`.scratch/d25/poll.log` and `.scratch/d25/poll2.log`):

| poll | window (UTC) | ticks | result |
|---|---|---|---|
| 1 | 09:15:52Z → 09:35:52Z | 21 (cap) | tree absent throughout; `tools/assemble-culture-d4.py` first observed at tick 18, **09:32:52Z** (`tree_files=0 tool=1`) |
| 2 | 09:33:34Z → 09:43:34Z | 11 | **READY at tick 11, 09:43:34Z**: `components=12 packet=1` |

The tree's first files (`examples/culture-d4/packet.d4.yml`, 12 components)
appeared 09:42:59–09:43:38Z; `brief.md` landed 09:43:38Z. Integration ran
09:43:58Z, after readiness. The poll-1 window ended at its declared 20-minute
cap; poll 2 covered the landing. Scratch recon during the wait recorded the
wave alive (design components landing under `reports/round-17/d4/components/`
from 09:22Z, typed-support and design docs, C-axis civ fragments) — the
extension past poll 1's cap is this seat's, taken because landings were
visibly in progress, and is recorded here as such.

## 2. The delivered tree and the tool

### 2.1 Tree at measurement (09:43:58Z, 14 files)

`examples/culture-d4/`: `brief.md`, `components/01-brief.yml` …
`components/12-provenance.yml` (12 files), `packet.d4.yml`. The assembler's
owned output is the single packet; the 12 components are the inputs it pins.

### 2.2 Tool revision history observed this round

| revision (sha256) | observed | selftest measured |
|---|---|---|
| `8661ea153750be1e525cfa093d289c7f3a8ab0050c87312d89ebe3d4e7f080f8` | first landing, 09:32:52Z | 79/79 (09:33Z) |
| `61e04320cee18f7f45e01e3439ccc0424edabb1db140b088b3142458671eb2db` | mid-round revision, ~09:40Z | 81/81 (09:40Z) |
| `03a0754eec5565aad76598be53de4ba26e0199c81a30814ec88e87e31951f466` | final at measurement (file mtime 09:41:07Z) | 81/81 (09:43:58Z) |

The delivered packet (mtime 09:42:59Z) was built by the final revision: its
embedded `assembly.assembler_sha256` equals `03a0754e…` and `--check` exits 0
(§3). The interim counts are recorded because `reports/round-17/assembler/
impl.md` cites "81 checks" — true of the final revision, not of the first
(§5.1).

### 2.3 CLI (read from `--help`, 09:43:58Z)

`python3 tools/assemble-culture-d4.py` writes exactly
`examples/culture-d4/packet.d4.yml`; `--check` compares bytes without writing
(exit 0 equal / 1 drift / 2 error); `--selftest` runs fixture controls in one
temporary directory. Contract: per-file `packet_keys` declarations (allowlist
fallback), non-packet keys recorded under `assembly.skipped_keys`, collisions
fail closed, packet-owned `name`/`canon`/`assembly`, self-pin of the tool
digest.

## 3. Measurements (all 2026-10-18)

### 3.1 Command table

| # | command (lane root, `TMPDIR=$PWD/.scratch`) | exit | stdout/stderr |
|---|---|---|---|
| 1 | `python3 tools/assemble-culture-d4.py --check` (delivered state) | 0 | `packet.d4.yml: byte-identical deterministic assembly` |
| 2 | `python3 tools/assemble-culture-d4.py` (full build) | 0 | `Wrote examples/culture-d4/packet.d4.yml (80509 bytes)` |
| 3 | `python3 tools/assemble-culture-d4.py --check` | 0 | same as #1 |
| 4 | `python3 tools/assemble-culture-d4.py` (second full build) | 0 | `Wrote … (80509 bytes)` |
| 5 | `python3 tools/assemble-culture-d4.py --check` | 0 | same as #1 |
| 6 | `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed — … no file outside the temporary directory touched` |
| 7 | `cd /tmp && python3 <repo>/tools/assemble-culture-d4.py --check` | 0 | same as #1 (run-from-any-directory holds) |

Pre-landing control (09:33Z, tree absent): `--check` → **exit 2**,
`assembly error: components directory not found: examples/culture-d4/components`
— fail-closed, no traceback, matching `impl.md` F-O-3.

### 3.2 Determinism

Two full builds of the same delivered tree both wrote 80509 bytes and the
packet's sha256 was `39c2d56a…` before and after the runs (measured by
`sha256sum` immediately before the harness and again after it, §3.3). The
delivered bytes therefore equal the deterministic assembly — the claim's
"twice byte-identical" leg, measured independently by this seat.

### 3.3 Side-write control

`.scratch/d25/snap.sh` hashes every file under `examples/culture-d4/`, the
assembler itself, and every `tools/*.py` (excluding `__pycache__`): **38
lines before, 38 after, `diff` empty**. `git status --porcelain` diff over the
run window: empty. The full builds wrote only their one owned output, and its
bytes did not change.

### 3.4 Packet pins re-verified against delivered bytes

Parsed with the packet's own reader (costume gate `parse_packet`, read-only
via `runpy`), 09:44Z:

- `assembly.assembler_sha256` == sha256(`tools/assemble-culture-d4.py`) → OK
- `assembly.reader_sha256` == sha256(`tools/gates/costume-era-consistency-gate.py`) → OK
- `assembly.serializer_sha256` == sha256(`tools/assemble-d2.py`) → OK
- `assembly.source_sha256`: 12/12 entries match the delivered component bytes → OK
- `name` = `D4 culture drill — round-17 design build (NON-CANON)`;
  `canon` = `not canonized (D4 NON-CANON design drill)`; the `non-canon`
  marker is present.
- Clearance sweep (2026-10-18T09:44Z): lowercased packet text grepped for
  `clearance granted`, `rights cleared`, `canonized (admitted)`,
  `community approved` → **0 of 4 present** (command in §7's probe); this
  names the sweep for the negative claim.
- `assembly.skipped_keys`: 75 recorded non-packet keys;
  `assembly.block_scalars_elided` counts recorded per component (2–5 each,
  30 total) — the F-O-1 reader shim is visible in the packet, not silent.

## 4. d2/d3 untouched and green (read-only, this seat's own runs)

Digests at 09:16Z and re-read 09:44Z, identical; filed-round records match
(round-11/round-14 receipts): `tools/assemble-d2.py` `8ea6bdde…`,
`tools/assemble-culture-d3.py` `ba8d19d5…`, `tools/d2-typed-labels.py`
`0da0015f…`, `tools/assemble-d2-typed.py` `c7e5a749…`. Green legs measured
09:16–09:17Z: `assemble-d2.py --check` exit 0 / `--selftest` 42/42;
`assemble-d2-typed.py --check` exit 0; `d2-typed-labels.py --check` exit 0;
`assemble-culture-d3.py --check` exit 0 / `--selftest` 85/85;
`typed-pipeline-gate.py --json` exit 0, 16/16 legs, holds 15 / note 1,
`translated_on_sound_channel` 0.

## 5. Findings — reported, never absorbed

1. **Tool revision count moved (informational).** `impl.md` cites 81 selftest
   checks; the first landed revision (`8661ea15…`) measured **79/79** at
   09:33Z, the final revision (`03a0754e…`) **81/81** at 09:43:58Z. No defect:
   the count tracks the tool revision; a pin should cite the revision, and the
   final one is green at this seat's stamp.
2. **Typed artifacts not yet landed (scope note).** At 09:43:34–09:44Z
   `examples/culture-d4/` held the brief, 12 components and `packet.d4.yml`;
   `typed-labels.d4.yml`, `packet.d4.typed.yml` and `expected-holds.json` were
   absent (still in flight — the runner's claim-D discovery listed the same at
   09:15Z). This integration measures the assembler leg only; the typed chain,
   hold-set equality and frozen replay are other seats' measurements.
3. **Design-family divergence (context, F-O-2 in `impl.md`).** The delivered
   components follow the furnace-league family (`01-brief` … `12-provenance`);
   `design-brief.md` §5 specifies the weigh-court registry. The assembler
   merged the delivered set deterministically via per-file `packet_keys` and
   recorded 75 non-packet keys rather than guessing; adjudicating the design
   families is the parent's call, not this seat's.
4. **Concurrent writers observed.** During the wait, other seats' files landed
   in `reports/round-17/**` (design, typed-support, civ, tests, assembler
   impl/tests) and the corpus C-edits stayed in flight; none touched the D4
   tree during the measurement window (§3.3), and none was modified by this
   seat.

## 6. Limits

- A green `--check`/`--selftest` is structural reproduction, not a design
  verdict; the packet is red by design (holds ride the typed pipeline).
- The measurement pins the tree at 09:43:58–09:44Z; later edits by other seats
  would move the digests (a pin is a read-time pin). `--check` re-run after
  this file was written remains exit 0 (final re-check, §7).
- This seat did not run the D4 typed adapter/projector/gate, the frozen
  replay, or the validation runner's full O leg; the runner grades claim O
  itself (`reports/round-17/run-validation.py`), and its inputs are the green
  legs recorded here.

## 7. Receipts

```sh
# 2026-10-18, lane root, TMPDIR=$PWD/.scratch for every command
python3 tools/assemble-culture-d4.py --check                 # exit 0, byte-identical (delivered)
python3 tools/assemble-culture-d4.py                         # exit 0, Wrote … (80509 bytes)
python3 tools/assemble-culture-d4.py --check                 # exit 0
python3 tools/assemble-culture-d4.py                         # exit 0, Wrote … (80509 bytes)
python3 tools/assemble-culture-d4.py --check                 # exit 0
python3 tools/assemble-culture-d4.py --selftest              # exit 0, 81/81
( cd /tmp && python3 "$REPO/tools/assemble-culture-d4.py" --check )   # exit 0
diff .scratch/d25/before.sha .scratch/d25/after.sha          # empty (38/38 lines)
python3 tools/assemble-culture-d4.py --check                 # final re-check after this file: exit 0
```

Pin + clearance probe (inline `python3` heredoc, 09:44Z): loads the packet with
the costume gate's `parse_packet` (read-only `runpy`), compares
`assembler_sha256`/`reader_sha256`/`serializer_sha256` and all 12
`source_sha256` entries against delivered bytes (all OK), then lowercases the
packet text and greps for the four clearance tokens above (0/4 present).

Digests (2026-10-18T09:44Z):

| artifact | sha256 |
|---|---|
| `tools/assemble-culture-d4.py` (measured revision) | `03a0754eec5565aad76598be53de4ba26e0199c81a30814ec88e87e31951f466` |
| `examples/culture-d4/packet.d4.yml` | `39c2d56a2ac357e2e8baf06eae94dc6c6c07740d39f4e85ee69ed1723c565038` |
| `examples/culture-d4/brief.md` + 12 components | pinned in the packet's `assembly.source_sha256` (12/12 verified) |
| `tools/assemble-d2.py` (untouched) | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `tools/assemble-culture-d3.py` (untouched) | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| `tools/d2-typed-labels.py` (untouched) | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `tools/assemble-d2-typed.py` (untouched) | `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` |

Sources read: `reports/round-17/{claims,targets}.json`, `scope.md`,
`d4/design-brief.md` §5/§7.1, `d4/typed-support-1.md` §5, `assembler/impl.md`,
`examples/culture-d4/**` (read-only apart from the assembler's own output),
`.scratch/d25/{poll,poll2}.log`, `.scratch/d25/{before,after}.sha`.
