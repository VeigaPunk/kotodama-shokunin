- Seat: O02 | executor | claim O | date 2026-10-19 | baseline ac47c78

# O02 — selftest controls for the N6 couples-extractor block parser (claim O)

Mission (verbatim, `reports/round-42/targets.json` seat `O02`): *"Selftest controls
(fenced): wrapped-field positive (4/4 targets), synthetic phantom negative,
unwrapped regression."*

Deliverable: one self-contained, dependency-free selftest battery for the fixed
`- couples:` extractor, fenced below, plus the executed red/green evidence that
the battery discriminates a fixed host from the filed one. No filed byte was
edited; nothing was staged under `corpus/`; no `run-validation.py` was executed;
no git, network or install action was taken.

## 1. What the controls assert (and why each has teeth)

The battery is a single function, `check(extract, label)`, run against any
instrument exposing `couples_field` / `couples_tokens` / `couples_refs` /
`couples_targets` (one-arg, or two-arg `(text, path)`). Four fixtures, each with
a `must_contain` and a `must_not_contain` set — a control fails on either leg.

| # | control | fixture | asserts | why it can fail |
|---|---|---|---|---|
| 1 | `wrapped-field-positive` | the live field's bytes, `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, verbatim | `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}` present; `{prosody.md, toneprosody.md, "tone- prosody.md"}` absent | the filed single-line host captures `[]`; a naive space-join captures `prosody.md`; a de-hyphenation that eats the hyphen captures `toneprosody.md` |
| 2 | `synthetic-phantom-negative` | hand-written wrapped field naming two files that exist nowhere (`linguistics/no-such-entry-anywhere.md` split across the break, `linguistics/absent-second-phantom.md`) | both phantoms present as tokens; body-prose `.md` name absent | a parser that resolves-and-drops instead of tokenizing loses them; an unbounded parser pulls in body prose |
| 3 | `unwrapped-regression` | a single-line field | its token set is exactly the two backticked names | a block parser that mishandles the 219-of-220 unwrapped shape regresses |
| 4 | `field-boundary-negative` | single-line field, blank line, body prose naming three `.md` files | only the field's token; all three prose names absent | C14's `fields_of` shape over-captures here (control 7 below) |

Three further controls guard the battery itself, so a green run cannot be
vacuous: **5** `before-state-zero-capture` (the filed single-line reading of
fixture 1 must really be `[]` — i.e. the N6 defect is live, not described);
**6** `naive-join-is-broken` (a join that does not repair the soft wrap must
really emit `prosody.md` and must not emit `tone-prosody.md`); **7**
`fixture-bytes-are-live-bytes` (the embedded wrapped bytes must equal the live
`:72-77` bytes, so control 1 cannot drift away from the corpus it grades).

## 2. The fenced selftest (draft — integrator applies)

Suggested durable home (the round's non-goals bar editing filed bytes, and
`tools/` carries no couples resolver): `tools/harness/check-couples-extraction.py`,
with the fixed instrument at the host O01/K01 confirm. Written here as bytes
only; this seat installed nothing.

````python
#!/usr/bin/env python3
"""O02 couples-extractor selftest controls (round 42, claim O / N6).

Self-contained. Read-only, stdlib only, no writes, no network, no git.

  python3 o02-selftest.py --selftest              # reference extractor
  python3 o02-selftest.py --against <instrument>  # a landed instrument
  python3 o02-selftest.py --live <corpus-root>    # corpus census, read-only

Exit 0 = all controls hold; 1 = a control failed; 2 = could-not-evaluate.
The landed instrument must expose one of: couples_field / couples_tokens /
couples_refs / couples_targets (one-arg, or two-arg (text, path)).
"""
import glob
import importlib.util
import os
import re
import sys

MDREF = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
BRACE = re.compile(r"\{([^{}]*)\}")
FIELD_RE = re.compile(r"^- ([a-z-]+):", re.M)
SINGLE_RE = re.compile(r"^- couples:\s*(.*)$", re.M)


def expand_braces(s):
    m = BRACE.search(s)
    if not m:
        return [s]
    out = []
    for part in m.group(1).split(","):
        out.extend(expand_braces(s[: m.start()] + part + s[m.end():]))
    return out


def tokens_of(field):
    out = set()
    if not field:
        return out
    for raw in MDREF.findall(field):
        for c in expand_braces(raw):
            out.add(c.strip())
    return out


def block_field_raw(text):
    """The raw newline-joined block, before soft-wrap repair (wrappedness test)."""
    lines = text.splitlines()
    start = None
    for i, l in enumerate(lines):
        if l.startswith("- couples:"):
            start = i
            break
    if start is None:
        return ""
    parts = [lines[start].split(":", 1)[1].strip()]
    for l in lines[start + 1:]:
        if not l.strip() or l.startswith("## ") or FIELD_RE.match(l):
            break
        parts.append(l.strip())
    return "\n".join(parts)


def reference_couples_field(text):
    """The fix: the `- couples:` value runs through its continuation lines until
    a blank line, the next `- key:` field, or a `## ` heading; a trailing hyphen
    at a line break is the word's own hyphen, so the join keeps it."""
    j = block_field_raw(text)
    return re.sub(r"(?<=-)\n(?=[A-Za-z0-9_])", "", j).replace("\n", " ")


def naive_block_field(text):
    """A block read that does NOT repair the soft wrap - the rejected shape."""
    return reference_couples_field(text).replace("tone-prosody.md", "tone- prosody.md")


def single_line_field(text):
    """The filed r19/r27 host (reports/round-19/audit/entry-audit.py:75)."""
    m = SINGLE_RE.search(text)
    return None if m is None else m.group(1)


HEADER = (
    "# Fixture entry\n"
    "\n"
    "- topic: fixture.\n"
    "- sources:\n"
    "  - KTD-FX-S-0001 - placeholder locator bullet.\n"
    "- verified-at: 2026-10-17 - placeholder.\n"
    "- recheck: on a source change.\n"
)

# Verbatim continuation lines of corpus/knowledge/linguistics/phonetics-phonology.md:72-77
# (sha256 of that file at ac47c78: b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b).
WRAPPED = (
    "- couples: language (this file, core method); myth (divine/true names, taboo\n"
    "  naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,\n"
    "  bouba/kiki iconography); era (Neolithic bite \u2192 f/v, sound-change dating of\n"
    "  strata); costume (masks/mouthgear vs articulation, whistle & drum channels);\n"
    "  environment/anatomy design; prospective sibling files: sound-change.md, tone-\n"
    "  prosody.md, sound-symbolism.md, writing-systems.md\n"
)

UNWRAPPED = (
    "- couples: method \u2014 `linguistics/phonetics-phonology.md`; boundary \u2014"
    " `linguistics/writing-systems.md`; never canon.\n"
)

PHANTOM = (
    "- couples: sibling \u2014 `linguistics/writing-systems.md`; seed \u2014 `linguistics/no-such-\n"
    "  entry-anywhere.md`; also `linguistics/absent-second-phantom.md`; never canon.\n"
)

BOUNDARY = (
    "- couples: method \u2014 `linguistics/phonetics-phonology.md`; never canon.\n"
    "\n"
    "Natural partners: `linguistics/body-prose-only.md` (diachrony),"
    " `linguistics/another-prose-name.md`.\n"
)

# name, text, must_contain, must_not_contain
FIXTURES = [
    ("wrapped-field-positive", HEADER + WRAPPED,
     {"sound-change.md", "tone-prosody.md", "sound-symbolism.md", "writing-systems.md"},
     {"prosody.md", "toneprosody.md", "tone- prosody.md"}),
    ("synthetic-phantom-negative", HEADER + PHANTOM,
     {"linguistics/no-such-entry-anywhere.md", "linguistics/absent-second-phantom.md"},
     {"linguistics/body-prose-only.md"}),
    ("unwrapped-regression", HEADER + UNWRAPPED,
     {"linguistics/phonetics-phonology.md", "linguistics/writing-systems.md"},
     {"linguistics/body-prose-only.md"}),
    ("field-boundary-negative", HEADER + BOUNDARY,
     {"linguistics/phonetics-phonology.md"},
     {"linguistics/body-prose-only.md", "linguistics/another-prose-name.md"}),
]


def check(extract, label):
    bad = []
    for name, text, must, mustnot in FIXTURES:
        try:
            raw = extract(text)
        except TypeError:
            raw = extract(text, "")
        if isinstance(raw, tuple):
            raw = [t for part in raw for t in part]
        got = tokens_of(raw) if isinstance(raw, str) else {t for t in raw if isinstance(t, str)}
        missing, extra = sorted(must - got), sorted(mustnot & got)
        ok = not missing and not extra
        print("  %-28s %s  tokens=%s" % (name, "OK" if ok else "FAIL", sorted(got)))
        if not ok:
            print("      missing=%s forbidden=%s" % (missing, extra))
            bad.append(name)
    print("%s: %d/%d controls hold" % (label, len(FIXTURES) - len(bad), len(FIXTURES)))
    return 1 if bad else 0


def selftest():
    rc = check(reference_couples_field, "SELFTEST")
    # the before-state is a real zero-capture (the defect is live)
    before = tokens_of(single_line_field(HEADER + WRAPPED))
    print("  %-28s %s  single-line capture=%s" % (
        "before-state-zero-capture", "OK" if not before else "FAIL", sorted(before)))
    rc |= 1 if before else 0
    # the naive join is rejected: it yields the phantom prosody.md
    naive = tokens_of(naive_block_field(HEADER + WRAPPED))
    ok = "prosody.md" in naive and "tone-prosody.md" not in naive
    print("  %-28s %s  naive-join capture=%s" % (
        "naive-join-is-broken", "OK" if ok else "FAIL", sorted(naive)))
    rc |= 0 if ok else 1
    # fixture fidelity: embedded bytes are the live bytes
    live = "corpus/knowledge/linguistics/phonetics-phonology.md"
    if os.path.isfile(live):
        blob = "\n".join(open(live, encoding="utf-8").read().splitlines()[71:77]) + "\n"
        ok = blob == WRAPPED
        print("  %-28s %s" % ("fixture-bytes-are-live-bytes", "OK" if ok else "FAIL"))
        rc |= 0 if ok else 1
    if rc:
        print("SELFTEST FAIL")
    else:
        print("SELFTEST OK %d/%d controls" % (len(FIXTURES) + 3, len(FIXTURES) + 3))
    return rc


def against(path):
    spec = importlib.util.spec_from_file_location("landed", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    getter = next((getattr(mod, a) for a in
                   ("couples_field", "couples_tokens", "couples_refs", "couples_targets")
                   if hasattr(mod, a)), None)
    if getter is None:
        print("COULD-NOT-EVALUATE: %s exposes no couples extractor" % path, file=sys.stderr)
        return 2
    return check(getter, "AGAINST %s" % path)


def live(root):
    files = sorted(glob.glob(os.path.join(root, "*", "*.md")))
    if not files:
        print("COULD-NOT-EVALUATE: no entries under %s" % root, file=sys.stderr)
        return 2
    wrapped, delta, n_s, n_f = [], [], 0, 0
    for p in files:
        text = open(p, encoding="utf-8").read()
        s = single_line_field(text)
        if s is None:
            continue
        f = reference_couples_field(text)
        n_s += len(tokens_of(s))
        n_f += len(tokens_of(f))
        if "\n" in block_field_raw(text):
            wrapped.append(os.path.relpath(p, root))
        if tokens_of(s) != tokens_of(f):
            delta.append((os.path.relpath(p, root), sorted(tokens_of(s)), sorted(tokens_of(f))))
    print("entries=%d  wrapped=%d  single-line tokens=%d  fixed tokens=%d  delta=%+d"
          % (len(files), len(wrapped), n_s, n_f, n_f - n_s))
    for w in wrapped:
        print("   wrapped: %s" % w)
    for d in delta:
        print("   delta: %s\n     single=%s\n     fixed =%s" % d)
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--against" in argv:
        return against(argv[argv.index("--against") + 1])
    if "--live" in argv:
        i = argv.index("--live")
        return live(argv[i + 1] if len(argv) > i + 1 else "corpus/knowledge")
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
````

## 3. Executed evidence (this seat, 2026-10-19, lane root, HEAD `ac47c78`)

All runs read-only under `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
Every output in (a)–(e) below was produced by the fenced draft itself: the fence
was extracted from this file to `.scratch/o02/o02-selftest.py` and executed
(sha256 `83d0d5cf686cda7a6238a465a9609cd35d5ef070b7424c643b984df453b89e8c`,
238 lines; scratch is gitignored). Re-extracting the fence reproduces that digest,
so the quoted transcript belongs to the shipped bytes.

**(a) The battery is green on the reference extractor.**

```
$ python3 -B .scratch/o02/o02-selftest.py --selftest
  wrapped-field-positive       OK  tokens=['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
  synthetic-phantom-negative   OK  tokens=['linguistics/absent-second-phantom.md', 'linguistics/no-such-entry-anywhere.md', 'linguistics/writing-systems.md']
  unwrapped-regression         OK  tokens=['linguistics/phonetics-phonology.md', 'linguistics/writing-systems.md']
  field-boundary-negative      OK  tokens=['linguistics/phonetics-phonology.md']
SELFTEST: 4/4 controls hold
  before-state-zero-capture    OK  single-line capture=[]
  naive-join-is-broken         OK  naive-join capture=['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']
  fixture-bytes-are-live-bytes OK
SELFTEST OK 7/7 controls          # rc=0
```

**(b) The battery has teeth — it red-flags the filed host and greens a patched one.**
A patched copy of the filed r19 instrument (single-line `re.search` at `:75` replaced
by a bounded block read; written to `.scratch/o02/landed/entry-audit-fixed.py`,
filed bytes untouched) is the only difference between these two runs:

```
$ python3 -B .scratch/o02/o02-selftest.py --against reports/round-19/audit/entry-audit.py
  wrapped-field-positive       FAIL  tokens=[]
      missing=['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md'] forbidden=[]
  synthetic-phantom-negative   FAIL  tokens=['linguistics/writing-systems.md']
      missing=['linguistics/absent-second-phantom.md', 'linguistics/no-such-entry-anywhere.md'] forbidden=[]
  unwrapped-regression         OK  tokens=['linguistics/phonetics-phonology.md', 'linguistics/writing-systems.md']
  field-boundary-negative      OK  tokens=['linguistics/phonetics-phonology.md']
AGAINST reports/round-19/audit/entry-audit.py: 2/4 controls hold          # rc=1

$ python3 -B .scratch/o02/o02-selftest.py --against .scratch/o02/landed/entry-audit-fixed.py
  wrapped-field-positive       OK  tokens=['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
  synthetic-phantom-negative   OK  tokens=['linguistics/absent-second-phantom.md', 'linguistics/no-such-entry-anywhere.md', 'linguistics/writing-systems.md']
  unwrapped-regression         OK  tokens=['linguistics/phonetics-phonology.md', 'linguistics/writing-systems.md']
  field-boundary-negative      OK  tokens=['linguistics/phonetics-phonology.md']
AGAINST .scratch/o02/landed/entry-audit-fixed.py: 4/4 controls hold       # rc=0
```

**(c) Live-corpus before→after through the instrument (the N6 before-state, and
the corrected reading).** Both hosts run unmodified/fixed against the same live entry:

```
$ python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md
FAIL corpus/knowledge/linguistics/phonetics-phonology.md src=15/15 couples=0 unresolved=[] gap=False dec=True
TOTAL 0/1 clear the bar            # rc=2 — couples=0: the wrapped field is silently zeroed

$ python3 -B .scratch/o02/landed/entry-audit-fixed.py corpus/knowledge/linguistics/phonetics-phonology.md
FAIL corpus/knowledge/linguistics/phonetics-phonology.md src=15/15 couples=2 unresolved=['sound-change.md', 'tone-prosody.md'] gap=False dec=True
TOTAL 0/1 clear the bar            # rc=2 — couples=2 (the two that exist); 2 named-and-absent surfaced as unresolved, not dropped
```

The overall `FAIL`/`rc=2` is unchanged and is **not** this claim's subject: the
entry fails the r19 instrument's `gap_named` leg, which the block parser does not
touch. The couples leg moves `0 → 2 resolved + 2 unresolved`, which is the claim.

**(d) The corrected corpus census (read-only, synthetic re-parse).**

```
$ python3 -B .scratch/o02/o02-selftest.py --live corpus/knowledge
entries=220  wrapped=1  single-line tokens=2607  fixed tokens=2611  delta=+4
   wrapped: linguistics/phonetics-phonology.md
   delta: linguistics/phonetics-phonology.md
     single=[]
     fixed =['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
```

Unit note (the r39 `2504` is **not** this number and must not be conflated with
it): `2607/2611` are raw per-file deduplicated token counts over 220 files; the
r39 policy's `2504 = 2335 + 163 + 0 + 6` is refs after brace expansion, per-entry
dedup and the two-tier resolution, measured at 212 entries
(`reports/round-39/calib/Ca03-basename-policy.md:35-36,268`). The denominator
itself moved (212 → 220), so the successor census is a re-run at 220, not
"2504 minus 2 phantoms". O03 owns the predicted census; this row is the
extractor delta the controls bound.

**(e) Invariants.** `git status --porcelain` → `?? reports/round-42/` only; HEAD
`ac47c78`. Digests before/after this seat's work, unchanged:
`reports/round-19/audit/entry-audit.py` `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`;
`reports/round-35/cov/C14-audit-6-10.md` `bf402bc6ebeeb6744e231065f83c2c2f0d2c2f7108a950ad9e2d13221dd309cb`;
`reports/round-39/calib/basename-couples-policy.md` `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`;
`corpus/knowledge/linguistics/phonetics-phonology.md` `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`.
No `reports/round-*/run-validation.py` was executed.

## 4. Fix contract the controls imply (for O01 / the landed host)

1. **Bounded block read.** The `- couples:` value spans its continuation lines
   and ends at the first blank line, the next `- [a-z-]+:` field, or a `## `
   heading. A `## `-only terminator is not enough: it over-captures through blank
   lines (control 7 below).
2. **Soft-wrap repair that keeps the hyphen.** When a continuation begins
   immediately after a line ending in `-`, the join keeps that hyphen and removes
   only the newline and the continuation indent: `tone-` + `prosody.md` →
   `tone-prosody.md`. Measured on the live field, all three other behaviours are
   wrong:

   | join | tokens on `phonetics-phonology.md:72-77` |
   |---|---|
   | single-line (filed r19/r27) | `[]` |
   | block, newline → space, no repair (C14 `fields_of` shape) | `[prosody.md, sound-change.md, sound-symbolism.md, writing-systems.md]` |
   | block, repair that *deletes* the hyphen | `[toneprosody.md, sound-change.md, sound-symbolism.md, writing-systems.md]` |
   | block, repair that keeps it (required) | `[sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md]` |

3. **Tokenize, then resolve — never resolve-and-drop.** A token that resolves
   nowhere must survive as `unresolved` (control 2); the filed host drops the
   wrapped phantoms entirely because it never sees them.
4. **Report the resolution class beside the count.** The corrected reading of the
   live entry is `couples=2 unresolved=['sound-change.md','tone-prosody.md']`;
   `2/2` is the claim's threshold, and `sound-change.md` / `tone-prosody.md` are
   the r39 Ca04 D1 phantoms, now surfaced rather than hidden.

## 5. Third defect class found (new — not in the r39 D1 row)

`reports/round-35/cov/C14-audit-6-10.md:223-236` `fields_of()` terminates a field
only on the next `- [a-z-]+:` line or `## ` heading — **blank lines are ignored**,
so continuation capture runs through them. Live instance:
`corpus/knowledge/linguistics/conlang-methodology.md` has a *single-line*
`- couples:` at `:7` followed by a blank line at `:8` and body prose at `:9`;
C14's shape reads the couples value as **2 lines**, the second being that prose
(executed: `couples n=2`, second value line
`"Attested artlangs are old — Hildegard of Bingen's 12th-c. Lingua Ignota is …"`).
This does not change that file's `.md` token set (the prose carries no `.md`
token), which is why the single-line-vs-block census in (d) shows a delta on the
wrapped file only — but any entry whose body prose names a `.md` file would
inflate its couples population. Control 4 (`field-boundary-negative`) is the
regression guard; control 7 of the harness form asserts the over-capture is real.
Recorded as a finding for the successor instrument; the r39 policy §1 ("single
physical line", `basename-couples-policy.md:22-24`) is the documented root of
both this and the wrapped-field zeroing.

## 6. What this seat does not establish

- The **host** for the fixed extractor: `tools/` carries no couples resolver
  (`grep -rn 'couples' tools/ --include=*.py` hits only `provenance-audit.py` and
  `source-audit-inventory.py` docstring/fixture text), and both filed resolver
  hosts are filed bytes the round's non-goals bar editing. K01/O01 confirm the
  host; the fenced battery runs against whichever lands via `--against`.
- The **corrected census arithmetic** (O03) and its independent verification
  (O04/O05). This seat supplies the extractor delta (+4 tokens, one file) and the
  controls, not the resolution census.
- Whether the intended token is `tone-prosody.md`: this seat reads the field's
  bytes (`:76` ends `tone-`, `:77` begins `prosody.md`) and the same file's own
  `:279` prose `Natural partners: \`sound-change.md\` …, \`tone-prosody.md\``, which
  corroborates the reading but does not prove authorial intent. Marked
  `to-verify`; the control encodes the reading, and if the intent were
  `prosody.md` the control must be revised with evidence, not silently loosened.

## Owed

- Integrator: place the fenced battery at its durable home (suggested
  `tools/harness/check-couples-extraction.py`) and run it with `--against <the
  landed fixed host>`; the claim's "selftest green" threshold is met only by that
  run, not by this seat's scratch run.
- Integrator: the successor note correcting r39 policy §1's "single physical
  line" extractor rule, carrying the wrap-repair rule of §4.2 and the
  blank-line boundary of §5. The policy document itself stays filed
  (`reports/round-42/claims.json` non-goals: "no filed byte rewrites"; O12 owns
  the arithmetic check).
- K01/O01: the host identification this battery's `--against` mode needs.
- `to-verify`: the `tone-prosody.md` intent question (§6, last bullet).

## Citations

- Assignment: `reports/round-42/targets.json:53-57` (seat `O02`, out
  `op/O02-controls.md`), `:4-9` (shared rules, incl. `:8` no in-tree
  `run-validation.py`); claim O and its thresholds
  `reports/round-42/claims.json:13-21`; non-goals `:24-26`.
- Defect row: `reports/round-40/op/defect-queue-v2.json` row
  `N6-couples-extractor-wrapped-field` (class `carried-with-owner`, owner
  "future resolver round", evidence `reports/round-39/calib/Ca04-verify.md`).
- Filed hosts: `reports/round-19/audit/entry-audit.py:31,34-42,74-96` (`:75`
  single-line capture); `reports/round-27/audit/entry-audit.py:275`.
- C14 shape and its over-capture: `reports/round-35/cov/C14-audit-6-10.md:199`
  (`FIELD_RE`), `:223-236` (`fields_of`), `:249-288` (resolution), `:281`
  (slash-bearing basename key).
- Policy root cause and census unit: `reports/round-39/calib/basename-couples-policy.md:22-24`
  (§1 "single physical line"), `:35-36,268` (`2504 = 2335 + 163 + 0 + 6` at 212
  entries), `:262-269` (filed run summary).
- Wrapped-field bytes and corroborating prose:
  `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, `:279`;
  boundary-case entry `corpus/knowledge/linguistics/conlang-methodology.md:7-9`.
- Command outputs: §3(a)–(e) above (this seat, 2026-10-19, `ac47c78`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only).
  Scratch artefacts (gitignored): `.scratch/o02/o02-selftest.py` (sha256
  `83d0d5cf…`, the fenced draft extracted and executed), `.scratch/o02/o02-controls-harness.py`
  (extended 9-control development harness; superseded by the fence), `.scratch/o02/landed/entry-audit-fixed.py`
  (patched *copy* of the filed host, filed bytes untouched), `.scratch/o02/probe.txt`.
