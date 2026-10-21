# ReviewSec08 — falsify §8 "Tenure, commons and mobility rights" (Hardin / Ostrom / earmark rows)

**Item attacked:** claim **C** (coverage) of round 50 — the landed entry
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` at
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, section **§8** (lines 108–118), plus the
SOURCES rows it leans on (S049, S054, S055, S059) and the two in-corpus anchors it cites
(`civilizations/finnic-sami.md:150`, `civilizations/dine-navajo.md:125`).

**Method:** every byte read from the landed commit via a private clone
(`git clone --shared` → `/tmp/k50sec08-XXXX`, `checkout 1c779e4a…`). The lane repo was not
touched; no jj/git mutation in the lane; no URL re-opened (URL re-opening is the
ReopenS0xx seats' job — flagged where I need them). No installs (nothing needed).

**Verdict: PARTIAL.**
The three model rows of §8 (Hardin / Ostrom / earmark) **HOLD** — each is quoted verbatim
from the round's Gate, each is inside its SOURCES row's scope, and each carries a
calibration status that matches `corpus/knowledge/verification/calibration-registry.md:35-39`.
(The earmark row's *facts* were independently re-verified live by `ReopenS059-21` on
2026-10-21: "Ett renmärke är mycket personligt och går vanligtvis i arv inom släkten." /
"Ett renmärke är registrerat för användning inom viss sameby." / "Omärkta renar är samebyns
kollektiva egendom." — all present verbatim on sametinget.se/renmarken. So §8 does not
overclaim there; what fails is the **entry's own wording** — "a Sámi earmark" (dropping the
Swedish/Norwegian distinction the row registers) and "is personal" (omitting the sameby holder
class the page states). The row's anchor is one paragraph narrow, a non-blocking precision nit
under `corpus/SOURCES.md:9-12`; no superseding row is owed.)
The sentences *around* those rows do **not** hold: one is an overclaim beyond both of its
cited in-corpus anchors, one is an uncited factual assertion, one drops the population bound
the registry's B rule requires, and the section's own title ("commons and mobility rights")
is not delivered. §8 also has a downstream ownership collision with
`agrarian-field-system-lexicon.md:33` (which owns *water* and *tenure*) that §2's boundary
table does not disclose.

---

## 1. What holds (verified)

### 1.1 The three model rows are quote-faithful to the round's Gate

| Entry line | Entry text | Gate (`corpus/lessons/round-50.md`) | SOURCES row |
|---|---|---|---|
| `:114` | `"Picture a pasture open to all" (S054)` | `:39` — p. 1244: "The tragedy of the commons develops in this way. **Picture a pasture open to all**." | `corpus/SOURCES.md:83` |
| `:115` | design principles for long-surviving institutions `"developed by the users of a resource" (S055)` | `:40` — §4E, PDF p. 15: "…long-term survival of an institution **developed by the users of a resource**." | `corpus/SOURCES.md:84` |
| `:110` | Tenure `"is thus divided by both ecology and the potential for agriculture" (S049)` | `:34` — §Land tenure: "**Tenure is thus divided by both ecology and the potential for agriculture.**" | `corpus/SOURCES.md:78` |

All three are exact substrings of the Gate quotes (no paraphrase, no invented wording).
Command evidence: `grep -n 'S054\|S055\|S049' pastoral.md` at the landed sha; Gate lines
read from `corpus/lessons/round-50.md:34,39,40`; SOURCES rows from
`corpus/SOURCES.md:78,83,84` (all in the landed tree).

### 1.2 Each row's status is inside its SOURCES row's scope

- **Hardin** — S054 scope: "the article's own wording and pagination of the open-pasture
  parable; **not an empirical description of any pastoral commons**"; supports column:
  "a counterfactual baseline, not a law of pastoral life". Entry status
  "**R** as a law of pastoral life; **B** for genuinely open access" is exactly that.
  R's registry stop rule (`calibration-registry.md:35`) permits "portray the theory as a
  dated ideology or choose a fictional premise explicitly" — the design cell ("a designed
  collapse only where no rule exists") does exactly that.
- **Ostrom** — S055 scope: "Ostrom's own 2009 formulation … ; **not the 1990 book's wording**";
  supports: "design principles as diagnostic, not a predictive law". Entry status "mainstream
  as diagnosis; C as a predictive law" matches. The entry never quotes Ostrom 1990 — it
  explicitly defers it (`pastoralism-animal-husbandry.md:195`: "open Herskovits 1926 and Ostrom
  1990 before quoting them (only S053 and S055 are opened)"). **Criterion-6 clean.**
- **Earmark** — S059 scope: "the Swedish earmark institution as stated by the agency that keeps
  the register; not Norwegian law, not a court holding"; supports: "personal, usually
  inherited, registered for one sameby; unmarked reindeer are the sameby's collective
  property". Entry `:116` asserts exactly these three facts and nothing more. **In scope.**

### 1.3 No canon decision is taken in §8

§8 contains no world-fact, no named people, no numbers. The worked example is fenced
(`## 12. NON-CANON`, `:167-171`) and the handoff is stated at `:197-199` ("which herds, routes,
marks, raids and rites exist in a world is canon, decided there"). QUALITY criterion 5 clean
for §8.

### 1.4 Claim-C mechanics that touch §8 are green (checked anyway)

Run in the private clone:

```
$ git ls-tree -r --name-only 4ad2683 corpus/knowledge | grep -icE 'pastoral|husband|herd'   → 0
$ git grep -niP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' 4ad2683 -- corpus/knowledge | wc -l → 0
$ git ls-tree -r --name-only 4ad2683 corpus/knowledge | grep -c '\.md$'                      → 225
$ git ls-tree -r --name-only 4ad2683 corpus/knowledge/culture-material | grep -c '\.md$'      → 27
$ python3 -B reports/round-28/readme/sweep.py        (at landed sha)
   rows 226 files 226 topic_mismatch 0 orphan_rows 0 totals_line 226 totals_ok True
   footer {"total": 226, "dir_totals": [25,26,28,29,24,94]} footer_ok True      exit 0
```

S-id resolution for the whole entry (script over the landed `pastoral.md` + `sources.md`):
cited `S048…S069` (22 ids) — **0 missing rows, 0 rows whose `used-by` fails to name the
entry**. Entry shape: 1 `#` H1, 0 `###` H3, 1 `- topic:` line, head fields in order
`topic, gap filled, sources, couples, source, verified-at, recheck, scope`. So the *coverage*
claim's mechanical conditions hold; the defects below are inside §8's prose.

---

## 2. Findings by severity

### P1 — §8 `:118`: the cited anchors do not support two of the three claims in the sentence

```
:118  State settlement, privatisation and route closure are local history, never a fixed
      endpoint of mobility (`finnic-sami.md:150`; `dine-navajo.md:125`).
```

Anchor text at the landed sha:

- `corpus/knowledge/civilizations/finnic-sami.md:150` — "| Late medieval/early modern
  livelihood changes | Large-scale pastoralism has a history; it is not the eternal condition
  of all Sámi communities (Aikio 2012: 86). | Date herd scale and seasonal labor by locality;
  do not make a single "reindeer revolution" fleet-wide. |"
- `corpus/knowledge/civilizations/dine-navajo.md:125` — "| Spanish-colonial and subsequent
  pastoral transformations | B23-E relates Navajo-Churro history to sheep introduced from
  Spain and to later Diné breeding and land-based practice. | "Traditional" can incorporate
  introduced animals; do not stage wool pastoralism as unchanged from remote antiquity. |"

What the anchors support: **pastoralism and its land base have a history** (both), and that
Diné land-based practice is a Spanish-colonial transformation (`:125`). What **neither**
anchor mentions: **privatisation**, **route closure**, or any rule about **movement rights**.
`finnic-sami.md:150` also does not say settlement is *not* an endpoint — it says pastoralism
is *not the eternal condition* of all Sámi communities, which is the opposite polarity and
can be read to make sedentarisation a real historical outcome. The absolute quantifier
"never" is additionally unearned.

This is a QUALITY criterion-1 defect: two of the three factual items in the sentence have no
cited support and are not marked `(to-verify)`.

**Smallest fix:** narrow the sentence to what the anchors carry, e.g.

> State settlement and land-based pastoral practice are local history, never a fixed endpoint
> of mobility (`finnic-sami.md:150`; `dine-navajo.md:125`); route closure and privatisation are
> case-specific `(to-verify)`.

(or drop "privatisation and route closure" and the word "never"). **Do not park the two items
on S049:** per the S049 re-open (`ReopenS049.md` §5–§6, live HTTP 200, 2026-10-21), the FAO
chapter carries the tenure-division sentence, the labour-wealth passage, "fluid systems that are
hard to pin down", the common-property *debates* framing and the weak-external-exclusion
sentence — it carries **no** privatisation or route-closure material, so those two need their
own source or the `(to-verify)` mark.

---

### P2-a — §8 `:110`: an uncited factual claim about what a herd move claims

```
:110  A herd move claims three things: a route, a water point and a pasture. Each is a rule
      with an owner, not a landscape feature. Tenure "is thus divided by both ecology and the
      potential for agriculture" (S049).
```

Sentence 1 is a general claim about the structure of pastoral tenure, presented as fact with
**no source and no `(to-verify)`** — a criterion-1 gap ("every factual claim carries a cited,
checkable source"; the entry's own `recheck` line `:11` promises exactly this discipline).
The registered source that could carry it is S049 (scope: "pastoral land tenure … §Land tenure
and the common property resources debate") — but the S049 citation in this paragraph is
attached to the *next* sentence only.

Second, smaller defect in the same line: the S049 fragment is quoted as
`Tenure "is thus divided by both ecology and the potential for agriculture"`. The quoted
fragment begins mid-sentence with "**is thus**", whose anaphor in FAO's text points at FAO's
own preceding argument; the entry places it immediately after its own sentence, so the reader
reads "thus" as following from *the entry's* route/water/pasture claim — which S049 does not
say. The quote therefore implies a derivation the source does not make.

**Smallest fix:** quote the full sentence (`"Tenure is thus divided by both ecology and the
potential for agriculture"`) and mark the three-unit decomposition `(to-verify)` — **do not
cite S049 for it** (the FAO land-tenure chapter carries no such three-part decomposition, per
`ReopenS049.md`); the nearest in-corpus framework that *does* treat water and tenure as
owned institutions is `agrarian-field-system-lexicon.md:33`, which is exactly the overlap to
declare (P2-b).

---

### P2-b — §8 `:110` vs `agrarian-field-system-lexicon.md:33`: an undisclosed ownership overlap

The agrarian entry states its partition rule in its own words:

```
corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:33
  … **This file owns parcel, implement, water, rotation, harvest, storage-as-bulk, and tenure.**
```

and the sibling hunting entry honours that in its boundary table
(`hunting-foraging-subsistence.md:51`: "parcel, plough, water, tenure (`:3,:33`); gleaning-right").

The new entry's §2 boundary table (`pastoralism-animal-husbandry.md:31`) lists the agrarian
neighbour as owning only "parcel, plough, stubble grazing, manure contract" — **water and
tenure are dropped** — and then §8 `:110` asserts that a herd move claims "a route, a water
point and a pasture. Each is a rule with an owner". The "water point … rule with an owner" and
the pasture-tenure claims sit inside the agrarian entry's declared ownership of *water* and
*tenure*, with no one-way citation and no statement of the difference (pastoral well/track
rights vs irrigation water institutions). The "route" claim likewise leans on
`transport-mobility-lexicon.md`, whose "route class" row is at `:92` (§2 `:34` cites `:95`,
see P3-a) — so §8's route-as-a-claim has no correctly-anchored owner citation either.

**Smallest fix:** in §2 `:31` write the agrarian neighbour's ownership as
"parcel, plough, water, tenure, stubble grazing, manure contract (`agrarian-field-system-lexicon.md:33`)";
and in §8 `:110` add one clause that draws the line, e.g. "pastoral water and track rights are
not the agrarian water institutions (`agrarian-field-system-lexicon.md:33`)".

---

### P2-c — §8 `:116`: the earmark row drops the population bound its own source demands

```
:116  | Earmark institutions | a Sámi earmark is personal, usually inherited and registered for
      use in one herding community; unmarked reindeer are that community's collective property
      (S059) | B — one legal system | write who may herd where, and how a mark is inherited |
```

`corpus/SOURCES.md:88` (S059) scope: "**the Swedish earmark institution** as stated by the
agency that keeps the register; **not Norwegian law**, not a court holding". The entry writes
"**a Sámi** earmark" and "one herding community", dropping *which* Sámi legal system is meant
and dropping the explicit non-Norwegian exception the row registers.

**Live re-open (by seat `KotodamaR50-2.ReopenS059-21`, https://sametinget.se/renmarken,
HTTP 200, two fetches, same text — handed to me, not re-opened here):** every fact the §8 row
asserts is verbatim on the page, but **not in the anchored paragraph**:

- "Omärkta renar är samebyns kollektiva egendom." (+ ingress end: "En omärkt ren tillhör samebyn i området.")
- "Ett renmärke är mycket personligt och går vanligtvis i arv inom släkten."
- "Ett renmärke är registrerat för användning inom viss sameby."

Location: the H1 `<div class="ingress"><p>` ends at "En omärkt ren tillhör samebyn i området.";
the four sentences above sit in the **next element, `<div class="text"><p>` — the first body
paragraph of the same opening section, one paragraph below the anchored Gate quote, before
`<h3>Vem kan äga ett renmärke?</h3>`**. Consequences for §8:

1. The §8 **proposition is factually backed** (good news — the earmark row is not an
   overclaim on the facts). What remains defective is the **entry's wording** (population and
   holder class, item 2 below) — not the claim. The row's anchor is one paragraph narrow
   ("page Renmärken (H1), **opening paragraph**" vs the facts in the first body paragraph);
   under `corpus/SOURCES.md:9-12` that is a **precision nit, not an admission defect**, and no
   superseding row is owed — see the optional note at the end of this item.
2. New, sharper scope slip the entry inherits: under that `<h3>` the page also says a sameby
   may itself own a mark ("Ett renmärke kan ägas av en sameby, …"), so §8's unqualified
   "a Sámi earmark **is personal**" omits a holder class the source itself states. The entry's
   row status "B — one legal system" is the only thing standing between the reader and that
   omission — which is exactly why the bound must be named (below).

The registry's B stop rule (`corpus/knowledge/verification/calibration-registry.md:37`) is:
"B | Bounded, usable within a named domain | **Carry population, genre, period, task, and
exceptions**; no extrapolation by resemblance". "B — one legal system" carries neither the
population nor the exception, so a designer can read the row as "Sámi earmarks work like this"
and import a Swedish register rule into a Norwegian/Sámi setting — the exact extrapolation the
registry forbids.

The same slip appears at `:77` (§5 ownership-mark cell: "a Sámi earmark is a combination of
cuts in both ears and names the owner (S059)"), which has no status cell at all.

**Smallest fix (entry text only — the two qualifiers live in the entry's propositions, not in
the registry):**

- `:116` → "a **Swedish** Sámi earmark is **usually personal** (a sameby may hold one),
  usually inherited and registered for use in one sameby; unmarked reindeer are that
  community's collective property (S059)"; Status → "B — the Swedish Sámi register only (not
  Norwegian law)".
- `:77` → "a **Swedish** Sámi earmark is a combination of cuts in both ears and names the
  owner (S059)" (and give the cell a status).

**Registry-side note (OPTIONAL, non-blocking — corrected after `ReopenS059-21`'s caution).**
The S059 anchor in `corpus/SOURCES.md:88` ("page Renmärken (H1), opening paragraph") is one
paragraph narrower than the facts the row and §8 rely on. That is a **precision nit, not an
admission defect**: `corpus/SOURCES.md:9-12` requires the Gate bullet to hold the row's URL,
access date and **one verbatim quote**, and the `anchor` field locates *that quote*; every
`teaches` fact is on the same page. No admission rule is broken, so **no superseding row is
owed**. (Were one filed anyway, it would have to be a new row whose `teaches` opens
"supersedes S059 —" and would need its own Gate bullet in a round lesson — heavier than the
finding, per `ReopenS059.md` N2 "No fix required for admission".) The fix that *is* owed is
entry-side, above.

---

### P3-a — §2 `:34` mis-describes the anchor it cites (`transport-mobility-lexicon.md:95`)

```
:34  | `transport-mobility-lexicon.md:95` | draught capacity chain, route class, load figures | …
```

At the landed sha that line is the **Draft** row:

```
corpus/knowledge/culture-material/transport-mobility-lexicon.md:95
  | Draft | human porterage, ox, horse/mule, camelid, dog, wind | load figure + daily distance +
  terrain law; harness and feed vocabulary | civilizations/inca.md, civilizations/turkic-steppe.md |
```

"Route class" is a **different row**, at `transport-mobility-lexicon.md:92`
("| Route class | track, paved road, causeway, canal, sea lane, relay corridor | a maintenance
institution and a permit regime |"). So one of the three ownership claims in §2's row is not
at the cited line. It matters for §8 because §8's route-as-a-claim is delegated to this owner.

**Smallest fix:** `:34` → `transport-mobility-lexicon.md:92,:95`.

---

### P3-b — §8 `:115`: status without the reason, and a design cell that lists a non-Ostrom item

QUALITY criterion 2 requires every framework entry to name its status "mainstream / contested
/ discredited, **with the reason**". §8's Ostrom row names statuses ("mainstream as diagnosis;
C as a predictive law") but no reason. The reason exists in the registry row
(`corpus/SOURCES.md:84`: "design principles as diagnostic, not a predictive law") and is not
carried into the entry.

Also, the design cell "rotas, fines, monitors and nested authority as in-world institutions"
lists **rotas**, which is not one of Ostrom's design principles (hers: boundaries,
congruence, collective choice, monitoring, graduated sanctions, conflict resolution,
recognition of the right to organise, nested enterprises), and rotas are not in the S055
anchor (§4E, one sentence on p. 15). Read as design instructions it is fine; read as "Ostrom's
principles" it is an overclaim. The Hardin and earmark rows, by contrast, do carry reasons.

**Smallest fix:** append the reason to the status cell — "mainstream as diagnosis (S055 states
the principles as diagnostic, not predictive); C as a predictive law" — and either drop "rotas"
or mark it `(to-verify)`.

---

### P3-c — §4 `:64` over-cites `finnic-sami.md:150`

```
:64  | Reindeer | taiga and tundra lichen pasture | … | herding status ≠ Sámi identity
     (`finnic-sami.md:140,:150`) |
```

`finnic-sami.md:140` ("Do not map herding status directly onto Sámi identity…") carries the
cell exactly. `finnic-sami.md:150` ("Large-scale pastoralism has a history; it is not the
eternal condition of all Sámi communities") does not — it is the anchor for the *history* of
herd scale, which is P1's sentence at `:118`. Cited in `:64` it is dead weight.

**Smallest fix:** `:64` → `(`finnic-sami.md:140`)` only.

---

### P3-d — coverage gap: §8's title promises "commons and mobility rights" that §8 does not deliver

The section is titled "Tenure, commons and mobility rights" (`:108`) but:

- **Commons**: the entry never states the commons distinction its own registered source carries.
  `corpus/SOURCES.md:78` (S049) files the third clause as "**pastoral tenure is a common-property
  debate, not open access**" — but that wording appears nowhere in the entry; the open-access /
  common-property / state / private set appears only in §13 `:182` ("choose the rule set first:
  open access, group, state or private") **without a citation**.
  **Correction (per `ReopenS049.md` caveat 1, live 2026-10-21):** only the first half of that
  registry clause is in the source — the chapter places pastoral systems "at the heart of many
  debates on the nature of common property resources" and calls pastoral tenure "fluid systems
  that are hard to pin down"; the phrase "**not open access**" is **not in the chapter** and the
  weak-external-exclusion sentence (farmers "can come and cultivate the land that herders
  regularly use for grazing their stock, without having to ask for permission") points the other
  way. So the fix is to import the **literal** half only; importing "not open access" would
  launder an over-adjudicated registry clause into an admitted sentence.
- **Mobility rights**: no rule, model or row anywhere in §8 governs *crossing* — who may use a
  route, a corridor, a well in season. §11 step 4 `:154` asks the designer to decide "who
  grazes, waters and **crosses where**", but §8 — the section that is supposed to supply the
  tenure model — gives no answer for the third of that triple.
  **Correction (per `ReopenS049.md`):** S049's land-tenure chapter does **not** carry
  movement/route-access material, so it cannot back a "route and corridor rights" row either;
  such a row needs its own source (or the FAO report's other chapters) or must be marked
  `(to-verify)`. What S049 *does* offer §8 is the honest pair of quotes above — tenure as
  "fluid systems that are hard to pin down" and the weak-external-exclusion sentence — which are
  a better fit for §8's commons gap than the unsupported half of the registry clause.

**Smallest fix:** (a) in §8's opening paragraph, carry the **literal** S049 material — tenure
"is thus divided by both ecology and the potential for agriculture" (S049) plus the chapter's
"fluid systems that are hard to pin down" and the weak-external-exclusion sentence — so the
commons question is framed from a source that actually says it; (b) add one **mobility-rights**
row to §8's table, marked `(to-verify)` unless a new row is registered for movement access; (c)
do **not** write "not open access" into the entry.

---

## 3. Canon decisions

**None found in §8.** The section makes no claim about any world; the only worked instance is
inside the `## 12. NON-CANON` fence (`:167-171`, and its tenure clause —
"pass rights held by lineages, meadow turns by lot, a fine for grazing out of turn (Ostrom-style,
S055)" — is a method demonstration, not a canon proposal). QUALITY criterion 5 holds for §8.
The only canon-adjacent hygiene note is the **living-practice flag** at `:189`, which names
Sámi herding as living practice (S058, S059, S063) — that flag covers the earmark row and
means the earmark material must be used as *mechanics*, not as a Sámi design template. Given
P2-c, that is one more reason the "one legal system" bound needs naming.

---

## 4. Residual risk / verification gaps (handed to other seats, not re-opened here)

1. **S059 depth — RESOLVED by `ReopenS059-21` (live, 2026-10-21, HTTP 200, two fetches, same
   text).** The §8 earmark row's three facts (personal / usually inherited / registered for
   one sameby; unmarked reindeer are the sameby's collective property) are **verbatim on
   https://sametinget.se/renmarken**: "Ett renmärke är mycket personligt och går vanligtvis i
   arv inom släkten." / "Ett renmärke är registrerat för användning inom viss sameby." /
   "Omärkta renar är samebyns kollektiva egendom." (plus "En omärkt ren tillhör samebyn i
   området." at the ingress end). **So §8's earmark proposition is factually backed — the
   defect is not overclaim, it is the anchor locator.** They sit in the first **body** paragraph
   (`<div class="text"><p>`), one paragraph **below** the H1 ingress paragraph that carries the
   quote (`corpus/lessons/round-50.md:44`: "Ett renmärke är kombinationen av snitt på både
   höger och vänster öra. Renmärket talar om vem som äger renen."), before the subheading
   "Vem kan äga ett renmärke?". `corpus/SOURCES.md:88`'s anchor ("page Renmärken (H1),
   **opening paragraph**") is therefore narrower than the facts it is registered for — a
   **precision nit, not an admission defect** (`corpus/SOURCES.md:9-12`: the Gate bullet holds
   the URL, access date and **one** verbatim quote; the `anchor` locates that quote), so **no
   superseding row is owed** — see P2-c for the optional note. **Residual open (entry-side):**
   the same subheading's "Ett renmärke kan ägas av en sameby" (a sameby may hold a mark) is
   omitted by §8's unqualified "is personal", and "a Sámi earmark" drops the Swedish/Norwegian
   distinction — both folded into P2-c as two-word entry fixes.
2. **S054 paragraph locator (→ `ReopenS054-21`).** `corpus/SOURCES.md:83` gives the anchor as
   "p. 1244, §The Tragedy of Freedom in a Commons, **first non-epigraph paragraph**", while the
   Gate's sentence context ("The tragedy of the commons develops in this way. Picture a pasture
   open to all.") reads like a mid-section paragraph. The entry's own quote is a verbatim
   substring either way, so the entry is safe; the **registry locator** may be imprecise.
3. **S055 §4E coverage (→ `ReopenS055-21`).** §8's design cell lists "rotas, fines, monitors
   and nested authority" while the registered anchor is a single p. 15 sentence. If the seat
   confirms only the general "design principles" formulation at that location, the cell needs
   either the wider location or the `(to-verify)` in P3-b.
4. **S049 tenure depth — RESOLVED by `ReopenS049-21` (live 2026-10-21, HTTP 200,
   `https://www.fao.org/4/y2647e/y2647e08.htm`).** §8's only S049 citation (`:110`) is
   **supported** — the Gate quote is the first sentence of the paragraph after the H2
   "LAND TENURE AND THE COMMON PROPERTY RESOURCES DEBATE", exact match, once. The chapter
   additionally carries: the labour-wealth passage (§Social structures: herds beyond a certain
   size "cannot be managed with household labour alone"), "fluid systems that are hard to pin
   down", the common-property *debates* framing, and the weak-external-exclusion sentence
   (farmers "can come and cultivate the land that herders regularly use for grazing their
   stock, without having to ask for permission"). It carries **no** privatisation, route-closure
   or movement-access material, and **not** the phrase "not open access" — so P1 and P3-d have
   been corrected accordingly above. Two sibling findings from that seat touch this entry but
   sit outside §8: `:155` (§11) asserts a herd ceiling "set by labour **and disease**" — the
   chapter never says "disease" (unsourced under criterion 1) — and `:22`/§3 place hired
   labour only at the ranch boundary although S049 documents hired labour (and formerly
   slavery/vassal castes) as how herds grow past household-labour capacity.

---

## 5. Smallest patch set (author lane, not applied here)

| # | file:line | change |
|---|---|---|
| 1 | `pastoralism-animal-husbandry.md:118` | drop "privatisation and route closure" and "never" (or mark them `(to-verify)` — **not** on S049: the chapter carries no privatisation/route material, per `ReopenS049.md`) |
| 2 | `pastoralism-animal-husbandry.md:110` | mark the route/water/pasture decomposition `(to-verify)` (S049 does not carry it); quote S049's full sentence so "thus" keeps FAO's anaphor |
| 3 | `pastoralism-animal-husbandry.md:31` | agrarian row → "parcel, plough, **water, tenure**, stubble grazing, manure contract (`agrarian-field-system-lexicon.md:33`)"; add the pastoral/agrarian water-and-tenure line to §8 `:110` |
| 4 | `pastoralism-animal-husbandry.md:116` (and `:77`) | "a **Swedish** Sámi earmark"; ":116" → "**usually personal** (a sameby may hold one)"; Status → "B — the Swedish Sámi register only (not Norwegian law)" |
| 5 | *(optional, non-blocking)* `corpus/SOURCES.md:88` | widen the S059 anchor to "H1 ingress + first body paragraph, before 'Vem kan äga ett renmärke?'" — **only as a superseding row with its own Gate bullet** (`corpus/SOURCES.md:9-12`); not required for admission |
| 6 | `pastoralism-animal-husbandry.md:34` | `transport-mobility-lexicon.md:95` → `transport-mobility-lexicon.md:92,:95` |
| 7 | `pastoralism-animal-husbandry.md:115` | add the reason to the Ostrom status cell; drop or `(to-verify)` "rotas" |
| 8 | `pastoralism-animal-husbandry.md:64` | drop `,:150` from the reindeer cell |
| 9 | `pastoralism-animal-husbandry.md` §8 | carry the **literal** S049 material only ("fluid systems that are hard to pin down"; the weak-external-exclusion sentence) — **never** "not open access" (not in the chapter, per `ReopenS049.md`); add one mobility-rights row marked `(to-verify)` unless a movement-access source is registered |

---

## 6. Bottom line

§8's **Hardin, Ostrom and earmark rows hold** — quote-faithful, scope-correct, calibrated
against `calibration-registry.md:35-39`, criterion-6 clean (no 1990 book quoted, no
publisher description laundered), canon-clean. The earmark row's underlying facts were
re-verified live on 2026-10-21 by `ReopenS059-21` (all three assertions verbatim on
sametinget.se/renmarken) — so §8 is **not** an overclaim there; what fails is the entry's own
wording: "a Sámi earmark" (dropping the Swedish-only scope the row registers) and "is
personal" (omitting the sameby holder class), plus a Status cell that names neither — P2-c is
therefore an **entry-text** fix of two qualifiers, not a registry correction (the row's anchor
is one paragraph narrow, a non-blocking nit under `corpus/SOURCES.md:9-12`). The
**sentence-level scaffolding of §8 does
not hold**: `:118` claims two things its anchors do not say (P1), `:110` asserts an uncited
tenure fact and mis-anchors a quote's anaphor (P2-a), §8's water/tenure claim collides with
`agrarian-field-system-lexicon.md:33` without disclosure (P2-b), `:116` drops the population
bound its own source registers (P2-c), and the section's title over-promises against its
content (P3-d). Section 8 therefore reads **PARTIAL**, not BROKEN: the framework rows that
carry the round's coverage claim are sound, and every defect above is a prose/anchor
correction that does not disturb the table's architecture.

**Two of the four §8 external rows are now independently re-opened live and consistent with
this report** — S059 (`ReopenS059.md`: row HOLDS; the entry's two qualifiers are the whole
defect) and S049 (`ReopenS049.md`: §8's citation `:110` supported; the chapter carries no
privatisation/route material and **not** the phrase "not open access", so P1 and P3-d's fixes
were corrected to import only its literal material). The two §8 rows still resting on a Gate
quote alone are S054 and S055 (residuals 2 and 3 above).

*(Verification note: all file reads are from the landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`
via `/tmp/k50sec08-XXXX`; `git diff --name-only 4ad2683 1c779e4a -- corpus/knowledge/` shows the
only corpus-knowledge change is the new entry, so all in-corpus anchors quoted above are
byte-stable across base→landed. The temporary clone was deleted after the run. No lane file,
git index, jj state, MANIFEST.json or `.ufo/state` was written; the only file written is this
report. The S059 and S049 live re-opens were performed by seats `KotodamaR50-2.ReopenS059-21`
and `KotodamaR50-2.ReopenS049-21` and handed to me over IRC; I did not re-open those URLs
myself, and I have cited their reports only where they bear on §8.)*
