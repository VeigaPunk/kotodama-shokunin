# R10-F18 — stale fix: round-3 frozen-replay claim in `SKILL.md` (live exit 2 → pinned-revision recipe)

- seat: freshness stale-fixer (R10-F16..F19). This file is the seat's write; the
  `SKILL.md` corrections it records are the in-place fix.
- date: 2026-10-17 · lane: `kotodama-shokunin` · baseline `9dc18ec1…`
- live HEAD at work: `e3a1ec9` (+ worktree edits)

## Items taken from the ledger

| ledger row (0-based) | locator | shard | verdict in ledger |
|---|---|---|---|
| 55 | `SKILL.md:162` (`round-3/MANIFEST.tsv`) | shard-09 | `stale-documented` (7/7 `gate_digest_mismatch`) |
| 56 | `SKILL.md:162` (`attempt-1/MANIFEST.tsv`) | shard-09 | `stale-documented` (same class) |
| 82 | `SKILL.md:190` (claim at `:162`/`:177`) | shard-10 | `stale-documented` (DR-10-01, "fix routing F15-F18/orchestrator") |
| 98, 99 | invoked by `reports/round-5/run-validation.py:158` | shard-11 | `stale-documented` (same two commands, as runner dependencies) |

## Evidence

- Live tree: `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`
  → **exit 2**, stdout sha256
  `76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80`;
  7 rows `could-not-evaluate`, `reason=gate_digest_mismatch` on all six gate
  scripts; `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0
  reproduced of 7 row(s)`. `attempt-1/MANIFEST.tsv` reads the same (shard-09
  row 2, sha `409db5ab…`).
- Cause, measured: the round-8 admission commit `e1694ba` (2026-10-17 17:44:17)
  revised every gate file the pins name
  (`git log --format='%h %ci %s' -- tools/gates/<gate>.py` → only `e1694ba`
  and `291c714` for each of the six). The pins name the **round-1** bytes.
- The pinned revisions are recoverable: at `291c714`, all six gate files hash to
  exactly the manifest's `gate_sha256` values:

```
fb05c644…  phonology-sanity-gate.py     63ee4ec6…  lexicon-coverage-audit.py
26d246e9…  myth-consistency-gate.py     29a9361c…  costume-era-consistency-gate.py
8c5afb0a…  naming-collision-gate.py     4aaea6e9…  provenance-audit.py
```
  (`for g in <six gates>; do git show 291c714:tools/gates/$g.py | sha256sum; done`)

## Fix applied (in place, `SKILL.md`)

1. `SKILL.md:162` (evidence-table row) — the bare live-tree command was replaced
   by the pinned-revision recipe, with the live reading named:

```
| Frozen replay exits 0 with recorded findings | The red verdict reproduced; the culture did not become clean | pinned-revision replay: restore each gate from the commit whose bytes match the manifest pin (the round-3 pins are the gate bytes at `291c714`), then run `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <isolated-tree>`; the live tree now reads exit 2, 7/7 `gate_digest_mismatch` (`reports/round-10/drift/fix-18.md`) |
```

2. `SKILL.md:177-182` (prose) — "The round-3 TSV recording is replayable" was
   replaced by the measured statement: replayable **only** in an isolated tree
   holding the pinned revisions; live tree reads exit 2 with 7/7
   `gate_digest_mismatch`; restoring the files from `291c714` reproduces 7/7,
   exit 0.

The new cited key (`tools/replay-frozen.py` + `--repo-root`) is already covered
by ledger row 57 (shard-09's remediation control, verdict `current`, exit 0), so
the round-10 validator's "ledger covers cited commands" check is not weakened by
this edit (verified: at the 18:55Z measurement the only missing keys it reported
were `--selftest` keys on SCORECARD rows — none introduced by this edit; the
missing-key list is volatile while other seats keep landing ledger rows, and a
later run showed one remaining key, `assemble-culture-d3.py --selftest` at
`SKILL.md:264`, again not from this edit).

## Control (re-runnable, two independent reproductions)

1. This seat — isolated tree built from `291c714` gates + committed frozen tree
   + committed replay tool:

```
ISO=.scratch/r10f16/iso; mkdir -p "$ISO/tools/gates"
cp tools/replay-frozen.py "$ISO/tools/replay-frozen.py"
for g in phonology-sanity-gate lexicon-coverage-audit myth-consistency-gate \
         costume-era-consistency-gate naming-collision-gate provenance-audit; do
  git show 291c714:tools/gates/$g.py > "$ISO/tools/gates/$g.py"; done
cp -a tools/gates/frozen "$ISO/tools/gates/frozen"
cd "$ISO" && python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root "$ISO" --json
```
   → **exit 0**, `"summary": {"rows": 7, "reproduced": 7, "mismatch": 0,
   "could_not_evaluate": 0, "exit": 0}` (2026-10-17).

2. shard-09 (independent) — export at commit `c610e0a`, same command shape →
   exit 0, sha256 `10b82d575006e744f06789b06e931541460aa3f6c65dde42222270e4fbed210d`,
   "7/7 rows reproduced (red rows 2,4,5,6 reproduced at exit=1)".

## Limits

- Replay exit 0 means the recorded verdicts were reproduced, including expected
  red ones — it is not a re-verification of any culture's content.
- `c610e0a` and `291c714` are two distinct commits whose gate bytes both match
  the pins; the recipe selects **by digest**, so either is acceptable.
- Round-4 remains unpinned legacy evidence (`manifest_unreadable`, shard-09
  row 4) — that claim in `SKILL.md:182-183` is current and was left unchanged.

## Ledger delta (for the F14 scribe / integrator)

```json
[{"id": "R10-F18-01", "command": "python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv", "source_locator": "SKILL.md:162", "round10_verdict": "stale-fixed", "output_sha256": "76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80", "exit": 2, "fix_evidence": "reports/round-10/drift/fix-18.md", "note": "claim corrected in place: live tree reads exit 2 (7/7 gate_digest_mismatch); pinned-revision recipe (restore gates from 291c714) reproduces 7/7 at exit 0 — control demonstrated twice"},
 {"id": "R10-F18-02", "command": "python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv", "source_locator": "SKILL.md:162 (same class)", "round10_verdict": "stale-fixed", "output_sha256": "409db5ab8b68ebc3da9a8360879db71c01e58b40ea4a8311e3818efe289c8452", "exit": 2, "fix_evidence": "reports/round-10/drift/fix-18.md", "note": "same cause and same recipe; the corrected SKILL.md text now names the live reading for the class"}]
```
