# ReopenS055 — attack on SOURCES row S055 (Ostrom 2009 Nobel lecture)

Seat: `KotodamaR50-2.ReopenS055-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below read with `git show <sha>:<path>`; working tree not trusted (it currently has an unrelated
`M reports/round-50/run-validation.py`).

## Verdict

**HOLDS.** The URL opens, the Gate quote is verbatim at the stated section and PDF page, tier A is honest for the
row's stated scope under `corpus/QUALITY.md` criterion 6, and every sentence in the knowledge entry that cites
S055 is supported by the source. Three non-breaking notes (two precision caveats and one build-scratch bookkeeping
observation) are recorded at the end; no fix is required for the landed work.

## Evidence

### 1. URL opened this session

```
$ curl -sS -L -o ostrom_lecture.pdf -w 'HTTP %{http_code} size=%{size_download} type=%{content_type}\n' \
    https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf
HTTP 200 size=2428710 type=application/pdf
$ sha256sum ostrom_lecture.pdf
5d11eb59b78e94bef479e66216078231dc803aa9bedd907314a96aba0e53c5f1
$ pdfinfo ostrom_lecture.pdf
Title:    Prize Lecture by Elinor Ostrom
Subject:  Beyond Markets and States: Polycentric Governance of Complex Economic Systems
Author:   Elinor Ostrom
Pages:    37
```

The fetched artifact is the named lecture, not a landing page or a different upload. `corpus/SOURCES.md:84` and
`corpus/lessons/round-50.md:40` use this exact URL; access date 2026-10-21 matches today.

### 2. Anchor location is exact

Extraction: `pdftotext -layout ostrom_lecture.pdf ostrom.txt`. Section headings in the extraction:

- `412: 4. Are Rational Individuals Helplessly Trapped in Social Dilemmas?`
- `644: E. Long-Surviving Resource Institutions`
- `718: 5. Conducting Experiments to Study Common-Pool Resource Problems`

So `§4E` in the row and Gate is correct (subsection E of section 4, not section 5). A per-page search puts the
anchor sentence on **PDF page 15**; the printed footer on that page is **422** (PDF p. 14 is printed 421). The row
says "PDF p. 15", which matches the PDF's own page index; it does not confuse printed page with PDF page.

```
$ for p in $(seq 10 20); do pdftotext -f $p -l $p -layout ostrom_lecture.pdf - | grep -q 'design principles appear' \
    && echo "FOUND on PDF page $p"; done
FOUND on PDF page 15
```

### 3. Gate quote is verbatim

Gate bullet, `corpus/lessons/round-50.md:40`:

> S055 — https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf — accessed 2026-10-21 — §4E Long-Surviving Resource Institutions, PDF p. 15: "The design principles appear to synthesize core factors that affect the probability of long-term survival of an institution developed by the users of a resource." Seat: SrcOstrom.

Character-level check against the de-hyphenated PDF text:

```
EXACT_MATCH: True
... 8. Nested Enterprises: ... multiple nested layers. The design principles appear to synthesize core factors
that affect the probability of long-term survival of an institution developed by the users of a resource. Cox,
Arnold, and Villamayor-Tomás (2009) analyzed over 100 studies ...
```

The only PDF line breaks inside the sentence are `prob-` / `ability` and `re-` / `source`; after normal PDF
de-hyphenation the sentence is byte-identical to the Gate quote, including the final period. The paragraph is the
first paragraph after the numbered principles 1A–8, as the build seat's report also recorded.

### 4. Row fields

`corpus/SOURCES.md:84` (header at `:28`: `id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`):

- **source**: title, lecture occasion and date match the PDF title page ("Prize Lecture, December 8, 2009 by Elinor Ostrom").
- **kind**: `paper` — acceptable for the published lecture text.
- **tier A**: primary source for Ostrom's own 2009 statement. Not a publisher description; cf. criterion 6's
  S034/S038/S039 → S044–S046 pattern, which this is not.
- **scope**: "Ostrom's own 2009 formulation of the design principles and the critique of the helpless-users
  presumption; not the 1990 book's wording" — the second clause is honest: the lecture itself says the principles
  are "described extensively in E. Ostrom (1990, 2005)" and lists an updated formulation. The helpless-users critique
  is present in the source: §4 is titled "Are Rational Individuals Helplessly Trapped in Social Dilemmas?" and the
  text calls the trapped-agent assumption "a retrogressive step" (extraction lines 412–431); §7 concludes "one can
  move beyond the presumption that rational individuals are helpless in overcoming social dilemma situations"
  (line 1159).
- **teaches** ("resource users can build long-surviving institutions; design principles as diagnostic, not a
  predictive law"): supported. The source sentence is explicitly probabilistic ("affect the probability of
  long-term survival"), and the same section records that some studies found the principles inadequate, that
  authors interpreted them "very rigidly", and that three principles were reworded (extraction lines 697–712).
- **status** `mined` with **used-by** naming the entry: the path exists and cites S055.
- **opened** 2026-10-21 / **recheck** 365d: consistent with this round's Gate.

### 5. Every S055 citation in the knowledge entry

`git grep -n 'S055' 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0 -- .` returns one SOURCES row, one Gate bullet, six lines of
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, and two build-scratch lines under
`.ufo/waves/round-50/build/` (see caveat 3). The entry's six:

| line | text (abridged) | support |
|---|---|---|
| `:7` | "S055 Ostrom 2009 Nobel lecture" in the external-shelf list | bibliographic only; title/date correct |
| `:11` | "re-open S054 and S055 together before writing a commons rule" | procedural; S055 is the 2009 lecture, S054 Hardin 1968 — both opened |
| `:115` | §8 table: "design principles for long-surviving institutions \"developed by the users of a resource\" (S055)"; status "mainstream as diagnosis; C as a predictive law"; design use "rotas, fines, monitors and nested authority" | fragment is an exact substring of the source sentence; monitoring = principles 4A/4B, nested authority = principle 8; "C as a predictive law" is the lane's calibration of use, not a claim about the source |
| `:171` | §12 NON-CANON Ketrun: "a fine for grazing out of turn (Ostrom-style, S055)" | design application of principle 5 (graduated sanctions: "start very low but become stronger if a user repeatedly violates a rule") + principle 4A; the paragraph is explicitly NON-CANON, so no ethnographic fact is asserted |
| `:182` | §13: "Hardin's tragedy describes pastoral commons — R as universal; B for unmanaged open access — S054 vs S055" / "choose the rule set first: open access, group, state or private" | S055 supplies both the Hardin/helpless-users correction (extraction 453–459) and the property-regime set: "A common-pool resource can be owned and managed as government property, private property, community property, or owned by no one (Bromley 1986)" (extraction 562–563). "group" is the entry's compression of "community property"; "open access" of "owned by no one" |
| `:195` | §14 recheck: "open Herskovits 1926 and Ostrom 1990 before quoting them (only S053 and S055 are opened)" | accurate: S055 is the 2009 lecture and the row's scope explicitly excludes the 1990 book's wording; S053 is Eczet 2020, which only attributes Herskovits 1926 |

No entry sentence cites S055 for a proposition the lecture does not carry. The entry does not quote the numbered
1A–8 list itself, so the attribution nuance below has no landed consequence today.

### 6. Tier/scope honesty (QUALITY criterion 6)

Criterion 6 reserves tier A for sources "primary or authoritative for the exact scope" and warns against
publisher descriptions. S055 is the authored lecture text published by the Nobel Foundation, the awarding body:
primary for what Ostrom said in 2009, and the row bounds it away from the 1990 book, from pastoral ethnography and
from post-2009 literature. The row's use for a pastoral-commons rule is grounded in the lecture's own Hardin
passage ("a pasture open to all", extraction 453–454) and its listing of "pastoralists" among CPR users
(extraction 663), not in an unsupported extension. Tier A is honest.

## Caveats (non-breaking)

1. **Scope omits the list's attribution.** The numbered 1A–8 list in §4E is introduced as "a brief updated list as
   developed by Cox, Arnold, and Villamayor-Tomás (2009)"; Ostrom adopts and presents it but
   did not author that wording (extraction lines 668–669). The build seat's candidate row said so ("updated list
   as developed by Cox, Arnold and Villamayor-Tomás 2009"); the landed `corpus/SOURCES.md:84` drops it. Because the entry quotes only Ostrom's
   own synthesis sentence, no landed sentence is unsupported. If a later writer quotes principles 1A–8 from S055,
   attribute the updated list or cite Cox et al. directly. Per the SOURCES preamble, a scope correction would be a
   superseding row, not an in-place edit; no change is needed this round.

2. **§13 four-way compression.** "open access, group, state or private" is a faithful paraphrase of Ostrom's
   "government property, private property, community property, or owned by no one (Bromley 1986)", but "group" is
   the entry's word, not the source's. It is presented as design guidance, not a quotation; acceptable.

3. **Stale provisional id in build scratch.** `.ufo/waves/round-50/build/ScoutCalibrationRegistry.md:95` and
   `:107` label the Librado et al. 2021 *Nature* horse paper "S055?"/"S055". That paper landed as `S067`
   (`corpus/SOURCES.md:96`). This is build-report bookkeeping, not a corpus citation; the final registry has one
   S055 (Ostrom) and one S067 (Librado), so there is no collision in landed corpus bytes. Flagged only because a
   naive `git grep S055` on the commit will surface it.

## Smallest fix

None required. If the lane wants caveat 1 closed, add a superseding row whose `teaches` begins `supersedes S055 —`
with the Cox et al. attribution in its scope, or leave the nuance to the next round's lesson; do not edit S055's
scope in place (SOURCES preamble append-only rule).

## Cost / cleanliness

No clone created (per-page `git show` was sufficient; no reproduction needed). One 2.43 MB PDF downloaded to `/tmp`
and deleted after extraction. No installs, no lane file edits, no git/jj state touched. Only this report written.
