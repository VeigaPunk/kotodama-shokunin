- Seat: A04 | executor | claim A | date 2026-10-19 | baseline 4a7aede

# A04 — audit slice: the rounds-33/34 `SKILL.md` edits (C14 fixes, O05 re-key, N1/N4/N5) + the `AGENTS.md` excision

Write scope: this file only (`reports/round-35/adj/A04-skill-agents.md`). No source file was
edited by this seat. Every command ran either in-tree read-only or inside isolated copies
(`.scratch/a04-iso` = `git archive HEAD`, `.scratch/a04-clone{,2,3}` = `git clone
--no-hardlinks`, `.scratch/a04-fixture` = a synthetic `reports/round-90|91/` tree). **No
`reports/round-*/run-validation.py` was executed in-tree** (F-C13-1); the three acceptance
re-runs live in §6/A04-3 and ran only in clones. Dependency `scout/K04-touched-census.md`
landed and is cited where it agrees.

## 1. Surface set — what rounds 33–34 actually touched

| surface | touched by | delta | state at HEAD | evidence |
|---|---|---|---|---|
| `SKILL.md` | round 33 only | +35 / −18 | 732 lines, sha256 `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | `git log --oneline cdd66d7..4a7aede -- SKILL.md` → `da68a6d` alone |
| `AGENTS.md` | round 33 only | +0 / −2 | 40 lines, sha256 `5ae7a9c8abab0843cfc6db09849f2fff369c0e880085deb546ec7ab764333808` | `git log --oneline cdd66d7..4a7aede -- AGENTS.md` → `da68a6d` alone |

Round 34 touched neither file: `git diff --stat 4a7aede..HEAD -- SKILL.md AGENTS.md` is empty,
`git diff --unified=0 cdd66d7..4a7aede -- SKILL.md` shows thirteen hunks (`:128`, `:479`, `:481`,
`:483`, `:486`, `:488`, `:491`, `:501`, `:584`, `:696`, `:702`, `:709`, `:730`), and round 34's
`targets.json` names `SKILL.md` 3× as a read-only surface only. K04's census
(`scout/K04-touched-census.md:39-40`) agrees on paths, rounds and deltas; its `R1/R2` risk
classes (ownership strain at `PROVINCE.md:11`/`:20`) are answered in §5.

Both HEAD digests equal the readings the round-33 assembled audit already recorded
(`adj/audit-assembled.md:41`), so nothing on these two surfaces drifted during round 34.

## 2. Applied-edit inventory — every landed edit against its draft

| # | edit | draft source | landed at HEAD | verdict |
|---|---|---|---|---|
| 1 | loanword-dating cite cluster | `calib/C14-fix-drafts.md` §Fix 1 Drafts 1a/1b | `:486` → `:30-31,63`; `:488` → `:59,63` | **verbatim** (the recommended variants; C04's smaller `:30,63`/`:59`-only subsets were not taken) |
| 2 | `worldbible-integration-contract.md:183` mis-cite | C14 §Fix 2 Drafts 2a/2b | `:128`, `:501` → `packet_uncertainty.py:205,209` + dated erratum | **verbatim**; `grep -c "worldbible-integration-contract.md:183" SKILL.md` → 0 |
| 3 | dangling tool anchors | C14 §Fix 3 Drafts 3a-3d | `:479`, `:481`, `:483`, `:491` | **verbatim**; Draft 3d landed in the **full** variant, not the minimal one |
| 4 | cold-run N1 expected-verdict errata | C14 §Fix 4 (r7 site) | `:709-720` | **verbatim** — but stale at HEAD, see A04-3 |
| 5 | N4 real operands | `calib/C05-item-05.md` FD-N4 | `:696-700` | **verbatim** |
| 6 | N5 history-retaining export | C05 FD-N5 | `:583-586` | **verbatim**; `grep -c "history-retaining" SKILL.md` → 1 |
| 7 | falsifier re-key (F-X16-3) | `op/O05-falsifier-disposition.md` §3b | `:730-732` | **verbatim** (4 physical lines, one-line command); live run → 0 rows, rc=0 — but see A04-1 |
| 8 | C14 Fix 5a/5b (conditional extras) | C14 §Fix 5 | `:485`, `:213` unchanged | **correctly not applied** — C14 scoped them "apply only on explicit instruction" |

Retired anchors survive only as dated erratum mentions, never as live authorities:
`TL-01` ×2 (`:479`, `:481`), `TL-02` ×1 (`:483`), `FIELD_DEFAULTS` ×1 (`:491`), each inside a
clause reading "erratum 2026-10-19: retired anchor …".

**Pointer resolution — every new citation, resolved at HEAD (nothing marked `to-verify`):**

| pointer | resolves to |
|---|---|
| `tools/harness/packet_uncertainty.py:205,209` | `"U-BASIS-BOILERPLATE"` / `"U-BASIS-RESTATES"` |
| `reports/round-15/handoff/v2-design.md:126,131-139` | `### 2.3 Zero-boilerplate: what the builder enforces` … the five builder checks |
| `corpus/knowledge/synthesis/loanword-material-dating.md:30,31,59,63` | Lexical clock row / Material clock row / dictionary-selection-bias row / "Date the **sense–referent pairing**" |
| `tools/d2-typed-labels.py:422` | `D2L_FORM = "D2L-FORM-UNRESOLVED"` |
| `tools/d2-typed-labels.py:500,520,529` | `"kind": "translated-label"` / `"text": None,  # the slot carries a gloss, not a form` / the unfilled-slot issue row |
| `tools/d2-typed-labels.py:549,565` | `"kind": "native-form"` / `base["kind"] = "borrowed-strata"` |
| `tools/d2-typed-labels.py:694-695,774-775` | `_fail(..., D2L_DATA, ... "supplied sound form has no text")` / `"status supplied requires text"` |
| `tools/d2-typed-labels.py:768-769` | `if label.get("kind") not in KINDS:` → `_fail(..., D2L_DATA, ... f"kind {...!r} is not one of {KINDS}")` |
| `tools/d2-typed-labels.py:810-814` | `_fail(findings, D2L_FORM, ... "translated label with no supplied sound form and no label_id", hold=True)` |
| `tools/d2-typed-labels.py:3195` | `check("live packet: no GAR label is graded on the sound channel", …)` |
| `reports/round-11/depth/shard-gate-adapter.md:120-125` | "Design-spec §8.1 proposes a five-kind superset (fictional-coordinate, …)" |
| `reports/supplement-opencode-1/22-label-representation.md:126-128,131-132` | the label-only record and the declared-kind-with-no-bytes rows |
| `corpus/knowledge/linguistics/language-contact.md:80-81` | the two borrowed-form principles (Fix 5a's target — unchanged, correctly) |

## 3. The `AGENTS.md` excision

The excised bytes were the trailing fence plus the orphan heading
`### 2.2 \`SKILL.md\` — append one item to "## Checklist (executable where a tool exists)" (after :534)`,
both landed by round-31's `17e90b9` and named as leaked drafting residue by round 33's own
audit (`adj/A10-receipt.md:77` A10-F15; `adj/A07-history.md:65-68`;
`cross/X02-conformance.md:110-139`; `adj/A15-audit-draft.md:178`).

Verified at HEAD, deletion-only:

- `git diff cdd66d7..4a7aede -- AGENTS.md` → 2 deletions, 0 insertions (no replacement text).
- `wc -l AGENTS.md` → 40; `grep -c '^```' AGENTS.md` → 0; `grep -n "### 2.2\|append one item" AGENTS.md` → no hits.
- The file ends with the telemetry bullet and one trailing blank line (harmless; no dangling fence).
- No re-addition: `git log --oneline cdd66d7..4a7aede -- AGENTS.md` → `da68a6d` only; no live
  residue in-repo outside filed round-33/34 fragments, `corpus/lessons/**`, and `.scratch`
  copies of pre-excision trees.

Adjacency verdict: the excision is a boundary **repair**, not absorption. Read as an
instruction the removed line ("append one item to `## Checklist`") would have collided with the
already-landed item at `SKILL.md:713-715`/now `:730-732` — round 33's `cross/X00-connector.md:68`
records exactly that collision — and its anchor was already 179 lines stale. The removed
content was never this lane's own instruction; nothing in-lane was lost.

## 4. Cross-domain language scan (claim A's core check)

Method: `git diff cdd66d7..4a7aede -- SKILL.md | grep '^+' | grep -v '^+++'` → 35 added lines,
scanned case-insensitively for `canon|promotion|promote|clearance|closure|ratif|absorb|sibling|
lore-shokunin|chousa|kake|kotoba|game-dev|world bible`, then for
`/home/|/Users/|\.\./|\.ufo|shokunin/|lore|sibling|fleet`.

- Exactly **one** hit: `clearance gate` at `:698`. It is a re-wrapped pre-existing negation —
  present at `cdd66d7:696` ("neither is a green clearance gate") and unchanged in meaning; the
  added line is only the new wrapping of FD-N4. **Not new language.**
- **Zero** hits for absolute host paths, `../`, `.ufo`, sibling repos, fleet, lore or the
  refused-domain names (chousa/kake/kotoba/game-dev).
- The only verdict-adjacent new sentences are the N1 errata, which **restate the contents of
  filed receipts** (`acceptance_checks_passed: false`, the F/O causes) rather than issue a
  verdict on any round; checked line-by-line against the filed receipts in A04-3.

## 5. PROVINCE conformance of the new content

Every new reference stays in-lane: this lane's own tools (`tools/d2-typed-labels.py`,
`tools/harness/packet_uncertainty.py`, the handoff/costume gates), its own corpus, its own
`reports/`, its own `examples/`, its own telemetry convention. Concretely:

- No new line cites a lore-owned artifact as authority, and no new line asserts canon,
  promotion, clearance or closure — the one place a lane-adjacent artifact appears
  (`worldbible-integration-contract.md`) appears **only** inside a dated erratum that
  explicitly disclaims its authority ("contract `:183` carries the delivered-record checklist
  item, not basis hygiene"), which is `PROVINCE.md:22-25` (adjacent contract; contested scope
  routed, never absorbed) applied correctly.
- The re-keyed item executes over this lane's own `reports/round-*/` tree only — no sibling
  path, no world-bible path.
- `PROVINCE.md:11` "owns … this lane's own gates, source-check records, non-canon examples and
  reports" covers all seven edits; `PROVINCE.md:20`'s refusal of "prompt/skill craft (kotoba)"
  is not strained, because every edit is pointer hygiene / acceptance-instruction content
  inside this lane's own skill file, not craft for another lane's skill. K04's `R1/R2` risk
  classes are thereby answered: **no ownership drift**.
- The excision removed content that *was* the strained kind (a fleet-channel instruction aimed
  at this lane's SKILL.md), so §3 and §5 reinforce each other.

## 6. Findings

### A04-1 — the re-keyed instrument's record-side glob is still name-and-depth keyed (medium; owner: integrator)

`SKILL.md:730-732` re-keys the **snapshot** side by content (`telemetry/availability-close-*.json`
+ `closes` + `closes_sha256`) — correct, and its live behaviour is green (`rc=0`, 0 rows at HEAD).
But the **record** side is still enumerated by `glob('reports/round-*/availability*.json')`, a
name- *and* depth-keyed pattern.

Live census at HEAD: **7** records carry `state == "open-at-seat-close"`; the glob sees 5
(`reports/round-{19,25,26,27,28}/availability.json`) and cannot see 2 —
`reports/round-33/telemetry/observed-dispatch.json` and
`reports/round-34/telemetry/observed-dispatch.json` (both one directory deeper and differently
named, which is the shape the AGENTS.md telemetry convention prescribes).

Control pair (`.scratch/a04-fixture`, synthetic roots; identical unclosed record bytes, no
snapshot): at `reports/round-90/telemetry/dispatch-declared.json` the landed command prints
**0 rows** (miss, rc=0); the same bytes at `reports/round-91/availability.json` print **1 row**
(fires, rc=0). So the instrument is silent about the record shape the round itself uses, and
its green on the live tree is partly a coverage artifact — the same defect *class* as F-X16-3
(a filename-keyed predicate), relocated to the record side.

Bounded fix for the integrator: enumerate both shapes/depths, e.g.
`glob('reports/round-*/*.json') + glob('reports/round-*/*/*.json')` with the existing
`state == "open-at-seat-close"` filter kept, and add the fixture control above (an unclosed
telemetry-shape record must fire). The item's own wording — "Every availability/**dispatch**
record filed `open-at-seat-close`" — already scopes this, so the fix is a coverage repair, not
a scope change.

### A04-2 — two records filed `open-at-seat-close` have no snapshot naming them (high for the rule; owner: the round-33/34 integrating parents, route via the integrator)

`reports/round-33/telemetry/observed-dispatch.json` and
`reports/round-34/telemetry/observed-dispatch.json` are filed `state: "open-at-seat-close"`;
both rounds' `validation.json` have landed (rounds admitted at `da68a6d` / `4a7aede`). No filed
file names either record in a `closes` field: the rounds' only snapshots close
`dispatch-declared.json` (`availability-close-33.json` → `closes = reports/round-33/telemetry/
dispatch-declared.json`, digest match **True**; same shape for 34). Both snapshots' key sets are
`[closed_fields, closes, closes_sha256, could_not_recover, date, owner, reason, round, schema,
sources]` — **no `also_closes` key exists in the filed bytes**, although round 34's own
telemetry draft anticipated one (`reports/round-34/scribe/S05-telemetry-draft.md:229-231`).

So the rule the item states (and `AGENTS.md`: "a round is not admitted to `LOG.md` while its own
availability record still owes a closing snapshot") is unmet for those two records, and the
instrument cannot report it (A04-1). The observation-dispatch record is *referenced* in the
snapshots' `sources` (provenance) but not *closed*.

**Actionable for round 35, which is about to repeat the shape:** the round-35 telemetry draft
plans `closes: reports/round-35/telemetry/dispatch-declared.json` again
(`scribe/S05-telemetry-draft.md:245-246`) and declares at `:151` that the observed record
"closes when `availability-close-35.json` lands in the same integrating pass". Under the item's
predicate that is not a closure. The integrator should pick one and record it:
(a) file a second append-only snapshot per round whose `closes` names the observed record
(AGENTS.md's correction rule allows new snapshots, never in-place edits), or
(b) extend the item's predicate to accept an `also_closes[]` entry, and then back-fill r33/r34
the same way. No filed byte (`reports/round-1..34/**`) may be edited; this seat wrote nothing
into those rounds.

### A04-3 — the landed N1 errata is stale on its r7 clause at HEAD (medium; owner: integrator)

The landed text (`SKILL.md:716-720`) says the r7 replay fails on preservation, inventory totals,
one claim-F rejection and the round-6 predecessor check "while its O leg passes (5/5, 16/16,
4/4, frozen 5/5)".

Measured independently at HEAD in a fresh `git clone --no-hardlinks` of `4a7aede` (r7 alone,
never in-tree): **exit 1**, `acceptance_checks_passed: false`, `claims.O.passed: false`, and
**five** failure rows — the four named **plus**
`claim O: expected manifest digest drift: ['examples/handoff-packet.sample.md']`.

Cause, measured: `examples/handoff-packet.sample.md` was changed by **`da68a6d`** — round 33,
the very commit that landed this errata (`git log --oneline cdd66d7..4a7aede --
examples/handoff-packet.sample.md` → `da68a6d`). The errata was measured pre-application
(C14's evidence point `139e3b6`), so the clause "its O leg passes" is true of that point and
false at HEAD; the count "one claim-F rejection" likewise undercounts the failure set by one.
The numbers 5/5, 16/16, 4/4, 5/5 do exist in the receipt — as the guard selftest sub-counts —
so the sentence is a *stale reading*, not an invented one.

The other two legs verified **exact** against the landed text:

- round 5 → exit 1; F = `non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')`; O = `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of 7 row(s) in tools/gates/frozen/round-3/MANIFEST.tsv`, every row `reason=gate_digest_mismatch`.
- round 6 → exit 1; `"error": "historical file changed: .gitignore"`.

Fix: a dated successor sentence inside the same block (SKILL.md is not a filed byte), naming the
fifth failure and its cause, or marking the block "measured at `139e3b6`". Either keeps the
erratum executable-by-verdict, which is N1's whole purpose.

### A04-4 — N1 landed at one of its three sites (low; owner: integrator)

`grep -n "Expected verdict" SKILL.md` → a single hit, `:709`. FD-N1-a (`:630-632`, the round-5
site) and FD-N1-b (`:655-658`, the round-6 site) were **not** applied, and the round-33 ledger
declares only the r7 site ("N1 errata APPLIED (C14 Fix 4, SKILL.md:701-704)"). The substance is
present — the consolidated block names a distinct expected verdict for all three rounds, with
the isolation sentence — but a cold reader standing at the round-5 or round-6 imperative still
sees no expected verdict. Recorded as a **partial application**, not a defect in the applied
bytes.

### A04-5 — ledger OI-04's `fix_draft` pointer cites the withdrawn variant (low; owner: A05 slice / integrator — note only, no edit)

`reports/round-33/calib/open-items-ledger.json` OI-04 `fix_draft` reads "Draft 1a (SKILL.md:486
-> ':29,63')", which is C14's **withdrawn** variant; the landed bytes carry `:30-31,63`. The
same row's integrator note records the correct values and the deviation honestly ("C04 §4's
prescriptive control is RED under the erratum variant … recorded as integrator deviation 1").
So the divergence is filed, not hidden — but the `fix_draft` field is now a stale pointer. Filed
artifact; no edit proposed; named for the assembled audit's consistency table.

## 7. Per-surface verdicts

| surface | verdict | basis |
|---|---|---|
| `SKILL.md` C14 Fixes 1–3 (7 lines) | **green** | verbatim drafts; all 14 replacement pointers resolve; retired anchors demoted to dated errata |
| `SKILL.md` Fix 4 (N1 errata) | **named-finding (A04-3, A04-4)** | r5/r6 legs exact; r7 clause stale at HEAD; one of three sites applied |
| `SKILL.md` FD-N4 / FD-N5 | **green** | verbatim; `examples/culture-d3/*` operands exist and behave as documented; `history-retaining` present |
| `SKILL.md` O05 re-key (`:730-732`) | **named-finding (A04-1, A04-2)** | snapshot side correct and green live; record-side glob misses the current record shape; two unnamed open records |
| `AGENTS.md` excision | **green** | deletion-only, complete, no residue, no re-addition, boundary repair |
| cross-domain language on all added lines | **green** | 1 hit, a re-wrapped pre-existing negation; 0 path/sibling/fleet refs |
| PROVINCE conformance of new content | **green** | all references in-lane; the one lane-adjacent artifact appears only inside a disclaiming erratum |

No row claims a promotion, canon, clearance or closure verdict; A04-2 records an *owed* closure
by the lane's own rule, which is a rule-compliance statement, not a closure verdict.

## Owed

none. `reports/round-35/scout/K04-touched-census.md` landed and is cited (§1); the two
independent-verification seats can reproduce every command here from §6 alone.

## Citations

Files read (paths relative to repo root; line numbers at HEAD `4a7aede` unless stated):

- `SKILL.md:128`, `:479`, `:481`, `:483`, `:486`, `:488`, `:491`, `:501`, `:583-586`,
  `:628-636`, `:653-662`, `:694-708`, `:709-720`, `:730-732`; sha256 `f9bd07c2…`, 732 lines
- `AGENTS.md:1-40` (sha256 `5ae7a9c8…`); `git show cdd66d7:AGENTS.md` (42 lines, trailing fence + orphan heading)
- `PROVINCE.md:11`, `:20`, `:22-25`
- `reports/round-35/targets.json:275-280` (seat A04); `reports/round-35/claims.json` (claim A)
- `reports/round-33/calib/C14-fix-drafts.md` §Fix 1-§Fix 5, §'Machine-checkable after-set', §'Application notes'
- `reports/round-33/calib/C05-item-05.md` §2-§5 (FD-N1-a/b/c, FD-N4, FD-N5)
- `reports/round-33/calib/open-items-ledger.json` rows OI-04 (integrator note, `fix_draft`), OI-07 (integrator note)
- `reports/round-33/op/O05-falsifier-disposition.md` §2-§4 (§3b after-bytes, 7-scenario control set, D-4 routing)
- `reports/round-33/adj/A10-receipt.md:77` (A10-F15); `reports/round-33/adj/A07-history.md:39,65-68`;
  `reports/round-33/adj/A15-audit-draft.md:178`; `reports/round-33/adj/audit-assembled.md:30,41`;
  `reports/round-33/cross/X00-connector.md:68,237`; `reports/round-33/cross/X02-conformance.md:110-139`
- `reports/round-33/telemetry/{dispatch-declared,observed-dispatch,availability-close-33}.json`;
  `reports/round-34/telemetry/{dispatch-declared,observed-dispatch,availability-close-34}.json`
- `reports/round-34/scribe/S05-telemetry-draft.md:186-231` (Template B, `also_closes` plan)
- `reports/round-35/scribe/S05-telemetry-draft.md:151,232-246` (round-35 close plan)
- `reports/round-35/scout/K04-touched-census.md:39-40,90`
- `reports/round-5/validation.json` (`claims.F.error`, `claims.O.error`); `reports/round-6/validation.json` (`error`);
  `reports/round-7/validation.json` (`failures`, `claims.O.passed`)
- `tools/harness/packet_uncertainty.py:205,209`; `reports/round-15/handoff/v2-design.md:126,131-139`;
  `corpus/knowledge/synthesis/loanword-material-dating.md:30,31,59,63`;
  `corpus/knowledge/linguistics/language-contact.md:80-81`;
  `tools/d2-typed-labels.py:422,500,520,529,549,565,694-695,768-769,774-775,810-814,3195`;
  `reports/round-11/depth/shard-gate-adapter.md:120-125`;
  `reports/supplement-opencode-1/22-label-representation.md:126-128,131-132`

Commands run (2026-10-19, lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git log --oneline cdd66d7..4a7aede -- SKILL.md AGENTS.md` → `da68a6d` only, both files
- `git diff cdd66d7..4a7aede -- AGENTS.md` → 2 deletions / 0 insertions; `-- SKILL.md` → 11 hunks
- `git diff cdd66d7..4a7aede -- SKILL.md | grep '^+' | grep -v '^+++'` → 35 added lines, scanned as §4
- `wc -l AGENTS.md` → 40; `grep -c '^```' AGENTS.md` → 0; `grep -n "### 2.2\|append one item" AGENTS.md` → no hits
- `sha256sum SKILL.md AGENTS.md`; `wc -l SKILL.md` → 732
- `grep -n "Expected verdict\|worldbible-integration-contract.md:183\|history-retaining" SKILL.md`
- pointer resolution loop over the 14 new citations (content quoted in §2)
- re-keyed one-liner from `SKILL.md:732`, run at HEAD → rc=0, 0 rows
- record census: `python3 -B -c` over `reports/round-*/*.json` + `reports/round-*/*/*.json` filtered
  by `state == "open-at-seat-close"` → 7 records, 2 outside the audit's glob
- fixture control pair in `.scratch/a04-fixture` (unclosed record at the telemetry path → 0 rows;
  same bytes at top level → 1 row)
- `git clone --no-hardlinks . .scratch/a04-clone{,2,3}`; `python3 -B reports/round-{5,6,7}/run-validation.py`
  inside the clones → exit 1 / 1 / 1 with the causes quoted in A04-3 (never in-tree)
- `git log --oneline cdd66d7..4a7aede -- examples/handoff-packet.sample.md` → `da68a6d`
- `python3 -B -c` reading the filed snapshots' key sets and `also_closes` → absent in both
