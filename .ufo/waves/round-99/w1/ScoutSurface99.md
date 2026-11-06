# ScoutSurface99 — Report (round 99, w1)

Seat: ScoutSurface99, leaf, read-only. Lane: kotodama-shokunin.
Item: confirm the claim-C coverage surface **by content**, map adjacency, propose the entry
skeleton, hold the bounded planning data-walk.
Main output: `.ufo/waves/round-99/w1/stage/ScoutSurface99/surface.md` (40,739 B,
sha256 63ef6bb3e7b91b833e4f81a39468b367ed8b2c8e1366bddd98a986423d2b0431).
Nothing committed; no lane file outside my stage touched; no network source opened; no tool
installed or upgraded (record: none).

---

## 1. Sweep outputs with rc

| # | command (run from the lane root) | result | rc |
|---|---|---|---|
| A | `grep -rn -i -E 'praise\|panegyr\|oríkì\|oriki\|izibongo\|imbongi\|griot\|jeli\|bard\|encomi\|eulog\|madih\|madīḥ\|qasida\|qaṣīda\|filid\|fili\|skald\|drápa\|drapa\|kenning\|epithet\|genealog' corpus/knowledge` | 1084 matches / 190 files | 0 |
| B | `grep -rnP -i '\b(praise\|panegyr\|oríkì\|oriki\|izibongo\|imbongi\|griot\|jeli\|bard\|encomi\|eulog\|madih\|madīḥ\|qasida\|qaṣīda\|fili\|filid\|skald\|drápa\|drapa\|kenning)\b' corpus/knowledge` | 206 matches / 50 files | 0 |
| C | per-file bounded counts (`grep -rcP … \| grep -v ':0$' \| sort -t: -k2 -rn`) | see surface.md §1.2 | 0 |
| D | six-phrase occurrence count (`grep -r -o -i -F "$p" \| wc -l`) | praise poetry=5, praise singer=0, panegyric=4, genealogical recitation=1, praise epithet=1, praise performance=2 | 0 |
| E | **C8 owner test** — phrase on `- topic:` line or any heading (`grep -r -i -F "$p" --include='*.md' \| grep -cE '^[^:]+:[0-9]+:(- topic:\|#)'`) | owners=0 for all six | 0 |
| F | partitions (`find corpus/knowledge -name '*.md' \| awk -F/ '{print $(NF-1)}' \| sort \| uniq -c \| sort -rn`) | 95 civilizations, 43 linguistics, 43 culture-material, 36 myth-symbol, 29 synthesis, 24 verification | 0 |
| G | total (`find corpus/knowledge -name '*.md' \| wc -l`) | 270 | 0 |
| H | registry rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`) | 930 | 0 |
| I | malformed rows (`awk -F'\|' … NF!=13`) | 0 | 0 |
| J | tier census / status census | A=556 B=345 C=29 / mined=821 queued=60 rejected=49 | 0 |
| K | highest id (`grep -oE '^\|[[:space:]]*S[0-9]+' … \| sort -V \| tail -1`) | S1006 | 0 |
| L | S1007+ presence (`grep -E '^\|[[:space:]]*S10(0[7-9]\|[1-9][0-9])[[:space:]]*\|' corpus/SOURCES.md`) | no output → **id range free** | **1** |
| M | insertion point (`ls corpus/knowledge/linguistics/ \| sort \| grep -n -A2 -B2 'politeness\|proverbs'`) | 25 politeness-taboo-euphemism.md, 26 proverbs-riddles-attestation-solutions.md | 0 |
| N | sibling sizes (`wc -c`) | funerary 51,055; toast 47,760; verbal-duelling 36,743; greeting 21,043 | 0 |
| O | sibling h2 counts (`grep -c '^## '`) | 8–15, modal 13 | 0 |
| P | `ls -la reports/round-99/evidence/` | directory does not exist yet | **2** |

Two false-positive classes are worth recording because they corrupt naive sweeps:
unbounded `fili` matches *filiation/filial*, and unbounded `bard` matches the **Bard
Graduate Center** publisher — all 7 of `civilizations/dine-navajo.md`'s high-signal hits are
that publisher, so its praise content is 0.

## 2. Hit classification

- **Owners (topic line or heading): none.** 0/6 phrases (§1.E). By hand, the four corpus h2
  that contain "praise" are `yoruba.md:78`, `zimbabwe-shona.md:87`,
  `funerary-lament-dirge-formulae.md:133`, `orality-formulaic-language.md:56` — none is a
  frozen phrase. The claim's `before` cell (owners=0) is confirmed **by content**, not just
  by filename.
- **Substantive sections (defer):** 38 anchors across 25 files; full table in surface.md §2.2.
  The load-bearing ones: `orality-formulaic-language.md:56-62` (§3 praise-names as formula
  lexicon — the claim's named boundary), `:99-127` (singer's speech, item 10 already names
  the jeli guild), `funerary-lament-dirge-formulae.md:56-84` (professional-keener office) and
  `:133-153` (praise of the dead), `verbal-duelling-ritual-insult.md:110-146` (boast formula),
  `toast-drinking-speech-formulae.md:122-171` (office + the three order rules),
  `deity-name-derivation-pipeline.md:69-88` (**divine** epithet grammar),
  `sacred-kingship-mythic-charter.md:150` (praise-recitation as performed pedigree),
  `heraldry-emblems-identity-marks.md:35-48` (bearer units),
  `polynesia-navigation.md:142-161` (whakapapa precision/access),
  `kinship-terminology.md:153` (genealogies as charters),
  `yoruba.md:78-94` (oríkì economy), `mali-songhai.md:50-70` (jeli register tags),
  `parthia.md:165-183` (gōsān calibration + the five-item office checklist).
- **Passing mentions:** 13 phrase occurrences in 9 files, all prose or table cells
  (`java-majapahit:198`, `zimbabwe-shona:23` — a **book title**, `orality:60,148`,
  `speech-surrogates:110`, `byzantium:7,55,90`, `tamil:105`, `inca:151`, `yoruba:161`,
  `fon:42`, `shona:104`), plus ~30 single-sentence files listed in surface.md §2.3.

## 3. Adjacency table (condensed; 30 rows in surface.md §3)

| neighbour | owns | boundary |
|---|---|---|
| ⚠ `orality-formulaic-language.md:56-62` | praise-names as formula lexicon; epithet sets; 5-step build order | cite `:60` once; never restate the formula machinery or "praise-name = compressed genealogy" |
| ⚠ `funerary-lament-dirge-formulae.md:56-84,133-153` | professional-mourner office; praise of the dead | do not re-derive the licensed-performer split; the praise office is patron-facing, the mourning office death-facing |
| ⚠ `verbal-duelling-ritual-insult.md:110-146` | boast formula; audience adjudication; satire-as-curse routing | own only praise-genre rivalry and flattery's limits |
| ⚠ `toast-drinking-speech-formulae.md:122-171` | office that runs a sequence; three order rules | cite and apply; do not re-derive ordered-speech theory |
| ⚠ `deity-name-derivation-pipeline.md:69-88` | **divine** epithet grammar (head+modifier+jurisdiction) | own human/lineage/office/place epithets only; route epiclesis there |
| ⚠ `sacred-kingship-mythic-charter.md:142-155` (`:150`) | royal register; praise-recitation as performed pedigree | cite the audit principle; do not re-own legitimation |
| `heraldry-emblems-identity-marks.md:35-48` | eight bearer units; grant/transmission of marks | borrow the bearer-unit model by citation; no second transmission ledger |
| `polynesia-navigation.md:142-161` | whakapapa precision, branch selection, access fields | cite `:146`; build no second genealogy-precision model |
| `kinship-terminology.md:153` | genealogies as present-serving charters | cite; do not re-argue |
| `yoruba.md:78-94` / `mali-songhai.md:50-70` / `zimbabwe-shona.md:87-107` / `fon-dahomey.md:118-143` | the Yorùbá, Mande, Shona and Fon cases | cite and route; no case rebuilt, no register tag generalized |
| `parthia.md:183` | the five-item bardic-office checklist | cite it, or state a genuinely different procedure |
| `naming-systems.md:44-63` | name slots incl. `laqab`, `nasab` | an epithet is not a name slot; state the distinction |
| `speech-surrogates-whistled-drummed.md:110` | the channel; already routes praise poetry to `orality:124` | mention only; no edit in scope |
| `linguistic-anthropology.md:9-28` | SPEAKING grid | apply, do not teach |
| `oath-blessing-curse-formulae.md:20-38` | binding formula | route the binding side of satire there |
| `contact-scenario-builder.md:94,101,156` | epithet translation under contact | route |

## 4. Skeleton (14 h2; 6/6 frozen phrases in h2 headings)

1 Scope and the six deferrals · 2 Praise as a public speech act (person/lineage/office/place)
· 3 **The praise singer**: office, recruitment, licence, patron · 4 **The praise epithet**:
keeping the name tied to its bearer · 5 **Genealogical recitation**: the lineage spine and
its access rules · 6 **The order of a praise performance**: slots, turns, the caller ·
7 Audience, uptake and the economy of recognition · 8 Rivalry, satire and the limits of
flattery · 9 **Panegyric**: praise of the office, dynasty and place · 10 **Praise poetry** as
a genre system: verse, register, transmission · 11 Design procedure (ten steps, each a
decision, none a re-run of orality §3) · 12 Error patterns · 13 Calibration, limits, handoff
· 14 Inference ledger.

Two tables carry the argument: **A** §1 one-owner boundary (≥6×3, the house pattern from
heraldry §2 / speech-surrogates §2); **B** §9 panegyric institutions at a glance (≥6×5, every
row routing to its owner file, no new case detail). Frozen phrases also land as table cells
in a §10 "genre at a glance" table if redundancy is wanted.

## 5. Planner data-walk: linguistics is the right partition

95/43/43/36/29/24 = 270 (rc 0). Reasons: (1) **shape match** — the entry is a speech-act
institution + design procedure, the exact shape of the seven existing linguistics entries
(sizes 21k–51k B, 8–15 h2), while civilization entries are reference bases with era/costume/
name sections; (2) **the five sharpest deferrals are all linguistics files**; (3) the frozen
phrases are genre/institution terms, which the corpus files under linguistics; (4) a
civilizations placement would collide with nine case owners and force either duplication or
a favourite; (5) the index mechanics agree — insertion between
`politeness-taboo-euphemism.md` and `proverbs-riddles-attestation-solutions.md` (rc 0), with
`## linguistics/` 43→44, total 270→271, footer vector 43/36/43/29/24/95 → 44/36/43/29/24/95,
new revision 2.25.

Registry preconditions measured for the owning seat: 930 rows, 0 malformed, highest S1006,
**S1007+ free** (grep rc 1), `kind` whitelist `spec|docs|paper|code|tool|dataset|talk|book|community|own-work`,
anchor convention `body text; reports/round-99/evidence/S10xx.txt; exact locator: "<quote>"`,
and `reports/round-99/evidence/` does not exist yet (rc 2).

## 6. Blockers and flags

None blocking. Three flags for the L1: (a) `speech-surrogates:110` will hold a second
pointer to "praise poetry" — a mention, not a C8 owner, and not my edit; (b) any future
sweep must use the word-bounded regex or it will report `dine-navajo` (Bard Graduate Center)
and `fili`-as-*filiation* as praise hits; (c) the divine/human epithet split is the boundary
most likely to be missed in drafting — the entry's §4 must state it in its first paragraph.
Lead worth passing on: `zimbabwe-shona.md:23` cites Hodza & Fortune 1979, *Shona Praise
Poetry* — canonical for the surface, but a row needs a fresh capture, so it is a lead, not a
commitment.

## 7. Files read

Full list in surface.md §7. Sweeps over `corpus/knowledge/**`; read in ranges: 25 entries
across linguistics, myth-symbol, civilizations, synthesis and culture-material, plus
`corpus/SOURCES.md`, `corpus/README.md`, `reports/round-99/claims.json`,
`reports/round-99/predispatch.py` (C8 legs), `reports/round-49/run-validation.py`,
`tools/check-corpus-index.py`, `tools/gates/lexicon-coverage-audit.py`.
