# ConnectSiblingSurrogate — claim C sibling overlap (round 52)

Seat `KotodamaR52.ConnectSiblingSurrogate`, connector, read-only. Accessed 2026-10-22. Lane read at `dea5ece63ca4372c41766ab242df1e26c2e6898a`.

## Result

No sibling lane owns any part of claim C's ground, not even partly. I scanned 20 sibling lanes (every `/home/vgpnk/Projects/shokunin/*-shokunin` except kotodama), covering each lane's `corpus/knowledge/`, `PROVINCE.md` and `SKILL.md` where present (audio, game-dev-2d and revenger have no `SKILL.md`). The search covered whistled speech, drum languages, speech surrogates, signal codes, acoustic long-distance communication and music-as-language. Every hit is a false positive (the same word used in an unrelated sense) or a passing mention. Claim C, `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`, takes no sibling's province. This agrees with the claim's own gap evidence (`reports/round-52/claims.json:37`, "the same topic grep over the sibling lanes' corpus/knowledge -> 0 files").

There is one boundary the integrator should know about. It is a risk, not a current conflict: **audio-shokunin** owns making in-game sound. If the entry gives recipes for producing whistled or drummed audio assets, it would step into audio's work. Details under "Contested scope".

## Axes

- Coverage (judged). The move below improves it by making the handoff clean, without adding scope.
- Separability of D and C. Not affected: nothing here touches the sign-language entry.
- Province hygiene. Improved: the boundary is named instead of being left implicit.

## Hits

Search 1 used a narrow pattern: whistl, surrogat, talking drum, drum language/speech/signal, Silbo, Kuşköy, bird language, signal code, semaphore, Morse, heliograph, smoke signal, yodel, long-distance or acoustic signal/communication, music-as-language, Solresol, jaw harp, slit drum, horn/gong signal, xylophone, reed pipe, instrument-borne, tone language, lexical tone, sound symbolism. Search 2 was broader: drum, horn, gong, flute, conlang, telegraph, leitmotif, beacon, prosody, intonation, speech.

| path:line | text sense | class |
|---|---|---|
| `revenger-shokunin/corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md:1,3,9` (+14 more lines) | Unicode UTF-16 surrogate code units | false positive (not speech surrogates) |
| `revenger-shokunin/corpus/knowledge/pe-resource-directory-layout.md:62,161` | UTF-16 surrogate pair | false positive |
| `tameshi-shokunin/corpus/knowledge/replay-projection-hardening.md:85` | "lone-surrogate stream" (UTF-16) | false positive |
| `kumitate-shokunin/corpus/knowledge/native-admission-detail.md:89` | cut splitting a UTF-16 surrogate | false positive |
| `kama-shokunin/SKILL.md:802` | Python `surrogateescape` | false positive |
| `kumitate-shokunin/corpus/knowledge/omp-task-contract.md:80` | concurrency semaphore | false positive |
| `kotoba-shokunin/corpus/knowledge/harness-verifier-round10.md:197` | concurrency semaphore | false positive |
| `audio-shokunin/corpus/knowledge/seed.md:26` | "layered stems (base/drum/lead)" — drum as a soundtrack stem | mention (music production, not drum speech) |
| `audio-shokunin/corpus/knowledge/2026-10-13-sox-act-autodetect-predicate.md:38` | "speech compression" codec | mention (codec) |
| `kake-shokunin/corpus/knowledge/accessibility-review-cards.json:442` | speech-input accessibility | false positive |
| `kengaku-shokunin/corpus/knowledge/eval-theory-notes.md:74` | speech recognition benchmark | false positive |
| `tabi-shokunin/corpus/knowledge/external-class-fixture-v2.md:560` (and 3 similar), `tabi-shokunin/SKILL.md:1891` | HTTP beacon requests | false positive |

Outside the declared scan scope (whole sibling repos minus `.git`, narrow pattern), the only hits are 12 files under `souji-shokunin/census/round-6/` (for example `seat-76.json`). They are disk-census file listings of kotodama clone paths such as `.../linguistics/conlang-methodology.md`: mentions of kotodama files, not ownership.

Sibling commits read: audio `7a2fcd4f`, lore `380ef3ab`, tabi `e3cf4e0d`, chousa `6c5eb146`, game-dev-2d `7753d49b`, game-dev-3d `89dd182b`, souji `4edb25df`.

## Province-level boundaries (no hit, but next to C)

| sibling clause | what it owns | overlap with C |
|---|---|---|
| `audio-shokunin/PROVINCE.md:3-5`, `:25` | "game audio production — SFX ... and soundtrack (motifs, loops, stems, adaptive layers)"; "original SFX, ambience, soundtrack motif/loop/stem/layer audio content" | **Nearest boundary.** C owns the language design (how a register maps tone or formants onto a channel). Producing an actual whistled or drummed sound asset, or measuring it, is audio's work. No overlap today. |
| `audio-shokunin/PROVINCE.md:13-15` | refuses narrative canon (lore) and game mechanics (game-dev-2d) | Same refusals as kotodama (`PROVINCE.md:16-20`). Consistent. |
| `lore-shokunin/PROVINCE.md:3`, `:28` | world records; "Kotodama also owns name generation ... lore owns the names and dates recorded on landed entities" | No overlap. The entry contract already requires `Handoff: lore-shokunin owns …` (`.ufo/waves/round-50/build/ReviewEntryContract.md:69`). |
| `game-dev-2d-shokunin/PROVINCE.md:3`, `:17`; `game-dev-3d-shokunin/PROVINCE.md` Owns | headless game fixtures, including Godot audio playback | Only if C framed a drum or horn relay as a game mechanic. Kotodama already refuses game mechanics (`kotodama-shokunin/PROVINCE.md:18-19`). |
| `chousa-shokunin/PROVINCE.md` Owns | source hierarchy and claim-vs-source checking | Not C's topic. Relevant only to the frontier step (see the side finding). |

## Contested scope for the integrator (named, not absorbed)

1. **The instrument-borne half of C sits next to audio-shokunin.** Evidence: kotodama's Refuses list (`kotodama-shokunin/PROVINCE.md:16-20`) names lore, game-dev-2d/3d, chousa, kake and kotoba, but **not audio**. Running `rg 'audio-shokunin' kotodama-shokunin/corpus/knowledge` finds 0 lines. C is the first kotodama entry whose subject is sound made on instruments (§3 typology, §5 drummed speech, §6 encoding). The risky sections are §10 decision table and build order, and §11 the worked example. If either gives sound-asset specifications (synthesis frequencies, loudness, stem or loop layout), the entry is doing audio's work.
2. **Music-as-language stays split inside the lane, not across lanes.** `culture-material/music-instrument-lexicon.md:98-100` already calls the talking drum "a language phenomenon, not merely a music phenomenon". C must cite that line one-way and not restate it, as the claim's falsifier requires (`claims.json:46`). No sibling owns music-as-language.

## Proposed move (one, bounded)

C's `- scope:` head line (field 8) and its §14 Scope paragraph should include a second, one-way handoff next to the required lore handoff. Draft text, ready to paste:

> It decides nothing about sound assets: producing, synthesizing or measuring a whistled, drummed or horn signal as game audio belongs to audio-shokunin (`audio-shokunin/PROVINCE.md:3-5`); signal relays as game mechanics belong to game-dev-2d/3d. Handoff: lore-shokunin owns any surrogate register recorded as canon.

Why this helps: it closes the only real sibling boundary in C's topic, at almost no cost (one sentence in fields that already exist), and it creates no ownership. Both model entries already end their scope lines with a "hands … to" clause (`sign-languages-manual-modality.md:12`, `pastoralism-animal-husbandry.md:12`), so this follows the existing pattern.

Risks:
- The contract check requires the exact scope key and the `Handoff: lore-shokunin` string (`ReviewEntryContract.md:55`, `:69`). The extra sentence must not replace it; it goes before it, as drafted.
- The draft cites a sibling path. [INFERENCE, not checked] Lane `path:line` checks may not resolve fleet-root paths. If the integrator's checker only resolves lane-relative paths, drop the parenthetical and keep the plain sentence.
- Do not edit `PROVINCE.md` to add audio this round. It is not one of claim C's `lands` (`claims.json:39-41`), so changing it would be scope creep.

Verification, unrun (for the integrator):
- `rg -n 'audio-shokunin' corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` → at least 1, inside the Scope H2 or the `- scope:` line.
- The round-50 contract checker passes, with the last H2 being Scope and `Handoff: lore-shokunin` present.
- `rg -niE 'Hz|LUFS|dBFS|stem|loop seam' corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. Any hit should be a language-side acoustic fact (for example a whistle's pitch range from a cited source), not an asset specification.

## Side finding (outside C's topic, for the frontier step only)

`tabi-shokunin/SKILL.md:613-616` already holds a fleet rule on captchas: "**`isTrusted`-checking sites are a stop, not a puzzle**: synthetic `click`/`fill` are ignored (banking portals, captchas) — hand the page back to the user". The round's mined mistake (S094 opened through a bot challenge; `corpus/lessons/round-51-verifier-spotcheck.md:108`, `:129`) and QUALITY criterion 10 (`corpus/QUALITY.md:37`) could cite that rule one-way as prior sibling evidence, rather than standing as a lane-local convention. This is advice only. Browser-access discipline is tabi's province (tabi `PROVINCE.md`, Owns/Refuses), so kotodama should cite it, not restate it.

## Unrun checks and limits

- I did not read each sibling's `corpus/README.md` frontier or `ports/` tree one by one. The narrow whole-repo sweep only reached them by pattern (souji census only).
- The scan is lexical. A sibling entry discussing the topic without any of the searched words would be missed. Search 2 lowers that risk but does not remove it.
- No tools were installed or updated.
