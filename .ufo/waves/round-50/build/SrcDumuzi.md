# SrcDumuzi — frontier source for claim C: the Sumerian "debate between Sheep and Grain" (ETCSL 5.3.2)

Seat `ChousaR27R2.SrcDumuzi-4` (scout, leaf; no delegation, no background jobs). Round 50, claim C
(coverage / pastoralism entry). Lane base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only on the
lane: this report is the only write; no clone, no patch, no install, nothing under
`/home/vgpnk/Projects/shokunin/.ufo`.

## Assigned item

Open the Oxford ETCSL text **"The debate between Sheep and Grain"** (or "Dumuzid and Enkimdu"), quote a
located line, and return one SOURCES candidate: URL, access date 2026-10-21, kind, tier with reason,
scope, a verbatim ≤25-word quote with location, what it teaches the entry (which section), recheck cadence.

## Access record — live host unreachable, the same Oxford page opened from the Internet Archive

- Canonical URL: `https://etcsl.orinst.ox.ac.uk/section5/tr532.htm`.
- **Live host failed this seat.** `read` on the URL returned `Failed to fetch URL; Cause: The operation
  timed out` (https); the ETCSL root page failed the same way. `curl` over both schemes with
  `--max-time 35` returned `curl: (28) Connection timed out after 35001 milliseconds`, `http=000
  bytes=0` (http and https, 2026-10-21). DNS is fine: `getent hosts etcsl.orinst.ox.ac.uk` →
  `163.1.185.89  orin-hutton.orient.ox.ac.uk`, so the failure is connection-level, not name resolution.
  The composition does exist at that URL — a search index returns it as "The debate between Sheep and
  Grain: translation" with ETCSL composition number t.5.3.2, which corroborates the path.
- **Opened instead, this session:** the Internet Archive capture of the same Oxford URL,
  `https://web.archive.org/web/20260605210113id_/https://etcsl.orinst.ox.ac.uk/section5/tr532.htm`
  (capture timestamp `20260605210113`, HTTP 200, gzip body, **12,767 bytes** decompressed,
  sha256 `97817899b6fdd7f5a567157b9b497ba2fbb2bef77c29ca3be0684551d43fd5f2`). Page `<title>` is
  `The debate between Sheep and Grain: translation`; the body carries the ETCSL line anchors
  `c532.htm#line1 … #line192` and the edition's revision history `29.vii.1999 … 7.ix.2001`, ending
  "substantive content of file not changed". CDX shows the 2026-02-18 and 2026-06-05 captures sharing
  digest `47QTFUXVUTJROVDRR6OKADGZU2IEWYFE`, and 2008–2025 captures sharing
  `26O4YF5ELCZHDV5QKJ65P3ZGLZS37BW5` (re-packaging only; the text is stable).
- Every quote below was machine-checked as an **exact substring** of the captured text
  (`re.sub(r'<[^>]*>','', …)` + whitespace collapse), and word counts are `len(q.split())`. None exceeds 25.

## Candidate row (paste-ready, 11 columns; id is L1's to assign — S048 is already proposed by `SrcSherratt`)

```
| S0NN | The debate between Sheep and Grain, Sumerian disputation, ETCSL translation (composition 5.3.2) — https://etcsl.orinst.ox.ac.uk/section5/tr532.htm | dataset | A | the composition's own wording on herding and its relation to farming — an emic literary representation (what the poem says), not a description of pastoral practice | translation page, line block 130–142 (anchor c532.htm#line130), Grain's third speech; opened 2026-10-21 from Internet Archive capture 20260605210113 of the Oxford URL (live host timed out on http and https) | a herd is a counted stock — the nightly count and tally-stick record ewes, lambs, goats and kids — and Sheep and Grain are co-created sister economies whose divine verdict still ranks Grain first and seats herd owners at the grain owner's gate | queued | 2026-10-21 | 365d | — |
```

Notes for the registrar:
- **kind**: `dataset` is the closest of the seven allowed values (a line-addressed electronic text
  corpus/edition; the row is scoped to one composition). `book` is the alternative if L1 prefers
  work-level kinds for literary texts — the composition is not a monograph.
- **status**: `queued`; set `mined` and `used-by:
  corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` only when the landed entry
  actually cites the row. No in-place edit of any filed row.
- **opened** is the access date 2026-10-21, per the registry convention.

## Tier and scope (QUALITY criterion 6)

- **Tier A, scoped to**: *the composition's text and wording* — ETCSL is the Oxford Oriental
  Institute's critical electronic edition and translation, i.e. primary/authoritative for what this
  composition says (criterion 6 reserves A for "sources primary or authoritative for the exact
  scope"). It is not a publisher blurb or an abstract of a work.
- **Not A for anything else.** For any claim about real pastoral practice, the poem is a single
  literary voice (topos), so use it as a period emic register and pair every practice claim with an
  archaeological/administrative source already on the shelf (Marciniak 2011, Zeder 2008, the FAO
  chapters) — the same rule §13 applies to the cattle-complex.
- **Access caveat for L1**: the row was opened from the Internet Archive capture because the live
  Oxford host was unreachable from this seat. If the registry's "opened" rule is read as
  *live-host-only*, hold this row (`queued`, tier B) rather than promote it; the capture is the
  publisher's own page (stable digest since 2008) and nothing about the text is reconstructed.
- **Scope sentence**: "the composition's own wording on herding and its relation to farming — an emic
  literary representation, not a description of pastoral practice."
- **Recheck cadence**: 365d. The text is frozen (revision history ends 2001, "substantive content of
  file not changed"); the annual check is for host/archive availability and any ETCSL revision, not for
  content drift.

## Located quotes (verbatim, each ≤25 words)

Primary (for the row's `anchor`):

1. **13 words**, line block **130–142** (anchor `c532.htm#line130`), Grain's third speech:
   > Every night your count is made and your tally-stick put into the ground

Supporting (same page, location as noted):

2. **16 words**, block 130–142, immediately after quote 1 — the count's purpose:
   > so your herdsman can tell people how many ewes there are and how many young lambs
3. **14 words**, block **43–53** — the fold and assigned grazing at creation:
   > Sheep being fenced in by her sheepfold, they gave her grass and herbs generously
4. **20 words**, block **26–36** — milk as the sheepfold's product, given to mankind:
   > the Anuna gods of the Holy Mound partook of the sweet milk of their holy sheepfold but were not sated
5. **19 words**, block **102–106** (Sheep speaking) — pastoral outputs feeding field labour:
   > Sustenance of the workers in the field is mine: the waterskin of cool water and the sandals are mine
6. **10 words**, block **180–191** (Enki's verdict) — co-creation without a ladder:
   > Sheep and Grain should be sisters! They should stand together!
7. **23 words**, block **180–191** — herd wealth seated at grain's gate (the dependence statement):
   > Whoever has silver, whoever has jewels, whoever has cattle, whoever has sheep shall take a seat at the gate of whoever has grain

## What it teaches the entry, by section

- **§1 (register property)** — Sheep and Grain are created together on the Holy Mound and given to
  mankind "as sustenance" (block 26–36); the pastoral and agrarian registers are **co-created sister
  economies, not rungs**. Quote 6 states the complement in the gods' own voice. Use it to open §1 and
  to refuse the hunting→herding→farming ladder without arguing from modern ethnography alone.
- **§6 (products)** — quote 4 gives milk as the sheepfold's repeated product (a secondary product
  taken from living animals), and quote 5 gives the waterskin and sandals as pastoral goods consumed
  by field labour: the product chain crosses the boundary in both directions.
- **§7 (herd as wealth and exchange)** — the load-bearing detail for the entry is **herd accounting**:
  quote 1 (nightly count) + quote 2 (ewes, lambs, goats, kids) make the herd a *counted stock* with a
  material record (the tally-stick) and a demography (species and age classes). It is stronger because
  the speaker is Grain, the herd's rival — an opponent's concession, not herder self-praise. Quote 7
  states the dependence of herd wealth on grain directly, the literary counterpart of Khazanov's
  "the more specialized … the more dependent" already queued for §7/§13.
- **§13 (calibration bank)** — quote 6 + quote 7 are the calibration pair: the ranking of grain over
  sheep is a **divine verdict** in the poem (Enki decrees "Grain shall be the greater"), not an
  evolutionary fact. Use against the "pastoralism is a stage" row: the earliest explicit ranking in the
  register is theological and political, and the poem still gives the herding side its own inventory.
  Do not quote the poem as evidence about Mesopotamian herd sizes or practices; that claim needs the
  administrative/archaeological shelf.

## Suggested search-log sentence (for `corpus/SOURCES.md ## Search log`, round-50 entry)

> **Pastoral primary voice (rows S048+).** Question: which primary text states the pastoral/agrarian
> complement and the herd-accounting practice in period voice? Where searched: the ETCSL composition
> 5.3.2 page (`etcsl.orinst.ox.ac.uk/section5/tr532.htm`) — the live host timed out on http and
> https from this seat (connection timeout, DNS resolving), so the same Oxford page was read from
> Internet Archive capture `20260605210113` (12,767 bytes decompressed, revision history ends 2001) —
> one row included; `Dumuzid and Enkimdu` not located (the section-4 `tr48*` prefix returns "The
> temple hymns" at `tr4801.htm`; `tr4802`/`tr4804` unopened), recorded as a lead, not a row.

## Caveats and unrun checks

- **Not a live-host read.** Report the access path exactly as above; do not upgrade the row's wording
  to "opened at etcsl.orinst.ox.ac.uk" without a successful live fetch.
- **Translation wording is ETCSL's** (Black/Cunningham/Robson/Zólyomi edition, revisions 1999–2001).
  Preserve the editors' uncertainty marks — e.g. "the vat on legs (?)" — and do not silently normalise
  `c`/`j` for `š`/ŋ in quoted text.
- **Literary, not ethnographic.** One composition, one period voice, hostile-witness framing for the
  count. Never let it carry a distributional or practice claim; §13 must keep it in the topos column.
- **"Dumuzid and Enkimdu" not opened.** It is a different composition; no ETCSL URL for it was
  identified in this seat (`section4/tr4801.htm` is "The temple hymns"; `tr4802`, `tr4804` are in the
  CDX list but were not opened). No second row is offered from an unread text.
- **Unrun (out of seat scope):** corpus sweep, README index, entry line counts, separability run, any
  build/lint. Nothing installed or updated (reads and searches only: `read`, `curl`, `web_search`).
