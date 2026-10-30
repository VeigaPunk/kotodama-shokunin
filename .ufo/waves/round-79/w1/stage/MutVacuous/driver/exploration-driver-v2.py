# MutVacuous driver v2: observed tokens are taken from the counter's own
# evaluate_pairs at base (not assumed); mutants are built from those values.
import copy, importlib.util, json, os, tempfile
W = "/fast/scratch/hyaku/kotodama-r79/MutVacuous"
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
spec = importlib.util.spec_from_file_location("acca", os.path.join(W, "accept-ca.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
work = os.path.join(W, "work")
m.CTX["root"] = LANE; m.CTX["fleet_root"] = None; m.RUN_STATE["work"] = work
cfg = {"base": BASE, "root": LANE, "fleet_root": None,
       "repair_mutable": list(m.REPAIR_MUTABLE), "annotate_append": list(m.ANNOTATE_ALLOW),
       "lane_row_ids": [], "c_families": [], "min_pairs": m.MIN_PAIRS_FLOOR}
m.CTX["cfg"] = cfg
tmp = tempfile.mkdtemp(prefix="basemm2-", dir=work)
clone = m.materialize(LANE, BASE, tmp, "base")
assert clone is not None
PRISTINE = json.load(open(os.path.join(W, "ledgers", "pristine.json")))["pairs"]
# observed at base, computed by the counter itself
OBS = {}
for p in PRISTINE:
    t, parsed, why = m.observed_token(p, clone["path"])
    OBS[p["id"]] = t
print("OBSERVED-AT-BASE (counter's own run):", json.dumps(OBS))

def run(label, pairs, quiet_rows=False):
    print("=== %s" % label)
    ev = m.evaluate_pairs(pairs, clone, clone)
    if not quiet_rows:
        for p, e in zip(pairs, ev):
            print("  %-4s stated=%r ok=%s base_obs=%r parsed=%s why=%r" % (
                p["id"], e["stated"], e["stated_ok"], e["base"][0], e["base"][1], e["base"][2]))
    out = []
    m.leg_basemismatch(out, cfg, pairs, ev)
    for name, passed, detail in out:
        print("  VERDICT %s passed=%s detail=%s" % (name, passed, detail))
    print()

def by(pairs, pid): return next(p for p in pairs if p["id"] == pid)
def no_obs_rec(pairs):
    for p in pairs: p.pop("observed_at_base", None)

if __name__ == "__main__":
    run("V0 pristine probe, as committed", copy.deepcopy(PRISTINE))
    run("V0b pristine minus observed_at_base (isolates the stated-token path)", (lambda x: (no_obs_rec(x), x)[1])(copy.deepcopy(PRISTINE)))
    # M1': one pair's stated token := its actual observed token (new==observed)
    def m1(pairs):
        no_obs_rec(pairs)
        p = by(pairs, "D11"); p.pop("stated_parse", None); p["stated_token"] = OBS["D11"]
    run("M1' D11 stated_token := actual observed %r (new==observed, only pair changed)" % OBS["D11"], (lambda: m1_pairs())()) if False else None
    pairs = copy.deepcopy(PRISTINE); m1(pairs); run("M1' D11 stated_token := actual observed %r (new==observed)" % OBS["D11"], pairs)
    # M2': every pair stated := its actual observed token
    pairs = copy.deepcopy(PRISTINE); no_obs_rec(pairs)
    for p in pairs:
        p.pop("stated_parse", None); p["stated_token"] = OBS[p["id"]]
    run("M2' every pair stated_token := actual observed (all green)", pairs)
    # M3': vacuity: no stated token derivation at all -> whole sentence; no observed_at_base
    pairs = copy.deepcopy(PRISTINE); no_obs_rec(pairs)
    for p in pairs:
        p.pop("stated_parse", None); p.pop("stated_token", None)
    run("M3' no stated_token/stated_parse anywhere, no observed_at_base (whole-sentence stated)", pairs)
    # M4': invalid explicit stated tokens: whitespace-only and empty, mixed with valid reds
    pairs = copy.deepcopy(PRISTINE); no_obs_rec(pairs)
    for p in pairs: p.pop("stated_parse", None); p["stated_token"] = "9" + p["id"]
    by(pairs, "D02")["stated_token"] = "   "
    by(pairs, "D03")["stated_token"] = ""
    run("M4' D02 stated_token='   ', D03 stated_token='' (invalid), other 9 valid-but-wrong", pairs)
    # M5': parse-miss on one pair, stated token set (invalid observation must not count as red)
    pairs = copy.deepcopy(PRISTINE); no_obs_rec(pairs)
    for p in pairs: p.pop("stated_parse", None); p["stated_token"] = "9" + p["id"]
    by(pairs, "D04")["parse"] = r"^NOPE:([0-9]+)$"
    run("M5' D04 parse-miss (invalid observation), other 10 valid-but-wrong", pairs)
    # M6': observe_cmd unknown binary (invalid observation)
    pairs = copy.deepcopy(PRISTINE); no_obs_rec(pairs)
    for p in pairs: p.pop("stated_parse", None); p["stated_token"] = "9" + p["id"]
    by(pairs, "D05")["observe_cmd"] = ["git", "-C", ".", "grep", "-c", "-E", "^#", "0000000000000000000000000000000000000000", "--", "LOG.md"]
    run("M6' D05 observe_cmd on non-existent revision (invalid observation)", pairs)
    # M7': truncation boundary: no-parse pair, stated token equal to the FULL observed text
    full_cmd = ["git", "-C", ".", "grep", "-h", "-E", "^#", BASE, "--", "LOG.md"]
    out, why = m.run_observe(clone["path"], full_cmd)
    full = m.norm(out)
    trunc = full[:200]
    print("TRUNC probe: len(full)=%d len(norm[:200])=%d why=%r" % (len(full), len(trunc), why))
    base_pair = {"id": "T01", "observe_cmd": full_cmd, "stated_text": full, "stated_token": full}
    pairs = [base_pair] + [dict(p, stated_token="9"+p["id"]) for p in copy.deepcopy(PRISTINE)[:9]]
    pairs = [{k: v for k, v in p.items() if k != "stated_parse"} for p in pairs]
    run("M7' T01 no parse, stated_token := FULL observed text (len %d)" % len(full), pairs)
    base_pair2 = dict(base_pair, stated_token=trunc)
    pairs[0] = base_pair2
    run("M7'' T01 no parse, stated_token := 200-char prefix (len %d)" % len(trunc), pairs)
