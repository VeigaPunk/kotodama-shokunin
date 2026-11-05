# ExecIndepRefetch — round 90, w1 (claim C anti-forgery defence)

Seat: independent re-fetch. Base 6b0b86e4, freeze d0b6f2a7 (claims.json read first, unamended).
Stage: `.ufo/waves/round-90/w1/stage/ExecIndepRefetch/` — `caps/` (32 bodies), `fetch.json`,
`agreement.json`, `forgery-class.txt`, `quote-candidates.json`, `prose-check.py`,
`prose-check-selftest.txt`, `recheck.py`. Scratch `/fast/scratch/hyaku/kotodama-r90/ExecIndepRefetch/`
(forge fixture + drivers) deleted before yield. No production file, no sibling stage, no git/jj
mutation was written by this seat; `git show` / `git ls-tree` / `git cat-file` only.

## 1. Method

Every surface was opened with `curl -sS -L -D <headers> -o <body>` (ordinary HTTP, no browser, no
CAPTCHA handling, no paywall workaround). Body saved verbatim, sha256 taken over the bytes on disk,
local instant recorded with the -03:00 offset. All 32 captures carry a status, an instant, a
sha256 and a byte count in `fetch.json`. Nothing was normalised, tag-stripped or re-wrapped before
hashing: a capture is the server's bytes, so a later re-fetch can be diffed against it.

## 2. Seed verdicts (for holding the scribe to A/B)

| seed | observed | verdict |
|---|---|---|
| `wals.info/chapter/72` | 200, "Chapter Imperative-Hortative Systems", van der Auwera / Dobrushina / Goussev | **A** — usable as labelled |
| `wals.info/chapter/73` | 200, "Chapter The Optative", Dobrushina / van der Auwera / Goussev | **A** — usable as labelled |
| `wals.info/chapter/74` | 200, but the page is **"Situational Possibility"** (van der Auwera & Ammann) | **A page, wrong seed** — the Prohibitive moved to **chapter 71**; a row citing /74 for prohibition would cite a chapter that does not say it |
| `glossary.sil.org/term/vocative` | **404** ("404 Page not found · Glossary of Linguistic Terms") | **dead** — working equivalent `glossary.sil.org/term/vocative-case` (200, B) |
| `glossary.sil.org/term/prayer` | **404** | **dead** — the glossary has no prayer term at all: prayer, prayers, invocation, hymn, supplication, petition, blessing, curse, vow, votive, dedicatory all 404 |
| `en.wikipedia.org/wiki/Votive_offering` | 200 | **C** — tertiary encyclopedia, no named author → reject under claims.json's tier rule |
| `en.wikipedia.org/wiki/Curse_tablet` | 200 | **C** — same |
| `en.wikipedia.org/wiki/Sacred_language` | 200 | **C** — same |

Tier rule applied as frozen: A = primary reference / scholarly chapter or catalogue with a named
author; B = authoritative glossary or museum/institution page; C = tertiary or unreferenced
encyclopedia copy. Three of the eight seeds are therefore C, two are dead, and one (74) is alive
but mislabelled. Only chapters 72 and 73 can be used exactly as seeded.

## 3. Verified A/B quote table (my own fetches, not the scribe's)

Every quote below was checked with the grader's own `norm()` against **my** capture bytes, and each
is 20–158 chars and ≤20 words (bounds: ≤25 words, ≥20 chars).

| surface | tier | located quote | present in my capture |
|---|---|---|---|
| `wals.info/chapter/71` — The Prohibitive | A | "The prohibitive uses the verbal construction of the second singular imperative and a sentential negative strategy found in (indicative) declaratives" | yes |
| `wals.info/chapter/72` — Imperative-Hortative | A | "cross-linguistically, the most pervasively grammaticalized imperative-hortative is the imperative second singular, the order or request to just one addressee." | yes |
| `wals.info/chapter/73` — The Optative | A | "this chapter restricts attention to languages with a dedicated inflectional optative form as in (1)" | yes |
| `glossary.sil.org/term/vocative-case` | B | "Vocative case is a case that marks a noun whose referent is being addressed." | yes |
| `atticinscriptions.com/inscription/AIUK45/14` | A | "This is one of a number of imperial period dedications to Zeus Hypsistos" | yes |
| `etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.4.05.1` — Enlil A | A | "The fate he decides is everlasting, his glance makes the mountains anxious" | yes |

Ids are deliberately omitted here: the scribe has already assigned S942–S948 (see §5), and these
are the fallback spans this seat verified independently should a row need re-sourcing.

Capture provenance: `caps/wals-71.txt`, `caps/aio-aiuk45-14.txt`, `caps/etcsl-enlil-a.txt`,
`caps/wals-72.txt`, `caps/wals-73.txt`, `caps/sil-vocative-case.txt`; sha256, status and instant in
`fetch.json`. AIO is A by named translators (Peter Liddel, Polly Low) and named publication
(AIUK 4.5, BM Dedications); ETCSL is A as an Oxford scholarly edition; SIL is B as an authoritative
glossary. WALS chapters carry named authors on the page itself.

**Operational caveat the scribe needs.** A gate quote must be a tag-free substring of the *raw*
capture. AIO renders "Eutychis, to the Highest (God), a vow." as two inline spans, so that sentence
is **absent** from its own page capture even though it is visible in a browser; "This is one of a
number of imperial period dedications to Zeus Hypsistos" is present. WALS, ETCSL and SIL prose
spans are clean. Pick quotes from prose spans, never across markup.

## 4. The survivor, demonstrated rather than asserted

Full commands and outputs: `stage/ExecIndepRefetch/forgery-class.txt` (13.6 KB). Fixture lives only
in scratch; no forged capture was ever written inside the lane.

1. **Forged captures + fabricated quotes → `ENTRY-EVIDENCE: PASS legs=6/6`, rc=0.** Three captures
   written by hand ("FORGED CAPTURE … never fetched from any server") with self-consistent sha256,
   http_status 200 and a local ISO instant. Three invented quotes. The counter accepts.
2. **Same fixture, real captures, same fabricated quotes → `FAIL CAPTURE`, rc=1**, one
   "quote absent from capture" per id. This is the defence and it is total: one re-fetch refuted
   every fabricated span.
3. **Real captures + real quotes → `PASS legs=6/6`, rc=0** (control: the fixture is not simply
   unpassable).

Two further entry-mode findings from the same fixture:

- **Title / site-chrome quotes are not refused in entry mode.** Advance mode's MEANING leg refuses
  a chrome quote; entry mode's GATE checks only length, url and date, and CAPTURE only asks that the
  quote occur in the capture — where the page's own `<title>` lives. Run 4 uses three title strings
  ("WALS Online - Chapter The Prohibitive", "Dedication to Zeus Hypsistos by Eutychis", "The
  Electronic Text Corpus of Sumerian Literature") and the counter prints **PASS legs=6/6**. Claim
  C's GATE leg therefore cannot distinguish located prose from chrome. The reviewer and the closure
  must refuse it; the counter will not.
- A capture pointing at the graded entry is refused, but by **confinement** ("capture outside
  reports/round-90/evidence") before the graded-file check fires, because the entry does not live in
  the capture dir. The O selftest exercises "capture is a graded file" with a graded path *inside*
  the capture dir — a different arrangement from this lane's layout.

## 5. agreement.json — capture-level verdict on the scribe's landed evidence

`ScribeEntry/evidence/` now holds seven captures (S942–S948) but no `manifest.json` yet. I fetched
every one of the seven URLs myself and compared bytes. Result: **all seven are honest fetches.**

| scribe id | surface | bytes (both) | verdict |
|---|---|---|---|
| S942 | `wals.info/chapter/72` | 41840 | byte-identical |
| S943 | `wals.info/chapter/73` | 50562 | byte-identical |
| S944 | `wals.info/chapter/71` | 46113 | byte-identical |
| S945 | `glossary.sil.org/term/vocative-case` | 11053 | byte-identical |
| S946 | `atticinscriptions.com/inscription/IGI3/646` | 13536 | byte-identical |
| S947 | `pmc.ncbi.nlm.nih.gov/articles/PMC13671548/` | 295969 | same length; differs only in `ncbi_phid` + `csrfmiddlewaretoken` |
| S948 | `drops.dagstuhl.de/entities/document/10.4230/OASIcs.CMN.2016.12` | 105415 | same length; differs only in `csrf-token` / `_token` |

The two non-identical pairs differ in exactly two lines each, both per-request session tokens; every
content line matches. That is what an honest capture looks like, and it is the shape a forged one
would not have. Tier check on the scribe's surfaces: WALS 71/72/73 are A (named authors on the page),
SIL vocative-case is B (SIL glossary), AIO IGI3 646 is A (AIO translation, named translators), the
PMC capture is Moshe Blidstein in PLOS One (`citation_author`/`citation_journal_title` in the bytes,
doi 10.1371/journal.pone.0361143) so A, and the Dagstuhl capture names Francesco Galofaro and
Magdalena Maria Kubas in OASIcs so A. None of the three C-tier Wikipedia seeds was used.

Quote-level agreement is still **pending**: `manifest.json` does not exist, so there is no scribe
`quote` to test. `agreement.json` records `status: "pending-absent"` with the seven capture rows and an empty
`quote_agreement`. Re-running the check is one command, no scratch needed:

    python3 -B .ufo/waves/round-90/w1/stage/ExecIndepRefetch/recheck.py

It reads the scribe manifest (lane path or stage copy) plus the lesson gate lines, normalises with
the grader's own `norm()`, compares each quote against this seat's capture of the same URL, rewrites
`agreement.json`, and exits 0 (all located) / 1 (a `no`, printing the id and the missing span) /
2 (no manifest — explicitly not a pass). A URL this seat never fetched is reported `unfetched`,
never guessed. Until the manifest lands there is no `no` — and no claim of agreement either.

**This seat ends on exit 2.** The last run of `recheck.py` (20:39 and again after every later check)
printed `PENDING: no scribe manifest; nothing to compare` and returned rc=2. That is explicitly not
a pass: no quote-level agreement has been demonstrated for S942–S948, and L1 must run the same
comparison at integration once `stage/ScribeEntry/evidence/manifest.json` exists.

### 5.1 The chrome trap is live on all seven of the scribe's surfaces, with a prose span ready per id

`stage/ExecIndepRefetch/quote-candidates.json` records, per id, the page `<title>` and one
independently verified prose span from the same capture. Every title below **is present in its own
capture**, and entry mode's GATE leg bounds length and checks url + date only, so each would pass the
frozen predicate as a gate quote. `stage/ExecIndepRefetch/prose-check.py` is the non-frozen
companion check: it classifies a quote PROSE / CHROME against (a) the capture `<title>`, (b) the
first 200 characters of the capture, (c) the row's own source cell. Its selfcheck receipt
`stage/ExecIndepRefetch/prose-check-selftest.txt` flags all seven titles CHROME and all seven
candidates PROSE.

| id | chrome trap (would pass the frozen GATE) | verified prose span to use instead |
|---|---|---|
| S942 | "WALS Online - Chapter Imperative-Hortative Systems" | "The constructions studied have to be grammaticalized, but they need not be morphologically or syntactically uniquely imperative-hortative." |
| S943 | "WALS Online - Chapter The Optative" | "this chapter restricts attention to languages with a dedicated inflectional optative form as in (1)" |
| S944 | "WALS Online - Chapter The Prohibitive" | "The prohibitive uses the verbal construction of the second singular imperative and a sentential negative strategy found in (indicative) declaratives" |
| S945 | "Vocative Case · Glossary of Linguistic Terms" | "Vocative case is a case that marks a noun whose referent is being addressed." |
| S946 | "IGI3 646 Dedication by Smikros the tanner" | "has objected that differences in letter forms mean that Smikros’ dedication cannot be the work of the ‘Hekatompedon Master’." |
| S947 | "Ancient Greek votive epigraphy: Ancient religion between individual choice and cultural trends - PMC" | "on the motives or objectives of the dedication" |
| S948 | "Dei Genitrix: A Generative Grammar for Traditional Litanies" | "We propose the notion of n-selection, a narrative rule which can't be reduced to syntax or semantics" |

Every prose span above was checked with the grader's own `norm()` against my capture of the same
bytes (8–20 words, 20–160 chars). If a scribe gate quote is one of the left-hand strings, the row is
CHROME and the right-hand span is the replacement — that is the per-id answer L1 asked for.

`python3 -B stage/ExecIndepRefetch/prose-check.py --manifest <manifest.json> --lesson <lesson>
--registry corpus/SOURCES.md --receipt <receipt>` runs the same classification over a landed
manifest; exit 0 all PROSE, 1 any CHROME (printing the candidate span inline), 2 nothing to check.

## 6. Base-surface confirmation (read-only)

`git ls-tree 6b0b86e4 corpus/knowledge/linguistics` → 34 files; `git show
6b0b86e4:corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` → rc 128 (absent);
`git show 6b0b86e4:corpus/SOURCES.md` → 865 rows; no S942–S949 anywhere in the worktree registry
yet. The claim's `before` figures hold as written.

## 7. Risks

- **Seed rot is live.** WALS renumbered chapters (74 → Situational Possibility, Prohibitive now 71)
  and the SIL glossary dropped `/term/vocative` and never had a prayer term. A row copied from the
  seed list without opening it would cite a page that contradicts its own scope cell.
- **Entry mode cannot refuse chrome quotes** (§4). If the scribe lifts a gate quote from a title or
  a nav string, claim C's GATE leg passes and the only remaining check is human.
- **Tag-split quotes** (§3) will look like a forgery to the counter while being genuine; the fix is
  to choose a different span, not to edit the capture.
- Wikipedia is C: three of the eight seeds are unusable for mined rows.

## 8. Blockers

None. The only open item is the scribe manifest, which is theirs to write; the comparator is in
place and `agreement.json` records the pending state honestly rather than guessing.

Tooling: no installs, no upgrades, no pacman. `curl`, `python3` and coreutils only.
Assimilation: none.
