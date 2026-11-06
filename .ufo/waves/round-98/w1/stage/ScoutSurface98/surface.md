# ScoutSurface98 — coverage surface for claim C (toasts and drinking-speech formulae)

Lane: kotodama-shokunin, round 98 w1. Read-only sweep of `corpus/knowledge` (270 `.md` files seen on disk; index counts 269 committed rows — one file may be mid-write by another seat, see §7). Frozen context read first: `reports/round-98/claims.json` and `reports/round-98/predispatch.py:1-63` (+ `predispatch-base.txt`). No frozen file was edited. Scratch `/fast/scratch/hyaku/kotodama-r98/ScoutSurface98/` was created and deleted before yield; nothing else was written outside this stage dir and the Report file.

## 1. Method and the exact commands (all cwd = /home/vgpnk/Projects/shokunin)

Broad sweep, as assigned (kept unbound deliberately, to quantify the noise the narrowed runs remove):

```
grep -rn -i -E 'toast|wassail|waes ?hael|drinc ?hael|bragaf|bragarf|minni|libation|health|symposi|symposiarch|tamada|supra|skål|skal|kanpai|ganbei|l.chaim|cheers|sláinte|prosit|propin|loving cup|stirrup cup|drinking horn|mead|ale|kylix|krater|oath-cup|boast' corpus/knowledge | wc -l
→ 2707   (rc 0)  # noise-dominated: substring 'ale' in scaled/sales/Alexander-class words
```

Narrowed sweeps (word boundaries fix `ale`/`mead`/`skal`/`supra`; `health` narrowed to `\bhealths?\b` which still needs per-hit classification because "health" is a common noun; all rc 0 unless stated):

```
grep -rn -i -E '\btoast(s|ed|ing)?\b|\btoastmaster\w*' corpus/knowledge                                  → no matches (rc 1)
grep -rn -i -E 'wassail(s|ing)?|waes ?hael|drinc ?hael|\bkanpai\b|\bganbei\b|\bgan bei\b|\bcheers\b|sláinte|\bprosit\b|\bpropin\w*|l.?chaim|\bskål\b|\bskal\b' corpus/knowledge   → no matches (rc 1)
grep -rn -i -E '\bbragaf\w*|\bbragarf\w*|\bminni\b|\bloving cup\b|\bstirrup cup\b|\bdrinking horns?\b|\boath-?cups?\b|\bboast(s|ing|ed)?\b' corpus/knowledge   → "grep: 21 matches in 7 files" (all of them `boast`; the other six alternatives = 0, verified on the capture artifact)
grep -rn -i -E '\blibations?\b' corpus/knowledge        → "grep: 7 matches in 4 files" (rc 0)
grep -rn -i -E '\bhealths?\b' corpus/knowledge          → "grep: 47 matches in 26 files" (rc 0)
grep -rn -i -E '\bsymposi\w*' corpus/knowledge          → "grep: 4 matches in 4 files" (rc 0)
grep -rn -i -E '\bsupra\b|\btamada\b' corpus/knowledge  → "grep: 5 matches in 4 files" (rc 0; all `supra-local` linguistic sense; tamada = 0)
grep -rn -i -E '\bmeads?\b|\bales?\b' corpus/knowledge  → "grep: 10 matches in 6 files" (rc 0)
grep -rn -i -E '\bkylix\b|\bkrater\b' corpus/knowledge  → "grep: 4 matches in 1 file" (rc 0)
grep -rn -i -E '\brhyton\w*|\bskyphos\w*|\bkantharos\w*|\bealu\b|\bmedu\b' corpus/knowledge             → 1 match (vessel:51 skyphos; the rest rc-miss) (rc 0)
grep -rn -i -E '\bfeast(s|ing|ed)?\b|\bbanquet(s|ing)?\b|\bcarous\w*' corpus/knowledge                  → "grep: 120 matches in 38 files" (rc 0; SUPPLEMENTARY terms, not in the assigned list)
```

Two attribution runs used `-o -n` to bind each hit to its exact term, and `grep -o … | sort | uniq -c` for per-file term frequency. An earlier per-file breakdown without `\b` (my command) produced `25 ale` for greece-classical etc. — that is substring noise (`Alexander`, `scaled`), superseded by the boundary runs; recorded here because the noisy number is mine.

Owner check (leg C8 guard, content-level): zero owners of any frozen phrase in a heading or `- topic:` line of any knowledge file other than the (not yet existing) entry:

```
grep -rn -i -E '(^#|^- topic:).*\b(libation|toast|wassail|health-drinking|drinking oath|toastmaster|bragaf|minni)\b' corpus/knowledge
→ no matches (rc 1)
```

`health-drinking` specifically: 0 anywhere (`grep -o -i -E '\bhealths?\b'` output inspected; no `health-drink` substring in the capture).

## 2. Result: the claim-C surface is empty, as frozen

Zero-hit terms across the whole corpus (each verified by a named command above, rc 1 or 0-alternative-miss): **toast, toastmaster, toasting, wassail, wæs hael, drinc hael, kanpai, ganbei, cheers, sláinte, prosit, propine/propination, l'chaim, skål, skal, bragafull, bragarfull, minni, loving cup, stirrup cup, drinking horn, oath-cup, tamada, health-drinking, rhyton, kantharos, ealu, medu**. `toast-drinking-speech-formulae.md` does not exist (linguistics listing, 42 files). This matches claims C "before" (0 files for toast/wassail/bragaf/toastmaster/health-drink; libation in 4 files) — my measurement agrees on the 4 files (ainu, funerary, vessel, death-afterlife) and finds 7 occurrences, not 4 (vessel carries libation at `:5`, `:36` **and** `:38`; death-afterlife at `:41` and `:100`).

## 3. Hit classification (every boundary-true hit, term in parentheses)

**Owner (heading/topic carries the subject):**
- `linguistics/verbal-duelling-ritual-insult.md` — `boast`: topic `:15`, scope `:20`, `## 6. The boast formula: claim, warrant and wager` `:110`, body `:112,:114,:116,:118,:119,:120,:122`, failure `:199`, procedure `:228`, worked example `:243`, handoff `:255`. Sole owner of boast-as-contest-speech. (Not a frozen phrase → no C8 conflict.)

**Substantive section (hit inside a body that teaches adjacent machinery):**
- `linguistics/oath-blessing-curse-formulae.md` — `boast` at `:59` inside the slot-discipline bullet: an oath formula with slots unfilled "will read as a boast, a threat or a prayer". The entry owns performative slots (performative verb, witness invocation, assertion, sanction clause, uptake; sources S975–S98x) and names boast only as a failure mode.
- `culture-material/vessel-container-lexicon.md` — `libation` `:5` (couples line), `:36` (SERVING table row: krater, oinochoe, kylix, *phiale* (libation dish)), `:38` (ritual extension: *phiale* and *patera* for libation); `kylix`/`krater` `:3,:36,:48,:55`; `skyphos` `:51`. Owns vessel names, naming grammar, emic/etic labelling.
- `culture-material/cuisine-food-lexicon.md` — `health` `:103` (ṣaḥtayn "two healths"), `:104` (afiyet olsun "may it be health") as **table cells of the pre/post-meal formula table (§6)** — the closest existing thing to drinking wishes, owned as *eating* etiquette; `ale` `:153` (calibration: ale/beer dominance ≠ bad water), `:18` (source line); feast h2 `:47` and topic line 1.
- `myth-symbol/death-afterlife-eschatology.md` — `libation(s)` `:41` (offering economy of the diminished shadow: "libations, food, the pouring of water — the dead are fed"), `:100` (libation as one *medium of transfer* in the ancestor-economy bullet).
- `culture-material/funerary-material-culture.md` — `libation` `:8` only inside the KTD-MMC-S-0002 in-corpus source bullet quoting vessel:38 (passing cross-reference, but the entry owns grave-assemblage vessels).
- `civilizations/ainu.md` — `libation` `:109`: table row "`ikupasuy` and `tuki` | Libation stick and lacquered cup used in prayer communication … Distinguish handling, speech, and offered drink". The corpus's one implement-level libation anchor, inside a civ reference entry.
- `civilizations/germanic-norse.md` — `boast` `:68` (register list: prayer, boast, memorial, shopping message — passing), `mead` `:95` (kenning table "poetry-mead" — substantive but kenning-decoding context, not a rite).
- `culture-material/furniture-interior-lexicon.md` — `symposium` `:52` (dining couch "belonged to the symposium", Richter 1966; Dunbabin 2003; middle/left couch rank at §3 `:56`); `health` `:16,:102` non-subject. Owns the *seating* of the drinking party, not its speech.

**Passing mention (no adjacency duty):**
- `boast`: `civilizations/arabia-pre-islamic.md:69,:74` (qasida fakhr), `civilizations/japan-edo.md:115` (registers), `myth-symbol/creation-myths-taxonomy.md:49` (dive-credit taboo), `myth-symbol/marriage-alliance-bridewealth.md:44` (substring-level hit; line shows marriage-pool table).
- `ale`: `culture-material/craft-artisan-lexicon.md:11,:111` and `culture-material/trade-economy-lexicon.md:49` — all "Assize of Bread and Ale (1266)", i.e. metrology/enforcement history.
- `mead`: `civilizations/maori.md:7,:47,:115` — author surname *Mead (2003)* (content-level false positive).
- `health`: ~45 further matches in 25 files (bathing-and-body-hygiene `:26,:27,:60,:86` incl. h2 "## 8. Health, medicine and the hygiene revolution"; dine-navajo `:19,:57`; inuit `:118,:191`; benin `:154`; polynesia `:135`; sogdian `:63` "extravagant health wishes … likened to that offered to gods" — letter-formula context, worth a look when sourcing; vietnam `:92`; india-tamil-sangam `:103`; dress `:141`; era `:77`; et al.) — all generic wellness/medicine senses, none cup-adjacent except sogdian `:63` and cuisine `:103,:104`.
- `supra`: 5 matches — `supra-local` in amazonia `:42,:121`, arabia `:59`, inca `:31`, mississippian `:60`. Zero Georgian-feast sense.
- `symposium`: 3 of 4 matches are "*Textile Society of America Symposium Proceedings*" (publication titles, inca `:187`, japan-edo `:27`, ritual-garments `:12`).
- Supplementary `feast/banquet` (not assigned; context only): 120 matches in 38 files. Notables: `civilizations/pacific-northwest.md` owns **feast-speech** (recheck `:8`, evidence distinction `:91`, Boas/Hunt 1921:788–793 Kwag'ul sequence `:14,:77,:80,:103,:181`) — ceremonial oratory at a feast, owned there; `myth-symbol/trickster.md:25` flyting "at Ægir's feast" (Lokasenna row); `civilizations/etruria.md` banquet imagery `:117,:118,:131`; `civilizations/mongol.md:116,:135` Rubruck feast days; `civilizations/thrace-dacia.md` h2 "## Getic tomb-feast symbolism" `:98`; `civilizations/slavs-early.md:117`; `myth-symbol/sacred-kingship-mythic-charisma.md`→`sacred-kingship-mythic-charter.md:98` king of the feast. None carries a frozen phrase.

**Boundary-true zero-hit files that were expected to be adjacent:** `myth-symbol/guest-right-hospitality-law.md`, `linguistics/petitionary-and-votive-formulae.md`, `linguistics/greeting-leave-taking-formulae.md`, `civilizations/greece-classical.md`, `civilizations/pacific-northwest.md` — 0 boundary-true term matches each (verified by the `-o -n` attribution run over all five). They are adjacent by **content**, not by these terms (§4).

## 4. Adjacency table — what the new entry must defer, not restate

| File | What it already owns | Boundary for `toast-drinking-speech-formulae.md` |
|---|---|---|
| `linguistics/oath-blessing-curse-formulae.md` | Performative slot grammar (performative verb, witness invocation, assertion, sanction clause, uptake); frame-is-heritage/assertion-is-living; blessing = transfer not wish (§2–§3); boast as failure mode `:59` | Defer the slot anatomy. The **drinking oath** section reuses those slots and adds only the cup-borne occasion (pledge over drink, self-imprecation witnessed by the cup/companions); cite, do not re-derive |
| `linguistics/verbal-duelling-ritual-insult.md` | Boast formula (framing/claim/warrant/stake, §6 `:110-122`), flyting/senna genres, audience adjudication; explicit deferral list §1 `:20-27` | Defer boast anatomy. **Boast-cup** = the cup as the wager/stake-token of a boast inside a drinking frame; the sumbl-style sequence where boasts ride the cup belongs here, the slot math stays there |
| `linguistics/petitionary-and-votive-formulae.md` | Vow = conditional self-binding debt ("a vow is a debt the culture can collect on"); votive inscription grammar; petition vs vow split (§1) | Defer vow mechanics. **Libation and the pledge** section distinguishes deity-ward pouring (votive-adjacent) from peer-ward toasting (exchange), and cites the vow-debt frame for "drink and promise" rites |
| `myth-symbol/guest-right-hospitality-law.md` | Hospitality as sacral-legal institution; **"shared cup" named as a bond-opening marker** in the topic line `:3` (threshold, first morsel, shared cup, parting gift); breach ladder; host package | Defer the bond grammar. The new entry owns the words spoken *over* the shared cup (welcome toast, refusal, penalty cup) and cites the guest-right marker for why the cup carries bond force; refusal-of-cup links to its breach ladder by reference |
| `culture-material/vessel-container-lexicon.md` | Vessel jobs (SERVING row `:36` with krater/kylix/phiale), six naming strategies `:44-51`, emic/etic rule `:55`, ritual extension `:38` | Defer all vessel-name morphology and typology. Use cup words as props only; when naming a fictional ritual cup, point at its naming-strategy table instead of re-teaching it |
| `culture-material/cuisine-food-lexicon.md` | Pre/post-meal formula table (§6 `:100-108`, incl. health-wishes `:103-104`), feast/famine `:47`, ale/beer calibration `:153`, table grammar | Defer eating-side formulae and foodway calibration. The new entry is the **drink-side bracket** (the cup, not the meal); cross-cite the ṣaḥtayn/afiyet rows as the eating-register analogue of the health-wish |
| `linguistics/greeting-leave-taking-formulae.md` | Greeting/farewell speech acts, access rituals (topic `:3`; sources S961–S964) | Defer greeting machinery. waes hael is historically a greeting-formula case; the new entry may *cite* it as the boundary case (toast as greeting) without re-teaching politeness/access rules |
| `culture-material/furniture-interior-lexicon.md` | Symposium seating (kline, regimes, rank-by-position `:48-56`) | Defer the room. The **toast sequence** section owns the order and offices of speech, and cites furniture for posture/seating constraints |
| `myth-symbol/death-afterlife-eschatology.md` | Libation as offering medium to the dead `:41,:100` | Defer the dead-ward offering economy. New entry covers the living-ward speech act; one cross-ref row where a toast is poured to the dead (libation-drops) |
| `civilizations/ainu.md` | ikupasuy/tuki libation implements `:109`, "distinguish handling, speech, and offered drink" | Exemplar only; do not generalize Ainu practice into a template; cite `:109` as the implement-level anchor |
| `civilizations/germanic-norse.md` | Poetry-mead kenning `:95`; boast as register `:68`; reference-base entry ("methods, never canon") | Exemplar material for bragafull/minni/drinking-oath *when sourced fresh* this round (the entry itself has none of it — no minni/bragafull content exists in-corpus, so nothing to restate) |
| `civilizations/pacific-northwest.md` | Feast-speech sequence (potlatch oratory, `:8,:91,:103`) | Defer feast-oratory scope to it; the toast entry covers cup-bound speech, not potlatch registers |

No other file needs a boundary: greece-classical has **no** symposium/krater/kylix/libation content (0 boundary hits), so the Greek symposium speech-side is unowned and available.

## 5. Entry skeleton (proposed; ≥6 h2, frozen-phrase placement)

Topic line: the frozen topic line, byte-equal, as `- topic:` in frontmatter (per house convention seen in oath/duelling/guest-right entries).

1. `## 1. The gap this entry fills — no corpus entry owns the words spoken over the shared cup` — negative sweep receipt (the §1/§2 numbers), gap statement, scope/deferral list in the duelling-entry style (`It explicitly does not own: …`).
2. `## 2. The toast formula: the speech-act slot pattern of drinking together` — **"toast formula"** in h2. Slots: the standing occasion, the filled cup, the named addressee(s), the wish/claim content, the simultaneous drink (uptake-by-sipping), the permitted response formula. Cross-ref oath slots; keep design-not-sourced labels.
3. `## 3. Health-drinking: the cup as the vehicle of a wished state` — **"health-drinking"** in h2. waes hael/drinc hael exchange, ṣaḥtayn/afiyet olsun (cite cuisine rows), prosit/sláinte/kanpai/ganbei/skål as one family map; differentiation of wished-for content (health, love, the dead, the sovereign).
4. `## 4. Libation and the pledge: the god's share and the promise made wet` — **"libation"** in h2. Deity-ward pour vs peer-ward toast; ainu ikupasuy/tuki `:109` as implement anchor; pledge = vow spoken over drink (cross-ref petitionary vow-debt); drop-for-the-dead cross-ref to death-afterlife.
5. `## 5. The toastmaster's office and the order of a toast sequence` — **"toastmaster"** and **"toast sequence"** in h2 (two frozen phrases in one heading is allowed by C1 counting, but keep the table too). Tamada/supra (Georgian), symposiarch (Greek), presidency of the order; sequence grammar: opening/official/personal rounds, who may propose whom, the closing cup; furniture cross-ref for seating rank.
6. `## 6. The drinking oath and the boast-cup` — **"drinking oath"** in h2. Cup-solemnized vows (sumbl-style rounds), minni (memory-toast) and bragafull/bragarfull (boast-cup) as the Germanic pair — sourced fresh this round, nothing in-corpus to restate; defer boast slots to duelling §6, oath slots to oath §2.
7. `## 7. Refusal, reciprocity and the penalty cup` — refusal of the cup as speech act (what a refusal asserts), reciprocity chains (one-toast-debts-a-toast), penalty/fine cup as institutionalized sanction; guest-right cross-ref (shared cup as bond marker `:3`; breach ladder).
8. `## 8. Design procedure — a fictional drinking rite whose words stay tied to its hosts, guests, cups and occasions` — the handoff procedure + the required table.

Required table (C1: ≥5 data rows × ≥3 cols) — proposal, "the toast-sequence order table", placed under §5 or §8:

| Stage | Office/who speaks | Words the stage carries | Cup action | Refusal/exit option |
|---|---|---|---|---|
| opening | host or toastmaster | welcome + health wish to the house | fill and raise, no sip yet | guest may arrive late, not refuse the opening |
| deity share | toastmaster or priest | the pledge / god's share naming | first pour out, not drunk | non-believer may pour silently (design choice) |
| official round | toastmaster (tamada) | the named theme, ranked addressees | drink on the theme's last word | may drink shallow, may not speak over |
| personal round | any guest, recognized in turn | reply-toast quoting the theme | sip + return the wish | may pass the turn forward |
| memory/boast cup | any qualified speaker | minni (memory) or the boast+warrant | full cup, drained | refusal asserts enmity (links guest-right breach) |
| penalty cup | wronged party or office | the named fault and the fine | drunk in one, no reply | refusal converts penalty to feud |

Couples block (house convention): oath-blessing, verbal-duelling, petitionary-votive, guest-right, vessel-container-lexicon, cuisine-food-lexicon, greeting-leave-taking, furniture-interior-lexicon, death-afterlife-eschatology, synthesis/worldbible-integration-contract.

## 6. Partition counts and why linguistics

```
find /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge -name '*.md' | awk -F/ '{print $(NF-1)}' | sort | uniq -c
     95 civilizations
     43 culture-material
     42 linguistics
     36 myth-symbol
     29 synthesis
     24 verification
```
(269 committed rows per the round-98 counter's C5 control line `CORPUS-INDEX: OK files=269`; the disk count's 270th file is a same-round write by another seat — either way the claim surface is `linguistics/toast-drinking-speech-formulae.md`, frozen, so this does not move any leg.)

Justification: the corpus already maintains a **speech-act/formulae family inside linguistics** — `oath-blessing-curse-formulae`, `greeting-leave-taking-formulae`, `petitionary-and-votive-formulae`, `funerary-lament-dirge-formulae`, `lullaby-child-song-formulae` — five entries, each built as speech-act anatomy + formula slots + design procedure, each citing S-registry rows. A toast is exactly that kind of object (a formulaic speech act bound to persons and occasions), and the frozen surface path fixes `linguistics/` anyway. culture-material would own only the cup object (already owned by vessel-container-lexicon) and myth-symbol only the sacral bond (already owned by guest-right/binding-speech) — the *words* are the new content, and words live in linguistics.

## 7. Files read (ranges)

`claims.json` (full), `predispatch.py:1-63`, `predispatch-base.txt` (full); knowledge: vessel-container-lexicon `:1-11,:30-56`, cuisine-food-lexicon `:1-11,:97-125,:147-161`, oath-blessing-curse-formulae `:1-11,:52-69`, verbal-duelling-ritual-insult `:1-27,:108-125`, guest-right-hospitality-law `:1-9`, greeting-leave-taking-formulae `:1-9`, petitionary-and-votive-formulae `:1-11`, ainu `:104-116`, germanic-norse `:1-11,:62-98`, furniture-interior-lexicon `:48-54`, death-afterlife-eschatology `:38-43,:98-102`, funerary-material-culture `:1-6`, pacific-northwest `:1-6`, plus captured grep artifacts for the three elided sweeps. Glob listing of `linguistics/*.md` (42 files; target entry absent).

## 8. Notes for the claim-C writer

- The six frozen phrases: zero in-corpus today. **No restatement risk anywhere** — every adjacency in §4 is a defer-and-cite, and two (greece-classical, guest-right) are adjacent only by content, not by any swept term.
- libation is the only frozen phrase with existing occurrences (7, in 4 files, all table cells/bullets/couples — **none** in a heading or topic line, so the C8 owner count stays 0 after the entry lands, provided the entry's own headings carry the phrases and others don't grow any).
- Sogdian `:63` ("extravagant health wishes and homage likened to that offered to gods") is the one unexploited in-corpus lead for health-drinking sourcing; it points at Sogdian letter formulae — worth a registry row if a fresh source is wanted from the corpus side, but the claim requires fresh captures under `reports/round-98/evidence/` regardless.
- Registry: linguistics entries cite S-rows in frontmatter (`- sources:`); duelling ends at S992, oath at S98x; claim C opens S994+ — no numbering conflict observed.
