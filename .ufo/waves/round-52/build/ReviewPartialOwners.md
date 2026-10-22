# ReviewPartialOwners — Claim C no-restatement guard (round 52, 2026-10-22)

Assigned item: read each partial-owner line in full context, quote what it already says, and give the one-way pointer the C entry (`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`) should use instead of repeating it; plus a verdict on `sound-symbolism.md:19`'s claim that `phonetics-phonology.md` §7 "owns whistled/drum channels".

Evidence method: every location re-read at the lane worktree today by ranged `read` + `grep -n` pinning; quotes verbatim. No LSP server applies to this prose corpus, so semantic verification is by direct full-context read (the ground truth for a restatement analysis). The C entry does not exist yet (`glob speech-surrogates*.md` → no files), so all pointers are recommendations to the L1's draft, not checks of landed text. No owner file was edited (none is in C's declared lands).

## 1. `corpus/knowledge/linguistics/phonetics-phonology.md` — §7 "Environment, anatomy, society → inventory (calibrated)" (heading :194)

Already says (grep-pinned):
- :197-198 — "Whistled speech: mountains + long-distance herding → whistled registers (Silbo Gomero, Kuşköy, Chinantec; Meyer 2008)."
- :199-200 — "Drum language: tone + gongs → tone-and-rhythm coding of set phrases (Kele/Congo; Carrington 1949); needs tonal lexicon + redundancy."
- :201-203 — sign-language phonology bullet (adjacent; that is D's territory, not C's — C must not touch or lean on it).

Owns: the *registration* of the two canonical couplings inside a calibrated ecology→inventory section — three lines each, no encoding, ambiguity, social-control or transmission content. The `:305-312` range assigned is the errata block; its surrogate-relevant entry is "Silbo Gomero whistled register (UNESCO element record)" listed under "Rechecked with no change found" (`:310` area) — a freshness receipt, not surrogate content; nothing for C to restate there, but it does mean the §7 whistled line has a live-recheck receipt behind it.

One-way pointers for C:
- §4 (whistled): "The ecological trigger — mountains + long-distance herding → whistled registers (Silbo Gomero, Kuşköy, Chinantec; Meyer 2008) — is registered at `linguistics/phonetics-phonology.md:197-198`; this entry takes the coupling as given and does not re-derive it."
- §5 (drummed): "The tone-plus-gongs coupling and its redundancy requirement (Kele/Congo; Carrington 1949) are registered at `linguistics/phonetics-phonology.md:199-200`; §6 builds the encoding analysis on that base."

Note: `reports/round-52/claims.json` gap-evidence cites this owner as `:197-199`, but the drum bullet wraps through `:200`. Cosmetic only — no counting command depends on it — but the L1 may want the prose corrected to `:197-200`.

## 2. `corpus/knowledge/culture-material/music-instrument-lexicon.md` — §6 "Music–myth links" (heading :81)

Already says:
- :98 (table row) — "| instruments that speak | Yoruba dùndún 'talking drum' mimics lexical tone; Akan atumpan; Lokele drum-speech documented | Carrington (1949); Finnegan (1970) |"
- :100 — "**The talking drum is this lane's centerpiece coupling**: a tone language can be *literally spoken* on a drum — phonological encoding on a musical instrument (cf. phonetics-phonology.md). Drum and whistle speech are language phenomena, not merely music phenomena."

Owns: the instrument-side roster and the jurisdictional claim (these are language phenomena, not music phenomena). `:101` is the inventor-hero design lever — myth-facing, not a surrogate restatement risk.

One-way pointer for C (§2 boundary and §3 typology): "Which instruments carry speech (dùndún, atumpan, Lokele) is tabled at `culture-material/music-instrument-lexicon.md:98`, and the jurisdictional claim — drum and whistle speech are language phenomena, not music phenomena — stands at `:100`; this entry adopts both rather than re-arguing them."

Hotspot: C's §3 typology must classify by *encoding strategy* (tone, formula, rhythm, redundancy), NOT re-tabulate speaking instruments — the instrument list is already owned at `:98`.

## 3. `corpus/knowledge/linguistics/orality-formulaic-language.md` — §8 "Designing an oral-formulaic register" (heading :109)

Already says:
- :114 — "12. Media extensions: tonal languages can ride drums (African talking drums; Carrington 1949) and whistled registers (Busnel & Classe 1976) — a 'broadcast layer' for the same formulas."
- :124 (meter decision-table row) — "| lexical tone | tonal counterpoint; drum/whistle speech | Yoruba dùndún (Carrington 1949) |"

Owns: the formula/register side — surrogacy as a broadcast layer for the *same formulas*, and the verse-engine coupling for lexical tone.

One-way pointers for C (§6/§7): "That formulas ride a drum/whistle broadcast layer (Carrington 1949; Busnel & Classe 1976) is owned at `linguistics/orality-formulaic-language.md:114`, and the lexical-tone verse engine at `:124`; this entry treats the channels, not the formulas they carry — repertoire, meter and formula-repetition questions stay with the orality entry."

Hotspot: C's planned §7 (ecology and function) must not absorb the "broadcast layer for the same formulas" argument; cite `:114` instead.

## 4. `corpus/knowledge/linguistics/sound-symbolism.md`

Already says:
- :19 (couples line) — "`phonetics-phonology.md` — its §8 is the compressed parent of this entry and its §7 owns whistled/drum channels" (the same line routes "drum/whistle speech as phonological encoding" to `music-instrument-lexicon.md`).
- :121 (§7 hook table, row "music") — "| music | tone-language drum/whistle speech — phonological encoding on instruments | `culture-material/music-instrument-lexicon.md`; `phonetics-phonology.md` §7 |"

Owns: pure cross-file routing — it carries no surrogate facts of its own. C needs no content pointer here beyond listing these rows among the owners in its boundary table; C must not treat `:19` as a source for any surrogate claim (it is a couples line, not a claim).

## 5. Verdict: is `sound-symbolism.md:19`'s "§7 owns whistled/drum channels" accurate?

Accurate, with two qualifications:

1. **Accurate as a locator.** `phonetics-phonology.md` §7 (heading :194) does host the whistled (:197-198) and drum (:199-200) bullets under "Solid couplings", and `sound-symbolism.md:121` routes to the same target consistently. Nothing is misdescribed.
2. **"Owns" overstates depth.** §7 registers each coupling in one wrapped bullet inside an ecology→inventory section; it has no encoding, ambiguity, social-control, or transmission treatment. Registration-level ownership only — exactly the "partial owner, one to three lines" status the claim records.

**How C's boundary should treat it:** split ownership by aspect, do not contradict the wording. C owns speech surrogacy *as method* (typology incl. horns/reed pipes/jaw harps/xylophones/gongs, encoding and ambiguity, ecology and function detail, who may speak, transmission/perception, signal-code boundary); §7 keeps the registered ecological couplings; `sound-symbolism.md:19/:121` keep their routing rows. Because C's lands are only the new entry + `corpus/README.md` + `corpus/SOURCES.md`, no owner file is edited this round and both `:19` and `:121` stay valid as written. If a later sweep wants `:19`'s "owns" re-pointed to the C entry, that is out of C's declared lands — record it, do not edit.

## 6. Civilization entries (assigned greps; not on the partial-owner list, but the deepest restatement risk)

### `civilizations/yoruba.md` — § "Drum speech: do not conflate a channel with a story genre" (heading :41)
- :42 — terminology gate: "àlọ́" is a riddle/folktale genre term, not an attested name for drum speech.
- :43 — Durojaye et al. 2021 mode labels: direct drum talking (DT-D), performative drum talking (DT-P), drum singing (DS), drum–dance rhythm (D-DR); assignment spelling "àló" flagged unverified.
- :44 — "Established mechanism: the tension-adjustable dùndún can reproduce relative pitch contours and timing associated with speech; its sound is not a recording of consonants and vowels."
- :45 — cord-tension direction; glides/embellishment, "rather than three mechanically fixed musical notes".
- :46 — "Interpretation constraint: many verbal strings share a tonal melody… do not model it as universally intelligible Morse code."
- :47 — Abiodun 2014 p. xxi: one-to-many mappings; phonological resemblance alone does not identify the sentence.
- :49-54 — analytical-category table (DT-D/DT-P/DS/D-DR × design questions; :54 "When must an observer stop claiming that every beat 'says' something?").
- :56 — calibration (small set of experienced male performers; no population-wide comprehension, no ancient date per mode).
- :57 — dùndún ≠ bàtá; Villepastour 2010 located-not-inspected, (to-verify).
- :58 — coupling chain: "tonal language → recognized phrase → drum repertoire → public identification/praise → patron or ritual occasion; instrument, performer, audience, and permission all matter."

This is the deepest in-corpus surrogate treatment anywhere in the corpus — deeper than the four listed partial owners. Pointer for C (§5/§6/§8): "The culture-specific dùndún evidence — mode taxonomy, mechanism, ambiguity constraints, calibration, and the coupling chain — is owned at `civilizations/yoruba.md:41-58`; this entry cites it as the worked exemplar of surrogate-mode analysis and does not re-tabulate it." C's §6 (encoding and ambiguity) and §8 (who may speak) overlap `:46-47` and `:58`'s "permission" clause most heavily; social-control content must come from C's own S134+ rows with `:58` cited, not re-derived.

### `civilizations/akan.md`
- :58 — "R23 ch. XXII records drum-language texts and explanations. A tonal speech-surrogate reference is useful, but drum or horn pitch alone is not a lossless transcription of ordinary Twi — the atumpan pair encodes only H and L (downstepped H is played as plain H), and tone/note mismatches appear elsewhere in the surrogate set [MO] — so verify a particular drum repertoire before reconstructing it." (:57, "Couple sound to social life through learnable practices… not through claims that tonal languages inherently create mystical speakers", is the guard against a mystical-speaker claim.)

Owns: the encoding-ceiling fact and the lossless-transcription caveat for Akan/horn. Pointer for C (§6): "The atumpan two-tone ceiling — H and L only, downstepped H played plain — and its verify-the-repertoire caveat are owned at `civilizations/akan.md:58`; §6's encoding-ceiling row cites it instead of repeating the H/L analysis."

### `civilizations/fon-dahomey.md` — § "Drum speech and the requested 'gun-gun' label" (heading :31)
- :32 — "gun-gun" as a specifically Fon talking-drum designation remains `(to-verify)`; :33 — do not equate with Gun/Gungbe or Yoruba gángan/dùndún; :34 — Durojaye 2021 is "Yoruba evidence, not a Fon experiment"; :35 — Finnegan caveat, no transplanting one community's drum vocabulary.
- :37-42 — four-row table: Speech surrogacy / Conventional signal / Ritual or dance music / Royal praise performance, each with "verification needed before calling it Fon practice" (:39 speech surrogacy, :40 conventional signal).
- :44 — "a fictional drum code should specify what is preserved, what is lost, who learns it, and how listeners resolve ambiguity. Tone without consonants and vowels is not automatically a lossless message channel."
- :45 — prototype-with-synthetic-language procedure; :46 — do-not-invent list (no Fon drum score, no universal cipher, no fixed distance, no "gun-gun" rank).
- :162 — build-order item: "Decide whether an instrument conveys lexical surrogacy, conventional signals, musical accompaniment, or several separately learned modes; mark this as a design choice, not Fon evidence."
- :181-182 — the entry's own Finnegan and Durojaye source rows.

Owns: exactly C's planned §3 signal-code boundary, at Fon scope (surrogacy vs conventional signal vs music vs praise), plus the ambiguity checklist at `:44`. Pointers for C: "The conventional-signal vs speech-surrogacy distinction is tabled at `civilizations/fon-dahomey.md:37-42`, and the preserve/lost/who-learns/ambiguity checklist at `:44`; §3 cites these instead of restating them, and the 'gun-gun' non-identification (`:32-33`) stays theirs." :162 is a second hotspot — C's §10 decision table should cite `:162` rather than rebuild the same four-way design choice.

## 7. Ready-to-paste block for C's §2 (one-owner boundary)

> **Ownership and one-way citations.** Speech surrogacy is owned here as *method*: channel typology (whistle, drum, horn, reed pipe, xylophone, jaw harp, gong), encoding and ambiguity, ecology and function, speaker licensing, transmission and decline, and the boundary with signal codes. Four knowledge entries partially own adjacent registrations and are cited one-way, not restated: the ecological couplings at `linguistics/phonetics-phonology.md:197-200`; the speaking-instrument roster and the language-not-music jurisdictional claim at `culture-material/music-instrument-lexicon.md:98,:100`; the formula broadcast layer and lexical-tone verse engine at `linguistics/orality-formulaic-language.md:114,:124`; and the routing rows at `linguistics/sound-symbolism.md:19,:121`. Culture-specific evidence is cited where it lives: dùndún mode taxonomy and ambiguity at `civilizations/yoruba.md:41-58`; the atumpan H/L ceiling at `civilizations/akan.md:58`; the Fon signal-type table and `gun-gun` non-identification at `civilizations/fon-dahomey.md:31-46,:162`. No fact established in those entries is re-derived here.

Cross-cutting guard for the L1: "cited one-way" can only mean C → owner citations this round, since C's lands exclude the owner files; any owner-file back-pointer is a later sweep's business. Highest-restatement sections are C §6 (vs `yoruba.md:46-47`, `fon-dahomey.md:44`, `akan.md:58`) and C §8 (vs `yoruba.md:58`'s permission clause).

## Residual risk and verification gaps

- `claims.json` gap-evidence span `phonetics-phonology.md:197-199` vs actual bullets `:197-200` (wrap line) — cosmetic, no counter depends on it.
- The C entry did not exist at review time (glob → no files), so pointers are untested against real draft text; the L1 should re-run this guard on the draft before integration.
- `music-instrument-lexicon.md` sources for Carrington 1949 / Finnegan 1970 (:98) were not opened this session by this seat; whether C needs its own S134+ rows for any source it quotes first-hand is the source seats' scope. Nothing here licenses C to lean on those rows as support — they belong to the owners.
- No files edited; no counting commands run (none assigned).
