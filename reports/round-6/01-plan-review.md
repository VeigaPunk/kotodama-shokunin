# 01 — Plan review: claim-F falsifiability, fixed-question anchoring, schema and preservation bounds

- role: 01 PLANNER + CONNECTOR (author-side planning evidence; **not** an admission decision, no SHONEN, no canon, no rank, no commit, no axis verdicts)
- baseline revision: `030c3928de74ed514853bc1f7490e0f8bb4d451f`; at write time lane `HEAD` **is** that commit ("report: file verified round-5 Flash outcome"), so the baseline is trivially an ancestor of HEAD; nothing has been committed since baseline
- inputs read: lane `AGENTS.md`, `PROVINCE.md`, fleet `AXES.md`, `SCORECARD.md`, `reports/round-6/{claims,targets,baseline,dispatch-plan,prompt-template}`, the round-5 source-reconciliation record set (`corpus/lessons/round-5.md`, `reports/round-5/parent-reconciliation.json`, `reports/round-5/kotodama.md`, LOG round-5 admission entry and round-6 declaration entry), `SKILL.md` "Source-to-system constraints — round 5" table, and the twelve pinned entries (anchor-term spot reads only)
- I redefined no declared target: everything in §5–§6 is an evidence requirement or a check the parent can run **on top of** the single declared claim F.

## 0. Vintage state (measured)

- Working tree: `M LOG.md` (the uncommitted round-6 declaration entry, parent-owned) and untracked `reports/round-6/`. No other dirt.
- `corpus/lessons/round-6-sources/` **does not exist** → claim F's before-side (zero round-6 ledgers) is currently true, not just asserted.
- `reports/round-6/run-validation.py` **does not exist**, yet it is F's only counting command; likewise `parent-source-spotchecks.json`, `parent-reconciliation.json` and `validation.json` are declared evidence files that do not exist yet. This is the same prerequisite shape as round-5's O9: the validator is parent-owned and must be landed, deterministic, and threshold-exact **before** admission measurement. A validator that cannot exist yet cannot measure yet; declaring it is fine, measuring with it is not done.
- Consequence for reviewers 14/15/16: at their dispatch time all twenty-four audits are nonexistent, not merely unreviewed. Their reports must say *unreviewed/nonexistent*, never predict a pass.

## 1. Baseline facts I established (re-executed, not quoted)

| # | Measurement | Observed |
|---|---|---|
| B1 | SHA256 of all twelve `entries_sha256` paths, each compared three ways: recorded hash vs `git show 030c3928:<path>` bytes vs working-tree bytes | **12/12 match all three** — `entry_sha256_before` is real, and the no-harm pin on the twelve entries is mechanically checkable for the whole round |
| B2 | ledger census | `round6_ledger_count: 0` corroborated by B0 absence of `corpus/lessons/round-6-sources/` |
| B3 | question census | 24 questions, **24 unique IDs**, exactly two per assignment, one entry per assignment, all twelve entry paths canonical and existing (B1 required reading them) |
| B4 | git state | HEAD == baseline; only in-flight LOG.md + untracked round-6 dir (§0) |
| B5 | anchor-term presence, each question's distinctive tokens against its entry | 11/12 entries contain their question's anchor terms. Exception: `mesopotamia-sumer-akkad.md` never contains the literal token "kaunakes". The entry does carry real dress-system content the question's *second* disjunct can anchor on: Zawadzki/Quillien priestly-garment rows incl. wool *gammidatu* (lines 22–23), the stage-separately garment-production row (line 69), Gudea "garment surface" (line 113), wool/textile-labor row (line 115). R6-02-B is therefore answerable **only** through its "or tufted/skirt-dress terminology" disjunct, anchored on the entry's actual terms, with *kaunakes* entering as the external scholarly term under test. An `entry_claim` asserting the entry discusses kaunakes would be a manufactured claim — exactly what the schema forbids. Flagged as an evidence requirement; not a target redefinition. |
| B6 | round-5 residual registry intact | `corpus/lessons/round-5-sources/` and the supplemental ledgers present; the 15 unresolved round-5 dispositions in `parent-reconciliation.json` remain the standing worklist, untouched by this round's declaration |

## 2. Claim F — falsifiability decomposition

Declared: exactly 24 named rows across all twelve entries; ≥6 distinct newly retrieved directly relevant non-bibliographic passages across ≥4 entries; ≥3 parent re-fetches; counting via the validator; supported totals do not decide improvement; access failure stays unresolved. The before is verified (B1/B2). The after resolves into independently checkable predicates:

- **P1 exact counts.** "Exactly 24" is strict: 22 or 26 rows fail; each file must carry exactly two audits (schema: `audits` exactly two). Round-5 lesson applied in reverse: there, companion rows merely failed to create *new* questions; here extra rows are a direct violation of the declared after.
- **P2 identity fidelity.** Each row's `id` and `question` must be byte-equal to `targets.json` text (the schema says "exact targets.json text"). Paraphrase drift = invention; the validator can diff these mechanically.
- **P3 entry anchoring.** `entry_locator` must resolve inside the baseline entry bytes (hash-pinned, so a mid-wave entry edit is detectable by re-running B1); `entry_claim` must be an actual bounded assertion locatable at the locator. Parent spot-check a sample against baseline bytes; do not trust locator-shaped strings.
- **P4 distinctness of the ≥6 passages.** Distinct should mean distinct `(source_url, source_locator)` pairs, with near-identical excerpts across rows collapsed to one passage. The two questions of one entry may legitimately converge on one famous source (Linear B textile tablets, the Liber Linteus, the Popol Vuh translation); convergence is legal but contributes **one** passage. Six rows / three distinct passages fails.
- **P5 novelty ("newly retrieved").** Prior art is enumerable: `corpus/lessons/round-5-sources/*.json`, `corpus/lessons/supplement-opencode-1/sources/*.json`, and round-5 `parent-source-spotchecks.json`. A `(url, locator)` pair already retrieved in a prior ledger must not count as newly retrieved; a genuinely new locator in an already-used source does. Cheap mechanical check: grep the prior ledgers for the claimed `source_url`/`source_locator` strings.
- **P6 directly relevant and non-bibliographic.** The excerpt must be substantive content keyed to the question: title/TOC/abstract-venue metadata, catalogue identity fields, accession numbers, page counts and book-jacket copy do not qualify (baseline `limit` and claims `rule` both say so; round-5's S09-08/SOG-29 and PHON-A11 are the precedents). Four parent round-5 checks were non-bibliographic and correctly not counted as prose; the same discipline binds here.
- **P7 spread.** Passages must land in ≥4 distinct entries; six passages on one entry fails.
- **P8 parent re-fetches.** ≥3, of directly relevant non-bibliographic passages, recorded in `parent-source-spotchecks.json` with locator + excerpt. Parent readings remain author-side evidence, not independent promotion verification (`admission_rule`).
- **P9 the counting command.** Must exist, be deterministic (two consecutive runs → identical output), need no network, encode P1–P4/P6–P7 mechanically, and refuse exit 0 when any threshold fails. All-or-nothing is acceptable this round only because there is exactly one claim — there is no second claim to couple through shared bookkeeping (round-5's §2.4 seam does not recur).
- **P10 verdict coherence.** `supported`/`contradicted` ⇒ `retrieved_passage: true` and non-empty `source_excerpt` ≤40 words. A `contradicted` verdict **without retrieved contradicting text** is invalid and must be `unresolved` (a contradiction is a claim about the source, not about an access failure). `support_scope: whole-bounded-claim` requires the passage to cover the entire bounded assertion; `partial` explicitly does not resolve the whole claim (round-5: TIB-A12/A16, meso-15, KIN-A07).
- **P11 anti-fabrication channels.** `retrieval_method` + `accessed_at` populated; `source_kind` honest (a catalogue record of a museum object is `catalogue`, not `museum-object` content); secondary quotation can support only as **mediator-scoped** support with the unread-primary residual named in `limits` — round-5 SR-REG-07 is the accepted shape (Haviland quoting Dixon 1971:437–438, original pages named unread). "Another worker's assertion" is never a source.
- **P12 honesty clause.** F can verify with **zero** `supported` verdicts if six novel passages were genuinely retrieved — freshness is re-verification activity with real evidence, not confirmation totals. Conversely, 24 supported-looking labels do not verify F (round-5: 13 worker `supported` labels → 5 parent-scoped dispositions). Parent reconciliation of worker labels must remain a separate artifact; "supported totals do not decide improvement" is load-bearing, not decoration.

## 3. Fixed questions — falsifiable and in province

Every question has the four-part shape that makes a row mechanically checkable: (a) a pinned existing entry, (b) a named assertion class inside it, (c) an external source class to test against, (d) one or more named confounders to keep separate ("do not make every receipt a spell", "not a universal king-only wearing law", "sound values are not unrestricted translation"). A row missing (b) or (d) fails P2/P3 review; the confounders give reviewers 14/15 and critic 16 concrete things to check rather than vibes.

Province: all twelve entries live in `corpus/knowledge/civilizations/` and all outputs in `corpus/lessons/round-6-sources/` — both owned ("its records … source-check records"). Costume/material questions are in-domain ("costume & material-culture terminology" is declared PROVINCE domain). The chousa boundary is respected **only while** rows stay entry-coupled: `entry_claim` + `coupling_implication` are what keep a row a kotodama source-check record rather than a generic research-method artifact (which would be chousa's). A row that reads as a freestanding retrieval how-to with no entry anchor has crossed that line — adjacent, report, never absorb.

The questions are tests, not truths: `selection_rule` states a question is not a presumption that the entry claim is true. Workers write only `corpus/lessons/round-6-sources/NN.json`; the twelve entries are worker-read-only and B1's hash pin enforces that mechanically. Any warranted correction to an entry is parent-only, appended as errata, never an in-place rewrite.

## 4. Source schema — adequacy and two flagged gaps

The declared schema covers the round-5 failure modes: `entry_claim` (anti-manufacture), `support_scope` (partial-vs-whole), one `source_url` only (corroboration forced into separately labelled optional fields — no shotgun URL lists), `source_excerpt` ≤40 words (bounds quotation and forces relevance), `retrieved_passage`, `accessed_at` + `retrieval_method` (reproducibility), `basis`, `coupling_implication` (the worldbuilding hook — this field is the province anchor), `limits` (residual preservation), and `unavailable` as a source kind so a blocked attempt still produces its row (access failure ≠ confirmation; P1 counts rows, not successes).

Two gaps, neither a target change:

- **G1 — no dedicated edition/translation/mediator field.** The contract requires recording "which language, translation, edition and mediator were actually inspected", but the fixed field list has no home for it; it must live in `retrieval_method`/`basis`/`limits` or labelled optional fields. Reviewers 14/15 should check that translated-source rows record the mediator somewhere, and the parent may have the validator warn when a translated/secondary-source row mentions none of edition/translation/mediator tokens in any field. Round-5's TIB-A12/A16 (earlier thesis vs later book) is the precedent this prevents.
- **G2 — excerpt truncation vs compound claims.** 40 words cannot carry a compound assertion; that is fine because `support_scope` exists, but reviewers should watch for a short excerpt being presented as covering a whole compound claim (P10). A 40-word cap plus `whole-bounded-claim` scope on a multi-conjunct claim is itself a red flag.

## 5. Historical-preservation constraints — checkable register

No-harm is stated as bytes, so it is falsifiable. Ranked checks for the parent:

| # | Preservation claim | Check |
|---|---|---|
| R1 | twelve entries unchanged | re-run the B1 three-way hash comparison at admission; any delta = harm, full stop |
| R2 | historical ledgers untouched | `git diff 030c3928..HEAD --stat -- corpus/lessons/` shows additions **only** under `round-6-sources/`; `corpus/lessons/round-5-sources/`, `supplement-opencode-1/` and all prior lesson files byte-identical |
| R3 | gates/examples/tools untouched | `git diff 030c3928..HEAD -- tools/ examples/` empty |
| R4 | scratch discipline | untracked scratch confined to ignored `/reports/supplement-opencode-1/scratch/round6-*/` (the one ignored subtree `.gitignore` names — `git check-ignore -v` a sample path); no raw downloaded works in any deliverable; scratch is not shipped |
| R5 | previous acceptance preserved | rerun round-5's acceptance in a disposable clean export (`git checkout-index` pattern used last round) without rewriting its historical receipt; expected red stays red (D2 still 20 findings) |
| R6 | marker hygiene | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` stays 592/598 unless the parent appends a warranted erratum — then the delta is reported with the command, never assumed away |
| R7 | append-only LOG | the round-6 declaration entry is currently an uncommitted modification; the diff must be an append, and any correction to this round's text lands as a new appended entry pointing at the superseded text |
| R8 | reports land in order | worker fragments → parent validation/spotchecks/reconciliation → work commit → `kotodama.md` citing that HEAD hash (`git merge-base --is-ancestor` check) → commit + push to the own-lane remote only |

## 6. Concrete admission counterexamples

Each is a scenario that would make F fail or be unjudgeable, with the check that detects it. Admission requires that none obtains.

- **C1 entry shortfall.** 24 rows exist but one entry has its two rows written by extrapolation from sibling entries while its own ledger is missing → P1's "across all twelve" fails; detect by per-entry file census plus B1 hash pin.
- **C2 duplicate-passage inflation.** Six rows quote the same Wikipedia-class tertiary page (or the same URL with cosmetic locator variation) → P4 distinctness fails; detect by `(url, locator)` clustering and excerpt-normalization diff.
- **C3 round-5 recycling.** A "newly retrieved" passage is already in a round-5 or supplemental ledger at the same `(url, locator)` → P5 novelty fails; detect by grepping prior ledgers.
- **C4 metadata-as-content.** A passage is a catalogue record, landing page, TOC, venue string or book-jacket line; or `retrieved_passage: true` on a snippet → P6 fails; detect by excerpt inspection against the non-bibliographic rule (round-5 S09-08/SOG-29 precedents).
- **C5 verdict incoherence.** `contradicted` with `retrieved_passage: false`; `supported` with empty excerpt; `whole-bounded-claim` on a partial passage → P10 fails; fully mechanical.
- **C6 manufactured entry claim.** Especially on R6-02-B (no literal "kaunakes" in the entry, B5): the row's `entry_claim` asserts terminology the entry does not contain → P3 fails; detect by resolving `entry_locator` in baseline bytes.
- **C7 label-count admission.** F declared verified because raw `supported` labels ≥ some number → violates P12 and the claims text outright; the validator and the parent reconciliation must never key admission to verdict labels.
- **C8 bot-wall laundering.** A paywalled snippet or a search-result preview recorded as a retrieved passage → P6/P11 fail; the no-grind rule says failed access stays `unresolved` with `limits` recording the wall.
- **C9 validator timing.** Admission measured before `run-validation.py` exists, or on a non-deterministic/lenient validator → P9 fails; the round-5 O9 prerequisite pattern applies.
- **C10 hash drift.** Any of the twelve entries changes mid-wave (e.g. a worker "helpfully" edits its entry) → R1 fails and the audit's `entry_sha256_before` no longer binds; the wave is harmed, not refreshed.
- **C11 scope creep into method or canon.** Rows drifting into a general retrieval guide (chousa's), or a row proposing a canon/lore disposition, or SKILL.md edited by a worker → province violation; detect by R3 plus row-shape review (every row must carry entry_claim + coupling_implication).
- **C12 coverage inflation in prose.** Report language like "the early-civilization references are now verified" or "all civilizations covered" → false and out of province; this wave addresses the twelve named entries and explicitly not the fifteen round-5 residuals (which stay residual unless separately evidenced) and not the other ~80 civilization entries.

## 7. Source-to-system distinctions (coupling map)

The round-5 `SKILL.md` "Source-to-system constraints — round 5" table (line ~154) established five decision rows. This wave's twenty-four questions exercise the same discipline at earlier reference strata; the recurring distinction classes, with the in-world system each guards:

| Distinction class | Questions | System guarded | Failure if conflated |
|---|---|---|---|
| script vs language affiliation vs sound vs meaning | R6-04-A, R6-10-A, R6-12-A, R6-08-A | naming/language systems; decipherment staging | readable letters or recovered sound values become translation or ethnic identity |
| speech community vs scribal register/genre vs royal ideology | R6-02-A, R6-05-A, R6-06-A, R6-09-A | language-contact and register staging | one archive's genre becomes all speech/belief; monumental trilingualism becomes populace literacy |
| transmitted prescription vs surviving object vs depicted convention | R6-03-B, R6-08-B, R6-13-A, R6-13-B | costume/material reconstruction bounds | a school-specific text rule becomes pan-period practice; a prescription date becomes a practice date |
| account/record class vs worn object | R6-04-B | costume economics | a textile ration tablet becomes a wardrobe description |
| object biography vs depicted form vs semantic attribution | R6-09-B, R6-10-B, R6-11-B, R6-05-B | symbol/icon semantics | reuse events (mummy wrapping) date original use; a modern diagram becomes ancient meaning |
| label provenance: modern/exonym/translated term vs native term vs material construction | R6-02-B, R6-07-A, R6-12-B | naming systems | Greek/English labels become in-world material or theological fact; a title gloss becomes a universal gender system |
| production/display evidence vs institutional rule | R6-07-B | sumptuary system modeling | a dye workshop becomes a king-only wearing law |
| controlled cross-era/cross-culture comparison | R6-06-B, R6-11-A, R6-05-B | era staging of institutions | Zhou prescription or colonial-era Kiche manuscript retrojects onto Shang objects or Classic Maya belief |

Workers must not edit SKILL.md (outside their write scope); whether any of these becomes a new SKILL decision row is the parent's call, on the same terms as round 5: a row exists only where a retrieved passage earned it.

## 8. Limits of this review

- Read-only except this file; no scratch artifacts created (all checks were inline one-shot commands); no provider/config/credential reads; no delegation; no commits.
- I performed **no source retrievals** and no feasibility fetches: the assignment forbids redoing the twelve researchers' work, and unlike round 5 there is no prior-ledger access-limit corpus for these twelve entries to read route classes from. Whether public content is reachable for each question is exactly what the executors will find out; nothing here predicts their outcomes.
- I judged only baseline bytes, file existence/absence, and question-to-entry anchor presence. No round-6 audit row exists yet (§0); every one of the 24 audits is therefore **nonexistent-and-unreviewed** at write time, and no pass/fail of claim F is expressed or implied anywhere above.
- No admission recommendation, no axis verdicts, no SHONEN marks, no target redefinition, no canon or lore disposition.

## 9. Questions left in this fragment for the parent

1. Will round-6 `run-validation.py` enforce *exactly* 24 rows, exactly-two-audits-per-file, and byte-equal id/question text against `targets.json` (P1/P2), and fail closed (P9)?
2. Will the parent spot-check `entry_locator` resolution against baseline entry bytes for at least a sample of rows (P3), with R6-02-B's no-literal-anchor caveat (B5/C6) explicitly in view?
3. Confirm the distinctness/novelty operationalization: `(source_url, source_locator)` pairs, near-identical excerpts collapsed, novelty grepped against round-5 + supplemental ledgers (P4/P5) — or substitute a stricter written definition before measurement.
4. G1: accept that language/edition/mediator recording lives in optional/retrieval-method fields, with reviewers 14/15 checking its presence on translated/secondary-source rows?
5. Admission language guard: confirm the round report will name F's verification in terms of P1–P12 and never as a supported-label count (P12/C7/C12).
