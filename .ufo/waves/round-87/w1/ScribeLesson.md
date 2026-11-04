# ScribeLesson — round 87 (w1), scoped findings

Seat: ScribeLesson (scribe, leaf member, no subagent dispatch). Axis: operability. Milestone: r87-v1. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Pins: base `83846a22ee1e9da7aa52ac505ccebf4455169247`; prefreeze controls `732c45394c73fcffd9fc623b939d446c7b11a9db`; frozen claims and counter `2a3b5643899c3520867ae930593cafef6ef19cad`.

## Scope and outputs

Drafted the round-87 lesson and a QUALITY criterion fragment about counterfeit non-readers and blanket refusals, grounded in the frozen prefreeze receipts. Both are drafts in my own stage. Nothing was filed, integrated or edited.

- `.ufo/waves/round-87/w1/stage/ScribeLesson/lesson-round-87-draft.md`: section-by-section draft (O scope correction, mistakes M1–M4, carried debts C1–C6, future bindings B1–B7, Gate left to a separate seat).
- `.ufo/waves/round-87/w1/stage/ScribeLesson/QUALITY-34-fragment.md`: proposed criterion 34, to be appended below 33 by L1. Four clauses: absence is not a counterfeit; counterfeit set frozen before claims; a kill is evidence only for its class; a counter that cannot parse candidate output fails closed with a receipt.
- `.ufo/waves/round-87/w1/stage/ScribeLesson/check34-draft.py`: draft read-only check over committed control receipts.
- `.ufo/waves/round-87/w1/stage/ScribeLesson/receipts/`: byte copies of frozen receipts and two author-side forgery files, with `SHA256S.txt` manifest.

## Findings

1. **O novelty is overstated in the frozen bounds text.** `claims.json` says acquisition is "a production CLI with the newly enumerated integrity relationships". The r86 stage checker `.ufo/waves/round-86/w1/stage/ExecCraftLedger/check-craft.py` (sha256 `b13f7338…9da6`, copied to `receipts/check-craft-r86-stage.py`) already checks fixed six-record population, duplicate ids, selected solution, conjecture promotion, translation clock and wording, and duplicate JSON keys. The real new work is a public `--packet/--json` CLI with a JSON findings shape, exit codes 0/1/2, and a population that is not fixed at six. Corrected here by text, with frozen bytes untouched. Confirmed against L1's note.

2. **Mistake M1 (able to fail, measured in r86).** The r86 absent-tool framing did not kill a present fake tool. The lane probe `.ufo/waves/round-86/w1/stage/CriticPredicate/probe.txt` reports `LEG PASS TOOL` and `ACCEPT-O-86: PASS legs=8/8` for `O-nonreader-fake-selftest-and-bare-registry`. This is a transport overlay on synthetic lands, not live-CLI evidence. Carried as QUALITY 34(i).

3. **r87 prefreeze controls kill the easy counterfeits.** Measured in the frozen receipts: the constant non-reader scores 3/12 (`receipts/constant-pass.json`, rc 1; passing cases `positive-six`, `unknown-explicit`, `reordered-records`); the blanket refusal scores 1/12 (`counter-selftest.json`); the absent tool scores 0/12 (`no-work.json`, `TOOL_ABSENT`). The "fails 12/12 target" claim is therefore not vacuous for these classes.

4. **Mistake M2 (survivor, not claimed away).** A filename-keyed non-reader that never opens the packet scores 12/12 against the frozen counter. CriticCounter's `filename-spoof.receipt.json` (rc 0) shows this; a label-echo forgery with invented record ids and `records=-999` also scores 12/12 (`all-labels-wrong-record.receipt.json`). Author-side repeat by ScribeLesson (see disclosure below): `receipts/forge-filename-keyed-measure87.json`, candidate sha256 `ef1fd47c…9334`, 12/12, rc 0. Consequence: O's 12/12 binds to the finite frozen battery, not to packet-sensitive correctness. The frozen counter's own selftest oracle reads expectations from fixture file names, which is the same mechanism.

5. **Mistake M3 (fail-open).** `findings: null` crashes the counter with a traceback and no aggregate receipt (CriticCounter `null-findings.receipt.json`, rc 1). Carried as QUALITY 34(iv).

6. **Question for L1, not decided (M4).** `no-work.json`, `constant-pass.json` and `counter-selftest.json` carry `/fast/scratch/hyaku/kotodama-r87/L1` in their `command` argv as `--work`. `measure87.py` and `controls/constant-pass.py` carry no scratch root. Whether a `--work` argv counts as "cited evidence" under QUALITY 31(ii) is a scanner-shape question. I did not run `tools/check-cited-records.py` and make no red or green call. Frozen bytes untouched.

7. **Timing (R86-C3).** `732c45394` adds the five control and counter files, all absent at base. `2a3b5643` adds only `claims.json`. Receipts carry argv, rc, stdout and digests, not wall-clock time, so "before declaration" is commit order only. Stated as such in the lesson.

8. **Draft check (`check34-draft.py`).** Green on frozen receipts: `COUNTERFEIT-KILL: PASS non-reader=3/12 rc=1 blanket-refusal=1/12`, exit 0. Red on a manufactured 12/12 non-reader receipt in scratch: `COUNTERFEIT-KILL: FAIL non-reader=12/12 rc=0 blanket-refusal=1/12`, exit 1. It does not see filename-keyed or label-echo forgeries, and the draft says so.

## Carried debts (preserved, not repaired, not all-green)

- **C1 (R86-C1):** no numeric 0–10 score asserted; freshness remains the lowest axis, paused by the round-11 L0 question.
- **C2 (R86-C2):** `measure87.py` is packet-only. It has no duplicate-source-id or empty-decision-cell leg. ExecAuditor's packet work does not repair these D-counter debts. R85-C2 remains partial.
- **C3 (R86-C3):** timing satisfied by commit order for round 87 only.
- **C4 (R86-C4):** L1 canonical planning versus the L2 planner-policy requirement is unresolved; disclosed, not waived.
- **C5 (R86-C5):** two scratch references in the unchanged non-author r84 spotcheck remain; not rewritten.
- **C6 (R86-C6):** S925/S926 same-page Wayback unresolved (429/403 with positive control, recorded as unavailability, not absence). S927/S928 inherited Wayback links not reopened here.

## Future bindings (exact)

- B1: any O sentence cites `reports/round-87/measure87.py` at `2a3b5643…` as "frozen finite battery 12/12" and names the filename-keyed 12/12 survivor. No reader takes 12/12 as anti-forgery.
- B2: production acceptance runs without `--candidate` on the committed production revision; the receipt records candidate sha256 and revision. L1 owns this run.
- B3: no sentence says the battery rejects counterfeits in general.
- B4: a future forgery-resistance claim freezes filename-keyed and label-echo forgeries before claims freeze (QUALITY 34(ii)). Not done in round 87.
- B5: a counter that crashes on candidate output fails closed with a receipt. Round 87's counter does not yet do so; recorded as a defect.
- B6: `check34-draft.py` filing under `tools/` and its citation in QUALITY 34 are L1 decisions.
- B7: pre-dispatch timing is stated as commit order, never execution time.

## Out of scope and not done

- No production change, no edit to `corpus/`, `reports/`, `tools/`, `SOURCES.md`, `QUALITY.md`, `LOG.md`, `SCORECARD.md` or any frozen counter or claim. No git or jj mutation, no index or commit. No task or delegation. No background jobs left running.
- No Source Gate row; no URL opened; no external source used.
- No promotion or admission claim.

## Extra executions disclosed (author-side, after lead asked to stop probing)

1. Draft `check34-draft.py` run twice in scratch (green on frozen receipts, red on manufactured 12/12), both before the lead's stop message. Exit 0 and 1 respectively.
2. The filename-keyed forgery run against `measure87.py` at `2a3b5643…` with `--candidate` (12/12, rc 0). It was launched just before the lead's "no further probes" message; the attempt to kill it failed (wrong tool used), and the job completed before any kill took effect. Its output was copied into my stage `receipts/` as `forge-filename-keyed-measure87.json` and `forge-filename-keyed.py`. Its `command` argv names my scratch `forge/work` path. L1 may delete both files if the disclosure is not wanted; they are not cited as freeze evidence.
3. Scratch `/fast/scratch/hyaku/kotodama-r87/ScribeLesson/` was removed after the last run. Confirmed by `rm -rf` output.

## Tooling

No installs, upgrades or updates. Read `/home/vgpnk/.omp/agent/RULES.md` before any action. No pacman transaction.

## Verification for the main agent (not run by this seat)

- Recompute the receipt hashes in `receipts/SHA256S.txt` against the frozen revision blobs (`git -C <lane> show 2a3b5643…:reports/round-87/<file> | sha256sum`).
- Run `check34-draft.py` on the frozen receipts (expected PASS 3/12, 1/12).
- Decide M4 with the cited-records checker, and decide whether the author-side forge receipts stay.
