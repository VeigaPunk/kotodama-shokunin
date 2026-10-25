# RevEntryQuality — round 73 wave 1 — staged conlang-scholarship entries as admission candidates

Reviewed against `corpus/QUALITY.md` (criteria 1–21), `PROVINCE.md`, and the coverage map in
`corpus/README.md`. Objects: the two staged files named in claim C's ENTRIES leg —
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md`
and `conlang-scholarship.amend-2026-10-23.md` — plus their five staged rows
(S881, S882, S892, S893, S901 staged-namespace). Nothing was edited anywhere; reads of the
staged tree and lane repo only, plus fetches to /tmp/RevEntryQuality/.

## Fetch log (QUALITY 21/22 draft hygiene)

All fetches plain `curl`, User-Agent exactly:
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`.
Downloads: `/tmp/RevEntryQuality/s881.html` (30,289 B), `s893.html` (97,656 B),
`s901.pdf` (193,610 B), `s892.pdf` (959,171 B), `s882.pdf` (1,055,723 B) — all HTTP 200.
S894: `https://doi.org/10.1017/cnj.2024.21` → cambridge.org answered **HTTP 429** with the
browser-shaped UA (headers saved, `__cf_bm` challenge cookie). Wall met, **not passed**;
no browser automation, no captcha (QUALITY 10). Abstract record reached by ordinary public
copy instead: Crossref `https://api.crossref.org/works/10.1017/cnj.2024.21` (200);
`api.semanticscholar.org` rate-limited 429 once (transient) and **no verdict rests on that
exhausted attempt**. No tools installed (system curl/pdftotext/python3 only).

## Wayback durability spot-check (QUALITY 18/21; CDX exact, statuscode:200 filter)

| row | live URL | captures |
|---|---|---|
| S881 | ojs.unito.it/index.php/ricognizioni/article/view/7099 | 10, earliest 2023-01-02 (embedded original is the `www.ojs.unito.it` variant — query-aware normalization must be checked when the capture cell is written) |
| S882 | philol.msu.ru/~sidorova/files/conlangs.pdf | 57, earliest 2011-07-16 |
| S892 | journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955 | 1, 2024-04-15 |
| S893 | cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike | **no capture** — see below |
| S901 | sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf | 2, earliest 2024-06-20 |

S893 no-capture ruling, probed URLs filed per criterion 21 (live URL is canonical — re-opened
today with 0 redirects, effective URL identical, 200, quote located):
- no capture under `cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` (exact, no status filter);
- no capture under `cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/` (trailing slash);
- no capture under `www.cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike`;
- prefix probe `cyberleninka.ru/article/n/klassifikatsii*` returns only the **unrelated** article `…/klassifikatsii` (200s 2022-03/2023-03) — a re-opener must not mistake those for ours.

Under QUALITY 18 the S893 row survives on its live leg only (live URL served the quote to this
re-opener today); its row must say so and carry the probes above, not a silent omission.

## Entry 1 — staged `conlang-scholarship.md` (staged S881+S882 → tentative lane S876+S877)

**Verdict: ADMIT-WITH-CUTS.** Payload is real, in-province, and lands on uncovered ground
(see coverage section); it is not landable as staged.

Factual sentences checked against the opened sources — all supported:
- §2 from S881 ✓ — abstract verbatim: construction by students "allows them to better grasp
  the reality of linguistic analysis than does the repetition of exercises based on data from
  natural languages", and "the reasons that lead me to marginalize natural languages from
  teaching are the same ones that lead most linguists to marginalize constructed languages
  from research" (teaching/research asymmetry ✓). Keywords line of the row checks ✓.
- §3 from S882 ✓ — the PDF carries the аннотация ("Чем они отличаются от других видов
  искусственных языков и от естественных языков?") and the chapter-1 heading "Естественные,
  искусственные, вспомогательные, фантастические, вымышленные… и другие" plus "Классификация
  искусственных языков (конлангов)".
- §4 ✓ (verified, though unattributed in the outline) — S882 TOC heading "Языки Толкина,
  клингон и D'ni как конланги, имеющие особый статус" and "Обзор литературы, посвященно[й]…".
- gap-filled claim about the lane's own `linguistics/conlang-methodology.md` ✓ — it really
  cites Rosenfelder, Peterson, Okrent, Higley and WALS/PHOIBLE/APiCS.

Required cuts/fixes (blocks AS-IS):
1. **Campaign-id trap (claims kill_rule).** `gap filled` line: "Round 1 added a conference
   paper (S728)". Lane `SOURCES.md:683` S728 = Frye 2022, *Child-directed Speech in Qaqet* —
   an unrelated document. The S728 token must appear nowhere in the landed entry.
2. **Criterion 15 lint fails as staged**: `check-cited-lines.py` on the staged bytes prints
   `MULTI-ID conlang-scholarship.md:7 S881,S882` (exit 1) — the two `source:` clauses share
   one line. Split to the lane's one `- source:`-per-line shape (round-71 convention,
   `dance-performance-movement-codes.md`). Re-point S881→S876, S882→S877 by document only.
3. **Recheck header is campaign-relative**: "re-run the two row recheck commands in round 2's
   `SOURCES-PROPOSED.md` (S881 -> 2, S882 -> 2)" — no such file exists in the lane; re-normalize
   to the lane rows' re-open commands with a receipt pointer (round-71 shape).
4. **Ground header is campaign-relative**: "round 1's CANNOT-ANSWER §4" — restate lane-legibly
   (the gap-sweep receipt is the lane-legible ground).
5. **Coupling line half-dangling (QUALITY 3)**: `linguistics/phonology-systems.md` and
   `culture-material/worldbuilding-setting-practice.md` do not exist in the lane (the real
   phonology entry is `linguistics/phonetics-phonology.md`; worldbuilding-setting-practice is a
   staged-only family the claims refuse this round). Re-point or cut.
6. **Calibration status not named (QUALITY 2)**: the outline's "Calibration key" says what each
   source *type* can carry but never names the entry's claims' status. Lane entries do carry
   status language (5+ linguistics entries contain "mainstream"). Add it: construction-as-
   pedagogy = one author's peer-reviewed argument (tier B, single article); the taxonomy =
   mainstream interlinguistics terminology.
7. **Usability (QUALITY 4)**: the "Proposed body" is a five-item table of contents, i.e. an
   essay skeleton — the bar is decision/typology tables. §3's classification must land as a
   typology table (kind / definition / examples / worldbuilding use), not prose promises.
8. Wording scope: the declared artefact for S881 is the **abstract**; "produces analysable
   data" (topic line) is stronger than the abstract's "better grasp the reality of linguistic
   analysis" — tighten to abstract scope or open the article's full text and cite that.
   Minor: "both read in the original language" is a process claim no re-opener can check;
   scope or drop it.

## Entry 2 — staged `conlang-scholarship.amend-2026-10-23.md` (staged S901 → tentative lane S880; embedded round-3 passage S892+S893+S894)

**Verdict: ADMIT-WITH-CUTS.** The S901 payload verifies cleanly; the embedded superseded
passage is where the defects concentrate.

Factual sentences checked — supported:
- from S901 ✓: "Sowers-Wills's 'Phonology from the inside out…' examines the use of constructed
  languages as an active learning approach in a project-based phonology course. In the course,
  examples of phonological systems in natural languages and constructed languages were
  presented along with instruction in language universals and typology. One innovation … a
  multi-part, creative project can be part of a course even at the introductory level."
  S901 confirmed as the special issue's opening article surveying Sowers-Wills's paper ✓
  ("companion article's account of a neighbouring study in the same special issue" holds).
- from S892 ✓ — Аннотация on p. 455 (range 455–467 verified): taxonomy of constructed
  languages "на основе их лексических, синтаксических, морфологических и иных особенностей",
  "связь между целями их создания и лингвистическими особенностями", "внимание также уделяется
  проблеме евроцентризма".
- from S893 ✓ — Шувалова/Сидорова classification stated exactly as claimed: "1. Auxlangs …
  2. Вымышленные языки (ВЯ) в широком смысле 2.1 Artlangs … 2.1.1 [вышедшие за пределы] …
  В качестве примера О. Н. Шувалова и М. Ю. Сидорова приводят языки Дж. Р. Р. Толкина,
  клингонский язык … а также язык Э'П из мира компьютерной игры «Myst»; … 2.2 Personal
  languages … проектируемые отдельными энтузиастами лингвоконструирования … «для собственного
  удовольствия» [Шувалова, Сидорова, 2006, с. 11]". Peterson comparison: "Наиболее
  детализированной классификацией … является типология Д. Питерсона" — "finer-grained" ✓.
- from S894 (abstract record, ordinary means) ✓ — "semester-long language construction
  project", project-based curriculum, nine students, special topics course. Publisher wall
  (429) reproduced today; any adopted row must record challenge-met-not-passed.

Required cuts/fixes (blocks AS-IS):
1. **Over-attribution to S901**: "semester-long" appears in the header topic and gap-filled
   lines attributed to S901; S901 does not carry it (case-insensitive grep: 0 hits). The word
   is S894-abstract content. Re-attribute or cut from every S901-sourced line.
2. **Unsourced synonym in §N+1**: "personal or автоконланги" — «автоконланг-» occurs in
   **neither** S893 (0 hits) nor S882 (0 hits); S893's stated alternative is «авторскими
   языками». Replace with the sourced term or cut.
3. **Garbled §N+3**: "the *Journal of Constructed Languages* was not resolved to an openable
   article" — no cited row corresponds (S894 is the *Canadian Journal of Linguistics*), and
   "(see `CANNOT-ANSWER.md`)" points at a campaign file that will not exist in the lane. Cut
   or rewrite lane-legibly.
4. **Embedded-superseded-passage disposition (pick one before freeze)**: (a) trim the folded
   round-3 passage outright (MERGE-REPORT.md explicitly permits it, and round 4's §N/§N+2
   supersede its abstract-level claim) — then S892/S893/S894 land no rows and cuts 2/5 collapse;
   or (b) keep it as the dated record — then re-point S892→S878 and S893→S879 by document, and
   for S894 either cut the §N+2 clause or adopt a lane row for the abstract record only (the
   claims' REJECTS trigger "payload stays unreachable" is **not** met — the abstract record is
   reachable via Crossref — but the row must scope the payload to the abstract and say the
   publisher wall was met and not passed).
5. **Criterion 15 lint fails as staged**: `MULTI-ID conlang-scholarship.amend-2026-10-23.md:34
   S892,S893,S894` (exit 1) — the recheck line names three ids on one line and cites campaign
   `SOURCES-PROPOSED.md`. Re-normalize to per-row recheck commands, one id per line.
6. **Row-anchor defect (S893)**: "§1, the classification passage" mislocates — the article's
   major sections are unnumbered (Происхождение и дефиниции термина → Классификация конлангов →
   Сравнительный анализ классификаций → Заключение); the passage sits in «Классификация
   конлангов», the article's second major section; the 1./2./2.1.x numerals are the
   Шувалова/Сидорова classification's own numbering. Fix the anchor wording when the row is
   re-normalized (criterion 18 shape).
7. **Coupling**: `linguistics/naming-systems.amend-2026-10-23.md` does not exist in the lane
   and its family is refused this round (claims REJECTS leg) — dangling; re-point to
   `linguistics/naming-systems.md` (exists) or cut.
8. Calibration + usability: same two conditions as entry 1 — name the claims' status
   explicitly (§N+2 "What this lets the lane claim" *is* a calibration decision; make it
   criterion-2 language), and land §N as a small design-element table, not essay paragraphs.
   Nuance if kept: S893 also notes Peterson's typology "уступает по уровню систематизации
   материала" — "finer-grained" must not imply more systematic.

## Trap sweep (by-document ids)

- Entry 1: **S728 present** (campaign conference paper) — collides with lane Qaqet row. Must be
  removed (claims REPOINTED/kill_rule already demand this; here is the concrete location:
  `gap filled` line).
- Entry 2: no S728/S769/S806 tokens (grep-verified). Its embedded passage's sibling staged
  files (`…amend-2026-10-23c.md` uses S769 for the Palgrave handbook; `…amend-2026-10-24.md`
  uses S806) confirm the campaign ids are a foreign namespace — lane S769 = Opie *Lore and
  Language of Schoolchildren*, lane S806 = Jaiswal & Williams Ayurveda. Also note staged S867
  (bunka.go.jp) is the *same document* as lane S875 — three namespaces, join by URL only.

## Coverage answer (README map)

**Yes — admission counts as expansion on uncovered ground.** The `corpus/README.md`
linguistics listing has no constructed-language-scholarship row; the only conlang owner is
`conlang-methodology.md` (craft pipeline; its own header says cited counts/typology figures
remain (to-verify), apparatus-audit only). My independent gap check agrees with claim C's
before-state: `grep -c` over all 799 lane rows for `unito.it|philol.msu.ru|journals.rudn.ru|
klassifikatsii-konlangov|sanders.phonologist.org` = **0**. Landing adds 2 files (linguistics
28→30; totals 243→245) and up to 5 rows (S876–S880 under the tentative map; S880 only if entry
2 lands its S901 row; S878/S879 only if the embedded passage is kept rather than trimmed) — the
README revision block, totals line and footer are the integrator's, on the round-71 pattern.

## Province check

Both entries stay in-province: reference method for the linguistics partition (what the
research literature says conlangs are and how taxonomies classify them), explicit "decides no
world's language" scope lines (canon hygiene ✓), no general source-research method content
(no chousa invasion), no canon recording. ✓

## Residual risk and verification gaps

- I linted the staged bytes; the claims' CITEDLINES leg (`0 findings`) must be re-run on the
  re-pointed, line-split bytes at `<lands>` — normalization is where a new MULTI-ID could slip.
- S881's capture cell: embedded original is the `www.` host variant; the wave must run the
  query-aware normalization check (criterion 18) when writing the capture cell.
- S893 row has **no capture** (probes filed above): durability rests entirely on the live page;
  if the live page later walls, the row fails durability with no archived fallback.
- "Round 1 / round 2 / round 3" history statements in the headers are campaign-internal and
  unverifiable from lane bytes; re-normalization (not preservation) is the fix — I did not
  verify the campaign's internal round numbering beyond MERGE-REPORT.md's conflict table.
- The claims ROWS leg says the row set is "fixed at freeze from the wave-1 scout verdicts";
  this report gives the wave a decision it must make explicit: embedded passage trimmed
  (S878/S879/S894-rows never land) vs kept (they do, with S894 scoped to the abstract record).
  Either is consistent with the staged evidence; silence is not.
- I did not open the S881 full text (abstract-scope wording flag stands), and I could not
  re-verify the historical "four attempts across two URL variants" count behind the amend's
  ground (today's 429 reproduces the wall itself).
