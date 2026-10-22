# CriticCriterion11Text — falsify attack on QUALITY criterion 11 (uncommitted text)

Seat: `KotodamaR53.CriticCriterion11Text` (critic, leaf; no subagents). Date: 2026-10-22. Axis judged: calibration.
Item attacked: `corpus/QUALITY.md` criterion 11, the last paragraph of the working copy (`git diff -- corpus/QUALITY.md`: +2 lines, uncommitted). I read criteria 7 to 10 first.

## Verdict

The idea is sound, and the timing exemption for round 53 is honest. As worded, though, the criterion is not yet safe to land. Four of its own parts let a declaration comply on paper while keeping the defect class it is meant to close:

- **Round 51.** Under the current wording, the criterion would **not** have caught round 51's directory-token counter. A compliant author can choose a red-control edit that the counter already catches. I ran this below.
- **Round 52.** It **would** have caught round 52's piped grep, through both its syntax clause and an index-row control.
- **Clause choice.** It lists "a topic" as a clause that a command can check. That invites a weak stand-in predicate: a hollow two-line entry passes every C leg, including the topic leg that round 53's control "shows able to fail".
- **Committed bytes.** What it asks for cannot be checked from committed bytes. The clause list is never committed, the receipt is prose rather than a replayable script, and there is no green control.

It also mis-cites one grounding file. It carries no "shown able to fail" evidence of its own, unlike criterion 10. And it does not say that round 53 fails it or that round 53 is the third consecutive claim-sizing round, which the round-52 closure said trips the drift sentinel.

All of these are fixable wording defects, not tradeoffs. A paste-ready replacement is at the end.

## Checks run

All runs were on throwaway exports under `/tmp/ccrit11`, made with `git archive`. No lane file was edited apart from this report, and no tool was installed.

| # | Command (abridged) | Output | Exit |
|---|---|---|---|
| 1 | `git archive 2b956d7` (round-51 tip). Run D's declared argv `sh -c 'test "$(python3 -B reports/round-51/boundary-count.py)" = '\''rows=15 resolved=15 distinct=15'\'''` on the unmodified copy | `rows=15 resolved=15 distinct=15` | 0 |
| 1a | same, with the row anchor `` `numerals-and-measures.md:101` `` replaced by `` `linguistics/` `` (only the `path:line` form is false) | `rows=15 resolved=15 distinct=15` | **0** |
| 1b | same, with the anchor replaced by `` `numerals-and-measures.md:9999` `` | `rows=15 resolved=14 distinct=14` | 1 |
| 1c | same, with the anchor replaced by `` `no-such-file.md:1` `` | `rows=15 resolved=14 distinct=14` | 1 |
| 2 | `git archive 47ec825` (C landed). Gesture entry replaced by two lines (its own `- topic:` line plus `- sources: S187`), README row unchanged. Ran `python3 -B reports/round-53/accept-c.py` | `COUNT PASS` / `ENTRY PASS` / `SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []` / `SIDS PASS cited=1 bad=[]` | **0** |
| 2a | same hollow tree: `python3 -B reports/round-53/clauses.py --base-tree <a9cf95f export>` | `C1 PASS` / `C2 PASS topic_chars=375` / `C3 PASS` / `D1 PASS` / `D2 PASS` | **0** |
| 3 | `python3 -B reports/round-53/final-measures.py --tree <47ec825 export> --lane <lane> --base-tree <a9cf95f export>` | Controls from committed bytes: `D-red-3`, `C-red-4` and `C-red-5` each print `can't open file …/reports/round-53/clauses.py` and exit 2 (`CONTROL-FAILED`), because `clauses.py` is untracked. With the working-copy `clauses.py` copied in, all eight controls are `RED-AS-STATED`. | — |
| 3a | `C-red-3` (entry deleted) inside run 3 | `COUNT FAIL knowledge_files=228` / `ENTRY FAIL` / `SWEEP FAIL exit=1 rows 229 files 228` / `SIDS FAIL … ['entry absent']`, labelled `RED-AS-STATED` | 1 |
| 4 | `sweep.py --readme <README without the gesture row> \| grep -q '"total": 229'`, run without and with `set -o pipefail` | without pipefail: `PIPESTATUS 1 0`; with pipefail: pipeline exit 1. The sweep prints `missing_from_index 1 [...]`, and `footer_live {"total": 229, …}` still matches the grep | 0 / **1** |
| 5 | `grep -c "one new entry\|topic" .ufo/waves/round-53/build/CriticCriterion11.md` | `0` | — |
| 6 | `grep -n "drift sentinel"` over `corpus/lessons/round-53.md`, `corpus/QUALITY.md`, `SCORECARD.md`, `LOG.md` | no hits. The sentence exists at `corpus/lessons/round-52-verifier-spotcheck.md:57`: "so this is the second consecutive round. A third trips the drift sentinel." | — |
| 7 | `reports/round-53/dry-run.py:69` (read) | `seen = {line[2:] … if line.startswith("$ ")}`: the set holds command strings only, with no tree or working-directory identity | — |

Instrument sha256 at the time of the runs: `accept-c.py` d056a7f1…, `d-count.py` 618bb09e…, `final-measures.py` 2aced2f8…, `clauses.py` 2fff00da…. The last two are untracked.

## Answers to the assigned questions

**Is it grounded?** Partly.

- R52-M3 exists (`corpus/lessons/round-52.md:139`, under `## Mistakes` at `:133`).
- R53-M2 exists in the working-copy lesson (`corpus/lessons/round-53.md`, `## Mistakes`). Its text is the L1's rewrite, not ScribeMistake's draft. ScribeMistake's draft R53-M2 said "No third occurrence in round 53's own declaration" (`.ufo/waves/round-53/build/ScribeMistake.md` §2). The landed row says round 53's C "carries two clauses its acceptance `accept-c.py` does not check". The criterion depends on the landed version, so the draft must not be pasted anywhere.
- The criterion's evidence citation `CriticCriterion11.md` is wrong for "found two C clauses its acceptance did not check": that file has 0 hits for "one new entry" or "topic" (check 5). The finding is at `.ufo/waves/round-53/build/CriticClaimSizingC.md:12-13` ("**Yes: two clauses.** 'one new entry' and 'on co-speech gesture, pointing …' are not checked").
- The lesson row R53-M2 cites `CriticGapPremise.md` §5 for the same finding. §5 (`:130-140`) lists draft ids and the entry contract, not those two clauses.

**Would it have caught round 51?** Not as worded.

- The correct control, a `dir/` token in place of a `path:line` anchor, stays green (run 1a, exit 0), and that would expose the defect.
- The criterion lets the author pick the edit. A missing line or a missing file also makes the `path:line` clause false, and both go red "for that clause's reason" (runs 1b and 1c). A compliant receipt therefore exists that misses the defect.
- The syntax clause adds nothing here. Round 51's argv is a `$(…)` exact-match comparison, not a piped grep.

**Would it have caught round 52?** Yes, in two ways.

- An index-row control with every other clause true exits 0 under the round-52 argv, and the "never a piped grep" clause bans the argv outright.
- The ban as worded is narrow, though: "a piped grep that can match a line the tool always prints". A pipe into a grep that matches only the success line, or `$(…)`, or `|| true`, still drops the tool's status. `set -o pipefail` would have caught R52-M3 (run 4, exit 1). ScribeCriterion11's rationale, finding 2 ("`set -o pipefail` alone would *not* have caught it"), is false.

**Checkable from committed bytes?** No. Four pieces are missing:

- **The clause split is never committed.** A closure cannot tell a clause that was skipped from one that was never listed.
- **"Naming its edit" is prose.** It cannot be replayed, and nothing ties it to the instrument version.
- **There is no green control.** A command that always exits 1 and prints every leg FAIL passes every red control, because the "for that clause's reason" substring is present.
- **"The claim holds except for that one clause" is not visible in the receipt.** Round 53's own C-red-3 fails four legs at once and is still recorded `RED-AS-STATED` (run 3a), which is the same flaw the criterion names for the base run.

**Does it conflict with criterion 9?** Not in intent, but it collides with criterion 9's mechanics in two places.

1. Red controls run a declared argv verbatim on another tree. If they go into criterion 9's receipt, `dry-run.py check` cannot tell them from the declared-input run (check 7). The two-way check can then pass on a receipt that holds only scratch-copy runs. Meanwhile any clause tool that is not declared (such as `clauses.py`) shows up as `UNDECLARED_IN_RECEIPT`.
2. "Every clause names the command that checks it" does not say *declared*. A round can therefore check clauses with record tools added after dispatch, as round 53 did with `clauses.py`, which sit outside criterion 9 altogether.

There is a third, minor gap involving criterion 7. Pre-dispatch controls need stand-in landings, for example a synthetic S187 row. The text should say these stay in the scratch copy, so a stand-in id is never read as a cross-claim citation.

**Does round 53 satisfy it? Is "from round 54 on" honest or a loophole?** The timing exemption is honest: the declaration `60f1d2a` was frozen before the criterion existed, so it cannot comply retroactively. It still works as a loophole, for three reasons:

- **The scope is ambiguous.** "committed before dispatch from round 54 on" scopes only the timing. Nothing says round 53 fails the rest.
- **Round 53 does not meet the rest.** Its after-landing controls (`final-measures.py`) cover:
  - the C clauses for the README row, used-by, "one new entry" and topic;
  - D's FRAG, WROW2 and D1 legs.

  No control in that receipt covers:
  - C's S187 floor, the "is a row" check or `mined` status;
  - D's SID_BAD, WROW1 or the six OVER instances.

  The build-wave controls covered some of these after dispatch, but by the criterion's own words a clause with no control is "unverified, not passing".
- **The drift sentinel is never mentioned.** Round 53 is the third consecutive claim-sizing round. The round-52 closure said that trips the drift sentinel (check 6), and neither the criterion nor R53-M2 says so. Deferring to round 54 without that sentence lets round 53's records read as compliant.

**Cheapest paper compliance under the current text:**

1. **Split the statement along the checker's own legs.** Every control then goes red by construction.
2. **Pick an easy break instead of the nearest near-miss.** Runs 1b and 1c in place of 1a.
3. **Cover a content clause ("on X as method") with a weak stand-in predicate.** A topic-line regex, for example: the hollow two-line entry passes it (runs 2 and 2a) while C-red-5 is "red".
4. **Label a multi-clause break as a single-clause control** (C-red-3).
5. **Commit a prose receipt** with no script and no instrument hash.
6. **Dodge the literal "piped grep" wording** with `$(…)`, `|| true`, or a grep for a success-only line.
7. **Check clauses with tools that are never declared,** so criterion 9 never sees them.

## Findings

| id | sev | file:line | what the text says | what the evidence shows | fix |
|---|---|---|---|---|---|
| F1 | high | `corpus/QUALITY.md:39` | "a red control runs the command on a scratch copy where the claim holds except for that one clause (the wrong count, …)" | The author chooses the edit. Round 51's argv goes red on `numerals-and-measures.md:9999` (run 1b, exit 1) but green on `linguistics/` (run 1a, exit 0), so a compliant receipt misses the round-51 defect | Require the nearest near-miss for each form clause, a clause list checked by a non-author before dispatch, and the before-value audit (replacement text below) |
| F2 | high | `:39` | lists "a topic" among the clauses a command checks | A two-line entry passes `accept-c.py` and `clauses.py` C2 (runs 2 and 2a, exit 0), so C-red-5 "shows" a clause able to fail while the clause's meaning stays unchecked | Content clauses are listed as review-only and must never be covered by a stand-in predicate |
| F3 | medium | `:39` | "shows a non-zero exit for that clause's reason"; "each naming its edit and its exit" | There is no green control, and the substring test accepts multi-leg failures (C-red-3, run 3a). Prose edits cannot be replayed | Add a green control. Require that the clause's leg FAILs and every other leg PASSes. Commit a control script and the instrument sha256 |
| F4 | medium | `:39` | example edit "a second added file" | Adding a file alone makes the count 230, which falsifies two clauses and contradicts "holds except for that one clause". R53-M2 itself uses "a second added file plus a removed one" | "a second added file with an existing one removed, so the count still holds" |
| F5 | medium | `:39` | "never a piped `grep` that can match a line the tool always prints" | Too narrow: `$(…)`, `\|\| true` and success-line greps still drop the status. pipefail turns R52-M3 red (run 4) | "reads the exit status of every tool it runs: no pipe without `set -o pipefail`, no `$(…)` or `\|\| true` that hides a status" |
| F6 | medium | `:39` | "Every clause names the command that checks it" | `clauses.py` is a record tool added after dispatch and is outside criterion 9. Red-control `$ ` lines collide with `dry-run.py check` (`dry-run.py:69`) | "names the declared counting or acceptance command". Keep controls in a separate receipt without the `$ ` prefix |
| F7 | medium | `:39` | grounding cites "`CriticClaimSizingC.md`, `CriticCriterion11.md`" for the two unchecked C clauses | `CriticCriterion11.md` has 0 hits for either clause (check 5). The finding is `CriticClaimSizingC.md:12-13` | Cite `.ufo/waves/round-53/build/CriticClaimSizingC.md:12-13` only. Also correct R53-M2's `CriticGapPremise.md` §5 pointer |
| F8 | medium | `:39` | "committed before dispatch from round 54 on" | Says nothing about round 53. Round 53 lacks controls for the S187 floor, `mined`, SID_BAD, WROW1 and OVER1–6, and the drift sentinel goes unmentioned (check 6) | State that round 53 does not meet it and is the third consecutive claim-sizing round |
| F9 | medium | `:39` | no "shown able to fail" for the criterion itself | Criterion 10 carries its own red evidence (`:37`). Criterion 11 asks for red evidence and gives none | Commit runs 1a and 4 (plus the round-52 replay at `CriticCriterion11.md:52-58`) as a receipt and cite it |
| F10 | low | `reports/round-53/final-measures.py:145`, `clauses.py` | the round-53 controls rely on `clauses.py` | Untracked. On the committed tree `47ec825`, D-red-3, C-red-4 and C-red-5 exit 2 (`CONTROL-FAILED`, run 3). `telemetry/final-measures.txt` does not exist yet, though the lesson's source line names it | Commit `clauses.py`, `final-measures.py` and `tools/check-draft-ids.py` before writing the after-landing receipt that R53-M2 cites |

## Smallest safe correction (paste-ready replacement for the criterion 11 paragraph)

> 11. **Each claim clause is shown able to fail** — adds to criterion 9, which checks that the receipt and the declaration agree; this criterion checks that the declared commands can fail at all. The declaration lists each claim's clauses (a count, a path, a form such as `path:line`, an index row, a status, a `used-by` cell, "one new entry"), and a non-author seat checks the list against the statement's words before dispatch. A clause no command checks mechanically (a topic, "on X as method", what a source carries) is listed as review-only and is never covered by a weaker stand-in predicate such as a `- topic:` pattern. Each other clause names the declared counting or acceptance command that checks it, and that command reads the exit status of every tool it runs: no pipe without `set -o pipefail`, and no `$(…)` or `|| true` that hides a status. Controls run the declared argv verbatim from the root of a scratch copy. A green control is a copy where every clause holds, and there the command exits 0; a stand-in landing is allowed in the copy only and is never landed. A red control is one per mechanical clause: it changes that clause alone with the nearest near-miss, not an easy break (a `dir/` token for a `path:line` clause, not a missing file; a second added file with an existing one removed, so the count still holds), and the command exits non-zero, printing that clause's leg as failing and every other leg as passing. The base run does not count as a control: there every clause is false at once. Where the statement ranges over rows that exist at base, the before-value matches the predicate applied by hand to those rows. Check from committed bytes, before dispatch: the clause list in the declaration, the control script that builds each copy, its receipt in a file criterion 9's two-way check does not read (no `$ ` prefix), and the sha256 of each instrument it ran; a closure replays a sample. A clause with no control is unverified, not passing. Shown able to fail: round 51's D argv exits 0 with one anchor replaced by `linguistics/`, and round 52's C argv exits 0 with the index row removed (the sweep exits 1). Round 53 does not meet this criterion: its declaration `60f1d2a` carries only the all-false base run, its per-clause controls ran in the build wave and after landing, and its after-landing receipt has no control for C's S187 floor or `mined` status or for D's SID_BAD. It binds from round 54's declaration. Grounded in mistakes R52-M3 and R53-M2 (`corpus/lessons/round-52.md#mistakes`, `corpus/lessons/round-53.md#mistakes`): round 51's D counter and round 52's C acceptance could not fail on a clause their statements made, and in round 53 the build-wave critic found two C clauses `accept-c.py` does not check (`.ufo/waves/round-53/build/CriticClaimSizingC.md:12-13`). That makes round 53 the third consecutive round of the class, which the round-52 closure said trips the drift sentinel (`corpus/lessons/round-52-verifier-spotcheck.md:57`).

If length binds, cut in this order: the before-value sentence, then the sha256 clause. Never cut "changes that clause alone with the nearest near-miss", the green control, "review-only", or the round-53 non-compliance sentence.

Two companion fixes outside `QUALITY.md`, both for the L1:

- In R53-M2 (`corpus/lessons/round-53.md`, `## Mistakes`), replace `CriticGapPremise.md` §5 with `CriticClaimSizingC.md:12-13`, and append: "third consecutive round; the round-52 closure's drift sentinel trips (`round-52-verifier-spotcheck.md:57`)".
- Commit the receipt for "Shown able to fail" (runs 1a and 4 above) under `reports/round-53/telemetry/` before the criterion cites it.

## Limits

- I did not run the replacement text's controls on a synthetic round-54 declaration.
- The round-52 index-row replay was run on the current tree (229 files, gesture row). The round-52-tip variant is CriticCriterion11's measurement (`CriticCriterion11.md:52-58`), which I did not re-run.
- `skill://godspeed` was followed from the inline instructions in the assignment. No tool was installed or upgraded.
