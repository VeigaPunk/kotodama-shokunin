# ReviewerO94 — grader v5 correctness review (2026-11-05)

## Status: BLOCKED — no candidate delivered in the Contract bound

Waited, bounded, per Contract loop for
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/DONE`
(45 iterations of `sleep 60`, service `watch_grader_done`, ~20 min wall, exit 1 = ABSENT).
`ExecGraderV5/` was never created in
`.ufo/waves/round-94/w1/stage/` while sibling seats (ExecBattery94, ExecMutants94,
ExecAdjacency94, ScoutLullaby94, ScribeLesson94, ConnectorLullaby94) all landed DONE.
Therefore: no diff.txt, no changes.md, no candidate bytes, no selftest of the candidate,
no regression diff, no mutant run, no integrate verdict on substance. Claim O has no
reviewed candidate from this seat.

## What was completed while waiting (baseline, all re-runnable)

1. **v4 base bytes pinned**: `git -C <lane> show e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2:tools/check-advance-evidence.py > <scratch>/prep/v4-base.py`; `sha256sum` → `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` rc 0 (matches claims.json O.before_tool_sha256); 1609 lines.
2. **v4 selftest baseline**: `python3 -B v4-base.py --selftest --work <scratch>/st-v4base` → rc 0, `SELFTEST PASS 114/114`, 114 lines beginning `  ok` (count via `grep -c "^  ok"` = 114). Full check-name list captured in `<scratch>/prep/v4-selftest.out` (deleted with scratch; the names are re-derivable with the same command).
3. **Re-attack harness built and validated against v4** (`stage/ReviewerO94/reattack.py`, imports the frozen `reports/round-93/battery93.py` and re-points only `TOOL`): reproduces the v4-before state exactly —
   - A1 (Cyrillic О U+041E in `LОCATED`): rc 0, PASS legs=9/9 (survivor) ✔ matches claims O.before
   - B1 (soft hyphen `LOCA<U+00AD>TED`): rc 0, PASS legs=9/9 (survivor) ✔
   - G1 (`## 1. address` … `## 5. Rites`): rc 0, PASS legs=9/9 (survivor) ✔
   - H1 (manifest row value a list): rc 2, `ADVANCE-EVIDENCE_ERROR: manifest rows is not a JSON object (list where mapping expected)` — note: in my H1 build the top-level `rows` is a list; the claims' H1 (row *value* a list, S955 → JSON list) produced the v4 AttributeError traceback at :710 per CriticClaims93; both shapes must refuse named under v5
   - I1 (new row 4 cells): rc 1 **TRACEBACK** `IndexError: list index out of range` ✔ unnamed on v4, must become a named refusal on v5
   - J1 (`S001 NOT–LOCATED` en-dash U+2013): rc 1, FAIL `APPENDONLY` — wrong-direction parse confirmed (line asserts NOT-LOCATED, tool reads LOCATED and flags a flip) ✔
   - K1 (lowercase `S001 located` unanchored prose): rc 0, PASS legs=9/9 (survivor — the `dispo-any-casei` evasion channel live on v4) ✔
   - G0 control: rc 0 PASS legs=9/9 (clean stays clean) ✔
   Command: `CAND=<tool> python3 -B stage/ReviewerO94/reattack.py <scratch>/reattack-<v>` rc 0.
4. **Recipes read from frozen sources**: `corpus/lessons/round-93.md:94` (routed mutant pins: html_body_text unit checks for script/style/comment/entity, dispositions lowercase unit check, base-row `opened` fixture) and `.ufo/waves/round-93/w1/CriticClaims93.md:66-76` (Smallest safe corrections for A1/B1/G1/H1/I1).

## Findings

- **blocking (process)** — ExecGraderV5 never dispatched: claim O cannot pass its regression/mutation/re-attack legs without the candidate; BLOCKED filed.

## Residual risk and verification gaps

- None of the seven fixes or five mutant pins were reviewed — no candidate exists to review.
- The harness above is staged in my stage dir; whoever reviews the candidate later can rerun it verbatim: `CAND=<candidate.py> python3 -B <stage>/ReviewerO94/reattack.py <scratch>`; expected after v5: A1/B1/G1/H1/I1/J1 rc≠0 with a named LEG or ADVANCE-EVIDENCE_ERROR diagnostic and no `Traceback`, K1 refused, G0 rc 0 PASS 9/9.

## Tooling record

No installs or upgrades (none needed); no pacman transactions; no sysctl changes; no writes outside my stage dir; no git mutations (one read-only `git show`).
