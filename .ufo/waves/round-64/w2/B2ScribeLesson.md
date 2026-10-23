# B2ScribeLesson — Round 64 lesson draft

## Behavior and axes

Axes: coverage and calibration. Created the lesson skeleton at `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ScribeLesson/lesson.md`, following the four-heading shape of `corpus/lessons/round-63.md`. It records the three frozen claim predicates, the base revision, a Gate insertion point for 26 lines, six disposition-row re-open placeholders, a census/count section, and all four requested mistake classes. All unmeasured integration fields are explicitly `TBD-...`; no acceptance result is claimed.

## Findings

1. **Attempt-1 counter scripts:** read-only `git status --short -- reports/round-64` returned:
   ```
    M reports/round-64/accept-c.py
    M reports/round-64/accept-ca.py
   ?? reports/round-64/accept-o.py
   ?? reports/round-64/telemetry/census-start.txt
   ?? reports/round-64/telemetry/dry-run-o-baseline-copy.txt
   ?? reports/round-64/telemetry/dry-run-o.txt
   ?? reports/round-64/telemetry/final-measures-o.txt
   ```
   This confirms the three counter scripts were not committed in the observed worktree. QUALITY criterion 9 requires the pre-dispatch receipt to be committed with its declaration; the attempt-1 termination was not caught in time. The draft records this as R64-M1.
2. **Round-63 canonical log:** `corpus/lessons/round-63-verifier-spotcheck.md` §6 item 1 reports that the round-63 entry is in `corpus/LOG.md`, while root `LOG.md` is unchanged. Round-64 `accept-ca.py` declares the CANONLOG replay check; the existing `reports/round-64/telemetry/dry-run-ca.txt` records `CANONLOG FAIL` at the base, not a completed correction. Draft row R64-M2 distinguishes this from a successful final check.
3. **Round-63 SHONEN mapping:** verifier spotcheck §1, “SHONEN heading, one line per box,” states that only boxes 1–2 were answered; boxes 3–4 were unanswered. Draft row R64-M3 records the one-line-per-box protocol and the spotcheck as the detector.
4. **Attempt-1 coverage:** the wave taskcall declares 26 row IDs S718–S743. `accept-c.py` requires every row and exactly 32 appended rows total; its APPEND leg states the 643→675 count. The assignment records six missing rows after attempt 1; ROWS and APPEND are the closure rules that should catch an incomplete set. No final ACCEPT-C-64 run was performed by this seat.

## Evidence and provenance

Read the full `corpus/lessons/round-63.md` for the requested shape; read `corpus/lessons/round-63-verifier-spotcheck.md` §1 and §6; read `reports/round-64/accept-c.py` docstring (including APPEND), `accept-ca.py` docstring (including CANONLOG), `accept-o.py` docstring, the matching existing dry-run receipts, `corpus/SOURCES.md` Census note, and the round-64 wave-1 taskcall/report paths. Round-64 claims and changes are described as declared scope only; this seat did not establish final landed state.

Exact shell commands and outcomes:

- `mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ScribeLesson` — succeeded with no output.
- `git status --short -- reports/round-64` — output recorded verbatim above; read-only.
- No acceptance, test, lint, build, or source re-open command was run. Existing telemetry receipts were read, not rerun. No tools were installed.

## Touched surfaces and limits

- Created scratch draft: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ScribeLesson/lesson.md`.
- Created the explicitly requested report: `.ufo/waves/round-64/w2/B2ScribeLesson.md`.
- No product code, registry, counter, judge, or lesson in `corpus/lessons/` was changed. No commits, pushes, deploys, or mutating jj/git commands were made.
- Known limit: the Gate quotes, disposition re-open outcomes, final counts, measured revisions, final log/entry changes, and all three acceptance results remain for L1 to populate from committed final evidence. The report describes no verification beyond the reads and status command above.
