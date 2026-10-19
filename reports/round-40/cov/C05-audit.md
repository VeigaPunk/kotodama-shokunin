- Seat: C05 | verifier | claim C | date 2026-10-19 | baseline fd55e1f

# C05 — audit of the four linguistics-partition entry drafts (claim C / coverage)

Round 40 (regimen 2, loop 1, position 8), seat **C05**, role **verifier**, claim **C**. Mission
(verbatim, `reports/round-40/targets.json` → `seats[id=C05].mission`): *"Audit all 4 drafts (runbook
+ source resolution + fabrication spot-checks); verdicts."* All four drafts landed inside this seat's
window (C01 11:18Z, C03 11:51Z, C02 11:53Z revised ~14:48Z, C04 12:09Z — mtimes preserved from the
swarm copy; last seen landing C06 12:05Z). Every reading below was **re-measured from the filed
bytes by this seat** at HEAD `fd55e1f`. Audit window 2026-10-19 13:55–15:20Z.

- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` →
  `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` (== declared baseline `fd55e1f`,
  `reports/round-40/claims.json:7`); at audit close `git status --porcelain` → ` M LOG.md`
  (parent-owned) + `?? reports/round-40/` only; corpus censuses at close: linguistics **21**,
  knowledge total **216** — zero corpus staging on the tree at any audit stamp.
- **Canon: NON-CANON.** This seat audits bytes and files defects; it admits no entry, certifies no
  round, promotes nothing. A green reading is a structural reading of named digests — never a
  verdict on the scholarship, never canon (`PROVINCE.md`; `corpus/QUALITY.md`).
- **Writes**: this file only, plus gitignored `.scratch/c05r40/`. No `corpus/**` byte, no
  `tools/**`, no filed round-1..39 byte. No commit, no push, no install, no network.
- **Runner ban**: no `reports/round-*/run-validation.py` was executed anywhere, in-tree or in a
  copy (`shared_rules[4]`; X00 §C8). The only filed code executed is read-only:
  `reports/round-35/cov/C12-audit-runbook.md` §5's instrument, installed from its own step-0 awk.

**Verdict at a glance: 4/4 PASS** the round-35/36/39 structural contract — **C01, C02, C03 clean
after adjudication; C04 PASS-with-named-defects** (one S2 receipt defect, below). ~200 fabrication
needles read at their cited lines; **every needle verifies** except two C03 sweep counts carrying a
+1 inflation consistent with C03's own disclosed transient file, and two C03 locator imprecisions.
Defects: one **S2** (C04's self-audit digest pin), four **S3** (§6). The claim-C threshold "audit
4/4 PASS (named defects allowed)" is **met by this leg on the draft bytes**; the sweep-green leg
remains the integrator's post-apply reading.

## 0. Instruments and audited bytes

| instrument | source | digest / result |
|---|---|---|
| **I-C12** (round-35 runbook instrument) | installed fresh from `reports/round-35/cov/C12-audit-runbook.md` §5 by its own step-0 awk | sha256 `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`, 663 lines — equals the filed digest C04's self-audit also records; `--selftest` → exit 0, SELFTEST PASS |
| **I-C05** (r39 resolver, carried) | `.scratch/c05/c05-audit.py` | sha256 `4326bb856e13e34a3334e4769140e4ee20a1a1d1266a91d8616eb557da75cbd6` — equals the digest filed at `reports/round-39/cov/C05-audit.md` §0; `--selftest` → exit 0 |
| **fence-run extractor** (this seat) | `.scratch/c05r40/extract.py` — 3/4+ backtick fences, info strings, unclosed-fence error | handles all four fragments (C01/C02 4-backtick; C03 4-backtick entry + 3-backtick receipt; C04 3-backtick) which the r35 stager regex does not (R01-10 precedent) |
| **corrected binder** (this seat) | `.scratch/c05r40/binder.py` — nearest-preceding-path binding of detached `:n` refs | 54 line refs over 4 fragments, **1 out-of-range** (the C03 `:209`, adjudicated §3/F3) |

Audited bytes (extracted fresh by this seat):

| seat | fragment | fragment sha256 | entry block | block bytes | block sha256[:16] | fence |
|---|---|---|---|---|---|---|
| C01 | `cov/C01-entry-1.md` | `ff3e004cdb797506…` | frag lines 5–140 | 32 798 | `379349d1a346487c` | one 4-backtick block |
| C02 | `cov/C02-entry-2.md` | `cec07007ef4175da…` (revised; block unchanged from the 44 949 B first sighting `3c283562b02482bb…`) | frag lines 5–135 | 33 091 (33 090 stripped = the self-audit pin, see §2) | `eb5f75d7ae59a6d1` | one 4-backtick block |
| C03 | `cov/C03-entry-3.md` | `fa7df06a1a5db116…` | frag lines 36–236 | 47 417 | `2289a9b77ea116c4` — **equals the fragment's own §3/§5 receipt pin byte-for-byte** | 4-backtick entry + 3-backtick receipt (staging hazard, §7) |
| C04 | `cov/C04-entry-4.md` | `c12c1683a22ef1f8…` | frag lines 28–188 | 37 206 | `1b007b5fb9702cdd` — **the fragment's Reading-2 pin `019a5b4d…` does NOT reproduce** (F1, §6) | one 3-backtick block |

Freeze: the audited digests are these. C02's fragment was revised mid-audit (+263 B at fragment
level only; `diff` of the entry blocks is **empty** and the self-audit pin still reconciles, so the
entry reading carries); its revision also removed a duplicated self-audit bullet this seat had
filed as a note against the first sighting. Any further post-audit byte change to a fragment voids
the corresponding reading and owes a re-run.

## 1. C01 — `taboo-strata-lifecycle.md` (K03 E1 / claims-C topic 1: taboo-euphemism lifecycle)

**Verdict: PASS** (one S3 locator defect, F2).

- I-C12: **PASS/clean** — frontmatter 4/4 + literal `- scope:`, lane 5-field profile 5/5, pointers
  8/8 resolved, gap named, decision record present, bleed 0 candidates / 6 negated mentions.
  Source leg 13/14 bullets carry `path:line` locators (the unlocated bullet is the in-repo-authority
  round-up; informational).
- I-C05: 30 citations / 31 line numbers / 13 unique paths — 0 unresolved, 0 missing; the single
  out-of-range hit (`contact-strata-verification-gate.md:233`, file has 165 lines) is the **known
  I-C05 F6 mis-binding** (r39 audit §6 F6: a detached `` `:n` `` binds to the last path on the line
  instead of the nearest preceding). Corrected binder: 12 refs, 0 out-of-range — the `:233`
  belongs to `historical-linguistics.md` (252 lines; the taboo paragraph). Hand-adjudicated: instrument artifact, not an entry defect.
- Head block: 9 fields (topic / gap filled / sources / calibration / couples / source / verified-at
  / recheck / scope), `verified-at` ISO 2026-10-19; decision record §8 with DR-TS-01…08, all eight
  defined in-table, all body references dangling-free.
- Absence sweeps: **all reproduce exactly** — `treadmill` → 4 files (same four);
  `minced` → 3 (same three); `"ordering test"|"sound-law bracket"|"bracketing"` → 0/0/0;
  `read-off` → 1, at `civilizations/parthia.md:157` whose text is exactly the attested-name-table
  sense C01 disposes; `grep -n -i taboo corpus/knowledge/linguistics/language-contact.md` → 0.
- Couples: 9/9 targets resolve (8 corpus + `corpus/QUALITY.md`). Filename `taboo-strata-lifecycle.md`
  collides with nothing (0 hits corpus-wide).
- Fabrication spot-checks (~50 needles): every cited line of
  `linguistics/politeness-taboo-euphemism.md` (:23,24,28,29,30,32,34,35,37,74,75,76,82,83,84-92,88,95,99-106,101,102,103,104,106,124,127,128),
  `synthesis/taboo-euphemism-lifecycle.md` (:5-11,15,17,19,20,27,28,29,34-43,45,49-65,62,72,73,82-94,94,117-123,121,122,125-137,139-144,146-156,150,151,152,153,156,163,185),
  `historical-linguistics.md` (:3 topic-adjacent, :7 couples, :233 taboo paragraph, §8 glottochronology at :166/:213),
  `language-contact.md` (:3 topic line — see F2), `corpus/QUALITY.md:3-23`,
  `reports/round-40/claims.json:7,14`, `reports/round-39/scout/K01-verification-gaps.md:106-123`,
  `corpus/README.md:6-10` — **read and verified: each says what the entry claims.** Highlights:
  the bìhuì "mechanism mainstream, specific cases thinly documented" hedge is verbatim
  `politeness:75`; the treadmill anti-overclaim note is `:127`; "generated wrong on purpose" is
  `:128`; the synthesis protocol steps :150/:152/:153/:156 and the safe/unsafe row :163 are exact.
- K03 §5 non-restatement criterion (E1): satisfied — §1's boundary table routes the ladders
  (`politeness:84-92`) and the four-strata design rule (:106) to their owner as inputs; §9's
  demonstration is an invented ordering exercise, not the :118 dating example restated.
- Line counts claimed in `- verified-at:` (politeness 135; synthesis 201): both reproduce.

## 2. C02 — `dialect-register-consistency.md` (K03 E2: dialect/register-consistency)

**Verdict: PASS** (no entry-level defect; fragment-level note N1).

- I-C12: **PASS/review** — one review-tier hit (`canon-mention-unnegated`), adjudicated **false
  positive**: the unnegated mention is the couples line's boundary idiom "canon stays there"
  (attributing, not asserting). All contract legs green (4/4, 5f, src 9/9, ptr 11/11, gap, decision
  record, bleed otherwise 0).
- I-C05: 8 citations / 12 line numbers / 15 paths — 0 unresolved, 0 out-of-range, 0 missing.
- **Digest-pin reconciliation: exact.** The self-audit pins staged bytes `e0ea254391922add…`,
  33 090 B; my extraction is 33 091 B with trailing newline; stripping it yields 33 090 B and
  sha256 `e0ea254391922addc4076ab6cf3bafc7c6321b9caaa97db99fff99965230dd37` — **match**. (Shape
  note for the integrator: this fragment pins the stripped-block shape, C03 pins the with-newline
  shape; the stager must record which shape a pin names. r39 §0 carried the same two shapes.)
- Absence sweeps: **all reproduce exactly** — `founder effect` → 1 file (migration-founder-effects,
  hit at :18); `new.dialect` → 0; `second.life` → 0; `anti-society` → 5 hits in 3 files at exactly
  `linguistic-anthropology.md:117,122,146`, `register-lexicon-ceilings.md:12`,
  `dialect-faction-map-workflow.md:202`; `koineization` → 5 files (same set); `focusing` → 1 hit at
  `dialect-faction-map-workflow.md:94`; `overlexical` → 3 files; `reallocation` → 6 files.
- Fabrication spot-checks (~45 needles) — **all verify**, including the load-bearing ones:
  `sociolinguistics-registers.md` :9,:13-16 (registrations), :41 (live-recheck verified-at), :58
  (load-bearing gap), :64 (the "emerges in 1–2 generations" sentence C02's DR-DC-04 reconciles —
  quoted accurately), :65 (Milroy networks), :84 (anti-language dies with institution), :126,:132,
  :140 (koine rows + worked example), :148 (decay-discredited); `dialect-faction-map-workflow.md`
  :4-9 (registrations), :69-77 (area table + feature-relativity + comparator rule), :82 (label
  substitution caution), :84-96 (koineization table rows :86,:88,:89,:90,:91 + the no-ladder :93
  and no-deadline MK :94 cautions + standardization :96), :122,:123 (anti-language category +
  threat model), :182 (checklist), :197 (verification scope), :202; `migration-founder-effects.md`
  :4,:13-14,:18,:25,:32,:33-34,:41 ("small population means fast sound change" invalid shortcut),
  :43,:44 ("First arrivals always win" invalid shortcut), :49-50 (departure-era comparison), :52
  (no rate constants), :63 (transmission network), :184-185 (Mufwene/Trudgill-2004 registrations
  with verification levels), :202; `urban-rural-register-ecology.md` :5-7,:26,:33-34;
  `linguistic-anthropology.md` :117,:120,:122-123; `register-lexicon-ceilings.md` :12,:182,:238-240;
  `language-contact.md` :7,:89-90; `historical-linguistics.md` :237; `conlang-methodology.md` :90
  ("## Stage 6"); `register-strata-attestation.md` :25,:27,:32. Claimed line counts (209 / 205 /
  202) all reproduce.
- Couples: 11 targets claimed, all resolve (10 corpus paths on the couples line + `corpus/QUALITY.md`
  which the fragment's Citations counts under the same heading — see N1). Filename == K03's
  proposal; sort position between `conlang-methodology.md` and `historical-linguistics.md` confirmed.
- K03 §5 non-restatement criterion (E2): satisfied — `:64` is reread as a reconciliation (DR-DC-04
  keeps the figure as the attested MK case and adopts the workflow's no-deadline rule), not
  restated; `:75-77,93-94` are cited as owned cautions.
- N1 (fragment note, non-blocking): the first sighting of this fragment carried a duplicated
  self-audit bullet; the current (revised) bytes have exactly one — **fixed in revision**. The
  Citations section's "11/11 in-repo couples targets" label counts `corpus/QUALITY.md`, which is a
  `- sources:`/DR reference, not a couples token (the couples line carries 10 in-corpus paths).
  Count-the-population imprecision only; every named file resolves.

## 3. C03 — `translation-protocol-fidelity.md` (K03 E3 / claims-C topic 3: translation-protocol fidelity)

**Verdict: PASS** (three S3s: F3 sweep-count inflation ×2, F4 locator imprecision ×2; no entry-level
contract defect).

- I-C12: **PASS/review** — review hits adjudicated **false positives**: `bleed-candidate:closure`
  and `ownership-assertion-candidate:closure` are the substring `closur` inside "di**closur**e"
  (the protocol's own tier vocabulary, quoted); the `canon`/`canonical` hits are the boundary
  sentences plus the registry's own topic phrase "Canonical local glossary-entry profile" quoted at
  `glossary-registry-format.md:3`. Contract legs green (4/4, 5f, src 15/15 with locators, ptr 21/21,
  gap, decision record DR-TF-01…10 all defined with rejected alternatives).
- I-C05: 22 citations / 22 line numbers / 21 paths — 0 unresolved, 0 missing; 1 out-of-range
  (`verification-method-overview.md:209`, file has ~206-207 lines) — adjudicated with F4 below.
- **Block digest: exact.** The fragment's §3/§5 receipt pins sha256
  `2289a9b77ea116c46a14b7fb9bd0e5e4757af35da782991dc47c61fd8b8e789c`, 47 417 B — **equals my
  extraction byte-for-byte**.
- **Six digest pins: 6/6 MATCH live bytes** — `cultural-translation-protocol.md` `fb5d705b…`,
  `verification-method-overview.md` `f52708d9…` (also the digest r39's audit recorded),
  `two-reader-interop-agreement.md` `daebba3a…`, `naming-systems.md` `d972a1d6…`,
  `semantics-pragmatics.md` `9b9a3ff7…`, `sociolinguistics-registers.md` `95ea235f…` (re-hashed
  this seat, 2026-10-19).
- Absence sweeps: reproduce except two counts — `thick translation` → 1 ✓; linguistics
  `thick|translation note` → 0 ✓; linguistics `domestication|foreignization` → 0 ✓; corpus-wide
  → **5 files, same five** ✓ (the false-positive-class disposition — book title, crop/animal
  domestication, J. Z. Smith — verified at the cited lines); `paratext` → 2 ✓; `glossing` → 8 ✓.
  **F3**: `gloss` in linguistics → **12** files with ≥1 hit (claimed "13 of 21"); `interpreter`
  corpus-wide → **47** files (claimed 48). Both deltas are **+1**, and C03's §5 discloses that its
  first audit attempt briefly copied a draft into the live partition
  (`corpus/knowledge/linguistics/C03-draft.md`, sha `e34f41b4…`, removed; self-disclosed, tree
  verified clean by this seat at every stamp). The draft text contains both `gloss` and
  `interpreter`, so a sweep run inside that window reads exactly +1 on both counts. Reconstruction
  offered, not proven — the intermediate bytes are gone; recorded as the owner's one-clause fix.
- Fabrication spot-checks (~90 needles) — **all verify**; the deepest verification of the wave:
  `cultural-translation-protocol.md` :2,:4-8 (Appiah page-level registration + corroboration,
  Genette, Venuti, couples), :16 (four-way separation), :17 (analogy caution), :18 (established
  terminology), :25-27 (framework calibrations), :34,:36,:40 (contract fields), :47-53 (T0-T4
  table), :55-56 (disclosure-not-ladder + consequence dependency), :83,:86,:96,:98 (name-first,
  reference/address form, to-verify marking, typography), :111-112 (ledger minimum, separate
  dates), :118-120 (provenance types, four questions, skip-test default), :122-130 (note-location
  table), :132-134 (skeleton, one dominant job, anchoring), :136-138 (real-source, to-verify,
  "untranslatable" ban), :142/:146 (delivery adjustments), :164-166,:174-178 (scratch demo beats +
  the template note + the collar clause — quoted accurately), :189-190 (reader check, removal
  test), :192 ("Only lore can adopt world facts"), :202,:206 (provenance cautions, mediation),
  :207-209; `verification-method-overview.md` :16,:27-31 (O/I/U/D), :49-56 (claim card, to-verify
  rule), :88 (coverage gap), :93-102 (verdict vocabulary, fail-closed, issues-only), :111 ("not
  merely in the author's translation" — exact), :127-129 (the transmission-clock row is **:128** —
  F4), :150 (laundering list — exact), :163 (prose walkthrough ≠ sign-off — exact), :206 (final
  invariant — exact); `two-reader-interop-agreement.md` :3,:23,:29-35,:79 (rejected alternative —
  exact); `naming-systems.md` :82,:84-85,:94,:117,:120,:127; `semantics-pragmatics.md` :84 (§5
  heading), :86,:88,:106 ("translation between in-laws" — exact), :115,:119;
  `conlang-methodology.md` :4 (Leipzig 2008 registration — exact), :80,:88 (the 300-word floor —
  exact at line end), :120,:122,:153-154; `glossary-registry-format.md` :3,:13;
  `symbol-lexicon-colexification.md` :49,:105-106 (exact); `register-strata-attestation.md` :218
  (the declared-but-unpopulated field lesson — exact); `mamluk.md:75`; `parthia.md:116`;
  `china-song.md:104`. Line-count claim (protocol 209) reproduces.
- Couples: 11/11 resolve. Filename `translation-protocol-fidelity.md` == K03's proposal; 0
  collisions; sort position penultimate confirmed.
- K03 §5 non-restatement criterion (E3): satisfied — the entry states "The protocol's requirements
  are the fidelity criteria's target; none of them is restated here", and structurally holds: every
  protocol surface is cited as a ground, §8's criteria are the new layer.
- Process note, for the integrator: C03's §5 discloses the symlink near-miss
  (`audit-root/corpus/knowledge/linguistics/` → live partition; one transient untracked file,
  removed in the next command). This seat verified the tree clean at all its stamps (§ header).
  The incident is disclosed, bounded, and root-caused by its author; recorded here so X01 F5's
  zero-staging watch and the r39 incident row stay reconciled — no corpus byte survives.

## 4. C04 — `sacred-registers-liturgical-language.md` (K03 E4: sacred registers / liturgical language)

**Verdict: PASS-with-named-defects** (one S2: F1, the self-audit Reading-2 digest pin; no
entry-level contract defect).

- I-C12: **PASS/review** — review hits are 15 unnegated `canon`/`canonical` mentions, adjudicated
  **false positives**: they are the entry's own subject-matter term of art ("closed canonical
  corpus", "canonical strings", "canonists") plus the boundary sentences; C04's Self-audit Reading 2
  documents the same adjudication and this seat independently agrees with it. Contract legs green
  (4/4 + literal scope, 5f, src 13/13 with locators, ptr 6/6, gap, decision record SRL-1…8 with
  SRL-8 honestly open as a to-verify backlog row, bleed 0/15).
- I-C05: 32 citations / 48 line numbers / 13 paths — 0 unresolved, 0 out-of-range, 0 missing.
  Corrected binder: 13 refs, 0 out-of-range.
- **F1 (S2): the Self-audit Reading-2 digest pin does not reproduce.** Reading 2 pins "the filed
  bytes" as sha256 `019a5b4ddbe2fdafb5cd0899634266f4f9f012afa67896f9a4ad9ecd5da4d437`, 37 207
  bytes. Measured by this seat against the filed block: raw 37 206 B → `1b007b5fb9702cdd…`;
  stripped 37 205 B → `b230fb0f…`; block+`\n` 37 207 B → `ab38db99…` (size matches the pin,
  digest does not); block+2×`\n` 37 208 B → `cb7c6c3c…`. No natural staging shape yields the
  pinned digest. Reading 1's pre-reword pin (`d54dc679…`, 37 118 B) is undevelopable by design
  (intermediate bytes). Likely shape: one further in-place edit landed after Reading 2 without a
  re-pin (the r39 F5 class, but here the carried pin is *wrong*, not merely absent — hence S2).
  The audit chain is intact regardless: this seat's verdicts are readings of the live block
  `1b007b5f…`, which passes everything. Owner: C04/integrator — re-pin Reading 2 against the filed
  bytes and name the staging shape (compare C02's exact reconciliation, §2).
- Absence sweeps: **all reproduce exactly** — `event-typed` → 0; `recitation accuracy` → 1
  (`religion-language-co-evolution.md`, competence-list line at :76 ✓); `liturgical fossilization`
  → 2 (religion + `myth-symbol/binding-speech-complex.md` — the "one myth-symbol aside" ✓);
  `sacred register` → 7; `recitation` → 52; `liturg` → 86 corpus-wide, **13 of 21** linguistics ✓.
  The fragment's own r28-lesson caveat (sweeps may gain self-/sibling-match hits post-landing) is
  the correct reading discipline and is inherited by C07.
- Fabrication spot-checks (~50 needles) — **all verify**: `sociolinguistics-registers.md`
  :5,:6,:18,:32,:69-77,:74,:75,:150 (Ferguson/Fishman/Badawi-Albirini/Waquet-Pollock registrations,
  the §3 diglossia block, the professional-secret line, Pollock's era axis, the prototype-not-law
  caveat); `historical-linguistics.md` :188 ("a liturgical language freezes an older stage"),
  :237-239 (the frozen-register paragraph — the entry's §4 quote "frozen registers are time
  capsules … generates in-world philology, schisms over recitation, plot misreadings" is exact
  across the three lines), :247 (S3 sacred-freeze row); `linguistic-anthropology.md` :95-101
  (:95 structural signature, :97 "Archaism equals authority", :99 Tambiah 1968), :131 (liturgical
  decision-table row); `language-shift-obsolescence-revival.md` :103 (stage-5 "A prayer nobody
  parses" — exact), :110 (diglossic stability), :116 (Hebrew row), :143 (revival-as-emblem —
  Coptic/Latin/Sumerian exact), :145 (flattening exact), :155 (Diglossic stability row exact),
  :162-163 (reversibility); `register-strata-attestation.md` :19 (Rappaport 1999 registration),
  :3; `orality-formulaic-language.md` :21 (Staal 1961/Howard 1986 registration), :47 and :134
  (vikṛti self-checking — exact); `ritual-liminality.md:112` ("the liturgy's very invariance is
  what ma[kes it authoritative]" — the Rappaport quote as carried); `politeness-taboo-euphemism.md:104`
  ("a liturgical name-register" — exact); `naming-systems.md:3`; `semantics-pragmatics.md:84` (§5
  heading); `real-world-inspiration-boundaries.md:109` (§7 heading);
  `era-language-staging.md:4` (Ferguson/Fishman registered); and the
  `religion-language-co-evolution.md` spine — :4 (sources), :14 ("specify the event, not merely
  the religion" — exact), :16 (fossilization = selective conservation), :25 (ownership vs
  custodianship), :37 (the learned-liturgical table row), :42 (re-archaization row), :47-61 (layer
  checklist incl. :55 performance, :60 inheritance-vs-borrowing exact, :61 "Textual stability
  requires work" exact), :64-76 (event policy questions; :76 the competence-list directive —
  exact), :84-87 (boundary/leakage/outsiders/public-face — all four exact), :100 (Vedic accent as
  "cultivated sign of continuity" — exact), :106 (Larios + UNESCO caution), :115 (SC era-model
  row), :134 (custodianship-not-universal + Burt — exact), :143 (Meyendorff recension), :192-203
  (the edition/verification table — every row C04's `- sources:` rides verified: Ferguson :194,
  Haeri :195, Burt :196, Meyendorff :197, Jamison & Brereton :198, Larios :199, UNESCO :200,
  Sacrosanctum Concilium :201, GIRM :202, Schimmel :203), :205 (closing take). Every external work
  C04 cites is registered exactly where the fragment says, with the registering entry's own
  verification limits carried — **no new bibliography, no fetched source, no invented locator**.
- Couples: all resolve (same-partition basenames direct per the r39 basename-couples policy §5.4;
  `religion-language-co-evolution.md`, `era-language-staging.md`,
  `real-world-inspiration-boundaries.md` unique-basename fallback with the mapping stated here).
  Filename == K03's proposal; sort position between `register-strata-attestation.md` and
  `semantic-fields-lexicon-building.md` confirmed.
- K03 §5 non-restatement criterion (E4): satisfied — §4's first line names
  `historical-linguistics.md:237` as the owner of the fossil's *use* and builds only the mechanics;
  the six-neighbour surface table (§1) keeps every owned surface coupled, not restated.

## 5. X00 §C1 routed duty — the E1 basename-couples confusion check (discharged)

X00's Owed routes to C05/integrator: check C01's `taboo-strata-lifecycle.md` vs K03's
`taboo-euphemism-lifecycle-stages.md` against `reports/round-39/calib/basename-couples-policy.md`.
Measured 2026-10-19: **clean under either name.** Neither basename exists anywhere in
`corpus/knowledge/` (0 hits each); the corpus-wide duplicate-basename index is empty (policy §5.5's
uniqueness assumption holds and is not disturbed by either candidate); and the one existing
Tier-2 fallback consumer of a similar basename — `linguistics/sound-symbolism.md`'s couples token
`taboo-euphemism-lifecycle.md` → `synthesis/taboo-euphemism-lifecycle.md` — keeps its unique
mapping under either candidate (exact-string tokens; the `-stages` suffix changes no token).
The exact-string policy is insensitive to the visual similarity X00 flagged. The filename choice
is therefore free on basename-couples grounds and stays C06/integrator's on sort/readability
grounds (X00 §C1 rule unchanged).

## 6. Defects, severity-ranked

Tiers: **S1** blocker (structural contract), **S2** major, **S3** review/precision. **No S1.**

| # | sev | defect | evidence | owner |
|---|---|---|---|---|
| **F1** | **S2** | **C04's Self-audit Reading-2 digest pin is not reproducible from the filed bytes** (pinned `019a5b4d…`/37 207 B; measured raw `1b007b5f…`/37 206, stripped `b230fb0f…`/37 205, +nl `ab38db99…`/37 207 — size matches, digest does not). The entry bytes themselves pass this audit; the fragment's own receipt is the defect. Likely a post-Reading-2 in-place edit without a re-pin (r39 F5 class, escalated because the carried pin is wrong rather than absent). | §4 F1; digest battery run 2026-10-19 | C04 / integrator (re-pin + name the staging shape) |
| **F2** | **S3** | **C01's two registration locators are off by one line**: `- sources:` says Campbell "registered at `historical-linguistics.md:3`" and T&T "registered at `language-contact.md:3`" — both files carry `- topic:` at :3 and `- sources:` at :4 (same layout as politeness, whose bullet-level locators in the same entry are all correct). The couples-context `:3` uses in the same entry point at the topic lines and are accurate; the registration pointers are not. Substantive leg (both works registered in-corpus at the named files) holds. | §1; `sed -n '3,6p'` both files, 2026-10-19 | C01 / integrator (named-defects threshold) |
| **F3** | **S3** | **C03's sweep counts `gloss` → "13 of 21" and `interpreter` → "48 files" read 12 and 47 at the clean tree** — both +1, consistent with sweeps run inside C03's own disclosed transient window (the stray draft contains both stems; §3). Reconstruction offered, not provable (intermediate bytes gone). All other C03 sweeps reproduce exactly. | §3; recount commands 2026-10-19 | C03 / integrator (one-clause fix or window note) |
| **F4** | **S3** | **C03 locator imprecision ×2**: (a) the transmission-clock row of `verification-method-overview.md` is **:128**; the entry's in-line anchors (§8 C7, DR-TF-08, KTD-TF-S-0002) say `:129` (the adjacent reference/design row); the fragment's Citations correctly cite the range :127-129. (b) the §13 detached anchors `(\`:192\`, \`:209\`)" bind mechanically to the overview (whose :209 does not exist) but their referent is the protocol file — `:192` is exact ("Only lore can adopt world facts"); protocol :209 exists (209-line file) but its S-0001 gloss ("evidence-status marks … canon is lore-shokunin's") conflates the bibliographic caution at :209 with the canon boundary that actually sits at :192. Content support holds at both anchors; anchors and one gloss are imprecise. | §3; binder + hand reads 2026-10-19 | C03 / integrator |
| **N1** | note | C02's first sighting carried a duplicated self-audit bullet — **fixed in the mid-audit revision**; its Citations label "11/11 couples targets" counts a non-couples file (all resolve). | §2 N1 | none (recorded) |
| **N2** | note | C03's §5 discloses a symlink near-miss (one transient untracked file inside the live corpus, removed next command; tree clean at every stamp this seat took). Disclosed, bounded, root-caused by its author; recorded for the X01 F5 watch and the r39 incident reconciliation. | §3 process note | integrator (record) |

Instrument note (carried, corrected): I-C05's detached-`:n` binding defect (r39 F6) fired once
more (C01's couples line) and was adjudicated by the corrected nearest-preceding binder + hand
read — 0 masked defects. C03's §13 line shows the residual hazard class: a detached `:n` whose
referent is a file *not* named earlier on the same line resolves under no mechanical rule; C03's
shorthand convention (`:n` = the S-0001 protocol unless another file names itself) is documented in
its `- sources:` and was hand-applied here.

## 7. Staging notes for the integrator (claim C's apply step)

- **Fence shapes**: C01/C02 are 4-backtick blocks; C03 is a 4-backtick entry **plus a 3-backtick
  receipt block in the same fragment** (do not let a stager regex pick the receipt); C04 is a
  3-backtick block. The r35 stager regex matches only the 3-backtick shape (R01-10 precedent) —
  stage with a fence-run parser or by hand.
- **Pin shapes differ**: C02's self-audit pin names the stripped block (33 090 B); C03's names the
  block-with-trailing-newline (47 417 B, verified); C04's names neither (F1). Verify each landed
  file against the **entry block digest** this audit records (§0), not against the fragment
  receipts, until F1 is re-pinned.
- Four filenames at this audit's close: `taboo-strata-lifecycle.md` (C01, diverges from K03's
  proposal — contract-legal, X00 §C1), `dialect-register-consistency.md` (C02, == K03),
  `translation-protocol-fidelity.md` (C03, == K03), `sacred-registers-liturgical-language.md`
  (C04, == K03). All four sort cleanly into the 21-file listing; C06 re-derives the rows against
  this final set per X00 §C1. No basename-couples obstruction (§5).

## 8. Limits

- **Structural, not scholarly; a pass is not admission.** Nothing here judges whether the four
  topics are the right four, whether the scholarship is sound, or whether the entries should be
  promoted (`PROVINCE.md`; `corpus/QUALITY.md`). K03's scope/non-restatement criteria were applied
  as supplied; their scholarly adequacy is not re-argued.
- **No network.** Every external work is audited at its in-corpus registration status only; the
  `(to-verify)` flags (C01: edition re-checks inherited; C02: Halliday 1976 full-text attribution;
  C03: Appiah/Genette/Venuti/Waquet/Tiersma "not consulted this round"; C04: primary sources
  unconsulted, SRL-8 open) were verified as present and correctly carried, not resolved.
- **One auditor.** C07's independent verification of this audit and of C06's delta numbers is the
  round's second leg and remains owed at this file's filing.
- **Freeze:** the audited digests are §0's. Any post-audit byte change to a fragment voids the
  corresponding reading and owes a re-run. C02's mid-audit revision is reconciled in §0/§2; any
  further revision re-opens it.

## Owed

- **F1 re-pin** — owner C04/integrator (S2): Reading 2 must be re-pinned against the filed bytes
  with the staging shape named, or the receipt row struck and this audit's §0 digests adopted as
  the receipt of record.
- **F2/F3/F4 one-clause fixes** — owners C01/C03; integrator decides apply-as-is with named
  defects (claim C's threshold allows named defects) or pre-landing repairs.
- **`reports/round-40/run-validation.py`** — claims Ca/A's counting command; never executed by
  this seat (in-tree or copy), per `shared_rules[4]` and X00 §C8.
- **Post-apply sweep** — `python3 -B reports/round-28/readme/sweep.py` green at 220 == 220 belongs
  to the integrator's apply step (X00 §C8 wording rule); C04's sweep caveat (self-/sibling-match
  classification) is inherited by C07's re-run.
- **C07** — independent verification of this audit + C06's delta numbers (`targets.json`
  seat C07); this file is its input.
- **Not owed by this seat**: the four entries' admission (integrator), the README rev-2.3 bytes
  (C06/integrator), the r39 G2-G4 verification gates (routed-not-absorbed; open rows — landing
  these linguistics entries does not discharge them, `K03-gaps.md:172-174`).

## Citations

- `reports/round-40/targets.json` — `seats[id=C05].mission`; `shared_rules[0-4]`.
- `reports/round-40/claims.json:7,13-18` — baseline; claim C before/after and thresholds.
- Contract and criteria: `reports/round-40/plan/P01-plan.md:40-47,54-57` (executor gate, C05 step);
  `reports/round-40/scout/K03-gaps.md:60-153` (E1-E4 binding scopes) and `:166-177` (§5 audit
  criteria, routed-not-absorbed, byte-consistency duty); `reports/round-40/cross/X00-connector.md`
  §C1 (filename rule + routed basename check), §C2 (criteria adoption), §C8 (runner/wording rules);
  `reports/round-39/calib/basename-couples-policy.md:14-48,71-102` (§5 limits, §6 recipe).
- Audited drafts (§0 digests): `reports/round-40/cov/C01-entry-1.md`, `C02-entry-2.md`,
  `C03-entry-3.md`, `C04-entry-4.md`; staged copies under `.scratch/c05r40/stage/`.
- Instruments: `reports/round-35/cov/C12-audit-runbook.md` §5 (digest `97361027…562d`, 663 lines);
  `.scratch/c05/c05-audit.py` (sha `4326bb85…`); `.scratch/c05r40/{extract,binder}.py` (this seat).
- R precedents: `reports/round-39/cov/C05-audit.md` §0 (I-C05 digest), §5 (F1 transient), §6 F5/F6
  (pin-shape and binder classes); `reports/round-35/cov/C02-entry-2.md` Finding 4 (fence hazard).
- Needle sources read at cited lines (all listed in §1-§4): `corpus/knowledge/linguistics/{politeness-taboo-euphemism,historical-linguistics,language-contact,sociolinguistics-registers,linguistic-anthropology,register-lexicon-ceilings,naming-systems,semantics-pragmatics,conlang-methodology,register-strata-attestation,orality-formulaic-language,language-shift-obsolescence-revival}.md`;
  `corpus/knowledge/synthesis/{taboo-euphemism-lifecycle,dialect-faction-map-workflow,migration-founder-effects,urban-rural-register-ecology,cultural-translation-protocol,glossary-registry-format,symbol-lexicon-colexification,religion-language-co-evolution,era-language-staging}.md`;
  `corpus/knowledge/verification/{verification-method-overview,two-reader-interop-agreement,contact-strata-verification-gate,real-world-inspiration-boundaries}.md`;
  `corpus/knowledge/civilizations/{parthia,mamluk,china-song}.md`;
  `corpus/knowledge/myth-symbol/{binding-speech-complex,ritual-liminality}.md`;
  `corpus/QUALITY.md`; `corpus/README.md`.
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD`; `git status --porcelain` (per stamp); partition censuses
  (`ls corpus/knowledge/linguistics/*.md | wc -l` → 21; `find corpus/knowledge -name '*.md' | wc -l`
  → 216); I-C12 install + sha256 + selftest; I-C05 selftest; fence extraction ×4 (+ C03 second
  block); I-C12 over staged blocks ×4; I-C05 over staged blocks ×4; corrected binder ×4 (54 refs);
  digest batteries (C02 shape reconciliation; C03 6 pins re-hash; C04 4-shape battery; fragment
  sha256 ×5 incl. the pre-revision C02); every quoted sweep re-run verbatim (C01 5, C02 9, C03 9,
  C04 7); ~200 needle line reads (`sed -n`/`awk` per line); couples `ls` resolution; basename
  collision + duplicate-basename index checks. **Not run, deliberately**: any
  `reports/round-*/run-validation.py`; any network call; no write outside this fragment and
  `.scratch/c05r40/`.
