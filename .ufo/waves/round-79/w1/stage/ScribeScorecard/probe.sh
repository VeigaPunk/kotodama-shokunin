#!/bin/sh
# Read-only probe: committed bytes only (git show / git grep / git cat-file / git log).
# No checkout, no worktree reads, no mutation.
set -u
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
G="git -C $LANE"
echo "## P0 lane toplevel"
$G rev-parse --show-toplevel
echo "HEAD=$($G rev-parse HEAD)"
echo "BASE_EXPECTED=44f76d456c1b326a71ffdb381590af825cbf11be"
$G merge-base --is-ancestor 44f76d456c1b326a71ffdb381590af825cbf11be HEAD && echo "base is ancestor of HEAD: yes" || echo "base is ancestor of HEAD: no"

echo "## P1 registry histogram (committed bytes)"
rowhist() {
  $G show "$1:corpus/SOURCES.md" | awk -F'|' '/^\| *S[0-9][0-9][0-9]+ *\|/{gsub(/ /,"",$9); print "status:" $9; gsub(/ /,"",$5); print "tier:" $5}' | sort | uniq -c | tr -s ' ' | tr '\n' ' '
  echo
  printf 'rows(%s)=' "$1"; $G show "$1:corpus/SOURCES.md" | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
}
for rev in 8c78e6b 012e8d3c 4f5e3b25 4b255745dea45a45d88b17e3c3fea4cdb6700cf7 HEAD; do
  echo "-- $rev"; rowhist "$rev"
done

echo "## P2 capability row as committed at HEAD"
$G show HEAD:SCORECARD.md | grep -n '^| sources registry' | cut -c1-260
echo "-- commits that touched the 43-row figure"
$G log --format='%h %s' -S'43 rows' -- SCORECARD.md | cut -c1-120

echo "## P3 S884 used-by token"
for rev in 4b255745dea45a45d88b17e3c3fea4cdb6700cf7 HEAD; do
  printf '%s: ' "$rev"; $G show "$rev:corpus/SOURCES.md" | awk -F'|' '/^\| S884 /{gsub(/^ +| +$/,"",$12); print $12}'
done
echo "-- receipt census-start line 33 vs census-end line 33 (committed)"
$G show HEAD:reports/round-78/telemetry/census-start.txt | sed -n '33p' | cut -c1-200
$G show HEAD:reports/round-78/telemetry/census-end.txt | sed -n '33p' | cut -c1-200
echo "-- r13 amend path existence"
for rev in 4b255745dea45a45d88b17e3c3fea4cdb6700cf7 HEAD; do
  $G cat-file -e "$rev:corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md" 2>/dev/null && echo "$rev: present" || echo "$rev: absent"
  $G cat-file -e "$rev:corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md" 2>/dev/null && echo "$rev: amend-2026-10-23 present" || echo "$rev: amend-2026-10-23 absent"
done
echo "-- self-assessment files naming the S884 used-by token or the r13 amend (HEAD)"
$G grep -n -F 'amend-2026-10-24-r13' HEAD -- SCORECARD.md SHONEN.md LOG.md corpus/lessons 2>/dev/null | cut -c1-160
echo "(exit $?)"
$G grep -n -E 'S884 ' HEAD -- SCORECARD.md SHONEN.md | cut -c1-160

echo "## P4 SHONEN boxes and promotion-gate definition"
echo "-- HEAD box marks"; $G show HEAD:SHONEN.md | grep -n '^- \['  | cut -c1-70
echo "-- 4b255745 box marks"; $G show 4b255745dea45a45d88b17e3c3fea4cdb6700cf7:SHONEN.md | grep -n '^- \[' | cut -c1-70
echo "-- 'Promotion gates' defined as a heading anywhere at HEAD?"
$G grep -n -i -E '^#+ .*promotion gates' HEAD -- '*.md' | head -3; echo "(heading exit $?)"
$G grep -n -i 'promotion gates' HEAD -- '*.md' | cut -c1-160
echo "-- operator-owned wording in SHONEN marks line"
$G show HEAD:SHONEN.md | grep -n -i 'operator' || echo "none in SHONEN.md"

echo "## P5 round-24 non-author dossier wording and round-78 closure box description"
$G show HEAD:reports/round-24/promotion-review.md | grep -n -i 'non-author' | head -4 | cut -c1-200
$G show HEAD:SCORECARD.md | sed -n '300p' | cut -c1-260
echo "-- round-78 closure SHONEN line"
$G show HEAD:corpus/lessons/round-78-verifier-spotcheck.md | grep -n 'SHONEN' | cut -c1-220
echo "-- round-74 closure statement of boxes"
$G show HEAD:corpus/lessons/round-74-verifier-spotcheck.md | grep -n 'SHONEN' | tail -1 | cut -c1-200
