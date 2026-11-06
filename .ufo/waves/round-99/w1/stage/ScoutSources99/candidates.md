# ScoutSources99 — praise poetry and panegyric: candidate sources

- seat: ScoutSources99 (leaf, read-only research)
- round: 99, wave w1, milestone r99-v1
- access date: 2026-11-06 (ISO), all captures fetched today
- target: >= 6 admitted tier A/B candidates supporting a claim about praise poetry; 11 admitted (6 A, 5 B), 3 rejected
- machine record: `candidates.json` (quotes re-counted from the capture bytes at build time)
- captures: `captures/` (raw + text derivatives; every file hashed in `candidates.json`)

## Registry duplicate check

`grep -c -F '<url>' corpus/SOURCES.md` for every candidate URL and for every host+path prefix
tested returned **0** (rc=0 for each grep). No candidate duplicates an existing registry row.
Checked prefixes: `books.openedition.org/obp/1192`, `openbookpublishers.com/books/10.11647/obp.0025`,
`journal.oraltradition.org/.../3iii/6_opland.pdf`, `.../20ii/Barber.pdf`, `.../16i/Groenewald.pdf`,
`.../10i/8_kaschula.pdf`, `iranicaonline.org/articles/courts-and-courtiers-x`,
`gutenberg.org/cache/epub/10717`, `gutenberg.org/files/9842`, `skaldic.org`,
`archive.org/stream/book-3-purananuru`, `archive.org/download/80204dff-...`,
`journals.uni-goettingen.de/wom/article/download/2303`, `asnc.cam.ac.uk/resources/mpvp`,
`mural.maynoothuniversity.ie/id/eprint/19500`, `journal.ru.ac.za/.../africanmusic/article/download/1116`.

The registry already holds three `journal.oraltradition.org` rows (S985, S990, S993) but none of
these four articles; host reuse is not duplication.

## Candidate table

| key | url | tier | http | bytes (quote capture) | quote (truncated) | admitted |
|---|---|---|---|---|---|---|
| C1 | https://archive.org/download/80204dff-c8a9-4155-a539-7ee980102875/80204dff-c8a9-4155-a539-7ee980102875_djvu.txt | B | 200 | 1431723 | In return the ruler acknowledges their praise by gifts or money whi… | yes |
| C2 | https://journal.oraltradition.org/wp-content/uploads/files/articles/3iii/6_opland.pdf | A | 200 | 49051 | it is his duty to greet Lord with a royal praise name | yes |
| C3 | https://journal.oraltradition.org/wp-content/uploads/files/articles/20ii/Barber.pdf | A | 200 | 39602 | Obscurity in praise poetry could be deployed for political reasons. | yes |
| C4 | https://journal.oraltradition.org/wp-content/uploads/files/articles/16i/Groenewald.pdf | A | 200 | 67894 | The praise poem for kings and chiefs has also been adapted to serve… | yes |
| C5 | https://www.journal.oraltradition.org/wp-content/uploads/files/articles/10i/8_kaschula.pdf | A | 200 | 37515 | directed at the Chief, decrying what was unworthy, praising what wa… | yes |
| C6 | https://www.iranicaonline.org/articles/courts-and-courtiers-x/ | — | 403 | 5539 | — (Cloudflare challenge shell) | no |
| C7 | https://www.gutenberg.org/cache/epub/10717/pg10717.txt | A | 200 | 320993 | Yet praise is overtaken of distaste, wherewith is no justice, but f… | yes |
| C8 | https://skaldic.org/m.php?p=text&v=intro&i=1258 | — | 0 | 0 | — (3x connect timeout) | no |
| C9 | https://www.gutenberg.org/files/9842/9842-h/9842-h.htm | A | 200 | 268434 | A more choice act of mine will be To celebrate thy praise in song | yes |
| C10 | https://archive.org/stream/book-3-purananuru/BOOK3-Purananuru_djvu.txt | B | 200 | 44945 | The main themes found in Purananuuru are praise of the ruler, patro… | yes |
| C11 | https://journals.uni-goettingen.de/wom/article/download/2303/1986/5234 | B | 200 | 32101 | the praise-singing function is by far the most obvious and audible … | yes |
| C12 | https://www.asnc.cam.ac.uk/resources/mpvp/wp-content/uploads/2013/02/Introduction-to-Skaldic-Poetry_Debbie-Potts.pdf | B | 200 | 100607 | There certainly was money in poetry for the skald; court poets woul… | yes |
| C13 | https://mural.maynoothuniversity.ie/id/eprint/19500/1/Kavanagh%20Emer%20Signs%20and%20Wonders.pdf | B | 200 | 616619 | a poet should not satirize or over-praise a subject, as the fili de… | yes |
| C14 | https://journal.ru.ac.za/index.php/africanmusic/article/download/1116/591/593 | B | 200 | 89409 | not above converting praise to satire of a potential patron’s miser… | no |

Full quotes, exact byte spans and per-file sha256 are in `candidates.json`.

## Admitted, by the claim each one carries

| key | source | tier | claim it supports | quote words | count |
|---|---|---|---|---|---|
| C1 | Finnegan, *Oral Literature in Africa*, ch. 5 "Panegyric" (OBP 2012, CC BY) | B | patronage and reward: the ruler answers praise with a public gift or payment; praise withheld or derogatory allusion as negative sanction (alt quote) | 16 / 17 | 1 / 1 |
| C2 | Opland, "Lord of the Singers", *Oral Tradition* 3/3 (1988) | A | the praise singer's office: the imbongi's duty to greet with a royal praise name; audience repeats the name | 12 | 1 |
| C3 | Barber, "Text and Performance in Africa", *Oral Tradition* 20/2 (2005) | A | praise epithet as performance: obscurity and allusion encode discreet criticism of power | 10 | 1 |
| C4 | Groenewald, "I Control the Idioms", *Oral Tradition* 16/1 (2001) | A | the office and its audiences: royal praise adapted to unions, campaigns, public ceremonials | 17 | 1 |
| C5 | Kaschula, "Mandela Comes Home", *Oral Tradition* 10/1 (1995) | A | praise performance: address to the chief, licensed criticism inside praise, political censorship | 12 | 1 |
| C7 | Pindar, *Extant Odes*, trans. Myers, Gutenberg #10717 | A | the limits of flattery: praise resented by the covetous; commissioned odes for Hieron and Theron | 16 | 1 |
| C9 | *Y Gododdin*, trans. Williams 1852, Gutenberg #9842 | A | the praise poet's office: praise instead of reproach for a fallen patron | 14 | 1 |
| C10 | *Purananuru*, English trans. Rajeswari (archive.org) | B | Sangam puram patronage: praise of the ruler, bards honoured with gifts before moving on | 15 | 1 |
| C11 | Kertzer, "Trio Da Kali and the Mande Griot Tradition", *World of Music* | B | the office and genealogical recitation: griot roles = genealogist, historian, advisor, praise-singer (Hale 1998 quoted) | 12 | 1 |
| C12 | Potts, *Skaldic Poetry: A Short Introduction* (Cambridge ASNC) | B | patronage, reward and rivalry: money in poetry for the skald; skalds competing for a patron's favour (alt quote) | 15 / 17 | 1 / 1 |
| C13 | Kavanagh, *Signs and Wonders* (Maynooth PhD thesis) | B | the limits of flattery: law-text rule against over-praise, because the fili lived on the patron's reward | 19 | 1 |

Coverage against the six frozen phrases (for the entry writer, not a claim of the entry):
`praise poetry` (C3, C4, C10, C12), `praise singer` (C1, C2, C5, C11), `panegyric` (C1, C10),
`genealogical recitation` (C1, C11), `praise epithet` (C3, C4, C12), `praise performance` (C2, C5, C9).

## Rejects

- **C6 — Encyclopaedia Iranica, "Courts and Courtiers x. Court Poetry"**. UNREACHABLE. Article page
  returned HTTP 403 with a Cloudflare "Just a moment..." shell (5539 bytes, 3 attempts); the
  `?generate_pdf=1` endpoint returned HTTP 403 (5621 bytes, 1 attempt). A bot challenge is a wall,
  not a transient failure, so no further retries. **Flip:** an open mirror of the same entry, or a
  peer-reviewed article on Persian *madḥ* / the *qaṣīda* panegyric, opened at source.
- **C8 — Skaldic Project, Óláfsdrápa introduction (skaldic.org)**. UNREACHABLE. Three attempts,
  `curl` rc=28 (connect timeout after 30 s), 0 bytes each. **Flip:** the database answers from this
  host, or the printed *SkP* volume text is available. Covered instead by C12 (Potts, ASNC).
- **C14 — Gourlay, "Long Trumpets of Northern Nigeria", *African Music* 6/2**. REJECTED for anchor
  scope: the article's subject is trumpets; the praise-singer patronage passage is a six-line aside,
  so a registry row scoped to praise poetry would be mis-anchored even though the quote (praise
  converted to satire when the gift is inadequate) is sound. **Flip:** a dedicated study of Hausa
  *maroka* praise-singing and patron exchange (e.g. Smith 1957, *Africa* 27/1) opened at source.
- **C1 primary URL (OpenEdition chapter page)** — not a candidate reject but a capture note: the
  page served only the chapter preview (89,742 chars of text, of which the chapter body is one
  paragraph). The OBP chapter page returned HTTP 429 on three attempts. Full text taken from the
  Internet Archive copy of the same CC BY edition (C1b), which is what the quote is counted in.

## Search log (14 queries, web_search, 2026-11-06)

1. `Finnegan "Oral Literature in Africa" Open Book Publishers panegyric praise poetry chapter` → C1 (ch. 5 "Panegyric", pp. 111–143).
2. `Opland "Xhosa Oral Poetry" imbongi izibongo praise poet open access pdf` → book is paywalled; led to C2 (open *Oral Tradition* article) and C5.
3. `Barber "I Could Speak Until Tomorrow" oriki Yoruba praise poetry archive.org` → book is borrow-only; led to C3 (open Barber article).
4. `Hale "Griots and Griottes" praise singing genealogy Mande open access` → book is borrow-only; led to C11 (open article quoting Hale).
5. `Old Irish bardic poetry praise poem filid CELT corpus electronic texts edition` → CELT bardic section (no single open praise text with a usable English quote); led to C13 via the satire query.
6. `Encyclopaedia Iranica panegyric madh qasida court poet entry` → C6 (blocked).
7. `Pindar extant odes Myers translation Project Gutenberg epinician victory ode` → C7.
8. `skaldic poetry drápa praise poem king skald open access database introduction` → C8 (timeout) and C12.
9. `Sangam Tamil puram praise poetry patron bard pulavar open access translation anthology` → C10.
10. `"Oral Tradition" journal open access article praise poetry panegyric Africa izibongo` → C2, C3, C4, C5.
11. `Open Encyclopedia of Anthropology entry poetry oratory praise performance` → dead end: the A–Z has no poetry/praise entry (closest: Voice, Freedom of speech, Feasting).
12. `Y Gododdin Welsh heroic praise poetry translation open access Book of Aneirin` → C9.
13. `Irish bardic satire áer poet praise blame power of satire early Irish law open access` → C13.
14. `Hausa maroki praise singer patronage reward open access article` → C14 (rejected on scope).

## Fetch and verification commands

- Fetch driver: `bash fetch.sh` (scratch), per-URL `curl -L --max-time 30 -sS`, retries 3x with 20 s
  backoff on transient failure; log at scratch `fetch.log`. rc=0 for the driver.
- Attempts recorded: C1 200/244383 (1); C2 200/122076 (1); C3 200/895589 (1); C4 200/941966 (1);
  C5 200/678241 (1); C6 403/5539 (3); C7 200/320993 (1); C8 rc=28/0 (3); C9 200/412673 (1);
  C10 200/191267 (1); C11 200/34807 HTML stub (1) then 200/121791 PDF at the galley URL (1);
  C12 200/294812 (1).
- C1b: `curl -L --max-time 60` → 200, 1431723 bytes, rc=0.
- C13: 200, 1897884 bytes, rc=0. C14: 200, 1441621 bytes, rc=0.
- PDF → text: `pdftotext -layout` (poppler 26.10.0), rc=0 for C2–C5, C12–C14, C11b.
- HTML → text: python3 tag strip (`re.sub` on `<script|style|head>` then tags, `html.unescape`,
  whitespace collapse), rc=0 for C1, C9, C10, C11 stub.
- Quote counts: `python3 build.py` rc=0; every admitted quote has `quote_count == 1` after
  `re.sub(r"\s+"," ")` on the capture text, and is <= 25 words (max used: 19).
- Hashes: `sha256sum captures/*` rc=0; per-file values in `candidates.json`.

## Notes for the L1

- No S-ids assigned, as instructed.
- Nothing was written outside this stage dir and `/fast/scratch/hyaku/kotodama-r99/ScoutSources99/`
  (scratch removed before yield). No git/jj commands were run.
- Tooling installed: none.
