# Round 51 attempt 3, falsify wave — ReviewCSec09 (claim C, section 9: alternate signing by hearing people)

Attack target: `corpus/knowledge/linguistics/sign-languages-manual-modality.md` §9 (lines 133–147) against SOURCES rows S075, S081, S109, S110, S111, S112 and the `politeness-taboo-euphemism.md` anchors `:75`, `:77`, `:101`. All work read-only in the lane; no sandbox needed (no mutations); no installs performed; no git/jj commands run.

## Commands run (all exit 0)

| Command | Output (abridged) |
|---|---|
| `sed -n '75p;77p;101p;118p' corpus/knowledge/linguistics/politeness-taboo-euphemism.md \| cut -c1-400` | :75 = "Domain inventory (seed 5–8): … names — the dead, and rulers … occupational (hunters and fishers rename the quarry and ban boat-words; specific regional cases to-verify)"; :77 = "What taboo does to language: … never deleted, replaced and preserved as a citation-form"; :101 = "1. Frozen replacements in the plain lexicon. PIE *h₂ŕ̥tḱos 'bear' …"; :118 = worked micro-example |
| `sed -n '35,39p' corpus/knowledge/verification/calibration-registry.md` | R / C / B / H / T code definitions |
| `awk 'NR==100\|\|NR==104\|\|NR==110\|\|NR==138\|\|NR==139\|\|NR==140\|\|NR==141' corpus/SOURCES.md` | full rows S071, S075, S081, S109, S110, S111, S112 |
| `awk 'NR==110\|\|NR==139\|\|NR==140\|\|NR==141' corpus/SOURCES.md \| grep -o "mined \| .*"` | used-by cell = `corpus/knowledge/linguistics/sign-languages-manual-modality.md` for S081, S110, S111, S112; S075 and S109 visible in the full-row dump |
| `curl -sL https://www.archives.gov/research/guide-fed-records/groups/106.html \| grep -i -B2 -A6 "intertribal\|sign language" \| sed 's/<[^>]*>//g' \| head -60` | RG 106 §106.3: "Development of an intertribal sign language dictionary of the American Indians of the Great Plains, and the theory, history, and practice of the sign language, ca. 1930-31 (13 reels)" |
| `sed -n '144,148p' …sign-languages-manual-modality.md`; `grep -n` for row strings | §9 line map: 133 heading, 135 headline, 139 Warlpiri row, 140 PISL row, 141 Cluny row, 142 sawmill row, 144 design rule, 145 calibration note, 146 speech-ban trigger, 147 terminology |
| `sed -n '190p' …sign-languages-manual-modality.md \| cut -c300-700` | §12 uses: "…plus a separate mourning alternate sign used by hearing women (S081); … the mourning sign answers a speech ban whose substitutes follow `politeness-taboo…`" |
| `realpath .ufo/waves/round-51/falsify && ls .ufo/waves/round-51/falsify` | `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-51/falsify` (inside the lane; report target confirmed) |

## Sources re-opened (access date 2026-10-22)

- **S075** — https://pmc.ncbi.nlm.nih.gov/articles/PMC4821822/ (Goldin-Meadow & Brentari 2017, BBS 40:e46, full text). Found §4.3 ("Silent gesture in hearing speakers is really spontaneous sign"): sawmills — "in sawmills where noise prevents the use of speech, workers create silent gestures … ([Meissner & Philpott, 1975])"; monastic — "Christian monastic orders impose a law of silence … ([Barakat, 1975])"; Aboriginal mourning — "Aboriginal sign languages have evolved in Australia in response to a taboo on speaking during mourning; since mourning is done primarily by women in this culture, Walpiri Sign Language tends to be confined to middle-aged and older women ([Kendon, 1984, 1988b, 1989])". Row quote, tier A and scope hold; §4.3 is in the row's anchor list.
- **S081** — https://books.google.com/books/about/Sign_Languages_of_Aboriginal_Australia.html?id=Aa34NAEACAAJ (redirected to google.com.br). Description matches the row's quotes verbatim ("first book-length study … sign language as a means of communication among Australian Aborigines … fieldwork conducted over a span of nine years … structure of sign languages and their relationship to spoken languages"). Tier B publisher description; scope holds, with the note that the blurb never says "alternate" or "hearing" — the row's scope gloss "alternate sign languages" is interpretive.
- **S109** — https://konferens.ht.lu.se/kendonsymposium2023/abstracts/ (Jennifer Green abstract). ¶1 matches the row verbatim: "predominantly used by hearing people as an alternative to speech when speech is either impractical or disallowed for cultural reasons"; later: "a Warlpiri meeting … his Warlpiri sign language dictionary". Tier B abstract; scope holds; Warlpiri is named.
- **S110** — https://assets.cambridge.org/97805216/90300/excerpt/9780521690300_excerpt.pdf (Davis 2010, Hand Talk). P. 1 description verbatim: "spoke so many different languages … As extensive trade networks developed and political alliances became necessary, an elegant language of the hands developed that cut across spoken language barriers … as a primary language of American Indians who are deaf." Contents confirm "List of tribal delegates at the Indian Sign Language Council, 1930", §5.1, §5.2 "Film dictionary of Indian Sign Language", Appendix 3 "Introductions to films of the 1930 Indian Sign Language Council" (pp. 197–201). Tier B publisher excerpt; scope holds. **The word "hearing" appears nowhere in the excerpt** — only deaf users are named.
- **S111** — https://www.archives.gov/research/guide-fed-records/groups/106.html (NARA RG 106, §106.3). Entry text matches the row exactly; dated "ca. 1930-31 (13 reels)". Tier A; scope holds. **The entry never says "council"** — it describes a dictionary/theory/history film project.
- **S112** — https://assets.cambridge.org/97805211/23938/excerpt/9780521123938_excerpt.pdf (Bruce 2007). Verbatim: "Rather than relinquish their ideal of silence as an essential virtue, the monks of Cluny created a silent language of hand signs that enabled them to express their needs without recourse to any verbal exchange" — this sentence sits on **excerpt PDF p. 4**, not p. 3 as the row's anchor says. Customaries "including their instruction in sign language" (taught) and "mechanisms of observance and control … to curb its misuse" (policed) support the design cell. Subtitle carries "c. 900-1200". Tier B; scope holds; anchor page off by one.

In-corpus anchors checked: politeness-taboo-euphemism.md `:75` (domain inventory: names of the dead; occupational bans), `:77` (replacement/preservation mechanics), `:101` (frozen replacements = fossil substitutes) — all three support their §9 uses. Used-by cells of all six S-rows name the entry.

## Findings

1. **MEDIUM — unsupported cell fragment "hearing" in the PISL row.** `sign-languages-manual-modality.md:140` — "Who signs: signers across nations — hearing and Deaf (S110)". The S110 excerpt (the only opened artifact behind this row) names deaf users only ("as a primary language of American Indians who are deaf"); hearing usage of PISL appears nowhere in the excerpt, and no other cited row in §9 states it. Half the cell rests on general knowledge, not an opened source — against the row's own calibration note at `:145`. Smallest fix: mark the hearing half `(to-verify)` or cite an opened source that states hearing PISL use (e.g. open Davis ch. 1, which discusses hearing users).
2. **MEDIUM — the Warlpiri mourning trigger is carried by no row it cites.** `sign-languages-manual-modality.md:139` — trigger "mourning speech restrictions — names of the dead (`politeness-taboo-euphemism.md:75`)". The politeness anchor supports only the names-of-the-dead taboo domain (and marks its own occupational specifics to-verify); S081's blurb says nothing about mourning or speech bans; S109 says only "disallowed for cultural reasons". The exact claim — taboo on speaking during mourning, with women as the signers — is stated verbatim in **S075 §4.3**, already opened, already cited by this entry (row 4 of the same table), and not cited in row 1. Smallest fix: add S075 to the trigger cell; that also lets the "(to-verify)" on "hearing signers, including bereaved women" in the same row be resolved, since S075: "mourning is done primarily by women … Walpiri Sign Language tends to be confined to middle-aged and older women".
3. **LOW — "a 1930 council was filmed to record it (S111)" over-cites S111 alone.** `sign-languages-manual-modality.md:140`. The NARA guide (S111's anchor) describes a "ca. 1930-31" intertribal dictionary/theory film project and never uses "council"; the council framing comes from S110's contents. Smallest fix: "(S110, S111)" or reword to the dictionary-film-project wording of the guide.
4. **LOW — "vows of silence" mislabels the Cluniac rule.** `sign-languages-manual-modality.md:141`. Bruce describes a "discipline of silence" / regulation of speech under the Rule (his n. 6 points to "The Meaning of Silence in the Rule of Saint Benedict"); monks do not profess a vow of silence. Smallest fix: "a rule-bound discipline of silence (S112)".
5. **LOW — S112 anchor page off by one.** `corpus/SOURCES.md:141` anchors the quote at "p. 3 (excerpt PDF)"; the "created a silent language of hand signs" sentence is on excerpt PDF p. 4. Fix: correct the anchor cell (append-only registry: superseding row or logged status/recheck change).
6. **LOW — §12 spill-over uses S081 for a claim its blurb does not carry.** `sign-languages-manual-modality.md:190` — "a separate mourning alternate sign used by hearing women (S081)" (NON-CANON worked example, outside §9). The S081 description mentions neither mourning nor women; support lives in S075 §4.3 + S109. Fix: cite S075/S109 there instead.

## Row verdicts against QUALITY criterion 6

- S075 (A): holds — full paper text, §4.3 carries all three §9 uses including the sawmill row at `:142` verbatim.
- S081 (B, publisher description): quote holds; no criterion-6 breach (declared tier B), but the blurb carries none of §9's Warlpiri substance — the row leans on S109/S075 for content.
- S109 (B, conference abstract): quote and scope hold; Warlpiri named; supports the headline and the relation cell at `:135`/`:139`.
- S110 (B, publisher excerpt): quote and scope hold; carries trigger/relation cells at `:140`; the "hearing" fragment exceeds it (finding 1).
- S111 (A): quote and scope hold; supports the archive claim; does not say "council" (finding 3).
- S112 (B): quote and scope hold; anchor page off by one (finding 5).

## Bounds, canon, register

§9 contains no canon decision (the design-consequence column is H-labelled; §12 is NON-CANON), no clinical, education-policy or rights ruling ("never a deficient substitute" and the terminology line at `:147` are lane register consistent with S076/S121 as cited in §13). No in-corpus path is mis-anchored: `politeness-taboo-euphemism.md:75`, `:77`, `:101` all resolve to supporting text.

## Verdict

**HOLDS-WITH-FIXES.** All four §9 systems are real and every row's load-bearing cells trace to opened sources once S075 §4.3 is counted; the defects are citation-precision failures (findings 1–6), none of which fabricates a source, a quote, or a canon decision.

## Unrun checks

- Round-lesson Gate quotes for S071–S124 (records seat's scope).
- Entry-level counters (`find corpus/knowledge -name '*.md' | wc -l`, `reports/round-28/readme/sweep.py`) and the §2 boundary table — other seats' scope.
- SOURCES rows S071–S074, S076–S080, S082–S108, S113–S122 generally (only my six rows checked).
