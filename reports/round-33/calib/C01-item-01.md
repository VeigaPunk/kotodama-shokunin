- Seat: C01 | executor | claim C | date 2026-10-19 | baseline 139e3b6

# C01 — disposition of open item 1

**Dependency reconciliation.** `reports/round-33/calib/K03-open-items.md` had not
landed at this seat's evidence cut (`ls reports/round-33/calib/` → empty,
2026-10-19T03:52Z), so item 1 was derived from the authoritative enumeration
K03 is chartered to canonicalize — `reports/round-32/dossier-d13-operator-decisions.md`
Decision 4, table row 1 (`:130`) — and cross-checked against the second
enumeration in `reports/round-33/claims.json:44`. **K03 landed at 03:55Z and was
read before this fragment closed.** Reconciliation result:

- K03's canonical id for this item is **`OI-01`**, and K03's own seat mapping is
  explicit: "C01↔OI-01 … in this order" (`calib/K03-open-items.md:75`).
- K03's OI-01 row reads "12 D4 garment-form holds + the six owed form slots",
  origin r18, class `design-debt`, pointers
  `reports/round-24/box2-d4.md:104-108` + `reports/round-22/bleed/verification.json:607`
  (`calib/K03-open-items.md:62`) — **identical** to this seat's independent
  derivation (§2a-2c), including the "six owed form slots" reading that §2c
  proves arithmetically (12 holds = 6 slots × 2 keyings).
- K03 independently classifies OI-01 as a carry candidate: "OI-01..OI-03,
  OI-08..OI-12 are the carry candidates (owner+reason+next-touch required)"
  (`calib/K03-open-items.md:76-78`) — the same disposition class reached here
  from the gate/tool evidence (§3a). Two independent routes, same class.
- **Vocabulary note for C13/C15.** K03's `class` column uses the domain
  vocabulary (`design-debt` for OI-01, `calib/K03-open-items.md:57-58`); the
  claim-C ledger's `disposition_class` uses
  `{fixed-with-evidence, carried-with-owner+reason+next-touch}`
  (`reports/round-33/claims.json:46`). These are different fields, not a
  contradiction: OI-01 is `design-debt` **and** `carried-…`. C15 must emit both,
  or map explicitly.
- **Cross-reference on K03's own caveat.** K03 flags the source of the numeral
  "12" as `to-verify` and names the contamination path: "the table's own first
  row, '**12** D4 garment-form holds' … which carries the numeral 12 as a *hold
  count*, not an item count" (`calib/K03-open-items.md:45-53`). That first row
  **is** OI-01. This fragment supplies the independent confirmation K03's caveat
  needs: §2c establishes the 12 is a hold count over 6 slots keyed twice
  (`reports/round-18/d4/holds.md:99-102`), and §2d shows no filed prose misuses
  it as an item count. So the collision is a numeral coincidence, not a
  membership error — recorded for R05/C13.

## 1. Item 1 — identity

| field | value |
|---|---|
| id | **`OI-01`** (K03 canonical, `calib/K03-open-items.md:62`); this seat's working label `C01-D4-GARMENT-HOLDS` |
| item | 12 D4 garment-form holds + owed slots (six owed garment forms) |
| origin | r18 (design debt by design) |
| class (K03 domain vocabulary) | `design-debt` |
| D13 pointer | `reports/round-24/box2-d4.md:104-108` |
| D13 text | "12 D4 garment-form holds + owed slots \| r18 (design debt by design)" — `reports/round-32/dossier-d13-operator-decisions.md:130` |

## 2. Status quo re-verified at HEAD (dated commands, all 2026-10-19)

HEAD at every command below: `139e3b662900557afe54f632b468619593dc9fcb`
(`git rev-parse HEAD`), identical to the round's declared baseline
(`reports/round-33/claims.json:8`). Working tree state before this seat's writes:
`M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/` — no lane source byte dirty.

**2a. The pointer resolves and still says what D13 says it says — VERIFIED.**

```
$ awk 'NR>=104 && NR<=108 {printf "%d\t%s\n", NR, $0}' reports/round-24/box2-d4.md
104	- **F3 (note): 12 open GAR form holds remain design findings** on the D4
105	  packet (six owed garment forms). They do not fail the gate, are named in
106	  the receipt limits ("Green gates do not clear the six owed garment forms",
107	  `verification.json:607`), and predate this round. Recorded so the promotion
108	  dossier does not read the 19/19 as a content clearance.
```

The pointer is exact (lines 104-108 = the F3 note, whole). `sha256sum
reports/round-24/box2-d4.md` = `20c1732d808b5862ee50bfa7037eff9a59fd50927a7d3a06bd7619010806ffe3`,
116 lines. The cited `verification.json:607` also resolves — it is
`reports/round-22/bleed/verification.json:607`, reading verbatim: `"Green gates
do not clear the six owed garment forms or establish lore acceptance."`
(`reports/round-22/bleed/verification.json:605-609` is the receipt's `limits`
array; the same line is byte-identical at
`reports/round-22/bleed/evidence/attempt-01-verification.json:607`).

**2b. The debt itself is still live and still 12 — VERIFIED by re-execution.**

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-19T03:54:58Z
$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
exit=0
stdout bytes 2213, sha256 865bb03e1694dc0f98a22eb2e44faab720eb1982632ec1ef04030c507a08ecba
$ grep -c "D2L-FORM-UNRESOLVED" <stdout>   → 12
$ grep -E "^ok +L1-expected-holds|^ok +L3-holds|^ok +L3-counts|summary:" <stdout>
ok   L1-expected-holds
ok   L3-holds
ok   L3-counts
summary: 20/20 legs passed
```

The 12 emitted holds are `GAR-01..GAR-06` and `LEX-GAR-01..LEX-GAR-06`, each
`D2L-FORM-UNRESOLVED` / severity `hold`, detail `label_id LEX-GAR-0n has no
supplied native/borrowed form`. The stdout digest `865bb03e1694dc0f…` is
**identical** to the filed r31 sweep row for this exact command
(`reports/round-31/final-sweep.md:62`, digest cell `865bb03e1694dc0f…`) — so the
debt is byte-stable across r31→r33, not drifting.

**2c. The 12 holds are the *pinned expectation*, not an incidental emission —
VERIFIED.** This is the load-bearing fact for the disposition.

- `examples/culture-d4/expected-holds.json` `counts` = `{"hold": 12, "note": 0,
  "fail": 0}`, with exactly 12 rows in `holds[]`, ids `GAR-01..06` +
  `LEX-GAR-01..06` — the same 12. `active_pin_generation` =
  `round-30-qreg-records`.
- The gate's equality legs (`L1-expected-holds`, `L3-holds`, `L3-counts`,
  `L3-details`, `L3-baseline`) are all green at HEAD, i.e. emitted == expected.
- The pinned `packet_sha256` matches the live packet:
  `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` ==
  `sha256sum examples/culture-d4/packet.d4.yml`.
- The packet carries exactly **6** `kind_owed: "native-form"` slots
  (`examples/culture-d4/packet.d4.yml:2496,2502,2508,2514,2520` and one
  `borrowed-strata` at `:2526`; `grep -c kind_owed` = 6) and the 6 `form_slot:
  LEX-GAR-0n` bindings (`:1967,1985,2003,2021,2039,2057`).
- The arithmetic is stated on the record at `reports/round-18/d4/holds.md:99-102`:
  "The 12 form rows are one hold per owed slot, keyed twice: once at the garment
  record id (`where: GAR-0n`) and once at the owed slot's own projected record
  (`where: LEX-GAR-0n`)." So **12 holds = 6 owed slots × 2 keyings** — the
  "+ owed slots" in D13's row is the same six slots, not an additional set.
- The 12 is additionally **hard-pinned inside tool code**: the typed gate's own
  selftest asserts it —
  `tools/d2-typed-labels.py:2998`:
  `len(current["findings"]) == 12 and all(row["id"] == D2L_FORM and row["severity"] == "hold" for row in current["findings"])`.
  `python3 -B tools/gates/typed-pipeline-gate.py --selftest` → exit 0 (19/19).

**2d. Filed prose stating the count is still accurate at HEAD — VERIFIED, no
erratum owed.** `reports/round-24/promotion-review.md:224-226` reads "the fix
must not be read as resolving D2's historical rank debts or filling D4's owed
terms (15 D2 holds + 1 note; 12 D4 garment/slot holds remain open by design)".
Both halves re-measure true today:
`examples/culture-d2/expected-holds.json` `counts` = `{"hold": 15, "note": 1,
"fail": 0}` and the D2 gate re-runs exit 0 with 15 FINDING lines. The parallel
statements at `reports/round-24/box4-bleed.md:134` and `SKILL.md:316` ("the six
owed garment forms remain") also hold. **No count drift to correct.**

## 3. Disposition

**Class: `carried-with-owner+reason+next-touch`.**

### 3a. Why not `fixed-with-evidence` — the fixability test, run honestly

I tested for a bounded, in-scope fix and found none. Four independent blockers,
each command-backed:

1. **The holds are the pinned expectation, so "fixing" them is a repin cascade,
   not a correction.** `expected-holds.json` `counts.hold = 12` and the
   equality legs are green (§2c). Reducing the hold set requires new expected
   bytes plus a new pin generation — the r22→r25 repin-cascade recipe, not a
   pointer edit.
2. **The 12 is hard-asserted in tool code.** `tools/d2-typed-labels.py:2998`
   asserts `len(findings) == 12`. Any fix must edit tool source and that
   selftest, not a report.
3. **The real fix is content, not bookkeeping.** The holds exist because six
   garment terms have no supplied native/borrowed form
   (`kind_owed: "native-form"`, `packet.d4.yml:2496-2526`). Clearing them means
   *authoring six D4 lexemes* — domain content generation. Round-33's non-goals
   forbid canon-adjacent verdicts (`reports/round-33/claims.json:66-71`) and the
   claim-C contract reserves source edits to the integrator
   (`reports/round-33/claims.json:42`); a seat cannot author this and should not.
4. **The record itself forbids the shortcut.** `SKILL.md:478` names the
   anti-pattern explicitly: "never rename the garment to 'fix' the gate". And
   the receipt limit at `reports/round-22/bleed/verification.json:607` states
   "Green gates do not clear the six owed garment forms". A seat "fixing" this
   would be manufacturing a green, which is the exact failure mode the item is
   recorded to prevent.

### 3b. Disposition record

| field | value |
|---|---|
| id | **`OI-01`** (K03 canonical, `reports/round-33/calib/K03-open-items.md:62,75`); this seat's working label `C01-D4-GARMENT-HOLDS` |
| item | 12 D4 garment-form holds + owed slots (6 owed forms keyed twice) |
| origin | r18 — `reports/round-18/d4/holds.md:82-93,99-102` |
| class (K03 domain vocabulary) | `design-debt` (`reports/round-33/calib/K03-open-items.md:62`) |
| pointer (re-verified) | `reports/round-24/box2-d4.md:104-108`; secondary `reports/round-22/bleed/verification.json:607`; `reports/round-24/promotion-review.md:224-226` |
| status_quo_check | re-verified at HEAD `139e3b6`, 2026-10-19T03:54:58Z — 12 holds emitted, exit 0, stdout sha256 `865bb03e…` == r31 sweep digest; expected counts hold:12; 6 `kind_owed` slots; pointers resolve (§2) |
| disposition_class | `carried-with-owner+reason+next-touch` |
| evidence | `reports/round-33/calib/C01-item-01.md` §2a-2d; `reports/round-31/final-sweep.md:62`; `examples/culture-d4/expected-holds.json` `counts`; `examples/culture-d4/packet.d4.yml:2496,2502,2508,2514,2520,2526`; `tools/d2-typed-labels.py:2998` |
| fix_draft | none — see §3a; no bounded fix exists in round-33 scope |
| owner | **operator** (D13 Decision 4 preamble: "owner unassigned (operator's call: future regimen, manual pass, or accepted-as-recorded)" — `reports/round-32/dossier-d13-operator-decisions.md:125-126`) |
| reason | design debt by design: the 12 holds are the frozen expectation (`expected-holds.json` counts.hold=12, equality legs green) and the 12 is asserted in tool code (`tools/d2-typed-labels.py:2998`); clearing them requires authoring six D4 garment lexemes — content generation, outside a calibration disposition and outside round-33's no-canon non-goals |
| next_touch | (a) operator Decision-4 call at regimen-2 close; or (b) a future regimen's D4 content pass, which must land as: author the six `kind_owed: native-form` forms at `examples/culture-d4/packet.d4.yml:2496-2526`, regenerate `expected-holds.json` under a new `active_pin_generation`, update `tools/d2-typed-labels.py:2998`, and re-run `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` expecting `counts.hold = 0` with `L3-holds` green |

### 3c. Named finding from this seat (calibration-relevant, not fixable)

**C01-F1 (minor, filed-byte pointer drift — record only, do not edit).**
`reports/round-18/d4/holds.md:101` cites `tools/d2-typed-labels.py:793` as the
hold's emit site. At HEAD that line is `if label.get("kind") in SOUND_KINDS and
status == "supplied":`; the `D2L_FORM` emits are at
`tools/d2-typed-labels.py:810` and `:813` (`D2L_FORM = "D2L-FORM-UNRESOLVED"`
defined at `:422`, registered `:419`). The drift is expected — the file was
written at r18 head — and is **not** an item to fix: r18 is a filed round and
its bytes are append-only (`targets.json` shared rule 2). Recorded so a future
reader does not follow `:793` and conclude the emit path vanished. Verification:

```
$ grep -n "D2L_FORM\|FORM_UNRESOLVED" tools/d2-typed-labels.py
419:FINDING_CLASSES = ("D2L-DATA", "D2L-FORM-UNRESOLVED", "D2L-NATIVE", "D2L-BORROW",
422:D2L_FORM = "D2L-FORM-UNRESOLVED"
810:            _fail(findings, D2L_FORM, label.get("id"),
813:            _fail(findings, D2L_FORM, label.get("id"),
```

**C01-F2 (observation, informational).** The r22 receipt's stdout tail read
`summary: 19/19 legs passed`; at HEAD the same command reads `20/20` because
`L3b-argot` was added by the r27/r28 register-law program (`SKILL.md:418`). The
19/19 phrasing survives in `reports/round-24/box2-d4.md:13` (review-scope line)
and `:103` ("exit 0, 19/19") as a historical reading. The *digest* is the
durable identity, not the leg count: `865bb03e…` is unchanged r31→r33. Not a
defect; noted so the integrator does not read 19-vs-20 as drift.

## 4. What this seat did not do

- No source byte edited. No file written outside
  `reports/round-33/calib/C01-item-01.md` and `.scratch/`.
- No git commit or push (`git status --porcelain` before and after this write
  shows only the pre-existing `M LOG.md` / `?? REGIMEN.md` /
  `?? reports/round-33/`).
- No promotion, canon, clearance or closure verdict: a green gate is integrity,
  never truth (PROVINCE.md; `reports/round-22/bleed/verification.json:607`).
- No edit to any filed round-1..32 byte, `corpus/lessons/*.md`,
  `tools/gates/frozen/**`, or fleet `.ufo/**`.
- Nothing here asserts that the 12 holds should be cleared, or that they should
  not — the decision is the operator's (§3b `owner`).

## 5. Cross-check — all nine D13 Decision-4 rows re-verified at HEAD

Filed as an independent cross-check of K03's canonicalization: the nine D13
pointers were each resolved at HEAD (`139e3b6`, 2026-10-19) independently of
K03, and all nine resolve. This is a pointer-existence check, not a
disposition. It doubles as the re-map hedge in case K03 had ordered rows
differently — K03's adopted convention (box-1 → 3 rows, lore-owned → 2 rows,
cold-run cluster kept as one) leaves row 1 = `OI-01` unmoved
(`calib/K03-open-items.md:36-43,62`).

| D13 row | item (`dossier-d13-operator-decisions.md:130-138`) | D13 pointer | resolves at HEAD | first line read |
|---|---|---|---|---|
| 1 | 12 D4 garment-form holds + owed slots | `reports/round-24/box2-d4.md:104-108` | YES (exact) | `- **F3 (note): 12 open GAR form holds remain design findings** on the D4` |
| 2 | `head2` empty proper domain | `reports/round-26/register/` named gaps | YES → `reports/round-26/register/design.md:228` | "RL-2 \| head2 has an empty proper domain: 59 of 62 delivered forms are ≤2 syllables …" |
| 3 | RL-3 register-lexicon ceiling | ceilings knowledge entry | YES → `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` | "KTD-RLC-S-0001 — reports/round-27/law/design.md §3.2 and reports/round-27/law/review.md §4 (RL-3) …" |
| 4 | box-1 citation conditions 2-4 | `promotion-review.md:71-88` | YES (exact) | "2. Loanword-dating cite cluster (both reviewers; re-confirmed by this scribe …" |
| 5 | cold-run N1/N4/N5/N7 | `promotion-review.md:176-196` | YES (exact) | "### Conditions" then "1. N1 (major): dated expected-verdict errata …" |
| 6 | lore-owned: bilateral read + L0 contract-digest | L0 queue; handoff contract | YES → `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45` (kotodama rows round-2, round-8) + `corpus/knowledge/synthesis/worldbible-integration-contract.md` (28421 bytes, header line 1) | fleet file is read-only (out of lane) |
| 7 | calibrated numeric rubric undefined | `SCORECARD.md` header | YES → `SCORECARD.md:12-14` | "They remain historical in Git, not new numeric claims. … defining a calibrated numeric rubric remains an explicit protocol-conformance gap." |
| 8 | devin availability could-not-evaluate | `reports/round-29/recount/` | YES (dir, 18 files incl. `ledger.json`, `dispositions.md`, `audit.md`) | — |
| 9 | r18 D4-adapter baseline supersession semantics | `final-sweep.md` §5 | YES → `reports/round-31/final-sweep.md:183-196` | `## 5. Scope notes — what this seat did not do` / `**The D4 adapter baselines were not re-pinned.** …` |

Note for the integrator: D13's row 2 pointer is a *directory* plus the phrase
"named gaps"; the load-bearing line is `register/design.md:228` (RL-2), and
`reports/round-26/register/review.md:1` is titled "…the named gaps". D13's row 6
pointer spans a fleet-root file (read-only) and a corpus file — the fleet half
cannot be re-verified as writable and is out of lane. K03 resolved rows 2, 3, 6,
8 and 9 to the same lines this seat did (`calib/K03-open-items.md:63,64,69,70,72,73`),
with one refinement: K03 gives row 8's load-bearing pointer as
`reports/round-29/recount/dispositions.md:22` (item 16) and `audit.md:18`
(item 12) rather than the bare directory.

## Owed

- **none.** The K03 dependency landed at 2026-10-19T03:55Z and was reconciled
  before close (see the dependency reconciliation note at the head of this
  fragment): K03's `OI-01` matches this seat's independently derived item
  identity, origin and both pointers, and K03's own seat mapping fixes
  `C01↔OI-01` (`calib/K03-open-items.md:62,75`).
- Handoff notes for C13/C15 (not owed work by this seat, recorded so the ledger
  does not have to re-derive them): the `fix_draft` field is deliberately
  **absent** rather than empty-string, so `C15-ledger-draft.json` should emit no
  `fix_draft` key for `OI-01`; and `OI-01` carries both vocabularies — K03
  `class: design-debt` and claim-C
  `disposition_class: carried-with-owner+reason+next-touch`.
- Residual `to-verify`, inherited from K03 and not resolvable by this seat: the
  provenance of the numeral "12" as an *item* count stays `to-verify`
  (`calib/K03-open-items.md:45-53`). This fragment narrows it — the "12" in
  `OI-01`'s own wording is a *hold* count, proven at §2c — but does not settle
  K03's expansion-rule question, which is R05's to check.

## Citations

Files read (all at HEAD `139e3b662900557afe54f632b468619593dc9fcb`):

- `reports/round-32/dossier-d13-operator-decisions.md:123-138` — Decision 4 table, rows 1-9; `:125-126` owner preamble
- `reports/round-32/dossier-d11-shonen-boxes.md:114-118,203-208` — box-2 standing design debts restatement
- `reports/round-33/claims.json:42,44,66-71` — claim-C after_required, item enumeration, non-goals
- `reports/round-33/targets.json:31` — C01 mission; `:5-11` shared rules
- `reports/round-33/calib/K03-open-items.md` — the canonical twelve; read in full at close (11902 bytes, mtime 2026-10-19T00:55:49-03:00, sha256 `fe0b11cc869f96e685b594af11be104c8d38ca6cea4b99095eaf8ee135dae578`). Lines relied on: `:45-53` (numeral-12 caveat), `:57-58` (class vocabulary), `:62` (OI-01 row), `:63,64,69,70,72,73` (K03's rows 2/3/6/8/9 pointers), `:75-78` (seat mapping + carry candidates), `:36-43` (counting conventions)
- `reports/round-24/box2-d4.md:1-16,104-108` (sha256 `20c1732d808b5862ee50bfa7037eff9a59fd50927a7d3a06bd7619010806ffe3`, 116 lines)
- `reports/round-24/promotion-review.md:71-88,114-115,176-196,224-226`
- `reports/round-24/box4-bleed.md:134`
- `reports/round-18/d4/holds.md:82-93,99-102,113,118-120`
- `reports/round-22/bleed/verification.json:600-609` (limits array; `:607` the garment-forms line) and `reports/round-22/bleed/evidence/attempt-01-verification.json:607`
- `reports/round-31/final-sweep.md:57,62,183-196`
- `reports/round-26/register/design.md:228` (RL-2); `reports/round-26/register/review.md:1`
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6,19` (RL-3)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md` (header, 28421 bytes)
- `SCORECARD.md:12-14,622-626` (rubric gap)
- `examples/culture-d4/expected-holds.json` — `counts {hold:12,note:0,fail:0}`, 12 `holds[]`, `active_pin_generation round-30-qreg-records`, `packet_sha256 aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`
- `examples/culture-d4/packet.d4.yml:167-198,1965-2057,2493-2526` — hold `where`/`reason` block, `form_slot` bindings, `kind_owed` slots
- `examples/culture-d2/expected-holds.json` — `counts {hold:15,note:1,fail:0}`
- `tools/d2-typed-labels.py:419,422,810,813,2998`
- `SKILL.md:167,266,316,418,478,500`
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45` (fleet root, read-only)

Commands run (dated 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`
- `git status --porcelain` → ` M LOG.md` / `?? REGIMEN.md` / `?? reports/round-33/`
- `git log --oneline -3` → `139e3b6`, `cdd66d7`, `4d50050`
- `sha256sum reports/round-24/box2-d4.md` → `20c1732d808b5862ee50bfa7037eff9a59fd50927a7d3a06bd7619010806ffe3`
- `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0, 2213 stdout bytes, sha256 `865bb03e1694dc0f98a22eb2e44faab720eb1982632ec1ef04030c507a08ecba`, 12 `D2L-FORM-UNRESOLVED`, `summary: 20/20 legs passed`, `ok L1-expected-holds`, `ok L3-holds`, `ok L3-counts` (2026-10-19T03:52:56Z and re-run 03:54:58Z)
- `python3 -B tools/gates/typed-pipeline-gate.py --selftest` → exit 0, `selftest: 19/19 checks passed`
- `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml` → exit 0, 15 FINDING lines
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → exit 0
- `sha256sum examples/culture-d4/packet.d4.yml` → `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` (== pinned)
- `grep -c "kind_owed" examples/culture-d4/packet.d4.yml` → 6; `grep -c "form_slot"` → 10
- `grep -c "D2L-FORM-UNRESOLVED"` on the D4 gate stdout → 12
- `grep -n "D2L_FORM\|FORM_UNRESOLVED" tools/d2-typed-labels.py` → `419,422,810,813,2241,2261-2262,2998`
- `grep -rn "12 open\|12 D4\|six owed" reports/round-1[89]/ reports/round-2[0-9]/ reports/round-3[0-2]/ LOG.md SCORECARD.md` — count-drift scan (§2d)
- `ls -la reports/round-33/{calib,op,adj,cross,review,scribe}/` → all six empty at 2026-10-19T03:52Z (this seat's evidence cut); at close `calib/` held `C01-item-01.md`, `C07-item-07.md`, `C12-item-12.md`, `C16-receipt.md`, `K03-open-items.md`, `P02-plan.md`
- `sha256sum reports/round-33/calib/K03-open-items.md` → `fe0b11cc869f96e685b594af11be104c8d38ca6cea4b99095eaf8ee135dae578`
- `awk 'NR==45||NR==62||NR==75||NR==76||NR==77||NR==78' reports/round-33/calib/K03-open-items.md` — spot-check of every K03 line cited above
- `ls -1 reports/round-29/recount/ | wc -l` → 18
- `git status --porcelain` (after all writes) → unchanged: ` M LOG.md` / `?? REGIMEN.md` / `?? reports/round-33/`
