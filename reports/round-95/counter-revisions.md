# round-95 counter revisions (pre-freeze, forced by the do-nothing control)

Frozen counter: `reports/round-95/predispatch.py`, frozen in commit `d41eb594d27fa71869c0c28d9c2dc051fda40079`.

Revision 1 (first draft, not frozen) printed `FAIL legs=3/10` over the base tree
with C2 `no registry rows parsed`: the POSIX-class regex `[[:space:]]` inside Python `re`
matched nothing (FutureWarning "Possible nested set"). Fixed to `\s` before any scoring.

Revision 2 (frozen): the same do-nothing control then reported C3 `git numstat failed`
because `git diff` cannot name a base revision inside a `git archive` tree. C3 now reads the
base bytes with `git show <base-rev>:corpus/SOURCES.md` when the root is a git work tree,
or from `--base-registry`, and counts removed lines with difflib opcodes. Refuses to score
without either source.

Re-measured after both fixes on the base tree: `PREDISPATCH-95: FAIL legs=4/10` (O1 126/134,
O2/O3 driver missing, O4 REG baseline unmeasurable without the battery leg, C1 entry absent,
C2 rows=893 highest=S969 qualifying=0). The control cannot reach either target.
Receipt: `reports/round-95/predispatch-base.txt`.
