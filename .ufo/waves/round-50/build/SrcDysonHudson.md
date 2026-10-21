# Frontier source open — Dyson-Hudson & Dyson-Hudson 1980, "Nomadic Pastoralism"

Seat: `ChousaR27R2.SrcDysonHudson-4` (scout, leaf). Round 50, claim C (coverage /
pastoralism entry). Base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Read-only: no lane file touched, no clone, no patch (scout seat, not executor).

## Assigned item

Open the landing page for Dyson-Hudson & Dyson-Hudson 1980, "Nomadic Pastoralism",
*Annual Review of Anthropology* 9, doi `10.1146/annurev.an.09.100180.000311`; quote the
abstract; return a SOURCES candidate (URL, access date 2026-10-21, kind, tier + reason,
scope, ≤25-word verbatim quote with location, what it teaches the entry and which section,
recheck cadence).

## Result — the premise does not hold: this article has no abstract

Opened for real this session. The landing page renders; **it contains no abstract
section**, and the publisher's deposited metadata records no abstract. This is a
finding about the source, not a fetch failure — I did not invent a quote to fill the slot.

| Route | Outcome |
|---|---|
| `https://www.annualreviews.org/content/journals/10.1146/annurev.an.09.100180.000311` | **renders** (native fetch, full page). Title, both authors, "Vol. 9:15-61 (Volume publication date October 1980)", DOI, "View Citation" block, Most Read / Most Cited lists. **No abstract section anywhere.** |
| `https://doi.org/10.1146/annurev.an.09.100180.000311` | resolves via Crossref; reader prints `## Abstract` / **`No abstract available.`** and an empty Crossref `abstract` field |
| `https://api.crossref.org/works/10.1146/annurev.an.09.100180.000311` | `status: ok`, no `abstract` key; `reference-count: 0`; pages `15-61`; vol `9`, issue `1` |
| `https://api.openalex.org/works/https://doi.org/10.1146/annurev.an.09.100180.000311` | `W4250333829`; `open_access.oa_status: "closed"`, `oa_url: null`, `any_repository_has_fulltext: false`, `has_fulltext: false`; no `abstract_inverted_index` |
| `https://www.annualreviews.org/doi/10.1146/annurev.an.09.100180.000311` | **HTTP 403** |
| `https://www.annualreviews.org/doi/pdf/10.1146/annurev.an.09.100180.000311` | **HTTP 403** |
| `https://www.jstor.org/stable/2155728` | **"Client Challenge"** bot wall |
| `https://www.deepdyve.com/lp/annual-reviews/nomadic-pastoralism-TDNSHW0UBY` | **HTTP 403** |
| `https://psycnet.apa.org/record/1981-27927-001` | **HTTP 403** |
| `https://www.erudit.org/en/journals/as/2020-v44-n3-as06115/1078165ar.pdf` | **Anubis proof-of-work wall** ("Making sure you're not a bot!") |

Net: no abstract exists to quote, and no open copy of the body is reachable from this
host. Annual Reviews commissioned no abstracts for the 1980 volume; the article is
closed access with zero repository copies.

## SOURCES candidate (proposed `S048`; id assignment is L1's)

Exact 11-column shape per `corpus/SOURCES.md:25` header
(`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`):

```
| S048 | Dyson-Hudson and Dyson-Hudson 1980, "Nomadic Pastoralism", Annual Review of Anthropology 9:15–61 — https://www.annualreviews.org/content/journals/10.1146/annurev.an.09.100180.000311 | paper | A | bibliographic identity and page span of the 1980 ARA review of nomadic pastoralism only — Annual Reviews published no abstract and no full text was reachable, so this row carries no content claims | landing page (renders) "Vol. 9:15-61" and View Citation block; Crossref works record doi 10.1146/annurev.an.09.100180.000311 (pages 15-61, vol 9, issue 1); OpenAlex W4250333829 oa_status closed, has_fulltext false; "No abstract available." on the DOI resolution; accessed 2026-10-21 | the field's standard 46-page review exists and is identifiability-pinned; its argument, typology and any definition are UNOPENED — tier A holds for identity only, never for what the article says | queued | 2026-10-21 | 365d | — |
```

### Verbatim quote (≤25 words) and its location

> "Rada Dyson-Hudson, Neville Dyson-Hudson. 1980. Nomadic Pastoralism. *Annual Review
> of Anthropology* 9:15-61."

12 words. Location: landing page, "View Citation" block
(`/content/journals/10.1146/annurev.an.09.100180.000311`), read 2026-10-21. This is the
**only** verbatim prose the opened page supplies about the article; it is the citation,
so it evidences identity and page span — nothing about content. The page's other verbatim
string of evidentiary value is the Crossref abstract slot: "No abstract available."

### Tier and scope — why A is narrow here

`A`, scoped to *bibliographic identity and page span*, because the publisher's own landing
page is primary/authoritative for what it published, and Crossref's deposited record
independently agrees (vol 9, issue 1, pp. 15–61). Per `corpus/QUALITY.md:38` (criterion 6)
tiers are scoped to the `scope` column and never global: **this row must never be cited as
tier A for any claim about pastoralism.** For content it is not B and not even C — it is
silent. The lane already has this exact row archetype: S035 (Woodburn) is cited in
`hunting-foraging-subsistence.md:112` as securing "only the article's identity", with every
detail `(to-verify)`.

Status: recommended `queued` (opened; usable as an identity anchor, the way the
hunting-foraging entry cites title/venue/year records at S035, S036). If claim C's entry
does not end up citing it, the honest status is `rejected` with flip "open the journal
full text (JSTOR/Annual Reviews paywall) before registering again".

### What it teaches the entry, and which section

**Nothing at section level.** It can appear only in the entry's `- sources:` external
shelf / bibliography as the field's standard 1980 synthesis, and at most supports a
sentence of the form *"the comparative review of nomadic pastoralism is Dyson-Hudson &
Dyson-Hudson 1980, ARA 9:15–61"* — an existence-and-locus sentence, not a claim about
herding. It cannot populate §1 (register property), the mobility/transhumance section, the
species-and-herd-composition section, or the calibration bank. If L1 wants it load-bearing
in a definition section, the flip is: obtain the body (JSTOR/ILL/paywall) and register a
superseding row with an opened-text anchor.

### Recheck cadence

`365d`. It is a fixed 1980 bibliographic record and cannot churn, but rechecking is cheap
and worth it for one reason only: to see whether Annual Reviews has since deposited an
abstract or opened the back catalogue, which would flip this row from identity-only to
content-capable.

## Anti-laundering notes for the C author (this is the r49 failure mode)

1. **Do not cite this row for content.** Any sentence of the form "Dyson-Hudson &
   Dyson-Hudson (1980) define nomadic pastoralism as…" would be fabricated from this
   row's evidence. If the entry needs the definition, it needs an opened text.
2. **OpenAlex `keywords` and `topics` are algorithmic indices, not author text.** That
   record carries `keywords: nomadic pastoralism, pastoral nomads, pastoralism, pastoral
   societies, animal husbandry, pastoral mobility` and `primary_topic: Rangeland
   Management and Livestock Ecology`. These are machine assignments over citing works.
   They may guide a *search*, and they may not be quoted, paraphrased, or attributed to
   the article.
3. **The web-search snippet is not an open.** A search result surfaced an APA PsycNet
   characterisation ("definition, pure pastoralism vs multi-resource exploitation, women's
   roles, ecology and social organization…") and a JSTOR opening line. PsycNet 403s and
   JSTOR bot-walls, so neither was opened; both stay in the `## Leads (unopened)` class at
   `corpus/SOURCES.md:119-121` — "A lead is not evidence and never a row". If the C author
   wants that characterisation, the PsycNet record must be opened or a text-bearing source
   registered in its place.
4. **Coverage consequence:** the pastoralism entry's substantive anchors must come from
   other rows opened this round. This candidate satisfies "cites a row opened this round"
   only for identity, and a thin citation set is a coverage risk for claim C.

## Unrun checks / bounds honoured

- No lane file, clone, patch, git index or jj state touched; no `git add`/`commit`/`checkout`;
  nothing written under `/home/vgpnk/Projects/shokunin/.ufo`.
- No installs required or attempted (no `pacman` transaction — host-wide pause respected);
  no tool/version/channel to record.
- Did not re-run the entry's §1 gap sweeps or the README sweep — not this seat's question
  (claim C's executor and the verifier own those).
- Did not open the article body; it is not reachable from this host by any of the nine
  routes logged above.
