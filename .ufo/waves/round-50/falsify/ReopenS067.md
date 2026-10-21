# ReopenS067 — attack on SOURCES row S067 (Librado et al. 2021, *Nature*)

Seat: `KotodamaR50-2.ReopenS067-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below are read with `git show <sha>:<path>`; the working tree was not trusted.

## Verdict

**HOLDS.** The row URL opens (HTTP 200), the Gate quote is verbatim in the source's Abstract, row title/volume/
pages/DOI match the served article, tier A is honest for the row's explicitly abstract-scoped claim under
`corpus/QUALITY.md:29` (criterion 6), and every sentence in the knowledge entry that cites S067 is supported by
what I read. One non-breaking calibration-wording note (entry `:62` vs `:185`) and one abstract/main-text date
nuance are recorded at the end; no fix is required for the landed work.

## Evidence

### 1. URL opened this session

```
$ curl -sS -L -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ...' -o s067.html \
    -w 'HTTP %{http_code} final=%{url_effective} bytes=%{size_download}\n' \
    'https://www.nature.com/articles/s41586-021-04018-9'
HTTP 200 final=https://www.nature.com/articles/s41586-021-04018-9?error=cookies_not_supported&code=f4046692-e607-42bc-96ee-45f6b07eadf8 bytes=996837
```

The redirect is Nature's cookie-notice route; the served body is the article, not an error/landing page. Metadata in
the body:

```
citation_title            The origins and spread of domestic horses from the Western Eurasian steppes
citation_journal_title    Nature
citation_volume           598
citation_firstpage        634
citation_lastpage         640
citation_doi              10.1038/s41586-021-04018-9
citation_author (first)   Librado, Pablo
citation_publication_date 2021/10
```

This matches the row's `Librado et al. 2021 … Nature 598:634–640` and its URL exactly. The article is open access
(JSON-LD `license: http://creativecommons.org/licenses/by/4.0/`), so the abstract is not a paywall preview.

### 2. Gate quote is verbatim at the stated location

Gate bullet, `corpus/lessons/round-50.md:52`:

> S067 — https://www.nature.com/articles/s41586-021-04018-9 — accessed 2026-10-21 — Abstract: "modern domesticated breeds do not descend from the earliest domestic horse lineage associated with archaeological evidence of bridling, milking and corralling". Seat: ScoutCalibrationRegistry.

Source, `<div id="Abs1-content">` (the Abstract), rendered text:

> Domestication of horses fundamentally transformed long-range mobility and warfare. However, **modern domesticated breeds do not descend from the earliest domestic horse lineage associated with archaeological evidence of bridling, milking and corralling**^2,3,4 at Botai, Central Asia around 3500 bc.

```
$ python3 -c "... count in Abs1 raw ..."
quote-present-raw: 1
```

The quote is byte-contiguous in the abstract; the only difference from the raw page is the superscript reference
markers `2,3,4` that the quoting omits between "corralling" and "at Botai". Anchor "Abstract" is exact, access date
2026-10-21 is today, and the SOURCES preamble (`corpus/SOURCES.md:8`) names `lessons/round-50.md` for S048–S069 —
so the pointer is correct.

### 3. Row fields and `teaches` against the abstract

`corpus/SOURCES.md:96`:

| field | landed value | check |
|---|---|---|
| source | Librado et al. 2021, *The origins and spread of domestic horses from the Western Eurasian steppes*, Nature 598:634–640 — URL | matches metadata above |
| kind | paper | correct |
| tier | A | see §4 |
| scope | origins of modern domestic horses (DOM2) and the riding/Yamnaya question **as stated in the abstract** | see §4 |
| anchor | Abstract | exact |
| teaches | modern domestic horses do not descend from the Botai lineage; DOM2 spreads from the lower Volga-Don from about 2000 BC | supported below |
| status / opened / recheck / used-by | mined / 2026-10-21 / 365d / `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` | used-by accurate (§6) |

Abstract sentences backing `teaches`:

- **Botai non-descent**: the quoted sentence above, plus "Other longstanding candidate regions for horse
  domestication, such as Iberia and Anatolia, have also recently been challenged."
- **Lower Volga-Don homeland**: "Here we pinpoint the Western Eurasian steppes, especially the lower Volga-Don
  region, as the homeland of modern domestic horses."
- **≈2000 BC spread**: "modern domestic horses ultimately replaced almost all other local populations as they
  expanded rapidly across Eurasia from about 2000 bc, synchronously with equestrian material culture, including
  Sintashta spoke-wheeled chariots."
- **Riding/Yamnaya clause in `scope`**: "Our results reject the commonly held association between horseback riding
  and the massive expansion of Yamnaya steppe pastoralists into Europe around 3000 bc driving the spread of
  Indo-European languages." This sentence is in the same Abstract div (`Yamnaya` in abstract: True).

`DOM2` is not a word the abstract uses; the paper's main text names the cluster "DOM2" ("modern domestic horses
clustered within a group that became geographically widespread and prominent following about 2200 bc and during the
second millennium bc (DOM2)", and the Fig. 1 caption marks "the inferred homeland of DOM2 horses in the lower
Volga-Don region"). The row's scope parenthetical equates DOM2 with modern domestic horses, so the compression is
transparent. The main text's "following about 2200 bc" is a slightly earlier spread onset than the abstract's
"from about 2000 bc"; the row is explicitly abstract-scoped and uses the abstract's date, so this is a wording
nuance, not an unsupported claim.

### 4. Tier/scope honesty (QUALITY criterion 6)

`corpus/QUALITY.md:29`: "publisher descriptions and abstracts are tier B for **substantive claims about a work**,
even when accurate; reserve tier A for sources primary or authoritative for **the exact scope**."

The row does not use the abstract as a stand-in for the paper's full argument: its scope is literally
"origins of modern domestic horses (DOM2) and the riding/Yamnaya question **as stated in the abstract**", its anchor
is the Abstract, and its `teaches` are the abstract's own two findings (Botai non-descent; lower Volga-Don homeland
plus ≈2000 BC expansion). For that exact scope the abstract of the primary research paper is the paper's own
statement, i.e. authoritative for what it states; this is the claim-scoped use criterion 6 permits, not the S057
pattern (publisher description rated B). Tier A is honest. The entry uses no S067 claim that exists only in the
main text (the DOM2 label is used only to identify the lineage, and the spread date follows the abstract).

### 5. Every S067 citation in the knowledge entry

`git grep -n 'S067' <sha> -- corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` returns exactly
lines 7, 11, 62, 185, 195.

| line | text (abridged) | support |
|---|---|---|
| `:7` | external-shelf list: "S067 Librado et al. 2021 (domestic horse origins)" | bibliographic; title/date verified |
| `:11` | "re-open S050/S067 before quoting a domestication date (aDNA moves fast)" | procedural recheck; S067 is the 2021 aDNA paper, 365d cadence — consistent |
| `:62` | §4 Horse row: "modern domestic horses do not descend from the Botai lineage (S067): **C** on Botai-as-origin" | factual clause is exactly the abstract's finding; the C code is the lane's calibration of the broader Botai-as-origin claim (see note 1) |
| `:185` | §13: "Botai horses are the ancestors of domestic horses \| C → R for modern horses — S067 \| treat early horse use and modern horse origins as different questions" | R for modern horses is exactly the abstract (modern breeds do not descend from the Botai lineage); "early horse use ≠ modern origins" is the abstract's own contrast between Botai bridling/milking/corralling evidence and the DOM2 origin; supported |
| `:195` | §14 recheck: "re-open S050 and S067 before quoting a date" | procedural; consistent with the row's 365d recheck and aDNA volatility |

No entry sentence cites S067 for a proposition the abstract does not carry.

### 6. Registry consistency

```
$ git grep -l 'S067' <sha> -- .
…:corpus/SOURCES.md
…:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
…:corpus/lessons/round-50.md
```

Only the registry row, the Gate lesson and the entry cite S067 in landed corpus bytes; `used-by` names the entry.
The C acceptance command in `reports/round-50/separability/r50-manifest.json` (S-id → SOURCES row whose 11th field
contains the entry path) would resolve S067: the row's used-by field is exactly that path. The build scratch
`.ufo/waves/round-50/build/ScoutCalibrationRegistry.md` still labels the paper "S055?"/"S055" — already flagged in
`ReopenS055.md` caveat 3; it is not a corpus citation and does not collide with landed S067.

## Non-breaking notes

1. **Calibration wording at `:62` vs `:185`.** The §4 table says "**C** on Botai-as-origin" while §13 says
   "C → R for modern horses". Both are defensible with the calibration-registry codes (`C` = contested
   interpretation, `R` = rejected as the specified general inference): `C` attaches to the broad
   "Botai-as-origin" proposition, `R` to its modern-horse scoping. If the author wants the table to read as
   precisely as the bank, the smallest alignment is "**C → R** for modern horses on Botai-as-origin". No source
   support is missing either way.
2. **Abstract vs main-text date.** The abstract says expansion "from about 2000 bc"; the main text says the DOM2
   cluster became widespread "following about 2200 bc". The row is abstract-scoped and quotes 2000 BC; no defect,
   but a later writer quoting the main text should not silently reuse 2000 BC as the main-text date.

## Smallest fix

None required: the URL, quote, location, tier/scope and every entry citation hold. Optional (not needed for
admission): align entry `:62`'s calibration code with `:185` ("C → R for modern horses").

## Cost / cleanliness

No installs, no clone, no lane edits, no git/jj state touched. One 996 KB HTML fetch in `/tmp`, deleted after
extraction. Only this report was written.
