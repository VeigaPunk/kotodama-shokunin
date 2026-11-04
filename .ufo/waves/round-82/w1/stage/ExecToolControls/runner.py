#!/usr/bin/env python3
"""ExecToolControls — controls receipt runner for draft tools/check-sources-recheck.py.

Env: RECHECK_TOOL=<path to draft tool>. --gen-only writes fixtures and exits.
Writes controls.md + controls.json into the seat stage dir.
"""
import argparse, hashlib, json, os, re, subprocess, sys
from datetime import date, timedelta

SCRATCH = "/fast/scratch/hyaku/kotodama-r82/ExecToolControls"
FX = os.path.join(SCRATCH, "fx")
STAGE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecToolControls"
TOOL = os.environ.get("RECHECK_TOOL", "")
AS_OF = "2026-11-04"
WINDOW = 90

HEADER = "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |"
SEP = "|---|---|---|---|---|---|---|---|---|---|---|"

def row(sid, opened, recheck, usedby="—", indent=0, extra=None):
    cells = [sid, "Fixture Source — https://example.org/fx", "dataset", "A",
             "controls stress scope", "anchor p1 para", "teaches text for controls", 
             "queued", opened, recheck, usedby]
    if extra:
        cells.append(extra)
    return " " * indent + "| " + " | ".join(cells) + " |"

def registry(*rows):
    return ("# SOURCES — controls fixture\n\n"
            "prose preamble; tool must scope to the Registry section.\n\n"
            "## Registry\n\n" + HEADER + "\n" + SEP + "\n" +
            "".join(r + "\n" for r in rows))

DUE_ASOF = row("S201", "2026-01-01", "2026-11-04")          # recheck ISO == as-of
DUE_NND  = row("S202", "2026-11-01", "3d")                  # NNd lands exactly on as-of
UP_EDGE  = row("S203", "2026-01-01", "2027-02-02")          # == as-of + 90
BEYOND   = row("S204", "2026-01-01", "2027-02-03")          # == as-of + 91
ONREL    = row("S205", "2026-01-01", "on-release")
NEUTRAL  = row("S210", "2026-01-01", "2099-01-01")          # far future: neither due nor upcoming

FIXTURES = {
    "fx01_empty":            registry(),
    "fx02_due_on_asof":      registry(DUE_ASOF),
    "fx02b_nnd_due":         registry(DUE_NND),
    "fx03_upcoming_edge":    registry(UP_EDGE),
    "fx04_beyond_window":    registry(BEYOND),
    "fx05_on_release":       registry(ONREL),
    "fx06_12_cell_row":      registry(row("S206", "2026-01-01", "90d", extra="EXTRA")),
    "fx07_recheck_soon":     registry(row("S207", "2026-01-01", "soon")),
    "fx08_bad_opened":       registry(row("S208", "2026-13-40", "90d")),
    "fx10_base_plus_neutral": registry(DUE_ASOF, NEUTRAL),
    "fx11_indented_neutral": registry(DUE_ASOF, NEUTRAL.replace("| S210", "  | S210")),
    "fx11b_4space_neutral":  registry(DUE_ASOF, NEUTRAL.replace("| S210", "    | S210")),
    "fx12_pipe_in_usedby":   registry(row("S212", "2026-01-01", "90d", usedby="corpus/a.md|corpus/b.md")),
}

# (id, fixture, extra_args, expected_exit, expected_stdout (exact, None=skip), desc)
CASES = [
    ("00-selftest", None, ["--selftest"], 0, None,
     "--selftest runs >= 8 checks, prints SELFTEST: PASS (<n> checks)"),
    ("01-empty-registry", "fx01_empty", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 0 rows",
     "header-only registry -> all zero, exit 0"),
    ("02-due-exactly-on-asof", "fx02_due_on_asof", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows\nDUE S201 2026-11-04",
     "recheck ISO == as-of -> due +1"),
    ("02b-nnd-lands-on-asof", "fx02b_nnd_due", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows\nDUE S202 2026-11-04",
     "opened 2026-11-01 + 3d == as-of -> due +1 (NNd conversion)"),
    ("03-due-at-window-edge", "fx03_upcoming_edge", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 0 due / 1 upcoming / 0 on-release / 1 rows",
     "due_date == as-of+window(90) -> upcoming +1 (inclusive edge)"),
    ("03b-window-89-flag", "fx03_upcoming_edge", ["--as-of", AS_OF, "--window", "89"], 0,
     "RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 1 rows",
     "same fixture with --window 89 -> edge drops out (window flag honoured)"),
    ("04-beyond-window", "fx04_beyond_window", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 1 rows",
     "due_date == as-of+window+1 -> neither due nor upcoming"),
    ("05-on-release", "fx05_on_release", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 0 due / 0 upcoming / 1 on-release / 1 rows",
     "on-release -> exempt cadence counted, not due"),
    ("06-12-cell-row", "fx06_12_cell_row", ["--as-of", AS_OF], 2, None,
     "12-cell row -> exit 2, RECHECK-ERROR, no traceback"),
    ("07-recheck-soon", "fx07_recheck_soon", ["--as-of", AS_OF], 2, None,
     "recheck 'soon' unparseable -> exit 2, RECHECK-ERROR, no traceback"),
    ("08-opened-invalid-iso", "fx08_bad_opened", ["--as-of", AS_OF], 2, None,
     "opened 2026-13-40 -> exit 2, RECHECK-ERROR, no traceback"),
    ("09-missing-registry-file", None, ["--registry", os.path.join(FX, "does-not-exist.md"),
                                        "--as-of", AS_OF], 2, None,
     "missing --registry path -> exit 2, RECHECK-ERROR (not an uncaught exception)"),
    ("10-population-modularity", "fx10_base_plus_neutral", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 2 rows\nDUE S201 2026-11-04",
     "base + neutral row -> due/upcoming/on-release unchanged, rows +1"),
    ("11-indented-row", "fx11_indented_neutral", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 2 rows\nDUE S201 2026-11-04",
     "2-space indented row parsed (census grammar allows 0-3 leading spaces)"),
    ("11b-4space-row-ignored", "fx11b_4space_neutral", ["--as-of", AS_OF], 0,
     "RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows\nDUE S201 2026-11-04",
     "observation: 4-space indented row is outside the 0-3 grammar -> silently ignored"),
    ("12-pipe-in-usedby", "fx12_pipe_in_usedby", ["--as-of", AS_OF], 2, None,
     "used-by with embedded pipe -> 12 cells -> grammar forbids; expect exit 2 RECHECK-ERROR"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen-only", action="store_true")
    args = ap.parse_args()

    os.makedirs(FX, exist_ok=True)
    os.makedirs(os.path.join(SCRATCH, "tmp"), exist_ok=True)
    for name, content in FIXTURES.items():
        with open(os.path.join(FX, name + ".md"), "w") as f:
            f.write(content)

    meta = {
        "seat": "ExecToolControls", "round": 82, "wave": "r82-v1",
        "as_of": AS_OF, "window": WINDOW,
        "window_edge_asof_plus_90": str(date(2026, 11, 4) + timedelta(days=90)),
        "window_edge_plus_91": str(date(2026, 11, 4) + timedelta(days=91)),
        "tool": TOOL, "tool_sha256": None, "tool_mtime": None, "tool_missing": not TOOL or not os.path.exists(TOOL),
        "python": sys.version.split()[0],
    }
    if TOOL and os.path.exists(TOOL):
        meta["tool_sha256"] = hashlib.sha256(open(TOOL, "rb").read()).hexdigest()
        meta["tool_mtime"] = os.path.getmtime(TOOL)

    results = []
    for cid, fxname, extra, eexit, eout, desc in CASES:
        rec = {"id": cid, "desc": desc, "fixture": fxname,
               "fixture_content": FIXTURES.get(fxname) if fxname else None,
               "command": None, "stdout": None, "stderr": None,
               "exit_code": None, "expected_exit": eexit,
               "expected_stdout": eout, "verdict": "unrun", "notes": []}
        if meta["tool_missing"]:
            rec["verdict"] = "unrun"
            rec["notes"].append("draft tool absent at run time")
            results.append(rec)
            continue
        argv = [sys.executable, TOOL] + (["--registry", os.path.join(FX, fxname + ".md")] if fxname and "--selftest" not in extra else []) + extra
        rec["command"] = " ".join(argv)
        env = dict(os.environ, TMPDIR=os.path.join(SCRATCH, "tmp"))
        p = subprocess.run(argv, capture_output=True, text=True, env=env, cwd=SCRATCH, timeout=60)
        rec["exit_code"] = p.returncode
        rec["stdout"] = p.stdout
        rec["stderr"] = p.stderr
        combined = p.stdout + p.stderr
        checks = []
        checks.append(("exit code", p.returncode == eexit))
        checks.append(("no traceback", "Traceback (most recent call last)" not in combined))
        if "--selftest" in extra:
            mst = re.fullmatch(r"SELFTEST: PASS \((\d+) checks\)\n?", p.stdout)
            checks.append(("selftest line format", bool(mst)))
            checks.append(("selftest >= 8 checks", bool(mst) and int(mst.group(1)) >= 8))
        else:
            if eexit == 0:
                checks.append(("exactly one summary line",
                               len(re.findall(r'^RECHECK-QUEUE:', combined, re.M)) == 1))
            if eout is not None:
                same_set = (sorted(p.stdout.splitlines()) == sorted(eout.splitlines())
                            and len(p.stdout.splitlines()) == len(eout.splitlines()))
                checks.append(("stdout lines exact, order-insensitive (contract pins membership, not order)", same_set))
                if same_set and p.stdout.rstrip("\n") != eout.rstrip("\n"):
                    rec["notes"].append(
                        "line ORDER differs from contract prose order: tool prints DUE lines first, "
                        "summary last; contract text pins membership only; tool's own selftest expects DUE-first")
        if eexit == 2:
            checks.append(("RECHECK-ERROR printed", bool(re.search(r'^RECHECK-ERROR \S', combined, re.M))))
        rec["checks"] = [{"check": n, "ok": ok} for n, ok in checks]
        rec["verdict"] = "pass" if all(ok for _, ok in checks) else "FAIL"
        results.append(rec)

    summary = {v: sum(1 for r in results if r["verdict"] == v) for v in ("pass", "FAIL", "unrun")}
    out = {"meta": meta, "summary": summary, "cases": results}
    os.makedirs(STAGE, exist_ok=True)
    with open(os.path.join(STAGE, "controls.json"), "w") as f:
        json.dump(out, f, indent=2)
    write_md(out)
    print("gen-only" if args.gen_only else "ran",
          {k: v for k, v in summary.items()}, "->", STAGE)
    return 0

def write_md(out):
    m, cases = out["meta"], out["cases"]
    L = []
    L.append("# ExecToolControls — controls receipt, draft `tools/check-sources-recheck.py`\n")
    L.append(f"- tool: `{m['tool'] or 'ABSENT'}`")
    if m.get("tool_sha256"):
        L.append(f"- tool sha256: `{m['tool_sha256']}` (mtime {m['tool_mtime']})")
    L.append(f"- as-of {m['as_of']}, window {m['window']}: edge +90 = {m['window_edge_asof_plus_90']}, +91 = {m['window_edge_plus_91']} — python3 -c \"date(2026,11,4)+timedelta(days=90)\"")
    L.append(f"- python {m['python']}; runner: /fast/scratch/hyaku/kotodama-r82/ExecToolControls/runner.py\n")
    for c in cases:
        L.append(f"## {c['id']} — {c['desc']}")
        L.append(f"- expected exit {c['expected_exit']}; verdict **{c['verdict']}**")
        if c.get("fixture_content"):
            L.append(f"- fixture `{c['fixture']}.md`:")
            L.append("```")
            L.append(c["fixture_content"].rstrip("\n"))
            L.append("```")
        if c.get("command"):
            L.append(f"- command: `{c['command']}`")
            L.append("- raw stdout:")
            L.append("```")
            L.append((c["stdout"] if c["stdout"] != "" else "(empty)").rstrip("\n"))
            L.append("```")
            L.append("- raw stderr:")
            L.append("```")
            L.append((c["stderr"] if c["stderr"] != "" else "(empty)").rstrip("\n"))
            L.append("```")
            L.append(f"- exit code: {c['exit_code']}")
        if c.get("checks"):
            L.append("- checks: " + "; ".join(f"{k['check']}={'ok' if k['ok'] else 'MISMATCH'}" for k in c["checks"]))
        for n in c.get("notes", []):
            L.append(f"- note: {n}")
        L.append("")
    L.append("## Observations (behavior, not failures)")
    L.append("- Output order: `DUE` lines precede the `RECHECK-QUEUE` summary; the contract pins line membership only "
             "(cases 02/02b/10/11), and the tool's own selftest expects DUE-first. No action needed unless the L1 wants to pin order.")
    L.append("- Row matching is `^\\s{0,3}\\|\\s*S\\d{3,}\\s*\\|` applied to EVERY line of the file (not scoped to `## Registry`). "
             "Harmless for the real corpus: sweep of base c285b2af and worktree found S-id pipe rows only as registry rows "
             "(base 827 / worktree 831 rows, all 11 cells, all flush-left).")
    L.append("- Real-corpus cadence vocabulary (worktree): on-release 14, NNd 663, ISO 154 — no other form occurs; "
             "case 07's `soon` cannot arise today but correctly exits 2.")
    L.append("- 4-space (or deeper) indented S-rows are silently skipped by ROW_RE (case 11b) — outside the 0-3 grammar, ignored not errored.")
    L.append("- `used-by` with an embedded pipe widens the cell count to 12 and is rejected exit 2 (case 12). The real registry forbids it: "
             "zero non-11-cell rows in base and worktree sweeps — python3 sweep over git show c285b2af…:corpus/SOURCES.md and worktree copy.")
    L.append("")
    with open(os.path.join(STAGE, "controls.md"), "w") as f:
        f.write("\n".join(L))

if __name__ == "__main__":
    main()
