# ExecRegistry100 — appended registry rows

- lane: kotodama, round 100, wave w1; registry: corpus/SOURCES.md, appended at end of ## Registry table after S1017
- used-by (all rows): corpus/knowledge/linguistics/work-song-labour-chant.md; opened (all rows): 2026-11-06; recheck: 180d; status: mined
- evidence: reports/round-100/evidence/<id>.<ext>; manifest reports/round-100/evidence/manifest.json

| id | key | url | tier | quote | capture | sha256 (quote capture) | bytes | quote count |
|---|---|---|---|---|---|---|---|---|
| S1018 | C1 | https://www.gutenberg.org/cache/epub/20774/pg20774.txt | A | The song was rendered by one singer, called the shantyman, and the chorus by the sailors | S1018.txt | f51fe9f0f6a7b99fb88fd6c8fdeec550745811b2cc5d4c15aa1f0f17f8c97c84 | 109627 | 1 |
| S1019 | C2 | https://archive.org/download/englishfolkchant00shar/englishfolkchant00shar_djvu.txt | A | by assuring unanimity of action, to aid them in the efficient execution of their collective task | S1019.txt | 3e55e9ac9ceac003cabe4f3ce4a7da5a5803da46413db520316e6efabc28653c | 113227 | 1 |
| S1020 | C3 | https://archive.org/download/slavesongsofunit00alle/slavesongsofunit00alle_djvu.txt | A | two measures are to be sung to each stroke, the first measure being accented by the beginning of the stroke | S1020.txt | 4f1b337df7fd039f3004a95c9a5bccb59cd7d4033b58f49e2e64daf783df1bcd | 225579 | 1 |
| S1021 | C4 | https://archive.org/download/arbeitundrhythm00bcgoog/arbeitundrhythm00bcgoog_djvu.txt | A | es ist kein Zweifel, dass das Festhalten eines gleichen Zeitmasses der Bewegung dadurch erleichtert wird | S1021.txt | 65a63dfffa9ab280095110a9718d4dd0b0a99044a84c37b768d1f638126674e7 | 661502 | 1 |
| S1022 | C6 | https://open.journals.ed.ac.uk/ScottishStudies/article/download/243/269/298 | A | They were said to be chanted by a song-leader among the boat’s crew, who repeated his lines in chorus | S1022.txt | 65aebef69e2a0eccf98278690de220ecf9df5a5ddd0a7c6602e8cf708527fe93 | 35632 | 1 |
| S1023 | C7 | https://journal.oraltradition.org/wp-content/uploads/files/articles/32i/05_32.1.pdf | A | Waulking-songs are work songs performed to facilitate the fulling of handwoven woolen cloth | S1023.txt | 763c3df64a22f5f483d3cab875bf63edc3585889511308d5091fceee61a9f707 | 236686 | 1 |
| S1024 | C8 | https://researchrepository.ucd.ie/server/api/core/bitstreams/f5b0128a-3198-4d44-83bd-4a960d8ef760/content | B | a work song helps the people who sing it to establish the rhythm of their work and to coordinate their effort | S1024.txt | ab2697f867c0260df70521e91ace69561f538898d9574a0d77609f305bc930ee | 46359 | 1 |
| S1025 | C11 | https://journals.openedition.org/angles/pdf/7360 | A | Rowing songs survive in the Scottish Gaelic tradition in some numbers, but they are no longer in use | S1025.txt | 1cfdb4f3547964eddcd70c0ba1c9175e1bc23649e11435297d9111081b837a84 | 44769 | 1 |
| S1026 | C12 | https://archive.org/download/shipsseasongssha00whal/shipsseasongssha00whal_djvu.txt | A | one mariner sings out and the rest follow in the same tune | S1026.txt | 76deafbaf01310d0d511909401d367affcc916ff8d60096781fb15555a046dd5 | 135268 | 1 |
| S1027 | C17 | https://philippines.sil.org/resources/audio_and_video/mangali_and_tanudan_valley_music | B | Tug-om is sung by women while pounding rice or coffee. | S1027.txt | fdd95355e045037b38334d0d99a24646f0cc858730de262f123454d61a8d0d3c | 9095 | 1 |

## Re-verification notes

- Each admitted candidate was re-fetched by plain `curl -L --max-time 30 -sS` (default user agent) from this seat,
  one attempt each, all HTTP 200 (attempts recorded in manifest). Fresh sha256 of the quote capture equals the
  scout capture for 8 of 10 (C1, C2, C3, C4, C6, C7, C11, C12).
- C8 (Bourke UCD PDF): fresh fetch 842805 bytes vs scout 842807 bytes (2-byte difference; the source PDF changed
  between scout and this seat). The quote counts 1 in the shipped text derived from the fresh fetch.
- C17 (SIL page): the scout's html-to-txt ("fc27d3f0...") differs from this seat's stdlib HTML strip
  ("fdd95355..."); the quote counts 1 in the shipped text derived by this seat's strip. Both derivations are of the
  same 43071-byte page.
- TXT derivation (this seat, stdout of record): `%PDF` magic -> `pdftotext -layout`; HTML -> stdlib strip
  (script/style removed, block tags to newlines, tags stripped, unescape); plain text -> as fetched.
