import json, subprocess, sys, importlib.util, re
sys.dont_write_bytecode=True
L="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
B="98c486bdb4650ba5b8e651d332910e8ee60ad121"
spec=importlib.util.spec_from_file_location("ac",L+"/reports/round-75/accept-ca.py"); ac=importlib.util.module_from_spec(spec); spec.loader.exec_module(ac)
pairs=json.load(open(L+"/.ufo/waves/round-76/w1/stage/ScoutLedgerA/pairs.json"))
ac.CTX["fleet_root"]="/home/vgpnk/Projects/shokunin"
for p in pairs:
    path,line=p["stated_at"].rsplit(":",1); line=int(line)
    body=subprocess.run(["git","-C",L,"show",B+":"+path],capture_output=True,text=True).stdout
    lines=body.splitlines(); st=ac.norm(p["stated_text"])
    on_line = st in ac.norm(lines[line-1]); in_body = st in ac.norm(body)
    tok,ok=ac.stated_token(p)
    why=ac.observe_problem(p["observe_cmd"],L)
    rwhy=ac.observe_problem(__import__("shlex").split(p["rederive"]),L,rederive=True)
    ot,parsed,pw=ac.observed_token(p,L)
    print(p["id"],"on_line=%s in_body=%s stated_tok=%r anchored=%s observe_problem=%r rederive_problem=%r observed=%r parsed=%s"%(on_line,in_body,tok,tok in st,why,rwhy,ot,parsed), "red=",ot!=tok, "line:",lines[line-1][:90])
