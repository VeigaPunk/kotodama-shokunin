# R10-C17 — Reviewer of worker C07's culture-material entry (author-side review)

- reviewer scope: `reports/round-10/coverage/review-C07.md` only. No corpus, ledger, bookkeeping, canon, or promotion edits. Author-side review evidence only; not an admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one per authored entry (poll for it, max 20 min): verify frontmatter completeness, source resolvability (re-run the cited command or open the cited path/URL), no filler, no duplication of an existing entry; verdict `reports/round-10/coverage/review-<id>.md`").
- **Correction record (this file was rewritten in place; the superseded bytes are preserved at `reports/round-10/coverage/review-C08.md`).** At 21:32Z the culture-material partition went 16 → 17 files and C07 had filed no fragment; this seat assumed the newly-landed `transport-mobility-lexicon.md` was C07's entry and reviewed it under this filename. That attribution was **wrong**: `reports/round-10/coverage/C08.md` (filed 18:28 local, i.e. *before* this review opened) names `transport-mobility-lexicon.md` as **C08's** entry, and `reports/round-10/coverage/C07.md` (filed 18:38) names `vessel-container-lexicon.md` as C07's. The transport review was re-filed unchanged under its correct seat as `review-C08.md`; this file now reviews C07's actual artifact. **Lesson recorded:** "which entry belongs to which seat" must be read off the author's own fragment or a pre-existing sibling fragment — partition file-count deltas do not identify authorship, and reviewer seats that assume otherwise mis-file whole reviews.
- C07 is the first culture-material author (`R10-C01..C10` seat split: linguistics ×3 = C01–C03, myth-symbol ×3 = C04–C06, culture-material ×2 = C07–C08, verification ×2 = C09–C10).
- date: 2026-10-17 (all times UTC; local = UTC-03:00). Tree at review: `e3a1ec9435787328ac9f828f96cb6390e4916b8f`, dirty from concurrent shards. Review window ≈21:26–21:42Z.
- baseline: round-10 declared revision `9dc18ec1339bffd6f81e74f1a5742464ef578749` (`reports/round-10/claims.json`).

## 0. Review status — LANDED, reviewed

**Artifact under review:** `corpus/knowledge/culture-material/vessel-container-lexicon.md` — 175 lines, 43,056 bytes, sha256 `073e7fc54b600a81a75e0db480f73597e2295f8daa317a74e9246846b5de2df3` (18:36 local = 21:36Z; hash matches the value C07's own fragment declares). Title: "Vessel and Container Lexicon — Pots, Jars, Baskets, Barrels: the Four Container Jobs, Vessel-Naming Grammar, Part-Naming, Ceramic Classes, and Containers as Chronometers".

**Verdict: 4 of 4 mandated checks pass. No defect found.** C07's fragment claims were independently reproduced rather than accepted — every count, DOI resolution, gate result and path citation below was re-run by this seat.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **pass** — 6/6 claimed Crossref DOIs reproduce exactly; URL 200 with byte-exact size; 23/23 path tokens resolve |
| no filler (gap named, real, delivered) | **pass** — gap sweep reproduces exactly, including the row-by-row hit inventory |
| no duplication of an existing entry | **pass** — no slug collision; max topic overlap J=0.066 |

## 1. Check 1 — frontmatter completeness: PASS

House profile = the five fields every committed entry carries, each exactly once in the head block. Instrument: `.scratch/c17-frontmatter-check.py`.

- `- topic:` L3, `- sources:` L4, `- couples:` L5, `- verified-at:` L6, `- recheck:` L7 — **each count=1**, all non-empty with inline content. Head block = L1–8; first `## ` at L9. No duplicate, missing, or placeholder field.
- `verified-at` is dated and genuinely scope-bearing: it enumerates the six Crossref resolutions, the OpenAlex book-record resolutions, the Krannert fetch, the partition sweep, and — importantly — the *negative* results (Met Museum page HTTP 429, not relied on; OED/books not re-consulted in full text).
- `recheck` names concrete triggers (capacity figures, firing-temperature ranges, celadon/porcelain etymologies) rather than a generic "when sources change".
- **Required decision-record section present and substantial:** `## 10. Decision record` L137, table **DR-1…DR-12** with four columns (decision / why / rejected alternative / evidence). The "rejected alternative" column is the part that makes this a decision record rather than a summary — e.g. DR-2 rejects "free mixing of all six strategies", DR-6 rejects "treating the found assemblage as the used assemblage". `## 12. Handoff note` L171 closes at the handoff per `corpus/QUALITY.md` §5.
- **Instrument note (false positive recorded so a later reviewer does not repeat it):** my placeholder sweep flagged `verified-at` for containing `<DOI>`. That is literal prose (`Crossref api.crossref.org/works/<DOI>`), not a placeholder token. A reviewer whose check is "does the value contain angle brackets" will mis-file this entry.
- Lane gate re-run by this seat: `python3 tools/gates/provenance-audit.py corpus/knowledge/culture-material/vessel-container-lexicon.md` → `INFO to-verify-count: … 16 mark(s) on 12 line(s)` / `INFO scan: files=1 marks=16 mark-lines=12 findings=0 blocked=0`, **exit 0** — reproduces C07's fragment §3 claim exactly.

## 2. Check 2 — source resolvability: PASS

### 2.1 The six claimed Crossref resolutions — all six reproduce exactly

Re-run by this seat against `api.crossref.org/works/<DOI>` (2026-10-17), comparing title / venue / date to C07's fragment §4 and the entry's `verified-at`:

| DOI | resolved title | venue | date | vs claim |
|---|---|---|---|---|
| `10.1126/science.1218643` | Early Pottery at 20,000 Years Ago in Xianrendong Cave, China | Science | 2012-06-29 | matches |
| `10.1023/A:1026558503986` | Materializing Identities: An African Perspective | J. Archaeological Method and Theory | 2000-09 | matches |
| `10.1017/s0026749x00009975` | Western Zhou Ritual Bronzes … (Rawson review) | Modern Asian Studies | 1992-07 | matches |
| `10.1086/ajs40037281` | *Cretan Bronze Age Pithoi* (Christakis review) | American Journal of Archaeology | 2007-04-01 | matches |
| `10.1017/s0003581500021302` | Arretine and Samian Pottery (Johns) | The Antiquaries Journal | 1972-09 | matches |
| `10.1525/aa.1980.82.1.02a00800` | Basketry Technology (Adovasio review) | American Anthropologist | 1980-03 | matches |

Six for six, including the two this seat had not been shown in the fragment's headline list. **No fabricated DOI.**

### 2.2 URL access — byte-exact reproduction

`https://kam.illinois.edu/exhibition/celadon-and-ox-blood-ceramics-china-and-korea` → `code=200 bytes=42254`. C07's fragment claims "HTTP 200, 42,254 bytes"; the size matches **to the byte**, which is stronger evidence than a bare 200. Both content uses were located in the fetched page:

- celadon etymology plurality: page gives the Saladin (al-Nasir Salah al-Din, 1171) leg *and* the L'Astrée/Céladon leg ("a character named Céladon who wears grey-green ribbons") — the entry's "at least three proposals … lists the plurality and calls the origin unknown" is a faithful reading.
- the gold-repaired Goryeo object: page carries "Celadon bowl, Korean, Goryeo (Koryo) Dynasty, 918–1392. Ceramic with gold repair. Gift of Barbara B. Camp **1997-17-2**" — the entry's object number and dating are exact.

### 2.3 In-corpus path citations — 23/23 resolve, `missing: []`

Re-derived independently by this seat over the `couples` line and body: 23 distinct partition-relative `.md` tokens, all resolving on disk (`.scratch/` resolver; `MISSING: []`), reproducing C07's fragment §3 claim. Spot-opened and confirmed to support their cited use: `trade-economy-lexicon.md` (measures/money), `craft-artisan-lexicon.md` (potter's stamp typology), `material-culture-inference-method.md` (inference ladder, formation processes), `to-verify-triage-protocol.md` (DR-12's routing target), `era-periodization-models.md` (DR-8's period-naming logic), and the same-round sibling `transport-mobility-lexicon.md` (cross-checked in §9 of the entry for the "two unrelated wheels" claim).

### 2.4 Honesty of the unresolved set

The entry does not overclaim. 16 `to-verify` marks on 12 lines, concentrated where the source work genuinely was not done: OED etymology legs, capacity/firing figures, celadon and porcelain etymologies, the kintsugi anecdote, per-period Chinese/Japanese size-class mappings, per-name antiquity of Greek vase names. Each routes through `to-verify-triage-protocol.md` per DR-12. `verified-at` and §12 both state that page-level checks of Rice, Shepard, Kerr & Wood, Vainker, Habu, Wilkinson, Bagley and Rawson were **not** performed — record-level verification only, declared as such. This is the behaviour the corpus asks for: the limit is named rather than the claim being softened.

## 3. Check 3 — no filler: PASS

- **The gap is named and its sweep is exact.** The entry's §1 heading is itself the gap statement ("The gap this entry fills — the container domain was missing from this partition") plus an inline "Gap filled: the container/vessel domain." This seat re-ran the sweep command verbatim and **reproduced every row** — including the one where a careless check would have gone wrong:

| keyword | C07 claim (16 committed files) | this seat's re-run (16 pre-round-10 files) | verdict |
|---|---|---|---|
| amphora | 0 | 0 | match |
| basketry | 0 | 0 | match |
| wheel-thrown | 0 | 0 | match |
| pottery | 1 | 1 | match |
| ceramic | 2 | 2 | match |
| kiln | 2 | 2 | match |
| vessel | 3 | 3 | match |
| container | 3 | 3 | match |

  My first pass read `vessel` as 2; the third hit is the **anatomy sense** ("vessel" in a blood/body context), which is exactly the qualifier the entry's own table records. The entry predicted its reviewer's mistake and pre-empted it.
- **The gap is real, not a rounding of an existing file.** The entry owns the *thing itself* (what containers are, what they are called, what their parts are called, the material vocabulary, what a container can date) and explicitly delegates the three adjacent domains to named siblings — measures/money to `trade-economy-lexicon.md`, the potter's stamp to `craft-artisan-lexicon.md`, the inference ladder and the "pots≠people" discredit to `material-culture-inference-method.md`. Each delegation is cited, not restated.
- **It delivers.** §2 four-job typology, §3 six naming strategies with attested Greek/Chinese/Japanese/English families, §4 body-metaphor part-naming table, §5 container→unit→money metonymy, §6 ceramic ladder with per-rung vocabulary, §7 non-ceramic inventory and the perishable/survival ratio, §8 containers as documents and chronometers, §9 ten-item calibration shelf, §10 twelve decision rows, §11 build order + a non-canon worked micro-example.
- **`corpus/QUALITY.md` item by item:** provenance — cited and re-verified above; calibration — §9 is unusually strong for this corpus (see §4 below); coupling — `couples` L5 plus per-section sibling pointers; usability — five tables, a numbered build order, and a worked example; canon hygiene — §11's worked example is labelled NON-CANON in bold, §12 states "It decides nothing about any world."

## 4. Check 4 — no duplication: PASS

- **Slug collision:** none. `vessel-container-lexicon.md` was absent from the 179-slug baseline; no `-b` suffix needed.
- **Topic overlap:** highest Jaccard against any committed entry is **J=0.066** (`myth-symbol/direction-symbolism.md` — unrelated domain), then 0.052 / 0.049 / 0.049; against its own same-round sibling `transport-mobility-lexicon.md` it is **J=0.045** (`.scratch/c17-dup-check.py`). No near-duplicate.
- **Same-round sibling separation is clean and mutual:** C08's fragment §2 records "Distinctness from C07: not observable at write time (no C07 fragment existed)"; C07's fragment §2 records seeing C08's entry before writing and coupling to it ("this entry couples to it for what cargo rides in"). Both landed files confirm it: transport owns routes/vehicles/draft/wayfinding; vessel owns the container. The two do not share a section.
- **Calibration cross-check is a coupling, not a duplication:** §9's "the two wheels are unrelated" points the reader *to* `transport-mobility-lexicon.md` rather than restating its wheel material — the correct move when two same-round entries touch one fact.

## 5. Notable strength worth flagging to the parent

§9 ("Calibration — contested, discredited, and apocryphal") does work most entries in this corpus do not: it separates **discredited** ("pots = people" as a default; pottery as a farming/sedentism marker — killed by Xianrendong at ~20,000 BP predating agriculture), **genuinely unsettled** (celadon's etymology, three competing proposals), **false friends** (Egyptian faience vs European faience; terra sigillata the Roman ware vs the modern slip recipe), **legend-grade** (the kintsugi Ashikaga anecdote, with the *object* evidence separated from the *story*), and **etic-vs-emic** (Dressel numbers are modern typology, not ancient vocabulary — carried into DR-9 as a world-bible rule). The "rejected alternative" column in the DR table turns the decision record into an anti-silent-default device. This is the `QUALITY.md` §2 bar met with room to spare.

## 6. Findings

**None.** No defect found against the four mandated checks; C07's fragment claims all reproduced. The only defect this seat found anywhere in the culture-material pair belongs to C08's entry and is filed at `review-C08.md` §2.4 / §6 (a mislinked Merriam-Webster URL — link text "coach", target `/dictionary/coachable`).

## 7. Limits of this review

- Author-side review, not independent promotion verification (lane rule, `AGENTS.md`). This seat verified that C07's **claims about its own evidence are true** — it re-ran the commands, re-resolved the DOIs, re-fetched the URL, and reproduced the sweep. It did **not** read the underlying scholarly works (Rice 1987, Shepard 1956, Habu 2004, Gosselain 2000, Peacock & Williams 1986, Christakis 2005, Zupko 1977 and the rest); agreement here means "the entry faithfully reports records this seat independently resolved", not "the ceramic history is settled".
- The six DOI resolutions were confirmed at **record level** (title/venue/date), not by reading the articles. The entry itself declares this same limit, so this review confirms the declaration rather than exceeding it.
- `.scratch/` is shared by all live workers; instruments are `c17-`-prefixed (the prefix records instrument origin, not a seat claim). This seat wrote no corpus byte and made no commit.

FILES: reports/round-10/coverage/review-C07.md
