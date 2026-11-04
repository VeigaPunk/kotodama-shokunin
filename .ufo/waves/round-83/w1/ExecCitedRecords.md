# ExecCitedRecords — round 83 w1 report

Seat: build + falsify the QUALITY-criterion-31 checker (`check-cited-records.py`).
Judged on calibration. Milestone r83-v1.

## Files written (all paths relative to the lane)

- `.ufo/waves/round-83/w1/stage/ExecCitedRecords/check-cited-records.py` —
  my independent implementation of the frozen contract (stdlib only,
  py_compile clean, no repository imports). Written to the stage path per the
  L1's mid-wave instruction; `tools/check-cited-records.py` was NOT touched
  by this seat (the L1 installed a working checker first).
- `.ufo/waves/round-83/w1/stage/ExecCitedRecords/proof.md` — both frozen-tree
  runs, selftest paste, falsification log, reverse cross-check, and the
  byte-level comparison against the installed tool. Absolute scratch paths
  masked (criterion 31); none appear in any committed byte I wrote.

## Behavior (frozen contract, as specified)

`--root/--from-round/--bind-round/--json/--selftest`; documents =
`reports/round-<k>/**/*.md` + `corpus/lessons/round-<k>*.md`; EMPTY leg on
backticked citation tokens resolving to 0-byte regular files; SCRATCH leg on
`^/(tmp|var/tmp|fast/scratch)/` for rounds ≥ bind; one
`CITED-RECORDS: <e> empty / <s> scratch` line; exits 0/1/2 with
`CITED-RECORDS-ERROR` (never a traceback) on could-not-evaluate; `--json`
shape `{"empty":[{"path","doc"}...],"scratch":[...],"documents":N}`; 15-check
selftest in a TMPDIR-honouring temp dir, exactly one `SELFTEST: PASS (15
checks)` line, no absolute paths printed.

## Evidence (all exercised; details and pastes in proof.md)

- Frozen tree 21277b0 materialized read-only via `git archive`.
- Run A (`--from-round 82 --bind-round 82`): `2 empty / 2 scratch`, exit 1 —
  catches `reports/round-82/counter-revisions.md` (0 bytes, cited by both
  `corpus/lessons/round-82.md` line 12 and `corpus/lessons/round-82-verifier-spotcheck.md`
  lines 207-208) and the two scratch-shape citations in the spot-check
  (fast-scratch shape at its line 233, tmp shape at its line 64; the seat
  text's "two /fast/scratch/ receipts" is one fast-scratch + one tmp shape on
  the actual frozen bytes — both flagged).
- Run B (default binding): `0 empty / 0 scratch`, exit 0; documents = 1
  (`reports/round-83/counter-revisions.md`, landed by the frozen counters'
  own r2 revision — clean). JSON run agrees.
- Falsification: planted round-83 lesson + planted 0-byte record + tmp-shape
  receipt → exactly `1 empty / 1 scratch`, exit 1; an uncited 0-byte file is
  not counted. (First fixture accidentally backticked the uncited file's own
  path and was correctly flagged — fixture fixed, rerun exact.)
- Reverse cross-check (independent code path): over the frozen tree, 4
  in-scope documents, 125 zero-byte files — reverse enumeration reproduces
  exactly Run A's 2 empty and 2 scratch (path, doc) pairs. Nothing missed,
  nothing extra.
- Selftest `SELFTEST: PASS (15 checks)`; `py_compile` clean; TMPDIR honored;
  fixtures and all scratch removed at exit.

## Comparison vs the installed `tools/check-cited-records.py`

Identical output line formats; both carry the frozen shape markers; both
clear the 10-check floor; on the frozen tree the installed tool reports
`2 empty / 9 scratch` at binding 82 and `0 empty / 2 scratch` at the default
binding because its document set also admits round-telemetry `*.txt` — which
catches 7 further genuine scratch citations, including the frozen counters'
own `smoke-d.txt`/`smoke-o.txt` receipts (its default-binding run is red on
the frozen tree for that reason). The frozen C counter's CHECKER leg
materializes no `.txt`, so the difference is unobservable to the grader;
both print `CITED-RECORDS: 0 empty / 0 scratch` exit 0 at lands. Remaining
deltas (scratch tail rendering on ellipsis-masked citations, citation
lookbehind, round-number parse strictness) do not diverge on any committed
byte in scope. Recorded for the L1; `.md`-only follows the seat contract,
`.md`+`.txt` is the wider net — policy choice is the L1's.

## Risks / limitations

- The `.md`-only document set leaves the round-telemetry `.txt` citations
  (e.g. `quality30-probe.txt`'s capture path) to the installed tool or a
  future binding decision; flagged in proof.md with exact file names.
- Scratch findings report the bare shape root when a document masks its
  path's tail with an ellipsis (frozen tail class stops there); the document
  and line are always named, which is the citable part.
- None observed beyond these.

## Tooling record

No tools installed or upgraded (none needed). No pacman transaction attempted
(host-wide pause respected). All proof commands were read-only git plus
python3 stdlib.

## R82-M3 (evidence precedence)

Not triggered in this seat: no source documents were read; the only
first/second-reading question was the checker itself, resolved by the L1's
message (installed tool binds) with my stage copy as the independent second
implementation, disagreement reported rather than silently picked.
