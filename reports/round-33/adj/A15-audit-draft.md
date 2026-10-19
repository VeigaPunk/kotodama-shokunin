- Seat: A15 | scribe | claim A | date 2026-10-19 | baseline 139e3b6

# Round 33 — adjacency audit, ASSEMBLED DRAFT v6 (A15, final for this seat)

**Status: DRAFT for integrator finalization.** Assembly skeleton for
`reports/round-33/adj/audit-assembled.md`, which has **no seat out** and is the
integrator's artifact (`claims.json:59`; X04-honesty marks it MISSING for that
reason). A15 scribe history: v1 03:54:35Z (empty `adj/`), v2 (4 fragments), v3
(8 + R07), v4 (12 + X00), v5 (+A07), this **v6** folding in A08. Nothing here is
round acceptance; no axis is judged.

**Fragment state at v6** (`ls reports/round-33/adj/`): **every executor fragment
has landed** — `K04`, `A01`, `A02`, `A03`, `A04`, `A05`, `A06`, `A07`, `A08`,
`A09`, `A10`, `A12`, `A13`, `A16` — plus `review/R07-adj-review.md` and
`cross/X00-connector.md`. Owed: the two verifier seats
`A11-verify-a01-a03.md` and `A14-verify-a10.md`.

Three evidence classes, never conflated: **fragment-backed verdict**;
**provisional** (A10's seat-executed rows — a landed fragment wins on
disagreement, A10-F5); **review-corrected** (R07 and A12 re-ran A10's cited
commands and contradict two of its findings — the corrections govern).

## 1. Check table

| # | Seat | Check | Fragment | Verdict at v6 | Basis |
|---|---|---|---|---|---|
| 1 | K04 | method scout: r21/r29 check sets, scope-watch method, counting commands | filed | **DONE** (scout, no verdict class) | `adj/K04-method-scout.md` |
| 2 | A01 | PROVINCE accuracy at HEAD | filed | **PASS ×4**; A01-5 routed finding | `adj/A01-province.md` |
| 3 | A02 | handoff boundary on the current packet pair + contract cross-check | filed | **PASS with one content finding** (A02-H1) | `adj/A02-handoff.md` |
| 4 | A03 | scope watch | filed | **PASS at 03:57:47Z**, one named finding (A03-F1) | `adj/A03-scope.md` |
| 5 | A04 | bleed scan | filed | **zero unfiled bleed**; F-A04-1/F-A04-2 routed | `adj/A04-bleed.md` |
| 6 | A05 | corpus boundary | filed | **PASS ×6** (incl. index integrity, closing A01's stale-prose item) | `adj/A05-corpus.md` |
| 7 | A06 | contested-scope posture | filed | **RESTATED — routed, not absorbed**; §4 stale-pointer finding | `adj/A06-contested.md` |
| 8 | A07 | adjacency history consistency | filed | **9 of 11 filed verdicts hold exactly; 2 superseded by later filed rounds, none false** (D1, D2); F1/F2 routed | `adj/A07-history.md` |
| 9 | A08 | language audit over round-33 fragments | filed | **CLEAN at its frozen snapshot** (04:04:35Z): 2044 pass-1 occurrences all classified, 11 residuals hand-adjudicated, zero verified-without-verifier claims | `adj/A08-language.md` |
| 10 | A09 | pin-cascade exposure | filed | **GREEN on the frozen surface; three non-frozen exposures + R1–R8 re-pin list** (A09-F1…F5) | `adj/A09-pins.md` |
| 11 | A10 | audit receipt draft | filed | **DONE** — provisional table; F1/F2/F6 stand, **F3 corrected (R07-F1, A12-DEF-02)**, F4 closed by A08, F5 stands | `adj/A10-receipt.md` |
| 12 | A11 | independent re-run of A01–A03 commands | owed | `pending` — A13/R07 partially cover the classes | — |
| 13 | A12 | independent re-run of A04–A06 commands | filed | **DONE** — three check classes green at its stamps; two filed defects | `adj/A12-verify-a04-a06.md` |
| 14 | A13 | independent re-run of A07–A09 commands | filed | **DONE** — 5 filed commands (4 exact, 1 currency defect F3); A09-class measured | `adj/A13-verify-a07-a09.md` |
| 15 | A14 | A10 receipt matches fragments row-for-row | owed | `pending` — now fully actionable: all nine A10 rows have landed fragments to match against | A10-F5 |
| 16 | A16 | SHONEN-section material | filed | **DONE** — four boxes untouched, conditions carried named | `adj/A16-shonen-material.md` |

Adversarial/cross coverage: **R07 filed** (23 re-runs; three material findings
against A10); **X00 filed** (dependency map, collision matrix, pin-cascade §3);
**R08** still owed.

## 2. Landed executor/verifier verdicts (digest)

**A01 — PROVINCE accuracy PASS.** Last touch `c53782ab…` (2026-10-17), blob
`313b182f…` identical at `c53782a` and HEAD, empty diff across 79 commits, 31
lines, sha256 `05b34a57…`; precision correction: the claim's "pre-round-8" is
really **pre-round-5**; A01-5 filed the wave-time filed-byte mutation.

**A02 — handoff boundary PASS with A02-H1.** Current pair fixed by the
renderer's own default (`tools/exercise-handoff-e2e.py:1933-1934` →
`reports/round-30/handoff/declared-in-r6/`), not by mtime. Eight re-runs green
(gate `16/16 / 20 / 0` from lane root and a foreign cwd; e2e `--quiet` exit 0,
packet sha256 `6ced88ad…` = `freeze.txt:2` = `expected.json.packet_sha256`;
`--selftest` 39 controls; links 105/105; uncertainty 27 claims, no findings).
Three stdin tamper probes red as designed; two earlier probes proved nothing and
are disclosed as such. Contract cross-check: digest `5f4c02bf…` = the packet's
`contract_ref` = `expected.json.cross_refs.contract_digest`, so §1's re-read
trigger is not tripped; 58/58 manifest paths exist and match their pins;
§6/§8/§9/§10/§11 green.

**A03 — scope watch PASS at 03:57:47Z.** 2655 tracked at HEAD *and* baseline;
`git diff --stat 139e3b6..HEAD` empty; protected roots 1830 + 179 + 237 = 2246;
`reports/round-33` 0 tracked; working tree 3 declared rows; protected-root
status **0 rows**; no out-of-lane write by this lane. Named finding A03-F1.

**A04 — bleed scan: zero unfiled bleed.** L0 file `60ccdc9e…`, mtime
2026-10-18 17:14 (pre-declaration), exactly four kotodama rows `:44-47`,
append-only (4 additions, 0 removals). Both lore-owned items restated with
current pointers including lore's own side (`lore-shokunin/l0-questions.md:5,6-7`).
No round-33 artifact references `kotodama-lore-adjacency`, `5f4c02bf` or
`50c4c2f2`.

**A05 — corpus boundary PASS ×6.** Six partitions exactly match the owns-list
(both directions); `examples/` non-canon confirmed at directory and artifact
level with six generated leaf fixtures inheriting directory status (coverage
note, not a defect); verification/civilizations drift PASS across 501 term-lines
in 114 files with 17 classifier residuals read line-by-line; out-of-repo
inventory exactly 2 read-only citations (one in-repo; one absolute fleet path at
`header-conformance-readings.md:4` with a declared `recheck:` trigger —
observation for a future portability pass, not drift); corpus and examples
untouched in the round-33 write window; index integrity PASS, **closing A01's
stale-prose item** as a dated reading superseded in-file by revision 1.9.

**A06 — contested-scope posture RESTATED — routed, not absorbed.** Two
lore/integrator-owned items plus one operator-gated item restated with pointers
re-verified at the cut; an absorption-pattern scan found 23 lines naming the
items, every one `pending`/`open`/`lore-owned`/`routed`/`owed`, **none asserting
a completed read, ratification, or ownership transfer**; A12 independently ran
the same check class before the fragment existed and agreed. §4 files the
stale-pointer finding: non-filed lane-owned example surfaces still cite the
superseded contract digest `50c4c2f2…`.

**A07 — adjacency history consistency: 9 of 11 filed verdicts hold exactly; 2
partially superseded, both by later filed rounds, none false.** Eleven filed
r21/r29 commands re-run verbatim, including an archive reconstruction of the r21
audit tree (`git archive 8115eaa…`) so moving counts are compared at their
revision of origin. Exact holds include: `assemble-d4-typed.py --selftest` 12/12;
the RGL extraction block field-for-field; `PROVINCE.md` blob `313b182f…` and
`git diff --quiet` exit 0; the r29 ledger census character-for-character;
`entry-audit.py` `entries=201 / index_failing=[] / bar_failing_count=184`; the
x63 source-resolvability numbers; the four-sweep reconstruction **byte-identical
including every line number**; the r21 inventory census; the
`corpus/README.md:138-139` locator rows. Supersessions: **D1** r21's gate leg
count 19 → 20 (the extra `L3b-argot` leg landed at `fc13cd2`, round 25 — the r21
verdict's substance holds); **D2** r29's three-file pin check 2 of 3
(`PROVINCE.md` and the contract still reproduce; `AGENTS.md` moved by filed
rounds 30/31, `11df1fd` + `17e90b9`, 29 insertions 0 deletions — dated
supersession with named provenance, not drift). Findings **F1** (orphan drafting
residue live in `AGENTS.md`) and **F2** (r29's `A29-ADJ-EVID-01` still
uncorrected) are carried in §3.

**A08 — language audit: CLEAN at the frozen snapshot (2026-10-19T04:04:35Z).**
Two passes over every file under `reports/round-33/`: pass 1 (broad, five term
families incl. the verdict verbs) found **2044** occurrences, every one a
negation (970), routed reference (127), mention (826) or cited result (111);
pass 2 (strict affirmative verdict frames) found **108**, of which 1 residual.
All **11** residuals were hand-read and adjudicated — ten are
evidence-introducing frames (`<verdict word> …:` followed by a fenced block or
table carrying the citation) and one is an ordinary-sense adjective ("K03's
canonical table"). Zero verified-without-verifier claims. The seat states its
own precision ceiling honestly (the scanner cannot see that a cited block
follows a colon) and binds its verdict to the per-file digest manifest rather
than to the final wave. **This closes the language leg that A10-F4 and R07-F7
left open — for the snapshot, not for fragments landed after it.**

**A09 — pin cascade: GREEN on the frozen surface, three non-frozen exposures.**
Zero frozen exposure confirmed independently: 0 hits for README/SKILL.md in all
11 `MANIFEST.tsv`; 20 `expected.json` baselines name neither file; SKILL.md
appears under frozen only as prose inside immutable snapshots; the four frozen
artifacts mentioning `corpus/lessons` are path strings whose source-ledger
digests still reproduce exactly. Real cascade: **E1** the README pinned by git
blob inside round-26's runner and seat tool; **E2** recorded digests at 6 README
+ 8 SKILL.md sites becoming superseded readings; **E3** box-1's live re-survey
obligation; **E4** line anchors (`AGENTS.md:42`'s `after :534` already 179 lines
off); **E5** the README's own in-file pins. Deliverable list **R1–R8** with
owners; none is a frozen re-pin.

**A12 — verification of A04–A06 classes: green at its stamps**, plus
A12-DEF-01/02 (§3).

**A13 — independent re-run of A07–A09 classes**: five filed r21/r29 commands
re-run, four reproduce exactly (including the r29 ledger census and the
four-sweep reconstruction), the fifth exposes A21-D4-XF-01's evidence currency
(A13-F3); A08-class partial clean over 7 files; A09-class found the two live
README pins (A13-F1).

**A16 — SHONEN material: four boxes untouched**, marks `[ ]`, SHONEN.md
unchanged since mint; box-1 inventory re-verified green at live bytes (28/28,
`skill_sha256 79fe91d3…` = live SKILL.md); §6 ready to paste.

**X00 — connector.** Dependency/sequencing map (X00 → A09 → R08); collision
matrix on the three shared files: the README (four O-seat drafters; its own rule
at `README.md:303-306` — superseding edits land as a new revision block, never
an in-place rewrite of per-round provenance claims; precedent = the Revision 2
block), SKILL.md (C14 drafts; no frozen pin, so the risk is anchoring not
pinning), and **`AGENTS.md` — no seat, and no seat may act on it**: `AGENTS.md:42`
is the trailing line of the round-31 patch scaffold quoted into dispatch prompts,
and read as an instruction it would collide with C14 and the already-landed item
at `SKILL.md:713-715`. Plus two in-README format collisions (queue-row pipe
escaping; the "Revision 3" naming collision with a filed round-26 artifact).

## 3. Findings carried into `audit-assembled.md`

Ordered by materiality. **No row is a promotion, canon, clearance, or closure
verdict.**

| id | finding | owner | state |
|---|---|---|---|
| **A09-F1 / A13-F1 / R07-F4** | **The lessons README is pinned by git blob inside round-26's runner** (`reports/round-26/run-validation.py:97` `README_BASELINE_BLOB = a3187055…` = live blob; `:1494-1500` fails the claim when it differs; mirrored at `reports/round-26/lessons/c51-revision-audit.py:48`; `reports/round-25/validation.json` also pins `input_sha256 = ec7469da…` = live sha256). Claim O requires the README itself to carry 33/33 rows and c31's `INDEX` is hard-coded to that path, so a revision-file-only approach cannot satisfy the declared counting command while an in-place edit supersedes the r26 pin. **A10's "no re-pin owed" must not be carried as the A09 verdict for the README leg** (it stays correct for SKILL.md and the frozen surface). X00 adds: row-cell repair is admissible only inside a **new named revision block with its own control line**, and "Revision 3" is already taken by a filed round-26 artifact. Options: new revision block + recorded supersession of both pins; exclude the README from the O-leg edit; or carry the tension without landing the edit. | claim-O integrator + R08 | open, material |
| **A09-F2 / A12-DEF-01** | **Filed receipts were written in place during the wave — three files, not two.** `reports/round-5,6,7/validation.json`; window 03:53:25Z–03:55:27Z; round-6 byte-identical (mtime-only), rounds 5/7 content-differing then restored (`git hash-object` = `git rev-parse HEAD:<f>` for all three). Cause visible in the deltas: both historical runners write their own receipt (`reports/round-5/run-validation.py:194`, `reports/round-7/run-validation.py:1171`) and **neither references `tools/harness/receipt_guard.py`** — the round-14 guard never fired, a guard-**adoption** gap, not a guard-behaviour defect. Not an authorized refresh (HEAD never moved; the round-23 `c64b2b3` precedent is committed and guarded). Probable writer C05, `to-verify`. **Consequence:** claim A's threshold requires the scope delta to be fully explained by `reports/round-33/` + `REGIMEN.md`/`LOG.md` appends (`claims.json:63`); this delta is not, so the scope condition is breached by a non-seat write in flight until the integrator records it. Recovery is the integrator's (`git checkout -- <paths>`); no seat may perform it. **`reports/round-26/run-validation.py` carries the same hazard** (default mode rewrites its filed receipt at `:90,1909`). | A03/X02 + integrator | open (restored), record owed |
| **A02-H1** | **The current default packet pair is shape-green and semantically stale.** Manifest rows `packet.md:68,69` agree with live bytes, but the claim ledger and OQ rows describe older numbers: `:148` typed_labels 74 / native-form 56 / findings 16 / hold-or-fail 15 vs live 82 / 64 / 12 / 12; `:149` hold 15, note 1 vs live hold 12, note 0; `:150,152` conflicts 4 and quarantine 3 vs live 0/0; `:307` OQ-V3-05 repeats them; the twin is stale in the same places. Every green check is shape/vocabulary-only, so 16/16 + 105/105 + 27 claims are consistent with stale prose. Concrete instance of the r32 standing item "r18 D4-adapter baseline supersession semantics (pins green, content ages)". Fix = a **new revision from live bytes** (contract §9); filed r2/r4/r5/r6 bytes stay frozen. | packet/renderer owner + integrator | open, material |
| **A07-F1 / A09-F3 / X00 §2** | **`AGENTS.md` carries leaked drafting residue**: `:40` an unmatched fence and `:42` an orphan `### 2.2 SKILL.md — append one item … (after :534)` heading, both landed by round-31's `17e90b9`. It sits in a live fleet instruction file every seat reads, and read as an instruction it would collide with C14 and the landed item at `SKILL.md:713-715`. **No seat may act on it** (X00); bounded fix draft for the integrator if the operator wants it: delete `:40` and `:42`, verify `grep -c '^```' AGENTS.md` → 0 and `wc -l` → 40. The anchor itself is 179 lines stale. | round-31 integrating parent (operator-visible) + integrator | open, routed |
| **A07-F2** | **r29's `A29-ADJ-EVID-01` is still uncorrected at HEAD**: the `which semantic fields` absence claim in `corpus/knowledge/linguistics/register-lexicon-ceilings.md:4` remains contradicted by `sound-symbolism.md:106`; the entry is 289 lines, sha256 `bb579d51…`, with no append-only amendment across rounds 30–32. Carried so the audit does not read A07's "holds exactly" reproduction as a correction. | entry owner / integrator (append-only amendment) | open, carried |
| **R07-F1 / A12-DEF-02** | **A10-F3 is false as written.** `reports/round-25/audit/c31-lessons-index-audit.py:462` returns `0 if not findings else 1` — plain mode exits **1** on the two findings (measured four times across R07/A12/O01); the exit-0-with-findings behaviour exists **only under `--json`** (`:456-458`). Corrected form: *plain-mode exit codes are informative here; a validator leg that runs a tool in `--json` mode must assert on `findings[]`, not the exit code.* | A10 owner + integrator | corrected; A10's A04/A05/A06 rows unaffected |
| **A06 §4** | **Stale contract-digest pointers in non-filed, lane-owned example surfaces** still citing the superseded `50c4c2f2…` rather than the live `5f4c02bf…`. Reported, not fixed; filed bytes untouched. | integrator (bounded fix draft) | open |
| **A09-F4** | `x57 --selftest` reads 34/37 at HEAD and `x45` exits 1 (`X45-P1`); neither is on a live round-33 surface, but neither may be quoted as a green instrument. | A15/A10 + integrator | open, naming |
| **A09-F5** | The declared SKILL.md fix targets (`:486/:488/:501/:128`) sit between the `:47` self-citations and the `:534` anchor, so C14's line behaviour decides whether R5 is a no-op or a re-issue. | C14 owner + integrator | open, owed |
| **R07-F3** | **"The current packet pair" has three referents across the fragments** (A10 → the Markdown sample; A15 → the r30 `declared-in-r6` packet; the r21 re-run → the r20 packet). All green, so no verdict is at risk, but the threshold's surface must be named once. Related datum: the **YAML** sample scans `glossary-entries=0` — expected (glossary count is a Markdown-surface property; `examples/handoff-packet.sample.md:6-8` states the Markdown supersedes the YAML) but must be named so a re-runner does not read it as a regression. | A02 owner + integrator | open, naming |
| **A13-F3** | `A21-D4-XF-01`'s cited evidence no longer reproduces at HEAD — evidence currency, not new bleed. | A07/A13 + integrator | open, currency |
| **A13-F2 / F-A15-2** | Two "tracked path" baselines in play: r32's "1,870" is the protected surface at *its* baseline; the claim's "2,655" is the whole lane. Same-surface count today **1,905** (1,770 + 135). Without the note the audit reads as a 785-path breach. | A03 + integrator | open, reporting clarity |
| **A10-F1 / A07-D1** | r21's filed D4 pipeline leg count 19/19 → live 20/20; verdict unchanged. | A07 + integrator | confirmed by R07-F6 and A07 check 2 |
| **A10-F2 / A07-D2** | r29's filed `AGENTS.md` digest `be3a9477…` vs live `1afaf106…` — explained by filed rounds 30/31 (`11df1fd`, `17e90b9`); K04 concurs ("not an unexplained drift — do not file it as one"). | A07/A13 + integrator | resolved by explanation |
| **A10-F4 / R07-F7** | The language leg is **closed at A08's snapshot** (04:04:35Z) and **not** for fragments landed after it; if any fragment changed after that stamp, re-run the sweep and record the pattern used (counts differ legitimately between patterns). | A08 + integrator | closed at snapshot, re-check owed |
| **A10-F5** | A10's nine rows are provisional; on disagreement the fragment wins and the row is errata. | integrator + A14 | open, procedural |
| **A10-F6 / F-A04-2** | `LOG.md`'s ` M` row is the pre-wave regimen declaration (+18 insertions, mtime 03:42:59Z, before the 03:49:01Z declaration). | integrator | note only |
| **F-A15-1** | claim's "pre-round-8" phrasing understated | — | **closed by A01** (pre-round-5); R07-F5 confirms |

Also owed, not findings: `reports/round-33/run-validation.py` — claim A's
counting command (`claims.json:61`) — does not exist, so no fragment could run
it; and A01's incidental note of an empty untracked tree
`kotodama-shokunin/reports/round-29/defects/` (path-mimic hazard; optional
integrator cleanup, not a PROVINCE matter).

## 4. Scope-watch section (draft text for `audit-assembled.md`)

> **Scope watch — PASS at 2026-10-19T03:57:47Z (A03), with one named finding.**
> Tracked surface byte-clean against baseline `139e3b6`: **2655** paths at HEAD
> and 2655 at the baseline commit, zero baseline→HEAD delta, **zero**
> working-tree rows under `reports/round-1..32`, `corpus/lessons`,
> `tools/gates/frozen` (2246 protected paths). Only working-tree delta is the
> declared in-lane one: the append-only `LOG.md` regimen entry (+18/0), the new
> `REGIMEN.md`, and the untracked `reports/round-33/` surface (0 tracked). No
> fleet-root write by this lane; `.ufo/l0-questions.md` untouched; no
> `.ufo/reports/round-33/`. **Count reconciliation:** r32's "1,870" is the
> protected surface at its baseline, not the whole lane; the same-surface count
> today is **1,905** (1,770 + 135), the +35 being round-32 artifacts filed after
> that watch. **Named finding A03-F1:** `reports/round-5,6,7/validation.json`
> were written in the working tree during the wave and restored byte-exact by
> 03:55:27Z — a `shared_rules[1]` violation event (guard-adoption gap, probable
> writer C05 `to-verify`) that must be recorded and prevented, not read as "did
> not happen"; it is also not explained by the claim's declared scope-delta
> allowance, so the round record must carry it explicitly. Sampling cannot
> exclude a write-and-restore between samples; the pass is byte/mode cleanliness
> at the sampled instants.

## 5. Contested-posture section (draft text for `audit-assembled.md`)

> **Contested scope — routed, not absorbed (A06, corroborated by A04/A12/R07).**
> (a) **Bilateral same-revision read**: contract fields
> `worldbible-integration-contract.md:14,16`; the contract's own text says initial
> bilateral acknowledgement is *pending* (`:15`), §1's read gate (`:127`) unmet;
> packet side pending (`reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`,
> OQ-V2-02 blocking-for-first-transfer). Open question `.ufo/l0-questions.md:44`
> (kotodama round-2); lore's own record `lore-shokunin/l0-questions.md:5`
> (round-89: lore holds no acknowledgement record for `kotodama-lore-adjacency`).
> (b) **Contract-digest ratification**: who owns the digest update and whether
> lore's r93 ratification subsumes it — `.ufo/l0-questions.md:45` (kotodama
> round-8); digest chain re-measured `e834f503…` → `50c4c2f2…` → `5f4c02bf…`
> (round-8 sweep), all declared revision `1.0.0` — the drift class the question
> names; escalation detail `reports/round-8/adjacency.md:104-114,137-150`; lore's
> round-93 side `lore-shokunin/l0-questions.md:6-7`. (c) **Freshness threshold
> recalibration** — `.ufo/l0-questions.md:47` (kotodama round-11); axis-move
> pause in force (`claims.json:18`). Fourth carried line:
> `.ufo/l0-questions.md:46` (round-9 /tmp inode exhaustion). **Round 33 absorbs
> none of them**: no round-33 artifact references `kotodama-lore-adjacency`,
> `5f4c02bf` or `50c4c2f2`; the absorption-pattern scan found 23 lines naming the
> items, every one `pending`/`open`/`lore-owned`/`routed`/`owed` and none
> asserting completion; `claims.json:68` declares no promotion/canon/clearance/
> closure verdicts; A08's two-pass audit found zero un-negated, un-routed,
> uncited verdict language across the fragment set. PROVINCE governs: "Contested
> scope → report to the integrator, never absorb" (`PROVINCE.md:25`); "Out of
> province → report, never absorb" (`:31`). Adjacent-but-distinct and **not**
> covered by this section: the SHONEN promotion marks (operator-owned), the
> round-32 routed O/C debt (owned by claims O/C), the filed findings
> `A21-D4-XF-01` / `A29-ADJ-EVID-01` (neither re-evaluated nor closed this
> round), and the `AGENTS.md` drafting residue (A07-F1 — filed bytes, routed to
> the round-31 parent, not contested scope).

## 6. SHONEN section for the round report

Use `adj/A16-shonen-material.md` §6 verbatim (or as edited): four boxes
untouched, conditions carried named, marks operator-owned per `SHONEN.md:10-11`.

## 7. Verification chain and integrator assembly recipe

1. Wait for A11 and A14 (the two remaining verifier seats).
2. Fill their rows from their fragments; a fragment beats A10's provisional row
   (A10-F5). Carry R07's and A12's corrections **as corrections** of A10
   (R07-F1/A12-DEF-02 on F3; R07-F2/A12-DEF-01 widening F3's mutation set to
   three files), never as parallel votes.
3. If any round-33 fragment changed after A08's 04:04:35Z snapshot, re-run the
   language sweep over the final set and record the pattern used (A08's manifest
   is the digest-bound input set to compare against).
4. **Decide the README pin question (A09-F1/A13-F1/R07-F4) before the O-leg edit
   lands**, honouring the README's own revision-block rule and the "Revision 3"
   naming collision (X00 §2); route to R08 for the pin test. Produce R1–R8's
   records (A09 §3) — none of them a frozen re-pin.
5. Record A03-F1/A12-DEF-01 (three files, window, restored digests, guard-adoption
   gap) and add the repeat-prevention note; at close re-check that the three
   receipts still match HEAD and that protected-root status is 0 rows.
6. Write `reports/round-33/run-validation.py` (does not exist) with A-legs
   asserting scope-watch counts, protected-root status rows, and the A03-F1
   finding; assert on `findings[]` wherever a leg runs `--json`.
7. Confirm the final artifact carries no unnegated promotion/canon/closure
   language and all six `after_required` checks are present (`claims.json:59`).

## 8. What this draft does not do

No promotion, canon, clearance, or closure verdict (`claims.json:68`). No filed
round byte was written by this seat; rounds 1–32, `corpus/lessons/*.md`,
`tools/gates/frozen/**` and fleet `.ufo/**` were read only. This seat wrote
exactly one file, this one; no git-mutating command, commit, or push; no
installs, no network. A10's provisional rows are quoted as A10's; R07's and
A12's corrections are carried as corrections of A10. A08's verdict binds its
snapshot digests, not this draft.

## Owed

Fragments absent at v6 (`ls reports/round-33/adj/`):

- `reports/round-33/adj/A11-verify-a01-a03.md`
- `reports/round-33/adj/A14-verify-a10.md`

Also owed, not this seat's to produce: `reports/round-33/adj/audit-assembled.md`
(integrator) and `reports/round-33/run-validation.py` (integrator; claim A's
counting command, `claims.json:61`).

## Citations

Fragments read in full or in part: `adj/K04-method-scout.md`,
`adj/A01-province.md`, `adj/A02-handoff.md`, `adj/A03-scope.md`,
`adj/A04-bleed.md`, `adj/A05-corpus.md`, `adj/A06-contested.md`,
`adj/A07-history.md`, `adj/A08-language.md`, `adj/A09-pins.md`,
`adj/A10-receipt.md`, `adj/A12-verify-a04-a06.md`, `adj/A13-verify-a07-a09.md`,
`adj/A16-shonen-material.md`, `review/R07-adj-review.md`, `cross/X00-connector.md`.

- `reports/round-33/claims.json:6,8,18,29,33,57,59,61,63,68`; `reports/round-33/targets.json` (missions, shared_rules)
- `REGIMEN.md`; `PROVINCE.md:9-14,16-20,22-25,27-29,31`; `SHONEN.md:5-11`; `AGENTS.md:13-39,40-42`
- `reports/round-32/scope.md:12`; `reports/round-32/dossier-d13-operator-decisions.md:135,138`; `reports/round-32/dossier-d11-shonen-boxes.md:49-51,192-194`; `reports/round-24/promotion-review.md:37,91,135,199`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:7,14-16,51-70,92-106,124-136,138-157,159-187,209`
- `corpus/lessons/README.md:97,207,303-306,307-345`; `SKILL.md:47,128,149,183,486,488,501,522,534-536,660,713-715`
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:4`; `corpus/knowledge/linguistics/sound-symbolism.md:106`
- `reports/round-30/handoff/declared-in-r6/{packet.md,freeze.txt,expected.json,twin.json}`; `examples/handoff-packet.sample.md:1-20`; `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`
- `reports/round-26/run-validation.py:90,96-97,1494-1510,1871,1909`; `reports/round-26/lessons/c51-revision-audit.py:48`; `reports/round-25/validation.json`; `reports/round-25/audit/c31-lessons-index-audit.py:36,456-462`; `reports/round-25/audit/x45-lessons-pointer-audit.py:178-179`; `reports/round-27/audit/x57-lessons-audit.py`; `tools/harness/receipt_guard.py:7,147,152,161`
- `reports/round-5/run-validation.py:194`; `reports/round-7/run-validation.py:1171`; `reports/round-30/craft/box1-survey.py:5,10`; `reports/round-30/run-validation.py:697-700`
- `reports/round-21/adjacency/province.md:11,17`; `reports/round-21/adjacency/entries.md`; `reports/round-21/adjacency/A11-A12-handoff.md:41,43,46`; `reports/round-29/adjacency/A09-A12-handoff.md`; `reports/round-29/adjacency/province-entries.md:15,31,42`
- `reports/round-28/audit/entry-audit.py`; `reports/round-28/audit/x63-entry-source-resolvability.py`; `corpus/README.md:138-139`
- `corpus/knowledge/verification/header-conformance-readings.md:4,6`; `corpus/knowledge/verification/internal-consistency-audit.md:11`; `corpus/knowledge/verification/gate-frozen-run-standard.md:6-8`
- `lore-shokunin/l0-questions.md:5,6,7` (read-only sibling); `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45,46,47`
- `tools/gates/handoff-packet-check.py:53-68,122-140,171`; `tools/exercise-handoff-e2e.py:184,1933-1934,3522-3532`; `tools/gates/typed-pipeline-gate.py`; `tools/gates/argot-derivation-gate.py:4`
- `reports/round-33/cross/X03-protocol.md:45,148`; `reports/round-33/cross/X04-honesty.md:75,126`
- Commands run by this seat, 2026-10-19T03:50–04:10Z (all read-only):
  - `git rev-parse HEAD` → 139e3b662900557afe54f632b468619593dc9fcb
  - `git ls-files | wc -l` → 2655; `git ls-files tools/gates/frozen | wc -l` → 237; surfaces 1857/237/561 and 1770/135/1905
  - `git status --porcelain -uall` (3→5→23+ rows as landings continued); `git status --porcelain=v1 -uall -- reports/round-{8..32} tools/gates/frozen` → 0 rows; `git diff --stat -- LOG.md` → 18 insertions
  - `git log --format='%H %ad %s' --date=short -1 -- PROVINCE.md` → c53782ab… 2026-10-17; `git diff --quiet -- PROVINCE.md` → exit 0; `sha256sum PROVINCE.md` → 05b34a57…
  - `python3 -B tools/gates/handoff-packet-check.py` on the r30 packet, the sample .md, `--selftest`, and the r20 packet → exit 0, 16/16, 0 findings each
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, packet_sha256 6ced88ad…
  - `grep -rn -i -E "promot|canon|clearance|closure|verified" reports/round-33/` → all negation/routed (pattern noted; superseded in coverage by A08's two-pass audit)
  - `ls corpus/knowledge/` + per-partition counts → 94/18/21/19/29/20 = 201
  - `find /home/vgpnk/Projects/shokunin/.ufo -maxdepth 3 -newermt "2026-10-19T03:49:00"` → no rows
  - `ls reports/round-33/adj/` at 03:54Z (empty), 03:56Z (4), 04:00Z (8), 04:05Z (13), 04:10Z (14)
  - `date -u` → 03:54:35Z (v1), 03:56:19Z (v2), 04:00:00Z (v3), 04:04:58Z (v5 check), v6 after 04:05Z
