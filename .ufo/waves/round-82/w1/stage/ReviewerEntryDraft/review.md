# ReviewerEntryDraft — claim-D entry review, kotodama round 82 w1

Seat: ReviewerEntryDraft (leaf reviewer). Object: claim-D knowledge entry, reviewed as the w1
draft and re-measured on the installed file
`corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` (29,020 B; installed after the
L1's ACCEPT-D-82; the only diff from the reviewed draft is a quote-scope trim on the S907
etymology line, receipts/diff-draft-vs-installed.txt). All line numbers below are the
installed file's. Bar: lane `corpus/QUALITY.md` criteria 1-5, 11, 15, 27.

## Verdict

ACCEPT on QUALITY 1-5 and 15. One routed defect in the round's records, not in the entry:
the Gate draft's S907 supersede paragraph contradicts the rows draft's tier cell
("tier B" vs C). Two craft weaknesses in the entry, each fixed by ≤2 sentences (the entry
seat may take them or route them). S907 refute discipline (QUALITY 27): compliant.

## QUALITY 1-5, with the deciding line

- **1 Provenance — PASS.** Deciding line 7 (`- source:`): "no source outside that list is
  used for a factual claim in this entry." Factual claims about the real texts are confined
  to the 22 §3 bullets (lines 70-91), one row id each, quotes verbatim with loci; craft is
  labelled (6 NON-CANON/(craft) hits); Vethari is declared invented (line 50). Evidence:
  `stage/ScribeEntry/quote-check.txt` binds all 22 quotes to ids and word counts — all OK,
  `quote_exit=0`; `stage/ScribeEntry/fetch-records.md` gives per-quote located passages
  with served-file line numbers for S904/S906, the S905 paragraph, and the S907 sentence;
  my own S-id sweep of the installed file (grep -nE 'S9[0-9]{2}') finds exactly 22 cited
  lines, ids=1 on each. The gap-claim provenance also verifies: `- gap filled:` line 4
  states 255 base files / 0 filename hits / 27 vocab lines in 15 files / 0 institutional
  core / 4-hit `ritual` positive control — re-run at base `c285b2af…` gives 255, 0, 27,
  15, 0, 4 (receipts/corpus-refs-and-gap-counts.txt). Observation, not a defect: line 63's
  "real-world precedent in §3 #22" leans on tier-C S907; the use is a labelled craft lever
  (a lead, not sole support), consistent with QUALITY 6.
- **2 Calibration — PASS.** Deciding line 10 (`- scope:`): "reference method and lane
  policy … it decides nothing about what is true in any world" and line 7: "Anything the
  rows do not settle is labelled craft, method, or `(to-verify)`." The entry advances no
  scholarly framework requiring a mainstream/contested label; the one named pop-mythography
  hazard (Frazerian evolutionism) is kept out of the corpus by the Gate's S908 reject, which
  is exactly the QUALITY 2 discipline applied upstream. No strong-Whorf/Campbell moves in
  the lexicon sections — the colexification lever (line 63) explicitly disclaims any
  attested-language claim ("not about any attested language").
- **3 Coupling — PASS.** Deciding line 6 (`- couples:`): nine files with line refs and
  own/return clauses; §1 (lines 14-23) adds ten one-way partial owners. All fifteen cited
  corpus refs were read at base `c285b2af…` and each line matches the entry's claim of what
  that file owns (receipts/corpus-refs-and-gap-counts.txt): cuisine-food-lexicon:95,138,170
  (salt covenant / token / formula slot), ritual-liminality:21,110 (passage model /
  communitas "strangers made total equals"), binding-speech-complex:62 ("a word holds only
  where an executor exists" — verbatim), kinship-terminology:119 (address escapes, refusal
  penalties), furniture:3 and bathing:3 (topic-line ownership claims — these two cite the
  files' topic lines rather than a deeper row, acceptable since the claim is ownership),
  purity-pollution:33 (stranger as own/other, pharmakos), creation-myths-taxonomy:49
  (muskrat's-kin guest-right), greece-classical:75 (Hestia/hearths row), myth-folktale-
  genres:55 (ATU 750–849), orality-formulaic-language:66 (arrival type-scene);
  ordeal-judicial-proof-rituals.md and synthesis/worldbible-integration-contract.md exist
  at base.
- **4 Usability — PASS.** Deciding lines: 25-36 (six-row decision table with options,
  anchors, consequences), 38-48 (five-field lexicon table with test questions), 50-60
  (worked derivation + paradigm table), 93-106 (twelve-item craft checklist), 108-124
  (worked example with six settings). A worldbuilder can act on every section; the two
  weaknesses below are gaps inside strong sections, not missing sections.
- **5 Canon hygiene — PASS.** Deciding lines: 126 ("It decides nothing about what is true
  in any world — not whether a given world's gods exist, not whether its hearth goddess
  answers, not whether its tide judges") and 124 ("Decides nothing about any world;
  demonstrates the checklist."); line 10 adds the PROVINCE sentence (no claim about living
  communities). Handoff names the contract file and the packet (line 127-128).

## QUALITY 15 — cited lines clause-scoped

`python3 -B tools/check-cited-lines.py corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`
→ `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0 (receipts/citedlines-installed.txt).
Independent sweep of the installed file: 22 cited lines (70-91), exactly one distinct S-id
on each (7×S904, 7×S905, 6×S906, 2×S907); zero lines carry ≥2 distinct ids; 22 table rows,
zero carry an S-id. There is no MULTI-ID line and no TABLE-ID row to name. The lint's stated
limit (a one-id line holding two clauses passes; clause scope stays review-only) is honored:
no §3 bullet fuses two clauses.

## Craft attack — the two weakest sections

**W1. §2.1 worked derivation (lines 50-64) — a worldbuilder cannot reproduce the entry's
own examples, and cannot build the degree system the entry makes them design.**
(a) The stated morphology is exactly "three suffixes: -n agent, -t abstract/result, -k
instrument/gift" (line 50), but the entry's own example sentences use morphemes outside
that inventory: *hepam* "host-DAT" (-m dative, line 60), *hepan-eth* "roof-keeper-elder"
(-eth eldership, line 62), and the bare sibling loan *šen* (line 62). As written, the two
glossed sentences cannot be parsed or extended from the stated grammar.
(b) §5 coins five guest-class compounds — *dawan-sirat*, *dawan-oph*, *dawan-hal*,
*dawan-mok*, *dawan-ves* (lines 109-124) — but §2.1 never states the compounding device, so
a worldbuilder following §2.1 can build the five canonical terms yet cannot lexicalize the
graded degrees that §2 row 1 (line 27) makes the primary design lever (the very thing the
worked example then uses).
Smallest edit (two sentences, no rewrite): after line 51 add "Outside the derivational
suffixes: -m marks the dative (*hepam* 'to the host'), -eth marks eldership in the
kin-escape register, and *šen* is a kinship-system loan — none is derivational."; after the
derivation table add "Guest-classes compound on the guest-term (*dawan-oph* 'suppliant',
*dawan-ves* 'unseen guest', …) — lexicalize the §2 degree ladder here, not in the root
inventory."

**W2. The violation-consequence row (§2 table row 5, line 33; lexicon violation-term row,
line 47) — a worldbuilder cannot tell the five consequences stack, and the entry's own test
question is unanswerable.**
(a) Line 33 lists "feud by kindred duty / sacral sanction / compensation / outlawry / the
stranger-god test" as one cell of options; the consequence prose discusses the opt-out
polity but never says the five are rungs of one ladder. The stacking instruction exists
only in the checklist (line 100: "Build the breach ladder … give each rung a procedure and
a price") and the worked example (line 121: "each rung has a different audience"). A
worldbuilder copying only the decision table builds a one-rung culture and misses the
institution's stated depth.
(b) Line 47's test question asks "is the violator a criminal, a breaker, or an outlaw —
and which of those can be redeemed?" — `grep -in redeem` finds the word nowhere else in
the entry; nothing answers it, and the lexicon choice's coupling to the ladder choice
(breaker→feud/compensation vs outlaw→outlawry) is left unstated.
Smallest edit: prepend to line 33's consequence cell "These are rungs, not alternatives —
a working culture stacks two or three and prices each (worked in §5)."; append to line
47's row "Vethari leaves redemption unlexicalized: a redeemed *kobar* needs a ritual repeal
the culture must design — pick the term after the ladder."

## S907 reject discipline (QUALITY 27) — checked

The lesson Gate draft (`.ufo/waves/round-82/w1/drafts/lesson-gate.md`) is compliant in
substance. The S907 admitted bullet names the capture artifact
`reports/round-82/evidence/S907.txt`, the span 「one who receives hospitality in the house
of another」 (9 words), and the finding "present once after whitespace folding in body and
capture". The supersede bullet states the planned scaffold ground "was measured false on
both artifacts": live body `grep -n 'one who receives hospitality' guest-plain.txt` →
line 518, closing `</p>` inside `div.prp-pages-output`; on the capture "the same sentence
occurs once after whitespace folding (raw count 0 — the served HTML line-wraps it)".
Fetch records bind each UA to its response: `UA "curl/8.23.0" -> HTTP 200, 60273 B, wall
absent` and the browser-shaped UA verbatim -> HTTP 200, 60273 B, byte-identical
(sha256 f6db75f3…); capture `UA "curl/8.23.0" -> HTTP 200, 29020 B` (sha256 37a3eb42…);
positive control in the same Wikisource 1911 namespace (Ordeal, HTTP 200, 87131 B, 3374
words of prose) per QUALITY 21+24. Automation: none.

**Routed defect (records consistency, not S907 discipline):** the Gate draft's supersede
bullet reads "Disposition: mined, tier B; the row's `scope` cell records that the article
is a single ~55-word gloss … and the tier is C on that ground" — "tier B" contradicts the
rows draft's S907 row, whose tier cell is `C` (verified at
`drafts/rows/S904-S907.md:raw:4`), and the same paragraph's own next sentence. One-word
fix in the Gate draft ("tier B" → "tier C") before install, else the committed lesson
contradicts the SOURCES row it cites (QUALITY 6 territory).

Observations (non-blocking): (i) the Gate draft measured the entry at "28992 B" — the
installed file is 29,020 B; the entry was revised twice mid-wave; drop or re-measure byte
counts of a moving draft at install (QUALITY 14 spirit). (ii) The carried heraldry reject
names the rejected entry itself as artifact (`git show …:corpus/knowledge/myth-symbol/
heraldry-emblems-identity-marks.md` → first line quoted) without the literal word
present/absent — acceptable for a carried entry-existence ground, but add the word at
install so the QUALITY 27 one-liner's shape is clean. (iii) The fresh S908 Golden Bough
reject and the EB11 Coin/Mint probes are fully QUALITY-27-shaped (artifact + 「」 span +
present + UA-bound bytes).

## Unrun / residual

Live re-fetch of the four URLs was not re-run by this seat (the scribe's scratch bytes were
deleted at yield per discipline; I verified the records and cross-readings, not live
pages). Claim-O (`tools/check-sources-recheck.py`) is outside this seat's scope; the
ExecEvidence selftest-fixture finding travels with the tool owner. The two craft weaknesses
are quality-of-craft findings for the entry seat; they do not block the acceptance above.

## Receipts

- `receipts/citedlines-installed.txt` — lint verdict on the installed entry.
- `receipts/corpus-refs-and-gap-counts.txt` — all 15 corpus line refs + the six gap-fill
  counts re-derived at base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c`.
- `receipts/diff-draft-vs-installed.txt` — the w1 draft vs installed bytes.
- `receipts/corpus-refs-first-pass-garbled.txt` — first-pass capture (a tee bug garbled
  interleaving; the readable ref lines in it corroborate receipts 2; kept for honesty).
