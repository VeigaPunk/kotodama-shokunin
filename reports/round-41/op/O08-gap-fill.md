- Seat: O08 | executor | O | date 2026-10-19 | baseline 456674d

## Gap-fill: distinguish a computed ROOT from a used ROOT

Round 40 declares the expected relative-root expression (`ROOT = str(pathlib.Path(__file__).resolve().parents[2])`), but a `grep -n ROOT reports/round-40/run-validation.py` search returns only the declaration and a later prose mention. Its working paths remain relative to the process cwd: `ROUND` is a relative string, `measure()` reads through it, and `main()` resolves the guard script and writes the receipt through relative paths. Thus a checker that confirms the ROOT assignment and absence of `os.chdir` can report the reference runner as root-anchored even though ROOT does not anchor any I/O. Running it from a non-repository cwd is **to-verify**; the in-tree runner must not be executed.

Round 33 shows ROOT-backed paths and subprocess `cwd=ROOT`, but also calls `os.chdir`, so it is evidence for root usage, not a directly reusable no-chdir solution. Suggested non-blocking checker distinction: report `root_declared` separately from `root_used_for_paths_or_cwd`; do not silently add the latter as a required contract point without confirming the intended invocation contract. A checker selftest could include a canonical ROOT declaration with otherwise cwd-relative I/O and assert it is not described as root-anchored.

## Owed

- None. The portability expectation is recorded as to-verify and is not asserted as a required defect under the five declared points.

## Citations

- `reports/round-40/run-validation.py:5-7,64-65,227-244` — ROOT declaration; relative ROUND; relative reads, guard-script resolution, and receipt write.
- `reports/round-40/run-validation.py:5,204` — `grep -n ROOT` returned only the declaration and prose mention.
- `reports/round-33/run-validation.py:23,98-120,217,243,876,1454` — ROOT-backed path/cwd use and the separate `os.chdir` behavior.
