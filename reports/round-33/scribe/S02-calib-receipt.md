- Seat: S02 | scribe | claim C | date 2026-10-19 | baseline 139e3b6

# S02 — final calibration receipt (claim C), with the ledger summary and the honest carried-list

Role: final claim-C receipt post-review — fold the sibling fragments into one
command-carried receipt, summarize the ledger, and name honestly what is
carried. Non-author declaration: this seat authored none of the artifacts it
cites. Write scope: this file only; no git commit/push, no installs, no
network, no filed-round bytes touched (`reports/round-1..32/**`,
`corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**` read-only).
Observation cut: **2026-10-19T03:57Z**, lane HEAD
`139e3b662900557afe54f632b468619593dc9fcb` (= the declared baseline,
`git rev-parse HEAD`, run this seat). This receipt claims no admission, no
promotion, no canon, no closure; it is an engineering record of what is on
disk at its cut.

## 1. Dependency ledger at this seat's cut

Landed and folded in (digests are of the bytes read, `sha256sum`, 2026-10-19):

| fragment | digest (first 16) | what it contributes |
|---|---|---|
| `calib/K03-open-items.md` | `fe0b11cc869f96e6` | the canonical 12 (ids OI-01..OI-12, class vocabulary, pointer re-verification, counting-convention record) |
| `calib/C01-item-01.md` | `7bcaba29b45a6e03` | OI-01 disposition: carried, with owner/reason/next-touch; 12 holds re-emitted at HEAD (exit 0, stdout sha `865bb03e…`) |
| `calib/C07-item-07.md` | `48169a6c292fb60a` | item-7 dispositions under three orderings (see F-S02-2) |
| `calib/C16-receipt.md` | `fd96f9548de99e98` | pre-review receipt draft: before→after narrative, candidate decomposition, pointer re-verification for all 12 |
| `calib/P02-plan.md` | (landed 03:56Z) | C/A execution plans and ledger schema |
| `calib/C12-item-12.md` | (landed 03:56Z) | OI-12 disposition |
| `op/O07-baseline-receipt.md` | `d2cb6b554d39a8ac` | the round-33 regression baseline (battery 44/44, craft 10/10+18/18, d4 81/81, c31 28/28) and its own post-capture observation of the filed-bytes mutation |

Absent at this cut (per the missing-dependency rule, named not invented):
`calib/C02..C06`, `calib/C08..C11`, `calib/C13-consistency.md`,
`calib/C14-fix-drafts.md`, `calib/C15-ledger-draft.json`, all of
`review/R04-R06`, and `reports/round-33/run-validation.py` (`ls` exit 2). The
review fold-in this seat's mission names therefore could not be performed —
see §6.

## 2. Claim C, before → after (as the tree stands at my cut)

**Before** (filed, unchanged): `SCORECARD.md:444-445` — "Routed debt recorded
for the operator: … **12 standing open items in the dossier**"; `LOG.md:3513`
carries the same numeral as round 33's starting queue; no ledger artifact
existed (`reports/round-33/calib/` was empty until 03:55Z).

**After-required** (`reports/round-33/claims.json` claim C):
`open-items-ledger.json` rows == the canonical 12, every row dispositioned
into `{fixed-with-evidence, carried-with-owner+reason+next-touch}`, C13
consistency green, bounded fix drafts at `calib/C14-fix-drafts.md`, and
`python3 reports/round-33/run-validation.py` exiting 0.

**Measured at my cut:** the canonical 12 exists (K03) and their pointers are
re-verified at HEAD (§3), but the ledger file, the consistency receipt, the
fix drafts and the counting command are **not on disk**. Claim C is therefore
**not verifiable at this cut** — the honest state is "input canonicalized,
dispositions partially landed, verification surface absent". No verdict is
claimed here.

## 3. Ledger summary — the canonical 12 with HEAD re-verification

Ids, items and classes are K03's (`calib/K03-open-items.md:62-73`, which owns
canonicalization per `targets.json`). The **status-quo column is this seat's
own re-measurement** at HEAD `139e3b6`, 2026-10-19, independent of K03's and
C16's (different commands, quoted inline).

| id | item (K03) | class | status quo re-verified by this seat | disposition status |
|---|---|---|---|---|
| OI-01 | 12 D4 garment-form holds + six owed slots | design-debt | `sed -n '104,108p' reports/round-24/box2-d4.md` → "**F3 (note): 12 open GAR form holds remain design findings** … six owed garment forms … do not fail the gate"; C01 re-emitted them at HEAD (exit 0) | **carried** (C01: owner operator, next-touch named) |
| OI-02 | `head2` empty proper domain (RL-2) | design-debt | `grep -n head2 reports/round-26/register/design.md` → `:228` "`head2` has an **empty proper domain**: 59 of 62 … identity, not a derivation" | owed: `calib/C02-item-02.md` |
| OI-03 | RL-3 register-lexicon ceiling (constraint) | design-debt | `grep -n 'RL-3\|ceiling' corpus/knowledge/linguistics/register-lexicon-ceilings.md` → `:6` KTD-RLC-S-0001 cites r27 §3.2/RL-3; `:19` measured 27/19/8, selftest 10/10 | owed: `calib/C03-item-03.md` |
| OI-04 | box-1 condition 2 — loanword-dating cite cluster | citation-condition | `sed -n '486p;488p' SKILL.md` → `:486` cites `loanword-material-dating.md:26,60`, `:488` cites `:57` — both still live; file last commit `e1694ba` (`git log -1 -- corpus/knowledge/synthesis/loanword-material-dating.md`) | owed: `calib/C04-item-04.md` |
| OI-05 | box-1 condition 3 — contract `:183` mis-cite | citation-condition | `sed -n '501p;128p' SKILL.md` → both still carry `worldbible-integration-contract.md:183`; `sed -n '183p'` → "Every delivered record has scope, stable identity…" (not the boilerplate rule); contract last commit `e1694ba` | owed: `calib/C05-item-05.md` |
| OI-06 | box-1 condition 4 — dangling tool anchors | citation-condition | `grep -c` in `tools/d2-typed-labels.py` for `TL-01`, `TL-02`, `FIELD_DEFAULTS`, `fictional-coordinate`, `descriptive-gloss` → **0 each** | owed: `calib/C06-item-06.md` |
| OI-07 | cold-run set N1/N4/N5/N7 | cold-run-condition | `sed -n '176,196p' reports/round-24/promotion-review.md` → N1 `:178`, N4 `:186`, N5 `:189`, N7 `:193`; D11 re-confirms N1 "NOT closed by text" (`dossier-d11-shonen-boxes.md:145-149`) | **contested** — C07 dispositioned the rubric under this id; see F-S02-2 |
| OI-08 | lore-owned — bilateral same-revision read outstanding | lore-owned-routing | `grep -n kotodama /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → `:44` (kotodama \| round-2) — read-only, out of repo | owed: `calib/C08/C09` |
| OI-09 | lore-owned — L0 contract-digest ratification | lore-owned-routing | same command → `:45` (kotodama \| round-8, evidence `reports/round-8/adjacency.md`) | owed: `calib/C08/C09` |
| OI-10 | calibrated numeric rubric undefined | protocol-gap | `sed -n '1,30p' SCORECARD.md` → `:13-14` "defining a calibrated numeric rubric remains an explicit protocol-conformance gap" | owed: `calib/C10-item-10.md`; C07 has a matching carried row (mis-keyed to OI-07) |
| OI-11 | devin availability `could-not-evaluate` | telemetry-gap | `sed -n '18p;23p' reports/round-29/recount/audit.md` → "All four availability records leave `launched_workers` and `completed_workers` null"; `test -s reports/round-29/devin-availability-disposition.md` → exists, sha256 `c659ce4260abfd58…` | owed: `calib/C11-item-11.md` |
| OI-12 | r18 D4-adapter baseline supersession semantics | baseline-semantics | `sed -n '183,196p' reports/round-31/final-sweep.md` → §5 "The D4 adapter baselines were not re-pinned … a successor baseline is the re-pin seat's surface" | landed: `calib/C12-item-12.md` (read at 03:56Z, not folded in detail here) |

One row (OI-01) has a filed disposition; OI-07 is contested; the remaining ten
are owed to their seats. **No item is claimed fixed by this receipt.**

## 4. Count provenance (reconciled, with the divergence named)

Three filed statements carry the numeral: `SCORECARD.md:444-445`,
`LOG.md:3513`, `reports/round-32/final-dossier.md:107-110` ("**Twelve named
items**"). The source table has **9 data rows** — this seat's independent
command: `sed -n '130,138p' reports/round-32/dossier-d13-operator-decisions.md
| grep -c '^|'` → `9`. K03 measured the same 9 and adopted the only convention
that includes all 9 rows and lands on 12: 3 design debts + 3 box-1 citation
conditions + 1 cold-run cluster + 2 lore-owned + 1 rubric + 1 devin + 1 adapter
= 12 (`calib/K03-open-items.md:32-43`). The expansion rule itself is
`to-verify` against the original author's intent (K03 §4, honest caveat
adopted here); the numeral-12 contamination path (the table's own first row,
"12 D4 garment-form holds", `dossier-d13:130`) is named, not absorbed.

## 5. Independent checks run by this seat (cross-check value)

| check | command | result at HEAD 139e3b6 |
|---|---|---|
| battery selftest | `python3 tools/check-gate-battery.py --selftest` | exit 0, `SELFTEST OK 44/44 controls behaved as expected` — agrees with `op/O07-baseline-receipt.md` §2 row 1 |
| c31 selftest | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | exit 0, `SELFTEST OK: 28/28 checks passed` — agrees with O07 row 4 |
| c31 live (claim-O before-state) | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | 33 files / 26 rows; `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`; findings 2 — the declared before-state, unchanged |
| SKILL digest | `sha256sum SKILL.md` | `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d` — equals the digest d11/r32-scribe pin (`dossier-d11-shonen-boxes.md:49-51`) |
| box-1 condition 5 census | `grep -c "supported / partial / unresolved" SKILL.md` | `1` — condition 5 reads closed at HEAD, consistent with its exclusion from the 12 (`calib/K03-open-items.md:84`) |

## 6. Named findings

**F-S02-1 — filed round bytes rewritten in place (live instance of cold-run
condition N2; needs an integrator decision before commit).** At 03:54:04Z and
03:54:07Z UTC, `reports/round-5/validation.json` and
`reports/round-7/validation.json` changed on disk (`stat -c '%y %n'`; `git
status --porcelain` → ` M` on both). Cause, visible in the diffs and in the
scripts: the historical validators write their own receipt —
`reports/round-5/run-validation.py:194` and `reports/round-7/run-validation.py:1171`
both do `(HERE / "validation.json").write_text(...)` — so any seat that
verifies cold-run condition N1 by re-running them mutates filed bytes. Round
5's diff moves its `O`-leg error from the battery baseline-coverage failure to
a `tools/replay-frozen.py … MANIFEST.tsv` `gate_digest_mismatch`
could-not-evaluate (7/7 rows); round 7's `tested_file_sha256` for
`tools/check-gate-battery.py` moves `0a126b70…` → `455b595a…` (the current
digest). Not this seat's: the commands in my mission and in §5 touch no
acceptance script (`grep -n "run-validation\|acceptance" tools/check-gate-battery.py`
→ no hits). `op/O07-baseline-receipt.md:147-181` observed the same two files
independently at 03:54:59Z with byte digests; attribution to the specific seat
stays **to-verify** (the plausible class is a claim-C seat checking N1). Owner:
integrator — the filed bytes are recoverable with
`git checkout -- reports/round-5/validation.json reports/round-7/validation.json`
before the round-33 commit; this seat did not repair them.

**F-S02-2 — the two 12-decompositions disagree on the row split, and C07's
item-7 mapping follows the superseded one.** K03's canonical partition
(box-1 → 3 rows, cold-run → **1** row, lore → 2 rows) and C16's candidate
partition (box-1 → 3, cold-run → **2**, lore → 1,
`calib/C16-receipt.md:50-57`) both total 12 and both cover the same 9 D13 rows,
but they cut the rows differently. K03 owns canonicalization
(`targets.json` K03 seat), and it fixes the C-lane mapping explicitly:
"C01↔OI-01 … C12↔OI-12 in this order" (`calib/K03-open-items.md:75-78`) — under
which **OI-07 = the cold-run set N1/N4/N5/N7** and the rubric is **OI-10**.
C07's fragment (written before K03 landed) takes the rubric as its *primary*
item 7 with two contingencies (`calib/C07-item-07.md:24-29`). Consequence for
C13/C15: the rubric row must be re-keyed to OI-10, OI-07 must consume the
cold-run set (N1 errata + N4/N5/N7), and C16's C-08 row (N4/N5/N7) has no
counterpart row in the canonical partition — it merges into OI-07. This is a
row-identity divergence, not a count divergence; it is fixable by the
integrator without touching any disposition's substance.

**F-S02-3 — D13's devin pointer is loose (adopted from C07, re-verified).**
`dossier-d13-operator-decisions.md:137` points at `reports/round-29/recount/`,
which holds the census (`recount/audit.md:18`, re-read by this seat) but not
the disposition record; the canonical artifact is
`reports/round-29/devin-availability-disposition.md`
(`test -s` exit 0, sha256 `c659ce4260abfd58…`). Ledger rows should carry the
precise path.

## 7. Honest carried-list

Carried because the round cannot close them (each with the reason class; the
per-row owner/reason/next-touch cells remain the C-lane seats' to file):

1. **All ten undispositioned rows** (OI-02..OI-06, OI-08..OI-11, and OI-07 in
   its canonical identity) are carried at this cut with reason: their
   disposition fragments had not landed when this receipt was written.
2. **Structurally carried, not fixable by a bounded draft:** OI-01 (design
   debt by design; C01 filed: owner operator, six D4 forms would have to be
   authored — content work outside round-33 non-goals), OI-03 (constraint, not
   defect), OI-08/OI-09 (lore-owned, contested scope — routed not absorbed,
   `l0-questions.md:44-45`), OI-11 (wave-time samples unrecoverable; AGENTS.md
   bars reconstruction), OI-12 (a re-pin decision, not a defect).
3. **Fixable class awaiting C14:** OI-04, OI-05, OI-06 (citation-level,
   SKILL.md bytes confirmed still stale at HEAD by my own `sed`/`grep` in §3)
   and OI-07's N1 errata. N4/N5 are text-level but touch the cold-run file
   set; N7 is a parent pin — partial.
4. **Verification surface absent:** `reports/round-33/run-validation.py` did
   not exist at my cut, so no claim-C leg could be executed or cited.
5. **Review fold-in owed:** `review/R04-R06` were empty at my cut, so this
   receipt could not fold adversarial findings; any R04-R06 defect that lands
   later must be applied as a dated erratum on top of this file, not by
   rewriting it.

## 8. Limits

Read-time draft of a live wave: sibling fragments kept landing while this
receipt was written (C01/C12/P02 arrived at 03:56Z), so re-measure before
integration rather than inheriting these readings. This seat re-graded nothing
it did not measure; K03's and C16's tables are quoted as merged. No
disposition, admission, axis verdict, promotion or closure language is claimed.

## Owed

- `reports/round-33/calib/C02-item-02.md` … `calib/C11-item-11.md` (ten files,
  minus the landed C01/C07/C12) — per-item dispositions with owner/reason/
  next-touch; OI-07's disposition must use the canonical cold-run identity
  (F-S02-2)
- `reports/round-33/calib/C13-consistency.md` — must resolve the C16-vs-K03
  row-partition divergence (F-S02-2) and the C07 item-7 re-key
- `reports/round-33/calib/C14-fix-drafts.md` — bounded drafts for OI-04/05/06
  and OI-07's N1 errata
- `reports/round-33/calib/C15-ledger-draft.json` — 12 rows under K03's ids
- `reports/round-33/review/R04-calib-review.md`, `R05-calib-review.md`,
  `R06-calib-review.md` — the adversarial pass this receipt's mission folds in
- `reports/round-33/run-validation.py` — the claim's counting command
- integrator: restore `reports/round-5/validation.json` and
  `reports/round-7/validation.json` from HEAD before committing (F-S02-1)

## Citations

- `reports/round-33/targets.json` (S02 seat object; shared_rules);
  `reports/round-33/claims.json:40-50` (claim C before/after, counting
  commands, thresholds), `:8` (baseline commit)
- `SCORECARD.md:13-14`, `:444-445`; `LOG.md:3513`
- `reports/round-32/dossier-d13-operator-decisions.md:123-138`;
  `reports/round-32/dossier-d11-shonen-boxes.md:49-51`, `:145-153`;
  `reports/round-32/final-dossier.md:107-110`;
  `reports/round-32/scribe/fragment-ledger.md:212-216`
- `reports/round-24/box2-d4.md:104-108`; `reports/round-24/promotion-review.md:71-88`, `:176-196`
- `reports/round-26/register/design.md:228`
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6`, `:19`
- `SKILL.md:128`, `:486`, `:488`, `:501`; `tools/d2-typed-labels.py` (grep, 0 hits)
- `reports/round-31/final-sweep.md:183-196`
- `reports/round-29/recount/audit.md:18`, `:23`;
  `reports/round-29/devin-availability-disposition.md` (sha256 `c659ce4260abfd58…`)
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44-45` (read-only, out of repo)
- `reports/round-33/calib/K03-open-items.md` (`fe0b11cc869f96e6…`),
  `calib/C01-item-01.md` (`7bcaba29b45a6e03…`), `calib/C07-item-07.md`
  (`48169a6c292fb60a…`), `calib/C16-receipt.md` (`fd96f9548de99e98…`),
  `calib/C12-item-12.md`, `calib/P02-plan.md` (landed 03:56Z);
  `op/O07-baseline-receipt.md` (`d2cb6b554d39a8ac…`)
- commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`; `git status --porcelain`;
  `stat -c '%y %n' reports/round-5/validation.json reports/round-7/validation.json LOG.md`;
  `git diff reports/round-5/validation.json reports/round-7/validation.json`;
  `grep -n "run-validation\|acceptance" tools/check-gate-battery.py`;
  `grep -n "validation.json\|write_text" reports/round-5/run-validation.py reports/round-7/run-validation.py`;
  `sed -n '130,138p' reports/round-32/dossier-d13-operator-decisions.md | grep -c '^|'`;
  `sed -n '104,108p' reports/round-24/box2-d4.md`; `sed -n '486p;488p;501p;128p' SKILL.md`;
  `for t in TL-01 TL-02 FIELD_DEFAULTS fictional-coordinate descriptive-gloss; do grep -c -- "$t" tools/d2-typed-labels.py; done`;
  `git log --oneline -1 -- corpus/knowledge/synthesis/loanword-material-dating.md`;
  `git log --oneline -1 -- corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `git log --oneline -1 -- PROVINCE.md`; `sed -n '183p' corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `grep -c "supported / partial / unresolved" SKILL.md`;
  `sha256sum SKILL.md`; `python3 tools/check-gate-battery.py --selftest`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`;
  `sha256sum reports/round-33/calib/*.md reports/round-33/op/O07-baseline-receipt.md`;
  `date -u`

## 9. Postscript — dated updates after the receipt was written (2026-10-19T03:58Z)

Append-only continuation of this file; §1–§8 above are unchanged as written.

**F-S02-1 is resolved (no longer live).** Both filed receipts were restored to
their HEAD bytes at 2026-10-19T03:55:27Z (`stat -c '%y %n'`): live digests now
`reports/round-5/validation.json` = `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794`
and `reports/round-7/validation.json` = `2f4c1e159b60d78250074c51f013d13aac3cf1b140a623d197a0883e5ecac6f3`,
each byte-identical to `git show HEAD:<path> | sha256sum`; `git status
--porcelain` no longer lists either (2026-10-19T03:58Z). The finding's substance
stands: the acceptance scripts still write their own receipts in place
(`reports/round-5/run-validation.py:194`, `reports/round-7/run-validation.py:1171`),
so any later re-run re-mutates them — cold-run condition N2 remains the live
mechanism, and the integrator should re-check `git status` immediately before
the round-33 commit.

**Late fragments landed, partially superseding §1/§3's owed cells.**
`calib/C03-item-03.md` (sha256 `66855c3647f096a7…`; `disposition_class:
carried-with-owner+reason+next-touch`, its `:170`) and `calib/C11-item-11.md`
(`f18f80f7ace9ca81…`) arrived at ~03:57–03:58Z, plus `scribe/S01-op-receipt.md`,
`scribe/S04-integration-draft.md`, `scribe/S05-telemetry-draft.md`. They are not
folded into §3's table; C13/C15 own the merge. `review/R04-R06` and
`reports/round-33/run-validation.py` were still absent at 03:58Z.

**F-S02-4 — hedged ledger rows are now a systemic C15 risk (new).** Three
claim-C seats ran before K03's canonical table landed and each hedged its row
identity: C07 offers three orderings for item 7 (`calib/C07-item-07.md:24-29`),
C11 offers a P1/P2/P3 set — P1 keys item 11 to *box-4 condition 3b*, an item
**excluded** from the canonical 12 (`calib/K03-open-items.md:88`), while P2/P3
key it to the devin gap (`calib/C11-item-11.md:236-266`) — and C01 carries a
nine-row re-map table. Two concrete hazards for the C15 ledger and its
validator:

1. **Naive insertion breaks the "rows == 12" leg.** C11's fragment alone offers
   2–3 rows for one item; C07 offers up to 3. Inserting them all yields > 12
   rows and fails `reports/round-33/claims.json:48`; C13 must select exactly one
   row per canonical OI id and drop the rest.
2. **One offered `disposition_class` is outside the claim's enum.** C11's P2/P3
   row reads `"fixed-with-evidence (process defect: telemetry durability) +
   carried-with-owner+reason+next-touch (historical samples; null counters)"`
   (`calib/C11-item-11.md:259`) — a compound string, not one of the two classes
   `claims.json:42` admits. Either the row is normalized to the enum with the
   compound reading moved to `reason`/`evidence`, or the validator files a named
   finding; silently passing it would make the class check vacuous.

This seat's reading, offered for C13: canonical row identity is K03's
(`C01↔OI-01 … C12↔OI-12`, `calib/K03-open-items.md:75-78`); hedge rows whose
item falls outside the canonical 12 are dropped, not merged; and the rubric
disposition C07 wrote as its primary belongs to OI-10 (F-S02-2).

**Additional commands for this postscript** (2026-10-19, repo root):
`git status --porcelain`; `git diff --stat reports/round-5/validation.json reports/round-7/validation.json`;
`stat -c '%y %n' reports/round-5/validation.json reports/round-7/validation.json`;
`sha256sum reports/round-5/validation.json reports/round-7/validation.json`;
`git show HEAD:reports/round-5/validation.json | sha256sum`;
`git show HEAD:reports/round-7/validation.json | sha256sum`;
`sha256sum reports/round-33/calib/C03-item-03.md reports/round-33/calib/C11-item-11.md`;
`grep -n "disposition_class" reports/round-33/calib/C03-item-03.md reports/round-33/calib/C11-item-11.md`;
`ls reports/round-33/{calib,review,scribe}`; `date -u`.
