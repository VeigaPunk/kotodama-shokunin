#!/usr/bin/env python3
"""Round-50 before/after measurement runner for claims C, O and Ca.

Usage:
    python3 -B reports/round-50/run-validation.py --tree DIR --base-tree DIR [--probe PATH] [--manifest PATH]

DIR is a lane tree; prefer a git checkout (clone or jj-colocated), because the
Ca checker reads claim bytes from git objects and an extract fails that leg
visibly. --base-tree is the base tree at 4ad2683. The runner itself writes
nothing into a tree; each subprocess runs with cwd inside the tree and
PYTHONDONTWRITEBYTECODE=1.

Output is one JSON object on stdout. Each claim reports before (--base-tree),
after (--tree), the integer delta, and acceptance checks. Expectations are the
claims.json values for round 50, hard-coded in EXPECT. Inputs that do not exist
are listed under "absent" with null values; a measurement that raises is
recorded under "error"; a command that fails or times out keeps its status and
output tail. Exit 0 when every check passes, 1 when one fails, 2 for bad args.

Claims:
  C   coverage     pastoralism-animal-husbandry entry (lines, H1, H3, topic, the
                   eight-field head in order); knowledge and culture-material
                   totals; the README sweep (reports/round-28/readme/sweep.py,
                   which measures the tree it lives in); each cited S-id against
                   a corpus/SOURCES.md row opened 2026-10-21 whose used-by names
                   the entry; before-check counts for pastoral/husbandry/herd.
  O   operability  reports/round-50/jj-colocation-probe.py --tools-root <tree> on
                   both trees. The probe is this runner's sibling, so base and
                   landed tool bytes go through one instrument. Also the
                   receipt_guard and check-readme-revisions --selftest runs and
                   the before-check greps.
  Ca  calibration  tools/check-claim-separability.py on the frozen r49 fixture
                   (expect exit 1 naming C->S), on the r50 manifest (expect exit
                   0), its --selftest, and corpus/QUALITY.md separability lines
                   and spot-check citations.
"""
import argparse
import fnmatch
import json
import os
import pathlib
import re
import subprocess
import sys

SCHEMA = "kotodama-round50-run-validation-v1"
DATE = "2026-10-21"
PROBE = pathlib.Path(__file__).resolve().with_name("jj-colocation-probe.py")
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")

KNOWLEDGE = "corpus/knowledge"
CULTURE = "corpus/knowledge/culture-material"
ENTRY = "corpus/knowledge/culture-material/pastoralism-animal-husbandry.md"
ENTRY_NAME = "pastoralism-animal-husbandry.md"
SOURCES = "corpus/SOURCES.md"
QUALITY = "corpus/QUALITY.md"
SWEEP = "reports/round-28/readme/sweep.py"
RECEIPT_GUARD = "tools/harness/receipt_guard.py"
README_REVISIONS = "tools/check-readme-revisions.py"
CHECKER = "tools/check-claim-separability.py"
FIXTURE_R49 = "reports/round-50/separability/r49-fixture.json"
MANIFEST_R50 = "reports/round-50/separability/r50-manifest.json"
SPOTCHECK = "round-49-verifier-spotcheck"

HEAD_FIELDS = ["- topic:", "- gap filled:", "- sources:", "- couples:",
               "- source:", "- verified-at:", "- recheck:", "- scope:"]
ROW_RE = re.compile(r"^\|\s*S\d{3,}\s*\|")
CITED_RE = re.compile(r"\bS\d{3}\b")
TOPIC_OWNER_RE = re.compile(r"^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)",
                            re.IGNORECASE)
FINDING_RE = re.compile(r"SEPARABILITY_DEPENDENCY\s+(\S+?)->(\S+)\s+via")
FALSE_NEG_RES = (
    re.compile(r"false[ _-]?negatives?\s*[:=]\s*(\d+)", re.IGNORECASE),
    re.compile(r"(\d+)\s*/\s*\d+\s+false[ _-]?negatives?", re.IGNORECASE),
)
SWEEP_ROWS_RE = re.compile(r"\brows (\d+) files (\d+)")
SWEEP_TOPIC_RE = re.compile(r"\btopic_mismatch (\d+)")
SWEEP_TOTALS_RE = re.compile(r"\btotals_ok (True|False)")
SWEEP_FOOTER_RE = re.compile(r"\bfooter_ok (True|False)")

# Acceptance expectations from reports/round-50/claims.json. ("min", n) means at
# least n. Keys absent here are measured and reported but not judged.
EXPECT = {
    "C": {
        "before": {
            "knowledge_entries": 225,
            "culture_material_entries": 27,
            "entry_present": False,
            "pastoral_filename_owners": 0,
            "husbandry_filename_owners": 0,
            "herd_filename_owners": 0,
            "pastoral_topic_owner_lines": 0,
        },
        "after": {
            "knowledge_entries": 226,
            "culture_material_entries": 28,
            "entry_present": True,
            "entry_h1": 1,
            "entry_h3": 0,
            "entry_topic": 1,
            "entry_head_fields_ordered": True,
            "sweep_rc": 0,
            "sweep_rows": 226,
            "sweep_files": 226,
            "sweep_topic_mismatch": 0,
            "sources_cited": ("min", 1),
            "sources_unresolved": [],
        },
    },
    "O": {
        "before": {
            "probe_false_negatives": 3,
            "probe_false_positives": 0,
            "guard_remote_ref_lines": 0,
            "readme_skip_marker_lines": ("min", 1),
        },
        "after": {
            "probe_false_negatives": 0,
            "probe_false_positives": 0,
            "receipt_guard_selftest_rc": 0,
            "readme_revisions_selftest_rc": 0,
        },
    },
    "Ca": {
        "before": {
            "separability_tool_files": 0,
            "quality_separab_lines": 0,
        },
        "after": {
            "checker_present": True,
            "r49_fixture_rc": 1,
            "r49_detects_C_to_S": True,
            "r49_matches_independent_prediction": True,
            "r50_manifest_rc": 0,
            "checker_selftest_rc": 0,
            "quality_separab_lines": ("min", 1),
            "quality_cites_spotcheck": ("min", 1),
        },
    },
}


def _text(raw):
    if raw is None:
        return ""
    if isinstance(raw, str):
        return raw
    return raw.decode("utf-8", "replace")


def run(cmd, cwd, timeout=600):
    """Run one command without raising; rc is None unless the command finished."""
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), env=ENV, capture_output=True,
                              timeout=timeout, check=False)
    except subprocess.TimeoutExpired as exc:
        out = _text(exc.stdout)
        return {"rc": None, "status": "timeout", "stdout": out,
                "text": out + _text(exc.stderr)}
    except OSError as exc:
        return {"rc": None, "status": "error", "stdout": "", "text": str(exc)}
    out = _text(proc.stdout)
    return {"rc": proc.returncode, "status": "ok", "stdout": out,
            "text": out + _text(proc.stderr)}


def py(cwd, script, *args, timeout=600):
    """`python3 -B SCRIPT ARGS`, run inside CWD."""
    return run([sys.executable, "-B", str(script), *args], cwd, timeout)


def brief(res):
    return {"rc": res["rc"], "status": res["status"],
            "tail": "\n".join(res["text"].splitlines()[-12:])}


def get(record, key):
    return None if record is None else record[key]


def read_lines(path):
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def count_matching(root, rel, pattern, flags=0):
    """grep -c equivalent: lines of REL matching PATTERN; None when REL is absent."""
    path = root / rel
    if not path.is_file():
        return None
    rx = re.compile(pattern, flags)
    return sum(1 for line in read_lines(path) if rx.search(line))


def find_count(root, rel, glob, ignore_case=False):
    """find REL -name/-iname GLOB | wc -l: files and directories whose name matches."""
    base = root / rel
    if not base.is_dir():
        return None
    total = 0
    for _dirpath, dirnames, filenames in os.walk(base):
        for name in dirnames + filenames:
            if ignore_case:
                hit = fnmatch.fnmatchcase(name.lower(), glob.lower())
            else:
                hit = fnmatch.fnmatchcase(name, glob)
            if hit:
                total += 1
    return total


def topic_owner_lines(root):
    """grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge."""
    base = root / KNOWLEDGE
    if not base.is_dir():
        return None
    hits = 0
    for path in base.rglob("*"):
        if path.is_file():
            hits += sum(1 for line in read_lines(path) if TOPIC_OWNER_RE.search(line))
    return hits


def entry_metrics(root):
    path = root / ENTRY
    if not path.is_file():
        return None
    raw = path.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    first_h2 = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    head = lines[:first_h2]
    positions = [next((i for i, line in enumerate(head) if line.startswith(field)), -1)
                 for field in HEAD_FIELDS]
    return {
        "lines": len(lines),
        "h1": sum(line.startswith("# ") for line in lines),
        "h3": sum(line.startswith("### ") for line in lines),
        "topic": sum(line.startswith("- topic:") for line in lines),
        "head_positions": positions,
        "head_fields_ordered": all(p >= 0 for p in positions) and positions == sorted(positions),
        "cited_source_ids": sorted(set(CITED_RE.findall(raw))),
    }


def sources_check(root, cited):
    """Each cited S-id needs one registry row, opened on DATE, whose used-by cell names the entry."""
    path = root / SOURCES
    if not path.is_file():
        return None
    rows = {}
    for line in read_lines(path):
        if ROW_RE.match(line):
            cells = [c.strip() for c in line.split("|")]
            rows.setdefault(cells[1], []).append(cells)
    status = {}
    for sid in cited:
        found = rows.get(sid, [])
        if not found:
            status[sid] = "no-row"
        elif len(found) > 1:
            status[sid] = "duplicate-row"
        else:
            cells = found[0]
            opened = cells[9] if len(cells) > 9 else ""
            used_by = cells[11] if len(cells) > 11 else ""
            if ENTRY_NAME not in used_by:
                status[sid] = "used-by-missing-entry"
            elif opened != DATE:
                status[sid] = f"opened-{opened or 'blank'}"
            else:
                status[sid] = "ok"
    unresolved = [f"{sid}:{state}" for sid, state in status.items() if state != "ok"]
    return {"cited": cited, "status": status, "unresolved": unresolved}


def sweep_run(root):
    script = root / SWEEP
    if not script.is_file():
        return None
    res = py(root, script)
    text = res["text"]
    rows = SWEEP_ROWS_RE.search(text)
    topic = SWEEP_TOPIC_RE.search(text)
    totals = SWEEP_TOTALS_RE.search(text)
    footer = SWEEP_FOOTER_RE.search(text)
    return {
        **brief(res),
        "rows": int(rows.group(1)) if rows else None,
        "files": int(rows.group(2)) if rows else None,
        "topic_mismatch": int(topic.group(1)) if topic else None,
        "totals_ok": (totals.group(1) == "True") if totals else None,
        "footer_ok": (footer.group(1) == "True") if footer else None,
    }


def measure_c(root, opts):
    absent = [rel for rel in (KNOWLEDGE, CULTURE, SWEEP, ENTRY, SOURCES)
              if not (root / rel).exists()]
    entry = entry_metrics(root)
    sweep = sweep_run(root)
    sources = sources_check(root, entry["cited_source_ids"]) if entry else None
    values = {
        "knowledge_entries": find_count(root, KNOWLEDGE, "*.md"),
        "culture_material_entries": find_count(root, CULTURE, "*.md"),
        "pastoral_filename_owners": find_count(root, KNOWLEDGE, "*pastoral*", True),
        "husbandry_filename_owners": find_count(root, KNOWLEDGE, "*husband*", True),
        "herd_filename_owners": find_count(root, KNOWLEDGE, "*herd*", True),
        "pastoral_topic_owner_lines": topic_owner_lines(root),
        "entry_present": entry is not None,
        "entry_lines": get(entry, "lines"),
        "entry_h1": get(entry, "h1"),
        "entry_h3": get(entry, "h3"),
        "entry_topic": get(entry, "topic"),
        "entry_head_fields_ordered": get(entry, "head_fields_ordered"),
        "sweep_rc": get(sweep, "rc"),
        "sweep_rows": get(sweep, "rows"),
        "sweep_files": get(sweep, "files"),
        "sweep_topic_mismatch": get(sweep, "topic_mismatch"),
        "sources_cited": None if entry is None else len(entry["cited_source_ids"]),
        "sources_unresolved": get(sources, "unresolved"),
    }
    return {"absent": absent, "values": values,
            "detail": {"entry": entry, "sweep": sweep, "sources": sources}}


def probe_run(root, probe):
    if not probe.is_file():
        return None
    res = py(root, probe, "--tools-root", str(root), timeout=900)
    try:
        data = json.loads(res["stdout"])
    except ValueError:
        data = None
    found = None
    if isinstance(data, dict) and isinstance(data.get("false_negatives"), int):
        found = data["false_negatives"]
    else:
        for rx in FALSE_NEG_RES:
            m = rx.search(res["text"])
            if m:
                found = int(m.group(1))
                break
    fp = re.search(r"JJ_COLOCATION_FALSE_POSITIVES=(\d+)/\d+", res["text"])
    return {**brief(res), "false_negatives": found,
            "false_positives": int(fp.group(1)) if fp else None}


def selftest_run(root, rel):
    script = root / rel
    if not script.is_file():
        return None
    return brief(py(root, script, "--selftest"))


def measure_o(root, opts):
    absent = [rel for rel in (RECEIPT_GUARD, README_REVISIONS) if not (root / rel).exists()]
    if not opts.probe.is_file():
        absent.append(str(opts.probe))
    probe_res = probe_run(root, opts.probe)
    guard = selftest_run(root, RECEIPT_GUARD)
    readme = selftest_run(root, README_REVISIONS)
    values = {
        "probe_false_negatives": get(probe_res, "false_negatives"),
        "probe_false_positives": get(probe_res, "false_positives"),
        "receipt_guard_selftest_rc": get(guard, "rc"),
        "readme_revisions_selftest_rc": get(readme, "rc"),
        "guard_remote_ref_lines": count_matching(root, RECEIPT_GUARD,
                                                 re.escape("refs/remotes/origin")),
        "readme_skip_marker_lines": count_matching(root, README_REVISIONS,
                                                   re.escape("base object unreachable")),
    }
    return {"absent": absent, "values": values,
            "detail": {"probe": probe_res, "receipt_guard_selftest": guard,
                       "readme_revisions_selftest": readme}}


def checker_run(root, manifest):
    if not (root / CHECKER).is_file() or not (root / manifest).is_file():
        return None
    res = py(root, root / CHECKER, str(root / manifest))
    return {**brief(res), "text": res["text"],
            "dependencies": [list(pair) for pair in FINDING_RE.findall(res["text"])]}


R49_EXPECTED = "reports/round-50/separability/r49-expected-independent.txt"


def _norm_finding(line):
    """(kind, pair, via, target) — the independent prediction and the tool word findings differently."""
    line = line.strip()
    m = re.match(r"SEPARABILITY_DEPENDENCY (\S+) via (export|land path) '?(.+?)'?(?: (?:named at|matched|x\d).*)?$", line)
    if m:
        return ("DEP", m.group(1), m.group(2), m.group(3).replace("\\\\", "\\"))
    m = re.match(r"SEPARABILITY_OVERLAP (\S+) (\S+)", line)
    return ("OVERLAP", m.group(1), m.group(2)) if m else None


def r49_matches(root, fixture):
    exp = root / R49_EXPECTED
    if fixture is None or not exp.is_file():
        return None
    want = {_norm_finding(l) for l in exp.read_text(encoding="utf-8").splitlines() if _norm_finding(l)}
    got = {_norm_finding(l) for l in fixture["text"].splitlines()
           if l.startswith("SEPARABILITY_") and _norm_finding(l)}
    return bool(want) and want == got


def measure_ca(root, opts):
    absent = [rel for rel in (CHECKER, FIXTURE_R49, QUALITY) if not (root / rel).exists()]
    if not (root / opts.manifest).exists():
        absent.append(opts.manifest)
    fixture = checker_run(root, FIXTURE_R49)
    manifest = checker_run(root, opts.manifest)
    selftest = selftest_run(root, CHECKER)
    values = {
        "separability_tool_files": find_count(root, "tools", "*separab*", True),
        "checker_present": (root / CHECKER).is_file(),
        "r49_fixture_rc": get(fixture, "rc"),
        "r49_detects_C_to_S": None if fixture is None else ["C", "S"] in fixture["dependencies"],
        "r49_matches_independent_prediction": r49_matches(root, fixture),
        "r50_manifest_rc": get(manifest, "rc"),
        "checker_selftest_rc": get(selftest, "rc"),
        "quality_separab_lines": count_matching(root, QUALITY, "separab", re.IGNORECASE),
        "quality_cites_spotcheck": count_matching(root, QUALITY, re.escape(SPOTCHECK)),
    }
    return {"absent": absent, "values": values,
            "detail": {"r49_fixture": fixture, "r50_manifest": manifest,
                       "checker_selftest": selftest}}


MEASURES = {"C": measure_c, "O": measure_o, "Ca": measure_ca}
AXES = {"C": "coverage", "O": "operability", "Ca": "calibration"}


def measured(claim, root, opts):
    try:
        return MEASURES[claim](root, opts)
    except Exception as exc:  # recorded in the receipt instead of aborting the run
        return {"absent": [], "values": {}, "detail": {},
                "error": f"{type(exc).__name__}: {exc}"}


def meets(actual, expected):
    if isinstance(expected, tuple):  # ("min", n)
        return isinstance(actual, int) and not isinstance(actual, bool) and actual >= expected[1]
    return actual == expected


def judge(claim, stage, values):
    return {key: {"expected": expected, "actual": values.get(key),
                  "ok": meets(values.get(key), expected)}
            for key, expected in EXPECT[claim][stage].items()}


def delta(before, after):
    out = {}
    for key, b in before.items():
        a = after.get(key)
        if all(isinstance(v, int) and not isinstance(v, bool) for v in (a, b)):
            out[key] = a - b
    return out


def claim_report(claim, base, tree, opts):
    before = measured(claim, base, opts)
    after = measured(claim, tree, opts)
    acceptance = {"before": judge(claim, "before", before["values"]),
                  "after": judge(claim, "after", after["values"])}
    passed = all(check["ok"] for stage in acceptance.values() for check in stage.values())
    return {"axis": AXES[claim], "before": before, "after": after,
            "delta": delta(before["values"], after["values"]),
            "acceptance": acceptance, "passed": passed}


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Round-50 before/after measurements for claims C, O and Ca (JSON on stdout).")
    ap.add_argument("--tree", required=True, help="landed lane tree (git checkout preferred)")
    ap.add_argument("--base-tree", required=True, help="base tree at 4ad2683")
    ap.add_argument("--probe", default=str(PROBE),
                    help="O probe (default: jj-colocation-probe.py beside this runner)")
    ap.add_argument("--manifest", default=MANIFEST_R50,
                    help="r50 separability manifest, tree-relative or absolute")
    args = ap.parse_args(argv)
    tree = pathlib.Path(args.tree).resolve()
    base = pathlib.Path(args.base_tree).resolve()
    opts = argparse.Namespace(probe=pathlib.Path(args.probe).resolve(), manifest=args.manifest)
    claims = {claim: claim_report(claim, base, tree, opts) for claim in ("C", "O", "Ca")}
    receipt = {
        "schema": SCHEMA,
        "date": DATE,
        "python": sys.version.split()[0],
        "argv": sys.argv[1:],
        "tree": str(tree),
        "base_tree": str(base),
        "probe": str(opts.probe),
        "claims": claims,
        "acceptance_passed": all(report["passed"] for report in claims.values()),
    }
    sys.stdout.write(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    return 0 if receipt["acceptance_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
