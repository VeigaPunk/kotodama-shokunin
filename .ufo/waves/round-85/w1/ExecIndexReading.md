# ExecIndexReading — round 85

Axes: depth, operability, calibration. Base-only measurement; no production edits, new index tool, commits, installs or general tests.

## Pinned observation

Measured committed base `0d181583b18ae94e80a251ca5ab5f3055b16c74c`, tree `2370b0e80afa59485eef19f7ad24f6b19252285e`, materialized by read-only `git archive` in the seat's scratch directory. Frozen claims and measure85 were read with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show ed816e71a97dde9b65f9265276b77c7583274671:<path>`; their bytes are retained in stage. No clone or fixture commits were needed.

Executed assigned count: `python3 -B reports/round-28/readme/sweep.py --json` in the materialized base; exit **1**, full stdout and revision/tree/tool-digest header retained in `stage/ExecIndexReading/r28-base-receipt.txt` relative to this wave directory. Independently counted with Python pathlib plus a line-state H2/row parser and topic-field comparison (not importing r28); its complete observations are retained in `stage/ExecIndexReading/independent-reading-receipt.json`.

Partition order: linguistics / myth-symbol / culture-material / synthesis / verification / civilizations.

| Reading | Result |
|---|---|
| Files | **258**, vector **32/36/42/29/24/95** |
| Canonical rows | **251** |
| Supplemental rows | **2**, README lines 793–794: `conlang-scholarship.md`, `conlang-scholarship.amend-2026-10-23.md`; both uniquely resolve to linguistics |
| Effective rows | **253** (251 + 2), not 251 |
| Missing | **5**, listed below |
| Ghosts / topic mismatches / duplicates | **0 / 0 / 0** |
| Header drift | myth-symbol 32 → 36; culture-material 41 → 42 |
| Last totals line | line 834: 253 → 258 |
| Last counts footer | line 836: 253 → 258; vector 32/32/41/29/24/95 → 32/36/42/29/24/95 |

Missing paths (relative to `corpus/knowledge/`):
- `culture-material/maritime-seafaring-lexicon.md`
- `myth-symbol/guest-right-hospitality-law.md`
- `myth-symbol/marriage-alliance-bridewealth.md`
- `myth-symbol/ordeal-judicial-proof-rituals.md`
- `myth-symbol/witchcraft-sorcery-accusation-institution.md`

Canonical row counts: linguistics 30, myth-symbol 32, culture-material 41, synthesis 29, verification 24, civilizations 95. Linguistics reaches 32 only with its two historical supplemental rows; those are not missing and must not be added again.

## Important calibration correction

An index checker already existed. Moreover, the frozen claim's first-footer characterization is stale against the actual committed base parser: `reports/round-28/readme/sweep.py:118` already selects `matches[-1]`; line 179 selects the last totals line, and lines 85–100 / 131–138 classify and resolve supplemental rows. Its real receipt reads the **253** footer, not the historical **243** footer. README lines 824–825 likewise describe older behavior, not these parser bytes. Main and ExecIndexAuditor were notified. The successor still adds explicit root/error CLI, duplicate-failure semantics (duplicates are measured but omitted from `ok` at lines 209–212), and independent subprocess selftest coverage. No frozen target was changed.

## Integration artifacts

All below reside in `.ufo/waves/round-85/w1/stage/ExecIndexReading/`:

- `index-reading.json`: exact drift, row topics, source hashes, old/new heading cells, separate candidate-D metadata.
- `README-APPEND.md`: paste once at EOF; five missing rows with verbatim entry topics, new last totals line **258**, new dated footer **258 / 32/36/42/29/24/95**. No existing rows, totals history or footer blocks are changed. The rows are supplemental and uniquely owner-resolved, matching existing r28 behavior. Do not add repeated partition headings: r28 stores sections by partition and repeated headings replace earlier sections.
- `candidate-D-row.json`: separate **proposed**, not final-topic-attested metallurgy row; deliberately absent from base repair. The D entry was not available in stage at drafting. At integration use its final `- topic:` text verbatim, not an unverified paraphrase. If D is the only new file, counts become **259 / 32/36/43/29/24/95**, culture-material header **43**. This conditional increment does not describe base bytes.
- `r28-base-receipt.txt`, `independent-reading-receipt.json`, `base-sweep.py.txt`, `frozen-claims.json`, `frozen-measure85.py`: retained evidence and measured input bytes.

Only L1 should apply these precise canonical heading replacements:

| Base line | Literal old | Literal new (base-only repair) |
|---|---|---|
| 376 | `## myth-symbol/ (32)` | `## myth-symbol/ (36)` |
| 410 | `## culture-material/ (41)` | `## culture-material/ (42)` |

Leave every historical footer and historical row byte-exact. A new totals line at EOF supersedes 253 without changing its historical line. Counts must reflect the final integrated corpus, including D if landed; do not append a 258 footer after a 259 population.

## Risks and handoff

No general tests/build/lint/formatters or live-lane fixture-writing gates were run. L1 should run the successor auditor on the final integrated root, its isolated selftest and frozen O counter, and confirm historical footer blocks remain byte-exact. Final D row is conditioned on its actual topic bytes and population. No LSP interface is exposed in this seat; this Markdown/data-only analysis required no symbol refactor. No tool installed or upgraded. The full scratch export is removed after evidence retention.

Self-evaluation: accuracy 4 (pinned bytes and independent agreement; candidate D explicitly not final-topic-attested); completeness 4 (base repair complete, D integration remains conditional by scope); clarity 4 (canonical/supplemental split explicit); actionability 4 (paste-ready append and exact heading cells, final integrated count still L1-owned); conciseness 4 (retained evidence avoids reprinting long topics). Overall 4.0; highest-impact handoff is choosing 258 versus 259 from the integrated file population. User-agreement check: base findings are measured; no green repaired-index result is claimed.
