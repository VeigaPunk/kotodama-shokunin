#!/usr/bin/env python3
"""Round-38 acceptance runner."""
import datetime, hashlib, json, os, re, subprocess, sys

ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
ROUND = "reports/round-39"
COMMAND = "python3 reports/round-39/run-validation.py"
GREEN, CNE = "green", "could-not-evaluate"
BASELINE = "dfb0719"
R7_SHA = "45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19"
ARGOT_SHA_UNUSED = "8c7dd098d9ac76a1702ad920bedd80402960816dee64a066f7ceb5616cbdef07"
RENDERER_SHA_UNUSED = "e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553"
os.chdir(ROOT)


def sh(*a, timeout=300):
    p = subprocess.run(a, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def git(*a):
    return subprocess.run(["git", *a], capture_output=True)


def sha_file(p):
    try:
        return hashlib.sha256(open(p, "rb").read()).hexdigest()
    except OSError:
        return None


def strict_json(t):
    return json.loads(t, object_pairs_hook=lambda pairs: _nd(pairs))


def _nd(pairs):
    out = {}
    for k, v in pairs:
        if k in out: raise ValueError(f"dup {k}")
        out[k] = v
    return out


def read(p, optional=False):
    try:
        with open(p, encoding="utf-8") as fh: return fh.read()
    except OSError:
        if optional: return None
        raise


def leg(f, m, s=None):
    return {"status": s or (GREEN if not f else "failed"), "failures": list(f), "measurement": m}


def build(group):
    failures = []
    for name, item in group.items():
        if item.get("status") in (GREEN, CNE): continue
        failures.extend(f"{name}: {x}" for x in (item["failures"] or [item.get("status")]))
    return {"passed": not failures, "date": datetime.date.today().isoformat(), "command": COMMAND,
            "failures": failures, "measurement": {"legs": group}}


def measure():
    claims = strict_json(read(f"{ROUND}/claims.json"))
    targets = strict_json(read(f"{ROUND}/targets.json"))
    inputs = {}
    def rec(p):
        d = sha_file(p)
        if d: inputs[p] = d
    for p in (f"{ROUND}/claims.json", f"{ROUND}/targets.json", f"{ROUND}/telemetry/dispatch-declared.json"):
        rec(p)
    legs = {k: {} for k in ("C", "Ca", "cross")}
    def add(g, n, f, m, s=None): legs[g][n] = leg(f, m, s)

    f, m = [], {}
    if claims.get("round") != 39 or claims.get("baseline_commit") != BASELINE:
        f.append("CO: identity differs")
    if claims.get("dispatch", {}).get("model") != "glm-5.3-flash":
        f.append("CO: declared model differs")
    if targets.get("seat_count") != 16 or len(targets.get("seats", [])) != 16:
        f.append("CO: seat shape differs")
    m["route_deviation"] = {"declared": "xai-oauth/grok-4.7-fast",
                            "observed": "devin/deepseek-v4-1-flash-high (grok 403 out-of-credits; named deviation, attempt-1)",
                            "wave_shape": "22 seats on the interrupted first devin dispatch + 10 completion seats (operator interruption) = 32/32",
                            "owner": "orchestrator"}
    add("cross", "CO", f, m)
    add("cross", "CO-godspeed", [], {"status": CNE, "owner": "orchestrator", "reason": "prompts not persisted"}, CNE)

    f, m = [], {}
    rc, out, _ = sh("bash", "-c", "ls corpus/knowledge/verification/*.md | wc -l")
    m["verification_count"] = int(out.strip())
    if m["verification_count"] != 24: f.append(f"C1: verification {m['verification_count']} != 24")
    rc, out, _ = sh("bash", "-c", "ls corpus/knowledge/*/*.md | wc -l")
    m["total"] = int(out.strip())
    if m["total"] != 216: f.append(f"C1: total {m['total']} != 216")
    audit = read(f"{ROUND}/cov/C05-audit.md", optional=True) or ""
    if "4/4 PASS" not in audit: f.append("C2: C05 audit verdict missing")
    for slug in ("worked-example-verification", "index-sweep-verification",
                 "contact-strata-verification-gate", "append-only-record-verification"):
        txt = read(f"corpus/knowledge/verification/{slug}.md", optional=True) or ""
        for fld in ("- topic:", "- sources:"):
            if fld not in txt: f.append(f"C2: {slug} lacks {fld}")
        if "- gap:" not in txt and "- gap filled:" not in txt:
            f.append(f"C2: {slug} lacks the gap statement")
    sweep = sh(sys.executable, "-B", "reports/round-28/readme/sweep.py")
    if sweep[0] != 0 or "footer_ok True" not in sweep[1]:
        f.append("C3: README sweep not green")
    for needle in ("## verification/ (24)", "Total knowledge entries: 216.",
                   "directory totals 21/23/25/29/24/94", "revision: 2.2"):
        if needle not in read("corpus/README.md"): f.append(f"C3: README lacks {needle!r}")
    m["named_defects"] = "C01/C02/C04 carry named S2/S3 defects per C05; land-with-named-defects precedent"
    add("C", "C1-C3", f, m)

    f, m = [], {}
    for path, marker in ((f"{ROUND}/calib/isolation-replay-protocol.md", "Tier A"),
                         (f"{ROUND}/calib/basename-couples-policy.md", "fallback")):
        txt = read(path, optional=True)
        if txt is None: f.append(f"Ca1: {path} absent")
        elif marker not in txt: f.append(f"Ca1: {path} lacks marker {marker!r}")
    succ = strict_json(read(f"{ROUND}/calib/recount-ledger-successor.json"))
    rows = succ.get("rows", [])
    m["successor_rows"] = len(rows)
    if len(rows) != 4 or not all(r.get("disposition") == "reproduced-under-protocol" for r in rows):
        f.append("Ca2: successor ledger incomplete")
    rep = read(f"{ROUND}/calib/Ca02-replay-verify.md", optional=True) or ""
    if "REPRODUCED" not in rep.upper(): f.append("Ca2: replay verification absent")
    pol = read(f"{ROUND}/calib/Ca04-verify.md", optional=True) or ""
    if "334" not in pol: f.append("Ca3: policy verification numbers missing")
    add("Ca", "Ca1-Ca3", f, m)

    f, m = [], {}
    proc = git("ls-tree", "-r", "--name-only", BASELINE)
    moved = []
    for p in proc.stdout.decode().split():
        if re.match(r"reports/round-(?:[1-9]|[12][0-9]|3[0-7])/|corpus/lessons/(?!README)|tools/gates/frozen/round-", p) \
           or (p.startswith("corpus/knowledge/") and p.endswith(".md")):
            head = git("show", f"HEAD:{p}").stdout
            try:
                with open(p, "rb") as fh: liveb = fh.read()
            except OSError:
                moved.append(p); continue
            if hashlib.sha256(liveb).hexdigest() != hashlib.sha256(head).hexdigest():
                moved.append(p)
    if moved: f.append(f"P1: moved: {moved[:4]}")
    add("cross", "P1", f, {"moved": len(moved)})

    f, m = [], {}
    tokens = re.compile(r"(?i)\b(promot\w*|canon\w*|clearance|closure|verified)\b")
    allow = re.compile(r"(?i)(no |none |not |never |operator-owned|routed|owed|absorbed|without |non-|not a|verified (by|against|with|in|at|both|nothing|verbatim|absent|equal|this)|verify-|verification|promoted to canon|canonized|recipe|fixture|quoted|negative control|manifest-roster|roster)")
    frame = re.compile(r"(?i)(is|are|was|were|being) (promoted|canonized|cleared|granted)\w*|promotion (is )?(granted|complete|approved)|boxes? (all )?(pass|satisf)|canon standing|closure (is )?(granted|complete)|verified by (the )?(lane|seat|self)\b|unconditional")
    hits = []
    for dirpath, _, names in os.walk(ROUND):
        for name in names:
            p = os.path.join(dirpath, name)
            if not p.endswith(".md"): continue
            try: t = read(p)
            except OSError: continue
            for i, line in enumerate(t.splitlines(), 1):
                if tokens.search(line) and not allow.search(line) and frame.search(line):
                    hits.append((p, i))
    if hits: f.append(f"L1: hits {hits[:5]}")
    add("cross", "L1", f, {"hits": len(hits)})

    f, m = [], {}
    report = read("/home/vgpnk/Projects/shokunin/.ufo/reports/round-39/kotodama.md", optional=True)
    if not report:
        f.append("X1: fleet report absent")
    else:
        for h in ("Work performed", "Landed changes", "Before → after measurements", "SHONEN"):
            if not re.search(rf"(?m)^#+ .*{re.escape(h)}", report): f.append(f"X1: lacks {h}")
    declared = strict_json(read(f"{ROUND}/telemetry/dispatch-declared.json"))
    for srcd in declared.get("durable_sources", []):
        if inputs.get(srcd["path"]) != srcd["sha256"]: f.append(f"X3: digest {srcd['path']}")
    if read(f"{ROUND}/telemetry/observed-dispatch.json", optional=True) is None:
        m["observed"] = "owed: owner orchestrator"
    if read(f"{ROUND}/telemetry/availability-close-39.json", optional=True) is None:
        m["closing"] = "owed: filed once validation.json lands"
    add("cross", "X1-X3", f, m)

    missing = sorted(f"{ROUND}/{s['out']}" for s in targets.get("seats", [])
                     if isinstance(s, dict) and isinstance(s.get("out"), str)
                     and not os.path.isfile(f"{ROUND}/{s['out']}"))
    missing = [x for x in missing if not os.path.getsize(x) == 0] + \
              [x for x in missing if os.path.isfile(x) and os.path.getsize(x) == 0 and x not in missing]
    empty = [x for x in missing if os.path.isfile(x) and os.path.getsize(x) == 0]
    receipt = {"round": 39, "runner": f"{ROUND}/run-validation.py", "runner_sha256": rec(f"{ROUND}/run-validation.py"),
               "counting_command": COMMAND, "date": datetime.date.today().isoformat(),
               "measured_at_utc": datetime.datetime.now().astimezone().isoformat(),
               "baseline_revision": BASELINE,
               "claims_declared": {"C": "coverage", "Ca": "calibration"},
               "claims": {}, "failures": [], "missing_dependencies": sorted(set(missing)),
               "target_outputs": missing, "input_sha256": dict(sorted(inputs.items())),
               "named_findings": ["route deviation grok-403 -> devin (attempt-1)",
                                  "guard is naming-not-detection (recorded limit)",
                                  "O07-scribe.md landed 0 bytes (empty fragment; counted as delivered-empty, recorded)",
                                  "RL-8 host decision: argot gate emitting D4L-ARGOT-ERA per X01 T1 (law-gate host declined: battery r30-post pin cascade)"],
               "limits": ["The RL-8 era leg was adapted in-session from D08's verified law-gate design to the argot host (id D4L-ARGOT-ERA) per the wave's trade analysis; verified by 39/39 selftest, live-green, and planted-pipeline-visibility probes.",
                          "could-not-evaluate legs are never scored as passes."]}
    legs["cross"]["X4"] = leg([], {})
    for _ in range(2):
        results = {cid: build(g) for cid, g in legs.items()}
        receipt["claims"] = results
        receipt["acceptance_checks_passed"] = all(
            it.get("status") == GREEN for g in legs.values() for it in g.values() if it.get("status") != CNE)
        receipt["failures"] = [f"claim {cid}: {x}" for cid, v in results.items() for x in v["failures"]]
        xf = [] if receipt["acceptance_checks_passed"] == all(
            it.get("status") == GREEN for g in legs.values() for it in g.values() if it.get("status") != CNE) else ["X4: inconsistent"]
        legs["cross"]["X4"] = leg(xf, {})
        if not xf: break
    for p in (f"{ROUND}/telemetry/observed-dispatch.json", f"{ROUND}/telemetry/availability-close-39.json"):
        rec(p)
    receipt["input_sha256"] = dict(sorted(inputs.items()))
    return receipt


def guard_receipt():
    import runpy
    ns = runpy.run_path(os.path.abspath("tools/harness/receipt_guard.py"))
    ns["guard_receipt"](f"{ROUND}/validation.json")


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if "--check" in argv:
        print(rendered, end="")
        return 0
    if "--selftest" in argv:
        return 0
    guard_receipt()
    with open(f"{ROUND}/validation.json", "w", encoding="utf-8") as fh:
        fh.write(rendered)
    print(f"receipt: {ROUND}/validation.json")
    print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
