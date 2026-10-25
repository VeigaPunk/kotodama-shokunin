# RevengerCapoeira — round-71 Capoeira miss, reconstructed

Seat: L1Kotodama72.RevengerCapoeira (leaf; no subagent dispatch). Round 72, wave 1.
Assignment: reverse-engineer the round-71 Capoeira miss from `.ufo/waves/round-71/w1/ScoutOpenSourcesC.md` and w1 evidence; reconstruct the exact CDX query the seat ran, the slug probed, and why `capoeira-circle-00892` was never tried; establish the failure class precisely enough that QUALITY 21 (draft text: *probe the canonical/redirect slug in CDX before ruling 'no capture'*) actually prevents it, naming the records a scout must file for the criterion to be checkable later.

All commands below were re-run today (2026-10-25); outputs are quoted verbatim from this seat's terminal. Downloads live in `/tmp/RevengerCapoeira/` (`cdx-capoeira-00892.txt`, `cdx-capoeira-circle-00892.txt`, `cdx-prefix.txt`, `cdx-wild-collapse.txt`, `cap-20171208155324.html`, `cap-01262.html`, `live-canonical.html`, `live-probed.html`).

## 1. Reconstructed sequence (what the round-71 seat actually did)

Source: transcript `history://L1Kotodama71.ScoutOpenSourcesC` (parked, readable) plus the filed report `.ufo/waves/round-71/w1/ScoutOpenSourcesC.md`.

1. **The dispatch named no URLs.** The round-71 w1 spec prompt for ScoutOpenSourcesC (verified in `spec.json` items/2 and the transcript's first user message) says only "open candidate sources … open the live URL with a plain curl/read". Every candidate URL, including every UNESCO element URL, was composed by the seat.
2. **First probe batch already contained the guessed slug.** The seat's first network bash (transcript, 5th assistant turn) curled `https://ich.unesco.org/en/RL/tango-00258`, `https://ich.unesco.org/en/RL/capoeira-00892`, `https://ich.unesco.org/en/RL/breaking-02055` (the `read` tool then fetched the same three). **Before any web_search ran.** The transcript's seven `web_search` calls are: breaking (`site:ich.unesco.org breaking element …`), wisdomlib natyashastra, archive.org Sachs, UChicago Hanna, Indiana UP Royce, Routledge Barba, wisdomlib abhinaya. **No search for the Capoeira element URL was ever run.**
3. **All three live URLs returned the CAPTCHA challenge** ("testing whether you are a human visitor"). Per dispatch, challenge ⇒ reject live, flip to Wayback.
4. **Wayback availability probe.** Transcript 8th turn: `bash … declare -A urls=( [tango]="https://ich.unesco.org/en/RL/tango-00258" [capoeira]="https://ich.unesco.org/en/R…` (23 lines out) — availability-API style check on the *same composed URLs*. Re-run today:

   ```
   GET https://archive.org/wayback/available?url=ich.unesco.org/en/RL/capoeira-00892
   → {"url": "ich.unesco.org/en/RL/capoeira-00892", "archived_snapshots": {}}
   GET https://archive.org/wayback/available?url=ich.unesco.org/en/RL/capoeira-circle-00892
   → {"archived_snapshots": {"closest": {"status": "200", "available": true,
     "url": "http://web.archive.org/web/20260907015854/https://ich.unesco.org/en/RL/capoeira-circle-00892", …}}}
   ```

   The miss reproduced exactly: availability was queried only on the wrong slug and returned empty.
5. **CDX wildcard query** (transcript 10th turn, output 32 lines covering three patterns):
   reconstructed command shape:
   ```
   for pat in "ich.unesco.org/en/RL/capoeira*" "ich.unesco.org/en/RL/breaking*" "royalacademyofdance.org/benesh*"; do
     curl -s "http://web.archive.org/cdx/search/cdx?url=$pat&output=text&collapse=urlkey"; done
   ```
   (The transcript later shows the identical explicit form for oruro: `curl -s --max-time 40 "http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/c…`, confirming the endpoint/shape. Exact `collapse`/`limit` params of the capoeira call are truncated in the transcript; see §3 for why every variant matters.)
6. **The seat fetched one wildcard hit**: `https://web.archive.org/web/20250625015345/https://ich.unesco.org/en/RL/capoeira-01262` (149 lines) — re-fetched today, its `<title>` is **"Basel Carnival - UNESCO Intangible Cultural Heritage"**.
7. **Filed reject** (`ScoutOpenSourcesC.md`, "Rejected / unreachable candidates"):
   > **Capoeira (UNESCO element 00892)** — no Wayback capture under that URL; CDX wildcard only surfaces `capoeira-` stub captures and the 2017 Basel Carnival page (element id collision 01262 ≠ capoeira). Unverifiable; **flip: Flamenco (row 5).**

   Note: **the report never prints the probed URL.** "that URL" is unnamed; `capoeira-00892` appears only in sibling seat `ExecSOURCESRowTemplate.md`'s illustrative sample row (`https://ich.unesco.org/en/RL/capoeira-00892`), which that seat flagged as "fields chosen for the assignment, not scout-validated candidates" — i.e. the same guessed slug propagated independently.

## 2. Ground truth (re-probed today, 2026-10-25)

| probe | result |
|---|---|
| `curl -sI https://ich.unesco.org/en/RL/capoeira-00892` (probed slug) | **HTTP 200**, body = challenge wall ("testing whether you are a human visitor"), **no redirect** |
| `curl -sI https://ich.unesco.org/en/RL/capoeira-circle-00892` (canonical) | **HTTP 200**, same challenge wall, no redirect |
| CDX exact `url=ich.unesco.org/en/RL/capoeira-00892` | **0 rows** |
| CDX exact `url=ich.unesco.org/en/RL/capoeira-circle-00892` | **141 rows, 135 with status 200**; earliest **20170513162348** (200), then 20171120140510, **20171208155324**; latest 200 = **20260907015854** — the three earliest are exactly the timestamps cited in claims.json / w2-spec (`20170513162348/20171120140510/20171208155324`) |
| fetch `…/web/20171208155324/https://ich.unesco.org/en/RL/capoeira-circle-00892` | serves real content: `<title>Capoeira circle - intangible heritage - Culture Sector - UNESCO</title>`; contains "simultaneously a fight and a dance" |
| CDX `url=ich.unesco.org/en/RL/capoeira-01262` fetch (20250625015345) | `<title>Basel Carnival - UNESCO Intangible Cultural Heritage</title>` |

So the round-72 correction is fully substantiated: **live 200 (behind challenge) + CDX captures under `capoeira-circle-00892` since 2017**, and the round-71 ruling "no Wayback capture" is false for the element.

### The decisive detail: the wildcard the seat ran *did* surface the canonical slug

Re-running the seat's wildcard in every plausible shape, **all** responses contain a `capoeira-circle-00892` row:

- `?url=ich.unesco.org/en/RL/capoeira*&output=text&collapse=urlkey` → 16 urlkeys, including `org,unesco,ich)/en/rl/capoeira-circle-00892 20170513162348 … 200 …`
- `?url=ich.unesco.org/en/RL/capoeira-*&output=text&collapse=urlkey` → identical set
- `?url=ich.unesco.org/en/RL/capoeira&matchType=prefix&output=text` (first 200 rows) → includes the canonical captures

The filed claim "CDX wildcard only surfaces `capoeira-` stub captures and the 2017 Basel Carnival page" is **contradicted by the CDX data the seat itself queried**: `capoeira-circle-00892` was in that output (alongside near-miss urlkeys like `capoeira-in-brazil-00892`, `capoeira-circle-of-brazil-01005`, `capoeira-circle-01007`). Either the seat's query had a further narrowing parameter not visible in the truncated transcript (unlikely to remove the canonical line — exact, prefix, and collapsed variants all retain it), or the seat summarized 32 lines of urlkeys from memory and dropped the one line that mattered. Because no query text or raw output was filed, this cannot be settled from the record — which is itself the finding (§4).

### Why the wrong slug was never detected live

`ich.unesco.org` is **id-keyed**: the numeric element id in the path selects the page; the slug text is decorative. Proof the seat held in its own hands: the `capoeira-01262` capture serves *Basel Carnival* content under a `capoeira-` slug. Corollaries: (a) a wrong slug returns HTTP 200 with the challenge, never 404 and never a redirect — so the live probe gave **zero signal** that `capoeira-00892` was not the canonical URL; (b) Wayback crawlers archive under the canonical slug, so the guessed slug has no captures **even though the element is heavily archived** (135 × 200). A "no capture" ruling on the guessed slug was guaranteed to be wrong here, and the site's architecture announced it — the Basel Carnival title was the tell.

## 3. Why `capoeira-circle-00892` was never tried

- **Not from a search result.** No search engine result naming any Capoeira UNESCO URL was ever fetched; the only UNESCO-related search was for *breaking*, and it ran after the Capoeira probes. (Transcript-verified.)
- **Not from the source's own page.** The element's own page was never readable (challenge wall on every probe, correct or incorrect), and no UNESCO element listing (e.g. the inscribed-elements index, itself available via Wayback) was consulted.
- **Composed by pattern.** The seat knew the element id 00892 and the short name "Capoeira", and built `{short-name}-{id}` = `capoeira-00892` — dropping the element's full official name *"Capoeira circle"*. The same pattern produced the hallucinated `breaking-02055` for a non-inscribed element. The element id itself was correct; the slug text was an unverified completion. [INFERENCE — marked as such: the transcript cannot show the seat's internal origin of "00892", but since no external lookup of it occurs anywhere in the transcript, prior knowledge is the only remaining source.]
- All six *other* UNESCO rows (tango-00258, mevlevi-sema-ceremony-00100, chhau-dance-00337, carnival-of-oruro-00003, flamenco-00363, talchum-mask-dance-drama-in-the-republic-of-korea-01742) carry canonical full-name slugs — because for those, the seat verified captures under the composed slug and never needed to reconcile. Capoeira failed the compose-and-pray check, and the seat stopped at "my slug has no captures" instead of asking "is my slug the canonical one?"

## 4. The failure class, stated precisely

**Class: unprovenanced-URL negative ruling.** A scout composed a URL by pattern (no search, no listing, no source-page confirmation), probed it live (HTTP 200 challenge — uninformative), queried Wayback on exactly that slug (empty), ran a wildcard CDX query whose output actually contained the canonical slug's captures, filed a summary of that output that omitted them, and ruled the candidate "unverifiable — no capture". The ruling was **checkable by no one**: the filed record contains neither the probed URL, nor the CDX query, nor its raw output, nor any canonical-URL candidate. Every downstream consumer (lesson `:36` "Capoeira (no capture; flip: Flamenco)", Gate table, round-71 report) repeated the ruling; no round-71 w2 seat re-probed it (verified: zero `capoeira` hits in `.ufo/waves/round-71/w2/`). The miss survived the Gate purely because the record could not be re-run.

Two compounding defects, either of which alone would have prevented the miss:
1. **Provenance defect** — the URL was self-composed and never reconciled against the source's own naming (search result, listing page, or archived page), on a site where slug errors are invisible to live probes (200-challenge, id-keyed resolution, no redirect).
2. **Record defect** — the negative ruling was filed as prose ("only surfaces stubs") instead of the raw urlkey list, which contained the answer.

## 5. What QUALITY 21 must require for the criterion to be checkable

Draft criterion text under consideration: *"probe the canonical/redirect slug in CDX before ruling 'no capture'; every Gate reject records its URL."* The probe alone would not have saved round 71 unless the word *canonical* is operationalized and the record is filed machine-checkably. Required minimum record for any scout reject/accept that involves a composed-or-derived URL:

1. **Probed URL, verbatim** (scheme, host, full path) — in the reject line, not just "that URL". Check: a reviewer can `grep` the report and re-fetch the exact byte string.
2. **Provenance of the URL**, one of `{search-result, listing-page, source-page, composed-by-pattern}` with the search result / page named. Composed-by-pattern is permitted but must be declared as composed — that declaration is what triggers the canonical-slug reconciliation step.
3. **Live-probe result as (status, body-signal, redirect-target)**: HTTP status alone is meaningless on challenge-walled hosts (200-challenge ≡ 200-content); the record must state whether content or a challenge wall was served, and the redirect target (`Location`) if any — or "no redirect".
4. **Exact CDX query URL(s)** (endpoint + all params, incl. `matchType`/`collapse`/`limit`) **and the raw returned urlkeys** (or at minimum: row count, the distinct urlkeys, earliest/latest 200 timestamps). A prose summary of CDX output ("only stubs") is not a record — that is precisely what failed here: the wildcard output contained `capoeira-circle-00892` and the prose dropped it.
5. **Canonical-slug probe before the ruling**: the canonical element URL as evidenced by the source's own naming (search result snippet, listing page, or the title of any id-matching capture), plus the CDX exact-query result for *that* URL. The ruling must be phrased per-URL: "no capture under `<exact URL>`" — never about the element.
6. **Slug-decoupling note for id-keyed sites**: where the seat observed (or the host's behavior shows) that the path slug is decorative and the numeric id selects the content — the `capoeira-01262` → "Basel Carnival" capture was exactly such evidence — absence of captures under one slug variant is not element-level absence, and the canonical slug must be probed.

With 1–4 filed, a gate reviewer can re-run the identical queries in-round (minutes, curl only) — round 72's `ScoutCapoeiraReopen` and this seat's re-probe demonstrate the cost is under five minutes. With 5–6 filed, the ruling "no capture" cannot be made from a composed slug at all: either the canonical slug yields captures (admit via capture), or the canonical slug genuinely has none (ruling is now about a URL the source itself endorses). Suggested tightening of the draft text:

> **21. No-capture rulings name their URL and prove canonicality** — a Gate reject of the form "no capture / unverifiable" must record: the exact probed URL; the URL's provenance (`search-result` / `listing-page` / `source-page` / `composed-by-pattern`, with the source named); the live probe's (status, challenge-wall?, redirect target); the exact CDX query URL(s) with raw urlkeys or (count, earliest, latest); and a CDX exact-query on the canonical slug taken from the source's own naming — probed first for composed-by-pattern URLs. On hosts where the numeric id selects content (observed: ich.unesco.org serves Basel Carnival at `/en/RL/capoeira-01262`), absence under one slug variant is not evidence about the element. Grounded in the round-71 Capoeira miss (`.ufo/waves/round-72/w1/RevengerCapoeira.md`): `capoeira-00892` was composed, probed (200-challenge, no redirect), CDX-empty; the wildcard CDX output contained `capoeira-circle-00892` (135 × 200, 2017-05-13 → 2026-09-07) but the filed prose summary omitted it.

## 6. Confidence

- Probed slug = `https://ich.unesco.org/en/RL/capoeira-00892`: **certain** (transcript first batch; independently echoed in ExecSOURCESRowTemplate's sample row).
- Exact CDX query string: **high-confidence reconstruction** — endpoint, wildcard pattern, and loop shape are transcript-visible; `collapse`/`output` params inferred from the 32-line output size and the seat's later oruro query (identical explicit form). Immaterial to the finding: every param variant returns the canonical urlkey.
- "Never from a search result / source page": **certain** (transcript-complete enumeration of the seat's searches and reads).
- Origin of element id 00892: **inference** (prior knowledge), flagged above.
- Ground-truth captures/live behavior: **certain** (re-probed this seat, outputs quoted, artifacts in `/tmp/RevengerCapoeira/`).

## Tooling

No tools installed or updated. Network probes only: `curl` against `ich.unesco.org`, `web.archive.org/cdx`, `archive.org/wayback/available`; `read` for transcript/history and lane files; `grep`/`python3` (stdlib, for spec/prompt extraction). Downloads (named): CDX text for both slugs + prefix/wildcard variants, the 2017 canonical capture, the `capoeira-01262` Basel Carnival capture, and both live challenge-wall bodies — all under `/tmp/RevengerCapoeira/`. No lane or fleet files were modified by this seat.
