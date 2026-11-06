# ScoutSources100 — work song and labour chant: source scout

Round 100, wave 1. Access date 2026-11-06. Read-only research; wrote only under
`.ufo/waves/round-100/w1/stage/ScoutSources100/` and scratch. No S-ids assigned.

Outputs: `stage/ScoutSources100/candidates.json`, `candidates.md`, `captures/` (15 files),
`DONE`. Detail lives in `candidates.md`; this file carries the log and the numbers.

## Admitted: 10 candidates, 8 tier A + 2 tier B (target was ≥6)

| key | source | tier | http | bytes | quote |
|---|---|---|---|---|---|
| C1 | Terry, *The Shanty Book I* (1921), PG #20774 | A | 200 | 109627 | "The song was rendered by one singer, called the shantyman, and the chorus by the sailors" |
| C2 | Sharp, *English Folk-Chanteys* (1914), IA | A | 200 | 113227 | "by assuring unanimity of action, to aid them in the efficient execution of their collective task" |
| C3 | *Slave Songs of the United States* (1867), IA | A | 200 | 225579 | "two measures are to be sung to each stroke, the first measure being accented by the beginning of the stroke" |
| C4 | Bücher, *Arbeit und Rhythmus* (1896), IA | A | 200 | 661502 | "es ist kein Zweifel, dass das Festhalten eines gleichen Zeitmasses der Bewegung dadurch erleichtert wird" |
| C6 | Collinson, Oyster Dredging Songs of the Firth of Forth, *Scottish Studies* 5 (1961) | A | 200 | 589572 | "They were said to be chanted by a song-leader among the boat's crew, who repeated his lines in chorus" |
| C7 | Blankenhorn, Classification of Gaelic Song, *Oral Tradition* 32/1 (2018) | A | 200 | 4927689 | "Waulking-songs are work songs performed to facilitate the fulling of handwoven woolen cloth" |
| C8 | Bourke, *Working and Weeping* (UCD 1988) | B | 200 | 842807 | "a work song helps the people who sing it to establish the rhythm of their work and to coordinate their effort" |
| C11 | Purser, Hebridean Rowing Songs, *Angles* 17 (2024) | A | 200 | 868447 | "Rowing songs survive in the Scottish Gaelic tradition in some numbers, but they are no longer in use" |
| C12 | Whall, *Ships, Sea Songs and Shanties* (1913), IA | A | 200 | 135268 | "one mariner sings out and the rest follow in the same tune" |
| C17 | SIL Philippines, Mangali and Tanudan Valley Music | B | 200 | 43071 | "Tug-om is sung by women while pounding rice or coffee." |

Coverage: leader/response (C1, C2, C6, C8, C12); rhythm-to-task (C2, C3, C4, C8);
occupational repertories — shanty, oyster dredging, waulking, iorram, Kalinga pounding
(C1, C2, C6, C7, C11, C12, C17); improvised verses (C1, C6); complaint/satire (C1);
learned/owned/retired (C6, C11, C7).

## Search log — 17 queries (all `web_search`, 2026-11-06)

1 Whall Sea Songs and Shanties Gutenberg → no PG edition; IA + PG #20774 (C1, C12).
2 Cecil Sharp English Folk-Chanteys archive.org → C2.
3 Slave Songs of the United States 1867 rowing songs → C3.
4 Bücher Arbeit und Rhythmus archive.org → C4.
5 1911 Britannica Chanty Wikisource → page absent (404 ×3).
6 waulking songs Hebrides open access → C8 (+ Cheape, Brewer leads).
7 Oral Tradition work songs call and response → C7 (+ Pigott 28/1, dreg-song 28/2).
8 African American work song chain gang open access → LoC 403, Gioia restricted.
9 rice pounding songs open access → C17 (+ Atlantic 1958 paywalled, ARCE 403).
10 shanty hauling halyard rhythm → Camus *Miranda* (French, not opened).
11 Gioia *Work Songs* open access → unauthorized mirror only; rejected.
12 Folk Music Journal work song → Pickering et al. JSTOR-only.
13 Blankenhorn Gaelic song pdf → mospace 404, journal PDF (C7).
14 dreg songs Firth of Forth → C6.
15 call and response Africa labour → Locke metadata only, Gunderson 403.
16 Gunderson Sukuma musical labor → Brill front matter, Smithsonian 403.
17 Work Songs Old Kingdom tombs → Roos *JEOL* 47, host 503 ×4.

## Rejects / unreachable (reason → flip)

- C5 EB1911 "Chanty" on Wikisource — 404 under three URL forms; API title search empty. Flip: scan-backed EB1911 volume carrying the entry.
- C9 LoC "Traditional Work Songs" — 403. Flip: LoC JSON API or open mirror.
- C10 Britannica "work song" — 403. Flip: an open reference work.
- C13 Roos, *JEOL* 47 (Egyptian tomb work songs) — 503 ×4. Flip: retry when host recovers; would be tier A.
- C14 Gunderson, Smithsonian Folkways — 403. Flip: open copy.
- C15 Merzeban, JAAUTH — connection error ×4. Flip: reachable network.
- C16 ARCE work songs (Naga pounding) — 403. Flip: open ARCE page.
- Gioia *Work Songs* (Duke 2006) — unauthorized mirror only; not opened. Flip: publisher OA edition.
- Pickering/Robertson/Korczynski, *Folk Music Journal* 9/2 (2007) — JSTOR-only. Flip: EFDSS open deposit.
- Camus, *Miranda* 45765 — open but French and duplicative. Flip: if a French quote is wanted.
- mospace bitstream — 404, superseded by the journal PDF.

Transient failures: up to four attempts, 20 s backoff, every attempt in `candidates.json`
under `attempts`. No wall was passed (no browser, no `-k`, no login).

## Commands and rc

- Registry duplicate check, `grep -c -F` on each of the ten URLs against `corpus/SOURCES.md`
  → `0` for all ten, **rc=0** (command transcribed in `candidates.md` §4).
- `sha256sum *` in `captures/` → 15 files, **rc=0**; hashes in `candidates.json`.
- Quote check: `re.sub(r"\s+"," ",capture).count(quote)` over `candidates.json` → count `1`
  and words ≤25 for all ten (10–21 words), **rc=0**; `admitted 10 of 10 bad 0`.
- Fetch: plain `requests`, default-ish UA, `allow_redirects=True`, `timeout=30`; statuses and
  byte counts per candidate recorded in `candidates.json`.

## Gaps

Complaint/satire rests on C1 alone; pounding on C17 (one sentence) plus C4's craft examples;
learning/ownership thin (C6 last bearers, C11 retirement). C13/C16 would close the pounding
gap if either host reopens.

Tooling installed: none.
