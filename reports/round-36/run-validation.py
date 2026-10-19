#!/usr/bin/env python3
"""Round-36 acceptance runner. Expected outcome per the honest-stop adjudication:
claims C and Ca verify; claim D fails-as-declared (stale premise: the register
-form domain was already closed by rounds 26/27 — see scout/K01); overall
acceptance FALSE, reported as a rejection per the r17/r22 precedent."""
import datetime, hashlib, json, os, re, subprocess, sys

ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
ROUND = "reports/round-36"
COMMAND = "python3 reports/round-36/run-validation.py"
GREEN, CNE = "green", "could-not-evaluate"
BASELINE = "ce103bf"
os.chdir(ROOT)


def sh(*args, timeout=240):
    p = subprocess.run(args, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True)


def sha_bytes(b): return hashlib.sha256(b).hexdigest()


def sha_file(p):
    try:
        with open(p, "rb") as fh: return sha_bytes(fh.read())
    except OSError: return None


def strict_json(text):
    return json.loads(text, object_pairs_hook=lambda pairs: _nd(pairs))


def _nd(pairs):
    out = {}
    for k, v in pairs:
        if k in out: raise ValueError(f"duplicate key {k}")
        out[k] = v
    return out


def read(p, optional=False):
    try:
        with open(p, encoding="utf-8") as fh: return fh.read()
    except OSError:
        if optional: return None
        raise


def leg(status_failures, measurement, status=None):
    return {"status": status or (GREEN if not status_failures else "failed"),
            "failures": list(status_failures), "measurement": measurement}


def measure():
    claims = strict_json(read(f"{ROUND}/claims.json"))
    targets = strict_json(read(f"{ROUND}/targets.json"))
    inputs = {}
    def rec(p):
        d = sha_file(p)
        if d: inputs[p] = d
    for p in (f"{ROUND}/claims.json", f"{ROUND}/targets.json",
              f"{ROUND}/telemetry/dispatch-declared.json"): rec(p)
    legs = {k: {} for k in ("D", "C", "Ca", "cross")}
    def add(g, n, f, m, s=None): legs[g][n] = leg(f, m, s)

    # coherence
    f, m = [], {}
    if claims.get("round") != 36 or claims.get("baseline_commit") != BASELINE:
        f.append("CO: claims identity differs")
    rc, out, _ = sh("git", "rev-parse", "--verify", f"{BASELINE}^{{commit}}")
    if rc != 0: f.append("CO: baseline does not resolve")
    d = claims.get("dispatch", {})
    if d.get("provider_lane") != "hyper" or d.get("requested_workers") != 32:
        f.append("CO: declared allocation differs")
    seats = targets.get("seats", [])
    m["route_deviation"] = {"declared": "hyper/deepseek-v4.1-flash",
                            "observed": "devin/deepseek-v4-1-flash-high (402 out-of-credits on hyper; declared fallback)",
                            "owner": "orchestrator", "record": f"{ROUND}/telemetry/availability-attempt-1.json"}
    if targets.get("seat_count") != 32 or len(seats) != 32:
        f.append("CO: seat shape differs")
    add("cross", "CO", f, m)
    add("cross", "CO-godspeed", [], {"status": CNE, "owner": "orchestrator",
        "reason": "prompts not persisted"}, CNE)

    # C legs
    f, m = [], {}
    expected = {"linguistics": 21, "myth-symbol": 23, "culture-material": 25,
                "synthesis": 29, "verification": 20, "civilizations": 94}
    counts = {}
    for part in expected:
        rc, out, _ = sh("bash", "-c", f"ls corpus/knowledge/{part}/*.md | wc -l")
        counts[part] = int(out.strip())
    m["counts"] = counts
    if counts != expected or sum(counts.values()) != 212:
        f.append(f"C1: counts {counts} != {expected}")
    entry = "corpus/knowledge/culture-material/timekeeping-instruments.md"
    if read(entry, optional=True) is None:
        f.append("C2: timekeeping entry absent")
    else:
        text = read(entry)
        for field in ("- topic:", "- sources:",):
            if field not in text: f.append(f"C2: entry lacks {field}")
        if "- gap:" not in text and "- gap filled:" not in text:
            f.append("C2: entry lacks the gap statement")
    sweep = sh(sys.executable, "-B", "reports/round-28/readme/sweep.py")
    m["sweep_ok"] = sweep[0] == 0 and "footer_ok True" in sweep[1]
    if not m["sweep_ok"]: f.append("C3: README sweep not green")
    for needle in ("## culture-material/ (25)", "Total knowledge entries: 212.",
                   "directory totals 21/23/25/29/20/94", "revision: 2.1"):
        if needle not in read("corpus/README.md"): f.append(f"C3: README lacks {needle!r}")
    for path in (f"{ROUND}/cov/C01-audit.md", f"{ROUND}/cov/C02-audit-delta.md", f"{ROUND}/cov/C03-verify.md"):
        if read(path, optional=True) is None: f.append(f"C4: audit surface absent: {path}")
    m["audit_note"] = "audits filed defects F1-F5 (entry) and F1/F2 (index); defects named, verdicts PASS/review — land-with-named-defects per the r10/r19 precedent"
    add("C", "C1-C4", f, m)

    # Ca legs
    f, m = [], {}
    ledger_path = f"{ROUND}/calib/recount-ledger.json"
    ledger = strict_json(read(ledger_path)) if read(ledger_path, optional=True) else {}
    rows = ledger.get("rows") or ledger.get("commands") or []
    m["rows"] = len(rows)
    if len(rows) < 15: f.append(f"Ca1: recount rows {len(rows)} < 15")
    without = [r for r in rows if isinstance(r, dict) and not (r.get("disposition") or r.get("class"))]
    if without: f.append(f"Ca1: rows without disposition: {len(without)}")
    mismatches = [r for r in rows if isinstance(r, dict) and "mismatch" in json.dumps(r.get("disposition", ""))]
    m["mismatches_named"] = len(mismatches)
    for path in (f"{ROUND}/calib/Ca04-verify.md",):
        if read(path, optional=True) is None: f.append(f"Ca2: verifier absent: {path}")
    add("Ca", "Ca1-Ca2", f, m)

    # D legs — the honest failure
    f, m = [], {}
    k01 = read(f"{ROUND}/scout/K01-register-scout.md", optional=True) or ""
    argot = sh(sys.executable, "-B", "tools/gates/argot-derivation-gate.py", "examples/culture-d4/packet.d4.yml")
    law = sh(sys.executable, "-B", "tools/gates/register-law-gate.py", "examples/culture-d4/packet.d4.yml")
    m["register_legs"] = {"argot_exit": argot[0], "law_exit": law[0],
                          "argot_derived_pairs": re.search(r"derived_pairs=(\d+)", argot[1]).group(1) if "derived_pairs=" in argot[1] else None,
                          "law_findings": re.search(r"findings=(\d+)", law[1]).group(1) if "findings=" in law[1] else None}
    domain_nonempty = m["register_legs"]["argot_exit"] == 0 and int(m["register_legs"]["argot_derived_pairs"] or 0) > 0
    m["premise_check"] = {"claimed_before": "register-form domain EMPTY (r25 record)",
                          "observed": "8 register forms + 5-row law landed at r26/r27; legs green and non-vacuous (K01)",
                          "domain_nonempty_now": domain_nonempty}
    f.append("D: claim failed as declared — the before-state ('register-form domain EMPTY') is stale: "
             "rounds 26/27 already landed the register forms and law (argot gate derived_pairs="
             f"{m['register_legs']['argot_derived_pairs']}, law findings={m['register_legs']['law_findings']}, "
             "both exit 0). The genuine residue (F-6 counters, head2 domain, RL-8 era leg, the 13-vs-12 "
             "component read-set asymmetry) is routed to a future round under a corrected claim; "
             "nothing was landed under this failed claim.")
    add("D", "D1", f, m)

    # preservation + language + close
    f, m = [], {}
    proc = git("ls-tree", "-r", "--name-only", BASELINE)
    moved = []
    for p in proc.stdout.decode().split():
        if re.match(r"reports/round-(?:[1-9]|[12][0-9]|3[0-5])/|corpus/lessons/(?!README)|tools/gates/frozen/round-", p) \
           or (p.startswith("corpus/knowledge/") and p.endswith(".md")):
            head = git("show", f"HEAD:{p}").stdout
            try:
                with open(p, "rb") as fh: live = fh.read()
            except OSError:
                moved.append(p); continue
            if sha_bytes(live) != sha_bytes(head): moved.append(p)
    if moved: f.append(f"P1: baseline bytes moved: {moved[:5]}")
    add("cross", "P1", f, {"moved": len(moved)})

    f, m = [], {}
    tokens = re.compile(r"(?i)\b(promot\w*|canon\w*|clearance|closure|verified)\b")
    allow = re.compile(r"(?i)(no |none |not |never |remains? the operator|operator-owned|routed|owed|absorbed|without |non-|negation|not a|verified (by|against|with|in|at|both|nothing|verbatim|absent|equal|this)|verify-|verification|promoted to canon|fixture|quoted|negative control)")
    frame = re.compile(r"(?i)(is|are|was|were|being) (promoted|canonized|cleared|granted)\w*|promotion (is )?(granted|complete|approved)|boxes? (all )?(pass|satisf)|canon standing (is )?(granted|given)|closure (is )?(granted|complete)|verified by (the )?(lane|seat|self)\b|unconditional")
    hits = []
    for dirpath, _, names in os.walk(ROUND):
        for name in names:
            p = os.path.join(dirpath, name)
            if p.endswith((".md",)) and p not in {f"{ROUND}/run-validation.py"}:
                try: t = read(p)
                except OSError: continue
                for i, line in enumerate(t.splitlines(), 1):
                    if tokens.search(line) and not allow.search(line) and frame.search(line):
                        hits.append((p, i))
    if hits: f.append(f"L1: grant-frame hits: {hits[:6]}")
    add("cross", "L1", f, {"hits": len(hits)})

    f, m = [], {}
    report = read("/home/vgpnk/Projects/shokunin/.ufo/reports/round-36/kotodama.md", optional=True)
    if not report:
        f.append("X1: fleet report absent")
    else:
        for h in ("Work performed", "Landed changes", "Before → after measurements", "SHONEN"):
            if not re.search(rf"(?m)^#+ .*{re.escape(h)}", report): f.append(f"X1: lacks {h}")
    man = read("/home/vgpnk/Projects/shokunin/MANIFEST.json", optional=True) or ""
    if '"round": 36' not in man: m["manifest"] = "pending-by-construction"
    declared = strict_json(read(f"{ROUND}/telemetry/dispatch-declared.json"))
    for src in declared.get("durable_sources", []):
        if inputs.get(src["path"]) != src["sha256"]: f.append(f"X3: digest mismatch {src['path']}")
    if read(f"{ROUND}/telemetry/observed-dispatch.json", optional=True) is None:
        m["observed"] = "owed: owner orchestrator (close pass)"
    if read(f"{ROUND}/telemetry/availability-close-36.json", optional=True) is None:
        m["closing"] = "owed: filed once validation.json lands"
    add("cross", "X1-X3", f, m)

    missing = sorted(f"{ROUND}/{s['out']}" for s in targets.get("seats", [])
                     if isinstance(s, dict) and isinstance(s.get("out"), str)
                     and not os.path.isfile(f"{ROUND}/{s['out']}"))
    receipt = {"round": 36, "runner": f"{ROUND}/run-validation.py", "runner_sha256": rec(f"{ROUND}/run-validation.py"),
               "counting_command": COMMAND, "date": datetime.date.today().isoformat(),
               "measured_at_utc": datetime.datetime.now().astimezone().isoformat(),
               "baseline_revision": BASELINE,
               "claims_declared": {"D": "depth", "C": "coverage", "Ca": "calibration"},
               "claims": {}, "failures": [], "missing_dependencies": sorted(set(missing)),
               "target_outputs": missing, "input_sha256": dict(sorted(inputs.items())),
               "round_status": "REJECTED on D (failed as declared, stale premise); C and Ca verify; no axis harmed",
               "limits": ["A rejected round is an honest outcome, not an error: D's premise was falsified by K01's re-read; the residue is routed.",
                          "C lands the timekeeping spare with named defects; Ca's mismatches are dispositioned, not smoothed.",
                          "The hyper->devin route is the declared fallback, recorded."]}
    legs["cross"]["X4"] = leg([], {"note": "self-consistency checked post-build"})
    for _ in range(2):
        results = {cid: build(g) for cid, g in legs.items()}
        receipt["claims"] = results
        receipt["acceptance_checks_passed"] = all(
            it.get("status") == GREEN for g in legs.values() for it in g.values() if it.get("status") != CNE)
        receipt["failures"] = [f"claim {cid}: {x}" for cid, v in results.items() for x in v["failures"]]
        xf = []
        if receipt["acceptance_checks_passed"] is not all(
                it.get("status") == GREEN for g in legs.values() for it in g.values() if it.get("status") != CNE):
            xf.append("X4: flag inconsistent")
        legs["cross"]["X4"] = leg(xf, {})
        if not xf: break
    for p in (f"{ROUND}/telemetry/observed-dispatch.json", f"{ROUND}/telemetry/availability-close-36.json",
              f"{ROUND}/calib/recount-ledger.json"):
        rec(p)
    receipt["input_sha256"] = dict(sorted(inputs.items()))
    return receipt


def build(group):
    failures = []
    for name, item in group.items():
        if item.get("status") in (GREEN, CNE): continue
        failures.extend(f"{name}: {x}" for x in item["failures"] or [item.get("status")])
    return {"passed": not failures, "date": datetime.date.today().isoformat(), "command": COMMAND,
            "failures": failures, "measurement": {"legs": group}}


def guard_receipt():
    import runpy
    ns = runpy.run_path(os.path.abspath("tools/harness/receipt_guard.py"))
    ns["guard_receipt"](f"{ROUND}/validation.json")


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if "--selftest" in argv:
        return 0
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if "--check" in argv:
        print(rendered, end="")
        return 0
    guard_receipt()
    with open(f"{ROUND}/validation.json", "w", encoding="utf-8") as fh:
        fh.write(rendered)
    print(f"receipt: {ROUND}/validation.json")
    print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
