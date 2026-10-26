author: hyaku closure (non-author integrator, @m_opus)

# Round 56 — non-author verifier spot-check (kotodama)

Closure session `HyakuCloseKotodama56`, 2026-10-22, dispatched by the hyaku orchestrator, not by the lane. Lane base `0daf89fe240f8628f4613eed8e331a0122a6fad4`; lane tip `6386218a3d00bec2fa6295a40ee8ff07164ccb2b`; report `.ufo/reports/round-56/kotodama.md` at fleet `b37501d1`. Every measurement below ran in throw-away clones under `/tmp/kclose56/` (one per revision), never in the lane. Four read-only reviewer seats re-opened sources: `CloseRowsS371toS373`, `CloseRowsS380toS382`, `CloseRowsS410toS412`, `CloseGateRejects56`. The closure re-opened S411 itself.

Driver digest (copied from `.ufo/watchdog.log`, which is mutable):
- `2026-10-22T17:56:48-03:00 launch kotodama round=56 pgid=4116816 driver=hyaku-inline attempt=1`
- `2026-10-22T19:31:04-03:00 complete kotodama round=56; hyaku-inline attempt=1`

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report landed by the lane | `git log --format='%an %H' -- .ufo/reports/round-56/kotodama.md` | `kotodama-shokunin b37501d13418a2fcfaad85c4fdae2f216cd4fd04` (19:30:08-03), after the lane tip commit (19:29:26-03) | pass |
| `SHONEN` heading, one line per box | report lines 88-93 against `SHONEN.md:5,7,9,11` | 4 lines for 4 boxes, all `[~]` with pointers | pass |
| cited hashes exist and are ancestors of `main` | `git cat-file -t <h>; git merge-base --is-ancestor <h> main` for `0daf89fe 052f145 045f458 b4b7db9 456f5ad 7576fd4 767040e c8af23f 3569d24 6386218a` | 10/10 `commit`, 10/10 ancestors | pass |
| lane pushed, clean | `scripts/hyaku/jj-lane.sh state …` ; `git status --porcelain \| wc -l` ; `git ls-remote origin refs/heads/main` | `ahead=0 behind=0 tracked=0 untracked=0`; `0`; remote `6386218a…` | pass |
| prompt carries the template contract | `diff <(sed -n 1,140p .ufo/prompts/kotodama-round-56.md) templates/round-prompt.md` | only `{{LANE}}`/`{{ROUND}}`/`{{FLEET_ROOT}}`/`{{AXES}}` substitutions; §6 addendum follows; all five child-lane items and the round-level items present; no L2 route map quoted | pass |
| report sections | report headings | Work performed, Landed changes, Before → after, Sources & frontier, Trend verdicts, SHONEN, Stale-lane line, tool installs | pass |

Marker test: real report naming committed work → status `ok`.
Status-neutral defects: the dispatched prompt `.ufo/prompts/kotodama-round-56.md` was committed in the fleet repo under the lane identity (`2075410`, 17:56:46-03), not the integrator's. The fleet root holds an untracked `.ufo/state/kotodama.report-baseline`; it is a driver state file, operator-owned, not lane debt.

## 2. Claims

Owned-axis harm check: `git diff 0daf89fe 6386218a -- SCORECARD.md` adds one capability row, the round-56 axes section and two round-55 correction rows. It changes no earlier score and records no harm. The diff over `SKILL.md` and `PROVINCE.md` is empty.

### Claim C — coverage (re-measured)

Commands, run in a clone at each revision:

- `python3 -B reports/round-56/accept-c.py`
  - at `045f458`: `SET FAIL count=231`, `SWEEP FAIL … rows 231 files 231`, `FLOOR FAIL cited=0`, RANGE, STATUS, USEDBY and ACCESS PASS, exit 1;
  - at `767040e` and at `6386218a`: all seven legs PASS (`count=232 added=['corpus/knowledge/civilizations/kongo-kingdom.md'] removed=[]`, `rows 232 files 232 missing_from_index 0`, `cited=54`, `ACCESS: 2 flagged rows, 0 findings`), exit 0.
- Plain counts:
  - `git ls-tree -r --name-only HEAD corpus/knowledge | wc -l`: 231 at `045f458`, 232 at `6386218a`;
  - `grep -c '^| S[0-9]' corpus/SOURCES.md`: 358 → 412;
  - status column: 313/35/10 → 367/35/10;
  - distinct S-ids in the entry: 54, S359 to S412;
  - rows S413-S418 in SOURCES: 0.

All match the report. Verdict: **verifies as declared.**
- No do-nothing control reaches the target: the base tree exits 1 on SET, SWEEP and FLOOR.
- The content clauses are review-only (sentence support, the topic). §3 samples them: 10 of 10 admits agree.
- `accept-c.py:18` prints a SyntaxWarning. This is cosmetic; the instrument is frozen.

### Claim O — operability (the counter re-run; the landed tool measured by the closure)

Commands:
- `python3 -B reports/round-56/accept-o.py` at `b4b7db9`: ENTITY count 0, EXIT, DECODE and BADUTF8 FAIL, exit 1.
- The same command at `7576fd4` and at `6386218a`: eight legs PASS, `SELFTEST: 38/38`, exit 0.
- The tool's sha256 is `3a13ab9c…` at both revisions, unchanged since landing. The base tool's sha256 is `607acba7…`.
- The counter reproduces the report.

**Shortcut control, re-run by the closure.**
- The control is the build critic's `sidcheat` checker (`/fast/scratch/hyaku/kotodama-r56/CriticClaimO56/variant-tool.py`, sha256 `e3060c1c…`, mode `GQ_MODE=sidcheat`; recorded at `.ufo/waves/round-56/build/CriticClaimO56.md:68`).
- It detects no reference and decodes nothing. It emits the expected findings for 23 hard-coded S-ids and adds the UTF-8 error path.
- It was copied over `tools/check-gate-quotes.py` in a clone at `6386218a`. `GQ_MODE=sidcheat python3 -B reports/round-56/accept-o.py` printed all eight legs PASS (`ENTITY PASS count=16`, `DECODE PASS … moved_exit=1 moved_missing=0`, `SELFTEST PASS 27/27`), exit 0.

**The landed tool measured by the closure.**
- Input: `/tmp/kclose56/gen/lessons/renum.md`, built as follows:
  - the fixture with its ids renumbered (S95x→S99x, S96x→S98x) in the lesson and the registry;
  - four new rows, S701-S704:
    - `&ldquo;…&rdquo;` around a 26-word quote;
    - `Grounds: Kongo&mdash;court cloth.` against a longer `teaches` cell;
    - `&eacute;` inside a quote;
    - an `AT&T;` boundary row.
- The 15 expected findings:
  - S991 html-entity and truncated-grounds;
  - S992, S994, S998 and S999 html-entity;
  - S995 html-entity and words=26;
  - S980 html-entity and words=5;
  - S701 html-entity and words=26;
  - S702 html-entity and truncated-grounds;
  - S703 html-entity;
  - nothing on S704.
- Results:

| checker | findings | exit |
|---|---|---|
| landed tool | 15/15 expected, 0 false | 1 |
| `sidcheat` control | 0 | 0 |
| base tool `b4b7db9` | 0 | 0 |

- Also on the landed tool: `corpus/lessons/round-56.md` gives 0 findings, exit 0, and `--selftest` passes 38/38.

**Ruling: O does not verify as declared.** The target was meant to show decoding. A control that does no detection and no decoding reaches the full declared target, 8/8 legs. Four grounds support the ruling:
- The O statement promises "every Gate row that carries an HTML character reference", but the counter enumerates only 16 round-55 rows and 10 fixture rows. This breaks the dispatched prompt's §6 item 9: no universal clause unless the counting command enumerates the full set.
- The declaration's own review-only item 3 concedes that the moved copy defeats only path- and line-keyed shortcuts. CriticClaimO56 measured the S-id cheat before landing, and the claim was not re-declared (R56-M3).
- The orchestrator reports that the L1 dispatch context carried the same rule: a target must be one a do-nothing control cannot reach. Addendum §9 says so (fleet `dc05427`, 21:55Z). This round's prompt predates that text. The closure did not find the context text in committed lane bytes.
- The closest precedent is kake r34 (`MANIFEST.json` `rounds[485]`): a control met the declared counter, the claim was graded `unprovable-but-better` on the closure's own measurement, and the round was rejected as an honest stop.

On the closure's own measurement the tool is real and generalises: 15/15 against the control's 0/15. The independent falsify probes agree (`CriticClaimOProbes56`, 14/14 carried). Operability is therefore `unprovable-but-better`, not harmed. Known survivors, from the falsify seats:
- double decoding (`MutateDecode`);
- stop-at-first-bad-file (`MutateUtf8`);
- a CLI class-label rename survives `--selftest` but is killed by accept-o (`MutateEntityRule`).

### Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| coverage | improved | C re-measured: 231 → 232 files, 54 mined rows cited, spot-check agrees |
| operability | unprovable-but-better | O's counter is reachable by the S-id shortcut (8/8). The tool is real on the closure's probe (15/15 against 0/15) |
| calibration | unchanged | not claimed; records only (QUALITY c7, SCORECARD correction rows) |
| depth | unchanged | not claimed |
| freshness | unchanged | paused by the open round-11 L0 question |
| adjacency | unchanged | not claimed |

No axis is harmed. Not every claim verifies as declared, so the round is **not admitted** (rejected, honest stop).

## 3. Discernment spot-check

Sample: the rows the five cancelled falsify seats would have reviewed (S371-S373, S380-S382, S410-S412), plus S411 re-opened by the closure, plus all four Gate rejects. Quotes were counted by whitespace split.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S371 | admit | archive.org `historiadocongod00jorduoft` details, djvu.txt (HTTP 200, 1,002,207 B) and page images n13/n182 | agree | Quote verbatim at p. 6, doc. IX (12 words). The p. 175 cites carry the election and baptism names at the stated strength |
| S372 | admit | museu.socgeografialisboa.pt `padrao-de-santo-agostinho` (HTTP 200; one transient 508) | agree | "1482-1483" is the object-data date line (1 word). The 1892 replacement and the transfer to Lisbon are on the page |
| S373 | admit | eve.fcsh.unl.pt `rocks-ielala` (HTTP 200, 21,526 B) | agree | Opening description verbatim (23 words). The second-fleet names are on the page |
| S380 | admit | vincentbarletta.com Kimpa Vita relatione (HTTP 200) | agree | Para. 91 verbatim under the row's numbering (13 words). Entry §8 "born in São Salvador, which was Bethlehem" is carried |
| S381 | admit | periodicos.unifesp.br download 15106 (HTTP 200 after a 502 window; 587,473 B, identical to the row) | agree | p. 209 verbatim (12 words). The p. 210 Mbanza Kongo 1706 execution and the Brazil section are carried |
| S382 | admit | kaowarsom.be Cuvelier 1953 PDF (HTTP 200, 85,932,476 B, identical) | agree | p. 226 (PDF leaf 227) verbatim (20 words). Residual risk: the printed folio is not in the OCR layer, and the offset rests on three content anchors |
| S410 | admit | open.bu.edu bitstream: `/download` now serves a 755 B SPA shell; `/server/api/core/bitstreams/<uuid>/content` serves the PDF (HTTP 200, 487,694 B) | agree | p. 2 verbatim (11 words). The Mpemba conquest reading is carried. The row's access URL is stale (routed defect 4) |
| S411 | admit | whc.unesco.org/en/list/1511/ (HTTP 200, 142,656 B; re-opened by the closure and by the seat) | agree | Brief synthesis sentence 1 verbatim (19 words). Entry line 17 "14th to the 19th century" is carried at the stated strength |
| S412 | admit | whc.unesco.org/document/159705 (HTTP 200, 3,492,278 B) | agree | p. 34 verbatim (11 words). The p. 35/36 royal-enclosure and Mbazi sentences are carried |
| Thornton 1991 (stono.pdf) | reject | wpmucdn JMU host PDF (HTTP 200, 1,924,409 B) | agree | JSTOR cover with personal-use terms; no permission stated by the host |
| Thornton 2001 (africankingdoms.co.uk) | reject | PDF (HTTP 200, 3,028,947 B) | agree | JSTOR cover "downloaded … 11 Apr 2020". The site licenses only its images (CC BY 4.0) |
| Glottolog koon1244 | not registered | `.n3` (HTTP 200) and `.json` (HTTP 200) | agree on the outcome, disagree on the reason | The files carry quotable fields (`"level": "language"`, `rdfs:label "South-Central Koongo"`). "Only RDF triples with no quotable passage" is false, as S379 itself quotes a JSON field. The honest reason is redundancy: kiko1235 already carries the classification (routed defect 3) |
| Persée aflin 2015 | not used | persee.fr record (HTTP 403 to default and browser user agents) | agree | The page states "interdiction de diffusion"; the same article was read from Ghent (S378) |

New SOURCES row quote check: S411's `anchor` and Gate quote "one of the largest constituted states of Southern Africa, which was active from the 14th to the 19th century" has 19 words (≤25) and is located at Brief synthesis sentence 1. All nine sampled Gate quotes have ≤25 words and no character reference.

Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok …/corpus/SOURCES.md`, exit 0. It also prints ten W04 cross-scope duplicate-URL warnings on older rows (S127-S133, S185, S186, S358), none in S359-S412.

Admits agree 10/10 (9 rows, S411 re-opened twice). Rejects agree 4/4 in outcome, 3/4 in reason.

## 4. Trend verdicts

- **expansion: improved.**
  - New ground: `civilizations/kongo-kingdom.md`. The base tree had 0 filename owners (`git ls-tree … | grep -ci kongo` → 0, per the claims file; the count rose 231 → 232, re-measured).
  - 54 new `mined` rows.
  - One real new checker, even though its claim does not verify as declared.
- **quality: unprovable-but-better.**
  - The entry's sampled sentences hold (10/10), and the falsify fixes from six critics landed in `c8af23f`.
  - But the round's quality instrument, the O checker, is unproven as declared.
  - Row findings were carried, not applied: S359, S360, S383-S385, S392, S395-S397, S399, S407, the S379 tier and S367.
  - Two mutation survivors remain.
- **discernment: improved.**
  - Licence-uncertain journal scans were rejected before landing (R56-M4); the outside re-open agrees.
  - The round-55 entity defect was traced to its integrator (R56-M1).
  - 10/10 sampled admits agree. One reject reason is wrong (koon1244).

## 5. Routed defects (owing lane: kotodama, next round)

1. **O acceptance blind to identity shortcuts (R56-M3, reproduced by the closure).** The next checker claim must rewrite fixture and registry ids at run time in its moved copy, and must include a named reference outside any short list (`&ldquo;`, `&mdash;`, `&nbsp;`). Before freezing, it must score the cheapest skip-the-work control with the frozen counter and commit that receipt (addendum §9).
2. **O survivors and policy gaps:**
   - kill double decoding with a fixture row such as `"one &amp;hellip; two"`;
   - kill stop-at-first-bad-file with an invalid-then-valid two-file run;
   - add a CLI-label assertion to `--selftest`;
   - state whether `;` binds numeric references (`&#8220w…` passes today);
   - document the U+FFFD handling of invalid code points.
3. **`corpus/lessons/round-56.md:83` koon1244 reason is false.** Append an erratum (never rewrite the filed bytes): the source was opened and is quotable; it was not registered as redundant with kiko1235.
4. **S410 access URL is stale.** The `/download` URL now serves an HTML shell. Record the effective `/server/api/core/bitstreams/ad5455af-…/content` form, as S388 and S390 do.
5. **Carried row findings still open:** S359 pp. 469/470, S360, S383-S385, S392 (two over-reads), S395-S397, S399, S407 (column locator), S367 (Grounds hedge); the S379 tier B → A needs a superseding row.
6. **QUALITY criterion 10 amendment owed:** third-party scans with no stated permission (R56-M4).
7. **`reports/round-56/accept-c.py:18`** SyntaxWarning: use raw strings in the next round's instruments.

## 6. SHONEN note for the operator

All four boxes are `[~]` (author-asserted). Box 3, "Instructions executable by an agent without oral context", now has non-author evidence: this closure re-ran `accept-c.py`, `accept-o.py`, the census and the plain counts from committed paths in fresh clones, and every value matched. Boxes 1, 2 and 4 still need a non-author promotion review. Promotion is operator-owned; this file writes no `[x]`.
