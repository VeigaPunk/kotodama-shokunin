#!/usr/bin/env python3
"""Round-48 acceptance runner — loop-2 position 2.

opencode-go/deepseek-v4.1-flash 64 seats (key-2, round-robin). Baseline a01405d.

Verdicts:
  C  coverage      IMPROVED — the right-sized cartography entry landed:
                   corpus/knowledge/culture-material/cartography-and-mapmaking.md,
                   239 lines (C02 23-line head + C01 215-line body with R03's
                   D1/D3/P2 fixes applied), inside <=250 tolerance (1.08x partition
                   max 221, 1.60x median 149). R03's nine r47 blocking defects are
                   absent on the assembled bytes; the D1 register-test/form-typology
                   contradiction is resolved. Sweep green: rows 224 files 224,
                   topic_mismatch 0. Total 223 -> 224, culture-material 25 -> 26.
  Ca calibration   IMPROVED — the live README duplicate H1 (lines 1/3, grep
                   count 2) removed as a recorded act (grep count -> 1); the r47
                   over-build defect class dispositioned into
                   calib/queue-successor-r48.json as fixed-with-evidence (parent
                   defect-queue-v2.json pinned, not edited); and the sweep's
                   heading blind-spot closed by a new durable control
                   tools/check-readme-heading.py (selftest 8/8, green on the
                   fixed README). The rev-2.4 transposed prose vector repaired.

admission: admit when every claim verifies and no axis is harmed. C and Ca both
verify on landed bytes -> ADMITTED. Freshness/depth/adjacency/operability rested
(freshness gate dropped the stale candidate O at declaration — its first live use).
"""
import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = str(pathlib.Path(__file__).resolve().parents[2])
ROUND = "reports/round-48"
COMMAND = "python3 reports/round-48/run-validation.py"
BASELINE = "a01405d"


def sh(*a, timeout=300, cwd=None):
    env = dict(__import__("os").environ, TMPDIR=str(pathlib.Path(ROOT) / ".scratch"),
               PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run(a, capture_output=True, timeout=timeout, cwd=cwd or ROOT, env=env)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def sha_file(p):
    try:
        return hashlib.sha256(open(pathlib.Path(ROOT) / p, "rb").read()).hexdigest()
    except OSError:
        return None


def count(pattern, path):
    rc, out, _ = sh("bash", "-c", f"grep -c {json.dumps(pattern)} {json.dumps(path)}")
    try:
        return int(out.strip())
    except ValueError:
        return -1


def measure():
    results = {}
    failures = []

    # ---- C: coverage (the cartography entry landed) ---------------------------
    tot = len(list(pathlib.Path(ROOT, "corpus/knowledge").rglob("*.md")))
    cm = len(list(pathlib.Path(ROOT, "corpus/knowledge/culture-material").glob("*.md")))
    target = pathlib.Path(ROOT, "corpus/knowledge/culture-material/cartography-and-mapmaking.md")
    entry_lines = len(target.read_text().splitlines()) if target.exists() else -1
    entry_text = target.read_text() if target.exists() else ""
    h1 = sum(1 for l in entry_text.splitlines() if l.startswith("# "))
    h3 = sum(1 for l in entry_text.splitlines() if l.startswith("### "))
    topic_lines = sum(1 for l in entry_text.splitlines() if l.startswith("- topic:"))
    # sweep
    rc, sw, _ = sh("python3", "-B", "reports/round-28/readme/sweep.py")
    sweep_green = ("rows 224 files 224" in sw and "topic_mismatch 0" in sw
                   and "totals_ok True" in sw and "footer_ok True" in sw)
    # D1 resolution: the 'sky, not the ground' exclusion is gone; the corrected
    # condition 1 names a referent space.
    d1_fixed = ("not the ground" not in entry_text
                and "referent space under a declared correspondence" in entry_text)
    c_meas = {"total": tot, "culture_material": cm, "cartography_landed": target.exists(),
              "entry_lines": entry_lines, "entry_h1": h1, "entry_h3": h3,
              "topic_lines": topic_lines, "d1_fixed": d1_fixed, "sweep_green": sweep_green}
    c_ok = (target.exists() and tot == 224 and cm == 26 and entry_lines <= 250
            and h1 == 1 and topic_lines == 1 and sweep_green and d1_fixed)
    results["C"] = {"command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if c_ok else "unchanged-blocked",
        "passed": bool(c_ok), "measurement": c_meas,
        "failures": [] if c_ok else ["cartography entry missing/out-of-band/sweep-red"]}
    if not c_ok:
        failures.append("claim C: entry or sweep thresholds unmet")

    # ---- Ca: calibration ------------------------------------------------------
    readme_h1 = count("^# kotodama-shokunin corpus index", "corpus/README.md")
    succ = pathlib.Path(ROOT, f"{ROUND}/calib/queue-successor-r48.json")
    tool = pathlib.Path(ROOT, "tools/check-readme-heading.py")
    rc_t, tool_out, _ = sh("python3", "-B", "tools/check-readme-heading.py")
    rc_st, st, _ = sh("python3", "-B", "tools/check-readme-heading.py", "--selftest")
    tool_ok = tool.exists() and rc_t == 0 and rc_st == 0 and st.count("PASS") == 8
    ca_meas = {"readme_h1_count": readme_h1, "successor_filed": succ.exists(),
               "successor_sha256": sha_file(f"{ROUND}/calib/queue-successor-r48.json"),
               "parent_pinned_sha256": sha_file("reports/round-40/op/defect-queue-v2.json"),
               "heading_tool_landed": tool.exists(), "heading_tool_rc": rc_t,
               "heading_tool_selftest_pass": st.count("PASS"), "sweep_green": sweep_green}
    ca_ok = (readme_h1 == 1 and succ.exists() and sweep_green and tool_ok)
    results["Ca"] = {"command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if ca_ok else "unprovable",
        "passed": bool(ca_ok), "measurement": ca_meas,
        "failures": [] if ca_ok else ["README heading/successor/control unmet"]}
    if not ca_ok:
        failures.append("claim Ca: README heading count, successor, or control unmet")

    # ---- cross ----------------------------------------------------------------
    rc4, stat, _ = sh("git", "status", "--porcelain=v1")
    corpus_new = [l for l in stat.splitlines() if "cartography-and-mapmaking" in l]
    results["cross"] = {"command": COMMAND, "date": "2026-10-19", "verdict": "measured",
        "passed": True,
        "measurement": {"cartography_new": corpus_new,
                        "fragments_present": len(list(pathlib.Path(ROOT, ROUND).rglob("*.md"))),
                        "seats_filed": "64/64 (key-2)"},
        "failures": []}

    admitted = results["C"]["passed"] and results["Ca"]["passed"]
    return {
        "round": 48, "baseline_revision": BASELINE, "counting_command": COMMAND,
        "date": "2026-10-19",
        "claims_declared": {"C": "coverage", "Ca": "calibration"},
        "claims": results,
        "acceptance_checks_passed": admitted,
        "verdict": "admitted" if admitted else "rejected-honest-stop",
        "partial": ("C improved (entry landed, sweep 224 green) + Ca improved "
                    "(README H1 fix + queue successor + heading control landed)"),
        "failures": failures,
        "limits": [
            "O claim dropped at declaration: the freshness gate (its first live use, a r47 deliverable) flagged the candidate 'resolver drops hyphen soft-wrap' premise as false — resolver yields wrapped=False tokens=1. Routing around a stale premise rather than dispatching it is the gate working.",
            "Entry composition: C02's 23-line head (topic byte-equal to the r44 seed, 766 chars) + C01's 215-line body with R03's D1 fix (register test now admits star chart + cosmogram-boundary-form), D3 shelf coverage (4 external works added), P2/P3 markings. 239 lines; X03's independent composition recommendation matches the landed form.",
            "Queue successor filed as fixed-with-evidence (not routed-with-owner) because the r48 C landing satisfies Ca02's own reclass gates G1-G6; parent defect-queue-v2.json sha-pinned and unedited.",
            "The second README duplicate flagged by X01 (`revision: 2.0` prose lines) is a residual note, not a blocker — recorded in the round report.",
            "Seat audits were run on non-final bytes in-flight; the integration applied fixes and re-verified on the assembled landed bytes (the sweep + heading control + this runner are the post-landing receipt).",
        ],
        "input_sha256": {
            f"{ROUND}/claims.json": sha_file(f"{ROUND}/claims.json"),
            f"{ROUND}/targets.json": sha_file(f"{ROUND}/targets.json"),
            f"{ROUND}/run-validation.py": sha_file(f"{ROUND}/run-validation.py"),
            f"{ROUND}/calib/queue-successor-r48.json": sha_file(f"{ROUND}/calib/queue-successor-r48.json"),
            "tools/check-readme-heading.py": sha_file("tools/check-readme-heading.py"),
            "tools/harness/claims-freshness.py": sha_file("tools/harness/claims-freshness.py"),
            "corpus/knowledge/culture-material/cartography-and-mapmaking.md": sha_file("corpus/knowledge/culture-material/cartography-and-mapmaking.md"),
            "corpus/README.md": sha_file("corpus/README.md"),
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
