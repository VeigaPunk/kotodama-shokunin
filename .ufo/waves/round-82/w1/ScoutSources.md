# ScoutSources — round 82 w1 (claim D recon: independent source opening)

Seat: `ScoutSources` (leaf scout). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Wave: round 82 w1, milestone r82-v1. Lane base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` (no lane file read or written; this seat writes only its own report and stage).

## Verdict

1. **All three planned rows open cleanly and carry a locatable, <=25-word body quote that occurs exactly once**, live *and* in a same-page Wayback capture: S904 (18 words), S905 (20), S906 (22). Plus a fourth candidate the L1 asked for, Tacitus *Germania* XXI (20 words), which is the **stronger S905 occupant**.
2. **S907's planned reject reason is falsified**: a plain fetch *does* reach article prose on `1911_Encyclopædia_Britannica/Guest` (the whole 1911 article, 43 words, begins 「GUEST (a word common to Teutonic languages…」). The "Wikibase scaffold" reading is an artifact of raw Parsoid template JSON that the page emits *inside the article region* — the prose follows it two spans later. **The reject must not be filed on the scaffold reason.** A different, measured ground is available (§5) if the L1 still wants the row out.
3. **Freshness caught**: Gutenberg eBook #1727 (*Odyssey*) was revised **2026-11-02**, two days before this round; the 2026-10-26 Wayback capture predates that revision and carries `Most recently updated: December 2, 2023`. The quote is unchanged in both. Cite the live fetch as anchor, the capture as durability copy, and say the capture is one revision behind.

## 1. Method (repeatable)

- Fetch: `curl -sSL --max-time 90 -o <file> -w 'HTTP %{http_code}, %{size_download} B, ctype=%{content_type}\n' <url>`, once with the tool default UA and once with `-A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'`. No proxy, no automation, no challenge met: `automation: none`.
- Plain UA is the tool's default: `curl 8.23.0` → literal string `curl/8.23.0`.
- Way-back: CDX exact query per URL, then the item at `https://web.archive.org/web/<ts>id_/<url>`. Four of the five captures arrive **gzip-compressed as stored** (the `id_` payload is the stored record) and were decoded with `zcat` before hashing/extracting; both the transferred-bytes sha256 and the decoded sha256 are in each evidence file.
- Text extraction: html → drop `script/style`, cut to `mw-parser-output`, tags → **a space**, entities decoded, then Unicode whitespace fold (`re.sub(r'\s+',' ',t)`), optional NFKC. Plain-text rows: whitespace fold only. Both are scripted in the evidence generator; the rule is stated per file under `extract:`.
- Offsets are character offsets into that folded text, and each file states `exactly 1 occurrence`, checked in both the live body and the capture body.

## 2. Source table (all numbers from the commands above)

| row | URL | plain UA | browser UA | wall | live bytes | Wayback capture | capture HTTP / bytes |
|---|---|---|---|---|---|---|---|
| S904 | `https://www.gutenberg.org/cache/epub/1727/pg1727.txt` | HTTP 200, 717782 B | HTTP 200, 717782 B | absent | 717782 | `20261026212950` | 200, 265452 B transferred → 717784 B decoded |
| S905 A | `https://en.wikisource.org/wiki/The_Poetic_Edda_(tr._Bellows)/Hovamol` | HTTP 200, 510701 B | HTTP 200, 510701 B | absent | 510701 | `20260918023250` | 200, 40729 B → 308283 B decoded |
| S905 B | `https://en.wikisource.org/wiki/Germania_(Church_%26_Brodribb)` | HTTP 200, 163266 B | HTTP 200, 163266 B | absent | 163266 | `20261007211035` | 200, 41873 B → 163433 B decoded |
| S906 | `https://www.gutenberg.org/cache/epub/26073/pg26073.txt` | HTTP 200, 853821 B | HTTP 200, 853821 B | absent | 853821 | `20260915020048` | 200, 332350 B → 853821 B decoded (**sha256 identical to live**) |
| S907 | `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Guest` | HTTP 200, 60273 B | HTTP 200, 60273 B | absent | 60273 | `20240912100001` | 200, 37460 B (uncompressed) |

QUALITY 22 records, verbatim as filed in each evidence file (each line carries both requests):

```
S904: UA "curl/8.23.0" -> HTTP 200, 717782 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 717782 B, wall absent
S905: UA "curl/8.23.0" -> HTTP 200, 510701 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 510701 B, wall absent
S905B: UA "curl/8.23.0" -> HTTP 200, 163266 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 163266 B, wall absent
S906: UA "curl/8.23.0" -> HTTP 200, 853821 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 853821 B, wall absent
S907: UA "curl/8.23.0" -> HTTP 200, 60273 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 60273 B, wall absent
```

Shape check (`grep -Ec 'UA "[^"]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'` = 1 line per file; `grep -o … | wc -l` = 2 on that line). Wall-marker sweep over both UA bodies — `grep -c -i -E 'Client Challenge|Just a moment|Attention Required|cf-browser-verification|Enable JavaScript and cookies'` — 0 in all ten bodies.

Redirect/canonical probe (`curl -sS -o /dev/null -w '%{http_code} redirects=%{num_redirects} final=%{url_effective}'`, no `-L`): all five planned URLs answer **200, redirects=0, final=itself**, i.e. each URL already is the canonical slug, so the CDX query was run on the same slug (QUALITY 21 needs no composition step here).

## 3. Per-row detail

### S904 — Homer, *Odyssey* trans. Butler (Gutenberg #1727)

- **Section**: Book XIV (the body heading `BOOK XIV` at e-text line 6099; the front contents list also says `BOOK XIV` at folded offset 1108, so a naive `BOOK XIV` search hits twice — the quote is after the second).
- **Span**: lines 6150-6153 —
  「To this you answered, O swineherd Eumaeus, "Stranger, though a still poorer man should come here, it would not be right for me to insult him, for all strangers and beggars are from Jove."」
- **Quote (18 words, 87 chars)**: `it would not be right for me to insult him, for all strangers and beggars are from Jove`
- Folded-text offset **354019** of 696070; `occurrences=1`. Capture: offset **354017** of 696068; `occurrences=1`. The phrase is **not** a contiguous byte substring of the artifact as served (`raw-contiguous: 0`): the e-text is hard-wrapped, so any re-opener must fold whitespace first.
- **Freshness**: live vs capture line-diff (`difflib.unified_diff` on CRLF-split lines) —
  ```
  -                Most recently updated: December 2, 2023
  +                Most recently updated: November 2, 2026
  -Leipsic Teubner edition of 894 makes Books ii. and iii. end with a
  +Leipsic Teubner edition of 1894 makes Books ii. and iii. end with a
  -when the man struck up with his tune.38
  +when the man struck up with his tune.]38
  ```
  Two typo repairs and the stamp; bytes 717782 live vs 717784 decoded capture (`raw:0`/`dec:1` diff count 685258 is the 2-byte line-ending shift downstream of line 20, not 685k independent edits). **The anchor quote is untouched.** File sha256 `b167ce5e…bbc69`.
- **Tier**: **A**, scoped to *the Greek epic's own statement of the guest-right norm — the swineherd's ground that "all strangers and beggars are from Jove" — in Butler's public-domain English (not the Greek text)*. Note the scope limit out loud: this is primary evidence of the *represented* norm, not of Attic law; a legal-institution claim needs S905-B/S906 alongside it.

### S905 candidate A — *Poetic Edda* trans. Bellows, Hovamol (Wikisource)

- **Section**: Hovamol **stanza 3** (the page prints `3.` in `<span class="ws-poem-versenum">`), the cold-comer stanza:
  「Fire he needs / who with frozen knees / Has come from the cold without; / Food and clothes / must the farer have, / The man from the mountains come.」
- **Quote (20 words, 104 chars)**: `Fire he needs who with frozen knees Has come from the cold without; Food and clothes must the farer have`
- Folded offset **20579** of 63728; `occurrences=1`; capture offset **3911** of 46994; `occurrences=1`. The capture is a *complete* copy for the anchor: both bodies carry stanzas through `165.` (count 2 occurrences each of `164.`/`165.`, identical tails).
- **The L1's structural doubt, tested four ways** — this is the row's real risk and it is a *method* risk, not a source defect:

  | extraction | occurrences of the 20-word span |
  |---|---|
  | raw HTML as served | 0 |
  | tags→space + **ASCII-only** fold (`[ \t\n\r]+`) | 0 |
  | tags→space + **Unicode** fold (`\s+`) | **1** |
  | tags→space + NFKC + fold | **1** |
  | tags→**nothing** + Unicode fold | 0 |

  Cause, observed in the markup: stanza 3 is `<div class="ws-poem-stanza">` holding `<span class="ws-poem-line">` hemistichs separated by `<span class="wst-cesura">` containing **U+2003 EM SPACE** (6 × U+2003 in the ±1-stanza segment; **0 `<td>`**). So it is *not* table cells — the L1's description is inaccurate — but the hemistichs are separate inline spans whose only separator is a Unicode space, and inline `<link>` elements sit **inside** the line spans (so a tag-stripper that deletes tags without substituting a space merges words). **A contiguous 20-word verbatim span does exist** and is found by the lane's standard normalise (tag→space, whitespace fold); the re-opener note must say so, or a reviewer will read the 0 as absence.
- **Tier**: **A**, scoped to *the Eddic-gnomic statement of the cold-comer's claim on fire, food and clothing — Bellows 1923 English*. Again: literary/gnomic, not a law code; and Bellows' stanza numbering is the translator's, not the Codex's.

### S905 candidate B — Tacitus, *Germania* trans. Church & Brodribb (Wikisource) — **recommended occupant**

- **Section**: chapter **XXI**; the page renders the heading `XXI [ edit ]` immediately before the sentence (preceding chapter's close: "…nor are there any advantages in childlessness. ( Latin ) XXI [ edit ] It is a duty among them…").
- **Span (the run the L1 named, contiguous)**:
  「No nation indulges more profusely in entertainments and hospitality. To exclude any human being from their roof is thought impious; every German, according to his means, receives his guest with a well-furnished table.」
- **Quote (20 words, 130 chars)**: `No nation indulges more profusely in entertainments and hospitality. To exclude any human being from their roof is thought impious`
- Folded offset **25246** of 57360; `occurrences=1`. Capture: **same offset 25246 of 57360, `occurrences=1`**. **`raw-contiguous: 1`** — the only one of the five that is a contiguous byte substring as served, i.e. the most durable anchor of the set. Live/capture sha256 differ (live `8138fd6b…`, capture decoded `a6777241…`); the difference is skin classes only — first differing byte 597 is `skin-thumbsize-clientpref-standard skin-underline-clientpref-browser` (live) vs `skin-thumbsize-clientpref-standard` (capture), and folded text length is **57361 in both**.
- **Tier**: **A**, scoped to *the Roman ethnographic report (AD 98) of Germanic hospitality as a duty with sacral sanction — exclusion "thought impious"* — with the standing caveat that Tacitus is an outsider moralist writing against Roman luxury (the same chapter's frame), which the entry must not launder into ethnography.

### S906 — Ovid, *Metamorphoses* VIII-XV trans. Riley (Gutenberg #26073)

- **Section**: Book **the Eighth** (`BOOK THE EIGHTH.` at line 428), lines 1647-1650, Baucis and Philemon (the theoxeny of Jupiter and Mercury):
  「To a thousand houses did they go, asking for lodging and for rest. A thousand houses did the bolts fasten {against them}. Yet one received them, a small one indeed, thatched with straw.」
- **Quote (22 words, 120 chars)**: `To a thousand houses did they go, asking for lodging and for rest. A thousand houses did the bolts fasten {against them}`
- Folded offset **89275** of 814397; `occurrences=1`. Capture: **identical file** — decoded capture sha256 `6eb47750…` equals the live sha256, same offset, same count. This is the cleanest capture of the set.
- **Body-scope hazard, observed**: the same story is stated three times at three levels — `FABLE VI. [VIII.611-737]` argument (line 1620-1622: "…are received by Philemon and Baucis, after having been refused admittance by their neighbours"), the narrative body (1647-1650, quoted above), and `EXPLANATION.` (1811+, Riley's own 1851 commentary, which reads the theoxeny as a refraction of Abraham/Elijah). Only 1647-1650 is body text; the other two are translator frame. Riley's `{…}` braces mark words he supplied — the entry must either keep the braces inside the quote or stop the quote before them; do not silently drop them.
- **Tier**: **A**, scoped to *the theoxeny narrative pattern as Ovid tells it in Book VIII — gods in disguise test a hundred roofs, refusal is punished, one household receives them — Riley 1851 English*. Do **not** import the `EXPLANATION`'s Abraham/Elijah diffusionism: that is exactly the Frazerian-adjacent comparativism QUALITY 2 flags.

### S907 — EB11 "Guest" (reject candidate, under test) — see §5

## 4. CDX controls (QUALITY 21 + 24)

Filed raw at `stage/ScoutSources/controls.txt`. Same query shape for every probe: `http://web.archive.org/cdx/search/cdx?url=<encoded>&output=json&limit=-3&filter=statuscode:200`.

- **Positive control 1** — `…url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHospitality…` → HTTP 200, 564 B, 3 status-200 rows (`20261012033337`, `20261014092519`, `20261022132155`). The query shape is known-good, so a `[]` below means absence, not a malformed query.
- **Positive control 2** — `…url=example.com/…` → HTTP 200, 435 B, 3 rows. Second host, same shape.
- **Deliberately empty probe** — `…url=example.com/no-such-page-r82-probe-xyzzy…` → HTTP 200, body `[]`, 3 B.
- Per-row CDX exact queries (full URL in each evidence file under `cdx-query:`): S904 3 rows; S905-A 3 rows; S905-B 4 rows; S906 3 rows; S907 2 rows — **every planned row has at least one status-200 capture of its own URL**, so no row here needs a "no capture" ruling at all.

## 5. S907 adjudication — the planned reject reason is falsified

**Claim under test** (from the round brief): "plain fetch returns the Wikibase scaffold, not article prose".

**Measured** — `curl -sSL 'https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Guest'` → HTTP 200, 60273 B, `text/html`, wall absent under both UAs, `redirects=0`. Folded text of the article region, offset 849:

> GUEST (a word common to Teutonic languages; cf. Ger. Gast , and Swed. gäst ; cognate with Lat. hostis , originally a stranger, hence enemy; cf. "host"), one who receives hospitality in the house of another, his "host"; hence applied to a parasite

That is **article prose, present, 43 words** — the complete 1911 entry (vol. 12, p. 673, `oldid=6456786`, last edited 2016-09-25), not a placeholder and not a Wikisource "no article text" page (`grep -c 'noarticletext'` = 0).

**Where the "scaffold" reading comes from, observed**: the same article region also renders raw Parsoid template JSON as literal text — `{"template": {"target": {"wt": ":MediaWiki:Proofreadpage_pagenum_template"…` and `{"template": {"target": {"wt": "#lst:Page:EB1911 - Volume 12.djvu/698"…` (`text.count('"template":')` = 2), immediately **before** the prose, plus a leaked `</templatestyles>` tag. A probe that greps for scaffold markers, or that stops at the first non-prose run, concludes "scaffold"; the prose is two spans later. So the observation is real, the conclusion drawn from it is not.

**QUALITY 27 shape** — artifact, span, presence:

```
artifact: .ufo/waves/round-82/w1/stage/ScoutSources/S907.txt (capture bytes, sha256 f6db75f387e95d9d83fc2515a09c4b3acfd66605fe876c995bd0c0c490b26718, live HTTP 200 / 60273 B; Wayback 20240912100001 HTTP 200 / 37460 B)
span: 「one who receives hospitality in the house of another」
finding: PRESENT — 1 occurrence at folded offset 1002 of 1820 in the live body, and 1 occurrence at offset 492 of 1803 in the 2024-09-12 capture.
counter-span: 「GUEST (a word common to Teutonic languages」 — PRESENT (offset 849); the Wikibase/template scaffold is PRESENT too ("template": ×2) but precedes the prose and does not replace it.
```

**What a reject *can* stand on (measured, if the L1 still wants it out)**: the article is a 43-word etymology gloss ("a word common to Teutonic languages… cognate with Lat. hostis") with **no institutional, legal or sacral content** — it says what the *word* means, not what guest-right is, and carries no sentence a claim about hospitality-as-sacral-institution could rest on. Under QUALITY 6 that makes it **tier C for claim D's scope** (a lead, never sole support). The honest reject reason is "etymology only, 43 words, no institutional content", not "scaffold".

**Slot replacement probed**: `1911_Encyclop%C3%A6dia_Britannica/Hospitality` → **HTTP 404** (42948 B error page), so the obvious EB11 replacement headword does not exist on Wikisource; do not plan it.

## 6. S905 slot: recommendation

- **Give S905 to Tacitus, *Germania* XXI.** Reasons: the anchor is `raw-contiguous: 1` (survives a re-opener who does no folding at all), it is a *primary* witness to hospitality carrying sacral sanction ("to exclude any human being from their roof is thought impious") which is precisely claim D's subject, and its chapter anchor (`XXI`) is unambiguous.
- **Carry Hovamol as a candidate, do not reject it.** The span exists (20 words, 1 occurrence live + 1 in capture) and its content — fire, food and clothing owed to the cold-comer — is the Eddic half of the same institution. The only thing against it is a *re-opening footnote* (Unicode folding required); that is a method note, not a source property, and QUALITY 10/12 forbid filing it as a reject. If both land, Hovamol is a second row in the S905 block's wake, not a replacement.
- **L1 ruling (recorded after this report was filed)**: S905 = Tacitus, with the 20-word span above adopted verbatim (their capture `20260206213325`; mine `20261007211035` — both status-200 copies of the same page, same span, same folded offset 25246). Hovamol is carried and additionally disqualified from the slot by ScoutGap's duplicate-document check (Bellows 1923 is already row S320, Gutenberg #73533 — same work). S907 stands as a row at tier C, scope narrowed to the etymology gloss, with the scaffold ground withdrawn; this seat's extraction-artifact finding became the round's mined mistake and the basis of QUALITY 30.

## 7. Defects that would refuse a row — and what does not

**Would refuse (none of the planned three fails these):**

- No same-page capture with the anchor present → all four planned URLs have it (§2).
- Wall present under both UAs → absent under both for all five.
- Article/argument instead of body text → only a hazard for S906 if the quoter takes line 1622 (FABLE VI argument) instead of 1647-1650.
- A quote that is a caption/alt/heading → none; all five sit in running prose or the poem's own stanza text.

**Would *not* refuse, but must be stated in the row:**

- **S904 capture is one revision behind**: live stamped `November 2, 2026`, capture stamped `December 2, 2023`; the two typo repairs listed in §3 fall outside the quote. A row that says "capture 2026-10-26 = live" would be false by three lines; say capture + one revision drift.
- **S905-A capture is much smaller than live** (308283 B decoded vs 510701 B; folded 46995 vs 63728 chars) yet carries the full poem (stanzas through 165 in both) and the anchor. The byte gap is skin/menu markup, not missing text — but a reviewer who compares sizes without comparing stanzas will misread it.
- **S905-A span is folding-dependent** (§3 table). The row must ship the normalise line or a reviewer will reproduce the 0.
- **S906's translator braces** `{against them}` are inside the quote and must stay inside it.

## 8. Files written

- `.ufo/waves/round-82/w1/ScoutSources.md` (this report).
- `.ufo/waves/round-82/w1/stage/ScoutSources/S904.txt` — capture-ready block, sha256 `10e87157b0997c6a84ab4b7a0f658545b5e85f131cb77deb287fecce039ed88a`.
- `.ufo/waves/round-82/w1/stage/ScoutSources/S905.txt` — Hovamol block, sha256 `a617ff9e61a668eb6861e6f2fd1ca2d26260b7570c55774d987bba90ce5b068c`.
- `.ufo/waves/round-82/w1/stage/ScoutSources/S905-tacitus.txt` — Germania block, sha256 `c0dbc67e3764d9f9db11ba7cc2193b4f353ad041eb6740e096fae061a2ed8992`.
- `.ufo/waves/round-82/w1/stage/ScoutSources/S906.txt` — Ovid block, sha256 `92788e1f58eb68045859fbefbc9c8b54c8bd44f5ab9dc8a0bcb9452808018a92`.
- `.ufo/waves/round-82/w1/stage/ScoutSources/S907.txt` — EB11 Guest block (whole-document window, 1820 chars < 4096), sha256 `8bde6fc29f5f0ed5c75209bab494da23d8dae2a95a3cd726d51a062e23bfc64a`.
- `.ufo/waves/round-82/w1/stage/ScoutSources/controls.txt` — the four CDX probes and the six redirect probes, raw output.

Each evidence block carries the header lines `row, slot, url, wayback, fetched, ua-records, bytes, sha256, extract, window-scope, window, window-sha256, quote, quote-words, quote-chars, quote-found-verbatim, quote-raw-contiguous, locator, wayback-bytes, wayback-sha256, wayback-transferred-sha256, wayback-quote, cdx-query, reopen, automation`, then `--- window ---` and `--- quote ---` bodies so a counter can recompute the window digest.

## 9. Scratch

All working files lived under `/fast/scratch/hyaku/kotodama-r82/ScoutSources/` and were deleted after the stage copies were written (`rm -rf /fast/scratch/hyaku/kotodama-r82/ScoutSources`, run from the fleet root with an absolute path; the seat root `/fast/scratch/hyaku/kotodama-r82` was left in place). No lane file other than this report and the stage directory was touched; no git/jj command was run in the lane; no install was made (curl 8.23.0 and python3 were already present, so the install log is empty).
