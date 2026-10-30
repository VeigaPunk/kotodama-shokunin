# Derives the mutation fixture set from the truthful control (clean-control-v2),
# so each fixture differs from a fully valid ledger by exactly one defect.
import copy, json, os, sys
FX = sys.argv[2]
IN = sys.argv[1]
import subprocess
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
ctrl = json.load(open(os.path.join(IN, "clean-control-v2.json")))
def save(name, pairs, note):
    led = dict(ctrl); led["pairs"] = pairs; led["status"] = "MUTANT fixture: " + note
    json.dump(led, open(os.path.join(FX, name), "w"), ensure_ascii=False, indent=1)
def P(pairs, pid):
    return next(p for p in pairs if p["id"] == pid)
base = copy.deepcopy(ctrl["pairs"])
save("f00-truthful-clean.json", copy.deepcopy(base), "none (control: expect guard PASS)")
x = copy.deepcopy(base); P(x, "C03")["stated_token"] = P(x, "C03")["observed_at_base"]
save("f01-stated-eq-observed-one.json", x, "C03 stated_token := observed_at_base (new==observed)")
x = copy.deepcopy(base)
for p in x: p["stated_token"] = p["observed_at_base"]
save("f02-stated-eq-observed-all.json", x, "every stated_token := observed_at_base")
x = copy.deepcopy(base); p = P(x, "C01"); p.pop("stated_token"); p.pop("stated_parse", None)
save("f03-stated-token-absent-whole-text.json", x, "C01 no stated_token: whole stated_text becomes the token")
x = copy.deepcopy(base); P(x, "C02")["stated_token"] = "   "
save("f04-stated-whitespace.json", x, "C02 stated_token = '   '")
x = copy.deepcopy(base); P(x, "C02")["stated_token"] = ""
save("f05-stated-empty.json", x, "C02 stated_token = ''")
x = copy.deepcopy(base); P(x, "C04")["parse"] = r"^NOPE:([0-9]+)$"
save("f06-observed-parse-miss.json", x, "C04 parse matches nothing")
x = copy.deepcopy(base); P(x, "C05")["observe_cmd"] = ["git", "-C", ".", "grep", "-c", "-E", "^#", "0" * 40, "--", "SCORECARD.md"]
save("f07-observed-dead-pin.json", x, "C05 observe_cmd pinned to a non-object")
x = copy.deepcopy(base); p = P(x, "C06")
p["observe_cmd"] = ["git", "-C", ".", "grep", "-h", "-o", "-E", "entries: [0-9]+", BASE, "--", "corpus/README.md"]
p["parse"] = "entries: ([0-9]+)"; p["stated_token"] = "0"; p["observed_at_base"] = "243"
save("f08-observed-multimatch-first-occurrence.json", x, "C06 observation matches 5 footers; parse takes the first (243)")
x = copy.deepcopy(base); p = P(x, "C07"); p.pop("parse", None)
p["observe_cmd"] = ["git", "-C", ".", "grep", "-h", "-E", "^#", BASE, "--", "LOG.md"]
p.pop("observed_at_base", None)
full = " ".join(subprocess.run(["git","-C","/home/vgpnk/Projects/shokunin/kotodama-shokunin","grep","-h","-E","^#",BASE,"--","LOG.md"],capture_output=True,text=True).stdout.split())
p["stated_token"] = full
save("f09-observed-no-parse-overcap-placeholder.json", x, "C07 no parse; observation is 11199 chars; token is truncated to 200")
x = copy.deepcopy(base); P(x, "C08").pop("observed_at_base", None)
save("f10-observed_at_base-absent.json", x, "C08 observed_at_base removed")
x = copy.deepcopy(base); P(x, "C09")["observed_at_base"] = "1"
save("f11-observed_at_base-wrong.json", x, "C09 observed_at_base '1' while actual is 2")
