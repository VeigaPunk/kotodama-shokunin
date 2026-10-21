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
- S070 — https://api.crossref.org/works/10.1007/s11069-017-3128-4 — accessed 2026-10-21 by the replacement L1 (KotodamaR50-2) after falsify seat ReopenS060 found S060's page range wrong — `message.page`: "165-181" (volume "92", issue "S1"). Supersedes S060's bibliographic pages only.

## Status and used-by change log

New rows S048–S069 enter `mined` with `used-by` = `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`.
Falsify-wave addition (post-landing, same round): S070 enters `queued` with `used-by` `—`; its `teaches` opens `supersedes S060 —`. S060 itself is unchanged in place (status `mined`, recheck `365d`, used-by the entry). The SOURCES preamble pointer changed `S048–S069` → `S048–S070`.
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

## Falsify wave (post-landing, 2026-10-21)

Round 50's coordinator ChousaR27R2 died with the host session (SIGHUP 13:10:51 -03) after landing the build wave at `1c779e4` and validating — but never spawning — a 66-seat falsify wave (attempt 1 refused by the job cap). The replacement L1 (KotodamaR50-2) dispatched that validated payload unchanged at 13:32:27 (`.ufo/waves/round-50/falsify-attempts.json`); seat reports are in `.ufo/waves/round-50/falsify/`. Fixes applied from their findings, all inside the claims' own lands:

- C entry (`culture-material/pastoralism-animal-husbandry.md`): scope transfers repaired (Swedish Sámi earmark, S059; WoDaaBe dated 1996–97, S058; Maasai marked `(to-verify)`; S048's two-to-four species scoped to Mongolia and northern Sudan); unsupported cells marked `(to-verify)` (cattle water, camel deserts, reindeer pasture, caravans, mobile empire, camelid fibre/meat) or removed ("and disease" in §11 step 5; "emic" for S060; species-mix hedge → herd splitting); Botai coded R for modern horses (matching §13 and S067); Sherratt quote attributed to the S051 review and linked to `agrarian-field-system-lexicon.md:80`; anchors corrected (cuisine `:81,:152`, transport `:92`, textile `:22`, semantic-fields `:70`, turkic-steppe `:194` wording); §2 gains animal-symbolism and shepherd-king rows so the head's "cited one-way in §2" and §15's "(§2)" are true; §12 now exercises water/dung, labour ceiling and a taboo with its rite. Seats: ReviewHead, ReviewSec01/04/08/09/11/12/13, CriticGapPremise2, ReopenS048/49/50/58/59/60/68.
- C entry, second pass: §3 gains an H/`(to-verify)` calibration line, Mongolia-scoped S060/S062 cells and a marked semi-nomadic interpolation; the political second axis is marked the lane's reading of a tier-B description (ReviewSec03); Sherratt is R as one horizon and C as a thesis, the review's words are no longer put in his mouth, "staged" → "idiosyncratic" per S051, castration marked `(to-verify)`, and §14 lists Sherratt 1981 as unopened (ReviewSec06).
- C entry, §7 (ReviewSec07): the raid rule's empty "(§9)" pointer and "and people" are gone; bridewealth anchored to `animal-symbolism.md:73`; a gift row now delivers what §1 and §11 route to §7; risk, loan-offspring and raid motives marked `(to-verify)`. Carried: no §13 bank rows for transfers; FAO chapter `x5439e03.htm` and Goody & Tambiah, read by the build seat, remain unregistered leads. Runner (ReviewRunner F4/F5): renumbering criterion 7, moving the README row or growing the entry past 250 lines would still pass the runner; control retention is checked by exit code only — carried.
- O: `tools/harness/receipt_guard.py` — a symbolic ref under `refs/heads`/`refs/remotes` whose target lies outside them now fails closed (was exit 0 for `origin/main → refs/tags/v1`; SentinelGuardFailOpen, ReviewGuardCode F1); HEAD at jj's `refs/jj/root` is treated as no commit instead of aborting (ScoutJjLive). Two selftest controls added (69 → 71); each fails (70/71) with its fix reverted. Probe `reports/round-50/jj-colocation-probe.py` v3: R1 now requires `landed_sha` to equal the `origin/main` tip and a refusal, over a receipt-free base (CriticProbeV2, CriticMeasurementAll, ScoutOCount); base tools 3/3, landed and post-falsify tools 0/3, fakes `landed_sha=<HEAD^>` and `<root>` 1/3 (`reports/round-50/telemetry/jj-probe-v3.txt`).
- O: `tools/check-readme-revisions.py` — `_git_run` sets `GIT_CEILING_DIRECTORIES` to the lane's parent, so a git-free lane nested inside another repository no longer borrows that repository's pin (ReviewReadmeRevCode Finding A): such a nested lane's `--selftest` exited 0 on the landed bytes and exits 2 now; the full-clone selftest stays 15/15, exit 0.
- Receipt: `reports/round-50/run-validation.py`'s word-bounded topic regex (written 13:04, one minute after the build commit, never committed by the dead coordinator) lands with the receipt it produced.

### Corrections to the Mistakes rows above (append-only)

- R50-M1: on the r49 fixture the checker reports **6** findings (5 dependencies + 1 overlap), not only C→S and S→C; two of them (`C->Ca` via `corpus/README.md:18`, `S->Ca` via `corpus/lessons/round-49.md:12`) are prose mentions in shared files, and the "independent" prediction came from the same seat and contract as the fixture (CriticIndependence, ReviewSepTool F7).
- R50-M2: the command reproduces; it misfires on "sherd" (class: substring evidence command). Eleven build reports mention the hit. The landed acceptance runner carried the same unbounded regex — see R50-M4.
- R50-M3: `reports/round-50/claims.json` still lists C's lands without `corpus/SOURCES.md`; the declaration and `separability/r50-manifest.json` disagree (ConnectSiblingCa, CriticR50Manifest).

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R50-M4 | receipt produced by uncommitted runner bytes: the landed `run-validation.py` exits 1 on C's before-check ("sherd"), and the passing `validation.json` came from a working-tree edit | falsify reports CriticCoverageCount, CriticMeasurementAll, ScoutCensusAfter, CriticMistakes | falsify wave (non-author seats); no landing gate compares a receipt's producer with committed bytes | runner edit and receipt land together; shown able to fail: the landed runner, rerun on clean clones of `4ad2683`/`1c779e4`, exits 1 |
| R50-M5 | counting probe's predicate changed after a measurement: v1 scored the landed tools 1/3, v2 relaxed R1 to "ancestor of origin/main" and scored 0/3; v2 also passed fakes | `reports/round-50/telemetry/jj-probe-v1.txt`, `-v2.txt`; CriticProbeV2, CriticMeasurementAll | falsify wave; none at measurement time | probe v3 (tip equality + refusal); shown able to fail: fakes `landed_sha=<HEAD^>`/`<root>` score 1/3 (`telemetry/jj-probe-v3.txt`) |
| R50-M6 | separability zero depends on path spelling: C's Gate lives in this lesson (REC), cited as bare `lessons/round-50.md`; writing `corpus/lessons/round-50.md` flips `r50-manifest.json` to `C->REC`, exit 1; Ca's declared leg "run on `claims.json` exits 0" exits 2 (`SEPARABILITY_INPUT_ERROR manifest is missing base, schema`) | CriticR50Manifest, ReviewSepTool F1, ScoutCaCount, ConnectSiblingCa, ReviewCriterion7 S3 | falsify wave; the checker matches whole paths only (`tools/check-claim-separability.py:602`) | not repaired this round: reported as Ca's unmet leg; carried — resolve relative paths against the citing file, and declare the round lesson's Gate as C's dependency |
| R50-M7 | replacement L1's retry loop fired 19 cap-refused dispatches in ~1 s (its sleep compared against a list that grew each pass) | `.ufo/waves/round-50/falsify-attempts.json` attempts 2–20 and the annotation record | none (unattended loop); the refusals spawned nothing | spaced retries recorded as attempts 21–22; loops key the sleep on the attempt counter, not a mutating list |
| R50-M8 | two falsify seats (SimplifySepTool, SimplifyGuard) wrote their reports under the fleet root's `.ufo/waves/round-50/falsify/` despite the absolute-path context | `git -C /home/vgpnk/Projects/shokunin status --porcelain` at sweep time | the round prompt's misroot sweep | copied byte-exact into the lane, `cmp` verified, fleet copies removed |
| R50-M9 | lessons index not reconciled: `corpus/lessons/README.md` did not index `round-49-verifier-spotcheck.md` or this lesson; the build wave's revision-5 diff carried fixture pins and never landed (audit `findings: 3` at `1c779e4`) | ScoutLessonsIndex, ReviewCriterion7 | `reports/round-25/audit/c31-lessons-index-audit.py` (not on round 50's acceptance surface) | lessons README revision 5 with measured pins; audit re-run to `findings: 0` |

### Carried (falsify findings not repaired this round)

- SOURCES locator errata (rows are append-only; no claim rests on the slips): S050 anchor "¶3" is prose ¶4 (ReopenS050); S052 "printed page = PDF − 24" holds only near p. 19 (plates shift it to −30) and §VIII runs to p. 47 (ReopenS052); S054's quote is the second paragraph and the printed heading has no "The" (ReopenS054); S064's lines 130–142 close Grain's **second** speech (ReopenS064); S053's "unreachable on every route" should read "unopened this round"; the Gate's S066 seat is SrcPeku's companion run, not a separate seat.
- Checker gaps (ReviewSepTool, ReviewCriterion7, ConnectSiblingCa, MutateSepTool): no lands-provenance check (93 changed paths owned by no unit); acceptance never run base-only (O's manifest acceptance exits 0 on base bytes); acceptance that rewrites another claim's bytes still counts as verified; `r49_matches` drops counts and locations. QUALITY criterion 7 states more than the tool enforces.
- Guard and gate coverage (MutateGuard, MutateReadmeRev, ConnectSiblingGuard): three guard mutants and four `check-readme-revisions` mutants survive the selftests; `landed_*` names the alphabetically first remote holder, not `origin/<branch>`; `refs/tags/*` is unprobed; `reports/round-14/guard/design.md` still states the HEAD-only contract.
- README sweep (`reports/round-28/readme/sweep.py`) passes a duplicated or out-of-order row (ReviewReadmeRow S2).

### Final review reconciliation (same round)

- ReviewSec02: the cuisine/textile/transport anchor repairs already landed;
  the last pass also removes a duplicate claim to the agrarian calendar,
  hands feed vocabulary back to transport, and preserves the hunt owner's
  `(to-verify)` on meat-for-crops. Residual: the commissioned ≥15-row
  boundary-table target was not met (11 rows); it is not silently lowered.
- ReviewSec05: §5 no longer infers lineage ownership from S059 or a
  livestock→wealth direction from the S065 gloss; the Nuer quotation is
  completed, and the morphology proposal is explicitly a design heuristic.
  S065's original teaches wording remains a disclosed registry correction debt.
- ReviewSec10: surplus-male sacrifice is marked `(to-verify)`, the design frame
  is H, and “milk and river” is corrected to “milky/river”. Additional ritual
  neighbours and the shepherd-king administration boundary remain unexpanded.
- ReviewSepFixture confirms the headline C→S detection but finds the r49
  export range misses S001–S030 and shared-land exclusions are not implemented.
  The six-pair expected file is a same-contract fixture prediction, not an
  independent semantic authority. These are calibration limits, not a pass.
- ReviewLessonGate re-opened all 22 quotes successfully. S058's work-root URL
  is front matter; its quote is on the explicitly named `y5115e08.htm` chapter.
  Its route locator and the other locator errata above remain recorded.
- R50-M4 wording correction: a dispatched reviewer is still author-lane
  evidence, not a non-author promotion verifier. Fresh closure remains external.
- Process disclosure: the replacement loaded the shokunin/swarm bindings and
  required jj trial/audit after dispatch rather than in the required load order.
  The retry burst is also nonconformant; neither defect is repaired by later reads
  or by the eventual successful dispatch. No tool was installed or upgraded.

- ReviewSourcesConformance: S070 is landed at `c8865c7` and corrects S060's
  pages/aggregate wording without altering S060. Additional source-locator,
  archive-access and route errata remain as above. The round-50 search-log note
  lacks identified/screened/excluded counts and a stop rationale; the build's
  unregistered opened-source list is not reconstructed as an invented census.
  This is a frontier conformance defect, not a clean search-log verdict.
- All 73 build and 66 falsify seats have durable reports (139 dispatched,
  zero report-less/dead seats). The predecessor's earlier chousa seats are
  excluded using the kotodama build-assignment receipt. Refused calls spawned none.

