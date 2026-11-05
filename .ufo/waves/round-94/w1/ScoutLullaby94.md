# ScoutLullaby94 — round-94 claim C source seat

Scope: open sources for the frozen claim C topic (lullaby and child-directed song formulae) and
produce registry rows S965+. Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.

## Files written (all inside the seat stage dir, plus this report)

- `.ufo/waves/round-94/w1/stage/ScoutLullaby94/rows.md` — the 11-cell registry rows S965–S969,
  the located-quote table with per-quote `grep -F -c` results, the capture sha256 table, and the
  full attempted-source log with outcomes.
- `.ufo/waves/round-94/w1/stage/ScoutLullaby94/evidence/S965.html`, `S966.pdf`, `S966.txt`,
  `S967.pdf`, `S967.txt`, `S968.html`, `S969.pdf`, `S969.txt` — the captures.
- `.ufo/waves/round-94/w1/stage/ScoutLullaby94/evidence/manifest.json` — per-row capture URL,
  final URL, HTTP status, sha256, byte count, quote and normalisation, in the round-92/93
  manifest shape.
- `.ufo/waves/round-94/w1/stage/ScoutLullaby94/DONE` — written last, one line: the sha256 of
  rows.md, `384f13f18cfc407cf0561070ed176b934d27eb1c1ec06603676ce87a97b9bd1c`.
- `.ufo/waves/round-94/w1/ScoutLullaby94.md` — this report.

No production file was written. `corpus/`, `tools/`, `reports/round-93/*`,
`reports/round-94/claims.json`, `reports/round-94/predispatch.py`, `reports/round-94/predispatch-base.txt`,
the corpus, `SKILL.md`, `PROVINCE.md`, `SCORECARD.md`, `LOG.md` and the fleet root were read only.
No git or jj mutation of any kind was run. The scratch dir `/fast/scratch/hyaku/kotodama-r94/ScoutLullaby94/`
was deleted before this report was written.

## Rows opened

| id | tier | kind | URL | status | capture | sha256 of capture | anchor quote located |
|---|---|---|---|---|---|---|---|
| S965 | A | paper | https://journals.openedition.org/tipa/2987 | 200 | S965.html (177416 B, text/html) | 10a716133b7f95dea02718946fac92e5b5cd4cbce6c7a6909187bacc5a295757 | yes — "Les premières berceuses qui sont adressées aux nouveau-nés sont constituées de sons vocaux rythmiques" (14 words) |
| S966 | A | paper | https://open.journals.ed.ac.uk/ScottishStudies/article/download/593/619 | 200 | S966.pdf (2332266 B) + S966.txt | pdf 901b0f9236170dfd4a03c8f320f3a089f97233e948c16b0d94ee6209ff11e17b / txt 5e810ad6bfcabb1fef5f3d04bcbef4600dbcc133f315429a81949bd63c74d201 | yes — "function of nonsense vocables is strongly indicated by a story which Donald Archie" (13 words) |
| S967 | A | paper | https://www.folklore.ee/tagused/nr90/nurijeva.pdf | 200 | S967.pdf (654637 B) + S967.txt | pdf f566dd70905e8be9c6d4964024bc655af1ff7c81e7ce9b5cc3a6eef0848919e6 / txt 72082b74ee639ef614c1bdd40cf817f8af7b0f81cbaf5f5817cbf0fdf9ba635d | yes — "intonations that are meant to soothe or put the child to sleep" (12 words) |
| S968 | A | paper | https://journals.openedition.org/ced/4965 | 200 | S968.html (208772 B, text/html) | 232a3e466441d16b73a61a97d2d0d42b548ff18859de2df8bf2f100f4c10914f | yes — "une version lente chantée de la comptine ainsi que des enregistrements des trois vers en version parlée" (17 words) |
| S969 | A | paper | https://www.scirp.org/journal/PaperDownload.aspx?paperID=109328 → https://content.scirp.org/pdf/adr_2021052514072571.pdf | 200 | S969.pdf (301659 B) + S969.txt | pdf d7147c8dcf9b374a02e514e01e73a1911bde31157169620a65d0038e1c6fee86 / txt f37239cf1946ee66386f14d2674f8750fa0a1e1b8f786d6762124d9385e119cc | yes — "the refrain stands out as the leading sound modulator in the song." (12 words) |

All five rows are tier A: each is a peer-reviewed journal article whose own body carries the
claim it is filed for, read in full (the HTML body for S965 and S968, the PDF body for S966,
S967 and S969). Every row's anchor cell names the fetch (URL, access date 2026-11-05), the
capture path under `reports/round-94/evidence/` and, for the PDF rows, the PDF's own path beside
the text rendering.

### Quote check

Nineteen located quotes are listed in rows.md (one anchor quote per row plus three or four
further located spans per row the entry author may draw on). Every one was checked with
`grep -F -c` against the capture file named in its row, and every count is exactly 1.
Re-verified after the row table was written:

```
python3 - <<'PY'   # extracts each quote cell from rows.md and counts it in its capture
checked 19 bad 0
PY
```

Normalisation, stated per capture class:
- **HTML captures (S965, S968):** none. The quotes are exact substrings of the raw served HTML
  bytes as fetched, not of a de-tagged rendering. Three quotes needed the typographic
  apostrophe and quote characters the servers actually sent (`l’acte`, `“parler”`, `s’en`,
  `l’interprétation`); three earlier drafts with straight ASCII equivalents were corrected to the
  exact bytes after the check reported them absent.
- **PDF captures (S966, S967, S969):** `pdftotext` (poppler, default layout) of the served PDF,
  one text file per PDF, committed beside the PDF as `S966.txt` / `S967.txt` / `S969.txt`. Each
  quote occurs exactly once in that text rendering.

Anchor quote word counts, all at or under the 25-word cap: S965 14, S966 13, S967 12, S968 17,
S969 12. The longest of the nineteen supporting quotes is 22 words.

## Coverage map (grep counts, corpus/knowledge, case-insensitive)

Measured with `grep -ril` (files) and `grep -rio` (occurrences) over
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge`:

| term | files | occurrences |
|---|---|---|
| lullaby | 0 | 0 |
| lullab | 1 | 1 |
| cradle song | 0 | 0 |
| cradle | 2 | 2 |
| nonsense syllable | 0 | 0 |
| nonsense | 0 | 0 |
| child-directed | 1 | 1 |
| berceuse | 0 | 0 |
| nursery rhyme | 0 | 0 |
| refrain | 7 | 16 |
| putting a child to sleep | 0 | 0 |

The single `lullab` hit is `myth-symbol/motif-index-usage.md:108` (a fantasy-inventory reading
for an orphan, not a lullaby claim). The two `cradle` hits are
`culture-material/games-play-sport-contests.md` and `myth-symbol/mineral-stone-symbolism.md`,
neither about lullaby text. The one `child-directed` hit is
`linguistics/language-socialization-and-acquisition.md` (S743, Japanese child-directed verbs),
which is infant-directed speech, not song text. `corpus/knowledge/linguistics/` holds 38 files
and no file named for the lullaby or child-song register: the ground is a zero-owner filename.

## Registry grammar check

The five rows were appended to a copy of `corpus/SOURCES.md` in scratch and validated with the
lane's own census:

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-11-05 ./cen/test-shokunin
rc=0
```

`rc=0` with the five rows present; the only lines printed are the W01/W04 warnings that the
base lane already prints (duplicate URL across scopes, tier-C mined rows), none of them naming
S965–S969. Each row has exactly 11 cells; kind `paper`, tier `A`, status `mined`, opened
`2026-11-05`, recheck `180d`, used-by `corpus/knowledge/linguistics/lullaby-child-song-formulae.md`.

### Grader-leg dry run on the proposed rows

The five rows and the manifest were also run through the lane's own grader functions in
`tools/check-advance-evidence.py` (imported read-only, no argument run, no file written):

- `MEANING` conditions: for all five anchor quotes, `norm(quote) in norm(source cell)` is False
  and `norm(quote) in norm(teaches cell)` is False, so no quote is a self-quote or a title
  echo; the content-word overlap with teaches/scope/anchor is at least 1 for every anchor
  quote, above the tool's `--min-overlap` default of 1.
- `CAPTURE` conditions: for all five rows the manifest's sha256 matches the staged capture
  bytes, `http_status` is 200, `fetched_at` is a local ISO instant dated 2026-11-05, the capture
  path is relative and confined under `reports/round-94/evidence/`, and the quote occurs in the
  grader's own normalised capture body text (`html_body_text` + `norm`): all True.
- `GATE` binding: a lesson gate quote must share at least 3 content words with the row's
  teaches cell or the manifest quote. rows.md marks, per quote, which of the nineteen are safe
  on a gate line (overlap >= 3) and which belong in the entry body only (overlap < 3); all five
  primary quotes are safe.

This was a dry run against the grader's helper functions, not a full run of the tool: the
tool's own fixture path needs the landed entry, the landed lesson and a lands registry, which
do not exist yet.


## Sources attempted and not rows (all in rows.md with the exact response)

OPENED but not rows: Berbel 2026 "Kinderlieder in Translation" (Linguistische Treffen in Wrocław 29,
HTTP 200, 814173 B) — a translation study of German children's songs with finger-play gestures,
offering no located quote about nonsense-syllable refrains, archaic retention or the lullaby as
archive; Aubinet 2026 *The Lullaby's Outline* (Routledge preview PDF, HTTP 200, 1346887 B) —
publisher front matter and blurb only, so tier B for substantive claims with no body argument;
Humanus 16(1) 2017 "Meaning and Form in Nursery Rhymes Translation" (HTTP 200 but 23120 B of
text/html — the OJS viewer page, not the PDF, so no article body was served).

UNREACHABLE, with the exact response: MDPI *Languages* 10(10) 257 (HTTP 403, 399 B access-denied
notice); MDPI *Languages* 10(9) 229 (HTTP 403, 400 B); *Textes & Contextes* 4110 (HTTP 403, 2747 B
after redirect to `preo.ube.fr`); *Intercultural Studies* 1632 download (HTTP 406, 413 B); UNT
dissertation PDF (curl exit 28, read timeout after 30 s, 0 bytes; not retried, a read timeout is
outside the declared transient-5xx/429 retry class); ballad-index.org (curl exit 6, host does not
resolve); ojs.badanbahasa.kemdikbud.go.id (curl exit 6, host does not resolve); Europe PMC
search (HTTP 502, 150 B); gutendex book search (HTTP 503 then a timeout).

No bot challenge was met anywhere and none was passed. Every request was a plain `curl` with the
default user agent and `-L`; no `-k`, no headless browser, no login, no paywall circumvention.

## Tooling

None installed. `pdftotext` (poppler) was already present on the host and was the only tool used
beyond `curl`, `grep`, `sha256sum` and `python3` (stdlib only). No pacman transaction was run and
no sysctl or host setting was touched.

## Hand-off notes for the L1

1. The five capture files and `manifest.json` are staged at
   `.ufo/waves/round-94/w1/stage/ScoutLullaby94/evidence/`. Claim C's SOURCES leg wants the
   captures committed under `reports/round-94/evidence/`; the sha256 values in rows.md and in
   manifest.json are the digests of the staged bytes, so they carry over unchanged on a plain
   copy.
2. `rows.md` gives the five rows in the `corpus/SOURCES.md` column order
   (`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`)
   as a single markdown table ready to append after S964, in id order, with a search-log note.
3. The five ids are S965, S966, S967, S968, S969 — contiguous from the frozen
   `registry_new_id_start` S965, and above the base's highest id S964 (888 rows at base, so 893
   after landing). The claim C predicate needs at least three rows with tier A or B, status
   `mined`, opened 2026-11-05, a fetch recorded in the anchor cell, and an anchor quote of at
   most 25 words that is an exact substring of a committed capture; all five meet that.
4. Every new row must be cited by the entry. The anchor quotes and the further located spans in
   rows.md are what the entry author can quote; each has its capture and page or section named.
5. The CENSUS leg was checked against a scratch copy of the registry with the rows appended
   (`rc=0`). It still needs re-running at the lands revision, where the entry file
   `corpus/knowledge/linguistics/lullaby-child-song-formulae.md` exists on disk for the E11
   used-by check; in my scratch fixture that path was a stub, so the check passed on the stub,
   not on the real entry.

## Not measured / open

- The `INDEX` leg (`tools/check-corpus-index.py`) was not run against a landed tree: it reads the
  real corpus tree, which the entry seat owns, and the entry file does not exist in the lane yet.
- `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` was not run against
  the live lane, because the rows are not landed; the equivalent check was run on a scratch copy
  of the registry with the rows appended (`rc=0`).
- Whether the entry author cites all five rows is outside this seat; the claim C SOURCES leg
  requires every new row to be cited by the entry, so a decision to drop one row should be
  communicated before the L1 lands the registry.
