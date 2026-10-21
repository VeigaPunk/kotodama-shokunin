# SrcHerskovits — frontier source for claim C: Herskovits 1926, *The Cattle Complex in East Africa*

Seat: `ChousaR27R2.SrcHerskovits-4`, source seat, 2026-10-21. Lane `kotodama-shokunin`,
base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Assigned: open the DOI/landing page
(Wiley AnthroSource) for Herskovits 1926, *American Anthropologist* 28; quote its scope;
note later critique if found on the same page; return a SOURCES candidate (URL, access date
2026-10-21, kind, tier + reason, scope, <=25-word verbatim quote with location, what it
teaches the entry, recheck cadence). Author-lane advice, never admission.

## Assigned item and outcome

**The assigned source could not be opened in any rendering that carries its text.**
Every route that serves the article body returned HTTP 403 (Wiley, HathiTrust), a
client challenge (JSTOR), or a network timeout (Internet Archive). Per the seat
instruction ("if unreachable, report the failure and stop on that source"), **no
content row is proposed for Herskovits 1926**; §3 offers an optional identity-only
row in the lane's existing S035/S036 pattern, and §2 offers the row that *did* open
and that carries both the construct's statement and its later critique.

- Opened in full this session: **Eczet 2020, *Techniques & Culture*** (DOI
  `10.4000/tc.14002`) — open edition, full HTML read; it states that the expression
  *cattle complex* comes from Herskovits 1926 and is itself a later critique of the
  imitation/identification vocabulary built on that complex.
- Opened in full this session: **Crossref records for all four part DOIs** of the
  1926 serial (title, pages, issue, citation counts; no abstract on any part).
- Not opened: the 1926 article's text, abstract, first page, or any description
  written by its author. Nothing below quotes Herskovits.

## 1. Access log — every route tried, 2026-10-21

| Route | Result |
|---|---|
| `https://anthrosource.onlinelibrary.wiley.com/doi/10.1525/aa.1926.28.1.02a00050` | **HTTP 403**, bot interstitial ("Performing security verification"); tried with `read`, with curl (two user agents) and through `r.jina.ai` (Cloudflare "Just a moment…", "Target URL returned error 403") |
| `…/doi/abs/10.1525/aa.1926.28.1.02a00050` | **HTTP 403** |
| `…/doi/pdf/10.1525/aa.1926.28.1.02a00050` | **HTTP 403** |
| `https://onlinelibrary.wiley.com/doi/…` and `https://doi.org/10.1525/aa.1926.28.1.02a00050` | **HTTP 403** (doi.org resolves to the same AnthroSource page) |
| Wayback capture `20240806173006` of the landing page | the archive captured the **403 block page** (8,221 bytes) — no article text |
| Wayback capture of the `/doi/pdf/…` URL | HTML shell only; `<title>` is the article title, extracted body text is 155 characters (body is JS-rendered) |
| JSTOR `https://www.jstor.org/stable/660813` | live: HTTP 200 but a "Client Challenge" page; Wayback `20230705145802`: metadata only (`og:description` = "…American Anthropologist, New Series, Vol. 28, No. 1 (Jan. - Mar., 1926), pp. 230-272") |
| JSTOR `https://www.jstor.org/stable/pdf/660813.pdf` | Wayback capture is a JSTOR terms-and-conditions page, not a PDF |
| HathiTrust catalog and full-text search | **HTTP 403** |
| Internet Archive `archive.org` and `ia801400.us.archive.org` | connection timeout from this host (curl `000`, 25–90 s) |
| `r.jina.ai` → `archive.org/stream/in.ernet.dli.2015.533297/…_djvu.txt` | 403 `AbuseAlleviationError`: "Anonymous access to domain archive.org blocked until Wed Oct 21 2026 16:19:09 GMT" |
| Google Books API | **HTTP 429**; `books.google.com` search → Google consent/redirect page |
| SciSpace paper page | human-check wall |
| Crossref `api.crossref.org/works/<doi>` | **200** for all four part DOIs (see §3 table); no `abstract` field on any |

The 1926 serial's four parts, as verified through Crossref this session: 28(1) 230–272,
28(2) 361–388, 28(3) 494–528, 28(4) 633–664; cited-by counts 166 / 42 / 14 / 23. These are
the article's *identity*, not its content.

**The one unexplored route:** `r.jina.ai`'s archive.org block expires 2026-10-21T16:19:09Z
(≈46 min after this seat's last attempt). Search-result URLs (not opened) indicate the
Internet Archive holds DLI scans of the journal — vol. 27 = `in.ernet.dli.2015.533296`,
vol. 29 = `in.ernet.dli.2015.533298` — so vol. 28 is presumably `…533297`, **unverified**.
If L1 wants the primary text this round, that is the retry — otherwise the honest position
stands: unread.

## 2. Candidate row (primary deliverable): S049 — Eczet 2020

Id: `S049` is proposed only because **two sibling seats have already proposed `S048`**
(this seat's UNESCO sibling `SrcUnescoGer.md` and the Dyson-Hudson sibling
`SrcDysonHudson.md`). Id assignment is L1's; renumber freely, the row is id-independent.
`grep -rn -E 'S0(48|49)' corpus tools reports` → no hits (2026-10-21), so the registry itself
is still free from S048 up.

Paste-ready row in the registry's own column order (id per L1):

| S049 | Eczet, Jean-Baptiste 2020, Logiques totémiques dans le cattle complex, *Techniques & Culture*, Suppléments au n°73 — https://journals.openedition.org/tc/14002 | paper | A | the article's own statements: the attribution of the expression cattle complex to Herskovits 1926, and its critique of the imitation/identification/equivalence vocabulary; B if read as a survey of East African pastoralism | full text, opening paragraph of "Texte intégral" (quote below), plus paragraph 1 for the critique clauses; live page opened 2026-10-21 | the cattle-complex label is an observer's culture-area construct; imitation, identification and equivalence are analyst terms whose emic/etic standing was never made clear; cattle coat-colour and "bull + colour" personal names make the herd an identity register, with totemic logic as the alternative to imitation | queued | 2026-10-21 | 365d | — |

Why each field says what it says:

| field | value |
|---|---|
| source | Eczet, Jean-Baptiste 2020, "Logiques totémiques dans le *cattle complex*. Sur l'imitation et l'identification avec les bovins", *Techniques & Culture*, Suppléments au n°73 — https://journals.openedition.org/tc/14002 (DOI 10.4000/tc.14002) |
| kind | paper |
| tier | **A, scoped to** "this article's own statements: the attribution of the expression *cattle complex* to Herskovits 1926, and its critique of the imitation / identification / equivalence vocabulary". If read as a survey of East African pastoralism it is **B** (one specialist's Mursi-fieldwork argument, quoting Evans-Pritchard and Lienhardt in French translation). Criterion-6 fix if a reviewer disagrees: a superseding B row, never an in-place tier edit. |
| scope | the article's own argument only: how the *cattle complex* label arose, why the imitation/identification reading is analytically weak, and the totemic alternative from recent Mursi fieldwork (Omo valley, Ethiopia). Not authority for herd economy, transhumance, pasture law, or Herskovits' own text. |
| anchor | full text, opening paragraph of "Texte intégral" (before the H1 "Imitation, identification, équivalence"); the same sentence is repeated in the page's `meta-prism.teaser`. Live page opened 2026-10-21 (publisher's open edition; the page's `DC.publisher` metadata names Les Éditions de l'EHESS). |
| status | `queued` until claim C's entry actually cites it; then `mined` with `used-by` = `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` |
| opened | 2026-10-21 |
| recheck | 365d (fixed 2020 DOI on an open-edition platform; nothing churns) |

### Quote (24 words, verbatim, French)

> L’omniprésence des bovins dans les pratiques et les discours des populations nilotiques
> d’Afrique de l’Est fut à l’origine de l’expression cattle complex (Herskovits 1926).

Location: "Texte intégral", **opening paragraph, first sentence** — the paragraph that
opens the body and continues "…l’indémaillable intrication entre les humains et bovins au
quotidien."

Two supporting clauses on the same page (use only if the entry needs the critique in the
source's own words):

> Ces dérives analytiques sont rendues possible, il me semble, par l’usage de plusieurs notions

(14 words) and

> dont on ne sait parfois si elles ont une valeur émique (le point de vue des Nuer) ou étique

(20 words). Both located in **paragraph 1** of "Texte intégral" (the numbered paragraph
opening "Pour justifier ces pratiques dépassant la production de protéines lactées et
carnées…"), the second immediately after the first, ending the sentence "…: imitation,
identification et équivalence, autant de termes ayant circulé jusqu’à aujourd’hui avec
efficacité dans la littérature anthropologique, à défaut d’avoir été tout à fait précisés."

The page also carries an official English abstract; its opening sentence is a translation,
not the author's English, so it is a locator aid, not a second anchor:
"Many gestures and practices of East African pastoralists have been interpreted by
anthropologists as 'imitation' or 'identification' with cattle…" (Abstract → English).

### What it teaches claim C's entry, by the planned C02 sections

Section names follow the round-35 plan's C02 "Owns" list
(`reports/round-35/plan/P01-c-plan.md:203-224`), which claim C inherits:

1. **Herd markers and identity.** The strongest fit. Cattle coat-colours are the elementary
   colour taxa and personal names are built as "bull + colour"; people sing poems to their
   finest oxen and women's poems describe herd distributions; scarification and body
   ornamentation mirror the herd; dance roles are keyed to bulls, calves and the herd as a
   whole. This is a *worked mechanism* for the entry's "how does a herd become an identity
   register" table — not the vague claim that "pastoralists love their cattle".
2. **"Nomad" and other labels as etic.** The *cattle complex* is named as an observer's
   culture-area construct derived from Graebner's *cultural complex*; imitation,
   identification and equivalence are analyst terms whose emic/etic status the article says
   was never made clear (the two clauses above). Feeds the entry's calibration rule that
   "cattle complex" and "nomad" are labels, not self-descriptions.
3. **Pastoral wealth with a source.** The article states a concrete Mursi marriage prestation
   order of magnitude (thirty-eight head) in its paragraph 13, as the largest livestock
   transfer in that pastoralism. Usable only as a single sourced case; **do not reproduce the
   number from this report** — the served HTML shows the word "topettes" where "têtes" is
   meant, so re-read the sentence at the URL before quoting, and give it as one ethnographer's
   case, never a regional figure.
4. **Calibration bank.** One row: "imitation of / identification with cattle" = analyst
   reading, criticized; "cattle complex" = classic construct, not an emic category.

### Cannot support

Herd species mix and product chains beyond cattle; transhumance routes and pasture law;
breeding/castration; fodder and wintering; herd disease; herd counting/numeracy; the
pastoral/settled market-tribute-raid interface; and anything about Herskovits' 1926 text
beyond the attribution sentence quoted above. The Nuer/Dinka material it cites is quoted in
French (Eczet's own translation marked "ma traduction" for Evans-Pritchard 1953/1956 and
Lienhardt 1961; a French edition for Evans-Pritchard 1968) — those primaries were not opened
and stay leads.

## 3. Optional fallback row: Herskovits 1926, identity only

Only file this if the entry names "cattle complex (Herskovits 1926)" in a way the Eczet row
cannot carry. It is the S035/S036 pattern — a bibliographic identity row, not a content row:

| S0NN | Herskovits, Melville J. 1926, The Cattle Complex in East Africa, *American Anthropologist* 28(1) 230–272; 28(2) 361–388; 28(3) 494–528; 28(4) 633–664 — https://doi.org/10.1525/aa.1926.28.1.02a00050 | paper | A | bibliographic identity of the four-part serial only; its text, scope statement and argument are unread | Crossref records for all four part DOIs, opened 2026-10-21 (no abstracts); the Wiley/AnthroSource landing page returned HTTP 403 on every route and no body text exists in this session | the culture-complex label for the East African cattle-centred complex is conventionally sourced to this four-part 1926 serial; open the article before attributing any content | queued | 2026-10-21 | 180d | — |

Verbatim available from the opened record: the title string **"THE CATTLE COMPLEX IN EAST
AFRICA*"** (Crossref, Part 1). That is a title, not a scope statement — the row must not
pretend otherwise. The asterisk is in the deposited title.

## 4. Later critique found on the opened page

All on `journals.openedition.org/tc/14002`, located by paragraph. The assigned Wiley page
carries no critique to note — it served no body text at all (§1), so "later critique on the
same page" could not be tested there.

- **The imitation/identification vocabulary is the target.** The article's stated aim is to
  trace "l’émergence de ces notions pour en montrer les limites" (Abstract, French), and its
  paragraph 1 names the three terms (imitation, identification, equivalence) as circulated
  but never precisely defined, with unclear emic/etic standing.
- **Psychologizing readings are criticized.** Paragraph 1: the "obsession for the animal"
  explanation, already in Evans-Pritchard, is taken up by Hardin (1968) to illustrate the
  "tragedy of the commons" and by psychoanalytic/psychiatric readings (Biedelman 1966;
  Hayley 1968) — the article calls these "dérives analytiques" and says they are enabled by
  the imprecise notions.
- **A narrower counter-claim is cited.** Paragraph 3: Gourlay (1972), from Karimojong
  fieldwork, argued identification is only a minor part of the human–cattle relation.
- **A positive alternative.** The article proposes totemic logic (shared qualities, not
  imitation or full identification) for Mursi dances, anthroponymy and body ornamentation,
  and adds a "colour complex" to the "cattle complex" (paragraph 18).
- **Not on this page:** any critique of Herskovits' 1926 *article* itself. Eczet critiques the
  tradition the label seeded, not the 1926 text, which he does not appear to quote.

## 5. Advice to the entry author (author-lane, not admission)

- Prefer the Eczet row as the content source; it is the only one of the two that supports a
  sentence about how the herd becomes an identity register.
- In the calibration bank, write the construct as etic: "cattle complex — classic culture-area
  label (Herskovits 1926, as reported by Eczet 2020); imitation/identification readings
  criticized". Do not write "the people imitate their cattle" as fact anywhere in the entry.
- Do not import the 38-head figure without re-reading the sentence at the URL (see §2.3).
- The `(to-verify)` list this source should generate: Herskovits 1926 body; Evans-Pritchard
  1956/1968; Lienhardt 1961; Gourlay 1972; Hardin 1968 — all leads seen only through Eczet.

## 6. Confidence and unresolved

- Access failures: **high** — each recorded with status code and, for the archive routes, the
  captured block page or the proxy's own error body.
- Quote text and location: **high** — the sentence is rendered twice on the same page (body
  and `meta-prism.teaser`) with identical wording; the page was fetched live, not from a
  capture. The PDF route returned a 5.1 KB `application/pdf` payload — far too small for a
  twenty-page article — and no text could be extracted from it, so there is no second
  rendering to diff.
- Tier call: **medium-high** — scope-dependent; the scope field states the argument so L1 can
  overrule with a superseding row rather than an edit.
- Remaining unknown: whether the live Wiley page differs from the 403 the bots see (it is a
  1926 item, so most likely a bare metadata page with no abstract); the archive.org retry
  window after 16:19:09Z; whether `in.ernet.dli.2015.533297` is really vol. 28.

## Unrun checks

No lane validator was run (`reports/round-28/readme/sweep.py`, `reports/round-49/run-validation.py`)
— source seat, no production edits. No production file was edited; nothing was written outside
this report. No tools installed or updated. No credentials, no logins, no live-process probing.
