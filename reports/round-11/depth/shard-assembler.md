# R11-D03 — assembler shard: typed-label consumption in the D2 assembly step

- seat: **R11-D03** (assembler shard, claim D `d2-typed-pipeline`), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D03 (assembler shard): implement assembler consumption of typed labels per design; deliver code as fragment reports/round-11/depth/shard-assembler.md (integrator D05 owns the tool files)."
- writes: **this file only** (all prototypes, mirrors and receipts live under `.scratch/D03/**`). No file outside `.scratch/` and this fragment was written; no commit, no push. `reports/round-{8,9,10}/**` were read only.
- canon: NON-CANON engineering evidence. No culture claim, no canon decision, nothing admitted.
- revision at read time: `git rev-parse HEAD` → `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (2026-10-17T22:10Z; sibling seats edit the tree concurrently, so every pin below names its file and its observation).
- design dependency: **landed** — `reports/round-11/depth/design.md` (R11-D01) was absent when this shard started and landed during the work; §2.2/§2.3 of that file are the contract implemented here. An earlier prototype of this seat (58-row router, advisory stale pin) was discarded when the design landed; nothing of it is in the code below.

## 1. What this shard delivers

One new file, **`tools/assemble-d2-typed.py`** (design §2.2/§7: "D03/D04 · `tools/assemble-d2-typed.py` · projection + packet"). Per this shard's assignment the file is delivered as a fragment for the integrator **D05** to land; the verified source is

- path: `.scratch/D03/assemble-d2-typed.py`
- sha256: `95ac9d05ff880234e4fafa33de3cac09db2fee248c760c61fa2dda7631318215` (2026-10-17T22:2xZ, 455 lines)
- landing check for the integrator: `cp .scratch/D03/assemble-d2-typed.py tools/assemble-d2-typed.py && sha256sum tools/assemble-d2-typed.py` → the sha above; the copy in Appendix A is byte-identical (checked by extracting the fenced block and hashing it).

CLI exactly as designed (§2.2):

```
python3 tools/assemble-d2-typed.py [--packet P] [--projection J] [--emit PATH] [--check [PATH]] [--selftest]
```

- `--emit PATH` writes the typed gate-facing packet (parent directories created); nothing is written without it.
- `--check PATH` byte-compares without writing (exit 1 on drift); `--check` **with no PATH** builds twice and asserts the two builds are byte-identical (the determinism leg of §2.2).
- exit `0` ok · `1` check/determinism mismatch · `2` could-not-evaluate (stale pin, non-assembly packet, coverage violation, unreadable input) — the exit-2 class always prints one named diagnostic, never a traceback, per `depth/test-boundary.md` §6's expectation for the wired subjects.

Nothing else is touched: the adapter reads four paths (packet, projection, assembler, projector), writes only `--emit`'s target, and no gate script, `tools/assemble-d2.py`, `tools/d2-typed-labels.py`, `examples/**` file or filed round artifact is modified.

## 2. Conformance to design §2.2/§2.3, check by check

| design rule (§2.2) | implementation (line) | control | receipt |
|---|---|---|---|
| assembler identity: `--packet` bytes equal `assemble-d2.py`'s deterministic assembly, "call the assembler's own build path; do not re-implement" | `check_assembler_identity()` `:101` calls `runpy.run_path(tools/assemble-d2.py)["assemble"]()` `:76` and compares bytes | tampered packet byte | selftest: "assembler identity: a tampered packet is exit 2"; §3.6 |
| projection freshness, both legs: pin equals the packet's sha256 **and** `d2-typed-labels.py` reproduces the projection byte-for-byte; "stale pin is a hard error, never a warning" | `check_projection_freshness()` `:110` — pin compare, then `run_pipeline()` + `serialize()` byte compare | committed (stale) projection; hand-edited projection | §3.2 `stale_pin_exit=2`; §3.6 |
| coverage: exactly one row per off-channel label; every routed record in the packet; no row for a record the projector did not type | `off_channel_labels()` `:136` (the projector's own off-channel set), `source_field()` `:147` (owner→section/field, cross-checked against `label.source.field`), `routing_rows()` `:162`, `apply_rows()` `:195` (the record must exist and still carry the field) | missing record / no field to route / double route / owner with no section / source-field mismatch | selftest: three coverage refusals |
| routing table = kind → channel, the five §2.3 rows | `off_channel_labels()`: `translated-label` (any status) and `kind in (native-form, borrowed-strata)` with `status in (absent, to-verify)`; no-asserted-kind carried as `kind: null`, `hold: to-verify` + `detail` | probe per class | selftest: "R5 … routed and held", "T1 row 5 …" |
| output: packet blocks + `typed_channel` rows + `assembly` pins | `build()` `:211` — each routed record's checked field is **moved**, not copied (`garment` → `garment_gloss`), nothing else on the record changes; row keys in the design's order (`ROW_KEYS` `:57`) | full-record diff against the legacy packet | §3.4 invariants: only the routed field differs; `lexicon`/`names` blocks byte-equal |
| determinism; `--check` compares bytes without writing | `emit()` `:249` | two emits + both `--check` forms | §3.3 |
| build product never rots in `examples/` (§2.1) | no default emit path exists; `--emit` is required to write | — | by construction |

One honest statement of the coverage argument, since a reviewer (D20/D22) should attack it rather than take it on trust: the routing rows are **generated from** the projector's own off-channel label set, so "row set == typed off-channel set" is true by construction; what the adapter actually *verifies* is (a) every such record exists in the packet, (b) it still carries the field it used to be checked on, (c) no record is routed twice, (d) the label set cannot be hand-edited, because the projection must be reproduced byte-for-byte by the projector. The teeth are therefore in the freshness and field-presence checks, not in a set comparison.

## 3. Receipts (commands, output, 2026-10-17)

All commands ran in scratch mirrors carrying byte copies of the live artifacts (`examples/culture-d2/packet.d2.yml` `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`; `examples/culture-d2/typed-labels.d2.yml` `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f`), under `TMPDIR=$PWD/.scratch`. Mirrors: `.scratch/D03/repo4` (receipts), `.scratch/D03/verify/repo` (the code extracted from Appendix A). Scripts: `.scratch/D03/receipts.sh`; transcripts `.scratch/D03/receipts2/**`.

### 3.1 Selftest — 22/22

```
$ python3 tools/assemble-d2-typed.py --selftest
ok   routing: only off-channel labels get a row (2 of 4)
ok   routing: row keys are the design's
ok   routing: gloss field is *_gloss
ok   rewrite: checked field moved, gloss kept
ok   rewrite: no other record touched
ok   R5: declared sound kind without bytes is routed and held
ok   T1 row 5: a record with no asserted kind is routed off-channel, held to-verify with its detail
ok   coverage: missing record refused
ok   coverage: no field to route refused
ok   coverage: double route refused
ok   stale committed projection refused with exit 2
ok   fixture projection re-emitted by the projector
ok   positive: CLI exit 0 over fresh artifacts
ok   positive: noted routing rows written
ok   positive: typed packet non-empty
ok   --check PATH exit 0 on the fresh build
ok   --check (no path) exit 0, two builds byte-identical
ok   --check: a changed byte is exit 1
ok   assembler identity: a tampered packet is exit 2
ok   typed packet: exactly the ten off-channel records are routed
ok   typed packet: 15 holds + 1 note carried
ok   typed packet: three pins recorded
selftest: 22/22 checks passed
```

The selftest builds its own fixture tree in one temporary directory (mirror of `tools/` + `examples/culture-d2/components` + packet), re-emits a projection there, then drives the same CLI over it. It touches no file outside that directory, and it is green whether or not the committed projection has been re-pinned (the stale-pin case is one of its controls).

### 3.2 The committed projection is refused until re-pinned (design §2.2, §5.1)

```
$ python3 tools/assemble-d2-typed.py --emit out/never.yml            # committed projection
stale_pin_exit=2
stderr: typed-assembly error: stale projection pin: …/typed-labels.d2.yml records 8da90b0788f86fd19babc67958715c8c16cb90a98…

$ python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.r11.yml \
      --packet examples/culture-d2/packet.d2.yml
Wrote examples/culture-d2/typed-labels.r11.yml                          # pipeline exit 1 (holds), file written
$ sha256sum examples/culture-d2/typed-labels.r11.yml
a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43
$ python3 tools/d2-typed-labels.py --check examples/culture-d2/typed-labels.r11.yml \
      --packet examples/culture-d2/packet.d2.yml
examples/culture-d2/typed-labels.r11.yml: byte-identical deterministic projection   # exit 0
```

The re-pinned bytes hash **exactly** the value design §5.1 predicted (`a3aa452c…`, 3010 lines): the prediction is reproduced by an independent run, in a different directory, from the same inputs. Two notes for the integrator: (i) the projector's `--emit` exits 1 because the projection carries holds — that is its pipeline verdict, not an emit failure, and the freshness the adapter checks is the `--check` leg; (ii) the adapter needs a re-pinned projection passed as `--projection` (or moved into place per §5.1/D07) — it never re-pins by itself, deliberately, so a re-pin cannot be blessed silently.

### 3.3 Typed assembly, determinism, pins

```
$ python3 tools/assemble-d2-typed.py --packet examples/culture-d2/packet.d2.yml \
      --projection examples/culture-d2/typed-labels.r11.yml --emit out/packet.d2.typed.yml
Wrote out/packet.d2.typed.yml (163522 bytes, 10 routing rows, 16 findings carried)    # exit 0
$ sha256sum out/packet.d2.typed.yml
7782485b3a75756e10ef4f8ba367752b77c7561ee46fbea697aaf7ffb691bfd3
$ python3 tools/assemble-d2-typed.py … --check out/packet.d2.typed.yml
out/packet.d2.typed.yml: byte-identical deterministic typed assembly                  # exit 0
$ python3 tools/assemble-d2-typed.py … --check
two consecutive builds are byte-identical (163522 bytes, 10 routing rows)             # exit 0
```

Embedded pins read back from the emitted packet (`assembly`): `packet_sha256 e0f21509…`, `projection_sha256 a3aa452c…`, `adapter_sha256 95ac9d05…` — the three §3.1 L4 values, each equal to the bytes on disk. The document also carries `typed_channel_rows: 10` and the projection's `findings` verbatim (16 objects: 15 holds, 1 note, 0 fails). Note the self-referential pin: editing the adapter changes `adapter_sha256` and therefore the emitted packet's bytes, so any adapter edit re-pins the freeze row (§5.2) — by design, but worth knowing before an edit is waved through.

### 3.4 Structural invariants of the emitted packet

```
routing rows      : 10    (all owner 11-costumes, source_field garment, off_channel_field garment_gloss,
                           channel off-sound-and-identity, hold D2L-FORM-UNRESOLVED, kind translated-label)
sound strings     : 48    | with a space: 0      # no English gloss survives on a checked slot
holds carried     : 15  [GAR-01..10, L-15, L-16, TR-04#a|TR-06#a, WR-02#g|WR-09#g, WR-08#g|WR-09#g]
notes carried     : 1   [SR-01#a|SR-01#b]
fails carried     : 0
invariant failures: none
```

The invariant run compares every costume record field-by-field against the legacy packet: the only difference per `GAR-0x` is `garment` removed and `garment_gloss` added; the `lexicon` and `names` blocks compare equal to the legacy ones. This matters because the channel differential must be *only* the routing, with no incidental rewrite.

### 3.5 Channel differential — and the design's own hashes reproduced

```
$ python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml   # legacy, exit 1
legacy lines=17  PHON-INVENTORY=10  GAR-named=10
  stdout sha256 ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b
$ python3 tools/gates/naming-collision-gate.py out/packet.d2.typed.yml            # typed, exit 1
typed  lines=7   PHON-INVENTORY=0
  stdout sha256 feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9
diff: removed lines 10, added lines 0
```

Both stdout hashes equal the values design §1.1/§1.3 measured in its own scratch run — the adapter reproduces the design's channel measurement byte-for-byte, from a separately built typed packet. The ten removed lines are exactly the ten `PHON-INVENTORY` FAILs naming `GAR-01..GAR-10`; nothing was added, so no cascade and no lost finding.

The four remaining gates are byte-identical between the legacy and typed runs, as §1.3 claimed:

```
phonology-sanity-gate        : legacy_exit=1 typed_exit=1 findings=3 654 bytes identical
                               (legacy stdout sha256 1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2 = design §1.3's value)
lexicon-coverage-audit       : legacy_exit=0 typed_exit=0 findings=0 0 bytes identical
myth-consistency-gate        : legacy_exit=0 typed_exit=0 findings=0 0 bytes identical
costume-era-consistency-gate : legacy_exit=0 typed_exit=0 findings=0 0 bytes identical
```

### 3.6 Fail-closed controls (CLI level)

| control | injection | observed |
|---|---|---|
| stale projection pin | committed projection passed as `--projection` | exit 2, `stale projection pin: … records 8da90b07… but … hashes e0f21509…` |
| hand-edited projection | one label's `kind`/`status`/`text` flipped in a copy | exit 2, `is not reproduced byte-for-byte by tools/d2-typed-labels.py` |
| malformed projection shape | `typed_labels.labels` replaced by a string list | exit 2, same byte-reproduction refusal, no traceback |
| non-assembly packet | one byte appended, or a malformed YAML-subset packet | exit 2, `is not assemble-d2.py's deterministic assembly …` |
| typed packet drift | `# tamper` appended to the emitted packet, then `--check …` | exit 1 |
| missing projection file | `--projection` pointing at nothing | exit 2, `no projection at …` |

### 3.7 Post-re-pin live bytes (mirror 5, read from the repository)

By the time this shard closed, a sibling seat (D07, design §5.1) had moved the re-pinned projection into the repository: `examples/culture-d2/typed-labels.d2.yml` now hashes `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` — **the same bytes this shard's independent re-pin produced** — and `python3 tools/d2-typed-labels.py --check` exits 0 over the live tree. Running the delivered adapter against copies of exactly those live bytes (mirror `.scratch/D03/repo5`, tool sha `95ac9d05…`, projector sha `0da0015f…` equal to the repository's, projection bytes `a3aa452c…`):

```
$ python3 tools/assemble-d2-typed.py --emit out/packet.d2.typed.yml
Wrote out/packet.d2.typed.yml (163521 bytes, 10 routing rows, 16 findings carried)   # exit 0
$ sha256sum out/packet.d2.typed.yml
bb480e34881c87814f953560ab769aa8705316be64fead67abe1b454bc0ec3b3
$ python3 tools/assemble-d2-typed.py --check out/packet.d2.typed.yml
out/packet.d2.typed.yml: byte-identical deterministic typed assembly                  # exit 0
routing rows: 10 | holds: 15
```

(The byte count moves to 163521 because the embedded projection path is `typed-labels.d2.yml` instead of the scratch `typed-labels.r11.yml`.) One sharp edge worth recording for the test shards: the freshness check is **root-anchored** — the projector embeds repo-relative paths (§2.2's `assembly.packet`), so pointing the adapter's `--packet/--projection` at another tree's files while the tool itself lives elsewhere legitimately refuses with exit 2; mirror the whole tree (as every receipt here and in `depth/test-*.md` does) rather than reaching across trees.

## 4. Interface notes for the sibling shards

1. **Top-level blocks of the emitted packet.** The packet's own blocks (existing order), then `typed_channel` (list of routing rows, the design's eight keys in the design's order), then `typed_channel_rows` (int), then `findings` (the projection's finding objects verbatim, projector order), then `assembly`. `findings` is this shard's proposed key for §3.1 L3's "projector findings carried in the typed packet" — the design names the requirement, not the key; if D05 lands a different name, one line in `build()` `:211` changes and everything else holds.
2. **`assembly` is extended, not replaced.** The emitted packet's `assembly` is the assembler's own block (generator/reader/source digests/normalizations/unresolved) **plus** `adapter`, `adapter_sha256`, `packet`, `packet_sha256`, `projection`, `projection_sha256`, `projection_pins` (the projection's assembly block verbatim), `typed_channel_contract`, `typed_channel_rows`. Design §2.2 sketches `assembly` with the three pins; extending keeps §3.1 L4 readable at exactly `assembly.packet_sha256` / `projection_sha256` / `adapter_sha256` while the assembler's provenance pins survive. If D05/D08 prefer a standalone pin block, the swap is confined to `build()` `:229-241`.
3. **Row schema.** `record, kind, label_id, owner, source_field, off_channel_field, channel, hold` — plus `detail` **only** in the design's T1-row-5 case (no asserted kind), where `kind: null` and `hold: to-verify` with the discriminator named. That case is latent for `examples/culture-d2` today; the adapter implements it rather than defaulting a kind it does not have.
4. **Round-10 N2 (design §8.3).** The projector is silent for `native-form, status: to-verify` with no bytes (`depth/test-boundary.md` F7 measured the silence). This adapter does not wait for the projector: `off_channel_labels()` `:136` routes that class off-channel and names `D2L-FORM-UNRESOLVED` itself, which is the design's required behaviour ("the adapter must inject the hold itself"). The deviation belongs to the projector and is reported here as an open item, **not** patched into the typed packet's `findings` (those stay the projector's verbatim output, so L3's set comparison is not silently shifted).
5. **Boundary behaviour.** The gate reader in `tools/gates/costume-era-consistency-gate.py:376` defines `Malformed(Exception)` — not a `ValueError` — so `parse_packet()` `:82` wraps it into the adapter's own error type; `main()` `:435` catches the named error classes and returns exit 2 with one diagnostic line. `depth/test-boundary.md` §6's "exit 2 with a named diagnostic, no traceback" therefore holds for this subject.
6. **The wire has no other entry point.** The adapter never re-pins, never rewrites the legacy packet, never writes under `examples/` unless `--emit` names a path there, and never edits a gate; the five gate scripts see nothing but a different packet path.

## 5. Limits, to-verify, out-of-province

1. **to-verify — landing.** `tools/assemble-d2-typed.py` does not exist in the repository from this seat; D05 lands the fragment (sha `95ac9d05…`). Nothing here is a repository capability until that copy exists and its selftest runs from `tools/`.
2. **to-verify — re-pin.** The receipts run against a scratch re-pin (`a3aa452c…`). D07's procedure (design §5.1) moves those bytes into `examples/culture-d2/typed-labels.d2.yml`; until then the default `--projection` legitimately exits 2. This fragment's re-pin run corroborates the design's predicted hash, which D07's receipt needs.
3. **Boundary of the argument.** The adapter proves *routing*: the ten glosses are off the checked channel and ten holds are named. It does not prove the holds are *correct design* (they are the projector's typing, which this seat did not re-derive independently of `tools/d2-typed-labels.py`), and it decides no canon. The wiring-vs-spec and hold-set-completeness attacks are D20/D21's.
4. **Not covered here (sibling shards, by design).** The gate (`tools/gates/typed-pipeline-gate.py`, D05), the committed `expected-holds.json` (D06), the freeze row (D08), the test receipts (D09–D16) and the three negative controls (D17–D19).
5. **Out of province (report, never absorb).** Whether the ten owed garment forms should ever be coined, and whether an English gloss may serve as an in-world name, are lore-shokunin questions. This fragment asserts nothing about any real language and makes no canon claim.
6. **Concurrency.** Sibling seats were writing `tools/` and `reports/round-11/` throughout; every pin above is a read at the stated time, and any later mismatch is a re-read event, not a licence to compare across revisions.

## 6. Adjacent observation, reported not absorbed — a second routing shape landed

While this shard was finishing (2026-10-17T19:12–19:13 local, after the receipts above), a sibling seat landed a **different** implementation of the same wiring:

- `tools/typed-gate-flow.py` (36305 bytes, 19:12) and `examples/culture-d2/packet.d2.typed.yml` (158129 bytes, sha256 `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb`, 19:13). `grep -n "typed_channel\|garment_gloss\|off-sound-and-identity\|assemble-d2-typed\|adapter_sha256" tools/typed-gate-flow.py` → **no match**: it has no `assemble-d2-typed.py` consumption at all.
- Its shape, read from the landed packet: each `GAR-0x` record keeps the English gloss **in `garment`**, gains `compare_only: true`, `typed_label_kind: translated-label` and `owed_form: LEX-GAR-0x`; the routing table is a top-level `typed_view` block (`typed_view.sound_channel.off = GAR-01..GAR-10`, `rule: "off = translated-label records (compare_only); …"`). The gloss is removed from the phonotest by the gate's own `compare_only` skip (`tools/gates/naming-collision-gate.py:1152-1153`).
- Design §2.2/§2.3 and the design's own §1.3 experiment prescribe the other shape: the checked field **moved** to `*_gloss` with `typed_channel` rows and `channel: off-sound-and-identity` — what this fragment implements. And round-8 design-spec R3 is explicit that the landed shape's mechanism is not licensed: "`compare_only` is therefore **not** a licensed exemption channel for typed labels; a record setting it while unresolved is `D2L-SCOPE` (misuse), not a pass" (`reports/round-8/depth/design-spec.md:155-160`).
- Both shapes remove the ten `PHON-INVENTORY` lines, so the L2 differential cannot separate them. The design's own negative control D17 ("typed packet where a routing record's gloss is left in its checked field") describes exactly the field-level appearance of the landed packet; under §2.2's shape the detector has teeth, under the landed shape only the self-declared `compare_only` flag separates it from the injected fault.

This seat changed nothing in the sibling's files and takes no position on which shape the round adopts — but the collision is on the D claim's critical path (two mechanisms now claim "the typed packet"), the round's reviewers (D20 wiring-vs-spec, D22 circularity) should rule on it with both artifacts in hand, and the acceptance runner `reports/round-11/run-validation.py` (read 19:1xZ) currently keys its depth legs on `assemble-d2.py --check` / `d2-typed-labels.py --check` and on JSON e2e receipts, not on either routing shape by name. An integration that lands this fragment's adapter *beside* the landed flow would produce two typed packets with different bytes for the same claim; one of the two must be the round's answer.

## Appendix A — the delivered source, verbatim

`.scratch/D03/assemble-d2-typed.py`, sha256 `95ac9d05ff880234e4fafa33de3cac09db2fee248c760c61fa2dda7631318215`, 455 lines. Extracting this fenced block and hashing it reproduces that sha (verified 2026-10-17T22:2xZ), and the extracted copy's `--selftest` is the 22/22 run above (mirror `.scratch/D03/verify/repo`).


```python
#!/usr/bin/env python3
"""Assemble the typed gate-facing D2 packet from the packet and the typed-label
projection (round-11 claim D, design: reports/round-11/depth/design.md §2.2).

    python3 tools/assemble-d2-typed.py [--packet P] [--projection J]
                                       [--emit PATH] [--check [PATH]] [--selftest]

Reads only; writes only the path given to --emit.  Fail-closed rules (§2.2):

  * assembler identity: --packet bytes equal assemble-d2.py's deterministic
    assembly (the assembler's own build path is called, never re-implemented);
  * projection freshness: the projection's assembly.packet_sha256 equals the
    sha256 of --packet bytes AND d2-typed-labels.py reproduces the projection
    byte-for-byte; a stale pin is a hard error, never a warning;
  * coverage: every label the projector types as off-channel has exactly one
    routing row, every routed record exists in the packet, and no row names a
    record the projector did not type.

Output: the packet's blocks plus `typed_channel` (one row per off-channel
record), the projector's `findings` carried verbatim, and `assembly` extended
with the three pins (packet/projection/adapter) plus the projection's own
assembly block verbatim under `projection_pins`.

Exit codes: 0 ok · 1 --check byte mismatch · 2 could-not-evaluate.
"""

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
PACKET = ROOT / "examples/culture-d2/packet.d2.yml"
PROJECTION = ROOT / "examples/culture-d2/typed-labels.d2.yml"
ASSEMBLER = ROOT / "tools/assemble-d2.py"
PROJECTOR = ROOT / "tools/d2-typed-labels.py"
READER = ROOT / "tools/gates/costume-era-consistency-gate.py"

CONTRACT = "kotodama-typed-channel/1"
SOUND_KINDS = ("native-form", "borrowed-strata")
OFF_CHANNEL = "off-sound-and-identity"
ABSENT_STATUSES = ("absent", "to-verify")

# owner component -> (packet section, the field the gate used to check)
OWNER_SECTIONS = {
    "11-costumes": ("costumes", "garment"),
    "05-lexicon": ("lexicon", "term"),
    "13-naming": ("names", "name"),
}
ROW_KEYS = ("record", "kind", "label_id", "owner", "source_field",
            "off_channel_field", "channel", "hold")


class TypedAssemblyError(ValueError):
    """Could-not-evaluate; main() maps this to exit 2."""


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def shown(path):
    try:
        return str(Path(path).relative_to(ROOT))
    except ValueError:
        return str(path)


def assembler_build():
    """The assembler's own deterministic bytes (its `assemble` entry point)."""
    namespace = runpy.run_path(str(ASSEMBLER))
    return namespace["assemble"]()


def parse_packet(text):
    namespace = runpy.run_path(str(READER))
    try:
        return namespace["parse_packet"](text)
    except namespace["Malformed"] as exc:
        raise TypedAssemblyError(
            "packet is not readable by the gate's YAML subset: %s" % exc) from exc


def projector_run(packet_path):
    """(findings-bearing projection, canonical bytes) from the projector."""
    namespace = runpy.run_path(str(PROJECTOR))
    result = namespace["run_pipeline"](Path(packet_path))
    if result["projection"] is None:
        raise TypedAssemblyError(
            "projector could not evaluate %s: %s" % (packet_path, result["findings"][:1]))
    return result["projection"], namespace["serialize"](result["projection"])


def check_assembler_identity(packet_path, packet_bytes):
    built = assembler_build()
    if packet_bytes != built:
        raise TypedAssemblyError(
            "%s is not assemble-d2.py's deterministic assembly "
            "(%d bytes vs %d); re-run tools/assemble-d2.py before wiring"
            % (packet_path, len(packet_bytes), len(built)))


def check_projection_freshness(projection_path, packet_path, packet_bytes):
    raw = Path(projection_path).read_bytes()
    try:
        projection = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise TypedAssemblyError("projection %s is not readable JSON: %s"
                                 % (projection_path, exc)) from exc
    if not isinstance(projection, dict) or "typed_labels" not in projection:
        raise TypedAssemblyError("projection %s carries no typed_labels block"
                                 % projection_path)
    pinned = (projection.get("assembly") or {}).get("packet_sha256")
    actual = hashlib.sha256(packet_bytes).hexdigest()
    if pinned != actual:
        raise TypedAssemblyError(
            "stale projection pin: %s records %s but %s hashes %s; re-emit with "
            "python3 tools/d2-typed-labels.py --emit (design §5.1)"
            % (projection_path, pinned, packet_path, actual))
    fresh, fresh_bytes = projector_run(packet_path)
    if fresh_bytes != raw:
        raise TypedAssemblyError(
            "projection %s is not reproduced byte-for-byte by "
            "tools/d2-typed-labels.py over %s; hand-edited or drifted"
            % (projection_path, packet_path))
    return projection


def off_channel_labels(projection):
    """The labels the routing table must carry, in projector order."""
    rows = []
    for label in projection["typed_labels"]["labels"]:
        if label["kind"] is None or label["kind"] == "translated-label":
            rows.append(label)
        elif label["kind"] in SOUND_KINDS and label.get("status") in ABSENT_STATUSES:
            rows.append(label)
    return rows


def source_field(label):
    owner = label["owner"]
    if owner not in OWNER_SECTIONS:
        raise TypedAssemblyError(
            "label %s/%s names an owner component with no declared section"
            % (owner, label["id"]))
    section, field = OWNER_SECTIONS[owner]
    declared = (label.get("source") or {}).get("field")
    if declared and declared != field:
        raise TypedAssemblyError(
            "label %s/%s declares source field %r but owner %s is checked on %r"
            % (owner, label["id"], declared, owner, field))
    return section, field


def routing_rows(packet, projection):
    """One row per off-channel record; coverage violations are exit-2 errors."""
    rows = []
    typed = set()
    for label in off_channel_labels(projection):
        section, field = source_field(label)
        record = next((item for item in packet.get(section) or []
                       if isinstance(item, dict) and item.get("id") == label["id"]), None)
        if record is None:
            raise TypedAssemblyError(
                "routing row names record %s/%s the packet does not carry"
                % (label["owner"], label["id"]))
        if (label["owner"], label["id"]) in typed:
            raise TypedAssemblyError(
                "record %s/%s is routed twice" % (label["owner"], label["id"]))
        typed.add((label["owner"], label["id"]))
        row = {"record": label["id"], "kind": label["kind"],
               "label_id": label.get("label_id"), "owner": label["owner"],
               "source_field": field, "off_channel_field": "%s_gloss" % field,
               "channel": OFF_CHANNEL, "hold": "D2L-FORM-UNRESOLVED"}
        if label["kind"] is None:                       # T1 row 5, latent for D2
            row["kind"] = None
            row["hold"] = "to-verify"
            row["detail"] = ("kind not asserted: %s"
                             % (label.get("issues") or "discriminator not named"))
        rows.append(row)
        if field not in record:
            raise TypedAssemblyError(
                "record %s/%s carries no %s field to route off-channel"
                % (label["owner"], label["id"], field))
    return rows


def apply_rows(packet, rows):
    """Move each routed checked field to its `*_gloss` neighbour, nothing else."""
    typed = copy.deepcopy(packet)
    for row in rows:
        section = OWNER_SECTIONS[row["owner"]][0]
        for record in typed.get(section) or []:
            if isinstance(record, dict) and record.get("id") == row["record"]:
                record[row["off_channel_field"]] = record.pop(row["source_field"])
                break
        else:
            raise TypedAssemblyError("routing row %s/%s lost its record between "
                                     "coverage check and rewrite"
                                     % (row["owner"], row["record"]))
    return typed


def build(packet_path=PACKET, projection_path=PROJECTION):
    packet_path = Path(packet_path)
    projection_path = Path(projection_path)
    if not packet_path.exists():
        raise TypedAssemblyError("no packet at %s" % packet_path)
    if not projection_path.exists():
        raise TypedAssemblyError("no projection at %s" % projection_path)
    packet_bytes = packet_path.read_bytes()
    check_assembler_identity(packet_path, packet_bytes)
    projection = check_projection_freshness(projection_path, packet_path, packet_bytes)
    packet = parse_packet(packet_bytes.decode("utf-8"))
    rows = routing_rows(packet, projection)
    typed = apply_rows(packet, rows)
    payload = {key: value for key, value in typed.items() if key != "assembly"}
    payload["typed_channel"] = [dict(row) for row in rows]
    payload["typed_channel_rows"] = len(rows)
    payload["findings"] = [dict(item) for item in projection.get("findings") or []]
    assembly = dict(packet.get("assembly") or {})
    assembly.update({
        "adapter": "tools/assemble-d2-typed.py",
        "adapter_sha256": digest(Path(__file__)),
        "packet": shown(packet_path),
        "packet_sha256": hashlib.sha256(packet_bytes).hexdigest(),
        "projection": shown(projection_path),
        "projection_sha256": digest(projection_path),
        "projection_pins": projection.get("assembly") or {},
        "typed_channel_contract": CONTRACT,
        "typed_channel_rows": len(rows),
    })
    payload["assembly"] = assembly
    return payload, rows


def dump(document):
    namespace = runpy.run_path(str(ASSEMBLER))
    return ("\n".join(namespace["yaml_lines"](document)) + "\n").encode("utf-8")


def emit(packet_path=PACKET, projection_path=PROJECTION, target=None, check=None):
    """Build once; write, compare, or report. Returns an exit code."""
    document, rows = build(packet_path, projection_path)
    payload = dump(document)
    if check is not None:
        if check is True:
            second, _ = build(packet_path, projection_path)
            if dump(second) != payload:
                print("two consecutive builds differ; the adapter is nondeterministic",
                      file=sys.stderr)
                return 1
            print("two consecutive builds are byte-identical (%d bytes, %d routing rows)"
                  % (len(payload), len(rows)))
            return 0
        target_path = Path(check)
        if not target_path.exists() or target_path.read_bytes() != payload:
            print("%s differs from the deterministic typed assembly" % target_path,
                  file=sys.stderr)
            return 1
        print("%s: byte-identical deterministic typed assembly" % target_path)
        return 0
    if target:
        Path(target).parent.mkdir(parents=True, exist_ok=True)
        Path(target).write_bytes(payload)
        print("Wrote %s (%d bytes, %d routing rows, %d findings carried)"
              % (target, len(payload), len(rows), len(document["findings"])))
        return 0
    print("typed assembly: %d bytes, %d routing rows, %d findings carried"
          % (len(payload), len(rows), len(document["findings"])))
    return 0


# --------------------------------------------------------------------------
# selftest — fixture controls in one temporary directory
# --------------------------------------------------------------------------

def selftest():
    passed, failed = [], []

    def check(label, condition, detail=""):
        (passed if condition else failed).append(label)
        print("%s %s%s" % ("ok  " if condition else "FAIL", label,
                           "" if condition else " — %s" % detail))

    probe_packet = {
        "costumes": [{"id": "GAR-01", "garment": "winter coat", "era": "E0"},
                     {"id": "GAR-02", "garment": "summer coat", "era": "E0"}],
        "lexicon": [{"id": "L-01", "term": "su", "layer": "native"}],
        "names": [{"id": "NM-01", "name": "sunel"}],
    }

    def probe(labels):
        return {"typed_labels": {"labels": labels}, "findings": [],
                "assembly": {"packet_sha256": "0" * 64}}

    def label(rid, owner, kind, status, **extra):
        base = {"id": rid, "owner": owner, "kind": kind, "status": status,
                "label_id": None, "source": {"field": None}, "issues": []}
        base.update(extra)
        return base

    rows = routing_rows(probe_packet, probe([
        label("GAR-01", "11-costumes", "translated-label", "to-verify"),
        label("GAR-02", "11-costumes", "translated-label", "to-verify",
              label_id="LEX-GAR-02"),
        label("L-01", "05-lexicon", "native-form", "supplied", text="su"),
        label("NM-01", "13-naming", "borrowed-strata", "supplied", text="sunel"),
    ]))
    check("routing: only off-channel labels get a row (2 of 4)", len(rows) == 2, rows)
    check("routing: row keys are the design's",
          set(rows[0]) == set(ROW_KEYS), sorted(rows[0]))
    check("routing: gloss field is *_gloss",
          rows[0]["off_channel_field"] == "garment_gloss"
          and rows[1]["label_id"] == "LEX-GAR-02", rows)
    typed = apply_rows(probe_packet, rows)
    check("rewrite: checked field moved, gloss kept",
          typed["costumes"][0].get("garment") is None
          and typed["costumes"][0]["garment_gloss"] == "winter coat"
          and typed["lexicon"][0]["term"] == "su", typed["costumes"][0])
    check("rewrite: no other record touched",
          typed["lexicon"][0] == probe_packet["lexicon"][0], typed["lexicon"][0])
    held = routing_rows(probe_packet, probe([
        label("L-01", "05-lexicon", "native-form", "to-verify")]))
    check("R5: declared sound kind without bytes is routed and held",
          held[0]["hold"] == "D2L-FORM-UNRESOLVED"
          and held[0]["off_channel_field"] == "term_gloss", held)
    unasserted = routing_rows(probe_packet, probe([
        label("GAR-01", "11-costumes", None, "to-verify",
              issues=[{"field": "kind", "reason": "exactly 1 discriminator holds: D2"}])]))
    check("T1 row 5: a record with no asserted kind is routed off-channel, "
          "held to-verify with its detail",
          unasserted[0]["kind"] is None and unasserted[0]["hold"] == "to-verify"
          and "D2" in unasserted[0]["detail"], unasserted)
    for raiser, why in (
        (lambda: routing_rows(probe_packet, probe([
            label("GAR-09", "11-costumes", "translated-label", "to-verify")])), "missing record"),
        (lambda: routing_rows({"lexicon": [{"id": "L-01", "layer": "native"}]}, probe([
            label("L-01", "05-lexicon", "translated-label", "to-verify")])), "no field to route"),
        (lambda: routing_rows(probe_packet, probe([
            label("GAR-01", "11-costumes", "translated-label", "to-verify"),
            label("GAR-01", "11-costumes", "translated-label", "to-verify")])), "double route"),
    ):
        try:
            raiser()
            check("coverage: %s refused" % why, False, "no error raised")
        except TypedAssemblyError as exc:
            check("coverage: %s refused" % why, True, str(exc))

    with tempfile.TemporaryDirectory(prefix="assemble-d2-typed-selftest-") as tmpdir:
        mirror = Path(tmpdir) / "repo"
        for rel in ("tools/gates", "examples/culture-d2/components"):
            (mirror / rel).mkdir(parents=True)
        shutil.copyfile(Path(__file__).resolve(), mirror / "tools/assemble-d2-typed.py")
        for name in ("assemble-d2.py", "d2-typed-labels.py"):
            shutil.copyfile(ROOT / "tools" / name, mirror / "tools" / name)
        shutil.copyfile(READER, mirror / "tools/gates/costume-era-consistency-gate.py")
        shutil.copyfile(PACKET, mirror / "examples/culture-d2/packet.d2.yml")
        for src in sorted((ROOT / "examples/culture-d2/components").glob("*.yml")):
            shutil.copyfile(src, mirror / "examples/culture-d2/components" / src.name)
        tool = mirror / "tools/assemble-d2-typed.py"
        packet = mirror / "examples/culture-d2/packet.d2.yml"
        projector = mirror / "tools/d2-typed-labels.py"
        repinned = mirror / "examples/culture-d2/typed-labels.r11.yml"
        emitted = mirror / "out/packet.d2.typed.yml"

        def run(script, *args):
            return subprocess.run([sys.executable, str(script), *args],
                                  capture_output=True, text=True, cwd=str(mirror))

        stale = run(tool, "--packet", str(packet),
                    "--projection", str(ROOT / PROJECTION), "--emit", str(emitted))
        check("stale committed projection refused with exit 2",
              stale.returncode == 2 and "stale projection pin" in stale.stderr,
              "exit %s: %s" % (stale.returncode, stale.stderr.strip()))

        emitted_projection = run(projector, "--emit", str(repinned), "--packet", str(packet))
        check("fixture projection re-emitted by the projector",
              repinned.exists() and emitted_projection.returncode in (0, 1),
              emitted_projection.stderr.strip()[:160])
        first = run(tool, "--packet", str(packet), "--projection", str(repinned),
                    "--emit", str(emitted))
        check("positive: CLI exit 0 over fresh artifacts", first.returncode == 0,
              "exit %s: %s" % (first.returncode, first.stderr.strip()))
        check("positive: noted routing rows written",
              "10 routing rows" in first.stdout, first.stdout.strip())
        payload = emitted.read_bytes() if emitted.exists() else b""
        check("positive: typed packet non-empty", bool(payload))
        clean = run(tool, "--packet", str(packet), "--projection", str(repinned),
                    "--check", str(emitted))
        check("--check PATH exit 0 on the fresh build", clean.returncode == 0,
              clean.stderr.strip())
        twice = run(tool, "--packet", str(packet), "--projection", str(repinned), "--check")
        check("--check (no path) exit 0, two builds byte-identical", twice.returncode == 0,
              twice.stderr.strip())
        emitted.write_bytes(payload + b"# tamper\n")
        drift = run(tool, "--packet", str(packet), "--projection", str(repinned),
                    "--check", str(emitted))
        check("--check: a changed byte is exit 1", drift.returncode == 1,
              "exit %s" % drift.returncode)
        packet.write_bytes(packet.read_bytes() + b"# tamper\n")
        broken = run(tool, "--packet", str(packet), "--projection", str(repinned))
        check("assembler identity: a tampered packet is exit 2",
              broken.returncode == 2 and "not assemble-d2.py's deterministic assembly"
              in broken.stderr, "exit %s: %s" % (broken.returncode, broken.stderr.strip()))
        tree = parse_packet(payload.decode("utf-8")) if payload else {}
        rows_out = tree.get("typed_channel") or []
        check("typed packet: exactly the ten off-channel records are routed",
              len(rows_out) == 10
              and all(row["off_channel_field"] == "garment_gloss" for row in rows_out)
              and all(row["owner"] == "11-costumes" for row in rows_out), rows_out[:2])
        findings = tree.get("findings") or []
        holds = [f for f in findings if f.get("severity") in ("hold", "reject")]
        notes = [f for f in findings if f.get("severity") == "note"]
        check("typed packet: 15 holds + 1 note carried", (len(holds), len(notes)) == (15, 1),
              (len(holds), len(notes)))
        pins = tree.get("assembly") or {}
        check("typed packet: three pins recorded",
              pins.get("packet_sha256") and pins.get("projection_sha256")
              and pins.get("adapter_sha256"), sorted(pins)[:6])

    total = len(passed) + len(failed)
    print("selftest: %d/%d checks passed%s" % (len(passed), total,
          "" if not failed else " — failures: " + "; ".join(failed)))
    return 0 if not failed else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--packet", default=str(PACKET))
    parser.add_argument("--projection", default=str(PROJECTION))
    parser.add_argument("--emit", metavar="PATH")
    parser.add_argument("--check", nargs="?", const=True, metavar="PATH",
                        help="compare against PATH, or (no PATH) two consecutive builds")
    parser.add_argument("--selftest", "--self-test", action="store_true", dest="selftest")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    try:
        return emit(args.packet, args.projection, target=args.emit, check=args.check)
    except (TypedAssemblyError, ValueError, OSError, KeyError, TypeError,
            IndexError) as exc:
        print("typed-assembly error: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
```

## Receipts

```sh
# 2026-10-17, lane repo, TMPDIR=$PWD/.scratch; scratch mirrors .scratch/D03/{repo4,verify/repo}
export TMPDIR=$PWD/.scratch
sha256sum examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml   # e0f21509…, e70ba147…
bash .scratch/D03/receipts.sh                    # §3.2-§3.6 transcripts -> .scratch/D03/receipts2/
python3 tools/assemble-d2-typed.py --selftest    # 22/22 checks passed (mirror copy of the delivered code)
python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.r11.yml \
    --packet examples/culture-d2/packet.d2.yml
                                                 # a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43 (= design §5.1 prediction)
python3 tools/assemble-d2-typed.py --packet examples/culture-d2/packet.d2.yml \
    --projection examples/culture-d2/typed-labels.r11.yml --emit out/packet.d2.typed.yml
                                                 # exit 0; 163522 bytes; 10 routing rows; 16 findings carried
sha256sum out/packet.d2.typed.yml                # 7782485b3a75756e10ef4f8ba367752b77c7561ee46fbea697aaf7ffb691bfd3
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml       # 17 lines, 10 PHON-INVENTORY, ebc8850d…
python3 tools/gates/naming-collision-gate.py out/packet.d2.typed.yml                 #  7 lines,  0 PHON-INVENTORY, feb64881…
python3 tools/gates/phonology-sanity-gate.py examples/culture-d2/packet.d2.yml       # 3 findings, 1ce5f0cd… (typed run identical)
sha256sum .scratch/D03/assemble-d2-typed.py      # 95ac9d05ff880234e4fafa33de3cac09db2fee248c760c61fa2dda7631318215
```
