#!/usr/bin/env python3
"""Myth-consistency gate — executable kernel for
corpus/knowledge/verification/myth-consistency-gate.md.

Interface
---------
    python3 tools/gates/myth-consistency-gate.py <culture-packet.yml>
        Prints one finding per line as `FINDING <id>: <message>` on stdout.
        Exit codes (no other codes are used):
            0  clean              — every kernel check evaluated, no finding
            1  findings           — at least one FAIL or HOLD finding printed
            2  could-not-evaluate — input missing/unreadable, or the root is
               not a YAML mapping carrying a nonempty `name` (malformed packet)
    python3 tools/gates/myth-consistency-gate.py --selftest
        (`--self-test` is accepted as an alias.) Rebuilds
        tools/gates/fixtures/myth-consistency-gate.yml and
        tools/gates/fixtures/myth-consistency-gate.expected, runs this gate on
        the fixture as a subprocess, and asserts exit 1 with every planted
        finding ID present, plus an in-memory repaired control asserting
        exit 0.

Kernel scope
------------
This implements the mechanically checkable subset of the spec's three
authored sections: §3 P pantheon role coverage, §4 M motif coherence, §6 S
symbol-domain uniqueness. Era alignment (§5 E), source scholarship, and every
semantic comparison remain with the manual review the spec describes. A clean
run is an engineering result, not canon, not authenticity, not canon approval
— lore-shokunin owns world-bible decisions (lane AGENTS.md).

Finding IDs
-----------
The spec's own IDs are emitted only for the spec's own conditions:
  MC-P01  FAIL  §3 — an exclusive agent is required for a critical dependency
                 but none is assigned while substitutes are explicitly denied
  MC-P02  HOLD  §3 — a role is marked absent solely because the surviving
                 elite text does not mention it
  MC-M01  FAIL  §4 — a variant that asserts its declared narrative law shows
                 the contradicting act inside that same variant with no
                 exception recorded
  MC-M02  HOLD  §4 — a claimed index comparison has no checked entry,
                 edition, or narrative witness
  MC-S01  FAIL  §6 — one normalized sign key carries incompatible exclusive
                 defaults with no bounded ambiguity/exception record
  MC-S02  HOLD  §6 — a "universal meaning" substitutes for community- and
                 period-specific evidence
Kernel-extension HOLD IDs (this file's documented admission policy, not spec
codes, emitted under the spec's "missing essential input is HOLD" rule):
  MC-P00  role ledger missing or under-specified (no status mark, SHARED
          without jurisdiction record, UNKNOWN without reason, dangling agent)
  MC-M00  motif ledger missing or under-specified (no local ID, declared law
          without testable trigger/effect or without variant records)
  MC-S00  symbol key not normalizable (form+medium+era+register+audience
          required; a bare sign is an inadequate key) or a multivalent reading
          without poles/context cues
  G-DATA  structural input failure (exit 2)

Packet schema
-------------
Shared fleet culture-packet schema, parsed leniently; keys this kernel does
not read are ignored, and a missing key is could-not-evaluate, never an
invented default:
    name, phonology, morphology, lexicon, pantheon, symbols, costumes,
    names, eras
`pantheon`: [{name, role, domain, era}], or the marker `NOT-APPLICABLE`
(with a `pantheon_note`) for a non-pantheonic system (§3).

Extensions this kernel reads (optional; absence produces HOLD findings):
`roles` — the role ledger of §2/§3:
    [{dependency, status, agents: [...], exclusive, substitute, basis, note,
      evidence}]
    status ∈ ASSIGNED | SHARED | NON-DIVINE | EXPLICITLY-UNEXPLAINED | UNKNOWN
`motifs` — the narrative/index ledger of §2/§4:
    [{id, tier, title, code, cf_atu, index_checked, index_edition,
      index_witness, official,
      law: {rule, when, then},
      variants: [{id, teller, register, asserts_law, exception,
                  events: [{actor, action, effect, exception}]}]}]
`symbols` — the symbol ledger of §2/§6, base keys plus:
    {medium|material, register|occasion, audience|office, community, place,
     exclusive, poles, evidence, exception, contrast}
    `domain` may be one string or a list of readings.

An index `code` not prefixed `cf.` and matching an index family prefix
(AT/ATU/FFC/ML) counts as a claimed official identifier and needs the same
checked entry, edition, and witness as a `cf_atu` comparison [spec §4].

Input support: a documented YAML subset (block mappings/sequences, flow
lists/mappings, quoted and plain scalars, comments, `- key: value` items).
The evaluator never writes to the packet; only --selftest writes, and only
inside tools/gates/fixtures/.
"""

import copy
import re
import subprocess
import sys
from pathlib import Path

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures"
FIXTURE_STEM = "myth-consistency-gate"

KEY_FIELDS = ("sign", "medium", "era", "register", "audience")
KEY_ALIASES = {
    "sign": ("symbol",),
    "medium": ("material",),
    "era": ("period",),
    "register": ("occasion",),
    "audience": ("office",),
}
STATUS_MARKS = {
    "ASSIGNED",
    "SHARED",
    "NON-DIVINE",
    "EXPLICITLY-UNEXPLAINED",
    "UNKNOWN",
}
UNIVERSAL_MARKERS = (
    "universal",
    "worldwide",
    "world-wide",
    "all cultures",
    "every culture",
    "all peoples",
    "all humans",
    "human nature",
    "inherent meaning",
)


class GateParseError(Exception):
    pass


# --- YAML subset parser -----------------------------------------------------


def _quote_start(prev):
    return prev is None or prev in " \t[{,:"


def _strip_comment(raw):
    out = []
    quote = None
    for i, ch in enumerate(raw):
        prev = raw[i - 1] if i else None
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
        elif ch in "'\"" and _quote_start(prev):
            quote = ch
            out.append(ch)
        elif ch == "#" and (i == 0 or raw[i - 1] in " \t"):
            break
        else:
            out.append(ch)
    return "".join(out)


def _split_top(text, sep=","):
    parts, buf, quote, depth = [], [], None, 0
    for i, ch in enumerate(text):
        prev = text[i - 1] if i else None
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
        elif ch in "'\"" and _quote_start(prev):
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
    parts.append("".join(buf))
    return parts


def _looks_like_mapping(text):
    quote, depth = None, 0
    for i, ch in enumerate(text):
        prev = text[i - 1] if i else None
        if quote:
            if ch == quote:
                quote = None
        elif ch in "'\"" and _quote_start(prev):
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == ":" and depth == 0 and (i + 1 == len(text) or text[i + 1] in " \t"):
            return True
    return False


def _is_sequence_line(text):
    return text == "-" or text.startswith("- ")


def _parse_scalar(text):
    text = text.strip()
    if not text:
        return None
    if text[0] in "[{":
        return _parse_flow(text)
    if text[0] in "'\"":
        if len(text) < 2 or text[-1] != text[0]:
            raise GateParseError("unterminated quoted scalar: %r" % text)
        return text[1:-1]
    low = text.lower()
    if low in ("true", "yes", "on"):
        return True
    if low in ("false", "no", "off"):
        return False
    if low in ("null", "~", "none"):
        return None
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    if re.fullmatch(r"-?\d+\.\d+", text):
        return float(text)
    return text


def _parse_flow(text):
    if text[0] == "[":
        if not text.endswith("]"):
            raise GateParseError("unterminated flow sequence: %r" % text)
        inner = text[1:-1].strip()
        return [] if not inner else [_parse_scalar(p) for p in _split_top(inner)]
    if not text.endswith("}"):
        raise GateParseError("unterminated flow mapping: %r" % text)
    inner = text[1:-1].strip()
    if not inner:
        return {}
    result = {}
    for part in _split_top(inner):
        key, sep, rest = part.partition(":")
        if not sep:
            raise GateParseError("flow mapping entry without ':': %r" % part)
        result[key.strip()] = _parse_scalar(rest)
    return result


def _parse_mapping(lines, index, indent):
    result = {}
    while index < len(lines):
        line_indent, text = lines[index]
        if line_indent < indent or _is_sequence_line(text):
            break
        if line_indent > indent:
            raise GateParseError("unexpected indentation near %r" % text)
        if not _looks_like_mapping(text):
            raise GateParseError("expected 'key: value', got %r" % text)
        key, _, rest = text.partition(":")
        key, rest = key.strip(), rest.strip()
        if not key:
            raise GateParseError("empty mapping key near %r" % text)
        if key in result:
            raise GateParseError("duplicate key %r" % key)
        index += 1
        if rest:
            result[key] = _parse_scalar(rest)
        elif index < len(lines) and lines[index][0] > indent:
            result[key], index = _parse_node(lines, index, lines[index][0])
        else:
            result[key] = None
    return result, index


def _parse_sequence(lines, index, indent):
    items = []
    while index < len(lines):
        line_indent, text = lines[index]
        if line_indent < indent or not _is_sequence_line(text):
            break
        if line_indent > indent:
            raise GateParseError("unexpected indentation near %r" % text)
        content = text[1:].strip()
        index += 1
        if not content:
            if index < len(lines) and lines[index][0] > indent:
                value, index = _parse_node(lines, index, lines[index][0])
            else:
                value = None
            items.append(value)
        elif _looks_like_mapping(content):
            cont_indent = indent + 2
            if (
                index < len(lines)
                and lines[index][0] > indent
                and not _is_sequence_line(lines[index][1])
            ):
                cont_indent = lines[index][0]
            lines.insert(index, (cont_indent, content))
            value, index = _parse_node(lines, index, cont_indent)
            items.append(value)
        else:
            items.append(_parse_scalar(content))
    return items, index


def _parse_node(lines, index, indent):
    if _is_sequence_line(lines[index][1]):
        return _parse_sequence(lines, index, indent)
    return _parse_mapping(lines, index, indent)


def parse_packet(text):
    lines = []
    for raw in text.splitlines():
        stripped = _strip_comment(raw)
        if not stripped.strip():
            continue
        indent_text = stripped[: len(stripped) - len(stripped.lstrip(" "))]
        if "\t" in indent_text:
            raise GateParseError("tab indentation is not supported")
        lines.append((len(indent_text), stripped.strip()))
    if not lines:
        raise GateParseError("empty document")
    if lines[0][0] != 0:
        raise GateParseError("document does not start at column 0")
    value, index = _parse_node(lines, 0, 0)
    if index != len(lines):
        raise GateParseError("unparsed YAML content at token %d" % index)
    return value


# --- normalization helpers --------------------------------------------------


def _as_entries(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _text(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).strip()


def _lower(value):
    return _text(value).lower()


def _truthy(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    return _lower(value) in ("true", "yes", "on", "1", "exclusive")


def _strings(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [s for s in (_text(v) for v in value) if s]
    text = _text(value)
    return [text] if text else []


def _is_denial(value):
    return _lower(value) in (
        "false",
        "no",
        "none",
        "denied",
        "not-licensed",
        "not licensed",
        "forbidden",
        "no-substitute",
        "no substitute",
    )


def _matches(needle, haystack):
    if not needle or not haystack:
        return False
    return needle == haystack or needle in haystack or haystack in needle


def _bounded(entry):
    return bool(
        entry.get("poles")
        or _text(entry.get("exception"))
        or _text(entry.get("contrast"))
        or _text(entry.get("exception_record"))
    )


def _domains(entry):
    return _strings(entry.get("domain") or entry.get("reading") or entry.get("meaning"))


def _sym_field(entry, name):
    for key in (name,) + KEY_ALIASES.get(name, ()):
        value = _text(entry.get(key))
        if value:
            return value
    return ""


# --- P: pantheon role coverage (spec §3) -----------------------------------


def check_pantheon(packet):
    findings = []
    pantheon_raw = packet.get("pantheon")
    roles_raw = packet.get("roles")

    not_applicable = _lower(pantheon_raw).startswith("not-applicable")
    if isinstance(pantheon_raw, dict):
        not_applicable = _lower(pantheon_raw.get("status")).startswith("not-applicable")

    names = set()
    if not not_applicable:
        for entry in _as_entries(pantheon_raw):
            if not isinstance(entry, dict):
                findings.append(
                    ("MC-P00", "pantheon entry is not a mapping: %r" % (entry,))
                )
                continue
            name = _text(entry.get("name"))
            if name:
                names.add(name)
            else:
                findings.append(
                    ("MC-P00", "pantheon entry without a name cannot be listed in the role ledger")
                )

    roles = _as_entries(roles_raw)
    if not not_applicable and not roles:
        findings.append(
            (
                "MC-P00",
                "no role ledger (`roles`) present: coverage marks "
                "ASSIGNED/SHARED/NON-DIVINE/EXPLICITLY-UNEXPLAINED/UNKNOWN cannot be "
                "evaluated [spec §3]",
            )
        )
    for role in roles:
        if not isinstance(role, dict):
            findings.append(("MC-P00", "role entry is not a mapping: %r" % (role,)))
            continue
        dependency = (
            _text(role.get("dependency"))
            or _text(role.get("role"))
            or _text(role.get("name"))
            or "<unnamed dependency>"
        )
        status = (
            _lower(role.get("status") or role.get("coverage"))
            .upper()
            .replace("_", "-")
            .replace(" ", "-")
        )
        if status and status not in STATUS_MARKS:
            findings.append(
                (
                    "MC-P00",
                    "role %r carries status %r, not one of the five coverage marks "
                    "[spec §3]" % (dependency, status),
                )
            )
            continue
        agents = _strings(role.get("agents") or role.get("agent"))
        resolved = [a for a in agents if not names or a in names]
        dangling = [a for a in agents if names and a not in names]
        note = _text(role.get("note"))
        basis = _lower(role.get("basis"))
        evidence = _text(role.get("evidence"))
        exclusive = _truthy(role.get("exclusive")) or _truthy(role.get("critical"))
        substitute = _text(role.get("substitute"))
        denied = (
            _is_denial(role.get("substitute"))
            or role.get("substitutes_allowed") is False
            or _truthy(role.get("no_substitute"))
        )
        if denied:
            substitute = ""
        non_divine = status == "NON-DIVINE" or bool(_text(role.get("mechanism")))

        if exclusive and not resolved and not non_divine and not substitute:
            if denied:
                findings.append(
                    (
                        "MC-P01",
                        "role %r requires an exclusive agent for its rite, assigns none, "
                        "and explicitly denies a substitute [spec §3 MC-P01]" % dependency,
                    )
                )
            else:
                findings.append(
                    (
                        "MC-P00",
                        "role %r is exclusive but has no resolved agent and no declared "
                        "substitute status [spec §3]" % dependency,
                    )
                )
            continue
        if dangling:
            findings.append(
                (
                    "MC-P00",
                    "role %r lists agent(s) absent from the pantheon: %s [spec §3]"
                    % (dependency, ", ".join(dangling)),
                )
            )
        if status == "ASSIGNED" and not resolved and not exclusive:
            findings.append(
                (
                    "MC-P00",
                    "role %r is marked ASSIGNED but no agent resolves to the pantheon "
                    "and no non-divine mechanism is declared [spec §3]" % dependency,
                )
            )
        if status == "SHARED" and not note:
            findings.append(
                (
                    "MC-P00",
                    "role %r is marked SHARED without a jurisdiction/occasion record "
                    "[spec §3]" % dependency,
                )
            )
        elite_silence = "elite" in basis and any(
            token in basis for token in ("silence", "text", "mention", "record")
        )
        if elite_silence and not evidence:
            findings.append(
                (
                    "MC-P02",
                    "role %r is marked absent solely on basis %r (the surviving elite "
                    "text does not mention it) with no other evidence recorded "
                    "[spec §3 MC-P02]" % (dependency, _text(role.get("basis"))),
                )
            )
        if status in ("UNKNOWN", "ABSENT", "NOT-MENTIONED", "UNATTESTED"):
            if not (basis or note or evidence):
                findings.append(
                    (
                        "MC-P00",
                        "role %r is marked %s without a reason or evidence pointer "
                        "[spec §3]" % (dependency, status),
                    )
                )
    return findings


# --- M: motif coherence (spec §4) ------------------------------------------


def check_motifs(packet):
    findings = []
    motifs = _as_entries(packet.get("motifs"))
    if not motifs:
        findings.append(
            (
                "MC-M00",
                "no narrative/motif ledger (`motifs`) present: index concordance and "
                "variant coherence cannot be evaluated [spec §2, §4]",
            )
        )
        return findings
    for motif in motifs:
        if not isinstance(motif, dict):
            findings.append(("MC-M00", "motif entry is not a mapping: %r" % (motif,)))
            continue
        mid = _text(motif.get("id"))
        title = _text(motif.get("title"))
        label = mid or title or "<unnamed motif>"
        if not mid:
            findings.append(
                (
                    "MC-M00",
                    "motif %r has no local ID (a fictional tale takes a local ID, not an "
                    "invented official number) [spec §4]" % label,
                )
            )
        code = _text(motif.get("code"))
        claimed = bool(_text(motif.get("cf_atu"))) or _truthy(motif.get("official"))
        if (
            code
            and not code.lower().startswith("cf")
            and re.match(r"(?i)^(at|atu|ffc|ml)\b", code)
        ):
            claimed = True
        if claimed:
            checked = _truthy(motif.get("index_checked"))
            edition = _text(motif.get("index_edition"))
            witness = _text(motif.get("index_witness"))
            if not (checked and edition and witness):
                findings.append(
                    (
                        "MC-M02",
                        "motif %s claims comparison %r without a checked entry, edition, "
                        "or narrative witness [spec §4 MC-M02]"
                        % (
                            label,
                            _text(motif.get("cf_atu")) or code,
                        ),
                    )
                )
        law = motif.get("law")
        if not isinstance(law, dict):
            continue
        rule = _text(law.get("rule"))
        when = _lower(law.get("when") or law.get("trigger"))
        then = _lower(law.get("then") or law.get("effect"))
        if not (when and then):
            findings.append(
                (
                    "MC-M00",
                    "motif %s declares law %r without a testable trigger/effect pair "
                    "[spec §4]" % (label, rule or "<unnamed>"),
                )
            )
            continue
        variants = _as_entries(motif.get("variants"))
        if not variants:
            findings.append(
                (
                    "MC-M00",
                    "motif %s declares law %r but carries no variant records to test it "
                    "against [spec §4]" % (label, rule or "<unnamed>"),
                )
            )
            continue
        for variant in variants:
            if not isinstance(variant, dict):
                findings.append(
                    ("MC-M00", "motif %s variant entry is not a mapping" % label)
                )
                continue
            if not _truthy(variant.get("asserts_law")):
                continue
            vid = _text(variant.get("id")) or _text(variant.get("teller")) or "<variant>"
            events = _as_entries(variant.get("events"))
            if not events:
                findings.append(
                    (
                        "MC-M00",
                        "motif %s variant %s asserts law %r but records no events to "
                        "test it [spec §4]" % (label, vid, rule or "<unnamed>"),
                    )
                )
                continue
            for event in events:
                if not isinstance(event, dict):
                    continue
                action = _lower(event.get("action"))
                effect = _lower(event.get("effect"))
                if not (action and effect):
                    continue
                if not _matches(action, when):
                    continue
                if _matches(effect, then):
                    continue
                if _text(event.get("exception")) or _text(variant.get("exception")):
                    continue
                findings.append(
                    (
                        "MC-M01",
                        "motif %s variant %s asserts law %r (%r -> %r) but the same "
                        "variant shows %r with effect %r and records no exception "
                        "[spec §4 MC-M01]"
                        % (label, vid, rule or "<unnamed>", when, then, action, effect),
                    )
                )
    return findings


# --- S: symbol-domain uniqueness (spec §6) ---------------------------------


def check_symbols(packet):
    findings = []
    symbols = _as_entries(packet.get("symbols"))
    if not symbols:
        findings.append(
            (
                "MC-S00",
                "no symbol ledger (`symbols`) present: context-keyed domain uniqueness "
                "cannot be evaluated [spec §6]",
            )
        )
        return findings

    complete, incomplete, all_entries = [], [], []
    for entry in symbols:
        if not isinstance(entry, dict):
            findings.append(("MC-S00", "symbol entry is not a mapping: %r" % (entry,)))
            continue
        all_entries.append(entry)
        key = tuple(_sym_field(entry, field) for field in KEY_FIELDS)
        sign = key[0] or "<unnamed sign>"
        if all(key):
            complete.append((entry, key))
        else:
            missing = [field for field, value in zip(KEY_FIELDS, key) if not value]
            incomplete.append("%s (missing %s)" % (sign, "/".join(missing)))
        domains = _domains(entry)
        exclusive = _truthy(entry.get("exclusive")) or any(
            "exclusive" in _lower(domain) for domain in domains
        )
        if len(domains) > 1 and not _bounded(entry):
            if exclusive:
                findings.append(
                    (
                        "MC-S01",
                        "symbol %s carries incompatible exclusive readings (%s) with no "
                        "poles or exception record [spec §6 MC-S01]"
                        % (sign, "; ".join(domains)),
                    )
                )
            else:
                findings.append(
                    (
                        "MC-S00",
                        "symbol %s carries several readings (%s) with no poles or "
                        "contextual cues [spec §6]" % (sign, "; ".join(domains)),
                    )
                )

    if incomplete:
        findings.append(
            (
                "MC-S00",
                "under-normalized symbol keys (form+medium+era+register+audience "
                "required; a bare sign is an inadequate key, spec §6): "
                + "; ".join(incomplete[:8])
                + ("; ..." if len(incomplete) > 8 else ""),
            )
        )

    groups = {}
    for entry, key in complete:
        groups.setdefault(key, []).append(entry)
    for key, group in groups.items():
        if len(group) < 2:
            continue
        bounded = any(_bounded(entry) for entry in group)
        exclusive = [
            entry
            for entry in group
            if _truthy(entry.get("exclusive"))
            or any("exclusive" in _lower(d) for d in _domains(entry))
        ]
        readings = sorted({d for entry in group for d in _domains(entry)})
        if len(exclusive) >= 2 and len(readings) >= 2 and not bounded:
            findings.append(
                (
                    "MC-S01",
                    "normalized key (%s) carries incompatible exclusive defaults (%s) "
                    "with no bounded ambiguity or exception record [spec §6 MC-S01]"
                    % (", ".join("'%s'" % part for part in key), "; ".join(readings)),
                )
            )
        elif len(readings) >= 2 and not bounded:
            findings.append(
                (
                    "MC-S00",
                    "normalized key (%s) carries several defaults (%s) without one "
                    "editorial record or a bounded multivalent reading [spec §6]"
                    % (", ".join("'%s'" % part for part in key), "; ".join(readings)),
                )
            )

    for entry in all_entries:
        claim = _lower(entry.get("domain")) + " " + _lower(entry.get("notes"))
        if not any(marker in claim for marker in UNIVERSAL_MARKERS):
            continue
        evidence = _lower(entry.get("evidence"))
        if evidence and not any(marker in evidence for marker in UNIVERSAL_MARKERS):
            continue
        findings.append(
            (
                "MC-S02",
                "symbol %r claims a universal meaning (%r) without community/period "
                "evidence [spec §6 MC-S02]"
                % (_sym_field(entry, "sign") or "<unnamed sign>", _text(entry.get("domain"))),
            )
        )
    return findings


# --- evaluation and CLI -----------------------------------------------------


def evaluate(packet):
    findings = []
    if not isinstance(packet, dict):
        raise GateParseError("root is not a YAML mapping")
    if not _text(packet.get("name")):
        raise GateParseError("packet `name` is missing or empty")
    findings.extend(check_pantheon(packet))
    findings.extend(check_motifs(packet))
    findings.extend(check_symbols(packet))
    seen, unique = set(), []
    for finding in findings:
        if finding not in seen:
            seen.add(finding)
            unique.append(finding)
    return unique


def print_findings(findings):
    for finding_id, message in findings:
        print("FINDING %s: %s" % (finding_id, message))


def main(argv):
    if argv and argv[0] in ("--selftest", "--self-test"):
        return selftest()
    if len(argv) != 1:
        print("usage: myth-consistency-gate.py <culture-packet.yml> | --selftest")
        return 2
    path = Path(argv[0])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        print("FINDING G-DATA: cannot read %s: %s" % (path, error))
        return 2
    try:
        packet = parse_packet(text)
        findings = evaluate(packet)
    except GateParseError as error:
        print("FINDING G-DATA: %s" % error)
        return 2
    print_findings(findings)
    return 1 if findings else 0


# --- selftest fixture -------------------------------------------------------

FIXTURE_TEXT = """\
# synthetic fixture for tools/gates/myth-consistency-gate.py --selftest
# not canon, not a fictional-world fact; it exists only to exercise MC finding IDs
name: gate-selftest-culture
phonology:
  consonants: [p, t, k, m, n, s]
  vowels: [a, i, u]
  tones: 0
pantheon:
  - name: Sedge-Mother
    role: subsistence, water
    domain: floodplain fertility
    era: marsh-era
  - name: Ash-Judge
    role: oath, conflict settlement
    domain: boundary oaths
    era: marsh-era
  - name: Cinder-Smith
    role: craft, exchange
    domain: forge work
    era: marsh-era
roles:
  - dependency: subsistence-water
    status: ASSIGNED
    agents: [Sedge-Mother]
  - dependency: oath-conflict
    status: SHARED
    agents: [Ash-Judge]
    note: shared with household elders; a disputed invocation goes to the boundary rite first
  - dependency: mortality-burial
    status: NON-DIVINE
    agents: []
    note: household rites only; no divine agent is claimed
  - dependency: cosmic-origins
    status: EXPLICITLY-UNEXPLAINED
    agents: []
    note: doctrine refuses an origin account
  - dependency: craft-exchange
    status: ASSIGNED
    exclusive: true
    agents: []
    substitute: false
    note: the forge rite requires one exclusive patron; no substitute is licensed
  - dependency: reproduction-care
    status: UNKNOWN
    basis: elite-text-silence
    note: absent from the surviving temple text
motifs:
  - id: local-07
    tier: folktale
    title: The Marsh-Wife Names the Reed-Cutter
    code: cf. ATU 500
    cf_atu: ATU 500
    index_checked: false
    note: claimed comparison rests on an unchecked recollection
  - id: local-11
    tier: myth
    title: The Oath-Chamber and the River Guest
    law:
      rule: true-name power
      when: captive speaks its true name
      then: captor power ends
    variants:
      - id: var-a
        teller: marsh-women guild
        register: teaching
        asserts_law: true
        events:
          - actor: river guest
            action: speaks its true name
            effect: power remains intact
      - id: var-b
        teller: reed-cutters lodge
        register: fireside
        asserts_law: false
        events:
          - actor: river guest
            action: speaks its true name
            effect: captor loses the trail
symbols:
  - sign: white salt crust
    medium: shell-lime paste
    era: marsh-era
    register: burial
    audience: mourners
    domain: grief
    exclusive: true
    evidence: household rite manual, burial entries
  - sign: white salt crust
    medium: shell-lime paste
    era: marsh-era
    register: investiture
    audience: officiant
    domain: purity of office
    exclusive: true
    evidence: investiture manual
  - sign: heron feather
    medium: feather worn on hem
    era: marsh-era
    register: oath-taking
    audience: parties under oath
    domain: grants the judge authority
    exclusive: true
    evidence: oath-chamber practice
  - sign: heron feather
    medium: feather worn on hem
    era: marsh-era
    register: oath-taking
    audience: parties under oath
    domain: denies the judge authority
    exclusive: true
    evidence: counter-oath practice
  - sign: serpent
    medium: body paint
    era: marsh-era
    register: healing
    audience: patients
    domain: universal meaning of healing
    notes: claimed to mean the same thing in every culture
costumes:
  - garment: reed cloak
    material: woven reed
    wearer_rank: officiant
    rite: investiture
    era: marsh-era
eras: [marsh-era]
"""

PLANTED_IDS = ["MC-P01", "MC-P02", "MC-M01", "MC-M02", "MC-S01", "MC-S02"]


def _clean_control(packet):
    control = copy.deepcopy(packet)
    roles = control.get("roles")
    if isinstance(roles, list):
        for role in roles:
            if not isinstance(role, dict):
                continue
            if role.get("dependency") == "craft-exchange":
                role.update(
                    {
                        "status": "NON-DIVINE",
                        "exclusive": False,
                        "substitute": None,
                        "note": "forge fires are kept by the smith household; no divine patron is claimed",
                    }
                )
            if role.get("dependency") == "reproduction-care":
                role["basis"] = "field-survey-gap"
    motifs = control.get("motifs")
    if isinstance(motifs, list):
        for motif in motifs:
            if not isinstance(motif, dict):
                continue
            if motif.get("id") == "local-07":
                motif.update(
                    {
                        "index_checked": True,
                        "index_edition": "ATU 2004",
                        "index_witness": "type index entry checked for this comparison",
                    }
                )
            if motif.get("id") == "local-11":
                for variant in _as_entries(motif.get("variants")):
                    if isinstance(variant, dict) and variant.get("id") == "var-a":
                        for event in _as_entries(variant.get("events")):
                            if isinstance(event, dict):
                                event["exception"] = (
                                    "the name spoken was a licensed substitute-name"
                                )
    symbols = control.get("symbols")
    if isinstance(symbols, list):
        for entry in symbols:
            if not isinstance(entry, dict):
                continue
            if entry.get("sign") == "heron feather" and entry.get("domain") == (
                "denies the judge authority"
            ):
                entry["audience"] = "counter-oath swearers"
            if entry.get("sign") == "serpent":
                entry["domain"] = "healing"
                entry["notes"] = "paint applied by the marsh healers in the midwinter rite"
                entry["evidence"] = "healer-household practice recorded in the rite manual"
    return control


def selftest():
    FIXTURE_DIR.mkdir(parents=True, exist_ok=True)
    fixture_path = FIXTURE_DIR / (FIXTURE_STEM + ".yml")
    expected_path = FIXTURE_DIR / (FIXTURE_STEM + ".expected")
    fixture_path.write_text(FIXTURE_TEXT, encoding="utf-8")
    expected_path.write_text("\n".join(PLANTED_IDS) + "\n", encoding="utf-8")

    run = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), str(fixture_path)],
        capture_output=True,
        text=True,
    )
    assert run.returncode == 1, "fixture exit %d, expected 1\n%s" % (
        run.returncode,
        run.stderr,
    )
    lines = [line for line in run.stdout.splitlines() if line.strip()]
    assert lines, "fixture produced no findings"
    for line in lines:
        assert re.fullmatch(r"FINDING \S+: .+", line), "malformed finding line: %r" % line
    printed = [line.split(":", 1)[0].split(None, 1)[1] for line in lines]
    for planted in PLANTED_IDS:
        assert planted in printed, "planted ID %s missing from %s" % (planted, printed)

    control_packet = _clean_control(parse_packet(FIXTURE_TEXT))
    control_findings = evaluate(control_packet)
    assert control_findings == [], "clean control still reports: %r" % (control_findings,)

    print(
        "selftest: OK — fixture exit 1; planted IDs present: %s; "
        "clean control exit 0 (0 findings); fixture and expected rewritten under tools/gates/fixtures/"
        % ", ".join(PLANTED_IDS)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))