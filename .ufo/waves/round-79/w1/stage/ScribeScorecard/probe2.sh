#!/bin/sh
# Read-only probe 2: committed bytes and fleet PROTOCOL/AXES history. No mutation.
set -u
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
FLEET=/home/vgpnk/Projects/shokunin
G="git -C $LANE"
F="git -C $FLEET"

echo "## Q1 'Promotion gates' as a markdown heading in the lane at HEAD (exit of git grep itself)"
$G grep -n -i -E '^#+ .*promotion gates' HEAD -- '*.md'
echo "git-grep-exit=$?  (1 = no match)"

echo "## Q2 where the promotion-gate text lives (fleet, committed)"
$F rev-parse --show-toplevel
$F grep -n -i -E '^## Promotion gates' HEAD -- PROTOCOL.md
echo "-- non-author rule line at fleet HEAD"
$F grep -n 'a subagent the lane' HEAD -- PROTOCOL.md | cut -c1-200
echo "-- rule introduced: first commit containing it (pickaxe)"
$F log --reverse --format='%h %ad %s' --date=short -S'a subagent the lane dispatched is still the lane' -- PROTOCOL.md | head -2 | cut -c1-140
echo "-- AXES dispatched-subagent rule: first commit containing it"
$F log --reverse --format='%h %ad %s' --date=short -S'a dispatched subagent does not count' -- AXES.md | head -2 | cut -c1-140

echo "## Q3 round-24 dossier dispatch wording (lane-committed)"
$G show HEAD:reports/round-24/promotion-review.md | grep -n -E 'workers|dispatch|Non-author|every seat self-declares' | cut -c1-220
echo "-- round-24 SCORECARD calibration row (HEAD)"
$G show HEAD:SCORECARD.md | grep -n 'SHONEN boxes never non-author-verified' | cut -c1-120
echo "-- round-24 date line"
$G show HEAD:SCORECARD.md | sed -n '292p' | cut -c1-200

echo "## Q4 round-78 closure claim about SHONEN box marks vs SHONEN.md at HEAD"
$G show HEAD:corpus/lessons/round-78-verifier-spotcheck.md | grep -n -c "4 lines \`\[ \]\`"
echo "-- SHONEN.md box marks at HEAD (count of [~], [ ], [x])"
for m in '~' ' ' 'x'; do printf '[%s] ' "$m"; $G show HEAD:SHONEN.md | grep -c "^- \[$m\]"; done

echo "## Q5 self-assessment files naming the r78 S884 used-by token at HEAD"
$G grep -n -F 'worldbuilding-setting-practice.amend-2026-10-24' HEAD -- SCORECARD.md SHONEN.md LOG.md
echo "git-grep-exit=$?  (1 = no match in self-assessment files)"
$G grep -c -F 'worldbuilding-setting-practice.amend-2026-10-24' HEAD -- corpus/lessons reports/round-78 2>/dev/null | grep -v ':0$'
