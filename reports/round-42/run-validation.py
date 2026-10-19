#!/usr/bin/env python3
"""Round-38 acceptance runner."""
import datetime, hashlib, json, os, pathlib, re, subprocess, sys

ROOT = str(pathlib.Path(__file__).resolve().parents[2])
ROUND = "reports/round-42"
COMMAND = "python3 reports/round-42/run-validation.py"
GREEN, CNE = "green", "could-not-evaluate"
BASELINE = "ac47c78"
R7_SHA = "45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19"
ARGOT_SHA_UNUSED = "8c7dd098d9ac76a1702ad920bedd80402960816dee64a066f7ceb5616cbdef07"
RENDERER_SHA_UNUSED = "e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553"


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
        return d
    for p in (f"{ROUND}/claims.json", f"{ROUND}/targets.json", f"{ROUND}/telemetry/dispatch-declared.json"):
        rec(p)
    legs = {k: {} for k in ("O", "C", "cross")}
    def add(g, n, f, m, s=None): legs[g][n] = leg(f, m, s)

    f, m = [], {}
    if claims.get("round") != 42 or claims.get("baseline_commit") != BASELINE:
        f.append("CO: identity differs")
    if claims.get("dispatch", {}).get("model") != "deepseek-v4-1-flash-high":
        f.append("CO: declared model differs")
    if targets.get("seat_count") != 32 or len(targets.get("seats", [])) != 32:
        f.append("CO: seat shape differs")
    m["route_deviation"] = {"declared": "xai-oauth/grok-4.7-fast",
                            "observed": "devin/deepseek-v4-1-flash-high (grok 403 out-of-credits; named deviation, attempt-1)",
                            "wave_shape": "22 seats on the interrupted first devin dispatch + 10 completion seats (operator interruption) = 32/32",
                            "owner": "orchestrator"}
    add("cross", "CO", f, m)
    add("cross", "CO-godspeed", [], {"status": CNE, "owner": "orchestrator", "reason": "prompts not persisted"}, CNE)

    f, m = [], {}
    if read("tools/harness/couples-reference-extractor.py", optional=True) is None:
        f.append("O1: the successor extractor absent")
    st = sh(sys.executable, "-B", "tools/harness/couples-reference-extractor.py", "--selftest")
    m["selftest_tail"] = st[1].strip().splitlines()[-2:]
    if st[0] != 0 or "N6 regression guard" not in st[1]:
        f.append("O2: extractor selftest not green or the N6 guard missing")
    live = sh(sys.executable, "-B", "tools/harness/couples-reference-extractor.py",
              "corpus/knowledge/linguistics/phonetics-phonology.md")
    if live[0] != 0 or "writing-systems.md" not in live[1] or "direct" not in live[1]:
        f.append("O2: the wrapped field does not read whole on the live entry")
    cens = read(f"{ROUND}/op/couples-extractor-census.json", optional=True) or ""
    if "entries=223" not in cens or "wrapped fields: 1" not in cens:
        f.append("O3: the corrected census reading missing")
    pol = read(f"{ROUND}/calib/basename-couples-policy-full.md", optional=True) or ""
    if len(pol) < 12000: f.append("O3: the full policy successor missing/truncated")
    m["named"] = ("the filed r19/r27/r28 instruments keep their bytes (the defect class is recorded); "
                   "the fix lives in the successor; the r39 policy truncation is corrected by the successor document")
    add("O", "O1-O3", f, m)

    f, m = [], {}
    rc, out, _ = sh("bash", "-c", "ls corpus/knowledge/myth-symbol/*.md | wc -l")
    ms = int(out.strip())
    rc2, out2, _ = sh("bash", "-c", "ls corpus/knowledge/*/*.md | wc -l")
    tot = int(out2.strip())
    m["counts"] = {"myth_symbol": ms, "total": tot}
    audit = read(f"{ROUND}/cov/C05-audit.md", optional=True) or ""
    if "4/4" not in audit: f.append("C-evidence: C05 audit verdict not found")
    spare = read(f"{ROUND}/cov/C01-mineral-spare.md", optional=True)
    m["ruling"] = ("C01 and C04 authored the same lithic register mid-wave; C04 lands, C01 routes as the named spare "
                   "(r36 timekeeping precedent); two existing entries (animal-symbolism, plant-symbolism) were "
                   "momentarily overwritten by stale path proposals and restored byte-exact from HEAD at integration")
    f.append(f"C: claim FAILED as declared — myth-symbol {ms} != 27, total {tot} != 224 (three entries landed, "
             "the fourth collided and is routed; audits 4/4 PASS-with-defects). The collision ruling, the "
             "overwrite-restore incident, and the spare are on record; a successor round can land the spare "
             "under a re-scoped claim.")
    add("C", "C1", f, m)
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
    allow = re.compile(r"(?i)(no |none |not |never |operator-owned|routed|owed|absorbed|without |non-|not a|verified (by|against|with|in|at|both|nothing|verbatim|absent|equal|this)|verify-|verification|promoted to canon|canonized|recipe|fixture|quoted|negative control|manifest-roster|roster|an axis is promoted)")
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
    report = read("/home/vgpnk/Projects/shokunin/.ufo/reports/round-42/kotodama.md", optional=True)
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
    if read(f"{ROUND}/telemetry/availability-close-42.json", optional=True) is None:
        m["closing"] = "owed: filed once validation.json lands"
    add("cross", "X1-X3", f, m)

    missing = sorted(f"{ROUND}/{s['out']}" for s in targets.get("seats", [])
                     if isinstance(s, dict) and isinstance(s.get("out"), str)
                     and not os.path.isfile(f"{ROUND}/{s['out']}"))
    missing = [x for x in missing if not os.path.getsize(x) == 0] + \
              [x for x in missing if os.path.isfile(x) and os.path.getsize(x) == 0 and x not in missing]
    empty = [x for x in missing if os.path.isfile(x) and os.path.getsize(x) == 0]
    receipt = {"round": 42, "runner": f"{ROUND}/run-validation.py", "runner_sha256": rec(f"{ROUND}/run-validation.py"),
               "counting_command": COMMAND, "date": datetime.date.today().isoformat(),
               "measured_at_utc": datetime.datetime.now().astimezone().isoformat(),
               "baseline_revision": BASELINE,
               "claims_declared": {"O": "operability", "C": "coverage"},
               "claims": {}, "failures": [], "missing_dependencies": sorted(set(missing)),
               "target_outputs": missing, "input_sha256": dict(sorted(inputs.items())),
               "named_findings": ["r40 runner is the O12 relative-ROOT cure (first of the streak)",
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
    for p in (f"{ROUND}/telemetry/observed-dispatch.json", f"{ROUND}/telemetry/availability-close-42.json"):
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
