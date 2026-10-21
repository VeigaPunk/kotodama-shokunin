# ReopenS049 — attack on SOURCES row S049 (FAO 2001, Social institutions chapter)

Seat: `KotodamaR50-2.ReopenS049-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes were read with `git show <sha>:<path>`; the working tree was not trusted for landed claims.

## Verdict

**PARTIAL.** The row, its URL, its Gate quote, its stated location, and its tier/scope hold. Four of the five
S049 citations in the entry are supported. The fifth, the §11 build-order row at
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:155`, asserts a herd ceiling "set by labour
**and disease**"; the cited chapter contains no occurrence of "disease", §7 (the other cited pointer) does not
either, and no other source is cited on that row. That is an unsourced factual factor under
`corpus/QUALITY.md` criterion 1, which requires unverified claims to be marked `(to-verify)` rather than
asserted. Smallest fix: one-word deletion ("and disease" → nothing) or mark it `(to-verify)`.

## Evidence

### 1. URL opened this session

```
$ curl -sSL -o s049.html -w 'HTTP %{http_code} final=%{url_effective} bytes=%{size_download}\n' \
    'https://www.fao.org/4/y2647e/y2647e08.htm'
HTTP 200 final=https://www.fao.org/4/y2647e/y2647e08.htm bytes=9888
$ sha256sum s049.html
ea278a3a5bc1c6538a3a1f9bb1dbe72b47bc2d3bcc027d707f5c3e851ce6060a  s049.html
```

No redirect, no login, no bot wall. The fetched page identifies itself as
`<title>Pastoralism in the new millennium</title>`; the document's TOC page (`y2647e00.htm`, HTTP 200) shows
`© FAO 2001`, `ANIMAL PRODUCTION AND HEALTH PAPER 150`, and the chapter `SOCIAL AND CULTURAL INSTITUTIONS OF
PASTORALISM` with exactly four subsections: `Social structures`, `Role of women in pastoral society`,
`Pastoral identities`, `Land tenure and the common property resources debate` — the chapter the row names.
The access date in the row and the Gate, 2026-10-21, is today.

### 2. Gate quote is verbatim at the stated location

`corpus/lessons/round-50.md:34`:

> S049 — https://www.fao.org/4/y2647e/y2647e08.htm — accessed 2026-10-21 — §Land tenure and the common property
> resources debate: "Tenure is thus divided by both ecology and the potential for agriculture." Grounds §8 and the
> labour-wealth link (§Social structures). Seat: ScribeSec11Decision; integrator re-fetch.

The page's heading is `<h2><a name="P20_5707"></a><b>LAND TENURE AND THE COMMON PROPERTY RESOURCES DEBATE</b></h2>`
(HTML offset 6866, anchor `P20_5707` — the same anchor the TOC links for that subsection). The quoted sentence is
the first sentence of the next paragraph (offset 8177). A whitespace-normalised exact search finds it **once**:

```
exact quote count: 1
gate fragment match: True
... its own political constituency. Tenure is thus divided by both ecology and the potential for agriculture. In much o ...
```

Entry use, `pastoralism-animal-husbandry.md:110`, quotes the predicate exactly (period outside the quote):

> Tenure "is thus divided by both ecology and the potential for agriculture" (S049).

The Gate's second ground, "the labour-wealth link (§Social structures)", is also on the page, in
`SOCIAL STRUCTURES` (H2 anchor `P2_47`): "A key aspect of pastoral systems is the strong relationship between
wealth in livestock and labour. Herds that grow beyond a certain size cannot be managed with household labour
alone, and outside herders must be sought."

### 3. Tier and scope under QUALITY criterion 6

`corpus/SOURCES.md:78` files the row as `docs`, tier **B**, scope "social structure and pastoral land tenure as
summarised for policy; not primary ethnography". That is honest: the chapter is a FAO policy synthesis whose
evidence is cited secondary literature (Khazanov 1984, Legesse 1982, Peters 1990, Olesen 1994), not primary
ethnography, and the scope excludes exactly what it does not carry. Tier A would be wrong; tier C would
understate a full-text survey. This is not the criterion-6 failure pattern (publisher description/abstract
promoted to A).

### 4. Row mechanics

`corpus/SOURCES.md:78` matches the 11-column header at `:28`
(`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`):

- source: FAO, title, year, "Social institutions chapter" — verified against the TOC (`© FAO 2001`, H1 above).
- kind `docs`, tier `B` — valid and honest.
- anchor: the two H2s that carry the row's claims exist on the page; both were read.
- teaches: "herd wealth tracks household labour" — supported by the Social-structures passage above;
  "tenure is divided by ecology and the potential for agriculture" — verbatim sentence; third clause caveated
  below.
- status `mined`, opened `2026-10-21`, recheck `365d`, used-by
  `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` — the path exists at the landed commit and
  cites S049. The C claim's mechanical requirement ("every cited S-id resolves to a SOURCES row whose used-by
  names the entry") passes for this id.

### 5. Every S049 citation in the entry

`git show <sha>:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | grep -n 'S049'` returns
`:7, :22, :102, :110, :155`.

| line | text (abridged) | support |
|---|---|---|
| `:7` | external-shelf list: "S049 same, social institutions and tenure" | bibliographic; correct title/scope |
| `:22` | §1 test "Labour-capped herd — household labour, not pasture alone, sets the herd a family can hold (S049)" | supported by the Social-structures labour passage: herds beyond a size "cannot be managed with household labour alone" |
| `:102` | §7 loan table: "a loan network is insurance and alliance at once `(to-verify)`: herd wealth tracks household labour (S049)" | the S049-bearing clause is the labour-wealth relation, supported; the loan/insurance claim is honestly flagged `(to-verify)` |
| `:110` | §8: "Tenure \"is thus divided by both ecology and the potential for agriculture\" (S049)" | exact substring of the source sentence |
| `:155` | §11 step 5: "herd ceiling set by labour and disease; loan and gift networks \| §7; S049" | **labour supported; "disease" unsupported** — see defect |

### 6. The one unsupported clause (defect)

```
$ grep -c -i 'disease' s049.html
0
$ git show <sha>:...:pastoralism-animal-husbandry.md | grep -n -i 'disease'
155:| 5 | Wealth | herd ceiling set by labour and disease; loan and gift networks | §7; S049 |
$ git show <sha>:... | sed -n '96,106p' | grep -n -i 'disease\|ceiling'
(no output)
```

- The cited chapter has zero occurrences of "disease" (full 1,319-word text extracted and read; all four sections).
- §7, the row's other Check pointer, has no "disease" and no "ceiling" (lines 96–106).
- The word occurs nowhere else in the entry, so no other citation rescues it.
- The entry's own §13 replacement advice (`:181`) says "herd size answers labour, risk and tenure" — not disease.
- Under `corpus/QUALITY.md` criterion 1 ("every factual claim carries a cited, checkable source … marked
  `(to-verify)` inline — never laundered into assertion"), an asserted factor with no source is a provenance gap.

**Smallest fix:** at `:155` delete "and disease" → `herd ceiling set by labour; loan and gift networks`
(Check stays `§7; S049`), or keep the factor and mark it `` `(to-verify)` ``. If the lane wants disease sourced,
the same FAO report has an `ANIMAL HEALTH` chapter at `https://www.fao.org/4/y2647e/y2647e05.htm` (TOC listing
only — not opened here); it would need its own registered row, because S049's scope is social structure/tenure,
not animal health. S048's chapter (the report's Introduction) mentions disease only as a movement trigger and a
cause of losses, not as a herd ceiling, so adding S048 to the Check cell would not cleanly close the gap either.
Do not widen S049's scope in place (SOURCES is append-only; a correction is a superseding row).

## Caveats (non-breaking)

1. **Row's `teaches` third clause over-adjudicates.** "pastoral tenure is a common-property debate, not open
   access" — the page says pastoral systems are "at the heart of many debates on the nature of common property
   resources", calls pastoral tenure "fluid systems that are hard to pin down", and notes farmers "can come and
   cultivate the land that herders regularly use for grazing their stock, without having to ask for permission".
   The phrase "not open access" is not in the chapter and the weak-external-exclusion sentence points the other
   way; "common-property debate" is literal. No entry sentence repeats the clause (the §8 Hardin/open-access
   calibration is cited to S054 vs S055), so this is registry wording, not an admitted claim. If corrected, use a
   superseding row per the append-only rule.
2. **Hired labour is placed only at the ranch boundary.** S049 documents hired labour and, formerly, slavery or
   vassal castes as how pastoral herds grow beyond household-labour capacity; the entry's §3 maps "hired
   stockmen" only to the enclosed/ranching row and `:22`'s fail cell reads "enclosed ranching with wage herders".
   The fail cell's referent is §3's enclosed row, so the pass condition is not wrong, but a future revision
   should not read S049 as saying wage herding is outside pastoralism.
3. **Provisional-id collisions in build scratch only.** A naive `git grep S049` on the commit also hits
   `.ufo/waves/round-50/build/` reports that had proposed S049 for other candidates before L1 assigned ids:
   `ScoutCalibrationRegistry.md:89` (FAO `y2647e10.htm`, environment chapter), `SrcHardin.md:55,:65` (Hardin),
   `SrcHerskovits.md:59,:69` (Eczet), `SrcMongolFiveSnouts.md:37,:49` (Chuluunbaatar), `SrcAndeanCamelids.md:20`
   (O'Hare et al.), `SrcFaoPastoralism.md:81` (FAO Pastoralist Knowledge Hub). These are wave bookkeeping, not
   corpus citations; the landed registry contains exactly one S049 (`corpus/SOURCES.md:78`) and the entry cites
   that id only, so there is no collision in landed corpus bytes. Flagged only so a reviewer grepping the commit
   does not mistake a scratch proposal for the landed row.

## Remaining unknowns

- The report's `ANIMAL HEALTH` chapter (`y2647e05.htm`) was not opened, so I cannot say the wider FAO document
  never supports "disease" as a herd-ceiling factor — only that the cited chapter (S049) and the entry's cited
  §7 do not.
- Public HTTP only; no live-session/login probing. Other S048–S069 rows were not audited by this seat.

## Cost / cleanliness

No clone created; no reproduction needed. Temp artifacts (`/tmp/s049.html`, `s049toc.html`, `s049next.html`,
`s048.html`) deleted after evidence capture. No installs, no pacman transactions (host paused), no lane edits
other than this report; no git/jj state touched. Tools used: curl 8.23.0, Python 3.14.8, coreutils/grep.
