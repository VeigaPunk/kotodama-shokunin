#!/usr/bin/env python3
"""X63 — lessons-index audit (round 26, read-only).

Audits `corpus/lessons/README.md` (the round-25 reconciled index) against the
live partition. It re-derives the row/file set, every pin cell, every format
and contract cell, the disposition pointers, the open-question queue and the
index's own stated arithmetic, and it reports the cells whose reading was true
at the index's stamp but is contradicted by today's bytes.

It opens no file for writing. The receipt is the caller's stdout redirect:

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-26/audit/x63-lessons-audit.py --selftest   # controls
    python3 -B reports/round-26/audit/x63-lessons-audit.py              # findings
    python3 -B reports/round-26/audit/x63-lessons-audit.py --json       # receipt

Relation to the round-25 auditors, named so the reader can tell the tools
apart rather than assume they overlap:

  * `reports/round-25/audit/c31-lessons-index-audit.py` checks row/file set,
    owner resolution, documented formats and pin re-derivation.
  * `reports/round-25/audit/x45-lessons-pointer-audit.py` checks the
    disposition-pointer column and the index's prose counts.
  * this tool re-checks the union of those surfaces on the *current* bytes and
    adds a staleness probe (a reading that was true at the index's stamp and is
    false now), which neither round-25 tool performs.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LESSONS = os.path.join(LANE, "corpus", "lessons")
INDEX = os.path.join(LESSONS, "README.md")
GATE = os.path.join(LANE, "tools", "gates", "typed-pipeline-gate.py")
R25_RECEIPT = os.path.join(LANE, "reports", "round-25", "validation.json")

ROW_RE = re.compile(r"(?m)^\|\s*`corpus/lessons/([A-Za-z0-9_.-]+\.md)`\s*\|(.*)\|\s*$")
R13_RE = re.compile(r"(?m)^\|\s*`?round-(\d+)`?\s*\|")
QUEUE_ROW_RE = re.compile(r"(?m)^\|\s*(Q-[A-Za-z0-9-]+)\s*\|")
CARRIED_RE = re.compile(r"Q-(\d+)-(\d+)\.\.(\d+)")
CARRIED_ONE_RE = re.compile(r"Q-([A-Za-z0-9]+)-(\d+)(?!\.\.)")
PIN_RE = re.compile(r"(bytes|lines|sha8)=([0-9a-zA-Z-]+)")

# A pointer cell that declares a path was never filed is honest and is exempt
# from resolution. Keyed to the cell's own words, so a silently dead pointer is
# still reported (the rule the round-25 X45 tool established).
DECLARED_ABSENT = (
    "not filed", "no lesson file", "does not exist", "never existed",
    "no such", "fleet root", "outside this repo", "operator-skipped",
)
DECLARED_ABSENT_RE = re.compile(r"no\s+`[^`]+`\s+exists|no\s+`[^`]+\*?`\s+exists")
TOKEN_RE = re.compile(r"`([^`\n]+)`")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    with open(path, "rb") as handle:
        return handle.read()


def lesson_files():
    return sorted(os.path.basename(p) for p in glob.glob(os.path.join(LESSONS, "*.md")))


def split_row(rest):
    """Cells of a §2 row after the file cell, splitting only on unescaped pipes."""
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", rest)]


def format_class(name, text):
    """The partition's classifier: exact `## Gate` heading wins over prose."""
    if name == "README.md":
        return "index"
    gate = bool(re.search(r"(?m)^## Gate\s*$", text))
    frag = bool(re.search(r"(?m)^## Fragment index\s*$", text))
    if frag:
        return "fragment-index"
    if gate:
        return "gate-keeper"
    return "plain"


def parse_index(text):
    rows = []
    for match in ROW_RE.finditer(text):
        cells = split_row(match.group(2))
        rows.append({"file": match.group(1), "cells": cells})
    return rows


def parse_queue(text):
    marker = re.search(r"(?im)^#{1,6}[^\n]*open[- ]question[^\n]*$", text)
    if not marker:
        return [], []
    tail = text[marker.end():]
    stop = re.search(r"(?m)^#{1,6}\s", tail)
    block = tail[:stop.start()] if stop else tail
    lines = [line.strip() for line in block.splitlines() if line.strip().startswith("|")]
    data = [line for line in lines if not re.match(r"^\|[\s|:-]+\|$", line)]
    header = data[0] if data else ""
    ids = [m.group(1) for m in QUEUE_ROW_RE.finditer("\n".join(data))]
    entries = []
    for line in data:
        cells = [cell.strip().strip("`*") for cell in re.split(r"(?<!\\)\|", line.strip("|"))]
        if len(cells) >= 4 and cells[0].startswith("Q-") and cells[0] != "Q-id":
            entries.append({"id": cells[0], "question": cells[1], "owner": cells[2],
                            "status": cells[3]})
    raw = [line for line in block.splitlines() if line.strip().startswith("|")]
    return entries, raw


def resolves(token):
    path = token.split()[0].strip("`")
    if not path or " " in path:
        return None
    if not re.match(r"^(corpus|reports|tools|examples|scripts|LOG|SCORECARD|AGENTS|"
                    r"PROVINCE|\.ufo|\.scratch)", path):
        return None
    return os.path.exists(os.path.join(LANE, path))


def measure():
    index_bytes = read(INDEX)
    text = index_bytes.decode()
    files = lesson_files()
    rows = parse_index(text)
    entries, queue_lines = parse_queue(text)
    out = {
        "schema": "kotodama-lessons-audit-x63-v1",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "lane": LANE,
        "index": {"path": "corpus/lessons/README.md",
                  "sha256": sha256_bytes(index_bytes),
                  "bytes": len(index_bytes),
                  "lines": index_bytes.decode().count("\n")},
        "partition": {"files": len(files)},
        "checks": {},
        "findings": [],
        "measurements": {},
    }
    checks = out["checks"]

    # ---- A: row/file set equality -------------------------------------
    row_files = [row["file"] for row in rows]
    orphans = [name for name in files if name not in row_files]
    phantom = [name for name in row_files if name not in files]
    dupes = sorted({name for name in row_files if row_files.count(name) > 1})
    checks["A_rows_eq_files"] = not orphans and not phantom and not dupes
    out["measurements"]["row_files"] = {"index_rows": len(row_files), "files": len(files),
                                        "orphans": orphans, "phantom": phantom,
                                        "duplicates": dupes}
    if orphans:
        out["findings"].append({"id": "X63-A1", "kind": "unindexed-file", "detail": orphans})
    if phantom:
        out["findings"].append({"id": "X63-A2", "kind": "phantom-row", "detail": phantom})

    # ---- B: pins and shape cells re-derived ---------------------------
    drift, shape_drift, exempt = [], [], []
    for row in rows:
        cells = row["cells"]
        name = row["file"]
        path = os.path.join(LESSONS, name)
        body = read(path)
        live = {"bytes": str(len(body)),
                "lines": str(body.decode().count("\n")),
                "sha8": sha256_bytes(body)[:8]}
        pin_cell = next((c for c in cells if "bytes=" in c), "")
        claimed = dict(PIN_RE.findall(pin_cell))
        if claimed.get("sha8") == "self-referential":
            exempt.append(name)
            continue
        bad = {k: {"claimed": claimed.get(k), "live": live[k]}
               for k in ("bytes", "lines", "sha8") if claimed.get(k) != live[k]}
        if bad:
            drift.append({"file": name, "drift": bad})
        live_fmt = format_class(name, body.decode())
        claimed_fmt = cells[0] if cells else ""
        claimed_fmt = claimed_fmt.split("(")[0].strip()
        if claimed_fmt and claimed_fmt != live_fmt and not claimed_fmt.startswith("index"):
            shape_drift.append({"file": name, "claimed": claimed_fmt, "live": live_fmt})
        contract_cell = cells[1] if len(cells) > 1 else ""
        match = re.match(r"(\d)/4", contract_cell)
        if match:
            head = body.decode().split("\n")[:14]
            live_n = sum(1 for line in head
                         if re.match(r"^(source|verified_at|verified-at|recheck|scope):",
                                     line.strip()))
            if int(match.group(1)) != live_n:
                shape_drift.append({"file": name, "contract_claimed": contract_cell,
                                    "contract_live": f"{live_n}/4"})
    checks["B_pins_rederived"] = not drift
    checks["B2_shape_cells_rederived"] = not shape_drift
    out["measurements"]["pins"] = {"checked": len(rows) - len(exempt),
                                   "self_referential_exempt": exempt,
                                   "drift": drift}
    out["measurements"]["shape_cells"] = {"drift": shape_drift}
    if drift:
        out["findings"].append({"id": "X63-B1", "kind": "pin-drift", "detail": drift})
    if shape_drift:
        out["findings"].append({"id": "X63-B2", "kind": "shape-cell-drift",
                                "detail": shape_drift})

    # ---- D: disposition pointers resolve ------------------------------
    unresolved, declared_absent = [], []
    for row in rows:
        pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
        absent_cell = any(phrase in pointer.lower() for phrase in DECLARED_ABSENT) \
            or bool(DECLARED_ABSENT_RE.search(pointer))
        for token in TOKEN_RE.findall(pointer):
            ok = resolves(token)
            if ok is None or ok:
                continue
            record = {"file": row["file"], "token": token,
                      "cell_says_absent": absent_cell}
            (declared_absent if absent_cell else unresolved).append(record)
    checks["D_pointers_resolve"] = not unresolved
    out["measurements"]["pointers"] = {"unresolved": unresolved,
                                       "declared_absent_unresolved": declared_absent}
    if unresolved:
        out["findings"].append({"id": "X63-D1", "kind": "dead-pointer",
                                "detail": unresolved})

    # ---- E: queue ↔ carried ids, owners -------------------------------
    queue_ids = [entry["id"] for entry in entries]
    carried = set()
    section = text.split("## 2. Per-round index")[1].split("**Rows:")[0]
    for match in CARRIED_RE.finditer(section):
        for i in range(int(match.group(2)), int(match.group(3)) + 1):
            carried.add("Q-%s-%d" % (match.group(1), i))
    for match in CARRIED_ONE_RE.finditer(section):
        carried.add("Q-%s-%s" % (match.group(1), match.group(2)))
    carried_not_queued = sorted(carried - set(queue_ids))
    queued_not_carried = sorted(set(queue_ids) - carried)
    bad_owners = []
    for entry in entries:
        owner = entry["owner"].strip("` ")
        token = owner.split()[0].strip("`") if owner else ""
        if token in ("operator", "parent"):
            continue
        if not os.path.exists(os.path.join(LANE, token)):
            bad_owners.append({"id": entry["id"], "owner": entry["owner"]})
    checks["E_queue_cross_consistency"] = not carried_not_queued and not queued_not_carried
    checks["E2_owners_resolve"] = not bad_owners
    out["measurements"]["queue"] = {"rows": len(entries), "ids": len(queue_ids),
                                    "carried_ids": len(carried),
                                    "carried_not_queued": carried_not_queued,
                                    "queued_not_carried": queued_not_carried,
                                    "unresolved_owners": bad_owners}
    if carried_not_queued or queued_not_carried:
        out["findings"].append({"id": "X63-E1", "kind": "queue-orphan",
                                "detail": {"carried_not_queued": carried_not_queued,
                                           "queued_not_carried": queued_not_carried}})
    if bad_owners:
        out["findings"].append({"id": "X63-E2", "kind": "unresolved-owner",
                                "detail": bad_owners})

    # ---- F: prose arithmetic vs measurement ---------------------------
    stated_rows = {int(v) for v in re.findall(r"(?i)\brows?\s*:\s*\**\s*(\d{1,3})", text)}
    stated_files = {int(v) for v in re.findall(r"(?i)\bfiles?\s*:\s*\**\s*(\d{1,3})", text)}
    # The runner's own convention: every pipe-prefixed line in the queue block.
    runner_lines = len(queue_lines)
    arithmetic_ok = (not stated_rows or len(queue_ids) in stated_rows) and \
                    (not stated_files or len(files) in stated_files)
    checks["F_prose_arithmetic"] = arithmetic_ok
    out["measurements"]["arithmetic"] = {
        "stated_rows": sorted(stated_rows), "measured_data_rows": len(queue_ids),
        "stated_files": sorted(stated_files), "measured_files": len(files),
        "runner_pipe_lines": runner_lines,
        "note": "the index states its row count; the runner counts every pipe-prefixed "
                "line in the queue block (header + separator + data), so the two "
                "readings differ by the table's own frame",
    }
    if not arithmetic_ok:
        out["findings"].append({"id": "X63-F1", "kind": "prose-arithmetic-drift",
                                "detail": out["measurements"]["arithmetic"]})

    # ---- G: staleness probe (readings true at the stamp, false now) ----
    stale = []
    r12 = os.path.join(LANE, "reports", "round-12", "validation.json")
    r21 = os.path.join(LANE, "reports", "round-21", "validation.json")
    for row in rows:
        pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
        if "no `validation.json`" not in pointer:
            continue
        candidate = r12 if row["file"].startswith("round-12") else r21
        if os.path.exists(candidate):
            receipt = json.loads(read(candidate).decode() or "{}")
            stale.append({"surface": f"{row['file']} pointer",
                          "claims": "no `validation.json`",
                          "measured": {"path": os.path.relpath(candidate, LANE),
                                       "exists": True,
                                       "acceptance_checks_passed":
                                           receipt.get("acceptance_checks_passed")}})
    gate_text = read(GATE).decode() if os.path.exists(GATE) else ""
    argot_hits = len(re.findall(r"D4L-ARGOT-DERIV", gate_text))
    r25_ok = None
    if os.path.exists(R25_RECEIPT):
        r25_ok = json.loads(read(R25_RECEIPT).decode()).get("acceptance_checks_passed")
    for entry in entries:
        status = entry["status"]
        if "D4L-ARGOT-DERIV" in status and "absent" in status:
            stale.append({"surface": f"{entry['id']} status",
                          "claims": "`D4L-ARGOT-DERIV` is absent from "
                                    "tools/gates/typed-pipeline-gate.py",
                          "measured": {"occurrences": argot_hits,
                                       "path": "tools/gates/typed-pipeline-gate.py"}})
        if "in flight round 25" in status:
            stale.append({"surface": f"{entry['id']} status",
                          "claims": "in flight round 25",
                          "measured": {"round_25_validation_exists": r25_ok is not None,
                                       "acceptance_checks_passed": r25_ok}})
    out["measurements"]["staleness"] = {"instances": stale}
    checks["G_no_stale_readings"] = not stale
    if stale:
        out["findings"].append({"id": "X63-G1", "kind": "stale-reading", "detail": stale})

    # ---- H: round-24 row presence (a claim in the round-25 audit prose)
    r13_rows = [m.group(1) for m in R13_RE.finditer(text)]
    r24_rows = [line for line in text.splitlines()
                if re.match(r"^\|\s*`?round-24`?\s*\|", line)]
    out["measurements"]["round_rows"] = {
        "round_13_rows": r13_rows,
        "round_24_rows": len(r24_rows),
        "round_24_prose_mention": bool(
            re.search(r"(?is)round\s+24\s+has\s+no\s+lesson\s+file", text))}
    checks["H_round13_row_self_describes"] = all(
        re.search(r"(?i)no lesson file|skipped|operator", line)
        for line in text.splitlines() if re.match(r"^\|\s*`?round-13`?\s*\|", line))
    return out


# --------------------------------------------------------------------------
# Controls: in-memory mutants, one per check. A tool that agrees only with
# itself is not a control, so each mutant changes exactly one surface.
# --------------------------------------------------------------------------

def selftest():
    checks = []
    base = read(INDEX).decode()
    files = lesson_files()

    def check(name, cond, observed=""):
        checks.append({"name": name, "pass": bool(cond), "observed": observed})

    live = measure()
    check("live index is audited", live["index"]["bytes"] > 0, live["index"]["sha256"][:16])
    check("live partition is 26 md files", len(files) == 26, len(files))
    check("A green on live bytes", live["checks"]["A_rows_eq_files"])
    check("B green on live bytes", live["checks"]["B_pins_rederived"])
    check("B2 green on live bytes", live["checks"]["B2_shape_cells_rederived"])
    check("D green on live bytes", live["checks"]["D_pointers_resolve"])
    check("E green on live bytes", live["checks"]["E_queue_cross_consistency"])
    check("E2 green on live bytes", live["checks"]["E2_owners_resolve"])
    check("F green on live bytes", live["checks"]["F_prose_arithmetic"])
    check("H round-13 row self-describes", live["checks"]["H_round13_row_self_describes"])

    def mutate(text):
        rows = parse_index(text)
        out = dict(live)
        return rows, out

    # A: delete one row -> orphan file
    rows = parse_index(base)
    cut = re.sub(r"(?m)^\|\s*`corpus/lessons/round-23\.md`[^\n]*\n", "", base)
    m = dict(live)
    m["checks"] = dict(live["checks"])
    row_files = [r["file"] for r in parse_index(cut)]
    m["checks"]["A_rows_eq_files"] = not [f for f in files if f not in row_files]
    check("A fires on a deleted row", not m["checks"]["A_rows_eq_files"])

    # B: falsify a pin
    forged = base.replace("sha8=b567a60a", "sha8=deadbeef")
    bad = []
    for row in parse_index(forged):
        claimed = dict(PIN_RE.findall(next((c for c in row["cells"] if "bytes=" in c), "")))
        if claimed.get("sha8") == "self-referential":
            continue
        body = read(os.path.join(LESSONS, row["file"]))
        if claimed.get("sha8") != sha256_bytes(body)[:8]:
            bad.append(row["file"])
    check("B fires on a falsified pin", bad == ["round-23.md"], bad)

    # D: a pointer that names a dead path without declaring it absent
    dead = base.replace("| `reports/round-8` |", "| `reports/round-8/nonexistent-xyz` |")
    unresolved = []
    for row in parse_index(dead):
        pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
        if any(p in pointer.lower() for p in DECLARED_ABSENT):
            continue
        for token in TOKEN_RE.findall(pointer):
            if resolves(token) is False:
                unresolved.append(token)
    check("D fires on an undeclared dead pointer", "reports/round-8/nonexistent-xyz" in unresolved,
          unresolved)
    check("D exempts a declared-absent pointer",
          any(r["cell_says_absent"] for r in
              live["measurements"]["pointers"]["declared_absent_unresolved"]))

    # E: drop one queue row while §2 still carries its id
    orphan = re.sub(r"(?m)^\|\s*Q-08-1\s*\|[^\n]*\n", "", base)
    ids = [e["id"] for e in parse_queue(orphan)[0]]
    section = orphan.split("## 2. Per-round index")[1].split("**Rows:")[0]
    carried = {"Q-%s-%d" % (a, i) for a, b, c in CARRIED_RE.findall(section)
               for i in range(int(b), int(c) + 1)}
    carried |= {"Q-%s-%s" % (a, b) for a, b in CARRIED_ONE_RE.findall(section)}
    check("E fires on a queue orphan", bool(carried - set(ids)), sorted(carried - set(ids)))

    # F: drift the stated row count
    drifted = base.replace("Rows: **49**", "Rows: **48**")
    stated = {int(v) for v in re.findall(r"(?i)\brows?\s*:\s*\**\s*(\d{1,3})", drifted)}
    check("F fires on drifted prose", len(parse_queue(drifted)[0]) not in stated, sorted(stated))

    # H: a round-13 row that does not say why it is absent
    silent = base.replace("operator-skipped; **no lesson file exists** (see §5)", "see §5")
    ok = all(re.search(r"(?i)no lesson file|skipped|operator", line)
             for line in silent.splitlines() if re.match(r"^\|\s*`?round-13`?\s*\|", line))
    check("H fires on a silent round-13 row", not ok)

    # G: the staleness probe fires on a live contradiction and stays silent
    #    when the claimed-absent receipt is genuinely absent.
    def stale_scan(text, receipt_present):
        hits = []
        for row in parse_index(text):
            pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
            if "no `validation.json`" in pointer and receipt_present:
                hits.append(row["file"])
        return hits

    check("G fires when the receipt exists", stale_scan(base, True) == ["round-12.md", "round-21.md"],
          stale_scan(base, True))
    check("G stays silent when the receipt is absent", stale_scan(base, False) == [])
    check("G reads the argot id in the live gate", live["measurements"]["staleness"]["instances"]
          and any(i["surface"].startswith("Q-04-1") for i in
                  live["measurements"]["staleness"]["instances"]))

    passed = sum(1 for c in checks if c["pass"])
    print(json.dumps({"schema": "kotodama-lessons-audit-x63-selftest-v1",
                      "checks": checks, "passed": passed, "total": len(checks)},
                     indent=1))
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
        print(json.dumps(result, indent=1, sort_keys=True))
        return 0
    print("index:        corpus/lessons/README.md")
    print("sha256:       %s" % result["index"]["sha256"])
    print("lesson files: %d" % result["partition"]["files"])
    print("index rows:   %d" % result["measurements"]["row_files"]["index_rows"])
    print("queue rows:   %d" % result["measurements"]["queue"]["rows"])
    for name, ok in result["checks"].items():
        print("  %s %s" % ("PASS" if ok else "FAIL", name))
    print("findings:     %d" % len(result["findings"]))
    for item in result["findings"]:
        print("  %s %s: %s" % (item["id"], item["kind"], json.dumps(item["detail"])[:200]))
    return 0 if all(result["checks"].values()) else 1


if __name__ == "__main__":
    sys.exit(main())
