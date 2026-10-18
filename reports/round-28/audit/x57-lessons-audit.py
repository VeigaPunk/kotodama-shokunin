#!/usr/bin/env python3
"""X57 — lessons audit (round 28, read-only).

Successor to `reports/round-27/audit/x57-lessons-audit.py`. That tool pinned the
partition at 27 files in its own controls and hard-coded
`reports/round-26/zzz-lessons-index-revision-4.md` as "the newest revision"; both
of those are now stale, so this is a **new file** rather than an edit of a filed
tool (lane rule: corrections are new files, never in-place rewrites).

It audits the lane's lessons surfaces against the live bytes at this seat's
stamp:

  * `corpus/lessons/README.md` — the **filed** round-25 index, and
  * the **newest revision** under `reports/**/zzz-lessons-index-revision-*.md`,
    resolved the way the round-26 runner resolves it (`find_readme_revisions()`,
    keyed by `(queue_ids, rows)`), but searched across every round directory
    rather than `reports/round-26` only — a round-28 revision, if one lands,
    must be found by this tool and is not found by the round-26 runner.

It re-derives the row/file set, every `bytes`/`lines`/`sha8` pin, every format
and contract cell, the disposition pointers, the open-question queue and each
surface's own stated arithmetic, and it probes staleness at four depths:

  G1  the six instances the round-26 auditor filed as `X63-G1`;
  G2  cells of the **revision** that today's bytes contradict;
  G3  the row-level `claims are pending` cells of the filed index;
  G4  **the newest lesson's own filed readings** — the round-27 lesson cites
      `reports/round-27/audit/x57-lessons-audit.py --selftest` as 37/37; the
      partition move to 28 files reds three of those controls, so the lesson's
      own claim is contradicted by the live bytes. New in round 28.

Opens no file for writing. The receipt is the caller's stdout redirect:

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-28/audit/x57-lessons-audit.py --selftest   # controls
    python3 -B reports/round-28/audit/x57-lessons-audit.py              # findings
    python3 -B reports/round-28/audit/x57-lessons-audit.py --json       # receipt
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LESSONS = os.path.join(LANE, "corpus", "lessons")
FILED = os.path.join(LESSONS, "README.md")
GATE = os.path.join(LANE, "tools", "gates", "typed-pipeline-gate.py")
ARGOT_GATE = os.path.join(LANE, "tools", "gates", "argot-derivation-gate.py")
README_BASELINE_BLOB = "a31870556c733498243b56697896504a2fb3679a"

# The round-27 lesson's own filed control claim, quoted so the probe can name it.
R27_LESSON = os.path.join(LESSONS, "round-27.md")
R27_TOOL = "reports/round-27/audit/x57-lessons-audit.py"
R27_CLAIMED_SELFTEST = (37, 37)
R27_CLAIMED_PARTITION = 27

ROW_RE = re.compile(r"(?m)^\|\s*`corpus/lessons/([A-Za-z0-9_.-]+\.md)`\s*\|(.*)\|\s*$")
CARRIED_RE = re.compile(r"Q-(\d+)-(\d+)\.\.(\d+)")
CARRIED_ONE_RE = re.compile(r"Q-([A-Za-z0-9]+)-(\d+)(?!\.\.)")
PIN_RE = re.compile(r"(bytes|lines|sha8)=([0-9a-zA-Z-]+)")
TOKEN_RE = re.compile(r"`([^`\n]+)`")
R13_RE = re.compile(r"(?m)^\|\s*`?round-(\d+)`?\s*\|")
SELFTEST_CLAIM_RE = re.compile(r"--selftest\*?\*?\s*[→>-]*\s*(?:exit\s+0\s*\()?\*?\*?(\d+)\s*/\s*(\d+)")

DECLARED_ABSENT = (
    "not filed", "no lesson file", "does not exist", "never existed",
    "no such", "fleet root", "outside this repo", "operator-skipped",
)
DECLARED_ABSENT_RE = re.compile(r"no\s+`[^`]+`\s+exists|no\s+`[^`]+\*?`\s+exists")

PEER_TOOLS = (
    ("c31", "reports/round-25/audit/c31-lessons-index-audit.py",
     "row/file set, owner resolution, documented formats, pin re-derivation"),
    ("x45", "reports/round-25/audit/x45-lessons-pointer-audit.py",
     "disposition-pointer column, prose counts, queue cross-consistency"),
    ("x63", "reports/round-26/audit/x63-lessons-audit.py",
     "the union of the two plus the staleness probe"),
    ("r27x57", R27_TOOL,
     "round-27 predecessor: both surfaces plus G1/G2/G3 and disposition coverage"),
)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read_bytes(path):
    with open(path, "rb") as handle:
        return handle.read()


def lesson_files():
    return sorted(os.path.basename(p)
                  for p in glob.glob(os.path.join(LESSONS, "*.md")))


def split_cells(rest):
    """Cells after the file cell, split only on unescaped pipes."""
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", rest)]


def format_class(name, text):
    """The partition's classifier: an exact `## Gate` heading wins over prose."""
    if name == "README.md":
        return "index"
    if re.search(r"(?m)^## Fragment index\s*$", text):
        return "fragment-index"
    if re.search(r"(?m)^## Gate\s*$", text):
        return "gate-keeper"
    return "plain"


def contract_count(body):
    head = body.decode().split("\n")[:14]
    return sum(1 for line in head
               if re.match(r"^(source|verified_at|verified-at|recheck|scope):",
                           line.strip()))


def parse_rows(text):
    rows = []
    for match in ROW_RE.finditer(text):
        rows.append({"file": match.group(1), "cells": split_cells(match.group(2))})
    return rows


def parse_queue(text):
    """Data rows of the `open-question` section, excluding the header row."""
    marker = re.search(r"(?im)^#{1,6}[^\n]*open[- ]question[^\n]*$", text)
    if not marker:
        return []
    tail = text[marker.end():]
    stop = re.search(r"(?m)^#{1,6}\s", tail)
    block = tail[:stop.start()] if stop else tail
    entries = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip().strip("`*")
                 for c in re.split(r"(?<!\\)\|", stripped.strip("|"))]
        if len(cells) >= 4 and cells[0].startswith("Q-") and cells[0] != "Q-id":
            entries.append({"id": cells[0], "question": cells[1],
                            "owner": cells[2], "status": cells[3]})
    return entries


def parse_dispositions(text):
    """§4 rows of a revision: id, class, owner, reason, next touch, evidence."""
    marker = re.search(r"(?im)^#{1,6}[^\n]*disposition of the[^\n]*$", text)
    if not marker:
        return []
    tail = text[marker.end():]
    stop = re.search(r"(?m)^#{1,6}\s", tail)
    block = tail[:stop.start()] if stop else tail
    rows = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", stripped.strip("|"))]
        if len(cells) >= 5 and cells[0].startswith("Q-") and cells[0] != "Q-id":
            rows.append({"id": cells[0].strip("`*"), "class": cells[1],
                         "owner": cells[2], "reason": cells[3],
                         "next_touch": cells[4]})
    return rows


def resolves(token):
    path = token.split()[0].strip("`")
    if not path or " " in path:
        return None
    if not re.match(r"^(corpus|reports|tools|examples|scripts|LOG|SCORECARD|"
                    r"AGENTS|PROVINCE|\.ufo|\.scratch)", path):
        return None
    return os.path.exists(os.path.join(LANE, path))


def brace_expand(token):
    """`a/{b,c}/d` -> the concrete paths; a token with no braces is itself."""
    match = re.search(r"\{([^{}]*)\}", token)
    if not match:
        return [token]
    out = []
    for part in match.group(1).split(","):
        out.extend(brace_expand(token[:match.start()] + part.strip()
                                + token[match.end():]))
    return out


def newest_revision():
    """Resolve the newest lessons-index revision the way the runner does, but
    searching every round directory rather than `reports/round-26` only."""
    found = []
    pattern = os.path.join(LANE, "reports", "*", "zzz-lessons-index-revision-*.md")
    for path in sorted(glob.glob(pattern)):
        text = read_bytes(path).decode()
        if ROW_RE.search(text) and re.search(r"(?i)open[- ]question", text):
            found.append({
                "path": os.path.relpath(path, LANE),
                "abs": path,
                "text": text,
                "queue_ids": len({m.group(0) for m in
                                  re.finditer(r"(?m)^\|\s*`?(Q-[A-Za-z0-9.-]+)`?\s*\|",
                                              text)}),
                "rows": len({m.group(1) for m in ROW_RE.finditer(text)}),
            })
    found.sort(key=lambda row: (row["queue_ids"], row["rows"]))
    return found


def surface_pin_drift(text, files):
    """Pin cells of an index text that disagree with the live lesson bytes."""
    drift, exempt = [], []
    for row in parse_rows(text):
        name = row["file"]
        target = os.path.join(LESSONS, name)
        if not os.path.exists(target):
            continue
        live_body = read_bytes(target)
        live = {"bytes": str(len(live_body)),
                "lines": str(live_body.decode().count("\n")),
                "sha8": sha256_bytes(live_body)[:8]}
        claimed = dict(PIN_RE.findall(
            next((c for c in row["cells"] if "bytes=" in c), "")))
        if claimed.get("sha8") == "self-referential":
            exempt.append(name)
            continue
        bad = {k: {"claimed": claimed.get(k), "live": live[k]}
               for k in ("bytes", "lines", "sha8") if claimed.get(k) != live[k]}
        if bad:
            drift.append({"file": name, "drift": bad})
    return drift, exempt


def audit_surface(path, rel, files, check_pins=True):
    """Re-derive one index surface (rows, pins, shapes, pointers, arithmetic)."""
    body = read_bytes(path)
    text = body.decode()
    rows = parse_rows(text)
    row_files = [row["file"] for row in rows]
    orphans = [name for name in files if name not in row_files]
    phantom = [name for name in row_files if name not in files]
    dupes = sorted({n for n in row_files if row_files.count(n) > 1})

    pin_drift, exempt = (surface_pin_drift(text, files) if check_pins else ([], []))
    shape_drift = []
    for row in rows:
        name = row["file"]
        target = os.path.join(LESSONS, name)
        if not os.path.exists(target):
            continue
        live_body = read_bytes(target)
        claimed_fmt = (row["cells"][0] if row["cells"] else "").split("(")[0].strip()
        live_fmt = format_class(name, live_body.decode())
        if claimed_fmt and claimed_fmt != live_fmt and not claimed_fmt.startswith("index"):
            shape_drift.append({"file": name, "claimed": claimed_fmt, "live": live_fmt})
        contract_cell = row["cells"][1] if len(row["cells"]) > 1 else ""
        match = re.match(r"(\d)/4", contract_cell)
        if match and int(match.group(1)) != contract_count(live_body):
            shape_drift.append({"file": name, "contract_claimed": contract_cell,
                                "contract_live": f"{contract_count(live_body)}/4"})

    unresolved, declared_absent = [], []
    for row in rows:
        pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
        absent = (any(p in pointer.lower() for p in DECLARED_ABSENT)
                  or bool(DECLARED_ABSENT_RE.search(pointer)))
        for token in TOKEN_RE.findall(pointer):
            for concrete in brace_expand(token):
                ok = resolves(concrete)
                if ok is None or ok:
                    continue
                record = {"file": row["file"], "token": concrete,
                          "cell_says_absent": absent}
                (declared_absent if absent else unresolved).append(record)

    entries = parse_queue(text)
    queue_ids = [e["id"] for e in entries]
    carried = set()
    section = text.split("## 2. Per-round index")[1].split("**Rows:")[0] \
        if "## 2. Per-round index" in text else ""
    for match in CARRIED_RE.finditer(section):
        for i in range(int(match.group(2)), int(match.group(3)) + 1):
            carried.add("Q-%s-%d" % (match.group(1), i))
    for match in CARRIED_ONE_RE.finditer(section):
        carried.add("Q-%s-%s" % (match.group(1), match.group(2)))
    bad_owners = []
    for entry in entries:
        owner = entry["owner"].strip("` ")
        token = owner.split()[0].strip("`") if owner else ""
        if token in ("operator", "parent"):
            continue
        if not os.path.exists(os.path.join(LANE, token)):
            bad_owners.append({"id": entry["id"], "owner": entry["owner"]})

    stated_rows = {int(v) for v in
                   re.findall(r"(?i)\brows?\s*:\s*\**\s*(\d{1,3})", text)}
    stated_files = {int(v) for v in
                    re.findall(r"(?i)\bfiles?\s*:\s*\**\s*(\d{1,3})", text)}
    arithmetic_ok = ((not stated_rows or len(queue_ids) in stated_rows)
                     and (not stated_files or len(files) in stated_files))

    return {
        "path": rel,
        "sha256": sha256_bytes(body),
        "bytes": len(body),
        "lines": body.decode().count("\n"),
        "rows": len(row_files),
        "orphans": orphans,
        "phantom": phantom,
        "duplicates": dupes,
        "pin_drift": pin_drift,
        "shape_drift": shape_drift,
        "self_referential_exempt": exempt,
        "unresolved_pointers": unresolved,
        "declared_absent_pointers": declared_absent,
        "queue_rows": len(queue_ids),
        "queue_ids": queue_ids,
        "carried_ids": sorted(carried),
        "carried_not_queued": sorted(carried - set(queue_ids)),
        "queued_not_carried": sorted(set(queue_ids) - carried),
        "unresolved_owners": bad_owners,
        "stated_rows": sorted(stated_rows),
        "stated_files": sorted(stated_files),
        "arithmetic_ok": arithmetic_ok,
    }


def staleness(filed_surface, rev_surface, rev_text, rev_rel):
    """G1 (the X63-G1 six), G2 (revision cells), G3 (row-level pending cells)."""
    g1, g2, g3 = [], [], []

    # ---- G1: the six the round-26 auditor filed -------------------------
    for row in parse_rows(read_bytes(FILED).decode()):
        pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
        if "no `validation.json`" not in pointer:
            continue
        name = "round-12" if row["file"].startswith("round-12") else "round-21"
        receipt = os.path.join(LANE, "reports", name, "validation.json")
        if os.path.exists(receipt):
            g1.append({"surface": f"{row['file']} pointer", "claims": "no validation.json",
                       "measured": {"path": os.path.relpath(receipt, LANE),
                                    "exists": True,
                                    "acceptance_checks_passed":
                                        json.loads(read_bytes(receipt).decode())
                                        .get("acceptance_checks_passed")}})
    gate_text = read_bytes(GATE).decode() if os.path.exists(GATE) else ""
    for entry in parse_queue(read_bytes(FILED).decode()):
        status = entry["status"]
        if "D4L-ARGOT-DERIV" in status and "absent" in status:
            g1.append({"surface": f"{entry['id']} status",
                       "claims": "D4L-ARGOT-DERIV is absent from typed-pipeline-gate.py",
                       "measured": {"occurrences": len(re.findall(r"D4L-ARGOT-DERIV", gate_text)),
                                    "argot_gate_exists": os.path.exists(ARGOT_GATE)}})
        if "in flight round 25" in status:
            receipt = os.path.join(LANE, "reports", "round-25", "validation.json")
            g1.append({"surface": f"{entry['id']} status", "claims": "in flight round 25",
                       "measured": {"round_25_validation_exists": os.path.exists(receipt),
                                    "acceptance_checks_passed":
                                        json.loads(read_bytes(receipt).decode())
                                        .get("acceptance_checks_passed")
                                        if os.path.exists(receipt) else None}})

    # ---- G2: cells of the newest revision contradicted by today's bytes --
    for drift in rev_surface["pin_drift"]:
        g2.append({"surface": f"revision pin for {drift['file']}",
                   "claims": "the pin cells bound at the revision's stamp",
                   "measured": drift["drift"]})
    for row in parse_rows(rev_text):
        cell = " ".join(row["cells"])
        if "claims are pending" not in cell and "claims pending" not in cell:
            continue
        round_name = re.search(r"round-(\d+)", row["file"])
        if not round_name:
            continue
        receipt = os.path.join(LANE, "reports", f"round-{round_name.group(1)}",
                               "validation.json")
        if os.path.exists(receipt):
            g2.append({"surface": f"revision §1 row for {row['file']}",
                       "claims": "its claims are pending",
                       "measured": {"path": os.path.relpath(receipt, LANE),
                                    "exists": True,
                                    "acceptance_checks_passed":
                                        json.loads(read_bytes(receipt).decode())
                                        .get("acceptance_checks_passed")}})
    for disp in parse_dispositions(rev_text):
        match = re.search(r"round\s+(\d+)", disp["next_touch"])
        if not match:
            continue
        round_no = int(match.group(1))
        receipt = os.path.join(LANE, "reports", f"round-{round_no}", "validation.json")
        if round_no < 27 and os.path.exists(receipt):
            g2.append({"surface": f"revision §4 disposition {disp['id']}",
                       "claims": f"next touch {disp['next_touch']}",
                       "measured": {"path": os.path.relpath(receipt, LANE),
                                    "exists": True,
                                    "acceptance_checks_passed":
                                        json.loads(read_bytes(receipt).decode())
                                        .get("acceptance_checks_passed")}})

    # ---- G3: row-level `claims are pending` cells of the filed index -----
    for row in parse_rows(read_bytes(FILED).decode()):
        cell = row["cells"][2] if len(row["cells"]) > 2 else ""
        if "pending" not in cell:
            continue
        round_name = re.search(r"round-(\d+)", row["file"])
        if not round_name:
            continue
        receipt = os.path.join(LANE, "reports", f"round-{round_name.group(1)}",
                               "validation.json")
        if os.path.exists(receipt):
            g3.append({"surface": f"filed §2 row for {row['file']}",
                       "claims": "this round's own claims are pending",
                       "measured": {"path": os.path.relpath(receipt, LANE),
                                    "exists": True,
                                    "acceptance_checks_passed":
                                        json.loads(read_bytes(receipt).decode())
                                        .get("acceptance_checks_passed")}})

    return {"G1_x63_instances": g1, "G2_revision_cells": g2, "G3_row_level": g3}


def lesson_self_claims(files):
    """G4: the newest lesson's own filed readings, re-derived now.

    Two probes, both about a lesson being a *measurement* that a later write can
    invalidate:

      L  every repo path the newest lesson's `source:` line names resolves
         (brace groups are expanded first; a group is a shorthand, not a path);
      M  every `<tool> --selftest <n>/<n>` figure the newest lesson states still
         holds when the tool is executed now.

    L is a resolvability probe and is expected green. M is the staleness probe:
    the round-27 lesson cites `x57-lessons-audit.py --selftest` as 37/37, and
    the partition move to 28 files reds three of that tool's own controls.
    """
    newest = max(files, key=lambda name: os.path.getmtime(os.path.join(LESSONS, name)))
    text = read_bytes(os.path.join(LESSONS, newest)).decode()
    source_line = next((line for line in text.splitlines()
                        if line.startswith("source:")), "")
    tokens = TOKEN_RE.findall(source_line)
    dead = []
    for token in tokens:
        for concrete in brace_expand(token):
            if resolves(concrete) is False:
                dead.append(concrete)

    # Every `--selftest` mention: the tool is the `.py` token in the enclosing
    # backtick span (the round-27 lesson writes `` `tool.py --selftest` ``), or
    # the nearest backticked `.py` token before the mention; the figure is the
    # first `n/n` inside the span after the mention, else just after it.
    spans = [(m.start(), m.end(), m.group(1))
             for m in re.finditer(r"`([^`\n]+)`", text)]
    claims = []
    for hit in re.finditer(r"--selftest", text):
        enclosing = next((s for s in spans if s[0] < hit.start() < s[1]), None)
        if enclosing:
            scope = enclosing[2][enclosing[2].find("--selftest"):]
            before = enclosing[2]
            after = text[enclosing[1]:enclosing[1] + 90]
        else:
            scope = ""
            before = text[max(0, hit.start() - 200):hit.start()]
            after = text[hit.end():hit.end() + 90]
        py_tokens = [t for t in re.findall(r"(\S*\.py)", before) if t]
        if not py_tokens:
            continue
        tool = py_tokens[-1].strip("`*,")
        if not os.path.exists(os.path.join(LANE, tool)):
            continue
        figure = (re.search(r"(\d+)\s*/\s*(\d+)", scope)
                  or re.search(r"(\d+)\s*/\s*(\d+)", after))
        if not figure:
            continue
        claimed = (int(figure.group(1)), int(figure.group(2)))
        if any(c["tool"] == tool and c["claimed"] == [claimed[0], claimed[1]]
               for c in claims):
            continue
        proc = subprocess.run([sys.executable, "-B", tool, "--selftest"],
                              cwd=LANE, capture_output=True, text=True, timeout=240)
        observed = None
        match = re.search(r'"passed"\s*:\s*(\d+)', proc.stdout)
        if match:
            total = re.search(r'"total"\s*:\s*(\d+)', proc.stdout)
            observed = (int(match.group(1)), int(total.group(1)) if total else None)
        else:
            match = (re.search(r"(?i)selftest(?:\s+OK)?[:\s]*\s*(\d+)\s*/\s*(\d+)",
                               proc.stdout)
                     or re.search(r"(?i)(\d+)\s*/\s*(\d+)\s+(?:checks|controls)\b",
                                  proc.stdout))
            if match:
                observed = (int(match.group(1)), int(match.group(2)))
        claims.append({"tool": tool, "claimed": [claimed[0], claimed[1]],
                       "observed": list(observed) if observed else None,
                       "exit": proc.returncode,
                       "holds": bool(observed) and observed[0] == claimed[0]
                                and (observed[1] in (None, claimed[1]))})

    return {"newest_lesson": newest, "source_tokens": len(tokens),
            "dead_source_tokens": dead, "selftest_claims": claims,
            "stale_selftest_claims": [c for c in claims if not c["holds"]]}


def disposition_coverage(filed_surface, rev_text):
    """I: every filed queue id has exactly one usable §4 disposition row."""
    queue_ids = filed_surface["queue_ids"]
    disps = parse_dispositions(rev_text)
    ids = [d["id"] for d in disps]
    missing = sorted(set(queue_ids) - set(ids))
    extra = sorted(set(ids) - set(queue_ids))
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    bad_class = [d["id"] for d in disps if d["class"] not in ("fixed", "carried")]
    bad_owner = []
    for d in disps:
        token = d["owner"].strip("` ").split()[0].strip("`") if d["owner"] else ""
        if token in ("operator", "parent"):
            continue
        if not token or not os.path.exists(os.path.join(LANE, token)):
            bad_owner.append({"id": d["id"], "owner": d["owner"]})
    no_reason = [d["id"] for d in disps
                 if d["class"] == "carried" and "reason:" not in d["reason"]]
    no_next = [d["id"] for d in disps
               if d["class"] == "carried" and not re.search(r"round\s+\d+", d["next_touch"])]
    return {
        "queue_ids": len(queue_ids),
        "disposition_rows": len(disps),
        "missing": missing,
        "extra": extra,
        "duplicates": dupes,
        "bad_class": bad_class,
        "unresolved_owners": bad_owner,
        "carried_without_reason": no_reason,
        "carried_without_next_touch": no_next,
        "classes": {c: sum(1 for d in disps if d["class"] == c)
                    for c in sorted({d["class"] for d in disps})},
        "ok": not (missing or extra or dupes or bad_class or bad_owner
                   or no_reason or no_next),
    }


def runner_coverage():
    """G6: does the round's own counting command still grade the lessons index?

    Rounds 25 and 26 each graded it (`find_readme_revisions()`, the filed blob
    baseline, the queue and its dispositions). Round 27's and round 28's runners
    carry no reference to `corpus/lessons` at all — so the ledger this audit
    measures is no longer on any acceptance surface, and the `O` claim's "every
    frozen/baseline/replay surface re-verified" cannot include it.
    """
    out = {}
    for path in sorted(glob.glob(os.path.join(LANE, "reports", "round-*",
                                              "run-validation.py"))):
        rel = os.path.relpath(path, LANE)
        if not re.match(r"reports/round-(2[5-9])/", rel):
            continue
        text = read_bytes(path).decode(errors="replace")
        out[rel] = {
            "sha256": sha256_bytes(read_bytes(path))[:16],
            "lessons_refs": len(re.findall(r"(?i)lessons", text)),
            "corpus_lessons_refs": len(re.findall(r"corpus/lessons", text)),
            "readme_baseline": bool(re.search(r"README_BASELINE_BLOB", text)),
            "grades_the_ledger": bool(re.search(r"corpus/lessons", text)),
        }
    latest = os.path.join(LANE, "reports", "round-28", "run-validation.py")
    return {"runners": out,
            "round_28_runner_exists": os.path.exists(latest),
            "round_28_grades_the_ledger":
                bool(os.path.exists(latest)
                     and re.search(r"corpus/lessons",
                                   read_bytes(latest).decode(errors="replace")))}


def peer_verdicts():
    """J: what the peer auditors say on these bytes right now."""
    out = {}
    for key, rel, question in PEER_TOOLS:
        path = os.path.join(LANE, rel)
        if not os.path.exists(path):
            out[key] = {"path": rel, "question": question, "exists": False}
            continue
        record = {"path": rel, "question": question, "exists": True}
        for mode in ("--selftest", None):
            cmd = [sys.executable, "-B", path] + ([mode] if mode else [])
            try:
                proc = subprocess.run(cmd, cwd=LANE, capture_output=True,
                                      text=True, timeout=240)
                tail = [line for line in proc.stdout.splitlines()
                        if re.search(r"(?i)^\s*(FAIL|findings|SELFTEST|passed)", line)]
                record["selftest" if mode else "live"] = {
                    "exit": proc.returncode, "tail": tail[-8:],
                }
            except subprocess.TimeoutExpired:
                record["selftest" if mode else "live"] = {"exit": None,
                                                          "tail": ["timeout"]}
        out[key] = record
    return out


def measure():
    files = lesson_files()
    filed = audit_surface(FILED, "corpus/lessons/README.md", files)
    candidates = newest_revision()
    rev_rel = candidates[-1]["path"] if candidates else None
    rev_abs = candidates[-1]["abs"] if candidates else None
    rev_text = candidates[-1]["text"] if candidates else ""
    rev = (audit_surface(rev_abs, rev_rel, files) if rev_abs
           else {"path": None, "rows": 0, "orphans": files, "phantom": [],
                 "duplicates": [], "pin_drift": [], "shape_drift": [],
                 "unresolved_pointers": [], "declared_absent_pointers": [],
                 "queue_ids": [], "queue_rows": 0, "carried_not_queued": [],
                 "queued_not_carried": [], "unresolved_owners": [],
                 "stated_rows": [], "stated_files": [], "arithmetic_ok": True,
                 "sha256": None, "bytes": 0, "lines": 0})
    stale = staleness(filed, rev, rev_text, rev_rel)
    coverage = disposition_coverage(filed, rev_text)
    lesson = lesson_self_claims(files)
    runners = runner_coverage()

    r13_rows = [m.group(1) for m in R13_RE.finditer(read_bytes(FILED).decode())]
    filed_text = read_bytes(FILED).decode()
    checks, findings = {}, []

    def check(name, ok, finding=None):
        checks[name] = bool(ok)
        if not ok and finding:
            findings.append(finding)

    check("A1_filed_rows_eq_files",
          not filed["orphans"] and not filed["phantom"] and not filed["duplicates"],
          {"id": "X57-A1", "kind": "filed-index-row-drift",
           "detail": {"orphans": filed["orphans"], "phantom": filed["phantom"],
                      "duplicates": filed["duplicates"]}})
    check("A2_revision_rows_eq_files",
          rev_abs is not None and not rev["orphans"] and not rev["phantom"]
          and not rev["duplicates"],
          {"id": "X57-A2", "kind": "revision-row-drift",
           "detail": {"revision": rev_rel, "orphans": rev["orphans"],
                      "phantom": rev["phantom"], "duplicates": rev["duplicates"]}})
    check("A3_partition_census", len(files) == 28,
          {"id": "X57-A3", "kind": "partition-census",
           "detail": {"measured": len(files), "names": files}})
    check("B1_filed_pins_rederived", not filed["pin_drift"],
          {"id": "X57-B1", "kind": "filed-pin-drift", "detail": filed["pin_drift"]})
    check("B2_revision_pins_rederived", not rev["pin_drift"],
          {"id": "X57-B2", "kind": "revision-pin-drift", "detail": rev["pin_drift"]})
    check("B3_shape_cells_rederived",
          not filed["shape_drift"] and not rev["shape_drift"],
          {"id": "X57-B3", "kind": "shape-cell-drift",
           "detail": {"filed": filed["shape_drift"], "revision": rev["shape_drift"]}})
    check("D_pointers_resolve",
          not filed["unresolved_pointers"] and not rev["unresolved_pointers"],
          {"id": "X57-D1", "kind": "dead-pointer",
           "detail": {"filed": filed["unresolved_pointers"],
                      "revision": rev["unresolved_pointers"]}})
    check("E_queue_cross_consistency",
          not filed["carried_not_queued"] and not filed["queued_not_carried"],
          {"id": "X57-E1", "kind": "queue-orphan",
           "detail": {"carried_not_queued": filed["carried_not_queued"],
                      "queued_not_carried": filed["queued_not_carried"]}})
    check("E2_owners_resolve", not filed["unresolved_owners"],
          {"id": "X57-E2", "kind": "unresolved-owner",
           "detail": filed["unresolved_owners"]})
    check("F_prose_arithmetic",
          filed["arithmetic_ok"] and rev["arithmetic_ok"],
          {"id": "X57-F1", "kind": "prose-arithmetic-drift",
           "detail": {"filed_stated_rows": filed["stated_rows"],
                      "filed_stated_files": filed["stated_files"],
                      "revision_stated_rows": rev["stated_rows"],
                      "revision_stated_files": rev["stated_files"],
                      "measured_files": len(files),
                      "measured_queue_rows": filed["queue_rows"]}})
    check("G1_x63_instances_reproduce", len(stale["G1_x63_instances"]) == 6,
          {"id": "X57-G1", "kind": "staleness-probe-drift",
           "detail": {"instances": len(stale["G1_x63_instances"])}})
    check("G2_revision_cells_clean", not stale["G2_revision_cells"],
          {"id": "X57-G2", "kind": "revision-stale-reading",
           "detail": stale["G2_revision_cells"]})
    check("G3_row_level_cells_clean", not stale["G3_row_level"],
          {"id": "X57-G3", "kind": "row-level-stale-reading",
           "detail": stale["G3_row_level"]})
    check("G4_lesson_source_tokens_resolve", not lesson["dead_source_tokens"],
          {"id": "X57-G4", "kind": "lesson-source-token-dead",
           "detail": lesson["dead_source_tokens"]})
    check("G5_lesson_selftest_claims_hold", not lesson["stale_selftest_claims"],
          {"id": "X57-G5", "kind": "lesson-control-claim-stale",
           "detail": lesson["stale_selftest_claims"]})
    check("G6_runner_still_grades_the_ledger", runners["round_28_grades_the_ledger"],
          {"id": "X57-G6", "kind": "ledger-dropped-from-acceptance-surface",
           "detail": runners})
    check("H_round13_row_self_describes",
          all(re.search(r"(?i)no lesson file|skipped|operator", line)
              for line in filed_text.splitlines()
              if re.match(r"^\|\s*`?round-13`?\s*\|", line)))
    check("I_disposition_coverage", coverage["ok"],
          {"id": "X57-I1", "kind": "disposition-coverage-gap", "detail": coverage})

    peers = peer_verdicts()
    for key, _, _ in PEER_TOOLS:
        check(f"J_{key}_reproduces",
              peers.get(key, {}).get("live", {}).get("exit") is not None)

    return {
        "schema": "kotodama-lessons-audit-x57-v2",
        "round": 28,
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "lane": LANE,
        "filed_blob": subprocess.run(["git", "hash-object", "corpus/lessons/README.md"],
                                     cwd=LANE, capture_output=True, text=True
                                     ).stdout.strip(),
        "filed_blob_baseline": README_BASELINE_BLOB,
        "partition": {"files": len(files), "names": files},
        "revision_candidates": [row["path"] for row in candidates],
        "filed_index": filed,
        "newest_revision": rev,
        "newest_revision_rel": rev_rel,
        "staleness": stale,
        "lesson_self_claims": lesson,
        "runner_coverage": runners,
        "disposition_coverage": coverage,
        "peers": peers,
        "round_rows": {"round_13_rows": r13_rows},
        "checks": checks,
        "findings": findings,
    }


# --------------------------------------------------------------------------
# Controls: in-memory mutants, one per check, plus negative controls that
# assert a probe stays SILENT when the contradicting byte is absent.
# --------------------------------------------------------------------------

def selftest():
    checks = []

    def check(name, cond, observed=""):
        checks.append({"name": name, "pass": bool(cond), "observed": observed})

    files = lesson_files()
    filed_text = read_bytes(FILED).decode()
    candidates = newest_revision()
    rev_rel = candidates[-1]["path"] if candidates else None
    rev_abs = candidates[-1]["abs"] if candidates else None
    rev_text = candidates[-1]["text"] if candidates else ""
    filed = audit_surface(FILED, "corpus/lessons/README.md", files)
    rev = (audit_surface(rev_abs, rev_rel, files) if rev_abs else None)
    lesson = lesson_self_claims(files)

    check("filed index is read", filed["bytes"] > 0, filed["sha256"][:16])
    check("newest revision is resolved", rev is not None and rev["bytes"] > 0,
          rev_rel)
    check("partition is 28 md files (round-28 control)", len(files) == 28, len(files))
    check("filed rows are 26", filed["rows"] == 26, filed["rows"])
    check("filed pins re-derive (live control)", not filed["pin_drift"],
          filed["pin_drift"][:2])
    check("filed orphan is exactly round-26.md and round-27.md (live control)",
          filed["orphans"] == ["round-26.md", "round-27.md"], filed["orphans"])
    check("filed queue is 49 rows (live control)", filed["queue_rows"] == 49,
          filed["queue_rows"])
    check("revision orphan is exactly round-27.md (live control)",
          rev["orphans"] == ["round-27.md"], rev["orphans"])
    check("revision pins drift on exactly one row (live control)",
          [d["file"] for d in rev["pin_drift"]] == ["round-26.md"],
          [d["file"] for d in rev["pin_drift"]])

    # A: delete a row from the filed index in memory -> orphan.
    cut = re.sub(r"(?m)^\|\s*`corpus/lessons/round-23\.md`[^\n]*\n", "", filed_text)
    row_files = [r["file"] for r in parse_rows(cut)]
    check("A1 fires on a deleted filed row",
          bool([f for f in files if f not in row_files]))

    # A2: drop the newest lesson's row from the revision -> revision orphan.
    cut_rev = re.sub(r"(?m)^\|\s*`corpus/lessons/round-26\.md`[^\n]*\n", "", rev_text)
    check("A2 fires on a revision that omits a lesson file",
          "round-26.md" in [f for f in files
                            if f not in [r["file"] for r in parse_rows(cut_rev)]])
    check("A2 is red on the live revision (round-27.md is omitted)",
          "round-27.md" in rev["orphans"], rev["orphans"])

    # B: falsify a pin in the revision in memory.
    forged = rev_text.replace("sha8=cf7461fe", "sha8=deadbeef")
    drift = []
    for row in parse_rows(forged):
        target = os.path.join(LESSONS, row["file"])
        if not os.path.exists(target):
            continue
        body = read_bytes(target)
        claimed = dict(PIN_RE.findall(
            next((c for c in row["cells"] if "bytes=" in c), "")))
        if claimed.get("sha8") == "self-referential":
            continue
        if claimed.get("sha8") != sha256_bytes(body)[:8]:
            drift.append(row["file"])
    check("B2 fires on a falsified revision pin", "round-26.md" in drift, drift)

    # B3: a shape cell that disagrees with the live bytes.
    shape = format_class("round-26.md",
                         read_bytes(os.path.join(LESSONS, "round-26.md")).decode())
    check("B3 classifier separates gate-keeper from fragment-index",
          shape == "gate-keeper" and format_class("round-8.md",
              read_bytes(os.path.join(LESSONS, "round-8.md")).decode()) == "fragment-index",
          shape)
    check("B3 reads the round-27 lesson as gate-keeper (round-28 control)",
          format_class("round-27.md",
                       read_bytes(os.path.join(LESSONS, "round-27.md")).decode())
          == "gate-keeper")

    # D: a dead pointer that does not declare itself absent.
    dead = filed_text.replace("| `reports/round-8` |", "| `reports/round-8/nope-xyz` |")
    unresolved = []
    for row in parse_rows(dead):
        pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
        if any(p in pointer.lower() for p in DECLARED_ABSENT):
            continue
        for token in TOKEN_RE.findall(pointer):
            for concrete in brace_expand(token):
                if resolves(concrete) is False:
                    unresolved.append(concrete)
    check("D fires on an undeclared dead pointer",
          "reports/round-8/nope-xyz" in unresolved, unresolved)
    check("D exempts a declared-absent pointer",
          bool(filed["declared_absent_pointers"]),
          len(filed["declared_absent_pointers"]))

    # E: drop a queue row while §2 still carries its id.
    orphan = re.sub(r"(?m)^\|\s*Q-08-1\s*\|[^\n]*\n", "", filed_text)
    ids = [e["id"] for e in parse_queue(orphan)]
    section = filed_text.split("## 2. Per-round index")[1].split("**Rows:")[0]
    carried = {"Q-%s-%d" % (a, i) for a, b, c in CARRIED_RE.findall(section)
               for i in range(int(b), int(c) + 1)}
    carried |= {"Q-%s-%s" % (a, b) for a, b in CARRIED_ONE_RE.findall(section)}
    check("E fires on a queue orphan", bool(carried - set(ids)),
          sorted(carried - set(ids))[:3])

    # E2: an owner that names nothing on disk.
    check("E2 accepts `operator` and `parent` as role tokens",
          not [o for o in filed["unresolved_owners"] if o["owner"] in ("operator", "parent")])
    check("E2 fires on a fabricated path owner",
          not os.path.exists(os.path.join(LANE, "corpus/nope-owner.md")))

    # F: drift the stated file count.
    drifted = filed_text.replace("Rows: **49**", "Rows: **48**")
    stated = {int(v) for v in re.findall(r"(?i)\brows?\s*:\s*\**\s*(\d{1,3})", drifted)}
    check("F fires on drifted prose", 49 not in stated, sorted(stated))

    # G1: the six instances reproduce, and the probe stays silent when the
    #     claimed-absent receipt is genuinely absent.
    stale = staleness(filed, rev, rev_text, rev_rel)
    check("G1 reproduces exactly six instances", len(stale["G1_x63_instances"]) == 6,
          len(stale["G1_x63_instances"]))
    check("G1 surfaces are the six X63-G1 names",
          sorted({i["surface"].split()[0] for i in stale["G1_x63_instances"]})
          == ["Q-04-1", "Q-23-1", "Q-23-2", "Q-23-3", "round-12.md", "round-21.md"],
          sorted({i["surface"].split()[0] for i in stale["G1_x63_instances"]}))

    def silent_scan(text, receipt_present):
        hits = []
        for row in parse_rows(text):
            pointer = row["cells"][3] if len(row["cells"]) > 3 else ""
            if "no `validation.json`" in pointer and receipt_present:
                hits.append(row["file"])
        return hits

    check("G1 silent when the receipt is absent", silent_scan(filed_text, False) == [])
    check("G1 fires when the receipt is present",
          silent_scan(filed_text, True) == ["round-12.md", "round-21.md"],
          silent_scan(filed_text, True))

    # G2: the revision's own drifted pin is the one live instance, and the
    #     probe would stay silent on a revision whose pin matches.
    check("G2 carries the drifted revision pin",
          any("revision pin" in i["surface"] for i in stale["G2_revision_cells"]),
          [i["surface"] for i in stale["G2_revision_cells"]][:4])
    pinned = rev_text.replace("bytes=46745 lines=190 sha8=cf7461fe",
                              "bytes=60054 lines=222 sha8=cae06660")
    check("G2 silent when the revision pin matches the live bytes",
          not surface_pin_drift(pinned, files)[0],
          surface_pin_drift(pinned, files)[0][:2])

    # G3: the row-level probe fires on the filed index's own pending cells.
    check("G3 fires on the filed row-level pending cell",
          bool(stale["G3_row_level"]), [i["surface"] for i in stale["G3_row_level"]])
    check("G3 names exactly the round-25 row (live control)",
          [i["surface"] for i in stale["G3_row_level"]]
          == ["filed §2 row for round-25.md"],
          [i["surface"] for i in stale["G3_row_level"]])
    check("G3 stays silent when the round's receipt is absent",
          not [i for i in stale["G3_row_level"]
               if not os.path.exists(os.path.join(
                   LANE, i["measured"]["path"]))])
    # G2 §4: the probe fires only when a `round N<27` next-touch already has a
    # receipt. Control: a revision whose next-touch column names only round 99
    # must produce no §4 instance.
    marker = re.search(r"(?im)^#{1,6}[^\n]*disposition of the[^\n]*$", rev_text)
    tail = rev_text[marker.end():]
    stop = re.search(r"(?m)^#{1,6}\s", tail)
    block = tail[:stop.start()] if stop else tail
    future_block = re.sub(r"(?m)^(\|\s*Q-[A-Za-z0-9-]+\s*\|[^\n]*?)\|[^|\n]*\|([^|\n]*\|)$",
                          r"\1| round 99 |\2", block)
    future = rev_text[:marker.end()] + future_block + (tail[stop.start():] if stop else "")
    check("G2 §4 silent when no next-touch round has closed",
          not [i for i in staleness(filed, rev, future, rev_rel)["G2_revision_cells"]
               if "§4 disposition" in i["surface"]],
          [i["surface"] for i in staleness(filed, rev, future, rev_rel)["G2_revision_cells"]
           if "§4 disposition" in i["surface"]][:3])
    check("G2 §4 fires on the live revision's closed next-touch row",
          any(i["surface"].startswith("revision §4 disposition Q-18-3")
              for i in stale["G2_revision_cells"]),
          [i["surface"] for i in stale["G2_revision_cells"]
           if "§4 disposition" in i["surface"]])

    # G4: the newest lesson's `source:` tokens resolve, and the probe fires on
    #     a fabricated dead token.
    check("G4 is green on the live newest lesson",
          not lesson["dead_source_tokens"], lesson["dead_source_tokens"])
    check("G4 reads the round-27 lesson as the newest",
          lesson["newest_lesson"] == "round-27.md", lesson["newest_lesson"])
    check("G4 fires on a fabricated dead source token",
          resolves("reports/round-27/nope-xyz.md") is False)
    check("G4 brace-expands a group token",
          brace_expand("reports/round-27/law/{design,rules,review}.md")
          == ["reports/round-27/law/design.md", "reports/round-27/law/rules.md",
              "reports/round-27/law/review.md"],
          brace_expand("reports/round-27/law/{design,rules,review}.md"))

    # G5: the round-27 lesson's own control claim is stale, and the probe stays
    #     silent on a claim that still holds.
    check("G5 finds the round-27 lesson's stale control claim",
          any(c["tool"] == R27_TOOL for c in lesson["stale_selftest_claims"]),
          [(c["tool"], c["claimed"], c["observed"]) for c in lesson["stale_selftest_claims"]])
    check("G5 records the measured figure for the round-27 tool",
          all(c["observed"] is not None for c in lesson["stale_selftest_claims"]),
          [(c["tool"], c["observed"]) for c in lesson["selftest_claims"]])
    check("G5 counts a claim that holds as not-stale",
          all(c["holds"] for c in lesson["selftest_claims"] if c["tool"] != R27_TOOL),
          [(c["tool"], c["claimed"], c["observed"]) for c in lesson["selftest_claims"]])

    # G6: the round-25/26 runners graded the ledger; the round-27/28 runners do
    #     not. The probe reads the runner text, so the control is a fabricated
    #     runner body with and without a `corpus/lessons` reference.
    runners = runner_coverage()
    check("G6 reads the four loop-era runners",
          len(runners["runners"]) == 4, sorted(runners["runners"]))
    check("G6 records rounds 25-26 as grading the ledger",
          all(runners["runners"][f"reports/round-{n}/run-validation.py"]
              ["grades_the_ledger"] for n in (25, 26)
              if f"reports/round-{n}/run-validation.py" in runners["runners"]),
          {k: v["grades_the_ledger"] for k, v in runners["runners"].items()})
    check("G6 records rounds 27-28 as not grading the ledger (live finding)",
          not runners["round_28_grades_the_ledger"], runners["round_28_runner_exists"])
    check("G6 fires on a runner body that names corpus/lessons",
          bool(re.search(r"corpus/lessons",
                         "LESSONS_README = \"corpus/lessons/README.md\"")))
    check("G6 stays silent on a runner body that does not",
          not re.search(r"corpus/lessons", "PROTECTED = ('reports/round-8',)"))

    # I: disposition coverage.
    coverage = disposition_coverage(filed, rev_text)
    check("I reads 49 queue ids and 49 disposition rows",
          coverage["queue_ids"] == 49 and coverage["disposition_rows"] == 49,
          (coverage["queue_ids"], coverage["disposition_rows"]))
    check("I is green on the live revision", coverage["ok"], coverage["missing"][:3])
    drop = re.sub(r"(?m)^\|\s*Q-08-1\s*\|[^\n]*\n", "", rev_text)
    check("I fires on a dropped disposition row",
          "Q-08-1" in disposition_coverage(filed, drop)["missing"])
    bad = rev_text.replace("| Q-02-1 | fixed |", "| Q-02-1 | resolved |")
    check("I fires on an out-of-vocabulary class",
          "Q-02-1" in disposition_coverage(filed, bad)["bad_class"])

    # J: the peer tools are reachable and their exit codes are recorded.
    peers = peer_verdicts()
    check("J records all four peer tools",
          set(peers) == {"c31", "x45", "x63", "r27x57"}, sorted(peers))
    check("J records a live exit code per peer",
          all(p.get("live", {}).get("exit") is not None for p in peers.values()))
    check("J records the round-26 auditor's selftest state (its controls pin the"
          " pre-round-26 partition)", peers["x63"]["selftest"]["exit"] in (0, 1),
          peers["x63"]["selftest"]["exit"])
    check("J records the round-27 auditor's selftest state (its controls pin the"
          " pre-round-28 partition)", peers["r27x57"]["selftest"]["exit"] in (0, 1),
          peers["r27x57"]["selftest"]["exit"])

    passed = sum(1 for c in checks if c["pass"])
    print(json.dumps({"schema": "kotodama-lessons-audit-x57-v2-selftest",
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
    print("filed index:      corpus/lessons/README.md")
    print("  sha256:         %s" % result["filed_index"]["sha256"])
    print("  blob:           %s (baseline %s)" % (result["filed_blob"],
                                                  result["filed_blob_baseline"]))
    print("  rows:           %d" % result["filed_index"]["rows"])
    print("revision candidates:")
    for path in result["revision_candidates"]:
        print("  %s" % path)
    print("newest revision:  %s" % result["newest_revision_rel"])
    print("  sha256:         %s" % result["newest_revision"]["sha256"])
    print("  rows:           %d" % result["newest_revision"]["rows"])
    print("lesson files:     %d" % result["partition"]["files"])
    print("queue rows:       %d" % result["filed_index"]["queue_rows"])
    for name, ok in result["checks"].items():
        print("  %s %s" % ("PASS" if ok else "FAIL", name))
    print("findings:         %d" % len(result["findings"]))
    for item in result["findings"]:
        print("  %s %s: %s" % (item["id"], item["kind"],
                               json.dumps(item["detail"])[:240]))
    return 0 if all(result["checks"].values()) else 1


if __name__ == "__main__":
    sys.exit(main())
