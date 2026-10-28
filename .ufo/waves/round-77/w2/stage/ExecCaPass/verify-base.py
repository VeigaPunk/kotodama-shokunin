import json, re, subprocess, sys
LANE="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE="211f9526800906e0c585d878d265c37e5e090c15"
L=json.load(open("ledger.json"))
print("meta round=%r claim=%r base=%r status=%r pairs=%d ids_unique=%s" % (
  L.get("round"), L.get("claim"), L.get("base"), L.get("status"),
  len(L["pairs"]), len({p["id"] for p in L["pairs"]})==len(L["pairs"])))
def basefile(p):
    return subprocess.run(["git","-C",LANE,"show","%s:%s"%(BASE,p)],capture_output=True,text=True)
def norm(t): return re.sub(r"\s+"," ",t or "").strip()
bad=0
for p in L["pairs"]:
    path,line=p["stated_at"].rsplit(":",1); line=int(line)
    r=basefile(path)
    body=r.stdout if r.returncode==0 else ""
    lines=body.splitlines()
    on = (0 < line <= len(lines)) and norm(p["stated_text"]) in norm(lines[line-1])
    st_parse=p.get("stated_parse")
    m=re.search(st_parse,p["stated_text"]) if st_parse else None
    stated=(m.group(1) if (m and m.groups()) else (m.group(0) if m else None))
    # independent observe: run the argv literally but with -C lane retargeted
    argv=[LANE if (i==2 and a in (".",)) else a for i,a in enumerate(p["observe_cmd"])]
    # replace literal "." -C operand and rev-as-declared kept
    o=subprocess.run(argv,cwd=LANE,capture_output=True,text=True)
    out=o.stdout
    pm=re.search(p["parse"],out) if p["parse"]!="count-presence" else None
    obs=(pm.group(1) if pm and pm.groups() else None)
    red = norm(stated or "")!=norm(obs or "")
    if not on: bad+=1
    print("%s %-14s line=%d on_line=%s stated=%r observed=%r expected=%r red_base=%s rc=%d out=%r" % (
      p["id"], p["disposition"], line, on, stated, obs, p.get("expected_after"), red, o.returncode, out.strip()[:60]))
print("on_line_failures=%d" % bad)
