# RevLoreHandoff — round 67, adjacency check on the medicine entry's lore handoff

- seat: RevLoreHandoff (independent leaf, no subagent dispatch)
- judged on: adjacency, coverage · milestone r67-v2
- base: `ad5b52b0ab5691358cd38718ab75649dc9916f9a`; lane tip read at `b78f8b8e` (jj `@` `406440ae`, empty); lane tree read-only
- objects read: `reports/round-67/claims.json` (claim C + `review_only`), `reports/round-67/accept-c.py`, `accept-ca.py`, `accept-o.py`, `.ufo/waves/round-67/spec-v2.json` (items 15, 26, 40 and the twelve ScoutRow briefs), `corpus/knowledge/synthesis/worldbible-integration-contract.md` (sha256 `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`), `.ufo/waves/round-67/rows/ScoutRow11/row-S825.txt`, `row-S826.txt`, `ScoutRow11/rejects.txt`, `rows/ScoutGapMed/gap.md`, `.ufo/waves/round-67/stage/gate-rows.md`, `stage/readme-row.txt`, the models `culture-material/games-play-sport-contests.md` (§13 `:108`, §14 `:122`, contract path `:124`), `scent-perfume-aromatics-codes.md` (`:31`, `:50`), `bathing-and-body-hygiene.md` (`:3`, `:27`, `:83`, `:93`, `:98`, `:121`, `:142`), and the measured owner entries in §HIGH-2/§HIGH-3 below; lore side: `lore-shokunin/PROVINCE.md:9`, `lore-shokunin/corpus/README.md:73,79,94`, `lore-shokunin/corpus/knowledge/r103-canon-status-and-supersession.md:6`; chousa side: `chousa-shokunin/tools/quote-reopen.py:1-60`, `research-gate.sh:1-40`, `argv-witness.py:1-35`, `mechanism-witness.py:1-35`
- review kind: **prose/contract review — no language server answers Markdown**, so every check is textual against the cited files and lines; no LSP `references`/`definition`/`diagnostics` claim is made for any of them, and none is presented as semantic proof. Row-fragment and census checks are literal greps, labelled as such.

## Verdict

**Not certifiable this run — and the instrument set still cannot see the property under review.**

The entry `corpus/knowledge/culture-material/medicine-healing-codes.md` does not exist at review time (`ls …/medicine-healing-codes.md` → No such file), and `.ufo/waves/round-67/stage/entry-spec.md` had not landed either (stage held `mut-c`, `mut-entry`, `mut-o`, `quality-c19.md`, `readme-row.txt`, `scorecard-r66.md`, `gate-rows.md`, `lesson-draft.md`, `log-r66.md`). Two row fragments exist (`S825`, `S826`). So I can certify no handoff bytes; what I can establish, and do below, is that the wave **brief now requires both sections** (r66's HIGH-1 is closed at brief level), that **no frozen leg or receipt can see them** (so a canon-claiming or rights-claiming sentence passes 12/12), that the brief's **four-owner list is three owners short of the rows actually inside the register**, and that the strictest constraints on the entry's prose are *mechanical* (the `(S###)` citation regex and the H2/line caps), which the L1 must know before writing a word.

The medicine register is a harder adjacency case than scent: it contains **deity material** (S825 incubation/Asclepius), **living-tradition material under explicit community restriction** (S817 medicine lodge/sweat lodge, S824 sangoma/nganga), and **translated classical medical texts** whose modern translations and museum images carry real-world rights (S805, S808, S811, S816). The one-way split is therefore not one split but two: **deity/canon → lore-shokunin**; **rights/permission → operator** (contract `:167`; lore refuses rights claims at `PROVINCE.md:9`). An entry that routes both to lore is wrong in the second case even if it sounds humble.

## Findings

### HIGH-1 — The brief now requires the two sections; nothing else in the round does

`.ufo/waves/round-67/spec-v2.json` item 15 (`ScribeEntrySpec`) reads verbatim: "…a **Boundaries section one-way pointing to partial owners** (bathing-and-body-hygiene, scent-perfume-aromatics, myth-symbol purity, funerary), **a lore handoff section (one-way, never canon)**, and a bullet template row S### -> clause." That closes r66's HIGH-1 (no seat authored a handoff) structurally. It does not close it instrumentally:

- `reports/round-67/accept-c.py` has twelve legs — STAMP, FILE, SET, ROWS, ONEID, RESTATE, HOSTS, LINK, APPEND, NOHARM, SWEEP, CAPTURE, TOPIC — and **zero occurrences of `canon|handoff|lore|rights|boundary|one-way`** (measured: `grep -niE 'canon|handoff|hand-off|adjacen|lore|world.bible|boundary|one-way|rights' reports/round-67/accept-c.py` → no matches). FILE (`:216-221`) counts H1/H2/H3/lines and the `- topic:` line; it never inspects a heading's *name*.
- `accept-ca.py` and `accept-o.py`: the same grep → **no matches**. No Ca records leg grades prose boundaries either.
- `claims.json` is honest about it: claim C `review_only` includes "lore handoff quality of the entry's handoff section" (`:42`). This seat is the only artifact that closes it.

Consequence: an entry sentence such as "incubation at the god's shrine cured the suppliant" or "the Canon of Medicine settled the doctrine" passes every leg. That is a contract breach at `:43` ("Sacred doctrine is not automatically world-fact") and `:102` ("Evidence strength and fictional truth are orthogonal"), invisible to the counters. Prior art in this fleet says exactly this about output equivalence: `chousa-shokunin/tools/mechanism-witness.py:1-20` records that "output equivalence cannot distinguish two engines that implement the same contract", and `argv-witness.py:1-25` records a global stamp threshold admitting a one-record shortcut. Twelve green legs are that stamp.

### HIGH-2 — The brief names four owners; the rows need at least sixteen

Measured one-way targets, by the row that lands on each. Form follows the lane's own model: `games-play-sport-contests.md:110-120` ("`path` owns X; this entry keeps Y as Z") and `myth-symbol/amulets-talismans-apotropaic-marks.md` §2 "One-owner boundary" table (`:22-30`).

| # | Owner, measured | Owns (evidence) | Row(s) inside the register | What the medicine entry keeps |
|---|---|---|---|---|
| 1 | `myth-symbol/amulets-talismans-apotropaic-marks.md` | the whole protective-object system, incl. **plague and illness as the danger answered**, how protection is said to work, materials/forms, who prescribes, renewal/suppression (`:3` topic; `:36-39` §3 senses, "disease" in the museum sense; §2 table `:22-30`) | **S828** medical amulets/charms | one object class inside a therapeutic regimen (a museum medical-collection object); **not** amulet typology, not "how protection works" |
| 2 | `myth-symbol/sacred-topography-pilgrimage.md` | site kind 6 "healing / incubation shrine", the *iamata* archive, votive/ex-voto economy (`:52`, `:77`, `:5`) | **S825** asklepieia/incubation | the therapeutic institution (regimen, staff, patient flow); **not** the shrine typology, route grammar or votive receipt |
| 3 | `myth-symbol/divination-omen-systems.md` | dream-oracle & incubation technique row ("Greek incubation at Asclepieia", `:89`), "Dream-sanctuary" institution (`:126`), the byproduct rule "medicine from incubation case archives" (`:135`) | **S825** | the medical case archive as a *medical* record; **not** incubation as divination technique |
| 4 | `myth-symbol/purity-pollution-boundary-systems.md` | miasma/pharmakos proximity carrier (`:58`), quarantines as boundary machinery (`:56`, `:61`, `:127`), the antisepsis trap (`:109`) and "discredited — hygienic reductionism" (`:140`) | **S813** plague costume, **S820** quarantine, **S827** plague treatises | disease as belief-classified; **not** the status-pollution system nor its leaks |
| 5 | `culture-material/bathing-and-body-hygiene.md` | the **sweat-lodge family** as one of five bathing regimes (`:3`, `:27`), and the restricted/permission-bound rule (`:93`, `:98`, `:142`) | **S817** medicine lodge / sweat-lodge therapy | the therapeutic claim as attributed practice; **not** the bath sequence, not the restricted ceremony |
| 6 | `culture-material/scent-perfume-aromatics-codes.md` | pomander as plague prophylaxis (`:31`, S791) and the aromatics register (`:50` Boundaries) | **S813** plague-doctor costume | costume-as-prophylaxis *logic* only; **not** the aromatic materia, not "disinfects the air" as fact |
| 7 | `culture-material/funerary-material-culture.md` | Egyptian embalming/natron and the artificial-preservation row (`:21`, `:64`), anti-pastiche guard (`:184`) | **S811** medical papyri (Ebers/Smith), **S819** anatomy | the text as medical evidence; **not** mortuary technique or the disposal/assemblage/monument/word machines |
| 8 | `culture-material/writing-media-surface-economy.md` | papyrus/parchment as priced media (`:47`), Pliny NH 13 at book level (`:15`) | **S811**, **S827** consilia | the treatise/recipe genre; **not** the surface economy or roll construction |
| 9 | `culture-material/craft-artisan-lexicon.md` | guild/non-guild ladder models incl. Roman *collegia* (`:63`) | **S818** apothecary guild regulation, **S823** barber-surgeon guilds | the *medical* licence/regulation content; **not** the workshop speech community or the ladder typology |
| 10 | `culture-material/trade-economy-lexicon.md` | guild and trade-association terms (`:3`), the *ḥisba* market inspectorate (`:43`), price/measure vocabulary | **S818**, **S810** supply, **S822** bimaristan endowment | drug/ingredient trade only as a *supply fact*; **not** measure→money→number or the inspectorate |
| 11 | `culture-material/architecture-settlement-lexicon.md` | built-environment vocabulary incl. sacred buildings and city planning (`:2`) | **S820** lazaretto, **S822** bimaristan, **S809** infirmary | the hospital as an *institution* inside those forms — the phrasing precedent is `bathing-and-body-hygiene.md:7` ("the bath is a building run … this entry owns the water-and-body institution inside those forms") |
| 12 | `culture-material/masks-masquerade.md` | mask typology and the restricted-tradition policy (`:42`, `:69`; Science Museum "Asian Medicine" re-classification `:106`) | **S813** beaked costume | the *suit* as prophylaxis equipment; **not** the mask as a sign system, no construction detail |
| 13 | `culture-material/ritual-garments.md` | the bulla as a doffed amulet (`:118`); garment sensory/wearer rules | **S828**, **S813** | nothing — cite for the worn-object rule only |
| 14 | `civilizations/haudenosaunee.md` + `civilizations/lakota-plains.md` + `civilizations/algonquian.md` | community-authored restriction on medicine masks and medicine societies (`haudenosaunee.md:133,137-142`); rejection of the "generic pan-Indigenous shaman"/medicine-wheel decoder (`lakota-plains.md:115,210`); Mide'wiwin ethnography is "colonial ethnography, not a contemporary authorization manual" (`algonquian.md:25`) | **S817**, **S824**, **S828** | names the public boundary and stops; **no** ritual sequence, no "shaman" as a generic role, no medicine-society reconstruction |
| 15 | `culture-material/cuisine-food-lexicon.md` | food/dietary-law system; "restorative broth" history (`:120`) | humoral dietetics in **S805/S812** | regimen as *medical* prescription; **not** the meal grammar or dietary-law case studies |
| 16 | `myth-symbol/number-symbolism.md` | *quarantena* as a sacred-adjacent number escaping into public health law (`:90`) | **S820** | the institution's practice; **not** the number doctrine |

The brief's four (bathing, scent, purity, funerary) cover rows 5, 6, 4, 7 only. Rows **S828, S825, S817, S824, S813, S818, S823, S811** would be written as if the medicine entry owned them. Ten bullets is in-norm (the model lists nine; the amulets entry's own table lists nine).

### HIGH-3 — Deity/canon: which sentences must be one-way, and to whom

Contract clauses that bind the payload (all measured at `5f4c02bf`):

- `:43` "Sacred doctrine is not automatically world-fact"; `:96` claim-kind enum incl. "attributed in-world belief"; `:100` "otherwise `not canonized`"; `:102` invented-and-accepted vs attested-and-not-canonized are orthogonal; `:105` etic framework ≠ emic self-description.
- `:167` rights/restricted knowledge → **Operator**, "a bibliography is not permission"; `:178` "Do not claim consultation or consent that did not occur".
- `:180`-region: a contested or discredited claim must be named **as a claim with its critique** before export.

Rows carrying explicit canon claims that must be phrased as belief/attribution, never as world-fact:

| Row | Subject | The canon claim it carries | One-way target |
|---|---|---|---|
| S825 | asklepieia, incubation | the god heals in sleep; the *iamata* are divine cures | lore (pantheon, whether the cure is real); divination `:89/:126/:135` owns the technique |
| S805, S812 | Hippocratic corpus, humoral canon, Galen | four humours as cosmology; disease as imbalance | lore (whether the world's medicine is true); purity `:109` owns the pollution/hygiene separation |
| S806 | Charaka, doshas | tridoṣa as metaphysical physiology | lore (canon standing); the entry states the theory as the tradition's model |
| S807, S826 | Huangdi Neijing, qi, meridians; moxa transmission | qi/meridian metaphysics; canonical text status | lore; and keep S807/S826 from double-writing TCM history |
| S808 | Ibn Sina, Canon | the Canon as authoritative synthesis | lore (canon standing of the text *in-world*) |
| S814 | Paracelsus, iatrochemistry | alchemical cosmology, signatures | lore |
| S816 | Four Tantras (Gyushi) | Buddhist medical canon | lore; and rights (§MED-4) — living canon, not a public-domain prop |
| S817, S824 | medicine lodge; sangoma/nganga | ancestral/initiatory agency, divination-based diagnosis | lore; and the restriction route below — **not** lore's to license |
| S815 | Badianus / curanderismo | colonial-era compilation of Nahua practice | lore; mark the colonial filter (`:176`-region) |
| S820, S827 | lazaretto/quarantine; plague consilia | plague as providence vs contagion; advice literature's authority | lore |
| S828 | medical amulets | efficacy of the charm | lore; amulets entry owns the mechanism vocabulary |

Required handoff strings (the model's, verbatim or equivalent, measured at `games-play-sport-contests.md:122-126`): "This entry supplies sourced anchors and conditional design questions; **it makes no canon decision**." · "**Those are canon choices for lore-shokunin, recorded and verified in the world bible, not here.**" · "contested scope goes to the integrator." The handoff must also say which rows are belief-classified and that the entry does not adjudicate efficacy (S825, S828, S813, S817, S824).

### MED-4 — Real-world rights on medical texts: a second, different one-way (to the operator, not to lore)

The register cites **translations and museum objects**, which is where rights actually attach:

- **Translations are separate works.** Hippocratic and Galen texts are cited through the Loeb/Perseus tradition; Ibn Sina through Latin/Arabic editions; the Gyushi through modern translations. Contract `:180`-region requires "translation/editor" per source — the entry may quote only the short anchor phrase its registry row's quote cell carries, and must not extend a copyrighted translation. The fleet's measured bound is `chousa-shokunin/tools/quote-reopen.py:55` `MAX_WORDS = 25`, with the verdict order NO_SOURCE/TOO_LONG/UNREACHABLE/VERBATIM (`:1-30`); `accept-c.py` RESTATE (`:292-322`) independently keeps entry bullets to a paraphrase carrying ≥3 in-order quote words, so the two bounds agree by construction.
- **Museum images and facsimiles** (Ebers papyrus, Edwin Smith papyrus, Badianus/Codex Barberini, Wellcome object pages) are object-rights decisions, not prose decisions. The entry describes objects; it does not reproduce plates, and it does not treat an open-access listing as a reuse licence.
- **Living-tradition knowledge**: Ayurveda/TCM/Kampo (classical, but biopiracy history attaches to materia medica), and specifically **restricted ceremonial knowledge** — sweat lodge (`bathing-and-body-hygiene.md:98` already quotes the corpus rule from `civilizations/australia-aboriginal.md:136`: "stop at a consultation/permission request; do not produce a speculative substitute labelled authentic"), medicine societies (`civilizations/haudenosaunee.md:137-142`), sangoma/nganga initiation. A bibliography is not permission (`:167`).
- **No consultation or consent may be claimed** (`:178`). The handoff must say so explicitly; the word "consulted"/"with permission" must not appear.
- **No medical advice.** The entry is a design reference for fictional cultures. It must not present dosing, treatment indications, or efficacy as guidance for the reader — the model's header discipline (`scent…:3` "- topic: … a sourced design reference for fictional scent cultures, not a universal history") is the form; for medicine the disclaimer is load-bearing, because several rows describe *discredited* prophylaxis (miasma, S813) and *contested* efficacy (S828).

**Route split, stated once in the handoff:** canon → `lore-shokunin` (world bible, `worldbible-integration-contract.md`; contested scope → integrator); rights/restricted knowledge/publication permission → **operator** via contract `:167`; research-method gaps → chousa (contract `:170`-region row "Evidence retrieval methodology is the actual task"). Lore's own province refuses the rights question outright: `lore-shokunin/PROVINCE.md:9` — "Refuses: … real-world rights claims".

### MED-5 — Mechanical traps that decide whether a *correct* handoff even survives the counter

These are measured from `accept-c.py` and must shape the prose before it is written:

1. **`(S###)` citations are global and exclusive.** `:282` `cited = re.findall(r"\((S\d{3,})\)", text)`; `:287` any id outside S805–S828 is `foreign` → ONEID FAIL. Therefore the Boundaries/Handoff sections **must contain no registry ids at all** — not S791 (scent's pomander), not S801–S804 (rejected rows), not "see S753". The regex requires parentheses, so a bare `S791` would be **invisible** to the counter: do not write bare foreign ids either, and reviewers should grep for them (recipe below). Each of the 24 ids must appear **exactly once**, inside its own bullet (`:300` `bullets = entry_bullets.get(sid, [])`, `len(bullets) != 1` fails).
2. **A second mention in a boundary bullet breaks it.** "…unlike the scent register (S791)" → `citations=2` for that id or a foreign id; either way FAIL.
3. **Budget:** FILE (`:216-221`) allows 1 H1, **≤16 H2**, **0 H3**, ≤250 lines. Two handoff H2s + 12 content H2s = 14, leaving two slots; do **not** plan 14 content sections. Boundary bullets must be plain list items (an H3 "§12.1" fails FILE).
4. **NOHARM (`:377-384`)** allows exactly `{ENTRY}` under `corpus/knowledge`. No companion handoff file, no reciprocal edit to any owner. The handoff must live **inside** the entry.
5. **TOPIC** requires the entry's first `- topic:` physical line verbatim inside the README row; a topic line that grows a "not medical advice" clause changes the README row too (see `stage/readme-row.txt` for the row grammar; `sweep.py` compares by equality).
6. **S801–S804 are rejected rows**: `EXTRA_IDS` (`:52`) exist for APPEND only. The lesson/gate prose carries their reasons (`stage/gate-rows.md` already does); the entry must not cite them.

### MED-5b — Cross-cutting: per-claim lands separation is load-bearing for the rejected rows (L1 ruling, verified here)

`CriticFrontier` flagged that C and Ca look jointly unsatisfiable: `accept-c.py` APPEND (`:350-377`) bounds the added set to `NEW_IDS ∪ EXTRA_IDS` = S805–S828 + S801–S804, while `accept-ca.py` D4 (`:207-239`) needs `len(R66_REJECTS)+2 = 6` rows with `status=rejected` and date `2026-10-24`. The L1's ruling — a C lands commit `A_c` and a later Ca lands commit `A_ca` — is mechanically sound and I verified the three facts it depends on:

- both counters read the registry from their own `--root` (`accept-c.py`/`accept-ca.py` `read(root, REGISTRY)`; `accept-ca.py:159`), so each sees its own lands tree, not the live worktree;
- at `A_c` the append set over base `ad5b52b0` is exactly S801–S804 (already landed at `A_r`) + S805–S828 → APPEND passes; `A_ca` also adds S829+ (reject rows), which is why **C must not be stamped at `A_ca` and S829+ must not exist at `A_c`**;
- `accept-ca.py` has **no** `APPEND`/`NEW_IDS` bound at all (grep → no matches), so the reject ids do not trip Ca; D4's count at `A_ca` is 4 (S801–S804, dated `2026-10-24` per `stage/gate-rows.md`) + the new rejects ≥ 2 → ≥ 6, which clears the threshold.

Residual for the L1: the four r66 rows must keep the `2026-10-24` date cell at `A_ca` (the draft does), and the Ca lesson leg (`accept-ca.py:42`-region) needs ≥20 of S805–S828 named at `A_ca`. If integration collapses to one commit and stamps C there, APPEND prints `extra=[S829…]` — a predictable, not mysterious, FAIL.

### MED-6 — The scent entry is *not* the model, and r66 scored it anyway

Measured on the recipe below: `scent-perfume-aromatics-codes.md` → sections matching `Boundaries|Handoff` = **1** (only `## Boundaries` at `:50`), `one-way` = **0**, contract path = **0**, "makes no canon decision" = **0**; yet r66's verifier scored adjacency "unchanged" and accepted the round. The model that satisfies the recipe is `games-play-sport-contests.md`: sections = **2** (§13 `:108`, §14 `:122`), `one-way` = **1**, contract path = **1** (`:124`), disclaimer = **1**, false-stamp hits = **0**. If the L1 copies scent's one-paragraph Boundaries, r67's handoff is absent while every leg stays green — the exact r66 failure repeated under a better brief.

### LOW-7 — Lore's side moved since r66; the handoff must not import the new surface

- CM-g (kotodama packet intake) is **still uncovered**: `cd lore-shokunin && git grep -l 'kotodama-lore-adjacency' -- corpus/knowledge SKILL.md` → **exit 1**; `corpus/README.md:73` records "uncovered … no acknowledgement record"; `:79` "zero durable-surface acknowledgement records". So: cite the contract **by path only**, no digest, no packet id, no receipt; never write "accepted", "read by lore", "canonized".
- CM-e (canon tiers, retcons, supersession) is now **governed-method** at `lore-shokunin/corpus/knowledge/r103-canon-status-and-supersession.md:6`. The handoff may **name** that file as lore's own surface (read-only) but must not restate its decision table or claim the medicine entry's status under it. Simpler and safer: contract path only.

### LOW-8 — Row-fragment evidence already shows the S825 collision

`rows/ScoutRow11/row-S825.txt` anchor: "Iamata stelae stood exposed inside the abaton, advertising dream incubation to new suppliants." The register therefore owns a *shrine archive* topic, not a therapeutic-technique topic; the bullet must be the institution/practice side and the Boundaries bullet #2/#3 above are mandatory, not advisory. `row-S826.txt` ("Chiso's sixth-century import seeded Japan's distinct lineages of needle and moxa practice") is internal-partition pressure with S807 — keep S807 on the canon/foundations side and S826 on transmission, without writing TCM history twice.

### LOW-9 — Reciprocity is out of reach (residual, not a defect)

NOHARM forbids touching owners, so this entry will point at sixteen and none will point back. Record it as residual; do not simulate a reciprocal bullet.

## Required text (build obligation for the L1)

Two H2 sections inside the 16-H2 / 250-line budget, modelled on `games-play-sport-contests.md:108-126` and the amulets entry's one-owner table (`amulets-talismans-apotropaic-marks.md:22-30`).

**`## Boundaries` (or `## Adjacent topics`) — opening line, model verbatim:** "This entry points to the following entries for adjacent scope. The pointing is one-way: they own their topic, and this entry does not restate or extend them." Then one bullet per owner from HIGH-2 (16 targets; 12–16 bullets acceptable, no registry ids). **The `(S###)` marks below are L1 annotations saying which row motivates the bullet; strip every one of them from the entry's Boundaries text** — a single surviving mark is a second citation and fails ONEID/RESTATE (§MED-5):

1. `myth-symbol/amulets-talismans-apotropaic-marks.md` owns protective objects and their claimed mechanisms; this entry keeps a medical-collection object inside a regimen (S828), not amulet typology.
2. `myth-symbol/sacred-topography-pilgrimage.md` owns the healing/incubation shrine and the votive economy; this entry keeps the therapeutic institution (S825).
3. `myth-symbol/divination-omen-systems.md` owns incubation as a divination technique and the dream-sanctuary; this entry keeps the medical case archive.
4. `myth-symbol/purity-pollution-boundary-systems.md` owns miasma/status pollution and its traps; plague material here is belief-classified (S813, S820, S827).
5. `culture-material/bathing-and-body-hygiene.md` owns the sweat-lodge family and the permission boundary; this entry names the therapeutic claim only (S817).
6. `culture-material/scent-perfume-aromatics-codes.md` owns the aromatic materia and the pomander; costume prophylaxis is cited here as logic, never as mechanism (S813).
7. `culture-material/funerary-material-culture.md` owns embalming and mortuary technique; the medical papyri are cited as medical evidence only (S811).
8. `culture-material/writing-media-surface-economy.md` owns the media economy; the treatise/recipe genre is kept here (S811, S827).
9. `culture-material/craft-artisan-lexicon.md` owns guild and workshop typology; licensing/regulation content stays here (S818, S823).
10. `culture-material/trade-economy-lexicon.md` owns measure/money/market vocabulary; drug supply is a cited fact here (S810, S818, S822).
11. `culture-material/architecture-settlement-lexicon.md` owns the built forms; the hospital is an institution inside them, on the bathing-entry precedent (`bathing-and-body-hygiene.md:7`) (S809, S820, S822).
12. `culture-material/masks-masquerade.md` owns the mask as sign and its restricted-tradition policy; the beaked suit is prophylaxis equipment here, no construction detail (S813).
13. `culture-material/ritual-garments.md` owns garment rules including the doffed bulla (`:118`); a worn protective object is cited here for its medical-context use only (S828, S813).
14. `culture-material/cuisine-food-lexicon.md` owns food and dietary law; regimen is a medical prescription here (S805, S812).
15. `myth-symbol/number-symbolism.md` owns the *quarantena* number doctrine; the institution's practice stays here (S820).
16. `civilizations/haudenosaunee.md`, `civilizations/lakota-plains.md`, `civilizations/algonquian.md` hold the public boundary on medicine masks/societies and reject the generic shaman frame; this entry stops at the published boundary (S817, S824, S828).

**`## Handoff to the world bible` — must contain, checkable as strings:**

- recipient `lore-shokunin`, owner of the world bible and its consistency verification under `corpus/knowledge/synthesis/worldbible-integration-contract.md`, **path only**; "contested scope goes to the integrator."
- the model's disclaimer, verbatim or equivalent: "**it makes no canon decision**" / "**Those are canon choices for lore-shokunin, recorded and verified in the world bible, not here.**"
- the **route split**: canon → lore; **rights, restricted cultural knowledge, publication permission → operator** (contract `:167`); method gaps → chousa.
- **Decisions this entry deliberately does not make** — medicine-specific, one sentence each: (a) whether a shrine cure, charm or regimen *works* (S825, S828, S813); (b) whether a tradition's physiology (humours, doshas, qi, iatrochemical signatures) is true rather than attributed (S805, S806, S807, S814); (c) the canon standing of a classical text (S808, S816) and whether a rite is sacred or secular; (d) who may practise, be licensed, or be treated, and the enforcement (S818, S823); (e) dates and era bounds of each practice (§3 Era row); (f) whether a text's authority is prescriptive or descriptive (S827, `:44`-region); (g) colonial, missionary and outsider filters on the record (S811, S815, `:176`-region); (h) whether any living practice may be borrowed at all (S817, S824 — operator, not lore).
- **Evidence-and-rights paragraph**: each bullet scoped to its cited row; translations carry translator/edition in the registry row, never extended in the entry; museum listings are not reuse licences; `(to-verify)` stays a backlog mark; **no consultation or consent is claimed**; restricted material is named and not described.
- **Status line**: this is a draft handoff; bilateral read is **pending**, no receipt exists, nothing here is `canonized`. No packet, envelope or receipt may be named.
- **No medical-advice sentence**, e.g. "This entry is a design reference for fictional medical cultures; it is not medical guidance and states no treatment."

## Verification recipe for the landed draft (run once, before commit)

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
E=corpus/knowledge/culture-material/medicine-healing-codes.md
grep -cE '^## .*(Boundaries|Adjacent|Handoff|handoff|adjacent)' "$E"        # expect 2
grep -c 'one-way' "$E"                                                      # expect >=2
grep -c 'worldbible-integration-contract' "$E"                              # expect exactly 1
grep -cE 'makes no canon decision|no canon decision' "$E"                   # expect 1
grep -c 'not canonized' "$E"                                                # expect 1  (r67-stricter than the model: see calibration)
grep -nE 'canonized|accepted by lore|approved by lore|has read|handoff accepted|bilateral (read )?(done|complete|acknowledged)' "$E"   # expect 0
grep -cE '\(S[0-9]{3,}\)' "$E"                                              # expect exactly 24
grep -oE '\(S[0-9]{3,}\)' "$E" | sort | uniq -d                             # expect empty (no id cited twice)
awk '/^## /{f=($0 ~ /(Boundaries|Adjacent|Handoff|handoff|adjacent)/)} f' "$E" | grep -nE 'S[0-9]{3,}'   # expect empty: no ids in handoff sections
grep -nE 'consulted|with permission|consent' "$E"                           # expect 0 (or an explicit negation only)
grep -niE 'miasma|prophyla|disinfect|efficacy|cures?' "$E"                  # each hit must be belief/marked-classified
grep -nE 'S81[378]|S825|S828' "$E"                                          # those bullets must defer to the named owner
python3 -B reports/round-67/accept-c.py --root . --lands <lands>            # 12 legs; unaffected by prose
```

Recipe calibration (measured this seat): `games-play-sport-contests.md` → sections 2, `one-way` 1, contract path 1, disclaimer 1, false-stamp 0, parenthesized ids 26. `scent-perfume-aromatics-codes.md` → 1 / 0 / 0 / 0, id count 22, i.e. **the recipe fires on the entry r66 accepted**, which is why it discriminates rather than decorates. One leg is deliberately stricter than both models: `not canonized` = 0 on games and on scent, and r67 requires it because the handoff is a draft with the bilateral read pending (contract `:15`, `:209`; lore `corpus/README.md:73,79`). Keep it, but read it as the one r67 addition rather than as model conformity — every other leg is calibrated on the accepted model. Caveat measured on `bathing-and-body-hygiene.md`: the word "receipt" appears in the idiom "contact receipt" (`:83`, `:121`), so a broad `receipt` grep false-fires — the recipe above deliberately omits the bare word and tests the phrases that would be false stamps. `grep -oE '\(S[0-9]{3,}\)' | wc -l` must count 24 for the new entry: the counter's regex is exactly this pattern (`accept-c.py:282`), so the recipe reads the same bytes the leg does.

## Residual risk and verification gaps

- **Primary gap:** the handoff text and the entry do not exist at review time; `.ufo/waves/round-67/stage/entry-spec.md` had not landed (dependency recorded, not waited on). This report specifies what must be true and the grep set that decides it; a later reader must re-run the recipe on landed bytes.
- **Counter invisibility stands:** all twelve C legs, all Ca/O legs, and both receipts can be green with no handoff, a canon-claiming sentence, or a rights claim in the entry. `claims.json` review_only is the only honest guard; do not let the L1 write "adjacency improved" off the row count.
- **Semantic ownership is review-only:** the claim's filename census (0 hits) is true and already corrected as narrow; the amulets entry, the two shrine entries and the civilizations' restriction policy are the semantic owners missing from the census, and they are the reason S828/S825/S817 need one-way bullets rather than new paragraphs.
- **Digest split is pre-existing:** live contract bytes hash `5f4c02bf…`; r66 recorded stale pins `50c4c2f2…` in r9/r18 fixtures and `corpus/lessons/round-2-adjacency.md:88`. Nothing in this round should re-pin; if the L1 does, it must be `5f4c02bf…` (measured again this seat).
- **Owner collisions are recorded, not resolved:** sixteen owners stay dual-topic until they point back; NOHARM forbids touching them.
- **Not in my scope, flagged for the L1:** the entry's section count and RESTATE arithmetic (`RevEntrySpec`), per-row source support (`RevSourceSupport*`), and the rejected-row teaches cells (`RevCounterCa`). My scope was the one-way split and the boundary bullets.

## Tooling

No install or upgrade performed; no pacman transaction attempted (host-wide pause respected). Read-only review, `git`/`git grep` reads only, lane jj state and Git index untouched.

Report: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-67/w1/RevLoreHandoff.md
