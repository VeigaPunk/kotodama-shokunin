#!/usr/bin/env bash
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
B=98c486bdb4650ba5b8e651d332910e8ee60ad121
run(){ echo; echo "### \$ $*"; bash -c "$*" 2>&1; echo "[exit=$?]"; }
run "for p in culture-material/calendar-festival-systems.amend-2026-10-24.md culture-material/calendar-festival-systems.amend-2026-10-24-r10.md culture-material/era-periodization-models.amend-2026-10-23b.md culture-material/calendar-festival-systems.amend-2026-10-23c.md; do printf '%s -> ' \"\$p\"; git -C $L cat-file -e $B:corpus/knowledge/\$p 2>/dev/null && echo present || echo absent; done"
run "git -C $L ls-tree -r --name-only $B corpus/knowledge | grep -E 'calendar-festival|era-periodization'"
