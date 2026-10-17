#!/usr/bin/env python3
"""costume-era-consistency-gate — executable audit kernel for costume packets.

Lane: kotodama-shokunin (言霊). Implements the bounded, executable subset of the
manual procedure in `corpus/knowledge/verification/costume-era-consistency-gate.md`
(M/T/E/R dimensions), grounded in the two corpus tables it cites:

  * `corpus/knowledge/culture-material/dress-through-eras.md`  (silhouette /
    material / wearer-rule grammar, enforcement mechanisms, debunk shelf)
  * `corpus/knowledge/culture-material/textile-technology.md`  (fiber, dye,
    loom/finish gates; "a culture cannot have a basic costume term for a cloth
    or color its four gates cannot make")

The kernel checks three assignment-named areas and one supporting area:

  1. material availability vs. claimed costume  — MAT-01..07, EAR-01
  2. rank-rule conflicts                        — R-01..R-07
  3. anachronism sweep (dated processes)        — E-01, EAR-04, G-ERA
  4. textile-tech bounds (supporting)           — T-01..T-03

Interface
---------
    python3 costume-era-consistency-gate.py <culture-packet.yml>
    python3 costume-era-consistency-gate.py --selftest        (alias --self-test)

One finding per stdout line:  ``FINDING <id>: [<severity>] <message>``
Severity vocabulary follows the spec's verdict words:
    [reject]  a demonstrated contradiction with the packet's own frozen inputs
    [hold]    no demonstrated contradiction, but an essential input is unresolved
    [note]    a declared violation / design departure kept visible

Exit codes
    0  clean: no finding lines printed
    1  findings: one or more FINDING lines printed (any severity; read the token)
    2  could-not-evaluate: unreadable/unparseable input, root not a mapping,
       wrong type for a present key, or no `costumes`/`eras` to review.

The exit code is a triage signal for the caller, never a canon ruling; mapping
findings to the spec's READY/REJECT/HOLD verdicts (and every lore decision)
belongs to the caller / lore-shokunin. This file is NOT a registered fleet gate
and the spec's §1 calibration applies: the tests below are designer audit
conventions, not historical laws.

Packet schema (shared gate schema, parsed leniently; extra keys below are this
gate's own optional extension, each ignored when absent)
--------------------------------------------------------
Base keys used:  name, eras, costumes[{garment, material, wearer_rank, rite, era}],
plus phonology / morphology / lexicon / pantheon / symbols / names, which are
accepted and not read by this kernel.

Gate extension (all optional):
    era_dates: {<era>: [start, end] | {start, end}}   # packet timeline, compared
        directly with the CE anchor table below; use CE-comparable numbers.
    materials: [{material|name, composition|fiber, excluded_eras: [era],
                 routes: [{name, kind: local|import|reuse|alternative|excluded,
                           stage: fiber|yarn|cloth|garment|dye|trim, eras: [era]}]}]
        A route without `eras` supplies every declared era. An entry absent from
        `materials` is an undeclared route (HOLD), never an invented default.
    costumes[] extras: id, provenance: local-production|import|reuse|alternative,
        claimed_status: lawful|violation|disguise|contested|misdescribed,
        dye, closures|trims|fastenings|padding|thread (material names or maps),
        panels: [{name, width_m, seamless}], alternatives_excluded: bool,
        features: [stretch|...], fit, stretch_mechanism, processes: [<token>],
        badge_office|badge, color|colour, placement.
    rank_rules: [{id, authority, jurisdiction, eras, rites, effect:
                 prohibit|permit|require, property: {kind, value},
                 wearer_ranks, exempt_ranks}]
    supply: [{material, era, unit, demand: {wearers, per_issue, issues} |
              demand_exact | demand_range, routes: [{name, kind, stage, output |
              output_range}]}]
    cloth_sources: [{name, max_width_m, eras}]  # loom/cloth width bound for T-01
    tailoring: {alternatives_excluded: bool}    # packet-level fallback for T-01
    rejection_rules: [<token>]                  # audit rules the packet itself uses
    rules, claims (if present) are tolerated and not read by this kernel's
    R checks, which read `rank_rules` (documented in the handoff, not a waiver).

Finding IDs
-----------
    G-DATA   could-not-evaluate: malformed input / missing essentials (exit 2)
    G-ERA    costume or rank rule names an era not in `eras`                [hold]
    MAT-01   material given only as a market name, no separate identification [hold]
    MAT-02   material unavailable: explicitly excluded, or no route declared
             (excluded -> [reject]; undeclared/no routes -> [hold])
    MAT-03   provenance claim contradicted by the declared imported stage
             (local-production claimed, only route is an imported garment
              -> [reject]; import/alternative claimed, no such route, or an
              unrecognised provenance value -> [hold])
    MAT-04   declared dye has no declared availability                      [hold/reject]
    MAT-05   quantified demand exceeds the feasible supply upper bound
             -> [reject] shortfall; overlapping ranges or possible double-count
             -> [hold]
    MAT-06   reuse claimed, no reuse/stock route declared                   [hold]
    MAT-07   closure/trim/padding material unavailable                     [hold/reject]
    EAR-01   material routes declared, none covers this costume's era      [hold]
    EAR-04   rank rule has no effective interval (dated predicate required) [hold]
    E-01     dated process claimed before its anchor year -> [reject];
             era window missing or straddling the anchor -> [hold]
    T-01     seamless panel wider than every declared cloth source; piecing /
             stretching / alternatives excluded -> [reject]; not excluded,
             or cloth width undeclared -> [hold]
    T-02     stretch / close fit claimed with no mechanism named           [hold]
    T-03     the packet's own rejection rule "silk is never spun" contradicts
             corpus [M] (spun silk = discontinuous silk yarn) -> [reject]
    R-01     applicable prohibition retained as a declared violation       [note]
    R-02     applicable unexempted prohibition claimed as lawful          [reject]
    R-03     badge claims an office incompatible with the declared rank
             under a lawful claim -> [reject]; unresolved -> [hold]
    R-04     applicable prohibition, claim status undeclared / unrecognised [hold]
    R-05     two authorities (or a permit and a prohibition) conflict      [hold]
    R-06     rule applicability unresolved (wearer rank or rite undeclared) [hold]
    R-07     rank-rule element not modelled (property kind / effect)       [hold]

Anchors used by E-01 (corpus-attested, not an invention chronology): mauveine
1856 discovery / 1857 factory [S]; synthetic alizarin 1868–69, industrial
indigo 1897, saw gin 1793, flying shuttle 1733, power loom 1785, and the
c. 552 silk-reeling transfer to Byzantium — `textile-technology.md` §3/§4.

Out of kernel scope (do not read silence as a pass): the spec's EAR-05/06/07
(vocabulary, motif meaning, source composition), MAT-08 (maintenance), the
silhouette/layer grammar of `dress-through-eras.md`, and all object-level
provenance work. Documentation, curation, and any historical claim still need
the spec's manual audit and its `(to-verify)` discipline.

stdlib only; read-only; no network. The YAML reader is a deliberate subset
(2-space-friendlier indent blocks, flow lists/maps, quoted scalars, comments,
`|`/`>` block scalars); it is not a conforming YAML parser. A pure-JSON
packet (`.json`, or text beginning with `{`) is accepted as well.
"""

import json
import os
import re
import sys

EXIT_CLEAN = 0
EXIT_FINDINGS = 1
EXIT_CNE = 2

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE_DIR = os.path.join(HERE, "fixtures")
FIXTURE_NAME = "costume-era-consistency-gate"
FIXTURE_PATH = os.path.join(FIXTURE_DIR, FIXTURE_NAME + ".yml")
EXPECTED_PATH = os.path.join(FIXTURE_DIR, FIXTURE_NAME + ".expected")


# --------------------------------------------------------------------------
# A deliberately small YAML subset reader (comments, nested blocks, flow
# collections, quoted scalars, block scalars). Not a conforming YAML parser.
# --------------------------------------------------------------------------

def _strip_comment(line):
    quote = None
    for n, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (n == 0 or line[n - 1] in " \t"):
            return line[:n]
    return line


def _split_flow(text):
    parts, buf, depth, quote = [], [], 0, None
    for ch in text:
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
        elif ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if "".join(buf).strip():
        parts.append("".join(buf))
    return parts


def _scalar(token):
    token = token.strip()
    if not token:
        return None
    if len(token) >= 2 and token[0] in "\"'" and token[-1] == token[0]:
        inner = token[1:-1]
        if token[0] == '"':
            inner = (inner.replace('\\"', '"').replace("\\n", "\n")
                     .replace("\\\\", "\\"))
        return inner
    low = token.lower()
    if low in ("null", "~"):
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    if re.fullmatch(r"[-+]?\d+", token):
        return int(token)
    if re.fullmatch(r"[-+]?(\d+\.\d*|\.\d+)([eE][-+]?\d+)?", token):
        return float(token)
    return token


def _flow(text):
    text = text.strip()
    if text.startswith("[") and text.endswith("]"):
        out = []
        for part in _split_flow(text[1:-1]):
            part = part.strip()
            out.append(_flow(part) if part[:1] in "[{" else _scalar(part))
        return out
    if text.startswith("{") and text.endswith("}"):
        out = {}
        for part in _split_flow(text[1:-1]):
            key, sep, value = _split_key(part)
            if sep is None:
                raise ValueError("flow mapping entry without ':'")
            out[key] = _value(value)
        return out
    return _scalar(text)


def _value(token):
    token = token.strip()
    if token[:1] in "[{":
        return _flow(token)
    return _scalar(token)


def _split_key(text):
    quote, depth = None, 0
    for n, ch in enumerate(text):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == ":" and depth == 0:
            rest = text[n + 1:]
            if rest == "" or rest.startswith(" "):
                return _scalar(text[:n]), ":", rest.strip()
    return None, None, None


def _parse_map(lines, i, indent):
    out = {}
    while i < len(lines) and lines[i][0] == indent and not lines[i][1].startswith("-"):
        key, sep, value = _split_key(lines[i][1])
        if sep is None:
            raise ValueError("not a mapping entry: %r" % lines[i][1])
        i += 1
        if value in ("|", ">"):
            block = []
            while i < len(lines) and lines[i][0] > indent:
                block.append(lines[i][1])
                i += 1
            out[key] = (" " if value == ">" else "\n").join(block)
        elif value != "":
            out[key] = _value(value)
        elif i < len(lines) and lines[i][0] > indent:
            out[key], i = _parse(lines, i, lines[i][0])
        elif i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("-"):
            out[key], i = _parse_list(lines, i, indent)
        else:
            out[key] = None
    return out, i


def _parse_list(lines, i, indent):
    out = []
    while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("-"):
        item = lines[i][1][1:].strip()
        i += 1
        if item == "":
            if i < len(lines) and lines[i][0] > indent:
                child, i = _parse(lines, i, lines[i][0])
                out.append(child)
            else:
                out.append(None)
        elif item[:1] in "[{":
            out.append(_flow(item))
        else:
            key, sep, value = _split_key(item)
            if sep is None:
                out.append(_scalar(item))
                continue
            entry = {}
            if value != "":
                entry[key] = _value(value)
            elif i < len(lines) and lines[i][0] > indent:
                entry[key], i = _parse(lines, i, lines[i][0])
            else:
                entry[key] = None
            while i < len(lines) and lines[i][0] > indent:
                more, i = _parse_map(lines, i, lines[i][0])
                entry.update(more)
            out.append(entry)
    return out, i


def _parse(lines, i, indent):
    if lines[i][1].startswith("-"):
        return _parse_list(lines, i, indent)
    return _parse_map(lines, i, indent)


def parse_packet(text):
    """Return the packet mapping, or raise Malformed with a reason."""
    stripped = text.lstrip()
    if stripped.startswith("{"):
        try:
            value = json.loads(text)
        except ValueError as error:
            raise Malformed("JSON parse error: %s" % error)
        if not isinstance(value, dict):
            raise Malformed("root is not a mapping")
        return value
    lines = []
    for raw in text.replace("\t", "    ").split("\n"):
        line = _strip_comment(raw).rstrip()
        if not line.strip() or line.strip() in ("---", "..."):
            continue
        lines.append((len(line) - len(line.lstrip(" ")), line.strip()))
    if not lines:
        raise Malformed("empty input")
    try:
        value, i = _parse(lines, 0, lines[0][0])
    except (ValueError, IndexError) as error:
        raise Malformed("YAML subset parse error: %s" % error)
    if i != len(lines) or not isinstance(value, dict):
        raise Malformed("input is not one mapping (or has unparsed trailing lines)")
    return value


class Malformed(Exception):
    """Input cannot be evaluated by this kernel (exit 2)."""


# --------------------------------------------------------------------------
# Lenient normalisation helpers
# --------------------------------------------------------------------------

def key(text):
    return str(text).strip().casefold()


def same_era(a, b):
    return key(a) == key(b)


def need_list(value, what):
    if value is None:
        return []
    if not isinstance(value, list):
        raise Malformed("%s must be a list" % what)
    return value


def need_mapping(value, what):
    if not isinstance(value, dict):
        raise Malformed("%s must be a mapping" % what)
    return value


def as_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise Malformed("expected a number, got %r" % (value,))
    return value


def numbered(value, what):
    value = as_number(value)
    return value


def norm_eras(packet):
    raw = packet.get("eras")
    if raw is None:
        raise Malformed("no `eras` model declared: anachronism sweep not evaluable")
    raw = need_list(raw, "eras")
    names, dates = [], {}
    for entry in raw:
        if isinstance(entry, dict):
            name = entry.get("name") or entry.get("era")
            if not isinstance(name, str) or not name.strip():
                raise Malformed("era entry without a name")
            names.append(name.strip())
            start = entry.get("start")
            end = entry.get("end")
            if start is not None or end is not None:
                dates[key(name)] = (None if start is None else numbered(start, "era start"),
                                    None if end is None else numbered(end, "era end"))
        elif isinstance(entry, str) and entry.strip():
            names.append(entry.strip())
        else:
            raise Malformed("era entries must be names or mappings")
    if not names:
        raise Malformed("`eras` is empty: nothing to sweep")
    extra = packet.get("era_dates")
    if extra is not None:
        for name, span in need_mapping(extra, "era_dates").items():
            if isinstance(span, list):
                if len(span) != 2:
                    raise Malformed("era_dates[%s] must be [start, end]" % name)
                dates[key(name)] = (numbered(span[0], "era start"),
                                    numbered(span[1], "era end"))
            elif isinstance(span, dict):
                start, end = span.get("start"), span.get("end")
                dates[key(name)] = (None if start is None else numbered(start, "era start"),
                                    None if end is None else numbered(end, "era end"))
            else:
                raise Malformed("era_dates[%s] must be [start, end]" % name)
    return names, dates


def index_materials(packet):
    index = {}
    for n, entry in enumerate(need_list(packet.get("materials"), "materials")):
        entry = need_mapping(entry, "materials[%d]" % n)
        name = entry.get("material") or entry.get("name")
        if not isinstance(name, str) or not name.strip():
            raise Malformed("materials[%d] has no material name" % n)
        routes = []
        for route in need_list(entry.get("routes"), "routes of %s" % name):
            route = need_mapping(route, "route of %s" % name)
            eras = route.get("eras")
            if eras is not None:
                eras = need_list(eras, "route eras of %s" % name)
            routes.append({
                "name": route.get("name"),
                "kind": key(route.get("kind") or "unspecified"),
                "stage": key(route.get("stage") or "unspecified"),
                "eras": eras,
            })
        excluded = [str(e) for e in need_list(entry.get("excluded_eras"),
                                              "excluded_eras of %s" % name)]
        index[key(name)] = {
            "name": name,
            "routes": routes,
            "excluded_eras": excluded,
            "composition": entry.get("composition") or entry.get("fiber"),
            "raw": entry,
        }
    return index


def normalise_rules(packet):
    rules = []
    for n, rule in enumerate(need_list(packet.get("rank_rules"), "rank_rules")):
        rule = need_mapping(rule, "rank_rules[%d]" % n)
        prop = rule.get("property")
        if prop is None:
            prop = {}
        prop = need_mapping(prop, "property of rank_rules[%d]" % n)
        eras = rule.get("eras")
        if eras is not None:
            eras = need_list(eras, "rank_rules[%d].eras" % n)
        rites = rule.get("rites", rule.get("occasions"))
        if rites is not None:
            rites = need_list(rites, "rank_rules[%d].rites" % n)
        rules.append({
            "id": rule.get("id") or "rank_rules[%d]" % n,
            "authority": rule.get("authority"),
            "jurisdiction": rule.get("jurisdiction"),
            "eras": eras,
            "rites": rites,
            "effect": key(rule.get("effect") or ""),
            "kind": key(prop.get("kind") or ""),
            "value": prop.get("value"),
            "wearer_ranks": (None if rule.get("wearer_ranks") is None
                             else [str(x) for x in need_list(rule.get("wearer_ranks"),
                                                             "rank_rules[%d].wearer_ranks" % n)]),
            "exempt_ranks": ([] if rule.get("exempt_ranks") is None
                             else [str(x) for x in need_list(rule.get("exempt_ranks"),
                                                             "rank_rules[%d].exempt_ranks" % n)]),
        })
    return rules


# --------------------------------------------------------------------------
# Evaluation
# --------------------------------------------------------------------------

VAGUE_MATERIALS = {
    "silk-like", "silklike", "silk substitute", "silk-substitute", "mock silk",
    "silk look", "wool-like", "woollike", "damask-like", "damasklike",
    "scarlet",
}

COLOUR_WORDS = {"mauve", "purple", "magenta", "violet", "scarlet", "crimson",
                "blue", "green", "red", "yellow", "black", "white"}

PROCESS_ANCHORS = {
    "mauveine": (1856, "mauveine: 1856 synthesis, 1857 factory [S]"),
    "perkin-s-mauve": (1856, "Perkin's mauveine: 1856 synthesis, 1857 factory [S]"),
    "perkins-mauve": (1856, "Perkin's mauveine: 1856 synthesis, 1857 factory [S]"),
    "aniline-mauve": (1856, "aniline mauve: 1856 synthesis, 1857 factory [S]"),
    "synthetic-alizarin": (1868, "synthetic alizarin: 1868–69 (`textile-technology.md` §3)"),
    "alizarin-synthesis": (1868, "synthetic alizarin: 1868–69 (`textile-technology.md` §3)"),
    "synthetic-indigo": (1897, "industrial indigo synthesis: 1897 (`textile-technology.md` §3)"),
    "indigo-synthesis": (1897, "industrial indigo synthesis: 1897 (`textile-technology.md` §3)"),
    "saw-gin": (1793, "saw gin: 1793 (`textile-technology.md` §2)"),
    "power-loom": (1785, "Cartwright power loom: 1785 (`textile-technology.md` §4)"),
    "flying-shuttle": (1733, "Kay flying shuttle: 1733 (`textile-technology.md` §4)"),
    "byzantine-silk-reeling": (552, "silk-reeling to Byzantium: c. 552 (Procopius, `Wars` 8.17)"),
}

REJECTED_RULE_TOKENS = {
    "silk-is-never-spun": "spun silk is a discontinuous-silk/waste yarn [M]; the rule conflates filament and spun silk",
    "silk-never-spun": "spun silk is a discontinuous-silk/waste yarn [M]; the rule conflates filament and spun silk",
    "all-silk-must-be-reeled": "spun silk is a discontinuous-silk/waste yarn [M]; the rule conflates filament and spun silk",
}

PROVENANCE = {"local-production", "local", "import", "imported", "reuse",
              "heirloom", "stock", "alternative", "substitute", "unspecified"}


def token(text):
    return re.sub(r"[^a-z0-9]+", "-", str(text).casefold()).strip("-")


def slot_name(cos, n):
    label = cos.get("id") or cos.get("garment") or "row %d" % n
    return str(label)


def era_covers(route, era):
    return route["eras"] is None or any(same_era(era, e) for e in route["eras"])


def availability(entry, era):
    """('ok'|'excluded'|'no-route'|'undeclared'|'no-era', detail)."""
    if entry is None:
        return "undeclared", None
    for excluded in entry["excluded_eras"]:
        if same_era(era, excluded):
            return "excluded", {"name": excluded}
    routes = entry["routes"]
    if not routes:
        return "no-route", None
    refused = [r for r in routes if r["kind"] == "excluded" and era_covers(r, era)]
    if refused:
        return "excluded", refused[0]
    covering = [r for r in routes if r["kind"] != "excluded" and era_covers(r, era)]
    if covering:
        return "ok", covering
    return "no-era", None


AVAILABILITY_ROUTING = {
    "main": {"undeclared": ("MAT-02", "hold"), "no-route": ("MAT-02", "hold"),
             "excluded": ("MAT-02", "reject"), "no-era": ("EAR-01", "hold")},
    "component": {"undeclared": ("MAT-07", "hold"), "no-route": ("MAT-07", "hold"),
                  "excluded": ("MAT-07", "reject"), "no-era": ("MAT-07", "hold")},
    "dye": {"undeclared": ("MAT-04", "hold"), "no-route": ("MAT-04", "hold"),
            "excluded": ("MAT-04", "reject"), "no-era": ("MAT-04", "hold")},
}


def components_of(cos, names):
    """Flatten e.g. closures: [silver-hook, {material: x}] to a list of names."""
    out = []
    for field in names:
        raw = cos.get(field)
        if raw is None:
            continue
        items = raw if isinstance(raw, list) else [raw]
        for item in items:
            if isinstance(item, dict):
                name = item.get("material") or item.get("name")
            else:
                name = item
            if name:
                out.append((field, str(name)))
    return out


def evaluate(packet):
    """Return (findings, exit_code); findings are (id, severity, message)."""
    if not isinstance(packet, dict):
        raise Malformed("root is not a mapping")
    outfits = packet.get("costumes")
    if outfits is None:
        raise Malformed("no `costumes` declared: nothing to review")
    outfits = need_list(outfits, "costumes")
    if not outfits:
        raise Malformed("`costumes` is empty: nothing to review")
    for n, cos in enumerate(outfits):
        need_mapping(cos, "costumes[%d]" % n)
    era_names, era_dates = norm_eras(packet)
    materials = index_materials(packet)
    rules = normalise_rules(packet)
    findings = []

    def add(fid, severity, message):
        findings.append((fid, severity, " ".join(str(message).split())))

    declared = {key(e) for e in era_names}

    # ---- packet-level: the packet's own rejection rules (spec §5 guard) -----
    for token_raw in need_list(packet.get("rejection_rules"), "rejection_rules"):
        probe = token(token_raw)
        if probe in REJECTED_RULE_TOKENS:
            add("T-03", "reject",
                "rejection rule %r is invalid: %s — withdraw it before judging any "
                "material" % (str(token_raw), REJECTED_RULE_TOKENS[probe]))

    # ---- rank rules: rule-level prerequisites (dated predicate, §6) ---------
    for rule in rules:
        if rule["eras"] is None:
            add("EAR-04", "hold",
                "rank rule %s has no effective interval: legal dress is a dated "
                "predicate — locate the rule's version before applying it" % rule["id"])
        else:
            missing = [e for e in rule["eras"] if key(e) not in declared]
            if missing:
                add("G-ERA", "hold",
                    "rank rule %s names era(s) %s not declared in `eras`: its window "
                    "cannot be resolved" % (rule["id"], ", ".join(map(str, missing))))
        if rule["kind"] not in ("material", "fiber", "cloth", "fabric", "textile",
                                "dye", "dyestuff", "garment", "robe", "clothing",
                                "trim", "closure", "fastening", "badge", "insignia",
                                "placement", "hue", "color", "colour"):
            add("R-07", "hold",
                "rank rule %s regulates property kind %r, which this kernel does not "
                "model; the rule is not applied (audit it manually)"
                % (rule["id"], rule["kind"] or "?"))
        if rule["effect"] not in ("prohibit", "permit", "require"):
            add("R-07", "hold",
                "rank rule %s has effect %r outside prohibit|permit|require; the rule "
                "is not applied" % (rule["id"], rule["effect"] or "?"))
        if rule["value"] is None:
            add("R-07", "hold",
                "rank rule %s declares no regulated property value; the rule is not "
                "applied" % rule["id"])

    # ---- textiles: the packet's own stated bounds --------------------------
    tailoring = packet.get("tailoring") or {}
    if tailoring and not isinstance(tailoring, dict):
        raise Malformed("tailoring must be a mapping")
    packet_alternatives_excluded = bool(tailoring.get("alternatives_excluded"))

    # ---- costumes ----------------------------------------------------------
    for n, cos in enumerate(outfits):
        label = slot_name(cos, n)
        era = cos.get("era")
        if not era:
            add("G-ERA", "hold",
                "%s: no era declared — the material/era and rank checks cannot be "
                "run for this row" % label)
            dated = False
        elif key(era) not in declared:
            add("G-ERA", "hold",
                "%s: era %r is not in `eras` — anachronism sweep cannot date this row"
                % (label, era))
            dated = False
        else:
            dated = True

        material = cos.get("material")
        provenance = key(cos.get("provenance") or "")
        claimed = cos.get("claimed_status")
        claimed_key = key(claimed) if claimed is not None else None

        if material is None or str(material).strip() == "":
            add("MAT-02", "hold",
                "%s: no material declared — the availability route is unknown"
                % label)
        elif key(material) in VAGUE_MATERIALS and not (
                materials.get(key(material), {}).get("composition")):
            add("MAT-01", "hold",
                "%s: material %r is a market/vague name without a separate fiber or "
                "composition identification" % (label, material))

        if dated and material is not None and str(material).strip():
            entry = materials.get(key(material))
            status, detail = availability(entry, era)
            if status != "ok":
                fid, severity = AVAILABILITY_ROUTING["main"][status]
                if status == "excluded":
                    which = (detail or {}).get("name")
                    reason = ("explicitly excluded in %s%s"
                              % (era, "" if not which else " by `excluded_eras: %s`" % which))
                    message = ("%s: material %r is %s; a declaration of exclusion is a "
                               "closed inventory, not an absent-evidence guess"
                               % (label, material, reason))
                elif status == "no-era":
                    message = ("%s: material %r has declared routes, but none covers %s "
                               "— timing unresolved (HOLD), not proven unavailable"
                               % (label, material, era))
                elif status == "no-route":
                    message = ("%s: material %r is declared with no supply route — "
                               "source/preparation/yarn/cloth route unknown"
                               % (label, material))
                else:
                    message = ("%s: material %r has no entry in the packet's material "
                               "declarations — route unknown (HOLD), and never invent "
                               "a default" % (label, material))
                add(fid, severity, message)

            # MAT-03 / MAT-06: route claims against the declared import stage
            if provenance and provenance not in PROVENANCE:
                add("MAT-03", "hold",
                    "%s: provenance %r is outside local-production|import|reuse|"
                    "alternative — the route claim cannot be checked" % (label, provenance))
            if status == "ok":
                covering = detail
                import_routes = [r for r in covering if r["kind"] in ("import", "imported")]
                local_routes = [r for r in covering if r["kind"] in ("local", "local-production")]
                reuse_routes = [r for r in covering if r["kind"] in ("reuse", "heirloom", "stock")]
                if provenance in ("local-production", "local") and not local_routes:
                    if import_routes and all(r["stage"] == "garment" for r in import_routes):
                        add("MAT-03", "reject",
                            "%s: local production of %r is claimed, but the only declared "
                            "route is an imported finished garment — an imported robe is "
                            "not evidence of local rearing, reeling, or weaving"
                            % (label, material))
                    elif import_routes:
                        add("MAT-03", "hold",
                            "%s: local production of %r is claimed from imported %s; the "
                            "local operation must be named before the claim is checkable"
                            % (label, material,
                               "/".join(sorted({r["stage"] for r in import_routes}))))
                if provenance in ("import", "imported") and not import_routes:
                    add("MAT-03", "hold",
                        "%s: imported provenance is claimed for %r but no import route "
                        "covers %s — name the imported stage (fiber, yarn, cloth, garment)"
                        % (label, material, era))
                if provenance in ("alternative", "substitute") and not any(
                        r["kind"] in ("alternative", "substitute") for r in covering):
                    add("MAT-03", "hold",
                        "%s: an alternative/substitute route is claimed for %r but none "
                        "is declared" % (label, material))
                if provenance in ("reuse", "heirloom", "stock") and not reuse_routes:
                    add("MAT-06", "hold",
                        "%s: reuse/inherited cloth is claimed for %r but no reuse or "
                        "stock route is declared — account for the object's biography"
                        % (label, material))

            # MAT-04: dye availability is tracked separately from the substrate
            dye = cos.get("dye")
            if dye is not None and str(dye).strip():
                dye_status, _ = availability(materials.get(key(dye)), era)
                if dye_status != "ok":
                    fid, severity = AVAILABILITY_ROUTING["dye"][dye_status]
                    add(fid, severity,
                        "%s: dye %r has no declared availability in %s — track dyestuff, "
                        "auxiliaries, substrate, and process separately from the garment"
                        % (label, dye, era))

            # MAT-07: closures, trimming, padding, thread, metal components
            for field, comp in components_of(cos, ("closures", "trims", "fastenings",
                                                   "padding", "thread")):
                comp_status, _ = availability(materials.get(key(comp)), era)
                if comp_status != "ok":
                    fid, severity = AVAILABILITY_ROUTING["component"][comp_status]
                    if comp_status == "excluded":
                        message = ("%s: %s material %r is explicitly excluded in %s; "
                                   "reviewing only the outer fabric hides this"
                                   % (label, field, comp, era))
                    elif comp_status == "no-era":
                        message = ("%s: %s material %r has routes, none covering %s — "
                                   "component timing unresolved" % (label, field, comp, era))
                    else:
                        message = ("%s: %s material %r has no declared route — closures, "
                                   "thread, and stiffening are part of the outfit"
                                   % (label, field, comp))
                    add(fid, severity, message)

        # ---- T-02: a fit claim must name its mechanism (spec §5) ------------
        features = cos.get("features")
        if isinstance(features, str):
            features = [features]
        feature_tokens = {token(f) for f in need_list(features, "costume features")}
        fit = key(cos.get("fit") or "")
        if feature_tokens & {"stretch", "stretch-fit", "elastic", "elasticity"} or fit in ("close", "stretch"):
            mechanism = (cos.get("stretch_mechanism") or cos.get("fit_mechanism")
                         or cos.get("mechanism"))
            if not mechanism:
                add("T-02", "hold",
                    "%s: stretch/close fit is claimed with no mechanism named — a "
                    "stretch claim does not imply a modern elastomer; specify knit, "
                    "bias, lacing, shaped panels, or elastic fibre before dating it"
                    % label)

        # ---- T-01: seamless panel against the declared cloth widths ---------
        panels = need_list(cos.get("panels"), "costume panels")
        if panels and dated:
            sources = []
            for source in need_list(packet.get("cloth_sources"), "cloth_sources"):
                source = need_mapping(source, "cloth_sources entry")
                sources.append(source)
            covering = [s for s in sources
                        if s.get("eras") is None
                        or any(same_era(era, e) for e in need_list(s.get("eras"), "cloth source eras"))]
            widths = [numbered(s.get("max_width_m"), "max_width_m") for s in covering
                      if s.get("max_width_m") is not None]
            for panel in panels:
                panel = need_mapping(panel, "costume panel")
                if not panel.get("seamless"):
                    continue
                width = panel.get("width_m")
                if width is None:
                    add("T-01", "hold",
                        "%s: seamless panel %r has no width — panel feasibility not "
                        "evaluable" % (label, panel.get("name") or "?"))
                    continue
                width = numbered(width, "panel width")
                if not widths:
                    add("T-01", "hold",
                        "%s: no cloth source covering %s declares a usable width — "
                        "seam/piecing/alternative routes unresolved"
                        % (label, era))
                elif width > max(widths):
                    excluded = (packet_alternatives_excluded
                                or bool(cos.get("alternatives_excluded")))
                    if excluded:
                        add("T-01", "reject",
                            "%s: seamless panel %r is %sm wide; every declared cloth "
                            "source covering %s is at most %sm wide, and piecing / "
                            "stretching / alternative sources are excluded"
                            % (label, panel.get("name") or "?", width, era, max(widths)))
                    else:
                        add("T-01", "hold",
                            "%s: seamless panel %r (%sm) exceeds the widest declared "
                            "cloth source covering %s (%sm); a seam, import, or "
                            "alternative route is not excluded — investigate before "
                            "rejecting" % (label, panel.get("name") or "?", width,
                                           era, max(widths)))

        # ---- E-01: dated process before its anchor --------------------------
        processes = cos.get("processes")
        if isinstance(processes, str):
            processes = [processes]
        for process in need_list(processes, "costume processes"):
            probe = token(process)
            anchor = PROCESS_ANCHORS.get(probe)
            if anchor is None:
                guard = (" — a colour word is not a dyestuff identification"
                         if probe in COLOUR_WORDS else "")
                add("E-01", "hold",
                    "%s: process %r has no anchor in this kernel's table; identify the "
                    "actual process before dating it%s" % (label, process, guard))
                continue
            year, note = anchor
            if not dated:
                add("E-01", "hold",
                    "%s: process %r (%s) cannot be dated against era %r"
                    % (label, process, note, era))
                continue
            start, end = era_dates.get(key(era), (None, None))
            if start is None or end is None:
                add("E-01", "hold",
                    "%s: process %r (%s) is claimed, but era %r has no declared date "
                    "window" % (label, process, note, era))
            elif end < year:
                add("E-01", "reject",
                    "%s: process %r requires %s, which falls after the declared end of "
                    "%s (%s) — an alternative invention or route needs its own "
                    "dependency chain, not a fantasy exemption"
                    % (label, process, note, era, end))
            elif start < year <= end:
                add("E-01", "hold",
                    "%s: process %r (%s) enters only late in %s (%s–%s); narrow the "
                    "claimed date or declare an alternative route"
                    % (label, process, note, era, start, end))

        # ---- R-01..R-06: rank-rule conflicts --------------------------------
        wearer = cos.get("wearer_rank")
        rite = cos.get("rite")
        property_hits = []
        for rule in rules:
            if rule["eras"] is None or rule["value"] is None:
                continue
            if not dated:
                continue  # the row's era is unresolved; G-ERA already reported it
            if not any(same_era(era, e) for e in rule["eras"]):
                continue
            if not property_match(rule, cos):
                continue
            if rule["effect"] not in ("prohibit", "permit"):
                continue
            if rule["wearer_ranks"] and wearer is None:
                add("R-06", "hold",
                    "%s: rank rule %s is scoped to wearer categories, but this row "
                    "declares no wearer_rank — entitlement cannot be resolved"
                    % (label, rule["id"]))
                continue
            if rule["wearer_ranks"] and wearer is not None and not any(
                    key(wearer) == key(w) for w in rule["wearer_ranks"]):
                continue
            if rule["rites"] is not None:
                if rite is None:
                    add("R-06", "hold",
                        "%s: rank rule %s grants/denies %s only on occasion(s) %s, but "
                        "this row declares no rite — the legality claim stays unresolved"
                        % (label, rule["id"], rule["value"],
                           "/".join(map(str, rule["rites"]))))
                    property_hits.append(("scope-unresolved", rule))
                    continue
                if not any(key(rite) == key(r) for r in rule["rites"]):
                    continue
            if any(key(wearer) == key(x) for x in rule["exempt_ranks"]):
                continue
            property_hits.append((rule["effect"], rule))

        prohibitions = [r for effect, r in property_hits
                        if effect == "prohibit" and r["effect"] == "prohibit"]
        permits = [r for effect, r in property_hits
                   if effect == "permit" and r["effect"] == "permit"]
        scoped = [r for effect, r in property_hits if effect == "scope-unresolved"]
        if scoped and (prohibitions or permits):
            # R-06 already reported the unresolved occasion scope; do not reject.
            pass
        elif prohibitions and permits:
            add("R-05", "hold",
                "%s: prohibition %s (%s) and permission %s (%s) both apply — record an "
                "authority conflict and hold unqualified legality until jurisdiction or "
                "priority is specified"
                % (label, prohibitions[0]["id"], prohibitions[0]["authority"] or "?",
                   permits[0]["id"], permits[0]["authority"] or "?"))
        elif prohibitions:
            rule = prohibitions[0]
            detail = ("%s: applicable prohibition %s (%s) covers %s"
                      % (label, rule["id"], rule["authority"] or "authority not named",
                         rule["value"]))
            if claimed_key in ("violation", "disguise", "contested", "misdescribed"):
                add("R-01", "note",
                    "%s as a declared %s — keep the violation, recognition, and likely "
                    "response visible; material/technical review continues"
                    % (detail, claimed_key))
            elif claimed_key == "lawful":
                add("R-02", "reject",
                    "%s, and the packet claims unqualified lawful entitlement with no "
                    "exemption on record — do not silently invent a grant" % detail)
            elif claimed_key == "n/a":
                pass
            else:
                add("R-04", "hold",
                    "%s, but the claim is not declared as lawful wear, violation, "
                    "disguise/contested recognition, or misdescribed insignia — resolve "
                    "the claim before the rule can be judged%s"
                    % (detail, "" if claimed_key is None else " (status %r)" % claimed))

        # ---- R-03: badge/insignia vs. declared rank --------------------------
        badge = cos.get("badge_office") or cos.get("badge")
        if badge is not None and str(badge).strip():
            if wearer is None:
                add("R-03", "hold",
                    "%s: badge %r is claimed but no wearer rank is declared — "
                    "certification cannot be checked" % (label, badge))
            elif key(badge) != key(wearer):
                if claimed_key == "lawful":
                    add("R-03", "reject",
                        "%s: badge %r is said to certify the wearer, but the declared "
                        "rank is %r — the stipulated code is contradicted; check reuse, "
                        "transfer, or retrospective misidentification before repair"
                        % (label, badge, wearer))
                elif claimed_key in ("violation", "disguise", "contested", "misdescribed"):
                    add("R-03", "note",
                        "%s: badge %r against rank %r reads as a declared %s — a coherent "
                        "scenario; do not silently promote the wearer to the badge's office"
                        % (label, badge, wearer, claimed_key))
                else:
                    add("R-03", "hold",
                        "%s: badge %r does not match the declared rank %r and the claim "
                        "is undeclared — resolve lawful wear, impersonation, or "
                        "misdescription first" % (label, badge, wearer))

    # ---- MAT-05: quantified demand against feasible supply ------------------
    for entry in need_list(packet.get("supply"), "supply"):
        entry = need_mapping(entry, "supply entry")
        where = str(entry.get("material") or "unspecified material")
        unit = str(entry.get("unit") or "units")
        era = entry.get("era")
        routes = []
        for route in need_list(entry.get("routes"), "supply routes"):
            route = need_mapping(route, "supply route")
            if route.get("output") is not None:
                value = numbered(route.get("output"), "route output")
                routes.append((value, value, route))
            elif route.get("output_range") is not None:
                span = need_list(route.get("output_range"), "output_range")
                if len(span) != 2:
                    raise Malformed("output_range must be [min, max]")
                routes.append((numbered(span[0], "output min"),
                               numbered(span[1], "output max"), route))
            elif route.get("output_min") is not None or route.get("output_max") is not None:
                routes.append((numbered(route.get("output_min", 0), "output min"),
                               numbered(route.get("output_max", 0), "output max"), route))
            else:
                raise Malformed("supply route has no output")
        demand = None
        demand_range = None
        if entry.get("demand_exact") is not None:
            demand = numbered(entry["demand_exact"], "demand_exact")
        elif entry.get("demand_range") is not None:
            span = need_list(entry.get("demand_range"), "demand_range")
            if len(span) != 2:
                raise Malformed("demand_range must be [min, max]")
            demand_range = (numbered(span[0], "demand min"), numbered(span[1], "demand max"))
        elif isinstance(entry.get("demand"), dict):
            spec = entry["demand"]
            parts = [spec.get("wearers"), spec.get("per_issue"), spec.get("issues")]
            if all(p is not None for p in parts):
                product = 1
                for p in parts:
                    product *= numbered(p, "demand factor")
                demand = product
            else:
                demand = None
        elif entry.get("demand") is not None:
            demand = numbered(entry["demand"], "demand")
        if demand is None and demand_range is None:
            add("MAT-05", "hold",
                "supply for %s%s is declared without a quantified demand — give exact "
                "or ranged figures before claiming a capacity bound"
                % (where, " in %s" % era if era else ""))
            continue
        if demand_range is None:
            demand_range = (demand, demand)
        if not routes:
            add("MAT-05", "hold",
                "supply for %s%s declares demand but no routes — feasible output "
                "unknown" % (where, " in %s" % era if era else ""))
            continue
        low_total = sum(r[0] for r in routes)
        high_total = sum(r[1] for r in routes)
        # Double-count guard (spec §4): imported yarn/fiber is not also cloth.
        stages = {r[2].get("stage") and key(r[2]["stage"]) for r in routes}
        kinds = {r[2].get("kind") and key(r[2]["kind"]) for r in routes}
        upstream_import = any(r[2].get("kind") and key(r[2]["kind"]) in ("import", "imported")
                              and r[2].get("stage") and key(r[2]["stage"]) in ("fiber", "yarn")
                              for r in routes)
        local_fabric = any(r[2].get("kind") and key(r[2]["kind"]) in ("local", "local-production")
                           and r[2].get("stage") and key(r[2]["stage"]) in ("cloth", "garment")
                           for r in routes)
        if upstream_import and local_fabric and not entry.get("independent_routes"):
            add("MAT-05", "hold",
                "supply for %s%s sums imported fiber/yarn alongside locally woven "
                "cloth — possible double-count; confirm route independence or declare "
                "`independent_routes: true`" % (where, " in %s" % era if era else ""))
        if demand_range[0] > high_total:
            add("MAT-05", "reject",
                "supply for %s%s: minimum required demand %s %s exceeds the maximum "
                "feasible supply %s %s (shortfall %s %s) — ambiguous sum: only "
                "independent routes, plus usable stock, may be added"
                % (where, " in %s" % era if era else "", demand_range[0], unit,
                   high_total, unit, demand_range[0] - high_total, unit))
        elif demand_range[1] <= low_total:
            pass  # demand met even at the pessimistic supply bound
        else:
            add("MAT-05", "hold",
                "supply for %s%s: demand %s–%s %s overlaps feasible supply %s–%s %s — "
                "investigate the slowest stage; do not report a falsely precise bound"
                % (where, " in %s" % era if era else "", demand_range[0], demand_range[1],
                   unit, low_total, high_total, unit))

    deduped = []
    seen = set()
    for finding in findings:
        if finding in seen:
            continue
        seen.add(finding)
        deduped.append(finding)
    code = EXIT_FINDINGS if deduped else EXIT_CLEAN
    return deduped, code


def property_match(rule, cos):
    """True/False, or None when the rule's property kind is not modelled."""
    kind, value = rule["kind"], str(rule["value"]).casefold()
    if kind in ("material", "fiber", "cloth", "fabric", "textile"):
        target = cos.get("material")
        return target is not None and key(target) == key(value)
    if kind in ("dye", "dyestuff"):
        target = cos.get("dye")
        return target is not None and key(target) == key(value)
    if kind in ("garment", "robe", "clothing"):
        target = cos.get("garment")
        if target is None:
            return False
        target = key(target)
        return target == key(value) or (len(value) >= 4 and key(value) in target)
    if kind in ("trim", "closure", "fastening"):
        names = [name for _, name in components_of(cos, ("closures", "trims",
                                                         "fastenings", "padding",
                                                         "thread"))]
        return any(key(name) == key(value) for name in names)
    if kind in ("badge", "insignia"):
        target = cos.get("badge_office") or cos.get("badge")
        return target is not None and key(target) == key(value)
    if kind == "placement":
        target = cos.get("placement")
        return target is not None and key(target) == key(value)
    if kind in ("hue", "color", "colour"):
        target = cos.get("color") or cos.get("colour")
        return target is not None and key(target) == key(value)
    return None


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

USAGE = ("usage: costume-era-consistency-gate.py <culture-packet.yml>\n"
         "       costume-era-consistency-gate.py --selftest\n"
         "exit: 0 clean / 1 findings / 2 could-not-evaluate")


def run_text(text):
    def gdata(reason):
        return "FINDING G-DATA: [could-not-evaluate] %s" % " ".join(str(reason).split())

    try:
        packet = parse_packet(text)
    except Malformed as error:
        return EXIT_CNE, [gdata(error)]
    try:
        findings, code = evaluate(packet)
    except Malformed as error:
        return EXIT_CNE, [gdata(error)]
    except (KeyError, TypeError, ValueError, IndexError, AttributeError) as error:
        return EXIT_CNE, [gdata("kernel fault on this packet: %s: %s"
                                % (type(error).__name__, error))]
    lines = ["FINDING %s: [%s] %s" % (fid, severity, message)
             for fid, severity, message in findings]
    return code, lines


def run_file(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeError) as error:
        return EXIT_CNE, ["FINDING G-DATA: [could-not-evaluate] cannot read %s: %s"
                          % (path, error)]
    return run_text(text)


# --------------------------------------------------------------------------
# Selftest fixture — synthetic audit packet, not fictional canon.
# --------------------------------------------------------------------------

FIXTURE = '''# costume-era-consistency-gate — synthetic audit fixture (NOT canon).
# One fictional packet "Kedrun Delta" with planted violations covering every
# finding ID in the .expected file. Clean rows (c_priestess_linen,
# c_smith_apron) are included so the fixture is not a wall of failures.
name: "Kedrun Delta (gate fixture, not canon)"
phonology: {consonants: [p, t, k, m, n, s, l, r], vowels: [a, e, i, o, u], phonotactics: "(C)V(C)", tones: 0, notable_rules: ["no word-final voiced stops"]}
morphology: {type: agglutinative, alignment: nom-acc, word_order: SOV}
lexicon:
  - {term: sirna, gloss: "flax thread", field: textile, etymology: "native", layer: native}
  - {term: mahul, gloss: "imported figured cloth", field: textile, etymology: "coastal trade language loan", layer: loan}
pantheon:
  - {name: Oru, role: "patron of weavers", domain: craft, era: "Reed Age"}
symbols:
  - {sign: "twelve-reed circle", domain: craft, era: "Reed Age", notes: "counts the twelve months"}
names:
  - {name: Kedrun, type: place, etymology: "ked 'reed' + run 'mouth'", era: "Reed Age"}
eras: ["Reed Age", "Loom Age", "Steam Age"]
era_dates:
  "Reed Age": [-400, 300]
  "Loom Age": [300, 1500]
  "Steam Age": [1500, 1840]

materials:
  - material: linen
    composition: "bast fiber, Linum-like"
    routes:
      - {kind: local, stage: fiber, eras: ["Reed Age", "Loom Age", "Steam Age"]}
      - {kind: local, stage: cloth}
  - material: hemp
    composition: "bast fiber"
    routes:
      - {kind: local, stage: cloth}
  - material: wool
    routes:
      - {kind: local, stage: cloth}
  - material: silk
    composition: "filament fibre, Bombyx-like"
    routes:
      - {kind: import, stage: garment, eras: ["Loom Age", "Steam Age"]}
  - material: cotton
    routes:
      - {kind: import, stage: cloth, eras: ["Loom Age"]}
    excluded_eras: ["Reed Age"]
  - material: "silk-like"
    routes:
      - {kind: import, stage: cloth}
  - material: silver-hook
    routes:
      - {kind: local, stage: trim, eras: ["Steam Age"]}
  - material: mauveine
    composition: "synthetic dyestuff"
    routes:
      - {kind: import, stage: dye, eras: ["Steam Age"]}

cloth_sources:
  - {name: "Kedrun ground loom", max_width_m: 0.6, eras: ["Reed Age", "Loom Age"]}
  - {name: "steam broadloom", max_width_m: 1.4, eras: ["Steam Age"]}

rejection_rules: ["silk is never spun"]

rank_rules:
  - id: rule-silk-guild
    authority: "Kedrun guild court"
    jurisdiction: "Kedrun city"
    eras: ["Loom Age"]
    effect: prohibit
    property: {kind: material, value: silk}
    wearer_ranks: [merchant]
  - id: rule-silk-crown
    authority: "Crown warrant"
    jurisdiction: "Kedrun city"
    eras: ["Loom Age"]
    rites: ["Crown Jubilee"]
    effect: permit
    property: {kind: material, value: silk}
    wearer_ranks: [merchant]
  - id: rule-earl-wolfskin
    authority: "Herald's table"
    effect: prohibit
    property: {kind: material, value: wolfskin}
    wearer_ranks: [peddler]
  - id: rule-vermillion
    authority: "Kedrun guild court"
    eras: ["Age of Sail"]
    effect: prohibit
    property: {kind: dye, value: vermillion}
    wearer_ranks: [merchant]
  - id: rule-price-cap
    authority: "Crown warrant"
    eras: ["Loom Age"]
    effect: prohibit
    property: {kind: price, value: "12 shillings"}

supply:
  - material: wool
    era: "Loom Age"
    unit: m2
    demand: {wearers: 200, per_issue: 2, issues: 2}
    routes:
      - {name: "Kedrun fulling mill", kind: local, output: 500}
      - {name: "coastal import", kind: import, output: 200}
      - {name: "old stock", kind: reuse, output: 50}
  - material: silk
    era: "Loom Age"
    unit: m2
    demand_exact: 100
    routes:
      - {name: "imported raw silk", kind: import, stage: yarn, output: 60}
      - {name: "local cloth", kind: local, stage: cloth, output: 60}

costumes:
  - id: c_priestess_linen
    garment: "linen temple mantle"
    material: linen
    wearer_rank: priestess
    rite: "Reed consecration"
    era: "Reed Age"
    provenance: local-production
    claimed_status: lawful
  - id: c_smith_apron
    garment: "hemp work apron"
    material: hemp
    wearer_rank: smith
    rite: "forge blessing"
    era: "Reed Age"
    provenance: local-production
  - id: c_merchant_silk
    garment: "silk under-robe"
    material: silk
    wearer_rank: merchant
    rite: "guild assembly"
    era: "Loom Age"
    provenance: local-production
    claimed_status: lawful
  - id: c_delta_kilt
    garment: "cotton kilt"
    material: cotton
    wearer_rank: elder
    rite: "delta assize"
    era: "Reed Age"
  - id: c_steam_cotton
    garment: "cotton day gown"
    material: cotton
    wearer_rank: noble
    era: "Steam Age"
  - id: c_shroud_panel
    garment: "shroud mantle"
    material: linen
    wearer_rank: mourner
    rite: "laying out"
    era: "Loom Age"
    panels: [{name: "mantle panel", width_m: 1.4, seamless: true}]
    alternatives_excluded: true
  - id: c_mauveine_gown
    garment: "court gown"
    material: wool
    wearer_rank: noble
    rite: "court assembly"
    era: "Steam Age"
    dye: mauveine
    processes: [mauveine]
  - id: c_sail_era
    garment: "sailcloth cloak"
    material: linen
    wearer_rank: sailor
    era: "Age of Sail"
  - id: c_moonthread
    garment: "moonthread veil"
    material: moonthread
    wearer_rank: oracle
    era: "Loom Age"
  - id: c_silklike_cloak
    garment: "silk-like cloak"
    material: "silk-like"
    wearer_rank: envoy
    era: "Loom Age"
  - id: c_relic_brocade
    garment: "inherited brocade"
    material: silk
    wearer_rank: shrine-keeper
    rite: "relic procession"
    era: "Loom Age"
    provenance: reuse
  - id: c_hook_belt
    garment: "belted tunic"
    material: linen
    wearer_rank: guard
    era: "Loom Age"
    closures: [silver-hook]
  - id: c_saffron_veil
    garment: "saffron veil"
    material: wool
    wearer_rank: dancer
    era: "Loom Age"
    dye: saffron
  - id: c_import_hemp
    garment: "hemp rain cloak"
    material: hemp
    wearer_rank: peddler
    era: "Loom Age"
    provenance: import
  - id: c_stretch_hose
    garment: "stretch hose"
    material: wool
    wearer_rank: dancer
    era: "Loom Age"
    features: [stretch]
    fit: close
  - id: c_badge_minister
    garment: "wool court robe"
    material: wool
    wearer_rank: household-servant
    era: "Loom Age"
    badge_office: "third-rank minister"
    claimed_status: lawful
  - id: c_nightgown_violation
    garment: "silk nightgown"
    material: silk
    wearer_rank: merchant
    rite: "guild assembly"
    era: "Loom Age"
    claimed_status: violation
  - id: c_undeclared_status
    garment: "silk scarf"
    material: silk
    wearer_rank: merchant
    rite: "guild assembly"
    era: "Loom Age"
  - id: c_jubilee_silk
    garment: "silk jubilee mantle"
    material: silk
    wearer_rank: merchant
    rite: "Crown Jubilee"
    era: "Loom Age"
    claimed_status: lawful
  - id: c_veil_rite_unknown
    garment: "silk veil"
    material: silk
    wearer_rank: merchant
    era: "Loom Age"
    claimed_status: lawful
'''

EXPECTED = [
    "G-ERA",
    "MAT-01",
    "MAT-02",
    "MAT-03",
    "MAT-04",
    "MAT-05",
    "MAT-06",
    "MAT-07",
    "EAR-01",
    "EAR-04",
    "E-01",
    "T-01",
    "T-02",
    "T-03",
    "R-01",
    "R-02",
    "R-03",
    "R-04",
    "R-05",
    "R-06",
    "R-07",
]

CLEAN_PACKET = {
    "name": "clean-control",
    "eras": ["Alpha", "Beta"],
    "era_dates": {"Alpha": [-100, 200], "Beta": [200, 900]},
    "materials": [
        {"material": "linen", "composition": "bast fibre",
         "routes": [{"kind": "local", "stage": "cloth", "eras": ["Alpha", "Beta"]}]},
    ],
    "costumes": [
        {"id": "c1", "garment": "linen wrap", "material": "linen",
         "wearer_rank": "priestess", "rite": "rite of reeds", "era": "Alpha",
         "provenance": "local-production", "claimed_status": "lawful"},
    ],
}


def _finding_ids(lines):
    ids = []
    for line in lines:
        match = re.match(r"^FINDING ([A-Z0-9-]+):", line)
        if match:
            ids.append(match.group(1))
    return ids


def selftest():
    os.makedirs(FIXTURE_DIR, exist_ok=True)
    with open(FIXTURE_PATH, "w", encoding="utf-8") as handle:
        handle.write(FIXTURE)
    with open(EXPECTED_PATH, "w", encoding="utf-8") as handle:
        handle.write("\n".join(EXPECTED) + "\n")

    checks = 0

    # 1. parser sanity on the fixture bytes
    packet = parse_packet(FIXTURE)
    assert packet["eras"] == ["Reed Age", "Loom Age", "Steam Age"], packet["eras"]
    assert len(packet["costumes"]) == 20, len(packet["costumes"])
    assert packet["costumes"][3]["material"] == "cotton", packet["costumes"][3]
    assert packet["rank_rules"][0]["wearer_ranks"] == ["merchant"], packet["rank_rules"][0]
    assert packet["supply"][0]["demand"]["issues"] == 2, packet["supply"][0]
    checks += 1

    # 2. fixture from disk: exit 1 and every planted ID present
    code, lines = run_file(FIXTURE_PATH)
    assert code == 1, "fixture must produce findings: %s" % lines
    got = _finding_ids(lines)
    expected = [line.strip() for line in open(EXPECTED_PATH, encoding="utf-8")
                if line.strip()]
    missing = [fid for fid in expected if fid not in got]
    assert not missing, "planted finding IDs missing: %s (all output: %s)" % (missing, got)
    unexpected = sorted(set(got) - set(expected))
    assert not unexpected, "unexpected finding IDs on the fixture: %s" % unexpected
    severities = {}
    for line in lines:
        match = re.match(r"^FINDING ([A-Z0-9-]+): \[([a-z]+)\]", line)
        if match:
            severities.setdefault(match.group(1), set()).add(match.group(2))
    for fid, severity in (("E-01", "reject"),        # mauveine before 1856 [S]
                          ("T-01", "reject"),        # 1.4 m seamless panel, 0.6 m loom
                          ("MAT-05", "reject"),      # demand 800 > supply 750
                          ("MAT-02", "reject"),      # explicit exclusion
                          ("MAT-03", "reject"),      # imported garment, local claim
                          ("R-01", "note"),          # declared violation kept visible
                          ("R-02", "reject")):       # lawful claim vs applicable ban
        assert severity in severities.get(fid, set()), (fid, severity, severities)
    checks += 1

    # 3. the .expected file must list every planted ID once, in ID order
    assert expected == EXPECTED, expected
    assert all("%s:" % fid in "\n".join(lines) for fid in expected), lines
    checks += 1

    # 4. clean control packet: no findings, exit 0
    findings, code = evaluate(CLEAN_PACKET)
    assert code == 0 and not findings, (code, findings)
    checks += 1

    # 5. malformed inputs: exit 2 with a G-DATA line
    for text in ("just a sentence\n", "name: x\ncostumes: [", "costumes: []\n"):
        code, lines = run_text(text)
        assert code == 2 and lines and lines[0].startswith("FINDING G-DATA:"), (code, lines)
        checks += 1

    # 5b. the same packet as JSON is accepted, with the same clean verdict
    code, lines = run_text(json.dumps(CLEAN_PACKET))
    assert code == 0 and not lines, (code, lines)
    checks += 1

    # 6. spec worked examples fire as designed (mauveine 1840, panel 1.4 vs 0.6)
    mini = {
        "name": "worked-example-control",
        "eras": ["Staging Era"],
        "era_dates": {"Staging Era": [1500, 1840]},
        "costumes": [{"id": "gown", "garment": "court gown", "material": "wool",
                      "wearer_rank": "noble", "era": "Staging Era",
                      "processes": ["mauveine"]}],
    }
    code, lines = run_text(_dump(mini))
    assert code == 1 and any(line.startswith("FINDING E-01: [reject]") for line in lines), lines
    checks += 1

    # 7. false-positive guard: a mauve HUE alone never triggers the dyestuff anchor
    hue_only = dict(mini)
    hue_only["costumes"] = [{"id": "gown", "garment": "court gown", "material": "wool",
                             "wearer_rank": "noble", "era": "Staging Era",
                             "dye": "mauve"}]
    code, lines = run_text(_dump(hue_only))
    assert "E-01" not in _finding_ids(lines), lines
    checks += 1

    print("self-test: %d/%d checks passed; fixture exit 1 with %d planted finding IDs"
          % (checks, checks, len(expected)))
    print("fixture:  %s" % FIXTURE_PATH)
    print("expected: %s" % EXPECTED_PATH)
    return 0


def _dump(packet):
    """Tiny YAML writer for the selftest controls (mapping/list/scalars only)."""
    def emit(value, indent):
        pad = " " * indent
        if isinstance(value, dict):
            out = []
            for k, v in value.items():
                if isinstance(v, (dict, list)):
                    out.append("%s%s:" % (pad, k))
                    out.append(emit(v, indent + 2))
                else:
                    out.append("%s%s: %s" % (pad, k, v))
            return "\n".join(out)
        if isinstance(value, list):
            out = []
            for item in value:
                if isinstance(item, dict):
                    lines = emit(item, indent + 2).split("\n")
                    out.append("%s- %s" % (pad, lines[0].strip()))
                    out.extend(lines[1:])
                else:
                    out.append("%s- %s" % (pad, item))
            return "\n".join(out)
        return "%s%s" % (pad, value)
    return emit(packet, 0) + "\n"


def main(argv):
    args = argv[1:]
    if args in (["--selftest"], ["--self-test"]):
        return selftest()
    if args == ["--help"] or args == ["-h"]:
        print(USAGE)
        return EXIT_CLEAN
    if len(args) != 1:
        print(USAGE, file=sys.stderr)
        return EXIT_CNE
    code, lines = run_file(args[0])
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))