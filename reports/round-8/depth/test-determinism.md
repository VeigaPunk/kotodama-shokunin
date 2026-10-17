# R8-D07 — D2 determinism test: regenerate twice via the new tool path, byte-compare

- round: 8 (loop 1, build 1 of 4) · date: 2026-10-17 · shard: R8-D07 (test)
- status: NON-CANON test record. No canon claim; no component, gate, packet or
  tool edited by this shard.
- claim under test: `reports/round-8/claims.json` D — "the D2 example packet
  regenerates deterministically". This record tests the **determinism leg
  only**; `--selftest` (32/32) and frozen replay are other shards' legs.
- artifact under test: `examples/culture-d2/typed-labels.d2.yml` — the new tool
  path's owned output (`tools/d2-typed-labels.py:1210`, `OUTPUT.write_bytes`).
  The tool must not touch `examples/culture-d2/packet.d2.yml` (design spec
  `reports/round-8/depth/design-spec.md` §5 D3); verified below.

## 1. Method (pre-registered before the definitive run)

1. Regenerate the artifact twice via the tool's only write path —
   `python3 tools/d2-typed-labels.py` (default mode; no `--emit` flag exists in
   the integrated tool) — keeping both byte images, then `sha256` +
   byte-compare (in memory; see §4 on `/tmp` ENOSPC).
2. Repeat once more as an independent confirmation pair after the cross-checks.
3. Stdout determinism: `python3 tools/d2-typed-labels.py --report` twice,
   byte-compare stdout.
4. Perturbations: same run from `cwd=/tmp` with `PYTHONHASHSEED=0`, and with
   `PYTHONHASHSEED=12345 TZ=UTC`.
5. Non-mutation: `packet.d2.yml` sha256 before/after; `--check` and `--report`
   must leave the artifact's sha256 and `st_mtime_ns` unchanged.
6. Content hygiene scan: no timestamps, no host paths, no CRLF in the artifact.
7. Pin all input hashes before and after every run so mid-round edits by other
   workers cannot silently contaminate the result (the tool is a live D02
   artifact — §4).

## 2. Environment and input pins at test time

- host date/time: 2026-10-17 17:24–17:25 (-03:00); python3 3.14.7
  (`python3 -c "import sys; print(sys.version.split()[0])"`); cwd = repo root.
- `tools/d2-typed-labels.py` sha256
  `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03`
  (66478 bytes, mtime 2026-10-17 17:22:53 -0300) — identical before and after
  every run in the definitive window.
- `tools/gates/costume-era-consistency-gate.py` sha256
  `6be04578fc219949daf938838793c3413c152a7c4339ff867d32621ea228f8f7`
  (70565 bytes, mtime 2026-10-17 17:20:31 -0300) — identical before and after.
- `examples/culture-d2/packet.d2.yml` sha256
  `8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e` —
  identical before and after.
- artifact at window start (written by D02's own run at ~17:24):
  `820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778`,
  68643 bytes.

## 3. Results

### 3.1 Regeneration pairs (the assigned test)

| pair | run | command | exit | stdout | artifact sha256 | bytes |
|---|---|---|---|---|---|---|
| A (17:24:21) | 1 | `python3 tools/d2-typed-labels.py` | 0 | `Wrote examples/culture-d2/typed-labels.d2.yml (68643 bytes)` | `820b7535…422f778` | 68643 |
| A (17:24:21) | 2 | `python3 tools/d2-typed-labels.py` | 0 | same bytes as run 1 | `820b7535…422f778` | 68643 |
| B (17:24:48) | 1 | `python3 tools/d2-typed-labels.py` | 0 | `Wrote … (68643 bytes)` | `820b7535…422f778` | 68643 |
| B (17:24:48) | 2 | `python3 tools/d2-typed-labels.py` | 0 | same bytes as run 1 | `820b7535…422f778` | 68643 |

- Pair A: artifact byte-identical True; stdout byte-identical True; stderr both
  empty; exits 0/0.
- Pair B: artifact byte-identical True; stdout byte-identical True.
- **4 regenerations, 2 independent pairs, one digest.** No drift.
- `python3 tools/d2-typed-labels.py --check` (17:24:21): exit 0, stdout
  `examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic build`.

### 3.2 Stdout determinism

- `--report` twice (17:24:21): exits 0/0, stdout byte-identical True, stdout
  sha256 `421c9173b1ed5dd36cd3700f14fc34bf03e14cd63c30953421cef8d27c7c801d`,
  stderr empty both.
- The report's own coverage counts (from that command, 2026-10-17):
  `labels_total=94, labels_by_kind={"borrowed-strata": 2, "descriptive-gloss":
  16, "fictional-coordinate": 9, "native-form": 48, "translated-label": 19},
  labels_unresolved=26, prose_rules_total=21, rank_rules_executable=3,
  rank_rules_held=18, costume_rows=10, costume_rows_rank_resolved=7,
  era_rows=7, era_rows_held=4, canonical_tags_referenced=['E0','E1','E2']`.

### 3.3 Perturbations (17:24:21)

| run | cwd | env | exit | artifact sha256 | byte-identical to pair A |
|---|---|---|---|---|---|
| 6 | `/tmp` | `PYTHONHASHSEED=0` | 0 | `820b7535…422f778` | True |
| 7 | `/tmp` | `PYTHONHASHSEED=12345 TZ=UTC` | 0 | `820b7535…422f778` | True |

stderr empty both; no path/locale/hash-seed leakage observed.

### 3.4 Non-mutation and content hygiene (17:24:21–17:25)

- `packet.d2.yml` sha256 unchanged across all runs (`8da90b07…`) — the tool
  never wrote the packet (design spec §5 D3 honored).
- `--check` exit 0 and `--report` exit 0 left the artifact's sha256 and
  `st_mtime_ns` unchanged (script compared `(sha256, st_mtime_ns)` tuples).
- `--selftest` (context; D06 owns this leg; measured on the pinned revision
  `623b5b1f…` only): `32/32 checks passed`, exit 0, "no file outside the
  temporary directory touched".
- Hygiene scan over the artifact bytes (`python3` re-scan, 2026-10-17):
  date-like strings `20\d\d-\d\d-\d\d` → none; lines containing `/home/` →
  none; `\r\n` present → False; trailing newline → True. LF-only,
  timestamp-free, host-path-free.
- Artifact top-level keys (read from the file): `name, canon, generator,
  label_kinds, labels, era_reconciliation, material_reconciliation,
  rank_rule_adapter, eras, materials, costumes, rank_rules, findings,
  coverage, assembly`. The `assembly` block pins `reader_sha256` and source
  hashes — see §4 on why a digest change across revisions is expected and is
  not run-to-run nondeterminism.

### 3.5 Head-revision re-test (17:31, tool `e9209f28…`)

D02 landed a larger revision during this window (`tools/d2-typed-labels.py`
sha256 `e9209f280c6d765561a47efdee074d0cff5f3e786e5f4f9ae7c96cc65df4a282`,
143147 bytes, mtime 17:30:40) with a changed CLI: `--emit PATH`,
`--check [PATH]`, `--json`, `--packet`; default mode now prints the report and
does not write. Re-tested because the on-disk artifact changed under it
(`examples/culture-d2/typed-labels.d2.yml` = `59a53456…`, 81469 bytes, mtime
17:30:45, emitted by D02's own run of this revision).

- `python3 tools/d2-typed-labels.py --check` (17:31:31): exit 0,
  "…typed-labels.d2.yml: byte-identical deterministic projection".
- Two `python3 tools/d2-typed-labels.py --emit /dev/stdout` runs (17:31:5x;
  `/tmp` was ENOSPC again, so projection bytes were captured in memory instead
  of scratch files): exits 1/1 (findings present), stdout 81487 bytes each,
  **byte-identical**. Captured stdout = projection payload + trailing
  `Wrote /dev/stdout\n`; the payload (81469 bytes) is byte-equal to the
  on-disk artifact (`59a53456…`) — the revision reproduces the same projection
  across runs and matches the artifact D02 emitted.
- Default-mode runs (17:31:24, 17:31:36): exit 1 (findings), stdout identical,
  artifact sha256 and `st_mtime_ns` unchanged (default mode no longer writes).
- Tool sha256 re-checked identical before and after all runs in this
  subsection.

## 4. Interference log (documented because receipts depend on it)

The tool is a live artifact of shard R8-D02 and the gates were concurrently
edited by O-claim workers during this test window. All timestamps are
2026-10-17, -03:00.

- Tool versions observed while polling (sha256 prefixes, sampled by
  `sha256sum tools/d2-typed-labels.py`): `429191fd…` (17:21:08, crash:
  `TypeError: adapt_rules() missing 1 required positional argument:
  'tag_space'`, raised from the then-current `build_artifact`, line 967),
  `3f1d2439…` (crash, same), `f0192bc4…` (crash), `33ce9eea…` (healthy),
  `da86132e…` (crash), `097a23a3…` (healthy), `623b5b1f…` (stable ≥3
  consecutive 30 s samples, then healthy through the definitive window). The
  definitive test ran entirely on `623b5b1f…`, re-verified before and after
  every run.
- An earlier healthy version (17:19:34, sha not captured) produced artifact
  `08de5a88ff93b42c59909ee04d028eda9526800b6955ca58db89dd33225479dd`
  (68223 bytes) with the same double-run byte-identity property. The stable
  version produces `820b7535…` (68643 bytes). The artifact embeds
  `assembly.reader_sha256` (currently `6be04578…`) and source hashes, so the
  digest change tracks **input revision** (tool + gate), not nondeterminism;
  each version was internally byte-deterministic.
- Version drift continued after the pinned-version test: `56c0db14…` (17:25:40,
  119148 bytes) crashed `--selftest` (`RecursionError: maximum recursion depth
  exceeded` at `contextlib.redirect_stdout(buffer)`) and its default run exited
  2 (`FINDING D2L-DATA: [error] … packet.d2.yml — content '-' is not a mapping
  line`); ten further sampled shas through 17:30:32 (`f0110e39…`, `5d87d346…`,
  `664cf81a…`, `61b61eb4…`, `3bb693fc…`, `6a80ffe4…`, `11e23ca9…`,
  `12f71137…`, `3548185c…`) all failed the `--report` health probe with exit
  2. The head revision `e9209f28…` (17:30:40) is healthy and is the version
  re-tested in §3.5; it then moved on again (`1fdc055e…`, 17:32:4x, not
  tested). The round harness's claim-D FAIL (`tools/d2-typed-labels.py
  --selftest exit 1 … traceback`, run ~17:26) was observed against one of
  these mid-integration revisions, not against `623b5b1f…` or `e9209f28…`.
- The frozen costume gate was edited concurrently: `packet.d2.yml:3322` pins
  `reader_sha256: "29a9361c…"`, while the on-disk gate became `2adb7b5e…`
  (mtime 17:20:05) and then `6be04578…` (mtime 17:20:31). Observed consequences
  (not caused by this shard, flagged for the round):
  - `python3 tools/assemble-d2.py --check` → `packet.d2.yml differs from
    deterministic assembly`, exit 1 (17:24:21). It was green earlier in this
    session: `packet.d2.yml: byte-identical deterministic assembly`, exit 0
    (17:13:31).
  - `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` →
    exit 2, `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0
    reproduced of 7 row(s)`, reason `gate_digest_mismatch` ("on-disk bytes are
    not the pinned revision"), e.g. `tools/gates/provenance-audit.py`
    (17:24:22). It was `REPLAY OK: 7/7 …`, exit 0 at 17:13:31.
  - The frozen-replay leg of claim D therefore currently needs the O-claim gate
    edits reconciled against the round-3 manifest; this test neither caused nor
    repaired it.
- `/tmp` (tmpfs) hit `OSError: [Errno 28] No space left on device` four times
  in the window (17:19:5x scratch copy, 17:24:13 scratch copy, 17:31:5x
  `--emit` to a scratch path, 17:32:41 `--selftest` fixture `mkdir`) under
  64-worker swarm pressure. Consequence for the round: the tool's `--selftest`
  builds its fixture tree in `/tmp`, so its pass/fail also measures tmpfs
  pressure; the harness's claim-D selftest check can be ENOSPC-driven. All
  receipts in this record are in-memory byte comparisons; no scratch files
  remain.

## 5. Verdict

- **Determinism leg of claim D: supported on both tested revisions.**
  - Pinned revision `623b5b1f…` (§2–§3.4): 4 regenerations in 2 independent
    pairs → one artifact digest (`820b7535…`, 68643 bytes); `--check` exit 0;
    stdout byte-identical; cwd/hash-seed/TZ perturbations byte-identical.
  - Head revision `e9209f28…` (§3.5): two `--emit` runs byte-identical, and the
    emitted projection (81469 bytes) is byte-equal to the on-disk artifact
    `59a53456…`; `--check` exit 0.
  - In both, `packet.d2.yml` (`8da90b07…`) was never touched by the tool path.
- Support scope: run-to-run byte determinism of the tool's own projection under
  pinned inputs on this host and interpreter. It is **not** a claim about
  cross-version stability — the artifact digest changed with input revision by
  design (it embeds `assembly.reader_sha256` and source hashes, §4), and the
  two tested revisions produce different projections (`820b7535…` vs
  `59a53456…`) — nor cross-host reproducibility.
- The tool is still moving under the round (newest observed sha `1fdc055e…` at
  17:32:4x, not tested). If a later revision becomes the delivered one, the
  determinism pair must be re-run; the result above is version-scoped.
- Not tested here (other shards): `--selftest` control semantics beyond the
  pass count, frozen-replay digest equality (currently could-not-evaluate,
  §4), and the claim-D requirement that the *packet* itself regenerates
  deterministically — that path is `tools/assemble-d2.py`, whose two
  consecutive regenerations were byte-identical at 17:13:31 (`8da90b07…`),
  before the concurrent gate edit turned its `--check` red.

Commands and dates for every count and claim in this record are inline above;
negative claims carry their scan commands in §3.4 and §4.

Record sealed 2026-10-17 17:33:21 (-03:00): at seal time the live tool sha256 is
`1131912d…` and the on-disk artifact is `e70ba147…` — both have moved since the
tests above, which remain version-scoped to the revisions named in each
section. `packet.d2.yml` is still `8da90b07…`.
