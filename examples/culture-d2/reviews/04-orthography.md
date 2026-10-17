# Review — component 04-orthography (culture D2)

- reviewer: round-4 REVIEW worker, completing the missing round-3 review
- target: `examples/culture-d2/components/04-orthography.yml` (560 lines)
- reviewed sha256: `fa0d2000539cf63921b9629d320a96b359888b044f11bc486032aa76e0faade6`
- status: **FINDINGS — not CLEAN**
- counts: **6 violation findings; 5 review/integration flags; 11 numbered review records**
- canon: **NON-CANON** design review; lore-shokunin owns canon

## Scope and evidence

Read the target in windows 1–120, 121–240, 241–360, 361–480, and 481–560.
Read `corpus/knowledge/linguistics/writing-systems.md` completely in two windows
(1–120, 121–159). Checked relevant passages of the shared brief, delivered
phonology, lexicon, era calendar, rank rules, and kin-address components;
those passages are interface checks, not full sibling-component reviews.
Additional corpus bases are cited below. No external historical source was
newly verified, and no invented real-world citation is supplied.

## Violations

Each row identifies this component's defect and its corpus basis. Encoding
ambiguity is not universally forbidden in natural scripts; the findings concern
missing rules or unacknowledged losses in this component's claimed phonology fit.

### ORT-V01 — the component is not valid YAML

`04-orthography | normal YAML loading fails | corpus/QUALITY.md item 4 (usability); corpus/knowledge/linguistics/writing-systems.md §8.7 (machine-readable handoff)`

- At target line 108, `consumed_from: 02-phonology (shared key name: phonology)`
  contains an unquoted `: ` inside its scalar. Psych rejects the delivered file
  at line 108, column 47: `mapping values are not allowed in this context`.
- CK-07 also closes its flow map at line 533 before adding a block `follows:`
  key at line 534. An isolated parse of these two unchanged lines fails too.
- Quote the former scalar and keep CK-07's fields inside one mapping in a future
  fix. No syntax repairs were applied here; the full-file parse remains red.

### ORT-V02 — no encoding for licensed vowel-initial words

`04-orthography | the abugida has no declared vowel carrier or independent-vowel rule | corpus/knowledge/linguistics/writing-systems.md §3.3, §6 Step 0, §8.1–§8.3`

- The interface permits `(C)V(C)` (line 114); delivered 02 explicitly licenses
  word-initial empty onsets (02 P-2, lines 131–133).
- G-C01..G-C15 and G-V01..G-V04 provide only consonant letters with inherent
  `/a/` and four marks placed on a letter (target lines 420–429). There is no
  declared independent vowel, zero-consonant carrier, or standalone-mark rule.
- The file's own O-T11 `ashu` (line 481) therefore lacks a specified first
  syllable spelling. G-S01 is a trade-copy classifier, not a vowel carrier.
  Supply a rule and inventory cost, or explicitly declare the intended loss;
  do not silently add an onset or assume a donor convention that is unbuilt.

### ORT-V03 — coda letters collide with inherent-vowel letters

`04-orthography | bare-coda use has no vowel-suppression/disambiguation rule | corpus/knowledge/linguistics/writing-systems.md §3.3 (inherent vowel and virama), §6, §7.2`

- AD-03 gives consonant letters inherent `/a/` unless a vowel mark overrides
  (lines 332–335); G-C says the same n/l/r/s letters serve as codas without
  separate E2 coda forms (lines 420–424). No killer, syllable boundary, or
  contextual algorithm distinguishes these uses.
- Witness: legal `/pan/` and `/pana/` both give the class sequence `P N` under
  the stated rules. A word boundary cannot resolve it: the final N can be
  coda `/n/` or onset plus inherent `/na/`. The same problem affects native
  coda-bearing terms such as `sul`, `hur`, and `tamur`.
- Add a suppression/reading rule and contrastive witness, or label this a
  deliberately lossy orthography rather than claiming the coda fit is solved.

### ORT-V04 — the tally-to-numeral mapping is not operationally specified

`04-orthography | incompatible or unseparated positional coordinates leave the number reading underdetermined | corpus/knowledge/linguistics/writing-systems.md §7.6 (numeral plumbing), §8.2`

- SP-3 makes low/high rungs encode valley/high-pasture accounts (lines 66–71),
  while T-03 assigns those rungs units/tens/hundreds (lines 202–210). T-02
  validates seasonal pole against rung station. No rule separates account,
  pole, and magnitude coordinates on the three-staff frame.
- T-03 fixes magnitude upward, but T-05 reverses reading direction by season
  and says the wrong direction necessarily changes the number (lines 223–231).
  With fixed place values, traversal order alone does not change the value:
  one unit on the low rung and two tens on the next are 21 either way. If
  seasonal orientation instead reassigns places or spoken digit order, say how.
- AD-07 then makes script magnitude run down the column, with blank zero
  positions (lines 355–362), without a worked cord-to-column conversion or
  fixed slot rule. Define the coordinate/read-out functions and show, for
  example, 21 and 201 in both seasons and on the page. The visual ascent/descent
  coupling is plausible, but it does not itself supply a decoder.

### ORT-V05 — the first written attestation supplies TAQ, not TPQ

`04-orthography | AD-01 reverses the bound on names in writing | corpus/knowledge/synthesis/loanword-material-dating.md §2 (lines 33–37)`

- AD-01 says the first L-side documents listing D2 names give a *terminus post
  quem* for D2 names in writing (target lines 320–327).
- If an original witness is securely dated to t, that representation existed
  **by t**: a TAQ for its entry into the documented register, not evidence it
  could not occur before t. Without a secure witness date, no dated bound has
  yet been established. An earliest survivor is not necessarily the first use.
- Keep the correct separation of L-side recording, script arrival, and D2
  adoption; change only the event/bound inference in a future fix.

### ORT-V06 — local eras are not reconciled with the shared era contract

`04-orthography | recording and script stages use conflicting E-labels without an alias map | corpus/knowledge/synthesis/era-language-staging.md §4, §7, §11.3; corpus/knowledge/linguistics/writing-systems.md §7.8`

- Target lines 161–165 define E0 as memory-only, E1 as tally, E2 as script
  arrival, and E3 as the reform. Its records index dates the corresponding
  institutions and signs with the same labels (lines 130–158).
- Shared brief CP-07 and `contract.era_tags` instead fix E0=tally, E1=arrival,
  E2=literate anchor, with E3 assigned by component 09. The brief explicitly
  requires a declared mapping for pre-contract labels (01, lines 176–184).
  Delivered 02 uses E0/E1 in that contract sense; 09 ER-07/08/09 also confirms
  arrival/literate/prospective-reserved stages (09, lines 189–224).
- No alias mapping occurs in 04. As written, its E1 cord-keeper and E2 script
  arrival cannot be merged by label with their consumed interfaces. Supply
  an explicit mapping/substage treatment and resolve E3 with the era owner;
  do not mechanically shift every institution or speech stage together.

## Review/integration flags — not additional violation findings

### ORT-F01 — accent policy needs a stage/register reconciliation

AD-05/G-P01 mark non-initial accent at local E2 and require marks on names and
numerals at E3 (target lines 340–347, 430–434). OR-04 adds loans to the E3
obligation and calls the ledger shallow (lines 384–390). The delivered native
`sára/sará` contrast (02 AC-3; 05 `pitch_accent`, lines 82–86) and grammatical
shifts need an explicit policy outside those named classes; global shallow
readability has not been demonstrated. Test ordinary words as well as names.

There is also an already-reported interface conflict: 14 A10/ES2 says accent
marks are absent until later (14, lines 196–199, 267–278), while 12 SR-05 says
the lowland script cannot mark the tune (12, lines 346–356). A donor abjad,
an adapted abugida, lexical pitch, and a legal recitation tune might be distinct
stages/domains, so this is **not** proof all those statements are incompatible.
Map eras and registers first; then have the integrator disposition the conflict.
Basis: `writing-systems.md` §6 (depth and tone marking), and
`corpus/knowledge/synthesis/era-language-staging.md` §4–§5.

### ORT-F02 — distinguish drawn signs from learned conventions in the price

The G-TOTAL sum is arithmetically correct: 15+4+1+1+4+10=35 (target line 451).
However, G-N calls all ten values numeral *figures* while zero is an empty slot,
and G-U counts a word gap explicitly called "not a sign" (lines 440–449).
On the stated zero/spacing policy those are 33 drawn units plus two positional/
spacing conventions, not 35 drawn glyphs. LI-03's "about 30" counts 31 units
before the four separators (lines 509–511); it is an approximate, partial
budget, not an arithmetic failure. Align the categories, supply the scribe-level
training cost, and reprice after resolving V02/V03 rather than preserving 35
as a target. Basis: `writing-systems.md` §7.4, §8.3.

### ORT-F03 — two hands are not automatically digraphia

SD-08 explicitly says "Two hands, one script" while declaring digraphia
(lines 301–309); RD-03 repeats that label. The cited corpus §4 defines digraphia
as one language in **two scripts**, while §7.5 separately covers hands and
registers. Call this a hand/register split, or explicitly establish an abjad/
abugida dual-script analysis if that is intended. Shared ancestry or rotated
orientation alone does not settle the classification. Basis:
`writing-systems.md` §1, §4, §7.5.

### ORT-F04 — some assumed-interface questions have already been answered

02's delivered interface adopts P-D2-PHON with no segmental deltas and supplies
the accent rule and minimal pair (02, lines 62–72). Its inventory has 15 C,
5 V, the same template/codas, and pitch accent rather than lexical tone.
05 supplies the pair's senses (05, lines 82–86). Thus 04's assumed-interface
status and OQ-01/OQ-04 should be reconciled against those deliveries, not treated
as evidence that the information is still missing. Donor L's glyphs, phonology,
and source history remain genuinely unbuilt under AD-00/OQ-03; they were not
verified by this review. Basis: `writing-systems.md` §6 Step 0, §8.1.

### ORT-F05 — several corpus section pinpoints are wrong

SD-07/LI-01 cite §2 for felt need and institutional backing, but that lesson
is in `writing-systems.md` §3.4 (line 67). AD-05/G-P01 cite §2 for Pahawh-style
marking and the usual under-marking of tone; the relevant material is in
§3.4/§6 (lines 66, 131). The entry exists; these are pinpoint errors, not
fabricated scholarship. Correct the references without implying lexical
pitch accent and tone are identical. Basis: the named corpus passages and
`corpus/QUALITY.md` item 1 (checkable provenance).

## Checks that hold, and limits

- The E1 tally is explicitly non-phonetic in the drill. Its uncertain in-world
  interpretation does not turn quipu research into a demonstrated phonetic
  precedent (T-00; `writing-systems.md` §1–§2).
- Script arrival is external, through L-side trade documents; the abjad-to-
  abugida patch is a plausible design mechanism, not a universal script ladder
  (§2, §3.2–§3.3). The notch-to-accent inheritance is a design proposal, not a
  fabricated historical claim. Repairing the decoder need not replace this idea.
- The 15-C/5-V cluster-light profile supports an abugida candidate. SD-01's
  approximately 480-sign heuristic follows the corpus §6 formula; it is not an
  exact enumeration of licensed syllables and was not treated as one here.
- Media survival, bilingual keys, scribal succession, and monumental/market/
  ledger variation are present (§4–§5, §7.5, §8.5–§8.6). Beliefs remain attributed;
  the knot is not used as a binding/obligation cosmology. No canon was decided.

Verification performed on the delivered files:

1. `ruby -rpsych -e 'Psych.parse_file(ARGV.fetch(0))' examples/culture-d2/components/04-orthography.yml`
   → **exit 1**, syntax error at line 108, column 47. Exact CK-07 fragment
   (lines 533–534) also fails Psych parsing; this is not a repaired-file pass.
2. Ruby `YAML.safe_load` with `Date` permitted loads 02 successfully: **15 C,
   5 V, `(C)V(C)`, `tones: 0`**; delivered interface says "ADOPTED with no deltas".
3. A small in-memory witness model of the declared inherent-/a/ and bare-coda
   rules reproduces `pan -> P N` and `pana -> P N`; this is a test of the prose
   specification, **not** a production script renderer or a passed gate.
4. Only this review file was written. No component, corpus entry, gate, fixture,
   or log was edited, and no commit was made. The full gate battery was not run;
   its round-4 close remains the integrator's unchanged check. This review makes
   no claim that the component or assembled packet currently passes it.
