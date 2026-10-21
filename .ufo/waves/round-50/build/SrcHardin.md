# Frontier source open — Hardin 1968, "The Tragedy of the Commons"

Seat: `ChousaR27R2.SrcHardin-4` (scout, leaf). Round 50, claim C (coverage / pastoralism
entry). Base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only: no lane file touched,
no clone, no patch (scout seat, not executor). Every finding below comes from bytes opened
this session on 2026-10-21.

## Assigned item

Open Garrett Hardin 1968, "The Tragedy of the Commons", *Science* 162:1243 (doi
`10.1126/science.162.3859.1243`); quote the pasture-open-to-all passage with its location;
return a SOURCES candidate (URL, access date 2026-10-21, kind, tier + reason, scope,
<=25-word verbatim quote with location, what it teaches the entry and which section,
recheck cadence). If unreachable, report the failure and stop.

## Result — opened, and the passage is pinned to printed page 1244

The canonical host blocked this host; an open page-faithful scan did not. All routes tried:

| Route | Outcome |
|---|---|
| `https://www.science.org/doi/10.1126/science.162.3859.1243` | **HTTP 403**, Cloudflare interstitial ("Just a moment..."), no article text |
| `https://www.science.org/doi/pdf/10.1126/science.162.3859.1243` and `/doi/epdf/...` | **HTTP 403**, same interstitial |
| `https://www.jstor.org/stable/1724745` (the article's own stable URL) | HTTP 200 but a 3,038-byte **"Client Challenge"** bot wall; no article text |
| `https://web.mit.edu/2.813/www/readings/HardinCommons.pdf` | **HTTP 200, `application/pdf`, 1,493,126 B, 6 pp. — OPENED; this is the anchor** |
| `https://www.garretthardinsociety.org/articles/art_tragedy_of_the_commons.html` | HTTP 200, 44,314 B HTML, full text — opened as an independent text cross-check |
| `https://pages.mtu.edu/~asmayer/rural_sustain/governance/Hardin%201968.pdf` | HTTP 200, 2,128,463 B, 6 pp.; a JSTOR scan of the same article but **image-only** (text layer is the JSTOR cover page), so not usable for quoting |
| `https://faculty.lsu.edu/kharms/files/hardin_1968.pdf` | HTTP 200, 2,132,729 B, 7 pp.; same JSTOR scan family (not the anchor) |

**Opened bytes (anchor):** `https://web.mit.edu/2.813/www/readings/HardinCommons.pdf`,
sha256 `bae818e253468cf71dfbd61d4bd21a781328e94a9fd775e5ed09237a5e67388a`, 1,493,126 B,
6 pages, page size 568.32 x 777.36 pts. It is the AAAS typesetting, not a retyped excerpt:
printed page numbers 1243–1248, running head "SCIENCE, VOL. 162", first-page footer
"13 DECEMBER 1968". Retrieved 2026-10-21.

**Independent identity check:** Crossref `works/10.1126/science.162.3859.1243` →
title "The Tragedy of the Commons", container *Science*, vol. 162, issue 3859,
page `1243-1248`, issued 1968-12-13. Agrees with the scan's page furniture.

**Location of the passage, verified three ways** (layout text, bbox coordinates, and the
rasterized page read as an image):

- printed **p. 1244**, section heading **"Tragedy of Freedom in a Commons"** (heading set
  in the middle column at y≈554 pt; bbox extraction shows the words at x 217–302), body
  passage in the **right-hand column**, first non-epigraph paragraph.
- Verbatim, contiguous, from the scan:
  "The tragedy of the commons develops in this way. Picture a pasture open to all. It is to
  be expected that each herdsman will try to keep as many cattle as possible on the
  commons. Such an arrangement may work reasonably satisfactorily for centuries because
  tribal wars, poaching, and disease keep the numbers of both man and beast well below the
  carrying capacity of the land. Finally, however, comes the day of reckoning..."
- The Hardin Society HTML reprint carries the same wording for the quoted sentences; the
  MIT scan is the anchor because it carries the pagination.

## SOURCES candidate — proposed `S049`

`S048` is already proposed by `ChousaR27R2.SrcUnescoGer-4` in this wave directory; `S049`
has no hit in `corpus/SOURCES.md`, `reports/round-50/` or this build directory
(`grep -rn 'S049' ...`, 2026-10-21). Id assignment stays L1's.

Paste-ready, 11 columns in `corpus/SOURCES.md:25` header order
(`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`):

```
| S049 | Hardin 1968, The Tragedy of the Commons, Science 162(3859):1243–1248, doi 10.1126/science.162.3859.1243 — https://web.mit.edu/2.813/www/readings/HardinCommons.pdf | paper | A | the article's own wording and pagination: the hypothetical open-pasture parable and the conditions Hardin states for it — explicitly NOT an empirical description of any pastoral commons, and not pastoral ethnography | JSTOR scan of the AAAS print at an MIT course mirror, 6 pp., printed pp. 1243–1248, footer "13 DECEMBER 1968"; passage at p. 1244, right column, §"Tragedy of Freedom in a Commons"; pdf sha256 bae818e2…7388a, 1,493,126 B; Crossref record agrees (Science 162(3859) 1243-1248, 1968-12-13); science.org and JSTOR blocked this host 2026-10-21 | the parable's engine is the absence of a stocking rule — "each herdsman will try to keep as many cattle as possible on the commons" — and Hardin himself grants the arrangement "may work reasonably satisfactorily for centuries" while "tribal wars, poaching, and disease keep the numbers of both man and beast well below the carrying capacity"; open-access collapse is therefore a conditional model with stated preconditions, not a law of pastoral life, and his frame is population policy ("no technical solution"), not ethnography | queued | 2026-10-21 | 365d — the 1968 text cannot churn; the cadence is for link rot on a course mirror, and to re-check whether Science/JSTOR has opened a stable copy | — |
```

`status: queued` and `used-by: —` are honest until claim C's entry text actually cites the
row; L1 flips it to `mined` with the entry path at admission (same convention as the
Dyson-Hudson candidate next door). If the entry does not cite it, `rejected` with flip
"the parable is a model, not pastoral evidence".

### Gate fragment for `corpus/lessons/round-50.md`

```
- S049 Hardin 1968, The Tragedy of the Commons — https://web.mit.edu/2.813/www/readings/HardinCommons.pdf
  (opened 2026-10-21; canonical doi 10.1126/science.162.3859.1243, science.org and JSTOR
  stable/1724745 both blocked this host). Verbatim, p. 1244, right-hand column, §"Tragedy of
  Freedom in a Commons", first non-epigraph paragraph: "The tragedy of the commons develops in
  this way. Picture a pasture open to all." (15 words)
```

### Quote and its location (<=25 words)

> "The tragedy of the commons develops in this way. Picture a pasture open to all."

**15 words.** Location: *Science* 162(3859), **p. 1244**, right-hand column, section
"Tragedy of Freedom in a Commons", first non-epigraph paragraph (immediately after the
indented Whitehead epigraph). The sentence that follows, quoted in the row's `teaches`,
supplies the conditions: the arrangement may work "for centuries because tribal wars,
poaching, and disease keep the numbers of both man and beast well below the carrying
capacity of the land."

### Tier reasoning (QUALITY criterion 6)

**A, scoped to "the article's own wording and pagination".** Criterion 6's B rule targets
publisher descriptions and abstracts *about* a work (the S034/S038/S039 → S044–S046
correction). What was opened here is the work's own typeset text — the JSTOR scan of the
AAAS print, with its page numbers — so the scope "what Hardin wrote on these pages" is
primary. The host is a course mirror, not an editorial intermediary; that is a **link-rot
risk, not a tier defect**, and it is recorded in `anchor`.

Two guards, so this A does not metastasize:

1. **Not A for any claim about pastoralists.** The row's scope excludes empirical
   description; the article contains no herders, no field data and no case. A sentence
   like "Hardin showed that real pastoral commons collapse" would be fabricated from this
   row.
2. **Not A for the article's policy argument.** The surrounding article is a
   population-control essay ("The population problem has no technical solution; it
   requires a fundamental extension in morality", p. 1243) whose later sections argue for
   "mutual coercion, mutually agreed upon". None of that is in scope, and none of it
   belongs in a pastoralism entry.

If a reviewer reads the mirror as third-party, the criterion-6 fix is a superseding tier-B
row — never an in-place tier edit (`SOURCES.md` append-only rule).

### What it teaches claim C's entry, and which section

1. **Register property / the null model.** "Picture a pasture open to all" is the entry's
   *baseline case*, and it is expressly hypothetical. The design question a pastoralism
   entry must answer is: which rule converts this baseline into a working system? That
   gives §register-property a clean opening: the pasture is not the pastoral default, it
   is the no-rules limit.
2. **Carrying capacity / stocking-rate table.** Hardin names his own regulators — war,
   poaching, disease — as what holds stock "well below the carrying capacity of the land"
   for centuries. A design table can invert them: for each mortality/offtake channel, what
   keeps the herd under capacity in a designed culture? (raiding, epizootic, winter kill,
   sale, culling, stinting). This is the most useful sentence in the article for a
   worldbuilder and it is usually skipped.
3. **Tenure / commons section.** The parable's premise is a resource "owned by no one"
   with no rule on access or stocking; real pastoral systems are defined by the rules the
   parable omits (seasonal rotation, reserved dry-season pasture, herd caps, common herd
   with private milk rights, grazing fees). Use Hardin as the *counterfactual* the tenure
   section answers, never as the description.
4. **Calibration bank.** Two rows, split by strength:
   - "Tragedy of the commons as a law of pastoral life" → **R** (rejected as a universal;
     it assumes away the institutions that pastoral systems are made of, and Hardin's own
     text makes collapse conditional).
   - "Unmanaged open access with no stocking rule tends to overstock" → **B** (bounded
     model; true as stated, silent on real commons).
5. **Decision-table row** ready to lift:
   `| Pasture open to all, no rule on stocking | expect overstocking of the highest-value animal; write the rule that prevents it or write the collapse | §commons; S049 conditional, do not universalize |`

**What it does not teach:** herd composition, species, transhumance routes, camp
organisation, labour, dairy/yield, tenure forms, or any ethnographic fact. Those need the
other rows opened this round (Dyson-Hudson; UNESCO ger) and, for tenure specifically, a
pastoral-commons case that is **not yet opened** — see the gap note below.

### Recheck cadence

`365d`. The 1968 text cannot change; the recheck exists for (a) link rot on the MIT mirror
and (b) whether Science/JSTOR opens a citable stable copy so the anchor can move to the
canonical URL without changing the quote.

## Companion candidate (offered for coverage) — proposed `S050`: Ostrom 2009

The Hardin row alone is a calibration hazard: a pastoralism entry that cites only the
parable inherits the very universal the lane's criterion 2 requires it to flag. I opened
the primary counter-text so L1 can file the pair, or reject it:

`https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf` — Elinor Ostrom, "Beyond
Markets and States: Polycentric Governance of Complex Economic Systems", Prize Lecture,
December 8, 2009. HTTP 200, `application/pdf`, 2,428,710 B, 37 pp., sha256
`5d11eb59b78e94bef479e66216078231dc803aa9bedd907314a96aba0e53c5f1`; printed page numbers
408–443 run in the footer. Opened 2026-10-21.

Paste-ready row:

```
| S050 | Ostrom 2009, Beyond Markets and States: Polycentric Governance of Complex Economic Systems, Prize Lecture, 8 December 2009, Nobel Foundation — https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf | paper | A | Ostrom's own argument as delivered: that resource users frequently self-organize, and that the presumption of helplessness in social dilemmas is empirically challengeable — not a pastoral-commons case study and not a consensus statement for all commons | Nobel Foundation prize-lecture PDF, 37 pp., printed pp. 408–443, sha256 5d11eb59…c5f1; quote at printed p. 432 (PDF p. 25), final section; Hardin discussed at printed p. 417 | users of common-pool resources are not necessarily trapped: "Thus, in some contexts, one can move beyond the presumption that rational individuals are helpless in overcoming social dilemma situations"; her survey adds that studies of local governance "were not noticed by many theorists and public officials", so the parable's no-rules premise is an assumption to test, not a finding | queued | 2026-10-21 | 365d — fixed lecture text; the cadence is for URL stability | — |
```

**Quote (20 words), printed p. 432 (PDF p. 25), closing section, last sentence of the
trust/cooperation paragraph:** "Thus, in some contexts, one can move beyond the
presumption that rational individuals are helpless in overcoming social dilemma
situations."

**Tier/scope note:** A for Ostrom's own position (the Nobel Foundation's own publication of
her lecture); not A for "commons self-governance is universal" — she says "in some
contexts", and the row's scope keeps that hedge. Claim C should cite it as the *critique
pair* to S049, not as pastoral evidence.

**Gap this pair still leaves, stated plainly:** neither row is a pastoral-commons case.
The entry's tenure section needs an opened ethnographic/historical source on herders'
own grazing rules (the standard candidate is Netting on Swiss alpine commons; not opened
this session, so it stays a lead — `SOURCES.md:119` rule: a lead is not evidence and never
a row). If claim C's entry needs tenure specifics before that row exists, mark them
`(to-verify)` rather than generalizing from Ostrom's irrigation and forest cases.

## Anti-laundering notes for the C author (the r49 failure mode)

1. **"Picture a pasture" is a hypothesis marker, not a report.** Never write "pastoralists
   in open pastures inevitably overstock" — the article supplies a model and no case.
2. **Do not cite S049 for the policy argument.** The article's population-control and
   "mutual coercion" sections are out of scope; so is Hardin's later political writing.
3. **Keep the two calibration rows split** (R for the universal, B for the conditional).
   Collapsing them into one "contested" row loses the usable design content.
4. **Quote page 1244, not "Science 162:1243" alone.** The article begins at 1243; the
   parable is on 1244. If a page-level citation becomes load-bearing, re-verify against
   JSTOR `stable/1724745` (blocked here) — the scan's own page furniture is the evidence
   used today.
5. **Do not launder the mirror.** The row records that the anchor is an MIT course copy of
   the JSTOR scan; a later stable copy may supersede it, but the quote and page stand as
   verified from the opened bytes.

## Unrun checks / bounds honoured

- No lane production file, clone, patch, git index or jj state touched; nothing written
  under `/home/vgpnk/Projects/shokunin/.ufo`. Only this report was written, under the
  lane's own `.ufo/waves/round-50/build/`.
- No installs attempted; no `pacman` transaction (host-wide pause respected). `pdftotext`,
  `pdfinfo`, `pdftoppm` and `curl` were already present. Nothing to record under the
  tooling directive.
- Did not run claim C's §1 gap sweeps, the README sweep, or any entry-contract check — not
  this seat's question.
- Did not open a pastoral-commons case (Netting or equivalent); it is named above as the
  remaining coverage gap, not smuggled in as a row.
- No live-process probing, no credentials, no downloads into the lane (PDFs stayed in
  `/tmp`; digests recorded here).
