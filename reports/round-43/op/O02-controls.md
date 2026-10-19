- Seat: O02 | executor | claim O | date 2026-10-19 | baseline 7ceff59

# O02 — selftest controls for the basename-couples resolver (claim O)

Mission (verbatim, `reports/round-43/targets.json:18`): *"Author the selftest
controls: a wrapped-field positive control (the phonetics-phonology field must
read 4/4 named targets), a synthetic phantom (basename matching zero files ->
unresolved), a synthetic ambiguous (basename matching two files -> ambiguous),
and a direct positive. Draft the --selftest leg as a fenced block."*

Deliverable: a drop-in `--selftest` leg, fenced in §2, plus executed red/green
evidence (§4) that the battery discriminates a conformant host from the three
failure shapes the r42 reviews measured: single-line zero-capture, space-join
mangling, and resolve-and-drop. **No filed byte was edited; nothing was staged
under `corpus/`; no `reports/round-*/run-validation.py` was executed; no git,
network or install action was taken.**

## 0. State of the host — the round's `before` is stale on one point

The claim's `before` says "no durable instrument implements the r39
basename-couples policy" (`reports/round-43/claims.json:27`). That is not true
at this baseline: `tools/harness/couples-reference-extractor.py` is committed
(`git log --oneline -- tools/harness/couples-reference-extractor.py` → `7ceff59
round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, …`), its
`--selftest` exits 0 (8 PASS lines, §4(a)), and r42's `validation.json` files
claim O as `"passed": true`. What is genuinely missing for r43's contract is
narrower and is the reason this seat exists:

1. **The r42 selftest has no four-class negative controls.** Its "phantom"
   check asserts the r42 fifth class `prospective` (`couples-reference-extractor.py:268-279`),
   not `unresolved`; it has no synthetic ambiguous case (the live corpus has
   zero duplicate basenames, §4(f)), and no direct positive. The r43 claim binds
   the policy's **four** classes (`direct / fallback / ambiguous / unresolved`,
   `claims.json:28`; policy §2, `reports/round-42/calib/basename-couples-policy-full.md:27-48`).
2. **`classify()` is not index-injectable.** Its r42 signature is
   `classify(ref, entry_dir, prospective=False)`
   (`couples-reference-extractor.py:134`), so the ambiguous branch cannot be
   exercised without touching the live tree. A synthetic two-hit index is the
   only way: the live corpus is 223 entries with 223 distinct basenames and
   **0 duplicates** (measured, §4(f); same finding at
   `reports/round-42/calib/Ca01-gap-fill.md:180-184`).
3. **A wrapped positive that asserts only arity is a false green.** Space-join
   and hyphen-aware join both return 4 tokens on the live field, but only the
   latter returns the intended identities (`reports/round-42/cross/X00-connector.md:89-104`;
   measured again in §4(c)). The control must assert token identity.

So the selftest below is written as a **replacement `selftest()`** for the r43
resolver, not as an addition to the r42 four-check set. It assumes the tool
path the claim names (`tools/harness/basename-couples-resolver.py`) and the
API contract in §3.

## 1. What the controls assert (and why each has teeth)

| # | control | fixture | asserts | failure it catches |
|---|---|---|---|---|
| S1a | fixture-drift guard | live `phonetics-phonology.md:72-77` read at run time | embedded bytes equal live bytes | grading a stale fixture after the entry moves |
| S1b | wrapped positive, identity | the same 6 lines | token set is exactly `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}` | single-line capture (`[]`), space-join (`prosody.md`), de-hyphenation (`toneprosody.md`) — all still "4 tokens" or "0 tokens", never the right four |
| S1c | mangling exclusion | S1b | no `prosody.md`, `toneprosody.md`, `tone- prosody.md` | a fix that mints the phantom it exists to remove |
| S1d | before-state | S1b | the filed single-line capture (`entry-audit.py:75`) yields 0 tokens | a battery that would pass without the defect being live |
| S1e | join-rule negative | S1b | `" ".join(parts)` yields `prosody.md`, never `tone-prosody.md` | the host idiom at `tools/gates/provenance-audit.py:244-260` (space join) |
| S1f | live resolution split | S1b + live index | 2 `direct` (`sound-symbolism.md`, `writing-systems.md`) + 2 `unresolved` (`sound-change.md`, `tone-prosody.md`) | a four-class tool that hides the two absent targets in a fifth class, or resolves them by guess |
| S2a | phantom extraction | synthetic wrapped field, two never-written names | both tokens survive, 2/2 | resolve-and-drop |
| S2b | hyphen-wrapped phantom | `synthetic-` / `phantom-beta.md` | heals to `synthetic-phantom-beta.md`; `phantom-beta.md` absent | continuation join without hyphen rejoin (Trap A/B) |
| S2c | phantom class | empty injected index | both are `unresolved` | classifying a zero-hit token as `prospective`, `fallback`, or nothing |
| S3a–d | synthetic ambiguous | injected index with two hits for one slash-free basename | class `ambiguous`; not guessed to a path; token survives extraction | a resolver that takes `hits[0]` (the C14-as-written shape, policy §5.1) |
| S3e | fallback positive | injected index with exactly one hit | `fallback` + the explicit mapping | a resolver that never exercises Tier 2 |
| S4a–c | direct positive | live `writing-systems.md` in the entry dir; `corpus/knowledge/linguistics/writing-systems.md` | `direct`, no mapping, even with a same-basename hit elsewhere | Tier 1 relaxed to basename lookup (§5.4) |
| S5 | no-drop invariant | all four fixtures | every extracted token gets exactly one of the four classes | silent drops / invented classes |
| S6 | slash gate | `linguistics/hero-journey-variants.md` (unique basename under `myth-symbol/`) | `unresolved` | the C14-as-written re-partitioning (§5.1 delta) |
| S7a–b | field boundary | prose after a blank line; couples as the last header field | only the field's token | C14 `fields_of` over-capture through blank lines (r42 O02 §5) and the queue's literal "next header field" over-read (`X00-connector.md:99-110`) |
| S8 | glob artifact | `-gate.md` with an empty index | `glob-fragment` (or documented artifact/skip), never `unresolved` | counting §5.6 fragments as couples findings |

Every control fails on the leg it is meant to police; §4 shows the green run and
three red runs against deliberately broken hosts.

## 2. The fenced `--selftest` leg (draft — integrator applies)

Paste into `tools/harness/basename-couples-resolver.py`, replacing any earlier
`selftest()`. The block assumes the host already defines the API in §3 and has
`import os, re` at module scope.

````python
# =========================================================================
# --selftest controls (O02, round 43) -- policy's four classes
# =========================================================================
# Required host API (module level):
#   LANE                                  # lane root (str)
#   couples_block(text) -> list[str]      # `- couples:` parts incl. continuations
#   join_parts(parts) -> str              # hyphen-aware soft-wrap repair
#   field_refs(text) -> set[str]          # brace-expanded, per-entry deduped
#   basename_index() -> dict[str, list]   # basename -> corpus-relative paths
#   classify(ref, entry_dir, index=None)  # -> (class, mapping|hits|None)
# `index` MUST be injectable: the synthetic controls never write to the tree.
# Classes: direct | fallback | ambiguous | unresolved, plus `glob-fragment`
# for the §5.6 extractor artifact. r43 claim O binds the four classes; if the
# host retains r42's fifth `prospective` class, S1f fails by design.

LIVE_ENTRY = os.path.join(LANE, "corpus", "knowledge", "linguistics",
                          "phonetics-phonology.md")

# Verbatim bytes of corpus/knowledge/linguistics/phonetics-phonology.md:72-77
# at r43 baseline 7ceff59 (file sha256 b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b).
# S1a fails on drift rather than grading a stale fixture.
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
LIVE_CLASSES = {
    "sound-change.md": "unresolved",
    "tone-prosody.md": "unresolved",
    "sound-symbolism.md": "direct",
    "writing-systems.md": "direct",
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
    ],
}
AMBIG_FIELD = "- couples: shared \u2014 `%s`\n" % AMBIG_REF

UNIQ_REF = "synthetic-uniq-basename.md"
UNIQ_INDEX = {UNIQ_REF: ["corpus/knowledge/linguistics/" + UNIQ_REF]}

DIRECT_REF = "writing-systems.md"  # exists in corpus/knowledge/linguistics/
DIRECT_SHADOW = {DIRECT_REF: ["corpus/knowledge/myth-symbol/" + DIRECT_REF]}
DIRECT_FIELD = "- couples: anchor \u2014 `%s`\n" % DIRECT_REF

MDREF = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
ALLOWED = {"direct", "fallback", "ambiguous", "unresolved"}


def _tokens(text):
    refs = field_refs(text)
    return set(refs) if not isinstance(refs, dict) else set(refs)


def _cls(ref, entry_dir, index):
    try:
        result = classify(ref, entry_dir, index)
    except TypeError:
        return "COULD-NOT-EVALUATE: classify() lacks index=", None
    if isinstance(result, tuple):
        return result[0], (result[1] if len(result) > 1 else None)
    return result, None


def _live_slice(text, n=6):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("- couples:"):
            return "\n".join(lines[i:i + n]) + "\n", i + 1
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

    # S1 -- wrapped-field positive: live bytes, identity, before-state, join rule
    with open(LIVE_ENTRY, encoding="utf-8") as handle:
        live_text = handle.read()
    live_slice, live_line = _live_slice(live_text)
    check("S1a embedded fixture == live bytes at :%s" % live_line,
          live_slice == LIVE_WRAPPED, "live_line=%s" % live_line)

    tokens = _tokens(LIVE_WRAPPED)
    check("S1b wrapped field extracts 4/4 by identity (not arity)",
          tokens == LIVE_TOKENS, sorted(tokens))
    check("S1c no mangled token (prosody.md / toneprosody.md / space split)",
          not ({"prosody.md", "toneprosody.md", "tone- prosody.md"} & tokens),
          sorted(tokens))

    single = re.search(r"^- couples:\s*(.*)$", LIVE_WRAPPED, re.M)
    single_tokens = set(MDREF.findall(single.group(1) if single else ""))
    check("S1d before-state: the filed single-line capture yields 0 tokens",
          single_tokens == set(), sorted(single_tokens))

    parts = couples_block(LIVE_WRAPPED)
    space_tokens = set(MDREF.findall(" ".join(parts)))
    check("S1e space-join is the rejected shape (prosody.md, never tone-prosody.md)",
          "prosody.md" in space_tokens and "tone-prosody.md" not in space_tokens,
          sorted(space_tokens))

    live_index = basename_index()
    entry_dir = os.path.dirname(LIVE_ENTRY)
    live_classes = {t: _cls(t, entry_dir, live_index)[0] for t in sorted(LIVE_TOKENS)}
    check("S1f live field resolves 2 direct + 2 unresolved (four-class policy)",
          live_classes == LIVE_CLASSES, live_classes)

    # S2 -- synthetic phantom: zero index hits -> unresolved, never dropped
    phantom_tokens = _tokens(PHANTOM_FIELD)
    check("S2a phantom tokens survive extraction 2/2",
          phantom_tokens == PHANTOM_TOKENS, sorted(phantom_tokens))
    check("S2b hyphen-wrapped phantom heals to synthetic-phantom-beta.md",
          "phantom-beta.md" not in phantom_tokens
          and "synthetic- phantom-beta.md" not in phantom_tokens,
          sorted(phantom_tokens))
    empty = {}
    phantom_classes = {t: _cls(t, entry_dir, empty)[0] for t in sorted(phantom_tokens)}
    check("S2c zero basename hits -> unresolved (both, not dropped)",
          phantom_classes == {t: "unresolved" for t in PHANTOM_TOKENS},
          phantom_classes)

    # S3 -- synthetic ambiguous, and the fallback positive beside it
    check("S3a synthetic index has exactly two hits",
          len(AMBIG_INDEX[AMBIG_REF]) == 2, AMBIG_INDEX[AMBIG_REF])
    amb_class, amb_map = _cls(AMBIG_REF, entry_dir, AMBIG_INDEX)
    check("S3b two basename hits -> ambiguous", amb_class == "ambiguous", amb_class)
    check("S3c ambiguous is not guessed to one path",
          amb_map is None or sorted(amb_map) == sorted(AMBIG_INDEX[AMBIG_REF]),
          amb_map)
    check("S3d ambiguous token survives extraction",
          _tokens(AMBIG_FIELD) == {AMBIG_REF}, sorted(_tokens(AMBIG_FIELD)))
    uniq_class, uniq_map = _cls(UNIQ_REF, entry_dir, UNIQ_INDEX)
    check("S3e one basename hit -> fallback with its explicit mapping",
          uniq_class == "fallback" and uniq_map == UNIQ_INDEX[UNIQ_REF][0],
          (uniq_class, uniq_map))

    # S4 -- direct positive and the §5.4 never-relax-Tier-1 guard
    direct_class, direct_map = _cls(DIRECT_REF, entry_dir, DIRECT_SHADOW)
    check("S4a Tier-1 direct wins over a same-basename hit elsewhere (§5.4)",
          direct_class == "direct", direct_class)
    check("S4b direct carries no fallback mapping", direct_map is None, direct_map)
    path_class, _ = _cls("corpus/knowledge/linguistics/writing-systems.md",
                         entry_dir, {})
    check("S4c corpus-relative path token -> direct (Tier-1 base 3)",
          path_class == "direct", path_class)

    # S5 -- no-drop invariant: every extracted token gets exactly one class
    fixtures = [
        ("live", LIVE_WRAPPED, live_index),
        ("phantom", PHANTOM_FIELD, empty),
        ("ambiguous", AMBIG_FIELD, AMBIG_INDEX),
        ("direct", DIRECT_FIELD, DIRECT_SHADOW),
    ]
    for label, text, index in fixtures:
        refs = _tokens(text)
        classes = {r: _cls(r, entry_dir, index)[0] for r in sorted(refs)}
        check("S5 no-drop %s: %d/%d tokens classed" % (label, len(classes), len(refs)),
              len(classes) == len(refs) and set(classes.values()) <= ALLOWED,
              classes)

    # S6 -- §5.1: a slash-bearing token never uses the basename fallback
    slash_class, _ = _cls("linguistics/hero-journey-variants.md", entry_dir, live_index)
    check("S6 slash-bearing token stays unresolved despite a unique basename elsewhere",
          slash_class == "unresolved", slash_class)

    # S7 -- field boundary: prose after the field is never a couples token
    boundary = ("- couples: method \u2014 `writing-systems.md`\n\n"
                "Body prose names `sound-symbolism.md`.\n")
    check("S7a body prose after a blank line is excluded",
          _tokens(boundary) == {"writing-systems.md"}, sorted(_tokens(boundary)))
    last_header = ("- topic: fixture\n- couples: `writing-systems.md`\n"
                   "## Section\n\nProse names `sound-symbolism.md`.\n")
    check("S7b couples as the last header field does not swallow the body",
          _tokens(last_header) == {"writing-systems.md"}, sorted(_tokens(last_header)))

    # S8 -- §5.6: a glob fragment is an artifact, not an unresolved finding
    glob_class, _ = _cls("-gate.md", entry_dir, empty)
    check("S8 glob fragment is not an unresolved couples finding (§5.6)",
          glob_class in ("glob-fragment", "artifact", "skipped"), glob_class)

    total = passed + len(failed)
    print("SELFTEST %s: %d/%d controls" % ("OK" if not failed else "FAIL", passed, total))
    if failed:
        print("  failed: " + ", ".join(failed))
    return not failed
````

The block is 25 controls. It writes nothing, opens only the one live entry and
the corpus index, and imports nothing beyond the host's `os`/`re`.

## 3. Interface contract the fence requires

The r42 instrument already exposes four of the six names
(`couples_block`, `join_parts`, `field_refs`, `basename_index`,
`couples-reference-extractor.py:50,76,112,124`). The r43 resolver needs two
changes for the controls to be runnable:

1. **`classify(ref, entry_dir, index=None)`** — an explicit `index` argument,
   defaulting to `basename_index()`. The r42 signature's third position is
   `prospective=False` (`:134`), so passing an index there would be a silent
   type error. This is the only interface change the synthetic ambiguous and
   phantom controls require; it is one default argument, not a redesign.
2. **Four classes on the corpus path.** If the resolver keeps r42's
   `prospective` class (`:148-149`, `O10 §4`), then `resolve_entry()` must not
   use it for the r43 census: the claim's `after_required` is the policy's four
   classes (`claims.json:28`), and S1f pins the two wrapped phantoms as
   `unresolved`. The disposition leg (O06) carries the named reason ("declared
   prospective sibling, never written") without inventing a fifth class. If the
   round instead wants the fifth class, the claim text must change; the selftest
   cannot be made green both ways.

`selftest()` returns a bool; `main()` should map it to exit 0/1 exactly as the
r42 tool does (`couples-reference-extractor.py:304-305`).

## 4. Executed evidence

All runs 2026-10-19, lane root, HEAD `7ceff59`, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, read-only. The §2
fence was extracted from this file by
`re.search(r"````python\n(.*?)\n````", md, re.S)` and executed in memory
against each host; **no host file was written or edited**. The extracted fence
is 209 lines, sha256
`3637fd46b89583ae67b69af7519742927f2b8b0d7aa7f0de482b04582a47a039`.

**(a) Green: the battery on a conformant four-class host.** The reference host
implements the §3 API exactly (`couples_block` with blank/field/indent
terminators, hyphen-aware `join_parts`, no-drop `field_refs`, one-level
`basename_index`, `classify(ref, entry_dir, index=None)` with the four classes
plus `glob-fragment`).

```
$ python3 - <<'PY'   # host + extracted §2 fence + selftest()
...
SELFTEST OK: 25/25 controls
EXIT 0
```

The 25 PASS lines are the 21 checks in §1 plus the four per-fixture S5 legs
(`live`, `phantom`, `ambiguous`, `direct`); the transcript is reproduced in
full below because this is the claim's green evidence:

```
PASS S1a embedded fixture == live bytes at :72
PASS S1b wrapped field extracts 4/4 by identity (not arity)
PASS S1c no mangled token (prosody.md / toneprosody.md / space split)
PASS S1d before-state: the filed single-line capture yields 0 tokens
PASS S1e space-join is the rejected shape (prosody.md, never tone-prosody.md)
PASS S1f live field resolves 2 direct + 2 unresolved (four-class policy)
PASS S2a phantom tokens survive extraction 2/2
PASS S2b hyphen-wrapped phantom heals to synthetic-phantom-beta.md
PASS S2c zero basename hits -> unresolved (both, not dropped)
PASS S3a synthetic index has exactly two hits
PASS S3b two basename hits -> ambiguous
PASS S3c ambiguous is not guessed to one path
PASS S3d ambiguous token survives extraction
PASS S3e one basename hit -> fallback with its explicit mapping
PASS S4a Tier-1 direct wins over a same-basename hit elsewhere (§5.4)
PASS S4b direct carries no fallback mapping
PASS S4c corpus-relative path token -> direct (Tier-1 base 3)
PASS S5 no-drop live: 4/4 tokens classed
PASS S5 no-drop phantom: 2/2 tokens classed
PASS S5 no-drop ambiguous: 1/1 tokens classed
PASS S5 no-drop direct: 1/1 tokens classed
PASS S6 slash-bearing token stays unresolved despite a unique basename elsewhere
PASS S7a body prose after a blank line is excluded
PASS S7b couples as the last header field does not swallow the body
PASS S8 glob fragment is not an unresolved couples finding (§5.6)
SELFTEST OK: 25/25 controls
```

**(b) Red: the battery has teeth.** Three deliberately broken hosts, differing
from the reference only in the named function; the fence is byte-identical.

| host | result | failed controls | what it proves |
|---|---|---|---|
| A single-line `field_refs` (the filed r19/r39 shape) | **22/25, exit 1** | S1b, S2a, S2c | the wrapped field reads `[]` and the continuation-wrapped phantom is dropped |
| B `" ".join(parts)` (`provenance-audit.py` idiom) | **20/25, exit 1** | S1b, S1c, S2a, S2b, S2c | 4 tokens but the wrong 4 (`prosody.md`); an arity-only positive would be a false green |
| C resolve-and-drop `field_refs` | **19/25, exit 1** | S1b, S2a, S2c, S3d, S7a, S7b | tokens that resolve nowhere vanish; boundary and ambiguous survivals fail |

The failed lines, verbatim (details elided only where the transcript repeats
the PASS list):

```
=== BROKEN-A single-line field_refs ===
FAIL S1b wrapped field extracts 4/4 by identity (not arity)  [[]]
FAIL S2a phantom tokens survive extraction 2/2  [['synthetic-phantom-alpha.md']]
FAIL S2c zero basename hits -> unresolved (both, not dropped)  [{'synthetic-phantom-alpha.md': 'unresolved'}]
SELFTEST FAIL: 22/25 controls
EXIT 1

=== BROKEN-B space-join ===
FAIL S1b wrapped field extracts 4/4 by identity (not arity)  [['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']]
FAIL S1c no mangled token (prosody.md / toneprosody.md / space split)  [['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']]
FAIL S2a phantom tokens survive extraction 2/2  [['phantom-beta.md', 'synthetic-phantom-alpha.md']]
FAIL S2b hyphen-wrapped phantom heals to synthetic-phantom-beta.md  [['phantom-beta.md', 'synthetic-phantom-alpha.md']]
FAIL S2c zero basename hits -> unresolved (both, not dropped)  [{'phantom-beta.md': 'unresolved', 'synthetic-phantom-alpha.md': 'unresolved'}]
SELFTEST FAIL: 20/25 controls
EXIT 1

=== BROKEN-C resolve-and-drop ===
FAIL S1b wrapped field extracts 4/4 by identity (not arity)  [[]]
FAIL S2a phantom tokens survive extraction 2/2  [[]]
FAIL S2c zero basename hits -> unresolved (both, not dropped)  [{}]
FAIL S3d ambiguous token survives extraction  [[]]
FAIL S7a body prose after a blank line is excluded  [[]]
FAIL S7b couples as the last header field does not swallow the body  [[]]
SELFTEST FAIL: 19/25 controls
EXIT 1
```

**(c) Red: the r42 host as filed, exec'd in memory (file untouched).** This is
the interface finding, not a defect against r42. The host is
`tools/harness/couples-reference-extractor.py`; the fence is exec'd into its
module dict only.

```
=== D r42 host as filed (classify lacks index=, retains prospective) ===
FAIL S1f live field resolves 2 direct + 2 unresolved (four-class policy)  [{'sound-change.md': 'prospective', 'sound-symbolism.md': 'direct', 'tone-prosody.md': 'prospective', 'writing-systems.md': 'direct'}]
FAIL S3b two basename hits -> ambiguous  [prospective]
FAIL S3e one basename hit -> fallback with its explicit mapping  [('prospective', None)]
FAIL S5 no-drop live: 4/4 tokens classed  [{'sound-change.md': 'prospective', 'sound-symbolism.md': 'direct', 'tone-prosody.md': 'prospective', 'writing-systems.md': 'direct'}]
FAIL S5 no-drop ambiguous: 1/1 tokens classed  [{'synthetic-dup-basename.md': 'prospective'}]
SELFTEST FAIL: 20/25 controls
EXIT 1
```

Two distinct causes, both intended:

- **S1f / S5-live** — the host's fifth `prospective` class
  (`couples-reference-extractor.py:146-149`) classifies the two wrapped
  phantoms as `prospective`, not the four-class `unresolved`. r43's claim binds
  four classes.
- **S3b / S3e / S5-ambiguous** — the host's signature is
  `classify(ref, entry_dir, prospective=False)` (`:134`). The fence's third
  positional argument (the injected index) is truthy, so it is consumed as
  `prospective`; the real index lookup is ignored, yielding `prospective` for
  both synthetic cases. S2c passes on this host only because its injected
  index is the empty dict, which is falsy — an artifact of the signature
  collision, not a semantic pass. The injectable `index=` is therefore
  required, not cosmetic.

**(d) The r42 host's own selftest is green but does not meet r43's threshold.**
Filed bytes, unmodified:

```
$ python3 -B tools/harness/couples-reference-extractor.py --selftest | tail -3
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS glob fragment classified
# rc=0 (8/8 PASS lines in full)
```

Missing from that set: the four-class phantom (its phantom check asserts
`prospective`, `:268-279`), the synthetic ambiguous, the direct positive, the
§5.4 guard, the slash gate, and the field-boundary controls.

**(e) Live census baseline for O03/O10 (measured, not predicted).** Using the
r42 host's own resolution over `corpus/knowledge/*/*.md` at 223 entries:

```
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  four-class fold: direct=2556 fallback=166 ambiguous=0 unresolved=7
  four-class total = 2729; glob-fragment artifact = 1 (2729 + 1 = 2730)
  prospective rows (5):
    language-contact.md: honorifics-and-register.md, naming-and-onomastics.md, phonology-basics.md
    phonetics-phonology.md: sound-change.md, tone-prosody.md
  unresolved rows (2, one distinct token):
    ../linguistics/phonology-sanity.md <- synthesis/typed-label-routing-workflow.md
    ../linguistics/phonology-sanity.md <- verification/label-channel-routing-verification.md
  glob-fragment row (1): -gate.md <- verification/gate-frozen-run-standard.md
```

This is the r42 instrument's classification, not the r43 resolver's; O03 owns
the predicted census and O10 the filed artifact. It is recorded here because
S1f pins exactly the two `phonetics-phonology.md` rows as `unresolved` under
the four-class contract, and the fold changes the unresolved total from 2 to 7.

**(f) Ambiguous has no live instance; the synthetic control is mandatory.**
`glob.glob("corpus/knowledge/*/*.md")` → 223 entries, `Counter(basename)` → 223
distinct basenames, `dups=[]`. Policy §2's "two or more → ambiguous" branch and
§5.5's re-adjudication trigger are unexercised at this tree, so S3 is the only
way to test the branch (same conclusion as
`reports/round-42/calib/Ca01-gap-fill.md:180-184`).

**(g) Hygiene.** `git status --porcelain` → `?? reports/round-43/` only;
`git diff --stat` → empty (no tracked byte changed); live entry sha256
`b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b` equals the
constant embedded in S1a; no `reports/round-*/run-validation.py` was executed;
nothing was staged under `corpus/`.

## 5. Findings and owed

1. **The four-class vs fifth-class choice is load-bearing and cannot be left
   implicit.** At the live tree the r42 class split is `2 unresolved + 5
   prospective`; folding `prospective` into `unresolved` gives `7 unresolved`
   and a four-class total of `2729` (plus 1 glob artifact). If the r43 resolver
   keeps the fifth class, S1f fails and the claim's "classifies every corpus
   token into the policy's four classes" is not met as written. If it folds,
   O06's disposition leg must name the reason for all five rows (three
   never-written seeds at `language-contact.md:7`, two declared prospective
   siblings at `phonetics-phonology.md:72-77`). Owner: O01 (tool) + O06
   (disposition) + O10 (census artifact); flagged to O08/R01.
2. **The r42 `--selftest` is green but insufficient for r43.** It lacks the
   four-class phantom/ambiguous/direct legs (§4(d)). This is not a defect
   against r42's claim; it is why r43 needs the replacement leg above.
3. **`classify(ref, entry_dir, index=None)` is required.** Without it the
   synthetic ambiguous/fallback controls cannot run without writing fixtures
   under the live tree (§4(c)). One default argument; the reference host in
   §4(a) is the existence proof.
4. **The claim's `before` overstates one point, and the round should record
   the narrower gap.** A durable instrument *does* exist at
   `tools/harness/couples-reference-extractor.py` (committed `7ceff59`), it
   *does* implement block extraction and hyphen-aware wrap repair
   (`:50-73,76-92`), and r42's `validation.json` files O as passed. What is
   missing for r43 is the four-class disposition/census contract, the
   index-injectable `classify`, and the filed corrected census. The r39
   *policy document* still states "single physical line" (§1), so the claim's
   sentence is true of the policy landing and false of the code at HEAD; the
   distinction should survive into the round's integration note.
5. **The two phantom targets are self-documented, not broken references.**
   The field opens the clause with `prospective sibling files:`, which is the
   C12 row-2 "documented" condition (`reports/round-35/cov/C12-audit-runbook.md:37`).
   Their class is still `unresolved` under the four-class policy; the
   disposition reason is "declared prospective sibling, never written". S1f
   and S2c keep that visible rather than letting a fifth class hide it.
6. **The fixture is drift-guarded, but the class expectation is a live-corpus
   fact.** S1a fails if the field's bytes move; S1f fails if `sound-change.md`
   or `tone-prosody.md` is ever written (or one of the two existing targets is
   removed). That is intended: update the control with the new corpus evidence,
   never loosen it silently.
7. **Owed to the integrator:** apply the §2 fence to the O01 tool, add the
   `index=` argument, run `python3 tools/harness/basename-couples-resolver.py
   --selftest` (exit 0, 25/25) and `--census`, and have O04/O05 re-run the
   fence independently. This seat confirms the controls discriminate; it does
   not claim the not-yet-authored tool is green.
8. **`tone-prosody.md` intent stays `to-verify`, though the evidence agrees.**
   Line 76 ends `tone-` and line 77 opens `prosody.md`; the same entry's `:279`
   prose names `tone-prosody.md` as a natural partner. The control encodes the
   hyphen-aware reading. If authorial intent were `prosody.md`, the control
   must be revised with evidence, never loosened silently (carried from
   `reports/round-42/op/O02-controls.md` §6).

## Citations

- Assignment: `reports/round-43/targets.json:18` (seat `O02`, out
  `op/O02-controls.md`); claim O: `reports/round-43/claims.json:24-35`.
- Policy (full successor doc): `reports/round-42/calib/basename-couples-policy-full.md`
  §1 `:14-25`, §2 `:27-48` (four classes at `:36-48`), §3 `:50-58`, §4
  `:60-69`, §5 `:71-102` (§5.1 slash gate `:73-81`, §5.4 Tier-1 never relaxed
  `:89-92`, §5.5 index scope `:93-96`, §5.6 glob fragments `:97-102`), §6
  recipe `:104-218`.
- Filed extractor defects: `reports/round-19/audit/entry-audit.py:31,34-42,75`;
  `reports/round-39/calib/Ca04-verify.md:78-93` (D1), `:114-115` (owed recount);
  `reports/round-35/cov/C14-audit-6-10.md:223-236` (`fields_of`), `:281`
  (slash-bearing basename key).
- r42 durable host: `tools/harness/couples-reference-extractor.py:50-73`
  (`couples_block`), `:76-92` (`join_parts`), `:112-118` (`field_refs`),
  `:124-131` (`basename_index`), `:134-150` (`classify`), `:242-295`
  (`selftest`), `:304-305` (exit mapping).
- r42 review traps the controls encode:
  `reports/round-42/review/R02-review.md:40-58` (Trap A de-hyphenation, Trap B
  space-join false green), `reports/round-42/cross/X00-connector.md:89-104`
  (identity not arity), `reports/round-42/cross/X01-trades.md:95-120`
  (hyphen-wrapped positive required).
- Live wrapped bytes: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`;
  corroborating prose naming the same four partners at `:279`; file sha256
  `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`.
- Duplicate-basename fact: `reports/round-42/calib/Ca01-gap-fill.md:180-184`;
  measured again at 223 entries in §4(f).
- Command outputs: §4(a)-(f) below (this seat, 2026-10-19, lane root, HEAD
  `7ceff59`, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all
  read-only). The fenced bytes in §2 are the bytes executed in §4(a); the
  extraction command is stated there so the transcript is reproducible.
