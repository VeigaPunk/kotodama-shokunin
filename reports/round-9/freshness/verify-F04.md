# verify-F04 — independent verification of R9-F04a/b/c (round-9 freshness, verifier V03)

- **Verifier:** FRESHNESS VERIFIER V03 (this shard). Assignment: "same for R9-F04a/b/c".
- **Target:** R9 freshness claim F, residual **R9-R8-F04** (prior row R6-07-A): *"Check mlqrt/Melqart's
  king-of-the-city analysis and the limits of a fixed merchant-patron/theological profile against an
  inscription, philological source or scholarly passage."* Entry:
  `corpus/knowledge/civilizations/levant-canaan-phoenician.md` §4 bullet 1 (line 78).
  The F claim requires per residual: ≥2 escalated-strategy receipts (primary-source/museum-record hunter,
  scholarly-fulltext hunter, alternate-angle hunter, **independent verifier**) and ≥2 of the 4 residuals at
  partial-support-or-better on primary or scholarly passages.
- **Role discipline:** this shard does not author receipts; it re-fetches, re-quotes, re-hashes and rules on
  R9-F04a/b/c and on what its own escalation can establish. Raw worker labels stay with the receipts.
- **Session window:** 2026-10-17 **20:48–21:03 UTC** (`date -u`, readings logged throughout). All fetches
  below were made in that window from this host.
- **Scratch (not a deliverable):** `~/.cache/r9v03/` with `qcheck.py`, `f04a/ f04b/ f04c/` artifact trees.
  A repo-local `.scratch-v03/` was created at 20:48:32 and deleted at 20:52 before any deliverable; it is not
  part of the round tree. `/tmp` was unusable (`df -i /tmp` → `1048576 1048576 0 100%` at 20:48:31), the same
  fleet-wide condition V02, R9-F03a and R9-F04c each recorded independently.

## 1. Receipt-presence poll log

`ls -la reports/round-9/freshness/` — 20:48:15 (empty), 20:48:32, 20:48:54, 20:50:26 (empty), 20:52:37
(only `verify-F03.md`), 20:54:16 (F01b, F03a), 20:54:33 (F03c), **20:55:36 → `R9-F04a-receipt.json`**,
20:56:13 (`R9-F04a-receipt.md`, `R9-F04c-receipt.json`), 20:57:39 (`R9-F04c-receipt.md`),
**20:58:41 → `R9-F04b-receipt.json`** (= the third and last F04 receipt), 21:00:41 (all stable). All three were
inside the mandated window.

The receipts kept being revised while this shard verified (F04a json 49006→49371 B; F04b json 27671→28092 B;
F04c json 41924→42229 B). §3 was executed against live sources, and §3.4 records that every specific claim
this file verifies was re-confirmed present in the **frozen copies** (hashes in §3.4).

## 2. Method and tooling

- Every source cited by the three receipts was re-fetched by **this** shard with curl (browser UA) or the
  FetchURL tool; HTTP status, byte size and sha256 recorded per artifact in `~/.cache/r9v03/`.
- **Quote test:** `~/.cache/r9v03/qcheck.py` — NFKC, quote/dash folding, whitespace collapse, bracket removal,
  then the longest contiguous normalized token n-gram of the receipt's quoted text found in **my own**
  artifact. ≥10 tokens = containment pass. A 7-token quote can only reach 7/7; such cases are reported as
  full-by-inspection.
- Entry digests re-measured with `sha256sum` and against the git object
  (`git show e1694bad…:corpus/…/levant-canaan-phoenician.md | sha256sum`).

## 3. Independent re-verification

### 3.1 R9-F04a — primary-source / museum-record hunter

| Receipt claim (URL → status/size/hash) | My independent result (2026-10-17, UTC) | Quote test |
|---|---|---|
| Louvre AO 4826 record `cl010165607` | HTTP 200, 60,666 B, `e65c1b8c…` | "Base de statue avec inscription phénicienne : dédicace du roi Milkyathon à Melqart" — **12/12 tokens, PASS** |
| Louvre AO 7676 record `cl010123319` | HTTP 200, 67,567 B, `b833c013…` | "Inscription bilingue … dédicace aux dieux du gymnase, Hermès et Héraclès-Milqart" **18 tokens**; "Bonnet, Corinne, Melqart … 1988, p. 117" **17 tokens — PASS** |
| CIS I scan `archive.org/download/CorpusInscriptionumSemiticarumI1/…djvu.txt` — claimed **728,299 bytes** | HTTP 200, **728,299 B (exact)**, `42243bed…` | CIS I 88 Latin at my lines 8319–8331 incl. "domino suo Melqarto … quia audiit Melqartus vocem eorum" (receipt's lines match); editor's note at my line 3076 ("…vocem šmʿ, quae saepissime titulos phoenicios claudit, piel esse non pual") — **both located as cited** |
| Virtual Museum of Syria stele page | HTTP 200, 206,795 B, `c3bb29ce…` | "This basalt stele was discovered in the 1930s at Bureij…" — **35 tokens, PASS** |
| Heritage Malta cippi page | HTTP 200, 166,491 B, `ce846488…` | "The Cippi, two marble pillars from the 2nd century BC…" — **24 tokens, PASS** |
| Aliquot 2025 (HAL `hal-05325053`) abstract quote | HAL **metadata API** returns the quoted sentences **verbatim**: "L'objectif du présent article est de rouvrir le dossier … sous le principat d'Auguste." — abstract leg **verified** | — |
| Aliquot 2025 PDF /document (3 body-page passages: translation block, "soit transcrit (ʾrms), soit traduit en phénicien (mlqrt)", παλαίστρα calque) | **NOT reproducible now:** curl on `hal.science/hal-05325053/document`, `/v1/document` and the `cnrs.hal.science/…/file/Aliquot-…pdf` URL each returned HTTP 200 with a **12,559-byte Anubis challenge page** ("Making sure you're not a bot!"); FetchURL returned the challenge text; Wayback has **no snapshot** of either HAL URL | **receipt-only** |
| Entry digest `2ca21052…` = blob at baseline `e1694ba` | **Confirmed:** my `sha256sum` and `git show e1694ba:… | sha256sum` both give `2ca210524696bca71a9f97238dd324f4abef7da3c3a52cd08a649a83b8e9e4da`; `git diff` empty | — |

Calibration honesty check: the receipt's own calibration (museum summary "dédicace du roi Milkyathon" vs CIS
text where the dedicant is an interpreter; "gymnase" vs παλαίστρα; "Astarhut (?)" vs ʿAštartiḥawwot) matches
what the two sources actually say on my copies. CIS OCR handling: the receipt discloses substitutions for
`hrnc→h[a]ec`-class noise but not all (e.g. scan "AdonUmesw" rendered "Adonisemes"); substantive text verifies
at the cited lines — flag, not fail.

### 3.2 R9-F04b — scholarly-fulltext hunter

- **Lipiński 1997 mirror PDF — the strongest byte-for-byte verification of the round.** Receipt claimed
  `sha256 11982779…f7d2e`, 21,929,634 bytes, pdftotext -layout hash `c8c30adf…b0cb0`. My fetch: HTTP 200,
  **21,929,634 B, sha256 `11982779862b1b0208e00fc6895ab50e4391cd60270e0fe91a535baa72cf7d2e` (exact)**;
  `pdftotext -layout` output **sha256 `c8c30adfae10c5fe409631939fcda240fbd3161f361fc64be250548d9f9b0cb0`
  (exact)**. Quotes located at the exact cited lines: line **9713** ("…some Phoenician divine names as Mlqrt,
  "Melqart", from milk ("king") + qart ("city")…"), **7837** ("mlqrt < *milk-qart, "the king of the
  city""), **8214** ("Mlqrt < *milk qart, "the king of the City", and to mlkty…"); the edition caveat
  verifies ("second edition" → **0 occurrences**). One small discrepancy: receipt says "756 PDF pages";
  `pdfinfo` reports **755** — off-by-one, immaterial.
- **Persée review pp. 447–449 via `?pageId=T1_446…449`** — **reproduces**: distinct artifacts per page
  (72,729 / 77,391 / 79,178 / 72,164 B; hashes `3f29aebb…`, `bc690c5a…`, `ac7952a4…`, `1c0b1a5a…`).
  Containment: p. 447 quote **46 tokens PASS**; p. 448 "avatar stricto sensu…" **16 PASS**, "l'expression
  culminante…" **10 PASS**; p. 449 "un éventail toujours plus large de prérogatives » (p. 432)" — quote is
  7 tokens and **fully present 7/7** (below the ≥10 threshold by length alone).
- **Bonnet 2009 chapter (`hal-01996916`)** — artifact claimed (`sha256 d4f3fe4a…`, 1,033,332 B, page-image
  transcripts). **Not reproducible now**: `/document`, `/v1/document` and the registered `/file/…pdf` URL all
  return the 12,559-byte Anubis challenge; FetchURL same. The HAL **API** does verify the deposit's existence
  and identity beyond round 8: title, author, `page_s 295-308`, `fileMain_s`/`files_s` registered.
  The vision-transcribed quotes are **receipt-declared, non-reproducible at verification time** (see §5, §6).
- HAL 1988 record metadata-only: **confirmed** (my API call returns no `fileMain_s`/`files_s`).
- archive.org negative sweep (numFound 6 for `title:(melqart)`, none the 1988 monograph): consistent with my
  own `creator:(Bonnet)` query (numFound 0) with archive.org back online — the negative is now outage-free.
- Open Library timeout: **constituent with mine** (my two attempts: curl(28) at 25 s and 40 s).

### 3.3 R9-F04c — alternate-angle hunter

- **Krahmalkov, Phoenician-Punic Dictionary scan** — claimed 898,880 B / `77c9ba63…`: my fetch **898,880 B,
  sha256 `77c9ba632da9d432…` (exact)**. MLQRT entry at my lines 16216–16230 as cited (OCR `MLORT`, `BASAL`
  — disclosed). Quote **13 tokens PASS**. **Negative claim verified:** `grep -ci "king of the city"` over the
  full scan → **0** — the dictionary indeed does not print the composite gloss.
- **Aubet, Tiro y las colonias…** — claimed 942,752 B / `6410fc2d…`: my fetch **942,752 B, sha256
  `6410fc2ddaf1e085…` (exact)**. Quotes: (b) divinización del rey **35 tokens PASS** (my lines 7440–7445,
  within the cited 7416–7498), (d) costumbre tiria **12 PASS**, (e) nexo de unión… básicamente política
  **51 PASS** (my lines 7552–7566, matching the citation exactly).
- **Persée RÉA 1990 review** — my page 72,423 B vs receipt 72,420 B, hash differs (`3fe6cd4d…` vs
  `24681df7…`): **live-page dynamism, not a discrepancy** — two of *my own* fetches (20:57 and 21:01) have
  identical size 72,423 B and different sha256 (`3fe6cd4d…` vs `0ca8cd86…`). Containment: p. 446
  historiography quote **49 PASS**; displayed-extract "roi de la cité (mlk qrt)" **15 PASS**.
- **Syria 1993 review** — 70,474 vs 70,471 B (same dynamism); p. 603 quote **31 tokens PASS**.
- **Mesnil du Buisson displayed extract** — the receipt's two gloss sentences are on the Persée search page
  (media labelled "displayed extract" in the receipt): "…al de Tyr, le « maître de la ville », ou comme son
  surnom l'indique, le « roi de la cité »" + "…« le Roi ; de la ; Cité infernale m1, parce q…" — my
  containment of the sentence as the receipt prints it (snippet artifacts cleaned) **16 tokens PASS**. The
  raw snippet carries stray `? ; ■` OCR debris the receipt does not transcribe — media type is disclosed.
- **huma-num closure — reproduces in full:** `melqart.huma-num.fr` → `curl: (6) Could not resolve host`
  (my third-round-independent check, 20:48:49Z); controls `map-polytheisms.huma-num.fr` and
  `www.huma-num.fr` → **HTTP 200** (mine, 20:58Z); Wayback `archived_snapshots: {}` and CDX `[]` (mine,
  20:49Z). Host-level failure, never archived — round 8's "DNS non-resolution" upgraded correctly.

### 3.4 Frozen versions verified

All specific claims verified above were re-confirmed present in the frozen copies of the receipts
(`cp` into `~/.cache/r9v03/verified/`, 15-point needle check, all PRESENT): `R9-F04a-receipt.json` sha256
`3195aea90de6def4…`, `.md` `efbcded1974f7457…`; `R9-F04b-receipt.json` `1e0cc4acb4837bb6…`, `.md`
`71eebc0457b8443d…`; `R9-F04c-receipt.json` `6d346e999d068602…`, `.md` `6ea874e74cb66846…`.

## 4. Cross-receipt and cross-row findings

1. **No re-fetch padding.** All three overlap sweeps hold: F04a's seven retrievals are new objects/hosts
   (round 8's set was Wikipedia / m-saunders / Louvre `cl010165603` / WiBiLex / Euphrosyne); F04b adds the
   grammar behind the relay; F04c adds the relay's own source and two reviews. No receipt re-labels a
   round-8 passage as new; F04a and F04c explicitly exclude the designated tertiary page.
2. **Channel conflict adjudicated — HAL.** F04b claims reading Bonnet 2009 from HAL (hash + page crops);
   F04c's access-failure table records the same URL as Anubis-blocked (12,570 B). From this host **now**, the
   wall reproduces (12,559 B), so F04c's failure stands and F04b's artifact is non-reproducible (§3.2);
   neither is a fabrication finding — it is an access-state question, flagged for the auditor rather than
   decided by me.
3. **F04c's "no viewer route exists" for Persée pp. 447–449 is falsified.** Its probe `?page=N` returning
   identical HTML is true as observed, but the route `?pageId=T1_447…449` serves the pages, and F04b read
   them; my fetches reproduce (three distinct page artifacts). **Consequence: F04c's deeper-limit item
   "the reviews' later pages" is not a residual limit — it is closed by F04b's route.**
4. **Round-8 WiBiLex author limit closed by this shard.** The author line *is* retrievable: my fetch
   (`-H Accept-Language` + browser UA, HTTP 200, 358,231 B, `8d4420ec…`) shows "**Bärbel Morstadt**"; the
   stable PDF (`cms.ibep-prod.com/…/Melqart__2019-09-10_21_28.pdf`, HTTP 200, 154,531 B, `4fe833d1…`, 533
   extracted lines) carries it too, with the full citation at txt line 393: "Morstadt, Bärbel, Art. Melqart,
   in: Das Wissenschaftliche Bibellexikon im Internet". (F04b notes the limit was "not re-attempted"; no
   receipt contradicts the finding.)
5. **F04a's VMS-operator gap closed by this shard.** `virtual-museum-syria.org/about/` → HTTP 200,
   1,646,723 B, `56fd7e91…` at 21:00Z: "The Syrian Virtual Museum (VMS) is an independent digital heritage
   initiative … Established in 2016 by **Mirath for Cultural Heritage, a non-profit organization
   registered in the United States**". The page is an initiative's own statement, not a national-museum
   authority — the receipt's caution about its record class remains correct.
6. **Label discipline intact.** All three receipts carry worker label `partial-support` (F04a md §Raw label;
   F04b `result` + vocabulary note; F04c `whole_claim_support_label`), all keep **Bonnet 1988 book-level
   unread** and none claims full support or denies a commercial role (calibrated absence only). The
   for-cause check on F04c's own anti-denial calibration is satisfied: the *relay source itself* (Aubet)
   does attribute commercial patronage as one function — quote (e) verified verbatim at my lines 7552–7566.

## 5. Access failures found by this verifier (commands + status)

| Target | Command (as run) | Result |
|---|---|---|
| HAL `/document`, `/v1/document`, `/file/…pdf` for hal-05325053 AND hal-01996916 | `curl -sSL -A <UA> …`; FetchURL | HTTP 200 but body = **12,559-byte Anubis challenge** ("Making sure you're not a bot!"); no Wayback snapshot |
| Wayback for `melqart.huma-num.fr` / wibilex article | `archive.org/wayback/available…`; CDX API | `{"archived_snapshots": {}}`; CDX `[]` |
| Perseus (Josephus CA 1.18 probe) | `curl …perseus.tufts.edu…` | **HTTP 503**, 285 B |
| openlibrary.org | `curl …search.json?q=Melqart…` ×2 | curl(28) timeout at 25 s and 40 s |
| api.persee.fr | `getent hosts api.persee.fr` / curl | **no DNS** (www.persee.fr resolves, 140.77.166.118) |
| Louvre search endpoint | `…/recherche?q=AO+7676`, `q=AO+8185` | **HTTP 429** (twice) |
| `/tmp` scratch | `mkdir -p /tmp/v03` | "No space left on device"; `df -i` → 0 free inodes |

These are channel receipts, not source verdicts. The HAL wall in particular explains exactly why two of the
strongest legs in this residual's set (Aliquot body, Bonnet 2009 body) cannot be re-derived today.

## 6. Adversarial checklist and per-receipt verdicts

What an F04 receipt must demonstrate (used as the rubric): (1) ≥2 escalated strategies beyond tertiary
pages, at least one primary/museum-record or scholarly-fulltext, with URL + locator + quote fidelity;
(2) datedness per witness (KAI 201 9th/8th c.; Kition c. 380–370; Malta 2nd c. BCE; Arados 25/24 BCE);
(3) no back-projection of late bilinguals onto Bronze Age Tyre; (4) passage support separated from
whole-claim support, raw labels preserved; (5) counts carry commands + dates, negatives carry sweeps;
(6) no re-labelled round-8 passages; (7) calibration against the merchant-patron half (Aubet relay and the
Caquot-via-Bonnet "patron of maritime and commercial adventure" nuance must not be tightened into denial).

| Receipt | Independent evidence reproduced | Non-reproducible / caveats | Verdict |
|---|---|---|---|
| **R9-F04a** | 6/7 channels live-verified with hashes; CIS scan **byte-exact**; internal calibrations accurate; entry digest exact | Aliquot **body** passages (3) receipt-only (Anubis wall); CIS OCR substitutions partially disclosed | **PASS, with one receipt-only leg (disclosed by receipt itself in access_failures)** |
| **R9-F04b** | Lipiński PDF **double byte-exact** (file + extraction) + 3 quotes at exact lines; Persée 447/448/449 readable & contained; HAL-1988 negative confirmed | Bonnet 2009 artifact hash non-reproducible (wall); page count 755 vs claimed 756 | **PASS (strongest)** |
| **R9-F04c** | Krahmalkov + Aubet **byte-exact**; 7/7 quotes contained; negative claim (`0` hits) verified; huma-num closure + controls reproduce | Mesnil quotes via displayed snippet with untranscribed OCR debris; "no viewer route" inference wrong (pages readable via `?pageId`) | **PASS with one corrected inference** |

## 7. Residual-row verdict (my ruling, for the F claim's counting)

R9-R8-F04 is, on my independent inspection, **partial-support-or-better on primary and scholarly passages**:
both substantive legs of line 78 now stand on dated primary objects (Kition c. 380–370 BCE, Malta 2nd c.
BCE, Arados 25/24 BCE, KAI 201) and on scholarly fulltexts (WiBiLex; Euphrosyne 45; Lipiński 1997 at
source; two peer reviews of Bonnet 1988). The `(Bonnet 1988)` attribution itself remains **book-level
unverified** — that is a *limits* statement, not a lack of passage support; nothing retrieved contradicts
the claim. The 3-hunter + verifier set for this residual is **complete** (a, b, c + this file), satisfying
the F claim's structure for this row. Whether "≥2 of the 4" is met depends on the sibling rows, not on me.

## 8. Limits of this verification

1. No pixel/vision-level checks: I did not re-perform page-image reading (Bonnet 2009 crops, museum photos).
2. The two HAL legs are adjudicated as *channel state at 20:57–21:01Z from this host*, not as claims of
   falsity; the wall may lift or route differently for other clients.
3. Persée pages are live-dynamic (same-size, different-hash across two of my own fetches); byte equality
   with any receipt's snapshot is therefore not expected — containment decides.
4. Bot-walled/tertiary sources drift; all my hashes are timestamped snapshots.
5. The receipts were revised during this window; §3.4's frozen hashes bound this verification. Any further
   revision invalidates the corresponding part of this file.
6. **Bonnet 1988 was still not read as a book by anyone in this set**; the entry's attribution stays open,
   and the best available routes into it remain the review pp. 417–436 quotes (verified) and the museum
   bibliography pointer to p. 117 (verified).

*Every quote in this file was matched by `qcheck.py` against an artifact fetched by this shard; token counts
are the longest contiguous normalized n-gram. Artifact tree (27 hashed files, sha256 prefixes 16 hex) and raw
fetches: `~/.cache/r9v03/` (e.g. `f04b/lipinski1997.pdf` `11982779862b1b02…`; `f04c/krahmalkov.txt`
`77c9ba632da9d432…`; `f04a/cis1-djvu.txt` `42243bed2b87e3df…`).*
