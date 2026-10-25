# MutLedgerCa — wave-2 FALSIFY, claim Ca ledger + observe guard (hyaku run 7)

Seat: MutLedgerCa-2. 2026-10-25. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, lands `0316b8883b4f8d44b8efd720140e7f52f734a102`, base `8841ad3b896a0227674fa0725b818c999118046f`, freeze commit `af65165`. Target: `reports/round-73/ledger.json` + the observe guard of `reports/round-73/accept-ca.py` (r3, sha256 `222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89`).

Method: throwaway clone per tasking recipe at `/tmp/MutLedgerCa-clone-rfwP` (`git -C "$D" rev-parse --show-toplevel` == `$D` verified before first commit; toplevel of clone == `$D/lane`). Each mutant is the landed ledger (or landed bytes) edited and **committed** as a child of lands; the counter ran at that commit: `python3 -B reports/round-73/accept-ca.py --root <clone> --lands <mut> --fleet-root /home/vgpnk/Projects/shokunin --main <mut>` (`--main <mut>` only to keep STAMP's `measured == lands` semantics for a detached mutant HEAD; the graded pristine run used the default `main`). No lane write except this file; no installs performed (python3/git sufficed; pacman untouched).

## Baseline (pristine bytes) — the detector is green and its controls work

- `--selftest` → `SELFTEST OK: 10 scenarios`, exit 0.
- Pristine run at lands: `ACCEPT-CA-73: PASS legs=9/9`, exit 0; BASEMISMATCH `found=8 min=8`; REPAIR `green=['L04','L05','L08']`; ledger source=lands sha `c912401dd511d712567d8a704a690bf02fa4a8253a628b8e67ab9473798356b9`. Claim Ca's `after` ("prints ACCEPT-CA-73: PASS legs=9/9") is exercised-true.

## Mutant results (all committed in `/tmp/MutLedgerCa-clone-rfwP`)

| id | mutation (committed) | expected | actual (exit, key legs) | verdict |
|---|---|---|---|---|
| M1a / M1a′ | observe `python3 -c "print(str(245))"` (item-exact, L01) and `"print(str(505))"` (L04) | reject | LEDGER FAIL `python3 -c code must read the clone (pathlib/open/subprocess/os)`; exit 1 | KILLED |
| M1b | observe `["python3","-c","import os;assert os.sep;print(str(505))"]` on L04/REPAIR | reject | `ACCEPT-CA-73: PASS legs=9/9`, exit 0 — "truth" is a hardcoded constant | **SURVIVED** (MAJOR) |
| M2a | observe `["printf","505\n"]` / `echo` argv | reject | LEDGER FAIL `argv[0] 'printf' not in the observe allowlist`; exit 1 | KILLED |
| M2b | observe `["wc","-l","/dev/null"]`, `expected_after="0 /dev/null"`, no statement_after | reject | `PASS legs=9/9`, exit 0 — allowlisted binary over a non-repo constant | **SURVIVED** (MAJOR) |
| M3a | observe `cat reports/round-73/telemetry/ca-truth.txt`, file created by the repair author at lands only | reject | BASEMISMATCH FAIL `L04:<empty-stdout-exit=1>` (unobservable at base — fails closed); exit 1 | KILLED |
| M3b | observe `["grep","-c","R73-CIRCULAR","LOG.md"]`, expected `1`, no statement_after; author appends the marker line to append-only LOG.md in the same commit | reject | `PASS legs=9/9`, exit 0 — the truth side is the author's own appended line | **SURVIVED** (MAJOR) |
| M4 | SHONEN.md:6 reverted to the stale `:468` (Error patterns); shadow line `` `:505` (Error patterns) `` appended; L04 `statement_after.parse` := `(?s).*:(\d+)` \(Error patterns\)` (ledger-controlled, greedy = last occurrence) | reject | `PASS legs=9/9`, exit 0 while `SHONEN.md:6` still reads `:468` (truth is 505) | **SURVIVED** (MAJOR) |
| M5 | L01 `rederive` := the culture-material count command (yields 38); second L01 correction row appended carrying it | NOSTUB tell | `PASS legs=9/9`, exit 0; the pasted command demonstrably yields **38** while the row claims 245 | **SURVIVED** (MINOR) |
| M6a | L01 `stated_text` := "Total knowledge entries: 999." | reject | LEDGER FAIL `stated_text not found in corpus/README.md at base`; exit 1 | KILLED |
| M6b | L01 `stated_at` := `corpus/README.md:407` (text lives on :732) | reject | only `NOTE L01 stated_text is in corpus/README.md but not on line 407`; `PASS legs=9/9`, exit 0 | **SURVIVED** (MINOR) |
| M7 | all 8 observe_cmds := constant printers of the stated token (all match at base) | BASEMISMATCH catch | BASEMISMATCH FAIL `found=0 min=8` (+ REPAIR red, `tok==stated`); exit 1 | KILLED |
| M8a | L01 observe = landed ls-tree-count code with the pin := `000…0` (nonexistent) | reject | git exits 128 (`fatal: not a tree object`) but the python wrapper prints `0`; counter observes `'0'` at base and lands → `PASS legs=9/9`, exit 0 | **SURVIVED** (MAJOR) |
| M8b | 9th ANNOTATE pair whose observe prints nothing at exit 0 (`find … -name zz-no-such-marker-zz`) → observed token `""`; correction row omits the observed token | ANNOTATE catch | ANNOTATE **PASS** (`"" in row` is trivially true); NOSTUB FAIL `L09:placeholder-token('')`; exit 1 | KILLED (only by NOSTUB) |
| M9 | observe `["python3","-c","import os;print(os.environ['LC_ALL'])"]`, expected `C.UTF-8`, no statement_after | reject | `PASS legs=9/9`, exit 0 — the counter itself injects the constant (`env` sets `LC_ALL=C.UTF-8`) | **SURVIVED** (MAJOR) |
| M10 | truth side repaired instead of the statement: `reports/round-72/telemetry/measures-ca.txt` edited in place `ACCEPT-72: FAIL`→`PASS` (file is in no protected set) | reject | `PASS legs=9/9`, exit 0; L06's observed token becomes PASS, the filed SCORECARD:1401 line becomes "true", and the committed L06 correction row ("> the committed round-72 receipt … reads `ACCEPT-CA-72: FAIL legs=12/12`") becomes **false** | **SURVIVED** (MAJOR) |

## Survivors — what is false, and the exact tightening

1. **Echo/constant channel is open (M1b, M2b, M9; guard evidence M7).** The literal-print guard only matches `print("<literal>")` — `print(str(505))` already evades it, and the clone-read regex `pathlib|open\(|subprocess|os\.` is satisfied by `os.sep`/`os.environ`, which read nothing from the clone; allowlisted binaries (`wc`, `cat`, `grep`) over non-repo or author-appended inputs re-open the channel. No leg requires an observation to depend on clone bytes. Tightening: reject `python3 -c` code whose only `os.` use is `os.environ`/constant attributes, require the argv's first file argument of `grep`/`cat`/`wc`/`ls`/`stat`/`sha256sum` to be a tracked path existing at base, and add a behavioral canary — rerun every observe in a second clone with the watched file mutated and require the token to change (or the pair to be flagged constant).
2. **Circular truth for REPAIR pairs (M3b, M10).** Nothing binds a pair's truth side to bytes the ledger author does not control: a pair without `statement_after` greens on `observed == expected_after`, and `LOG.md` appends and round-72 telemetry edits are invisible to APPENDONLY (`APPENDONLY_FILES` + `INPLACE_PATHS` cover neither), to SEPARABLE (round-73 telemetry only), and to TRACKED. M10 shows the falsifier can even make a filed lie true and a committed correction row false while every leg stays green. Tightening: require `statement_after` on every REPAIR pair (all three landed REPAIR pairs have it — the landed ledger does not exploit this); forbid observe targets that the lands commit itself appends to; extend APPENDONLY's zero-removed set to every base-existing path any pair's `observe_cmd`/`rederive` reads.
3. **Shadow-stub repair (M4).** `statement_after` is a ledger-controlled regex over the whole file; a greedy last-occurrence pattern greens the REPAIR leg from an appended copy while `stated_at` still carries the false token. SHONEN.md is in neither `APPENDONLY_FILES` nor `INPLACE_PATHS`, so no leg constrains it. Tightening: evaluate `statement_after` at `stated_at` (matched occurrence must lie on the stated line), or require the stale `stated_text` to be absent from the file at lands.
4. **Degenerate observed tokens self-annotate (M8a, M8b).** A dead pin is not detected (the counter never checks that hashes in `observe_cmd` resolve), the wrapped failure surfaces as a confident `0`, and ANNOTATE/NOSTUB token containment is raw substring — the observed `0` is "found" inside `L01`/the pinned hash `8841ad3b896a0227674fa0725b818c999118046f` of the landed row. Only NOSTUB's `STUB_TOKENS` (which contains `""` but not `"0"`) caught the empty-token variant. Tightening: `git cat-file -e` every 40-hex in `observe_cmd`/`rederive` at the LEDGER leg; boundary-match tokens (`(?<![0-9A-Za-z])tok(?![0-9A-Za-z])`) in ANNOTATE/NOSTUB; fail a pair closed when its parse-miss raw token is empty.
5. **NOSTUB verifies string presence, not derivation (M5).** The `rederive` string is pasted, never executed; APPENDONLY correctly blocks in-place row rewrites, but a contradictory duplicate row appends freely and satisfies the leg. Tightening: bounded-execution of `rederive` (or at least a run whose output must contain the observed token) with the result disclosed in the receipt.
6. **stated_at line resolution is warn-only (M6b).** `stated_text` off the stated line is a `note()`, not a problem; the ledger's location claims are unaudited. Tightening: make the line check a LEDGER problem.

## Landed-bytes findings (no mutation needed)

- **MINOR — stale registry row:** `SKILL.md:704` (accept-ca-73 gate row) says the selftest "prints `SELFTEST OK: 9 scenarios`" (5 words, SKILL.md:704); the landed r3 counter prints `SELFTEST OK: 10 scenarios` (scenario 7b was added in r3, `reports/round-73/counter-revisions.md`). Repro: `python3 -B reports/round-73/accept-ca.py --selftest` (exit 0) vs `sed -n '704p' SKILL.md`.
- **MINOR — no committed PASS receipt:** `git ls-tree -r 0316b88… reports/round-73/telemetry/` lists 13 files, none named `measures-ca.txt`; every committed `ACCEPT-CA-73` line in telemetry is a FAIL control (`controls-ca*.txt:41`). The graded PASS receipt exists only as an uncommitted run (this seat's baseline re-run). Wave-1 `ConnectorPatterns.md:293` expected it committed; claim Ca's `after` only says the counter "prints" PASS — letter-true, receipt absent.
- **MINOR — control description drift:** claims.json Ca `do_nothing_control` says "FAIL legs=5/9; red: REPAIR, ANNOTATE, NOSTUB, TRACKED; green and unmoved: LEDGER, BASEMISMATCH, APPENDONLY, SEPARABLE, STAMP" (accurate for the cited `controls-ca.txt`), but the r3 receipt committed at the landed counter sha (`controls-ca-r3.txt:41`) reads `ACCEPT-CA-73: FAIL legs=4/9` — STAMP is additionally red there because lane main (`35378990…`) had moved past base, as the receipt's own header discloses.

No BLOCKER found: all nine Ca legs hold on the landed bytes as exercised, and the claim's letter (counter prints PASS 9/9; 8/8 pairs red at base; controls fail closed) is reproducible.

## Could NOT check

- STAMP's receipt grammar against `tools/check-receipt-seq.py` beyond the counter's internal check (not part of the assigned probes).
- Anything under `/home/vgpnk/Projects/shokuknow` (read-only, no campaign tools) — not needed for these probes.
- Exhaustive regex/glob spaces for `parse`/`stated_parse` (catastrophic backtracking not probed; `re.search` without timeout in `observed_token`/`statement_after` is a theoretical DoS surface left untested).
- Whether sibling seats' concurrent w2 writes touched the lane — this seat performed exactly one lane write (this file).

## Restoration evidence

- All mutations lived in `/tmp/MutLedgerCa-clone-rfwP` (14 mutant commits, each recorded above with the counter output at that commit). After probes: clone reset to lands, `git status --porcelain` empty, HEAD == `0316b88…`.
- Pristine re-run after restoration: `ACCEPT-CA-73: PASS legs=9/9`, exit 0.
- sha256 before == after: counter `222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89`, ledger `c912401dd511d712567d8a704a690bf02fa4a8253a628b8e67ab9473798356b9` — identical in the throwaway clone and the real lane; real-lane claims.json `5716523f3e8e798217d947d664c313911d4d1e6c15524f22056584e8feead130`. No jj/git state, index, or working-tree byte of the lane or fleet root was modified by this seat.
- Tooling: none installed (no pacman, no uv/npm/cargo); no downloads; no live fetches (none required).
