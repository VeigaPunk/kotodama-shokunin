# CriticC95 — findings on claim C (funerary lament/dirge entry + S970–S974)

Scope: attack the staged entry (`stage/ScribeEntry95/funerary-lament-dirge-formulae.md`, 50148 bytes, 282 lines) and the proposed rows (`stage/ExecRegistry95/SOURCES.append.md`, S970–S974). Disclosure only, not a verdict. Captures read: `stage/ExecRegistry95/evidence/S970.txt` … `S974.txt`. Base registry: `corpus/SOURCES.md` (highest S969, read-only). Scripts: `stage/CriticC95/receipts/` (verify.py, ctx.py, ctx2.py, gates.py).

Findings: 7 (3 medium, 4 low). Top severity: medium.

## F1 — medium — novelty: two entry paragraphs restate the lullaby entry
- Evidence: `ScribeEntry95/funerary-lament-dirge-formulae.md:250` (§11 opener) is verbatim `corpus/knowledge/linguistics/lullaby-child-song-formulae.md:266` ("NON-CANON. The people, the language, the songs and the names below are invented for this worked example only. Nothing here describes a real community, and canon belongs to lore-shokunin"). 8-gram shingle share 1.00 (`gates.py` §4).
- Evidence: `…funerary-lament-dirge-formulae.md:31` (§1 closing paragraph, "The base is deliberately small and heterogeneous — five cases from five language traditions, none of them a survey…") against `lullaby…md:26` ("The base is deliberately small and heterogeneous, and it is read as small and heterogeneous: five cases from five language traditions, none of them a survey…"). Shingle share 0.57.
- Structural echoes (below 0.25, disclosed, not counted): new `:27`, `:197`, `:199`.
- Not restated: `orality-formulaic-language.md`, `funerary-material-culture.md`, `death-afterlife-eschatology.md`, `sacred-registers-liturgical-language.md` — no new paragraph reaches 0.10 shingle share against any of them (`gates.py` §4, flagged count 0 for those four). Lament is a type-scene card at `orality-formulaic-language.md:66`, cited, not restated.
- Count of restating paragraphs: 2 (meets the >= 2 pattern threshold of the r92 ideophones-overlap lesson).
- Recipe: rewrite `:31` as an own-voice sentence that cites `linguistics/lullaby-child-song-formulae.md` for the sibling sample design; replace the `:250` opener with a lament-specific NON-CANON sentence (e.g. "NON-CANON. The Vessemi, their names and their songs are invented for this worked example only."). Re-run `gates.py` §4: target no paragraph >= 0.50 against the lullaby entry.

## F2 — medium — sourcing: S971 misattributed (Seremetakis on Maniat laments, presented as Corsican)
- Evidence: entry `:90` — "The Corsican material shows the antiphonal form carrying an argument… The claim is that a family's laments can function as truth-claims supported by the 'inherently jural and historicizing structure' of antiphony… (S971)".
- Capture: `ExecRegistry95/evidence/S971.txt` footnote 11: "Seremetakis argues that Maniat laments can function as truth-claims supported by the 'inherently jural and historicizing structure' of antiphony (1990:508)." The quoted span is grounded (count 1), but the claim is Seremetakis's on Maniat (Greek) laments, reported in a footnote. The Corsican sentence in the capture is the author's own "suggests", which the entry does paraphrase correctly. "a family's laments" is not in the capture.
- Related, unflagged second-hand: entry `:157` "in the Greek context specifically it has been shown that lament can serve as a privileged arena…" (S971) — capture text is "it has been demonstrated… (Auerbach 1987; Seremetakis 1990, 1991; Caraveli 1986; …)". Grounded, but the entry does not say it is a report of other authors.
- Recipe: at `:90` name Seremetakis (1990:508) and Maniat, state it is S971's footnote-11 report, and drop "a family's". At `:157` add "(reporting Auerbach 1987 and Seremetakis 1990, 1991, via S971)".

## F3 — medium — unsourced cross-tradition claim, contradicting §12
- Evidence: entry `:133` (§6 opener): "the inventory has four named compartments that recur across traditions. … (design, not sourced)".
- Contrast: entry `:277` (§12): "The four-compartment inventory of §6 … are the entry's own analytical apparatus applied to the reports; they are not a claim that every tradition organises its grief content under those four headings."
- Problem: "recur across traditions" is an empirical cross-tradition claim with no S-id and no located quote; the design marker does not cover it, and §12 disowns it.
- Recipe: at `:133` replace "that recur across traditions" with "that this entry uses to sort the reports (design, not sourced)".

## F4 — low — sourcing: "vocative" grammar gloss attributed to S974
- Evidence: entry `:112`: "Each phrase of her agonized litany ends with a refrain exclamation — the dead man's name in the vocative — … (S974)"; and "the refrain is a *name* in the vocative" (same paragraph).
- Capture: `S974.txt` has "refrain exclamation 'way Pridon!' (woy Pridon!)" and the name Pridon. Term "vocative" count = 0 in S974.txt (`ctx.py`/`gates.py`). The name Pridon, the village doctor and the "other women mourners" are all grounded.
- Recipe: replace "in the vocative" with "(the name Pridon inside 'woy Pridon!')" or append "(grammatical gloss, design, not sourced)".

## F5 — low — unsourced claim: "classical division"
- Evidence: entry `:60`: "The classical division has three positions…". No S-id; the design marker is present but "classical" asserts a scholarly consensus with no citation.
- Recipe: replace with "A three-way division (design, not sourced)".

## F6 — low — prose defect: spliced quote, grounded span
- Evidence: entry `:68`: "…is described as representing and maintaining community Catholicism in a context of scarce priests, and it is "was important in the role of the female professional mourner who performed ritualized laments" (S973)."
- The quote is grounded (`S973.txt`, count 1; "scarcity of priests" and "both representing and maintaining community Catholicism" are also present). The sentence is ungrammatical ("it is 'was important…'").
- Recipe: "…, and her role "was important in the role of the female professional mourner who performed ritualized laments" (S973)." Keep the quote byte-identical.

## F7 — low — attribution omitted: Ó Madagáin reported inside S973
- Evidence: entry `:114`: "The communal wail is characterised as a largely non-lexical element by professional mourners… 'No words were used, only vocables such as…' (S973)".
- Capture: `S973.txt` "Breandán Ó Madagáin describes the gol or communal wail … as a largely non-lexical element…". The description and quote are Ó Madagáin's, reported through S973. The entry drops the primary author. (Do not conflate with S966, Ó Madagáin 1985 "Gaelic Lullaby", a different article.)
- Recipe: at `:114` write "as reported by Breandán Ó Madagáin via S973".

## Checks run (all measured in this seat; commands in `receipts/`)
- Quotes (`verify.py`, rc 0): 14 double-quoted spans of >= 12 chars in the entry; 14/14 occur in the cited capture, each count 1, all <= 14 words. 0 misses.
- Registry anchor quotes (`ctx2.py` tail / inline): 5/5 occur exactly once in their capture; 4–10 words each (<= 25).
- Frozen topic line (`- topic: `): one line, byte-equal to the frozen topic in `reports/round-95/predispatch.py`.
- Phrase anchors: all six frozen phrases appear in h2 headings (§3 professional keeners, §4 antiphonal lament, §5 lament refrain, §6 praise of the dead, §7 gendered mourning rules, §9 fictional mourning register). None is only in a table cell.
- Headings: 12 h2, all substantive; no tiny or padding headings.
- Table (§9, `gates.py` §2): 11 data rows x 5 columns; 0 empty cells. Disclosure: the 5th column ("status") reads "design, not sourced" in all 11 rows; the other 4 columns vary (min 14, max 304 chars). Floor (>= 5x3) met by the varied columns.
- Byte padding (`gates.py` §3): "design, not sourced" = 144 occurrences = 2736 bytes = 5.5% of 50148. Longest repeated sentence > 80 chars: 0 repeats. Not padding.
- Unmarked body sentences (`gates.py` §1): 8 framing lines (`:37, :66, :68, :86, :88, :90, :112, :114`); each has its S-id in the same paragraph, so none is an unsourced fact. Unmarked real-world-looking assertions are F3 and F5.
- Novelty against base: `grep -rni` for lament/dirge/keen/mourning in corpus/knowledge (run this seat): lament/dirge/keen hits exist only in orality (`:66` type-scene card, cited), funerary-material-culture (`:139` dirge etymology, not restated), and non-linguistics files. `lullaby-child-song-formulae.md` has 0 "lament" hits. The surface is unowned at base; the only restatement is F1.
- Registry URL duplicates vs base (`grep -F`, rc 1 = no match for each): `sciendo.com/pdf/10.2478`, `journals.library.columbia.edu` + `currentmusicology` + `5043/2312`, `mdpi-res.com/…religions-10-00235`, `…religions-15-00879`, `dergipark…/1673889`, `jef-2025-0006`: 0 base matches. No W04-style duplicate.
- Tier: all five A. All are peer-reviewed journal or MDPI article bodies; no community source at A. Not inflated.
- used-by: all five rows = `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`. That path does not exist at base yet (expected pre-landing).
- Census (`ExecRegistry95/census.txt`): rows S970–S974 findings 0; E-codes 0; W-codes are pre-existing base rows.

## Not measured
- Capture sha256 values for the five rows were not recomputed by this seat (the rows carry no sha256 column in the staged file).
- Row evidence paths `reports/round-95/evidence/S97x.txt` are not present in the lane until the L1 lands them; the staged copies in `ExecRegistry95/evidence/` were verified in place.
- Lesson Gate lines (`corpus/lessons/round-95.md`) were not in the stage and were not checked.
