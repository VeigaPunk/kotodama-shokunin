#!/usr/bin/env python3
"""Round-74 landing edits (worktree). Usage: apply-landing.py ca|c"""
import re, sys, shutil, subprocess
LANE="/home/vgpnk/Projects/shokunin/kotodama-shokunin"; W=LANE+"/.ufo/waves/round-74"; D=W+"/drafts"
def rd(p): return open(p,encoding="utf-8").read()
def wr(p,t): open(p,"w",encoding="utf-8").write(t)
which=sys.argv[1]
if which=="ca":
    # SKILL.md: line 594 repair + gate rows
    s=rd(LANE+"/SKILL.md")
    old="- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization"
    new="- `corpus/knowledge/civilizations/` — 95 entries: 93 earlier-civilization"
    assert s.count(old)==1; s=s.replace(old,new)
    rows=[l for l in rd(D+"/skill-gates-rows.md").splitlines() if l.startswith("| accept-c-74") or l.startswith("| accept-ca-74") or l.startswith("| accept-c-73 / accept-ca-73")]
    assert len(rows)==3, len(rows)
    lines=s.split("\n")
    idx=max(i for i,l in enumerate(lines) if l.startswith("| accept-ca-73 |"))
    lines[idx+1:idx+1]=rows
    wr(LANE+"/SKILL.md","\n".join(lines))
    # SCORECARD corrections
    tab=[l for l in rd(D+"/annotate-rows.md").splitlines() if re.match(r"^\| LC-\d+ \|",l)]
    assert len(tab)==12,len(tab)
    sc=rd(LANE+"/SCORECARD.md")
    sec="\n## Corrections — round 74\n\nAppend-only record (hyaku run 7, L1 KotodamaR74). Claim Ca ledger `reports/round-74/ledger.json` (frozen with `reports/round-74/claims.json`). Counter: `python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin`. The filed lines named below stand as filed; each row carries id, old token, new token and the re-derivation command, which the counter re-runs.\n\n| id | old token | new token | re-derivation command |\n|---|---|---|---|\n"+"\n".join(tab)+"\n"
    if not sc.endswith("\n"): sc+="\n"
    wr(LANE+"/SCORECARD.md",sc+sec)
    # QUALITY 25
    q=rd(D+"/quality-25.md").split("## The criterion, as it would be appended\n",1)[1].split("\nCheck (red-before",1)
    body=q[0].strip("\n")
    chk="\nCheck (red-before"+q[1].split("\n## What it does not cover",1)[0]
    qm=rd(LANE+"/corpus/QUALITY.md"); 
    if not qm.endswith("\n"): qm+="\n"
    wr(LANE+"/corpus/QUALITY.md",qm+"\n"+body+"\n"+chk.rstrip("\n")+"\n")
    print("ca applied")
elif which=="c":
    shutil.copy(D+"/worldbuilding-setting-practice.md",LANE+"/corpus/knowledge/culture-material/worldbuilding-setting-practice.md")
    shutil.copy(D+"/worldbuilding-setting-practice.amend-2026-10-23.md",LANE+"/corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md")
    shutil.copy("/tmp/ScribeReadmeIndex/r74/README.md",LANE+"/corpus/README.md")
    sh=LANE+"/corpus/SOURCES.md"; s=rd(sh); lines=s.split("\n")
    rows=[l for l in rd(D+"/rows-S881-S884.md").splitlines() if re.match(r"^\| S88[1-4] ",l)]
    assert len(rows)==4
    ch=[l for l in rd(D+"/s877-usedby-change.md").splitlines() if l.startswith("| S877 ")]
    assert len(ch)==2; assert lines.count(ch[0])==1, "old S877 line mismatch"
    lines[lines.index(ch[0])]=ch[1]
    idx=max(i for i,l in enumerate(lines) if re.match(r"^ {0,3}\|\s*S880\s*\|",l))
    lines[idx+1:idx+1]=rows
    wr(sh,"\n".join(lines))
    print("c applied")
