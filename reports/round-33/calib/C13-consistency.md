- Seat: C13 | executor | claim C | date 2026-10-19 | baseline 139e3b6

# C13 — consistency cross-check over C01-C12 (claim C)

Scope: this file only. No filed byte edited, no source edit, no git mutation.
Read-only commands only. NON-CANON engineering evidence; no promotion, canon,
clearance or closure language.

Mission (`reports/round-33/targets.json`, seat C13): "Consistency cross-check
over C01-C12 fragments: no item dispositioned twice, no contradictory classes,
every pointer re-verified by at least one seat; file the consistency verdict
with a per-item table."

## 0. Verdict summary

| check | result |
|---|---|
| exactly one disposition owner per canonical item | **PASS with re-keys recorded** (F-C13-2/3/5/7; §3.1) — no item is left un-owned |
| no contradictory classes in the final ledger draft | **PASS after normalization** (F-C13-2/5) — every ledger row carries one of the two allowed values |
| every pointer re-verified by at least one seat at HEAD | **PASS 12/12** — each by its own seat's fragment (C09 landed 04:13:04Z), plus this seat's independent re-checks on all twelve |
| K03 canonical 12 ↔ C01-C12 1:1 | **PASS** (`calib/K03-open-items.md:62-73,75`) |
| ledger draft rows == 12, unique ids, required fields | **PASS 12/12 ids unique, fields complete; OI-09 `disposition_class` null at C15's cut, fillable from C09 §3** |
| claim-C threshold "no filed bytes edited by seats" | **BREACHED IN FLIGHT, RESTORED — F-C13-1**: r5/r6/r7 receipts rewritten 03:53:25Z-03:55:27Z; all three byte-identical to HEAD at 04:15:47Z; the incident itself is still unrecorded |
| membership of the twelve vs K03's adopted convention | **FAIL — named finding F-C13-4** (C10/C11 primary-disposition box-4 readings 3a/3b, which K03 excluded) |

The consistency receipt is **green for the twelve canonical rows** and carries
**two open items at claim level**: the filed-bytes incident (F-C13-1 — breached,
restored, record owed) and the membership question (F-C13-4). Both are named and
owner-assigned; neither requires rework of the disposition content.

## 1. Dependency timeline — why re-keys exist at all

All 64 seats were dispatched as ONE batch, so K03's canonical table and the
C01-C12 executors raced. Measured landing order (`ls -la --time-style=+%H:%M:%S
reports/round-33/calib/`, local = UTC-3; round declared 2026-10-19T03:49:01Z):

| file | local mtime | UTC | K03 available? |
|---|---|---|---|
| `K03-open-items.md` | 00:55:49 | 03:55:49 | — (the anchor) |
| `C07-item-07.md` | 00:55:42 | 03:55:42 | **no** (7s before) |
| `C12-item-12.md` | 00:56:37 | 03:56:37 | no |
| `C11-item-11.md` | 00:57:23 | 03:57:23 | no |
| `C08-item-08.md` | 00:59:26 | 03:59:26 | yes (reconciled) |
| `C01/C04/C03/C05/C02` | 01:00:18-01:00:48 | 04:00:18-04:00:48 | yes (reconciled) |
| `C06-item-06.md` | 01:02:25 | 04:02:25 | yes (reconciled) |
| `C10-item-10.md` | 01:10:57 | 04:10:57 | yes (but kept its own route) |
| `C09-item-09.md` | 01:13:04 | 04:13:04 | yes (reconciled) |

Consequence: C07, C11, C12 wrote before the anchor existed and each reconstructed
the item order from filed sources. C04, C05 and C10 landed after K03 but had
already fixed their own routes (each says so in its own `## Owed`). This seat
does not treat that as a seat defect — it is the batch's structure — but the
integrator must apply the re-keys below, because four mutually exclusive routes
to "12" were in play (`K03:34-43`; `C10-item-10.md:31-40` R-A/R-B/R-C/R-D;
`C11-item-11.md:12-47` P1/P2/P3; `C12-item-12.md:1-29` and `:179-186`).

**K03's adopted convention is the binding one** for this receipt: 3 design debts
+ 3 box-1 citation conditions + 1 cold-run cluster + 2 lore-owned + 1 rubric
+ 1 devin + 1 adapter = 12 (`K03-open-items.md:38,40-43`), seat map
`C01↔OI-01 … C12↔OI-12` (`K03-open-items.md:75`), and its own caveat that the
numeral "12" is reconstructed, not quoted (`K03-open-items.md:45-53`, carried by
C15 as F-C15-1).

**C15's `owed` list is stale for two paths.** `C15-ledger-draft.json` `owed[]`
names `C06-item-06.md` and `C10-item-10.md` as unlanded, but their mtimes
(04:02:25Z and 04:10:57Z) precede C15's last write (04:14:23Z, `stat -c '%y'`).
Both cross-checks can therefore be closed from landed bytes — C06 in §3.1 below,
C10 in F-C13-4 — and the integrator should not re-open them as owed work.
C15's remaining owed paths are genuinely open: `C09-item-09.md` (now landed
04:13:04Z — its `disposition_class` is available for the OI-09 fill, §3.4),
`C13-consistency.md` (this file), `open-items-ledger.json`, `run-validation.py`.

## 2. Per-item consistency table

Class column: `F` = `fixed-with-evidence`, `C` = `carried-with-owner+reason+next-touch`
(as filed in the fragment). Ledger column = C15's draft row
(`calib/C15-ledger-draft.json`). "Pointer re-verified" names the seat that ran a
dated command against the item's pointer at HEAD `139e3b6`.

| OI | item | content fragment(s) | class as filed | ledger class (C15) | pointer re-verified | verdict |
|---|---|---|---|---|---|---|
| OI-01 | 12 D4 garment-form holds + six owed slots | C01 §2, §3 | C | C | C01 (dated §2a-2d; 12 holds reproduced, `.scratch/c01-d4-out.txt`) | clean |
| OI-02 | `head2` empty proper domain | C02 §2, §3 | C | C | C02 §2; C13 re-check `register/design.md:228`, `register/rules.md:89-95` | clean |
| OI-03 | RL-3 register-lexicon ceiling | C03 §2-§4 + sub-finding C03-F1 | C (+ fix-drafted sub-finding) | C | C03 §2; C13 re-check `register-lexicon-ceilings.md:6` | clean; F1/F2 routed to C14 |
| OI-04 | box-1 cond. 2 — loanword-dating cites | C04 §1.1/§3.1 (cluster row); C05 §5 corroboration | F (C04) | C + `class_flips_to` | C04 §1; C13 re-check `SKILL.md:486,488` (stale cites stand) | re-keyed (F-C13-2) |
| OI-05 | box-1 cond. 3 — `contract:183` mis-cite | C04 §1.2/§3.2; **C05 §4 + own row `C05-row5-B`** | **F (C04) vs C (C05)** | C + `class_flips_to` | C04 §1; C13 re-check `SKILL.md:128,501`, `contract:183` | **class conflict, resolved by re-key** (F-C13-2) |
| OI-06 | box-1 cond. 4 — dangling tool anchors | C04 §1.3/§3.3; **C06 §2/§3 own draft `F-OI06`** | F (C04) vs **C at cut (C06 §2)** | C + `class_flips_to` | C04 §1; C13 re-check anchor grep = 0 hits in `tools/d2-typed-labels.py` | re-keyed; two drafts, C14 wins (F-C13-7) |
| OI-07 | cold-run set N1/N4/N5/N7 | **C05 §3 own row `C05-row5-A`**; C07 Contingency A (N4 only) | C | C | C05 §2 table; C13 re-check N5 grep `history-retaining` = 0 | clean after C15 kept C05's row (F-C13-3) |
| OI-08 | lore-owned — bilateral same-revision read | C08 §2, §3 + §4 draft | C | C | C08 §2; C13 re-check `contract:15` "pending" | clean |
| OI-09 | lore-owned — L0 contract-digest ratification | **C09 §2, §3 + §4 draft** | C | **null at C15's cut → fill C** | C09 §2; C13 re-check `.ufo/l0-questions.md:45`, `contract:7,16,155,182`, `contract-v2-audit.md:31` | **owed slice now closable** (F-C13-6) |
| OI-10 | calibrated numeric rubric undefined | **C07 primary (mislabeled OI-07)**; C10 does not disposition it | C | C | C07 §"Primary" commands; C13 re-check `SCORECARD.md:13-14` | **re-key C07→OI-10** (F-C13-3) |
| OI-11 | devin availability could-not-evaluate | **C11 §4 P2/P3 row**; C07 Contingency B (duplicate) | composite string (C11) vs C (C07) | C + `class_flips_to` | C11 §2; C13 `test -s` disposition record exit 0 | **schema violation normalized; duplicate dropped** (F-C13-5, F-C13-7) |
| OI-12 | r18 D4-adapter baseline supersession | C12 §2, §3 primary; §6 alternate 3c | C (both candidates) | C | C12 §2; C13 re-check `final-sweep.md:187-190` | clean; keep the adapter row (F-C13-4) |

## 3. Check results in detail

### 3.1 No item dispositioned twice

Twelve ledger rows, twelve unique ids, no duplicate (`json` walk of
`C15-ledger-draft.json`: ids `OI-01..OI-12`, `duplicate ids: []`). Four
overlaps existed at fragment level and each is resolved to a single owner:

- **OI-05**: C04's cluster row and C05's own row. C05 §8 declares the overlap
  by design and defers to the canonical seat; C15 kept C05's `C05-row5-B` as
  the binding OI-05 row (`C15-ledger-draft.json` row OI-05, `seat: C04 (cluster
  row) + C05 (row5-B) + C14 (draft)`).
- **OI-06**: C04 cluster + C06 dedicated. C06's fragment landed at 04:02:25Z,
  before C15's last write (04:14:23Z), though C15's `owed` still names it as
  unlanded; C06 §2 states the same dual value C15 wrote
  (`fixed-with-evidence` only once the integrator applies `F-OI06`,
  `carried-…` "the honest value at this fragment's cut"). Consistent — the
  cross-check C15 owed for C06 is closed by this receipt.
- **OI-07**: C05's row + C07's Contingency A. **C05's own ledger row** carries
  the field `owner: "C07 owns this row; integrator (round 33) for N1/N4/N5
  application…"` (`C05-item-05.md` §7 row `C05-row5-A`), while C07's actual
  OI-07 content is only N4 — C05's row is the complete one, and
  `C15-ledger-draft.json` row OI-07 cites it (`seat: C05 (row5-A) + C14
  (Fix 4) + C07 (contingency A)`, `source_fragment: …C05-item-05.md §7 row
  C05-row5-A`). C15 kept C05's; C07's Contingency A and C14's Fix 4 remain as
  corroboration.
- **OI-11**: C11's P2/P3 row + C07's Contingency B. C15 kept C11's (the
  dedicated seat). C07's duplicate carries the same class, so no contradiction.

### 3.2 No contradictory classes

Every ledger row carries one of the two allowed values
(`claims.json:46`; `C15-ledger-draft.json` `class_vocabulary`), verified by
script: 11 rows `carried-with-owner+reason+next-touch`, 1 row null (OI-09).

The only true class conflict was **OI-05: C04 `fixed-with-evidence` vs C05
`carried-…`** — the same item, two values, filed by two seats. It is resolvable
on the record, not by preference: C04 itself supplies the transition rule in its
row's `reason` field ("if the drafts are NOT applied in round 33, re-classify
this row carried-…"), and C06 §2 states the same rule. At HEAD no source edit
exists — `grep -n 'loanword-material-dating.md:26,60' SKILL.md` still hits
`SKILL.md:486` (C15's command, re-checked by this seat: the stale cites stand).
C15 therefore re-keyed OI-04/05/06 to `carried-…` with `class_flips_to:
fixed-with-evidence on integrator application + green control`. **This seat
records the re-key as correct** and finds no residual contradiction, on one
condition: the integrator must flip the three rows to `fixed-with-evidence` in
the same step that applies C14's Fixes 1-3, or leave them `carried-…` — never
leave a row `fixed-with-evidence` while the stale pointer is still live.

### 3.3 Every pointer re-verified by at least one seat

12/12. Independent re-checks run by this seat (all 2026-10-19, HEAD `139e3b6`),
each reproducing the filing seat's reading:

- `register/design.md:228` (RL-2 row) and `register/rules.md:89-95` (§3.2) — OI-02.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` — OI-03.
- `SKILL.md:486,488,501,128` carry the three stale cites; `grep -c` of the five
  anchor tokens in `tools/d2-typed-labels.py` = **0** — OI-04/05/06.
- `grep -n -i "history-retaining" SKILL.md | wc -l` = **0** — OI-07 (N5).
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:15` = "Initial
  bilateral acknowledgement is **pending**" — OI-08.
- `.ufo/l0-questions.md:45` (kotodama | round-8 digest-drift row present and
  unanswered), `contract:7,16,155,182`, `contract-v2-audit.md:31` — OI-09
  (whose dedicated fragment landed last; this is the one item no earlier seat
  could verify at C15's cut).
- `SCORECARD.md:13-14` — OI-10.
- `test -s reports/round-29/devin-availability-disposition.md` → exit **0**
  (1304 B); `recount/audit.md:18` — OI-11.
- `reports/round-31/final-sweep.md:187-190` — OI-12.

### 3.4 The ledger draft's own consistency receipt

C15 filed `consistency_receipt.present = false, owed = true` pointing at this
file. That leg can now be satisfied: this receipt is the C13 surface, and the
integrator may set the ledger's `consistency_receipt` to
`reports/round-33/calib/C13-consistency.md` with the re-keys in F-C13-2/3/5/7
recorded, and fill `OI-09.disposition_class` from `C09-item-09.md:101`
(`carried-with-owner+reason+next-touch`).

## 4. Named findings

| id | severity | finding | owner |
|---|---|---|---|
| **F-C13-1** | **major** | **Filed receipts were written in place during this round — three files, then restored.** Window **03:53:25Z-03:55:27Z** (round declared 03:49:01Z): `reports/round-5/validation.json` (mtime 03:53:25Z, content-differing), `reports/round-7/validation.json` (03:53:28Z, content-differing), `reports/round-6/validation.json` (03:54:32Z, **mtime-only**, bytes never differed). Cause: the historical runners write their own receipt in place — `reports/round-5/run-validation.py:194` and `reports/round-7/run-validation.py:1171` both do `(HERE / "validation.json").write_text(...)` — which is exactly the hazard filed as cold-run condition **N2** (`reports/round-24/promotion-review.md:180-182`: "the three acceptance scripts rewrite filed tracked receipts in place; the isolation caveat must cover them"). This seat observed the modification at 03:54:10Z (`git status --porcelain`, `git diff --stat` = 3 insertions/3 deletions) and observed the **restored** state at 04:15:47Z: `git hash-object <f>` == `git rev-parse HEAD:<f>` for all three (`r5 778c3f5e…`, `r6 9f6a0f45…`, `r7 e7a8d449…`), i.e. byte-identical to `139e3b6`. **Status: breached in flight, restored, record owed** — no LOG.md entry or telemetry row records the write or the restore (LOG.md still carries only its pre-declaration 18-line regimen-2 entry, `git diff --stat LOG.md`). Probable writer **C05, `to-verify`** (C05's fragment documents running `python3 reports/round-{5,6,7}/run-validation.py`, but inside an isolated `git archive HEAD` copy, `.scratch/c05-iso/`, `C05-item-05.md` §2 row 1, `:365`, `:492-493`; the in-tree run is a separate event). Independently found and filed by **A03** (`adj/A03-scope.md:265`, A03-F1), **A09/A15** (`adj/A15-audit-draft.md:176`, A09-F2/A12-DEF-01, which adds the round-6 mtime-only detail and the `git hash-object` check) and **R06** (`review/R06-calib-review.md:18,249,467`, which reproduced N1/N2 and names the recovery command `git checkout -- reports/round-5/validation.json reports/round-7/validation.json`). Forward risk on the same mechanism: `reports/round-26/run-validation.py:1909` writes its own filed receipt (`A15-audit-draft.md:176`; re-verified by this seat). | integrator: (a) record the incident + restore as a dated LOG.md/telemetry row (append-only, never a silent heal); (b) confirm no other round's receipt is touched at close; (c) do not run any `run-validation.py` in-tree again this round |
| **F-C13-2** | major | Class conflict on OI-04/05/06: C04 filed `fixed-with-evidence` while C05 (OI-05) and C06 (OI-06) filed `carried-…` at the same HEAD, where no SKILL.md edit exists. Resolved by C15's re-key + `class_flips_to`; the flip must be atomic with the integrator's application of C14 Fixes 1-3. | integrator |
| **F-C13-3** | major | Id collision from the pre-K03 seats: C07's primary disposition (the **rubric** item) is labeled `OI-07`, but K03's `OI-07` is the cold-run cluster and the rubric is `OI-10` (`K03-open-items.md:68,71`); C07 also files a **second** row under the same id for the devin item (`C07-item-07.md:83,173`). C15 re-keyed the rubric row to OI-10 and kept C05's row as OI-07. C08 flagged the same collision independently (`C08-item-08.md:32-36`). This seat confirms the re-key and records it as **not** a duplicate-disposition defect. | C13 (recorded); integrator (apply) |
| **F-C13-4** | major | **Membership conflict.** C10 primary-dispositions box-4 reading **3a** (`C10-item-10.md:31-40` route R-A) and C11 primary-dispositions reading **3b** (`C11-item-11.md:48-104` route P1); C12's §6 alternate dispositions **3c**. K03 explicitly excluded all three — `dossier-d11-shonen-boxes.md:176-181` calls them "standing readings, not defects", and `K03-open-items.md:88` excludes them by the dossier's own wording. Under the binding convention those three dispositions are **outside the twelve** and correctly have no ledger row; but two seats' *primary* work then does not disposition their canonical slot (C10's slot content came from C07's re-keyed row; C11's from its own P2/P3 alternate). Integrator decision required: (a) keep the twelve as K03 canonicalized and record 3a/3b/3c as out-of-set corroboration, or (b) re-open the canonicalization. **This seat does not decide it** — the count's provenance is already `to-verify` (F-C15-1). | integrator / operator |
| **F-C13-5** | minor | Schema violation: C11's devin row carries a composite class string — `fixed-with-evidence (process defect: telemetry durability) + carried-with-owner+reason+next-touch (historical samples; null counters)` — which is not one of the two allowed values. C15 kept the `carried-…` half plus `class_flips_to`. Normalized; recorded so the integrator does not copy the composite string into the ledger. | integrator |
| **F-C13-6** | minor | Two corrections to filed claims about the "12": (a) **C10's `to-verify` note is a false negative** — it asserts `grep -n "12 standing open items" SCORECARD.md` finds nothing and infers "SCORECARD.md contains no such phrase"; the phrase exists at `SCORECARD.md:444-445`, wrapped across the newline ("…7 unindexed lessons, 12 standing / open items in the dossier…"), so a single-line grep exits 1. K03's citation (`K03-open-items.md:17-18`) is the correct one. (b) **D13's devin pointer is loose** — `reports/round-29/recount/` resolves to the census, not the disposition record; canonical path is `reports/round-29/devin-availability-disposition.md` (`C07-item-07.md:157-160`, `C15` row OI-11 `pointer_accuracy_finding`). | integrator (record); no rework |
| **F-C13-7** | minor | Draft duplication on OI-05/OI-06: C05 §4 drafts `FD-B1C3-a/b` and C05 §5 drafts for conditions 2/4 duplicate C14 Fixes 1-3; C06 §3 files `F-OI06` for the same lines as C14 Fix 3. C05 §8 and C06 §2 both declare C14 the single aggregator. This seat records the rule: **where wording differs, C14's wins**, and the integrator applies exactly one draft per line. | C14 / integrator |

### 4.1 Not findings (checked and cleared)

- **No double disposition survives into the ledger** (§3.1).
- **No seat edited `corpus/lessons/*.md`, `SKILL.md`, `tools/gates/frozen/**`,
  or fleet `.ufo/**`**: `git status --porcelain` shows only `LOG.md` (the
  pre-declaration regimen-2 entry), untracked `REGIMEN.md` /
  `reports/round-33/`, and — until its 03:55:27Z restore — the F-C13-1 receipts.
  F-C13-1 is the single filed-bytes incident and it is named, restored and
  still owed a record; it is not absorbed.
- **No promotion/canon/closure language** in the C-fragments: every occurrence
  of those words in the fragments is a negation or a routed reference (sample
  checked: `C05-item-05.md` §8, `C08-item-08.md` §3, `C12-item-12.md` §3).
  A08 owns the exhaustive grep.

## 5. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# 1. ledger schema + duplicate-id check
python3 - <<'PY'
import json
d=json.load(open('reports/round-33/calib/C15-ledger-draft.json'))
rows=d['rows']; ids=[r['id'] for r in rows]
print(len(rows), sorted(ids), 'dupes=',[i for i in set(ids) if ids.count(i)>1])
print([r['id'] for r in rows if r.get('disposition_class') not in
       ('fixed-with-evidence','carried-with-owner+reason+next-touch')])
PY
# 2. F-C13-1 (filed-receipt incident) evidence — current state and mechanism
git status --porcelain -- reports/round-5 reports/round-6 reports/round-7
for n in 5 6 7; do f=reports/round-$n/validation.json; \
  [ "$(git hash-object $f)" = "$(git rev-parse HEAD:$f)" ] && echo "r$n CLEAN" || echo "r$n DIFFERS"; done
ls -la --time-style=full-iso reports/round-5/validation.json reports/round-6/validation.json reports/round-7/validation.json
grep -n 'write_text' reports/round-5/run-validation.py reports/round-7/run-validation.py reports/round-26/run-validation.py
# 3. F-C13-6 (SCORECARD phrase wraps across the newline)
grep -n "12 standing open items" SCORECARD.md ; echo "exit=$? (1 = the wrap)"
sed -n '444,445p' SCORECARD.md
# 4. class-at-cut (no SKILL.md edit applied)
grep -n 'loanword-material-dating.md:26,60' SKILL.md
```

Expected at 04:15:47Z: 12 unique ids; exactly `['OI-09']` as the non-conforming
class at C15's cut (fillable from `C09-item-09.md:101`); **no** modified round-5/6/7
rows and `CLEAN` for all three (the incident was restored; its record is owed);
the mechanism greps hit `run-validation.py:194`, `:1171`, `:1909`; grep exit 1
with the phrase visible at `SCORECARD.md:444-445`; the stale cite still at
`SKILL.md:486`.

## Owed

- **F-C13-1 record** — the in-tree write of `reports/round-5/6/7/validation.json`
  (window 03:53:25Z-03:55:27Z) and its restore are **outside every seat's write
  scope** to record: the integrator files the dated LOG.md/telemetry row naming
  the incident, the restore and the probable writer (`to-verify`). The tree is
  byte-identical to `139e3b6` at 04:15:47Z, so the claim-C threshold holds at the
  current tree; what is owed is the record, not a repair.
- **F-C13-4 decision** — whether the twelve stay as K03 canonicalized (3a/3b/3c
  recorded as out-of-set corroboration) or are re-canonicalized; integrator /
  operator, not this seat.
- `reports/round-33/calib/open-items-ledger.json` — the finalized ledger does
  not exist yet; C15's draft is the input. This receipt's re-key list must be
  folded there.
- `reports/round-33/run-validation.py` — absent; the claim-C legs named in
  `claims.json:48` cannot be run by this seat. S04's spec owns the leg
  definitions.

## Citations

Paths (read/verified 2026-10-19 at HEAD `139e3b662900557afe54f632b468619593dc9fcb`):

- `reports/round-33/targets.json` (seat C13; shared_rules), `reports/round-33/claims.json:44-50` (claim C, classes, thresholds, counting commands)
- `reports/round-33/calib/K03-open-items.md:17-18,24-30,34-43,45-53,60-73,75-78,84-90`
- `reports/round-33/calib/C01-item-01.md:13-30,175-190,230-237,262-272`; `C02-item-02.md:15-33,238-250,289-294`; `C03-item-03.md:10-33,158-180,209-215,262-287,297-309`; `C04-item-04.md:10-35,117-135,332-360,352-370`; `C05-item-05.md:11-42,56-104,227-272,330-353,354-399,399-413`; `C06-item-06.md:3-26,96-125,204-228`; `C07-item-07.md:5-29,31-103,105-145,147-190,192-209`; `C08-item-08.md:14-36,69-117,169-181`; `C09-item-09.md:1-35,62-116,156-172,193-199`; `C10-item-10.md:1-60`; `C11-item-11.md:12-47,48-104,105-218,234-268`; `C12-item-12.md:1-29,107-130,179-199`
- `reports/round-33/calib/C14-fix-drafts.md`; `reports/round-33/calib/C15-ledger-draft.json` (`_meta`, `count_provenance`, `consistency_receipt`, `class_vocabulary`, `draft_class_policy`, `findings` F-C15-1..5, `owed`, rows OI-01..OI-12); `reports/round-33/calib/C16-receipt.md`; `reports/round-33/calib/P02-plan.md:77`
- `reports/round-33/adj/A03-scope.md:265` (A03-F1, same incident); `reports/round-33/adj/A15-audit-draft.md:176` (A09-F2/A12-DEF-01, round-6 mtime-only, `git hash-object` check, the round-26 hazard); `reports/round-33/review/R06-calib-review.md:18,249,467` (N1/N2 reproduction, recovery command, clean-state receipt)
- `reports/round-32/dossier-d13-operator-decisions.md:125-138`; `reports/round-32/dossier-d11-shonen-boxes.md:42-79,133-153,176-181,203-208`; `reports/round-32/final-dossier.md:107-110`
- `reports/round-24/promotion-review.md:71-88,178-195,180-182`; `reports/round-24/box2-d4.md:104-108`
- `reports/round-22/bleed/verification.json:607`; `reports/round-15/handoff/contract-v2-audit.md:31,72`; `reports/round-26/register/design.md:228`; `reports/round-26/register/rules.md:89-95`; `reports/round-29/devin-availability-disposition.md`; `reports/round-29/recount/audit.md:18`; `reports/round-29/recount/dispositions.md:22`; `reports/round-31/final-sweep.md:158,167,187-192`; `reports/round-30/fixes/telemetry-convention.md`
- `SCORECARD.md:13-14,444-445`; `LOG.md:3307,3312,3513`; `AGENTS.md:15-31`; `REGIMEN.md:25-50`
- `SKILL.md:128,486,488,501,531-534`; `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6`; `corpus/knowledge/synthesis/worldbible-integration-contract.md:7,15,16,155,182`; `tools/d2-typed-labels.py`; `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45`

Commands (all 2026-10-19, this seat, read-only): `git rev-parse HEAD` →
`139e3b662900557afe54f632b468619593dc9fcb`; `git status --porcelain`;
`git diff --stat reports/round-5/validation.json reports/round-7/validation.json`
(3 insertions/3 deletions at 03:54Z, empty at 04:15Z); `git hash-object <f>` vs
`git rev-parse HEAD:<f>` for `reports/round-{5,6,7}/validation.json` → all CLEAN;
`ls -la --time-style=full-iso` / `stat -c '%y'` on the three receipts
(03:53:25Z, 03:54:32Z, 03:53:28Z restored at 03:55:27Z) and on
`reports/round-33/calib/`; `git diff --stat LOG.md` (18 insertions, unchanged);
`grep -n 'write_text' reports/round-5/run-validation.py reports/round-7/run-validation.py`
→ `:194` / `:1171`, and `reports/round-26/run-validation.py` → `:1909`;
`grep -n "12 standing open items" SCORECARD.md` → exit 1;
`sed -n '444,445p' SCORECARD.md`; `grep -n -i "history-retaining" SKILL.md | wc -l`
→ 0; `grep -c "TL-01\|TL-02\|FIELD_DEFAULTS\|fictional-coordinate\|descriptive-gloss" tools/d2-typed-labels.py`
→ 0; `grep -n 'loanword-material-dating.md:26,60' SKILL.md` → `:486`;
`grep -c "examples/culture-d2/" examples/culture-d4/typed-labels.d4.yml` → 1;
`test -s reports/round-29/devin-availability-disposition.md` → exit 0;
`sed -n` spot-reads of `register/design.md:228`, `register/rules.md:89-95`,
`register-lexicon-ceilings.md:6`, `contract:7,15,16,155,182`,
`contract-v2-audit.md:31`, `.ufo/l0-questions.md:44-45`, `LOG.md:3307,3312`,
`final-sweep.md:158,167,187-190`, `SCORECARD.md:13-14`; the JSON walk of
`C15-ledger-draft.json` (12 rows, unique ids, class/field check) and the
fragment scanner `.scratch/c13-consistency-check.py`.
