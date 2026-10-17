# R10-F17 — stale fix: `SKILL.md` civilizations count (92 → 94 entries)

- seat: freshness stale-fixer (R10-F16..F19). This file is the seat's write;
  the `SKILL.md` correction below is the in-place fix it records.
- date: 2026-10-17 · lane: `kotodama-shokunin` · baseline `9dc18ec1…`
- live HEAD at work: `e3a1ec9` (+ worktree edits)

## Item taken from the ledger

| ledger row (0-based) | locator | shard | verdict in ledger |
|---|---|---|---|
| 38 | `SKILL.md:143` | shard-07 | `stale-documented` (note: "94 vs SKILL.md's '92'; corpus/README.md:116 already says (94); owner shard 08 / F15-F18") |

- `reports/round-10/drift/shard-07.md` §3.2 and
  `reports/round-10/drift/shard-08.md` §3.2 both note the ambiguity: shard-08
  reads it as "92 = 94 − 2 maps" (a clarity question), shard-07 as stale
  against the directory and the README. Either reading is resolved by naming
  the two source maps explicitly.

## Evidence

- `ls corpus/knowledge/civilizations/*.md | wc -l` → `94` (2026-10-17, lane root).
- `corpus/README.md:116` → `## civilizations/ (94)`.
- `SCORECARD.md` (round-5/6 coverage rows) already reads "civilization partition
  remains 92 bases + two source maps, not 94 verified civilizations".
- The two non-base files are `africa-primary-sources.md` and
  `mesoamerica-primary-sources.md` (`corpus/README.md:119,179` describe both as
  bounded source maps, not culture bases).

## Disposition: `stale-fixed`

`SKILL.md:143-145` — before:

```
- `corpus/knowledge/civilizations/` — 92 earlier-civilization bases, each
  coupling that tradition's language, writing, myth, symbols, era model,
  costume, and naming, with provenance cautions.
```

after:

```
- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
  bases plus two source maps (`africa-primary-sources.md`,
  `mesoamerica-primary-sources.md`), each
  coupling that tradition's language, writing, myth, symbols, era model,
  costume, and naming, with provenance cautions.
```

The "92 bases" claim is preserved (it is the SCORECARD/README claim); the file
count is now named as well, so a reader counting the directory cannot read the
row as an off-by-two error.

## Control (re-runnable)

- `sed -n '143,147p' SKILL.md` → the corrected row.
- `ls corpus/knowledge/civilizations/*.md | wc -l` → `94`.
- `grep -n "92 earlier-civilization bases" SKILL.md` → no match (exit 1).

## Limits

- This corrects a count, not a verification claim: the 92 bases remain
  author-side reference bases, not independently verified civilizations
  (`SCORECARD.md` "no … 94 verified civilizations" wording is retained).

## Ledger delta (for the F14 scribe / integrator)

```json
[{"id": "R10-F17-01", "command": "ls corpus/knowledge/civilizations/*.md | wc -l", "source_locator": "SKILL.md:143", "round10_verdict": "stale-fixed", "output_sha256": "6fc16b03d8c15b9885876848a301a01816cccaf7b48e74f2b51db99c007a3bd5", "exit": 0, "fix_evidence": "reports/round-10/drift/fix-17.md", "note": "row now reads '94 entries: 92 earlier-civilization bases plus two source maps'; matches corpus/README.md:116 and SCORECARD"}]
```
