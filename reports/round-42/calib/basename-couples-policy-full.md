# Basename-couples resolution policy

Adopted by round 39 (claim Ca, leg c) as the lane audit rule for resolving
`couples:` reference tokens in corpus knowledge entries. This document closes the
documentation leg of queue item `basename-couples-policy`
(`reports/round-37/op/defect-queue.json:202-211`: "couples resolver leaves 15
basename-only references unresolved; a working unique-basename fallback exists but
is undocumented policy"). It changes no filed bytes: the round-19 instrument stays
as filed, and successor audit instruments implement this policy.

Method/audit rule only — no canon, no promotion, no corpus byte edit; corpus
admission stays governed by `corpus/QUALITY.md:13-20`.

## 1. Token extraction (fixed, so every audit counts the same population)

- Field: the `- couples:` line of the entry header (single physical line;
  extraction per `reports/round-19/audit/entry-audit.py:75`).
- Tokens: every match of `[A-Za-z0-9_./{},\-]+\.md` in the field value
  (`entry-audit.py:31`), brace-expanded one level (`{a,b}` -> `a`, `b`;
  `entry-audit.py:34-42`), deduplicated per entry. A `:NN` anchor after a token
  is not part of the token (`calibration-registry.md:91` -> token
  `calibration-registry.md`).
- Unit: per-entry deduplicated tokens. Cross-entry repeats count once per entry;
  a global-distinct total may be cited alongside it (r37 scan: 334 per-entry
  tokens vs 222 globally distinct strings — `reports/round-37/adj/A06-verify.md:29`).

## 2. Resolution — two tiers, four classes

Tier 1 — direct (the documented rule; `entry-audit.py:87-95`, unchanged):
a token is class `direct` iff any of

    <entry directory>/<token>   <lane root>/<token>   corpus/knowledge/<token>

names an existing file.

Tier 2 — unique-basename fallback (this policy). Fires only when ALL hold:

  (a) Tier 1 failed for the token;
  (b) the token contains no `/` (pure basename form; §5.1);
  (c) exactly one file under `corpus/knowledge/<partition>/` carries that
      basename, the index being one partition level: glob
      `corpus/knowledge/*/*.md` (index construction:
      `reports/round-35/cov/C14-audit-6-10.md:252-260`).

The token is then class `fallback`, carried with its explicit mapping
`token -> corpus-relative path` in the audit output. Zero index hits ->
`unresolved`; two or more -> `ambiguous`. Neither is ever dropped, guessed, or
counted as resolved.

## 3. Reporting rules

1. The four classes are reported separately, per entry and in totals
   (`C14-audit-6-10.md:332-334` output pattern). A "zero unresolved" claim must
   state the fallback count beside it; "zero dangling couples" without the
   fallback class named is not an admissible result (r37 integration ruling:
   `reports/round-37/scribe/S04-integration-draft.md:38,80`).
2. Fallback hits are never merged into the path-resolved count.
3. Every fallback mapping is listed, not only counted.

## 4. Group-alignment leg

When a `couples:` field groups tokens under domain labels (`myth-symbol —`,
`linguistics —`, ...), every `fallback` token must map into the partition its
group label names (`corpus/knowledge/<label>/...`). A mismatch is an
`alignment` finding, not a resolution. Current population: all 15 fallback
tokens of `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`
align — 7 linguistics, 6 culture-material, 1 verification, 1 synthesis
(independently established at r37: `reports/round-37/adj/A12-gap-fill.md:11-24`;
re-verified with full coverage by §6).

## 5. Limits — what the fallback does not do

1. No re-partitioning of slash-bearing tokens. A token with a partition prefix
   resolves (or not) on Tier 1 alone; a wrong prefix stays a finding even when
   the basename is unique elsewhere. Declared delta: the r35 C14 instrument as
   implemented keys its index on `basename(ref)` for ANY unresolved token,
   slash-bearing included (`C14-audit-6-10.md:281`); this policy narrows that
   behavior. Demonstration: token `linguistics/hero-journey-variants.md` is
   `unresolved` under this policy but would fallback-resolve into
   `corpus/knowledge/myth-symbol/hero-journey-variants.md` under the C14 code
   as written (§6, Part 3).
2. `couples:` only. The `- sources:` locator legs keep their own rules —
   existing repo path, URL, digest — with no basename fallback
   (`C14-audit-6-10.md:291-299`).
3. Existence and one-level uniqueness only. The fallback certifies that the
   target file exists uniquely and (via §4) matches its declared group; it
   certifies neither content quality nor absence of cross-domain bleed
   (`reports/round-37/adj/A12-gap-fill.md:26`).
4. Tier 1 is never relaxed. A directly resolvable token is `direct` even when a
   same-basename file exists elsewhere. The entry-directory base is why the 14
   same-partition basenames in the sacred-kingship field are `direct`, not
   `fallback`.
5. Index scope is exactly one partition level (`corpus/knowledge/*/*.md`; 6
   partitions, 212 files at adoption). Nesting, a new top-level directory, or
   duplicate basenames across partitions change the uniqueness assumption:
   re-run §6 and re-adjudicate before relying on the fallback then.
6. Glob fragments are an extractor artifact, not couples references. Star
   patterns inside the field (`corpus/knowledge/verification/*-gate.md`,
   `tools/gates/*.py` — `corpus/knowledge/verification/gate-frozen-run-standard.md:15`)
   yield partial tokens such as `-gate.md`. A successor instrument should skip
   or separately class glob fragments; this policy forbids counting them as
   unresolved couples findings or resolving them via the fallback.

## 6. Verification recipe (read-only; reproduces the filed evidence)

Run from the lane root; no writes, no runner invocation
(`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```python
import glob, os, re
LANE = os.getcwd()
KNOW = os.path.join(LANE, "corpus", "knowledge")
MDREF = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
BRACE = re.compile(r"\{([^{}]*)\}")
LABEL = re.compile(r"(myth-symbol|linguistics|culture-material|civilizations|verification|synthesis) \u2014")

def expand(s):
    m = BRACE.search(s)
    if not m: return [s]
    out = []
    for part in m.group(1).split(","):
        out.extend(expand(s[:m.start()] + part + s[m.end():]))
    return out

IDX = {}
for p in glob.glob(os.path.join(KNOW, "*", "*.md")):
    IDX.setdefault(os.path.basename(p), []).append(os.path.relpath(p, LANE))

def classify(ref, entry_dir):
    # Tier 1: direct bases (entry dir, lane root, corpus/knowledge) -- entry-audit.py:87-95
    for b in (entry_dir, LANE, KNOW):
        if os.path.isfile(os.path.normpath(os.path.join(b, ref))):
            return "direct", None
    # Tier 2 gate: slash-free tokens only (policy narrows C14:281)
    if "/" in ref:
        return "unresolved", None
    hits = IDX.get(os.path.basename(ref), [])
    if len(hits) == 1: return "fallback", hits[0]
    return ("ambiguous", None) if len(hits) > 1 else ("unresolved", None)

def refs_of(field):
    out = set()
    for raw in MDREF.findall(field):
        for c in expand(raw):
            out.add(c.strip())
    return out

def couples_field(text):
    m = re.search(r"^- couples:\s*(.*)$", text, re.M)
    return m.group(1) if m else ""

ELEVEN = [
 "corpus/knowledge/culture-material/agrarian-field-system-lexicon.md",
 "corpus/knowledge/culture-material/bathing-and-body-hygiene.md",
 "corpus/knowledge/culture-material/fire-fuel-light.md",
 "corpus/knowledge/culture-material/funerary-material-culture.md",
 "corpus/knowledge/culture-material/furniture-interior-lexicon.md",
 "corpus/knowledge/culture-material/writing-media-surface-economy.md",
 "corpus/knowledge/culture-material/timekeeping-instruments.md",
 "corpus/knowledge/myth-symbol/binding-speech-complex.md",
 "corpus/knowledge/myth-symbol/death-afterlife-eschatology.md",
 "corpus/knowledge/myth-symbol/eschatology-world-end-systems.md",
 "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
]

print("== Part 1: eleven r35/r36 entries (r37 scan reproduction) ==")
tot = {"direct":0,"fallback":0,"ambiguous":0,"unresolved":0}
for rel in ELEVEN:
    d = os.path.join(LANE, rel)
    cls = {r: classify(r, os.path.dirname(d)) for r in sorted(refs_of(couples_field(open(d, encoding="utf-8").read())))}
    for c, _ in cls.values(): tot[c] += 1
    print("  %-45s refs=%3d " % (rel.split("/")[-1], len(cls)) +
          " ".join("%s=%d" % (k, sum(1 for _, (cc, _) in cls.items() if cc == k))
                   for k in ("direct","fallback","ambiguous","unresolved")))
print("  TOTALS: refs=%d (per-entry dedup, summed) -> %s" % (sum(tot.values()),
      " ".join("%s=%d" % (k, v) for k, v in tot.items())))

print("== Part 1b: group alignment of all fallback refs (sacred-kingship couples field) ==")
d = os.path.join(LANE, ELEVEN[-1]); skdir = os.path.dirname(d)
field = couples_field(open(d, encoding="utf-8").read())
misaligned = 0
for m in MDREF.finditer(field):
    c, mp = classify(m.group(0), skdir)
    if c != "fallback": continue
    labs = LABEL.findall(field[:m.start()])
    lab = labs[-1] if labs else None
    ok = bool(lab) and mp.startswith("corpus/knowledge/" + lab + "/")
    misaligned += (not ok)
    print("  %-38s -> %s  group=%-16s %s" % (m.group(0), mp, lab, "OK" if ok else "MISALIGNED"))
print("  misaligned=%d" % misaligned)

print("== Part 2: corpus-wide current scan (corpus/knowledge/*/*.md) ==")
tot2 = dict.fromkeys(("direct","fallback","ambiguous","unresolved"), 0)
unres, amb, n = {}, {}, 0
for dd in sorted(glob.glob(os.path.join(KNOW, "*", "*.md"))):
    n += 1
    for r in refs_of(couples_field(open(dd, encoding="utf-8").read())):
        c, mp = classify(r, os.path.dirname(dd))
        tot2[c] += 1
        if c == "unresolved": unres[r] = unres.get(r, 0) + 1
        if c == "ambiguous": amb.setdefault(r, []).append(mp)
print("  entries=%d refs=%d -> %s" % (n, sum(tot2.values()),
      " ".join("%s=%d" % (k, v) for k, v in tot2.items())))
print("  unresolved distinct=%d: %s" % (len(unres),
      ", ".join("%s(x%d)" % (r, c) for r, c in sorted(unres.items()))))
for r, ms in amb.items(): print("  AMBIGUOUS: %s -> %s" % (r, ms))

print("== Part 3: slash-gate delta demonstration (synthetic, in-memory) ==")
for tok in ("linguistics/hero-journey-variants.md", "hero-journey-variants.md", "no-such-entry-anywhere.md"):
    c_pol, mp = classify(tok, skdir)
    hits = IDX.get(os.path.basename(tok), [])
    c14 = ("fallback -> " + hits[0]) if len(hits) == 1 and c_pol == "unresolved" else c_pol
    print("  %-42s policy=%-11s C14-code-as-written=%s" % (tok, c_pol, c14))

fail = not (tot["fallback"] == 15 and tot["ambiguous"] == 0 and tot["unresolved"] == 0
            and tot["direct"] + tot["fallback"] == 334 and misaligned == 0)
print("RESULT:", "FAIL" if fail else "PASS (334=319+15, 0 ambiguous, 0 unresolved, 0 misaligned)")
```

Filed run of this exact script (2026-10-19, tree at round-39 baseline `dfb0719`,
212 knowledge entries), summary:

- Part 1 — eleven-entry totals `refs=334 -> direct=319 fallback=15 ambiguous=0
  unresolved=0`; sacred-kingship: 36 = 21 direct + 15 fallback; RESULT line
  `PASS (334=319+15, 0 ambiguous, 0 unresolved, 0 misaligned)`.
- Part 1b — all 15 fallback refs printed `OK`, `misaligned=0`
  (7 linguistics, 6 culture-material, 1 verification, 1 synthesis).
- Part 2 — `entries=212 refs=2504 -> direct=2335 fallback=163 ambiguous=0
  unresolved=6`, 5 distinct, all attributed:
  `-gate.md` x1 = the §5.6 glob fragment from
  `corpus/knowledge/verification/gate-frozen-run-standard.md:15`;
  `../linguistics/phonology-sanity.md` x2 = the r19 X26-1 phantom, still live in
  `corpus/knowledge/verification/label-channel-routing-verification.md:14`
  (`reports/round-19/audit/x26-spotcheck-entries.md` §3;
  `C14-audit-6-10.md:114-119`);
  `phonology-basics.md`, `naming-and-onomastics.md`, `honorifics-and-register.md`
  x1 each = never-written "sibling knowledge files to seed" named in
  `corpus/knowledge/linguistics/language-contact.md:7` (its other two seeds,
  `writing-systems.md` and `numerals-and-measures.md`, exist and resolve).
- Part 3 — the §5.1 delta, observed: `linguistics/hero-journey-variants.md`
  policy=`unresolved`, C14-as-written=`fallback ->
  corpus/knowledge/myth-symbol/hero-journey-variants.md`.

Part 1 reproduces the filed r37 counts from every angle: A02's 334 checked /
0 unresolved (contingent on exactly this fallback —
`reports/round-37/adj/A02-entries-bleed.md:7,23`), A06's 319 direct + 15
unresolved under the documented-only resolver
(`reports/round-37/adj/A06-verify.md:29`), A08's conditional zero
(`reports/round-37/adj/A08-verify.md:17`), and A12's independent 334/319/15
(`reports/round-37/adj/A12-gap-fill.md:9`).

## 7. Adoption evidence

- Queue item: `reports/round-37/op/defect-queue.json:202-211`.
- Finding population: `reports/round-37/scout/K04-entries-scout.md:43,56,61`;
  `reports/round-37/adj/A06-verify.md:29,49`; `reports/round-37/adj/A08-verify.md:17,31`.
- Cross-check this policy encodes: `reports/round-37/adj/A12-gap-fill.md:9-26,38`.
- Fallback in prior, undocumented use: `reports/round-35/cov/C14-audit-6-10.md:249-288`
  (instrument), `:69` and `:112-119` (filed counts incl. the 4- and 148-shorthand
  populations and the 8 unresolved).
- Documented direct-only resolver: `reports/round-19/audit/entry-audit.py:74-96`.
- Integration rulings this policy answers:
  `reports/round-37/scribe/S04-integration-draft.md:38,80,109,124`.
