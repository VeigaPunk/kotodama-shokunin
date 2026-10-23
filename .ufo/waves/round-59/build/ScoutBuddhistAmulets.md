# ScoutBuddhistAmulets — claim C sources: S628, S629

Question (seat): open 2–4 sources on Buddhist protective amulets (Tibetan gau boxes, Thai
*phra khrueang*, protective yantra) and offer at most two claim-C rows S628 and S629 aimed at
design decisions a worldbuilder makes: what the object is made of, what danger it answers, who
makes or blesses it, where it is worn or placed, and what words or signs it carries.

Axes named: **coverage** (the claim's declared axis — new ground, 0 filename owners), **verifiability**
(FETCH-59: a live page that answers a plain GET, with the quote in body text and a clear site
root), and **usability** (each quote must carry an actual construction choice, not a definition).
Kept moves: one Tibetan gau row (purpose and contents) plus one Thai *phra khrueang* row
(maker's authority, yantra, activation). No move that harms an axis was kept.

Method: every page below was opened in this session by an ordinary GET through the round's own
`reopen-quote.py` fetch (desktop UA, redirects, no cookies, no challenge solving) or by `curl`
for the HTTP status and byte count. No headless browser. No installs or updates were made;
`uv` (already present at `~/.local/bin/uv`) is used only by the instrument's pinned
`pypdf==5.4.0` extraction. Working directory for every command:
`/fast/scratch/hyaku/kotodama-r59/ScoutBuddhistAmulets/`; artifacts `rows.md`, `stub.md`,
`text/*.txt`, `rej-ngv.md`, `rej-rubinobj.md`.

Both rows were checked with the round-59 instrument before being offered:

```
cd /fast/scratch/hyaku/kotodama-r59/ScoutBuddhistAmulets && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutBuddhistAmulets/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutBuddhistAmulets/stub.md
S628 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://rubinmuseum.org/projecthimalayanart/essays/amulet-box-gau-with-its-contents/ | BOILER: root-clear https://rubinmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'fortu', 'harm', 'life', 'long', 'love'] | TOPIC: quote_hits=1 function_words=3 page_hits=55 page_terms=40 need=1/2/3/2
S629 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://englishkyoto-seas.org/wp-content/uploads/SEAS_0202_Baker-and-Pasuk.pdf | BOILER: root-clear https://englishkyoto-seas.org/; not a title, h1 or meta label | RELEVANCE: shared=['adept', 'amule', 'famou', 'monk', 'yantr'] | TOPIC: quote_hits=1 function_words=7 page_hits=99 page_terms=94 need=1/2/3/2
EXIT=0
```

---

## S628 — Tibetan gau: what the wearer asks the object to do

**Registry row (11 cells, paste-ready):**

| S628 | Rubin Museum of Art, Project Himalayan Art; James Gentry, object essay Amulet Box (Gau) with Its Contents (Kathmandu, Nepal, first decade of the 21st century; private collection, Central Europe), undated page read 2026-10-23 — https://rubinmuseum.org/projecthimalayanart/essays/amulet-box-gau-with-its-contents/ (direct, HTTP 200, 239,349 bytes); capture https://web.archive.org/web/20260608142343id_/https://rubinmuseum.org/projecthimalayanart/essays/amulet-box-gau-with-its-contents/ (Wayback availability API returned status 200 for this snapshot; the capture itself was not opened on 2026-10-23 because web.archive.org refused connections from this host) | docs | B | what a Tibetan gau is worn for, what a wearer expects an amulet to secure, and what its sacred contents are (museum-curated object essay; B for the general practice it states, not a community or liturgical source) | Summary, opening sentences: "People wear amulets to bring long life, good fortune, success in love, and protection against harm." | Wearers expect an amulet to deliver specific worldly benefits, from long life and fortune to love and protection from harm. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

**Gate line:**

- S628 — https://rubinmuseum.org/projecthimalayanart/essays/amulet-box-gau-with-its-contents/ — accessed 2026-10-23 — Summary, opening sentences: "People wear amulets to bring long life, good fortune, success in love, and protection against harm." Grounds: Wearers expect an amulet to deliver specific worldly benefits, from long life and fortune to love and protection from harm. Seat: ScoutBuddhistAmulets.

**Rowcheck output:** pasted above; S628 all four legs PASS (`page_hits=55 page_terms=40`).

**What the opened page carries (for the entry, not only the quote):**

- The essay is signed James Gentry (listed under "108 Object Essays" / "Portable Sacred Items for
  Pragmatic and Transcendent Goals"); the object is a gau from Kathmandu, first decade of the 21st
  century, metal alloy, private collection.
- Gau definition on the page: "In Tibetan Buddhism and Bon, a gau is an amulet box, often gilded or
  painted, that contains sacred objects like images, mantras and dharanis, relics, tsatsas, and
  medicinal pills. Tibetans often wear gaus on a cord around the neck, or slung across the shoulder."
- Sizes and carrying: from under an inch to over fourteen inches; small ones worn at the neck,
  larger ones "hung over the chest or under the arm, suspended from a leather strap or cloth band";
  the flat base lets a large gau serve as a travel shrine.
- Contents: "The contents of amulet boxes are referred to in Tibetan as ten, meaning 'receptacle,'
  for their role in encapsulating the 'blessings' (jinlab) and 'power' (tu) of buddhas,
  bodhisattvas, and revered lamas." Contents listed: miniature statues, photographs of lamas,
  votive plaques, amulets, Sanskrit mantras or sacred incantations on small pieces of paper, relic
  pills, materials from sacred sites, fragments of silk, hair, anything once in contact with a
  revered person, place or thing.
- Making to specification: "Amulets are sometimes made using astrological calculations to tailor
  them to specific individuals and functions … the date of birth of the wearer or target is tallied
  according to the sixty-year astrological cycle"; "An amulet is then specially produced to
  manipulate negative and positive influences according to personal and temporal specifications."
- Consecration (page key term): an image "must be made sacred ('consecrated') by inviting the deity
  to inhabit it", by eye-dotting, visualization, mantras written on a thangka's back, or placing
  sacred texts and mantras inside a statue.
- Wealth/status: materials and decoration "vary considerably, reflecting the social status,
  religious role, and gender of their owners, and sometimes the region of their origin"; the essay
  distinguishes men's and women's gau by size and shape.

**Draft sentences (2–4, each ending with the id):**

A Tibetan gau is an amulet box worn on a cord or strap that holds relics, sacred diagrams and pills, and the Rubin's essay says people wear amulets to bring long life, fortune, success in love and protection from harm (S628).

The aims are this-worldly and plural — long life, good fortune, love, protection from harm — rather than one single promise (S628).

---

## S629 — Thai *phra khrueang*: the maker's authority and the yantra on the back

**Registry row (11 cells, paste-ready):**

| S629 | Baker, Chris and Pasuk Phongpaichit, 2013, Protection and Power in Siam: From Khun Chang Khun Phaen to the Buddha Amulet, Southeast Asian Studies 2(2): 215–242, Center for Southeast Asian Studies, Kyoto University — https://englishkyoto-seas.org/wp-content/uploads/SEAS_0202_Baker-and-Pasuk.pdf (direct, HTTP 200, 1,159,618 bytes, PDF); capture https://web.archive.org/web/20250916192115id_/https://englishkyoto-seas.org/wp-content/uploads/SEAS_0202_Baker-and-Pasuk.pdf (Wayback availability API returned status 200 for this snapshot; the capture itself was not opened on 2026-10-23 because web.archive.org refused connections from this host) | paper | A | the article's account of Thai Buddha amulets (phra khrueang), of yantra, and of the maker's authority — what makes an amulet effective and what a monk's manual prescribes | section From Yantra to Amulet, paragraph on Somdet To: "Also like yantra, an amulet is effective only if made by a monk or adept famous for supernatural power (like Somdet To)." | Thai Buddha amulets were held to work only when a famous monk or adept made them, the same efficacy rule the article says governed yantra. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

**Gate line:**

- S629 — https://englishkyoto-seas.org/wp-content/uploads/SEAS_0202_Baker-and-Pasuk.pdf — accessed 2026-10-23 — section From Yantra to Amulet, paragraph on Somdet To: "Also like yantra, an amulet is effective only if made by a monk or adept famous for supernatural power (like Somdet To)." Grounds: Thai Buddha amulets were held to work only when a famous monk or adept made them, the same efficacy rule the article says governed yantra. Seat: ScoutBuddhistAmulets.

**Rowcheck output:** pasted above; S629 all four legs PASS (`page_hits=99 page_terms=94`).

**What the opened page carries (for the entry, not only the quote):**

- Citation from the PDF itself: "Southeast Asian Studies, Vol. 2, No. 2, August 2013, pp. 215–242
  ©Center for Southeast Asian Studies, Kyoto University"; authors Chris Baker and Pasuk
  Phongpaichit.
- Definition used by the article: "Today in Thailand the wearing of an amulet (พระเครื่อง phra
  khrueang), a small image of the Buddha…" (abstract).
- The efficacy rule, in its own paragraph: Somdet To "made several types of protective device,
  including yantra, but also Buddha amulets which are the most desired and most expensive in the
  market today"; "Somdet To also wrote a manual on amulet making which shows the close similarity to
  the creation of yantra. In Somdet To's description, the amulet is made from powerful materials
  (enchanted powder, precious metals, herbs used in lore) following strict rules, including the
  recitation of mantra, and finally is 'activated' by ritual"; "Also like yantra, an amulet is
  effective only if made by a monk or adept famous for supernatural power (like Somdet To). In
  addition, most Buddha amulets have a small yantra inscribed on the reverse side."
- History and trade the entry may use from the same page (for the "how the practice changes"
  section): older amulets are "broken-wall" votive tablets retrieved from ruined wats and stupas;
  the modern form "combines the Buddha image of the votive tablet with the convenient portability of
  a takrut"; nineteenth-century elite acquisition (King Chulalongkorn); by the early twentieth
  century monks famous for asceticism and supernatural power produced amulets "in many parts of the
  country", and acquisition spread with roads and railways; business sponsorship in batches of
  several thousand; a Tha Prachan amulet market near Thammasat University.
- Caution the article itself raises: amulets are "status markers" and have monetary value, so a
  sacred object is also an investment (the page names "alternative investments").

**Draft sentences (2–4, each ending with the id):**

In Thailand the worn amulet is called phra khrueang, and the article holds that such an amulet was effective only when a monk or adept famous for supernatural power made it (S629).

The same rule governed yantra, and most Buddha amulets carry a small yantra inscribed on the reverse (S629).

Somdet To's manual prescribes powerful materials, strict rules, mantra recitation and ritual activation (S629).

---

## Checked and not offered (opened, or attempted and refused)

1. **Metropolitan Museum of Art, "Amulet Box of a Noblewoman", object 39462** — attempt refused,
   not opened. Verbatim `curl` output (desktop UA, 60 s):
   `429 34217` (https://www.metmuseum.org/art/collection/search/39462). A 429 is exactly the FETCH-59
   failure class; the page's search snippet ("Amulet boxes (ga'u) like this one would have contained
   written or printed texts that monks consecrated to protect the wearer") was not treated as
   evidence because I never read the page.
2. **The British Museum, gau / amulet-box, 2003,0628.1** — attempt refused, not opened. Verbatim:
   `403 5707 text/html; charset=UTF-8  https://www.britishmuseum.org/collection/object/A_2003-0628-1`.
3. **National Gallery of Victoria, Amulet box (Gau), work 54508** — opened (direct HTTP 200,
   205,616 bytes). Not offered: the page is a catalogue record whose readable text is a one-line
   physical description; there is no curatorial statement about protection, use, maker or
   deposition, so any quote is caption-like and a blind reviewer would have to reject it as not
   body text about protective practice. Trial row under throwaway label S900 (outside both the
   export and the records blocks; the relevance failure is an artifact of a stub entry that does not
   cite it, not of the source) gave, verbatim:
   `S900 LOCATE PASS BOILER PASS RELEVANCE FAIL TOPIC PASS | ... | RELEVANCE: entry-does-not-cite | TOPIC: quote_hits=1 function_words=2 page_hits=4 page_terms=4 need=1/2/3/2`
4. **Rubin Museum of Himalayan Art, Amulet Box (Gau), C2008.21** — opened (direct HTTP 200,
   94,539 bytes). Not offered, two reasons: (a) the only sentence aimed at protection, "This amulet
   box (gau) would have been filled with religious contents to protect the wearer as well as serve
   as a portable shrine", has no CHARM-GUARD window inside three words (`window_hits=0` under the
   instrument's own scan), so it cannot serve as a TOPIC quote; (b) it is the same host and subject
   as S628, and the two-row cap is better spent on the essay. Trial row under throwaway label
   S901, verbatim:
   `S901 LOCATE PASS BOILER PASS RELEVANCE FAIL TOPIC PASS | ... | RELEVANCE: teaches-copies-quote; entry-does-not-cite | TOPIC: quote_hits=1 function_words=7 page_hits=6 page_terms=6 need=1/2/3/2`
5. **ANU Press, *Power, Protection and Magic in Thailand*, chapter 5** — opened (direct HTTP 200,
   111,243 bytes, XHTML). Not offered only because of the two-row cap: it is a strong Thai source
   (my scan of the extracted text: `page_windows 129 discipline 100`, e.g. "During the twentieth
   century, the Buddhist amulet became a popular magical device for protection, not only for
   soldiers and police, but also for many others"), and it is the best next row for a later round.
   It is held as a lead, not rejected on content; its title is a book offered open-access by ANU
   Press.
6. **web.archive.org** — refused every connection from this host, so neither listed capture was
   opened. Verbatim: `getent hosts web.archive.org` → `207.241.237.3`; `curl` → `000 0` and exit 7;
   the instrument's fetch → `URLError <urlopen error [Errno 111] Connection refused>` for both
   `https://web.archive.org/web/20260608142343id_/…` and
   `https://web.archive.org/web/20250916192115id_/…`. The snapshots are listed as a FETCH-59
   fallback because the Wayback availability API reports them `status: 200, available: true`;
   the live URLs are first and pass, so the captures are never read while the live pages answer.

---

## Confidence, cautions and remaining unknowns

- **Confidence in both rows: high** on the mechanical legs (instrument PASS, run above) and high on
  the content: each quote was read in its paragraph, not only matched.
- **S628 quote sits in the page's Summary paragraph.** It is body text (BOILER: not title, h1 or
  meta; not on the site root) and states the purpose the row teaches. If a reviewer wants a
  deep-body sentence instead, the essay also carries and locates
  "An amulet is then specially produced to manipulate negative and positive influences according to
  personal and temporal specifications." (verified `locate True`, 1 window, 4 function words) — a
  swap the L1 may make without re-opening the source.
- **S629 is a PDF.** The quote was verified through the instrument's own `pypdf 5.4.0` extraction
  path, which is what acceptance runs; a different extractor may space the text differently. The
  chosen sentence sits in a cleanly extracted region (no hyphen or ligature damage), unlike
  neighbouring sentences such as "modern-da y equivalent of yantra".
- **Host reuse:** `rubinmuseum.org` already carries row S251 (a different page). DISTINCT counts
  hosts, never pages, so this is legal, but if the round's host count is tight the L1 may prefer to
  replace S628 with the ANU chapter (a fresh host) and keep the gau row for a later round — that
  costs the Tibetan gau coverage this seat was asked for.
- **Thai terminology:** the page glosses *phra khrueang* in its abstract; the quoted sentence itself
  says only "amulet". The draft sentence keeps the term and attributes it to the page, which is
  accurate; do not let the entry claim the quote uses the Thai word.
- **Unknowns:** (a) no Thai museum object record could be opened this session (Met 429, BM 403,
   NGV textless), so the Thai row rests on a journal article rather than an object record;
  (b) captures unverified (archive refused); (c) I did not survey whether the lane already owns the
  Somdet To material — the sibling connect report
  (`ConnectInLaneAmulets59.md`) lists no Thai amulet owner, so the ground looks free, but the L1
  holds the final census.
