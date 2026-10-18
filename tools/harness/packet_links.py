#!/usr/bin/env python3
"""Claim-to-record link resolver for handoff packet v2.

Round 12 rejected the round-11 packet because D2's couplings were carried as
one aggregate edge instead of claim-to-record links (`reports/round-12/
adjacency/contract.md`, "§4 field comparison", coupling_edges row), and
because claim-ledger rows name no relation to other records. Contract §4
requires `artifact_manifest` rows with paths and record IDs, and
`coupling_edges` as "typed source→target relations". This module is the
O-impl fragment that makes those relations resolvable instead of asserted:

- a link spec is a repo-relative record pointer: `path`, `path#token`
  (record ID / anchor inside the file), `path:LINE` or `path:LINE-LINE`
  (1-based, inclusive);
- every path must exist as a file inside the repo root, with symlinks
  resolved — an escape outside the repo is a finding, not a crash;
- `#token` must match the file bytes: exact key, string value, or list
  element in a `.json` file; a word-boundary match in any other text file;
- coupling edges are checked against the `artifact_manifest` record index:
  every `target_ids` entry must be a concrete record ID that resolves to a
  real path, so range tokens like `L-01–L-40` or aggregate rows fail
  (`E-TARGET-UNKNOWN`) instead of passing as an aggregate edge.

Findings are stable-ID rows (`L-...` / `E-...`); exit 0 means no findings,
1 means findings, 2 means usage or IO errors. Output is deterministic (no
clocks or random paths) so a parent tool can freeze it into an expected.json
baseline. Inputs: `--packet FILE` reads JSON or the lane's `yaml_lines()`
line-oriented dialect (`tools/assemble-d2.py:72-95`); `--links` takes bare
specs.

CLI: packet_links.py [--packet FILE | --links SPEC[,SPEC...]]
    [--repo-root DIR] [--json] | --selftest
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

TOOL = "tools/harness/packet_links.py"
SPEC_LINE_RE = re.compile(
    r"^(?P<path>[^:]+):(?P<first>\d+)(?:-(?P<last>\d+))?$")
LINE_ANCHOR_RE = re.compile(r"^L(\d+)$")


class Finding:
    def __init__(self, code, subject, detail):
        self.code = code
        self.subject = subject
        self.detail = detail

    def as_row(self):
        return {"code": self.code, "subject": self.subject,
                "detail": self.detail}


def _looks_like_path(left):
    # Artifact IDs (A-02, A-D3) contain neither separators; repo paths do.
    return "/" in left or "." in left


def _json_path_get(node, selector):
    """Walk a dotted key path with optional [N] indices; None when absent.

    `lexicon.L01`, `sound_changes[0]`, `beliefs.B01` (v2-design §3.1).
    """
    for part in selector.split("."):
        match = re.match(r"^([A-Za-z_][\w-]*)?((?:\[\d+\])*)$", part.strip())
        if not match:
            return None
        name = match.group(1)
        if name:
            if isinstance(node, dict) and name in node:
                node = node[name]
            else:
                return None
        for index in re.findall(r"\[(\d+)\]", part):
            index = int(index)
            if isinstance(node, list) and index < len(node):
                node = node[index]
            else:
                return None
    return node


def verify_manifest_digests(manifest_rows, repo_root):
    """Re-measure live sha256 against each manifest row's pinned digest."""
    findings = []
    if not isinstance(manifest_rows, list):
        return [Finding("E-MANIFEST-NOT-LIST", "-",
                        "artifact_manifest is not a list")]
    root = Path(os.path.realpath(repo_root))
    for position, row in enumerate(manifest_rows):
        if not isinstance(row, dict):
            continue
        path = row.get("path")
        digest = row.get("digest", row.get("sha256"))
        if not path or not digest:
            findings.append(Finding(
                "M-DIGEST-MISSING", f"#{position}",
                "manifest row lacks a path or digest to re-measure"))
            continue
        digest = str(digest).removeprefix("sha256:")
        target = Path(os.path.realpath(root / str(path)))
        if not _within(root, target) or not target.is_file():
            findings.append(Finding(
                "M-DIGEST-MISSING", str(path),
                "manifest row path is not a readable in-repo file"))
            continue
        live = hashlib.sha256(target.read_bytes()).hexdigest()
        if live != digest:
            findings.append(Finding(
                "M-DIGEST-MISMATCH", str(path),
                f"live sha256 {live} != manifest {digest}"))
    return findings


def _within(root, candidate):
    try:
        return os.path.commonpath([str(root), str(candidate)]) == str(root)
    except ValueError:
        return False


def _file_lines(path):
    return len(path.read_text(encoding="utf-8", errors="replace")
               .splitlines())


def _json_contains(node, token):
    if isinstance(node, dict):
        return (token in node
                or any(_json_contains(child, token) for child in node.values()))
    if isinstance(node, list):
        return (token in node
                or any(_json_contains(child, token) for child in node))
    if isinstance(node, str):
        return node == token
    return False


def _text_contains(path, token):
    if not token:
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix == ".json":
        try:
            return _json_contains(json.loads(text), token)
        except ValueError:
            pass
    pattern = (r"(?<![A-Za-z0-9_-])" + re.escape(token)
               + r"(?![A-Za-z0-9_-])")
    return re.search(pattern, text) is not None


def resolve_link(spec, repo_root, record_index=None):
    """Resolve one link spec; return a row dict (ok plus code/detail).

    Spec forms: `<path>`, `<path>#<token>`, `<path>:LINE[-LINE]`, and the
    v2-design §3.1 artifact form `<artifact_id>#<selector>` where the id is
    a row of the packet's artifact_manifest (`record_index`) and the
    selector is `L<n>`, a dotted JSON key path, or a literal token.
    """
    row = {"spec": spec, "ok": False, "code": None, "detail": None}
    root = Path(os.path.realpath(repo_root))
    if "#" in spec:
        left, _, token = spec.partition("#")
        token = token.strip()
        if not token:
            row["code"] = "L-SPEC-MALFORMED"
            row["detail"] = "empty #selector"
            return row
    else:
        left, token = spec, None
    first = last = None
    if record_index is None or left not in record_index:
        match = SPEC_LINE_RE.match(left)
        if match:
            left = match.group("path")
            first = int(match.group("first"))
            raw_last = match.group("last")
            last = int(raw_last) if raw_last else first
    if record_index is not None and left in record_index:
        left = record_index[left]
    elif (record_index is not None and token is not None
            and not _looks_like_path(left)):
        row["code"] = "L-ARTIFACT-UNKNOWN"
        row["detail"] = f"{left!r} is not a row of the artifact_manifest"
        return row
    if not left.strip():
        row["code"] = "L-SPEC-MALFORMED"
        row["detail"] = "empty path"
        return row
    candidate = root / left
    real = Path(os.path.realpath(candidate))
    if not _within(root, real) or not _within(root, Path(os.path.abspath(
            root / left))):
        row["code"] = "L-PATH-OUTSIDE"
        row["detail"] = f"{left} escapes the repo root"
        return row
    if not real.is_file():
        row["code"] = "L-PATH-MISSING"
        row["detail"] = f"{left} is not a file in the repo"
        return row
    if token is not None:
        line_anchor = LINE_ANCHOR_RE.match(token)
        if line_anchor:
            first = last = int(line_anchor.group(1))
            token = None
        elif real.suffix == ".json":
            try:
                document = json.loads(
                    real.read_text(encoding="utf-8", errors="replace"))
            except ValueError as error:
                row["code"] = "L-SELECTOR-UNRESOLVED"
                row["detail"] = f"{left} is not parseable JSON: {error}"
                return row
            # Key path first (v2-design §3.1); a miss falls back to exact
            # value/element search for the full selector, then for the tail
            # segment — list-shaped collections address records by their id
            # value (lexicon is a list of {id: L01} rows in the live D3
            # packet), so `lexicon.L01` still resolves to the record.
            if _json_path_get(document, token) is None:
                tail = token.rsplit(".", 1)[-1] if "." in token else token
                if _json_contains(document, token) or \
                        _json_contains(document, tail):
                    token = None
                else:
                    row["code"] = "L-SELECTOR-UNRESOLVED"
                    row["detail"] = (f"selector {token!r} resolves to no "
                                     f"key path or value in {left}")
                    return row
            else:
                token = None
    if first is not None:
        if first < 1 or last < first:
            row["code"] = "L-LINE-RANGE"
            row["detail"] = f"invalid line range {first}-{last}"
            return row
        count = _file_lines(real)
        if last > count:
            row["code"] = "L-LINE-RANGE"
            row["detail"] = f"line {last} beyond end of {left} ({count} lines)"
            return row
    if token is not None and not _text_contains(real, token):
        row["code"] = "L-TOKEN-MISSING"
        row["detail"] = f"token {token!r} not found in {left}"
        return row
    row["ok"] = True
    return row


def resolve_links(specs, repo_root, record_index=None):
    return [resolve_link(spec, repo_root, record_index) for spec in specs]


def build_record_index(manifest_rows):
    """Map record IDs to repo-relative paths from artifact_manifest rows.

    Each row needs `path`; record IDs come from `record_ids` (list), the
    row's `artifact_id`, or a `record_id` scalar. Rows without a usable path
    or ID set are returned as findings for the caller to surface.
    """
    index = {}
    findings = []
    if not isinstance(manifest_rows, list):
        return index, [Finding("E-MANIFEST-NOT-LIST", "-",
                               "artifact_manifest is not a list")]
    for position, row in enumerate(manifest_rows):
        if not isinstance(row, dict) or not row.get("path"):
            findings.append(Finding(
                "E-MANIFEST-ROW", f"#{position}",
                "manifest row lacks a path"))
            continue
        path = str(row["path"])
        ids = []
        record_ids = row.get("record_ids")
        if isinstance(record_ids, list):
            ids.extend(str(value) for value in record_ids)
        if row.get("record_id"):
            ids.append(str(row["record_id"]))
        if row.get("artifact_id"):
            ids.append(str(row["artifact_id"]))
        if not ids:
            findings.append(Finding(
                "E-MANIFEST-ROW", path,
                "manifest row names no record IDs"))
            continue
        for record_id in ids:
            index[record_id] = path
    return index, findings


def resolve_edges(edges, record_index, repo_root, claim_ids=None):
    """Resolve coupling-edge target IDs against the record index.

    Every target must be one concrete record ID present in the index and its
    path must resolve inside the repo; range tokens or invented IDs fail.
    An edge declaring `aggregate: true` is flagged outright. With
    `claim_ids`, an edge naming no existing claim id (`claim`/`claims`
    column, v2-design §3.1) fails E-EDGE-NO-CLAIM.
    """
    findings = []
    if not isinstance(edges, list):
        return [Finding("E-EDGES-NOT-LIST", "-",
                        "coupling_edges is not a list")]
    for edge in edges:
        if not isinstance(edge, dict):
            findings.append(Finding("E-EDGE-NOT-MAP", "#",
                                    "edge row is not a mapping"))
            continue
        edge_id = str(edge.get("edge_id", "#"))
        if edge.get("aggregate"):
            findings.append(Finding(
                "E-EDGE-AGGREGATE", edge_id,
                "edge declares itself an aggregate row"))
        if claim_ids is not None:
            named = edge.get("claims", edge.get("claim"))
            named = ([str(value) for value in named]
                     if isinstance(named, list)
                     else ([str(named)] if named else []))
            if not named or not any(value in claim_ids for value in named):
                findings.append(Finding(
                    "E-EDGE-NO-CLAIM", edge_id,
                    "edge names no existing claim id"))
        targets = edge.get("target_ids")
        if not isinstance(targets, list) or not targets:
            findings.append(Finding(
                "E-EDGE-NO-TARGETS", edge_id,
                "edge names no concrete target records"))
            continue
        for target in targets:
            target = str(target)
            if target not in record_index:
                findings.append(Finding(
                    "E-TARGET-UNKNOWN", edge_id,
                    f"target {target!r} is not a concrete record ID in the "
                    f"artifact_manifest index"))
                continue
            row = resolve_link(record_index[target], repo_root)
            if not row["ok"]:
                findings.append(Finding(
                    "E-TARGET-UNRESOLVED", edge_id,
                    f"target {target!r} path did not resolve: "
                    f"{row['code']} {row['detail']}"))
    return findings


# --------------------------------------------------------------------------
# Packet reading (shared dialect with packet_uncertainty.py): JSON, or the
# yaml_lines() line-oriented form of `tools/assemble-d2.py:72-95`.

def _parse_scalar(text):
    text = text.strip()
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
            return text[1:-1]
        return text


def _parse_block(lines, start, indent):
    i = start
    while i < len(lines) and (lines[i].strip() == ""
                              or lines[i].startswith("#")):
        i += 1
    if i >= len(lines):
        return None, i
    line = lines[i]
    lead = len(line) - len(line.lstrip(" "))
    if lead < indent:
        return None, start
    body = line.lstrip(" ")
    if body.startswith("-"):
        # Sequence: sibling dashes sit at the first item's own column; item
        # content (after a bare dash) sits two columns deeper.
        dash_col = lead
        items = []
        while i < len(lines):
            raw = lines[i]
            if raw.strip() == "":
                i += 1
                continue
            lead2 = len(raw) - len(raw.lstrip(" "))
            body2 = raw.lstrip(" ")
            if lead2 != dash_col or not body2.startswith("-"):
                break
            if body2 == "-":
                value, i = _parse_block(lines, i + 1, dash_col + 2)
                items.append(value)
            else:
                items.append(_parse_scalar(body2[1:].strip()))
                i += 1
        return items, i
    mapping = {}
    i = start
    while i < len(lines):
        raw = lines[i]
        if raw.strip() == "" or raw.lstrip(" ").startswith("#"):
            i += 1
            continue
        lead = len(raw) - len(raw.lstrip(" "))
        if lead < indent:
            break
        body = raw.strip()
        if body.startswith("- "):
            break
        if ":" not in body:
            raise ValueError(f"line {i + 1}: not a mapping row: {body!r}")
        key, _, rest = body.partition(":")
        key = _parse_scalar(key.strip())
        rest = rest.strip()
        if rest:
            mapping[key] = _parse_scalar(rest)
            i += 1
        else:
            value, i = _parse_block(lines, i + 1, indent + 2)
            if value is None:
                # Tolerate dash lists at the key's own column.
                j = i
                while j < len(lines) and (lines[j].strip() == ""
                                          or lines[j].startswith("#")):
                    j += 1
                if j < len(lines):
                    leadj = len(lines[j]) - len(lines[j].lstrip(" "))
                    if leadj == indent and lines[j].lstrip(" ").startswith("-"):
                        value, i = _parse_block(lines, i + 1, indent)
            mapping[key] = value
    return mapping, i


def _expand_inline_dashes(lines):
    """Expand compact `- key: value` items into dialect form.

    The yaml_lines() serializer (`tools/assemble-d2.py:72-95`) always emits a
    bare `-` line followed by keys two columns deeper, but hand-written
    packets commonly use the compact form. A dash line expands only when the
    content starts with a bare identifier key (the dialect's own key rule),
    so scalar items like `- docs/x.md:53-70` stay scalars.
    """
    expanded = []
    for line in lines:
        match = re.match(r"^(\s*)- (.+)$", line)
        content = match.group(2).strip() if match else None
        if (match and content
                and re.match(r"^[A-Za-z_][\w-]*\s*:", content)):
            expanded.append(match.group(1) + "-")
            expanded.append(match.group(1) + "  " + content)
        else:
            expanded.append(line)
    return expanded


def read_packet(path):
    text = Path(path).read_text(encoding="utf-8")
    stripped = text.lstrip()
    if stripped.startswith("{") or stripped.startswith("["):
        return json.loads(text)
    value, _ = _parse_block(_expand_inline_dashes(text.splitlines()), 0, 0)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: packet root is not a mapping")
    return value


def packet_specs(data):
    """Extract (claim link specs, edges, manifest rows) from a packet."""
    claims = data.get("claim_ledger", data.get("claims")) or []
    specs = []
    for claim in claims:
        if isinstance(claim, dict) and isinstance(claim.get("links"), list):
            specs.extend(str(spec) for spec in claim["links"])
    edges = data.get("coupling_edges")
    manifest = data.get("artifact_manifest")
    if isinstance(manifest, dict):
        manifest = manifest.get("rows")
    return specs, edges, manifest


# --------------------------------------------------------------------------

def _selftest():
    """Positive + negative fixtures under tempfile; no repo writes."""
    import tempfile

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        docs = root / "docs"
        docs.mkdir()
        contract = docs / "contract.md"
        contract.write_text(
            "\n".join(f"line {n} of the fixture contract" for n in range(1, 91))
            + "\n", encoding="utf-8")
        data_dir = root / "data"
        data_dir.mkdir()
        packet_json = data_dir / "packet.json"
        packet_json.write_text(json.dumps({
            "sound_changes": [{"id": "SC1", "rule": "/p/ > /f/"}],
            "lexicon": ["L01", "L02"],
            "beliefs": {"B01": {"id": "B01"}},
        }), encoding="utf-8")
        outside = root.parent / "outside-secret.txt"
        outside.write_text("outside\n", encoding="utf-8")
        escape = docs / "escape.md"
        escape.symlink_to(outside)

        good = [
            ("data/packet.json", True),
            ("data/packet.json#SC1", True),
            ("data/packet.json#L01", True),
            ("docs/contract.md", True),
            ("docs/contract.md:53-70", True),
            ("docs/contract.md:90", True),
        ]
        for spec, expected_ok in good:
            row = resolve_link(spec, root)
            if row["ok"] != expected_ok:
                failures.append(f"{spec}: expected ok={expected_ok}, got {row}")
        bad = [
            ("data/packet.json#NOPE", "L-SELECTOR-UNRESOLVED"),
            ("data/missing.json", "L-PATH-MISSING"),
            ("docs/contract.md#NOT-ANYWHERE", "L-TOKEN-MISSING"),
            ("docs/contract.md:91", "L-LINE-RANGE"),
            ("docs/contract.md:0", "L-LINE-RANGE"),
            ("docs/contract.md:70-53", "L-LINE-RANGE"),
            ("docs/escape.md", "L-PATH-OUTSIDE"),
            ("data/packet.json#", "L-SPEC-MALFORMED"),
        ]
        for spec, expected_code in bad:
            row = resolve_link(spec, root)
            if row["ok"] or row["code"] != expected_code:
                failures.append(
                    f"{spec}: expected {expected_code}, got {row}")

        d3_digest = hashlib.sha256(packet_json.read_bytes()).hexdigest()
        con_digest = hashlib.sha256(contract.read_bytes()).hexdigest()
        manifest = [
            {"artifact_id": "A-D3", "path": "data/packet.json",
             "digest": f"sha256:{d3_digest}",
             "record_ids": ["SC1", "L01", "L02"]},
            {"artifact_id": "A-CON", "path": "docs/contract.md",
             "digest": con_digest, "record_id": "CONTRACT"},
            {"artifact_id": "A-STALE", "path": "docs/contract.md",
             "digest": "sha256:" + "0" * 64, "record_ids": ["STALE"]},
        ]
        index, index_findings = build_record_index(manifest)
        if index_findings:
            failures.append(f"index findings on clean manifest: "
                            f"{index_findings}")
        if set(index) != {"SC1", "L01", "L02", "CONTRACT", "A-D3",
                          "A-CON", "STALE", "A-STALE"}:
            failures.append(f"index wrong: {sorted(index)}")

        artifact_good = [
            ("A-D3#sound_changes[0]", True),
            ("A-D3#beliefs.B01", True),
            ("A-CON#L90", True),
            ("A-CON#fixture", True),
        ]
        for spec, expected_ok in artifact_good:
            row = resolve_link(spec, root, index)
            if row["ok"] != expected_ok:
                failures.append(f"{spec}: expected ok={expected_ok}, "
                                f"got {row}")
        artifact_bad = [
            ("GHOST#SC1", "L-ARTIFACT-UNKNOWN"),
            ("A-D3#beliefs.GHOST", "L-SELECTOR-UNRESOLVED"),
            ("A-D3#sound_changes[7]", "L-SELECTOR-UNRESOLVED"),
            ("A-CON#L91", "L-LINE-RANGE"),
        ]
        for spec, expected_code in artifact_bad:
            row = resolve_link(spec, root, index)
            if row["ok"] or row["code"] != expected_code:
                failures.append(
                    f"{spec}: expected {expected_code}, got {row}")

        digest_findings = verify_manifest_digests(manifest, root)
        if [f.code for f in digest_findings] != ["M-DIGEST-MISMATCH"]:
            failures.append(f"digest verify: {digest_findings}")

        edges_ok = [
            {"edge_id": "BR01", "relation": "method-transfer",
             "target_ids": ["SC1", "L01"], "claims": ["CL-1"]},
            {"edge_id": "BR02", "relation": "analogy",
             "target_ids": ["CONTRACT"], "claim": "CL-1"},
        ]
        clean = resolve_edges(edges_ok, index, root, claim_ids={"CL-1"})
        if clean:
            failures.append(f"clean edges flagged: {clean}")

        aggregate_like = [
            {"edge_id": "D2-EDGES", "relation": "dependency",
             "target_ids": ["L-01–L-40", "NM-01–NM-08"]},
            {"edge_id": "AGG", "aggregate": True, "target_ids": ["SC1"]},
            {"edge_id": "EMPTY", "target_ids": []},
            {"edge_id": "BROKEN", "target_ids": ["GHOST"]},
        ]
        codes = sorted(f.code for f in
                       resolve_edges(aggregate_like, index, root))
        expected = sorted(["E-TARGET-UNKNOWN", "E-TARGET-UNKNOWN",
                           "E-TARGET-UNKNOWN", "E-EDGE-AGGREGATE",
                           "E-EDGE-NO-TARGETS"])
        if codes != expected:
            failures.append(f"aggregate fixtures: expected {expected}, "
                            f"got {codes}")

        claim_crosswalk = [
            {"edge_id": "NOCLAIM", "target_ids": ["SC1"]},
            {"edge_id": "ORPHAN", "target_ids": ["SC1"],
             "claims": ["NO-SUCH-CLAIM"]},
        ]
        codes = sorted(f.code for f in
                       resolve_edges(claim_crosswalk, index, root,
                                     claim_ids={"CL-1"}))
        if codes != ["E-EDGE-NO-CLAIM", "E-EDGE-NO-CLAIM"]:
            failures.append(f"claim crosswalk: expected two NO-CLAIM, "
                            f"got {codes}")

    if failures:
        for failure in failures:
            print(f"selftest: FAIL {failure}", file=sys.stderr)
        return 1
    print("selftest: 31 checks passed (path/token/line specs, artifact-id "
          "refs, JSON key paths, L-anchors, symlink escape, digests, "
          "record index, aggregate+claim crosswalk rejection)")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Resolve handoff packet v2 claim-to-record links and "
                    "coupling-edge targets (L-*/E-* findings).")
    parser.add_argument("--packet", type=Path,
                        help="packet file: JSON or the yaml_lines dialect")
    parser.add_argument("--links",
                        help="comma-separated bare link specs")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(),
                        help="repo root the specs are relative to "
                             "(default: cwd)")
    parser.add_argument("--json", action="store_true",
                        help="emit findings as one JSON object")
    parser.add_argument("--no-digests", action="store_true",
                        help="skip live sha256 re-measurement of manifest "
                             "rows (default: verify)")
    parser.add_argument("--selftest", action="store_true",
                        help="run embedded positive/negative fixtures")
    args = parser.parse_args(argv)

    if args.selftest:
        return _selftest()
    if bool(args.packet) == bool(args.links):
        parser.error("exactly one of --packet / --links is required")

    try:
        if args.packet:
            data = read_packet(args.packet)
            specs, edges, manifest = packet_specs(data)
            claim_rows = data.get("claim_ledger", data.get("claims")) or []
            claim_ids = {str(c["claim_id"]) for c in claim_rows
                         if isinstance(c, dict) and c.get("claim_id")}
            index, index_findings = build_record_index(manifest or [])
        else:
            specs = [part.strip() for part in args.links.split(",") if
                     part.strip()]
            edges = manifest = index = claim_ids = None
            index_findings = []
    except (OSError, ValueError) as error:
        print(f"{TOOL}: cannot read packet: {error}", file=sys.stderr)
        return 2

    rows = resolve_links(specs, args.repo_root, index)
    findings = [Finding(row["code"], row["spec"], row["detail"])
                for row in rows if not row["ok"]]
    findings.extend(index_findings)
    if edges is not None:
        findings.extend(resolve_edges(edges, index, args.repo_root,
                                      claim_ids))
        if not args.no_digests:
            findings.extend(verify_manifest_digests(manifest or [],
                                                    args.repo_root))

    if args.json:
        print(json.dumps({
            "tool": TOOL,
            "links_checked": len(rows),
            "resolved": sum(1 for row in rows if row["ok"]),
            "findings": [f.as_row() for f in findings],
        }, ensure_ascii=False, indent=1))
    else:
        for row in rows:
            if not row["ok"]:
                continue
            print(f"ok [{row['spec']}]")
        for finding in findings:
            detail = finding.as_row()
            print(f"{detail['code']} [{detail['subject']}] "
                  f"{detail['detail']}")
        print(f"links={len(rows)} "
              f"resolved={sum(1 for row in rows if row['ok'])} "
              f"findings={len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
