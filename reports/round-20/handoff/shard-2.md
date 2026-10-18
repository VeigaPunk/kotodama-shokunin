# shard-2 — v3 read set, manifest and digest web (R20-D05..D12)

- topic: the v3 read set (58 files), the live-measured manifest, the 25
  component digests and the 8 D4 tree pins. Every figure below was measured in
  the run, not copied.
- date: 2026-10-18.

## 1. Read set (58 files)

- v1's 21 files, in order (so A-01..A-21 keep their v1 meaning), plus:
  - the filed v2 twins `reports/round-15/handoff/packet-v2-05.{md,yml}`
    (subset-equality source and digest pins);
  - the four D2 component inputs the D2 projector's selftest fixture copies
    (`examples/culture-d2/components/{05-lexicon,09-eras-calendar,11-costumes,
    12-rank-rules}.yml`) — the D2 byte-identity control's inputs;
  - the D4 tree: `packet.d4.yml`, `packet.d4.typed.yml`,
    `typed-labels.d4.yml`, `expected-holds.json`, `brief.md`, `ASSEMBLY.md`,
    the twelve components;
  - the two D4 tools (`assemble-culture-d4.py`, `assemble-d4-typed.py`), the
    two D4 adapter gates, the D4 reader gate;
  - the four round-18 D4 receipts (`holds.md`, `determinism.md`, `manifest.md`,
    `replay.md`);
  - the two round-15 harness validators;
  - `reports/round-20/handoff/claims-map.md` (the twelve D4 rows' copy
    surface) and `reports/round-19/validation.json` (a D4-CL08 link target).

## 2. Digest web (measured in the freeze run)

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-20/handoff
```

- component digests: **25/25 matched** (D2 9, D3 4, D4 12) — each re-measured
  against the assemblers' own `assembly.source_sha256` manifests.
- D4 tree pins: **8/8 matched** — `packet.d4.yml` assembler/reader/serializer,
  `typed-labels.d4.yml` packet/reader, `expected-holds.json`
  packet/projection/projector.
- manifest equality: every `§artifact_manifest` row's digest equals the sha256
  of the file it names, measured in the same run (58 files + the inline
  A-GLOSS row).
- D4 read-only counts carried into the packet: 54 lexicon / 8 names /
  8 symbols / 6 costumes / 4 rank rules / 8 era records (4 tags) / 2 contact
  layers / 9 provenance rows; typed channel 74 labels (56 native-form /
  12 translated-label / 6 borrowed-strata), 16 findings, 15 hold-or-fail,
  13 unresolved rank items, 3 quarantine handles; hold set 15 holds / 1 note /
  0 fails.

## 3. D4 legs run by the exercise (observed, same run)

- `tools/assemble-culture-d4.py --check` → exit 0, `packet.d4.yml:
  byte-identical deterministic assembly`.
- `tools/assemble-d4-typed.py --check` → exit 0, `examples/culture-d4/
  packet.d4.typed.yml: byte-identical deterministic typed packet`.
- `tools/d2-typed-labels.py --selftest` → exit 0, `50/50 checks passed`.
- `tools/assemble-d4-typed.py --selftest` → exit 0, `12/12 checks passed`
  (the mirror copies only `examples/culture-d4` — the D4-CL08 witness).

Not asserted by this exercise: the two D4 adapter gates (pinned read-only;
the O seat's receipt surface) and the battery.
