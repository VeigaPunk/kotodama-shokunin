# ScoutSources96 — round 96, claim C: sources for the oath, blessing and curse formulae entry

Seat: `ScoutSources96` (scout, coverage axis). Lane: `kotodama-shokunin`. Wave `round-96/w1`. Date 2026-11-05.

## What this seat did

Read-only source reconnaissance for the new knowledge entry
`corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` (Claim C, frozen in
`reports/round-96/claims.json`, freeze commit `deca7e6fff988061f01bfc501a91e18fca892822`).
I did **not** edit `claims.json`, `predispatch.py`, `predispatch-base.txt`, anything under
`reports/round-95/`, the corpus registry, the entry file, or any file another seat owns.
No S-id was assigned — the registry seat assigns ids sequentially from S975.

Outputs, all under
`.ufo/waves/round-96/w1/stage/ScoutSources96/`:

- `candidates.json` — 11 admitted candidates, one object per candidate with the required
  fields (`key, url, access, http, bytes, capture, sha256, tier, quote, quote_count,
  admitted, reason`) plus `kind, venue, supports, raw_capture, raw_bytes, raw_sha256,
  raw_quote_count, wayback_timestamp, wayback_capture, quote_count_command`.
- `candidates.md` — search log (11 queries, result counts, URLs kept), the registry
  duplicate check, the candidate table with HTTP status and quote counts, per-row
  admissibility reasons, the reject/UNREACHABLE table with flip conditions, the Wayback
  note, and the handover ordering.
- `captures/` — 11 text renderings `C1.txt` … `C11.txt` (the quotable artefact), the 11 raw
  fetches `C<n>.raw.<ext>`, and `captures/rejected/` holding 28 rejected or unreachable raw
  responses.
- `DONE` — written last, one line, the sha256 of `candidates.json`.

## Numbers, with commands and rc

| measure | command | rc | result |
|---|---|---|---|
| admitted candidates | `python3 -c "import json;c=json.load(open('candidates.json'));print(len(c),sum(1 for x in c if x['admitted']),sum(1 for x in c if x['tier'] in ('A','B')))"` | 0 | `11 11 11` |
| quote counts (all must be 1) | `python3 -c "print(open('captures/C<n>.txt','rb').read().count(<quote>.encode()))"` for each n=1..11 | 0 | `1` for all eleven |
| tier A/B admitted | same as above | 0 | **11** (target was ≥3) |
| registry duplicate check | `grep -c -F -- "<url>" corpus/SOURCES.md` for each of the 11 admitted URLs | 0 | `0` for all eleven |
| one family-level match | `grep -c -F -- "wisdomlib.org/hinduism/book/manusmriti" corpus/SOURCES.md` | 0 | `1` (row S838 → R27 reject) |
| registry size | `grep -c '^| S[0-9]' corpus/SOURCES.md` | 0 | `898` rows, highest `S974` (unchanged by this seat) |
| sha256 of candidates.json | `sha256sum candidates.json` | 0 | `8a11bb98661013b5336fcb6a34574e2ed622dc5905eedaae3d66b9055a5338a3` |
| rejects recorded | `ls captures/rejected \| wc -l` | 0 | `28` raw responses |

Distinct traditions covered by the admitted rows: ancient Near East and Greek (C1, C3),
West African (C9), Old Norse (C2), Deuteronomic/treaty (C11), Japanese (C10, C8), Irish (C6, C4),
Celtic comparative (C5), and the performative-speech frame (C7). All six frozen phrases of
Claim C have at least one supporting row: *oath formula* (C1, C2, C3), *blessing formula*
(C8, C10), *curse formula* (C4, C5, C6), *self-imprecation* (C1, C9), *witness invocation*
(C2, C3, C9, C11), *sanction clause* (C11).

## Openings by plain curl

Every fetch used `curl -sS -L --max-time 30` with the default user agent. No browser, no
login, no CAPTCHA or bot-challenge passing, no paywall circumvention, no `curl -k`. Transient
results were retried up to three times with 20 s backoff; every attempt is recorded in
`candidates.md` §3.

Admitted captures (HTTP status, bytes of the raw response, raw sha256 in `candidates.json`):
C1 OpenEdition/EHESS 200; C2 hcmc.uvic.ca 200; C3 Perseus hopper 200; C4 Persée 200;
C5 journal.fi 200; C6 Maynooth eprint 200; C7 Oxford ORA 200; C8 Kokugakuin Digital Museum 200;
C9 ojs.unm.ac.id 200; C10 Wikisource 200; C11 thetorah.com 200.

## UNREACHABLE, named with the exact response

- **R01** `dspace.cuni.cz/bitstream/handle/20.500.11956/64612/140044187.pdf` — attempt 1 HTTP 429,
  162 B nginx `429 Too Many Requests` page; attempts 2 and 3 curl rc=28 after 30 s each.
- **R02** `archive.chs.harvard.edu/CHS/article/display/3963.8-the-oath-in-greece` — 3 × curl rc=28
  (connection timeout, 0 B).
- **R03** `nome.unak.is/wordpress/05-1/…` — curl rc=60, TLS certificate verify failed; verification
  was not bypassed.
- **R04** Fordham `ir.lawnet.fordham.edu` HTTP 403 (5,675 B); **R06** George Fox digitalcommons HTTP 403
  (5,634 B); **R08** uplopen HTTP 403 (134 B); **R14/R22** sacred-texts HTTP 403 (5,686 B).
- **R07/R12** JSTOR answered HTTP 200 with a 3,038 B `<title>Client Challenge</title>` wall — recorded as
  a wall, not routed around.
- **Wayback** `web.archive.org` CDX and `/web/…` fetches: curl rc=28 on every attempt, up to
  `--max-time 110`. The `archive.org/wayback/available` API answered normally and supplied the
  eight same-page status-200 timestamps recorded in `candidates.md` §2. For C3, C4 and C9 that API
  returned an empty `archived_snapshots` for the canonical URL and for every variant probed; the
  same API's status-200 answers for the other URLs are the positive control, so the empties are
  recorded as "no same-page capture found via the availability API", not as absence.

## Tools

No tool was installed or upgraded: none was needed. Plain `curl`, `pdftotext` (poppler, already
present), `python3` (stdlib only) and `grep` covered the work. No pacman action was taken
(pacman is paused host-wide).

## Blockers and open items for other seats

1. **Registry seat (ExecRegistry96)** — the eleven rows above are ready for id assignment from
   S975. Leg C7 of the frozen counter looks for capture copies under `reports/round-96/evidence/`;
   that directory is the registry seat's to write. My captures are under
   `.ufo/waves/round-96/w1/stage/ScoutSources96/captures/` and can be copied from there.
2. **Wayback bodies** — I could not download any archived capture (`web.archive.org` timed out on
   every attempt). The timestamps in `candidates.json` are availability-API pointers; the registry
   seat should open each capture and confirm the anchor quote before writing a row.
3. **C4 capture extent** — Persée serves the Ó Murchú article's opening section as text and the
   remaining pages as page images, so the capture holds the article head only. Any row anchored on
   C4 should quote from that opening paragraph, or the registry seat should re-open the per-page
   transcription service.
4. **Host incident** — a sibling seat (`ConnectorScope-23`) reported deleting `/fast/scratch/hyaku/kake-r97`
   (the round parent for a different lane group). My scratch tree
   `/fast/scratch/hyaku/kotodama-r96/ScoutSources96/` is under a different parent and was intact; I
   re-created it and confirmed it before writing the deliverables.

## Cleanup

`/fast/scratch/hyaku/kotodama-r96/ScoutSources96/` was removed before this report was written;
no temporary file remains outside the stage directory.
