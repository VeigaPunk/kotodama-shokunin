# Round 51 attempt 3 — FALSIFY — ReviewCSec11 (claim C entry, section 11)

Attack target: `corpus/knowledge/linguistics/sign-languages-manual-modality.md` §11 "Decision table and build order" (lines 162–187): every decision-table row's section pointer and anchor, the S100 citation, build order, and DR-SGN-01..04. All paths lane-relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Author-lane attack; this report is a recommendation, not an admission.

## Commands run (all in the lane, read-only)

| Command | Output | Exit |
|---|---|---|
| `grep -n '^## ' corpus/knowledge/linguistics/sign-languages-manual-modality.md` | §11 header at line 162 (next §12 at 188) | 0 |
| `grep -rn 'DR-SGN' corpus` | exactly 4 hits: the entry's own lines 183–186. Prefix unused anywhere else in `corpus/` | 0 |
| `grep -rn 'DR-' corpus/knowledge --include='*.md'` (excluding this entry) | precedent scheme exists: `language-shift-obsolescence-revival.md:171-180` uses `DR-1..DR-10`; `taboo-strata-lifecycle.md:110-117` uses `DR-TS-01..08`. `DR-SGN-NN` matches the `DR-TS-NN` mnemonic style; no collision | 0 |
| `grep -c 'round-51\|boundary-count' corpus/knowledge/linguistics/sign-languages-manual-modality.md` | `0` (claim C's must-not-cite holds for §11 and the whole entry) | 0 |
| `find corpus/knowledge -name '*.md' \| wc -l` | `227` (matches claim C's after-required; full counters are sibling seats' scope) | 0 |
| `read` of the four neighbour anchors (below) | all resolve and support their cells | — |

Anchor re-reads (exact line confirmed by `grep -n` on each file):

- `linguistics/phonetics-phonology.md:201` — "Sign-language phonology works without acoustics — handshape, location, movement carry contrast (Sandler & Lillo-Martin 2006)". Supports row 1's gloss "manual parameters carry contrast" and build item 3. ✓
- `linguistics/syntax-typology.md:99` — "Claims that SOV is 'the human default' draw on emerging sign languages and homesign … suggestive, interpretively contested — don't assert it flat." Supports row 2's gloss "don't assert a default word order for homesign". ✓
- `linguistics/conlang-methodology.md:36` — "Rule (Rosenfelder 2010; Peterson 2015): start from the society, not the phonemes." Supports row 4's gloss "start from the society's need". ✓
- `linguistics/writing-systems.md:20-21` — line 20 featural ("distinctive phonetic features"), line 21 semasiography "(not writing proper) | meaning directly, not speech". Supports row 6's gloss and DR-SGN-04's failure cell. ✓
- `calibration-registry.md:38` = the **H** row ("Heuristic or interpretive framework … Generate with it; label the designer's choices"). §11's opening line 164 cites `:38` for H — correct (35=R, 36=C, 37=B, 38=H, 39=T). ✓

## Source re-opened (access date 2026-10-22)

- **S100** — https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ (Sandler, Meir, Padden & Aronoff 2005, PNAS 102(7):2661–2665). Opened OK (native HTML, PMCID PMC548320, PMID 15699343). Found at the stated location: abstract — "In the space of one generation from its inception, systematic grammatical structure has emerged"; Results (Fig. 3 discussion) — "Where two nouns are mentioned in a clause, subject precedes object (in all 32 cases)"; "the prevalent word order for ABSL sentences is S–O–V"; orders differ from ambient Arabic/Hebrew and ISL. The §11-adjacent word-order facts hold at the declared anchor. **However**, the hearing-signer material sits in the *Introduction* (Kisch paragraph): "a significant fraction of its hearing members communicate by means of a sign language"; "Many of the signers in this community are hearing" — outside the row's registered anchor. Quote, tier (A) and scope otherwise hold; the used-by cell names this entry (SOURCES.md:129).

No other external URL is cited in §11 — its remaining "check" cells point at in-corpus sections/anchors, all re-read above. Unrun: no other S-row URLs (none cited by §11).

## Findings

**F1 — medium — §11 row 3 (`sign-languages-manual-modality.md:170`) uses S100 beyond its registered anchor scope.**
Row: "is a small community with high hereditary deafness | a village/shared sign language that hearing neighbours also learn; expect expansion beyond the deaf cohort | §3; S100". The claim cell's hearing-neighbour/expansion content is owned by §3/§4 (S086, S091–S093). The check cell hands the reader S100, whose registered scope (SOURCES.md:129) is "the ABSL word-order findings … (second generation)", anchor "Abstract; Results (Fig. 3 discussion)". The hearing-signer facts exist in the paper but in the Introduction, outside that anchor; conversely nothing tells the reader what S100 is being checked *for* here (unlike row 1, which glosses its anchor). Smallest fix: gloss the cell — e.g. "§3; §4; S100 — early word order, not the hearing-signer census" — or file a superseding S100 SOURCES row extending the anchor to the Introduction's Kisch passage (QUALITY criterion 6 mechanics; never an in-place tier edit).

**F2 — low — DR-SGN-03 (:185) and build item 3 (:177) enumerate three parameters where §5 establishes six.**
"Choose the manual parameter set (handshape × location × movement)" omits palm orientation (§5: Battison's fourth parameter), grammatical nonmanuals, and two-handed constraints — all parameters §5's own build order ("handshape inventory → locations → movement classes → orientation rule → grammatical nonmanuals → two-handed constraints") requires before the lexicon. Read literally, the decision record licenses exactly the under-specified design §5's failure column warns about (orientation collapsed into homophony). Fix: "handshape × location × movement × orientation (see §5's six-row parameter table)".

**F3 — low — build item 3 (:177) is the only build step without an owning §-pointer.**
Items 1/2/4/5 cite §3/§7/§6/§10; item 3 cites only `phonetics-phonology.md:201` and never names §5, the section that owns manual phonology. Fix: "(§5; `phonetics-phonology.md:201`)".

**F4 — low — row 1's claim cell promises "registers" (:168) but its check cell points only at §3.**
§3's deaf-community row covers transmission, scale and history; register material lives in §10 (contact registers) and the `sociolinguistics-registers.md:50` boundary row. Fix: "§3; §10" in the check cell.

Not defects (checked and passed): every section pointer resolves (§3, §9, §10, §6, §7 all exist and own the pointed detail); row 2's homesign framing ("not a community language") is consistent with §3/S079 ("language-like structure without a model"); DR-SGN-01..04 are actionable (each has a decision, a concrete trigger, and an observable failure mode); `DR-SGN` prefix is unused elsewhere in `corpus/` and follows the existing `DR-TS` house style; terminology clean (no "deaf-mute"/"hearing-impaired"; capital-D usage matches the §13 B row); no canon decision, clinical claim, education-policy or rights ruling in §11 (all four DR rows are design-method rules ending before the lore handoff); the calibration H label at line 164 is correctly registered.

## Verdict

**HOLDS-WITH-FIXES.** §11's pointers, in-corpus anchors, DR records and prefix hygiene all check out against the landed bytes; the S100 citation in row 3 needs a scope gloss or a superseding SOURCES-row anchor (F1), and the parameter enumeration in DR-SGN-03/build item 3 should name §5's full parameter set (F2/F3).

Residual risk: I did not re-open any S-row other than S100 (§11 cites no other external S-id in a check cell — verified by reading §11 in full); abstract-vs-fulltext tiering for S100 is per its row and was not re-adjudicated. Unrun: `reports/round-28/readme/sweep.py` (avoided — write behavior unknown; owned by other seats).

Tooling: no installs or updates performed (none needed).
