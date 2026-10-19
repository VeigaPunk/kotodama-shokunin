# Round-34 anchor reissue — A09 R5 SKILL.md anchors (claim C, second leg)

**Source:** `reports/round-34/calib/C09-final-receipt.md` §5/§5.1 (measured there by
two independent derivations — content match against `git show 139e3b6:SKILL.md`
and cumulative hunk arithmetic; both agree). Landed by the integrator as a NEW
table: filed rows citing old anchors stay byte-identical as superseded readings.

**Pins:** SKILL.md at the round-33/34 boundary moved 715 → 732 lines,
digest `79fe91d3…` → `f9bd07c2…`. Old-anchor citations in filed bytes are
superseded readings, re-issued here, never edited.

Class legend: **U** unchanged · **C** address stable, content replaced by the
round-33 edits · **M** address moved · **R** target retired.

| pre-r33 anchor (715 lines) | post-r33 anchor (732 lines) | class | owning row | what changed |
|---|---|---|---|---|
| `:47` | `:47` | U | A09 R5 | self-cite target, unchanged; cited by `SKILL.md:149`, `SKILL.md:183` |
| `:128` | `:128` | C | A09 R5 / C14 Fix 4 | basis-witness line now cites `tools/harness/packet_uncertainty.py:205,209` with the dated erratum clause |
| `:149` | `:149` | U | A09 R5 | self-citing row, unchanged |
| `:183` | `:183` | U | A09 R5 | second self-citing row, unchanged |
| `:294` | `:294` | U | A09 R5 | cited by `corpus/lessons/README.md:245`, `round-31.md:46`, `round-32.md:34`, `round-32.md:58` |
| `:456-458` | `:456-458` | U | A09 R5 | no live citer (A09 prose grouping only) |
| `:479`,`:481`,`:483`,`:486`,`:488`,`:491` | same | C | A09 R5 | decision-table rows rewritten by C14 Fixes 1-3 |
| `:501` | `:501` | C | A09 R5 | boilerplate-basis row rewritten |
| `:522` | `:522` | U | A09 R5 | checklist heading |
| `:534` | `:534` | U | A09 R5 | checklist section end |
| `:535` | `:535` | U | A09 R5 | blank line |
| `:536` | `:536` | U | A09 R5 | `## Corpus map` |
| `:584` | `:584-586` | C+M | A09 R5 | TMPDIR/isolated-export line rewritten (1→3 lines) |
| `:660` | `:662` | M | A09 R5 | D3 drill heading; no live citer at the census |
| `:710` | `:726` | M | A09 R5 | no live citer at the census |
| `:713-715` | `:729-732` | M | A09 R5 | the round-31 checklist item + its continuation |
| `AGENTS.md:42` (residue) | — | R | A09 R5 / A09-F3 | target excised by the round-33 integration (42 → 40 lines; Q-32-2 closed) |

**Live stale cites (exactly seven, re-issued as superseded readings):**
`SKILL.md:715` → `:731-732` at `corpus/lessons/README.md:242`, `round-32.md:7`,
`round-32.md:41`, `round-32.md:55`; `SKILL.md:713-715` → `:729-732` at
`README.md:244`, `round-32.md:33`, `round-32.md:57`.

**Finding C09-F2:** a reissue built from A09's §2.4 prose grouping alone would
carry phantom rows (`:456-458`, `:522`, `:534-536`, `:710`, `:660` have no live
citer); this table is built from the line-level citation census (21 sites).
