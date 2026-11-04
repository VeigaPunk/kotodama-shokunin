# ConnectorOverlap — sibling-overlap map for claims O and D (round 82, w1)

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` (read-only: every
probe is `git -C <lane> show|grep|ls-tree <base>`, or a copy of the base blob into
`/fast/scratch/hyaku/kotodama-r82/ConnectorOverlap/`). Seat: ConnectorOverlap. Date: 2026-11-04.

## 0. What this file adds, and what it deliberately does not repeat

`ScoutGap` already published the claim-D absence census (15 files / 27 lines on its narrow pattern; two
nearest owners) and the S905↔S320 work-level duplicate. `ScoutRegistry` already published the registry
grammar census (827 rows, 11 cells, cadence histogram, date boundaries, queue oracle). **This file adds the
three things neither seat produced**: (1) the `owns` / `mentions` / `hands off` classification with the
one-way pointer sentence the entry needs for `- couples:`; (2) the claim-O consumer scan of the `recheck`
cell across lane tools, frozen counters, the corpus contract and the **fleet** script; (3) the pre-existing
`corpus/README.md` index drift the landing must not inherit blindly.

Pattern reconciliation, so two honest numbers do not read as a defect: ScoutGap's census pattern
`xenia|hospitium|guest-friend|guest-right|guest right|theoxeny|hospitality` → 15 files / 27 lines. Mine,
`guest|hospitality|hospit|xenia|suppliant|supplication` (case-insensitive, `corpus/knowledge/**/*.md`) → **35
files**. Mine is a strict superset because it includes bare `\bguest`, `hospit*` (which pulls in *hospital*
homographs) and `supplia*`. Command and count in §8 V5.

## 1. Claim D — every file whose surface touches guest-right

`owns` = the file claims that surface as its subject; `mentions` = one clause or table cell, incidental;
`hands off` = the surface is absent (measured 0 hits) and the quoted line is the nearest neighbour the
entry must still cite. Quote is verbatim from the base blob at the line given.

| file:line | class | quoted line | one-way pointer the entry should use |
|---|---|---|---|
| `culture-material/cuisine-food-lexicon.md:95` (also `:138`, `:170`) | **owns** (token + loyalty vocabulary) | "The guest-host bond is lexicalized as *taste*: betraying your host is a flavor word." | Cuisine owns the salt/bread token, the `namak-halāl`/`namak-harām` loyalty lexemes and the table grammar; this entry owns the sacral-legal institution (who owes what, when the bond starts, what breach costs) and returns the *sanction*, not the vocabulary. |
| `myth-symbol/sacred-topography-pilgrimage.md:92` (also `:66`, `:79`, `:86`) | **owns** (visitor access law) | "Access law is the entry's sharpest deliverable. Three variables settle it: *who may enter* …, *when* …, and *what must be true of the visitor* (purity state, dress, escort, payment)." | STP owns access to a **site** (hostel, toll, purity state, escort); this entry owns the obligation between two **persons** (host↔guest) and returns the bilateral term and its breach. |
| `culture-material/architecture-settlement-lexicon.md:30` (also `:57`, `:124`, `:125`) | **owns** (built boundary) | "**chuihuamen** 垂花门 \"festooned-flower gate\" dividing outer (male/guest) from inner (female/family) court" | Architecture owns the threshold furniture and the drip-line legal strip ("the eaves even marked a legal strip around the building", `:124`); this entry owns the *act* performed at the threshold (bond start) and returns the ceremony's legal effect. |
| `myth-symbol/ritual-liminality.md:21` (also `:110`) | **mentions** | "safe-conduct (the guest's token)" | RL owns the rite grammar (separation/liminality/incorporation) and the gift; this entry owns the token's legal content (what it entitles, for how long) and must not restate the triad. |
| `linguistics/orality-formulaic-language.md:66` | **owns** (arrival type-scene) | "arrival (host sees guest → questioning → hospitality)" | OFL owns the narrative beat-order; this entry owns the institution the scene encodes. The worked example must not re-teach the type-scene, only cite its beat slots. |
| `linguistics/register-strata-attestation.md:206` (also `:88`, `:136`) | **owns** (register law over the guest's binding word) | "\| `QREG-08` \| the guest's charge \| `broker`, `market-goer` \| `directive-binding`, `not-rollable` \| binds at the gate; may not write the roll \|" | RSA owns force/record ("binds but is `not-rollable`"); this entry owns what the charge *promises* in hospitality terms (protection, seat, parting gift) and returns the content, never the register. |
| `myth-symbol/binding-speech-complex.md:138` (also `:127`) | **hands off** (`guest` = 0 hits) | "should be written as a culture of *hostages and sureties* instead" | BSC owns oath/curse enforcement models; this entry cites §4.1–§4.4 for "what seals it" (oath, self-imprecation, surety) and returns the hospitality obligation the oath carries. |
| `linguistics/politeness-taboo-euphemism.md:57` | **hands off** (`guest` = 0 hits) | "speaker→**bystander** (audience-conditioned forms) … A bystander axis makes eavesdroppers grammatical participants" | PTE owns address/deference grammar; this entry cites the bystander axis for guest-address formulas and returns no honorific typology of its own. |
| `linguistics/naming-systems.md:106` | **hands off** (`guest` = 0 hits) | "true name = power over; false name = immunity; renaming = rebirth/sanctuary" | NS owns the name system; this entry may use a guest-name/alias as an *institutional* act and returns the slot (who assigns it, who may use it). |
| `synthesis/coupling-model.md:77` | **hands off** | "Fix a scene-scale brief: interval, location, speakers/wearers, audience, resources, and inherited facts supplied by lore" | CM owns the coupling procedure (its worked case is cloth); this entry's worked example follows CM's brief shape and returns a hospitality slice, never a second coupling method. |
| `myth-symbol/myth-folktale-genres.md:55` | **owns** (theoxeny genre label) | "\| 750–849 \| Religious tales \| God/saint-in-disguise hospitality tests; miracle and judgment legends \|" | Genre owns the ATU label; this entry owns the *test* as an institution (what the disguised visitor checks, what failure triggers) and must not re-table the genre index. |
| `myth-symbol/number-symbolism.md:118` | **mentions** (calibration hazard) | "\"Loki the 13th guest\" origin of the 13 taboo: modern reconstruction" | Number-symbolism owns the 13-taboo calibration; this entry must **not** cite thirteen-at-table as ancient guest-right evidence. |
| `myth-symbol/purity-pollution-boundary-systems.md:33` (also `:73`) | **mentions** | "\| 5 \| own / other \| the stranger, the foreigner, the captive \| the *pharmakos* exiled for the group" | Purity owns the stranger as boundary category and the *pharmakos* export; this entry owns the *admission* procedure, and returns the distinction between admitted guest and expelled scapegoat. |
| `myth-symbol/sacred-kingship-mythic-charter.md:111` (also `:159`) | **mentions** | "The ruler comes from outside the society he rules — a foreign lineage, a captive, a younger son from elsewhere" | Sacred kingship owns the stranger-**king** (Sahlins); this entry owns the stranger-**guest**, and returns the point where guest-right ends and a legitimacy claim begins. |
| `synthesis/conlang-blueprint-template.md:126` (also `:85`) | **owns** (lexicon slots) | "People/kinship \| 091:guest=[ ]; 092:host=[ ]" | The blueprint already allocates slots 091 `guest` / 092 `host` and its first test sentence is "a guest arrives" (`:85`); this entry must use those slots and propose new numbers for bond/violation/parting-gift rather than invent a parallel field list. |
| `culture-material/furniture-interior-lexicon.md:69` | **mentions** | "make one bed a legal object (the heir's bed, the widow's bed, the guest's bed)" | Furniture owns the guest's bed as legal object; this entry cites it for the host's duty to provide a seat/bed and returns the duty's duration. |
| `civilizations/pacific-northwest.md:78` (also `:95`, `:97`, `:99`) | **mentions** (real-world case) | "\| Guests/witnesses \| Gifts recognize their role in acknowledging transfers and claims \|" | PNW owns the guest as **witness** in potlatch transfers; this entry cites it as a case and must carry `:85`'s caveat that "gift exchange" is a partial lens. |
| `civilizations/ainu.md:70` (also `:79`) | **mentions** (real-world case) | "Gratitude, hospitality, respectful communication, and sending-back form a reciprocal relationship." | Ainu owns the spirit-guest reciprocity (iomante); this entry takes only the design pattern (`:79` visitor→hospitality→return) and never an operational reenactment (`:164`). |
| `civilizations/celts.md:74` | **mentions** (violation case) | "**Hospitality mechanism:** Bres's failures of provisioning and patronage bring complaint and satire" | Celts owns hospitality-failure-as-illegitimacy; this entry cites it as the breach exemplar and returns the sanction ladder, not the sovereignty argument. |
| `civilizations/thrace-dacia.md:111` (also `:105`) | **mentions** (comparison method) | "compare **host/guest → seating → vessel material → portion/service → gesture → spatial threshold → audience**" | Thrace-Dacia owns that comparison method and warns to keep "textual hospitality, mortuary provisioning, and painted banqueting distinguishable"; this entry may reuse the variable list but must not restate the tomb-feast comparison. |
| `civilizations/arabia-pre-islamic.md:69` (also `:71`) | **mentions** (real-world case) | "\| Fakhr: self/group praise \| Descent, courage, generosity, hospitality \|" | Arabia owns hospitality as honour-contest vocabulary; this entry cites it as the reputation weapon a breach hands the accuser. |
| `civilizations/greece-classical.md:75` | **mentions** | "\| Hestia and household/civic hearths \| Continuity, hospitality, sacrificial order \|" | Greece owns the hearth row only; there is **no** xenia/Zeus Xenios content anywhere (§8 V5: `xenia|hospitium|guest-friend|theoxeny` → 0 files / 0 lines), which is the entry's gap evidence. |
| `myth-symbol/creation-myths-taxonomy.md:49` | **mentions** (hook to answer) | "guest-right owed to the muskrat's kin" | Creation-myths left one craft hook unbuilt; this entry answers it and returns the full institution behind the hook. |
| `culture-material/medicine-healing-codes.md` | **hands off** (homograph) | "hospitals and infirmaries" (`:3`); `:32` "advertising dream incubation to new suppliants" | Medicine owns *hospital* (Latin *hospes* but a different institution) and the suppliant at the abaton; do not treat either as hospitality-law evidence — only `:32` may anchor "suppliant" as a distinct degree. |

Sweep appendix (35 files, hit counts on the broad pattern, `corpus/knowledge/`): register-strata 7,
pacific-northwest 6, medicine-healing 6, ainu 5, cuisine 4, amazonia-tupi 3, furniture 3, arabia 2, balts 2,
celts 2, thrace-dacia 2, number-symbolism 2, conlang-blueprint 2, germanic-norse 1, greece-classical 1,
igbo 1, india-tamil-sangam 1, mamluk 1, tibet 1, zimbabwe-shona 1, architecture 1, bathing 1, funerary 1,
masks 1, scent 1, historical-linguistics 1, numerals 1, orality 1, creation-myths 1, direction-symbolism 1,
divination 1, myth-folktale-genres 1, ritual-liminality 1, symbolism-synthesis-method 1,
contact-scenario-builder 1. (Files with 1 hit and no guest-right content are passing vocabulary: `bathing`,
`funerary`, `masks`, `scent`, `numerals`, `direction-symbolism`, `divination`, `symbolism-synthesis-method`,
`contact-scenario-builder`, `historical-linguistics`, `mamluk`, `tibet`, `zimbabwe-shona` — no table row
needed; they own nothing the entry touches.)

## 2. Cross-partition couplings the entry must declare one-way

Each row is a coupling the entry needs and cannot own. Left column = the file that owns it; right = what the
entry returns so the coupling is a trade, not a copy.

| surface | owner (one-way) | what this entry returns |
|---|---|---|
| bond formation (threshold, first morsel, clasp) | `ritual-liminality.md` + `architecture-settlement-lexicon.md` | the legal effect of the act, and when the bond *ends* (which no rite grammar supplies) |
| sealing (oath, token, salt, surety) | `binding-speech-complex.md` + `cuisine-food-lexicon.md` | which seal is available at which degree of guest (stranger vs guest-friend vs envoy) |
| guest's binding word | `register-strata-attestation.md` (`QREG-08`) | what the charge promises in protection/keep terms |
| address and deference | `politeness-taboo-euphemism.md` + `naming-systems.md` | the guest-name as an institutional slot |
| the scene and its beats | `orality-formulaic-language.md` (arrival) + `myth-folktale-genres.md` (ATU 750–849) | the institution the scene tests, and what failure triggers |
| the road and the site | `sacred-topography-pilgrimage.md` (access law, hostel, toll) | the person-to-person obligation that survives after the road |
| breach and expulsion | `purity-pollution-boundary-systems.md` (*pharmakos*) + `binding-speech-complex.md` (curse) | the hospitality-specific sanction (feud, sacral penalty, stranger-god test) |
| lexicon fields | `synthesis/conlang-blueprint-template.md` (091/092) | new slot numbers for bond/violation/parting-gift |
| canon boundary | `synthesis/worldbible-integration-contract.md:17` | "decides nothing about what is true in any world" |

**Sibling lanes that could claim the surface (report, never absorb).** No knowledge file owns hospitality as
an institution, so the only claimants are lanes, not files: `civilizations/greece-classical.md` would be the
natural home for *xenia* as a real-world case (it holds one hearth row today); `linguistics/register-strata-
attestation.md` could absorb the guest's *charge*; `culture-material/cuisine-food-lexicon.md` could absorb
the token. The entry should name those three as the ones that would claim it if it did not exist, and hand
the *canon* decision (which culture keeps guests, for how long, under which god) to lore-shokunin.

## 3. Rows surface — S904–S907

- **S905 is a work-level duplicate of an existing row.** `corpus/SOURCES.md:349` S320 is *The Poetic Edda*
  trans. Bellows, Gutenberg **#73533**, graded A, full text fetched (HTTP 200, 977,828 bytes, 24,314 lines),
  scoped to Völuspá + Grimnismol 39. Planned S905 is the same translation, different delivery (Wikisource),
  different poem (Hávámál). Not a duplicate URL; a duplicate *document*. Agrees with ScoutGap §4. Decision is
  the L1's; if S905 lands it must say "same translation as S320, new poem" in `teaches`.
- **S907's reject premise has an in-lane positive control.** S903 (round 81) opened the **same Wikisource
  1911 EB slug family** by plain `curl -sL` and got HTTP 200 / 87230 bytes of article prose
  (`reports/round-81/evidence/S903.txt`: "article fully transcluded server-side; a plain fetcher receives the
  prose"). So "plain fetch returns the Wikibase scaffold" cannot be asserted for
  `.../1911_Encyclop%C3%A6dia_Britannica/Guest` without (a) the canonical-slug probe, (b) the S903 slug re-run
  as the positive control in the same session and UA, and (c) both UAs recorded per QUALITY 22. If the S903
  control is clean and the Guest slug scaffolds, the reject stands and the reason must name the artifact.
- **S904 (Gutenberg #1727) and S906 (#26073) are clean** at URL and work level (ScoutGap §4; my registry grep
  found no `Homer`, `Ovid`, `1727`, or `26073` row).

## 4. `corpus/README.md` — the landing surface nobody owns (measured drift)

Measured at base (`§8 V9`): files **255** (95/42/32/33/29/24); section headings **32/32/41/29/24/95**;
present index rows: linguistics 32, myth-symbol **32 of 33**, culture-material **41 of 42**, synthesis 29,
verification 24, civilizations 95. Missing rows are exactly two, both from recent landings:

- `corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md` (round-81 D entry, no index row, heading
  still `## myth-symbol/ (32)` against 33 files);
- `corpus/knowledge/culture-material/maritime-seafaring-lexicon.md` (no index row, heading 41 against 42).

The footer's last "Counts checked" line (`:836`) still reads **253**. So the guest-right landing must reckon
from **255 → 256** files and `## myth-symbol/ 32 → 34` (its own row plus the missing ordeal row) — or state
that it inherits the drift deliberately. Incrementing the footer's 253 as if it were current turns a 2-file
drift into a 3-file one. ScribeEntry/ScribeRows do not own README by their briefs; this is the coverage hole
in the wave, and it belongs to the L1 or to a named seat.

## 5. Claim O — who already reads the `recheck` cell

Sweep: `git -C <lane> grep -ln 'recheck' <base> -- tools/ 'reports/round-*/accept-*.py'` plus `tools/*.py`.

| surface | line | what it does with the cell | verdict |
|---|---|---|---|
| `scripts/sources-census.sh` (**fleet**, `mode=overdue`) | `:675-686` | full implementation: `due = opened + N days` for `NNd`, ISO date = itself, any symbolic cadence never overdue; prints `overdue <id> <N>d recheck=… opened=…` plus a `cadence` line per cadenced row | **duplicate capability, not duplicate code.** The arithmetic the round specifies already exists fleet-wide, with selftests including indents 0–3 (`:287`). The lane tool's delta is: summary-only output, `DUE <id> <iso-date>` instead of days-past, exit 2 on malformed input, and `on-release` as the only exempt token. |
| `scripts/sources-census.sh` (`mode=validate`, `E09`) | `:664-666` | flags a recheck that is neither ISO, nor `NNd`, nor `symbolic()`; `symbolic(s) = ^[A-Za-z][A-Za-z0-9 _-]*$` | **contradiction risk.** `annual`, `quarterly`, `on demand` are legal to the fleet census and would be **exit 2** for the round's tool. Base data has none (E09 = 0, §8 V8), so the divergence is latent, not live. |
| `tools/reopen-row.py` | header | executes a recheck: refetches a named row's URLs, verdict LOCATED/ABSENT/… | **complement.** It fetches by id on demand; the new tool only schedules and must never fetch. State this one-way in the tool docstring. |
| `tools/check-supersession-settlement.py` | `:90` | destructures `recheck` and ignores it (`status`/`usedby` drive the settlement chain) | adjacent only; no arithmetic |
| `tools/check-row-fragments.py` | `:131` | `_recheck` bound and deliberately unused; validates staged row fragments (`status`, `opened`, 11 cells, `dup-url` within one round) | adjacent only; the new tool is the first to give the cell meaning |
| `tools/check-source-access.py` | `:106`, `:31` | column-header literal; row regex `^\|\s*(S\d{3,})\s*\|` — **0 leading spaces**, and `len(cells)!=11` raises | **row-grammar divergence.** Indent 1–3 is invisible to it while the round contract (and the fleet census, and `tests/` selftest at `:287`) require 0–3 |
| `tools/check-settlement-fixture.py` | `:56` | fixture header literal with `365d` | fixture only |
| `tools/check-craft-exercise.py` | `:282` | the prose heading "## Source rechecks" in a crafted exercise | unrelated object |
| `tools/d2-typed-labels.py` | `:1201` | unrelated prose ("RR-01 recheck") | unrelated |
| `reports/round-73/accept-c.py` | `:147` | `RECHECK_RE = ^(?:\d+d|\d{4}-\d{2}-\d{2}|[a-z][a-z-]*)$` | frozen counter over **staged row fragments**; accepts ISO **and** any lowercase token |
| `reports/round-75/accept-c.py`, `round-76/accept-c.py` | `:221`, `:269` | `RECHECK_RE = ^(?:\d+d|[a-z][a-z0-9]*(?:[ -][a-z0-9]+)*)$` + `_rows_cadence_ok` | **the ISO branch was dropped** between r74 and r75; if this counter ever ran on the registry, the 154 ISO rows would fail. It runs on round rows, so base is unaffected — but it is the second vocabulary the new tool must not be confused with. |
| `corpus/QUALITY.md` | — | **0 occurrences of `recheck` and of `cadence`** (`grep -ci` = 0 each) | the cell has no rulebook definition in-lane; the only definition is the frozen contract |
| `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (fleet, frozen) | `:38` | "`recheck` — ISO date or cadence (`90d`, `180d`, `on-release`)" | the authority the round's tool implements; the contract also fixes `opened` mutability and the append-only rule (`:49`) |

**Defects to report (not repair).**
1. **D-O1 row-grammar split**: frozen census (`^\|`) and `check-source-access.py` (`^\|`) see only column-0
   rows; the round contract, the fleet selftest and the r76 counter accept 0–3 indents. Base has 0 indented
   rows (§8 V4), so numbers agree today and will disagree the day a row is indented.
2. **D-O2 vocabulary split**: fleet `symbolic()` and `RECHECK_RE` (r73–r76) accept arbitrary symbolic tokens;
   the round contract and the new tool accept only `on-release`. A row with `annual` would be census-green and
   recheck-fatal. Recommend the tool's `RECHECK-ERROR` name the offending cell value verbatim so the
   disagreement is visible rather than "unparseable cadence".
3. **D-O3 no status filter**: the contract defines no status exclusion, so the queue counts the 37 `rejected`
   and 58 `queued` rows. At `--as-of 2027-10-24` that yields **813 due of 827**, 37 of them rejections.
   Correct per contract; worth one sentence in the tool docstring so a reviewer does not read it as a bug.
4. **D-O4 no capability novelty at fleet level**: `sources-census.sh overdue` already answers "what is due".
   The O claim should be described as *contract conformance + error discipline + in-lane quiet output*, not as
   a new capability — otherwise a critic can defeat the claim's premise with one fleet command.
5. **D-O5 entry prose vs row cell**: five entries already state `- recheck: 180 days, per row
   (`corpus/SOURCES.md` recheck cells).` (measured: 5 occurrences of that exact string). Nothing checks that
   an entry's prose horizon equals its rows' cadence cells. This round can, once (see §7).

**Queue shape (why the tool looks dead on real data).** The registry's `opened` dates span 2026-10-19 …
2026-11-01 (10 values, §8 V7), so cadences produce a **cliff, not a distribution**: `due/upcoming` =
0/18 at 2026-11-04 → 25/242 at 2027-04-18 → **267/0** at 2027-05-03 → 267/540 at 2027-07-25 → 695/118 at
2027-10-22. The `--window` band is empty for long stretches because everything due within a year was opened
within two weeks. `due = 0` today is correct, not broken: the DUE-line branch has **no** real-data exercise at
the base as-of date.

## 6. The cross-claim number: D moves O's summary line

The D claim lands four rows; the O claim lands a tool whose last field is `rows`. Measured interaction
(`§8 V6`, from the base histogram plus the four planned rows at 180d):

| input | `RECHECK-QUEUE` at `--as-of 2026-11-04 --window 90` | at `--as-of 2027-05-03` |
|---|---|---|
| base registry | `0 due / 18 upcoming / 14 on-release / 827 rows` | 267 due |
| base + S904–S907 at `180d` | `0 due / 18 upcoming / 14 on-release / **831** rows` | **271** due |
| base + S904–S907 at `90d` | `0 due / **22** upcoming / 14 on-release / 831 rows` | 271 due |

So the D seat's cadence choice is observable in the O tool's output, and the O tool's `rows` field is
observable in D's registry growth. Neither claim's acceptance may *require* the other's path (QUALITY 7
separability): the merged-tree run is an L1 post-merge check, not an acceptance leg inside `accept-o*`.

## 7. Proposed move (one, bounded)

**Bind the two claims with one declared value and one cross-check, without touching either claim's bytes
beyond what the contract already requires.**

1. **Value**: ScribeRows writes all four rows with `180d`; ScribeEntry writes the header line in the existing
   house form — `- recheck: 180 days, per row (`corpus/SOURCES.md` recheck cells).` (the exact string five
   entries already use). Rationale for 180d over 365d: the four sources are canonical/stable texts (Homer,
   Ovid, Eddic poetry, a 1911 encyclopaedia), and 180d matches the entry-header precedent; 90d would be a
   curatorial lie told to make a test easy.
2. **Cross-check (L1, post-merge, outside both claims' acceptance)**:
   `python3 tools/check-sources-recheck.py --as-of 2026-11-04 --window 90` must print
   `RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 831 rows`; and at
   `--as-of 2027-05-03` the tool must print `271 due` with `DUE S904 2027-05-03`, `DUE S905 2027-05-03`,
   `DUE S906 2027-05-03`, `DUE S907 2027-05-03` among the due lines. Independently,
   `scripts/sources-census.sh overdue <lane> --today 2027-05-03` must report 271 overdue rows (the fleet
   implementation agrees: 267 on base, §8 V8) — two implementations, one number.
3. **Why it is worth the bytes**: today's base yields **zero** DUE lines, so the tool's DUE branch is exercised
   by fixtures only; the round's own four rows are the one cheap chance to exercise it on real registry data,
   and the same probe makes the entry's prose horizon and its rows' cells one checked value (defect D-O5).

**Risks.** (a) If ScribeRows picks `365d` instead, the 2027-05-03 probe still returns 267 but no longer
demonstrates the new rows — declare the value before either seat writes. (b) S907 is a `rejected` row and will
appear in the DUE list; that is contract-correct (D-O3) but a reviewer may read it as noise — if the L1
prefers, S907 can carry `on-release` and be exempt, which changes the count to 270 and should then be stated.
(c) The merged-tree run must stay out of `accept-o*`, or QUALITY 7 separability breaks. (d) If a critic
presses D-O4 (fleet already has `overdue`), the cross-check in (2) is the answer: the lane tool and the fleet
script agree on 0 and on 267/271, which is what "two implementations, one truth" looks like.

**Axes affected.** operability (a real-data DUE path + one checked cadence value), adjacency (D↔O coupled by a
number; entry prose ↔ registry cells), coverage (README drift named so it is not inherited). None harmed: no
new claim, no canon, no new file beyond the four rows and the tool the round already lands.

## 8. Verification — commands and raw output

All at base `c285b2a`, run 2026-11-04 from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Scratch root:
`/fast/scratch/hyaku/kotodama-r82/ConnectorOverlap/`.

- **V1 row/cadence census** (python3 over `git show <base>:corpus/SOURCES.md`, registry section only):
  `rows: 827`; `cell-count distribution: {11: 827}`; `recheck`: `365d` 392, `180d` 249, `2027-10-23` 112,
  `2027-10-22` 42, `90d` 18, `on-release` 14; `status`: mined 732, queued 58, rejected 37; leading spaces
  `{0: 827}`.
- **V2 queue oracle**: `as-of 2026-11-04 window 90 -> due=0 upcoming=18 on-release=14 rows=827`.
- **V3 ISO branch**: `ISO rows: 154 diverging from opened+365: 0`.
- **V4 scope agreement**: file-wide `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' SOURCES.base.md`
  → `827`; indented 1–3 → `0`; `NF!=13` → `0`; rows after the `## Paths` heading → `0`.
- **V5 guest sweep**: `git grep -ilE 'guest|hospitality|hospit|xenia|suppliant|supplication' <base> --
  corpus/knowledge/ | wc -l` → `35`; topic-line owners `git grep -ilE '^- topic:.*(guest|hospital|xenia|
  hospitium)'` → 3 files (cuisine, furniture, medicine — medicine is the *hospital* homograph);
  `^- gap filled:` owners → `0`; `guest-right|guestright|guest right` → 4 files (cuisine ×3 lines, README,
  creation-myths); `xenia|hospitium|guest-friend|theoxeny` → 0 files.
- **V6 D→O interaction**: base + 4 rows at 180d → `due=0 upcoming=18 on-release=14 rows=831`, and at
  2027-05-03 → `due=271`; at 90d → `upcoming=22`.
- **V7 queue shape**: 2026-11-04 0/18 · 2027-04-18 25/242 · 2027-05-03 267/0 · 2027-07-25 267/540 ·
  2027-10-22 695/118. `opened` histogram is 10 ISO dates, 2026-10-19 … 2026-11-01.
- **V8 fleet cross-check** (`bash scripts/sources-census.sh overdue <scratch-lane> --today 2026-11-04`):
  exit 0, `673 cadence`, `0 overdue`; `--today 2027-05-03` exit 1, `673 cadence`, `267 overdue`;
  `census` mode → `rows 827`, `tier.A 498 / tier.B 313 / tier.C 16`, `status.mined 732 / status.queued 58`;
  `validate` → `grep -c E09` = `0`.
- **V9 README drift**: headings `32/32/41/29/24/95`; files `95/42/32/33/29/24` = 255; missing rows
  `['ordeal-judicial-proof-rituals.md']` (myth-symbol) and `['maritime-seafaring-lexicon.md']`
  (culture-material); footer "total 253".
- **V10 contract text**: `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:38` — "`recheck` — ISO date or cadence
  (`90d`, `180d`, `on-release`)"; `corpus/QUALITY.md` → `grep -ci recheck` = 0, `grep -ci cadence` = 0.
- **V11 S320 row**: `corpus/SOURCES.md:349` — Bellows *Poetic Edda*, Gutenberg #73533, HTTP 200, 977,828
  bytes, 24,314 lines, scoped to Völuspá + Grimnismol 39.
