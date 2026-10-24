# Round 65 counter review (C / O / fragment checker)

Scope: read-only review of `reports/round-65/accept-c.py`, `reports/round-65/accept-o.py`, and `tools/check-row-fragments.py`. No counter was edited.

## Smoke evidence

- `python3 -B tools/check-row-fragments.py --selftest` printed all ten named checks as PASS and `SELFTEST: PASS 10/10`.
- `python3 -B reports/round-65/accept-c.py --root . 2>&1 | tail -15` ended `ACCEPT-C-65: FAIL` at the data-free base: FILE, ROWS, ONEID, APPEND, NOHARM, SWEEP, and LIVE fail; RESTATE/HOSTS/LINK pass vacuously or on empty input. The missing entry and all 26 registry rows explain the intended red result. The base receipt `reports/round-65/telemetry/dry-run-c.txt` has the same result. `controls-c.txt` records the old/new RESTATE and duplicate-URL controls; its new run also emits the SyntaxWarning noted below.
- `python3 -B reports/round-65/accept-o.py --root . --only FRAG` printed SKIP for the other selected-counter legs, but printed `FRAG PASS selftest=exit0 scan=exit0 scan_out=['FRAG: 0 finding(s) in 0 file(s)']` and `ACCEPT-O-65: PASS [filtered: 1/26 legs]`. This is contrary to the requested filtered red signal. The rows directory exists but the directory listing contains no files. `dry-run-o.txt` also records `FRAG PASS ... 0 file(s)` and FULL/MUTEX failures at base.

## Defects / false-green paths

1. **Filtered runs can still claim acceptance.** `reports/round-65/accept-o.py:430-445,1235-1242`: `legs` contains only selected legs; `all(legs)` may therefore be true, while the `[filtered: ...]` suffix is informational. The observed FRAG-only run exits through the PASS branch. Minimal fix: make filtered invocations diagnostic-only/non-accepting (nonzero and `FAIL`), or require an unfiltered complete run before an acceptance PASS.

2. **FRAG accepts an empty scan.** `reports/round-65/accept-o.py:1208-1224` accepts scan exit 0 plus a `0 finding` substring, without requiring scanned files or the expected fragment set. `tools/check-row-fragments.py:99-105,271-279` returns a clean result for an existing directory containing no `.txt` files. The observed `0 file(s)` result becomes FRAG PASS. Minimal fix: require and count the expected fragment set (at least nonempty; preferably the claim's exact expected rows), and fail on missing inputs.

3. **FULL is impossible to pass as written.** `reports/round-65/accept-o.py:1120-1131` invokes a child filtered to CORE/EDGE/TOOL/DRIP/MUT, which intentionally omits FULL/MUTEX/FRAG; the child prints SKIP for those legs through `leg()` at 441-443 and 1134-1226. FULL nevertheless requires `not skip_lines`. The frozen `dry-run-o.txt:27` confirms `FULL FAIL ... skip=3`. Minimal fix: use an explicit recursion/selected-leg protocol and validate the exact expected skip set, rather than requiring zero skips from a deliberately filtered child.

4. **MUTEX does not validate mutant-run completion.** `reports/round-65/accept-o.py:1170-1181` receives `xc`/`xe` from each mutant subprocess but never checks them, the child’s final ACCEPT line, or traceback/crash output. It judges only extracted FAIL names. A crashed or otherwise unsuccessful child that emitted the expected lines before failing can be counted as valid evidence. Minimal fix: require the expected child exit/verdict and no traceback, and ensure the selected leg output set is exact in addition to comparing failures.

5. **Fragment traversal can silently omit inputs.** `tools/check-row-fragments.py:102-105` silently ignores every non-`.txt` file; `os.walk` has no `onerror`, so unreadable subdirectories can also be skipped without a finding. Together with the empty-directory case, this can produce a clean scan without checking all supplied fragments. Minimal fix: enumerate/validate allowed files and expected paths, and surface traversal errors.

6. **Malformed fragment row IDs are not rejected.** `tools/check-row-fragments.py:121-127` sets `sid` only when `ROW_RE` matches; it does not report a failed match. An 11-cell ROW with an invalid/missing `S…` identifier proceeds through the other checks and can pass. Minimal fix: add a finding and stop processing unless `ROW_RE` matches.

7. **Malformed URL ports are mishandled inconsistently.** `reports/round-65/accept-c.py:128-142` catches `urlsplit` errors but reads `parts.port` at line 136 without catching `ValueError`; a nonnumeric/out-of-range port can terminate the counter instead of producing a failing leg. `tools/check-row-fragments.py:53-64` catches the same port error and silently drops the port, potentially treating an invalid URL as its valid host/path. Minimal fix: validate port parsing explicitly and report malformed URLs as findings in both paths; do not normalize an invalid port as absent.

8. **HOSTS can be bypassed by URL userinfo.** `reports/round-65/accept-c.py:343-355` derives host by splitting the raw URL, not parsing its hostname. For example, `https://user@example.org/path` yields `user@example.org`, so it does not match the `example.org` placeholder list. Minimal fix: use `urllib.parse.urlsplit(url).hostname` (and fail malformed inputs) for placeholder-host comparison.

## Ambiguities / evidence dependencies

9. **NOHARM observes committed `main`, not the candidate worktree.** `reports/round-65/accept-c.py:379-384` compares `BASE` to the hard-coded `main` ref and only under `corpus/knowledge`; staged, unstaged, and untracked candidate changes are not represented by that comparison. Its base output is `NOHARM FAIL diff=[]`. If acceptance is intended after committing the candidate onto `main`, state that precondition; otherwise compare the candidate tree/worktree and include untracked files. Also clarify whether unrelated changes in the other declared lands (`corpus/SOURCES.md`, `corpus/README.md`) are supposed to fail this leg.

10. **Checker label requirements are underspecified.** `tools/check-row-fragments.py:81-93,156-164` recognizes VERIFY/CAPTURE/ACCESS labels but never requires or validates them; BULLET is checked only if nonempty. If these are required source/verification evidence in each fragment, the current scan allows them to be absent. Minimal fix: specify and enforce the required label set, or document these labels as informational.

11. **SyntaxWarning in accept-c.** `reports/round-65/accept-c.py:97-100` has `\w` in a non-raw docstring. The frozen `controls-c.txt:11-12` captures Python's `SyntaxWarning: "\w" is an invalid escape sequence`. Minimal fix: make the docstring raw or escape the backslash. This warning did not prevent the observed smoke run, but is avoidable output noise.

## Missing O artifacts at this tip

The telemetry directory listing contains `dry-run-o.txt` but not `controls-o.txt` or `exactness-sweep-o65.txt`. The latter is also reported as `not_committed` by the frozen O dry-run at line 28. Thus no O control receipt or committed exactness-sweep receipt was available for this review; this is a dependency, not a counter edit.
