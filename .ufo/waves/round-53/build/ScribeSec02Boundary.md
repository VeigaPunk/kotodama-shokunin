# ScribeSec02Boundary — Claim C, entry section `## 2. One-owner boundary`

- Seat: `KotodamaR53.ScribeSec02Boundary` (leaf; no delegation, no background jobs, no swarm).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch main. HEAD read at this seat: `60f1d2a3d832b926e37f82b11c67496d131a1431` (the round-53 declaration commit) on base `a9cf95fe47a82b516f6c2487cb76b89c3a71c493`; `git status --porcelain` shows only the untracked `.ufo/waves/round-53/`, `corpus/lessons/round-53.md`, `reports/round-53/final-measures.py` and the claim-D edit to `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (not mine).
- Read-only seat: **no corpus file, no SOURCES row, no README row and no entry file was created, edited, staged or committed.** The only file written is this report, at `.ufo/waves/round-53/build/ScribeSec02Boundary.md` inside the lane repo. The draft was assembled in `/tmp/sec02draft.md` (scratch, outside the lane).
- Assigned item: draft claim C's entry section 2 for `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` — one lead sentence plus a `| Neighbour (anchor) | What it owns | This entry's boundary |` table with 9–13 rows, one distinct in-corpus neighbour per row, each row anchored by exactly ONE backticked `file.md:N`.
- Claims axis: coverage (claim C). **No S-id of any number is cited in the draft**, so the "every cited S-id must be S187 or above" condition of `reports/round-53/accept-c.py` is satisfied by construction; no draft `NEW-<SeatName>-<n>` id appears either.
- The entry file `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` does not exist yet and was **not** created by me. `find corpus/knowledge -name '*.md' | wc -l` → **228** at the lane worktree.

## 1. Result

- Section 2 drafted at **exactly 18 lines** (H2 line, blank lines and the trailing blank that separates it from `## 3.` all counted) in the model entry's pipe-table style, ready to paste.
- **11 rows**, one per distinct in-corpus file, each anchored by exactly one backticked `file.md:N` with a single line number — inside the assigned 9–13 range.
- Every anchor was re-read at the lane worktree this session and is quoted verbatim in §3 below.
- The draft cites **no S-id below S187** (no S-id at all) and no draft id, so the accept-c SIDS leg cannot fail on this section.
- Every `§N` cross-reference in the table points at a planned C section (1 register property, 3 gesture types, 4 pointing, 5 space and time, 6 language shapes gesture, 7 quotable gestures, 8 social control, 9 acquisition), all ≤ the planned 14 H2s.
- Two conflicts with sibling advice are recorded verbatim in §5 for the canonical Rust judge.

## 2. Drafted section text (paste-ready, 18 lines)

Paste as-is. Path style follows the model entry `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:32-47`: same-partition files bare (`sign-languages-manual-modality.md:64`), cross-partition files with `../` (`../culture-material/adornment-body-codes.md:79`).

```markdown
## 2. One-owner boundary

Each neighbour below owns its register; this entry cites it one way and owns only the co-speech layer: gesture as a systematic part of the utterance it accompanies (§1), and what a language's speakers do with their hands while they talk.

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `../culture-material/adornment-body-codes.md:79` | the nonverbal-behaviour toolkit: the Ekman–Friesen categories, Morris's emblem geography, Hall's proxemic bands, and the etiquette script built on them | the category names, the emblem geography, the proxemic bands and the etiquette script stay there; this entry owns only the co-speech relation — what such a gesture contributes to the utterance it accompanies, and how a quotable gesture is learned (§1, §3, §7, §9) |
| `sign-languages-manual-modality.md:64` | the manual modality's own boundary row, which places co-speech gesture outside sign languages and routes conventional emblems to the body-code file | sign and its acquisition stay there; this entry takes the register that row declines — co-speech gesture as part of a spoken utterance (§1, §9) |
| `numerals-and-measures.md:107` | finger counting as a culturally patterned counting technology, with its own parameter space (direction, start finger, thumb as counter or folder) | counting gestures stay there; this entry cites that row once, for counting-as-body-code, and owns no numeral or counting system |
| `../myth-symbol/direction-symbolism.md:36` | the absolute frame, with the field evidence that some speakers anchor their gestures to the world rather than to the body | frames of reference and the direction register stay there; this entry owns only the pointing act and the placement of a hand inside a frame (§4, §5) |
| `semantics-pragmatics.md:115` | deixis as grammar: the deictic centre, and the taxonomy of person, spatial, temporal, discourse and social deixis | deictic words and their grammar stay there; this entry owns only the manual realisation of a deixis (§4) |
| `linguistic-anthropology.md:147` | the coupling of a register to the body: registers license dress and gesture at a speech event | the coupling rule stays there; this entry owns the gesture side of it — what a licensed gesture contributes to the utterance (§6) |
| `politeness-taboo-euphemism.md:76` | the taboo sanction gradient: which institution backs a taboo, from self-enforcing dread to legal censor | the sanction machinery stays there; this entry marks only which gestures a culture bans and who enforces the ban (§8) |
| `../myth-symbol/binding-speech-complex.md:108` | the oath's uptake: who must hear it for it to hold, and the ring that makes the event bodily | the binding channel and its enforcement ledger stay there; this entry owns only the gesture a culture pairs with sworn words, as one licensed gesture among many (§7) |
| `synthesis/symbol-lexicon-colexification.md:141` | the colexification method and its test that a symbol enters a lexicon only when a practice uses the association | the pairing method and its test stay there; this entry supplies only the gesture side of a pairing — which bodily forms a culture can quote at all (§7) |
| `../civilizations/rome.md:43` | the Roman oratorical case: trained speech and controlled gesture as a warrant of civic standing | the Roman evidence and its prescriptions stay there; this entry cites it once, as a trained-gesture example, and claims nothing about Roman oratory |
| `../civilizations/byzantium.md:75` | the term *proskynēsis*, with the reading that a bow does not by itself identify worship | the term and its religious-versus-courtly reading stay there; this entry cites it once, for the calibration that a gesture alone never says what it means (§8) |

```

Line count measured mechanically on the assembled draft (`wc -l /tmp/sec02draft.md` → **18**): H2 (1), blank (2), lead sentence (3), blank (4), table header (5), separator (6), eleven neighbour rows (7–17), trailing blank (18). Row count measured (`grep -c '^| '` → **12**, i.e. header plus 11 neighbour rows).

### Notes for the L1 on this section

- **Row order.** The rows are ordered by distance from C's own ground: the body-code toolkit first, then the register seam with sign languages, then the two measurement systems (counting, frames) and the grammar of deixis, then the coupling and sanction owners, then the binding and symbol owners, then the two historical cases. The order carries no claim.
- **Anchor style.** I used the model entry's convention (`speech-surrogates-whistled-drummed.md:32-47`): bare basename for same-partition files, `../partition/` for cross-partition. `sign-languages-manual-modality.md:37` uses the bare cross-partition form (`adornment-body-codes.md:79`) instead, and the reviewer seat `ReviewPartialOwners.md` §C used the corpus-relative form (`culture-material/adornment-body-codes.md:79`). Both variants exist in the corpus; switching is a mechanical edit if the integrator prefers one. The paths as written resolve correctly **from `corpus/knowledge/linguistics/`**, which is where C's entry sits.
- **Single line per anchor.** Each row carries one backticked `file.md:N` with one line number. Where a neighbour owns a range (the adornment section 7, the direction frames section), the row anchors the single line that carries the ownership claim and names the rest of the range in prose, so no row carries two files or a bare directory.
- **What is deliberately absent.** No row names `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (claim D's file), and no row names `corpus/lessons/round-53.md` — both are on claim C's `must_not_cite` list. No row cites a file outside `corpus/knowledge`.
- **Section references.** `§1, §3, §4, §5, §6, §7, §8, §9` refer to C's planned sections in the wave context (register property; gesture types; pointing; space and time; language shapes gesture; quotable gestures; social control; acquisition). If the integrator renumbers, these are the cells to fix. All are ≤ the planned 14 H2s, so the contract's `§N` ceiling holds.
- **One-way discipline.** Every "What it owns" cell names what the neighbour owns and every "This entry's boundary" cell says what stays there; no cell re-teaches the neighbour's content. The two cells that risk overlap with a sibling's plan are the adornment row (C's §3 and §7 must not re-list the five Ekman–Friesen categories or the bow/wai/kowtow gradient table) and the byzantium row (C's §8 must not re-argue the worship-versus-court reading; it is cited as a calibration).

## 3. Anchors re-read at the lane worktree (2026-10-22), quoted verbatim

Every line below was read from `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/` at the lane worktree. Command used: `sed -n '<N>p' <file>` per row (read-only).

| anchor | quoted line (verbatim) |
|---|---|
| `culture-material/adornment-body-codes.md:79` | "- **The toolkit**: Ekman & Friesen (1969) classify nonverbal behavior into *emblems* (culture-specific gestures with dictionary meanings — the conlang-adjacent category), illustrators, affect displays, regulators, adaptors; Morris et al. (1979) mapped emblem geography across Europe. Hall (1966) named proxemic distance bands (intimate/personal/social/public). These four labels are enough to script any fictional etiquette." |
| `linguistics/sign-languages-manual-modality.md:64` | "\| co-speech gesture (boundary) \| speakers, alongside speech (S079) \| picked up with the spoken language (design frame, **H**) \| every speaker; no community boundary (design frame, **H**) \| conveys information but is not conventionalized and systematic the way sign is (S087); conventional emblems are body code at `adornment-body-codes.md:79` \|" |
| `linguistics/numerals-and-measures.md:107` | "- **Finger counting** is culturally patterned, not universal: direction (left-to-right, right-to-left), start finger, whether the thumb is a counter or a folder, and whether the same gesture is a digit or a word differ across cultures (Bender & Beller 2012 `(to-verify)` on the statistics; Flegg 1983 for the historical finger-arithmetic traditions). A fictional counting gesture system should be specified like any other body code." |
| `myth-symbol/direction-symbolism.md:36` | "  - **Absolute** — fixed bearings regardless of anyone's facing: the cardinal type. Guugu Yimithirr (Cape York, Australia) runs everyday small-scale space on absolute cardinals — a speaker must maintain a running compass fix to say \"move your left foot,\" and gestures are anchored to the world, not the body (Haviland 1993, 1998; Levinson 1997). For such a culture, \"north\" is not a compass abstraction borrowed from navigation; it is a grammatical primitive." |
| `linguistics/semantics-pragmatics.md:115` | "- Bühler (1934): the deictic **origo** — the I-here-now center. Taxonomy (Levinson 1983): person, spatial, temporal, discourse, social deixis. Silverstein (1976): \"shifters\" are where grammar and social structure interlock — a pronoun is a tiny institution. Deixis in practice is culture-saturated (Hanks 1990, Maya)." |
| `linguistics/linguistic-anthropology.md:147` | "7. Couple to costume: registers license dress and gesture (oath regalia, mourning-silence garb, initiate masks); a speech event without costume flags feels unfinished." |
| `linguistics/politeness-taboo-euphemism.md:76` | "- Sanction gradient — a culture exposes which institution backs each taboo: supernatural dread (self-enforcing) → kin/elder ridicule → community reputation → legal censor (obscenity law, blasphemy law, platform moderation). The blasphemy/indecency split is an era marker: religious censorship of oaths (medieval–early modern) gives way to sexual/scatological censorship (industrial–modern), and in-networked regimes to moderation filters." |
| `myth-symbol/binding-speech-complex.md:108` | "\| **Uptake** \| makes the oath an event \| the assembly hears; the people answer *Amen* (Deut 27); the ring is reddened (`../culture-material/adornment-body-codes.md:17`) \| who must hear it for it to hold — a god, a crowd, a record? \|" |
| `synthesis/symbol-lexicon-colexification.md:141` | "6. Add a symbol only when a practice uses the association: a motif, oath gesture, ritual material, or naming formula. Record interpreters, occasion, and the reading's competitors." |
| `civilizations/rome.md:43` | "\| Rhetorical/educated \| Cicero; Quintilian; grammatical commentary \| trained speech and controlled gesture authorize civic standing \| prescriptions and self-presentation, not a population recording \|" |
| `civilizations/byzantium.md:75` | "\| **proskynēsis** \| Reverence, obeisance; meaning depends on recipient and context \| Bowing can belong to religious veneration or courtly respect; gesture alone does not identify worship. [J; C] \|" |

All eleven files exist at the lane worktree; existence was checked with `test -f corpus/knowledge/<path>` per row (11/11 OK). No file in the table is a duplicate of another row's file, so the "one distinct in-corpus neighbour per row" rule holds.

## 4. Neighbour set and how it was chosen

Starting from the partial owners named in the wave context, then grepping `corpus/knowledge` for `gestur`, `pointing`, `kinesic`, `emblem`, `nod`, `bow`, `proskyn`, `mudra`, `hand`:

| wave-context partial owner | anchor used | in the table |
|---|---|---|
| `culture-material/adornment-body-codes.md:77-93` (emblem taxonomy, Morris geography, Hall proxemics, bow/wai gradients, nod/shake inversion, finger counting) | `:79` | row 1 |
| `linguistics/sign-languages-manual-modality.md:64` and `:161` (co-speech gesture as the manual modality's boundary row) | `:64` | row 2 |
| `linguistics/numerals-and-measures.md:107` (finger counting) | `:107` | row 3 |
| `myth-symbol/direction-symbolism.md:6` and `:36` (Guugu Yimithirr, Haviland 1993 on pointing) | `:36` | row 4 |

Added by grep, each because a planned C section would otherwise restate it: `semantics-pragmatics.md:115` (deixis grammar, §4/§5); `linguistic-anthropology.md:147` (register–costume–gesture coupling, §6); `politeness-taboo-euphemism.md:76` (taboo sanction gradient, §8); `binding-speech-complex.md:108` (oath uptake and the bodily ring, §7); `symbol-lexicon-colexification.md:141` (a symbol needs a practice behind it, §7); `rome.md:43` (orators' controlled gesture, §1/§8); `byzantium.md:75` (*proskynēsis*, gesture alone does not identify worship, §8).

The `sign-languages-manual-modality.md:161` sentence ("Sign is not gesture-code: emblems and proxemics stay at `adornment-body-codes.md:79`") and `direction-symbolism.md:6` (the Haviland pointing-gesture citation) were read and are **not** used as anchors: row 1 and row 4 already carry the ownership each of them routes. Adding them would have produced two rows for the same file, which the assignment's "one distinct in-corpus neighbour per row" rule forbids.

## 5. Conflicts with sibling advice, reported verbatim for the canonical judge

**C1 — sibling-lane rows versus in-corpus rows.** `ConnectSiblingGesture.md` §"Proposed move" proposes that C's section 2 be "one boundary table with two blocks" and gives draft rows for lore-shokunin and game-dev-2d/3d, e.g. "| world-specific gesture canon on landed entities | lore-shokunin (world bible; intake via `../synthesis/worldbible-integration-contract.md`) | designs and hands off; never records canon |". My assignment says the table's rows are "one distinct **in-corpus** neighbour per row", so no sibling-lane row is in my draft. Recommendation to the integrator: place the lore canon row and the animation-runtime row in C's Scope / handoff paragraph (where the contract puts the `Handoff: lore-shokunin owns …` sentence) rather than in the boundary table, or widen the table's remit explicitly. I am not making that change.

**C2 — anchor path style.** Three corpus conventions are in play: the model entry `speech-surrogates-whistled-drummed.md:32-47` uses bare basenames for same-partition and `../partition/` for cross-partition; `sign-languages-manual-modality.md:37` uses a bare cross-partition basename; `ReviewPartialOwners.md` §C uses corpus-relative `culture-material/…`. My draft uses the model entry's convention because C's entry sits in the same partition as that model. This is a style choice for the integrator to confirm, not a defect.

**C3 — the emblem split.** `ConnectSiblingGesture.md` §"Second-order effect" warns that C's planned §7 ("quotable gestures and emblem repertoires") duplicates `adornment-body-codes.md:79` and `:92`, and that "C needs an explicit split: adornment owns the inventory and failure modes, and C owns quotability (how an emblem is lexicalized, cited and coined in a conlang)", or else "the integrator should amend :161 in the same change". My row 1 already performs the split in the boundary table (the category names, emblem geography, proxemic bands and etiquette script stay at `adornment-body-codes.md:79`; C owns the co-speech relation and how a quotable gesture is learned) and row 9 assigns the pairing test to `symbol-lexicon-colexification.md:141`. This keeps `sign-languages-manual-modality.md:161` true without editing it — no amendment needed on the evidence of the boundary table alone. C's §7 body still has to avoid re-listing the five categories or the bow/wai/kowtow table; that is the §7 scribe's line, not mine.

## 6. Unrun checks and limits

- **No lane gate was run**: `reports/round-28/readme/sweep.py`, `tools/check-readme-heading.py`, `tools/check-readme-revisions.py`, `tools/gates/provenance-audit.py`, `tools/harness/basename-couples-resolver.py`, `reports/round-53/accept-c.py` and `reports/round-53/d-count.py` were not executed. This seat wrote no entry file, no README row and no SOURCES row, so the acceptance counters are the integrator's.
- The contract checklist was applied by hand to the draft (H2 numbered and matching C's plan, zero H3, pipe table with a separator row, blank line before and after, no forbidden placeholder word, no `§N` above the planned H2 count, no canon claim, no emoji). No Markdown linter or LSP answers Markdown in this repo, so these are manual readings, not tool verdicts.
- **Line and row counts were measured**, not estimated: `wc -l` → 18; `grep -c '^| '` → 12 (header + 11 rows).
- **No external source was opened.** Every anchor is in-corpus. The S187+ rows C's other sections cite are the drafting seats' work and are not judged here.
- **Not read:** `corpus/lessons/round-53.md`; the round-53 claim counters' internals beyond `claims.json`; sibling section drafts other than `ScribeSec04Pointing.md`, `ScoutGapGesture.md`, `ConnectSiblingGesture.md` and `ReviewPartialOwners.md`, which I used only to check for conflicts with my neighbour set.
- **Not claimed:** that the eleven neighbours are the complete set of in-corpus gesture-adjacent owners. The set is the union of the wave context's partial owners, the neighbours named in my assignment, and the grep hits that a planned C section would otherwise restate; a further sweep may add rows.

## 7. Tooling record

- **No installs, no updates.** Nothing was installed: no `pacman`, `uv tool`, `cargo` or `npm` transaction was run, no host service was restarted, and no tool was downgraded. The tooling directive's channel order was not needed for a read-only drafting seat.
- Commands used, all read-only and inside the lane or `/tmp`: `git rev-parse HEAD`, `git log --oneline -1`, `git status --porcelain`, `find corpus/knowledge -name '*.md' | wc -l`, `find corpus/knowledge -iname '*gestur*' -o -iname '*pointing*' -o -iname '*kinesic*'`, `sed -n '<N>p' <file>` for each anchor, `test -f` for each neighbour file, `wc -l` and `grep -c` on the scratch draft; the `read` and `grep` tools for corpus searches. No `jj` command was run at the fleet root or in the lane; no git mutating command was run anywhere.
- Scratch file: `/tmp/sec02draft.md` only, outside the lane.
