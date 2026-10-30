# SentinelLimits — round 79 W1: timeout/output caps, UTF-8, hostile JSON fields

Seat: `SentinelLimits` (sentinel, leaf, W1 pre-data). Lane: `kotodama-shokunin`. Base: `44f76d456c1b326a71ffdb381590af825cbf11be`.
Stage: `.ufo/waves/round-79/w1/stage/SentinelLimits/` (draft module, selftest, probes, raw receipts).
Status: findings and a bounded design are complete. Nothing in the production tree was edited, nothing was committed, and no claim counter was frozen or run. The draft module passes its own selftest (42/42, receipt below). That is evidence for the draft, not for ExecGuard's `tools/ledger-token-guard.py`, which does not exist yet.

## 0. Verdict in one screen

1. The round-76 observation and JSON paths (`reports/round-76/accept-ca.py`) have no output cap, no decode guard, and no timeout that is safe against child processes. Each of these is measured, not inferred (§2).
2. Four hostile-input classes escape the round-76 handlers as uncaught tracebacks or silent acceptance: `RecursionError` on deep nesting, invalid UTF-8 from `text=True`, duplicate keys, and `NaN`/`Infinity`/lone surrogates/oversize strings.
3. Ledger `parse` and `stated_parse` fields are regexes run with no time bound. A nested-quantifier pattern on a 61-character input exceeded a 10 s wall cap. A closed parse grammar is the only boring fix (§4.3).
4. Historical Ca-schema ledgers cannot all be re-run under a closed grammar: 72 of 75 pairs at base use regex `parse`, and 6 pairs use interpreter-shaped observations, two of which read worktree paths (L07, L08). The guard must refuse those by label. This is consistent with the O clause: "one working guard … not historical truth certification" (`CLAIMS-DRAFT.md` line 3).
5. A bounded design with fixed limits, stable refusal labels, and a closed observation environment is in §4. Every limit has a measured justification.

## 1. Inputs read

- `/home/vgpnk/.omp/agent/RULES.md`: tooling directive only. Nothing was installed (see §7).
- `.ufo/waves/round-79/CLAIMS-DRAFT.md`: O clause (lines 3, 6) and the pre-freeze requirements (frozen constants, `--freeze`, `--lands`, do-nothing and junk receipts, counters grade committed bytes).
- `corpus/QUALITY.md`: criteria 9, 11, 17, 19, 23, 25, 26, 28 read. Criteria 25 and 28 bind the counter's own reads to committed bytes, and criterion 23 requires a `--selftest` receipt with a verdict line, exit code and counter sha256.
- Committed `reports/round-76/accept-ca.py` at base (sha256 in `stage/SentinelLimits/receipts/round-76-accept-ca.sha256`): `git` helper 345–352, `norm` 362–363, `OBSERVE_TIMEOUT` 301, `load_frozen` 697–705 and `ledger` load 893, `_child_env` 1255–1270, `run_observe` 1273–1288, `parse_observed` 1317–1340 (regex `rx.search(out)` at 1330, `norm(out)[:200]` at 1337), `stated_token` 1355–1360 (`re.search(stated_parse, stated_text)`), `statement_after` 1397–1399.
- Committed ledger bytes at base, read with `git cat-file` / `git show <base>:<path>` only. No worktree file was read for evidence.
- Round-78 census and lesson (`reports/round-78/telemetry/census-end.txt`, `corpus/lessons/round-78.md` R78-M1), and the round-77 probe ledger `.ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json` (6,815 B, loads OK).

## 2. Measured findings

Each row names its raw receipt in `stage/SentinelLimits/receipts/`. "Legacy" means the round-76 call shape replayed on the same bytes.

| id | finding | measured | receipt |
|---|---|---|---|
| F1 | Observation output has no byte cap. `subprocess.run(capture_output=True, text=True)` captures whatever the child writes. | A committed 40 MiB file via `git grep -n -E . <rev> -- big.txt` captured 132,344,001 B with a 7-char rev and 258,173,100 B with a 40-char rev, in 0.57 s and 175 MB RSS. Output size scales with the rev string and the file. | `p2_output_timeout.raw.txt`, `selftest.raw.txt` (LEGACY line) |
| F2 | Non-UTF-8 observation output escapes `run_observe` as an uncaught exception. `run_observe` catches only `FileNotFoundError`, `TimeoutExpired`, `OSError`. | `git grep` on a file containing `0xff` with `text=True` raised `UnicodeDecodeError` out of `subprocess.run`. Base also contains a deliberate invalid-UTF-8 file, `reports/round-56/fixtures/lessons/bad-utf8.md` (position 81), so an observation over that path reproduces it. | `p2_output_timeout.raw.txt`, `p5_base_survey.raw.txt` |
| F3 | Deep JSON nesting: `RecursionError` is not `ValueError`, so the `except ValueError` at lines 705 and 893 does not catch it. | 200,000 nested `[` → `RecursionError: Stack overflow` escapes `json.loads`. 40-deep nesting parses. | `p1_json.raw.txt`, selftest legacy column |
| F4 | `json.loads` accepts `NaN`, `Infinity`, `-Infinity`, duplicate keys (last wins silently), lone surrogates (fail later, at `.encode`), floats such as `1e999999`, a UTF-8 BOM, and a 64 MiB string. Only the 5,000-digit integer raises (`ValueError`, the 4,300-digit limit). | Each row of the selftest legacy column shows `OK` for these inputs. Lone surrogate: `UnicodeEncodeError` only when encoded. | `p1_json.raw.txt` |
| F5 | Timeout does not clean the process tree. `subprocess.run(timeout=)` kills only the direct child. A grandchild that inherited stdout/stderr keeps running after the call returns. | Naive `subprocess.run`: `TimeoutExpired` at 2.00 s, and 1 marker process still alive afterwards. Process-group kill: returned at 2.00 s, 0 survivors. `subprocess.run` does not hang on pipes here; the defect is the orphan. | `p3b_leak_check.raw.txt` |
| F6 | Ledger regex fields are unbounded. `parse`, `stated_parse` compile with `re` and run on unbounded text, with no time limit. | `(a|aa)+$` on 27 chars: 0.034 s. `^(\w+\s?)+:$` on 41 chars: 2.11 s. Same pattern on 61 chars: exceeded the 10 s wall cap. Historical `([0-9]+)$` on 60,000 digits: 6.55 s (quadratic `re.search`). | `p4_regex.raw.txt` |
| F7 | `git -P` is PCRE-bounded: `pcre2_jit_match … match limit exceeded`, rc 128, 0.01 s. Only a note; the grammar should refuse `-P` anyway. | Measured on `redos.txt`. | `p2_output_timeout.raw.txt` |
| F8 | Silent truncation and aliasing in token normalization. `norm(out)[:200]` (line 1337) truncates observed tokens and never truncates stated ones, so a long equal prefix can fake equality. `str.split()` folds U+00A0 and U+3000 into spaces. | `norm_token("a\u00a0b") != "a b"` is `True` in the draft; the round-76 `norm` returns `"a b"` for `"a\u00a0b"`. | selftest `token-nbsp-distinct` and `token-ascii-collapse` |
| F9 | The round-76 child environment keeps `HOME`, so the observed `git` reads `~/.gitconfig`. | With `HOME=<scratch>` and a `[test] r79 = seen-from-global` config: round-76 env shape prints `seen-from-global`, rc 0. Draft env (`GIT_CONFIG_GLOBAL=/dev/null`) prints nothing, rc 1. | command in §6; output in §2 transcript below |
| F10 | `git show <rev>:<path>` and `git cat-file blob <rev>:<path>` return the same committed bytes; neither applies a `textconv` driver. `git grep --textconv` does apply it, only when asked. | Fixture with `t.txt diff=x` and `diff.x.textconv` set: `show`, `cat-file`, `grep` (default) show `hello lower`; `grep --textconv` shows `HELLO LOWER`. | §6 command 3 |
| F11 | `statement_after` reads a path joined to the clone and decodes with `encoding="utf-8"`, catching only `OSError` (lines 1397–1399). Code-read, not probed: `os.path.join(clone, "/abs")` returns `/abs`, and `..` escapes the clone. A decode error escapes uncaught. | Code-read at base. Python `os.path.join` documented behaviour. | `accept-ca.py` lines 1397–1399 |

Transcript for F9 (verbatim from the probe run):

```
--- round-76 _child_env shape (HOME kept, no GIT_CONFIG_GLOBAL):
seen-from-global
rc=0
--- draft env (GIT_CONFIG_GLOBAL=/dev/null):
rc=1
```

## 3. Historical shapes at base (what a strict guard must refuse, honestly)

Survey `p6_schema_survey.raw.txt` (read-only, `git show` at base):

- Ca-schema ledgers (pairs with an `observe_cmd` argv list): 7 files, 75 pairs. Largest: `reports/round-76/ledger.json` (20 pairs, 20,203 B). Largest Ca-schema file is `reports/round-74/ledger.json` (53,057 B). Largest ledger-named blob overall is `reports/round-10/drift/ledger.json` (75,791 B, not Ca-schema).
- `parse`: 0 pairs with null, 3 `count-presence`, 72 regex. A closed grammar that refuses regex refuses 72 of 75 historical pairs. That is an explicit scope cut, not a silent one.
- Interpreter-shaped observations, all refused by the existing H2 rule and by any strict grammar: 6 pairs. Five are in `reports/round-73/ledger.json` (L01, L02, L03, L07, L08) and one in `.ufo/waves/round-73/counters/fixture/ledger.json` (F-R3README, not itemised here). L01–L03 wrap `git ls-tree` at a pinned revision inside `python3 -c`; L07 `open()`s `reports/round-72/claims.json` and L08 `glob()`s `reports/` in the worktree, so those two are mutable-revision shapes as well.
- Non-UTF-8 committed text: 1 of 8,222 text-like blobs at base, the deliberate `reports/round-56/fixtures/lessons/bad-utf8.md`. No NUL bytes and no BOM-prefixed text blobs at base (`p5_base_survey.raw.txt`).
- Largest committed blobs: 2,706,268 B (`.ufo/waves/round-77/w2/stage/ExecCpass/lane-snapshot-after.txt`), 343 text-like blobs above 64 KiB. Irrelevant to ledger caps but relevant to any future "read a whole file" observation: those files must not be read through the observation path.

## 4. Bounded design

### 4.1 Limits (draft constants in `ledger_limits_draft.py`)

| constant | value | justification |
|---|---|---|
| `LEDGER_MAX_BYTES` | 1 MiB | largest Ca-schema ledger at base is 53,057 B (~19× headroom); largest ledger-named blob is 75,791 B |
| `OBS_TIMEOUT_S` | 20 s wall per observation | measured worst is 0.5 s for a 40 MiB `git grep`; 20 s is 40× headroom |
| `RUN_BUDGET_S` | 600 s wall per guard run | worst case 20 pairs × 2 observations × 20 s = 800 s > 600 s, so an all-hanging run stops with `BUDGET` (fail closed); normal runs are seconds |
| `OBS_STDOUT_MAX` | 64 KiB | historical observations emit one count line; read stops at cap + one 64 KiB chunk |
| `OBS_STDERR_MAX` | 8 KiB | diagnostic only |
| `TOKEN_MAX_CHARS` | 200 | refuse, never truncate (F8) |
| `JSON_MAX_DEPTH` | 32 | explicit iterative walk; recursion overflow is separately labelled |
| `JSON_MAX_NODES` | 100,000 | exceeds any base ledger by orders of magnitude; `json-nodes-100001` case refuses |
| `JSON_MAX_STR_CHARS` | 65,536 | the 70,000-char case refuses |
| `JSON_MAX_INT_DIGITS` | 18 | no integer field in the schema needs more |
| `ARGV_MAX_ITEMS` / `ARGV_MAX_ITEM_CHARS` | 32 / 1,024 | argv is refused before spawn; the historical observe_cmds are short |
| `PAIRS_MAX` | 256 | ≈13× the largest base Ca ledger (20 pairs) |

### 4.2 Check order (fail early, cheapest first, every refusal labelled)

1. Size: `len(raw) <= LEDGER_MAX_BYTES` before any decode (`LIMIT-BYTES`).
2. Decode: no NUL byte; strict UTF-8; no leading BOM (`NUL-BYTE`, `ENCODING`, `BOM`).
3. JSON with hooks: `object_pairs_hook` refuses duplicate keys (`DUP-KEY`); `parse_constant` refuses NaN/Infinity (`NONSTD-CONST`); `parse_int` caps digits (`BIG-INT`); `parse_float` refuses floats (`FLOAT`). `RecursionError` → `DEPTH`; `JSONDecodeError` → `JSON`.
4. Tree walk (iterative): depth, node count, string length, NUL inside strings, lone surrogates (`DEPTH`, `NODES`, `STR-TOO-LONG`, `NUL-IN-STRING`, `SURROGATE`).
5. Shape: pair count ≤ `PAIRS_MAX`; `parse` in `{count-presence, exact}` else `UNSUPPORTED-PARSE`; interpreter/constant-printer binaries refused by the grammar (SentinelExec owns the grammar).
6. Observation: argv checked (`ARGV`), then `run_bounded` in a new session with a closed env, wall deadline, per-stream caps and killpg on every exit path (`SPAWN`, `TIMEOUT`, `OUTPUT-CAP`), then strict decode (`ENCODING`), then the closed parse (`PARSE`, `TOKEN-TOO-LONG`).

### 4.3 Closed parse and token rules

- `count-presence`: stripped output is one line `<head>:<digits>`; `rpartition(":")`; `present` if count > 0, `absent` otherwise. No regex.
- `exact`: the output is one line; token = ASCII-whitespace-collapsed line. No regex.
- Any other `parse` value → `UNSUPPORTED-PARSE`. A `stated_parse` regex is not supported; the stated token is an explicit field in the new schema. Regex-free rules remove F6 by construction.
- Normalization folds only `[ \t\r\n\f\v]`. Other code points stay distinct (F8).

### 4.4 Process rules

- `start_new_session=True`, `stdin=DEVNULL`, `close_fds=True`.
- Selector loop over stdout and stderr with a monotonic deadline. Cap exceeded → `OUTPUT-CAP`. Deadline passed, or a pipe still open after the leader exits → `TIMEOUT` (a pipe held open by a grandchild is refused, not waited for).
- `os.killpg(pid, SIGKILL)` runs on every exit path before the reap, so a grandchild cannot outlive the observation (F5).
- Closed env: `PATH`, `HOME=<work>`, `TMPDIR=<work>`, `GIT_CONFIG_GLOBAL=/dev/null`, `GIT_CONFIG_NOSYSTEM=1`, `GIT_TERMINAL_PROMPT=0`, `GIT_NO_REPLACE_OBJECTS=1`, `GIT_OPTIONAL_LOCKS=0`, `LC_ALL=C.UTF-8` (F9).
- Read committed bytes with `git cat-file blob <rev>:<path>`, never a worktree path. Both `show` and `cat-file` are safe re textconv here (F10), so `cat-file` is preferred for explicitness.
- `--work` is required and must be an explicit directory; no system temp dir is used.

### 4.5 Refusal labels and exit mapping (stable)

Exit 0: clean. Exit 1: a measured finding (token mismatch, `stated == actual`, `observed_at_base` differing from the actual observation). Exit 2: any refusal, printed as `REFUSED <LABEL>: <detail>`. Labels: `LIMIT-BYTES`, `NUL-BYTE`, `ENCODING`, `BOM`, `DUP-KEY`, `NONSTD-CONST`, `BIG-INT`, `FLOAT`, `DEPTH`, `JSON`, `NODES`, `STR-TOO-LONG`, `NUL-IN-STRING`, `SURROGATE`, `UNSUPPORTED-PARSE`, `PARSE`, `TOKEN-TOO-LONG`, `ARGV`, `SPAWN`, `TIMEOUT`, `OUTPUT-CAP`, `BUDGET`. Any unlabelled exception is a defect; the selftest checks for `UNLABELLED:` and fails on it.

### 4.6 Per-field hostile-input table (what the guard reads from each ledger pair)

| field | type | bound | hostile vector | refusal |
|---|---|---|---|---|
| file as a whole | bytes | ≤ 1 MiB | oversize, NUL, BOM, invalid UTF-8 | `LIMIT-BYTES`, `NUL-BYTE`, `BOM`, `ENCODING` |
| object keys | str | ≤ 64 Ki chars, no NUL, no surrogate | duplicate key shadowing a second value | `DUP-KEY`, `SURROGATE` |
| any number | int/float | ≤ 18 digits; no float; no NaN/Infinity | `1e999999`, 5,000-digit int | `BIG-INT`, `FLOAT`, `NONSTD-CONST` |
| any container | list/dict | depth ≤ 32, nodes ≤ 100,000 | deep nesting | `DEPTH`, `NODES` |
| `id`, `disposition`, `stated_at`, `why`, `expected_after` | str | ≤ 64 Ki chars | long text | `STR-TOO-LONG` |
| `stated_text`, `stated_token` | str | token ≤ 200 chars after normalization | long token that shares a prefix | `TOKEN-TOO-LONG` |
| `stated_parse` | str | regex not supported | nested quantifier | `UNSUPPORTED-PARSE` (never compiled) |
| `parse` | str | `count-presence` or `exact` | nested quantifier, historical regex | `UNSUPPORTED-PARSE` |
| `observe_cmd` | list[str] | ≤ 32 items, ≤ 1,024 chars each, no NUL | shell string, interpreter, huge argv | `ARGV`; grammar refusal owned by SentinelExec |
| `rederive` | str | ≤ 64 Ki chars; must equal the `observe_cmd` argv after `shlex.split` | mismatch between text and argv | grammar / guard finding |
| `observed_at_base`, `red_at_base` | str/bool | recomputed by the guard, never trusted | stale or stated value | finding (exit 1) |
| `statement_after` | object | `path` relative, no `..`, no absolute, read via `git cat-file` at lands | absolute or `..` path, invalid UTF-8 | `ARGV`-style path refusal (new label to add to §4.5 if kept) |

Note on `statement_after`: a read through the clone path is the worktree-read defect class (criterion 25/28). The draft does not implement it; the design requires `git cat-file blob <lands>:<path>` plus the path validation above. Raise with L1 as a required change to the round-76 shape.

## 5. Selftest of the draft (run, raw preserved)

`stage/SentinelLimits/selftest_draft.py` against `stage/SentinelLimits/ledger_limits_draft.py`. Run in an isolated fixture repository whose root was verified before use (`git rev-parse --show-toplevel`), with explicit `--work`. Verdict line: `SELFTEST OK: all cases passed`, exit 0, 42 `CASE` lines, 0 `FAIL` lines. Raw: `receipts/selftest.raw.txt`. Sha256 of the draft and the selftest: `receipts/draft-sha256.txt`.

Scope of this claim, stated: the selftest is the draft's own probe. It does not run ExecGuard's production guard, a counter, or `--freeze`/`--lands` logic, and it does not cover the grammar (SentinelExec). The LEGACY rows in the same receipt are the round-76 shapes on the same bytes; they show the red-before.

Cases (42): 17 hostile-JSON cases with the expected label, each with its legacy outcome; 4 committed ledgers at base (`git cat-file`) loading OK; 12 process cases (clean observation, 40 MiB output-cap, exact-cap pass and cap+1 refusal, timeout on a sleeping leader, pipe held by a grandchild with 0 survivors, bad-UTF-8 observation, missing binary, two argv refusals, budget exhaustion); 9 parse and token cases.

## 6. Commands (reproduction)

Run from the stage dir; fixture recreated under an explicit scratch dir.

```
# 1. isolated fixture, root verified
mkdir -p /fast/scratch/hyaku/kotodama-r79/SentinelLimits/fx && cd $_
git init -q . && test "$(git rev-parse --show-toplevel)" = "$PWD" && echo root-verified
python3 -B -c 'open("big.txt","wb").write(b"abcdefghij\n"*(40*1024*1024//11)); open("bad.txt","wb").write(b"ok line\nbyte \xff here\n")'
git add -A && git -c user.name=fx -c user.email=fx@invalid commit -q -m fixture

# 2. selftest (draft) — REV is the fixture HEAD
python3 -B .../stage/SentinelLimits/selftest_draft.py --selftest --work <explicit-dir> \
   --fixture-repo <fixture> --rev "$(git rev-parse HEAD)" \
   --lane /home/vgpnk/Projects/shokunin/kotodama-shokunin --base 44f76d456c1b326a71ffdb381590af825cbf11be

# 3. textconv control (F10): set diff.x.textconv in the fixture, compare show/cat-file/grep
git config diff.x.textconv "tr a-z A-Z <"
```

Probes (`stage/SentinelLimits/probes/`): `p1_json.py` (F3, F4), `p2_output_timeout.py` (F1, F2, F7), `p3_pipe_timeout.py` and `p3b_leak_check.py` (F5), `p4_regex.py` (F6), `p5_base_survey.py` (UTF-8 and size at base), `p6_schema_survey.py` (Ca-schema and parse modes), `survey.py` (ledger-shape survey). The probes reference the scratch fixture path; they are kept for repetition, not as part of any counter.

## 7. Tooling record

- Installed: nothing. The host already had `git 2.56.0` and `python3 3.14.8`, both used as found. No pacman, no service change, no install under `~/.local/bin`.
- Written paths: only this report and `stage/SentinelLimits/`. The lane was read via `git cat-file`/`git show`/`git ls-tree` only. Fleet root was not written.
- Scratch: `/fast/scratch/hyaku/kotodama-r79/SentinelLimits/` (fixture repo, work dir, home) was removed after receipts were copied.
- Tool-sourced processes: the fixture-repo `git` calls and the probe runs. The leak probes leave one marker grandchild alive for 25 s by design (the naive-run measurement, F5). I removed survivors with `pkill -f` on their markers; a `ps` scan after scratch deletion found 0 marker processes.
- Background jobs: one regex probe (`bg_7294`) ran past its expected time and was cancelled through `proc://bg_7294/kill`. The result was re-run under a per-case 10 s wall cap; the rerun is the receipt (`p4_regex.raw.txt`).

## 8. Open items for L1 (not decided by this seat)

1. Closed parse grammar versus historical regex. Adopting §4.3 means the new guard cannot re-verify 72 of 75 historical Ca pairs. That matches the O clause's "not historical truth certification", but it is a schema decision for the planner seat.
2. `statement_after` must read `git cat-file blob <lands>:<path>` with path validation, not a clone path. This changes the round-76 shape, so it belongs in the new guard's schema and not in a re-patch of round 76.
3. Limits constants are draft values. Changing any of them after the frozen counter runs is a counter revision (criterion 23). Freeze them in `claims.json` before data.
4. A grandchild that calls `setsid` leaves the process group, so killpg cannot reach it. The pipe-held case still refuses (`TIMEOUT`), but the process may outlive the run. The grammar (no shell, no interpreter, no `-O`/`--textconv`) is the real control; SentinelExec owns it.
5. ExecGuard's env must take `GIT_CONFIG_GLOBAL=/dev/null`. The round-76 env does not (F9).

## 9. Not claimed

- No production file was written or changed. `tools/ledger-token-guard.py` does not exist in this seat's output.
- No counter, claim, freeze, or ledger row was produced. No `observed_at_base` or stated-token value was asserted from this seat.
- No external source was opened, and no source row was touched.
- No build, lint, or test suite was run beyond the seat's own probe and draft selftest, which the assignment explicitly asked for.

Report: .ufo/waves/round-79/w1/SentinelLimits.md
