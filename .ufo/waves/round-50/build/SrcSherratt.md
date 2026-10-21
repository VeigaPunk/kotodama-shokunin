# SrcSherratt — frontier source for claim C: Sherratt's secondary products revolution

Seat `ChousaR27R2.SrcSherratt-4` (scout, leaf). Round 50, claim C (coverage / pastoralism
entry). Base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only: no lane file touched, no
clone, no patch (source seat, not executor); nothing written under
`/home/vgpnk/Projects/shokunin/.ufo`.

## Assigned item

Open an authoritative page for Andrew Sherratt's secondary products revolution (1981/1983)
that states the thesis (milk, wool, traction), and return one SOURCES candidate with URL,
access date 2026-10-21, kind, tier + reason, scope, a <=25-word verbatim quote with
location, what it teaches the entry (which section), and recheck cadence.

## Result — assigned candidate: Marciniak 2011, open-access review (opened in full)

The 1983 primary article's own landing page is closed to this host, but a peer-reviewed
open-access review that states Sherratt's thesis and audits its zooarchaeological basis was
opened in full at the publisher. That is the candidate below.

**Citation.** Arkadiusz Marciniak 2011, "The Secondary Products Revolution: Empirical
Evidence and its Current Zooarchaeological Critique", *Journal of World Prehistory* 24(2)
117–130, DOI `10.1007/s10963-011-9045-7`, CC BY-NC, published online 2011-06-01 (issue
September 2011).

**Opened route (read 2026-10-21).** `https://link.springer.com/article/10.1007/s10963-011-9045-7`
rendered as the full open-access article (native fetch): title, abstract, Introduction,
"Empirical Evidence Supporting Sherratt's Model", the three regional critique sections, and
"Discussion and Conclusions" all readable. The canonical URL is the one in the page's
`meta-canonical`.

### Paste-ready registry row (11 columns; id is L1's to assign — next free is S048+)

```
| S048 | Marciniak 2011, The Secondary Products Revolution: Empirical Evidence and its Current Zooarchaeological Critique, Journal of World Prehistory 24(2) 117–130 — https://doi.org/10.1007/s10963-011-9045-7 | paper | B | what Sherratt's Secondary Products Revolution thesis claims (meat-first Neolithic, then milk, wool, textiles and traction) and this review's own three-region zooarchaeological critique of it — Old World Neolithic only | open-access article, Abstract sentence 1 and Introduction paras 1–2 (link.springer.com/article/10.1007/s10963-011-9045-7), published online 2011-06-01; opened 2026-10-21 | primary animal products are taken once at death, secondary repeatedly without slaughter; the thesis is post-domestication milk, wool, textiles and traction, a consequence rather than a cause of domestication; the review's Central Anatolia / Central Balkans / North European Plain evidence finds adoption idiosyncratic and never a single horizon — date a culture by its local trajectory, not by a single Near Eastern horizon | queued | 2026-10-21 | 365d | — |
```

Set `status: mined` and `used-by: corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`
only if claim C's landed entry actually cites it; otherwise leave `queued` / `—`.

### Required quote (16 words, verbatim), with location

> a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction

Location: Abstract, first (opening) sentence — the sentence that begins "Andrew Sherratt is
perhaps best known for the concept of a 'Secondary Products Revolution', which stressed that
the 'primary' pattern of exploiting domesticated animals for meat in the Early Neolithic was
followed by …". The fragment starts mid-sentence; the preceding clause names the meat-first
Neolithic.

### Supporting verbatim quotes (also <=25 words each), for the entry author

1. Definition, Introduction para. 1, final sentence (23 words):
   > secondary animal products can be exploited without slaughtering animals, and the same animal can be repeatedly exploited in the course of its lifetime
2. Causal status, Introduction para. 2 (24 words):
   > exploitation of secondary products appeared long after animal domestication, and that it should be considered as a consequence, not a cause, of the domestication
   (The sentence's subject is "Sherratt argued that …".)
3. Calibration, Discussion and Conclusions para. 1 (22 words):
   > the changes that might be linked with the Secondary Products Revolution are by no means associated with a single century or millennium

### Tier and scope — why B, not A

`B`, scoped exactly as the row's scope column says. QUALITY.md:29 (criterion 6): "publisher
descriptions and abstracts are tier B for substantive claims about a work, even when
accurate; reserve tier A for sources primary or authoritative for the exact scope." This is
a peer-reviewed review *reporting* Sherratt's thesis; it is not Sherratt's 1981/1983 text, so
it cannot be A for what the thesis says. It is A only for the narrower scope "what this 2011
review itself concludes from its three regional case studies" — deliberately not the row's
scope, so the row stays B and the entry under-claims rather than over-claims.

The tier-A route was tried and blocked, which is why the review is the candidate:

| Route to the primary statement | Outcome |
|---|---|
| `https://www.tandfonline.com/doi/abs/10.1080/00438243.1983.9979887` (Sherratt 1983, *World Archaeology* 15(1) 90–104) | **HTTP 403** |
| `https://api.crossref.org/works/10.1080/00438243.1983.9979887` | record OK (title, author, pp. 90–104, vol 15 issue 1, issued 1983-06); **no `abstract` field** |
| `https://doi.org/10.1515/9781474472562-010` (revised 1983 chapter, *Economy and Society in Prehistoric Europe*, 1997) | Crossref resolution prints **"No abstract available."** |
| `https://www.tandfonline.com/doi/full/10.1080/00438240903429722` (Greenfield 2010 review) | **HTTP 403** |
| `https://www.jstor.org/stable/25679726` (Greenfield 2010) | JSTOR "Client Challenge" bot wall, no content |

My Crossref query found no open landing for the 1981 chapter (*Pattern of the Past*, CUP,
pp. 261–306) — only the 1997 reprint in *Economy and Society in Prehistoric Europe* — and its
full citation is carried in the review's reference list and in Orton 2020 (below). I did not
open the 1981 print text.

**Scope boundary.** Old World Neolithic, archaeological; the review's own cases are Central
Anatolia (Çatalhöyük), the Central Balkans (Greenfield's material) and the North European
Plain (Kujavia/Wielkopolska). It says nothing about nomadic pastoralism as a social form,
transhumance routes, herd composition rules, pastoral tenure, or any modern herding people.
It cannot ground those sections, and it must not be stretched to.

### What it teaches the entry, and where

- **§6 Products (main use).** The primary/secondary distinction in operational form: primary
  products are extracted once, at the animal's death (meat, hide, blood, bone); secondary
  products are taken repeatedly from a living animal (milk, wool/textiles, traction,
  transport). The review also reports Sherratt's causal ordering — secondary exploitation as
  a *consequence* of domestication, not a cause — and the two claimed payoffs (milking as an
  efficient mode; the plough extending cultivated area). This is the source for the entry's
  "the animal that became a machine" generator, which `agrarian-field-system-lexicon.md:80`
  already flags as `(to-verify)`.
- **§13 Calibration (second main use).** The review's own finding: across all three regions
  the introduction of secondary products "was idiosyncratic and highly diverse", there was no
  specialized secondary-product economy before much later (in the Balkans, not until the Iron
  Age), and the linked changes are "by no means associated with a single century or
  millennium". Two concrete calibration flags it supplies: (a) do not date a culture's
  milking/wool/traction by a single Near Eastern horizon — make it a local trajectory;
  (b) Sherratt's original evidence was assembled "in an unconstrained manner, calling in
  examples from diverse chronological periods and vast geographical areas", mostly Uruk
  Mesopotamia and Old Kingdom Egypt — the model is a research programme, not a dated event.
- **§9 Relations / §10 Ritual (seam, optional).** The review argues that cattle's
  ceremonial/social role had to be disassociated from the domestic domain before the
  economically more efficient, household-based exploitation could expand. If the entry wants
  the ritual/wealth seam stated with a source, that sentence is in "Discussion and
  Conclusions" (final paragraphs); otherwise leave it to the ritual owner. Do not import the
  review's social-transformation argument as production fact.

### Recheck cadence

`365d`. It is a fixed 2011 open-access article (no edition churn); recheck is cheap and is
for one reason only — whether the SPR critique has moved (Greenfield 2010 and later
zooarchaeology), not for wording drift.

## Additional opened evidence (not the assigned candidate; L1 rules whether to file)

These were genuinely opened this session and materially strengthen §6/§13, but each has an
access caveat that the assigned candidate does not. They are listed so the C author can use
them without pretending they are publisher-opened primary text.

1. **Sherratt 1983's own abstract, via OpenAlex's mirrored inverted index.** OpenAlex
   `W2016559981` (`https://api.openalex.org/works/https://doi.org/10.1080/00438243.1983.9979887?select=id,title,publication_year,abstract_inverted_index,open_access`)
   carries an `abstract_inverted_index` that reconstructs deterministically to: "This paper
   considers the range of evidence for secondary uses and products of animals: traction,
   transport, wool and milk. It suggests that early farming populations used livestock mainly
   for meat …". Verbatim fragment (10 words): "secondary uses and products of animals:
   traction, transport, wool and milk". The T&F landing 403s and Crossref has no abstract, so
   this wording is read through an index, not the publisher. **Recommendation: do not file a
   tier-A row from this; if L1 admits index-mirrored abstracts, file it B with the anchor
   naming OpenAlex and the 403.** It is the only route I found to Sherratt's own triad.
2. **Orton 2020, "Secondary Products and the 'Secondary Products Revolution'",
   *Encyclopedia of Global Archaeology*, pp. 9571–9577, DOI `10.1007/978-3-030-30018-0_2364`.**
   The publisher landing (`https://link.springer.com/rwe/10.1007/978-3-030-30018-0_2364`)
   renders the Introduction as a free preview; the rest is subscription ("This is a preview
   of subscription content"). Verbatim (15 words), Introduction para. 1: "three resources
   that can be provided by livestock prior to slaughter: milk, wool, and labor". Its next
   sentence gives the causal chain the entry's §6/§8 can use, verbatim (14 words):
   "systematic production of milk and wool rendered specialized large-scale pastoralism
   (geared toward exchange) feasible", followed by cattle-drawn ploughs extending cultivation
   to marginal soils and wheeled vehicles moving arable and pastoral produce in bulk; it dates
   the complex to the fourth millennium BCE Near East, spreading to Europe by diffusion, and
   notes Sherratt built on Bökönyi and others. Tier B, preview-only; use only for the triad and
   the exchange/plough/transport chain, never for detail beyond the Introduction.

## Anti-laundering notes for the C author

1. **Do not put words in Sherratt's mouth.** The assigned row is a review. Write "Sherratt's
   model, as Marciniak summarises it, …" or cite the review directly; never "Sherratt (1983)
   says …" on the strength of this row. The only third-party text that names his triad in his
   own abstract is the OpenAlex mirror above, and that is caveated.
2. **One wrong DOI is circulating in my own log.** `10.1080/00438243.1983.9979884` is **not**
   Sherratt: Crossref identifies it as David S. Geddes, "Neolithic transhumance in the
   Mediterranean Pyrenees", *World Archaeology* 15(1) 51–66. The correct Sherratt DOI is
   `10.1080/00438243.1983.9979887`. Do not let the Geddes record enter the entry as Sherratt.
3. **No manure.** This row's product list is milk, wool/textiles, traction, transport. The
   agrarian entry's line 80 adds manure; that is a different claim and must not be sourced to
   this row.
4. **No horizon dating.** The row's strongest calibration sentence is that the changes are
   "by no means associated with a single century or millennium"; an entry that dates a
   culture's secondary-product adoption to "the fourth millennium BCE" would contradict its
   own source.
5. **Status discipline.** The row is `queued`, not `mined`, until the entry text cites it;
   `used-by` names only path(s) that actually cite it.

## Unrun checks / bounds honoured

- No lane file, clone, patch, git index or jj state touched; no `git add`/`commit`/`checkout`;
  nothing written under `/home/vgpnk/Projects/shokunin/.ufo`.
- No installs attempted (pacman host-wide pause respected); nothing to record.
- Did not run the entry's gap sweeps, README sweep, or separability/operability checks — not
  this seat's question.
- Did not open the 1983 article body (403), the Greenfield 2010 body (403), the JSTOR copy
  (bot wall), or the Orton entry beyond its free Introduction preview.
- Remaining unknown: whether the OpenAlex-mirrored 1983 abstract is byte-faithful to the
  publisher's deposited abstract (not verifiable from this host); whether the review's
  regional conclusions have been superseded since 2011 (recheck cadence covers it).
