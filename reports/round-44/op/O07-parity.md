# O07 — Parity receipt: four-class resolver vs six-class witness

- **Seat:** O07 (verifier, claim O)
- **Round:** 44, baseline commit `c9f4eaa`
- **Claim served:** O — land the r43 O09 verified successor body at `tools/harness/basename-couples-resolver.py` as the single census authority; `tools/harness/couples-reference-extractor.py` demoted to N6 witness (bytes untouched)
- **Owner:** O07, observation time 2026-10-19T14:2xZ (CLI session; commands below re-runnable)
- **Verdict:** **PARITY PASS** — same 223 entries / 2730 refs read by both tools; every token class agrees after exactly the documented subclass mapping (`prospective` → `unresolved`); 0 unexplained token diffs; 0 fallback-mapping mismatches. Both digests and both selftests confirmed.

## 1. Tool identities

| Tool | Path (this run) | Lines | SHA-256 | Status |
|---|---|---|---|---|
| Successor (r43 O09 body) | `.scratch/o07-parity/run/basename-couples-resolver.py` | 515 | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` | new, read-only, stdlib-only |
| Witness (r42) | `tools/harness/couples-reference-extractor.py` | 332 | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` | read-only, bytes unchanged |

Successor extraction (byte-exact from the filed fence, no edits):

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o07-parity/run/basename-couples-resolver.py
$ wc -l .scratch/o07-parity/run/basename-couples-resolver.py
515
$ sha256sum .scratch/o07-parity/run/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
```

Fence: `reports/round-43/op/O09-scribe.md:355` (````python) through `:871` (````); body is lines 356-870 = 515 lines. Digest equals the O09 claim's pinned value at `reports/round-43/op/O09-scribe.md:10` and the landing check at `:887`. Witness digest equals the claim threshold (`d8d23a26…`) and the O09 citation at `:8`.

**Witness-only demotion:** the extractor was opened for reading only in this seat; its mtime and digest are unchanged. Demotion is by record (O04's label + this receipt), never by editing bytes.

## 2. Run environment (and a real hazard found)

Both tools locate the corpus by walking upward to the first `corpus/knowledge`. Before trusting any census, the resolved root must be printed/checked. In this parity run both resolved to the live corpus:

```
resolver LANE : /home/vgpnk/Projects/shokunin/kotodama-shokunin
resolver KNOW : /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge
extractor LANE: /home/vgpnk/Projects/shokunin/kotodama-shokunin
extractor KNOW: /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge
input entries : 223
```

**Shadow trap (observed, not caused by this seat):** `.scratch/o07/` pre-exists as a full repository snapshot (all top-level files, `tools/`, `reports/`, and `corpus/knowledge` with **212** entries, all dated 2026-10-19 08:00). Running the successor from that directory silently reads the snapshot:

```
$ python3 .scratch/o07/basename-couples-resolver.py --census
entries=212 refs=2508
  policy four-class: direct=2337 fallback=163 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
```

That first run is **not** live evidence and is discarded. The shadow directory was left untouched. Consequence for the integrator and for O02/O08: run the census from `tools/harness/` after landing, or from a scratch directory with no `corpus/` ancestor, and confirm `KNOW` points at the repo root — the default text output does not print the resolved root. This is a run-environment hazard, not a defect in the O09 body, and it does not affect the parity result below.

## 3. Counting commands and outputs

Both tools, same shell environment (`PYTHONDONTWRITEBYTECODE=1`), live corpus at 223 entries:

```
$ python3 .scratch/o07-parity/run/basename-couples-resolver.py --selftest
... (27 PASS lines) ...
SELFTEST OK: 27/27 controls          # exit 0
$ python3 .scratch/o07-parity/run/basename-couples-resolver.py --selftest | grep -c '^PASS'
27

$ python3 tools/harness/couples-reference-extractor.py --selftest
... (8 PASS lines) ...               # exit 0
$ python3 tools/harness/couples-reference-extractor.py --selftest | grep -c '^PASS'
8
```

Successor census (live):

```
$ python3 .scratch/o07-parity/run/basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct):
    ... 50 rows, occurrences sum 166 ...
  unresolved (7 rows): ... (see §5)
  ambiguous (0 rows):
  glob-fragment (1 rows):
    -gate.md  corpus/knowledge/verification/gate-frozen-run-standard.md  extractor-artifact  c12=not-applicable
  misaligned: none
```

Witness census (live, read-only):

```
$ python3 tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

Input identity: both read the same 223 paths (`glob(corpus/knowledge/*/*.md)`), the same realpath `KNOW`, and the same 2730 refs. Entries with zero `couples` tokens: **25** in both.

## 4. Parity reconciliation (six-class → four-class)

| Extractor class (r42, six-class) | Count | Resolver class (four-class + artifact) | Count | Separation |
|---|---:|---|---:|---|
| direct | 2556 | direct | 2556 | none |
| fallback | 166 | fallback | 166 | none; 50 distinct mappings, **0** mapping mismatches token-by-token |
| ambiguous | 0 | ambiguous | 0 | none (0 = 0 live) |
| unresolved | 2 | unresolved | 7 | the 5 `prospective` tokens fold in |
| prospective | 5 | *(folded into unresolved)* | — | **documented subclass separation**: four-class has no `prospective` class; each row keeps a disposition reason |
| glob-fragment | 1 | artifact `glob-fragment`, excluded from four-class totals | 1 | **documented artifact separation** (policy §5.6) |

Arithmetic:

```
four-class total = 2556 + 166 + 0 + 7 = 2729
+ quarantined glob artifact            =    1
refs                                   = 2730   (conservation True)
```

This is exactly the claim's required `2556+166+0+7=2729 + 1 glob` over 223/2730.

The 7 unresolved rows, with named dispositions (successor `--census`; extracted-body lines cited as `O09-scribe.md:355+N`):

| Token | Entry | Disposition | c12 |
|---|---|---|---|
| `honorifics-and-register.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed | blocker |
| `naming-and-onomastics.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed | blocker |
| `phonology-basics.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed | blocker |
| `sound-change.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | declared-prospective-seed | blocker |
| `tone-prosody.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | declared-prospective-seed | blocker |
| `../linguistics/phonology-sanity.md` | `corpus/knowledge/synthesis/typed-label-routing-workflow.md` | dangling-reference | blocker |
| `../linguistics/phonology-sanity.md` | `corpus/knowledge/verification/label-channel-routing-verification.md` | dangling-reference | blocker |

Glob artifact row: `-gate.md` in `corpus/knowledge/verification/gate-frozen-run-standard.md` → `extractor-artifact`, `c12=not-applicable`.

The 50 fallback mappings (distinct refs; 166 occurrences). Target paths are printed by the successor's `--census` (50 rows) and belong in O06's filed artifact; this receipt verified the target of every fallback token is identical between the two tools (0 mismatches):

```
adornment-body-codes.md, animal-symbolism.md, architecture-settlement-lexicon.md,
calendar-festival-systems.md, calibration-registry.md, color-symbolism.md,
comparative-frameworks.md, consistency-verification-checklist.md, cosmology-cosmography.md,
costume-semiotics.md, coupling-model.md, creation-myths-taxonomy.md, dress-through-eras.md,
era-language-staging.md, era-periodization-models.md, garment-lexicon-crosslinguistic.md,
historical-linguistics.md, inca.md, kinship-terminology.md, language-contact.md,
lexicon-coverage-audit.md, loanword-material-dating.md, material-culture-inference-method.md,
maya-classic.md, mesopotamia-sumer-akkad.md, morphological-typology.md,
music-instrument-lexicon.md, myth-ritual-theories.md, myth-to-language-derivation.md,
naming-systems.md, number-symbolism.md, orality-formulaic-language.md, pantheon-archetypes.md,
phonetics-phonology.md, politeness-taboo-euphemism.md, real-world-inspiration-boundaries.md,
register-strata-attestation.md, religion-language-co-evolution.md, ritual-garments.md,
ritual-liminality.md, semantics-pragmatics.md, sociolinguistics-registers.md,
source-discipline-calibration.md, sumptuary-law-rank-display.md, symbolism-synthesis-method.md,
taboo-euphemism-lifecycle.md, textile-technology.md, trade-economy-lexicon.md,
warrior-material-culture.md, writing-systems.md
```

## 5. Token-level diff proof (differences are *only* the subclass separation)

Method: import both modules in one process, resolve every live entry with both, and compare per-entry token sets, classes, mappings and alignment flags. Reported classes are mapped through the single documented substitution `prospective → unresolved`; anything else is a diff.

```
$ python3 .scratch/o07-parity/compare.py
extractor class totals: {'direct': 2556, 'fallback': 166, 'glob-fragment': 1, 'prospective': 5, 'unresolved': 2}
resolver  class totals: {'direct': 2556, 'fallback': 166, 'glob-fragment': 1, 'unresolved': 7}
class-pair table (extractor -> resolver):
  direct         -> direct        2556
  fallback       -> fallback       166
  glob-fragment  -> glob-fragment    1
  prospective    -> unresolved       5
  unresolved     -> unresolved       2

token/detail diffs after documented subclass mapping: 0
fallback mapping mismatches: 0
entries with zero couples tokens: 25
conservation extractor: 2730
conservation resolver : 2730
```

No token differs in class, mapping, or alignment; no entry differs in token set or `wrapped` flag. The entire delta between the tools is the two documented separations above.

Wrapped-field identity check (claim: 4/4 by identity, not arity):

```
$ python3 .scratch/o07-parity/run/basename-couples-resolver.py corpus/knowledge/linguistics/phonetics-phonology.md
... wrapped=True tokens=4
    sound-change.md       unresolved  declared-prospective-seed
    sound-symbolism.md    direct
    tone-prosody.md       unresolved  declared-prospective-seed
    writing-systems.md    direct

$ python3 tools/harness/couples-reference-extractor.py corpus/knowledge/linguistics/phonetics-phonology.md
... wrapped=True tokens=4
    sound-change.md       prospective
    sound-symbolism.md    direct
    tone-prosody.md       prospective
    writing-systems.md    direct
```

Both read the four distinct tokens — none dropped, none split (`prosody.md` / `toneprosody.md` never appear).

## 6. Differences that are *not* subclass separation — latency only, zero live effect

These are implementation deltas between the witness and the successor that produce **no** difference on the live corpus (the diff above is 0), and are covered by the successor's selftest:

1. **Glob precedence.** Witness checks the basename/ambiguous branch before `glob-fragment` (`tools/harness/couples-reference-extractor.py:141-147`); successor checks `glob-fragment` before the slash/unresolved and basename branches (`O09-scribe.md:504`, body line 149), so a glob token that collides with a basename cannot be mislabeled ambiguous. Live `ambiguous=0`, so no observed delta; control S8b passes (`O09-scribe.md:777`).
2. **Blank-line termination.** Witness skips blank lines and keeps capturing later indented lines (`couples-reference-extractor.py:63-70`, `continue` at :65); successor terminates the block at a blank line unless the previous part ends in a hyphen soft wrap (`O09-scribe.md:424`, body line 69). Live effect: 0 token diffs — the over-capture is a latent trap, proven by fixture S7c, not by a current corpus row. Stated exactly: the successor's control is green; no live entry currently manifests the over-capture.
3. **Prospective scope.** Witness applies `prospective` as an entry-level flag to every unresolvable token (`couples-reference-extractor.py:159,164`); successor derives disposition per token from the token's position relative to the prospective marker (`O09-scribe.md:541`, body line 186). Live effect: 0 — the same 5 tokens land in the same class on both.
4. **Ambiguous coverage.** Witness `--selftest` has no ambiguous control (its 8 checks are wrapped/unwrapped/over-capture/phantom/N6×2/glob); successor adds S3a/S3b (`O09-scribe.md:499` region; selftest 27/27). Live `ambiguous=0` on both, so ambiguous parity is 0=0 and rests on the successor's control.

## 7. Reproducibility

The comparison harness lived at `.scratch/o07-parity/compare.py` (scratch, not durable). To re-run after scratch cleanup:

1. `sed -n '356,870p' reports/round-43/op/O09-scribe.md > <clean-dir>/basename-couples-resolver.py`; confirm sha256 `43ce341f…`.
2. Place `<clean-dir>` where walking upward reaches the repo root without passing a `corpus/knowledge` (e.g. `.scratch/o07-parity/run/`); assert the module's `KNOW` realpath is `<repo>/corpus/knowledge`.
3. Load both modules via `importlib`, call each `resolve_entry(path)` over `sorted(glob(<KNOW>/*/*.md))`, and diff `(class, mapping, alignment)` per token with the map `{"prospective": "unresolved"}`.
4. Expect: 223 entries, 2730 refs, class-pair table as in §5, 0 diffs.

Machine-readable successor census captured this run at `.scratch/o07-parity/census.json` (`schema=kotodama-couples-census-v3`, `entries=223`, `refs=2730`, `four_class_totals={direct:2556,fallback:166,ambiguous:0,unresolved:7}`, `artifact_totals={glob-fragment:1}`, `conservation=true`, `fallback_mappings=50`, disposition rows 7/0/1). **This scratch JSON is parity evidence only — it is not the filed census artifact.** The durable artifact (O06) must be generated after landing, from `tools/harness/basename-couples-resolver.py`, so its `tool` field reads that path; note the body's `--json` also hardcodes `"round": 43` as body provenance (`reports/round-43/op/O09-scribe.md:816`) and pins `schema` at `:815`, while `tool_sha256` is computed from the file actually run (`:819`).

**Denominator ordering (223 vs 224).** Every number in this receipt is at baseline `c9f4eaa` with the 223-entry partition. Claim C lands a 224th entry; if the O census artifact is regenerated after C's landing, the totals will legitimately move (the new entry's `couples` tokens enter the classes). The claim threshold `2556+166+0+7` is a 223-entry denominator, so the O artifact must pin `baseline_commit: c9f4eaa` and `entries: 223`; if a post-C census is also filed, name both denominators and the ordering rather than comparing a 224-entry run against the 223-entry threshold. O03 raises the same ordering caveat.

**Independent agreement.** O02 reports the same 27/27 and the same `entries=223 refs=2730` / `2556+166+0+7` + 1 glob (`reports/round-44/op/O02-verify.md:11,156-159`), and O03 reports the same totals and the six-class equivalence `2556+166+0+2+5+1 = 2556+166+0+7+1 = 2730` (`reports/round-44/op/O03-defects-verify.md:177-180,216`). No verifier contradicts this parity receipt.

## 8. Claim-threshold checklist (parity scope)

| Threshold element | Status | Evidence |
|---|---|---|
| successor durable body at claim path, sha256 `43ce341f…` | verified at extraction; landing is the integrator's apply | §1 |
| `--selftest` 27/27 green | PASS | §3 |
| four-class census `2556+166+0+7=2729` + 1 glob = 2730 | PASS | §3, §4 |
| every fallback mapping listed (50 distinct) | PASS | §4 |
| every unresolved/ambiguous row reasoned | PASS (7 unresolved rows with dispositions; 0 ambiguous) | §4 |
| wrapped field 4/4 by identity | PASS on both tools | §5 |
| same 223/2730 input, differences solely subclass separation | PASS (0 unexplained diffs) | §3, §5 |
| r42 extractor bytes unchanged `d8d23a26…` | PASS (read-only; digest unchanged) | §1 |

**Verdict: the successor is a faithful successor.** On the live 223-entry corpus the four-class resolver accounts for every token the six-class witness accounts for; the only deltas are (a) `prospective` folded into `unresolved` with a named disposition and (b) the glob fragment quarantined as an artifact, both of which are the policy's documented four-class shape. Witness demotion is by record only; its bytes were not touched.
