- Seat: P02 | planner | C (execution plans for claims C and A) | date 2026-10-19 | baseline 139e3b6

# P02 — execution plans for claim C (calibration ledger) and claim A (adjacency audit)

Planning only: this fragment writes no ledger row, no audit verdict, and no
source byte. The mission's two named dependencies — `calib/K03-open-items.md`
(claim C) and `adj/K04-method-scout.md` (claim A) — **do not exist** at this
seat's read time (`ls reports/round-33/calib/ reports/round-33/adj/` → both
empty, 2026-10-19). Everything below is therefore grounded directly in the
round-32 dossiers, the round-21/29 adjacency lineage, the round-33 declaration
files, and this seat's own measurements; the two missing paths are recorded
under `## Owed`.

## 0. Measured state at plan time (2026-10-19, lane root, `TMPDIR=$PWD/.scratch`)

| probe | command | result |
|---|---|---|
| HEAD / baseline | `git log --oneline -3` | `139e3b6` = declared baseline; parents `cdd66d7`, `4d50050` |
| tracked files | `git ls-files \| wc -l` | `2655` — matches the declared baseline count (`claims.json:57`) |
| working-tree delta, first reading (~03:54Z) | `git status --porcelain` | `M LOG.md`, `M reports/round-5/validation.json`, `M reports/round-7/validation.json`, `?? REGIMEN.md`, `?? reports/round-33/` |
| LOG.md delta | `git diff LOG.md` | +18 lines = the regimen-2 / round-33 declaration entry (expected; integrator commits it) |
| r5/r7 receipt delta, first reading | `git diff reports/round-{5,7}/validation.json`; `stat -c '%y %n'` | both **modified 2026-10-19 00:54:32/35 (-0300)** — after the round's `declared_at_utc` 2026-10-19T03:49:01Z; r5 rewrites the `O.error` strings and `tested_file_sha256["tools/check-gate-battery.py"]` `0a126b70…`→`455b595a…`; r7 rewrites the `inventory:` failure counts `189/688/700/702/633`→`201/717/731/733/655` |
| working-tree delta, re-reading `VERIFY_UTC=2026-10-19T03:56:48Z` | `git status --porcelain`; `git diff --stat reports/round-{5,7}/validation.json` (exit 0); `stat -c '%y %n'` | **remediated**: both receipts are back to committed bytes (diff empty, porcelain clean); mtime `00:55:27 -0300` (= 03:55:27Z) ⇒ the dirty window was ≈55 s (03:54:32Z–03:55:27Z), the dirty bytes themselves no longer recoverable from disk — only the diffs quoted above |
| PROVINCE pin | `git log --oneline -2 -- PROVINCE.md`; `git rev-parse HEAD:PROVINCE.md`; `sha256sum PROVINCE.md` | last commit `c53782a`; blob `313b182f251564b7997b06996b4f063370778f11`; sha256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` — A01's expected state |
| round-33 validator | `ls reports/round-33/` | no `run-validation.py` yet — legs below are the spec S04/integrator implements |
| telemetry | `cat reports/round-33/telemetry/dispatch-declared.json` | declaration record present, `closing_snapshot` marked `open-at-seat-close` |

**In-window filed-receipt modification — remediated, must still be recorded.**
At the first reading (~03:54Z, five minutes after the round's
`declared_at_utc` 2026-10-19T03:49:01Z) two filed-round receipt files were
dirty in the working tree: `reports/round-5/validation.json` (its `O.error`
strings and `tested_file_sha256["tools/check-gate-battery.py"]`
`0a126b70…`→`455b595a…` rewritten) and `reports/round-7/validation.json` (its
`inventory:` failure counts `189/688/700/702/633`→`201/717/731/733/655`
rewritten). At `VERIFY_UTC=2026-10-19T03:56:48Z` both files again match HEAD
byte-for-byte (`git diff --stat` exit 0, `git status --porcelain reports/round-5
reports/round-7` empty; mtime `00:55:27 -0300`), so the dirty window was ≈55 s
and the dirty bytes are no longer on disk — only the diffs quoted in §0 survive.
`tools/harness/receipt_guard.py:7` says only `REFRESH_RECEIPTS=1` permits a
committed-receipt overwrite, so a refresh path ran in-window; this is the same
class as r10's reverted r8/r9 clobber (SCORECARD r10 conformance defect) and
r12's restored r8/r9 receipts (SCORECARD r12 admission note). Required of
A03/A04/R07/X02, owner = integrator: record the window as a named observation
with the mtimes and the quoted diffs (not a silent pass — claim A's scope-watch
threshold `claims.json:63` is met only if the record explains it), confirm no
other filed round is dirty, and state the runbook rule that validators for filed
rounds are not re-run in this tree without the receipt guard. No seat may edit
these files; no errata is owed now that the bytes match HEAD.

## 1. Claim C plan — `reports/round-33/calib/open-items-ledger.json` (12/12 rows)

### 1.1 Artifact and ownership map

| artifact | owner | role |
|---|---|---|
| `calib/K03-open-items.md` | K03 | canonical table: exactly 12 rows, `id/item/origin-round/pointer/class`, plus the **count method** (how 12 was reached) — the cross-check source |
| `calib/C01..C12-item-NN.md` | C01-C12 | one item each: status-quo re-verification at HEAD, class call, evidence, fix draft if fixable |
| `calib/C13-consistency.md` | C13 | duplicate/contradiction census over C01-C12; per-item table |
| `calib/C14-fix-drafts.md` | C14 | before/after text blocks for every fixable item; **no source edits** |
| `calib/C15-ledger-draft.json` | C15 | the ledger draft, schema below; missing slices marked owed |
| `calib/open-items-ledger.json` | integrator | final ledger from C15 draft + K03 cross-check |
| `calib/C16-receipt.md`, `scribe/S02-calib-receipt.md` | C16, S02 | receipt narrative |

### 1.2 Ledger schema (binding)

Top level: `{round: 33, baseline: "139e3b6…", generated_from: [K03 path, C01..C14 paths], count_provenance: <string + command>, rows: [12], consistency_receipt: <C13 path>, unfiled: 0}`.

Row fields (all required unless marked): `id` (stable slug, e.g. `OI-01`),
`item`, `origin` (round number + filing path), `pointer` (`file:line` or
command that locates the item at HEAD), `status_quo_check` (`{date, command,
result}` — dated, re-runnable, at HEAD), `disposition_class`,
`evidence` (list of `file:line` / command-output citations), `fix_draft`
(path + anchor in C14; required iff class is `fixed-with-evidence`),
`owner`, `reason`, `next_touch` (required iff class is
`carried-with-owner+reason+next-touch`).

Class vocabulary is **exactly two** (`claims.json:42`): `fixed-with-evidence`
and `carried-with-owner+reason+next-touch`. Required-field matrix:

| class | must carry | must not claim |
|---|---|---|
| `fixed-with-evidence` | fix draft pointer, verification command + expected result, evidence citations | that a seat landed the fix — seats draft, the integrator applies (`claims.json:42`, `targets.json:7`) |
| `carried-with-owner+reason+next-touch` | `owner` (a live path, an operator, or a resolving round pointer), `reason`, `next_touch`, status-quo evidence | a fix, or "unassigned" — zero unassigned rows is the threshold (`claims.json:50`) |

`fixed-with-evidence` semantics, stated once so C13/C15 cannot over-claim: the
row is fixed **as a bounded draft plus its verification**; the applied state is
the integrator's act, recorded afterwards.

### 1.3 Status-quo check protocol

Pointer classes and their check form: (a) `path:line` → read the line at HEAD,
quote it; (b) round artifact → `test -s <path>` + the filed verdict line; (c)
tool behavior → the gate/selftest command + exit code; (d) provenance claim →
`git log -1 --format=%h -- <path>`. Each check is dated, and the ledger row
carries the command verbatim. No historical command is re-run as proof of a
current state unless it is deterministic and re-run live.

### 1.4 Count provenance — the "12" is a reconciliation, not a given

Measured hazard: `SCORECARD.md:444-445` records "12 standing open items in the
dossier"; `reports/round-32/dossier-d13-operator-decisions.md:123-139` (Decision
4) tables **9 rows**; `reports/round-32/final-dossier.md:107` says "Twelve named
items tabled … design debts (12 garment holds, head2, RL-3), the r24
citation/cold-run conditions, lore-owned items, the rubric gap,
devin-telemetry could-not-evaluate, adapter-baseline supersession semantics".
Two arithmetics reach 12, and they are not equivalent:

- **Candidate B (covers every element the dossier names):** 9 table rows with
  "box-1 citation conditions 2-4" split into 3 (`+2`) and "lore-owned: bilateral
  read + L0 contract-digest" split into 2 (`+1`) → 9 + 2 + 1 = **12**.
- **Candidate A:** 3 design debts + 3 box-1 conditions + 4 cold-run items
  (N1/N4/N5/N7) + 2 lore-owned = **12**, but it drops the rubric gap, devin
  telemetry, and adapter supersession, which `final-dossier.md:107` explicitly
  lists among the twelve.

K03 owns the canonical call; R05 is chartered to attack exactly this
(`targets.json:69`). The ledger's `count_provenance` field must carry K03's
chosen arithmetic and the reconciliation note, and the validation leg C-leg-3
below re-derives it.

**Post-read landing (K03 exists now — reconciled).** `calib/K03-open-items.md`
landed at 00:55 local after this plan's first read. Its adopted convention
(`K03-open-items.md:32-43`) is arithmetically identical to Candidate B:
3 design debts + 3 box-1 citation conditions + 1 cold-run cluster + 2
lore-owned + 1 rubric + 1 devin telemetry + 1 adapter semantics = **12**, and it
is the only convention that both includes all 9 D13 rows and lands on the filed
"12" — an independent agreement with this seat's derivation above. Two K03
points are binding on the C lane:

- The numeral "12" is flagged `to-verify` as to the original author's intent,
  with a named contamination path: the D13 table's first row carries "**12** D4
  garment-form holds" (`K03-open-items.md:45-53`) — a hold count, not an item
  count. The ledger's `count_provenance` must reproduce this caveat, and if the
  operator's intended set is the literal 9 rows, the re-merge targets are
  OI-04..OI-06 and OI-08..OI-09.
- K03 carries a **domain class** per row (`design-debt`, `citation-condition`,
  `cold-run-condition`, `lore-owned-routing`, `protocol-gap`, `telemetry-gap`,
  `baseline-semantics`; `K03-open-items.md:57-58`) which is a different axis from
  the ledger's two-value **disposition class**. C15 must carry both fields
  without conflating them: domain class explains what the item *is*, disposition
  class records what round 33 *did with it*.
- K03's seat mapping C01↔OI-01 … C12↔OI-12 (`K03-open-items.md:75-78`) matches
  this plan's §1.5 fix register: C14's bounded drafts are OI-04, OI-05, OI-06,
  and OI-07's N1 errata; OI-01..OI-03 and OI-08..OI-12 are the carry
  candidates.

### 1.5 Fix-draft register (verified pointers; C14 owns the drafts)

Known in-scope bounded fixes, each re-measured here or by the cited filed
round:

1. **Loanword-dating cite cluster.** `SKILL.md:486` cites
   `loanword-material-dating.md:26,60`; `SKILL.md:488` cites `:57` (both read
   this seat, 2026-10-19). D11 re-confirmed both open and measured the intended
   content at `:63` (sense–referent pairing) and `:59` (prestige /
   dictionary-bias) — re-verify those targets before drafting
   (`reports/round-32/dossier-d11-shonen-boxes.md:53-58`).
2. **Contract `:183` mis-cite.** `SKILL.md:501` and `SKILL.md:128` cite
   `worldbible-integration-contract.md:183`; this seat measured
   `grep -n boilerplate corpus/knowledge/synthesis/worldbible-integration-contract.md`
   → **no matches**: the "basis is never boilerplate" rule does not live in that
   file at all, so a same-file repoint cannot repair it. Bounded options for
   C14: reword the row to rest the rule on `reports/round-15/claims.json:14`
   (already cited at `SKILL.md:501`) and drop/replace the `:183` token, or
   repoint to a live carrier the C14 seat verifies. D11:59-62 records the
   current state.
3. **Dangling tool anchors.** `TL-01` (`SKILL.md:479,481`), `TL-02`
   (`SKILL.md:483`), `FIELD_DEFAULTS` / `fictional-coordinate` /
   `descriptive-gloss` (`SKILL.md:491`) occur **0** times in
   `tools/d2-typed-labels.py` (D11:64-68). Decision rule for C14, now
   **measured** rather than conditional: prefer a SKILL-only rewording naming the
   real selftest behavior — `SKILL.md` is pinned **nowhere** (live sha256
   `79fe91d3…` appears in zero frozen files, no `MANIFEST.tsv` row, no live tool
   parses it; `adj/A10-receipt.md:47`, finding A10-F10, corroborated by
   `adj/A13-verify-a07-a09.md`), so the reword option carries **zero** pin cost.
   Adding tool tokens stays the integrator's option only if A09/X00's matrix
   shows no pinned baseline references those bytes. Conversely, C14 must **not**
   propose edits to `corpus/lessons/README.md`: that file is pinned twice
   (`reports/round-26/run-validation.py:97` `README_BASELINE_BLOB = a3187055…`
   and `reports/round-25/validation.json:1020` `input_sha256 = ec7469da…`) and
   claim O's README reconciliation is the integrator's recorded trade
   (A10-F10) — C-lane drafts touching it would collide with claim O.
4. **N1 errata.** The checklist item at `SKILL.md:695-712` names no expected
   verdict for the round-5/6/7 acceptance re-runs, which exit 1 at clean HEAD
   for distinct causes (D11:145-149). Bounded fix: errata lines naming the
   expected exit per re-run.

Every draft in C14 is a before/after text block plus a rationale and the
command that will verify the applied state. Seats never edit SKILL.md
(`targets.json:7`); the integrator applies, and any applied SKILL edit feeds
A09's pin-cascade list.

### 1.6 Claim-C validation legs (spec for `reports/round-33/run-validation.py`)

S04's machine-checkable leg spec (`targets.json:82`) must mirror these ids.

| leg | assertion | command/mechanism | expected |
|---|---|---|---|
| C-leg-1 | ledger parses; `len(rows) == 12`; ids unique; `unfiled == 0` | JSON load + assertions | pass |
| C-leg-2 | every row: class ∈ the two licensed values; required fields present per the 1.2 matrix | per-row schema check | pass |
| C-leg-3 | ledger id set == K03's canonical id set (one-to-one, or an explicit mapping note); `count_provenance` present and re-derivable | set equality vs K03 table | pass |
| C-leg-4 | consistency receipt: C13 exists, dated, names zero duplicates/contradictions **or** names each finding with owner | read C13 | pass |
| C-leg-5 | pointer resolution: every row's `pointer` and `evidence` path exists at HEAD (path-existence + `file:line` in range; no historical command re-run) | pathlib checks | pass |
| C-leg-6 | no filed bytes edited by seats: `git status --porcelain reports/round-1..32` is empty **or** the leg names each residual row; the ≈55 s r5/r7 dirty window (03:54:32Z–03:55:27Z, bytes since restored to HEAD) is recorded, never silently passed | git status parse | empty or named rows, never blanket-assert clean |
| C-leg-7 | `test -s reports/round-33/calib/C14-fix-drafts.md` and every `fixed-with-evidence` row's `fix_draft` anchor resolves in it | file + anchor check | pass |

Threshold to admit claim C: 12/12 rows dispositioned, zero unassigned
(`claims.json:50`); any row failing C-leg-2/3/5 is a rejection, not a note.

## 2. Claim A plan — consolidated adjacency audit (`adj/audit-assembled.md`)

### 2.1 Check set with commands and expected results

| check | command (verbatim; run at lane root with `TMPDIR=$PWD/.scratch`) | expected |
|---|---|---|
| A01 PROVINCE accuracy | `git log --oneline -2 -- PROVINCE.md`; `git diff --quiet -- PROVINCE.md`; `git rev-parse HEAD:PROVINCE.md`; `sha256sum PROVINCE.md`; re-read `PROVINCE.md` owns/refuses vs the tree | last commit `c53782a`, blob `313b182f…`, sha `05b34a57…` (measured, §0); owns/refuses still match; verdict + no edit proposed |
| A02 handoff boundary | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet`; `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest`; `python3 tools/gates/handoff-packet-check.py <packet.md>` on the current pair; cross-read `corpus/knowledge/synthesis/worldbible-integration-contract.md` | exit 0; 16/16 fields, 20/20 glossary, 0 findings, links resolving, statuses 16/7/4; verdict **prepared-not-accepted** (computational green ≠ acceptance; `reports/round-21/adjacency/A11-A12-handoff.md:50`) |
| A02 note | **current pair (K04 §5.2, A10 A02 row): `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json}`** — latest of four filed pairs, gate exit 0, `packet_sha256 6ced88ad…` equal to its freeze (`adj/K04-method-scout.md:189-213`; `adj/A10-receipt.md:40`); earlier pairs: `reports/round-22/handoff/declared-in/`, `declared-in-r2/` (the `tools/exercise-handoff-e2e.py:38` default), `reports/round-26/handoff/declared-in-r5/`, `reports/round-28/pinsweep/v3-baseline-r28/`. The A02 seat names **which** pair it ran; citing a stale pair is a named finding, not a green | | |
| A03 scope watch | `git ls-files \| wc -l`; `git status --porcelain`; out-of-lane write scan | `2655` (whole tracked tree, §0); **label the surface**: the r32 watch's `1,870` and A10's measured protected surface `1,905` are different denominators (`adj/A10-receipt.md:64`, finding A10-F12) — unlabeled they read as a 785-path breach; delta explained: expected rows (`M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`) plus the **recorded** ≈55 s r5/r7 receipt window, since restored to HEAD (§0; independently corroborated as A10-F7, `adj/A10-receipt.md:59`); window evidence and mtimes filed, not silently passed |
| A04 bleed scan | read fleet `.ufo/l0-questions.md` kotodama lines (read-only); confirm lore-owned items (bilateral read, L0 contract digest) routed-not-absorbed; `grep` round-33 fragments for canon/clearance/promotion language | zero unfiled bleed; every hit a negation or routed reference |
| A05 corpus boundary | partitions on disk vs `PROVINCE.md:9-14` owns-list; confirm `examples/` in-lane non-canon | pass / named finding |
| A06 contested scope | restate contested items with current pointers: contract revision 1.0.0 bilateral read pending (`reports/round-20/handoff/packet.md:1-16`; `corpus/knowledge/synthesis/worldbible-integration-contract.md:11-18,49-70`; preserved at `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14` per `reports/round-29/adjacency/province-entries.md:17`) | routed-not-absorbed; nothing in round 33 absorbs them |
| A07 history consistency | re-run 2-3 filed commands from `reports/round-21/adjacency/ledger.json:80-90` and `reports/round-29/adjacency/ledger.json:75-96` (e.g. the r21 ledger census command, the PROVINCE sha check, the r29 census) | same green, or a filed defect with the differing output |
| A08 language audit | `grep -rn` over `reports/round-33/**` for `promot|canon|clearance|closure|verified` | every hit a negation or routed reference; output filed |
| A09 pin-cascade exposure | from X00's matrix: which frozen baselines/pins reference the lessons README or SKILL.md lines that O/C drafts would change | re-pin list or "none"; no edit by A-seat |
| A10 receipt | verdict table over A01-A09 + named findings | every row verdict-filled |

The audit verdict surface is a **row schema**:
`{check_id, check, status ∈ {green, named-finding, could-not-evaluate},
command, date_utc, result (exit code + key numbers), evidence_paths,
finding?: {id, severity, out_of_province, bleed, filed, owner, disposition}}`.
`could-not-evaluate` is legal only with an owner and a reason (mirrors
`AGENTS.md`); blank or "unknown" is not a verdict. Recommended (integrator's
call): land the machine-readable twin `reports/round-33/adj/ledger.json`
mirroring the r21/r29 shape (`round, date, assignment, scope, verdict,
province_accuracy, handoff_status, unfiled_bleed, inventory{observed_at_utc,
counts, command, result}, entries[], rows[], audits[], checks[], findings[],
non_scope_observations[]`) so A14 and run-validation.py can census it.

### 2.2 Named-finding rule (binding on A01-A10)

Any non-green check **must** carry a finding with: id `A33-<CHECK>-NN`
(precedent ids `A21-D4-XF-01`, `A29-ADJ-EVID-01`), severity, `out_of_province`,
`bleed`, `filed: true`, owner, disposition. `unfiled_bleed` = count of bleed
rows lacking a filed finding → must be 0. Out-of-province content is
**reported, never absorbed** (`PROVINCE.md:31`); the audit makes no canon,
rights, clearance, or promotion claim anywhere.

### 2.3 Verifier rules (A11-A14)

A11/A12/A13 independently re-run the cited commands of A01-A03 / A04-A06 /
A07-A09 from a fresh context: same green, or a filed defect quoting the
differing output (the r29 instrument-history pattern — preliminary failed
probes disclosed, not used as evidence: `reports/round-29/adjacency/A09-A12-handoff.md:50`).
A14 checks A10's table row-for-row against the fragments and flags any verdict
not backed by a fragment.

### 2.4 Claim-A validation legs

| leg | assertion | expected |
|---|---|---|
| A-leg-1 | `adj/audit-assembled.md` exists; check table has one row per A01-A10, each with a licensed verdict | pass |
| A-leg-2 | validator re-runs the handoff gate on the named pair: exit 0, 16/16 + 20/20, 0 findings; handoff_status == prepared-not-accepted | pass |
| A-leg-3 | scope-watch counts recorded; every delta path is under `reports/round-33/`, `REGIMEN.md`, `LOG.md`, or is a **named** residual row (r5/r7) | named rows, not silent pass |
| A-leg-4 | language grep clean (negations/routed refs only) | pass |
| A-leg-5 | ledger census: `unfiled_bleed == 0`; every non-green check has a filed finding with owner | pass |
| A-leg-6 | A11-A14 exist, are dated, and A14's cross-check names zero unbacked verdicts | pass |

## 3. Cross-claim interfaces and integration order

- **X00** must feed A09 (pin matrix) and C14 (blast radius of SKILL edits);
  my §1.5 decision rule depends on it.
- **S04** must mirror the leg ids C-leg-1..7 and A-leg-1..6 in its
  validation-leg spec (`targets.json:82`), or the integrator's runner will
  diverge from this plan.
- **R04/R05/R06** attack: ledger rows vs C01-C12, K03's 12-arithmetic (§1.4),
  and whether C14's proposed targets are real lines (§1.5 — note the measured
  0-hit `boilerplate` result).
- **R07/R08/X02** attack: the §0 filed-receipt window (record it, confirm no
  other round is dirty), the audit verdict table, and pin-cascade claims.
- Integration order: K03 → C01-C12 → C13 → C14 → C15 → integrator ledger;
  K04 → A01-A09 → A10 → A11-A14 → A15; both before S02/S03/S04 and the
  validator.

## Owed

- ~~`reports/round-33/adj/K04-method-scout.md`~~ — **closed during this seat's
  run**: K04 landed and is reconciled in §2.1 (current pair corrected to the r30
  `declared-in-r6` pair, K04 §5.2) and §0/A03 (its HEAD quick-reads agree with
  this seat's: PROVINCE `c53782a`/`313b182f…`, ls-files 2655, protected surface
  clean).
- ~~`reports/round-33/calib/K03-open-items.md`~~ — **closed during this seat's
  run**: K03 landed (00:55 local) and is reconciled in §1.4 (same 12-arithmetic,
  plus the to-verify provenance caveat and the domain-vs-disposition class
  distinction C15 must carry).
- No owed fragment remains from this seat's mission. Downstream, the A-lane's
  own owed set is A10's (A02-A09 fragments), not this seat's
  (`reports/round-33/adj/A10-receipt.md:79-94`).

## Citations

- `reports/round-33/adj/K04-method-scout.md:189-235,245-256` (current pair,
  scope-watch method, check-set mapping)
- `reports/round-33/adj/A10-receipt.md:40,47,59,64,79-94` (A02/A03/A09 rows,
  findings A10-F7/F10/F12)
- `reports/round-33/calib/K03-open-items.md:32-43,45-53,57-58,75-78` (count
  conventions, to-verify provenance, class vocabularies, seat mapping)
- `reports/round-33/claims.json:19-64` (claims C/A, thresholds), `:57`, `:63`
- `reports/round-33/targets.json:19-20,31-46,48-63,65-72,82` (seat missions)
- `reports/round-32/dossier-d13-operator-decisions.md:123-139` (Decision 4, 9 rows)
- `reports/round-32/dossier-d11-shonen-boxes.md:53-68,145-149,205-207`
- `reports/round-32/final-dossier.md:107`
- `SCORECARD.md:444-445` (r32 routed debt incl. "12 standing open items"), `:521` (r10 clobber), `:571-576` (r12 receipt restore)
- `PROVINCE.md:9-14,16-25,31`
- `SKILL.md:128,479,481,483,486,488,491,501,695-712`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md` (grep `boilerplate` → 0 hits)
- `reports/round-21/adjacency/ledger.json:80-90`, `A11-A12-handoff.md:39-50`
- `reports/round-29/adjacency/ledger.json:75-96`, `A09-A12-handoff.md:50`, `province-entries.md:15-17`
- `tools/exercise-handoff-e2e.py:13-16,38`, `tools/harness/receipt_guard.py:7`
- `reports/round-33/telemetry/dispatch-declared.json`
- Commands (2026-10-19, lane root): `git log --oneline -3`; `git ls-files | wc -l` → 2655; `git status --porcelain`; `git diff --stat reports/round-{5,7}/validation.json`; `git diff LOG.md`; `stat -c '%y %n'`; `git log --oneline -2 -- PROVINCE.md` → c53782a; `git rev-parse HEAD:PROVINCE.md` → 313b182f…; `sha256sum PROVINCE.md` → 05b34a57…; `ls reports/round-33/calib/ reports/round-33/adj/` → empty; `grep -n loanword-material-dating|:183 SKILL.md`; `grep -n boilerplate corpus/knowledge/synthesis/worldbible-integration-contract.md` → none; remediation re-read `date -u` → `VERIFY_UTC=2026-10-19T03:56:48Z`, `git diff --stat reports/round-{5,7}/validation.json` exit 0, `git status --porcelain reports/round-5 reports/round-7` empty
