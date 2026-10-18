### Register craft

Build a register as three linked objects: a **typed stratum of forms**, a
**law over speech acts**, and a **replayable delivery**. A register value says
who uses a form and in which situation; it does not decide whether the bytes
are native, borrowed, or a translated label. A derivation pass proves neither
the law nor the register's semantic coverage. This subsection composes, rather
than replaces, *Label typing*, *Claim uncertainty typing*, *Slot-label routing*,
*Derivation replay*, and *Family-clean projection* above. Design authorities:
`reports/round-26/register/design.md` §§2–6,
`corpus/knowledge/linguistics/register-strata-attestation.md` §§1,4,7–8 and §13,
and `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§3–5,10.
The D4 furnace-league is a NON-CANON worked case, not a real-language model or
an accepted world-bible record (`reports/round-29/adjacency/register-law.md`
§Verdict).

#### Stratum discipline — select an operation, then test its domain

| Condition | Do | Never / boundary | Evidence |
|---|---|---|---|
| A form carries a marked register | Type its form channel first; keep supplied native and recipient-adapted borrowed forms on the sound-and-identity channel. Only a translated label without a supplied form is moved, with its owed-form hold | Give `stamp`, `ritual`, or `trade` a private inventory, or use register as an exemption flag | `reports/round-26/register/impl.md` §5; `examples/culture-d4/components/04-lexicon.yml` `registers` / `QREG-02`; `corpus/knowledge/synthesis/era-language-staging.md` §7 |
| A stratum is derived from the delivered lexicon | Resolve the base in the same family's packet; name the base record, `derived_from`, `doublet_of`, operation and candidate. In D4 `QREG-03` selects `mark → reverse`, `fire → lengthen` from the **base's** axis | Choose the operation from the desired spelling, borrow an absent forecast record, or mistake replay of an arbitrary declared operation for enforcement of the axis selector | `reports/round-26/register/rules.md` §2; `reports/round-26/register/impl.md` §§1,3; `tools/gates/argot-derivation-gate.py` `declared_derivation` / `evaluate_packet`; `reports/round-29/defects/routed.md` §`R26-ARGOT-DERIVATION-IDENTITY-AND-PAIR-SCOPE` |
| The selected operation must replay | Use the declared computed operation or a machine-readable `morphology.derivation_rules` pattern/output pair. `reverse` reverses characters; the landed `lengthen` rule doubles the first vowel and its id is lowercase `lengthen`, exactly matching `derivation.op` | Treat the design's uppercase `LENGTHEN` as the landed id; confuse character reversal with syllable reversal; claim that first-vowel doubling handles every stress pattern or diphthong | `examples/culture-d4/components/04-lexicon.yml` `morphology.derivation_rules` / `derivation_spelling_note`; `reports/round-26/register/rules.md` §§3.1,4 RU-1/RU-2; `reports/round-26/register/impl.md` §4.2; `tools/gates/argot-derivation-gate.py` `OP_FUNCTIONS` / `replay_rule` |
| An operation yields the stated bytes | Check recipient inventory, syllables, collisions and identity separately; report missing bases, malformed pairs and unresolved rules as debt. Arithmetic equality is not that entire check set | Read an argot exit 0 as proof of base ownership, phonotactic legality, non-identity, label typing, era legality or complete coverage | `tools/gates/argot-derivation-gate.py` §Calibration / `evaluate_packet`; `reports/round-29/defects/routed.md` §§`R26-ARGOT-DERIVATION-IDENTITY-AND-PAIR-SCOPE`, `R26-ARGOT-LABEL-TYPING-AND-REGISTER-SCOPE`; `reports/round-26/register/impl.md` §3 |
| The institution needs a semantic field | List its required acts, offices, obligations and measures **before** selecting the operation. Measure `semantic class × operation-legality` over named delivered bases, with the exact legality call, reader digest, packet digest, command and date | Call an operation total because it selects an operation for each axis; apply a one-syllable predicate to a whole word; assume a legal identity truncation makes a useful marked form | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§3–5,10; `reports/round-28/argot/D20-ceiling-wording.md` §§1–4; `reports/round-26/register/rules.md` §§2,3.2 |
| The operation cannot supply a needed form | Choose and record the price: hand-pick/replace the bases, choose or amend the operation, or accept the ceiling and declare the paraphrase/substitution/other record channel that carries the missing term | Coin more instances under an unchanged illegal transformation, relax the inventory to legalize one desired word, or infer that a missing derived word makes its concept inexpressible | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§2,5,10; `corpus/knowledge/linguistics/register-strata-attestation.md` §6 and §13 |
| A register has an institutional era | Carry its availability window with the forms and law. D4's `stamp` is available from E1; E3 is reserved, not a substitute historical attestation | Present an era declaration as an executed era check: the argot arithmetic leg does not implement that institution-date test | `reports/round-26/register/design.md` §5; `reports/round-26/register/rules.md` §5; `examples/culture-d4/components/04-lexicon.yml` `QREG-04`; `examples/culture-d4/components/13-register-law.yml` `RGL-05` |

Worked ceiling, measured **2026-10-18T21:53:04Z** with
`python3 -B reports/round-28/ceiling/measure-ceiling.py`: reader `b5406bcd…`
over the pre-integration packet `543d68a8…` finds **19 legal / 8 illegal**
among **27** mark-axis plain words; the named institutional abstraction set
has **1 legal / 4 illegal**. `L-45 tikmes → sem.kit` is the surviving
abstraction; `L-30 gis → sig` is not legal. This supersedes the pre-fix
reader's 18/9 and 0/5 readings, without rewriting them. Test legality
**per syllable**: `all(is_legal_syllable(s) for s in syllabify(form))`.
The base-initial-coda predicate agrees on that measured population, not on
every possible language or arbitrarily shaped input. The transferable result
is the check over the **operation + base list + phonotactics + reader**, not
this fixture's ratio (`corpus/knowledge/linguistics/register-strata-attestation.md`
§13; `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§4,10;
`reports/round-28/argot/D20-ceiling-wording.md` §§3–4). Read the ceiling entry's
phrase-absence evidence with the separate qualification
`reports/round-30/fixes/x63-f2.md` §Applied amendment: that evidence correction
changes neither the measured arithmetic nor the declared ceiling.

#### Law discipline — speech acts are not lexical or costume properties

| Condition | Do | Never / boundary | Evidence |
|---|---|---|---|
| A register is meant to make speech bind | State each act as a row: speaker/authority, venue/slot, procedure, force, record consequence and penalty shape. Use the speech-act classes as a design checklist; declarations need an authorizing institution | Treat a register identity row, vocabulary list or prose claim that “the word binds” as a replayable law; assert that the delivered checker evaluates every felicity condition | `corpus/knowledge/linguistics/register-strata-attestation.md` §§1–4,8; `reports/round-27/law/design.md` §§1,3; `reports/round-28/law/design.md` §§1,3.5 |
| An act fails its conditions | Distinguish **misfire** (act void/not performed) from **abuse** (act performed, speaker sanctionable); state the record effect separately from the penalty | Infer that every wrong act merely incurs a fine, or that every sanction erases the record | `corpus/knowledge/linguistics/register-strata-attestation.md` §§2–3,10 RSA-3 |
| A speaker's rank authorizes an act | Link the law row to the delivered authorizing rank/rite/institution record. Keep law over speech in `register_law`; keep costume/material permits in their own ledger | Add `register` to a costume-rule membership guard and call it enforcement: the costume resolver can fall through to `not-applies` without a speech target | `reports/round-27/law/design.md` §§3.1,4–5; `corpus/knowledge/linguistics/register-strata-attestation.md` §7; `reports/round-28/law/impl-1.md` §§1–3 |
| The design and delivered law disagree | Name both row sets and scope the claim to the delivered wording. D4 `RGL-02` refuses a binding stamp oath; do not substitute the historical round-27 positive `QREG-06` proposal for it. `RGL-03` enters the guest act under a stamp-name while restricting the guest's furnace-roll access | Equate `not-rollable` with no record of any kind, silently resolve competing oath scopes, or turn a proposed QREG id into a delivered record by citation alone | `examples/culture-d4/components/13-register-law.yml` `RGL-01` / `RGL-02` / `RGL-03`; `reports/round-27/law/design.md` §3; `reports/round-28/law/design.md` §3.1 |
| Law rows reach a packet | Name their component owner, packet key, declared fields, assembler validation and delivered record links. Recheck the assembled **record** set, not a substring in a component | Read “present in source”, “read by the auditor”, “validated by assembly” and “enforced” as synonyms; let `design_row` point to nonexistent QREG records | `corpus/knowledge/linguistics/register-strata-attestation.md` §4.1 and §10 RSA-9; `reports/round-28/law/impl-1.md` §§2–3; `reports/round-29/defects/routed.md` §§`R28-LAW-REGISTER-ROW-ASSEMBLY-VALIDATION`, `R28-LAW-DANGLING-DESIGN-ROW-REFERENCES` |
| The law is replayed | Invoke `tools/gates/register-law-gate.py` on the source packet. Its `evaluate_packet` checks delivered references, declared register names/ids, force vocabulary, consequence machinery, axes/kinds and expected row presence within its stated scope; retain each emitted finding's severity | Copy an early design's all-HOLD severity onto the executable's FAIL findings; call string/record resolution a simulation of authority, polarity, delegation, uptake or record transactions | `tools/gates/register-law-gate.py` §Finding ids / §Calibration / `evaluate_packet`; `reports/round-28/law/design.md` §§3.2,3.5,5; `reports/round-29/defects/routed.md` §§`R28-LAW-FORCE-OVERMATCH`, `R28-LAW-CONSEQUENCE-AND-SPEAKER-BLINDNESS` |
| A law checker or cited row changes | Pair the clean input with named negative controls for force, speaker, consequence and missing/dangling rows; compare finding identities and messages, not only their count. Include the tokenless speaker shape as distinct from `Name (ZZ-99)` | Call a token-bearing tamper proof of tokenless-speaker coverage; call equal finding counts identical findings; bless a broken clean baseline from the producer's output | `tools/gates/register-law-gate.py` `selftest`; `reports/round-29/defects/routed.md` §`R28-LAW-CONSEQUENCE-AND-SPEAKER-BLINDNESS`; `corpus/knowledge/verification/verification-independence-anti-circularity.md` §2 |

#### Composition and delivery — preserve every type and every obligation

| Pipeline boundary | Required invariant | Wrong reading to reject | Evidence |
|---|---|---|---|
| Family → label type → register scope | Select family-local records first; keep provenance-based `native-form` / `borrowed-strata` / `translated-label` independent of register. Loans retain donor/adaptation and separate entry/referent clocks | A legal register form proves native provenance; a declared linguistic loan licenses foreign fixture data | `reports/round-22/bleed/design.md` §§Decision,Required paired controls; `reports/round-26/register/impl.md` §5; `corpus/knowledge/synthesis/loanword-material-dating.md` §§2–3 |
| Typed labels → adapter → routing/holds | The family's own assembler is the identity authority; move gloss fields by text transform, never delete or re-serialize the foreign packet. The routed record set equals the owed-form hold set; distinguish obligations from record/slot rows | A register label moves supplied sound bytes off-channel; removing inherited fixture findings or adding supplied register forms discharges the unrelated garment obligations | `reports/round-17/d4/typed-support-1.md` §§4–5; `reports/round-18/d4/holds.md` §4; `reports/round-22/bleed/design.md` §Integration obligations; `reports/round-26/register/impl.md` §5 |
| Form replay + law replay → gate result | Run both legs. The generalized typed gate has `L3b-argot`; that leg admits argot HOLDs while rejecting FAILs/input refusals. Run the separate law gate even when typed routing is green | A typed-pipeline pass implies a clean law, or `L3b-argot` means no argot debt. Gate exit 0 is scope-specific, not clearance | `tools/gates/typed-pipeline-gate.py` `evaluate`, `L3b-argot`; `tools/gates/register-law-gate.py` §Calibration / `main`; `reports/round-28/law/impl-1.md` §§5–6 |
| Read-set pins → frozen replay | Name every input; keep commands flagless where the replay interface requires it; record re-pins as new rows and verify the pinned dependency closure. Keep reproduction, mismatch and could-not-evaluate distinct | Overwrite a filed manifest, equate a pin match with a fresh verdict, or claim isolated snapshot replay while a ROOT-relative peer reads the live tree | `reports/round-18/d4/manifest.md` §§2,6; `corpus/knowledge/verification/gate-frozen-run-standard.md` §§4,6; `reports/round-29/defects/fix-14.md` §§Instrument limitation found later,Route |
| Checks → claim ledger → lore handoff | Give each claim its own resolving basis and `supported` / `partial` / `unresolved` status; preserve restrictions and owner/reopen questions on unresolved law, era, ceiling and source legs | Promote arithmetic support onto an untested institutional edge, digest equality onto semantics, or a prepared packet onto lore acceptance/canon | `reports/round-15/handoff/v2-design.md` §2; `corpus/knowledge/verification/to-verify-triage-protocol.md` §2; `corpus/knowledge/synthesis/worldbible-integration-contract.md` §§4,8; `reports/round-29/adjacency/province-entries.md` §§Province and contract boundary,Deliverables reviewed |

#### Executable entry points and supporting helpers

Use the **source** packet, not the derived typed packet, for the normal entry
commands:

```sh
export TMPDIR=$PWD/.scratch
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
```

Argot and law use 0 = no reported findings, 1 = findings, 2 =
could-not-evaluate; `--selftest` is a capability check, not a measurement of
every packet. The typed gate's 0 instead means equality with its pinned
expected findings. All three interfaces are documented in their module
docstrings (`tools/gates/argot-derivation-gate.py`,
`tools/gates/register-law-gate.py`, `tools/gates/typed-pipeline-gate.py`).

These previously implicit supporting surfaces are named so the craft index is
not mistaken for a smaller executable inventory. Helpers are not independent
culture-clearance gates, and a historical baseline must not be silently
replaced by the latest bytes.

| Surface | Role / entry contract | Evidence |
|---|---|---|
| `tools/exercise-handoff-e2e.py` | v1/v2/v3 handoff exerciser; `--profile v3 --baseline <authorized-successor>/expected.json` selects the intended generation instead of silently blessing stale prose/pins | module docstring §§Profiles,Assertions; `reports/round-29/defects/routed.md` §Fresh v3 renderer claim drift |
| `tools/assemble-d2-typed.py` | D2 typed adapter; `--check` compares the typed packet without regenerating it; D4 uses its own adapter rather than borrowing D2's build | module docstring §§Interface,Fail-closed rules; `reports/round-17/d4/typed-support-1.md` §4 |
| `tools/gates/d4-assembly-check-gate.py` | flagless frozen-row adapter: `<source-packet>` must equal the D4 assembler's own build; 0 identity / 1 drift / 2 could-not-evaluate | module docstring and `main`; `reports/round-18/d4/manifest.md` §2 |
| `tools/gates/d4-typed-labels-check-gate.py` | flagless frozen-row adapter: `<projection>` is checked against the D4 **source** packet; forwards the projector's `--check` byte-identity verdict: 0 identical / 1 drift / 2 could-not-evaluate, not the label-findings verdict | module docstring and `main`; `reports/round-18/d4/manifest.md` §2 |
| `tools/harness/packet_links.py` | claim/edge link resolver, `--packet <machine-twin> --json`; path/token/line links must resolve against the manifest and live bytes | module docstring §§Inputs,CLI; `reports/round-15/handoff/v2-design.md` §3 |
| `tools/harness/receipt_guard.py` | receipt-write preflight; rejects committed-receipt writes by default, not a sandbox or permission to refresh historical evidence | module docstring, `guard_receipt` / `round_runner_main` |
| `tools/harness/r8_checks.py` | internal round-8 parent-receipt identity/deduplication module; `--measure` reads the old inputs without rewriting their filed receipt | module docstring §§Corrected semantics,Modes |

Run scratch-writing tools only after `export TMPDIR=$PWD/.scratch`; a
mirror-safety leg that rejects an in-repo temporary directory requires its own
external temporary directory (for example `/var/tmp`) and an explicitly
pinned input/dependency set. A refusal is not a failed linguistic judgment.
The historical replay-isolation caveat remains routed until its own paired
control closes it (`reports/round-29/defects/fix-14.md` §§Instrument limitation
found later,Route; `reports/round-29/defects/routed.md`
§`R28-FROZEN-REPLAY-USES-LIVE-TREE`). All register choices here remain
NON-CANON, with no real-language resemblance, cultural-permission, rights or
lore-acceptance claim (`corpus/knowledge/linguistics/register-strata-attestation.md`
§§11–12; `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§10–11).
