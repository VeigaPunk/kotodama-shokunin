# ConnectorOverlap100 — adjacency scan: work song and labour chant (round 100)

Read-only scan. Base `60010a55fb5f04ee728070c463b1a57ae1cc17fc`; nothing written outside this
stage dir. The surface scanned is claim C's: `corpus/knowledge/linguistics/work-song-labour-chant.md`
plus registry rows S1018 upward.

Ownership test used is the lane's own: `corpus/QUALITY.md:373` rule 39 — a file **owns** a surface
when its `- topic:` line or any markdown heading carries a frozen phrase (normalized containment);
prose and table-cell mentions are **adjacency, not ownership**.

---

## 1. Sibling lanes — owner table

21 `*-shokunin/PROVINCE.md` files exist; 19 lanes carry a `SKILL.md`. Term sweep over both files
per lane (`song|music|shanty|chant|rhythm|labour|labor|oral|performance`).

| Owner | Its own text (anchor) | Category | Verdict |
|---|---|---|---|
| **audio-shokunin** | `PROVINCE.md:3-5` "Owns: game audio production — SFX … and soundtrack (motifs, loops, stems, adaptive layers) — verified by headless analysis"; `:13` "Refuses: perceptual-quality claims without a measurable proxy"; `:49` frontier names "engine-native adaptive music (Godot AudioStreamInteractive/Synchronized)" | sound production | **boundary to respect.** Owns audio *content* and its measured proxies, not song as a cultural/linguistic system. Nothing in its province claims repertoire, text, or performance roles. The new entry must not claim audio assets, tempo/timbre design, or perceived quality. |
| **game-dev-2d-shokunin** | `PROVINCE.md:17` lists `audio` among the engine systems its fixtures cover; `:10` refuses "narrative canon (lore lane — contested scope is reported, not absorbed)" | engine integration | **boundary to respect.** Engine-side audio (mixer, triggers, import) is theirs; no reference-craft claim. |
| **game-dev-3d-shokunin** | no `audio|music|sound` line in `PROVINCE.md` (`grep` rc=1); `SKILL.md:17` "Nothing here is oral knowledge" (disclaimer) | — | **no overlap.** |
| **lore-shokunin** | `PROVINCE.md:3` owns "fictional-world records … with consistency verification"; `:9` refuses "claiming canon without an in-world citation"; `:28` names kotodama as the generator and reserves "the names and dates recorded on landed entities and events" | canon | **boundary to respect.** The entry is non-canon reference + generative method; every worked example must stay a handoff packet, never a world-bible record. |
| **chousa-shokunin** | `PROVINCE.md:3-8` owns "question framing; source hierarchy …; citation chaining and hop resolution; claim-vs-source verification; search-strategy taxonomy". No oral-history, interview or fieldwork claim (`grep -inE 'oral|interview|fieldwork|song|music'` over PROVINCE+SKILL → one hit, `SKILL.md:550` "behavioral", rc=0) | research method | **boundary to respect.** The entry's sourcing follows the lane's own `SOURCES-CONTRACT-v1`; the *method of research* stays chousa's. |
| **kotoba-shokunin** | `PROVINCE.md:69` records the split: "kotodama owns generative linguistic-cultural worldbuilding … and refuses prompt/skill craft by name; kotoba owns that craft". `grep -inE 'song|music|chant|oral'` → none, rc=1 | prompt/skill craft | **no overlap.** |
| **kotodama-shokunin** (own lane) | `PROVINCE.md:3-20`: domain is linguistic-cultural worldbuilding; owns `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`; refuses canon, research method, prompt craft, game mechanics | reference craft | **this lane's surface.** |
| kagi, kaidoku, kake, kama, kasegi, kengaku, kumitate, mado, mori, revenger, souji, tabi, tameshi, tsukuroi | term hits are incidental only: `kake` = field-performance/CWV and an HTML `audio` element list; `kama` = llama.cpp audio-modality errors; `kasegi`/`revenger` = "division of labour"; `kengaku` = "No oral tradition" disclaimer (`SKILL.md:21`); `kaidoku` = "temporal-sweep"; `mori` = "behavioral"; `tabi`/`mado`/`tsukuroi`/`kumitate` = "Nothing here is oral knowledge" disclaimers and no-oral-context test prose; `souji`/`tameshi` = gate prose | — | **no overlap.** None claims song, music, chant, or oral performance as a domain. |

Not fleet siblings, checked and excluded: `/home/vgpnk/Projects/audio-shokunin-publish/PROVINCE.md`
is a separate top-level repo carrying the same audio `Owns` text (sha256 `99ba0e93…` vs the lane's
`20d881a6…`; different bytes, same claim); `kimi-shokunin` has no `PROVINCE.md`/`SKILL.md`;
`art-east-asian-design` (named in two refusals) does not exist as a repo here;
`/home/vgpnk/Projects/shokuknow` is a read-only domain source tree whose `lanes/` mirror and
`doctrine/` carry no work-song/shanty/labour-chant line (`grep -rliE` rc=1).

**Result: no sibling lane claims the work-song surface.** The only adjacent sibling owner is
audio-shokunin, and it owns sound *production*, not the cultural-linguistic system.

---

## 2. In-lane neighbours — one boundary sentence each

| Entry | What it owns (anchor) | Boundary for the new entry | Verdict |
|---|---|---|---|
| `linguistics/orality-formulaic-language.md` | the Parry–Lord composition engine: meter, epithet banks, type-scenes, kennings, §8 register checklist (`:99-128`) | It owns *how the words are composed*; the new entry owns *when and why the song is sung* (task timing, leader/crew, repertoire) and cites orality one-way for the formula machinery. | boundary to respect |
| `linguistics/lullaby-child-song-formulae.md` | child-directed song and the repertoire-graph idea — a tune shared with a work song (`:193`, `:253`, `:285`) | It owns the lullaby end of the tune graph; the new entry owns the labour end and must not re-derive lullaby register shift or address-to-child. | boundary to respect |
| `linguistics/funerary-lament-dirge-formulae.md` | mourning song; uses "work song" only as a contrast class — a lament "too singable … will be mistaken for a work song" (`:129`, `:206`) | It owns the lament and the singability test; the new entry owns the work-song side of that contrast. | boundary to respect |
| `linguistics/praise-poetry-panegyric.md` | the praise singer's office, patronage, reward, and the limits of flattery (`:18` topic) | It owns the occupational *praise* role and its economy; a work song's licensed complaint/satire is a different speech act and must not absorb praise's office/patronage grammar. | boundary to respect |
| `linguistics/verbal-duelling-ritual-insult.md` | song duels, flyting, senna, boast-and-riposte (`:15` topic) | It owns song-as-contest; the new entry owns song-as-coordination and cites it for improvised riposte rules. | boundary to respect |
| `linguistics/speech-surrogates-whistled-drummed.md` | channel design — whistled/drummed speech, ambiguity repair, who may use the channel (`:3` topic); `:12` already routes "sound production to audio-shokunin, canon to lore-shokunin" | It owns the surrogate channel; the new entry owns the unmediated vocal work song. Its `:12` scope line is the precedent phrasing for the new entry's own boundary section. | boundary to respect |
| `linguistics/toast-drinking-speech-formulae.md` | the toast as speech act, toastmaster's office, toast sequence, penalty cup (`:18` topic) | It owns the drinking rite; call-and-response over a task is not a toast sequence. | boundary to respect |
| `culture-material/music-instrument-lexicon.md` | music as a cultural system: Hornbostel–Sachs, scale-and-affect doctrine, instrument naming, §5 ceremonial registers, §6 music–myth (`:3`, `:72-102`) | It owns organology, scale doctrine and ceremonial register; the new entry owns song repertoire and task fit, and makes no instrument-taxonomy claim. | boundary to respect |
| `culture-material/maritime-seafaring-lexicon.md` | the ship's working register as one of six hull decisions: `:29` "what the crew says to work the hull — commands, the wage cycle, **the songs that pace shared labour**", handoff column "**who times the work**" | It owns the hull's working-register row; the new entry owns the song system and must cite this row one-way rather than re-derive shipboard command vocabulary. | boundary to respect — **closest seam in the lane** |
| `culture-material/dance-performance-movement-codes.md` | movement vocabulary, notation, "Dance–song–voice coupling" (the baile/cante/toque triad), festival registers | It owns the performing-art triad and movement codes; the new entry owns the labour function, not the dance coupling. | boundary to respect |
| `culture-material/craft-artisan-lexicon.md` | the workshop as a speech community: tool names, material grading, guild ranks, maker's marks (`:3` topic) | It owns the workshop's term banks; a craft work song cites it for the trade vocabulary and owns only the song. | boundary to respect |
| `culture-material/agrarian-field-system-lexicon.md` | the field system and the labour calendar — "peak-labor month", the four institutions (`:4` topic) | A field song's timing couples to that calendar; the calendar and its vocabulary stay there. | boundary to respect |
| `culture-material/trade-economy-lexicon.md` | market language, including "auction chant" (`:3` topic) | Chant as a market cry is a market register, not a work song; no absorption either way. | boundary to respect |
| `culture-material/textile-technology.md`, `metallurgy-metal-register.md` | fibre/loom/fulling labour (`textile:3`); ore-to-metal vocabulary (`metallurgy:10`) | Textile and smithing work songs cite these for the production chain and own only the song. | boundary to respect |

---

## 3. Contested scope — routed to the L1 (not absorbed)

**C-1 — the coupling line already assigns "work songs" to the orality entry.**
`culture-material/material-culture-inference-method.md:15` reads: "linguistics/orality-formulaic-language
(work songs, maker formulas, epic object biographies)". But `orality-formulaic-language.md` carries no
frozen phrase in its topic line or headings (owner sweep below, 0/271) and its §8 checklist has no
task-timing item. Two readings are live: (a) the coupling line is a stale pointer and the new entry
becomes the owner; (b) orality owns work songs as formulaic verse and the new entry is a subtype.
The honest resolution is a one-way pointer update in a later round — it is **outside claim C's surface**
(entry + registry rows + evidence + index), so it must not be edited this round.

**C-2 — the seafaring entry already assigns "the songs that pace shared labour" and "who times the work".**
`culture-material/maritime-seafaring-lexicon.md:29` puts both in the ship's working-register row. If the
new entry writes a shanty section with crew roles and timing, the seam "who times the work" is claimed
twice. Proposed split (for the L1 to accept or refuse): seafaring owns the hull's register row; the new
entry owns the song system; each cites the other one-way. Not contested if the entry never re-derives
shipboard command vocabulary.

**C-3 — "work rhythm" invites an acoustic claim that belongs to audio-shokunin.**
audio-shokunin owns soundtrack content and refuses "perceptual-quality claims without a measurable proxy"
(`PROVINCE.md:13`). A design procedure that says how the song *sounds* (tempo, timbre, overlap of call
and response) crosses into its surface. The entry should design words, roles and timing only; any
acoustic or perceptual statement is audio's, and none is needed for claim C.

---

## 4. Measurements (command, rc)

| # | Command | Result | rc |
|---|---|---|---|
| 1 | `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md \| wc -l` | 21 | 0 |
| 2 | `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md \| wc -l` | 19 | 0 |
| 3 | per-lane `grep -ciE 'song\|music\|shanty\|chant\|rhythm\|labour\|labor\|oral\|performance'` over PROVINCE.md and SKILL.md | table in §1 | 0 |
| 4 | python3 sweep, topic lines + all `#`–`######` headings, normalized containment, six frozen phrases, over `corpus/knowledge/**/*.md` | **owners = 0**, files = 271 | 0 |
| 5 | python3 sweep, same six phrases, whole-file prose | 5 files: `civilizations/balts.md` (work song×1), `civilizations/maori.md` (call and response×1), `culture-material/material-culture-inference-method.md` (work song×1), `linguistics/funerary-lament-dirge-formulae.md` (work song×2), `linguistics/lullaby-child-song-formulae.md` (work song×3) | 0 |
| 6 | `grep -cE '^\| S[0-9]+ ' corpus/SOURCES.md` | 941 rows | 0 |
| 7 | `grep -oE '^\| S[0-9]+ ' corpus/SOURCES.md \| tr -d '\| ' \| sort -V \| tail -1` | highest `S1017` | 0 |
| 8 | `grep -inE 'shanty\|chantey\|work song\|worksong\|song leader' corpus/SOURCES.md` | no output — the lane holds **no** work-song source row | 1 |
| 9 | `sha256sum audio-shokunin/PROVINCE.md /home/vgpnk/Projects/audio-shokunin-publish/PROVINCE.md` | `20d881a6…`, `99ba0e93…` | 0 |
| 10 | `grep -rliE 'work song\|shanty\|labour chant' /home/vgpnk/Projects/shokuknow/lanes /home/vgpnk/Projects/shokuknow/doctrine` | no output | 1 |
| 11 | `grep -inE 'song\|music\|chant\|oral' lore-shokunin/PROVINCE.md` | no output | 1 |
| 12 | `grep -inE 'song\|music\|chant\|oral' kotoba-shokunin/PROVINCE.md` | no output | 1 |
| 13 | `grep -inE 'song\|music\|chant\|oral' kotodama-shokunin/PROVINCE.md` | no output (the lane's music mention is `SKILL.md:607`, its own corpus map) | 1 |
| 14 | `grep -inE 'oral\|interview\|fieldwork\|song\|music' chousa-shokunin/PROVINCE.md chousa-shokunin/SKILL.md` | 1 hit, `SKILL.md:550` "behavioral" | 0 |
| 15 | `grep -inE 'audio\|music\|sound' game-dev-3d-shokunin/PROVINCE.md` | no output | 1 |

Sweep 4 independently reproduces claim C's frozen before-state (`C8 owners=0`) on the worktree; it is
the same definition as `corpus/QUALITY.md:373` rule 39, not a filename sweep.

---

## 5. Files not read / absent

- `/home/vgpnk/Projects/shokunin/kimi-shokunin/PROVINCE.md` and `SKILL.md` — **absent** (rc=2). Not a
  province-bearing lane; excluded from the table.
- `/home/vgpnk/Projects/art-east-asian-design/` — **absent** (rc=2), though two provinces refuse into it.
- `/home/vgpnk/Projects/shokunin/audio-shokunin-publish/PROVINCE.md` — **absent**; the publish copy lives
  at `/home/vgpnk/Projects/audio-shokunin-publish/PROVINCE.md` and was read there.
- No sibling `PROVINCE.md` or `SKILL.md` was unreadable for permission or format reasons.

---

## 6. What the new entry must carry (one-way pointers, for ScribeEntry100)

1. `orality-formulaic-language.md` — formula composition; the entry owns task coupling only.
2. `lullaby-child-song-formulae.md` — the tune/repertoire graph; the entry owns the labour end.
3. `funerary-lament-dirge-formulae.md` — the singability contrast that separates lament from work song.
4. `praise-poetry-panegyric.md` — the occupational singer's office and patronage; licensed complaint is
   not panegyric.
5. `verbal-duelling-ritual-insult.md` — song as contest.
6. `speech-surrogates-whistled-drummed.md` — the channel, not the song.
7. `culture-material/music-instrument-lexicon.md` — organology, scales, ceremonial registers.
8. `culture-material/maritime-seafaring-lexicon.md:29` — the hull's working-register row and "who times
   the work"; cite, do not re-derive.
9. `culture-material/dance-performance-movement-codes.md` — the dance–song–voice triad.
10. `audio-shokunin` (sound production) and `lore-shokunin` (canon) — the two external routes, phrased as
    `speech-surrogates-whistled-drummed.md:12` already phrases them.

Hazard for the wave, not for this entry: `praise-poetry-panegyric.md` is simultaneously an in-lane
neighbour (item 4) and claim O's O3 replay target. `claims.json` separability requires its Yoruba row
label, table header and Yoruba limit cell to stay byte-unchanged; no seat may let a praise-entry edit
move those bytes.
