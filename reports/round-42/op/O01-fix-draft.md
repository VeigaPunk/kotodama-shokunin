- Seat: O01 | executor | claim O | date 2026-10-19 | baseline ac47c78

# O01 — N6 fix draft: block-parser couples extraction (fenced patch against the confirmed host)

Assignment (verbatim, `reports/round-42/targets.json` seat `O01`): "The fix patch
(fenced diff against the confirmed host): a block parser reading the whole couples
field incl. continuations." Out: `op/O01-fix-draft.md`. Claim O
(`reports/round-42/claims.json:13-18`). This fragment is a **fenced draft** — it
stages nothing under `corpus/` or `tools/` and edits no filed byte.

## 0. Verdict

The defect is reproduced live, the host is confirmed by line, and the patch is
**verified by execution**: spliced into a scratch copy of the host at the correct
directory depth, the instrument's own selftest stays green (8/8 PASS) and the
wrapped field moves from **`couples=0 unresolved=[]`** to
**`couples=2 unresolved=['sound-change.md','tone-prosody.md']`**, with **zero
change to any other entry's token set (1/220)**. The patch below is the
minimal-semantics form; the full successor instrument is in §6.

Two independent peer seats (K01 §1–§5, O10 §1–§4) landed the same host, the same
unwrap rule, and the same census numbers as this seat; §5 records the agreement
and the one place this seat found a defect in its *own* first draft.

## 1. The host, confirmed by line (not assumed)

Ca04's guess ("likely the r39 C12 runbook's resolver") is wrong — C12 is a
runbook *document* (`reports/round-35/cov/C12-audit-runbook.md`), not a couples
resolver. The implementation carrying the single-line extractor:

- **`reports/round-19/audit/entry-audit.py:74-96`** — `def couples_targets(text, path)`.
  **`:75` is the defect site**: `m = re.search(r"^- couples:\s*(.*)$", text, re.M)`.
  With `re.M`, `$` stops at the first newline, so the capture is exactly the first
  physical line; `:80-82` runs `MDREF_RE.findall` over that one line only.
- **`:105,118-119,130`** — the call site. The result feeds `couples_resolved` /
  `couples_unresolved` and the `quality_bar` conjunction (`:130 and not unresolved`).
  A zeroed field therefore does not merely miscount: it *removes* tokens from the
  gate's input and makes the entry look like it couples nothing — the
  `empty-couples` shape `tools/gates/provenance-audit.py:16-18` treats as a
  reference-not-craft defect. A silent zero is worse than a visible failure.
- **Copy count (measured, this seat).** A regex scan for the single-line capture
  finds it in **exactly two** live instruments: `reports/round-19/audit/entry-audit.py`
  (sha256 `e7992c32…`) and `reports/round-27/audit/entry-audit.py`
  (`fb589b28…`), the latter at its own `:275` (`COUPLES_TOKEN_RE` at `:271`).
  `reports/round-28/audit/entry-audit.py` (`918a0c1e…`) has **0** such sites: it
  imports r27's core by path (`:63-68 load_core`, "no copy, no divergence") and
  only prints `couples_unresolved` (`:251,264-268`). So **r27 is the live second
  copy** and r28 inherits whatever r27 does. This seat therefore names the host
  set as **{r19, r27}**, superseding K01's `to-verify` on that point (K01 §Owed
  asked the executor to confirm before claiming the extractor is singular).

**Host constraint (binding, from `shared_rules` and K01 §7).** Both hosts are
filed bytes (`reports/round-1..41/**` is never edited). The patch **cannot** be
applied in place. It lands either (a) as a successor instrument that the round
owns, or (b) — if the integrator chooses — as a one-function splice into a
future revision of those files, in which case this fragment supplies the exact
diff in §3. This seat does not make that choice; it supplies both forms.

## 2. The defect, measured

The corpus has **exactly one** wrapped `couples:` field (independently counted
this seat; K01 §5 and O10 §3 agree):

```
corpus/knowledge/linguistics/phonetics-phonology.md:72-77
72  - couples: language (this file, core method); myth (divine/true names, taboo
73    naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74    bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75    strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76    environment/anatomy design; prospective sibling files: sound-change.md, tone-
77    prosody.md, sound-symbolism.md, writing-systems.md
```

Line 78 is blank; line 79 is `## 1. Two levels: phonetics vs phonology`. The
field is bounded on both sides, which matters for the stopping rule (§3).

Measured on the live field (read-only, `python3 -B`, this seat):

| extractor | tokens captured |
|---|---|
| single-line (`entry-audit.py:75`) | **0** — capture is `'language (this file, core method); myth (divine/true names, taboo'`, no `.md` token |
| block + space join | 4 but **mis-named**: `prosody.md`, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md` |
| block + hyphen-delete | 4 but **mis-named**: `toneprosody.md`, … |
| **block + soft-wrap heal (this fix)** | **4 correct**: `sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`, `writing-systems.md` |

Existence against the three Tier-1 bases: `sound-symbolism.md` and
`writing-systems.md` resolve **direct**; `sound-change.md` and `tone-prosody.md`
are **absent** — the two phantom attributions the claim asks to disposition (§5).

**The join rule is load-bearing, not cosmetic.** The line break falls *inside* a
filename (`tone-` / `prosody.md`). Two of the four plausible joins produce a
plausible-looking but wrong token, so the fix must state the rule: *if a part ends
in a hyphen preceded by a word character, concatenate the next part directly and
**keep** the hyphen.* `"".join` (hyphen deleted) and `" ".join` (token split) are
both wrong. This discharges Ca04's `to-verify` on the mangled `prosody.md`.

**The reading is no longer inference — the file names the token itself.** The
same entry writes the name in full and unwrapped at
`corpus/knowledge/linguistics/phonetics-phonology.md:279`:

```
279  - Natural partners: `sound-change.md` (diachrony → §5), `tone-prosody.md`,
```

`tone-prosody.md` appears verbatim in the entry body while the header field spells
it as `tone-` / `prosody.md` across `:76-77`. So the soft-wrap heal is not a
convention this seat chose; it is the only join that recovers a token the entry
itself uses. (`sound-symbolism.md` and `writing-systems.md` likewise appear twice
each in that file.) Independently observed by O04 (`O04-verify.md:315-322`).

## 3. The fix — fenced diff against the confirmed host

Minimal splice replacing `reports/round-19/audit/entry-audit.py:74-96`. Everything
downstream (`:80-95`) is unchanged because it already operates on a string. This
diff was produced by `diff -u` on the before/after extracts and is applied
verbatim in §4's execution evidence.

```diff
--- reports/round-19/audit/entry-audit.py:74-96
+++ reports/round-19/audit/entry-audit.py (fixed)
@@ -1,8 +1,42 @@
+def couples_field_block(text):
+    """The `- couples:` value with its indented continuations joined.
+
+    A soft wrap inside a filename (`tone-` + `prosody.md`) is healed by
+    concatenating a part that ends in a hyphen preceded by a word character,
+    keeping the hyphen. Stopping rule: the field ends at the next `- key:`
+    header line, at the first non-indented line, or at end of input.
+    """
+    lines = text.splitlines()
+    for index, line in enumerate(lines):
+        m = re.match(r"^- couples:[ \t]*(.*)$", line)
+        if not m:
+            continue
+        parts = [m.group(1).strip()]
+        for following in lines[index + 1:]:
+            if not following.strip():
+                continue
+            if re.match(r"^- [a-z][a-z-]*:", following):
+                break
+            if following[:1] in (" ", "\t"):
+                parts.append(following.strip())
+                continue
+            break
+        out = ""
+        for part in parts:
+            if not out:
+                out = part
+            elif out.endswith("-") and re.search(r"[A-Za-z0-9_]-$", out):
+                out += part
+            else:
+                out += " " + part
+        return out
+    return ""
+
+
 def couples_targets(text, path):
-    m = re.search(r"^- couples:\s*(.*)$", text, re.M)
-    if not m:
+    line = couples_field_block(text)
+    if not line:
         return [], []
-    line = m.group(1)
     refs = set()
     for raw in MDREF_RE.findall(line):
         for c in expand_braces(raw):
```

The same splice applies to `reports/round-27/audit/entry-audit.py:274-286`
(identical `couples_targets` body, `COUPLES_TOKEN_RE` at `:271`); r28 needs no
patch because it delegates to r27.

**Stopping-rule note.** The rule is *indentation-bounded* and also stops at a
`- key:` line, deliberately. It does **not** append a blank-separated
non-indented paragraph. That is the difference from C14's `fields_of`
(`reports/round-35/cov/C14-audit-6-10.md:225-236`), which appends any non-blank
line and so joins the entry's opening prose paragraph onto the couples value —
K01's D1b over-capture, a false-positive generator. `tools/gates/provenance-audit.py:244-261`
`field_block` already implements the correct rule (`INDENT_RE` at `:77`), which is
why §6's instrument follows that precedent rather than C14's.

Boundary behaviour measured on synthetic in-memory cases (no writes):

```
unwrapped          -> ['a — `x.md`']
wrapped            -> ['a — `x.md`, `y-', 'z.md`']
blank-between      -> ['a — `x.md`', '`y.md`']
stops-at-header    -> ['a — `x.md`']        # - follows: is not swallowed
stops-at-prose     -> ['a — `x.md`']        # body prose is not swallowed
tab-continuation   -> ['a — `x.md`', '`y.md`']
code-fence-body    -> ['a — `x.md`']
```

Corpus-wide, **0** entries have a non-indented body line directly after the
field, and **0** have a blank-then-indented continuation: 198 fields are followed
immediately by the next `- key:` line, 21 by a blank then a `## ` heading, 1 by an
indented continuation. So the stopping rule is exercised in its correct branch on
every entry.

## 4. Execution evidence — the patch verified on a real host copy

Because the host is filed bytes, the patch was verified by splicing it into a
scratch copy **at the host's own directory depth** (the instrument computes
`LANE = abspath(HERE/../../..)`, so a relocated copy silently re-roots — this bit
me once, see §5).

Setup: `.scratch/o01-successor/mirror/reports/round-19/audit/entry-audit.py`
(patched bytes) with `.scratch/o01-successor/mirror/corpus` a symlink to the live
`corpus/`, so `LANE` resolves to the mirror and the corpus reads live. No filed
byte was touched; nothing was executed from `reports/round-*/run-validation.py`.

```
$ python3 -B <mirror>/entry-audit.py --selftest
PASS braces / PASS braces nested / PASS selftest entry quality / PASS selftest source locator
PASS selftest gap / PASS selftest decision / PASS selftest couples resolve
PASS negative control (no sources fails)                                    exit=0

$ python3 -B <mirror>/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md
FAIL … src=15/15 couples=2 unresolved=['sound-change.md', 'tone-prosody.md'] gap=False dec=True
TOTAL 0/1 clear the bar

$ python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md   # BEFORE, read-only
FAIL … src=15/15 couples=0 unresolved=[] gap=False dec=True
TOTAL 0/1 clear the bar
```

`couples=0 unresolved=[]` → `couples=2 unresolved=[…]` is the whole N6 fix in one
line: the field goes from **invisible** to **counted**, with the two real targets
resolving and the two phantoms made visible rather than silently dropped.

**No-regression oracle (regression on any other entry is a hard failure).** Diffing
each entry's brace-expanded token set, single-line vs fixed:

```
entries=220  entries whose token set changed: 1
  corpus/knowledge/linguistics/phonetics-phonology.md
     dropped=[] added=['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
```

Blast radius is **exactly one entry**, and the operation is a strict superset
(nothing dropped). The second oracle is the sacred-kingship entry, whose 36 tokens
are the r39 policy's documented population: before **and** after the patch the
instrument reports `couples=21 unresolved=[15 tokens]` — identical, so the fix
disturbs no single-line field. (Its `quality_bar` stays False from the
pre-existing `src=30/31` locator leg, not from couples; not this claim's scope.)

## 5. Corrected census + agreement with the peer seats

Recount over all **220** `corpus/knowledge/*/*.md`, per-entry deduplicated,
brace-expanded one level, classified per the r39 policy §2 (`direct` / slash-free
unique-basename `fallback` / `ambiguous` / `unresolved`) plus the two classes the
policy lacks:

```
entries=220 refs=2611
  direct=2437  fallback=166  ambiguous=0  unresolved=2  prospective=5  glob-fragment=1
  2437 + 166 + 0 + 2 + 5 + 1 = 2611  ✓
  wrapped fields: 1   misaligned: none
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
```

The single-line extractor on the same classifier gives
`2607 = 2435 + 166 + 0 + 6`; **`2607 + 4 = 2611`**, with `direct` +2
(`sound-symbolism.md`, `writing-systems.md`) and the unresolved-side +2
(`sound-change.md`, `tone-prosody.md`). `fallback` and `ambiguous` are unchanged —
the fix touches only the wrapped field. This matches K01 §5 rows A/B and O10 §4
line for line.

**On the r39 policy's `2504`.** That figure is a **212-entry** measurement
(`basename-couples-policy.md` §6 Part 2, `entries=212 refs=2504 -> 2335/163/0/6`).
The live corpus is **220** entries, so `2504` must **not** be "corrected" by
subtracting two phantoms — the denominator itself moved. Re-running the policy's
own §6 recipe byte-exact today reproduces the single-line extractor exactly
(`entries=220 refs=2607 -> 2435/166/0/6`), i.e. **the policy's own verification
recipe still carries the N6 defect**; Ca04's D1 fix was never applied to the
landed policy text (consistent with queue row `r39-basename-successor-instrument`).

**The two phantoms dispositioned (claim O's `after_required`).** The field's own
prose calls them *"prospective sibling files:"* — it declares these are planned,
not present. The same construction appears at `corpus/knowledge/linguistics/language-contact.md:7`
(*"sibling knowledge files to seed:"*, three absent targets). A plain `unresolved`
verdict mislabels a declared intention as a dangling reference, so this fix adds a
**fifth class `prospective`** with a non-blocker disposition — independently
reached by O10 §4. That is why `unresolved` reads **2**, not 8:

| tokens | entry | class | why |
|---|---|---|---|
| `sound-change.md`, `tone-prosody.md` | `phonetics-phonology.md:76-77` | **prospective** | line reads "prospective sibling files" |
| `phonology-basics.md`, `naming-and-onomastics.md`, `honorifics-and-register.md` | `language-contact.md:7` | **prospective** | line reads "files to seed" |
| `../linguistics/phonology-sanity.md` ×2 | `label-channel-routing-verification.md:14`, `synthesis/typed-label-routing-workflow.md:16` | **unresolved (real defect)** | path absent; the file is `verification/phonology-sanity-gate.md`, cited on the same line |
| `-gate.md` | `verification/gate-frozen-run-standard.md:15` | **glob-fragment** | inside `corpus/knowledge/verification/*-gate.md`; policy §5.6 forbids counting it |

**Zero phantom attributions remain**: the only tokens the old parsers invented
(`prosody.md`, and `toneprosody.md` under a hyphen-delete heal) are gone under the
soft-wrap heal, and every real token carries a disposition.

**A defect this seat found in its own first draft.** The first alignment leg
(§4 group-alignment of `fallback` tokens) reported **72 false mismatches**. Cause:
the label regex matched the word `synthesis` *inside the filename*
`symbolism-synthesis-method.md`, so a token's "group" was read from a substring of
another token. That is the **same substring-class bug** as C14's over-capture, and
it is exactly the failure a positional match invites. Anchoring the label to a
group boundary (`(?:^|;\s*)`) and matching by span drops the corpus-wide
misalignment count to **0**, while the policy's own population still verifies
(sacred-kingship: 15 fallback, groups 7 linguistics / 6 culture-material /
1 verification / 1 synthesis, **15/15 ok**). Recorded because a false-green
alignment leg would have been worse than no leg.

## 6. Fenced successor instrument (never staged by this seat)

The durable form of the fix: a new, round-owned instrument. It carries the block
parser of §3, the soft-wrap heal, the policy's four classes plus `prospective` and
`glob-fragment`, the group-alignment leg, and the selftest controls claim O
requires. Fenced for the integrator to apply; this seat stages nothing.

```python
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
```

**Selftest run of the exact fenced bytes** (`python3 -B`, scratch copy, read-only;
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed {'sound-change.md': 'prospective', 'sound-symbolism.md': 'fallback', 'tone-prosody.md': 'prospective', 'writing-systems.md': 'fallback'}
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS glob fragment classified                                                          exit=0
```

`--census` run of the same bytes:

```
entries=220 refs=2611 -> direct=2437 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

This instrument is the artifact O03/O04/O05 must reproduce: **`220 / 2611 →
2437 / 166 / 0 / 2 / 5 / 1`** (the `0` is `ambiguous`), with the wrapped field
reading **4/4** and **1/220** blast radius. The dependency-free `--selftest`/
`--census` pair is deliberately read-only so a verifier can run it in a
`git archive` copy without touching filed bytes.

## 7. What this fragment does and does not claim

- **Claimed, with command output above:** the defect is live and reproduced; the
  host is `reports/round-19/audit/entry-audit.py:75` (plus r27's copy); the patch
  is verified by execution against a depth-correct host copy; the selftest is
  green; the wrapped field moves 0→2 resolved with 2 phantoms made visible; the
  blast radius is 1/220; the corrected census is `2611 = 2437+166+0+2+5+1`.
- **Not claimed:** that the fix is *landed* (this seat stages nothing; the
  integrator applies §3 or §6). Not claimed: that `prospective` is adopted policy
  — it is a **drafted** fifth class (`reports/round-39/calib/basename-couples-policy.md`
  is filed and its §2 defines four classes; adding a fifth is a policy successor
  note, O12's scope). Not claimed: any promotion, canon, clearance or closure.
  The r39 policy document itself is filed bytes and is **not** edited here.
- **Deliberate non-actions:** no edit to `reports/round-1..41/**`, `corpus/**`,
  `tools/**`, `tools/gates/frozen/**` or fleet `.ufo/**`; no
  `run-validation.py` executed in-tree; no re-freeze of `declared-in-r7`; no
  packet-surface change; no git, network, or install action.

## Owed

- **Integrator (host decision, the round's call, not this seat's):** land the fix
  as either (a) a new round-owned instrument carrying §6, or (b) the §3 splice
  into a future revision of `reports/round-19/audit/entry-audit.py` **and**
  `reports/round-27/audit/entry-audit.py` (r28 delegates, so it needs none). If
  (b), the splice is a filed-byte change and needs an explicit round owner — the
  §3 diff is supplied so that decision is cheap, not because this seat makes it.
- **Owed to the queue (new row, not in `defect-queue-v2.json`):** the
  `../linguistics/phonology-sanity.md` couples path is a **real dangling
  reference** in two entries (`verification/label-channel-routing-verification.md:14`,
  `synthesis/typed-label-routing-workflow.md:16`) while the existing
  `verification/phonology-sanity-gate.md` is cited on the same lines. That is a
  corpus-byte repair, so it is a drafted corpus leg for the integrator, not a
  seat action. Independently found by O10 §4 (rows 6–7).
- **Owed to the queue:** K01's **D1b** (C14 `fields_of` over-capture) and this
  seat's §5 self-caught **label-substring** defect are the same class of bug; if a
  successor instrument is adopted, the queue should carry one row naming the
  substring-class hazard rather than two.
- **Owed (verify, not this seat):** O04/O05 must reproduce §4's blast radius
  (`1/220`, superset-only) and §6's census from the **landed** artifact. O03
  predicts; this seat's numbers are the prediction's cross-check, not its source.
- **to-verify:** whether the integrator intends r27 to be patched or declared
  superseded. This seat confirmed the *parse site* exists at r27:275 and that r28
  imports r27's core (`:63-68`); it did **not** run r27's instrument against the
  wrapped entry, so r27's end-to-end behaviour is `to-verify` (K01 §Owed carried
  this; it is now narrowed from "does r27 have the parse" — **yes** — to "is r27
  patched or superseded").

## Citations

- **Assignment / claim:** `reports/round-42/targets.json:40-46` (seat O01);
  `reports/round-42/claims.json:13-18` (claim O).
- **Defect site / host:** `reports/round-19/audit/entry-audit.py:31,34-42,74-96`
  (`:75` the single-line capture; `:80-82` findall over the captured line;
  `:87-95` Tier-1 resolution), `:105,118-119,130` (call site, `quality_bar`),
  `:151-182` (selftest; `:168-170` single-line fixture, `:177-181` sources-only
  negative control — no wrapped case); `reports/round-27/audit/entry-audit.py:271,274-286`
  (`COUPLES_TOKEN_RE`, `couples_targets`, single-line capture at `:275`);
  `reports/round-28/audit/entry-audit.py:63-68` (`load_core`, imports r27 by path),
  `:251,264-268` (`couples_unres` print legs). Host sha256 (this seat, `sha256sum`):
  r19 `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`,
  r27 `fb589b28cf4769ac2ce39d820640bb464a93601f4486f54268d31e1c4c06bcda`,
  r28 `918a0c1e5654db6ea5cecaa0b8b1eea6aef37e2f2cf1c74d1a7ec2e0850a3e5c`.
- **Wrapped field bytes:** `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (blank at `:78`, `## ` heading at `:79`); the `prospective sibling files:` phrase
  is on `:76`. Existence of the four targets measured by `ls`/`os.path.isfile`
  (this seat, 2026-10-19).
- **Fix-surface precedents:** `tools/gates/provenance-audit.py:76-77`
  (`FIELD_RE`, `INDENT_RE`), `:244-261` (`field_block`, the correct
  indentation-bounded rule), `:263-265` (`is_empty_value`), `:16-18` (the
  empty-couples reference-not-craft rationale), `:318-324` (couples
  presence/emptiness check); `reports/round-35/cov/C14-audit-6-10.md:199`
  (`FIELD_RE`), `:208-222` (`frontmatter_block`, `## ` terminator), `:225-236`
  (`fields_of`, the over-capture rule), `:249-260` (basename index), `:263-288`
  (`couples_refs`), `:281` (slash-bearing basename key).
- **Policy:** `reports/round-39/calib/basename-couples-policy.md:14-25` (§1
  single-line extractor), `:27-48` (§2 tiers/four classes), `:50-58` (§3
  reporting), `:60-69` (§4 group alignment), `:71-102` (§5 limits, incl. §5.6
  glob fragments), `:104-107` (§6 recipe head; the recipe body is the landed
  draft `reports/round-39/calib/Ca03-basename-policy.md:149-258`, whose Part 2 is
  the 212-entry `2504` run).
- **Ca04 D1:** `reports/round-39/calib/Ca04-verify.md:78-105` (the single-line
  zeroing, 0 vs 4, 2 phantoms, the `prosody.md` `to-verify`), `:114` (the
  `to-verify` full recount).
- **Queue:** `reports/round-40/op/defect-queue-v2.json` rows
  `N6-couples-extractor-wrapped-field` (owner "future resolver round"),
  `r39-basename-successor-instrument` (policy landed verbatim without D1/D2),
  `basename-couples-policy`; origin row `reports/round-37/op/defect-queue.json:202-211`.
- **Peer seats (agreement, read at this cut):** `reports/round-42/scout/K01-n6-scout.md`
  §1 (host), §3 (fix surface), §4 (join rules), §5 (census rows A/B), §7
  (boundaries); `reports/round-42/op/O10-gap-fill.md` §1 (unwrap rule), §4
  (disposition table, the fifth class).
- **Commands (this seat, 2026-10-19, lane root at `ac47c78`, all read-only,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):** (a) single-line vs
  block token capture on the live field → `[]` vs the 4 tokens; (b) corpus-wide
  wrapped-field count → 1/220; (c) four join rules over the field → only the
  soft-wrap heal yields `tone-prosody.md`; (d) brace-expanded token-set diff,
  single-line vs fixed → 1/220 changed, superset-only; (e) census A
  `220/2607→2435/166/0/6` and B `220/2611→2437/166/0/2/5/1`; (f) the fenced
  instrument's `--selftest` → 8/8 PASS, `--census` → the B line; (g) the patched
  host copy's `--selftest` → 8/8 PASS and the wrapped entry → `couples=2
  unresolved=['sound-change.md','tone-prosody.md']` vs the filed instrument's
  `couples=0 unresolved=[]`; (h) sacred-kingship identical before/after
  (`couples=21 unresolved=[15]`, groups 7/6/1/1, alignment 15/15 ok); (i) boundary
  probes on synthetic in-memory fields. No filed byte was edited; no
  `run-validation.py` was executed; no git, network, or install action.
