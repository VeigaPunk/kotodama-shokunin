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
file carrying `typed_channel` is graded as the build product, and L3/L4 run as
usual. For L2 the legacy side is the source the typed packet *declares* under
`typed_assembly.packet`, digest-checked against its own `assembly.packet_sha256`
— the gate's own rebuild of that source is not byte-faithful (the serializer
escapes backslashes a second time and re-quotes nulls), so grading a rebuild
manufactured DERIV-REPLAY findings that exist in no file (round-24 cold-run C2).
A declared source that is unreadable or stale against its pin is an input-class
refusal (exit 2, named) rather than a verdict; only an unnamed typed packet falls
back to the rebuild, and then only if the rebuild round-trips.

Declared assembler identity (round-18 O claim). The gate grades more than one
pipeline family by *declaration*: the graded packet may carry a `typed_pipeline`
block (or an `assembly.generator` / `assembly.assembler` key) naming the
assembler, projection, adapter, expected-holds file and legacy packet, and the
CLI adds `--assembler/--projection/--adapter/--expected/--legacy-packet`
overrides. Precedence is flags > packet declaration > family convention
(`examples/culture-<family>/…`, the D2/D3 naming) > D2 defaults; with nothing
declared the resolution lands on exactly the D2 paths, so the default run is
byte-identical to the pre-generalization gate. When a non-D2 assembler is
declared, L1 runs an `L1-assembler` identity leg that calls the declared
assembler's own `assemble()` — the same call `--check` makes, never a
re-implementation — and requires the packet bytes (and, when the packet pins
`assembly.assembler_sha256`, the live assembler bytes) to match; a mismatch is
exit 2. `--selftest-generalized` drives that mechanism over fixture trees in
one temporary directory.
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
# The argot-derivation leg (round-25 D claim) lives in a sibling gate that
# replays the two declared argot operations and the packet's own formation
# claims. It is loaded read-only by path and invoked with the same single
# input, so the leg is the sibling's bytes, never a re-implementation here.
ARGOT_GATE = GATES_DIR / "argot-derivation-gate.py"
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

# The D2 identity the resolver returns when nothing is declared — the exact
# pre-generalization constants, kept equal to them (round-18 O claim: the
# default path is byte-identical; `--selftest-generalized` asserts the equality).
PROFILE_DEFAULT = GATES_DIR / "typed-pipelines.json"
D2_DEFAULTS = {
    "packet": PACKET_DEFAULT,
    "typed": ROOT / "examples/culture-d2/packet.d2.typed.yml",
    "projection": PROJECTION_DEFAULT,
    "adapter": ADAPTER,
    "expected": EXPECTED_HOLDS_PATH,
    "assembler": SERIALIZER,
    "projector": PROJECTOR,
}
# Keys a packet may declare about its own pipeline (additive: only the D2 path
# keys are honoured, anything else in the block is left to its owner).
DECLARED_ALIASES = {
    "assembler": "assembler",
    "generator": "assembler",
    "projection": "projection",
    "adapter": "adapter",
    "expected": "expected",
    "expected_holds": "expected",
    "packet": "packet",
    "legacy_packet": "packet",
    "typed_packet": "typed",
    "projector": "projector",
}


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


def load_packet_strict(text, projector=None):
    return load_peer(projector or PROJECTOR)["load_packet_strict"](text)


def key_of(finding):
    return (finding.get("id"), finding.get("severity"), str(finding.get("where")))


def detail_of(finding):
    return finding.get("detail", "")


def nullish(value):
    """A missing key or a null-ish value (`null`, `none`, `~`, empty).

    The lane's reader keeps an unquoted `null` as the *string* `"null"`, so a
    plain truthiness test would read a null slot as a present one.
    """
    return not isinstance(value, str) or value.strip().lower() in ("", "null", "none", "~")


def moved_field(row):
    """The field a routing row moved off the sound channel.

    A missing key or a null-ish value (`null`, `none`, `~`, empty — the lane's
    reader keeps an unquoted `null` as the string) means the row stays on
    channel, the D4 register class the round-17 brief declares.
    """
    value = row.get("off_channel_field")
    return None if nullish(value) else value


def owed_slot_of(row):
    """The slot a routing row owes, or None when the row owes no slot.

    `owed_slot: null` is the D4 register class: the record is routed off the
    sound channel but owes no form slot, so it contributes no owed slot to the
    routing-consistency set. The null-ish test is the same one `moved_field`
    applies, so the two halves of a routing row cannot disagree.
    """
    value = row.get("owed_slot")
    return None if nullish(value) else value


# --------------------------------------------------------------------------
# declared pipeline identity (round-18 O claim)
# --------------------------------------------------------------------------


def candidate_path(value):
    """A declared path string as a path; relative values resolve against ROOT."""
    if not isinstance(value, str) or not value.strip():
        return None
    path = Path(value.strip())
    return path if path.is_absolute() else ROOT / path


def family_of(path):
    """`examples/culture-d4/packet.d4.yml` -> `d4`; None when not that shape."""
    match = re.fullmatch(r"culture-([a-z0-9]+)", Path(path).parent.name)
    return match.group(1) if match else None


def family_paths(family):
    """The lane's per-family naming convention (D3 idiom, brief §9.1)."""
    base = ROOT / ("examples/culture-%s" % family)
    assembler = ROOT / ("tools/assemble-culture-%s.py" % family)
    if not assembler.is_file():
        assembler = ROOT / ("tools/assemble-%s.py" % family)
    projector = ROOT / ("tools/%s-typed-labels.py" % family)
    if not projector.is_file():
        projector = PROJECTOR
    return {
        "packet": base / ("packet.%s.yml" % family),
        "typed": base / ("packet.%s.typed.yml" % family),
        "projection": base / ("typed-labels.%s.yml" % family),
        "adapter": ROOT / ("tools/assemble-%s-typed.py" % family),
        "expected": base / "expected-holds.json",
        "assembler": assembler,
        "projector": projector,
    }


def family_projector(packet_path):
    """The family's own reader when one exists (D2's reader otherwise)."""
    family = family_of(packet_path)
    if family and family != "d2":
        candidate = ROOT / ("tools/%s-typed-labels.py" % family)
        if candidate.is_file():
            return candidate
    return PROJECTOR


def declared_paths(document):
    """What the graded packet declares about its own pipeline, if anything."""
    declared = {}
    if not isinstance(document, dict):
        return declared
    for block in (document.get("typed_pipeline"), document.get("assembly")):
        if not isinstance(block, dict):
            continue
        for key, value in block.items():
            if key in DECLARED_ALIASES and key not in declared:
                declared[key] = value
    # A typed artifact names its own source under `typed_assembly.packet` (its
    # `assembly` block names the source's *digests*). Only that one key is read:
    # `typed_assembly.generator` is the typed *adapter*, not the assembler, so
    # the block cannot be scanned wholesale without mis-binding the identity.
    typed_block = document.get("typed_assembly")
    if isinstance(typed_block, dict) and isinstance(typed_block.get("packet"), str):
        declared.setdefault("packet", typed_block["packet"])
    return declared


def load_profile(document, flags=None):
    """The sha-pinned pipeline profile matching the graded packet (design §4).

    The flagless channel `tools/replay-frozen.py` can replay: matching is by the
    packet's own `assembly.generator` string, never by filename. Returns
    `(info, chosen)`; `info` is None when no profile file exists.
    """
    path = candidate_path((flags or {}).get("profile")) or PROFILE_DEFAULT
    if not path.is_file():
        return None, None
    info = {"file": path, "problems": []}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        info["problems"].append("unreadable: %s" % exc)
        return info, None
    info["payload"] = payload
    generator = None
    if isinstance(document, dict) and isinstance(document.get("assembly"), dict):
        generator = document["assembly"].get("generator")
    info["generator"] = generator
    profiles = []
    for key in ("profiles", "pipelines", "families"):
        value = payload.get(key) if isinstance(payload, dict) else None
        if isinstance(value, dict):
            profiles = list(value.values())
            break
        if isinstance(value, list):
            profiles = value
            break
    info["profiles"] = len(profiles)
    chosen = None
    for profile in profiles:
        if not isinstance(profile, dict):
            continue
        match = profile.get("match") or {}
        if generator and match.get("assembly_generator") == generator:
            chosen = profile
            break
    info["chosen"] = (chosen or {}).get("id")
    return info, chosen


def profile_pins(profile, resolved):
    """Every pinned profile field re-verified against the live bytes."""
    checks = []
    if not isinstance(profile, dict):
        return checks
    for key in ("packet", "assembler", "projection", "adapter", "expected"):
        field = profile.get(key)
        if not isinstance(field, dict):
            continue
        target = candidate_path(field.get("path")) or resolved.get(key)
        pinned = field.get("sha256")
        entry = {"field": key, "path": target, "pinned": pinned, "live": None, "ok": True}
        if target is not None and target.is_file():
            entry["live"] = sha256_file(target)
        if isinstance(pinned, str) and pinned:
            entry["ok"] = entry["live"] == pinned
        elif pinned is None:
            entry["ok"] = True
            entry["detail"] = "path only: pin pending"
        checks.append(entry)
    return checks


def resolve_config(packet_path, document, flags=None):
    """flags > packet declaration > profile > family convention > D2 defaults.

    An unresolved key keeps the D2 default, and with every key on its D2 value
    the run is `generalized = False`: no declared-identity leg, no extra check,
    no extra output — the pre-generalization behavior exactly.
    """
    flags = {key: value for key, value in (flags or {}).items() if value}
    resolved = dict(D2_DEFAULTS)
    family = family_of(packet_path)
    if family and family != "d2":
        resolved.update(family_paths(family))
    profile_info, profile = load_profile(document, flags)
    if isinstance(profile, dict):
        for key in D2_DEFAULTS:
            field = profile.get(key)
            if isinstance(field, dict):
                field = field.get("path")
            path = candidate_path(field if isinstance(field, str) else None)
            if path is not None:
                resolved[key] = path
    declared = declared_paths(document)
    for key, value in declared.items():
        path = candidate_path(value)
        if path is not None:
            resolved[DECLARED_ALIASES[key]] = path
    for key in D2_DEFAULTS:
        path = candidate_path(flags.get(key))
        if path is not None:
            resolved[key] = path
    resolved["family"] = family
    resolved["declared"] = declared
    resolved["flags"] = sorted(flags)
    resolved["profile"] = (profile or {}).get("id") if isinstance(profile, dict) else None
    resolved["profile_file"] = (profile_info or {}).get("file")
    resolved["profile_problems"] = list((profile_info or {}).get("problems") or [])
    resolved["profile_pins"] = profile_pins(profile, resolved)
    resolved["generalized"] = bool(flags) or any(
        resolved[key] != D2_DEFAULTS[key] for key in D2_DEFAULTS)
    return resolved


def resolution_line(config):
    """The one line a non-default run prints: the resolved, digest-bearing set."""
    if not config.get("generalized"):
        return None
    parts = ["declared pipeline: family %s" % config.get("family")]
    profile_file = config.get("profile_file")
    if profile_file:
        digest = sha256_file(profile_file)[:12] if Path(profile_file).is_file() else "absent"
        parts.append("profile %s (sha256 %s)"
                     % (rel(profile_file), digest if config.get("profile") else "no-match"))
    for key in ("assembler", "adapter", "projection", "expected"):
        target = Path(config[key])
        digest = sha256_file(target)[:12] if target.is_file() else "absent"
        parts.append("%s %s (sha256 %s)" % (key, rel(target), digest))
    return "; ".join(parts)


def assembler_identity(packet_path, assembler_path, declared_sha=None):
    """The declared assembler's own build must reproduce the packet bytes.

    This is the byte comparison `--check` performs, through the same call
    (`assemble()`); the gate never re-implements an assembler. A packet that
    pins `assembly.assembler_sha256` additionally has the live assembler bytes
    verified against that pin.
    """
    try:
        namespace = load_peer(assembler_path)
        build = namespace.get("assemble")
    except Exception as exc:
        return False, "assembler unreadable: %s: %s: %s" % (
            rel(assembler_path), type(exc).__name__, exc)
    if not callable(build):
        return False, "%s has no assemble() build path" % rel(assembler_path)
    try:
        expected = build()
    except Exception as exc:
        return False, "assembler refused the components: %s: %s" % (
            type(exc).__name__, exc)
    if not isinstance(expected, bytes):
        return False, "%s assemble() did not return bytes" % rel(assembler_path)
    actual = Path(packet_path).read_bytes()
    if actual != expected:
        return False, "packet bytes %s are not %s's deterministic assembly (%s)" % (
            sha256_bytes(actual)[:12], rel(assembler_path), sha256_bytes(expected)[:12])
    if declared_sha:
        live = sha256_file(assembler_path)
        if declared_sha != live:
            return False, "assembler self-pin broken: packet pins %s, live %s hashes %s" % (
                str(declared_sha)[:12], rel(assembler_path), live[:12])
    return True, ""


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
            flags=None, config=None):
    """Run L1-L4 once; returns the result dict (never raises for input)."""
    checks = []

    def check(check_id, ok, detail=""):
        checks.append({"id": check_id, "ok": bool(ok),
                       "detail": detail if not ok else ""})
        return bool(ok)

    result = {"exit": 2, "checks": checks, "typed": None, "legacy": None,
              "deltas": None, "findings": [], "routing": [], "pins": {}}
    loaded = None
    document = None
    reader = family_projector(typed_arg or packet_path)
    if typed_arg is not None:
        typed_bytes = Path(typed_arg).read_bytes()
        loaded = load_packet_strict(typed_bytes.decode("utf-8"), reader)
        document = loaded["packet"]
    elif Path(packet_path).is_file():
        try:
            parsed = load_packet_strict(Path(packet_path).read_text(encoding="utf-8"), reader)
            document = parsed.get("packet")
        except Exception:
            document = None
    config = config or resolve_config(packet_path, document, flags)
    if typed_arg is not None and config["projector"] != reader:
        loaded = load_packet_strict(typed_bytes.decode("utf-8"), config["projector"])
        document = loaded["packet"]
    result["config"] = config
    generalized = config["generalized"]
    identity_requested = (config["assembler"] != SERIALIZER) or bool(
        (flags or {}).get("assembler"))

    # ---- L3b argot derivation (round-25 D claim) -------------------------
    # The register-scoped derivation relation the round-17 Δ3 forecast. The
    # sibling gate owns the semantics and is invoked with the same single input
    # (never re-implemented here); its FAIL findings join this verdict, so a
    # form whose stated inputs and rules do not yield it cannot read green even
    # when an earlier L1 leg refuses the run. Guarded on the generalized path:
    # the D2 default run keeps its pre-round-25 output byte for byte.
    argot_lines = []
    if generalized and ARGOT_GATE.is_file():
        proc = run_gate(ARGOT_GATE, packet_path if typed_arg is None else typed_arg,
                        ROOT)
        result["argot"] = {"exit": proc.returncode,
                           "sha256": sha256_bytes(proc.stdout.encode())}
        argot_lines = [line for line in proc.stdout.splitlines()
                       if line.startswith("FINDING D4L-ARGOT-")]
        result["argot_lines"] = argot_lines
        argot_fails = [line for line in argot_lines if "FAIL" in line]
        if argot_fails:
            for line in argot_fails:
                result["findings"].append({"id": "D4L-ARGOT-DERIV", "severity": "fail",
                                           "where": "argot-derivation-gate",
                                           "detail": line})
        check("L3b-argot", not argot_fails and proc.returncode in (0, 1),
              "argot leg exit %d: %s" % (proc.returncode,
                                         "; ".join(argot_fails[:2]) or "unreadable"))

    # ---- L1 declared identity -------------------------------------------
    if generalized and config.get("profile_problems"):
        check("L1-profile", False, "; ".join(config["profile_problems"]))
        return result
    if generalized and config.get("profile_pins"):
        broken = [item for item in config["profile_pins"] if not item["ok"]]
        check("L1-profile", not broken,
              "; ".join("%s: pins %s, live %s (%s)"
                        % (item["field"], str(item["pinned"])[:12],
                           str(item["live"])[:12], rel(item["path"]))
                        for item in broken))
        if broken:
            return result
    if generalized and identity_requested:
        declared_sha = None
        if isinstance(document, dict) and isinstance(document.get("assembly"), dict):
            declared_sha = document["assembly"].get("assembler_sha256")
        ok, detail = assembler_identity(
            config["packet"] if typed_arg is not None else packet_path,
            config["assembler"], declared_sha)
        check("L1-assembler", ok, detail)
        if not ok:
            return result
    expected_holds, expected_notes, expected_counts = EXPECTED_HOLDS, EXPECTED_NOTES, EXPECTED_COUNTS
    expected_baseline = None
    if generalized:
        expected_path = config["expected"]
        if not expected_path.is_file():
            check("L1-expected-holds", False, "missing: %s" % rel(expected_path))
            return result
        try:
            expected_baseline = json.loads(expected_path.read_text(encoding="utf-8"))
        except ValueError as exc:
            check("L1-expected-holds", False, "unreadable: %s: %s"
                  % (rel(expected_path), exc))
            return result
        expected_holds = tuple(
            (item.get("id"), item.get("severity"), str(item.get("where")))
            for item in (expected_baseline.get("holds") or []))
        expected_notes = tuple(
            (item.get("id"), item.get("severity"), str(item.get("where")))
            for item in (expected_baseline.get("notes") or []))
        expected_counts = dict(expected_baseline.get("counts") or {})
        consistent = (expected_counts.get("hold") == len(expected_holds)
                      and expected_counts.get("note") == len(expected_notes)
                      and expected_counts.get("fail") == 0
                      and expected_baseline.get("schema") in (None, SCHEMA))
        check("L1-expected-holds", consistent,
              "inconsistent expected file: schema %r, counts %s, %d holds, %d notes"
              % (expected_baseline.get("schema"), expected_counts,
                 len(expected_holds), len(expected_notes)))
        if not consistent:
            return result
    result["expected_counts"] = expected_counts

    # ---- L1 build --------------------------------------------------------
    if typed_arg is not None:
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
        if not config["adapter"].is_file():
            check("L1-build", False, "adapter missing: %s" % rel(config["adapter"]))
            return result
        try:
            adapter_ns = load_peer(config["adapter"])
            built = adapter_ns["build"](Path(packet_path), Path(config["projection"]))
        except Exception as exc:
            check("L1-build", False, "adapter %s refused the run: %s: %s"
                  % (rel(config["adapter"]), type(exc).__name__, exc))
            return result
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
    # rows whose form field was moved off the sound channel (D2: every row) vs
    # rows the routing keeps on channel (`off_channel_field: null`, D4 register
    # class) — only the moved ones may retire gate lines.
    moved_records = sorted(row.get("record") for row in routing
                           if row.get("record") and moved_field(row))
    retained_records = sorted(row.get("record") for row in routing
                              if row.get("record") and not moved_field(row))
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
    # The legacy side of the comparison. A typed packet handed in directly does
    # not carry its source bytes, and the gate's own rebuild of them is not
    # byte-faithful: the serializer's `scalar` escapes backslashes a second time
    # and the reader keeps an unquoted `null` as the string, so grading a rebuild
    # manufactures DERIV-REPLAY findings that exist in no file (round-24 cold-run
    # C2). The graded legacy side is therefore the source the typed packet
    # declares, digest-checked against the pin the typed packet carries. Only
    # when no source resolves does the rebuild stand in — and then it is trusted
    # only if it round-trips, so a manufactured delta becomes a named
    # input-class refusal (exit 2) instead of a plausible false red.
    legacy_bytes = None
    result["input_class"] = "source"
    result["rebuild_faithful"] = None
    if typed_arg is not None:
        declared_source = Path(config["packet"])
        declared_sha = (typed_doc.get("assembly") or {}).get("packet_sha256")
        typed_block = typed_doc.get("typed_assembly")
        # only a typed packet that *names* its source is graded against one: an
        # unnamed fallback may be a family convention that never built this
        # artifact, so the rebuild stays the default there.
        source_named = isinstance(typed_block, dict) and isinstance(
            typed_block.get("packet"), str) and typed_block["packet"].strip()
        source_named = bool(source_named or "packet" in (config.get("flags") or []))
        source_bytes = (declared_source.read_bytes()
                        if source_named and declared_source.is_file() else None)
        if source_bytes is not None and (declared_sha is None
                                         or sha256_bytes(source_bytes) == declared_sha):
            legacy_bytes = source_bytes
            result["input_class"] = "typed-declared-source"
        elif source_named and source_bytes is None:
            result["input_class"] = "typed-unresolvable"
            result["input_class_error"] = True
            check("L2-channel", False,
                  "typed-packet input without its source: %s declares source %s, "
                  "which is unreadable — a typed packet is the pipeline's output, "
                  "not a gate input; restore the source or grade it directly"
                  % (rel(typed_arg), rel(declared_source)))
            return result
        elif source_named:
            result["input_class"] = "typed-stale-source"
            result["input_class_error"] = True
            check("L2-channel", False,
                  "typed packet pins source %s, %s hashes %s — the derived artifact "
                  "is stale against its own source; re-derive it or grade the source"
                  % (str(declared_sha)[:12], rel(declared_source),
                     sha256_bytes(source_bytes or b"")[:12]))
            return result
        else:
            rebuilt = copy.deepcopy(typed_doc)
            for row in routing:
                for entry in rebuilt.get("costumes") or []:
                    if isinstance(entry, dict) and str(entry.get("id")) == row["record"]:
                        field = row.get("source_field") or "garment"
                        moved = moved_field(row) or "%s_gloss" % field
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
            result["input_class"] = "typed-rebuilt"
            result["rebuild_faithful"] = (
                load_packet_strict(legacy_bytes.decode("utf-8"), reader)["packet"] == rebuilt)
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
            if any(record in line for record in moved_records):
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
                    not any(record in line for record in moved_records):
                delta_ok = False
                delta_detail.append("%s: non-artifact removal: %s" % (gate, line))
    removed_total = sum(len(deltas[gate]["removed"]) for gate in GATE_NAMES)
    added_total = sum(len(deltas[gate]["added"]) for gate in GATE_NAMES)
    result["sound_channel"] = {"translated_on_sound_channel": len(off_named),
                               "removed": removed_total, "added": added_total,
                               "routed": len(moved_records)}
    if generalized:
        result["sound_channel"]["retained_on_channel"] = len(retained_records)
        # D4 family: two routing rows per costume (garment-field row + owed-slot
        # row) but exactly one field move per costume — the removed-artifact
        # count must equal the costumes whose field actually moved, not the
        # routing-row count. D2: every moved record is a costume record, so
        # this reduces to the legacy comparison unchanged.
        costume_ids = {str(entry.get("id"))
                       for entry in (typed_doc.get("costumes") or [])
                       if isinstance(entry, dict)}
        field_moved = sorted(name for name in moved_records if name in costume_ids)
    else:
        field_moved = moved_records
    l2_ok = delta_ok and not off_named and removed_total == len(field_moved)
    l2_detail = ("; ".join(delta_detail)
                 or ("off-channel lines in the typed run: %s" % off_named[:2]
                     if off_named else "removed %d, routed %d"
                     % (removed_total, len(moved_records))))
    if not l2_ok and result.get("rebuild_faithful") is False:
        result["input_class"] = "typed-unfaithful-rebuild"
        result["input_class_error"] = True
        l2_detail = ("typed-packet input: %s declares no source packet that hashes to "
                     "its own assembly.packet_sha256, and the gate's rebuild of that "
                     "source does not round-trip — the serializer escapes backslashes "
                     "a second time and re-quotes nulls, so this delta is manufactured "
                     "by the rebuild, not found in any file; grade the source packet "
                     "(%s) instead. Underlying delta: %s"
                     % (rel(typed_arg), rel(config["packet"]), l2_detail))
    check("L2-channel", l2_ok, l2_detail)
    # a routing row that keeps its record on the sound channel may not remove
    # that record's inventory line (D4 register class: routing, not deletion)
    if retained_records:
        lost = [record for record in retained_records
                if any(record in line for lines in legacy_lines.values() for line in lines)
                and not any(record in line for lines in typed_lines.values() for line in lines)]
        check("L2-retention", not lost,
              "on-channel records lost from the typed run: %s" % lost)

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
    expected_pairs = set(expected_holds) | set(expected_notes)
    check("L3-holds", holds == set(expected_holds), "missing %s; extra %s"
          % (sorted(set(expected_holds) - holds), sorted(holds - set(expected_holds))))
    check("L3-notes", notes == set(expected_notes), "missing %s; extra %s"
          % (sorted(set(expected_notes) - notes), sorted(notes - set(expected_notes))))
    check("L3-fails", not fails, "fail set: %s" % sorted(fails))
    check("L3-counts", {severity: sum(1 for item in observed if item[1] == severity)
                        for severity in ("hold", "note", "fail")} == expected_counts,
          "observed counts differ from %s" % expected_counts)
    baseline = expected_baseline
    if not generalized:
        if EXPECTED_HOLDS_PATH.is_file():
            try:
                baseline = json.loads(EXPECTED_HOLDS_PATH.read_text(encoding="utf-8"))
            except ValueError as exc:
                check("L3-baseline", False, "expected-holds.json unreadable: %s" % exc)
        else:
            check("L3-baseline", False, "missing: %s" % rel(EXPECTED_HOLDS_PATH))
    if baseline is not None:
        committed = {(item.get("id"), item.get("severity"), str(item.get("where")))
                     for item in (baseline.get("holds") or []) + (baseline.get("notes") or [])}
        details_committed = {(item.get("id"), str(item.get("where"))): item.get("detail")
                             for item in (baseline.get("holds") or []) + (baseline.get("notes") or [])}
        details_observed = {(item["id"], str(item["where"])): detail_of(item)
                            for item in findings}
        if generalized:
            check("L3-baseline", committed == expected_pairs
                  and (baseline.get("counts") or {}) == expected_counts,
                  "declared baseline disagrees with its own expected set")
        else:
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

    # routing consistency: every off-channel hold names a moved routing record
    # and every moved record carries exactly one such hold (a dropped routing
    # row, or a hold without its routing row, is a defect — design §2.2
    # coverage, D18). The hold id is read off the routing rows, so a D4-family
    # packet checks its own class (`D4L-FORM-UNRESOLVED`).
    routing_hold_ids = sorted({row.get("hold") for row in routing
                               if moved_field(row) and row.get("hold")})
    hold_records = sorted(str(item["where"]) for item in findings
                          if item["id"] in routing_hold_ids)
    hold_slots = sorted({match.group(1) for item in findings
                         if item["id"] in routing_hold_ids
                         and (match := re.search(r"label_id\s+(\S+)", detail_of(item)))})
    routed_slots = sorted(slot for row in routing
                          if moved_field(row) and (slot := owed_slot_of(row)))
    check("L3-routing-consistency",
          hold_records == moved_records and hold_slots == routed_slots,
          "holds %s vs routed %s; owed slots %s vs routing %s"
          % (hold_records, moved_records, hold_slots, routed_slots))

    # ---- L4 pins ---------------------------------------------------------
    pins = typed_doc.get("assembly") or {}
    result["pins"] = pins
    if not generalized:
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
    else:
        # every pin the packet declares re-verifies against the bytes read; a
        # declared pin whose live file is gone is a could-not-evaluate
        live = {"packet_sha256": config["packet"],
                "projection_sha256": config["projection"],
                "adapter_sha256": config["adapter"],
                "assembler_sha256": config["assembler"]}
        expected_pins, missing, mismatched = {}, [], []
        for key, target in live.items():
            if key not in pins:
                continue
            if not target.is_file():
                missing.append("%s: live %s missing" % (key, rel(target)))
                continue
            expected_pins[key] = sha256_file(target)
            if pins.get(key) != expected_pins[key]:
                mismatched.append("%s: pins %s, live %s"
                                  % (key, str(pins.get(key))[:12], expected_pins[key][:12]))
        check("L4-pins",
              bool(expected_pins) and not missing and not mismatched,
              "; ".join(missing + mismatched)
              or "no pin declared: %s" % sorted(pins))

    failed = [item for item in checks if not item["ok"]]
    result["exit"] = 0 if not failed else 1
    if result.get("input_class_error"):
        result["exit"] = 2
    if generalized and any(item["id"] == "L4-pins" for item in failed):
        result["exit"] = 2
    result["typed"] = typed_gates
    result["legacy"] = legacy_gates
    result["deltas"] = deltas
    result["typed_doc"] = typed_doc
    return result


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------


def report(result, stream=sys.stdout, config=None):
    config = config or result.get("config") or {}
    line = resolution_line(config)
    # The argot leg's own findings always reach the reader, including on the
    # exit-2 path where an earlier L1 leg refused the run: a derivation failure
    # must be legible, not hidden behind the refusal that preceded it.
    argot_lines = result.get("argot_lines") or []
    if result["exit"] == 2:
        if line:
            print(line, file=stream)
        for item in argot_lines:
            print(item, file=stream)
        for item in result["checks"]:
            print("%s %s: %s" % ("ok  " if item["ok"] else "FAIL", item["id"],
                                 item["detail"]), file=stream)
        return 2
    print(BANNER, file=stream)
    if line:
        print(line, file=stream)
    for item in argot_lines:
        print(item, file=stream)
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


def json_document(result, config=None):
    config = config or result.get("config") or {}
    resolved = None
    if config.get("generalized"):
        resolved = {"assembler": rel(config["assembler"]),
                    "adapter": rel(config["adapter"]),
                    "expected": rel(config["expected"]),
                    "family": config.get("family"),
                    "flags": config.get("flags", []),
                    "packet": rel(config["packet"]),
                    "profile": config.get("profile"),
                    "profile_file": rel(config["profile_file"]) if config.get("profile_file") else None,
                    "profile_sha256": (sha256_file(config["profile_file"])
                                       if config.get("profile_file")
                                       and Path(config["profile_file"]).is_file() else None),
                    "projection": rel(config["projection"]),
                    "typed_packet": rel(config["typed"])}
    if result["exit"] == 2:
        document = {"ok": False, "exit_code": 2, "checks": result["checks"]}
        if result.get("argot_lines"):
            document["argot"] = result["argot_lines"]
        if resolved is not None:
            document["resolved"] = resolved
        return document
    deltas = {gate: {"legacy_findings": result["deltas"][gate]["legacy_findings"],
                     "typed_findings": result["deltas"][gate]["typed_findings"],
                     "removed": len(result["deltas"][gate]["removed"]),
                     "added": len(result["deltas"][gate]["added"])}
              for gate in GATE_NAMES}
    document = {
        "banner": BANNER,
        "checks": result["checks"],
        "counts": result.get("expected_counts") or EXPECTED_COUNTS,
        "deltas": deltas,
        "exit_code": result["exit"],
        "findings": result["findings"],
        "gates": [{"gate": item["gate"], "exit": item["exit"],
                   "findings": len(item["findings"]), "stdout_sha256": item["sha256"]}
                  for item in result["typed"]],
        "input_class": result.get("input_class"),
        "ok": all(item["ok"] for item in result["checks"]),
        "packet": rel(config.get("packet") or PACKET_DEFAULT),
        "pins": result["pins"],
        "routing": result["routing"],
        "sound_channel": result.get("sound_channel", {}),
        "translated_on_sound_channel": (result.get("sound_channel") or {}).get(
            "translated_on_sound_channel"),
        "typed_packet": rel(config.get("typed")
                            or ROOT / "examples/culture-d2/packet.d2.typed.yml"),
    }
    if resolved is not None:
        document["resolved"] = resolved
    return document


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

        # hazard control 3b: the null-ish owed_slot normalization (round-25 fix)
        module = runpy.run_path(str(tool))
        owed = module["owed_slot_of"]
        truth = [({}, None), ({"owed_slot": None}, None), ({"owed_slot": "null"}, None),
                 ({"owed_slot": "  ~ "}, None), ({"owed_slot": ""}, None),
                 ({"owed_slot": 5}, None), ({"owed_slot": "LEX-GAR-01"}, "LEX-GAR-01")]
        check("owed_slot normalization: the null-ish truth table holds",
              all(owed(row) == want for row, want in truth),
              "%s" % [(row, owed(row), want) for row, want in truth if owed(row) != want])

        # hazard control 3c: a moved row that owes no slot must not contribute a
        # phantom owed slot to the routing comparison. Pre-fix the literal
        # `'null'` entered `routed_slots` and the check detail carried it.
        unowed = original.replace(b'    owed_slot: "LEX-GAR-01"\n', b"    owed_slot: null\n", 1)
        assert unowed != original, "the fixture must carry the owed slot"
        unowed_path = Path(tmpdir) / "unowed-typed.yml"
        unowed_path.write_bytes(unowed)
        unowed_run = run("--json", str(unowed_path))
        unowed_payload = (json.loads(unowed_run.stdout)
                          if unowed_run.stdout.strip().startswith("{") else {})
        routing_detail = next((item["detail"] for item in unowed_payload.get("checks") or []
                               if item["id"] == "L3-routing-consistency"), "")
        check("phantom owed slot: a null-ish owed_slot never reaches the comparison",
              unowed_run.returncode == 1 and "'null'" not in routing_detail,
              "exit %d: %s" % (unowed_run.returncode, routing_detail[:200]))

        # hazard control 3d: the declared-assembler source leg is taken only when
        # the declared assembler builds a gradeable packet; the D2 mirror declares
        # none, so the reconstruction path stays in force
        check("declared-assembler source leg: absent without a declared assembler",
              not any(item["id"] == "L2-legacy-source"
                      for item in (payload.get("checks") or [])),
              "%s" % [item["id"] for item in (payload.get("checks") or [])])

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

        # input-class controls (round-25 O): a typed packet grades against its
        # declared source; an unresolvable or stale declaration refuses, exit 2
        typed_positive = run(str(built))
        typed_json = run("--json", str(built))
        typed_payload = (json.loads(typed_json.stdout)
                         if typed_json.stdout.strip().startswith("{") else {})
        check("typed input: graded against its declared source (exit 0)",
              typed_positive.returncode == 0
              and "L2-channel" in typed_positive.stdout
              and typed_positive.stdout != first.stdout,
              "exit %d" % typed_positive.returncode)
        check("typed input: --json reports the input class",
              typed_payload.get("input_class") == "typed-declared-source",
              "%s" % typed_payload.get("input_class"))
        orphan_text = original.decode("utf-8").replace(
            '  packet: "examples/culture-d2/packet.d2.yml"',
            '  packet: "examples/culture-d2/packet.absent.yml"', 1)
        assert orphan_text != original.decode("utf-8"), "the typed packet must name its source"
        orphan = Path(tmpdir) / "orphan-typed.yml"
        orphan.write_text(orphan_text, encoding="utf-8")
        orphan_run = run(str(orphan))
        check("typed input, missing source: exit 2 and the class is named",
              orphan_run.returncode == 2 and "not a gate input" in orphan_run.stdout,
              "exit %d: %s" % (orphan_run.returncode, orphan_run.stdout[-200:]))
        stale_source = mirror / "examples/culture-d2/packet.stale.yml"
        stale_source.write_bytes(
            (mirror / "examples/culture-d2/packet.d2.yml").read_bytes() + b"\n# drift\n")
        stale_text = original.decode("utf-8").replace(
            '  packet: "examples/culture-d2/packet.d2.yml"',
            '  packet: "examples/culture-d2/packet.stale.yml"', 1)
        stale_typed = Path(tmpdir) / "stale-source-typed.yml"
        stale_typed.write_text(stale_text, encoding="utf-8")
        stale_source_run = run(str(stale_typed))
        check("typed input, stale source: exit 2 and the class is named",
              stale_source_run.returncode == 2
              and "stale against its own source" in stale_source_run.stdout,
              "exit %d: %s" % (stale_source_run.returncode, stale_source_run.stdout[-200:]))

    total = len(passed) + len(failed)
    if failed:
        print("selftest: %d/%d checks passed — failures: %s"
              % (len(passed), total, "; ".join(failed)), file=sys.stderr)
        return 1
    print("selftest: %d/%d checks passed — constant==baseline, the mirrored four "
          "legs, determinism/--json, and the smuggled-label, dropped-row, "
          "laundered-hold, adapter-drift, malformed, missing and input-class "
          "controls; no file "
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
# generalized selftest (round-18 O claim)
# --------------------------------------------------------------------------

FIXTURE_ASSEMBLER = '''#!/usr/bin/env python3
"""fixture assembler for the round-18 generalized-gate controls; not a lane tool."""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKET = ROOT / "examples/culture-d9/packet.d9.yml"
COMPONENTS = ROOT / "examples/culture-d9/components"


def assemble():
    rows = []
    for path in sorted(COMPONENTS.glob("*.yml")):
        rows.append('  "%s": "%s"'
                    % (path.name, hashlib.sha256(path.read_bytes()).hexdigest()))
    lines = ['name: "d9 fixture"', "assembly:",
             '  generator: "tools/assemble-culture-d9.py"',
             '  assembler_sha256: "%s"'
             % hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             "components:"]
    return ("\\n".join(lines + rows) + "\\n").encode("utf-8")


def main():
    payload = assemble()
    if "--check" in sys.argv:
        if not PACKET.exists() or PACKET.read_bytes() != payload:
            print("packet.d9.yml differs from deterministic assembly", file=sys.stderr)
            return 1
        print("packet.d9.yml: byte-identical deterministic assembly")
        return 0
    PACKET.parent.mkdir(parents=True, exist_ok=True)
    PACKET.write_bytes(payload)
    print("Wrote %s (%d bytes)" % (PACKET.relative_to(ROOT), len(payload)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def _fixture_typed_packet(pins):
    """A minimal typed packet whose one routing row stays on channel.

    The non-typed blocks are the smallest the five culture gates accept at
    exit 0/1 (measured, `.scratch/r18-o03/gfixture/`): a phonology mapping, one
    costume, one lexicon entry and an era tag list.
    """
    return "\n".join([
        'name: "d9 fixture typed"',
        "assembly:",
        '  packet_sha256: "%s"' % pins["packet_sha256"],
        '  projection_sha256: "%s"' % pins["projection_sha256"],
        '  adapter_sha256: "%s"' % pins["adapter_sha256"],
        '  assembler_sha256: "%s"' % pins["assembler_sha256"],
        "phonology:",
        '  consonants: ["p", "t", "k", "m", "n", "s", "l", "r"]',
        '  vowels: ["a", "i", "u"]',
        '  coda: ["n", "l", "r", "s"]',
        "  onset_clusters: false",
        "costumes:",
        "  -",
        '    id: "RF-01"',
        '    garment: "plain coat"',
        '    form_slot: "LEX-RF-01, the plain grade"',
        '    material: "felt"',
        '    wearer_rank: "any adult"',
        '    rite: "none"',
        '    era: "E0"',
        '    route: "local chain: shear -> felt -> seam"',
        '    provenance: "local-production"',
        '    rank_mark: "none"',
        '    evidence: "design-choice"',
        "    follows:",
        '      - "alias_dress"',
        "lexicon:",
        "  -",
        '    id: "L-01"',
        '    term: "ir"',
        '    gloss: "breath"',
        '    field: "body"',
        '    layer: "native"',
        '    route: "root"',
        '    stage: "E0"',
        '    class: "noun"',
        '    axis: "wind"',
        '    evidence: "design-choice"',
        'eras: ["E0"]',
        'schema: "kotodama-typed-packet-v1"',
        "typed_channel:",
        "  -",
        '    record: "RF-01"',
        '    kind: "translated-label"',
        '    label_id: "LEX-RF-01"',
        '    owner: "09-costumes"',
        '    source_field: "garment"',
        "    off_channel_field: null",
        '    channel: "on-sound-and-identity"',
        '    hold: "D9L-REGISTER-UNRESOLVED"',
        '    owed_slot: "LEX-RF-01"',
        "typed_assembly:",
        '  generator: "tools/assemble-d9-typed.py"',
        "pipeline_findings:",
        "  -",
        '    id: "D9L-REGISTER-UNRESOLVED"',
        '    code: "REGISTER"',
        '    severity: "hold"',
        '    where: "LEX-RF-01"',
        '    detail: "fixture hold"',
        "pipeline_counts:",
        "  hold: 1",
        "  note: 0",
        "  fail: 0",
    ]) + "\n"


def selftest_generalized():
    """Declared-identity controls, run over fixture trees in one temp directory."""
    passed, failed = [], []

    def check(label, condition, detail=""):
        (passed if condition else failed).append(label)
        print("%s %s%s" % ("ok  " if condition else "FAIL", label,
                           "" if condition else " — %s" % detail))

    # default resolution: nothing declared lands exactly on the D2 constants
    for probe in (PACKET_DEFAULT, ROOT / "examples/culture-d2/packet.d2.typed.yml"):
        resolved = resolve_config(probe, {"assembly": {"packet_sha256": "0" * 64}})
        drift = {key: rel(resolved[key]) for key in D2_DEFAULTS
                 if resolved[key] != D2_DEFAULTS[key]}
        check("default resolution lands on the D2 constants (%s)" % rel(probe),
              not resolved["generalized"] and not drift, "%s" % drift)
    declared = resolve_config(ROOT / "examples/culture-d4/packet.d4.yml",
                              {"typed_pipeline": {"assembler": "tools/assemble-culture-d4.py"}})
    check("a declaration resolves the family paths",
          declared["generalized"] and declared["family"] == "d4"
          and declared["assembler"] == ROOT / "tools/assemble-culture-d4.py"
          and declared["expected"] == ROOT / "examples/culture-d4/expected-holds.json",
          "%s, %s" % (rel(declared["assembler"]), rel(declared["expected"])))

    with tempfile.TemporaryDirectory(prefix="typed-pipeline-gate-generalized-") as tmpdir:
        mirror = Path(tmpdir) / "repo"
        (mirror / "tools/gates").mkdir(parents=True)
        (mirror / "examples/culture-d9/components").mkdir(parents=True)
        for name in ("assemble-d2.py", "assemble-d2-typed.py", "d2-typed-labels.py"):
            shutil.copyfile(ROOT / "tools" / name, mirror / "tools" / name)
        for name in GATE_NAMES:
            shutil.copyfile(GATES_DIR / name, mirror / "tools/gates" / name)
        shutil.copyfile(Path(__file__), mirror / "tools/gates/typed-pipeline-gate.py")
        # the argot-derivation sibling (round-25 D): mirrored with its fixtures
        # so the leg is exercised inside the mirror, and its own selftest runs there.
        shutil.copyfile(ARGOT_GATE, mirror / "tools/gates/argot-derivation-gate.py")
        (mirror / "tools/gates/fixtures").mkdir(parents=True, exist_ok=True)
        for fixture in ("argot-derivation-gate.yml", "argot-derivation-gate.expected"):
            shutil.copyfile(GATES_DIR / "fixtures" / fixture,
                            mirror / "tools/gates/fixtures" / fixture)
        fixture_assembler = mirror / "tools/assemble-culture-d9.py"
        fixture_assembler.write_text(FIXTURE_ASSEMBLER, encoding="utf-8")
        (mirror / "examples/culture-d9/components/01-brief.yml").write_text(
            'name: "d9 fixture component"\n', encoding="utf-8")
        projection = mirror / "examples/culture-d9/typed-labels.d9.yml"
        projection.write_text('name: "d9 fixture projection"\n', encoding="utf-8")
        adapter = mirror / "tools/assemble-d9-typed.py"
        adapter.write_text('"""fixture adapter stub (round-18 control)."""\n', encoding="utf-8")
        build = subprocess.run([sys.executable, str(fixture_assembler)],
                               capture_output=True, text=True, cwd=str(mirror),
                               env=child_env(), check=False)
        check("fixture assembler built its packet", build.returncode == 0,
              build.stdout[-200:] + build.stderr[-200:])
        packet = mirror / "examples/culture-d9/packet.d9.yml"
        expected = mirror / "examples/culture-d9/expected-holds.json"
        typed = mirror / "examples/culture-d9/packet.d9.typed.yml"
        pins = dict((name, sha256_file(path)) for name, path in (
            ("packet_sha256", packet), ("projection_sha256", projection),
            ("adapter_sha256", adapter), ("assembler_sha256", fixture_assembler)))
        typed.write_text(_fixture_typed_packet(pins), encoding="utf-8")
        expected.write_text(json.dumps(
            {"schema": SCHEMA, "counts": {"hold": 1, "note": 0, "fail": 0},
             "holds": [{"id": "D9L-REGISTER-UNRESOLVED", "severity": "hold",
                        "where": "LEX-RF-01", "detail": "fixture hold"}],
             "notes": []}, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        tool = mirror / "tools/gates/typed-pipeline-gate.py"

        def run(*args):
            return subprocess.run([sys.executable, str(tool), *args],
                                  capture_output=True, text=True, cwd=str(mirror),
                                  env=child_env(), check=False)

        def as_check(proc):
            payload = json.loads(proc.stdout) if proc.stdout.strip().startswith("{") else {}
            checks = {item["id"]: item for item in payload.get("checks") or []}
            return checks, payload

        positive = run("--json", str(typed))
        checks, payload = as_check(positive)
        check("declared identity: the typed fixture grades green (exit 0)",
              positive.returncode == 0 and payload.get("ok") is True,
              "exit %d: %s" % (positive.returncode, positive.stdout[-300:]))
        check("declared identity: L1-assembler passed and the pin re-verified",
              (checks.get("L1-assembler") or {}).get("ok") is True
              and (checks.get("L4-pins") or {}).get("ok") is True,
              "%s" % checks.get("L1-assembler"))
        check("declared identity: the resolved block is reported",
              (payload.get("resolved") or {}).get("assembler")
              == "tools/assemble-culture-d9.py",
              "%s" % payload.get("resolved"))
        first, second = positive.stdout, run("--json", str(typed)).stdout
        check("declared identity: two gate runs byte-identical", first == second)

        # argot-derivation leg (round-25 D claim): the sibling is mirrored, so
        # the leg runs inside the mirror too. The sibling's own selftest names
        # its controls, and the mirror's leg must be present and answer.
        argot_tool = mirror / "tools/gates/argot-derivation-gate.py"
        argot_selftest = subprocess.run([sys.executable, str(argot_tool), "--selftest"],
                                        capture_output=True, text=True, cwd=str(mirror),
                                        env=child_env(), check=False)
        check("argot derivation leg: the mirrored sibling selftest is green",
              argot_selftest.returncode == 0 and "checks passed" in argot_selftest.stdout,
              "exit %d: %s" % (argot_selftest.returncode, argot_selftest.stdout[-200:]))
        argot_probe = subprocess.run(
            [sys.executable, str(argot_tool), str(mirror / "examples/culture-d9/packet.d9.yml")],
            capture_output=True, text=True, cwd=str(mirror), env=child_env(), check=False)
        check("argot derivation leg: the mirrored leg runs on the family packet",
              argot_probe.returncode in (0, 1) and "coverage:" in argot_probe.stdout,
              "exit %d: %s" % (argot_probe.returncode, argot_probe.stdout[-200:]))

        packet_bytes = packet.read_bytes()
        packet.write_bytes(packet_bytes + b"# tamper\n")
        tampered_check = subprocess.run([sys.executable, str(fixture_assembler), "--check"],
                                        capture_output=True, text=True, cwd=str(mirror),
                                        env=child_env(), check=False)
        tampered = run("--json", str(typed))
        tampered_checks, _ = as_check(tampered)
        check("tamper: the gate's identity leg agrees with the assembler's --check",
              tampered_check.returncode == 1 and tampered.returncode == 2
              and (tampered_checks.get("L1-assembler") or {}).get("ok") is False,
              "check %d, gate %d: %s" % (tampered_check.returncode, tampered.returncode,
                                         (tampered_checks.get("L1-assembler") or {}).get("detail")))
        packet.write_bytes(packet_bytes)

        assembler_bytes = fixture_assembler.read_bytes()
        fixture_assembler.write_bytes(assembler_bytes + b"\n# drift\n")
        drifted = run("--json", str(typed))
        drifted_checks, _ = as_check(drifted)
        check("assembler drift: the identity leg breaks (exit 2)",
              drifted.returncode == 2
              and (drifted_checks.get("L1-assembler") or {}).get("ok") is False,
              "exit %d" % drifted.returncode)
        fixture_assembler.write_bytes(assembler_bytes)

        module = runpy.run_path(str(tool))
        stale_pin, stale_detail = module["assembler_identity"](packet, fixture_assembler,
                                                               "0" * 64)
        good_bytes, good_detail = module["assembler_identity"](packet, fixture_assembler)
        check("self-pin control: a stale assembler pin is refused",
              stale_pin is False and "self-pin broken" in stale_detail, stale_detail)
        check("identity leg agrees with --check on the restored tree",
              good_bytes is True and good_detail == "", "%s / %s" % (good_bytes, good_detail))

        expected_bytes = expected.read_bytes()
        expected.unlink()
        no_expected = run("--json", str(typed))
        no_expected_checks, _ = as_check(no_expected)
        check("missing expected file: exit 2 and the expected leg names it",
              no_expected.returncode == 2
              and "missing" in (no_expected_checks.get("L1-expected-holds") or {}).get("detail", ""),
              "exit %d: %s" % (no_expected.returncode,
                               (no_expected_checks.get("L1-expected-holds") or {}).get("detail")))
        expected.write_bytes(expected_bytes)

        text = typed.read_text(encoding="utf-8")
        stale = text.replace('adapter_sha256: "%s"' % pins["adapter_sha256"],
                             'adapter_sha256: "%s"' % ("0" * 64), 1)
        assert stale != text, "the fixture must carry the adapter pin"
        typed.write_text(stale, encoding="utf-8")
        stale_run = run("--json", str(typed))
        stale_checks, _ = as_check(stale_run)
        check("stale declared pin: exit 2 and L4-pins fires",
              stale_run.returncode == 2 and (stale_checks.get("L4-pins") or {}).get("ok") is False,
              "exit %d: %s" % (stale_run.returncode,
                               (stale_checks.get("L4-pins") or {}).get("detail")))
        typed.write_text(text, encoding="utf-8")

    total = len(passed) + len(failed)
    if failed:
        print("selftest-generalized: %d/%d checks passed — failures: %s"
              % (len(passed), total, "; ".join(failed)), file=sys.stderr)
        return 1
    print("selftest-generalized: %d/%d checks passed — default resolution on the "
          "D2 constants, a declared family graded green, determinism, and the "
          "tamper/drift/self-pin/missing-expected/stale-pin controls, each "
          "identity verdict agreed with the assembler's own --check; no file "
          "outside the temporary mirror touched" % (len(passed), total))
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("packet", nargs="?", default=str(PACKET_DEFAULT),
                        help="packet to grade (default: %s)" % rel(PACKET_DEFAULT))
    parser.add_argument("--json", action="store_true", help="one JSON document")
    parser.add_argument("--assembler", help="declared assembler identity")
    parser.add_argument("--projection", help="declared projection pin path")
    parser.add_argument("--adapter", help="declared typed adapter path")
    parser.add_argument("--expected", help="declared expected-holds file")
    parser.add_argument("--legacy-packet", dest="legacy_packet",
                        help="legacy packet the declared pipeline assembles")
    parser.add_argument("--selftest", "--self-test", action="store_true", dest="selftest",
                        help="mirrored four legs plus hazard controls")
    parser.add_argument("--selftest-generalized", action="store_true",
                        dest="selftest_generalized",
                        help="declared-identity controls over fixture trees")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.selftest_generalized:
        return selftest_generalized()
    candidate = Path(args.packet)
    typed_arg = None
    if candidate.is_file():
        try:
            head = load_packet_strict(candidate.read_text(encoding="utf-8"),
                                      family_projector(candidate))
            document = head.get("packet") or {}
        except Exception:
            document = {}
        if document.get("typed_channel") is not None:
            typed_arg = candidate
    flags = {"assembler": args.assembler, "projection": args.projection,
             "adapter": args.adapter, "expected": args.expected,
             "packet": args.legacy_packet}
    result = grading(candidate, typed_arg=typed_arg, flags=flags)
    if args.json:
        print(json.dumps(json_document(result, result.get("config")),
                         sort_keys=True, ensure_ascii=False))
        return result["exit"]
    return report(result, config=result.get("config"))


if __name__ == "__main__":
    sys.exit(main())
