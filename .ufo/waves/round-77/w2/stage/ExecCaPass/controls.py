import copy, json, os, subprocess, sys
ROOT="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE="211f9526800906e0c585d878d265c37e5e090c15"
S=os.path.dirname(os.path.abspath(__file__))
LED=json.load(open("ledger.json"))
OUT=os.path.join(S,"controls")
def pick(pairs,pid):
    return [p for p in pairs if p["id"]==pid][0]
def run(name, ledger, expect_exit, expect_substrings, cwd=S):
    path=os.path.join(OUT,name+".json")
    json.dump(ledger,open(path,"w"),indent=1)
    p=subprocess.run([sys.executable,"-B",os.path.join(S,"accept-ca.py"),
        "--ledger-check",path,"--root",ROOT,"--base",BASE,
        "--work",os.path.join(S,"work-ctl")],capture_output=True,text=True,cwd=cwd)
    open(os.path.join(OUT,name+".out"),"w").write(p.stdout)
    open(os.path.join(OUT,name+".err"),"w").write(p.stderr)
    ok_rc = (p.returncode==expect_exit)
    text=p.stdout+p.stderr
    missing=[s for s in expect_substrings if s not in text]
    verdict = "OK" if (ok_rc and not missing) else "MISMATCH"
    print("%-26s rc=%d want=%d %s%s" % (name,p.returncode,expect_exit,verdict,
        "" if not missing else " MISSING=%r"%missing))
    if p.stdout.strip(): print("   out: "+p.stdout.strip().replace("\n"," | ")[:300])
    return ok_rc and not missing

def mut(name, fn, expect_exit, subs, base=None):
    L=copy.deepcopy(base or LED)
    fn(L)
    return run(name,L,expect_exit,subs)

def P(L,pid="D01"): return pick(L["pairs"],pid)

def m_absent(L):
    P(L)["stated_text"]="SEAT-CTRL absent text 0xdeadbeef"
def m_wrong_line(L):
    P(L)["stated_at"]="LOG.md:447"
def m_annotate_mutable(L):
    p=P(L); p["stated_at"]="corpus/README.md:755"; p["stated_text"]="Total knowledge entries: 243."
def m_annotate_skill(L):
    p=P(L); p["stated_at"]="SKILL.md:1"; p["stated_text"]="---"
def m_fleet_site(L):
    P(L)["stated_at"]="fleet:LOG.md:3"
def m_eof(L):
    P(L)["stated_at"]="LOG.md:999999"
def m_absent_path(L):
    P(L)["stated_at"]="corpus/nope-not-a-file.md:3"
def m_repair_not_mutable(L):
    p=P(L,"D11"); p["stated_at"]="LOG.md:3"; p["stated_text"]="## 2026-10-17 — mint (round 0)"
def m_repair_no_stmt(L):
    P(L,"D11").pop("statement_after",None)
def m_repair_after_log(L):
    P(L,"D11")["statement_after"]["path"]="LOG.md"
def m_repair_after_nogroup(L):
    P(L,"D11")["statement_after"]["parse"]="Total knowledge"
def m_shell_string(L):
    P(L)["observe_cmd"]="git -C . grep -c -E '^#' %s -- LOG.md"%BASE
def m_no_c(L):
    P(L)["observe_cmd"]=["git","grep","-c","-E","^#",BASE,"--","LOG.md"]
def m_wrong_subcommand(L):
    P(L)["observe_cmd"]=["git","-C",".","push","origin","main"]
def m_rev_in_path(L):
    P(L)["observe_cmd"]=["git","-C",".","grep","-c","-E","^#","--","LOG.md",BASE]
def m_bare_assign(L):
    P(L)["observe_cmd"]=P(L)["observe_cmd"]+["X=1"]
def m_escaped_pipe(L):
    P(L)["observe_cmd"]=P(L)["observe_cmd"]+["a\\|b"]
def m_backtick_rederive(L):
    P(L)["rederive"]="grep -o -E '^#' corpus/README.md `x`"
def m_interpreter(L):
    P(L)["observe_cmd"]=["python3","-c","print(1)"]
def m_echo(L):
    P(L)["observe_cmd"]=["echo","1"]
def m_missing_bin(L):
    P(L)["observe_cmd"]=["seat-ctrl-no-such-binary","--version"]
def m_parse_missing(L):
    P(L).pop("parse")
def m_parse_nogroup(L):
    P(L)["parse"]="^#"
def m_parse_bad(L):
    P(L)["parse"]="([0-9]"
def m_expected_empty(L):
    P(L)["expected_after"]=""
def m_absence(L):
    p=P(L); p["observe_cmd"]=["git","-C",".","grep","-c","-E","^ZZZabsentZZZ",BASE,"--","LOG.md"]; p["expected_after"]="1"
def m_stated_parse_nomatch(L):
    P(L)["stated_parse"]="ZZZ([0-9]+)"
def m_stated_empty(L):
    P(L)["stated_text"]=""
def m_dup_id(L):
    P(L,"D02")["id"]="D01"
def m_min_pairs(L):
    L["pairs"]=L["pairs"][:9]
def m_bad_disp(L):
    P(L)["disposition"]="APPEND"
def m_dead_pin(L):
    P(L)["observe_cmd"]=["git","-C",".","grep","-c","-E","^#","0"*40,"--","LOG.md"]
def m_meta_round(L):
    L["round"]=76
def m_meta_claim(L):
    L["claim"]="C"
def m_meta_base(L):
    L["base"]="0"*40
def m_empty_argv_elem(L):
    P(L)["observe_cmd"]=["git","-C",".","grep","","--","LOG.md"]
def m_observe_not_list(L):
    P(L)["observe_cmd"]={"argv":["git"]}

results=[]
results.append(run("G1-green-cwdscratch",copy.deepcopy(LED),0,["LEDGER-CHECK-77: PASS pairs=11"]))
# G2: -C <lane> declaration form
L2=copy.deepcopy(LED)
for p in L2["pairs"]:
    if p["observe_cmd"][:3]==["git","-C","."]:
        p["observe_cmd"][2]=ROOT
    p["rederive"]=p["rederive"].replace("git -C . ","git -C %s "%ROOT,1)
results.append(run("G2-green-C-lane",L2,0,["LEDGER-CHECK-77: PASS pairs=11"]))
results.append(run("G3-green-cwd-lane",copy.deepcopy(LED),0,["LEDGER-CHECK-77: PASS pairs=11"],cwd=ROOT))
for name,fn,subs in [
 ("R01-stated-absent",m_absent,["stated_text not found in LOG.md at base"]),
 ("R02-wrong-line",m_wrong_line,["NOT on line 447"]),
 ("R03-annotate-mutable",m_annotate_mutable,["not in the frozen ANNOTATE allowlist"]),
 ("R04-annotate-skill",m_annotate_skill,["not in the frozen ANNOTATE allowlist"]),
 ("R05-fleet-site",m_fleet_site,["not a lane path:line"]),
 ("R06-eof",m_eof,["beyond EOF"]),
 ("R07-absent-path",m_absent_path,["stated_at path corpus/nope-not-a-file.md absent at base"]),
 ("R08-repair-not-mutable",m_repair_not_mutable,["not in the frozen REPAIR allowlist"]),
 ("R09-repair-no-statement",m_repair_no_stmt,["REPAIR without a statement_after"]),
 ("R10-repair-after-log",m_repair_after_log,["REPAIR statement_after path LOG.md is not one of the frozen mutable files"]),
 ("R11-repair-after-nogroup",m_repair_after_nogroup,["statement_after.parse has no capture group"]),
 ("R12-shell-string",m_shell_string,["observe_cmd is a shell string"]),
 ("R13-no-c-form",m_no_c,["must open with `-C <dir>`"]),
 ("R14-wrong-subcommand",m_wrong_subcommand,["not in the read-only allowlist"]),
 ("R15-rev-in-path",m_rev_in_path,["does not exist in the clone"]),
 ("R16-bare-assign",m_bare_assign,["bare name=value"]),
 ("R17-escaped-pipe",m_escaped_pipe,["shell construct"]),
 ("R18-rederive-backtick",m_backtick_rederive,["shell construct"]),
 ("R19-interpreter",m_interpreter,["interpreter/constant-printer"]),
 ("R20-echo",m_echo,["not in the observe allowlist"]),
 ("R21-missing-binary",m_missing_bin,["not in the observe allowlist"]),
 ("R22-parse-missing",m_parse_missing,["parse missing"]),
 ("R23-parse-nogroup",m_parse_nogroup,["parse has no capture group"]),
 ("R24-parse-bad",m_parse_bad,["parse does not compile"]),
 ("R25-expected-empty",m_expected_empty,["expected_after is not a non-empty string"]),
 ("R26-absence-pair",m_absence,["absence-observation pair"]),
 ("R27-stated-parse-nomatch",m_stated_parse_nomatch,["stated token cannot be derived"]),
 ("R28-stated-empty",m_stated_empty,["empty stated_text"]),
 ("R29-dup-id",m_dup_id,["duplicate id"]),
 ("R30-min-pairs",m_min_pairs,["the 10-pair floor"]),
 ("R31-bad-disposition",m_bad_disp,["disposition="]),
 ("R32-dead-pin",m_dead_pin,["dead pin"]),
 ("R33-meta-round",m_meta_round,["round=76"]),
 ("R34-meta-claim",m_meta_claim,["claim='C'"]),
 ("R35-meta-base",m_meta_base,["base="]),
 ("R36-empty-argv-elem",m_empty_argv_elem,["not a non-empty string"]),
 ("R37-observe-not-list",m_observe_not_list,["observe_cmd is not a non-empty argv list"]),
]:
    results.append(mut(name,fn,1,subs))
# V: vacuity controls (expected GREEN = admitted)
def m_vacuity_clones(L):
    proto=copy.deepcopy(L["pairs"][0]); L["pairs"]=[]
    for i in range(11):
        p=copy.deepcopy(proto); p["id"]="V%02d"%i; L["pairs"].append(p)
def m_fabricated(L):
    for p in L["pairs"]:
        p["observed_at_base"]="999"; p["expected_after"]="999"
def m_identical_repair(L):
    proto=copy.deepcopy(L["pairs"][10]); L["pairs"]=[]
    for i in range(11):
        p=copy.deepcopy(proto); p["id"]="W%02d"%i; L["pairs"].append(p)
def m_abs_path(L):
    P(L)["observe_cmd"]=["grep","-o","-E","root","/etc/passwd"]
def m_mutable_rev(L):
    P(L)["observe_cmd"]=["git","-C",".","grep","-c","-E","^#","main","--","LOG.md"]
results.append(mut("V01-11-identical-pairs",m_vacuity_clones,0,["LEDGER-CHECK-77: PASS pairs=11"]))
results.append(mut("V02-fabricated-observation",m_fabricated,0,["LEDGER-CHECK-77: PASS pairs=11"]))
results.append(mut("R38-absolute-path",m_abs_path,1,["does not exist in the clone"]))
results.append(mut("R39-mutable-rev",m_mutable_rev,1,["mutable ref"]))
results.append(mut("V03-11-identical-repair",m_identical_repair,0,["LEDGER-CHECK-77: PASS pairs=11"]))
print("SUMMARY %d/%d controls as expected" % (sum(1 for r in results if r), len(results)))
