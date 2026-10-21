# ReopenS051 — attack on SOURCES row S051 (Marciniak 2011)

Seat: `KotodamaR50-2.ReopenS051-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below read with `git show <sha>:<path>`; the working tree was not used for any landed claim.

## Verdict

**HOLDS.** The URL opens this session, the Gate quote is a verbatim substring of the abstract's opening
sentence, `B` is honest for the row's scope under `corpus/QUALITY.md` criterion 6, and all three `S051`
citations in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` are supported by the
article. No fix is required. Three non-breaking precision caveats are recorded at the end.

## Evidence

### 1. Row and Gate bytes

`corpus/SOURCES.md:80` (11 columns parsed against the header):

```
| S051 | Marciniak 2011, The Secondary Products Revolution: Empirical Evidence and its Current Zooarchaeological Critique, Journal of World Prehistory 24(2):117–130 — https://link.springer.com/article/10.1007/s10963-011-9045-7 | paper | B | what Sherratt's secondary-products thesis claims and this review's three-region critique (Central Anatolia, Balkans, North European Plain); not primary for Sherratt | Abstract; Introduction ¶1–2; Discussion and Conclusions ¶1 | milk, wool, textiles and traction as secondary products; adoption idiosyncratic and not tied to one century or millennium | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

`corpus/lessons/round-50.md:36`:

```
- S051 — https://link.springer.com/article/10.1007/s10963-011-9045-7 — accessed 2026-10-21 — Abstract, opening sentence: "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction". Seat: SrcSherratt.
```

The row is new at the landed commit: `git show 4ad2683:corpus/SOURCES.md | grep -c S051` → `0`;
`git diff --stat 4ad2683 1c779e4 -- corpus/SOURCES.md` → `25 insertions(+), 1 deletion(-)`.

### 2. URL opened this session (2026-10-21), route recorded

Direct `curl` to the exact URL returns HTTP 200 but only Springer's JavaScript bot challenge
(`Client Challenge`, 3,038 bytes, no article text). A real Chromium session passes it:

```
URL: https://link.springer.com/article/10.1007/s10963-011-9045-7
HTTP: 200 (performance navigation responseStatus)
Title: The Secondary Products Revolution: Empirical Evidence and its Current Zooarchaeological Critique | Journal of World Prehistory | Springer Nature Link
readyState: complete; canonical == the row URL; page text 49,581 chars
Page says: "Open access", "Published: 01 June 2011", "Volume 24, pages 117–130 (2011)"
```

So the URL is reachable for a browser; the curl challenge is a route caveat, not an unreachable-URL
finding. No login used.

### 3. Gate quote is verbatim at the stated location

Live abstract (`document.querySelector('.c-article-section__content p').innerText`, 690 chars), sentence 1:

> Andrew Sherratt is perhaps best known for the concept of a ‘Secondary Products Revolution’, which stressed that the ‘primary’ pattern of exploiting domesticated animals for meat in the Early Neolithic was followed by a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction.

Machine checks:

```
q1 = "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction"
q1 in abstract: True
q1 in abstract first sentence: True
Gate quote == entry quote: True
```

It is a 16-word contiguous substring starting after “followed by”; the fragment begins lowercase, so the
mid-sentence cut is signalled. “Abstract, opening sentence” is accurate. The quote also appears verbatim in
the OpenAlex abstract for DOI `10.1007/s10963-011-9045-7`, an independent witness.

### 4. Bibliographic cells match the publisher

`citation_*` metadata on the live page vs the row:

| field | live page | row | match |
|---|---|---|---|
| title | The Secondary Products Revolution: Empirical Evidence and its Current Zooarchaeological Critique | same | yes |
| journal | Journal of World Prehistory | same | yes |
| volume / issue / pages | 24 / 2 / 117–130 | 24(2):117–130 | yes |
| DOI | 10.1007/s10963-011-9045-7 | same | yes |
| author / date | Arkadiusz Marciniak; online 2011-06-01, issue 2011/09 | Marciniak 2011 | yes |
| access | open access (Unpaywall: hybrid, CC BY-NC) | no paywall claim | consistent |

Crossref returns `issue: "2-3"` for the aggregate; the publisher's own `citation_issue` is `2`, which the
row follows. See caveat C1.

### 5. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29` (criterion 6): “publisher descriptions and abstracts are tier B for substantive
claims about a work, even when accurate; reserve tier A for sources primary or authoritative for the exact
scope.”

The row is `B`, its scope is “what Sherratt's secondary-products thesis claims and this review's three-region
critique …; not primary for Sherratt”, and its first anchor is the abstract. That is exactly the criterion-6
posture: the article is a peer-reviewed review *reporting* Sherratt, not Sherratt 1981/1983, so it cannot be
A for what the thesis says. The `SOURCES.md:14-21` tier definitions agree (`B` = strong secondary).

The scope's three regions are the article's own three H3 critique sections, read in DOM order:

```
Central Anatolia
The Central Balkans
The North European Plain
```

The row's “Balkans” abbreviates “The Central Balkans”; not misleading. The scope's disclaimer (“not primary
for Sherratt”) is honest and matches the build seat's anti-laundering note.

### 6. Every `S051` citation in the entry is supported

`grep -n S051 corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` → lines **7, 93, 183** only.

**Line 7** — external-shelf list: “S051 Marciniak 2011 (secondary-products critique)”. The article's title
ends “and its Current Zooarchaeological Critique”; supported.

**Line 93** — “Sherratt's "secondary products revolution" — "a more diversified exploitation of secondary
applications and products such as milk, wool, textiles, and traction" (S051) — is **C**: the review finds
adoption regional and staged, not one horizon (S051). Write product sequences per region.”

- Quote: byte-identical to the Gate quote and to the live abstract (checked above).
- “regional and staged, not one horizon”: the article's Discussion and Conclusions ¶1 (the row's third
  anchor) says, verbatim:

  > Considering the wide span of the Neolithic dispersal across Anatolia and Europe, the changes that might be linked with the Secondary Products Revolution are by no means associated with a single century or millennium. On the contrary, they emerged in different periods, ranging from the second half of the seventh millennium cal BC in Central Anatolia to the first half of the fourth millennium cal BC in the Central Balkans and in the North European Plain.

  Same paragraph: “Parallel developments by no means imply any kind of universal rule or pattern.” The
  abstract adds “the idiosyncratic nature of the introduction of secondary products in particular areas of
  Anatolia and Europe.” Different regions + different periods + explicit rejection of a single century or
  millennium supports “regional and staged, not one horizon”; “staged” is a fair gloss on “emerged in
  different periods”, not a quotation.
- The entry's `C` here is the calibration code “contested”, not a source tier:
  `pastoralism-animal-husbandry.md:175` — “Codes per `calibration-registry.md:35-39` (R rejected, C
  contested, B bounded, H heuristic, T to-verify).”

**Line 183** — decision table: “Sherratt's secondary products arrived as one revolution | C — S051 |
regional, staged product sequences”. Same support; the review's own conclusion is that the change was
“clearly more complex than Sherratt suggests (1981, 1983)” and that the evidence “challenges a meat-based,
livestock-rearing system for early farmers”. The corrective column is the review's regional, period-specific
finding. Supported.

No other corpus/tool/README file cites S051:

```
$ grep -rn 'S051' <landed tree>/corpus /tools /README.md
corpus/SOURCES.md:80
corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:7,93,183
corpus/lessons/round-50.md:36
```

`used-by` therefore names the only citing knowledge path, and `status: mined` is correct.

### 7. Build-seat record is consistent

`.ufo/waves/round-50/build/SrcSherratt.md` (seat `ChousaR27R2.SrcSherratt-4`) records the same 16-word
abstract quote, the same “Abstract, first (opening) sentence” location, the same tier-B reasoning against
criterion 6, the same three anchor groups, and the Discussion ¶1 timing sentence. Its proposed row was
S048 before integrator renumbering; the landed S051 is the same candidate, renumbered. This is a consistency
check only, not independent proof.

## Non-breaking precision caveats

- **C1 — issue number.** Crossref lists the volume as `24(2-3)`; the publisher's article metadata lists
  `citation_issue: 2`, and the row says `24(2)`. The row follows the publisher's own record. Not a defect;
  a superseding row is not warranted. If a future editor prefers Crossref's aggregate, that is a new-row
  correction, not an in-place edit.
- **C2 — “secondary products” vs “applications”.** The row's `teaches` lists “milk, wool, textiles and
  traction as secondary products”. The Introduction distinguishes “secondary products, such as milk, wool
  and textiles, and applications, such as traction power or transport”. The abstract's umbrella phrase is
  “secondary applications and products”, which covers all four, and the entry's table keeps traction in its
  own “Traction and carrying” row. A compression, not a misstatement; no change needed.
- **C3 — route.** Direct curl gets Springer's JS challenge (HTTP 200, 3,038 bytes); a real browser gets the
  full open-access article. The Gate's “accessed 2026-10-21” is true via browser, and I re-opened it the same
  day. The build seat's report claims a “native fetch”; my curl could not reproduce that route, but the row
  is about the source, not the fetch method.

## Smallest fix

None required. The row, its Gate bullet, its tier/scope, and its three entry citations all hold against the
live article and the landed bytes.

## Bounds and tooling

- No lane file written except this report; no `git add/commit/stash/checkout/reset`, no jj command, no
  touching of `.ufo/state`, `MANIFEST.json`, the fleet repo, or sibling lanes.
- No packages installed; pacman/uv/cargo/npm untouched.
- Temporary evidence kept under `/tmp` only and removed after the checks (`/tmp/s051*`, `/tmp/s051tree`).
- Remaining unknowns: whether the article's regional conclusions have been superseded since 2011 (the row's
  365d recheck covers this); Crossref's `2-3` aggregate is untested against a physical issue wrapper.
