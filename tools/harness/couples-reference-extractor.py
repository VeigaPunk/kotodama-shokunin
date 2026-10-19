#!/usr/bin/env python3
"""Successor couples-reference resolver + census (N6 fix; r42 claim O).

Replaces the single-line `- couples:` capture that silently zeroes wrapped
fields. Defect site (filed, unedited): reports/round-19/audit/entry-audit.py:75
`re.search(r"^- couples:\\s*(.*)$", text, re.M)`.

Policy implemented: reports/round-39/calib/basename-couples-policy.md
  Tier 1 direct / Tier 2 slash-free unique-basename fallback / ambiguous /
  unresolved (§2), group alignment (§4), glob-fragment exclusion (§5.6),
  plus the two Ca04 fixes the policy landed without: block extraction (D1)
  and the C12-row-2 blocker/document disposition leg (D2), plus the fifth
  `prospective` class for declared-prospective seeds (O10 §4).

Read-only: opens corpus files, writes nothing. Stdlib only.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = HERE
for _ in range(8):
    if os.path.isdir(os.path.join(LANE, "corpus", "knowledge")):
        break
    LANE = os.path.dirname(LANE)

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
    header field, the first non-indented line, or end of input. Blank lines are
    skipped so a blank-separated continuation still joins (measured: 0 such
    cases in the live corpus, but the rule is total).
    """
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = FIELD_RE.match(line)
        if match and match.group(1) == "couples":
            parts = [match.group(2).strip()]
            for following in lines[index + 1:]:
                if not following.strip():
                    continue
                if FIELD_RE.match(following):
                    break
                if INDENT_RE.match(following):
                    parts.append(following.strip())
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


def classify(ref, entry_dir, prospective=False):
    """(class, mapping). Policy §2 tiers plus the prospective fifth class."""
    for base in (entry_dir, LANE, KNOW):
        if os.path.isfile(os.path.normpath(os.path.join(base, ref))):
            return "direct", None
    if "/" in ref:
        return "unresolved", None
    hits = basename_index().get(os.path.basename(ref), [])
    if len(hits) == 1:
        return "fallback", hits[0]
    if len(hits) > 1:
        return "ambiguous", None
    if GLOB_FRAG_RE.search(ref):
        return "glob-fragment", None
    if prospective:
        return "prospective", None
    return "unresolved", None


def resolve_entry(path):
    """Full resolution record for one entry (read-only)."""
    with open(path, "rb") as handle:
        text = handle.read().decode("utf-8", "replace")
    parts = couples_block(text)
    joined = join_parts(parts)
    prospective = bool(PROSPECTIVE_RE.search(joined))
    documented = bool(TO_VERIFY_RE.search(joined))
    entry_dir = os.path.dirname(os.path.abspath(path))
    tokens = {}
    for ref in sorted(field_refs(text)):
        klass, mapping = classify(ref, entry_dir, prospective)
        # Group label in force at this token: the last label whose group section
        # opens before the token's own position. Tokens are matched by span so a
        # label-like substring inside a filename cannot be mistaken for a label.
        labels = [m.group(1) for m in LABEL_RE.finditer(joined) if m.start() <= joined.find(ref)]
        token_dir = mapping if mapping else (
            "corpus/knowledge/" + labels[-1] + "/" if labels else None
        )
        alignment = None
        if klass == "fallback" and labels:
            alignment = "ok" if mapping.startswith("corpus/knowledge/" + labels[-1] + "/") else "MISALIGNED"
        tokens[ref] = {
            "class": klass,
            "mapping": mapping,
            "group": labels[-1] if labels else None,
            "alignment": alignment,
            "documented": documented,
            "_dir": token_dir,
        }
    return {"path": os.path.relpath(path, LANE), "wrapped": len(parts) > 1, "tokens": tokens}


def census(paths=None):
    if paths is None:
        paths = sorted(glob.glob(os.path.join(KNOW, "*", "*.md")))
    totals = dict.fromkeys(
        ("direct", "fallback", "ambiguous", "unresolved", "prospective", "glob-fragment"), 0
    )
    unresolved, misaligned, wrapped = {}, [], []
    for path in paths:
        record = resolve_entry(path)
        if record["wrapped"]:
            wrapped.append(record["path"])
        for ref, info in record["tokens"].items():
            totals[info["class"]] += 1
            if info["class"] == "unresolved":
                unresolved[ref] = unresolved.get(ref, 0) + 1
            if info["alignment"] == "MISALIGNED":
                misaligned.append((record["path"], ref))
    return {
        "entries": len(paths),
        "refs": sum(totals.values()),
        "totals": totals,
        "unresolved": unresolved,
        "misaligned": misaligned,
        "wrapped_fields": wrapped,
    }


# --- selftest controls ----------------------------------------------------
WRAPPED_POSITIVE = """# Fixture \u2014 wrapped couples field

- topic: fixture
- couples: language \u2014 `sound-symbolism.md`, `writing-systems.md`; prospective
  sibling files: sound-change.md, tone-
  prosody.md
- verified-at: 2026-10-19
- recheck: x
"""

UNWRAPPED_REGRESSION = """# Fixture \u2014 unwrapped couples field

- topic: fixture
- couples: language \u2014 `sound-symbolism.md`, `writing-systems.md`
- verified-at: 2026-10-19
"""

OVER_CAPTURE_TRAP = """# Fixture \u2014 prose paragraph after the field carries a .md mention

- topic: fixture
- couples: language \u2014 `sound-symbolism.md`
- verified-at: 2026-10-19

This opening paragraph deliberately mentions `writing-systems.md` in running
prose. A blank-line-blind parser (C14 fields_of) would attribute it to couples.
"""


def selftest():
    ok = True

    def check(name, condition, detail=""):
        nonlocal ok
        if not condition:
            ok = False
        print(("PASS " if condition else "FAIL ") + name + (" " + detail if detail else ""))

    # 1. wrapped positive: the field reads whole, 4 tokens, hyphen healed
    tokens = sorted(field_refs(WRAPPED_POSITIVE))
    check("wrapped positive 4/4 tokens",
          tokens == ["sound-change.md", "sound-symbolism.md", "tone-prosody.md", "writing-systems.md"],
          str(tokens))
    check("wrapped positive heals soft wrap",
          "tone-prosody.md" in tokens and "prosody.md" not in tokens)

    # 2. unwrapped regression: single-line field unchanged
    check("unwrapped regression",
          sorted(field_refs(UNWRAPPED_REGRESSION)) == ["sound-symbolism.md", "writing-systems.md"])

    # 3. over-capture trap: prose after the field is NOT a couples token
    check("over-capture trap (prose excluded)",
          "writing-systems.md" not in field_refs(OVER_CAPTURE_TRAP),
          str(sorted(field_refs(OVER_CAPTURE_TRAP))))

    # 4. phantom negative: a wrapped field naming an absent target stays visible
    import tempfile
    tmp = tempfile.mkdtemp()
    os.makedirs(os.path.join(tmp, "linguistics"))
    fixture = os.path.join(tmp, "e.md")
    with open(fixture, "w", encoding="utf-8") as handle:
        handle.write(WRAPPED_POSITIVE)
    record = resolve_entry(fixture)
    classes = {ref: info["class"] for ref, info in record["tokens"].items()}
    check("phantom negative: absent wrapped targets are visible, not zeroed",
          classes.get("sound-change.md") == "prospective" and classes.get("tone-prosody.md") == "prospective",
          str(classes))

    # 5. the N6 defect itself: single-line capture of the live field yields 0 tokens
    live = os.path.join(KNOW, "linguistics", "phonetics-phonology.md")
    with open(live, encoding="utf-8") as handle:
        text = handle.read()
    single = re.search(r"^- couples:\s*(.*)$", text, re.M)
    check("N6 regression guard: single-line capture still yields 0 tokens",
          MDREF_RE.findall(single.group(1) if single else "") == [])
    check("N6 regression guard: block read yields 4 tokens",
          len(field_refs(text)) == 4, str(sorted(field_refs(text))))

    # 6. glob fragment is its own class, never unresolved
    check("glob fragment classified",
          classify("-gate.md", tmp) [0] == "glob-fragment")

    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(description="couples-reference resolver + census")
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--census", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return 0 if selftest() else 1
    if args.census:
        result = census()
        totals = result["totals"]
        print("entries=%d refs=%d -> %s" % (
            result["entries"], result["refs"],
            " ".join("%s=%d" % (k, v) for k, v in totals.items() if v),
        ))
        print("  wrapped fields: %d %s" % (len(result["wrapped_fields"]), result["wrapped_fields"]))
        print("  unresolved distinct=%d: %s" % (
            len(result["unresolved"]),
            ", ".join("%s(x%d)" % (k, v) for k, v in sorted(result["unresolved"].items())),
        ))
        print("  misaligned: %s" % (result["misaligned"] or "none"))
        return 0
    if args.paths:
        for path in args.paths:
            record = resolve_entry(path)
            print("%s wrapped=%s tokens=%d" % (record["path"], record["wrapped"], len(record["tokens"])))
            for ref, info in record["tokens"].items():
                print("    %-32s %-14s %s" % (ref, info["class"], info["mapping"] or ""))
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
