#!/usr/bin/env python3
"""Durable resolver + census for the basename-couples policy (r43 claim O).

Policy: reports/round-42/calib/basename-couples-policy-full.md (full successor
of the truncated r39 filing). Defect provenance: reports/round-19/audit/
entry-audit.py:75 (single-line capture); reports/round-39/calib/Ca04-verify.md
D1/D2. Predecessor (NOT edited, NOT imported): tools/harness/
couples-reference-extractor.py (r42, sha256 d8d23a26...), which remains the N6
regression witness.

Read-only: opens corpus entries, writes nothing. Stdlib only.
Modes: --selftest | --census [--json] | [PATH ...]
Exit: 0 green/completed, 1 selftest red, 2 usage/IO/root error.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.realpath(__file__))
LANE = HERE
for _ in range(8):
    if os.path.isdir(os.path.join(LANE, "corpus", "knowledge")):
        break
    LANE = os.path.dirname(LANE)
else:
    sys.exit("lane root not found upward from " + HERE)
KNOW = os.path.join(LANE, "corpus", "knowledge")

FIELD_RE = re.compile(r"^- ([a-z][a-z-]*):[ \t]*(.*)$")
INDENT_RE = re.compile(r"^[ \t]+\S")
MDREF_RE = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
BRACE_RE = re.compile(r"\{([^{}]*)\}")
LABEL_RE = re.compile(
    r"(?:^|;\s*)(myth-symbol|linguistics|culture-material|civilizations|verification|synthesis)\s*[\u2014-]"
)
PROSPECTIVE_RE = re.compile(
    r"(prospective sibling files|files to seed|sibling knowledge files to seed)\s*:", re.I
)
TO_VERIFY_RE = re.compile(r"\(to-verify", re.I)
GLOB_FRAG_RE = re.compile(r"^-|\*")


def couples_block(text):
    """The `- couples:` field value as a list of parts, continuations included.

    Continuations are indentation-bounded (`^[ \\t]+\\S`) and stop at the next
    header field, the first non-indented line, or end of input. A blank line
    terminates the block unless the previous part ends in a hyphen soft wrap
    and the next line is indented (measured: 0 blank-separated continuations in
    the live corpus; the hyphen exception keeps the rule total without letting
    body prose after a blank line be captured).
    """
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = FIELD_RE.match(line)
        if match and match.group(1) == "couples":
            parts = [match.group(2).strip()]
            saw_blank = False
            for following in lines[index + 1:]:
                if not following.strip():
                    saw_blank = True
                    continue
                if FIELD_RE.match(following):
                    break
                soft_wrap = parts[-1].endswith("-") and not saw_blank
                if INDENT_RE.match(following) and (not saw_blank or soft_wrap):
                    parts.append(following.strip())
                    saw_blank = False
                    continue
                break
            return parts
    return []


def join_parts(parts):
    """Join field parts, healing a hyphen soft-wrap.

    `tone-` + `prosody.md` -> `tone-prosody.md`. A part ending in a hyphen
    preceded by a word character is a soft wrap: concatenate directly, KEEPING
    the hyphen. `"".join` (hyphen deleted) yields `toneprosody.md`; `" ".join`
    yields two broken tokens. Both are wrong.
    """
    out = ""
    for part in parts:
        if not out:
            out = part
        elif out.endswith("-") and re.search(r"[A-Za-z0-9_]-$", out):
            out += part
        else:
            out += " " + part
    return out


def couples_field(text):
    """The joined `- couples:` value (single string)."""
    return join_parts(couples_block(text))


def expand_braces(value):
    match = BRACE_RE.search(value)
    if not match:
        return [value]
    out = []
    for alternative in match.group(1).split(","):
        out.extend(
            expand_braces(value[: match.start()] + alternative + value[match.end():])
        )
    return out


def field_refs(text):
    """Per-entry deduplicated couples tokens, brace-expanded one level."""
    refs = set()
    for raw in MDREF_RE.findall(couples_field(text)):
        for candidate in expand_braces(raw):
            refs.add(candidate.strip())
    return refs


_BASENAME_INDEX = None


def basename_index():
    global _BASENAME_INDEX
    if _BASENAME_INDEX is None:
        index = {}
        for path in glob.glob(os.path.join(KNOW, "*", "*.md")):
            index.setdefault(os.path.basename(path), []).append(os.path.relpath(path, LANE))
        _BASENAME_INDEX = index
    return _BASENAME_INDEX

CLASSES = ("direct", "fallback", "ambiguous", "unresolved")
ARTIFACTS = ("glob-fragment",)


def classify(ref, entry_dir, index=None):
    """(class, mapping). Policy §2 tiers; glob fragments are artifacts."""
    for base in (entry_dir, LANE, KNOW):
        if os.path.isfile(os.path.normpath(os.path.join(base, ref))):
            return "direct", None
    if GLOB_FRAG_RE.search(ref):
        return "glob-fragment", None
    if "/" in ref:
        return "unresolved", None
    table = basename_index() if index is None else index
    hits = table.get(os.path.basename(ref), [])
    if len(hits) == 1:
        return "fallback", hits[0]
    if len(hits) > 1:
        return "ambiguous", None
    return "unresolved", None


def resolve_entry(path, index=None):
    """Full resolution record for one entry (read-only)."""
    with open(path, "rb") as handle:
        text = handle.read().decode("utf-8", "replace")
    parts = couples_block(text)
    joined = join_parts(parts)
    prospective_at = PROSPECTIVE_RE.search(joined)
    documented = bool(TO_VERIFY_RE.search(joined))
    entry_dir = os.path.dirname(os.path.abspath(path))
    tokens = {}
    for ref in sorted(field_refs(text)):
        klass, mapping = classify(ref, entry_dir, index=index)
        position = joined.find(ref)
        labels = [m.group(1) for m in LABEL_RE.finditer(joined) if m.start() <= position]
        label = labels[-1] if labels else None
        alignment = None
        if klass == "fallback" and label:
            alignment = (
                "ok" if mapping.startswith("corpus/knowledge/" + label + "/")
                else "MISALIGNED"
            )
        disposition = None
        if klass == "unresolved":
            prospective = bool(prospective_at) and position >= prospective_at.start()
            disposition = (
                "declared-prospective-seed" if prospective else "dangling-reference"
            )
        tokens[ref] = {
            "class": klass,
            "mapping": mapping,
            "group": label,
            "alignment": alignment,
            "documented": documented,
            "disposition": disposition,
        }
    return {"path": os.path.relpath(path, LANE), "wrapped": len(parts) > 1, "tokens": tokens}


def _reason(info):
    if info["class"] == "unresolved":
        if info["disposition"] == "declared-prospective-seed":
            return (
                "declared prospective/sibling-seed token in the couples field; "
                "never written, not a referenced entry"
            )
        return (
            "Tier 1 failed and the token is not eligible for the unique-basename "
            "fallback (slash-bearing or zero index hits)"
        )
    if info["class"] == "ambiguous":
        return (
            "two or more corpus files carry this basename; the fallback cannot "
            "choose; needs an explicit path or a re-partition"
        )
    return "glob pattern fragment (policy 5.6): extractor artifact, not a couples finding"


def census(paths=None, index=None):
    if paths is None:
        paths = sorted(glob.glob(os.path.join(KNOW, "*", "*.md")))
    totals = dict.fromkeys(CLASSES + ARTIFACTS, 0)
    fallback_mappings = {}
    disposition_rows = {name: [] for name in ("unresolved", "ambiguous") + ARTIFACTS}
    misaligned = []
    wrapped = []
    entries_detail = []
    for path in paths:
        record = resolve_entry(path, index=index)
        if record["wrapped"]:
            wrapped.append(record["path"])
        for ref, info in record["tokens"].items():
            totals[info["class"]] += 1
            if info["class"] == "fallback":
                row = fallback_mappings.setdefault(
                    ref, {"mapping": info["mapping"], "occurrences": 0}
                )
                row["occurrences"] += 1
            if info["class"] in disposition_rows:
                disposition_rows[info["class"]].append({
                    "entry": record["path"],
                    "token": ref,
                    "mapping": info["mapping"],
                    "disposition": info["disposition"] or "extractor-artifact",
                    "reason": _reason(info),
                    "c12": (
                        "not-applicable" if info["class"] == "glob-fragment"
                        else ("documented" if info["documented"] else "blocker")
                    ),
                })
            if info["alignment"] == "MISALIGNED":
                misaligned.append((record["path"], ref))
        entries_detail.append(record)
    four = {name: totals[name] for name in CLASSES}
    artifacts = {name: totals[name] for name in ARTIFACTS}
    refs = sum(totals.values())
    return {
        "entries": len(paths),
        "refs": refs,
        "four_class_totals": four,
        "artifact_totals": artifacts,
        "conservation": sum(four.values()) + sum(artifacts.values()) == refs,
        "wrapped_fields": wrapped,
        "fallback_mappings": fallback_mappings,
        "disposition": disposition_rows,
        "misaligned": misaligned,
        "entries_detail": entries_detail,
    }


# --- selftest controls (in-memory fixtures; one read-only live read) --------
LIVE_PATH = os.path.join(KNOW, "linguistics", "phonetics-phonology.md")
LIVE_WRAPPED = (
    "- couples: language (this file, core method); myth (divine/true names, taboo\n"
    "  naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,\n"
    "  bouba/kiki iconography); era (Neolithic bite \u2192 f/v, sound-change dating of\n"
    "  strata); costume (masks/mouthgear vs articulation, whistle & drum channels);\n"
    "  environment/anatomy design; prospective sibling files: sound-change.md, tone-\n"
    "  prosody.md, sound-symbolism.md, writing-systems.md\n"
)
LIVE_TOKENS = {
    "sound-change.md", "tone-prosody.md", "sound-symbolism.md", "writing-systems.md",
}
PHANTOM_FIELD = (
    "- couples: sibling \u2014 `synthetic-phantom-alpha.md`; wrapped seed \u2014 `synthetic-\n"
    "  phantom-beta.md`\n"
)
PHANTOM_TOKENS = {"synthetic-phantom-alpha.md", "synthetic-phantom-beta.md"}
AMBIG_REF = "synthetic-dup-basename.md"
AMBIG_INDEX = {
    AMBIG_REF: [
        "corpus/knowledge/linguistics/" + AMBIG_REF,
        "corpus/knowledge/myth-symbol/" + AMBIG_REF,
    ]
}
UNIQ_REF = "synthetic-uniq-basename.md"
UNIQ_INDEX = {UNIQ_REF: ["corpus/knowledge/linguistics/" + UNIQ_REF]}
DIRECT_REF = "writing-systems.md"
DIRECT_SHADOW = {DIRECT_REF: ["corpus/knowledge/myth-symbol/" + DIRECT_REF]}


def _live_slice(text, count=6):
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("- couples:"):
            return "\n".join(lines[index:index + count]) + "\n", index + 1
    return "", None


def selftest():
    passed, failed = 0, []

    def check(name, condition, detail=""):
        nonlocal passed
        if condition:
            passed += 1
            print("PASS " + name)
        else:
            failed.append(name)
            print("FAIL " + name + (("  [" + str(detail) + "]") if detail != "" else ""))

    with open(LIVE_PATH, encoding="utf-8") as handle:
        live_text = handle.read()
    live_slice, live_line = _live_slice(live_text)
    check("S1a embedded fixture == live bytes at :%s" % live_line,
          live_slice == LIVE_WRAPPED, "live_line=%s" % live_line)

    tokens = field_refs(LIVE_WRAPPED)
    check("S1b wrapped field extracts 4/4 by identity (not arity)",
          tokens == LIVE_TOKENS, sorted(tokens))
    check("S1c no mangled token (prosody.md / toneprosody.md / space split)",
          not ({"prosody.md", "toneprosody.md", "tone- prosody.md"} & tokens),
          sorted(tokens))

    single = re.search(r"^- couples:\s*(.*)$", LIVE_WRAPPED, re.M)
    single_tokens = set(MDREF_RE.findall(single.group(1) if single else ""))
    check("S1d before-state: the filed single-line capture yields 0 tokens",
          single_tokens == set(), sorted(single_tokens))

    parts = couples_block(LIVE_WRAPPED)
    space_tokens = set(MDREF_RE.findall(" ".join(parts)))
    check("S1e space-join is the rejected shape (prosody.md, never tone-prosody.md)",
          "prosody.md" in space_tokens and "tone-prosody.md" not in space_tokens,
          sorted(space_tokens))

    entry_dir = os.path.dirname(LIVE_PATH)
    live_classes = {t: classify(t, entry_dir)[0] for t in sorted(LIVE_TOKENS)}
    check("S1f live field resolves 2 direct + 2 unresolved (four-class policy)",
          live_classes == {
              "sound-change.md": "unresolved",
              "tone-prosody.md": "unresolved",
              "sound-symbolism.md": "direct",
              "writing-systems.md": "direct",
          }, live_classes)

    phantom_tokens = field_refs(PHANTOM_FIELD)
    check("S2a phantom tokens survive extraction 2/2",
          phantom_tokens == PHANTOM_TOKENS, sorted(phantom_tokens))
    check("S2b hyphen-wrapped phantom heals to synthetic-phantom-beta.md",
          "synthetic-phantom-beta.md" in phantom_tokens
          and "phantom-beta.md" not in phantom_tokens, sorted(phantom_tokens))
    empty = {}
    phantom_classes = {t: classify(t, entry_dir, index=empty)[0]
                       for t in sorted(phantom_tokens)}
    check("S2c zero basename hits -> unresolved (both, not dropped)",
          phantom_classes == {t: "unresolved" for t in PHANTOM_TOKENS},
          phantom_classes)

    amb_class, amb_map = classify(AMBIG_REF, entry_dir, index=AMBIG_INDEX)
    check("S3a two basename hits -> ambiguous", amb_class == "ambiguous", amb_class)
    check("S3b ambiguous is not guessed to one path", amb_map is None, amb_map)
    uniq_class, uniq_map = classify(UNIQ_REF, entry_dir, index=UNIQ_INDEX)
    check("S3c one basename hit -> fallback with its explicit mapping",
          uniq_class == "fallback" and uniq_map == UNIQ_INDEX[UNIQ_REF][0],
          (uniq_class, uniq_map))

    direct_class, direct_map = classify(DIRECT_REF, entry_dir, index=DIRECT_SHADOW)
    check("S4a Tier-1 direct wins over a same-basename hit elsewhere (5.4)",
          direct_class == "direct", direct_class)
    check("S4b direct carries no fallback mapping", direct_map is None, direct_map)
    path_class, _ = classify("corpus/knowledge/linguistics/writing-systems.md",
                             entry_dir, index={})
    check("S4c corpus-relative path token -> direct (Tier-1 base 3)",
          path_class == "direct", path_class)

    for label, text, table in (
        ("live", LIVE_WRAPPED, None),
        ("phantom", PHANTOM_FIELD, empty),
        ("ambiguous", "- couples: shared \u2014 `%s`\n" % AMBIG_REF, AMBIG_INDEX),
        ("direct", "- couples: anchor \u2014 `%s`\n" % DIRECT_REF, DIRECT_SHADOW),
    ):
        refs = field_refs(text)
        classes = [classify(r, entry_dir, index=table)[0] for r in refs]
        check("S5 no-drop %s: %d/%d tokens classed" % (label, len(classes), len(refs)),
              len(classes) == len(refs) and set(classes) <= set(CLASSES) | set(ARTIFACTS),
              sorted(zip(sorted(refs), classes)))

    slash_class, _ = classify("linguistics/hero-journey-variants.md", entry_dir)
    check("S6 slash-bearing token stays unresolved despite a unique basename elsewhere",
          slash_class == "unresolved", slash_class)

    boundary = ("- couples: method \u2014 `writing-systems.md`\n\n"
                "Body prose names `sound-symbolism.md`.\n")
    check("S7a body prose after a blank line is excluded",
          field_refs(boundary) == {"writing-systems.md"}, sorted(field_refs(boundary)))
    last_header = ("- topic: fixture\n- couples: `writing-systems.md`\n"
                   "## Section\n\nProse names `sound-symbolism.md`.\n")
    check("S7b couples as the last header field does not swallow the body",
          field_refs(last_header) == {"writing-systems.md"}, sorted(field_refs(last_header)))

    blank_indented = ("- couples: method \u2014 `writing-systems.md`\n\n"
                      "  Indented body prose names `sound-symbolism.md`.\n")
    check("S7c blank line + indented prose is excluded (no over-capture)",
          field_refs(blank_indented) == {"writing-systems.md"},
          sorted(field_refs(blank_indented)))

    glob_class, _ = classify("-gate.md", entry_dir, index=empty)
    check("S8 glob fragment is an artifact, not an unresolved finding (5.6)",
          glob_class == "glob-fragment", glob_class)
    glob_two = { "-gate.md": ["corpus/knowledge/verification/-gate.md",
                              "corpus/knowledge/linguistics/-gate.md"] }
    check("S8b glob fragment wins over the ambiguous branch (5.6)",
          classify("-gate.md", entry_dir, index=glob_two) == ("glob-fragment", None),
          classify("-gate.md", entry_dir, index=glob_two))

    result = census()
    check("S9 live census conservation (four classes + artifacts == refs)",
          result["conservation"] and result["refs"] == sum(
              result["four_class_totals"].values()) + sum(result["artifact_totals"].values()),
          (result["refs"], result["four_class_totals"], result["artifact_totals"]))
    wrapped_record = resolve_entry(LIVE_PATH)
    check("S10 live wrapped entry reads 4 tokens (2 direct + 2 unresolved)",
          wrapped_record["wrapped"] and len(wrapped_record["tokens"]) == 4,
          wrapped_record["tokens"])

    total = passed + len(failed)
    print("SELFTEST %s: %d/%d controls" % ("OK" if not failed else "FAIL", passed, total))
    if failed:
        print("  failed: " + ", ".join(failed))
    return not failed


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="basename-couples resolver (Tier 1 direct + Tier 2 fallback)")
    parser.add_argument("paths", nargs="*")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--selftest", action="store_true")
    modes.add_argument("--census", action="store_true")
    parser.add_argument("--json", "--census-json", action="store_true", dest="json")
    args = parser.parse_args(argv)
    if args.json and not (args.census or args.paths):
        parser.error("--json requires --census or PATH")
    if args.selftest:
        return 0 if selftest() else 1
    if args.census:
        result = census()
        if args.json:
            payload = dict(result)
            payload["schema"] = "kotodama-couples-census-v3"
            payload["round"] = 43
            payload["tool"] = os.path.relpath(os.path.realpath(__file__), LANE)
            with open(__file__, "rb") as handle:
                payload["tool_sha256"] = hashlib.sha256(handle.read()).hexdigest()
            print(json.dumps(payload, indent=1, sort_keys=True))
            return 0
        four = result["four_class_totals"]
        artifacts = result["artifact_totals"]
        print("entries=%d refs=%d" % (result["entries"], result["refs"]))
        print("  policy four-class: direct=%d fallback=%d ambiguous=%d unresolved=%d" % (
            four["direct"], four["fallback"], four["ambiguous"], four["unresolved"]))
        print("  artifacts (excluded from the four-class totals): %s" % (
            " ".join("%s=%d" % (k, v) for k, v in artifacts.items()),))
        print("  conservation: %s (sum=%d refs=%d)" % (
            result["conservation"],
            sum(four.values()) + sum(artifacts.values()), result["refs"]))
        print("  wrapped fields: %d %s" % (
            len(result["wrapped_fields"]), result["wrapped_fields"]))
        print("  fallback mappings (%d distinct):" % len(result["fallback_mappings"]))
        for ref, row in sorted(result["fallback_mappings"].items()):
            print("    %-40s -> %-60s x%d" % (ref, row["mapping"], row["occurrences"]))
        for name in ("unresolved", "ambiguous") + ARTIFACTS:
            rows = result["disposition"][name]
            print("  %s (%d rows):" % (name, len(rows)))
            for row in rows:
                print("    %-36s %-52s %-28s c12=%s" % (
                    row["token"], row["entry"], row["disposition"], row["c12"]))
        print("  misaligned: %s" % (result["misaligned"] or "none"))
        return 0
    if args.paths:
        if args.json:
            records = []
            for path in args.paths:
                if not os.path.isfile(path):
                    sys.exit("entry not found: " + path)
                records.append(resolve_entry(path))
            print(json.dumps(records, indent=1, sort_keys=True))
            return 0
        for path in args.paths:
            if not os.path.isfile(path):
                sys.exit("entry not found: " + path)
            record = resolve_entry(path)
            print("%s wrapped=%s tokens=%d" % (
                record["path"], record["wrapped"], len(record["tokens"])))
            for ref, info in record["tokens"].items():
                print("    %-32s %-14s %-28s %s" % (
                    ref, info["class"], info["disposition"] or "",
                    info["mapping"] or ""))
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
