# ExecRegistry97 — round-97 registry rows and evidence (2026-11-05)

Seat: ExecRegistry97 (coverage lane, wave 1). Sole writer this round of `corpus/SOURCES.md`
appends and `reports/round-97/evidence/`. Base 1ffc5a8; no frozen file touched; nothing committed.

## Dependency
Waited on `.ufo/waves/round-97/w1/stage/ScoutSources97/DONE` (bounded loop, 30 s interval;
appeared at iter ~20). Read `candidates.json`: 8 admitted (7 tier A, 1 tier B), 2 opened-but-
unadmitted, 7 rejects. `candidates.json` sha256 (scout's DONE): cc940051577528f69e6b61b069c4943197e9c146fdde1303f164dc1955a50953.

## Pre-assignment checks (commands + rc)
- Id-range collision: `grep -cE '^ {0,3}\|[[:space:]]*S98[5-9]' corpus/SOURCES.md` -> 0 (rc 1 = no match) before; 5 (rc 0) after.
- URL collision, full + host+path, `grep -c -F` per URL against SOURCES.md: 0/0 for all 8 (loop rc 0).
- Registry at check: `grep -c -E '^\| S[0-9]+' corpus/SOURCES.md` -> 908, highest S984.
- Baseline census before edits: validate rc 0 (29 W-warnings, `ok`), saved in scratch, not a deliverable.

## Re-verification (all fetches mine: plain curl, default UA, -L, --max-time 30; transient retry 3x/20 s)
| id | key | fetches (attempt, rc, http) | capture B | raw sha == scout | quote count |
|---|---|---|---|---|---|
| S985 | pagliai_2009 | (1,0,200) | 269331 | yes (pdf; txt == scout quote_text_sha256) | 1 |
| S986 | hoebel_1954 | (1,0,200) details; (1,28,302)+(2,0,200) djvu | 212777 / 844105 | djvu yes; details page dynamic (expected) | 1 |
| S987 | lokasenna_bellows | (1,0,200) | 307750 | yes | 1 |
| S988 | dunbar_kennedie_murphy | (1,0,200) | 390354 | yes (pdf; txt == scout) | 1 |
| S989 | ruszkiewicz_2020 | (1,0,200) | 130290 | yes (pdf; txt == scout) | 1 |
| S990 | garzia_2007 | (1,0,200) | 370994 | yes (pdf; txt == scout) | 1 |
| S991 | nadera_2019 | (1,0,200) | 229711 | yes (pdf; txt == scout) | 1 |
| S992 | nicholson_1907 | (1,0,200) | 1203657 | yes | 1 |

Quote recount method: `python3 bytes.count(quote.encode('utf-8')) == 1` on my own capture text
(pdftotext -layout extractions for PDFs, matching scout's extraction mode). One retry consumed
(S986 djvu, attempt 1 curl rc 28 on the 302 hop; attempt 2 200). All 8 PASS; nothing dropped
from the admitted set. Transcript: scratch `verify.json` (deleted with scratch; the durable
numbers live in this Report, rows.md and manifest.json).

## Rows written (append-only, end of Registry table, lines 942-950 of corpus/SOURCES.md)
S985 Pagliai 2009 (Oral Tradition 24/1), S986 Hoebel 1954, S987 Poetic Edda/Lokasenna (Bellows,
Wikisource), S988 Flyting of Dunbar and Kennedy (Murphy ed., tier B), S989 Ruszkiewicz 2020
(Prace Filologiczne 10(13)), S990 Garzia 2007 (Oral Tradition 22/2), S991 Nadera Jr &
Mooney-Singh 2019 (SARE 56/1), S992 Nicholson 1907 (Gutenberg #37985) — all `paper`/`book`/`docs`
per enum, tier A except S988, status mined, opened 2026-11-05, recheck 180d, used-by exactly
`corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md`. S993 Fishman 2008 (Oral
Tradition 23/2), tier A, mined, opened 2026-11-05, recheck 180d, used-by exactly
`corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`. No literal or escaped pipe in
any cell (checked programmatically; 11 cells per row).

## Frontier curation (round-96 routed defect 4)
Threnoi PDF re-opened myself: attempt1 rc 0 http 200, 302080 B, sha256 1e53dabf880576270d134fa285914b17c802d62ee84b159a72e535fc3fc5599a —
byte-identical to the ReviewerThrenoi96 decision capture. pdftotext rc 0, 83367 B; quotes
Q1/Q2/Q3 each count 1. Row S993 appended with Q1 as locator; id + quote written to
`stage/ExecRegistry97/threnoi.md` for ScribeEntry97 (consumed: one sentence at
funerary-lament-dirge-formulae.md line 70 citing S993).

## Evidence and manifest
`reports/round-97/evidence/`: S985.pdf/.txt, S986.html/.txt, S987.html, S988.pdf/.txt,
S989.pdf/.txt, S990.pdf/.txt, S991.pdf/.txt, S992.txt, S993.pdf/.txt (16 files), each sha256 in
`manifest.json` (9 entries: id, url, access, http, bytes, sha256, quote byte-exact incl.
newlines, quote_count, attempts, tier, status, used_by, captures[], raw_capture, and a
scout-artifact sha match flag — true for all 8 admitted; S986 matched on the djvu quote
artifact, its dynamic details page differs as expected).

## Append-only, census, counts
- `git show 1ffc5a8...:corpus/SOURCES.md` snapshot; diff vs landed file: added=9 removed=0
  (`diff | grep -c '^>'/^<'`; numstat 9 0). Saved: stage/append-only.txt (+ full diff
  append-only-diff.txt).
- Census: `sources-census.sh validate --file corpus/SOURCES.md` -> rc 0, `ok` (pre-existing
  W01/W04 warnings only; no E-codes). Saved: stage/census.txt.
- Rows after: `grep -c -E '^\| S[0-9]+'` -> 917; highest S993.
- ScribeEntry97 landed the entry (sha256 d021072f1e20e4db738df6e24f22eee64a28c0f8018c4a06d8c6a0682b7eb4a4)
  between my row append and my census run, per the coordination agreed over peer messages;
  its frozen-counter transcript shows C1-C8 PASS, rows=917, new=9, qualifying=8.

## Dropped (not written)
bevan_nakaid_edition (no count==1 span: title string 6x on details page, Arabic OCR without
clean English), labov_chapter (preview mirrored in metadata with counts 6/5; none of 11 probed
spans unique; self-bib 403), plus the scout's 7 wall/interstitial rejects. Detail:
stage/dropped.md.

## Tooling
None installed (pdftotext poppler already present; pacman untouched per host pause). No host
sysctls touched. No git/jj mutation. Scratch /fast/scratch/hyaku/kotodama-r97/ExecRegistry97/
deleted before yield.

## Bounds kept
Writes: corpus/SOURCES.md (9 appended lines only), reports/round-97/evidence/* (16 captures +
manifest.json), stage/ExecRegistry97/{rows.md, threnoi.md, dropped.md, census.txt,
append-only.txt, append-only-diff.txt, DONE}, .ufo/waves/round-97/w1/ExecRegistry97.md.
No frozen file, no sibling-lane file, no other seat's file touched.
