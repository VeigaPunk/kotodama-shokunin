# ScoutSources99 — source scouting for the praise poetry / panegyric entry

- round 99, wave w1, milestone r99-v1, access date 2026-11-06
- stage: `.ufo/waves/round-99/w1/stage/ScoutSources99/` (`candidates.json`, `candidates.md`, `captures/`)
- scope: read-only research; no S-ids assigned; nothing written outside the stage dir and scratch

## Result

**11 admitted candidates (6 tier A, 5 tier B), 3 rejected, 14 opened.** Target was >= 6 admitted
so that two may drop; the margin is five.

| key | source | tier | claim carried |
|---|---|---|---|
| C1 | Finnegan, *Oral Literature in Africa*, ch. 5 "Panegyric" (OBP 2012, CC BY) | B | patronage and reward; praise withheld as negative sanction |
| C2 | Opland, "Lord of the Singers", *Oral Tradition* 3/3 (1988) | A | the imbongi's duty to greet with a royal praise name; audience repetition |
| C3 | Barber, "Text and Performance in Africa", *Oral Tradition* 20/2 (2005) | A | praise epithet as performance; obscurity encoding criticism |
| C4 | Groenewald, "I Control the Idioms", *Oral Tradition* 16/1 (2001) | A | the office and its audiences (unions, campaigns, ceremonials) |
| C5 | Kaschula, "Mandela Comes Home", *Oral Tradition* 10/1 (1995) | A | praise directed at the chief; licensed criticism; censorship |
| C7 | Pindar, *Extant Odes*, trans. Myers, Gutenberg #10717 | A | limits of flattery; commissioned epinician for named patrons |
| C9 | *Y Gododdin*, trans. Williams 1852, Gutenberg #9842 | A | praise instead of reproach for a fallen patron |
| C10 | *Purananuru*, English trans. Rajeswari (archive.org) | B | Sangam puram patronage and gift exchange |
| C11 | Kertzer, "Trio Da Kali and the Mande Griot Tradition", *World of Music* | B | griot roles: genealogist, historian, advisor, praise-singer |
| C12 | Potts, *Skaldic Poetry: A Short Introduction* (Cambridge ASNC) | B | money in poetry for the skald; rivalry for a patron's favour |
| C13 | Kavanagh, *Signs and Wonders* (Maynooth PhD thesis) | B | law-text rule against over-praise; the fili on the patron's reward |

Every admitted quote is an exact substring of its `.txt` capture, <= 25 words, `count == 1` after
`re.sub(r"\s+"," ")`; counts and sha256 are in `candidates.json` and were recomputed from the
capture bytes by `build.py` (rc=0).

## Rejects

- **C6 Encyclopaedia Iranica, "Courts and Courtiers x. Court Poetry"** — UNREACHABLE: HTTP 403
  Cloudflare challenge shell (5539 bytes, 3 attempts); `?generate_pdf=1` HTTP 403 (5621 bytes).
  Flip: an open mirror or a peer-reviewed article on Persian *madḥ* / *qaṣīda*.
- **C8 Skaldic Project, Óláfsdrápa introduction** — UNREACHABLE: 3x `curl` rc=28 connect timeout,
  0 bytes. Flip: host answers. Covered instead by C12.
- **C14 Gourlay, "Long Trumpets of Northern Nigeria", *African Music* 6/2** — REJECTED for anchor
  scope: the praise-singer patronage passage is a six-line aside in an article about trumpets.
  Flip: a dedicated study of Hausa *maroka* praise-singing (e.g. Smith 1957, *Africa* 27/1).

## Search log (14 queries)

Finnegan OBP panegyric chapter; Opland imbongi/izibongo open access; Barber oriki archive.org;
Hale griots and griottes; Old Irish bardic poetry CELT; Iranica panegyric madh qasida; Pindar
Myers Gutenberg epinician; skaldic drápa open access; Sangam puram praise poetry patron bard;
*Oral Tradition* praise poetry articles; Open Encyclopedia of Anthropology poetry/oratory;
Y Gododdin translation; Irish satire áer and early Irish law; Hausa maroki patronage.
Per-query routing and dead ends are in `candidates.md` § Search log.

Dead ends worth recording: Opland's and Barber's and Hale's books are all access-controlled
(borrow-only or paywalled), so the open journal articles and the open article quoting Hale were
used instead; the Open Encyclopedia of Anthropology has no poetry/praise entry.

## Commands (with rc)

- `bash fetch.sh` — per-URL `curl -L --max-time 30 -sS`, 3 attempts with 20 s backoff on transient
  failure; rc=0. Attempt log: C1 200, C2 200, C3 200, C4 200, C5 200, C6 403 x3, C7 200, C8 rc=28 x3,
  C9 200, C10 200, C11 200 (HTML stub) then 200 (PDF galley), C12 200.
- `curl -L --max-time 60` for the Internet Archive full text of Finnegan → 200, 1431723 bytes, rc=0.
- `pdftotext -layout` (poppler 26.10.0) for C2–C5, C11b–C14 → rc=0 each.
- python3 tag strip for C1, C9, C10, C11 stub → rc=0.
- `python3 build.py` (hashes, byte sizes, quote counts, JSON emit) → rc=0, 11 admitted of 14.
- `sha256sum captures/*` → rc=0; values embedded in `candidates.json`.
- `grep -c -F <url> corpus/SOURCES.md` for 16 URL/prefix strings → 0 for every one, rc=0.

## Notes

- Tooling installed: none.
- No git or jj command was run; nothing committed.
- Scratch `/fast/scratch/hyaku/kotodama-r99/ScoutSources99/` removed before yield.
- Boundary reminder for the entry writer: `corpus/knowledge/linguistics/orality-formulaic-language.md`
  §3 owns praise-names as formula lexicon; C1/C3/C4/C12 here carry the institutional claims
  (office, patronage, occasion, rivalry, satire), not the formula-lexicon claim.
