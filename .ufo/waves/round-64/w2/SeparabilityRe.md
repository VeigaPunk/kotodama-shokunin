# SeparabilityRe — round-64 wave-2 separability re-run (revised counters)

Scope: re-run inter-claim separability against the **revised** counters — static path
inventory plus an `open()`-trace of each counter and all its children — and re-run the
two ablations in scratch. No counter was patched; the lane tree was read-only.

Counters under test (byte-bound, read from the working tree):

| claim | file | sha256 | rev / mtime |
|---|---|---|---|
| C | reports/round-64/accept-c.py | `979050ce21fa01758c075745b08bf3ecf7d6e73baad543a1df83f666ecc5de2b` | rev3 |
| O | reports/round-64/accept-o.py | `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7` | rev4, 00:08:52 (m5 fix) |
| Ca | reports/round-64/accept-ca.py | `d0787979ae4e318c4a7cde4385dd2b2e36890f8e258b3733cc1a6e980533f917` | rev2 |

The counters moved during this review (C to rev3, Ca to rev2, O rev4 then a 00:08:52 m5 fix). Evidence below is
regenerated at the hashes above. The revisions are read-set neutral: C's open/subprocess
sites are unchanged (155/169/400/412, git 115/383/419, subprocess 268/393/435); Ca's only
shift by three lines (read() 74-76 called at 80/81/100/134, `git show` 111); O's only
root-relative read is still `src = os.path.join(root, TOOL)` (467) copied into the
mkdtemp work dir (480-487). `tools/reopen-row.py` is byte-identical to the base
(`c0f10a84…` both sides). Ca moved once more during the review (NITS now pins the
round-63 numeric-corrections record); at `d0787979…` the read set is identical
(`read()` 74-76 called at 80/81/100/134, `git show` 111), cross-claim opens are 0, and
ACCEPT-CA-64 PASSes. The churn was in leg logic and datum, never in the read set.

## Verdict

**Separability holds: no counter reads another claim's land or receipt, and no counter
invokes another counter.** Each predicate is scored by its own counter alone, on its own
lands. Of the two intra-claim defects reported at rev3, the `--only` fail-open is
**closed** (unknown selectors exit 2) and the m5 kill-attribution repair is **fixed and
verified**: it was broken in the 23:54 bytes (mutant did not compile), and the 00:08:52
bytes compile, give `EDGE_SCHEMEREL PASS` / `EDGE_SLASHLESS FAIL`, and `MUT PASS`. This
seat ran MUT and leg subsets, not a full 23-leg acceptance run.

Method note: no `lsp` device is exposed to this seat (toolset is read/bash/edit/eval/
glob/grep/task/wait/web_search/write), and the property under test is a runtime data-flow
one rather than a symbol-reference one; evidence is therefore kernel-level. Every
`openat`/`open` was traced with `strace -f` over the counter and all children
(`git`, `python3 -B` subprocesses, the tool under test). A cold/empty grep result was
never used as absence: each trace is a full run at the pinned hashes.

## Cross-claim read matrix (dynamic)

Traces (scratch, final bytes): `…/SeparabilityRe/trace-c3.log`, `trace-ca5.log`,
`trace-o.log` (+ the partial `trace-o3.log` at rev4).

| counter | lane-root paths opened | writes | O lands | Ca lands | C lands (measured) |
|---|---|---|---|---|---|
| C | own `accept-c.py`; `corpus/SOURCES.md`; `corpus/README.md`; 244 files under `corpus/knowledge/**` (via sweep); `tools/check-cited-lines.py`; `reports/round-28/readme/sweep.py`; `reports/round-61/reopen-quote.py`; `.git` objects | none (only `/dev/null`) | 0 | 0 | its own |
| O | `tools/reopen-row.py`; own `accept-o.py`; `.git` none | only `/tmp/accept-o-64-*` and `tempfile` (`/tmp/5t6fxc27`) | own | 0 | 0 |
| Ca | `LOG.md`; `corpus/LOG.md`; `SCORECARD.md`; `reports/round-63/telemetry/revisions.txt`; own `accept-ca.py`; `.git` object for `BASE:corpus/SOURCES.md` | none (only `/dev/null`) | 0 | own | 0 |

Targeted greps over the same traces for the other claims' exact land paths returned 0
matches: C never opens `LOG.md`/`SCORECARD.md`/`revisions.txt`/`accept-o.py`/`-o.txt`;
O never opens any C or Ca land, `telemetry`, or `corpus/`; Ca never opens
`accept-c.py`/`accept-o.py`/`-o.txt`/the entry/`corpus/README.md`. No counter opens
`.ufo/` staged rows (`grep -c '\.ufo'` = 0 in all three traces).

A second independent O trace over the core legs (`trace-o-fast.log`, `--only
TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR`, exit 0) shows the same lane-root
surface — `tools/reopen-row.py`, `reports/round-64/accept-o.py`, the `reports/round-64`
directory — with every fixture registry (`SOURCES.md`, `PRIV.md`, `home/corpus/SOURCES.md`,
…) under `TMPWORK` only.

Static corroboration (current bytes, line numbers): C reads at 155/169/400/412 with git
at 115/383/419 and subprocess at 268/393/435; Ca's only reader is `read()` (74-76) called
at 80/81/100/134 plus `git show` at 111; O's only root-relative read is
`src = os.path.join(root, TOOL)` (467) copied into the mkdtemp work dir (480-487), all
registries written under that work dir. `reports/round-64/accept-ca.py:17` mentions
`S694-S717` only as docstring prose (the HISTOGRAM window); no counter references
S718-S749 outside C.

## Ablations (scratch only; lane untouched)

1. **C absent → ACCEPT-C FAIL.** Run at the current tree (entry file absent, no staged
   registry rows): `python3 -B reports/round-64/accept-c.py --root .` → exit 1,
   `ACCEPT-C-64: FAIL`. FILE, ROWS, REJECTS, ONEID, APPEND, NOHARM, SWEEP, LIVE fail;
   ONEID detail `citations_exactly_once=False missing=[S718…S743]` (rev3 check active).
   RESTATE/HOSTS/LINK pass vacuously with `lines=0` — vacuity cannot green the claim
   because ONEID/ROWS/APPEND/NOHARM/SWEEP/LIVE all fail without the datum.
2. **Records-only → ACCEPT-CA FAIL on the pinned legs.** Scratch clone
   (`git clone --local`, then BASE `LOG.md`/`SCORECARD.md`/`corpus/LOG.md` + a prose-only
   `reports/round-63/telemetry/revisions.txt` carrying no hashes or receipt names) →
   exit 1, all 7 legs FAIL including PTRS, HISTOGRAM and REVNAMES. HISTOGRAM's detail is
   the sharp case: `tiers={'A': 13, 'B': 11}` is arithmetically right but
   `correction_present=False` — the leg keys on the recorded correction value, so prose
   without the named values cannot pass. Same result reproduced on rev2 bytes
   (`seat_reports_nit=False duplicate_url_nit=False fail_legs_nit=False`).

## Dependency classification

- **C — shared-tool dependency (not inter-claim).** sweep.py and check-cited-lines.py are
  unpinned shared tools; reopen-quote.py is content-pinned to its BASE sha at runtime
  (lines ~419-426) and fails closed on mismatch or unreadable bytes. NOHARM constrains
  any sibling corpus/knowledge edit to exactly the new entry.
- **Ca — frozen-BASE dependency.** HISTOGRAM reads `corpus/SOURCES.md` only as
  `git show BASE:corpus/SOURCES.md`; C's *measured* registry cannot influence Ca.
  If the base blob is unreachable the leg sees an empty registry and fails closed
  (static reading of 108-117).
- **O — tool-only dependency.** The tool under test plus its own counter file; no
  registry, knowledge, log, or telemetry read. MUT re-invokes this same counter
  (`os.path.abspath(__file__)`) against a scratch mroot inside the work dir.
- No receipt-as-proof: none of the three counters reads any `telemetry/*` file as
  evidence (Ca's `revisions.txt` is its own declared land and its datum, not another
  claim's receipt).

## Findings

**F1 — RESOLVED in rev4 (was MEDIUM; wave-1 ReviewerCounterO2 H2).** rev3 failed open on
an unknown `--only` name (ten `SKIP` lines, `ACCEPT-O-64: PASS`, exit 0, zero legs).
rev4 validates the selector set against `ALL_LEGS` (446-450): `python3 -B
reports/round-64/accept-o.py --root . --only NOSUCHLEG` now prints
`ACCEPT_O_INPUT_ERROR unknown --only leg(s): NOSUCHLEG` and exits 2 (verified at
both `6d9c9354…` and `760ddd4d…`). The zero-leg green path is closed; no further action.

**F2 — RESOLVED at 00:08:52 (was HIGH in the 23:54 rev4 bytes).** The 23:54 bytes added
the isolation the wave-1 receipt asked for (m5 runs the pair `EDGE_SCHEMEREL,
EDGE_SLASHLESS`, 1094-1096; MUT requires `EDGE_SCHEMEREL PASS`, 1115-1121) but the m5
replacement was syntactically invalid: a 12-space `if (` followed the tool's 8-space
`parsed_location = …` assignment, so the mutant did not compile
(`IndentationError: unexpected indent (reopen-row.py, line 605)`; mutant sha256
`795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6`, matching the
RevVerifyO2 seat's independent build). Both legs then failed with `rows=[]` (tool crash),
the isolation check recorded `m5:EDGE_SCHEMEREL isolation=[…FAIL…]`, and
`--only MUT` gave `MUT FAIL … ACCEPT-O-64: FAIL`, exit 1 (255.3 s) — claim O could not
pass. The 00:08:52 bytes dedent the replacement (8-space `slashless_relative = (` /
`if` / `else`, 12-space bodies) and fix the inverted revision-4 docstring. Verified:
mutant sha256 `f04dc0029ed89fc35abd36564907ab2e47c1b44ca0baed4b7528327b5de3e710`,
`PY_COMPILE OK`, `EDGE_SCHEMEREL PASS rows=[('S…','REFUSED',1)]`,
`EDGE_SLASHLESS FAIL rows=[('S…','UNREACHABLE',2)] root_hits=1`, and `--only MUT` →
`MUT PASS bad=[] mutants=10 … ACCEPT-O-64: PASS`, exit 0. No action left on this finding.

**F3 — LOW (identity coherence, claim C).** Two byte sources for "the entry":
FILE/RESTATE/LINK score the working tree; SWEEP runs over the working tree; NOHARM
scores the committed `main` (`git diff BASE main`, 383). In a clean checkout at the
measured revision they coincide; in the jj working copy they can diverge (a green
NOHARM can certify a committed entry while FILE scores different uncommitted bytes).
Fail-closed today (both legs fail while the datum is absent). Repair direction: diff
the working tree, or pin and print the measured revision.

**F4 — LOW (operability/diagnostics; `--only` is a report filter, not an execution
filter, for the CORE block).** A single `if run_core:` (499) wraps the entire core
section; `need()` gates only the EDGE/DRIP/MUT sections. Requesting any one core leg
therefore runs every core scenario — including the DEFAULT dead-host scenario, which
spends ~150 s (9 attempts in three bursts with 60 s gaps, 612-632). `--only
TOOL,INDEP,GEN` prints those three legs PASS then stalls in the unrequested DEFAULT
workload and is killed by a 120 s/90 s timeout (exit 124; reproduced twice, with and
without strace); the run only completes at ~158 s. Subset runs are not cheap. The frozen
predicate runs every leg, so acceptance is unaffected.

## Residual risk and verification gaps

- The e2e O trace was taken at rev3 (`c27a9fef…`): 22 of 23 legs (MUT skipped, 171.8 s,
  exit 0 with the requested legs PASS). rev4 changed only MUT/`--only` logic and the read
  sites are identical (467/480-487); a rev4 subset trace (`TOOL,INDEP,GEN`) reached
  TOOL/INDEP/GEN PASS and the same lane-root read set (`tools/reopen-row.py`, its own
  counter) before being killed at 120 s inside the unrequested DEFAULT workload (F4).
  MUT's read surface remains static-only: it re-invokes this counter under a scratch
  mroot inside the mkdtemp work dir. The core-leg trace took 158.7 s, of which the
  DEFAULT leg alone is 150 s; budget minutes, not seconds, for a full 23-leg acceptance
  run. No correctness impact.
- C's LIVE leg did not reach the network (all six ids absent → `no_row`), so the
  locator's network surface is untraced; it is invoked only as the pinned locator with
  `--row`.
- The only lane paths in the C trace that are not lands or tools are failed lookups
  (`ENOENT`) for `uv.toml`/`pyproject.toml` walking up the parent chain — neither file
  exists in the lane, so they read no data (interpreter/environment discovery).
- Concurrent churn: C rev3, Ca rev2 (twice) and O rev4 (twice, including the m5 fix)
  landed mid-review. If the L1 stamps further counter revisions, re-check the read sites
  listed above (C 155/169/400/412; Ca 74-76/111; O 467/480-487) against the new hashes.
- Ca's PTRS/NITS/R63SEP are record-string legs over its own lands; by design they
  certify that the named values are recorded, not that the underlying numerics are right.
  HISTOGRAM is the one computed leg and it is arithmetic-independent of the prose.

## Tooling

No installs or upgrades performed; pacman untouched.

Report: .ufo/waves/round-64/w2/SeparabilityRe.md
