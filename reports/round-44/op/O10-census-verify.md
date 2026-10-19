# O10 — census arithmetic verification (claim O)

- Seat: O10 | role verifier | claim O | date 2026-10-19T17:21Z
- Out: `reports/round-44/op/O10-census-verify.md`
- Mission (`reports/round-44/targets.json`, seat `O10`): independently recompute the four-class fold from the O09 body's `--census` output (2556+166+0+7=2729 +1 glob = 2730); confirm zero tokens dropped and policy §5.6's glob exclusion is honored; confirm the census artifact's conservation identity.
- Baseline: `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (`git rev-parse HEAD`); `git status --porcelain` at read time showed only `?? reports/round-44/` (this round's out files). No filed byte was edited by this seat.
- Method: read-only. Extracted the fenced body to `.scratch/r44-o10/resolver.py`, ran it there, and recomputed the fold with a second, policy-derived implementation that does **not** import the body. No corpus staging, no in-tree `run-validation.py`, no git/network/install.

**Verdict: PASS** on all four assigned checks. Two filing caveats are recorded in §6: the machine payload has no `baseline_commit` and hard-codes `round: 43`; the `conservation` boolean is tautological by construction and is not, by itself, evidence that no token was dropped (my independent fold is that evidence).

---

## 1. Inputs and provenance

### 1.1 The body under test

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/r44-o10/resolver.py
$ wc -l .scratch/r44-o10/resolver.py
515 .scratch/r44-o10/resolver.py
$ sha256sum .scratch/r44-o10/resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  .scratch/r44-o10/resolver.py
```

The digest matches the claim prefix `43ce341f…` (`reports/round-44/claims.json:26`) and the r43 fence is exactly `` ````python `` at `reports/round-43/op/O09-scribe.md:355` through the closing fence at `:871`. Body line *N* cites as `O09-scribe.md:(N+355)` below.

The body is **not yet landed**: `ls tools/harness/basename-couples-resolver.py` → `No such file or directory` at the verification tree. This out verifies the body as a candidate; it does not land it (O01/O09 own the landing evidence).

### 1.2 Population pin

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do echo "$p $(ls corpus/knowledge/$p/*.md | wc -l)"; done
linguistics 25
myth-symbol 26
culture-material 25
synthesis 29
verification 24
civilizations 94
```

`25+26+25+29+24+94 = 223`. Manifest digest over sorted `path:sha256` lines (recipe: `reports/round-43/op/O10-census-artifact.md:544-552`):

```
444ff801727604b614e1eca302ff77314ebbd0f5f064a82d1c167e7f02125e35
```

This reproduces the r43 population digest at the r44 baseline (`reports/round-43/op/O10-census-artifact.md:45`), so the census below and the r43 measurement are on the same 223-entry bytes.

### 1.3 Selftest gate

```
$ cd .scratch/r44-o10 && python3 resolver.py --selftest ; echo EXIT=$?
PASS S1a embedded fixture == live bytes at :72
PASS S1b wrapped field extracts 4/4 by identity (not arity)
PASS S1c no mangled token (prosody.md / toneprosody.md / space split)
PASS S1d before-state: the filed single-line capture yields 0 tokens
PASS S1e space-join is the rejected shape (prosody.md, never tone-prosody.md)
PASS S1f live field resolves 2 direct + 2 unresolved (four-class policy)
PASS S2a phantom tokens survive extraction 2/2
PASS S2b hyphen-wrapped phantom heals to synthetic-phantom-beta.md
PASS S2c zero basename hits -> unresolved (both, not dropped)
PASS S3a two basename hits -> ambiguous
PASS S3b ambiguous is not guessed to one path
PASS S3c one basename hit -> fallback with its explicit mapping
PASS S4a Tier-1 direct wins over a same-basename hit elsewhere (5.4)
PASS S4b direct carries no fallback mapping
PASS S4c corpus-relative path token -> direct (Tier-1 base 3)
PASS S5 no-drop live: 4/4 tokens classed
PASS S5 no-drop phantom: 2/2 tokens classed
PASS S5 no-drop ambiguous: 1/1 tokens classed
PASS S5 no-drop direct: 1/1 tokens classed
PASS S6 slash-bearing token stays unresolved despite a unique basename elsewhere
PASS S7a body prose after a blank line is excluded
PASS S7b couples as the last header field does not swallow the body
PASS S7c blank line + indented prose is excluded (no over-capture)
PASS S8 glob fragment is an artifact, not an unresolved finding (5.6)
PASS S8b glob fragment wins over the ambiguous branch (5.6)
PASS S9 live census conservation (four classes + artifacts == refs)
PASS S10 live wrapped entry reads 4 tokens (2 direct + 2 unresolved)
SELFTEST OK: 27/27 controls
EXIT=0
```

---

## 2. Independent recomputation

### 2.1 Method

I implemented the fold from `reports/round-42/calib/basename-couples-policy-full.md` §1-§2 and §5.6, **not** from the O09 body (no import, no copied code):

- field = the `- couples:` header value; continuation lines are indented lines; the first blank line or the next header field terminates the block (the r43 over-capture fix, and the negative control at S7c);
- a trailing hyphen on a wrapped part is a soft wrap: concatenate keeping the hyphen (`tone-` + `prosody.md` → `tone-prosody.md`);
- tokens = every `[A-Za-z0-9_./{},\-]+\.md` match, brace-expanded, deduplicated per entry (policy §1:14-26);
- classification per policy §2:27-48 — Tier-1 bases (entry dir, lane root, `corpus/knowledge`), then slash-bearing → `unresolved`, else basename index over `corpus/knowledge/*/*.md`: 1 hit → `fallback`, ≥2 → `ambiguous`, 0 → `unresolved`;
- §5.6 (policy:97-102): a token that is part of a glob pattern (immediately preceded by `*`, or containing `*`) is a separate `glob-fragment` artifact, never an `unresolved` couples finding.

The compact reproduction script is embedded in §8. A first pass of my implementation omitted the hyphen soft-wrap; it produced `prosody.md` instead of `tone-prosody.md` on the one wrapped entry — exactly the rejected shape S1c/S1e guard. That was a defect in **my** first pass, not the tool: it changed one token's label but not the class totals (`prosody.md` and `tone-prosody.md` are both `unresolved`), which is a useful negative control for the "identity, not arity" claim. After implementing the soft-wrap identity, all 223 per-entry maps matched (§3.2).

### 2.2 Side-by-side

| quantity | O09 `--census` | independent | agree |
|---|---:|---:|---|
| entries | 223 | 223 | yes |
| refs (per-entry dedup) | 2730 | 2730 | yes |
| direct | 2556 | 2556 | yes |
| fallback | 166 | 166 | yes |
| ambiguous | 0 | 0 | yes |
| unresolved | 7 | 7 | yes |
| glob-fragment (artifact) | 1 | 1 | yes |
| fallback distinct mappings | 50 | 50 | yes |
| fallback occurrences | 166 | 166 | yes |
| unresolved rows | 7 | 7 | yes |
| wrapped fields | 1 | 1 | yes |
| per-entry class maps identical | — | 223/223 | yes |

### 2.3 Arithmetic

```
2556 + 166 = 2722
2722 +   0 = 2722
2722 +   7 = 2729      (four-class total)
2729 +   1 = 2730      (+ the quarantined glob artifact)
2730 == refs           (entries_detail token sum = 2730)
```

The tool's own stdout (`reports/round-44/op/O10-census-verify.md` §7, verbatim):

```
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
```

The r42 witness (`tools/harness/couples-reference-extractor.py --census`, read-only) was also run as a six-class cross-check:

```
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
```

`2556+166+2+5+1 = 2730`; the four-class fold closes `2+5` into `unresolved=7`. The two tools agree on the population, the refs and the direct/fallback totals; they differ only by the documented six-class-vs-four-class subclass presentation, which is the parity O07 owns.

---

## 3. Zero tokens dropped

### 3.1 Extraction → classification accounting

- Raw `.md` matches after brace expansion, across all 223 entries: **2733 occurrences**.
- Per-entry distinct tokens (policy §1 dedup): **2730**.
- Classed tokens: **2730** (every distinct token receives exactly one of the five classes).

The 3-occurrence reduction is the policy-sanctioned per-entry dedup, not a drop. The three duplicated tokens are:

| entry | duplicated token | occurrences |
|---|---|---:|
| `corpus/knowledge/culture-material/craft-artisan-lexicon.md` | `culture-material/era-periodization-models.md` | 2 |
| `corpus/knowledge/culture-material/funerary-material-culture.md` | `culture-material/material-culture-inference-method.md` | 2 |
| `corpus/knowledge/linguistics/taboo-strata-lifecycle.md` | `politeness-taboo-euphemism.md` | 2 |

Both implementations dedup per entry identically (`field_refs` uses a `set` in the body; my reproduction uses `seen`), which is why 2733 → 2730 → 2730.

### 3.2 Per-entry agreement

Compared all 223 `entries_detail` records against my independent per-entry class map:

```
entries: 223 223
mismatches: 0
tool per-entry token sum: 2730 independent: 2730
```

Every token in every entry has a class; no entry is missing from either side; no token name differs (after the soft-wrap identity fix).

### 3.3 Resolution legs

- **Fallback mappings**: 50 distinct rows, occurrences sum **166 = fallback class total**. For each of the 50: the mapping path exists on disk and is the *unique* basename hit in `corpus/knowledge/*/*.md` (0 defects). Every mapping is printed, not merely counted (policy §3.3).
- **Direct**: every `direct` token re-resolves at one of the three Tier-1 bases (0 defects).
- **Unresolved**: 7 rows = 7 class occurrences, 6 distinct tokens (`../linguistics/phonology-sanity.md` occurs in 2 entries and is correctly counted once per entry). Each row carries a non-empty reason: 5 `declared-prospective-seed`, 2 `dangling-reference` (policy §2: zero index hits → unresolved; never guessed). Independent zero-hit check: all six distinct basenames have **zero** files in `corpus/knowledge/*/*.md`; `phonology-sanity.md` does not exist anywhere, so the `../linguistics/` token is unresolved both by the §5.1 slash gate and by zero hits.
- **Ambiguous**: 0 rows = 0 class total; no token was guessed to one path.
- **Glob**: 1 row = 1 artifact; see §4.

### 3.4 Caveat: the tool's `conservation` flag is tautological

The body computes `refs = sum(totals.values())` (`O09-scribe.md:611`) and then `"conservation": sum(four.values()) + sum(artifacts.values()) == refs` (`O09-scribe.md:617`). Since `four` and `artifacts` are subsets of the same `totals` dict and every increment uses one of those class keys, the equality is true by construction. It guards against a class missing from `CLASSES`/`ARTIFACTS` (a new class would inflate `refs`), but it cannot detect a token that was never extracted or was dropped before classification. **The zero-drop evidence is the independent extraction in §3.1-§3.2, not the `conservation` boolean.** The integrator should carry the independent count (`extracted_tokens: 2730`) or the population digest (`444ff801…`) in the filed artifact rather than treating `"conservation": true` as sufficient.

---

## 4. Policy §5.6 glob exclusion

Policy text (`reports/round-42/calib/basename-couples-policy-full.md:97-102`): star patterns inside the field yield partial tokens such as `-gate.md`; a successor instrument "should skip or separately class glob fragments"; the policy "forbids counting them as unresolved couples findings or resolving them via the fallback".

Observed:

- Exactly **one** glob artifact in the live corpus: `-gate.md` from `corpus/knowledge/verification/gate-frozen-run-standard.md` (the `corpus/knowledge/verification/*-gate.md` star pattern). My independent detector found the same entry and token.
- The tool classes it `glob-fragment` and reports it under `artifacts (excluded from the four-class totals): glob-fragment=1`, with disposition `extractor-artifact`, `c12=not-applicable`. It is **not** in `unresolved` (which stays 7), and it is not resolved via the fallback.
- Precedence: `GLOB_FRAG_RE` (`O09-scribe.md:403`), checked in `classify` (`O09-scribe.md:499`, glob branch at `:504`) **after** Tier-1 direct and **before** the slash/zero-hit unresolved branch and before the basename index. S8b proves glob wins over the ambiguous branch when a synthetic index has two `-gate.md` hits.
- Exclusive accounting: the five class totals sum to 2730 with no double count. If the glob fragment had been left in `unresolved`, unresolved would read 8 and the four-class total 2730; the tool reports 7 and 2729+1, as required.

Edge to-verify (no live instance): Tier-1 direct is checked before the glob branch (`O09-scribe.md:501-504`), so a glob fragment that happens to name an existing file would be classed `direct`. No such token exists in the 223-entry tree; if the corpus grows a file literally named `-gate.md` (or a `*`-bearing name), re-run the fold and adjudicate. This is a policy edge, not a current arithmetic defect.

---

## 5. Wrapped-field corroboration (claim `after_required`, bonus check)

`corpus/knowledge/linguistics/phonetics-phonology.md` couples field wraps across five physical lines; it is the single `wrapped fields: 1` entry. The joined field ends in:

```
...; prospective sibling files: sound-change.md, tone-
  prosody.md, sound-symbolism.md, writing-systems.md
```

Identity read: `sound-change.md`, `tone-prosody.md`, `sound-symbolism.md`, `writing-systems.md` — **4 tokens by identity**, classes 2 `direct` (`sound-symbolism.md`, `writing-systems.md`) + 2 `unresolved` (`sound-change.md`, `tone-prosody.md`). The rejected shapes are absent: no `prosody.md`, no `toneprosody.md` (S1b/S1c/S1e/S10). This is consistent with the r42 witness's 4/4 wrapped read, and confirms the token identity is not an arity accident.

---

## 6. Census artifact: conservation identity and filing checklist

At verification time (`2026-10-19T17:21Z`) `reports/round-44/calib/` was empty; **no census artifact had been filed yet** (O06 is a parallel seat). The identity below is what the filed artifact must satisfy; the artifact-specific fields are `to-verify` at integration.

### 6.1 Identity (verified against the machine payload)

```
four_class: {direct: 2556, fallback: 166, ambiguous: 0, unresolved: 7}
artifact:   {glob-fragment: 1}
classified  = 2556 + 166 + 0 + 7            = 2729
extracted   = classified + artifact_total   = 2729 + 1 = 2730
refs        = extracted                     = 2730
fallback_occurrences                        = 166
unresolved_rows                             = 7
ambiguous_rows                              = 0
```

All hold in `--census --json` (`schema: kotodama-couples-census-v3`, `tool_sha256: 43ce341f…`).

### 6.2 Fields the integrator must add when filing

The `--json` payload contains: `entries`, `refs`, `four_class_totals`, `artifact_totals`, `conservation`, `wrapped_fields`, `fallback_mappings` (50), `disposition` (7 unresolved + 0 ambiguous + 1 glob), `misaligned` ([]), `entries_detail` (223), `schema`, `round`, `tool`, `tool_sha256`.

- **`baseline_commit` is absent.** O06's contract (`reports/round-44/targets.json:23`) requires a `baseline_commit` + `entries` header; the integrator must add `baseline_commit: c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (or the close commit) when filing. The tool must not be edited to add it (the claim lands the body byte-exact).
- **`round` is hard-coded `43`** at `O09-scribe.md:816` (`payload["round"] = 43`). Filed verbatim for r44, the payload will self-describe as round 43. The integrator should record the round in the artifact wrapper/Markdown and annotate the payload field, not modify the tool bytes. Flagged as provenance, not arithmetic.
- If the C landing moves the tree to 224 before the census is filed, **re-run**; do not file the 223 numbers against a 224 tree. The census must record the tree it ran on (single census artifact, claim O: "File ONE census artifact").

### 6.3 What this seat did not verify

- The landed tool path (`tools/harness/basename-couples-resolver.py`) does not exist yet; this verification used the byte-identical extracted body.
- The census artifact file itself; no file was present at read time. O06/scribe and the integrator own its contents.
- `--selftest` internals beyond execution and the 27/27 count (O02/O03/O05 own the control semantics).

---

## 7. Raw census stdout (verbatim, durable copy)

Command: `cd .scratch/r44-o10 && python3 resolver.py --census` (rc=0). Stdout sha256 `87ef57d5db28676563dbb94df838bdc0979482bc1dc4229548357c20adfc7867`.

```
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct):
    adornment-body-codes.md                  -> corpus/knowledge/culture-material/adornment-body-codes.md    x2
    animal-symbolism.md                      -> corpus/knowledge/myth-symbol/animal-symbolism.md             x1
    architecture-settlement-lexicon.md       -> corpus/knowledge/culture-material/architecture-settlement-lexicon.md x4
    calendar-festival-systems.md             -> corpus/knowledge/culture-material/calendar-festival-systems.md x2
    calibration-registry.md                  -> corpus/knowledge/verification/calibration-registry.md        x2
    color-symbolism.md                       -> corpus/knowledge/myth-symbol/color-symbolism.md              x3
    comparative-frameworks.md                -> corpus/knowledge/myth-symbol/comparative-frameworks.md       x4
    consistency-verification-checklist.md    -> corpus/knowledge/synthesis/consistency-verification-checklist.md x1
    cosmology-cosmography.md                 -> corpus/knowledge/myth-symbol/cosmology-cosmography.md        x2
    costume-semiotics.md                     -> corpus/knowledge/culture-material/costume-semiotics.md       x8
    coupling-model.md                        -> corpus/knowledge/synthesis/coupling-model.md                 x1
    creation-myths-taxonomy.md               -> corpus/knowledge/myth-symbol/creation-myths-taxonomy.md      x1
    dress-through-eras.md                    -> corpus/knowledge/culture-material/dress-through-eras.md      x5
    era-language-staging.md                  -> corpus/knowledge/synthesis/era-language-staging.md           x1
    era-periodization-models.md              -> corpus/knowledge/culture-material/era-periodization-models.md x1
    garment-lexicon-crosslinguistic.md       -> corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md x3
    historical-linguistics.md                -> corpus/knowledge/linguistics/historical-linguistics.md       x9
    inca.md                                  -> corpus/knowledge/civilizations/inca.md                       x1
    kinship-terminology.md                   -> corpus/knowledge/linguistics/kinship-terminology.md          x1
    language-contact.md                      -> corpus/knowledge/linguistics/language-contact.md             x10
    lexicon-coverage-audit.md                -> corpus/knowledge/verification/lexicon-coverage-audit.md      x1
    loanword-material-dating.md              -> corpus/knowledge/synthesis/loanword-material-dating.md       x1
    material-culture-inference-method.md     -> corpus/knowledge/culture-material/material-culture-inference-method.md x10
    maya-classic.md                          -> corpus/knowledge/civilizations/maya-classic.md               x1
    mesopotamia-sumer-akkad.md               -> corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md    x1
    morphological-typology.md                -> corpus/knowledge/linguistics/morphological-typology.md       x2
    music-instrument-lexicon.md              -> corpus/knowledge/culture-material/music-instrument-lexicon.md x1
    myth-ritual-theories.md                  -> corpus/knowledge/myth-symbol/myth-ritual-theories.md         x1
    myth-to-language-derivation.md           -> corpus/knowledge/synthesis/myth-to-language-derivation.md    x1
    naming-systems.md                        -> corpus/knowledge/linguistics/naming-systems.md               x14
    number-symbolism.md                      -> corpus/knowledge/myth-symbol/number-symbolism.md             x1
    orality-formulaic-language.md            -> corpus/knowledge/linguistics/orality-formulaic-language.md   x4
    pantheon-archetypes.md                   -> corpus/knowledge/myth-symbol/pantheon-archetypes.md          x5
    phonetics-phonology.md                   -> corpus/knowledge/linguistics/phonetics-phonology.md          x1
    politeness-taboo-euphemism.md            -> corpus/knowledge/linguistics/politeness-taboo-euphemism.md   x2
    real-world-inspiration-boundaries.md     -> corpus/knowledge/verification/real-world-inspiration-boundaries.md x2
    register-strata-attestation.md           -> corpus/knowledge/linguistics/register-strata-attestation.md  x1
    religion-language-co-evolution.md        -> corpus/knowledge/synthesis/religion-language-co-evolution.md x1
    ritual-garments.md                       -> corpus/knowledge/culture-material/ritual-garments.md         x6
    ritual-liminality.md                     -> corpus/knowledge/myth-symbol/ritual-liminality.md            x2
    semantics-pragmatics.md                  -> corpus/knowledge/linguistics/semantics-pragmatics.md         x3
    sociolinguistics-registers.md            -> corpus/knowledge/linguistics/sociolinguistics-registers.md   x7
    source-discipline-calibration.md         -> corpus/knowledge/synthesis/source-discipline-calibration.md  x1
    sumptuary-law-rank-display.md            -> corpus/knowledge/culture-material/sumptuary-law-rank-display.md x3
    symbolism-synthesis-method.md            -> corpus/knowledge/myth-symbol/symbolism-synthesis-method.md   x10
    taboo-euphemism-lifecycle.md             -> corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md      x1
    textile-technology.md                    -> corpus/knowledge/culture-material/textile-technology.md      x4
    trade-economy-lexicon.md                 -> corpus/knowledge/culture-material/trade-economy-lexicon.md   x3
    warrior-material-culture.md              -> corpus/knowledge/culture-material/warrior-material-culture.md x1
    writing-systems.md                       -> corpus/knowledge/linguistics/writing-systems.md              x13
  unresolved (7 rows):
    honorifics-and-register.md           corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    naming-and-onomastics.md             corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    phonology-basics.md                  corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    sound-change.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    tone-prosody.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/synthesis/typed-label-routing-workflow.md dangling-reference           c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/verification/label-channel-routing-verification.md dangling-reference           c12=blocker
  ambiguous (0 rows):
  glob-fragment (1 rows):
    -gate.md                             corpus/knowledge/verification/gate-frozen-run-standard.md extractor-artifact           c12=not-applicable
  misaligned: none
```

Machine payload sha256 `4cb9c0dafc9186355f76dae9a0e1011f2777249f6bff0616fe2530951c51833b`; independent JSON sha256 `017aabced0bc390ef9637b18ef56cf787e41f88509cfffc947bcad26a73dcc99`. Those two files and the reproduction script were `.scratch` working files; the stdout above is the durable copy.

---

## 8. Reproduction

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```sh
# 1. body + digest
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/r44-o10/resolver.py
sha256sum .scratch/r44-o10/resolver.py    # 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64

# 2. gate + census (clean dir; lane root found by walking up)
cd .scratch/r44-o10
python3 resolver.py --selftest && python3 resolver.py --census --json > census.json
```

Independent fold (policy-derived, does not import the body; reproduces §2):

```python
import glob, os, re
LANE=os.getcwd(); KNOW=os.path.join(LANE,"corpus","knowledge")
MD=re.compile(r"[A-Za-z0-9_./{},\-]+\.md"); BR=re.compile(r"\{([^{}]*)\}")
FIELD=re.compile(r"^- ([a-z][a-z-]*):[ \t]*(.*)$"); IND=re.compile(r"^[ \t]+\S")
def exp(s):
    m=BR.search(s)
    if not m: return [s]
    return sum([exp(s[:m.start()]+a+s[m.end():]) for a in m.group(1).split(",")],[])
def field(text):
    ls=text.splitlines(keepends=True)
    for i,l in enumerate(ls):
        m=FIELD.match(l.rstrip("\r\n"))
        if m and m.group(1)=="couples":
            parts=[m.group(2).strip()]
            for f in ls[i+1:]:
                r=f.rstrip("\r\n")
                if not r.strip() or FIELD.match(r): break
                if IND.match(r): parts.append(r.strip()); continue
                break
            out=""
            for p in parts:
                out = p if not out else (out+p if re.search(r"[A-Za-z0-9_]-$",out) else out+" "+p)
            return out
    return None
idx={}
for p in glob.glob(os.path.join(KNOW,"*","*.md")):
    idx.setdefault(os.path.basename(p),[]).append(os.path.relpath(p,LANE))
tot=dict.fromkeys(("direct","fallback","ambiguous","unresolved","glob-fragment"),0)
for p in sorted(glob.glob(os.path.join(KNOW,"*","*.md"))):
    text=open(p,encoding="utf-8",errors="replace").read(); f=field(text) or ""
    seen=set()
    for m in MD.finditer(f):
        globbed = (m.start()>0 and f[m.start()-1]=="*") or "*" in m.group(0)
        for t in exp(m.group(0)):
            t=t.strip()
            if t in seen: continue
            seen.add(t)
            if globbed: k="glob-fragment"
            else:
                k=None
                for b in (os.path.dirname(os.path.abspath(p)),LANE,KNOW):
                    if os.path.isfile(os.path.normpath(os.path.join(b,t))): k="direct"; break
                if k is None:
                    if "/" in t: k="unresolved"
                    else:
                        h=idx.get(os.path.basename(t),[])
                        k="fallback" if len(h)==1 else ("ambiguous" if len(h)>1 else "unresolved")
            tot[k]+=1
print("entries=%d refs=%d"%(len(glob.glob(os.path.join(KNOW,"*","*.md"))),sum(tot.values())))
print(tot, "four=%d"%(tot["direct"]+tot["fallback"]+tot["ambiguous"]+tot["unresolved"]))
```

Output (measured 2026-10-19, baseline `c9f4eaa`, 223 entries):

```
entries=223 refs=2730
{'direct': 2556, 'fallback': 166, 'ambiguous': 0, 'unresolved': 7, 'glob-fragment': 1} four=2729
```

---

## 9. Claim-threshold checklist (this seat's leg)

| threshold (`reports/round-44/claims.json:34`) | status | evidence |
|---|---|---|
| `--selftest` 27/27 green incl. ambiguous, indented-prose-boundary, glob-precedence, wrapped-identity | **PASS** | §1.3: 27 PASS lines, exit 0 |
| census four-class 2556+166+0+7=2729 +1 glob | **PASS** | §2.2-§2.3, §7 stdout; independent §8 |
| every fallback mapping + unresolved reason listed | **PASS** | §3.3: 50 mappings, 166 occurrences, 7 reasoned rows |
| parity receipt filed | not this seat | O07; six-class cross-check in §2.3 is corroborative only |
| the r42 extractor bytes unchanged (`d8d23a26…`) | **PASS** | `sha256sum tools/harness/couples-reference-extractor.py` → `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` |
| ONE census artifact filed | `to-verify` | `reports/round-44/calib/` empty at `2026-10-19T17:21Z`; §6.2 gives the identity + missing fields |

---

## 10. Scope, non-actions, and handoff notes

- Wrote only this out file (`reports/round-44/op/O10-census-verify.md`). Working files stayed under `.scratch/r44-o10/`. No corpus write, no staging, no filed-byte edit, no `run-validation.py`, no git/network/install.
- The census arithmetic is verified against a second implementation; the two agree at the entry level (223/223), not just the totals.
- Two things the integrator must not miss: add `baseline_commit` to the filed census payload (the tool does not emit it), and do not quote `"conservation": true` as zero-drop evidence — carry `extracted_tokens: 2730` (or the manifest digest) from the independent fold. Note the payload's hard-coded `round: 43`.
- If C lands `+1` entry before the census is filed, the census denominator moves to 224: re-run and do not file the 223 numbers against the 224 tree (claims.json:39-46; X00 owns the ordering question).
