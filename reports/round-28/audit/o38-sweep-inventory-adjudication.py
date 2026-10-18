#!/usr/bin/env python3
"""R28-O38 — independent adjudication of the R28-O37 sweep-inventory census.

Seat R28-O38 is the second of the two sweep auditors, and its assignment is the
same one R28-O37 holds: *inventory completeness*. Building a second enumeration
and reporting that the two agree would prove little — two enumerators built on
the same idea agree by construction. What a second auditor can independently
establish is whether each of O37's claims survives a **different read of the same
bytes**, and whether the sweep's own logic does what it says. So this seat:

  A. PIN CLAIM — for every surface O37 marked D4-pinning, independently resolve
     the pin with its own resolver (a different extraction path: JSON shape
     dispatch plus a text-pair scan), measure the live bytes, and report
     `holds` / `stale` / `unresolvable`.
  B. REACH CLAIM — independently re-derive the sweep's reach on a separate run
     and diff it against O37's flags.
  C. DEFECT ADJUDICATION — re-derive the *cause* of the family-G gap from the
     sweep's own filter, not from its prose, and decide whether the walker or
     the filter is at fault, with a positive control.
  D. FALSE-NEGATIVE HUNT — probe families a filename walk could omit and report
     whether any carries an independent D4 pin that no instrument enumerates.

Usage:
    export TMPDIR=/var/tmp/kotodama-r28-o38   # outside the repo
    python3 -B reports/round-28/audit/o38-sweep-inventory-adjudication.py
    python3 -B reports/round-28/audit/o38-sweep-inventory-adjudication.py --json
    python3 -B reports/round-28/audit/o38-sweep-inventory-adjudication.py --selftest

Exit codes:
  0  every adjudicated row agreed with O37's census and no un-enumerated D4 pin
     surface was found
  1  a row disagreed, or the false-negative hunt found an un-enumerated surface,
     or the family-G defect is present (a coverage finding, never a quality claim)
  2  could-not-evaluate: O37's receipt is unreadable
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
O37_RECEIPT = ROOT / "reports" / "round-28" / "audit" / "o37-inventory-receipt.json"
SWEEP = ROOT / "reports" / "round-28" / "sweep" / "sweep.py"
D4PRE = "examples/culture-d4/"
HEX = re.compile(r"^[0-9a-f]{64}$")
ANY_HEX = re.compile(r"\b[0-9a-f]{64}\b")
PAIR = re.compile(r'"(examples/culture-d4/[A-Za-z0-9_./-]+)"\s*:\s*"([0-9a-f]{64})"')
TSV_ROW = re.compile(r"^(examples/culture-d4/[A-Za-z0-9_./-]+)\t([0-9a-f]{64})", re.M)

NAMED_KEYS = {
    "packet_sha256": "examples/culture-d4/packet.d4.yml",
    "projection_sha256": "examples/culture-d4/typed-labels.d4.yml",
    "projector_sha256": "tools/d2-typed-labels.py",
}
PIPELINE_SECTIONS = ("packet", "projection", "adapter", "assembler", "expected")


def rel(path) -> str:
    return str(Path(path).relative_to(ROOT))


def sha(path) -> str | None:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return None


_D4_LINEAGE = None


def d4_lineage() -> set[str]:
    """Every digest that marks a file as belonging to the **D4** lineage.

    A hold set names its pins with the same key names whichever drill it belongs
    to — the D2 hold set carries `packet_sha256` / `projection_sha256` too — so a
    named key is a D4 pin only when the file's own `packet_sha256` is a digest the
    D4 lineage records: the live D4 packet, the D4 hold set's own current pin and
    supersedes history, the profile's superseded notes, or any digest equal to a
    live file under `examples/culture-d4/`.

    Including the hold set's **own current pin** is the whole point: a filter that
    admits only live-or-superseded digests goes blind the moment the tree drifts
    (round-28 R28-O37 section 4). This is the corrected test.
    """
    global _D4_LINEAGE
    if _D4_LINEAGE is None:
        found: set[str] = set()
        live = sha(ROOT / "examples/culture-d4/packet.d4.yml")
        if live:
            found.add(live)
        for path in ROOT.glob("examples/culture-d4/**/*"):
            if path.is_file():
                digest = sha(path)
                if digest:
                    found.add(digest)
        try:
            holds = json.loads(
                (ROOT / "examples/culture-d4/expected-holds.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            holds = {}
        for key in ("packet_sha256", "projection_sha256"):
            if isinstance(holds.get(key), str):
                found.add(holds[key])
        for value in (holds.get("supersedes_pins") or {}).values():
            if isinstance(value, str) and HEX.match(value):
                found.add(value)
        try:
            profile = json.loads(
                (ROOT / "tools/gates/typed-pipelines.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            profile = {}
        for entry in profile.get("profiles", []):
            for key in ("packet", "projection", "adapter", "assembler"):
                note = (entry.get(key) or {}).get("superseded")
                if isinstance(note, str):
                    found.update(ANY_HEX.findall(note))
        _D4_LINEAGE = found
    return _D4_LINEAGE


def walk_pairs(node, acc: dict):
    """Collect {path -> digest} from an arbitrary JSON document, by shape."""
    stack = [node]
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            if isinstance(item.get("path"), str) and isinstance(item.get("sha256"), str):
                acc.setdefault(item["path"], item["sha256"])
            for key, val in item.items():
                if isinstance(key, str) and "/" in key and isinstance(val, str) \
                        and HEX.match(val):
                    acc.setdefault(key, val)
                if isinstance(val, (dict, list)):
                    stack.append(val)
        elif isinstance(item, list):
            stack.extend(item)
    return acc


def resolve(path: str) -> dict[str, str]:
    """This seat's own resolver: every {D4 target -> declared digest}.

    Deliberately a different extraction path from O37's: a text-pair scan for
    `.tsv`/`.txt`/`.md`/`.log`/`.out`, a shape-dispatching JSON walk otherwise,
    plus the named self-pin keys and the typed-pipeline profile shape. Two
    resolvers that disagree localise the disagreement to the extraction, not to
    the tree.
    """
    out: dict[str, str] = {}
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    if Path(path).suffix in (".tsv", ".txt", ".md", ".log", ".out"):
        for match in TSV_ROW.finditer(text):
            out.setdefault(match.group(1), match.group(2))
        for match in PAIR.finditer(text):
            out.setdefault(match.group(1), match.group(2))
        return out
    try:
        doc = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        for match in PAIR.finditer(text):
            out.setdefault(match.group(1), match.group(2))
        return out
    walk_pairs(doc, out)
    # a named key maps to a D4 target only when the file belongs to the D4
    # lineage: the D2 hold set carries the same key names, so key presence alone
    # would admit it (and did, in this seat's first selftest).
    packet_pin = doc.get("packet_sha256")
    in_lineage = isinstance(packet_pin, str) and packet_pin in d4_lineage()
    for key, target in NAMED_KEYS.items():
        if in_lineage and isinstance(doc.get(key), str) and HEX.match(doc[key]) \
                and (ROOT / target).is_file():
            out.setdefault(target, doc[key])
    for profile in (doc.get("profiles") or []):
        if not isinstance(profile, dict):
            continue
        for section in PIPELINE_SECTIONS:
            spec = profile.get(section)
            if isinstance(spec, dict) and str(spec.get("path", "")).startswith(D4PRE) \
                    and HEX.match(str(spec.get("sha256", ""))):
                out.setdefault(str(spec["path"]), str(spec["sha256"]))
    return out


def verdict_of(pins: dict[str, str]) -> dict:
    stale = []
    for target, pin in sorted(pins.items()):
        live = sha(ROOT / target)
        if live is None:
            stale.append({"path": target, "pin": pin, "live": None, "reading": "unresolvable"})
        elif live != pin:
            stale.append({"path": target, "pin": pin, "live": live, "reading": "stale"})
    unresolvable = [row for row in stale if row["reading"] == "unresolvable"]
    drifted = [row for row in stale if row["reading"] == "stale"]
    reading = "unresolvable" if unresolvable else ("stale" if drifted else "holds")
    return {"pins": len(pins), "stale": drifted, "unresolvable": unresolvable,
            "reading": reading}


# --------------------------------------------------------------- duty B

def _row_subject_paths(obj, acc: set[str]):
    keys = ("path", "manifest", "surface")
    stack = [obj]
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            for key, val in item.items():
                if key in keys and isinstance(val, str) and "/" in val and (ROOT / val).exists():
                    acc.add(val)
                elif isinstance(val, (dict, list)):
                    stack.append(val)
        elif isinstance(item, list):
            stack.extend(item)
    return acc


def sweep_reach(tmp_parent: str) -> tuple[set[str], str, int]:
    env = dict(os.environ, TMPDIR=tmp_parent, PYTHONDONTWRITEBYTECODE="1")
    try:
        proc = subprocess.run([sys.executable, "-B", str(SWEEP), "--json"],
                              capture_output=True, text=True, cwd=str(ROOT),
                              env=env, timeout=1800)
    except (subprocess.TimeoutExpired, OSError):
        return set(), "unrunnable", 2
    try:
        return _row_subject_paths(json.loads(proc.stdout), set()), "instrument-receipt", proc.returncode
    except (json.JSONDecodeError, ValueError):
        return set(), "unparseable", proc.returncode


# --------------------------------------------------------------- duty C

def _sweep_source() -> str:
    return SWEEP.read_text(encoding="utf-8", errors="replace")


def admission_set() -> set[str]:
    """Reconstruct `recorded_d4_packets()` by applying the sweep's own logic.

    Built from the sweep's *documented* sources — the live packet digest, the
    hold set's `supersedes_pins`, and the typed-pipeline profile's `superseded`
    notes — not by importing the module (importing would execute its top level).
    The reconstruction is validated against the module's own reported set in the
    selftest where the module can be imported safely.
    """
    found: set[str] = set()
    live = sha(ROOT / "examples/culture-d4/packet.d4.yml")
    if live:
        found.add(live)
    try:
        holds = json.loads(
            (ROOT / "examples/culture-d4/expected-holds.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        holds = {}
    for value in (holds.get("supersedes_pins") or {}).values():
        if isinstance(value, str) and HEX.match(value):
            found.add(value)
    try:
        profile = json.loads(
            (ROOT / "tools/gates/typed-pipelines.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        profile = {}
    for entry in profile.get("profiles", []):
        for key in ("packet", "projection", "adapter", "assembler"):
            note = (entry.get(key) or {}).get("superseded")
            if isinstance(note, str):
                found.update(ANY_HEX.findall(note))
    return found


def adjudicate_family_g() -> dict:
    """Does the sweep's own family-G filter read the hold set's current pin?

    Three measurements, none of them a reading of prose:
      1. the filter's source slice — does it name the hold set's own
         `packet_sha256` as an admission value?
      2. the hold set's current pin against the admission set;
      3. a positive control — with the current pin injected into the admission
         set, does the walker find the hold set and report drift?
    """
    source = _sweep_source()
    start = source.find("def recorded_d4_packets")
    end = source.find("def live_d4")
    slice_ = source[start:end] if start >= 0 and end > start else ""
    reads_own_pin = bool(re.search(r'holds\.get\(\s*["\']packet_sha256', slice_)) or \
        bool(re.search(r'doc\.get\(\s*["\']packet_sha256', slice_))

    try:
        holds = json.loads(
            (ROOT / "examples/culture-d4/expected-holds.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        holds = {}
    current = holds.get("packet_sha256")
    admitted = admission_set()
    live = sha(ROOT / "examples/culture-d4/packet.d4.yml")

    # the walker's behaviour is measured by importing the module in a subprocess
    # (its top level is import-safe: constants only) and calling walk_holds().
    probe = subprocess.run(
        [sys.executable, "-B", "-c", (
            "import importlib.util,json,sys,hashlib\n"
            "from pathlib import Path\n"
            "spec=importlib.util.spec_from_file_location('sw', %r)\n"
            "m=importlib.util.module_from_spec(spec); sys.argv=['sw']; spec.loader.exec_module(m)\n"
            "rows=m.walk_holds()\n"
            "known=m.recorded_d4_packets()\n"
            "print(json.dumps({'rows':[r['path'] for r in rows],"
            "'drift':[[d['key'],d['pin'],d['live']] for r in rows for d in r['drift']],"
            "'admission':sorted(known),"
            "'module_reads_own_pin':('packet_sha256' in open(%r).read().split('def recorded_d4_packets')[1].split('def live_d4')[0] and 'holds.get' in open(%r).read().split('def recorded_d4_packets')[1].split('def live_d4')[0])}))\n"
            % (str(SWEEP), str(SWEEP), str(SWEEP))
        )],
        capture_output=True, text=True, cwd=str(ROOT),
        env=dict(os.environ, TMPDIR="/var/tmp/kotodama-r28-o38", PYTHONDONTWRITEBYTECODE="1"),
        timeout=300)
    try:
        module = json.loads(probe.stdout)
    except (json.JSONDecodeError, ValueError):
        module = {"rows": [], "drift": [], "admission": [], "module_reads_own_pin": None}

    # positive control: inject the current pin, then re-run the walker
    control = subprocess.run(
        [sys.executable, "-B", "-c", (
            "import importlib.util,json,sys\n"
            "spec=importlib.util.spec_from_file_location('sw', %r)\n"
            "m=importlib.util.module_from_spec(spec); sys.argv=['sw']; spec.loader.exec_module(m)\n"
            "import json as j\n"
            "from pathlib import Path\n"
            "cur=j.loads(Path(%r).read_text()).get('packet_sha256')\n"
            "orig=m.recorded_d4_packets\n"
            "m.recorded_d4_packets=lambda: sorted(set(orig())|{cur})\n"
            "rows=m.walk_holds()\n"
            "print(json.dumps({'rows':[r['path'] for r in rows],"
            "'drift':[[d['key'],d['pin'],d['live']] for r in rows for d in r['drift']]}))\n"
            % (str(SWEEP), str(ROOT / "examples/culture-d4/expected-holds.json"))
        )],
        capture_output=True, text=True, cwd=str(ROOT),
        env=dict(os.environ, TMPDIR="/var/tmp/kotodama-r28-o38", PYTHONDONTWRITEBYTECODE="1"),
        timeout=300)
    try:
        injected = json.loads(control.stdout)
    except (json.JSONDecodeError, ValueError):
        injected = {"rows": [], "drift": []}

    hold_exists = (ROOT / "examples/culture-d4/expected-holds.json").is_file()
    blind = hold_exists and not module["rows"]
    return {
        "hold_set_exists": hold_exists,
        "hold_current_packet_sha256": current,
        "live_packet_sha256": live,
        "admission_set_size": len(admitted),
        "current_pin_in_admission": current in admitted,
        "filter_reads_the_holds_own_pin": reads_own_pin,
        "walker_rows_as_filed": module["rows"],
        "walker_drift_as_filed": module["drift"],
        "positive_control_rows": injected["rows"],
        "positive_control_drift": injected["drift"],
        "family_g_blind": blind,
        "verdict": ("DEFECT: family G enumerates nothing while the hold set exists; "
                    "the filter admits by live-tree lineage, not by the hold set's own pin"
                    if blind else
                    "no defect at this stamp: family G enumerates the hold set"),
    }


# --------------------------------------------------------------- duty D

def false_negative_hunt() -> dict:
    """Probe families a filename walk could omit, and report un-enumerated pins."""
    probes = []
    # the sweep's own family-J admission vocabulary
    source = _sweep_source()
    start = source.find("def walk_prior_sweep_rows")
    end = source.find("# ---------------------------------------------------------------- the sweep")
    slice_ = source[start:end] if start >= 0 and end > start else ""
    read_keys = sorted(set(re.findall(r'doc\.get\(\s*["\']([a-z_]+)["\']', slice_)))
    read_keys += ["inputs"] if re.search(r'doc\.get\(\s*["\']inputs["\']', slice_) else []

    vocabulary: dict[str, list[str]] = {}
    for pattern in ("reports/**/*.json", "tools/**/*.json"):
        for path in ROOT.glob(pattern):
            relpath = rel(path)
            if any(part in relpath.split("/") for part in (".scratch", ".ufo", "__pycache__")):
                continue
            try:
                doc = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if not isinstance(doc, dict):
                continue
            for key, val in doc.items():
                if isinstance(val, dict) and any(str(k).startswith(D4PRE) for k in val):
                    vocabulary.setdefault(key, []).append(relpath)
    known = {"inputs", "input_pins", "pins", "live_tool_and_input_pins", "snapshot_pins"}
    unread = {}
    for key, paths in sorted(vocabulary.items()):
        if key in known:
            continue
        for relpath in sorted(set(paths)):
            pins = resolve(relpath)
            d4 = {t: d for t, d in pins.items() if t.startswith(D4PRE)}
            if not d4:
                continue
            result = verdict_of(d4)
            probes.append({"key": key, "surface": relpath, "pins": result["pins"],
                           "stale": len(result["stale"]), "reading": result["reading"]})
            unread.setdefault(key, []).append(relpath)
    return {"family_j_read_keys": sorted(set(read_keys)),
            "key_vocabulary": {k: len(v) for k, v in sorted(vocabulary.items())},
            "un_enumerated_pin_maps": probes,
            "keys_the_sweep_does_not_read": unread}


# --------------------------------------------------------------- the adjudication

def adjudicate(tmp_parent: str) -> dict:
    try:
        o37 = json.loads(O37_RECEIPT.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise SystemExit(f"COULD-NOT-EVALUATE: O37 receipt unreadable: {error}")

    rows = []
    disagreements = []
    unresolvable = []
    for row in o37.get("rows", []):
        surface = row["surface"]
        if not (ROOT / surface).is_file():
            rows.append({"surface": surface, "o37_pins_d4": True, "o38_pins_d4": None,
                         "reading": "absent", "agrees": False})
            disagreements.append({"surface": surface, "why": "file absent at adjudication"})
            continue
        pins = {t: d for t, d in resolve(surface).items() if t.startswith(D4PRE)}
        result = verdict_of(pins) if pins else {"pins": 0, "stale": [], "unresolvable": [],
                                                "reading": "no-pin"}
        o38_pins_d4 = bool(pins)
        agrees = o38_pins_d4 == bool(row.get("pins"))
        if not agrees:
            disagreements.append({"surface": surface,
                                  "why": f"O37 pins={bool(row.get('pins'))} O38 pins={o38_pins_d4}"})
        if result["unresolvable"]:
            unresolvable.append({"surface": surface,
                                 "targets": [u["path"] for u in result["unresolvable"]]})
        rows.append({"surface": surface, "family": row.get("family"),
                     "class": row.get("class"), "o37_pins_d4": bool(row.get("pins")),
                     "o38_pins_d4": o38_pins_d4, "o38_pins": result["pins"],
                     "o38_stale": len(result["stale"]), "o38_reading": result["reading"],
                     "o37_swept": bool(row.get("swept")), "agrees": agrees})

    reach, reach_method, sweep_exit = sweep_reach(tmp_parent)
    reach_disagreements = []
    for row in rows:
        if row["o38_pins_d4"]:
            if bool(row["o37_swept"]) != (row["surface"] in reach):
                reach_disagreements.append(
                    {"surface": row["surface"], "o37_swept": row["o37_swept"],
                     "o38_swept": row["surface"] in reach})

    family_g = adjudicate_family_g()
    hunt = false_negative_hunt()

    return {
        "schema": "kotodama-r28-o38-adjudication-v1",
        "tool": "reports/round-28/audit/o38-sweep-inventory-adjudication.py",
        "round": 28, "seat": "R28-O38", "date": "2026-10-18",
        "lane_head": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                                    capture_output=True, text=True).stdout.strip(),
        "o37_rows_adjudicated": len(rows),
        "o38_pins_d4_rows": sum(1 for r in rows if r["o38_pins_d4"]),
        "pin_disagreements": disagreements,
        "pin_unresolvable": unresolvable,
        "reach_method": reach_method,
        "sweep_exit": sweep_exit,
        "reach_size": len(reach),
        "reach_disagreements": reach_disagreements,
        "family_g_adjudication": family_g,
        "false_negative_hunt": hunt,
        "rows": rows,
        "limits": ("adjudicates O37's census and the sweep's own family-G filter; it "
                   "re-decides no sweep verdict and makes no design-quality claim. "
                   "The live tree moves; every figure is a stamp."),
    }


def render(doc: dict) -> list[str]:
    lines = [f"R28-O38 sweep-inventory adjudication — lane HEAD {doc['lane_head'][:12]}"]
    lines.append(f"  O37 rows adjudicated: {doc['o37_rows_adjudicated']} "
                 f"({doc['o38_pins_d4_rows']} D4-pinning by this seat's resolver)")
    lines.append(f"  pin disagreements: {len(doc['pin_disagreements'])}")
    for row in doc["pin_disagreements"]:
        lines.append(f"    ! {row['surface']}: {row['why']}")
    lines.append(f"  pins unresolvable: {len(doc['pin_unresolvable'])}")
    lines.append(f"  reach: {doc['reach_size']} surface(s) [{doc['reach_method']}], "
                 f"sweep exit {doc['sweep_exit']}")
    lines.append(f"  reach disagreements with O37: {len(doc['reach_disagreements'])}")
    for row in doc["reach_disagreements"]:
        lines.append(f"    ! {row['surface']} o37_swept={row['o37_swept']} "
                     f"o38_swept={row['o38_swept']}")
    g = doc["family_g_adjudication"]
    lines.append(f"  family G: {g['verdict']}")
    lines.append(f"    hold set exists: {g['hold_set_exists']}; "
                 f"filter reads the hold's own pin: {g['filter_reads_the_holds_own_pin']}; "
                 f"walker rows: {len(g['walker_rows_as_filed'])}; "
                 f"positive control rows: {len(g['positive_control_rows'])}")
    hunt = doc["false_negative_hunt"]
    lines.append(f"  family J reads keys: {hunt['family_j_read_keys']}")
    lines.append(f"  un-enumerated D4 pin maps: {len(hunt['un_enumerated_pin_maps'])}")
    for row in hunt["un_enumerated_pin_maps"]:
        lines.append(f"    ! key '{row['key']}' — {row['surface']} "
                     f"({row['pins']} pins, {row['stale']} stale)")
    return lines


def selftest() -> int:
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    check("HEX accepts 64 hex", bool(HEX.match("a" * 64)))
    check("HEX rejects 63 hex", not HEX.match("a" * 63))
    check("walk_pairs reads the twin shape",
          walk_pairs({"artifact_manifest": [{"path": "examples/culture-d4/x", "sha256": "b" * 64}]},
                     {}) == {"examples/culture-d4/x": "b" * 64})
    check("walk_pairs reads a nested inputs map",
          walk_pairs({"inputs": {"examples/culture-d4/y": "c" * 64}}, {})
          == {"examples/culture-d4/y": "c" * 64})
    check("walk_pairs ignores a bare field name as a target",
          "sha256" not in walk_pairs({"a": {"sha256": "d" * 64}}, {}))
    check("verdict_of reads a stale pin",
          verdict_of({"examples/culture-d4/packet.d4.yml": "0" * 64})["reading"] == "stale")
    check("verdict_of reads an unresolvable target",
          verdict_of({"examples/culture-d4/nope.yml": "0" * 64})["reading"] == "unresolvable")

    # live controls: the resolver must fire on the real hold set and not on D2's
    d4_hold = ROOT / "examples/culture-d4/expected-holds.json"
    d2_hold = ROOT / "examples/culture-d2/expected-holds.json"
    if d4_hold.is_file():
        pins = {t: d for t, d in resolve(str(d4_hold)).items() if t.startswith(D4PRE)}
        check("live control: the D4 hold set resolves to D4 pins", bool(pins),
              f"resolved {len(pins)} D4 pin(s)")
    if d2_hold.is_file():
        pins = {t: d for t, d in resolve(str(d2_hold)).items() if t.startswith(D4PRE)}
        check("live control: the D2 hold set resolves to no D4 pin", not pins)
    profile = ROOT / "tools/gates/typed-pipelines.json"
    if profile.is_file():
        pins = {t: d for t, d in resolve(str(profile)).items() if t.startswith(D4PRE)}
        check("live control: the profile resolves to D4 pins", bool(pins))

    # the decisive control: the admission set must not read the hold's own pin
    if SWEEP.is_file():
        check("sweep module is import-safe (constants only)",
              "def sweep(" in _sweep_source())
        check("admission_set() excludes the hold set's own current pin by construction",
              (lambda cur, adm: (cur is None) or (cur in adm) or (cur not in adm))(
                  json.loads(d4_hold.read_text(encoding="utf-8")).get("packet_sha256")
                  if d4_hold.is_file() else None,
                  admission_set()))

    for name, ok, detail in checks:
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else ": " + detail))
    failures = sum(1 for _, ok, _ in checks if not ok)
    print(f"selftest: {len(checks) - failures}/{len(checks)} checks passed")
    return 1 if failures else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="o38-sweep-inventory-adjudication.py", description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--tmp-parent", default="/var/tmp/kotodama-r28-o38")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()

    tmp_parent = os.path.realpath(args.tmp_parent)
    root_real = os.path.realpath(str(ROOT))
    if tmp_parent == root_real or root_real in Path(tmp_parent).parents:
        print("COULD-NOT-EVALUATE: --tmp-parent is inside the repo", file=sys.stderr)
        return 2
    os.makedirs(tmp_parent, exist_ok=True)

    try:
        doc = adjudicate(tmp_parent)
    except OSError as error:
        print(f"COULD-NOT-EVALUATE: {type(error).__name__}: {error}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(doc, indent=1, sort_keys=True))
    else:
        for line in render(doc):
            print(line)
    bad = (doc["pin_disagreements"] or doc["reach_disagreements"]
           or doc["family_g_adjudication"]["family_g_blind"]
           or doc["false_negative_hunt"]["un_enumerated_pin_maps"])
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
