# ScribeSec11Build — claim C entry, section 11 (Decision table and build order)

- Seat: KotodamaR51a3.ScribeSec11Build (leaf; no subagent dispatch). Lane: `kotodama-shokunin`, base `bff83ba65bf9559af4d7567e81703059667a0005`, branch tip `5ab3634`.
- Assigned item: section `## 11. Decision table and build order` of the claim-C entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, within a 24-line budget, per the section plan 1–15 (11 = decision and build).
- Read before drafting: `reports/round-51/claims.json`; entry contract `corpus/lessons/`-adjacent `.ufo/waves/round-50/build/ReviewEntryContract.md` §2; model entries `culture-material/pastoralism-animal-husbandry.md` (§11) and `culture-material/hunting-foraging-subsistence.md` (§9–§11); `corpus/QUALITY.md`; `PROVINCE.md`; `corpus/knowledge/verification/calibration-registry.md:35-39`; `corpus/SOURCES.md` (last row S070); `corpus/README.md` (linguistics index, footer). The C entry file does not exist yet (glob of `corpus/knowledge/linguistics/*` shows no `sign-languages-manual-modality.md`); section 11 is drafted to paste, with cross-references to the entry's planned sections (H2 numbers 1–15, max referenced §10).

## 1. Drafted section text (24 lines, ready to paste)

```markdown
## 11. Decision table and build order

Unanchored rows are the lane's design heuristics (**H**, `calibration-registry.md:38`); each check names the entry section that owns the detail.

| If your culture… | then the sign system needs… | and check |
|---|---|---|
| has a Deaf community whose members meet daily — schools, clubs, households | a conventionalized deaf-community sign language, transmitted across generations, with its own history and registers | §3; `phonetics-phonology.md:201` — manual parameters carry contrast |
| has only isolated deaf members, no signing community around them | homesign — a private, improvised gestural system, not a community language | §9; `syntax-typology.md:99` — don't assert a default word order for homesign |
| is a small community with high hereditary deafness | a village/shared sign language that hearing neighbours also learn; expect expansion beyond the deaf cohort | §3; NEW-ScribeSec11Build-1 |
| uses visible signing only for a restricted purpose — ritual silence, market, military, hunting | an alternate or manual code with a limited lexicon, not a full sign language | §9; `conlang-methodology.md:36` — start from the society's need |
| wants sign used alongside a spoken language by bilingual signers | contact signing: mouthing, loan signs, code-switching, with clear boundaries from the full language | §10 |
| wants to record its sign language — literature, law, dictionaries | a notation that segments handshape, location and movement; never a pictographic transcript | §10; `writing-systems.md:20-21` — featural scripts encode features; semasiography is not writing proper |

1. **Community census** — map who signs: a Deaf-only circle, a mixed hearing-and-Deaf city, or one village with hereditary deafness (decides the §3 type). *Artifact: signer-population map.*
2. **Iconicity budget** — fix how much of the vocabulary is transparent form-meaning mapping versus arbitrary (§7). *Artifact: iconicity dial setting.*
3. **Manual phonology** — choose handshape, location and movement inventories and their constraints; contrast lives in these parameters (`phonetics-phonology.md:201`). *Artifact: manual-parameter chart.*
4. **Grammar in space** — decide spatial verb agreement, layout of discourse, and classifier use (§6). *Artifact: spatial-grammar sketch.*
5. **Contact and notation** — set loan-sign direction, mouthing, and whether the culture writes the language down (§10; `writing-systems.md`). *Artifact: notation sample and contact rules.*

| ID | Decision | Trigger | Failure if skipped |
|---|---|---|---|
| DR-SGN-01 | Fix the community type before any grammar | any sign-language brief | a full language built for an isolated signer, or a homesign imposed on a village |
| DR-SGN-02 | Set the iconicity budget before coining signs | lexicon work begins | an all-transparent "pantomime" stock — the disallowed frame — or an all-arbitrary stock that reads as a spoken conlang in disguise |
| DR-SGN-03 | Choose the manual parameter set (handshape × location × movement) before the lexicon | coining names | a lexicon that cannot be produced fluently or kept distinct in space |
| DR-SGN-04 | Decide notation and contact before any record or loan | literature, archives, bilingual settings | treating a notation as the language itself (`writing-systems.md:21`), or inventing loan signs with no source direction |
```

Line count: 24 exactly (H2, 1 blank, preamble, 1 blank, table head, separator, 5 rows, 1 blank, 5 build steps, 1 blank, record head, separator, 4 rows).

## 2. Source opened this round (one, as permitted) — registry row and Gate line

Opened: Sandler, Meir, Padden & Aronoff 2005, "The emergence of grammar: systematic structure in a new language", *PNAS* 102(7):2661–2665, doi 10.1073/pnas.0405448102, PMID 15699343. Fetched verbatim via NCBI E-utilities (efetch) on 2026-10-22; the journal's own page returned HTTP 403 (PNAS site blocks; the Europe PMC and publisher pages were tried and failed). Canonical public URL: https://pubmed.ncbi.nlm.nih.gov/15699343/.

Registry row (exact column order; id NEW-<SeatName>-<n>, to be renumbered by the L1 to S071+):

```
| NEW-ScribeSec11Build-1 | Sandler, Meir, Padden & Aronoff 2005, The emergence of grammar: systematic structure in a new language, PNAS 102(7):2661–2665, doi 10.1073/pnas.0405448102 — https://pubmed.ncbi.nlm.nih.gov/15699343/ | paper | A | emergence of a village sign language (Al-Sayyid Bedouin Sign Language) in a community with high hereditary deafness; the pace of grammatical emergence | Abstract, second sentence | Al-Sayyid Bedouin Sign Language arose in the last ~70 years in an isolated endogamous community with high recessive prelingual deafness; systematic grammatical structure emerged within one generation, with word orders independent of the ambient spoken and signed languages | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
```

Gate line:

```
- NEW-ScribeSec11Build-1 — https://pubmed.ncbi.nlm.nih.gov/15699343/ — accessed 2026-10-22 — Abstract, sentence 2: "an isolated endogamous community with a high incidence of nonsyndromic, genetically recessive, profound prelingual neurosensory deafness"
```

Quote is verbatim from the fetched record, 16 words, location "Abstract, second sentence". Tier A: primary original research for its exact scope (village-sign emergence). Used by the section for the "high hereditary deafness → village/shared sign language" decision row; the "one generation" emergence fact is paraphrased in `teaches` and can be mined by the entry's §3 typology section.

## 3. Evidence — in-corpus anchors (re-read at the lane worktree this session; corpus bytes equal base bff83ba)

- `corpus/knowledge/linguistics/phonetics-phonology.md:201` — "Sign-language phonology works without acoustics — handshape, location, movement carry contrast (Sandler & Lillo-Martin 2006); deaf cultures need this layer." Supports rows/steps citing manual parameters carrying contrast.
- `corpus/knowledge/linguistics/syntax-typology.md:99` — "Claims that SOV is 'the human default' draw on emerging sign languages and homesign (e.g., Nicaraguan Sign Language research); suggestive, interpretively contested — don't assert it flat." Supports the homesign row's "don't assert a default word order".
- `corpus/knowledge/linguistics/conlang-methodology.md:36` — "Rule (Rosenfelder 2010; Peterson 2015): start from the society, not the phonemes." Supports the alternate-code row's "start from the society's need".
- `corpus/knowledge/linguistics/writing-systems.md:20-21` — featural (supplementary class) row ("distinctive phonetic features") and semasiography row "(not writing proper) — meaning directly, not speech". Supports the notation row and DR-SGN-04.
- `corpus/knowledge/verification/calibration-registry.md:38` — H code definition (heuristic, label the designer's choices).
- Entry-internal references: §3 typology, §6 grammar in space, §7 iconicity, §9 alternate/homesign, §10 contact and writing (planned numbering 1–15; no § reference exceeds 15).

## 4. Result and compliance

- Decision table: 5 rows (required 5–7); build order: 5 numbered steps each ending in `*Artifact: …*`; decision record: 4 rows, IDs DR-SGN-01…DR-SGN-04 (required 4–6; prefix DR-SGN unused in corpus/reports).
- Section is exactly 24 lines including H2 and blank lines (budget 24). Pipe tables with `|---|` separator, blank line before and after each.
- Terminology: deaf/Deaf (community), signers, sign languages, homesign, manual codes; no "deaf-mute", "dumb", "hearing-impaired"; sign languages are never framed as deficient or as pantomime (DR-SGN-02 names the pantomime frame as disallowed).
- Every factual claim carries either a NEW-id (NEW-ScribeSec11Build-1), an in-corpus `path:line` (above), or is declared a lane design heuristic (H) in the preamble. No `(to-verify)` needed because nothing unverifiable is asserted.
- Conlang/worldbuilding method only; no clinical, education-policy, legal, or rights rulings; no handoff text (handoff belongs to the entry's §15, another seat).
- Claim-C must-not-cite list respected: neither `corpus/lessons/round-51.md` nor `reports/round-51/boundary-count.py` is named. No S-id from S071 upward is cited by this section (the NEW-id is for the L1 to renumber).
- Frontier: one SOURCES row drafted (above), status `mined`, opened 2026-10-22, used-by the entry path; the L1 renumbers NEW-ScribeSec11Build-1 into the S071+ block and appends the Gate line to `corpus/lessons/round-51.md`.

## 5. Unrun checks and limits

- The entry file, README index, SOURCES append, and round lesson are landed by the L1 at integration; this seat drafted text only and wrote only its own report.
- Sibling section drafts were not read (not yet written when this seat ran); Section 11's `§N` cross-references assume the planned numbering 1–15, which the L1 owns.
- Not run: sweep, provenance gate, couples resolver, section-2.9 checker (integration-time; the entry does not exist yet).
- The PNAS publisher page and Europe PMC returned HTTP 403; the abstract was read via NCBI E-utilities (official API), quote verified verbatim. No installs; no lane files other than this report were created or edited; no git/jj state touched.
