# ScribeS776Gate — Gate line for the S776 supersession (round 66, v2 wave)

Seat: `ScribeS776Gate`, scribe, axes calibration+coverage, milestone `r66-v2`.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated, base
`94209e8f80969dbac48d56c5d0e2e623635b8616`). Leaf seat: no subagent dispatch, no git/jj
writes, no counter or product edits. Tool installs: none (no pacman/uv/npm transaction ran).

## Behavior

Drafted `.ufo/waves/round-66/stage/s776-gate.md`: the round-66 `## Gate` line for S776 in the
round-65 Gate shape, one disposition line, the matching append-only `corpus/SOURCES.md` row, the
evidence table, and an integration checklist for the L1. The quote was copied from
`corpus/lessons/round-65.md:24` and byte-compared, never retyped:

```
- S776 | https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf (https://web.archive.org/web/20261024111013id_/https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf) | 2026-10-24 | "Versions of mancala are traditionally played across Africa and Asia, with gameplay and board dimensions varying considerably between different regions."
```

```
- S776 supersedes S753 — S753's committed capture 20250926172224 no longer serves a snapshot at
  its own timestamp (replay answers 302 to 20261024111013), so S776 re-cites the same live URL
  with the fresh capture 20261024111013, byte-identical to the live PDF today; quote and teaches
  are unchanged, and the games entry's mancala bullet re-points (S753) -> (S776).
```

## Gates (all run by this seat; commands and outcomes verbatim)

| gate | command | outcome |
|---|---|---|
| quote identity | `python3` compare of lesson S753 quote vs drafted S776 quote | `quote_identical= True words= 20` |
| quote cap | `python3 -B tools/check-gate-quotes.py /tmp/lesson-gate-check.md` (Gate line wrapped in a lesson stub) | `GATE_QUOTES: 0 findings`, exit 0 |
| row shape | row fed to `tools/reopen-row.py` `cell_urls`/`cell_quote` | urls = `[live pdf, https://web.archive.org/web/20261024111013id_/...]`; quote = `Versions of mancala are traditionally played across Africa a…`; 11 real cells; `teaches` opens `supersedes S753` |
| live anchor | `curl … https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf` | `200 application/pdf` 529795 bytes, sha256 `cb6ff9b8ef73c176782b12c7b4cada9be63de54feac248069eb009f17e538632` |
| quote in live PDF | `pdftotext -layout` | quote verbatim (2-column layout wraps after "Africa"; sentence continues "and Asia, …") |
| fresh capture | `curl 'http://web.archive.org/web/20261024111013id_/…/sowing-seeds.pdf'` ×2 | `200 application/pdf` 529795 bytes, byte-identical sha256 to live; quote present in its text |
| old capture | `curl -L 'http://web.archive.org/web/20250926172224id_/…/sowing-seeds.pdf'` | `302`, 1 redirect to `…/20261024111013id_/…`, final `200 application/pdf`, bytes identical to live |
| authoritative locator | `python3 -B reports/round-61/reopen-quote.py --row S753` | `LOCATED https://www.penn.museum/…/sowing-seeds.pdf`, exit 0 |
| frozen Ca counter | `python3 -B reports/round-66/accept-ca.py --root .` (twice, 08:33 and 08:36) | run 1: `D1 FAIL bad=['quote', 's776', 's776_citations=0', 's753_citations=1']`; run 2 (after the receipt gained the quote): `D1 FAIL bad=['s776_citations=0', 's753_citations=1']`; both `ACCEPT-CA-66: FAIL` with D2 `…absent`, D3 `named=65 existing=0 min=8`, D4 incomplete, CRITERION FAIL, `QUOTES FAIL exit=2 gate_ids=0` |

## Touched surfaces

- Wrote `.ufo/waves/round-66/stage/s776-gate.md` (draft only).
- Wrote `.ufo/waves/round-66/w1/ScribeS776Gate.md` (this report).
- Scratch downloads under `/tmp` (`s753-live.pdf`, `s753-cap.pdf`, `cap2.pdf`, `old-http.bin`,
  `lesson-gate-check.md`) and a module import of `tools/reopen-row.py` (read-only, no writes).
- Read-only: `corpus/lessons/round-65.md`, `corpus/SOURCES.md`, `corpus/QUALITY.md` path refs,
  `corpus/knowledge/culture-material/games-play-sport-contests.md`,
  `reports/round-66/{claims.json,accept-ca.py,telemetry/*}`, `tools/{reopen-row,check-gate-quotes}.py`,
  `reports/round-61/reopen-quote.py`.
- Not touched: `corpus/SOURCES.md`, `corpus/lessons/round-66.md`, the games entry,
  `reports/round-66/telemetry/*` (peer-owned and changing), lane index, jj/git state.

## Findings

**F1 (calibration, blocking for Ca D1).** The frozen D1 leg cannot pass on the state I measured;
the blocker is now the citation re-point alone. `corpus/knowledge/culture-material/games-play-sport-contests.md:23`
still cites `(S753)` once and `(S776)` zero times. The receipt side moved while I watched:
`reports/round-66/telemetry/s753-recapture.txt` had no quote text at 08:33:39
(`grep -c 'Versions of mancala'` = 0; counter then printed
`D1 FAIL bad=['quote', 's776', 's776_citations=0', 's753_citations=1']`), and was updated at
08:35:10 to carry the quote (1 occurrence), after which the same unchanged counter printed
`D1 FAIL bad=['s776_citations=0', 's753_citations=1']`. Both receipts are honest observations of a
peer-owned file in flux; only the games-entry re-point remains, and it is an L1 integration task.

**F1b (process).** The file `reports/round-66/telemetry/s753-recapture.txt` changed body between
two reads seconds apart (8-line body with `old_capture status=000` first, then a 40+ line body with
the CDX row and a fresh-capture replay `200 size=529795`). Any receipt-based leg that reads it once and
asserts a datum should name its own mtime; the D1 leg does not.

**F2 (calibration, conflict to report verbatim).** The `20250926172224` capture no longer
replays 404 here. My probe gets `302` → `20261024111013id_/…` → `200 application/pdf` with bytes
identical to the live PDF, and the peer-written receipt's later revision records
`old_replay_status=200 size=529795`. The seat briefs say "the committed capture 20250926172224
still replays 404 today" (`RevD1Anchor` prompt) — that observation does not reproduce from this
host. The honest defect is narrower: the old capture no longer serves **its own snapshot**
(302 to the newest capture), so it is a redirect stub rather than a pinned snapshot. The live URL
is not dead: `reopen-quote.py --row S753` prints `LOCATED` today. My disposition line is written
to that narrower, measured claim, not to "unresolvable".

**F3 (instrument, R65-M3 class still open in the registry).** 23 registry rows still carry
scheme-less captures: S751 S752 S753 S754 S755 S756 S757 S758 S759 S760 S761 S762 S763 S764 S766
S767 S768 S769 S770 S771 S772 S773 S774 (S750 and S775 were fixed by R65-M3; S765 carries the
scheme). `tools/reopen-row.py` extracts with `URL_RE = r"https?://[^\s]+"`, and a bare
`web.archive.org/web/<ts>id_/https://<orig>` cell contains the original `https://` URL, so
`cell_urls` returns the live URL **twice** and never requests Wayback — measured for
S751/S752/S753: `['…sowing-seeds.pdf', '…sowing-seeds.pdf']`. Any durability audit run through
that tool is blind to those captures while looking well-formed (2 attempted URLs).

**F4 (instrument, PDF rows cannot pass `tools/reopen-row.py`).** That tool has no PDF text path
(`grep -i 'pdf|pdftotext|flate'` finds only HTTP gzip handling), so a Flate-compressed PDF is
scanned as raw bytes. Measured: `ROW S753 ABSENT attempts=2 url=-` from `reopen-row.py`, against
`LOCATED` from `reports/round-61/reopen-quote.py --row S753` (pypdf 5.4.0). Since S776's anchor
is the same PDF, a durability leg routed through `reopen-row.py` fails for instrument reasons,
not source reasons; use `reopen-quote.py --row`.

**F5 (limit, local egress).** `https://web.archive.org/web/<ts>id_/…` failed at TCP connect on
4 of 5 attempts (`curl` exit 7, ~180 ms); `https://web.archive.org/` root answered 200; one
`--resolve 207.241.237.3` attempt answered 200; the `http://` scheme answered 200 every time.
Recorded as a host artifact, not as evidence about the capture. The drafted cell keeps the
`https://` scheme (house convention, and the only form the extractors see as a URL).

**F6 (dependency).** The proposed S776 registry row is a draft, not a landed row: `grep '^| S776'`
on `corpus/SOURCES.md` returns `S776 ABSENT`, and `reopen-row.py S776` returns `ROW S776 NO_ROW`.
`reports/round-66/telemetry/s753-recapture.txt` was being rewritten by another seat during this
run (two different bodies minutes apart, mtime 08:33:39); I did not edit it and did not treat
either revision as final.

## Out of scope (deliberately not done)

- No append to `corpus/SOURCES.md`, no `corpus/lessons/round-66.md` write, no games-entry re-point.
- No telemetry edit; no counter repair; no claim/predicate change.
- No review of the other 23 new rows (S777–S800) or of the claim O instrument.

## Artifacts

- `.ufo/waves/round-66/stage/s776-gate.md` — Gate line, disposition, proposed registry row,
  evidence table, integration checklist.
- `.ufo/waves/round-66/w1/ScribeS776Gate.md` — this report.
