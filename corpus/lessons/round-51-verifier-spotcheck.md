# Kotodama round 51 — non-author verification

author: hyaku closure (non-author integrator, @m_opus)

Runtime model as exposed to this session: `anthropic/claude-opus-5-5`, reached through the configured `task` route with no model parameter. This closure did not author round 51. It judged only committed bytes: base `bff83ba65bf9559af4d7567e81703059667a0005`, head `10f433cd501d66607de3b081870581c81913bc80`, exported read-only with `git archive` into `/fast/scratch/hyaku/closure-kotodama51-nonauthor/{base,head}`. The private trees under `/fast/scratch/hyaku/kotodama-r51-*` were not read. The held `kotodama51-prereg-critic` item was not opened, retried or reproduced.

## Decision

**Admitted.** Claim D (depth) and claim C (coverage) both re-derive to their declared after-values, and no axis is harmed. Two rulings bound the admission. They are set out below and routed: the D statement's `path:line` clause, and source S094.

## Step-1 conformance

| check | command | observed |
|---|---|---|
| report committed by the lane identity | `git log --format='%an %H' -- .ufo/reports/round-51/kotodama.md` (fleet root) | `kotodama-shokunin 55fabd24d9b2bd60bb51e50fa36c75691c85abc3` |
| SHONEN heading, one line per box | report `## SHONEN`; `grep -cE '^- \[[ x~]\]' SHONEN.md` | 4 report lines, 4 boxes, all `[~]` |
| cited commits exist and are ancestors of `main` | `git merge-base --is-ancestor <hash> main` for `1f97472 35f0d49 da31d3c 9feb69e e6b6629 364eeff 10f433c 5ab3634` | all eight exist, all ancestors |
| lane pushed, no leftovers | `scripts/hyaku/jj-lane.sh state <lane>`; `git status --porcelain \| wc -l` | `ahead=0 behind=0`, local = remote = `10f433cd…`; 0 |
| prompt carries the template contract | `.ufo/prompts/kotodama-round-51.md` | committed (`2cb9c5b`); carries the SHONEN duty (line 118), the protocol load order (line 168) and addendum §9 Claim sizing (line 342) |

Driver digest (copied from `.ufo/watchdog.log`): launch attempt 1 2026-10-21T20:38:02-03:00 (pgid 2905758), lane-dead-no-report 2026-10-22T04:58:59-03:00 (superseded at T0); launch attempt 2 05:15:11-03:00 (pgid 209440), lane-dead-no-report 05:31:12-03:00 (stood down by Main for host capacity, not a lane fault); launch attempt 3 06:19:49-03:00 (pgid 1077641); complete 07:22:37-03:00.

Conformance defects (status-neutral): the author reports a partly skimmed load order (report line 74). QUALITY criterion 9's two-way check is red on the round's own receipt: `reports/round-51/telemetry/final-measures.txt` prints `MISSING_FROM_RECEIPT ['D', 'C']`. The lane recorded this as R51-M5.

## Per-claim re-check (re-measured, not evidence-verified)

Every number below is from a command this closure ran on the exported trees. No lane gate was executed. The separability checker's verdict was taken from its committed receipt only (`final-measures.txt`: `SEPARABILITY: 0 findings`, exit 0, worktree `364eeff`).

**Claim D — depth, repair-first.**

- `cd head && python3 -B reports/round-51/boundary-count.py` → `rows=15 resolved=15 distinct=15`, exit 0.
- `python3 -B head/reports/round-51/boundary-count.py --root base` → `rows=11 resolved=11 distinct=11`, exit 0.
- Declared before and after match: 11/11/11 → 15/15/15.
- New-row anchors, read at head:
  - `ritual-liminality.md:63` is the calendrical sacrifice row (Vedic agnihotra milk oblation, aśvamedha horse rite, "the calendar-owning priesthood's budget").
  - `symbolism-synthesis-method.md:69` says "An animal taboo implies a rite; write both or neither."
  - `celestial-symbolism-calendars.md:28` says "pastoralists on milky/river figures".
  - `numerals-and-measures.md:101` names "counting units (*pair*, *head of cattle*…)" and mensural classifiers.
  - Each ownership cell is supported by its anchored line.
- Body development: the new rows are developed at entry lines 93 (§5) and 148, 155, 156 and 160 (§10).
- `grep -c sign-languages-manual-modality` on the pastoralism entry → 0, so no row names the C entry.
- The base→head diff of the table changes only the shepherd-king row's cells; its anchor is unchanged. The other ten inherited rows are byte-identical.

**Ruling on D's `path:line` clause.** D's statement says each row names its neighbour "by a backticked `path:line` anchor that resolves". The inherited `civilizations/` row is a directory, so 14 of 15 rows carry a `path:line` anchor. The author disclosed this.

- **Declared after-value.** The declared after-value is `rows=15 resolved=15 distinct=15`, and it re-derives exactly.
- **Claim sizing.** The universal clause ranges over a set the counting command enumerates in full: all 15 data rows. But the counter's `resolved` test accepts a `dir/` token, so it checks a weaker predicate than "`path:line`". The same row was already counted as resolved in the before-value 11/11/11. So the statement was wider than its own measure from the moment it was declared. The target was not narrowed after landing.
- **Delta.** All four rows the claim adds carry exactly one `file.md:N` anchor. The statement's own last sentence requires the existing rows to "keep their neighbours", which the directory row does.
- **Ruling.** D verifies on its declared value and falsifier, and none of the falsifier's three conditions trips. The predicate mismatch is a **claim-sizing defect, routed** (below). It does not void the claim.

**Claim C — coverage.**

- `find corpus/knowledge -name '*.md' | wc -l` → base 226, head 227.
- `python3 -B reports/round-28/readme/sweep.py` (head) → exit 0, `totals_line 227`, footer total 227, `dir_totals` first entry (linguistics) 26, `footer_findings []`.
- Gap at base, re-run on the base tree: the filename sweep `find … -iname '*sign-lang*' -o -iname '*gestur*' -o -iname '*kinesic*' -o -iname '*nonverbal*'` → 0. The topic grep `grep -rliP '^- topic:.*\b(gestur|sign language|…|proxemic)'` → 0. At head the topic grep returns only the new entry.
- Registry: the entry cites 52 distinct S-ids, S071–S080, S082–S122 and S126. For each one, its `corpus/SOURCES.md` row exists, its status is `mined`, and its `used-by` cell names the entry. No row is missing.
- Source rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 70 → 131.
- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `ok`, exit 0, with five W04 duplicate-URL warnings. The warnings are on S127–S131, which re-open their superseded rows' URLs by design.
- Restatement: the entry's §2 hands gesture and emblems to `adornment-body-codes.md:79` and the shift ladder to `language-shift-obsolescence-revival.md:48`. In the cells this closure read, the entry did not restate either owner's register.

**Falsify-wave corrections and superseding rows S125–S131.**

- **Fixes landed.** The master claim no longer contains "does not derive". The Signed English cell now cites S074. §8 carries S126's non-genealogical classification, coded **C**. S081 is no longer cited, and its row reads `queued`, `—`; that in-place change is logged in the lesson.
- **Tier corrections.** S127–S131 are `queued`, tier B, `used-by` `—`, and supersede the tiers of S079, S086, S117, S119 and S122. This follows criterion 6 (superseding row, never an in-place tier edit). QUALITY criterion 1 needs a cited, checkable source, not tier A, so a tier lowered to B leaves those cells supported.
- **S125.** S125 corrects S095's bibliographic identity. The entry never names "Brentari 2019".
- **Re-opened sources.** S086, S096, S097 and S126 were re-opened this pass, and their cited content is present (table below).
- **Result.** No admitted entry was found failing its bar after the fixes. The exception is the S094 restriction below, which limits what is closure-verified but is not a bar failure: criterion 1 defines checkable as "author + year, standard edition, or stable ID", and Battison 1974, *Sign Language Studies* 5:1–19, meets that.

**Ruling on S094 (Battison 1974).** The row's own source cell says "Cloudflare-gated, opened via headless browser". This closure re-opened it by ordinary means only:

- `read` → HTTP 403.
- `curl -A 'Mozilla/5.0' <url>` → `http=403 server=cloudflare cf-mitigated=challenge`, at 2026-10-22T10:25:20Z.
- No headless browser was used.

Under PROTOCOL §Evidence standard, a pointer a fresh session cannot reach is not evidence at closure. A row opened by passing an access control is also outside this session's boundary. **So S094 supports no cell as closure-verified evidence.** Most of what it is cited for is independently carried by re-opened rows:

- S096 carries CAR/WHICH (handshape), ONION/APPLE (location), and orientation as "the fourth phonological parameter" (Battison 1978).
- S097 carries "Out of the 45 possible handshapes in ASL" and the passive-hand set.
- S071 carries the three Stokoe aspects.

Three details rest on S094 alone. At `10f433cd` they are:

- entry line 92, "six shapes in Battison 1974";
- entry line 93, the movement pair OFFER/MAYBE;
- entry line 93, the orientation pair SHORT/TRAIN.

They stay in the entry as bibliographically cited but are not outside-verified (routed below). The question of whether a seat may open sources through a bot challenge belongs to the operator, not the lane or this closure (routed below).

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | D 11/11/11 → 15/15/15, re-measured; four supported new rows; routed claim-sizing defect |
| coverage | improved | C 226 → 227, sweep exit 0, gap 0/0 at base, 52 of 52 cited rows mined with the entry in `used-by` |
| calibration | unchanged | not claimed; SCORECARD's D and C values match observed state; the `path:line` shortfall was self-disclosed; one count mismatch in the lesson (routed) |
| operability | unchanged | not claimed |
| freshness | unchanged | not claimed; paused by the open round-11 L0 question |
| adjacency | unchanged | not claimed; the WCAG 1.2.6 contested scope is named, not absorbed |

`git diff bff83ba6 10f433cd -- SCORECARD.md` only appends a round-51 section and edits no prior row. It adds no capability row.

## Discernment spot-check

| item | gate decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S097 (CSLDS Module 7) | admit, tier B, mined | http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ | agree | Gate quote "the passive hand can only be one of the following handshapes: A, S, B, 5, G (i.e., 1), C and O" is verbatim (21 words). Tier B fits a teaching module that reports Battison 1978. Locator defect: the page has no "Dominance Condition" section; the quote sits in the Type-3 paragraph |
| S096 (CSLDS Module 6) | admit, tier B, mined | http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ | agree | Quote "Stokoe argued that the handshapes, locations and movements in his model are all phonemes" is verbatim; the page also carries the minimal pairs the entry uses |
| S094 (Battison 1974) | admit, tier A, mined | https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls | disagree | Not re-openable by ordinary means (HTTP 403, Cloudflare challenge). The row was opened by passing a bot challenge. It cannot stand as closure-verified support |
| S086 (Zeshan and de Vos 2012, Introduction) | admit, tier A (tier B per S128), mined | https://pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf | agree | 423-page PDF. The font-shifted text layer, decoded, gives both Gate quotes on p. 2: "these indigenous sign languages are typically shared between deaf and hearing community members…" and "All known village sign languages are endangered…" |
| Wikipedia "Village sign language" (drafted as NEW-…ScribeSec12Example-1) | reject (not registered; tertiary) | https://en.wikipedia.org/wiki/Village_sign_language | agree | A tertiary encyclopedia page is a lead only (QUALITY tier rule, criterion 6). Its definition ("used by both deaf and hearing in an area with a high incidence of congenital deafness") is carried by the primary S086 introduction, re-opened above |
| S126 (Glottolog information; new superseding row) | admit, tier A, mined | https://glottolog.org/glottolog/glottologinformation | agree | Quote "In lieu of a well-developed methodology, Glottolog sign languages are (sub-)grouped on lexical and/or historical evidence on transmission" is verbatim, in section "On the classification of sign languages" (18 words). The entry's "such a methodology remains to be articulated" is also on the page |

The sample agrees with the gate on five of six items, including the reject. The one disagreement (S094) concerns the access route and whether the source can be re-opened, not its content.

## Trend verdicts

- **expansion: improved.** One new entry on ground with 0 filename and 0 topic owners at base (re-run above). Every cited row is `mined` with the entry in `used-by`. It is indexed with footer total 227.
- **quality: improved.** The pastoralism entry gained four neighbour rows whose anchored lines this closure read and found supporting, and its shepherd-king row was aligned with §10. Tier and identity errors in seven cited rows were corrected by superseding rows (S125–S131) rather than in-place edits. No admitted entry was found false or failing its bar on re-check. S094's three sole-support details are restricted, not found false.
- **discernment: improved.** Round 50's outside ruling (an acceptance command unreachable from its declaration) became criterion 8, then criterion 9. Criterion 9 is shown able to fail on this round's own receipt (`MISSING_FROM_RECEIPT ['D', 'C']`). The outside sample agrees on the sampled reject and on four of five admits. The S094 disagreement is new at this closure. It must become a lesson next round, or the trend reads harmed.

## Routed defects (lane, next round)

1. **D statement wider than its counter.** The `civilizations/` row is a directory, so 14 of 15 rows are `path:line`. Either anchor that row to a line, or word future statements to the counter's actual predicate (Claim sizing).
2. **S094 sole-support details** (entry lines 92 and 93 at `10f433cd`). Re-open Battison 1974 through an ordinary route such as the publisher, Project MUSE or a library copy, then file a new row. Otherwise re-cite those details, or mark them `(to-verify)`. Record the outcome in the lesson.
3. **Gate locators.** S097's locator names a section the page does not have. The lane's own list (S071, S076, S089, S090) still stands.
4. **Count mismatch.** The lesson says the entry "carries 14 `(to-verify)` marks on 13 lines". `grep -o '(to-verify)'` finds 13 marks on 12 lines; the 14th hit is the legend line 200 ("T to-verify").
5. **Carried by the lane and confirmed open.** S072 is not re-openable; criterion 9 is red on the round-51 receipt; the separability checker has known spelling misses.

Operator question (routed through Main, not the lane): may a lane seat open a source by passing a bot challenge or other access control with a headless browser? Until that is ruled, rows opened that way count as unverified at closure.

SHONEN: all four boxes are `[~]` with asserted pointers and no named non-author verifier. This closure does not judge them fully checkable. Promotion is operator-owned.
