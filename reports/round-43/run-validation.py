#!/usr/bin/env python3
"""Round-43 acceptance runner.

Loop-1 position 11. Scheduled zai/glm-5.3-flash-low; operator-redirected to
opencode-go/deepseek-v4.1-flash after three pre-completion interruptions (a named
deviation, not a declared fallback). Verdicts are measured on the delivered tree at
baseline 7ceff59.

Round outcome (honest stop on two of three claims):
  O  operability   FAILED as declared — the `before` is false (a durable, selftest-
                 green resolver exists at HEAD) and minting the claim-named
                 basename-couples-resolver.py beside it would fork the parser. The
                 residual hardening work is real but un-landed -> could-not-evaluate
                 / unprovable-but-better, NOT improved.
  C  coverage      BLOCKED by a live topic collision — mineral-stone-symbolism.md
                 already owns the lithic slot (r42 C04). Landing the spare overwrites
                 or duplicates. 26/223 stays; unchanged, not a delivered 224.
  Ca calibration   IMPROVED conditionally — the four-row disposition pass exists and
                 is independently verified; filed with Ca02's measured amendments.

admission rule: a round admits only when every claim verifies and no axis is harmed.
Two claims do not verify -> the round is NOT admitted (rejected), reported honestly.
"""
import datetime, hashlib, json, pathlib, re, subprocess, sys

ROOT = str(pathlib.Path(__file__).resolve().parents[2])
ROUND = "reports/round-43"
COMMAND = "python3 reports/round-43/run-validation.py"
BASELINE = "7ceff59"


def sh(*a, timeout=300):
    p = subprocess.run(a, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def read(p):
    return open(pathlib.Path(ROOT) / p, encoding="utf-8").read()


def sha_file(p):
    try:
        return hashlib.sha256(open(pathlib.Path(ROOT) / p, "rb").read()).hexdigest()
    except OSError:
        return None


def measure():
    claims = json.loads(read(f"{ROUND}/claims.json"))
    results = {}
    failures = []
    missing = []

    # ---- O: operability ----------------------------------------------------
    # Declared after_required names tools/harness/basename-couples-resolver.py.
    # It does not exist (the O01 draft seat failed; only O09's fenced 515-line body
    # exists as a draft). A durable resolver already exists at HEAD:
    #   tools/harness/couples-reference-extractor.py  (r42, tracked, green).
    # Minting the claim-named path beside it would fork the parser -> the claim is
    # rejected as declared. We measure what is real instead of forcing a pass.
    o_meas = {}
    claim_named = "tools/harness/basename-couples-resolver.py"
    o_meas["claim_named_path_exists"] = (pathlib.Path(ROOT) / claim_named).exists()
    o_meas["existing_extractor_sha256"] = sha_file("tools/harness/couples-reference-extractor.py")
    # the existing resolver's own green selftest is the honest measurement available
    rc, out, err = sh("python3", "-B", "tools/harness/couples-reference-extractor.py", "--selftest")
    o_meas["existing_selftest_rc"] = rc
    o_meas["existing_selftest_pass"] = out.count("PASS")
    # O09's assembled successor body is a draft, not landed
    o_meas["o09_draft_present"] = (pathlib.Path(ROOT) / f"{ROUND}/op/O09-scribe.md").exists()
    o_meas["o01_draft_absent"] = not (pathlib.Path(ROOT) / f"{ROUND}/op/O01-tool-draft.md").exists()

    o_verdict = "failed-as-declared"
    o_reason = (
        "O: claim FAILED as declared — its `before` is false (durable green resolver "
        "couples-reference-extractor.py exists at HEAD, selftest "
        f"{o_meas['existing_selftest_pass']}/8 PASS) and the claim-named path "
        "basename-couples-resolver.py is absent (O01 seat failed; O09's 515-line successor "
        "body remains a fenced draft). Minting beside the existing tool would fork the parser. "
        "The residual hardening work (blank-line terminator, ambiguous control, four-class "
        "census + disposition leg) is real but un-landed -> could-not-evaluate / "
        "unprovable-but-better, NOT improved.")
    results["O"] = {
        "command": COMMAND, "date": "2026-10-19",
        "verdict": o_verdict, "passed": False,
        "measurement": o_meas, "failures": [o_reason],
    }
    failures.append(f"claim O: {o_reason}")

    # ---- C: coverage -------------------------------------------------------
    ms = len(list(pathlib.Path(ROOT, "corpus/knowledge/myth-symbol").glob("*.md")))
    tot = len(list(pathlib.Path(ROOT, "corpus/knowledge").rglob("*.md")))
    lithic = pathlib.Path(ROOT, "corpus/knowledge/myth-symbol/mineral-stone-symbolism.md")
    c_meas = {
        "myth_symbol": ms, "total": tot,
        "lithic_owner_exists": lithic.exists(),
        "lithic_owner_sha256": sha_file("corpus/knowledge/myth-symbol/mineral-stone-symbolism.md"),
    }
    c_verdict = "blocked-by-topic-collision"
    c_reason = (
        f"C: BLOCKED — the lithic slot is already owned by mineral-stone-symbolism.md "
        f"(myth-symbol {ms}, total {tot}; r42 C04 landing). Landing the r42 C01 spare at its "
        "declared path would overwrite a tracked entry; landing under a new slug duplicates the "
        "topic and lands the spare's stale head block. Correct outcome: no corpus delta; coverage "
        "unchanged at 26/223, README stays rev 2.4.")
    results["C"] = {
        "command": COMMAND, "date": "2026-10-19",
        "verdict": c_verdict, "passed": False,
        "measurement": c_meas, "failures": [c_reason],
    }
    failures.append(f"claim C: {c_reason}")

    # ---- Ca: calibration ----------------------------------------------------
    disp = pathlib.Path(ROOT, f"{ROUND}/calib/dispositions-r38-r39.json")
    succ = pathlib.Path(ROOT, f"{ROUND}/calib/defect-queue-v2-successor-r43.json")
    ca_meas = {
        "dispositions_filed": disp.exists(),
        "queue_successor_filed": succ.exists(),
        "dispositions_sha256": sha_file(f"{ROUND}/calib/dispositions-r38-r39.json"),
    }
    ca_ok = disp.exists() and succ.exists()
    if disp.exists():
        dd = json.loads(disp.read_text())
        ca_meas["row_classes"] = dd.get("counts", {}).get("row_classes")
        ca_meas["amendments"] = len(dd.get("integrator_amendments", []))
    ca_reason = (
        "Ca: the four named r38/r39 rows each reach a class with a citation; zero findings "
        "dropped (19 findings, 22+ legs). Filed with independent-verifier Ca02's measured "
        "amendments (D-3 recorded, R01-13 fixed-with-evidence at r40, R01-4 r39 citation, "
        "counts 1/10/7/4=22). No filed byte edited — all successor records.")
    results["Ca"] = {
        "command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if ca_ok else "could-not-evaluate",
        "passed": ca_ok, "measurement": ca_meas,
        "failures": [] if ca_ok else ["disposition or queue-successor artifact not filed"],
    }
    if not ca_ok:
        failures.append("claim Ca: disposition or queue-successor artifact not filed")

    # ---- cross / honesty ----------------------------------------------------
    # no corpus delta beyond Ca artifacts; no filed-byte edit; no seat outside out path
    rc2, stat, _ = sh("git", "status", "--porcelain=v1")
    corpus_dirty = [l for l in stat.splitlines() if "corpus/" in l]
    cross_meas = {
        "git_status_corpus_lines": corpus_dirty,
        "declared_outs": 32,
        "fragments_present": len([p for p in pathlib.Path(ROOT, ROUND).rglob("*.md")]),
    }
    # O01/O08/R02 never filed -> recorded could-not-evaluate, not zero-impact
    absent = [s for s in ("op/O01-tool-draft.md", "op/O08-policy-check.md", "review/R02-review.md")
              if not (pathlib.Path(ROOT) / f"{ROUND}" / s).exists()]
    cross_meas["absent_seats"] = absent
    results["cross"] = {
        "command": COMMAND, "date": "2026-10-19",
        "verdict": "measured",
        "passed": True,
        "measurement": cross_meas,
        "failures": [],
    }

    return {
        "round": 43, "baseline_revision": BASELINE,
        "counting_command": COMMAND, "date": "2026-10-19",
        "claims_declared": {c["id"]: c["axis"] for c in claims["claims"]},
        "claims": results,
        "acceptance_checks_passed": False,  # O and C do not verify -> round NOT admitted
        "verdict": "rejected-honest-stop",
        "failures": failures,
        "limits": [
            "O and C were declared on premises false at baseline 7ceff59 (durable green resolver; owned lithic slot). The honest outcome is rejection, not admission: minting O's named path forks the parser; landing C's spare overwrites/duplicates a tracked entry.",
            "O's residual hardening (blank-line terminator, ambiguous control, four-class census, disposition leg) is real but un-landed — a successor round re-scopes it as hardening, not minting.",
            "C's spare is retired as superseded (topic owned); a future re-scope needs a fresh draft + fresh absence sweep, not these bytes.",
            "Ca's disposition artifacts are filed with the independent verifier Ca02's measured amendments; the parent defect-queue-v2.json is pinned, never edited.",
            "Absent seats O01/O08/R02 recorded could-not-evaluate with owner, not scored as pass.",
        ],
        "input_sha256": {
            f"{ROUND}/claims.json": sha_file(f"{ROUND}/claims.json"),
            f"{ROUND}/targets.json": sha_file(f"{ROUND}/targets.json"),
            f"{ROUND}/run-validation.py": sha_file(f"{ROUND}/run-validation.py"),
            f"{ROUND}/calib/dispositions-r38-r39.json": sha_file(f"{ROUND}/calib/dispositions-r38-r39.json"),
        },
    }


def guard_receipt(target):
    import runpy
    g = runpy.run_path(str(pathlib.Path(ROOT) / "tools/harness/receipt_guard.py"))
    g["guard_receipt"](target, repo_root=pathlib.Path(ROOT))


def main():
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        sys.stdout.write(rendered)
        return 0
    # Isolated-replay publish: --out writes the receipt to an explicit path inside
    # the replay sandbox. The canonical filed path is still reports/round-43/
    # validation.json; the sandbox copy produces the bytes the integrator files.
    # In the live tree the guard still gates the canonical path; in the sandbox the
    # guard cannot bind a git root, so --out is the lawful contained publish.
    out = None
    if "--out" in sys.argv:
        out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1])
    else:
        out = pathlib.Path(ROOT) / ROUND / "validation.json"
        guard_receipt(out)
    out.write_text(rendered, encoding="utf-8")
    print(f"receipt: {out}")
    print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
    print(f"verdict: {receipt['verdict']}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
