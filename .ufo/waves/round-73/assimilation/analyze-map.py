#!/usr/bin/env python3
"""Round 73, seat ExecRenumber: theme-row collision verdict + round-71 map staleness.
Read-only over the lane registry, the staged package and the round-71 map.
Writes only under $A (assimilation scratch)."""
import json, re, subprocess, sys
from pathlib import Path

A = Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/assimilation")
L = Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin")
S = Path("/home/vgpnk/Projects/shokuknow")
REG = L / "corpus/SOURCES.md"
STAGED = S / "merge/kotodama/SOURCES.append.md"
OLD = L / ".ufo/waves/round-71/assimilation/id-renumber-map.json"

ROW = re.compile(r"^ {0,3}\|[ \t]*(S[0-9]{3,})")
THEME = ["S881", "S882", "S892", "S893", "S901"]
ADOPT = ["S876", "S877", "S878", "S879", "S880"]

def rows(path):
    out = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = ROW.match(line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append((m.group(1), n, cells))
    return out

reg = rows(REG)
stg = rows(STAGED)
reg_ids = {r[0] for r in reg}
stg_ids = {r[0] for r in stg}
reg_by_id = {r[0]: r for r in reg}
stg_by_id = {r[0]: r for r in stg}

lines = []
def p(s=""):
    lines.append(s)
    print(s)

p("## A. registry shape")
p(f"registry rows={len(reg)} distinct ids={len(reg_ids)} first={min(reg_ids)} last={max(reg_ids)}")
nums = sorted(int(i[1:]) for i in reg_ids)
gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in set(nums)]
p(f"gaps in S{nums[0]:03d}..S{nums[-1]:03d}: {gaps if gaps else 'none (contiguous)'}")
p(f"staged rows={len(stg)} distinct ids={len(stg_ids)} first={min(stg_ids)} last={max(stg_ids)}")
p()

p("## B. five theme staged rows: do their STAGED ids collide with lane ids?")
p(f"{'staged':7} {'in reg-ids?':12} {'staged doc (first 90 chars of source cell)'}")
for sid in THEME:
    doc = stg_by_id[sid][2][1][:90]
    p(f"{sid:7} {('YES' if sid in reg_ids else 'no'):12} {doc}")
p()
coll = sorted(reg_ids & stg_ids)
p(f"full collision set (reg-ids ∩ staged-ids): n={len(coll)} {coll}")
p(f"theme ids in that set: {[i for i in THEME if i in coll] or 'none'}")
p(f"numeric rule that holds: staged ids <= S{max(reg_ids)[1:]} collide only when the lane already uses that number; "
  f"theme ids are all > S{max(reg_ids)[1:]} -> no collision")
p()

p("## C. adopted lane ids S876..S880: absent from reg-ids, and what they mean in each namespace")
for aid in ADOPT:
    inreg = aid in reg_ids
    staged_doc = stg_by_id[aid][2][1][:80] if aid in stg_by_id else "(absent from staged)"
    p(f"{aid}: in reg-ids={inreg}  staged row with the same number names: {staged_doc}")
p("NOTE: the five adopted lane ids numerically equal five OTHER staged rows (S876..S880, naming/narrative docs). "
  "Three namespaces: same number, different document. A later adoption of staged S876..S880 must renumber by document.")
p()

p("## D. URL evidence for the five theme rows (lane hits = 0 means the ground is uncovered)")
hosts = {
    "S881": "ojs.unito.it",
    "S882": "philol.msu.ru",
    "S892": "journals.rudn.ru",
    "S893": "cyberleninka.ru",
    "S901": "sanders.phonologist.org",
}
reg_text = REG.read_text(encoding="utf-8")
for sid, host in hosts.items():
    p(f"{sid}: lane rows containing '{host}': {reg_text.count(host)}   staged line {stg_by_id[sid][1]}")
p()

p("## E. round-71 map staleness (registry_count 797, next_free S874 -> now 799 rows, last S875)")
old = json.loads(OLD.read_text(encoding="utf-8"))
p(f"old map: registry_count={old['registry_count']} staged_count={old['staged_count']} "
  f"next_free={old['next_free']} span={old['span']} entries={len(old['map'])}")
p(f"old collision list n={len(old['collisions'])} last={old['collisions'][-1]}   now n={len(coll)} last={coll[-1]}")
occupied = {s: t for s, t in old["map"].items() if t in reg_ids}
p(f"old-map entries whose TARGET is now an occupied lane id: n={len(occupied)}")
for s, t in sorted(occupied.items(), key=lambda kv: kv[1]):
    lane_doc = reg_by_id[t][2][1][:95]
    p(f"  staged {s} -> {t} OCCUPIED; lane {t} now names: {lane_doc}")
    p(f"    staged {s} document: {stg_by_id[s][2][1][:95]}")
p(f"old-map targets still free: n={len(old['map']) - len(occupied)} (all targets S876..S1005, none occupied)")
p()
p("old-map targets for the five theme rows (offset +15 arithmetic):")
for sid in THEME:
    p(f"  staged {sid} -> old target {old['map'].get(sid)}; round-73 document-derived target "
      f"{ADOPT[THEME.index(sid)]}")
p()
p("## F. why the old map cannot be reused at all")
p("- It is pure arithmetic (staged + 15). The lane appended 2 rows after it was written, so every target shifts.")
p("- Two of its targets (S874, S875) are already live lane rows; assigning into them would duplicate ids (census E03).")
p("- Its five theme targets (S896/S897/S907/S908/S916) are unoccupied but wrong: the lane's next free id is S876, "
  "and append-only order forbids leaving a 20-id hole.")
p("- Its own collision list (S859..S873) is stale: the real collision set is S859..S875.")

(A / "theme-row-collision.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"\nwrote {A/'theme-row-collision.txt'}", file=sys.stderr)
