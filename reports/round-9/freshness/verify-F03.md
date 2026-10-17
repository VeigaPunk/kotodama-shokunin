# verify-F03 — independent verification of R9-F03a/b/c (round-9 freshness, verifier V02)

- **Verifier:** FRESHNESS VERIFIER V02 (this shard). Assignment: "same for R9-F03a/b/c".
- **Target claim:** R9 freshness claim F, residual **R9-R8-F03** (prior row R6-05-B): *"Check one dated
  divine/royal headgear, pointed-cap or horned-crown identification in the entry; distinguish depicted
  rank, deity/king identification and earlier Hattic or later Neo-Hittite comparators."* Entry:
  `corpus/knowledge/civilizations/anatolia-hittite.md`. Required by the F claim: each of the 4 residuals
  carries ≥2 escalated-strategy retrieval receipts (primary-source/museum-record hunter, scholarly-fulltext
  hunter, alternate-angle hunter, **independent verifier**); ≥2 of the 4 residuals move to partial-support
  or better on primary or scholarly passages.
- **Role discipline:** this verifier does **not** claim receipt authorship; it re-fetches, re-quotes and
  rules on the hunters' receipts and on what an independent escalation can itself establish. Raw round-6
  labels stay with the receipts; nothing here rewrites them.
- **Session window:** 2026-10-17 20:47–21:xx UTC (`date -u`, this host). All fetches below were made in
  that window from this host unless a different date is stated.
- **Scratch (this verifier's own, not a deliverable):** `~/.cache/r9v02/` — `/tmp` was unusable during
  this window (16 GB tmpfs, **0 free inodes**: `df -i /tmp` → `1048576 1048576 0 100% /tmp` at 20:48:31).
  Command + observation recorded here because it explains why this verifier's artifacts are not under `/tmp`.

## 1. Receipt-presence observations (poll log)

`ls reports/round-9/freshness/` at 20:48:13, 20:48:22, 20:49:01, 20:49:27, 20:50:03, 20:50:45, 20:51:17,
20:51:26, 20:51:35, 20:52:0x UTC → directory held only `.scratch-v03/` (a sibling verifier's scratch,
containing Melqart/cippi material, i.e. F04 work). First F03 material landed during my continued polling:

| Observed (UTC) | Directory contents (F-relevant) |
|---|---|
| 20:52:06 | none (my `verify-F03.md` written 20:52) |
| 20:52:50 | none |
| 20:54:03 | `R9-F03a-receipt.json` (+`R9-F01b-*`) |
| 20:55:15 | `R9-F03a-receipt.md`, `R9-F03c-receipt.json`/`.md` |
| 20:56:12 | `R9-F03b-receipt.md`; `R9-F03b-receipt.json` moments later; `R9-F04a/F04c` also present |

All three hunter receipts (a/b/c) were on disk well inside the 20-minute poll cap, so §6 is a full
per-receipt adjudication, not an absence report. Scratching: F03a's `/var/tmp/r9f03a/ev/`, F03c's
`/var/tmp/r9f03c/` and F03b's `~/.cache/r9f03b/` were still present during verification, which allowed
**byte-level comparison against the hunters' own artifacts** rather than hash-claim trust alone.

## 2. Method and tooling

- **Independent artifact store:** every source cited below was re-fetched by *this* shard with
  `curl -sSL -A <browser UA>`, HTTP status, byte size and sha256 recorded in `~/.cache/r9v02/fetch-log.tsv`.
- **Quote test:** `~/.cache/r9v02/qcheck.py` — NFKC, quote/dash folding, whitespace collapse, then longest
  contiguous normalized token n-gram of the quoted text found in my own artifact; ≥10 tokens = containment
  pass. This is intentionally *my* copy, not the receipt's, so a receipt cannot pass by quoting itself.
- **Entry locators:** working-tree line numbers; the round-8 metadata sweep's +3 offset note
  (`reports/round-8/freshness/R8-F03-receipt.md` §intro) still applies.

## 3. Independent re-verification of the three legs the residual demands

### 3.1 Leg A — dated divine headgear identification (scholarly fulltext)

Bonatz, "The Iconography of Religion in the Hittite, Luwian, and Aramaean Kingdoms", IDD electronic
pre-publication (last revision 26 Feb 2007).
Fetched 2026-10-17: HTTP 200, **209300 bytes**, sha256
`3315a9bc15a6e96f3d7e3b8bc55f2bea805d9f9c9178c9854efffb7c8edca6aa` — byte-identical to the artifact
hash recorded in round 8 (`3315a9bc…6aa`), so the round-8 leg's substrate is reproducible. `pdftotext
-layout` → 1448 lines, also matching round 8.

Containment re-tests against **my** extraction (all ≥10-token passes):

| Quoted passage (round-8 set) | My artifact lines | Longest n-gram |
|---|---|---|
| "For the most part the male gods wear a short kilt and, corresponding to their hierarchical standing, a single or multiple horned, pointed cap, the typical headgear of Hittite deities since the Old Kingdom (cf. five-faced seals, 16th cent. …)" | 244–247 | 46 |
| "Behind the mountain gods, twelve nameless gods appear wearing kilts and single horned, pointed caps, and shouldering scimitars." | 292–294 | 18 |
| "Both wear the long robe and rounded skullcap, and both carry the lituus." | 406–407 | 13 |

So: horned-pointed cap as a **rank marker with gradient** (single vs multiple horns), dated to the
Yazılıkaya program, with an Old Kingdom comparator inside Hittite tradition. Deity/king separation has a
scholarly passage ("distinguished only by different hieroglyphic inscriptions and the winged sun disc",
IDD §1.4), and the chapter itself keeps the ambiguity honest (Kurunta at Hatip; Urhi-Teshub's seal
impressions). **Leg A: reproducible on my own copy.**

### 3.2 Leg B — deity/king identification (scholarly fulltext, escalated beyond round 8)

**New this round (my own probe, not inherited from round 8):** H. Kübra Ensert, "Is the small god figure
in the seal impression of Tudkhaliya IV, RS 17.159, Murshili II?", *Anadolu / Anatolia* 30 (2006), 93–101.
Fetched 2026-10-17: HTTP 200, 674838 bytes, sha256
`434498f95b93433e04cfd9b2d077cb5cbfbc4e38cb4d1004f7618647b0760ee9`
(`dspace.ankara.edu.tr/server/api/core/bitstreams/5fa1a57a-0ce2-4e86-8328-015c896c66d8/content`).

Passages relevant to the entry's lines 123/135/136/137 (my extraction, `ensert.txt`):

- "…the pointed hat was worn by both the kings and the gods since Khattushili III is depicted with the
  pointed hat at Abu Simbel. However the lack of the horn with the hat is important. Because the most
  important divinity sign is the horned hat in both Anatolia and Mesopotamia. Therefore these figures
  should be the figures of the kings and princes deified after death, but not of those in life." (txt 134–145)
- "…Van den Hout agrees that the Hittite kings were depicted with horny hats only when they were deified
  after death." (txt 176–177, citing van den Hout 1995a, 559)
- Footnote 34: "The mortal, deified while in life, was not allowed to have himself depicted with the horned
  hat and in god dress (Boehmer 1972-75, 431-432)." (txt 203)
- Identifies a Tudkhaliya figure at Boğazköy House-a wearing "a pointed hat with five pairs of horn, a
  short skirt and a pair of shoes with the upturned toes" (txt 181–183).

**Disagreement is documented, not smoothed:** the same article records that Akurgal and Alexander put
Khattushili III *in life* with the one-horned pointed hat at Fraktin, while Akurgal also held that "only
the kings, deified after death, are depicted with the horn" (txt 336, 345) — an unresolved scholarly
tension about exactly the god/king boundary the entry's line 123 brakes on.

A second independent scholarly line already in my store: Burcu Özer, *Yazılı Belgeler Işığında Hitit Kral
Heykelleri İçin Yapılan Ritüeller*, İstanbul Üniversitesi MA thesis, 2021
(`nek.istanbul.edu.tr/ekos/TEZ/ET003071.pdf`, HTTP 200, 4499395 bytes, sha256 `51a1d859…`): Chamber B
"Šarruma … başında tanrılık mertebesini ifade eden boynuzlu koni biçimli başlık" vs "Kral ise takke
biçimli başlıklı" (txt 6957–6973); the KBo 15.15 king-statue passage with "kalot başlık … Hatti stilinde
ayakkabılar" (txt 6817–6820, citing Kümmel 1967: 136–137) — containment 22 tokens.
**Leg B: supported by ≥2 independent scholarly fulltexts, with the contest disclosed.**

### 3.3 Leg C — Neo-Hittite later comparators and the earlier-comparator leg

**Later (Iron Age) comparators, primary + dated:**
- İvriz (hittitemonuments.com/ivriz/, HTTP 200, 12050 bytes, sha256 `19bb7858…ac91` — byte-identical to
  round 8): "The god wears a horned helmet, a symbol of divinity." (containment 10 tokens), plus the
  738–710 BCE dating of Warpalawa. Iron Age, must not be projected back.
- Carchemish III (Woolley–Barnett 1952, IA scan, 20335518 bytes, sha256 `85f6806e…a5d7` — byte-identical
  to round 8): "wears no horned crown of divinity" (Processional-Entry priestess, txt 620, 10 tokens);
  "part of a horned crown from a statue of a god which may have belonged to the same figure (B. 63a)."
  (txt 1084–1085, 11 tokens); the Water-Gate bull-legged deity "wears the horned crown" (txt 1346). This
  is a primary excavation report at object level.

**Earlier-comparator leg: still partial, and my sweep agrees with round 8's limit.**
- IDD states Hattian priority for the *earlier water-god* ("the earlier, earth-bound Water-god is
  indigenous to the Hattian population", txt 128) and dates Old Kingdom five-faced seals (16th cent.) as
  the internal earlier comparator; but **no Hattic-period headgear image** was retrieved by me either.
- Alaca Höyük Early Bronze "Royal Tombs" (2850–2450 BC) diadems/adornment: Wikipedia Alaca Höyük
  (HTTP 200, 305504 bytes) and Simpson ch. 32, *The Adventure of the Illustrious Scholar* (Brill 2018;
  PDF HTTP 200, 2730752 bytes, sha256 `8576b52e…`) both date the tombs and their gold diadems; neither
  pictures or identifies a horned-cap *image*, and the "Hattian" ethnic attribution of those tombs is a
  modern convention, not something either source asserts.
- Empire-period Alaca orthostats are the dated *royal-cap* comparator in the same town
  (`hittitemonuments.com/alacahoyuk/`, HTTP 200, 28578 bytes; "the gate complex probably dates to the
  13th century BCE").
- My own escalated attempt on the earlier leg: **failed to open a new earlier-image door** — see §4.
  The honest state is: earlier leg = Old Kingdom seal comparator + pre-Hittite objects, no Hattic image.

**Leg C verdict: later-comparator half supported (primary + dated, twice); earlier half partial, with the
gap now carrying *my* sweep receipts as well as round 8's.**

## 4. Access failures found by this verifier (command + status) — candidate "deeper limits"

| Attempt | Command (as run) | Result |
|---|---|---|
| Oreshko 2018 (round 8's kupaḫi garment-term source) | `curl -sSL -A <UA> …/hal-03880014/file/Oreshko…final.pdf` | HTTP 200 but **HTML bot-wall**, 12591 bytes (title "Making sure you're not a bot!"); same 12591-byte HTML from `hal.sorbonne-universite.fr/hal-03880014`, `shs.hal.science/…/document`, `hal.science/…/document` |
| Oreshko Wayback fallback | `archive.org/wayback/available?url=hal.sorbonne-universite.fr/…` | `{"archived_snapshots": {}}` — no snapshot |
| British Museum object record | `…/britishmuseum.org/collection/object/H_1862-0423-1` | **403** (5707 bytes) — same wall as round 8 |
| OI Chicago OIP 37 (Brett seal catalogue, has a "HITTITE SEALS — CONICAL HEADDRESSES" section per the search index) | `…/oi.uchicago.edu/sites/default/files/uploads/shared/docs/oip37.pdf` | HTTP 200 but **HTML page**, 183848 bytes (no PDF obtained) |
| Same catalogue on archive.org | `archive.org/download/ancientorientals00vond_0/…_djvu.txt` | HTTP 403 "Item not available" (lending-restricted item) |
| Grace White dissertation (Cappadocian glyptic iconography) | `isac.uchicago.edu` and `oi.uchicago.edu` variants | **404** (159503-byte HTML) on both hosts |
| `/tmp` for scratch | `mkdir -p /tmp/r9v02` | "No space left on device"; `df -i /tmp` → 0 free inodes |

These are receipts of *my* failures, not refutations of the sources' existence; a later round can retry
through a library or a mirrored host. Any F03 receipt that cites the Oreshko HAL file, OIP 37 or the BM
record needs either a cached/snapshot copy or this same failure recorded — a bare live-cite is not
reproducible as of 2026-10-17.

### 4.1 Re-tests of hunter-reported failures (my commands, 20:55–21:00Z)

| Hunter claim | My re-run | Outcome |
|---|---|---|
| CHD K fascicle PDF 404 (F03c) | `curl -sIL …/isac.uchicago.edu/sites/default/files/uploads/shared/docs/chd_k.pdf` | **404** — reproduced |
| e-CHD 404/403 (F03c) | `curl -sIL https://ochre.lib.uchicago.edu/eCHD/` | **403** — reproduced |
| Firenze UP DOI 403 (F03c) | `curl -sSL -A <browser UA> https://doi.org/10.36253/979-12-215-0109-4.12` | **200, 82148 B** (20:57Z) — the interstitial has cleared; F03c's scratch copy shows its 403 was real at fetch time, but this limit is now stale (§6.3) |
| Google Books API 429 (F03c) | same endpoint with my UA | **404** (method/UA-dependent; both non-success — the variance itself is worth recording) |
| British Museum 403 + no Wayback snapshot (F03a) | `curl -A <UA>` and `archive.org/wayback/available` | **403 / `{}`** — both reproduced |
| Met collection API unusable (F03a) | `…/v1/search` (410) and `…/v1.1/search` | v1 410 reproduced, **v1.1 200 and usable** — a live replacement F03a did not try (§6.1 defect b) |
| Penn Museum 403, Louvre search 429, museum-digital, Wikidata zero-hit (F03a) | not re-run one-by-one | accepted as recorded; none is load-bearing for a passage leg, and their file/status fields are of the same shape as the failures I did reproduce |

## 5. What an F03 receipt must demonstrate (adversarial checklist)

1. **≥2 escalated strategies beyond `en.wikipedia.org`**, one of them primary/museum-record or scholarly
   fulltext, with `file:line`/page locators and quote-fidelity treatment of OCR/diacritics.
2. **Datedness**: every headgear claim tied to a dated object/monument (Yazılıkaya program; Boğazköy
   House-a; Abu Simbel; Fraktin; İvriz 738–710 BCE) — not a timeless "Hittite look".
3. **Layer discipline**: depicted rank (single vs multiple horns; cap without horn) kept separate from
   deity/king identification, and figurative depictions kept separate from textual garment terms
   (kupaḫi/kalot/TÚG layers).
4. **No back-projection**: Iron Age Carchemish/İvriz/Malatya material labelled as such, not folded into
   the Empire period (entry line 49 terminology trap).
5. **Earlier-comparator honesty**: if Hattic leg stays unresolved, the receipt must name what specifically
   remains unretrieved and the sweeps that failed (my §4 table is available as a cross-check).
6. **Counts carry command + date; negatives carry sweeps;** no fabricated page/plate numbers.
7. Receipt must not restate round-8's passages as if newly retrieved without saying so.

## 6. Per-receipt verdicts (R9-F03a/b/c)

### 6.0 Shared substrate checks (all three receipts)

- **Entry hash:** all three receipts claim `entry_sha256 = a8e421f7118e…`. My
  `sha256sum corpus/knowledge/civilizations/anatolia-hittite.md` (2026-10-17) returns exactly that, and
  `git status --porcelain` on the file is clean → the receipts attach to committed text and my locators
  (123 / 135 / 136 / 137 / 49) are the same rows the receipts name. ✓
- **`/tmp` inode exhaustion** is independently corroborated: F03a and F03c each record the `df -i /tmp`
  observation; I hit the same wall at 20:48:31 and also moved scratch (`~/.cache/r9v02/`). ✓
- **Hunters' scratch dirs were still on disk during verification** (`/var/tmp/r9f03a/ev/`,
  `/var/tmp/r9f03c/`, `~/.cache/r9f03b/`), which allowed *byte-level* comparison against their own
  artifacts in addition to live re-fetch.

### 6.1 R9-F03a — primary-source/museum-record hunter → **PASS** (`partial-support` upheld; 2 disclosure defects)

**Artifacts (mine vs theirs vs claimed):** 9/9 byte-identical — Cleveland 1971.45 `30e4e344…`, 1985.70
`0880e7d7…`, 1973.19 `b9d5dfd6…`, `?q=Hittite` search `09b7aed0…` (my parse reproduces `info.total = 5`
and the same five accessions), Louvre AO 11073 `9444d7dc…`, AO 11072 `5d3ea9c8…`, AO 8191 `f0db48e4…`,
Hittite Monuments Alaca `e5fd321c…`, Yazılıkaya `28620a2f…` (the last two also match *round 8*'s hash for
the same URL). The two Turkish-ministry pages differ from my live copy by ~250 bytes **of markup only** —
`difflib` over extracted text reports the text byte-identical, so no content drift.

**Quotes:** "This large basalt sculpture is exceptionally rare in depicting a Hittite god or priest-king
wearing a horned conical crown, false beard, and long robe." — verbatim in my copy of the Cleveland JSON
(field `description`, closing sentences, corpus `(?q=1971.45)`); "a seated god or king" / "The standing
figure is a priest pouring a liquid offering." — verbatim in 1985.70. Both are dated (c. 1600 BCE;
1400–1200 BCE) and accessioned, and the receipt's own `does_not_support` correctly refuses to project
1971.45 onto the imperial Yazılıkaya rows.

**Negative sweeps:** reproduced. My own word-boundary regex over my own copies of the two ministry pages
and the two Hittite Monuments pages returns **0** hits for
{horn, horned, crown, cap, headdress, helmet, boynuz, başlık, takke, tiara}; the same sweep over the three
Louvre notices returns no headgear term either (one `cor` hit per page is a substring artefact of my
pattern, not a word).

**Defect (a) — quote-fidelity disclosure is wrong about the ministry pages.** The receipt's
`quote_fidelity` says Turkish diacritics "are preserved in the artifact text and rendered here as
delivered where quoted (e.g. 'Bogazkoy Yerkapi Sphinx' appears without diacritics in the retrieved
English-language page text itself)". The pages *do* carry diacritics (HTML-entity-encoded:
`BO&#x11E;AZK&#xD6;Y` = Boğazköy, `Yerkapı`, `ALACAH&#xD6;Y&#xDC;K`, `Alacahöyük`), so the excerpt is a
silently diacritic-stripped rendering; the ALC01 excerpt also drops a leading word without an ellipsis
("The museum displays artefacts…" for "The Alacahöyük Museum displays artefacts…"). Substance unaffected;
the disclosure block needs correcting (or the excerpts restoring) — this is a rule-6-class finding
("every quote names its location" + fidelity disclosure), not a fabrication.

**Defect (b) — the Met route is reported as closed when it is not.** Its `access_failures` says the "API
path is gone (HTTP 410)". The 410 is real, but it is v1's documented retirement (2026-10-01) with a live
replacement the receipt did not try: `…/public/collection/v1.1/search?q=Hittite` → `total: 76`;
`q=Hattian` → `total: 48`; `q=55.137.14` → objectID 324453. I used v1.1 successfully. The receipt's Met
record (Hattian axe, 55.137.14) is otherwise corroborated: my FetchURL read of the object page shows
"Restituted. This artwork was restituted in September 2026. It is no longer in the museum's collection.",
Culture: Hattian, ca. 2300–2000 BCE, Bronze — and the object 404s on **both** v1 and v1.1 object
endpoints, which is consistent with post-restitution removal and *supports* the receipt's reading. Minor
`to-verify`: the string "Object Number: 55.137.14" did not render in my FetchURL read (the accession is
confirmed only through the API search index).

**Verdict:** PASS. The result label `partial-support` is accurate; its limits match my §3 (no Hattic
headgear witness, no plate-level reading), and the museum-object leg it claims is genuinely new and dated.

### 6.2 R9-F03b — scholarly-fulltext hunter → **PASS** (`partial-support-or-better` upheld; 1 unsubstantiated bibliographic row)

**Artifacts:** 5/5 byte-identical — Ensert/Ankara `434498f9…` (equals my own independent fetch),
Durusu-Tanrıöver/Bilkent repo `05debcfe…`, Sacred Landscapes PDF `e9edf217…` (my re-download HTTP 200,
8550096 bytes), Wygnańska/PAM `cf59066c…`, Klaunzer/Metalla `0a750ba3…`. Citation check: the Ensert
article is foliated **93–109** in my extraction (folios present: 93–107, 109; 17 PDF pages), so its
"*Anadolu/Anatolia* 30: 93–109" is correct, not the 93–101 a shorter read might suggest.

**Quotes, under its own declared extraction mode:** F03b declares raw-mode `pdftotext` and folds
diacritics for testing. Re-running my containment checker accordingly: Klaunzer p. 89/90 quotes → **19**
and **17** tokens in raw-mode extraction (my `-layout` run gives only 7 — i.e. the receipt's method
declaration is load-bearing and it reproduces); Taracha p. 60 → **31/18**; Gilibert n. 46 (Malatya) →
**27**; Durusu-Tanrıöver p. 301 → **10–11** on `-layout`. All ≥10 under a disclosed mode; the Disagree-
ment it discloses (Südburg Šuppiluliuma in a horned hat; Muršili III seal; Emirgazi) matches what I
independently found in Ensert, so its "not exceptionless" caveat is real scholarship, not hedging.

**Defect — bibliographic-control claim not substantiated by its own manifest.** §2 states that the
Hethitologie Portal Mainz bibliography page carried the row `Hout Th.P.J. van den 1995a | Tudḫalija IV.
und die Ikonographie hethitischer Grosskönige des 13. Jhs. | BiOr 52 545-573`. The artifacts in its
manifest do not contain it: `hethport62.html` (`b762edd7…`, 1744 B) is the portal's relocation notice
("Das Hethitologie-Portal Mainz ist aktuell erreichbar unter: https://hethport.net/"), and
`hethport-62.html` (278 B) is a bare "302 Found" page. `grep -c -i 'BiOr\|Tud' hethport62.html` → **0**.
The row is plausible (it is the article this residual has chased since round 8) but at receipt level it is
`to-verify`: it must be re-derived from a page that actually carries it, or dropped. It is bibliographic
control, not a passage leg, so the F claim's passage requirement is unaffected.

**Verdict:** PASS. Legs 1–3 (rule-stating royal/god headgear contrast; dated labelled identification;
dated Iron Age Malatya/Karkemiš comparator) are supported by peer-reviewed fulltexts new to round 9; leg 4
is partial exactly as I found independently (dated pre-Hittite diadems, no Hattic horned cap).

### 6.3 R9-F03c — alternate-angle hunter → **PASS** (strongest disclosure discipline; 1 stale limit)

**Artifacts:** 6/6 byte-identical — Hoffner djvu `f94d303f…`, Bilkent Anodos `c2321a6a…`, PAM diadem
`cf59066c…`, Simpson `8576b52e…`, votive djvu `ff15cf2e…`. One benign difference: `hoffner-meta.json`
differs from my re-fetch **only** in IA's dynamic `server` / `workable_servers` fields (ia903204 vs
ia803204) — expected for that API, not a content discrepancy.

**Quote methodology — independently reproduced.** This is the receipt's strongest feature and it checks
out: my own containment runs on *my own* raw extractions reproduce its disclosed raw-interleaved figures
**exactly** — Q_P1 **10** tokens (theirs: 10), Q_P5 **8** (theirs: 8), Q_P6 **8** (theirs: 8), Q_P3a/b
**9/8** (theirs: 9/8) — while its column-reconstruction tests pass at 25–74 tokens. That is the signature
of an honest two-column handling rather than a quote laundered to fit. Key quotes re-verified in my
copies: "…the term Jcupahi-, which denotes a type of headgear" (20 tokens), TÚG kureššar "headgear
characteristic for women" (11), Bilkent "firmly embedded in a Pre-Hittite sequence … erroneously referred
to as 'Hittite' products" (24) and the calibrated bracket "upper limit at around 2,300 BC cal. … around
2,000/1,950 BC" (25), Simpson diadems (30).

**Stale limit (not an error):** its deeper-limit list closes the Firenze University Press CC-BY chapter
("Kubaba and other Divine Ladies…") as unreachable (Cloudflare 403) — its own scratch proves that was
true at fetch time (`fup-landing.html`, 5538 B, "Just a moment…"). But by 20:57Z the same DOI returned
**HTTP 200 / 82148 bytes** to me: the interstitial has cleared, so that Iron-Age divine-head-dress lead has
re-opened and can be retrieved by the orchestrator (its `to-verify` status can be retired on re-fetch).

**Verdict:** PASS. `partial-support` scope accurate; deeper-limit naming precise; no over-claim; its
cross-check note about this file's §5 checklist is accurate and I adjusted nothing because of it.

### 6.4 Cross-receipt checks against the F claim

- **No passage recycled as new:** all three receipts re-fetch and hash every shared substrate
  (Hittite Monuments Alaca; Wygnańska/PAM; Simpson) and name round 8's differing sentences; F03a's
  `positive_reuse_check` and F03c's `new_vs_round8` both hold up against my artifact hashes.
- **"≥2 of the 4 move to partial-support-or-better on primary or scholarly passages":** for this residual
  F03 alone, all three hunters land at partial-support or better with primary or scholarly passages
  (museum object records; peer-reviewed journal fulltexts; philological fulltexts). The earlier-Hattic
  limb stays open in all three — which the claim explicitly permits — and each names it as unretrieved
  with its sweeps, as §5.5 required.
- **Independence:** my §3 re-derives the three legs from artifacts I fetched myself (IDD, Carchemish III,
  Ensert, İvriz, Özer 2021, Alaca/Simpson), not from the receipts; the overlap is convergent, not copied.
- **Residual disposition to carry:** `partial-support` (up from `unresolved`), with three named open
  limbs — Hattic headgear witness; plate-level cap construction (Seeher 2011); first-hand van den Hout
  1995 / Goetze 1955. None of these is claimed closed by any receipt, and none is contradicted by my own
  sweeps.

## 7. Limits of this verification

1. I did not inspect plates or photographs at image level (Seeher 2011 plates, Bittel Tafeln); all
   headgear readings here are text/OCR level, as in round 8.
2. My earlier-comparator sweep found no Hattic headgear image; the IDD Hattian water-god sentence (txt 128)
   is the nearest scholarly statement obtained and does not itself picture headgear.
3. The Ensert article reports a live scholarly disagreement (Akurgal/Alexander vs the posthumous-deification
   rule); this verification does not adjudicate it — it records it as the reason the entry's line 123 must
   stay a characteristic-representation rule.
4. Artifact hashes in §2–§3 are of *live* fetches on 2026-10-17; Wikipedia prose drifts (the live
   Yazılıkaya article's byte size/sha256 no longer matches round 8's: mine 275572 bytes /
   `3be1075d…c07` vs round 8's 275571 / `939565a7…1811`), so receipts quoting Wikipedia should carry their
   own fetch hash, as round 8 did.
5. **Coverage limit of this verdict.** I re-fetched and hashed the load-bearing artifacts of all three
   receipts and containment-tested their passage quotes, but I did not re-run every negative sweep or
   every access failure one-by-one (§4.1 shows what I did re-run and what I accepted as recorded). Where a
   hunter's statement was not independently reproduced, this file says so rather than endorsing it.
6. **Both defects are disclosure-level, not evidence-level.** F03a's ministry-page excerpts and F03b's
   BiOr row misdescribe their own artifacts, but no *passage leg* of either receipt failed verification;
   the classification I recommend for the F claim is therefore `partial-support` with two
   correction-notes (`to-verify` on the BiOr row; quote_fidelity block to be amended), not a downgrade.
7. **This verifier wrote exactly one file** — this one. It made no corpus, tool, gate, or hunters'
   receipt edits, and it does not adjudicate the residual's final disposition (reconciliation belongs to
   the round-9 orchestrator). Hunters' raw labels are untouched by anything above.

*Every quote in this file was matched by `qcheck.py` against an artifact fetched by this shard; token
counts are the longest contiguous normalized n-gram.*
