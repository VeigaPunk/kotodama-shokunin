# RevSourceSupport1 — blind per-row source support, S805–S810 (claim C)

Seat: `L1-kotodama-r67.RevSourceSupport1` · round 67 v2 · lane `kotodama-shokunin`
Base: `ad5b52b0ab5691358cd38718ab75649dc9916f9a` · review window 2026-10-24 09:39–09:47 (host clock, -0300)

**What I attacked.** Not the counters: the six row fragments and their live evidence. For each id I
re-fetched the live URL myself (curl, browser UA and, for S809, a full Chrome header set), re-fetched
the `web.archive.org/...id_/` capture with `--compressed`, extracted body text with BeautifulSoup
(`lxml`), and matched the anchor quote as a literal substring under whitespace folding. I then judged
the **teaches cell clause by clause against the page body**, not against the anchor — a row can be
quotable and still teach something the page never says.

**Pinned revisions.** Fragments were still being rewritten while I reviewed (S805 changed between the
09:40 dispatch snapshot and 09:40:16). Findings below apply to these exact bytes; the L1 must
integrate from the same hashes, not from any earlier copy:

| fragment | mtime | bytes | sha256 |
|---|---|---|---|
| rows/ScoutRow01/row-S805.txt | 09:40:16 | 1333 | `c30fd3eda4a61cd4ad78cc9e898b5d1d5a23543276ebdef9bb04b9977b8940bc` |
| rows/ScoutRow01/row-S806.txt | 09:40:39 | 1541 | `8d8b7fbcbacb157299a6a3096997a2ff7d5737f89d78a6263218f676e1dd2c34` |
| rows/ScoutRow03/row-S809.txt | 09:41:19 | 1748 | `374a8bf178efb10a005f6b10282a80a800ba08685c1db17d1f6316d0cd87ee28` |
| rows/ScoutRow03/row-S810.txt | 09:41:42 | 1659 | `71719cdde915624feccd66c25a9e2a6d000eaaff882b5c75985876f7408f51a8` |
| rows/ScoutRow02/row-S807.txt | — | — | **absent at close** |
| rows/ScoutRow02/row-S808.txt | — | — | **absent at close** |

## 0. Per-id verdicts

| id | verdict | one-line basis |
|---|---|---|
| S805 | **PASS** (teaches supported; minor wording note F6) | live 200 = capture 200, quote verbatim in both; all teaches clauses on the page |
| S806 | **PASS on teaches / FAIL anchor-verbatim** (F2) | teaches fully supported; the anchor string is *not* a literal substring of live or capture (curly-quote omission) |
| S807 | **UNVERIFIABLE — fragment absent** (F1) | seat wrote nothing; no row to review |
| S808 | **UNVERIFIABLE — fragment absent** (F1) | seat wrote nothing; no row to review |
| S809 | **PASS on teaches with one attribution defect (F4); access claim not reproducible (F3)** | capture carries the quote verbatim; live 403s to every scripted client I could build |
| S810 | **PASS (clean)** | live 200 + capture 200, quote verbatim in both; every teaches clause, including 4,500 m²/60 rooms/300, is on the page |

## Findings

### F1 — HIGH (blocking for S807, S808): fragments never landed
`rows/ScoutRow02/` does not exist at 09:42; `agent://L1-kotodama-r67.ScoutRow02` reports "Britannica
live is challenged … checking captures of the Canon topic page" with no published output. There is no
S807/S808 row to judge, so the wave's blind-support evidence covers **4 of the 6 assigned ids only**.
This is a dependency finding, not a source defect: nothing about Ibn Sina / Huangdi Neijing sources has
been established by this seat. If the fragments land after this report, they need a pass from a seat
that can still run the same procedure; the L1 must not read this file as "S807/S808 reviewed".

### F2 — MEDIUM (S806): anchor quote is not verbatim; the row's own VERIFY contradicts itself
Page body (live 200, 142,562 B; `id_` capture 20260614165133, 142,342 B, both fetched here):

```
… are collectively called as “ Tridoshas ” and they control the basic physiological fu…
```

Row anchor: `"Vata dosha , Pitta dosha and Kapha dosha are collectively called as Tridoshas"` —
the closing (and the shape of the opening) quotation marks are dropped. Literal substring match on
live text: **False**. On capture text: **False**. Even punctuation-normalised (space-before-punctuation
folded) it stays **False**, because the curly quotes survive normalisation. `VERIFY` says
"quote verbatim in body text Y (page renders … as “ Tridoshas ”)" and `CAPTURE` says the capture
"contains … the anchor verbatim" — both assertions are refuted by the bytes.
**Flip:** keep the marks (`… called as “ Tridoshas ”`) or cut the anchor at `… are collectively
called as`, then re-grep the capture. The substantive claim is unaffected; the re-openable string is.

### F3 — MEDIUM (S809): the live URL is not reachable as the row claims; capture-only
Row: live `https://circulatingnow.nlm.nih.gov/2023/01/05/medicine-and-miracle-in-a-medieval-monastery/`,
`VERIFY` "HTTP 200, 216,990 bytes with full browser UA headers", `ACCESS` "browser UA + Accept-Language
gets 200". Measured here, three ways, same minute:

| request | result |
|---|---|
| plain curl | 403, 535 B |
| Chrome UA | 403, 535 B |
| Chrome UA + `Accept` + `Accept-Language` + `sec-ch-ua*` + `Sec-Fetch-*` + `Upgrade-Insecure-Requests` | 403, 548 B |

The `id_` capture `20260801154508` **does** serve 200 (218,000 B) and **does** carry the anchor
verbatim (`infirmary could range from a single room just for the monks to a complex of medical
buildings including a hospital, pharmacy, baths`). So `CAPTURE` passes and claim C's CAPTURE leg is
safe, but the row's operative access advice is wrong for a re-opener and the `200 / 216,990 B` stamp is
unverifiable now. **Flip:** record "live 403 to scripted clients on 2026-10-24; read the capture",
the same shape S809's own `rejects.txt` already uses for English Heritage (403 class). This is the
honesty class the round is meant to fix: a `VERIFY` line should not assert a status the lane cannot
reproduce — either re-measure at integration time or cite the capture only.

### F4 — MEDIUM (S809): teaches fuses two separate page claims into one attribution
Teaches: "*the Bury St Edmunds medical manuscript shows a monastery's infirmary scaled by wealth* —
single room for monks or a complex with hospital and pharmacy; its 185 folios carry diagnosis and
herbal remedies." The page has **two distinct** statements:

- general: "Depending on the size and wealth of the monastery, this infirmary could range from a single
  room just for the monks to a complex of medical buildings including a hospital, pharmacy, baths,
  bloodletting services, and a separate chapel" — about monasteries generally, not about E8;
- manuscript-specific: "The bulk of the manuscript, its first 185 folios, is dedicated to medical
  diagnosis and herbal remedies."

The second clause of the teaches cell checks out verbatim; the first attributes the scale claim to the
manuscript, which the page never does. **Flip:** "NLM's survey of monastic infirmaries: scale follows a
house's wealth — single room for the monks or a complex with hospital, pharmacy and baths; the Bury St
Edmunds manuscript (E8), first 185 folios, carries diagnosis and herbal remedies." Style/boundary
seats should also note bloodletting and the chapel are in the page's list but not in the teaches cell —
no harm, just not exhaustive.

### F5 — LOW (S806): the bullet adds a claim the page does not make
`BULLET=The trinity Ayurveda calls Tridoshas - Vata dosha, Pitta dosha, Kapha dosha - collectively
governs somatic temperament.` The page has **zero** occurrences of "temperament"/"personality"; its
statement is "they control the basic physiological functions of the body". The teaches cell itself is
fully supported; the bullet (the paraphrase the entry will carry) is not. **Flip:** "… collectively
control the body's basic physiological functions." (Also note the bullet is the one RESTATE reads;
this is a support defect, not a counter-metric one.)

### F6 — LOW (S805): "canon" is editorial; the earlier revision's treatise clause was unsupported
Current teaches: "… health their balance, disease their imbalance - the humoral canon." Page: "The most
historically prominent theoretical scheme of the Coan writers was the doctrine of the four humors of
the body: blood, phlegm, black bile, and yellow bile (or sometimes serum). Health was defined as the
balance of the four humors. Disease was defined as the imbalance of the humors." Every substantive
clause is supported; "canon" is the cell's own characterisation, acceptable as curation. Worth
recording because the **09:40 snapshot** of this same file ended "… the humoral canon codified in
treatises like *On the Nature of Man*", and I confirmed the IEP page contains **0** occurrences of
"Nature of Man" (its only "Nature" hit is "the nature of disease"). The current revision silently drops
that clause — the build seat caught its own over-reach, or the file was rewritten mid-flight. Either
way: integrate the pinned hash, do not resurrect the 09:40 wording in the lesson Gate.

### F7 — LOW (S806 tier): tier A on a narrative review is precedent-compatible, not definitional
`kind=paper, tier=A` for Jaiswal & Williams' *J Tradit Complement Med* review. Tier A's definition names
"original paper"; this is a review. The lane already admits this shape (S800 = BMCR book review, tier A),
so it is consistent curation, but if the calibration claim wants tier discipline, B is the defensible
grade for a narrative review. Not a blocker for claim C; flagged for the tier-inflation seat.

### S810 — no defect found
Live 200 (64,635 B) and capture 20260316002018 (55,278 B) both contain the anchor verbatim; same-page
normalisation equal (no query). Teaches clauses each verified on the page: "approx. 4,500 m2",
"discovered in 1936", "The 60 sick rooms enabled the provision of medical care for up to 300
legionaries", "military doctors and medical orderlies treated battle injuries, everyday illnesses and
work accidents", "archaeologically investigated but has since been entirely covered with modern
buildings", "authentically reconstructed and fully equipped field infirmary". Two wording nits only:
teaches says "300 patients" where the page says "legionaries", and the page’s "site built over" wording
is rendered as "site built over, field infirmary reproduced" (faithful). Tier A for a museum page
describing its own excavation is defensible ("primary or authoritative for that scope").

## Shape facts I checked (so other seats do not have to)

All four landed rows: 11 cells; `kind` in enum (docs, paper); tier B/A; status `mined`;
opened `2026-10-24`; recheck `180d`; used-by exactly
`corpus/knowledge/culture-material/medicine-healing-codes.md`; scope lengths 51/49/60/57 (≤60);
anchor quotes 16/13/22/18 words. URLs: none of the four appears in `corpus/SOURCES.md` (grep 0) and
none collides with a sibling fragment. Hosts: `iep.utm.edu` and `museumaargau.ch` and
`circulatingnow.nlm.nih.gov` are new to the registry; `pmc.ncbi.nlm.nih.gov` is already heavily used
(32 base rows), so these six add rather than concentrate host coverage.

## Residual risk and verification gaps

1. **S807/S808 have no evidence at all** (F1). That is the single largest gap in this seat's scope.
2. **Live pages move.** S805/IEP and S810/Aargau matched exactly at 09:41–09:42; S809 already does not.
   Any row's `VERIFY` status is a timestamp, not an invariant — the counters cannot see this, which is
   exactly why this seat exists.
3. **Capture reading needs `--compressed`.** `id_` serves the original encoding; without it the S805
   capture reads as 15,890 B of compressed bytes and the quote "disappears". A capture-checking seat
   that omits `--compressed` will file false "capture does not contain quote" failures — I hit this and
   re-probed before reporting. Anyone auditing `CAPTURE` should re-probe with `--compressed` and a
   second scheme before alleging a dead or mismatched capture.
4. **No real-browser rendering check** was possible in-seat (no headless browser installed, and the
   pacman guard forecloses installing one). Text extraction is post-render DOM, so JS-only text would
   be missed; none of these four pages needed JS to surface the quote, but S809 could not be tested
   live at all.
5. I did not judge RESTATE counter arithmetic, bullet uniqueness across the 24 rows, duplicate-host
   thresholds, or tier grading for rows outside my six — those belong to the counter, entry-spec, and
   calibration seats.

## Tooling

No installs or upgrades. Used `curl` (preinstalled), `python3` + `bs4`/`lxml` (preinstalled), and the
lane's own `reports/round-67/accept-c.py` imported read-only for its tokenizer when reporting shape
numbers. No pacman, no network write, no repo/jj mutation; all writes are this file.

Report: .ufo/waves/round-67/w1/RevSourceSupport1.md
