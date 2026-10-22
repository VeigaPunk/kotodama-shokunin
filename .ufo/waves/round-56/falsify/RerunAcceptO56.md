# RerunAcceptO56 — claim O rerun (round 56 falsify, 2026-10-22)

## Verdict

CARRIED. Every declared expectation reproduces exactly. The counting command exits 1 at the
declaration revision with ENTITY, EXIT, DECODE and BADUTF8 failing (NOFALSE, KEEP, FORMAT,
SELFTEST passing, 27/27), exits 0 at the landing revision with all eight legs passing,
--selftest exits 0 at both revisions, and the landing commit touches
tools/check-gate-quotes.py only. No defect found; no fix needed.

## Method

Two fresh sandbox clones under /fast/scratch/hyaku/kotodama-r56-falsify/RerunAcceptO56/
(lane-decl, lane-o), `git clone` of the lane with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE
unset; revisions checked out and confirmed by rev-parse (DECL=b4b7db91a38447bb2c07b0ef436fc9654dcec89c,
O=7576fd43bbbe34a00341e4b1956c907f2760e7d8). All runs `python3 -B` as declared. No git or jj
writes anywhere outside the sandbox clones; the only lane write is this report.

## Checked items

- reports/round-56/accept-o.py at b4b7db91 (declaration) — CARRIED. Exit 1. ENTITY FAIL
  count=0 with all 16 declared (line, S-id) pairs missing and extra=[]; EXIT FAIL
  round55=0 fixture=0; DECODE FAIL with exactly the ten declared fixture pairs missing,
  extra=[], moved_exit=0 moved_missing=10 moved_extra=0; BADUTF8 FAIL with traceback=True;
  NOFALSE, KEEP, FORMAT, SELFTEST PASS 27/27. Matches claims.json:211 word for word,
  including the "(27/27)" detail. Evidence (accept-o.py stdout, declaration clone):
  "BADUTF8 FAIL exit=1 stderr_first='Traceback (most recent call last):' traceback=True".
- reports/round-56/accept-o.py at 7576fd43 (claim O) — CARRIED. Exit 0, all eight legs PASS:
  ENTITY PASS count=16 missing=[] extra=[]; NOFALSE PASS stray=[]; EXIT PASS round55=1
  fixture=1; DECODE PASS missing=[] extra=[] moved_exit=1 moved_missing=0 moved_extra=0;
  KEEP PASS changed=[]; BADUTF8 PASS exit=2, first stderr line a GATE_QUOTES_ERROR naming
  reports/round-56/fixtures/lessons/bad-utf8.md, traceback=False; FORMAT PASS
  malformed_runs=[]; SELFTEST PASS exit=0, 38/38. Satisfies claims.json:212, "all eight
  legs PASS (exit 0)". Evidence: "ENTITY PASS count=16 missing=[] extra=[]" and
  "EXIT PASS round55=1 fixture=1" (accept-o.py stdout, landing clone).
- tools/check-gate-quotes.py --selftest at b4b7db91 — CARRIED. Exit 0, "SELFTEST: 27/27
  pass". The 27 cases are the pre-landing set; the decoded/entity/UTF-8 cases appear only
  at the landing revision, consistent with the declaration.
- tools/check-gate-quotes.py --selftest at 7576fd43 — CARRIED. Exit 0, "SELFTEST: 38/38
  pass"; the 11 new cases include decoded-quote, decoded-ellipsis, decoded-doubled-locator
  and the UTF-8 path. Evidence: "PASS decoded-truncated-grounds-red want=('html-entity',
  'truncated-grounds') got=html-entity,truncated-grounds" (selftest stdout, landing clone).
- Commit scope 7576fd43 — CARRIED. `git show --stat 7576fd43bbbe34a00341e4b1956c907f2760e7d8`
  reports "1 file changed": tools/check-gate-quotes.py, 101 insertions(+), 9 deletions(-),
  110 lines changed. No other path touched; agrees with claims.json:206-208 (O lands exactly
  tools/check-gate-quotes.py). Evidence: "tools/check-gate-quotes.py | 110 ... 1 file changed".
- Runner integrity — CARRIED. reports/round-56/accept-o.py is the identical blob (103f5209)
  at both revisions, so one counting script produced both results. Both clones are clean
  after the runs (`git status --porcelain` empty in each): zero mutation by the reruns.

## Unrun checks (outside this seat's scope)

- Red-control mutations (RED-ENTITY, RED-DECODE-FP, RED-BADUTF8, RED-SELFTEST, and the
  rest) were not run here; claims.json:214 assigns mutation of the new rule to the falsify
  wave's mutation-tester seat.
- Claim C counting (reports/round-56/accept-c.py) not rerun here (RerunAcceptC56 scope).
- The 16 html-entity rows of corpus/lessons/round-55.md were not re-opened against their
  sources here (ReviewRows seats' scope).
- No LSP/diagnostics check applies: the exercise is byte-reproducible command reruns, not
  source semantic queries.

## Notes

No tools installed (none needed; pacman transactions paused host-wide). Godspeed axes:
coverage of the declared rerun matrix (both revisions, both commands, stat check),
fidelity of captured exit codes and leg lines, speed via parallel batches. Kept moves:
fresh-clone isolation, blob-identity check between revisions, post-run mutation check.
