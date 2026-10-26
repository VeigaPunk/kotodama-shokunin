# Round 62 verifier spot-check — hyaku closure (non-author)

author: hyaku closure (non-author integrator, @m_kfc)
date: 2026-10-23
lane base d42ffb890a54c8431fa891380b6c38bb608b8362; tip 972b52d3d9678f6844b062d1e484a4e92f65da47 (records 2ce9d4d1 + safety-hold append 972b52d3, Main directive, appended after filing).
Dispatch digest (.ufo/watchdog.log, copied per assignment):
2026-10-23T07:41:48-03:00 launch kotodama round=62 pgid=453586 driver=hyaku-inline attempt=1
2026-10-23T09:30:19-03:00 complete kotodama round=62; hyaku-inline attempt=1
2026-10-23T15:03:28-03:00 complete kotodama round=62; hyaku-inline attempt=1
Closure seats: 3 read-only reviewers (D evidence, O evidence, prompt/report conformance), 0 dead. No lane gate or selftest executed (PROTOCOL §Gate standard closure consequence); all claim checks are plain measurements over committed bytes plus committed-receipt verification.

## 1. Step-1 conformance

| check | result | evidence |
|---|---|---|
| report committed by lane identity | pass | `git log --format='%an %H' -- .ufo/reports/round-62/kotodama.md` → `kotodama-shokunin 994151331fbd7ee2979b151715638878f51294ee` |
| SHONEN heading, one line per box | pass | `## SHONEN`, 4/4 boxes `[~]`, each with a resolvable pointer and honest "No non-author verifier" |
| cited commits exist + ancestor of branch `main` (HEAD is detached; tested vs `main`, never `@{u}`) | pass | d42ffb89, 972b52d3, f0173481, e6a61e82, 9143fc44, e605603c, a2c5caa5, 25b44b8a, 2ce9d4d1 — all `git cat-file -e` OK and `git merge-base --is-ancestor <h> main` YES (9/9) |
| no uncommitted round work; pushed | pass | `jj-lane.sh state` → branch=main local=remote=972b52d3 ahead=0 behind=0; `git status --porcelain` empty |
| prompt carries template contract | pass | §1–§5 byte-identical to `templates/round-prompt.md` modulo the `<lane-repo>` substitution; §6 hyaku addendum present. Round-level items (a)–(e) and all five child-lane items present (mechanical diff seat). Defect (status-neutral, operator): the prompt embeds phase 3–4 addendum content only; the 2026-10-23 phase-5 directives are absent — temporal (this round self-identifies "hyaku phase 4"), but the driver should regenerate lane prompts from the current `lane-addendum.md` for future rounds |
| marker vs report | real report | work performed + evidence pointers, landed-changes table tied to LOG, Sources & frontier with counting command, trend verdicts, SHONEN — no marker predicate |

## 2. Per-claim re-check

### Claim D — depth (sourced, S693). Verdict: verifies. Re-measured + evidence-verified; gate not executed.

Re-measured (closure, this session):
- `git show 972b52d3:corpus/knowledge/culture-material/footwear-codes-terminology.md | sed -n '63p;74p;75p;93p'` → 63 open list "Netherlands, France, Belgium, etc. (S692)"; 74 "A Bata Shoe Museum image caption says… (S665)"; 75 "According to the BBC article, the earliest evidence we have… (S666)"; 93 "Talaria are the wings or winged sandals… (S693)". Base d42ffb89 same command → closed list, bare heel assertion, "comes from" without hedge, "(S687)". Freeze 9143fc44 four lines byte-identical to base (repairs landed after the freeze, at a2c5caa5) — before/after sequencing confirmed.
- `grep -c '^| S[0-9]' corpus/SOURCES.md` at d42ffb89 = 618; at 972b52d3 = 619 (matches report 618→619).
- S693 row at tip: tier B, docs, mined, opened 2026-10-23, used-by the footwear entry, live URL + 2024-05-29 same-page capture. S687 used-by `corpus/knowledge/culture-material/footwear-codes-terminology.md` → `—`, tier C unchanged (old→new as reported).
- Live re-open by closure: `curl -A Mozilla/5.0…Firefox/131.0 https://www.dictionary.com/browse/talaria` → HTTP 200, "wings or winged sandals" present; Wayback capture `…/20240529024530id_/…` → HTTP 200, same quote present (same page).

Evidence-verified (committed receipts, not executed):
- `reports/round-62/telemetry/final-measures.txt`: ACCEPT-D-62 PASS, 16 legs, `SOLE id=S693 tier=B`, `LOCATE located=1 cited=1 at=2026-10-23T12:05Z`, exit 0, measured revision a2c5caa5; counter sha256 0f601625… matches the freeze record.
- Freeze integrity: `sha256sum` of accept-d.py, accept-o.py, locate-control.py identical at 9143fc44 and a2c5caa5 (also matched to the shas named in the receipt header).
- `declaration-dry-run-rev1.txt`: ACCEPT-D-62 FAIL at the freeze (SET/OPEN/HEDGE/CAPTION/SOLE/ROWS/LOCATE), exit 1. Nuance: run 12:04:37Z against the freeze tree seconds before the freeze commit 12:04:42Z; identity attested by matching sha256s.
- `controls-rescore.txt`: 24 receipts = 21 frozen=FAIL adversarial fixtures + 3 frozen=PASS honest positives exactly as named in its header ("honest positives PASS" wording accurate).
- Residuals (committed `.ufo/waves/round-62/resid/`): ResidRerunD HOLDS (byte-identical except LOCATE timestamp); ResidLine63/74/75/93 SUPPORTED/HOLDS; ResidCriticFreeze MIXED (freeze integrity holds; three revision-1 O guards forced by source inspection, not executed controls — recorded in the lesson `## Errata`).
- LOG round-62 entry cites a2c5caa5/e605603c/f0173481/e6a61e82/9143fc44. Defect (informational): `25b44b8a` and `2ce9d4d1` are not named in LOG.md; the entry cites their artifacts instead.

### Claim O — operability (capability acquisition: tools/reopen-row.py). Verdict: verifies as filed; fitness-for-use deferred by the lane's own marked safety hold. Evidence-verified; gate/selftest not executed.

- Existence: `tools/reopen-row.py` absent at d42ffb89; present at e605603c, a2c5caa5, tip (blob c31ac76a, 100755, 31 478 bytes, unchanged since landing).
- Receipts: `final-measures.txt` ACCEPT-O-62 PASS, 9 legs (TOOL/INDEP/GEN 53/53/ORDER repeats 5/5/BOUND/EXIT/PRIV REFUSED×3/DEFAULT bursts [3,3,3] gaps [60,60] 150 s/ERR), exit 0, counter sha256 a222a156… = freeze record. ResidRerunO HOLDS: two independent fresh-clone runs, both PASS with different random fixtures; `--selftest` "32 checks, 0 failures" (receipt-backed; the build report's own captured selftest reads 28 checks pre-revision-1, the landed 32/32 is receipt-backed — cosmetic wording).
- SCORECARD capability row "bounded row re-opener with archived fallback and caption verdict" present with evidence pointer and first-working round 62.
- Safety hold (closure code read): `Fetcher.fetch` uses plain `urllib.request.urlopen`; the default opener auto-follows redirects (up to 10 hops, cross-host) and `Fetcher.refused()` is consulted once per listed URL before fetch, with no custom redirect handler and no re-check of Location targets — a public URL 302-ing to loopback/RFC1918 is fetched even without `--allow-private`. Malformed URLs (bad port, bad IPv6) raise `ValueError` inside `refused()`'s `urlsplit`/`parts.port` outside the `REOPEN_ERROR` guard → raw traceback. Both defects are real in the committed source; both are disclosed in the report, marked by the appended hold in `corpus/lessons/round-62.md`, `SCORECARD.md` and `corpus/QUALITY.md`, and routed to round 63. The predicate was frozen offline-fixture-only and passes; the hold defers the capability's live utility pending repair + independent review. It does not defeat the claim as filed; it is a named, marked, routed harm-in-waiting, not an unmarked harm.

## 3. Per-axis verdicts (non-author)

| axis | verdict | basis |
|---|---|---|
| depth | improved | four routed overstatements repaired in place and re-measured; sole support moved tier C → tier B |
| operability | improved | falsifiable before→after verifies (no tool → landed tool, frozen predicate PASS, receipts + reruns committed); capability under an explicit safety hold — see routed items |
| calibration | unchanged | honest disclosures (errata, unrun separability, safety hold); no calibration claim |
| coverage | unchanged | no new knowledge surface |
| freshness | unchanged | paused by the open round-11 L0 question |
| adjacency | unchanged | ConnectSiblings: nearest prior art `chousa-shokunin/tools/quote-reopen.py`; no sibling owns footwear/talaria |

## 4. Discernment spot-check (LEARNING.md — checked from outside)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S693 Dictionary.com talaria | admit | live `https://www.dictionary.com/browse/talaria` HTTP 200 (browser UA), quote "wings or winged sandals" present in body; Wayback 2024-05-29 capture HTTP 200, same quote, same page | agree | quote is definition body text (12 words ≤ 25), tier B scoped to the Classical Mythology sense, used-by the repaired entry line 93 |
| Merriam-Webster talaria (tier-A candidate) | reject | live `https://www.merriam-webster.com/dictionary/talaria` → HTTP 403 with the lesson's own curl | agree | live page refuses ordinary requests; capture-only under observed Wayback 429s cannot carry a new row |
| Cambridge Farnese Hermes cast | reject (cross-check) | live page → HTTP 404 today; does not name talaria | agree | even stronger grounds than the filed reason (quote does not name talaria; locator NOT_LOCATED) |
| census validate | — | `scripts/sources-census.sh validate --root … kotodama` → exit 0; `ok corpus/SOURCES.md`; W03 S687 mined-but-unused (matches the lesson old→new log); W04 duplicate-URL warnings are the pre-existing class (S693 not among them) | agree | registry well-formed; the one new row is clean |

Trend verdicts: expansion unchanged (one row added for a repair; no new knowledge surface); quality improved (four routed lines repaired and verified; tier-C sole support removed; all findings found after measurement are marked and routed, none left standing); discernment improved (twelve pre-data controls met revision 0 and were closed before data; counters frozen and hash-identical at measurement; outside spot-check agrees with the gate on the sampled admit and both rejects; the one disclosure gap (three O guards from source inspection, not executed controls) is recorded as an erratum).

## 5. Routed defects for round 63 (and later)

1. (gate, HIGH) `tools/reopen-row.py`: re-validate redirect targets against the private-host refusal; answer malformed URLs with `REOPEN_ERROR`; then independent review — before ANY live use. The capability stays under hold until both land (already lane-routed; closure re-affirms as gating).
2. Residual O gaps flagged by ResidRerunO, already routed with the SSRF: attempts undercount across redirect chains; 30 s timeout is per-socket not per-request; silent 4 MiB truncation → false ABSENT; gzip bodies read as ABSENT.
3. Run `tools/check-claim-separability.py` against the round-63 manifest after landing (round 62's check ran only at the dry run; disclosed, unrun after landing).
4. (informational) LOG round-62 entry names five of the seven landed commit hashes; add `25b44b8a`/`2ce9d4d1` (or their artifact paths) in a future append if a reader needs the chain.
5. (cosmetic) report/lesson reference residual receipts as `resid/ResidRerun{O,D}.md`; the committed files carry the `KotodamaR62.` prefix.
6. (cosmetic) report says the builder landed the tool "selftest 32/32"; the build report's captured selftest is 28 checks (pre-revision-1); the landed 32/32 is receipt-backed by ResidRerunO.
7. (LOW, lane-noted) S693 kind `docs` vs S692 kind `book` same publisher; line 75 drops "from"; census W03 S687 disposition — decide lead-row vs `queued` status change logged old→new.
8. (operator) SHONEN boxes look fully checkable by a non-author this round: SKILL.md decision table (:20), error patterns (:468), executable checklist (:522) verified present; LOG round-62 is an end-to-end routed-defect→repair→measure→review chain; residual seats ran from one line/one row each; ConnectSiblings names no sibling owner of footwear or talaria. Promotion remains operator-owned; this closure wrote no `[x]`.
9. (operator) regenerate lane prompts from the current `lane-addendum.md` (phase-5 content) for future rounds.

## 6. Closure verdict

Both declared claims verify against committed bytes and committed receipts; no axis is harmed — every post-measure finding is disclosed and marked, none left standing. Round admitted. The safety hold on the new capability is recorded here, in the closure entry notes, and gates round 63.
