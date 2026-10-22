# CriticCriterion11 — attack on planned QUALITY criterion 11

Seat: KotodamaR53.CriticCriterion11 (critic, leaf). Axis judged: calibration.
Target: the planned criterion 11 as summarised in the dispatch ("every declared acceptance command must be shown before dispatch to exit non-zero on a scratch copy where each clause of its claim is false, reading the checked tool's own exit code, never a piped grep"). No ScribeCriterion11 draft existed under `.ufo/waves/round-53/build/` when this review ran, so the summary is the text under attack.

## Verdict

The idea is right and would have caught both historical defects. **The wording as summarised would not.** There are three defects in the wording:

1. "A scratch copy where each clause of its claim is false" reads as one copy where every clause is false. That copy is the base, and both round 52 and round 53 already committed a base run that exits 1 for that reason.
2. The rule does not say who splits the statement into clauses. If the author derives the controls from the checker's own legs, they are tautological and cannot catch round 51's defect.
3. "Before dispatch" is the part that actually carries the weight. Round 52 already ran per-clause controls, but only in its build wave after dispatch. Round 53 repeats that timing, so round 53 fails its own criterion.

All three are fixable defects, not tradeoffs. Corrected wording and a falsifier are given below.

## Strongest counterexample: round 53 against its own criterion

- The declaration commit `60f1d2a` lands only `claims.json`, `separability-manifest.json` and `telemetry/declaration-dry-run.txt` (`git show --stat 60f1d2a`). The instrument commit `a9cf95f` lands only the four tools.
- The only pre-dispatch "red" evidence for C is the base run in `reports/round-53/telemetry/declaration-dry-run.txt:52-56`. All four legs fail together:
  `COUNT FAIL knowledge_files=228`, `ENTRY FAIL`, `SWEEP FAIL exit=0 rows 228 files 228 missing_from_index 0 []`, `SIDS FAIL cited=0 bad=['entry absent']`, `exit 1`.
  - The SWEEP leg fails only because 228 ≠ 229. The sweep's own exit is 0, and `missing_from_index` is 0.
  - Nothing committed before dispatch shows that SWEEP goes red when an index row is missing, which is the exact R52-M3 class.
- `claims.json:66` (`red_before_rule`) says outright: "Before landing, the base is that copy". So the round's declared rule is the weak reading.
- The per-clause controls were dispatched as build-wave seats cloned at the declaration (`gen-build-spec.py:84` ExecCAcceptanceControls, `:96` ExecDCounterControls). That is after dispatch.
- Round 52 already did the same thing. `corpus/lessons/round-52.md:139` (R52-M3) is "caught by the build wave before landing; the declaration is frozen and was not changed". Its controls are at `.ufo/waves/round-52/build/ExecCAcceptanceControls.md:53-57` (a2–a6: README untouched or partly edited, acceptance exit 0) and `:109`.

**Consequences.** Per-clause controls are not new in round 53. What would be new is running them before the declaration freezes. A criterion 11 that lands in round 53 must not cite round 53 as complying with it, because that would be false provenance. It applies from round 54. If the L1 wants round 53 to comply, it would need to commit the controls before dispatch, which is too late now.

## (1) Would it have caught round 51 and round 52? Yes, but only under the per-clause reading

**Round 51, the directory-token defect** (`round-51-verifier-spotcheck.md:44-49`).

- D's acceptance was `sh -c 'test "$(python3 -B reports/round-51/boundary-count.py)" = 'rows=15 resolved=15 distinct=15''` (`reports/round-51/separability-manifest.json`, unit D).
  - It compares stdout and drops the counter's exit code through command substitution. That is not a pipe.
- The counter's `resolve()` accepts a `dir/` token (`reports/round-51/boundary-count.py:44-47`).
- I ran it on process-substituted copies of the entry. No file was written.

| copy | output | exit |
|---|---|---|
| base `bff83ba` entry | `rows=11 resolved=11 distinct=11` | 0 |
| round-51 tip `2b956d7` entry | `rows=15 resolved=15 distinct=15` | 0 |
| tip with one row's `numerals-and-measures.md:N` anchor replaced by `` `linguistics/` `` (the path:line clause alone is false; the row is still distinct and still resolves) | `rows=15 resolved=15 distinct=15` | **0** |
| tip with every file anchor replaced by `` `civilizations/` `` | `rows=15 resolved=15 distinct=1` | 1 (fails on distinctness only) |

- **Caught when:** the control falsifies the *form* predicate (`path:line`). The declared string test then still holds, so the control stays green when it should be red, and the defect is exposed before dispatch.
- **Missed when:** the author picks a mutation the counter already catches, such as an unresolvable `file.md:9999` or a duplicate target. Both of those also break the "resolves" or "distinct" clause.
- **The base already contained the counterexample.** The base table's last row is `` `civilizations/` regional entries `` (`git show bff83ba:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, section 2). Yet the before-value was `resolved=11`. A non-author applying the statement's words to the 11 base rows would have counted 10 path:line rows against the counter's 11. That before-value audit is cheaper than a mutant and needs no mutation design. It is added in the wording below.

**Round 52, the piped grep** (`round-52-verifier-spotcheck.md:53-57`).

- I re-ran the mechanism on the current lane (228 files). The README from round-52 tip `7cee23b` was process-substituted with the entry's index row removed, using the sweep's own `--readme` option.

  ```
  sweep own exit 1
  rows 227 files 228
  missing_from_index 1 ['linguistics/speech-surrogates-whistled-drummed.md']
  footer_live {"total": 228, ...}
  piped grep exit 0 PIPESTATUS 1 0
  ```

- `footer_live` always prints the live file count (`reports/round-28/readme/sweep.py:207`). So `grep -q '"total": 228'` is satisfied by the count clause alone, whatever the README says.
- A per-clause control ("index row removed, everything else true") makes the declared argv print `knowledge_files=228` / `C_SID_BAD 0` and exit 0. The control fails to go red, and the defect is caught.
- Under the all-false reading it is not caught. Round 52's committed base run (`reports/round-52/telemetry/declaration-dry-run.txt:14-16`) exits 1 at the first `&&` with `knowledge_files=227`. That already "exits non-zero on a copy where the claim is false". Its later legs never ran, the same short-circuit that criterion 9 names for absent lands.
- Round 51's C argv used `sweep.py >/dev/null &&` (correct). Round 52 rewrote it into the piped form. Per-clause controls also catch regressions of this kind when an instrument is rewritten. A syntax ban alone does not.

## (2) Committed bytes or re-execution?

**A closure can check these from committed bytes:**

- A control receipt exists for each declared command.
- It is in the tree of the declaration commit or an earlier one (ordering via `git log`).
- Each control names one clause, gives its mutation, runs the declared argv verbatim, and shows a non-zero exit whose output names that clause while the other clauses print as passing.
- The argv contains no status-dropping construct: an unguarded `|`, `$(…)`, `|| true` or `; true` around a checker. This is a static lint.
- Base-row audit: the before-value matches a count of the statement's predicate on the base rows.

**These need re-execution:**

- Whether the printed outputs are real.
- Whether the instrument that produced them is the declared one. For example, `accept-c.py` could have been edited between the controls and the declaration.

A receipt alone is author text. Criterion 8's "checks this from committed bytes" has the same weakness. The fix, matching criterion 10's `--selftest`:

- Commit each control as a replayable transform: a small patch or a `--selftest`-style fixture.
- Record the instrument's sha256 in the receipt.

The closure then checks presence and order from bytes, checks that the hash matches the declared instrument, and replays a sample of controls (seconds; the round-52 controls are a few file edits).

Deciding which clauses the statement makes is judgment, not mechanical. That mapping must be checked by a non-author seat before dispatch, which round 53's CriticClaimSizingC shape already provides, though after dispatch.

## (3) Conflicts with criteria 8 and 9

1. **Superseded reference.** Criterion 9 supersedes 8 (`QUALITY.md:35`). Criterion 11 should say "adds to criterion 9" and should not cite 8.
2. **Criterion 8's "runs once on its exact declared input" and "never substitute a different input after measuring"** (`QUALITY.md:33`).
   - Controls run the same argv on other trees. If they go into the criterion-9 receipt, that receipt no longer shows which run was on the declared input.
   - `dry-run.py check` reads `$ ` lines into a set (`reports/round-53/dry-run.py:69`), so duplicate argv lines pass silently, while a `--root <scratch>` variant shows up as `UNDECLARED_IN_RECEIPT` and fails criterion 9's two-way check.
   - **Fix:** controls go in a separate committed file (for example `reports/round-N/telemetry/red-controls.txt`) with a non-`$ ` prefix. Round 52 already used `$$` for non-declared commands (`reports/round-52/telemetry/declaration-dry-run.txt:26,31`). Run each control with the scratch copy as the working directory, so the argv stays verbatim. State that controls are negative tests, not measurements.
3. **Criterion 9's expected pre-landing result** ("an after-value comparison failing with the before value printed", `QUALITY.md:35`) is exactly the all-false base run. Criterion 11 must say that run does not count as a control. Otherwise criterion 9's own receipt satisfies criterion 11.
4. **No conflict with criterion 7.** Controls that need a stand-in landing (a synthetic entry, an S187 row, README bumps) live only in the scratch copy. Say so, so that a stand-in S-id is never read as a cross-claim citation.

## (4) Cheapest ways to satisfy it on paper without closing the class

1. **Use the base run as "the scratch copy"** (round 53's own `red_before_rule`). Every clause is false, the first leg fails, and nothing is learned about the rest.
2. **Derive the controls from the checker's legs, not from the statement's words.** Each leg catches its own mutation, so this is tautological. It cannot find a predicate the checker never implemented, which is round 51's case.
3. **Pick mutations the instrument already catches.** For round 51, an unresolvable anchor instead of a directory token.
4. **Red for the wrong reason.** ExecDCounterControls (e) "cite S187" goes red at the declaration only because no S187 row exists (`SID_BAD` = no row). It is not because "S187 or above" is checked. `d-count.py:72-73` tests only "row exists and used-by names the entry". After C lands, the same control could go green if the S187 row's used-by also named D's entry. Require the control's output to name the falsified clause.
5. **Declare hard clauses "review" to exempt them.** This is fine when honest; round 53's `method_not_statement` does it openly. It needs the non-author clause mapping in (2).
6. **Unreplayable receipt text,** or controls run against an instrument edited afterwards. Needs the transform plus sha256 from (2).
7. **Run the controls after dispatch** (rounds 52 and 53) and record them as compliance.
8. **Satisfy only the syntax ban.** Drop the pipe but keep another status drop, such as round 51's `test "$(…)" = …` or `|| true`. Or keep a correct exit read on a checker that tests a weaker predicate. The pipe ban is a symptom rule. The per-clause control is the real test.

## Wording fix (paste-ready, criterion-style, replaces the summary)

> 11. **Acceptance commands are shown able to fail, clause by clause, before dispatch** — adds to criterion 9. Before the declaration is committed, a non-author seat lists the predicates the claim statement names (a count, a path, a form such as `path:line`, an index row, a status, a used-by cell, distinctness); clauses the statement leaves to review are named as such. For each listed predicate, a scratch copy makes that predicate alone false while every other clause holds (a stand-in landing is allowed in the copy only), and the declared counting or acceptance argv, run verbatim from the copy's root, exits non-zero with output naming that clause. The base, where every clause is false at once, does not count as a control. Where the statement ranges over rows that exist at base, the before-value must match the predicate applied by hand to those rows. A pass reads each checking tool's own exit status or an exact match on its whole output: no unguarded pipe, `$(…)` or `|| true` around a checker. Controls are committed with the declaration in a separate receipt (`$$` prefix, so criterion 9's two-way check is unchanged), each as a replayable transform with the instrument's sha256; a closure checks presence, order and hashes from committed bytes and replays a sample. Controls run after dispatch do not meet this: a weak command found then is routed, not fixed. Grounded in R52-M3 at `corpus/lessons/round-52.md#mistakes` (build-wave controls a2–a6 caught the piped grep after the declaration froze) and the round-51 `path:line` ruling at `corpus/lessons/round-51-verifier-spotcheck.md:44-49` (one `dir/` anchor still prints `rows=15 resolved=15 distinct=15`, exit 0). First applies to round 54; round 53 ran its controls after dispatch.

Anchors checked: `corpus/lessons/round-52.md:133` is `## Mistakes`. The round-51 spot-check has no adjudication heading (its headings include `## Discernment spot-check` at :102), so the D ruling is cited by line range. If the 8-line budget binds, the first lines to cut are the sha256 clause and the base-row audit, in that order. Never cut the "alone false while every other clause holds" clause or the "after dispatch does not meet this" clause.

## Falsifier for the criterion

The criterion's closure check is too weak if it passes any one of F1–F3, or fails F4.

| id | input | criterion check must report |
|---|---|---|
| F1 | Round-51 declaration (`reports/round-51/*` at `2b956d7`) | No path:line control. Replaying the D argv on the one-row `linguistics/` mutant above exits 0. **Fail.** |
| F2 | Round-52 declaration (`147cfde` plus the round-52 declaration files) | No control receipt. Its only red is the base run, which stops at the first `&&`. The index-row control from the `--readme` replay above exits 0. **Fail.** |
| F3 | Round-53 declaration `60f1d2a` | Only the all-false base run, with SWEEP's own `exit=0` (`declaration-dry-run.txt:54`). The per-clause controls are post-dispatch build-wave reports. **Fail.** |
| F4 | A synthetic declaration: `accept-c.py` plus a committed control receipt with one transform each for count 230, entry absent with the count held at 229 by a second stand-in file, index row removed, an S-id below S187, a cited row that is absent, queued or rejected, a missing used-by, and no S-id cited. Each control goes red on its named leg, all are committed before the declaration, and the hashes match. | **Pass.** |
| F5 (mutation) | F4 with `accept-c.py` changed to pipe the sweep into a grep (`returncode` ignored) | The hash differs from the receipt. Replaying the index-row control exits 0. **Fail.** |

## Impacted axes

- **Calibration** (primary): a false "shown able to fail" on rounds 52 and 53.
- **Operability**: the cost of controls scales with the number of clauses. Stand-in landings are needed before dispatch, and stating "per predicate, not per instance" keeps the cost bounded.

## Evidence I ran (read-only; no file written except this report)

- `boundary-count.py --root . --entry <(git show …)` on the base, the round-51 tip and two mutants (the table above).
- `sweep.py --readme <(git show 7cee23b:corpus/README.md | grep -v speech-surrogates…)`, then the same command piped into `grep -q '"total": 228'` with `PIPESTATUS` printed.
- `git show --stat a9cf95f 60f1d2a`, and `git log` for the round-52 build-wave controls file, which landed in records commit `2eb489f`, after the declaration.

## Unrun checks

- I did not run the F4 or F5 synthetic declaration. That needs a sandbox, and ExecCAcceptanceControls is building the equivalent controls (b)–(f).
- `skill://godspeed` did not resolve under `~/.omp`, so I followed the inline godspeed instructions in the task.
- No tools were installed.
