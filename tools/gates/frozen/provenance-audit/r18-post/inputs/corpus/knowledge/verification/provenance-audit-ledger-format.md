# Provenance Audit Ledger Format — Per-Round Evidence and Append-Only Corrections
- topic: A durable, claim-level source-audit record for linguistic-cultural coupling: entry schema, calibrated verdicts, evidence dependencies, era boundaries, and non-destructive correction history.
- sources: Luc Moreau and Paolo Missier, eds. (2013), PROV-DM: The PROV Data Model, W3C Recommendation, 30 April; John A. Kunze et al. (2018), The BagIt File Packaging Format (V1.0), RFC 8493; Stephanie Russo Carroll et al. (2020), “The CARE Principles for Indigenous Data Governance,” Data Science Journal 19, article 43; Linda Tuhiwai Smith (2021), Decolonizing Methodologies: Research and Indigenous Peoples, 3rd ed., Zed Books.
- couples: language — linguistics/{historical-linguistics,writing-systems,naming-systems}.md; myth/symbol — myth-symbol/{comparative-frameworks,symbolism-synthesis-method}.md; era/costume — culture-material/{era-periodization-models,dress-through-eras,material-culture-inference-method}.md; siblings — evidence questions to chousa-shokunin, reference-only handoff to lore-shokunin; no sibling writes or canon decisions.

## 1. Standing, provenance, and boundaries

- Format identifier: `kotodama.provenance-audit/1`; the schema and verdict rules below are lane-local craft conventions, not an external certification standard.
- source: The editions and links in §12; PROV-DM supplies provenance concepts, BagIt supplies a fixity comparison, and CARE supplies governance principles. None prescribes this ledger schema.
- verified-at: 2026-10-17 — PROV-DM, RFC 8493, and the CARE article inspected online; Smith's edition, contents, and publisher summary checked through a library catalogue only.
- recheck: At reuse, check the actual cited passage, edition, access conditions, corrections, and changed URLs; bibliographic verification never substitutes for passage verification.
- A source audit asks what a reference warrants; a craft-round axis verdict asks what improved. Keep those records separate: `supported` does not mean `improved`, and neither means canon.
- Record one atomic claim at one target revision per event; a round may produce many such events. Do not bundle a whole culture into one passing verdict.
- Suggested future ledger location: `corpus/lessons/provenance-audit-ledger.md` within this lane; this format entry does not create a ledger or declare a completed round.
- Lore-shokunin decides fictional truth. This lane records reference support, design transformations, limits, and handoff recommendations; it never changes the world bible.

## 2. Provenance model: entities, activities, agents

PROV-DM (Moreau and Missier 2013, §§2.1–2.2) distinguishes entities, activities, agents, and provenance bundles; use these distinctions without claiming full PROV conformance.

| Ledger object | Provenance role | Operational distinction |
|---|---|---|
| Particular edition, inscription image, recorded performance | Entity used as evidence | A work title alone does not identify the consulted witness. |
| Exact corpus claim at a fixed revision | Entity being assessed | A changed sentence is a new claim revision, even at the same path. |
| Reading, transcription comparison, translation check | Activity | Record what was actually done, not merely the intended search. |
| Auditor, translator, editor, responsible institution | Agent with a named role | Tool/model assistance does not become a scholar or an independent witness. |
| Event recording that assessment | New provenance entity | The audit itself has an author, date, method, and limitations. |
| Per-round set of event IDs | Bundle-like grouping | Groups evidence; it does not grant every member the same verdict. |

Preserve distinct edges for quotation, revision, and inference. A costume inference derived from a lexical observation is not another attestation of that observation.

## 3. Event schema and identity

Store each future event as a heading `## <entry_id>` followed by one fenced JSON object. UTF-8 text, stable field names, no duplicate JSON keys, one completed object per append.
Every field below is required; unknown scalar values use `null` plus an explanation in `limits`. Empty arrays mean no members, never “not checked.” Angle-bracket values in §9 are template slots, not valid submitted evidence.

| Field | Type / constraint | Meaning |
|---|---|---|
| `schema_version` | Integer; currently `1` | Never reinterpret an old event using a later schema silently. |
| `ledger_id` | Stable string | Identifies this lane's particular ledger across file moves. |
| `entry_id` | Unique string | Prefer `kotodama:rN:eNNNN`; never recycle an ID. |
| `sequence` | Positive integer, increasing in append order | Orders storage, not historical events or the cultures being studied. |
| `event_type` | `audit`, `recheck`, `correction`, `withdrawal` | All types carry a complete assessment, not an implicit patch. |
| `round_id` | Dispatched lane-round identifier or `null` | Use the actual lane's counter; an unsteered mint task names its assignment in `reason`. |
| `recorded_at` | UTC timestamp with `Z` | Actual append time; late work keeps its original round ID without backdating. |
| `auditor` | Object: `id`, `role`, `method` | Accountable actor and executed inspection method. |
| `reviewer` | Object: `id`, `independence` | `independence`: `not-reviewed`, `author-side`, `non-author`; absent reviewer has `id: null`. |
| `target` | Object: `path`, `revision`, `locator` | Lane-relative path, immutable revision/digest, heading plus exact passage locator. |
| `claim` | Object: `id`, `revision`, `text`, `kind` | Stable claim ID; revision integer; exact text; kind vocabulary below. |
| `scope` | Object: `people`, `region`, `social_group`, `time_range`, `tradition`, `language`, `script` | Explicit boundaries; `null` is unknown, `not-applicable` is a reasoned string value. |
| `systems` | Nonempty array | Members: `language`, `myth`, `symbol`, `era`, `costume`, `method`. |
| `couplings` | Array of objects: `from`, `to`, `relation`, `evidence_ids` | Directed cross-system links; `relation` states the claimed mechanism, not merely resemblance. |
| `sources` | Array of source objects, §4 | Include counterevidence and intermediary sources, not just favorable references. |
| `checks` | Array of objects: `check`, `result`, `pointer` | `result`: `done`, `blocked`, `not-run`; a completed search can still find nothing. |
| `verdict` | One value from §5 | Assesses the exact claim, not the author's reputation. |
| `calibration_flags` | Array of strings | Explicit uncertainty/bias flags; definitions in §5. |
| `rationale` | String | Connect the inspected evidence to this verdict and its scope. |
| `limits` | Array of strings | Missing pages, unknown dates, thin expertise, alternative readings, access problems. |
| `disposition` | One value from §5 | Reference-use recommendation, never permission to make canon. |
| `depends_on` | Array of event IDs | Audited upstream claims on which this inference relies. |
| `supersedes` | Array of earlier event IDs | Explicit replacement links for the same claim; empty for the first assessment. |
| `reason` | String | Trigger, correction reason, or withdrawal reason; no unexplained verdict flips. |
| `follow_up` | Array of objects: `task`, `owner`, `trigger` | Durable unresolved work; use a named lane/role, not an invented assignment acceptance. |

`claim.kind` is `attestation`, `historical-inference`, `comparison`, `design-rule`, or `method`. A myth's attested statement and the historical reality of its narrative require different claims.
Pin `target.revision` to an actual immutable revision or a digest of the exact inspected bytes, with its algorithm. A moving branch name or “current” is insufficient; if unavailable, keep the limitation and withhold reference-ready status.

## 4. Source subrecord: identify, inspect, relate

Every member of `sources` has these fields; a source ID identifies one edition/witness/access snapshot, not all versions of a work.

| Source field | Required content |
|---|---|
| `source_id` | Stable local ID; a new translation or changed web witness gets a new snapshot ID. |
| `citation` | Author/editor, year, title, edition, publisher/journal; translator and original date where relevant. Unknown information is marked `(to-verify)`, not guessed. |
| `identifier` | DOI, ISBN, shelfmark, accession ID, or stable URL; include the repository/institution for an object or manuscript. |
| `locator` | Page/section/line, folio, object side, figure, or recording timestamp; distinguish printed pagination from PDF image numbering. |
| `genre` | Specific genre: chronicle, inscription, lexicon, oral performance, object, image, scholarship, catalogue, standard, or another explicit label. |
| `witness_context` | Production/collection date, claimed event date, locality, maker/speaker, audience, patron/collector, and transmission history as known. |
| `bibliography_status` | `located`, `not-located`, `identity-conflict`; located means that bibliographic identity was checked, not that the contents are correct. |
| `access` | `passage-inspected`, `metadata-only`, `inaccessible`, `not-attempted`; an abstract, snippet, catalogue, or review is not inspection of the cited book passage. |
| `checked_at` | Actual access date/time or `null` with a limit; never manufacture precision from a remembered consultation. |
| `evidence` | Short accurate quotation or explicitly labeled paraphrase; preserve relevant negation and uncertainty; obey access/reuse restrictions. |
| `language_translation` | Original language; consulted translation/editor; own translation or machine assistance disclosed; unresolved readings marked `(to-verify)`. |
| `relation` | `supports`, `qualifies`, `contradicts`, `context-only`; attach it to this claim only. |
| `dependency_group` | Shared underlying witness/source chain; use `unknown` when independence has not been established. |
| `integrity` | Object with `algorithm`, `digest`, `snapshot_pointer`; all may be `null` if no lawful durable snapshot was made. |
| `governance` | Known attribution, sensitivity, access, community-control and reuse constraints; `unknown` is not consent or a rights ruling. |

Record a secondhand citation as “A cites B” and audit A's passage; do not mark B inspected. Several websites copying one translation remain one dependency group, not independent corroboration.
A search-engine or AI-generated citation is a lead. Unresolved author/year/title, DOI mismatch, or an unavailable passage stays `(to-verify)` at the point of use.

## 5. Verdict vocabulary and use recommendations

These are categorical judgments, not a summed confidence score. A prestigious or early source can be biased, mistaken, prescriptive, or irrelevant to this particular claim.

| `verdict` | Required interpretation | Default disposition |
|---|---|---|
| `supported` | Directly inspected, relevant evidence supports the exact scoped claim; no known unresolved material counterevidence. | `reference-ready`, subject to the separate safeguards below. |
| `qualified` | Evidence is partial or the interpretation uncertain; state exactly what is and is not warranted. | `conditional-reference`; retain visible limitations. |
| `contested` | Material competing interpretations or witnesses remain unresolved; name them and their disagreement. | `conditional-reference` for the disagreement only; otherwise `hold`. |
| `contradicted` | Inspected evidence materially opposes the claim as written; cite the opposing passage. | `withdraw-reference`; a replacement claim needs its own audit. |
| `unverified` | Identity, passage, scope, translation, or inference cannot yet be checked. Includes metadata-only checks. | `hold`; mark the unresolved claim `(to-verify)`. |
| `not-applicable` | No external factual assertion is being made, as with an explicitly local design convention. | `method-only`; never use to bypass factual checks. |

- `reference-ready` additionally requires a pinned target, resolvable evidence, and no unresolved material governance restriction; `hold` overrides any favorable verdict when these are missing.
- Local design rules may have provenance explaining their inspiration, but scholarship does not “prove” the fictional rule. Split any historical justification into separately audited factual claims.
- Suggested flags: `thin-local-expertise`, `limited-chronicle-evidence`, `colonial-mediation`, `elite-survival-bias`, `translation-dependent`, `dating-uncertain`, `source-dependent`, `framework-contested`, `discredited-as-evidence`, `restricted-use`.
- Explain each flag in `limits`. Scarce chronicles do not make a tradition unknowable or oral evidence intrinsically inferior; identify the actual corpus and the question it can answer.
- Universal symbol dictionaries or a monomyth template do not establish a culture's historical meanings. Record their use as designer comparison, not attestation; claims of scholarly discredit themselves require a checked critical source.
- A failed search is not proof a practice never existed. Log repositories, queries, languages, date bounds, and unavailable material before stating the bounded negative result.

## 6. Coupling coverage: audit the bridge, not only the endpoints

For any civilization/reference profile, make separate claims for every row below; “not examined” is a gap, never an implicit pass. No profile is attested by this format entry itself.

| System / bridge | Minimum audit question | Frequent unsupported leap |
|---|---|---|
| Language family + writing | What classification, date, variety, script, and decipherment status does the source actually support? | Shared script proves shared ancestry; historical label denotes one uniform language. |
| Naming + language | Is the form a personal name, title, epithet, exonym, or later normalization; whose social/register rules apply? | Royal or masculine naming evidence represents everyone. |
| Myth/pantheon core | Which recension, cult, narrator, locale, and era attest the deity or narrative relationship? | A late synthesis supplies a timeless national pantheon. |
| Symbolic system | Is meaning supplied by participant exegesis, contextual association, analyst interpretation, or modern reuse? | A color or animal has one meaning across all eras and communities. |
| Era model | Who named the period, by what evidence, with what regional boundary uncertainty? | A dynastic boundary instantly changes speech, dress, and belief together. |
| Costume/material signature | Does the evidence establish material, cut, manufacture, wearer, occasion, or regulation; which remain inference? | Painted color proves a dyestuff; sumptuary law proves actual compliance. |
| Language → myth/symbol | Is the proposed etymology or homophony present in the relevant historical variety? | A modern pun explains an ancient cult name. |
| Myth/symbol → costume | What connects text, depicted garment, excavated object, and interpreted wearer? | Co-occurrence proves exclusive priestly or ethnic ownership. |
| Era → all systems | Is the coupling contemporaneous, inherited, revived, borrowed, or only a designer analogy? | Similar motifs prove contact, descent, or a single historical cause. |

Endpoint verdicts do not transfer across the arrow: a checked garment word plus a checked myth does not verify a causal relationship between them. Each bridge needs its own claim and evidence or an explicit design-rule label.

## 7. Era staging and source survival

- Keep separate clocks: claimed event/practice interval; witness production date; manuscript/object survival or collection date; edition/translation date; audit timestamp.
- Stage reference claims as `earlier-attested`, `later-attested`, `retrospective-report`, or `modern-reconstruction` in `witness_context`; these describe evidence relationships, not universal civilization stages.
- A first surviving attestation supplies an observed bound, not automatically an invention date. “Still used” requires later evidence, not an empty interval between finds.
- For a revival, distinguish the older attestation, the reviver's claimed continuity, and the modern reconstruction; neither authenticity nor fraud follows from resemblance alone.
- When chronicles are scarce, record which oral, linguistic, archaeological, visual, and community-held evidence was examined and which was unavailable; do not invent bridging centuries.
- Thin local expertise requires a named review need, not a blanket confidence downgrade for an entire people. This entry has not surveyed any tradition-specific chronicle corpus: such coverage remains `(to-verify)` in actual applications.

## 8. Append-only rules and active-view reconstruction

1. Append complete events at EOF; never rewrite, delete, sort, renumber, or silently “clean up” a filed event. Fix typographical and bibliographic errors with a new correction identifying the old field.
2. `correction` and `withdrawal` must name earlier `supersedes` IDs and give a reason. A `recheck` replacing an earlier assessment also names it; a changed claim text increments `claim.revision`.
3. A changed culture/time/scope is not a silent correction of the old proposition: create a new claim ID, retain the old assessment, and explain the relationship in `reason` and dependencies.
4. Supersession may connect only the same claim ID and must point backward in append order; prohibit cycles, duplicate IDs, and dangling links. A `withdrawal` must use `disposition: withdraw-reference`; it retracts support without proving the opposite. Only a new, justified assessment may reopen reference use.
5. Reconstruct the active view per claim ID by following explicit supersession edges; no “latest timestamp wins.” A unique unsuperseded leaf is current; multiple leaves are an unresolved fork, held from reference-ready use.
6. Resolve a fork by appending an assessment that names every conflicting leaf it supersedes and explains the evidence. Never choose the most favorable verdict or discard a dissenting witness.
7. A changed source snapshot receives a new source ID. A corrected URL or new edition does not overwrite an earlier event's access history; append a new event with the new pointer.
8. If upstream evidence is withdrawn or materially revised, identify all `depends_on` consumers and queue rechecks; current-use views hold those descendants until rechecked. No automatic reversal of every descendant's factual verdict.
9. Serialize concurrent appends through one responsible writer; colliding sequences or partial objects are conformance defects. Do not let a second writer edit a closed prefix to fix a collision.
10. Persist checkpoints of the exact closed prefix's byte length and digest against an independently retained anchor; exclude a checkpoint's own bytes from the bytes it describes. A digest printed from a mutable file alone detects no drift.
11. BagIt (Kunze et al. 2018, §§2.1.3, 3, 5.4) compares stored manifests with file bytes; that is a useful fixity analogy, not proof of scholarly truth, authorship, or protection against active tampering.
12. Restrict sensitive material before appending: record only permissible metadata, not sacred/restricted passages or personal details. Escalate accidental exposure to the responsible operator; never replicate it in an erratum.
13. New schema versions append a migration note and conversion rules without reformatting historical bytes. Derived indexes may be regenerated, but must name their input checkpoint and never replace the underlying events.

## 9. Copyable event skeleton

Template only, not an executed audit or a fabricated round. Replace every `<...>` slot, use actual identities/times/revisions, and populate source objects per §4 before a factual claim can become reference-ready.

```json
{
  "schema_version": 1,
  "ledger_id": "kotodama:provenance",
  "entry_id": "kotodama:r<ROUND>:e<SEQUENCE>",
  "sequence": 1,
  "event_type": "audit",
  "round_id": "kotodama:round-<ROUND>",
  "recorded_at": "<ACTUAL-UTC-TIMESTAMP>",
  "auditor": {"id": "<AUDITOR>", "role": "source-auditor", "method": "<EXECUTED-CHECK>"},
  "reviewer": {"id": null, "independence": "not-reviewed"},
  "target": {"path": "<LANE-RELATIVE-PATH>", "revision": "<IMMUTABLE-REVISION>", "locator": "<EXACT-PASSAGE>"},
  "claim": {"id": "<STABLE-CLAIM-ID>", "revision": 1, "text": "<EXACT-CLAIM> (to-verify)", "kind": "historical-inference"},
  "scope": {"people": null, "region": null, "social_group": null, "time_range": null, "tradition": null, "language": null, "script": null},
  "systems": ["language", "myth", "symbol", "era", "costume"],
  "couplings": [],
  "sources": [],
  "checks": [{"check": "inspect supporting passage", "result": "not-run", "pointer": null}],
  "verdict": "unverified",
  "calibration_flags": ["thin-local-expertise"],
  "rationale": "No inspected source passage yet supports this claim.",
  "limits": ["Scope fields and source witnesses remain unestablished (to-verify)."],
  "disposition": "hold",
  "depends_on": [],
  "supersedes": [],
  "reason": "<AUDIT-TRIGGER>",
  "follow_up": [{"task": "locate and inspect the relevant witness", "owner": "<RESPONSIBLE-ROLE>", "trigger": "before reference reuse"}]
}
```

## 10. Per-round application and closure checks

1. Freeze the delivered target revision; enumerate new/changed factual claims and affected coupling edges. Name the inspected population; any sample reports its selection rule and unaudited remainder.
2. Inspect identifiers and passages, record source chains and counterevidence, then test scope, translation, era, and bridge mechanisms independently. Do not turn a catalogue hit into a content pass.
3. Append claim events; distinguish performed checks from blocked/not-run checks. Record access failure as failure to inspect, not evidence that the work or practice is nonexistent.
4. Validate required fields, enums, unique IDs, increasing sequences, backward supersession, resolvable dependencies, pinned targets, and evidence locators. Structural validity does not validate a historical interpretation.
5. Reconstruct the active view, flag forks and affected descendants, and hand off only the eligible reference material with its exact event IDs and limitations.
6. In the ordinary round report/LOG, cite the round's event IDs, checkpoint, commands actually run, and observed counts by verdict; keep “new events,” “claims audited,” and “active claims” separate denominators.
7. Keep unresolved `follow_up` work visible across rounds with owner and trigger. A round can close with held references; a closed round does not settle them or erase them from the queue.

## 11. What a worldbuilder can take; provenance cautions

- Take the traceable reasoning shape: language form → interpretation → material practice, with era and social boundaries at every arrow. Copy the audit discipline, not a living culture's names, sacred repertoire, or costume as a package.
- Take supported reference observations as constraints or comparisons; label invented links as design choices. Lore receives the distinction, not a pre-decided canon tag masquerading as evidence.
- CARE (Carroll et al. 2020, “The CARE Principles” and “The CARE Principles and Their Supporting Concepts”) names Collective Benefit, Authority to Control, Responsibility, and Ethics. Public accessibility does not itself settle community authority or appropriate reuse.
- Colonial collection, elite patronage, translation, and archival survival can shape what is visible. Record the actual mediation and missing perspectives rather than pretending a technically tidy ledger removes those biases.
- Smith (2021) is a decolonizing-research orientation, not a universal permission checklist or a substitute for local authority. Specific passage-level applications from that book remain `(to-verify)` until its text is inspected.
- This document supplies no civilization-specific facts and no rights/attribution ruling; tradition-specific expertise, scarce evidence, and sensitive reuse must be assessed in the actual reference audit.

## 12. Checkable editions and verification limits

- Moreau, Luc, and Paolo Missier, eds. (2013). [PROV-DM: The PROV Data Model](https://www.w3.org/TR/2013/REC-prov-dm-20130430/). W3C Recommendation, 30 April 2013. Inspected: §§2.1–2.2 on entities/activities/agents, derivation, and provenance of provenance; not a historical source-reliability scale.
- Kunze, John A., Justin Littman, Liz Madden, John Scancella, and Chris Adams (2018). [The BagIt File Packaging Format (V1.0)](https://www.rfc-editor.org/rfc/rfc8493.html). RFC 8493, October 2018; DOI: 10.17487/RFC8493. Informational RFC, explicitly not an Internet Standards Track specification; inspected §§2.1.3, 3, 5.4.
- Carroll, Stephanie Russo, et al. (2020). [“The CARE Principles for Indigenous Data Governance”](https://datascience.codata.org/articles/10.5334/dsj-2020-043). Data Science Journal 19, article 43; DOI: 10.5334/dsj-2020-043. Article inspected; apply its governance principles with the relevant people, not as authorization granted by this lane.
- Smith, Linda Tuhiwai (2021). Decolonizing Methodologies: Research and Indigenous Peoples. 3rd ed. London/New York: Zed Books. ISBN 9781786998132. [Canadian Centre for Architecture catalogue record](https://www.cca.qc.ca/en/search/details/library/publication/1242806586) inspected for edition, contents, and publisher summary; book passages not inspected here `(to-verify)`.
