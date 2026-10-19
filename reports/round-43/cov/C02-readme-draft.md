# C02 — README rev 2.5 draft (claim C)

- seat: C02 (executor, claim C) · out: `reports/round-43/cov/C02-readme-draft.md`
- contract: `reports/round-43/targets.json` seat C02; `reports/round-43/claims.json` claim C
- date: 2026-10-19 · baseline commit: `7ceff59a0216a8ea21ee43262d9fc72abf770cee`
- scope: README edits only, drafted as a fenced diff; no filed byte edited, nothing staged under `corpus/`

## 0. Bottom line

**Blocked as declared, with a mechanically verified conditional draft.** The claim's before-state — "myth-symbol 26, the lithic slot named but unbuilt" — is false at HEAD. The lithic register is already owned by `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, landed in the baseline commit `7ceff59` as the r42 C04 entry. The r42 C01 spare is a second author draft of the **same topic**, and r42's own close-out says it may land only "under a re-scoped claim".

Consequences:

- Landing the spare as-is under a second filename would index two entries that both claim to fill the same lapidary slot.
- Its `- gap filled:` evidence is stale: it asserts HEAD `ac47c78`, 220 files, "no entry owns stone"; HEAD is `7ceff59`, 223 files, and an owner exists.
- A README rev 2.5 at 224 would be **mechanically sweep-green but substantively wrong** — the r28 sweep checks row↔file topic equality, not duplicate topics across files.

Deliverables below:

- **Variant A (§3)**: the exact README rev-2.5 unified diff, verified green against a staged 224-file tree, conditional on the integrator ruling the spare lands under the free r42-plan name `stone-symbolism.md` after a re-scope.
- **Variant B (§6)**: the honest no-bump outcome if the collision is accepted — README stays rev 2.4 / 223, and claim C records `could-not-land-as-declared` with §2 as the evidence.

## 1. Live baseline receipt (measured this seat)

```text
$ git rev-parse HEAD
7ceff59a0216a8ea21ee43262d9fc72abf770cee

$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26

$ find corpus/knowledge -name '*.md' | wc -l
223

$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md

$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", ..., "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
exit=0
```

Pre-edit line anchors in `corpus/README.md`: rev 2.4 block at `:5`; `## myth-symbol/ (26)` at `:205`; section rows `:206-231`; `mineral-stone-symbolism.md` row at `:219`; `Total knowledge entries: 223.` at `:544`; footer block at `:546-548`.

## 2. Collision evidence

1. **Live partition owns the topic.** `ls corpus/knowledge/myth-symbol/*.md` returns 26 entries including `mineral-stone-symbolism.md`; `git log --oneline -5 -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` → `7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore`.
2. **README rev 2.4 already records the routing.** `corpus/README.md:8-9`: "a fourth draft (C01's lithic register) collided with C04's and is routed as a named spare by integrator ruling."
3. **r42's rejection receipt requires a re-scope.** `reports/round-42/validation.json` (claim C failure): "the fourth collided and is routed; … a successor round can land the spare **under a re-scoped claim**."
4. **The spare's own ruling says the same.** `reports/round-42/cov/C01-mineral-spare.md:1`: "C01 and C04 authored the same lithic topic mid-wave … C04 lands … THIS draft is routed as the named spare for a future re-scoped claim."
5. **Topic identity, not complementarity.** The spare's `- topic:` (`:6`) opens "the **lithic register** a fictional culture's symbolic grammar runs on stone, gem and metal"; the landed entry's `- topic:` opens "the lithic register of a fictional culture's symbolic grammar". Both `- gap filled:` lines claim the same lapidary slot from `symbolism-synthesis-method.md:29`. Both files carry 13 numbered sections on the same subject.
6. **The spare's evidence is stale and would land false.** `C01-mineral-spare.md:7` asserts "no entry owns stone" at HEAD `ac47c78` over 220 files; `:24` (`- verified-at:`) repeats `ac47c78`, 220 files, myth-symbol 23. At HEAD: 223 files, myth-symbol 26, owner present. Applying the fenced bytes "unmodified" — the claim's threshold — would inject a false absence claim, a provenance defect under `corpus/QUALITY.md:1`.
7. **No-overwrite check.** `corpus/knowledge/myth-symbol/stone-symbolism.md` is ABSENT; `mineral-stone-symbolism.md` keeps sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`. This seat wrote nothing under `corpus/`.

## 3. Variant A — conditional README rev 2.5 diff

Assumptions, all explicit:

- **A1** target filename `stone-symbolism.md` — the r42 plan's own proposed name (`reports/round-42/plan/P01-plan.md:358`, "**`stone-symbolism.md` — the lithic/gem register.** *Strongest candidate*"), free at HEAD (checked ABSENT), matching the partition's `<topic>-symbolism.md` convention (`animal-`, `color-`, `direction-`, `number-`, `plant-`).
- **A2** the landed entry's `- topic:` is byte-equal to the spare's `:6` text (1337 chars after `- topic: `); the row below carries exactly those bytes.
- **A3** the integrator has resolved the collision by authorizing a re-scoped second entry. If the re-scope changes the topic line or filename, this diff must be regenerated — the row is topic-byte-equal or the sweep fails.

```diff
--- corpus/README.md
+++ corpus/README.md (rev 2.5, conditional)
@@ -1,6 +1,14 @@
 # kotodama-shokunin corpus index
 
 # kotodama-shokunin corpus index
+
+revision: 2.5 — Round-43 lithic-register spare landing (2026-10-19): the
+round-42 C01 spare landed as `stone-symbolism.md` (author fragment
+`reports/round-42/cov/C01-mineral-spare.md`); `## myth-symbol/` moved 26 → **27**;
+the totals line and the counts footer moved 223 → **224** and the footer vector
+25/26/25/29/24/94 → **25/27/25/29/24/94**. Re-measured with
+`python3 reports/round-28/readme/sweep.py`: 224 rows vs 224 files, exit 0.
+Non-canon examples and passing structural gates do not certify historical truth.
 
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
 myth-symbol entries landed (`mineral-stone-symbolism.md`,
@@ -202,7 +210,7 @@
 - `writing-systems.md` — Script typology (logographic, syllabic, abugida, abjad, alphabet, featural), independent inventions and evolution lineages (Sumerian→cuneiform, Egyptian→abjad→alphabets, Brahmi family), decipherment cases as design lessons, matching script type to a language's phonology, and conscript pitfalls.
 
 
-## myth-symbol/ (26)
+## myth-symbol/ (27)
 - `animal-symbolism.md` — fauna as the densest symbolic substrate for a fictional culture — the totemism archive and its demolition (what survives as solid ground: clan totems, crest heraldry, other-than-human persons), a working typology of seven animal-binding mechanisms, guardian/spirit animals and their institutional slots, animal taboos and food laws as category logic vs ecology, zodiac day-signs as animal lexicons (Chinese branches, Mesoamerican 20, Egyptian decans), heraldic beasts as era fossils with heraldic-lag, the serpent's cross-culture double ledger (fertility/water vs chaos/border-foe), and the biogeography rule that fauna maps to land first and myth second; with kotodama hooks — animal names as tabooed, performative, and register-marked language
 - `binding-speech-complex.md` — the binding-speech complex as a designed system for a fictional culture — the four channels (oath, curse, blessing, name-power) treated as one machinery with four directions of binding, the binding triangle (speaker → word → executor) and the maxim that a word holds only where an executor exists; the master channel table (genre, binder, bound party, executor, sanction shape, release, failure mode, visibility); the oath in depth (formula anatomy: invocation / assertion / self-imprecation / uptake; the four enforcement models with attested exemplars; oath institutions — compurgation, the oath ring, the covenant archive, the oath-scroll; the oath-witness slot in a pantheon); the curse in depth (seven curse genres, curse physics: retention, targeting, spillover, reversibility; release and counter-curse); the blessing in depth (irrevocability, the blessing as transferable asset, the curse/blessing asymmetry, the blessing economy); name-power in depth (the name as handle; the four name-operations — speak or withhold, write or erase, rename, refuse; the secret-name institution); the enforcement ledger worked as a design table (divine, automatic, communal, and ordeal enforcement, with the "who pays" question); six release procedures with exemplars; a build protocol; a NON-CANON worked micro-example; and a calibration bank for the contested and discredited readings (Frazerian word-magic evolutionism, the Lévy-Bruhl "primitive mentality" reading, the popular *religio* < *religare* etymology, the "every culture has true names" universal). Reference knowledge and method only; canon decisions belong to lore-shokunin.
 - `celestial-symbolism-calendars.md` — The naked-eye sky as the worldbuilder's highest-yield symbolic system — sun/moon deity gender assignments across cultures (no universal pattern; aspect-switching), the planet-as-god interpretatio chain (Babylonian → Greek/Roman → Germanic/Chinese/Indian/Maya), constellation vs asterism as a naming problem, the Pleiades as the most calendrically overloaded object worldwide, Milky Way figure typology, eclipse-omen systems and their rituals and archives, the mechanics by which celestial cycles anchor calendars and festivals; with a calibration section on discredited celestial-myth schools
@@ -227,6 +235,7 @@
 - `ritual-liminality.md` — The ritual toolkits a worldbuilder uses to generate transitions, exchanges, killings, and time-cycles — van Gennep's three-phase rite-of-passage grammar (separation / liminality / incorporation) applied to life-crisis, territorial and funerary rites; Turner's deepened liminality, communitas vs anti-structure, social-drama four-phase plot engine, liminoid; Mauss's gift (three obligations, hau, kula, potlatch with full colonial-contact calibration); sacrifice theories and a working typology table with substitution logic; calendrical rites (renewal, reversal, intercalation, invented traditions); and the mapping of ritual grammar onto narrative structure (plot skeletons, liminal characters and spaces, performative ritual language) — with build order and calibration throughout
 - `sacred-kingship-mythic-charter.md` — how a myth system legitimates a ruler — the eight legitimation channels (divine descent, incarnation or vessel, delegation from a god, election and acclamation, conquest-and-test, installation rite, marriage-alliance into the divine line, and the regalia as found title-deed) with attested exemplars and the political cost of each; the king's-body-is-the-land's-body doctrine and the rule that it needs an observable channel (flood, harvest, weather, plague, victory) or it is decoration; the failing-king device family (regicide, jubilee or renewal, substitute king, mock king, abdication, interregnum) with a reliability grade per device; dual and co-sovereign slots (the king's two bodies, queen-mother and she-elephant pairs, the priest-versus-warrior split); installation and regalia; taboo and seclusion cost accounting; the stranger-king and the pedigree-distance rule; the re-legitimation toolkit for usurpers and the reception check; and the **royal register** — the speech levels addressed to the ruler, the ruler's own first person, the spokesman institution, name taboos, praise-recitation as performed pedigree (oríkì, royal hymns), and the oath formula — with a build order, a decision record, and a calibration shelf for the Frazer–Hocart divine-kingship tradition. Reference and method only; canon decisions belong to lore-shokunin.
 - `sacred-topography-pilgrimage.md` — the place register of a fictional culture's symbolic grammar — the holy-site typology (natural hierophany: spring, cave, mountain, grove, confluence, meteorite, and the *built* shrine that houses one; relic-bearing site; tomb; oracle seat; boundary/pillar mark; the imperial palladium site), the six properties that make a place holy (theophany, relic, tomb, natural feature, boundary function, miracle archive), the **route as rite** (the journey's separation/liminality/incorporation grammar, the fixed itinerary vs the votive ramble, the station sequence, circumambulation direction, and why the *road* is the entry's real object rather than the destination), the votive and ex-voto economy (the deposited object, the inscribed receipt, the healing archive, the pilgrim badge as a mass-produced token), the shrine institution (who holds the site — guild, lineage, monastic order, state bureau, or a lay trust — and the revenue, custody and access rules that follow), sacred-geography mapping (a culture's holy sites as a diagram: radial, quartered, linear-corridor, or archipelago), access law and the restricted-knowledge boundary (who may go, who may not, and what the worldbuilder must not fill in from a living tradition), and the pilgrimage economy (hostelry, tolls, market, protection of the road) — with a build order, a decision record, and a calibration shelf for the contested and discredited readings (the "pilgrimage is a universal human impulse" claim, Eliade's center-monopoly, the Turner communitas generalisation, and the Mecca-trade projection).
+- `stone-symbolism.md` — the **lithic register** a fictional culture's symbolic grammar runs on stone, gem and metal — the property that makes stone a register at all (a mineral is **stationary, ownable, inheritable, divisible and unforgeable** in a way a plant or an animal is not); the five sign-properties a stone can carry (colour, hardness, fracture, provenance, and **workedness**); the four stone-meaning mechanisms (material property → metaphor, provenance → charter, scarcity → rank, and the container-name fossil); the eight material classes with their attested symbolic loads (the precious/native metals, the gemstones, the ornamental hardstones, the worked industrial stone, the salt and evaporite family, the pigment minerals, the **meteoric and exotic** class, and the carved sacred object); the scarcity ladder that converts a geology into a prestige economy; the lapidary as a trade with a ladder, a mark and a fraud problem; the heirloom rule and the heirloom-dating trap; the mining-and-extraction surface; a build order; a NON-CANON worked micro-example; and a calibration bank (the discredited gem-lore and sympathetic-magic readings, the lapidary's own genre status, the "crystal energy" folk model, and the living-practice rules for jade, pounamu and turquoise). Reference knowledge and method only; canon decisions belong to lore-shokunin.
 - `symbolism-synthesis-method.md` — the core generation method for this category — how to build one fictional culture's coherent symbolic grammar across the five canonical registers (color, animal, number, celestial body, direction) as a single closed correlative system instead of a grab-bag of associations; the consistency rules (one symbol, one primary domain; cross-register alignment; a licensed transformation set for satellite meanings), the change rules (six era-drift mechanisms, date-stamping, the anachronism check), and the symbol-audit checklist that gates every handoff to lore-shokunin
 - `trickster.md` — the trickster as a cross-cultural figure class (Wakdjunkaga, Coyote, Raven, Anansi, Loki, Sun Wukong, Èṣù/Legba, Hermes, Br'er Rabbit) — Hynes's feature set, Radin's Winnebago cycle and its contested evolutionary reading, Hyde's boundary-crosser interpretation, structural and liminal analyses (Lévi-Strauss, Turner, Babcock-Abrahams), institutionalized sacred clowns, and how trickster tales encode the critique of the weak under durable power asymmetry; typology table, design protocol, and calibration flags for building a fictional culture's trickster
 
@@ -541,11 +550,11 @@
   `reports/round-{5,6}/parent-reconciliation.json` receipts and name the drift;
   do not edit the old runners.
 
-Total knowledge entries: 223.
+Total knowledge entries: 224.
 
 Counts checked 2026-10-19 from the repo root:
 `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
-(total 223 files; directory totals 25/26/25/29/24/94).
+(total 224 files; directory totals 25/27/25/29/24/94).
 The inventory counts markers, not verified facts.
 Superseded reading, preserved as the dated record it was: this footer read
 `(total 199 files; directory totals 19/19/18/29/20/94)` from round 20 through
```

## 4. Edit mechanics / invariants

- Insert the revision block immediately above `revision: 2.4 — Round-42` (pre-edit `:5`), one blank line between blocks — the rev 2.2/2.3/2.4 convention.
- `## myth-symbol/ (26)` → `(27)` (pre-edit `:205`).
- Insert the new row after the `sacred-topography-pilgrimage.md` row (pre-edit `:229`) and before `symbolism-synthesis-method.md` (`:230`). Sorted proof: `sacred-topography-pilgrimage.md < stone-symbolism.md < symbolism-synthesis-method.md` (`t` < `y` at char 2).
- `Total knowledge entries: 223.` → `224.` (pre-edit `:544`).
- Footer `(total 223 files; directory totals 25/26/25/29/24/94).` → `(total 224 files; directory totals 25/27/25/29/24/94).` (pre-edit `:546-548`); date stays `2026-10-19`, command unchanged.
- Do not touch the "Superseded reading" paragraph; revs 2.1–2.4 did not append there.
- The row's topic must be byte-equal to the entry file's `- topic:` text — no paraphrase, no truncation. The spare's line is 1346 chars total; the topic payload after `- topic: ` is 1337 chars.

## 5. Verification of Variant A (staged; no corpus write)

- Built `.scratch/c02-stage/`: symlinks to all 223 live entries plus `myth-symbol/stone-symbolism.md` holding the spare's fenced bytes (spare lines 4–218) — 224 files.
- Built `.scratch/c02-readme-2.5.md` by applying §3's edits to a copy of the live README (draft sha256 `8078c4794dbea7705a41034a127c704930ff81f46f73d9e00a36cb5355c4e3d7`; the filed README remains `7c788a1d…`).
- Imported `reports/round-28/readme/sweep.py` and called its own `sweep(patched_text, root_override=stage)` — the filed instrument, not a round runner:

```text
ok True
total_rows 224  total_files 224
missing_from_index []  topic_mismatch []  orphan_rows []  header_drift {}
totals_line 224  totals_ok True
footer {"total": 224, "dir_totals": [25, 27, 25, 29, 24, 94]}  footer_findings []  footer_ok True
myth-symbol {"declared": 27, "rows": 27, "files": 27, "duplicate_rows": []}
new_row_topic_chars 1337 == live_entry_topic_chars 1337
```

- **Limit:** this proves mechanical consistency (rows/files/topic bytes/totals/footer) under A1–A3. It does **not** prove the second entry is substantively non-duplicative; §2 is the evidence that it is not.

## 6. Variant B — no-bump recommendation (preferred on the evidence)

If the integrator accepts the collision:

- No rev 2.5. `corpus/README.md` stays at sha256 `7c788a1d…`, rev 2.4, 223 rows == 223 files, footer `25/26/25/29/24/94`.
- Claim C records `could-not-land-as-declared` with §2 as its citation: the lithic slot is already owned; the spare duplicates it; the spare's absence evidence is stale.
- Coverage does not move (myth-symbol 26, total 223). That is an **unchanged** axis, not a harmed one, provided the round does not claim 224.
- A future coverage move needs a genuinely unowned gap and a re-scoped entry with its own `- topic:`, `- gap filled:` and sources. This seat cannot invent one (no fabrication).

## 7. Decision left to the integrator

1. **Re-scope?** If the C01 spare is re-scoped to a genuinely unowned topic, regenerate this diff from the new topic line and filename. The structural edits in §4 still hold: myth-symbol header +1, totals +1, footer vector +1 in slot 2.
2. **No re-scope?** Adopt Variant B; do not issue rev 2.5; record the claim as blocked with §2.
3. **Land anyway under `stone-symbolism.md`?** Apply §3 verbatim, then also repair the spare's stale `- gap filled:` (`C01-mineral-spare.md:7`) and `- verified-at:` (`:24`) before staging — they contradict HEAD. The claim's "applied unmodified" threshold is unsafe as written.

## 8. Integrity

- Writes: this out file only under `reports/round-43/`; scratch artifacts under `.scratch/c02-*` (TMPDIR). `git status --porcelain` → `?? reports/round-43/` only; no tracked file modified.
- No corpus staging, no filed-byte edit, no round-runner execution, no git mutation, no network.
- The O-claim resolver/selftest work belongs to other seats; I did not touch `tools/harness/`.
- Unknowns: none asserted. The target filename is a **proposal** (`reports/round-42/plan/P01-plan.md:358`), not a contract assignment — flagged, not fabricated.
