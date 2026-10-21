# Frontier source open — Khazanov, *Nomads and the Outside World* (2nd ed. 1994)

Seat: `ChousaR27R2.SrcKhazanov-4` (scout, leaf). Round 50, claim C (coverage /
pastoralism entry). Base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Read-only: no lane file touched, no clone, no patch (scout seat, not executor).

## Assigned item

Open the University of Wisconsin Press page for Anatoly Khazanov, *Nomads and the
Outside World*, 2nd ed. 1994, and quote its description of nomad-sedentary
interdependence (tier B blurb); return a SOURCES candidate (URL, access date
2026-10-21, kind, tier + reason, scope, ≤25-word verbatim quote with location, what it
teaches the entry and which section, recheck cadence).

## Result — the page opens, but the premise does not hold

The page is reachable and was opened natively this session. **Its Description section
contains no statement of nomad-sedentary interdependence.** The served HTML has **zero**
occurrences of `sedentary`, `interdepend` or `symbio` (`curl -sL`, 62,773 bytes,
2026-10-21). The Description's review excerpt calls the book a comparative survey and a
challenge to the "nomadic feudalism" orthodoxy; neither the publisher's own prose nor the
excerpt states the thesis the section brief needs.

| Fact | Evidence |
|---|---|
| Page opens, canonical URL | `https://uwpress.wisc.edu/Books/N/Nomads-and-the-Outside-World`; page title "Nomads and the Outside World — University of Wisconsin Press" |
| Edition identity | Paperback `9780299142841`, 442 pages, 6 x 9 inches, May 1994; translated by Julia Crookenden; foreword by Ernest Gellner (Show Details block) |
| Publisher Description, first sentence | "Hailed by reviewers as “majestic and magisterial,” *Nomads and the Outside World* was first published in English in 1984." |
| Publisher Description, only content claim | the Ingold review excerpt: the book "sets out to challenge the orthodox view of nomadic feudalism and, in the process, has produced the first comparative survey of pastoral societies that can claim to be truly comprehensive, covering their history in Eurasia, the Middle East, and Africa from the origins of pastoralism to the dawn of the modern era." |
| Reviews block | "This is the first paperback edition of Anatoly M. Khazanov's famous comparative study of pastoral nomadism." |
| Interdependence wording | **absent** — 0 hits for the three stems sedentary, interdependence, symbiosis in the served HTML; the title's "Outside World" is the only trace of the relation |

I did not invent the requested sentence. A row that quoted an interdependence thesis
from this page would be the r49 failure mode in a new place: citing a source for what its
label promises instead of what its bytes say.

The book body is also not reachable by the routes tried here: Google Books' about page
was opened but reproduces the same publisher copy and bibliographic data, with no
readable body text in the fetched page; the Internet Archive item timed out; Cambridge
Core returned HTTP 429. So the 1994 book's own argument remains `(to-verify)` beyond the
publisher's characterization and Khazanov's later restatements.

## Candidate 1 (the assigned source): University of Wisconsin Press page

Exact 11-column registry shape per `corpus/SOURCES.md:28`. Id is L1's to assign
(S048 is already proposed by other seats; next free is later).

```
| S??? | Khazanov 1994, Nomads and the Outside World, 2nd ed., University of Wisconsin Press, trans. Julia Crookenden, foreword Ernest Gellner — https://uwpress.wisc.edu/Books/N/Nomads-and-the-Outside-World | book | B | the book's programme and coverage as its publisher states it — a comparative survey of pastoral societies across Eurasia, the Middle East and Africa from the origins of pastoralism to the modern era, framed against the orthodox "nomadic feudalism" thesis; 2nd-edition identity (ISBN 9780299142841, 442 pp., May 1994). Not its argument, evidence, page-level claims, or any nomad-sedentary interdependence thesis — the page states none | publisher Description section, first review excerpt attributed to Tim Ingold, Current Anthropology; Show Details block for ISBN 9780299142841, 442 pages, May 1994; served HTML contains 0 occurrences of sedentary, interdepend or symbio (curl, 62,773 bytes, 2026-10-21) | pastoralism as a comparative, historically deep phenomenon across three continents rather than one local type; the book is framed against a stage-model "nomadic feudalism"; the page is a scope anchor only — cite it for the survey's existence and coverage, never for §9's interdependence thesis | queued | 2026-10-21 | 365d | — |
```

### Verbatim quote (≤25 words) and its location

> "the first comparative survey of pastoral societies that can claim to be truly
> comprehensive, covering their history in Eurasia, the Middle East, and Africa"

24 words. Location: **Description section, first review excerpt**, attributed on the page
to Tim Ingold, *Current Anthropology*. Read 2026-10-21 at the URL above.

A second, publisher-voice quote for identity only (17 words): "This is the first
paperback edition of Anatoly M. Khazanov's famous comparative study of pastoral
nomadism." Location: **Reviews** block.

### Tier and scope — why B

`B`, per `corpus/QUALITY.md:29` (criterion 6): a publisher description and a
publisher-selected review excerpt are strong secondary for claims *about the work*, never
primary for its argument. Scoped to the book's programme, coverage and edition identity.
It is **not A** for any substantive pastoralism claim and **not C** — it is a usable
orientation and scope anchor.

### What it teaches the entry, and which section

- **§1 register property** (the section that opens the entry; see the model at
  `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:25`): pastoralism is
  a comparative, historically deep phenomenon across Eurasia, the Middle East and Africa,
  not one local type — the book is the field's classic comparative survey.
- **§2 one-owner boundary**: the book's frame is "nomads and the outside world", and the
  Description's review excerpt says it challenges "nomadic feudalism" — a stage-model the
  entry should name and refuse, not reproduce.
- **§9 pastoral-sedentary relations**: **not usable for the thesis.** Cite it at most for
  the fact that the book takes the nomad/outside-world relation as its frame; the
  interdependence claim needs the supplement below.

### Recheck cadence

`365d`. A fixed 1994 publisher page cannot churn in substance; recheck only to catch a
retitled URL or a changed description.

## Candidate 2 (recommended supplement): Khazanov's own comments in the Reichert sample

The §9 brief is explicit: "Pastoral-sedentary relations: interdependence (Khazanov),
trade, tribute, conquest states, raiding; avoid 'barbarian' stereotyping"
(`.ufo/waves/round-50/build-spec.json:450`). Candidate 1 cannot support that sentence.
This publisher sample can: it reproduces Khazanov's own printed comments, with page
numbers, and — critically — his qualification of the interdependence thesis.

```
| S??? | Khazanov's comments in Paul (ed.) 2013, Nomad Aristocrats in a World of Empires (Nomaden und Sesshafte 17), Reichert Verlag, pp. 17–22 — sample PDF — https://reichert-verlag.de/media/pdf/9783895009754_sample.pdf | book | A | Khazanov's own stated position in the publisher's printed sample, pp. 17–22: the material asymmetry of the nomad-sedentary relation (trade, exchange, tribute, agricultural and craft procurement), nomadic states as connected with asymmetrical relations with sedentary societies and their exploitation, and his explicit qualification of the stronger "one and the same system" claim; not the volume's other chapters, not the 1994 book, not any page outside the sample | sample PDF pp. 17–22, "AKh comments" blocks at p. 18 and p. 22; volume metadata from https://reichert-verlag.de/en/9783895009754_nomad_aristocrats_in_a_world_of_empires-detail/ (ed. Jürgen Paul, 2013, 208 p., series Nomaden und Sesshafte 17, ISBN 9783895009754) | interdependence is material and asymmetric: trade, exchange, tribute and procurement of agricultural and craft products were crucial to nomads, and the emergence and features of nomadic states were connected with asymmetrical relations with sedentary societies and the exploitation of them; but Khazanov rejects the stronger claim that nomads and sedentaries always formed one economic and political system, and doubts that steppe nomads had more in common with sedentary partners than with other nomads. Feeds §9 (interdependence, trade, tribute, conquest states) and the §1/§13 caution against "pure nomads", ideal types and ecological determinism | queued | 2026-10-21 | 365d | — |
```

### Verbatim quotes (≤25 words) and locations

Row quote:

> "It is true that trade, exchange, tribute, and other ways of procuring agricultural and
> craft products were crucial for the nomads"

21 words. Location: **p. 18**, first "AKh comments" block, first paragraph (PDF page 2).

Second quote for §9's conquest/tribute paragraph:

> "the emergence and characteristic features of nomadic states were connected with
> asymmetrical relations between the nomads and sedentary societies"

19 words. Location: **p. 22**, "AKh comments" on item 7, opening sentence (PDF page 6).

Qualification the entry **must** carry (do not quote the thesis without it):

> "I am not sure that nomads of the Eurasian steppes and their sedentary counterparts
> always formed a single economic and political system."

22 words. Location: **p. 18**, same first comment, immediately before the row quote.

### Tier and scope — why A

`A`, scoped to *Khazanov's own comments as printed in this publisher sample, pp. 17–22*.
This is not a blurb or abstract: the sample is a facsimile of the printed chapter, and the
quoted sentences are the author's own text. It is **not A** for the 1994 book, for the
volume's other chapters, or for pastoralism outside the Eurasian steppe. If L1 reads
criterion 6 conservatively for any publisher-hosted PDF, `B` is the fallback; the text's
authority for these sentences is unaffected.

### What it teaches the entry, and which section

- **§9 (primary)**: the relation is material and asymmetric. Nomads needed agricultural
  and craft products; trade, exchange and tribute were the procurement channels; nomadic
  states' emergence and features were tied to asymmetric relations with sedentary
  societies and their exploitation. This supports a §9 that presents trade, tribute,
  raiding and conquest as strategies inside one relationship, not as a "barbarian"
  essence — and it supplies the counterweight: integration was variable, not universal.
- **§1/§3**: "practically no 'pure' nomads"; mixed strategies (caravan leaders, soldiers,
  raiding, protection money, some agriculture, trade); no ideal type. The SFB statement
  the comments address says this at p. 17; Khazanov agrees with the definition and the
  "no ideal type" claim at p. 18.
- **§5/§13**: settlement-based transhumance vs mobile pastoralism, and the archaeological
  ambiguity between seasonal camps and settlement-based shepherds' camps (p. 20) — a
  calibration caution for any entry claim that material culture proves mobile nomadism.
- **§13**: "pastoral nomadism originally emerged as an alternative to cultivation only in
  those regions where the latter was impossible, or economically less profitable"
  (22 words; p. 19) — the anti-ecological-determinism caveat, with Khazanov's own
  reservation that the SFB's anti-determinism can be overstated.

### Recheck cadence

`365d`. The 2013 print is fixed; recheck the PDF URL, which can move on a publisher site
redesign.

## Optional third opened primary text: Khazanov 2019, steppe trade

Opened and useful, but not required for the assigned item. The article is Khazanov's own
later restatement of the non-autarky thesis and cites Khazanov 1994 for it.

```
| S??? | Khazanov 2019, Steppe Nomads in the Eurasian Trade, Chungara Revista de Antropología Chilena (AOP), doi 10.4067/S0717-73562019005000302 — https://www.chungara.cl/Vols/2019/AOP/AOP-KHAZANOV.pdf | paper | A | Khazanov's own 2019 statement of steppe nomads' economic non-autarky and their trade with sedentary societies; not the 1994 book, not the sedentary side, not other nomadic regions | abstract sentence 2 and PDF p. 3, "In principle, the trade between nomads and sedentary peoples was beneficial for both sides"; published online 2019-03-01; PDF opened 2026-10-21 | the specialized, non-autarchic pastoral economy created a standing need for external agricultural and craft products; nomad-sedentary trade was structurally beneficial to both sides, and nomadic rulers' political economy (tribute, gifts, luxury redistribution) belongs to the same relation. Feeds §9's trade and tribute paragraphs | queued | 2026-10-21 | 365d | — |
```

Quote: "The specialized and non-autarchic character of their economy, provoked that the
nomads always experienced a need for external agricultural and handicraft products."
22 words. Location: abstract, sentence 2 (PDF p. 1). The grammar is the article's; quote
verbatim, do not silently correct it.

## Author-lane advice for claim C (not admission)

1. **Do not** write "Khazanov (1994) argues that nomads and sedentaries were
   interdependent" on the strength of the publisher page. That sentence is not on the
   page. Use candidate 2 for the thesis and candidate 1 for the book's scope.
2. The calibrated §9 sentence the opened evidence supports: *pastoral nomads depended on
   sedentary economies for agricultural and craft goods, with trade, exchange and tribute
   as the procurement channels; nomadic states formed through asymmetric relations with
   sedentary societies — but the degree of integration varied, and Khazanov explicitly
   denies that the two always formed a single system.* Make integration a design
   variable, not a universal.
3. Keep the "barbarian" caution structural: raiding, tribute and conquest are strategies
   within an asymmetric relationship, not evidence of a nomadic essence. Candidate 2's
   "asymmetrical relations ... and specific forms of exploitation" is the sentence to
   build on; it is not a moral verdict on nomads.
4. Every cited S-id must end with `used-by` naming
   `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (claim C's
   after-required check). These rows are proposed `queued`; flip to `mined` only when the
   entry actually cites them, and do not cite a row for a claim its scope excludes.

## Mined-mistake candidate for `corpus/lessons/round-50.md`

Dispatched to quote a publisher blurb's "description of nomad-sedentary
interdependence"; the page opens but prints no such description. The trap is quoting the
thesis the title promises instead of the sentence the page serves. Fix: quote only served
text; when the assigned source lacks the needed claim, register it for what it does say
and open a text that states the claim (here, Khazanov's 2013 comments in the Reichert
sample), rather than stretching the blurb. This is the r49 pattern in a new place: a
citation whose content was assumed from its label.

## Unrun checks / bounds honoured

- Did not run the entry's gap sweeps or `reports/round-28/readme/sweep.py` — claim C's
  executor and the verifier own those.
- Did not open the 1994 book body. Attempts: Google Books about page (no preview;
  publisher copy only), Internet Archive item (timed out), Cambridge Core (HTTP 429).
  The book's own argument therefore stays `(to-verify)` beyond the publisher's
  characterization and Khazanov's later restatements.
- Did not edit `corpus/SOURCES.md`, assign an id, or write the round lesson — L1 owns
  integration, id assignment and the lesson.
- No lane file, clone, patch, git index or jj state touched; nothing written under
  `/home/vgpnk/Projects/shokunin/.ufo`.
- No installs required or attempted (no `pacman` transaction; host-wide pause respected);
  no tool/version/channel to record.
