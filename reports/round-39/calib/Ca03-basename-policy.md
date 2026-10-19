- Seat: Ca03 | executor | claim Ca | date 2026-10-19 | baseline dfb0719

# Ca03 — basename-couples fallback policy (r37 queue item `basename-couples-policy`)

Draft for the integrator: land the fenced document below **verbatim** at
`reports/round-39/calib/basename-couples-policy.md` (the path claim Ca's
`after_required` names, `reports/round-39/claims.json:22`), then close queue item
`basename-couples-policy` (`reports/round-37/op/defect-queue.json:202-211`,
`next_touch` "document or fix the resolver") with a pointer to it. This drafts the
**document** leg; no filed byte is edited by this seat — `entry-audit.py` and the
r35 C14 fragment stay exactly as filed. The policy was verified live before
drafting: the §6 recipe ran clean this seat (output quoted in the document and
summarized under Citations).

Key design decisions, each evidence-backed (details in the document):

1. Two tiers, four classes: the documented three-base direct rule
   (`reports/round-19/audit/entry-audit.py:87-95`) stays Tier 1 and is never
   relaxed; the unique-basename fallback becomes Tier 2 with explicit
   `direct / fallback / ambiguous / unresolved` classes — closing S04's ruling
   that "zero dangling couples" must not be reported unconditionally
   (`reports/round-37/scribe/S04-integration-draft.md:38,80`).
2. The fallback fires for slash-free tokens only. This is a **declared narrowing**
   of the r35 C14 instrument as implemented, which keys its index on
   `basename(ref)` for *any* unresolved token, slash-bearing included
   (`reports/round-35/cov/C14-audit-6-10.md:281`): under C14-as-written a typo'd
   `linguistics/hero-journey-variants.md` would silently retarget into
   `myth-symbol/`; under this policy it stays `unresolved` (demonstrated live,
   §6 Part 3). Flagged here so Ca04 files it as a decision, not an error.
3. Group-alignment leg: when a `couples:` field groups tokens under domain
   labels, every fallback mapping must land in the partition its label names.
   All 15 current fallback refs align (re-verified with full coverage this run;
   A12 verified the same 15 independently at `57c8409`,
   `reports/round-37/adj/A12-gap-fill.md:11-26`).
4. Fresh corpus-wide measurement at this round's tree (212 entries): 2504
   `couples:` refs → 2335 direct + 163 fallback + 0 ambiguous + 6 unresolved
   (5 distinct, all attributed — see Citations). The fallback is therefore a
   corpus-wide load-bearing rule (163 refs), not a sacred-kingship special case.

````markdown
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
````

## Owed

- Integrator: land the fenced document above verbatim at
  `reports/round-39/calib/basename-couples-policy.md`; close defect-queue item
  `basename-couples-policy` with a pointer to it. Do not edit
  `reports/round-19/audit/entry-audit.py` (filed bytes) — successor instruments
  implement the policy.
- Ca04 (verifier seat): check the policy's §1–§2 semantics against
  `entry-audit.py:74-96` and `C14-audit-6-10.md:249-288`, §4/§7 against
  `A12-gap-fill.md`; the §5.1 slash-gate narrowing vs `C14-audit-6-10.md:281`
  is a declared decision of this seat, to be confirmed or contested — a
  disagreement there is expected to be filed, not silent.
- to-verify: whether the unresolved trio in
  `corpus/knowledge/linguistics/language-contact.md:7` (three never-written
  seeds) and the X26-1 phantom get repair dispositions — outside this seat's
  claim; recorded here as scan findings only.
- to-verify: whether a successor audit instrument should give glob fragments
  (§5.6) their own extractor rule; this policy only fixes their reporting
  treatment.

## Citations

- Assignment: `reports/round-39/targets.json:90-95` (seat Ca03, out
  `calib/Ca03-basename-policy.md`); claim Ca leg (c) and durable path:
  `reports/round-39/claims.json:19-24`.
- Queue item: `reports/round-37/op/defect-queue.json:202-211`.
- Documented resolver (Tier 1): `reports/round-19/audit/entry-audit.py:31,34-42,74-96`
  (MDREF `:31`; braces `:34-42`; candidates `:87-91`; resolve/unresolved `:92-95`).
- Fallback instrument (undocumented policy being adopted):
  `reports/round-35/cov/C14-audit-6-10.md:249-288` (index `:252-260`; classes
  `:271-288`; slash-bearing basename key `:281`); filed use counts `:69`, `:112-119`;
  sources-leg locator rules (no fallback) `:291-299`.
- r37 finding + cross-checks: `reports/round-37/scout/K04-entries-scout.md:43,56,61`;
  `reports/round-37/adj/A02-entries-bleed.md:7,23`;
  `reports/round-37/adj/A06-verify.md:29,49`;
  `reports/round-37/adj/A08-verify.md:17,31`;
  `reports/round-37/adj/A12-gap-fill.md:9-26,38`.
- Integration rulings: `reports/round-37/scribe/S04-integration-draft.md:38,80,109,124`.
- X26-1 phantom provenance: `reports/round-19/audit/x26-spotcheck-entries.md` §3
  (as quoted in `C14-audit-6-10.md:114-119`); live source line
  `corpus/knowledge/verification/label-channel-routing-verification.md:14`.
- Unresolved trio provenance: `corpus/knowledge/linguistics/language-contact.md:7`.
- Glob-fragment provenance: `corpus/knowledge/verification/gate-frozen-run-standard.md:15`.
- The 15 fallback refs' field: `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`.
- Command output (this seat, 2026-10-19, lane root, tree at baseline `dfb0719`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, read-only heredoc =
  §6's script): Part 1 `refs=334 -> direct=319 fallback=15 ambiguous=0
  unresolved=0`, RESULT `PASS (334=319+15, 0 ambiguous, 0 unresolved, 0
  misaligned)`; Part 1b 15/15 OK, `misaligned=0`; Part 2 `entries=212
  refs=2504 -> direct=2335 fallback=163 ambiguous=0 unresolved=6`, 5 distinct
  (`-gate.md` x1, `../linguistics/phonology-sanity.md` x2,
  `honorifics-and-register.md` x1, `naming-and-onomastics.md` x1,
  `phonology-basics.md` x1); Part 3 delta as §5.1. No filed byte was edited; no
  `run-validation.py` was executed; no git, network, or install actions.
