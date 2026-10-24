# readme-plan — corpus/README.md delta for round 66 (claim C, axis: coverage)

Seat: `ScribeReadmePlan`. Draft only — the L1 applies, integrates and is the only committer.
No byte under `corpus/` was written by this seat.

Base: lane tip `94209e8f80969dbac48d56c5d0e2e623635b8616`; `git diff <base> -- corpus/README.md`
is empty, so the hunk line numbers below are exact at the tip.
`sha256(corpus/README.md)` at draft time = `0c04517bcd485feb64b283d934db2037552f5d771449374a5a36f9cb3b26d3e7`.

The topic text is **not this seat's invention** — it is frozen from
`stage/entry-spec.md` §2 (ScribeEntrySpec), which arrived while this draft was in progress and was
then adopted byte-for-byte; §1 of the same file is the TOPIC-trap rule that shapes hunk 1. The edit recipe below matches spec §5 R1-R5, with the one addition this
item owns: the `## Known gaps (frontier)` bullet.

## The delta (four hunks)

1. `revision: 2.18` block above `revision: 2.17` — **the new entry named without `.md`** (see the
   TOPIC trap below; spec §5 R1);
2. `## culture-material/ (32)` -> `(33)` (line 373, single occurrence);
3. one index row between `ritual-garments.md` (l.398) and `sumptuary-law-rank-display.md` (l.399),
   filename order, carrying the entry's `- topic:` payload verbatim in the `ROW_RE` shape
   `` - `name.md` — text`` (backticks, U+2014, one space each side);
4. the Round-66 frontier bullet after the Round-65 one, then `Total knowledge entries: 239.` ->
   `240.` and the footer total/vector `239` / `30/29/32/29/24/95` -> `240` / `30/29/33/29/24/95`.

## Measured before drafting (read-only, this seat)

- Claim C's own base census:
  `git ls-tree -r --name-only 94209e8f… -- corpus/knowledge | grep -ciE '(^|[^a-z])(scent|perfume|aromatic|incense|fragran|cosmetic|unguent)([^a-z]|$)'`
  -> `0` (grep exit 1): no filename owner at the base.
- Live partition counts `ls corpus/knowledge/<part>/*.md | wc -l`: linguistics 30, myth-symbol 29,
  culture-material 32, synthesis 29, verification 24, civilizations 95 = **239**.
  `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` ->
  `totals.files 239`, same six totals.
- Partial-owner census (word-bounded, `corpus/knowledge/**/*.md`) behind the frontier bullet:
  `adornment-body-codes.md` (cosmetic ×8), `bathing-and-body-hygiene.md` (`:3` scent in the bath
  register), `vessel-container-lexicon.md` (`:3`, `:5`, `:38`, `:158` cosmetic/ritual container
  extensions), `timekeeping-instruments.md` (`:26` incense sticks as FIRE clocks),
  `funerary-material-culture.md` (`/cosmetic/` in its own gap/couples text),
  `cuisine-food-lexicon.md` (`:93`, `:139` grave-incense chopsticks),
  `sogdian-silk-road.md` (`:149` Mongolian *küji* "incense" loanword stratum).
  Excluded on purpose: `craft-artisan-lexicon.md`, whose four hits are the temper-line word *nioi*
  ("scent") — a lexical accident, not a scope.

## Measured on this draft (controls run, results as printed)

    git apply --check .ufo/waves/round-66/stage/readme-plan.diff        -> exit 0
    python3 tools/check-readme-revisions.py --readme <new>               -> exit 0, findings 0
                                                                            (1 carried REVISION-ORPHAN:
                                                                            the round-28 unheaded paragraph)
    python3 tools/check-readme-heading.py  --readme <new>                -> exit 0, findings 0

End-state sweep, `reports/round-28/readme/sweep.py`'s own `sweep()` over a scratch tree (symlinks to
the 239 lane files + a synthetic entry whose `- topic:` is exactly the payload below):

    ok True  rows 240  files 240  totals_line 240  totals_ok True  footer_ok True
    topic_mismatch []  missing_from_index []  orphan_rows []  header_drift {}
    footer_live {"total": 240, "dir_totals": [30, 29, 33, 29, 24, 95]}

Against the *unmodified* live tree the same README reads `rows 240 files 239`,
`header_drift {culture-material: declared 33, files 32}`, one orphan row (the entry),
`footer_ok False` — the only residual is the missing entry file, i.e. the expected pre-landing state.

### The TOPIC trap, measured both ways

`accept-c.py`'s TOPIC leg is a **first-match** scan:
`row = next(l for l in rtext.splitlines() if "scent-perfume-aromatics-codes.md" in l)` and then
`topic_payload in row`. The revision block sits above the index, so a `.md` token in it captures the
match. Replayed on this draft (counter code reproduced line-for-line):

    first match with `.md` kept out of the revision note
      -> "- `scent-perfume-aromatics-codes.md` — scent, perfume and aromatics as ..."  TOPIC leg: True
    negative control, `.md` re-inserted into the revision note
      -> "culture-material entry landed (`scent-perfume-aromatics-codes.md`, the scent, ..."  TOPIC leg: False

So: the revision note names `` `scent-perfume-aromatics-codes` `` (no suffix); the index row and the
frontier bullet may use the full filename because both follow the index row. Dropping `.md` from the
revision note is the single load-bearing detail in hunk 1. (The unfixed round-65 precedent at
README line 4 still names `games-play-sport-contests.md`; that entry's TOPIC leg is already behind
the round-65 closure — do not "repair" it here, it is not this round's surface.)

## The delta, verbatim

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -1,4 +1,10 @@
 # kotodama-shokunin corpus index
+
+revision: 2.18 — Round-66 culture-material landing (2026-10-24): one
+culture-material entry landed (`scent-perfume-aromatics-codes`, the scent, perfume
+and aromatics register), its row added in filename order between `ritual-garments.md`
+and `sumptuary-law-rank-display.md` with the entry's `- topic:` text verbatim;
+`## culture-material/` moved 32 → **33**; the totals and footer moved 239 → **240**.
 
 revision: 2.17 — Round-65 culture-material landing (2026-10-24): one
 culture-material entry landed (`games-play-sport-contests.md`, games, play,
@@ -370,7 +376,7 @@
 - `trickster.md` — the trickster as a cross-cultural figure class (Wakdjunkaga, Coyote, Raven, Anansi, Loki, Sun Wukong, Èṣù/Legba, Hermes, Br'er Rabbit) — Hynes's feature set, Radin's Winnebago cycle and its contested evolutionary reading, Hyde's boundary-crosser interpretation, structural and liminal analyses (Lévi-Strauss, Turner, Babcock-Abrahams), institutionalized sacred clowns, and how trickster tales encode the critique of the weak under durable power asymmetry; typology table, design protocol, and calibration flags for building a fictional culture's trickster
 
 
-## culture-material/ (32)
+## culture-material/ (33)
 
 - `adornment-body-codes.md` — the inscribed body as a legible system for fictional cultures — the master claim is that every body code sits in one of three columns, WEALTH (assayable, alienable: jewelry as walking bank account, from Norse hacksilver and ring-giving to bead economies, inalienable heirlooms like the kula shells and pounamu, seal-rings as documents), RITE (inalienable: Polynesian tattoo with its tapu protocol, Māori moko as legal signature, Nuer gar and Yoruba ila lineage scars, Khalsa kesh, mourning hair), and PUNISHMENT (administered by authority: Chinese mò 黥 and Roman stigma, Song convict-soldier face marks, Meiji bans) — and the craft is keeping the columns distinct while designing their leaks; secondary claims: hair is the most regulable body part and therefore the state's favorite (Qing queue, 1871 danpatsu-rei, Merovingian tonsure-deposition, Mexica warrior hair); cosmetics is a vocabulary before it is a pigment (Egyptian kohl → Arabic *al-kuḥl* → English *alcohol*; Greek kosmētikē vs kommotikē; Heian oshiroi/ohaguro; sindoor); greeting and posture are engineered honorific gradients (bow degrees, wai/sampeah, proskynesis, kowtow diplomacy, Byzantine adoratio, homage's immixtio manuum) that fail legibly at embassy scenes.
 - `agrarian-field-system-lexicon.md` — the field system as the substrate under every other material register — the FOUR INSTITUTIONS (parcel, implement, water, claim) that any fictional agrarian economy must name, and the vocabulary each one generates. Master claim: a culture's agrarian lexicon is generated at the seams where three quantities (yield per unit area, water control, labor calendar) meet four institutions, so an author who fixes the peak-labor month, the water source, and the harvest claim first gets the field, plough, measure, and status words almost for free. The entry supplies: a ten-system field typology with labor/tenure/lexical signatures; the plough family (ard, coultered mouldboard, wheeled) as a capacity chain, not a progress ladder; the water chain (source → lift → deliver → right) with the baray/qanat/acequia/paddy cases; rotation and crop-loanword clocks; the harvest tool-and-share vocabulary; the work-unit land measures (jugerum, morgen, acre, hide, carucate); a calibration shelf of the framework's contested claims (heavy-plough revolution, plough→gender, hydraulic despotism, rice culture); and a decision record for authors
@@ -396,6 +402,7 @@
 - `music-instrument-lexicon.md` — music as a cultural system for worldbuilders — how instruments are classified (Hornbostel–Sachs decimals, its famous misplacements, Schaeffner's alternative, folk taxonomies); how scales bind to affect/time/status as emic doctrine (Greek harmoniai, church modes and the octoechos, raga-rasa and thaat/melakarta, maqam, gamelan patet, Chinese wuyin–wuxing and the lü); how instruments get named (material, sound, technique, measurement, number, shape, eponymy, register) and how name-families radiate, drift, and fossilize; ceremonial music registers (court/temple/military/life-crisis, borrowed contact registers); music–myth links (inventor heroes, named divine instruments, musical contests, talking drums) — each section with design levers for a fictional culture
 - `pastoralism-animal-husbandry.md` — herding and animal husbandry as a production register for fictional cultures — the standing herd as living capital; species portfolios and ecology; mobility systems (nomadic, transhumant, agro-pastoral, enclosed); the herd lexicon and ownership marks; primary and secondary products; herd wealth, loans, bridewealth and raiding; pasture tenure and commons; pastoral–sedentary interdependence; the ritual ledger of the flock; and the calibration traps (stage ladders, the "pure nomad", the cattle complex, the universal tragedy of the commons)
 - `ritual-garments.md` — How clothing does ritual work, as a worldbuilding system: four load-bearing frameworks (garment-as-office and investiture; donning-as-rite with fixed order and formula; Turner's bipolar symbol applied to cloth; dress-as-register with loanword strata); cross-cultural priestly typology — Hebrew bigdei kehuna (eight garments, the b.Arakhin 16a atonement map, the Yom Kippur linen reduction, Philo/Josephus cosmic allegory), Buddhist kāṣāya/ticīvara and the East Asian kesa (strip-count grades, paddy-field patch grid, per-school palettes, the kāṣāya→jiāshā→kesa loan chain), Christian Roman and Eastern vestments (amice/alb/stole/chasuble, omophorion/sakkos, vesting prayers as performative speech, the GIRM color calendar), Shinto jōe/kariginu/kanmuri and miko dress, plus Hindu yajñopavīta and ochre sannyāsa, Islamic ihram, Daoist fǎyī; the Chinese twelve ornaments of imperial dress as cosmology worn; lifecycle-rite dress — wedding white/red variance with calibration, mourning systems (Chinese wǔfú grades, keriah and sackcloth, European black and deuil blanc, Victorian stages, East Asian white), coming-of-age dress changes (toga virilis, guānlǐ/jílǐ, bar/bat mitzvah, furisode/seijin-shiki, Navajo kinaaldá); cloth-economy mechanics (dye scarcity, sumptuary law, inalienable regalia, khil'a robes of honor); build order, calibration, and canon boundary
+- `scent-perfume-aromatics-codes.md` — scent, perfume and aromatics as a material-culture register — how a culture names and classifies smells, sources aromatic materials, extracts and compounds them, burns them as incense, wears them as unguents and oils, reads them as medicine, and moves them along trade routes — a sourced design reference for fictional scent practice, not a universal history of smell
 - `sumptuary-law-rank-display.md` — what the law does to clothing when hierarchy needs to be readable — Roman purple and the clavus, Tang/Ming color-and-badge administration, Edo status outfit and the hidden-luxury dialect, English price-schedule statutes and the cap act, casta dress-as-evidence in colonial Spanish America, Mexica cotton monopoly as the deep layer — organized around one craft claim: a dress law is a semiotic machine, it regulates a SIGN (color-grade, fiber, price-per-ell, stripe width, badge, fur), and it only survives where the sign is assayable; the second craft claim is that each statute is written in a small repertoire of recurring formulae ("no person under the degree of...", forfeiture-to-the-informer, wedding-day exemptions, wives-through-husbands clauses) that can be lifted whole into a fictional culture's legal register
 - `textile-technology.md` — the material substrate of dress for a fictional culture — fiber hierarchy (linen/wool/silk/cotton/hemp) and the prep labor each demands; dye chemistry, fastness classes, and prestige trade (Tyrian purple, indigo vs woad, madder, kermes vs cochineal, fugitive yellows); loom typology and the forensic signatures each loom leaves in the cloth; fulling/finishing as the expensive half of production; and a "four gates" framework for deriving which costume words a technology can and cannot generate
 - `timekeeping-instruments.md` — the timekeeping instrument as a material-culture system for fictional cultures — the five instrument families that measure the day before and beside the clock (SHADOW: gnomon, obelisk, the sundial families Vitruvius catalogues, portable dials; FLOW: the clepsydra as legal timer and its constant-head fix; FIRE: calibrated candle, lamp and incense measures; SKY: decan star clocks, the astrolabe, the nocturnal; WHEEL: the escapement, tower clock, pendulum, chronometer, quartz) each with its resolution, failure mode and what it leaves in the ground; the variable-hour (temporal) regime against the equal-hour regime as the single biggest design decision, with Roman, monastic, Islamic, Edo Japanese and Italian-hour anchors; the unit ladder by which an instrument's resolution becomes the smallest unit a culture can *name* (hour → minute → second, sexagesimal inheritance) and what each rung enables; the institutions a time device generates (bell and tower, curfew, market bell, night watch, canonical hour, muwaqqit, timekeeper office, clockmakers' guild, standard time); the ownership question — temple, palace, city, state or employer — as the axis that decides whether time is public or private; the archaeology of timekeeping (what survives, what decays, what an in-world antiquarian can read); a calibration bank of legend-grade and contested items (Alfred's candles, the monks-invented-the-clock story, Salisbury's 1386 date, Chinese-to-European escapement diffusion, clock-as-cause-of-industrialism, sundial-time = clock-time); a twelve-row decision record; a build order with one NON-CANON worked example. Reference knowledge and method only; canon decisions belong to lore-shokunin.
@@ -689,12 +696,24 @@
   do not edit the old runners.
 - Round 64 adds one linguistics entry, `linguistics/language-socialization-and-acquisition.md` (language socialization and acquisition as culturally organized participation in language). The topic had 0 filename owners and 0 topic-line owners before it; partial one-way owners remain `gesture-co-speech-pointing.md`, `naming-systems.md`/`kinship-terminology.md`, and `sociolinguistics-registers.md`.
 - Round 65 adds `games-play-sport-contests.md` as a sourced culture-material register. Partial scopes remain in `linguistics/orality-formulaic-language.md`, `culture-material/music-instrument-lexicon.md`, `civilizations/taino.md`, and `culture-material/calendar-festival-systems.md`; the entry points to these without claiming a universal game taxonomy or canon.
-
-Total knowledge entries: 239.
+- Round 66 adds `scent-perfume-aromatics-codes.md` as a sourced culture-material
+  register (scent, perfume, aromatics and incense). The base had 0 word-bounded
+  filename owners and 0 whole-register topic owners; partial one-way scopes
+  remain in `culture-material/adornment-body-codes.md` (cosmetic use),
+  `culture-material/bathing-and-body-hygiene.md` (perfumed bathing),
+  `culture-material/vessel-container-lexicon.md` (cosmetic and ritual
+  containers), `culture-material/timekeeping-instruments.md` (incense clocks),
+  `culture-material/funerary-material-culture.md` and
+  `culture-material/cuisine-food-lexicon.md` (passing incense/cosmetic
+  mentions), and `civilizations/sogdian-silk-road.md` (an incense loanword);
+  the entry points to these without claiming a universal perfume history or
+  canon.
+
+Total knowledge entries: 240.
 
 Counts checked 2026-10-24 from the repo root:
 `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
-(total 239 files; directory totals 30/29/32/29/24/95).
+(total 240 files; directory totals 30/29/33/29/24/95).
 The inventory counts markers, not verified facts.
 Superseded reading, preserved as the dated record it was: this footer read
 `(total 199 files; directory totals 19/19/18/29/20/94)` from round 20 through
```

A pre-applied whole file is kept at `stage/_readme-build/README.new.md`
(sha256 `ea9276354734acf10a8c9f8c7174f4c09397efe82eb31c6da36d222ce2fee350`, measured after the
frozen topic was adopted), so the L1 can `diff` it instead of trusting the hunks.
Apply with:

    git apply .ufo/waves/round-66/stage/readme-plan.diff      # validated exit 0 at the tip

## Row text, stated separately (byte-equal is the contract)

    - `scent-perfume-aromatics-codes.md` — scent, perfume and aromatics as a material-culture register — how a culture names and classifies smells, sources aromatic materials, extracts and compounds them, burns them as incense, wears them as unguents and oils, reads them as medicine, and moves them along trade routes — a sourced design reference for fictional scent practice, not a universal history of smell

Source of truth: `stage/entry-spec.md` §1/§2, which states the payload is one physical line, has no
period, and is what both legs compare. `reports/round-28/readme/sweep.py` requires **equality** with
`topic_of()` (payload, continuations space-joined); `accept-c.py` requires it as a **substring** of
the first matching README line. Both are satisfied above (measured).

If the built entry ends up with a different `- topic:` line than the spec's, do not hand-edit the
row — copy the entry's payload in with this tested one-row rewrite (exercised on a differently
worded, three-line payload: exit 0, row then equal to `sweep.topic_of()`, scratch lane removed):

    python3 - <<'PY'
    import re, pathlib
    e = pathlib.Path("corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md").read_text()
    m = re.search(r"^- topic:(.*?)(?=\n- \w)", e, re.M | re.S)
    topic = " ".join(p.strip() for p in m.group(1).strip("\n").splitlines() if p.strip())
    r = pathlib.Path("corpus/README.md"); t = r.read_text()
    t2 = re.sub(r"^- `scent-perfume-aromatics-codes\.md` — .*$",
                "- `scent-perfume-aromatics-codes.md` — " + topic, t, count=1, flags=re.M)
    assert t2 != t or topic in t
    r.write_text(t2)
    PY

It rewrites exactly one row (`count=1`), so it cannot create a duplicate row, and it leaves the
revision note untouched.

## Verify after the entry lands (L1, one pass)

    python3 reports/round-28/readme/sweep.py                  # exit 0, rows 240 files 240, totals_ok True
    python3 tools/check-readme-revisions.py                   # exit 0, findings 0
    python3 tools/check-readme-heading.py                     # exit 0, findings 0
    python3 -B reports/round-66/accept-c.py --root .          # TOPIC + SWEEP legs ride on the above

## Findings (this seat)

1. **Frozen**: the topic payload and the `.md`-less revision note are both from `stage/entry-spec.md`
   (§1 trap, §2 head block, §5 R1-R5). The one deviation from the spec's recipe is hunk 4's frontier
   bullet, which the spec lists as optional and which this item's assignment requires; it sits after
   the index row, so it cannot capture the TOPIC first-match (verified by the replay above).
2. The frontier bullet names `cuisine-food-lexicon.md` and `funerary-material-culture.md` as
   *passing mentions* rather than partial registers, because that is what they are; it does **not**
   name `craft-artisan-lexicon.md`, whose hits are the temper-line word *nioi*. Naming it would
   inflate the partial-owner set and misstate the base census.
3. Convention choice, stated: the footer's "Superseded reading" paragraph has not been appended to
   since revision 2.0 and the tail "Index rows re-measured" block stops at round 35; this delta
   matches that precedent and touches neither. `Counts checked 2026-10-24` and its backticked command
   are unchanged and still true — only its two numbers move.
4. The 2.18 revision block is convention, not a gate (`check-readme-revisions.py` passes without it),
   but every landing since 2.5 has one and the spec's R1 prescribes this one. Hunk 1 is the only
   non-counter-checked hunk — and, per the TOPIC replay, it is also the hunk that can break the
   counter if it is spelled with `.md`.
5. No tool installed or upgraded for this seat.

Report: .ufo/waves/round-66/w1/ScribeReadmePlan.md
