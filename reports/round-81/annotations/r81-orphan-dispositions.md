# Round-81 orphaned-evidence dispositions (carry-in 4, landed first)

The round-80 closure's carry-in duty: any kotodama prior-round evidence file
cited by closed reports but never committed lands via treecommit explicit
paths first. This round ran the duty mechanically instead of by hand: the new
sweep instrument (`tools/check-orphan-evidence.py`, claim C this round) scans
all 71 closed fleet round reports plus the lane's 32 verifier spot-checks
(103 documents, 510 distinct cited paths) and classifies each citation against
the lane HEAD tree and the worktree. Red-before receipt (committed in this
same records commit): `reports/round-81/telemetry/orphan-sweep-red.txt`.

Result: **zero ORPHAN-ONDISK** citations — there is nothing landable; every
cited-but-uncommitted evidence file's bytes are absent from this host, and
fabricating them is forbidden. The three ORPHAN-ABSENT citations, each with
its disposition:

| orphan path | cited in | disposition |
|---|---|---|
| `corpus/knowledge/a.md` | round-68 fleet report; round-68 lane spot-check | review-only false positive of the mechanical class: the path appears inside round-68's prose about its frozen fixture never creating `corpus/knowledge/a.md` (the EXEC-FAIL record itself) — it was never an evidence file, never staged, and the sentence citing it says exactly that. No bytes exist; none are owed. The instrument stays unweakened: the classification is mechanical, this disposition is the author's, per the tool's stated limits. |
| `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` | round-78 fleet report (twice, as pasted census-receipt W01 lines); round-78 and round-79 lane spot-checks | the S884 receipt-vs-registry drift, already bounded append-only by `reports/round-79/corrections/ca79-r78-s884.md` (receipt names the r13 snapshot; the committed registry names `amend-2026-10-23.md`). `git log --all` over the r13 path is empty and the file is absent on disk: the r13 snapshot bytes were never committed anywhere reachable from this host and are unknowable — none are fabricated. The r81 sweep now names the citation mechanically; no further repair exists to land. |
| `reports/round-63/telemetry/final-measures.txt` | round-63 lane spot-check only | a historical quote inside the round-63 spot-check's own routed-defect text (its dead-pointer defect named the file, ordered the pointer fix, and the fix landed: the live receipts are `final-measures-o.txt`/`final-measures-c.txt`, and current SCORECARD/LOG rows cite the split receipts). The only remaining citation of the dead path is the defect record itself; the record stays as filed (append-only), this row is its pointer-resolution note. |

Carry-in execution order: this record + the red-before receipt are the first
round-81 lane commits, before any claim work lands, per the carry-in's "land
via treecommit explicit paths first" — the explicit paths turned out to be an
empty set, and the honest landing of that fact is this disclosure.
