# ScoutEvilEyeMediterranean — claim C sources: S606, S607

Question (seat): open 2–4 sources on the evil-eye complex around the Mediterranean and the Middle
East — eye beads (*nazar*), blue glass, what the eye is believed to do — and offer at most two
claim-C rows aimed at the design decisions a worldbuilder makes: what the object is made of, what
danger it answers, who makes or blesses it, where it is worn or placed, and what signs it carries.

Axes named: **coverage** (claim C's axis — `nazar`, `evil eye`, `amulet` had 0 filename owners and
0 knowledge files; `ConnectInLaneAmulets59 §4` shows `nazar` = 0 hits), **verifiability** (FETCH-59:
a live page that answers a plain GET, the quote in body prose, a clear site root), **usability**
(the quote must carry a buildable choice, not a definition). Moves kept: one museum object record
that names the object class and its material (*nazar* = glass eye bead) and one editorial synthesis
that says what the shiny surface is *for*. No move that harms an axis was kept.

Method: every page below was opened in this session by an ordinary GET — `curl` for status and byte
count, and the round's own `reopen-quote.py` fetch (desktop Firefox/131 UA, redirects, no cookies,
no challenge solving) for the text. No headless browser, no installs or updates (nothing to record).
Working directory for every command:
`/fast/scratch/hyaku/kotodama-r59/ScoutEvilEyeMediterranean/`; artifacts `probe.py`, `rows.md`,
`stub.md`, `cap-only.md`, `smg103790.html`, `cur.html`, `cur-cap.html`.

Check run (verbatim):

```
cd /fast/scratch/hyaku/kotodama-r59/ScoutEvilEyeMediterranean && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutEvilEyeMediterranean/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutEvilEyeMediterranean/stub.md
S606 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103790/glass-amulet | BOILER: root-clear https://collection.sciencemuseumgroup.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'bead', 'commo', 'evil', 'form', 'glas'] | TOPIC: quote_hits=1 function_words=3 page_hits=26 page_terms=27 need=1/2/3/2
S607 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.curationist.org/editorial-features/article/protection-from-the-evil-eye | BOILER: root-clear https://www.curationist.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'away', 'gaze', 'malic', 'mater', 'refle'] | TOPIC: quote_hits=1 function_words=5 page_hits=63 page_terms=104 need=1/2/3/2
EXIT=0
```

---

## S606 — a nazar is a glass eye bead, and it is the commonest form of the evil-eye amulet

**Registry row (11 cells, paste-ready):**

| S606 | Science Museum Group Collection (Science Museum, London), undated object record co103790, "Glass amulet" — glass eye bead amulet known as a nazar, Sir Henry Wellcome's Museum Collection, said to have been carried by a soldier in Palestine 1914–1918. — https://collection.sciencemuseumgroup.org.uk/objects/co103790/glass-amulet (direct, HTTP 200, 43397 bytes) | docs | A | what this museum record states about one glass nazar and about evil-eye amulets in general — its own curatorial framing, not a regional survey | Curatorial description paragraph of the object record: "Glass eye beads, also called nazars are one of the commonest forms of evil eye amulet." | Glass eye beads known as nazars are the commonest form of evil-eye amulet, and the record places them around the Mediterranean, Central Asia and the Middle East. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

**Gate line:**

- S606 — https://collection.sciencemuseumgroup.org.uk/objects/co103790/glass-amulet — accessed 2026-10-23 — Curatorial description paragraph of the object record: “Glass eye beads, also called nazars are one of the commonest forms of evil eye amulet.”. Grounds: Glass eye beads known as nazars are the commonest form of evil-eye amulet, and the record places them around the Mediterranean, Central Asia and the Middle East. Seat: ScoutEvilEyeMediterranean.

**What the opened page carries beyond the quote** (body of the same description; useful for entry
sentences as long as they are not tied to *this* quote's stems):

- The belief defined: the evil eye is "the belief that someone – perhaps a real individual or a
  perceived supernatural power – can cause physical harm, misfortune or plain bad luck through a
  malicious glance or glare"; amulets are "worn or carried as protection against it".
- The design constant: "Such amulets exist in a variety of forms but the common characteristic is
  they incorporate an eye shaped design. This can be realistic or highly stylised."
- Distribution of the bead form: "They are particularly found around the Mediterranean, Central Asia
  and the Middle East."
- Object and provenance: made 1914–1918 (maker unknown), glass and fibre, 21 mm, "worn by a soldier
  in Palestine during the First World War"; "bought for the Wellcome collection in 1930 from Edward
  Lovett's (1852-1933) collection of mostly British amulets and charms" — i.e. the collector is the
  western buyer, not the maker.
- Related objects in the same Wellcome set, on the page: "Ring, blue glass with bare mount at front,
  worn by children to avert the evil eye, Palestinian, 1870-1930" and "Glass arrowhead trade amulet,
  European manufacture for use in Africa, Europe, 1880-1930" — both carry *blue glass* and
  *children* and *trade*, but they are carousel labels, not body prose; they cannot be a quote.

---

## S607 — a shiny surface is the mechanism: the amulet reflects the gaze off its wearer

**Registry row (11 cells, paste-ready):**

| S607 | Gattuso, Reina. September 2025. "Protection from the Evil Eye." Curationist, editorial feature with numbered citations, 18-minute read. — https://www.curationist.org/editorial-features/article/protection-from-the-evil-eye (direct, HTTP 200, 295269 bytes); capture https://web.archive.org/web/20260417193418id_/https://www.curationist.org/editorial-features/article/protection-from-the-evil-eye (HTTP 200, 283623 bytes) | community | B | why shiny and precious materials were chosen for evil-eye amulets, and how their motifs, wearers and modern market are described; an editorial synthesis that cites its scholarship | Section The Power of Reflection, body paragraph: "In some times and places, people used shiny materials to craft amulets meant to reflect malicious gazes away from the user." | Shiny materials were chosen for amulets so that a malicious gaze would be reflected away from the person wearing it. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

**Gate line:**

- S607 — https://www.curationist.org/editorial-features/article/protection-from-the-evil-eye — accessed 2026-10-23 — Section The Power of Reflection, body paragraph: “In some times and places, people used shiny materials to craft amulets meant to reflect malicious gazes away from the user.”. Grounds: Shiny materials were chosen for amulets so that a malicious gaze would be reflected away from the person wearing it. Seat: ScoutEvilEyeMediterranean.

**What the opened page carries beyond the quote** (all body prose; the page is a curated survey
with footnotes to Kotzé on Sumerian evil-eye deities, Musacchio on coral in Renaissance Italy,
Pliny, al-Biruni, and Berghahn's *The Evil Eye* volume):

- Doctrine: "The evil eye translates powerful emotions such as envy into harmful magic through the
  medium of vision"; "By desiring or admiring something, the admirer (even inadvertently) curses it"
  — envy, and even praise, are the mechanism.
- Reflection and mirrors: jet prayer beads carved with saints in the early modern Iberian peninsula;
  *tensifa* mirror covers used at weddings "to ward off malicious gazes".
- Colour and material: turquoise "considered protective against the evil eye" in the Eastern
  Mediterranean and Central Asia; "Those who couldn't obtain objects made of turquoise could acquire
  imitations, in the hope that the color blue itself would protect the wearer even in the gem's
  absence"; coral "and by extension, the color red itself" protecting women and children, back to
  Pliny; coral necklaces gifted to pregnant women in 19th-century Yemen; the infant Jesus wearing a
  coral necklace in medieval and early modern portraits.
- Sound and multi-function: the Yemeni necklace's jangling silver, and a gold-and-coral
  rattle/whistle/bell that is "both an evil eye amulet and a teething toy".
- Motifs and placement: dot-in-circle eye, *wedjat*, open-hand *khamsa* ("Hand of Fatima"/"Hand of
  Miriam", "particularly thought to confer evil eye protection to women and children"), *mano
  fica*, genital imagery, and "a long tradition of affixing fearsome, staring figures to buildings
  in order to repel evil" (the Medusa gorgoneion antefix on a roof), plus eyes on ship's prows.
- Makers and the modern market: "artists and ritual specialists consider the qualities of the
  material as well as the power of sculptural form and motif"; the blue nazar now "more commercially
  popular" in North America and in tourist markets; Greek Orthodox clergy "quite critical of the
  practice as at-odds with proper religious devotion" (footnote 10) — the reform/tension thread.
- Naming and reach: the blue-ringed glass nazar is called "*nazar boncuğu*" in Turkey; the harmful
  gaze is *nazar*, *malocchio*, *mal de ojo*, *mati*.

---

## draft sentences (also in `stub.md`)

A glass eye bead called a nazar is one of the commonest amulets against the evil eye, so the cheapest protective object in a Mediterranean-flavoured setting can be a bead rather than a plaque (S606).

Such amulets vary in form but share an eye-shaped design, so the motif, not the object type, is what carries the protection (S606).

A shiny material is part of the mechanism: the surface of the amulet is meant to reflect a malicious gaze away from its wearer (S607).

Precious materials were believed to hold innate protective power, so setting a stone into an amulet added potency rather than ornament (S607).

Where turquoise was out of reach, imitation blue was bought in the hope that the colour itself would protect the wearer (S607).

Note for the L1: sentences 1–2 are carried by S606's quote and by the same page's next paragraph;
sentence 3 is carried by S607's quote; sentences 4–5 are carried by S607's *page* (the sections
"Precious Materials (And Their Imitators)" and the turquoise-imitation paragraph), not by the quoted
sentence. If the blind SUPPORT seat reads strictly "the quote carries the entry sentences", keep
sentence 3 only and take blue from a sibling row; if it reads the page, 4–5 hold. I would keep 3–5
but not add any further colour claim beyond what those paragraphs say.

---

## rejected (opened, not offered)

- https://collection.sciencemuseumgroup.org.uk/objects/co103089/necklace-worn-to-ward-off-the-evil-eye — opened, HTTP 200, 54026 bytes; page_hits=14 page_terms=10. Rejected: the only body sentence about making is "The glass beads of this necklace are painted to look like eyes to protect against the ‘Evil Eye’." (18 words, 1 window), and the other windowed candidate is the page's own heading "Necklace worn to ward off the Evil Eye." — a quote that the BOILER leg rejects as a title. Same host as S606, weaker claim; kept in reserve if a later round wants a Hebron/children row (`Amulet necklace, 49 glass beads resembling eyes, worn to avert Evil Eye, from Hebron, Palestinian, 1880-1930`).
- https://historicengland.org.uk/research/current/discover-and-understand/faith-and-ritual/ — verbatim: `https://historicengland.org.uk/research/current/discover-and-understand/faith-and-ritual/ -> 403 5895`. Rejected: never opened live; no page to quote (this was the intended route to protective marks on buildings).
- https://www.britishmuseum.org/blog — verbatim: `https://www.britishmuseum.org/blog -> 403 5583`. Rejected: host refuses plain GETs.
- https://www.cmog.org/article/evil-eye — verbatim: `https://www.cmog.org/article/evil-eye -> 403 5631`. Rejected: the Corning Museum of Glass was the intended blue-glass-maker source; the host refuses plain GETs.
- https://www.fitzmuseum.cam.ac.uk/ — verbatim: `https://www.fitzmuseum.cam.ac.uk/ -> 503 11523`. Rejected: 503 on a plain GET.
- https://museumofwitchcraftandmagic.co.uk/object/amulet-eye/ — verbatim: `https://museumofwitchcraftandmagic.co.uk/object/amulet-eye/ -> 503 3571`. Rejected: 503; the object ("1889 – NAZAR BONCUGU EYE CHARM") was found only through a tier-C search result and never opened, so no row may use it.
- https://www.brooklynmuseum.org/opencollection/objects — verbatim: `https://www.brooklynmuseum.org/opencollection/objects -> 429 34228`. Rejected: throttled; never opened.
- Host probes opened only to test plain GET, no evil-eye page selected, so not offered (a root cannot carry a row — BOILER `source-is-root`): `https://www.penn.museum/ -> 200 62985`, `https://oi.uchicago.edu/ -> 200 304665`, `https://www.prm.ox.ac.uk/ -> 200 189214`, `https://journals.openedition.org/ -> 200 5281`, `https://art.thewalters.org/ -> 200 71847`, `https://harvardartmuseums.org/ -> 200 103096`, `https://www.agakhanmuseum.org/ -> 200 189927`.

---

## confidence, risks, unknowns

- **High confidence** in both quotes as body prose: S606's sentence sits in the object record's
  description paragraph (checked in raw HTML: `<p>` text, not the `<meta name="description">`, which
  carries only the short object summary "Glass eye bead amulet, known as a nazar, for protection
  against the Evil Eye, worn by a soldier in Palestine…"); S607's sentence is a `<p>` under the
  sub-heading "The Power of Reflection".
- **FETCH-59 risk, S606**: no Wayback capture exists for
  `…/objects/co103790/glass-amulet` (CDX exact query returned `[]`; the availability API returned
  `{"archived_snapshots": {}}`), so this row has one URL. The live page answered the locator's GET
  with 200 four times in this session (43,397 bytes each). The host is **user-agent sensitive**: a
  bare `Mozilla/5.0` UA got `403 919` from the same object URL, and a sibling seat's search URL got
  `403 919` as well; the instrument's Firefox/131 UA is the one that passes, and accept-c runs the
  same instrument.
- **FETCH-59 risk, S607**: the capture was opened live (HTTP 200, 283,623 bytes) and contains the
  quote, but a capture-only run fails BOILER right now — verbatim:
  `S607 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | … | BOILER: root-unfetchable https://web.archive.org/web/20260417193418/https://www.curationist.org/ URLError`.
  archive.org was serving "Internet Archive: Temporarily Offline" and then refusing connections
  during this session, so the capture is a second chance only when the archive is healthy; the live
  Curationist page (200 on every attempt) is the deciding URL. Nothing in the row depends on the
  capture.
- **Tier judgement**: S606 is A for the narrow scope "what this record states"; the museum's
  generalisation ("one of the commonest forms") is curatorial, not measured, so no entry sentence
  should convert it into a statistic. S607 is B: an authored, footnoted editorial feature on a
  nonprofit museum-adjacent platform (`community` kind), strong for materials, motifs and the
  commodification/reform threads, not a peer-reviewed study.
- **Unknown / not covered by these two rows**: what the eye is believed to *do* as a doctrine (envy,
  praise, the glance as pollution) is on S607's page but outside its quote; the eye-bead makers
  (glass workshops, *nazar boncuğu* artisans) and the mezuzah/ofuda/omamori comparison are not in
  either row — other seats own them. Blue glass is carried by S607's page text, not by its quote.
