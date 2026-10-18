#!/usr/bin/env python3
"""Uncertainty-field validator for handoff packet v2 claim ledgers.

Round 12 rejected the round-11 packet on semantics: the claim ledger carried
no per-claim uncertainty dimension (`reports/round-12/adjacency/contract.md`,
"§4 field comparison", claim_ledger row). Contract §4 requires each
`claim_ledger` row to state "evidence status, uncertainty, and relation to
other records". This module is the O-impl fragment that makes the uncertainty
dimension checkable instead of prose:

- every claim must carry `uncertainty: {status: <supported|partial|unresolved>,
  basis: <text>}` with no extra keys;
- `basis` must be individually reasoned text: non-empty, at least
  `--min-basis-len` characters (default 40), free of boilerplate tokens, and
  unique across claims after normalization ("zero boilerplate");
- optionally (`--require-oq`) every `unresolved` claim must be referenced by
  some `open_questions` row, so unresolved items stay routed, not dropped.

Findings are stable-ID rows (`U-...`); exit 0 means no findings, 1 means
findings, 2 means usage or IO errors. Output is deterministic (no clocks or
random paths) so a parent tool can freeze it into an expected.json baseline.

Inputs: `--packet FILE` reads the lane's own serialization — JSON, or the
line-oriented YAML dialect emitted by `yaml_lines()`
(`tools/assemble-d2.py:72-95`); no third-party YAML module is required.
`--claims-json FILE` accepts a bare list of claim dicts.

CLI: packet_uncertainty.py [--packet FILE | --claims-json FILE]
    [--min-basis-len N] [--require-oq] [--json] | --selftest
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

STATUS_VOCABULARY = ("supported", "partial", "unresolved")
REQUIRED_UNCERTAINTY_KEYS = ("status", "basis")
DEFAULT_MIN_BASIS_LEN = 40
# Generic filler that names no reason; matched case-insensitively as the whole
# basis or as a standalone line inside it. None of these cite a locator.
BOILERPLATE_TOKENS = (
    "none",
    "n/a",
    "na",
    "ok",
    "pass",
    "passed",
    "tbd",
    "to-verify",
    "todo",
    "same as above",
    "see above",
    "as usual",
    "standard",
    "verified",
    "looks good",
    "fine",
)
TOOL = "tools/harness/packet_uncertainty.py"


class Finding:
    def __init__(self, code, claim_id, detail):
        self.code = code
        self.claim_id = claim_id
        self.detail = detail

    def as_row(self):
        return {
            "code": self.code,
            "claim_id": self.claim_id,
            "detail": self.detail,
        }


def _normalize_basis(text):
    return re.sub(r"\s+", " ", text).strip().casefold()


def _is_boilerplate(basis):
    folded = _normalize_basis(basis)
    if folded in BOILERPLATE_TOKENS:
        return True
    return any(
        f" {token} " in f" {folded} " for token in BOILERPLATE_TOKENS
        if " " in token
    )


def parse_basis(basis):
    """Split a basis string into its grammar slots (v2-design §2.2).

    Returns {"grounding": str|None, "restriction": str|None, "open":
    str|None, "owner": str|None}. Slots are the text after each literal
    prefix (`grounding:`, `restriction:`, `open:`, `owner:`); a slot holds
    only its own clause, so prefixes may appear in any order.
    """
    slots = {"grounding": None, "restriction": None, "open": None,
             "owner": None}
    if not isinstance(basis, str):
        return slots
    pattern = re.compile(
        r"(grounding|restriction|open|owner)\s*:\s*", re.IGNORECASE)
    matches = list(pattern.finditer(basis))
    if not matches:
        return slots
    for position, match in enumerate(matches):
        name = match.group(1).lower()
        end = matches[position + 1].start() if position + 1 < len(matches) \
            else len(basis)
        value = basis[match.end():end].strip().rstrip(";").strip()
        if slots.get(name) is None:
            slots[name] = value
    return slots


def _restates_status(basis, claim):
    folded = _normalize_basis(basis)
    candidates = [claim.get("evidence_status")]
    uncertainty = claim.get("uncertainty")
    if isinstance(uncertainty, dict):
        candidates.append(uncertainty.get("status"))
    return any(isinstance(token, str) and folded == _normalize_basis(token)
               for token in candidates)


def validate_uncertainty(claims, min_basis_len=DEFAULT_MIN_BASIS_LEN,
                         open_questions=None):
    """Return the finding list for a claim-ledger list.

    `claims` is a list of dicts; each needs a `claim_id` and an `uncertainty`
    mapping. `open_questions`, when given, is the packet's open_questions
    list; each `unresolved` claim must be referenced there.
    """
    findings = []
    if not isinstance(claims, list):
        return [Finding("U-CLAIMS-NOT-LIST", "-",
                        "claim_ledger is not a list")]
    if not claims:
        return [Finding("U-CLAIMS-EMPTY", "-", "claim_ledger has no rows")]

    seen_bases = {}
    oq_text = None
    if open_questions is not None:
        if not isinstance(open_questions, list):
            findings.append(Finding("U-OQ-NOT-LIST", "-",
                                    "open_questions is not a list"))
            open_questions = None
        else:
            oq_text = json.dumps(open_questions, ensure_ascii=False)

    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            findings.append(Finding("U-CLAIM-NOT-MAP", f"#{index}",
                                    "claim row is not a mapping"))
            continue
        claim_id = str(claim.get("claim_id", f"#{index}"))
        uncertainty = claim.get("uncertainty")
        if uncertainty is None:
            findings.append(Finding(
                "U-FIELD-MISSING", claim_id,
                "claim has no uncertainty field"))
            continue
        if not isinstance(uncertainty, dict):
            findings.append(Finding(
                "U-FIELD-NOT-MAP", claim_id,
                "uncertainty is not a mapping"))
            continue
        extra = sorted(set(uncertainty) - set(REQUIRED_UNCERTAINTY_KEYS))
        if extra:
            findings.append(Finding(
                "U-FIELD-EXTRA", claim_id,
                "uncertainty has unexpected keys: " + ", ".join(extra)))
        missing = [key for key in REQUIRED_UNCERTAINTY_KEYS
                   if key not in uncertainty]
        if missing:
            findings.append(Finding(
                "U-FIELD-PARTIAL", claim_id,
                "uncertainty lacks keys: " + ", ".join(missing)))
            continue

        status = uncertainty["status"]
        if status not in STATUS_VOCABULARY:
            findings.append(Finding(
                "U-STATUS-VOCAB", claim_id,
                f"status {status!r} outside " + "|".join(STATUS_VOCABULARY)))

        basis = uncertainty["basis"]
        if not isinstance(basis, str) or not basis.strip():
            findings.append(Finding(
                "U-BASIS-EMPTY", claim_id,
                "basis is empty or not a string"))
        else:
            if len(basis.strip()) < min_basis_len:
                findings.append(Finding(
                    "U-BASIS-SHORT", claim_id,
                    f"basis is {len(basis.strip())} chars; "
                    f"minimum {min_basis_len}"))
            if _is_boilerplate(basis):
                findings.append(Finding(
                    "U-BASIS-BOILERPLATE", claim_id,
                    "basis is a boilerplate token, not a reason"))
            if _restates_status(basis, claim):
                findings.append(Finding(
                    "U-BASIS-RESTATES", claim_id,
                    "basis only restates the status or evidence_status "
                    "token"))
            slots = parse_basis(basis)
            if slots["grounding"] is None:
                findings.append(Finding(
                    "U-BASIS-NO-GROUNDING", claim_id,
                    "basis lacks the mandatory 'grounding:' witness clause"))
            if status == "partial" and slots["restriction"] is None:
                findings.append(Finding(
                    "U-BASIS-NO-RESTRICTION", claim_id,
                    "partial claim lacks the 'restriction:' clause"))
            if status == "unresolved":
                if slots["open"] is None:
                    findings.append(Finding(
                        "U-BASIS-NO-OPEN", claim_id,
                        "unresolved claim lacks the 'open:' clause"))
                if slots["owner"] is None:
                    findings.append(Finding(
                        "U-BASIS-NO-OWNER", claim_id,
                        "unresolved claim lacks the 'owner:' clause"))
            key = _normalize_basis(basis)
            if key in seen_bases:
                findings.append(Finding(
                    "U-BASIS-DUPLICATE", claim_id,
                    f"basis identical to claim {seen_bases[key]}"))
            else:
                seen_bases[key] = claim_id

        if oq_text is not None and status == "unresolved":
            if claim_id not in oq_text:
                findings.append(Finding(
                    "U-OQ-UNROUTED", claim_id,
                    "unresolved claim is not referenced by any "
                    "open_questions row"))

    return findings


# --------------------------------------------------------------------------
# Packet reading: JSON, or the yaml_lines() line-oriented dialect
# (`tools/assemble-d2.py:72-95`): mappings `key: <json scalar>` or `key:`
# followed by a deeper block; sequences as `-` blocks or `- scalar` lines.

def _parse_scalar(text):
    text = text.strip()
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
            return text[1:-1]
        return text


def _parse_block(lines, start, indent):
    """Parse lines[start:] at exactly `indent`; return (value, next_index)."""
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
    """Read a packet file; return its top-level mapping.

    JSON packets load directly; otherwise the text is parsed with the
    yaml_lines() dialect parser above.
    """
    text = Path(path).read_text(encoding="utf-8")
    stripped = text.lstrip()
    if stripped.startswith("{") or stripped.startswith("["):
        return json.loads(text)
    value, _ = _parse_block(_expand_inline_dashes(text.splitlines()), 0, 0)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: packet root is not a mapping")
    return value


def packet_sections(data):
    """Extract (claims, open_questions) from a packet mapping.

    Accepts `claim_ledger` or `claims` as the ledger key; open_questions may
    be absent (None).
    """
    claims = data.get("claim_ledger", data.get("claims"))
    open_questions = data.get("open_questions")
    if isinstance(open_questions, dict):
        open_questions = open_questions.get("rows")
    return claims, open_questions


# --------------------------------------------------------------------------

def _selftest():
    """Positive + negative fixtures; writes only under tempfile."""
    import tempfile

    failures = []
    good_basis = ("grounding: A-D2; the typed-label coverage check holds 15 "
                  "of 16 findings at hold-or-fail in "
                  "examples/culture-d2/typed-labels.d2.yml")
    claims_ok = [
        {"claim_id": "CL-A", "uncertainty": {
            "status": "supported", "basis": good_basis}},
        {"claim_id": "CL-B", "uncertainty": {
            "status": "partial",
            "basis": "grounding: A-S02; restriction: support rests on the "
                     "museum object record alone, which carries the "
                     "museum's own dating caveat"}},
        {"claim_id": "CL-C", "uncertainty": {
            "status": "unresolved",
            "basis": "grounding: A-SCR; open: no real-language sweep exists "
                     "for any spelling; owner: kotodama"}},
    ]
    clean = validate_uncertainty(claims_ok)
    if clean:
        failures.append(f"clean fixture produced findings: {clean}")

    oq = [{"id": "OQ-1", "question": "screening?", "claims": ["CL-C"]}]
    routed = validate_uncertainty(claims_ok, open_questions=oq)
    if routed:
        failures.append(f"routed unresolved claim flagged: {routed}")
    unrouted = validate_uncertainty(claims_ok, open_questions=[])
    if [f.code for f in unrouted] != ["U-OQ-UNROUTED"]:
        failures.append(f"unrouted unresolved claim not flagged: {unrouted}")

    bad_cases = [
        ({"claim_id": "X1"}, ["U-FIELD-MISSING"]),
        ({"claim_id": "X2", "uncertainty": "supported"}, ["U-FIELD-NOT-MAP"]),
        ({"claim_id": "X3", "uncertainty": {
            "status": "supported", "basis": "grounding: A-D2; extra key "
            "probe with sufficiently long unique text to clear the floor",
            "note": "x"}},
         ["U-FIELD-EXTRA"]),
        ({"claim_id": "X4", "uncertainty": {"status": "supported"}},
         ["U-FIELD-PARTIAL"]),
        ({"claim_id": "X5", "uncertainty": {
            "status": "true", "basis": "grounding: A-D2; status vocabulary "
            "probe with unique text clearing the length floor"}},
         ["U-STATUS-VOCAB"]),
        ({"claim_id": "X6", "uncertainty": {
            "status": "supported", "basis": ""}}, ["U-BASIS-EMPTY"]),
        ({"claim_id": "X7", "uncertainty": {
            "status": "supported", "basis": "short"}},
         ["U-BASIS-SHORT", "U-BASIS-NO-GROUNDING"]),
        ({"claim_id": "X8", "uncertainty": {
            "status": "supported", "basis": "n/a"}},
         ["U-BASIS-SHORT", "U-BASIS-BOILERPLATE", "U-BASIS-NO-GROUNDING"]),
        ({"claim_id": "X9", "uncertainty": {
            "status": "supported", "basis": good_basis}},
         ["U-BASIS-DUPLICATE"]),
        ({"claim_id": "X10", "uncertainty": {
            "status": "supported", "basis": good_basis + "!"}}, []),
        ({"claim_id": "X11", "uncertainty": {
            "status": "supported", "basis": "no grounding clause at all, "
            "just prose long enough to clear the length floor"}},
         ["U-BASIS-NO-GROUNDING"]),
        ({"claim_id": "X12", "uncertainty": {
            "status": "partial", "basis": "grounding: A-S02; restriction "
            "clause missing entirely from this long-enough basis string"}},
         ["U-BASIS-NO-RESTRICTION"]),
        ({"claim_id": "X13", "uncertainty": {
            "status": "unresolved", "basis": "grounding: A-SCR; open: "
            "screening unperformed but no owner is named here at all"}},
         ["U-BASIS-NO-OWNER"]),
        ({"claim_id": "X14", "evidence_status": "invented", "uncertainty": {
            "status": "supported", "basis": "supported"}},
         ["U-BASIS-SHORT", "U-BASIS-RESTATES", "U-BASIS-NO-GROUNDING"]),
    ]
    for claim, expected_codes in bad_cases:
        got = [f.code for f in validate_uncertainty(
            [claims_ok[0], claim])]
        if got != expected_codes:
            failures.append(
                f"negative fixture {claim.get('claim_id')}: "
                f"expected {expected_codes}, got {got}")

    empty_ledger = validate_uncertainty([])
    if [f.code for f in empty_ledger] != ["U-CLAIMS-EMPTY"]:
        failures.append(f"empty ledger not flagged: {empty_ledger}")

    dialect = (
        "claims:\n"
        "  - claim_id: CL-A\n"
        "    kind: generative rule\n"
        "    uncertainty:\n"
        "      status: supported\n"
        "      basis: \"grounding: A-D2; holds for the measured rows: 15 "
        "of 16 label findings are hold-or-fail\"\n"
        "    links:\n"
        "      - examples/culture-d3/packet.json#SC1\n"
        "      - corpus/knowledge/synthesis/worldbible-integration-"
        "contract.md:53-70\n"
        "  - claim_id: CL-C\n"
        "    kind: screening statement\n"
        "    uncertainty:\n"
        "      status: unresolved\n"
        "      basis: \"grounding: A-SCR; open: no real-language sweep "
        "exists; owner: kotodama\"\n"
        "open_questions:\n"
        "  - id: OQ-1\n"
        "    question: \"screening?\"\n"
        "    claims:\n"
        "      - CL-C\n"
    )
    with tempfile.TemporaryDirectory() as tmp:
        packet_path = Path(tmp) / "packet.yml"
        packet_path.write_text(dialect, encoding="utf-8")
        data = read_packet(packet_path)
        claims, open_questions = packet_sections(data)
        if [c["claim_id"] for c in claims] != ["CL-A", "CL-C"]:
            failures.append(f"dialect claims misparsed: {claims}")
        if claims[0]["uncertainty"]["status"] != "supported":
            failures.append("dialect uncertainty.status misparsed")
        if claims[0]["links"] != [
                "examples/culture-d3/packet.json#SC1",
                "corpus/knowledge/synthesis/"
                "worldbible-integration-contract.md:53-70"]:
            failures.append(f"dialect links misparsed: {claims[0]['links']}")
        if (open_questions is None or open_questions[0]["claims"] != ["CL-C"]):
            failures.append(f"dialect open_questions misparsed: "
                            f"{open_questions}")
        routed = validate_uncertainty(claims, open_questions=open_questions)
        if routed:
            failures.append(f"dialect fixture produced findings: {routed}")

    bare = (
        "claims:\n"
        "  -\n"
        "    claim_id: CL-A\n"
        "    uncertainty:\n"
        "      status: partial\n"
        "      basis: \"grounding: A-S02; screening unperformed, museum "
        "record carries its own dating caveat\"\n"
        "open_questions:\n"
        "  -\n"
        "    id: OQ-2\n"
        "    claims:\n"
        "      - CL-A\n"
    )
    with tempfile.TemporaryDirectory() as tmp:
        packet_path = Path(tmp) / "packet-bare.yml"
        packet_path.write_text(bare, encoding="utf-8")
        data = read_packet(packet_path)
        claims, open_questions = packet_sections(data)
        if [c["claim_id"] for c in claims] != ["CL-A"]:
            failures.append(f"bare-dash claims misparsed: {claims}")
        if claims[0]["uncertainty"]["status"] != "partial":
            failures.append("bare-dash uncertainty.status misparsed")
        if open_questions[0]["claims"] != ["CL-A"]:
            failures.append(f"bare-dash open_questions misparsed: "
                            f"{open_questions}")

    if failures:
        for failure in failures:
            print(f"selftest: FAIL {failure}", file=sys.stderr)
        return 1
    print("selftest: 19 checks passed (uncertainty rules, boilerplate, "
          "oq routing, yaml_lines dialect compact+bare)")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate handoff packet v2 claim-ledger uncertainty "
                    "fields (U-* findings).")
    parser.add_argument("--packet", type=Path,
                        help="packet file: JSON or the yaml_lines dialect")
    parser.add_argument("--claims-json", type=Path,
                        help="bare JSON list of claim dicts")
    parser.add_argument("--min-basis-len", type=int,
                        default=DEFAULT_MIN_BASIS_LEN,
                        help=f"minimum basis length "
                             f"(default {DEFAULT_MIN_BASIS_LEN})")
    parser.add_argument("--require-oq", action="store_true",
                        help="flag unresolved claims not referenced by any "
                             "open_questions row (packet mode)")
    parser.add_argument("--json", action="store_true",
                        help="emit findings as one JSON object")
    parser.add_argument("--selftest", action="store_true",
                        help="run embedded positive/negative fixtures")
    args = parser.parse_args(argv)

    if args.selftest:
        return _selftest()
    if bool(args.packet) == bool(args.claims_json):
        parser.error("exactly one of --packet / --claims-json is required")

    try:
        if args.packet:
            data = read_packet(args.packet)
            claims, open_questions = packet_sections(data)
            if not args.require_oq:
                open_questions = None
        else:
            claims = json.loads(args.claims_json.read_text(encoding="utf-8"))
            open_questions = None
    except (OSError, ValueError) as error:
        print(f"{TOOL}: cannot read packet: {error}", file=sys.stderr)
        return 2

    findings = validate_uncertainty(claims, args.min_basis_len,
                                    open_questions)
    if args.json:
        print(json.dumps({"tool": TOOL, "claims": len(claims) if
                          isinstance(claims, list) else 0,
                          "findings": [f.as_row() for f in findings]},
                         ensure_ascii=False, indent=1))
    else:
        for finding in findings:
            row = finding.as_row()
            print(f"{row['code']} [{row['claim_id']}] {row['detail']}")
        print(f"claims={len(claims) if isinstance(claims, list) else 0} "
              f"findings={len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
