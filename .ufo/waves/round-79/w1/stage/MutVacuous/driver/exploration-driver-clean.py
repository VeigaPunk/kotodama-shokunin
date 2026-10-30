import json, os, sys
sys.argv = [sys.argv[0]]
import importlib.util
W = "/fast/scratch/hyaku/kotodama-r79/MutVacuous"
exec(open(os.path.join(W, "driver-v2.py")).read().split('if __name__ == "__main__":')[0])
led = json.load(open(os.path.join(W, "ledgers", "clean-control-v2.json")))
run("CLEAN control v2 (10 truthful pairs), observed_at_base present", led["pairs"])
