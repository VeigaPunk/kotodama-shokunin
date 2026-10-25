#!/usr/bin/env bash
# Round-73 scratch mirror: lane corpus + the five normalized rows + the two admitted entries,
# validated with `sources-census.sh validate --file` BEFORE any registry append in the lane.
set -u
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
A=$LANE/.ufo/waves/round-73/assimilation
M=/tmp/r73-mirror
ENT=${ENT:-/tmp/r73-entries}
rm -rf "$M" && mkdir -p "$M/corpus" && rsync -a "$LANE/corpus/" "$M/corpus/" && cp "$LANE/SKILL.md" "$M/SKILL.md"
python3 - "$M" "$A/rows-S876-S880.md" <<'PY'
import sys,re
M,rows=sys.argv[1],sys.argv[2]
p=M+"/corpus/SOURCES.md"
L=open(p,encoding="utf-8").read().split("\n")
i=max(n for n,l in enumerate(L) if re.match(r"^\|\s*S875\s*\|",l))
new=[l for l in open(rows,encoding="utf-8").read().split("\n") if l]
L[i+1:i+1]=new
open(p,"w",encoding="utf-8").write("\n".join(L))
print("inserted",len(new),"rows after line",i+1)
PY
cp "$ENT"/conlang-scholarship.md "$ENT"/conlang-scholarship.amend-2026-10-23.md "$M/corpus/knowledge/linguistics/"
echo "entry pins:"; sha256sum "$M"/corpus/knowledge/linguistics/conlang-scholarship*.md
echo "mirror registry: $(sha256sum "$M/corpus/SOURCES.md")"
echo "lane registry (pre-append): $(sha256sum "$LANE/corpus/SOURCES.md")"
echo "rows lane/mirror: $(grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' "$LANE/corpus/SOURCES.md") / $(grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' "$M/corpus/SOURCES.md")"
echo '$ sources-census.sh validate --file '"$M/corpus/SOURCES.md"
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$M/corpus/SOURCES.md" > /tmp/r73-mirror-census.out 2>&1; rc=$?
grep -v 'W04' /tmp/r73-mirror-census.out; echo "W04 lines: $(grep -c W04 /tmp/r73-mirror-census.out)"
echo "exit=$rc"
echo '$ check-cited-lines.py over mirrored entries'
python3 -B "$LANE/tools/check-cited-lines.py" "$M"/corpus/knowledge/linguistics/conlang-scholarship.md "$M"/corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md; echo "cited-lines exit=$?"
