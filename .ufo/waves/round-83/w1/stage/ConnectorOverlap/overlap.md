# Cross-axis overlap scan — round 83 w1 (claims O, D, C)

Seat: ConnectorOverlap. Read-only scan. Every byte below is read from the frozen base
`3088bd7fe2a55a123214abba7008dcddf12b301c` (`git show <base>:<path>`) or from the frozen
config `21277b089e3c64c247bb4e0fcb033abfdfa1e668`. The lane worktree HEAD is a later
revision (`774cc2e3`); no worktree byte is graded here.

Authority assignment (R82-M3): for the `corpus/SOURCES.md` rows of claim D, `ScribeRows`'
fetch receipts are authoritative and `ScoutSources`' reading is the independent second
reading; this file is a third reading of *ownership adjacency*, not of source bytes. Where
this file's census disagrees with a frozen `claims.json` sentence, the disagreement is
reported in §5, not resolved by preference.

`{WAVE}/stage/ScoutGap/owners.md` is **absent** at the time of writing
(`ls .ufo/waves/round-83/w1/stage/` lists only `ScoutSources`), so the table in §1 is the
only owners table this scan can sit beside.

---

## 1. Claim D — who already touches marriage / alliance / bride-price

### 1.1 The eight mandated files

Class key: **owns** = the file states the surface as its own subject with a decision rule;
**mentions** = the surface appears as one bullet, example, or cross-reference and the file
does not legislate it; **hands-off** = the file names the surface only to send it elsewhere
(including a stated negative).

| # | path:line | quoted line (verbatim fragment) | class | what it owns, and what D must not restate |
|---|---|---|---|---|
| 1 | `corpus/knowledge/linguistics/kinship-terminology.md:80` | `## 5. Affinal logic: the marriage rule is usually IN the lexicon` | **owns** | Owns the *inference from lexicon to marriage rule* for the whole entry. D may cite §5 and must not re-derive terminological inference. |
| 2 | `corpus/knowledge/linguistics/kinship-terminology.md:82` | `Two classical schools: **descent** theory ... vs **alliance** theory (lineages reproduce *through* exchanging brides; Lévi-Strauss 1949). Both are half-right; modern work uses both locally and models the household instead where descent fails` | **owns** | Owns the descent-vs-alliance frame *and its calibration*. D's title word "alliance" inherits this sentence; an entry that states alliance theory as an engine contradicts `:149` (`Alliance theory as universal engine ... contested`) and `:151` (`Descent vs alliance as exhaustive: superseded`). |
| 3 | `corpus/knowledge/linguistics/kinship-terminology.md:88` | `Wife-giver/wife-taker asymmetry: systems that remember who gives and who takes mark it asymmetrically in terms and deference; the debt outlives the wedding.` | **mentions** | The corpus's nearest existing sentence to a transfer obligation, but it is a *deference/debt* note, not a payment institution. D owns the payment direction; it should cite this line as the asymmetry it prices rather than paraphrase it. |
| 4 | `corpus/knowledge/linguistics/kinship-terminology.md:86` | `**Levirate** (widow marries deceased husband's brother; Deuteronomy 25:5–10, Genesis 38) and **sororate** (widower marries wife's sister): the institution presupposes affinal terms that mark those substitutions` | **mentions** | Levirate/sororate are owned here as *terminological prerequisites*. D's dissolution/substitution section must not present them as new material; cite `:86`. |
| 5 | `corpus/knowledge/linguistics/kinship-terminology.md:63` | `the European shift toward Eskimo-type terms tracks the **Church's prohibited-degrees marriage law** breaking up agnatic marriage strategies — law, not subsistence, moved the lexicon` | **owns** | Owns the prohibited-degrees case as a *lexicon* event (repeated at `:125`). D owns prohibited degrees as *law*; it must cite `:63`/`:125` and not re-narrate Goody. |
| 6 | `corpus/knowledge/culture-material/sumptuary-law-rank-display.md:25` | `by gender (women pinned to fathers'/husbands' rank — the "wives problem," §6)` | **owns** | Owns the legal-grammar of rank transfer through marriage, developed at `:64` (`## 6. England: price-schedule statutes, the cap act, and the wives problem`), `:69` (`grades *women through men*: "wives of..." rungs descend below the male degrees`) and `:88` (`The **women-through-men clause**: "wives of X may wear Y"`). D must not restate the clause; cite `:64-69`, `:88`. |
| 7 | `corpus/knowledge/culture-material/sumptuary-law-rank-display.md:87` | `The **occasion exemption**: "except on the day of her wedding" — Italian statutes licensed the trousseau ritually; display allowed, but only in ritual time` | **owns** | Owns the wedding-day exemption as a sumptuary device (also `:23` `trousseau allowed on the wedding day`). D's transfer/rite section may cite it as the licence that a transfer needs; it does not own the statute corpus. |
| 8 | `corpus/knowledge/culture-material/ritual-garments.md:1` | `# Ritual garments & vestments: ... lifecycle-rite dress (wedding, mourning, coming-of-age) ...` | **owns** | Owns wedding *dress* as an object class, with the row set at `:98-102` (shiromuku, white/1840, badeken, red sari, hwarot) and the calibration at `:146` (`Victoria did not invent the white wedding`) and `:149` (no "white = wedding" universal). D must not carry a second wedding-dress table. |
| 9 | `corpus/knowledge/culture-material/ritual-garments.md:104` | `Decide who supplies the cloth; cloth-giving is dowry politics.` | **hands-off** | The explicit handoff: the file names *dowry politics* and stops. This is the single sentence D answers. Cite it as the handoff, do not restate the dress craft beat at `:104`. |
| 10 | `corpus/knowledge/culture-material/ritual-garments.md:140` | `Wire lifecycle dress to the same cloth economy: wedding cloth supply, mourning grades as law ... make one garment do double duty across life and death (kittel-style).` | **mentions** | Owns the cloth-economy wiring for lifecycle dress (and the kittel wedding/shroud loop at `:36`, `:100`). D owns the transfer, not the cloth supply. |
| 11 | `corpus/knowledge/culture-material/trade-economy-lexicon.md:125` | `**The pledge family**: *pledge, wage, wed, wedlock* all < Gmc \**wadją* 'pledge' ... Germanic *mundr* bride-price in Grágás ... Lat. *dōs* → *dowry, dot*.` | **owns** | Owns the *word history* of the payment vocabulary (`mundr`, `dōs`/`dowry`, `wedlock`) and the security-word frame. This is the corpus's only existing bride-price citation base. D owns the *institution* and should cite `:125` for every etymology it uses rather than re-glossing. |
| 12 | `corpus/knowledge/culture-material/trade-economy-lexicon.md:166` | `**The teeth of the contract**: split tokens, tooth-cut deeds, tally halves — one authentication technology per administrative sphere, shared with marriage and oath.` | **mentions** | Owns the authentication-token family and states that marriage shares it. D may take the shared-token fact as given. |
| 13 | `corpus/knowledge/culture-material/funerary-material-culture.md:10` | `KTD-MMC-S-0004 — in-corpus mourning-dress and mourning-color layer, pointed at rather than restated: `corpus/knowledge/culture-material/ritual-garments.md:106-112`` | **hands-off** | No marriage surface: both hits (`:10`, `:12`) are cross-references into ritual-garments' *mourning* section. D must keep out of mourning grades; the only joint surface is the kittel double duty, owned by `ritual-garments.md:36`. |
| 14 | `corpus/knowledge/linguistics/naming-systems.md:116` | `**Life-stage schedule** — how many names does one person hold at birth, majority, office, marriage, death? Who may speak which one, and who assigns them?` | **owns** | Owns the name-slot schedule with a marriage slot already reserved, and the in-law taboo register at `:103` (`mother-in-law register Jalnguy`) and `:115` (`post-mortem, ruler-name, in-law, sacred-name, homophone taboos`). D's "name change" section must cite `:116` and add only what the schedule does not decide (who the change is *owed* to, and what happens on dissolution). |
| 15 | `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md:31` | `inheritance turns the bond into a durable alliance between houses, with the dead as parties` | **mentions** | Names the heritable inter-house bond as one option of the guest ladder. D owns the marriage version of that bond; it should cite `:31` rather than define "durable alliance between houses" a second time. |
| 16 | `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md:99` | `Fix the end marker: parting gift, departure, death, or inheritance — and say what survives the end (remembrance, debt, alliance).` | **mentions** | The surviving-debt grammar. D's dissolution section is the marriage counterpart; it must not mint a *second* breach ladder because `:35` and `:101` already own one (`feud by kindred duty / sacral sanction ... / compensation / outlawry / the stranger-god test`, `Build the breach ladder: feud, compensation, outlawry, sacral sanction, proof`). |
| 17 | `corpus/knowledge/synthesis/contact-scenario-builder.md:112` | `What transfers through marriage? ... Residence, property eligibility, ritual duties, or nothing in the name itself` | **owns** | Owns the *transfer-through-marriage* decision for the contact case, inside `## 8. Intermarriage and names: institutions, not syllable blending` (`:105`), with the reverse arrow at `:21` (`a marriage alliance can secure a warehouse lease`) and the worked case at `:165` (`Their household alliance gives apprentices access to yarn suppliers`). D must not publish a competing "what transfers" table; it should scope its own transfer table to the *payment and rights* side and cite §8 for the name/loan side. |

### 1.2 Same-partition and cross-partition neighbours outside the mandated eight

| # | path:line | quoted line (verbatim fragment) | class | note |
|---|---|---|---|---|
| 18 | `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:23` | `animals move as gift, loan, bridewealth and raid (§7)` | **owns** | The strongest rival for the payment direction: `:109` states the design rule — `A herd works as marriage currency, loanable capital and risk buffer at once ... design each transfer by what moves, who gains rights and what it insures.` D must cite `:23`/`:109` for the livestock case, not restate the transfer frame. |
| 19 | `corpus/knowledge/culture-material/adornment-body-codes.md:21` | `**Bridewealth and the woman's portion**: jewelry as gendered capital — South Asian *strīdhana* ... Goody & Tambiah (1973) is the comparative baseline: who *holds* ...` | **owns** | The only bullet in `culture-material` that names bridewealth as a subject, and the only in-corpus citation of the comparative bridewealth/dowry baseline (Goody & Tambiah 1973). If D uses that baseline it cites `:21`; if D ignores the jewellery case it says so. |
| 20 | `corpus/knowledge/myth-symbol/ritual-liminality.md:30` | `marriage ... bride/groom leave natal households ... threshold-crossing, shared meal, name/style change` | **owns** | Owns the marriage rite's three-phase grammar, including the `name/style change` D also wants. See also `:107` (`return, recognition, marriage, enthronement`) and `:116` (`Inventory the rites: birth, naming, puberty, marriage ...`). D's rite sequence must be a citation of this row plus only the institution-specific beats (who pays, who witnesses, what the transfer is). |
| 21 | `corpus/knowledge/myth-symbol/color-symbolism.md:12` | `The **flagship inversion pair**: Europe runs *white wedding / black funeral*; Han cultural sphere runs (traditionally) *red wedding / white funeral*; India runs *red ...*` | **owns** | Owns bridal/widow colour codes: `:55` (`India ... widowhood, renunciation ... white sari of the widow`), `:58` (shiromuku), `:60` (Victoria 1840), `:80` (`the auspicious-marriage complex`), `:134` (the false "white bridal purity" universal). D's dress-change section must not restate colours. |
| 22 | `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md:79` | `marshalling on marriage ... the wife's arms are impaled unless she is an heraldic heiress, when they go ...` | **owns** | Owns *arms/identity transfer on marriage* with named source rows, and `:148` (`Fix transmission: cadency, matriculation, marriage marshalling`). This is the corpus's only worked case of a name-change-on-marriage institution. D's name-change section must cite it. |
| 23 | `corpus/knowledge/verification/calibration-registry.md:53` | `CAL-06 ... "Totemism" is one universal primitive stage linking animal worship, clan descent, exogamy and taboo ... R as universal package/stage` | **owns** | Owns the rejected-package ledger, including `:118` (`Replacement feature matrix: ... marriage restrictions ...`) and `:140` (`Kin terms prove group marriage, matriarchy or fixed social organization — R`). D's calibration of "bridewealth = purchase", "group marriage", "kin terms prove practice" must point here, and D may not edit this file (not in its `own_paths`). |
| 24 | `corpus/knowledge/myth-symbol/animal-symbolism.md:73` | `Nuer "cattle of money" ... cattle as social idiom — names, songs, bridewealth; not primarily food` | **mentions** | Owns the faunal idiom of value; `:110` (`Decide which species is the culture's **idiom of value** — the one whose words mean wealth, marriage, time, honor`). Hands-off for the institution. |
| 25 | `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:69` | `**alliance / marriage into the divine line** ... the ruler is joined to the divine by marriage, fosterage, or the transfer of a sacred object` | **mentions** | Owns alliance-marriage as one of eight legitimation channels. D owns the institution, not the charter. |
| 26 | `corpus/knowledge/myth-symbol/motif-index-usage.md:49` | `T ... Sex: courtship, marriage, incest ... marriage-system block` | **hands-off** | The narrative partition already expects a "marriage-system block" and owns none. D supplies the block this row names; cite it as the forward pointer. |
| 27 | `corpus/knowledge/linguistics/kinship-terminology.md:104` | `Avoidance/joking term pairs for specific in-laws ... institutionalized affinal politics ... high` | **mentions** | Affinal address politics; owned as an inference row, not as an institution. |
| 28 | `corpus/knowledge/civilizations/kongo-kingdom.md:101` | `and dowry was glossed as nzimbu or other named goods (S362, p. 744)` | **mentions** | The corpus's only civilisation-level marriage-payment datum: Kongo dowry denominated in shell money per Bentley's 1895 dictionary, with the file's own caution that `No opened page gives an exchange rate`. D owns the payment institution; it may cite this as the one worked non-Eurasian payment case and must not build a rate on it. `:77` (`the kanda the exogamous matrilineal group from a common ancestress`) owns clan exogamy, not marriage. |
| 29 | `corpus/knowledge/civilizations/persia-sasanian.md:68,139`; `corpus/knowledge/civilizations/aksum-ethiopia.md:74,75` | `Amahraspands and yazads ... Learned categories of beneficent beings/powers`; `Ādurbād ī Mahraspandān ... offered models of remembered priestly and courtly authority`; `Inscriptions invoke Astar, Mahrem, Beher, and Meder` | **hands-off** | Recorded as a census caveat, not a surface: the token `mahr` matches as a **substring** of Mahrem, Amahraspands and Mahraspandān. Four lines of any `mahr`-bearing census are these false positives and none is a marriage term; the D census (bridewealth, bride-price, bride price, dowry, betroth) does not include them. |
| 30 | `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:113` | `Bridewealth ... stock from groom's kin to bride's kin (`animal-symbolism.md:73`); the rights it transfers vary by culture `(to-verify)`` | **owns** | A second, *material* direction rule beside `kinship-terminology.md:88`'s terminological one. Both are `(to-verify)`-grade; D must say which is authoritative for its transfer section (R82-M3 applied inside the corpus) and must not average them. Independently found by `stage/ScoutGap/owners.md` §3; verified here at base. |
| 31 | `corpus/knowledge/culture-material/funerary-material-culture.md:213` | `DR-MMC-08 ... Keep mourning **dress** in `ritual-garments.md` and mourning **color** in `myth-symbol/color-symbolism.md`; this entry owns duration, economy and register ... adopt` | **hands-off** | The corpus's worked *decision-record* shape for a boundary: a DR-id row with an owned/not-owned split and a `path:line` evidence column. ScoutGap recommends D copy this shape (with `binding-speech-complex.md:49-56`'s boundary table); it is the closest in-corpus precedent for D's one-way couplings. |
| 32 | `corpus/knowledge/myth-symbol/purity-pollution-boundary-systems.md:186` | `**What this entry deliberately does not own:** the lexical taboo lifecycle (...), washing as an institution (...), food as system (...), death doctrine (...), rite grammar (...), the register synthesis (...), and canon (lore-shokunin).` | **hands-off** | Named by ScoutGap as a marriage hands-off; precisely, it is a *pattern* precedent (the does-not-own list) and mentions no marriage surface. Recorded so the two readings can be compared: D may copy the list shape; it is not a surface D must answer. |

### 1.3 Coverage of the mandated eight

All eight exist at base and all eight were read at line level: yes — the 17 rows of §1.1 cover
them, and §1.2 adds 15 rows for neighbours outside the mandated list. The two thin surfaces are
complete, not under-read: `culture-material/funerary-material-culture.md` has 2 hits (both
cross-references into ritual-garments' mourning rows) and
`myth-symbol/guest-right-hospitality-law.md` has 2 (`:31`, `:99`); each was verified with the
wider vocabulary and re-checked with the narrow one. The `mahr` token is unreliable as a
substring (see row 29).

---

## 2. One-way couplings the entry must declare

Each coupling is stated in the direction the *pointer* runs. "D -> X" means D's entry points
at X and X does not point back at D (the corpus convention: the newer entry carries the
back-pointer, `guest-right-hospitality-law.md:1-35` is the model).

1. **D -> `linguistics/kinship-terminology.md:80-88,63,149`** — affinal logic, the lexicon
   rule, the levirate/sororate term prerequisites, the prohibited-degrees case, and the
   alliance-theory calibration. Owns the inference; D owns the institution.
2. **D -> `culture-material/trade-economy-lexicon.md:125,166`** — the payment words and the
   contract-token family. D must not gloss `mundr`/`dōs`/`wedlock` a second time.
3. **D -> `culture-material/pastoralism-animal-husbandry.md:23,109`** — herd-as-capital
   transfer. Cross-partition (culture-material -> myth-symbol); the only coupling in this
   list where the *rival* states D's own design rule in advance, so the direction must be
   explicit or the two files will double-own livestock bridewealth.
4. **D -> `culture-material/adornment-body-codes.md:21`** — bridewealth as gendered
   jewellery capital and the Goody & Tambiah baseline.
5. **D -> `culture-material/sumptuary-law-rank-display.md:25,64-69,87,88`** — the
   wives-through-husbands legal grammar and the wedding-day exemption.
6. **D -> `culture-material/ritual-garments.md:1,98-104,140`** — wedding dress; the handoff
   sentence is `:104` (`cloth-giving is dowry politics`).
7. **D -> `myth-symbol/ritual-liminality.md:30,107,116`** — the rite's three-phase grammar.
8. **D -> `myth-symbol/color-symbolism.md:12,55,58,80,134`** — bridal and widow colour codes.
9. **D -> `myth-symbol/heraldry-emblems-identity-marks.md:79,148`** — arms/identity
   transfer on marriage; the worked name-change institution.
10. **D -> `myth-symbol/guest-right-hospitality-law.md:31,35,99,101`** — the heritable
    inter-house bond and the one breach ladder the corpus already owns.
11. **D -> `synthesis/contact-scenario-builder.md:105-116,21,165`** — intermarriage's
    contact and name-transmission effects.
12. **D -> `linguistics/naming-systems.md:103,115,116`** — the life-stage name-slot
    schedule and the in-law taboo register.
13. **D -> `verification/calibration-registry.md:53,118,140`** — the rejected packages D
    must not re-assert (group marriage; kin terms prove practice; totemism+exogamy as one
    package).
14. **X -> D (the one pointer that must run the other way)**: `myth-symbol/motif-index-usage.md:49`
    already reserves a "marriage-system block" it does not own. D is that block; the
    Motif-Index owner does not need to change, and D should name `:49` so a reader can find
    the reservation.

### 2.1 Sibling lane that could claim the surface (report, never absorb)

- **`lore-shokunin`** — the canon lane. It does not own reference knowledge and holds no
  marriage file (`find lore-shokunin -name '*.md' | grep -iE 'marri|bride|dowry|kinship|wedd'`
  returns nothing). What is *load-bearing for D* is its standing boundary: D supplies
  reference and method, `lore-shokunin` decides canon — the same boundary
  `guest-right-hospitality-law.md` `- scope:` writes for itself.
- **Vocabulary collision worth reporting**: `lore-shokunin/reports/r65-alliance-scout.md:1`
  (`# Round 65 alliance source-status scout`) and `r7-alliance-scout.md:1` use **alliance**
  for the citation reciprocal-witness relation, not for Lévi-Strauss's affinal alliance. A
  fleet-wide grep for `alliance` will now return both senses plus D's title. No lane claims
  the marriage surface; two lanes use the word.
- `kotoba-shokunin`, `chousa-shokunin`, `kengaku-shokunin`: no marriage/bridewealth file
  (`corpus/knowledge` exists in each; filename sweep returns nothing).

---

## 3. Claims O and C — existing tool adjacency

### 3.1 Claim O (gate registry)

**Does any tool in `tools/` read the SKILL.md table?** No:
`git grep -ln 'Gates and probes' <base> -- tools/` returns **zero** lines. The 17 base files
holding the string are all under `reports/` (missions, drifts, claims) plus one counter.

| hit | what it does with the surface | relation to `tools/check-gate-registry.py` |
|---|---|---|
| `reports/round-73/accept-ca.py:144` | `REGISTRY_HEADING_RE = re.compile(r"^##\s+Gates and probes\s*$")` — locates the section only, to authorize in-place edits *inside* it (`:70-72`: `in-place edits are authorized only inside SKILL.md "## Gates and probes" or a README footer, and only for a file a ledger pair names in stated_at`) and to seed a fixture at `:1083`. It never enumerates rows or counters. | **No duplication.** One hard constraint: the heading line must stay byte-identical (`^## Gates and probes$`, no suffix, no sub-heading inserted above the table). Renaming it to `## Gates and probes (registry)` reds a frozen counter. |
| `reports/round-70/claims.json:17,20` | A **prior, lapsed claim O on the same surface**: `SKILL.md ## Gates and probes registry gains one row per reports/round-*/accept-*.py counter (36 counters enumerated ...)` with predicate `registry row count for reports/round-[0-9]+/accept-[a-z]+\.py equals the enumerated counter-file count (36)`. Landed 36 rows at `SKILL.md:662-697` per `reports/round-70/corrections-r69.md:15` (`D7 ... gate-registry rows ... 36 rows added`). | **This is the predecessor and the root cause.** Its regex `accept-[a-z]+\.py` cannot match `accept-c81.py`/`accept-d81.py`/`accept-o81.py`/`accept-d82.py`/`accept-o82.py` (letter+digits), so 5 of the 11 current defects are invisible to it, and it has no DEAD direction. Round 70 shipped no counter of its own (`reports/round-70/` contains no `.py`), so nothing ever re-ran the predicate and it lapsed silently. Measured on base bytes the predicate now reads `47` matching rows against `53` regex-matching counter files (6 visible defects of 11) and `58` actual counters. The new tool must **state that it supersedes round-70's predicate**, or the corpus holds two definitions of "registry complete" with different globs. |
| `reports/round-24/audit-gates.md`, `reports/round-24/skill-audit.md`, `reports/round-9/baselines/registry.md`, `reports/round-10/drift/shard-09.md`, `reports/round-18/d4/*`, `reports/round-19/knowledge/skill-draft-b.md`, `reports/round-23/shonen-survey.md`, `reports/round-34/calib/*`, `reports/round-70/corrections-r69.md`, `reports/round-74/ledger.json` | prose audits, drift notes, or ledger entries that *mention* the section | narrative only; none is executable against the table. |

**Second vocabulary hazard (different object, same word).** `tools/check-gate-battery.py`
maintains a *gate baseline registry* (`read_registry`, `REGISTERED_GATE_NAMES`,
`write_registry_fixture`, `:1044-1171`) whose home is `reports/round-9/baselines/registry.md`
— not SKILL.md. Its duty 2 reports `0 uncovered` by discovering pins, so it never requires a
row for an unregistered counter and cannot detect O's defect. The two tools answer different
questions; the new tool's output must not reuse "uncovered"/"baseline" vocabulary, and
`corpus/SOURCES.md` is a third thing also called a registry.

**The note row is a trap for both counts.** Table shape at base: 62 table lines = header +
separator + **60 data rows** (48 rows whose first cell starts `accept`, of which one is not a
gate at all: `SKILL.md:709` `| accept-c-73 / accept-ca-73 correction | note | — | ...`; plus
12 non-counter gate/probe rows). After the 14 new rows land: 74 rows, 61 instruments. The
frozen arithmetic therefore forces the split: `r >= base rows + 14` = 74 counts **all** rows
(so the note row counts in `r`), while `i >= 61` counts instruments and `0 dead` requires
rows that name no instrument to be excluded — the note row's command cell is `—`, so a naive
DEAD rule makes the verdict non-zero on a clean tree.

**Line-shift hazard (second-order, cross-claim).** The only two legal insertion points are
between `SKILL.md:708` (`| accept-ca-75 | ...`) and `:709` (the note row, last per the
"notes at the end" convention), so all 14 rows land at 709-722 and every line at >= 709
moves down by 14 — the closing prose at `:711-727` and `## Source-to-system constraints — round 5`
at `:729`. Committed citations at affected lines: 9 distinct real line numbers
(`709, 710, 713, 715, 716, 728, 729, 730, 732`) in **133 occurrences**, against 316 distinct
`SKILL.md:<line>` citations overall. `SKILL.md:713` (38x) and `:715` (53x) are the hot ones;
`:715` is cited as `17e90b9:SKILL.md:715` in `reports/round-34/calib/C08-verify-reissue.md:192`
(revision-anchored, stays valid) but as a bare `SKILL.md:713-715` in
`corpus/lessons/README.md:261` (not revision-anchored, goes stale). Claim O's `own_paths` are
`tools/check-gate-registry.py` and `SKILL.md` only, so the O seat cannot repair
`corpus/lessons/README.md`; the stale live citations must be routed, not absorbed.

### 3.2 Claim C (cited records)

`git grep -ln 'counter-revisions' <base> -- tools/ reports/` returns zero `tools/` hits; the
surface is read only by a counter's constants and by prose.

| hit | what it does with the surface | relation to `tools/check-cited-records.py` |
|---|---|---|
| `reports/round-80/accept-o.py:635` | `"revision_record": "reports/round-80/counter-revisions.md"` — a claim-specific constant; the counter grades *its own* round's record | **No duplication, but a format precedent.** `reports/round-80/counter-revisions.md` is 3534 bytes and is the template the repaired round-82 record should follow: `# Counter/tool revisions — round 80`, `## Revision 1 (...)`, then a field table `old bytes` / `new bytes` / `what moved` / `predicate moved?` / `recorded behavior change` / `red-befores` / `registry re-derivation` / `counter`, with sha256 + byte counts in the byte cells. The C claim requires only `> 400 bytes` and the two revision hashes `696835ee`, `ea667212`; matching round-80's field shape is free and prevents a third dialect. |
| `reports/round-82/counter-revisions.md` | 0 bytes at base, cited by three committed documents: `SCORECARD.md:1663` (`(\`reports/round-82/counter-revisions.md\`). Do-nothing control: at`), `corpus/lessons/round-82-verifier-spotcheck.md:207-208` (`**Empty record cited as evidence.**` ... `is 0 bytes at \`1d650c8c\``), `corpus/lessons/round-82.md:12` (`r3 \`ea667212…\` are recorded in \`reports/round-82/counter-revisions.md\``) | The defect is exactly as routed; no tool catches an empty record today. |
| `reports/round-73/telemetry/selftest-r2.txt`, `reports/round-80/claims.json`, `reports/round-81/claims.json`, `reports/round-81/telemetry/orphan-sweep-red.txt` | prose/JSON mentions | none executable on the record's bytes. |

**What `tools/` already reads, and what the new checker must not duplicate:**

- `tools/check-cited-lines.py` (round 61) — clause scoping for `S\d{3,}` ids in knowledge
  files (`MULTI-ID` / `TABLE-ID`, `CITED-LINES: <k> finding(s) in <m> file(s)`). This is
  QUALITY criterion 15. Claim D's `>= 20` anchors with exactly one S-id each are graded by
  *this* tool. `check-cited-records.py` must therefore grade record *files* (bytes, path
  shape), not id scoping, or the two tools produce two verdicts on one defect class.
- `tools/check-orphan-evidence.py:93` — `# mask <placeholder> shapes with a sentinel the path
  regex refuses to match after, so \`<scratch>/reports/x.txt\` yields nothing`, with the
  selftest case at `:206` (`("<scratch>/reports/x.txt", None)`). The lane already has a
  path-token scanner and a `<...>` masking convention. `check-cited-records.py`'s "0 scratch"
  leg must mask `<...>` placeholders first, or it will flag the sanctioned `<scratch>/...`
  form as an absolute path; and it must distinguish a host absolute path (a leading `/` plus a
  scratch or temp root) from that placeholder form. The seat-level ban on absolute scratch
  citations in committed reports is the same distinction, one level up.
- No tool today checks that a committed record file is non-empty: `st_size`/`getsize` appears
  only in `tools/d2-typed-labels.py` and its frozen copies, on packet record *lists*. The
  new checker is genuinely novel on the defect that motivated it.
- `tools/check-gate-quotes.py` reads lesson `## Gate` sections (25-word quotation cap);
  `tools/check-row-fragments.py` reads `corpus/SOURCES.md` coverage rows (teaches length,
  URL normalisation). Neither reads the SKILL.md table, so neither collides with O either.

**QUALITY numbering and clause collision.** Criteria end at `30.` (`corpus/QUALITY.md:207`),
so `^31\. ` is free; criterion 30 (`:207-219`) is the shape precedent — title sentence,
`Scope:`, `Check (red-before):`, `Grounded in round-82's measurement (...)`, `Limits, stated:`,
`Binds from round 83`. The string `access date` occurs **nowhere** in `corpus/QUALITY.md`
today, so the third clause is new; but criterion 18 (`:57`) already binds the registry-row
anchor (`one live URL plus a wayback capture of that same page`). Criterion 31's per-row
`URL and access date` is a *weaker and different* obligation on the same cell, so 31 must
declare itself as adding to 18 (as 30 does: `adds to criteria 10, 12, 18, 21, 24 and 27`) or
the two criteria contradict on what a row's source cell must carry.

---

## 4. Claim O — the 14 row names against the existing table

**Arithmetic of "14".** Frozen `claims.json` `after` reads `r >= (base rows + 14)`; its
`before` names exactly **11** base-missing counters and `min_instruments_at_lands: 61` =
58 + 3 round-83 counters. So 14 = 11 base-missing + 3 new, and the claim prose's "the 14
missing rows" is the post-landing count, not the base deficit. The frozen `base_missing`
list is authoritative; this scan reproduces it byte for byte:

`reports/round-76/accept-c.py`, `reports/round-76/accept-ca.py`,
`reports/round-79/accept-ca.py`, `reports/round-79/accept-o.py`,
`reports/round-80/accept-d.py`, `reports/round-80/accept-o.py`,
`reports/round-81/accept-c81.py`, `reports/round-81/accept-d81.py`,
`reports/round-81/accept-o81.py`, `reports/round-82/accept-d82.py`,
`reports/round-82/accept-o82.py`.

**Collision check.** `git show <base>:SKILL.md | grep -c -- '<stem>'` = 0 for all fourteen
stems (`accept-c-76`, `accept-ca-76`, `accept-ca-79`, `accept-o-79`, `accept-d-80`,
`accept-o-80`, `accept-c-81`, `accept-d-81`, `accept-o-81`, `accept-d-82`, `accept-o-82`,
`accept-c-83`, `accept-d-83`, `accept-o-83`). No collision with any row name, any cell text,
or any other table in SKILL.md.

**Order convention.** The table runs by round ascending (`accept-c-53` ... `accept-ca-75`) and
the single `kind = note` row is the last table line, which is the only testable reading of
"round order, notes at the end" (kinds: 57 `gate`, 1 `gate (bounded example)`, 1 `probe`,
1 `note`). It admits the fourteen exactly: the eleven go between `:708` and the note row in
round order (76, 76, 79, 79, 80, 80, 81, 81, 81, 82, 82), the three round-83 rows follow
them, and the note row moves to last-again. Any other placement — appending after the note,
or sorting by row *name* string (`accept-c-76` < `accept-c-81` < `accept-ca-76`, which inverts
round order) — breaks the convention. Sorting by name is the failure mode to guard against
because the round-81/82 files are named `accept-c81.py` and the round-53-76 files
`accept-c.py`; the two namings do not sort into one round sequence.

---

## 5. Contradictions, stated rather than smoothed

1. **D `before` census does not reproduce (numbers).** The frozen sentence says the
   institutional core `bridewealth|bride-price|bride price|dowry|betroth` "appears on 9 files
   and in 27 whose-word lines". At base, that exact regex over `corpus/knowledge` gives **9
   files / 14 lines**; over `corpus/` it gives 13 files / 19 lines; adding `bride` gives 39
   lines / 22 files. No variant tried yields 27. The 9-file half reproduces exactly. The 27 has
   a verified source and a different subject: it is the round-82 run's hospitality census
   (`.ufo/waves/round-82/w1/ScoutGap.md`, sha256 `22ff6a2c…`) at base `c285b2af` (27 lines / 15 files / 255 knowledge files / 0 filename hits, reproduced in §6),
   copied into D's `before` from a different surface. Nothing in the D counter's legs grades
   this sentence, so the reproducible figure is 14/9; "27" should be quoted by no seat. Existing pre-existing 0-byte and shape defects are separate.
2. **O's "14" is a post-landing count, not a base count** (see §4). A seat that reads the
   prose as "14 rows are missing at base" will look for three counters that do not exist yet
   and may add rows for `accept-*` files it invents. Frozen `base_missing` is the authority.
3. **Round-70's committed predicate is now both stale and blind**, and nothing in the tree
   says it was superseded: measured `47` vs `53` (6 visible) against a real deficit of 11,
   because `accept-[a-z]+\.py` cannot match the `accept-c81.py` naming. Two predicates
   defining the same property with different globs is a defect, not a redundancy.
4. **Criterion 31's third clause vs criterion 18.** Both bind a Gate row's source cell;
   18 requires live URL + same-page wayback capture + findable anchor quote, 31 requires URL
   + access date per row. Unless 31 declares itself an addition to 18, one cell now owes two
   different obligations with no stated precedence.
5. **"alliance" is two words in this fleet.** Lévi-Strauss affinal alliance (D's title) and
   `lore-shokunin`'s reciprocal-witness source alliance (`r65`/`r7-alliance-scout.md`) share
   the token; a fleet grep will mix them. Reported, not absorbed.
6. **No seat owns the stale revision-less `SKILL.md:709+` citations** that O's insertion
   creates. O cannot edit `corpus/lessons/README.md` (`own_paths` = tool + SKILL.md); the
   repair needs routing.

---

7. **"S905 duplicates S320" is not a row fact; the real finding is work-level and
   id-contingent.** Verified: at `c285b2af` the registry ends at **S903** and
   `git grep -cE '^\| S90[4-7] '` returns 0 rows, so S904-S907 are *planned* ids from the
   round-82 brief, not rows. At `3088bd7f` S905 is Tacitus, *Germania* (Church & Brodribb,
   Wikisource) at `corpus/SOURCES.md:861` and S320 is *The Poetic Edda*, trans. Bellows (1923),
   Project Gutenberg #73533 at `:349` - different works, so no row-id duplicate exists at either
   base. The durable observation is one level up: the brief's planned Bellows Hávámál row would
   reuse the **same 1923 Bellows translation** already opened as S320 (whose document is the
   complete Poetic Edda, while its `scope` cell names only Völuspá stanzas, Grimnismol 39 and the
   introductory notes, not Hávámál). Cite it as "planned Bellows Hávámál row vs S320 -
   work-level, id contingent", and let the source seat decide whether the poem needs its own row
   or a scope extension; D should reuse S904/S905 as they stand and carry no duplicate claim.


## 6. Reconciliation with `stage/ScoutGap/owners.md` (landed after this scan's first check)

`stage/ScoutGap/owners.md` (23,464 B) and `stage/ScoutGap/gap-census.md` (23,154 B) appeared
after this seat's initial `ls`; both now exist and were read. Reported, not merged.

**Agreements (independent, round-83 artifact versus this scan):** 9 files / **14 lines** for the institutional core; 0 filename
owners of 256; the entry lands as the 257th file and myth-symbol's 35th; no `- couples:` target
names a marriage path; `kinship-terminology.md:80-88` is the strongest partial owner;
`heraldry-emblems-identity-marks.md:79` is the one grounded status-transfer case;
`contact-scenario-builder.md:105-116` owns intermarriage as a contact variable; funerary and
guest-right are hands-off; `calibration-registry.md:53,140` binds D's calibration.

**The "owns" definition collision — the one thing an integrator must not conflate.** In the
round-83 artifact, `.ufo/waves/round-83/w1/stage/ScoutGap/owners.md:15` reads `Measured result:
**0 owns, 7 mentions, 3 hands-off** across the ten named files`, and
`.ufo/waves/round-83/w1/ScoutGap.md:61` reads `**0 owns / 7 mentions / 3 hands-off.**` Its
"owns" is institution-sense only. §1 above reports **10 files that own a sub-surface with a
decision rule**. The two senses are disjoint and both correct: the round-83 artifact asks whether
a file owns *the marriage institution* (answer: none), this table asks whether a file owns *a
surface D would otherwise restate* (answer: ten). The entry needs both readings, in this order:
the absence claim uses the institution sense (`0 owners`), the `- couples:` list uses the
sub-surface sense (the 14 couplings of §2). A reviewer who reads either number against the other
will think one seat miscounted.

**Two ScoutGap artifacts, cited by path (this replaces an earlier single-seat framing).** Two
different runs share the seat name, and an earlier note in this file merged them. They are both
real, both unchanged, and each claim about a document must name its artifact:

| artifact | path | bytes / sha256 / time | what it carries |
|---|---|---|---|
| round-83 run (this wave's mate) | `.ufo/waves/round-83/w1/ScoutGap.md`; `.ufo/waves/round-83/w1/stage/ScoutGap/owners.md`, `gap-census.md` | 6,996 B `7a15c2b3bf166966665f2a48…` 09:28; 23,464 B `64c32143718636193e72ec16…` 09:26; 23,154 B `384c3e8654d805b72cee8481…` 09:28 | `ScoutGap.md:61` `**0 owns / 7 mentions / 3 hands-off.**`; `:68` `**Two files state a direction rule** — kinship:88 (in terms) and pastoralism:113`; `owners.md:15` the same 0/7/3 sentence. This is the table §1 and this section reconcile. |
| round-82 run (the seat that messaged this one) | `.ufo/waves/round-82/w1/ScoutGap.md`; `stage/ScoutGap/{census.sh,gap-census.md,raw-transcript.txt}` | 10,224 B `22ff6a2ca004881a023926b3…` 08:15; 4,364 B `77ec4599…`; 159,077 B `9c174457…`; 144,207 B `14f5c48a…` | `grep -c '0 owns'` = **0**; `grep -c 'pastoralism:113'` = **0**; no `owners.md`; it holds the round-82 hospitality census (27 lines / 15 files / 255 knowledge files at `c285b2af`). |

No contradiction between them, and no revision: the round-82 seat closed at 08:15, the round-83
run wrote at 09:26-09:28, and the earlier "contradicts all three" reading was an artifact of
comparing one seat's message against the other run's files. The earlier note is withdrawn; the
bytes above stand. Consequence for this scan: the 0/7/3 and direction-rule lines are cited as
**round-83** bytes, the 27/15 census as **round-82** bytes, and nothing in §1-§5 changes.

**Where ScoutGap corrected this scan.** `pastoralism-animal-husbandry.md:113` states a material
direction rule (`stock from groom's kin to bride's kin`, `(to-verify)`) that this scan missed;
verified at base and added as row 30. It sits beside `kinship-terminology.md:88`'s terminological
direction note, so D has **two** direction rules of different kinds and must say which is
authoritative rather than average them.

**Where this scan reads the bytes more narrowly.** `purity-pollution-boundary-systems.md:186`
names no marriage surface at base; it is a *pattern* precedent (the does-not-own list), not a
hands-off D must answer — row 32 records the distinction. `funerary-material-culture.md:213`
(DR-MMC-08) is the better shape precedent of the two.

**The stray "27" — provenance verified, not inferred.** `myth-symbol/
guest-right-hospitality-law.md:4` reads `-> 27 lines in 15 files`; that sentence is the round-82
*hospitality* census taken at base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c`, and it reproduces
exactly there: `git grep -icE 'xenia|hospitium|guest-friend|guest-right|guest right|theoxeny|
hospitality' c285b2af -- corpus/knowledge` = **27 lines in 15 files**, against **255** knowledge
`.md` files and **0** filename hits. The entry that carries the sentence does not exist at that
base (it is the 256th file at `3088bd7f`), which is why the census is stated as a gap at all.
So D's `before` copied a round-82 number from a different surface at a different base; the
measured facts stand and are citable: marriage core = **9 files / 14 lines** at `3088bd7f`, and
the landing entry's own `- gap filled:` already says 14 in 9.

**What each table has that the other does not.** ScoutGap: the source-probe readings, the
duplicate-document check against the registry (Hammurabi, EB11 "Marriage", RV 10.85, Leviticus
unregistered; S904/S905 reusable), the index state, and the unowned family-law surfaces
(divorce, inheritance, custody). This scan: the two O/C tool surfaces (§3), the row-name and
row-order checks (§4), the line-level quotes for `trade-economy-lexicon.md:125`,
`naming-systems.md:116`, `sumptuary-law-rank-display.md:25,64-69,88`, `color-symbolism.md:12,55`,
`motif-index-usage.md:49`, and the 11 + 3 arithmetic behind "14".

**One consequence neither table can repair, now recorded by both.** The index footer is stale
and no claim this round can fix it: `corpus/README.md:834` reads `Total knowledge entries: 253.`
with `directory totals 32/32/41/29/24/95`, against base truth **256** files at
`32/34/42/29/24/95`; D's landing makes it 257 while the file still says 253. The README's own
convention is that the landing round appends a block (cf. `:791`, `:802`), but D's `own_paths`
are the entry and `corpus/SOURCES.md` only, and O's are the tool and `SKILL.md`. Route it.
