# Round 50 — lesson (kotodama, hyaku phase 2)

source: `reports/round-50/claims.json` (declaration); `reports/round-50/validation.json` (acceptance receipt); `.ufo/waves/round-50/` (wave specs, registries and seat reports); the URLs opened in `## Gate`
verified-at: 2026-10-21 — lane `main`, base `4ad2683`; Gate rows opened the same day by round-50 build seats and re-checked by the integrator where noted
recheck: whenever a `corpus/SOURCES.md` row's `status`, `recheck` or `used-by` changes (log old→new in that round's lesson), and on the per-row `recheck` cadences
scope: the round-50 record — Gate evidence for SOURCES S048–S069, the outside spot-check intake, mined mistakes and frontier; it admits nothing and certifies no verdict

Round 50 is kotodama's first hyaku-campaign round and its first round on the jj-colocated
lane. Coordinator: ChousaR27R2 (reused idle agent; Main spawn job-capped). Claims
(`reports/round-50/claims.json`): **C** coverage — `culture-material/pastoralism-animal-husbandry.md`;
**O** operability — `tools/harness/receipt_guard.py` and `tools/check-readme-revisions.py`
made correct under jj colocation, with `reports/round-50/jj-colocation-probe.py`;
**Ca** calibration — `tools/check-claim-separability.py`, its frozen round-49 fixture and
QUALITY criterion 7. Verdicts live in `reports/round-50/validation.json`, `SCORECARD.md`
and `LOG.md`.

## Spot-check intake (round-49 outside verifier)

`corpus/lessons/round-49-verifier-spotcheck.md` adjudicated round 49 REJECTED-HONEST-STOP on
claim separability: claim C cited the registry claim S created, and the runner's
`c_without_s` leg checked inline URLs instead of removing S's rows. Disposition: turned into
QUALITY criterion 7 plus an executable control (Ca); this round's own manifest declares
`corpus/SOURCES.md` as a land of C, because the rows C cites are C's sources. The tier and
quote disagreements were already learned as QUALITY criterion 6 in round 49. No
`operator-*.md` lesson exists in the lane.

## Gate

Every row S048–S069 was opened on 2026-10-21 by the round-50 build seat named in its
bullet (reports under `.ufo/waves/round-50/build/`). S048 and S049 quotes were re-fetched
by the integrator and matched under the named headings.

- S048 — https://www.fao.org/4/y2647e/y2647e02.htm — accessed 2026-10-21 — §Classifying pastoral systems: "there is little or no impetus to herd animals". Grounds the register's conditions, typology, species count and stage-ladder refutation. Seats: ScribeSec01Register, ScribeSec11Decision, ScoutCalibrationRegistry; integrator re-fetch.
- S049 — https://www.fao.org/4/y2647e/y2647e08.htm — accessed 2026-10-21 — §Land tenure and the common property resources debate: "Tenure is thus divided by both ecology and the potential for agriculture." Grounds §8 and the labour-wealth link (§Social structures). Seat: ScribeSec11Decision; integrator re-fetch.
- S050 — https://pmc.ncbi.nlm.nih.gov/articles/PMC2575338/ — accessed 2026-10-21 — §Initial Animal Domestication in the Fertile Crescent, penultimate paragraph: "with all four major livestock species coming under management over a period from ca. 11,000 to 10,000 B.P." Seat: SrcZederDomestication (PNAS DOI page 403; PMC full text used).
- S051 — https://link.springer.com/article/10.1007/s10963-011-9045-7 — accessed 2026-10-21 — Abstract, opening sentence: "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction". Seat: SrcSherratt.
- S052 — https://people.duke.edu/~ldbaker/classes/gradtheory/Evans_Pritchard_E_E_The_Nuer_a_description_of_the_modes_1940.pdf — accessed 2026-10-21 — Ch. I §I, p. 19: "Nuer tend to define all social processes and relationships in terms of cattle." Seat: SrcEvansPritchard (archive.org unreachable; Internet Archive-digitized mirror opened and page images read).
- S053 — https://journals.openedition.org/tc/14002 — accessed 2026-10-21 — Texte intégral, opening paragraph: "L’omniprésence des bovins dans les pratiques et les discours des populations nilotiques d’Afrique de l’Est fut à l’origine de l’expression cattle complex (Herskovits 1926)." Seat: SrcHerskovits (Herskovits 1926 itself unreachable on every route).
- S054 — https://web.mit.edu/2.813/www/readings/HardinCommons.pdf — accessed 2026-10-21 — p. 1244, §The Tragedy of Freedom in a Commons: "The tragedy of the commons develops in this way. Picture a pasture open to all." Seat: SrcHardin (science.org 403).
- S055 — https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf — accessed 2026-10-21 — §4E Long-Surviving Resource Institutions, PDF p. 15: "The design principles appear to synthesize core factors that affect the probability of long-term survival of an institution developed by the users of a resource." Seat: SrcOstrom.
- S056 — https://www.scielo.cl/pdf/chungara/v51n1/0717-7356-chungara-00302.pdf — accessed 2026-10-21 — Abstract, p. 85: "always experienced a need for external agricultural and handicraft products". Seat: ScribeSec09Relations.
- S057 — https://www.routledge.com/Pastoralists-Equality-Hierarchy-And-The-State/Salzman/p/book/9780813338149 — accessed 2026-10-21 — Description ¶1 sentence 2: "provides detailed analyses of divergent types of pastoral societies, including segmentary tribes, tribal chiefdoms, and peasant pastoralists". Grounds the publisher's description only (tier B, QUALITY 6). Seat: SrcGalatyJohnson.
- S058 — https://www.fao.org/4/y5115e/y5115e00.htm — accessed 2026-10-21 — chapter y5115e08, item 2 (baartol): "Typically, seasonal migration starts with the beginning of the rains in May or June and leads towards the west." Seat: SrcFulani.
- S059 — https://sametinget.se/renmarken — accessed 2026-10-21 — opening paragraph under the H1: "Ett renmärke är kombinationen av snitt på både höger och vänster öra. Renmärket talar om vem som äger renen." Seat: SrcSamiReindeer.
- S060 — https://d-nb.info/1152169939/34 — accessed 2026-10-21 — §2 Bayankhongor province ¶2 (PDF p. 4): “an aggregate of the “five snouts” represented by horses, yaks/cattle, camel, goats and sheep”. Seat: SrcMongolFiveSnouts.
- S061 — https://www.fao.org/4/AD347E/ad347e0j.htm — accessed 2026-10-21 — ch. 8 Management of Yak, Overview ¶1: "During the warm season of summer and autumn, yak are on pastures at high elevations and the herdsmen live in campsites". Seat: SrcYak.
- S062 — https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872 — accessed 2026-10-21 via Wayback 20260103060250 (live page CAPTCHA) — Description, third sentence: "It is light enough for nomads to carry; flexible enough to fold and pack; and sturdy enough to be dismantled and reassembled." Seat: SrcUnescoGer.
- S063 — https://ich.unesco.org/en/RL/cultural-space-of-the-bedu-in-petra-and-wadi-rum-00122 — accessed 2026-10-21 — Description ¶2: "The Bedu communities inhabiting this area keep alive a traditional pastoral culture and related skills." Seat: SrcBedouin.
- S064 — https://etcsl.orinst.ox.ac.uk/section5/tr532.htm — accessed 2026-10-21 via Wayback 20260605210113 (host timed out) — lines 130–142: "Every night your count is made and your tally-stick put into the ground". Seat: SrcDumuzi.
- S065 — https://www.ahdictionary.com/word/indoeurop.html#IR084700 — accessed 2026-10-21 — entry *peku-, headword gloss: "Wealth, movable property. Oldest form *pek̑u‑, becoming *peku‑ in centum languages." Seat: SrcPeku.
- S066 — https://d-place.org/parameters/EA004 — accessed 2026-10-21 — variable Description: "Dependence on animal husbandry, relative to other subsistence activities." Seat: SrcPeku.
- S067 — https://www.nature.com/articles/s41586-021-04018-9 — accessed 2026-10-21 — Abstract: "modern domesticated breeds do not descend from the earliest domestic horse lineage associated with archaeological evidence of bridling, milking and corralling". Seat: ScoutCalibrationRegistry.
- S068 — https://doi.org/10.1093/af/vfaa065 — accessed 2026-10-21 (full text PMC8214430) — Introduction ¶1: "South American camelids are the only domesticated ungulates in the Americas, and the Andean region sustained the only pastoralist societies in the pre-Hispanic New World." Seat: SrcAndeanCamelids.
- S069 — https://ich.unesco.org/en/decisions/14.COM/10.B.2 — accessed 2026-10-21 — decision text, sentence 4: "Two broad types of transhumance can be distinguished: horizontal transhumance, in plain or plateau regions; and vertical transhumance, typically in mountain regions." Seat: SrcUnescoTranshumance.

## Status and used-by change log

New rows S048–S069 enter `mined` with `used-by` = `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`.
No existing row (S001–S047) changed `status`, `recheck` or `used-by` this round. The SOURCES
preamble pointer changed from `lessons/round-49.md` for S001–S043 to `lessons/round-49.md`
for S001–S047 and `lessons/round-50.md` for S048–S069 (S044–S047's Gate bullets already sat in
round-49.md, so the old pointer was stale).

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R50-M1 | inseparable claims passed by a vacuous counterfactual: a claim cited identifiers another claim created, and the leg tested bytes that survive the removal | `corpus/lessons/round-49-verifier-spotcheck.md#adjudication`; `reports/round-49/run-validation.py:264-274` (c_without_s reads only C's inline URLs) and `:276-305` (s_without_c strips C from used-by before the census) — `.ufo/waves/round-50/build/RevengerR49Runner.md` | none at the time (the legs were non-gating); now QUALITY criterion 7 | `tools/check-claim-separability.py` on the frozen fixture `reports/round-50/separability/r49-fixture.json`; shown able to fail: it exits 1 with the C→S and S→C findings on the round-49 bytes, and its selftest's inline-URL control exits 1 (receipt in `reports/round-50/validation.json`) |
| R50-M2 | declaration evidence command not reproducible: substring grep matched "sherd" for "herd" | `reports/round-50/claims.json` C before-check `pastoral-unowned` evidence_command; hit at `corpus/knowledge/culture-material/writing-media-surface-economy.md:3` (found by six seats) | the claims-freshness gate's word-mode probe (correct verdict) — the printed command is not executed by the gate | the entry's `gap filled` line records the word-bounded command (`grep -P '\b…'`) and names the non-owner hit; the filed declaration is not rewritten |
| R50-M3 | the round's first declaration repeated the r49 shape: C cited S-rows opened by an undeclared "frontier" unit | `reports/round-50/claims.json` `separability_contract`; `.ufo/waves/round-50/build/CriticFrontier.md`, `ReviewR50Separability.md`, `ReviewSourcesContract.md` | build-wave critics (author-lane) | `reports/round-50/separability/r50-manifest.json` lists `corpus/SOURCES.md` among C's lands; the checker runs on that manifest |

## Frontier

- Carried, not repaired: the README rev-1.9 `REVISION-ORPHAN` residual routed to "r50 Ca" by `round-49.md`; this round's Ca is the separability control, so the residual stays a warning (`tools/check-readme-revisions.py` default run: findings 0, warnings 1).
- Carried: `hunting-foraging-subsistence.md` still cites superseded S034/S038/S039 rather than S044–S046 (`.ufo/waves/round-50/build/ReviewSourcesContract.md` F7) — a logged repoint for a later round.
- Carried: eight round-49 mined rows are cited by source name, not by S-id (ReviewSourcesContract F6); census cannot see it.
- Leads (opened this round, not registered): listed in `corpus/SOURCES.md` `## Search log`, round-50 note.
