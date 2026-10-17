#!/usr/bin/env python3
"""typed-pipeline-gate — the D2 typed-pipeline entry point (R11-D05, design §3).

Gate-shaped so `tools/replay-frozen.py` can pin it (a Python file directly under
`tools/gates/`). It grades the typed pipeline in four legs and never edits a
peer: `tools/assemble-d2.py`, `tools/d2-typed-labels.py`, the adapter
`tools/assemble-d2-typed.py` and the five culture gates are executed or loaded
read-only.

    python3 tools/gates/typed-pipeline-gate.py [PACKET]   # default examples/culture-d2/packet.d2.yml
    python3 tools/gates/typed-pipeline-gate.py --selftest
    python3 tools/gates/typed-pipeline-gate.py --json

Legs (design §3.1):

  L1 build    assembler identity check; projector run over the packet; adapter
              builds the typed packet into a temp mirror (never into examples/)
  L2 channel  the five gates run over the legacy packet and over the typed
              packet in isolated mirrors; the typed findings must be the legacy
              findings minus exactly the ten `PHON-*` lines naming the routed
              records, and zero typed-run line may name an off-channel record
  L3 holds    the pipeline finding set must equal the frozen expected set
              exactly: 15 holds, 1 note, 0 fails — key `(id, severity, where)`
              as a set, details pinned too (design §4.4)
  L4 pins     the packet/projection/adapter digests embedded in the typed packet
              re-verify against the bytes read

Exit codes (design §3.2): 0 = L1-L4 all pass — the pipeline emitted exactly the
frozen expected hold set; 1 = a leg mismatched (channel, hold set, note set, fail
set, determinism); 2 = could-not-evaluate (stale projection pin, malformed
packet, gate traceback, pin mismatch).

Exit 0 is **not** a clearance: the banner says so, and the 15 hold lines are
printed verbatim, so the artifact a reader sees is red at the design level. A
hold laundered into a note, deleted or renamed fails L3.

A typed packet may also be handed in directly (the frozen replay row does): a
file carrying `typed_channel` is graded as the build product — L2 reconstructs
the legacy packet from the moved fields, and L3/L4 run as usual.
"""

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent.parent
GATES_DIR = ROOT / "tools/gates"
PACKET_DEFAULT = ROOT / "examples/culture-d2/packet.d2.yml"
PROJECTION_DEFAULT = ROOT / "examples/culture-d2/typed-labels.d2.yml"
EXPECTED_HOLDS_PATH = ROOT / "examples/culture-d2/expected-holds.json"
ADAPTER = ROOT / "tools/assemble-d2-typed.py"
PROJECTOR = ROOT / "tools/d2-typed-labels.py"
SERIALIZER = ROOT / "tools/assemble-d2.py"
GATE_NAMES = (
    "naming-collision-gate.py",
    "phonology-sanity-gate.py",
    "costume-era-consistency-gate.py",
    "lexicon-coverage-audit.py",
    "myth-consistency-gate.py",
)
SCHEMA = "kotodama-typed-pipeline-holds-v1"
FINDING_PREFIX = "FINDING "
NOTE_PREFIX = "NOTE "
BANNER = ("TYPED-PIPELINE: exit 0 = the emitted findings equal the frozen expected "
          "hold set; every hold below is still open design debt.")

# The frozen expected hold set for examples/culture-d2 (design §4.2-§4.3), keyed
# by (id, severity, where). --selftest asserts this constant equals
# examples/culture-d2/expected-holds.json in both directions, so the constant and
# the committed record cannot drift apart.
EXPECTED_HOLDS = (
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-01"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-02"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-03"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-04"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-05"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-06"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-07"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-08"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-09"),
    ("D2L-FORM-UNRESOLVED", "hold", "GAR-10"),
    ("D2L-NATIVE", "hold", "L-15"),
    ("D2L-NATIVE", "hold", "L-16"),
    ("D2L-RANK", "hold", "TR-04#a|TR-06#a"),
    ("D2L-RANK", "hold", "WR-02#g|WR-09#g"),
    ("D2L-RANK", "hold", "WR-08#g|WR-09#g"),
)
EXPECTED_NOTES = (("D2L-RANK", "note", "SR-01#a|SR-01#b"),)
EXPECTED_COUNTS = {"hold": 15, "note": 1, "fail": 0}


def sha256_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path):
    try:
        return str(Path(path).relative_to(ROOT))
    except ValueError:
        return str(path)


def child_env():
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return environment


def load_peer(path):
    return runpy.run_path(str(path))


def load_packet_strict(text):
    return load_peer(PROJECTOR)["load_packet_strict"](text)


def key_of(finding):
    return (finding.get("id"), finding.get("severity"), str(finding.get("where")))


def detail_of(finding):
    return finding.get("detail", "")


def run_gate(gate_path, input_path, cwd):
    return subprocess.run(
        [sys.executable, str(gate_path), str(input_path)],
        capture_output=True, text=True, cwd=str(cwd), env=child_env(), check=False)


def gate_bundle(input_path, cwd, gates_dir=GATES_DIR):
    records = []
    for name in GATE_NAMES:
        gate_path = gates_dir / name
        if not gate_path.exists():
            return None, "gate missing: %s" % name
        proc = run_gate(gate_path, input_path, cwd)
        if proc.returncode not in (0, 1):
            return None, "%s: exit %d: %s" % (name, proc.returncode,
                                              proc.stderr.strip()[:200])
        records.append({"gate": name, "exit": proc.returncode,
                        "findings": [line for line in proc.stdout.splitlines()
                                     if line.startswith(FINDING_PREFIX)],
                        "sha256": sha256_bytes(proc.stdout.encode())})
    return records, None


def grading(packet_path, pkt_arg=None, typed_arg=None, gates_dir=GATES_DIR,
            expected_path=EXPECTED_HOLDS_PATH):
    """Run L1-L4 once; returns the result dict (never raises for input)."""
    checks = []

    def check(check_id, ok, detail=""):
        checks.append({"id": check_id, "ok": bool(ok),
                       "detail": detail if not ok else ""})
        return bool(ok)

    result = {"exit": 2, "checks": checks, "typed": None, "legacy": None,
              "deltas": None, "findings": [], "routing": [], "pins": {}}
    adapter_ns = load_peer(ADAPTER)

    # ---- L1 build --------------------------------------------------------
    if typed_arg is not None:
        typed_bytes = Path(typed_arg).read_bytes()
        loaded = load_packet_strict(typed_bytes.decode("utf-8"))
        if loaded["packet"] is None:
            check("L1-build", False, "typed packet unparseable: %s"
                  % loaded["findings"][:1])
            return result
        typed_doc = loaded["packet"]
        check("L1-build", True, "")
        adapter_inputs = None
    else:
        if not Path(packet_path).is_file():
            check("L1-build", False, "packet missing: %s" % rel(packet_path))
            return result
        built = adapter_ns["build"](Path(packet_path), Path(PROJECTION_DEFAULT))
        for name, record in built["inputs"].items():
            check("L1-%s" % name, record["ok"], record["detail"])
        if built["exit"] != 0:
            check("L1-build", False, "; ".join(built["problems"]))
            return result
        typed_bytes = built["payload"]
        typed_doc = built["doc"]
        adapter_inputs = built["inputs"]
        check("L1-build", True, "")

    routing = typed_doc.get("typed_channel") or []
    off_records = sorted(row.get("record") for row in routing if row.get("record"))
    result["routing"] = routing
    if typed_doc.get("schema") != "kotodama-typed-packet-v1":
        check("L1-schema", False, "typed packet schema is %r" % typed_doc.get("schema"))
    else:
        check("L1-schema", True, "")
    if not off_records:
        check("L1-routing", False, "no routed record: the typed packet is not typed")
        return result
    check("L1-routing", True, "")

    # ---- L2 channel ------------------------------------------------------
    legacy_bytes = None
    if typed_arg is not None:
        # reconstruct the legacy packet by moving the off-channel fields back
        rebuilt = copy.deepcopy(typed_doc)
        for row in routing:
            for entry in rebuilt.get("costumes") or []:
                if isinstance(entry, dict) and str(entry.get("id")) == row["record"]:
                    field = row.get("source_field") or "garment"
                    moved = row.get("off_channel_field") or "%s_gloss" % field
                    if moved in entry:
                        entry[field] = entry.pop(moved)
        rebuilt.pop("typed_channel", None)
        rebuilt.pop("typed_pipeline", None)
        rebuilt.pop("typed_assembly", None)
        rebuilt.pop("assembly", None)
        rebuilt.pop("pipeline_findings", None)
        rebuilt.pop("pipeline_counts", None)
        rebuilt.pop("schema", None)
        legacy_bytes = ("\n".join(load_peer(SERIALIZER)["yaml_lines"](rebuilt))
                        + "\n").encode("utf-8")
    else:
        legacy_bytes = Path(packet_path).read_bytes()

    with tempfile.TemporaryDirectory(prefix="typed-pipeline-gate-") as tmp:
        typed_file = Path(tmp) / "packet.d2.typed.yml"
        legacy_file = Path(tmp) / "packet.d2.yml"
        typed_file.write_bytes(typed_bytes)
        legacy_file.write_bytes(legacy_bytes)
        typed_gates, error = gate_bundle(typed_file, ROOT, gates_dir)
        if error:
            check("L2-channel", False, error)
            return result
        legacy_gates, error = gate_bundle(legacy_file, ROOT, gates_dir)
        if error:
            check("L2-channel", False, error)
            return result

    typed_lines = {item["gate"]: item["findings"] for item in typed_gates}
    legacy_lines = {item["gate"]: item["findings"] for item in legacy_gates}
    off_named = []
    for gate, lines in typed_lines.items():
        for line in lines:
            if any(record in line for record in off_records):
                off_named.append("%s: %s" % (gate, line))
    deltas = {}
    delta_ok = True
    delta_detail = []
    for gate in GATE_NAMES:
        legacy = list(legacy_lines.get(gate, []))
        typed = list(typed_lines.get(gate, []))
        removed = [line for line in legacy if line not in typed]
        added = [line for line in typed if line not in legacy]
        deltas[gate] = {"legacy_findings": len(legacy), "typed_findings": len(typed),
                        "removed": removed, "added": added}
        if added:
            delta_ok = False
            delta_detail.append("%s: unexpected added findings: %s" % (gate, added[:2]))
        if sorted(typed + removed) != sorted(legacy):
            delta_ok = False
            delta_detail.append("%s: retained findings are not the legacy set" % gate)
        for line in removed:
            if not line.startswith("FINDING PHON-") or \
                    not any(record in line for record in off_records):
                delta_ok = False
                delta_detail.append("%s: non-artifact removal: %s" % (gate, line))
    removed_total = sum(len(deltas[gate]["removed"]) for gate in GATE_NAMES)
    added_total = sum(len(deltas[gate]["added"]) for gate in GATE_NAMES)
    result["sound_channel"] = {"translated_on_sound_channel": len(off_named),
                               "removed": removed_total, "added": added_total,
                               "routed": len(off_records)}
    check("L2-channel",
          delta_ok and not off_named and removed_total == len(off_records),
          "; ".join(delta_detail)
          or ("off-channel lines in the typed run: %s" % off_named[:2]
              if off_named else "removed %d, routed %d" % (removed_total, len(off_records))))

    # ---- L3 holds --------------------------------------------------------
    findings = typed_doc.get("pipeline_findings") or []
    if typed_arg is None:
        findings = [{"id": item["id"], "code": item["code"],
                     "severity": item["severity"], "where": str(item["where"]),
                     "detail": item["detail"]} for item in findings]
    result["findings"] = findings
    observed = {key_of(item) for item in findings}
    holds = {item for item in observed if item[1] == "hold"}
    notes = {item for item in observed if item[1] == "note"}
    fails = {item for item in observed if item[1] not in ("hold", "note")}
    expected_pairs = set(EXPECTED_HOLDS) | set(EXPECTED_NOTES)
    check("L3-holds", holds == set(EXPECTED_HOLDS), "missing %s; extra %s"
          % (sorted(set(EXPECTED_HOLDS) - holds), sorted(holds - set(EXPECTED_HOLDS))))
    check("L3-notes", notes == set(EXPECTED_NOTES), "missing %s; extra %s"
          % (sorted(set(EXPECTED_NOTES) - notes), sorted(notes - set(EXPECTED_NOTES))))
    check("L3-fails", not fails, "fail set: %s" % sorted(fails))
    check("L3-counts", {severity: sum(1 for item in observed if item[1] == severity)
                        for severity in ("hold", "note", "fail")} == EXPECTED_COUNTS,
          "observed counts differ from %s" % EXPECTED_COUNTS)
    baseline = None
    if Path(expected_path).is_file():
        try:
            baseline = json.loads(Path(expected_path).read_text(encoding="utf-8"))
        except ValueError as exc:
            check("L3-baseline", False, "expected-holds.json unreadable: %s" % exc)
    else:
        check("L3-baseline", False, "missing: %s" % rel(expected_path))
    if baseline is not None:
        committed = {(item.get("id"), item.get("severity"), str(item.get("where")))
                     for item in (baseline.get("holds") or []) + (baseline.get("notes") or [])}
        details_committed = {(item.get("id"), str(item.get("where"))): item.get("detail")
                             for item in (baseline.get("holds") or []) + (baseline.get("notes") or [])}
        details_observed = {(item["id"], str(item["where"])): detail_of(item)
                            for item in findings}
        check("L3-baseline", committed == expected_pairs
              and (baseline.get("counts") or {}) == EXPECTED_COUNTS,
              "committed baseline disagrees with the embedded constant")
        check("L3-details", all(details_committed.get(key) == value
                                for key, value in details_observed.items()),
              "a detail string differs from the committed baseline")
        check("L3-baseline-set", committed == observed,
              "committed set differs from the observed finding set")
    else:
        check("L3-baseline-set", False, "no baseline to compare")

    # routing consistency: every owed-form hold names a routed record and every
    # routed record carries exactly one such hold (a dropped routing row, or a
    # hold without its routing row, is a defect — design §2.2 coverage, D18)
    hold_records = sorted(str(item["where"]) for item in findings
                          if item["id"] == "D2L-FORM-UNRESOLVED")
    hold_slots = sorted({match.group(1) for item in findings
                         if item["id"] == "D2L-FORM-UNRESOLVED"
                         and (match := re.search(r"label_id\s+(\S+)", detail_of(item)))})
    routed_slots = sorted(row.get("owed_slot") for row in routing
                          if row.get("owed_slot"))
    check("L3-routing-consistency",
          hold_records == off_records and hold_slots == routed_slots,
          "holds %s vs routed %s; owed slots %s vs routing %s"
          % (hold_records, off_records, hold_slots, routed_slots))

    # ---- L4 pins ---------------------------------------------------------
    pins = typed_doc.get("assembly") or {}
    result["pins"] = pins
    if typed_arg is None:
        expected_pins = {"packet_sha256": sha256_file(packet_path),
                         "projection_sha256": sha256_file(PROJECTION_DEFAULT),
                         "adapter_sha256": sha256_file(ADAPTER)}
        check("L4-pins", all(pins.get(key) == value
                             for key, value in expected_pins.items()),
              "pin mismatch: %s" % {k: (pins.get(k), v)
                                    for k, v in expected_pins.items()
                                    if pins.get(k) != v})
    else:
        check("L4-pins",
              pins.get("adapter_sha256") == sha256_file(ADAPTER),
              "frozen typed packet pins adapter %s, live adapter hashes %s"
              % (pins.get("adapter_sha256"), sha256_file(ADAPTER)))

    failed = [item for item in checks if not item["ok"]]
    result["exit"] = 0 if not failed else 1
    result["typed"] = typed_gates
    result["legacy"] = legacy_gates
    result["deltas"] = deltas
    result["typed_doc"] = typed_doc
    return result


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------


def report(result, stream=sys.stdout):
    if result["exit"] == 2:
        for item in result["checks"]:
            print("%s %s: %s" % ("ok  " if item["ok"] else "FAIL", item["id"],
                                 item["detail"]), file=stream)
        return 2
    print(BANNER, file=stream)
    holds = [item for item in result["findings"] if item["severity"] == "hold"]
    notes = [item for item in result["findings"] if item["severity"] == "note"]
    for item in holds:
        print("FINDING %s: [%s] %s — %s" % (item["id"], item["severity"],
                                            item["where"], item["detail"]), file=stream)
    for item in notes:
        print("NOTE %s: [%s] %s — %s" % (item["id"], item["severity"],
                                         item["where"], item["detail"]), file=stream)
    removed = sum(len(result["deltas"][gate]["removed"]) for gate in GATE_NAMES)
    print("channel: %d PHON artifact(s) retired, %d added, retained lines identical"
          % (removed, sum(len(result["deltas"][gate]["added"]) for gate in GATE_NAMES)),
          file=stream)
    for item in result["checks"]:
        print("%s %s%s" % ("ok  " if item["ok"] else "FAIL", item["id"],
                           "" if item["ok"] else " — %s" % item["detail"]), file=stream)
    failed = [item for item in result["checks"] if not item["ok"]]
    print("summary: %d/%d legs passed" % (len(result["checks"]) - len(failed),
                                          len(result["checks"])), file=stream)
    return result["exit"]


def json_document(result):
    if result["exit"] == 2:
        return {"ok": False, "exit_code": 2, "checks": result["checks"]}
    deltas = {gate: {"legacy_findings": result["deltas"][gate]["legacy_findings"],
                     "typed_findings": result["deltas"][gate]["typed_findings"],
                     "removed": len(result["deltas"][gate]["removed"]),
                     "added": len(result["deltas"][gate]["added"])}
              for gate in GATE_NAMES}
    return {
        "banner": BANNER,
        "checks": result["checks"],
        "counts": EXPECTED_COUNTS,
        "deltas": deltas,
        "exit_code": result["exit"],
        "findings": result["findings"],
        "gates": [{"gate": item["gate"], "exit": item["exit"],
                   "findings": len(item["findings"]), "stdout_sha256": item["sha256"]}
                  for item in result["typed"]],
        "ok": all(item["ok"] for item in result["checks"]),
        "packet": rel(PACKET_DEFAULT),
        "pins": result["pins"],
        "routing": result["routing"],
        "sound_channel": result.get("sound_channel", {}),
        "translated_on_sound_channel": (result.get("sound_channel") or {}).get(
            "translated_on_sound_channel"),
        "typed_packet": rel(ROOT / "examples/culture-d2/packet.d2.typed.yml"),
    }


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------


def selftest():
    """Mirrored positive path plus the design's §6 hazard controls."""
    passed, failed = [], []

    def check(label, condition, detail=""):
        (passed if condition else failed).append(label)
        print("%s %s%s" % ("ok  " if condition else "FAIL", label,
                           "" if condition else " — %s" % detail))

    # the embedded constant and the committed record, both directions
    baseline = None
    if EXPECTED_HOLDS_PATH.is_file():
        baseline = json.loads(EXPECTED_HOLDS_PATH.read_text(encoding="utf-8"))
    committed = {(item.get("id"), item.get("severity"), str(item.get("where")))
                 for item in ((baseline or {}).get("holds") or [])
                 + ((baseline or {}).get("notes") or [])}
    check("constant == committed expected-holds.json (both directions)",
          baseline is not None
          and committed == set(EXPECTED_HOLDS) | set(EXPECTED_NOTES)
          and (baseline.get("counts") or {}) == EXPECTED_COUNTS,
          "baseline %s" % (rel(EXPECTED_HOLDS_PATH) if baseline else "missing"))

    with tempfile.TemporaryDirectory(prefix="typed-pipeline-gate-selftest-") as tmpdir:
        mirror = Path(tmpdir) / "repo"
        (mirror / "tools/gates").mkdir(parents=True)
        for name in ("assemble-d2-typed.py", "assemble-d2.py", "d2-typed-labels.py"):
            shutil.copyfile(ROOT / "tools" / name, mirror / "tools" / name)
        for name in GATE_NAMES:
            shutil.copyfile(GATES_DIR / name, mirror / "tools/gates" / name)
        shutil.copyfile(Path(__file__), mirror / "tools/gates/typed-pipeline-gate.py")
        shutil.copytree(ROOT / "examples/culture-d2", mirror / "examples/culture-d2",
                        ignore=shutil.ignore_patterns("__pycache__"))
        tool = mirror / "tools/gates/typed-pipeline-gate.py"

        def run(*args, tree=mirror, cwd=None):
            return subprocess.run([sys.executable, str(tool), *args],
                                  capture_output=True, text=True,
                                  cwd=str(cwd or tree), env=child_env(), check=False)

        first = run()
        check("positive: exit 0", first.returncode == 0,
              "exit %d: %s" % (first.returncode, first.stdout[-400:] or first.stderr[-400:]))
        check("positive: banner present and red-at-design-level wording",
              first.stdout.startswith("TYPED-PIPELINE:"), first.stdout[:120])
        check("positive: 15 FINDING lines and 1 NOTE line",
              sum(1 for line in first.stdout.splitlines()
                  if line.startswith(FINDING_PREFIX)) == 15
              and sum(1 for line in first.stdout.splitlines()
                      if line.startswith(NOTE_PREFIX)) == 1,
              "FINDING/NOTE counts differ")
        second = run()
        check("determinism: two runs byte-identical", second.stdout == first.stdout)
        js = run("--json")
        payload = json.loads(js.stdout) if js.stdout.strip().startswith("{") else {}
        check("--json: one document, ok true, 16 findings",
              js.returncode == 0 and payload.get("ok") is True
              and len(payload.get("findings") or []) == 16, js.stdout[:160])

        # hazard control 1: a translated label smuggled back onto the sound channel
        built = mirror / "examples/culture-d2/packet.d2.typed.yml"
        original = built.read_bytes()
        smuggle = original.replace(b'    garment_gloss: "winter valley coat',
                                   b'    garment: "winter valley coat', 1)
        assert smuggle != original, "the fixture must carry the moved gloss field"
        smuggled = Path(tmpdir) / "smuggled-typed.yml"
        smuggled.write_bytes(smuggle)
        smuggled_run = run(str(smuggled))
        check("smuggle control: exit 1 and L2 names the channel",
              smuggled_run.returncode == 1 and "L2-channel" in smuggled_run.stdout,
              "exit %d" % smuggled_run.returncode)

        # hazard control 2: an owed form dropped from the routing table (hold laundered)
        dropped = original.replace(b'    owed_slot: "LEX-GAR-01"\n', b"", 1)
        assert dropped != original
        dropped_path = Path(tmpdir) / "dropped-typed.yml"
        dropped_path.write_bytes(dropped)
        dropped_run = run(str(dropped_path))
        check("dropped routing row: exit 1 (L3 or L4 fires)",
              dropped_run.returncode == 1, "exit %d" % dropped_run.returncode)

        # hazard control 3: a hold laundered into a note
        laundered = _launder_hold(mirror, tmpdir)
        launder_run = run(str(laundered))
        check("laundered hold: exit 1 and L3 fires",
              launder_run.returncode == 1 and "L3" in launder_run.stdout,
              "exit %d" % launder_run.returncode)

        # hazard control 4: the adapter edited under a frozen packet (pin break)
        adapter_copy = mirror / "tools/assemble-d2-typed.py"
        adapter_bytes = adapter_copy.read_bytes()
        adapter_copy.write_bytes(adapter_bytes + b"\n# drift\n")
        pin_run = run(str(built))
        check("adapter drift: the frozen packet's adapter pin breaks (exit 1)",
              pin_run.returncode == 1 and "L4-pins" in pin_run.stdout,
              "exit %d" % pin_run.returncode)
        adapter_copy.write_bytes(adapter_bytes)

        # malformed input: stable exit 2
        broken = Path(tmpdir) / "broken.yml"
        broken.write_text("name: X\nphonology:\n  consonants: [p, t\n", encoding="utf-8")
        bad = run(str(broken))
        check("malformed packet: exit 2, no traceback",
              bad.returncode == 2 and "Traceback" not in bad.stdout + bad.stderr,
              "exit %d" % bad.returncode)
        missing = run(str(Path(tmpdir) / "absent.yml"))
        check("missing packet: exit 2", missing.returncode == 2,
              "exit %d" % missing.returncode)

    total = len(passed) + len(failed)
    if failed:
        print("selftest: %d/%d checks passed — failures: %s"
              % (len(passed), total, "; ".join(failed)), file=sys.stderr)
        return 1
    print("selftest: %d/%d checks passed — constant==baseline, the mirrored four "
          "legs, determinism/--json, and the smuggled-label, dropped-row, "
          "laundered-hold, adapter-drift, malformed and missing controls; no file "
          "outside the temporary mirror touched" % (len(passed), total))
    return 0


def _launder_hold(mirror, tmpdir):
    """Build a typed packet whose ten owed-form holds are renamed to notes."""
    built = mirror / "examples/culture-d2/packet.d2.typed.yml"
    text = built.read_text(encoding="utf-8")
    return_me = Path(tmpdir) / "laundered-typed.yml"
    swapped = text.replace('severity: "hold"', 'severity: "note"')
    return_me.write_text(swapped, encoding="utf-8")
    return return_me


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("packet", nargs="?", default=str(PACKET_DEFAULT),
                        help="packet to grade (default: %s)" % rel(PACKET_DEFAULT))
    parser.add_argument("--json", action="store_true", help="one JSON document")
    parser.add_argument("--selftest", "--self-test", action="store_true", dest="selftest",
                        help="mirrored four legs plus hazard controls")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    candidate = Path(args.packet)
    typed_arg = None
    if candidate.is_file():
        try:
            head = load_packet_strict(candidate.read_text(encoding="utf-8"))
            document = head.get("packet") or {}
        except (ValueError, OSError):
            document = {}
        if document.get("typed_channel") is not None:
            typed_arg = candidate
    result = grading(candidate, typed_arg=typed_arg)
    if args.json:
        print(json.dumps(json_document(result), sort_keys=True, ensure_ascii=False))
        return result["exit"]
    return report(result)


if __name__ == "__main__":
    sys.exit(main())
