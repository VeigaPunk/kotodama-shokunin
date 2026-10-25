# Round 73 (2026-10-25, hyaku run 7, L1 KotodamaR73)

Claims: C (coverage — shokuknow assimilation of the conlang-scholarship theme: two entries,
five new rows S876–S880 re-pointed by document) and Ca (calibration — an eight-pair
self-assessment-vs-repo ledger plus the round-72 routed defects R1–R3). Frozen at
`reports/round-73/claims.json` (freeze commit af65165, wave-1 attacks applied as
`pre_data_corrections`). Round shape: wave 1 = 37 seats (policy v1; see the fleet report).
Assimilation: ONE theme, two entries, five rows; `considerthese/` is absent for this lane.

## Gate

Admitted this round (every row opened by this lane on 2026-10-25 by a plain request with a
recorded browser-shaped UA; the per-row capture file carries the fetch line, bytes, sha256 and
the quote inside its context window; staged ids re-pointed by document, never by arithmetic):

| source | access date | quote (≤25 words) | locator | evidence capture | verdict |
|---|---|---|---|---|---|
| S876 — https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (paper, Enguehard 2022) | 2026-10-25 | "the construction of languages by students allows them to better grasp the reality of linguistic analysis" | Abstract paragraph under the Abstract heading (page-source line 267) | reports/round-73/evidence/S876.txt (HTTP 200, 30289 B, sha256 e7260b49370e9a1e…, UA Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36) | admitted |
| S877 — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf (book, Sidorova & Shuvalova 2006 (full 184-page text)) | 2026-10-25 | «Языки, используемые в художественных произведениях, называют вымышленными или фикциональными.» | printed p. 10, Глава 1 «Классификация искусственных языков (конлангов)» | reports/round-73/evidence/S877.txt (HTTP 200, 1055723 B, sha256 e512a20dd3eef97e…, UA Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36) | admitted |
| S878 — https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955 (paper, Novikov 2022) | 2026-10-25 | "the author examines the existing classifications of constructed languages and attempts to establish a connection between purposes of their creation and their linguistic features" | Abstract, p. 455 | reports/round-73/evidence/S878.txt (HTTP 200, 959171 B, sha256 9f745ddaccdbccbf…, UA Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36) | admitted |
| S879 — https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike (paper, Kostyukhin 2023; live leg only) | 2026-10-25 | "2.2. Personal languages Это личные, или персональные, языки, т. е. вымышленные языки, проектируемые отдельными энтузиастами лингвоконструирования" | comparison section, item 2.2 (PDF p. 5 = printed p. 32) | reports/round-73/evidence/S879.txt (HTTP 200, 97622 B, sha256 709e186b934c9ccb…, UA Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36) | admitted |
| S880 — https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf (paper, Anderson/Grant/Sanders (companion to Sowers-Wills)) | 2026-10-25 | "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level." | §3 These papers, p. 5 | reports/round-73/evidence/S880.txt (HTTP 200, 193610 B, sha256 26dbcf2c0fab6d75…, UA Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36) | admitted |

Adoption old→new (by document; three namespaces — staged S859..S990, register S776..S835, lane
S001..S875 — are joined by URL only): staged S881 → S876 (ojs.unito.it article 7099); staged
S882 → S877 (philol.msu.ru conlangs.pdf); staged S892 → S878 (journals.rudn.ru 31528); staged
S893 → S879 (cyberleninka klassifikatsii-konlangov); staged S901 → S880
(sanders.phonologist.org anderson-etal-cjl-sotl.pdf). The round-71 map
`.ufo/waves/round-71/assimilation/id-renumber-map.json` (S859→S874, S860→S875, …) is STALE and
byte-identical (superseded, not edited): its S874/S875 targets are the two round-72 rows; the
regenerated map is `.ufo/waves/round-73/assimilation/id-renumber-map.json`.

Tier reasons recorded: S877 is B, not the A the scout proposed — a monograph (not peer-reviewed)
whose taxonomy is one classification among several it surveys; the staged row's "announcement
booklet" wording is NOT carried because the full 184-page text was opened (ScoutS882). S879 lives
on its live leg only: the canonical slug has no Wayback capture in the CDX
(`cdx?url=cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` → none
before this round); the one Save-Page-Now capture made this round (20261025222414, 23443 B) is a
shell that does not carry the span and is deliberately not named in the row (QUALITY 18: a
capture whose body lacks the quote is not an anchor).

Refused or not adopted from the assimilation set (reason + flip; every row names the probed URL;
ids are in the STAGED namespace unless marked):

| staged entry | staged rows | reason | flip | probed URLs | verdict |
|---|---|---|---|---|---|
| conlang-scholarship.amend-2026-10-23.md (embedded Sowers-Wills clause, cut from the admitted amendment) | S894 | status: UA "curl/8.7.1" -> HTTP 429, 1302 B, wall present ("Too many automated requests"); retry UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 429, 1302 B, wall present ("Too many automated requests"); automation: none; the 429 is a rate limit read per QUALITY 16, not UA-gating; no Wayback capture of the same page (CDX 0 for the DOI, the cambridge identifier URL and the slug prefix); the Crossref abstract record is reachable but is a different page than the DOI the row would name (QUALITY 18) and no admitted entry may cite a row it cannot anchor | a same-page capture, or the publisher page serving, or a row that names the Crossref record as its own page with its own capture | https://doi.org/10.1017/cnj.2024.21 ; https://api.crossref.org/works/10.1017/cnj.2024.21 ; https://web.archive.org/cdx/search/cdx?url=doi.org/10.1017/cnj.2024.21&filter=statuscode:200 | refused |
| conlang-scholarship.amend-2026-10-23b.md | S909, S910 | status: UA "curl/8.7.1" -> HTTP 200, 325225 B, wall absent; retry UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 3038 B, wall present ("Client Challenge"); automation: none; the Springer chapter page serves in full under the plain UA and is walled under the browser UA, so an unreachability ground would be VOID (QUALITY 22); S909 (MGIMO PDF) is reachable HTTP 200, 5824942 B with its nine-field abstract span present; neither row is cited by an admitted entry — adoption stays at the five declared rows (CORPUS rule 4) | a later round that takes the amendment as its theme and re-opens S909/S910 by ordinary means | https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15 ; https://philnauki.mgimo.ru/jour/article/viewFile/520/524 | not adopted |
| conlang-scholarship.md clause 'a conference paper (S728)' | S869 | the clause cites campaign id S728, which in the LANE registry names Frye 2022 on Qaqet child-directed speech — an unrelated document (ScoutMapIds §1b); the intended document is staged S869 (register S786, conlang.org/26c3.pdf): hand-checked PRESENT (title-page epigraph "conlanging (n): the art and craft of making your very own language", live HTTP 200, 753374 B, and capture 20100107110431), so the register's payload-absent class is contradicted for the English quote (the register's Chinese quote is a URL↔quote mispairing); not appended because no admitted entry cites it (CORPUS rule 4) and the clause is cut | an entry that needs the conference paper cites a re-opened S869 row of its own | http://conlang.org/26c3.pdf ; https://web.archive.org/web/20100107110431id_/http://conlang.org/26c3.pdf | refused |
| conlang-scholarship.amend-2026-10-23c.md | S915 (S769 is a campaign id in prose) | the Crossref query row is defective as staged (query token "Languistics" misspelled, `query.container-title` is a relevance search not a filter; the prose id S769 names Opie's schoolchildren book in the lane); not an unreachability ground | restage with the corrected query and the real document cited | https://api.crossref.org/works?query.container-title=The+Palgrave+Handbook+of+Constructed+Languages&rows=40 | not adopted |
| conlang-scholarship.amend-2026-10-24.md | S929, S930 (S806 is a campaign id in prose) | both rows reachable (Luba PDF HTTP 200, 168723 B; Schreyer Crossref record HTTP 200) and span-present, but outside the declared set; S929's second span is on printed p. 390, not p. 387; the prose id S806 names the Ayurveda article in the lane | adopt in a later round with the p. 390 location and the real handbook citation | https://linguistische-treffen.pl/articles/27/24_luba.pdf ; https://api.crossref.org/works/10.1146/annurev-anthro-101819-110152 | not adopted |
| conlang-methodology.amend-2026-10-24.md | S920, S922, S923 (S806 campaign id) | reachable and span-present but outside the declared set; S920's span is §1.3 printed p. 310, not §2.1.2 p. 312 | adopt in a later round with the corrected anchor | https://api.crossref.org/works/10.1146/annurev-linguistics-030421-064707 ; https://api.crossref.org/journals?query=constructed+language&rows=20 | not adopted |

Not adopted this round: the naming-systems, calendar, era and verification staged families
(`naming-systems.amend-*`, `calendar-festival-systems.amend-*`, `era-periodization-models.amend-*`,
`citation-format-and-source-registry.amend-*`, `reopen-gate.amend-*`,
`journal-serial-catalogue-records.amend-*`, `narrative-structure-frameworks*`,
`worldbuilding-setting-practice*`, `heritage-taxonomy-models.amend-*` already adopted) — one theme per
round (item 10); reason and flip: a later round takes one family at a time, re-points every
cited id by document (the by-document check is mandatory: staged citations to S726/S732/S746/S757
name unrelated lane documents) and re-opens each row.

Per-row re-open and capture evidence: `reports/round-73/evidence/S876.txt`..`S880.txt` (committed
before data at the freeze); seat reports `.ufo/waves/round-73/w1/ScoutS881.md`, `ScoutS882.md`,
`ScoutS892.md`, `ScoutS893.md`, `ScoutS901.md`, `ScoutQuarantineConlang.md`,
`ScoutAmendTriage.md`, `RevSowersAccess.md`. Word counts are by direct `wc -w`/token count
(S876 16, S877 9, S878 24, S879 16, S880 25); `tools/check-gate-quotes.py` is not the cap check
(pipe-row blind spot routed in round 72).

Sibling-overlap note: `.ufo/waves/round-73/w1/ScoutGapSweep.md` §[5] swept 20 sibling lanes' knowledge
for the conlang terms and the five URL fragments — 0 files in every lane; the connector seat
ConnectorSiblings returned no report (dead seat, see the fleet report), so the sweep and PROVINCE.md
(lore owns the world bible; the handoff contract
`corpus/knowledge/synthesis/worldbible-integration-contract.md` is cited by both entries) are the
evidence. Handoff obligation: none fires (the rows are used-by lane-internal method entries).

## Collision guard and scratch mirror (item 10)

- Guard (0–3 leading spaces, CORPUS item 10 verbatim): `reg-ids` 799 (S001..S875), `staged-ids` 132
  (S859..S990), `collisions` 17 (S859..S875 — staged-namespace ids coinciding with lane ids);
  the adopted ids S876..S880 are absent from `reg-ids` and from `collisions`.
  Files: `.ufo/waves/round-73/assimilation/{reg-ids,staged-ids,collisions}`.
- Guard proved before use: `.ufo/waves/round-73/assimilation/guard-proof/guard-proof.txt` (planted
  indented row found by the 0–3-space guard, missed by the column-zero control; verdict PASS) and the
  mutation matrix in `.ufo/waves/round-73/w1/MutRegistryCollision.md`.
- Scratch mirror before append: `.ufo/waves/round-73/assimilation/validate-receipt.txt` —
  `sources-census.sh validate --file` exit 0 on the mirror carrying the five normalized rows and the
  two entries; the real registry bytes after append are byte-identical to the mirror
  (sha256 `93d6046444f2170e…018774`). Normalization: recheck cells became `180d`; staged
  `curl … | grep` recheck prose (with a literal pipe) moved out of the row and into the entry
  `recheck:` line; opened `2026-10-25`; used-by exactly the citing entries; status mined.

## Quarantine (register slice, kotodama, hand-checks this round)

The 21-row slice was verdicted in rounds 68–71 and is not re-derived here. Rows touching this theme,
hand-checked 2026-10-25 (`.ufo/waves/round-73/w1/ScoutQuarantineConlang.md`):

| register row (namespace: register) | staged row | verdict | note |
|---|---|---|---|
| S786 conlang.org/26c3.pdf | S869 | PRESENT (title-page epigraph, p. 1) | the register's Chinese quote is a URL↔quote mispairing (it belongs to the chinawriter article, staged S870); not payload loss |
| S812 doi.org/10.1017/cnj.2024.21 | S894 | PRESENT in the Crossref abstract record; publisher page HTTP 429 | unverifiable at the publisher page, not fabrication; the row is not adopted |
| S827 doi.org/10.1007/978-3-032-03277-5_15 | S910 | PRESENT in the Crossref record; publisher page serves in full under a plain UA | the "wall" reading was UA-gated the other way (R73-M3) |

## Mistakes

| class | evidence | captured-by | fix | state |
|---|---|---|---|---|
| R73-M1 landing | `.ufo/waves/round-72/w1/ScoutMergeScan.md` and `ScribeLesson.md` untracked at round-72 close (spot-check R1: `corpus/lessons/round-72-verifier-spotcheck.md:65`); base tree has neither (`git ls-tree -r 8841ad3 --name-only`) | none (PROTOCOL 'landed = committed' names the report and the lane work, no leg lists the wave seat files) | claim Ca TRACKED leg + both files committed in the Ca landing; red-before: `reports/round-73/telemetry/controls-ca.txt` TRACKED FAIL at base, green at the landing | fixed |
| R73-M2 reference-drift | SCORECARD.md:1401 'ACCEPT-CA-72 PASS legs=12/12' vs `reports/round-72/telemetry/measures-ca.txt` reading `ACCEPT-CA-72: FAIL legs=12/12` (spot-check R2, :66); QUALITY 17/19 pin a receipt's stamp but nothing forced the filed verdict to equal the receipt | QUALITY 17/19 (stamp only) — not the verdict text | ledger pair L06 (ANNOTATE row naming FAIL vs PASS) + append-only rerun receipt `reports/round-73/telemetry/measures-ca72-rerun.txt` (PASS 12/12 at 21ad3088 after the fleet report landed — it does not repair the filed row) | fixed (annotated) |
| R73-M3 stale-premise | wave-1 seats and the round-72 Routed-to-73 notes read a Springer/Cambridge "wall" from one UA each; measured here: Springer `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15` answers HTTP 200 / 325225 B to `curl/8.7.1` and HTTP 200 / 3038 B `Client Challenge` to the browser UA; Cambridge answers 429 / 1302 B to both | QUALITY 21 probes the canonical slug, not the UA | QUALITY 22 (UA bound to its response, both directions) with `reports/round-73/telemetry/quality22-controls.txt` filed; the S894/S910 Gate rows are its first applications | fixed |
| R73-M4 survivor | `python3 -B reports/round-72/accept-c.py --selftest` → `SELFTEST: 10/11`, exit 1 (`--- clean fixture: expected PASS 10/10, got exit=1`) at the round-73 base; the round-72 report and SCORECARD cite the counter's mode with no selftest receipt | none (QUALITY 19 requires `--lands`, not a selftest receipt) | QUALITY 23; the round-73 counters commit their selftest receipts (`reports/round-73/telemetry/selftest*.txt`); the round-72 counter is not amended | fixed for round 73; round-72 counter left red, recorded |
| R73-M5 survivor | Ca counter r1 read the ledger from the worktree (`load_ledger` passed a dict to `git -C`; header `source=worktree-uncommitted`), found only when grading the landed data; the r1 selftest could not see it (worktree == commit in the fixture) | the r1 selftest (blind to the class) | counter r2 (bug fix) and r3 (default-path guard + selftest scenario 'worktree-only ledger'); red-before: `reports/round-73/telemetry/red-before-r3.txt` (same selftest with only the guard removed prints `SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'`); `reports/round-73/counter-revisions.md` | fixed |

Sweep for further mistakes in rounds 70–72 lessons: `grep -c '^| .* | none |' corpus/lessons/round-7[012].md` is a
capture-by-none count only; the three routed families (stale id map, staged S934/S936 fabrication-class rows,
S869 re-verification) were handled as follows: the stale map is superseded (regenerated, round-71 bytes
untouched); staged S934/S936 are not adopted (outside the theme; their companions S903/S918 stay
re-verification-flagged for a naming-systems round); S869 (lane, RAD Benesh) is NOT touched — it is the lane's
registry row S869 (dance), a different document from staged S869 (conlang.org); its correction-chain
re-verification stays routed to a dance/performance round.

## Frontier-step

- Registry 799 → 804 rows (S876–S880 opened and mined this round; tier B ×5); census start exit 0
  (`reports/round-73/telemetry/census-start.txt`), end exit 0 (`census-end.txt`).
- Frontier ground entered: constructed-language scholarship as a research literature (English,
  Russian) — before: `find corpus/knowledge -iname '*conlang-scholarship*' | wc -l` = 0.
- QUALITY 22 (UA record) and 23 (selftest receipt, red-before) added with this lesson as ground.
- Assimilation: ADOPTED (one theme, two entries); `considerthese/` absent for this lane.

## Routed to round 74

- Staged families still unadopted (naming-systems ×11 amendments, calendar ×3, era ×2, verification
  ×9, narrative-structure ×5, worldbuilding-setting-practice): take one per round with by-document
  re-pointing; S909/S910/S929/S930/S923 are reachable and span-present (this lane's triage) and can
  seed a conlang-scholarship amendment round.
- `reports/round-72/accept-c.py --selftest` is red at HEAD (R73-M4); decide whether a corrected
  successor counter is warranted or the receipt stays a recorded defect.
- The ConnectorSiblings, ScribeMistakes and ExecScratchMirror seats returned no report (dead);
  their work was done by the L1 (`.ufo/waves/round-73/assimilation/validate-receipt.txt`, this
  lesson, the PROVINCE read).
