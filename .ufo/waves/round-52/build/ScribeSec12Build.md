# ScribeSec12Build — report

- Seat: KotodamaR52.ScribeSec12Build (leaf, no delegation).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (branch main). Read-only; no lane file
  edited, staged or committed. The only file written is this report.
- Assigned item: Claim C — Section `## 12. Decision table and build order` (budget 24 lines) for
  `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`.

## Numbering note (author-lane advice)

The seat prompt says Section `## 10. Decision table and build order`, but the planned section list
in the wave context (1–16) places "decision table and build order" at 12: 10 = decline and revival
(peer seat ScribeSec10Decline), 11 = perception and learning, 12 = decision table and build order,
13 = NON-CANON example, 14 = calibration bank. The draft below uses `## 12.` to stay consistent
with the 1–16 plan and the sibling seats. If the L1 keeps a different numbering, only the H2
number changes; body and tables are unchanged.

## Verified facts (lane worktree, re-read this session)

- `DR-SRG` prefix is unused in corpus and reports: `grep -rn "DR-SRG" corpus reports` → 0 hits.
  The only matches in the repo are the build-spec files themselves
  (`.ufo/waves/round-52/build-spec.json`, `gen-build-spec.py`, `build-dispatch.json`), which are
  not corpus/reports content.
- Partial owners re-read, pointed to one-way, never restated:
  - `phonetics-phonology.md:197-199` — whistled/drum channel couplings (tone→drum, long-distance→whistle).
  - `music-instrument-lexicon.md:98-100` — "instruments that speak" row and talking-drum centerpiece.
  - `orality-formulaic-language.md:114` — media extensions: drums/whistles as a broadcast layer;
    `:124` — lexical-tone meter row.
  - `sound-symbolism.md:121` — music row pointing to `music-instrument-lexicon.md` and `phonetics-phonology.md`.
- Model shape copied from `sign-languages-manual-modality.md:163-188` (decision table → numbered
  build order with `*Artifact: …*` → decision record table) and `pastoralism-animal-husbandry.md:162-181`.

## Opened sources (ordinary means, direct HTTP 200; no browser, no bot past)

1. Seifart, Meyer, Grawunder & Dentel 2018, "Reducing language to rhythm: Amazonian Bora drummed
   language exploits speech rhythm for long-distance communication", Royal Society Open Science 5:170354,
   doi 10.1098/rsos.170354. Route: direct PMC full text (https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/),
   HTTP 200. Tier A for drummed-speech encoding and reach. Quote (Abstract, sentence 1, 22 words):
   "Many drum communication systems around the world transmit information by emulating tonal and
   rhythmic patterns of spoken languages in sequences of drumbeats."
2. Meyer & Moore 2021, "A Flute, Musical Bows and Bamboo Clarinets that 'Speak' in the Amazon
   Rainforest; Speech and Music in the Gavião Language of Rondônia", Frontiers in Psychology 12:674289,
   doi 10.3389/fpsyg.2021.674289. Route: direct PMC full text (https://pmc.ncbi.nlm.nih.gov/articles/PMC8724528/),
   HTTP 200. Tier A for instrument-borne speech beyond drums. Quote (Abstract, sentence 1, 21 words):
   "The Gavião, a native Amazonian group in Rondônia, Brazil, use three different traditional musical
   instruments that they identify as "speaking" ones"
- Unopened, recorded as such: Stern 1957 "Drum and Whistle Languages" (Wiley AnthroSource HTTP 403
  Cloudflare challenge; JSTOR client challenge) — not cited, not cited as opened. UNESCO ICH element
  pages (https://ich.unesco.org/en/RL/silbo-gomero-00168 and whistled-language-of-turkey-01255) serve a
  human-verification captcha to the read tool and return a generic shell to plain curl; Wayback has no
  capture of either URL — recorded unopened, not cited here (the decline/revival seat handles those).

### Registry row drafts (11 columns, to be assigned S134+ by the L1)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-ScribeSec12Build-1 | Seifart et al. 2018, Royal Society Open Science 5:170354, doi 10.1098/rsos.170354 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ | paper | A | drummed-speech encoding, rhythm units, reach | Abstract, sentence 1 | drum speech emulates tonal and rhythmic patterns of a spoken language; reach up to ~100× voice | queued | 2026-10-22 | 365d | — |
| NEW-ScribeSec12Build-2 | Meyer and Moore 2021, Frontiers in Psychology 12:674289, doi 10.3389/fpsyg.2021.674289 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8724528/ | paper | A | instrument-borne speech beyond drums | Abstract, sentence 1 | the Gavião identify flute, mouth bows and bamboo clarinets as "speaking" instruments with a tight music-lyric pitch relation | queued | 2026-10-22 | 365d | — |

### Gate lines (for the round lesson)

- `- NEW-ScribeSec12Build-1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ — accessed 2026-10-22 — Abstract, sentence 1: "Many drum communication systems around the world transmit information by emulating tonal and rhythmic patterns of spoken languages in sequences of drumbeats." Grounds: open full text of the Royal Society Open Science article; supports drummed-speech encoding and reach checks in section 12.`
- `- NEW-ScribeSec12Build-2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8724528/ — accessed 2026-10-22 — Abstract, sentence 1: "The Gavião, a native Amazonian group in Rondônia, Brazil, use three different traditional musical instruments that they identify as "speaking" ones" Grounds: open full text in Frontiers in Psychology; supports instrument-borne speech beyond drums (flute, mouth bows, bamboo clarinets).`

## Drafted section text (24 lines, paste-ready; H2 number per the 1–16 plan)

```
## 12. Decision table and build order

| If your culture… | then the surrogate needs… | and check |
|---|---|---|
| speaks a tonal language | the tones ride the instrument: choose what holds pitch and length | §5; `phonetics-phonology.md:197-199` |
| speaks a non-tonal language | a whistle register planned around vowels and pitch — see §4 for what survives | §4; `phonetics-phonology.md:197-199` |
| has a fixed set of ritual or military messages | a signal code, not a surrogate — fixed signs, no syntax | §6; `music-instrument-lexicon.md:98-100` |
| keeps a formula-backed oral canon | your formula inventory is the stock-phrase list the channel can carry | §7; `orality-formulaic-language.md:114` |
| herds or hunts beyond earshot | a channel whose reach matches the travel time — plus a repair convention | §8; `phonetics-phonology.md:197-199` |
| treats speech as an office — drums as hereditary | gate who may play before the instrument is designed | §9; `music-instrument-lexicon.md:98-100` |

1. Fix the language's tone and stress inventory first (`phonetics-phonology.md:197-199`) — every channel choice hangs off it. *Artifact: tone-and-rhythm chart.*
2. Choose the channel and measure what it can carry: pitch set, rhythm units, reach (NEW-1). *Artifact: channel-capacity sheet.*
3. Pick the message domain and reuse your formula bank as stock phrases; decide how ambiguity is repaired (`orality-formulaic-language.md:114`). *Artifact: stock-phrase list with repair rules.*
4. Name the instruments and the players; write who may use the channel (`music-instrument-lexicon.md:98-100`). *Artifact: instrument roster and speaker office.*
5. Test one full message end-to-end against the §14 calibration bank before expanding the vocabulary. *Artifact: one verified message and its gloss.*

| ID | Decision | Trigger | Failure if skipped |
|---|---|---|---|
| DR-SRG-01 | Decide surrogate vs signal code before any phonology | the culture's message set is fixed and finite | a closed set taught as a language — the §6 error |
| DR-SRG-02 | Set the tone and rhythm inventory before choosing the channel | the language's tone inventory is settled | an instrument register that cannot carry the contrasts you chose |
| DR-SRG-03 | Reuse the existing formula bank as the stock-phrase core | the oral canon already supplies formulas | coining channel-only phrases no listener knows |
| DR-SRG-04 | Gate who may use the channel before naming the instrument | the office (court, guild, gender rule) is already defined | a free-for-all channel that breaks the office premise |
| DR-SRG-05 | Write the decline trigger into the fiction (roads, phones, school shift) | the culture's history includes contact change | a timeless channel with no loss driver — a static portrait |
```

Line count: 24 exactly (1 H2, 1 blank, 3 table lines + 6 rows, 1 blank, 5 build steps, 1 blank,
3 table lines + 5 rows). All pipe tables have a blank line before and after and a `|---|` separator.
Every factual claim cites an in-corpus `path:line`, a NEW-id, or points to an entry section (§4–§9,
§14); no real-world claim without a source. Build steps each end with `*Artifact: …*`.
Decision record IDs run DR-SRG-01…05 (prefix confirmed unused). No placeholder words, no emoji,
no heritage-policy or legal rulings, no exoticizing language, no partial-owner restatement.

## Result

Drafted section delivered above, within the 24-line budget, with two opened primary sources drafted
into registry rows and Gate lines. Line count verified by structure; not re-run through the entry's
acceptance gates (those belong to the integrator).

## Unrun checks

- The entry's full acceptance gates (sweep, provenance audit, couples resolver, S-ids, length) are
  the L1's; not run here.
- No verification of sibling sections' text; §-references in the draft assume the planned 1–16 H2
  order. Anything else the indent: the H2 number conflict noted at the top.

## Tooling record

- No installs; no tools updated. Only plain `curl` (system), Python stdlib for text extraction
  (read-only, /tmp), and read-only lane commands.
