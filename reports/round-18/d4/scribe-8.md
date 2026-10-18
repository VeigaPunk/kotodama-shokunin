# R18-D28 — spot-check ledger: independent re-derivations (round 18)

- round: 18 (operator loop 2 of 3, build round 2 of 4) · seat **R18-D28**
  (spot-check ledger) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D21..D28 (scribes+docs x8): frozen-manifest
  records; fragment ledger; capability drafts; ASSEMBLY.md/README updates for
  culture-d4 (new files only); docs; run logs; disposition drafts; spot-check
  ledger. reports/round-18/d4/scribe-{1..8}.md."
- date: 2026-10-18 · reference revision `c66ac3c951b346a2a56f9386e3324b4f5fe33902`
  · readings 10:19–10:31Z · `export TMPDIR=$PWD/.scratch` for every probe.
- canon: NON-CANON. A spot-check re-derives a reading from bytes; it endorses
  no verdict. A reproduced red stays red; a green says "as recorded".
- writes: **this file only** + `.scratch/r18d21/`. No commit, no push.

## 0. What "spot-check" means here

For each load-bearing claim of the round-18 D/O boundary, this seat re-measured
the underlying bytes rather than re-reading a sibling's number. Where a reading
exists only in another fragment, the row says **cited** and names it. Marks:
⟦IC⟧ = independently checked here, command given.

## 1. Ledger

| # | checked claim | command | reading | verdict |
|---|---|---|---|---|
| SP-1 | the default D2 gate path is green and unchanged | `python3 tools/gates/typed-pipeline-gate.py`; `--json` | exit 0, `16/16 legs passed`, 15 FINDING + 1 NOTE; JSON has 16 checks, `counts` present | ⟦IC⟧ GREEN (10:20Z) |
| SP-2 | the gate selftest's control matrix runs | `python3 tools/gates/typed-pipeline-gate.py --selftest` | `12/12 checks passed` (smuggled-label, dropped-row, laundered-hold, adapter-drift, malformed, missing) | ⟦IC⟧ GREEN (10:30Z) |
| SP-3 | the D4 projector emits 15 holds / 1 note / 0 fails over 74 labels | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | exit 1; `stats {"hold":15,"note":1,"fail":0,"labels":74}` | ⟦IC⟧ GREEN (10:20Z) |
| SP-4 | the landed expected set equals a fresh projector run | set comparison keyed `(id,severity,where,detail)` | 16/16 rows; symmetries empty; counts `{15,1,0}` | ⟦IC⟧ GREEN (10:29Z) |
| SP-5 | the expected file's pins name live bytes | sha256 vs `packet.d4.yml`, `typed-labels.d4.yml`, `tools/d2-typed-labels.py` | all three equal (`e7ecd204…`, `a59990bb…`, `0da0015f…`) | ⟦IC⟧ GREEN (10:29Z) |
| SP-6 | the projection is the projector's own build | `--check examples/culture-d4/typed-labels.d4.yml` | exit 0, `byte-identical deterministic projection` | ⟦IC⟧ GREEN (10:20Z) |
| SP-7 | the packet is the D4 assembler's own build | `assemble-culture-d4.py --check` | exit 0, `byte-identical deterministic assembly` | ⟦IC⟧ GREEN (10:20Z) |
| SP-8 | the D4 assembler's fixture matrix is intact | `assemble-culture-d4.py --selftest` | `81/81 checks passed` | ⟦IC⟧ GREEN (10:22Z) |
| SP-9 | the packet's component pins equal live component bytes | packet `assembly.source_sha256` block vs `sha256sum components/*.yml` | 12/12 equal (e.g. `01-brief a2bc3111…`, `12-provenance 540f7d22…`) | ⟦IC⟧ GREEN (10:21Z) |
| SP-10 | the projection's reader pin equals the live gate | `typed-labels.d4.yml:assembly.reader_sha256` vs `tools/gates/costume-era-consistency-gate.py` | equal (`e6bffd70…`) | ⟦IC⟧ GREEN (10:21Z) |
| SP-11 | the round-11 generation replays | `TMPDIR=/var/tmp/… python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | `REPLAY OK: 11/11` exit 0 | ⟦IC⟧ GREEN (10:22Z) |
| SP-12 | the round-17 D4 generation replays | same over `reports/round-17/tests/frozen/MANIFEST.tsv` | `REPLAY OK: 5/5` exit 0 | ⟦IC⟧ GREEN (10:22Z) |
| SP-13 | historical generations fail closed, not silently | same over `round-3`, `round-3/attempt-1`, `round-4` | exit 2 (`gate_digest_mismatch`, `manifest_unreadable`) | ⟦IC⟧ RED-as-recorded (10:28Z) |
| SP-14 | the D2-bound boundary exists on the gate **and** the adapter | gate over D4 packet; adapter over D4 packet+projection | exit 2 both; same detail `(e7ecd2045ef0 vs e0f21509e14a)` | ⟦IC⟧ RED-before-state (10:20/10:21Z) |
| SP-15 | legacy gates over the live D4 packet never exit 2 | five gates | exits {1,1,0,0,0}, no traceback | ⟦IC⟧ GREEN (10:22Z) |
| SP-16 | the 8→14 naming delta is packet-driven, not gate-side | naming gate over the pre-normalization frozen copy | 8 findings (vs 14 over live) | ⟦IC⟧ GREEN (10:28Z) |
| SP-17 | filed rounds 8–17 are untouched | `git status --porcelain -- reports/round-8 … 17`; `git diff --stat HEAD -- <same>`; `git ls-files <same> \| wc -l` | 0 / 0 / 761 | ⟦IC⟧ GREEN (10:30Z) |
| SP-18 | the two new gates run and forward their peer's verdict | `d4-typed-labels-check-gate.py`; `d4-assembly-check-gate.py` | exit 0, peer lines verbatim | ⟦IC⟧ GREEN (10:26Z) |
| SP-19 | battery/craft/assembler regressions | battery; craft `--counts` + `--selftest`; d2/d3 `--check` | 0 / 0 + 10/10 + 18/18 / 0 | ⟦IC⟧ GREEN (10:29Z) |
| SP-20 | the round-17 runner still fails on exactly one dependency | `reports/round-17/run-validation.py --check` | exit 1, `missing_dependencies ["examples/culture-d4/typed"]` | ⟦IC⟧ (10:29Z) |
| SP-21 | the expected file's landed bytes are the D01/D02 file | `sha256sum` at 10:25Z vs holds.md §0 | `09490a2756d123eb…`, 2850 B | ⟦IC⟧ GREEN |
| SP-22 | the union fragment's digest | cited: holds.md §3 (`ee0908e108b22fea…`) | — | cited |
| SP-23 | round-17 frozen copy ≠ live packet | `sha256sum` both | `2776d85c…` 82635 B vs `e7ecd204…` 82859 B | ⟦IC⟧ GREEN |
| SP-24 | the claims' counting command exists after the wave | `ls reports/round-18/run-validation.py` | present at 10:28Z; **not run** by this seat (a runner can itself be a writer) | ⟦IC⟧ present, unexecuted |

## 2. Hash-stability re-reads (a mismatch later means the file moved)

| path | digest (read time) | re-read |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | `d102fd1d…` (10:19:55Z) | identical at every poll through 10:28:55Z (receipt `.scratch/r18d21/poll.log`) |
| `tools/assemble-d2-typed.py` | `c7e5a749…` (10:19:55Z) | identical through 10:28:55Z |
| `tools/d2-typed-labels.py` | `0da0015f…` (10:19:55Z) | identical through 10:28:55Z |
| `examples/culture-d4/packet.d4.yml` | `e7ecd204…` (10:19:55Z) | identical at 10:21Z, 10:29Z |

## 3. Spot-checks deliberately **not** made (named gaps)

- **No D4 typed-packet check.** `examples/culture-d4/packet.d4.typed.yml` was
  absent at every stamp; the generalized gate was never observed (poll rows).
  The claim-D equality at the *gate* level is therefore not independent-checked
  here — only the expected-side and the projector-side equality are (SP-3/4/5),
  which is exactly the half this scribe shard owns.
- **No round-18 frozen generation to replay** at 10:31Z: `find reports/round-18
  -name 'MANIFEST.tsv'` → none; `tools/gates/frozen/round-18` → absent.
- **No write-behavior audit** of the new gates beyond their stdout: both are
  read-only by construction (they invoke peers in `--check` mode), and both
  reported no side effects; no filesystem diff was captured by this seat.
- **No independent replay of the D01/D02 derivation script**; SP-4 re-derives
  the content from the projector instead, which is the stronger test.

## 4. Reproduction

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/typed-pipeline-gate.py                       # SP-1
python3 tools/gates/typed-pipeline-gate.py --selftest            # SP-2
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json | head -5   # SP-3
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml                  # SP-14 (exit 2, before-state)
TMPDIR=/var/tmp/kotodama-r18d21 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv  # SP-11
git status --porcelain -- reports/round-8 reports/round-17 | wc -l   # SP-17 → 0
```

## 5. Limits

- Read-time pins; conclusions are bytes-plus-commands, never design quality,
  canon, or clearance.
- The wave was in flight at close: SP rows that depend on wave artifacts name
  their stamp, and any later re-read supersedes the value, not the method.

## 6. Post-state spot-checks (10:34–10:37Z)

| # | checked claim | command | reading | verdict |
|---|---|---|---|---|
| SP-25 | the generalized gate's default path is stdout-identical to the pre-change path | `python3 tools/gates/typed-pipeline-gate.py` → file digest | exit 0, 16/16 legs, stdout `15cdfbda73cd56cb6107…` = the pre-change reading (scribe-6 row 1) and the D01/D02 fragment's pin | ⟦IC⟧ GREEN (10:36Z) |
| SP-26 | only the gate surface changed at baseline | `git show 3dd3754:<p> \| sha256sum` vs live, four surfaces | gate `d102fd1d…` → `d4785d9a…`; adapter/projector/serializer unchanged | ⟦IC⟧ (10:36Z) |
| SP-27 | the gate revision moved during the window | poll rows | six distinct digests 10:23:55–10:33:55Z, then stable | ⟦IC⟧ |
| SP-28 | the new round-18 generation replays | `replay-frozen.py tools/gates/frozen/round-18-repin/MANIFEST.tsv` | exit 2: `1 could-not-evaluate` (`gate_digest_mismatch`, pin `5b4501a9…` vs live `d4785d9a…`), 10 reproduced | ⟦IC⟧ **RED** — routed as F-D21-1 |
| SP-29 | the D4 path advanced but is blocked on the adapter | gate over `examples/culture-d4/packet.d4.yml` | exit 2, `ok L1-assembler`, `ok L1-expected-holds`, `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` | ⟦IC⟧ (10:37Z) |
| SP-30 | the r18-post cascade left round-9 bytes alone | `git status --porcelain -- reports/round-9` | empty | ⟦IC⟧ GREEN (10:31Z) |
| SP-31 | the r18-post provenance stdout delta is a path echo, not a verdict change | inputs digests, gate pin, `expected` sets compared | inputs identical, gate pin identical, `expected` byte-equal (exit 1, same 6 ids); stdout differs only by the baseline-home path inside the scan lines | ⟦IC⟧ GREEN (10:34Z) |
| SP-32 | the battery still covers the enlarged surface | `check-gate-battery.py` | exit 0, `pass 7, fail 0, unevaluable 0` | ⟦IC⟧ GREEN (10:32Z) |

Two of the six post-state checks are not green, and both are routed rather
than repaired here: SP-28 (a stale gate pin inside the new generation) and
SP-29 (the missing D4 adapter). Neither is a data-integrity defect: no filed
byte moved and no pin was edited in place.

### 6.1 Negative claims at close (10:37Z)

- `examples/culture-d4/packet.d4.typed.yml` — absent (`ls examples/culture-d4/`
  → 7 entries; poll rows `typed_packet=no` T1–T11).
- `tools/assemble-d4-typed.py` — absent (the gate's own error line names it).
- Any D4 typed row in a frozen manifest — absent (`grep -l 'packet.d4.typed'
  tools/gates/frozen/round-18-repin/MANIFEST.tsv` → no match; the manifest's
  rows name the D2 typed packet and the D2 legacy packet).
- `reports/round-18/civ/` map-revision fragments exist (`README.md`,
  `patch-apply.md`, `delta-vs-round16.json`, `lessons-entry.md`) but the C
  claim is another shard's; nothing here re-derives it.
