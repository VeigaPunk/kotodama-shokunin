- Seat: K01 | scout | C | date 2026-10-19 | baseline dfb0719

# Verification-partition gap scout — 20 entries inventoried, 4 gap-named topic recommendations

## 1. Baseline state (measured, not asserted)

- Verification partition = 20 files: `ls corpus/knowledge/verification/*.md | wc -l` → 20
  (2026-10-19, lane root). Corpus totals 212 = civilizations 94 + culture-material 25 +
  linguistics 21 + myth-symbol 23 + synthesis 29 + verification 20 (per-directory `wc -l`
  sweep; matches `corpus/README.md:4-9` revision 2.1 footer vector 21/23/25/29/20/94).
- The partition has been **closed to additions since round 19**: git add-history for
  `corpus/knowledge/verification` shows the newest five entries
  (`gate-battery-surface-verification.md`, `generated-artifact-roundtrip-verification.md`,
  `label-channel-routing-verification.md`, `pre-declared-hold-set-reconciliation.md`,
  `two-reader-interop-agreement.md`) landed in commit `caf1bea` 2026-10-18 (round 19);
  the next-oldest two in `94ca098` (round 10); nine in `49ac1a5` (mint wave); one in
  `c610e0a` (round 3). Rounds 20–38 added nothing here while other partitions grew —
  the "thinnest partition" premise of claim C is confirmed by git, not by count alone.

## 2. The 20 existing entries' topics

| # | entry (topic one-line) |
|---|---|
| 1 | `calibration-registry.md` — contested claims, discredited inferences, replacement practice |
| 2 | `citation-format-and-source-registry.md` — citation formats, source registry, provenance ledger |
| 3 | `costume-era-consistency-gate.md` — costume/era gate: materials, rank rules, textile-tech bounds |
| 4 | `gate-battery-surface-verification.md` — what the isolated gate battery measures / does not |
| 5 | `gate-frozen-run-standard.md` — the two-evidences clause and frozen-run layout |
| 6 | `generated-artifact-roundtrip-verification.md` — byte-identity, `--check`, corruption class |
| 7 | `header-conformance-readings.md` — measuring source/verified-at/recheck without laundering |
| 8 | `internal-consistency-audit.md` — coupling graphs, terminology sweeps, contradiction triage |
| 9 | `label-channel-routing-verification.md` — which channel a form-bearing record is graded on |
| 10 | `lexicon-coverage-audit.md` — seven-field release gate |
| 11 | `myth-consistency-gate.md` — myth roles, motifs, eras, symbol domains |
| 12 | `naming-collision-gate.md` — name identity, pronunciation, derivation, cultural overlap |
| 13 | `phonology-sanity-gate.md` — inventory, phonotactics, markedness, allophony |
| 14 | `pre-declared-hold-set-reconciliation.md` — naming expected findings before the artifact |
| 15 | `provenance-audit-ledger-format.md` — per-round evidence, append-only corrections |
| 16 | `real-world-inspiration-boundaries.md` — borrowing, transformation, living-culture authority |
| 17 | `to-verify-triage-protocol.md` — confirm / downgrade / excise coupled claims |
| 18 | `two-reader-interop-agreement.md` — independent readers of one artifact agree |
| 19 | `verification-independence-anti-circularity.md` — earned greens, control sensitivity, re-pins |
| 20 | `verification-method-overview.md` — testable coupling, separated evidence, fail-closed handoffs |

Shape of the coverage: the partition is dense on **process** (ledgers, gates about gates,
triage, interop) and on **three system gates** (myth, naming, phonology) + **one era gate**
(costume-era). It is thin on verification surfaces for the **contact/sociolinguistic half of
the synthesis partition**: of 29 synthesis method entries, the ones that build
contact, taboo, dialect/register, and translation artifacts have no verification
counterpart — an executor following `verification-method-overview.md` §5's routing table
finds no corpus surface for those claim families (the overview itself flags this
failure mode at `verification-method-overview.md:88`: "If no applicable rule exists,
record a coverage gap and a candidate test").

## 3. Unnamed gaps — absence sweeps (commands run 2026-10-19, lane root)

Scoped `grep -lic <term> corpus/knowledge/verification/*.md` (case-insensitive, file
counts; all hits inspected — every one is an incidental mention inside another gate's
body, none is a dedicated entry):

| sweep | hits | dedicated entry? |
|---|---|---|
| `loanword` | 4 (label-channel-routing, lexicon-coverage-audit, myth gate, overview) | **no** |
| `taboo` | 9 (all incidental: gates mention taboo context; no taboo lifecycle gate) | **no** |
| `euphemism` | 4 (incidental) | **no** |
| `dialect` | 6 (incidental) | **no** |
| `sacred register / ritual language / liturgical` | 6 (incidental) | **no** |
| `translation note` | **0 files** | **no** — strongest absence |
| `era-language staging / law ordering` | 10 (incidental; era↔language edge appears only as a row in overview §7) | **no** |

Synthesis counterparts confirmed to be **method-only** entries: each carries a
verification-scope disclaimer, not a verification procedure —
`synthesis/contact-scenario-builder.md:198`, `synthesis/loanword-material-dating.md:6`,
`synthesis/taboo-euphemism-lifecycle.md:20`, `synthesis/dialect-faction-map-workflow.md:15-16`,
`synthesis/urban-rural-register-ecology.md:19`, `synthesis/cultural-translation-protocol.md:10`.

## 4. Four topic recommendations (gap-named, sourced)

Each recommendation: the gap, the internal decision surfaces, and source candidates —
external sources are taken **only from already-registered, in-corpus verified source
lists** (no new bibliography invented; executors still re-check editions at authoring
time per `corpus/QUALITY.md:5-8`).

### G1 — Contact-strata verification gate (loanword / borrowed-thing chronology)

- **Gap:** no entry defines how to *audit a built culture's* loan strata — a term dated
  before its contact channel, strata ordering contradicting the declared contact history,
  a loan-thing without an object chain. `verification-method-overview.md:114` states the
  question ("do borrowing, sound change, spelling, and name strata have compatible
  relative order?") and `:118` notes propagation ("a failed dye-import date reopens …
  loanword dating"), but no gate operationalizes either.
- **Internal decision surfaces:** `linguistics/language-contact.md`;
  `linguistics/historical-linguistics.md` (§2 correspondence table, §6 dating — as routed
  at `verification-method-overview.md:73`);
  `synthesis/loanword-material-dating.md` (status vocabulary at :23);
  `synthesis/contact-scenario-builder.md`; `synthesis/multi-culture-creole-workshop.md`.
- **Sources:** Thomason & Kaufman (1988) *Language Contact, Creolization, and Genetic
  Linguistics*, UC Press, chs. 3–5 (registered + publisher-contents-checked at
  `synthesis/contact-scenario-builder.md` `- sources:`); Haspelmath & Tadmor (2009) and
  Durkin (2014) (registered at `synthesis/loanword-material-dating.md:3`).
- **Couples:** synthesis — loanword-material-dating, contact-scenario-builder,
  multi-culture-creole-workshop; linguistics — language-contact,
  historical-linguistics; verification — internal-consistency-audit,
  verification-method-overview.

### G2 — Taboo–euphemism lifecycle consistency gate

- **Gap:** `synthesis/taboo-euphemism-lifecycle.md` dates worlds by forbidden-word
  strata, but no verification entry audits a built artifact against lifecycle stages —
  a euphemism in use before its taboo onset, a divine-name avoidance substitute
  confused with an ordinary euphemism, a fossilized taboo read as live. The naming
  gate touches taboo only as a name-slot context (`naming-collision-gate.md`, taboo
  sweep incidental).
- **Internal decision surfaces:** `linguistics/politeness-taboo-euphemism.md`;
  `synthesis/taboo-euphemism-lifecycle.md` (naming-practice split at :119; provenance
  cautions at :108); `synthesis/deity-name-derivation-pipeline.md`; myth gate's
  taboo-of-narrative checks (`myth-consistency-gate.md:75-76`).
- **Sources:** Allan & Burridge (2006) *Forbidden Words: Taboo and the Censoring of
  Language*, CUP, doi:10.1017/CBO9780511617881 (registered at
  `synthesis/taboo-euphemism-lifecycle.md` `- sources:`).
- **Couples:** synthesis — taboo-euphemism-lifecycle, deity-name-derivation-pipeline;
  linguistics — politeness-taboo-euphemism; verification — naming-collision-gate,
  myth-consistency-gate.

### G3 — Dialect–faction / register-ecology consistency gate

- **Gap:** `synthesis/dialect-faction-map-workflow.md` and
  `synthesis/urban-rural-register-ecology.md` build lect maps and register ecologies;
  no verification gate audits the built map — a faction lect feature outside its
  declared geography, a register used in the wrong social context, migrant founder
  effects applied without the migration premise, an avoidance register treated as a
  caste lect. `dialect-faction-map-workflow.md:16` explicitly defers these to "local
  descriptive scholarship" — a built artifact still needs its own consistency check.
- **Internal decision surfaces:** `linguistics/sociolinguistics-registers.md`;
  `linguistics/register-strata-attestation.md`;
  `linguistics/register-lexicon-ceilings.md`;
  `synthesis/migration-founder-effects.md`; `synthesis/dialect-faction-map-workflow.md`
  (evidence labels at :42); `synthesis/urban-rural-register-ecology.md`.
- **Sources:** Chambers & Trudgill (1998) *Dialectology*, 2nd ed., CUP,
  doi:10.1017/CBO9780511805103 (registered at `synthesis/dialect-faction-map-workflow.md`
  `- sources:`); Siegel (1985) "Koines and koineization," *Language in Society* 14(3)
  (registered at `synthesis/urban-rural-register-ecology.md` `- sources:`).
- **Couples:** synthesis — dialect-faction-map-workflow, urban-rural-register-ecology,
  migration-founder-effects; linguistics — sociolinguistics-registers,
  register-strata-attestation, register-lexicon-ceilings; verification —
  internal-consistency-audit.

### G4 — Cultural-translation protocol fidelity verification

- **Gap (strongest absence — sweep returned 0 files):**
  `synthesis/cultural-translation-protocol.md` defines name-first reading and
  translation notes, and no verification entry tests a built artifact's translation
  notes for protocol fidelity (note present but missing the declared context fields; a
  gloss asserting meaning the protocol does not license; translation mistaken for
  original wording — the laundering class at `verification-method-overview.md:150`).
  The existing `two-reader-interop-agreement.md` verifies that readers *agree*, not
  that the notes carry what the protocol requires — distinct failure sources.
- **Internal decision surfaces:** `synthesis/cultural-translation-protocol.md` (couples
  at :8); `linguistics/naming-systems.md`, `linguistics/semantics-pragmatics.md` (both
  already coupled by the protocol entry); `verification/two-reader-interop-agreement.md`
  as the neighboring instrument.
- **Sources:** Appiah (1993) "Thick Translation," *Callaloo* 16(4): 808–819,
  doi:10.2307/2932211 — registered **with page-level verification already recorded in
  the corpus** at `synthesis/cultural-translation-protocol.md:4`.
- **Couples:** synthesis — cultural-translation-protocol; linguistics — naming-systems,
  semantics-pragmatics, sociolinguistics-registers; verification —
  two-reader-interop-agreement, verification-method-overview.

### Alternates (ranked behind the four, one line each)

- **Era-staging language-drift verification:** operationalize the overview §7 era↔language
  edge (`verification-method-overview.md:114`) against `synthesis/era-language-staging.md`;
  sources registered there (Campbell 2013; Ferguson 1959; Fishman 1967 at
  `synthesis/era-language-staging.md:4`).
- **Sacred-register verification:** audit prayer/liturgical register separation against
  `synthesis/religion-language-co-evolution.md` (verification scope at :7; research gap
  at :90).

## 5. Entry-contract inputs for the executors (C01–C04)

- The round-35/36 head-block contract, as exemplified by the newest verification entry:
  H1 + `- topic:` / `- gap filled:` / `- sources:` (numbered, locators) / `- calibration:` /
  `- couples:` / `- source:` / `- verified-at:` / `- recheck:`
  (`corpus/knowledge/verification/gate-battery-surface-verification.md:1-18`), plus a
  numbered decision-record section (`:75-82`).
- Admission bar: `corpus/QUALITY.md:3-23` — provenance (to-verify inline, never
  laundered), calibration status, couples, usability, canon hygiene.
- Index implications for C06: verification 20 → 24; totals 212 → 216; footer vector
  21/23/25/29/20/94 → 21/23/25/29/**24**/94; rows in filename order with byte-equal
  `- topic:` text (the rev-2.1 convention, `corpus/README.md:4-9`); sweep green via
  `python3 reports/round-28/readme/sweep.py`.
- Filename recommendations (kebab-case, sorted between existing neighbors):
  `contact-strata-verification-gate.md`, `taboo-euphemism-lifecycle-gate.md`,
  `dialect-register-consistency-gate.md`, `translation-protocol-fidelity-verification.md`
  — all four sort cleanly into the current filename set; exact names are the
  executors' choice provided the row/file stay byte-consistent for the sweep.

## Owed

- none. (External sources recommended above are all already registered in the corpus;
  executors must still re-verify editions/DOIs at authoring time per QUALITY.md — that
  re-check belongs to C01–C04, not to this scout.)

## Citations

- Partition counts: `ls corpus/knowledge/verification/*.md | wc -l` → 20; per-directory
  sweep → 94/25/21/23/29/20 (run 2026-10-19); cross-checked against
  `corpus/README.md:4-9` (rev 2.1, vector 21/23/25/29/20/94, total 212).
- Partition add-history: `git log --diff-filter=A --format="%h %ad %s" --date=short
  --name-only -- corpus/knowledge/verification` → newest `caf1bea` 2026-10-18 (round 19,
  5 entries), then `94ca098` (round 10, 2), `c610e0a` (round 3, 1), `49ac1a5` (mint, 12).
- Entry-contract exemplar: `corpus/knowledge/verification/gate-battery-surface-verification.md:1-18,75-82`.
- Admission bar: `corpus/QUALITY.md:3-23`.
- Coverage-gap duty: `corpus/knowledge/verification/verification-method-overview.md:88`;
  era↔language edge `:114`; propagation `:118`; translation-laundering caution `:150`;
  routing table `:73`.
- Absence sweeps: `grep -lic` counts in §3 (commands shown, run 2026-10-19, lane root);
  `translation note` → 0 files.
- Synthesis verification-scope disclaimers: `contact-scenario-builder.md:198`,
  `loanword-material-dating.md:6`, `taboo-euphemism-lifecycle.md:20`,
  `dialect-faction-map-workflow.md:15-16`, `urban-rural-register-ecology.md:19`,
  `cultural-translation-protocol.md:10`.
- Registered external sources (in-corpus): Thomason & Kaufman 1988 and
  `synthesis/contact-scenario-builder.md` `- sources:`; Haspelmath & Tadmor 2009 +
  Durkin 2014 at `synthesis/loanword-material-dating.md:3`; Allan & Burridge 2006 at
  `synthesis/taboo-euphemism-lifecycle.md` `- sources:`; Chambers & Trudgill 1998 at
  `synthesis/dialect-faction-map-workflow.md` `- sources:`; Siegel 1985 at
  `synthesis/urban-rural-register-ecology.md` `- sources:`; Appiah 1993 at
  `synthesis/cultural-translation-protocol.md:4`; Campbell 2013 / Ferguson 1959 /
  Fishman 1967 at `synthesis/era-language-staging.md:4`.
- Linguistics decision surfaces (titles verified):
  `linguistics/language-contact.md`, `linguistics/politeness-taboo-euphemism.md`,
  `linguistics/sociolinguistics-registers.md`, `linguistics/register-strata-attestation.md`,
  `linguistics/register-lexicon-ceilings.md`, `linguistics/historical-linguistics.md`.
