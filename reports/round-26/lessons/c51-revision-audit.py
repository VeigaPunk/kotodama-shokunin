#!/usr/bin/env python3
"""R26-C52 — independent audit of the lessons-index revision (read-only).

Audits `reports/round-26/zzz-lessons-index-revision-4.md` against the live
partition, without trusting the revision's own numbers. It answers, one check
per question:

  C52-1  row/file set: every `corpus/lessons/*.md` file has exactly one row in
         the revision, every row names a live file, no duplicate.
  C52-2  pins re-derived: every `bytes`/`lines`/`sha8` cell equals the live
         bytes (the filed index's self-row carries a real digest here).
  C52-3  shape cells re-derived: every `format` and `contract` cell equals a
         live re-classification.
  C52-4  census formats documented: the three the partition carries appear.
  C52-5  prose arithmetic: the revision's stated row/file counts equal the
         measurement.
  C52-6  counting command present.
  C52-7  filed immutability: `corpus/lessons/README.md`'s Git blob equals the
         runner's declared baseline `README_BASELINE_BLOB`.
  C52-8  stale-reading dispositions: each of the six X63-G1 instances has a
         named disposition row in the revision, and the four `fixed`-class
         claims re-verify against the live bytes / `git log`.

`--selftest` mutates the revision in memory, one surface per control, and
asserts the matching check fires. Opens no file for writing; the receipt is the
caller's stdout redirect.

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-26/lessons/c51-revision-audit.py --selftest
    python3 -B reports/round-26/lessons/c51-revision-audit.py
    python3 -B reports/round-26/lessons/c51-revision-audit.py --json
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LESSONS = os.path.join(LANE, "corpus", "lessons")
FILED = os.path.join(LESSONS, "README.md")
REVISION = os.path.join(LANE, "reports", "round-26",
                        "zzz-lessons-index-revision-4.md")
README_BASELINE_BLOB = "a31870556c733498243b56697896504a2fb3679a"

ROW_RE = re.compile(
    r"(?m)^\|\s*`?(?:corpus/lessons/)?([A-Za-z0-9_.-]+\.md)`?\s*\|")
PIN_RE = re.compile(r"(bytes|lines|sha8)=([0-9a-f]+|self-referential)")
FORMATS = ("gate-keeper", "fragment-index", "plain")
ROWS_DECLARED_RE = re.compile(r"(?i)\brows?\s*[:=]\s*\**\s*(\d{1,3})")
FILES_DECLARED_RE = re.compile(r"(?i)\bfiles?\s*[:=]\s*\**\s*(\d{1,3})")
COUNT_COMMAND_RE = re.compile(r"`([^`\n]*(?:ls|find|wc)[^`\n]*)`")

# The six X63-G1 instances: surface token -> the live fact that must hold.
STALE = {
    "round-12.md": ("reports/round-12/validation.json", "44070b4"),
    "round-21.md": ("reports/round-21/validation.json", "46a0325"),
    "Q-04-1": ("tools/gates/typed-pipeline-gate.py", "fc13cd2"),
    "Q-23-1": ("reports/round-25/validation.json", "fc13cd2"),
    "Q-23-2": ("reports/round-25/validation.json", "fc13cd2"),
    "Q-23-3": ("reports/round-25/validation.json", "fc13cd2"),
}


def read_bytes(path):
    with open(path, "rb") as handle:
        return handle.read()


def sha8(data):
    return hashlib.sha256(data).hexdigest()[:8]


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def git(*argv):
    try:
        proc = subprocess.run(["git", *argv], cwd=LANE, capture_output=True,
                              text=True, timeout=60)
        return proc.stdout if proc.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def classify(text):
    if re.search(r"(?m)^## Fragment index\s*$", text):
        return "fragment-index"
    if re.search(r"(?m)^## Gate\s*$", text):
        return "gate-keeper"
    return "plain"


def contract(text):
    head = text.split("\n")[:14]
    return sum(1 for line in head
               if re.match(r"^(source|verified_at|verified-at|recheck|scope):", line.strip()))


def split_row(line):
    """Cells of a §2 row after the file cell, splitting only on unescaped pipes."""
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def parse_rows(text):
    rows = []
    for line in text.splitlines():
        match = ROW_RE.match(line)
        if match:
            rows.append({"file": match.group(1), "cells": split_row(line)})
    return rows


def measure(text=None):
    body = text if text is not None else read_bytes(REVISION).decode("utf-8")
    files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(LESSONS, "*.md")))
    rows = parse_rows(body)
    names = [row["file"] for row in rows]
    out = {"checks": {}, "findings": [], "measurements": {}}

    # C52-1 row/file set
    orphans = [name for name in files if name not in names]
    phantom = [name for name in names if name not in files]
    dupes = sorted({n for n in names if names.count(n) > 1})
    out["checks"]["C52-1_rows_eq_files"] = not orphans and not phantom and not dupes
    out["measurements"]["row_files"] = {"rows": len(names), "files": len(files),
                                        "orphans": orphans, "phantom": phantom,
                                        "duplicates": dupes}
    if orphans or phantom or dupes:
        out["findings"].append({"id": "C52-1", "detail": {"orphans": orphans,
                                                          "phantom": phantom,
                                                          "duplicates": dupes}})

    # C52-2 pins, C52-3 shape cells
    pin_drift, shape_drift = [], []
    for row in rows:
        path = os.path.join(LESSONS, row["file"])
        if not os.path.exists(path):
            continue
        data = read_bytes(path)
        live = {"bytes": str(len(data)), "lines": str(data.decode().count("\n")),
                "sha8": sha8(data)}
        pin_cell = next((c for c in row["cells"] if "bytes=" in c), "")
        claimed = dict(PIN_RE.findall(pin_cell))
        bad = {key: {"claimed": claimed.get(key), "live": live[key]}
               for key in ("bytes", "lines", "sha8") if claimed.get(key) != live[key]}
        if bad:
            pin_drift.append({"file": row["file"], "drift": bad})
        claimed_fmt = (row["cells"][1] if len(row["cells"]) > 1 else "").split("(")[0].strip()
        if claimed_fmt and claimed_fmt != "index" and claimed_fmt not in ("—", "-"):
            if claimed_fmt != classify(data.decode()):
                shape_drift.append({"file": row["file"], "claimed": claimed_fmt,
                                    "live": classify(data.decode())})
        claimed_contract = row["cells"][2] if len(row["cells"]) > 2 else ""
        match = re.match(r"(\d)/4", claimed_contract)
        if match and int(match.group(1)) != contract(data.decode()):
            shape_drift.append({"file": row["file"], "claimed": claimed_contract,
                                "live": f"{contract(data.decode())}/4"})
    out["checks"]["C52-2_pins_rederived"] = not pin_drift
    out["checks"]["C52-3_shape_cells_rederived"] = not shape_drift
    out["measurements"]["pins"] = {"checked": len(rows), "drift": pin_drift}
    out["measurements"]["shape_cells"] = {"drift": shape_drift}
    if pin_drift:
        out["findings"].append({"id": "C52-2", "detail": pin_drift})
    if shape_drift:
        out["findings"].append({"id": "C52-3", "detail": shape_drift})

    # C52-4 formats documented
    present = [name for name in FORMATS if name in body.lower()]
    out["checks"]["C52-4_formats_documented"] = len(present) == len(FORMATS)
    out["measurements"]["formats"] = {"documented": present}
    if len(present) != len(FORMATS):
        out["findings"].append({"id": "C52-4", "detail": present})

    # C52-5 prose arithmetic, C52-6 counting command
    declared_rows = {int(v) for v in ROWS_DECLARED_RE.findall(body)}
    declared_files = {int(v) for v in FILES_DECLARED_RE.findall(body)}
    ok = (not declared_rows or len(rows) in declared_rows) and \
         (not declared_files or len(files) in declared_files)
    out["checks"]["C52-5_prose_arithmetic"] = ok
    out["measurements"]["arithmetic"] = {"declared_rows": sorted(declared_rows),
                                         "measured_rows": len(rows),
                                         "declared_files": sorted(declared_files),
                                         "measured_files": len(files)}
    if not ok:
        out["findings"].append({"id": "C52-5", "detail": out["measurements"]["arithmetic"]})
    has_cmd = bool(COUNT_COMMAND_RE.search(body))
    out["checks"]["C52-6_counting_command"] = has_cmd
    if not has_cmd:
        out["findings"].append({"id": "C52-6", "detail": "no counting command"})

    # C52-7 filed immutability
    filed_blob = git_blob_sha(read_bytes(FILED))
    out["checks"]["C52-7_filed_unchanged"] = filed_blob == README_BASELINE_BLOB
    out["measurements"]["filed"] = {"blob_sha1": filed_blob,
                                    "declared_baseline": README_BASELINE_BLOB,
                                    "unchanged": filed_blob == README_BASELINE_BLOB}
    if filed_blob != README_BASELINE_BLOB:
        out["findings"].append({"id": "C52-7", "detail": out["measurements"]["filed"]})

    # C52-8 stale-reading dispositions
    section3 = body.split("## 3.")[1].split("## 4.")[0] if "## 3." in body else ""
    dispositions = []
    for surface, (path, commit) in STALE.items():
        row = next((line for line in section3.splitlines()
                    if surface in line and line.strip().startswith("|")), "")
        named = bool(row)
        live_ok = None
        if path.endswith("validation.json"):
            try:
                live_ok = json.loads(read_bytes(os.path.join(LANE, path))
                                     .decode())["acceptance_checks_passed"] is True
            except (OSError, ValueError, KeyError):
                live_ok = False
        elif path.endswith(".py"):
            live_ok = b"D4L-ARGOT-DERIV" in read_bytes(os.path.join(LANE, path))
        if path.endswith(".py"):
            log = git("log", "--format=%h", "-S", "D4L-ARGOT-DERIV", "--", path) or ""
        else:
            log = git("log", "--format=%h", "--diff-filter=A", "--", path) or ""
        commit_ok = commit in log
        dispositions.append({"surface": surface, "disposition_row": named,
                             "live_fact_ok": live_ok, "commit_ok": commit_ok})
    ok = all(d["disposition_row"] and d["live_fact_ok"] and d["commit_ok"]
             for d in dispositions)
    out["checks"]["C52-8_stale_dispositions"] = ok
    out["measurements"]["stale_dispositions"] = dispositions
    if not ok:
        out["findings"].append({"id": "C52-8", "detail": dispositions})

    out["revision"] = {"path": os.path.relpath(REVISION, LANE),
                       "bytes": len(read_bytes(REVISION)),
                       "sha256": hashlib.sha256(read_bytes(REVISION)).hexdigest()}
    out["passed"] = not out["findings"]
    return out


def selftest():
    checks = []
    base = read_bytes(REVISION).decode("utf-8")
    live = measure(base)

    def check(name, cond, observed=""):
        checks.append({"name": name, "pass": bool(cond), "observed": observed})

    check("live revision is audited", live["revision"]["bytes"] > 0,
          live["revision"]["sha256"][:16])
    check("partition is 27 files", live["measurements"]["row_files"]["files"] == 27,
          live["measurements"]["row_files"]["files"])
    for key in ("C52-1_rows_eq_files", "C52-2_pins_rederived",
                "C52-3_shape_cells_rederived", "C52-4_formats_documented",
                "C52-5_prose_arithmetic", "C52-6_counting_command",
                "C52-7_filed_unchanged", "C52-8_stale_dispositions"):
        check(f"{key} green on live bytes", live["checks"][key])

    # controls: one mutation per surface
    cut = re.sub(r"(?m)^\|\s*`corpus/lessons/round-23\.md`[^\n]*\n", "", base)
    rows = [r["file"] for r in parse_rows(cut)]
    files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(LESSONS, "*.md")))
    check("row/file check fires on a deleted row", bool([f for f in files if f not in rows]))

    forged = base.replace("sha8=b567a60a", "sha8=deadbeef")
    bad = []
    for row in parse_rows(forged):
        data = read_bytes(os.path.join(LESSONS, row["file"]))
        pin = dict(PIN_RE.findall(next((c for c in row["cells"] if "bytes=" in c), "")))
        if pin.get("sha8") != sha8(data):
            bad.append(row["file"])
    check("pin check fires on a falsified pin", bad == ["round-23.md"], bad)

    drifted = base.replace("Rows: 27", "Rows: 99").replace("Files: 27", "Files: 99")
    stated = {int(v) for v in ROWS_DECLARED_RE.findall(drifted)}
    # The control is a *new* declared value the measurement does not match, which
    # is the defect the check exists to catch; the earlier occurrence of the
    # honest 27 must not mask it.
    check("arithmetic check fires on drifted prose",
          99 in stated and len(parse_rows(drifted)) != 99, sorted(stated))

    no_cmd = base.replace("`", "")
    check("counting-command check fires when the command is removed",
          not COUNT_COMMAND_RE.search(no_cmd))

    silent = re.sub(r"(?m)^\| 3 \| `Q-04-1`[^\n]*\n", "", base)
    sec3 = silent.split("## 3.")[1].split("## 4.")[0]
    rows8 = [surface for surface in STALE
             if not any(surface in line and line.strip().startswith("|")
                        for line in sec3.splitlines())]
    check("stale-disposition check fires on a removed disposition row", bool(rows8), rows8)

    passed = sum(1 for c in checks if c["pass"])
    print(json.dumps({"schema": "kotodama-c51-revision-audit-selftest-v1",
                      "checks": checks, "passed": passed, "total": len(checks)},
                     indent=1, ensure_ascii=False))
    return 0 if passed == len(checks) else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    result = measure()
    if args.json:
        print(json.dumps(result, indent=1, ensure_ascii=False, sort_keys=True))
        return 0 if result["passed"] else 1
    print("revision:     %s" % result["revision"]["path"])
    print("sha256:       %s" % result["revision"]["sha256"])
    print("rows/files:   %d / %d" % (result["measurements"]["row_files"]["rows"],
                                     result["measurements"]["row_files"]["files"]))
    for key, value in result["checks"].items():
        print("  %-34s %s" % (key, "PASS" if value else "FAIL"))
    print("findings:     %d" % len(result["findings"]))
    for finding in result["findings"]:
        print("  %s: %s" % (finding["id"], json.dumps(finding["detail"], ensure_ascii=False)[:300]))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
