# ScoutSources100 — work song and labour chant: candidate sources

Round 100, wave 1, seat ScoutSources100. Access date for every capture: **2026-11-06**.
Lane root: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Registry checked: `corpus/SOURCES.md` (1127 lines, rows S001–S1017). No candidate URL or
host+path below occurs in it — `grep -c -F` per URL returned 0 for all ten (command and rc
in §4). These are new rows, not duplicates.

No S-ids assigned (the L1 owns numbering).

## 1. Admitted candidates (10; 8 tier A, 2 tier B)

| key | source | tier | http | bytes | quote (≤25 words, count 1) | supports |
|---|---|---|---|---|---|---|
| C1 | Terry, *The Shanty Book, Part I: Sailor Shanties* (1921), PG #20774 | A | 200 | 109627 | "The song was rendered by one singer, called the shantyman, and the chorus by the sailors" | leader/response; shanty repertory; improvised verses; satire |
| C2 | Sharp, *English Folk-Chanteys* (1914), IA djvu text | A | 200 | 113227 | "by assuring unanimity of action, to aid them in the efficient execution of their collective task" | rhythm fits the task; capstan vs pulling; shanty |
| C3 | Allen, Ware & Garrison, *Slave Songs of the United States* (1867), IA djvu text | A | 200 | 225579 | "two measures are to be sung to each stroke, the first measure being accented by the beginning of the stroke" | rowing stroke ↔ measure; boat/field repertory |
| C4 | Bücher, *Arbeit und Rhythmus* (1896), IA djvu text | A | 200 | 661502 | "es ist kein Zweifel, dass das Festhalten eines gleichen Zeitmasses der Bewegung dadurch erleichtert wird" | work rhythm from the tool's stroke; pounding/craft |
| C6 | Collinson, "The Oyster Dredging Songs of the Firth of Forth", *Scottish Studies* 5 (1961) | A | 200 | 589572 | "They were said to be chanted by a song-leader among the boat's crew, who repeated his lines in chorus" | leader/response; improvised; learned/owned/retired |
| C7 | Blankenhorn, "A New Approach to the Classification of Gaelic Song", *Oral Tradition* 32/1 (2018) | A | 200 | 4927689 | "Waulking-songs are work songs performed to facilitate the fulling of handwoven woolen cloth" | waulking/rowing/harvest/quern repertories; task over theme |
| C8 | Bourke, *Working and Weeping* (UCD, 1988) | B | 200 | 842807 | "a work song helps the people who sing it to establish the rhythm of their work and to coordinate their effort" | rhythm + coordinated effort; solidarity |
| C11 | Purser, "Hebridean Rowing Songs", *Angles* 17 (2024) | A | 200 | 868447 | "Rowing songs survive in the Scottish Gaelic tradition in some numbers, but they are no longer in use" | rowing; retirement and reuse of a repertory |
| C12 | Whall, *Ships, Sea Songs and Shanties* (1913), IA djvu text | A | 200 | 135268 | "one mariner sings out and the rest follow in the same tune" | leader/response; hauling; 1450 *Complaynt of Scotland* |
| C17 | SIL Philippines, "Mangali and Tanudan Valley Music" (field documentation) | B | 200 | 43071 | "Tug-om is sung by women while pounding rice or coffee." | pounding; non-Atlantic field repertory |

Every quote is an exact substring of its `quote_capture` `.txt` file after collapsing
whitespace runs to one space, and occurs exactly once there. Counts and word counts are
reproduced in §4.

### What the ten jointly cover against the frozen topic line

- **song leader and the crew's response** — C1, C2, C6, C8, C12 (five independent traditions:
  British shanty, Scottish dredging, Gaelic waulking, and the 1450 *Complaynt*).
- **fit of rhythm to the task** — C2 (capstan vs pulling), C3 (measure per oar-stroke, 16–30
  strokes a minute), C4 (the stroke's sound as the measure), C8 (rhythm and breathing).
- **occupational repertories** — shanty C1/C2/C12; oyster dredging C6; waulking/rowing/harvest/
  quern C7; iorram C11; Kalinga pounding/harvest C17.
- **improvised verses** — C1 (topics "many and varied", personal allusions, sarcasm about food),
  C6 (words "always improvised", informants' own words).
- **complaint and satire inside work song** — C1 only; the weakest axis, flagged in §5.
- **learned, owned or retired** — C6 (the last two men who knew the Dreg Song), C11 (rowing
  songs no longer in use; survive as waulking songs), C7 (repertory classified by task).
- **design procedure** — C4 is the only candidate that states a generative rule (rhythm is
  derived from the stroke and eased by marking it), and C2/C3 give the task→tempo mapping.

## 2. Search log (17 queries, 2026-11-06)

| # | query | outcome |
|---|---|---|
| 1 | Whall Sea Songs and Shanties Project Gutenberg | no PG edition; led to IA `shipsseasongssha00whal` and PG #20774 (Terry) |
| 2 | Cecil Sharp English Folk-Chanteys archive.org full text | direct `_djvu.txt` → C2 |
| 3 | Slave Songs of the United States 1867 Gutenberg rowing songs | no PG edition; IA `slavesongsofunit00alle` → C3 |
| 4 | Bücher Arbeit und Rhythmus archive.org full text | 1896 IA scan → C4 |
| 5 | 1911 Encyclopaedia Britannica Chanty Wikisource | page does not exist at that title (404 ×3) → §3 |
| 6 | waulking songs Hebrides open access article full text | Bourke UCD PDF → C8; also Cheape, Brewer, *Scottish Studies* |
| 7 | journal.oraltradition.org work songs call and response article | Blankenhorn 32/1 → C7; also Pigott 28/1, dreg-song article 28/2 |
| 8 | African American work song chain gang field holler open access scholarly article | LoC essay (403), Gioia (restricted), JRSM note; no new open A/B admitted |
| 9 | rice pounding songs ethnomusicology open access full text | SIL Kalinga page → C17; Atlantic 1958 (paywalled), ARCE (403) |
| 10 | sailors' chantey hauling halyard rhythm work song open access article | Camus *Miranda* 45765 (French, not opened), NPS/LoC pages |
| 11 | Ted Gioia "Work Songs" book introduction excerpt open access | only an unauthorized mirror and a restricted IA loan → §3 |
| 12 | Folk Music Journal work song occupational song open access article | Pickering/Robertson/Korczynski 2007 is JSTOR-only → §3 |
| 13 | Blankenhorn "A New Approach to the Classification of Gaelic Song" work songs pdf | mospace bitstream 404 → journal PDF (C7) |
| 14 | "dreg songs" Firth of Forth oyster dredging song Oral Tradition | Collinson *Scottish Studies* open PDF → C6 |
| 15 | "call and response" work song Africa labour rhythm open access scholarly | Locke (DOAJ metadata only), Gunderson (403) → §3 |
| 16 | Gunderson "Musical Labor" Sukuma Tanzania work songs pdf | Brill front matter, Smithsonian page (403) → §3 |
| 17 | "Work Songs" "Old Kingdom" elite tombs pdf reaping song call and response | Roos, *JEOL* 47 — server 503 ×4 → §3 |

## 3. Rejected / unreachable (with flip condition)

| key | URL | result | reason | flip |
|---|---|---|---|---|
| C5 | `en.wikisource.org/wiki/1911_Encyclopædia_Britannica/Chanty` (+ `Encyclopaedia` spelling, + `action=raw`) | 404 ×3 | Wikisource has no EB1911 "Chanty" transcription; API search for the title returns nothing | a scan-backed EB1911 volume 5/6 copy on Wikisource or IA that carries the entry |
| — | `mospace.umsystem.edu/bitstream/handle/11655/2460/OT32-1Blankenhorn.pdf` | 404 | DSpace bitstream path retired | superseded: C7 taken from the journal's own PDF |
| C9 | `loc.gov/collections/songs-of-america/.../traditional-work-songs/` | 403 | bot wall on loc.gov | LoC JSON API or an open mirror |
| C10 | `britannica.com/art/work-song-music` | 403 | bot wall | an open reference work with the same scope |
| C13 | `exorientelux.nl/download/JEOL/JEOL_47_08_Roos.pdf` (Roos, work songs in Old Kingdom tombs) | 503 ×4 | host down for the whole retry window | retry when the host recovers — peer-reviewed, would be tier A for Egyptian reaping/hauling songs |
| C14 | `music.si.edu/story/musical-labor-performed-northwest-tanzania` (Gunderson) | 403 | bot wall | an open copy of the same essay |
| C15 | `jaauth.journals.ekb.eg/article_149934_...pdf` (Merzeban, work songs in Egyptian tombs) | connection error ×4 | host unreachable | retry from a reachable network |
| C16 | `vmis.in/arce-categories/music_in_context_innercat/94` (ARCE work songs, Naga pounding song) | 403 | bot wall | an open ARCE catalogue page |
| — | Gioia, *Work Songs* (Duke 2006) | not opened | only an unauthorized full-text mirror (copyright) and a restricted IA loan | a publisher open-access edition or a library copy the lane may cite |
| — | Pickering, Robertson & Korczynski, "Rhythms of Labour", *Folk Music Journal* 9/2 (2007) | not opened | JSTOR-only, no open copy found | an EFDSS open deposit |
| — | Camus, "Vienne bientôt l'avitailleur", *Miranda* 45765 | not opened | open, but French-language and duplicative of C1/C2 on the halyard point | open if a French-language quote is wanted |

Transient failures were retried up to four attempts with 20 s backoff; every attempt is
recorded in `candidates.json` under `attempts`. No 403/404/503 was retried as if transient
beyond that rule, and no wall was circumvented (no browser, no `-k`, no login).

## 4. Commands and rc

Registry duplicate check (rc=0), run from the lane root:

```
for u in 'gutenberg.org/cache/epub/20774/pg20774.txt' 'archive.org/download/englishfolkchant00shar' \
         'archive.org/download/slavesongsofunit00alle' 'archive.org/download/arbeitundrhythm00bcgoog' \
         'open.journals.ed.ac.uk/ScottishStudies/article/download/243' \
         'oraltradition.org/wp-content/uploads/files/articles/32i/05_32.1.pdf' \
         'researchrepository.ucd.ie/server/api/core/bitstreams/f5b0128a' \
         'journals.openedition.org/angles/pdf/7360' 'archive.org/download/shipsseasongssha00whal' \
         'philippines.sil.org/resources/audio_and_video/mangali'; do
  printf '%s\t%s\n' "$(grep -c -F -- "$u" corpus/SOURCES.md)" "$u"; done
```
Output: `0` for all ten.

Capture hashes (rc=0): `sha256sum *` in `captures/`, reproduced in `candidates.json`
(`captures[].sha256`).

Quote counts (rc=0): each quote was counted with
`re.sub(r"\s+", " ", open(capture).read()).count(quote)` — result `1` for all ten, word
counts 10–21 (limit 25). The two that first returned 0 were fixed before admission:
C4 (pdftotext hyphenated *glei-chem*) was re-quoted on an unbroken sentence; C6 used a
typographic apostrophe (`boat’s`, U+2019) in the capture.

## 5. Gaps left for the entry

- **Complaint and satire** rests on C1 alone. A second, non-shipping source on licensed
  complaint (prison/chain-gang or agricultural) would harden that axis; the open candidates
  found were all walls or paywalls (§3).
- **Pounding** rests on C17 (tier B, one sentence) plus C4's craft examples. Roos (C13) and
  the ARCE Naga recording (C16) would fix this if either host reopens.
- **Learning and ownership** is thin: C6 gives the last two bearers, C11 the retirement, but
  no source yet describes how a leader is chosen or a song is transmitted as property.
