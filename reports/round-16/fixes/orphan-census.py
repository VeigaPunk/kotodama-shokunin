#!/usr/bin/env python3
"""Delivered-record coverage census for handoff packet v2 (review-9.md F9-2).

v2-design §3.2 rule 4: every delivered record id appears in >=1 claim link or
coupling-edge target — no orphan records. The round-15 reviewer census found
33 delivered D3 records with neither (18 lexemes L03-L20, 6 names N01-N06,
3 materials M01-M03, 2 objects O02-O03, 4 utterances U03-U06), riding only on
the manifest record_ids index, the inline glossary payload and the
requested_decisions rows. This module is the standing control for that rule:

- delivered ids are enumerated from the D3 payload's own `id` fields
  (examples/culture-d3/packet.json collections: lexicon, names, utterances,
  materials, objects, costumes, eras, beliefs, symbols, references, bridges,
  sound_changes, speech_rules, naming_rule, rank_rules);
- carried ids are read from the packet's machine surface: the tail segment of
  every claim link selector (`A-02#lexicon.L03` -> L03, `path#SC1` -> SC1),
  every coupling-edge target, source and edge_id;
- orphans = delivered - carried; exit 0 iff none.

CLI: orphan-census.py [--packet FILE] [--payload FILE] [--repo-root DIR]
                      [--json] | --selftest
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

TOOL = "reports/round-16/fixes/orphan-census.py"
REPO = Path(__file__).resolve().parents[3]
DEFAULT_PACKET = "reports/round-16/handoff/packet-v2-07.yml"
DEFAULT_PAYLOAD = "examples/culture-d3/packet.json"
COLLECTIONS = ("lexicon", "names", "utterances", "materials", "objects",
               "costumes", "eras", "beliefs", "symbols", "references",
               "bridges", "sound_changes", "speech_rules", "naming_rule",
               "rank_rules")


def delivered_ids(payload):
    ids = []
    for collection in COLLECTIONS:
        rows = payload.get(collection)
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict) and row.get("id"):
                    ids.append(str(row["id"]))
        elif isinstance(rows, dict) and rows.get("id"):
            ids.append(str(rows["id"]))
    return ids


def carried_ids(data):
    from_links, from_edges = set(), set()
    claims = data.get("claim_ledger", data.get("claims")) or []
    for claim in claims:
        if not isinstance(claim, dict):
            continue
        for spec in claim.get("links") or []:
            spec = str(spec)
            if "#" not in spec:
                continue
            selector = spec.partition("#")[2].strip()
            tail = selector.rsplit(".", 1)[-1]
            for part in ("[]",):
                tail = tail.replace(part, "")
            from_links.add(tail)
    for edge in data.get("coupling_edges") or []:
        if not isinstance(edge, dict):
            continue
        if edge.get("edge_id"):
            from_edges.add(str(edge["edge_id"]))
        if edge.get("source"):
            from_edges.add(str(edge["source"]))
        for target in edge.get("target_ids") or []:
            from_edges.add(str(target))
    return from_links, from_edges


def census(packet_path, payload_path, repo_root):
    sys.path.insert(0, str(REPO / "tools" / "harness"))
    import packet_links

    data = packet_links.read_packet(packet_path)
    payload = json.loads(Path(payload_path).read_text(encoding="utf-8"))
    delivered = delivered_ids(payload)
    from_links, from_edges = carried_ids(data)
    carried = from_links | from_edges
    orphans = [record for record in delivered if record not in carried]
    return {
        "tool": TOOL,
        "packet": str(packet_path),
        "payload": str(payload_path),
        "design_rule": "v2-design §3.2 rule 4 (no orphan delivered records)",
        "delivered_total": len(delivered),
        "delivered_ids": delivered,
        "carried_in_claim_links": sorted(record for record in delivered
                                         if record in from_links),
        "carried_in_edges": sorted(record for record in delivered
                                   if record in from_edges
                                   and record not in from_links),
        "orphan_count": len(orphans),
        "orphans": orphans,
    }


def _selftest():
    import tempfile

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        payload = {"lexicon": [{"id": "L01"}, {"id": "L02"}],
                   "names": [{"id": "N01"}]}
        payload_path = root / "packet.json"
        payload_path.write_text(json.dumps(payload), encoding="utf-8")
        good = root / "good.yml"
        good.write_text(
            "claim_ledger:\n"
            "  - claim_id: CL01\n"
            "    links:\n"
            "      - \"examples/packet.json#SC1\"\n"
            "      - \"A-02#lexicon.L02\"\n"
            "      - \"A-02#names.N01\"\n"
            "coupling_edges:\n"
            "  - edge_id: BR01\n"
            "    source: S01\n"
            "    target_ids:\n"
            "      - \"L01\"\n",
            encoding="utf-8")
        report = census(good, payload_path, root)
        if report["orphan_count"] != 0 or report["orphans"]:
            failures.append(f"clean packet flagged orphans: {report}")
        if report["delivered_total"] != 3:
            failures.append(f"delivered enumeration wrong: {report}")
        bad = root / "bad.yml"
        bad.write_text(
            "claim_ledger:\n"
            "  - claim_id: CL01\n"
            "    links:\n"
            "      - \"examples/packet.json#SC1\"\n"
            "      - \"A-02#lexicon.L02\"\n"
            "coupling_edges:\n"
            "  - edge_id: BR01\n"
            "    source: S01\n"
            "    target_ids:\n"
            "      - \"L01\"\n",
            encoding="utf-8")
        report = census(bad, payload_path, root)
        if report["orphan_count"] != 1 or report["orphans"] != ["N01"]:
            failures.append(f"orphan missed: {report}")
    if failures:
        for failure in failures:
            print(f"selftest: FAIL {failure}", file=sys.stderr)
        return 1
    print("selftest: 3 checks passed (delivered enumeration, dotted-tail "
          "carriage, orphan detection)")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Census delivered D3 records without a claim link or "
                    "coupling-edge target (v2-design §3.2 rule 4 / F9-2).")
    parser.add_argument("--packet", type=Path, default=Path(DEFAULT_PACKET),
                        help=f"packet machine twin (default: {DEFAULT_PACKET})")
    parser.add_argument("--payload", type=Path, default=Path(DEFAULT_PAYLOAD),
                        help="D3 payload delivering the records")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true",
                        help="emit the census as one JSON object")
    parser.add_argument("--selftest", action="store_true",
                        help="run embedded positive/negative fixtures")
    args = parser.parse_args(argv)
    if args.selftest:
        return _selftest()
    try:
        report = census(args.packet, args.payload, args.repo_root)
    except (OSError, ValueError, ImportError) as error:
        print(f"{TOOL}: cannot census: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print(f"packet: {report['packet']}")
        print(f"delivered D3 record ids: {report['delivered_total']}")
        print(f"carried in claim links: {len(report['carried_in_claim_links'])}")
        print(f"carried (edges only): {len(report['carried_in_edges'])}")
        print(f"orphans: {report['orphan_count']} {report['orphans']}")
    return 0 if report["orphan_count"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
