# Seat ScoutS892 — staged row S892 (Novikov 2022, RUDN) scout report

Seat: ScoutS892 (leaf, no delegation). Item: re-open staged row S892; tentative lane id S878.
Verdict: **ADMIT**.

---

## 1. Assignment and source

Staged row S892 (SOURCES.append.md row 40):
Novikov, P.N. (2022), «Искусственные языки как семантические и семиотические системы» / "Constructed Languages as Semantic and Semiotic Systems", *Вестник РУДН. Серия: Теория языка. Семиотика. Семантика* 13(2): 455–467, DOI 10.22363/2313-2299-2022-13-2-455-467 — https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955 (tier B, mined, opened 2026-10-23, recheck 180d, used-by conlang-scholarship.amend-2026-10-23.md).

Amendment claims citing S892 (conlang-scholarship.amend-2026-10-23.md, second amendment §N): "from S892: classification of constructed languages by lexical, syntactic and morphological features, connected to the purposes their creation serves, with the Eurocentrism problem named." Verified against the fetched PDF, abstract p. 455 and body pp. 457–459.

---

## 2. Fetch commands and raw outputs

UA used for live fetch (browser-shaped; recorded per QUALITY 21/22):
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

Command 1 (headers + probe, first 3000 bytes shown):
```
curl -sS -o - -D - -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -w "\nHTTP_STATUS:%{http_code}\nBYTES:%{size_download}\nFINAL_URL:%{url_effective}\n" "https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955" | head -c 3000
```
Raw output (excerpt):
```
HTTP/2 200
server: ddos-guard
content-type: application/pdf
content-length: 959171
content-disposition: inline; filename="31528-41702-1-PB.pdf"
HTTP_STATUS:200
...
%PDF-1.6
```

Command 2 (saved download):
```
cd /tmp/ScoutS892 && curl -sS -o S892-novikov-2022.pdf -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -w "HTTP_STATUS:%{http_code}\nBYTES:%{size_download}\n" "https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955"
```
Raw output:
```
HTTP_STATUS:200
BYTES:959171
-rw-r--r-- 1 vgpnk vgpnk 959171 Oct 25 19:06 S892-novikov-2022.pdf
S892-novikov-2022.pdf: PDF document, version 1.6 (zip deflate encoded)
```

Command 3 (text extraction + header):
```
cd /tmp/ScoutS892 && pdftotext -enc UTF-8 S892-novikov-2022.pdf S892-text.txt
pdfinfo S892-novikov-2022.pdf | grep -E 'Pages|Title|Author|CreationDate'
```
Raw output:
```
Pages:           13
CreationDate:    Wed Jul 13 19:33:03 2022 -03
```

---

## 3. Header verification (PDF vs claim)

| Field | Claimed | Verified in PDF (first page text) | Match |
|---|---|---|---|
| Title (EN) | "Constructed Languages as Semantic and Semiotic Systems" | `Constructed Languages as Semantic / and Semiotic Systems` | ✓ |
| Title (RU) | «Искусственные языки как семантические и семиотические системы» | `Искусственные языки как cемантические / и семиотические системы` | ✓ |
| Author | Novikov, Philipp N. / Ф.Н. Новиков | `Philipp N. Novikov` (p. 1); `Ф.Н. Новиков` (RU block) | ✓ |
| Journal | Вестник РУДН. Серия: Теория языка. Семиотика. Семантика / RUDN Journal of Language Studies, Semiotics and Semantics | `RUDN Journal of Language Studies, Semiotics and Semantics` + `Вестник Российского университета дружбы народов. Серия: ТЕОРИЯ ЯЗЫКА. СЕМИОТИКА. СЕМАНТИКА` | ✓ |
| Vol/issue | 13(2), 2022 | `2022 Vol. 13 No. 2 455–467` | ✓ |
| Pages | 455–467 | running heads 455…466 in extraction + 13 PDF pages; header range 455–467 | ✓ |
| DOI | 10.22363/2313-2299-2022-13-2-455-467 | `DOI: 10.22363/2313-2299-2022-13-2-455-467`; Citation block: `13(2), 455—467` | ✓ |
| ISSN | 2313-2299 (print), 2411-1236 (online) | first page: `2313-2299 (print), ISSN 2411-1236 (online)` | ✓ |

DOI resolution check (redirect target):
```
curl -sS -L -o /dev/null -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -w "HTTP_STATUS:%{http_code} FINAL:%{url_effective}\n" "https://doi.org/10.22363/2313-2299-2022-13-2-455-467"
# HTTP_STATUS:200 FINAL:https://journals.rudn.ru/semiotics-semantics/article/view/31528
```

---

## 4. Located quote (≤25 words, verbatim)

> "the author examines the existing classifications of constructed languages and attempts to establish a connection between purposes of their creation and their linguistic features"

- Location: Abstract, p. 455 (article PDF, first page; extraction lines 24–26).
- Word count (wc -w): **24** ≤ 25. Verbatim checked by `tr '\n' ' ' | grep -oE '…'` matched, 24 words.
- This single sentence carries both claims the amendment makes: existing classifications (lexical/syntactic/morphological feature analysis) and the purpose-to-structure link.

Supporting passage in the body (classification section, ch. 1, pp. 457–459): section heading `Correlation between types of constructed languages, purposes of their creation and linguistic features` (p. 457); a priori / a posteriori dichotomy, Halley's interlangs vs artlangs, zonal languages, controlled natural languages, artlangs (Klingon, aUI, Láadan, Ygyde, etc.). Eurocentrism named in abstract ("attention is also drawn to the problem of eurocentrism in constructed languages") and argued throughout (SAE features conclusion).

Recheck grep (the row's own recheck pattern, run by me):
```
pdftotext -enc UTF-8 S892-novikov-2022.pdf - | grep -c 'by analyzing various types of languages based on their lexical'
# output: 1
```

---

## 5. Amendment claim verification (conlang-scholarship.amend-2026-10-23.md)

| Amendment claim | Verified in PDF | Status |
|---|---|---|
| "classification of constructed languages by lexical, syntactic and morphological features" | Abstract: "examining various types of languages based on their lexical, syntactic, morphological and other features" | ✓ |
| "connected to the purposes their creation serves" | Abstract: "attempts to establish a connection between purposes of their creation and their linguistic features on various levels"; ch. 1 section title | ✓ |
| "with the Eurocentrism problem named" | Abstract: "attention is also drawn to the problem of eurocentrism in constructed languages"; conclusion: Standard Average European features | ✓ |
| "Abstract, p. 455" fetch record | Quote above at p. 455; PDF served 2026-10-25, HTTP 200 | ✓ |

No misquote found. The amendment's §N summary is faithful.

---

## 6. Wayback CDX canonical-slug probe

Probed URLs (both `?output=json&limit=20&filter=statuscode:200`):

1. Canonical article slug: `http://web.archive.org/cdx/search/cdx?url=journals.rudn.ru/semiotics-semantics/article/view/31528&output=json&limit=20&filter=statuscode:200`
   - Result: 14 snapshots, all text/html 200, earliest 20220729220713 (2022-07-29), latest 20260629043113 (2026-06-29). Canonical slug is archived and live.
2. PDF (viewFile) slug: `http://web.archive.org/cdx/search/cdx?url=journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955&output=json&limit=20&filter=statuscode:200`
   - Result: 1 snapshot, application/pdf, statuscode 200, timestamp 20240415141632, length 861874 (archive copy is a byte-different rendering of the same URL; live copy is 959171 bytes).

Both CDX calls returned HTTP 200. No 'no capture' ruling needed.

---

## 7. Proposed lane registry row (11-column schema, tentative id S878)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S878 | Новиков, Филипп Н. (2022), «Искусственные языки как семантические и семиотические системы» / "Constructed Languages as Semantic and Semiotic Systems", *Вестник Российского университета дружбы народов. Серия: Теория языка. Семиотика. Семантика* 13(2): 455–467, DOI 10.22363/2313-2299-2022-13-2-455-467 — https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955 | paper | B | Tier B for a peer-reviewed Russian-language treatment of constructed languages as semantic and semiotic systems: the existing classifications of constructed languages, and the attempt to connect a language's purposes of creation with its features on the lexical, syntactic and morphological levels. One research article, the author's own framework | Abstract, p. 455 (article PDF, 13 pages) — DOI 10.22363/2313-2299-2022-13-2-455-467 as served 2026-10-25 | Gives the lane a scholarly statement that a conlang is a sign system whose parts can be analysed as such, with the Eurocentrism problem in the field named — the counterweight to the craft manuals that treat a conlang as a set of pleasing forms | mined | 2026-10-25 | 180d — `curl -fsSL 'https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955' -o /tmp/r.pdf && pdftotext -enc UTF-8 /tmp/r.pdf /tmp/r.txt && grep -c 'by analyzing various types of languages based on their lexical' /tmp/r.txt` -> 1 (ran 2026-10-25) | corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md |

Notes:
- No pipe character inside any cell; recheck uses the no-pipe variant (grep against a text file), avoids the escaped-pipe `\|` of the draft row.
- status mined; opened 2026-10-25 (this verification date); recheck 180d with command (ISO-date/NNd/on-release form).
- used-by: exactly the admitted entry that cites S892 — conlang-scholarship.amend-2026-10-23.md (the base conlang-scholarship.md cites S881/S882, not S892).
- The recheck output `1` was reproduced by me on 2026-10-25 (PD §4).

---

## 8. Tier assignment

**Tier B**, matching the staged row and the amendment's own tier note.

Reason: the tier definition in corpus/SOURCES.md sums "B — strong secondary (expert write-up with reproducible detail, survey, textbook)". This is one peer-reviewed research article presenting the author's own framework — a strong secondary source for the conlang-scholarship entry, not a primary/official spec of the lane (tier A is reserved for specs, official docs, source code, maintainer statements, the lane's own re-runnable gate output). The article is read in the original language (Russian) and the full PDF is open access, which supports B. It is not C (it is real, reachable, and peer-reviewed). Flip condition: if the fleet's tier rubric were interpreted so that "original paper" (the A-list mention) covers this article, it could be argued A; the amendment and draft row both assign B, and B is the conservative, evidence-matched choice given the entry cites the abstract plus the ch. 1 classification passage.

---

## 9. Verdict

**ADMIT.**

Reason: live fetch HTTP 200, application/pdf, 959171 bytes, saved as /tmp/ScoutS892/S892-novikov-2022.pdf; header verified in full (title EN/RU, author, journal, 13(2) 2022, pages 455–467, DOI, ISSN); the located 24-word quote is verbatim on p. 455; the amendment's claims (classification by lexical/syntactic/morphological features, purpose-to-structure connection, Eurocentrism problem named) are all confirmed in the fetched text; recheck grep returns 1; Wayback CDX confirms the canonical slug is archived (14 captures) and the PDF slug archived (1 capture) — no reachability concern.

Flip condition: REFUSE/UNVERIFIABLE if (a) a later check shows the fetched PDF is not the final published version (e.g., header or pagination mismatch with the journal's issue) — currently no evidence of that; or (b) the amendment prose expands beyond what p. 455 and ch. 1 actually say (e.g., if "classification by lexical, syntactic and morphological features" is misread as a taxonomy table the paper itself proposes, whereas the paper surveys existing classifications) — the proposed body text above stays within the verified statements.

---

## 10. Hygiene records

- Tool installs: none (curl, pdftotext, pdfinfo, grep all preinstalled system tools; no pacman, no installs).
- Downloads: /tmp/ScoutS892/S892-novikov-2022.pdf (959171 bytes), /tmp/ScoutS892/S892-text.txt, /tmp/ScoutS892/r.pdf (/tmp/r.txt) — recheck scratch.
- UA recorded in §2. No challenge walls encountered (ddos-guard header present but content served).
- Nothing written to the fleet repo, lane repo, shokuknow source tree, or registry; only this report file under .ufo/waves/round-73/w1/.
