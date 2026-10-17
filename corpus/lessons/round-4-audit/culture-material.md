# Round-4 audit — culture-material (all 16 entries)

- role: AUDIT; corpus entries and triage ledgers read-only
- checked: 2026-10-17
- revision audited: `c610e0abd8edf90d6c6d86ebebdc7a7cba8d4a0b`; the partition had no working-tree diff during inspection
- scope: every `corpus/knowledge/culture-material/*.md` entry; ledger lookup across `corpus/lessons/*triage*/`
- canon status: NON-CANON reference-apparatus audit only; lore-shokunin owns canon

## Result and counting rules

**15 PASS; 1 entry with a defect; 1 finding.**

| Check | Result |
|---|---|
| Entries audited | 16/16 |
| Header fields (`topic`, `sources`, `couples`) | 48/48 present and populated; 0 missing/empty fields |
| Calibration section | 15/16 present; 1 missing section (CM-A01) |
| Unbased claim flags | 0 |
| Remaining claim flags | 3 occurrences representing 2 distinct claims, supported by 2 existing triage rows |
| Raw `to-verify` inventory | 4 occurrences on 4 lines; includes 1 generic reminder, not a claim flag |

A blank opening `- sources:` line followed by a populated indented source list is not an empty field. Calibration is checked as a section containing status/limits, not merely the occurrence of the word. A labelled inline bullet alone is recorded separately rather than silently treated as a section. Both ordinary `(to-verify)` and the extended parenthetical `(to-verify — …)` are claim flags. A generic instruction to flag future uncertainties is not a factual claim.

## Per-file results

File names below are relative to `corpus/knowledge/culture-material/`. Header evidence gives the starting line of `topic / sources / couples`; every listed field has non-placeholder content. A source block may continue below its opening line.

| File | Verdict | Header lines | Calibration evidence | Claim-flag audit |
|---|---|---|---|---|
| adornment-body-codes.md | PASS | 3 / 4 / 5 | §8, lines 93–100 | 0 |
| architecture-settlement-lexicon.md | PASS | 2 / 3 / 4 | §8, lines 125–132 | 0 |
| calendar-festival-systems.md | PASS | 3 / 4 / 19 | §10, lines 145–157 | 0 |
| costume-semiotics.md | PASS | 2 / 3 / 4 | §8, lines 108–119; also §1 | 0 |
| craft-artisan-lexicon.md | PASS | 3 / 4 / 13 | §11, lines 136–148 | 0 |
| cuisine-food-lexicon.md | PASS | 3 / 4 / 20 | §9, lines 143–157 | 0; line 175 is a generic reminder (see below) |
| dress-through-eras.md | PASS | 3 / 4 / 5 | §1, lines 7–11; §12 debunk shelf, lines 135–147 | 1 occurrence, ledger-backed |
| era-periodization-models.md | PASS | 3 / 5 / 16 | §12, lines 119–126 | 0 |
| garment-lexicon-crosslinguistic.md | PASS | 3 / 4 / 5 | §8, lines 108–116 | 0 |
| material-culture-inference-method.md | PASS | 3 / 4 / 15 | §5, lines 76–86 | 0 |
| music-instrument-lexicon.md | PASS | 3 / 4 / 5 | §7, lines 101–109 | 0 |
| ritual-garments.md | PASS | 3 / 5 / 14 | §9, lines 142–150 | 2 occurrences of 1 claim, ledger-backed |
| sumptuary-law-rank-display.md | PASS | 2 / 3 / 4 | §9, lines 92–99 | 0 |
| textile-technology.md | DEFECT — CM-A01 | 3 / 4 / 5 | No calibration section; inline calibration bullet at line 29 | 0 |
| trade-economy-lexicon.md | PASS | 3 / 4 / 5 | §9, lines 145–153 | 0 |
| warrior-material-culture.md | PASS | 3 / 4 / 13 | §7, lines 93–102 | 0 |

## Finding

**CM-A01 — missing calibration section: `corpus/knowledge/culture-material/textile-technology.md`.**

The entry's seven section headings (lines 7, 15, 31, 53, 69, 76, 89) organize gates, fibers, dyes, looms, finishing, vocabulary, and an application checklist. None is a calibration section. Line 29 does contain a substantive `- Calibration:` bullet limiting the Harappan silk identification; other uncertainties are scattered in prose/table cells (for example, lines 28, 36–38, 41, 84, 87). This is not an absence of calibration language or all calibration content. It is the missing section required by this assignment. No entry was edited to address it.

## Existing ledger support for every remaining claim flag

Ledger paths below are relative to `corpus/lessons/`. Decisions are quoted from existing rows, not new triage decisions by this audit.

| Entry / current line | Flag summary | Existing row naming the flag | Existing disposition / basis |
|---|---|---|---|
| dress-through-eras.md:56 | Sideless surcoat “gates of hell” / French “porte/fenêtre d'enfer”: primary sermon text not located | `round-1-triage/C4.md:24` | DOWNGRADE; row names the file, sobriquet, and missing primary sermon locus, records costume-history witnesses, and retains the narrowed flag |
| ritual-garments.md:109 | Brazil purple-mourning association: only popular/funeral-industry material found | `round-2-triage/C12.md:16` | DOWNGRADE; row names the Brazilian claim, states that no scholarly study was located, and explicitly retains the marker |
| ritual-garments.md:150 | Calibration-summary repetition of the same Brazilian purple-mourning claim | `round-2-triage/C12.md:16` | Same supporting row; ledger lines 8 and 39 explicitly account for two occurrences of this one claim |

`corpus/knowledge/culture-material/cuisine-food-lexicon.md:175` says “flag every to-verify item before it approaches the bible.” This is a generic handoff instruction, not an unresolved factual proposition, so it needs no claim-specific ledger row. This explains the difference between four raw marks and three claim-flag occurrences. Both unresolved claims remain unresolved; ledger support is not factual confirmation.

## Verification and limits

The unchanged read-only gate was run with:

```sh
python3 tools/gates/provenance-audit.py corpus/knowledge/culture-material
```

Exit code: **0**. Final output: `INFO scan: files=16 marks=4 mark-lines=4 findings=0 blocked=0`.

A supplemental read-only Python check, consuming entries in windows of at most 120 lines, independently confirmed 16 files, 48 populated fields, 15 files with calibration/debunk section headings, 4 raw marks, and 3 parenthetical claim marks. Header blocks and calibration sections were inspected in chunked reads; each remaining claim was matched to the specific ledger row above. `git diff --stat -- corpus/knowledge/culture-material` was empty.

The gate result does not override CM-A01: `tools/gates/provenance-audit.py:19–23,90–93,323–326` accepts calibration vocabulary/labels without requiring a section; lines 31–35 and 328–329 count raw marks without auditing their ledger basis. Its topic check at lines 303–305 also checks presence only, so this audit separately checked all topic values for emptiness. No gate was modified or weakened.

This is an apparatus/ledger-coverage audit, not a fresh verification of every real-world citation or historical assertion. Existing ledger bases were inspected locally, not revalidated against their external sources. The only file written is this report; corpus entries, ledgers, tools, and `LOG.md` remain untouched. Any batch logging required by `AGENTS.md` is left to the integrator because this worker may write only the assigned report.
