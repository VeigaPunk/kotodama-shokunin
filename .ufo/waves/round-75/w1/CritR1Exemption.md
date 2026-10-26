# CritR1Exemption — round 75

## Verdict

The drafted exemption is too broad as a predicate: “inside the status, recheck or used-by cell” identifies a location, not an allowed semantic change. This review assesses the draft leg text; `reports/round-75/accept-ca.py` is not present yet, so no counter execution or implementation behavior is claimed. No tools installed.

Evidence: draft `claims.json` Ca legs APPENDONLY/R1EXEMPT; draft C legs ROWS/CENSUS. `corpus/SOURCES.md` states that status/recheck/used-by changes must each be logged old→new in a round lesson and defines mined as cited by `used-by`. Census contract/script: `sources-census.sh` E01 requires NF=13, E07 validates status enum, E09 accepts `NNd`, E11 checks paths only for mined rows; warnings do not fail validation. The CENSUS leg invokes `validate`, not `overdue`. C’s ROWS requires every pre-existing row byte-identical, but that is a separate claim/counter—not a Ca-only safeguard. `COMBINED` does not state that accept-c.py is run at Ca lands/combined head as a Ca leg.

## Counterexamples

### (a) Used-by payload smuggle — missed by Ca as drafted

Edit a pre-existing queued row’s used-by cell to add a nonexistent path, `../../reports/round-75/ledger.json`, or `https://evil.example/claim`. APPENDONLY exempts the cell by location. Census E11 is not applied to queued rows; for mined rows E11 checks only filesystem existence, and a traversal resolving to an existing file can pass. C’s `check-cited-lines.py` checks S-id scope in knowledge lines, not registry used-by payloads. C ROWS would catch a changed pre-existing row if C is run on that same tree, but does not make the Ca APPENDONLY predicate safe and is not a stated Ca-only check.

**Patch:** Require each changed used-by token to be a normalized, repository-relative `corpus/knowledge/*.md` path that exists in the graded tree; reject URLs, absolute paths, `..` components, duplicates, and non-path payloads. For a mined row, require used-by to correspond to actual citing source lines; require each changed value’s old→new pair in the round lesson. Do not treat mere cell location as sufficient.

### (b) 180d→1d across rows — missed as aggregate drift

Every `180d`→`1d` edit is individually inside recheck. The census accepts `1d` under E09, and validate does not test due status; only the separate `overdue` mode reports dates/cadences. No draft Ca leg bounds aggregate changes or checks the overdue queue. Thus the whole registry’s cadence meaning can change while every edited row is individually exempt.

**Patch:** Add a frozen, explicit permitted-change set (row id + old cadence + new cadence + lesson location), and reject any recheck-cell diff not in that set. At minimum require every changed cell’s old→new to be logged in the lesson, as the existing SOURCES contract requires; do not infer that a syntactically valid cadence is an authorized change. This catches bulk drift without declaring every single cadence update illegitimate.

### (c) queued→mined — missed by Ca alone; C ROWS is conditional defense

A pre-existing queued row changed to mined with used-by `—` has a valid status. Census emits W03 (“mined but unused”), which is warning-only and does not fail validation; no Gate/provenance is required for pre-existing rows by the drafted Ca legs. If the same tree is graded by C’s ROWS leg, its “every pre-existing row is byte-identical” catches the edit. That is not an independent Ca-only guarantee, and the C leg is not identified as the catch for Ca’s exemption.

**Patch:** Specify that status changes are exempt only when their old→new transition is listed in a frozen allowlist and the lesson records it; queued→mined must additionally have a located Gate record and real used-by citations (or be disallowed in-place, requiring a newly opened row). Make the same-tree C ROWS check an explicit combined acceptance requirement if relying on it.

### (d) Whitespace / NF — stated construct impossible; adjacent pipe mutant needs fail-closed rule

Whitespace alone cannot change a row’s number of pipe delimiters (and therefore NF). A literal whitespace-only change may still alter bytes, but cannot produce the specified NF change. The adjacent realistic mutant—insert a pipe into a cell—changes NF; census validate emits E01 (NF!=13) **if** CENSUS is run. But C’s CENSUS is separate from Ca, while Ca APPENDONLY does not itself require valid cell count before granting the exemption. A Ca-only landing therefore has no specified census defense. A leading-indentation change to four spaces can also make the census parser ignore a row (the parser accepts 0–3 spaces); no canonical row-count assertion is in the cited CENSUS leg.

**Patch:** In APPENDONLY, require both old and new lines to parse as exactly 11 cells (NF=13), and require equality of every non-exempt cell by index; fail closed on any parse ambiguity or changed delimiter/indentation. If the intended attack is strictly whitespace-only, state that it cannot change NF and test a separate inserted-delimiter case.

## Fixture bytes constructed

All rows below are literal one-line registry fixtures, using the lane’s 11-cell shape. `S004`’s original row is copied from the base `corpus/SOURCES.md`; the following are proposed mutated bytes (one mutation at a time):

```text
| S004 | Grambank v1.0, https://github.com/grambank/grambank | dataset | A | grammatical feature design and family-level constraint | README “Grambank v1.0” heading and How to cite section | global structural-feature dataset in Glottobank, CC-BY-4.0 CLDF; cite the original paper plus release DOI; usable as design space and bibliographic record | queued | 2026-10-19 | 180d | ../../reports/round-75/ledger.json |
| S004 | Grambank v1.0, https://github.com/grambank/grambank | dataset | A | grammatical feature design and family-level constraint | README “Grambank v1.0” heading and How to cite section | global structural-feature dataset in Glottobank, CC-BY-4.0 CLDF; cite the original paper plus release DOI; usable as design space and bibliographic record | queued | 2026-10-19 | 1d | — |
| S004 | Grambank v1.0, https://github.com/grambank/grambank | dataset | A | grammatical feature design and family-level constraint | README “Grambank v1.0” heading and How to cite section | global structural-feature dataset in Glottobank, CC-BY-4.0 CLDF; cite the original paper plus release DOI; usable as design space and bibliographic record | mined | 2026-10-19 | 180d | — |
| S004 | Grambank v1.0, https://github.com/grambank/grambank | dataset | A | grammatical feature design and family-level constraint | README “Grambank v1.0” heading and How to cite section | global structural-feature dataset in Glottobank, CC-BY-4.0 CLDF; cite the original paper plus release DOI; usable as design space and bibliographic record | queued | 2026-10-19 | 180d | — |
```

The fourth line is byte-identical in cells and has NF=13; it illustrates that whitespace-only alterations cannot change NF. An inserted `|` (not a whitespace-only change) yields NF≠13 and should be a distinct fail-closed fixture.

**Impacted axes:** calibration (Ca APPENDONLY/R1EXEMPT soundness); coverage only indirectly through C ROWS/CENSUS interaction. Smallest safe action is to tighten the exemption predicate as above before freezing; do not claim the fixtures demonstrate behavior of a counter that is not yet present.
