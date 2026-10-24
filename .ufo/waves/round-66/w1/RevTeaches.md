# RevTeaches — teaches-cell overreach vs anchor quote (S777–S800)

Seat: L1-kotodama-r66.RevTeaches (reviewer, axes coverage+calibration). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `94209e8f`. Read-only: no lane
jj/git writes, no commits. Tool installs: none (no uv/pacman/npx used).

## Question and test

For each new row S777–S800: does the teaches cell add a claim the anchor quote does not
carry? The test applied is directional — **quote ⇒ teaches**, not teaches ⇒ quote:

1. List the assertions the quote itself licenses (subject, predicate, qualifiers).
2. List the assertions in the teaches cell (cell 7 of the `ROW=` line).
3. Any teaches assertion not licensed by the quote is an **added claim**. Severity by what
   the added claim does to the row's use:
   - **H** — the teaches' load-bearing claim (what the row is cited for) is not in the
     quote, or the quote is referentially incomplete/agnostic so nothing specific is
     anchored (dangling anaphora, generic boilerplate, sub-floor fragment).
   - **M** — teaches adds substantive unquoted claims (species, ranks, dates, numbers,
     institutional claims, interpretive theses) that the page may carry but the frozen
     Gate quote cannot re-verify.
   - **L** — only identity/context gloss, or elaboration independently verified on the
     page (recorded as verified, not as overreach).

Evidence base: the 20 in-scope fragments on disk at review time (08:41), quoted below with
their full cells. Commands: `find .ufo/waves/round-66/rows -name 'row-S*.txt'`; cells parsed
exactly as `reports/round-66/accept-c.py:cells()`; quote extracted with the counter's own
`anchor_quote()` regex. Page spot-checks by `curl` (S790 capture, S793 live).

## Verdict summary

Reviewed: 20 of 24 (S779, S780, S781, S782, S783, S784, S785, S786, S787, S788, S789,
S790, S791, S792, S793, S794, S795, S796, S799, S800). Not on disk when the time-box closed:
S777, S778, S797, S798 (dependency finding D-1).

| Row | Sev | Added claim(s) the quote does not carry |
|---|---|---|
| S779 | M | Greek⇐kapet etymology and gloss “a substance to be smoked”; “some sixteen ingredients”; “defying modern recreation” |
| S780 | M | South Arabian merchants; frankincense/myrrh/luxury goods actually moving on the route; Strabo and Pliny citations (quote is pure geography) |
| S781 | **H** | vessel inventory (alabastron, aryballos, lekythos, plemochoe, unguentaria); “Greek perfume meant scented olive oil” (quote: olive oil *a* base); “status”; design directive “worlds can borrow” |
| S782 | **H** | Avicenna (d. 1037); “true attar – separated rose essential oil”; Jahangir’s court 1611–12 — the entire calibration half of the cell |
| S783 | **H** | Hungary water name; c.1370; rosemary base; Italy’s c.1320 serpentine cooler; commercialisation — quote is a 3-word fragment |
| S784 | **H** | Grasse; cultivation of perfume plants, processing of raw materials, art of composition — quote is element-agnostic UNESCO boilerplate |
| S785 | M | copal chino / *Bursera bipinnata*; feast list (sun, earth, water, fire, wind, war); “INAH-affiliated” — quote opens on a dangling “its” |
| S786 | M | “mostly local scents individually in religious contexts”; “secular usage”; “seasonal osmographies” |
| S787 | M | functional glosses (anoints, fumigate, burn); thesis “puja fragrance is a staged system, not a single incense”; “vrata”/“puja” |
| S788 | M | “Suyá”; “life-stage”; “natural and symbolic odors”; thesis “smell operates as a social classification system” |
| S789 | M | water-**steam** distillation; cohobation; “IRAP, Kazanlak” (quote carries only yield + water distillation) |
| S790 | L | doeskin, “odour-masking”, “Ownership & Use” — **page-verified** on the V&A capture; not quote-carried |
| S791 | M | pomander definition and neck/waist suspension; “Lightbown’s 1287 amber-apple record” (unquoted date) |
| S792 | **H** | Flower Mountain paradise thesis; Maya palace aromas marking breath and soul; Sahagún; “opening course” banquet claim — quote is a dangling “as Spanish observers recorded it” |
| S793 | M | whale origin; “prized white varieties most” (severed by quote truncation); ambrein as fixative; synthetics replacing it |
| S794 | M | “seized the perfumer’s métier, took its monopoly”; scented waters and cosmetics; “courtiers whose curial etiquette demanded them”; “Parisian” |
| S795 | **H** | fire clocks replacing clepsydrae when water froze or failed; sticks marked into intervals; seal templates; hanging cords with gong balls; “across East Asia” — quote is a couplet carrying only the principle |
| S796 | **H** | Ibn Baḥshāl on Wāsiṭ; Umayyad period; ‘aṭṭārīn fragrance shops beside grocers; rulers planning retail quarters — quote is generic commodity zoning |
| S799 | M | mid-Edo 18th-c. dating; makie; silver/ivory/tortoiseshell tools (gameplay claim itself is quoted) |
| S800 | L | Monteix catalogue and BMCR review attribution; “equipment reading, not a label” (perfume-press claim itself is quoted) |

Count: 7 H, 11 M, 2 L. **18 of 20 teaches cells add claims the anchor quote does not
carry.**

## Per-row detail (quote ⇒ teaches)

**S779 (M)** quote: “The most famous of all scents was kyphi, known from three versions on
temple walls (two at Edfu, one at Philae), from papyri (P. Ebers)”. Licensed: kyphi was the
most famous scent; three wall versions (2 Edfu, 1 Philae); P. Ebers. Teaches adds etymology
(Greek⇐kapet), the gloss “a substance to be smoked”, the count “some sixteen ingredients”
and “defying modern recreation”. The count and the recreation claim are the row's most
citable specifics and neither is in the quote. Disposition: drop the count or add a second
quoted span carrying it.

**S780 (M)** quote: “The Incense Route ran along the western edge of Arabia’s central desert
about 100 miles inland from the Red Sea coast”. Licensed: route geography only. Teaches'
central claim — merchants shipped frankincense, myrrh and luxury goods — is carried by the
scope cell and source title, not by the quote; Strabo/Pliny are additional unquoted
citations. Disposition: the anchor should be the sentence that names the commodities.

**S781 (H)** quote: “Beyond its culinary uses, olive oil served as the base for perfumes,
cosmetics, and medicines”. Licensed: olive oil was a base for perfumes/cosmetics/medicines.
Teaches adds five vessel names, a status frame, and the identity “Greek perfume **meant**
scented olive oil” (a base is not a definition), plus the worldbuilding directive. The
fragment's BULLET goes further — “Athletes carried small flasks of scented olive-oil base
into the gymnasium” — which shares only `olive`/`base` with the quote and therefore **fails
RESTATE as written** (`inq=2` < 3); the repair the counter invites (insert a third quote
word) leaves the gymnasium/athletes invention intact. Verified by re-running the counter's
own functions: quote content words {beyond, culinary, uses, olive, served, base, perfumes,
cosmetics, medicines}; bullet content words {athletes, carried, small, flasks, scented,
olive, base, gymnasium}.

**S782 (H)** quote: “large quantities of rose-water were regularly distilled in Persia and
Iraq at least from the ninth century”. Licensed: regular rose-water distillation in
Persia/Iraq from the 9th c. Teaches spends half its budget on claims outside that: Avicenna's
death date, the definition of true attar, and the move to Jahangir's court 1611–12. The
“calibration” the cell performs cannot be checked from the frozen quote at all. Disposition:
quote the Iranica sentence that carries the attar/Jahangir chronology, or cut that half.

**S783 (H)** quote: “first-named, alcohol-based perfume,” — three body words (four
whitespace tokens), trailing comma, syntactically incomplete. This is below the row format's
own 8–25 body-word floor and it licenses only the compound “first-named alcohol-based
perfume”. Every other element of the teaches cell (Hungary water, c.1370, rosemary, the c.1320
serpentine cooler, commercialisation) is unquoted. Disposition: reject/redo the fragment; the
quote must be a complete clause of ≥8 body words.

**S784 (H)** quote: “Inscribed in 2018 (13.COM) on the Representative List of the Intangible
Cultural Heritage of Humanity”. Licensed: some element was inscribed in 2018. The quote is
element-agnostic — it does not name Grasse — so the teaches' Grasse content (perfume-plant
cultivation, raw-material processing, composition) is entirely unanchored. Disposition: anchor
on the element title/decision sentence that names Pays de Grasse.

**S785 (M)** quote: “its aromatic smoke, that was also considered divine food, allowed the
link between deities and humans”. Licensed: aromatic smoke = divine food = link between
deities and humans. The quote's subject is a dangling “its” (copal appears only in the
teaches and source title). Teaches adds the species, the six-way feast dedication list, and
the “INAH-affiliated” attribution. Disposition: extend the quote left to include the resin
name, or move the feast list behind a second quote.

**S786 (M)** quote: “elite scent culture had already begun to be transformed by the
importation of foreign aromatics”. Licensed: transformation by imported aromatics had begun.
Teaches adds the prior-practice characterisation (“mostly local scents individually in
religious contexts”), the “secular usage” outcome, and “seasonal osmographies”. The
before-Buddhism timing is in the source title, not the quote. Disposition: keep the timing
claim only if the quote carries it.

**S787 (M)** quote: “sandalwood paste, incense, pastille, camphor, lamps of burning oil or
ghī, and fragranced flowers to the deity”. Licensed: the offering list. Teaches adds ritual
verbs (anoints, fumigate, burn) and the interpretive thesis “puja fragrance is a staged
system, not a single incense”. The thesis is the cell's contribution and is not quote-carried.
Disposition: acceptable only if the row states the thesis as the reviewer's reading, or the
quote carries a staged-sequence sentence.

**S788 (M)** quote: “Men are socialized through initiation and lose their strong-smelling
odor. Women, on the other hand, by their very sexuality are strong smelling.” Licensed: the
sexed odour asymmetry. Teaches adds the ethnonym “Suyá”, “life-stage”, “natural and symbolic
odors”, and the general thesis that smell is a social classification system. Disposition: the
generalisation outruns a two-sentence quote about one people.

**S789 (M)** quote: “More than 3000 kg of rose flowers produce 1 kg of rose oil by water
distillation.” Licensed: the yield ratio and water distillation. Teaches adds water-**steam**
distillation, cohobation, and the IRAP/Kazanlak line. Low risk (technical detail from the
same paper) but unquoted. Disposition: none required if the L1 accepts page-level support;
record the extra terms in ACCESS/VERIFY if kept.

**S790 (L)** quote: “Recipes for scenting gloves survive from the 17th century using
ingredients such as musk, ambergris, floral extracts and aromatic spices.” Page-verified on
the named capture (`https://web.archive.org/web/20260108224147id_/https://collections.vam.ac.uk/item/O78794/pair-of-gloves-unknown/`,
HTTP 200, quote present verbatim in body). The teaches' extras (doeskin, “Ownership & Use”,
odour-masking) are all present on that page — “masking of body odours rather than washing them
away”, “Pair of brown doeskin gloves, England, 1660s”. Not quote-carried, so not re-verifiable
from the Gate, but not false. Disposition: pass.

**S791 (M)** quote: “strong-scented substances had the power to disinfect the air and to ward
off plague and other diseases”. Licensed: the belief that strong scents disinfect air and ward
off plague. Teaches adds the pomander object definition, neck/waist suspension, and the
“Lightbown's 1287 amber-apple record” date. Disposition: the 1287 figure is a specific that
must be quoted or dropped.

**S792 (H)** quote: “como lo registraron observadores españoles con respecto a los palacios
aztecas de Centroamérica en el siglo XVI” (“as Spanish observers recorded it, regarding Aztec
palaces in Central America in the 16th century”). Licensed: only that Spanish observers
recorded something about 16th-century Aztec palaces. The quote's object (“lo”) is outside the
excerpt, so the anchor is referentially empty. Teaches then supplies everything: Flower
Mountain paradise, breath/soul marking, incense and breeze, Sahagún, and the banquet
“opening course”. Highest overreach in the set. Disposition: replace with a self-contained
sentence naming flowers/scent and its claim.

**S793 (M)** quote: “For hundreds of years, perfumers have categorised the quality of
ambergris according to its colour”. Live page (HTTP 200) shows the full sentence continues
“…, with the finest perfumes made from pure white varieties” — i.e. the clause that carries
“prized white varieties most” was **cut by the quote's word budget**. The teaches' remaining
extras (whale origin, ambrein as fixative, synthetics in all but the most expensive perfumes)
are page-carried but not quote-carried. Disposition: accept the row; do not treat “white
varieties” as quote-anchored. Separate durability finding D-2: the named capture
`web.archive.org/web/20261013203536id_/…what-is-ambergris.html` returned **HTTP 000 / 0
bytes on two attempts** while the live URL answered 200 — CAPTURE would still PASS because it
matches the URL pattern. That is the R65-D1 class again and must be resolved before freezing.

**S794 (M)** quote: “les gantiers-parfumeurs fabriquent les gants parfumés, dont le succès est
à son apogée à la cour de Louis XIV” (“the glover-perfumers make scented gloves, whose success
peaked at Louis XIV's court”). Licensed: glover-perfumers make scented gloves; peak at Louis
XIV's court. Teaches adds the seizure of the perfumer's métier and its monopoly, scented waters
and cosmetics, courtier etiquette, and “Parisian”. The monopoly is in the scope cell, not the
quote. Disposition: quote the sentence that carries the guild privilege, or mark the monopoly
as scope-level.

**S795 (H)** quote: “By burning incense [we] know the passage of the night, With graduated
candle [we] confirm the tally of the watches.” Licensed: burning incense gives the passage of
the night; a graduated candle confirms the watches. Every mechanism the teaches cell is cited
for — sticks marked into intervals, seals burned along template paths, cords releasing gong
balls, fire clocks replacing clepsydrae when water froze or failed, East Asian spread — is
outside the quote. The bracketed “[we]” also marks a reconstructed translation, so even the
couplet's wording is editorial. Disposition: quote the mechanism sentence (Bedini describes
the seal-and-cord apparatus explicitly), or restrict the teaches to the principle.

**S796 (H)** quote: “designed them to function as a set of defined zones for various
commodities and the streets took on the name of the trade plied there”. Licensed: commodity
zoning and trade-named streets. The row's whole reason to be in a scent register — ‘aṭṭārīn
fragrance shops beside grocers — is not in the quote, nor are Ibn Baḥshāl, Wāsiṭ, the Umayyad
dating, or the planning thesis. Disposition: anchor on the sentence that names the perfume
sellers, else the row documents generic sūq zoning, not a scent institution.

**S799 (M)** quote: “In these games, over several rounds, a host selects varieties of incense
for their guests to savor and identify.” Licensed: multi-round games; host selects incense
varieties; guests savor and identify. This is the best-aligned quote in the set — the gameplay
claim is fully carried. Extras are object-level: mid-Edo 18th-c. dating, makie lacquer, and the
silver/ivory/tortoiseshell tool list. Disposition: pass the teaches' core; move the dating and
materials to scope/ACCESS or quote the catalogue line that dates it.

**S800 (L)** quote: “it was an oil press for the production of perfume and not a textile
press”. Licensed: the workshop's press was reinterpreted as a perfume-oil press, not a textile
press. Teaches' claim is carried; extras are the Monteix catalogue and BMCR review
attribution, the workshop number (also in scope), and the gloss “equipment reading, not a
label”. Note for RevGateRows/RevSourceSupport: the anchor is a review's paraphrase of
Monteix, i.e. a second-hand anchor — the tier-A row rests on BMCR's summary, not on the
catalogue itself. Disposition: pass as a teaches/quote pair; flag the secondary anchor.

## Structural findings (why this class is systematic, and what the instrument misses)

**S-1 (HIGH, instrument): the frozen counter cannot fail on teaches overreach.**
`reports/round-66/accept-c.py` RESTATE (lines 224–248) compares the *entry bullet* to the
quote (`inq`) and to the teaches (`cov`, `novel`). No leg compares teaches to quote. A teaches
cell may assert anything; ACCEPT-C-66 still prints PASS. Claim C's “sourced” leg therefore
rests entirely on blind review, and this report is that review for 20 rows.

**S-2 (MED, incentive): RESTATE rewards teaches inflation.** `cov = in_order_coverage(teaches,
bullet) < 0.8` gets easier as the teaches cell grows, and `novel = bullet words not in teaches`
gets easier too. Padding the teaches cell (vessel lists, feast lists, dates) mechanically
helps the bullet pass while adding unquoted claims — exactly the cells graded M/H above
(S781, S782, S785, S792).

**S-3 (MED, format): the 8–25-word quote cap severs referents, and the teaches then supply
them.** Direct evidence: S783 (3-word fragment), S785 and S792 (dangling anaphora: “its”,
“lo”), S793 (the white-variety clause cut), S795 (a couplet plus a bracketed reconstruction
standing in for the apparatus description). The row spec's cap and the teaches' 240-char
budget are in tension; when they conflict, the teaches silently carries the load and the Gate
freezes only the truncated quote.

**S-4 (LOW, calibration): the same defect shipped in round 65, so the base rate is not
zero.** Base rows parsed from `corpus/SOURCES.md` (701 rows): S760 quote “Today historians no
longer think that the Greek athletes were amateurs” → teaches “Worldbuilders can show athletic
prestige continuing into civic life beyond the festival's finish” (no support); S761 quote on
pitz as political/religious/social → teaches a design directive (“Use ball courts as civic
spaces…”); S762 teaches a c.1600 BCE date absent from its quote; S767 teaches “earlier than
known Old World dice”; S768 teaches “Victorian”, “six-sided”, the pot rule and the dreidel
comparison from a quote giving only four letters; S772 teaches “no weapons” and stamping that
“drives evil” from a quote covering only claps and palms. If S777–S800 repeat this style the
entry inherits an unsourced register, not a sourced one.

## Dependencies and residual risk

- **D-1 (dependency, coverage):** four in-scope fragments were still absent at the time-box:
  S777, S778, S797, S798. Their teaches cells are unreviewed. High-risk scopes by the same
  mechanism: S777 (UNESCO listing quote will be boilerplate like S784), S797 (anointing
  practice), S798 (vessel typology — a collection record that will outrun any short quote).
  The L1 should re-run this test on those four before integration; the rubric above is
  mechanical enough to apply directly. If they land with the same shape as S784/S792, expect
  two more H grades.
- **Residual risk:** for the 11 M-graded rows the page probably carries the extra claims; I
  verified only S790 (all extras present) and S793 (all extras present, quote truncated). The
  other M grades are “unquoted but plausible”, not “false”. Severity would rise to H if any
  extra claim is not on its page.
- **Verification gap:** I did not fetch every source. Quotes unverified for presence in body:
  S779, S780, S781, S782, S783, S784, S785, S786, S787, S788, S789, S791, S792, S794, S795,
  S796, S799, S800. Quote presence in body is a VERIFY-cell claim, not a counter leg; a
  fabricated or mis-transcribed quote passes CAPTURE/RESTATE. That check belongs to
  RevSourceSupport, and it is the precondition for every verdict above.
- **Verdict:** claim C should not be admitted while S781, S782, S783, S784, S792, S795 and
  S796 stand as written (H); S783 additionally violates the row's own 8–25-word quote floor
  and S795's anchor is an editorially bracketed translation. S779, S780, S785, S786, S787,
  S788, S789, S791, S793, S794, S799 need a quoted second span or a trimmed teaches before the
  Gate is frozen; S790 and S800 pass on this axis (S800 with a secondary-anchor note).
