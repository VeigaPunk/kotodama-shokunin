#!/usr/bin/env python3
"""assemble-d2-typed — the D2 typed-packet adapter (R11-D03/D04, landed by D05).

The one step where typed labels enter assembly (`reports/round-11/depth/design.md`
§2): it reads the assembled D2 packet and the round-8 typed projection, and emits
one deterministic YAML-subset document — the **typed packet** the gates read.

What it changes, and only this:

  * a record the projector types `translated-label` (and for which no native
    form is supplied) has its checked field **moved**: `garment` →
    `garment_gloss`. The field the naming gate reads as a surface form is gone,
    so the gloss is off the sound-and-identity channel; it is not exempted by a
    flag (design §2.3 T1 row 6: "adding typing fields cannot exempt a string"),
    and it is not deleted — it rides in the typed packet under its new name;
  * every moved record gets exactly one `typed_channel` routing row naming the
    record, its kind, its label id, the source field, the off-channel field and
    the hold it carries (`D2L-FORM-UNRESOLVED`) — the owed native form is
    carried **by name**;
  * the projector's finding set is carried verbatim under `pipeline_findings`,
    with the counts, so the gate reads the holds from the typed packet (§3.1 L3);
  * `assembly` pins the three inputs: `packet_sha256`, `projection_sha256` and
    `adapter_sha256` (this file's own digest, so a frozen row's gate hash pins
    the adapter transitively).

Interface (design §2.2):

    python3 tools/assemble-d2-typed.py [--packet P] [--projection J]
                                       [--emit PATH] [--check [PATH]] [--selftest]

Fail-closed rules (design §2.2 table): assembler identity (the packet bytes must
equal `assemble-d2.py`'s deterministic assembly — the assembler's own build
path is called, never re-implemented) and projection freshness (the projection's
`assembly.packet_sha256` must equal the packet's digest, and the projector's
pipeline must reproduce the committed projection byte-for-byte) both exit **2**;
a coverage violation (an off-channel record without a routing row, a routing row
for an unknown record, a costume record the projector did not type) exits **2**;
determinism/`--check` drift exits **1**; success exits **0**.

Read-only over its peers: `tools/assemble-d2.py` and `tools/d2-typed-labels.py`
are loaded with `runpy.run_path` and never written. `assemble-d2.py` is byte-pinned
by the D3 packet's `serializer_sha256`, which is why the wiring lives out here.
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

ROOT = Path(__file__).resolve().parent.parent
PACKET_DEFAULT = ROOT / "examples/culture-d2/packet.d2.yml"
PROJECTION_DEFAULT = ROOT / "examples/culture-d2/typed-labels.d2.yml"
TYPED_PACKET_DEFAULT = ROOT / "examples/culture-d2/packet.d2.typed.yml"
SERIALIZER = ROOT / "tools/assemble-d2.py"
PROJECTOR = ROOT / "tools/d2-typed-labels.py"
SCHEMA = "kotodama-typed-packet-v1"
ROUTED_KINDS = ("translated-label",)
HOLD = "D2L-FORM-UNRESOLVED"
CHANNEL = "off-sound-and-identity"
OWED_SLOT_RE = re.compile(r"\s*([A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*-\d+)")


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


def owed_slot(form_slot):
    if not isinstance(form_slot, str):
        return None
    match = OWED_SLOT_RE.match(form_slot)
    return match.group(1) if match else None


# --------------------------------------------------------------------------
# fail-closed inputs
# --------------------------------------------------------------------------


def assembler_identity(packet_path):
    """The packet bytes must equal the assembler's own deterministic build."""
    serializer = load_peer(SERIALIZER)
    try:
        expected = serializer["assemble"]()
    except (ValueError, OSError) as exc:
        return False, "assembler refused the components: %s" % exc
    actual = Path(packet_path).read_bytes()
    if actual != expected:
        return False, ("packet bytes are not assemble-d2.py's deterministic "
                       "assembly (%s vs %s)"
                       % (sha256_bytes(actual)[:12], sha256_bytes(expected)[:12]))
    return True, "packet equals the assembler's deterministic build"


def projection_fresh(projection_path, packet_path):
    """The projection must pin this packet and regenerate byte-for-byte."""
    projector = load_peer(PROJECTOR)
    if not Path(projection_path).is_file():
        return False, "projection missing: %s" % rel(projection_path)
    committed = Path(projection_path).read_bytes()
    try:
        document = json.loads(committed.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        return False, "projection is not JSON: %s" % exc
    packet_sha = sha256_file(packet_path)
    pinned = (document.get("assembly") or {}).get("packet_sha256")
    if pinned != packet_sha:
        return False, ("stale projection pin: projection records %s, packet "
                       "hashes %s" % (pinned, packet_sha))
    result = projector["run_pipeline"](str(packet_path))
    if result["projection"] is None:
        return False, "projector could not evaluate the packet"
    if projector["serialize"](result["projection"]) != committed:
        return False, ("projector does not reproduce the committed projection "
                       "byte-for-byte")
    return True, "projection pins the packet and regenerates byte-for-byte"


def typed_labels(projection_path):
    document = json.loads(Path(projection_path).read_text(encoding="utf-8"))
    return (document.get("typed_labels") or {}).get("labels") or [], document


# --------------------------------------------------------------------------
# the build
# --------------------------------------------------------------------------


def build_typed_packet(packet, labels, packet_rel, packet_sha, projection_rel,
                       projection_sha, adapter_sha):
    """Derive the typed gate packet; returns (document, routing, problems)."""
    doc = copy.deepcopy(packet)
    by_record = {}
    for label in labels:
        record = (label.get("source") or {}).get("record")
        if record:
            by_record.setdefault(str(record), []).append(label)

    routing = []
    problems = []
    typed_ids = set()
    costumes = doc.get("costumes")
    if isinstance(costumes, list):
        for entry in costumes:
            if not isinstance(entry, dict):
                continue
            rid = str(entry.get("id") or "")
            kinds = sorted({label.get("kind") for label in by_record.get(rid, [])
                            if label.get("kind")})
            if not kinds:
                if entry.get("garment"):
                    problems.append(
                        "costume record %s carries a garment label the projector "
                        "did not type (coverage gap)" % rid)
                continue
            typed_ids.add(rid)
            if not any(kind in ROUTED_KINDS for kind in kinds):
                continue
            field = "garment"
            label_id = None
            owner = None
            for label in by_record.get(rid, []):
                if label.get("kind") in ROUTED_KINDS:
                    label_id = label.get("label_id") or label.get("id")
                    owner = label.get("owner")
                    break
            if field not in entry:
                problems.append("routed record %s has no %s field to move"
                                % (rid, field))
                continue
            entry["%s_gloss" % field] = entry.pop(field)
            routing.append({
                "record": rid,
                "kind": kinds[0] if len(kinds) == 1 else "+".join(kinds),
                "label_id": label_id,
                "owner": owner,
                "source_field": field,
                "off_channel_field": "%s_gloss" % field,
                "channel": CHANNEL,
                "hold": HOLD,
                "owed_slot": owed_slot(entry.get("form_slot")),
            })
    for record in sorted(by_record):
        if record not in typed_ids and any(
                label.get("kind") in ROUTED_KINDS for label in by_record[record]):
            problems.append("routing row names record %s which is not in the "
                            "packet's costume ledger" % record)

    doc["schema"] = SCHEMA
    doc["typed_channel"] = sorted(routing, key=lambda row: row["record"])
    doc["typed_assembly"] = {
        "generator": "tools/assemble-d2-typed.py",
        "packet": packet_rel,
        "projection": projection_rel,
        "rules": [
            "translated-label (no native form supplied): checked field moved "
            "garment -> garment_gloss; off sound-and-identity channel; owed form "
            "held as %s (design §2.3 T1 rows 1/3)" % HOLD,
            "native-form and borrowed-strata records ride through unchanged; "
            "their checked field stays (T1 rows 2/4)",
            "an untyped record is a coverage problem, never a silent exemption "
            "(T1 row 6)",
        ],
    }
    doc["assembly"] = {
        "packet_sha256": packet_sha,
        "projection_sha256": projection_sha,
        "adapter_sha256": adapter_sha,
    }
    return doc, routing, problems


def carry_findings(doc, projection_document):
    """Carry the projector's finding set (and counts) into the typed packet."""
    findings = projection_document.get("findings") or []
    doc["pipeline_findings"] = findings
    counts = {"hold": 0, "note": 0, "fail": 0}
    for item in findings:
        severity = item.get("severity")
        if severity in counts:
            counts[severity] += 1
        elif severity:
            counts[severity] = counts.get(severity, 0) + 1
    doc["pipeline_counts"] = counts
    return doc


def render(doc):
    serializer = load_peer(SERIALIZER)
    return ("\n".join(serializer["yaml_lines"](doc)) + "\n").encode("utf-8")


def build(packet_path=PACKET_DEFAULT, projection_path=PROJECTION_DEFAULT):
    """Run the three fail-closed inputs and return the build result."""
    result = {"exit": 2, "problems": [], "doc": None, "payload": None,
              "routing": [], "inputs": {}}
    packet_path = Path(packet_path)
    projection_path = Path(projection_path)
    if not packet_path.is_file():
        result["problems"].append("packet missing: %s" % rel(packet_path))
        return result
    ok, detail = assembler_identity(packet_path)
    result["inputs"]["assembler_identity"] = {"ok": ok, "detail": detail}
    if not ok:
        result["problems"].append(detail)
        return result
    ok, detail = projection_fresh(projection_path, packet_path)
    result["inputs"]["projection_freshness"] = {"ok": ok, "detail": detail}
    if not ok:
        result["problems"].append(detail)
        return result
    labels, projection_document = typed_labels(projection_path)
    doc, routing, problems = build_typed_packet(
        load_peer(PROJECTOR)["load_packet_file"](str(packet_path))["packet"],
        labels, rel(packet_path), sha256_file(packet_path),
        rel(projection_path), sha256_file(projection_path),
        sha256_file(Path(__file__)))
    result["inputs"]["coverage"] = {
        "ok": not problems,
        "detail": ("%d routing row(s), no coverage problem" % len(routing))
                  if not problems else "; ".join(problems)}
    if problems:
        result["problems"].extend(problems)
        return result
    doc = carry_findings(doc, projection_document)
    payload = render(doc)
    if render(doc) != payload:                       # two consecutive builds
        result["problems"].append("two consecutive builds are not byte-identical")
        return result
    result.update({"exit": 0, "doc": doc, "payload": payload, "routing": routing})
    return result


def report(result, stream=sys.stdout):
    for name, record in result.get("inputs", {}).items():
        print("%s %s: %s" % ("ok  " if record["ok"] else "FAIL", name,
                             record["detail"]), file=stream)
    if result["exit"] == 2:
        for problem in result["problems"]:
            print("assembly error: %s" % problem, file=stream)
        return 2
    routing = result["routing"]
    print("typed packet: %d routing row(s); checked field moved for %s"
          % (len(routing), ", ".join(row["record"] for row in routing) or "-"))
    counts = result["doc"]["pipeline_counts"]
    print("carried findings: hold %d, note %d, fail %d"
          % (counts.get("hold", 0), counts.get("note", 0), counts.get("fail", 0)))
    return 0


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------


def selftest():
    """Fixture controls in a temporary mirror; no file outside it is touched."""
    passed, failed = [], []

    def check(label, condition, detail=""):
        (passed if condition else failed).append(label)
        print("%s %s%s" % ("ok  " if condition else "FAIL", label,
                           "" if condition else " — %s" % detail))

    with tempfile.TemporaryDirectory(prefix="assemble-d2-typed-") as tmpdir:
        mirror = Path(tmpdir) / "repo"
        (mirror / "tools/gates").mkdir(parents=True)
        for name in ("assemble-d2-typed.py", "assemble-d2.py", "d2-typed-labels.py"):
            shutil.copyfile(ROOT / "tools" / name, mirror / "tools" / name)
        shutil.copyfile(ROOT / "tools/gates/costume-era-consistency-gate.py",
                        mirror / "tools/gates/costume-era-consistency-gate.py")
        shutil.copytree(ROOT / "examples/culture-d2", mirror / "examples/culture-d2",
                        ignore=shutil.ignore_patterns("__pycache__"))
        tool = mirror / "tools/assemble-d2-typed.py"

        def run(*args, tree=mirror):
            return subprocess.run([sys.executable, str(tool), *args],
                                  capture_output=True, text=True, cwd=str(tree),
                                  env=child_env(), check=False)

        emitted = mirror / "examples/culture-d2/packet.d2.typed.yml"
        first = run("--emit", str(emitted))
        check("positive: --emit exit 0", first.returncode == 0,
              "exit %d: %s" % (first.returncode, first.stdout[-300:] or first.stderr[-300:]))
        payload = emitted.read_bytes() if emitted.exists() else b""
        check("positive: typed packet written", bool(payload))
        second = run("--emit", str(emitted))
        check("determinism: two builds byte-identical",
              second.returncode == 0 and emitted.read_bytes() == payload)
        clean = run("--check", str(emitted))
        check("--check: exit 0 on the build", clean.returncode == 0,
              clean.stderr.strip()[:200])
        committed = mirror / "examples/culture-d2/packet.d2.typed.yml"
        original = committed.read_bytes()
        committed.write_bytes(original.replace(b"typed_channel:", b"typed_channel :", 1))
        drift = run("--check", str(committed))
        check("tamper: --check exit 1 on a changed byte", drift.returncode == 1,
              "exit %d" % drift.returncode)
        committed.write_bytes(original)
        check("tamper: restored build passes", run("--check", str(committed)).returncode == 0)

        # stale projection pin: exit 2, named
        projection = mirror / "examples/culture-d2/typed-labels.d2.yml"
        projection_backup = projection.read_bytes()
        projection.write_bytes(projection_backup.replace(
            b'"packet_sha256": "', b'"packet_sha256": "0', 1))
        stale = run()
        check("stale projection: exit 2 and the pin is named",
              stale.returncode == 2 and "stale projection pin" in stale.stdout,
              "exit %d: %s" % (stale.returncode, stale.stdout[-200:]))
        projection.write_bytes(projection_backup)

        # coverage: unit-level controls on the build's routing table (design §2.2)
        _, _, untyped = build_typed_packet(
            {"costumes": [{"id": "GAR-99", "garment": "gloss"}]}, [],
            "p", "0" * 64, "j", "0" * 64, "0" * 64)
        check("coverage: an untyped garment record is a problem",
              any("did not type" in problem for problem in untyped), untyped)
        _, _, orphan = build_typed_packet(
            {"costumes": []},
            [{"kind": "translated-label", "label_id": "LEX-X-01",
              "source": {"record": "GAR-99"}}],
            "p", "0" * 64, "j", "0" * 64, "0" * 64)
        check("coverage: a routing row for a missing record is a problem",
              any("not in the packet" in problem for problem in orphan), orphan)
        routed, routing, problems = build_typed_packet(
            {"costumes": [{"id": "GAR-99", "garment": "gloss",
                           "form_slot": "LEX-GAR-99, (to-verify)"}]},
            [{"kind": "translated-label", "label_id": "LEX-GAR-99",
              "owner": "11-costumes", "source": {"record": "GAR-99"}}],
            "p", "0" * 64, "j", "0" * 64, "0" * 64)
        check("routing: the checked field is moved, not flagged",
              not problems and routed["costumes"][0].get("garment") is None
              and routed["costumes"][0].get("garment_gloss") == "gloss"
              and routing[0]["off_channel_field"] == "garment_gloss"
              and routing[0]["owed_slot"] == "LEX-GAR-99", routing)

        # malformed packet: exit 2, no traceback
        broken = mirror / "examples/culture-d2/packet.d2.yml"
        broken_backup = broken.read_bytes()
        broken.write_text("name: X\nphonology:\n  consonants: [p, t\n", encoding="utf-8")
        bad = run()
        check("malformed packet: exit 2, no traceback",
              bad.returncode == 2 and "Traceback" not in bad.stdout + bad.stderr,
              "exit %d: %s" % (bad.returncode, (bad.stderr or bad.stdout)[:200]))
        broken.write_bytes(broken_backup)

    total = len(passed) + len(failed)
    if failed:
        print("selftest: %d/%d checks passed — failures: %s"
              % (len(passed), total, "; ".join(failed)), file=sys.stderr)
        return 1
    print("selftest: %d/%d checks passed — build/determinism/--check/tamper plus "
          "stale-projection, coverage-gap and malformed-packet controls; no file "
          "outside the temporary mirror touched" % (len(passed), total))
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--packet", default=str(PACKET_DEFAULT),
                        help="the assembled D2 packet (default: %s)" % rel(PACKET_DEFAULT))
    parser.add_argument("--projection", default=str(PROJECTION_DEFAULT),
                        help="the typed projection (default: %s)" % rel(PROJECTION_DEFAULT))
    parser.add_argument("--emit", metavar="PATH", help="write the typed packet to PATH")
    parser.add_argument("--check", metavar="PATH", nargs="?",
                        const=str(TYPED_PACKET_DEFAULT),
                        help="byte-compare the build (default target: %s)"
                             % rel(TYPED_PACKET_DEFAULT))
    parser.add_argument("--selftest", "--self-test", action="store_true", dest="selftest",
                        help="fixture controls in a temporary mirror")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    result = build(args.packet, args.projection)
    if result["exit"] == 2:
        return report(result)
    if args.emit:
        Path(args.emit).write_bytes(result["payload"])
        print("Wrote %s (%d bytes, %d routing row(s))"
              % (args.emit, len(result["payload"]), len(result["routing"])))
        return 0
    if args.check:
        target = Path(args.check)
        if not target.exists() or target.read_bytes() != result["payload"]:
            print("%s differs from the deterministic typed packet" % rel(target),
                  file=sys.stderr)
            return 1
        print("%s: byte-identical deterministic typed packet" % rel(target))
        return 0
    return report(result)


if __name__ == "__main__":
    sys.exit(main())
