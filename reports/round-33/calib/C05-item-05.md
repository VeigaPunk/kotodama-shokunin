- Seat: C05 | executor (claim C, item 5) | claim C | date 2026-10-19 | baseline 139e3b6

# C05 — disposition of standing open item 5

Write scope: this file only. No source edits, no git mutations, no filed-byte
edits (rounds 1-32 untouched). Every measurement below is this seat's, dated
2026-10-19, taken at lane HEAD `139e3b662900557afe54f632b468619593dc9fcb`.
Scratch: `TMPDIR=$PWD/.scratch`; the acceptance re-runs were executed in
`.scratch/c05-iso/` (a `git archive HEAD` copy), never in the real tree.

## 1. Item identification — K03 landed mid-run; item 5 = OI-05

At this seat's cut `reports/round-33/` held only `claims.json`, `targets.json`
and `telemetry/dispatch-declared.json` (`find reports/round-33 -type f`,
2026-10-19), so **`reports/round-33/calib/K03-open-items.md` was not yet
landed** and item 5 was derived from K03's own named primary source
(`reports/round-32/dossier-d13-operator-decisions.md` Decision 4 table,
`:130-138`, plus `dossier-d11-shonen-boxes.md` open conditions, `:205-208`).
**K03 landed during this seat's run and is reconciled here**: its canonical
table (`reports/round-33/calib/K03-open-items.md:60-73`) numbers the twelve as
OI-01..OI-12, and **item 5 = OI-05 = box-1 condition 3, the
`worldbible-integration-contract.md:183` mis-cite** (`K03:66`), dispositioned
in full at §4 below. The cold-run cluster is OI-07 (`K03:68`), dispositioned
at §3; box-1 conditions 2 and 4 are OI-04 and OI-06 (`K03:65`, `:67`),
drafted at §5.

The Decision 4 table carries 9 data rows (`dossier-d13:130-138`; K03 measures
the same: `sed -n '130,138p' … | grep -c '^|'` → 9, `K03:26-27`); the
C-claim's "12" (`claims.json:42-45`) requires three further splits drawn from
D11's `open at HEAD` column. Three schemes reconcile to exactly 12, and they
disagree about row 5:

| scheme | split rule | rows 1-12 | row 5 |
|---|---|---|---|
| A | D13 order; cold-run cluster expanded into N1/N4/N5/N7 | garment(130), head2(131), RL-3(132), box1-conds(133), **N1, N4, N5, N7**, lore(135), rubric(136), devin(137), r18-adapter(138) = 12 | **N1** |
| B | box-1 conds split 2/3/4; lore split bilateral-read / L0-digest; cold-run cluster kept whole | garment, head2, RL-3, cond2, **cond3**, cond4, cold-run-cluster, bilateral-read, L0-digest, rubric, devin, r18 = 12 | **box-1 condition 3** |
| C | D13's 9 rows + D11 box-4 standing readings 3a/3b/3c (`dossier-d11:208`) | garment, head2, RL-3, box1-conds, **cold-run cluster**, lore, rubric, devin, r18, 3a, 3b, 3c = 12 | **cold-run cluster (N1 first)** |

**K03 adopted scheme B** (`K03:38`, `:40-43`: 3 design debts + 3 box-1
citation conditions + 1 cold-run cluster + 2 lore-owned + 1 rubric gap +
1 devin telemetry + 1 adapter semantics = 12), and its row order matches this
fragment's scheme-B order exactly (OI-04/OI-05/OI-06 = the three box-1
conditions; OI-07 = the cold-run cluster). Because K03 was unavailable while
this seat's checks ran, §3 and §5 are retained as cross-coverage for
OI-07/OI-04/OI-06 rather than discarded — every row they touch is a real row
of the canonical twelve. The count-provenance reconciliation itself stays
K03's and C13's to file, including K03's own `to-verify` caveat on the
numeral's origin (`K03:45-53`); this seat claims no authority over the
enumeration, only over item 5's content.

## 2. Status quo at HEAD — dated checks

| # | check | command | result (2026-10-19) |
|---|---|---|---|
| 1 | cold-run N1: acceptance scripts at clean HEAD | `git archive HEAD \| tar -x -C .scratch/c05-iso` then `python3 reports/round-{5,6,7}/run-validation.py` inside the copy | **exit 1 / 1 / 1** — r5: O leg embeds the round-3 frozen replay, `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced`; r6: `"error": "entry prefix lost: corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md"`; r7: `"historical knowledge totals changed: {'files': 201, 'raw_lines': 717, ...}"` + `"claim F: wrong rejection for duplicate-parent-receipt-does-not-inflate"` + r6 cascade |
| 2 | N2 control (overwrite mechanism, re-measured) | same copy, `git -C <real repo> show HEAD:reports/round-N/validation.json \| cmp -` after each run | **CHANGED for all three** — r5/r6/r7 filed receipts are rewritten in place by one run (r24 N2 re-confirmed at HEAD) |
| 3 | N1 text state: expected verdicts absent | `grep -n "run-validation.py" SKILL.md` | three imperative sites, zero expected-verdict text: `:630-632` (r5), `:655-658` (r6), `:701-704` (r7) |
| 4 | N4: real operands absent from the four files | `grep -n "handoff.md\|artifact set" SKILL.md` → no hit; `costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` → exit 1 (1 finding, the documented C03 R-01 red); `… examples/culture-d2/packet.d2.yml` → exit 0; `… examples/culture-d4/packet.d4.yml` → exit 0 | operands **exist on disk** (`examples/culture-d3/handoff.md`, `examples/culture-d3/packet.gates.yml`) but are named in no cold-run file → N4 is pointer-level fixable |
| 5 | N5: "isolated repo export" undefined | `grep -n -i "history-retaining" SKILL.md` → **0 hits**; the phrase appears once at `SKILL.md:584` | still open as filed |
| 6 | N7: no durable reading pin | `grep -rn "reading of.*checklist\|per-seat file set" reports/round-2[5-9] reports/round-3[0-2]` → no pin artifact; only `reports/round-24/cold-run-fixes.md:30` (B-F5 → N7) | still open as filed |
| 7 | box-1 cond 3: the mis-cited contract line | `worldbible-integration-contract.md:183` = "Every delivered record has scope, stable identity, provenance/invention status, and a disposition question; unknowns are not blank cells."; `grep -rn -i "boilerplate\|basis\|witness"` in that contract → **0 hits** | the cite cannot be repointed inside the contract; the rule lives in the harness (`tools/harness/packet_uncertainty.py:45,84`) and `reports/round-15/claims.json:14` |
| 8 | box-1 cond 2: loanword cites | `loanword-material-dating.md:26` = **blank line**; `:57` = "Recipient form reflects a donor innovation…"; `:59` = "…Dictionary selection bias; imported prestige terminology for local goods"; `:30` = "Lexical \| A word or sense enters a specified speech community \| Arrival of its referent…"; `:63` = "…Date the **sense–referent pairing**…" | both r24 defects re-confirmed, plus the correct re-point targets located |
| 9 | box-1 cond 4: dangling anchors | `for t in TL-01 TL-02 FIELD_DEFAULTS fictional-coordinate descriptive-gloss; do grep -c -- "$t" tools/d2-typed-labels.py; done` → **0 0 0 0 0** | still open; live vocabulary located: `D2L-*` (`tools/d2-typed-labels.py:421-427`), `KINDS` (`:410`, three kinds) |

## 3. Cross-coverage for OI-07 (seat C07) — the cold-run cluster `N1/N4/N5/N7`

This was item 5 under my pre-K03 schemes A/C; under K03's adopted scheme B it
is **OI-07** (`K03:68`), not item 5. Retained because its content is a real row
of the canonical twelve.

Origin: r24 (`reports/round-24/promotion-review.md:176-195`, conditions 1, 4, 5,
7), re-confirmed r32 (`dossier-d11:207`), listed as debt at
`dossier-d13:134`. Pointer at HEAD: `SKILL.md:630-632`, `:655-658`,
`:694-700`, `:701-704`, `:583-584`.

### N1 — dated expected-verdict errata (major) — **fix drafted, not applied**

Status quo re-verified at HEAD: all three scripts exit 1 for distinct,
explainable causes (§2 row 1); the three SKILL sites state the commands
imperatively with no expected verdict (§2 row 3). r24's own reading is
reproduced exactly, with one updated number: r24 measured round-7's
`files: 199`; at HEAD it is `files: 201` — same class, corpus grown since.

Disposition class: **carried-with-owner+reason+next-touch** with a bounded
draft attached; flips to `fixed-with-evidence` once the integrator applies
the drafts and the control below is green. Seats may not edit source.

Fix drafts (exact before/after; `SKILL.md` is not a filed round byte, so the
integrator may apply these directly):

FD-N1-a — `SKILL.md:630-632`
before:
```
Round-scoped acceptance is re-runnable with
`python3 reports/round-5/run-validation.py`; it records the two declared claims
and writes its own validation receipt. It is an orchestration check, not a new
general culture or scholarship-certification gate.
```
after:
```
Round-scoped acceptance is re-runnable with
`python3 reports/round-5/run-validation.py`; it records the two declared claims
and writes its own validation receipt. It is an orchestration check, not a new
general culture or scholarship-certification gate. **Expected verdict on a live
tree: exit 1**, because its O leg embeds the round-3 frozen replay, which reads
exit 2 / 7-of-7 `gate_digest_mismatch` outside a pinned-revision tree — the
state documented for that replay above, not a current break (measured
2026-10-19, round 33 seat C05, isolated copy of `139e3b6`). Run it in a
disposable copy: it rewrites the filed `reports/round-5/validation.json`.
```

FD-N1-b — `SKILL.md:655-658`
before:
```
Re-run this round's receipt/count/preservation checks with
`python3 reports/round-6/run-validation.py`. The five parent readings are
separate from the twenty qualifying worker main passages; neither count
certifies whole cultures, ancient pronunciation or cultural permission.
```
after:
```
Re-run this round's receipt/count/preservation checks with
`python3 reports/round-6/run-validation.py`. The five parent readings are
separate from the twenty qualifying worker main passages; neither count
certifies whole cultures, ancient pronunciation or cultural permission.
**Expected verdict on a live tree: exit 1** — the script pins round-6-era byte
prefixes of corpus files and the corpus has legitimately grown since (appended
errata), so its invariant is structurally unre-publishable outside the round-6
tree (`entry prefix lost: …mesopotamia-sumer-akkad.md`; measured 2026-10-19,
round 33 seat C05, isolated copy of `139e3b6`). Run it in a disposable copy: it
rewrites the filed `reports/round-6/validation.json`.
```

FD-N1-c — `SKILL.md:701-704` (checklist item 5)
before:
```
5. Run `python3 reports/round-7/run-validation.py` for the original F/O
   thresholds, input preservation and old-surface regressions. It writes its
   own receipt, not historical receipts. Fresh source access and invented
   model consistency are causally separate checks.
```
after:
```
5. Run `python3 reports/round-7/run-validation.py` for the original F/O
   thresholds, input preservation and old-surface regressions. It writes its
   own receipt, not historical receipts. Fresh source access and invented
   model consistency are causally separate checks. **Expected verdict on a live
   tree: exit 1** — historical knowledge totals have changed (files 201 /
   raw_lines 717 at `139e3b6`), the duplicate-parent-receipt control rejects by
   parent-check identity collision, and the round-6 acceptance it chains reads
   `.gitignore` as changed (measured 2026-10-19, round 33 seat C05, isolated
   copy of `139e3b6`). Run it in a disposable copy: it rewrites the filed
   `reports/round-7/validation.json`.
```

Control for all three (the integrator's post-edit verification): re-run the
three commands in a fresh `git archive HEAD` copy — exit 1 each with the
reasons quoted — and confirm the three filed `validation.json` receipts are
byte-identical to HEAD afterwards (`git diff HEAD --stat -- reports/round-{5,6,7}/validation.json`
empty).

### N4 — real operands for checklist items 3/4 (major) — **fix drafted, not applied**

Status quo: the four files name no real costume/era artifact set and no real
handoff packet path (`dossier-d11:150`; §2 row 4). Measured: the operands
exist and behave as documented — `examples/culture-d3/handoff.md` is the
handoff the envelope check passes 16/16 + 20 glossary rows on
(`reports/round-24/cold-run-conditions.md` §A), and
`costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` reads
the documented C03 R-01 red (exit 1, 1 finding) while the d2/d4 packets read
clean. So N4's residue is pointer-level, not artifact-absent.

Fix draft — `SKILL.md:694-700`
before:
```
3. Run legacy naming and costume checks on `packet.gates.yml`. Keep naming's
   CROSS-HOLD (and E0/E1 similarity review) and C03's costume R-01 finding;
   neither is a green clearance gate. Verify the native coda adapter, not
   merely a permissive synthetic fixture.
4. Compare the handoff's glossary, names, source bridges and digest rows
   against actual packet bytes, then run its structural envelope check.
   Sixteen fields and twenty glossary rows alone cannot prove content agrees.
```
after:
```
3. Run legacy naming and costume checks on
   `examples/culture-d3/packet.gates.yml`. Keep naming's CROSS-HOLD (and E0/E1
   similarity review) and C03's costume R-01 finding; neither is a green
   clearance gate. Verify the native coda adapter, not merely a permissive
   synthetic fixture.
4. Compare the handoff's glossary, names, source bridges and digest rows
   against actual packet bytes (`examples/culture-d3/handoff.md` against
   `examples/culture-d3/packet.gates.yml`), then run its structural envelope
   check. Sixteen fields and twenty glossary rows alone cannot prove content
   agrees.
```
Control: `python3 tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md`
→ exit 0; `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml`
→ exit 1 with the single R-01 finding (both measured 2026-10-19, this seat).

### N5 — define "isolated repo export" as history-retaining (minor) — **fix drafted, not applied**

Status quo: `SKILL.md:583-584` says "Run that battery in an isolated repo
export; byte equality after a run does not prove no writes"; `history-retaining`
occurs 0 times in SKILL.md (§2 row 5). The round-3 restore-and-replay leg
resolves gate bytes from `291c714` via `.git` (`SKILL.md:573`, `:594-598`), so
a plain tree export cannot execute it.

Fix draft — `SKILL.md:583-584`
before:
```
isolated repo export; byte equality after a run does not prove no writes.
```
after:
```
isolated repo export — a history-retaining copy (clone or worktree; the
round-3 restore-and-replay leg reads `291c714` from `.git`, which a plain tree
export lacks); byte equality after a run does not prove no writes.
```
Control: `git clone --no-hardlinks . <tmp> && git -C <tmp> show 291c714:tools/gates/phonology-sanity-gate.py | sha256sum`
resolves, while the same command in a `.git`-less export fails.

### N7 — pin the executed checklist reading + per-seat file set (process) — **carried**

Status quo: no durable artifact pins (a) which reading of "the SKILL.md
executable checklist" future cold runs execute or (b) the exact per-seat file
set; the two r24 executors diverged productively
(`reports/round-24/cold-run-fixes.md:30`, B-F5 → N7; §2 row 6).

Disposition class: **carried-with-owner+reason+next-touch**. Owner: the parent
(operator), not a lane seat — the condition is a declaration of authority, and
`AGENTS.md` forbids this lane absorbing contested scope. Reason: only the
parent can fix which reading is canonical and who holds which file set.
Next touch: land a one-file pin artifact (proposed path
`reports/round-33/calib/N7-reading-pin.md`) naming the reading, the four-file
set, and the per-seat file assignment; a lane seat may draft it, the parent
must issue it. Drafting it inside this round would be a lane seat issuing a
parent-owned declaration, so this seat records the shape and stops.

## 4. Item 5 under scheme B — box-1 condition 3, the `:183` mis-cite

Origin: r24 audit-2 (`reports/round-24/promotion-review.md:77-80`), re-confirmed
r32 (`dossier-d11:59-63`), listed as debt at `dossier-d13:133`. Two live sites:
`SKILL.md:128` and `SKILL.md:501`.

Status quo re-verified at HEAD (§2 row 7): `worldbible-integration-contract.md:183`
carries the delivered-record checklist item, not the basis rule; and
`boilerplate`, `basis` and `witness` all occur **0 times** in that contract —
so r24's "re-point or dated erratum" resolves to **re-point out of the
contract**, not within it. The rule's real authority is the enforcing harness
and the round-15 declaration.

Fix draft FD-B1C3-a — `SKILL.md:128`
before:
```
rejected (`worldbible-integration-contract.md:183`; v2-design §2.3).
```
after:
```
rejected (`reports/round-15/claims.json:14`; executable
`tools/harness/packet_uncertainty.py:45,84`; v2-design §2.3).
```

Fix draft FD-B1C3-b — `SKILL.md:501`
before:
```
| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; `worldbible-integration-contract.md:183`) |
```
after:
```
| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; executable `tools/harness/packet_uncertainty.py:45,84`) |
```

Controls: `grep -c -i boilerplate corpus/knowledge/synthesis/worldbible-integration-contract.md`
→ 0 (the cite is unmendable in-file); `python3 tools/harness/packet_uncertainty.py --selftest`
→ exit 0 with its boilerplate leg green (`reports/round-15.md:108` records
19/19 checks including the boilerplate rule); the replacement ids resolve:
`reports/round-15/claims.json:14` contains "zero boilerplate",
`tools/harness/packet_uncertainty.py:45` is `BOILERPLATE_TOKENS`, `:84` is
`_is_boilerplate`.

Disposition class: **carried-with-owner+reason+next-touch** (draft ready;
flips to `fixed-with-evidence` on application + green control).

## 5. Enumeration-coverage rows — box-1 conditions 2 and 4

Drafted so that schemes A and B both find their row-4/row-6 neighbours
dispositioned by this seat rather than orphaned. Both are the same class and
treatment as §4.

**Condition 2 (loanword cite cluster, `promotion-review.md:71-76`)** — both
defects re-measured (§2 row 8). Two single-token edits, each independently
bounded:

FD-B1C2-a — `SKILL.md:486`: replace `` `loanword-material-dating.md:26,60` ``
with `` `loanword-material-dating.md:30,112` `` — `:26` is a blank line and
`:30` is the clock-table row that actually states "Arrival of its referent" is
not automatically dated; `:112` is the method sentence ("Maintain separate
intervals for first trade, name adoption, and costume popularization"). `:60`
(topical, about a native term replacing a foreign label) is retained only if
the integrator prefers a two-token minimal edit; the `:63` sense–referent line
that r24 names is the authority for the *sibling* row's rule at `SKILL.md:487`,
so re-pointing to it here would move the row's claim, not fix its cite — this
seat recommends `:30,112` and flags the choice to C14.

FD-B1C2-b — `SKILL.md:488`: replace `` (`loanword-material-dating.md:57`) ``
with `` (`loanword-material-dating.md:59`) `` — `:59` carries "Dictionary
selection bias; imported prestige terminology for local goods" verbatim.

Controls: `awk 'NR==26' corpus/knowledge/synthesis/loanword-material-dating.md`
→ empty; `grep -n "sense–referent" …` → `:63`; `grep -n "imported prestige terminology" …` → `:59`.

**Condition 4 (dangling tool anchors, `promotion-review.md:81-84`)** — 0 hits
for all five tokens (§2 row 9). A filed round-10 drift shard already recommends
the fix shape and must be honoured rather than re-derived:
`reports/round-10/drift/shard-05.md:54` — "update the four citations to the
live ids (`D2L-FORM-UNRESOLVED`, `D2L-DATA`) or land the mapping table; do not
rewrite filed round-8 report bytes"; `:46` records that
`fictional-coordinate`/`descriptive-gloss` are retired names and the class is
now handled by translated-label projection + era reconciliation.

FD-B1C4-a — `SKILL.md:479` and `:481`: replace executable `` `TL-01` `` with
`` `D2L-DATA` `` (`:479`, the label-only/off-channel hold class) and
`` `D2L-FORM-UNRESOLVED` `` (`:481`, the declared-sound-kind-with-no-bytes
hold). Verified: `tools/d2-typed-labels.py:810-814` emits `D2L_FORM`
(`= "D2L-FORM-UNRESOLVED"`, `:422`) with `hold=True` for both
no-supplied-form cases; `:421` defines `D2L_DATA` (`= "D2L-DATA"`), the class
the loader's `E-LABEL-*` codes map onto (`:2250-2257`).
FD-B1C4-b — `SKILL.md:483`: replace `` `TL-02` `` with `` `D2L-DATA` `` —
the loader's kind leg is `E-LABEL-KIND` → `D2L-DATA`
(`tools/d2-typed-labels.py:2252`), and the tool docstring now states the
repaired contract: "`P-*` loader code or `D2L-DATA`; stable message, no
traceback" (`:48`, the r25 N3 repair).
FD-B1C4-c — `SKILL.md:491`: replace "type them `fictional-coordinate` /
`descriptive-gloss`; … (tool `FIELD_DEFAULTS`)" with the live vocabulary —
the tool ships three kinds (`KINDS`, `:410`) and types era material through
era reconciliation (`resolve_era`, `:1840`; class `D2L_ERA`, `:425`), so the
row should read as an era-reconciliation/`D2L-ERA` row with the retired kind
names dropped. **to-verify:** the exact replacement wording for this cell is a
craft decision (it must not invent a kind the tool lacks); this seat has
verified the ids and the three-kind fact but leaves the sentence to C14/R06.

## 6. Observation (not one of the 12) — filed receipts and a stat artifact

Recorded because it touches N2 and because this seat published an intermediate
reading that it must correct.

- At 00:56 local (`2026-10-19T03:56Z`) `git status --porcelain` showed
  ` M reports/round-5/validation.json` and ` M reports/round-7/validation.json`,
  and `git diff` printed content differences for both. That reading was **not
  content drift**: `git hash-object <file>` equals
  `git rev-parse HEAD:<file>` for both (`778c3f5e…` r5, `e7a8d449…` r7), and
  `git diff HEAD --stat` for both paths is **empty** — the working-tree bytes
  are HEAD's bytes. The `M`/diff came from index-vs-HEAD divergence with the
  index holding older blobs (r7: index `files 189/raw 688` vs HEAD
  `files 201/raw 717`), i.e. a stale index, not edited filed bytes.
- Both files carry the identical mtime `2026-10-19 00:55:27.940762254 -0300`
  (~6 minutes after this round's declaration), while their content equals
  HEAD. Something wrote or restored both paths in this round's window without
  changing content — most consistent with a restore from HEAD of receipts a
  run had dirtied, since §2 row 2 proves one run of those scripts does change
  the bytes. **to-verify:** the cause is not determinable from the artifacts
  alone; no round-33 seat is named as the writer in any fragment landed so far.
- No action owed: filed bytes are intact at HEAD, and this seat's own
  acceptance re-runs were confined to `.scratch/c05-iso/`.

## 7. Ledger rows for C15 (schema per `claims.json:46`)

Per K03's numbering (`K03:60-73`, seat map `K03:75-78`: C05↔OI-05) the item-5
row is **OI-05**, given first; the OI-07 row is this seat's cross-coverage for
C07 and must not be double-filed. `status_at_fragment` is this seat's honest
added field: a seat may not edit source, so no row is `fixed` at fragment
time.

```json
[
  {
    "id": "OI-05",
    "id_crosswalk": "C05-row5-B",
    "item": "box-1 condition 3 — worldbible-integration-contract.md:183 mis-cite",
    "origin": "r24 (audit-2), re-confirmed r32",
    "pointer": "reports/round-24/promotion-review.md:77-80; reports/round-32/dossier-d11-shonen-boxes.md:59-63; reports/round-32/dossier-d13-operator-decisions.md:133; reports/round-33/calib/K03-open-items.md:66; SKILL.md:128 and SKILL.md:501",
    "status_quo_check": "2026-10-19, HEAD 139e3b6: contract:183 = delivered-record checklist item; grep -c -i 'boilerplate' and 'basis' and 'witness' in that contract = 0 — the cite cannot be repointed inside the contract; the enforcing authority is tools/harness/packet_uncertainty.py:45,84 with reports/round-15/claims.json:14",
    "disposition_class": "carried-with-owner+reason+next-touch",
    "status_at_fragment": "fix-drafted-not-applied",
    "evidence": "reports/round-33/calib/C05-item-05.md §2 row 7, §4",
    "fix_draft": "reports/round-33/calib/C05-item-05.md FD-B1C3-a (SKILL.md:128), FD-B1C3-b (SKILL.md:501)",
    "owner": "integrator (round 33); C14 is the single fix-draft aggregator",
    "reason": "pointer-level, bounded, but seats may not edit source",
    "next_touch": "apply FD-B1C3-a/b, run packet_uncertainty.py --selftest and the 0-hit greps, then flip to fixed-with-evidence",
    "class_flips_to": "fixed-with-evidence on application + green control"
  },
  {
    "id": "OI-07",
    "id_crosswalk": "C05-row5-A",
    "item": "cold-run set N1/N4/N5/N7 (N1 = no dated expected-verdict errata for the r5/6/7 acceptance re-runs; N4 = no real costume/era artifact set or handoff path named; N5 = 'history-retaining export' wording absent; N7 = executable-surface reading never pinned as a durable artifact)",
    "origin": "r24",
    "pointer": "reports/round-24/promotion-review.md:178,186,189,193; reports/round-32/dossier-d13-operator-decisions.md:134; reports/round-32/dossier-d11-shonen-boxes.md:207; reports/round-33/calib/K03-open-items.md:68; SKILL.md:583-584,630-632,655-658,694-704",
    "status_quo_check": "2026-10-19, HEAD 139e3b6: r5/r6/r7 run-validation.py exit 1/1/1 in an isolated git-archive copy (7 could-not-evaluate round-3 replay; entry-prefix loss; totals 201/717 + identity collision + r6 cascade); SKILL.md carries zero expected-verdict text at the three imperative sites; history-retaining 0 hits; no reading-pin artifact found",
    "disposition_class": "carried-with-owner+reason+next-touch",
    "status_at_fragment": "fix-drafted-not-applied",
    "evidence": "reports/round-33/calib/C05-item-05.md §2 rows 1-6, §3; reports/round-24/cold-run-conditions.md C3/C4/C5; reports/round-24/cold-run-fixes.md:26-30",
    "fix_draft": "reports/round-33/calib/C05-item-05.md FD-N1-a/b/c (N1), FD-N4 (N4), FD-N5 (N5)",
    "owner": "C07 owns this row; integrator (round 33) for N1/N4/N5 application; parent/operator for N7",
    "reason": "N1/N4/N5 are pointer-level and bounded, but seats may not edit source; N7 is a parent-owned declaration the lane may not absorb",
    "next_touch": "C07's fragment is authoritative for this row; if it is not landed, the integrator may lift these drafts — apply FD-N1-a/b/c + FD-N4 + FD-N5, re-run the named controls and the isolated acceptance control, then flip to fixed-with-evidence; parent issues the N7 reading pin",
    "class_flips_to": "fixed-with-evidence on application + green control"
  }
]
```

Cross-coverage drafts for the neighbouring canonical rows, owned by their own
seats and aggregated by C14: box-1 condition 2 = OI-04 (seat C04,
`FD-B1C2-a/b`) and box-1 condition 4 = OI-06 (seat C06, `FD-B1C4-a/b/c`, one
cell `to-verify`) — §5.

## 8. Collision and honesty notes

- **C14 overlap is by design.** `claims.json:46` assigns C14 "the three box-1
  citation pointer fixes in SKILL.md, N1 expected-verdict errata" — the same
  content drafted here. This fragment's drafts exist so that item 5 is
  dispositioned regardless of how the twelve are numbered; **C14 must remain
  the single aggregator** and C13 must not file a duplicate-disposition defect
  over this overlap. Where C14's wording differs, C14's wins.
- **Sibling-seat overlap is also by design.** K03's seat map (`K03:75-78`) puts
  OI-04 with C04, OI-06 with C06 and OI-07 with C07; §3 and §5 cover those
  rows' content only because they were the alternate item-5 candidates while
  K03 was unlanded. C13 should read them as cross-coverage: OI-04, OI-06 and
  OI-07 are each dispositioned once, by their own seats, and this fragment's
  rows for them are corroboration, not a second disposition.
- No promotion, canon, clearance or closure language is claimed anywhere in
  this fragment; classes are ledger bookkeeping, not verdicts on any round.
- Nothing here edits filed bytes; §6's `to-verify` is the only unresolved
  observation and it owes no lane action.
- This seat claims no authority over the 12-item enumeration, the count
  provenance, or any disposition other than item 5's content.

## Owed

- K03's canonical table **landed during this run**
  (`reports/round-33/calib/K03-open-items.md`, 131 lines) and is reconciled in
  §1 and §7 — item 5 = OI-05; no row rework is owed.
- `reports/round-33/calib/C14-fix-drafts.md` — C14 must absorb or supersede
  `FD-B1C3-a/b` (item 5, OI-05) and, for the cross-covered rows,
  `FD-N1-a/b/c`, `FD-N4`, `FD-N5`, `FD-B1C2-a/b`, `FD-B1C4-a/b/c`, so the
  applied-draft record has one owner.
- `reports/round-33/calib/C13-consistency.md` — cross-check that item 5 is
  dispositioned once, with the §8 overlap note applied.
- Integrator application of the drafted edits + the named controls (the
  counting command `test -s reports/round-33/calib/C05-item-05.md` passes as
  of this write; the C-claim's ledger legs are C15's to run).

## Citations

- `REGIMEN.md:25-50` (per-round contract), `reports/round-33/claims.json:40-51`
  (claim C), `reports/round-33/targets.json:35` (seat C05), `:5-11` (shared rules)
- `reports/round-32/dossier-d13-operator-decisions.md:123-138` (Decision 4
  table; row 5 at `:134`), `:15-52` (Decision 1 box-1 conditions)
- `reports/round-32/dossier-d11-shonen-boxes.md:203-208` (open-at-HEAD table),
  `:42-79` (box-1 condition status), `:131-167` (box-3 N-item status), `:150`
  (N4/N5/N7 "remain as filed")
- `reports/round-24/promotion-review.md:71-88` (box-1 conditions 2-5),
  `:176-195` (box-3 N1-N7)
- `reports/round-24/cold-run-conditions.md` §A (executable baseline), C3
  (acceptance scripts exit 1), C4 (in-place receipt overwrite), C5
  ("isolated repo export" undefined)
- `reports/round-24/cold-run-fixes.md:26-30` (fix/condition map: N1, N2, N4,
  N5, N7, B-F5)
- `SKILL.md` — `:128`, `:479`, `:481`, `:483`, `:486`, `:488`, `:491`, `:501`,
  `:573`, `:583-584`, `:590-598`, `:630-632`, `:655-658`, `:694-704`; sha256
  `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d` (715 lines)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:179`, `:183`
  (0 hits for boilerplate/basis/witness in that file)
- `corpus/knowledge/synthesis/loanword-material-dating.md:26` (blank), `:30`,
  `:57`, `:59`, `:60`, `:63`, `:112`
- `tools/d2-typed-labels.py:48`, `:410`, `:421-427`, `:798-814`, `:1840`,
  `:2239-2257`
- `tools/harness/packet_uncertainty.py:45`, `:84`
- `reports/round-15/claims.json:14`; `reports/round-15.md:108` (selftest
  19/19 incl. boilerplate rule)
- `reports/round-10/drift/shard-05.md:46`, `:54` (filed anchor re-point
  recommendation)
- `reports/round-29/recount/` (devin could-not-evaluate, adjacent item only);
  `reports/round-24/box2-d4.md:104-108` (adjacent item only)
- Commands run 2026-10-19 (all in `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  `TMPDIR=$PWD/.scratch`):
  `find reports/round-33 -type f`; `git rev-parse HEAD`; `git status --porcelain`;
  `git diff HEAD --stat -- reports/round-{5,7}/validation.json`;
  `git hash-object reports/round-{5,7}/validation.json`;
  `git rev-parse HEAD:reports/round-{5,7}/validation.json`;
  `stat -c '%n mtime=%y' reports/round-{5,7}/validation.json`;
  `git archive HEAD | tar -x -C .scratch/c05-iso` (2655 files);
  `python3 reports/round-{5,6,7}/run-validation.py` inside `.scratch/c05-iso`
  (exit 1/1/1) + `cmp` against `git show HEAD:…` (CHANGED ×3);
  `grep -n "run-validation.py" SKILL.md`; `grep -n -i "history-retaining" SKILL.md` (0);
  `for t in TL-01 TL-02 FIELD_DEFAULTS fictional-coordinate descriptive-gloss; do grep -c -- "$t" tools/d2-typed-labels.py; done` (0 ×5);
  `grep -rn -i "boilerplate" .` (no contract hits);
  `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d{2,3,4}/packet*.yml`
  (0 / 1 with R-01 / 0); `sha256sum SKILL.md`; `wc -l SKILL.md`
