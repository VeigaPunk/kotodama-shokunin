# Round 66 - 2026-10-24 (hyaku run 5, L1 KotodamaR66)

## Round summary

Three claims at base `94209e8f80969dbac48d56c5d0e2e623635b8616`. C (coverage,
sourced): new culture-material entry
`corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` - scent,
perfume, aromatics and incense as material and social practice - supported by
22 new registry rows S779-S800 (tier A or B, opened 2026-10-24, mined, used-by
the entry, each cited once). Predicate ACCEPT-C-66: every leg of
`reports/round-66/accept-c.py` prints PASS. O (operability): the routed defect
R65-D4 (the separability checker timed out at 600s on the round-65 manifest) is
bounded - `tools/check-claim-separability.py` gains `--jobs`, `--budget`,
`--max-runs`, `--static-only`, honest-partial exit 2 and per-run stderr
forwarding; predicate ACCEPT-O-66: every leg of `reports/round-66/accept-o.py`
prints PASS against the same revision. Ca (calibration): the round-65 closure's
four routed defects are dispositioned: R65-D1 (S753's 2025 capture replayed a
redirect-stub; live 200 pdf verified, fresh capture 20261024111013 saved and
sha256-bound, the games entry re-pointed S753 -> S776 and S753's used-by cell
flipped to `-`), R65-D2 (receipts re-derived against the stamped lands
revision), R65-D3 (the wave dispatched 64 seats in one task call and
`telemetry/seat-evidence.txt` names each returned report on disk), R65-D4 (the
bounded separability checker runs the round-66 manifest to a complete verdict).
Predicate ACCEPT-CA-66: every leg of `reports/round-66/accept-ca.py` prints
PASS.

Wave note: one seat (ScoutRow01, rows S777 and S778) returned a provider error
and produced no fragment. The claim statement was shrunk pre-data to
S779-S800 (22 rows) and the gap is named here, so the missing work is a dead
seat, not silent scope-cutting.

## Gate (rows opened this round; each quote is the anchor quote of that row's own
final `row-*.txt` artifact, verbatim)

- S776 | https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf | 2026-10-24 | "Versions of mancala are traditionally played across Africa and Asia, with gameplay and board dimensions varying considerably between different regions."
- S779 | https://escholarship.org/content/qt0pb1r0w3/qt0pb1r0w3.pdf | 2026-10-24 | "The most famous of all scents was kyphi, known from three versions on temple walls (two at Edfu, one at Philae), from papyri (P. Ebers)"
- S780 | https://www.metmuseum.org/essays/trade-between-arabia-and-the-empires-of-rome-and-asia | 2026-10-24 | "The Incense Route ran along the western edge of Arabia's central desert about 100 miles inland from the Red Sea coast"
- S781 | https://ecampusontario.pressbooks.pub/dressandadornmentancientgreece/chapter/perfume-and-scented-oils/ | 2026-10-24 | "Beyond its culinary uses, olive oil served as the base for perfumes, cosmetics, and medicines"
- S782 | https://www.iranicaonline.org/articles/atr-perfume/ | 2026-10-24 | "large quantities of rose-water were regularly distilled in Persia and Iraq at least from the ninth century"
- S783 | https://www.huntbotanical.org/virtues-pleasures-herbs/page.php?Fragrance-4 | 2026-10-24 | "believed to have been produced around 1370 and derived its base from this herb, which imparted a rejuvenating fragrance"
- S784 | https://ich.unesco.org/en/RL/the-skills-related-to-perfume-in-pays-de-grasse-the-cultivation-of-perfume-plants-the-knowledge-and-processing-of-natural-raw-materials-and-the-art-of-perfume-composition-01207 | 2026-10-24 | "Inscribed in 2018 (13.COM) on the Representative List of the Intangible Cultural Heritage of Humanity"
- S785 | https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0185-62862016000200045 | 2026-10-24 | "its aromatic smoke, that was also considered divine food, allowed the link between deities and humans"
- S786 | https://lockwoodonlinejournals.com/index.php/jaos/article/view/1362 | 2026-10-24 | "elite scent culture had already begun to be transformed by the importation of foreign aromatics"
- S787 | https://www.seiryo-u.ac.jp/u/research/gakkai/ronbunlib/humanities_ronsyu_pdf/No2/04_koiso.pdf | 2026-10-24 | "sandalwood paste, incense, pastille, camphor, lamps of burning oil or ghī, and fragranced flowers to the deity"
- S788 | https://david-howes.com/senses/Consert-Odor.htm | 2026-10-24 | "Men are socialized through initiation and lose their strong-smelling odor. Women, on the other hand, by their very sexuality are strong smelling."
- S789 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8951631/ | 2026-10-24 | "More than 3000 kg of rose flowers produce 1 kg of rose oil by water distillation."
- S790 | https://collections.vam.ac.uk/item/O78794/pair-of-gloves-unknown/ | 2026-10-24 | "Recipes for scenting gloves survive from the 17th century using ingredients such as musk, ambergris, floral extracts and aromatic spices."
- S791 | https://collections.vam.ac.uk/item/O105969/pomander-unknown/ | 2026-10-24 | "strong-scented substances had the power to disinfect the air and to ward off plague and other diseases"
- S792 | https://cienciassociales.uniandes.edu.co/opca/articulo/paraiso-perfumado-crear-y-recrear-los-mundos-olfativos-de-los-mayas-del-periodo-clasico%C2%B9/ | 2026-10-24 | "como lo registraron observadores españoles con respecto a los palacios aztecas de Centroamérica en el siglo XVI"
- S793 | https://www.nhm.ac.uk/discover/what-is-ambergris.html | 2026-10-24 | "For hundreds of years, perfumers have categorised the quality of ambergris according to its colour"
- S794 | https://www.chateauversailles-recherche.fr/article964.html | 2026-10-24 | "les gantiers-parfumeurs fabriquent les gants parfumés, dont le succès est à son apogée à la cour de Louis XIV"
- S795 | https://daily.jstor.org/keeping-time-with-incense-clocks/ | 2026-10-24 | "incense clocks burned all night in Beijing's tall drum tower" (cont. in row: "measuring out the time until the beating of the huge drum announced the end of the night watch")
- S796 | https://research-information.bris.ac.uk/ws/files/150040263/Bessard_paper_preliminary_edit_FB.pdf | 2026-10-24 | "designed them to function as a set of defined zones for various commodities and the streets took on the name of the trade plied there"
- S797 | https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0137:book=13:chapter=2 | 2026-10-24 | "In later times Phœnicia eclipsed Egypt in the manufacture of these last two" (cont. in row)
- S798 | https://slll.cass.anu.edu.au/classics-museum/catalogue/objects/corinthian-alabastron-196302 | 2026-10-24 | "The alabastron was a shape introduced into Corinthian pottery from the east" (cont. in row)
- S799 | https://knmdb.kyohaku.go.jp/eng/30115.html | 2026-10-24 | "In these games, over several rounds, a host selects varieties of incense for their guests to savor and identify."
- S800 | https://bmcr.brynmawr.edu/2013/2013.04.46/ | 2026-10-24 | "it was an oil press for the production of perfume and not a textile press"

## Mistakes

- R66-M1 (class: source-durability). Seat ScoutRow10's S795 fragment paired a
  live archive.org PDF with a Wayback capture of the JSTOR landing page - a
  capture of a different page than the named live URL. The claim's CAPTURE leg
  requires same-page and there is no wayback capture of the archive.org
  download (fresh /save 523). Fix: the row's source was replaced with a
  JSTOR Daily article whose live page and 20260808211740 capture both carry
  the anchor quote verbatim; the Bedini PDF is out. Captured-by: the hardened
  CAPTURE leg `S795:capture_target_mismatch` plus the L1 re-open (live 200,
  capture body verified verbatim, gzip-decoded).
- R66-M2 (class: quote-integrity). Seat ScoutRow04's S783 anchor quote was
  assembled with a nested straight-quote inside the quoted span
  (`"first-named... "Hungary water" is believed..."`), which the anchor_quote
  extractor reads as a 6-word fragment and which misrepresents the page text.
  Fix: the anchor was replaced with the page's own verbatim sentence
  (`"believed to have been produced around 1370 and derived its base from this
  herb, which imparted a rejuvenating fragrance"`), confirmed verbatim by
  fetching the live page. Captured-by: RESTATE leg plus L1 re-fetch.
- R66-M3 (class: counter-shape). The LINK dup-base leg used norm_url, which
  drops the query, so every Perseus `hopper/text` URL in the base collided with
  the new Pliny XIII.2 URL - thirteen false `dup-base` hits on rows S242..S311.
  Fix: the leg now compares norm_url_q (host+path+percent-decoded query,
  scheme-agnostic), matching the counter's documented same-page intent; the
  row itself was verified verbatim on its live page and on its 20260127095527
  capture. Captured-by: LINK leg `S797:dup-base` plus a manual census diff.
- R66-M4 (class: wave-planning). Seat ScoutRow01 died on a provider error and
  rows S777-S778 were never produced; the first dispatched claim named
  S777-S800. Fix: the claim was shrunk pre-lands to S779-S800, the missing
  rows are named in this lesson, and the seat is recorded dead in
  `telemetry/seat-evidence.txt`. Captured-by: swarm-registry.json plus the
  seat-evidence file.
- R66-M5 (class: anchor-vs-landing). S797's verbatim quote carries the ligature
  "Phœnicia"; a plain-text copy ("Phoenicia") is not verbatim on the page.
  Fix: the registry anchor keeps the ligature exactly as rendered (confirmed
  verbatim on the live page and inside the 20260127095527 capture body).
  Captured-by: QUOTES leg re-test and manual verbatim search.
