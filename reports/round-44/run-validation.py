#!/usr/bin/env python3
"""Round-44 acceptance runner.

Loop-1 position 12. Scheduled antigravity/gemini-3.8-flash; operator-redirected to
opencode-go/deepseek-v4.1-flash after the antigravity lane aborted twice with zero
seat output ('skip the gemini and argon rounds' — named deviation, not a declared
fallback). Baseline c9f4eaa. 14/32 seats filed; the rest failed on an opencode-go
reasoning_content API error.

Round outcome:
  O  operability   IMPROVED — the r43 O09 verified successor body landed byte-exact at
                 tools/harness/basename-couples-resolver.py (sha 43ce341f…): 27/27
                 selftest, four-class census 2556+166+0+7=2729 +1 glob, every fallback
                 mapping + unresolved reason listed, 0-diff parity with the r42 witness
                 (bytes d8d23a26… untouched). Fixes blank-line over-capture + adds the
                 ambiguous/indented-prose/glob-precedence controls.
  C  coverage      UNCHANGED — the only drafted gap candidate (dream) was already named
                 in r42 K02 R2 (same slug), violating the claim's 'not carried' clause;
                 the fresh gap (cartography) has no entry body. No landing; 223 stays.
  Ca calibration   UNPROVABLE-BETTER — the stale-premises defect (R01-43-12) is
                 confirmed and a scratch prototype correctly flags r43 O/C stale + Ca
                 fresh, but no durable gate and a red selftest; all three Ca seats
                 failed. Not delivered.

admission rule: admit only when every claim verifies and no axis is harmed. C does not
verify (unchanged is not the claimed +1) and Ca is unprovable -> the round is NOT
admitted on its declared claim set, reported honestly. O's improvement is real and
landed; the round records it without averaging the C/Ca shortfalls into an accept.
"""
import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = str(pathlib.Path(__file__).resolve().parents[2])
ROUND = "reports/round-44"
COMMAND = "python3 reports/round-44/run-validation.py"
BASELINE = "c9f4eaa"
RESOLVER_SHA = "43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64"
WITNESS_SHA = "d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1"


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

    # ---- O: operability -----------------------------------------------------
    res = "tools/harness/basename-couples-resolver.py"
    o_meas = {
        "landed": (pathlib.Path(ROOT) / res).exists(),
        "landed_sha256": sha_file(res),
        "landed_sha_matches_pin": sha_file(res) == RESOLVER_SHA,
        "witness_sha256": sha_file("tools/harness/couples-reference-extractor.py"),
        "witness_untouched": sha_file("tools/harness/couples-reference-extractor.py") == WITNESS_SHA,
        "census_artifact": sha_file(f"{ROUND}/calib/couples-census-r44.json"),
    }
    rc, out, _ = sh("python3", "-B", res, "--selftest")
    o_meas["selftest_rc"] = rc
    o_meas["selftest_pass"] = out.count("PASS")
    rc2, cen, _ = sh("python3", "-B", res, "--census")
    o_meas["census_rc"] = rc2
    o_meas["census_has_four_class"] = "direct=2556" in cen and "unresolved=7" in cen
    o_meas["census_conservation"] = "conservation: True" in cen
    o_meas["wrapped_4of4"] = "phonetics-phonology.md" in cen
    o_ok = (o_meas["landed"] and o_meas["landed_sha_matches_pin"]
            and o_meas["selftest_rc"] == 0 and o_meas["selftest_pass"] == 27
            and o_meas["census_has_four_class"] and o_meas["census_conservation"]
            and o_meas["witness_untouched"])
    results["O"] = {
        "command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if o_ok else "unprovable",
        "passed": bool(o_ok), "measurement": o_meas,
        "failures": [] if o_ok else ["O landed but did not meet its thresholds"],
    }
    if not o_ok:
        failures.append("claim O: landed but thresholds unmet")

    # ---- C: coverage --------------------------------------------------------
    tot = len(list(pathlib.Path(ROOT, "corpus/knowledge").rglob("*.md")))
    c_meas = {"total": tot, "landed_new": tot == 224}
    c_reason = (
        f"C: UNCHANGED — total {tot} (no landing). The only drafted gap candidate "
        "(dream/vision/trance) was already named at reports/round-42/scout/K02-myth-gaps.md:216 "
        "with the same slug, violating the claim's 'not carried from a prior round' clause "
        "(strict reading per R01-44-09); the fresh gap (cartography, K02) has no entry body. "
        "No corpus delta; coverage holds at 223.")
    results["C"] = {
        "command": COMMAND, "date": "2026-10-19",
        "verdict": "unchanged-blocked", "passed": False,
        "measurement": c_meas, "failures": [c_reason],
    }
    failures.append(f"claim C: {c_reason}")

    # ---- Ca: calibration ----------------------------------------------------
    gate = pathlib.Path(ROOT, "tools/harness/claims-freshness.py")
    ca_meas = {
        "durable_gate_exists": gate.exists(),
        "calib_dir_files": sorted(p.name for p in pathlib.Path(ROOT, f"{ROUND}/calib").glob("*")),
    }
    ca_reason = (
        "Ca: UNPROVABLE-BETTER — the R01-43-12 stale-premises defect is confirmed and a "
        "scratch prototype flags r43 O/C stale + Ca fresh (exit 2 + REFUSE), but no durable "
        "gate exists under tools/harness/ and the prototype selftest is red (17/19); all three "
        "Ca seats failed on the opencode-go reasoning_content error. Method proven, not delivered.")
    results["Ca"] = {
        "command": COMMAND, "date": "2026-10-19",
        "verdict": "unprovable-but-better", "passed": False,
        "measurement": ca_meas, "failures": [ca_reason],
    }
    failures.append(f"claim Ca: {ca_reason}")

    # ---- cross / honesty ----------------------------------------------------
    rc3, stat, _ = sh("git", "status", "--porcelain=v1")
    corpus_dirty = [l for l in stat.splitlines() if "corpus/" in l and "M" in l[:3]]
    results["cross"] = {
        "command": COMMAND, "date": "2026-10-19", "verdict": "measured", "passed": True,
        "measurement": {
            "corpus_modified_lines": corpus_dirty,
            "fragments_present": len(list(pathlib.Path(ROOT, ROUND).rglob("*.md"))),
            "failed_seats_opencode_reasoning_err": 18,
        },
        "failures": [],
    }

    return {
        "round": 44, "baseline_revision": BASELINE,
        "counting_command": COMMAND, "date": "2026-10-19",
        "claims_declared": {c["id"]: c["axis"] for c in claims["claims"]},
        "claims": results,
        # O verifies; C unchanged (not the claimed +1); Ca unprovable -> not admitted
        "acceptance_checks_passed": False,
        "verdict": "rejected-honest-stop",
        "partial": "operability improved and landed; coverage + calibration did not verify",
        "failures": failures,
        "limits": [
            "O is a real landed improvement (successor resolver + four-class census authority). It did not save the round's admission because C (the claimed +1) did not land and Ca did not verify.",
            "C unchanged is the honest outcome: dream was a carried topic (r42 R2); cartography is fresh but undrafted. The 'not carried' clause is recorded strict per R01-44-09.",
            "Ca unprovable-but-better: the freshness-gate method is proven by a scratch prototype but no durable gate exists; the defect (R01-43-12) stays open with owner integrator.",
            "18/32 seats failed on an opencode-go reasoning_content API error (provider defect, not a content failure); the O landing is verified independently of seat count.",
            "No filed byte edited; the r42 extractor demoted-by-record (bytes d8d23a26…); corpus unchanged (223).",
        ],
        "input_sha256": {
            f"{ROUND}/claims.json": sha_file(f"{ROUND}/claims.json"),
            f"{ROUND}/targets.json": sha_file(f"{ROUND}/targets.json"),
            f"{ROUND}/run-validation.py": sha_file(f"{ROUND}/run-validation.py"),
            "tools/harness/basename-couples-resolver.py": RESOLVER_SHA,
            "tools/harness/couples-reference-extractor.py": WITNESS_SHA,
            f"{ROUND}/calib/couples-census-r44.json": sha_file(f"{ROUND}/calib/couples-census-r44.json"),
        },
    }


def main():
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        sys.stdout.write(rendered)
        return 0
    out = None
    if "--out" in sys.argv:
        out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1])
    else:
        out = pathlib.Path(ROOT) / ROUND / "validation.json"
    out.write_text(rendered, encoding="utf-8")
    print(f"receipt: {out}")
    print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
    print(f"verdict: {receipt['verdict']}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
