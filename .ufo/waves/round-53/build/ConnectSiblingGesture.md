# ConnectSiblingGesture — round 53, claim C sibling overlap

Seat: `KotodamaR53.ConnectSiblingGesture` (connector, leaf, read-only). Date 2026-10-22.
Lane head read: `60f1d2a3d832b926e37f82b11c67496d131a1431` (kotodama declaration commit).
Assigned item: read-only scan of every sibling lane `/home/vgpnk/Projects/shokunin/*-shokunin`
(20 lanes, kotodama excluded) — `corpus/knowledge/**`, `PROVINCE.md`, `SKILL.md` — for ownership of
gesture, body language, pointing, nonverbal communication, character animation of gesture,
emotes and kinesics. Advice for the integrator only. Nothing was absorbed, edited or admitted.

## Result

**No sibling lane owns or partially owns gesture, body language, pointing, nonverbal communication,
emotes or kinesics.** The proposed entry `linguistics/gesture-co-speech-pointing.md` (co-speech
gesture, pointing and quotable gestures as conlang and worldbuilding method) does not overlap any
sibling's province. Two siblings sit **adjacent** to it (lore and the two game-dev lanes), and every
other hit is a homonym or a figure of speech. Contested scope: **none that requires a ruling.**
There are two adjacency boundaries to state in the entry's one-owner section; both are already covered by
kotodama's own refusal line (`PROVINCE.md:16-19`).

The real overlap risk is **inside kotodama**, not across lanes (see "Second-order effect" below).

## Hit table

Sibling pins read: lore `380ef3ab`, game-dev-2d `7753d49b`, game-dev-3d `89dd182b`, kake `f1ffb817`,
audio `7a2fcd4f`, mado `8e5d9369`, kotoba `43ca0bfb`. Paths are fleet-root-relative.

| Path:line | What it says | Class | Overlap with C? |
|---|---|---|---|
| `lore-shokunin/PROVINCE.md:3` | owns fictional-world records: entities, relations, timeline events, consistency verification | adjacent (canon owner) | no. Lore records a world's gesture repertoire once it lands as canon; kotodama designs the system and hands it off (`kotodama-shokunin/PROVINCE.md:16-17,22-25`) |
| `lore-shokunin/PROVINCE.md:28` | lists kotodama's owned design surfaces (names, calendars, eras) and the handoff contract; CM-g kotodama packet intake is `uncovered` (`:19`) | adjacent (handoff) | no. A gesture system is a new kotodama design surface that is not on lore's list. Advisory only: lore's line 28 will not name it until lore chooses to |
| `game-dev-3d-shokunin/PROVINCE.md:53` | "Input-driven movement and animation have deterministic in-engine fixture cases" (fixtures `corpus/fixtures/run_battery.py:294-304`: blend, playback and key tracks on position) | adjacent (animation runtime) | no. These are runtime playback fixtures with no gesture content. Kotodama refuses game mechanics (`kotodama-shokunin/PROVINCE.md:18-19`) |
| `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/executability/animation-controlrig.md:1-15` | static-only verdict card for Unreal Control Rig, State Tree and Behavior Tree; no tool was executed | mention (engine animation tooling) | no |
| `game-dev-2d-shokunin/PROVINCE.md:17` | core includes "animation" (Godot 2D headless) | adjacent (animation runtime) | no |
| `game-dev-2d-shokunin/corpus/knowledge/2026-10-12-production-checklist.md:14` | AnimationPlayer state change at frame k, no stuck state | mention | no |
| `kake-shokunin/corpus/knowledge/accessibility-review-cards.json:411-419` | WCAG 2.2 SC 2.5.1 "Pointer Gestures" (multipoint and path-based touch input) | homonym (input-device gesture) | no. This is about touch input, not human communication |
| `mado-shokunin/corpus/knowledge/walker-deep.md:217`, `walker-route-r18.md:255` | desktop emoji picker | homonym (emoji) | no |
| `kotoba-shokunin/SKILL.md:330`, `corpus/knowledge/dispatch-prompt-audit-round7.md:28` | "no deictic references" in prompts | homonym (deixis in prompt text) | no |
| `kotoba-shokunin/corpus/knowledge/harness-independent-round37.md:250`; `kasegi-shokunin/corpus/knowledge/intake-surface.md:123` | "an empty gesture", "only gesture at" | figure of speech | no |
| `tabi-shokunin/corpus/knowledge/webmcp-nonautosubmit-round-21-corrected.md:34` | the `isTrusted` user-gesture flag on a submit event | homonym (browser user activation) | no |

Zero hits in any sibling for: `body language`, `nonverbal`/`non-verbal`, `kinesic*`, `emote`/`emoting`,
`co-speech`, `proxemic*`, `sign language`, `facial expression`, `hand signal`, `mocap`/`motion capture`,
`facial rig`, `lip sync`. Zero sibling filenames match `*gestur*`, `*pointing*`, `*kinesic*`, `*emote*`,
`*nonverbal*` or `*body-lang*`. The two `*body*` filename hits are a Godot physics body
(`game-dev-2d-shokunin/corpus/knowledge/2026-10-19-tilemaplayer-body-rid-attribution.md`) and a Chrome
profile (`tabi-shokunin/corpus/knowledge/chrome-remote-debugging-profile-boundary.md`), not gesture.
Lanes with no hit of any class: audio, chousa, kaidoku, kama, kengaku, kumitate, mori, revenger,
souji, tameshi, tsukuroi, kagi (only "handshake" and "posture" as technical terms).

## Contested scope for the integrator

None of these needs a ruling. Name both in C's section 2 (one-owner boundary) as one-way pointers,
and absorb neither:

1. **lore (canon).** A gesture repertoire designed for a world is a kotodama system. Once that world
   adopts it, lore records it as canon. The handoff goes through
   `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`.
   Lore's intake row CM-g is `uncovered` (`lore-shokunin/PROVINCE.md:19`), so this handoff is
   declared but unexercised. Keep C's worked example NON-CANON, as the contract requires.
2. **game-dev-2d / game-dev-3d (animation runtime).** If C's decision table says a repertoire
   "feeds character animation", that is a design input only. Playback, blending, rigs and emote
   triggers are game-dev runtime. Kotodama refuses mechanics (`kotodama-shokunin/PROVINCE.md:18-19`), and
   neither game-dev lane holds gesture-content knowledge to cite.

The kake, mado, kotoba and tabi hits are homonyms. None of them should appear in C's boundary table.

## Second-order effect: the overlap is internal

Every concentrated owner of this topic is already in kotodama. C's planned sections run into those
owners in three places. Read at the lane worktree:

| C section | Internal owner (re-read) | Restatement risk |
|---|---|---|
| 3 gesture types | `corpus/knowledge/culture-material/adornment-body-codes.md:79`: Ekman and Friesen (1969) taxonomy: emblems, illustrators, affect displays and more | high. Restating the five-way taxonomy would duplicate it. C should own what each type *carries in the utterance* (the co-speech relation) and point to :79 for the taxonomy |
| 7 quotable gestures and emblem repertoires | `adornment-body-codes.md:79` (emblems "the conlang-adjacent category") and `:92` (emblem collisions, nod/shake inversion); `linguistics/sign-languages-manual-modality.md:161` already routes "emblems and proxemics stay at `adornment-body-codes.md:79`" | high. An existing in-corpus route sends emblems to adornment-body-codes. For C to own "emblem repertoires as method" without contradicting that route, it needs an explicit split: adornment owns the inventory and failure modes, and C owns quotability (how an emblem is lexicalized, cited and coined in a conlang). Otherwise the integrator should amend :161 in the same change, and only kotodama can do that |
| 8 social control: politeness, hand and status | `adornment-body-codes.md:80-91`: bow, wai, sampeah, kowtow, adoratio and homage gradient table | medium. Point to :82-91, do not re-tabulate. C can own the taboo hand (left-hand rules, pointing taboos), which :77-93 does not cover |
| 5 space and time | `myth-symbol/direction-symbolism.md:6,36`: Guugu Yimithirr absolute frame; Haviland (1993) on pointing | medium. Point to :36 for frames of reference. C owns the pointing behavior, not the frame inventory |
| 9 / finger counting | `linguistics/numerals-and-measures.md:107` | low. One pointer |
| boundary row | `linguistics/sign-languages-manual-modality.md:64` (co-speech gesture as the boundary row of the manual modality) | none. C becomes the owner that this row points to. Nothing in :64 needs to change |

## Proposed move

Connector proposal: one move, bounded. It improves coverage and harms no axis.
Draft C's section 2 as one boundary table with two blocks. In the **sibling** block, write rows for lore and game-dev,
using the wording in "Contested scope" above, and mark the homonym lanes as absent. In the **internal** block, write rows that
split emblems three ways: adornment-body-codes owns the inventory, failure modes and status gradients;
sign-languages owns the manual-modality boundary; C owns the co-speech relation, pointing and
quotability. This keeps `sign-languages-manual-modality.md:161` true without editing it. D is
unaffected because D edits only `speech-surrogates-whistled-drummed.md`.

Draft rows ready to paste (S-ids omitted; these rows cite corpus paths, not sources):

```markdown
| Topic | Owner | This entry's role |
|---|---|---|
| world-specific gesture canon on landed entities | lore-shokunin (world bible; intake via `../synthesis/worldbible-integration-contract.md`) | designs and hands off; never records canon |
| animation playback, rigs, emote triggers | game-dev-2d / game-dev-3d (runtime fixtures) | supplies a repertoire spec as design input only |
| emblem inventory, emblem failure modes, bow and wai gradients | `../culture-material/adornment-body-codes.md:77-93` | points there; owns quotability, not the inventory |
| co-speech gesture as the manual-modality boundary | `sign-languages-manual-modality.md:64,161` | owns the co-speech relation that boundary row points to |
| absolute and relative frames of reference | `../myth-symbol/direction-symbolism.md:36` | owns pointing behavior inside a frame |
| finger counting | `numerals-and-measures.md:107` | one pointer |
```

## Risks

- If C's section 7 claims "emblem repertoires" without the quotability split, `sign-languages-manual-modality.md:161`
  (which routes emblems to adornment-body-codes) and C will name two owners for one topic. That is a
  one-owner-boundary defect a verifier would flag.
- The sibling pins above are the current HEADs. A sibling that adds a gesture or emote entry later
  changes this answer. Rerun the recheck command below.
- Scope of the scan: `corpus/knowledge`, `PROVINCE.md` and `SKILL.md` only, as assigned. Sibling
  `corpus/fixtures`, `reports` and `corpus/lessons` were not scanned, except one read of
  `game-dev-3d-shokunin/corpus/fixtures/run_battery.py:294-304`, which confirmed that the animation fixtures have no gesture content.

## Verification (run by this seat)

```bash
cd /home/vgpnk/Projects/shokunin
for d in *-shokunin; do [ "$d" = kotodama-shokunin ] && continue
  rg -n -i -e '\b(gestur\w*|body[ -]language|nonverbal|non-verbal|kinesic\w*|emotes?\b|emoting|co-speech|deictic|facial expression\w*|hand signals?|pointing (gesture|finger)|lip[ -]?sync|proxemic\w*|sign language)' \
    $d/corpus/knowledge $d/PROVINCE.md $(ls $d/SKILL.md 2>/dev/null); done
```

Output: 13 lines across kake (8, all inside the WCAG cards at `accessibility-review-cards.json:412-464`), kasegi (1), kotoba (3) and tabi (1). All of them are classified above.
A broader second pass (animation, AnimationTree, IK, mocap, etiquette, greeting, bow, posture, emoji)
found only the game-dev animation rows, the mado emoji picker, and unrelated "posture" and "handshake" uses.
The filename `find` over sibling `corpus/knowledge`, `PROVINCE.md` and `SKILL.md` found 0 gesture owners.

Unrun: none of the lane's acceptance scripts (`accept-c.py`, `d-count.py`). They are out of scope for this
seat. Installs: none.
