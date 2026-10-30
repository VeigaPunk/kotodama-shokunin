import subprocess, re
LANE="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
def show(rev,path):
    r=subprocess.run(["git","-C",LANE,"show",f"{rev}:{path}"],capture_output=True,text=True)
    return r.stdout
for rev,label in [("44f76d456c1b326a71ffdb381590af825cbf11be","base(44f76d45)"),("4b255745dea45a45d88b17e3c3fea4cdb6700cf7","round78(4b255745)")]:
    receipt=show(rev,"reports/round-78/telemetry/census-end.txt")
    registry=show(rev,"corpus/SOURCES.md")
    rec={}
    for line in receipt.splitlines():
        m=re.match(r"kotodama W01 (S\d+) tierC mined used-by=(\S+)",line)
        if m: rec[m.group(1)]=m.group(2)
    reg={}
    for line in registry.splitlines():
        if line.startswith("| S"):
            f=line.split("|")
            rid=f[1].strip()
            if re.fullmatch(r"S\d+",rid) and len(f)>=13:
                reg[rid]=f[11].strip()   # awk field 12 == split index 11
    mism=[]
    for rid,usedby in sorted(rec.items()):
        actual=reg.get(rid)
        if actual is None: mism.append((rid,usedby,"NO-REGISTRY-ROW"))
        elif usedby!=actual: mism.append((rid,usedby,actual))
        else: print(f"  OK {rid} receipt==registry [{usedby}]")
    print(f"=== {label}: receipt W01 rows={len(rec)} registry rows={len(reg)} MISMATCH count={len(mism)}")
    for m in mism: print("  MISMATCH",m)
