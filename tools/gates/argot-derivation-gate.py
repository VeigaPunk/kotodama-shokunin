#!/usr/bin/env python3
r"""argot-derivation-gate.py — register-scoped derivation replay.

Spec:  `SKILL.md` "Derivation replay — replay the family's own build, by text
       transform" (machine-readable pattern/output pairs; the replay names every
       input) and `reports/round-17/d4/design-brief.md` Δ3 + control C-02
       ("a fixture whose quote form != apply(op, base) -> FAIL, id
       D4L-ARGOT-DERIV"). Algorithms: `reports/round-17/d4/design-language.md`
       §5 (the two argot operations, with the 11 worked derivations) and §7.1.

Interface
---------
    python3 tools/gates/argot-derivation-gate.py <culture-packet.yml>
    python3 tools/gates/argot-derivation-gate.py --selftest
    (`--self-test` is accepted as an alias, matching the sibling gates.)

Flagless and single-input, so `tools/replay-frozen.py` can pin a row
(`[python3, <gate>, <input>]`). Read-only: no network, no writes at run time,
and `--selftest` reads the two committed fixture files beside this script.

Output:  one finding per line, `FINDING <id>: <LEVEL> — <message>`, LEVEL in
         FAIL / HOLD, then one `coverage:` line and one `dependency:` line.

Exit codes (only these three):
    0   clean — no findings printed
    1   one or more findings printed
    2   could-not-evaluate — the input is unreadable, not UTF-8, or outside the
        declared YAML subset; a single `FINDING D4L-ARGOT-DATA` line is printed

What it checks
--------------
A *register-scoped form* is a packet record that declares a `register`, or whose
`loan_layer`/`layer` resolves to a declared layer that carries a `register`, or
that declares the forecast `derived_from`/`derivation` pair. For every such
record the gate replays the record's own stated inputs and compares the replayed
text with the delivered form — three sources of rule, tried in order:

1. the two declared argot operations (`head2`, `reverse`), whose algorithms are
   fixed by `design-language.md` §5 and embedded here as an explicit table;
2. a packet `morphology.derivation_rules` entry whose `id` is the declared rule,
   replayed through its machine-readable `pattern`/`output` pair;
3. for a borrowed register-scoped record, its layer's `substitutions` map applied
   to its own `donor_form` (longest donor key first).

Finding ids
-----------
    D4L-ARGOT-DATA    input could not be evaluated                      [exit 2]
    D4L-ARGOT-DERIV   the stated inputs and rules do not yield the form [FAIL]
    D4L-ARGOT-RULE    the declared derivation is not replayable         [HOLD]
    D4L-ARGOT-COVERAGE  the argot relation is declared, not delivered   [HOLD]

Calibration (craft policy, declaring what this implementation does)
-------------------------------------------------------------------
- The two operations and their algorithms are the round-17 design's, adopted
  unchanged and cited. The maximal-onset reading of `head2` is load-bearing
  because it is the one row where the maximal-coda reading disagrees
  (`saalumi` -> `saalu`, never `saalum`; `design-language.md` §5). The design's
  rule is *legality-constrained* maximal onset, and the constraint is the whole
  substance of it: round 26 measured that the delivered `syllabify` moved every
  consonant run forward without checking the resulting syllable, so it read
  `tikmes` as `ti.kme.s` and `ker` as `ke.r` — clusters and a dangling coda the
  declared phonotactics (`(C)V(V)(C)`, `onset_clusters: false`) refuse. Round 27
  makes the onset assignment legality-aware (`is_legal_syllable`), so the gate
  implements the algorithm its own docstring cites. The change is scoped to
  `head2`: no delivered `derived_from`/`derivation` record in any family names
  `head2` (the D4 register stratum uses `reverse` and `lengthen`), so the
  replayed verdicts over delivered packets are unchanged.
- This gate is a **capability plus a replay**, not a clearance: exit 0 means
  "every register-scoped form that states its inputs re-derives", not that the
  stratum is complete or that any hold elsewhere is closed.
- Scope limits, declared rather than silently skipped:
  * only the `head2`/`reverse` operations are built in; a family declaring a
    third argot operation must declare it as a `morphology.derivation_rules`
    entry, or the record reads `D4L-ARGOT-RULE`;
  * "the packet declares the argot relation" is read from
    `morphology.derivation_rules` (rule id/name/note text) and from an explicit
    `derivation_ops` list; a family that declares its operations only in prose
    will not trigger the coverage hold;
  * the borrow-adaptation leg overlaps `tools/gates/lexicon-coverage-audit.py`'s
    `L-adaptation-mismatch` by design: that gate audits the whole lexicon, this
    one is scoped to register-scoped records and speaks the `D4L-ARGOT-*`
    vocabulary the round-17 design names.
- The naming gate's YAML subset loader and its budgeted pattern replay are
  loaded read-only by path from `tools/gates/naming-collision-gate.py`; this gate
  adds no semantics to them and the dependency is named on stdout with its live
  digest, so a reader can tell which bytes the replay used.

Non-canon: findings are review evidence, never canon rulings (PROVINCE.md).
"""

import hashlib
import re
import runpy
import sys
import unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
NAMING = HERE / "naming-collision-gate.py"
FIXTURE_PATH = HERE / "fixtures" / "argot-derivation-gate.yml"
EXPECTED_PATH = HERE / "fixtures" / "argot-derivation-gate.expected"

EXIT_CLEAN = 0
EXIT_FINDINGS = 1
EXIT_UNEVALUATED = 2

FORM_FIELDS = ("term", "quote_form", "form", "candidate", "name")
# A *lexical form* record is one a language owns: it carries the lexicon's own
# `term` (or the forecast `quote_form`), or it declares the derived_from/
# derivation pair. A `symbols` record's `form:` is prose about a medium and a
# `contact` record's `name:` labels a road — neither is a form the
# sound-and-identity channel could check, so neither is graded here.
LEXICAL_FORM_FIELDS = ("term", "quote_form")
LEXICAL_MARKERS = ("derived_from", "derivation", "donor_form", "loan_layer", "route",
                   "formation")
NON_FORMS = ("", "null", "none", "~")
# `plain` is the unmarked register: a form scoped to it is the baseline the
# argot is measured against, not a member of the argot. Every other declared
# register (quote, trade, craft, ritual, taboo, sacred, …) is in scope.
UNMARKED_REGISTERS = ("plain", "neutral", "standard", "ordinary")


# --------------------------------------------------------------------------
# the two declared argot operations (design-language.md §5)
# --------------------------------------------------------------------------

VOWELS = frozenset("aeiou")
# The syllable template, quoted from the D4 design's own phonology
# (`examples/culture-d4/components/02-phonology.yml:82,92`: `(C)V(V)(C)` with
# `onset_clusters: false`). It is what "a legal syllable" in the maximal-onset
# rule below is measured against, so it is stated here rather than left implicit
# — the legality test is the whole difference between this implementation and a
# naive maximal-onset scan.
CODAS = frozenset("nmsklrtd")
ONSET_CLUSTERS = False

OPS = {
    "head2": {
        "kind": "syllable-prefix",
        "count": 2,
        "syllabification": "maximal-onset",
        "design": "reports/round-17/d4/design-language.md §5",
    },
    "reverse": {
        "kind": "string-reversal",
        "design": "reports/round-17/d4/design-language.md §5",
    },
}


def syllabify(word):
    """Maximal-onset syllabification of a D4-shaped word (design §5).

    The design's rule is: "a consonant is taken as the onset of the following
    syllable **whenever that yields a legal syllable**"
    (`reports/round-17/d4/design-language.md:191-196`). The legality clause is
    load bearing, not decoration: `onset_clusters: false` means a *single*
    consonant is the only legal onset, so a two-consonant run before a vowel
    splits coda|onset — `tikmes` is `tik.mes`, never `ti.kme.s`, and its `head2`
    is `tik`, never `tikme`. A naive maximal-onset scan that moves the whole run
    forward manufactures a cluster-bearing "syllable" the language cannot
    spell.

    So: a single intervocalic consonant is the onset of the following syllable
    (`saalumi` is `saa.lu.mi`, `head2` `saalu` — not `saalum`, which a
    maximal-coda reading would give); a run of two or more keeps all but its
    last consonant as the coda of the preceding syllable; a word-final run is
    the last syllable's coda (`ker` is one syllable, `ker`, not `ke.r`).
    """
    tokens, index = [], 0
    while index < len(word):
        char = word[index]
        if char in VOWELS:
            if index + 1 < len(word) and word[index + 1] == char:
                tokens.append(("V", char * 2))
                index += 2
            else:
                tokens.append(("V", char))
                index += 1
        else:
            tokens.append(("C", char))
            index += 1

    syllables, pending, position = [], "", 0
    while position < len(tokens):
        kind, text = tokens[position]
        if kind == "V":
            syllables.append(pending + text)
            pending = ""
            position += 1
            continue
        run = ""
        while position < len(tokens) and tokens[position][0] == "C":
            run += tokens[position][1]
            position += 1
        if position >= len(tokens):      # word-final run: a coda, never an onset
            if syllables:
                syllables[-1] += run
            else:
                syllables.append(run)
            continue
        onset = run[-1:]                 # onset_clusters: false — one consonant
        coda = run[:-1]
        if coda:
            if syllables:
                syllables[-1] += coda
            else:
                syllables.append(coda)
        pending = onset
    if pending:
        syllables.append(pending)
    return syllables


def is_legal_syllable(syllable):
    """Is one syllable of the template `(C)V(V)(C)` with a licensed coda?"""
    index, length = 0, len(syllable)
    if index < length and syllable[index] not in VOWELS:
        index += 1                       # a single onset consonant
    if index >= length or syllable[index] not in VOWELS:
        return False
    if index + 1 < length and syllable[index + 1] == syllable[index]:
        index += 2                       # a long vowel is one nucleus
    else:
        index += 1
    if index < length:
        if syllable[index] not in CODAS:
            return False
        index += 1
    return index == length


def op_head2(base):
    return "".join(syllabify(base)[:OPS["head2"]["count"]])


def op_reverse(base):
    return base[::-1]


OP_FUNCTIONS = {"head2": op_head2, "reverse": op_reverse}


def apply_op(op, base):
    return OP_FUNCTIONS[op](base)


# --------------------------------------------------------------------------
# dependencies, loaded read-only by path (never re-implemented, never written)
# --------------------------------------------------------------------------


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_naming():
    """The sibling naming gate's loader and replay kernel, read-only.

    Imported by path, exactly as `tools/gates/typed-pipeline-gate.py` loads its
    peers. The module is never written; its live digest is printed on every run
    so a replay names the bytes it actually used.
    """
    return runpy.run_path(str(NAMING))


def finding(fid, level, message):
    return {"id": fid, "level": level, "message": message}


def format_finding(item):
    return "FINDING %s: %s — %s" % (item["id"], item["level"], item["message"])


def text_of(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def has_text(value):
    return isinstance(value, str) and value.strip() != ""


def norm(text):
    return unicodedata.normalize("NFC", text)


# --------------------------------------------------------------------------
# packet reading
# --------------------------------------------------------------------------


def record_blocks(packet):
    """Every top-level list-of-mappings block, with its key."""
    blocks = []
    for key in sorted(packet):
        value = packet.get(key)
        if not isinstance(value, list):
            continue
        entries = [item for item in value if isinstance(item, dict)]
        if entries:
            blocks.append((key, entries))
    return blocks


def layer_index(packet):
    """Declared contact layers by name and by id, compact-keyed."""
    table = {}
    layers = packet.get("layers")
    if isinstance(layers, dict):
        layers = list(layers.values())
    if not isinstance(layers, list):
        return table
    for entry in layers:
        if not isinstance(entry, dict):
            continue
        for key in ("id", "name"):
            label = text_of(entry.get(key)).strip()
            if label:
                table[label.casefold()] = entry
    return table


def record_form(entry):
    for key in FORM_FIELDS:
        value = text_of(entry.get(key)).strip()
        if value and value.casefold() not in NON_FORMS:
            return value
    return ""


def is_form_record(entry):
    """True for a record that carries a language form, not prose about one.

    A `symbols` record's `form:` describes a medium and a `contact` record's
    `name:` labels a road; neither is a form the sound-and-identity channel
    could check. A lexical form record carries the lexicon's own `term`/`quote_form`,
    or declares the forecast `derived_from`/`derivation` pair, or carries a
    borrowing record (`donor_form` / `loan_layer`) — all three are language
    facts; a display string is not.
    """
    if any(has_text(entry.get(key)) for key in LEXICAL_FORM_FIELDS):
        return True
    if any(key in entry for key in LEXICAL_MARKERS):
        return True
    return declared_derivation(entry) is not None


def record_id(entry, block, position):
    label = text_of(entry.get("id")).strip()
    return label or "%s[%d]" % (block, position)


def record_register(entry, layers):
    """The register a record is scoped to, or None when it is not scoped.

    `plain` and its synonyms are the *unmarked* register — the baseline the
    argot is measured against — so they are reported as unscoped rather than
    silently treated as an argot register.
    """
    declared = text_of(entry.get("register")).strip()
    if declared and declared.casefold() not in NON_FORMS:
        if declared.casefold() not in UNMARKED_REGISTERS:
            return declared
        return None
    for key in ("loan_layer", "layer"):
        label = text_of(entry.get(key)).strip()
        if not label:
            continue
        layer = layers.get(label.casefold())
        if layer is None:
            continue
        layer_register = text_of(layer.get("register")).strip()
        if layer_register and layer_register.casefold() not in NON_FORMS:
            if layer_register.casefold() not in UNMARKED_REGISTERS:
                return layer_register
            return None
    return None


def declared_derivation(entry):
    """(op, base) from the forecast `derived_from` + `derivation` shape."""
    base = text_of(entry.get("derived_from")).strip()
    derivation = entry.get("derivation")
    op = ""
    if isinstance(derivation, dict):
        op = text_of(derivation.get("op") or derivation.get("rule")).strip()
        if not base:
            base = text_of(derivation.get("base")).strip()
    else:
        op = text_of(derivation).strip()
    formation = entry.get("formation")
    if isinstance(formation, dict):
        if not base:
            base = text_of(formation.get("derived_from")).strip()
        if not op:
            op = text_of(formation.get("rule") or formation.get("rule_id")).strip()
    if not base or not op or base.casefold() in NON_FORMS or op.casefold() in NON_FORMS:
        return None
    return op, base


def claimed_formation(entry):
    """(rule, stem) from the packet's own `formation` idiom.

    The D2/D4 shape is `formation: {stem: "su+nel", bases: [su, nel], rule:
    UP-COMPOUND}`: the stem is the stated input and the rule id is the stated
    chain. It is the same relation `derived_from`/`derivation` states, in the
    vocabulary the delivered packets actually use, so the leg must replay it —
    otherwise a packet that declares `derivation_rules` and then loses them
    reads clean.
    """
    formation = entry.get("formation")
    if not isinstance(formation, dict):
        return None
    stem = text_of(formation.get("stem")).strip()
    rule = text_of(formation.get("rule") or formation.get("rule_id")).strip()
    if not stem or not rule or stem.casefold() in NON_FORMS or rule.casefold() in NON_FORMS:
        return None
    return rule, stem


def packet_rules(packet):
    morphology = packet.get("morphology")
    if not isinstance(morphology, dict):
        return {}
    rules = morphology.get("derivation_rules")
    if not isinstance(rules, list):
        return {}
    table = {}
    for entry in rules:
        if not isinstance(entry, dict):
            continue
        rid = text_of(entry.get("id")).strip()
        if rid:
            table[rid] = entry
    return table


def packet_declares_ops(packet):
    """The argot operations the packet itself names, if any.

    Three declarations count, and they are read from the places a packet
    actually puts them: a top-level `derivation_ops` list, a `morphology.
    derivation_ops` list, and a `morphology.derivation_rules` entry whose
    id/name/kind/note text names the operation. A family that declares its
    argot operations only in prose elsewhere is not detected, and that limit
    is stated in the module docstring rather than guessed around.
    """
    named = set()
    morphology = packet.get("morphology")
    for source in (packet, morphology if isinstance(morphology, dict) else {}):
        declared = source.get("derivation_ops")
        if isinstance(declared, list):
            for item in declared:
                label = text_of(item).strip().casefold()
                if label in OP_FUNCTIONS:
                    named.add(label)
    for rule in packet_rules(packet).values():
        haystack = " ".join(
            text_of(rule.get(key)) for key in ("id", "name", "kind", "note", "description")
        ).casefold()
        for op in OP_FUNCTIONS:
            if op in haystack:
                named.add(op)
    return sorted(named)


# --------------------------------------------------------------------------
# the legs
# --------------------------------------------------------------------------


def replay_rule(rule, base, form, naming):
    """Replay a packet rule's pattern/output pair; (verdict, detail).

    verdict is True (replays to `form`), False (does not), or None (the pair is
    outside the replayable subset, so the record reads HOLD).
    """
    pattern = text_of(rule.get("pattern")).strip()
    output = text_of(rule.get("output")).strip()
    if not pattern or not output:
        return None, "rule %r lacks a machine-readable `pattern`/`output` pair" % (
            text_of(rule.get("id")).strip() or "?",)
    try:
        if naming["_catastrophic_pattern"](pattern):
            return None, "pattern nests a quantifier or alternation inside a quantified group"
        match = naming["_match_with_budget"](pattern, base)
    except naming["_MatchBudgetExceeded"] as exc:
        return None, "pattern is not usable: %s" % exc
    except re.error as exc:
        return None, "pattern is not usable: %s" % exc
    if match is None:
        return False, None
    problem = naming["_template_problem"](output, match.groupdict())
    if problem:
        return None, "output template is outside the accepted subset (%s)" % problem
    try:
        replayed = output.format(**match.groupdict())
    except (KeyError, IndexError) as exc:
        return None, "output template cannot be resolved (%s)" % exc
    return norm(replayed) == norm(form), None


def replay_borrow(entry, layers):
    """Apply the layer's substitutions to the record's own donor form."""
    layer_label = ""
    layer = None
    for key in ("loan_layer", "layer"):
        label = text_of(entry.get(key)).strip()
        if label and label.casefold() in layers:
            layer_label, layer = label, layers[label.casefold()]
            break
    if layer is None:
        return None, None, "the record names no declared layer"
    donor = text_of(entry.get("donor_form")).strip()
    substitutions = layer.get("substitutions")
    if not donor or not isinstance(substitutions, dict) or not substitutions:
        return None, layer_label, None
    pairs = sorted(
        ((text_of(k), text_of(v)) for k, v in substitutions.items() if text_of(k)),
        key=lambda pair: len(pair[0]),
        reverse=True,
    )
    expected = donor
    for donor_part, recipient_part in pairs:
        expected = expected.replace(donor_part, recipient_part)
    return norm(expected), layer_label, None


def evaluate_packet(packet, naming):
    """Findings and the coverage counters for one packet."""
    findings = []
    layers = layer_index(packet)
    rules = packet_rules(packet)
    counters = Counter()

    for block, entries in record_blocks(packet):
        for position, entry in enumerate(entries):
            counters["records"] += 1
            form = record_form(entry)
            if not form or not is_form_record(entry):
                continue
            eid = record_id(entry, block, position)
            derivation = declared_derivation(entry)
            register = record_register(entry, layers)
            claimed = claimed_formation(entry)
            if register is None and derivation is None and claimed is None:
                continue
            if register is not None or derivation is not None:
                counters["register_scoped"] += 1
            scoped = register or "unstated"

            if derivation is not None:
                op, base = derivation
                counters["derived_pairs"] += 1
                # F-6 (reports/round-17/d4/design-brief.md:306-307) needs the
                # derivation class counted on its own. The shared `violations`
                # total also counts claimed-chain (:626) and borrow (:652)
                # failures, so `derived_pairs - violations` is NOT the
                # derivation pass count. K01 section 8 owed this decision and
                # reports/round-38/depth/D01-f6-design.md measures it.
                if op in OP_FUNCTIONS:
                    replayed = apply_op(op, base)
                    if norm(replayed) != norm(form):
                        counters["violations"] += 1
                        counters["derived_failures"] += 1
                        findings.append(finding(
                            "D4L-ARGOT-DERIV", "FAIL",
                            "register-scoped form %s %r (register %r): declared chain %r applied to "
                            "%r yields %r; the stated inputs and rules do not yield the candidate"
                            % (eid, form, scoped, op, base, replayed)))
                    continue
                if op in rules:
                    verdict, detail = replay_rule(rules[op], base, form, naming)
                    if detail is not None:
                        counters["rule_holds"] += 1
                        findings.append(finding(
                            "D4L-ARGOT-RULE", "HOLD",
                            "register-scoped form %s %r: declared rule %r is not replayable (%s)"
                            % (eid, form, op, detail)))
                    elif verdict is False:
                        counters["violations"] += 1
                        counters["derived_failures"] += 1
                        findings.append(finding(
                            "D4L-ARGOT-DERIV", "FAIL",
                            "register-scoped form %s %r (register %r): declared chain %r applied to "
                            "%r does not yield the candidate; the stated inputs and rules do not "
                            "yield it" % (eid, form, scoped, op, base)))
                    continue
                counters["rule_holds"] += 1
                findings.append(finding(
                    "D4L-ARGOT-RULE", "HOLD",
                    "register-scoped form %s %r: declared derivation %r is neither a declared argot "
                    "operation (%s) nor a licensed packet rule (%s); replay is not possible"
                    % (eid, form, op, ", ".join(sorted(OP_FUNCTIONS)),
                       ", ".join(sorted(rules)) or "none")))

            # The packet's own `formation` idiom states the same relation in the
            # vocabulary the delivered packets use. It is graded for every form
            # record that claims it — scoped or not — because the claim is what
            # the round-17 Δ3 discipline replays, and a packet that declares its
            # rules and then loses them must not read clean.
            if claimed is not None:
                rule_id, stem = claimed
                counters["claimed_chains"] += 1
                if rule_id in rules:
                    verdict, detail = replay_rule(rules[rule_id], stem, form, naming)
                    if detail is not None:
                        counters["rule_holds"] += 1
                        findings.append(finding(
                            "D4L-ARGOT-RULE", "HOLD",
                            "form %s %r: claimed formation rule %r is not replayable (%s)"
                            % (eid, form, rule_id, detail)))
                    elif verdict is False:
                        counters["violations"] += 1
                        findings.append(finding(
                            "D4L-ARGOT-DERIV", "FAIL",
                            "form %s %r (register %r): claimed formation %r applied to stem %r does "
                            "not yield the candidate; the stated inputs and rules do not yield it"
                            % (eid, form, scoped, rule_id, stem)))
                elif rules:
                    counters["violations"] += 1
                    findings.append(finding(
                        "D4L-ARGOT-DERIV", "FAIL",
                        "form %s %r (register %r): claimed formation rule %r is not among the "
                        "packet's declared derivation rules (%s); the stated chain does not exist"
                        % (eid, form, scoped, rule_id, ", ".join(sorted(rules)))))
                else:
                    counters["rule_holds"] += 1
                    findings.append(finding(
                        "D4L-ARGOT-RULE", "HOLD",
                        "form %s %r: claims formation rule %r but the packet declares no "
                        "`morphology.derivation_rules`; the chain is not replayable"
                        % (eid, form, rule_id)))

            if text_of(entry.get("route")).strip() == "borrowed" or \
                    text_of(entry.get("donor_form")).strip():
                replayed, layer_label, problem = replay_borrow(entry, layers)
                if problem is not None:
                    counters["borrow_holds"] += 1
                    findings.append(finding(
                        "D4L-ARGOT-RULE", "HOLD",
                        "register-scoped loan %s %r: %s, so its adaptation cannot be replayed"
                        % (eid, form, problem)))
                elif replayed is not None:
                    counters["borrow_pairs"] += 1
                    if norm(replayed) != norm(form):
                        counters["violations"] += 1
                        findings.append(finding(
                            "D4L-ARGOT-DERIV", "FAIL",
                            "register-scoped loan %s %r (register %r): layer %r substitutions applied "
                            "to donor form %r yield %r; the stated inputs and rules do not yield the "
                            "candidate"
                            % (eid, form, scoped, layer_label,
                               text_of(entry.get("donor_form")).strip(), replayed)))

    # F-6 (reports/round-17/d4/design-brief.md:306-307): the coverage block
    # ---- RL-8 era leg (round 38): a `stamp` form dated before the register
    # exists (REGISTER-ERA-01, reports/round-26/register/rules.md:110-112).
    # Emitted as D4L-ARGOT-ERA so the typed pipeline's L3b leg (which reads
    # `FINDING D4L-ARGOT-`) sees it; the r26 token D4L-ERA is named in-message.
    # Law/identity stamp rows carry no `stage` key and are skipped by design.
    era_floor = "E1"
    for _block, _entries in record_blocks(packet):
        for _entry in _entries:
            if not isinstance(_entry, dict):
                continue
            if text_of(_entry.get("register")).strip() != "stamp":
                continue
            _stage = text_of(_entry.get("stage")).strip()
            if not _stage:
                continue
            if _stage < era_floor:
                counters["era_failures"] += 1
                findings.append(finding(
                    "D4L-ARGOT-ERA", "FAIL",
                    "%s is a `stamp` form dated %s; RGL-05 dates every stamp form "
                    "available_from %s (03-orthography); the r26 token is D4L-ERA"
                    % (text_of(_entry.get("id")).strip() or "?", _stage, era_floor)))

    # reports `derived_forms` and `derived_ok` counts that agree. The pair is
    # materialised here, not at the print, so a consumer can assert it.
    counters["derived_forms"] = counters["derived_pairs"]
    counters["derived_ok"] = counters["derived_pairs"] - counters["derived_failures"]

    declared_ops = packet_declares_ops(packet)
    if declared_ops and counters["register_scoped"] and not counters["derived_pairs"]:
        findings.append(finding(
            "D4L-ARGOT-COVERAGE", "HOLD",
            "packet declares the argot operation(s) %s and %d register-scoped form(s), but no record "
            "carries a derived_from/derivation pair; the forecast derivation relation is declared, "
            "not delivered" % (", ".join(declared_ops), counters["register_scoped"])))
    return findings, counters, declared_ops


def evaluate_text(text, naming):
    try:
        root = naming["load_yaml"](text)
    except naming["YamlError"] as exc:
        return EXIT_UNEVALUATED, [finding(
            "D4L-ARGOT-DATA", "FAIL", "input could not be evaluated: %s" % exc)], Counter()
    except RecursionError:
        return EXIT_UNEVALUATED, [finding(
            "D4L-ARGOT-DATA", "FAIL",
            "input could not be evaluated: flow nesting exceeds the supported depth")], Counter()
    if isinstance(root, dict):
        packets = [root]
    elif isinstance(root, list):
        packets = root
    else:
        return EXIT_UNEVALUATED, [finding(
            "D4L-ARGOT-DATA", "FAIL",
            "input could not be evaluated: root is neither a mapping nor a list of mappings")], Counter()
    if not packets:
        return EXIT_UNEVALUATED, [finding(
            "D4L-ARGOT-DATA", "FAIL", "input could not be evaluated: empty packet list")], Counter()

    findings = []
    totals = Counter()
    multiple = len(packets) > 1
    for index, packet in enumerate(packets):
        if not isinstance(packet, dict):
            return EXIT_UNEVALUATED, [finding(
                "D4L-ARGOT-DATA", "FAIL",
                "input could not be evaluated: packet %d is not a mapping" % (index + 1))], Counter()
        label = text_of(packet.get("name")).strip() or "packet %d" % (index + 1)
        packet_findings, counters, _ops = evaluate_packet(packet, naming)
        totals.update(counters)
        for item in packet_findings:
            if multiple:
                item["message"] = "[packet %r] " % label + item["message"]
            findings.append(item)
    findings.sort(key=lambda item: (item["id"], item["message"]))
    return (EXIT_CLEAN if not findings else EXIT_FINDINGS), findings, totals


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

# The round-17 design's own eleven worked derivations (design-language.md §5),
# quoted verbatim. A leg that cannot re-derive the design's own table cannot
# check anything the design asks for.
DESIGN_TABLE = (
    ("saalumi", "head2", "saalu"),
    ("min", "reverse", "nim"),
    ("kus", "reverse", "suk"),
    ("nam", "reverse", "man"),
    ("nes", "reverse", "sen"),
    ("sam", "reverse", "mas"),
    ("mus", "reverse", "sum"),
    ("kin", "reverse", "nik"),
    ("sun", "reverse", "nus"),
    ("samun", "reverse", "numas"),
    ("makun", "reverse", "nukam"),
)

FIXTURE_EXPECTED = Counter({
    "D4L-ARGOT-DERIV": 4,
    "D4L-ARGOT-RULE": 1,
})

POSITIVE_CONTROL = """\
name: F-argot-positive
phonology: {consonants: [p, t, k, b, d, g, m, n, s, r, l, w, j, h], vowels: [a, e, i, o, u], phonotactics: "(C)V(V)(C)"}
layers:
  - {id: LY-01, name: "West layer", register: trade, substitutions: {sh: s}}
morphology:
  derivation_rules:
    - {id: CX-01, kind: compound, pattern: "^(?P<a>.+)\\\\+(?P<b>.+)$", output: "{a}{b}"}
lexicon:
  - {id: Q-01, term: saalu, register: quote, derived_from: saalumi, derivation: head2}
  - {id: Q-02, term: nim, register: quote, derived_from: min, derivation: reverse}
  - {id: Q-03, term: numas, register: quote, derived_from: samun, derivation: reverse}
  - {id: Q-04, term: sunel, register: quote, derived_from: "su+nel", derivation: CX-01}
  - {id: B-01, term: res, route: borrowed, layer: LY-01, loan_layer: "West layer", donor_form: resh}
"""

COVERAGE_CONTROL = """\
name: F-argot-coverage
morphology:
  derivation_rules:
    - {id: head2, kind: prefix, pattern: "^(?P<stem>.+)$", output: "{stem}"}
lexicon:
  - {id: Q-01, term: nim, register: quote}
  - {id: Q-02, term: suk, register: quote}
"""

# The packet's own `formation` idiom (the D2/D4 shape), in both directions: two
# chains that replay, and — under mutation — a lost rule set or a bad stem.
FORMATION_CONTROL = """\
name: F-argot-formation
morphology:
  derivation_rules:
    - id: UP-COMPOUND
      pattern: "^(?P<B1>[a-z]+)[+](?P<B2>[a-z]+)$"
      output: "{B1}{B2}"
names:
  - {id: NM-01, name: sunel, formation: {stem: "su+nel", bases: [su, nel], rule: UP-COMPOUND}}
  - {id: NM-02, name: banwal, formation: {stem: "ban+wal", bases: [ban, wal], rule: UP-COMPOUND}}
"""


def _recount_derivations(text):
    """Re-derive (forms, failures) from packet bytes, sharing no gate code.

    Counts every mapping that declares a `derivation` key, in either of the two
    styles the tree uses: block style (`  derivation: head2` on its own line,
    the delivered packets) and flow style (`, derivation: head2}` inside a
    `{...}` record, the committed fixture). The `derivation_rules:` key is not a
    match, because the token must be followed directly by a colon. This is
    deliberately not the gate's own reader — a recount that reused the gate's
    parse could not catch a wrong count. The failure half is not inferable from
    bytes alone (it needs the replay), so it is returned as zero and the failing
    control asserts it separately.
    """
    return len(DERIVATION_KEY_RE.findall(text)), 0


DERIVATION_KEY_RE = re.compile(r"(?:^|[,{]\s*)\s*derivation\s*:")


def _printed_pair(text):
    """The (derived_forms, derived_ok) pair the CLI prints for a packet text.

    Runs the gate as a subprocess over a temporary copy of `text` and parses its
    own `coverage:` line, so the assertion is on the delivered output rather
    than on the counter object.
    """
    import subprocess
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False,
                                     encoding="utf-8") as handle:
        handle.write(text)
        temp = handle.name
    try:
        proc = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()),
                               temp], capture_output=True, text=True, check=False)
    finally:
        Path(temp).unlink()
    for line in proc.stdout.splitlines():
        if line.startswith("coverage:"):
            fields = dict(re.findall(r"(\w+)=(\d+)", line))
            return int(fields["derived_forms"]), int(fields["derived_ok"])
    return None


RULE_MISMATCH_CONTROL = """\
name: F-argot-rulemismatch
morphology:
  derivation_rules:
    - id: CX-01
      pattern: "^(?P<a>.+)[+](?P<b>.+)$"
      output: "{a}{b}"
lexicon:
  - {id: Q-01, term: wrong, register: quote, derived_from: nope, derivation: CX-01}
"""

TWO_MIXED_CONTROL = """\
name: F-argot-mixed
morphology:
  derivation_rules:
    - id: CX-01
      pattern: "^(?P<a>.+)[+](?P<b>.+)$"
      output: "{a}{b}"
    - id: UP-COMPOUND
      pattern: "^(?P<B1>[a-z]+)[+](?P<B2>[a-z]+)$"
      output: "{B1}{B2}"
layers:
  - {id: LY-01, name: "West layer", register: trade, substitutions: {sh: s}}
lexicon:
  - {id: Q-01, term: nim, register: quote, derived_from: min, derivation: reverse}
  - {id: Q-02, term: wrong, register: quote, derived_from: nope, derivation: CX-01}
  - {id: Q-03, term: bad, register: quote, formation: {stem: "su+bel", bases: [su, nel], rule: UP-COMPOUND}}
  - {id: B-01, term: res, route: borrowed, layer: LY-01, loan_layer: "West layer", donor_form: resk}
"""


def selftest():
    checks = []

    # 1. the two operations re-derive the design's own eleven worked rows.
    rederived = all(apply_op(op, base) == expected for base, op, expected in DESIGN_TABLE)
    checks.append(("design-table-rederived-11", rederived))
    # 2. the maximal-onset reading is the one that holds, on the row where the
    #    two readings disagree.
    checks.append(("head2-maximal-onset", op_head2("saalumi") == "saalu"))
    checks.append(("head2-maximal-coda-differs", op_head2("saalumi") != "saalum"))
    checks.append(("head2-single-syllable", op_head2("min") == "min"))
    # 2b. the maximal-onset rule is legality-constrained, and that clause is
    #     the whole difference between this implementation and a naive scan:
    #     a two-consonant run splits coda|onset because onset_clusters is false.
    checks.append(("syllabify-cluster-splits-coda-onset",
                   syllabify("tikmes") == ["tik", "mes"]))
    checks.append(("syllabify-naive-scan-differs",
                   syllabify("tikmes") != ["ti", "kme", "s"]))
    checks.append(("syllabify-word-final-run-is-coda",
                   syllabify("ker") == ["ker"] and syllabify("kalker") == ["kal", "ker"]))
    checks.append(("syllabify-vowel-sequence-splits",
                   syllabify("haitun") == ["ha", "i", "tun"]))
    checks.append(("head2-cluster-base",
                   op_head2("tumkalker") == "tumkal" and op_head2("tumkalker") != "tumka"))
    checks.append(("legality-tests-the-template",
                   is_legal_syllable("tik") and is_legal_syllable("kme") is False
                   and is_legal_syllable("tuu") and is_legal_syllable("s") is False))
    checks.append(("reverse-involution", op_reverse(op_reverse("makun")) == "makun"))
    # 3. the operations are discriminating, not always-true.
    checks.append(("leg-discriminates",
                   apply_op("reverse", "min") == "nim" and apply_op("reverse", "min") != "min"))

    naming = load_naming()

    # 4. the committed fixture fails with exactly the planted id set.
    try:
        fixture_text = FIXTURE_PATH.read_text(encoding="utf-8")
        code, findings, _totals = evaluate_text(fixture_text, naming)
    except OSError as exc:
        print("selftest: FAIL — fixture unreadable: %s" % exc)
        return EXIT_FINDINGS
    got = Counter(item["id"] for item in findings)
    expected_ids = [
        line.strip() for line in EXPECTED_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    checks.append(("fixture-exits-1", code == EXIT_FINDINGS))
    checks.append(("fixture-ids-match-expected-file", set(expected_ids) == set(got)))
    checks.append(("fixture-counts-pinned", got == FIXTURE_EXPECTED))
    checks.append(("fixture-names-the-violating-form",
                   any("Q-11" in item["message"] and "saalum" in item["message"] for item in findings)))

    # 5. the positive control is clean: every one of the design's own pairs plus
    #    a licensed packet rule plus a clean borrow replays.
    pos_code, pos_findings, pos_totals = evaluate_text(POSITIVE_CONTROL, naming)
    checks.append(("positive-control-clean", pos_code == EXIT_CLEAN and not pos_findings))
    checks.append(("positive-control-replayed-pairs", pos_totals["derived_pairs"] == 4))
    checks.append(("positive-control-replayed-borrows", pos_totals["borrow_pairs"] == 1))

    # 5b. the packet's own `formation` idiom is graded too, and losing the
    #     declared rules turns a claimed chain into a named FAIL — the mutation
    #     a packet that drops `derivation_rules` would otherwise read clean.
    form_code, form_findings, form_totals = evaluate_text(FORMATION_CONTROL, naming)
    checks.append(("formation-control-clean",
                   form_code == EXIT_CLEAN and form_totals["claimed_chains"] == 2))
    broken_code, broken_findings, _ = evaluate_text(
        FORMATION_CONTROL.replace("derivation_rules:", "derivation_rules_broken:", 1), naming)
    checks.append(("formation-control-rules-lost-held",
                   broken_code == EXIT_FINDINGS
                   and any(item["id"] == "D4L-ARGOT-RULE" for item in broken_findings)))
    checks.append(("formation-control-bad-stem-fails",
                   evaluate_text(FORMATION_CONTROL.replace("stem: \"su+nel\"",
                                                           "stem: \"su+bel\"", 1), naming)[0]
                   == EXIT_FINDINGS))

    # 6. a declared-but-undelivered argot relation is a named HOLD, never silence.
    cov_code, cov_findings, _cov = evaluate_text(COVERAGE_CONTROL, naming)
    checks.append(("coverage-hold-fires",
                   cov_code == EXIT_FINDINGS
                   and [item["id"] for item in cov_findings] == ["D4L-ARGOT-COVERAGE"]))

    # 6b. F-6 (reports/round-17/d4/design-brief.md:306-307): the coverage
    #     block reports `derived_forms` and `derived_ok` counts that agree, and
    #     the pair is CONSUMED, not merely printed. These controls re-derive
    #     both numbers from the committed fixture bytes by an independent line
    #     scan and assert the emitter's own relation against that recount — the
    #     vacuous-pass guard D10b's mission requires. The projector's
    #     byte-identity check provably accepts a lying value, so byte-equality
    #     cannot stand in for this.
    fixture_forms, fixture_failures = _recount_derivations(fixture_text)
    checks.append(("f6-recount-matches-the-fixture",
                   fixture_forms == _totals["derived_pairs"]))
    checks.append(("f6-counters-agree-on-clean-control",
                   pos_totals["derived_forms"] == pos_totals["derived_ok"]
                   and pos_totals["derived_forms"] == 4))
    checks.append(("f6-counters-are-non-vacuous",
                   pos_totals["derived_forms"] > 0))
    # the discriminating control: a record whose declared chain does not replay
    # moves `derived_ok` and leaves `derived_forms` alone.
    _rm_code, _rm_findings, rm_totals = evaluate_text(RULE_MISMATCH_CONTROL, naming)
    checks.append(("f6-counters-disagree-on-a-failing-record",
                   _rm_code == EXIT_FINDINGS
                   and rm_totals["derived_forms"] == 1
                   and rm_totals["derived_ok"] == 0
                   and rm_totals["derived_failures"] == 1))
    # the domain control: `violations` also counts claimed-chain and borrow
    # failures, so the shared total must NOT be the emitter's source. On this
    # control violations (3) exceeds derived_pairs (2), so the formula the block
    # drafted (`derived_pairs - violations`) yields -1 — a negative count.
    _mx_code, _mx_findings, mx_totals = evaluate_text(TWO_MIXED_CONTROL, naming)
    checks.append(("f6-derived-ok-ignores-non-derivation-violations",
                   mx_totals["derived_pairs"] == 2
                   and mx_totals["violations"] == 3
                   and mx_totals["derived_forms"] == 2
                   and mx_totals["derived_ok"] == 1))
    checks.append(("f6-shared-violations-total-is-not-the-emitters-source",
                   mx_totals["derived_ok"]
                   != mx_totals["derived_pairs"] - mx_totals["violations"]))
    checks.append(("f6-derived-forms-is-a-recount-not-a-constant",
                   fixture_forms > 0
                   and fixture_forms != pos_totals["derived_forms"]))
    # the printed line itself is asserted against the recount, so a print that
    # lies about the pair is caught here (D10b's C3 control).
    checks.append(("f6-printed-line-agrees-with-an-independent-recount",
                   _printed_pair(fixture_text) == (fixture_forms,
                                                   fixture_forms - _totals["derived_failures"])))

    # 7. malformed input exits 2 with D4L-ARGOT-DATA, never a traceback.
    for label, text in (("root-is-a-string", "just a string"),
                        ("unclosed-flow", "name: F\nlexicon: [\n"),
                        ("tab-indent", "\tname: F\n")):
        bad_code, bad, _ = evaluate_text(text, naming)
        checks.append(("malformed-%s-exit-2" % label,
                       bad_code == EXIT_UNEVALUATED and bad[0]["id"] == "D4L-ARGOT-DATA"))

    # 8. a negative control the forecast's control C-02 asks for, stated in the
    #    gate's own terms: apply(op, base) != form must be rejected.
    checks.append(("c-02-negative-control-rejected",
                   apply_op("head2", "saalumi") != "saalum"))

    # RL-8 era leg controls (round 38): fires on an E0-dated stamp form, names
    # row+stage, stays silent on E1, and is not masked by a missing law block.
    era_text = ("registers:\n  - {id: QREG-02, register: stamp}\n"
                "register_law:\n  - {id: RGL-05, register: stamp, axis: mark, kind: era, "
                'force: "none \u2014 a dating constraint", speaker: "any speaker", '
                'consequence: "a constraint statement", design_row: []}\n'
                "lexicon:\n"
                "  - {id: L-99, term: tuum, register: stamp, stage: E0}\n"
                "  - {id: L-98, term: kit, register: stamp, stage: E1}\n")
    era_findings = [f for f in evaluate_text(era_text, naming)[1]
                    if f["id"] == "D4L-ARGOT-ERA"]
    checks.append(("era-leg-fires-on-early-stamp-form", len(era_findings) == 1))
    checks.append(("era-leg-names-the-row-and-the-stage",
                   bool(era_findings) and "L-99" in era_findings[0]["message"]
                   and "E0" in era_findings[0]["message"]))
    checks.append(("era-leg-silent-on-e1-stamp-form",
                   not [f for f in evaluate_text(
                       era_text.replace("stage: E0", "stage: E1"), naming)[1]
                       if f["id"] == "D4L-ARGOT-ERA"]))
    checks.append(("era-leg-not-masked-by-missing-law-block",
                   bool([f for f in evaluate_text(
                       "lexicon:\n  - {id: L-99, term: tuum, register: stamp, stage: E0}\n",
                       naming)[1] if f["id"] == "D4L-ARGOT-ERA"])))

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%-38s %s" % (name, "ok" if ok else "FAIL"))
    print("selftest: %d/%d checks passed" % (len(checks) - len(failed), len(checks)))
    return EXIT_FINDINGS if failed else EXIT_CLEAN


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv):
    args = list(argv[1:])
    if args and args[0] in ("--selftest", "--self-test"):
        return selftest()
    if len(args) != 1:
        sys.stderr.write(
            "usage: argot-derivation-gate.py <culture-packet.yml> | --selftest\n")
        return EXIT_UNEVALUATED
    if not NAMING.is_file():
        print(format_finding(finding(
            "D4L-ARGOT-DATA", "FAIL", "dependency missing: %s" % NAMING)))
        return EXIT_UNEVALUATED
    path = Path(args[0])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(format_finding(finding(
            "D4L-ARGOT-DATA", "FAIL", "input could not be evaluated: %s" % exc)))
        return EXIT_UNEVALUATED
    except UnicodeDecodeError as exc:
        print(format_finding(finding(
            "D4L-ARGOT-DATA", "FAIL", "input could not be evaluated: not UTF-8 text: %s" % exc)))
        return EXIT_UNEVALUATED

    naming = load_naming()
    code, findings, totals = evaluate_text(text, naming)
    for item in findings:
        print(format_finding(item))
    try:
        shown = str(path.resolve().relative_to(ROOT))
    except ValueError:
        shown = str(path)
    print("coverage: %s records=%d register_scoped=%d derived_pairs=%d claimed_chains=%d "
          "borrow_pairs=%d violations=%d rule_holds=%d derived_forms=%d derived_ok=%d"
          % (shown, totals["records"], totals["register_scoped"], totals["derived_pairs"],
             totals["claimed_chains"], totals["borrow_pairs"], totals["violations"],
             totals["rule_holds"], totals["derived_forms"], totals["derived_ok"]))
    print("dependency: %s sha256 %s"
          % (NAMING.relative_to(ROOT), sha256_file(NAMING)))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
