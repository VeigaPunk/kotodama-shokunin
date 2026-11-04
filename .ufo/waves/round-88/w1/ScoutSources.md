# ScoutSources — round 88, w1

Read-only source verification of the three reserved ids behind claim D. No production file was
edited, no registry row was written, no git/jj command mutated anything. All commands below were
run from the lane root or from the seat's own scratch; every receipt lives in
`.ufo/waves/round-88/w1/stage/ScoutSources/`.

Lane: `kotodama-shokunin` · freeze `4b76524c51e1c2f76c99eeb3b629cfac08a44a76` · base
`4956282281dac1306cfbe59523e46dde99749d75` · controls `0c8c733088df8c4f06770c9e714360eed7f29272`.

## 1. What I opened, and how it answered

| id | live URL | live result on 2026-11-04 | what was actually read |
|---|---|---|---|
| S931 | `https://journals.openedition.org/terrain/17506?lang=en` | HTTP 200 but the body is an **Anubis bot-check challenge page** (5,281 bytes, `anubis_challenge` JSON embedded). The challenge was **met and not passed**; no article text was served. | Wayback capture `20251211231049id_` of the same URL (190,162 bytes) — the English article body, 41 numbered paragraphs |
| S932 | `https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/` | HTTP 200, 65,959 bytes, article body served | the live body |
| S933 | `https://mathshistory.st-andrews.ac.uk/HistTopics/Egyptian_numerals/` | HTTP 200, 23,397 bytes, article body served | the live body |

Live MacTutor bytes are byte-identical to my saved captures (sha256 `ac4701fb…` Babylonian,
`5f6ef5ee…` Egyptian), so the quotes below are stable against a re-fetch.

**S931 metadata** (from the served page head): Chrisomalis, Stephen — "The writing of numbers.
Recounting and recomposing numerical notations", *Terrain. Anthropologie & sciences humaines* 70,
published 2018/10/09, doi 10.4000/terrain.17506. The task's "Chrisomalis2018" identification is
correct.

**Paragraph numbering for S931** is the publisher's own: each of the 41 `<p class="texte">` blocks
carries a `<span class="paranumber">N</span>` marker, 1..41, monotonically ascending, and the same
numbering is present in the 2019 and 2021 captures. So `¶7`–`¶10` and `¶25` are the publisher's
ordinals, not my counting. The task's "paragraph25" and "typology paragraphs7-10" both resolve.

## 2. Exact quotes (<= 25 words), with locator

Full table with hit counts, capture manifest and sha256 digests:
`.ufo/waves/round-88/w1/stage/ScoutSources/receipts/quotes.md`.

Every quote below was located **exactly once** in the served body, and **exactly once** in the
archived capture of the same page (durability re-check, same receipt file).

S931 — Terrain (typology):
- ¶7 — "All numerical notations fall into five basic typological categories, across two dimensions (fig. 1)."
- ¶7 — "How are the signs formed and combined within any power of the base?"
- ¶8 — "We may call these, respectively, intraexponential and interexponential principles."
- ¶8 — "There are only three basic intraexponential principles." / "Similarly, there are only two interexponential principles."
- ¶8 — "Cumulative systems are those where signs are repeated and added within each power"
- ¶8 — "Multiplicative systems use two signs per power, which are multiplied together."
- ¶9 — "Combining these two principles provides six possible types, of which one (multiplicative-positional) is logically excluded"
- ¶9 — "because multiplicative systems express power through special power signs, not through place value"
- ¶9 — "The Babylonian sexagesimal (base 60) numerals exemplify cumulative-positional notation"
- ¶10 — "all known systems use these five principles, and no others"
- ¶10 — "This avoids the teleological argument of Ifrah (1987) and Dehaene (1997)"
- ¶10 — "it is evident that there is no perfect system"
- ¶19 — "the early hieroglyphic numerals used in predynastic Egypt" / "are cumulative-additive"
- ¶25 — "Cumulative-positional numeral systems are cross-culturally very rare, in fact the rarest of the five types described above."
- ¶25 — "while this structure is excellent for manipulating numbers, it is among the least concise ways to write a number"
- ¶25 — "Because numerical notation is, first and foremost, a system for numerical representation, not for computation"

S932 — MacTutor Babylonian numerals (block indices under the stated scope):
- body ¶2 — "the Babylonians only had to learn two symbols to produce their base 60 positional system"
- body ¶3 — "the 59 numbers, which go into one of the places of the system, were built from a 'unit' symbol and a 'ten' symbol"
- body ¶10 — "A much more serious problem was the fact that there was no zero to put into an empty position."

S933 — MacTutor Egyptian numerals:
- body ¶3 — "The Egyptians had a bases 10 system of hieroglyphs for numerals."
- body ¶3 — "separate symbols for one unit, one ten, one hundred, one thousand, one ten thousand, one hundred thousand, and one million"
- body ¶22 — "the hieratic numerals did not form a positional system so the particular numerals could be written in any order"
- body ¶22 — "The number 9999 had just 4 hieratic symbols instead of 36 hieroglyphs."

Extraction scope (stated per QUALITY 33): S931 = the 41 `p.texte` body blocks, publisher numbering.
S932/S933 = the page body between the first body sentence and the `References` heading, block-indexed
from 1; MacTutor pages carry no publisher paragraph numbers, so those locators are this seat's block
index under the stated scope, **not** an article-asserted ordinal. `tools/check-paragraph-locator.py`
is MediaWiki-scoped and does not apply to these pages.

## 3. Tier and scope judgments

Full reasoning: `.ufo/waves/round-88/w1/stage/ScoutSources/receipts/tier-and-scope.md`.

- **S931 — tier A**, kind `paper`. Scope: *the two-axis typology of numerical notations and the
  trade-offs among its five types*. Caveat: fig. 1 is captioned "after Chrisomalis 2004, 2010", so
  the typology is the author's earlier work restated here — the scope should read "the typology as
  presented in this 2018 paper", not "the origin of the typology".
- **S932 — tier B**, kind `docs`. Scope: *how a sexagesimal positional notation is built and where
  it fails without a zero*. It cannot carry the typology: MacTutor never says "cumulative-positional".
- **S933 — tier B**, kind `docs`. Scope: *how Egyptian hieroglyphic and hieratic numerals are built
  and why the hieratic form is non-positional*. It cannot carry the typology either; the
  cumulative-additive classification of early Egyptian hieroglyphic numerals is S931 ¶19.

Three concrete hazards for whoever writes the rows and the section:

1. **No `|` may appear inside any registry cell.** `reports/round-88/measure88.py:claim_d` splits the
   row on `|` to read tier and status; a pipe inside a cell shifts the parsed columns and the
   `new-rows-mined` leg reads the wrong fields. The `teaches` cell for S932/S933 in particular must
   not quote a table row.
2. **S933's live text carries typos** — "The Egyptians had a bases 10 system" and "they has separate
   symbols". A quote cell reproduces them verbatim; the entry prose and the `teaches` cell must not.
3. **The S931 access note must not read like a bypass.** `tools/check-source-access.py` flags a mined
   row whose source/anchor/teaches cell records getting *past* an access control. I tested six
   candidate phrasings of "challenge met, not passed; content read from Wayback capture" against that
   tool's own BYPASS regex; none matched. "solved the challenge" or "read via headless browser" would
   match and must not be used.

## 4. Duplicate-URL / scope-collision scan and reserved ids

Full receipt: `.ufo/waves/round-88/w1/stage/ScoutSources/receipts/duplicate-and-id-scan.md`.

- **No duplicate URL.** I scanned all 21 fleet `*/corpus/SOURCES.md` registries. `terrain/17506`:
  0 hits everywhere. `mathshistory.st-andrews.ac.uk`: 0 hits everywhere. So no census E04
  (URL+scope duplicate) and no W04 (same URL across scopes) can fire for these three rows.
- **Chrisomalis has no registry row anywhere** — `corpus/SOURCES.md` contains 0 occurrences of
  "Chrisomalis" across 854 rows — but the author is already cited inside the corpus at
  `numerals-and-measures.md:23,111,209` and `number-symbolism.md:4,5,15,100,142`. The new rows must
  not double-count what the corpus already asserts without a registry receipt.
- **S931/S932/S933 are unused at base and everywhere else.**
  - `git show 4956282281dac1306cfbe59523e46dde99749d75:corpus/SOURCES.md | grep -c "S93[123]"` → **0**
  - base numerals entry carries **0** S-ids of any kind (`grep -oE "\bS[0-9]{3}\b"` → empty)
  - current registry: 854 rows, max id **S930**, 0 duplicate ids → S931-S933 free
  - no other lane registry carries 931-933 (fleet-wide id scan)
  - the round-71 `id-renumber-map.json` mentions S931/S932/S933 only as *staged* ids that were
    renumbered to S946/S947/S948; no registry row ever carried them.

Lane checks I ran read-only (no files written):
`sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, 0 E-findings,
35 pre-existing W-findings; `tools/check-source-access.py --root .` → exit 0, `ACCESS: 3 flagged
rows, 0 findings`; `tools/check-cited-lines.py corpus/knowledge/linguistics/numerals-and-measures.md`
→ exit 0, `CITED-LINES: 0 finding(s) in 1 file(s)`.

## 5. Depth vs coverage, and duplication

Full assessment: `.ufo/waves/round-88/w1/stage/ScoutSources/receipts/depth-vs-coverage.md`.

The held entry touches notation in **one clause** (`numerals-and-measures.md:111`) and its own open
item (2) says "no entry yet exists for numeral *notation* as a writing subsystem (Chrisomalis-grade
detail)". No corpus file holds a two-axis typology, a five-type classification, or the trade-offs
among the types.

One finding worth L1's attention: that clause calls the notation kinds "typological stages" — the
exact teleological framing S931 ¶10 rejects ("This avoids the teleological argument of Ifrah (1987)
and Dehaene (1997)" … "it is evident that there is no perfect system"). So the proposed section does
not merely add a parallel section; it **corrects an existing corpus statement** that currently
mis-frames notation as a progression toward a perfect system. Whether the new section rewrites that
clause or leaves the contradiction standing is L1's call — the claim's `bounds` speak to the section,
not to §5.

Overlap with adjacent files is limited and each is a different owner: `writing-systems.md:21` lists
"math notation" under semasiography and `:146` lists numerals as "missing plumbing" (a coverage
note, not a typology); `number-symbolism.md:100,142` uses Chrisomalis 2010 for number *meaning* and
era-marking, not notation structure. The D claim's `bounds` already state the section does not
supersede `writing-systems.md`.

**Wording hazard for the section author.** The dispatch asks for "five types from coefficient vs
power axes". That is not Chrisomalis's language. The paper's own terms (¶7-¶8) are the two questions
about powers of the base and about combining the different powers, named "intraexponential and
interexponential". A section presenting "coefficient vs power" as the source's axes would be a
paraphrase dressed as the source's terms. Use the quoted terms.

The five types as the paper names them (¶9): cumulative-additive (Greek acrophonic; and early
Egyptian hieroglyphic numerals per ¶19), cumulative-positional (Babylonian sexagesimal), ciphered-
additive (Georgian alphabetic), ciphered-positional (Lao; and Western numerals), multiplicative-
additive (classical Chinese). Multiplicative-positional is the logically excluded sixth (¶9). The
trade-off material is ¶10 (ciphered-additive most compact; cumulative-positional "often as few as
two or three" signs but "far less compact") and ¶25 (cumulative-positional is "the rarest of the
five types").

## 5b. Clause-scoping hazard for the section and the rows (read by L1 and the scribes)

Two lane tools constrain how the ids may appear, and they pull in opposite directions from a naive
reading of the D predicate:

- The frozen D leg `new-rows-cited` only requires that `S931`, `S932` and `S933` each appear
  somewhere inside the section text (`re.search(r'\bS93[123]\b', section)`), table rows included.
- `tools/check-cited-lines.py` (QUALITY 15) additionally requires that **no table row carries any
  S-id** and that **a cited line carries exactly one distinct S-id** (`MULTI-ID` when a line carries
  two or more). The entry currently passes this lint with 0 findings, so a new section can regress it.

So the three ids must appear in the section's **prose**, one id per line, and not inside any table
row. The dispatch already says "cite S931 S932 S933 outside table rows (QUALITY15)" — that is
correct and load-bearing; a table row carrying `S931` would satisfy the frozen D leg and still fail
the lane lint.

## 6. Defects and unresolved items I could not close

1. **The `?lang=en` URL form has no capture of its own.** CDX exact query for
   `journals.openedition.org/terrain/17506?lang=en` returns `[]`. Captures exist only for the
   query-less URL, whose body serves the same English article (41 paragraphs, verified). The S931
   row should therefore name the live URL without the query, or name the capture of the query-less
   same page. This is the kind of gap that QUALITY 21/24 exists for; I did not file it as a lesson
   because I have no write access to `corpus/lessons/`.
2. **The S931 live URL is behind an Anubis challenge right now.** The article text is not
   re-openable at that URL by a plain fetch today. The capture is the durable route; the row must say
   the challenge was met and not passed. I could not verify from inside the lane how long the
   challenge state persists.
3. **MacTutor pages are a 2000 vintage** ("Last Update December 2000"). Tier B is right, but any
   recheck cadence shorter than the lane's usual 180d/365d would be noise; and the pages' own
   base-60-origin discussion is explicitly the authors' speculation ("I [EFR] feel that all of these
   reasons are really not worth considering seriously"), so it must not be rowed as a finding.
4. **No tool named `check-sources-census` exists** in the lane or the fleet, though the D kill rule
   names "the phenomenon checked by check-sources-census". The nearest real artifact is the fleet
   script `scripts/sources-census.sh` (mode `validate`), which I ran: exit 0, 0 error findings. If
   the frozen kill rule intends that script, its behaviour is satisfied; if it intends a lane-local
   tool, that tool is missing. I did not amend the frozen claim.
5. **MacTutor row anchors are block indices, not publisher ordinals** (no publisher numbering on
   those pages). A reviewer re-opening them must use the same stated scope to reproduce the index;
   the receipt states the scope so this is reproducible, but it is weaker than the Terrain anchors.

## 7. Files written by this seat

- `.ufo/waves/round-88/w1/stage/ScoutSources/captures/s931-terrain.html` (live challenge page),
  `s931-terrain-wb.html` (the capture actually read), `s931-paras-full.txt` (41 numbered body
  paragraphs), `cdx-terrain.json`, `s932-babylonian.html`, `s932-text.txt`, `s932-wb.html`,
  `s933-egyptian.html`, `s933-text.txt`, `s933-wb.html`
- `.ufo/waves/round-88/w1/stage/ScoutSources/receipts/quotes.md`
- `.ufo/waves/round-88/w1/stage/ScoutSources/receipts/tier-and-scope.md`
- `.ufo/waves/round-88/w1/stage/ScoutSources/receipts/duplicate-and-id-scan.md`
- `.ufo/waves/round-88/w1/stage/ScoutSources/receipts/depth-vs-coverage.md`
- this report: `.ufo/waves/round-88/w1/ScoutSources.md`

The seat's scratch working directory (the round-88 ScoutSources scratch under the hyaku scratch
root) was deleted after the captures and receipts were copied into the stage. No tool was installed
for this seat; `curl`, `python3` (stdlib), `git` (read-only) and the lane's own read-only checkers
were used. No pacman transaction was run.

No S-id was cited to claim O; S931-S933 stay reserved for D. No canon or historical certification
is asserted anywhere above.
