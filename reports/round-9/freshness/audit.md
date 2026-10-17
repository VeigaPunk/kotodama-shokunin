# Round-9 freshness receipts — X02 audit

- Auditor: X02 scribe (F-receipts auditor), author-side. **Not an independent promotion verifier.**
- Audit window: 2026-10-17T17:48–18:01 local (-03:00) = 20:48–21:01 UTC; every retrieval below was
  re-run live in that window against my own copies.
- Scope: `reports/round-9/freshness/`. The F claim requires, for each of the four round-8 leftovers,
  ≥2 escalated-strategy retrieval receipts (primary-source/museum-record hunter, scholarly-fulltext
  hunter, alternate-angle hunter) **plus an independent verifier**, with ≥2 of the 4 moving to
  partial-support-or-better (`reports/round-9/claims.json`, claim F).
- Counting command (run 2026-10-17T18:01, re-run 18:03, final 18:04 local):
  `ls reports/round-9/freshness/ | grep -v '^\.' | wc -l` → **25 files at 18:01**, **26 at 18:03**,
  **27 at audit close** = **12 hunter receipt JSONs** (F01a/b/c, F02a/b/c, F03a/b/c, F04a/b/c — the full
  set), 12 `.md` companions, **2 verifier files** (`verify-F03.md`, `verify-F04.md` — the latter landed
  mid-audit), plus this audit.
- Method: (a) structural scan of every receipt (URL, accessed-at, locator, excerpt, support-scope
  fields); (b) independent re-fetch of every cited artifact, recording HTTP status, byte size and sha256,
  then **char-normalized quote matching** (NFKC, quote/dash folding, whitespace collapse, Wikipedia
  ref-marker stripping) against *my* artifact — never the receipt's; (c) sha256 equality tests wherever a
  receipt names a hash; (d) accessed-at plausibility vs file mtime.
- **Fetch-method discipline (earned the hard way, see §3.1, §3.8, §2.7):** every hash test below was run
  twice where the first attempt hit a wall — once with a desktop browser User-Agent, once with curl's
  default UA — and proxy-disclosed artifacts were re-fetched through the same proxy. Hosts in this
  ecosystem variously return a 12,591-byte Anubis interstitial or a ~770-byte DataDome challenge to one
  class of client and the real artifact to another, so a single UA-blind test produces both false
  failures and false passes.
- Matcher validated before use on a known passage: true quote → `EXACT 258/258`; the same quote with one
  word changed → `PARTIAL 41/256`.

## 0. Environment note (affects every shard, including this auditor)

`/tmp` held **0 free inodes** throughout this window: `df -i /tmp` → `1048576 1048576 0 100% /tmp`,
2026-10-17T17:49 local. Any write there fails with "No space left on device" — including a `nohup`
poller this auditor launched. My artifacts therefore live outside `/tmp`. Both the F01b receipt and the
F03 verifier independently record the same condition (`R9-F01b` access_failures; `verify-F03.md` §intro,
`df -i` at 20:48:31 UTC), which is corroboration, not duplication.

## 1. Verdict summary (all 12 hunter receipts + 2 verifier files on disk)

| Receipt | Residual | Strategy | Its own result claim | My spot-check | Verdict |
|---|---|---|---|---|---|
| `R9-F01a` | F01 | primary-source / museum-catalogue | object-level leg retrieved (Louvre + CDLI + ATF) | **6/6** artifacts byte-identical (incl. 154 MB dump) | pass (strongest) |
| `R9-F01b` | F01 | scholarly-fulltext | 6 unread scholarly fulltexts, named printed pages | **6/6** hashes byte-identical (after UA correction, §3.1) | pass |
| `R9-F01c` | F01 | alternate-angle | partial-support-or-better; passage + object-record | quote-level read only; not hash-checked | pass with note |
| `R9-F02a` | F02 | primary-source / reference-work | candidate-term primary reading (CAD, dated objects) | structural read only; no hash claims to test | unaudited by me |
| `R9-F02b` | F02 | scholarly-fulltext | Breniquet 2016 read **in full** + peer-reviewed corroboration | **2/2** byte-identical, incl. the proxy artifact (§2.7) | pass (strongest) |
| `R9-F02c` | F02 | alternate-angle | 1902 Louvre catalogue, 1931 JRAS, 1935 excavation report | structural read only; not hash-checked | unaudited by me |
| `R9-F03a` | F03 | primary-source / museum-record | partial-support | 4 hashes exact; 2 pages proven volatile (§3.2); Met 429 reproduced | pass with note |
| `R9-F03b` | F03 | scholarly-fulltext | partial-support-or-better (lane) | **6/6** sources byte-identical | pass (strongest) |
| `R9-F03c` | F03 | alternate-angle | partial-support | not spot-checked (time-boxed) | unaudited by me |
| `R9-F04a` | F04 | primary-source / museum-record | partial-support | quote locations verified on my own copies (§2.5) | pass with note |
| `R9-F04b` | F04 | scholarly-fulltext | partial-support (escalated) | **2/2** hashes byte-identical, incl. the Lipiński volume | pass (strongest) |
| `R9-F04c` | F04 | alternate-angle | passage-supported, rival reading documented | not spot-checked (time-boxed) | unaudited by me |
| `verify-F03.md` | F03 | independent verifier | §3–§5 findings; §6 verdicts pending its own poll | **12/12** testable claims reproduce | pass, with one correction (§3.8) |
| `verify-F04.md` | F04 | independent verifier | §6–§7: F04a/b PASS, F04c PASS with one corrected inference | its own byte-exact tests confirmed; its "non-reproducible" rulings corrected (§3.10) | pass, with one correction |

**Coverage against the F claim's own text — final state:** all four residuals carry ≥2 escalated-strategy
receipts (F01 a/b/c, F02 a/b/c, F03 a/b/c, F04 a/b/c) — **the 3-hunter requirement is satisfied on disk**.
The **independent-verifier requirement is satisfied for F03 and F04 only**: `verify-F03.md` and
`verify-F04.md` landed; `verify-F01` and `verify-F02` never appeared. F02's receipts arrived last, at
17:59–18:00, i.e. inside this auditor's poll window but late enough that my hash-level testing of F02
covers one of its three receipts; F02 is also one of the two residuals with no verifier.

## 2. Spot-checks performed (40 byte-level tests; target was ≥4)

### 2.1 `R9-F01a` — 6 of 6 artifacts byte-identical, including a 154 MB dump

| Cited artifact | Receipt claims | My independent fetch | Match |
|---|---|---|---|
| Louvre `cl010166127` **JSON API** (`.json`, not the human page) | 5,930 B / `e9b0f67e…` | 5,930 B / `e9b0f67ec2bac48e3dbafd1e43912c3b4c875fc11f3a59e0df91c70fc8970aa7` | yes |
| `cdli.earth/artifacts/220619.json` | 4,694 B / `a7c94e4d…` | 4,694 B / `a7c94e4d2f52478bd50ad77cbebe5b8eaebdca7e91591d8f00ae04a4b76f6d5b` | yes |
| `cdli.earth/artifacts/461964.json` | 3,543 B / `f9b1c2f7…` | 3,543 B / `f9b1c2f7e0d066e5f65cdbb5d0ffebca42926c7373a0bdf3d2705d03dc48e085` | yes |
| `cdli.earth/artifacts/227513.json` | 12,250 B / `1a93486c…` | 12,250 B / `1a93486c21658dfbd3d99abf44fffdbd76bffd5bc45b9b696ab8c5a44a24237a` | yes |
| Wikidata `Special:EntityData/Q87473226.json` | 11,177 B / `59a47cbf…` | 11,177 B / `59a47cbf5b5361faac5fdacf5165c71e4bab3d588f89581731052765e9e451bd` | yes |
| CDLI `cdli_cat.csv` (GitHub LFS mirror) | 154,768,722 B / `2e3232f7…` | 154,768,722 B / `2e3232f75325b61c4d1e788d4d8c074c6230a947aed422110f9f35a6e353d09c` | yes |

Clarification for readers, not a defect: the receipt's `source_url` for the first item names the human
record page while the hashed artifact is the `.json` API response; the receipt names the API endpoint in
its text. My first fetch used the human page and returned 58,975 B — the hash belongs to the API artifact.

### 2.2 `R9-F01b` — 6 of 6 hashes byte-identical

mprl `Studies10Chap8.pdf` 4,445,650 B / `02839a70…`; mprl `Studies10.pdf` 5,290,603 B / `592b4990…`;
Viano (Edizioni Ca' Foscari) 2,941,956 B / `e2d8f8c3…`; van Dijk-Coombes 1,945,759 B / `73a6ee96…`;
Sommerfeld (SAA 28.1) 632,295 B / `60744adc…`; Jordan & Fink (Studia Orientalia Electronica) 591,441 B /
`191c417e…`. **All six byte-identical to my own downloads.** The Jordan–Fink case initially failed and is
the most instructive single result of this audit — see §3.1.

### 2.3 `R9-F03b` — 6 of 6 sources byte-identical

Ensert 674,838 B / `434498f9…`; Durusu-Tanriöver (Bilkent) 1,723,823 B / `05debcf…`;
*Sacred Landscapes of Hittites and Luwians* (archive.org) 8,550,096 B / `e9edf217…`;
Wygnańska (BazHum) 6,416,638 B / `cf59066c…`; Klaunzer (Metalla 20.2) 887,194 B / `0a750ba3…`;
Hethitologie-Portal bibliography row 1,744 B / `b762edd7…`.

### 2.4 `R9-F03a` — museum records: 4 exact, 2 explained, 1 disclosed

Cleveland `1971.45` 16,000 B / `30e4e344…`; Cleveland `1985.70` 6,017 B / `0880e7d7…`; Cleveland
`1973.19` 4,019 B / `b9d5dfd6…`; Louvre `cl010135786` (AO 11073) 51,590 B / `9444d7dc…`; Louvre
`cl010135785` (AO 11072) 52,369 B / `5d3ea9c8…`; `hittitemonuments.com/alacahoyuk/` 28,578 B /
`e5fd321c…` — **all exact**. The two `muze.gov.tr` pages are the exception analysed in §3.2. The Met
record is honestly disclosed as FetchURL-only ("a curl re-fetch of the same host returned HTTP 429, so no
local byte artifact exists") — **I reproduced 429 myself**, exactly the disclosure an auditor wants in
place of a silent success.

### 2.5 `R9-F04a` — quote locations verified on my own copies

Louvre `cl010165607` (AO 4826 = CIS I 88), record fields *Description/Features*, *Places and dates*,
*Inscriptions*: my fetch contains `Base de statue avec inscription phénicienne`, `Milkyathon`, `AO 4826`,
`CIS I 88`, `Chypro-classique II`, `Kition`. Heritage Malta page: both quoted sentences present verbatim.
CIS I `djvu.txt` (728,299 B, 16,353 lines): the receipt's line-3076 claim reproduces — my lines 3076–3078
read "Vox pʿl, in qua pronomen suffixum clare apparet, ostendit vocem šmʿ…" in OCR-garbled form, the very
artifact the receipt quotes. Its `virtual-museum-syria.org` page returns **403 to me**, as the receipt
itself flags with a provenance caveat. The receipt also carries a good-faith calibration: it warns that
the museum summary attributes the dedication to the king whereas the corpus shows the dedicant is
Resefyaton, the royal interpreter — it tells the integrator *not* to tighten the record's wording.

### 2.6 `R9-F04b` — 2 of 2 hashes byte-identical, including the volume round 8 could not open

| Cited artifact | Receipt claims | My independent fetch | Match |
|---|---|---|---|
| Lipiński, *Semitic Languages: Outline of a Comparative Grammar* (wordpress-hosted OCR PDF) | 21,929,634 B / `11982779…` | 21,929,634 B / `11982779862b1b0208e00fc6895ab50e4391cd60270e0fe91a535baa72cf7d2e` | yes |
| Bonnet 2009, `hal.science/hal-01996916/document` | 1,033,332 B / `d4f3fe4a…` | 1,033,332 B / `d4f3fe4aedaf48ec8aa2d0891d13c4d7df5e5fffd52631e0a5ca144d3e8057e1` | yes |

The first is the source whose inaccessibility round 8 recorded as a limit ("Lipiński's page remain
unread"; archive.org search `numFound 0`); this shard found it on an OCR'd mirror and the artifact is
byte-stable. The second produced §3.8's correction.

### 2.7 `R9-F02b` — 2 of 2 byte-identical, and the round-8 wall was routed around honestly

The Breniquet 2016 article (*Revue d'assyriologie* 110/1) is the specialist source that defined the
kaunakes debate and which round 8 recorded as HTTP 403 / unread. This shard's receipt claims a
proxy-retrieved artifact; I reproduced **both** its artifacts exactly:

| Cited artifact | Receipt claims | My independent fetch | Match |
|---|---|---|---|
| Breniquet 2016 via `r.jina.ai` reader proxy of the cairn PDF | 84,993 B / `105fe5e2…` | 84,993 B / `105fe5e2dad4dc598b03d3385175b8c87bdf5ae8b3cf078fb4e3c829ce243c09` | yes |
| Heuzey, *Histoire du costume* (archive.org `djvu.txt`) | 466,347 B / `c11607c…` | 466,347 B / `c11607cbc41535fe90ee6ee503f6ec7dabfed665fbc0099aac481890376c` | yes |

I also reproduced the *blocked* direct route: `cairn.info/load_pdf.php?ID_ARTICLE=ASSY_110_0001` returns
**HTTP 403, 770 bytes**, a DataDome JS challenge ("Please enable JS and disable any ad blocker"), both
with a browser UA and with curl's default UA. The receipt discloses exactly this and names the proxy it
used instead, so the artifact's provenance chain is complete: publisher OA confirmed by Unpaywall →
direct fetch refused by DataDome → text obtained through the named reader proxy → saved and hashed
locally. **This is the receipt that closed the residual round 8 could not close, and every step of it is
reproducible from my chair.**

## 3. Findings

**3.1 A bot-wall that depends on your User-Agent — my own false negative, corrected.**
My first fetch of `https://journal.fi/store/article/download/129805/78658` with a desktop Chrome UA
returned **HTTP 200 but 7,319 bytes of HTML**, an Anubis proof-of-work interstitial
(`<title>Making sure you&#39;re not a bot!</title>`). Re-running with curl's default User-Agent returned
**591,441 bytes of `application/pdf`, sha256 `191c417e076c7f1beaf573fb3adf6c3f28fb5151d8e25abe1783a5f13256ff44`**
— byte-identical to the receipt's claim. Same host, same URL, same minute. The receipt is correct; my
first test was wrong.

**3.2 `muze.gov.tr` pages are length-stable but hash-volatile — a property of the page, not the receipt.**
The F03a receipt records BOG01 as 52,602 B / `360d338d…` and ALC01 as 51,631 B / `cdef33fa…`. My fetches
returned the **same byte counts** but different hashes (`0e8a505e…`, `60ab8822…`). To separate page
behaviour from receipt error I fetched the *identical* BOG01 URL twice myself, seconds apart:
**52,602 bytes both times, two different sha256 values** (`0e8a505e…` then `25b23b0e…`), 12/12 GUID-like
tokens shared, bodies equal in length but not content. Both quoted excerpts *are* present in my copies
verbatim (the receipt renders Turkish diacritics in ASCII — `Boğazköy Yerkapı Sphinx` becomes "Bogazkoy
Yerkapi Sphinx"; its `quote_fidelity` field is null for these two, a gap worth closing). Net: the quotes
are verified; the hashes are per-fetch snapshots and must not be used as drift pins.

**3.3 Line-locator deltas are normal and were reproduced.**
CIS I: the receipt puts "Vulgo Idaliensis" inside "scan OCR lines 8319–8331"; in my extraction the Latin
translation `Verte autem :` sits at 8317 and the `Vulgo Idaliensis` header at **8338** — same dossier,
about ten lines later under my invocation. IDD: the receipt cites lines 244–247 for the horned-cap
sentence; mine is at 246 in a 1,448-line extraction matching the receipt's own line count. As in round 8,
`pdftotext`/OCR line numbers are invocation-dependent; quotes should be located by printed page or by
search string, not by raw line number alone.

**3.4 The round-8 access walls are real and reproduce byte-exactly.** Independently re-run by me:
`assziriologia.hu` download → HTTP 200, **51,231 bytes** of parked-domain HTML (round 8 recorded 51,231);
`isac.uchicago.edu/.../ois2_2007.pdf` → HTTP 200, **188,642 bytes** HTML, not a PDF (exact match);
CDLI `/search?q=AO+5477` → **1,633,509 bytes**, the string "Showing 25 entries of 10000+ results" present,
and **no server-side result row** — the three literal "AO 5477" occurrences are the search form echoing
its own query (round 8's claim about client-rendered results is correct); `melqart.huma-num.fr` → DNS
`ENOTFOUND`; British Museum `H_1862-0423-1` → 403 / 5,707 B; `ricerca.sns.it` Bonnet–Ridotto → 403;
Louvre search → 429; cairn DataDome 403 (§2.7).

**3.5 A route the round-9 set may have missed: the Zólyomi preprint is retrievable and hash-stable.**
The Wayback capture `20210228041703id_/http://www.assziriologia.hu/downloads/gz_structural_interference.pdf`
is a real 555,585-byte, 6-page PDF ("Structural interference from Akkadian in Old Babylonian Sumerian",
Zólyomi, *Acta Sumerologica* 22) with sha256
`3c256e65b10e3ba760797f6a7d98b8fcb01c4a07254e0dae4fafe23e98afbe23` — **identical to the hash round-8 F01
recorded**, so the artifact is reproducible across rounds. Naming note: the round-8 receipt's source key
calls this "Gzella"; the article's author is **Gábor Zólyomi** (the file lives on a `.hu` host, possibly
where the mislabel came from).

**3.6 The F02 gap closed inside the window — but late, and with no verifier.** F02 was the last residual
to produce receipts: at 17:58 the directory still held none; by 18:00 all three (`F02a`, `F02b`, `F02c`)
were present. My poll log (60 s from 17:50:18 to 17:56:18, then 45 s) timestamps this precisely. The
practical consequence for the integrator: F02 has the **least verification depth** of the four residuals
— its receipts are the newest, only `F02b` received hash-level testing from me, and unlike F03 it has no
independent verifier. Its claims should be treated as the least corroborated in the set even though its
F02b artifact proved fully reproducible (§2.7).

**3.7 One transient mid-write read, timestamped.** At 17:56:35 local `R9-F01a-receipt.json` failed
`json.load` ("Expecting property name enclosed in double quotes: line 380"); the file's mtime at that
moment was 17:56:35.224. A re-read minutes later parsed cleanly, and all 12 JSON receipts validate today.
Recorded because a harness run in that instant would have scored a false failure — the same class of
transient round 8 saw with `reconciliation.json`.

**3.8 The UA-conditional wall cuts against `verify-F03.md` — one of its three "deeper limits" is not a wall.**
`verify-F03.md` §4 records the Oreshko 2018 PDF as an access failure —
"`curl -sSL -A <UA> …/hal-03880014/file/Oreshko…final.pdf` → HTTP 200 but HTML bot-wall, 12591 bytes" —
and §4's closing paragraph builds a requirement on it: "Any F03 receipt that cites the Oreshko HAL file,
OIP 37 or the BM record needs either a cached/snapshot copy or this same failure recorded — a bare
live-cite is not reproducible as of 2026-10-17."
**The bare live-cite is reproducible.** Fetching the *identical* file URL with curl's default UA returns
**578,236 bytes of `application/pdf`, 27 pages, sha256 `953ce90a2414c67780b061e2d09fa0717de27bdef15d78bf9a672d490e3682e5`**,
whose text contains the garment term the residual wanted: "Hitt. kupaḫi 'a headgear'" (my extraction line
762), plus the Puhvel discussion at line 835 and the Oreshko citation block at 1353 — the right article,
Oreshko, "Anatolian linguistic influences in Early Greek (1500–800 BC)?", *Journal of Language
Relationship* 16/1-2 (2018), 93–118 (HAL-03880014).
What this does and does not mean: the verifier's *observation* (browser-UA request → 12,591-byte
interstitial; landing-page variants also walled) is accurate and I reproduced the interstitial byte for
byte; its *conclusion* that the source is not retrievable by a bare live-cite is wrong, because the wall
is UA-conditional. The verifier itself wrote "a later round can retry", so the correction is within the
receipt's own spirit. **Recommendation:** amend §4 with the UA condition and the 578,236-byte artifact
hash; do not let a UA artifact stand as evidence that a source is unobtainable.

**3.9 The counting command for claim F does not test the verifier half of the claim's own after-state.**
`reports/round-9/validation.json` reports claim F as `passed: true`, `failures: []`, with all four
residuals in `moved_rows`. I checked how that verdict is produced, because the directory contradicts part
of it: `reports/round-9/run-validation.py` detects an "independent verifier" only as a **role word** —
`ESCALATION_RE = re.compile(r"hunter|verifier|primary[-_ ]?source|museum…")` and, in
`nested_retrieval_units()`, `has_role = bool(re.search(r"hunter|verifier|scout|strategy|role|shard|retrieval", role_keys, re.I))`.
There is no check that a verifier **document** exists for each residual; a receipt that contains the word
"verifier" in a key name or a sentence satisfies the role control. On disk, exactly one verifier file
exists (`verify-F03.md`), for one of the four residuals. A reader of `validation.json` alone would
conclude the claim's "…alternate-angle hunter, **independent verifier**" requirement is met for all four.
It is met for F03.
Related terminology point, same section: the harness's `receipt_counts` (`R9-R8-F01: 48`, `F02: 71`,
`F03: 60`, `F04: 45`) count *nested retrieval units*, not "retrieval receipts" in the claim's sense —
a single receipt listing 48 retrievals and 48 receipt documents both report as 48. The numbers are
therefore not a measure of the claim's "≥2 escalated-strategy retrieval receipts" floor.
This is reported, not adjudicated: whether "independent verifier" was intended as a document-per-residual
or as a role designation is the orchestrator's call, not the X02 scribe's.

**3.10 The UA-conditional wall is a pattern across both verifier files, not a one-off.**
`verify-F04.md` (which landed last, during this audit) repeats §3.8's error on a different artifact. Its
§3.2 records the Bonnet 2009 HAL PDF as **"NOT reproducible now: curl on `hal.science/hal-01996916/document`,
`/v1/document` and the `cnrs.hal.science/…/file/Aliquot-…pdf` URL each returned HTTP 200 with a 12,559-byte
Anubis challenge page … Wayback has no snapshot → receipt-only"**, and §6 marks the F04b artifact
"non-reproducible". **I reproduced it exactly**: the identical URL fetched with curl's default UA returns
**1,033,332 bytes of `application/pdf`, sha256 `d4f3fe4aedaf48ec8aa2d0891d13c4d7df5e5fffd52631e0a5ca144d3e8057e1`**
— byte-identical to the F04b receipt's claim and to my §2.6 test. My browser-UA fetch of the same URL
returns the interstitial (12,591 B in my run, 12,559 B in the verifier's — the challenge page varies), so
the verifier's observation is accurate and its reproducibility conclusion is not.
Scope of the correction: two verifier files, three artifacts (Oreshko §3.8, Bonnet 2009 §3.10, and the
same wall behind the Aliquot record both verifiers cite). The artifact-level facts are unaffected; what is
affected is any "deeper-limit" narrative that treats these as permanently unobtainable sources. **A single
`curl` without a browser UA is enough to settle each case**, and I have done so for all three.

## 4. Negative-claim sweep coverage

Every landed receipt carries explicit sweep/command records for its negative claims: `R9-F01a`
(12 access failures, 4 negative sweeps), `F01b` (9 failures, 3 sweeps), `F01c` (8 failures, 3 sweeps),
`F02a` (14 failures, 7 sweeps), `F02b` (10 failures, 4 sweeps), `F02c` (9 failures, 5 sweeps),
`F03a` (8 failures, 5 sweeps), `F03b` (9 failures, 4 sweeps), `F03c` (10 failures), `F04a` (7 failures,
3 sweeps), `F04b` (8 failures + a search sweep), `F04c` (7 failures + a dedicated limit/negative-evidence
block). I re-ran 9 of the documented failures myself (§3.4, §3.8, §2.7) and all 9 reproduced with
matching status or byte size — with the caveat that one (§3.8) proves to be UA-conditional rather than
absolute.

## 5. What this audit does and does not establish

- **Establishes:** for 7 of the 12 hunter receipts and both landed verifier files, the artifacts they name
  exist, at the byte sizes and sha256 values they claim, on 2026-10-17, reproduced from my own downloads —
  40 byte-level tests, 38 exact matches, 2 explained by documented page volatility; the quoted material
  for the F04a and F03a records is present at the locations claimed on my copies; the round-8 walls are
  reproducible (with the UA caveat); the negative-claim sweeps name commands and statuses.
- **Does not establish:** the truth of the underlying scholarship, the correctness of any disposition
  (partial-support / supported), the adequacy of the escalated strategies against the residuals' wording,
  or the completeness of the four residuals' evidence. Verdicts here are about receipt quality and
  reproducibility, per the X02 assignment.
- I did not spot-check `R9-F01c`, `R9-F02a`, `R9-F02c`, `R9-F03c` or `R9-F04c` on the clock; their
  internal consistency was read but not re-tested, and I make no hash-level claim about them.

## 6. Notes for the integrator

1. **The 3-hunter half of the F claim is satisfiable on disk** (12/12 hunter receipts, all four residuals
   covered). **The verifier half is satisfied for F03 and F04 only**: `verify-F03.md` and `verify-F04.md`
   landed, `verify-F01` and `verify-F02` never did. Either those land, or the claim's after-state must be
   restated — and note that `reports/round-9/validation.json` will not surface this on its own (§3.9): it
   scores F `passed: true` because it looks for the *word* "verifier", not for a verifier document.
2. **F02 is the least corroborated residual** — latest to land, one of three receipts hash-tested, and one
   of the two residuals with no verifier (§3.6).
3. **Do not use receipt hashes as drift pins for dynamic pages.** `muze.gov.tr` (§3.2) is length-stable
   and hash-volatile; every other hash I tested is stable and reproducible.
4. **Do not score receipts — or limits — by a single UA-blind curl.** §3.1, §3.8, §3.10 and §2.7 are four
   live examples in both directions: a correct receipt nearly failed, two verifier "non-reproducible"
   rulings are wrong for the same reason, and a proxy-disclosed artifact verified cleanly once the proxy
   was named.
5. **Correct both verifier files' non-reproducibility findings** before their "deeper limit" narratives
   are carried into any acceptance decision: `verify-F03.md` §4 for the Oreshko artifact (§3.8) and
   `verify-F04.md` §3.2/§6 for the Bonnet 2009 artifact (§3.10). Each is one `curl` without a browser UA
   away from being settled; I have already run both.
6. Round-8's walls stand, except for the routes the round-9 shards genuinely opened: cairn via the named
   reader proxy (§2.7), the Lipiński volume via an OCR mirror (§2.6), the Bonnet 2009 deposit (§2.6), and
   the Wayback Zólyomi preprint (§3.5) — all hash-stable and re-verifiable at zero cost.

## 7. Receipt state at audit close (2026-10-17T18:01 local, -03:00)

`sha256sum reports/round-9/freshness/*` at close (audit file excluded):

```
448cd64f6941d582a7a2c3fd05b8efc7e6baac399b366ead4a11be90a96f88cd  R9-F01a-receipt.json
b11fb066756c9766630d35f34c6fae33e4ae90812184ae33a81a036233c17b3a  R9-F01a-receipt.md
6e563f816a599bfeee1a194e2bbcf812390a5d877b7e1c13fcc3c67f4611fd64  R9-F01b-receipt.json
5c3cd450395893646fe20342977ebdd5a87f3650a822d3c6375a8130a6844e7e  R9-F01b-receipt.md
1035d55e26f679ec72644f7d0eb3d4f462b20e478e77f5528e85c405f392a37f  R9-F01c-receipt.json
cbac4d24c07c8f101e15a6855db6664ab8617530b3c68e5527c99ee9387580e2  R9-F01c-receipt.md
8a48d19027037be4db1f147c46a42ff445fbbad26a2d4ab964ba7143f95830a1  R9-F02a-receipt.json
(R9-F02b-receipt.md landed 18:04, after the 18:01 snapshot)
6559973d666bdc58b6668a7dfa96c54fd59d0b1904ccac18e2307240dc42b6d7  R9-F02b-receipt.json
ca2bd2d7a2d52f3027337dbb5972dda2113d5c2ac0c5c49aebb09126d236f1c4  R9-F02c-receipt.json
1746a903f1ba8a5bd385cadc16d3c7ddf6e68605d3ea7042c38582d0529797ec  R9-F03a-receipt.json
07374e3a09b2ad0f2a400229fdcc8d31e52a2cd4d96e1a90d3ac4c7d842f197c  R9-F03a-receipt.md
2b49e9735f6f5b502ec9cba7adf9c0d83df7c043d04e409ebbea21e23558cf18  R9-F03b-receipt.json
eb00d72ebf7c9e0c3c98b4b3f0ec6275b6bae3ca6cc97ad9f119527168c92629  R9-F03b-receipt.md
dfe1b62aafddf0abf63754a735cda2e2541acd4efbfff331add9662ae9c97349  R9-F03c-receipt.json
e741820d1417dbf586706a8b9df2bdbbd29105293d3371d0fb9053cc990fc04d  R9-F03c-receipt.md
3195aea90de6def43d6397ea7593dc52bad5ecdb9512477b2b6f74d4a08914d0  R9-F04a-receipt.json
efbcded1974f7457651c3ded82f8b9782ab4801ee39dc98a2a138503d90e7ee9  R9-F04a-receipt.md
1e0cc4acb4837bb6db522a500a92468895f47a66d3f1242ddfecbb683a3dba99  R9-F04b-receipt.json
e5bb68145c9856083ad4e03a5cbfb2af911796d0702469ab2464914b4f376f7c  R9-F04c-receipt.json
01c92c38c2db9d7acacd177d133b62934d60352f5f362f86907c93e1c4bbe46c  R9-F04c-receipt.md
a2de696959913c865a7195a74cfc17fa4bc9a3028c65e32f40ed9f5b34d04308  verify-F03.md
79bfc3e8bcbc4d169e6c29fad124ba9f51dc8298aec1808b73f182899c2c50ad  verify-F04.md
```

`.md` companions existed for all twelve hunter receipts at close except `R9-F02b-receipt.md`, which landed
at 18:04 during this audit; the F02a/F02c/F04b `.md` files also appeared within the audit window.
`verify-F04.md` landed during this audit (≈18:03) and is audited in §3.10 from the live file. No
`verify-F01` or `verify-F02` file existed at any point in the poll log. Files written after this close
are outside the audit.
