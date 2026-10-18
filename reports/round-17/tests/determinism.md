# R17-D26 — determinism: two independent D4 assemblies are byte-identical

- round: 17 (operator loop 2 of 3, build round 1 of 4) · shard: **D26** (tests ×4,
  claim D `culture-d4-assembly`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "D4 R17-D26..D29 (tests x4): determinism (two assemblies
  byte-identical); replay-frozen over D4 artifacts; interop (assemble-d2/d3
  --check + battery + craft green); gate findings == named hold set exactly.
  reports/round-17/tests/{determinism,replay,interop,holdset}.md."
- date: 2026-10-18. Baseline revision
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (`reports/round-17/claims.json:5`);
  working-tree HEAD `9b49a4a` at write time.
- canon: NON-CANON engineering evidence. No culture design, no canon record, no
  handoff, no real-world clearance or rights statement is made here.
- writes: **this file only** plus gitignored scratch under `.scratch/r17-tests/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No tool,
  gate, packet, component, projection or earlier-round byte is edited by this
  seat. No commit, no push.
- **status: complete — deterministic.** Two assemblies in isolated mirrors at
  different absolute paths are byte-identical to each other and to the delivered
  packet, and the build writes exactly one file.

## 1. What is measured

Claim D's determinism leg: "deterministic assembly (twice byte-identical)"
(`reports/round-17/claims.json:15`); the round-17 counting contract measures the
same leg as "the d4 assembler's `--check` regenerates byte-identically and two
fresh adapter builds are byte-identical to each other"
(`reports/round-17/scope.md:106`). This shard measures the **assembler** half on
the delivered tree; the adapter half has no artifact to build (see §5).

## 2. Method (scratch-only, no live-tree write)

Two mirrors, each at a different absolute path (so any host-path or cwd leak
would show as a byte difference), each containing the same copy set:
`tools/assemble-culture-d4.py` plus the sibling tools it may load read-only
(`assemble-d2.py`, `assemble-d2-typed.py`, `d2-typed-labels.py`,
`assemble-culture-d3.py`), the whole `tools/gates/` tree, and the delivered
`examples/culture-d4/` tree (148 files per mirror). The assembler was then run
once in each mirror; the two trees were hashed file-by-file and compared.

Pins at measurement time (`sha256sum`, 2026-10-18): assembler
`03a0754eec5565aad76598be53de4ba26e0199c81a30814ec88e87e31951f466`; delivered
packet `2776d85cb2b3f03bf084df3974b3ff59c44b81b0004997c4e4bd830b05335d72`
(82635 bytes). Python 3.14.7.

## 3. Receipts (2026-10-18, all exits measured)

| # | command (mirror cwd) | exit | observed |
|---|---|---:|---|
| 1 | `python3 tools/assemble-culture-d4.py` in `mirror-a` | 0 | `Wrote examples/culture-d4/packet.d4.yml (82635 bytes)` |
| 2 | `python3 tools/assemble-culture-d4.py` in `mirror-b` | 0 | `Wrote examples/culture-d4/packet.d4.yml (82635 bytes)` |
| 3 | `find … \| sort \| xargs sha256sum` over both trees, `diff -u` | 0 | empty diff — 148/148 files identical |
| 4 | `sha256sum` of the two built packets + the delivered packet | — | `2776d85c…335d72` ×3 (mirror-a = mirror-b = delivered) |
| 5 | `python3 tools/assemble-culture-d4.py --check` (live tree) | 0 | `packet.d4.yml: byte-identical deterministic assembly` |
| 6 | `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed` (fixture positive/tamper/malformed/missing + collision, duplicate-id, wrong-type, empty-block, missing-field, too-few-files, serializer/reader-absent) |

**Exactly one file written, nothing else touched** (measured, not assumed): the
mirror file set equals the copied source file set exactly — 148 copied, 148
present, `extra = []`, `missing = []`, and per-file content drift against the
source `= []`. The only rewrite is `packet.d4.yml`, and it is byte-identical to
the delivered bytes.

**The packet's own pins re-verify** against the bytes read (2026-10-18): all 12
`assembly.source_sha256` component digests match the delivered
`examples/culture-d4/components/*.yml`; `assembler_sha256`, `reader_sha256`
(`tools/gates/costume-era-consistency-gate.py` `e6bffd70…ec478f`) and
`serializer_sha256` (`tools/assemble-d2.py` `8ea6bdde…c8655d`) all match the live
files — 0 mismatches.

**Revision note.** The packet was revised once while this wave ran: `39c2d56a…`
(80509 bytes, 06:44 local) → `2776d85c…` (82635 bytes, 06:49 local); `--check`
was exit 0 on both revisions, and every receipt above is on the final
`2776d85c…` bytes. A later component edit invalidates these pins before any
verdict (the standard's rule, `corpus/knowledge/verification/gate-frozen-run-standard.md`).

## 4. What this does and does not establish

- It establishes: the D4 assembler is byte-deterministic across independent
  builds at different absolute paths, regenerates the delivered packet
  byte-identically, and owns exactly one output file.
- It does **not** establish: that the packet is *correct*, that any gate is
  clean, or canon standing. The five legacy gates still return 9 findings over
  this packet (8 naming + 1 phonology; `reports/round-17/tests/interop.md` §3),
  and the two red gate rows stay red.

## 5. Named gap (reported, not absorbed)

The **typed** half of the determinism leg — "two fresh adapter builds are
byte-identical to each other" and reproduce the delivered typed packet
(`reports/round-17/scope.md:106`) — is **not evaluable at this stamp**: no
`examples/culture-d4/packet.d4.typed.yml` or `typed-labels.d4.yml` exists, and no
D4 adapter exists to build one. Sweep (2026-10-18, lane root): `ls tools/ | grep
-i d4` → `assemble-culture-d4.py` only; `ls examples/culture-d4/` → `ASSEMBLY.md
brief.md components packet.d4.yml README.md`; `reports/round-17/run-validation.py
--check` lists the typed/projection/expected artifacts as missing dependencies.
The blocking cause is recorded independently in `reports/round-17/d4/typed-run.md`
§0 (projector exit 2, `packet.eras: expected a non-empty list of era tags`) and
re-measured by this seat in `reports/round-17/tests/holdset.md` §4.

## 6. Reproduce

```sh
export TMPDIR=$PWD/.scratch
# mirrors, two independent builds, byte comparison, live --check:
bash .scratch/r17-tests/determinism-run.sh        # scratch harness used above
python3 tools/assemble-culture-d4.py --check      # exit 0 on the delivered tree
python3 tools/assemble-culture-d4.py --selftest   # 81/81
```
