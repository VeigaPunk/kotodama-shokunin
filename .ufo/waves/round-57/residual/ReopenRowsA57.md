# ReopenRowsA57 — residual falsify: S413–S426 re-opened by ordinary means

Scope: rows S413–S426 of `corpus/SOURCES.md` at 78d83b5e (claim C landing = HEAD;
worktree diff is only appended rows S481–S491, so rows read match the landed bytes).
Method: plain `curl -sL` GETs (desktop UA) of every URL in each row's source cell,
then verbatim match of every `"…"` span in each row's anchor cell against the served
bytes — strict (whitespace-collapse + glyph normalisation) and loose (alnum-only).
All 56 anchor quotes checked (LOCATE requires only the first per row; I checked all).
Then every entry sentence citing these ids was carried-checked against the served text.

## Findings

### MINOR — S413 cadency quote is not verbatim as served (punctuation changed)
`corpus/SOURCES.md:442` anchor cell prints (as "served text"):
`"For the second son a crescent, for the third son a mullet, for the fourth son a martlet, for the fifth son an annulet"`.
All four listed files print semicolons, not commas (verified in completeguidetoh00foxduoft_djvu.txt 1,875,872 B, completeguidetoh00foxdrich djvu.txt ×2, cu31924029796608_djvu.txt — identical span in each):
`For the second son a crescent ; for the third son a mullet ; for the fourth son a martlet ; for the fifth son an annulet`.
Fix (SOURCES.md:442, keep the "served text" label honest):
- old: `"For the second son a crescent, for the third son a mullet, for the fourth son a martlet, for the fifth son an annulet"`
- new: `"For the second son a crescent ; for the third son a mullet ; for the fourth son a martlet ; for the fifth son an annulet"`

### MINOR — S417 scope term "arms-of-domination" vs served "Arms of Dominion"
`corpus/SOURCES.md:447` scope cell: "arms-of-domination/community/office/pretension categories".
Served Boutell text: `Arvis of Dominion, Borne by Sovereign Princes` (OCR of "Arms of Dominion"); index "of Community, 102: of Dominion, 102". The classification is real; the row's spelling "domination" is not the book's term.
Fix (SOURCES.md:447): old `arms-of-domination/community/office/pretension categories` → new `arms-of-Dominion/community/office/pretension categories`.

### NIT — S413 line anchors are file-ambiguous (correct on the 4th URL, wrong on the 1st)
`djvu.txt:9122-9123` and `djvu.txt:9295-9298` are correct **only** on the fourth-listed
URL (`cu31924029796608_djvu.txt`, 1,868,841 B): L9122-9123 is verbatim `Lion rampant. — The animal is here depicted in profile, and erect, resting upon its sinister hind-paw`; L9295-9296 is the walking-lion quote. On the first-listed URL (1,875,872 B) those lines hold a motto and the sejant-regardant definition; the quotes sit at ~L8912 / ~L9089. The row names no file for the line refs.
Fix (SOURCES.md:442): old `ch. XI, djvu.txt:9122-9123:` / `ch. XI, djvu.txt:9295-9298:` → new `ch. XI, cu31924029796608_djvu.txt:9122-9123:` / `ch. XI, cu31924029796608_djvu.txt:9295-9298:` (or the exact lines of the u0 file).

### INFO (not defects) — quote-flatten conventions hold elsewhere
- Dehyphenation of line-wrap hyphens is applied in row quotes: S413 `in- fraction`→`infraction`, `inherit- ance`→`inheritance`; S417 `care- fully`→`carefully`, `em- inence`→`eminence`. All words verbatim otherwise; consistent with lane practice of quoting de-wrapped text.
- Punctuation trims at quote edges (no mid-quote change): S420 LYON-COATS-3 served `…Bearings in Scotland, they are protected under the law of Scotland.` (row drops the comma, ends early); S420 LYON-COATS-4 served `a formal "Petition"` (row drops inner quotes); S421 LYON-BLAZ-3/4 served `"undifferenced"`, `…a person.` (row drops quote marks, final period, a comma, and lowercases `Every one`→`everyone` — hmm, served `However, everyone of the same surname` … row quote starts `However everyone of the same surname` dropping the comma; verbatim modulo punctuation).
- S414's `/stream/` URL served `Content-Type: text/html` today (1,355,402 B) while the body is the plain djvu text; all four quotes strict-verbatim.
- S419's Wayback URL answered 429 on first GET (rate-limit after an archive.org burst), 200 on a spaced refetch; all four quotes strict-verbatim on the capture. Row's "challenge met, not passed" refers to the live host, honestly stated.

## Tier check (rubric: A = primary/authoritative for scope; `community` never A)
S413–S416 `book|A`: Fox-Davies, Woodward(-Burnett), Parker are the standard English reference works; "authoritative for that scope" fits the rubric, same basis as S428 (1876 paper, A). S417 `book|B`: Boutell is the popular survey; demoted tier is consistent curation, not an over-read. S418–S426 `docs|A`: College of Arms, Lord Lyon, 1672 Act (legislation.gov.uk plain text), gg.ca, e-codices and KBR holding-institution records — each is the authority/primary record for its scope cell. No tier objected.

## Per-row verdicts
- **S413** — 8/10 quotes strict-verbatim; the two "misses" are hyphen-splits in the served file (`in- fraction`, `inherit- ance`), words verbatim. One real defect: commas-for-semicolons cadency quote (fix above). Line anchors valid only on the 4th URL (nit). Tier A OK. Entry uses verified: tincture list (ermine/vair/pean, "colour of nature, i.e. 'proper'", "well-known coats which break the rule" → §5 C hedge kept), "Neither officially nor unofficially is any attempt made to enforce their use in England" → §6 "no attempt enforces it" verbatim-supported, "when the marriage is dissolved the impalement becomes meaningless, and should be discontinued" → "impalement ends with the marriage" supported, lion/leopard "has long since become obsolete in British armory" supported. **Agree, one quote fix.**
- **S414** — 4/4 strict-verbatim. "heiress in British and Scottish Heraldry now only means heiress of blood, and has no reference at all to possessions" → §6 claims verbatim. Tier A OK. **Agree.**
- **S415** — 4/4 strict-verbatim. Tudor systematisation + "not even the semblance of provision" verbatim → §6/§10 supported. Tier A OK. **Agree.**
- **S416** — 4/4 strict-verbatim, including served OCR artifacts (`\a`, `peculiaiities`) which the row honestly flags. Blazon order (FIELD→ORDINARY→charges) supported. Tier A OK. **Agree.**
- **S417** — 4/4 quotes present; two reach strict only after dehyphenation (served `care- fully`, `em- inence`). Tier B OK (see rubric note). Scope term nit "domination"→"Dominion". Entry crest claims verbatim. **Agree, one term fix.**
- **S418** — 4/4 strict-verbatim on Wayback capture. "concise verbal description … known as the blazon. The same arms may be rendered perfectly correctly in numerous artistic styles" → §5 "the verbal blazon, not the painting, governs" verbatim-supported. Tier A OK. **Agree.**
- **S419** — 4/4 strict-verbatim on capture (after 429 refetch). "transmit their arms as a quartering to their descendants", "little used in modern heraldry", surname statement, helm-top crest — all verbatim → §3/§5/§6 supported. Tier A OK. **Agree.**
- **S420** — 4/4 present; two match only after punctuation trims listed above (words verbatim). "court of law", "must petition", "protected under the law", "matriculate off a previous Grant" verbatim → §3/§4/§6/§11 supported. Tier A OK. **Agree.**
- **S421** — 4/4 present modulo punctuation trims (words verbatim). "Or = gold Argent = silver … Vert = green … given capital letters" → §5 Scottish-names claim supported; `"regardant" = facing backward, "dormant" = sleeping` → §5 supported; "all Arms are individual to a person" → §3 supported. Tier A OK. **Agree.**
- **S422** — 4/4 strict-verbatim on the capture. Escheat verbatim: "escheat to his Maiestie all the moveable Goods and Geir vpon which the saids Armes are engraven" → §4 supported. Tier A OK. **Agree.**
- **S423** — 2/2 strict-verbatim on live page. §4 merit/honour claims verbatim. Tier A OK. **Agree.**
- **S424** — 2/2 strict-verbatim; additionally §9's `"Purpure an Inukshuk of six stones Or"` and the Inuvialuktun motto verified verbatim on the page. Tier A OK. **Agree.**
- **S425** — 4/4 strict-verbatim; "missing fourth part … known from a late 18th century copy of the roll" verified → §9 supported. Tier A OK. **Agree.**
- **S426** — 4/4 strict-verbatim; convolute sections, dates and "[Drawing of the herald Gelre, Claes Heynen]" verbatim → §9 supported. Tier A OK. **Agree.**

## Verdict
**Agree with what landed**, with two fixes inside the checked rows:
1. S413 cadency anchor: commas → served semicolons (SOURCES.md:442).
2. S417 scope term: `arms-of-domination` → `arms-of-Dominion` (SOURCES.md:447).
Recommended (optional): name `cu31924029796608` in the S413 line anchors (SOURCES.md:442).

Residual risk: for multi-URL rows the anchor-cell quotes were found on at least one listed URL; the locator's per-URL attribution is not re-derived here, and only the served text was checked — image/PDF surfaces (e.g. S418/S419 live pages behind the met challenge) were not bypassed. No entry sentence was found to over-read its cited row; hedges (§5 C, §11 codes) are kept.

Tools installed: none (existing curl/python3 only). Processes ≤3, page cache <8 MB under /tmp/r57a57.
