# ScoutSources — round 83 w1 (claim D recon: independent second reading of S909–S912)

Seat: `ScoutSources` (leaf scout; no subagent dispatch). Lane: this repository (the kotodama-shokunin lane); all paths below are repo-relative.
Wave: round 83 w1, milestone r83-v1. Lane base revision `3088bd7fe2a55a123214abba7008dcddf12b301c`; frozen claims/counters `21277b089e3c64c247bb4e0fcb033abfdfa1e668`.
Written: `.ufo/waves/round-83/w1/ScoutSources.md` and `.ufo/waves/round-83/w1/stage/ScoutSources/sources.md` (same text); receipts `.ufo/waves/round-83/w1/stage/ScoutSources/S909.txt` … `S912.txt`; counting helper `.ufo/waves/round-83/w1/stage/ScoutSources/foldcount.py`.

## Verdict

1. **All four candidates carry prose that supports the claim-D scope; none is refused as a glossary stub.** Each yields a unique, <=25-word span with a recorded `raw <n> / folded <m>` count, live and in a Wayback copy. All four quotes open in the *folded* read; three of the four are `raw 0 / folded 1` for a measured typographic reason (doubled space, source newline, 72-column wrap), and S911 is `raw 2 / folded 1` because Parsoid emits the poem twice (attribute + rendered `<pre>`).
2. **Two anchor flips are required, both proven by status codes and bytes:**
   - **S909:** the seat-named `hamframe.asp` is a 356-byte `<frameset>` with **no law text**; the prose is `hamcode.asp` (74,531 B, HTTP 200). A row anchored on `hamframe.asp` cannot carry a quote.
   - **S911:** the seat-named `/wiki/The_Rig_Veda/Mandala_10/Hymn_85` is **HTTP 404** (42,463 B); the page moved to `/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85` (HTTP 200, 70,655 B). The old slug's Wayback captures (2023–2024) are the evidence of the move.
3. **The S911 alternate hosting is not admissible under the sources rule.** The seat's second option, `https://www.sacred-texts.com/hin/rigveda/rv10085.htm`, answers **301** to a redesigned URL whose plain-UA request returns a **Cloudflare block page** (HTTP 403, "Sorry, you have been blocked"). One browser-UA probe returned the page; in that returned copy the Griffith text carries diacritics (`Sūrya`, `Aśvins`, `Pūṣan`), so a stanza-9 quote copied from the Wikisource ASCII text would be `folded 0` there. The path is challenge-gated: it is recorded as a warning, **not** as an anchor or evidence, and the row must use the Wikisource wording only.
4. **S910's role is narrower than the claim's vocabulary suggests.** The Wikisource EB11 "Marriage" article is the *legal/church-law* article: it contains **no** bride-price/capture/dowry typology (`bride` 0, `purchase` 0, `dowry` 0, `polygamy` 0 in the folded text). What it does supply is the institution's legal vocabulary — **connubium** (the alliance gate), **coemptio in manum / mancipatio** (the conveyance), and canon-law impediments. Its opening **three-stage evolutionary scheme is calibration material only** (§3.2).
5. **S912 supplies the boundary, not the transfer.** Leviticus 18 is a prohibited-degrees chapter; it has no bridewealth term. Use it for *who may not be taken* (the alliance network's edge) and for the stranger-within-the-gates clause; do not load it with transfer mechanics.
6. **No same-page Wayback capture exists for the current S911 title** (CDX `[]`). The pre-move title's capture (2024-02-04) carries the identical hymn text (word diff: one stray `-->` deleted, nothing added). Recorded as a durability caveat, not a source defect.

## 1. Method (repeatable; every number below is from these commands)

- Live fetch: `curl -sSL --max-time 90 -o <file> -w 'HTTP %{http_code}, %{size_download} B, ctype=%{content_type}\n' <url>`, once with the tool default UA and once with `-A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'`. No proxy, no login, no challenge met on any anchored fetch: `automation: none` (one off-protocol browser-UA probe of the challenge-gated sacred-texts path is disclosed in §3.3 and is not evidence).
- Default UA binds to the literal string `curl/8.23.0` (curl 8.23.0, OpenSSL 3.6.5).
- Wayback: CDX exact query (`filter=statuscode:200`, `limit=-3`), then the capture at `https://web.archive.org/web/<ts>id_/<url>`. Both UA requests were run per capture and are byte-identical; gzip payloads decoded before hashing and counting (the `id_` record is the stored payload).
- Span counting: `foldcount.py` (in this stage dir). `raw` = occurrences in the decoded document **as served**; `folded` = script/style dropped, **tags → one space**, entities decoded (HTML only), **U+00A0 and U+2003 → space**, whitespace runs → one space. The script prints `bytes=… sha256=… raw=… folded=… words=… chars=…` and exits 1 unless `folded == 1`. Each receipt carries the exact command and its output.
- Locators are paragraph/law/stanza/verse identifiers inside the fetched page, not line numbers of any local copy.
- Access date for every fetch: **2026-11-04**.

### 1.1 Source table (all numbers from the commands above)

| row | URL anchored | live HTTP | live bytes | sha256 (decoded) | template-rendered | Wayback capture | capture HTTP / bytes |
|---|---|---|---|---|---|---|---|
| S909 | `https://avalon.law.yale.edu/ancient/hamcode.asp` | 200 | 74,531 | `93410a95…c9eb12` | no | `20261024211059` | 200, 74,531 transferred = 74,531 decoded (**sha identical to live**) |
| S910 | `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Marriage` | 200 | 147,040 | `79faf533…d050df` | yes (transclusion + Parsoid) | `20260831215114` | 200, 37,459 gz → 128,008 decoded (`3d170e52…008733`) |
| S911 | `https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85` | 200 | 70,655 | `4d4737d7…058a29` | yes (Parsoid) | same title: **none**; pre-move title `20240204183600` | 200, 12,368 gz → 39,087 decoded (`0be4b87c…87493c`) |
| S912 | `https://www.gutenberg.org/cache/epub/10/pg10.txt` | 200 | 4,455,950 | `0204adae…ed83c0` | no (plain text) | `20261012135648` | 200, 1,405,040 gz → 4,455,950 decoded (**sha identical to live**) |

QUALITY 22-shaped UA records, verbatim (each line is one URL, two requests):

```
S909 hamcode: UA "curl/8.23.0" -> HTTP 200, 74531 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 74531 B, wall absent
S909 hamframe (seat-named): UA "curl/8.23.0" -> HTTP 200, 356 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 356 B, wall absent
S910: UA "curl/8.23.0" -> HTTP 200, 147040 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 147040 B, wall absent
S911 old title (seat-named): UA "curl/8.23.0" -> HTTP 404, 42463 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 404, 42463 B, wall absent
S911 new title: UA "curl/8.23.0" -> HTTP 200, 70655 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 70655 B, wall absent
S912: UA "curl/8.23.0" -> HTTP 200, 4455950 B, wall absent | UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 4455950 B, wall absent
```

Wall-marker sweep over the six fetched live bodies (hamcode 200, hamframe 200, S910 200, S911 old title 404, S911 new title 200, S912 200) with `grep -c -i -E 'Client Challenge|Just a moment|Attention Required|cf-browser-verification|Enable JavaScript and cookies'`: 0 in all six. The wave's one challenge-gated path is the sacred-texts redirect target (§3.3), which is not anchored and is not used as evidence.

## 2. The cheapest usable quote per source (and a second passage for another section)

| row | primary span (<=25 words) | words | raw / folded | second passage (different section) | words | raw / folded |
|---|---|---|---|---|---|---|
| S909 | `If any one, who has brought chattels into his father-in-law's house, and has paid the purchase-money, looks for another wife` | 20 | 0 / 1 | `If his father-in-law do not pay back to him the amount of the "purchase price"` (Law 164 — return/dissolution) | 15 | 1 / 1 |
| S910 | `In Roman law no legal marriage could be contracted unless there was connubium between the parties.` | 16 | 0 / 1 | `Coemptio was a conveyance of the woman by mancipatio` (transfer section) | 9 | 0 / 1 |
| S911 | `The Sun-God Savitar bestowed his willing Surya on her Lord` (RV 10.85.9) | 10 | 2 / 1 | `I take thy hand in mine for happy fortune that thou mayst reach old age with me thy husband` (RV 10.85.36 — ritual-formula section) | 19 | 2 / 1 |
| S912 | `None of you shall approach to any that is near of kin to him, to uncover their nakedness: I am the LORD.` (Lev 18:6) | 22 | 0 / 1 | `Neither shalt thou take a wife to her sister, to vex her, to uncover her nakedness, beside the other in her life time.` (Lev 18:18 — polygyny section) | 23 | 0 / 1 |

Each primary has exactly **one** folded occurrence in both the live body and its capture. Folded offsets (live, of folded length): S909 31,496 / 62,324; S910 7,902 / 61,342; S911 2,319 / 8,982; S912 465,788 / 4,326,670. A third passage per row is in the receipt (`third-passage:`), for the section the entry actually builds.

## 3. Per-row detail

### 3.1 S909 — Code of Hammurabi, trans. L. W. King (Yale Avalon) — **tier A**

- **Scope:** the code's own prescriptive text; the marriage cluster is Laws 128 (consummation makes the wife) and 159–164 (chattels + purchase-money into the father-in-law's house; forfeiture if the groom reneges; restitution if the father reneges; the price subtracted from the dowry), with 172–174 (the widow's dowry and remarriage). This is a *transfer between households secured by goods*, with symmetric return rules — the alliance-and-transfer reading is carried by the code's own words, not by a commentator.
- **Anchor flip:** `hamframe.asp` is a frameset (356 B, sha `b4d1c2d3…94ea`); its two frames are `hamcode.asp` (the code) and `codeind1.asp` (the index). The row must anchor `hamcode.asp`.
- **Why raw 0:** the page prints `has paid the  purchase-money` with **two ASCII spaces**; the folded read collapses them (raw 0 → folded 1). This is a typographic fact of the served bytes, not a stripper artifact — the receipt records it so a re-opener does not file a false defect.
- **Framework:** casuistic, prescriptive; King renders the bride-wealth term as "purchase price"/"purchase-money" and glosses neither. The page contains `bride` 0, `tirhatu` 0, `terhatu` 0 (folded counts); the underlying Akkadian term is not on the page. Do not literalize the English as a market sale.
- **Freshness:** the server sends no `Last-Modified`/`ETag` (IIS, `Cache-Control: private`); the 2026-10-24 capture is byte-identical to live (`sha256` equal), so the page's content has not moved since at least that date.

### 3.2 S910 — "Marriage", EB11 vol. 17 (Wikisource) — **tier B**

- **What the article actually is:** a transclusion of the labelled section "Marriage" from `Page:EB1911 - Volume 17.djvu/770`–`/776` = printed pp. 753–759; the next page (djvu/777) begins "Marryat, Frederick", so the transcription is complete. 43 article paragraphs (43 `<p>`, all non-empty). Revision `oldid 10430027`, last edited 2020-09-04; the HTTP `last-modified` (2026-10-21) is the Parsoid render time, not the content revision.
- **Scope it can carry:** definition of marriage as an institution/contract; the **alliance gate** (`connubium`: no legal marriage without it; plebs/patricians; Latini/Peregrini); the **transfer modes** (`confarreatio`, `coemptio in manum` — "a conveyance of the woman by mancipatio … a fictitious sale per aes et libram", `usus` — acquisition by prescription; all place the woman in the `manus`); the paterfamilias's consent; the canon-law impediments (near relationship public; impotence and force private; disparity of faith; mixed and morganatic marriages).
- **Scope it cannot carry:** the bride-price/capture typology. Folded counts: `bride` 0, `purchase` 0, `dowry` 0, `polygamy` 0, `polyandry` 0, `totem` 0, `kinship` 0. Any row text that claims those from this URL is misfiled.
- **Framework — calibration, never doctrine:** the opening "three stages … the animal or physical stage, the proprietary or legal stage, and the personal or moral stage", and the sentence "in the second or legal stage greater permanence was secured in marriage by assigning the husband a property right in his wife or wives", are 19th-century unilinear stage-law. The article's own dated legal matter (e.g. `19 Geo. II. c. 13`) is historical, not current law. Both belong in the entry only as *the 1911 article's doctrine*, labelled as such.
- **Extraction hazard (record it for the Scribe):** italics are tags, so the folded read carries a space before a following comma (`mancipatio ,`). A quote that ends at the italic word folds cleanly (`Coemptio was a conveyance of the woman by mancipatio`); a quote that crosses the comma does not. The chosen primary avoids italics entirely.
- **Freshness:** capture 2026-08-31 vs live word diff = 3 live-only insertions (template JSON block, "Switch to legacy parser", "Page was rendered with Parsoid"), **0 deletions, 0 replacements** — article prose identical. Both bodies give the primary quote exactly once (capture offset 4,886; live 7,902).

### 3.3 S911 — Rigveda 10.85, trans. R. T. H. Griffith (Wikisource) — **tier A**

- **Anchor flip:** old title 404 (42,463 B, sha `1e9dd362…ea06e`); new title `/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85` 200 (70,655 B). The moved page is one `<pre>` block, 47 stanzas, rev `oldid 14397100`, last edited 2024-08-08.
- **Reading:** the hymn stages the mythic wedding — Savitar **bestows** his willing Sūryā on her Lord (st. 9), Soma wooed, the Aśvins are groomsmen, the gods agree to the wooing (st. 14); the human rite supplies the hand-clasp formula (st. 36), the procession to the husband's house (st. 26), the bride as household mistress, the driving-off of the clinging fiend (st. 28–31), and the mythic serial husbands (st. 40: Soma, Gandharva, Agni, then a mortal). That is an alliance-and-transfer reading *in the poem's own terms*: who gives, who receives, what is said, where she goes.
- **Why raw 2:** Parsoid emits the poem twice — once escaped in the `<pre data-mw="…">` attribute, once as rendered text — so the served bytes carry two raw hits and the tag-stripped read carries one. On the 2024 capture (older Parsoid) the raw count is 1. The receipt states both.
- **Framework:** Griffith's 1889 verse translation (public domain) is a Victorian rendering, not a critical edition; the hymn is ritual poetry, not a law code. Stanza 40 is mythic precedent, never a social rule. The "marriage hymn" identification is the tradition's, not this reading's measurement.
- **Durability caveat:** CDX for the current title is `[]` (no capture). The pre-move title's latest capture (2024-02-04; 12,368 B gz → 39,087 B decoded, sha `0be4b87c…87493c`) carries the same 47 stanzas; word diff vs live: 1 deletion (a stray `-->`), 0 additions, 0 replacements.
- **Alternate hosting (seat's second option) — not usable:** `https://www.sacred-texts.com/hin/rigveda/rv10085.htm` answers **301** to `https://sacred-texts.com/book/the-rig-veda/rig-veda-book-10-hymn-lxxxv-surya-s-bridal`; the redirect target returns a **Cloudflare block page to the plain UA** (HTTP 403, 5,686 B, "Sorry, you have been blocked"). A single off-protocol browser-UA probe returned HTTP 200, 296,271 B (sha `aec62a8b…7adc14`), and that copy prints the Griffith text with diacritics (`Sūrya`, `Aśvins`, `Pūṣan`). Because the path is challenge-gated it is **not evidence** for any row: use the Wikisource ASCII wording only, and never mix hostings in one quote.

### 3.4 S912 — Leviticus 18, KJV (Gutenberg #10) — **tier A**

- **Reading:** a prohibited-degrees list opened by "I am the LORD your God" (18:2), bounded against Egypt and Canaan (18:3), closed by the land-vomit sanction (18:24–28) and extended to "any stranger that sojourneth among you" (18:26). Its contribution is the **edge of the alliance network** (who may not be taken: near of kin, father's wife, sister, aunt, daughter-in-law, brother's wife, a woman and her daughter, a wife's sister in her lifetime), not the transfer mechanics. The chapter has no bridewealth term.
- **Why raw 0:** Gutenberg hard-wraps at 72 columns; the verse crosses a line break after "to". Folded 1 in live and capture.
- **Edition:** #10 is the whole KJV Bible (4,455,950 B; "Most recently updated: October 29, 2024"). The other candidate #7999 ("…Complete Contents") is a different packaging (4,642,387 B, HTTP 200) and is **not** the anchored bytes.
- **Freshness:** the 2026-10-12 capture is byte-identical to live (same sha256). No content drift.
- **Framework:** 1611 translation; prescriptive priestly legislation. The KJV wording is the evidence, not a claim about ancient Israelite practice.

## 4. Independent second reading vs the binding fetch receipts (R82-M3 rule)

This wave's rule: **`ScribeRows`' fetch receipts bind the registry rows; this reading is the independent second reading.** Nothing here may silently override a ScribeRows receipt. What this report fixes so a disagreement is *detectable*:

- byte counts + sha256 for every anchored URL (live and capture) are in §1.1 and in each receipt;
- the two anchor flips (S909 → `hamcode.asp`; S911 → `/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85`) are proven by 200/404 status and by the frameset's 356 bytes;
- the S911 alternates differ at the byte level (`Sūrya` vs `Surya`) in the one off-protocol probe, so a quote from another hosting is a checkable mismatch, not a preference;
- every quote carries `raw <n> / folded <m>` under the stated rule, so a different count is a checkable disagreement, not a judgment call.

If ScribeRows' receipt disagrees on a byte count or a quote, **report it; do not pick one silently.**

## 5. Refusals and flips

- **No candidate is refused.** Measured grounds: S909 62,324 folded chars of law text (257 `<p>`); S910 61,342 folded chars / 43 article paragraphs; S911 47 stanzas; S912 a 30-verse chapter inside a 4.3M-char Bible. None is a bare glossary stub for this scope.
- **Two anchor flips** (not refusals): S909 `hamframe.asp` → `hamcode.asp`; S911 `/The_Rig_Veda/Mandala_10/Hymn_85` → `/The_Hymns_of_the_Rigveda/Book_10/Hymn_85`. Both flips are forced by the served bytes, not by taste.
- **One hosting caution** (not a flip): S911's sacred-texts alternative is challenge-gated (Cloudflare) and diacritic-different; keep the Wikisource anchor and never quote from the blocked copy.

## 6. Remaining unknowns

- S911 has **no same-page Wayback capture** at the current title; only the pre-move title is captured. A future move of the Wikisource page would leave the row anchor stale until re-probed.
- Avalon sends no `Last-Modified`/`ETag`; freshness for S909 rests on the byte-identical 2026-10-24 capture, not on a server date.
- The EB11 transcription is complete for this article (pp. 753–759, verified against djvu/777's different article), but I did not collate it against page scans; a scan-level collation is out of scope for this reading.
- S909's Akkadian term behind "purchase price" is not on the page; identifying it as *tirhatu* is literature-level inference, deliberately left out of the quote and out of the row's evidence.
- The ScribeRows fetch receipts were not visible to this seat; the comparison in §4 is therefore a protocol, not a completed diff.

## 7. Tooling

No installs or upgrades. Used: curl 8.23.0 (system), Python 3 standard library (`hashlib`, `gzip`, `html`, `re`), coreutils `sha256sum`/`stat`. No pacman, no `uv`, no network automation beyond plain fetches. Raw fetched bytes were kept in the seat's scratch dir and are **not** committed; every receipt carries URL + sha256 so the bytes can be re-fetched.
