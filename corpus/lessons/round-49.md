# Round 49 — lesson (kotodama, kaika wave 2)

source: `reports/round-49/claims.json` + `reports/round-49/claims-addendum-kaika.json` (declarations); `reports/round-49/validation.json` (acceptance receipt); the URLs opened in `## Gate`
verified-at: 2026-10-19 — lane worktree `kaika/round`, base `c42d675`; Gate rows opened the same day
recheck: whenever a `corpus/SOURCES.md` row's `status`, `recheck` or `used-by` changes (log old→new in that round's lesson), and on the per-row `recheck` cadences
scope: the round-49 record — Gate evidence for SOURCES S001–S043, pre-landing registry normalizations, mined mistakes and frontier; it admits nothing and certifies no verdict

Round 49 closes the declared-and-dispatch-blocked round (`reports/round-49/claims.json`,
C + Ca) and fills the third claim slot with the kaika campaign's sources capability
(`reports/round-49/claims-addendum-kaika.json`, S). Claims: **C** coverage —
`culture-material/hunting-foraging-subsistence.md`; **Ca** calibration — the dangling
`revision: 2.0` README stub removed and `tools/check-readme-revisions.py` landed;
**S** depth / capability — `corpus/SOURCES.md` (43 rows opened 2026-10-19). Verdicts live in
`reports/round-49/validation.json` and `LOG.md`; this file is the record the contract asks
for: the `## Gate` evidence for every new SOURCES row, the registry changes made before
landing, and the lane's mined mistakes.

## Gate

Every row in `corpus/SOURCES.md` S001–S043 was opened on 2026-10-19 by the seat that
wrote it (S001–S015 R49SourcesA, S016–S030 R49SourcesB, S031–S043 the L1 integrator,
after the entry seat died on a provider rate limit). Fragment temp ids were renumbered
contiguously at merge (S201–S215 → S001–S015, S301–S315 → S016–S030, S101–S113 →
S031–S043), which keeps S001–S030 aligned with the wave-1 ART dossier's draft ids.
Quotes are verbatim, ≤25 words, with their location.

Per-row open evidence, all accessed 2026-10-19; quotes verbatim, ≤25 words.

- S001 — https://glottolog.org/about.html — accessed 2026-10-19 — About → Contributing: "Glottolog data is curated in a public repository at https://github.com/glottolog/glottolog." Grounds: versioned, citable catalogue.
- S002 — https://github.com/cldf-datasets/wals — accessed 2026-10-19 — README How to cite: "the derived dataset using the DOI of the particular released version you were using". Grounds: dual citation norm.
- S003 — https://github.com/phoible/dev — accessed 2026-10-19 — README Citing PHOIBLE: "make use of the most recent release in your own analyses, rather than working from the tip of the master branch" (trimmed to ≤25 words by the integrator). Grounds: pin releases.
- S004 — https://github.com/grambank/grambank — accessed 2026-10-19 — README Description: "Global dataset of structural linguistic features, part of Glottobank. This dataset is licensed under a CC-BY-4.0 license". Grounds: scope and licence.
- S005 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283218 — accessed 2026-10-19 — Abstract: "a new database of 210,903 kinterms from a global sample of 1,229 spoken languages". Grounds: dataset identity.
- S006 — https://datsemshift.ru/ — accessed 2026-10-19 — home page: "A semantic shift is defined as a pair of meanings, A and B, that are connected to each other through a process of semantic derivation." Grounds: what a row is.
- S007 — https://d-place.org/about — accessed 2026-10-19 — Overview: "All cultural descriptions are tagged with the date to which they refer and with the ethnographic sources that provided the descriptions." Grounds: provenance tagging.
- S008 — https://zompist.com/kit.html — accessed 2026-10-19 — order-of-steps paragraph: "Working backwards (e.g. creating a text and then devising a grammar to match) will lead to an inconsistent if not incoherent work." Grounds: pipeline order.
- S009 — https://cals.info/statistics/ — accessed 2026-10-19 — Quick numbers: "97.9% of all features are from WALS". Grounds: census, not evidence.
- S010 — https://github.com/def-gthill/lexurgy — accessed 2026-10-19 — README Welcome: "It allows the user to simulate historical changes in spoken languages by applying regular rules to a list of words." Grounds: what it does.
- S011 — https://chridd.nfshost.com/diachronica/ — accessed 2026-10-19 — Some notes about sources and data files: "I (chridd) did not write the Index Diachronica itself." Grounds: trace to the cited source.
- S012 — https://arxiv.org/abs/2508.06094 — accessed 2026-10-19 — Abstract: "a multi-hop pipeline that decomposes language design into modular stages -- phonology, morphology, syntax, lexicon generation, and translation." Grounds: staged pipeline.
- S013 — https://www.ruthenia.ru/folklore/thompson/indexleft.htm — accessed 2026-10-19 — title block: "Please write me about errors etc" (digitization solicits corrections). Grounds: check load-bearing IDs against print.
- S014 — https://www.theomeder.nl/momfer.pdf — accessed 2026-10-19 — pp. 39–40: "the index lists seventy-two motifs twice under different headwords" (accessibility section). Grounds: measured index defects.
- S015 — https://github.com/KatjaMellmann/TMI_as_CSV — accessed 2026-10-19 — README: "The main purpose of the csv file is to generate a reference table within a relational database". Grounds: ID-existence check, not search.

- S016 — https://www.folklorefellows.fi/ffc-284-286-2024-edition/ — accessed 2026-10-19 — edition page opening summary: "The ATU catalog is constituted of international types, practically defined as identified among three or more cultural or national groups."
- S017 — https://www.ruthenia.ru/folklore/berezkin/eng.html — accessed 2026-10-19 — motif entry a1: "The old sun. Another sun, usually less benevolent and/or powerful, existed before the present one."
- S018 — https://pubmed.ncbi.nlm.nih.gov/26909191/ — accessed 2026-10-19 — abstract: "we show that these oral traditions probably originated long before the emergence of the literary record".
- S019 — https://search.isebel.eu/ — accessed 2026-10-19 — welcome page: "this search engine harvests folktales and metadata from five European regions: the Netherlands, Flanders, Denmark, North-East Germany and Iceland".
- S020 — https://arxiv.org/abs/2603.19283 — accessed 2026-10-19 — abstract: "identified 2,670 motif expressions of 200 different motifs across 58,450 sentences for training and testing".
- S021 — https://arxiv.org/abs/2606.17350 — accessed 2026-10-19 — abstract: "common mitigation strategies, including negative prompting and temperature scaling, fail to meaningfully address this homogeneity".
- S022 — https://perio.do/technical-overview/ — accessed 2026-10-19 — §Authorities: "Belonging to the same authority does not imply any semantic relationship between periods, other than sharing a source."
- S023 — https://www.nature.com/articles/s41597-025-04516-9 — accessed 2026-10-19 — §Methods: "polities occupy at least 5000 km2 and have a duration of at least 50 years".
- S024 — https://terminology.collectionstrust.org.uk/ICOM-costume/vbt_ie.htm — accessed 2026-10-19 — Introduction (Anne Buck): "They apply to fashionable and unfashionable dress within the orbit of European style."
- S025 — https://www.getty.edu/research/tools/vocabularies/aat/about.html — accessed 2026-10-19 — §Purpose: "The AAT contains generic terms; it contains no iconographic subjects and no proper names."
- S026 — http://lexisproject.arts.manchester.ac.uk/research/ — accessed 2026-10-19 — Research outline: "an analytical corpus of medieval dress and textiles terminology of the British Isles in the form of a searchable database".
- S027 — https://iconclass.org/en/_ — accessed 2026-10-19 — top-level outline, division 9: "Classical Mythology and Ancient History" (list runs 0–9; division 7 reads "Bible").
- S028 — https://www.folkloredatabase.com/ — accessed 2026-10-19 — home page Important notice: "expressly reserves all rights in relation to text and data mining, automated extraction, scraping, machine learning".
- S029 — https://aras.org/ — accessed 2026-10-19 — Archive Search section: "The ARAS Archive contains about 18,000 photographic images, each cross-indexed, individually mounted, and accompanied by scholarly commentary."
- S030 — https://www.vulgarlang.com/ — accessed 2026-10-19 — home page: "Trial the demo version with a 200 word output. Signup for a 4000 word vocabulary and extra features."

All accessed 2026-10-19 by the L1 integrator; quotes verbatim, ≤25 words.

- S031 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287101 — accessed 2026-10-19 — Results, para. 1: "Of the 63 different foraging societies, 50 (79%) of the groups had documentation on women hunting." Grounds the frequency and its sample.
- S032 — https://api.crossref.org/works/10.1016/j.evolhumbehav.2024.04.014 — accessed 2026-10-19 — (DOI record; publisher page 403) — title field: "Female foragers sometimes hunt, yet gendered divisions of labor are real: a comment on Anderson et al. (2023) The Myth of Man the Hunter". Grounds the title-level position only.
- S033 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0309543 — accessed 2026-10-19 — opening paragraph: "concerns were raised about the reliability and replicability of the results." Grounds the contested status.
- S034 — https://api.crossref.org/works/10.1017/CBO9781139176132 — accessed 2026-10-19 — publisher abstract: "challenges the preconceptions that hunter-gatherers were Paleolithic relics living in a raw state of nature". Grounds the anti-relic programme.
- S035 — https://api.crossref.org/works/10.2307/2801707 — accessed 2026-10-19 — record fields title "Egalitarian Societies", container "Man", volume 17, issue 3, page 431, issued 1982-09. Grounds identity only.
- S036 — https://api.crossref.org/works/10.1086/203816 — accessed 2026-10-19 — title field: "Foragers, Genuine or Spurious?: Situating the Kalahari San in History [and Comments and Reply]". Grounds identity and framing only.
- S037 — https://www.culturalsurvival.org/publications/cultural-survival-quarterly/ecologically-noble-savage — accessed 2026-10-19 — section The European Ideal: "The recently accumulated evidence, however, refutes this concept of ecological nobility." Grounds the rejection.
- S038 — https://www.routledge.com/Stone-Age-Economics/Sahlins/p/book/9781138702615 — accessed 2026-10-19 — Description: "Sahlins concludes, controversially, that the experiences of those living in subsistence economies may actually have been better, healthier and more fulfilled". Grounds the contested status.
- S039 — https://press.princeton.edu/books/paperback/9780691084428/foraging-theory — accessed 2026-10-19 — description para. 1: "present the basic “average-rate maximizing” models and their extensions." Grounds optimality models as the book's subject.
- S040 — https://api.crossref.org/works/10.2307/279653 — accessed 2026-10-19 — abstract: "Hunter-gatherer subsistence-settlement strategies are discussed in terms of differing organizational components, "mapping-on" and "logistics,"". Grounds the two mobilities.
- S041 — https://api.crossref.org/works/10.1126/sciadv.abd0310 — accessed 2026-10-19 — abstract: "a sample that includes 10 other females in statistical parity with early male hunter burials." Grounds the archaeological corrective.
- S042 — https://d-place.org/parameters/EA001 — accessed 2026-10-19 — Description: "Dependence on the gathering of wild plants and small land fauna, relative to other subsistence activities." Values table: 722 / 265 / 118 / 62 / 48 / 35 / 31 / 6 / 3 / 0 (sum 1290).
- S043 — https://www.sciencedaily.com/releases/2023/10/231020145921.htm — accessed 2026-10-19 — full story para. 3: "Through a review of current archaeological evidence and literature, they found little evidence to support the idea that roles were assigned specifically to each sex." Grounds the rejection: a summary, not the evidence.

### Post-review supersession rows — opened 2026-10-19

- S044 — https://api.crossref.org/works/10.1017/CBO9781139176132 — accessed 2026-10-19 — publisher abstract: "In this book, Robert L. Kelly challenges the preconceptions that hunter-gatherers were Paleolithic relics living in a raw state of nature". Grounds the publisher's summary; supersedes S034 at tier B.
- S045 — https://www.routledge.com/Stone-Age-Economics/Sahlins/p/book/9781138702615 — accessed 2026-10-19 — Description: "Sahlins concludes, controversially, that the experiences of those living in subsistence economies may actually have been better, healthier and more fulfilled". Grounds the publisher's description; supersedes S038 at tier B.
- S046 — https://press.princeton.edu/books/paperback/9780691084428/foraging-theory — accessed 2026-10-19 — description paragraph 1: "present the basic “average-rate maximizing” models and their extensions." Grounds the publisher's description; supersedes S039 at tier B.
- S047 — https://aras.org/ — accessed 2026-10-19 — Archive Search: "Available to our members"; Supporting ARAS: "universal connections that symbols allow us to make". Grounds the member-access and universal-framing rejection; supersedes S029.

## Registry changes before landing (integrator normalizations, logged per contract rule 2)

The registry is new this round, so these are not in-place edits of filed rows; they are
recorded because they are not the row authors' original values.

- S028, S029, S030, S043 `recheck` `—` → `365d` (rejected rows re-test their flip yearly).
- S001 `used-by` dropped `civilizations/hopi.md`, `civilizations/ottoman.md`,
  `synthesis/costume-language-coupling-table.md`; S002 `used-by` dropped
  `civilizations/china-qing.md`, `civilizations/malagasy-madagascar.md` — those files cite
  only the sites' bibliographic reference records (`glottolog.org/resource/reference/…`,
  `wals.info/refdb/…`), not the catalogue or dataset each row scopes (R49Critic finding).
- S004 `status` `mined` → `queued`, `used-by` `civilizations/siam-thai.md` → `—` (it cites a
  Grambank source record, `grambank.clld.org/sources/…`); S007 and S013 `used-by` dropped
  `civilizations/mesoamerica-primary-sources.md` (a D-PLACE source record; its "Thompson" is
  a Paris-Codex dating attribution, not the Motif-Index) (R49Critic findings).
- Class lesson: a substring hit on a site name is not a citation of the row's scope —
  a `mined` row's `used-by` must cite the catalogue/dataset/work the row scopes.
- Anchors given a revision or open date (contract: never undated): S007, S008, S017,
  S022, S025, S026, S029 (row authors' fragment fixes) and S010 (master `fa50277`,
  2026-06-18, release v1.7.6, read by the integrator from the GitHub API). S013 `tier`
  A → B: an individually maintained digitization of the print index is a strong
  secondary for motif identity, not the primary (R49Reviewer finding).
- S003 Gate quote trimmed from 26 to 21 words (R49Critic finding).
- Entry `hunting-foraging-subsistence.md`: claims tied to S032, S035, S036 (bibliographic
  record only) re-scoped to `(to-verify)`; S038 quote corrected to the page's
  "concludes, controversially"; the S040 risk sentence narrowed to what the abstract
  says; a dependence-calibration paragraph added from S042's counts; the Kelly quote
  re-spliced to the abstract's own words, meat-for-crops exchange and `inuit.md:136-137`
  corrected (R49EntryB), and a §13 status row added for Binford's mapping-on / logistics
  split (R49Reviewer's QUALITY criterion 2 block).

## Mistakes

Scribe stamp (R49Scribe): read-only verification **2026-10-19T21:28–21:33Z**, Ca post-fix correction
**21:38–21:39Z**; lane worktree
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotodama-shokunin`, HEAD `c42d675`
(clean tree at the first stamp; the Ca fix landed mid-write at 21:37Z — see the
dated correction before `## Frontier`). Source dossier:
`../fleet-ledger/.ufo/waves/kaika-w1/kotodama-state.md` §4 (`:114-133`) and §5
(`:138-185`; the lessons finding at `:172`). Every pointer below was re-executed against the live tree; corrections
to the dossier are marked **[corrected]**. This is a record, not a fix: no filed byte,
QUALITY criterion, or convention was edited.

**README citation basis.** `c42d675:corpus/README.md:N` = the round's base bytes;
`sha256:666fb794:corpus/README.md:N` = the current rev-2.6 bytes measured
2026-10-19T22:03Z (`sha256sum corpus/README.md` → `666fb794…`, 609 lines). Earlier
stamps are named where they occur: `5fd038b6…` (rev-2.6 first apply, 22:01Z),
`097c2910…` (post-Ca, pre-rev-2.6), and commit-qualified `git show ce103bf…`.
The integrator has **not declared the README frozen**; each stamp binds only its
own sha, and rev-2.6 edits shift every line below `:22`. Line numbers decay on
every apply; the quoted content plus the sha is the durable cite (the r48 Ca01
§5 self-decaying-cite class). Any consumer must re-measure before quoting.

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| r2, r4 — rejected (historical) | `SCORECARD.md:4` "including rejected rounds 2 and 4" | record: `corpus/lessons/round-2-adjacency.md`, `corpus/lessons/round-4-sol-fixes-and-audits.md` | none — historical |
| r7 — acceptance recorded false; the F claim's wrong rejection called "a preservation failure" | `reports/round-7/validation.json` (`acceptance_checks_passed: false`); `c42d675:corpus/README.md:490-491` verbatim; current `sha256:666fb794:corpus/README.md:510-511` | append-only correction pattern (r22 correction entry, `corpus/lessons/round-22.md`) | none owed — correction recorded |
| r11 — F failed as declared: `0.778 < 0.95` 24h hash-stability threshold | fleet `.ufo/l0-questions.md:47`; `LOG.md:3010` (header), `:3022` ("= 0.778 < 0.95"); `SCORECARD.md:543` | **none** — freshness paused until the operator rules; no QUALITY/SKILL criterion | **uncaptured** — L0 row open |
| r13 — operator-skipped | `SCORECARD.md:148` "rounds 8-16 (r13 operator-skipped)" | record (`corpus/lessons/README.md` §5: no round-13 file) | none — record fact |
| r17, r22 — REJECTED on claim D (×2) | **[corrected]** `LOG.md:3223` (r17), `LOG.md:3298` (r22). The dossier's "LOG headers 1081, 1156" does not resolve: `sed -n '1081p;1156p' LOG.md` holds unrelated text | `corpus/lessons/round-17.md`, `round-22.md` + correction entry | none — rejections on record |
| r33 — F-C13-1: filed receipts written in-tree during the wave (restored) | `LOG.md:3548` (incident record header) | `tools/harness/receipt_guard.py` (selftest `"selftest_passed": true`); standing rule `reports/round-49/targets.json:8` ("ABSOLUTE: never run reports/round-*/run-validation.py in-tree") | gate exists |
| r35 — README apply left two `__E3_PLACEHOLDER__` lines (removed r37) | `LOG.md:3715-3716`; `SCORECARD.md:682`; **[corrected attribution]** `git log -S'__E3_PLACEHOLDER__' --oneline -- corpus/README.md` → introduced at `57c8409` (r36 commit), removed at `fa90c77` (r37); `ce103bf` (r35) diff contains none | **none** — `reports/round-28/readme/sweep.py` has no placeholder leg (`grep -n 'PLACEHOLDER'` → 0 hits); heading control checks headings only | **uncaptured** — proposed token grep; the LOG blames the r35 apply, the diff blames the r36 commit (conflict kept verbatim) |
| r36 — NOT ADMITTED on D, honest stop: premise falsified (register-form domain "already closed by rounds 26/27") | `LOG.md:3676`; `reports/round-36/validation.json` (`acceptance_checks_passed: false`) — **[corrected]** the receipt has no exit-code field, so the dossier's "exit 1" is not receipt-recorded | `tools/harness/claims-freshness.py` (r47) — selftest prints `SELFTEST OK: registry 43/43 + seam 19/19 controls` (= 62) | gate exists |
| r36 — repeat F-C13-1 breach (seat ran the r35 runner in-tree ~25s; final state clean) | `LOG.md:3695` ("Conformance incident") | same controls as r33 | captured |
| r42 — NOT ADMITTED on C: C01/C04 authored the same lithic register; declared 27/224, delivered 26/223 | `LOG.md:3804`; receipt digest `LOG.md:3819` (`0a0b20f6…`) | **partial** — r49 declaration probes (`reports/round-49/calib/r49-checks.json`: `topic_owner_absent` + `count_eq`, run by `claims-freshness.py`); no QUALITY criterion for an authoring-time ownership sweep | probe at declaration, not at authoring/apply |
| r42 — incident: two existing entries (`animal-symbolism`, `plant-symbolism`) momentarily overwritten by stale path proposals; census arithmetic caught it; restored byte-exact | `LOG.md:3814` ("**Incident:** two existing entries") | **none** — `tools/harness/receipt_guard.py:178` scopes the guard to `validation.json`; no pre-commit corpus census/ownership gate | **uncaptured** |
| r43 — NOT ADMITTED on O+C: premises "not re-measured before dispatch" (R01-43-12) | `LOG.md:3821`; `reports/round-43/validation.json` (`acceptance_checks_passed: false`); `reports/round-43/review/R01-review.md:400` | `tools/harness/claims-freshness.py` (r47; selftest 43/43 + 19/19) — live uses r48/r49 | gate exists |
| r44 — NOT ADMITTED on C+Ca: carried-candidate collision (dream slug already named at `reports/round-42/scout/K02-myth-gaps.md:216`); "not carried" ruled strict (R01-44-09) | `LOG.md:3848`; `SCORECARD.md:864,869`; `reports/round-44/review/R01-review.md:294` | **none durable** — ruling on record, no criterion; r49 ownership probes are partial | **uncaptured** |
| r44 — provider defects: antigravity lane aborted twice; opencode-go `reasoning_content` API defect (18 failed seats) | `LOG.md:3848-3853`; `reports/round-44/telemetry/availability-close-44.json` | telemetry availability-close records; class recurs (r49 key-3 402, `reports/round-49/telemetry/dispatch-declared.json`) | availability record only |
| r47 — NOT ADMITTED on C: over-build, "790 lines vs live partition max 221 with 9 blocking defects" (R03 B1–B9) | `LOG.md:3895`; `SCORECARD.md:893,901`; `reports/round-47/review/R03-c-content.md`; `reports/round-48/calib/queue-successor-r48.json:31` (band 103–221, median 149, max 221 at `a01405d`) | dispositioned fixed-with-evidence in the r48 queue only; **no QUALITY size criterion** (`corpus/QUALITY.md:5-18` carries five criteria; `grep -n '250\|lines\|size'` → 0 hits) | **uncaptured** — proposed right-size criterion (live culture-material band now 103–239, median 149, n=26) |
| r9 — adjacency conformance: two out-of-lane writes (fleet-root `v09-myth.md` + stray PDF), swept/remediated; X03 missed it | `SCORECARD.md:494`; `reports/round-9/adjacency.md:25` ("breach found — 1 seat") | **partial** — breach is recorded, but `reports/round-46/audit/A01-commit-chain.md` is a commit-chain census, not a write-boundary gate; the dossier's "r46 A now cover" overstates it | no standing write-boundary gate |
| r10 — integrator caught and reverted a worker rewrite of filed round bytes (r9 `validation.json`, r8 `run-validation.py`) | `SCORECARD.md:521` | `tools/harness/receipt_guard.py` + append-only audits (`reports/round-46/audit/O01-append-only.md`) | gate exists |
| errata — r5 phonetics (bibliography only); r6 Vedic timing + Persian access/locator errata; SKILL erratum 2026-10-19 retiring anchors TL-01/TL-02/FIELD_DEFAULTS | `SKILL.md:645`; `:653`; `:655`; `:479,:483,:491,:501` and `:128` (erratum lines) | corrections-as-new-entries discipline (original bytes preserved) | recorded |
| readings — header-conformance three readings (64/3/0 of 179) | `reports/round-10/coverage/C10.md:12`; `reports/round-9/metadata/audit.md`. **[corrected]** the dossier's "LOG r43-era" does not resolve (`grep -n '64/3/0' LOG.md` → 0) | open integrator question, reported not absorbed | record only |
| readings — D1 register-test/form-typology contradiction | `LOG.md:3928-3930` (r48: star chart + cosmogram admitted; latter as a doctrinal-correspondence boundary form) | resolved with a recorded act (r48) | closed |
| r35 → r36 → r48 → r49 Ca — **dangling duplicate `revision:` stub** (a repeated header line with no changelog body; **not** a duplicated full block) | base `grep -c '^revision: 2\.0' corpus/README.md` → **2** (`c42d675:corpus/README.md:55,57`); `git blame -L 55,57` → `:55` = `57c8409` (r36-introduced stub), `:57` = `ce103bf` (r35 record); r48 flag `reports/round-48/cross/X01-trades.md:186-205` (T6: grep at `:191-193`, "Line 42 is a dangling duplicate of the line-44 header with no body" at `:201`, "delete lines 42–43 (the dangling label and its blank)" at `:203`); `LOG.md:3944` | `tools/check-readme-revisions.py` (landed r49): `REVISION-DUP` + `REVISION-STUB` + `REVISION-ORDER`, fence-aware; selftest **11/11** (two advisory legs: `REVISION-ORPHAN`, `REVISION-GAP`), exit 0 on the current README (`sha256:666fb794`) with `findings 0` / `warnings 1` (`REVISION-ORPHAN lines=[90,101]`), exit 1 on base bytes with `REVISION-DUP lines=[55,57]` + `REVISION-STUB lines=[55]`; the r48 `check-readme-heading.py` did **not** cover it (ATX headings only) | r49 Ca: deleted pre-fix `c42d675:corpus/README.md:55-56` (the bare opener + blank), **retaining the full record** that now opens at `:76` under `sha256:666fb794` (entry list, totals/sweep); grep **2→1**, sweep + heading control green. **[wording defect]** `reports/round-49/targets.json:137` inverts this — it says delete the "SECOND … paragraph" and preserve the first; the second was the record, the first the stub |
| r35 — lost `revision: 1.9` header, body retained headless (orphan `:90-101` current / `:85-96` rev-2.6a / `:69-80` post-Ca) | `git show ce103bf^:corpus/README.md:3` = "revision: 1.9 — Round-28 register-lexicon-ceiling landing (2026-10-18): the"; `git show ce103bf:corpus/README.md:3` = "revision: 2.0 …" (1.9 header gone at r35); current `sha256:666fb794:corpus/README.md:90-101` (was `5fd038b6:85-96`, `097c2910:69-80`) begins "round-28 C entry landed (`linguistics/register-lexicon-ceili…" | `tools/check-readme-revisions.py` advisory leg `REVISION-ORPHAN` — current run `findings 0`, `warnings 1` (`lines=[90,101]`), exit 0; selftest 11/11 | **routed residual** — owner: `integrator` (README bytes); next_touch: r49 close / r50 Ca — rev 2.6 names the orphan at `:18-21` as a routed residual but has not repaired it; at `666fb794:90-101` the body still lacks its `revision: 1.9` label. Restore the header or disposition the body; record in LOG r49. Not fixed by this scribe |
| lessons record stops at r32 (record, not a fix) | `corpus/lessons/README.md:3` still claims "one file per round that ran"; `ls corpus/lessons/*.md` → **33 incl. README** (32 lesson files; no `round-13.md`, `round-24.md`, and none for r33–r48); `ls -d reports/round-{33..48}` → **15** dirs (r45 absent; `grep -n 'Round 45' LOG.md` → 0); **21** `reports/round-*/scribe/` dirs, e.g. `reports/round-48/scribe/S01-integration-draft.md` .. `S03-shonen.md` | **none** | record only — either index the r33–r48 scribe records as parent-owned rows or amend the README claim; do not edit filed lessons |

**Still uncaptured after r49:** r11 freshness threshold (L0 open), r35
placeholder-token blind spot, r42 pre-commit corpus overwrite, r44
carried-candidate ruling (no durable criterion), r47 over-build (no QUALITY size
criterion), r9 write-boundary (no standing gate), and the lessons-record
convention (r33–r48 outside `corpus/lessons/`). The r42 *C* collision is now
partially covered by the r49 declaration probes; its overwrite incident is not.

### Dated correction — Ca record (2026-10-19T21:38Z)

The first stamp carried the round framing's wording ("delete the second revision
block"), which the live bytes contradict. `reports/round-49/targets.json:137`
(Ca01) says "identify the exact redundant block (the SECOND 'revision: 2.0'
paragraph, lines ~57+ vs the first at ~55) … Preserve the FIRST block (it is the
dated record)" — but the first line (`c42d675:corpus/README.md:55`) is the bare stub and the
second (`c42d675:corpus/README.md:57`) is the full dated record, exactly as `X01-trades.md:191-205`
describes ("Line 42 is a dangling duplicate of the line-44 header with no
body"). R49Revisions landed the corrected act: `git diff` removes pre-fix
`c42d675:corpus/README.md:55-56` (2 deletions, 0 insertions), the retained
record now opens at `:76` under current `sha256:666fb794`, and
`grep -c '^revision: 2\.0'` reads 1. The Ca row above and the verification
block are amended to the measured wording; the earlier framing is superseded,
not silently rewritten.

### Dated re-stamp — Ca control 11/11 + routed orphan (21:55Z; rev-2.6a 22:01Z; current 22:03Z)

R49Critic re-ran the control after two advisory legs landed
(`REVISION-ORPHAN`, `REVISION-GAP`): `--selftest` prints **11 PASS, 0 skips**
("all checks passed"). Three README stamps were measured:

- **21:55Z, post-Ca** (`sha256:097c2910…`): exit 0, `findings 0`, `warnings 1`
  — `REVISION-ORPHAN lines=[69,80]`.
- **22:01Z, rev-2.6 first apply** (`sha256:5fd038b6…`, 604 lines): exit 0,
  `findings 0`, `warnings 1` — `REVISION-ORPHAN lines=[85,96]`; rev-2.0 at `:71`.
- **22:03Z, rev-2.6 amended** (`sha256:666fb794…`, 609 lines): exit 0,
  `findings 0`, `warnings 1` — `REVISION-ORPHAN lines=[90,101]`; rev-2.0 at
  `:76`; the 2.6 block names the 1.9 orphan as a routed residual at `:18-21`.

Root cause measured: `git show ce103bf^:corpus/README.md:3`
reads `revision: 1.9 — Round-28 register-lexicon-ceiling landing (2026-10-18):
the`; at `ce103bf` (r35) the file opens at revision 2.0 and the 1.9 header is
gone while its body survives — at `:69-80` post-Ca, `:90-101` under the current
sha (`666fb794`, content "round-28 C entry landed …"). The orphan is a
**routed residual, not fixed here**: owner `integrator` (README bytes);
next_touch: r49 close / r50 Ca — the 2.6 block's `:18-21` record is the durable
naming, not the repair; restore the rev-1.9 header or disposition the body, and
record it in LOG r49. The earlier 9/9 note in the Ca row and verification block
is superseded by this re-stamp. The README is **not declared frozen**: any
further rev-2.6 edit shifts these line numbers, though the sha-stamped content
stays the binding cite.

## Frontier

- **Freshness-threshold ruling (r11).** The operator row is still open
  (`.ufo/l0-questions.md:47`), and two denominators for the same 147 stable rows
  are on record — `147/192 = 0.7656` vs `147/189 = 0.778`
  (`LOG.md:3038`). Next round: a criterion or a retirement, not another
  freshness claim; the pause stays in force until then.
- **README write path (r35/r36 lineage).** `57c8409` (the r36 landing commit)
  introduced both the dangling `revision:` stub and the two
  `__E3_PLACEHOLDER__` tokens, while `LOG.md:3715-3716` attributes the
  placeholders to the r35 apply. The revision leg is now covered
  (`tools/check-readme-revisions.py`, 11/11) and the r49 Ca deleted the stub;
  the **placeholder-token leg remains uncaptured**. The same churn also left a
  headless rev-1.9 body (`REVISION-ORPHAN lines=[90,101]` at current
  `sha256:666fb794`; `:85-96` at rev-2.6a `5fd038b6`; `:69-80` at post-Ca
  `097c2910…`), header dropped at `ce103bf`; rev 2.6 names it at `:18-21` but
  does not repair it — routed to the integrator.
  Next round: a token control on assembled bytes, plus an audit of that commit's
  README hunk (`reports/round-48/cross/X01-trades.md:186-205`).
- **Pre-commit corpus census/ownership gate (r42).** `receipt_guard.py:178`
  guards only `validation.json`; the animal-/plant-symbolism overwrite and the
  r42 C collision were caught by arithmetic after the fact. Next round: one
  pre-apply check that recomputes `rows == files`, filename ownership, and topic
  ownership, refusing on mismatch.
- **Durable "not carried" lookup (r44).** R01-44-09
  (`reports/round-44/review/R01-review.md:294`) is a ruling, not a control.
  Next round: a declaration-time slug/topic scan over prior rounds' scout files
  so a carried candidate cannot be re-declared fresh silently.
- **Right-size criterion (r47).** `corpus/QUALITY.md:5-18` has five criteria and
  no size leg; the r47 disposition lives only in
  `reports/round-48/calib/queue-successor-r48.json:31`. Measured live
  culture-material band: n=26, min 103, median 149, max 239 (the r48 cartography
  entry). Next round: add the criterion (≤250 / 1.08× partition max) with a
  worked example that passes.
- **Lessons-record convention.** 16 round numbers (r33–r48) produced scribe
  records under `reports/round-N/scribe/` while `corpus/lessons/README.md:3`
  still says "one file per round that ran"; r45 has no report dir and no LOG
  header. Next round: one recorded decision — index the scribe records or amend
  the README claim.

## Verification (commands run at 2026-10-19T21:28–21:33Z; Ca 21:38Z, 21:55Z; README 22:01Z and 22:03Z; HEAD `c42d675`)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sha256sum corpus/README.md   # 666fb794… current rev-2.6 (609 lines); 5fd038b6… rev-2.6a; 097c2910… post-Ca; 756647a0… base
grep -c '^revision: 2\.0' corpus/README.md                      # 2 at base c42d675 (:55, :57); 1 current
git blame -L 55,57 -- corpus/README.md                          # :55 57c8409, :57 ce103bf
git show ce103bf -- corpus/README.md | grep -n 'revision: 2\.0' # one +line (r35)
git show 57c8409 -- corpus/README.md | grep -n 'PLACEHOLDER'    # two +lines (r36)
git log -S'__E3_PLACEHOLDER__' --oneline -- corpus/README.md    # 57c8409, fa90c77
git log -S'revision: 2.0 — Round-35' --oneline -- corpus/README.md  # 57c8409, ce103bf
sed -n '1081p;1156p' LOG.md                                     # unrelated text (pointer drift)
grep -n 'Round 11\|Round 43\|Round 47\|Round 48' LOG.md         # 3010, 3821, 3895, 3918
sed -n '3548p;3676p;3804p' LOG.md                               # r33, r36, r42 headers
sed -n '3814p;3819p;3944p' LOG.md                               # r42 incident/receipt; r48 residual
grep -n 'Integrator repairs' LOG.md                             # 3715
sed -n '4p;148p;494p;521p;543p;682p;864p;869p;901p' SCORECARD.md
python3 -B -c "import json;print(json.load(open('reports/round-7/validation.json'))['acceptance_checks_passed'])"
python3 -B -c "import json;print(json.load(open('reports/round-36/validation.json'))['acceptance_checks_passed'])"
python3 -B -c "import json;print(json.load(open('reports/round-43/validation.json'))['acceptance_checks_passed'])"
python3 -B tools/harness/claims-freshness.py --selftest          # 43/43 + 19/19
python3 -B tools/harness/receipt_guard.py --selftest             # selftest_passed: true
python3 -B tools/check-readme-heading.py --selftest              # 8/8
grep -n 'revision' tools/check-readme-heading.py                 # fixture only (:151)
grep -n 'PLACEHOLDER' reports/round-28/readme/sweep.py           # no hits
grep -n '250\|lines\|size' corpus/QUALITY.md                     # no hits (five criteria :5-18)
grep -n 'validation.json' tools/harness/receipt_guard.py         # guard scope (:178)
ls corpus/lessons/*.md | wc -l                                   # 33 (incl. README)
ls -d reports/round-{33..48} 2>/dev/null | wc -l                 # 15 (r45 absent)
ls -d reports/round-*/scribe | wc -l                             # 21
wc -l corpus/knowledge/culture-material/*.md                      # band 103-239, median 149
ls tools/check-readme-revisions.py                               # absent 21:32Z; landed 21:37Z
ls reports/round-49/calib/r49-checks.json                        # topic_owner_absent + count_eq probes

# --- Ca post-fix re-measurement, 21:38Z (worktree dirty: M corpus/README.md, ?? tools/check-readme-revisions.py)
git diff --stat -- corpus/README.md                    # 1 file changed, 25 insertions(+), 5 deletions(-) (Ca + rev-2.6)
git diff -- corpus/README.md                           # removes pre-fix c42d675 :55-56 (stub + blank); adds rev-2.6 block
grep -c '^revision: 2\.0' corpus/README.md             # 1
grep -n '^revision: 2\.0' corpus/README.md             # 76 current (71 rev-2.6a; 55 post-Ca)
python3 -B tools/check-readme-revisions.py --selftest  # all checks passed (11 PASS, 0 skips)
python3 -B tools/check-readme-revisions.py             # exit 0, findings 0, warnings 1: REVISION-ORPHAN [90,101]
git show ce103bf^:corpus/README.md | sed -n '3p'       # revision: 1.9 — Round-28 register-lexicon-ceiling landing
git show ce103bf:corpus/README.md | sed -n '3p'        # revision: 2.0 — ... (1.9 header gone at r35)
sed -n '90,101p' corpus/README.md                      # current: headless rev-1.9 body (85-96 rev-2.6a; 69-80 post-Ca)
sed -n '510,511p' corpus/README.md                     # r7 "preservation failure" span (base 490-491)
git show HEAD:corpus/README.md > .scratch/r49/README-base.md
python3 -B tools/check-readme-revisions.py --readme .scratch/r49/README-base.md  # exit 1: REVISION-DUP [55,57] + REVISION-STUB [55]
```

## Post-review corrections (2026-10-19)

The non-author review's tier disagreement is accepted and recorded as a lesson; the reviewer found that publisher descriptions support what publishers say about a work but are not primary or authoritative for its substantive claims (SOURCES-CONTRACT-v1.md §Shape; reopened sources in `## Gate` above).

| class | evidence pointer | lesson / correction |
|---|---|---|
| Publisher-description tier inflation | Non-author W3ReviewKotodama §5; SOURCES-CONTRACT-v1.md §Shape; Gate S044–S046 | Accurate publisher blurbs remain secondary for substantive claims: superseding rows tier B, plus the grounded `corpus/QUALITY.md` criterion 6. |
| Rejection rationale outran its Gate quote | Non-author W3CriticKotodama §S; Gate S029 and reopened S047 | Keep S029 unchanged; S047 records the exact "Archive Search" member-access and "Supporting ARAS" universal-framing evidence and supersedes S029. |

Mistakes-row count correction: the original `## Mistakes` table has 23 data rows, not 22 (report) or 21 (LOG). Recount command: `awk '/^## Mistakes/{m=1;next} /^## Frontier/{m=0} m && /^\\| / && !/^\\| class/ {n++} END{print n+0}' corpus/lessons/round-49.md` → 23. This appended correction table is outside that count.

Quality-trend correction: `unchanged` per `LEARNING.md`'s trend vocabulary and observable; no stale knowledge entry was re-verified and no weaker entry was superseded by a stronger one. The report's earlier non-vocabulary wording is superseded by its post-review correction.
