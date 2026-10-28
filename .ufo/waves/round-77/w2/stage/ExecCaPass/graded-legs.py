import importlib.util, json, os
S=os.path.dirname(os.path.abspath(__file__)); os.chdir(S)
spec=importlib.util.spec_from_file_location("aca", os.path.join(S,"accept-ca.py"))
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
LANE="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE="211f9526800906e0c585d878d265c37e5e090c15"
m.CTX["root"]=LANE; m.CTX["fleet_root"]=None; m.CTX["cfg"]={}
m.RUN_STATE["work"]=os.path.join(S,"work-tok"); os.makedirs(m.RUN_STATE["work"],exist_ok=True)
cfg={"base":BASE,"root":LANE,"lands":BASE,"fleet_root":None,"round":77,
     "repair_mutable":list(m.REPAIR_MUTABLE),
     "annotate_append":list(m.ANNOTATE_ALLOW),
     "lane_row_ids":[], "c_families":[], "min_pairs":m.MIN_PAIRS_FLOOR,
     "claim_c_owned_inplace":[]}
led=json.load(open("ledger.json")); pairs=led["pairs"]
ev=m.evaluate_pairs(pairs, {"path":LANE}, {"path":LANE})
out=[]
ok=m.leg_basemismatch(out,cfg,pairs,ev)
print("BASEMISMATCH_PASSED=%s" % ok)
ok2=m.leg_repair(out,cfg,pairs,ev)
print("REPAIR_PASSED=%s" % ok2)
