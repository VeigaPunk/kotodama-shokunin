# ReopenS066 — attack on SOURCES row S066 (D-PLACE EA004, animal-husbandry dependence)

Seat: `KotodamaR50-2.ReopenS066-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below were read with `git show <sha>:<path>`; the working tree was not trusted. No lane edits,
no git/jj writes, no installs.

## Verdict

**HOLDS.** The URL opens (HTTP 200, same route), the Gate quote is verbatim at the stated Description location,
tier A is honest for the row's narrow "code definitions and value counts in the edition served 2026-10-21" scope
under `corpus/QUALITY.md:29` (criterion 6), and the only substantive S066 citation in the entry
(`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:25`) is supported by the page's Values table:
12 of 1,290 coded societies at 86–100% dependence (0.93%; 27/1,290 = 2.09% at ≥76%; 39/1,290 = 3.02% at ≥66%).
Two non-blocking observations are recorded below: the Gate bullet does not itself carry the Values-table counts
its `teaches` quantifier rests on (the row anchor names the table and the page shows it; S042's precedent quotes
them), and the row's `recheck` is 365d where the same dataset's S042 and the seat's own recommendation use
`on-release`. Neither changes the truth of the row or of the entry sentence.

## Evidence

### 1. URL opened this session

Row URL: `https://d-place.org/parameters/EA004` (`corpus/SOURCES.md:95`).

```
$ curl -sSI -L 'https://d-place.org/parameters/EA004'
HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 16:36:31 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 59660
Server: gunicorn
Vary: Accept
Link: <https://d-place.org/parameters/EA004.json>; rel="alternate"; type="application/json"
Link: <https://d-place.org/parameters/EA004.rdf>; rel="alternate"; type="application/rdf+xml"
...
```

No redirect (minimal `curl -L` final URL is identical), no login, no CAPTCHA. The page is the variable page:
`<h2>Subsistence economy: animal husbandry [EA004]</h2>`.

The machine-readable alternate independently carries the exact description:

```
$ curl -sS -L -o ea004.json -w 'HTTP %{http_code} bytes=%{size_download} ct=%{content_type}\n' \
    'https://d-place.org/parameters/EA004.json'
HTTP 200 bytes=297 ct=application/json
{"pk": 1017, "type": "Ordinal", "dataset_pk": 5, ..., "id": "EA004",
 "name": "Subsistence economy: animal husbandry [EA004]",
 "description": "Dependence on animal husbandry, relative to other subsistence activities.", ...}
```

**Quote check.** `grep -c -F 'Dependence on animal husbandry, relative to other subsistence activities.'`
on the fetched HTML → **2**. Raw HTML contexts:

```html
<p class="large"><strong>Description:</strong> Dependence on animal husbandry, relative to other subsistence activities.</p>
...
<dt>Description:</dt>
<dd>Dependence on animal husbandry, relative to other subsistence activities.</dd>
```

Both occurrences are the variable's Description (the top Description line and the metadata block); the Gate quote
is byte-identical, including the final period.

**Dataset attribution.** The page's metadata block reads `Dataset: Murdock et al. 1999 'Ethnographic Atlas'`
(link `https://d-place.org/contributions/EA`). This matches the row's title/parenthetical.

**Codes and Values.** The page renders ten codes, 0→9:

```
0  0-5%     1  6-15%    2  16-25%   3  26-35%   4  36-45%
5  46-55%   6  56-65%   7  66-75%   8  76-85%   9  86-100%
```

and a Values table with counts, in code order 0→9:

```
434, 344, 230, 139, 57, 34, 13, 12, 15, 12      (sum 1,290)
```

Arithmetic: code 9 = 12 (0.93%); code 8+9 = 27 (2.09%); code 7+8+9 = 39 (3.02%). The page does not print the total;
the sum is our arithmetic and matches the seat report's own sum (`build/SrcPeku.md:235-237`, "Their sum is 1,290
(my arithmetic; the page does not print the total)").

**Second representation, same counts.** Fetching the ten per-code map layers
(`/parameters/EA004.geojson?domainelement=EA004-N`, N = 0..9) yields features per code
434 / 344 / 230 / 139 / 57 / 34 / 13 / 12 / 15 / 12, with **1,290 distinct language `pk`s and zero duplicates
across codes**. The HTML Values table and the map layers therefore agree; the frequency claim is not a misreading
of one rendering.

### 2. Row fields, `corpus/SOURCES.md:95`

```
| S066 | D-PLACE, variable EA004 Subsistence economy: animal husbandry (Murdock et al. 1999 Ethnographic Atlas) — https://d-place.org/parameters/EA004 | dataset | A | EA004 code definitions and value counts in the edition served 2026-10-21 | variable page Description and Values table | dependence on animal husbandry is coded in ten bins; few societies are near-totally dependent | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Parsed shape (`awk -F'|'` on the landed row): **NF=13, i.e. 11 cells**, matching the contract's census shape.
Field-by-field:

- `source` — title, `EA004`, attribution and URL all match the opened page.
- `kind` `dataset` — correct: the row is the dataset's variable page, not a paper or a landing-page description.
- `tier` `A` — see §4.
- `scope` — exactly the authority boundary this attack tested: "EA004 code definitions and value counts in the
  edition served 2026-10-21". It does not claim ethnographic truth, mobility, herd size or causation.
- `anchor` — "variable page Description and Values table": both exist on the opened page (raw HTML above; Values
  block above). No bare homepage.
- `teaches` — "dependence on animal husbandry is coded in ten bins; few societies are near-totally dependent":
  ten bins confirmed; "few" confirmed by 12/1,290 (or 27/1,290 on a 76–100% reading). The phrase is a derived
  frequency, but the row's own `scope` includes "value counts", and both clauses are directly readable from the
  anchored Values table.
- `status` `mined`; `used-by` path exists at the landed commit and is the entry under attack; `opened` `2026-10-21`
  matches today and the Gate bullet; `recheck` `365d` — see §7.

### 3. Gate bullet, `corpus/lessons/round-50.md:51`

```
- S066 — https://d-place.org/parameters/EA004 — accessed 2026-10-21 — variable Description: "Dependence on animal husbandry, relative to other subsistence activities." Seat: SrcPeku.
```

- URL and access date match the row (`SOURCES.md:95`).
- Quote is 9 words (≤25 per contract rule 1) and appears verbatim at the stated location (two raw-HTML occurrences
  above; the "variable Description" label is exact).
- The Gate header (`round-50.md:29`) says every row S048–S069 was opened by the round-50 build seat named in its
  bullet. The named seat report exists and records the same source:
  `.ufo/waves/round-50/build/SrcPeku.md:224-241` ("Row E — D-PLACE EA004 animal husbandry", the 9-word quote,
  the counts, "Tier A, reason", and `on-release`). So the seat attribution is not invented.
- The seat report's proposed row was `status queued`, `used-by —`; the landed row is `mined` with the entry in
  `used-by`, correct because the entry cites it. The seat's proposed `teaches` carried the explicit counts; the
  landed row condenses them to "few societies are near-totally dependent" — faithful, not stronger.

### 4. Tier and scope under `corpus/QUALITY.md:29` (criterion 6)

Criterion 6: "publisher descriptions and abstracts are tier B for substantive claims about a work, even when
accurate; reserve tier A for sources primary or authoritative for the exact scope."

- This is **not** a publisher description or abstract; it is the dataset's own variable page, served by D-PLACE,
  carrying the code labels and value counts for EA004.
- The row's scope is deliberately narrow: "EA004 code definitions and value counts in the edition served
  2026-10-21". D-PLACE is authoritative for the codes/values of the edition it serves; the page's own
  `Dataset: Murdock et al. 1999 'Ethnographic Atlas'` line identifies the underlying dataset.
- The tier does **not** extend to mobility, herd size, species mix, causal claims, or the Ethnographic Atlas's
  ethnographic truth — the row's scope says none of that, and the entry's sentence uses it only for a frequency.
- Same-source, same-pattern precedent: S042 (`corpus/lessons/round-49.md:74`) is the D-PLACE EA001 row with the
  identical tier logic ("variable page, Codes table and Values counts") and tier A; it was accepted. S066 follows
  that precedent, not a new tier convention.
- No tier inflation: `dataset` + A is not the `community`-A prohibition; the census's tier-inflation check is not
  tripped.

Verdict on this axis: **A is honest for the exact scope.**

### 5. Every S066 citation in the landed tree

Census:

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -n 'S066' 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0 -- .
1c779e4...:corpus/SOURCES.md:95:<row>
1c779e4...:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:7:<shelf range S048–S069>
1c779e4...:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:25:<the claim sentence>
1c779e4...:corpus/lessons/round-50.md:51:<Gate bullet>
```

No other landed file cites S066. The entry's citations:

| line | text (abridged) | support |
|---|---|---|
| `:25` | "Dependence varies: the Ethnographic Atlas codes only a small minority of its societies as near-totally dependent on animal husbandry (S066) — design a **dial**, not a type." | **HOLDS.** The page's Values table gives 12/1,290 at 86–100% (0.93%), 27/1,290 at ≥76% (2.09%), 39/1,290 at ≥66% (3.02%); "only a small minority" is true under any near-total reading. "Dependence varies" is supported by the ten-bin spread (434 at 0–5% through 12 at 86–100%). "Design a dial, not a type" is craft advice, not a factual claim. No number, threshold or cause is asserted beyond the source. |
| `:7` | external-shelf list: "S048–S069, each row carrying its URL, access date, tier scope and anchor" | **HOLDS** bibliographically: S066 has URL, access date, tier scope and anchor. |
| `:9` | `source:` line: "S048–S069 ... each with URL, access date 2026-10-21, tier scope and the round lesson's located quote" | **HOLDS** bibliographically: S066's Gate bullet carries URL, date and a located quote. |

The entry does not restate the counts, the ten-bin structure, or any causal claim from S066; there is no overreach
to correct.

### 6. Gate-evidence observation (non-blocking)

The Gate quote grounds the variable's subject ("dependence on animal husbandry, relative to other subsistence
activities") but does not itself state the row's quantifier ("coded in ten bins; few societies are near-totally
dependent"). The Values table that grounds that quantifier is named in the row's `anchor` and is immediately below
the Description on the same page; the build seat's report records the counts; the round's own S064 bullet follows
the same locator pattern (a single located quote plus a broader anchor). So I do **not** score this as a rule-1
breach or a false claim. It is thinner than the same-source S042 precedent, whose round-49 bullet explicitly
records the Values counts (`round-49.md:74`: "Values table: 722 / 265 / ... (sum 1290)"). If the author lane wants
full parity, the smallest improvement is an appended, dated correction (or next-round Gate note) carrying
"Values table: 434/344/230/139/57/34/13/12/15/12 (sum 1290; 12 at 86–100%)". Do not silently rewrite a landed
lesson.

### 7. Recheck-cadence observation (non-blocking)

The row says `recheck` `365d`; the same dataset's S042 uses `on-release`, and the seat's own row-E proposal says
`on-release` for the reason "D-PLACE editions churn; re-open before quoting counts" (`build/SrcPeku.md:255`).
All new rows S048–S069 land with 365d, so this looks like a wave-wide normalization, not a S066-specific error.
The row's `scope` pins the edition to "the edition served 2026-10-21", so the claim is time-scoped and 365d is a
yearly refresh rather than a false stability claim. Optional consistency fix: change `recheck` to `on-release`
(contract rule 2 allows in-place `recheck` changes; log old→new in a round lesson).

### 8. Receipt note

`reports/round-50/validation.json` is **not in the landed commit**:

```
$ git -C ... show 1c779e4...:reports/round-50/validation.json
fatal: path 'reports/round-50/validation.json' exists on disk, but not in '1c779e4...'
```

The on-disk receipt's `"S066": "ok"` (`reports/round-50/validation.json:209`) is produced by
`sources_check` (`reports/round-50/run-validation.py:246-274`), which checks only: one registry row exists,
`used-by` contains the entry name, and `opened == DATE`. It does **not** open the URL or verify the quote/counts.
The receipt therefore cannot stand in for this source re-open; the evidence above is the direct check.

## Smallest fixes (optional; no claim fix required)

1. **Gate evidence (optional).** Append a dated correction/next-round Gate note for S066 with the Values counts
   quoted above, matching S042's precedent. The row's anchor already names the Values table, so the claim itself
   needs no change.
2. **Recheck (optional).** If the lane wants same-dataset consistency, log `recheck` `365d` → `on-release` for
   S066 per contract rule 2. The row's scope already pins the edition, so this is a guard-strength choice, not a
   correction of a false statement.
3. **No row or entry rewrite is required.** The tier, scope, attribution, quote, ten bins and "few" all hold.

## Limits

- No installs (no pacman/uv/npx); nothing to record under the tooling directive.
- No private clone was needed; `git show` sufficed. The fetched HTML/JSON/geojson temp files were deleted after
  the checks; only this report was written.
- The D-PLACE page shows no explicit edition/version string; "the edition served 2026-10-21" is a serve-date pin.
  The counts are the served state on 2026-10-21 and match the seat's same-day read and two independent page
  representations (HTML Values block and per-code geojson layers); D-PLACE can change after that date, and the
  row's `recheck` is the guard.
- The underlying Murdock et al. 1999 *Ethnographic Atlas* book was not opened; the row's attribution rests on the
  page's own dataset line, which is within the row's served-edition scope. This attack does not certify the EA's
  ethnographic coding beyond what D-PLACE serves.
- The on-disk acceptance receipt is not landed and its S066 "ok" is resolution-only (see §8).
