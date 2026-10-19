- Seat: R04 | reviewer | claim C | date 2026-10-19 | baseline 139e3b6

# R04 — adversarial review of the `calib/` fragments (claim C)

Mission (`reports/round-33/targets.json`, seat R04): "Adversarial review of calib/
fragments: re-run cited commands, check ledger draft rows against C01-C12
fragments, hunt duplicate/contradictory dispositions."

**Observation cut:** 2026-10-19, lane HEAD `139e3b662900557afe54f632b468619593dc9fcb`
(`git rev-parse HEAD`) == the round's declared baseline (`reports/round-33/claims.json:8`).
**Write scope:** this file only. No filed byte edited, no git, no installs, no
network. Non-author declaration: this seat authored none of the artifacts it
cites; every verdict below is a dated command run by this seat or a prior
round's filed byte, quoted with `file:line`.

**Fragments available at this cut** (`ls reports/round-33/calib/`): `K03-open-items.md`,
`P02-plan.md`, `C01-item-01.md`, `C03-item-03.md`, `C07-item-07.md`,
`C11-item-11.md`, `C12-item-12.md`, `C16-receipt.md`.
**Not landed:** `C02`, `C04`-`C06`, `C08`-`C10`, `C13`, `C14`,
`C15-ledger-draft.json`, and `reports/round-33/run-validation.py` (see `## Owed`).
This review therefore attacks the **identity/count layer**, which is where the
landed fragments can already be shown to conflict, and leaves the
disposition-content layer of the missing fragments to a re-review.

## 1. Independent re-execution receipt (all commands re-run by this seat)

| cited claim | source fragment | this seat's re-run | verdict |
|---|---|---|---|
| D13 Decision-4 table has 9 data rows | `K03-open-items.md:24-28` | `sed -n '130,138p' reports/round-32/dossier-d13-operator-decisions.md \| grep -c '^\|'` → `9` | **VERIFIED** |
| "12 standing open items" is the filed numeral | `K03:17-20`, `C16:23-27` | `SCORECARD.md:443-444` ("Routed debt recorded for the operator: the falsifier / audit's filename mismatch (substance 5/5), 7 unindexed lessons, 12 standing"); `LOG.md:3513` | **VERIFIED** |
| `final-dossier.md` says "Twelve named items" | `K03:21-22` | `reports/round-32/final-dossier.md:107-110` | **VERIFIED** |
| C01's gate re-run: exit 0, 12 holds, digest `865bb03e…` | `C01:85-101` | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit **0**; stdout sha256 **`865bb03e1694dc0f98a22eb2e44faab720eb1982632ec1ef04030c507a08ecba`**; 12 × `D2L-FORM-UNRESOLVED` = `GAR-01..06` + `LEX-GAR-01..06`; `summary: 20/20 legs passed`; digest matches the filed r31 row `reports/round-31/final-sweep.md:62` | **VERIFIED** (byte-exact) |
| C01's `expected-holds.json` arithmetic | `C01:106-114` | `counts = {"hold": 12, "note": 0, "fail": 0}`; `holds` n = 12; ids `{D2L-FORM-UNRESOLVED}`; `packet_sha256 aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` == `sha256sum examples/culture-d4/packet.d4.yml` | **VERIFIED** |
| C01's `D2L_FORM` symbol reference | `C01:127,192-202` | `tools/d2-typed-labels.py:422` reads `D2L_FORM = "D2L-FORM-UNRESOLVED"` — the assertion is a Python-symbol reference, not a literal token; **no finding** | **VERIFIED** |
| C12's r18 frozen digests | `C12:33-40` | `sha256sum` of both frozen inputs → `a59990bb…` / `e7ecd204…`, byte-identical to the two `input_sha256` values in `tools/gates/frozen/round-18/freeze-receipt.json` and to `MANIFEST.tsv:2-3` | **VERIFIED** |
| C12's §5 wording | `C12:20-24` | `reports/round-31/final-sweep.md:187-192` verbatim | **VERIFIED** |
| C07's rubric pointers | `C07:40-63` | `grep -n "rubric" SCORECARD.md` → `:14, :624` (exactly two); `corpus/QUALITY.md` = 23 lines, `grep rubric` no matches (exit 1); `corpus/lessons/README.md:75,163`; `reports/round-5/kotodama.md:54`; `grep -rn rubric reports/round-2[7-9]/ reports/round-3[0-1]/ \| wc -l` → `0` | **VERIFIED** |
| C07's C42 quote | `C07:67-77` | `reports/round-26/open-questions/C42.md:58-60` reads "…deliberately left open rather than papered over with an invented rubric. Next touch round 27."; `reports/round-26/zzz-lessons-index-revision-4.md:229` re-declares the same next touch | **VERIFIED** |
| K03/C16/C12's ceilings reading | `K03:64`, `C16:63` | `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` (KTD-RLC-S-0001) and `:19` (delivered gate `legal=19 illegal=8`, pre-fix reader `18/9`, `--selftest` 10/10) | **VERIFIED** |
| the box-1 conditions and the N-set line numbers | `K03:65-68`, `C16:64-68` | `promotion-review.md` `:71-76` (cond 2), `:77-80` (cond 3), `:81-84` (cond 4), `:85-88` (cond 5), `:178` (N1), `:186` (N4), `:189` (N5), `:193` (N7) — all exact | **VERIFIED** |
| live SKILL bytes still stale | `C16:64-66` | `SKILL.md:486` cites `loanword-material-dating.md:26,60`; `:488` cites `:57`; `:491` carries `FIELD_DEFAULTS`/`fictional-coordinate`/`descriptive-gloss`; `:501` and `:128` cite `worldbible-integration-contract.md:183`; all five anchor tokens `grep -c` → **0** in `tools/d2-typed-labels.py` | **VERIFIED** |
| the devin null counters | `K03:72`, `C11:105-…` | `reports/round-25..28/availability.json` each read route `devin/deepseek-v4-1-flash-high`, requested `64`, `launched_workers`/`completed_workers` `None`; `reports/round-29/recount/audit.md:18,23`; `dispositions.md:22`; canonical record `reports/round-29/devin-availability-disposition.md` | **VERIFIED** |
| the L0 queue rows | `K03:69-70`, `C16:69` | `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45` (kotodama round-2 and round-8 rows); `grep -c "^kotodama"` → `4`; 49 lines. **Out-of-repo read** (fleet root, read-only) | **VERIFIED** |
| `git ls-files \| wc -l` = 2655 | `C16:118` | `2655` | **VERIFIED** |
| K03's table is self-consistent at 12 | `K03:60-73` | `grep -c "^\| OI-" reports/round-33/calib/K03-open-items.md` → `12` | **VERIFIED** |

**Zero citation errors found in the landed fragments.** Every `file:line` this
seat spot-checked resolved and said what the fragment said it said. The findings
below are therefore not accuracy findings — they are **identity and assembly**
findings.

## 2. F1 (major, assembly-blocking) — the "12" is underdetermined: five decompositions, two incompatible camps

`claims.json` claim C requires `open-items-ledger.json` rows == "K03's
canonicalized 12 (cross-checked against SCORECARD's '12')". The landed fragments
produce **five distinct decompositions that each land on 12**, and they do not
have the same membership. Each is a seat's own reconstruction, because the filed
sources never state an expansion rule:

| # | source | decomposition that reaches 12 | item 7 | item 11 | item 12 |
|---|---|---|---|---|---|
| 1 | `K03:36-43` (adopted canonical) | 9 D13 rows; box-1 `+2`; lore-owned `+1` | cold-run cluster | devin | adapter |
| 2 | `C16:52-57` | 9 D13 rows; box-1 `+2`; cold-run `+1` (N1 \| N4/N5/N7) | N1 | devin | adapter |
| 3 | `C12:6-15` | 9 D13 rows; box-1 as 1; cold-run `+3` | N5 | devin | adapter |
| 4 | `C11:35-46` (P1) | D13's 9 rows + D11's 3 box-4 readings | rubric | box-4 3b | **box-4 3c** |
| 5 | `C11:35-46` (P2) | D13 rows 1-4,6-9 (8) + cold-run `+3` | rubric | devin | adapter |

Two further arithmetics appear on the record and reach 12 as well:
`P02:106-114` Candidate B (= #1) and Candidate A (3 design + 3 box-1 + 4
cold-run + 2 lore, which `P02:110-114` notes "drops the rubric gap, devin
telemetry, and adapter supersession, which `final-dossier.md:107` explicitly
lists among the twelve").

**Why 12 is not a measured quantity.** The D13 table has 9 rows
(`dossier-d13-operator-decisions.md:130-138`, re-measured `9` by this seat).
Exactly three of those rows bundle multiple named conditions — box-1
"conditions 2-4" (3 items, `+2`), cold-run "N1/N4/N5/N7" (4 items, `+3`), and
"lore-owned: bilateral read + L0 contract-digest ratification" (2 items, `+1`).
To reach `9 + 3` a seat must spend exactly `+3` of the available `+2/+3/+1`
splits, and there are **four** ways to do that: `{box1+2, lore+1}` (= #1),
`{box1+2, coldrun+1}` (= #2), `{coldrun+3}` (= #3), `{lore+1, coldrun+2}` (not
claimed by any seat), plus the off-table `{+3 readings}` (= #4) and the
drop-three-rows variant (= #5). The numeral 12 therefore does not select a
membership; it selects a *class* of memberships.

**Camp structure.** #1/#2/#3 agree on items 1-6 and on 12 = adapter; #4 puts the
adapter at item 9 and fills 10-12 with D11's box-4 readings; #5 agrees with #4
on item 7 = rubric. So the C-lane splits into **Camp 1 (K03, C16, C12)** and
**Camp 2 (C11-P1, and C07's primary, which independently assumed D13's literal
order — `C07:21-29`)**.

## 3. F2 (major) — item-identity collisions between fragments

Because the camps disagree, two landed fragments disposition content that K03's
canonical table assigns to a **different item number**:

1. **C07's primary row is item 10's content filed as item 7.** `C07:31-103`
   dispositions "calibrated numeric rubric undefined" under `"id": "OI-07"`
   (`C07:83`). Under K03's adopted table the rubric is **OI-10** (`K03:71`) and
   OI-07 is the cold-run set (`K03:68`). Under C16's and C12's orderings the
   rubric is likewise item 10 (`C16:70`, `C12:6-15`). C07's primary row is
   therefore mis-numbered under all three Camp-1 orderings; it is correct only
   under Camp-2 (#4/#5). C07 flagged the dependency (`C07:13-29`, `C07:200-207`)
   and covered three mappings — this is a hedge, not a fabrication — but the
   primary row as written is the wrong row.
2. **C11's primary row is an item K03 excludes from the twelve.**
   `C11:48-104` dispositions "box-4 condition 3b — the r22 ledger-row reading
   discipline" as item 11. `K03:88` explicitly excludes box-4 readings 3a/3b/3c
   from the canonical twelve, quoting `dossier-d11-shonen-boxes.md:176-181`
   ("standing readings, not defects"). C11's P1 ordering (`C11:35-46`) is
   mutually exclusive with K03's table: adopt one, and the other's rows are not
   the twelve.
3. **C12's primary identity is stable only inside Camp 1.** `C12:6-15` puts the
   adapter at item 12, which holds under #1/#2/#3/#5 but **not** under #4, where
   item 12 is box-4 reading 3c. C12 anticipated this and filed the 3c
   disposition as §6 (`C12:179-195`), instructing the integrator to keep exactly
   one. That is the correct handling; it is recorded here so C13/C15 actually
   enforce it.

**Net:** three of the eight landed fragments carry an item identity that is
correct only under a decomposition other than K03's. All three are self-flagged
and offer alternates, so the correct verdict is **"assembly hazard, honestly
disclosed"** — but claim C cannot pass while the ledger mixes the camps.

## 4. F3 (major) — duplicate-id hazard in the C15 assembly path

C15's own schema (`P02:66-73`) requires `id` to be a stable slug, and P02's
validation leg **C-leg-1** asserts `ids unique` (`P02:164`). Two landed
fragments violate uniqueness if concatenated naively:

- `C07` emits **two** rows with `"id": "OI-07"` (`C07:83` and `C07:173` —
  primary rubric row and Contingency-B devin row), plus a third contingency
  (N4) that carries no JSON block.
- `C11` emits **two** rows with `"id": "item-11"` (`C11:239` and `C11:253`),
  and states the rule itself: "**exactly one may enter
  `open-items-ledger.json`**" (`C11:44-46`).

Both fragments name the hazard. The finding is that **nothing in the landed set
mechanically enforces the drop**: C13 (consistency) and C15 (assembly) are the
seats that must do it, and neither had landed at this cut. If C15 concatenates
the `## Ledger row` blocks in file order, C-leg-1 fails on duplicate ids and
C-leg-4 finds contradictory dispositions for one id.

## 5. F4 (moderate) — K03's adopted counting rule is answer-driven, not a rule

`K03:38` states the adopted convention as: "expand only where the dossier itself
enumerates distinct conditions with distinct fixes (box-1 conditions 2/3/4 → 3
rows; lore-owned → 2 rows); keep the cold-run set as the one filed row it is".

Applied uniformly that rule does **not** yield 12. `promotion-review.md:178-195`
enumerates N1, N4, N5 and N7 as four conditions with four distinct, separately
stated fixes (dated errata; a real artifact set/packet path; history-retaining
export wording; a parent pin), and `dossier-d13:134` names those four tokens
exactly as `dossier-d13:133` names box-1's three. The uniform rule therefore
yields 15 (`K03:37`'s own "maximal" figure) — which is why K03 must append an
exception for the cold-run row.

K03 justifies that exception with `dossier-d11:207` ("groups it as one 'open at
HEAD' cell", `K03:38`). That justification does not hold on D11's bytes:
`dossier-d11-shonen-boxes.md:205` groups box-1 identically — one cell reading
"conditions 2, 3, 4 (citation-level; re-confirmed today)" — while
`:207` reads "N1, N4, N5, N7 (as filed)". The two cells have the same
granularity, so D11 does not license expanding one and not the other.

K03 concedes the direction of fit: "This is the only convention that both
includes all 9 D13 rows and lands on the filed '12'" (`K03:42-43`), and flags
the numeral's provenance as `to-verify` with a named contamination path (the
table's own first row, "**12** D4 garment-form holds", `K03:45-53`). **Verdict:
honest but answer-driven.** The count was the target and the rule was fitted to
it — which is precisely why three other seats fitted three other rules to the
same target. The ledger's `count_provenance` (P02:66) must carry K03's
`to-verify` caveat verbatim; the twelve must not be presented downstream as a
measured fact.

## 6. F5 (moderate) — pointer-precision items for C13/C15

1. **The devin pointer is coarse in both K03 and D13.** `dossier-d13:137` points
   at the directory `reports/round-29/recount/`, and `K03:72` follows it
   (`recount/dispositions.md:22`, `recount/audit.md:18`). The canonical record is
   `reports/round-29/devin-availability-disposition.md` (`test -s` exit 0,
   2026-10-19), which is the only artifact that states the disposition class
   ("a documented could-not-evaluate, not a pass"). C07 found this
   (`C07:157-160`); the ledger should carry the canonical path, not the
   directory.
2. **`promotion-review.md:71-88` spans a fifth condition.** D13:133 and
   `K03:65` cite the range for "conditions 2-4", but `:85-88` is condition 5
   (duplicated uncertainty status block), which `dossier-d11:69-75` reads closed
   at HEAD and `K03:84` correctly excludes. The range is not wrong, but a ledger
   row citing `:71-88` for a three-condition item should cite `:71-84`.
3. **K03's OI-01 carries two counts in one row.** `K03:62` bundles "12 D4
   garment-form holds" with "the six owed form slots". C01's re-run shows why
   this is one debt and not two (`C01:96-122`: 12 holds = 6 owed slots × 2
   keyings, `reports/round-18/d4/holds.md:99-102`), so the bundle is right — but
   the row text should say "12 holds over 6 owed slots" to stop a reader
   counting 18.

## 7. F6 (moderate, cross-claim) — claim O rewrites a file C07 pins by line number

`C07:56` and `C07:87` pin the rubric's status-quo evidence at
`corpus/lessons/README.md:163` (the `Q-05-3` row). Claim O's after-requirement is
that the same file gains one index row per lesson file for
`round-26..round-32` (7 rows) and that its prose arithmetic be restated to 33
(`reports/round-33/claims.json`, claim O `after_required.a_lessons`). The index
section is `corpus/lessons/README.md:61-110` and the queue is `:144-233`
(`grep -n "^## "`, 2026-10-19), so an insertion into the index shifts every
queue line **including :163**.

**Consequence:** a ledger row carrying `corpus/lessons/README.md:163` is stale at
validation time if claim O lands. C13/C15 should carry the row id (`Q-05-3`)
plus the section anchor (`§4 Open-question queue`) and re-resolve the line number
after the README delta is applied, or state the pointer as "row `Q-05-3`".
This is the only cross-claim pointer collision this seat found; the other
pointers in the landed fragments resolve into `reports/round-1..32/**`,
`corpus/knowledge/**`, `SKILL.md`, `SCORECARD.md` and `LOG.md`, none of which
claim O rewrites.

## 8. F7 (observation, owner: integrator) — the r5/r7 filed receipts were rewritten and restored during this round

`P02:22-42` records that `reports/round-5/validation.json` and
`reports/round-7/validation.json` were **modified at 2026-10-19
00:54:32/35 (-0300)** — after the round's `declared_at_utc`
(`reports/round-33/claims.json:6`, `03:49:01Z`) — with content diffs (r5:
`O.error` strings and `tested_file_sha256["tools/check-gate-battery.py"]`
`0a126b70…`→`455b595a…`; r7: `inventory:` counts `189/688/700/702/633` →
`201/717/731/733/655`).

**This seat's independent re-measurement at a later cut:** `stat -c '%y %n'`
→ both files mtime `2026-10-19 00:55:27.940762254 -0300`;
`git status --porcelain reports/` → only `?? reports/round-33/`;
`git diff --exit-code reports/round-5/validation.json
reports/round-7/validation.json` → **exit 0**; `git diff --quiet reports/` →
**exit 0**.

So at this cut the filed bytes are **content-identical to HEAD** and the
modification was reversed. This is the r24 condition **N2** firing live in round
33 (`promotion-review.md:180-182`: "the three acceptance scripts rewrite filed
tracked receipts in place; the isolation caveat must cover them (run in a
disposable copy or restore afterwards)"), and the restored state is consistent
with the caveat having been applied. Two consequences for claim C and for the
round:

- **"no filed bytes edited by seats"** (claim C threshold) is verifiable only by
  content comparison, never by mtime. C13/C15 must not read a clean
  `git status` as evidence that no seat ran the acceptance scripts.
- The r5/r7 receipts now carry round-33 mtimes with round-32 content. A future
  mtime-based audit will read this as a violation. Recording it here is the
  durable note; the integrator may want it in the round's admission note.

## 9. Per-fragment verdicts

| fragment | verdict |
|---|---|
| `K03-open-items.md` | **Sound, with one named defect.** All 12 rows re-verified at HEAD by this seat; the count reconciliation is transparent and the numeral is flagged `to-verify`. Defect: F4 — the adopted expansion rule is answer-driven and its stated asymmetry justification does not hold on D11's bytes. Accept the table as the canonical *set*, require the `to-verify` caveat in `count_provenance`. |
| `P02-plan.md` | **Sound and load-bearing.** §1.4 predicted the F1 hazard before the seats landed ("Two arithmetics reach 12, and they are not equivalent", `P02:106`) and chartered R05 against it. §1.5's fix-draft register and the C-leg table give C13/C15 a usable contract. Its C-leg-1 (`ids unique`) and C-leg-3 (`ledger id set == K03's canonical id set`) are exactly the legs F2/F3 break. |
| `C01-item-01.md` | **Strong.** Item 1 is stable under **all five** decompositions (design debts occupy 1-3 in every ordering), so this fragment has no identity risk. Every command re-ran byte-exact (gate exit 0, digest `865bb03e…` == the filed r31 row; `counts.hold = 12`; packet sha match). The `D2L_FORM` symbol reference is correct (`tools/d2-typed-labels.py:422`). Disposition `carried-with-owner+reason+next-touch` is supported by four command-backed blockers (`C01:145-160`). |
| `C07-item-07.md` | **Honest hedge, wrong primary.** F2.1: the primary row files the rubric's content as item 7, which is item 10 under K03/C16/C12. Its Contingency A covers only N4 of K03's four-item OI-07 cluster. All citations verify. Must be re-mapped or re-dispatched; the rubric material should be routed to the item-10 seat and the N4 material merged into OI-07. |
| `C11-item-11.md` | **Honest hedge, camp-exclusive primary.** F2.2: P1 files box-4 reading 3b as item 11, which K03:88 excludes from the twelve; its P2 alternate (devin) agrees with K03/C16/C12. The ordering table at `C11:35-46` is the clearest statement of the count problem any fragment produced. Exactly one of its two rows may enter the ledger. |
| `C12-item-12.md` | **Strong, with a genuinely new finding.** Both item-12 identities are dispositioned (§3 adapter, §6 box-4 3c) with a keep-exactly-one rule. N-C12-1 (`C12:160-177`) is a real, reproducible hazard: the r18 replay control exits **2** (`could-not-evaluate`, `mirror_unsafe`) instead of its declared **1** when `TMPDIR=$PWD/.scratch` is used in-repo, so a validator leg written without an out-of-repo TMPDIR would mis-file the control. Its digests re-verified byte-exact. |
| `C16-receipt.md` | **Sound.** Its decomposition (#2) is a third distinct 12 but a coherent Camp-1 one; its §2 status-quo re-verification matches this seat's on every line checked; §4's "no claim is made that any item is fixed" is the correct posture. Its §3 ledger table correctly marks every disposition `owed`. |
| `C03-item-03.md` | landed at the cut but **not reviewed** (this seat's review budget went to the identity/count layer, which is where the conflicts are). Owed to a re-review. |

## 10. What claim C needs before it can pass (conditions on C13/C15/run-validation)

1. **Adopt exactly one decomposition and say so.** `count_provenance` must name
   the adopted convention, its arithmetic, K03's `to-verify` caveat on the
   numeral, and — if the adopted set is not K03's — a one-to-one mapping note
   from each C-fragment to a ledger id (P02's C-leg-3 wording).
2. **Enforce id uniqueness mechanically.** C-leg-1 must fail on the duplicate
   `OI-07` / `item-11` pairs; the C15 assembler must select one row per id and
   drop the alternates, recording the drop.
3. **Re-map C07's primary and C11's primary** (F2), or re-dispatch those items;
   a ledger containing both C07's rubric row and the item-10 row is a
   contradiction C13 is chartered to catch.
4. **Re-resolve `corpus/lessons/README.md` line pointers after claim O lands**
   (F6), or cite the queue by row id.
5. **Record the r5/r7 receipt rewrite** (F7) as a content-verified restoration,
   not a silent clean tree.
6. **Do not present "12" as measured.** No ledger row, receipt, or SCORECARD
   line may read "12 standing open items" as a fact of the dossier; the dossier
   tables 9 rows and the twelve is a reconstruction (`K03:45-53`,
   `P02:106-114`).

**Language-gate self-check (for A08/X04).** This fragment contains the tokens
`promotion`, `canon` and `closure` only inside artifact names
(`reports/round-24/promotion-review.md`) and in canonicalization vocabulary
("canonical table", "canonical record", "canonicalized 12"). It asserts no
promotion, canon, clearance or closure verdict; the one place it touches the
promotion decision it reports a hazard (`§10.6`, the box-1 citation conditions
are still open at HEAD, so no box may read as cleared by this round's work).

## 11. Addendum — fragments that landed after §1-§10 (same cut, later poll)

Between §9's cut and this addendum, `C02-item-02.md`, `C04-item-04.md`,
`C05-item-05.md`, `C08-item-08.md` and `C14-fix-drafts.md` landed (plus peer
reviews `R05-calib-review.md`, `R06-calib-review.md`). Their identities were
checked against the §2 collision map; the map holds and extends.

**11.1 Updated fragment → candidate-identity table.**

| fragment | row id as filed | identity as filed | stable? |
|---|---|---|---|
| `C01` | `C01-D4-GARMENT-HOLDS` | item 1 = garment holds | stable in all five decompositions |
| `C02` | `OI-02` | item 2 = `head2` empty domain | stable |
| `C03` | (not re-checked here) | item 3 = RL-3 ceiling | stable |
| `C04` | `item-04` | item 4 = **all three** box-1 conditions 2/3/4 as one cluster (`C04:22-28`) | correct under the cluster mapping (Camp 2 / D13 row 4); under K03 it spans OI-04..OI-06 |
| `C05` | `C05-row5-A`, `C05-row5-B` | item 5 = {N1 (schemes A/C), box-1 condition 3 (scheme B)} | **camp-dependent**; C05 filed both |
| `C07` | `OI-07` ×2 | item 7 = {rubric, N4, devin} | rubric row is Camp 2 only (F2.1) |
| `C08` | `OI-08` | item 8 = bilateral same-revision read | K03-consistent |
| `C11` | `item-11` ×2 | item 11 = {box-4 3b, devin} | P1 is Camp 2 (F2.2) |
| `C12` | (prose row) | item 12 = {adapter, box-4 3c} | primary Camp 1, alternate Camp 2 |

**11.2 New duplicate pair — C04 §1.2 and C05 row5-B disposition box-1 condition
3 twice.** `C04:24-28` anticipates exactly this and instructs C13: "treat
§1.1-§1.3 as ONE item's three sub-parts under the cluster mapping; under the
split mapping they are items 4, 5, 6. **Do not disposition them a second time
from another fragment.**" C05 nonetheless files box-1 condition 3 in full as its
scheme-B row (`C05:363-383`, class `carried-with-owner+reason+next-touch`). Both
are self-flagged alternates; the finding is that **three separate duplicate
pairs now exist** (C04↔C05 on condition 3, C07-primary↔item-10 on the rubric,
C11-P1↔K03-excluded-3b), and C13 is the only seat chartered to resolve them.

**11.3 Independent corroboration of F2.1.** `C08:30-35` reaches the same
conclusion this review does, from K03's table: "Under K03's binding item 7 =
OI-07 and item 8 = OI-08, so C07's primary is OI-10's content and C10's item may
be dispositioned twice. C13 must re-bind or record the duplicate." Two seats
found it independently; it is not a reviewer artifact.

**11.4 Independent corroboration of F1 and a fourth enumerating source.**
`R05:1-30` re-derived the count from the dossiers without the fragments and
concludes "the dossier's own enumeration is 9 rows; '12' is inherited, never
derived", adding a fourth source that enumerates the same nine:
`reports/round-32/scribe/fragment-ledger.md:213-216` (re-verified by this seat:
"12 D4 garment holds, empty `head2`, RL-3 ceiling, box-1 conditions 2–4,
cold-run N1/N4/N5/N7, lore-owned bilateral read + L0 contract-digest
ratification, the rubric gap, devin-telemetry could-not-evaluate, D4-adapter
supersession semantics" — nine groups). §2's table stands; R05's finding is
independent evidence for it.

**11.5 F7 refined — the r5/r7 rewrite has an identified actor and a filed
repair.** `R06:238-249` states "This seat triggered it, and restored the filed
bytes", with `git checkout -- reports/round-5/validation.json
reports/round-7/validation.json` and the digests
`reports/round-5/validation.json` `73a66f74…` (HEAD) → `fe926984…` (rewritten) →
`73a66f74…` (restored ✅). Combined with `P02:22-42` (observed the dirty state at
00:54:32/35) and this seat's mtime read (00:55:27, after the restore), the
sequence is one event with two independent observers and a digest-backed repair.
**F7's consequences are unchanged** — the acceptance scripts do rewrite filed
receipts in place (N2 live), and "no filed bytes edited" remains
content-verifiable only — but the event is now fully accounted for and needs no
further investigation, only the admission note.

**11.6 New class hazard — conditional `fixed-with-evidence` rows assert an
unapplied fix.** Claim C's threshold requires that "every 'fixed' row names the
fix draft and its verification". `C04:336-350` files box-1 as
`"disposition_class": "fixed-with-evidence"` while `SKILL.md:486/:488/:501/:128`
are **still stale at HEAD** (re-verified in §1); the row's own `reason` field
carries the escape hatch ("if the drafts are NOT applied in round 33,
re-classify this row carried-with-owner+reason+next-touch"). `C11:253-259` uses
a mixed class ("fixed-with-evidence (process defect…) + carried-…"), and
`C12:119-125` defines a class-transition rule for the same reason. If C13/C15
copy these classes verbatim, the ledger asserts fixes that have not landed, and
the round's "no filed bytes edited by seats" condition will read as satisfied
against a tree whose SKILL.md bytes are demonstrably still stale. **Required:**
either finalize these rows as `carried` with the draft as the next touch, or
finalize the ledger only after the integrator applies the drafts and re-runs the
named controls (`C04`'s §4 control printing GREEN with 0 failing assertions,
exit 0 — measured RED, exit 1, 13 failing assertions pre-application).

**11.7 C14 landed and is structurally sound.** `C14-fix-drafts.md` (456 lines)
carries Fix 1-3 for the three box-1 conditions (`:23`, `:88`, `:151`), Fix 4 for
the cold-run N1 errata (`:284`), and Fix 5 for "conditional extras (**NOT** among
the D13 'three box-1 conditions'; apply only if C01-C12 mark them fixable)"
(`:354`). That Fix-5 scoping is the right boundary discipline — it keeps the
adjacent citation drift C04 §7 named from silently entering the twelve. C14 was
not content-reviewed by this seat; `R06` is chartered to that.

## Owed

- `reports/round-33/calib/C09`, `C10`, `C13`, `C15-ledger-draft.json` — not
  landed at this cut; their item identities must be checked against the adopted
  decomposition (F1/F2/§11.1) when they land.
- `reports/round-33/calib/C13-consistency.md` — the seat chartered to catch
  F2/F3 and the three §11.2 duplicate pairs; this review supplies the collision
  map it must resolve.
- `reports/round-33/calib/C15-ledger-draft.json` — not landed; the duplicate-id,
  camp-mixing and §11.6 conditional-class findings apply directly to it.
- `reports/round-33/calib/C03-item-03.md` — landed, not reviewed here (see §9).
- `reports/round-33/calib/C06-item-06.md` — landed after §11's cut and
  spot-checked only for identity: `C06:19` binds `id` `OI-06` to K03's canonical
  `K03-open-items.md:67` (box-1 condition 4), i.e. **C06 re-bound to K03 rather
  than to a self-derived ordering** — the correct handling and the only landed
  fragment that did so. Its content is not reviewed here.
- `reports/round-33/run-validation.py` — absent at this cut
  (`ls`, exit 2), so claim C's own counting command could not be run by this
  seat; every check in §10 is written to be re-runnable from it.

## Citations

Fragments reviewed: `reports/round-33/calib/K03-open-items.md`,
`P02-plan.md`, `C01-item-01.md`, `C03-item-03.md`, `C07-item-07.md`,
`C11-item-11.md`, `C12-item-12.md`, `C16-receipt.md`.

Round inputs: `reports/round-33/claims.json` (`:6` declared_at_utc, `:8`
baseline, claim C before/after/thresholds), `reports/round-33/targets.json`
(seat R04, shared_rules), `REGIMEN.md`.

Filed sources re-verified: `reports/round-32/dossier-d13-operator-decisions.md:128-138`;
`reports/round-32/dossier-d11-shonen-boxes.md:69-75,176-181,203-208`;
`reports/round-32/final-dossier.md:107-110`;
`reports/round-24/box2-d4.md:104-108`;
`reports/round-24/promotion-review.md:71-88,178-195`;
`reports/round-22/bleed/verification.json:605-609`;
`reports/round-18/d4/holds.md:99-102`;
`reports/round-31/final-sweep.md:62,187-192`;
`reports/round-29/recount/audit.md:18,23`,
`reports/round-29/recount/dispositions.md:22`,
`reports/round-29/devin-availability-disposition.md`;
`reports/round-25..28/availability.json`;
`reports/round-26/register/design.md:228`, `rules.md:89-95`,
`open-questions/C42.md:43-60`, `zzz-lessons-index-revision-4.md:229`;
`reports/round-5/kotodama.md:54`;
`reports/round-15/handoff/contract-v2-audit.md:31,48`;
`reports/round-8/adjacency.md:144-150`;
`corpus/knowledge/linguistics/register-lexicon-ceilings.md:6,19`;
`corpus/knowledge/synthesis/worldbible-integration-contract.md:7,15,16,155,182`;
`corpus/QUALITY.md`; `corpus/lessons/README.md:61-110,144-233` (`:75`, `:163`);
`SCORECARD.md:13-14,443-445,624`; `LOG.md:3045,3312,3513`;
`SKILL.md:128,486,488,491,501,531-534,607`;
`tools/d2-typed-labels.py:422`;
`examples/culture-d4/expected-holds.json`, `examples/culture-d4/packet.d4.yml`;
`tools/gates/frozen/round-18/{MANIFEST.tsv,freeze-receipt.json,README.md:56-62}`;
`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45` (out-of-repo,
read-only).

Commands run by this seat, 2026-10-19, at `139e3b6` (all quoted inline):
`git rev-parse HEAD`; `git status --porcelain reports/`; `git diff --exit-code
reports/round-5/validation.json reports/round-7/validation.json` (exit 0);
`git diff --quiet reports/` (exit 0); `git ls-files | wc -l` (=2655);
`sed -n '130,138p' reports/round-32/dossier-d13-operator-decisions.md | grep -c '^|'` (=9);
`grep -c "^| OI-" reports/round-33/calib/K03-open-items.md` (=12);
`python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
(exit 0, stdout sha256 `865bb03e…`, 12 `D2L-FORM-UNRESOLVED`, 20/20 legs);
`python3` JSON reads of `examples/culture-d4/expected-holds.json` and
`reports/round-25..28/availability.json`; `sha256sum` over
`examples/culture-d4/packet.d4.yml` and the two r18 frozen inputs;
`grep -n "rubric" SCORECARD.md` (=`14,624`); `grep -n "rubric" corpus/QUALITY.md`
(exit 1); `grep -rn "rubric" reports/round-2[7-9]/ reports/round-3[0-1]/ | wc -l` (=0);
`grep -c` for the five dangling anchor tokens in `tools/d2-typed-labels.py` (=0);
`stat -c '%y %n' reports/round-5/validation.json reports/round-7/validation.json`;
`grep -n "^## " corpus/lessons/README.md`;
`sed -n '44,45p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`;
`grep -c "^kotodama" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` (=4).
