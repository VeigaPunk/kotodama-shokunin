# CriticClaimC — round 54 attempt 2, residual falsify check of claim C

Seat: KotodamaR54a2.CriticClaimC (attack only; no fixes made). Lane tip `6a658ca4fe9230f70eaa3b421e6c9d78da5c1633` (real lane HEAD = same, read-only). Sandbox: `/fast/scratch/hyaku/kotodama-r54-a2/CriticClaimC/kotodama-shokunin` (git clone, checkout 6a658ca). Installs: none.

## 1. Mechanical re-runs (sandbox clone at 6a658ca)

| Command | Exit | Key output |
|---|---|---|
| `python3 -B reports/round-54/accept-c.py` | 0 | SET PASS count=230 added=[masks-masquerade.md] removed=[]; SWEEP PASS rows 230 files 230 missing_from_index 0; FLOOR PASS cited=46; RANGE PASS bad=[] range_notation=[]; STATUS PASS; USEDBY PASS; ACCESS PASS "2 flagged rows, 0 findings" |
| `python3 -B reports/round-28/readme/sweep.py` | 0 | rows 230 files 230; missing_from_index 0; topic_mismatch 0; orphan_rows 0; header_drift {}; totals_ok True; footer_ok True; readme_sha256 6172793…7e77 |
| `python3 -B tools/check-source-access.py` | 0 | `ACCESS: 2 flagged rows, 0 findings` |
| `sources-census.sh validate --root <scratch root: kotodama-shokunin symlink → clone + kotodama row copied from fleet shokunin.conf> kotodama` | 0 | 9 × W04 (S127–S133, S185, S186: same URL across scopes; all pre-round rows); `ok` |
| `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (real lane, read-only) | 0 | identical 9 × W04; `ok` |
| `sources-census.sh census <clone>` | 0 | rows 284, mined 240, queued 34, rejected 10, missing 0 |

First census attempt with `--root <clone-parent>` exited 2 (`config not found … shokunin.conf`); fixed by the scratch conf copy above. `git diff --stat 5757c45 6a658ca`: only `corpus/README.md`, `corpus/SOURCES.md`, the entry (3 files) — matches `lands`.

## 2. Review-only clauses

### 2a. Topic delivered — HOLDS
§1 (what the mask is), §3 (complex), §4 (make/keep/wear/see/know/unmask), §5 (voice and interpreters), §6 (ritual, funerary, theatrical, festival occasions), §7 (funerary), §8 (reveal/removal/retirement), §12 (universal / art-object traps) cover every element of the declared topic line.

### 2b. One-way pointing to partial owners — HOLDS (one-way) with one restatement defect
All 12 §2 anchors plus `verification/calibration-registry.md:35-39` resolve at 6a658ca; no owner file was modified (one-way holds).

| Anchor | Cell supported? | What the line says (≤25 words) |
|---|---|---|
| culture-material/ritual-garments.md:20 | CARRIED | "Sacred dress is not decoration on an office; it *is* the office, transferable and revocable." |
| culture-material/costume-semiotics.md:127 | CARRIED | "Keep a ledger per item: term \| carrier \| wearer \| viewer \| penalty \| era-of-change" |
| culture-material/funerary-material-culture.md:47 | CARRIED (MONUMENT omitted) | "DISPOSAL … ASSEMBLAGE … MONUMENT … and WORD" |
| culture-material/adornment-body-codes.md:75 | CARRIED | "material word … applicator/tool word … occasion word … and moral slur" |
| myth-symbol/ritual-liminality.md:117 | CARRIED | "Pick the liminal medium and its props: seclusion hut, desert, ship, labyrinth, wound-scar, mask, fasting" |
| myth-symbol/trickster.md:13 | CARRIED | "the licensed crossing of a boundary … *which boundary*, *whose license*, *what institution holds the license*" |
| civilizations/siam-thai.md:2 | CARRIED (topic line) | "Ramakien indigenization, khon masked performance, rachasap, and sakdina" |
| civilizations/pacific-northwest.md:157 | CARRIED, slight over-read | "Regalia and held objects can display family histories or privileges … may participate in a right" — cell says "participants in family histories"; the line makes them participants in a *right* |
| civilizations/igbo.md:97 | CARRIED (section §5 "Mmanwụ", line 94) | "controls membership, making, storage, revelation, appearance, and sanction. Access restrictions differ by place and mask type" |
| civilizations/yoruba.md:136 | CARRIED (Gelede named at :135, not :136) | "build a local satire genre whose sanctioned voice, moving costume, material innovations, and audience knowledge agree" |
| civilizations/haudenosaunee.md:139 | CARRIED | "The policy opposes public exhibition and exhibition use of reproductions, photographs, castings, or illustrations. [S95, “Exhibition”]" |
| civilizations/newar-nepal.md:147 | CARRIED | "making, keeping and wearing ritual equipment are not the same office" |
| verification/calibration-registry.md:35-39 | CARRIED | rows R, C, B, H, T |

Defect (duplicate authority): the entry says the haudenosaunee row "points to that public boundary", but `masks-masquerade.md:69` also quotes the same 1995 Grand Council policy itself through a new row, S265. The owner cites the same document as `[S95]` (`haudenosaunee.md:78,133,134,139`). In the lane registry, S095 is a different source: Brentari, "Sign Language Phonology" (SOURCES.md:124). So the owner's pointer does not resolve in the registry, and the policy now has two citation identities. Census E04 cannot catch this because the URLs differ. Impacted axes: provenance, one-owner boundary. Smallest fix: cut :69 down to a pointer to `../civilizations/haudenosaunee.md:139` plus the Hopi sentence, or route the owner's broken `S95` so that S265 becomes the single row for the policy. The owner's broken `S95` predates this claim and is outside its scope; it is routed here, not charged to C.

### 2c. Restricted traditions beyond a community or holding-institution public statement
- **Haudenosaunee medicine masks — HOLDS.** :69 quotes only S265. The page I re-opened (nativetech.org, HTTP 200) reads: "The public exhibition of all medicine masks is forbidden." / "No institution has the authority over medicine masks". There is no image, construction detail or sequence.
- **Hopi — HOLDS.** :69 gives only the Hopi Cultural Preservation Office (HCPO) statement (S266, kind `community`). Not re-opened.
- **Nyau — HOLDS (absent).** No Nyau or Gule Wamkulu sentence appears in the entry. The S262 page discusses Gule Wamkulu; the entry takes nothing from it.
- **Kòmò — FAILS.** `masks-masquerade.md:79` says: "Driver reports a roar made by several friction drums carried by the mask bearers, heard as one omnipresent voice (S267, §Sources of power)". Opened page (S267 PDF, HTTP 200, printed p. 107): "The voice of the jarawara mask … is created not by a mirliton, but by the sum of several friction drums held by the mask bearers" and the voice "keeps non-initiates hiding silently indoors". The jarawaraw is a Kòmò mask of a secret jow "power association" (p. 106). The sentence therefore discloses how a restricted mask's voice is produced, which is withheld from non-initiates. Its source is a scholar relaying Jespers, not a community or institution statement. The sentence also drops the name Kòmò, which hides where the claim comes from. This breaks the entry's own scope line :12 ("no image, construction detail or ceremonial sequence"). :76 (headpieces forbidden to non-initiates) only states a restriction and is acceptable. :85 (Kòmò masks come out after sunset in a seasonal coming-out) is ceremonial timing from the same scholarly source, a minor case of the same fault. Smallest fix: delete :79 and drop the Kòmò clause from :85.
- **Sande — FAILS (narrow).** The holding-institution part of :67 is CARRIED. S260, the Agnes Etherington Art Centre page (HTTP 200), reads: "Commissioned by the Sande society … worn exclusively by women, a rarity in African masquerades". The rest of :67 and all of :110 come from scholars (Curnow S261, Phillips S262), not from Sande or a holding institution. They describe Sande access (an enclosure men could not enter, which figures are brought out in stricter villages) and the gonde clown's reuse of a retired sowei mask. The Phillips sentence also OVER-READS: the page says "sometimes in an enclosed area that men could not enter" and "the Sande women brought out the fully masked and costumed figures". The entry drops "sometimes" and adds "only". Smallest fix: keep the S260 sentence; restore "sometimes" and delete "only" in the S262 sentence, or cut it and :110 if the rule is strictly community or holding institution.
- Beyond the five named traditions, same pattern: :75 gives construction detail of the Boki spirit voice-disguiser ("bone tube with a spider-silk membrane", Potter S268, a scholar), and :77 describes the Tarok orìm coded register (Blench S269). Both describe how a secret society produces its voice. This is flagged for the judge, not counted.

### 2d. One case generalised to "some communities" or "masks everywhere" — FAILS (2 sentences)
- `:65`: "The Pingxiang fieldworker reports that some sacred rituals were not fully accessible to him (S249, p. 99): a closed portion is normal". One fieldworker in one county becomes a general norm. Smallest fix: "a closed portion is possible".
- `:53`: "a type can be reproduced, a portrait cannot". This rests on one V&A mould (S253), and the entry's own §7 contradicts it: Smith reports a face mould and a fresh cast (:99, S255), and Pliny's wax faces (:21) were impressions. Smallest fix: delete "a portrait cannot".
- Minor: `:8` "the threshold phase in which masks often appear" has no citation (couples field).
- The literal phrases "some communities" and "masks everywhere" do not appear. "Universal" and "everywhere" occur only as R-coded traps (:19, :142). HOLDS for those.

## 3. Head fields and line count vs the round-53 model entry (`linguistics/speech-surrogates-whistled-drummed.md`) — HOLDS with notes
- Both have the same H1 and the same field set in the same order: topic, gap filled, sources (in-corpus + external shelf), couples, source, verified-at, recheck, scope.
- Field differences:
  - The entry names no S-id range. The model writes "S134–S183"; the entry's RANGE leg forbids range notation, so this is intended.
  - In-corpus anchors are moved to the §2 table instead of listed inline.
  - `recheck:` is only "see §13." where the model has inline recheck actions.
  - verified-at uses `find -type f`, where the model uses `-name '*.md'`. This is consistent with the SET leg.
- Line count: the entry has 153 lines and the model 195 (−42, −21.5%).

## Counts
Clauses: mechanical re-runs 4 of 4 exit 0 (HOLDS); topic HOLDS; one-way HOLDS (13 of 13 anchors resolve and support their cells, plus 1 duplicate-authority defect); restricted traditions: 3 HOLDS (Haudenosaunee, Hopi, Nyau), 2 FAILS (Kòmò, Sande-narrow); generalisation FAILS (:65, :53); head and line count HOLDS with notes.
Item verdicts: 15 CARRIED (13 anchors, plus S265 and S260 quotes), 2 OVER-READ (S262 at :67; pacific-northwest:157 cell, slight), 0 WRONG-LOCATOR, 1 restriction breach (:79, carried by its page, but restricted content).

## Unrun checks
- I did not re-open S239–S259, S261, S263–S264, S266 or S268–S284, so per-sentence carriage of the remaining roughly 40 rows is unchecked.
- I did not replay the 13 RED controls.
- I found no line-count budget for a model entry and did not search the QUALITY or rubric files for one.
- must_not_cite has since been checked: a grep for `lessons` in the entry returns 0 matches, so it HOLDS.
