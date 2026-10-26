#!/bin/sh
# assemble accept-c.py from PART A (counters/accept-c.py lines 1-509) + w2/parts in CFG-CONTRACT order -> $1
W=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75
P=$W/w2/parts
{ sed -n 1,509p $W/w2/parts/part-a.py; for f in part-cfg leg-entries leg-rows leg-repointed leg-gate leg-evidence leg-rejects leg-ground-cited-census leg-mirror-coll leg-frozencfg leg-index part-selftest-fixtures part-selftest-run part-main; do echo; cat $P/$f.py; done; } > "$1"
python3 -B -m py_compile "$1"
