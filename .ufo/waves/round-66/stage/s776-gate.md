# S776 Gate line + disposition (draft for L1 integration)

Seat: ScribeS776Gate (independent leaf, no subagent dispatch). Prepared 2026-10-24.
Nothing here is landed; the L1 is the only committer. Gate shape is copied from
`corpus/lessons/round-65.md:24` (the S753 line). The quote is copied verbatim from that
line, not retyped from memory.

## Gate line (one line; paste verbatim into `corpus/lessons/round-66.md` `## Gate`)

- S776 | https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf (https://web.archive.org/web/20261024111013id_/https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf) | 2026-10-24 | "Versions of mancala are traditionally played across Africa and Asia, with gameplay and board dimensions varying considerably between different regions."

Line facts (checked, not assumed):

- Quote provenance: `corpus/lessons/round-65.md:24` (S753 Gate line). Byte-checked with
  `grep -o '"[^"]*"' <(grep '^- S753 ' corpus/lessons/round-65.md) | od -c`: plain ASCII,
  no curly quotes, no ellipsis. 20 words — inside `tools/check-gate-quotes.py`'s
  `MAX_WORDS = 25` cap, so the QUOTES leg can pass on this line.
- Capture scheme: written as `https://web.archive.org/...`, not the bare
  `web.archive.org/...` form that the round-65 S753 line still carries. `tools/reopen-row.py`
  extracts URLs with `URL_RE = re.compile(r"https?://[^\s]+")`, so a bare capture is invisible
  to it and — because the bare archive path *contains* the original `https://` URL — the
  extractor silently returns the live URL twice (measured: S751/S752/S753 all yield
  `[live, live]`). This is the R65-M3 class; S776 must not repeat it.
- Row/quote pairing: the first double-quoted span of the proposed registry anchor cell (below)
  is exactly this quote, so `reports/round-61/reopen-quote.py --row S776` reads the same string.

## Disposition (one line, for the lesson Gate preamble / the R66-Mn block)

S776 supersedes S753 — S753's committed capture 20250926172224 no longer serves a snapshot at
its own timestamp (replay answers 302 to 20261024111013), so S776 re-cites the same live URL
with the fresh capture 20261024111013, byte-identical to the live PDF today; quote and teaches
are unchanged, and the games entry's mancala bullet re-points (S753) -> (S776).

## Proposed registry row (append at the end of the `## Registry` table, before `## Paths`)

| S776 | Kristen Pearson, “Sowing the Seeds of Competitive Play: The Enduring Legacy of Mancala,” Expedition 58(1) (Spring 2016) — https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf ; https://web.archive.org/web/20261024111013id_/https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf . | paper | B | mancala family distribution and sowing gameplay (durability re-open of S753) | "Versions of mancala are traditionally played across Africa and Asia, with gameplay and board dimensions varying considerably between different regions." — located in the live PDF and in capture 20261024111013, whose bytes equal the live bytes (sha256 cb6ff9b8ef73c176782b12c7b4cada9be63de54feac248069eb009f17e538632) | supersedes S753 — the row, quote and teaches stand; the committed 20250926172224 capture now answers 302 to 20261024111013, so this row carries the snapshot that still serves at its own timestamp | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/games-play-sport-contests.md |

Shape conformance: 11 cells matching the header
`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`;
`teaches` opens `supersedes S753 —` per `corpus/SOURCES.md:12`; `used-by` is the round-65 games
entry (not the new scent entry), matching the reviewed S753 row's used-by.

## Evidence (all measured by this seat on 2026-10-24, ~08:30–08:40 local)

| probe | command (abridged) | outcome |
|---|---|---|
| live URL | `curl -sS -o s753-live.pdf -w '%{http_code} %{content_type} %{size_download}' https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf` | 200 application/pdf 529795 bytes; sha256 `cb6ff9b8ef73c176782b12c7b4cada9be63de54feac248069eb009f17e538632` |
| quote in live PDF | `pdftotext -layout s753-live.pdf` then read the WHAT IS MANCALA? paragraph | quote present verbatim; the 2-column layout breaks the line after "Africa", "and Asia, with gameplay and board dimensions varying" continues the same sentence |
| fresh capture 20261024111013 | `curl 'http://web.archive.org/web/20261024111013id_/https://www.penn.museum/.../sowing-seeds.pdf'` (twice) | 200 application/pdf 529795 bytes, sha256 identical to live (byte-identical); quote present in its `pdftotext` text |
| old capture 20250926172224 | `curl -L 'http://web.archive.org/web/20250926172224id_/https://www.penn.museum/.../sowing-seeds.pdf'` | 302 with 1 redirect to `.../20261024111013id_/...`, final 200 application/pdf, bytes identical to live — the old timestamp no longer serves its own snapshot |
| archived metadata | `reports/round-66/telemetry/s753-recapture.txt` (peer-written, mtime 08:33:39) | CDX row `20261024111013` status 200 application/pdf digest `F5PON6QPZ4DXOBF5DE2MQCTJPNVBUZVC` length 386911; replay 200 size 529795 |
| authoritative locator | `python3 -B reports/round-61/reopen-quote.py --row S753` | `LOCATED https://www.penn.museum/.../sowing-seeds.pdf` (exit 0) — S753's live anchor still resolves today; only the committed *capture* moved |

Local-network limit (recorded, not hidden): `https://web.archive.org/web/<ts>id_/...` failed at
TCP connect on 4 of 5 attempts from this host (`curl` exit 7, 185 ms), while
`https://web.archive.org/` root answered 200 and one `--resolve 207.241.237.3` attempt answered
200; the `http://` scheme replay answered 200 every time. Treat the scheme in the cell as
correct-by-convention (113 registry rows already carry it) and the https flakiness as a host
egress artifact of this seat, not as evidence about the capture.

## Integration checklist for the L1 (not done here)

1. Append the registry row above to `corpus/SOURCES.md` inside the `## Registry` table
   (R65-M2: before `## Paths`, never after `## Leads`).
2. Paste the Gate line into `corpus/lessons/round-66.md` `## Gate`; keep the `S776` id — the
   frozen QUOTES leg regex expects `S776`-class ids and the Ca D1 leg wants `S776` present.
3. Re-point `corpus/knowledge/culture-material/games-play-sport-contests.md:23`
   `(S753)` -> `(S776)`; the frozen D1 leg requires exactly one `(S776)` and zero `(S753)` in
   that file (`grep -n` at draft time: line 23 still cites `S753`).
4. `reports/round-66/telemetry/s753-recapture.txt` must carry the quote token itself —
   `Versions of mancala are traditionally played across Africa and Asia`. That gap closed while
   this seat watched: at the first read the file (mtime 08:33:39 body) had `20261024111013` and
   `S776` but no quote text, and the unchanged counter printed
   `D1 FAIL bad=['quote', 's776', 's776_citations=0', 's753_citations=1']`; the file was updated
   at 08:35:10 with the quote (1 occurrence) and the same counter then printed
   `D1 FAIL bad=['s776_citations=0', 's753_citations=1']` — i.e. only the citation re-point in
   item 3 remains. The receipt is peer-owned; this seat did not edit it.
