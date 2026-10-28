# ScoutFrontier — round 76 W2

## Verdict

The committed registry supports the lesson's three-row delta and tier increments. The opened-source and frontier descriptions are consistent with the rows and committed evidence windows. Caveat: the files named `census-start.txt` and `census-end.txt` are validate receipts, not row-count census output; neither records the claimed start/end counts. Those counts are directly verifiable from the committed registry blobs, but the lesson's statement that the post-landing census appears in the round report is not yet evidenced at C landing (the committed `LOG.md` ends at round 75).

## Evidence

- `corpus/lessons/round-76.md:91-93` states 817 → 820, A +2/B +1, no prior row-cell changes, the calendar-announcement/archive lookup frontier, unread normative clause text, no `considerthese/`, and census follow-up.
- Registry row count: `corpus/SOURCES.md` at base `98c486bdb4650ba5b8e651d332910e8ee60ad121` has 817 source rows; at C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a` it has 820. The diff adds rows S894-S896 and Paths/search-log material; it removes no source-row content. This confirms +3 rows and that pre-existing rows were not edited.
- At C landing, S894 is tier A (dataset; archive era-name lookup), S895 tier A (official openstd registry record; expressly not normative clause text), and S896 tier B (Guangming Daily report; expressly not normative wording). All are `mined`, opened `2026-10-27`, recheck `180d`, and point `used-by` to `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`. Thus the tier delta is A +2, B +1, C +0. Each corresponding committed evidence file exists and is nonempty: `reports/round-76/evidence/S894.txt` (10,930 bytes), `S895.txt` (3,609 bytes), `S896.txt` (5,922 bytes). The amendment exists at the C landing.
- The frontier is grounded: S896 is the state-press announcement, S895 the official standard registry record, and S894 the archive's era-name lookup instrument. S895/S896 explicitly disclaim carrying the normative clause text, consistent with the lesson's caveat that clause text remains unread. No `considerthese/` path is present in the C-landing tree.
- `CORPUS.md:131-150` defines the manual census commands (row count, malformed rows, tier/status histograms, duplicate ids, enum/tier checks, and mined used-by path check). The committed `reports/round-76/telemetry/census-start.txt` and `census-end.txt` contain validation output (`W04`/`W01` warnings and `ok`/exit 0); end additionally has a command echo for `sources-census.sh validate`. They are not census row-count output and are effectively identical apart from that echo. No round-76 entry is present in `LOG.md` at C landing (its tail ends with round 75), so the lesson's promised round-report census remains to be evidenced later.

## Scope

Read-only verification of committed revisions; no live fetch, build, test, lint, formatter, or install was run. The row/tier counts above were derived from committed `corpus/SOURCES.md` blobs, not from a live census command.
