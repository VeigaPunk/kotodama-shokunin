# Review — component 05-lexicon (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/05-lexicon.yml`
- status: **REVIEWED — delivered; 4 corpus-grounded findings, 7 contract findings, core checks clean**
- reviewed artifact: 700 lines + a trailing `canon_boundary:` line (no final newline), 43 750 bytes, md5 `1dd99c9b52db7ff7144b0f67eb14b0b0`, mtime 2026-10-17 11:33:56 −03
- canon: not canonized (D2 design drill)
- no component content was edited by this worker (review scope: this file only)

## Evidence (commands run against the frozen md5)

- Gate: `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d2/components/05-lexicon.yml`
  → no findings printed, exit 0.
- Parser probe (the gate's own `load_packet`): `pitch_accent` key **absent** from the
  parsed packet; `era_notes` has 5 items whose last is a dict — the whole
  `pitch_accent` block is swallowed into `era_notes`. Cause: line 61 has no newline
  between the era note's closing quote and the key (`…new formations)."pitch_accent:`).
- Counts (gate parser, not hand-counted): 40 records; field tallies body 3 /
  kinship 4 / weather 5 / landscape 5 / subsistence 7 / war 3 / religion 5, plus
  trade 4, costume 2, social_order 2; layers native 34 / loan 2 / sacred 3 /
  taboo 1; routes root 22 / derived 14 / borrowed 2 / lexicalized 1 / compound 1;
  `axis` key on 0 of 40 records, `evidence` 0 of 40, `basis` 40 of 40.
- D1 non-import sweep (`grep -niE` river/ford/current/net/bind/tie/tying/knot/rope/
  cord/watercourse/sea/coast): hits only in the component's own non-import
  declarations, the tally-cord entry (a counting device, no binding symbolism),
  and one English meta-text need (see watch list). No in-world D1 imagery found.
- Provenance spot-check of every `basis:`/`follows:` pointer: sf-lex §2–§7,
  audit §3/§4/§6/§7, kin §1 (G+1 row at kin file line 27–29; atom of kinship at
  line 39), §4 rule 4 (line 71), §9; trade §2/§3/§7/§10; textile §2/§6;
  cosmo §2/§9; taboo §3/§5 — all files exist and the named sections carry the
  claim. All citations are repo paths; no outside or invented source is cited.

## Violations (corpus-grounded)

`05-lexicon | <violation> | <corpus path:section>`

1. `05-lexicon | line 61 drops the newline before the pitch_accent key; the parsed model loses pitch_accent entirely and era_notes gains a corrupted dict item, so the packet's only recorded minimal pair (kol / kól) is unreachable to any consumer; the lane gate does not catch this (exit 0) | corpus/knowledge/verification/lexicon-coverage-audit.md §2 (lexicon snapshot: form/pronunciation records must resolve) + §8.1 (freeze reproducible inputs); corpus/QUALITY.md §4 (usability)`
2. `05-lexicon | L26 kat "the written tally-sheet" is staged in Nalne, the era before the script loan pert (Pertne) and before D2 literacy; the entry never states who writes the sheet, so referent availability is asserted (layer referent_available_from: Nalne) without the producer being named | corpus/knowledge/verification/lexicon-coverage-audit.md §6 (cultural/material availability; L-material-anachronism: contemporary referent used before its declared availability) + §7 (keep naming dates and material availability separate)`
3. `05-lexicon | L40 senin is formed with AGENT on sen ("raid, herd-taking"), a base outside AGENT's declared eligible set (herd, pasture, land, war-band, lineage); no exception note covers it and derivation_tests tests AGENT boundaries only for pal and im — the restriction has no demonstrated boundary for the raid base | corpus/knowledge/verification/lexicon-coverage-audit.md §4 (construction signature; a restricted construction needs an eligible context and a demonstrated boundary) + §8 adversarial case ("apply an agent-forming rule to a base excluded by its declared restrictions" = D-rule-violation)`
4. `05-lexicon | coverage_notes rows carry need/field/need_text/context/expression/status but no example and no back-translation, the per-need record shape the audit requires | corpus/knowledge/verification/lexicon-coverage-audit.md §3 (For each need record need ID → field → context → expression IDs/construction → example → back-translation → reviewer finding)`

## Contract findings (against the drill's own brief, not corpus violations)

Source of the contract: `examples/culture-d2/components/01-brief.yml` — `contract.record_fields`
and acceptance `A-04`. These are not superseded by any corpus rule I could find; where the
corpus text leans the other way it is noted.

1. `05-lexicon | 40 records, not A-04's ≥60; field floors missed (body 3, war 3 vs ≥4; weather 5 and landscape 5 vs ≥10 each); layer floors missed (native 34 vs ≥40; loan 2 vs ≥6; sacred 3 vs ≥4; taboo 1 vs ≥2) | brief A-04; corpus does not forbid smaller fields — sf-lex §7 requires profile-based sizing, which field_weights does supply, so this is a scope decision for the round integrator, not a design fault`
2. `05-lexicon | route tokens derived / borrowed / lexicalized (17 of 40 records) are outside the contract's fixed list root|derivation|compound|loan|calque; layer and route value spaces are not declared as extensions | brief contract.record_fields; note the corpus audit itself uses "derived/compound/borrowed" (lexicon-coverage-audit.md §4), so the brief's value list and the corpus vocabulary disagree — report to the integrator rather than silently renaming`
3. `05-lexicon | no axis key on any of the 40 records and no per-record evidence status (basis: is a corpus pointer, not a status label) | brief record_fields + CP-11; corpus lexicon-coverage-audit.md §2 wants reference/design claims marked (attested/reconstructed/contested/design-choice/(to-verify)) — the file declares design-choice globally in its header, which covers the substance, so this is a record-shape gap`
4. `05-lexicon | mirrored phonology block is out of the brief's spec: tones: 2 where the contract fixes tones: 0; 1 notable rule vs A-02's ≥6; 11 consonants vs A-02's ≥14 | brief A-02/record_fields; corpus phonetics-phonology.md §6 keeps stress accent, pitch accent and tone as distinct values, so tones: 2 for a pitch-accent language is calibration drift unless component 02 declares a tonal analysis — 02 owns the final block`
5. `05-lexicon | era stages Korne/Nalne/Pertne are used with no one-line mapping to the fixed E0–E3 tag space, and the file names the eras although era names belong to component 09 | brief era_tags alias_rule + design_space`
6. `05-lexicon | A-04's recorded gate run and D1-overlap scan report are absent (no validation block); the brief also names worked-example-mini-culture.md §8 as the overlap reference list, which is not cited | brief A-04, D1B-06; this reviewer ran the gate instead — exit 0, evidence above`
7. `05-lexicon | cross-component id bindings are not discharged: 12-rank-rules pins LEX-DEG-1..7 (surface forms + pitch-accent class), 15-pragmatics cites D2-Lnn, but 05 declares no such ids and records accent only for the kol/kól pair | brief RG-03 (cross-component references use only contract IDs); candidates exist in the file (lasin ≈ "lineage head", ralin ≈ herder, velim ≈ wind-breath) and can be bound at integration`

## Watch list (advisory, no repair demanded)

- L24 `talur` "to wind-dry meat" derives by PROCESS from `tal`, glossed "dried meat";
  composition needs L21's recorded narrowing ("keepable provision" → "dried meat")
  restated in the entry (audit §4 meaning composition).
- phonology `notable_rules: s → ∅ / _#` with `las` recorded as `las`, and the witness
  note's "the orthography is phonemic throughout, so recorded forms carry the s" —
  a phonemic spelling would drop the s; state underlying vs surface, or leave the
  rule to 02 (phonology-sanity-gate.md §5 derivation row expects predicted surface
  = supplied form).
- coverage_notes N14 need_text "swear a bargain bindingly" is English meta-text, but
  the word "bindingly" is exactly the D1 obligation metaphor the brief's RG-01
  forbids as in-world imagery; reword to avoid tripping a D1B-02 check on a later pass.
- EOF: no final newline; the archive convention in this repo is one.
- `kól` is listed both in `roots.native_roots` and as a headword; that is consistent
  here (accent pair) but the double listing should stay deliberate at integration.

## Clean checks (what was checked, with evidence)

- **Field coverage (assignment check 1) — pass with declared gaps.** All seven corpus
  fields carry entries and need rows; gaps are declared and kept in the denominator
  (N01 body state/pain verbs; N17 war refusal/settlement), exclusions are explicit
  (sea/coast and watercourses, with the D1 reason), and coupling probes from audit
  §3 are exercised (pasture claim by descent; herd count; traveller weather warning;
  route/direction; toll at the fair). Earnings: audit §3 row shape is the one miss
  (finding 4).
- **Etymology validity (assignment check 2) — pass.** Every derived/compound term
  reproduces from its declared construction and bases: LOC velra/tokra/sirra/senra;
  AGENT ralin/lasin/velin; SPIRIT velim/hurim; MATRI-SIDE nemter; WIND velsu;
  UP-COMPOUND suwal; PROCESS talur; GARMENT mirken; lexicalized toksa flagged
  noncompositional with its history note (audit §4 exception accountability).
  Loan forms recompute under the declared substitutions (gate: gad→kat, bherd→pert).
  No entry rests on an unrecorded base. Held-out rows and boundary rejections are
  present for every construction (audit §4 project diagnostic).
- **Layer coherence (assignment check 3) — pass.** Two layers, each with donor,
  donor stage, entry stage, channel, contact window, substitutions and referent
  availability; trade loan precedes script loan; borrowability sites match sf-lex §3
  (trade/administration borrowed, costume native because D2 is the fiber exporter —
  textile §2/§6); no function words, pronouns, numerals or inflection borrowed
  (language-contact §2–§3 rungs 1–2 only); the script word is an adaptation, not an
  invention. Caveat carried: the kat producer question (finding 2).
- **English-relex screen (assignment check 4) — pass.** Field splits are not
  English's: hand+forearm one term; fleece on-animal/off-animal one term; terrain cut
  by the two season poles and the pass instead of English's water/hill scatter;
  weather cut by slope, not by kind; kin type (Omaha) is read off the terminology
  rather than English labels respelled (audit §3 "typical false coverage" avoided);
  the one loaded colexification (breath = wind) is flagged (to-verify) for a CLICS³
  check instead of asserted; no snow-word inflation (sf-lex §4/Weather, §7).
- **Spine coupling — pass.** Verticality: two poles, the pass, snow-line, era names,
  LOC place/span set, upslope/downslope wind set; wind: oath medium, storm law,
  death breath, wind-dried meat. No river/ford/binding imagery in any entry.
- **Canon hygiene — pass.** `canon: not canonized (D2 design drill)`, a canon_boundary
  block, and a handoff list to sibling components; no world claim asserted.

## Re-run condition

Re-dispatch a review worker against the same path if the writer revises the file
(md5 will change): findings 1–4 and contract items 2–7 must be re-checked, and the
gate re-run. Nothing here is a canon decision; the component remains a non-canon
design proposal.