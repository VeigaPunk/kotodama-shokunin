# O06 — census artifact: exact `couples-census-r44.json`

- Seat: O06 | executor | claim O | date 2026-10-19 | baseline `c9f4eaa`
- Mission (`reports/round-44/targets.json:23`): "the exact calib/couples-census
  JSON the integrator files — four-class totals 2556+166+0+7=2729 +1 quarantined
  glob, the 50 distinct fallback mappings, the 7 unresolved rows with reasons,
  conservation identity, baseline_commit + entries header."
- **Deliverable: §5.** The JSON block is generated programmatically from the
  landed body's own `--census --json` output; it is not hand-typed. All twelve
  derivation invariants asserted by the assembly script are `true` (§2). The
  file name this seat binds is `reports/round-44/calib/couples-census-r44.json`
  — **one artifact, one name** (the r43 F4 conflict is not repeated).

No filed byte was edited. No corpus byte was staged. No `run-validation.py`
was executed. No git/network/install action was taken. Scratch lives only under
`.scratch/o06c/`.

## 1. What was run, and the shadow trap that had to be cleared

The body was extracted from `reports/round-43/op/O09-scribe.md:356-870`:

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > body.py
$ wc -l body.py && sha256sum body.py
515 body.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  body.py
```

The sha256 matches the claim's `43ce341f…`. But the first extraction landed in
`.scratch/o06/`, which is **not an empty scratch directory**: it is a
pre-existing lane clone with its own `corpus/knowledge` (212 entries). The
body's root search (`HERE` -> upward until a `corpus/knowledge` directory
exists) stopped there, not at the live lane root:

```
$ python3 -B -c '... import body ...; print(LANE, KNOW)'
LANE /home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/o06
KNOW /home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/o06/corpus/knowledge
$ python3 -B body.py --census
entries=212 refs=2508
  policy four-class: direct=2337 fallback=163 ambiguous=0 unresolved=7
```

That is the exact hazard `reports/round-44/targets.json:19` names for the
independent verifier ("no corpus shadow above it"). Re-extracted to
`.scratch/o06c/`, whose ancestors contain no `corpus/` directory, the root
search lands on the live lane:

```
$ python3 -B -c '... import body ...; print(LANE, KNOW)'
LANE /home/vgpnk/Projects/shokunin/kotodama-shokunin
KNOW /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge
```

All numbers below are from that clean run (2026-10-19T17:22Z, HEAD
`c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`).

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ python3 -B .scratch/o06c/basename-couples-resolver.py --selftest
...
PASS S10 live wrapped entry reads 4 tokens (2 direct + 2 unresolved)
SELFTEST OK: 27/27 controls          # rc=0
$ python3 -B .scratch/o06c/basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct):
  ...
  unresolved (7 rows):
    ... 7 named rows, each with a disposition and c12 flag
  ambiguous (0 rows):
  glob-fragment (1 rows):
    -gate.md  corpus/knowledge/verification/gate-frozen-run-standard.md  extractor-artifact  c12=not-applicable
  misaligned: none
```

The census was captured twice: text stdout (`.scratch/o06c/census-stdout.txt`)
and structured JSON (`.scratch/o06c/census-raw.json`, 586844 bytes, sha256
`ef90ef86ec4381019a8d135ecb8c9df2a6a234c91b7e2d8481cde82ca3349c03`). The artifact in §5 is derived from the structured JSON.

## 2. Conservation identity and the derivation checks

```
2556 direct + 166 fallback + 0 ambiguous + 7 unresolved = 2729
2729 + 1 quarantined glob-fragment                       = 2730 refs
```

The 2729 is the policy four-class total; the glob fragment is reported beside
it, never folded in, per policy §5.6
(`reports/round-42/calib/basename-couples-policy-full.md:99-104`). The
quarantine rule is operational at `basename-couples-resolver.py:150-151`
(glob check precedes the ambiguous branch), the four classes at `:140-141`.

Every check in the filed JSON is a computed boolean, not a claim:

- `I1_entries_equal_entries_detail`: PASS
- `I2_refs_equal_sum_per_entry_tokens`: PASS
- `I3_four_plus_artifacts_equal_refs`: PASS
- `I4_fallback_occurrences_equal_four_fallback`: PASS
- `I5_distinct_fallbacks_equal_mapping_rows`: PASS
- `I6_unresolved_rows_equal_four_unresolved`: PASS
- `I7_ambiguous_rows_equal_four_ambiguous`: PASS
- `I8_glob_rows_equal_artifact_totals`: PASS
- `I9_every_unresolved_row_has_reason`: PASS
- `I10_every_fallback_mapping_exists`: PASS
- `I11_wrapped_field_reads_4_tokens`: PASS
- `I12_unaccounted_zero`: PASS

Additional derivations carried in the artifact:

- wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md`,
  **4/4 tokens by identity** (`sound-change.md`, `tone-prosody.md` unresolved;
  `sound-symbolism.md`, `writing-systems.md` direct), not by arity — the
  body's S1b control is `27/27`.
- `fallback_occurrences` = 166 = `four_class_totals.fallback`; every one of the
  50 mapping paths exists on disk (`I10`).
- `unaccounted` = 0; the per-entry token sum is 2730 (`I2`). 25 entries carry
  no `couples:` tokens at all — measured, not dropped (the tool lists every
  entry in `entries_detail`).
- `misaligned: []`; no fallback row is an alignment finding.

## 3. The 7 unresolved rows (verbatim reasons from the tool)

| row | entry | token | disposition | c12 | documented |
|---|---|---|---|---|---|
| `U-001` | `linguistics/language-contact.md` | `honorifics-and-register.md` | `declared-prospective-seed` | `blocker` | `documented=false` |
| `U-002` | `linguistics/language-contact.md` | `naming-and-onomastics.md` | `declared-prospective-seed` | `blocker` | `documented=false` |
| `U-003` | `linguistics/language-contact.md` | `phonology-basics.md` | `declared-prospective-seed` | `blocker` | `documented=false` |
| `U-004` | `linguistics/phonetics-phonology.md` | `sound-change.md` | `declared-prospective-seed` | `blocker` | `documented=false` |
| `U-005` | `linguistics/phonetics-phonology.md` | `tone-prosody.md` | `declared-prospective-seed` | `blocker` | `documented=false` |
| `U-006` | `synthesis/typed-label-routing-workflow.md` | `../linguistics/phonology-sanity.md` | `dangling-reference` | `blocker` | `documented=false` |
| `U-007` | `verification/label-channel-routing-verification.md` | `../linguistics/phonology-sanity.md` | `dangling-reference` | `blocker` | `documented=false` |

Grouping: 5 `declared-prospective-seed` (the fields say "prospective sibling
files:" / "files to seed") and 2 `dangling-reference` (slash-bearing
`../linguistics/phonology-sanity.md`; no such file exists). Every row carries a
non-empty `reason` and is named in `disposition.unresolved`; none is dropped.
All 7 read `c12=blocker` because `documented=false` (no `(to-verify` marker on
the token's own part) — that is the C12 rule's output, not a seat judgment.

## 4. The 50 distinct fallback mappings

`occurrences` is the token's raw occurrence count across entries; `carriers` is
the number of distinct entries. The JSON carries the full carrier path list per
row. Mapping paths are shown relative to `corpus/knowledge/`.

| token | -> mapping (under corpus/knowledge/) | occurrences | carriers |
|---|---|---|---|
| `adornment-body-codes.md` | `culture-material/adornment-body-codes.md` | 2 | 2 |
| `animal-symbolism.md` | `myth-symbol/animal-symbolism.md` | 1 | 1 |
| `architecture-settlement-lexicon.md` | `culture-material/architecture-settlement-lexicon.md` | 4 | 4 |
| `calendar-festival-systems.md` | `culture-material/calendar-festival-systems.md` | 2 | 2 |
| `calibration-registry.md` | `verification/calibration-registry.md` | 2 | 2 |
| `color-symbolism.md` | `myth-symbol/color-symbolism.md` | 3 | 3 |
| `comparative-frameworks.md` | `myth-symbol/comparative-frameworks.md` | 4 | 4 |
| `consistency-verification-checklist.md` | `synthesis/consistency-verification-checklist.md` | 1 | 1 |
| `cosmology-cosmography.md` | `myth-symbol/cosmology-cosmography.md` | 2 | 2 |
| `costume-semiotics.md` | `culture-material/costume-semiotics.md` | 8 | 8 |
| `coupling-model.md` | `synthesis/coupling-model.md` | 1 | 1 |
| `creation-myths-taxonomy.md` | `myth-symbol/creation-myths-taxonomy.md` | 1 | 1 |
| `dress-through-eras.md` | `culture-material/dress-through-eras.md` | 5 | 5 |
| `era-language-staging.md` | `synthesis/era-language-staging.md` | 1 | 1 |
| `era-periodization-models.md` | `culture-material/era-periodization-models.md` | 1 | 1 |
| `garment-lexicon-crosslinguistic.md` | `culture-material/garment-lexicon-crosslinguistic.md` | 3 | 3 |
| `historical-linguistics.md` | `linguistics/historical-linguistics.md` | 9 | 9 |
| `inca.md` | `civilizations/inca.md` | 1 | 1 |
| `kinship-terminology.md` | `linguistics/kinship-terminology.md` | 1 | 1 |
| `language-contact.md` | `linguistics/language-contact.md` | 10 | 10 |
| `lexicon-coverage-audit.md` | `verification/lexicon-coverage-audit.md` | 1 | 1 |
| `loanword-material-dating.md` | `synthesis/loanword-material-dating.md` | 1 | 1 |
| `material-culture-inference-method.md` | `culture-material/material-culture-inference-method.md` | 10 | 10 |
| `maya-classic.md` | `civilizations/maya-classic.md` | 1 | 1 |
| `mesopotamia-sumer-akkad.md` | `civilizations/mesopotamia-sumer-akkad.md` | 1 | 1 |
| `morphological-typology.md` | `linguistics/morphological-typology.md` | 2 | 2 |
| `music-instrument-lexicon.md` | `culture-material/music-instrument-lexicon.md` | 1 | 1 |
| `myth-ritual-theories.md` | `myth-symbol/myth-ritual-theories.md` | 1 | 1 |
| `myth-to-language-derivation.md` | `synthesis/myth-to-language-derivation.md` | 1 | 1 |
| `naming-systems.md` | `linguistics/naming-systems.md` | 14 | 14 |
| `number-symbolism.md` | `myth-symbol/number-symbolism.md` | 1 | 1 |
| `orality-formulaic-language.md` | `linguistics/orality-formulaic-language.md` | 4 | 4 |
| `pantheon-archetypes.md` | `myth-symbol/pantheon-archetypes.md` | 5 | 5 |
| `phonetics-phonology.md` | `linguistics/phonetics-phonology.md` | 1 | 1 |
| `politeness-taboo-euphemism.md` | `linguistics/politeness-taboo-euphemism.md` | 2 | 2 |
| `real-world-inspiration-boundaries.md` | `verification/real-world-inspiration-boundaries.md` | 2 | 2 |
| `register-strata-attestation.md` | `linguistics/register-strata-attestation.md` | 1 | 1 |
| `religion-language-co-evolution.md` | `synthesis/religion-language-co-evolution.md` | 1 | 1 |
| `ritual-garments.md` | `culture-material/ritual-garments.md` | 6 | 6 |
| `ritual-liminality.md` | `myth-symbol/ritual-liminality.md` | 2 | 2 |
| `semantics-pragmatics.md` | `linguistics/semantics-pragmatics.md` | 3 | 3 |
| `sociolinguistics-registers.md` | `linguistics/sociolinguistics-registers.md` | 7 | 7 |
| `source-discipline-calibration.md` | `synthesis/source-discipline-calibration.md` | 1 | 1 |
| `sumptuary-law-rank-display.md` | `culture-material/sumptuary-law-rank-display.md` | 3 | 3 |
| `symbolism-synthesis-method.md` | `myth-symbol/symbolism-synthesis-method.md` | 10 | 10 |
| `taboo-euphemism-lifecycle.md` | `synthesis/taboo-euphemism-lifecycle.md` | 1 | 1 |
| `textile-technology.md` | `culture-material/textile-technology.md` | 4 | 4 |
| `trade-economy-lexicon.md` | `culture-material/trade-economy-lexicon.md` | 3 | 3 |
| `warrior-material-culture.md` | `culture-material/warrior-material-culture.md` | 1 | 1 |
| `writing-systems.md` | `linguistics/writing-systems.md` | 13 | 13 |

Sum of `occurrences` = 166, the fallback class total. 50 distinct tokens; all
50 target files resolve (`I10`).

## 5. The exact JSON the integrator files

Path: `reports/round-44/calib/couples-census-r44.json`
(sha256 of this exact block: `c0ee791a89883f0958c62fb46755397a6c8f8f64f0a26e1c31227b30b4940699`; `content_sha256` `3ee551fca0b5c88f8dacdf37a544fcd658a23bb7619c9f38501299f773d896a9`).

````json
{
 "schema": "kotodama-couples-census-v4",
 "round": 44,
 "claim": "O",
 "date": "2026-10-19",
 "artifact": "reports/round-44/calib/couples-census-r44.json",
 "baseline_commit": "c9f4eaa707b6e977ff6e1616463e91f4b8afea5d",
 "entries": 223,
 "refs": 2730,
 "policy": {
  "path": "reports/round-42/calib/basename-couples-policy-full.md",
  "sha256": "8c3d7c356ea7c1df3bcaab414ccc2035f6dc90272aaed305e4edf35b2890cdd6",
  "status": "full successor of the truncated r39 filing; four-class rule source"
 },
 "tool": {
  "path": "tools/harness/basename-couples-resolver.py",
  "sha256": "43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64",
  "run_path": ".scratch/o06c/basename-couples-resolver.py",
  "source": "reports/round-43/op/O09-scribe.md:356-870",
  "selftest": "27/27 PASS (python3 -B <run_path> --selftest, rc=0)",
  "role": "single census authority",
  "witness": {
   "path": "tools/harness/couples-reference-extractor.py",
   "sha256": "d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1",
   "role": "N6 regression witness only; bytes untouched; not the census authority"
  }
 },
 "corpus": {
  "entries": 223,
  "partitions": {
   "civilizations": 94,
   "culture-material": 25,
   "linguistics": 25,
   "myth-symbol": 26,
   "synthesis": 29,
   "verification": 24
  },
  "index_scope": "corpus/knowledge/*/*.md",
  "corpus_fingerprint": "7675c7246cf0ac62072d083443fba6b9b699e6108f100476284e44c0972953ba",
  "fingerprint_rule": "sha256 over sorted '<repo-relative-path>:<file-sha256>\\n' lines",
  "state_note": "223-entry tree at c9f4eaa, pre-C landing; claim C's +1 is a separate, later corpus change - re-run --census after a lawful landing; never hand-adjust this artifact"
 },
 "four_class_totals": {
  "ambiguous": 0,
  "direct": 2556,
  "fallback": 166,
  "unresolved": 7
 },
 "artifact_totals": {
  "glob-fragment": 1
 },
 "conservation": {
  "four_class_sum": 2729,
  "artifact_sum": 1,
  "refs": 2730,
  "identity": "2556+166+0+7 + 1 == 2730",
  "holds": true,
  "unaccounted": 0,
  "zero_token_entries": 25
 },
 "wrapped_fields": {
  "count": 1,
  "paths": [
   "corpus/knowledge/linguistics/phonetics-phonology.md"
  ],
  "token_count": 4,
  "tokens_by_class": {
   "sound-change.md": "unresolved",
   "sound-symbolism.md": "direct",
   "tone-prosody.md": "unresolved",
   "writing-systems.md": "direct"
  },
  "identity_note": "4/4 tokens by identity (token names), not by arity"
 },
 "misaligned": [],
 "fallback_mappings": [
  {
   "token": "adornment-body-codes.md",
   "mapping": "corpus/knowledge/culture-material/adornment-body-codes.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "animal-symbolism.md",
   "mapping": "corpus/knowledge/myth-symbol/animal-symbolism.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/civilizations/china-qing.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "architecture-settlement-lexicon.md",
   "mapping": "corpus/knowledge/culture-material/architecture-settlement-lexicon.md",
   "occurrences": 4,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md",
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "calendar-festival-systems.md",
   "mapping": "corpus/knowledge/culture-material/calendar-festival-systems.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "calibration-registry.md",
   "mapping": "corpus/knowledge/verification/calibration-registry.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/linguistics/sound-symbolism.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "color-symbolism.md",
   "mapping": "corpus/knowledge/myth-symbol/color-symbolism.md",
   "occurrences": 3,
   "entries": [
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "comparative-frameworks.md",
   "mapping": "corpus/knowledge/myth-symbol/comparative-frameworks.md",
   "occurrences": 4,
   "entries": [
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md",
    "corpus/knowledge/verification/citation-format-and-source-registry.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "consistency-verification-checklist.md",
   "mapping": "corpus/knowledge/synthesis/consistency-verification-checklist.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "cosmology-cosmography.md",
   "mapping": "corpus/knowledge/myth-symbol/cosmology-cosmography.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/china-qing.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "costume-semiotics.md",
   "mapping": "corpus/knowledge/culture-material/costume-semiotics.md",
   "occurrences": 8,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md",
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md",
    "corpus/knowledge/verification/naming-collision-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "coupling-model.md",
   "mapping": "corpus/knowledge/synthesis/coupling-model.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "creation-myths-taxonomy.md",
   "mapping": "corpus/knowledge/myth-symbol/creation-myths-taxonomy.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/civilizations/persia-sasanian.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "dress-through-eras.md",
   "mapping": "corpus/knowledge/culture-material/dress-through-eras.md",
   "occurrences": 5,
   "entries": [
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/citation-format-and-source-registry.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "era-language-staging.md",
   "mapping": "corpus/knowledge/synthesis/era-language-staging.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/sacred-registers-liturgical-language.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "era-periodization-models.md",
   "mapping": "corpus/knowledge/culture-material/era-periodization-models.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/civilizations/china-qing.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "garment-lexicon-crosslinguistic.md",
   "mapping": "corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md",
   "occurrences": 3,
   "entries": [
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md",
    "corpus/knowledge/verification/naming-collision-gate.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "historical-linguistics.md",
   "mapping": "corpus/knowledge/linguistics/historical-linguistics.md",
   "occurrences": 9,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md",
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/culture-material/dress-through-eras.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/naming-collision-gate.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "inca.md",
   "mapping": "corpus/knowledge/civilizations/inca.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "kinship-terminology.md",
   "mapping": "corpus/knowledge/linguistics/kinship-terminology.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "language-contact.md",
   "mapping": "corpus/knowledge/linguistics/language-contact.md",
   "occurrences": 10,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md",
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/culture-material/costume-semiotics.md",
    "corpus/knowledge/culture-material/textile-technology.md",
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md",
    "corpus/knowledge/verification/naming-collision-gate.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "lexicon-coverage-audit.md",
   "mapping": "corpus/knowledge/verification/lexicon-coverage-audit.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "loanword-material-dating.md",
   "mapping": "corpus/knowledge/synthesis/loanword-material-dating.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "material-culture-inference-method.md",
   "mapping": "corpus/knowledge/culture-material/material-culture-inference-method.md",
   "occurrences": 10,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md",
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/citation-format-and-source-registry.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "maya-classic.md",
   "mapping": "corpus/knowledge/civilizations/maya-classic.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "mesopotamia-sumer-akkad.md",
   "mapping": "corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "morphological-typology.md",
   "mapping": "corpus/knowledge/linguistics/morphological-typology.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/verification/naming-collision-gate.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "music-instrument-lexicon.md",
   "mapping": "corpus/knowledge/culture-material/music-instrument-lexicon.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/sound-symbolism.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "myth-ritual-theories.md",
   "mapping": "corpus/knowledge/myth-symbol/myth-ritual-theories.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "myth-to-language-derivation.md",
   "mapping": "corpus/knowledge/synthesis/myth-to-language-derivation.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/sound-symbolism.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "naming-systems.md",
   "mapping": "corpus/knowledge/linguistics/naming-systems.md",
   "occurrences": 14,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md",
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/citation-format-and-source-registry.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "number-symbolism.md",
   "mapping": "corpus/knowledge/myth-symbol/number-symbolism.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/numerals-and-measures.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "orality-formulaic-language.md",
   "mapping": "corpus/knowledge/linguistics/orality-formulaic-language.md",
   "occurrences": 4,
   "entries": [
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "pantheon-archetypes.md",
   "mapping": "corpus/knowledge/myth-symbol/pantheon-archetypes.md",
   "occurrences": 5,
   "entries": [
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/naming-collision-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "phonetics-phonology.md",
   "mapping": "corpus/knowledge/linguistics/phonetics-phonology.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/verification/naming-collision-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "politeness-taboo-euphemism.md",
   "mapping": "corpus/knowledge/linguistics/politeness-taboo-euphemism.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/verification/naming-collision-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "real-world-inspiration-boundaries.md",
   "mapping": "corpus/knowledge/verification/real-world-inspiration-boundaries.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/linguistics/sacred-registers-liturgical-language.md",
    "corpus/knowledge/linguistics/sound-symbolism.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "register-strata-attestation.md",
   "mapping": "corpus/knowledge/linguistics/register-strata-attestation.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "religion-language-co-evolution.md",
   "mapping": "corpus/knowledge/synthesis/religion-language-co-evolution.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/sacred-registers-liturgical-language.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "ritual-garments.md",
   "mapping": "corpus/knowledge/culture-material/ritual-garments.md",
   "occurrences": 6,
   "entries": [
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "ritual-liminality.md",
   "mapping": "corpus/knowledge/myth-symbol/ritual-liminality.md",
   "occurrences": 2,
   "entries": [
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "semantics-pragmatics.md",
   "mapping": "corpus/knowledge/linguistics/semantics-pragmatics.md",
   "occurrences": 3,
   "entries": [
    "corpus/knowledge/culture-material/costume-semiotics.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "sociolinguistics-registers.md",
   "mapping": "corpus/knowledge/linguistics/sociolinguistics-registers.md",
   "occurrences": 7,
   "entries": [
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "source-discipline-calibration.md",
   "mapping": "corpus/knowledge/synthesis/source-discipline-calibration.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/sound-symbolism.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "sumptuary-law-rank-display.md",
   "mapping": "corpus/knowledge/culture-material/sumptuary-law-rank-display.md",
   "occurrences": 3,
   "entries": [
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "symbolism-synthesis-method.md",
   "mapping": "corpus/knowledge/myth-symbol/symbolism-synthesis-method.md",
   "occurrences": 10,
   "entries": [
    "corpus/knowledge/civilizations/aegean-minoan-mycenaean.md",
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/citation-format-and-source-registry.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "taboo-euphemism-lifecycle.md",
   "mapping": "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/linguistics/sound-symbolism.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "textile-technology.md",
   "mapping": "corpus/knowledge/culture-material/textile-technology.md",
   "occurrences": 4,
   "entries": [
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "trade-economy-lexicon.md",
   "mapping": "corpus/knowledge/culture-material/trade-economy-lexicon.md",
   "occurrences": 3,
   "entries": [
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/linguistics/numerals-and-measures.md",
    "corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "warrior-material-culture.md",
   "mapping": "corpus/knowledge/culture-material/warrior-material-culture.md",
   "occurrences": 1,
   "entries": [
    "corpus/knowledge/civilizations/java-majapahit.md"
   ],
   "mapping_exists": true
  },
  {
   "token": "writing-systems.md",
   "mapping": "corpus/knowledge/linguistics/writing-systems.md",
   "occurrences": 13,
   "entries": [
    "corpus/knowledge/civilizations/ancestral-puebloan.md",
    "corpus/knowledge/civilizations/arabia-pre-islamic.md",
    "corpus/knowledge/civilizations/australia-aboriginal.md",
    "corpus/knowledge/civilizations/china-qing.md",
    "corpus/knowledge/civilizations/japan-yayoi-kofun.md",
    "corpus/knowledge/civilizations/java-majapahit.md",
    "corpus/knowledge/civilizations/persia-sasanian.md",
    "corpus/knowledge/synthesis/symbol-lexicon-colexification.md",
    "corpus/knowledge/synthesis/symbolism-consistency-rules.md",
    "corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md",
    "corpus/knowledge/verification/citation-format-and-source-registry.md",
    "corpus/knowledge/verification/naming-collision-gate.md",
    "corpus/knowledge/verification/phonology-sanity-gate.md"
   ],
   "mapping_exists": true
  }
 ],
 "fallback_mapping_count": 50,
 "fallback_occurrences": 166,
 "unresolved": [
  {
   "row_id": "U-001",
   "entry": "corpus/knowledge/linguistics/language-contact.md",
   "token": "honorifics-and-register.md",
   "class": "unresolved",
   "disposition": "declared-prospective-seed",
   "reason": "declared prospective/sibling-seed token in the couples field; never written, not a referenced entry",
   "c12": "blocker",
   "mapping": null,
   "documented": false
  },
  {
   "row_id": "U-002",
   "entry": "corpus/knowledge/linguistics/language-contact.md",
   "token": "naming-and-onomastics.md",
   "class": "unresolved",
   "disposition": "declared-prospective-seed",
   "reason": "declared prospective/sibling-seed token in the couples field; never written, not a referenced entry",
   "c12": "blocker",
   "mapping": null,
   "documented": false
  },
  {
   "row_id": "U-003",
   "entry": "corpus/knowledge/linguistics/language-contact.md",
   "token": "phonology-basics.md",
   "class": "unresolved",
   "disposition": "declared-prospective-seed",
   "reason": "declared prospective/sibling-seed token in the couples field; never written, not a referenced entry",
   "c12": "blocker",
   "mapping": null,
   "documented": false
  },
  {
   "row_id": "U-004",
   "entry": "corpus/knowledge/linguistics/phonetics-phonology.md",
   "token": "sound-change.md",
   "class": "unresolved",
   "disposition": "declared-prospective-seed",
   "reason": "declared prospective/sibling-seed token in the couples field; never written, not a referenced entry",
   "c12": "blocker",
   "mapping": null,
   "documented": false
  },
  {
   "row_id": "U-005",
   "entry": "corpus/knowledge/linguistics/phonetics-phonology.md",
   "token": "tone-prosody.md",
   "class": "unresolved",
   "disposition": "declared-prospective-seed",
   "reason": "declared prospective/sibling-seed token in the couples field; never written, not a referenced entry",
   "c12": "blocker",
   "mapping": null,
   "documented": false
  },
  {
   "row_id": "U-006",
   "entry": "corpus/knowledge/synthesis/typed-label-routing-workflow.md",
   "token": "../linguistics/phonology-sanity.md",
   "class": "unresolved",
   "disposition": "dangling-reference",
   "reason": "Tier 1 failed and the token is not eligible for the unique-basename fallback (slash-bearing or zero index hits)",
   "c12": "blocker",
   "mapping": null,
   "documented": false
  },
  {
   "row_id": "U-007",
   "entry": "corpus/knowledge/verification/label-channel-routing-verification.md",
   "token": "../linguistics/phonology-sanity.md",
   "class": "unresolved",
   "disposition": "dangling-reference",
   "reason": "Tier 1 failed and the token is not eligible for the unique-basename fallback (slash-bearing or zero index hits)",
   "c12": "blocker",
   "mapping": null,
   "documented": false
  }
 ],
 "unresolved_summary": {
  "declared-prospective-seed": 5,
  "dangling-reference": 2,
  "total": 7
 },
 "ambiguous": [],
 "glob_fragment": [
  {
   "entry": "corpus/knowledge/verification/gate-frozen-run-standard.md",
   "token": "-gate.md",
   "class": "glob-fragment",
   "disposition": "extractor-artifact",
   "reason": "glob pattern fragment (policy 5.6): extractor artifact, not a couples finding",
   "c12": "not-applicable",
   "source_policy": "policy 5.6: glob fragments are extractor artifacts, never couples findings"
  }
 ],
 "checks": {
  "I1_entries_equal_entries_detail": true,
  "I2_refs_equal_sum_per_entry_tokens": true,
  "I3_four_plus_artifacts_equal_refs": true,
  "I4_fallback_occurrences_equal_four_fallback": true,
  "I5_distinct_fallbacks_equal_mapping_rows": true,
  "I6_unresolved_rows_equal_four_unresolved": true,
  "I7_ambiguous_rows_equal_four_ambiguous": true,
  "I8_glob_rows_equal_artifact_totals": true,
  "I9_every_unresolved_row_has_reason": true,
  "I10_every_fallback_mapping_exists": true,
  "I11_wrapped_field_reads_4_tokens": true,
  "I12_unaccounted_zero": true
 },
 "tool_payload": {
  "sha256": "ef90ef86ec4381019a8d135ecb8c9df2a6a234c91b7e2d8481cde82ca3349c03",
  "bytes": 586844,
  "regenerate": "python3 -B .scratch/o06c/basename-couples-resolver.py --census --json > .scratch/o06c/census-raw.json"
 },
 "content_sha256": "3ee551fca0b5c88f8dacdf37a544fcd658a23bb7619c9f38501299f773d896a9"
}
````

## 6. Filing order and integrator checklist

1. **Land the body first, byte-exact** at
   `tools/harness/basename-couples-resolver.py` from
   `reports/round-43/op/O09-scribe.md:356-870`; sha256 must stay
   `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`.
   Do not edit the body's cosmetic `payload["round"] = 43` (line 461): the
   artifact's `round` is 44; a byte-exact landing is the claim's condition.
2. `python3 -B tools/harness/basename-couples-resolver.py --selftest` -> must
   print `SELFTEST OK: 27/27 controls`, rc=0.
3. `python3 -B tools/harness/basename-couples-resolver.py --census` -> first
   two lines must be `entries=223 refs=2730` and
   `direct=2556 fallback=166 ambiguous=0 unresolved=7`; artifact line
   `glob-fragment=1`; `conservation: True`.
4. File the §5 block as `reports/round-44/calib/couples-census-r44.json` and
   verify its `content_sha256` recomputes over the body minus `date` and
   `content_sha256`. **Do not file a second census** under another name (the
   r43 F4 two-name conflict); if a human summary is wanted, make it the same
   basename with `.md`, not a second JSON.
5. **Order against claim C.** This artifact pins the **223-entry** tree at
   `c9f4eaa` (`entries: 223`, `corpus.corpus_fingerprint`, `state_note`). Claim
   C's +1 landing is a later corpus change and would make a re-run read 224.
   Do not hand-edit 223 to 224 and do not reuse this artifact as the 224
   census: the claim's threshold is the 223 census (2729 + 1 glob = 2730). If
   the round also wants a post-C census, that is a **new run and a new
   artifact**, not a mutation of this one.
6. Keep `tools/harness/couples-reference-extractor.py` at sha256
   `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`
   (witness-only; the artifact records it under `tool.witness`).

## 7. Provenance, reproduction, and open items

- Raw tool JSON: `.scratch/o06c/census-raw.json`, 586844 bytes, sha256 `ef90ef86ec4381019a8d135ecb8c9df2a6a234c91b7e2d8481cde82ca3349c03`.
  Regenerate with
  `python3 -B .scratch/o06c/basename-couples-resolver.py --census --json > .scratch/o06c/census-raw.json`
  (run from the lane root; the script must sit in a directory with no
  `corpus/` shadow, or the root search will census the shadow — §1).
- Artifact JSON as generated: `.scratch/o06c/census-artifact.json`, sha256
  `c0ee791a89883f0958c62fb46755397a6c8f8f64f0a26e1c31227b30b4940699`; the §5 block is that file verbatim.
- Assembly script: `.scratch/o06c/build_artifact.py` (transient; it asserts
  I1-I12 above and refuses to write on failure).
- Policy digest: `reports/round-42/calib/basename-couples-policy-full.md`,
  sha256 `8c3d7c356ea7c1df3bcaab414ccc2035f6dc90272aaed305e4edf35b2890cdd6` (263 lines; §5.6 at `:99-104`).
- Corpus fingerprint: `7675c7246cf0ac62072d083443fba6b9b699e6108f100476284e44c0972953ba`
  (sha256 over sorted `<repo-relative-path>:<file-sha256>\n` lines); partition
  counts are in `corpus.partitions` (94/25/25/26/29/24 = 223).
- `to-verify`: whether a future round wants the body's hardcoded `round: 43`
  in `--json` output changed. This seat did not change it: byte-exact landing
  is claim O's explicit condition, and the filed artifact's `round: 44` is
  authoritative for this round.
- `to-verify` (not this seat's call): whether the 5 declared-prospective rows
  should read `c12=blocker` or a non-blocker code; the tool currently marks
  them blockers because `documented=false`. Changing that is a tool/policy
  decision, not a census edit.
