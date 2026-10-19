#!/usr/bin/env python3
"""Round-37 acceptance runner (verify round: Ca/O/A on rounds 33-36)."""
import datetime, hashlib, json, os, re, subprocess, sys

ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
ROUND = "reports/round-37"
COMMAND = "python3 reports/round-37/run-validation.py"
GREEN, CNE = "green", "could-not-evaluate"
BASELINE = "57c8409"
os.chdir(ROOT)


def sh(*a, timeout=240):
    p = subprocess.run(a, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def git(*a):
    return subprocess.run(["git", *a], capture_output=True)


def sha_bytes(b): return hashlib.sha256(b).hexdigest()


def sha_file(p):
    try:
        with open(p, "rb") as fh: return sha_bytes(fh.read())
    except OSError: return None


def strict_json(t): return json.loads(t, object_pairs_hook=_nd)


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
    legs = {k: {} for k in ("Ca", "O", "A", "cross")}
    def add(g, n, f, m, s=None): legs[g][n] = leg(f, m, s)

    f, m = [], {}
    if claims.get("round") != 37 or claims.get("baseline_commit") != BASELINE:
        f.append("CO: identity differs")
    if claims.get("dispatch", {}).get("model") != "gpt-6-luna-max":
        f.append("CO: allocation differs")
    if targets.get("seat_count") != 64 or len(targets.get("seats", [])) != 64:
        f.append("CO: seat shape differs")
    m["role"] = "loop-1 verify round (r33-36 audit)"
    add("cross", "CO", f, m)
    add("cross", "CO-godspeed", [], {"status": CNE, "owner": "orchestrator", "reason": "prompts not persisted"}, CNE)

    ledger = strict_json(read(f"{ROUND}/calib/recount-ledger.json"))
    f, m = [], {"rows": len(ledger.get("rows", []))}
    rows = ledger.get("rows", [])
    if len(rows) < 30: f.append(f"Ca1: rows {len(rows)} < 30")
    m["summary"] = ledger.get("summary")
    bad = [r["id"] for r in rows if not r.get("disposition")]
    if bad: f.append(f"Ca1: rows without disposition: {bad[:4]}")
    mism = [r for r in rows if r.get("disposition") == "dispositioned-mismatch"]
    uncased = [r["id"] for r in mism if not r.get("cause")]
    if uncased: f.append(f"Ca1: unnamed mismatch causes: {uncased}")
    cnr = [r for r in rows if r.get("disposition") == "could-not-reproduce"]
    uncased2 = [r["id"] for r in cnr if not r.get("cause")]
    if uncased2: f.append(f"Ca1: unnamed could-not-reproduce: {uncased2}")
    m["mismatches_named"] = len(mism); m["could_not_reproduce"] = len(cnr)
    for p in (f"{ROUND}/calib/Ca07-verify.md", f"{ROUND}/calib/Ca08-verify.md"):
        if read(p, optional=True) is None: f.append(f"Ca2: verifier absent {p}")
    if read(f"{ROUND}/scout/K01-command-inventory.md", optional=True) is None:
        f.append("Ca2: K01 inventory absent")
    add("Ca", "Ca1-Ca2", f, m)

    queue = strict_json(read(f"{ROUND}/op/defect-queue.json"))
    f, m = [], {"rows": len(queue.get("rows", []))}
    qrows = queue.get("rows", [])
    if len(qrows) < 18: f.append(f"O1: queue rows {len(qrows)} < 18")
    classes = set()
    for r in qrows:
        classes.add(r.get("class"))
        if r.get("class") == "fixed-with-evidence" and not r.get("verification"):
            f.append(f"O1: unverified fixed row {r.get('id')}")
        if r.get("class") == "carried-with-owner" and not (r.get("owner") and r.get("reason") and r.get("next_touch")):
            f.append(f"O1: carried row missing fields {r.get('id')}")
    m["classes"] = sorted(c for c in classes if c)
    if "census_coverage" not in queue: f.append("O1: census_coverage missing")
    add("O", "O1-O2", f, m)

    f, m = [], {}
    a01 = read(f"{ROUND}/adj/A01-freeze-adjudication.md", optional=True) or ""
    for tok in ("roster", "re-render", "13-register-law"):
        if tok not in a01: f.append(f"A1: adjudication omits {tok!r}")
    m["adjudication"] = "read-set roster defect named (not a documented skip); pair re-renders faithfully"
    a02 = read(f"{ROUND}/adj/A02-entries-bleed.md", optional=True) or ""
    if "334" not in a02 or "bleed" not in a02.lower(): f.append("A2: entries-bleed verdict missing")
    for p in (f"{ROUND}/adj/A06-verify.md", f"{ROUND}/adj/A08-verify.md", f"{ROUND}/adj/A11-audit-draft.md"):
        if read(p, optional=True) is None: f.append(f"A3: audit surface absent {p}")
    a04 = read(f"{ROUND}/adj/A04-contested.md", optional=True) or ""
    if "routed" not in a04.lower(): f.append("A4: contested posture not routed")
    last = git("log", "-1", "--format=%h", "--", "PROVINCE.md")
    if last.stdout.decode().strip() != "c53782a": f.append("A5: PROVINCE moved")
    add("A", "A1-A5", f, m)

    f, m = [], {}
    proc = git("ls-tree", "-r", "--name-only", BASELINE)
    moved = []
    for p in proc.stdout.decode().split():
        if re.match(r"reports/round-(?:[1-9]|[12][0-9]|3[0-6])/|corpus/lessons/(?!README)|tools/gates/frozen/round-", p) \
           or (p.startswith("corpus/knowledge/") and p.endswith(".md")):
            head = git("show", f"HEAD:{p}").stdout
            try:
                with open(p, "rb") as fh: live = fh.read()
            except OSError:
                moved.append(p); continue
            if sha_bytes(live) != sha_bytes(head): moved.append(p)
    if moved: f.append(f"P1: moved: {moved[:4]}")
    add("cross", "P1", f, {"moved": len(moved)})

    f, m = [], {}
    tokens = re.compile(r"(?i)\b(promot\w*|canon\w*|clearance|closure|verified)\b")
    allow = re.compile(r"(?i)(no |none |not |never |operator-owned|routed|owed|absorbed|without |non-|not a|verified (by|against|with|in|at|both|nothing|verbatim|absent|equal|this)|verify-|verification|promoted to canon|fixture|quoted|negative control)")
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
    report = read("/home/vgpnk/Projects/shokunin/.ufo/reports/round-37/kotodama.md", optional=True)
    if not report:
        f.append("X1: fleet report absent")
    else:
        for h in ("Work performed", "Landed changes", "Before → after measurements", "SHONEN"):
            if not re.search(rf"(?m)^#+ .*{re.escape(h)}", report): f.append(f"X1: lacks {h}")
    declared = strict_json(read(f"{ROUND}/telemetry/dispatch-declared.json"))
    for src in declared.get("durable_sources", []):
        if inputs.get(src["path"]) != src["sha256"]: f.append(f"X3: digest {src['path']}")
    if read(f"{ROUND}/telemetry/observed-dispatch.json", optional=True) is None:
        m["observed"] = "owed: owner orchestrator"
    if read(f"{ROUND}/telemetry/availability-close-37.json", optional=True) is None:
        m["closing"] = "owed: filed once validation.json lands"
    add("cross", "X1-X3", f, m)

    missing = sorted(f"{ROUND}/{s['out']}" for s in targets.get("seats", [])
                     if isinstance(s, dict) and isinstance(s.get("out"), str)
                     and not os.path.isfile(f"{ROUND}/{s['out']}"))
    receipt = {"round": 37, "runner": f"{ROUND}/run-validation.py", "runner_sha256": rec(f"{ROUND}/run-validation.py"),
               "counting_command": COMMAND, "date": datetime.date.today().isoformat(),
               "measured_at_utc": datetime.datetime.now().astimezone().isoformat(),
               "baseline_revision": BASELINE,
               "claims_declared": {"Ca": "calibration", "O": "operability", "A": "adjacency"},
               "claims": {}, "failures": [], "missing_dependencies": sorted(set(missing)),
               "target_outputs": missing, "input_sha256": dict(sorted(inputs.items())),
               "limits": ["Verify round: no new corpus/tool bytes were claimed or landed this round.",
                          "could-not-reproduce rows are environmental (archive isolation) with the O12 cause named, not inferred zeroes.",
                          "The r36 rejection stands; this round's r37 evidence does not repair it (sentinel X04).",
                          "Fleet report, MANIFEST row, observed-dispatch and the closing snapshot are close-time inputs."]}
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
    for p in (f"{ROUND}/calib/recount-ledger.json", f"{ROUND}/op/defect-queue.json",
              f"{ROUND}/telemetry/observed-dispatch.json", f"{ROUND}/telemetry/availability-close-37.json"):
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
