# R28-D23 — SKILL rule draft: the register-law replay leg (and the rule for a law with none)

- round: 28 (operator: loop 3 of 3, **build round 4 of 4 — the last build round**;
  64 declared workers, `devin/deepseek-v4-1-flash-high`). Seat **R28-D23**
  (D-scribe 3 of 4).
- claim under draft: `reports/round-28/claims.json` claim **D**, axis `depth`,
  capability `register-law-replay`.
- date: 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`.
  Lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **final stamp 2026-10-18T20:15:52Z.** The tree moved once in this seat's window
  (the RL-4 `packet_keys` fix, ~20:13Z); every citation below is re-measured at
  the final stamp.
- **status: DRAFT ONLY — `SKILL.md` is not edited by workers.** The orchestrator
  lands the row below. This seat wrote no `SKILL.md`, `LOG.md`, `SCORECARD.md`,
  `corpus/**`, `tools/**`, `examples/**` or filed round-8–27 byte. Scratch under
  `.scratch/` only (`export TMPDIR=$PWD/.scratch` preceded every scratch write).
  No commit, no push.
- canon: **NON-CANON engineering draft.** No real language, script, institution
  or register is described, cited or approximated in it.

## 0. The finding that shapes this draft

**`SKILL.md` is byte-still, and the law it would teach does not yet have the leg
the rule is about.** Measured at the final stamp:

```
$ sha256sum SKILL.md          # 2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048
$ wc -l SKILL.md              # 598
$ grep -c "Derivation relations" SKILL.md          # 0  — round 25's rule, still absent
$ grep -c "register law\|Register law" SKILL.md    # 0  — round 27's rule, never landed
$ grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md   # 352 / 354
$ grep -rl "D4L-LAW" tools/ | wc -l                # 0  — no replay leg exists
```

Three consequences, and the third is the reason this draft is shaped as it is:

1. **The insertion point is unchanged and unambiguous.** `SKILL.md:352`
   (`<!-- END R23-D SKILL SUBSECTION -->`) → `:354` (`## Error patterns`).
   Nothing has to be re-derived; the last subsection is still
   `### Family-clean projection` (`:243-352`).
2. **The round-27 rule never landed, so this is the second round it is absent.**
   §2 is the addition to a derivation-relations subsection if one lands; §3 is the
   standalone block if none does. Land one, not both.
3. **This round's rule is unusual: it must teach how to write a law leg AND how
   to report a law that has none, because the second is the measured state.** The
   claim asked for a replay leg and the tree does not have one (§1). A rule that
   only described the ideal leg would be a rule about bytes that do not exist. So
   §3 carries **both halves**, and the second half — *a declared law with no
   checker must say so, in the artifact* — is the part the delivered tree
   actually demonstrates.

## 1. What is demonstrated, and what is not

| # | proposition | demonstrated? | evidence |
|---|---|---|---|
| 1 | a component declares its own packet contribution, and the assembler merges exactly those blocks | **YES** | `03-orthography.yml:24` `packet_keys: [orthography, records, literacy_institutions]`; `09-costumes.yml:22` adds `enforcement`; `tools/assemble-culture-d4.py:258-262` honors it per file |
| 2 | the declared blocks reach the packet as **records** (list rows carrying `id`), not as prose | **YES** | the packet gains `records:` (OR-01..03), `literacy_institutions:` (LI-01..03), `enforcement:` (EN-01..02); all eight ids resolve as records where round 27 measured five at 0 |
| 3 | a law row's citations resolve against the delivered tree | **YES, for the ids** | `RGL-01`'s `mold-keeper (OR-02, component-only)` now names a packet record — round 27 marked it `to-verify` for exactly this reason |
| 4 | a law row is **checked** by anything delivered | **NO** | seven value tampers + one row deletion; `findings_total=12` unchanged; `D4L-LAW-*` emitted 0 times; `grep -rl "D4L-LAW" tools/` → 0 |
| 5 | the law declares its own non-execution, in the artifact | **YES** | `13-register-law.yml` `law_binding.enforcement`: *"no gate executes these rows … a declared law with named non-execution, not a claim of enforcement"* |
| 6 | a `force` vocabulary exists to check forces against | **NO** | five distinct `force` strings in use, no declared vocabulary anywhere; `x59` reports `force_vocabulary=0`, `L10-HOLD` |

**The pairing of rows 4 and 5 is the round's lesson.** The artifact is **honest**
about not being enforced, and the machinery **proves** the honesty. That is the
pattern the rule must teach: the non-execution is a *declared, measured* fact, not
an omission nobody noticed.

## 2. LANDING-READY — the row, as an addition to a derivation subsection

If the orchestrator lands a derivation-relations subsection (round 25's draft is
paste-ready), append these two rows to its table. Columns match round 26's
proposed table (`Derivation requirement | Correct shape | Never | Consequence if
violated | Citation`).

```markdown
| Register-law packet surface | a component declares its own packet contribution with a top-level `packet_keys:` list, and the assembler merges exactly those blocks, so a record block's ids are packet records rather than prose cross-references; the declaration names the file's real contribution, not the allowlist's nearest hit | leave a record block to the `PACKET_KEYS` allowlist fallback; cite a component-only id (`OR-02`, `EN-01`) as a law row's authority; widen the packet surface without a declared reason | a legal-in-component record is invisible to every gate that reads the packet: the citation dangles, the id resolves to nothing, and the packet's own record set is smaller than the component's | `examples/culture-d4/components/03-orthography.yml:24` and `09-costumes.yml:22` (the round-28 declarations); `tools/assemble-culture-d4.py:258-262` (the per-file path; `:262` is the allowlist fallback); measured `reports/round-28/scribe/capability-row.md` §1 |
| A law with no checker must say so | where a law is declared but nothing evaluates it, the artifact states its own non-execution in its `law_binding`/equivalent, and the capability row repeats the measurement; the claim that "the law is enforced" is never made | land a law block and let a reader assume a gate grades it; cite an audit instrument as a lane gate; discover the gap only when someone tampers a row | a declaration is read as a clearance: a tampered law value changes no verdict and nobody notices | `examples/culture-d4/components/13-register-law.yml` (`law_binding.enforcement`); measured `reports/round-28/scribe/capability-row.md` §2 (eight tamper routes, `D4L-LAW-*` emitted 0 times); `reports/round-28/audit/x59-register-law-negatives.py` (`L6b-HOLD`) |
```

## 3. LANDING-READY — the standalone rule (recommended shape)

Insert after `<!-- END R23-D SKILL SUBSECTION -->` (`SKILL.md:352`), before
`## Error patterns` (`SKILL.md:354`). Self-contained.

```markdown
### Register-law replay — a law is a claim, a leg is a measurement, and a law without a leg must say so

A **register law** is a set of declared speech-act rows: what may be said in a
register (`act`), by whom (`speaker` / `holder`), with what illocutionary value
(`force`), and with what record consequence (`consequence`). The law's *carrier*
is a component that declares its own packet contribution with a top-level
`packet_keys:` list, which the assembler honours per file
(`tools/assemble-culture-d4.py:258-262`) — so a law's supporting records are **packet
records**, list rows carrying an `id`, and never prose cross-references. Where a
component leaves its record blocks to the assembler's `PACKET_KEYS` allowlist
fallback, those records are legal in the component and **invisible to every gate
that reads the packet**, and a law row citing one carries a **dangling citation**.
Worked instance `examples/culture-d4/components/03-orthography.yml:24` and
`09-costumes.yml:22` (the round-28 declarations) with
`examples/culture-d4/components/13-register-law.yml` (`RGL-01..05`) and
`04-lexicon.yml:244-253` (`QREG-01..04`); executable authority
`tools/assemble-culture-d4.py` (`--check` byte-identical, `--selftest` 81/81).

**A declared law is not an enforced law, and the difference is measured, not
assumed.** A law row is replayable only when a delivered instrument resolves it
against the tree it governs: every agent token `Name (ID)` in `speaker`/`holder`
must resolve to a **delivered record**, every `force` must name a value in a
**declared vocabulary**, and every `consequence` must name delivered roll/rank
machinery. Where no instrument does this, the artifact must state its own
non-execution (`13-register-law.yml` `law_binding.enforcement`: *"no gate
executes these rows"*), and the capability row must carry the **measurement** that
proves it — a tamper route per clause, each of which must produce a named
`<family>-LAW-*` finding. The round-28 measurement is the negative instance and
the shape to imitate: eight tamper routes (six field values, one whole-row
deletion, one control), `findings_total=12` **unchanged** from clean,
`grep -rl "D4L-LAW" tools/` → **0**. A positive control in the same run shows the
machinery *can* discriminate — breaking a landed derivation's surface moves the
projector's count and fires the argot gate — which is what makes the negative
meaningful rather than vacuous.

Two prerequisites are part of the rule, because a leg cannot be written without
them. First, the **vocabulary the leg grades against must itself be declared**:
if the law's `force` values are checked against nothing, a checker would have to
invent the set it grades, which is the failure mode where an unknown value routes
to `cannot-evaluate` forever rather than to a finding. Second, a **count that does
not move is not a missing update**: a landing that adds records rather than forms
leaves the hold count unchanged, and the honest bookkeeping is to re-pin the
digests and name the landing, never to manufacture a count movement.

| Register-law requirement | Correct shape | Never | Consequence if violated | Citation |
|---|---|---|---|---|
| The law's records are packet records | the component declares its own `packet_keys`, naming its real contribution; the assembler merges exactly those blocks | leave a record block to the allowlist fallback; cite a component-only id as a law row's authority | the citation dangles and the packet's record set is smaller than the component's | `examples/culture-d4/components/03-orthography.yml:24`; `09-costumes.yml:22`; `tools/assemble-culture-d4.py:258-262` |
| A declared law is not an enforced law | the artifact states its non-execution; the capability row carries the tamper measurement that proves it | claim enforcement no gate provides; cite an audit instrument as a lane gate | a declaration is read as a clearance | `13-register-law.yml` (`law_binding.enforcement`); `reports/round-28/scribe/capability-row.md` §2 |
| A leg resolves against the tree it governs | every speaker resolves to a delivered record, every force to a declared vocabulary, every consequence to delivered roll/rank machinery | grade a law against a vocabulary the packet does not declare; resolve an agent token against prose | the leg is unfalsifiable, or it invents the set it grades | `reports/round-28/audit/x59-register-law-negatives.py` (`L6b-HOLD`, `L10-HOLD`) |
| A negative claim needs a positive control | a tamper the machinery **must** catch is run in the same breath (a broken derivation moves a count; a broken law does not) | report "no findings" without showing the machinery can produce one | a leg that always passes is capability, not measurement | measured `reports/round-28/scribe/capability-row.md` §2.4 (C2: projector 12→13, argot exit 1) |
| One row per named class | a tampered clause produces a finding whose id names the clause (`<family>-LAW-FORCE`, `-SPEAKER`, `-CONSEQUENCE`), never an anonymous failure | a generic "law invalid" finding; a count that moves without a named id | the reader cannot tell which clause broke, and a re-pin cannot be distinguished from a re-bless | `reports/round-28/run-validation.py:160` (`LAW_FINDING_RE`; cited by revision — the runner moved under this seat); `reports/round-28/scribe/x54-law-negatives-spotcheck.py` (14 routes) |
| A landing that adds records, not forms | re-pin the digests, leave the counts, name the landing in the revision note | manufacture a count movement to "show the update landed"; leave the pin naming bytes that no longer exist | a false count change, or a stale pin that refuses (exit 2) under an unrelated edit | `examples/culture-d4/expected-holds.json` (counts stay 12/0/0; packet pin must move `86079a67…` → `543d68a8…`); measured `reports/round-28/scribe/frozen-rows.md` §4.1 |
| A law's vocabulary is declared before it is graded | the packet declares the set a `force` (or equivalent) value is drawn from | grade values against a set that exists only in the checker | the leg routes an unknown value to `cannot-evaluate` rather than to a finding | measured `reports/round-28/audit/x59-register-law-negatives.py` (`force_vocabulary=0`, 5 values in use) |
| Register is scope, not field, and not channel | a register-scoped form keeps its checked form; the register value is a scope fact | promote the register value into `off_channel_field`; let a register label remove a string from the checked channel | the round-8 T1 violation at a new address | `SKILL.md:47,149,176-182`; `examples/culture-d4/components/04-lexicon.yml:245-249` |

Cautions that are part of the rule: a **declared** law is not an **enforced** law,
and the delivered instance demonstrates the gap rather than closing it; a green
register leg is not canon, lore acceptance or a real-world register claim; a
register-scoped *hold* is owed design debt, never a defect to repair into a pass;
an audit instrument is not a lane gate and may not be cited as one; and where a
shared replay engine is reused across families, the family-clean projection rule
above still governs which records a register relation may name
(`SKILL.md:243-352`).
```

## 4. Row placement and the citation ledger

**Placement.** `grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md`
→ `352`, `354`. The insertion point is unambiguous and leaves the R23-D block
byte-intact.

**Citation ledger.** Every cited path resolves; digests are worktree digests at
`69cecbc`, measured 2026-10-18T20:15Z.

| cited path | sha256 | resolves |
|---|---|---|
| `SKILL.md` (at draft time) | `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048` | yes |
| `examples/culture-d4/components/03-orthography.yml` | `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b` | yes |
| `examples/culture-d4/components/09-costumes.yml` | `f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23` | yes |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` | yes |
| `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240` | yes |
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` | yes |
| `examples/culture-d4/expected-holds.json` | `857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f` | yes |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | yes |
| `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` | yes |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | yes |
| `reports/round-28/run-validation.py` | `53e9b4d1…` (moving; cited by revision) | yes |
| `reports/round-28/audit/x59-register-law-negatives.py` | `a4482c9c…` (moving; cited by revision) | yes |
| `reports/round-28/scribe/x54-law-negatives-spotcheck.py` | `9841e71d…` (moving; cited by revision) | yes |

Line anchors re-checked at draft time (20:15Z): `SKILL.md:47`, `:149`,
`:176-182`, `:243-352`, `:352`/`:354`; `03-orthography.yml:24` and
`09-costumes.yml:22` (the `packet_keys` declarations);
`13-register-law.yml:18` (`packet_keys: [register_law]`), `:51-58`
(`law_binding`, incl. `enforcement`); `04-lexicon.yml:244-253` (`QREG-01..04`);
`tools/assemble-culture-d4.py:258-262` (the per-file `packet_keys` path).

## 5. The counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum SKILL.md examples/culture-d4/components/03-orthography.yml \
  examples/culture-d4/components/09-costumes.yml \
  examples/culture-d4/components/13-register-law.yml \
  examples/culture-d4/packet.d4.yml tools/assemble-culture-d4.py
grep -c "Derivation relations" SKILL.md                             # 0 — the round-25 rule never landed
grep -c "register law\|Register law" SKILL.md                       # 0 — the round-27 rule never landed
grep -n "END R23-D SKILL SUBSECTION\|^## Error patterns" SKILL.md   # 352 / 354
grep -rl "D4L-LAW" tools/ | wc -l                                   # 0 — no replay leg exists
grep -n "packet_keys" examples/culture-d4/components/03-orthography.yml \
  examples/culture-d4/components/09-costumes.yml
grep -n "enforcement" examples/culture-d4/components/13-register-law.yml
python3 tools/assemble-culture-d4.py --check                        # exit 0, byte-identical
python3 tools/assemble-culture-d4.py --selftest | tail -1           # 81/81
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | head -1
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -3
python3 reports/round-28/scribe/x54-law-negatives-spotcheck.py | grep ^verdict
python3 reports/round-28/audit/x59-register-law-negatives.py | tail -3
```

## 6. Limits

- Draft text only; the orchestrator owns placement, wording and admission. No
  `SKILL.md` byte was written by this seat, and this draft admits nothing.
- **The rule describes a delivered packet surface and a NOT-delivered replay
  leg.** It teaches both halves on purpose (§0.3): a rule that described only the
  ideal leg would describe bytes that do not exist. If the D seats land the leg
  before integration, §3's first clause still holds and the second clause should
  be re-measured, not deleted.
- The rule carries the general derivation conditions inline because the
  derivation-relations subsection has now been absent for **two** rounds. If that
  subsection lands, §2 is the addition to it and §3 becomes redundant.
- Readings bind to the digests and stamps above, and **the tree moved once in this
  seat's window**; a successor seat must re-hash before quoting.
- **This file makes no claim that the round-28 D claim is met.** It supplies the
  rule text and names the insertion point.
