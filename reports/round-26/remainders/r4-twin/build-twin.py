#!/usr/bin/env python3
"""Round-26 O seat — generate the declared-in-r4 machine twin from the packet.

Disposition of the round-25 remainder: the v3 revision
`reports/round-25/v3-supersession/declared-in-r4/` landed packet-only — it holds
`packet.md`, `expected.json` and `freeze.txt` and **no** `twin.json`, unlike the
r20 and r22 siblings. The round-25 X48 shard audit filed exactly this gap
(`reports/round-25/audit/x48-v3-supersession.md` §"the successor lands
packet-only"). The corrected prose is therefore on disk and verified, but the
ledger surface of that revision stays unauditable.

This seat lands the twin as a **new row** under `reports/round-26/remainders/`,
never by writing into the filed round-25 directory (rounds 8-25 are frozen).

The twin is not a new artifact kind: it is exactly the projection
`tools/exercise-handoff-e2e.py`'s `v3_build_twin` (line 2621) performs at
assembly time — the packet's three Markdown tables (`artifact_manifest`,
`claim_ledger`, `coupling_edges`), the `open_questions` passenger list, and the
four `record_ids` indexes the edges and the harness resolve against. This
generator performs that same projection on the filed packet bytes and mines the
indexes with the renderer's **own** `v3_mine_d2` / `v3_mine_d3` / `v3_mine_d4`
functions (imported read-only), so no projection rule is re-implemented here.

Reproduction control: run against the filed r20 (3.0.0) and r22 (3.1.1) packets,
this generator reproduces both filed twins **byte-identically** (sha256
`58cb2460…` and `d3de56a8…`). That is the load-bearing control that the
projection rule is the renderer's, not this seat's invention.

Usage:
    python3 reports/round-26/remainders/r4-twin/build-twin.py --emit
    python3 reports/round-26/remainders/r4-twin/build-twin.py --stdout
    python3 reports/round-26/remainders/r4-twin/build-twin.py --selftest
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

RENDERER = "tools/exercise-handoff-e2e.py"
R25_CHECKER = "reports/round-25/v3-supersession/v3-supersession-check.py"
R4_PACKET = "reports/round-25/v3-supersession/declared-in-r4/packet.md"
R4_PACKET_SHA256 = "5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03"

# The two filed predecessors, used as the reproduction control. Their twins are
# the renderer's own output, so equality is an end-to-end check of this
# projection. The r20 twin is the 3.0.0 shape (no `declared_in` edge column).
PREDECESSORS = (
    ("reports/round-20/handoff/packet.md", "reports/round-20/handoff/twin.json",
     "58cb246081e03e351dc35c4c13ae7961ee9e046e569f0cc7081d76813de88628", "3.0.0"),
    ("reports/round-22/handoff/declared-in-r2/packet.md",
     "reports/round-22/handoff/declared-in-r2/twin.json",
     "d3de56a8be1d28fdcead751aa0ac9364f7b43ff2b8bad71b696f0b57955b4d5c", "3.1.1"),
)

MANIFEST_HEADER = ("artifact_id", "path", "role", "sha256", "records")
LEDGER_HEADER = ("claim_id", "kind", "evidence_status", "uncertainty_status",
                 "uncertainty_basis", "links", "statement")
EDGE_HEADER = ("edge_id", "source", "relation", "target_ids", "claims",
               "applicability", "mechanism", "limits")
OQ_RE = re.compile(r"^- (OQ-V[23]-\d+):\s*(.+)$")
INLINE_ROW = "§"  # the packet's inline glossary payload row; never in the twin


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def table_rows(text: str, first_header):
    """The first table whose header starts with `first_header`; rows as cell lists.

    Mirrors `tools/exercise-handoff-e2e.py`'s own `table_rows`.
    """
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            continue
        header = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if tuple(header[: len(first_header)]) != tuple(first_header):
            continue
        if index + 1 >= len(lines) or not re.match(r"^\|[\s:|-]+\|$", lines[index + 1].strip()):
            continue
        rows, cursor = [], index + 2
        while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
            rows.append([part.strip() for part in lines[cursor].strip().strip("|").split("|")])
            cursor += 1
        return header, rows
    return None, []


def field(text: str, name: str):
    match = re.search(rf"^\|\s*{re.escape(name)}\s*\|\s*(.+?)\s*\|$", text, re.M)
    return match.group(1) if match else None


def profile_of(text: str):
    match = re.search(r"^- profile\s+(\S+)", text, re.M)
    return match.group(1) if match else None


def load_renderer():
    spec = importlib.util.spec_from_file_location("r26_r4_renderer", ROOT / RENDERER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_detector():
    """The filed round-25 checker module, for its stale-prose detector only."""
    spec = importlib.util.spec_from_file_location(
        "r26_r4_detector", ROOT / R25_CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def live_record_index(renderer, source_root=None):
    """The four `record_ids` indexes, mined by the renderer's own functions."""
    renderer.ROOT = Path(source_root) if source_root else renderer.ROOT
    d2 = renderer.v3_mine_d2(renderer.ROOT)
    d3 = renderer.v3_mine_d3(renderer.ROOT)
    d4 = renderer.v3_mine_d4(renderer.ROOT)
    recon = sorted(set(re.findall(r'"R6-\d\d-[A-Z]"',
                                  renderer.read_text(renderer.ROOT, renderer.RECONCILIATION))))
    return {
        "A-02": list(d3["record_ids"]),
        "A-10": sorted(set(d2["record_ids"]) | set(d2["cit_ids"])),
        "A-16": recon,
        "A-28": sorted(set(d4["record_ids"]) | set(d4["index_extra"])),
    }


def open_questions(text: str):
    rows = []
    for line in text.splitlines():
        match = OQ_RE.match(line)
        if not match:
            continue
        question = match.group(2)
        claims = "—"
        tail = re.search(r"\(unresolved claims:\s*([^)]*)\)\s*$", question)
        if tail:
            claims = tail.group(1).strip()
            question = question[: tail.start()].strip()
        rows.append({"id": match.group(1), "question": question,
                     "unresolved_claims": claims})
    return rows


def project(text: str, record_index):
    """The twin as a pure function of the packet's delivered tables."""
    _, manifest_rows = table_rows(text, MANIFEST_HEADER)
    _, ledger_rows = table_rows(text, LEDGER_HEADER)
    edge_header, edge_rows = table_rows(text, EDGE_HEADER)
    if not manifest_rows or not ledger_rows or not edge_rows:
        raise SystemExit("build-twin: the packet carries no manifest/ledger/edges table")
    manifest = []
    for cells in manifest_rows:
        row = dict(zip(MANIFEST_HEADER, cells))
        if row["path"].startswith(INLINE_ROW):
            continue
        entry = {"artifact_id": row["artifact_id"], "path": row["path"],
                 "sha256": row["sha256"]}
        if row["artifact_id"] in record_index:
            entry["record_ids"] = record_index[row["artifact_id"]]
        manifest.append(entry)
    edges = []
    for cells in edge_rows:
        row = dict(zip(edge_header, cells))
        edge = {"edge_id": row["edge_id"], "source": row["source"],
                "relation": row["relation"],
                "target_ids": [tok.strip() for tok in row["target_ids"].split(",") if tok.strip()],
                "claims": [tok.strip() for tok in row["claims"].split(",") if tok.strip()],
                "applicability": row["applicability"], "mechanism": row["mechanism"],
                "limits": row["limits"]}
        if "declared_in" in row:
            edge["declared_in"] = row["declared_in"]
        edges.append(edge)
    ledger = []
    for cells in ledger_rows:
        row = dict(zip(LEDGER_HEADER, cells))
        ledger.append({"claim_id": row["claim_id"], "claim_kind": row["kind"],
                       "evidence_status": row["evidence_status"],
                       "uncertainty": {"status": row["uncertainty_status"],
                                       "basis": row["uncertainty_basis"]},
                       "links": [tok.strip() for tok in row["links"].split(";") if tok.strip()],
                       "statement": row["statement"]})
    return {
        "packet_id": field(text, "packet_id"),
        "packet_version": (field(text, "packet_version") or "").split(" ")[0] or None,
        "profile": profile_of(text),
        "claim_ledger": ledger,
        "open_questions": open_questions(text),
        "artifact_manifest": manifest,
        "coupling_edges": edges,
    }


def render(twin) -> str:
    return json.dumps(twin, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def record_index(renderer, source_root, pins):
    """The four `record_ids` indexes, mined by the renderer's own functions.

    The mining reads the four source packets, so it is only meaningful when those
    bytes are the ones the target packet pins. Each source is digest-checked
    against the target packet's own `artifact_manifest` row before mining, and a
    mismatch refuses the build — otherwise a concurrently-rewritten live tree
    would silently produce a twin whose record index does not match the packet it
    is the twin of.
    """
    for artifact_id, relative in (("A-02", renderer.D3_PACKET),
                                  ("A-10", renderer.D2_PACKET),
                                  ("A-16", renderer.RECONCILIATION),
                                  ("A-28", renderer.D4_PACKET)):
        observed = sha256_bytes((Path(source_root) / relative).read_bytes())
        if pins.get(artifact_id) != observed:
            raise SystemExit(
                f"build-twin: source {relative} is {observed[:16]}… but the "
                f"packet pins {artifact_id} at {str(pins.get(artifact_id))[:16]}… "
                f"— pass --source-root at the pinned read set")
    renderer.ROOT = Path(source_root)
    d2 = renderer.v3_mine_d2(renderer.ROOT)
    d3 = renderer.v3_mine_d3(renderer.ROOT)
    d4 = renderer.v3_mine_d4(renderer.ROOT)
    recon = sorted(set(re.findall(r'"R6-\d\d-[A-Z]"',
                                  renderer.read_text(renderer.ROOT, renderer.RECONCILIATION))))
    return {
        "A-02": list(d3["record_ids"]),
        "A-10": sorted(set(d2["record_ids"]) | set(d2["cit_ids"])),
        "A-16": recon,
        "A-28": sorted(set(d4["record_ids"]) | set(d4["index_extra"])),
    }


def manifest_pins(text):
    _, rows = table_rows(text, MANIFEST_HEADER)
    return {dict(zip(MANIFEST_HEADER, cells))["artifact_id"]:
            dict(zip(MANIFEST_HEADER, cells))["sha256"] for cells in rows}


def build_twin(root=ROOT, source_root=None):
    """Build the declared-in-r4 twin; refuse a drifted packet or read set.

    `root` supplies the packet (digest-pinned); `source_root` supplies the four
    source packets the record index is mined from (defaults to `root`). Both are
    guarded, so a stray byte in either stops the build rather than emit a silent
    twin.
    """
    packet = (Path(root) / R4_PACKET).read_text(encoding="utf-8")
    live = sha256_bytes(packet.encode("utf-8"))
    if live != R4_PACKET_SHA256:
        raise SystemExit(f"build-twin: the source r4 packet drifted "
                         f"({live[:16]}… != {R4_PACKET_SHA256[:16]}…)")
    renderer = load_renderer()
    index = record_index(renderer, source_root or root, manifest_pins(packet))
    return project(packet, index)


def reproduce_filed(source_root=None):
    """Rebuild the two filed predecessor twins; both must be byte-identical.

    Each predecessor is mined from the read set its own packet pins, so this
    control is an end-to-end check of the projection *and* the index mining.
    """
    renderer = load_renderer()
    out = []
    for packet_rel, twin_rel, digest, version in PREDECESSORS:
        packet = read(packet_rel)
        index = record_index(renderer, source_root or ROOT, manifest_pins(packet))
        twin = project(packet, index)
        text = render(twin)
        observed = sha256_bytes(text.encode("utf-8"))
        filed = (ROOT / twin_rel).read_text(encoding="utf-8")
        out.append({"packet": packet_rel, "twin": twin_rel, "declared": digest,
                    "observed": observed, "byte_identical": text == filed,
                    "packet_version": version})
    return out


def selftest(source_root=None):
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    live_packet = sha256_bytes((ROOT / R4_PACKET).read_bytes())
    check("filed-r4-packet-digest-pinned", live_packet == R4_PACKET_SHA256,
          sha256=live_packet)
    for row in reproduce_filed(source_root):
        check(f"reproduces-filed-twin:{row['twin']}", row["byte_identical"],
              declared=row["declared"], observed=row["observed"])
    r20 = next(row for row in reproduce_filed(source_root) if row["packet_version"] == "3.0.0")
    check("r20-twin-is-the-3.0.0-shape",
          "declared_in" not in json.loads(read(PREDECESSORS[0][1]))["coupling_edges"][0],
          note="the r20 twin carries no declared_in edge column; the projection "
               "is header-adaptive, so the same code renders both shapes")
    twin = build_twin(source_root=source_root)
    text = render(twin)
    check("twin-carries-no-inline-glossary-row",
          all(not row["path"].startswith(INLINE_ROW) for row in twin["artifact_manifest"]),
          manifest_rows=len(twin["artifact_manifest"]))
    check("twin-shape-is-3.1.1",
          twin["packet_version"] == "3.1.1" and twin["profile"] == "kotodama-handoff-e2e/3"
          and "declared_in" in twin["coupling_edges"][0],
          packet_version=twin["packet_version"], profile=twin["profile"])
    check("twin-census-27-88-10",
          len(twin["claim_ledger"]) == 27 and len(twin["coupling_edges"]) == 88
          and len(twin["open_questions"]) == 10,
          claims=len(twin["claim_ledger"]), edges=len(twin["coupling_edges"]),
          open_questions=len(twin["open_questions"]))
    # the correction the r4 revision carries must be visible in the twin
    rows = {row["claim_id"]: json.dumps(row) for row in twin["claim_ledger"]}
    predecessor = json.loads(read(PREDECESSORS[1][1]))
    old = {row["claim_id"]: json.dumps(row) for row in predecessor["claim_ledger"]}
    watched = ("D4-CL05", "D4-CL06", "D4-CL07", "D4-CL09")
    check("twin-carries-the-corrected-rows",
          all(rows[cid] != old[cid] for cid in watched),
          changed=[cid for cid in watched if rows[cid] != old[cid]])
    check("twin-carries-the-corrected-oq-passenger",
          any(row["id"] == "OQ-V3-05"
              and "zero rank holds" in row["question"] for row in twin["open_questions"]))
    # The stale-assertion detector is the filed round-25 checker's own
    # `stale_hits` (imported read-only), not a token scan invented here: a
    # whole-twin token scan would flag D2-CL01's legitimate live
    # "findings_total 16 with 15 hold-or-fail" and the corrected rows' honest
    # negation ("zero `D2L-RANK` rows of either severity").
    detector = load_detector()
    surface = {row["claim_id"]: row["statement"] + " " + row["uncertainty"]["basis"]
               for row in twin["claim_ledger"]}
    surface.update({row["id"]: row["question"] for row in twin["open_questions"]})
    predecessor_surface = {row["claim_id"]: row["statement"] + " " + row["uncertainty"]["basis"]
                           for row in predecessor["claim_ledger"]}
    predecessor_surface.update({row["id"]: row["question"]
                                for row in predecessor["open_questions"]})
    check("twin-clean-under-the-filed-stale-detector",
          detector.stale_hits(surface) == [], hits=detector.stale_hits(surface)[:8])
    check("detector-fires-on-the-r22-predecessor-twin",
          sorted({row_id for row_id, _ in detector.stale_hits(predecessor_surface)})
          == sorted(detector.FIVE_ROWS),
          rows=sorted({row_id for row_id, _ in detector.stale_hits(predecessor_surface)}))
    check("twin-d2-rows-preserved-verbatim",
          [r for r in twin["claim_ledger"] if r["claim_id"].startswith("D2-")
           or r["claim_id"].startswith("CL")] ==
          [r for r in predecessor["claim_ledger"] if r["claim_id"].startswith("D2-")
           or r["claim_id"].startswith("CL")],
          rows=len([r for r in twin["claim_ledger"] if r["claim_id"].startswith("D2-")
                    or r["claim_id"].startswith("CL")]))
    passed = all(item["passed"] for item in controls)
    return {"controls": controls, "passed": passed,
            "passed_controls": sum(item["passed"] for item in controls),
            "total_controls": len(controls)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=(
        "Round-26 O seat: project the declared-in-r4 twin from the filed packet."))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--emit", action="store_true", help="write twin.json")
    group.add_argument("--stdout", action="store_true", help="print the twin")
    group.add_argument("--selftest", action="store_true")
    parser.add_argument("--source-root", type=Path,
                        help="root holding the packet's pinned read set (default: "
                             "the lane root); pass an isolated clone when the live "
                             "tree is being rewritten by a concurrent seat")
    args = parser.parse_args(argv)
    source_root = args.source_root.resolve() if args.source_root else None
    if args.selftest:
        payload = selftest(source_root)
        print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
        return 0 if payload["passed"] else 1
    text = render(build_twin(source_root=source_root))
    if args.stdout:
        sys.stdout.write(text)
        return 0
    target = HERE / "twin.json"
    target.write_text(text, encoding="utf-8")
    print(json.dumps({"wrote": str(target.relative_to(ROOT)),
                      "bytes": len(text.encode("utf-8")),
                      "sha256": sha256_bytes(text.encode("utf-8"))},
                     indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
