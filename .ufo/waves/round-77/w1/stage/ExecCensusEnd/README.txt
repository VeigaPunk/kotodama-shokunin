ExecCensusEnd — receipts (kotodama round 77, wave 1)
====================================================
Lane base revision: 211f9526800906e0c585d878d265c37e5e090c15
Scratch root used (deleted after the run): /fast/scratch/hyaku/kotodama-r77/ExecCensusEnd
Nothing in the lane repo or the fleet repo was modified; the real corpus/SOURCES.md was never touched.

RECEIPT 1 — base run, roster path (assigned command)
----------------------------------------------------
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
      --root /home/vgpnk/Projects/shokunin kotodama
exit=0
stdout -> census-base.out  (3769 bytes: 28 x W04, 4 x W01, 1 x "kotodama ok" line)
stderr -> census-base.err  (0 bytes)

Fidelity of "at base": the lane HEAD is the base revision and the working-tree registry
is byte-identical to the base blob:
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD
211f9526800906e0c585d878d265c37e5e090c15
$ sha256sum corpus/SOURCES.md
51b18f1c98996056287e0eae4d24cd682b3d756fe898e50f7356cbf680af8301  corpus/SOURCES.md
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show \
      211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md | sha256sum
51b18f1c98996056287e0eae4d24cd682b3d756fe898e50f7356cbf680af8301  -

MIRROR construction (scratch only, 205 MB)
------------------------------------------
$ mkdir -p <scratch>/mirror
$ git -C <lane> archive 211f9526800906e0c585d878d265c37e5e090c15 | tar -x -C <scratch>/mirror
$ sha256sum <scratch>/mirror/corpus/SOURCES.md
51b18f1c98996056287e0eae4d24cd682b3d756fe898e50f7356cbf680af8301  -> identical to base

Mirror control (untouched registry, proving the mirror is faithful):
$ sources-census.sh validate --file <scratch>/mirror/corpus/SOURCES.md
exit=0   stdout -> census-mirror-base.out (28 x W04, 4 x W01, 1 x ok)   stderr -> census-mirror-base.err (0 bytes)
$ sources-census.sh census --file <scratch>/mirror/corpus/SOURCES.md
rows=820   -> census-mirror-base-census.out

RECEIPT 2 — mirrored registry + the two draft rows appended in census schema
----------------------------------------------------------------------------
Rows: rows-897-898.md (S897 -> D1 cssn.cn, S898 -> D2 onomastica; both 11 cells / 13 fields).
Assembly: lines 1-851 of the mirrored file (Registry ends at S896), the two rows, then the rest.
$ wc -l <scratch>/mirror-draft/corpus/SOURCES.md
955      (base 953 + 2)
$ grep -n '^## ' <scratch>/mirror-draft/corpus/SOURCES.md
26:## Registry   855:## Paths   892:## Search log   906:## Leads (unopened)   -> rows at 852,853 stay inside Registry
A stand-in C-lands entry was created at the used-by path the rows cite
(corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md).

$ sources-census.sh validate --file <scratch>/mirror-draft/corpus/SOURCES.md
exit=0
stdout -> census-mirror-draft.out  (28 x W04, 4 x W01 == base's 32 warnings; 0 x E-codes; 1 x "file ok")
stderr -> census-mirror-draft.err  (0 bytes)
$ grep -cE '\tE0[34]\t' census-mirror-draft.out   -> 0
$ sources-census.sh census --file <scratch>/mirror-draft/corpus/SOURCES.md
rows=822, tier.A=495, status.mined=727   -> census-mirror-draft-census.out

CONTROLS (each is a hardlinked copy of the draft mirror with one row added/replaced)
------------------------------------------------------------------------------------
ctl-e03.out        duplicate id S897 (distinct URL/scope)            exit=1  E03 x1
ctl-e04.out        S899 = same URL + same scope as S898, no supersedes exit=1  E04 x1
ctl-e04super.out   supersedes row INSERTED BEFORE S898               exit=1  E04 x1 (fires on S898)
ctl-e04super2.out  same supersedes row inserted AFTER S898           exit=0  E=0, "ok"
ctl-e12.out        the two draft rows appended at end of file         exit=1  E12 x2 (S897,S898)
ctl-e11entry.out   rows landed but the used-by entry file absent      exit=1  E11 x2 (S897,S898)
ctl-minimal.out    registry-only mirror (no corpus tree)              exit=1  E11 x755

Commands for the controls (all from <scratch>):
  cp -al -- mirror-draft ctl-<name>; then rewrite ctl-<name>/corpus/SOURCES.md
  sources-census.sh validate --file <scratch>/ctl-<name>/corpus/SOURCES.md

EXTRA — the script's own selftest, same base revision, TMPDIR inside scratch
---------------------------------------------------------------------------
$ TMPDIR=<scratch>/tmp sources-census.sh selftest
exit=0   "selftest ok"; 96 "killed" lines; 0 "SURVIVED" lines
stdout -> selftest.out
$ grep -c SURVIVED selftest.out   -> 0
$ grep -c '^killed' selftest.out  -> 96
$ ls -A <scratch>/tmp              -> (empty; no residue)
