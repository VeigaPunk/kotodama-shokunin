# ReopenS052 — attack on SOURCES row S052 (Evans-Pritchard 1940, *The Nuer*)

Seat: `KotodamaR50-2.ReopenS052-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes read with `git -C … show <sha>:<path>`; the working tree was not used for any claim.

## Verdict

**PARTIAL.** Every substantive claim in the row holds: the URL opens, both quoted fragments are verbatim in
Chapter I §I and §VIII, the first printed anchor (`pp. 18–19`) is exact, tier A is honest for the row's
claim-scoped wording under `corpus/QUALITY.md` criterion 6, and all S052 citations in the knowledge entry are
supported by the pages read. **Two locator slips:** the row's parenthetical `(printed page = PDF page − 24)` is not
a constant offset (following it to the §VIII anchor lands on Plate V and printed pp. 37–40, not §VIII), and the
`§VIII pp. 41–46` range stops one page short of the section (it runs to p. 47). Both are one-line fixes in a
superseding row under the SOURCES append-only contract; no content or citation changes.

## Evidence

### 1. URL opened this session (row URL, not a re-derivation)

```
$ curl -sSIL --max-time 60 'https://people.duke.edu/~ldbaker/classes/gradtheory/Evans_Pritchard_E_E_The_Nuer_a_description_of_the_modes_1940.pdf'
HTTP/1.1 200 OK
Last-Modified: Tue, 06 Aug 2024 20:04:36 GMT
Content-Length: 17058687
Content-Type: application/pdf

$ sha256sum nuer.pdf
3bc19af66161e93b31c82ce3405d0a7e1c3bbaa052b5414300228f1856c36abd  nuer.pdf

$ pdfinfo nuer.pdf
Title:   The Nuer : a description of the modes of livelihood and political institutions of a Nilotic people
Author:  Evans-Pritchard, E. E. (Edward Evan), 1902-1973
Creator: Digitized by the Internet Archive
Keywords: http://www.archive.org/details/nuerdescriptiono00evan
Pages:   344
```

The artifact is the book named in the row, not a landing page. Its printed title page (extracted, PDF pp. 5–12)
reads `THE NUER / A DESCRIPTION OF THE MODES OF LIVELIHOOD AND POLITICAL INSTITUTIONS OF A NILOTIC PEOPLE /
BY E. E. EVANS-PRITCHARD … OXFORD / AT THE CLARENDON PRESS / 1940` — publisher and year in the row are exact.
The `Digitized by the Internet Archive` creator and the `archive.org/details/nuerdescriptiono00evan` keyword
support the row's "(Internet Archive-digitized scan)" provenance note.

### 2. Gate quote and first anchor — exact at printed p. 19

`corpus/lessons/round-50.md:37`:
> `S052 — <same URL> — accessed 2026-10-21 — Ch. I §I, p. 19: "Nuer tend to define all social processes and relationships in terms of cattle."`

PDF page 43 carries the printed running head `INTEREST IN CATTLE  19` and contains, above the section `II`
heading:

> "Nuer tend to define all social processes and relationships in terms of cattle. Their social idiom is a bovine idiom."

Confirmed twice: `pdftotext -f 43 -l 43` (OCR layer) and a 110-dpi render of that page (`pdftoppm -f 43 -l 43 -r 110 -png`)
read as an image. The OCR layer is reliable for this sentence; the page image shows the same words. §I is correct:
the `II` heading appears lower on the same page, so p. 19 is inside §I.

The row's broader first anchor `Ch. I §I pp. 18–19` is also honest: p. 18 (PDF 42) carries the lead-in
("…most of their social behaviour directly concerns their cattle…") and p. 19 carries the quoted sentence.

### 3. §VIII anchor — printed pp. 41–46 covers the cited content; the section runs to 47

- PDF page 71 = printed `41`, and `VIII` begins mid-page; the page image shows the heading directly above
  "Linguistic profusion in particular departments of life…".
- PDF page 76 = printed `46`; PDF page 77 = printed `47` still carries §VIII (the closing song verses, no new
  heading); §IX begins on printed `48` (PDF 78, line 36 = `IX`). So §VIII actually runs pp. 41–47, and the row's
  `pp. 41–46` understates it by the final song page. Nothing the entry cites sits on p. 47, so this is a
  one-page anchor imprecision, not a citation defect.
- The entry's second quote is verbatim at p. 41: "In naming a Nuer cow one has to notice **its colours and the way
  in which they are distributed on its body**." (OCR and page image agree.)
- The age/sex list is at p. 45 (PDF 75): "prefixes which denote the sex or age of an animal, e.g. `tut`, bull,
  `yang`, cow, `thak`, ox, `nac`, heifer, `math`, male calf, `dou`, female calf, `kol`, calf which has not yet begun
  to graze" — supports the entry's "bull, cow, ox, heifer and calf terms".

### 4. The one broken sentence: the PDF-page arithmetic

`corpus/SOURCES.md:81` ends the anchor with `(printed page = PDF page − 24)`. Measured against this exact file,
the offset is not constant:

| printed page (running head) | PDF page | implied offset |
|---|---|---|
| 19 | 43 | −24 |
| 23 | 49 | −26 |
| 33 | 61 | −28 |
| 37 | 67 | −30 |
| 41 | 71 | −30 |
| 46 | 76 | −30 |
| 47 | 77 | −30 |
| 48 | 78 | −30 |

The drift comes from inserted plate/figure leaves (e.g. PDF 47 = Plate III, 55 = Fig. 3 leaf, 57 = Plate IV,
60 = Fig. 4, 65 = Plate V, 72–73 = Figs. 8–9, 77 = plate leaf). The formula happens to be right for the Gate quote
(p. 19 = PDF 43) and wrong for the second anchor: `41 + 24 = 65`, and PDF 65–70 are:

```
$ pdftotext -f 65 -l 70 nuer.pdf - | head
PLATE V
Girl milking (Luu)
…
INTEREST IN CATTLE
37
…
```

```
$ pdftotext -f 65 -l 70 nuer.pdf - | grep -c 'VIII'
0
```

So a reader following the row's parenthetical lands five to six pages before §VIII, on a plate and printed
pp. 37–40. The section/page numbers themselves are right; only the conversion is false.

### 5. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md` criterion 6 reserves tier A for "sources primary or authoritative for the exact scope" and
downgrades publisher descriptions/abstracts to B. S052 is the book itself, and the row's scope is narrowed to
"Evans-Pritchard's own 1940 assertions about Nuer cattle idiom and cattle naming; not contemporary Nuer practice,
not a pastoral universal". That is exactly the authoritative relation: A is honest here, and the scope sentence
pre-empts the two over-readings the entry actually guards against. No criterion-6 downgrade applies.

The entry's own calibration is consistent, not confused with source tiers: entry line 175 defines the
`R/C/B/H/T` codes per `calibration-registry.md:35-39` (B = bounded), which is what line 106's "**B** to that
people and period" means — not tier B of SOURCES.

### 6. Every S052 citation in the knowledge entry

Repo-wide census at the landed commit (`git grep -n 'S052' <sha> -- corpus/ reports/ tools/`): the only lane
occurrences are `corpus/SOURCES.md:81`, `corpus/lessons/round-50.md:37`, and the S052 lines in
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (line 7 shelf-list mention, then five citing
sentences at 59, 75, 76, 106, 186). The SOURCES row's `used-by` (same entry) is complete and accurate; no other
entry cites the row.

| entry line | sentence | support in the opened pages |
|---|---|---|
| 7 | shelf list: "S052 Evans-Pritchard 1940 *The Nuer*" | name only; correct |
| 59 | "social idiom in Nilotic ethnography (S052) is regional, not a law" | p. 19 states the Nuer idiom; p. 41 extends the cattle *vocabulary* to "all the pastoral Nilotes"; the "regional, not a law" clause is the entry's calibration, and the sentence is scoped to Nilotic ethnography, not to herders generally. Supported with a hedge (see caveat b). |
| 75 | "Nuer cow names follow \"its colours and the way in which they are distributed on its body\" (S052, ch. I §VIII)" | verbatim fragment at p. 41; the original sentence is "In naming a Nuer cow one has to notice its colours and the way in which they are distributed on its body." |
| 76 | "Nuer separate bull, cow, ox, heifer and calf terms (S052)" | p. 45 prefix list (`tut`, `yang`, `thak`, `nac`, `math`, `dou`, `kol`) |
| 106 | "Evans-Pritchard wrote that \"Nuer tend to define all social processes and relationships in terms of cattle\" (S052): a 1940 outsider's functionalist claim, **B** to that people and period" | verbatim at p. 19; the outsider framing is EP's own ("for such it seems to an outsider", p. 19; "to Europeans the custom is…", p. 18); B = bounded per the entry's own code legend |
| 186 | "\"Nuer define everything through cattle\" generalises to herders — B — S052, one 1940 ethnography" | the generalisation is exactly what the row's scope excludes; calibration correct |

No entry sentence citing S052 overstates the source beyond the row's scope.

### 7. Secondary observations (non-breaking)

a. **"archive.org itself unreachable 2026-10-21"** is not reproducible as literally worded this session:
   `https://archive.org/details/nuerdescriptiono00evan` returned `200`, and the IA metadata API returns the item
   (`creator` Evans-Pritchard, `date` 1940, `publisher` "Oxford : Clarendon Press", `access-restricted-item:
   true`). The direct PDF derivative returned `401` because the item is lending-restricted — which is the real
   reason a mirror was needed. A dated observation of a transient outage would not be a defect by itself; the
   wording simply describes a restriction as unreachability, and a reader today sees a live details page. If a
   superseding row is written for the anchor fix, this clause should be reworded, e.g. "IA item access-restricted
   (lending), direct scan download 401; Duke course mirror used".

b. **Line 59's "Nilotic ethnography"** is a family-level noun for what S052 evidences at Nuer level. EP's own
   p. 41 sentence (vocabulary shared by "all the pastoral Nilotes") plus the Dinka cattle-names footnote (p. 41
   n. 1) make the family-level framing defensible, and the clause is a calibration hedge, not a factual
   generalisation. Recorded, not counted as a defect.

## Smallest fix

SOURCES is append-only (`corpus/SOURCES.md` header): only `status`, `recheck`, `used-by` change in place, and a
correction is a new row whose `teaches` opens `supersedes S0NN —`. The minimal compliant repair is one new row
(e.g. S070) that supersedes S052 with the anchor corrected and everything else unchanged:

> `Ch. I §I pp. 18–19; §VIII pp. 41–47. PDF mapping is not constant (inserted plate/figure leaves): p. 19 = PDF 43,
> p. 23 = PDF 49, p. 33 = PDF 61, pp. 37–47 = PDF 67–77, p. 48 = PDF 78; locate by the printed running head, not by
> arithmetic.`

No change to the entry, the Gate quote, the tier, the scope or `used-by` is warranted: those all verify.

## Housekeeping

No installs and no tool changes (host pacman paused; nothing needed — `pdftotext`/`pdfinfo`/`pdftoppm` were already
present). No lane files edited; no git/jj state, index, .ufo state or watchdog log touched. All work ran in
`/tmp/reopens052` on a copy of the public PDF; the directory (PDF, text extract, two page renders) was deleted
after this report was written.
