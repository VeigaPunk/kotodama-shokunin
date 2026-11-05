# ExecMutants94 — round-94 mutant set (claim O, operability)

Stage: `.ufo/waves/round-94/w1/stage/ExecMutants94/` (files: `mutants94.py`, `red-before-v4.txt`, `DONE`).

## Output files

- `mutants94.py` sha256 `cdaf7f241a6ebff61500ba53687ce953882c55869bb1a158c7523b065d7bbfa1`
  - copied from `reports/round-93/mutants.py` (sha256 `c5747989bf0493e04a57cd9c6bd6f77ec4e879aabbdce314b6f61c1850c69966`), then edited: five routed entries added, driver rewritten.
- `red-before-v4.txt` sha256 `d1dd53e7b3b176e738bad87ddbb03326b98c3ff23d4d3217ac2153ed3370fd2b`

## Driver (mutants94.py)

- `--tool <path>` (required) and `--work <dir>` (required, must exist). The `--out` default into `reports/round-93/` is gone; the receipt goes to `<work>/mutation94-score.txt`. No `/tmp`, no lane writes.
- `--only a,b,c` runs a named subset; unknown names refused rc 2 (`MUTANTS94_ERROR: unknown mutant name(s): ...`, checked: `--only bogus-name` gives rc=2).
- Missing `--work` refused rc 2 (checked with a nonexistent dir: rc=2).
- Clean copy must print `SELFTEST PASS` with rc 0 before any mutant runs.
- Each mutant prints `MUANT <name> <KILLED|SURVIVED|BROKEN-PATTERN> selftest_rc=<n>`. KILLED when rc != 0 OR the output lacks `SELFTEST PASS`. Final line `MUTATION-SCORE: <k>/<t> killed, <s> survived, <b> broken-pattern`.
- Exactly-once rule: enforced for the five routed patches (`ROUTED`). Round-93 entries keep replace-all semantics; absent patterns are refused for all entries (BROKEN-PATTERN). Reason: six round-93 patterns match more than once on the v4 bytes (see below); the exactly-once rule applied to them would mark the frozen 83-entry set broken.

## Routed mutants: patch-count check (v4 bytes, sha 9799a96c…)

Command: `python3 -B -c` importing `mutants94.MUTANTS` and counting `src.count(old)` on the v4 file.

| mutant | matches on v4 | recipe source |
|---|---|---|
| script-strip-off | 1 | `s = re.sub(r'(?is)<(script|style)\b…', ' ', s)` → `pass` (html_body_text) |
| comment-strip-off | 1 | `s = re.sub(r'(?s)<!--.*?-->', ' ', s)` → `pass` |
| unescape-off | 1 | `return _html.unescape(s)` → `return s` |
| dispo-any-casei | 1 | `DISPO_ANY_RE` gains `re.I` |
| baserows-drop-cell8 | 1 | `for i in (0, 1, 2, 3, 4, 5, 6, 8):` → without `8` |

## Red-before (v4 base)

Extraction: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2:tools/check-advance-evidence.py` → scratch copy, sha256 `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` (matches). Clean v4 selftest: `SELFTEST PASS 114/114`, rc 0.

```
MUTANT script-strip-off SURVIVED selftest_rc=0
MUTANT comment-strip-off SURVIVED selftest_rc=0
MUTANT unescape-off SURVIVED selftest_rc=0
MUTANT dispo-any-casei SURVIVED selftest_rc=0
MUTANT baserows-drop-cell8 SURVIVED selftest_rc=0
MUTATION-SCORE: 0/5 killed, 5 survived, 0 broken-pattern
```

Driver rc=1 (expected: survivors). All five survive as predicted, so each routed class is a real selftest pin gap on v4. The full 83-entry round-93 run was not executed (MutationTester94's job).

## Noted for MutationTester94 (not run here)

On v4, six round-93 patterns match more than once, so replace-all applies to every site: `self-quote-check-off` (2), `source-quote-check-off` (2), `duplicate-id-off` (2), `duplicate-url-off` (3), `cellcount-off` (2), `gap-cap-slash-capture-error-off` (2). Measured with the static count above; the round-93 score was taken with the same replace-all behaviour, so the frozen 83 are unchanged.

## Not measured / limits

- Not run: the candidate (v5) tool; the round-93 83-mutant set; the stub control. These are for MutationTester94 and the L1.
- Dead-kill check of the routed mutants against a v5 candidate is not done here; the red-before only shows they survive on v4.

## Tooling, host

- Installs: none. Sysctl/host changes: none. pacman: not touched.
- Scratch `/fast/scratch/hyaku/kotodama-r94/ExecMutants94/` deleted before yield (verified absent).
- No commits or mutating git commands; only `git show` (read-only) on the base.
