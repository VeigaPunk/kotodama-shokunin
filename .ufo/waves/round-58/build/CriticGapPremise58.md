# CriticGapPremise58 — claim C's substantive gap

Seat: `KotodamaR58A2.CriticGapPremise58`. Claim base: `80f48c2c6f99381c0ba971d640fc7faef88aa406`.

**Axes:** coverage is the assigned axis; depth, calibration and adjacency are the principal regression risks. Operability concerns usable decisions and the existing handoff; freshness concerns honest source/verification status. These are review dimensions, not additional claims or verdicts. Advisory critique only: no admission, integration, runtime invocation or support-row judgment.

## 1. Genuinely new ground versus repetition

**Strongest counterexample:** the filename sweep misses the literal heading `naming-systems.md:65`, **“Toponymy: functions, strata, politics,”** and its substantive treatment at :67–71. Its §5 already owns endonym/exonym introductory treatment. Thus “0 matching filenames” does not establish “0 substantive coverage.” This is not just an incidental mention.

Opened the frozen version with:

```sh
timeout 60 git show 80f48c2c6f99381c0ba971d640fc7faef88aa406:corpus/knowledge/linguistics/naming-systems.md
```

Base evidence includes functions (:67), conquest/migration strata and tautologies (:68), folk etymology (:69), political/street renaming (:70), UNGEGN/Pinyin (:71), endonym/exonym definitions (:82), contact routes (:83–85), a map-layering recipe (:118), a name ledger (:120), fake-name calibration (:129), and the lore boundary (:136). The existing header explicitly limits verification to an apparatus audit and leaves etymologies to verify (:34–35): these are coverage evidence, **not freshly verified historical facts**.

A bounded base search also returned:

```text
language-contact.md:165: Rivers, hills, and old market names keep the deepest stratum — toponymy survives conquest (Celtic hydronyms across England).
semantic-fields-lexicon-building.md:65: Toponymic strata date settlement layers: suffix chains (English -chester/-caster/-cester; Slavic -grad/-gorod) work like geological strata in era-work.
language-shift-obsolescence-revival.md:177: DR-7 already stages replace / fossilize / reclaim, with reclaim evidence explicitly thin/to-verify.
```

Command: `timeout 60 git grep -n -E 'Rivers, hills|Toponymic strata|DR-7|endonym/exonym definitions' 80f48c2c6f99381c0ba971d640fc7faef88aa406 -- corpus/knowledge/linguistics/language-contact.md corpus/knowledge/linguistics/semantic-fields-lexicon-building.md corpus/knowledge/linguistics/language-shift-obsolescence-revival.md corpus/knowledge/linguistics/translation-protocol-fidelity.md` (excerpts above omit output prefixes).

| Wave-goal surface | Already covered; not a novelty claim | Potentially genuine addition relative to inspected owners |
|---|---|---|
| Generic/specific elements and suffixes | Generic derivation machinery exists in `synthesis/naming-canon-workflow.md:54–65`; suffix examples already occur above. | A place-specific construction grammar: order, bound/free status, inflection, productivity, dialect and feature class. |
| Substrate, conquest, settlement | `naming-systems.md:68,118`; historical-linguistics already supplies sound-law/strata machinery. | A procedure discriminating retention, borrowing, calque, transfer, hybrid formation and replacement using dated forms. |
| Old river/mountain names | Explicitly present in `language-contact.md:165`. | Supported retention mechanisms, regional limits and countercases; separate feature age, naming age and witness age. |
| Endonyms/exonyms | `naming-systems.md:82–85,117`. | Language-, community-, era- and audience-indexed coexistence, including multiple local names and distinct official statuses. |
| Standardization/romanization | UNGEGN/Pinyin already at :71; rendering layers already in naming-canon workflow :61. | National/local jurisdiction versus international coordination; a scheme/version-aware place-label selection procedure. |
| Local usage, dual names, waiting rules, derogatory removal | General power/pejoration is present; inspected passages provide no policy decision table. | Source-specific principles, eligibility, consultation, exceptions and conflict handling—not one invented global rule. |
| Renaming and streets | Political renaming and the street grid already at :70. | Trigger → authorized operation → contested adoption → retained historical relation; street-address and field-name scales treated separately. |
| Field/farm names | No substantive treatment in the inspected §3/§5 passages. | Microtoponymy: oral versus cadastral records, landscape/land-use distinctions, local extent and persistence. |
| Folk etymology and handoff | Already :69,120,129,136; naming-canon workflow :65,79–96 has an evidence/meaning ledger. | Apply that existing ledger to place-name uncertainty; do not claim a second ledger or canon authority as new ground. |

No corpus-wide absence is asserted for the proposed additions. These are the missing **decisions in the inspected partial owners**, not a second filename-count argument.

[INFERENCE] Reformatting §3/§5 and attaching twenty fresh, truthful sources could improve file/citation counts without improving substantive coverage. Support for repeated statements would not itself prove novelty. `reports/round-58/accept-c.py:61–64` and `claims.json:152–158` explicitly leave uncovered-in-substance and one-way ownership to review. This counterexample was assessed by reading, not by constructing or scoring a fixture.

## 2. Twelve section headings for a deep owner

Each heading needs an output a reader cannot obtain merely by rereading the old overview.

1. **Scope and units: place identity, name-form, community and era** — boundary statement and links outward to partial owners.
2. **Element grammar: generics, specifics, suffixes and compounds** — construction table, not a suffix souvenir list.
3. **Names in contact: borrowing, translation, calques, hybrids and transfers** — operation-by-operation derivations.
4. **Reading strata: substrate, settlement and conquest hypotheses** — witness-based procedure and competing explanations.
5. **Hydronyms and oronyms: conservatism, replacement and limits of antiquity** — conditional retention matrix, not “all rivers are oldest.”
6. **Endonyms, exonyms and multilingual coexistence** — user/language/era/status matrix.
7. **Naming authorities and principles: usage, dual names, commemoration and derogatory-name removal** — jurisdiction-specific policy table including UNGEGN's distinct role.
8. **Renaming politics: triggers, contested uptake and continuity** — event table separating decree, signage, documents and speech.
9. **Romanization, transliteration and reader/map forms** — conversion decisions with scheme/version and information loss.
10. **Microtoponymy: streets, fields, farms and cadastral names** — scale/use/media matrix; do not let city-renaming examples stand in for fields.
11. **Etymology calibration: attestation, opacity and folk explanation** — evidence ladder and explicit unresolved analyses.
12. **Worked place-name dossier and lore-shokunin handoff** — one connected example exercising these decisions, labeled design-invention rather than historical evidence.

## 3. Decision tables and procedure the worldbuilder needs

The following are authoring requirements, not new historical findings or registry rows. Real-language examples and policy assertions need opened, qualifying S500–S559 evidence before entering the entry.

### A. Element grammar

| Input condition | Decision/output | Required record / failure to prevent |
|---|---|---|
| Productive feature generic + distinguishing specific | Choose the language's `G+S`, `S+G`, or other licensed construction. | Feature class, head/dependent order, agreement, linking and phonotactics; no universal English compound order. |
| Possessor, dedication or relational specific | Choose genitive/possessive, adjectival or other locally licensed morphology. | Referent and historical stage; do not paste dictionary forms together. |
| Productive bound suffix | Distinguish derivational morpheme from a free generic or accidental ending. | Meaning range, allomorphs, dialect, productive period; a suffix alone is not an ethnic census. |
| Settlement takes a river/other place's name | Record transfer or relational construction and its direction. | Separate feature IDs, name records and dates; the two places need not be equally old. |
| Borrowed/opaque inherited element | Preserve the form; identify adaptation or added generic only where supported. | Donor/recipient stage and uncertainty; never invent a gloss merely to fill the table. |

### B. Stratum-reading procedure

| Step | Operation | Stop/qualification |
|---|---|---|
| 1 | Fix the geographic referent and collect dated spellings, pronunciation and source contexts. | Distinguish copied witness, first attestation and hypothesized coinage. |
| 2 | Segment candidate generics/specifics using period-specific morphology. | Preserve alternative segmentations and an opaque outcome. |
| 3 | Compare neighboring forms, distributions and regular correspondences. | One modern lookalike is insufficient. |
| 4 | Compare retention, loan, calque, hybrid, transfer, replacement and antiquarian revival. | A conquest-only explanation is not the default winner. |
| 5 | Bracket operations against sound changes and documentary anchors. | Relative ordering is not an exact foundation date or proof of population replacement. |
| 6 | Record competing analyses and confidence per claim; use them as design alternatives. | “Unknown” is a valid outcome, not permission for a folk story to become scholarly fact. |

Reuse `historical-linguistics.md:21–54,143–173` for comparative method; specialize it to place-name evidence rather than re-teaching the entire method.

### C. Naming-authority principles

| Principle/problem | Required decision | Essential scope control |
|---|---|---|
| Local usage | Which communities, varieties, records and consultation establish usage? | Local is not necessarily singular, officially recognized, or unanimously accepted. |
| Dual/multiple naming | Dual compound, parallel official names, alternatives, or unofficial usage? | Record order, punctuation, language, extent, status and effective date; these are not interchangeable arrangements. |
| Commemoration | Who is eligible, which feature classes qualify, what waiting rule applies? | Cite the specific authority/version; never universalize a waiting period. |
| Derogatory-name removal | Who evaluates the objection and approves a replacement? | Separate historical attestation from present official use; retain provenance without requiring continued public display. |
| Standard spelling/rendering | Which domestic authority selects forms and schemes? | Standardization date does not prove universal spoken adoption. |
| International coordination | What guidance/resolution is relevant, and who has domestic decision power? | Do not turn UNGEGN guidance into a world naming legislature. |

### D. Renaming triggers

| Trigger | Options to analyze, not prescribe | Continuity/identity check |
|---|---|---|
| Conquest or regime change | Retain, replace, restore, translate, commemorate. | Distinguish decree date, actual uptake and later reversal. |
| Indigenous/local-language restoration | Restore one form, recognize parallel forms, or adopt an authorized dual form. | Identify communities, jurisdiction and competing usage; no automatic single “authentic” name. |
| Derogatory designation | Remove/replace through the applicable process. | Preserve historical source relations; do not confuse an archive label with the current preferred label. |
| Commemorative nomination | Accept, reject or defer under the applicable policy. | Eligibility and waiting rules are jurisdiction-specific. |
| Merger, split or changed feature extent | Determine whether this is renaming or a changed referent. | An entity merge/split belongs to lore, not a spelling operation. |
| Script/spelling reform | Change representation, or separately document an underlying name change. | A new romanization is not automatically a new place or new spoken name. |

### E. Name use and rendering

| Question | Required separation |
|---|---|
| What do different users call the same feature? | Language/community, era, audience, territory, endonym/exonym relation and official status. |
| What does a written conversion preserve? | Original script, transliteration scheme/version, pronunciation, romanized output and optional editorial form. |
| Which form appears on this map or in this scene? | Declared audience/era/policy; preserve alternatives instead of silently overwriting the record. |
| Do two forms match? | Form equivalence, historical name relation and feature identity are separate decisions. |

### F. Microtoponymic scale

| Register | Design decision absent from a city-renaming list |
|---|---|
| Street/address | Distinguish the street's name from address numbering, dedication and informal neighborhood usage. |
| Field/farm | Record named extent, local users, land-use/tenure context where supported, and oral versus cadastral witness. |
| River/mountain | Separate named segment/summit/massif from the whole feature; document the reach of each usage. |

**Handoff reuse:** `synthesis/naming-canon-workflow.md:79–96,147–167` already supplies entity/name IDs, meaning/evidence separation and a proposal envelope. Add place-specific content to that contract; do not create another canonical gazetteer, approval state machine or collision gate. `verification/naming-collision-gate.md:17–29` is a review specification, not proof an executable canon search ran. Lore retains feature-identity and name-selection decisions.

## 4. Calibration traps the entry must mark

- **“Every name has a meaning.”** Separate historical formation, present reference, synchronic transparency and a speaker's explanation. Unknown or opaque derivation is legitimate; a neat English gloss is not mandatory (`naming-canon-workflow.md:65,87,93–95`).
- **Pop etymology as evidence.** Sound resemblance, a modern dictionary segmentation, a tourism explanation or a rebus does not establish historical derivation. Attribute in-world explanations rather than adopting them as narrator truth.
- **Romanticized antiquity.** Opaque does not imply ancient or substrate. A recent loan can be opaque, an old formation can remain transparent, and a revived “ancestral” form may have discontinuous use. The base already makes the opacity warning in `deity-name-derivation-pipeline.md:63`.
- **“Rivers and mountains are the oldest layer.”** State a source-bounded tendency and mechanisms, not a ranking guaranteed for every feature. Check renaming, transferred names, revived forms and documentary survival; feature age is not name age.
- **Suffix → conquest → ethnicity.** Reused productive elements, fashion, analogy, transfer and borrowing are competing explanations. Name distributions do not by themselves establish a homogeneous population or exact settlement chronology.
- **Tautology hunting.** The old owner itself flags the viral “Torpenhow Hill” story (:129). Verify both the feature's existence and each linguistic analysis; do not use an attractive multi-hill example to prove a universal layering rule.
- **One local name / one official name.** Avoid collapsing multiple local language communities, unofficial usage and institutional recognition. Do not classify every different spelling as an exonym or treat romanization as translation.
- **Every renaming is a coup, every standard is neutral.** Separate commemorative, administrative, restorative, derogatory-removal and representational changes. Record policy goals and contested uptake without inventing universal motives.
- **Inherited example = fresh provenance.** Do not copy the base's anomalous `Leningrad→Petrograd→Leningrad→St Petersburg` chain (:70), tidy long-distance transmission chains, or UNGEGN summaries without fresh support. This review has not externally reverified them.
- **Quota saturation.** Twenty rows, ten hosts, many language-specific scouts or twelve headings cannot substitute for missing grammar, field-name, authority or uncertainty decisions. LOCATE/TOPIC/stem overlap are not semantic entailment or evidence of new coverage.

## Smallest safe correction and no-trade boundary

**Fixable before drafting:** disclose the old overview explicitly and make the new owner the **place-specific analysis/design system** above. Point one-way to `naming-systems.md` §3/§5, historical method, the established naming workflow, sacred-topography's site/route institution, and deity-name derivation for divine-name machinery. Preserve the frozen predicate, ID range and ownership contract; do not change the metric to conceal overlap.

**Impacted axes:** duplicate overviews inflate coverage without adding decisions; forced etymologies and universal antiquity/policy claims risk depth and calibration; a second gazetteer/canon authority harms adjacency and operability; inherited bibliography presented as freshly opened evidence harms freshness/provenance.

**Unacceptable trade to submit to canonical judgment:** a larger file/source count does not compensate for those regressions. If the delivered entry merely repeats the old owners or needs false certainty to look deeper, the substantive coverage premise remains unsupported regardless of a mechanical count. This seat supplies the counterexample and repair, not an admission verdict.

Evidence work: local reads and bounded synchronous read-only git commands only. No external pages or registry rows offered; no rowcheck, acceptance command, tests, background jobs or runtime invoked. Only this scoped report was written.

installs: none.
