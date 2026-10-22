# Scribe Sec 08 — Emergence, families and diachrony (claim C entry)

## Assigned item

Section `## 8. Emergence, families and diachrony` of `corpus/knowledge/linguistics/sign-languages-manual-modality.md`
(budget 15 lines, counting the H2 line and blank lines): a table covering emergence by cohorts
(Nicaraguan Sign Language), sign-language families independent of the surrounding spoken languages
(French Sign Language / American Sign Language; British, Australian and New Zealand Sign Language),
historical attestation of deaf signing (Plato, *Cratylus* 422e), and what a fictional sign language's
history must record. Sources to open: Senghas, Kita & Özyürek 2004 Science abstract; Glottolog family
pages for the French Sign Language family and the British Sign Language family; Perseus Digital Library
text of Plato, *Cratylus* 422e. Leaf seat: no delegation, no background jobs.

## Draft section text (ready to paste; 15 lines counted)

```markdown
## 8. Emergence, families and diachrony

| Question | Evidence | Source |
| --- | --- | --- |
| How do sign languages arise? | Nicaraguan Sign Language arose among deaf Nicaraguans over ~25 years; successive child cohorts turned early gestural signing into a linguistic system | NEW-ScribeSec08Diachrony-1 |
| What are they related to? | Genealogically to other signed languages, not spoken neighbours: ASL classifies inside LSFic, the French Sign Language pseudo-family | NEW-ScribeSec08Diachrony-2, -3 |
| The British strand | BSL, Auslan and NZSL form the BANZSL subgroup within BSLic, argued on lexical and historical evidence | NEW-ScribeSec08Diachrony-4, -5 |
| Deep attestation | Plato's *Cratylus* 422e has Socrates propose signalling with hands, head and body when there is no voice | NEW-ScribeSec08Diachrony-6 |

A conlang's sign history must record: the founder cohort (a school or village
generation) whose peer learning became the grammar (NEW-ScribeSec08Diachrony-1);
its signed lineage — which manual family it descends from, never the ambient
spoken language (NEW-ScribeSec08Diachrony-2–-5); when and how it was first
attested (records, documents, signatures); and any later cohort's re-analysis,
like NSL's grammar-fixing children (NEW-ScribeSec08Diachrony-1).
```

Line count: 15 exactly (H2, blank, table header, separator, 4 rows, blank, 6 method lines).
Every factual cell cites a NEW-id; the method block is design guidance. Respectful terminology only
(deaf Nicaraguans, signers, sign languages); no clinical, education-policy or legal rulings.

## Sources opened this round (registry rows; L1 renumbers)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-ScribeSec08Diachrony-1 | Senghas, Kita & Özyürek 2004, "Children creating core properties of language", Science 305:1779–1782 (article abstract) | paper | B | emergence of Nicaraguan Sign Language by child cohorts | Abstract | successive cohorts turned early gestural signing into a linguistic system | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec08Diachrony-2 | Glottolog 5.3, LSFic pseudo-family (lsfi1234), French Sign Language family node | dataset | A | existence and naming of the FSL-rooted family node | Page heading | an LSF-named pseudo-family node exists; FSL (fren1243) and ASL (amer1248) classify under it | mined | 2026-10-22 | 90d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec08Diachrony-3 | Glottolog 5.3, American Sign Language languoid (amer1248) | dataset | A | ASL's genealogical placement | JSON classification array | ASL's lineage runs through LSFic, not through English | mined | 2026-10-22 | 90d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec08Diachrony-4 | Glottolog 5.3, BSLic pseudo-family (bsli1234), British Sign Language family node | dataset | A | BSLic family and its BANZSL subgroup | Comments on subclassification | the BANZSL subgroup is argued on lexical and historical evidence | mined | 2026-10-22 | 90d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec08Diachrony-5 | Glottolog 5.3, BANZSL family node (banz1243) | dataset | A | membership of BSL/Auslan/NZSL | JSON newick field | British Sign Language and New Zealand Sign Language (with Auslanic/Auslan) are children of BANZSL | mined | 2026-10-22 | 90d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec08Diachrony-6 | Perseus Digital Library, Plato, *Cratylus* (Burnet ed.), section 422e | book | A | wording of Cratylus 422e | section 422e (Stephanus milestone) | manual/bodily sign-making is imagined when there is no voice | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |

## Gate lines

- NEW-ScribeSec08Diachrony-1 — https://pubmed.ncbi.nlm.nih.gov/15375269/ — accessed 2026-10-22 — Abstract: "Successive cohorts of learners extended this procedure, transforming Nicaraguan signing from its early gestural form into a linguistic system."
- NEW-ScribeSec08Diachrony-2 — https://glottolog.org/resource/languoid/id/lsfi1234 — accessed 2026-10-22 — Page heading: "Pseudo Family: LSFic"
- NEW-ScribeSec08Diachrony-3 — https://glottolog.org/resource/languoid/id/amer1248.json — accessed 2026-10-22 — classification array: "name": "LSFic", "id": "lsfi1234"
- NEW-ScribeSec08Diachrony-4 — https://glottolog.org/resource/languoid/id/bsli1234 — accessed 2026-10-22 — Comments on subclassification: "The BANZSL subgroup is argued by Adam Schembri and Kearsy Cormier and Trevor Johnston and David McKee and Rachel McKee and Bencie Woll (2010)"
- NEW-ScribeSec08Diachrony-5 — https://glottolog.org/resource/languoid/id/banz1243.json — accessed 2026-10-22 — newick: "'British Sign Language [brit1235][bfi]-l-':1,'New Zealand Sign Language [newz1236][nzs]-l-':1"
- NEW-ScribeSec08Diachrony-6 — https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0059/tlg005/tlg0059.tlg005.perseus-grc2.xml — accessed 2026-10-22 — section 422e (Stephanus): "ἆρʼ οὐκ ἄν, ὥσπερ νῦν οἱ ἐνεοί, ἐπεχειροῦμεν ἂν σημαίνειν ταῖς χερσὶ καὶ κεφαλῇ καὶ τῷ ἄλλῳ σώματι;"

All quotes ≤25 words, verbatim from what was opened.

## Evidence and provenance notes

- **Senghas et al. 2004.** Science.org DOI page returned HTTP 403; the same article abstract was opened
  via PubMed (PMID 15375269, Science 305:1779–1782, DOI 10.1126/science.1100199). The quote above is
  the exact Abstract sentence; it supports the cohort-emergence row (25 years, successive cohorts,
  gestural → linguistic).
- **Glottolog 5.3 — French strand.** The family node is named LSFic (`lsfi1234`); the French Sign Language
  languoid `fren1243` and American Sign Language `amer1248` both classify under it (fren1243 page tree
  path `sign1238/deaf1237/lsfi1234/fren1243`; amer1248 JSON classification array lists LSFic). Row 3's
  dictionary is the JSON array entry `"name": "LSFic", "id": "lsfi1234"`.
- **Glottolog 5.3 — British strand.** BSLic (`bsli1234`) is the BSL family node; its comments record that
  the BANZSL subgroup is argued by Schembri et al. (2010) and Johnston (2003), with lexicostatistical
  evidence (Johnston & Schembri 2007:60–66; Woll 1987) and historical evidence (Woll et al. 2001:28).
  BANZSL (`banz1243`) JSON newick lists British Sign Language and New Zealand Sign Language as children,
  alongside the Auslanic branch (Auslan). This supports the "BSL, Auslan, NZSL" family row.
- **Plato, *Cratylus* 422e.** The Perseus hopper was busy throughout (HTTP 503 / "Perseus is busy");
  I opened the same Burnet Greek text from the PerseusDL canonical-greekLit corpus file
  `tlg0059.tlg005.perseus-grc2.xml` (line 1452, milestone `n="422e"`, `<said>` by Socrates — the full
  sentence was read verbatim). The quote is the final clause of that sentence: "…ἆρʼ οὐκ ἄν,
  ὥσπερ νῦν οἱ ἐνεοί, ἐπεχειροῦμεν ἂν σημαίνειν ταῖς χερσὶ καὶ κεφαλῇ καὶ τῷ ἄλλῳ σώματι;"
  ("…should we not try, as the mute do, to make signs with hands, head and the rest of the body?").
  The Fowler translation was cross-checked on a Perseus-sourced mirror (pub22.net, Steinù marker 422e);
  Fowler's 1921 wording "as dumb people actually do" is quoted only verbatim where relevant, never used
  as our label.
- **Observation (not blocking).** The Glottolog LSFic page comment reads "Earley independent origin"
  (sic) — a source typo, not reproduced in the draft.

## Result

- Section 8 drafted at exactly 15 lines, in the contract's pipe-table style, with every factual cell
  carrying a NEW-id; no `(to-verify)` needed because all cited rows were opened this session.
- No lane file was edited, created or deleted except this report; no git/jj commands were run; no
  installs were made (all fetches used existing tooling; curl was used only to open URLs that the read
  tool could not reach, writing to /tmp only).

## Unrun checks / handoff

- Entry-wide integration is the L1's job: 226→227 count, `corpus/SOURCES.md` used-by cells,
  `corpus/README.md` index, and the section's position among the numbered H2s of the entry.
- If a live Perseus hopper load is required (rather than the canonical Perseus text file), re-open
  https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0171%3Atext%3DCratylus%3Asection%3D422e
  before final merge; it was unavailable during this session.
