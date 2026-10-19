- Seat: K03 | scout | claim C | date 2026-10-19 | baseline 139e3b6

# K03 — canonicalization of the twelve standing open items (round-32 dossier)

Scope: `reports/round-33/calib/K03-open-items.md` only. No filed byte edited.
All pointers below re-verified at lane HEAD `139e3b6` (2026-10-19). Non-canon
engineering evidence; no promotion/closure language.

## 1. What was canonicalized, and the honest count

Sources read in full: `reports/round-32/dossier-d13-operator-decisions.md`
(151 lines), `reports/round-32/dossier-d11-shonen-boxes.md` (227 lines),
`reports/round-32/final-dossier.md` (136 lines), `SCORECARD.md` round-32
section, `LOG.md:3495-3530`.

**The filed wording being reconciled:**
- `SCORECARD.md:444-445`: "Routed debt recorded for the operator: … **12 standing
  open items in the dossier**".
- `LOG.md:3513`: "round-32 routed debt (… **12 standing open items in the
  dossier**) is the starting queue for round 33's claim declaration."
- `reports/round-32/final-dossier.md:107-110`: "**Twelve named items** tabled
  with origins and pointers".

**Measured state of the source table:** the D13 Decision 4 table
(`reports/round-32/dossier-d13-operator-decisions.md:128-138`) carries a header
row plus **9 data rows** — command: `sed -n '130,138p'
reports/round-32/dossier-d13-operator-decisions.md | grep -c '^|'` → `9`
(run 2026-10-19). So "12" is not a literal row count of the table; it is a
count over the items the table names, under some expansion convention that the
dossier never states.

**Counting conventions, all three measured:**

| convention | rule | result |
|---|---|---|
| literal | one per D13 table data row | **9** |
| maximal | every separately-named condition counted separately (box-1 conditions 2/3/4 = 3; cold-run N1/N4/N5/N7 = 4; lore-owned = 2; design debts = 3; rubric/devin/adapter = 1 each) | **15** |
| canonical (adopted here) | expand only where the dossier itself enumerates distinct conditions with distinct fixes (box-1 conditions 2/3/4 → 3 rows; lore-owned → 2 rows); keep the cold-run set as the one filed row it is (`dossier-d13:134` = "cold-run N1/N4/N5/N7"; `dossier-d11:207` groups it as one "open at HEAD" cell) | **12** |

Adopted convention arithmetic: 3 design debts + 3 box-1 citation conditions +
1 cold-run cluster + 2 lore-owned + 1 rubric gap + 1 devin telemetry + 1
adapter-semantics = **12**. This is the only convention that both includes all
9 D13 rows and lands on the filed "12".

**Honest caveat (named, not absorbed):** the source of the numeral "12" is
`to-verify`. A plausible contamination path is the table's own first row,
"**12** D4 garment-form holds" (`dossier-d13:130`, `box2-d4.md:104`), which
carries the numeral 12 as a *hold count*, not an item count. No filed artifact
states the expansion rule that produced "12"; this fragment states the rule it
used so C13/R05 can check it rather than inherit it. If the operator's intended
set is the literal 9 rows, rows OI-04..OI-06 and OI-08..OI-09 are the
sub-splits to re-merge — the 12-row set is a superset of the 9 rows with no
row dropped.

## 2. The canonical twelve (id / item / origin / class / pointer, HEAD-checked)

Class vocabulary: `design-debt`, `citation-condition`, `cold-run-condition`,
`lore-owned-routing`, `protocol-gap`, `telemetry-gap`, `baseline-semantics`.

| id | item | origin round | class | pointer (re-verified at HEAD 139e3b6) |
|---|---|---|---|---|
| OI-01 | 12 D4 garment-form holds + the six owed form slots | r18 | design-debt | `reports/round-24/box2-d4.md:104-108` (F3: "12 open GAR form holds … six owed garment forms"); receipt limit `reports/round-22/bleed/verification.json:607` |
| OI-02 | `head2` empty proper domain (59/62 delivered forms ≤2 syllables ⇒ identity, not derivation) | r26 | design-debt | `reports/round-26/register/design.md:228` (RL-2 row); `reports/round-26/register/rules.md:89-95` (§3.2) |
| OI-03 | RL-3 register-lexicon ceiling — constraint, not defect | r27/r28 | design-debt | `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` (KTD-RLC-S-0001 cites `reports/round-27/law/design.md` §3.2 + `review.md` §4 RL-3); instrument `reports/round-28/ceiling/measure-ceiling.py` |
| OI-04 | box-1 condition 2 — loanword-dating cite cluster (`SKILL.md:486` cites `:26,60`; `:488` cites `:57`) | r24, re-confirmed r32 | citation-condition | `reports/round-24/promotion-review.md:71-76`; re-measurement `reports/round-32/dossier-d11-shonen-boxes.md:53-58` (content at corpus `:63`/`:59`) |
| OI-05 | box-1 condition 3 — `worldbible-integration-contract.md:183` mis-cite (`SKILL.md:501`, `:128`) | r24, re-confirmed r32 | citation-condition | `reports/round-24/promotion-review.md:77-80`; `dossier-d11-shonen-boxes.md:59-63` (contract unchanged since `291c714`) |
| OI-06 | box-1 condition 4 — dangling tool anchors `TL-01`/`TL-02`/`FIELD_DEFAULTS`/`fictional-coordinate`/`descriptive-gloss` | r24, re-confirmed r32 | citation-condition | `reports/round-24/promotion-review.md:81-84`; `dossier-d11-shonen-boxes.md:64-68` (0 hits in `tools/d2-typed-labels.py`) |
| OI-07 | cold-run set N1/N4/N5/N7 (N1 = no dated expected-verdict errata for r5/6/7 acceptance re-runs; N4 = no real costume/era artifact set or handoff path named; N5 = "history-retaining export" wording absent; N7 = executable-surface reading never pinned as a durable artifact) | r24 | cold-run-condition | `reports/round-24/promotion-review.md:178` (N1), `:186` (N4), `:189` (N5), `:193` (N7); status at HEAD `dossier-d11-shonen-boxes.md:145-153` |
| OI-08 | lore-owned — bilateral same-revision read record still outstanding | r8/r15 (L0 row stamped round-2) | lore-owned-routing | `corpus/knowledge/synthesis/worldbible-integration-contract.md:15` ("Initial bilateral acknowledgement is **pending**"), `:7`; `reports/round-15/handoff/contract-v2-audit.md:31,48` ("the bilateral same-revision read is declared still outstanding, not represented as complete"); L0 queue `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44` (kotodama \| round-2) |
| OI-09 | lore-owned — L0 contract-digest ratification (drift vs lore's open round-93 ratification) | r8/r15 (L0 row stamped round-8) | lore-owned-routing | `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:45` (kotodama \| round-8, evidence `reports/round-8/adjacency.md`); contract `:7,:16,:155,:182`; `reports/round-15/handoff/contract-v2-audit.md:31` (contract digest `5f4c02bf…` unchanged) |
| OI-10 | calibrated numeric rubric undefined (per-axis verdicts only) | r5 | protocol-gap | `SCORECARD.md:13-14` ("defining a calibrated numeric rubric remains an explicit protocol-conformance gap") |
| OI-11 | devin availability could-not-evaluate (launched/completed counters null; seat-marker totals are not launch receipts) | r29 | telemetry-gap | `reports/round-29/recount/dispositions.md:22` (item 16); `reports/round-29/recount/audit.md:18` (item 12); source records `reports/round-25..28/availability.json` |
| OI-12 | r18 D4-adapter baseline supersession semantics (pins green, content ages; no re-pin seat claimed) | r31 sweep §5 (baselines date to r18) | baseline-semantics | `reports/round-31/final-sweep.md:187-192` (§5: "The D4 adapter baselines were not re-pinned … a successor baseline is the re-pin seat's surface") |

Seat mapping for the C-lane: C01↔OI-01 … C12↔OI-12 in this order. C14's
bounded-fix drafts correspond to OI-04, OI-05, OI-06 (the three box-1 citation
pointer fixes) and OI-07's N1 errata; OI-01..OI-03, OI-08..OI-12 are the
carry candidates (owner+reason+next-touch required).

## 3. Boundary calls — what was deliberately NOT counted as one of the twelve

Each exclusion is a dossier-verdict, not my inference:

- **box-1 condition 5 (duplicated uncertainty status block)** — `dossier-d11-shonen-boxes.md:69-75` reads it "closed at HEAD" by re-measurement (1 phrase occurrence); not open.
- **box-1 condition 1 (inventory)** — closed r30, re-verified 28/28 (`dossier-d11:44-52`); not open.
- **cold-run N2** — `dossier-d11:140-144` records the receipt guard as documented machinery; the D13 row names only N1/N4/N5/N7 (`dossier-d13:134`).
- **cold-run N3, N6** — closed r25 / in SKILL text (`dossier-d11:133-138`).
- **box-4 standing readings 3a/3b/3c** — `dossier-d11:176-181` states "standing readings, not defects"; excluded by the dossier's own wording.
- **box-2 "none of the r24 three"** — `dossier-d11:206` summary cell; the box-2 debts that remain are OI-01..OI-03, counted once.
- **Decision 1 (promotion), Decision 2 (freshness threshold), Decision 3 (closure bookkeeping)** — these are operator *decisions* (`dossier-d13:15-121`), not open items; Decision 2's F-claim pause is separately recorded in `SCORECARD.md` and `REGIMEN.md`.

## 4. Count reconciliation record (for C13 / R05)

- Declaration of this seat's counting command and date: `sed -n '130,138p'
  reports/round-32/dossier-d13-operator-decisions.md | grep -c '^|'` → `9`,
  2026-10-19.
- The "12" is **reconstructed, not quoted**: no filed artifact states the
  expansion rule. SCORECARD's/LOG's/final-dossier's "12" and this table's 12
  rows agree in count and in membership (the 12 are the 9 rows with
  box-1 → 3 and lore-owned → 2), but the derivation is this fragment's, and is
  flagged `to-verify` as to the original author's intent.
- Membership cross-check against `claims.json` claim-C `before.items`
  (`reports/round-33/claims.json:44`): "design debts: 12 D4 garment-form holds,
  head2 empty domain, RL-3 ceiling; box-1 citation conditions; cold-run
  N1/N4/N5/N7; lore-owned items; rubric gap; devin-telemetry
  could-not-evaluate; r18 adapter supersession semantics" — 9 groups, same 9
  D13 rows, no member added or dropped by this canonicalization.

## Owed

- none (K03 deliverable complete; downstream C01-C16/R04-R06 consume this table)

## Citations

- `reports/round-33/claims.json:44` — claim C before-state and the 9-group enumeration
- `reports/round-33/targets.json` (K03 seat object) — mission and out path
- `SCORECARD.md:13-14` (rubric gap), `:436-439` (round-32 verdicts), `:444-445` ("12 standing open items")
- `LOG.md:3513` (12 standing open items in the standing-inputs entry), `:3045` (bilateral acknowledgment routing), `:3495-3530` (regimen-2 opening entry)
- `reports/round-32/dossier-d13-operator-decisions.md:128-138` (Decision 4 table, 9 data rows), `:15-121` (Decisions 1-3)
- `reports/round-32/dossier-d11-shonen-boxes.md:42-79` (box 1 conditions 2-4 open; condition 5 closed), `:133-153` (box 3: N3/N6 closed, N2 documented, N1/N4/N5/N7 open), `:176-181` (box 4 standing readings), `:203-208` (summary table)
- `reports/round-32/final-dossier.md:107-110` ("Twelve named items")
- `reports/round-24/box2-d4.md:104-108` (F3, 12 holds / six owed forms)
- `reports/round-24/promotion-review.md:71-88` (conditions 2-5), `:178-195` (N1-N7)
- `reports/round-26/register/design.md:228` (RL-2), `reports/round-26/register/rules.md:89-95` (§3.2)
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` (KTD-RLC-S-0001, RL-3)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:7,15,16,155,182` (bilateral read + digest)
- `reports/round-15/handoff/contract-v2-audit.md:31,48` (bilateral read outstanding; contract digest)
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45` (kotodama round-2 and round-8 rows; file has 4 kotodama lines, 49 lines total)
- `reports/round-29/recount/dispositions.md:22`, `reports/round-29/recount/audit.md:18` (devin counters null)
- `reports/round-31/final-sweep.md:187-192` (adapter supersession semantics)
- Commands (2026-10-19, lane HEAD `139e3b6`): `sed -n '130,138p' reports/round-32/dossier-d13-operator-decisions.md | grep -c '^|'` → `9`; `grep -c "^kotodama" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → `4`; `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`
