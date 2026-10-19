- Seat: K03 | scout | C | date 2026-10-19 | baseline fd55e1f

# Gap scout — G2/G3/G4 + the fourth, with sources and the linguistics-partition collision check

## 1. Baseline measured (not asserted)

- Linguistics partition = 21 files (`ls corpus/knowledge/linguistics/*.md | wc -l` → 21,
  2026-10-19, lane root). Verification = 24 (`ls corpus/knowledge/verification/*.md | wc -l`
  → 24), confirming r39's expansion landed and linguistics is now the thinnest
  non-verification partition — claim C's premise holds.
- Routing fact from git (the collision check depends on it): r39's verification
  expansion was `contact-strata-verification-gate.md` (G1) plus three process entries
  (`worked-example-verification.md`, `index-sweep-verification.md`,
  `append-only-record-verification.md`) in commit `fd55e1f`
  (`git log --diff-filter=A --name-only -- corpus/knowledge/verification`). **G2/G3/G4
  verification gates were NOT landed at r39** — `ls corpus/knowledge/verification/ |
  grep -c 'lifecycle-gate\|dialect-register\|translation-protocol'` → 0. So this round's
  linguistics entries face no verification-partition duplicate, and the three future
  verification gates stay open (routed-not-absorbed; see §5).
- Collision base = the 21 existing filenames (exact list in §2) + the synthesis
  counterparts (different partition; topic-adjacency verdicts per entry in §3).

## 2. Collision check vs the 21 existing entries

**Filename collisions: none.** No proposed basename below exists in
`corpus/knowledge/linguistics/` (checked against the 21-file listing; also no basename
collides with synthesis counterparts). Sort positions are clean:

| new (proposed) | sorts between |
|---|---|
| `dialect-register-consistency.md` (E2) | `conlang-methodology.md` / `historical-linguistics.md` |
| `sacred-registers-liturgical-language.md` (E4) | `register-strata-attestation.md` / `semantic-fields-lexicon-building.md` |
| `taboo-euphemism-lifecycle-stages.md` (E1) | `syntax-typology.md` / `translation-protocol-fidelity.md` |
| `translation-protocol-fidelity.md` (E3) | `taboo-euphemism-lifecycle-stages.md` / `writing-systems.md` |

Topic-level collision verdicts (nearest neighbors, with measured depth):

- **E1 vs `politeness-taboo-euphemism.md` — HIGH overlap.** The existing entry already
  carries: euphemism cycles + treadmill with lifespan heuristic (:80,:83), dysphemism
  reclamation (:94), minced oaths (:102), the four-strata design rule ending "In-world
  philologists can then date documents by which rung they use" (:106), era-tagged
  ladders (:113), and a worked micro-example doing exactly that dating (:118). Secondary
  inbound coverage: `semantic-fields-lexicon-building.md:78`, `semantics-pragmatics.md:129`.
- **E2 vs `sociolinguistics-registers.md` — MEDIUM overlap.** Koineization is already a
  full paragraph with the four-step sequence (:64; Kerswill & Williams 2000 registered in
  its own sources at :16); anti-language churn and a temple-H worked example appear at
  :126 and :140. "Founder effect" → **0 hits across the 21**; focal/relic-area diagnostics
  appear only inside the :140 worked example.
- **E3 — LOW collision (true absence).** `grep -ric 'thick translation\|translation note'`
  across all 21 → 0 files (command in §Citations). Nearest surfaces are out of scope of
  glossing: `naming-systems.md` §5 endonym/exonym (:80), `semantics-pragmatics.md` §5
  speech acts (:84).
- **E4 — MEDIUM-LOW collision (no dedicated entry).** "liturg-" hits are incidental in 13
  of 21 files (mostly couples lines/examples); the deepest are `historical-linguistics.md`
  "Frozen registers are time capsules" (:237) and its S3 sacred-freeze row (:247), and
  `linguistic-anthropology.md` §5's survey treatment of special languages (:91). By the
  corpus's own survey→dedicated precedent (`kinship-terminology.md:24`: semantic-fields
  "defers to" it as "the full treatment"), a dedicated entry is the same legitimate move.

## 3. The four topics — scoped angle, registered sources, binding boundary

Sources are taken only from already-registered in-corpus source lists (no new
bibliography invented); executors re-check editions/locators at authoring time per
`corpus/QUALITY.md:5-8`.

### E1 (claim-C topic 1) — Taboo–euphemism lifecycle stages — verdict: CONDITIONAL PASS

- **Scope (binding for C01):** the lifecycle as a *staged taxonomy*, not a restatement of
  §4–5 of `politeness-taboo-euphemism.md` — per-stage diagnostics (onset → competing
  euphemisms → minced/fossilized replacement → re-tabooing generation), the
  orthophemism/euphemism/dysphemism triad, the divine-name/naming-practice split (a
  sacred-name avoidance is not an ordinary euphemism), and cross-domain spread order
  (which domains re-lexify first). The dating-instrument angle is **owned by
  `politeness-taboo-euphemism.md:106,118`** — E1 couples to it and must not duplicate the
  four-strata rule or the worked example.
- **Registered sources:** Allan & Burridge (2006) *Forbidden Words*,
  doi:10.1017/CBO9780511617881 (`synthesis/taboo-euphemism-lifecycle.md:5`); Burridge
  (2012) "Euphemism and Language Change: The Sixth and Seventh Ages", doi:10.4000/lexis.355
  (`:6`, the generational-stage frame); the divine-name cluster — Rösel (2007) JTSOT
  31(4), Tov (2012) 3rd ed., Mishnah Yoma 6:2/Danby (`:4-17` block, the sacred-name split
  is exactly their subject).
- **Couples (recommended):** politeness-taboo-euphemism, naming-systems (§4 theonymy :73,
  §6 name taboo :87), sociolinguistics-registers; synthesis counterparts
  taboo-euphemism-lifecycle + deity-name-derivation-pipeline; the r39-unrouted
  verification gate.

### E2 (claim-C topic 2) — Dialect/register consistency — verdict: PASS with scope note

- **Scope (binding for C02):** the *formation and drift mechanics* a built lect map
  depends on as reference knowledge — founder effects and migration trajectories (0-hit
  gap), focal/relic area diagnostics as concepts (not just the :140 worked example),
  anti-language formation mechanics (Halliday's overlexicalization/reflective
  relexicalization), and the koineization sequence as the *process model* (the :64
  paragraph compresses it; E2 expands with the registered corpus behind it). The
  **consistency audit of a built map is NOT this entry** — that is the r39-unrouted
  verification gate; E2 supplies its decision surface.
- **Registered sources:** Chambers & Trudgill (1998) *Dialectology* 2nd ed.,
  doi:10.1017/CBO9780511805103 (`synthesis/dialect-faction-map-workflow.md:4`); Trudgill
  (1986) *Dialects in Contact* (`:5`); Milroy (1987) *Language and Social Networks* (`:6`);
  Kerswill & Williams (2000, LiS 29(1)) (`sociolinguistics-registers.md:16`); Siegel
  (1985) "Koines and koineization" (`synthesis/urban-rural-register-ecology.md:5`);
  Halliday (1976) "Anti-Languages" (`synthesis/dialect-faction-map-workflow.md:9`).
- **Couples:** sociolinguistics-registers, register-strata-attestation,
  register-lexicon-ceilings, language-contact, linguistic-anthropology §5; synthesis
  dialect-faction-map-workflow + urban-rural-register-ecology + migration-founder-effects.

### E3 (claim-C topic 3) — Translation-protocol fidelity — verdict: PASS (strongest)

- **Scope (binding for C03):** the linguistics of glossing and translation commentary as
  cultural practice — the anatomy of a translation note (what a gloss asserts vs what it
  licenses), thick translation as the reference frame, paratext layers (preface/glossary/
  footnote) as carriers of cultural mediation, domestication vs foreignization as a
  design axis, and the interpreter/mediator's register. This is the reference companion
  the r39 verification framing assumed ("two-reader-interop verifies readers *agree*, not
  that notes carry what the protocol requires" — `reports/round-39/scout/
  K01-verification-gaps.md:154-157`).
- **Registered sources:** Appiah (1993) "Thick Translation", *Callaloo* 16(4): 808–819,
  doi:10.2307/2932211 — **page-level verification already recorded in-corpus** (p. 817
  sentence) at `synthesis/cultural-translation-protocol.md:4`; Genette (1997)
  *Paratexts* (`:6` block); Venuti (2018[1995]) *The Translator's Invisibility* (`:7`
  block) — all in the same `- sources:` list at `:3-7` (couples begin `:8`).
- **Couples:** naming-systems, semantics-pragmatics, sociolinguistics-registers,
  writing-systems; synthesis cultural-translation-protocol; verification
  two-reader-interop-agreement.

### E4 (the fourth, named by this seat) — Sacred registers / liturgical language — verdict: PASS

- **Why this one (gap-named by sweeps, not preference):** no dedicated entry exists;
  coverage is incidental in 13 of 21 files (deepest: `historical-linguistics.md:237,247`
  frozen-register paragraphs; `linguistic-anthropology.md:91` survey section;
  `sociolinguistics-registers.md:69` diglossia section whose paradigm H-varieties are
  sacred languages). It is also r39's ranked alternate territory
  (`K01-verification-gaps.md:175-177`), so the fourth stays inside the routed gap set.
  It carries the **richest already-registered source list in the corpus** for any
  unclaimed linguistics topic.
- **Scope (binding for C04):** reference knowledge of the sacred-register system —
  Ferguson's diglossia applied to sacred languages (H reserved to liturgy; domain
  allocation), liturgical fossilization mechanics (why liturgy freezes an older stage —
  complementing, not repeating, `historical-linguistics.md:237`), event-typed prayer
  language rules (recitation/petition/sermon differ), priestly closure devices, chant/
  recitation vs speech, and the register's decay/revival paths (complementing
  `language-shift-obsolescence-revival.md`). Canon and religion content stay out;
  this is a register-systems entry.
- **Registered sources:** Ferguson (1959) "Diglossia"; Haeri (2003) *Sacred Language,
  Ordinary People*; Burt (2003) review; Meyendorff (1991); Jamison & Brereton (2014)
  Rigveda; Larios (2017); UNESCO Vedic-chanting inscription; Vatican II *Sacrosanctum
  Concilium*; GIRM (2002, 3rd typical ed.); Schimmel (1989) *Islamic Names* — all in the
  single registered list at `synthesis/religion-language-co-evolution.md:4`; Ferguson
  (1959) also registered at `synthesis/era-language-staging.md:4`.
- **Couples:** sociolinguistics-registers (§3 diglossia), historical-linguistics
  (frozen stages), orality-formulaic-language, linguistic-anthropology §5,
  register-strata-attestation; synthesis religion-language-co-evolution (the
  workflow/case-study counterpart) + era-language-staging.

## 4. Ranked alternates for E4 (if the integrator or C04 rejects the sacred-register choice)

1. **Era-drift / diachronic register staging** (r39's top alternate, linguistics-framed) —
   but collisions are heavier: `historical-linguistics.md` owns dating stages;
   `sociolinguistics-registers.md:116` §8 already maps register→era. Sources: Campbell
   (2013), Ferguson (1959), Fishman (1967) at `synthesis/era-language-staging.md:4`.
2. **Epistolary registers / the written voice** — "epistol" → 0 hits across the 21 (true
   absence) but the registered source base is thin (Nevalainen & Raumolin-Brunberg 2003,
   registered at `synthesis/urban-rural-register-ecology.md:9` for its
   correspondence evidence); weaker than E4 on the ≥1-resolvable-source spirit.

## 5. Routing notes (for C05 audit + X00 + parent)

- **Non-restatement boundaries in §3 are audit criteria**: C05 should FAIL or mark any
  entry that restates `politeness-taboo-euphemism.md:80-118` (E1), the
  `sociolinguistics-registers.md:64` paragraph verbatim-deep (E2), or
  `historical-linguistics.md:237` (E4) instead of coupling to it.
- **Routed-not-absorbed**: landing E1–E4 as linguistics decision surfaces does NOT
  discharge r39's G2/G3/G4 verification-gate gaps (verified unrouted, §1). Those remain
  open gap-rows for a future round — record in the round record, do not mark resolved.
- **Byte-consistency duty passes to C01–C04**: exact filenames are the executors' choice
  provided the README row and file stay byte-equal for the sweep (r35/36/39 convention,
  `corpus/README.md:17`); the four proposed names in §2 sort cleanly as listed.

## Owed

- none. (All four topics have ≥1 resolvable registered source and no filename collision;
  edition/DOI re-checks at authoring time belong to C01–C04 per QUALITY.md, and the
  Appiah p. 817 check is already recorded in-corpus at
  `synthesis/cultural-translation-protocol.md:4`.)

## Citations

- Counts: `ls corpus/knowledge/linguistics/*.md | wc -l` → 21; `ls
  corpus/knowledge/verification/*.md | wc -l` → 24 (run 2026-10-19, lane root).
- r39 routing: `git log --diff-filter=A --format="%h %ad" --date=short --name-only --
  corpus/knowledge/verification` → `fd55e1f` adds contact-strata-verification-gate +
  3 process entries; grep for `lifecycle-gate|dialect-register|translation-protocol`
  under `corpus/knowledge/verification/` → 0 files.
- G2/G3/G4 definitions and the alternates: `reports/round-39/scout/K01-verification-gaps.md:106,125,148,169-177`.
- Absence sweeps (run 2026-10-19): `grep -ric 'thick translation\|translation note'
  corpus/knowledge/linguistics/*.md` → 0 files; `grep -ric 'founder effect'` → 0 files;
  `grep -nic 'epistol'` → 0 files; "liturg" → incidental hits in 13 of 21 files
  (counts logged in the seat transcript); "koine" → sociolinguistics-registers.md
  5 hits, language-contact.md 1 hit.
- Existing-entry depth: `politeness-taboo-euphemism.md:80,83,94,97,102,106,113,118`;
  `sociolinguistics-registers.md:16,60,64,69,116,126,132,140`;
  `naming-systems.md:73,80,87`; `semantics-pragmatics.md:84,129`;
  `historical-linguistics.md:7,188,237,247`; `linguistic-anthropology.md:55,91`;
  `semantic-fields-lexicon-building.md:78`; `kinship-terminology.md:24,87`;
  `conlang-methodology.md:97`.
- Registered sources: `synthesis/taboo-euphemism-lifecycle.md:4-17` (Allan & Burridge :5,
  Burridge 2012 :6); `synthesis/dialect-faction-map-workflow.md:3-12` (Chambers & Trudgill
  :4, Trudgill :5, Milroy :6, Kerswill & Williams :7, Halliday :9);
  `synthesis/urban-rural-register-ecology.md:4-16` (Siegel :5, Nevalainen &
  Raumolin-Brunberg :9); `synthesis/cultural-translation-protocol.md:3-7` (Appiah :4,
  Genette :6, Venuti :7); `synthesis/religion-language-co-evolution.md:4`;
  `synthesis/era-language-staging.md:4`.
- Index convention: `corpus/README.md:5-13` (rev 2.2, sweep green at 216),
  `corpus/README.md:17` (byte-equal `- topic:` row convention).
- Admission bar: `corpus/QUALITY.md:3-23`.
