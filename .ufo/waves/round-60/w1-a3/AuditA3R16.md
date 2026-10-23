# AuditA3R16 — pre-freeze wording audit, ids S650 + S651 (round 60 attempt 3, wave 1)

Date: 2026-10-23 UTC. Object: /fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md (inherited candidate build, uncommitted) + working-tree SOURCES rows S650/S651 (SOURCES.md:605-606).
Method: ordinary means only — `curl -sL` plain GET with the row's first URL written literally in the command; quote location judged with the lane locator `reports/round-60/reopen-quote.py` (`to_text`, `locate_in`, `normalise`), copied read-only into my sandbox (/fast/scratch/hyaku/kotodama-r60a3/AuditA3R16/). Lane untouched (no write, no git/jj command). No installs.
Byte identity: my live fetches are sha256-identical to the L1 pinned captures (L1/captures/S650.bin, S651.bin, manifest.json) — so every sentence below is carried by the pinned capture bytes too.

- S650 live: HTTP 200, 248354 bytes, https://footwearresearchnetwork.org/articles/concealed-shoes-revealed, sha256 5e353d2f81f4c6ee4dca42362a36ec56981c6e4247dadc95a108f5e1bb432ef5 (= manifest).
- S651 live: HTTP 200, 46556 bytes, https://collections.vam.ac.uk/item/O87367/ (no redirect away from the record), sha256 8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79 (= manifest).
- Row quotes locate in BOTH the live text and the pinned capture: `locate_in == True` for both (locator's own predicate).
- OLDWORD screen (all four frozen phrases from accept-d.py:102-107) over the whole candidate entry: zero hits; also zero hits in S650/S651 scope+anchor+teaches cells.

## AUDIT S650 OK

Candidate entry line (candidate-entry.md:103, the only line citing S650):
`- Concealed shoes: Shawcross says the reason why people concealed shoes remains a mystery; University of Hertfordshire research currently suggests less and less that they were specifically apotropaic items, and that they were connected to notions of good luck and hope (S650). **C**`

Row: SOURCES.md:605, status mined, tier B, used-by the entry; teaches opens `supersedes S623 —`; quote `currently suggests less and less that they were specifically apotropaic items, ones that have the power to avert evil influences or bad luck` (anchor: University of Hertfordshire research paragraph, `locate_in=True`).

Page evidence (all in article body prose, not heading/caption/nav/cookie/promo):
- Clause "remains a mystery": verbatim body sentence — "As common as this practice appears to have been the reason why people concealed shoes remains a mystery. To date there has been no contemporaneous written evidence found to pinpoint a specific reason…".
- Clause "suggests less and less … apotropaic": verbatim in the research sentence — "The research undertaken by the University of Hertfordshire, in particularly Professor Owen Davies and Dr Ceri Houlbrook, currently suggests less and less that they were specifically apotropaic items, ones that have the power to avert evil influences or bad luck, …". This sentence also carries the row quote exactly (locator True).
- Clause "connected to notions of good luck and hope": verbatim, same sentence, under the same verb.
- Teaches cell carried: the research sentence plus the article's authorship (Rebecca Shawcross) carry "Shawcross reports that University of Hertfordshire research currently suggests less and less that concealed shoes were specifically apotropaic items, and that they were connected to notions of good luck and hope."
- Attribution check: "Shawcross says" for the mystery clause is fair — the article is first-person FRN authorship by Shawcross ("…we collaborated with the university of hertfordshire to digitise the concealed shoe index…").

Round-59 mapped rejection (S623, spot-check section 3): the old entry "stated the apotropaic purpose as fact" while the page hedges ("For many years the most common theory was…", "remains a mystery"). The new line states no apotropaic purpose at all: the theory appears only as declining ("suggests less and less"), the mystery is acknowledged, and the good-luck-and-hope reading is the page's own clause. Frozen phrase 4 ("concealed shoes highly worn and often patched act as apotropaic devices") absent from line, row cells and entry. Over-reach gone, not reworded. Teaches differs from S623's row teaches; same page as S623's first URL (footwearresearchnetwork.org/articles/concealed-shoes-revealed).

Notes (not defects):
- The page's own sentence attaches both conjuncts to "suggests less and less that …, and that …". The entry mirrors that structure word-for-word, so it asserts nothing the page does not; any "fix" of the ellipsis would insert words the page lacks. Leave as is.
- The quote starts mid-sentence (lowercase "currently"); this is disclosed by the anchor ("University of Hertfordshire research paragraph") and is contiguous body prose, not a fragment of a heading or caption.

## AUDIT S651 OK

Candidate entry line (candidate-entry.md:70, the only line citing S651):
`- Ga'u as container: the V&A record describes this amulet case or ga'u as used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil (S651). **B**`

Row: SOURCES.md:606, status mined, tier A, used-by the entry; teaches opens `supersedes S643 —`; quote `was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil.` (anchor: summary description paragraph beneath the object title, after its opening words "This amulet case or ga'u of silver and coral", explicitly NOT the Physical description catalogue field).

Page evidence:
- The quote is verbatim and locates twice, both object-description body text: (1) the summary paragraph directly beneath the title block — "This amulet case or ga'u of silver and coral was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil. This type of round amulet box was most popular among the nomads of north east Tibet…"; (2) the "Summary" field of Object details. Neither hit is navigation, cookie or promo text (the nav strings "Join support shop…" sit outside the sentence).
- Entry line clause coverage: "the V&A record describes" (report verb, correct attribution), "this amulet case or ga'u" ✓, "used to hold rolled prayers and blessed or holy objects" ✓, "believed to protect the wearer from evil" ✓ — every clause sits in that one summary sentence. No added contrast, cause, date or place; no efficacy claim (scope's "not evidence of efficacy or that the objects alone protect" is respected).
- The entry correctly tracks the summary wording "from evil", not the Physical description's "against evil"; and "used to hold", not the Physical description's "used to contain".

Round-59 mapped rejection (S643, corpus/lessons/round-59.md:72 + spot-check section 3): the old proposition credited the protection "to those contents rather than to the metal shell" (frozen phrase 3), a contents-versus-shell contrast the record never makes; its quote was the Physical description sentence. The new line drops the contrast entirely and rests only on the summary sentence. Over-reach gone, not reworded. Teaches differs from S643's row teaches; same page as S643's first URL (collections.vam.ac.uk/item/O87367/).

## Flags
- None. No quote on my two ids is a heading, caption fragment, promo, cookie or navigation text. No REWRITE and no TEACHES findings.

## Residual risk / verification gaps
- S650's "and that they were connected…" ellipsis inherits the page's own ambiguity (see note above); a hostile reader could parse both conjuncts under "less and less". Mirrors the source exactly, so a blind seat cannot call it added claim; no action.
- This audit covers only S650 and S651 (assigned ids). Predicate-side checks I confirmed incidentally (each id exactly one entry line, both new lines, tier, status mined, supersedes prefix, same-page mapping) are not a substitute for the counter's full run at 14e6413.
