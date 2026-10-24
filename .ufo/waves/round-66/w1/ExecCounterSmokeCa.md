# ExecCounterSmokeCa — counter smoke, claim Ca counter (operability)

Scope: run and smoke `reports/round-66/accept-ca.py` at lane base, record every leg and exit
code, and document defects/crashes/ambiguities with `path:line` + minimal fix. Counter bytes were
not edited; the only files this seat wrote are this report and
`.ufo/waves/round-66/stage/execcountersmokeca.md` (full detail, 25 findings CS-01…CS-25).
Synthetic repros live under `/tmp/ca-d2`, `/tmp/ca-d3`; no lane bytes outside `.ufo/` were touched.

## Observed runs (lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`)

Counter self sha256 `a4b93bf750e997b3ed6185dc3bcf242b460f14068a3c492490fc721879775c11`,
header revision `94209e8f80969dbac48d56c5d0e2e623635b8616`.

`python3 -B reports/round-66/accept-ca.py --root .`:

| leg | verdict | detail |
|---|---|---|
| D1 | FAIL | `bad=['live_status','quote','capture_ts','s776','s776_citations=0','s753_citations=1']` |
| D2 | FAIL | all three `final-measures-{c,o,ca}.txt` absent |
| D3 | FAIL | `named=65 existing=0 min=8` (later re-run: `existing=7`) |
| D4 | FAIL | complete verdict + run count, no partial |
| CRITERION | FAIL | QUALITY criterion 18 absent |
| QUOTES | FAIL | `exit=2 gate_ids=0 clean=True` (lesson absent) |
| ACCEPT-CA-66 | FAIL | **exit 1** |

Re-run ~2 min later at the same revision (siblings writing drafts): D1
`bad=['quote','s776_citations=0','s753_citations=1']`, D3 `existing=7`; exit 1 again.

`python3 -B reports/round-66/accept-ca.py --help` → **exit 0, no crash**:
`usage: accept-ca.py [-h] [--root ROOT]` with `-h/--root` options.

`python3 -B reports/round-66/accept-ca.py --root /nonexistent` → **uncaught traceback**
`FileNotFoundError: [Errno 2] No such file or directory: '/nonexistent'` from
`accept-ca.py:171`, exit 1 (CS-01).

## Highest-impact defects (detail + repro in stage doc)

1. **CS-04 D2 validates worktree bytes, not the receipt's carrier commit** — `accept-ca.py:108-113,135`.
   Demonstrated: empty receipts committed at a commit whose parent equals the stamp, correct text
   only in the worktree → `D2 PASS bad=[]` while the committed blobs are 0 bytes. This is the
   stale-receipt / false-stamp bypass class the claim exists to close. Fix: read receipt and
   counter via `git show {carrier}:{rpath}` / `git show {stamped}:{counter_path}`.
2. **CS-07/08 D3 passes on eight empty files** — `:146-152`. A receipt carrying only the seed
   comment `# seat status: added at integration` plus 8 zero-byte `.md` files → `D3 PASS`. The
   documented per-seat status and dead-seat `last-error:` lines are never checked, yet
   `len(existing) == reported` makes any genuinely dead (report-less) seat fail the leg forever.
3. **CS-10/11 D4 passes a run that never ran** — `:158-160`. `SEPARABILITY: 0 findings` +
   `acceptance_runs=0 (static-only; partial coverage)` → `D4 PASS`; `PARTIAL` is case-sensitive
   and blind to `static-only`/`skipped`, and `acceptance_runs=` is not emitted by
   `tools/check-claim-separability.py` at all (hand-typed count = fabrication surface).
4. **CS-15 QUOTES counts the 25 ids anywhere in the lesson, not in its Gate** — `:174-177`. Gate
   naming only `S001` + body listing S776–S800 → `QUOTES PASS`.
5. **CS-03 header revision is CWD-scoped** — `:78` lacks `-C root`; from `/tmp` the header says
   `unresolvable`, from the parent repo it prints the outer repo's `5695abb…` while `--root` is
   the lane. Fix: `["git", "-C", root, "rev-parse", "main"]`.
6. **CS-18 D1 live-status check is vacuous** — `:92` accepts the bare substrings `200` and
   `application/pdf`; a `status=404` receipt with `response_bytes=200` and `Accept:
   application/pdf` passes that sub-check.
7. **CS-06 D2 parent-equality sequencing trap** — `:121-129`; lane git HEAD is detached
   (jj-colocated) and `reports/round-66` is untracked at main (0 files in `git ls-tree main`), so
   unless integration moves the git `main` ref to a commit whose parent is the stamped revision,
   D2 cannot pass. Receipts must be measured at the integrated revision R and committed in a
   single receipt-only child commit of R (or the leg relaxed to `merge-base --is-ancestor`).
8. **CS-02 documented exit 2 is never returned** — `:34` vs `:184`; missing inputs read as
   predicate FAIL (1), not INPUT_ERROR (2), contrary to `corpus/QUALITY.md:45`.

Lower-severity: CS-05 vacuous tree line (`:130-133`), CS-09 unescaped dot (`:146`), CS-12 exact
`findings` wording, CS-13 900-char CRITERION window (demonstrated false FAIL), CS-14 any `18.`
line, CS-16/17 fragile id capture + line-count filler, CS-19 capture timestamp unpaired, CS-20
parenthesized-only citation regexes, CS-21 receipt quote line (was absent in the 08:33 draft,
present at :25 after the 08:35 rewrite, so D1's `quote` sub-check now passes), CS-22 receipt's
old-capture claim conflicts with its own `old_capture status=000` (:8) / `old_replay_status=200`
(:21) lines and, per peer re-probe, the :21 200 is a 302 into the fresh capture over a broken
negative-length CDX record, CS-23 receipt URL unpinned, CS-24 live-tree non-determinism across
runs, CS-25 any counter fix invalidates the three final receipts (re-measure required).

State note for D1 now (third run, after the 08:35 receipt rewrite):
`D1 FAIL bad=['s776_citations=0','s753_citations=1']` — the receipt's `quote` sub-check passes
(the verbatim quote now sits at `s753-recapture.txt:25`), and D1 fails only because the games
entry still carries `(S753)` once and `(S776)` zero times
(`corpus/knowledge/culture-material/games-play-sport-contests.md:23`). D3 at the same run:
`existing=60` of 65 named. Receipt-side, CS-22 still stands: the receipt's `old_capture
status=000` (:8) and `old_replay_status=200` (:21) lines do not support its :26 claim that the old
capture "replays 200 application/pdf TODAY" — peer re-probe (RevengerIntent F3/F4) reports the
:21 200 is a 302 redirect into the fresh capture and the CDX old record length is negative.

## Retained evidence

- Verbatim leg output and exit codes in §1 above and stage doc §1.
- `--help` output (exit 0), `--root /nonexistent` traceback (exit 1).
- Header-vs-root mismatch: `git rev-parse main` in the lane = `94209e8…`; in
  `/home/vgpnk/Projects/shokunin` = `5695abb…`; from `/tmp` = unresolvable.
- `grep -cF "Versions of mancala are traditionally played across Africa and Asia"` on
  `reports/round-66/telemetry/s753-recapture.txt` = 0 in the 08:33 draft, = 1 after the 08:35
  rewrite (line 25); D1's quote sub-check flipped FAIL→PASS between those runs.
- `git ls-tree -r main --name-only reports/round-66` = empty; `git rev-parse --abbrev-ref HEAD`
  = `HEAD`.
- Synthetic bypass runs: `/tmp/ca-d2` (D2 PASS over 0-byte committed receipts),
  `/tmp/ca-d3` (D3/D4/QUOTES/CRITERION/live_status demonstrations).

## Risks / blockers

- The counter is being exercised against a live, mutating worktree (sibling seats writing). Any
  final receipt must be measured after the last data commit on a clean worktree, and must say so
  (criterion 17).
- D2's `main` requirement is an integration prerequisite, not just a counter detail: the L1 must
  move the git `main` ref to the receipt carrier or D2 fails no matter how correct the data is.
- Blocker (external to this seat): the S753 receipt lacks the frozen quote, so D1 cannot pass
  until its owner adds `Versions of mancala are traditionally played across Africa and Asia`
  verbatim and the games entry's mancala bullet re-points `(S753)` → `(S776)`.

No tools installed or upgraded; no git/jj writes; no counter edits.

Report: `.ufo/waves/round-66/w1/ExecCounterSmokeCa.md`
