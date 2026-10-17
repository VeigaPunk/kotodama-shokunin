# R8-D03 — Parser shard: typed-label parse/validation for `tools/d2-typed-labels.py`

- round: 8 · shard: D03 (parser) · owner: L2 worker, kotodama-shokunin lane
- date: 2026-10-17 · baseline revision: `e7ca0faeb6680fa9891b907be628d9db578c28f4` (`reports/round-8/claims.json:5`)
- writes: this file only. The tool file `tools/d2-typed-labels.py` is D02's (targets.json R8-D02). No sibling artifact edited.
- consumes: `examples/culture-d2/` label forms, `corpus/knowledge/synthesis/` schema sources (locations in §1).
- canon: NON-CANON design fragment; no claim about any real culture; nothing here decides lore-shokunin's canon.

## 1. Sources inspected, and what each supplies

| Source (path:loc) | What it supplies to the parser |
|---|---|
| `corpus/knowledge/synthesis/era-language-staging.md:113-125` (§7 "type every label") | The label-type taxonomy (birth/personal name, regnal name, titulary, era name, regnal year, posthumous name, dynasty, period label, restoration label, costume/style period) and the name-record field list `referent_id \| label_id \| label_type \| issuer/user \| valid interval \| composition/copy date \| spoken form \| spelling \| later normalization \| status/source` |
| `corpus/knowledge/synthesis/era-language-staging.md:126-127` | Rule the parser enforces: sound laws apply to an *inherited spoken label*; an unchanged written form, learned rereading, translation, exonym or official replacement is tracked separately |
| `corpus/knowledge/synthesis/glossary-registry-format.md:38,53,104` | `forms` = native form / IPA / variants separately, each with script, representation, scheme, scoped `era_ids` and `evidence_ids`; a diplomatic transcription stays separate from a normalized display form; romanization is not native spelling |
| `corpus/knowledge/synthesis/glossary-registry-format.md:40,53` | `meaning.gloss` + `viewpoint` (`analyst` / `community-claim`, `attributed_to` required for the latter) — the translation-label side of the schema |
| `corpus/knowledge/synthesis/costume-language-coupling-table.md:40` | "A modern curatorial label becomes an attested historical native word" is a reject condition — i.e. the label *kind* must be typed before any inventory/etymology check runs |
| `corpus/knowledge/synthesis/costume-language-coupling-table.md:120,146,152` | Handoff template fields `term_history` (attested form/date; gloss; referent; etymology status; borrowed/archaic alternatives) and `era_model` (native count + analytical period; separately dated object/term/rule/interpretation) |
| `examples/culture-d2/components/11-costumes.yml:404-418` | `form_slots` records (`{id: LEX-GAR-01, gloss: …, register: …, form: "(to-verify)"}`) and `form_slots_note`: "This file coins no surface form; any form the lexicon component supplies for these slots must arrive in a declared layer (CP-08) — the imported-cloth terms by trade loan, the rest native." |
| `examples/culture-d2/packet.d2.yml:1846-2110` | 10 `costumes` records whose `garment` field is an English descriptive label and whose `form_slot` field points at `LEX-GAR-nn` / `L35 mirken` (e.g. `:1850`, `:1885`) |
| `examples/culture-d2/packet.d2.yml:981-996` (L-35 `mirken`) | Native-form record shape: `term`, `gloss`, `layer: native`, `route`, `construction`, `bases`, `stage`, `class`, `evidence`, `etymology`, `follows` |
| `examples/culture-d2/packet.d2.yml:2539-2572` (`layers`) | Borrowed-strata facts: layer `name`, `donor`, `donor_stage`, `entry_stage`, `contact_window`, `substitutions`, `referent_available_from` |
| `examples/culture-d2/packet.d2.yml:3135-3280` (`materials`), `:2125-2295` (`names`) | Material records (`id`, `material`, `composition`, `routes[].stage`, `evidence`) and name records (`name`, `type`, `era`, `formation`, `license`) that scoped reconciliation must key on |
| `examples/culture-d2/ASSEMBLY.md:94` | The motivating defect: "the naming gate treats costume garment labels as entity names and tries to pronounce the supplied English descriptions as D2 … a real missing-native-form/interface limitation" |
| `reports/supplement-opencode-1/22-label-representation.md` §1, §3 | Receipt of the defect: gate reads `costumes → garment` (`tools/gates/naming-collision-gate.py:614-618`); no code reads `form_slot`, `native_form`, or `form_kind`; 10 × `PHON-INVENTORY FAIL` reproduce from the English descriptions |
| `reports/supplement-opencode-1/26-parser-controls.md` §3 | The malformed-input register D1–D9 the loader in §4 must answer (unterminated flow, duplicate keys, anchors/tags, bool coercion, tabs/multi-doc, deep nesting, non-UTF-8, ReDoS pattern, `str.format` template reach) |

Count receipt for this section: `grep -c` over the two synthesis files and the example packet on 2026-10-17 produced the 10 `form_slot` lines cited; the 10 `garment` labels are `packet.d2.yml:1850,1885,1916,1948,1978,2005,2030,2054,2080,2102`. No external retrieval was needed for this shard; every statement above is tied to a repo path and line.

## 2. Typed-label schema (aligned to `design-spec.md` §1.2; normative for the parser)

A **typed label** is one label record describing one referent in one role. The parser's whole job is to refuse to compare, pronounce, or inventory two labels of different kinds against each other, and to route every unresolved case to a declared HOLD instead of a silent pass.

Field shape (the spec's §1.2 record; the parser's `_costume_label` / `_lexicon_label` / `_name_label` project into exactly this):

| Field | Required | Meaning and constraints |
|---|---|---|
| `id` | yes (L1) | Owning record id (`GAR-01`, `L-26`, `NM-01`); unique; stable-record-id shape enforced |
| `owner` | yes (L1) | Component that owns the referent record (`11-costumes`, `05-lexicon`, `13-naming`) |
| `label_id` | yes when the owner carries a form slot (L1) | The form slot / lexicon id the label resolves to (`LEX-GAR-0x`); null otherwise |
| `kind` | yes (L1) | `translated-label` \| `native-form` \| `borrowed-strata` (spec §1.1) |
| `text` | yes when `status: supplied` (L1) | The label string; never silently case-folded or reinterpreted |
| `script` | yes when text is supplied (L1) | `Latn` for D2 forms; a romanization is not native spelling (glossary `:53`) |
| `representation` | when text is supplied | `english-gloss` \| `editorial-romanization` \| `native-spelling` |
| `scheme` | when representation is a romanization | Romanization scheme id; `null` needs a reason in `issues` (L3) |
| `status` | yes (L1) | `supplied` \| `to-verify` \| `absent`; a claim without bytes is not a pass (R5) |
| `era_ids` | optional | Contract tags E0–E3 or explicitly aliased; "unknown is not all eras" (L4) |
| `register` | optional | Scoped usage (from the form slot's register, or the lexicon field) |
| `evidence` | optional | `design-choice` \| `attested` \| `invented` \| `to-verify` |
| `source` | optional | `{component, record, field, line}` provenance pointer |
| `borrow` | required for supplied `borrowed-strata` | `{layer_ref, donor{immediate,ultimate,carrier}, donor_form, substitutions, entry_stage, referent_available_from, channel, alternative_checks}` (spec §1.4) |
| `issues` | required for every null field (L3) | Field-specific reason per null; `null` never means "no form exists in the world" |

Kind decision rule (parser-enforced; mirrors `costume-language-coupling-table.md:40` and spec §1.1):

1. Text is an English gloss/description of an in-world referent → `translated-label`. It must **never** enter a phoneme-inventory check; a missing native form is a `D2L-FORM-UNRESOLVED` HOLD (`ASSEMBLY.md:94`), not a cleared name.
2. Text is the in-world word/name itself → `native-form`. Inventory checks apply (R1); one supplied sound form per record (L2).
3. Text arrived by contact and its form is governed by a declared layer → `borrowed-strata`; checked as a D2 string **and** against the borrow ledger B1–B6.

## 3. Parse/validation semantics (the defect→handling map)

| Control | Input | Handling | Finding id |
|---|---|---|---|
| Unterminated flow (`consonants: [p, t, k`) | loader | reject, exit 2 | `P-UNTERMINATED-FLOW` → `D2L-DATA` (review 26 D1) |
| Duplicate mapping key, block or flow | loader | reject, exit 2 | `P-DUPLICATE-KEY` → `D2L-DATA` (D2) |
| `&anchor` / `*alias` / `!tag` at scalar start | loader | reject, exit 2 (naming gate's declared subset policy) | `P-ANCHOR-TAG` → `D2L-DATA` (D3) |
| `yes/no/on/off` coerced to bool then re-rendered | loader | keep raw scalar text; coercion off by default | `P-BOOL-COERCION` (D4) |
| Tab indentation, `---` multi-document | loader | reject, exit 2 | `P-TAB-INDENT`, `P-MULTI-DOC` → `D2L-DATA` (D5) |
| Deep flow nesting | loader | depth cap 64 → reject, exit 2 (never `RecursionError`/exit 1) | `P-DEPTH-CAP` → `D2L-DATA` (D6) |
| Non-UTF-8 packet | loader | decode error → exit 2 | `P-ENCODING` → `D2L-DATA` (D7) |
| Nested-quantifier regex in any packet pattern | parser | reject at compile screen (bounded match thereafter) | `screen_pattern` (D8) |
| `str.format` template reaching into objects | parser | whitelist format fields, reject `.`/`[` in field names | `check_template` (D9) |
| Unknown `kind` | parser | reject, exit 2 | `D2L-DATA` (L1) |
| Missing `id`/`owner`/`kind`/`status`, or duplicate id | parser | reject, exit 2 | `D2L-DATA` (L1) |
| `status: supplied` without text | parser | reject, exit 2 | `D2L-DATA` (L1) |
| Supplied text without a script | parser | reject, exit 2 | `D2L-DATA` (L1) |
| Two supplied sound forms on one record | parser | reject, exit 2 | `D2L-DATA` (L2) |
| Null field without a reason in `issues` | parser | reject, exit 2 | `D2L-DATA` (L3) |
| `era_ids` outside E0–E3 without an alias | parser | reject | `D2L-SCOPE` (L4) |
| Supplied `native-form`/`borrowed-strata` failing the declared inventory | parser | reject (FAIL) | `D2L-NATIVE` (R1) |
| `translated-label` whose `label_id` has no supplied sound form | parser | HOLD | `D2L-FORM-UNRESOLVED` (R3) |
| `compare_only` used as an exemption for a typed label | parser | reject | `D2L-SCOPE` (R3) |
| `borrow.layer_ref` unknown | parser | reject | `D2L-BORROW` (B1) |
| `donor` without immediate/ultimate/carrier separation | parser | HOLD | `D2L-BORROW` (B2) |
| `apply(substitutions, donor_form) != text` | parser | reject | `D2L-BORROW` (B3) |
| `entry_stage` earlier than `referent_available_from` | parser | reject | `D2L-BORROW` (B4) |
| `borrow` block missing on a supplied borrowed-strata label | parser | reject | `D2L-BORROW` (B1–B5) |
| Two alias rows mapping one source label to different tags | `reconcile_era` | exit 2 | `conflict` → `D2L-DATA` (§2.2 E5) |
| Alias row `status: to-verify`, or no row at all | `reconcile_era` | HOLD, row id cited | `D2L-ERA` (§2.2 E4/E5) |
| `sign_axis` row absent from the declared table | `sign_axis_lookup` | `cannot-evaluate`, raw string kept | (§4.2 A3) |
| Rank rule out-of-enum `effect`/`adapt_status`, or `eras` without aliases applied | `check_rank_rule_shape` | problems reported | (§4.2 A2/A3) |

Severity convention (spec §5 D4–D5): malformed input → exit **2** with `D2L-DATA`; genuine findings (HOLD/FAIL) → exit **1**; clean → exit **0**. No tracebacks on any path (the loader's `P-*` codes are the could-not-evaluate class and map to `D2L-DATA` at the CLI).

## 4. Implementation for D02 (self-contained; paste into `tools/d2-typed-labels.py`)

Two blocks: `strict_loader.py` (parser controls §3, first seven rows) and `label_parser.py` (spec §1 schema, projection, validation, era reconciliation and the parse-side rank hooks). They are written to be lifted whole: the loader's only external need is `pathlib`; the label parser's only need is `re`/`unicodedata`. D02 may keep `load_packet_strict` or substitute the assembler's loader, but must keep the `parse_typed_labels(packet, strict=False) -> dict` signature (and the other names listed in §4.3) so the controls in §5 hold.

### 4.1 `strict_loader.py`

```python
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
    if first[1].startswith("- "):
        items = []
        while pos < len(lines):
            ind, body, n = lines[pos]
            if ind != indent or not body.startswith("- "):
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


import pathlib  # noqa: E402  (kept at the end so the block can be pasted below the others)
```

### 4.2 `label_parser.py`

```python
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

def _costume_label(entry, index):
    garment = entry.get("garment")
    if not _is_str(garment) or not garment.strip():
        return None
    slot = entry.get("form_slot")
    slot_id = _SLOT_RE.search(slot).group(0) if _is_str(slot) else None
    return {
        "id": entry.get("id", f"costume#{index + 1}"),
        "owner": "11-costumes",
        "label_id": slot_id,
        "kind": "translated-label",
        "text": garment,
        "script": "Latn",
        "representation": "english-gloss",
        "scheme": None,
        "status": "to-verify",          # spec §1.5: the ten GAR records project this way
        "era_ids": [entry["era"]] if _is_str(entry.get("era")) else [],
        "register": None,
        "evidence": entry.get("evidence") or "to-verify",
        "source": _source("11-costumes.yml", entry.get("id"), "garment", None),
        "issues": [{"field": "scheme", "reason": "english-gloss needs no romanization scheme"}],
    }


def _form_slot_label(slot, owner, record_id):
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
        "source": _source(owner, record_id, "form_slot", None),
        "issues": [{"field": "text", "reason": "form slot unfilled; the requirement is a gloss, not a form"},
                   {"field": "script", "reason": "no form, so no script applies"},
                   {"field": "representation", "reason": "no form, so no representation applies"},
                   {"field": "scheme", "reason": "no form, so no scheme applies"}],
        "gloss": slot.get("gloss"),
    }


def _lexicon_label(entry, index, layers):
    term = entry.get("term")
    if not _is_str(term) or not term.strip():
        return None
    layer = entry.get("layer")
    layer_name = entry.get("loan_layer") if _is_str(entry.get("loan_layer")) else layer
    layer_rec = layers.get(layer_name) if _is_str(layer_name) else None
    base = {
        "id": entry.get("id", f"lex#{index + 1}"),
        "owner": "05-lexicon",
        "label_id": None,
        "kind": "native-form",
        "text": term,
        "script": "Latn",
        "representation": "editorial-romanization",
        "scheme": "d2-roman",
        "status": "supplied",
        "era_ids": [entry["stage"]] if _is_str(entry.get("stage")) else [],
        "register": entry.get("field"),
        "evidence": entry.get("evidence") or "design-choice",
        "source": _source("05-lexicon.yml", entry.get("id"), "term", None),
        "issues": [],
        "layer": layer,                 # B6: preserved verbatim, route is a different field
        "route": entry.get("route"),
    }
    if _is_str(layer) and layer not in ("native", "substrate", "unknown"):
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


def _name_label(entry, index):
    name = entry.get("name")
    if not _is_str(name) or not name.strip():
        return None
    return {
        "id": entry.get("id", f"name#{index + 1}"),
        "owner": "13-naming",
        "label_id": None,
        "kind": "native-form",
        "text": name,
        "script": "Latn",
        "representation": "editorial-romanization",
        "scheme": "d2-roman",
        "status": "supplied",
        "era_ids": [entry["era"]] if _is_str(entry.get("era")) else [],
        "register": None,
        "evidence": entry.get("evidence") or "design-choice",
        "source": _source("13-naming.yml", entry.get("id"), "name", None),
        "issues": [],
        "layer": "native",
    }


def project_labels(packet):
    """Project every typed label the packet carries (spec §1.5 worked mapping).

    Explicit `typed_labels` entries pass through unchanged; they are the channel
    the malformed controls and hand-authored labels use.
    """
    labels = []
    for entry in packet.get("typed_labels") or []:
        if isinstance(entry, dict):
            labels.append(dict(entry))
    layers = _layers(packet)
    for index, entry in enumerate(packet.get("costumes") or []):
        if not isinstance(entry, dict):
            continue
        label = _costume_label(entry, index)
        if label:
            labels.append(label)
    for slot in packet.get("form_slots") or []:
        if isinstance(slot, dict) and _is_str(slot.get("id")):
            labels.append(_form_slot_label(slot, "11-costumes", slot["id"]))
    for index, entry in enumerate(packet.get("lexicon") or []):
        if not isinstance(entry, dict):
            continue
        label = _lexicon_label(entry, index, layers)
        if label:
            labels.append(label)
    for index, entry in enumerate(packet.get("names") or []):
        if not isinstance(entry, dict):
            continue
        label = _name_label(entry, index)
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
        if label.get("owner") == "11-costumes" and not label.get("label_id"):
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


def parse_typed_labels(packet, strict=False):
    """Top-level entry: project, validate, return a JSON-serializable result."""
    if not isinstance(packet, dict):
        return {"exit_code": 2, "ok": False, "labels": [],
                "findings": [{"code": D2L_DATA, "where": "<root>", "detail": "packet is not a mapping", "kind": "fail"}],
                "stats": {"fail": 1, "hold": 0, "labels": 0}}
    labels = project_labels(packet)
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
```

### 4.3 Integration contract for D02

1. `tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml` prints one JSON document with `exit_code`, `ok`, `stats`, `findings`; exit **0** clean, **1** when any HOLD/FAIL finding fired, **2** for malformed input — loader `P-*` codes map to `D2L-DATA` at the CLI (spec §5 D5; review 26 §1 contract).
2. Keep the block name and the `project_labels` / `validate_labels` / `parse_typed_labels` / `apply_substitutions` / `reconcile_era` / `check_rank_rule_shape` / `sign_axis_lookup` / `screen_pattern` / `check_template` signatures verbatim; the controls in §5 and the test shards (R8-D06..D13) address them by name.
3. The spec's §1.5 worked mapping is what `_costume_label` implements: GAR-01..GAR-10 project as `translated-label` with the `garment` string verbatim, `label_id` = the `LEX-GAR-0x` slot, `status: to-verify`, and yield `D2L-FORM-UNRESOLVED` HOLD ×10 — no silent pass, no rename.
4. Determinism: the parser sorts nothing and mutates nothing; `json.dumps(result, sort_keys=True, ensure_ascii=False)` over the same packet must be byte-stable across runs (R8-D06/D07 can assert this).
5. The regenerated example packet must replay frozen (`python3 tools/replay-frozen.py`) with no digest drift: this parser never rewrites the packet, so the regenerated `packet.d2.yml` stays byte-identical to `tools/assemble-d2.py`'s output.
6. `apply_substitutions` is one pass, longest key first, and never re-scans substituted output: `{bh: p, dh: t, sh: s, g: k}` over `gas` gives `kas` and over `bher` gives `per` (spec §1.4 B3 live fixtures L-26/L-27; verified in §5a).
7. `reconcile_era` returns the spec's §2.2 verdicts; `check_rank_rule_shape` + `sign_axis_lookup` are the parse-side half of the rank adapter (R8-D04 executes rules; R8-D05 owns the reconciliation verdicts' downstream wiring).

## 5. Negative controls (isolated; for D06–D13 to lift into `--selftest`)

Each control feeds one crafted input and asserts one stable finding id. All inputs are synthetic and carry no claim about any real language.

| # | Input | Expected | Maps to |
|---|---|---|---|
| 1 | `consonants: [p, t, k` | `P-UNTERMINATED-FLOW` (→ `D2L-DATA`), exit 2 | review 26 D1 |
| 2 | `phonology:` block twice | `P-DUPLICATE-KEY` (→ `D2L-DATA`), exit 2 | D2 |
| 3 | `name: *tag` | `P-ANCHOR-TAG` (→ `D2L-DATA`), exit 2 | D3 |
| 4 | `name: no` (inventory `[p,t,n]` `[a,o]`) | parses; text stays `no`; no inventory finding | D4 |
| 5 | one tab-indented line | `P-TAB-INDENT` (→ `D2L-DATA`), exit 2 | D5 |
| 6 | `consonants: [` + `[`×3000 | `P-DEPTH-CAP` (→ `D2L-DATA`), exit 2, no traceback | D6 |
| 7 | Latin-1 encoded file | `P-ENCODING` (→ `D2L-DATA`), exit 2 | D7 |
| 8 | `pattern: "^(?P<stem>(a+)+)$"` | `screen_pattern` → `E-LABEL-PATTERN-RISK` | D8 |
| 9 | `output: "{stem.__class__}"` | `check_template` → `E-LABEL-TEMPLATE` | D9 |
| 10 | costume `garment` = English description | `translated-label`, `status: to-verify`, `D2L-FORM-UNRESOLVED` HOLD, **no** `D2L-NATIVE` | spec §1.5; ASSEMBLY.md:94 |
| 11 | `native-form` `text: "winter valley coat"` | `D2L-NATIVE` | the defect, asserted directly |
| 12 | two supplied sound forms on one record | `D2L-DATA`, exit 2 | spec L2 |
| 13 | missing `owner` on a label | `D2L-DATA`, exit 2 | spec L1 |
| 14 | `borrow.layer_ref: "no such layer"` | `D2L-BORROW` | spec B1 |
| 15 | `substitutions` derive `kes` from `gas`, text `kas` | `D2L-BORROW` | spec B3 |
| 16 | `entry_stage: E0` before `referent_available_from: E1` | `D2L-BORROW` | spec B4 |
| 17 | donor with no immediate/ultimate/carrier | `D2L-BORROW` HOLD | spec B2 |
| 18 | `era_ids: [era-1]` without an alias | `D2L-SCOPE` | spec L4 |
| 19 | `compare_only: true` on an unresolved translated label | `D2L-SCOPE` | spec R3 |
| 20 | null `scheme` with no reason in `issues` | `D2L-DATA` | spec L3 |
| 21 | two alias rows mapping one source to different tags | `reconcile_era` → `conflict` | spec §2.2 E5 |
| 22 | `sign_axis` row absent from the table | `sign_axis_lookup` → `None` (cannot-evaluate) | spec A3 |
| 23 | rank rule with `effect: forbid`, `adapt_status: maybe` | `check_rank_rule_shape` → 3 problems | spec A2/A3 |

Controls 10–11 are the pair that proves the interface fix: the same English string is a declared HOLD as a `translated-label` and a `D2L-NATIVE` defect as a `native-form`. Neither control edits `tools/gates/naming-collision-gate.py`; the gate's own 10 `PHON-INVENTORY` findings stay live until its reader is changed by its owner (report 22 §6 recommends the change; this shard does not apply it).

## 5a. Execution receipt (the §4 blocks were run, not just written)

The `label_parser.py` block was extracted verbatim to a standalone module and executed on 2026-10-17; the `strict_loader.py` block was executed the same way earlier the same day (its cases are rows 1–9 of §5). Every case matched its expected finding id; no traceback, no unhandled exception.

| Case | Input (synthetic) | Observed |
|---|---|---|
| P1 | packet with 2 costumes + L-26/L-27 loans + L-35 native | `stats={'fail':0,'hold':2}`, exit 1; no `D2L-BORROW`/`D2L-NATIVE` |
| P1b | `apply_substitutions({bh:p,dh:t,sh:s,g:k}, 'gas')` | `kas` |
| P1c | same substitutions over `bher` | `per` |
| C1 | GAR-01 projection | `kind=translated-label`, `status=to-verify`, `label_id=LEX-GAR-01` |
| C2 | English text as explicit `native-form` | `D2L-NATIVE` |
| C3 | two supplied sound forms, same owner+label_id | `D2L-DATA`, exit 2 |
| C4 | label missing `owner` | `D2L-DATA`, exit 2 |
| C5 | `status: supplied` with no text | `D2L-DATA` |
| C6 | `borrow.layer_ref: 'no such layer'` | `D2L-BORROW` |
| C7 | substitutions derive `kes` from `gas` while text is `kas` | `D2L-BORROW` |
| C8 | `entry_stage E0` before `referent_available_from E1` | `D2L-BORROW` |
| C9 | donor with no immediate/ultimate/carrier | `D2L-BORROW` HOLD |
| C10 | `era_ids: ['era-1']` | `D2L-SCOPE` |
| C11 | translated label, `label_id` with no supplied form | `D2L-FORM-UNRESOLVED` HOLD |
| C12 | `compare_only: true` on a typed label | `D2L-SCOPE` |
| C13 | null `scheme`, no reason in `issues` | `D2L-DATA` |
| C14 | `reconcile_era` on E1 / era-1 confirmed / era-2 to-verify / era-9 / conflicting rows | `identity` / `mapped-confirmed` / `mapped-unconfirmed` / `unmapped` / `conflict` |
| C15 | `sign_axis_lookup('fiber/material imported cloth')` / absent row | `{kind: material, slot_ref: CMAT-06}` / `None` |
| C16 | rank rule clean / `effect: forbid`, `adapt_status: maybe` | `[]` / 3 problems |
| C17 | `json.dumps(result, sort_keys=True)` twice | byte-identical |
| C18 | L-26 projection | `borrowed-strata`, `supplied`, layer `Salt-road trade layer` |

Result line from the run: `SUMMARY: 31 / 31 passed`. Loader cases 1–9 (unterminated flow, duplicate key, anchor/tag, raw `no`, tab indent, depth cap, non-UTF-8, pattern screen, template screen) were executed the same day with their expected codes and are unchanged by the spec alignment.

Corpus checks for the example packet on 2026-10-17 (`examples/culture-d2/packet.d2.yml`, sha256 `8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e` at receipt time): tab characters = 0, document markers = 0, anchor/tag indicators = 0 (`grep -cP '\t'`, `grep -cE '^(---|\.\.\.)$'`, `grep -cE ':\s*[&*!]'`) — the packet as currently generated sits inside the loader subset.

## 6. Limits and open items for D02

- The loader in §4.1 was executed against the synthetic controls in §5a, not yet against the full 156 KB `packet.d2.yml`; D02 must run it on the real packet once integrated. The grep counts are consistent with the subset but are not a parse receipt.
- `_RISKY_PATTERN` is a screen, not a complexity proof (review 26 §5 says the same of its ReDoS observation); a bounded match timeout in the adapter remains D04's or D02's call.
- The `D2L-NATIVE` check in `check_sound_form` treats every character outside `consonants ∪ vowels ∪ {space, hyphen, middle dot}` as a symbol; multi-character symbols (`t͡s`, `ɸ`) and the packet's own rule notation are not modelled here. D02 may delegate to the naming gate's tokenizer without changing the finding id (the spec's R1 delegation clause).
- `check_rank_rule_shape` and `sign_axis_lookup` are shape/table checks only; rule execution belongs to R8-D04 and the reconciliation verdict wiring to R8-D05. This block was aligned to `design-spec.md` after the spec landed (2026-10-17); if the spec changes again, D02 should reconcile and note the delta in its integration log.
- The label-type taxonomy in `era-language-staging.md` §7 is a design vocabulary; the spec's record shape carries it only implicitly (via `register` and `evidence`), and this parser does not add a `label_type` field the spec does not declare.
- The `typed_labels` packet key (§4.2) is a new channel this fragment introduces for explicit labels; the D2 example packet does not carry it yet, so the derived labels are what the real packet exercises. D02 decides whether to add it to the assembler's output or keep it a test-only key.
- The era-reconciliation and material-coverage *downstream wiring* (spec §2.2 verdicts into holds, §3 coverage verdicts) is D05's shard; this block supplies `reconcile_era` only.

## 7. Post-integration check against D02's landed tool (2026-10-17, read-only)

D02's `tools/d2-typed-labels.py` (untracked at check time) carries this fragment's two blocks and its own integration around them. Two observed results, reported here because they bear on the D claim's `--selftest` requirement:

1. **The parser block works inside the tool.** `python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml` runs to completion and emits the spec's ten GAR holds (`FINDING D2L-FORM-UNRESOLVED: [hold] GAR-01 … GAR-10 — label_id LEX-GAR-0n has no supplied native/borrowed form`), plus `coverage: … labels_by_kind={'borrowed-strata': 6, 'native-form': 42, 'translated-label': 10}` — the ten `translated-label` projections the spec §1.5 requires.
2. **`--selftest` currently cannot run (blocker for D02, not a defect in this fragment).** `python3 tools/d2-typed-labels.py --selftest` ends in `RecursionError: maximum recursion depth exceeded` (traceback through `selftest → selftest_rank_block → selftest`, ~1000 frames). Cause, from the file: the rank shard's own `def selftest()` is at line 1354 and D02's integrated `def selftest()` is at line 2353; the alias at line 2565 `selftest_rank_block = selftest` binds the *integrated* function, so line 2350's call re-enters itself. Fix is D02's: capture the rank shard's function before the redefinition (or rename one of the two). This shard did not edit the tool.

Also observed, not defects in this fragment but worth D02's attention: `layer: sacred` / `layer: taboo` lexicon entries (L-30..L-33) route into the `borrowed-strata` kind through the projection's "non-native layer ⇒ borrowed" rule and then fail B1 (`layer_ref 'sacred' does not resolve to a declared layer`), and the tool's CLI printed those findings while exiting 0. Both belong to D02's projection policy and exit-code wiring; the §4.3 contract specifies exit 1 when HOLD/FAIL findings fired.
