import sys
lines=open(sys.argv[1],encoding="utf-8").read().split("\n")
blocks=[]; cur=[]; start=0
for i,l in enumerate(lines,1):
    if l.startswith("|"):
        if not cur: start=i
        cur.append(l)
    else:
        if cur: blocks.append((start,cur)); cur=[]
if cur: blocks.append((start,cur))
bad=0
for s,b in blocks:
    nf={len(l.split("|")) for l in b}
    print("table at line %d: rows=%d splits=%s %s"%(s,len(b),sorted(nf),"OK" if len(nf)==1 else "MISMATCH"))
    bad+= len(nf)>1
print("mismatched:",bad)
