# Round 5 — scoped source follow-up and runnable verification (2026-10-17)

source: LOG.md round-5 admission entry; reports/round-5/flash-claims.json, dispatch.json, parent-reconciliation.json, parent-source-spotchecks.json, validation.json and battery-mutation.json
verified-at: 2026-10-17; parent reran python3 reports/round-5/run-validation.py, exit 0, F=true and O=true
recheck: rerun that acceptance command after changing the current ledgers, craft CLI or battery; preserve historical source ledgers, frozen manifests and original corpus bytes

The operator authorized Z.ai GLM-5.3 Flash after the native non-flash alias
was rejected before launch. One actual 16-worker native batch completed;
existing identities were continued for schema cleanup, repairs and bounded
re-review. The non-flash zero-launch receipt is retained, not relabelled as
Flash work. Count with `python3 -c 'import json; d=json.load(open("reports/round-5/dispatch.json")); print(d["workers"],d["completed"],d["actual_executed_batches_after_authorization"])'`
→ 16, 16, 1. The saved alias is `zai-coding-plan/glm-5.3-flash-low` (legacy
name, host-documented MAX thinking); upstream wire identity and simultaneous
runtime concurrency were not independently instrumented.

## Domain lessons

| Evidence distinction | Worldbuilding consequence | Bounded evidence |
|---|---|---|
| Support date versus image/use date | Date the bark support and pretreatment result separately; do not infer the era of painting, ritual performance or depicted dress from the support alone | Solís et al., DOI 10.1017/RDC.2020.71, publisher-deposited abstract; parent spotcheck 1 |
| Kin term versus social institution | A borrowed or cross-cutting term does not establish a matching marriage, descent or residence rule; keep the social-system claim separate | Lowie, Chapter V of Gutenberg #49153; parent spotcheck 3; KIN-A07 retains unread compound residuals |
| Avoidance register versus synonym list | Functional expressive replacement can use a smaller vocabulary and many-to-one mappings; do not build a one-to-one taboo dictionary from an expressive-scope statement | Haviland quoting Dixon 1971:437–438; parent spotcheck 4; original Dixon pages not independently read |
| Earlier thesis versus later book | Record the version actually inspected; relevant earlier case evidence does not verify a later edition's exact argument or every succession | TIB-A12/TIB-A16 follow-ups and parent reconciliation |
| Venue metadata versus causal endorsement | Correct bibliography without upgrading a contested diet/bite-configuration explanation to settled fact | PHON-A11; Science 363(6432):eaav3218, DOI 10.1126/science.aav3218; bibliography-only appended erratum |
| Bounded witness absence versus global origin claim | An unnamed she-wolf in an inspected witness does not prove that a name never appeared elsewhere or establish its modern origin | Zhoushu 50 opening account; parent spotcheck 5; TURK-06 remains unresolved |

Freshness improved through follow-up, not marker deletion. The acceptance
command counts **22 raw rows / 20 original questions / 17 retrieved rows /
five parent checks**. Companion rows do not create additional original
questions. Raw worker labels (13 supported, eight unresolved, one
contradicted) are not whole-claim confirmations. Parent reconciliation
conservatively keeps **five scoped supported / 15 unresolved / zero
whole-claim contradicted**. Four parent checks concern non-bibliographic
content; the passage threshold does not depend on counting venue metadata
as prose. The 15 residuals remain a worklist, not failures erased from history.

## Operability lessons

- `python3 tools/check-gate-battery.py` now gives a standalone entry point
  for seven legacy selftests in a disposable copied tree. The prior
  supplemental parent runner already isolated those tests; this is not a
  claim that isolation was first invented here. Its default actual run is
  seven passes, exit 0, original byte hashes and path set preserved.
- `python3 tools/check-gate-battery.py --selftest` passes ten controls.
  A recognized stable child failure is exit 1; missing/crashing/timed-out
  or unclassifiable children are exit 2. A Python traceback veto prevents
  an earlier FAIL line from laundering a later crash into a genuine finding.
  Five old assert-based gates can still have genuine failures classified
  conservatively as could-not-evaluate, never green.
- `python3 tools/check-craft-exercise.py --selftest` passes ten domain
  mutations and 18 real CLI subprocess cases. All six originally declared
  malformed controls now return stable exit-2 diagnostics without tracebacks;
  positive example, existing-report read, counts, foreign cwd and genuine
  domain finding/exit 1 remain exercised. Reviewed nested/argument cases are
  not proof of arbitrary malformed-schema safety.
- `python3 reports/round-5/run-validation.py` also reproduces both historical
  round-3 manifests, seven of seven rows each, and reruns the previous
  acceptance assertions in an isolated input copy. Expected red stays red:
  D2 still has 20 findings, not a whole-culture clearance.

## Gate

Candidates: F (historically lowest axis, freshness) and O (operability),
declared before the authorized dispatch in `flash-claims.json`. F required
at least ten original unresolved-question follow-ups, three new relevant
passages and three parent re-fetches. O required the standalone seven-gate
battery, six malformed cases normalized from traceback/exit 1 to typed
exit 2, preserved positive/domain checks, both frozen replays and the older
acceptance assertions. Commands and exact tested code hashes are in
`validation.json`.

Admitted: both measurable claims verify. Every-axis verdicts are freshness
improved, operability improved, calibration improved as an unclaimed
observation, depth unchanged, coverage unchanged and adjacency unchanged.
No tested axis was harmed; this does not certify all untested behavior.

Rejected or limited candidates: whole-claim promotion from nearby facts,
catalogue-as-content, edition conflation, treating worker support counts as
independent confirmations, arbitrary-schema safety and whole-culture
clearance. Prior numbered round-2/round-4 rejections remain historical.
The earlier non-flash alias rejection earns no completed-round credit.

Spot checks: five parent source re-fetches with locators and access limits;
real CLI calls; seven actual copied-tree selftests; both pinned replays;
positive and genuine-finding craft runs; previous acceptance; final bounded
review by existing worker 15. `battery-mutation.json` records a scratch-copy
veto-removal mutant rejected by CTRL-MARKER-THEN-CRASH while the original
10/10 selftest stays green. These are author-side readings/reviews, not
independent non-author promotion verification.

## Limits and next work

- Coverage remains 179 knowledge entries in six partitions. The civilization
  partition has 92 bases plus two source maps, not 94 verified civilizations.
  `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  reports 592 raw marker-bearing lines and 598 raw occurrences; markers were
  not erased or used as a scholarship-quality score.
- The battery is not an OS sandbox. Byte equality is not a no-write proof;
  it trusts child exit 0 and does not repair legacy parsers, fixture writes,
  assert-based failure conventions or independent-expected-value debts.
  Craft LAW-ORDER early-return coverage and declared-count metadata remain
  limited; the frozen example still contains a historical scratch command.
- Intermediate ledger-schema and parent negative-probe errors, review
  findings and the caught recursive-selftest repair mistake are retained in
  `integration-attempts.json` and executor/reviewer reports. The reviewer
  observed 428 historical /tmp craft-selftest directories, unchanged by final
  runs; they were not swept outside this child-only write scope. Parent's
  PID-only check found no matching live selftest process. Worker 12 reported
  cleaning its own stray root temporary files; no independent claim of
  zero outside writes ever is made, and no such files are shipped.
- No lore receipt, cultural permission, rank move, canon or shared-fleet
  closure is claimed. The final report stays inside this child repo by the
  operator's scope rule; full corpus-header, numeric-rubric and expected.json
  conformance debts remain explicit.
- Pending numbered sequence: two more Z.ai Flash 16-worker rounds (6–7),
  two OpenCode Go DeepSeek v4.1 Flash 32–64-worker rounds (8–9), then the
  requested exact-model Grok 4.7 xhigh fast 128-worker round (10).
