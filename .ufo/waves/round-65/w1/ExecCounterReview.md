# ExecCounterReview

## Files changed
- `.ufo/waves/round-65/stage/counter-review.md` — read-only attack findings with paths, line ranges, minimal fixes, and smoke evidence.
- `.ufo/waves/round-65/w1/ExecCounterReview.md` — this handoff.
- No counter/source files were edited; no tools were installed.

## Behavior and exact retained evidence
- Fragment selftest: printed all ten checks PASS and `SELFTEST: PASS 10/10`.
- Coverage command: `ACCEPT-C-65: FAIL` at base, with missing entry/rows as expected; output included `RESTATE PASS ... lines=0` and `NOHARM FAIL diff=[]`.
- Filtered O command: printed SKIP lines, but `FRAG PASS ... scan_out=['FRAG: 0 finding(s) in 0 file(s)']` and `ACCEPT-O-65: PASS [filtered: 1/26 legs]`, contrary to the requested red result.
- Frozen `dry-run-o.txt` records `FULL FAIL ... skip=3`, `MUTEX FAIL ... exactness-sweep-o65.txt:not_committed`, and the same empty-scan FRAG PASS. The rows directory listing had no files. `controls-c.txt` was read; `controls-o.txt` and `exactness-sweep-o65.txt` were absent from the telemetry listing.

## Main findings
- O filtered mode can still return an acceptance PASS; FRAG passes on zero files; FULL rejects its child’s intentional skips. MUTEX does not check mutant subprocess return/verdicts.
- Fragment scanner silently skips non-`.txt` files and traversal errors, and does not reject invalid ROW IDs.
- C URL parsing has an uncaught malformed-port exception and HOSTS parsing can miss placeholder domains with userinfo; NOHARM only observes committed `main`. Accept-C emits the retained invalid-escape SyntaxWarning.
- Full details and minimal fixes are in the stage review.

## Risks / blockers
- FRAG and filtered O acceptance are false-green surfaces; FULL is an inevitable failure under its current skip condition.
- O control/exactness evidence is absent at this tip. No counter changes were made. No builds/tests/linters were run beyond the three explicitly requested smoke commands.
