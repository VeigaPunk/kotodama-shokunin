import json,re,subprocess,shlex,sys
root="/fast/scratch/hyaku/kotodama-r76/ScribeCorrections/clone"
def load(p):
    d=json.load(open(p))
    return d["pairs"] if isinstance(d,dict) else d
pairs=load("/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w1/stage/ScoutLedgerA/pairs.json")+ \
      load("/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w1/stage/ScoutLedgerB/pairs.json")
print("pairs:",len(pairs))
bad=0
for p in pairs:
    cmd=p["observe_cmd"]
    r=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
    out=r.stdout
    parse=p["parse"]
    if parse=="count-presence":
        n=sum(int(l.rsplit(":",1)[1]) for l in out.strip().splitlines() if l.strip())
        tok="present" if n>0 else "absent"; extra=f"count={n}"
    else:
        m=re.search(parse,out,re.M); tok=(m.group(1) if m and m.groups() else (m.group(0) if m else None)); extra=""
    exp=p["expected_after"]
    ok = tok==exp
    if not ok: bad+=1
    print(f'{p["id"]} {p["disposition"]:8} exp={exp!r:32} got={tok!r:34} {"OK" if ok else "MISMATCH"} rc={r.returncode} {extra}')
print("mismatches:",bad)
