#!/usr/bin/env python3
"""d2-typed-labels — typed translated-label/native-form handling for D2 (R8-D02).

One tool, three capabilities, one projection:

  1. **typed labels** — every label a D2 packet carries is typed into exactly
     three kinds: `native-form` (a constructed D2 surface form owned by
     05-lexicon; the only kind that enters a sound/identity test),
     `translated-label` (a reader-facing English rendering; never sound-tested)
     and `borrowed-strata` (a form that entered through a declared loan layer,
     checked as a recipient form plus borrow-ledger checks). The parser is
     R8-D03 §4.2 (`parse_typed_labels`); its loader is R8-D03 §4.1
     (`load_packet_strict`, a closed YAML subset that refuses what it cannot
     parse instead of guessing).
  2. **scoped era/material reconciliation** — R8-D05 §4 (`reconcile_scoped`):
     era labels resolve through declared, scoped rows (`identity`,
     `mapped-confirmed`, `mapped-unconfirmed`, `unmapped`, `conflict`) and
     materials through slot identity, never by label; a `to-verify` row holds
     rather than promotes.
  3. **rank-rule adapter** — R8-D04 §4 (`build_payload`): D2's prose rank rules
     become normalized records carrying `adapt_status` (`executable`,
     `partial`, `cannot-evaluate`) and an `unresolved[]` list, plus the
     gate-facing projection of the rules that can be executed. A
     `cannot-evaluate` rule is never read as a pass.

The integrated output is one deterministic projection document (JSON, sorted
keys, LF): the typed labels, the reconciliation ledger, the normalized rule set
with its conflict triage and quarantine table, the merged finding list under the
design spec's `D2L-*` vocabulary (`reports/round-8/depth/design-spec.md` §6), and
the coverage counts.

For non-D2 families the integration layer selects packet-native rank records
before invoking any D2 fixture machinery. D4 labels cite its own components and
its declared orthography scheme; explicit foreign provenance fails closed.
Unsupported rank properties remain held, and an absent rank leg is explicitly
skipped. Shared D2L-* diagnostics and method references do not import D2 data.

Interface
---------
    python3 tools/d2-typed-labels.py [--packet PATH]        # report to stdout
    python3 tools/d2-typed-labels.py --json                 # one JSON document
    python3 tools/d2-typed-labels.py --emit PATH            # write the projection
    python3 tools/d2-typed-labels.py --check                # byte-compare the projection
    python3 tools/d2-typed-labels.py --selftest             # fixture + control matrix

Exit codes (design-spec §0): 0 = no HOLD/FAIL (notes only), 1 = findings
emitted and the report is still complete, 2 = could-not-evaluate (malformed
input, `P-*` loader code or `D2L-DATA`; stable message, no traceback).
`--check` answers one question — byte-identity — so it exits 0 on an identical
projection, 1 on drift and 2 when nothing could be built; the finding count is
the default report's business, not the byte comparison's.

Two interface proposals met here and this tool reconciles them: the parser shard
(R8-D03 §4.3) asks for `--packet` to print one JSON document with `ok`, `stats`
and `findings`; the design spec fixes the exit-code table. Both hold: `--json`
prints the shard's document shape, while the exit code follows the spec (a
finding is exit 1, a malformed input is exit 2) rather than the shard's
`E-* → 2`.

Calibration: this is a designer audit aid, not a gate and not a canon ruling
(`AGENTS.md`). It is read-only over components, packet and gates; it never
rewrites the packet, so the regenerated `packet.d2.yml` stays byte-identical to
`tools/assemble-d2.py`'s output and the frozen round-3 replay keeps its digests.
A `(to-verify)` row stays `(to-verify)`, an unresolved form slot stays held, and
canon belongs to lore-shokunin.

The original R8 integration lifted four shard payloads — R8-D03 §4.1/§4.2,
R8-D04 §4, R8-D05 §4 — removing the shard process drivers, accepting bare-dash
YAML list items, and treating the declared sacred/taboo registers as native.
The label parser now also accepts family-owned metadata; its default helper
arguments retain the D2 contract. The lower integration layer selects each
family's data, validates ownership, combines findings and owns the CLI.
"""

import argparse
import contextlib
import hashlib
import io
import json
import pathlib
import re
import runpy
import shutil
import subprocess
import sys
import tempfile

# ==========================================================================

# Block 1/4 — strict loader (R8-D03 §4.1), lifted verbatim.

# ==========================================================================

# strict_loader.py — parse the packet subset the gates consume, rejecting
# everything the subset does not cover (report 26 §3 D1-D7). No YAML library,
# no anchors, tags, aliases, multi-document streams or tab indentation: input
# outside the subset is refused with a stable P-* code, never guessed.
import re

FLOW_DEPTH_CAP = 64
_IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")
_FORBIDDEN_AT_START = "&*!"
_INT_RE = re.compile(r"[-+]?[0-9]+$")
_FLOAT_RE = re.compile(r"[-+]?([0-9]+\.[0-9]*|\.[0-9]+)$")
_RAW_TRUE = {"true", "false"}
_RAW_BOOL = {"true", "false", "yes", "no", "on", "off"}


class PacketSyntaxError(Exception):
    def __init__(self, code, line, detail):
        self.code = code
        self.line = line
        self.detail = detail
        super().__init__(f"{code} at line {line}: {detail}")


def _strip_comment(raw):
    out, quote = [], None
    for ch in raw:
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#" and (not out or out[-1] in " \t"):
            break
        else:
            out.append(ch)
    return "".join(out)


def _scan_flow_balance(text, line_no):
    """Reject unbalanced flow collections before any value parsing (D1)."""
    depth, quote, i = 0, None, 0
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
            if depth > FLOW_DEPTH_CAP:
                raise PacketSyntaxError("P-DEPTH-CAP", line_no,
                                        f"flow nesting deeper than {FLOW_DEPTH_CAP}")
        elif ch in "]}":
            depth -= 1
            if depth < 0:
                raise PacketSyntaxError("P-UNTERMINATED-FLOW", line_no,
                                        "closing bracket without opener")
        i += 1
    if quote:
        raise PacketSyntaxError("P-UNTERMINATED-FLOW", line_no, "unterminated quote")
    if depth != 0:
        raise PacketSyntaxError("P-UNTERMINATED-FLOW", line_no,
                                "flow collection is not closed on its line")


def _split_flow(body, line_no, sep=","):
    """Split a flow body on top-level separators; quotes are respected."""
    parts, buf, depth, quote = [], [], 0, None
    for ch in body:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch in "[{":
            depth += 1
            buf.append(ch)
        elif ch in "]}":
            depth -= 1
            buf.append(ch)
        elif ch == sep and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf or parts:
        parts.append("".join(buf))
    return parts


def _find_top_colon(body, line_no):
    depth, quote = 0, None
    for i, ch in enumerate(body):
        if quote:
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == ":" and depth == 0:
            if i + 1 >= len(body) or body[i + 1] in " \t":
                return i
    return -1


def parse_scalar(raw, line_no, bool_coercion=False):
    """Return the authored value with minimal typing; raw text is preserved for
    form-bearing fields. Booleans are only coerced when the caller opts in."""
    s = raw.strip()
    if not s:
        return None
    if s[0] in "\"'":
        if len(s) < 2 or s[-1] != s[0]:
            raise PacketSyntaxError("P-UNTERMINATED-FLOW", line_no, "unterminated string")
        return s[1:-1]
    if s[0] in _FORBIDDEN_AT_START:
        raise PacketSyntaxError("P-ANCHOR-TAG", line_no,
                                "anchor, alias or tag is outside the accepted subset")
    if s.startswith("["):
        if not s.endswith("]"):
            raise PacketSyntaxError("P-UNTERMINATED-FLOW", line_no, "flow sequence not closed")
        body = s[1:-1].strip()
        if not body:
            return []
        return [parse_scalar(p, line_no, bool_coercion)
                for p in _split_flow(body, line_no)]
    if s.startswith("{"):
        if not s.endswith("}"):
            raise PacketSyntaxError("P-UNTERMINATED-FLOW", line_no, "flow mapping not closed")
        body = s[1:-1].strip()
        if not body:
            return {}
        out = {}
        for part in _split_flow(body, line_no):
            ci = _find_top_colon(part, line_no)
            if ci < 0:
                raise PacketSyntaxError("P-UNTERMINATED-FLOW", line_no,
                                        f"flow mapping item {part!r} has no key colon")
            key = part[:ci].strip()
            if key and key[0] in "\"'":
                key = key[1:-1]
            if key in out:
                raise PacketSyntaxError("P-DUPLICATE-KEY", line_no,
                                        f"duplicate flow key {key!r}")
            out[key] = parse_scalar(part[ci + 1:], line_no, bool_coercion)
        return out
    if s in _RAW_TRUE and bool_coercion:
        return s == "true"
    if s in _RAW_BOOL and not bool_coercion:
        return s                      # keep 'no' as the authored text (D4)
    if _INT_RE.match(s):
        return int(s)
    if _FLOAT_RE.match(s):
        return float(s)
    return s


def _content_lines(text):
    lines = []
    for n, raw in enumerate(text.splitlines(), 1):
        if raw.startswith("---") or raw.startswith("..."):
            raise PacketSyntaxError("P-MULTI-DOC", n,
                                    "document markers are not part of the subset")
        if raw.strip() in ("", "---", "..."):
            continue
        if raw[:1] == "\t" or "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise PacketSyntaxError("P-TAB-INDENT", n, "tab indentation is refused")
        indent = len(raw) - len(raw.lstrip(" "))
        body = _strip_comment(raw.strip()).rstrip()
        if not body:
            continue
        lines.append([indent, body, n])
    return lines


def _parse_block(lines, pos, indent):
    if pos >= len(lines):
        return None, pos
    first = lines[pos]
    if first[1] == "-" or first[1].startswith("- "):
        items = []
        while pos < len(lines):
            ind, body, n = lines[pos]
            if ind != indent or not (body == "-" or body.startswith("- ")):
                break
            item = body[2:].strip()
            _scan_flow_balance(item, n)
            if item == "":
                value, pos = _parse_block(lines, pos + 1, _next_indent(lines, pos + 1, indent))
                items.append(value)
                continue
            ci = _find_top_colon(item, n)
            if ci >= 0:
                entry = {}
                key = item[:ci].strip()
                rest = item[ci + 1:].strip()
                if not rest:
                    value, pos = _parse_block(lines, pos + 1, _next_indent(lines, pos + 1, indent))
                    entry[key] = value
                else:
                    entry[key] = parse_scalar(rest, n)
                    pos += 1
                    while pos < len(lines) and lines[pos][0] > indent:
                        sub_ind, sub_body, sub_n = lines[pos]
                        ci2 = _find_top_colon(sub_body, sub_n)
                        if ci2 < 0 or sub_body.startswith("- "):
                            break
                        skey = sub_body[:ci2].strip()
                        srest = sub_body[ci2 + 1:].strip()
                        if not srest:
                            value, pos = _parse_block(lines, pos + 1, _next_indent(lines, pos + 1, sub_ind))
                            entry[skey] = value
                        else:
                            entry[skey] = parse_scalar(srest, sub_n)
                            pos += 1
                items.append(entry)
            else:
                items.append(parse_scalar(item, n))
                pos += 1
        return items, pos
    mapping = {}
    while pos < len(lines):
        ind, body, n = lines[pos]
        if ind != indent or body.startswith("- "):
            break
        ci = _find_top_colon(body, n)
        if ci < 0:
            raise PacketSyntaxError("P-UNTERMINATED-FLOW", n, f"content {body!r} is not a mapping line")
        key = body[:ci].strip()
        if key and key[0] in "\"'":
            key = key[1:-1]
        if not key:
            raise PacketSyntaxError("P-UNTERMINATED-FLOW", n, "empty mapping key")
        if key in mapping:
            raise PacketSyntaxError("P-DUPLICATE-KEY", n, f"duplicate key {key!r}")
        rest = body[ci + 1:].strip()
        _scan_flow_balance(rest, n)
        if rest:
            mapping[key] = parse_scalar(rest, n)
            pos += 1
        else:
            value, pos = _parse_block(lines, pos + 1, _next_indent(lines, pos + 1, indent))
            mapping[key] = value
    return mapping, pos


def _next_indent(lines, pos, current):
    if pos < len(lines) and lines[pos][0] > current:
        return lines[pos][0]
    return current + 1


def load_packet_strict(text, bool_coercion=False):
    """Parse a packet string into plain Python objects.

    Returns {"packet": obj|None, "findings": [ {code, line, detail}, ... ]}.
    `packet` is None exactly when an E-class syntax finding fired; the caller
    exits 2 in that case (gates' could-not-evaluate contract).
    """
    findings = []
    try:
        lines = _content_lines(text)
        if not lines:
            findings.append({"code": "P-EMPTY", "line": 0, "detail": "no content lines"})
            return {"packet": None, "findings": findings}
        packet, pos = _parse_block(lines, 0, lines[0][0])
        if pos != len(lines):
            _, body, n = lines[pos]
            raise PacketSyntaxError("P-UNTERMINATED-FLOW", n, f"unconsumed content {body!r}")
    except PacketSyntaxError as exc:
        findings.append({"code": exc.code, "line": exc.line, "detail": exc.detail})
        return {"packet": None, "findings": findings}
    if not isinstance(packet, dict):
        findings.append({"code": "P-ROOT", "line": lines[0][2], "detail": "root is not a mapping"})
        return {"packet": None, "findings": findings}
    return {"packet": packet, "findings": findings}


def load_packet_file(path, bool_coercion=False):
    """Read UTF-8 with an explicit failure (D7), then parse."""
    try:
        text = pathlib.Path(path).read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return {"packet": None,
                "findings": [{"code": "P-ENCODING", "line": 0, "detail": str(exc)}]}
    except OSError as exc:
        return {"packet": None,
                "findings": [{"code": "P-IO", "line": 0, "detail": str(exc)}]}
    return load_packet_strict(text, bool_coercion)




# ==========================================================================

# Block 2/4 — label parser (R8-D03 §4.2), with family-owned metadata.

# ==========================================================================

# label_parser.py — spec-conformant typed-label projection and validation for D2
# packets (reports/round-8/depth/design-spec.md §1). Pure functions over
# already-loaded packet objects; no I/O, no YAML. Finding ids are the spec's
# §6 classes (D2L-*); the loader's P-* codes map to D2L-DATA at the CLI.
import re
import unicodedata

KINDS = ("translated-label", "native-form", "borrowed-strata")
SOUND_KINDS = ("native-form", "borrowed-strata")
STATUSES = ("supplied", "to-verify", "absent")
REPRESENTATIONS = ("english-gloss", "editorial-romanization", "native-spelling")
CONTRACT_ERAS = ("E0", "E1", "E2", "E3")
ROUTE_KINDS = ("local", "import", "reuse", "alternative", "excluded")
ROUTE_STAGES = ("fiber", "yarn", "cloth", "garment", "dye", "trim")
EFFECTS = ("prohibit", "permit", "obligate", "exempt")
ADAPT_STATUSES = ("executable", "partial", "cannot-evaluate")
FINDING_CLASSES = ("D2L-DATA", "D2L-FORM-UNRESOLVED", "D2L-NATIVE", "D2L-BORROW",
                   "D2L-ERA", "D2L-MATERIAL", "D2L-RANK", "D2L-SCOPE")
D2L_DATA = "D2L-DATA"
D2L_FORM = "D2L-FORM-UNRESOLVED"
D2L_BORROW = "D2L-BORROW"
D2L_NATIVE = "D2L-NATIVE"
D2L_ERA = "D2L-ERA"
D2L_MATERIAL = "D2L-MATERIAL"
D2L_SCOPE = "D2L-SCOPE"

# spec §4.2 A3 — the declared sign_axis table; an absent row is cannot-evaluate,
# never a prose inference
SIGN_AXIS_TABLE = (
    # (sign_axis head, distinguishing tail, kind, value source, slot_ref)
    ("fiber/material", "grade", "grade", "grade_ladder", "MAT-02"),
    ("fiber/material", "imported cloth", "material", "lowland-plant-cloth", "CMAT-06"),
    ("fiber/material", "fossil law", "material", "plant-thread", "CMAT-06"),
    ("trim/embellishment", "", "trim", "hem-cords", "GAR-03"),
    ("garment-type/badge", "", "badge", "mast-sash", "GAR-05"),
    ("rite/lifecycle", "", "rite-state", "mourning finish", "GAR-07"),
    ("quantity/occasion", "", "occasion-exemption", "wedding day", None),
    ("regulated person", "", "wearer-category", "treaty stranger", "GAR-06"),
    ("claim", "", "act", "hem-knot", "GAR-05"),
    ("touch", "", "act", "handshake", "GAR-03"),
)

_SLOT_RE = re.compile(r"LEX-GAR-[0-9]{2}")
_LABEL_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*(-[A-Za-z0-9]+)*$")
_TEMPLATE_FIELD = re.compile(r"\{([^{}]*)\}")
_RISKY_PATTERN = re.compile(r"[+*]\s*[)\]|]|[+*]\)|[+*][+*?*]")


def _is_str(v):
    return isinstance(v, str)


def _nfc(v):
    return unicodedata.normalize("NFC", v)


def _has_combining(v):
    return any(unicodedata.combining(ch) for ch in unicodedata.normalize("NFD", v))


def _inventory(packet):
    phon = packet.get("phonology") or {}
    if not isinstance(phon, dict):
        return None, None
    cons = phon.get("consonants")
    vows = phon.get("vowels")
    return (set(cons) if isinstance(cons, list) else set(),
            set(vows) if isinstance(vows, list) else set())


def _layers(packet):
    out = {}
    for layer in packet.get("layers") or []:
        if isinstance(layer, dict) and _is_str(layer.get("name")):
            out[layer["name"]] = layer
    return out


def _source(component, record, field, line):
    return {"component": component, "record": record, "field": field, "line": line}


# ---------------------------------------------------------------------------
# projection: packet records -> spec §1.2 label records
# ---------------------------------------------------------------------------

def _costume_label(entry, index, owner="11-costumes", component="11-costumes.yml"):
    garment = entry.get("garment")
    if not _is_str(garment) or not garment.strip():
        return None
    slot = entry.get("form_slot")
    match = _SLOT_RE.search(slot) if _is_str(slot) else None
    slot_id = match.group(0) if match else None
    return {
        "id": entry.get("id", f"costume#{index + 1}"),
        "owner": owner,
        "label_id": slot_id,
        "kind": "translated-label",
        "text": garment,
        "script": "Latn",
        "representation": "english-gloss",
        "scheme": None,
        "status": "to-verify",
        "era_ids": [entry["era"]] if _is_str(entry.get("era")) else [],
        "register": None,
        "evidence": entry.get("evidence") or "to-verify",
        "source": _source(component, entry.get("id"), "garment", None),
        "issues": [{"field": "scheme", "reason": "english-gloss needs no romanization scheme"}],
    }


def _form_slot_label(slot, owner, record_id, component=None):
    return {
        "id": record_id,
        "owner": owner,
        "label_id": slot.get("id"),
        "kind": "translated-label",
        "text": None,                   # the slot carries a gloss, not a form
        "script": None,
        "representation": None,
        "scheme": None,
        "status": "to-verify",
        "era_ids": [],
        "register": slot.get("register"),
        "evidence": "to-verify",
        "source": _source(component or owner, record_id, "form_slot", None),
        "issues": [{"field": "text", "reason": "form slot unfilled; the requirement is a gloss, not a form"},
                   {"field": "script", "reason": "no form, so no script applies"},
                   {"field": "representation", "reason": "no form, so no representation applies"},
                   {"field": "scheme", "reason": "no form, so no scheme applies"}],
        "gloss": slot.get("gloss"),
    }


def _lexicon_label(entry, index, layers, owner="05-lexicon",
                   component="05-lexicon.yml", scheme="d2-roman"):
    term = entry.get("term")
    if not _is_str(term) or not term.strip():
        return None
    layer = entry.get("layer")
    layer_name = entry.get("loan_layer") if _is_str(entry.get("loan_layer")) else layer
    layer_rec = layers.get(layer_name) if _is_str(layer_name) else None
    base = {
        "id": entry.get("id", f"lex#{index + 1}"),
        "owner": owner,
        "label_id": None,
        "kind": "native-form",
        "text": term,
        "script": "Latn",
        "representation": "editorial-romanization",
        "scheme": scheme,
        "status": "supplied",
        "era_ids": [entry["stage"]] if _is_str(entry.get("stage")) else [],
        "register": entry.get("field"),
        "evidence": entry.get("evidence") or "design-choice",
        "source": _source(component, entry.get("id"), "term", None),
        "issues": [],
        "layer": layer,                 # B6: preserved verbatim, route is a different field
        "route": entry.get("route"),
    }
    if _is_str(layer) and layer not in ("native", "substrate", "unknown",
                                     "sacred", "taboo"):  # register strata of the native language
        base["kind"] = "borrowed-strata"
        base["borrow"] = {
            "layer_ref": layer_name,
            "donor": {"immediate": (layer_rec or {}).get("donor_stage") or (layer_rec or {}).get("donor"),
                      "ultimate": None, "carrier": None},
            "donor_form": entry.get("donor_form"),
            "substitutions": (layer_rec or {}).get("substitutions"),
            "entry_stage": entry.get("stage"),
            "referent_available_from": (layer_rec or {}).get("referent_available_from"),
            "channel": (layer_rec or {}).get("channel"),
            "alternative_checks": [],
        }
    return base


def _name_label(entry, index, owner="13-naming", component="13-naming.yml",
                scheme="d2-roman"):
    name = entry.get("name")
    if not _is_str(name) or not name.strip():
        return None
    return {
        "id": entry.get("id", f"name#{index + 1}"),
        "owner": owner,
        "label_id": None,
        "kind": "native-form",
        "text": name,
        "script": "Latn",
        "representation": "editorial-romanization",
        "scheme": scheme,
        "status": "supplied",
        "era_ids": [entry["era"]] if _is_str(entry.get("era")) else [],
        "register": None,
        "evidence": entry.get("evidence") or "design-choice",
        "source": _source(component, entry.get("id"), "name", None),
        "issues": [],
        "layer": "native",
    }


def family_label_metadata(packet, family="d2", packet_path=None):
    if family == "d2":
        return {"costumes": ("11-costumes", "11-costumes.yml"),
                "form_slots": ("11-costumes", "11-costumes"),
                "lexicon": ("05-lexicon", "05-lexicon.yml"),
                "names": ("13-naming", "13-naming.yml"), "scheme": "d2-roman"}
    orthography = packet.get("orthography") or {}
    scheme = orthography.get("scheme") if isinstance(orthography, dict) else None
    if not isinstance(scheme, str) or not scheme.strip():
        raise Malformed("P-FAMILY-SOURCE: %s declares no orthography.scheme" % family)
    if family == "d4":
        base = "examples/culture-d4/components/"
        return {"costumes": ("09-costumes", base + "09-costumes.yml"),
                "form_slots": ("09-costumes", base + "09-costumes.yml"),
                "lexicon": ("04-lexicon", base + "04-lexicon.yml"),
                "names": ("05-naming", base + "05-naming.yml"), "scheme": scheme}
    source = shown_path(packet_path) if packet_path else "packet"
    return {block: (block, source) for block in
            ("costumes", "form_slots", "lexicon", "names")} | {"scheme": scheme}


def project_labels(packet, family="d2", packet_path=None):
    """Project labels with family-owned metadata; explicit rows are never rewritten."""
    metadata = family_label_metadata(packet, family, packet_path)
    labels = []
    for entry in packet.get("typed_labels") or []:
        if isinstance(entry, dict):
            labels.append(dict(entry))
    layers = _layers(packet)
    for index, entry in enumerate(packet.get("costumes") or []):
        if not isinstance(entry, dict):
            continue
        label = _costume_label(entry, index, *metadata["costumes"])
        if label:
            labels.append(label)
    for slot in packet.get("form_slots") or []:
        if isinstance(slot, dict) and _is_str(slot.get("id")):
            owner, component = metadata["form_slots"]
            labels.append(_form_slot_label(slot, owner, slot["id"], component))
    for index, entry in enumerate(packet.get("lexicon") or []):
        if not isinstance(entry, dict):
            continue
        label = _lexicon_label(entry, index, layers, *metadata["lexicon"], metadata["scheme"])
        if label:
            labels.append(label)
    for index, entry in enumerate(packet.get("names") or []):
        if not isinstance(entry, dict):
            continue
        label = _name_label(entry, index, *metadata["names"], metadata["scheme"])
        if label:
            labels.append(label)
    return labels


# ---------------------------------------------------------------------------
# validation: spec §1.2 L1-L5, §1.3 R1-R6, §1.4 B1-B6
# ---------------------------------------------------------------------------

def _fail(findings, code, where, detail, hold=False):
    findings.append({"code": code, "where": where, "detail": detail,
                     "kind": "hold" if hold else "fail"})


def apply_substitutions(substitutions, donor_form):
    """Apply a layer's substitutions to a donor form: longest key first, one
    left-to-right pass, substituted output is never re-scanned (B3)."""
    if not isinstance(substitutions, dict) or not _is_str(donor_form):
        return None
    keys = sorted((k for k in substitutions if _is_str(k) and k), key=len, reverse=True)
    out, i = [], 0
    while i < len(donor_form):
        for key in keys:
            if donor_form.startswith(key, i):
                out.append(str(substitutions[key]))
                i += len(key)
                break
        else:
            out.append(donor_form[i])
            i += 1
    return "".join(out)


def check_sound_form(label, cons, vows, findings):
    """R1/R2/NATIVE: a supplied sound form is checked against the declared
    profile. The profile here is the packet's own inventory; D02 may delegate
    to the naming gate's tokenizer without changing the finding id."""
    if label.get("kind") not in SOUND_KINDS or label.get("status") != "supplied":
        return
    text = label.get("text")
    where = label.get("id")
    if not _is_str(text) or not text.strip():
        _fail(findings, D2L_DATA, where, "supplied sound form has no text")
        return
    text = _nfc(text)
    if cons is None:
        return
    allowed = cons | vows | {" ", "-", "\u00b7"}
    bad = sorted({ch for ch in text if ch not in allowed})
    if bad:
        _fail(findings, D2L_NATIVE, where,
              f"supplied form {text!r} carries symbols outside the declared inventory: {bad}")
    if _has_combining(text) and not (label.get("script") and label.get("representation")):
        _fail(findings, D2L_DATA, where,
              "diacritic-bearing form needs script and representation")


def check_borrow(label, layers, findings):
    """B1-B6 for a supplied borrowed-strata label."""
    if label.get("kind") != "borrowed-strata" or label.get("status") != "supplied":
        return
    where = label.get("id")
    borrow = label.get("borrow")
    if not isinstance(borrow, dict):
        _fail(findings, D2L_BORROW, where, "borrowed-strata label carries no borrow block")
        return
    layer_ref = borrow.get("layer_ref")
    layer = layers.get(layer_ref) if _is_str(layer_ref) else None
    if layer is None:
        _fail(findings, D2L_BORROW, where, f"layer_ref {layer_ref!r} does not resolve to a declared layer")
        return
    donor = borrow.get("donor")
    if not isinstance(donor, dict) or not (donor.get("immediate") or donor.get("ultimate")):
        _fail(findings, D2L_BORROW, where,
              "donor must separate immediate donor, ultimate etymon and carrier; immediate is unset",
              hold=True)
    donor_form = borrow.get("donor_form")
    subs = borrow.get("substitutions")
    if not _is_str(donor_form) or not donor_form.strip():
        _fail(findings, D2L_BORROW, where, "borrowed form names no donor_form", hold=True)
    elif isinstance(subs, dict) and subs:
        derived = apply_substitutions(subs, donor_form)
        if derived != _nfc(label.get("text") or ""):
            _fail(findings, D2L_BORROW, where,
                  f"substitutions derive {derived!r} from donor {donor_form!r}, not {label.get('text')!r}")
    entry_stage = borrow.get("entry_stage")
    available = borrow.get("referent_available_from")
    if _is_str(entry_stage) and _is_str(available) and entry_stage < available:
        _fail(findings, D2L_BORROW, where,
              f"entry_stage {entry_stage} precedes referent_available_from {available}")
    layer_subs = layer.get("substitutions")
    if isinstance(layer_subs, dict) and isinstance(subs, dict):
        for key, value in subs.items():
            if key in layer_subs and layer_subs[key] != value:
                _fail(findings, D2L_BORROW, where,
                      f"substitution {key}->{value} contradicts layer {layer_ref!r}'s declared {key}->{layer_subs[key]}")


def validate_labels(labels, packet, strict=False):
    """L1-L5, R1-R6, B1-B6 over projected labels. Returns (findings, exit_code)."""
    findings = []
    cons, vows = _inventory(packet)
    layers = _layers(packet)
    seen = {}
    supplied_by_key = {}
    for label in labels:
        where = label.get("id", "<no id>")
        for field in ("id", "owner", "kind", "status"):
            if not _is_str(label.get(field)) or not label.get(field):
                _fail(findings, D2L_DATA, where, f"required field {field!r} is missing")
        if not _is_str(label.get("id")) or not _LABEL_ID_RE.match(str(label.get("id"))):
            _fail(findings, D2L_DATA, where, f"id {label.get('id')!r} is not a stable record id")
        if label.get("id") in seen:
            _fail(findings, D2L_DATA, where, "duplicate label record id")
        seen[label.get("id")] = True
        if label.get("kind") not in KINDS:
            _fail(findings, D2L_DATA, where, f"kind {label.get('kind')!r} is not one of {KINDS}")
            continue
        status = label.get("status")
        if status not in STATUSES:
            _fail(findings, D2L_DATA, where, f"status {status!r} is not one of {STATUSES}")
        if status == "supplied" and not (_is_str(label.get("text")) and label["text"].strip()):
            _fail(findings, D2L_DATA, where, "status supplied requires text")
        if _is_str(label.get("text")) and label["text"].strip() and not label.get("script"):
            _fail(findings, D2L_DATA, where, "supplied text requires a script")
        if label.get("representation") not in (None,) + REPRESENTATIONS:
            _fail(findings, D2L_DATA, where,
                  f"representation {label.get('representation')!r} is not one of {REPRESENTATIONS}")
        if label.get("owner") in ("11-costumes", "09-costumes", "costumes", "form_slots") and not label.get("label_id"):
            _fail(findings, D2L_DATA, where, "costume label carries no label_id for its form slot")
        for field in ("text", "script", "representation", "scheme"):
            if label.get(field) is None:
                issues = label.get("issues") or []
                if not any(isinstance(i, dict) and i.get("field") == field for i in issues):
                    _fail(findings, D2L_DATA, where,
                          f"null {field} carries no field-specific reason in issues")
        for era in label.get("era_ids") or []:
            if era not in CONTRACT_ERAS:
                _fail(findings, D2L_SCOPE, where,
                      f"era id {era!r} is not a contract tag {CONTRACT_ERAS}; alias it explicitly")
        if label.get("kind") in SOUND_KINDS and status == "supplied":
            key = (label.get("owner"), label.get("label_id") or label.get("id"))
            supplied_by_key.setdefault(key, []).append(label)
    for key, group in supplied_by_key.items():
        if len(group) > 1:
            _fail(findings, D2L_DATA, group[0].get("id"),
                  f"two supplied sound forms on one record ({key[0]} {key[1]}): identity collision")
    supplied_label_ids = {label.get("label_id") for label in labels
                          if label.get("kind") in SOUND_KINDS and label.get("status") == "supplied"}
    for label in labels:
        if label.get("kind") != "translated-label":
            continue
        if label.get("compare_only"):
            _fail(findings, D2L_SCOPE, label.get("id"),
                  "compare_only is not a licensed exemption for typed labels")
        label_id = label.get("label_id")
        if label_id and label_id not in supplied_label_ids:
            _fail(findings, D2L_FORM, label.get("id"),
                  f"label_id {label_id} has no supplied native/borrowed form", hold=True)
        elif not label_id and not (label.get("gloss") or "").strip():
            _fail(findings, D2L_FORM, label.get("id"),
                  "translated label with no supplied sound form and no label_id", hold=True)
    for label in labels:
        if label.get("kind") != "translated-label":
            continue
        owner = label.get("owner")
        label_id = label.get("label_id") or label.get("id")
        for sound in labels:
            if sound.get("kind") not in SOUND_KINDS or sound.get("status") != "supplied":
                continue
            if sound.get("owner") == owner and (sound.get("label_id") or sound.get("id")) == label_id:
                check_sound_form(sound, cons, vows, findings)  # R4: native bytes govern
    for label in labels:
        check_sound_form(label, cons, vows, findings)
        check_borrow(label, layers, findings)
    fails = [f for f in findings if f["kind"] == "fail"]
    holds = [f for f in findings if f["kind"] == "hold"]
    exit_code = 2 if fails else (1 if holds else 0)
    return findings, exit_code


def parse_typed_labels(packet, strict=False, family="d2", packet_path=None):
    """Top-level entry: project, validate, return a JSON-serializable result."""
    if not isinstance(packet, dict):
        return {"exit_code": 2, "ok": False, "labels": [],
                "findings": [{"code": D2L_DATA, "where": "<root>", "detail": "packet is not a mapping", "kind": "fail"}],
                "stats": {"fail": 1, "hold": 0, "labels": 0}}
    labels = project_labels(packet, family, packet_path)
    if family != "d2":
        validate_family_labels(packet_path, packet, labels, family)
    findings, exit_code = validate_labels(labels, packet, strict)
    return {
        "exit_code": exit_code,
        "ok": exit_code == 0,
        "labels": labels,
        "findings": findings,
        "stats": {"fail": sum(1 for f in findings if f["kind"] == "fail"),
                  "hold": sum(1 for f in findings if f["kind"] == "hold"),
                  "labels": len(labels)},
    }


# ---------------------------------------------------------------------------
# scoped era reconciliation (spec §2.2) — used by the era/material shard
# ---------------------------------------------------------------------------

def reconcile_era(source_label, era_aliases):
    """Return one verdict for a source label: identity, mapped-confirmed,
    mapped-unconfirmed, unmapped or conflict (spec §2.2)."""
    if source_label in CONTRACT_ERAS:
        return {"verdict": "identity", "tag": source_label, "row": None}
    rows = [row for row in (era_aliases or [])
            if isinstance(row, dict) and row.get("source") == source_label]
    tags = {row.get("tag") for row in rows if row.get("tag")}
    if len(tags) > 1:
        return {"verdict": "conflict", "tag": None, "row": None,
                "detail": f"two alias rows map {source_label!r} to different tags"}
    if not rows:
        return {"verdict": "unmapped", "tag": None, "row": None}
    row = rows[0]
    verdict = "mapped-confirmed" if row.get("status") == "confirmed" else "mapped-unconfirmed"
    return {"verdict": verdict, "tag": row.get("tag"), "row": row.get("id")}


# ---------------------------------------------------------------------------
# parse-side hooks for the rank-rule adapter (spec §4; D04 owns execution)
# ---------------------------------------------------------------------------

def check_rank_rule_shape(rule):
    """A2/A3 parse-side validation of a normalized rank-rule record."""
    problems = []
    if not _is_str(rule.get("id")):
        problems.append("rule id missing")
    if rule.get("effect") not in EFFECTS:
        problems.append(f"effect {rule.get('effect')!r} is not one of {EFFECTS}")
    prop = rule.get("property")
    if not isinstance(prop, dict) or not _is_str(prop.get("kind")):
        problems.append("property.kind missing")
    if rule.get("adapt_status") not in ADAPT_STATUSES:
        problems.append(f"adapt_status {rule.get('adapt_status')!r} is not one of {ADAPT_STATUSES}")
    if rule.get("eras") and not isinstance(rule.get("era_aliases_applied"), dict):
        problems.append("eras present without era_aliases_applied (A1)")
    return problems


def sign_axis_lookup(sign_axis):
    """A3: the declared table; an absent row is cannot-evaluate, never prose."""
    if not _is_str(sign_axis):
        return None
    for head, tail, kind, value, slot_ref in SIGN_AXIS_TABLE:
        if sign_axis.startswith(head) and (not tail or tail in sign_axis):
            return {"kind": kind, "value_source": value, "slot_ref": slot_ref}
    return None


def screen_pattern(pattern):
    """D8 screen for any packet-controlled regex before it is compiled."""
    if not _is_str(pattern) or _RISKY_PATTERN.search(pattern):
        return "E-LABEL-PATTERN-RISK"
    try:
        re.compile(pattern)
    except re.error:
        return "E-LABEL-PATTERN-RISK"
    return None


def check_template(template, allowed_fields):
    """D9 screen for packet-controlled str.format templates."""
    if not _is_str(template):
        return "E-LABEL-TEMPLATE"
    for field in _TEMPLATE_FIELD.findall(template):
        name = field.split("!")[0].split(":")[0].strip()
        if not name or "." in name or "[" in name or name not in allowed_fields:
            return "E-LABEL-TEMPLATE"
    return None

# ==========================================================================

# Block 3/4 — rank-rule adapter (R8-D04 §4), lifted verbatim except the

# trailing sys.exit(selftest()), removed so this CLI owns the exit.

# ==========================================================================

import json, re, hashlib

class Malformed(ValueError):
    pass

def key(text):
    return str(text).strip().casefold()

C12 = "examples/culture-d2/components/12-rank-rules.yml:"

RANK_TOKENS = {
    "lineage-head":     {"deg": "DEG-1", "wi": "WI-1", "aliases": ["lineage head"]},
    "wind-speaker":     {"deg": "DEG-2", "wi": None,   "aliases": ["wind-speaker", "wind-speakers", "wind speaker"]},
    "herd-master":      {"deg": "DEG-3", "wi": "WI-3", "aliases": ["herd-master", "registered herd-master", "caravan-registered herd-master"]},
    "herder-household": {"deg": "DEG-4", "wi": None,   "aliases": ["herder household", "herder households"]},
    "shelter-kin":      {"deg": "DEG-5", "wi": None,   "aliases": ["shelter-kin", "attached client"]},
    "fair-stranger":    {"deg": "DEG-6", "wi": "WI-5", "aliases": ["fair-stranger", "treaty stranger", "fair stranger"]},
    "spouse":           {"deg": "DEG-7", "wi": None,   "aliases": ["spouse", "spouse-of-household"]},
    "vanguard-herder":  {"deg": None,    "wi": "WI-2", "aliases": ["vanguard herder"], "slot_unresolved": True},
    "mast-bearer":      {"deg": None,    "wi": "WI-4", "aliases": ["wind-standard bearer", "mast-sash bearer"]},
    "mourner":          {"deg": None,    "wi": "WI-6", "aliases": ["mourner", "household of the dead"]},
    "bale-keeper":      {"deg": None,    "wi": "WI-7", "aliases": ["bale keeper", "caravan hands", "caravan hand"]},
}
WI_MARK = re.compile(r"\bWI-(\d)\b")
DEG_MARK = re.compile(r"\bDEG-(\d+)\b")
RITE_TOKENS = {
    "mourning year": ["mourning year", "mourning"],
    "wedding day": ["wedding day", "day of her wedding"],
    "the crossing": ["crossing", "ascent and descent"],
    "the caravan fair": ["caravan fair", "treaty days"],
    "storm law": ["storm law"],
    "the bale audit": ["bale audit"],
}
GATE_PROPERTY_KINDS = frozenset((
    "material", "fiber", "cloth", "fabric", "textile", "dye", "dyestuff",
    "garment", "robe", "clothing", "trim", "closure", "fastening", "badge",
    "insignia", "placement", "hue", "color", "colour"))
NON_PROJECTABLE_KINDS = frozenset(("grade", "rite-state", "occasion-exemption", "wearer-category", "act"))
GATE_KIND_MAP = {"material": "material", "trim": "trim", "badge": "badge", "dye": "dye"}
GATE_VALUE_MAP = {
    ("material", "lowland-plant-cloth"): "lowland plant-thread cloth",
    ("material", "plant-thread"): "lowland plant-thread cloth",
    ("trim", "hem-cords"): "hem-cord",
    ("badge", "mast-sash"): "mast-sash",
}
GATE_EFFECT_MAP = {"prohibit": "prohibit", "permit": "permit", "obligate": "require", "exempt": None}

def wi_by_id(wid):
    return next((t for t, m in RANK_TOKENS.items() if m.get("wi") == wid), None)

def deg_by_id(did):
    return next((t for t, m in RANK_TOKENS.items() if m.get("deg") == did), None)

def rank_tokens(text):
    out, text = [], str(text or "")
    for m in WI_MARK.findall(text):
        tok = wi_by_id("WI-" + m)
        if tok and tok not in out:
            out.append(tok)
    for m in DEG_MARK.findall(text):
        tok = deg_by_id("DEG-" + m)
        if tok and tok not in out:
            out.append(tok)
    low = key(text)
    for tok, meta in RANK_TOKENS.items():
        if tok not in out and any(a in low for a in meta["aliases"]):
            out.append(tok)
    return sorted(out)

def normalize_rite(text):
    low = key(text)
    for tok, pats in RITE_TOKENS.items():
        if any(p in low for p in pats):
            return tok
    return None

RANK_RESOLUTIONS = {
    "GAR-01": {"primary": "lineage-head", "secondary": ["herder-household"],
               "reason": "WI-1 lineage head speaks the grade; the coat is 'any adult of a pasture-holding lineage'",
               "cite": "examples/culture-d2/packet.d2.yml:1852"},
    "GAR-06": {"primary": "fair-stranger", "secondary": ["herd-master"],
               "reason": "WI-5 is the index marker; herd-master is the gift reading ('by gift, a registered herd-master may wear one')",
               "cite": "examples/culture-d2/packet.d2.yml:2007"},
    "GAR-08": {"primary": "bale-keeper", "secondary": ["herder-household"],
               "reason": "WI-7 bale keeper; the coil is worn by the man who counts bales",
               "cite": "examples/culture-d2/packet.d2.yml:2056"},
}

def resolve_costume_rank(cos):
    cid = cos.get("id") or "?"
    toks = rank_tokens(cos.get("wearer_rank"))
    if cid in RANK_RESOLUTIONS:
        return RANK_RESOLUTIONS[cid]["primary"], "resolved-by-declaration", RANK_RESOLUTIONS[cid]
    if len(toks) == 1:
        return toks[0], "resolved", None
    if not toks:
        return None, "unresolved", None
    return None, "ambiguous", {"candidates": toks}

def N(rid, effect, kind, value, slot_ref, eras, era_history_raw, wearer_ranks, exempt_ranks,
      authority, jurisdiction_raw, places, bands, rites, garment_refs, enforcement,
      adapt_status, unresolved, line, **extra):
    rec = {"id": rid, "authority": authority,
           "jurisdiction": {"raw": jurisdiction_raw, "places": list(places), "bands": list(bands)},
           "effect": effect, "property": {"kind": kind, "value": value, "slot_ref": slot_ref},
           "wearer_ranks": list(wearer_ranks), "exempt_ranks": list(exempt_ranks),
           "eras": list(eras), "era_history_raw": era_history_raw, "rites": list(rites),
           "garment_refs": list(garment_refs), "enforcement": enforcement,
           "adapt_status": adapt_status, "unresolved": list(unresolved),
           "source": {"component": "12-rank-rules.yml", "record_id": rid, "line": line}}
    rec.update(extra)
    return rec

def ENF(mechanism, assay, reality, sanction):
    return {"mechanism": mechanism, "assay": assay, "reality": reality, "sanction": sanction}

NORMALIZED = [
 N("WR-01", "prohibit", "grade", "G1-G3 felt-day ladder", "MAT-02", ["E0", "E1", "E2"],
   "E0 (knot only) -> E1 (renewed in script) -> E2 (grade floors frozen, prices left to the fair)",
   ["herd-master", "lineage-head"], [], "Valley Moot statute; oldest cord in the archive",
   "all circuits and all altitude bands", [], [], [], ["GAR-01", "GAR-02", "GAR-03"],
   ENF("winter moot cord check", "felt-days stamped at the bale seal-knot",
       "obeyed in the valley where the cord check runs; above the snow-line a household wears one grade up all summer and is not prosecuted",
       "knot cut, the coat's hem to the informing household, salt fine"),
   "partial", ["prose-only span: no felt-day-to-grade thresholds exist (RR-05)"], 199),
 N("WR-02", "prohibit", "material", "lowland-plant-cloth", "CMAT-06", ["E1", "E2"],
   "E1 onward (the treaty is the script's first D2 use)",
   ["herd-master"], [], "caravan treaty ratified at the winter moot",
   "valley fairgrounds and valley road; void at transit and high pasture",
   ["fairgrounds", "valley-road"], [], ["the caravan fair"], ["GAR-04", "GAR-06"],
   ENF("fair court register", "the fair court reads the caravan register against the coat",
       "the fair court prosecutes strangers and the visibly overdressed, and almost never a registered herd-master's spouse",
       "forfeiture of the coat at the fair gate, half the coat's hem-value to whoever sues"),
   "partial", ["the sell-line is undefined, so the upland scope is undecidable (RR-02)"], 212),
 N("WR-03", "prohibit", "trim", "hem-cords", "GAR-03", ["E0", "E1", "E2"], "E0 to E2",
   [], [], "Valley Moot statute", "all bands; the check itself happens only in the winter valley",
   [], [], ["the crossing"], ["GAR-03"],
   ENF("moot cord check", "count of cords against the cord archive",
       "over-fringed coats at the fair, cord-twist forgeries, a summer trade in second-hand fringes",
       "the over-count cords are cut at the moot in public; a forger's twist cord pays a bale"),
   "partial", ["cord count versus recorded ascents is not expressible",
               "costume rows carry hem-cords in prose, not in closures/trims"], 225),
 N("WR-04", "prohibit", "badge", "mast-sash", "GAR-05", ["E0", "E1", "E2"], "E0 to E2",
   ["mast-bearer"], [], "lineage head with moot confirmation",
   "all bands, because the mast travels with the herds", [], [], [], ["GAR-05"],
   ENF("moot issuance and recall", "weights tied into the end-cords, counted against the archive",
       "a forged sash is the only D2 dress crime that can end a family",
       "sash forfeited and burned; moot voice lost for a year"),
   "partial", ["the annual issuance/revocation interval is not expressible",
               "GAR-05 declares no badge field, so the gate's R-03 cannot fire"], 238),
 N("WR-05", "prohibit", "rite-state", "mourning finish", "GAR-07", ["E0", "E1", "E2"], "E0 to E2",
   ["mourner"], [], "Valley Moot statute with the wind-speakers' recitation",
   "all bands; suspended during storm law's first day (see TR-05)", [], [], ["mourning year"], ["GAR-07", "GAR-04"],
   ENF("moot comment by the dead-roll reciter", "the shaggy finish is visible; cut-back cords checked at the next moot",
       "observed hard - mourning is the one rule that is self-enforcing",
       "none needed; the sanction is social"),
   "cannot-evaluate", ["rite-state is not a gate-modelled property kind",
                       "the suspension interval (storm law's first day) disagrees with TR-05 (while storm law holds)"], 251),
 N("WR-06", "exempt", "occasion-exemption", "wedding day", None, ["E0", "E1", "E2"], "E0 to E2",
   ["spouse"], [], "Valley Moot statute", "any band, the day only", [], [], ["wedding day"], ["GAR-01", "GAR-03"],
   ENF("moot single-day entry", "the exemption is recorded by the moot as a single-day entry",
       "kept and even traded - families time weddings to the muster",
       "for the second wearing - salt fine and the cords returned"),
   "cannot-evaluate", ["the single-day duration and the borrowed household grade are not expressible"], 264),
 N("WR-07", "obligate", "wearer-category", "treaty stranger", "GAR-06", ["E1", "E2"], "E1 onward",
   ["fair-stranger"], [], "caravan treaty; enforced by the fair court",
   "fairgrounds and valley road only", ["fairgrounds", "valley-road"], [], ["the caravan fair"], ["GAR-06", "GAR-02"],
   ENF("fair court", "at corridor distance a good imitation passes; the court's real test is speech",
       "the fair court convicts on speech, not cloth",
       "coat forfeited; the trader's seal withdrawn for a season"),
   "cannot-evaluate", ["wearer-category is not a gate-modelled property kind",
                       "the G1 ceiling on strangers' felt is a grade predicate"], 277),
 N("WR-08", "prohibit", "material", "plant-thread", "CMAT-06", ["E0", "E1", "E2"],
   "E0 (when the thread was rare) to E2 (when everyone wears it)",
   [], [], "an archaic cord in the archive; renewed twice in living memory", "all bands, unenforced",
   [], [], [], ["GAR-08", "GAR-01", "GAR-04"],
   ENF("none that works", "none that works - the repair patch is the loophole written into the statute",
       "dead letter; old herders still refuse the patch publicly and wear it under the placket",
       "on paper, a salt fine; in practice, moot laughter"),
   "partial", ["the exception channel (bale-tying cord; patches smaller than a hand) is a form/size exemption the gate cannot express"], 290),
 N("WR-09", "permit", "material", "lowland-plant-cloth", "CMAT-06", ["E2"], "E2",
   [], [], "Valley Moot, after the storm-famine", "valley fairgrounds", ["fairgrounds"], [], ["the caravan fair"],
   ["GAR-02", "GAR-04", "GAR-08"],
   ENF("fair register", "the register keeps the seller's name, not the buyer's",
       "the reform passes and the fair booms",
       "none (permissive statute)"),
   "partial", ["the supersession list (which clauses this reform overrides) is not stated (RR-01)"], 303),
]

ACT_RULES = [
 {"id": "SR-01#a", "source_rule": "SR-01", "channel": "speech", "object": "storm-name", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": ["wind-speaker"], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "below the snow-line", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel; raw sign_axis: sacred speech - the storm-name"], "cite": C12 + "318-329"},
 {"id": "SR-01#b", "source_rule": "SR-01", "channel": "speech", "object": "storm-name", "effect": "permit",
  "wearer_ranks": ["wind-speaker"], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "above the snow-line", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "318-329"},
 {"id": "SR-02#a", "source_rule": "SR-02", "channel": "speech", "object": "summit greeting", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"], "jurisdiction": "below the snow-line",
  "adapt_status": "cannot-evaluate", "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "330-341"},
 {"id": "SR-03#a", "source_rule": "SR-03", "channel": "speech", "object": "another lineage's dead-name",
  "effect": "prohibit", "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "valley moot only", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "342-353"},
 {"id": "SR-04#a", "source_rule": "SR-04", "channel": "speech", "object": "oath-form", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "valley and camps (lineage oath); fairgrounds (trade oath)", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "354-365"},
 {"id": "SR-05#a", "source_rule": "SR-05", "channel": "speech", "object": "statute-recitation", "effect": "obligate",
  "wearer_ranks": ["wind-speaker"], "exempt_ranks": [], "eras": ["E1", "E2"],
  "jurisdiction": "everywhere the moot's law runs", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "366-377"},
 {"id": "SR-06#a", "source_rule": "SR-06", "channel": "speech", "object": "storm-law recitation", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "valley, any season except the storm; camps, never", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel",
                 "the jurisdiction field excludes the settings where the prohibition appears to operate (RR-02)"], "cite": C12 + "378-389"},
 {"id": "TR-01#a", "source_rule": "TR-01", "channel": "touch", "object": "archive cord", "effect": "prohibit",
  "wearer_ranks": ["lineage-head"], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "the winter valley archive", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel; the touch right is limited to the lineage's own cord in the keeper's presence"], "cite": C12 + "392-404"},
 {"id": "TR-02#a", "source_rule": "TR-02", "channel": "touch", "object": "wind-standard hem", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"], "jurisdiction": "the moot only",
  "adapt_status": "cannot-evaluate", "unresolved": ["touch is not a gate-modelled channel; the act kind is named by the spec's table but not modelled by the gate"], "cite": C12 + "405-417"},
 {"id": "TR-03#a", "source_rule": "TR-03", "channel": "touch", "object": "bale seal-knot", "effect": "permit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E1", "E2"],
  "jurisdiction": "fairgrounds; the custom travels with the bales", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel"], "cite": C12 + "418-430"},
 {"id": "TR-04#a", "source_rule": "TR-04", "channel": "touch", "object": "salt-measure", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": ["fair-stranger"], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "fairgrounds and valley stores", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel"], "cite": C12 + "431-442"},
 {"id": "TR-05#a", "source_rule": "TR-05", "channel": "touch", "object": "mast rope", "effect": "permit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "above the snow-line, during storm law only", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel; the necessity clause's interval (while storm law holds) disagrees with WR-05"], "cite": C12 + "443-455"},
 {"id": "TR-06#a", "source_rule": "TR-06", "channel": "touch", "object": "salt-measure", "effect": "obligate",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E1", "E2"], "jurisdiction": "fairgrounds",
  "adapt_status": "cannot-evaluate", "unresolved": ["touch is not a gate-modelled channel"], "cite": C12 + "456-468"},
]
RESIDUALS = [
 {"id": "WR-06#b", "source_rule": "WR-06", "reason": "the household-grade lock is a grade predicate; recorded as a loss, not a record", "cite": C12 + "264-276"},
]
CALIBRATION_FLAGS = [
 {"rule": "WR-05", "text": "observed hard - mourning is the one rule that is self-enforcing", "cite": C12 + "259"},
 {"rule": "SR-06", "text": "kept strictly", "cite": C12 + "386"},
 {"rule": "TR-05", "text": "the one rule no one evades", "cite": C12 + "451"},
]
ENTITLEMENT_EDGES = [
 {"rank": "fair-stranger", "rights": "may wear their own lowland cloth and fair coat", "cite": C12 + "189", "against": ["WR-02"]},
 {"rank": "herd-master", "rights": "may wear lowland cloth inside the fairgrounds", "cite": C12 + "171", "against": []},
]
QUARANTINE = [
 {"handle": "WI-2", "issue": "no DEG slot: rule_ref is '(to-verify) DEG slot'", "adapt_status": "cannot-evaluate",
  "cite": "examples/culture-d2/components/11-costumes.yml:102"},
 {"handle": "WI-3..WI-7", "issue": "lexicon_ref is '(to-verify)' for each", "adapt_status": "cannot-evaluate",
  "cite": "examples/culture-d2/components/11-costumes.yml:103-107"},
 {"handle": "GAR-06", "issue": "one wearer_rank field names two ranks; the primary is declared in RANK_RESOLUTIONS, the gift reading stays secondary",
  "adapt_status": "cannot-evaluate", "cite": "examples/culture-d2/packet.d2.yml:2007"},
]
CONFLICT_TRIAGE = {
 "WR-02|WR-09": {"status": "genuine-priority-gap", "why": "RR-01: the E2 reform's supersession of the E1 monopoly is unstated", "cite": C12 + "212-224,303-315"},
 "WR-05|WR-09": {"status": "genuine-priority-gap", "reachable": False,
                 "why": "RR-01 recheck: an ordinary household's lowland cloth at the E2 winter fair against the mourning-body ban; not emitted as a conflict because WR-05's rite-state kind is not gate-modelled", "cite": C12 + "251-263,303-315"},
 "WR-08|WR-09": {"status": "genuine-priority-gap", "why": "RR-01: the fossil ban is a dead letter in practice but is not repealed on paper", "cite": C12 + "290-302,303-315"},
 "WR-03|WR-06": {"status": "abstraction-artifact", "reachable": False,
                 "why": "both carry {trim, hem-cord}, but WR-06 is an occasion exemption (exempt path, A6) and is not projected, so the pair cannot fire; retained because a future projection change would resurrect it", "cite": C12 + "225-237,264-276"},
 "SR-01#a|SR-01#b": {"status": "band-keyed-pair", "why": "below-line prohibition and above-line permission of the same rule; jurisdictions are disjoint by construction", "cite": C12 + "318-329"},
 "TR-04#a|TR-06#a": {"status": "genuine-priority-gap", "why": "RR-03: the sale's mandatory touch of the buyer's measure collides with the prohibition on touching the measure rather than the salt", "cite": C12 + "431-442,456-468"},
}
JURISDICTION_GAPS = [
 {"rule": "WR-02", "gap": "the sell-line is undefined, so upland wearing is either illegal-but-unpoliced or outside the ban", "cite": C12 + "212-224"},
 {"rule": "SR-06", "gap": "the jurisdiction field excludes the settings where the prohibition appears to operate", "cite": C12 + "378-389"},
 {"rule": "JU-3", "gap": "officer coverage disagrees with EN-2's circuit-wide reach", "cite": C12 + "514-520,528-533"},
]
ASSAY_GAPS = [
 {"rule": "WR-01", "gap": "no felt-day-to-grade thresholds, ascent/bale-to-entitlement rule, or coat-to-bale link exists", "cite": C12 + "199-211"},
 {"rule": "WR-03", "gap": "the cord count has no machine-readable field on the costume rows", "cite": C12 + "225-237"},
]
COMPONENT_RULE_IDS = ["WR-0%d" % i for i in range(1, 10)] + ["SR-0%d" % i for i in range(1, 7)] + ["TR-0%d" % i for i in range(1, 7)]

def project_to_gate(rec):
    """Normalized record -> gate schema, or None when the gate cannot evaluate it."""
    kind = key(rec["property"]["kind"])
    if rec["adapt_status"] == "cannot-evaluate" or kind in NON_PROJECTABLE_KINDS:
        return None
    if kind not in GATE_KIND_MAP:
        raise Malformed("%s: no declared gate kind mapping for %r" % (rec["id"], kind))
    value = GATE_VALUE_MAP.get((kind, rec["property"]["value"]))
    if value is None:
        raise Malformed("%s: no declared gate value mapping for (%s, %s) - refusing to invent one"
                        % (rec["id"], kind, rec["property"]["value"]))
    gate_effect = GATE_EFFECT_MAP[rec["effect"]]
    if gate_effect is None:
        return None
    if rec["effect"] == "prohibit":
        wearer_ranks, exempt_ranks = [], list(rec["wearer_ranks"]) + list(rec["exempt_ranks"])
    else:
        wearer_ranks, exempt_ranks = list(rec["wearer_ranks"]), list(rec["exempt_ranks"])
    return {"id": rec["id"] + "#g", "source_rule": rec["id"], "authority": rec["authority"],
            "jurisdiction": rec["jurisdiction"]["raw"], "eras": list(rec["eras"]),
            "rites": list(rec["rites"]) or None, "effect": gate_effect,
            "property": {"kind": GATE_KIND_MAP[kind], "value": value},
            "wearer_ranks": wearer_ranks, "exempt_ranks": exempt_ranks,
            "adapt_status": rec["adapt_status"], "cite": rec["source"]["component"] + ":" + str(rec["source"]["line"]),
            "semantics_note": ("spec wearer_ranks names the licensed class for a prohibition; the gate scopes "
                               "wearer_ranks to the class the rule bites, so the licensed class moves to exempt_ranks")}

def naive_projection(rec):
    """The un-translated copy that inverts prohibition verdicts; shipped only as a negative control."""
    out = project_to_gate(rec)
    if out is None:
        return None
    out = dict(out)
    out["wearer_ranks"], out["exempt_ranks"] = list(rec["wearer_ranks"]), list(rec["exempt_ranks"])
    return out

def build_payload():
    src = sorted({r["id"] for r in NORMALIZED} | {r["source_rule"] for r in ACT_RULES} | {r["source_rule"] for r in RESIDUALS})
    if src != sorted(COMPONENT_RULE_IDS):
        raise Malformed("coverage: component rules %r not partitioned exactly" % sorted(set(COMPONENT_RULE_IDS) ^ set(src)))
    for rec in NORMALIZED:
        if not rec["eras"]:
            raise Malformed("%s: no effective interval (EAR-04 class)" % rec["id"])
        if rec["adapt_status"] not in ("executable", "partial", "cannot-evaluate"):
            raise Malformed("%s: unknown adapt_status %r" % (rec["id"], rec["adapt_status"]))
    gate = [g for g in (project_to_gate(r) for r in NORMALIZED) if g is not None]
    unresolved = sorted([{"rule": r["id"], "item": u} for r in NORMALIZED for u in r["unresolved"]],
                        key=lambda d: (d["rule"], d["item"]))
    return {"normalized_rules": sorted(NORMALIZED, key=lambda r: r["id"]),
            "gate_rank_rules": sorted(gate, key=lambda r: r["id"]),
            "act_rules": sorted(ACT_RULES, key=lambda r: r["id"]),
            "residuals": sorted(RESIDUALS, key=lambda r: r["id"]),
            "unresolved": unresolved,
            "quarantine": sorted(QUARANTINE, key=lambda r: r["handle"]),
            "calibration_flags": sorted(CALIBRATION_FLAGS, key=lambda r: r["rule"]),
            "entitlement_edges": sorted(ENTITLEMENT_EDGES, key=lambda r: r["rank"]),
            "jurisdiction_gaps": sorted(JURISDICTION_GAPS, key=lambda r: r["rule"]),
            "assay_gaps": sorted(ASSAY_GAPS, key=lambda r: r["rule"]),
            "coverage": {"component_rules": len(COMPONENT_RULE_IDS), "normalized": len(NORMALIZED),
                         "gate_projected": len(gate), "partitioned": True}}

def scope_of(rule):
    return {r for r in (rule.get("wearer_ranks") or sorted(RANK_TOKENS)) if r not in set(rule.get("exempt_ranks") or [])}

def eras_overlap(a, b):
    return bool({key(x) for x in a} & {key(x) for x in b})

def conflicts(records):
    out = []
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            if key(a["property"]["kind"]) != key(b["property"]["kind"]) or key(a["property"]["value"]) != key(b["property"]["value"]):
                continue
            if {key(a["effect"]), key(b["effect"])} != {"prohibit", "permit"}:
                continue
            if not eras_overlap(a["eras"], b["eras"]):
                continue
            shared = scope_of(a) & scope_of(b)
            if shared:
                pid = "%s|%s" % (a["source_rule"], b["source_rule"])
                out.append({"class": "R-05-class", "pair": [a["id"], b["id"]], "rank_in_scope": sorted(shared)[0],
                            "triage": CONFLICT_TRIAGE.get(pid, {"status": "UNTRIAGED"})})
    return out

def act_conflicts(rules):
    out = []
    for i, a in enumerate(rules):
        for b in rules[i + 1:]:
            if a["channel"] != b["channel"] or key(a["object"]) != key(b["object"]):
                continue
            if not eras_overlap(a["eras"], b["eras"]):
                continue
            effs = {key(a["effect"]), key(b["effect"])}
            if effs & {"prohibit"} and effs & {"permit", "obligate"}:
                pid = "%s|%s" % (a["id"], b["id"])
                out.append({"class": "act-collision", "pair": [a["id"], b["id"]], "object": a["object"],
                            "triage": CONFLICT_TRIAGE.get(pid, {"status": "UNTRIAGED"})})
    return out

def verdict_for(rule, row):
    """Three-valued verdict in the spec's vocabulary, mirroring the gate's applicability order."""
    if not any(key(e) == key(row.get("era")) for e in rule["eras"]):
        return "not-applies"
    kind = key(rule["property"]["kind"])
    if kind not in GATE_PROPERTY_KINDS:
        raise Malformed("property kind %r is outside the gate's modelled set" % kind)
    value = key(rule["property"]["value"])
    if kind in ("material", "fiber", "cloth", "fabric", "textile"):
        target = key(row.get("material") or "")
        if not target or target != value:
            return "not-applies"
    elif kind in ("garment", "robe", "clothing"):
        target = key(row.get("garment") or "")
        if not target or not (target == value or (len(value) >= 4 and value in target)):
            return "not-applies"
    elif kind in ("badge", "insignia"):
        target = key(row.get("badge_office") or row.get("badge") or "")
        if not target or target != value:
            return "not-applies"
    elif kind in ("trim", "closure", "fastening"):
        return "cannot-evaluate"
    else:
        return "not-applies"
    if rule.get("effect") not in ("prohibit", "permit"):
        return "cannot-evaluate"
    wearer, status, _ = resolve_costume_rank(row)
    wearer_ranks = rule.get("wearer_ranks")
    if wearer_ranks:
        if status != "resolved":
            return "cannot-evaluate"
        if not any(key(wearer) == key(w) for w in wearer_ranks):
            return "not-applies"
    elif status in ("unresolved", "ambiguous"):
        return "cannot-evaluate"
    if any(key(wearer) == key(x) for x in (rule.get("exempt_ranks") or [])):
        return "not-applies"
    return "applies"

def entitlement_conflicts(records):
    by_rule = {r["source_rule"]: r for r in records}
    out = []
    for edge in ENTITLEMENT_EDGES:
        for rid in edge["against"]:
            rec = by_rule[rid]
            if key(rec["effect"]) == "prohibit" and edge["rank"] in scope_of(rec):
                out.append({"class": "entitlement-conflict", "rank": edge["rank"], "rule": rid, "cite": edge["cite"],
                            "note": "declared degree entitlement meets a projected prohibition with no exemption"})
    return out

def fixtures():
    gate = {r["source_rule"]: r for r in (g for g in (project_to_gate(r) for r in NORMALIZED) if g is not None)}
    stranger = {"id": "FIX-STRANGER", "material": "lowland plant-thread cloth", "era": "E2",
                "wearer_rank": "treaty stranger (WI-5)", "rite": "the caravan fair (treaty days)"}
    master = {"id": "FIX-MASTER", "material": "lowland plant-thread cloth", "era": "E1",
              "wearer_rank": "registered herd-master only (WI-3)", "rite": "the caravan fair (treaty days)"}
    mourner = {"id": "FIX-MOURNER", "material": "lowland plant-thread cloth", "era": "E1",
               "wearer_rank": "mourner, household of the dead (WI-6)", "rite": "the mourning year (time-locked)"}
    return [
      {"name": "RR-01 treaty stranger in their own lowland cloth at the E2 fair", "row": stranger,
       "verdicts": {rid: verdict_for(gate[rid], stranger) for rid in ("WR-02", "WR-09")}},
      {"name": "spec worked example: registered herd-master at the E1 fair", "row": master,
       "verdicts": {rid: verdict_for(gate[rid], master) for rid in ("WR-02", "WR-09")}},
      {"name": "RR-04 mourner on the second day of storm law", "row": mourner,
       "verdicts": {"WR-05": "cannot-evaluate (rite-state is not gate-modelled)"},
       "act_interval": {"WR-05": "storm law's first day only", "TR-05#a": "while storm law holds"},
       "interval_mismatch": True},
      {"name": "RR-05 shelter-kin coat of unrecorded felt grade",
       "verdicts": {"WR-01": "cannot-evaluate (grade kind; no felt-day-to-grade thresholds exist)"}},
    ]

def selftest():
    checks, payload = [], build_payload()
    def ck(name, cond, detail=""):
        checks.append({"check": name, "ok": bool(cond), "detail": detail})
    ck("coverage.partition", payload["coverage"]["partitioned"] and payload["coverage"]["component_rules"] == 21)
    ck("coverage.normalized_nine", payload["coverage"]["normalized"] == 9)
    ck("coverage.gate_projected_five", payload["coverage"]["gate_projected"] == 5
       and "WR-04" in [g["source_rule"] for g in payload["gate_rank_rules"]],
       str([g["source_rule"] for g in payload["gate_rank_rules"]]))
    ck("triage.unreachable_marked", all(("reachable" in t) == (t.get("reachable") is False)
       for t in CONFLICT_TRIAGE.values()))
    ck("record.spec_shape", all({"id", "authority", "jurisdiction", "effect", "property", "wearer_ranks",
        "exempt_ranks", "eras", "era_history_raw", "rites", "garment_refs", "enforcement", "adapt_status",
        "unresolved", "source"} <= set(r) for r in payload["normalized_rules"]))
    ck("record.source_mapping", all(r["source"]["component"] == "12-rank-rules.yml" and r["source"]["line"]
        and r["source"]["record_id"] == r["id"] for r in payload["normalized_rules"]))
    ck("record.adapt_status_vocabulary", all(r["adapt_status"] in ("executable", "partial", "cannot-evaluate")
        for r in payload["normalized_rules"]))
    ck("identity.herd_master", resolve_costume_rank({"id": "GAR-04", "wearer_rank": "registered herd-master only (WI-3)"})[0] == "herd-master")
    ck("identity.ambiguous_never_silent", resolve_costume_rank({"id": "X", "wearer_rank": "treaty stranger and a lineage head"})[1] == "ambiguous")
    ck("identity.unresolved_never_silent", resolve_costume_rank({"id": "X", "wearer_rank": "no rank named"})[1] == "unresolved")
    ck("quarantine.A8_present", {q["handle"] for q in payload["quarantine"]} >= {"WI-2", "WI-3..WI-7", "GAR-06"})
    conf = conflicts(payload["gate_rank_rules"])
    pairs = sorted(tuple(c["pair"]) for c in conf)
    ck("conflict.WR02_vs_WR09", ("WR-02#g", "WR-09#g") in pairs, str(pairs))
    ck("conflict.all_triaged", all(c["triage"]["status"] != "UNTRIAGED" for c in conf))
    actp = act_conflicts(payload["act_rules"])
    ck("actconflict.TR04_vs_TR06", ("TR-04#a", "TR-06#a") in sorted(tuple(c["pair"]) for c in actp))
    ck("actconflict.all_triaged", all(c["triage"]["status"] != "UNTRIAGED" for c in actp))
    gate = {r["source_rule"]: r for r in payload["gate_rank_rules"]}
    master = {"id": "FIX-MASTER", "material": "lowland plant-thread cloth", "era": "E1",
              "wearer_rank": "registered herd-master only (WI-3)"}
    ck("spec.worked_example_not_applies", verdict_for(gate["WR-02"], master) == "not-applies",
       verdict_for(gate["WR-02"], master))
    naive = {r["source_rule"]: r for r in (naive_projection(r) for r in NORMALIZED) if r is not None}
    ck("control.naive_projection_inverts", verdict_for(naive["WR-02"], master) == "applies",
       "naive=%s declared=%s" % (verdict_for(naive["WR-02"], master), verdict_for(gate["WR-02"], master)))
    stranger = {"id": "FIX-STRANGER", "material": "lowland plant-thread cloth", "era": "E2",
                "wearer_rank": "treaty stranger (WI-5)"}
    ck("control.declared_projection_still_catches_stranger", verdict_for(gate["WR-02"], stranger) == "applies")
    ent = entitlement_conflicts(payload["gate_rank_rules"])
    ck("entitlement.fair_stranger", any(e["rank"] == "fair-stranger" for e in ent))
    fx = fixtures()
    ck("fixture.RR01_conflict_visible", fx[0]["verdicts"] == {"WR-02": "applies", "WR-09": "applies"}, str(fx[0]["verdicts"]))
    ck("fixture.RR04_interval_mismatch", fx[2]["interval_mismatch"] is True)
    ck("fixture.RR05_cannot_evaluate", "cannot-evaluate" in fx[3]["verdicts"]["WR-01"])
    ck("gaps.RR02_present", {g["rule"] for g in payload["jurisdiction_gaps"]} >= {"WR-02", "SR-06", "JU-3"})
    ck("gaps.RR05_present", {g["rule"] for g in payload["assay_gaps"]} >= {"WR-01", "WR-03"})
    ck("calibration.flags_present", len(payload["calibration_flags"]) == 3)
    ck("unresolved.not_empty", len(payload["unresolved"]) >= 6, str(len(payload["unresolved"])))
    d1 = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
    d2 = hashlib.sha256(json.dumps(build_payload(), sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
    ck("determinism.double_build", d1 == d2, d1)
    try:
        project_to_gate({"id": "X", "effect": "prohibit", "adapt_status": "executable",
                         "property": {"kind": "material", "value": "invented-cloth"}, "wearer_ranks": [],
                         "exempt_ranks": [], "eras": ["E0"], "rites": [], "authority": "?", "jurisdiction": {"raw": "?"},
                         "source": {"component": "12-rank-rules.yml", "record_id": "X", "line": 1}})
        ck("neg.undeclared_value_refused", False, "no rejection")
    except Malformed as exc:
        ck("neg.undeclared_value_refused", True, str(exc))
    ck("neg.unknown_rank_cannot_evaluate", verdict_for({"eras": ["E0"], "effect": "prohibit",
        "property": {"kind": "material", "value": "felt"}, "wearer_ranks": [], "exempt_ranks": []},
        {"id": "X", "material": "felt", "era": "E0", "wearer_rank": "unlisted rank"}) == "cannot-evaluate")
    ck("neg.trim_cannot_evaluate", verdict_for({"eras": ["E0"], "effect": "prohibit",
        "property": {"kind": "trim", "value": "hem-cord"}, "wearer_ranks": [], "exempt_ranks": []},
        {"id": "GAR-03", "material": "felt", "era": "E0", "wearer_rank": "herder household"}) == "cannot-evaluate")
    failed = [c for c in checks if not c["ok"]]
    print("passed=%d failed=%d digest=%s" % (len(checks) - len(failed), len(failed), d1))
    for c in failed:
        print("FAIL", c["check"], c["detail"])
    print("conflicts:", json.dumps([(c["pair"], c["triage"]["status"]) for c in conf]))
    print("act:", json.dumps([(c["pair"], c["triage"]["status"]) for c in actp]))
    return 0 if not failed else 1



# The rank block's own selftest prints and returns 0/1; the integrated

# selftest calls it through this alias, bound before the CLI defines its own

# `selftest` (binding it after would recurse).

selftest_rank_block = selftest

# ==========================================================================

# Block 4/4 — scoped era/material reconciliation (R8-D05 §4), lifted

# verbatim except its __main__ driver, removed for the same reason.

# ==========================================================================

"""Scoped era/material reconciliation for D2 typed labels (R8-D05 shard).

One scope = one era label system + one material inventory. Every decision is
local to a declared scope; cross-scope comparisons run only through an
explicitly declared bridge with an era_map. Nothing is aliased, dated, unioned
or rewritten: findings are additive dispositions beside the raw records.

Grounded in examples/culture-d2/packet.d2.yml assembly.unresolved (:3339,
:3342), CMAT-03/CMAT-08 maps_to notes (:3172-3173, :3253-3254), GAR-04/GAR-06
era seams (:1964, :2017); corpus/knowledge/synthesis/era-language-staging.md
§1, §7; loanword-material-dating.md §2, §6; costume-language-coupling-table.md
§2; reports/supplement-opencode-1/22-label-representation.md §2;
reports/round-7/parent-reconciliation.json (scoped dispositions).

Finding codes are R-* (reconciliation), distinct from the parser's E-*/W-*.
Malformed input raises ReconciliationError; the CLI maps it to exit 2.
"""

import json
import re
import unicodedata

_ID_TOKEN = re.compile(r"(?<![A-Za-z0-9-])([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)(?![A-Za-z0-9-])")


def _declared_id(value):
    """The id token a maps_to string declares, or None.

    Packet maps_to values carry a declared id inside prose ("10-materials
    MAT-01 ewe-fleece (same slot: …)"); extraction is token-shape only — the
    lane's id convention (D03's _ID_RE) — never an alias or a guessed target.
    """
    match = _ID_TOKEN.search(value)
    return match.group(1) if match else None


R_ERA_IN_SCOPE = "R-ERA-IN-SCOPE"
R_ERA_NAME_FORM = "R-ERA-NAME-FORM"
R_ERA_UNMAPPED = "R-ERA-UNMAPPED"
R_ERA_BRIDGE_UNMAPPED = "R-ERA-BRIDGE-UNMAPPED"
R_ERA_MAPPING_UNCONFIRMED = "R-ERA-MAPPING-UNCONFIRMED"
R_MAT_RESOLVED = "R-MAT-RESOLVED"
R_MAT_UNRESOLVED = "R-MAT-UNRESOLVED-REF"
R_MAT_TRANSLATED = "R-MAT-TRANSLATED-MATCH"
R_MAT_ERA_UNCHECKED = "R-MAT-ERA-UNCHECKED"
R_MAT_ERA_EXCLUDED = "R-MAT-ERA-EXCLUDED"
R_MAT_CARRIED_FLAG = "R-MAT-CARRIED-FLAG"
R_MAT_BRIDGE_MISSING = "R-MAT-BRIDGE-MISSING"
R_MAT_CROSS_SCOPE = "R-MAT-CROSS-SCOPE"
R_MAT_DANGLING = "R-MAT-DANGLING"
R_MAT_SLOT_CONFLICT = "R-MAT-SLOT-CONFLICT"
R_MAT_SLOT_MISMATCH = "R-MAT-SLOT-MISMATCH"

SEVERITY = {
    R_ERA_IN_SCOPE: "ok", R_ERA_NAME_FORM: "note", R_ERA_UNMAPPED: "hold",
    R_ERA_BRIDGE_UNMAPPED: "hold", R_ERA_MAPPING_UNCONFIRMED: "hold",
    R_MAT_RESOLVED: "ok", R_MAT_UNRESOLVED: "hold", R_MAT_TRANSLATED: "hold",
    R_MAT_ERA_UNCHECKED: "hold", R_MAT_ERA_EXCLUDED: "reject",
    R_MAT_CARRIED_FLAG: "note", R_MAT_BRIDGE_MISSING: "hold",
    R_MAT_CROSS_SCOPE: "note", R_MAT_DANGLING: "hold",
    R_MAT_SLOT_CONFLICT: "hold", R_MAT_SLOT_MISMATCH: "hold",
}

# R8-D01 design-spec §2.2/§3.2 verdicts and §6 finding classes, carried beside
# every code so D02 can emit the contract vocabulary without a second mapping.
VERDICT = {
    R_ERA_IN_SCOPE: "identity", R_ERA_NAME_FORM: "mapped-confirmed",
    R_ERA_UNMAPPED: "unmapped", R_ERA_BRIDGE_UNMAPPED: "unmapped",
    R_ERA_MAPPING_UNCONFIRMED: "mapped-unconfirmed",
    R_MAT_RESOLVED: "available", R_MAT_CROSS_SCOPE: "available",
    R_MAT_ERA_EXCLUDED: "unavailable-by-closure",
    R_MAT_ERA_UNCHECKED: "unresolved", R_MAT_UNRESOLVED: "unresolved",
    R_MAT_TRANSLATED: "unresolved", R_MAT_CARRIED_FLAG: "unresolved",
    R_MAT_BRIDGE_MISSING: "unresolved", R_MAT_DANGLING: "unresolved",
    R_MAT_SLOT_CONFLICT: "unresolved", R_MAT_SLOT_MISMATCH: "unresolved",
}

FINDING_CLASS = {
    R_ERA_IN_SCOPE: "D2L-ERA", R_ERA_NAME_FORM: "D2L-ERA",
    R_ERA_UNMAPPED: "D2L-ERA", R_ERA_BRIDGE_UNMAPPED: "D2L-ERA",
    R_ERA_MAPPING_UNCONFIRMED: "D2L-ERA",
    R_MAT_RESOLVED: "D2L-MATERIAL", R_MAT_CROSS_SCOPE: "D2L-MATERIAL",
    R_MAT_ERA_EXCLUDED: "D2L-MATERIAL", R_MAT_ERA_UNCHECKED: "D2L-MATERIAL",
    R_MAT_CARRIED_FLAG: "D2L-MATERIAL", R_MAT_SLOT_CONFLICT: "D2L-MATERIAL",
    R_MAT_SLOT_MISMATCH: "D2L-MATERIAL",
    R_MAT_UNRESOLVED: "D2L-SCOPE", R_MAT_TRANSLATED: "D2L-SCOPE",
    R_MAT_BRIDGE_MISSING: "D2L-SCOPE", R_MAT_DANGLING: "D2L-SCOPE",
}


class ReconciliationError(ValueError):
    """Malformed input: fail closed (the CLI maps this to exit 2)."""


def _token(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ReconciliationError(f"{field}: expected a non-empty string, got {value!r}")
    return unicodedata.normalize("NFC", value.strip())


def _check_unique_ids(records, what):
    ids = []
    for record in records:
        if not isinstance(record, dict):
            raise ReconciliationError(f"{what}: every record must be a mapping")
        ids.append(_token(record.get("id"), f"{what}[].id"))
    if len(ids) != len(set(ids)):
        raise ReconciliationError(f"{what}: duplicate record ids; refusing silent deduplication")
    return ids


def _finding(code, where, detail, scope):
    return {"code": code, "where": where, "scope": scope,
            "severity": SEVERITY[code], "verdict": VERDICT[code],
            "class": FINDING_CLASS[code], "detail": detail}


def era_scope_from_packet(packet):
    """Packet era scope: tags are packet.eras; names are the declared emic
    names from packet.era_records, kept with their row ids — never guessed
    aliases, and a name-form claim cites the row that declares it."""
    if not isinstance(packet, dict):
        raise ReconciliationError("packet: expected a mapping")
    tags = packet.get("eras")
    if not isinstance(tags, list) or not tags or not all(isinstance(t, str) for t in tags):
        raise ReconciliationError("packet.eras: expected a non-empty list of era tags")
    names = {}
    for record in packet.get("era_records") or []:
        if not isinstance(record, dict):
            raise ReconciliationError("packet.era_records[]: expected mappings")
        tag, name = record.get("tag"), record.get("name")
        if not (isinstance(tag, str) and isinstance(name, str)):
            continue
        if tag not in tags:
            raise ReconciliationError(f"packet.era_records: {name!r} names undeclared tag {tag!r}")
        row = {"tag": tag, "row": record.get("id") if isinstance(record.get("id"), str) else None}
        if names.get(name) not in (None, row):
            raise ReconciliationError(f"packet.era_records: name {name!r} maps to two tags")
        names[name] = row
    return {"id": "packet-eras", "axis": "era", "tags": list(tags), "names": names}


def material_scope_from_packet(packet):
    """Packet material scope: the costume-facing inventory as delivered."""
    if not isinstance(packet, dict):
        raise ReconciliationError("packet: expected a mapping")
    records = packet.get("materials")
    if not isinstance(records, list) or not records:
        raise ReconciliationError("packet.materials: expected a non-empty record list")
    _check_unique_ids(records, "packet.materials")
    return {"id": "packet-materials", "axis": "material", "records": records}


def claims_from_packet(packet):
    """Costume records -> reconciliation claims {id, era, material_ref}."""
    claims = []
    for record in packet.get("costumes") or []:
        if not isinstance(record, dict):
            raise ReconciliationError("packet.costumes[]: expected mappings")
        rid = _token(record.get("id"), "packet.costumes[].id")
        era, ref = record.get("era"), record.get("material")
        if not isinstance(era, str) or not era.strip():
            raise ReconciliationError(f"{rid}: costume carries no era claim")
        if not isinstance(ref, str) or not ref.strip():
            raise ReconciliationError(f"{rid}: costume carries no material reference")
        claims.append({"id": rid, "era": era, "material_ref": ref})
    if not claims:
        raise ReconciliationError("packet.costumes: no costume claims to reconcile")
    _check_unique_ids(claims, "claims")
    return claims


def _prepare_scope(scope):
    if not isinstance(scope, dict):
        raise ReconciliationError("scope: expected a mapping")
    sid = _token(scope.get("id"), "scope.id")
    axis = scope.get("axis")
    if axis == "era":
        tags = scope.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(t, str) for t in tags):
            raise ReconciliationError(f"{sid}: era scope needs a non-empty tag list")
        names = scope.get("names") or {}
        if not isinstance(names, dict):
            raise ReconciliationError(f"{sid}: era scope names must map name -> tag or {{tag, row}}")
        normalized = {}
        for key, value in names.items():
            if not isinstance(key, str):
                raise ReconciliationError(f"{sid}: era scope names must map name -> tag or {{tag, row}}")
            if isinstance(value, str):
                normalized[key] = {"tag": value, "row": None}
            elif isinstance(value, dict) and isinstance(value.get("tag"), str):
                normalized[key] = {"tag": value["tag"], "row": value.get("row")}
            else:
                raise ReconciliationError(f"{sid}: era name {key!r} must map to a tag or a {{tag, row}} row")
        return {"id": sid, "axis": "era", "tags": list(tags), "names": normalized}
    if axis == "material":
        records = scope.get("records")
        if not isinstance(records, list) or not records:
            raise ReconciliationError(f"{sid}: material scope needs a non-empty record list")
        _check_unique_ids(records, sid)
        return {"id": sid, "axis": "material", "records": records}
    raise ReconciliationError(f"{sid}: scope axis must be 'era' or 'material'")


def _normalize_era_row(value, where):
    """One declared mapping row: a bare tag (confirmed by declaration) or a
    {tag, status, scope, row} record (design spec §2.1 E4/E5)."""
    if isinstance(value, str):
        return {"tag": value, "status": "confirmed", "scope": None, "row": None}
    if isinstance(value, dict) and isinstance(value.get("tag"), str):
        status = value.get("status", "confirmed")
        if status not in ("confirmed", "to-verify"):
            raise ReconciliationError(f"{where}: mapping status must be confirmed | to-verify")
        scope = value.get("scope")
        if scope is not None and scope not in ("slot", "label"):
            raise ReconciliationError(f"{where}: mapping scope must be slot | label")
        return {"tag": value["tag"], "status": status, "scope": scope, "row": value.get("row")}
    raise ReconciliationError(f"{where}: era mapping must be a tag or a {{tag, status, scope, row}} row")


def _prepare_bridges(bridges, material_scope):
    """Bridges whose source is this material scope; each carries its own
    target scope, an explicit era_map of declared rows, and an optional target
    era scope. Two rows mapping one source tag to different targets raise the
    spec's conflict class (exit 2, D2L-DATA)."""
    prepared = []
    seen = {}
    for bridge in bridges:
        if not isinstance(bridge, dict):
            raise ReconciliationError("bridges[]: expected mappings")
        source = _token(bridge.get("source_scope"), "bridge.source_scope")
        if source != material_scope["id"]:
            continue
        target = _prepare_scope(bridge.get("target_scope"))
        if target["axis"] != "material":
            raise ReconciliationError(f"bridge {source}: target scope must be a material scope")
        era_map = bridge.get("era_map")
        if not isinstance(era_map, dict) or not all(isinstance(k, str) for k in era_map):
            raise ReconciliationError(f"bridge {source} -> {target['id']}: era_map must map tags to rows")
        rows = {}
        for source_tag, value in era_map.items():
            row = _normalize_era_row(value, f"bridge {source} -> {target['id']} era_map[{source_tag!r}]")
            key = (source, source_tag)
            if key in seen and seen[key] != row["tag"]:
                raise ReconciliationError(
                    f"era mapping conflict for {source_tag!r} in {source}: {seen[key]!r} vs {row['tag']!r}; "
                    "exit-2 class D2L-DATA (design spec §2.2 conflict)")
            seen[key] = row["tag"]
            rows[source_tag] = row
        target_era = bridge.get("target_era_scope")
        if target_era is not None:
            target_era = _prepare_scope(target_era)
            if target_era["axis"] != "era":
                raise ReconciliationError(f"bridge {source}: target_era_scope must be an era scope")
        prepared.append({"source_scope": source, "source_records": material_scope["records"],
                         "target": target, "target_era": target_era, "era_map": rows})
    return prepared


def resolve_era(value, era_scope):
    """One era label inside ONE declared system.

    Returns (code, tag, detail): a declared tag is in scope; a declared emic
    name resolves to its tag as a name-form note; anything else is unmapped
    (hold) — never aliased, never dated (packet.d2.yml:3339).
    """
    v = _token(value, "era")
    if v in era_scope["tags"]:
        return R_ERA_IN_SCOPE, v, f"declared tag {v}"
    entry = era_scope["names"].get(v)
    if entry is not None:
        row = entry.get("row") or "<unnamed row>"
        return R_ERA_NAME_FORM, entry["tag"], (f"emic name {v!r} resolves to declared tag {entry['tag']} "
                                               f"(era_records {row}); name form, not a tag")
    return R_ERA_UNMAPPED, None, (f"{v!r} is not a tag or declared name of scope {era_scope['id']} "
                                  f"(tags={era_scope['tags']}); kept as declared, never aliased")


def _match_material(ref, scope):
    """(record, how) over ONE scope; how in {id, key, translated, missing}.

    `key` = the inventory's own material name; `translated` = a display label
    matched instead — identity by translation is not identity
    (22-label-representation.md §2) and is held, never promoted.
    """
    if isinstance(ref, dict):
        rid, name = ref.get("id"), ref.get("name")
        if rid is None and name is None:
            raise ReconciliationError("material_ref: a mapping needs 'id' or 'name'")
    elif isinstance(ref, str):
        rid, name = None, ref
    else:
        raise ReconciliationError(f"material_ref: expected a string or mapping, got {ref!r}")
    if rid is not None:
        rid = _token(rid, "material_ref.id")
        for record in scope["records"]:
            if record["id"] == rid:
                return record, "id"
    if name is not None:
        name = _token(name, "material_ref")
        for record in scope["records"]:
            key = record.get("material")
            if isinstance(key, str) and _token(key, record["id"]) == name:
                return record, "key"
        for record in scope["records"]:
            label = record.get("display_label")
            if isinstance(label, str) and _token(label, record["id"]) == name:
                return record, "translated"
    return None, "missing"


def _era_allowed(material, era):
    """(allowed, why) from the material's own exclusions and declared routes."""
    excluded = material.get("excluded_eras") or []
    if not isinstance(excluded, list) or not all(isinstance(e, str) for e in excluded):
        raise ReconciliationError(f"{material['id']}: excluded_eras must be a list of era tags")
    if era in excluded:
        return False, f"excluded_eras declares {era}"
    routes = material.get("routes")
    if routes:
        if not isinstance(routes, list):
            raise ReconciliationError(f"{material['id']}: routes must be a list")
        for route in routes:
            if not isinstance(route, dict):
                raise ReconciliationError(f"{material['id']}: routes must be mappings")
            eras = route.get("eras")
            if eras is None:
                return True, f"route {route.get('id', route.get('name', '?'))} declares no era bound"
            if not isinstance(eras, list):
                raise ReconciliationError(f"{material['id']}: route eras must be a list or absent")
            if era in eras:
                return True, f"route {route.get('id', route.get('name', '?'))} covers {era}"
        return False, f"no declared route covers {era}"
    return True, "no route list declared"


def _resolve_ref(ref, material_scope, bridges):
    """(record, how, scope_id, bridge): own scope first, then declared bridges."""
    material, how = _match_material(ref, material_scope)
    if material is not None:
        return material, how, material_scope["id"], None
    for bridge in bridges:
        material, how = _match_material(ref, bridge["target"])
        if material is not None:
            return material, how, bridge["target"]["id"], bridge
    return None, "missing", material_scope["id"], None


def reconcile_claim(claim, era_scope, material_scope, bridges=()):
    """One claim -> disposition + non-clean findings. Pure; no I/O.

    claim: {"id", "era", "material_ref"} (claims_from_packet builds these).
    """
    if not isinstance(claim, dict):
        raise ReconciliationError("claims[]: expected mappings")
    rid = _token(claim.get("id"), "claims[].id")
    findings = []

    era_code, era_tag, era_detail = resolve_era(claim.get("era"), era_scope)
    if era_code != R_ERA_IN_SCOPE:
        findings.append(_finding(era_code, rid, era_detail, era_scope["id"]))

    material, how, scope_id, bridge = _resolve_ref(claim.get("material_ref"), material_scope, bridges)
    resolved = material["id"] if material is not None else None
    if material is None:
        material_code = R_MAT_UNRESOLVED
        findings.append(_finding(material_code, rid,
                                 f"material_ref {claim.get('material_ref')!r} resolves in no declared scope "
                                 f"({material_scope['id']} or a declared bridge); a name that matches nothing is "
                                 "not invented into the inventory", material_scope["id"]))
    elif how == "translated":
        material_code = R_MAT_TRANSLATED
        findings.append(_finding(material_code, rid,
                                 f"only a display label matched {material['id']}; identity by translation is not "
                                 "identity (22-label-representation.md §2)", scope_id))
    else:
        check_era = era_tag
        if bridge is not None:
            row = bridge["era_map"].get(era_tag) if era_tag else None
            if row is None:
                check_era = None
                findings.append(_finding(R_ERA_BRIDGE_UNMAPPED, rid,
                                         f"bridge {bridge['source_scope']} -> {scope_id} declares no mapping for "
                                         f"{era_tag!r}; era compatibility not evaluated", scope_id))
            elif row["status"] != "confirmed":
                check_era = None
                findings.append(_finding(R_ERA_MAPPING_UNCONFIRMED, rid,
                                         f"bridge mapping {row['row'] or '<unnamed row>'} for {era_tag!r} is "
                                         f"to-verify (scope {row['scope'] or 'unstated'}); scoped HOLD, the row is "
                                         "never promoted (design spec §2.1 E4/E5)", scope_id))
            else:
                check_era = row["tag"]
                if bridge["target_era"] is not None and row["tag"] not in bridge["target_era"]["tags"]:
                    findings.append(_finding(R_ERA_UNMAPPED, rid,
                                             f"bridged era {row['tag']!r} is not declared in {scope_id} tags "
                                             f"{bridge['target_era']['tags']}", bridge["target_era"]["id"]))
                    check_era = None
        if check_era is None:
            material_code = R_MAT_ERA_UNCHECKED
            findings.append(_finding(material_code, rid,
                                     f"identity {material['id']} resolved, but the era leg has no declared "
                                     "mapping; compatibility held, not assumed", scope_id))
        else:
            allowed, why = _era_allowed(material, check_era)
            if not allowed:
                material_code = R_MAT_ERA_EXCLUDED
                bridged = f" (bridged {era_tag} -> {check_era})" if bridge is not None else ""
                findings.append(_finding(material_code, rid,
                                         f"{material['id']} is not available in {check_era}: {why}{bridged}",
                                         scope_id))
            elif bridge is not None:
                material_code = R_MAT_CROSS_SCOPE
                findings.append(_finding(material_code, rid,
                                         f"resolved {material['id']} across bridge {bridge['source_scope']} -> "
                                         f"{scope_id}; era {era_tag} -> {check_era}; carried as a declared "
                                         "cross-scope reference, not merged", scope_id))
            else:
                material_code = R_MAT_RESOLVED
    return {"record": rid,
            "era": {"code": era_code, "tag": era_tag},
            "material": {"code": material_code, "resolved": resolved},
            "findings": findings}


def _material_record_flags(scope, bridges):
    """Record-side flags: carried notes, missing bridges, dangling maps_to."""
    findings = []
    bridge_by_source = {b["source_scope"]: b for b in bridges}
    for material in scope["records"]:
        maps_to = material.get("maps_to")
        if maps_to is None:
            if material.get("maps_to_note"):
                findings.append(_finding(R_MAT_CARRIED_FLAG, material["id"],
                                         "carried with its declared flag; never merged or dropped",
                                         scope["id"]))
        elif isinstance(maps_to, str):
            key = _declared_id(maps_to) or maps_to
            bridge = bridge_by_source.get(scope["id"])
            if bridge is None:
                findings.append(_finding(R_MAT_BRIDGE_MISSING, material["id"],
                                         f"maps_to {maps_to!r} declares {key!r} with no bridge for scope "
                                         f"{scope['id']}; carried, not merged", scope["id"]))
            else:
                target_record = next((r for r in bridge["target"]["records"] if r["id"] == key), None)
                if target_record is None:
                    findings.append(_finding(R_MAT_DANGLING, material["id"],
                                             f"maps_to {maps_to!r} declares {key!r}, which names no record in "
                                             f"{bridge['target']['id']}", scope["id"]))
                else:
                    source_slot, target_slot = material.get("slot"), target_record.get("slot")
                    if (isinstance(source_slot, str) and isinstance(target_slot, str)
                            and source_slot != target_slot):
                        findings.append(_finding(R_MAT_SLOT_MISMATCH, material["id"],
                                                 f"maps_to {key!r} carries slot {source_slot!r} but the target "
                                                 f"declares {target_slot!r}; identity is by slot, never by label "
                                                 "(design spec §3.1 M1/M3)", scope["id"]))
        else:
            raise ReconciliationError(f"{material['id']}: maps_to must be a string or null")
    return findings


def _slot_conflicts(scopes, bridges):
    """Same-slot claims are kept as declared and flagged, within and across
    declared bridges (OQ-3: keep both luxuries or re-letter the record)."""
    findings = []
    seen = set()

    def add(record, scope_id, slot, ids):
        key = (record["id"], scope_id, slot)
        if key in seen:
            return
        seen.add(key)
        findings.append(_finding(R_MAT_SLOT_CONFLICT, record["id"],
                                 f"slot {slot!r} is claimed by {ids}; both records are kept as declared "
                                 "(OQ-3), never merged", scope_id))

    def grouped(scope):
        out = {}
        for record in scope["records"]:
            slot = record.get("slot")
            if slot is None:
                continue
            out.setdefault(_token(slot, f"{record['id']}.slot"), []).append(record)
        return out

    for scope in scopes:
        for slot, records in grouped(scope).items():
            if len(records) > 1:
                ids = [r["id"] for r in records]
                for record in records:
                    add(record, scope["id"], slot, ids)
    for bridge in bridges:
        target = bridge["target"]
        source_slots = grouped({"id": bridge["source_scope"], "records": bridge["source_records"]})
        target_slots = grouped(target)
        for slot in sorted(set(source_slots) & set(target_slots)):
            source_records, target_records = source_slots[slot], target_slots[slot]
            ids = [r["id"] for r in source_records] + [r["id"] for r in target_records]
            for record in source_records:
                add(record, bridge["source_scope"], slot, ids)
            for record in target_records:
                add(record, target["id"], slot, ids)
    return findings


def reconcile_claims(claims, era_scope, material_scope, external_scopes=(), bridges=()):
    """Core driver over declared scopes; returns a JSON-serializable result."""
    era = _prepare_scope(era_scope)
    if era["axis"] != "era":
        raise ReconciliationError(f"{era['id']}: expected an era scope")
    mat = _prepare_scope(material_scope)
    if mat["axis"] != "material":
        raise ReconciliationError(f"{mat['id']}: expected a material scope")
    externals = [_prepare_scope(s) for s in external_scopes]
    for scope in externals:
        if scope["axis"] != "material":
            raise ReconciliationError(f"{scope['id']}: external scopes must be material scopes")
    brs = _prepare_bridges(bridges, mat)
    _check_unique_ids(claims, "claims")

    results = [reconcile_claim(claim, era, mat, brs) for claim in claims]
    findings = [f for r in results for f in r["findings"]]
    scanned = set()
    for scope in [mat] + externals + [b["target"] for b in brs]:
        if scope["id"] in scanned:
            continue
        scanned.add(scope["id"])
        findings += _material_record_flags(scope, brs)
    findings += _slot_conflicts([mat] + [b["target"] for b in brs] + externals, brs)
    findings.sort(key=lambda f: (f["where"], f["code"], f["scope"], f["detail"]))
    by_severity = {}
    for f in findings:
        by_severity[f["severity"]] = by_severity.get(f["severity"], 0) + 1
    return {
        "scopes": {"era": era["id"], "material": mat["id"],
                   "bridges": [f"{b['source_scope']}->{b['target']['id']}" for b in brs]},
        "records": results,
        "findings": findings,
        "summary": {"claims": len(claims), "findings": len(findings),
                    "by_severity": dict(sorted(by_severity.items())),
                    "by_code": {code: sum(1 for f in findings if f["code"] == code)
                                for code in sorted({f["code"] for f in findings})}},
    }


def reconcile_scoped(packet, external_scopes=(), bridges=(), claims=None):
    """Packet entry: derive scopes/claims from the packet, then reconcile.

    external_scopes/bridges are declared inputs (e.g. the 10-materials E1-E4
    inventory and the E4 = brief-E2 mapping). This function never reads sibling
    component files and never infers an alias or a date.
    """
    era_scope = era_scope_from_packet(packet)
    material_scope = material_scope_from_packet(packet)
    if claims is None:
        claims = claims_from_packet(packet)
    return reconcile_claims(claims, era_scope, material_scope, external_scopes, bridges)


def _selftest_era_material():
    """Positive + malformed controls. Returns [(label, ok, detail), ...]."""
    checks = []

    def check(label, condition, detail=""):
        checks.append((label, bool(condition), detail))

    era_scope = {"id": "brief-E0-E3", "axis": "era", "tags": ["E0", "E1", "E2", "E3"],
                 "names": {"Open Grazing": "E0"}}
    material_scope = {"id": "costumes-CMAT", "axis": "material", "records": [
        {"id": "CMAT-01", "material": "wool", "slot": "state-fiber",
         "display_label": "felt display name",
         "routes": [{"id": "RT-c01", "kind": "local", "stage": "fiber", "eras": ["E0", "E1", "E2"]}]},
        {"id": "CMAT-06", "material": "lowland plant-thread cloth", "slot": "imported-cloth",
         "excluded_eras": ["E0"],
         "routes": [{"id": "RT-c06", "kind": "import", "stage": "cloth", "eras": ["E1", "E2"]}]},
        {"id": "CMAT-08", "material": "silk", "slot": "anchor-era-luxury", "maps_to": None,
         "maps_to_note": "REPORT, do not merge: 10-materials has no silk record (packet.d2.yml:3254)",
         "routes": [{"id": "RT-c08", "kind": "import", "stage": "cloth", "eras": ["E2"]}]},
        {"id": "CMAT-09", "material": "hearth-dark",
         "maps_to": "10-materials MAT-10 hearth-dark (same slot and chemistry)",
         "routes": [{"id": "RT-c09", "kind": "local", "stage": "dye", "eras": ["E1", "E2"]}]},
        {"id": "CMAT-10", "material": "bog-iron (fixture only)",
         "maps_to": "10-materials MAT-99 nowhere (fixture-only dangling target)",
         "routes": [{"id": "RT-c10", "kind": "local", "stage": "trim", "eras": ["E2"]}]},
        {"id": "CMAT-11", "material": "smoke-cured hide (fixture only)", "slot": "wind-facing-outer",
         "maps_to": "10-materials MAT-10 hearth-dark (fixture: deliberate slot mismatch)",
         "routes": [{"id": "RT-c11", "kind": "local", "stage": "garment", "eras": ["E2"]}]},
    ]}
    target = {"id": "materials-MAT", "axis": "material", "records": [
        {"id": "MAT-07", "material": "lowland-broadcloth", "slot": "anchor-era-luxury",
         "excluded_eras": ["E1", "E2", "E3"],
         "routes": [{"id": "RT-m07", "kind": "import", "stage": "cloth", "eras": ["E4"]}]},
        {"id": "MAT-10", "material": "hearth-dark", "slot": "smoke-dark",
         "routes": [{"id": "RT-m10", "kind": "local", "stage": "dye", "eras": ["E1", "E2", "E3", "E4"]}]},
    ]}
    bridge = {"source_scope": "costumes-CMAT", "target_scope": target, "era_map": {"E2": "E4"},
              "target_era_scope": {"id": "materials-eras", "axis": "era",
                                   "tags": ["E1", "E2", "E3", "E4"], "names": {}}}
    to_verify_bridge = {"source_scope": "costumes-CMAT", "target_scope": target,
                        "era_map": {"E2": {"tag": "E4", "status": "to-verify", "scope": "slot", "row": "ERX-2"}}}
    base = [{"id": "GAR-01", "era": "E0", "material_ref": "wool"},
            {"id": "GAR-04", "era": "E1", "material_ref": "lowland plant-thread cloth"}]

    def run(claims, bridges=()):
        return reconcile_claims(claims, era_scope, material_scope, bridges=list(bridges))

    def codes(result, rid):
        for record in result["records"]:
            if record["record"] == rid:
                return sorted(f["code"] for f in record["findings"])
        return None

    result = run(base, [bridge])
    check("P1 own-scope claim is clean", codes(result, "GAR-01") == [], str(codes(result, "GAR-01")))
    check("P2 in-scope route claim is clean", codes(result, "GAR-04") == [], str(codes(result, "GAR-04")))
    check("P2b carried flag fires once for CMAT-08",
          [f["where"] for f in result["findings"] if f["code"] == R_MAT_CARRIED_FLAG] == ["CMAT-08"])
    check("P2c cross-scope slot conflict flags both records",
          sorted(f["where"] for f in result["findings"] if f["code"] == R_MAT_SLOT_CONFLICT)
          == ["CMAT-08", "MAT-07"])

    excluded = run([{"id": "GAR-04-E0", "era": "E0", "material_ref": "lowland plant-thread cloth"}])
    check("P3 excluded era rejects", codes(excluded, "GAR-04-E0") == [R_MAT_ERA_EXCLUDED],
          str(codes(excluded, "GAR-04-E0")))

    foreign = run([{"id": "GAR-SY", "era": "E4", "material_ref": "wool"}])
    check("P4 foreign era label system holds",
          codes(foreign, "GAR-SY") == [R_ERA_UNMAPPED, R_MAT_ERA_UNCHECKED],
          str(codes(foreign, "GAR-SY")))

    name_form = run([{"id": "GAR-NM", "era": "Open Grazing", "material_ref": "wool"}])
    check("P5 declared emic name resolves as a name form",
          codes(name_form, "GAR-NM") == [R_ERA_NAME_FORM], str(codes(name_form, "GAR-NM")))

    missing = run([{"id": "GAR-MX", "era": "E0", "material_ref": "linen"}])
    check("P6 unresolvable reference holds", codes(missing, "GAR-MX") == [R_MAT_UNRESOLVED],
          str(codes(missing, "GAR-MX")))

    translated = run([{"id": "GAR-TR", "era": "E0", "material_ref": "felt display name"}])
    check("P7 translated-label-only match holds",
          codes(translated, "GAR-TR") == [R_MAT_TRANSLATED], str(codes(translated, "GAR-TR")))

    cross = run([{"id": "GAR-XS", "era": "E2", "material_ref": "lowland-broadcloth"}], [bridge])
    check("P8 bridged cross-scope reference notes",
          codes(cross, "GAR-XS") == [R_MAT_CROSS_SCOPE], str(codes(cross, "GAR-XS")))

    no_bridge = run([{"id": "GAR-XS", "era": "E2", "material_ref": "lowland-broadcloth"}])
    check("P9 without the bridge the same reference holds",
          codes(no_bridge, "GAR-XS") == [R_MAT_UNRESOLVED], str(codes(no_bridge, "GAR-XS")))

    empty_map = run([{"id": "GAR-XS", "era": "E2", "material_ref": "lowland-broadcloth"}],
                    [{"source_scope": "costumes-CMAT", "target_scope": target, "era_map": {}}])
    check("P10 undeclared bridge mapping holds",
          codes(empty_map, "GAR-XS") == [R_ERA_BRIDGE_UNMAPPED, R_MAT_ERA_UNCHECKED],
          str(codes(empty_map, "GAR-XS")))

    once, twice = run(base, [bridge]), run(base, [bridge])
    check("P11 deterministic output",
          json.dumps(once, sort_keys=True, ensure_ascii=False)
          == json.dumps(twice, sort_keys=True, ensure_ascii=False))

    def raises(fragment, fn):
        try:
            fn()
        except ReconciliationError as exc:
            return fragment in str(exc)
        except Exception:
            return False
        return False

    check("N1 duplicate claim ids rejected",
          raises("duplicate record ids", lambda: run(base + [dict(base[0])])))
    check("N2 non-string era rejected",
          raises("expected a non-empty string",
                 lambda: run([{"id": "X", "era": 4, "material_ref": "wool"}])))
    check("N3 bad reference type rejected",
          raises("expected a string or mapping",
                 lambda: run([{"id": "X", "era": "E0", "material_ref": 4}])))
    check("N4 tagless era scope rejected",
          raises("non-empty tag list",
                 lambda: reconcile_claims(base, {"id": "bad", "axis": "era", "tags": []}, material_scope)))
    check("N5 era scope as bridge target rejected",
          raises("material scope",
                 lambda: run(base, [{"source_scope": "costumes-CMAT", "target_scope": era_scope,
                                     "era_map": {}}])))

    packet = {
        "eras": ["E0", "E1", "E2"],
        "era_records": [{"id": "ER-01", "tag": "E0", "name": "Open Grazing"}],
        "materials": [{"id": "CMAT-06", "material": "lowland plant-thread cloth",
                       "excluded_eras": ["E0"],
                       "routes": [{"id": "RT-c06", "kind": "import", "stage": "cloth",
                                   "eras": ["E1", "E2"]}]}],
        "costumes": [{"id": "GAR-04", "era": "E0", "material": "lowland plant-thread cloth"},
                     {"id": "GAR-05", "era": "E4", "material": "lowland plant-thread cloth"}],
    }
    before = json.dumps(packet, sort_keys=True)
    packet_result = reconcile_scoped(packet)
    packet_codes = {r["record"]: sorted(f["code"] for f in r["findings"]) for r in packet_result["records"]}
    check("P12 packet entry reproduces the GAR-04 E0 exclusion",
          packet_codes["GAR-04"] == [R_MAT_ERA_EXCLUDED], str(packet_codes["GAR-04"]))
    check("P13 packet entry holds the foreign E4 label system",
          packet_codes["GAR-05"] == [R_ERA_UNMAPPED, R_MAT_ERA_UNCHECKED], str(packet_codes["GAR-05"]))
    check("P14 packet era scope carries the emic name index with its row id",
          packet_result["scopes"]["era"] == "packet-eras"
          and era_scope_from_packet(packet)["names"] == {"Open Grazing": {"tag": "E0", "row": "ER-01"}})
    check("P15 input packet untouched", json.dumps(packet, sort_keys=True) == before)

    bridged_flags = run(base, [bridge])["findings"]
    bridged_missing = [f["where"] for f in bridged_flags if f["code"] == R_MAT_BRIDGE_MISSING]
    unbridged_missing = [f["where"] for f in run(base)["findings"] if f["code"] == R_MAT_BRIDGE_MISSING]
    check("P16 declared prose maps_to resolves under a bridge (and holds without one)",
          "CMAT-09" not in bridged_missing and "CMAT-09" in unbridged_missing,
          f"bridged={bridged_missing} unbridged={unbridged_missing}")
    check("P17 prose maps_to naming an absent target dangles",
          [f["where"] for f in bridged_flags if f["code"] == R_MAT_DANGLING] == ["CMAT-10"],
          str([f["where"] for f in bridged_flags if f["code"] == R_MAT_DANGLING]))
    check("N6 non-string maps_to rejected",
          raises("maps_to must be a string or null",
                 lambda: run(base, [{"source_scope": "costumes-CMAT", "era_map": {},
                                     "target_scope": {"id": "t", "axis": "material",
                                                      "records": [{"id": "MAT-10", "material": "hearth-dark",
                                                                   "maps_to": 7}]}}])))

    unconfirmed = run([{"id": "GAR-TV", "era": "E2", "material_ref": "lowland-broadcloth"}],
                      [to_verify_bridge])
    check("P18 to-verify mapping row holds and cites its row id",
          codes(unconfirmed, "GAR-TV") == [R_ERA_MAPPING_UNCONFIRMED, R_MAT_ERA_UNCHECKED]
          and any("ERX-2" in f["detail"] for f in unconfirmed["records"][0]["findings"]),
          str(codes(unconfirmed, "GAR-TV")))
    check("P19 two rows mapping one tag differently raise the conflict class",
          raises("mapping conflict",
                 lambda: run(base, [bridge, {"source_scope": "costumes-CMAT", "target_scope": target,
                                             "era_map": {"E2": "E1"}}])))
    check("P20 bridged slot mismatch holds",
          [f["where"] for f in bridged_flags if f["code"] == R_MAT_SLOT_MISMATCH] == ["CMAT-11"],
          str([f["where"] for f in bridged_flags if f["code"] == R_MAT_SLOT_MISMATCH]))

    verdict_codes = {(f["code"], f["verdict"], f["class"])
                     for f in excluded["records"][0]["findings"] + foreign["records"][0]["findings"]}
    check("P21 findings carry the spec verdict and class vocabulary",
          (R_MAT_ERA_EXCLUDED, "unavailable-by-closure", "D2L-MATERIAL") in verdict_codes
          and (R_ERA_UNMAPPED, "unmapped", "D2L-ERA") in verdict_codes, str(sorted(verdict_codes)))
    return checks

# ---------------------------------------------------------------------------
# Integration layer (R8-D02) — finding vocabulary, projection, CLI, selftest
# ---------------------------------------------------------------------------

ROOT = pathlib.Path(__file__).resolve().parent.parent
ERA_TAG_RE = re.compile("[^0-9A-Za-z]E[0-9](?![0-9])|^E[0-9](?![0-9])")
PACKET_DEFAULT = ROOT / "examples/culture-d2/packet.d2.yml"
PROJECTION_DEFAULT = ROOT / "examples/culture-d2/typed-labels.d2.yml"
READER = ROOT / "tools/gates/costume-era-consistency-gate.py"

# Design spec §6 finding vocabulary. Every shard code maps into it; an
# unmapped code is a defect in this table, not a silent pass.
D2L_BY_CODE = {
    "D2L-DATA": "D2L-DATA",
    "D2L-FORM-UNRESOLVED": "D2L-FORM-UNRESOLVED",
    "D2L-NATIVE": "D2L-NATIVE",
    "D2L-BORROW": "D2L-BORROW",
    "D2L-ERA": "D2L-ERA",
    "D2L-MATERIAL": "D2L-MATERIAL",
    "D2L-RANK": "D2L-RANK",
    "D2L-SCOPE": "D2L-SCOPE",
}
CODE_TO_D2L = {
    "E-PACKET": "D2L-DATA",
    "E-LABEL-ID": "D2L-DATA",
    "E-LABEL-KIND": "D2L-DATA",
    "E-LABEL-TYPE": "D2L-DATA",
    "E-LABEL-EMPTY": "D2L-DATA",
    "E-LABEL-SCRIPT": "D2L-DATA",
    "E-LABEL-LAYER-ORDER": "D2L-DATA",
    "E-LABEL-PATTERN-RISK": "D2L-DATA",
    "E-LABEL-TEMPLATE": "D2L-DATA",
    "E-LABEL-INVENTORY": "D2L-NATIVE",
    "W-LABEL-INVENTORY": "D2L-NATIVE",
    "E-LABEL-GLOSS": "D2L-FORM-UNRESOLVED",
    "W-LABEL-TOVERIFY": "D2L-FORM-UNRESOLVED",
    "E-LABEL-LAYER": "D2L-BORROW",
    "E-LABEL-ERA": "D2L-ERA",
    "E-LABEL-ERA-SCOPE": "D2L-ERA",
    "E-LABEL-MATERIAL": "D2L-MATERIAL",
    "E-LABEL-RANK-SHAPE": "D2L-DATA",
}
PREFIX_TO_D2L = (
    ("P-", "D2L-DATA"),
    ("R-ERA-", "D2L-ERA"),
    ("R-MAT-", "D2L-MATERIAL"),
    ("R-RANK-", "D2L-RANK"),
    ("R-SCOPE-", "D2L-SCOPE"),
)

HARD = ("fail", "reject", "hold", "error")


def d2l_id(code):
    """Map a shard finding code into the design spec's D2L-* vocabulary."""
    if code in D2L_BY_CODE:          # already in the spec vocabulary
        return code
    if code in CODE_TO_D2L:
        return CODE_TO_D2L[code]
    for prefix, mapped in PREFIX_TO_D2L:
        if code.startswith(prefix):
            return mapped
    raise Malformed("finding code %r has no D2L-* mapping; extend CODE_TO_D2L "
                    "rather than letting it pass unlabelled" % code)


def normalize_finding(code, where, detail, severity):
    return {"id": d2l_id(code), "code": code, "where": where,
            "detail": detail, "severity": severity}


# The written acute accent. 02-phonology.yml declares the accent pair by its
# written forms — "sara valley-locus [sára] versus sara ridge-locus [sará] —
# same segments, different peak" (02-phonology.yml:73) — so an acute vowel in a
# supplied native form is the component's declared accent mark, not a segment
# outside the inventory. The parser's segment check cannot tell the two apart,
# so the integration layer reclassifies those findings as HOLD and cites the
# declaration instead of letting them read as a broken inventory.
ACUTE_VOWELS = frozenset("áéíóú")


def reclassify_parser_finding(item):
    code = item.get("code")
    detail = item.get("detail", "")
    if code not in ("E-LABEL-INVENTORY", "W-LABEL-INVENTORY", "D2L-NATIVE"):
        return None
    marker = "outside the declared inventory: "
    if marker not in detail:
        return None
    try:
        import ast
        offenders = ast.literal_eval(detail.split(marker, 1)[1])
    except (ValueError, SyntaxError):
        return None
    if not isinstance(offenders, list) or not offenders:
        return None
    if not all(isinstance(sym, str) and len(sym) == 1 and sym in ACUTE_VOWELS
               for sym in offenders):
        return None
    return {"code": "D2L-NATIVE", "where": item.get("where", "<label>"),
            "detail": "%s — but the offending symbol(s) %s are acute-accented "
                      "vowels, the accent mark 02-phonology.yml declares by its own "
                      "minimal pair (02-phonology.yml:73 sara [sára] vs sara "
                      "[sará]); the segment inventory is not the test for a "
                      "diacritic, so this is held for the form's owner rather "
                      "than failed" % (detail, offenders),
            "severity": "hold"}


ALIAS_COMPONENT = "examples/culture-d2/components/12-rank-rules.yml"


def declared_era_aliases():
    """The alias map component 12 declares (A1: no silent aliasing)."""
    path = ROOT / ALIAS_COMPONENT
    if not path.exists():
        raise Malformed("missing %s; A1 cannot be recorded" % ALIAS_COMPONENT)
    loaded = load_packet_file(str(path))
    if loaded["packet"] is None:
        raise Malformed("cannot read %s: %s"
                        % (ALIAS_COMPONENT, loaded["findings"][:1]))
    aliases = loaded["packet"].get("era_aliases")
    if not isinstance(aliases, dict) or not aliases:
        raise Malformed("%s declares no era_aliases map (A1)" % ALIAS_COMPONENT)
    return dict(aliases)


COSTUME_COMPONENT = "examples/culture-d2/components/11-costumes.yml"


BLOCK_TOP_KEY = re.compile(r"^([A-Za-z_][\w-]*):")


def component_block(path, key):
    """One top-level block of a component file, via the frozen gate's reader.

    The lane's own assembler extracts component blocks this way
    (`tools/assemble-d2.py` `extract`); the reader is a stdlib YAML-subset
    parser, so a block scalar elsewhere in the file cannot block the read.
    """
    namespace = runpy.run_path(str(READER))
    parse = namespace["parse_packet"]
    malformed = namespace["Malformed"]
    lines = pathlib.Path(path).read_text(encoding="utf-8").splitlines(keepends=True)
    starts = [(index, match.group(1)) for index, line in enumerate(lines)
              if (match := BLOCK_TOP_KEY.match(line))]
    matches = [position for position, (_, name) in enumerate(starts) if name == key]
    if len(matches) != 1:
        raise Malformed("%s: expected exactly one top-level %r" % (path.name, key))
    position = matches[0]
    start = starts[position][0]
    end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
    try:
        block = parse("".join(lines[start:end]))
    except malformed as exc:
        raise Malformed("%s: %s" % (path.name, exc)) from exc
    value = block.get(key) if isinstance(block, dict) else None
    if not isinstance(value, (dict, list)) or not value:
        raise Malformed("%s: %r has no usable records" % (path.name, key))
    return value


def era_alias_rows():
    """Declared alias rows for `reconcile_era` (spec §2.2), read from the
    components — never guessed.

    Two sources, both on disk: 12-rank-rules.yml `era_aliases` (the legacy
    handles era-1..3 -> E0..E2, declared in that component's header, so
    `confirmed`) and 11-costumes.yml `era_reconciliation` (ERX-0/ERX-R
    `confirmed`; ERX-1..4 still `(to-verify)` -> `mapped-unconfirmed`). A row
    that maps one source label to two tags (ERX-3's declared two-to-one) is
    kept in `two_to_one` with its raw text rather than collapsed into a
    conflict verdict the component does not assert.
    """
    rows, two_to_one = [], []
    rules_path = ROOT / ALIAS_COMPONENT
    if rules_path.exists():
        loaded = load_packet_file(str(rules_path))
        if loaded["packet"] is None:
            raise Malformed("cannot read %s" % ALIAS_COMPONENT)
        for alias, tag in sorted((loaded["packet"].get("era_aliases") or {}).items()):
            rows.append({"id": "12-rank-rules era_aliases.%s" % alias,
                         "source": alias, "tag": tag, "status": "confirmed"})
    costumes_path = ROOT / COSTUME_COMPONENT
    if costumes_path.exists():
        # 11-costumes.yml carries a `|` block scalar (scope_note, line 16), which
        # the strict loader refuses by design (P-UNTERMINATED-FLOW). Only one
        # block is needed here, so it is read with the same block extractor the
        # lane's assembler uses for component files, and the loader's own
        # refusals stay exactly as delivered.
        shaped_rows, shaped_two_to_one = shape_reconciliation_rows(
            component_block(costumes_path, "era_reconciliation"))
        rows.extend(shaped_rows)
        two_to_one.extend(shaped_two_to_one)
    return rows, two_to_one


def shape_reconciliation_rows(declared):
    """The declared costume-era reconciliation rows as `reconcile_era` rows.

    One shaping for both sources: the D2 leg reads 11-costumes.yml with the
    block extractor above, and a packet that declares its own
    `era_reconciliation` table (round 20) is shaped by this same function, so a
    row means the same thing wherever it is declared. A row that maps one
    source label to two tags is kept in `two_to_one` with its raw text rather
    than collapsed into a conflict verdict the declaration does not assert.
    """
    rows, two_to_one = [], []
    for row in declared or []:
        if not isinstance(row, dict) or row.get("warning"):
            continue
        their = row.get("their_labels")
        if isinstance(their, dict):
            labels = [str(value) for value in their.values()]
        elif isinstance(their, str):
            labels = [their]
        else:
            continue
        tags = sorted(set(ERA_TAG_RE.findall(str(row.get("maps_to") or ""))))
        if not tags:
            continue
        status = ("confirmed" if "(to-verify)" not in str(row.get("status"))
                  else "to-verify")
        if len(tags) > 1:
            two_to_one.append({"id": row.get("id"), "sources": labels,
                               "tags": tags, "status": status,
                               "raw": row.get("maps_to")})
            continue
        for label in labels:
            rows.append({"id": row.get("id"), "source": label,
                         "tag": tags[0], "status": status})
    return rows, two_to_one


# ---- per-family alias leg (round 20, O claim) ----------------------------
#
# The round-19 routed wart: the era-alias leg hard-required
# examples/culture-d2/components/12-rank-rules.yml for every packet, so a D4
# run read the D2 tree and a faithful D4 mirror had to carry it. The leg now
# resolves per packet family: the D2 path above is the round-8 path, unchanged;
# every other family resolves the alias rules its own packet declares and, when
# the packet declares none, is skipped in the open — never aliased silently
# (A1) and never read from another family's tree.

DEFAULT_FAMILY = "d2"
D2_ERA_PROBES = ("E0", "era-1", "E1 shelter era", "E4 script era", "E9 no such label")
UNMAPPED_PROBE = "E9 no such label"
PACKET_ALIAS_KEYS = ("era_aliases", "named_eras", "era_records")


def packet_family(packet_path):
    """`d2` / `d4` / … from `examples/culture-<family>/…`; the D2 default else.

    The same convention `tools/gates/typed-pipeline-gate.py` `family_of` names.
    A packet outside that convention keeps the D2 default, so every
    pre-round-20 invocation resolves exactly as it did.
    """
    match = re.fullmatch(r"culture-([a-z0-9]+)",
                         pathlib.Path(packet_path).parent.name)
    return match.group(1) if match else DEFAULT_FAMILY


def shown_path(path):
    """The path as the projection reports it: repo-relative when inside ROOT."""
    try:
        return str(pathlib.Path(path).relative_to(ROOT))
    except ValueError:
        return str(path)


def validate_alias_pair(name, tag, where):
    if not isinstance(name, str) or not name.strip():
        raise Malformed("P-ERA-ALIAS at %s: alias name must be a non-empty string"
                        % where)
    if not isinstance(tag, str) or tag not in CONTRACT_ERAS:
        raise Malformed("P-ERA-ALIAS at %s: tag must be one of %s, got %r"
                        % (where, ", ".join(CONTRACT_ERAS), tag))


def packet_alias_rows(packet):
    """(aliases, rows, key) from the packet's own era-alias declaration.

    Three declared shapes are read, in this order: `era_aliases` (the D2-shaped
    label -> tag map), then the era-name record lists (`named_eras`,
    `era_records`), whose declared `name` -> `tag` pair is the family's own
    alias. Names must be non-empty strings and tags must be contract tags;
    malformed declarations raise P-ERA-ALIAS, never coerce or silently skip.
    `key` is None when no non-empty alias declaration is present.
    """
    if "era_aliases" in packet and not isinstance(packet["era_aliases"], dict):
        raise Malformed("P-ERA-ALIAS at era_aliases: expected a label-to-tag map")
    declared = packet.get("era_aliases")
    if declared:
        for label, tag in declared.items():
            validate_alias_pair(label, tag, "era_aliases.%s" % label)
        aliases = dict(declared)
        rows = [{"id": "packet era_aliases.%s" % label, "source": label,
                 "tag": aliases[label], "status": "confirmed"}
                for label in sorted(aliases)]
        return aliases, rows, "era_aliases"
    for key in ("named_eras", "era_records"):
        if key not in packet:
            continue
        records = packet[key]
        if not isinstance(records, list):
            raise Malformed("P-ERA-ALIAS at %s: expected an era-record list" % key)
        aliases, rows = {}, []
        for index, record in enumerate(records):
            where = "%s[%d]" % (key, index)
            if not isinstance(record, dict):
                raise Malformed("P-ERA-ALIAS at %s: expected an era record" % where)
            name, tag = record.get("name"), record.get("tag")
            validate_alias_pair(name, tag, where)
            if name in aliases and aliases[name] != tag:
                raise Malformed("P-ERA-ALIAS at %s: alias %r maps to different tags"
                                % (where, name))
            aliases[name] = tag
            rows.append({"id": "packet %s.%s" % (key, record.get("id", name)),
                         "source": name, "tag": tag, "status": "confirmed"})
        if rows:
            return aliases, rows, key
    return {}, [], None


def family_alias_leg(packet_path, packet):
    """The family's era-alias leg: aliases, rows, basis, probes, skips.

    D2 keeps the round-8 leg (`declared_era_aliases` + `era_alias_rows`, both
    reading the D2 components) byte for byte. Every other family resolves from
    its own packet, and each leg the packet does not declare is reported as a
    skip row rather than satisfied from a foreign tree.
    """
    family = packet_family(packet_path)
    if family == DEFAULT_FAMILY:
        rows, two_to_one = era_alias_rows()
        return {
            "family": family,
            "aliases": declared_era_aliases(),
            "rows": rows,
            "two_to_one": two_to_one,
            "basis": [
                "examples/culture-d2/components/12-rank-rules.yml era_aliases (A1)",
                "examples/culture-d2/components/11-costumes.yml era_reconciliation "
                "(ERX-0/ERX-R confirmed, ERX-1..4 (to-verify), ERX-W warning)",
            ],
            "probes": list(D2_ERA_PROBES),
            "skipped": [],
            "ledger_basis": (
                "examples/culture-d2/components/12-rank-rules.yml era_aliases (A1); "
                "the D2 records already use the canonical tags, so the map is "
                "identity for every rule emitted here"),
        }
    label = shown_path(packet_path)
    aliases, rows, key = packet_alias_rows(packet)
    skipped = []
    if key is not None:
        basis = ["%s %s (A1)" % (label, key)]
        ledger_basis = ("%s %s (A1); the normalized rank records already use the "
                        "canonical tags, so the map is identity for every rule "
                        "emitted here" % (label, key))
    else:
        basis = ["%s: no era-alias rules declared (%s) — skipped in the open, "
                 "never aliased silently (A1)"
                 % (label, ", ".join(PACKET_ALIAS_KEYS))]
        ledger_basis = ("%s: no era-alias rules declared (A1) — no alias map is "
                        "applied and none is imported from another family's tree; "
                        "the emitted rank records already use the canonical tags"
                        % label)
        skipped.append({"leg": "era-alias resolution", "source": label,
                        "why": "the packet declares none of %s"
                               % ", ".join(PACKET_ALIAS_KEYS)})
    declared = packet.get("era_reconciliation")
    two_to_one = []
    if isinstance(declared, list) and declared:
        shaped, two_to_one = shape_reconciliation_rows(declared)
        rows = rows + shaped
        basis.append("%s era_reconciliation (%d shaped rows)"
                     % (label, len(shaped)))
    else:
        basis.append("%s era_reconciliation: skipped — the packet declares no "
                     "reconciliation rows (the D2 leg's "
                     "examples/culture-d2/components/11-costumes.yml is not read "
                     "for family %s)" % (label, family))
        skipped.append({"leg": "costume-era reconciliation", "source": label,
                        "why": "the packet declares no era_reconciliation rows"})
    probes = (sorted({row["tag"] for row in rows})[:2]
              + sorted({row["source"] for row in rows})[:2]
              + [UNMAPPED_PROBE])
    return {"family": family, "aliases": aliases, "rows": rows,
            "two_to_one": two_to_one, "basis": basis, "probes": probes,
            "skipped": skipped, "ledger_basis": ledger_basis}


def sha256_file(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def validate_family_provenance(value, packet_path, metadata, where):
    components = {pair[1] for key, pair in metadata.items() if key != "scheme"}
    components.add(shown_path(packet_path) if packet_path else "packet")
    owners = {pair[0] for key, pair in metadata.items() if key != "scheme"}

    def walk(item, location):
        if isinstance(item, dict):
            for field, child in item.items():
                here = "%s.%s" % (location, field)
                if field in ("component", "cite", "citation", "source_path", "source_file"):
                    path = re.split(r"[:#]", child, maxsplit=1)[0] if isinstance(child, str) else None
                    if path not in components:
                        raise Malformed("P-FAMILY-SOURCE at %s: citation is not family-owned: %r"
                                        % (here, child))
                if field == "owner" and child not in owners:
                    raise Malformed("P-FAMILY-SOURCE at %s: foreign owner %r" % (here, child))
                if field == "scheme" and child is not None and child != metadata["scheme"]:
                    raise Malformed("P-FAMILY-SOURCE at %s: foreign scheme %r" % (here, child))
                walk(child, here)
        elif isinstance(item, list):
            for index, child in enumerate(item):
                walk(child, "%s[%d]" % (location, index))
    walk(value, where)


def validate_family_labels(packet_path, packet, labels, family):
    metadata = family_label_metadata(packet, family, packet_path)
    fields = {"garment": "costumes", "form_slot": "form_slots",
              "term": "lexicon", "name": "names", "text": "typed_labels"}
    for label in labels:
        where = "typed_labels.%s" % label.get("id", "?")
        validate_family_provenance(label, packet_path, metadata, where)
        source = label.get("source")
        if not isinstance(source, dict):
            raise Malformed("P-FAMILY-SOURCE at %s: a qualified source is required" % where)
        block = fields.get(source.get("field"))
        records = packet.get(block) if block else None
        record = next((row for row in records or [] if isinstance(row, dict)
                       and row.get("id") == source.get("record")), None)
        if record is None or label.get("id") != source.get("record"):
            raise Malformed("P-FAMILY-SOURCE at %s: source record/field does not resolve" % where)
        if block == "typed_labels":
            if (source.get("component") != (shown_path(packet_path) if packet_path else "packet")
                    or source.get("block") != block):
                raise Malformed("P-FAMILY-SOURCE at %s: explicit label needs packet/typed_labels source" % where)
            if label.get("owner") not in {metadata[key][0] for key in fields.values()
                                           if key != "typed_labels"}:
                raise Malformed("P-FAMILY-SOURCE at %s: explicit label owner is not local" % where)
        else:
            owner, component = metadata[block]
            if label.get("owner") != owner or source.get("component") != component:
                raise Malformed("P-FAMILY-SOURCE at %s: owner/component does not own this field" % where)
            expected = None if block == "form_slots" else record.get(source["field"])
            if label.get("text") != expected:
                raise Malformed("P-FAMILY-SOURCE at %s: text differs from the family source" % where)
            if block in ("costumes", "form_slots"):
                slot = record.get("id") if block == "form_slots" else record.get("form_slot")
                match = _SLOT_RE.search(slot) if isinstance(slot, str) else None
                if not match or label.get("label_id") != match.group(0):
                    raise Malformed("P-FAMILY-SOURCE at %s: owed slot is missing or foreign" % where)
        if label.get("kind") in SOUND_KINDS and label.get("scheme") != metadata["scheme"]:
            raise Malformed("P-FAMILY-SOURCE at %s: supplied form needs the declared scheme" % where)


def family_rank_payload(packet_path, packet, family):
    import copy
    metadata = family_label_metadata(packet, family, packet_path)
    source_path = shown_path(packet_path)
    records = packet.get("rank_rules", [])
    if not isinstance(records, list):
        raise Malformed("P-FAMILY-RANK: rank_rules must be a record list")
    ledger = {key: [] for key in ("normalized_rules", "gate_rank_rules", "act_rules",
              "residuals", "unresolved", "quarantine", "calibration_flags",
              "entitlement_edges", "jurisdiction_gaps", "assay_gaps")}
    seen = set()
    for index, record in enumerate(records):
        where = "rank_rules[%d]" % index
        if not isinstance(record, dict):
            raise Malformed("P-FAMILY-RANK at %s: expected a mapping" % where)
        rid = record.get("id")
        if not isinstance(rid, str) or not _LABEL_ID_RE.fullmatch(rid) or rid in seen:
            raise Malformed("P-FAMILY-RANK at %s: invalid or duplicate id %r" % (where, rid))
        seen.add(rid)
        validate_family_provenance(record, packet_path, metadata, where)
        if "source" in record:
            source = record["source"]
            if (not isinstance(source, dict) or source.get("block") != "rank_rules"
                    or source.get("component") not in (source_path, metadata["costumes"][1])
                    or source.get("record_id", source.get("record")) != rid):
                raise Malformed("P-FAMILY-SOURCE at %s: source must identify this rank record" % where)
        for field in ("authority", "jurisdiction", "effect"):
            if (not isinstance(record.get(field), str)
                    or record[field].strip().lower() in ("", "null", "none", "~")):
                raise Malformed("P-FAMILY-RANK at %s: missing %s" % (where, field))
        eras = record.get("eras")
        if (not isinstance(eras, list) or not eras or
                any(not isinstance(era, str) or era not in packet.get("eras", []) for era in eras)):
            raise Malformed("P-FAMILY-RANK at %s: eras must name declared packet tags" % where)
        prop = record.get("property")
        if not isinstance(prop, dict) or any(not isinstance(prop.get(key), str)
                                            or not prop[key].strip() for key in ("kind", "value")):
            raise Malformed("P-FAMILY-RANK at %s: property.kind/value required" % where)
        for field in ("wearer_ranks", "exempt_ranks", "rites", "garment_refs"):
            value = record.get(field, [])
            if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
                raise Malformed("P-FAMILY-RANK at %s: %s must be a string list" % (where, field))
        costume_ids = {row.get("id") for row in packet.get("costumes", []) if isinstance(row, dict)}
        if any(ref not in costume_ids for ref in record.get("garment_refs", [])):
            raise Malformed("P-FAMILY-SOURCE at %s: garment_refs names a foreign record" % where)
        normalized = copy.deepcopy(record)
        normalized["source"] = {"component": source_path, "block": "rank_rules",
                                "record_id": rid, "field": "rank_rules"}
        unsupported = []
        if prop["kind"] not in GATE_PROPERTY_KINDS:
            unsupported.append("property kind %r is outside the gate model" % prop["kind"])
        if record["effect"] not in ("permit", "prohibit", "require"):
            unsupported.append("effect %r has no packet-native gate mapping" % record["effect"])
        normalized["adapt_status"] = "cannot-evaluate" if unsupported else "executable"
        normalized["unresolved"] = unsupported
        if record["effect"] == "require":
            normalized["effect"] = "obligate"
        ledger["normalized_rules"].append(normalized)
        ledger["unresolved"].extend({"rule": rid, "item": item} for item in unsupported)
        if not unsupported:
            gate = copy.deepcopy(record)
            gate.update({"id": rid + "#g", "source_rule": rid,
                         "source": dict(normalized["source"]), "adapt_status": "executable"})
            ledger["gate_rank_rules"].append(gate)
    for field in ("normalized_rules", "gate_rank_rules"):
        ledger[field].sort(key=lambda row: row["id"])
    ledger["coverage"] = {"component_rules": len(records), "normalized": len(records),
                          "gate_projected": len(ledger["gate_rank_rules"]), "partitioned": True}
    ledger["skipped"] = [{"leg": "D2 prose-rank adapter and residual tables", "source": source_path,
                           "why": "packet-native rank rules only; no foreign fixture data is imported"}]
    if not records:
        ledger["skipped"].append({"leg": "rank-rule projection", "source": source_path,
                                  "why": "the packet declares no rank_rules"})
    return ledger


def family_rank_conflicts(records):
    findings = []
    for index, first in enumerate(records):
        for second in records[index + 1:]:
            if (first["property"] != second["property"]
                    or {first["effect"], second["effect"]} != {"permit", "prohibit"}
                    or not set(first["eras"]) & set(second["eras"])):
                continue
            a, b = first.get("rites", []), second.get("rites", [])
            if a and b and not set(a) & set(b):
                continue
            a, b = set(first.get("wearer_ranks", [])), set(second.get("wearer_ranks", []))
            excluded = set(first.get("exempt_ranks", [])) | set(second.get("exempt_ranks", []))
            if a and b and not (a & b) - excluded:
                continue
            if (a or b) and not ((a & b) if a and b else a or b) - excluded:
                continue
            findings.append({"class": "declared-rank-overlap", "pair": [first["id"], second["id"]],
                             "triage": {"status": "untriaged-family-local",
                                        "why": "declared scopes may overlap; no prose jurisdiction priority inferred"}})
    return findings


def validate_family_projection(packet_path, packet, projection):
    family = packet_family(packet_path)
    if family == DEFAULT_FAMILY:
        return
    metadata = family_label_metadata(packet, family, packet_path)
    validate_family_labels(packet_path, packet, projection["typed_labels"]["labels"], family)
    ledger = projection["rank_rules"]
    expected = family_rank_payload(packet_path, packet, family)
    for field in ("normalized_rules", "gate_rank_rules", "act_rules", "residuals", "unresolved",
                  "quarantine", "calibration_flags", "entitlement_edges", "jurisdiction_gaps", "assay_gaps", "coverage"):
        validate_family_provenance(ledger[field], packet_path, metadata, "rank_rules." + field)
        if ledger[field] != expected[field]:
            raise Malformed("P-FAMILY-SOURCE at rank_rules.%s: differs from packet-native records" % field)
    local_ids = {label["id"] for label in projection["typed_labels"]["labels"]}
    local_ids.update(row["id"] for row in ledger["normalized_rules"])
    local_ids.update(row["id"] for row in ledger["gate_rank_rules"])
    for finding in projection["findings"]:
        if not set(str(finding["where"]).split("|")) <= local_ids:
            raise Malformed("P-FAMILY-SOURCE at findings: record is outside the family view")


def run_pipeline(packet_path):
    """Run every capability over one packet; return the projection document."""
    packet_path = pathlib.Path(packet_path)
    loaded = load_packet_file(str(packet_path))
    findings = [normalize_finding(item.get("code", "P-IO"),
                                  item.get("where", str(packet_path)),
                                  item.get("detail", ""), "fail")
                for item in loaded["findings"]]
    if loaded["packet"] is None:
        return {"exit": 2, "projection": None, "findings": findings,
                "json_document": {"exit_code": 2, "ok": False,
                                  "packet": str(packet_path),
                                  "stats": {"fail": len(findings), "hold": 0,
                                            "labels": 0},
                                  "findings": findings}}
    packet = loaded["packet"]
    family = packet_family(packet_path)
    parse_result = parse_typed_labels(packet, family=family, packet_path=packet_path)
    for item in parse_result["findings"]:
        reclassified = reclassify_parser_finding(item) if family == DEFAULT_FAMILY else None
        if reclassified is not None:
            findings.append(normalize_finding(reclassified["code"],
                                              reclassified["where"],
                                              reclassified["detail"],
                                              reclassified["severity"]))
            continue
        findings.append(normalize_finding(item["code"], item.get("where", "<label>"),
                                          item.get("detail", ""),
                                          item.get("kind", "fail")))
    ledger = (build_payload() if family == DEFAULT_FAMILY else
              family_rank_payload(packet_path, packet, family))
    leg = family_alias_leg(packet_path, packet)
    aliases = leg["aliases"]
    era_verdicts = [
        dict(reconcile_era(label, leg["rows"]), label=label)
        for label in leg["probes"]
    ]
    ledger["era_aliases_applied"] = aliases
    ledger["era_aliases_basis"] = leg["ledger_basis"]
    for rule in ledger["normalized_rules"]:
        shaped = dict(rule)
        shaped.setdefault("era_aliases_applied", aliases)
        for problem in check_rank_rule_shape(shaped) or []:
            findings.append(normalize_finding(
                "E-LABEL-RANK-SHAPE", rule.get("id", "?"),
                "normalized rule shape rejected by the parser-side check: %s"
                % problem, "hold"))
    if family == DEFAULT_FAMILY:
        conflict_list = conflicts(ledger["gate_rank_rules"])
        act_list = act_conflicts(ledger["act_rules"])
    else:
        conflict_list = family_rank_conflicts(ledger["gate_rank_rules"])
        act_list = []
        for item in ledger["unresolved"]:
            findings.append(normalize_finding("R-RANK-UNSUPPORTED", item["rule"], item["item"], "hold"))
    for item in conflict_list + act_list:
        triage = item.get("triage") or {}
        findings.append(normalize_finding(
            "R-RANK-CONFLICT", "|".join(item["pair"]),
            "%s: %s" % (item["class"], triage.get("status", "UNTRIAGED")),
            "hold" if family != DEFAULT_FAMILY or triage.get("status") == "genuine-priority-gap" else "note"))
    reconciliation = reconcile_scoped(packet)
    for record in reconciliation["records"]:
        for item in record["findings"]:
            if item["severity"] == "ok":
                continue
            findings.append(normalize_finding(
                item["code"], record["record"], item["detail"], item["severity"]))
    findings.sort(key=lambda f: (f["id"], f["code"], str(f["where"]), f["detail"]))
    hard = [f for f in findings if f["severity"] in HARD]
    exit_code = 2 if any(f["id"] == "D2L-DATA" for f in findings) else (1 if hard else 0)
    coverage = {
        "typed_labels": parse_result["stats"]["labels"],
        "labels_by_kind": {
            kind: sum(1 for label in parse_result["labels"] if label["kind"] == kind)
            for kind in sorted(KINDS)},
        "label_findings_fail": parse_result["stats"]["fail"],
        "label_findings_hold": parse_result["stats"]["hold"],
        "rank_rules_component": ledger["coverage"]["component_rules"],
        "rank_rules_normalized": ledger["coverage"]["normalized"],
        "rank_rules_gate_projected": ledger["coverage"]["gate_projected"],
        "rank_rules_unresolved_items": len(ledger["unresolved"]),
        "rank_quarantine_handles": len(ledger["quarantine"]),
        "reconciliation_records": len(reconciliation["records"]),
        "conflicts": len(conflict_list) + len(act_list),
        "findings_total": len(findings),
        "findings_hold_or_fail": len(hard),
    }
    shown = shown_path(packet_path)
    era_block = {
        "alias_rows": leg["rows"],
        "two_to_one": leg["two_to_one"],
        "verdicts": era_verdicts,
        "basis": leg["basis"],
        "note": "a (to-verify) row yields mapped-unconfirmed (hold); a label "
                "no row names stays unmapped — the E-number is never a mapping",
    }
    if leg["skipped"]:
        era_block["skipped"] = leg["skipped"]
    projection = {
        "name": "%s typed labels, scoped reconciliation and adapted rank rules "
                "(derived projection, non-canon)" % family.upper(),
        "canon": "not canonized (%s design drill); derived view of %s" % (family.upper(), shown),
        "generator": "tools/d2-typed-labels.py",
        "label_kinds": list(KINDS),
        "typed_labels": {"stats": parse_result["stats"], "labels": parse_result["labels"]},
        "era_material_reconciliation": reconciliation,
        "era_reconciliation": era_block,
        "rank_rules": ledger,
        "findings": findings,
        "coverage": coverage,
        "assembly": {
            "packet": shown,
            "packet_sha256": sha256_file(packet_path),
            "reader": "tools/gates/costume-era-consistency-gate.py",
            "reader_sha256": sha256_file(READER) if READER.exists() else None,
            "shard_blocks": [
                "R8-D03 §4.1 strict_loader", "R8-D03 §4.2 label_parser",
                "R8-D04 §4 rank_adapter", "R8-D05 §4 era_material"],
            "schema_basis": [
                "reports/round-8/depth/design-spec.md (R8-D01)",
                "reports/round-8/depth/shard-parser.md (R8-D03)",
                "reports/round-8/depth/shard-rank.md (R8-D04)",
                "reports/round-8/depth/shard-era-material.md (R8-D05)",
                "corpus/knowledge/synthesis/glossary-registry-format.md §1-4",
                "corpus/knowledge/synthesis/loanword-material-dating.md",
                "corpus/knowledge/synthesis/era-language-staging.md"],
            "notes": [
                "read-only over components, packet and gates; the packet is never "
                "rewritten",
                "no CE dates are synthesized (design-spec §2.2 E7)",
                "a (to-verify) row is held, never promoted (E5)",
            ],
        },
    }
    validate_family_projection(packet_path, packet, projection)
    document = {"exit_code": exit_code, "ok": exit_code == 0,
                "packet": shown,
                "stats": {"fail": sum(1 for f in findings
                                      if f["severity"] in ("fail", "error")),
                          "hold": sum(1 for f in findings
                                      if f["severity"] in ("hold", "reject")),
                          "note": sum(1 for f in findings
                                      if f["severity"] == "note"),
                          "labels": parse_result["stats"]["labels"]},
                "findings": findings}
    return {"exit": exit_code, "projection": projection, "findings": findings,
            "json_document": document}


def serialize(projection):
    """Deterministic bytes: sorted keys, LF, no host paths, no timestamps."""
    return (json.dumps(projection, sort_keys=True, indent=2, ensure_ascii=False)
            + "\n").encode("utf-8")


def report(result, stream=sys.stdout):
    """Human report: findings first, then the coverage counts."""
    for item in result["findings"]:
        print("FINDING %s: [%s] %s — %s"
              % (item["id"], item["severity"], item["where"], item["detail"]),
              file=stream)
    coverage = result["projection"]["coverage"] if result["projection"] else {}
    if coverage:
        print("coverage: " + ", ".join("%s=%s" % (key, coverage[key])
                                       for key in sorted(coverage)), file=stream)
        print("labels by kind: " + ", ".join(
            "%s=%d" % (kind, count)
            for kind, count in sorted(coverage["labels_by_kind"].items())), file=stream)
    return result["exit"]


def _selftest_family(check):
    import copy
    from unittest.mock import patch
    path = ROOT / "examples/culture-d4/packet.d4.yml"
    packet = load_packet_file(path)["packet"]
    current = run_pipeline(path)["projection"]
    before = parse_typed_labels(packet)["labels"]
    labels = current["typed_labels"]["labels"]
    identity = lambda rows: [(row["id"], row["kind"], row["text"], row["label_id"], row.get("borrow")) for row in rows]
    check("boundary: label texts, kinds, owed slots and all six borrow ledgers unchanged",
          identity(labels) == identity(before) and sum(row["kind"] == "borrowed-strata" for row in labels) == 6)
    check("boundary: D4 owners and declared romanization replace D2 metadata",
          {row["owner"] for row in labels} == {"09-costumes", "04-lexicon", "05-naming"}
          and all(row["scheme"] == packet["orthography"]["scheme"] for row in labels if row["kind"] in SOUND_KINDS))
    check("boundary: D4 metadata and local rank census",
          current["name"].startswith("D4 ") and "D4 design drill" in current["canon"]
          and current["rank_rules"]["coverage"] == {"component_rules": 4, "normalized": 4, "gate_projected": 4, "partitioned": True})
    check("boundary: only the twelve owed-form holds remain",
          len(current["findings"]) == 12 and all(row["id"] == D2L_FORM and row["severity"] == "hold" for row in current["findings"]))
    missing_slot = copy.deepcopy(labels[0])
    missing_slot["label_id"] = None
    check("boundary: the D4 owner does not bypass the costume-slot requirement",
          any(row["code"] == D2L_DATA and "no label_id" in row["detail"]
              for row in validate_labels([missing_slot], packet)[0]))
    synthetic = copy.deepcopy(current)
    synthetic["typed_labels"]["labels"] = before
    try:
        validate_family_projection(path, packet, synthetic)
        refused = False
    except Malformed:
        refused = True
    check("boundary control: deterministic D2-owned label metadata is rejected", refused)
    for field, value in (("component", str(ROOT / ALIAS_COMPONENT)), ("component", "12-rank-rules.yml:212"),
                         ("owner", "11-costumes"), ("scheme", "d2-roman")):
        contaminated = copy.deepcopy(labels[0])
        if field == "component":
            contaminated["source"][field] = value
        else:
            contaminated[field] = value
        try:
            validate_family_labels(path, packet, [contaminated], "d4")
            refused = False
        except Malformed as exc:
            refused = "P-FAMILY-SOURCE" in str(exc)
        check("boundary control: foreign label %s %r rejected" % (field, value), refused)
    method_packet = copy.deepcopy(packet)
    method_packet["orthography"]["writing_rules"] = [{"id": "WR-01", "tool": "tools/d2-typed-labels.py"}]
    try:
        validate_family_projection(path, method_packet, current)
        accepted = True
    except Malformed:
        accepted = False
    check("boundary: D4 WR writing ids and shared engine references are not substring-banned", accepted)
    with tempfile.TemporaryDirectory(prefix="family-clean-") as tmp:
        mirror = pathlib.Path(tmp) / "repo"
        (mirror / "tools/gates").mkdir(parents=True)
        (mirror / "examples/culture-d4").mkdir(parents=True)
        for source, target in ((pathlib.Path(__file__), mirror / "tools/d2-typed-labels.py"),
                               (READER, mirror / "tools/gates/costume-era-consistency-gate.py"),
                               (path, mirror / "examples/culture-d4/packet.d4.yml")):
            shutil.copyfile(source, target)
        ns = runpy.run_path(str(mirror / "tools/d2-typed-labels.py"))
        globals_ = ns["run_pipeline"].__globals__
        mirror_path = mirror / "examples/culture-d4/packet.d4.yml"
        local = ns["run_pipeline"](mirror_path)["projection"]
        check("boundary: packet-only D4 mirror is byte-identical without a foreign tree",
              ns["serialize"](local) == serialize(current) and not (mirror / "examples/culture-d2").exists())
        def poison(*args, **kwargs):
            raise AssertionError("D2 fixture machinery invoked")
        hooks = ("build_payload", "project_to_gate", "resolve_costume_rank", "conflicts",
                 "act_conflicts", "entitlement_conflicts")
        with patch.dict(globals_, {name: poison for name in hooks}):
            poisoned = ns["run_pipeline"](mirror_path)["projection"]
        check("boundary poison control: D4 never calls embedded D2 fixture machinery",
              ns["serialize"](poisoned) == ns["serialize"](local))
        text = mirror_path.read_text(encoding="utf-8")
        def write_rules(rows):
            block = "rank_rules:" + ("\n" + "".join("  - " + json.dumps(row, ensure_ascii=False) + "\n" for row in rows) if rows else " []\n")
            mirror_path.write_text(re.sub(r"^rank_rules:\n.*?(?=^\S)", lambda match: block, text, count=1, flags=re.M | re.S), encoding="utf-8")
        changed = copy.deepcopy(packet["rank_rules"])
        changed[0].update(authority="the local probe charter", property={"kind": "material", "value": "probe hide"}, wearer_ranks=["probe-smith"])
        write_rules(changed)
        mutation = ns["run_pipeline"](mirror_path)["projection"]
        check("boundary local control: RK-01 authority/property/rank follow the local packet only",
              mutation["rank_rules"]["normalized_rules"][0]["authority"] == "the local probe charter"
              and mutation["rank_rules"]["gate_rank_rules"][0]["property"] == changed[0]["property"]
              and mutation["rank_rules"]["gate_rank_rules"][0]["wearer_ranks"] == ["probe-smith"]
              and mutation["rank_rules"]["normalized_rules"][1:] == local["rank_rules"]["normalized_rules"][1:]
              and mutation["typed_labels"] == local["typed_labels"] and mutation["findings"] == local["findings"])
        extra = copy.deepcopy(packet["rank_rules"][0]); extra["id"] = "RK-99"
        for label, rows, count in (("add", packet["rank_rules"] + [extra], 5), ("remove", packet["rank_rules"][1:], 3), ("absent", [], 0)):
            write_rules(rows)
            result = ns["run_pipeline"](mirror_path)["projection"]
            check("boundary coverage control: %s local row counted exactly once" % label,
                  result["coverage"]["rank_rules_component"] == count and result["coverage"]["rank_rules_gate_projected"] == count)
        unsupported = copy.deepcopy(packet["rank_rules"]); unsupported[0]["property"]["kind"] = "unmodelled-local-property"
        write_rules(unsupported)
        held = ns["run_pipeline"](mirror_path)["projection"]
        check("boundary limitation: an unsupported local property is held, not evaluated",
              held["coverage"]["rank_rules_gate_projected"] == 3 and held["coverage"]["rank_rules_unresolved_items"] == 1
              and any(row["where"] == "RK-01" and row["severity"] == "hold" for row in held["findings"]))
        prohibition = copy.deepcopy(extra); prohibition["effect"] = "prohibit"
        write_rules(packet["rank_rules"] + [prohibition])
        conflict = ns["run_pipeline"](mirror_path)["projection"]
        check("boundary conflict control: local prohibition is not inverted through D2 licenses",
              conflict["rank_rules"]["gate_rank_rules"][-1]["wearer_ranks"] == prohibition["wearer_ranks"]
              and conflict["coverage"]["conflicts"] == 1 and any(row["where"] == "RK-01#g|RK-99#g" and row["severity"] == "hold" for row in conflict["findings"]))
        malformed = [packet["rank_rules"] + [packet["rank_rules"][0]], [None]]
        for field, value in (("authority", None), ("property", []), ("eras", ["E9"]),
                             ("wearer_ranks", "smith"), ("cite", "12-rank-rules.yml:212"),
                             ("source", {"component": str(ROOT / ALIAS_COMPONENT), "record_id": "RK-01", "block": "rank_rules"})):
            row = copy.deepcopy(packet["rank_rules"][0]); row[field] = value; malformed.append([row])
        for index, rows in enumerate(malformed):
            write_rules(rows)
            try:
                ns["run_pipeline"](mirror_path)
                refused = False
            except ns["Malformed"] as exc:
                refused = "P-FAMILY-" in str(exc)
            check("boundary malformed local rank set %d fails closed" % (index + 1), refused)
        mirror_path.write_text(text, encoding="utf-8")
        contaminated = copy.deepcopy(labels[0])
        contaminated["source"]["component"] = str(ROOT / COSTUME_COMPONENT)
        mirror_path.write_text(text + "\ntyped_labels:\n  - " + json.dumps(contaminated) + "\n", encoding="utf-8")
        target = mirror / "output.yml"
        for existing in (False, True):
            if existing:
                target.write_bytes(b"sentinel\n")
            proc = subprocess.run([sys.executable, str(mirror / "tools/d2-typed-labels.py"), "--packet", str(mirror_path), "--emit", str(target)], capture_output=True, text=True, cwd=mirror)
            check("boundary explicit same-id foreign label: emit refuses and preserves %s output" % ("existing" if existing else "absent"),
                  proc.returncode == 2 and "P-FAMILY-SOURCE" in proc.stderr and (target.read_bytes() == b"sentinel\n" if existing else not target.exists()))
        shutil.copytree(ROOT / "examples/culture-d2", mirror / "examples/culture-d2")
        d2path = mirror / "examples/culture-d2/packet.d2.yml"
        d2 = ns["run_pipeline"](d2path)["projection"]
        check("boundary compatibility: D2 projection keeps its exact baseline digest",
              hashlib.sha256(ns["serialize"](d2)).hexdigest() == "a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43")
        normalized = copy.deepcopy(globals_["NORMALIZED"]); normalized[0]["authority"] = "D2 mutation control"
        with patch.dict(globals_, {"NORMALIZED": normalized}):
            mutated = ns["run_pipeline"](d2path)["projection"]
        check("boundary D2 control: D2 rank projection remains enabled and responds to D2 mutation",
              mutated["rank_rules"]["normalized_rules"][0]["authority"] == "D2 mutation control" and ns["serialize"](mutated) != ns["serialize"](d2))


def selftest():
    """Control matrix: shards, malformed cases, family boundaries, CLI tamper."""
    passed, failed = [], []

    def check(label, condition, detail=""):
        (passed if condition else failed).append(label)
        print("%s %s%s" % ("ok  " if condition else "FAIL", label,
                           "" if condition else " — %s" % detail))

    def codes(result):
        return sorted({f["code"] for f in result["findings"]})

    def ns_packet(result):
        loaded = load_packet_file(str(PACKET_DEFAULT))
        if loaded["packet"] is None:
            raise Malformed("selftest: live packet unreadable")
        return loaded["packet"]

    # ---- 1. the three shard blocks' own control matrices ----------------
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        rank_rc = selftest_rank_block()
    check("rank adapter block: its own controls pass", rank_rc == 0,
          buffer.getvalue().strip().splitlines()[-1] if buffer.getvalue() else "")
    era_results = _selftest_era_material()
    era_bad = [label for label, ok, _ in era_results if not ok]
    check("era/material block: its own controls pass (%d)" % len(era_results),
          not era_bad, "; ".join(era_bad))

    # ---- 2. loader and parser controls (design-spec §5 D4 malformed) ----
    def load(text, **kw):
        return load_packet_strict(text, **kw)

    cases = (
        ("P-UNTERMINATED-FLOW", "phonology:\n  consonants: [p, t, k\n"),
        ("P-DUPLICATE-KEY", "name: a\nphonology:\n  tones: 0\nphonology:\n  tones: 1\n"),
        ("P-ANCHOR-TAG", "name: *tag\n"),
        ("P-TAB-INDENT", "name: a\nphonology:\n\ttones: 0\n"),
        ("P-EMPTY", ""),
    )
    for code, text in cases:
        loaded = load(text)
        got = sorted({item["code"] for item in loaded["findings"]})
        check("loader: %s refused" % code, code in got, str(got))
    deep = "phonology:\n  consonants: [" + "[" * 3000
    loaded = load(deep)
    check("loader: P-DEPTH-CAP refused without traceback",
          "P-DEPTH-CAP" in {item["code"] for item in loaded["findings"]},
          str(sorted({item["code"] for item in loaded["findings"]})))

    # ---- 3. the spec's positive cases on the live packet ----------------
    packet_path = PACKET_DEFAULT
    if packet_path.exists():
        result = run_pipeline(packet_path)
        check("live packet: pipeline evaluates (exit 0/1, never 2)",
              result["exit"] in (0, 1), "exit=%s" % result["exit"])
        projection = result["projection"] or {}
        labels = projection.get("typed_labels", {}).get("labels", [])
        costumes = [label for label in labels
                    if label.get("owner") == "11-costumes"]
        check("live packet: the ten GAR costume labels are typed translated-label",
              len(costumes) == 10 and all(l["kind"] == "translated-label"
                                          for l in costumes),
              "%d labels, kinds %s" % (len(costumes),
                                       sorted({l["kind"] for l in costumes})))
        check("live packet: each GAR label keeps its owed form slot (LEX-GAR-0x)",
              all(str(l.get("label_id", "")).startswith("LEX-GAR-")
                  for l in costumes),
              json.dumps([l.get("label_id") for l in costumes]))
        held_forms = [label for label in labels if label.get("status") == "to-verify"]
        check("live packet: the owed form slots stay held, never passed",
              len(held_forms) >= 10, "%d to-verify labels" % len(held_forms))
        check("live packet: no GAR label is graded on the sound channel",
              not any(f["code"] in ("E-LABEL-INVENTORY", "W-LABEL-INVENTORY")
                      for f in result["findings"]),
              str(codes(result)))
        lexicon = [label for label in labels if label["kind"] == "borrowed-strata"]
        check("live packet: the two loan records are typed borrowed-strata",
              len(lexicon) == 2, "%d borrowed labels" % len(lexicon))
        check("live packet: loan ledger keeps the layer reference",
              all(label.get("borrow", {}).get("layer_ref") for label in lexicon)
              if lexicon and "borrow" in (lexicon[0] if lexicon else {}) else
              all(label.get("layer_ref") for label in lexicon),
              json.dumps(lexicon[:1], ensure_ascii=False)[:200])
        ledger = projection.get("rank_rules", {})
        check("live packet: every component rule is partitioned exactly",
              ledger.get("coverage", {}).get("partitioned") is True,
              json.dumps(ledger.get("coverage", {})))
        check("live packet: no rule is silently executable (adapt_status present)",
              all(rule.get("adapt_status") in ("executable", "partial", "cannot-evaluate")
                  for rule in ledger.get("normalized_rules", [])),
              json.dumps([r.get("id") for r in ledger.get("normalized_rules", [])
                          if r.get("adapt_status") not in
                          ("executable", "partial", "cannot-evaluate")]))
        check("live packet: unresolved items are carried, not dropped",
              isinstance(ledger.get("unresolved"), list)
              and isinstance(ledger.get("quarantine"), list))
        # the live packet carries no costume that breaks these two rules, so the
        # controls are run as declared probes over the packet's own scopes: a
        # claim on CMAT-06 in E0 (closed inventory) and a foreign E4 label.
        import copy
        packet = ns_packet(result)
        probe_e0 = copy.deepcopy(packet)
        probe_e0["costumes"] = [{"id": "PROBE-E0", "era": "E0",
                                 "material": "lowland plant-thread cloth",
                                 "garment": "probe", "rite": "probe",
                                 "wearer_rank": "probe",
                                 "provenance": "import"}]
        e0 = reconcile_scoped(probe_e0)["records"][0]["findings"]
        check("probe: a claim on the closed inventory in E0 is a reject",
              any(f["code"] == "R-MAT-ERA-EXCLUDED" and f["severity"] == "reject"
                  for f in e0), json.dumps(e0))
        probe_e4 = copy.deepcopy(packet)
        probe_e4["costumes"] = [{"id": "PROBE-E4", "era": "E4",
                                 "material": "felt", "garment": "probe",
                                 "rite": "probe", "wearer_rank": "probe",
                                 "provenance": "local-production"}]
        e4 = reconcile_scoped(probe_e4)["records"][0]["findings"]
        check("probe: a foreign era label holds rather than merging by number",
              any(f["code"] == "R-ERA-UNMAPPED" and f["severity"] == "hold"
                  for f in e4), json.dumps(e4))
    else:
        check("live packet present", False, str(packet_path))

    # ---- 3b. the spec's parser-level negative controls (§5 D4) ----------
    def probe_packet(labels):
        return {"eras": ["E0", "E1", "E2", "E3"],
                "layers": [{"name": "Salt-road trade layer",
                            "substitutions": {"bh": "p", "dh": "t", "sh": "s", "g": "k"}}],
                "typed_labels": labels}

    def base_label(**over):
        label = {"id": "PROBE-01", "owner": "05-lexicon", "label_id": "L-99",
                 "kind": "native-form", "text": "kas", "script": "Latn",
                 "representation": "editorial-romanization", "scheme": "d2-roman",
                 "status": "supplied", "era_ids": [], "issues": []}
        label.update(over)
        return label

    two_forms = parse_typed_labels(probe_packet([
        base_label(), base_label(id="PROBE-02")]))
    check("spec L2: two supplied sound forms on one record is D2L-DATA",
          two_forms["exit_code"] == 2
          and any(f["code"] == "D2L-DATA" for f in two_forms["findings"]),
          json.dumps(two_forms["findings"])[:200])
    missing_owner = parse_typed_labels(probe_packet([
        {key: value for key, value in base_label().items() if key != "owner"}]))
    check("spec L1: a missing required field is D2L-DATA",
          missing_owner["exit_code"] == 2
          and any(f["code"] == "D2L-DATA" for f in missing_owner["findings"]),
          json.dumps(missing_owner["findings"])[:200])
    bad_borrow = parse_typed_labels(probe_packet([base_label(
        kind="borrowed-strata", text="kes",
        borrow={"layer_ref": "Salt-road trade layer",
                "donor": {"immediate": "lowland stage 1", "ultimate": None,
                          "carrier": None},
                "donor_form": "gas", "substitutions": {"g": "k"},
                "entry_stage": "E1", "referent_available_from": "E1",
                "channel": "the salt road", "alternative_checks": []})]))
    check("spec B3: substitutions that do not derive the form are D2L-BORROW",
          any(f["code"] == "D2L-BORROW" for f in bad_borrow["findings"]),
          json.dumps(bad_borrow["findings"])[:200])
    good_borrow = parse_typed_labels(probe_packet([base_label(
        kind="borrowed-strata", text="kas",
        borrow={"layer_ref": "Salt-road trade layer",
                "donor": {"immediate": "lowland stage 1", "ultimate": None,
                          "carrier": None},
                "donor_form": "gas", "substitutions": {"g": "k"},
                "entry_stage": "E1", "referent_available_from": "E1",
                "channel": "the salt road", "alternative_checks": []})]))
    check("spec B3 positive: gas with g->k derives kas and is clean",
          not any(f["code"] == "D2L-BORROW" for f in good_borrow["findings"]),
          json.dumps(good_borrow["findings"])[:200])
    check("parser: apply_substitutions is one pass, longest key first",
          apply_substitutions({"bh": "p", "g": "k"}, "bher") == "per"
          and apply_substitutions({"g": "k"}, "gas") == "kas",
          apply_substitutions({"bh": "p", "g": "k"}, "bher"))
    check("parser: screen_pattern flags a catastrophic pattern",
          screen_pattern("^(?P<stem>(a+)+)$") == "E-LABEL-PATTERN-RISK")
    check("parser: check_template refuses an attribute path",
          check_template("{stem.__class__}", ("stem",)) == "E-LABEL-TEMPLATE")

    # ---- 3c. era reconciliation verdicts (spec §2.2) on declared rows ----
    alias_rows, two_to_one = era_alias_rows()
    verdicts = {label: reconcile_era(label, alias_rows)
                for label in ("E0", "era-1", "E1 shelter era", "E9 no such label")}
    check("era: a contract tag is identity",
          verdicts["E0"]["verdict"] == "identity", json.dumps(verdicts["E0"]))
    check("era: the declared legacy handle is mapped-confirmed",
          verdicts["era-1"]["verdict"] == "mapped-confirmed"
          and verdicts["era-1"]["tag"] == "E0", json.dumps(verdicts["era-1"]))
    check("era: a (to-verify) ERX row is mapped-unconfirmed, never promoted",
          verdicts["E1 shelter era"]["verdict"] == "mapped-unconfirmed",
          json.dumps(verdicts["E1 shelter era"]))
    check("era: an unnamed label is unmapped, never identity-by-number",
          verdicts["E9 no such label"]["verdict"] == "unmapped",
          json.dumps(verdicts["E9 no such label"]))
    check("era: the declared two-to-one row is kept, not collapsed",
          all(entry.get("tags") for entry in two_to_one), json.dumps(two_to_one))

    # ---- 3d. per-family alias resolution (round 20, O claim) ------------
    # The round-19 wart: the alias leg read examples/culture-d2 for every
    # packet. These controls hold the two ends apart — the D2 leg is the
    # round-8 leg, and a non-D2 packet is resolved from its own declaration or
    # skipped in the open, never satisfied from the D2 tree.
    d4_packet_path = ROOT / "examples/culture-d4/packet.d4.yml"
    if d4_packet_path.is_file():
        d4_leg = family_alias_leg(d4_packet_path,
                                  load_packet_file(str(d4_packet_path))["packet"] or {})
        check("family: a d4 packet resolves its own declared alias rows",
              [row["source"] for row in d4_leg["rows"]]
              == ["the stamp era", "the mark hand", "the league",
                  "the cold fire (reserved)"]
              and all(row["status"] == "confirmed" for row in d4_leg["rows"]),
              json.dumps(d4_leg["rows"]))
        check("family: no d4 alias row or basis line resolves from the d2 tree",
              not any("12-rank-rules" in str(row["id"]) for row in d4_leg["rows"])
              and not any(str(entry).startswith("examples/culture-d2")
                          for entry in d4_leg["basis"]),
              json.dumps(d4_leg["basis"]))
        check("family: the leg the d4 packet does not declare is skipped, not faked",
              [entry["leg"] for entry in d4_leg["skipped"]]
              == ["costume-era reconciliation"], json.dumps(d4_leg["skipped"]))
        check("family: the d4 verdict probes are the packet's own labels",
              d4_leg["probes"][-1] == UNMAPPED_PROBE
              and "the league" in d4_leg["probes"]
              and d4_leg["aliases"].get("the league") == "E2",
              json.dumps(d4_leg["probes"]))
    else:
        check("family: the d4 packet is present", False, str(d4_packet_path))
    d2_leg = family_alias_leg(PACKET_DEFAULT,
                              load_packet_file(str(PACKET_DEFAULT))["packet"] or {})
    check("family: the d2 leg is the round-8 leg, unchanged",
          [row["id"] for row in d2_leg["rows"]][:3]
          == ["12-rank-rules era_aliases.era-1", "12-rank-rules era_aliases.era-2",
              "12-rank-rules era_aliases.era-3"]
          and d2_leg["probes"] == list(D2_ERA_PROBES) and d2_leg["skipped"] == []
          and d2_leg["basis"][0]
          == "examples/culture-d2/components/12-rank-rules.yml era_aliases (A1)",
          json.dumps(d2_leg["basis"]))
    bare_leg = family_alias_leg(ROOT / "examples/culture-d4/probe-bare.yml",
                                {"eras": ["E0"]})
    check("family: a packet declaring no alias rules is skipped, never aliased",
          bare_leg["aliases"] == {} and bare_leg["rows"] == []
          and {entry["leg"] for entry in bare_leg["skipped"]}
          == {"era-alias resolution", "costume-era reconciliation"}
          and bare_leg["probes"] == [UNMAPPED_PROBE],
          json.dumps(bare_leg["skipped"]))
    shaped_leg = family_alias_leg(
        ROOT / "examples/culture-d4/probe-rows.yml",
        {"named_eras": [{"id": "ER-01", "name": "the stamp era", "tag": "E0"}],
         "era_reconciliation": [{"id": "ERX-9", "their_labels": {"a": "the old era"},
                                 "maps_to": "E1", "status": "(to-verify)"}]})
    check("family: a packet-declared reconciliation row is shaped like the d2 leg",
          any(row["id"] == "ERX-9" and row["source"] == "the old era"
              and row["status"] == "to-verify" and row["tag"] == "E1"
              for row in shaped_leg["rows"]), json.dumps(shaped_leg["rows"]))

    def alias_refusal(packet):
        try:
            packet_alias_rows(packet)
        except Malformed as exc:
            return str(exc)
        return ""

    for tag in CONTRACT_ERAS:
        aliases, rows, key = packet_alias_rows({"era_aliases": {"old era": tag}})
        check("alias: declared %s stays mapped-confirmed without coercion" % tag,
              aliases == {"old era": tag} and key == "era_aliases"
              and reconcile_era("old era", rows)["verdict"] == "mapped-confirmed"
              and rows[0]["tag"] == tag, json.dumps(rows))
    invalid_tags = ([1, 2], {"tag": "E1"}, 1, 1.5, True, None,
                    "", " E1", "E1 ", "e1", "E9", "E10", "E1 suffix")
    for key in PACKET_ALIAS_KEYS:
        for tag in invalid_tags:
            declared = ({"old era": tag} if key == "era_aliases" else
                        [{"id": "ER-PROBE", "name": "old era", "tag": tag}])
            diagnostic = alias_refusal({key: declared})
            check("alias: %s rejects malformed tag %r" % (key, tag),
                  diagnostic.startswith("P-ERA-ALIAS at ") and key in diagnostic,
                  diagnostic)
    malformed_aliases = (
        {"era_aliases": "nope"}, {"era_aliases": []}, {"era_aliases": None},
        {"era_aliases": {1: "E1"}}, {"era_aliases": {"": "E1"}},
        {"era_aliases": {" ": "E1"}},
        {"era_aliases": {"old era": [1, 2]},
         "named_eras": [{"name": "valid fallback", "tag": "E1"}]},
    )
    for index, malformed in enumerate(malformed_aliases):
        diagnostic = alias_refusal(malformed)
        check("alias: malformed map/name %d refuses before fallback" % (index + 1),
              diagnostic.startswith("P-ERA-ALIAS at "), diagnostic)
    for key in ("named_eras", "era_records"):
        aliases, rows, source = packet_alias_rows(
            {key: [{"id": "ER-PROBE", "name": "old era", "tag": "E1"}]})
        check("alias: valid %s preserves its declared name/tag pair" % key,
              aliases == {"old era": "E1"} and source == key
              and rows == [{"id": "packet %s.ER-PROBE" % key,
                            "source": "old era", "tag": "E1",
                            "status": "confirmed"}], json.dumps(rows))
        for index, declared in enumerate((None, {}, ["not a record"],
                                           [{"name": "old era"}],
                                           [{"name": "", "tag": "E1"}],
                                           [{"name": "old era", "tag": "E1"},
                                            {"name": "old era", "tag": "E2"}])):
            diagnostic = alias_refusal({key: declared})
            check("alias: malformed %s record set %d refuses" % (key, index + 1),
                  diagnostic.startswith("P-ERA-ALIAS at "), diagnostic)
    empty_aliases = packet_alias_rows({"era_aliases": {}, "named_eras": [],
                                       "era_records": []})
    check("alias: empty declarations keep the explicit no-alias path",
          empty_aliases == ({}, [], None), repr(empty_aliases))

    # ---- 4. CLI: emit / check / tamper, in an isolated tree -------------
    with tempfile.TemporaryDirectory() as tmp:
        mirror = pathlib.Path(tmp) / "repo"
        (mirror / "tools/gates").mkdir(parents=True)
        (mirror / "examples/culture-d2/components").mkdir(parents=True)
        shutil.copy(pathlib.Path(__file__).resolve(),
                    mirror / "tools/d2-typed-labels.py")
        for name in ("costume-era-consistency-gate.py",):
            src = ROOT / "tools/gates" / name
            if src.exists():
                shutil.copy(src, mirror / "tools/gates" / name)
        shutil.copy(PACKET_DEFAULT, mirror / "examples/culture-d2/packet.d2.yml")
        for name in ("12-rank-rules.yml", "11-costumes.yml", "09-eras-calendar.yml",
                     "05-lexicon.yml"):
            shutil.copy(ROOT / "examples/culture-d2/components" / name,
                        mirror / "examples/culture-d2/components" / name)
        tool = mirror / "tools/d2-typed-labels.py"

        def run(*args):
            return subprocess.run([sys.executable, str(tool)] + list(args),
                                  capture_output=True, text=True, cwd=str(mirror))

        emitted = mirror / "examples/culture-d2/typed-labels.d2.yml"
        write = run("--emit", str(emitted))
        check("cli: --emit writes the projection", write.returncode in (0, 1)
              and emitted.exists(), write.stderr.strip()[:200])
        clean = run("--check", str(emitted))
        check("cli: --check exit 0 on the fresh projection", clean.returncode == 0,
              clean.stderr.strip()[:200])
        payload = emitted.read_bytes() if emitted.exists() else b""
        if not payload:
            check("cli: tamper controls skipped (no projection written)", False,
                  "emit failed; see the previous check")
        emitted.write_bytes(payload.replace(b'"translated-label"',
                                            b'"translated-labelX"', 1))
        drift = run("--check", str(emitted))
        check("cli: --check exit 1 on a changed byte", drift.returncode == 1,
              "exit=%s" % drift.returncode)
        emitted.write_bytes(payload)
        again = run("--check", str(emitted))
        check("cli: --check exit 0 after restore", again.returncode == 0)
        first = run("--emit", str(emitted))
        second_payload = emitted.read_bytes()
        check("cli: two builds are byte-identical", second_payload == payload)
        js = run("--json")
        check("cli: --json prints one JSON document",
              js.returncode in (0, 1) and js.stdout.lstrip().startswith("{"),
              js.stdout[:120])
        bad = mirror / "examples/culture-d2/broken.yml"
        bad.write_text("phonology:\n  consonants: [p, t\n")
        broken = run("--packet", str(bad))
        check("cli: malformed packet exits 2 with a stable code",
              broken.returncode == 2 and "D2L-DATA" in broken.stdout + broken.stderr,
              "exit=%s %s" % (broken.returncode, broken.stdout[:120]))

    # ---- 5. the d4 family is faithful with no foreign examples tree -----
    # The round-19 wart: a faithful d4 mirror had to copy
    # examples/culture-d2/components/{12-rank-rules,11-costumes}.yml. The mirror
    # below holds only the d4 family's own tree, the reader the projection names
    # and the projector — and must rebuild the filed d4 projection byte for byte.
    d4_packet = ROOT / "examples/culture-d4/packet.d4.yml"
    d4_projection = ROOT / "examples/culture-d4/typed-labels.d4.yml"
    if d4_packet.is_file():
        with tempfile.TemporaryDirectory() as tmp:
            d4mirror = pathlib.Path(tmp) / "repo"
            (d4mirror / "tools/gates").mkdir(parents=True)
            (d4mirror / "examples/culture-d4").mkdir(parents=True)
            shutil.copy(pathlib.Path(__file__).resolve(),
                        d4mirror / "tools/d2-typed-labels.py")
            shutil.copy(ROOT / "tools/gates/costume-era-consistency-gate.py",
                        d4mirror / "tools/gates/costume-era-consistency-gate.py")
            shutil.copy(d4_packet, d4mirror / "examples/culture-d4/packet.d4.yml")
            check("mirror: the d4 mirror holds no examples/culture-d2 tree",
                  not (d4mirror / "examples/culture-d2").exists())
            d4tool = d4mirror / "tools/d2-typed-labels.py"
            d4emitted = d4mirror / "examples/culture-d4/typed-labels.d4.yml"

            def d4run(*args):
                return subprocess.run([sys.executable, str(d4tool)] + list(args),
                                      capture_output=True, text=True, cwd=str(d4mirror))

            build = d4run("--packet", "examples/culture-d4/packet.d4.yml",
                          "--emit", "examples/culture-d4/typed-labels.d4.yml")
            check("mirror: the d4 build runs with no foreign tree (exit 0/1)",
                  build.returncode in (0, 1) and d4emitted.exists(),
                  "exit=%s %s" % (build.returncode, build.stderr.strip()[:200]))
            live = d4_projection.read_bytes() if d4_projection.is_file() else b""
            check("mirror: the mirror build is byte-identical to the filed d4 projection",
                  bool(live) and d4emitted.exists() and d4emitted.read_bytes() == live,
                  "mirror %d bytes vs filed %d bytes"
                  % (d4emitted.stat().st_size if d4emitted.exists() else -1, len(live)))
            clean = d4run("--packet", "examples/culture-d4/packet.d4.yml",
                          "--check", "examples/culture-d4/typed-labels.d4.yml")
            check("mirror: --check exits 0 in the mirror", clean.returncode == 0,
                  "exit=%s %s" % (clean.returncode, clean.stderr.strip()[:200]))
            original = d4_packet.read_text(encoding="utf-8")
            malformed_declarations = (
                ("list-tag", "era_aliases", {"era-9": [1, 2]}),
                ("invalid-tag", "era_aliases", {"era-9": "E9"}),
                ("non-map", "era_aliases", "nope"),
                ("named-list-tag", "named_eras",
                 [{"id": "ER-PROBE", "name": "old era", "tag": [1, 2]}]),
            )
            for label, key, declaration in malformed_declarations:
                probe = d4mirror / "examples/culture-d4" / (label + ".yml")
                line = "%s: %s\n" % (key, json.dumps(declaration))
                text = (original + "\n" + line if key == "era_aliases" else
                        re.sub(r"^named_eras:\n.*?(?=^\S)", lambda match: line,
                               original, count=1, flags=re.M | re.S))
                probe.write_text(text, encoding="utf-8")
                target = d4mirror / "examples/culture-d4" / (label + "-output.yml")
                refused = d4run("--packet", str(probe), "--emit", str(target))
                check("alias cli: %s emit refuses without creating a projection" % label,
                      refused.returncode == 2 and "P-ERA-ALIAS" in refused.stderr
                      and not refused.stdout and not target.exists(),
                      "exit=%s %s" % (refused.returncode, refused.stderr.strip()[:200]))
                sentinel = b"existing output must survive malformed input\n"
                target.write_bytes(sentinel)
                refused = d4run("--packet", str(probe), "--emit", str(target))
                check("alias cli: %s emit preserves an existing output" % label,
                      refused.returncode == 2 and "P-ERA-ALIAS" in refused.stderr
                      and target.read_bytes() == sentinel, refused.stderr.strip()[:200])
                refused = d4run("--packet", str(probe), "--json")
                check("alias cli: %s json refuses without a confirmed row" % label,
                      refused.returncode == 2 and "P-ERA-ALIAS" in refused.stderr
                      and not refused.stdout, refused.stderr.strip()[:200])
                refused = d4run("--packet", str(probe), "--check", str(d4emitted))
                check("alias cli: %s check refuses before byte comparison" % label,
                      refused.returncode == 2 and "P-ERA-ALIAS" in refused.stderr,
                      refused.stderr.strip()[:200])
            valid = d4mirror / "examples/culture-d4/valid-alias.yml"
            valid.write_text(original + '\nera_aliases: {"era-9": "E1"}\n',
                             encoding="utf-8")
            target = d4mirror / "examples/culture-d4/valid-alias-output.yml"
            accepted = d4run("--packet", str(valid), "--emit", str(target))
            alias_rows = (json.loads(target.read_text(encoding="utf-8"))
                          ["era_reconciliation"]["alias_rows"] if target.is_file() else [])
            check("alias cli: a valid declared map still emits a confirmed contract tag",
                  accepted.returncode in (0, 1)
                  and alias_rows == [{"id": "packet era_aliases.era-9",
                                      "source": "era-9", "tag": "E1",
                                      "status": "confirmed"}],
                  "exit=%s %s" % (accepted.returncode, accepted.stderr.strip()[:200]))
    else:
        check("mirror: the d4 packet is present", False, str(d4_packet))

    _selftest_family(check)
    total = len(passed) + len(failed)
    if failed:
        print("selftest: %d/%d checks passed — failures: %s"
              % (len(passed), total, "; ".join(failed)))
        return 1
    print("selftest: %d/%d checks passed — the three shard control matrices, the "
          "loader/parser malformed cases, the live-packet typing and "
          "reconciliation cases, and the CLI emit/check/tamper controls; no file "
          "outside the temporary directory touched" % (len(passed), total))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--packet", default=str(PACKET_DEFAULT),
                        help="packet to read (default: %s)" % PACKET_DEFAULT)
    parser.add_argument("--json", action="store_true",
                        help="print one JSON document instead of the report")
    parser.add_argument("--emit", metavar="PATH",
                        help="write the deterministic projection to PATH")
    parser.add_argument("--check", metavar="PATH", nargs="?", const=str(PROJECTION_DEFAULT),
                        help="byte-compare the projection; writes nothing")
    parser.add_argument("--selftest", "--self-test", action="store_true",
                        dest="selftest", help="fixture + control matrix")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    try:
        if args.check:
            result = run_pipeline(args.packet)
            target = pathlib.Path(args.check)
            payload = serialize(result["projection"]) if result["projection"] else None
            if payload is None:
                print("could-not-evaluate: %s" % result["findings"][:1],
                      file=sys.stderr)
                return 2
            if not target.exists() or target.read_bytes() != payload:
                print("%s differs from the deterministic projection" % target,
                      file=sys.stderr)
                return 1
            print("%s: byte-identical deterministic projection" % target)
            return 0   # --check answers byte-identity; findings are the report's job
        result = run_pipeline(args.packet)
        if args.json:
            print(json.dumps(result["json_document"], sort_keys=True,
                             ensure_ascii=False))
            return result["exit"]
        if args.emit:
            if result["projection"] is None:
                print("could-not-evaluate: nothing to emit", file=sys.stderr)
                return 2
            pathlib.Path(args.emit).write_bytes(serialize(result["projection"]))
            print("Wrote %s" % args.emit)
            return result["exit"]
        return report(result)
    except (Malformed, PacketSyntaxError, ReconciliationError, ValueError,
            OSError) as exc:
        print("d2-typed-labels error: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
