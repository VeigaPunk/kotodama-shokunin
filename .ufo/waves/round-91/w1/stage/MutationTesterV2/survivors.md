# New-mutation survivors (v2 entry mode, round 91)

7 of 16 new mutants survived the v2 tool's own 77-check selftest
(measured 2026-11-05, command `python3 -B runner.py`, rc 0; runner in scratch).

Six are fixture gaps. `newids-cited-closure-off` is an EQUIVALENT mutant:
`scoped` is built as `new_ids` filtered by `in cited`, so
`set(qualifying) <= set(cited)` is always true and the removed arm can never
fire on any input. It is not a coverage gap; it is dead hardening.

A surviving mutant is a coverage finding: the selftest has no fixture that
notices the removed sub-check. It is not permission to change the contract.

## newids-status-off

- Detector output: `selftest rc=0 first='SELFTEST PASS 77/77'`
- Check weakened: NEWIDS arm `status != mined`. A cited, tier-A, opened-today, entry-named row with a non-mined status cell still qualifies.
- Kill fixture idea: cite a new row whose status cell reads `rejected` with tier A, opened as_of and used-by naming the entry; expect FAIL NEWIDS `not mined`.

## newids-cited-closure-off (EQUIVALENT)

- Detector output: `selftest rc=0 first='SELFTEST PASS 77/77'`
- Check weakened: NEWIDS arm `qualifying ids not cited`. Unreachable by construction (`scoped` is a subset of `cited`); no fixture can kill it.
- Kill fixture idea: none. Dead arm; remove it rather than fixture it, or keep it as a guard whose input space is empty.

## gate-missing-line-entry-off

- Detector output: `selftest rc=0 first='SELFTEST PASS 77/77'`
- Check weakened: GATE arm `no lesson line with id and quote`. An entry-mode qualifying id with no gate line at all is never tested.
- Kill fixture idea: round lesson carrying gate lines for S011 and S012 only, S010 absent; expect FAIL GATE `no lesson line with id and quote`.

## capture-fetched-date-off

- Detector output: `selftest rc=0 first='SELFTEST PASS 77/77'`
- Check weakened: CAPTURE arm `fetched_at date != as_of`. No fixture re-opens a capture fetched on any other day, in either mode.
- Kill fixture idea: manifest `fetched_at` of `2026-11-03T19:00:00-03:00` (day before as_of) with an otherwise valid capture; expect FAIL CAPTURE `fetched_at date`.

## capture-traversal-off

- Detector output: `selftest rc=0 first='SELFTEST PASS 77/77'`
- Check weakened: CAPTURE arm `not relative and confined`. Absolute or `..` capture paths are never fixture-tested.
- Kill fixture idea: manifest capture `reports/round-90/evidence/../sneak.txt` or an absolute path; expect FAIL CAPTURE `not relative and confined`.

## topic-anchor-table-off

- Detector output: `selftest rc=0 first='SELFTEST PASS 77/77'`
- Check weakened: TOPIC phrase-anchor text source, table-cell half. Every fixture's anchored phrases also sit in h2 headings, so table cells add nothing the fixtures can see.
- Kill fixture idea: entry whose fourth phrase (`table`) appears only inside table cells and in no h2 heading; expect FAIL TOPIC `phrase anchors`.

## graded-sources-autoinclude-off

- Detector output: `selftest rc=0 first='SELFTEST PASS 77/77'`
- Check weakened: CAPTURE graded set. The lesson, lands-registry and entry bytes are auto-included in `graded_shas`. The byte-copy fixture survives only because it also passes the lesson through `--graded corpus/lessons/round-90.md`; the auto-include arm is never isolated.
- Kill fixture idea: entry-mode run with `--graded` listing only `corpus/SOURCES.md`, and a capture that byte-copies the lesson file; expect FAIL CAPTURE `byte-copies a graded file`.
