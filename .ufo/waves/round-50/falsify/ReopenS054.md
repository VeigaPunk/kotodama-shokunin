# Falsify — SOURCES S054 (Hardin 1968, MIT-hosted PDF)

- **Item attacked:** `corpus/SOURCES.md:83` row S054 at landed commit
  `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, its Gate bullet
  `corpus/lessons/round-50.md:39`, and every S054 citation in
  `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`
  (`:7`, `:11`, `:114`, `:182`; the untagged Hardin mention at `:154` also checked).
- **Verdict:** **PARTIAL** — the source, URL, page, verbatim quote, tier/scope and
  every entry citation hold. The registry locator is wrong on the paragraph
  (`first non-epigraph paragraph`; the quote is the **second** paragraph of the
  section) and the landed row/lesson add a `The` the printed heading does not carry.
  No sentence of the entry that cites S054 is unsupported, so the coverage claim is
  not broken; the row's anchor metadata is.
- **Base/commit read:** all lane bytes through
  `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a…:<path>`;
  no working-tree reads for landed claims, no lane edits, no clone needed.

## 1. Route and HTTP status (live, 2026-10-21)

```
$ curl -sS -L -o /tmp/hardin.pdf -w 'HTTP %{http_code} size %{size_download} type %{content_type} url %{url_effective}\n' \
    https://web.mit.edu/2.813/www/readings/HardinCommons.pdf
HTTP 200 size 1493126 type application/pdf url https://web.mit.edu/2.813/www/readings/HardinCommons.pdf
$ sha256sum /tmp/hardin.pdf
bae818e253468cf71dfbd61d4bd21a781328e94a9fd775e5ed09237a5e67388a  /tmp/hardin.pdf
$ pdfinfo /tmp/hardin.pdf | grep Pages
Pages:           6
```

The digest is identical to the one the build seat recorded (`SrcHardin.md:31`), so the
row is anchored to bytes I actually opened. `https://www.science.org/doi/10.1126/science.162.3859.1243`
and `https://doi.org/10.1126/science.162.3859.1243` both returned **403**; the Gate's
seat note "(science.org 403)" is accurate, and the MIT course mirror is the open route.
No login; the PDF is the AAAS typesetting, not a retyped excerpt.

Identity check (Crossref `works/10.1126/science.162.3859.1243`):

```
title: The Tragedy of the Commons | container: Science | volume: 162 | issue: 3859
page: 1243-1248 | issued: 1968-12-13 | DOI: 10.1126/science.162.3859.1243
```

The scan's folios run 1243–1248 (page 1 footer `13 DECEMBER 1968`, last page
`SCIENCE, VOL. 162 1248`), matching the row's citation exactly.

## 2. Quote and location

The Gate quote (lesson `:39`) is **verbatim** on printed p. 1244. `pdftotext -f 2 -l 2
-raw /tmp/hardin.pdf` reads, in order:

```
65:1244
111:Tragedy of Freedom in a Commons
112:The rebuttal to the invisible hand in
...
130:The tragedy of the commons develops
131:in this way. Picture a pasture open to
132:all. It is to be expected that each herds-
```

so the quoted sentence pair is at the correct page and section. The heading is
**`Tragedy of Freedom in a Commons`**, with no leading `The` (bold heading, middle
column; the rasterised page confirms it).

**The locator's paragraph ordinal is false.** The quote is the **second** paragraph of
the section. The first paragraph is Hardin's own body text, not an epigraph:

> "The rebuttal to the invisible hand in population control is to be found in a
> scenario first sketched in a little-known pamphlet (6) in 1833 by a mathematical
> amateur named William Forster Lloyd (1794–1852). We may well call it "the tragedy
> of the commons," using the word "tragedy" as the philosopher Whitehead used it
> (7): "The essence of dramatic tragedy is not unhappiness…" He then goes on to say,
> "This inevitableness of destiny can only be illustrated in terms of human life by
> incidents which in fact involve unhappiness. For it is only by them that the
> futility of escape can be made evident in the drama.""

The Whitehead quotations are **inline**: the line starts sit at the column margin, not
at a block-quote indent. `pdftotext -f 2 -l 2 -bbox`:

```
Tragedy   x=217.68 y=554.43   (heading, col 2)
The rebuttal ...   x=227.88 y=576.03   (paragraph 1, normal ~10 pt first-line indent; col margin ~217)
volve ...  x=391.56 y=33.86   (tail of paragraph 1 at top of col 3)
The tragedy of the commons develops  x=401.40 y=67.46  (paragraph 2, normal indent; col margin ~391.44)
Picture   x=445.80 y=78.49
dramatic  x=218.76 y=674.91;  Whitehead x=218.52 y=663.15  (quotation lines start at the col-2 margin)
```

The build seat's rationale — "first non-epigraph paragraph (immediately after the
indented Whitehead epigraph)" (`SrcHardin.md:45`, `:88`) — is therefore wrong: there is
no indented epigraph. Paragraph 1 is ordinary body text with a normal first-line
indent; its Whitehead quotations are inline. Even reading the column break as a
paragraph break, paragraph 2 is preceded by paragraph 1's tail (`volve unhappiness…`)
at the top of column 3, so it is not "first".

Landed wording checked:

- `corpus/SOURCES.md:83`, field 6: `p. 1244, §The Tragedy of Freedom in a Commons, first non-epigraph paragraph`
- `corpus/lessons/round-50.md:39`: `p. 1244, §The Tragedy of Freedom in a Commons: "..."`
- `SrcHardin.md:45` / `:79` / `:88` (build seat, not landed) correctly has
  `Tragedy of Freedom in a Commons`; the landed `The` is absent from the seat's
  candidate and from the print — an integration slip [INFERENCE: introduced during
  paste-up; no intermediate patch was inspected].

## 3. Tier and scope under QUALITY criterion 6

The row's tier A is scoped to "the article's own wording and pagination of the
open-pasture parable; not an empirical description of any pastoral commons"
(`SOURCES.md:83`, field 5). That is honest:

- What was opened is the article's own typeset text with the original folios, so tier A
  for "the article's own wording and pagination" is the criterion-6 A case (primary for
  the exact scope), not the B case for a description/abstract *about* a work.
- The scope disclaimer is true of the text: "Picture a pasture open to all" is a
  hypothetical (paragraph 2); the essay is normative/analytic, not an ethnography of
  any pastoral commons. The row's `teaches` — "the pasture model assumes access open to
  all and no rule; a counterfactual baseline, not a law of pastoral life" — matches the
  text (the pasture is open to all; no rule appears in the parable; the arrangement's
  durability is attributed to tribal wars, poaching and disease, not to a rule).
- No tier inflation, and no in-place tier edit was made.

One locator-honesty defect remains: calling the passage the "first **non-epigraph**
paragraph" asserts a structural fact the scan does not support (see §2).

## 4. S054 citations and the related Hardin mention in the entry

| Entry line | Sentence | Holds? |
|---|---|---|
| `:7` | "S054 Hardin 1968" in the external-shelf list | **Yes** — row exists, is `mined`, and its `used-by` names this entry. |
| `:11` | "re-open S054 and S055 together before writing a commons rule" | **Yes** — appropriate to a model/parable; the row's 365d recheck is a floor, not a bar. |
| `:114` | "Hardin 1968 \| "Picture a pasture open to all" (S054) — an unregulated parable \| **R** as a law of pastoral life; **B** for genuinely open access \| a designed collapse only where no rule exists" | **Yes** — quote is a verbatim substring on p. 1244; "unregulated parable" matches the open-access model; the R/B labels are the entry's calibration, consistent with the row's "not a law of pastoral life". |
| `:154` | "§8; never default to Hardin's open pasture" (no S-id; untagged Hardin mention) | **Yes** — design instruction consistent with the row's counterfactual-baseline scope. |
| `:182` | "Hardin's tragedy describes pastoral commons \| R as universal; B for unmanaged open access — S054 vs S055 \| choose the rule set first: open access, group, state or private" | **Yes** — the source is a model, not an empirical description; the B bound for unmanaged open access matches the row's scope. The "open access, group, state or private" typology is S055's side of the comparison and is outside this seat. |

No S054-citing sentence overreads the source, and the untagged Hardin instruction at
`:154` is consistent with it. The entry is safe as landed.

## 5. Smallest fixes (author lane, not applied here)

1. **Paragraph locator.** `corpus/SOURCES.md:83`, field 6: replace
   `p. 1244, §The Tragedy of Freedom in a Commons, first non-epigraph paragraph`
   with
   `p. 1244, §Tragedy of Freedom in a Commons, second paragraph (first is the Lloyd/Whitehead paragraph; the Whitehead quotations are inline, not an epigraph)`.
   The registry is append-only — "only `status`, `recheck` and `used-by` change in
   place; a correction is a new row whose `teaches` opens `supersedes S0NN —`"
   (`corpus/SOURCES.md:9-12`) — so the contract-compliant form is a **superseding row**
   (e.g. S070) whose `teaches` opens `supersedes S054 — …` and carries the corrected
   anchor. If the integrator treats a locator typo as correctable before the round
   record closes, patch the field and log old→new in `corpus/lessons/round-50.md`.
2. **Heading transcription.** Delete `The ` before `Tragedy` in
   `corpus/SOURCES.md:83` (same field 6) and `corpus/lessons/round-50.md:39`. The
   printed heading is `Tragedy of Freedom in a Commons`; URL, date, page and quote stay
   as landed.
3. **Optional guard.** In the superseding row's `teaches`, record that the quote is
   paragraph 2's first two sentences and that the Whitehead quotations in paragraph 1
   are inline, so a future re-opener is not misled by the seat's "indented epigraph"
   note.

Not BROKEN: the row still points at the correct page and section, the quote is
byte-verbatim, the tier/scope is honest, and all four S054-tagged entry citations
(plus the untagged `:154` mention) are supported. Only the paragraph ordinal and one
heading word are wrong.

## 6. Unresolved / not found

- No S054 citation outside `corpus/SOURCES.md:83`, the entry's four citing lines, and
  `corpus/lessons/round-50.md:39` (`git grep -c 'S054'` over `corpus/`: SOURCES 1,
  entry 4, lesson 1).
- `reports/round-50/validation.json` (working tree; **not** in `1c779e4`) records
  `"S054": "ok"` in its source-resolution block (lines 165–197), but that is a
  used-by/resolution check, not an anchor check; cited only as context.
- No credentials, no logins; no installs or upgrades (curl, poppler-utils, python3
  stdlib only). Temp artifacts `/tmp/hardin.pdf`, `/tmp/hardin.txt`, `/tmp/p2.png`,
  `/tmp/crop.png` removed after the checks.

## Reproduction

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:corpus/SOURCES.md | sed -n '83p'
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:corpus/lessons/round-50.md | sed -n '39p'
curl -sS -L -o /tmp/hardin.pdf https://web.mit.edu/2.813/www/readings/HardinCommons.pdf
pdftotext -f 2 -l 2 -raw /tmp/hardin.pdf - | sed -n '60,70p;105,135p'
pdftotext -f 2 -l 2 -bbox /tmp/hardin.pdf - | grep -E 'Tragedy|rebuttal|Picture|volve|dramatic'
pdftoppm -f 2 -l 2 -r 110 -png -singlefile /tmp/hardin.pdf /tmp/p2
```
