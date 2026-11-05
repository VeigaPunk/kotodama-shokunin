# ScribeLesson — round-90 notes

Seat: ScribeLesson, 2026-11-04. Stage:
`.ufo/waves/round-90/w1/stage/ScribeLesson/`. Scratch:
`/fast/scratch/hyaku/kotodama-r90/ScribeLesson/` (deleted before yield).

## What this seat produced

- `lesson.md` — the draft for `corpus/lessons/round-90.md`: `## Gate`,
  `## Mistakes` (R90-M1…R90-M6), `## Corrections` (the six round-89 routed
  defects and their dispositions), `## Rounds`, `## Census`.
- `census-after.txt` — the two round-end commands and their full output.
- `.ufo/waves/round-90/w1/ScribeLesson.md` — the scoped findings report.

## Gate block status

ScribeEntry's stage (`.ufo/waves/round-90/w1/stage/ScribeEntry/`) held only an
empty `evidence/` directory when this seat read it at 2026-11-04T20:05-03:00 and
again at 20:10. Its `gates.md` / `rows.md` / `entry.md` were therefore not
available, and no quote is invented here: the Gate block in `lesson.md` is
marked PENDING and this seat watched the directory until the packet landed (see
below). If the packet had not landed, the Gate block would wait for it: the
Mistakes, Corrections and Rounds sections stand on their own evidence and do
not depend on claim C's sources.

## Sources this seat opened

None. This seat is a scribe for the lesson: every quote in `lesson.md` is either
a repo-internal receipt line (cited by path and line) or a gate line copied
verbatim from ScribeEntry's packet. No URL was fetched by this seat, so no
capture, http status or fetch instant is claimed here. Source opening and
capture commitment belong to ScribeEntry and ExecIndepRefetch.

## Measurements this seat ran (cheap facts, not re-runs of graded work)

1. `sha256sum tools/check-advance-evidence.py` → `121888f0…`, equal to
   `claims.json` O.tool_sha256 and to the receipt's own `tool sha256` line.
2. `git grep -lciE "petition"` vs `\bpetition` vs `competition` at base
   `6b0b86e4` over `corpus/knowledge` → 91 / 35 / 32 files (R90-M5).
3. `git log`/`git show` over `reports/round-90/measure90.py` and
   `counter-revisions.md` → counter revision 6 (`6e1ea6a5…`) is committed at
   `ebd81b1b` and records the ENTRY-keying defect as R90-M3; the working-tree
   file matches HEAD.
4. The round-end census and recheck-queue check (below).

## Census (round end)

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama; echo rc=$?
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
rc=0
$ python3 -B tools/check-sources-recheck.py --as-of 2026-11-04 --window 90
RECHECK-QUEUE: 0 due / 4 upcoming / 16 on-release / 865 rows
rc=0
```

Full output: `census-after.txt`. The warnings are pre-existing W04 duplicate-URL
and W01 tier-C-mined rows named by the round-89 census; none names a round-90
row.

## Refusals and limits of this seat

- Did not run the frozen counter, the grader's `--selftest` or the mutant
  battery: their receipts are the freeze's, and re-running them to decorate a
  report is out of scope (and `mutation-score.txt` already pins the tool sha).
- Did not fetch or re-open any source; did not repair or re-date any registry
  row (freshness paused, `APPENDONLY` would kill C).
- Did not edit any production file; no commit, push or mutating git/jj call.
- No tool was installed or upgraded; nothing to record under the operator's
  2026-10-19 tooling authorization.
