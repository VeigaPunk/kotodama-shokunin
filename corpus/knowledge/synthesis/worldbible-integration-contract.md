# World-Bible Integration Contract — Kotodama Systems, Lore Canon
- topic: The shared adjacency interface by which kotodama-shokunin hands linguistic-cultural systems to lore-shokunin without claiming, recording, or silently changing canon.
- sources: Star & Griesemer (1989), “Institutional Ecology, ‘Translations’ and Boundary Objects”; Moreau & Missier (eds., 2013), PROV-DM, W3C Recommendation; Miles & Bechhofer (eds., 2009), SKOS Reference, W3C Recommendation; Preston-Werner (2013), Semantic Versioning 2.0.0; editions, links, and verification limits below.
- couples: language — ../linguistics/{naming-systems,historical-linguistics,writing-systems,semantic-fields-lexicon-building}.md; myth/symbol — ../myth-symbol/{comparative-frameworks,symbolism-synthesis-method}.md; era/costume — ../culture-material/{era-periodization-models,costume-semiotics,material-culture-inference-method,textile-technology}.md; siblings — lore-shokunin owns canon, chousa owns general research method, integrator arbitrates contested scope.

## 1. Both-lane read: authority and activation

- Contract ID: `kotodama-lore-adjacency`; initial interface revision: `1.0.0`; verification date: 2026-10-17.
- This is a method/reference contract, not a world-bible entry, canon ruling, or assertion that either lane has already accepted a packet.
- Canonical contract copy: this file in kotodama-shokunin; lore reads it read-only. Do not maintain an independently edited mirror.
- Before the first transfer, both lanes read the whole file and record `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer` in their own permitted records.
- Initial bilateral acknowledgement is **pending** until those records exist; writing this file is not a substitute for lore's read.
- Before later transfers, compare the pinned contract digest; a changed revision/digest requires both lanes to re-read and acknowledge before importing under it.
- Kotodama owns generative craft and its reproducible design records; lore owns world-bible entities, relations, chronology, canon decisions, and bible-wide consistency verification (`PROVINCE.md` §§Owns/Adjacent contract).
- Each lane writes only its own authorized surfaces. A request from lore does not grant kotodama world-bible write access; a receipt does not delegate canon authority.
- Existing lore/operator approval policies remain authoritative. This contract defines a handoff, not permission to bypass an operator gate.

## 2. Provenance and named frameworks

| Framework | Contract use | Calibration / limit |
|---|---|---|
| Boundary object, Star & Griesemer (1989) | One identifiable packet supports a generative reading and an archival reading without merging lane ownership | Heuristic adaptation from science studies; definition at p. 393 corroborated by verbatim quotations in independent scholarly sources; publisher full text paywalled in this pass |
| PROV-DM, Moreau & Missier (2013), §§2.1–2.2 | Distinguish source/artifact entities, generation/review activities, responsible agents, derivation, and revision | Provenance permits assessment; it does not establish truth, cultural permission, or canon |
| SKOS, Miles & Bechhofer (2009), §§5, 7, 10 | Separate concept identity from labels, record scope notes, distinguish mappings from identity | Borrowed vocabulary discipline, not a requirement to deploy RDF or claim SKOS conformance |
| Semantic Versioning, Preston-Werner (2013), rules 1–8 | Declare the public interface, preserve released bytes, distinguish compatible additions from breaks | Software convention adapted here; a version number never grants canon status |

- Susan Leigh Star & James R. Griesemer (1989), “Institutional Ecology, ‘Translations’ and Boundary Objects: Amateurs and Professionals in Berkeley's Museum of Vertebrate Zoology, 1907–39,” *Social Studies of Science* 19(3):387–420. [DOI](https://doi.org/10.1177/030631289019003001). Bibliographic details corroborated; the p. 393 definition is quoted verbatim in independent scholarly sources, but the publisher full text was paywalled in this pass.
- Luc Moreau & Paolo Missier (eds., 2013), *PROV-DM: The PROV Data Model*, W3C Recommendation, 30 April 2013. [Official text](https://www.w3.org/TR/prov-dm/), dated edition `REC-prov-dm-20130430`; core structures and revision model inspected.
- Alistair Miles & Sean Bechhofer (eds., 2009), *SKOS Simple Knowledge Organization System Reference*, W3C Recommendation, 18 August 2009. [Official text](https://www.w3.org/TR/skos-reference/), dated edition `REC-skos-reference-20090818`; label and mapping distinctions checked.
- Tom Preston-Werner (2013), *Semantic Versioning 2.0.0*. [Versioned specification](https://semver.org/spec/v2.0.0.html); immutable releases and change categories checked. Contract rules below are local policy, not quotations from these works.
- Recheck sources when an edition changes, a locator fails, or a claim is challenged; record the accessed edition and exact section rather than silently substituting a newer text.

## 3. Ownership decision table

| Work item | Kotodama supplies | Lore records / decides | Stop condition |
|---|---|---|---|
| Language | Phonology, morphosyntax, registers, script conventions, change rules, tests | Which groups use which system, where and when | A generator cannot assign a canon population |
| Lexicon | Sense-separated entries, morphology, material terms, usage restrictions | Approved senses/forms and their world associations | A gloss cannot establish an entity's existence |
| Naming ledger | Slot grammar, derivations, aliases, exonyms, taboo rules, candidate labels | Entity identity, approved names, official/contested status | Matching strings do not prove matching entities |
| Myth / pantheon | Variant relations, ritual consequences, candidate epithets, attribution rules | Who holds a belief; whether any supernatural claim is true | Sacred doctrine is not automatically world-fact |
| Symbol / costume | Contextual sign rules, garment construction constraints, lexicon and wearer permissions | Actual institutions, permitted wearers, objects, enforcement | Prescriptive dress rules do not prove actual practice |
| Era | Candidate change sequence, relative stages, calendars and conversion assumptions | Event dates, period boundaries, temporal consistency | A stylistic stage cannot date a canon event by itself |
| Contradiction | Finding, reproducer, impacted candidate records, repair alternatives | Bible-wide verification and canon resolution | Kotodama never silently repairs a canon conflict |
| Scope / rights | Evidence and an explicitly bounded question | Integrator rules scope; operator handles rights/permission decisions | Neither lane invents legal clearance or absorbs a sibling province |

## 4. Handoff envelope: required fields

Use UTF-8 Markdown with explicit tables unless both lanes agree another serialization; these are data requirements, not claims that an importer already exists.

| Field | Required content / interpretation |
|---|---|
| `packet_id`, `packet_version` | Stable packet identifier and immutable release version; revised bytes require a new version |
| `contract_ref` | Contract ID, revision, and digest acknowledged by both lanes |
| `producer`, `recipient`, `request_ref` | Kotodama author, lore recipient, and scoped brief or request pointer |
| `baseline_bible_ref` | Lore-supplied world-bible revision/digest and the constraints read from it; `none` only for a deliberately unbound research packet |
| `artifact_manifest` | Artifact IDs, record IDs, paths/sections, versions, file digests, and record counts; identify the exact delivered bytes |
| `subject_refs` | Lore entity IDs when supplied; otherwise namespaced candidate IDs, explicitly unresolved, never guessed canon IDs |
| `scope` | Culture/group, region, language variety, script, social/register context, and era applicability for each record |
| `dependency_manifest` | Exact system/rule/lexicon versions, candidate prerequisites, and lore dependencies; no floating `latest` |
| `claim_ledger` | Statement, claim kind, source/invention provenance, evidence status, uncertainty, and relation to other records |
| `coupling_edges` | Typed source→target relations with applicability and justification; distinguish dependency, analogy, and attributed association |
| `requested_decisions` | Per-record accept/defer/reject questions, mutually exclusive alternatives, blockers, and allowed partial-acceptance boundaries |
| `validation`, `open_questions` | Checks actually run with inputs/results; unresolved issues with responsible lane and blocking/nonblocking status |

- Artifact paths live in the delivering lane's permitted handoff surface; lore supplies its own bible/receipt locations. Do not invent a sibling path or tool and call it established.
- An unbound research packet may be retained as reference but cannot be imported as canon without a lore baseline and a new reviewed handoff.
- Freeze the manifest before review; changing a referenced file invalidates that delivery's digest even if its filename stays unchanged.

## 5. Artifact payloads: systems, lexica, naming ledgers

| Artifact | Minimum record content | Reproduction / coupling check |
|---|---|---|
| System specification | System ID, inputs/assumptions, rule IDs, outputs, exceptions, applicable varieties/eras | Show valid and invalid derivations; state whether rules are deterministic or curated |
| Diachronic specification | Parent/daughter stage IDs, ordered change rules, contact assumptions, retained archaisms | Re-derive a named fixture set; do not force names or liturgy to change with ordinary speech |
| Lexicon | Entry and sense IDs, form, pronunciation, script/transliteration, morphemes, part of speech, gloss, usage, stage | Trace a garment/ritual term to both the linguistic rules and its material/ritual referent |
| Naming ledger | Name-record ID, target candidate/lore ID, slot order, derivation, name type, address/reference use, validity, taboo | Trace endonym/exonym and life-stage changes without merging identities or losing old forms |
| Myth-symbol register | Variant ID, attributed tellers, proposition, ritual setting, signs, interpretations, counter-readings | Trace an epithet or emblem to a named variant; do not infer divine identity from shared attributes |
| Era-costume matrix | Era key, region/wearer, material/fiber/dye, technique/cut, term, sign value, rule versus observed use | Check terminology against available processes, trade assumptions, borrowing, repair, and heirloom reuse |
| Coupling register | Edge ID, source and target record IDs/versions, relation, mechanism, scope, exceptions, evidence/design status | A changed source yields an explicit impact list, not automatic downstream rewriting |

- Keep `form_id`, `sense_id`, `concept_id`, and `entity_ref` distinct: homographs may be unrelated; several names may denote one entity; a borrowed term may change meaning.
- Preserve original spelling, normalized search form, script, transliteration scheme, pronunciation, and variety separately; lossy ASCII/search normalization is not the authoritative name.
- Use local language/variety IDs for invented languages; do not fabricate ISO codes or imply a real language family is a fictional culture's ancestry.
- A lexical gloss is an aid, not a one-to-one conceptual equivalence. Record near-equivalence, broader/narrower scope, and gaps rather than forcing an English-sized sense inventory (SKOS-inspired, not an identity proof).
- Name collisions produce review findings; shared theonyms produce a proposed relation. Neither licenses an entity merge or a syncretism ruling.
- Generator inputs include rule versions, seed if randomized, selection procedure, and human-curated exceptions. If nondeterministic, preserve the selected output fixture rather than promise exact regeneration.
- Suggested fixture situations: naming/address at accession, an interregional market, a funeral, an inherited garment, and an archaizing inscription. These are tests of design rules, not fictional events established here.

## 6. Keep claim kind, evidence, and canon status separate

| Dimension | Values / required distinctions | Who may change it |
|---|---|---|
| Claim kind | Real-world reference; generative rule; candidate world-fact; attributed in-world belief; designer interpretation | Kotodama identifies what it supplied; lore preserves the distinction on import |
| Evidence status | Attested; inferred with stated bridge; contested with alternatives; invented; `(to-verify)` | Evidence reviewer supplies reasons and locators; no automatic promotion |
| Scholarly calibration | Established within stated scope; debated; rejected/discredited claim; heuristic only | Cite the particular claim/reception, not a blanket verdict on a tradition |
| Workflow state | Draft → submitted → returned/deferred/rejected or accepted-by-lore; later superseded/withdrawn | Kotodama submits; lore issues disposition; each records its own actions |
| Canon standing | Lore's own policy and approved world-bible record/revision; otherwise `not canonized` | Lore only, subject to its operator approval gates |

- A statement can be **invented and accepted as fiction**, or **well-attested in a real source and not canonized**. Evidence strength and fictional truth are orthogonal.
- “The temple teaches P” and “P is true” are separate candidate propositions. Accepting the former does not entail the latter; cite the attributed speaker, group, place, and period.
- Legacy corpus labels such as `HARD`, `SOFT`, `DOCTRINE`, `DESIGN`, or myth/legend/folktale tiers are advisory source labels, not transferable canon grades. Preserve their definitions and ask lore to map them explicitly.
- An etic generator/framework remains designer metadata; it does not automatically become the fictional culture's emic self-description. Lore may separately approve an in-world analytical tradition.
- Contradictory attributed accounts may coexist; conflicting unqualified world-facts require lore review. Kotodama flags the distinction without adjudicating which account is true.

## 7. Era staging: align records without a universal ladder

Keep artifact release time, scholarly source date, fictional event time, and in-world narrator/document date in different fields.

| Staging situation | Language / naming | Myth / symbol | Costume / material | Lore-facing question |
|---|---|---|---|---|
| Baseline under design | Fix a variety, script, naming slots and referent keys | Specify tellers, sign context and competing readings | Define materials, production and wearer categories | Which assumptions are already canon constraints? |
| Contact / coexistence | Loans, bilingual labels, exonyms, mixed scripts | Rival associations, translation or syncretism candidates | Imported cloth, copied cuts, hybrid terms | Which contacts and populations actually exist? |
| Reform / rupture | Proposed sound/script/name reforms; rates of uptake | Reinterpretation, suppression, rival ritual calendars | New permissions, shortages, substitution, regulation | What changes, for whom, and on which dates? |
| Retention / revival | Archaic liturgical names beside current everyday forms | Reconstructed tradition or disputed antiquity | Heirlooms, ceremonial copies, regional survivals | Is continuity asserted, demonstrated, or invented in-world? |

- These are optional analytical situations, not a required historical sequence; they can overlap across regions and social groups.
- Record start/end bounds, uncertainty, calendar/conversion rule, and applicable group for each edge. For machine interchange, use a declared half-open interval convention; retain uncertain bounds rather than invent precision.
- Prescribed introduction, first attestation, popular uptake, and later retrospective description need separate dates when known; an old name on a new object is not automatically an error.
- Do not map Stone/Bronze/Iron, oral/literate, political centralization, dress complexity, and language type onto one progress scale. Use `era-periodization-models.md` as a question set, not universal chronology.

## 8. Transfer and receipt procedure

1. Lore supplies a scoped brief, baseline bible reference, existing entity/era keys, constraints, canon policy, and the actual authorized receipt surface; absent inputs become explicit questions.
2. Both lanes satisfy §1's same-revision read gate; unresolved boundary conflicts take §10's route before affected work proceeds.
3. Kotodama assembles the envelope and payload, lists alternatives, checks local generation/derivation, and produces a cross-system impact report; this is not bible-wide consistency certification.
4. Kotodama submits immutable bytes and a digest manifest, naming lore as recipient. Submission, delivery, and silence are never acceptance.
5. Lore verifies receipt completeness, sources/uncertainties, entity mapping, timeline applicability, and bible-wide consistency against the named baseline; changed baselines require revalidation before acceptance.
6. Lore returns a receipt containing packet ID/version/digest, contract reference, review baseline, per-record disposition/reason, unresolved blockers, and reviewer/time/evidence pointer.
7. Acceptance becomes a canonized import only when the receipt also names approved bible IDs, the resulting bible revision, retained qualifiers, and any required operator approval. Otherwise record `accepted for integration; not yet canonized`.
8. For partial acceptance, lore enumerates accepted record IDs and prerequisite closure; deferred/rejected alternatives remain noncanon. No accepted label may depend on an unaccepted rule unless the frozen selected form is explicitly accepted as an exception.
9. Kotodama records the returned receipt pointer without editing it; revisions use §9. Lore may ask for repair, but does not edit the generator in kotodama's repo.

A transport acknowledgement means only “bytes received”; a review acknowledgement means only “read.” Both differ from a disposition and from a completed canon import.

## 9. Versioning, invalidation, and retcon safety

Maintain distinct versions for **this interface**, **each system/rule/lexicon packet**, and **lore's bible revision**; none is the fictional era number.

| Change | Release treatment | Required downstream action |
|---|---|---|
| Editorial correction with unchanged forms, meanings, references and decisions | PATCH | Publish corrected bytes and provenance; receivers explicitly record any adopted replacement |
| Optional field, new independent sense, compatible alternative or deprecation | MINOR | Declare added scope; existing accepted records remain unchanged; no implicit acceptance of additions |
| Required-field change, altered sense/derivation, remapped identity, changed era bounds or existing name | MAJOR when it breaks the declared consumer contract | Supply migration map, affected record/edge list, options and renewed lore review |
| Source retraction, discovered mistranslation, or invalid derivation | Withdraw/flag affected release; publish a correcting release classified by compatibility | Notify lore immediately; lore assesses accepted assertions and any canon/attribution correction |
| Contract authority/scope change | Treat as a breaking interface proposal | Integrator ruling where contested, then both-lane re-read; no lane transfers ownership unilaterally |

- Initial `1.0.0` proposes a stable consumer interface; bilateral acknowledgement is still required. Experimental `0.y.z` or prerelease packets must declare instability and cannot silently replace accepted dependencies.
- Freeze released versions; corrections are new records/releases with `supersedes`/`derived_from` references, not rewrites of old receipts or accepted snapshots (PROV-DM revision; SemVer rule 3).
- State compatibility in observable terms: can the old consumer reproduce accepted forms/senses and interpret fields unchanged? A scientifically better derivation can still be a breaking change.
- Maintain old→new record mappings, including splits/merges and unmapped cases; preserve obsolete names as historically scoped aliases where lore approves, never delete their history by normalization.
- Traverse changed coupling edges to lexica, names, ritual variants, symbolic readings, era matrices and garments; distinguish directly changed records from merely flagged dependants.
- Lore pins exact delivered versions and digests, not version ranges. No auto-upgrade, including PATCH: even a corrected citation needs an auditable adopted revision.
- A system update changes proposals, not previously canonized facts. Lore can retain an older selected form, approve an irregularity, defer migration, or authorize a retcon under its policy.
- Rollback is a new recorded decision restoring a named earlier snapshot; preserve intervening receipts and explain what is superseded. Do not erase the audit trail.

## 10. Contested-scope escalation

| Finding | Route | Safe work while unresolved |
|---|---|---|
| A request asks kotodama to decide an event, identity, pantheon truth or official costume | Return canon decision to lore | Supply bounded alternatives and consequences |
| Lore requests a generative repair or new diachronic rule | Kotodama, within the brief | Validate local rule effects; lore retains canon consistency checks |
| Both lanes claim ownership, or a consistency request straddles generation and canon | Report to fleet integrator | Freeze only disputed output/import; continue separable reference work |
| Evidence retrieval methodology is the actual task | Route to chousa; preserve domain question | Mark unsupported claim `(to-verify)`; do not invent source coverage |
| Rights, restricted cultural knowledge, or publication permission is unresolved | Operator / appropriate authorized specialist | Hold restricted material; a bibliography is not permission |

- Scope report fields: issue ID; originating request; both province clauses; exact disputed action; affected packet/record versions; evidence pointers; options/costs; current hold; requested ruling.
- File the issue through each lane's permitted reporting route; the integrator records the ruling and routes boundary refinements to the authorized owners. Neither lane edits the other's province or this contract by proxy.
- Distinguish **scope ruling** from **canon ruling**: integrator resolves ownership; lore resolves canon within its authority; operator gates remain in force.
- If no ruling exists by the next completed round, re-flag the issue in the lane report for integrator/aggregator tracking. Silence, elapsed time, first authorship, and a passing local check never award scope.

## 11. Provenance cautions and acceptance checklist

- For each real-world source, preserve author/year, title/edition, page/section/object identifier, translation/editor, access locator, exact supported claim, and how it was transformed into a design option.
- Distinguish primary attestation, later compilation, modern reconstruction, scholarly comparison, and deliberate invention; a citation to an entire tradition does not substantiate a particular garment or name.
- Mark colonial, missionary, administrative, elite or outsider filters explicitly; identify whose speech/practice is missing and whether independent/community-authored evidence was checked. Do not claim consultation or consent that did not occur.
- Where chronicle evidence is scarce, oral transmission, archaeology, later testimony and reconstruction remain different evidence kinds. Write `thin coverage` / `unknown` / `(to-verify)` per field; silence is not proof of absence.
- This contract is not a civilization survey: it establishes no tradition-specific expertise. A received civilization dossier must disclose which languages, periods and source traditions its compiler cannot assess.
- Comparative or pop frameworks are generation aids, not validated universal histories. Identify a contested or discredited **claim** and its supporting critique before exporting that calibration; do not flatten an entire tradition into a single verdict.
- [ ] Both-lane read records agree on contract revision/digest; packet and baseline references resolve.
- [ ] Every delivered record has scope, stable identity, provenance/invention status, and a disposition question; unknowns are not blank cells.
- [ ] Lexicon/name derivations and fixtures are reproducible; each material/ritual term resolves through the coupling register; test results name actual inputs and outputs.
- [ ] Era overlap, register variation, belief versus world-fact, prescriptions versus practice, and legacy advisory tags remain distinguishable.
- [ ] Dependency closure and an impact/migration list are available; open blockers prevent affected canon import, not unrelated method work.
- [ ] Lore's receipt separates delivery, review, acceptance, and canonized bible revision; no producer-issued canon certification appears.

## 12. Apply to a fictional culture: handoff drill, not canon

| Dossier component | Prepare as method output | Decision reserved for lore |
|---|---|---|
| Language family + writing | Proposed internal genealogy/contact model; real typological inspirations separately cited; varieties, scripts and media | Which speakers, relations and scripts exist in the world |
| Mythic / pantheon core | Variant graph, attributed tellers, cult epithets, no forced single pantheon | Which variants are held, by whom, and which supernatural propositions are true |
| Symbolic system | Context-specific sign→interpretation rules, exceptions and competing readings | Which institutions use the signs and whether any claimed efficacy is real |
| Era model | Relative stages, calendars, reform/retention alternatives and uncertainty | Dates, era boundaries and event ordering |
| Costume / material signature | Fiber/process/trade assumptions, cut, garment terms, wearer/occasion rules, surviving-object cautions | Actual availability, enforcement, wearers and canon artifacts |
| Naming practices | Slot grammar, derivation fixtures, life-stage/address use, exonyms and unresolved target IDs | Entity identity, approved names and historical aliases |

1. Begin with lore's brief; fill each component above with either a bounded proposal or an explicit knowledge gap, not a borrowed civilization package.
2. Follow a candidate garment term through material process → lexeme/sense → ritual use → sign reading → wearer-title/name → era scope; record every link as an edge with its own justification.
3. Change a technique or script rule in a trial revision; enumerate the impacted terms/names and retained exceptions. This demonstrates the dependency method without establishing fictional history.
4. Hand lore the frozen proposal, alternatives, provenance cautions and requested decisions. Rehearse both partial acceptance and rejection; neither requires inventing a canon outcome.

## 13. What a worldbuilder can take

- Take a reproducible language–myth–symbol–era–costume coupling graph, explicit naming/lexicon records, and a reviewable change path; do not take the existence of a polished packet as a canon decision.
- Take comparative mechanisms and bounded reference claims, with their source filters and thin-evidence warnings; do not transplant a living tradition or treat access/citation as permission.
- Take a clear division of labor: **kotodama proposes and traces systems; lore selects, records, and verifies canon; the integrator arbitrates contested scope**. Bilateral reading and receipts remain required, not self-attested here.
