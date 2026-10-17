# Round 5 — assignment 03: isolated seven-gate battery

Lane: kotodama-shokunin round 5, worker 03 (executor, isolated battery).
Baseline revision: `1ccb2b7119039d8026ad1d004f20427623838b94`.
Scope honored: I touched only `tools/check-gate-battery.py` (new) and this
report. No gate script, fixture, frozen byte, ledger, corpus file or shared
bookkeeping file was modified.

## Work performed

- Read the operative contracts (`AGENTS.md`, `reports/round-5/flash-claims.json`,
  `reports/round-5/flash-authorization.json`) and confirmed the baseline hash.
- Confirmed the isolation premise: all seven gates resolve their fixtures via
  `__file__` (e.g. `tools/gates/lexicon-coverage-audit.py:124-126`,
  `tools/gates/myth-consistency-gate.py:100`), so copying the seven scripts plus
  `tools/gates/fixtures/` into a mirror makes every selftest — including the
  ones that rewrite fixtures in place (`provenance-audit.py:403-426`,
  `myth-consistency-gate.py:1066`) — run entirely on mirror bytes.
- Implemented `tools/check-gate-battery.py` (stdlib only, Python 3):
  - Fixed internal tuple of the seven gate names; nothing is read from or
    executed via any manifest, and no shell string is ever built. Each child is
    launched as `[sys.executable, <resolved mirror path>, "--selftest"]` with
    `shell=False`, `cwd=mirror`.
  - Copies the seven scripts (`shutil.copy2`) and the fixture tree
    (`shutil.copytree`) into a disposable `tempfile.mkdtemp` mirror; verifies
    the copies hash-identical to the sources before launching anything.
  - Hashes all 28 live originals (7 scripts + every fixture file) before and
    after the run; a mismatch is reported (`GATE-BYTES-CHANGED`) and forces
    exit 2 — copying alone is not treated as proof the live tree stayed
    read-only; the hash comparison is the proof.
  - Exit semantics: 0 all seven selftests exit 0 and originals preserved;
    1 at least one selftest ran and exited 1 (genuine finding,
    `GATE-SELFTEST-FAIL`); 2 could-not-evaluate — missing gate file
    (`GATE-FILE-MISSING`), copy mismatch (`GATE-COPY-MISMATCH`), launch error
    (`GATE-LAUNCH-ERROR`), timeout (`GATE-TIMEOUT`), abnormal child exit
    (`GATE-ABNORMAL-EXIT`), or changed live bytes. A non-clean child exit code
    other than 1 classifies as unevaluable. Any unevaluable gate dominates.
  - Bounded diagnostics: per-child stdout/stderr capped at 2000 chars with
    `*_truncated` flags; durations recorded; mirror paths masked to basenames in
    echoed argv; default per-gate timeout 120 s (`--timeout`), mirror kept only
    with `--keep-mirror`.
  - `--selftest`: five isolated controls on synthetic children in their own
    temp dir, never touching live paths — clean-pass control (`CTRL-PASS-EXIT0`,
    expects exit 0/pass), negative exit control (`CTRL-FAIL-EXIT1`, expects
    observed exit 1, outcome `fail`, battery mapping 1), missing-gate case
    (`CTRL-MISSING-GATE`, expects stable id `GATE-FILE-MISSING`, mapping 2),
    timeout case (`CTRL-TIMEOUT-GATE`, 1 s budget vs a sleeping child, expects
    `GATE-TIMEOUT`, mapping 2), and a stable-ID shape control
    (`CTRL-STABLE-IDS`: every emitted control and finding id must match
    `^[A-Z][A-Z0-9-]+$`).

## Landed changes

- `tools/check-gate-battery.py` (new, 12108 bytes at first write, verified with
  `python3 -m py_compile`).
- `reports/round-5/03-isolated-battery.md` (this file).
- Not landed by me: LOG.md/SCORECARD.md integration and any commit — the lane
  parent owns those; my files are working-tree deliverables.

## Commands and observed exits

All run from the repo root on 2026-10-17, Python 3.14.7.

| Command | Exit | Result |
|---|---|---|
| `python3 -m py_compile tools/check-gate-battery.py` | 0 | compiles clean |
| `python3 tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 5/5 controls behaved as expected` |
| `python3 tools/check-gate-battery.py` | 0 | JSON report: `pass=7 fail=0 unevaluable=0`, `originals.preserved=true` over 28 files, mirror removed |
| `python3 tools/check-gate-battery.py --timeout 0.001` | 2 | forced negative demo: all seven gates `GATE-TIMEOUT`, battery exit 2, originals still preserved |

All seven observed gate selftest exits in the default run were 0:
costume-era-consistency-gate 0, handoff-packet-check 0,
lexicon-coverage-audit 0 (`selftest: 14/14 checks passed`),
myth-consistency-gate 0, naming-collision-gate 0, phonology-sanity-gate 0
(`15/15 planted finding IDs present; 26 control cases passed`),
provenance-audit 0 (stdout truncated by the report cap, as designed).

After every run, `git status --porcelain tools/gates/` was empty: the live gate
scripts and fixtures kept baseline bytes throughout, including across the
fixture-rewriting selftests and the timeout run.

## Before → after

- Before: no standalone isolated battery existed; the seven legacy selftests
  could only be exercised in place, and several of them rewrite
  `tools/gates/fixtures/` live (my earlier single live `provenance-audit.py
  --selftest` probe regenerated identical bytes, which is luck, not a
  guarantee).
- After: `python3 tools/check-gate-battery.py` runs all seven selftests against
  a disposable mirror with measured (not assumed) preservation of the 28 live
  files, exits 0/1/2 per the contract, and `--selftest` proves the pass/fail,
  missing-gate, timeout and stable-ID behaviors on synthetic children. This
  feeds claim O's "isolated battery actually runs all seven original gate
  selftests in a copied tree" requirement; the malformed craft-CLI controls and
  historical manifest replays named in claim O belong to other assignments and
  were not touched here.

## Limits

- The battery proves the seven selftests pass on unchanged bytes in this
  environment; it does not make the legacy selftests themselves read-only
  (they still rewrite fixtures when run live outside the mirror).
- Per-child diagnostics are capped (2000 chars/stream); truncated streams are
  flagged, not stored in full.
- The timeout control and forced `--timeout` demo kill children at the
  subprocess level; a gate that traps SIGKILL-equivalent shutdown is out of
  scope for stdlib `subprocess.run` semantics.
- No network, no provider access, no delegation, no commits; unreviewed by
  anyone but me — parent judging is the only admission authority.

---

# Revision 2 (2026-10-17, post review `reports/round-5/15-cli-review.md`)

## Explicit corrections to the original sections above

- **Byte hashes prove byte preservation, NOT absence of writes.** The
  before/after sha256 comparison can only detect a change in content, path set
  aside; a selftest that rewrites a fixture with identical bytes passes the
  check. "Preserved" in this report means "bytes and path set identical before
  and after", never "nothing was written".
- **"could only be exercised in place" was false.** A prior supplemental parent
  runner already executed an isolated battery of the gate selftests; the
  original Before bullet overstated the gap. What this round adds is a
  *standalone committed entry point* (`tools/check-gate-battery.py`) with a
  stable CLI, exit contract and selftest — not the first isolated execution.

## Repairs for review findings (P1, P3, P4 — battery items only)

- **P1 (HIGH) — fixed.** An exit-1 child is a genuine test failure (battery
  exit 1) only if its captured output contains line-anchored stable failure
  evidence drawn from the legacy gates' own conventions: a line starting
  `SELFTEST FAIL` (provenance-audit.py:489, lexicon-coverage-audit.py:1413),
  `FAIL <token>` (lexicon-coverage-audit.py:1501 check printer,
  check-craft-exercise.py finding printer) or `failed: <token>`
  (lexicon-coverage-audit.py:1504). Any other exit-1 child — including an
  uncaught traceback — gets stable finding `GATE-CRASH-EXIT1`, outcome
  `unevaluable`, battery exit 2, with a bounded `stderr_tail` (600 chars) kept
  for crash diagnosis. Recognition runs on the full captured output, before
  the 2000-char report cap. Conservative distinction, documented in the module
  docstring: five of the seven legacy gates (costume-era, handoff, myth,
  naming, phonology) fail via bare `assert` → traceback, so a *genuine*
  selftest failure in those gates now classifies as exit 2, not exit 1. The
  battery is nonzero either way; it only refuses to vouch for "genuine finding"
  without stable evidence. No legacy gate bytes were changed.
- **P3 (LOW) — fixed.** Preservation now compares the path set as well as
  per-file digests: `originals` reports `modified` / `added` / `deleted`
  counts, any of which forces `GATE-BYTES-CHANGED` and battery exit 2. A pure
  `diff_snapshots` helper is unit-checked by control `CTRL-TREE-DIFF`.
- **P4 (LOW) — fixed.** `--timeout` uses a validating type: zero, negative,
  non-numeric and non-finite values are usage errors (argparse exit 2), so no
  absurd all-timeout run can be launched with a nonpositive budget.

## Repair verification — exact commands and outcomes

All from the repo root on 2026-10-17, Python 3.14.7; `python3 -m py_compile
tools/check-gate-battery.py` → exit 0 first.

| # | Command | Exit | Outcome |
|---|---|---|---|
| 1 | `python3 tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 9/9 controls behaved as expected` — controls: PASS-EXIT0 pass; RECOGNIZED-FAIL (`SELFTEST FAIL:` line, exit 1) → fail/exit 1; FAIL-LINE-ID (`FAIL <tok>` + `failed:` lines) → fail/exit 1; EXIT1-UNRECOGNIZED (bare exit 1) → GATE-CRASH-EXIT1/exit 2; CRASH-EXIT1 (`raise NameError`, traceback) → GATE-CRASH-EXIT1/exit 2 with `NameError` in stderr_tail; MISSING-GATE → GATE-FILE-MISSING/2; TIMEOUT-GATE → GATE-TIMEOUT/2; TREE-DIFF (modified+added+deleted detected); STABLE-IDS (all ids match `^[A-Z][A-Z0-9-]+$`) |
| 2 | `python3 tools/check-gate-battery.py` | 0 | 7/7 pass, `originals` modified=0 added=0 deleted=0 preserved=true over 28 files, mirror removed |
| 3 | `python3 tools/check-gate-battery.py --timeout 0` | 2 | usage rejected, no children launched |
| 4 | `python3 tools/check-gate-battery.py --timeout -5` | 2 | usage rejected |
| 5 | `python3 tools/check-gate-battery.py --timeout abc` | 2 | usage rejected |
| 6 | `python3 tools/check-gate-battery.py --timeout inf` | 2 | usage rejected |
| 7 | `python3 tools/check-gate-battery.py --timeout 0.001` | 2 | forced all-timeout: 7× GATE-TIMEOUT, unevaluable=7, preserved=true |

P1 end-to-end repro of the reviewer's R1 class, in a `/tmp/p1demo` sandbox
(copy of the tool + fake gates with real filenames; deleted afterwards; zero
`gate-battery-*` dirs left in /tmp):

| # | Sandbox setup | Exit | Outcome |
|---|---|---|---|
| 8 | six exit-0 fake gates + `myth-consistency-gate.py` = `raise NameError("boom")` | 2 | summary pass=6 unevaluable=1; the crashing gate: observed_exit 1, outcome `unevaluable`, finding `GATE-CRASH-EXIT1`, traceback visible in bounded stderr_tail — no longer misreported as a genuine finding |
| 9 | same, but the fake gate prints `SELFTEST FAIL: planted-evidence` then exits 1 | 1 | summary fail=1 pass=6; genuine recognized failure still maps to exit 1 |

`git status --porcelain tools/gates/` empty after every run; no legacy gate,
fixture or frozen byte changed (fixes live entirely in
`tools/check-gate-battery.py` and this report).

## Revision 2 limits

- The crash-shape reclassification is lossy by design: for the five
  assert-based gates, exit 2 means "child exited 1 without stable evidence",
  which may be either a crash or a genuine but evidence-less selftest failure;
  the stderr_tail excerpt (600 chars) is the diagnostic path, not the exit
  code. Disambiguating further would require editing legacy gates, which the
  contract forbids.
- `CTRL-TREE-DIFF` checks the pure diff helper on synthetic dicts; the
  end-to-end added/deleted path under the *live* tree is covered by design
  (rglob sets before/after), not by a live mutation — deliberately, since
  mutating live fixtures to prove detection would itself be a no-harm
  violation.
- Everything from Revision 1 still holds: no manifest-command execution, fixed
  argv, disposable mirror, bounded diagnostics, author-side only, uncommitted;
  landed means committed and the parent owns that commit and round judging.

## Parent integration correction — final delivered controls (2026-10-17)

Revision 2's nine-control count describes that intermediate executor revision,
not the final deliverable. The parent added a traceback veto before stable
failure-marker recognition and `CTRL-MARKER-THEN-CRASH`: a child that prints
`FAIL MYTH-X: seeded` and then emits a Python traceback is now unevaluable,
battery exit 2, rather than a recognized failure/exit 1. The final
`python3 tools/check-gate-battery.py --selftest` passes **10/10**, and the
standalone default battery still passes seven of seven copied-tree selftests
with the original bytes and path set preserved. `reports/round-5/validation.json`
records the actual commands and tested SHA256
`077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67`.

The final bounded re-review in `15-cli-review.md` observed this behavior.
`battery-mutation.json` records that deleting only the veto in a scratch copy
makes the new control reject that mutant. This is one bounded mutation, not
universal coverage. Exit-0 children remain trusted; the wrapper is not an OS
sandbox, and byte equality does not prove absence of writes. Historical
intermediate observations above remain intact.
