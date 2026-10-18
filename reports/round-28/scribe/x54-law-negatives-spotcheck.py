#!/usr/bin/env python3
"""X54 (round 28) — independent spot-check of the register law's NEGATIVES.

Assignment (verbatim): "SCRIBE X54: spot-check (law negatives independently)."

Claim under test: **D / depth** — round-28 claim D `after_required` reads "The
law gains a replay/checking leg: ... a tampered row is a named finding
(D4L-LAW-* class); RL-4 fixed (the components declare packet_keys; the records
reach the packet; the named-holds set updated honestly)" (`reports/round-28/
claims.json`). Its `before` carries round 27's **RL-1**: "a tampered law row
(`force: 'no-such-force'`) emits the same 12 findings as a clean one".

This seat is a **spot-check**, not the round's verdict. It measures; it
adjudicates nothing and blesses no fix.

## What is measured, and by which route

The claim is a *negative* claim: it says tampering must be **caught**. A
negative claim is only as good as the negative controls it fails closed on, so
this instrument measures four things no single positive run can:

1. **the clean packet is silent** — the law checker must emit **zero** law
   findings on the delivered bytes. A checker that fires on everything would
   otherwise pass every tamper route. (Route: run the checker on the delivered
   packet, unmodified.)
2. **each tamper route is caught, by name** — for every route below the checker
   must emit at least one finding whose id matches the claim's named class
   (`D4L-LAW-*`) and whose subject names the tampered row. (Route: this seat's
   **own** text transform of the delivered bytes, never the D seat's probe
   files; each tampered packet is written under gitignored scratch.)
3. **the tamper is isolated** — a law tamper must not perturb the rest of the
   projection: the non-law finding count of every tampered packet must equal the
   clean packet's. This catches a checker that "catches" tampering by breaking
   the packet. (Route: `tools/d2-typed-labels.py --packet <tampered>`.)
4. **a prose change is not a structural finding** — the false-positive control.
   Rewriting a row's `act`/`consequence` prose must leave the structural law
   verdict unchanged, or the checker is reading prose as structure.

The checker is discovered, not named: this instrument greps the live tree for
the finding class the claim itself names and runs whatever it finds. Before the
landing the discovery set is empty, which is the RL-1 reading; after the landing
the same command measures the fix. One instrument, both legs.

## Independence

- The tamper routes are authored **here**, from the claim's own field list
  (`speaker`, `force`, `consequence`), and are a superset of round 27's single
  `force` route. None is copied from `.scratch/r28-law/probe/`.
- The transform is a **line-level text edit of the delivered bytes**. It is not
  the D seat's probe transform and it is not a re-serialization: a control
  asserts the tampered packet differs from the clean packet in exactly the bytes
  the route intends.
- The instrument reads the packet with the projector's own strict loader (loaded
  by `runpy`, read-only, never re-implemented) for *structure*, and transforms
  the *text*. Neither the checker nor the transform is re-implemented here.

## Write scope

This file and `reports/round-28/scribe/x54-law-negatives-spotcheck.md`, plus
gitignored scratch under `.scratch/x54/`. `export TMPDIR=$PWD/.scratch` precedes
every scratch write. Read-only over every other path: no component, packet,
tool, gate, fixture, pin file, or filed rounds 8-27 byte is written; no commit,
no push.

## Usage

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-28/scribe/x54-law-negatives-spotcheck.py            # census
    python3 -B reports/round-28/scribe/x54-law-negatives-spotcheck.py --json     # receipt
    python3 -B reports/round-28/scribe/x54-law-negatives-spotcheck.py --selftest # controls

Exit codes: 0 = every measured leg behaved as the claim requires; 1 = at least
one leg did not (the census says which); 2 = could-not-evaluate.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "examples/culture-d4/packet.d4.yml"
COMPONENT = ROOT / "examples/culture-d4/components/13-register-law.yml"
ORTHO = ROOT / "examples/culture-d4/components/03-orthography.yml"
COSTUMES = ROOT / "examples/culture-d4/components/09-costumes.yml"
PROJECTOR = ROOT / "tools/d2-typed-labels.py"
SCRATCH = ROOT / ".scratch/x54"

COMMAND = "python3 -B reports/round-28/scribe/x54-law-negatives-spotcheck.py"
DATE = "2026-10-18"

LAW_CLASS_RE = re.compile(r"\bD4L-LAW[A-Z-]*")
LAW_ID_RE = re.compile(r"\bRGL-\d{2}\b")
FINDING_RE = re.compile(r"^FINDING\s+(\S+):\s*\[(\w+)\]\s*(.*)$")


# ---------------------------------------------------------------------------
# small utilities
# ---------------------------------------------------------------------------

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def lane_head() -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                          check=False, text=True)
    return proc.stdout.strip() or "unknown"


def run(cmd: list) -> dict:
    proc = subprocess.run([str(c) for c in cmd], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=False, cwd=str(ROOT))
    return {
        "cmd": " ".join(str(c) for c in cmd),
        "exit": proc.returncode,
        "stdout": proc.stdout.decode("utf-8", "replace"),
        "stderr": proc.stderr.decode("utf-8", "replace"),
    }


def findings_of(stdout: str) -> list:
    out = []
    for line in stdout.splitlines():
        m = FINDING_RE.match(line.strip())
        if m:
            out.append({"id": m.group(1), "level": m.group(2), "message": m.group(3)})
    return out


def load_packet(path: Path) -> dict:
    """The projector's own strict loader, loaded by runpy — never re-implemented."""
    mod = runpy.run_path(str(PROJECTOR))
    return mod["load_packet_file"](str(path))["packet"]


# ---------------------------------------------------------------------------
# this seat's own transform: a line-level edit of the delivered bytes
# ---------------------------------------------------------------------------

def law_block_span(text: str) -> tuple:
    """(start, end) line indices of the top-level `register_law:` block."""
    lines = text.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line == "register_law:":
            start = i
            break
    if start is None:
        raise ValueError("no top-level `register_law:` block in the packet")
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j] and not lines[j].startswith(" "):
            end = j
            break
    return lines, start, end


def row_spans(lines: list, start: int, end: int) -> dict:
    """{row_id: (first_line, last_line)} for `  -` list items carrying an id."""
    spans, current, rid = {}, None, None
    for i in range(start + 1, end):
        line = lines[i]
        if line.startswith("  -"):
            if current is not None:
                spans[rid] = (current, i)
            current, rid = i, None
        m = re.match(r'^\s{4}id:\s*"([^"]+)"\s*$', line)
        if m:
            rid = m.group(1)
    if current is not None:
        spans[rid] = (current, end)
    return spans


def tamper(text: str, route: dict) -> tuple:
    """Apply one route. Returns (new_text, changed_line_numbers)."""
    lines, start, end = law_block_span(text)
    spans = row_spans(lines, start, end)
    changed = []
    if route["op"] == "drop-row":
        first, last = spans[route["row"]]
        del lines[first:last]
        return "\n".join(lines), [first]
    if route["op"] == "duplicate-row":
        first, last = spans[route["row"]]
        dup = lines[first:last]
        lines[first:first] = dup
        return "\n".join(lines), [first]
    if route["op"] == "set-field":
        first, last = spans[route["row"]]
        field, value = route["field"], route["value"]
        pat = re.compile(r'^(\s{4}%s:\s*)(.*)$' % re.escape(field))
        for i in range(first, last):
            m = pat.match(lines[i])
            if m:
                lines[i] = m.group(1) + json.dumps(value)
                changed.append(i)
                break
        if not changed:
            raise ValueError(f"row {route['row']} has no `{field}:` line")
        return "\n".join(lines), changed
    if route["op"] == "set-field-block":
        # A field whose value is a nested block (`design_row:` + indented items).
        # Replacing the key line alone would orphan the nested items, so the whole
        # span is collapsed to one scalar line. The control asserts the packet
        # still parses afterwards, which is what catches a botched collapse.
        first, last = spans[route["row"]]
        field, value = route["field"], route["value"]
        for i in range(first, last):
            if re.match(r'^\s{4}%s:\s*$' % re.escape(field), lines[i]):
                j = i + 1
                while j < last and (not lines[j].strip() or lines[j].startswith(" " * 6)):
                    j += 1
                lines[i:j] = ["    %s: %s" % (field, json.dumps(value))]
                return "\n".join(lines), [i]
        raise ValueError(f"row {route['row']} has no block `{field}:` line")
    raise ValueError(f"unknown op {route['op']}")


# ---------------------------------------------------------------------------
# the tamper routes (authored here; a superset of round 27's single route)
# ---------------------------------------------------------------------------

ROUTES = [
    dict(id="T-01", op="set-field", row="RGL-01", field="force",
         value="no-such-force",
         why="round 27's RL-1 route, re-run: an undeclared illocutionary force"),
    dict(id="T-02", op="set-field", row="RGL-01", field="speaker",
         value="no-such-office",
         why="a speaker class that no delivered record carries"),
    dict(id="T-03", op="set-field", row="RGL-01", field="speaker",
         value="mold-keeper",
         why="RL-4's own casualty: legal in 03-orthography.yml, absent from the packet"),
    dict(id="T-04", op="set-field", row="RGL-01", field="consequence",
         value="entered on the no-such-roll by a clerk",
         why="a record consequence naming a roll no delivered record carries"),
    dict(id="T-05", op="set-field", row="RGL-01", field="axis",
         value="no-such-axis",
         why="an axis outside the packet's declared axis vocabulary"),
    dict(id="T-06", op="set-field", row="RGL-02", field="kind",
         value="no-such-kind",
         why="a law kind outside the delivered kind set"),
    dict(id="T-07", op="set-field", row="RGL-03", field="register",
         value="no-such-register",
         why="a register name the `registers` block does not declare"),
    dict(id="T-08", op="set-field", row="RGL-03", field="force",
         value="commissive-binding",
         why="RGL-03 declares a not-rollable guest charge; a binding force contradicts it"),
    dict(id="T-09", op="set-field", row="RGL-04", field="consequence",
         value="a stamp form licenses its own phoneme inventory",
         why="RGL-04's own clause (no segment) reversed in its consequence text"),
    dict(id="T-10", op="set-field", row="RGL-05", field="consequence",
         value="every stamp form is available_from E0",
         why="RGL-05's own era clause reversed (E0 stamp claims are the named defect)"),
    dict(id="T-11", op="drop-row", row="RGL-03",
         why="a whole law row removed from the block"),
    dict(id="T-12", op="duplicate-row", row="RGL-01",
         why="a duplicated row id"),
    dict(id="T-13", op="set-field-block", row="RGL-01", field="design_row",
         value="QREG-99",
         why="a design_row naming a QREG id no record carries"),
    dict(id="T-14", op="set-field", row="RGL-02", field="cite",
         value="",
         why="a row whose citation is emptied"),
]

# The false-positive control: prose that changes no structural fact.
PROSE_ROUTES = [
    dict(id="P-01", op="set-field", row="RGL-01", field="act",
         value="a restated charge, differently worded, with the same holder and force",
         why="prose reword: the structural verdict must not move"),
    dict(id="P-02", op="set-field", row="RGL-04", field="consequence",
         value="the register owns no segment (restated in other words)",
         why="prose reword of a negative clause"),
]


# ---------------------------------------------------------------------------
# checker discovery: find whatever emits the class the claim names
# ---------------------------------------------------------------------------

# The claim names a class, not a file. Two kinds of instrument can emit it, and
# the difference is the whole point of the spot-check:
#
#   DELIVERED — a tool or gate under `tools/`. This is the tree's checking leg:
#               the thing the claim asks for, on the surface a downstream
#               consumer would run.
#   EVIDENCE  — an instrument filed under `reports/round-28/`, i.e. the round's
#               own probe or acceptance runner. A finding here proves a seat
#               wrote a checker; it does not prove the tree has one.
#
# Both are reported. Only the DELIVERED class is graded, because a spot-check
# that accepted a round-28 probe as the tree's replay leg would be measuring the
# round against itself.
DELIVERED_BASES = ("tools",)
EVIDENCE_BASES = ("reports/round-28",)


def discover_checkers() -> dict:
    """{kind: [paths]} — every live .py whose bytes mention the claim's class."""
    found = {"delivered": [], "evidence": []}
    for kind, bases in (("delivered", DELIVERED_BASES), ("evidence", EVIDENCE_BASES)):
        for base in bases:
            root = ROOT / base
            if not root.is_dir():
                continue
            for path in sorted(root.rglob("*.py")):
                if "__pycache__" in path.parts or path == Path(__file__):
                    continue
                try:
                    text = path.read_text(encoding="utf-8")
                except (UnicodeDecodeError, OSError):
                    continue
                if LAW_CLASS_RE.search(text):
                    found[kind].append(path)
    return found


def invoke_checker(path: Path, packet: Path) -> dict:
    """`python3 <checker> <packet>` and `python3 <checker> --packet <packet>`.

    The claim names no interface, so both shapes are tried and the first that
    answers (not exit 2 with no findings) is the one reported. The interpreter
    is named explicitly: a filed round artifact is not necessarily executable,
    and a permission error is an artefact of the file mode, not a verdict on
    the checker.
    """
    attempts = []
    for tail in ([packet], ["--packet", packet]):
        argv = ["python3", path] + tail
        res = run(argv)
        res["argv_shape"] = " ".join(str(a) for a in tail)
        attempts.append(res)
        if res["exit"] != 2 or findings_of(res["stdout"]):
            return res
    return attempts[-1]


# ---------------------------------------------------------------------------
# the measurement
# ---------------------------------------------------------------------------

def measure() -> dict:
    clean_text = PACKET.read_text(encoding="utf-8")
    clean_sha = sha256_bytes(clean_text.encode("utf-8"))
    clean_packet = load_packet(PACKET)

    law_rows = clean_packet.get("register_law") or []
    registers = clean_packet.get("registers") or []

    out = {
        "seat": "SCRIBE X54",
        "round": 28,
        "date": DATE,
        "command": COMMAND,
        "lane_head": lane_head(),
        "claim": "D / depth — the law gains a replay/checking leg; a tampered row is a named finding (D4L-LAW-* class)",
        "packet": {"path": str(PACKET.relative_to(ROOT)), "sha256": clean_sha},
        "packet_shape": {
            "register_law_rows": len(law_rows),
            "register_law_ids": [r.get("id") for r in law_rows],
            "registers_ids": [r.get("id") for r in registers],
            "law_fields_union": sorted({k for r in law_rows for k in r.keys()}),
        },
        "artifact_digests": {},
        "checkers": {"delivered": [], "evidence": []},
        "legs": [],
    }

    for name, path in (("packet.d4.yml", PACKET), ("13-register-law.yml", COMPONENT),
                       ("03-orthography.yml", ORTHO), ("09-costumes.yml", COSTUMES),
                       ("d2-typed-labels.py", PROJECTOR)):
        if path.is_file():
            out["artifact_digests"][name] = sha256_file(path)

    # ---- leg 0: the checker surface
    checkers = discover_checkers()
    out["checkers"] = {kind: [str(p.relative_to(ROOT)) for p in paths]
                       for kind, paths in checkers.items()}
    graded = checkers["delivered"]

    # ---- leg 1: the clean packet must be silent (negative control)
    clean_proj = run(["python3", PROJECTOR, "--packet", PACKET])
    clean_findings = findings_of(clean_proj["stdout"])
    clean_nonlaw = [f for f in clean_findings if not LAW_CLASS_RE.match(f["id"])]
    out["clean"] = {
        "projector_exit": clean_proj["exit"],
        "projector_findings_total": len(clean_findings),
        "projector_findings_nonlaw": len(clean_nonlaw),
        "projector_finding_ids": sorted({f["id"] for f in clean_findings}),
        "law_findings": 0,
        "checker_runs": [],
    }
    for path in graded + checkers["evidence"]:
        res = invoke_checker(path, PACKET)
        law = [f for f in findings_of(res["stdout"]) if LAW_CLASS_RE.match(f["id"])]
        out["clean"]["checker_runs"].append({
            "checker": str(path.relative_to(ROOT)),
            "graded": path in graded,
            "exit": res["exit"],
            "findings_total": len(findings_of(res["stdout"])),
            "law_findings": len(law),
            "law_ids": sorted({f["id"] for f in law}),
        })
        if path in graded:
            out["clean"]["law_findings"] += len(law)

    # ---- leg 2/3/4: the tamper matrix
    SCRATCH.mkdir(parents=True, exist_ok=True)
    mirror = SCRATCH / "mirror"
    if mirror.exists():
        shutil.rmtree(mirror)
    # The family is resolved from the packet's PARENT DIRECTORY NAME
    # (`tools/d2-typed-labels.py:2477` `packet_family`, the same convention
    # `tools/gates/typed-pipeline-gate.py` `family_of` names). A tampered copy in
    # a differently-named directory therefore resolves as the D2 default and its
    # finding count is not comparable with the delivered packet's — a trap this
    # seat hit on its first run (16 findings for an UNMODIFIED flat copy, against
    # 12 in place). The mirror reproduces the `culture-d4/` shape so every leg
    # measures the tamper and not the path.
    mirror = SCRATCH / "mirror" / "culture-d4"
    mirror.mkdir(parents=True)

    for route in ROUTES + PROSE_ROUTES:
        entry = dict(route)
        try:
            tampered_text, changed_lines = tamper(clean_text, route)
        except ValueError as exc:
            entry["error"] = str(exc)
            out["legs"].append(entry)
            continue
        tsha = sha256_bytes(tampered_text.encode("utf-8"))
        target = mirror / ("packet.%s.yml" % route["id"].lower())
        target.write_text(tampered_text, encoding="utf-8")
        entry["tampered_path"] = str(target.relative_to(ROOT))
        entry["tampered_sha256"] = tsha
        entry["bytes_changed"] = bool(tsha != clean_sha)
        entry["changed_lines"] = changed_lines
        entry["line_delta"] = len(tampered_text.split("\n")) - len(clean_text.split("\n"))

        # control: the tampered packet must still parse, or the route measures
        # the loader, not the law checker
        try:
            tp = load_packet(target)
            entry["parses"] = True
            entry["tampered_law_rows"] = len(tp.get("register_law") or [])
        except Exception as exc:  # noqa: BLE001 - reported, never swallowed
            entry["parses"] = False
            entry["parse_error"] = "%s: %s" % (type(exc).__name__, exc)

        # leg 3: isolation — the non-law projection must not move
        proj = run(["python3", PROJECTOR, "--packet", target])
        pf = findings_of(proj["stdout"])
        entry["projector_exit"] = proj["exit"]
        entry["projector_findings_total"] = len(pf)
        entry["projector_findings_nonlaw"] = len([f for f in pf if not LAW_CLASS_RE.match(f["id"])])
        entry["projection_isolated"] = entry["projector_findings_nonlaw"] == len(clean_nonlaw)

        # leg 2: every discovered checker, by name; the delivered class is graded
        entry["checker_runs"] = []
        for path in graded + checkers["evidence"]:
            res = invoke_checker(path, target)
            fs = findings_of(res["stdout"])
            law = [f for f in fs if LAW_CLASS_RE.match(f["id"])]
            entry["checker_runs"].append({
                "checker": str(path.relative_to(ROOT)),
                "graded": path in graded,
                "exit": res["exit"],
                "law_findings": len(law),
                "law_ids": sorted({f["id"] for f in law}),
                "law_subjects": sorted({m for f in law for m in LAW_ID_RE.findall(f["message"])}),
            })
        graded_runs = [r for r in entry["checker_runs"] if r["graded"]]
        entry["law_findings_total"] = sum(r["law_findings"] for r in graded_runs)
        entry["evidence_law_findings_total"] = sum(
            r["law_findings"] for r in entry["checker_runs"] if not r["graded"])
        entry["caught"] = entry["law_findings_total"] > 0
        entry["named_row"] = route["row"] in sorted(
            {s for r in graded_runs for s in r["law_subjects"]})
        out["legs"].append(entry)

    return out


def verdict(measurement: dict) -> dict:
    tamper_legs = [l for l in measurement["legs"] if l["id"].startswith("T-")]
    prose_legs = [l for l in measurement["legs"] if l["id"].startswith("P-")]
    caught = sum(1 for l in tamper_legs if l.get("caught"))
    return {
        "checkers_delivered": len(measurement["checkers"]["delivered"]),
        "checkers_evidence": len(measurement["checkers"]["evidence"]),
        "delivered_checkers": measurement["checkers"]["delivered"],
        "clean_law_findings": measurement["clean"]["law_findings"],
        "clean_silent": measurement["clean"]["law_findings"] == 0,
        "tamper_legs": len(tamper_legs),
        "tamper_caught": caught,
        "tamper_caught_and_named": sum(1 for l in tamper_legs if l.get("caught") and l.get("named_row")),
        "tamper_all_parse": all(l.get("parses") for l in tamper_legs),
        "projection_isolated": all(l.get("projection_isolated") for l in tamper_legs),
        "prose_legs": len(prose_legs),
        "prose_false_positives": sum(1 for l in prose_legs if l.get("caught")),
        "rl1_reproduces": caught == 0,
    }


def render(measurement: dict, v: dict) -> str:
    lines = []
    A = lines.append
    A("# X54 — register-law negatives spot-check (round 28)")
    A("")
    A("- command: `%s`" % measurement["command"])
    A("- date: %s | lane HEAD `%s`" % (measurement["date"], measurement["lane_head"]))
    A("- packet `%s` sha256 `%s`" % (measurement["packet"]["path"], measurement["packet"]["sha256"]))
    A("- law rows: %s" % ", ".join(measurement["packet_shape"]["register_law_ids"]))
    A("")
    A("## Verdict")
    A("")
    A("| question | answer |")
    A("|---|---|")
    A("| delivered checkers emitting `D4L-LAW-*` (the graded class) | **%d** %s |"
      % (v["checkers_delivered"],
         ("(" + ", ".join("`%s`" % c for c in v["delivered_checkers"]) + ")")
         if v["delivered_checkers"] else "(none)"))
    A("| round-28 evidence instruments emitting the class (not graded) | %d |" % v["checkers_evidence"])
    A("| does the clean packet produce zero law findings? | %s |"
      % ("**yes**" if v["clean_silent"] else "**no** (%d)" % v["clean_law_findings"]))
    A("| tamper routes caught by name | **%d of %d** |" % (v["tamper_caught_and_named"], v["tamper_legs"]))
    A("| every tampered packet still parses? | %s |" % v["tamper_all_parse"])
    A("| the rest of the projection unmoved? | %s |" % v["projection_isolated"])
    A("| prose routes read as structural findings? | %d of %d |"
      % (v["prose_false_positives"], v["prose_legs"]))
    A("")
    A("## The tamper matrix")
    A("")
    A("| route | row | field | why | parses | law findings (delivered) | caught | names the row | non-law findings |")
    A("|---|---|---|---|---|---|---|---|---|")
    for l in measurement["legs"]:
        A("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            l["id"], l["row"], l.get("field", "—(row op)"), l["why"],
            "yes" if l.get("parses") else "**NO**",
            l.get("law_findings_total", "—"),
            "yes" if l.get("caught") else "**no**",
            "yes" if l.get("named_row") else "**no**",
            l.get("projector_findings_nonlaw", "—")))
    A("")
    A("## Clean-packet control")
    A("")
    A("- `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml` → exit %s, findings %s"
      % (measurement["clean"]["projector_exit"], measurement["clean"]["projector_findings_total"]))
    A("- finding ids: %s" % ", ".join("`%s`" % i for i in measurement["clean"]["projector_finding_ids"]))
    A("- law findings on the clean packet, delivered class: **%d**" % measurement["clean"]["law_findings"])
    A("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# selftest: the controls this instrument must fail closed on
# ---------------------------------------------------------------------------

def selftest() -> int:
    failures = []
    total = [0]

    def check(name, cond, detail=""):
        total[0] += 1
        print("%-52s %s%s" % (name, "ok" if cond else "FAIL",
                               ("  " + detail) if detail and not cond else ""))
        if not cond:
            failures.append(name)

    clean = PACKET.read_text(encoding="utf-8")
    lines, start, end = law_block_span(clean)
    check("the packet carries a top-level register_law block", start is not None)
    spans = row_spans(lines, start, end)
    check("the block resolves 5 rows by id", len(spans) == 5, str(sorted(spans)))
    check("RGL-01..RGL-05 are the ids",
          sorted(spans) == ["RGL-0%d" % i for i in range(1, 6)], str(sorted(spans)))

    # the transform is deterministic
    t1, c1 = tamper(clean, ROUTES[0])
    t2, c2 = tamper(clean, ROUTES[0])
    check("the transform is deterministic", t1 == t2 and c1 == c2)
    check("the transform changes bytes", sha256_bytes(t1.encode()) != sha256_bytes(clean.encode()))
    check("the transform changes exactly one line", len(c1) == 1, str(c1))
    check("the tampered line carries the route's value",
          "no-such-force" in t1.split("\n")[c1[0]], t1.split("\n")[c1[0]])

    # a route that targets a field the row does not carry must raise, not no-op
    try:
        tamper(clean, dict(id="X", op="set-field", row="RGL-02", field="no_such_field", value="x"))
        check("a missing field raises instead of silently no-op'ing", False)
    except ValueError:
        check("a missing field raises instead of silently no-op'ing", True)

    # a route that targets a row that does not exist must raise
    try:
        tamper(clean, dict(id="X", op="set-field", row="RGL-99", field="force", value="x"))
        check("an unknown row raises", False)
    except (ValueError, KeyError):
        check("an unknown row raises", True)

    # the tampered packet still loads under the projector's own loader
    try:
        tp = load_packet_from_text(t1)
        check("the tampered packet still parses", True)
        check("the tampered row carries the tampered value",
              any(r.get("force") == "no-such-force" for r in tp["register_law"]))
    except Exception as exc:  # noqa: BLE001
        check("the tampered packet still parses", False, str(exc))

    # the drop and duplicate routes
    t3, _ = tamper(clean, dict(id="X", op="drop-row", row="RGL-03"))
    check("drop-row removes exactly one row",
          len(load_packet_from_text(t3)["register_law"]) == 4)
    t4, _ = tamper(clean, dict(id="X", op="duplicate-row", row="RGL-01"))
    check("duplicate-row adds exactly one row",
          len(load_packet_from_text(t4)["register_law"]) == 6)

    # the cleaner: the tampered bytes are not the delivered bytes
    check("the delivered packet is untouched by this selftest",
          sha256_file(PACKET) == sha256_bytes(clean.encode()))

    # the discovery must be a real search, and it must be empty-or-nonempty honestly
    found = discover_checkers()
    check("checker discovery returns both classes",
          isinstance(found, dict) and set(found) == {"delivered", "evidence"}, str(found))
    check("checker discovery excludes this instrument",
          Path(__file__).resolve() not in found["delivered"] + found["evidence"])
    check("the graded class is the delivered one (tools/), not the round's own probes",
          all("reports/" not in str(p) for p in found["delivered"]))
    print("checker discovery (informational): delivered=%s evidence=%s"
          % ([str(p.relative_to(ROOT)) for p in found["delivered"]] or "none",
             [str(p.relative_to(ROOT)) for p in found["evidence"]] or "none"))

    # a checker that cannot be launched must be reported, never silently a pass:
    # the invocation helper names the interpreter explicitly, so a filed artifact
    # with no exec bit is still runnable.
    check("the invocation helper names the interpreter",
          invoke_checker.__doc__.find("python3") >= 0)

    # the mirror must preserve the family-resolution shape: an UNMODIFIED copy in
    # the mirror must project exactly as the delivered packet does. This is the
    # control that catches the path-dependence trap (a flat copy resolves as D2).
    SCRATCH.mkdir(parents=True, exist_ok=True)
    probe_dir = SCRATCH / "mirror" / "culture-d4"
    probe_dir.mkdir(parents=True, exist_ok=True)
    probe = probe_dir / "packet.selftest.yml"
    probe.write_text(clean, encoding="utf-8")
    inplace = run(["python3", PROJECTOR, "--packet", PACKET])
    copied = run(["python3", PROJECTOR, "--packet", probe])
    check("an unmodified mirror copy projects exactly as the delivered packet",
          len(findings_of(copied["stdout"])) == len(findings_of(inplace["stdout"])),
          "%d vs %d" % (len(findings_of(copied["stdout"])), len(findings_of(inplace["stdout"]))))
    probe.unlink()
    flat = SCRATCH / "mirror" / "packet.selftest-flat.yml"
    flat.write_text(clean, encoding="utf-8")
    flatrun = run(["python3", PROJECTOR, "--packet", flat])
    check("a flat copy does NOT project the same (the trap is real, not assumed)",
          len(findings_of(flatrun["stdout"])) != len(findings_of(inplace["stdout"])),
          "%d vs %d" % (len(findings_of(flatrun["stdout"])), len(findings_of(inplace["stdout"]))))
    flat.unlink()

    # the finding parser must reject non-findings and accept the gate convention
    check("finding parser accepts the gate convention",
          findings_of('FINDING D4L-LAW-FORCE: [hold] RGL-01 — no-such-force') ==
          [{"id": "D4L-LAW-FORCE", "level": "hold",
            "message": "RGL-01 — no-such-force"}])
    check("finding parser rejects prose", findings_of("no findings here") == [])

    print("")
    if failures:
        print("selftest: %d/%d checks passed, %d FAILED: %s"
              % (total[0] - len(failures), total[0], len(failures), ", ".join(failures)))
        return 1
    print("selftest: %d/%d checks passed" % (total[0], total[0]))
    return 0


def load_packet_from_text(text: str) -> dict:
    mod = runpy.run_path(str(PROJECTOR))
    return mod["load_packet_strict"](text)["packet"]


# ---------------------------------------------------------------------------

def check_one_packet(packet_path: Path) -> int:
    """Answer one question about an arbitrary packet, in the shape the round's
    discovery harness expects (`<instrument> --packet PATH`).

    The question is this seat's own: does any **delivered** instrument under
    `tools/` emit a named `D4L-LAW-*` finding on this packet?

    This mode deliberately prints **no** `D4L-LAW-<token>` of its own. A
    spot-check that manufactured the class it is measuring would make its own
    negative unmeasurable: the discovery harness counts instruments that can
    emit the token, so a spot-check that emitted one on every packet would be
    counted as a replay leg, and the very absence the claim is about would be
    hidden behind the instrument measuring it. The answer is therefore reported
    in this instrument's own vocabulary, and the absence is stated as absence.
    """
    packet_path = Path(packet_path)
    if not packet_path.is_file():
        print("could-not-evaluate: packet missing: %s" % packet_path, file=sys.stderr)
        return 2
    found = discover_checkers()["delivered"]
    runs = []
    for path in found:
        res = invoke_checker(path, packet_path)
        law = [f for f in findings_of(res["stdout"]) if LAW_CLASS_RE.match(f["id"])]
        runs.append({"checker": str(path.relative_to(ROOT)), "exit": res["exit"],
                     "law_findings": len(law), "law_ids": sorted({f["id"] for f in law})})
    total = sum(r["law_findings"] for r in runs)
    print("x54-spotcheck: packet=%s delivered_instruments=%d law_findings=%d"
          % (packet_path, len(found), total))
    for r in runs:
        print("  %s exit=%s law_findings=%d ids=%s"
              % (r["checker"], r["exit"], r["law_findings"], r["law_ids"]))
    if total == 0:
        print("x54-spotcheck: no delivered instrument names the law's finding class on "
              "this packet — the law has no replay leg on the delivered surface")
    return 1 if total == 0 else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--packet", metavar="PATH",
                        help="answer this seat's single question about one packet "
                             "(the shape the round's discovery harness uses)")
    parser.add_argument("--json", action="store_true", help="emit the receipt")
    parser.add_argument("--selftest", "--self-test", action="store_true",
                        help="run the instrument's own controls")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()
    if args.packet:
        return check_one_packet(Path(args.packet))
    if not PACKET.is_file():
        print("could-not-evaluate: packet missing: %s" % PACKET, file=sys.stderr)
        return 2
    measurement = measure()
    v = verdict(measurement)
    measurement["verdict"] = v
    measurement["generated_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if args.json:
        print(json.dumps(measurement, indent=1, sort_keys=True))
    else:
        print(render(measurement, v))
        print("verdict: delivered_checkers=%d evidence_checkers=%d clean_law_findings=%d "
              "tamper_caught_by_name=%d/%d rl1_reproduces=%s"
              % (v["checkers_delivered"], v["checkers_evidence"], v["clean_law_findings"],
                 v["tamper_caught_and_named"], v["tamper_legs"], v["rl1_reproduces"]))
    return 0 if (v["clean_silent"] and v["tamper_caught_and_named"] == v["tamper_legs"]
                 and v["tamper_all_parse"] and v["projection_isolated"]
                 and v["prose_false_positives"] == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
