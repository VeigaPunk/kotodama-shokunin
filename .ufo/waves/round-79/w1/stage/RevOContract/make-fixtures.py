#!/usr/bin/env python3
"""Generate RevOContract O-guard contract fixtures (single-field mutants of fx-guard-clean-ledger.json).

Run: python3 make-fixtures.py   (from this directory; writes into ./fixtures/)
Every emitted file is the FULL clean ledger with exactly one documented change,
so each fixture loads independently. Expected verdicts name the O clause the
mutant is the red-before for.
"""
import copy
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CLEAN = os.path.join(HERE, "fixtures", "fx-guard-clean-ledger.json")

with open(CLEAN, encoding="utf-8") as fh:
    doc = json.load(fh)

BASE = doc["ledger"]["base"]  # 362e71615521ddb23f1af02306251a9262a1acdb
TREE = "38612c028083a5a94183ac19dc44ad73ae218e15"  # non-commit pin, probes/fixture-measure.txt


def emit(name, clause, expected, mutate, evidence):
    mut = copy.deepcopy(doc)
    mut["fixture"] = name
    mut["clause"] = clause
    mut["expected_verdict"] = expected
    mut["mutation"] = mutate["desc"]
    mut["red_before_evidence"] = evidence
    mutate["fn"](mut)
    path = os.path.join(HERE, "fixtures", name + ".json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(mut, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("wrote", path)


def pair(mut, pid):
    for p in mut["ledger"]["pairs"]:
        if p["id"] == pid:
            return p
    raise KeyError(pid)


# --- clause (c): fabricated recorded observation (R78-M1 class) ---
emit(
    "fx-mut-fabobs-c", "O clause (c): reject observed_at_base differing from the actual observation",
    "REJECT pair OC-A1 (recorded observation '1' != re-observed 'green-7'); exit nonzero",
    {"desc": "OC-A1 observed_at_base: 'green-7' -> '1' (fabricated; reads no committed byte)",
     "fn": lambda m: pair(m, "OC-A1").__setitem__("observed_at_base", "1")},
    "R78-M1; .ufo/waves/round-77/w2/ScoutLogPairs.md D01-D10 (recorded '1' vs actual '149'); "
    "corpus/lessons/round-78.md R78-M1; routed defect 3 (fix not yet shown able-to-fail)")

# --- clause (d): stated old token equals the actual observation (void correction) ---
emit(
    "fx-mut-nomismatch-d", "O clause (d): reject stated_token equal to the actual observation",
    "REJECT pair OC-A1 (stated_token 'green-7' == observed 'green-7'; no mismatch exists); exit nonzero",
    {"desc": "OC-A1 stated_token: 'old-claim-3' -> 'green-7' (equals observation; also update stated_text/stated_parse to match the lie)",
     "fn": lambda m: (pair(m, "OC-A1").__setitem__("stated_token", "green-7"),
                      pair(m, "OC-A1").__setitem__("stated_text", "the calibration token is token=green-7"),
                      pair(m, "OC-A1").__setitem__("red_at_base", False))},
    ".ufo/waves/round-77/w2/ScoutLogPairs.md D11 'not red at base' (stated 243 = observed 243); "
    "round-77 CLAIMS-DRAFT kill rule 'any ledger pair not red at base'")

# --- clause (b): mutable revisions ---
emit(
    "fx-mut-headrev-b", "O clause (b): refuse mutable revisions (HEAD class)",
    "REFUSE OC-A1 observe_cmd (revision operand 'HEAD' is a symbolic/mutable ref); exit nonzero, never a silent PASS",
    {"desc": "OC-A1 observe_cmd revision operand: 40-hex base -> 'HEAD'",
     "fn": lambda m: pair(m, "OC-A1").__setitem__(
         "observe_cmd", ["git", "-C", ".", "grep", "-o", "-E", "token=[a-z0-9-]+", "HEAD", "--", "records/cal.txt"])},
    ".ufo/waves/round-77/w2/MutCaLedger.md e1 SURVIVED (HEAD accepted by round-76/77 grammar, "
    "REV_NAMES=('HEAD','HEAD^','HEAD~1','@') at reports/round-76/accept-ca.py:1070); O must close this")

emit(
    "fx-mut-branchrev-b", "O clause (b): refuse mutable revisions (branch names)",
    "REFUSE OC-A1 observe_cmd (revision operand 'main' is mutable); exit nonzero",
    {"desc": "OC-A1 observe_cmd revision operand: 40-hex base -> 'main'",
     "fn": lambda m: pair(m, "OC-A1").__setitem__(
         "observe_cmd", ["git", "-C", ".", "grep", "-o", "-E", "token=[a-z0-9-]+", "main", "--", "records/cal.txt"])},
    ".ufo/waves/round-77/w2/MutCaLedger.md e2 KILLED ('main' refused); round-77 CLAIMS-DRAFT "
    "'immutable 40-hex revision in revision position'")

emit(
    "fx-mut-treerev-b", "O clause (b): refuse non-commit 40-hex pins (immutable bytes must be a COMMIT's bytes)",
    "REFUSE OC-A1 observe_cmd (operand is a tree object id, not a commit); exit nonzero",
    {"desc": "OC-A1 observe_cmd revision operand: commit base -> tree id " + TREE,
     "fn": lambda m: pair(m, "OC-A1").__setitem__(
         "observe_cmd", ["git", "-C", ".", "grep", "-o", "-E", "token=[a-z0-9-]+", TREE, "--", "records/cal.txt"])},
    "QUALITY 17/19 (pin measured revision); a tree pin names immutable bytes but not a commit — "
    "the guard's contract says 'immutable committed bytes', so only commit ids are admissible")

# --- clause (b): constant printers ---
emit(
    "fx-mut-echo-b", "O clause (b): refuse constant printers (echo class, J4)",
    "REFUSE OC-A1 observe_cmd (argv[0] 'echo' is a constant printer outside the read-only allowlist); exit nonzero",
    {"desc": "OC-A1 observe_cmd -> ['echo', 'green-7'] (constant-printer)",
     "fn": lambda m: pair(m, "OC-A1").__setitem__("observe_cmd", ["echo", "green-7"])},
    "QUALITY 25 fixture J4; .ufo/waves/round-77/w2/MutCaLedger.md c2 KILLED; "
    "reports/round-76/accept-ca.py observe allowlist {git,grep,wc,sha256sum,ls,cat,head,tail,cut}")

emit(
    "fx-mut-pyprint-b", "O clause (b): refuse evasive constant printers (J4b)",
    "REFUSE OC-A1 observe_cmd (interpreter argv[0] 'python3' refused); exit nonzero",
    {"desc": "OC-A1 observe_cmd -> ['python3', '-c', \"print('green-7')\"] (evasive constant printer reading no clone byte)",
     "fn": lambda m: pair(m, "OC-A1").__setitem__("observe_cmd", ["python3", "-c", "print('green-7')"])},
    "QUALITY 25 fixture J4b ('import os;print(str(...))' class); .ufo/waves/round-77/w2/MutCaLedger.md c1 KILLED")

emit(
    "fx-mut-shellstring-b", "O clause (a)+(b): observe commands are argv arrays, never shell strings",
    "REFUSE OC-A1 observe_cmd (single joined string, not an argv array); exit nonzero",
    {"desc": "OC-A1 observe_cmd -> one shell string 'git -C . grep -o -E token=[a-z0-9-]+ 362e7161... -- records/cal.txt'",
     "fn": lambda m: pair(m, "OC-A1").__setitem__(
         "observe_cmd",
         "git -C . grep -o -E token=[a-z0-9-]+ 362e71615521ddb23f1af02306251a9262a1acdb -- records/cal.txt")},
    "round-77 CLAIMS-DRAFT Ca: 'observe/rederive stored and executed as validated argv'; "
    "reports/round-76/accept-ca.py H2 guard (shell string refused)")

# --- clause (a): path/option discipline ---
emit(
    "fx-mut-pathtrav", "O clause (a): refuse paths escaping the pinned repo",
    "REFUSE OC-A1 observe_cmd (path operand '../outside.txt' escapes the fixture repo); exit nonzero",
    {"desc": "OC-A1 observe_cmd path operand: 'records/cal.txt' -> '../outside.txt'",
     "fn": lambda m: pair(m, "OC-A1").__setitem__(
         "observe_cmd", ["git", "-C", ".", "grep", "-o", "-E", "token=[a-z0-9-]+", BASE, "--", "../outside.txt"])},
    "QUALITY 19 (counter grades committed bytes in a materialized clone); MutPath seat family")

emit(
    "fx-mut-optinject", "O clause (a): refuse option injection in operand position",
    "REFUSE OC-A1 observe_cmd (operand '-c' option injection attempt in path position); exit nonzero",
    {"desc": "OC-A1 observe_cmd: append operand '-c' after '--'",
     "fn": lambda m: pair(m, "OC-A1").__setitem__(
         "observe_cmd", ["git", "-C", ".", "grep", "-o", "-E", "token=[a-z0-9-]+", BASE, "--", "records/cal.txt", "-c"])},
    "MutRevision seat family (option injection fixtures); reports/round-76/accept-ca.py _git_grep_problem role parsing")

# --- do-nothing control ---
emit(
    "fx-donothing", "do-nothing control: an empty ledger is not a pass",
    "REJECT (zero pairs is the do-nothing landing; never PASS); exit nonzero",
    {"desc": "ledger.pairs -> []",
     "fn": lambda m: m["ledger"].__setitem__("pairs", [])},
    "QUALITY 25/26 do-nothing control; lands==freeze graded, never passed")

# --- structural: duplicate pair id ---
emit(
    "fx-dupid", "structural: duplicate pair ids are not two independent mismatches",
    "REJECT (duplicate id OC-A2); exit nonzero",
    {"desc": "second pair id 'OC-A2' -> duplicate of the first (same id, both rows otherwise identical)",
     "fn": lambda m: m["ledger"]["pairs"].__setitem__(1, copy.deepcopy(m["ledger"]["pairs"][0]))},
    "round-77 CLAIMS-DRAFT Ca: 'reject duplicates'; round-76 ledger.json status (20 unique pairs)")

print("done")
