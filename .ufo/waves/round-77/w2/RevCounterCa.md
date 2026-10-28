# RevCounterCa — W2 falsification of the staged round-77 `accept-ca.py` + ledger schema

Seat: RevCounterCa (leaf, attack-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base: `211f9526800906e0c585d878d265c37e5e090c15`. Target (the only final staged copy; `reports/round-77/`
holds just `telemetry/` until the L1 installs): `.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py`
(4040 lines). Named W1 grounding: `.ufo/waves/round-77/w1/ExecAdaptCa.md`. No task/delegation, no
background jobs, no installs (python 3 + git in place were sufficient; pacman untouched). No lane file
outside this wave dir was written. Lane git/jj/index untouched (read-only `git -C …` calls only).

---

## 1. Artifact identity and reproduction of the W1 build claims

| check | command (abbreviated; full form in transcript) | raw result |
|---|---|---|
| staged bytes unchanged since W1 | `sha256sum …/ExecAdaptCa/accept-ca.py` | `ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e` — equals W1's claim |
| leg table source of truth | `python3 -B accept-ca.py --emit-legs \| python3 -c …` | `legs: 12`, `digest: 0f40d78e029f4104e04c89f688a0987e02ddc8466f7ac7eea3930ce48bfa94bd`, names `LEDGER BASEMISMATCH REPAIR ANNOTATE APPENDONLY R1EXEMPT NOSTUB SEPARABLE COMBINED RECEIPTS FROZENCFG STAMP` — equals W1's claim |
| selftest re-run in my scratch | `HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r77/RevCounterCa/selftest python3 -B accept-ca.py --selftest` | `exit=0`, `SELFTEST OK: 199 checks across 51 scenarios reported-fail=0`, `SELFTEST: 199/199`; stderr carries only the three deliberate CLI-error probes — matches W1 |
| real-base build check re-run | `… --ledger-check …/probe-real-ledger.json --root <lane> --base 211f952…` | `LEDGER-CHECK-77: PASS pairs=11`, `exit=0` |
| no `/tmp` literal | `grep -n '/tmp' accept-ca.py` | no match (exit 1) |

Ledger schema (effective, from `load_frozen` + `pair_problems` + the W1 probe): ledger object
`{round, claim, base, pairs[], fleet_pin?, fleet_report?/fleet_sha256?}` (a bare list is also accepted);
pair `{id, disposition: REPAIR\|ANNOTATE, stated_at "path:line", stated_text, stated_token?/stated_parse?,
observe_cmd [argv], parse (compiling regex with capture group, or "count-presence"), expected_after,
rederive? (string; defaults to shlex.join(observe_cmd)), statement_after {path, parse} (REPAIR only),
observed_at_base?, why?}`. Schema shape is sound; the gaps below are semantic.

## 2. Verified sound (attacked, held)

- **stated_at allowlists** (`pair_problems`, `_lane_site`, `_allow_for`): lane-only `path:line`
  (absolute/fleet/`..`/multi-colon/non-numeric refused), exact per-disposition membership in
  `ANNOTATE_ALLOW`/`REPAIR_MUTABLE`; a bad disposition fails on its own, so the allowlist can't be
  skipped into a pass.
- **stated_text at base**: must be a substring of the normalized base file AND of the normalized
  stated line (`show(base_clone,"HEAD",path)`), EOF/line-0/negative refused. Closes L76-19 as claimed.
- **argv grammar** refusals all reproduced by the selftest (shell string, interpreters/constant
  printers, bare `name=value`, backtick/escaped-pipe outside a PATTERN, `git` without leading `-C`,
  `-c`/`--git-dir` class global opts, grep without path operand, stdin `-`, dead 40-hex pin,
  mutable-ref operands for `git grep`/`git diff`). Two admission gaps survive — F4/F5.
- **REPAIR landing**: truth at lands observable, `statement_after` last-match == truth, != base
  statement, base `stated_text` absent from statement lines (shadow-append rule, README:805-style
  prose mention tolerated exactly as documented), `expected_after` pinned, claim-C `owned_inplace`
  collision refused (`_c_appended_line`).
- **ANNOTATE/NOSTUB**: leading-id rows, old+new token boundary-matched (`token_in`), rederive command
  verbatim in row, rederive re-executed at lands and must equal the observed token, count pairs must
  pin the 40-hex base, placeholder-token guard. Vacuous-green only when the ledger has zero ANNOTATE
  pairs (all-REPAIR ledgers are legitimate per the claim text).
- **R1EXEMPT**: fixtures read from the freeze blob (never the worktree), re-built and re-graded live
  (green→APPENDONLY green, teaches→red, teaches+used-by→red), receipts must carry
  `LEG PASS/FAIL APPENDONLY` + exit 0/1 at the freeze. Both ways really proven.
- **RECEIPTS**: never vacuously green (`if not named: FAIL`, line 2484); pair-named + fixture-named +
  R1 receipt paths resolved with `git cat-file -e <freeze>:<path>`. The r76 "cited but never
  committed" class is closed.
- **COMBINED line-number**: `_readme_exemption_problems` refuses a record without integer
  `base_line`/`line`, and checks `base_lines[n-1] == base_text` / combined `lines[n-1] == after_text`
  byte-exact at both trees; a whole-file README exemption is refused (line 2160). The r76 COMBINED
  defect class is closed. (`owned-inplace-shifted` has no selftest scenario, but the byte-exact check
  catches shifts by construction.)
- **FROZENCFG**: LEGCOUNT refusal on name/order mismatch (line 2899), freeze ancestor of lands on the
  first-parent chain, base ancestor of freeze, claims+ledger blob-identical freeze↔lands, frozen
  allowlists re-derived from the leg text and compared to the constants, legs digest checked when
  present.
- **STAMP**: header grammar matches `tools/check-receipt-seq.py` (headers only — leg order is not
  consumed by it), tree == `rev-parse lands^{tree}`, counter self-sha, `outside_clone` tripwire.
  One weakening — F6.
- **Refusals**: missing `--combined`, `lands == base`, do-nothing `freeze == lands` all-green,
  missing scratch root, non-commit revs, non-40-hex revs — all exit 2 with no leg line. Re-executed
  via the selftest.

## 3. Findings by severity

### F1 — HIGH — an unbound `fixed_surfaces` entry is an unlimited whole-file APPENDONLY exemption

`leg_appendonly` exempts any changed non-protected, non-SOURCES path from the changed-line whitelist
when the frozen Ca claim carries `fixed_surfaces: [{path: P}]` **without** `line` (2117–2180); the
only refusal is for `README.md` basenames (2160). Without `sha256` there is no pin; without
`required` the REPAIR-leg loop (1965–1978) skips it too. `load_frozen` accepts such an entry
unchecked (859–861). The docstring blesses "an entry with neither is a whole-file exemption"
(line 193) — but the frozen APPENDONLY sentence the L1 will freeze says changed lines are "a subset
of the stated_at lines of REPAIR pairs, claim-C owned in-place lines …, plus appended lines"; the
counter admits a class the sentence does not name. Executed proof (fixture lane, both arms identical
landing with one SKILL.md prose line rewritten post-freeze, `python3 -B fs_probe.py`, staged under
`.ufo/waves/round-77/w2/stage/RevCounterCa/`):

```
=== arm ctrl (no fixed_surfaces): exit=1  APPENDONLY FAIL  COMBINED FAIL  → ACCEPT-CA-77: FAIL legs=10/12
injected fixed_surfaces: [{"path": "SKILL.md"}]
=== arm mut:                     exit=0  all 12 PASS       → ACCEPT-CA-77: PASS legs=12/12
```

In the real lane SKILL.md is REPAIR_MUTABLE and NOT protected, so `{"path": "SKILL.md"}` would let
the landing rewrite SKILL.md arbitrarily post-freeze with zero pair accounting. The exemption also
propagates into the COMBINED probe (same `fixed_surfaces` in the re-run). Minimum guard the L1/next
counter rev should add: refuse a whole-file `fixed_surfaces` entry that lacks both `sha256` and
`required` (and any entry on a protected path).

### F2 — HIGH — SHONEN.md non-mark prose changes are graded by no leg at all

For protected paths the changed-line whitelist is skipped entirely (`if path in protected_paths:
continue`, 2145–2146), and SHONEN.md's protected scope is only its mark lines
(`_shonen_mark_lines`: checklist `- [x]`-class lines + the `Marks:` legend block). Removed-line
grading therefore covers only mark lines; **prose-line rewrites of SHONEN.md are invisible to
APPENDONLY (main run and COMBINED probe)** and to every other leg. Executed proof — control arm of
the same driver, SHONEN.md prose line (`  asserted: old` under item one) rewritten post-freeze with
NO exemption and NO pair:

```
=== arm ctrl (SHONEN rewrite, no fixed_surfaces): exit=0, 12/12 PASS, ACCEPT-CA-77: PASS legs=12/12
```

Adjacent-but-distinct: W1 RevSeparability F4 flagged that mark lines are unrepairable (ledger
admission); this is the inverse hole — non-mark content is unpoliced (landing freedom). The frozen
sentence ("zero removed lines in … SHONEN.md's mark lines") reads as if intended, so this is a
spec+implementation gap to surface, not a coding slip: the promotion-carrier file can be reworded
post-freeze without any falsifier noticing.

### F3 — MEDIUM — "≥ 10 unique pairs" is id-uniqueness only

`leg_ledger` dedups on `id` alone (1776–1786; same in `run_ledger_check`); no cross-pair content
comparison exists. Ten content-identical pairs with distinct ids satisfy the floor. Executed proof:

```
10 × deep-copy of probe pair D01, ids PAD01..PAD10 →
python3 -B accept-ca.py --ledger-check probe-dup.json --root <lane> --base 211f952…
LEDGER-CHECK-77: PASS pairs=10   exit=0
```

`--ledger-check` is the same `pair_problems` the LEDGER leg runs, so the graded leg admits it too.
The L1 should freeze "10 pairs with pairwise-distinct (stated_at, observe_cmd, parse) triples" or
the counter should enforce it.

### F4 — MEDIUM — a mutable ref is admitted in revision position for every non-grep/diff subcommand

`_git_problem` applies `_mutable_ref` only in `_git_grep_problem`/`_git_diff_problem`; for
`show`/`log`/`cat-file`/… a bare word operand falls through every check (1152–1170:
`_pathspec_ok` false, no `:`, no `/`, no known extension → accepted). Executed proof (inside a
ledger that passes the build check, so the LEDGER leg would admit it at grading):

```
"observe_cmd": ["git","-C",".","log","-1","--format=%H","main"], "parse": "([0-9a-f]{40})"
LEDGER-CHECK-77: PASS pairs=11  (mutant probe-mutants.json, exit=0)
```

The routed r76 defect ("immutable revision in revision position") is thus only half-closed: grep/diff
pinning is enforced, `show`/`log` observations can still drift with a branch. The clone is
counter-materialized, which caps the damage, but the ANNOTATE count-pair rule (base pin) shows the
intent — extend the mutable-ref refusal to all subcommands.

### F5 — MEDIUM-LOW — the frozen LEDGER sentence promises `-- <path>`; the code enforces it only for grep

The frozen leg text the L1 must freeze verbatim says every argv is "in the form
`git -C <dir> <sub> ... <rev> -- <path>`". `_git_problem` enforces a path operand only inside
`_git_grep_problem` ("git grep has no path operand"); `git show <rev>` with no `--` and no path is
admitted. Executed proof (same mutant probe, exit 0, pair executed): `["git","-C",".","show","HEAD"]`.
A pair can therefore pass the leg while violating the frozen grammar sentence — a text/code
mismatch inside a claim whose whole point is that the frozen text is enforced.

### F6 — MEDIUM-LOW — STAMP `measured` silently falls back to the worktree HEAD

`main_check` 2927–2933: when `--main` does not resolve, `measured = git(root,"rev-parse","HEAD")`
with only a printed NOTE; STAMP then compares measured to lands. Executed proof: lane whose `main`
stays at the combined commit, worktree checked out at the Ca landing, `--main no-such-branch`:

```
# measured revision (lane main): 3dd6543a672e5106fdf4bcbb92b179bd5977f54e   (fallback HEAD)
ACCEPT-CA-77: PASS legs=12/12   exit=0   STAMP PASS
```

So "stamped == evaluated == measured == <lands>" can be satisfied by the operator's checkout state
rather than by the lane's `main` being pinned — the exact r65/66 worktree-drift class that
`check-receipt-seq.py` only flags. The selftest's `stamp-measured` uses a resolvable wrong branch
and never exercises the fallback. Guard: refuse (exit 2) when `--main` does not resolve.

### F7 — LOW — the `PAIR` line prints the pair id unredacted

`leg()` scrubs every detail line ("every printed line is redacted", 536–539), but the PAIR dump at
2966 prints `pair.get("id")` raw (stated_at/tokens are scrubbed, the id is not). A pair id carrying
`S897` or `naming-systems` would leak into the counter receipt, which SEPARABLE treats as read-set
bytes (`ca_named_paths`, 2381) — a self-inflicted SEPARABLE failure and a violation of the counter's
own redaction rule. One `scrub(pair.get("id"), cfg)` fixes it.

### F8 — LOW — executed leg order ≠ the frozen legs[] order the receipt will be diffed against

`--emit-legs` order (frozen): … ANNOTATE, **APPENDONLY, R1EXEMPT, NOSTUB**, SEPARABLE, **COMBINED,
RECEIPTS**…; actual stdout (captured in my control-arm run): … ANNOTATE, **NOSTUB, APPENDONLY,
R1EXEMPT**, SEPARABLE, **RECEIPTS, COMBINED**… No consumer grades sequence (check-receipt-seq reads
headers only), but any reviewer diffing the committed receipt against the frozen legs[] sees a
mismatch; make the dispatch follow LEG_SPECS order or document the divergence.

### F9 — LOW — "this lane writes no byte under the fleet root" is checked only for the pinned report

2239–2247: report drift pin→HEAD, numstat pin..HEAD on the report, and `status --porcelain -- report`
— i.e. one path. Uncommitted bytes anywhere else under the fleet root, or committed fleet changes to
other paths since the pin, are undetected, while the frozen STAMP-adjacent sentence claims the whole
root. Either narrow the sentence or widen the check.

### F10 — LOW — binary deltas escape the changed-line whitelist

`changed_files` uses `--name-status` (binary M detected) but `_removed_base_lines` uses a text
`diff -U0`, which yields no hunks for binary files → no removed lines → the path passes silently.
No binary files are expected in this corpus's landing set, so informational.

### F11 — INFO — SOURCES.md blind spots (by construction, but name them)

`sources_diff` grades only rows present at base: appended non-row lines are invisible (only removed
base lines are checked), and `sources_rows` silently overwrites duplicate row ids, so a
cell-identical duplicate row appended mid-file passes. Claim C's own counter owns registry shape —
but APPENDONLY's semantic half should not be described as covering appends.

### F12 — INFO — documented residuals, accepted

Absence-pair guard implemented on the count shape only; `legs_sha256` optional in claims (LEGCOUNT
order still enforced; semantic re-derivation covers the allowlists/floor/families either way); the
REPAIR statement is not re-graded at the combined tree (claim C appending a later
`statement_after`-matching line would drift it uncaught); `fixed_surfaces` binding via `required`
is a ≥4-char word-bag test (`_required_ok`), much weaker than the byte checks elsewhere.

## 4. L1 integration obligations distilled from this seat

1. Never freeze a `fixed_surfaces` entry without `sha256` (or `line`); prefer omitting the field —
   F1. Until the counter refuses it, nothing else will.
2. Do not rely on APPENDONLY to police SHONEN.md prose — F2; keep REPAIR pairs off mark lines
   (W1 RevSeparability F4 stands) and expect prose edits to be invisible.
3. Ten pairs must be ten distinct observations — F3; id suffixes don't make them unique.
4. Pair observations on `show`/`log` must pin 40-hex (F4) and carry `-- <path>` (F5) even though the
   counter won't refuse their absence — the frozen sentence will claim them anyway.
5. Run graded with a resolvable `--main` actually pinned at `<lands>` (F6); a NOTE in the receipt is
   not a guard.
6. W1 RevSeparability F1 (`owned_inplace` line 344 record), F2 (Ca-first ordering) and F3 (README
   REPAIR × C-INDEX) remain binding; this counter enforces the first via COMBINED but cannot enforce
   their F3 (C-side INDEX).

## 5. Residual risk / verification gaps

- Not run: the graded `ACCEPT-CA-77` against real round-77 data — `reports/round-77/claims.json`,
  `ledger.json`, fixtures do not exist yet (`ls reports/round-77/` → `telemetry` only), so every
  finding above is against the W1 fixture lanes + the real-base ledger-check path.
- The selftest's synthetic SHONEN/SKILL bytes differ from the real lane's; F2's real-lane impact
  (which SHONEN prose lines exist at base) was not enumerated — the mechanism is file-agnostic.
- No C-counter (`accept-c.py`) review — RevCounterC's seat.

## 6. Hygiene

Scratch: `/fast/scratch/hyaku/kotodama-r77/RevCounterCa/` (selftest, ledger-check runs, fixture
repos from `fs_probe.py`/`fs_probe2.py`) — deleted before yield. Probe inputs/outputs retained at
`.ufo/waves/round-77/w2/stage/RevCounterCa/` (`fs_probe.py`, `fs_probe2.py`, `probe-mutants.json`,
`probe-dup.json`, `selftest-ca.out`, `selftest-ca.err`). Installs: none. Fleet repo, sibling lanes,
lane git/jj/index, LOG.md/SCORECARD.md/SKILL.md/SHONEN.md/corpus/reports production files: untouched.
