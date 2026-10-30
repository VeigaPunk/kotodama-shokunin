#!/bin/sh
# Read-only recon for SHONEN four-box pointers and the S884 census token.
# Reads committed bytes only (git show / git grep / git cat-file); writes nothing in the lane.
# Usage: sh shonen-box-probe.sh <lane-root>   (run from any cwd; output goes to stdout)
set -u
LANE="${1:?lane root}"
B=44f76d456c1b326a71ffdb381590af825cbf11be
HERE="$(cd "$(dirname "$0")" && pwd)"
g() { git -C "$LANE" "$@"; }
echo "# base: $B"; echo "# toplevel: $(g rev-parse --show-toplevel)"
echo "## box1 pointers"
g show $B:SKILL.md | sed -n '20p;505p;564p' | cut -c1-80
g show $B:SKILL.md | grep -n -E '^## (Decision table|Error patterns|Checklist)'
echo "## box1 registry histogram at round-75 landing 4f5e3b25 and round-74 d7a38405"
for r in d7a38405 4f5e3b25 $B; do
  echo -n "$r: "; g show $r:corpus/SOURCES.md | awk 'NR>=26 && /^\| *S[0-9]+ /{ if (index($0,"## Paths")) exit; n++; split($0,a,"|"); st=a[9]; gsub(/^ +| +$/,"",st); c[st]++} END{printf "rows=%d mined=%d queued=%d rejected=%d\n", n, c["mined"], c["queued"], c["rejected"]}'
done
echo "## box1 census receipts: exit line and presence of the count tokens"
for f in census-start census-end; do echo "round-75 $f: $(g show $B:reports/round-75/telemetry/$f.txt | grep -E '^exit=' ) count-hits(817|722|808|713)=$(g show $B:reports/round-75/telemetry/$f.txt | grep -cE '817|722|808|713')"; done
echo "## box2 round-51 registry at 1923bfe, 4ad2683, 2b956d7 (queued ids)"
for r in 1923bfe 4ad2683 2b956d7; do echo -n "$r rows: "; g show $r:corpus/SOURCES.md | awk 'NR>=26 && /^\| *S[0-9]+ /{ if (index($0,"## Paths")) exit; n++} END{print n}'; done
g show 2b956d7:corpus/SOURCES.md | awk -F'|' '/^\| *S[0-9]+ /{ if($9 ~ /queued/){gsub(/ /,"",$2); printf "%s ", $2}}'; echo
echo "## box2 final receipt tail"; g show $B:reports/round-51/telemetry/final-measures.txt | tail -2
echo "## box3 round-50 commits and SCORECARD pointer"
for c in 1923bfe 4ad2683; do echo "$c $(g cat-file -t $c)"; done
g show $B:SCORECARD.md | grep -n -E '1923bfe|4ad2683' | cut -c1-160 | head -3
echo "## box4 sign-language handoff, owner table, connector sweep"
g show $B:corpus/knowledge/linguistics/sign-languages-manual-modality.md | sed -n '224p' | grep -o 'Handoff: lore-shokunin[^.]*\.'
g show $B:corpus/knowledge/linguistics/sign-languages-manual-modality.md | grep -c -E '^\| `[a-z-]+\.md:[0-9]+` \|'
g show $B:.ufo/waves/round-51/build/ConnectSiblingSign.md | grep -n -E 'No sibling lane owns|no owner in the fleet' | cut -c1-160
echo "## S884 census token: receipts vs registry at base (probe-used-by.py)"
for f in reports/round-78/telemetry/census-end.txt reports/round-78/telemetry/census-start.txt reports/round-75/telemetry/census-end.txt; do echo "-- $f"; python3 -B "$HERE/probe-used-by.py" "$LANE" $B $f; echo "exit=$?"; done
echo "## any SCORECARD/SHONEN/LOG self-assessment citing the S884 used-by token?"
g grep -n -E 'amend-2026-10-2[34](-r13)?' $B -- SCORECARD.md SHONEN.md | cut -c1-160; echo "(end)"
echo "## SCORECARD correction rows naming S884 (L75-09 is an evidence-presence pair, not used-by):"
g show $B:SCORECARD.md | grep -n 'S884' | cut -c1-200
