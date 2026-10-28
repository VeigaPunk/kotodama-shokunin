import importlib.util, json, os, sys
S=os.path.dirname(os.path.abspath(__file__)); os.chdir(S)
spec=importlib.util.spec_from_file_location("aca", os.path.join(S,"accept-ca.py"))
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
LANE="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE="211f9526800906e0c585d878d265c37e5e090c15"
m.CTX["root"]=LANE; m.CTX["fleet_root"]=None
m.RUN_STATE["work"]=os.path.join(S,"work-tok"); os.makedirs(m.RUN_STATE["work"],exist_ok=True)
cfg={"base":BASE,"root":LANE,"fleet_root":None,
     "repair_mutable":list(m.REPAIR_MUTABLE),
     "annotate_append":list(m.ANNOTATE_ALLOW),
     "lane_row_ids":[], "c_families":[]}
L=json.load(open("ledger.json"))
rows=[]; nred=0
for p in L["pairs"]:
    st,stok=m.stated_token(p)
    obs,ok,why=m.observed_token(p,LANE)
    probs=m.pair_problems(cfg,p,LANE)
    red = (st is not None and obs is not None and m.norm(st)!=m.norm(obs))
    nred+=1 if red else 0
    rows.append((p["id"],p["disposition"],st,obs,p.get("observed_at_base"),p.get("expected_after"),red,len(probs)))
    print("%s %-8s stated=%-12r observed=%-12r recorded_ob=%r expected=%r red_at_base=%-5s pair_problems=%d"
          % (p["id"],p["disposition"],st,obs,p.get("observed_at_base"),p.get("expected_after"),red,len(probs)))
print("RED_AT_BASE %d/11 ; RECORDED_MATCHES_OBSERVED %d/11"
      % (nred, sum(1 for r in rows if r[4] is not None and m.norm(r[4])==m.norm(r[3] or ""))))
