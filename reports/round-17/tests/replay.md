# R17-D27 — replay: the round-17 D4 frozen record replays green

- round: 17 (operator loop 2 of 3, build round 1 of 4) · shard: **D27** (tests ×4,
  claim D `culture-d4-assembly`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "D4 R17-D26..D29 (tests x4): determinism (two assemblies
  byte-identical); replay-frozen over D4 artifacts; interop (assemble-d2/d3
  --check + battery + craft green); gate findings == named hold set exactly.
  reports/round-17/tests/{determinism,replay,interop,holdset}.md."
- date: 2026-10-18. Baseline revision
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; working-tree HEAD `9b49a4a`.
- canon: NON-CANON engineering evidence. Nothing here is a clearance or a canon
  record; a reproduced red verdict stays red.
- writes: **this file**, plus the frozen record this shard is chartered to build
  (`reports/round-17/tests/frozen/`: `MANIFEST.tsv`, the pinned packet copy, its
  snapshot, five recorded outputs), plus gitignored scratch under
  `.scratch/r17-tests/`. No tool, gate, packet, component, projection or
  earlier-round byte is edited; `tools/gates/frozen/**` and
  `reports/round-{8..16}/**` are filed and read-only. No commit, no push.
- **status: complete — 5/5 rows reproduced (exit 0).** The parent's runner now
  finds a round-17 manifest and replays it green (§4).

## 1. What is pinned

The frozen record pins **the five legacy culture gates over a byte copy of the
delivered D4 packet**, the same five runs `examples/culture-d4/ASSEMBLY.md:32-38`
records:

| row | gate | input | recorded verdict |
|---|---|---|---|
| 1 | `tools/gates/naming-collision-gate.py` | `reports/round-17/tests/frozen/packet.d4.yml` | exit **1**, 8 findings |
| 2 | `tools/gates/phonology-sanity-gate.py` | same | exit **1**, 1 finding |
| 3 | `tools/gates/costume-era-consistency-gate.py` | same | exit **0**, 0 findings |
| 4 | `tools/gates/lexicon-coverage-audit.py` | same | exit **0**, 0 findings |
| 5 | `tools/gates/myth-consistency-gate.py` | same | exit **0**, 0 findings |

Pinned bytes: packet copy = delivered
`examples/culture-d4/packet.d4.yml` sha256
`2776d85cb2b3f03bf084df3974b3ff59c44b81b0004997c4e4bd830b05335d72` (82635
bytes, frozen 2026-10-18); the five gate scripts are pinned by `gate_sha256`
against the live files, which the D claim requires untouched (verified: §3).

Rows are recorded against the **frozen copy** rather than the live packet path on
purpose: the standard's rule is that later input edits invalidate a snapshot
before any verdict, and this wave was still writing when the record was built.
The live-path receipts are recorded separately in §3 so the tie to the delivered
artifact is explicit, not implied.

## 2. Replay receipts (2026-10-18)

| # | command | exit | observed |
|---|---|---:|---|
| 1 | `TMPDIR=/tmp python3 tools/replay-frozen.py reports/round-17/tests/frozen/MANIFEST.tsv` | 0 | `REPLAY OK: 5/5 rows reproduced the recorded verdicts` — every row `bytes=match launched=yes` |
| 2 | `TMPDIR=/var/tmp/kotodama-r17 python3 tools/replay-frozen.py …` (second, independent TMPDIR) | 0 | same 5/5 |
| 3 | `TMPDIR=/var/tmp/kotodama-r17 python3 tools/replay-frozen.py --selftest` | 0 | `selftest: 79/79 checks passed` |
| 4 | `TMPDIR=/var/tmp/kotodama-r17 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | 0 | `REPLAY OK: 11/11 rows` — the live D2 generation still reproduces |

`TMPDIR` is outside the repo for every replay call, as
`tools/gates/frozen/round-11/README.md` requires (`replay-frozen.py` refuses
in-repo mirrors by design). Row 1 uses `/tmp`, exactly how
`reports/round-17/run-validation.py` invokes the tool.

## 3. Live-path receipts and pins (the delivered artifact tie)

The five gates run over the **live** packet at the same revision return the same
verdicts and byte-identical output (2026-10-18, `TMPDIR=$PWD/.scratch`):
naming exit 1 / 8 findings, phonology exit 1 / 1 finding,
costume/lexicon/myth exit 0 / 0 findings; no exit 2 and no traceback in any of
the five runs. Gate pins: naming `d9e4e8f4…630a1d`, phonology `d5fe087f…c34230`,
costume `e6bffd70…ec478f`, lexicon `2c4dd397…d27d4287`, myth `5368b135…6b95f08`
(`sha256sum`, 2026-10-18).

## 4. The parent's discovery leg

`python3 reports/round-17/run-validation.py --check` (read-only mode, does not
write the parent's receipt) was run by this seat at 2026-10-18 07:04 local: the
manifest is discovered (`MANIFEST_GLOBS` matches
`reports/round-17/**/MANIFEST.tsv`, `reports/round-17/run-validation.py:94-97`),
replays green, and `missing_dependencies` no longer lists "round-17 frozen
manifest". The remaining claim-D failures are exactly the three typed artifacts
(`typed`, `projection`, `expected`), which are outside this shard (§6).

## 5. Controls, including the superseded generations

| control | command | observed |
|---|---|---|
| round-3 generation | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | exit **2** — 7/7 rows `gate_digest_mismatch` (`launched=no`), e.g. provenance-audit pinned `4aaea6e9…` vs live `8a96aaf4…` |
| round-3 attempt-1 | same over `round-3/attempt-1/MANIFEST.tsv` | exit **2** — 7/7 rows `gate_digest_mismatch` |
| round-11 (live generation) | §2 row 4 | exit 0, 11/11 |

The round-3 readings are the recorded historical-pin class: rounds 8–16
legitimately revised those gates, so the old manifests can no longer be
evaluated — they fail closed rather than silently passing. This independently
matches `reports/round-17/scope.md` finding F-X02-3 (same reason, same rows). No
filed manifest was edited to make it green.

## 6. Named gap and limits

- **Reproduction only.** Exit 0 means every row reproduced its recorded verdict;
  rows 1–2 are recorded red and stay red. Nothing here says the D4 packet is
  clean, and the record is not canon, acceptance, or clearance.
- **No typed-gate row exists.** A row pinning a D4 typed-pipeline gate is absent
  because no such gate or typed packet exists at this stamp (sweep 2026-10-18:
  `ls tools/gates/ | grep -i d4` → empty; `ls examples/culture-d4/` → no
  `packet.d4.typed.yml`). The typed half of claim D's replay requirement
  (`reports/round-17/scope.md:106-108`) therefore cannot be measured yet; the
  blocking cause is recorded in `reports/round-17/d4/typed-run.md` §0 and
  re-measured in `reports/round-17/tests/holdset.md` §4.
- **Staleness rule.** Any later edit to a component (hence the packet) or to a
  pinned gate invalidates this record before any verdict; rebuild with
  `.scratch/r17-tests/build-frozen-record.py` after such an edit — never edit
  `MANIFEST.tsv` by hand.

## 7. Reproduce

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-culture-d4.py --check                 # exit 0, packet bytes as pinned
TMPDIR=/tmp python3 tools/replay-frozen.py reports/round-17/tests/frozen/MANIFEST.tsv
# → REPLAY OK: 5/5 rows reproduced the recorded verdicts
```
