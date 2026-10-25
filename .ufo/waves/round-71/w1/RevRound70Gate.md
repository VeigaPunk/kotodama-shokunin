# Round-70 Gate review (V70-2/V70-3)

Reopened `corpus/lessons/round-70.md`, S860 row. Its quote text is:

> A row whose `used-by` names a path that does not contain the row's own id is `STALE-USED-BY` (reported; gated only for the frozen ruling set, not globally...)

Whitespace-split word count: **27** (V70-3; the column says “≤25 words,” so this is over by 2).

The same row's grounds says the selftest was run at **6cb51a4**. That is a pointer flaw (V70-2): the hardened checker blob `6a314e9c7c5635a15a9b2f8b57bc34db8039a301` first appears in the tree at **acc2d614**; `6cb51a4` has the different blob `1ef2e965204f53f40ffbabf45abea3fae9f029a6`. The cited revision therefore does not evidence running the hardened checker.

Evidence: lesson lines 11–13; `git ls-tree acc2d614 tools/check-supersession-settlement.py` and the corresponding `6cb51a4` tree lookup.
