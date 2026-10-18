# R28-D09 — the regeneration and the pin rows

- **Seat:** R28-D09 (D axis, law-replay implementation 5 of 8). Round 28, loop 3
  build 4 of 4, claim **D** `register-law-replay`. Integrator: `impl-1.md`.
- **Date:** 2026-10-18. Baseline `6c0ac448…`; lane HEAD `69cecbc`.
- **Files written:** the three generated D4 artifacts,
  `examples/culture-d4/expected-holds.json`, `tools/gates/typed-pipelines.json`.
- **Write scope:** this file only; scratch under `.scratch/r28-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. The three generated artifacts, rebuilt by the delivered tools

None is hand-edited. Each is produced by the tool that owns it, then verified
`--check` byte-identical:

| # | command | result | exit |
|---|---|---|---|
| V-1 | `python3 tools/assemble-culture-d4.py` then `--check` | `packet.d4.yml: byte-identical deterministic assembly` | 0 |
| V-2 | `python3 tools/d2-typed-labels.py --packet … --emit …` then `--check` | `byte-identical deterministic projection` | 0 |
| V-3 | `python3 tools/assemble-d4-typed.py --emit …` then `--check` | `byte-identical deterministic typed packet` | 0 |

Digests at this tree:

| artifact | sha256 | was |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` | `86079a67…` |
| `examples/culture-d4/typed-labels.d4.yml` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` | `88a94422…` |
| `examples/culture-d4/packet.d4.typed.yml` | `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6` | `1c4b8808…` |

The typed adapter reports `12 routing row(s)` — unchanged, as expected: a law row
is not a form, so no routing row moves.

## 2. The hold set: re-pinned as **new rows**, counts unchanged

`examples/culture-d4/expected-holds.json` — `counts` stay **12 holds / 0 notes /
0 fails**, and the round-27 pins are **moved into `supersedes_pins`, not
overwritten**:

| field | value |
|---|---|
| `packet_sha256` | `543d68a8…` (live) |
| `projection_sha256` | `339bfd83…` (live) |
| `projector_sha256` | `2819f687…` — **unchanged**, the projector did not move |
| `supersedes_pins.r27_packet_sha256` | `86079a67…` (new key) |
| `supersedes_pins.r27_projection_sha256` | `88a94422…` (new key) |
| `supersedes_pins.r27_revision_note` | the round-27 revision-2 note, verbatim (new key) |

The existing `packet_sha256`/`projection_sha256` keys under `supersedes_pins`
keep the **round-26** pins; the new `r27_*` keys carry the round-27 pins. That is
the lane's re-pin convention: **a re-pin is a new row, and no historical
generation is overwritten in place.**

`revision_note` now names the round-28 landing and the RL-4 fix (the round
runner's §7 measures exactly those two clauses and both read true).

## 3. The typed-pipeline profile: a new history row, then the live pins

`tools/gates/typed-pipelines.json` carries the flagless L1-profile pin channel
(`tools/gates/typed-pipeline-gate.py:343-363` re-verifies every pinned field
against the live bytes and refuses a stale pin). Three fields moved:

| field | was | now |
|---|---|---|
| `packet.sha256` | `86079a67…` | `543d68a8…` |
| `projection.sha256` | `88a94422…` | `339bfd83…` |
| `expected.sha256` | `857417e9…` | `65f5a03e…` |

`assembler` and `adapter` did **not** move (both tools are unchanged).

**The round-27 pins were recorded as a NEW `repin_history` row before the live
pins were overwritten** — the file's own note says "No filed receipt is edited by
a re-pin; the pins move in this file and are recorded in the round's fragments".
History is now 7 rows (rounds 20, 22 ×3, 27, 28), and `repin` names this round:

```json
"repin": {"round": 28, "claim": "D (R28-D05..D12 law replay leg + RL-4 packet_keys fix)",
          "date": "2026-10-18",
          "command": "sha256sum examples/culture-d4/packet.d4.yml …",
          "recorded_in": "reports/round-28/law/impl-1.md"}
```

`projection.superseded` and `expected.note` were extended rather than replaced,
so a reader can still trace the round-26/27 generations.

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -3
ok   L3-routing-consistency
ok   L4-pins
summary: 20/20 legs passed
```

Before the re-pin the same command read `FAIL L1-profile` naming all three stale
digests; after it, 20/20.

## 4. What was deliberately NOT re-pinned here

The RL-4 packet change cascades into **filed** surfaces the O seat owns:
`tools/gates/frozen/**` manifests, the `tools/gates/expected/**` battery
baselines, the historical `reports/round-2x/handoff/*/expected.json` rows, and
the round-27 `pinsweep` generations. Two of the classes are this seat's (the hold
set and the profile, above); the rest are the **O claim's sweep**, which owns
re-pinning them as new round-28 rows. This seat did not edit a filed round-8..27
byte, and `git status` over the protected paths is empty (`impl-8.md` §4).

## 5. The frozen-verdict replay, re-verified

The filed manifests pin `gate_sha256` for `tools/gates/typed-pipeline-gate.py`.
That gate did **not** move in this round, so the filed round-26 rows stay GREEN
and the older rows stay DRIFT for reasons that predate this round (the sweep's
own census records them). Measured:

```
tools/gates/frozen/round-26/gate-input/MANIFEST.tsv       gate=b749ad07cf17… GREEN
tools/gates/frozen/round-26/post-register/MANIFEST.tsv    gate=b749ad07cf17… GREEN
```

`b749ad07cf171027…` is the live digest. Had this seat wired the new gate into the
typed pipeline, all six of those rows would have drifted — which is precisely why
the standalone route was taken (`impl-7.md` §2).

## 6. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-culture-d4.py --check
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml
python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
python3 -c "import json;d=json.load(open('examples/culture-d4/expected-holds.json'));print(d['counts']);print([k for k in d['supersedes_pins'] if k.startswith('r27')])"
python3 -c "import json;p=json.load(open('tools/gates/typed-pipelines.json'))['profiles'][0];print(len(p['repin_history']), p['repin'])"
sha256sum examples/culture-d4/{packet.d4.yml,typed-labels.d4.yml,packet.d4.typed.yml,expected-holds.json}
```
