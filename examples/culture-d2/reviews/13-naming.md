# Review — component 13-naming (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/13-naming.yml`
- status: **ABSENT — component not delivered**
- canon: not canonized (D2 design drill)

## Evidence

- Look 1 (14:26Z): `examples/` contains only `handoff-packet.sample.md` /
  `.yml`; `examples/culture-d2/` does not exist. Repo-wide
  `find . -iname '*13*naming*'` → nothing.
- Wait-and-retry: 60 s sleep, per assignment protocol → same result
  (14:28Z: `examples/culture-d2/` still absent).
- Look 2 (14:32Z): `examples/culture-d2/` now exists; `components/` holds
  `04-orthography.yml`, `08-symbols.yml`, `12-rank-rules.yml`,
  `15-pragmatics.yml`; `reviews/` holds `01-brief.md` and
  `03-morphosyntax.md` (both written with an ABSENT verdict — this is a
  known wave pattern, not a single lost file). No `13-naming.yml`.
- Extended retries (45 s, 100 s, 150 s, 225 s sleep loops, ~10 min of
  explicit wait beyond protocol): every check → absent. Writers were
  demonstrably active during the window — the component set grew
  04→15 files and `09-eras-calendar.yml` was rewritten at 14:37Z — so the
  absence reads "not yet delivered", not "repo idle".
- Look 3 (final, 14:41:44Z, `date -u`): `components/` holds
  `01-brief`, `02-phonology`, `03-morphosyntax`, `04-orthography`,
  `05-lexicon`, `06-pantheon`, `07-myths-motifs`, `08-symbols`,
  `09-eras-calendar`, `10-materials`, `11-costumes`, `12-rank-rules`,
  `14-kin-address`, `15-pragmatics` — **13-naming is the one missing
  number** (11-costumes landed last, 14:34Z). No file anywhere in the
  repo mentions a `13-naming` target; no sibling component quotes a
  naming record id. (Only lead: `06-pantheon.yml` defers "final theonym
  spellings, NM- records, and the name-taboo layer" to a names-owned
  component under the older number `08-names` — numbering drift worth
  checking at re-dispatch.)
- No LOG.md entry was written by this worker: the review-assignment
  write scope is this named file only (same practice as the two sibling
  reviews in this directory).

## What I checked instead (corpus side complete)

Chunk-read in <=80-line windows, so the checklist below can execute the
moment the component lands:

- `corpus/knowledge/linguistics/naming-systems.md` (134 lines, full) —
  §1 four systems + the name-magic force; §2 slot table (segmentary
  lineages run patronymic chains; formation rules), §3 toponymy strata +
  folk etymology + critical toponymy, §4 theonymy transparent/opaque +
  cult epithets, §5 endonym/exonym, §6 the name-taboo table (bìhuì,
  imina, damnatio, Inuit name inheritance, Jalnguy) + kotodama attesta-
  tions, §7 the 10-step derivation pipeline, §8 calibration (acronym
  etymologies false; Torpenhow phantom; tartan forgery), §9 canon
  boundary.
- `corpus/knowledge/linguistics/semantics-pragmatics.md` (135 lines,
  full) — §4 evidentiality/mirativity, §5 implicature + politeness
  mechanics table, §6 deixis + the four-part deixis spec (name-avoidance
  is indexed here), §7 method incl. taboo chains, calibration.
- `corpus/knowledge/linguistics/politeness-taboo-euphemism.md` (132
  lines, full) — §1 politeness logics, §2 honorific stack + Comrie axes,
  §3 taboo domains + sanction gradient + "replaced and preserved as a
  citation form", §4 euphemism treadmill, §5 the four fossil strata +
  the closing design rule, §6 construction procedure, §7 calibration,
  §8 canon boundary.
- `corpus/knowledge/verification/naming-collision-gate.md` §1–§8 —
  required input records (§2), Gate A uniqueness (§4), similarity
  triage (§5), **Gate B pronounceability** (§6), **Gate C derivational
  validity** (§7), era staging (§8).
- `corpus/knowledge/verification/phonology-sanity-gate.md` §1–§5 —
  verdict vocabulary, finite-segment input contract, inventory bands,
  markedness priors, legality/allophony audit rows.
- `corpus/knowledge/linguistics/historical-linguistics.md` §1–§9
  section map (name strata, sound change in transmitted names, stage
  dating — for the fossil/loan etymology checks).
- `corpus/QUALITY.md` — the five admission items (provenance,
  calibration, coupling, usability, canon hygiene).

## Cross-component contracts snapshot at review time (pointers only)

Not substitutes for corpus checks, but the naming component was expected
to bind these fields; the re-run should read them fresh:

- `02-phonology.yml` §phonology: consonants
  `[p, t, k, b, d, g, m, n, s, ʃ, r, l, j, w, h]`, vowels
  `[a, e, i, o, u]`, phonotactics `(C)V(C)`, `tones: 0`, accent =
  culminative pitch accent, two levels H/L, **one H per prosodic word**;
  notable rules include nasal place assimilation, `s → h / _ #`,
  `t → t͡s / _ i`, `k → c / _ i`, `h → ɸ / _ u`, `h → ç / _ i`.
- `04-orthography.yml` §phonology_interface (assumed, reconcile at
  handoff): codas limited to `/n l r s/`; no onset clusters; no
  geminates; a minority non-initial-H class marked in script.
- `03-morphosyntax.yml`: suffixing agglutination; M4 compounding
  modifier+head; N2 Class A plural `-ra`; N3 Class B accent-shift
  plural; N5 genitive `-ni`; N6/N7/N8 lative `-ku`/`-mu` and locative
  `-an`/`-ir` and traverse `-wa`; N9 possessive `-na`/`-ha`; all forms
  provisional pending the phonology handoff.
- `14-kin-address.yml` A01–A09 (its own dispatch note says these
  "constrain the naming component's address slots"): A02 wind-name
  licence (name spoken only at the same fire in the same winter shelter;
  across distance, kin terms), A03 storm law (no wind-names while the
  storm runs), A04 name closing at death (name left in the tally knot;
  still-breath year), A06 teknonymy `-ánpa`.
- `15-pragmatics.yml` (the pragmatics brief): TB-1 storm true name
  spoken only by the storm-speaker at the mid-winter recitation, no
  second context; TB-3 rungs; TB-5 closed-mark legal fossil; TD-1–TD-6
  taboo domains incl. TD-2 herd-loss-winter dead and TD-4 in-marrying
  spouses' home camps; B-marking rule (in-world belief, not narrator
  metaphysics).
- `12-rank-rules.yml` speech rules: storm-name statute (above the
  snow-line only a wind-speaker may name it; below, only the grandfather-
  name) and the dead-roll rule (a lineage's dead named only by that
  lineage).
- `06-pantheon.yml` explicitly hands theonym spellings and the
  name-taboo layer to the names component.

## Pre-registered checklist for the re-run

Violations will be written
`13-naming | <violation> | <corpus path:section that forbids it>`;
if nothing fails, the verdict is CLEAN with the checks listed as run.
Planned tests, in order:

1. **Header/format/canon.** File starts `component: 13-naming` +
   `culture: D2`; carries `canon: not canonized (D2 design drill)`;
   every record carries a short id; every design choice carries a
   `follows:` list citing corpus decision tables (path + section) —
   dispatch rules; QUALITY.md items 1/4/5 (provenance, usability, canon
   hygiene).
2. **Phonotactics (the assigned axis 1).** Every personal, lineage,
   clan, place, and divine form is a legal string under the declared
   D2 phonology — not under English reading habits. Syllabify sound
   tokens, not spelling; test the inflected/address forms too (possessive
   `-na`/`-ha`, plural `-ra` / accent-shift, genitive `-ni`, the A01
   pitch-compass forms). Failure signatures per
   `naming-collision-gate.md §6` (segment inventory / syllable structure
   / distribution / prosody / connected use) and
   `phonology-sanity-gate.md §5` (inventory membership, syllable roles).
   A name stratum with archaic phonemes is allowed **only if declared
   as its own stratum with its own rules** — `naming-systems.md §7`
   step 1; silent exotic letters are a FAIL.
3. **Etymologies (assigned axis 2).** Replay each derivation
   independently: licensed construction (compounds modifier+head,
   suffix set per the morphology contract) → morphophonology → dated
   transmission → surface form → script; keep historical derivation,
   current-speaker analysis, and folk etymology in **separate fields**
   — `naming-collision-gate.md §7` (Gate C); `naming-systems.md §2`
   (dithematic vs monothematic choice), §3 (toponym strata; plant one
   tautology and one folk etymology deliberately), §4 (old gods opaque /
   young gods transparent — opacity recorded, not dated), §8 (no
   acronym etymologies; single-gloss folk etymologies are suspect).
   Unverifiable items marked `(to-verify)` — QUALITY.md item 1.
4. **Taboo logic vs the pragmatics brief (assigned axis 3).** The
   component's avoidance rules must not contradict `15-pragmatics.yml`
   TB-1/TB-3/TD-2/TD-4 and `14-kin-address.yml` A02–A04. Corpus that
   forbids contradictions and shapes the required machinery:
   `politeness-taboo-euphemism.md §3` (the dangerous word is replaced
   and preserved as a citation form; names of the dead and ruler-name
   avoidance as standard domains), §4–§5 (each deep taboo deposits four
   strata: one fossilized euphemism nobody analyzes, one live ladder,
   one minced oath, one legal/liturgical fossil), §6 step 3 (5–8 domains,
   each with owner + sanction), §7 (Frazer as folk-model only; do not
   build "real" magic on it without flagging); `naming-systems.md §6`
   (taboo mechanisms table) and §7 step 5 (taboo layer generates
   substitution mechanism + stratum); `semantics-pragmatics.md §6`
   (name-avoidance as social deixis) and its calibration (beliefs marked
   as in-world ideology, never narrator-endorsed). A taboo that produces
   no substitution mechanism, no citation-form survival, and no stratum
   is incomplete, not minimal.
5. **Pipeline completeness** — `naming-systems.md §7` steps 1–10:
   slot inventory + order (segmentary lineage → decide patronymic vs
   free chain), formation rules, curated name lexicon as a separate
   semantic field, life-stage schedule (who may say which name, when),
   exonym layer for the lowland trade partner (≥1 pejorative root and
   one double-arrival), toponym strata, theonym layer + cult epithets
   derived from toponyms, ledger, and the four stress tests (coronation /
   funeral / market between exonym-users / clerk dating a document by
   its missing or closed characters). Tally-knot-era name records and
   the script-era closed mark (TB-5) should be dated, not modernized.
6. **Spine and contrast guard.** Every naming rule couples to
   verticality (high/low, ascent/descent, seasonal poles) and wind
   (breath, soul-carrier, storm law) — dispatch seed; no D1 river /
   water / tying / binding / knot-as-binding imagery is imported
   (knots may appear only as the tally-counting technology the seed
   assigns); sibling references only by CONTRACT field names, never by
   importing another component's contents — dispatch rules for write
   assignments (the same `d1_guard` the wave's other components carry).
7. **Calibration and canon hygiene.** In-world beliefs marked as
   beliefs; no fabricated real-world citation (use `(to-verify)`);
   file ends at the handoff, deciding no world truth — QUALITY.md items
   2/5; `naming-systems.md §9` canon boundary.

## Re-run note

This review is written to be superseded: when `13-naming.yml` is
delivered, re-dispatch this review and the checklist above executes
without new preparation. The component file was not created, read, or
modified by this worker; nothing else in the repo was touched.