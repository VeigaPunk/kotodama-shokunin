# ScoutGapSurrogate — claim C premise: gap sweeps re-run and owner map

Seat: KotodamaR52.ScoutGapSurrogate (leaf). Round 52, attempt 1, 2026-10-22.
Worktree: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, `git rev-parse HEAD` = `dea5ece63ca4372c41766ab242df1e26c2e6898a` (claim D landed on declaration `d9f73c8`, base `147cfde`). Untracked only: `.ufo/waves/round-52/`, `corpus/lessons/round-52.md`; corpus bytes otherwise equal to base. No subagents, no background jobs.

## 1. Assigned item

Re-run the two sweeps named in `reports/round-52/claims.json` → `claims[C].gap_evidence_at_base`, enumerate every `corpus/knowledge` line the surrogate vocabulary touches, and rule on whether any current file owns **speech surrogates as a register** (whistled, drummed and other instrument-borne speech, plus the signal-code boundary).

## 2. Sweeps re-run (2026-10-22, worktree as above)

| sweep | command | result |
|---|---|---|
| filename | `find corpus/knowledge -iname '*whistl*' -o -iname '*surrogat*' -o -iname '*drum*'` | **0** paths — matches the declaration |
| topic line | `grep -rliE '^- topic:.*(whistl\|surrogat\|drum language\|talking drum)' corpus/knowledge` | **1** file: `culture-material/music-instrument-lexicon.md` — matches the declaration |
| sibling lanes, topic | same grep over 20 sibling `corpus/knowledge` trees | **0** files |
| sibling lanes, filename | `find` over 7 of those trees for the same three stems | **0** paths |
| corpus size | `find corpus/knowledge -name '*.md' \| wc -l` | **227**; `linguistics/` = 26 |

Caveat on the topic sweep, for the head's `gap filled` wording: the single hit is `music-instrument-lexicon.md:3`, where the match is the tail of a long music–myth clause — "musical contests, talking drums" — not a claim to own speech surrogacy. The probe also omits `silbo`, `gong`, `horn call`; I added them in the enumeration below and they produce **no** topic-line owner. The hit is therefore a near-miss, not an owner.

## 3. Enumeration — 46 matches, 15 files

`grep -rniE 'whistl|drum speech|talking drum|drum language|surrogate|slit gong|qeej|silbo|horn call|bugle' corpus/knowledge`

| file | n | lines | what the file owns |
|---|---|---|---|
| `civilizations/yoruba.md` | 8 | 21, 41, 42, 43, 47, 53, 57, 189 | **Yoruba dùndún speech surrogacy** as a case: a dedicated H2 `Drum speech` at `:41`, the DT-D/DT-P/DS/D-DR labels `:43`, one-to-many mapping `:47`, bàtá `(to-verify)` `:57` |
| `civilizations/mesoamerica-primary-sources.md` | 7 | 8, 51, 58, 67, 68, 118, 130 | documentary sense only — "digital surrogate"/facsimile layer; **unrelated** |
| `linguistics/phonetics-phonology.md` | 6 | 75, 197, 198, 199, 309, 310 | **environment→inventory couplings** in §7: whistled registers (`:197-198`) and drum language (`:199`); couples line `:75`; Silbo errata recheck `:309-310` |
| `culture-material/music-instrument-lexicon.md` | 6 | 3, 4, 5, 76, 98, 100 | **organology / music–myth**: `instruments that speak` table row `:98`, the "centerpiece coupling" bullet `:100`, bugle-call signal lexicon `:76`, topic `:3`, couples `:5` |
| `civilizations/fon-dahomey.md` | 5 | 29, 31, 35, 181, 182 (+ table 39–42, rules 44–46) | **Fon drum speech as an unresolved identification problem**: H2 at `:31`, the four-way comparison table `:39-42`, the channel-loss rule `:44`, the prototyping method `:45` |
| `linguistics/orality-formulaic-language.md` | 3 | 24, 114, 124 | **the "broadcast layer" extension** of the oral-formulaic register: item 12 `:114`, meter-table row `:124`; sources head `:24` |
| `linguistics/sound-symbolism.md` | 2 | 19, 121 | a **pointer row** `:121` and a couples claim `:19` ("phonetics-phonology §7 owns whistled/drum channels") |
| `civilizations/akan.md` | 2 | 28, 58 | **Akan atumpan limit**: H/L only, tone/note mismatches `:58`; abstract citation `:28` |
| `verification/to-verify-triage-protocol.md` | 1 | 4 | "Consulted surrogates" — access terminology; **unrelated** |
| `verification/phonology-sanity-gate.md` | 1 | 4 | "surrogates" in the sources list; **unrelated** |
| `verification/naming-collision-gate.md` | 1 | 8 | "Whistler" (Ken Whistler, Unicode) — **false positive** |
| `synthesis/naming-canon-workflow.md` | 1 | 9 | "Whistler" — **false positive** |
| `myth-symbol/motif-index-usage.md` | 1 | 13 | "verification surrogates" — **unrelated** |
| `culture-material/textile-technology.md` | 1 | 30 | "silk-surrogate" — **unrelated** |
| `culture-material/sumptuary-law-rank-display.md` | 1 | 37 | "measurable surrogate" — **unrelated** |

Signal: **13 of 46 matches are not about speech at all** (7 facsimile + 2 Whistler + 2 access-terminology + 1 fibre + 1 sumptuary). The real evidence base is 33 lines in 8 files — four linguistics/culture-material files, three civilization entries, one pointer row.

## 4. Verdict: is there a current owner of speech surrogates as a register?

**No — no file owns the register. C is a genuine coverage claim.** Three independent grounds:

1. **No filename owner** (sweep 1 = 0) and **no topic-line owner** (sweep 2's single hit is a music entry's incidental phrase, §2).
2. **No H2 anywhere owns the cross-channel typology.** The only H2s in the territory are per-culture (`yoruba.md:41`, `fon-dahomey.md:31`). The linguistics treatments are one bullet inside an environment section (`phonetics-phonology.md:197-199`) and one design-lever bullet inside a music–myth section (`music-instrument-lexicon.md:100`). Nothing covers horns, reed pipes, jaw harps, xylophones or gongs as speech channels: `grep -rniE 'xylophone|jaw.?s? harp|qeej|slit.?gong|reed pipe|horn (call|signal|speech)|signal code' corpus/knowledge --include='*.md'` exits 0 with **0 lines**. The nearest thing to that territory is the *signal* side, surfaced only by the broader enumeration: `music-instrument-lexicon.md:76` (bugle calls as a fixed time-of-day lexicon) — exactly the boundary C must draw.
3. **The boundary claims are per-culture or single-sentence.** `music-instrument-lexicon.md:100` asserts "Drum and whistle speech are language phenomena, not merely music phenomena"; `fon-dahomey.md:39-42` distinguishes surrogacy from signal/ritual-music/praise but only as a Fon verification table; `fon-dahomey.md:44` states the channel-loss rule once. No general, cross-channel, design-facing treatment exists, and nothing assigns an owner. `PROVINCE.md` and `corpus/*.md` top-level docs mention the topic nowhere.

**Sub-defect in the declaration:** `gap_evidence_at_base` lists five partial-owner locations in four files and says "one to three lines each". That understates the corpus: three civilization entries carry dedicated drum-speech sections (yoruba 8 matches, fon 5 plus an H2, akan 2). The claim's *falsifier* is restatement, not the count of neighbours, so the claim stands as declared — provided C's §2 boundary table cites those three entries one-way. If the head's `gap filled` line repeats "one to three lines each" for the linguistics files only and names the civilization cases explicitly, it is accurate.

## 5. Partial owners C must cite one-way

Drafted rows for C's §2 (`| Neighbour (anchor) | What it owns | This entry's boundary |`), all re-read at `dea5ece` today:

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `phonetics-phonology.md:197-199` (also `:75`, `:309-310`) | the environment→inventory couplings: mountains + herding → whistled registers (Silbo Gomero, Kuşköy, Chinantec; Meyer 2008); tone + gongs → tone-and-rhythm set phrases (Kele/Congo; Carrington 1949) | the inventory inference stays there; this entry owns the channel typology and what each channel can and cannot encode |
| `../culture-material/music-instrument-lexicon.md:98-100` (also `:76`, `:3`, `:5`) | organology and the music–myth slot: the "instruments that speak" row and the sentence that drum/whistle speech are language phenomena; bugle calls as a ceremonial signal lexicon | the instrument taxonomy and ceremonial registers stay there; surrogate encoding, its ambiguity and its social control are designed here |
| `orality-formulaic-language.md:114` and `:124` | the "broadcast layer" extension of the formulaic register, and the meter-table row for drum/whistle speech | formulaic composition stays there; the channels themselves, and who may use them, are designed here |
| `sound-symbolism.md:121` (with `:19`) | the cross-file hook row pointing at the music and phonology files | the iconicity toolkit stays there; this entry makes no iconicity claim |
| `../civilizations/yoruba.md:41-58` (also `:21`, `:189`) | the Yorùbá dùndún case: the DT-D/DT-P/DS/D-DR analytical labels, the one-to-many interpretation constraint, the bàtá gap | the Yorùbá evidence and its calibration stay there; cited here as one case, never rebuilt |
| `../civilizations/akan.md:58` (with `:28`) | the Akan limit: the atumpan pair encodes only H and L; tone/note mismatches elsewhere in the surrogate set | the Akan evidence stays there; cited as the channel-loss example |
| `../civilizations/fon-dahomey.md:31-46` (esp. `:39-42`, `:44-46`) | the Fon identification problem, the surrogacy/signal/ritual-music/praise comparison, and the rule that tone without segments is not a lossless channel | the Fon question stays there; this entry states the signal boundary as one general criterion and cites `:39-41` |
| `sociolinguistics-registers.md:49-50` | register machinery: register vs dialect vs diglossia, chosen per setting | the machinery stays there; who may speak (§8) is one permission case |
| `writing-systems.md:21` | script typology, including semasiography as "not writing proper" | the script taxonomy stays there; a whistle or drum code is not a script for speech |
| `register-lexicon-ceilings.md:3` | what a mechanically derived marked register can and cannot say | the ceiling argument stays there; a surrogate's losses are channel losses here |
| `language-shift-obsolescence-revival.md:43` and `:48` | transmission/function/documentation axes and the semi-speaker ladder | the ladder stays there; §9's learning and decline of a surrogate repertoire is a case under it |
| `conlang-methodology.md:3` | the artlang pipeline, spoken-first | the pipeline stays there; this entry adds the channel choice as a pipeline step |
| `linguistic-anthropology.md:13` and `:77` | SPEAKING-grid speech events and register ecology | the speech-event frame stays there; performance occasions are designed here |
| `verification/calibration-registry.md:33-41` | the R/C/B/H/T status vocabulary | cited for every status code in §12 |

That is 14 verified rows; the contract (§2.4) asks for 15 or more, so C's own §4 candidate sweep must add at least one more that it re-reads, not a padding row.

## 6. Lines C would restate if it is careless

Each is a specific sentence whose content C's planned sections duplicate; cite the anchor, do not re-assert.

1. `music-instrument-lexicon.md:100` — "Drum and whistle speech are language phenomena, not merely music phenomena." This is C's §1/§2 thesis already stated. C should say the music partition owns that sentence and build only the channel design.
2. `phonetics-phonology.md:197-199` — both ecology→channel couplings, with their exemplars and citations. C's §4/§5 must not present "mountains + herding → whistling" or "tone + gongs → set phrases" as its own finding; cite `:197-199` and carry its own S134+ sources for channel structure.
3. `fon-dahomey.md:39-42` — the four-row speech-surrogacy / conventional-signal / ritual-music / royal-praise comparison. C's §3 boundary is the same distinction generalized: state one criterion (a recoverable verbal message vs an event index) and cite `:39-41`; do not re-use those four labels as C's taxonomy.
4. `fon-dahomey.md:44` — "Tone without consonants and vowels is not automatically a lossless message channel", plus the prototyping method at `:45`. C's §6 would restate this; cite `:44-45`.
5. `yoruba.md:43` and `:47` — the DT-D/DT-P/DS/D-DR labels and the one-to-many mapping constraint; also `:57` (dùndún ≠ bàtá) and the table at `:48-53`. C's §5/§6 must cite `:41-58` as a case study pointer, not reproduce the labels or table.
6. `akan.md:58` — the atumpan H/L limit and tone/note mismatch. C's channel-loss claim must cite `:58`.
7. `orality-formulaic-language.md:114` — "a 'broadcast layer' for the same formulas". If C uses "broadcast layer" as its own coinage, cite `:114`.
8. Safe to cite with no restatement risk: `sound-symbolism.md:121` (pointer only).

## 7. Consequences for C's declaration and head

- Counters: 227 → 228 files; `linguistics/` 26 → 27. README targets are live and precise: `corpus/README.md:231` `## linguistics/ (26)`; `:602` `Total knowledge entries: 227.`; `:606` `(total 227 files; directory totals 26/26/28/29/24/94)`; the increment block at `:3-12` (revision 2.8 pattern) and a new `revision: 2.9` above it; `python3 -B reports/round-28/readme/sweep.py` must print `rows 228 files 228`, `topic_mismatch 0 []`, exit 0. Insert the index row between `sound-symbolism.md` (`README.md:253`) and `syntax-typology.md` (`README.md:254`), topic text byte-equal to the entry's `- topic:`.
- `corpus/SOURCES.md` has **zero** rows for this literature. Greps for `whistl|drum speech|surrogate|silbo|gong|Carrington|Busnel|Meyer|Finnegan|Durojaye|Villepastour` hit only substring false positives (`S052`'s URL contains `classes`). The existing citations are inline author-year mentions in entry bodies (`phonetics-phonology.md:197-199`, `orality-formulaic-language.md:24`, `fon-dahomey.md:181-182`, `yoruba.md:21`, `akan.md:28`), never registry rows. So every C source is new ground: each must be opened by ordinary means this round, given an S134+ row at `SOURCES.md:28`'s 11 columns, and its `used-by` must name the new entry. Citing `yoruba.md:21` gives C the study's existence, not the claim.
- Stale-ownership note for the L1, **outside C's `lands`**: `sound-symbolism.md:19` asserts that `phonetics-phonology.md` "§7 owns whistled/drum channels", and `phonetics-phonology.md:75` lists "whistle & drum channels" in its couples line. Once C lands, both sentences under-describe the corpus. They are not C's to edit (C lands entry + README + SOURCES only); route as a follow-up repair rather than widening C.

## 8. Unrun checks and limits

- No LSP server serves Markdown semantic references here; `lsp` was not attached, so every owner claim above rests on literal `grep`/`find` over `corpus/knowledge` at `dea5ece`, not on semantic reference resolution. Recorded as the literal fallback, not presented as semantic proof.
- I did not open any external source for this seat; source opening belongs to C's seats. No URL claims appear above.
- Post-landing state is unmeasured: I did not create the entry, so 227 → 228 and the sweep footer are predictions from the counter, not observed values. `python3 tools/check-source-access.py`, `reports/round-28/readme/sweep.py` and the entry contract's checker were **not** run (they belong to the integrator's acceptance).
- The 14-row §2 draft is verified for existence and line number only; each row's "what it owns" wording is my reading of the line, to be re-checked by C's boundary scribe against the source text.
- Tooling: nothing installed, nothing upgraded; no package manager transaction. Read-only `git rev-parse/log/status` and read-only `jj log --ignore-working-copy` used for state only; no index, jj or worktree mutation.
