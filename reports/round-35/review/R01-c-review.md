- Seat: R01 | reviewer | claim C | date 2026-10-19 | baseline 4a7aede

# R01 — adversarial review of entry drafts C01–C05 (claim C, coverage)

**Assignment** (`reports/round-35/targets.json:324-329`, seat R01): *"Adversarial review of entries
1-5: source-pointer resolution re-checked independently, frontmatter re-read, no-fabrication hunt."*
Out path: `reports/round-35/review/R01-c-review.md`. Binding rules read at `targets.json:5-13` —
`:6` write only the assigned out path, `:8` corpus entries are integrator-applied, `:9` **no network**
this wave, `:10` never execute a filed round runner in-tree, `:12` missing dependency → do what you
can and record the owed path.

**Review surface.** The drafts are *fragments*: each carries the full entry bytes inside one fenced
block. This review binds to the **extracted entry bytes** (digest-pinned in §2), not to the fragments'
prose, and not to `corpus/knowledge/**` (no entry has landed: `git status --porcelain corpus/` →
empty, §2.3). Per `targets.json:8` the integrator applies the bytes; **any post-application edit
invalidates every verdict below** — re-run `.scratch/r01-review.py` on the landed file.

## 0. Verdicts

| seat | intended path (draft's own declaration) | entry bytes | mechanical legs (my instrument) | verdict |
|---|---|---|---|---|
| C01 | `corpus/knowledge/culture-material/mortuary-material-culture.md` | `94cd206a…` | gap ✓ decision ✓ pointers 0-unresolved couples 0-unresolved | **pass with 1 minor defect** (§3.1) |
| C02 | `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md` | `0b382526…` | gap ✓ decision ✓ pointers 0-unresolved couples 0-unresolved | **pass clean** (§3.2) |
| C03 | slug `writing-media-and-surface-economy` declared; explicit target path **not stated** | `570b82ea…` | gap ✓ decision ✓ pointers 0-unresolved couples 0-unresolved; 4/4 digest pins byte-matched | **pass clean** (§3.3) |
| C04 | `corpus/knowledge/culture-material/timekeeping-instruments.md` | `9805c0b8…` | gap ✓ decision ✓ pointers 0-unresolved couples 0-unresolved | **pass clean** (§3.4) |
| C05 | `corpus/knowledge/culture-material/furniture-interior-lexicon.md` | `9dddc9d1…` | gap ✓ decision ✓ **1 source pointer mechanically unresolved (a documented inline repair)**; couples 0-unresolved | **pass with 1 low defect + 1 frontmatter-floor finding** (§3.5) |

No fabrication found in any of the five: no URL is claimed as fetched this round, every external work
is an inherited citation, and every unresolved external item carries `(to-verify)` in-file (§3.6).
Cross-entry findings that the integrator must disposition: **F4** (frontmatter field-name contract
splits across the five), **F5** (C12's staging regex extracts zero blocks from C01/C03/C05), **F6**
(P01's topic table does not match the landed drafts' topics), **F7** (the two filed audit instruments
disagree on the same bytes).

## 1. Method — instruments, controls, and one correction

| instrument | what it does | self-test |
|---|---|---|
| `.scratch/r01-extract.py` (this seat) | extracts the fenced entry block, pins its digest | reports every fence with size/tag so the pick is auditable |
| `.scratch/r01-review.py` (this seat) | independent legs: head-field census (exactly-once, placeholder sweep), gap leg, decision leg, per-bullet source locator/ref resolution + digest-pin classification, couples resolution, same-day-network-claim hunt, DOI/URL/ISBN extraction with cross-lane recurrence, topic-Jaccard duplication screen | **14/14 controls pass**, incl. negative controls: phantom path, fabricated 64-hex pin, same-day fetch claim, placeholder fields, missing gap/decision |
| `.scratch/r01-anchors.py` (this seat) | resolves every `<file>.md:<line>` citation, flags out-of-bounds lines, prints the cited line text | **181 line-citations** across the five drafts (74/34/24/17/32), 0 out-of-bounds, 0 unresolved files, §3 |
| `.scratch/r01-gapcheck.py` (this seat) | tests the claimed gap's distinctive terms against the **baseline revision** (`git grep … 4a7aede -- corpus/knowledge/<part>`), so same-wave sibling drafts cannot fake a hit | validated on the r28 ceiling entry (known-real gap): its distinctive term `operation-constrained` → 0 baseline files |
| `reports/round-27/audit/entry-audit.py` (filed, read-only) | the strongest filed bar (filler, locator, ref resolution, digest laundering, couples, gap, decision) | **11/11 controls pass**; run on the extracted drafts only, never on corpus bytes |
| `reports/round-19/audit/entry-audit.py` (filed, read-only) | the earlier bar C03 cites as its own contract | run for divergence evidence only (§4.3) |

**Correction to my own first reading (recorded, not hidden).** My first couples pass ran against
extractions staged under `.scratch/r01-entries/`, where C03's `../culture-material/…` and C01/C02's
bare-basename refs read as unresolved — a **staging artifact of mine**, not an entry defect. Every
verdict in §3 uses a resolver that tries the entry's own directory, the lane root, `corpus/knowledge/`
and each partition (`r01-review.py:resolve_ref`); on those terms **all 134 couples refs across the
five drafts resolve** (48/22/20/25/19). §4.3 records the instrument divergence this exposed.

## 2. Baseline pins and preservation

2.1 **Census at baseline** (2026-10-19, HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`):
`for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
→ `21 19 18 29 20 94`; `ls corpus/knowledge/*/*.md | wc -l` → `201`. Reproduces `claims.json:26-27`
and P01's §1 (`plan/P01-c-plan.md:76-77`) exactly. My five drafts' partitions are the two named:
culture-material 18 → +6 (C01,C02,C03,C04,C05,C06) and myth-symbol 19 → +4 (C07–C10).

2.2 **Per-file digests pinned** before any landing: `sha256sum corpus/knowledge/culture-material/*.md
corpus/knowledge/myth-symbol/*.md corpus/README.md > .scratch/r01-baseline-digests.tsv` → 38 rows,
file digest `6434b18d1e1eee7547c4c7dfc43fbf96016852fc52574e64dd581e4d4931b1db`. Any in-place edit of
an existing entry is detectable by re-hashing against this list.

2.3 **Preservation observed.** `git status --porcelain corpus/` → empty at 08:33Z and again after all
five drafts had landed; `corpus/README.md:469` still `Total knowledge entries: 201.`,
`:473` footer `(total 201 files; directory totals 21/19/18/29/20/94)`; census re-run → unchanged
`21 19 18 29 20 94`. No draft author wrote a corpus byte; the two write surfaces remain owed to the
integrator (entries + README delta).

## 3. Per-entry review

Anchor digests: **fragment** = `reports/round-35/cov/C0N-entry-N.md`, **entry bytes** = the extracted
fenced block this review ran against (`.scratch/r01-entries/…`). All line numbers below are the
extracted entry's own lines.

### 3.1 C01 — mortuary material culture (fragment `3164d10d…`, entry `94cd206ac589ff67…`, 220 lines / 85,659 B)

- **Frontmatter**: 7 head fields (`topic`, `gap filled`, `sources`, `couples`, `source`,
  `verified-at`, `recheck`), each exactly once, no placeholder values. Claim-4 literal: 3/4
  (`scope` absent — see F4). House shape: 5/5.
- **Gap**: named twice (`- gap filled:` field + §1), and **real at baseline**: distinctive terms
  `mortuary`, `grave-goods`, `disposal`, `death-word` → **0 files** in `corpus/knowledge/culture-material`
  at `4a7aede` (my gapcheck); the nearest prior text is `ritual-liminality.md` (the rite side), which
  the entry cross-references rather than restates.
- **Decision record**: §10, 9 `DR-MMC-*` rows (grep `^| DR-` → 9).
- **Sources/pointers**: 32 bullets; **every cited path resolves** (0 unresolved); 74 `path:line`
  citations all in-bounds (0 out-of-bounds); 21/32 bullets satisfy the filed r27 locator regex — the
  11 misses are classical/legal loci without a 4-digit year (e.g. `Cicero, *De Legibus* 2.58–2.59`),
  10 of the 11 carrying `(to-verify)` (F3-adjacent, §4.3). Digest pins: none. Couples: 48 refs,
  0 unresolved.
- **Duplication**: topic-Jaccard max 0.105 (`culture-material/vessel-container-lexicon.md`) → no
  near-duplicate; slug `mortuary-material-culture` absent from the 201-file baseline.
- **Fabrication hunt**: no URL claimed as fetched; `verified-at` states "**in-corpus half measured,
  external half not fetched**" — the honest shape for a no-network wave. 42 `to-verify` occurrences /
  40 lines.
- **Finding R01-F8 (LOW)**: the source bullet at entry line 30 begins **`- Paul Barber? — no. The
  **substitution-arc** evidence: …`** — a drafting self-question left in the delivered bytes. The
  bullet's content is sourced and marked `to-verify`; the residue is cosmetic but it is in the bytes
  the integrator would apply.
- **Observation (informational)**: 85,659 B is ~2× the current house scale (P01 §0.4: 36–43 KB).
  Size is not a defect under `corpus/QUALITY.md`; recorded so no auditor reads it as a shape failure.

### 3.2 C02 — agrarian field-system lexicon (fragment `6746faf3…`, entry `0b382526227ae3f1…`, 188 lines / 36,945 B)

- **Frontmatter**: 7 fields (`gap`, `topic`, `sources`, `couples`, `source`, `verified-at`,
  `recheck`), exactly once each, no placeholders. Claim-4 literal 3/4 (`scope` absent). House 5/5.
- **Gap**: named (`- gap:` + §1 census) and **real at baseline**: `agrarian`, `parcel`, `tenure`,
  `food-as-meal` → 0 files; the entry's own §1 sweep table reproduces (I re-ran the same terms).
- **Decision record**: §11, 10 `DR-AG-*` rows.
- **Sources/pointers**: 2 bullets, **both satisfy the filed locator regex** (the only draft of the
  five that does); 0 unresolved refs; **34 `path:line` citations, all in-bounds**, and I re-read the
  cited lines independently — content matched in every spot-check: `cuisine-food-lexicon.md:17`
  (FAO 2026 ≈40 % of calories), `:26` (wet-rice water control), `:27` (Nunn & Qian 2011),
  `:157` (the 42 %→40 % calibration row); `calendar-festival-systems.md:52` (Akhet/Peret/Shemu),
  `:116` (`harvest stored → tithes, debts, assembly`), `:167` (festival-arc build step);
  `textile-technology.md:11` (fiber gate), `:76` (stink trades), `:83` (`Arabic *quṭn* → *cotton,
  algodón, algodão*`); `trade-economy-lexicon.md:17` (measures from body/substance/action/container);
  `transport-mobility-lexicon.md:29` (mobility as capacity) and `DR-TR-03` (exists, line 118);
  `vessel-container-lexicon.md:34` (STORAGE job row); `material-culture-inference-method.md:13,:33,
  :61,:66,:73,:75,:105` (Boserup/Alesina; flint-sickle gloss; cost gradients; energy/fuel;
  seasonality; the plough→gender chain, which line 75 does carry; the mechanism critiques);
  `austronesia-philippines-taiwan.md:109-126,:115-116` (*muyong–uma–payo*, *payo*/*uma* rows);
  `khmer-angkor.md:146-149` (incl. the `sre` row's "one word does not identify the source or scale");
  `nazca.md:37,:105` (puquio horizon; contested overreading). Couples: 22 refs, 0 unresolved.
- **Duplication**: topic-Jaccard max 0.082; slug absent from baseline.
- **Fabrication hunt**: 0 URLs, 0 DOIs; 38 `to-verify` occurrences / 26 lines; the fragment states
  "no network at seat time" and marks every external figure. **Verdict: the cleanest draft of the five.**
- Its own fragment also files the `- scope:` finding (§Findings 2 there) and the staging-fence hazard
  (§Findings 4 there); both are confirmed independently below (F4, F5).

### 3.3 C03 — writing media and the surface economy (fragment `82af002e…`, entry `570b82ea616272ec…`, 202 lines / 46,135 B)

- **Frontmatter**: **9 fields** — the house five plus `gap filled`, `source`, and **`- scope:`** and
  **`- calibration:`**. Claim-4 literal **4/4**; house 5/5. `- scope:` is novel (0/201 corpus-wide,
  §4.1); `- calibration:` is not (10/201 corpus files carry it).
- **Gap**: named, and **real at baseline**: `media-blind`, `parchment` → 0 files; the delegate clause
  it cites (`linguistics/writing-systems.md:7` couples line) resolves and does delegate the medium
  economy outward, as the entry claims.
- **Decision record**: §10, **13 rows, ids `DR-1…DR-11`** (grep `^| DR-` → 13). Note: my instrument's
  DR-id regex expects a two-segment id (`DR-XX-01`) and first read 0 here — corrected by direct grep;
  recorded because an auditor using that pattern will mis-read C03's ids.
- **Sources/pointers**: 22 bullets, 17 satisfy the filed r27 locator regex; the 5 misses are 4
  `` `path.md:92,121` ``-style citations (path resolves; the regex does not accept the `:line` suffix —
  F3/§4.3) plus 1 Pliny locus marked `to-verify`. 0 unresolved refs; 24 `path:line` citations, all
  in-bounds. **4/4 sha256 pins byte-matched independently by this seat**: `writing-systems.md`
  `76263260…`, `examples/culture-d4/components/03-orthography.yml` `0f2ff454…`,
  `material-culture-inference-method.md` `7cc44399…`, `verification/calibration-registry.md`
  `cf7cceee…` — this is the strongest provenance evidence in the five drafts. Couples: 20 refs,
  0 unresolved (all resolve once the entry is read from its intended partition directory; §4.3).
- **Duplication**: topic-Jaccard max 0.073; slug absent from baseline.
- **Fabrication hunt**: 0 URLs/DOIs claimed; 24 `to-verify` occurrences / 22 lines; `verified-at`
  states the in-repo checks were mechanical at HEAD and no external work was inspected.
- **Owed item (integrator)**: the fragment declares the slug but **no explicit target path**; the
  path used in this review (`corpus/knowledge/culture-material/writing-media-and-surface-economy.md`)
  is the integrator's to confirm, and the README row must then carry its `- topic:` byte-equal.

### 3.4 C04 — timekeeping material culture (fragment `c828b06f…`, entry `9805c0b854334ed3…`, 141 lines / 40,234 B)

- **Churn record (R01-F1)**: the fragment was revised **mid-review** — `6d5e7832…` (first read) →
  `c828b06f…` (re-read 08:5xZ). The **entry bytes are unchanged** (`9805c0b8…` in both revisions);
  the revision added preamble material only (a 2-line fenced block naming the intended path).
  Verdicts bind to `9805c0b8…`; the fragment digest moved, so anyone re-reading the fragment must
  re-extract.
- **Frontmatter**: 8 fields incl. **both** `source` and `sources`, plus `- scope:`. Claim-4 literal
  **4/4**; house 5/5.
- **Gap**: named; **real at baseline**: `era-stamp`, `aksum-ethiopia`, `twelve-hour` → 0 files; the
  calendar/era siblings are cited as the boundary, not restated.
- **Decision record**: §11, 12 rows.
- **Sources/pointers**: **1 bullet** (a 3,983-char line carrying ~24 semicolon-separated works);
  0 unresolved refs; 17 `path:line` citations, all in-bounds; couples 25 refs, 0 unresolved.
- **Fabrication hunt**: 1 DOI — `10.1093/past/38.1.56` (Thompson 1967, *Past & Present* 38:56–97),
  **marked `(to-verify), not resolved this round`** in-line; 0 URLs; 33 `to-verify` occurrences /
  23 lines; `verified-at` states the in-repo readings and the no-network condition. The DOI's
  registrant prefix (`10.1093`, OUP) is consistent with the venue; **not re-fetched** (no network
  this wave — `targets.json:9`), so its resolution is `to-verify` exactly as the draft marks it.
- **Finding R01-F10 (LOW)**: the single-bullet shape makes the filed instruments' "every source
  bullet carries a locator" leg **vacuous** (1/1 trivially satisfied) while ~24 works sit inside the
  one line. Auditors should check per-work, not per-bullet (owner C12/C13/C14).
- **Duplication**: topic-Jaccard max 0.118; slug `timekeeping-instruments` absent from baseline.

### 3.5 C05 — furniture and the interior (fragment `d6f930b2…`, entry `9dddc9d1fb1a3175…`, 143 lines / 39,475 B)

- **Frontmatter**: **6 fields** — `topic`, `gap filled`, `sources`, `couples`, `verified-at`,
  `recheck`. **No singular `- source:`.** Claim-4 literal **2/4** (3/4 if the plural `sources:` is
  accepted as the source leg; the corpus carries `- source:` on 134/201 files, §4.1). House 5/5.
- **Gap**: named; **real at baseline**: `stool`, `mattress`, `bedstead`, `canopy`, `desk` → 0 files
  in the partition; the nearest text (`architecture-settlement-lexicon.md`, `adornment-body-codes.md`)
  is cited as the boundary.
- **Decision record**: §11, 12 `DR-FUR-*` rows.
- **Sources/pointers**: 8 bullets, 7 satisfy the filed locator regex (the miss is Shakespeare's will,
  1616 — a year the regex's 19xx/20xx class does not accept — marked `to-verify`). 32 `path:line`
  citations, all in-bounds. Couples 19 refs, 0 unresolved.
- **Finding R01-F2 (LOW)**: **one source pointer is mechanically unresolved in both filed
  instruments and in mine** — the bullet at entry line 13 contains
  `` `corpus/knowledge/era-periodization-models.md` → `corpus/knowledge/culture-material/era-periodization-models.md:6,31` ``.
  The first token lacks the `culture-material/` segment; the arrow immediately supplies the correct
  path, i.e. **it is a documented inline repair, not a fabricated pointer**. Verdict: the claim's
  "source pointers resolve" leg reads **red mechanically** on these bytes (r27: `refs_unres=1`,
  `bar=False`) and **green on the human reading**. The integrator should either keep it (a repair
  note is honest) and instruct auditors to read it as such, or delete the broken token; **it must not
  be filed as a fabrication**.
- **Fabrication hunt**: 0 URLs/DOIs; 31 `to-verify` occurrences / 26 lines; `verified-at` states
  explicitly "**no network access**: every in-repo pointer … re-checked".
- **Duplication**: topic-Jaccard max 0.089; slug `furniture-interior-lexicon` absent from baseline.

### 3.6 No-fabrication hunt — the block-level result

Across all five drafts: **0 URLs**, **1 DOI** (C04's Thompson, in-line `to-verify`), **0 ISBNs**;
no draft claims a fetch, download, or HTTP status for this round; every `verified-at` line either
records in-corpus commands run today or states the no-network condition and the resulting backlog.
The same-day-access check (`r01-review.py` network leg) fired only on in-corpus re-check language
("re-checked by `grep -n` on 2026-10-19"), which is a local operation, not a network claim. **No
invented source, no laundered citation, no fabricated digest found.** Every `to-verify` census:
C01 42/40 lines, C02 38/26, C03 24/22, C04 33/23, C05 31/26.

## 4. Cross-entry findings (integrator disposition required)

### 4.1 F4 — the frontmatter contract splits across the five drafts (MEDIUM–HIGH)

| draft | head fields | claim-4 literal (`source`/`verified-at`/`recheck`/`scope`) | house 5/5 |
|---|---|---|---|
| C01 | topic, gap filled, sources, couples, source, verified-at, recheck | **3/4** | yes |
| C02 | gap, topic, sources, couples, source, verified-at, recheck | **3/4** | yes |
| C03 | topic, gap filled, sources, **calibration**, couples, source, verified-at, recheck, **scope** | **4/4** | yes |
| C04 | topic, gap filled, sources, source, couples, verified-at, recheck, **scope** | **4/4** | yes |
| C05 | topic, gap filled, sources, couples, verified-at, recheck | **2/4** (3/4 if `sources` counts) | yes |

Evidence: my field census per draft; corpus-wide `grep -rl -- '^- scope:' corpus/knowledge/ | wc -l`
→ **0**; `grep -rl -- '^- source:' corpus/knowledge/ | wc -l` → **134** of 201; `- couples:` →
201/201. P01 reached the same reading independently (`plan/P01-c-plan.md:16-26`) and recommends the
4/4 leg be implemented against the **live** field names (`topic`/`sources`/`couples`/`verified-at`/
`recheck`) with `- topic:` read as the scope statement. `claims.json:29` names `scope`, which exists
nowhere in the corpus, and its "documented 3/4 class" escape hatch has no defined documentation
locus. **Owner: integrator, with S04/O08 implementing the validator leg**; the C block should not be
read as 10/10 on a field that three of five drafts do not carry (and one carries without the singular
`source` leg).

### 4.2 F5 — C12's staging regex extracts zero blocks from C01, C03 and C05 (HIGH)

C12's runbook tool extracts fragments with
`re.findall(r"^```(?:markdown|md)\s*$([\s\S]*?)^```\s*$", text, re.M)` and takes `blocks[0]`
(`reports/round-35/cov/C12-audit-runbook.md:766,773`). Replicating that regex **verbatim** against the
five fragments:

```
C01 fences: 19:```  26:```  42:````markdown  264:````  270:```  277:```  285:```  301:```   -> C12 blocks=0
C02 fences: 15:```markdown  195:```  203:```  …                                        -> C12 blocks=1 (37,793 B)
C03 fences: 35:````markdown  237:````  259:```  281:```                              -> C12 blocks=0
C04 fences: 11:```  13:```  17:```markdown  158:```                                  -> C12 blocks=1 (39,997 B)
C05 fences: 67:````markdown  211:````  251:```  253:```                              -> C12 blocks=0
```

C01/C03/C05 wrap the entry in a **four-backtick** fence, which the regex cannot match; those three
drafts would stage as "no fenced block" → `CANNOT-EVALUATE` under the runbook's own tool
(`C12-audit-runbook.md:932`), and the round's "10/10 audited clean" threshold is unreachable through
that path. C02 predicted this in its own fragment (§Findings 4). **Owner: C12** (accept 4+-backtick
fences; select the entry block, not `blocks[0]`); auditors C13/C14/C17 must state which extractor
produced the bytes they audited.

### 4.3 F7 — the two filed instruments disagree on the same bytes (MEDIUM)

Same extracted bytes, both instruments run by this seat:

| draft | r19 `src` / couples-unresolved | r27 `src` / `bar` | my instrument |
|---|---|---|---|
| C01 | 21/32 · 1 (`craft-artisan-lexicon.md`, bare basename) | 21/32 · bar=False | 0 unresolved; 48 couples resolved |
| C02 | 2/2 · 1 (`textile-technology.md`) | 2/2 · bar=True | 0 unresolved |
| C03 | 17/22 · 20 (`../culture-material/…` form) | 17/22 · bar=False | 0 unresolved; 20 couples resolved |
| C04 | **0/0** (its `- sources:` is a single inline line, not `  - ` bullets) · 25 couples ok | **1/1 · bar=True** | 1 bullet, 0 unresolved |
| C05 | 7/8 · 0 | 7/8 · **bar=False** (`refs_unres=1`) | 1 mechanically unresolved (documented repair) |

Two mechanisms: (a) **locator-regex gap** — the lane's own `` `path.md:12,34` `` citation form and
classical loci (`Cicero, *De Legibus* 2.58–2.59`) are not accepted by `LOC_RE`
(`reports/round-27/audit/entry-audit.py:65`), so C01/C03/C05 read `bar=False` although **every cited
path resolves** (my resolver: 0 unresolved in all five); (b) **resolver/couples-form divergence** —
r19's resolver (`reports/round-19/audit/entry-audit.py:83-92`) lacks r27's partition fallbacks, so
bare-basename and `../partition/file.md` couples refs read unresolved depending on staging root and
instrument version (r27's token regex starts matching after `../`, which is why it reads 0 there).
**Consequence: "10/10 new entries audited clean by two independent auditors" is instrument- and
staging-dependent.** C12 must pin the instrument, the locator regex, the resolver, and the staging
root; C13/C14/C17 must report which. **Owner: C12, with X03 reviewing the threshold's checkability.**

### 4.4 F6 — P01's topic table does not match the landed drafts' topics (HIGH, integrator's call)

`plan/P01-c-plan.md:108-119,375-386` assigns: C01 `timekeeping-instruments`, C02
`healing-material-culture`, C03 `games-and-play-material-culture`, C04 `bathing-and-body-hygiene`,
C05 `incense-and-aromatics`, C06 `light-and-fire-material-culture`, C07 `afterlife-and-eschatology`,
C08 `magic-and-witchcraft-systems`, C09 `sacred-geography-and-pilgrimage`, C10 `sacred-kingship`.
Landed: C01 mortuary material culture, C02 agrarian field-system, C03 writing media/surface economy,
C04 **timekeeping** (P01's C01 topic), C05 furniture/interior, C06 fire/fuel/light (≈ C06), C07
eschatology (≈ C07), C08 `sacred-kingship-mythic-charter` (P01's C10 topic), C09
`death-afterlife-eschatology` (P01: sacred-geography; **note its overlap with C07's topic — R02's
surface, flagged here only as a duplicate risk**), C10 (P01's sacred-kingship slot).
P01 landed at 08:32Z, after the drafts were authored under the missing-dependency rule (each draft
records this). **The partition allocation and the counting legs are unaffected** (6 culture-material +
4 myth-symbol → 24/23/211); what cannot be applied is P01's per-topic ownership boundaries, couples
minimums and calibration lists — the drafts' own gap sweeps substitute. **Owner: integrator** —
either accept the landed topic set as the de-facto plan (recording P01 §3 as superseded for topics,
and reconciling K01's candidate ranking), or require re-authoring; a half-and-half reading will file
false "topic mismatch" defects.

## 5. Findings table

| # | finding | severity | owner | status |
|---|---|---|---|---|
| R01-F2 | C05 entry line 13: `` `corpus/knowledge/era-periodization-models.md` → `…/culture-material/era-periodization-models.md:6,31` `` — first token mechanically unresolved; a documented inline repair | low | integrator / C13–C14 (read as repair, not fabrication) | open |
| R01-F3 | C05 carries no singular `- source:` → claim-4 literal 2/4 | medium | integrator (F4 normalization) | open |
| R01-F4 | frontmatter field-name contract splits across the five drafts (`scope` 0/201 corpus-wide; P01 §0.1 same reading) | medium–high | integrator + S04/O08 | open |
| R01-F5 | C12's staging regex extracts **0 blocks** from C01/C03/C05 (4-backtick fences; `blocks[0]`) | high | C12 | open |
| R01-F6 | P01's topic table ≠ landed topics (C01–C05, C08, C09); counts unaffected | high | integrator | open |
| R01-F7 | filed instruments disagree on the same bytes (r19 vs r27; locator regex; couples resolver/staging) | medium | C12 + X03 + C13/C14/C17 | open |
| R01-F8 | C01 entry line 30: drafting residue "`Paul Barber? — no.`" heads a source bullet | low | integrator (cosmetic) | open |
| R01-F10 | C04's single-bullet `- sources:` line makes the per-bullet locator leg vacuous (~24 works in one bullet) | low | C12/C13/C14 | open |
| R01-F1 | C04's fragment revised mid-review (`6d5e7832…` → `c828b06f…`); entry bytes unchanged (`9805c0b8…`) | informational | — | closed with evidence |
| R01-F11 | extracted-bytes boundary is extractor-dependent (my extractor vs C12's regex differ by boundary/trailing newline; both contain the full entry, identical final line) → the applied bytes' digest must be pinned | informational | integrator | open |

## 6. Limits

- **No network** (`targets.json:9`): no external source in any draft was re-fetched or independently
  resolved. URL/DOI claims were checked for *internal* consistency (syntax, registrant prefix,
  in-line `to-verify` marking, absence of same-day fetch claims) and for cross-lane recurrence
  (`git grep -F` per DOI: C04's single DOI → 0 prior occurrences). A DOI that resolves syntactically
  may still be wrong; the drafts' own `to-verify` marks carry that risk, and my review does not
  upgrade them.
- **Extraction dependence**: my verdicts bind to the bytes I extracted and pinned (§2, §3 headers).
  My C02 extraction (188 lines / 36,945 B) is corroborated by C02's own self-audit (187 lines /
  36,617 chars — the char/byte gap is CJK content) and contains all 12 `## ` sections; C12's regex
  reading of the same fragment is 181 lines / 37,793 B with the same final line. No verdict depends
  on the divergent boundary, but the integrator must pin the extraction rule (F11).
- **Author-side review, not independent promotion verification** (lane rule, `AGENTS.md`): this seat
  decides no admission, no promotion, no canon; it holds no corpus write and wrote only this file.
- **Not re-run**: the drafts' own cited commands (their gap sweeps) were re-derived by me from the
  baseline revision, not executed from their fragments; the filed instruments were run read-only and
  their self-tests re-verified (11/11) before use.
- Verdicts bind to the entry digests in §0; any post-application edit (or further fragment revision)
  invalidates them — re-run `.scratch/r01-review.py` on the landed file and re-hash against §2.2.

## Owed: none

All five entries of this seat's surface (C01–C05) landed inside the review window and are reviewed
above. Residual dependencies for the integrator, not owed by this seat: the ten applied entry bytes
+ the README delta (C11), and the round-35 validator legs (S04/O08).

## Citations

- `reports/round-35/targets.json:5-13` (shared rules: `:6` write scope, `:8` integrator applies
  entries, `:9` no network, `:10` F-C13-1), `:324-329` (seat R01).
- `reports/round-35/claims.json:20-36` (claim C: `:24` text incl. the `source / verified-at /
  recheck / scope` list, `:26-27` before-census, `:29` after_required + the 4/4-or-3/4 clause,
  `:35` thresholds), `:9-10` (baseline commit).
- `reports/round-35/plan/P01-c-plan.md:16-26` (the `scope`-field finding), `:76-77` (census),
  `:108-119` (topic table), `:375-386` (author assignments), `:46-53` (`- gap filled:` 13/201,
  decision record 22/201, house size 36–43 KB).
- Drafts reviewed (fragment digests): `reports/round-35/cov/C01-entry-1.md` `3164d10d…`,
  `C02-entry-2.md` `6746faf3…`, `C03-entry-3.md` `82af002e…`, `C04-entry-4.md` `c828b06f…` (revised
  from `6d5e7832…`), `C05-entry-5.md` `d6f930b2…`; extracted entry bytes `94cd206a…`, `0b382526…`,
  `570b82ea…`, `9805c0b8…`, `9dddc9d1…` (all under `.scratch/r01-entries/`, scratch).
- `reports/round-35/cov/C12-audit-runbook.md:766,773` (staging regex + `blocks[0]`), `:932`
  (`CANNOT-EVALUATE` shape); `reports/round-35/cov/C02-entry-2.md` §Findings 2/4 (the same two
  findings, reached independently by the author seat).
- `reports/round-27/audit/entry-audit.py:65` (`LOC_RE`), `:109-140` (`resolve_ref` partition
  fallbacks), `:353-438` (selftest, 11/11 re-verified by this seat);
  `reports/round-19/audit/entry-audit.py:69` (`LOC_RE`), `:83-92` (resolver without partition
  fallbacks), `:99-134` (bar).
- `corpus/QUALITY.md:1-23` (admission bar); `corpus/README.md:469` (`Total knowledge entries: 201.`),
  `:473` (counts footer), `:123,147,169` (partition headers).
- Baseline bytes, **two verification classes** (all at `4a7aede`):
  **(a) line-cited files — resolution + in-bounds verified programmatically for all 181 citations
  (0 out-of-bounds, 0 unresolved files), cited-line text printed by `r01-anchors.py` and read by this
  seat for C02 in full and as tail spot-reads for C01/C03/C04/C05**, with targeted content checks
  re-run by hand for C02's list: `culture-material/{material-culture-inference-method.md:13,33,61,66,73,75,76,105; cuisine-food-lexicon.md:17,26,27,157;
  calendar-festival-systems.md:52,116,167; textile-technology.md:11,21,76,83; trade-economy-lexicon.md:17,87,89,92,110,121;
  transport-mobility-lexicon.md:4,29,118; vessel-container-lexicon.md:34,97,120; ritual-garments.md:21,112;
  adornment-body-codes.md:81; architecture-settlement-lexicon.md:30,49,80,121,125; era-periodization-models.md:6,31,56;
  sumptuary-law-rank-display.md:1}`, `linguistics/{writing-systems.md:7,43,47,117,149,156;
  numerals-and-measures.md:10,110,135; register-strata-attestation.md:21}`,
  `myth-symbol/{ritual-liminality.md:21,24,30,32,61,87,88,93,110,111; plant-symbolism.md:7,56,162;
  divination-omen-systems.md:112; celestial-symbolism-calendars.md:83}`,
  `civilizations/{austronesia-philippines-taiwan.md:109-126,:115-116; khmer-angkor.md:146-149; nazca.md:37,105;
  scythian-saka.md:24,64}`, `verification/{calibration-registry.md:78-88}`,
  `synthesis/{conlang-blueprint-template.md:22; loanword-material-dating.md:68}`.
  **(b) couples-only targets — existence on disk verified, no line claim made**:
  `culture-material/craft-artisan-lexicon.md`, `linguistics/{language-contact.md; semantic-fields-lexicon-building.md;
  naming-systems.md; politeness-taboo-euphemism.md; orality-formulaic-language.md}`,
  `myth-symbol/{color-symbolism.md; creation-myths-taxonomy.md; symbolism-synthesis-method.md}`,
  `verification/{to-verify-triage-protocol.md; citation-format-and-source-registry.md}`,
  `synthesis/{coupling-model.md; worldbible-integration-contract.md}`.
  The pinned per-file digest list for both target partitions + the README is
  `.scratch/r01-baseline-digests.tsv` (`6434b18d…`, 38 rows).
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`; the census loop → `21 19 18 29
  20 94`; `ls corpus/knowledge/*/*.md | wc -l` → 201; `sha256sum` pins; `git status --porcelain
  corpus/` → empty; `.scratch/r01-extract.py`, `.scratch/r01-review.py` (14/14 controls),
  `.scratch/r01-anchors.py` (164 line-citations, 0 out-of-bounds, 0 unresolved files),
  `.scratch/r01-gapcheck.py` (baseline-scoped greps); `reports/round-27/audit/entry-audit.py` and
  `reports/round-19/audit/entry-audit.py` (read-only, on extracted bytes at intended paths under
  `.scratch/r01-stage/`); `grep -rl -- '^- scope:' corpus/knowledge/ | wc -l` → 0;
  `grep -rl -- '^- source:' corpus/knowledge/ | wc -l` → 134; the fence-tag census and the verbatim
  replication of C12's staging regex (§4.2).
