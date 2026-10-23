# ScoutDanelawNames — round 58, claim C source item (Scandinavian settlement names in England)

Seat: KotodamaR58A2.ScoutDanelawNames (scout, leaf). S-ids: S516, S517. Accessed 2026-10-23.
Two rows offered, both pass all four rowcheck legs. Both URLs are absent from `corpus/SOURCES.md`: `grep -c -F` gave 0 for `vsnrweb`, 0 for the combined `emidsvikings` / `archaeologydataservice.ac.uk/library` / `eprints.nottingham.ac.uk/74185` patterns, and 0 for the combined `repository.nottingham.ac.uk` / `a9d0a620-a3b5-490b-9f0c-898ec21de02b` / `Fellows-Jensen.pdf` patterns.

## (1) Registry rows

| S516 | Gillian Fellows-Jensen, 1995 (Dorothea Coke Memorial Lecture delivered at University College London 21 February 1994; published for the College by the Viking Society for Northern Research), *The Vikings and their Victims: The Verdict of the Names* — http://www.vsnrweb-publications.org.uk/Fellows-Jensen.pdf (direct, HTTP 200) | paper | A | the distribution of Scandinavian -bý place-names as evidence of where Danish settlers stayed | p. 17 (PDF page 19): "the presence of numerous Scandinavian place-names in -bý points to the survival of an enclave of Danes here" | A dense cluster of Scandinavian place-names ending in -bý in one district can show that an enclave of Danes survived there. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S517 | Joshua Neal, 2023 (PhD thesis, School of English, University of Nottingham; supervisors Jayne Carroll and John Baker; CC BY 4.0), *A Study on Anglo-Scandinavian bý(r)-names: Statistical Analysis and Case-Studies*, full-text PDF — https://repository.nottingham.ac.uk/bitstreams/a9d0a620-a3b5-490b-9f0c-898ec21de02b/download (direct, HTTP 200 after the repository's redirect to its /server/api/core/bitstreams/…/content file) | paper | B | what a Grimston- or Toton-hybrid place-name is built from and how it has been read | p. 284 (PDF page 294): "So-called Grimston-/Toton-hybrids, Anglo-Scandinavian place-names generally held to be ON personal name + OE tūn formations, have been a focus point." | Grimston or Toton hybrids are mixed Anglo-Scandinavian place-names that join an Old Norse personal name to the Old English generic tūn. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Provenance:
- **S516 is tier A.** It is the Viking Society for Northern Research's own free PDF, linked from its publications home page http://www.vsnrweb-publications.org.uk/. The title page reads "© UNIVERSITY COLLEGE LONDON 1995 / REPRINTED IN THE UNIVERSITY OF BIRMINGHAM 1998". The author is styled "Reader in Name Studies in the University of Copenhagen".
- **S517 is tier B, a doctoral thesis.** The repository record https://repository.nottingham.ac.uk/entities/publication/314dc762-2734-4b08-8773-07b55ba31a08 (reached from https://eprints.nottingham.ac.uk/id/eprint/74185) states "Re-use License info … https://creativecommons.org/licenses/by/4.0" and links this PDF.
- **Extraction.** Text was extracted with pypdf 5.4.0, the locator's own PDF path. The S517 quote's `tūn` is a precomposed character in that extraction.

## (2) Gate lines

- S516 — http://www.vsnrweb-publications.org.uk/Fellows-Jensen.pdf — accessed 2026-10-23 — p. 17 (PDF page 19): “the presence of numerous Scandinavian place-names in -bý points to the survival of an enclave of Danes here”. Grounds: A dense cluster of Scandinavian place-names ending in -bý in one district can show that an enclave of Danes survived there. Seat: ScoutDanelawNames.
- S517 — https://repository.nottingham.ac.uk/bitstreams/a9d0a620-a3b5-490b-9f0c-898ec21de02b/download — accessed 2026-10-23 — p. 284 (PDF page 294): “So-called Grimston-/Toton-hybrids, Anglo-Scandinavian place-names generally held to be ON personal name + OE tūn formations, have been a focus point.” Grounds: Grimston or Toton hybrids are mixed Anglo-Scandinavian place-names that join an Old Norse personal name to the Old English generic tūn. Seat: ScoutDanelawNames.

## (3) rowcheck output

Command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutDanelawNames/rows.md`

```
S516 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: http://www.vsnrweb-publications.org.uk/Fellows-Jensen.pdf | BOILER: root-clear http://www.vsnrweb-publications.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['dane', 'encla', 'name', 'place', 'scand', 'survi'] | TOPIC: quote_hits=1 function_words=5 page_hits=64 page_terms=43 need=1/2/3/2
S517 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://repository.nottingham.ac.uk/bitstreams/a9d0a620-a3b5-490b-9f0c-898ec21de02b/download | BOILER: root-clear https://repository.nottingham.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['anglo', 'gener', 'grims', 'hybri', 'name', 'perso'] | TOPIC: quote_hits=1 function_words=5 page_hits=967 page_terms=717 need=1/2/3/2
exit=0
```

The same command was also run with `--entry /fast/scratch/hyaku/kotodama-r58/ScoutDanelawNames/mock-entry.md`. That mock file holds exactly the six draft sentences below. The output was the same two all-PASS lines with exit 0, so RELEVANCE checks (c) and (d) pass on these sentences.

Per-sentence check: each sentence's stems overlap at least 2 stems of its row's quote and at least 2 of its teaches cell. The smallest overlap was S516 sentence 3, with quote stems `dane`, `name`, `scand` and the same three teaches stems.

## (4) Draft sentences

These sentences are written for the worldbuilder's decisions: which language layer a name belongs to, what it is built from, who renames, and under what conditions.

S516 (the page carries all three: printed pp. 17, 19 and 21):
- Fellows-Jensen reads the island of Flegg in Norfolk, where numerous Scandinavian place-names in -bý cluster, as the home of an enclave of Danes that survived after most Vikings were driven out of East Anglia in 903 (S516).
- Where invading Danes stayed only for short periods, as at the sites of their winter quarters, they left the local place-names alone, but where they settled more permanently they sometimes gave the settlements they seized completely new Scandinavian names such as Kirkby and Derby (S516).
- Later the Danes detached specialised units from old English estates and named them in -bý for their function or site, as in Sowerby ‘the settlement on sour ground’, a Scandinavian name-type that also occurs across the Pennines in Cumbria and Lancashire and in the Isle of Man (S516).

S517 (the page carries all three: printed p. 284):
- A Grimston- or Toton-hybrid is an Anglo-Scandinavian place-name built from an Old Norse personal name plus the Old English generic tūn (S517).
- Such hybrids have commonly been interpreted as Anglo-Saxon estates taken over by Scandinavian settlers and perhaps partially renamed, the settler's Old Norse personal name standing before the Old English generic (S517).
- Parsons, as the thesis reports, offers two other readings of these Anglo-Scandinavian place-names: Scandinavian settlers may have adopted Old English tūn in the sense ‘English village’ and coined names with it, or English speakers coined Grimston-/Toton-hybrids for estates held by Scandinavian landowners (S517).

The second S517 sentence's clause "the settler's Old Norse personal name standing before the Old English generic" is a gloss that joins the quote (ON personal name + OE tūn) to the next sentence on the page ("taken over by Scandinavian settlers"). The L1 may drop the gloss if it wants the sentence to carry only page text.

Swap options from the S516 URL. Both passed all four legs in a separate rowcheck run of `alt.md` (exit 0). Each could replace the S516 anchor, but not stand as a second row, because one URL gives one row:
- p. 19: "they showed no tendency to interfere with the local place-names in these cases". Teaches: Danish invaders who only stayed briefly in winter quarters left the local English place-names alone. Result: `S516 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS … shared=['local', 'name', 'place']`.
- p. 13: "the only evidence we have for the holding of land by men with Scandinavian personal names is the presence of place-names containing such names". Teaches: Place-names that contain Scandinavian personal names are often the sole record that such men once held land. Result: `S517 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS … shared=['conta', 'land', 'name', 'perso', 'place', 'scand']`.

Attacks a SUPPORT reviewer may raise, and the answers:
- **S516's quote is a clause, not a whole sentence.** The full sentence runs to 49 words, over the 25-word cap. The quote is its main clause, with subject and verb: "the presence … points to the survival …". "here" refers to "the island of Flegg" earlier in the same sentence.
- **S517's quote defines the hybrid but does not state the reading.** The "taken over … perhaps partially re-named" reading is the very next sentence on the same page. Only draft sentence 2 depends on it.

## (5) Rejected

- **http://vsnrweb-publications.org.uk/Swedish%20Vikings%20in%20England.pdf** (Viking Society): image-only scan. The pypdf 5.4.0 extract is empty (`wc -w sw.txt` → `0 sw.txt`), so LOCATE cannot pass.
- **https://repository.nottingham.ac.uk/entities/publication/314dc762-2734-4b08-8773-07b55ba31a08** (Neal thesis record page; reached via https://eprints.nottingham.ac.uk/id/eprint/74185): its abstract is repeated in `<meta name="description">`, `og:description` and `twitter:description`. Rowcheck on the abstract's first sentence gave: `S517 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | … | BOILER: quote-is-title-heading-or-meta`. Every abstract sentence sits in that meta content, so the row moved to the thesis PDF body.
- **https://eprints.nottingham.ac.uk/74185/**: HTTP 404, a DSpace "No item found for the identifier handle: eprint/74185" page.
- **https://archaeologydataservice.ac.uk/library/browse/details.xhtml?recordId=3001126** (BIAB abstract of Cameron 1971, "Grimston-hybrids"): HTTP 403 Cloudflare challenge, body `<title>Just a moment...</title>` with a `challenges.cloudflare.com` script. Not bypassed (QUALITY criterion 10).
- **https://emidsvikings.ac.uk/blog/two-languages-one-name-hybrid-place-names-in-the-east-midlands/** (Vikings in the East Midlands): not opened. curl gave `Could not resolve host: emidsvikings.ac.uk`, and the root failed the same way. It is known only from a search snippet, so it cannot count.
- **https://www.nottingham.ac.uk/research/groups/ins/projects/past-projects/impact-of-diasporas.aspx** (Institute for Name-Studies): a project stub listing funding and members, with no place-name claims.
- **https://www.nottingham.ac.uk/research/groups/ins/resources/vocabulary.aspx** (Institute for Name-Studies): a description of the Vocabulary of English Place-Names resource, with nothing on Scandinavian distribution.
- **https://kepn.nottingham.ac.uk/** and **https://kepn.nottingham.ac.uk/about** (Key to English Place-Names): a general guide to interpreting English place-names (about 300 words), with no Danelaw distribution text.
- **https://www.nottingham.ac.uk/research/groups/ins/index.aspx**, **…/projects/index.aspx**, **…/resources/index.aspx**, **…/public-engagement.aspx**: navigation and listing pages, used only to find links.
- **Probed and not found:** https://www.nottingham.ac.uk/research/groups/isnam/index.aspx (404), …/isnam/research/index.aspx (404), https://kepn.nottingham.ac.uk/map/place/Lincolnshire/Grimsby (404), https://www.nottingham.ac.uk/research/groups/ins/research/vikings.aspx (404), …/projects/vikings-in-the-east-midlands.aspx (404), https://www.bbc.co.uk/history/ancient/vikings/place_names_01.shtml (404), http://www.vsnrweb-publications.org.uk/The%20Vikings%20and%20their%20Victims.pdf (404; the lecture's real file is Fellows-Jensen.pdf).
- **https://www.english-heritage.org.uk/learn/story-of-england/vikings/**: HTTP 403, not pursued.
- **https://epns.nottingham.ac.uk/**: redirects to the Institute for Name-Studies Digital Survey resource page. Only the status was checked; no text was read.

Remaining unknowns:
- No `-thorpe` sentence was offered. The Fellows-Jensen lecture mentions only Danish `-torp` (Drammelstrup), and the thesis was searched only for `bý` / Grimston material.
- The Neal thesis is a 2023 doctoral thesis, so the L1 should confirm that tier B is the lane's convention for theses.

## installs:

None. pypdf 5.4.0 ran only inside `uv run --no-project --with pypdf==5.4.0`, the locator's own invocation; it is ephemeral and nothing was installed. No pacman. Scratch files are under /fast/scratch/hyaku/kotodama-r58/ScoutDanelawNames/ (rows.md, alt.md, mock-entry.md, PDFs and text extracts). No processes are left running.
