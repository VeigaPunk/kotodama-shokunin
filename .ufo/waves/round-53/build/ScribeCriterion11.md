# ScribeCriterion11 — QUALITY criterion 11 draft

Seat: `KotodamaR53.ScribeCriterion11` (leaf scribe). Assigned item: draft QUALITY criterion 11 for `corpus/QUALITY.md` — every declared acceptance command must be shown, before dispatch, to exit non-zero on a scratch copy where its claim is false for each clause the statement makes, and its pass must read the checked tool's own exit code, never a piped grep.

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (branch main). Date: 2026-10-22. No subagent dispatched. No tool installed.

## Behavior

Read `corpus/QUALITY.md` criteria 1–10 in full, the two named lessons, the round-52 acceptance-control report and the round-51 counter, then drafted one criterion paragraph in the house style (bold title, em-dash rule, `Check:`, `Grounded in`). The draft is below, ready to paste after criterion 10 (`corpus/QUALITY.md:37`; the file ends there today, 37 lines).

## Drafted text, ready to paste

Paste as one list item after `corpus/QUALITY.md:37`; the eight lines below are the eight physical lines of the item (continuation lines indented three spaces, as criteria 1–5 do):

```
11. **Acceptance commands are shown able to fail** — before dispatch, every declared acceptance command is shown to exit non-zero on a
   scratch copy where the claim holds except for the clause under test: the wrong count, the index row removed, a cited row missing its
   used-by. A pass reads the checked tool's own exit code, never a piped grep. Check: a closure reads committed bytes — the declaration
   dry-run receipt plus the red-control receipt, one control per clause, each naming the falsifying edit and its non-zero exit; a
   command with no red control is unverified, not passing. Adds to criterion 9, which checks that receipt and declaration agree both
   ways; 11 checks that the commands the receipt records can fail at all. Grounded in round 51's D defect and round 52's R52-M3 — two
   rounds running (`corpus/lessons/round-51-verifier-spotcheck.md:44-49`, `corpus/lessons/round-52-verifier-spotcheck.md:53-57`,
   `corpus/lessons/round-52.md:139`).
```

### Why each clause is in the draft

- **Before dispatch, on a scratch copy, one clause at a time.** The scratch copy must hold the claim true except for the clause under test, or the control proves nothing: at base the whole claim is false (the land is absent) and every acceptance command exits 1 for the wrong reason. The clause-level controls are what found R52-M3, and they were built on a synthetic tree before landing (`.ufo/waves/round-52/build/ExecCAcceptanceControls.md` §3, controls (a)–(g): the state that satisfies the claim, then one edit per clause).
- **The three falsifiers named** are the clauses the round-52 and round-53 statements actually make: a count clause (files 228 → 229), an index clause (the README index row), a citation clause (a cited `SOURCES.md` row whose `used-by` names the entry).
- **"The checked tool's own exit code, never a piped grep."** The R52-M3 cause was exactly the pipe: `sweep.py | grep -q '"total": 228'` took grep's status, and the pattern also matched sweep's live `footer_live` line, so `set -o pipefail` alone would *not* have caught it — grep still exits 0 on the live footer line (`.ufo/waves/round-52/build/ExecCAcceptanceControls.md` §5, measured `sweep exit: 1`, `grep -q exit: 0`). Reading the tool's own exit code is strictly stronger than pipefail, and this is the wording that closes the defect.
- **Closure reads committed bytes.** Two receipts, both committed: the declaration dry-run receipt (the declared acceptance argv and its expected pre-dispatch exit) and the red-control receipt (one control per clause, each naming the falsifying edit and the non-zero exit). No re-running is implied; a command with no red control counts as unverified, not as passing.
- **Adds to criterion 9, does not supersede it.** Criterion 9 is a completeness rule about the receipt and the declaration agreeing both ways (`corpus/QUALITY.md:35`). Criterion 11 is a falsifiability rule about the commands that receipt records. A receipt can be complete and still record a command that cannot fail — that is the round-52 case exactly: the C acceptance argv was in the receipt and matched the declaration, and it still passed a false claim.
- **Grounding, both rounds.** Round 51's D defect is the predicate half: the counter's `resolved` test accepted a `dir/` token, so the count could not fail on the statement's `path:line` clause (`corpus/lessons/round-51-verifier-spotcheck.md:44-49`; `corpus/lessons/round-51.md:129`). Round 52's R52-M3 is the transport half: the acceptance could not fail on the README-index clause because the pipe dropped the sweep's exit code (`corpus/lessons/round-52-verifier-spotcheck.md:53-57`; `corpus/lessons/round-52.md:139`). Same class, two rounds running: the closure already called the repeat "the second consecutive round" and said a third trips the drift sentinel (`corpus/lessons/round-52-verifier-spotcheck.md:57`).

## Evidence (file:line, re-read at the lane worktree)

- `corpus/QUALITY.md:29` (criterion 6), `:31` (7), `:33` (8), `:35` (9, "supersedes criterion 8"), `:37` (10) — style template: one bold title, em-dash rule, `Check:` where a checker exists, `Grounded in` a lesson, and criterion 9's own supersession sentence as the precedent for saying how a new criterion relates to an older one.
- `corpus/lessons/round-51-verifier-spotcheck.md:44-49` — "**Ruling on D's `path:line` clause.** … the counter's `resolved` test accepts a `dir/` token, so it checks a weaker predicate than '`path:line`' … The statement was wider than its own measure from the moment it was declared." Also `:123` (routed defect 1, "D statement wider than its counter").
- `corpus/lessons/round-51.md:129` — "the counter's 15 is 14 `path:line` rows plus one directory row (RerunDCounter F1)".
- `reports/round-51/boundary-count.py:11` (docstring: "`dir/` names an existing knowledge directory") and `:46-47` (the branch that returns the directory) — the acceptance measure that could not fail the statement's clause.
- `corpus/lessons/round-52-verifier-spotcheck.md:53-57` — "On a scratch copy of head with the entry's README index row removed, the declared C acceptance still prints `knowledge_files=228`, `C_SID_BAD 0` and exits 0 … The cause: `grep -q '"total": 228'` also matches the live `footer_live` line, and the pipe drops the sweep's exit code." Lines 55–56: every clause of the statement re-derives at head with one plain command each; the declaration was frozen, not narrowed after landing.
- `corpus/lessons/round-52-verifier-spotcheck.md:57` — "This class repeats from round 51 (D's statement wider than its counter), so this is the second consecutive round. A third trips the drift sentinel."
- `corpus/lessons/round-52.md:139` — mistake R52-M3 row: the piped acceptance, the cause, the fix ("the next declaration must gate on the sweep's exit status"), and the open cell "Not yet shown able to fail as a rule" — the gap criterion 11 closes.
- `.ufo/waves/round-52/build/ExecCAcceptanceControls.md` §3 (control table: (a)–(g), each control's exit code; (a2)–(a6) exit 0 while `sweep.py` exits 1) and §5 (the two independent reasons the acceptance cannot see a stale README; the measured `grep -q exit: 0` on the `footer_live` match).
- `reports/round-53/claims.json` — `red_before_rule`: "each acceptance command is run on a scratch copy with the claim made false and shown to exit non-zero for the stated reason"; `dry_run_rule`: "QUALITY criterion 9: … its check mode compares receipt and declarations both ways". The round's own red-control set is enumerated in `reports/round-53/final-measures.py` (docstring: D-red-1, D-red-2, C-red-1 README index row removed, C-red-2 used-by emptied, C-red-3 entry deleted) — the three clause kinds in the draft.
- `reports/round-53/telemetry/declaration-dry-run.txt` — the pre-dispatch receipt shape: `$ <argv>`, output, `exit <n>`, `# role: …; expected pre-landing: …`. The C acceptance exits 1 pre-landing with `COUNT FAIL knowledge_files=228 required=229`.

## Result

One criterion paragraph drafted, in house style, eight physical lines. It states the rule (per-clause red control before dispatch), the check (committed dry-run receipt plus red-control receipt; no red control means unverified), the relation to criterion 9 (adds a falsifiability requirement; does not supersede the two-way receipt check), and the grounding (round 51's D defect and round 52's R52-M3, two rounds running). `corpus/QUALITY.md` was not edited: it is a records land owned by the L1 (`reports/round-53/claims.json` `records_not_claims`), and this seat writes only its own report.

## Gates

- Style match against criteria 6–10 read at `corpus/QUALITY.md:29-37`.
- Clause coverage checked against the three clause kinds the round-53 statements make (`reports/round-53/claims.json` claims D and C, `falsifier` fields) and against the round-52 control set.
- Non-supersession of criterion 9 stated in the text itself; criterion 8 is left as criterion 9 already superseded it.
- Closure route is committed-bytes-only; no re-run of any lane command was performed or needed for the draft.

## Touched surfaces

- Wrote: `.ufo/waves/round-53/build/ScribeCriterion11.md` (this file) — the only file created in the lane.
- Read only: `corpus/QUALITY.md`, `corpus/lessons/round-51-verifier-spotcheck.md`, `corpus/lessons/round-51.md`, `corpus/lessons/round-52-verifier-spotcheck.md`, `corpus/lessons/round-52.md`, `.ufo/waves/round-52/build/ExecCAcceptanceControls.md`, `.ufo/waves/round-51/falsify/RerunDCounter.md`, `.ufo/waves/round-51/falsify/ReviewQuality8.md`, `.ufo/waves/round-51/build/ScribeQualityCriterion.md`, `reports/round-51/boundary-count.py`, `reports/round-53/claims.json`, `reports/round-53/separability-manifest.json`, `reports/round-53/accept-c.py`, `reports/round-53/dry-run.py`, `reports/round-53/final-measures.py`, `reports/round-53/telemetry/declaration-dry-run.txt`, `~/.omp/agent/RULES.md`.

## Out of scope

- Editing `corpus/QUALITY.md` (L1's land), landing the criterion, editing `corpus/lessons/round-53.md`, any `SOURCES.md` row, any knowledge entry.
- Building a checker for criterion 11 (no tool was specified, and the criterion's check is receipt-reading).
- Re-running any declared command: the receipts are the evidence and the role forbids decorating the report with re-runs.

## Findings

1. **A receipt can be complete and still record an unfalsifiable command.** Round 52's C acceptance argv was in the declaration and matched the manifest, so criterion 9's two-way check was satisfied, and it still passed a false claim (`corpus/lessons/round-52-verifier-spotcheck.md:53-57`). Criterion 9 checks the receipt's coverage; it does not check that the recorded command can fail. That is the gap criterion 11 fills, and it is why 11 must be stated as an addition to 9, not a replacement.
2. **`set -o pipefail` would not have caught R52-M3.** The pattern `'"total": 228'` also matches sweep's live `footer_live` line, so grep exits 0 on a stale README and the pipeline exits 0 even under pipefail (measured in `.ufo/waves/round-52/build/ExecCAcceptanceControls.md` §5). The criterion's wording ("the checked tool's own exit code, never a piped grep") is therefore deliberately stronger than the round-52 lesson's suggested fix (`corpus/lessons/round-52.md:139`).
3. **The clause-level control must be built on a tree where the claim otherwise holds.** A pre-dispatch control on the base tree only shows the land is absent (the round-53 receipt's `COUNT FAIL`/`ENTRY FAIL`), which is not a clause test. Round 52's controls had to synthesise the claim-true state first (`ExecCAcceptanceControls.md` §3), which is why the draft says "the claim holds except for the clause under test".
4. **Round 51's D defect is the same class from the other side.** The counter's `resolved` predicate accepted `dir/`, so the printed 15 could not fail the statement's `path:line` clause; the defect was measured only by re-reading the entry, not by any command (`corpus/lessons/round-51-verifier-spotcheck.md:47-49`). Criterion 11 turns that class into a mechanical pre-dispatch requirement.
5. **Open for the L1's decision (author-lane advice, not a defect).** The draft says *before dispatch*. Round 53's own clause-level red controls are enumerated to run on the landed tree (`reports/round-53/final-measures.py`), while its pre-dispatch receipt shows only the wholesale-false base state. If the L1 wants criterion 11 to be satisfiable by this round as declared, *before landing* is the word that fits; the round-52 control method (synthetic claim-true tree, one edit per clause, pre-dispatch) is what makes *before dispatch* achievable at all, and it is already the lane's demonstrated practice.

## Unrun checks

- No declared command was executed: no `d-count.py`, `accept-c.py`, `dry-run.py`, `final-measures.py`, `check-claim-separability.py` or `claims-agree.py` run. Every number quoted here comes from a committed receipt or a committed report read at the cited line.
- `python3 -B reports/round-28/readme/sweep.py` was not run; the sweep's exit behaviour is quoted from the round-52 control report, not re-measured.
- The draft was not pasted into `corpus/QUALITY.md` and no renderer or linter checked it; the eight-line shape was counted by hand on the drafted block.

## Tooling

No installs or updates were performed; none was needed. Tools used: `read`, `grep`, `glob`, `write`, one `bash` call for a line count and a heading grep (`grep -n "^[0-9]*\. \*\*" corpus/QUALITY.md`, `wc -l corpus/QUALITY.md` — both read-only). No `pacman`, no `uv`, no `npm`, no `jj`; no git command that writes was run in the lane.

## Artifact paths

- This report: `.ufo/waves/round-53/build/ScribeCriterion11.md` (lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`).
- Drafted text destination when the L1 lands it: `corpus/QUALITY.md`, after line 37.
- Referenced artifacts: `corpus/lessons/round-51-verifier-spotcheck.md:44-49,123`; `corpus/lessons/round-51.md:129`; `corpus/lessons/round-52-verifier-spotcheck.md:53-60`; `corpus/lessons/round-52.md:139`; `.ufo/waves/round-52/build/ExecCAcceptanceControls.md`; `reports/round-53/claims.json`; `reports/round-53/final-measures.py`; `reports/round-53/telemetry/declaration-dry-run.txt`.
