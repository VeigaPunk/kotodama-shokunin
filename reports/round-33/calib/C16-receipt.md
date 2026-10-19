- Seat: C16 | executor | claim C (calibration) | date 2026-10-19 | baseline 139e3b6

# C16 — calibration receipt draft (claim C: the twelve standing open items)

Role: draft the calibration receipt for claim C — the before→after narrative, the
ledger summary table, and the honest naming of everything carried (with why).
Non-author declaration: this seat authored none of the artifacts it cites.
Write scope: this file only; no git commit/push, no installs, no network, no
filed-round bytes touched (`reports/round-1..32/**`, `corpus/lessons/*.md`,
`tools/gates/frozen/**`, fleet `.ufo/**` read-only). Observation cut for every
live check below: **2026-10-19T03:54Z**, lane HEAD
`139e3b662900557afe54f632b468619593dc9fcb` (= the declared baseline;
`git rev-parse HEAD`, run this seat, 2026-10-19).

This receipt claims no admission, no promotion, no canon, no closure. It is a
draft written while the claim-C sibling seats were still running; every
disposition column it cannot fill from disk is marked `owed` with the exact
path, per the missing-dependency rule.

## 1. Before → after narrative (claim C)

**Before (at declaration, `reports/round-33/claims.json` claim C).** The round-32
close routed exactly one calibration debt: *"12 standing open items in the
dossier"* — `SCORECARD.md:443-444` ("Routed debt recorded for the operator: the
falsifier audit's filename mismatch (substance 5/5), 7 unindexed lessons, 12
standing open items in the dossier, the promotion + freshness decisions"),
restated in `LOG.md:3513` as a standing input to round 33. No ledger artifact
existed: the only durable enumeration at HEAD was prose — the dossier Decision 4
table (`reports/round-32/dossier-d13-operator-decisions.md:128-138`, nine debt
rows) plus the open conditions in `reports/round-32/dossier-d11-shonen-boxes.md`
(box-1 conditions 2-4 at `:78-79`, box-3 N1/N4/N5/N7 at `:145-152`, summary
table `:203-208`). At this seat's cut `reports/round-33/calib/` was **empty**
(`ls`, 2026-10-19T03:51Z) and `reports/round-33/run-validation.py` did **not
exist** (`ls` exit 2, 2026-10-19T03:51Z) — i.e. the claim's own counting command
was not yet on disk when this receipt was drafted.

**After (what claim C requires).** `reports/round-33/calib/open-items-ledger.json`
(C15) with rows == K03's canonicalized 12, cross-checked against SCORECARD's
"12"; every row dispositioned `fixed-with-evidence` or
`carried-with-owner+reason+next-touch`; C13 consistency receipt green; bounded
fix drafts at `reports/round-33/calib/C14-fix-drafts.md` for integrator
application; `python3 reports/round-33/run-validation.py` exits 0.

**After-state at this seat's cut:** the after-artifacts above were not on disk;
this receipt therefore records (a) the candidate canonical decomposition and its
arithmetic, (b) this seat's own HEAD re-verification of every status-quo pointer,
and (c) the carried-why for each item — and marks all per-row *disposition*
cells owed to the sibling seats. Nothing here should be read as a disposition.

## 2. Candidate canonical decomposition (12) — provisional, K03 owns the canonical list

Derivation from the two declared sources, with the arithmetic that lands on 12:
d13's nine rows (`dossier-d13-operator-decisions.md:130-138`), expanding its
bundled row *box-1 citation conditions 2-4* into its three named conditions
(`promotion-review.md:71-84`; d11 `:78-79` names exactly "three citation-level
conditions (2-4)") = +2, and its bundled *cold-run N1/N4/N5/N7* into N1 and
N4/N5/N7 = +1. 9 + 2 + 1 = **12**.

| id | item | on record since | status-quo pointer, re-verified at HEAD 139e3b6 | disposition | why carried / owed |
|---|---|---|---|---|---|
| C-01 | 12 D4 garment-form holds + owed slots (design debt by design) | r18 | `reports/round-24/box2-d4.md:104-108` — read: "**F3 (note): 12 open GAR form holds remain design findings** … (six owed garment forms) … do not fail the gate" | owed: `calib/C01-item-01.md` | carried by design at r24 (d13:130); clearing it is a design change, not a fix — integrator/operator surface |
| C-02 | `head2` empty proper domain (RL-2) | r26 | `reports/round-26/register/design.md:228` — "`head2` has an **empty proper domain**: 59 of 62 delivered forms are ≤2 syllables, so `head2(form) == form` is an identity, not a derivation" | owed: `calib/C02-item-02.md` | design finding; the operation is declared and enforced, the domain is thin |
| C-03 | RL-3 register-lexicon ceiling (constraint, not defect) | r27/r28 | `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` (KTD-RLC-S-0001, cited by revision) and `:19` (measured 27 plain / legal 19 / illegal 8, selftest 10/10) | owed: `calib/C03-item-03.md` | d13:132 names it a constraint; no defect to fix, disposition should be carried-with-owner |
| C-04 | box-1 condition 2 — loanword-dating cite cluster | r24 | `reports/round-24/promotion-review.md:71-76`; live bytes at HEAD: `SKILL.md:486` still cites `loanword-material-dating.md:26,60` and `SKILL.md:488` still cites `:57` (both named doubly-wrong by r24) | owed: `calib/C04-item-04.md`; fix draft expected at `calib/C14-fix-drafts.md` | pointer-level, fixable; SKILL.md is integrator-applied (seats never edit shared files) |
| C-05 | box-1 condition 3 — `worldbible-integration-contract.md:183` mis-cite | r24 | `reports/round-24/promotion-review.md:77-80`; live bytes at HEAD: `SKILL.md:501` still carries the `:183` pointer (also `SKILL.md:128` per claims.json) | owed: `calib/C05-item-05.md` | pointer-level, fixable; needs re-point or dated erratum |
| C-06 | box-1 condition 4 — dangling tool anchors | r24 | `reports/round-24/promotion-review.md:81-84`; this seat's re-measure at HEAD: `grep -rl` for `TL-01`, `TL-02`, `FIELD_DEFAULTS`, `fictional-coordinate`, `descriptive-gloss` over `tools/` → **0 files each**; `grep -c` in `tools/d2-typed-labels.py` → 0 | owed: `calib/C06-item-06.md` | anchors absent, described behaviors real — errata-or-repoint class |
| C-07 | cold-run N1 — no expected-verdict errata for the r5/6/7 acceptance re-runs | r24 | `reports/round-24/promotion-review.md:176-178`; re-confirmed `dossier-d11-shonen-boxes.md:145-149` ("NOT closed by text", checked `SKILL.md:695-712`, 2026-10-18) | owed: `calib/C07-item-07.md`; errata draft expected at `calib/C14-fix-drafts.md` | text-level, fixable; the re-runs exit 1 for distinct explainable causes |
| C-08 | cold-run N4 / N5 / N7 | r24 | `reports/round-24/promotion-review.md:184-196` (N4 real artifact set/packet path; N5 history-retaining export; N7 parent pin of the checklist reading); re-confirmed `dossier-d11-shonen-boxes.md:150-152` ("remain as filed") | owed: `calib/C08-item-08.md` | partly process-owned (N7's pin was never issued as a durable artifact) — likely carried-with-owner |
| C-09 | lore-owned: bilateral read + L0 contract-digest ratification | r8/r15 | fleet queue `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44` (r2: §1 same-revision read record per lane) and `:45` (r8: contract digest drift vs lore's open r93 ratification); digest caveat `reports/round-8/adjacency.md:144-150` | owed: `calib/C09-item-09.md` | **not this lane's to fix** — contested scope, routed-not-absorbed (AGENTS.md); disposition must be carried-with-owner=lore |
| C-10 | calibrated numeric rubric undefined | r5 | `SCORECARD.md:14` ("defining a calibrated numeric rubric remains an explicit protocol-conformance gap"); restated `:624` | owed: `calib/C10-item-10.md` | protocol gap; the scorecard's own answer is verdicts-not-scalars — carried pending operator |
| C-11 | devin availability `could-not-evaluate` | r29 | `reports/round-29/recount/audit.md:18,23` ("all four availability records leave `launched_workers` and `completed_workers` null … the 64-worker value is therefore unverified"); restated `reports/round-29/recount/dispositions.md:22` | owed: `calib/C11-item-11.md` | historical telemetry cannot be reconstructed (AGENTS.md: never reconstruct historical samples) — carried permanently with reason |
| C-12 | r18 D4-adapter baseline supersession semantics (pins green, content ages) | r31 | `reports/round-31/final-sweep.md:187-190` (§5: "The D4 adapter baselines were not re-pinned … a successor baseline is the re-pin seat's surface if the round wants one") | owed: `calib/C12-item-12.md` | re-pin decision, not a defect; green pins are integrity, not truth (same §5) |

**Excluded, recorded for the cross-check:** box-1 condition 5 (duplicated
uncertainty status block, `promotion-review.md:85-88`) is **not** in the
canonical 12 — d11's net names only conditions 2-4 as open
(`dossier-d11-shonen-boxes.md:78-79`, `:205`). If K03's canonical list includes
it, the count is 13 and the SCORECARD "12" needs a named finding, not a silent
rescale. `to-verify` against `calib/K03-open-items.md`.

## 3. Ledger summary table (as required by claim C — status at this seat's cut)

| ledger field | required by claim C | state at 2026-10-19T03:54Z |
|---|---|---|
| row count | == 12, cross-checked against SCORECARD's "12" | candidate 12 above; canonical count **owed**: `calib/K03-open-items.md`, `calib/C15-ledger-draft.json` |
| per-row status-quo pointer re-verified at HEAD | yes | **done for all 12** (column 4 above; commands in §5) |
| disposition class ∈ {fixed-with-evidence, carried-with-owner+reason+next-touch} | every row | **owed**: `calib/C01-item-01.md` … `calib/C12-item-12.md`; no seat had landed a disposition at this cut |
| consistency check (no duplicate/contradictory dispositions) | green | **owed**: `calib/C13-consistency.md` |
| bounded fix drafts for in-scope fixable items | at `calib/C14-fix-drafts.md` | **owed**: `calib/C14-fix-drafts.md` (this receipt's own reading: C-04, C-05, C-06, C-07 are the pointer/text-level fixable class; C-01..C-03, C-08..C-12 are structural/owned) |
| counting command | `python3 reports/round-33/run-validation.py` | **absent at cut** (`ls` exit 2) — cannot be run or cited by this seat |

## 4. Honest naming of what is carried, and why

1. **All twelve dispositions are carried at this cut**, with reason: the
   claim-C sibling seats (K03, C01-C15) had not written their fragments when
   this receipt was drafted (`reports/round-33/calib/` empty, `ls`,
   2026-10-19T03:51Z). Per the missing-dependency rule this seat does the part it
   can — the decomposition and the pointer re-verification — and names the owed
   paths rather than inventing dispositions.
2. **Structurally carried (not fixable by a bounded draft), with owner class:**
   C-01 (design debt by design, d13:130), C-03 (constraint, not defect,
   d13:132), C-09 (lore-owned, contested scope — routed not absorbed,
   `l0-questions.md:44-45`), C-11 (historical telemetry cannot be reconstructed
   per AGENTS.md — `could-not-evaluate` stands), C-12 (re-pin decision,
   `final-sweep.md:187-190`).
3. **Fixable class, pending C14 drafts:** C-04, C-05, C-06 (citation-level,
   SKILL.md bytes confirmed still stale at HEAD) and C-07 (errata text).
   N4/N5 (C-08) are text-level but touch the cold-run file set; N7 is a parent
   pin — partial.
4. **No claim is made that any item is fixed.** The words fixed/closed appear in
   this receipt only inside quotations of prior rounds' verdicts.

## 5. Commands run by this seat (2026-10-19, all read-only)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD                      # 139e3b662900557afe54f632b468619593dc9fcb
git ls-files | wc -l                    # 2655
ls reports/round-33/calib/              # empty (2026-10-19T03:51Z)
ls reports/round-33/run-validation.py   # exit 2: No such file or directory
sed -n '104,108p' reports/round-24/box2-d4.md            # C-01 F3 note read
sed -n '71,88p;174,198p' reports/round-24/promotion-review.md  # C-04..C-08 conditions read
sed -n '486p;488p;501p' SKILL.md        # C-04/C-05 stale cites still live
for a in TL-01 TL-02 FIELD_DEFAULTS fictional-coordinate descriptive-gloss; do grep -rl "$a" tools/; done   # 0 files each (C-06)
grep -c 'TL-01\|TL-02\|FIELD_DEFAULTS' tools/d2-typed-labels.py   # 0
sed -n '44,50p;140,152p;190,208p' reports/round-32/dossier-d11-shonen-boxes.md
sed -n '123,138p' reports/round-32/dossier-d13-operator-decisions.md
grep -n 'rubric' SCORECARD.md           # :14, :624
grep -n 'could-not-evaluate\|launched_workers' reports/round-29/recount/audit.md  # :18, :23
grep -n 'bilateral\|contract-digest' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md  # :44, :45
sed -n '183,196p' reports/round-31/final-sweep.md   # C-12 §5 read
```

## 6. Limits

- Read-time draft, not an atomic final tree: the round-33 wave was still writing
  when this receipt was cut; re-measure before integration instead of inheriting
  these readings.
- The candidate 12 is this seat's derivation, offered for cross-check only; K03
  owns canonicalization and C13 owns consistency. Divergence is a named finding.
- No disposition, no admission, no axis verdict, no promotion/canon/closure
  language is claimed here.

## Owed

- `reports/round-33/calib/K03-open-items.md` — canonical 12 (ids, origins, pointers); receipt's row ids and count cross-check against it
- `reports/round-33/calib/C01-item-01.md` … `calib/C12-item-12.md` — per-item dispositions (12 files)
- `reports/round-33/calib/C13-consistency.md` — duplicate/contradiction check over the 12 dispositions
- `reports/round-33/calib/C14-fix-drafts.md` — bounded fix drafts (expected: C-04, C-05, C-06, C-07)
- `reports/round-33/calib/C15-ledger-draft.json` — the ledger itself (row count 12, required fields, valid classes)
- `reports/round-33/run-validation.py` — the claim's counting command; absent at this seat's cut

## Citations

- `reports/round-33/claims.json` — claim C, before/after_required, counting commands, thresholds
- `reports/round-33/targets.json` — seat C16 mission and out path; shared_rules
- `SCORECARD.md:14`, `:443-444`, `:624`
- `LOG.md:3513`
- `reports/round-32/dossier-d13-operator-decisions.md:123-138`
- `reports/round-32/dossier-d11-shonen-boxes.md:44-49`, `:78-79`, `:145-152`, `:190-198`, `:203-208`
- `reports/round-24/box2-d4.md:104-108`
- `reports/round-24/promotion-review.md:71-88`, `:174-198`
- `SKILL.md:486`, `:488`, `:501`, `:128`
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6`, `:19`
- `reports/round-26/register/design.md:228`
- `reports/round-29/recount/audit.md:18`, `:23`; `reports/round-29/recount/dispositions.md:22`
- `reports/round-31/final-sweep.md:187-190`
- `reports/round-8/adjacency.md:144-150`
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44-45` (read-only, out of repo)
- Commands: `git rev-parse HEAD`; `git ls-files | wc -l`; `ls reports/round-33/{calib,run-validation.py}`; the `grep`/`sed` set in §5 — all 2026-10-19, output quoted inline
