# SrcEvansPritchard — round 50 frontier source: Evans-Pritchard, *The Nuer* (1940)

Seat: `ChousaR27R2.SrcEvansPritchard-4` (leaf; no delegation, no background jobs). Lane:
kotodama-shokunin, base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only over the lane;
no production file edited; no git/jj mutation; **no tool installed or updated** (poppler
`pdftotext`/`pdfinfo`/`pdftoppm` already present). Downloads went to `/tmp` only (17.1 MB and
15.0 MB, both > 1 MiB, deliberately outside the lane). Report is author-lane advice, not admission.

## Assigned item and result

Assigned: open a full-text scan of E. E. Evans-Pritchard, *The Nuer* (1940) and return a
SOURCES candidate quoting a located passage on cattle names/colour terms or cattle as idiom.
**Result: quote obtained and visually verified on the printed page — but not through
archive.org, which is unreachable from this egress. The opened copy is an Internet Archive-
digitized scan of the same 1940 Clarendon edition, mirrored on a Duke course host.** See the
access record below before minting the row.

## Access record (what was actually opened)

1. **archive.org direct: unreachable.** `archive.org` resolves to `207.241.224.2`; `curl` to
   `http://archive.org/`, `https://archive.org/` and `https://archive.org/advancedsearch.php`
   timed out at 15–25 s (HTTP 000) on 2026-10-21, repeated. General egress is fine in the same
   minute: `https://example.com` 200, `https://en.wikipedia.org` 301, `https://web.archive.org` 200.
2. **Wayback route: blocked.** `web.archive.org` answered `/details/nuer0000eeev` with HTTP 403;
   response header `x-nid: Claro NXT Telecomunicacoes Ltda` (ISP-level denial). CDX prefix
   queries for `archive.org/details/*nuer*` returned HTTP 403 or timed out. So the archive.org
   item page, its BookReader and its `_djvu.txt` were **not** opened.
3. **Opened instead (HTTP 200, this session):**
   `https://people.duke.edu/~ldbaker/classes/gradtheory/Evans_Pritchard_E_E_The_Nuer_a_description_of_the_modes_1940.pdf`
   — 17,058,687 bytes, 344 PDF pages, text layer present. `pdfinfo`:
   Title "The Nuer : a description of the modes of livelihood and political institutions of a
   Nilotic people"; Author "Evans-Pritchard, E. E. (Edward Evan), 1902-1973";
   **Creator "Digitized by the Internet Archive"**; Producer "Recoded by LuraDocument PDF v2.28";
   CreationDate 2008-09-18; **Keywords `http://www.archive.org/details/nuerdescriptiono00evan`**.
   The keyword string is reproduced exactly as `pdfinfo` printed it; it differs from the
   identifiers a search engine currently lists (`nuerdescriptiono0000evan`, `nuer0000eeev`),
   so do not assert byte identity with any one live item — assert only what the metadata says.
4. **Independent cross-check scan (HTTP 200):**
   `https://sites.evergreen.edu/anthrozoology/wp-content/uploads/sites/142/2015/11/Evans-and-Pritchard.pdf`
   — 15,049,913 bytes, 20 pages, Creator "EPSON DS-5500/6500/7500", a separate 2015 capture of
   Chapter I. It reproduces both load-bearing passages (pp. 18–19 and p. 41) with different OCR
   errors, which rules out a single-scan OCR artifact.
5. **Visual verification:** rasterized PDF pages 43, 71, 74, 75 and 76 (`pdftoppm -r 160`) and read
   the page images. Printed running heads read "19 / INTEREST IN CATTLE" and "INTEREST IN CATTLE / 41";
   both quoted sentences are as transcribed below. Body pagination in this PDF is
   **printed page = PDF page − 24** (verified at 43→19, 71→41, 74→44, 75→45, 76→46).

**Honest status:** the exact archive.org object was not opened. The opened artifact is an
IA-digitized scan of the same edition, obtained from a mirror. If L1 requires the archive.org
URL itself as the row URL, this row cannot be minted this round; if a mirror-opened IA scan is
acceptable (the URL cell names the URL actually opened, the `anchor` cell names the IA item),
the candidate below is ready.

## SOURCES candidate (proposed id S048 — L1 assigns)

```markdown
| S048 | Evans-Pritchard 1940, The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People, Oxford: Clarendon Press — https://people.duke.edu/~ldbaker/classes/gradtheory/Evans_Pritchard_E_E_The_Nuer_a_description_of_the_modes_1940.pdf (Internet Archive-digitized scan, mirror of IA item named in PDF metadata) | book | A | Evans-Pritchard's own 1940 assertions about Nuer cattle idiom, cattle-colour naming and ox-names — not contemporary Nuer practice, not a general law of pastoralists | Ch. I §I pp. 18–19 and §VIII pp. 41–46; printed page = PDF page − 24; PDF Keywords field names IA item `nuerdescriptiono00evan` | cattle are the Nuer social idiom and a social archive — names, genealogies, marriage transfers, ritual and legal argument run through cattle terms (pp. 18–19); naming turns on colour plus colour distribution: ten principal colour terms, twelve common white-plus-one distributions, several hundred permutations, horn/ear and sex/age modifiers, ox-names as age-mate salutations and song material (pp. 41–46) — so a pastoral register must design the herd's naming grammar and its social-archive role together | queued | 2026-10-21 | 365d | — |
```

Field-by-field, for a minting check:

- **URL opened:** the Duke mirror above (HTTP 200, 2026-10-21); IA item named in PDF metadata,
  not reachable direct.
- **kind:** book.
- **tier:** **A**, reasoned — the object is the primary monograph, the author's own 1940 field
  report, so it is authoritative for the only scope claimed: *what Evans-Pritchard asserted in
  this edition*. It is **not** tier A for present-day Nuer herding or for any general
  pastoralist law; those scopes would need their own rows (see Calibration).
- **scope:** Nuer cattle idiom and cattle-colour/ox-name vocabulary as reported in the 1940
  edition, Chapter I §I and §VIII.
- **access date:** 2026-10-21.
- **recheck:** 365d — the mirror is a course host and can disappear; the printed pagination is
  stable, so a recheck is about link rot and edition identity, not content change. Re-open an
  archive.org copy when the host is reachable, and prefer the 1940 Clarendon pagination.
- **status:** queued (opened, worth mining); set `used-by` to
  `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` when C lands and cites it.

Gate line, round-49 format:

```
- S048 — https://people.duke.edu/~ldbaker/classes/gradtheory/Evans_Pritchard_E_E_The_Nuer_a_description_of_the_modes_1940.pdf — accessed 2026-10-21 — Ch. I §I, p. 19: "Nuer tend to define all social processes and relationships in terms of cattle." Grounds: cattle as social idiom (IA-digitized scan; archive.org host unreachable, see report).
```

## Located passages (all read on the opened scan; p. 19, 41, 44, 45 and 46 read on page images)

| Location | Verbatim (quote; word count) | What it supports |
|---|---|---|
| Ch. I §I, p. 19 | "Nuer tend to define all social processes and relationships in terms of cattle." (13) | the register claim: stock as social grammar, not only calories |
| Ch. I §I, p. 19 | "Their social idiom is a bovine idiom." (7) | the thesis sentence the entry may cite once, never universalize |
| Ch. I §I, p. 18 | "Hence a Nuer genealogy may sound like an inventory of a kraal." (12) | herd history as social archive |
| Ch. I §I, p. 18 | "the history of each cow in a kraal … an account of all the kinship links and affinities of the owners" (ellipsis-span; not contiguous) | one cow's biography encodes kinship and mystical ties — a design rule for herd records |
| Ch. I §VIII, p. 41 | "In naming a Nuer cow one has to notice its colours and the way in which they are distributed on its body." (22) | the naming grammar: colour × distribution, not colour alone |
| Ch. I §VIII, p. 41 | "There are ten principal colour terms: white (bor), black (car), brown (lual), chestnut (dol), tawny (yan), mouse-grey (lou), bay (thiang), sandy-grey (lith), blue and strawberry roan (yil), and chocolate (gwir)." (30) | the term set; quote as glossed English, see Calibration |
| Ch. I §VIII, p. 44 | "it is evident from the few examples cited that there are several hundred colour permutations." (15) | vocabulary density as evidence of interest; the entry's build-order warning |
| Ch. I §VIII, p. 45 | "an imposing and complicated system of ramifications which bears eloquent witness to the social value of cattle" (17) | the density→value inference, in EP's own words |
| Ch. I §VIII, p. 45 | "these ox-names are the preferred salutations among age-mates" (8) | ox-names as address register, not decoration |
| Ch. I §VIII, pp. 45–46 | "Men salute one another with these names" (7); ox-names chanted at dances and in poems, shouted when spearing | the name system reaches speech genres — a handoff point to the linguistics partition |

Structural detail worth carrying into the entry's build order (all p. 41–46): a cattle
description composes **base colour × distribution term × horn shape/ear cut × sex/age prefix**
(`tut` bull, `yang` cow, `thak` ox, `nac` heifer, `ruath` male calf, `dou` female calf, `kol`
calf not yet grazing); distribution compounds take the form colour + `looka`/`roal` (e.g. white
face `kwe looka`, white shoulder `rol looka`); `cuany` (more than two colours) is rare; ox proper
names add ornament/quality terms (`luth` large bell, `gier` small bell, `lue` long tassel,
`dhuor` short tassel, `wak` tinkling of an ox-bell, `cwai` fatness, `boi` shining whiteness).
That is a ready-made worked lexicon for a worldbuilder, and EP explicitly frames the terms as
**ideal distributions an actual coat approximates** (p. 45) — the design licence for a finite
term set over infinite coats.

## What it teaches the entry (which sections)

The pastoralism entry does not exist yet at base (`ls corpus/knowledge/culture-material/
pastoralism-animal-husbandry.md` → absent), so section numbers are the hunting-foraging
model's (`hunting-foraging-subsistence.md:25–203`); map by topic, not number.

1. **§1 register property** (the opening claim): the herd is not just a calorie store — it is
   the culture's **social idiom and archive**. EP p. 19 ("social idiom"), p. 18 (genealogy as
   kraal inventory; a cow's history carries kinship and mystical ties). Design consequence the
   entry should state: decide what the herd *records* (descent, marriage transfers, ritual
   obligations) before deciding what it produces.
2. **Herd-marking / naming section** (the entry's vocabulary-density section, wherever
   numbered): pp. 41–46 give the full worked template — ten base colour terms, twelve common
   white-plus-one distributions, several hundred permutations, horn/ear and sex/age modifiers,
   ox-names as salutations and song material. This is also the section that can carry the
   **one-owner boundary** against `linguistics/color-terminology.md`: EP's English glosses are
   a lexical inventory, not a basic-colour-term claim; the linguistics entry owns the
   colour-term debate, this entry owns the husbandry naming *use*.
3. **Distribution / bridewealth row** (the hunting model's §6 analogue, recast for stock):
   p. 18 — "movements of cattle from kraal to kraal are equivalent to lines on a genealogical
   chart"; marriage transfers as the herd's bookkeeping.
4. **§8 taboo/ritual** (if the pastoral entry keeps that section): pp. 18–19 — cows dedicated
   to lineage spirits and personal spirits, beasts to ghosts, ashes rubbed on the back to reach
   the associated spirit, sacrifice of ram/he-goat/ox. Cite as the ritual *use* of stock; the
   rite itself stays with `myth-symbol/animal-symbolism.md` (one-owner rule).
5. **Build order / decision table**: the composition rule (colour × distribution × horn ×
   age/sex) is a four-slot generative grammar the entry can turn into a table; EP's "ideal
   distributions" note (p. 45) is the rule that keeps the table finite.

## Calibration (must travel with the row)

- The book is **1940 functionalist ethnography of the Nuer**, written by a colonial-era
  anthropologist; tier A is scoped to *his assertions*, not to Nuer life today and not to
  pastoralists in general. The entry must not generalize "bovine idiom" into a law (the
  Herskovits "cattle complex" style universal is exactly the failure mode QUALITY criterion 2
  flags — and this row does not support it).
- EP himself marks the framing as an outsider's: "this obsession — for such it seems to an
  outsider" (p. 19) and "to Europeans the custom is the most striking evidence of the pastoral
  mentality of the Nuer" (p. 18). Quote those hedges if the entry uses the thesis strongly.
- The ten "principal colour terms" are **EP's English glosses** of Nuer terms (bor, car, lual,
  dol, yan, lou, thiang, lith, yil, gwir). Do not present the glosses as semantic primitives;
  `linguistics/color-terminology.md` owns that analysis (its one `pastoral` mention at `:63` is
  Welsh `glas`, unrelated — no overlap risk, but no support either).
- OCR in both scans mangles diacritics and some vowels; the quoted sentences above were read
  on page images, and the ten-term list was cross-checked across two independent scans. If the
  entry quotes individual Nuer terms, re-open the page image, not the text layer.

## Lesson material (for the round-50 scribe, not written here)

The frontier-step mistake candidate from this seat: **a registry URL must be the URL actually
opened.** The canonical host was recorded in `anchor` and in the report, never in the URL cell;
a row citing `archive.org/details/...` this round would be a source claim with no opening —
exactly the provenance failure QUALITY criterion 1 exists to catch, and the same failure shape
as an uncited registry row. L1 decides whether this belongs in `corpus/lessons/round-50.md`.

## Verification run / unrun

Run this session: `curl` reachability probes (archive.org 000 at 15–25 s; example.com 200;
wikipedia 301; web.archive.org 200; Wayback 403 + `x-nid` header); `curl` of the two PDFs
(HTTP 200, sizes above); `pdfinfo` on both; `pdftotext -layout` on both; `pdftoppm` pages 43
and 71 plus visual read; grep for "Interest in Cattle", "ten principal colour terms",
"social idiom", "history of each cow"; page mapping across PDF 38–80.

Unrun: the archive.org item page, BookReader, page images and `_djvu.txt` (host unreachable —
this is the standing gap in this report); no library print copy; no check of a 1937/1956
printing's pagination; no run of the lane sweep/README gates (out of this seat's scope); no
comparison against the entry's yet-unwritten bytes (the entry is absent at base).
