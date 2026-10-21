# Frontier source open — Fulani/WoDaaBe transhumance, two candidates opened

Seat: `ChousaR27R2.SrcFulani-4` (scout, leaf). Round 50, claim **C** (coverage / pastoralism entry).
Base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only: no lane file edited, no clone, no patch
(scout seat, not executor). Nothing written under `/home/vgpnk/Projects/shokunin/.ufo`.

## Assigned item

Open an FAO / ILRI / peer-reviewed open source on Fulani/WoDaaBe transhumance in the Sahel; quote a
located passage on seasonal mobility; return a SOURCES candidate (URL, access date 2026-10-21, kind,
tier + reason, scope, ≤25-word verbatim quote with location, what it teaches the entry and which
section, recheck cadence). If unreachable, report the failure and stop.

## Result — both candidates are real, opened, and quotable

Verdict: **one tier-A source for the movement system itself** (Schareika's FAO monograph, full text
open, quoted from the author's own chapters) and **one tier-B source for the 2022 contraction of the
mobility space** (Morello & Rizk, *Forced Migration Review* 69). No fetch failed; no quote is
paraphrased; every quote below was re-fetched as raw HTML this session and matched byte-for-byte
(italics tags only).

URLs opened this session (2026-10-21), in order:

| # | URL | What it yielded |
|---|---|---|
| 1 | https://www.fao.org/4/y5115e/y5115e00.htm | front matter: title, author, `ECOLOGICAL KNOWLEDGE AND HERD MOVEMENT STRATEGIES AMONG THE WODAABE OF SOUTHEASTERN NIGER`, `© FAO 2003`, `ISBN 92-5-105061-9`, full TOC |
| 2 | https://www.fao.org/4/y5115e/y5115e02.htm | foreword: the study's scope (local knowledge in semi-arid rangelands; herd mobility and labour; scouts as "pastoral sentinels") |
| 3 | https://www.fao.org/4/y5115e/y5115e03.htm | introduction, incl. the **orthography note** on Fulfulde implosives (see precision limits) |
| 4 | https://www.fao.org/4/y5115e/y5115e07.htm | ch. "THE PASTORAL WAY TO EARN A LIVING": diversify-vs-specialize; "Most Fulani in West Africa diversify…"; women sell milk |
| 5 | https://www.fao.org/4/y5115e/y5115e08.htm | ch. "THE CULTURE OF MOVING AND THE PATTERNS OF MOVEMENT": **the four move types**, camp rhythm, calf rope, habit (*woowa*), identity |
| 6 | https://www.fao.org/4/y5115e/y5115e0c.htm | ch. "THE SEASONAL CYCLE": *seedu*/*ndunngu* as vegetation states; season vocabulary; move decisions by ground inspection |
| 7 | https://www.fao.org/4/y5115e/y5115e0d.htm | ch. "APPLICATION OF KNOWLEDGE…": the annual route leg by leg; mobility as timing; wells; *kundeeri*; drought |
| 8 | https://www.fao.org/4/y5115e/y5115e0e.htm | ch. "CONCLUSIONS": 2003-era security/policy pressures (Fulani–Tubu conflict, fees at borders) |
| 9 | https://ora.ox.ac.uk/objects/uuid:7b8f982c-c38a-4edd-8768-baa0f05835f7/files/s1v53jx974 | Morello & Rizk PDF (ORA copy), pp. 22–24, FMR 69 |
| 10 | https://www.fmreview.org/climate-crisis/morello-rizk/ | canonical FMR page: `FMR 69 – Climate crisis and displacement…`, `February 2022`, authors + affiliations, 5 endnotes |

Re-fetch check used to pin the quotes: `curl -s <url> | tr '\n' ' ' | tr -s ' '` then a literal
pattern match on each sentence; all matched.

## Candidate rows — ids pending L1 (`S048` is already taken by two sibling reports)

`S048` is proposed independently by `build/SrcDysonHudson.md:38` (Dyson-Hudson & Dyson-Hudson 1980)
and `build/SrcUnescoGer.md:11` (UNESCO Mongol Ger). **Do not assign `S048` to either row below.**
They need two consecutive ids from the next free block, after the sibling proposals are numbered.
Rendered here with id placeholders `<A>` and `<B>`; substitute before landing.

Both rows obey the round-49 census shape (`reports/round-49/run-validation.py:56-62`): exactly 11
cells / `NF==13` on `|`, no pipe characters inside cells, kind ∈ `{spec,docs,paper,code,tool,dataset,talk,book,community,own-work}`,
tier ∈ `{A,B,C}`, status ∈ `{queued,mined,rejected}`, `opened` = `2026-10-21`.

### Row `<A>` — Schareika 2003, FAO monograph (movement system)

```
| S<A> | Schareika 2003, Know to Move, Move to Know: Ecological Knowledge and Herd Movement Strategies among the Wodaabe of Southeastern Niger, FAO — https://www.fao.org/4/y5115e/y5115e00.htm | book | A | the WoDaaBe seasonal movement system and its named move types in southeastern Niger, as one ethnographer's 1996-97 fieldwork account — not Fulani pastoralism at large, not herd species other than cattle, not current practice | FAO 2003, ISBN 92-5-105061-9, © FAO 2003 front matter; ch. "The culture of moving and the patterns of movement" at https://www.fao.org/4/y5115e/y5115e08.htm; ch. "The seasonal cycle" at y5115e0c.htm; ch. "Application of knowledge to the pursuit of herding" at y5115e0d.htm | four named move types — historical perol, seasonal baartol (west with the first rains in May-June, about-turn when the rains install in July, back east by early October), middle-range goonsol, camp-site transfer sottol; herd and household move together every two to ten days; the year is classified by vegetation state (seedu dry matter vs ndunngu fresh matter) not by calendar, and movement is used to time an ecological process rather than merely to cover distance; proving oneself mobile conditions herder membership and stock loans (habbaye) | queued | 2026-10-21 | 365d | — |
```

### Row `<B>` — Morello & Rizk 2022, FMR 69 (pressure snapshot)

```
| S<B> | Morello and Rizk 2022, Conflict, climate change and the shrinking mobility space in the Central Sahel, Forced Migration Review 69:22-24 — https://www.fmreview.org/climate-crisis/morello-rizk/ | paper | B | the contraction of transhumant mobility space in Burkina Faso, Mali and Niger as of early 2022 — conflict, corridor encroachment and policy bias; not pastoral ecology and not movement technique | FMR 69 "Climate crisis and displacement: from commitment to action", February 2022, pp. 22-24; section "The Liptako-Gourma border region: from transhumance to displacement", paragraphs 1-3 | security has become the main criterion for transhumant route choice; corridors are narrowed by insecurity, farmland encroachment and a policy bias toward sedentary agriculture, so mobility turns from resilience strategy into a reactive mechanism — a dated pressure snapshot, not a description of the movement system | queued | 2026-10-21 | 180d | — |
```

Status/used-by rule (append-only, `corpus/SOURCES.md:12-16`): append as `queued` with `used-by —`.
When claim C's entry cites a row, the C author flips it to `mined` with `used-by
corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` and logs the old→new change in
`corpus/lessons/round-50.md`. Census command 7 requires that path to exist on disk, so the flip must
land **with or after** the entry, never before it.

## Verbatim quotes and locations (all ≤25 words)

| # | Quote | Words | Exact location | Grounds |
|---|---|---|---|---|
| A1 | "Typically, seasonal migration starts with the beginning of the rains in May or June and leads towards the west." | 19 | y5115e08.htm, list "There are four types of pastoral movement", item 2 (*baartol*), last sentence | **Gate quote for row `<A>`** — seasonal mobility has a named type, a season, and a direction |
| A2 | "Rather, the nomads use spatial mobility as a tool for timing an ecological process" | 14 | y5115e0d.htm, §"EARLY RAINY SEASON - MOVING TO THE SANDY DUNES", ¶2 | the entry's register property: movement is a scheduling instrument |
| A3 | "*seedu* stands for hardship, barrenness, drought and the danger of animal death; *ndunngu* by contrast is joy, fertility, freshness and life" | 21 | y5115e0c.htm, §"THE DUAL CLASSIFICATION OF THE YEAR", ¶2 | the affective valence that makes the pastoral calendar a cosmology hook, not just agronomy |
| A4 | "Both are states within which a herder finds himself and not particular periods of time" | 15 | y5115e0c.htm, same section, ¶3 | the year is indexed by vegetation state, so the "calendar" is a monitoring instrument |
| A5 | "Decisions to move are mostly based on the inspection (*seewtunde*, *woosunde*) of ground surface and the grass found there" | 19 | y5115e0c.htm, §"THE SEASONS IN DETAIL", ¶3 | the decision rule: ground truth beats sky-reading |
| A6 | "According to the Wodaabe, constant and unhindered roaming through free and unpopulated bushland is of prime importance to herd development" | 20 | y5115e08.htm, ch. opening ¶1 | the group's own stated preference for open bush — an emic value, not a constraint |
| A7 | "They dispose of neither huts nor tents and only possess belongings that can be easily and quickly saddled to a couple of donkeys." | 23 | y5115e08.htm, ¶ after Photo 10 | the material-culture consequence of the move rhythm |
| A8 | "The calf rope is in fact a central symbol of Wodaabe pastoral culture" | 13 | y5115e08.htm, ¶3 (sentence continues "and not only a technical implement, cf. Schareika 2003a") | the one object the entry can treat as symbolic as well as technical |
| A9 | "static herd size is not the appropriate and relevant unit of analysis to a herder" | 15 | y5115e08.htm, §"MOVING AS A WAY TO KNOW", ¶1 | anti-myth: wealth is herd fertility (cows mated), not head count |
| A10 | "Pastoral mobility has thus become a socially relevant marker of attitude of those who 'keep the cows under surveillance'" | 19 | y5115e08.htm, §"MOBILITY AS A MARKER OF IDENTITY", ¶1 | mobility as membership test (stock loans, *habbaye*) |
| A11 | "there is no absolute standard for choosing good range" | 9 | y5115e08.htm, §"MOVING AS A WAY TO KNOW", ¶3 (habit, *woowa*) | why a "best pasture" rule cannot be written abstractly |
| A12 | "Most Fulani in West Africa diversify production by herding cattle and cultivating fields." | 13 | y5115e07.htm, ch. opening ¶1 | the diversify/specialize continuum — the WoDaaBe are the specialized pole |
| B1 | "Security has now become the main, if not the only, criterion informing the choice of transhumant routes." | 17 | fmreview.org/climate-crisis/morello-rizk/, §"The Liptako-Gourma border region…", ¶2 | **Gate quote for row `<B>`** — route choice inverted by conflict |
| B2 | "Herders’ movements are constrained by high levels of insecurity, encroachments on transhumant corridors and pastoral land" | 16 | same article, same section, ¶1 | the three named constraints, in the authors' own list |

## Tier and scope reasoning (QUALITY criterion 6, `corpus/QUALITY.md:29`)

- **`<A>` = A, narrowly.** Criterion 6 reserves A for sources "primary or authoritative for the
  exact scope" and demotes publisher blurbs/abstracts to B. This is not a blurb: the opened bytes are
  the monograph's own chapters, the author's first-hand 1996–97 fieldwork account, published by FAO
  with ISBN. For the scope "the WoDaaBe seasonal movement system and its vocabulary in southeastern
  Niger" it is primary. It is **not** A for Fulani pastoralism generally (one group, one region), not
  A for current practice (fieldwork 1996–97), and says nothing about camels or small ruminants — the
  book is about cattle.
- **`<B>` = B.** FMR is an editorially reviewed practitioner journal of the Refugee Studies Centre
  (Oxford), not a peer-reviewed research journal; the piece is a short analysis with named authors
  (Samuel Hall research manager; ICRC migration advisor) and 5 endnotes. Strong secondary for the
  policy/conflict scope; it reports no new data and is not primary. Not C — it is specific,
  attributable and internally referenced, and its factual claims are checkable against its endnotes.
- Both scopes are deliberately narrower than the entry's topic. Tier travels with the `scope` cell,
  never with the row (`corpus/SOURCES.md:17-20`).

## What each source teaches the entry, and which section

Section numbering below follows the model entry `culture-material/hunting-foraging-subsistence.md`
(§1 register property … §15 scope); the C author sets the pastoral entry's own numbering.

| Target section (model numbering) | Take from `<A>` (Schareika) | Anchor |
|---|---|---|
| §1 register property | Herding is an argument about **vegetation state and season**, and mobility is the instrument that times it — the pastoral analogue of the hunting entry's "landscape as a schedule". The year is not a calendar of months but two states (*seedu* dry matter / *ndunngu* fresh matter) with an affective charge. | A2, A3, A4 |
| §2 one-owner boundary | Nothing here duplicates an existing owner. Nearest existing mentions, all cross-references, none owning the register: `linguistics/semantic-fields-lexicon-building.md:70` (pastoral wealth vocabulary), `:105` (steppe-pastoral field bundle), `myth-symbol/celestial-symbolism-calendars.md:28` (pastoralists on milky/river figures), `culture-material/calendar-festival-systems.md:79` (husbandry month names). | greps run this session |
| §3 production chain (herd → household) | The unit is **household + herd moving together**, not a herd alone; the calf rope (*daangol*) binds the herd to the camp; the camp splits when herders disagree. | A7, A8; y5115e08 ¶3–5 |
| §4 toolkit and materials | Portability is the design constraint: no huts, no tents, two donkeys, and the two heaviest items belong to married women (wooden bead stead; platform for donkey bags). The calf rope is simultaneously technique and central symbol. | A7, A8 |
| §5 seasonal round and mobility | The four named move types with their triggers: *perol* (rare historical relocation), *baartol* (seasonal, scouted + predetermined direction, west May–June → about-turn July → east by early October), *goonsol* (middle-range, between pasturelands of one zone; in the dry season, between well territories), *sottol* (camp transfer inside one pastureland, used when droppings degrade a site). Camp rhythm: every 2 days in the rains, up to 10 in the dry season. The dry-season leg ends the *baartol* cycle at the wells (*nanngita bunndu*, "catch anew a well"); well access is registered and paid, which fixes position. | A1; y5115e08 items 1–4; y5115e0d §§ early rains / height of rains / cold dry season |
| §5 (decision rules) | Move on ground inspection, not cloud-reading; avoid old droppings (*welaande*) and the stench of dirty grass (*fufo*); avoid grasshopper-infested range and herds with contagious disease; prefer untouched rangeland (*geene de njaabaaka*); habit (*woowa*) caps where a herd can go; competition (*nyaara*) to be ahead of other herds. | A5, A11; y5115e0d ¶s 2–4 |
| §7 labour and identity | Mobility is the membership test: to get stock on loan (*habbaye*) "one has to prove oneself mobile"; herd performance is compared in joking verbal battles (*mbeefi*); women pack the household and sell milk; men take over milking when women sell. | A10; y5115e07 (milk sale); y5115e08 §"MOVING AS A WAY TO KNOW" |
| §9 decision table | Each move type answers a distinct failure mode: *sottol* ← droppings/stench; *goonsol* ← exhausted well territory or degraded range; *baartol* ← the fresh-matter front moving; *perol* ← political/ecological crisis. | y5115e08 items 1–4; y5115e0d |
| §13 calibration bank | Four anti-myths, below. | A2, A9, A12, B1 |
| §14 recheck | 1996–97 fieldwork / 2003 publication: never present as current. The FMR 2022 snapshot is itself dated and fast-moving. | A-row `opened`/`recheck`; B1 |
| §15 scope | Cattle only; southeastern Niger (Kawlaa) only; one ethnographer's account. | front matter + y5115e07 |

## Anti-myths for the calibration bank (§13)

1. **"Pastoralists wander."** False for this case: movement is typed, named, scouted, directional and
   seasonal, and each type answers a specific degradation problem (A1; y5115e08 items 1–4). Wander is
   the *absence* of the system this entry describes.
2. **"Wealth is head count."** Explicitly not: herders aim at herd fertility, do not count animals,
   and do count mated cows (A9). Any entry sentence equating herd size with status contradicts the
   source.
3. **"Fulani = one production system."** The monograph itself splits the continuum: most Fulani
   combine herding with cultivation; the WoDaaBe are the specialized herders (A12, y5115e07). The
   entry may write "Fulani herders *who specialize*…", never "Fulani herders…".
4. **"Mobility is free."** Two independent brakes: internally, habit (*woowa*) and paid/registered
   wells (A11; y5115e0d cold-dry-season §); externally, in 2022 security is the first criterion for
   route choice (B1) and corridors are narrowed by farmland and policy (B2).
5. **"The seasonal calendar is a calendar."** It is a vegetation-state classification with an
   affective valence (A3, A4) — a monitoring instrument, not a month list.

## Precision limits and non-uses (read before citing)

1. **Group vs category.** The book is about the **Wodaabe of southeastern Niger**, a Fulfulde-speaking
   herding group. That they belong to the wider Fulani/Fulɓe category is an **inference** from (a) the
   orthography note "the implosive b and d used in the Fulfulde language" (y5115e03) and (b) the
   contrast drawn with "Most Fulani in West Africa" in a book about these specialized herders
   (y5115e07) — the pages I opened never state "the Wodaabe are Fulani" in one sentence. Safest
   phrasing for the entry: "Fulfulde-speaking Wodaabe herders of southeastern Niger"; if the entry
   wants "Fulani", mark it as the wider category and keep the claim scoped to these herders.
2. **Orthography.** The publisher warns it could not render the implosive *b* and *d* of Fulfulde and
   writes them as plain *b*/*d* (y5115e03, "Note on orthography"). Therefore the online spellings
   *baartol*, *perol*, *goonsol*, *sottol*, *seedu*, *ndunngu* are **lossy transliterations**. The
   entry must not claim phonetic accuracy, and should say "as transcribed by Schareika/FAO online".
3. **Time.** Fieldwork 1996–97, book 2003. This is a historical ethnography of a system, not a report
   on 2026 conditions. The entry's present-tense sentences need a second, current source or a dated
   hedge.
4. **Species.** Cattle (red Zebu). No camels, no sheep/goats beyond passing mentions. A herd-species
   section cannot be built from this row.
5. **No numbers.** The opened chapters are qualitative: no herd sizes, no yields, no frequencies. Do
   not manufacture a statistic; the entry's calibration bank must state its quantities as
   `(to-verify)` or leave them out.
6. **Do not cite `<B>` for technique** and do not cite `<A>` for conflict/policy. The rows are disjoint
   by scope on purpose — this is the r49 separability lesson applied inside claim C.

## Handoff candidates (lore, not ownership)

- *daangol* (calf rope) as "a central symbol of Wodaabe pastoral culture" (A8) → `myth-symbol/animal-symbolism.md` or the entry's own §8, cited, not restated.
- Season valence — *seedu* hardship/death, *ndunngu* joy/life (A3) — plus the wind/cloud vocabulary (Box 8, y5115e0c) → `myth-symbol/celestial-symbolism-calendars.md` (which already assigns pastoralists milky/river figures at `:28`); the sky-register lexical set → `linguistics/semantic-fields-lexicon-building.md`.
- Rain prayer (Box 7, y5115e0c) and the fear of *seeduwa* (disastrous drought) → ritual/religion handoff, comparable to the hunting entry's kill-rite seam.
- Mobility-as-membership (A10) → the entry's labour/identity section, and a possible cross-link from `linguistics/semantic-fields-lexicon-building.md:70` (pastoral wealth vocabulary indexes property systems) — that line currently has no pastoral owner to point at.

## Gate lines for `corpus/lessons/round-50.md` `## Gate`

The frontier seat/L1 should paste one line per row, substituting the assigned id. The round-49
validator requires each line to start `- S0NN ` (space after the id) and to cover every registry id
(`run-validation.py:210-215`); round 50's own receipt needs `opened`/access date `2026-10-21`.

```
- S<A> — https://www.fao.org/4/y5115e/y5115e08.htm — accessed 2026-10-21 — ch. "The culture of moving and the patterns of movement", list "There are four types of pastoral movement", item 2 (*baartol*), last sentence: "Typically, seasonal migration starts with the beginning of the rains in May or June and leads towards the west." Grounds: seasonal mobility is a named, scouted, directional move type with fixed seasonality. Tier: A per QUALITY criterion 6 (opened monograph text, author's own fieldwork, scope-limited to the WoDaaBe movement system).
- S<B> — https://www.fmreview.org/climate-crisis/morello-rizk/ — accessed 2026-10-21 — section "The Liptako-Gourma border region: from transhumance to displacement", ¶2: "Security has now become the main, if not the only, criterion informing the choice of transhumant routes." Grounds: the 2022 contraction of transhumant mobility space in Burkina Faso, Mali and Niger; a dated pressure snapshot. Tier: B per QUALITY criterion 6 (editorially reviewed practitioner journal, named authors, endnoted; not peer-reviewed primary).
```

Note on URL placement: the row's `source` URL is the work root (`y5115e00.htm`, which carries the
title/ISBN/TOC); the Gate quote lives on chapter page `y5115e08.htm`. If the frontier seat prefers
one URL per row for mechanical matching, swap the row URL to `y5115e08.htm` and keep the other
chapters in `anchor` — both forms are honest; only the Gate line must name the URL actually opened
for the quote.

## What claim C's entry must satisfy mechanically (checked, not guessed)

- The `- source:` line must render every cited id as `**S0NN** (https://…)`, else the r49 cross leg
  reports it as `no_inline_url` (`run-validation.py:266-270`).
- Census command 7 requires each `mined` row's `used-by` path to exist (`run-validation.py:62`), so
  flip status in the same landing as the entry.
- No `|` inside any registry cell: the census malformed check requires `NF==13` (`run-validation.py:57`).

## Unrun checks / bounds honoured

- Did not run the entry's gap sweeps, the README sweep, or any lane selftest — not this seat's
  question (claim C's executor and the verifier own those). The 225-entry / 27-culture-material count
  and the zero-pastoral registry grep are single facts read this session, not a sweep.
- Did not write, clone, patch, or touch git/jj state; no `git add|commit|checkout|reset`; no mutating
  `jj`; nothing under `/home/vgpnk/Projects/shokunin/.ufo`.
- Did not open the monograph's remaining chapters (y5115e04, y5115e05, y5115e06, y5115e09–0b, y5115e0f)
  beyond the two title/identification checks; no claim above rests on them.
- No installs attempted or needed (no `pacman` transaction; host pause respected); nothing to record
  in the tool ledger.
- Remaining unknown for the C author: whether "Wodaabe are Fulani" is stated in a source this lane has
  opened. It is not stated on the pages opened here — either use the directly supported phrasing or
  open a second source that says it.
