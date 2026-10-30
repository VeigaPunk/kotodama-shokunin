# ExecGuard — draft tools/ledger-token-guard.py (round 79 W1 BUILD)

Verdict: **BUILD done, self-tested green, real-base demonstrated, contract
aligned with ExecOCounter.** The draft guard is at
`.ufo/waves/round-79/w1/stage/ExecGuard/tools/ledger-token-guard.py`
(874 lines, sha256 `ccb4ef5e37175b25bf07568f05e7c5dd8e1fb096ea2f961364548a8c10d2a986`
— `stage/ExecGuard/guard.sha256`). `--selftest` exits 0 with
`SELFTEST: 24/24 scenarios green (clean green-first: yes)` (receipt
`stage/ExecGuard/selftest.txt`, empty stderr, exit in `stage/ExecGuard/selftest.exit`).
The guard satisfies the contract published by the acceptance-counter seat in
`stage/ExecOCounter/schema-to-ExecGuard.md`. Nothing committed; no lane file
outside this wave dir was written; scratch
`/fast/scratch/hyaku/kotodama-r79/ExecGuard` removed after receipts copied.

## Contract conformance (schema-to-ExecGuard.md)

- CLI `--ledger PATH --repo PATH --base HEX40 --work DIR [--emit PATH]
  [--selftest]`; missing flags → exit 2 `LEDGER-GUARD-79: FAIL (refused: …)`.
- Ledger grammar: `observe_cmd` argv array (never a shell string); literal
  `{base}` in any element (and in the top-level `base`) substituted with
  `--base` before grammar checks and execution — the demo ledgers carry the
  literal top-level `"base": "{base}"` and pass.
- Pinning: after substitution at least one element must equal `--base` or
  start with `<base>:` — `HEAD`, another commit, a branch or a worktree
  target is a refusal (demonstrated: `refuse-unpinned-head`,
  `refuse-other-commit`).
- `argv[0]` must be `git` with a read-only subcommand from
  {show grep cat-file ls-tree rev-parse log diff ls-files rev-list
  merge-base}; interpreters and constant printers are refused because the
  only legal argv[0] is git (demonstrated: `refuse-interpreter`
  python3, `refuse-constant-printer` echo); any shell metacharacter
  (`| & ; < > ` $(` CR LF) in any element is a refusal
  (`refuse-shell-meta`); an optional leading `-C <dir>` is allowed only when
  `<dir>` resolves inside `--repo` (`refuse-c-traversal` on `-C ..`).
- `parse` / `stated_parse` compile with exactly one capture group
  (`refuse-parse-no-group`); observed token = `parse` searched in observe
  stdout (`re.M | re.S`, the R77 `parse_observed` lineage); stated token =
  `stated_parse` searched in `stated_text`.
- Per-observe timeout 60 s, stdout cap 1 MiB; ledger ≤ 1 MiB, ≤ 500 pairs;
  child env scrubbed (HOME/TMPDIR pinned to `--work`, git terminal prompt and
  system config off); observation argv runs with cwd=repo so a fixture's
  `-C .` reads the guarded repository.
- Exit labels exactly: `LEDGER-GUARD-79: PASS pairs=N` (0);
  `LEDGER-GUARD-79: FAIL pairs=N problems=M` (1) with per-pair lines
  `PAIR <id>: OBS_MISMATCH recorded='<r>' actual='<a>'`,
  `PAIR <id>: NOT_RED token='<t>'`, `PAIR <id>: STATED_MISMATCH …`,
  `PAIR <id>: UNOBSERVABLE <why>`, `PAIR <id>: UNPARSEABLE pattern='<p>'`;
  `LEDGER-GUARD-79: FAIL (refused: <why>)` (2).
- `--emit PATH` writes the contracted strict JSON
  `{"verdict","pairs":[{"id","observed","stated","status"}]}` with status in
  {ok, obs-mismatch, not-red, stated-mismatch, unobservable, unparseable};
  written on refusals too as `{"verdict":"FAIL","pairs":[]}`; the selftest
  cross-checks the clean run's emit against an in-process re-derivation
  (mirrors the counter's independent re-derivation).
- `--selftest` exits 0 and prints the deterministic line
  `SELFTEST: 24/24 scenarios green (clean green-first: yes)` (fixture commit
  dates pinned, so the receipt is stable).

## Choices where the contract was silent (flagged to ExecOCounter)

1. A pair's stated side is validated against committed bytes:
   `stated_text` must equal the base blob's line `stated_at` names. Mismatch
   is an **exit-1 pair problem** `PAIR <id>: STATED_MISMATCH …` (status
   `stated-mismatch`), not a refusal — it requires reading the repository.
2. `stated_parse` not matching `stated_text` is decidable from the ledger
   alone → **exit-2 refusal** (self-inconsistent pair).
3. Refusal class split: everything decidable from ledger+CLI alone is exit 2;
   anything requiring repository access is an exit-1 pair verdict.
4. `disposition`, `expected_after`, `rederive` are accepted, length-capped,
   and **not executed or graded** — the guard validates base observations
   only (documented in the docstring).
5. Strict key set: exactly the documented keys; the R77 scratch probe's `why`
   key is refused (see below).

## What I inspected before designing

- `.ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json` (269
  lines): 11 pairs, argv shape with `observe_cmd`, `rederive`, `parse`,
  `expected_after`, `observed_at_base`, `disposition`, `why`. Its
  `observed_at_base` values are placeholders: D01 records `1`, but the stated
  observe command re-derives `149` at `211f952…` (measured read-only:
  `git show 211f9526800906e0c585d878d265c37e5e090c15:LOG.md | grep -c -E '^#'`
  → `149`). The probe was a shape probe, not a truth probe.
- R77 counter BASEMISMATCH evidence (`stage/ExecAdaptCa/accept-ca.py:1847-1882`
  `leg_basemismatch`, leg text at `:350-352`): stated != observed required,
  recorded `observed_at_base` compared to the actual observation, parse-miss
  and unobservable pairs fail.
- R77 lineage parse compilation: `parse_observed` compiles `parse` with
  `re.M | re.S` (`accept-ca.py:1487`); `stated_parse` searched with `re.M`
  (`:1518`). Mirrored.
- R77 mutation evidence (`MutLedgerPairs.md` §1): interpreter/constant-printer
  refusal and operand-role parsing were the surviving attack classes — both
  are closed here by the git-only argv[0] rule and the pinning rule.

## Unsupported historical shapes — honest report

- The R77 scratch probe is **not gradable as-is** under the strict schema:
  refused exit 2 on its undocumented `why` key (`r77-historical-refusal.txt`).
  Even with `why` dropped, its placeholder `observed_at_base` values (e.g. D01
  `1`) would fail `OBS_MISMATCH` against the actual `149` — shown directly in
  `demo-real-base-red.txt`. Converting a historical pair means: drop `why`,
  record the true observed token, keep the argv pinned at the base.
- REPAIR post-state grading, ANNOTATE rows, `expected_after` enforcement,
  receipt presence and round acceptance legs are **out of scope** — the round
  counter's job, not the guard's.

## Deliverables (all under `.ufo/waves/round-79/w1/stage/ExecGuard/`)

| file | what it is |
|---|---|
| `tools/ledger-token-guard.py` | the draft guard (L1: copy to `tools/ledger-token-guard.py`) |
| `selftest.txt` / `selftest.err` / `selftest.exit` | `SELFTEST: 24/24 …`, stderr empty, `SELFTEST_EXIT=0` |
| `demo-red.json` / `demo-real-base-red.txt` | real D01 pair at `211f952…`, `{base}` placeholders, recorded `1` → `OBS_MISMATCH recorded='1' actual='149'`, exit 1 |
| `demo-green.json` / `demo-real-base-green.txt` / `demo-green.emit.json` | recorded `149` → `LEDGER-GUARD-79: PASS pairs=1`, exit 0; emit JSON shown |
| `r77-pairs-only.json` / `r77-historical-refusal.txt` | R77 probe minus `status` → `refused: … unknown key(s) ['why']`, exit 2 |
| `usage-error.txt` | missing `--repo` → refused label + usage, exit 2 |
| `guard.sha256` | `ccb4ef5e…a986` |

## Selftest coverage (24 scenarios, clean green-first)

Green: `clean` (isolated fixture repo, `rev-parse --show-toplevel` asserted),
`emit-agrees`, `substitute-base`. Exit-1 mutants: `obs-mismatch`,
`not-red`, `unobservable`, `unparseable`, `stated-mismatch`. Exit-2
refusals: `refuse-interpreter`, `refuse-constant-printer`,
`refuse-shell-meta`, `refuse-unpinned-head`, `refuse-other-commit`,
`refuse-mutable-subcommand`, `refuse-c-traversal`, `refuse-parse-no-group`,
`refuse-unknown-key`, `refuse-ledger-base-differs`, `refuse-emit-written`
(emit file still written), `refuse-base-not-hex`, `refuse-repo-missing`,
`refuse-base-not-commit`, `refuse-unwritable-work`, `refuse-usage-label`.

## Evidence (command → raw output)

- `python3 -m py_compile tools/ledger-token-guard.py` → exit 0.
- `python3 -B tools/ledger-token-guard.py --selftest --work …/selftest-final` → exit 0, receipt `selftest.txt` (24/24).
- `… --ledger demo-red.json --repo <lane> --base 211f952… --work … --emit …` → exit 1, `PAIR D01: OBS_MISMATCH recorded='1' actual='149'` (`demo-real-base-red.txt`).
- Same with `demo-green.json` → exit 0, `LEDGER-GUARD-79: PASS pairs=1`; emit `{"verdict":"PASS","pairs":[{"id":"D01","observed":"149","stated":"0","status":"ok"}]}` (`demo-real-base-green.txt`, `demo-green.emit.json`).
- Same with `r77-pairs-only.json` → exit 2 refused `unknown key(s) ['why']` (`r77-historical-refusal.txt`).
- `sha256sum tools/ledger-token-guard.py` → `ccb4ef5e37175b25bf07568f05e7c5dd8e1fb096ea2f961364548a8c10d2a986`.
- Independent cross-check (observed, not run by me): ExecOCounter ran its
  counter's full selftest harness with these production guard bytes swapped in
  — 65/65 scenarios ok, exit 0; clean landing graded `ACCEPT-O-79: PASS
  legs=8/8`; all four junk landings and six controls red
  (`stage/ExecOCounter/cross-selftest-production-guard.txt`).

## Notes / risks

- No tool installs this wave (python 3.14, git 2.56 in place).
- Sibling drafts visible in `git status` (`reports/round-79/`, lane-root
  `tools/ledger-token-guard.py`) are **not mine** — my only writes are this
  report and `stage/ExecGuard/`.
- The 60 s timeout cap is a documented constant, not deterministically
  exercised; the 1 MiB stdout cap is enforced in `run_observe` (a capped
  fixture would need a >1 MiB blob, not materialized).
- Scratch `/fast/scratch/hyaku/kotodama-r79/ExecGuard` removed after receipts
  were copied; the selftest re-creates its fixtures under any `--work`.
