# ScoutSurface97 — claim C coverage surface and adjacency (2026-11-05)

Seat: ScoutSurface97 (read-only sweep; wrote only this stage). Base tree 1ffc5a83d2c70e3bc581594efbcf32c562ba2569.

## 1. Frozen sweep record (sweep-control.py)

Command: `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-97/sweep-control.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin` — rc 0, output verbatim:

```
R96-REPLAY base=0539276c0e329743200b60e98bf289c540f78864 files=267 owners=2 ['corpus/knowledge/myth-symbol/binding-speech-complex.md', 'corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md']
R97-BASE base=1ffc5a83d2c70e3bc581594efbcf32c562ba2569 files=268 owners=0 []
SWEEP-CONTROL: PASS (round-96 replay must find >= 1 owner)
```

R97-BASE owners=0 as expected: no file other than the (not yet existing) entry owns any frozen phrase on a topic line or heading.

## 2. Body sweep (16-term pattern, case-insensitive)

Command: `grep -rn -i -E 'flyting|senna|verbal duel|ritual insult|song duel|boast|taunt|invective|hija|the dozens|izibongo|halay|insult poetry|contest poetry|nith|lampoon|satire' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge` — rc 0, **59 matches in 32 files** (full listing in §4; per-line matched tokens from `grep -o` rerun, rc 0).

Token histogram (`grep -rn -i -o -E <same> | awk | sort | uniq -c | sort -rn`, rc 0):

```
     24 satire / 14 nith / 9 senna / 7 boast / 3 invective / 3 flyting / 3 Hija
      2 Satire / 1 the dozens / 1 taunt / 1 lampoon / 1 izibongo / 1 hija / 1 Senna
```

False-positive tokens: `nith` inside *zenith/senith* (persia-sasanian 19,98,111,203; celestial-symbolism-calendars 143,149; direction-symbolism 82); `Senna` in *Sennacherib* (israel-ancient-hebrew 181); `Hija`/`hija` in *Hijazi/Hijaz/hijab* (islamic-caliphate-arabic 11,156; music-instrument-lexicon 48,65); `Satire` = Persius *Satires* in two source lists (dress-through-eras 4; ritual-garments 11).

Heading/topic owner check: rerunning the same 16-term grep and counting lines whose content starts `#` → **0** (rc 0); starting `- topic` → **0** (rc 0). So every one of the 59 hits is body prose, a list item, or a table cell — passing mention or substantive section, never an ownership surface. Consistent with §1 (owners=0 for the frozen six).

Frozen-phrase status at base: `verbal duel` 0 hits; `ritual insult` 0; `song duel` 0; `boast formula` 0; `audience adjudication` 0; `flyting` 3 hits (orality-formulaic-language.md:112 list item; myth-symbol/trickster.md:25 and :62 table row / body line). Matches claims.json before-state exactly.

Entry absence: `test -e corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` → rc 1 (absent). ✓

## 3. Classification of the 59 hits

Classes: **owner** = on `- topic:` line or `#` heading (none exist); **S** = substantive section (a paragraph/list/table row a reader would consult for the topic); **P** = passing mention; **FP** = false-positive token match.

| File:line | Token(s) | Class | Note (line content) |
|---|---|---|---|
| linguistics/orality-formulaic-language.md:112 | flyting, senna×2 | S | "competitive forms (Scottish flyting; Lokasenna-style senna)" — performer-licensing item in §8 design checklist |
| linguistics/orality-formulaic-language.md:60 | izibongo | S | Nguni izibongo praise poetry as social formula (Barber 1991; Opland 1983) |
| linguistics/orality-formulaic-language.md:127 | satire | P | "satire of bad poets" as metadiscourse (Agha 2007) |
| myth-symbol/trickster.md:35 | senna×2 | S | "Lokasenna belongs to the *senna* (institutionalized insult-freestyle)" |
| myth-symbol/trickster.md:62 | flyting, senna | S | transformer spectrum ends at "pure flyting clown (Lokasenna)" |
| myth-symbol/trickster.md:69 | the dozens | S | pragmatics of indirection — "insult, pun, … the dozens"; Gates 1988 |
| myth-symbol/trickster.md:25 | senna (Lokasenna), flyting | P | Loki typology table row: "flyting at Ægir's feast" (table cell) |
| myth-symbol/trickster.md:4 | senna (Lokasenna) | P | sources list |
| civilizations/arabia-pre-islamic.md:69 | boast | S | Fakhr (self/group praise) qaṣīdah mode table row |
| civilizations/arabia-pre-islamic.md:71 | invective | S | Hijāʾ (invective) qaṣīdah mode table row: "Reputation is contested through language" |
| civilizations/arabia-pre-islamic.md:74 | boast | P | nasīb → raḥīl → praise/boast teaching-model caveat |
| linguistics/oath-blessing-curse-formulae.md:84 | satire | S | S979 "the seven requirements which compose any satire (cach n-aír) are" — satire as composed curse genre |
| linguistics/oath-blessing-curse-formulae.md:120 | satire | S | same S979 quote reused in §6 sanction-clause section |
| linguistics/oath-blessing-curse-formulae.md:59 | boast | P | underfilled oath formula "will read as a boast, a threat or a prayer" |
| civilizations/yoruba.md:123 | satire | S | Ẹ̀fẹ̀ satire/song vs Gelede dancing sequencing |
| civilizations/yoruba.md:130 | satire | S | "Sculpted satire and sung commentary can address the same social issue" (table row) |
| civilizations/yoruba.md:136 | satire | S | design transfer: "build a local satire genre whose sanctioned voice … agree" |
| culture-material/masks-masquerade.md:41 | satire | S | one-owner boundary row: Gẹ̀lẹ̀dẹ́ satire performance account stays at yoruba.md:136 |
| culture-material/masks-masquerade.md:80 | lampoon | S | Sri Lankan kolam "the form licenses lampooning officials" (S257) |
| civilizations/celts.md:50 | satire | S | Diodorus 5.31 praise/satire singers (bards) |
| civilizations/celts.md:74 | satire | S | Bres's provisioning failures bring complaint and satire |
| civilizations/celts.md:76 | satire | S | "praise, satire, vows … can alter reputation or obligation" |
| civilizations/celts.md:179 | satire | S | authority through trained speech: apprenticeship, praise/satire, patronage |
| civilizations/balts.md:148 | satire | P | dainas cover "work, seasonal observance, … satire, and erotic material" |
| civilizations/china-ming.md:145 | satire | P | "without making satire a doctrinal manual" (table cell) |
| civilizations/fon-dahomey.md:89 | satire | P | "Song, praise, irony, satire, and instruction" (table cell) |
| civilizations/fon-dahomey.md:164 | satire | P | "distinguish royal praise from neighborhood satire" (design item) |
| civilizations/germanic-norse.md:68 | boast | P | "the same alphabet can serve a prayer, boast, memorial …" |
| civilizations/japan-edo.md:115 | boast | P | "a customer's boast" in register-profile example |
| myth-symbol/creation-myths-taxonomy.md:49 | boast | S | "boasting about one's contribution is the tabooed speech act" (diving-species coupling) |
| culture-material/pastoralism-animal-husbandry.md:152 | taunt | S | "the farmer taunts the herder" — herd-accounting taunt as poetry (S064, table cell) |
| myth-symbol/marriage-alliance-bridewealth.md:44 | boast | P | passing mention inside long marriage-pool table row |
| myth-symbol/hero-journey-variants.md:112 | satire | P | "a rival city's satire" as curator of founder scores |
| myth-symbol/number-symbolism.md:28,85 | senna (Lokasenna) | P | Loki 13th-guest calibration; poem named, not taught |
| culture-material/agrarian-field-system-lexicon.md:104 | satire | P | "agricultural extension satire live" in failed-crop note |
| culture-material/calendar-festival-systems.md:73,149 | satire | P | Hogarth grievance satire (calendar riots myth) |
| culture-material/cuisine-food-lexicon.md:92,150 | invective | P | Peter Damian's late invective as fork-anecdote source |
| culture-material/dress-through-eras.md:4 | Satire | FP/P | Persius, Satires in source list |
| culture-material/ritual-garments.md:11 | Satire | FP/P | Persius, Satires 5.30–31 in source list |
| civilizations/islamic-caliphate-arabic.md:11 | Hija | FP | *Hijazi* origins (Quranic reading traditions) |
| civilizations/islamic-caliphate-arabic.md:156 | hija | FP | *hijab* dress caution |
| culture-material/music-instrument-lexicon.md:48,65 | Hija | FP | maqam *Hijaz* (toponym as mode name) |
| civilizations/israel-ancient-hebrew.md:181 | Senna | FP | *Sennacherib* synchronism |
| civilizations/persia-sasanian.md:19,98,111,203 | nith | FP | *zenith/senith* (sky-alignment calibration) |
| myth-symbol/celestial-symbolism-calendars.md:143,149 | nith | FP | *zenith-passage* |
| myth-symbol/direction-symbolism.md:82 | nith | FP | *zenith* ten-directions row |
| synthesis/glossary-registry-format.md:137 | satire | P | `courtly` glossary row: "mocked in satire" |
| synthesis/taboo-euphemism-lifecycle.md:154 | satire | P | satire in preservation/revival mechanism list |

Summary: 0 owners; 22 substantive; 30 passing; 7 false-positive-token hits. **Zero topic-line or heading owner of any of the six frozen phrases anywhere in corpus/knowledge — claim C's zero-owner premise holds by content, not by filename.**

## 4. Adjacency table — boundary the new entry must respect (defer, do not restate)

| Neighbour (evidence lines read) | What it owns | Boundary for verbal-duelling-ritual-insult.md |
|---|---|---|
| linguistics/orality-formulaic-language.md (55–130 read; :112 key) | the oral-formulaic register machinery: meter, epithet sets, type-scenes, performer licensing, enregisterment; flyting+senna appear only as two words inside its licensing checklist item | defer meter/formula engineering and performer-licensing inventory to it; the new entry treats flyting/senna as *contest genres with rules*, cites :112 as the hook it fills, and does not edit that file (not claim C's write surface) |
| myth-symbol/trickster.md (1–75 read; 25/35/62/69 key) | the trickster *figure*: genre slots ("Lokasenna belongs to the *senna*"), flyting-clown slot, indirection pragmatics incl. the dozens + Gates 1988 | trickster keeps figure/mask and the signifying-monkey theory; new entry defers the dozens' pragmatics-of-indirection framing to :69 and treats the dozens as an adjudicated insult game with rules and stakes; cross-cite, no restatement of Gates |
| civilizations/arabia-pre-islamic.md (58–80 read; 69/71/74 key) | the qaṣīdah mode system incl. Fakhr (boast) and Hijāʾ (invective) rows; "do not turn every insult into an ethnographic fact" | cite hijāʾ/fakhr as one lineage in the taxonomy table; the ode's mode table, nasīb→raḥīl order and its calibration stay there |
| myth-symbol/binding-speech-complex.md (topic + §3–§5 read) | the binding-speech complex: oath formula anatomy (invocation/assertion/self-imprecation/uptake), enforcement ledger, curse genres/physics; topic line carries self-imprecation; notes "Norse *níð* and *blessan* are opposed formulas" (:80) | when words *bind* (níð, satire with legal force, curse-duels), defer enforcement/ledger machinery to it; new entry keeps the licensed-contest side (frames, stakes, adjudication, release from the frame) |
| linguistics/oath-blessing-curse-formulae.md (55–125 read; 84/120 key) | formula slot grammar (5 slots) and the Irish satire-as-curse requirement set (S979 "seven requirements which compose any satire") | the juridical/binding requirements of satire stay there with S979; new entry may reference the cause-grammar idea but must not restate the slot model or re-mine S979's content into new rows |
| linguistics/politeness-taboo-euphemism.md (104–123 read; :114 key) | politeness/taboo/enregisterment machinery; satire appears as one metadiscourse item | "rules that keep insult ritual" section is about contest rules (license, occasion, stakes, riposte rights), not politeness scoring; metadiscourse/enregisterment defers to :114 (Agha 2007) |
| linguistics/sociolinguistics-registers.md (55, 137 seen) | stereotype/marker/indicator; satire as metadiscourse quotes | passing adjacency; register-policing recipe defers to it |
| civilizations/yoruba.md (123/130/136) + culture-material/masks-masquerade.md (:41 one-owner row, :80) | Gẹ̀lẹ̀dẹ́ satire performance account (yoruba.md:136; masks entry already declares "the performance account stays there"); kolam lampoon license | new entry follows the corpus's one-owner-boundary convention: cite Gelede as a masked-satire lineage in its table, costume/performance detail stays in the two owners |
| civilizations/celts.md (50/74/76/179) | bardic praise/satire as Celtic institution (Diodorus; Bres tale) | cite as an instance row; Celtic institutional detail (apprenticeship, patronage) stays there |

## 5. Proposed entry skeleton (10 h2; ≥ 6 required) with frozen-phrase placement

Frozen phrases to place in h2 or table data rows (C1 needs ≥ 4): all six placed, five in headings, one duplicated in the taxonomy table.

- `- topic:` line byte-equal to the frozen topic (C1), then `sources:` block (new S985+ rows cited by id, in-corpus cross-references by path), `couples:`, `verified-at:`, `recheck:` — header block per corpus convention (trickster.md/oath entry pattern).
- `## 1. The verbal duel: contestants, occasion, and frame` — **"verbal duel"**; defines contest vs quarrel; stakes tied to contestants, judges, occasions (topic promise).
- `## 2. Flyting and senna: the northern evidence` — **"flyting"** (+ senna; Lokasenna at Ægir's feast, Dunbar–Kennedie; license, venue, wager).
- `## 3. Ritual insult across traditions` — **"ritual insult"** (+ hijāʾ, Gelede, kolam lampoon as cited instances; boundary notes per §4).
- `## 4. Song duels: adjudicated singing contests` — **"song duel"** (substring in heading ✓; Inuit drum duels etc.).
- `## 5. The boast formula: genealogy, deed, and hazard` — **"boast formula"**; slot-filling praise→claim→wager grammar (defers slot theory to oath entry, cites oríkì/izibongo :60).
- `## 6. Audience adjudication: judges, uptake, and outcome` — **"audience adjudication"**; who decides a win, what a loss costs.
- `## 7. The rules that keep an insult ritual rather than real` — license, cause grammar (pointer to binding-speech §5.3), off-switch rituals, relation-vs-fact calibration (arabia :71 caveat).
- `## 8. One-owner boundary table` — the §4 adjacency rows in corpus table form (masks-masquerade.md:41 convention).
- `## 9. Design procedure: a fictional word-contest` — build checklist + worked micro-example (corpus style); stakes bound to contestants/judges/occasions.
- `## 10. Calibration flags` — contested claims, commonly botched (e.g. "Norse Loki 13th guest" style modern tallies; number-symbolism:85 already flags Lokasenna misuse).

Taxonomy table (≥ 5 data rows × ≥ 3 cols; 7 rows planned): `| Tradition | Form and venue | Formula grammar | Adjudication and stakes |` — rows: Scottish flyting; Norse senna; Arabic hijāʾ/fakhr; Inuit song duel; the dozens; Gẹ̀lẹ̀dẹ́ satire (cross-ref); Irish satire-aír (cross-ref, binding side deferred). Table data rows can double-carry "ritual insult" / "audience adjudication" for phrase-count headroom.

Registry plan feeding C2: rows S985+ (highest current S984, SOURCES.md:941; S980–S984 pattern: `| S98x | Author Year, title, venue — URL | type | A|B | topics | body text; reports/round-9N/evidence/S98x.txt; exact locator: "…" | calibration | mined | 2026-11-05 | 180d | <used-by path> |`), `used-by` exactly `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md`, captures under reports/round-97/evidence/.

## 6. Planner data-walk: partition counts

`find corpus/knowledge -name '*.md' | awk -F/ '{print $(NF-1)}' | sort | uniq -c` (rc 0):

```
     95 civilizations
     43 culture-material
     41 linguistics
     36 myth-symbol
     29 synthesis
     24 verification
```
Total 268 files (`find … | wc -l`, rc 0). **linguistics/ is the right partition**: (a) the neighbouring genre-of-speech entries (oath-blessing-curse-formulae, orality-formulaic-language, politeness-taboo-euphemism, sociolinguistics-registers) already live there and the frozen phrases are formula-grammar/pragmatics vocabulary, not one civilization's dossier; (b) the S-series tail this entry extends (S975–S984) is currently used by a linguistics/ entry (oath-blessing-curse-formulae.md), so S985+ continues that evidence chain; (c) topic scope is cross-cultural contest speech with a design procedure — the linguistics/ house style, not myth-symbol (no deity/figure required) and not civilizations (no single culture).

## 7. Files read

reports/round-97/claims.json (whole); reports/round-97/predispatch.py:1-63; sweep-control output (§1); orality-formulaic-language.md:55-130; trickster.md:1-11, 20-72; arabia-pre-islamic.md:58-80; oath-blessing-curse-formulae.md:55-125; politeness-taboo-euphemism.md:105-120; masks-masquerade.md:38-44,78-82; binding-speech-complex.md grep (satire/oath/curse/formula, rc 0) + :1-6; SOURCES.md grep S98x (rc 0, rows S980–S984 at :937–:941).

Tools installed/updated this seat: none. Nothing committed; no file outside my stage touched.
