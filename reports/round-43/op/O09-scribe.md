- Seat: O09 | scribe | claim O | date 2026-10-19 | baseline `7ceff59` | out `reports/round-43/op/O09-scribe.md`
- Status: integration-ready summary. This file is the only report path this seat wrote; disposable probes live under `.scratch/o09-run/` (gitignored). No filed byte, corpus byte, or in-tree instrument byte was edited; nothing was staged under `corpus/`; no `reports/round-*/run-validation.py` was executed; no git/network/install action.

# O09 — claim-O evidence chain, assembled for integration

## 0. Bottom line for the integrator

1. **The claim's `before` is false at HEAD.** `tools/harness/couples-reference-extractor.py` (r42 N6 successor, 332 lines, sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`) is tracked at `7ceff59`; its `--selftest` is 8/8 green and `reports/round-42/validation.json` records claim O `"passed": true`. The r39 I-C05 identification in `claims.json:27` is also wrong: I-C05 is a citation/path resolver, not a couples resolver (`reports/round-39/cov/C05-audit.md:30`; O07 §5.1). **Do not file the stale wording**; re-scope O as the four-class census + disposition leg, or replace the before-line.
2. **The real r43 increment** is exactly what O04 G1–G5, O05, O06 and O07 measured: four policy classes with a named disposition for every non-direct row, every fallback mapping listed, a synthetic ambiguous control, and a filed census artifact. D1 (block extraction) is already fixed and live.
3. **I assembled and tested a complete successor body** for the new path `tools/harness/basename-couples-resolver.py` (do not edit the r42 tool — O07 §4.3, O12). Bytes are fenced in §5; sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`, 515 lines. It is a new file, standalone, stdlib-only, read-only, in-memory fixtures.
4. **Selftest 27/27 green**, including the wrapped-field positive (identity set, not arity), phantom negative, synthetic ambiguous (two injected index hits), glob-fragment-wins-over-ambiguous (O05's trap), blank-line over-capture trap, slash gate, and live-census conservation.
5. **Census at the live 223-entry tree:** `refs=2730 = direct 2556 + fallback 166 + ambiguous 0 + unresolved 7`, plus `glob-fragment=1` excluded from the four-class totals per policy §5.6. 50 distinct fallback mappings / 166 occurrences, all listed in §4.3. Conservation closes. The r37 eleven-entry anchor reproduces **334 = 319 + 15** exactly.
6. **Claim C is blocked and must not land.** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` already exists at HEAD (r42 C04, sha `c99f44ca...`); the r43 C01 "spare" is a second draft of the same lithic register. C06 and C01-prepare both report the collision. Consequence for O: file the census at **223**, not the post-landing 224 O06 assumed, with `state_note` naming the C collision.
7. **Two artifact-name conflicts must be resolved before filing:** O06 binds `reports/round-43/calib/couples-census-r43.json`; O10 says `reports/round-43/calib/basename-couples-census.json`. O06 owns the name by mission; file **one** artifact, not two. O06's full v3 schema is richer than the draft's JSON; the gap is enumerated in F5 and is the remaining O01/full-body task.

## 1. Evidence chain at this cut

| seat | artifact | status | what it establishes |
|---|---|---|---|
| K01 | `scout/K01-resolver-scout.md` | present | four policy classes; wrapped field is the one instance; r42 class mismatch (`prospective` vs policy `unresolved`) |
| O01 | `op/O01-tool-draft.md` | **absent** | this file supplies an assembled fallback body (§5) |
| O02 | `op/O02-controls.md` | present; §4 evidence executed | 25-control selftest leg; 25/25 PASS quoted in its §4 |
| O03 | `op/O03-predicted.md` | present | predicts `2730 = 2556 + 166 + 7 + 1`, 50 mappings, 6 distinct unresolved; matches this run exactly |
| O04 | `op/O04-verify.md` | present | independent oracle `2730 = 2556 + 166 + 0 + 8` (glob counted with unresolved); G1–G5 gaps |
| O05 | `op/O05-traps.md` | present | trap oracle; found the r42 glob-order bug (`-gate.md` + two hits → `ambiguous`); 79 brace entries / 218 groups / 977 expansions |
| O06 | `op/O06-disposition-leg.md` | present | binding artifact name + v3 schema + disposition table + invariants I1–I11 |
| O07 | `op/O07-durability.md` | present | canonical new path; do not edit r42; no `.scratch` dependency; in-memory fixtures |
| O08 | `op/O08-policy-check.md` | **absent** | policy-conformance checklist not independently filed; §3 below covers the clauses |
| O10 | `op/O10-census-artifact.md` | present | artifact skeleton; **name conflicts with O06** |
| O12 | `op/O12-negative-proof.md` | present | static+dynamic write-surface gate; PASS on the assembled draft (§4.6) |
| O09 | this file | present | assembly, re-measurement, integration sequence |

All seat outputs above are at `reports/round-43/`; none had been integrated into `LOG.md` at this cut.

## 2. Baseline measurements (read-only, HEAD `7ceff59`)

Commands ran from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse --short HEAD                      -> 7ceff59
$ git status --porcelain                          -> ?? reports/round-43/   (only)
$ find corpus/knowledge -name '*.md' | wc -l      -> 223
$ ls corpus/knowledge/myth-symbol/*.md | wc -l    -> 26
$ partitions                                      -> civilizations 94, culture-material 25,
                                                     linguistics 25, myth-symbol 26,
                                                     synthesis 29, verification 24
```

Wrapped field, `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
(file sha256 `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`):

- exactly **one** wrapped `couples:` field corpus-wide (223 fields / 223 entries);
- the filed r19 single-line capture `re.search(r"^- couples:\s*(.*)$", text, re.M)` returns 0 tokens;
- block extraction with hyphen-retained soft-wrap repair returns **4/4**:
  `sound-change.md`, `tone-prosody.md`, `sound-symbolism.md`, `writing-systems.md`;
- resolution: `sound-symbolism.md` and `writing-systems.md` are `direct`
  (`corpus/knowledge/linguistics/`); `sound-change.md` and `tone-prosody.md` are
  `unresolved` (never written; declared prospective seeds at `:76`).

r42 predecessor, measured live:

```
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens [...]
... 8 PASS lines, exit 0
$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

The r42 tool is the N6 witness. It is **not** edited by this round and **not**
imported by the successor.

## 3. Contract-integrity findings

### F1 — the declared `before` is false (blocking for filed prose)
`reports/round-43/claims.json:27` says "no durable instrument implements the r39
basename-couples policy; the only resolver that ever ran (r39 I-C05) lives in
ephemeral .scratch". At HEAD the tracked r42 extractor implements Tier 1 + Tier 2
+ block extraction, its selftest is green, and r42's O claim passed. The r39
I-C05 artifact is a different instrument (citation/path resolver). Owner:
integrator/scribe; either re-scope O as the four-class census + disposition
increment or replace the before-line. Evidence: O07 §0.3/§7 F1, O12-F2,
`reports/round-42/validation.json` (claims.O.passed=true), `git log --oneline --
tools/harness/couples-reference-extractor.py` → `7ceff59`.

### F2 — what O still owes, and what it does not
Already landed (do not re-claim as missing):
- block extraction of the wrapped field (D1), 4/4 by identity;
- hyphen-retained soft-wrap repair (`tone-` + `prosody.md` → `tone-prosody.md`);
- Tier 1/Tier 2 resolution and 8/8 predecessor selftest.

Still owed (the r43 increment):
- four-class headline totals (not six buckets presented as "four classes");
- every fallback mapping listed (the r42 `--census` prints none; `grep -c
  "fallback.*->"` on its output = 0);
- a named disposition for every unresolved/ambiguous row (C12 row 2: blocker
  unless the field marks `(to-verify`);
- a synthetic ambiguous negative (the live corpus has 0 duplicate basenames);
- a filed census artifact under `reports/round-43/calib/`;
- two independent verifiers against the landed bytes (O04/O05 can re-run; their
  verdicts at this cut are `could-not-evaluate` for the absent O01 draft).

### F3 — the four-class arithmetic and the glob fragment
Policy §5.6: "skip or separately class glob fragments; this policy forbids
counting them as unresolved couples findings." Therefore the headline is:

```
2556 direct + 166 fallback + 0 ambiguous + 7 unresolved + 1 glob-fragment artifact = 2730
```

O04's independent oracle reports `unresolved=8` because it counts `-gate.md` as an
unresolved row. O03 and O06 both use 7 + 1. The r42 aggregate JSON
(`reports/round-42/op/couples-census-corrected.json`) also reports 8 at the
220-entry tree; that 8 = 2 strict unresolved + 5 prospective + 1 glob fragment.
The corrected r43 headline is **7 unresolved + 1 artifact**, with O04's 8 shown
only in a reconciliation note. This is a reporting correction, not a token drop:
all 8 rows are named in §4.4.

### F4 — artifact-name conflict (resolve before filing)
- O06 §3.1 binds `reports/round-43/calib/couples-census-r43.json` and says "one
  artifact, one name; do not file a second".
- O10 §1 names `reports/round-43/calib/basename-couples-census.json` (plus a
  `.md` summary).
Recommendation: use O06's path (O06 owns the name by mission); if the parent
wants O10's human summary too, file it as the same basename `.md`, not a second
JSON. Do not file both JSON names.

### F5 — O06's v3 schema vs the assembled draft's JSON
The draft emits the core census: `schema`, `round`, `entries`, `refs`,
`four_class_totals`, `artifact_totals`, `conservation`, `wrapped_fields`,
`fallback_mappings`, `disposition`, `misaligned`, `entries_detail`, `tool`,
`tool_sha256`. O06 additionally requires (all binding if O06's contract is
adopted): `date`, `supersedes`, `policy.path/sha256/successor_path/successor_sha256`,
`corpus.baseline_commit/partitions/index_scope/corpus_fingerprint/state_note`,
`extraction.*` rule strings, `reconciliation.*` counters, `disposition_counts`,
`fallback_mappings` as an array with `entries` and alignment counts, `entries[]`
with `field_parts/field_line_span/expanded_refs/dedup_repeats/counts/tokens`,
per-token `row_id/reason_code/resolution/occurrences/line_span/documented`,
`findings`, `blockers`, and `content_sha256`. The draft's data model contains
enough to derive most of these (per-entry token records and mappings); the
missing pieces are line spans, anchor lists, near-miss evidence, row IDs, and
the content digest. Owner: O01/full-body author or integrator; do not hand-enter
counts the tool did not print (O10's rule).

### F6 — claim C is blocked; the census denominator is 223, not 224 (cross-claim)
`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists at HEAD, added by
`7ceff59` (r42 C04; 192 lines; sha `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`).
The r42 C01 spare is a second draft of the same lithic register; its own header
says C04 landed and it was routed as a spare. C06 files a **BLOCKING COLLISION**;
C01-prepare marks the landing **BLOCKED** and names the spare's false head-block
claims ("never built", "no entry owns stone", 220 files/23 myth-symbol). Do not
land it. O's census is therefore the 223-entry state; O06's "generate after the
C01 landing (224)" cannot be met. File with `state_note: "pre-C01-landing; claim
C blocked by collision (C06/C01-prepare)"` and re-run only if a lawful landing
occurs.

### F7 — O02 vs the assembled selftest
O02 authored a 25-control leg and its §4 now records 25/25 PASS. The assembled
draft implements an equivalent battery natively and adds two controls O05's trap
hunt proved necessary: (a) glob fragment wins over the ambiguous branch when the
fragment's basename has two index hits; (b) a blank line followed by indented
prose is not captured. 27/27 PASS in §4.2.

### F8 — limits carried
- `tone-prosody.md` is an authorial-intent reading, not a filed rule; the in-file
  witness is `corpus/knowledge/linguistics/phonetics-phonology.md:279` (the entry
  writes the name in full, unwrapped). `to-verify`, inherited from r42.
- The draft's group-label position uses `joined.find(ref)`; a brace-expanded
  token not present literally can get position -1 and therefore no group label.
  Live measurement: `misaligned=0`; no alignment finding depends on the edge.
  If O06's per-token `group` is made binding, track spans during extraction.
- The 212-entry r39 figures (2504 = 2335 + 163 + 0 + 6) and the 220-entry r42
  figures (2611 = 2437 + 166 + 0 + 8) are different denominators; never subtract
  from them. The 223-entry measurement is this run: 2730 = 2556 + 166 + 0 + 7 + 1.

## 4. The assembled instrument — measured

### 4.1 Path and durability
- Proposed path: `tools/harness/basename-couples-resolver.py` (new file; the
  claim sanctions this name or a wave-named equivalent).
- The r42 extractor stays at sha `d8d23a26...`, untouched; the r19/r27/r28 filed
  instruments stay untouched (`e7992c32...`, `fb589b28...`, `9b2ccac0...`).
- Standalone: no import of the r42 tool, no `.scratch` read, no `tempfile`, no
  subprocess/network; only the live entry is opened for reading.
- Root discovery uses `os.path.realpath(__file__)` and exits 2 if no
  `corpus/knowledge` is found upward.

### 4.2 Selftest (27/27; exit 0)
```
$ python3 -B .scratch/o09-run/new-resolver.py --selftest
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
```

### 4.3 Census (223 entries; exit 0)
```
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct):
  ...
  misaligned: none
```

Every fallback mapping (50 distinct tokens / 166 occurrences):

| token | mapping | occurrences |
|---|---|---|
| `adornment-body-codes.md` | `corpus/knowledge/culture-material/adornment-body-codes.md` | 2 |
| `animal-symbolism.md` | `corpus/knowledge/myth-symbol/animal-symbolism.md` | 1 |
| `architecture-settlement-lexicon.md` | `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` | 4 |
| `calendar-festival-systems.md` | `corpus/knowledge/culture-material/calendar-festival-systems.md` | 2 |
| `calibration-registry.md` | `corpus/knowledge/verification/calibration-registry.md` | 2 |
| `color-symbolism.md` | `corpus/knowledge/myth-symbol/color-symbolism.md` | 3 |
| `comparative-frameworks.md` | `corpus/knowledge/myth-symbol/comparative-frameworks.md` | 4 |
| `consistency-verification-checklist.md` | `corpus/knowledge/synthesis/consistency-verification-checklist.md` | 1 |
| `cosmology-cosmography.md` | `corpus/knowledge/myth-symbol/cosmology-cosmography.md` | 2 |
| `costume-semiotics.md` | `corpus/knowledge/culture-material/costume-semiotics.md` | 8 |
| `coupling-model.md` | `corpus/knowledge/synthesis/coupling-model.md` | 1 |
| `creation-myths-taxonomy.md` | `corpus/knowledge/myth-symbol/creation-myths-taxonomy.md` | 1 |
| `dress-through-eras.md` | `corpus/knowledge/culture-material/dress-through-eras.md` | 5 |
| `era-language-staging.md` | `corpus/knowledge/synthesis/era-language-staging.md` | 1 |
| `era-periodization-models.md` | `corpus/knowledge/culture-material/era-periodization-models.md` | 1 |
| `garment-lexicon-crosslinguistic.md` | `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md` | 3 |
| `historical-linguistics.md` | `corpus/knowledge/linguistics/historical-linguistics.md` | 9 |
| `inca.md` | `corpus/knowledge/civilizations/inca.md` | 1 |
| `kinship-terminology.md` | `corpus/knowledge/linguistics/kinship-terminology.md` | 1 |
| `language-contact.md` | `corpus/knowledge/linguistics/language-contact.md` | 10 |
| `lexicon-coverage-audit.md` | `corpus/knowledge/verification/lexicon-coverage-audit.md` | 1 |
| `loanword-material-dating.md` | `corpus/knowledge/synthesis/loanword-material-dating.md` | 1 |
| `material-culture-inference-method.md` | `corpus/knowledge/culture-material/material-culture-inference-method.md` | 10 |
| `maya-classic.md` | `corpus/knowledge/civilizations/maya-classic.md` | 1 |
| `mesopotamia-sumer-akkad.md` | `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` | 1 |
| `morphological-typology.md` | `corpus/knowledge/linguistics/morphological-typology.md` | 2 |
| `music-instrument-lexicon.md` | `corpus/knowledge/culture-material/music-instrument-lexicon.md` | 1 |
| `myth-ritual-theories.md` | `corpus/knowledge/myth-symbol/myth-ritual-theories.md` | 1 |
| `myth-to-language-derivation.md` | `corpus/knowledge/synthesis/myth-to-language-derivation.md` | 1 |
| `naming-systems.md` | `corpus/knowledge/linguistics/naming-systems.md` | 14 |
| `number-symbolism.md` | `corpus/knowledge/myth-symbol/number-symbolism.md` | 1 |
| `orality-formulaic-language.md` | `corpus/knowledge/linguistics/orality-formulaic-language.md` | 4 |
| `pantheon-archetypes.md` | `corpus/knowledge/myth-symbol/pantheon-archetypes.md` | 5 |
| `phonetics-phonology.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | 1 |
| `politeness-taboo-euphemism.md` | `corpus/knowledge/linguistics/politeness-taboo-euphemism.md` | 2 |
| `real-world-inspiration-boundaries.md` | `corpus/knowledge/verification/real-world-inspiration-boundaries.md` | 2 |
| `register-strata-attestation.md` | `corpus/knowledge/linguistics/register-strata-attestation.md` | 1 |
| `religion-language-co-evolution.md` | `corpus/knowledge/synthesis/religion-language-co-evolution.md` | 1 |
| `ritual-garments.md` | `corpus/knowledge/culture-material/ritual-garments.md` | 6 |
| `ritual-liminality.md` | `corpus/knowledge/myth-symbol/ritual-liminality.md` | 2 |
| `semantics-pragmatics.md` | `corpus/knowledge/linguistics/semantics-pragmatics.md` | 3 |
| `sociolinguistics-registers.md` | `corpus/knowledge/linguistics/sociolinguistics-registers.md` | 7 |
| `source-discipline-calibration.md` | `corpus/knowledge/synthesis/source-discipline-calibration.md` | 1 |
| `sumptuary-law-rank-display.md` | `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` | 3 |
| `symbolism-synthesis-method.md` | `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md` | 10 |
| `taboo-euphemism-lifecycle.md` | `corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md` | 1 |
| `textile-technology.md` | `corpus/knowledge/culture-material/textile-technology.md` | 4 |
| `trade-economy-lexicon.md` | `corpus/knowledge/culture-material/trade-economy-lexicon.md` | 3 |
| `warrior-material-culture.md` | `corpus/knowledge/culture-material/warrior-material-culture.md` | 1 |
| `writing-systems.md` | `corpus/knowledge/linguistics/writing-systems.md` | 13 |

The eleven-entry r37/r39 anchor reproduces exactly:
`334 = direct 319 + fallback 15 + ambiguous 0 + unresolved 0` (sacred-kingship
`36 = 21 direct + 15 fallback`). The three r42 myth-symbol entries contribute
`44 + 36 + 39 = 119` direct tokens, which is the whole 2437 → 2556 delta; no new
fallback or unresolved token came from them.

### 4.4 Disposition leg — every non-direct row named
Unresolved (7 occurrences, 6 distinct):

| token | entry | disposition | C12 row 2 | reason |
|---|---|---|---|---|
| `honorifics-and-register.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed | blocker | declared prospective/sibling-seed token in the couples field; never written, not a referenced entry |
| `naming-and-onomastics.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed | blocker | declared prospective/sibling-seed token in the couples field; never written, not a referenced entry |
| `phonology-basics.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed | blocker | declared prospective/sibling-seed token in the couples field; never written, not a referenced entry |
| `sound-change.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | declared-prospective-seed | blocker | declared prospective/sibling-seed token in the couples field; never written, not a referenced entry |
| `tone-prosody.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | declared-prospective-seed | blocker | declared prospective/sibling-seed token in the couples field; never written, not a referenced entry |
| `../linguistics/phonology-sanity.md` | `corpus/knowledge/synthesis/typed-label-routing-workflow.md` | dangling-reference | blocker | Tier 1 failed and the token is not eligible for the unique-basename fallback (slash-bearing or zero index hits) |
| `../linguistics/phonology-sanity.md` | `corpus/knowledge/verification/label-channel-routing-verification.md` | dangling-reference | blocker | Tier 1 failed and the token is not eligible for the unique-basename fallback (slash-bearing or zero index hits) |

Glob artifact (1; excluded from the four-class totals):

| token | entry | disposition | reason |
|---|---|---|---|
| `-gate.md` | `corpus/knowledge/verification/gate-frozen-run-standard.md` | extractor-artifact | glob pattern fragment (policy 5.6): extractor artifact, not a couples finding |

`ambiguous`: zero live rows (223 files, 223 distinct basenames, 0 duplicates);
the synthetic two-hit control is the coverage. No token is dropped: 2556 + 166 +
0 + 7 + 1 = 2730, and the per-entry records close the same sum.

### 4.5 Per-entry wrapped-field read
```
$ python3 -B new-resolver.py corpus/knowledge/linguistics/phonetics-phonology.md
corpus/knowledge/linguistics/phonetics-phonology.md wrapped=True tokens=4
    sound-change.md                  unresolved     declared-prospective-seed
    sound-symbolism.md               direct
    tone-prosody.md                  unresolved     declared-prospective-seed
    writing-systems.md               direct
```

### 4.6 O12 negative-proof gate on the assembled draft
The gate source is O12's Appendix A, extracted verbatim to
`.scratch/o09-run/o12-gate.py` and run against the draft:

```
VERDICT PASS-static
  dont_write_bytecode True
  imports ['__future__', 'argparse', 'glob', 'hashlib', 'json', 'os', 're', 'sys']
  non-stdlib none
  write-calls none
DYNAMIC: --selftest rc=0; --census rc=0; per-entry rc=0
  tree-diff NO-DIFF
  git-status-diff SAME
GATE_EXIT=0
```

## 5. Fenced draft — `tools/harness/basename-couples-resolver.py`

Integrator applies this block as a **new** file (0644; no chmod needed). It is
the assembled fallback body because O01 is absent at this cut; if O01 lands,
prefer O01's bytes and use §6/§7 as the acceptance checklist. The body copies
the parse semantics of the r42 witness (cited, not imported) and adds the
four-class report, the disposition leg, the ambiguous/phantom/over-capture
controls, and the JSON census.

````python
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
````

## 6. Integration sequence (ordered)

1. **Apply** the §5 block to `tools/harness/basename-couples-resolver.py`
   (new file; do not touch `tools/harness/couples-reference-extractor.py`).
2. **Selftest:** `python3 -B tools/harness/basename-couples-resolver.py --selftest`
   → `SELFTEST OK: 27/27`, exit 0.
3. **Census:** `python3 -B tools/harness/basename-couples-resolver.py --census`
   → first line `entries=223 refs=2730`; four-class `2556/166/0/7`; artifact
   `glob-fragment=1`; `conservation: True`; 50 mapping lines.
4. **Artifact:** `... --census --json > reports/round-43/calib/couples-census-r43.json`
   (O06's binding name; do not also file O10's name). If O06's full schema is
   enforced, extend the JSON with F5's fields first or record the reduced schema
   as an explicit ruling. Set `state_note` to the C-collision state.
5. **Pin:** `sha256sum tools/harness/basename-couples-resolver.py` → record in
   the artifact and the LOG entry; expected `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` for the §5 bytes.
6. **Negative proof:** run O12's gate (Appendix A of `op/O12-negative-proof.md`)
   with `--dynamic`; expect `PASS-static`, `tree-diff NO-DIFF`,
   `git-status-diff SAME`.
7. **Witness cross-check:** `python3 -B tools/harness/couples-reference-extractor.py --census`
   must still say `wrapped fields: 1` and the same four token names; its digest
   must remain `d8d23a26...`.
8. **Two verifiers:** O04 re-runs its §3 matrix (R1–R11) against the landed
   bytes; O05 re-runs its trap vectors (anchors, braces, two-hit basename,
   last-header field, glob-over-ambiguous). O08's policy checklist is still
   absent; the §3 clauses above are the checklist it would apply.
9. **Queue:** close `r39-ic05-resolver-durability` as a successor record
   (`fixed-with-evidence`, owner integrator) — cross-claim with Ca; never edit
   the r40 file.
10. **Do not** re-freeze `declared-in-r7`, change packet surfaces, edit filed
    bytes, or stage the C spare.

## 7. Acceptance checks the absent `reports/round-43/run-validation.py` should carry

`reports/round-43/run-validation.py` does not exist at this cut. When the
integrator authors it, the O leg should assert:

- O1: `tools/harness/basename-couples-resolver.py` exists and its sha256 equals
  the pinned value.
- O2: `--selftest` exit 0 and its output contains `SELFTEST OK: 27/27` (or the
  O02 25/25 battery if O02's block is used instead).
- O3: `--census` first line matches `entries=223 refs=2730` and the four-class
  line matches `direct=2556 fallback=166 ambiguous=0 unresolved=7`; artifact
  line matches `glob-fragment=1`; `conservation: True`.
- O4: per-entry on the wrapped field prints exactly the four tokens with classes
  `2 direct + 2 unresolved`, and no standalone `prosody.md`.
- O5: `--census --json` parses; `conservation` true; `fallback_mappings` has 50
  entries; `disposition.unresolved` has 7 rows; every row has a non-empty reason
  and a C12 disposition.
- O6: O12 gate exit 0; tree manifest `NO-DIFF`; `git status --porcelain` only
  `?? reports/round-43/`.
- O7: r19/r27/r28/r42 digests unchanged; no `M` under `corpus/`.
- O8: the artifact carries the tool digest, the population digest and the exact
  command; unknown fields are `null` with a reason, never inferred.

## 8. Owed / to-verify

- **O01 draft:** absent; §5 is the assembled fallback. If O01 lands, re-run the
  §6 checklist against its bytes; do not merge two tool bodies.
- **O06 schema:** F5's fields are not emitted by the draft; the filed artifact
  must either add them or record the reduced schema as a named ruling.
- **O06/O10 artifact name:** conflict; use `couples-census-r43.json` and one JSON.
- **C claim:** blocked (F6); the 224-entry census cannot be produced lawfully.
- **`tone-prosody.md`:** authorial intent, `to-verify` (in-file witness `:279`).
- **O08:** policy-conformance checklist not independently filed.
- **Runner:** `reports/round-43/run-validation.py` absent; §7 is the proposed O leg.
- **Eight-row arithmetic:** the filed r42 census and O04's oracle report 8
  unresolved; this round's headline is 7 + 1 artifact per §5.6. Record the
  reconciliation, do not rewrite the r42 file.
- **`joined.find(ref)`:** group labels for brace-expanded tokens are best-effort;
  no live misalignment, but a strict per-token `group` schema needs span tracking.

## 9. Citations

- Claim, thresholds, counting commands: `reports/round-43/claims.json:24-35`
  (claim O), `:4-13` (axes), `:36-55` (claim C), `:56-70` (claim Ca).
- Baseline and tree: `git rev-parse --short HEAD` → `7ceff59`; `git status
  --porcelain` → `?? reports/round-43/`; `find corpus/knowledge -name '*.md'` → 223.
- r42 durable instrument: `tools/harness/couples-reference-extractor.py` (332
  lines, sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`);
  `couples_block:50-73`, `join_parts:76-93`, `classify:134-150`,
  `census:186-211`, `selftest:242-296`, `main:298-330`.
- r42 O pass: `reports/round-42/validation.json` (`claims.O.passed=true`).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (sha256 `b4f9b003...`), in-file witness `:279`.
- Policy: `reports/round-39/calib/basename-couples-policy.md` (107 lines;
  truncated), full successor `reports/round-42/calib/basename-couples-policy-full.md`
  (§1 `:14-25`, §2 `:27-48`, §3 `:50-58`, §4 `:60-69`, §5 `:71-102`, §5.6 `:97-102`).
- Defects: `reports/round-39/calib/Ca04-verify.md:78-106` (D1/D2);
  `reports/round-39/review/R01-review.md:262-274` (R01-7);
  `reports/round-40/op/defect-queue-v2.json` rows `N6-couples-extractor-wrapped-field`,
  `r39-basename-successor-instrument`, `r39-ic05-resolver-durability`.
- Seat evidence: `reports/round-43/scout/K01-resolver-scout.md`;
  `op/O02-controls.md` (§4 25/25); `op/O03-predicted.md` (§1 table, §5, §6);
  `op/O04-verify.md` (§2 oracle, §4 G1–G5, §6 verdict);
  `op/O05-traps.md` (§1 trap matrix, §4 glob-order finding);
  `op/O06-disposition-leg.md` (§3 schema, §4 vocabularies, §5 invariants);
  `op/O07-durability.md` (§2.6 header, §4.3 no-edit, §5 no-scratch);
  `op/O10-census-artifact.md` (§1 name conflict, §2 schema);
  `op/O12-negative-proof.md` (Appendix A gate).
- Cross-claim collision: `reports/round-43/cov/C06-collision.md` (BLOCKING
  COLLISION, live listing), `reports/round-43/cov/C01-prepare.md` (BLOCKED,
  byte-identical C04 landing, sha `c99f44ca...`), `reports/round-42/cov/C01-mineral-spare.md:1`
  (the spare's own routing note).
- Command outputs quoted in §2/§4 are this seat's runs at 2026-10-19T17:00Z,
  read-only; the §5 tool's sha256 is `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`.
