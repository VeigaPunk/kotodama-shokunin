#!/usr/bin/env bash
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
W=$L/.ufo/waves/round-76
ST=$W/w1/stage/ScribeLesson-7
P=/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material
run(){ echo; echo "### \$ $*"; bash -c "$*" 2>&1; echo "[exit=$?]"; }
run "find $W/assimilation/guard-proof -type f | sort"
run "ls -la $W/assimilation/"
echo; echo "### \$ independent re-check: each stored window carries its anchor exactly once (NFKC + whitespace folded)"
python3 - "$ST/windows" <<'PY'
import sys,pathlib,unicodedata,re
def fold(s):
    s=unicodedata.normalize("NFKC",s); return re.sub(r"\s+"," ",s).strip()
for p in sorted(pathlib.Path(sys.argv[1]).glob("*.txt")):
    t=p.read_text(); hdr,_,win=t.partition("--- window ---")
    m=re.search(r"^anchor: (.*)$",hdr,re.M); a=m.group(1) if m else None
    print(p.name, "anchor-hits-in-window:", (fold(win).count(fold(a)) if a else "carrier-only"), "window-chars:", len(fold(win)))
PY
echo "[exit=$?]"
run "sha256sum $P/calendar-festival-systems.amend-2026-10-24.md $P/calendar-festival-systems.amend-2026-10-24-r10.md $P/era-periodization-models.amend-2026-10-23b.md $P/calendar-festival-systems.amend-2026-10-23c.md"
run "wc -c $P/calendar-festival-systems.amend-2026-10-24.md $P/calendar-festival-systems.amend-2026-10-24-r10.md $P/era-periodization-models.amend-2026-10-23b.md $P/calendar-festival-systems.amend-2026-10-23c.md"
run "grep -n 'recheck:' $P/calendar-festival-systems.amend-2026-10-24.md $P/calendar-festival-systems.amend-2026-10-24-r10.md $P/era-periodization-models.amend-2026-10-23b.md $P/calendar-festival-systems.amend-2026-10-23c.md"
