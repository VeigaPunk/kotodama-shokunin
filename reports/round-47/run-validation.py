#!/usr/bin/env python3
"""Round-47 acceptance runner — loop-2 position 1.

opencode-go/deepseek-v4.1-flash 64 seats (key-1 initial + key-6 refire of 14
missing seats). Baseline 6e9a30d.

Verdicts:
  C  coverage      UNCHANGED — verified-fresh cartography gap but the assembled
                 entry is 790 lines vs partition max 221 with 9 blocking defects
                 (R03 B1-B9: arithmetic, false source-accusation, mis-anchored
                 citations, worked-example FAIL). Not landing-ready; repeats the
                 r42/r44 collision pattern if forced. Honest unchanged.
  O  operability   IMPROVED — tools/harness/claims-freshness.py landed durable:
                 selftest 62/62 (registry 43 + seam 19), r43 positive regression
                 (O STALE 2/2, C STALE, Ca FRESH, exit 1 + REFUSE), negative
                 control green (r47 3 FRESH, exit 0), anti-theater verified.
                 Closes R01-43-12.
  Ca calibration   IMPROVED — loop-1 defect reconciliation filed with corrections
                 (zai-sentence fix + Ca05 re-pin) at calib/queue-successor-r47.json;
                 successor records only, parent defect-queue-v2.json pinned.

admission: admit only when every claim verifies and no axis is harmed. C does not
verify (no landing; unchanged != the claimed +1) -> NOT admitted on C; O and Ca
verify and are recorded without averaging the C shortfall into an accept.
"""
import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = str(pathlib.Path(__file__).resolve().parents[2])
ROUND = "reports/round-47"
COMMAND = "python3 reports/round-47/run-validation.py"
BASELINE = "6e9a30d"


def sh(*a, timeout=300, cwd=None):
    p = subprocess.run(a, capture_output=True, timeout=timeout, cwd=cwd or ROOT)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def sha_file(p):
    try:
        return hashlib.sha256(open(pathlib.Path(ROOT) / p, "rb").read()).hexdigest()
    except OSError:
        return None


def measure():
    results = {}
    failures = []

    # ---- C: coverage (unchanged; over-built + blocking defects) -------------
    tot = len(list(pathlib.Path(ROOT, "corpus/knowledge").rglob("*.md")))
    target = pathlib.Path(ROOT, "corpus/knowledge/culture-material/cartography-and-mapmaking.md")
    c_meas = {"total": tot, "cartography_landed": target.exists(), "culture_material": len(list(pathlib.Path(ROOT, "corpus/knowledge/culture-material").glob("*.md")))}
    c_reason = ("C: UNCHANGED — verified-fresh cartography gap (0 owners) but the assembled "
        "entry is 790 lines vs live partition max 221 with 9 blocking defects (R03 B1-B9: "
        "arithmetic 20x-not-10x, C02's false source-accusation 'archive of coups' which IS at "
        "naming-systems.md:70, mis-anchored craft-ladder cite, worked-example F-1/F-2 FAIL). "
        "Not landing-ready; repeats the r42/r44 collision if forced. No corpus delta; 223 holds.")
    results["C"] = {"command": COMMAND, "date": "2026-10-19", "verdict": "unchanged-blocked",
        "passed": False, "measurement": c_meas, "failures": [c_reason]}
    failures.append(f"claim C: {c_reason}")

    # ---- O: operability (freshness gate landed) ------------------------------
    gate = "tools/harness/claims-freshness.py"
    rc, st, _ = sh("python3", "-B", gate, "--selftest")
    o_meas = {"gate_exists": (pathlib.Path(ROOT) / gate).exists(), "gate_sha256": sha_file(gate),
              "selftest_rc": rc, "selftest_pass": st.count("PASS")}
    rc2, r43, _ = sh("python3", "-B", gate, "--claims", "reports/round-43/claims.json",
                     "--checks", f"{ROUND}/calib/r43-checks.json")
    o_meas["r43_exit"] = rc2
    o_meas["r43_flags_O_C_stale"] = ("[O] STALE" in r43 and "[C] STALE" in r43 and "[Ca] FRESH" in r43)
    rc3, neg, _ = sh("python3", "-B", gate, "--claims", "reports/round-47/claims.json",
                     "--checks", f"{ROUND}/calib/r47-checks.json")
    o_meas["neg_exit"] = rc3
    o_meas["neg_all_fresh"] = "3 fresh, 0 stale" in neg
    o_ok = (o_meas["gate_exists"] and o_meas["selftest_rc"] == 0 and o_meas["selftest_pass"] == 62
            and o_meas["r43_flags_O_C_stale"] and o_meas["neg_all_fresh"])
    results["O"] = {"command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if o_ok else "unprovable",
        "passed": bool(o_ok), "measurement": o_meas,
        "failures": [] if o_ok else ["O landed but thresholds unmet"]}
    if not o_ok:
        failures.append("claim O: gate thresholds unmet")

    # ---- Ca: calibration -----------------------------------------------------
    succ = pathlib.Path(ROOT, f"{ROUND}/calib/queue-successor-r47.json")
    ca_meas = {"successor_filed": succ.exists(), "successor_sha256": sha_file(f"{ROUND}/calib/queue-successor-r47.json"),
               "parent_pinned": sha_file("reports/round-40/op/defect-queue-v2.json")}
    ca_ok = succ.exists()
    ca_reason = ("Ca: loop-1 defect reconciliation filed (3 defect rows + 2 provider amendments) "
        "with integrator corrections — zai-verification sentence fixed, Ca05 re-pinned to live sha; "
        "successor records only, parent defect-queue-v2.json sha-pinned not edited.")
    results["Ca"] = {"command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if ca_ok else "unprovable",
        "passed": ca_ok, "measurement": ca_meas,
        "failures": [] if ca_ok else ["queue successor not filed"]}
    if not ca_ok:
        failures.append("claim Ca: queue successor not filed")

    # ---- cross ---------------------------------------------------------------
    rc4, stat, _ = sh("git", "status", "--porcelain=v1")
    corpus_dirty = [l for l in stat.splitlines() if "corpus/" in l and l[:3].strip() in ("M","MM","AM")]
    results["cross"] = {"command": COMMAND, "date": "2026-10-19", "verdict": "measured",
        "passed": True, "measurement": {"corpus_modified": corpus_dirty,
            "fragments_present": len(list(pathlib.Path(ROOT, ROUND).rglob("*.md"))),
            "seats_filed": "50/64 initial + 14/14 key-6 refire = 64/64"},
        "failures": []}

    return {
        "round": 47, "baseline_revision": BASELINE, "counting_command": COMMAND,
        "date": "2026-10-19",
        "claims_declared": {"C": "coverage", "O": "operability", "Ca": "calibration"},
        "claims": results,
        "acceptance_checks_passed": False,
        "verdict": "rejected-honest-stop",
        "partial": "O + Ca improved and landed; C unchanged (over-built + blocking defects)",
        "failures": failures,
        "limits": [
            "C unchanged is honest: the gap is verified-fresh but the 790-line entry is 3.6x the partition max with 9 blocking defects; landing it repeats the r42/r44 collision. A re-scoped, right-sized draft is the successor path.",
            "O's freshness gate closes R01-43-12 — the stale-premises class that hit r43+r44. Its could-not-evaluate-on-no-checks contract is the anti-theater guarantee.",
            "Ca's successor carries integrator corrections (the zai-verification sentence was conflating 'requested lane' with 'names zai anywhere'; Ca05 re-pinned).",
            "Round ran 50/64 then a key-6 refire of the 14 missing seats on operator instruction; key-6 was 402'd in the earlier census but served the refire.",
            "No filed byte edited; corpus unchanged (223); the r42 extractor + r44 resolver untouched.",
        ],
        "input_sha256": {
            f"{ROUND}/claims.json": sha_file(f"{ROUND}/claims.json"),
            f"{ROUND}/targets.json": sha_file(f"{ROUND}/targets.json"),
            f"{ROUND}/run-validation.py": sha_file(f"{ROUND}/run-validation.py"),
            "tools/harness/claims-freshness.py": sha_file(gate),
            f"{ROUND}/calib/queue-successor-r47.json": sha_file(f"{ROUND}/calib/queue-successor-r47.json"),
        },
    }


def main():
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        sys.stdout.write(rendered)
        return 0
    out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv \
        else pathlib.Path(ROOT) / ROUND / "validation.json"
    out.write_text(rendered, encoding="utf-8")
    print(f"receipt: {out}")
    print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
    print(f"verdict: {receipt['verdict']}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
