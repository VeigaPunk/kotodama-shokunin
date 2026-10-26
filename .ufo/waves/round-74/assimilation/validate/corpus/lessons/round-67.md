# Round 67 - 2026-10-24 (hyaku run 5, L1 KotodamaR67)

## Round summary

Three claims at base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`; the
declaration plus frozen instruments (three counters, claims.json, base
dry-runs and do-nothing controls) sit one commit past it at the draft-time
lane tip `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21` ("round-67: declaration
+ instruments ... census start"). One v2 wave of 64 seats ran build and
attack together; build output is a draft under `.ufo/waves/round-67/` and the
L1 is the only committer.

C (coverage, sourced): the medicine / healing / physician / remedy register
is unowned at the base - the word-bounded filename census prints 0
(`.ufo/waves/round-67/rows/ScoutGapMed/gap.md` re-derives it at base
`ad5b52b0`, and the `- topic:` sweep finds only partial-scope mentions:
bathing/body hygiene, scent prophylaxis, myth-symbol apotropaic purity,
civilization notes) - so the round lands one new culture-material entry
`corpus/knowledge/culture-material/medicine-healing-codes.md` supported by
exactly 24 registry rows S805-S828 (tier A or B, opened 2026-10-24, mined,
used-by the entry, each cited once by it). Base counts re-derived read-only:
corpus/knowledge 240 entries, culture-material 33, registry 724 rows; at the
claim's own lands commit the registry reads 752 (S801-S804 already landed by
the earlier records commit A_r, plus the 24 new rows), so corpus / 34
culture-material / 752 registry are the per-lands figures. The two-plus new
gate rejects append only at Ca's later lands commit A_ca, because C's APPEND
leg bounds appended ids to S805-S828 plus S801-S804 (R67-M7). Predicate
ACCEPT-C-67: every leg of `reports/round-67/accept-c.py` prints PASS.

O (operability, capability acquisition): the r65/r66 Ca rejections share one
class - a frozen counter's committed verdict was FAIL at lands because its
carrier leg could only see a records commit that did not exist yet, while the
same predicate re-derived HOLDS at tip. R66-D3 prescribed the fix, and this
round buys it as a tool: `tools/check-receipt-seq.py` lands with receipt
header equality (stamped / evaluated / measured plus tree and counter
sha256), committed-bytes `--lands` evaluation (`git show`, never a moved
worktree, with `moved_past` reported), post-records carrier parentage
(`--topo`), and a `--selftest` the claim pins at 14/14 fixtures. Five pinned
byte-mutants under `.ufo/waves/round-67/stage/mut-o/` fix one failure class
each (equality-always-true, parent-always-true, missing-headers-ok,
no-carrier-pass, tree-unchecked). Predicate ACCEPT-O-67: every leg of
`reports/round-67/accept-o.py` prints PASS.

Ca (calibration, records): the round-66 verifier spot-check
(`corpus/lessons/round-66-verifier-spotcheck.md` section 5) routed five
defects to this lane; each is dispositioned this round:

- R66-D1 (wave evidence undurable: `.ufo/waves/round-66/` entirely
  untracked) -> a committed manifest
  `reports/round-67/dispositions/r66-wave-evidence-manifest.txt` dispositions
  the r66 wave tree (seat reports, spec, registry, row fragments, mutant
  sources tracked at lands; scratch clone trees named excluded with reasons).
  Note for integration: `.ufo/waves/round-66/` was still untracked at draft
  time, so the manifest is the sole durable carrier of that tree.
- R66-D2 (census exit 1: E12 x23 rows under `## Leads`, E11 S753 used-by
  `-`) -> S776 and S779-S800 move into `## Registry` and S753's used-by flips
  to `—`; the validate census must exit 0 at lands. Pre-state is on disk and
  is exactly the defect: `reports/round-67/telemetry/census-start.txt` shows
  `EXIT=1` with 23 E12 lines (S776, S779-S800) plus `E11 S753 missing
  used-by -`.
- R66-D3 (receipt-of-receipts sequencing: the Ca counter's D2 leg could only
  print PASS after the commit it was filed in) -> the `--lands` /
  stamped==evaluated protocol lands across all three counters, the receipt
  records stamped + evaluated + measured revisions plus tree and counter
  sha256, STAMP fails unless evaluated == stamped, evaluations run inside a
  materialized clone at the lands commit, and carrier parentage becomes
  post-records evidence (`--topo`, `reports/round-67/telemetry/post-records.txt`)
  rather than a lands-time leg. `corpus/QUALITY.md` criterion 19 grounds it.
- R66-D4 (no LOG.md / SCORECARD.md round-66 entries) -> LOG.md carries a
  `Round 66` entry and SCORECARD.md an `Axes — round 66` table with
  coverage / operability / calibration rows (base 94209e8f, lands 65fe8572,
  records 4589ebdd; claim-Ca is recorded as unprovable at its committed
  verdict even though the substance verified post-hoc).
- R66-D5 (no first-class rejected rows; repeat of r65) -> S801-S804 land as
  first-class `status=rejected` rows with `REJECTED:` reason and `flip:`
  teaches cells at the earlier records commit A_r, and at Ca's lands commit
  A_ca the round-67 gate rejects (S829-S832 candidates from the two reject
  seats) append beside this lesson for at least two new reject rows opened
  2026-10-24. They cannot append at C's own lands commit: C's APPEND leg
  bounds appended ids to S805-S828 plus S801-S804, so the per-claim lands
  sequence A_r -> A_c -> A_ca is the resolution (R67-M7).

Predicate ACCEPT-CA-67: every leg of `reports/round-67/accept-ca.py` prints
PASS. Leg names do not track defect numbers one-for-one: the frozen counter's
`D1`/`D2`/`SEQ` legs cover R66-D1/R66-D2/R66-D3, its `D3` leg is the R66-D4
ledger restoration and its `D4` leg is the R66-D5 rejection rows; its
`QUOTES` leg also reads this lesson, so this file is inside the Ca claim's
legs array and must be complete in the same commit, not after it. Two
pre-data instrument findings are recorded: R67-M2 (the rev0 Ca `QUOTES` id
count could not pass for any lesson; fixed pre-data, counter re-frozen) and
R67-M7 (the id-bound/lands-sequence conflict between C's APPEND bound and
Ca's rejection requirement; resolved by per-claim lands separation
A_r -> A_c -> A_ca, not by widening the bound). If a frozen leg is ever left
unrevisable, the honest record is a frozen-predicate defect - not a FAIL of
this lesson.

Receipt discipline (the r66 fix this round exists to prove): every r67
counter takes a REQUIRED `--lands <40hex>`; the receipt prints stamped,
evaluated and measured revisions plus the lands tree hash and the counter's
own sha256; STAMP fails unless evaluated == stamped; a run is executed inside
a materialized clone (`git clone --no-local`) at the lands commit, never on a
worktree that may have moved past the stamp. The pre-data controls are on
disk (`reports/round-67/telemetry/controls-{c,o,ca}.txt` plus
`dry-run-{c,o,ca}.txt`): each counter materializes the BASE revision, runs
`--lands <base>` and must fail on base bytes, so a do-nothing control cannot
pass a frozen predicate. The base Ca dry-run does fail on base bytes (for
instance `QUOTES FAIL exit=2 gate_ids=0`, `D1 FAIL bad=['manifest_absent']`,
`D2 FAIL` on the 23 E12 lines), which is the expected shape of a live
predicate, not evidence of a broken counter.

Wave note: the v2 wave ran 64 seats in one task call (`spec-v2.json`);
63 returned reports and every row seat delivered - the four late-landing
fragments (S807, S808, S827, S828) arrived inside the round window, so no
claim shrink and no dead row seat. One seat lane (`ScoutGapMed`) delivered
the census finding as `rows/ScoutGapMed/gap.md` rather than a w1 report.
Seat-level evidence is itemized in
`reports/round-67/telemetry/seat-evidence.txt` (r66) - the r67 wave's own
bundle travels in this commit under `.ufo/waves/round-67/`.

## Gate (rows opened this round; each quote is the anchor quote of that row's own final `row-*.txt` artifact, verbatim)

Draft-time state: the seat's sibling `ScribeGateRows` owns the real Gate lines
at `.ufo/waves/round-67/stage/gate-rows.md` (12.4K when this skeleton was
written; 18,064 bytes at 09:43Z with most opened rows filled - merge that
version, do not trust the MISSING markers below, and re-run its fill recipe at
integration because its F1 records a `teaches` cell that changed between two
reads). When this skeleton was written `.ufo/waves/round-67/rows/` held
`ScoutGapMed/gap.md`, `ScoutRow11/row-S825.txt`, `row-S826.txt` and
`ScoutRow11/rejects.txt` - nothing else. S825/S826 are filled below from those
two fragments' own `ROW=` anchor cells (verbatim; 16 and 13 words); the other
22 opened rows are marked MISSING with the frozen seat topic from
`.ufo/waves/round-67/gen-spec.py` ROW_TOPICS. Integration replaces each line
with `- S### | <live URL> | 2026-10-24 | "<anchor quote 8-25 body words>"`,
copying the quote verbatim from that row's fragment.

- S805 | https://iep.utm.edu/hippocra/ | 2026-10-24 | "the doctrine of the four humors of the body: blood, phlegm, black bile, and yellow bile"
- S806 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5198827/ | 2026-10-24 | "Vata dosha , Pitta dosha and Kapha dosha are collectively called as Tridoshas"
- S807 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8128758/ | 2026-10-24 | "Twelve major meridians were documented in the classic medical book, Huangdi Neijing (written ~2000 years ago)"
- S808 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7427450/ | 2026-10-24 | "Most notable is his 14-volume book, al-Qanun fi al-Tibb or The Canon of Medicine"
- S809 | https://circulatingnow.nlm.nih.gov/2023/01/05/medicine-and-miracle-in-a-medieval-monastery/ | 2026-10-24 | "infirmary could range from a single room just for the monks to a complex of medical buildings including a hospital, pharmacy, baths"
- S810 | https://www.museumaargau.ch/en/legionary-trail/roman-sites/military-hospital-valetudinarium | 2026-10-24 | "At the camp hospital (valetudinarium), military doctors and medical orderlies treated battle injuries, everyday illnesses and work accidents."
- S811 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10621680/ | 2026-10-24 | "one of the oldest and most complete contemporaneous perspectives on Ancient Egyptian healing practices"
- S812 | https://iep.utm.edu/galen/ | 2026-10-24 | "Galen traveled to Egypt (Alexandria) where he lived for perhaps five years (152-157)"
- S813 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8156585/ | 2026-10-24 | "no proof at all of its use during plague outbreaks in Middle Europe"
- S814 | https://www.sciencehistory.org/stories/magazine/paracelsus-the-alchemist-who-wed-medicine-to-magic/ | 2026-10-24 | "For Paracelsus, mastering chemical as well as magical cures was crucial to understanding illness and wellness"
- S815 | https://tischlibrary.tufts.edu/special-collections-badianus-manuscript | 2026-10-24 | "It is the earliest known work on Mexican medicinal practices and treatment of diseases"
- S816 | https://www.himalayanart.org/search/set.cfm?setID=253 | 2026-10-24 | "The Four Tantras was discovered as a 'Revealed Treasure' text (terma) by Draba Ngonshe in the 11th century"
- S817 | https://www.mpm.edu/educators/wirp/great-lakes-traditional-culture/medicine-healing | 2026-10-24 | "The chief purpose of the sweat bath was curative, although it played a prominent role in the ritual of the Midewiwin"
- S818 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2836216/ | 2026-10-24 | "the education of surgeons and apothecaries was an apprenticeship system overseen exclusively by their own guilds"
- S819 | https://www.nlm.nih.gov/exhibition/historicalanatomies/vesalius_bio.html | 2026-10-24 | "Vesalius performed his own careful dissections and observed the body in great detail, confirming and refuting many of Galen's anatomical and physiological tenets."
- S820 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3559034/ | 2026-10-24 | "the first permanent plague hospital (lazaretto) was opened by the Republic of Venice in 1423"
- S821 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8676632/ | 2026-10-24 | "traditional medicine (known as Kampo) is regulated by the government and prescribed by over 90% of physicians"
- S822 | https://www.iranicaonline.org/articles/bimarestan-hospital/ | 2026-10-24 | "hospitals were also the principal centers of medical education and granted diplomas to their graduates"
- S823 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1357167/ | 2026-10-24 | "the Barber's Company was organized in 1308 and established by ordinance in 1376"
- S824 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10476505/ | 2026-10-24 | "isangoma [diviner], inyanga [herbalist] and umthandazi [faith healer]"
- S825 | https://edizionicafoscari.unive.it/riviste/axon/2017/2/guarigioni-di-asclepio-a-epidauro/ | 2026-10-24 | "The Epidaurian Iamata were probably exposed in the stoa-abaton, the place where dream incubations took place"
- S826 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2887322/ | 2026-10-24 | "After Chiso brought acupuncture to Japan from Wu (China) in the sixth century"
- S827 | https://www.gutenberg.org/files/52413/52413-h/52413-h.htm | 2026-10-24 | "medical faculty of Paris, the most celebrated of the 14th century, were commissioned to deliver their opinion on the causes of the Black Plague"
- S828 | https://england.prm.ox.ac.uk/englishness-sailors-charm.html | 2026-10-24 | "In Iceland the guardian spirit of a child was supposed to reside in the caul, which was carefully preserved after birth and kept"

### Rejected rows (first-class `status=rejected`; R66-D5 dispositions and this round's gate rejects)

S801-S804 were vacant at base (`grep -cE '^\| *S80[1-4] '` on the base registry prints 0), which is why the r66 rejection dispositions take those ids; S829-S832 are this round's own gate rejects. Each integrated line carries the row's `REJECTED: <reason>; flip:` finding, not a restated fragment.

- S801 | https://www.penn.museum/sites/expedition/saffron-and-swans-grease/ | 2026-10-24 | "Pliny the Elder tells of such a cream composed of incense and nitre mixed with gum stripped of its bark" — REJECTED: scope cell is Rome's cosmetics trade and that field is already owned (adornment-body-codes.md:68 "## 6. Cosmetics and their vocabulary"; kohl, cerussa, fucus at :71-73), so admitting it re-owns cosmetics rather than extending medicine; flip: open it used-by adornment-body-codes.md, or substitute a materia-medica source for the medicine entry
- S802 | https://www.sciencemuseum.org.uk/objects-and-stories/preventing-infection-lessons-past | 2026-10-24 | "Miasma theory led to positive advancements in medicine, although for the wrong reasons." — REJECTED: the anchor asserts a belief system, and miasma is owned by purity-pollution-boundary-systems.md:58 (proximity/air row naming miasma and the pharmakos), while the scent register's plague-prophylaxis slot is already S791; flip: a source showing what the costume was made of and did — practice, not theory — under the medicine entry
- S803 | https://student-journals.ucl.ac.uk/pia/article/id/489/ | 2026-10-24 | "smell was used in the medieval world as a means to challenge or confirm a relic’s authenticity" — REJECTED: relic-authenticity adjudication is myth-symbol machinery (sacred-topography-pilgrimage.md:33, the P2 relic property; myth-ritual-theories.md:32, Frazer's contact magic), not a scent or medicine practice; flip: admit it under sacred-topography-pilgrimage.md as relic-custody evidence
- S804 | https://asia-archive.si.edu/object/F1905.309/ | 2026-10-24 | "The annual airing of books and clothing to prevent mildew and insects takes place each year in summer." — REJECTED: topical fit fails, because the anchor describes mildew and insect prevention with no aromatic content, so neither the scent nor the medicine register can cite it; flip: a source whose anchor names the aromatic material (incense, scented sachet, aromatic herb) used in the airing
- S829 | https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(96)12240-6/fulltext | 2026-10-24 | none reachable: plain curl gets a Cloudflare "Just a moment..." challenge page (5,632 bytes), never the article — REJECTED: live URL is JS/Cloudflare-walled - plain curl gets HTTP 403 challenge bytes, not the article text, so nothing quotable was opened (QUALITY criterion 10); flip: an openly reachable copy (author host, JISC/open repository scan, or a capture that serves article text)
- S830 | https://collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals | 2026-10-24 | Description field quoted already at S252 ("Wooden disease mask,…"), same object record — REJECTED: live URL is already rowed - registry row S252 owns collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals (object A19437, tier A, mined 2026-10-22); a second row adds no new source; flip: a different record or publication on sanni healing rituals not already registered
- S831 | https://www.jstor.org/stable/44438180 | 2026-10-24 | none reachable: the stable URL returns a JSTOR "Client Challenge" JavaScript shell (HTTP 200, 3,038 bytes of /_fs-ch- assets, "JavaScript is disabled in your browser"), not the article — REJECTED: a plain request gets a JS "Client Challenge" shell, not the article; bypassing it counts as unopened (QUALITY criterion 10, cf. S132); flip: an ordinary-means copy (publisher PDF, library scan, open deposit)
- S832 | https://archive.org/details/b20456943 | 2026-10-24 | none reachable at this URL: the details page is an item record (title/creator/date metadata, BookReader viewer chrome, IN COLLECTIONS, SHOW ALL); the catalogue text lives in separate streams - b20456943_djvu.txt and b20456943.pdf under /download/ — REJECTED: the details page is a metadata/BookReader landing stub; the catalogue text lives in the b20456943_djvu.txt/pdf streams, so this URL resolves to no quotable text; flip: cite the text-stream or leaf-image URL directly


## Mistakes

- R67-M1 (class: receipt-sequencing; mined from round 66, antecedent round
  65). The r66 Ca counter's committed verdict was FAIL for a defect of the
  *receipt*, not of the work: `reports/round-66/telemetry/final-measures-ca.txt`
  records `D2 FAIL bad=[...final-measures-c.txt:no_carrier,
  ...final-measures-o.txt:no_carrier, ...final-measures-ca.txt:no_carrier]`
  with `# measured revision (lane main): 65fe8572...` and no stamped header,
  while at tip the same predicate holds - the receipts' carrier
  `4589ebdd36659060a978d0bb5b41b8c4e275a549` has parent
  `65fe8572822ef83f1750593af77daddf34a1e337`, i.e. the exact
  `measured revision` the receipts name (verified read-only:
  `git log -1 --format='%P' 4589ebdd` -> `65fe8572`). Round 65 is the same
  class one layer earlier: `reports/round-65/telemetry/accept-ca-post-records-fail.txt`
  shows `RECEIPTS FAIL lands=53a60275` with `lands_stamp`/`tree` findings for
  receipts stamped at landed revision
  `3b1b5a6794ea860187a791d88933ae6ab79cdc9c` (and the records commit
  `53a60275` is a child of `3b1b5a67`, verified read-only). Fix: R66-D3 as
  built this round - REQUIRED `--lands`, stamped==evaluated equality before
  any verdict, evaluations inside a materialized clone at lands, carrier
  parentage graded post-records by `tools/check-receipt-seq.py --topo`.
  Captured-by: `reports/round-67/accept-o.py` leg R66 (re-derivation of the
  r66 receipts at tip), the `SEQ` leg of `reports/round-67/accept-ca.py`, and
  the 14/14 selftest the O claim pins.
- R67-M2 (class: instrument-regression; the round's own counter). The r67
  rev0 Ca counter's QUOTES leg put the `S` inside the capture group:
  `reports/round-67/accept-ca.py:272` reads `gate_ids =
  set(re.findall(r"\bS(8[0-2]\d)\b", lesson_text)) & {f"S{n}" for n in
  range(805, 829)}`. `findall` returns `805`, the right-hand set holds
  `S805`, so the intersection is empty for every possible lesson:
  `gate_ids=0`, `QUOTES FAIL`, and `ACCEPT-CA-67` can never print PASS no
  matter how complete the lesson is. Reproduced at draft time: the frozen
  expression returns 0 on `corpus/lessons/round-66.md` (which names
  S779-S800), while `re.findall(r"\b(S8[0-2]\d)\b", ...)` returns 24 on this
  skeleton. The r66 counter did not have the defect -
  `reports/round-66/accept-ca.py:190` counted matches directly
  (`set(re.findall(r"\bS(77[6-9]|7[89]\d|800)\b", lesson_text))`, no
  intersection) - so the regression was introduced by the r67 rewrite. Fix:
  applied pre-data on L1 resolution - `reports/round-67/accept-ca.py:272`
  now reads `re.findall(r"\b(S8[0-2]\d)\b", lesson_text)`, keeping the `S`
  inside the capture, so the same leg counts 24 on this skeleton; the
  counter's sha256 changes from rev0 `5e8915ac...` (the digest recorded in
  `telemetry/dry-run-ca.txt`) and the base control must be re-run against
  the revised counter. If the policy had been "no revision", the honest
  record would have been a frozen-predicate defect, never a FAIL of the
  work. Captured-by: the reproduction above; peer drafts disagreed and both
  are preserved for the canonical judge -
  `.ufo/waves/round-67/w1/ExecCounterSmokeCa.md` finding F4 reports only the
  `clean=True` text, while `.ufo/waves/round-67/stage/gate-rows.md` finding
  F2 asserts the same placeholders "would give `gate_ids=24` and the leg
  `QUOTES` would pass", which the rev0 reproduction contradicted.
- R67-M3 (class: stamp-vs-worktree). A run can print `STAMP PASS` while the
  measured bytes are uncommitted worktree state: the mutation seat's M9
  (uncommitted tier flip on a registry row, worktree != lands) passed with
  `dirty_tracked=True`, and `.ufo/waves/round-67/w1/RevCounterC.md` finding
  F1 reports the same hole and asks that STAMP include an empty
  `git status --porcelain`. Reported by those seats, not re-run here. Fix:
  the claim protocol runs every evaluation inside a materialized clone at
  the lands commit; if the frozen predicate is to catch the class itself the
  STAMP leg has to gate on cleanliness too (L1 decision). Captured-by:
  MutEntryClass M9 row and RevCounterC F1.
- R67-M4 (class: citation-shape). ONEID counts only parenthesized
  `(S\d{3,})` occurrences over the whole entry text, so a bare foreign id
  (`see S099`) and a fabricated extra bullet with no citation both survive -
  the mutation seat's M5 and M10 PASSed - and duplicate citations are caught
  only by that count (M6). Reported by the mutation seat, not re-run here.
  Fix: the entry spec keeps exactly one parenthesized citation per bullet and
  no bare ids; integration re-opens every bullet against its row fragment.
  Captured-by: `.ufo/waves/round-67/w1/MutEntryClass.md` mutant table.
- R67-M5 (class: predicate-vs-intent). `accept-ca.py` leg D4 requires six
  rejected rows *opened 2026-10-24* (`rej_opened_today >= len(R66_REJECTS)+2`),
  while the Ca claim text says only "S801-S804 + >=2 new"; restoring
  S801-S804 with an older opened date would make D4 unpassable, and the leg
  computes `new_rejects` and never uses it (`.ufo/waves/round-67/w1/
  ExecCounterSmokeCa.md` F6). Mitigation in this draft: every rejected Gate
  row below carries opened 2026-10-24. The leg revision (or the date
  decision) belongs to L1. Captured-by: ExecCounterSmokeCa F6.
- R67-M6 (class: wave-planning). At draft time only 2 of the 24 opened-row
  fragments existed (`ScoutRow11/row-S825.txt`, `row-S826.txt`); the other 22
  ids had no `row-*.txt` and no URL/quote could be inlined without
  fabrication. Fragments arrived late (by the sibling's 09:43Z snapshot,
  S809-S820 and S821-S826 were filled; S807, S808, S827 and S828 were still
  absent, and one `teaches` cell changed between reads). Fix: <fill at
  integration - name the dead seats and the ids they still owe, or the
  L1-mined rows; if the claim shrinks, the shrink is named here>. Captured-by:
  `.ufo/waves/round-67/w1/swarm-registry.json`, the `rows/` listing,
  `stage/gate-rows.md` finding F1 and `telemetry/seat-evidence.txt`.
- R67-M7 (class: id-bound vs records, resolved as per-claim lands
  separation). `accept-c.py`'s APPEND leg bounds appended registry ids to
  `set(NEW_IDS) | EXTRA_IDS` = S805-S828 plus S801-S804
  (`reports/round-67/accept-c.py:357`), while `accept-ca.py`'s D4 leg
  requires six rejected rows opened 2026-10-24 (S801-S804 plus at least two
  more; `rej_opened_today < len(R66_REJECTS) + 2`). Any new reject id
  (S829-S832) appended in the commit C is evaluated at therefore prints
  `APPEND FAIL extra=['S829', ...]`, and the claims' own registry arithmetic
  disagrees (C states 724 -> 752 = 728 + 24; Ca implies at least 754). L1
  resolution (no counter or claims revision): per-claim lands separation -
  A_r carries S801-S804 with the r66 dispositions and lands first, A_c is
  C's own lands commit where only S805-S828 append over base (registry 752,
  APPEND bound satisfied), and A_ca is Ca's later lands commit that carries
  the S829+ reject rows plus this lesson. Each counter is run inside a
  materialized clone at its own lands revision with evaluated == stamped, so
  the joint predicate is satisfiable as sequenced, not by widening the
  bound. Captured-by: CriticFrontier's alert
  (`.ufo/waves/round-67/w1/CriticFrontier.md`), the two counter legs quoted
  above, and the per-lands receipts.
- R67-M8 (class: source-integrity, fragment review). Three fragments
  landed out of contract and were repaired at integration, inside this
  commit: S813's fragment asserted the *opposite* of its source - the
  paper's conclusion is that the beak mask has "no proof at all" of
  plague-outbreak use in Middle Europe and the Ingolstadt/Berlin specimens
  look like replicas or art-market fakes (re-fetch of the live URL confirms
  the wording), so the row was recast around the real quote; S814's teaches
  named "iatrochemistry" and "seeding" claims the article does not make
  (dropped to what it says); S824's teaches restated only its quote
  (RESTATE teaches_cov would print 1.00; rewritten to teach beyond the
  typology line). Two more cells ran over the row model's length budget
  (S813 teaches 274, S818 242, both now under 240). Rejected-row fragments
  S829/S830 shipped teaches cells of 274/311 chars and tier=C; the filed
  rows were rewritten under 240 with the REJECTED/flip text kept, per the
  row model. Fix: fragment-first review - every cell re-checked at
  integration, never trusted verbatim. Captured-by: this file's Gate lines
  vs `rows/*/row-*.txt`; counter legs ROWS/RESTATE on the final bytes.
- R67-M9 (class: records-read). S753's round-66 disposition first shipped
  as a status+teaches+used-by rewrite; claim C's frozen APPEND leg only
  permits the generic mutable cells (status/recheck/used-by) or the
  declared S753 used-by flip, so a teaches edit would print
  `immutable_violations=['S753']`. The filed row is the generic-mutation
  shape: status `rejected`, used-by `—`, teaches byte-equal to base; the
  REJECTED rationale lives in S776's teaches cell and this lesson's Gate.
  Captured-by: `accept-c.py` leg APPEND.

