- Seat: C03 | executor | C (open item 3 of 12) | date 2026-10-19 | baseline 139e3b6

# R33-C03 — disposition: item 3, the RL-3 register-lexicon ceiling

**Claim:** C (calibration). **Write scope:** this file only. No git commit/push,
no corpus/SKILL/LOG edit — every proposed change below is a **draft for the
integrator**. Scratch: `TMPDIR=$PWD/.scratch`. Non-canon engineering evidence:
nothing here promotes, certifies, clears or closes anything.

## 1. Which item is "item 3" — and why the identification is robust

`calib/K03-open-items.md` (the scout's canonicalization) had **not landed** when
this seat started — `reports/round-33/calib/` was empty at 2026-10-19
(`ls reports/round-33/calib/` → no files). Per the shared missing-dependency rule
I reconstructed the enumeration myself from the two sources claim C names,
`reports/round-32/dossier-d13-operator-decisions.md` Decision 4 table
(`:128-138`) and `reports/round-32/dossier-d11-shonen-boxes.md` open conditions.

**K03 landed at 00:55 during this seat's run, and the identification matches.**
K03's canonical table numbers the items `OI-01..OI-12`; its **OI-03** is *"RL-3
register-lexicon ceiling — constraint, not defect"* (`calib/K03-open-items.md:64`),
and the C-lane seat mapping is `C03 ↔ OI-03` (`K03-open-items.md:75`). Three
independent orderings had already put the same object at position 3:

| ordering rule | positions 1 / 2 / 3 |
|---|---|
| Decision-4 table row order (9 rows, `dossier-d13:130-138`) | 12 D4 garment-form holds / `head2` empty domain / **RL-3 ceiling** |
| K03's adopted expansion (box-1 conditions 2/3/4 → 3 rows; lore-owned → 2 rows; the cold-run set kept as its one filed row) | OI-01 / OI-02 / **OI-03 = RL-3 ceiling** |
| claim C's own `before.items` enumeration order (`claims.json:44`) | 12 garment holds / `head2` / **RL-3 ceiling** |

So item 3 = the row `dossier-d13:132` — *"RL-3 register-lexicon ceiling
(constraint, not defect) | r27/r28 | ceilings knowledge entry"* — under every
ordering, and the id is now fixed: **OI-03**.

**Count provenance — my derivation is superseded by K03's; they differ in
mechanism and agree in count and membership.** Decision 4 tabulates **9 rows**,
not 12 (`K03-open-items.md:24-30` measures the same 9). Before K03 landed I
derived the 12 by expanding the *cold-run* row into N1/N4/N5/N7 (8 + 4); K03
adopts the expansion *box-1 conditions 2/3/4 → 3 rows and lore-owned → 2 rows*,
keeping the cold-run set as one row (`K03-open-items.md:36-43`). Both land on 12
with the same membership; **K03's convention is the canonical one** — it is the
scout's declared rule and the C-lane seat mapping is built on it. K03 also flags
the numeral's provenance `to-verify` and names the same contamination path I had
noted: the table's first row, "**12** D4 garment-form holds" (`dossier-d13:130`),
carrying 12 as a *hold count* (`K03-open-items.md:45-53`). My alternative
expansions (box-1 only → 11; both → 14) are recorded here as the superseded
derivation, not as a competing count.

## 2. Status quo at HEAD — re-verified, dated, command-carried

Lane HEAD at this seat's run: `139e3b662900557afe54f632b468619593dc9fcb`
(`git rev-parse HEAD`, 2026-10-19).

**2.1 The pointer resolves.** "ceilings knowledge entry" →
`corpus/knowledge/linguistics/register-lexicon-ceilings.md`:
289 lines, sha256 `bb579d51cea0a900571e77b6690978256a607ec08f500923674738107dc1bffe`
(`wc -l`; `sha256sum`). Indexed at `corpus/README.md:138`, index revision 1.9
(`corpus/README.md:3`), totals line 201. The entry is **single-commit** —
`git log --follow -- corpus/knowledge/linguistics/register-lexicon-ceilings.md`
returns exactly `3b13a2f` ("round-28: admit D/O/C … ceiling knowledge"), 289
insertions, no later touch. Nothing has drifted the filed bytes since landing.

**2.2 The index and entry audits are green at HEAD.**

```
python3 -B reports/round-28/audit/entry-audit.py corpus/knowledge/linguistics/register-lexicon-ceilings.md
# → bar=True filler=False src=11/11 refs_unres=0 digests_bad=0 couples_unres=0 index=ok
#   audited 1; bar clear 1; bar failing 0 []; indexed 1; index clear 1; index failing 0 []
#   EXIT=0
python3 -B reports/round-28/audit/entry-audit.py --selftest
# → selftest: 11/11 checks passed; EXIT=0
python3 -B reports/round-28/readme/sweep.py
# → parts {… "linguistics": 21 …}; rows 201 files 201; missing 0; topic_mismatch 0;
#   orphan_rows 0; header_drift {}; totals_ok True; footer_ok True; EXIT=0
```

**2.3 The measurement still reproduces at HEAD — including through its own
recheck trigger.** The entry's `recheck:` line fires on any change to
`packet.d4.yml`/`04-lexicon.yml`, and that trigger **has fired**: the entry's
`verified-at` pins the packet at `543d68a8…`, while HEAD's packet is
`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`
(`sha256sum examples/culture-d4/packet.d4.yml`); the packet last moved in
`11df1fd` (round-30 wave integration). The gate digest the entry pins is
**unchanged**: `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`
(`tools/gates/argot-derivation-gate.py`, `sha256sum`; last moved `6c0ac44`, r27).
Re-run against the moved packet:

```
python3 -B reports/round-28/ceiling/measure-ceiling.py
# → population: mark-axis plain words = 27
#   delivered gate (b5406bcd)  legal=19 illegal=8
#   filed round 27: legal=18 illegal=9  (pre-fix reader); delta vs delivered: {'L-45'}
#   mechanism: reverse is legal <=> the base-initial consonant is a licensed coda -> True (27/27)
#   onsets=14 codas=8 never-coda=b,g,h,j,p,w   EXIT=0
python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest
# → selftest: 10/10 checks passed   EXIT=0
```

The ceiling reading (19 legal / 8 illegal; 4 of 5 legal-institutional
abstractions refusing `reverse`; 27/27 mechanism) **holds at HEAD over the
changed packet**, so the item owes no re-measurement; the entry's dated packet
digest is a historical reading by its own append-only design, not a stale pin.
`--json` also confirms the population is 27 ids over `mark_axis_all: 29`
(`measure-ceiling.py --json`).

**2.4 The cited round-27 filing resolves.** `reports/round-27/law/design.md:197`
§3.2 carries the `mark-axis plain words: 27 reverse-legal: 18 reverse-ILLEGAL: 9`
table and the five named abstractions; `reports/round-27/law/review.md:146` is
`## 4. Finding RL-3 — the register cannot spell its own law's vocabulary`;
`reports/round-27/law/rules.md:153` is §3.3. The entry's "cited by revision, not
by digest" note resolves to its provenance: `reports/round-27/entry/C43.md:54`
records `reports/round-27/law/design.md 00f201b3… → 9d5c1dd7…` exactly as the
entry claims.

**2.5 The item's substance is a constraint, not a defect — and the record says
so in three places.** `SCORECARD.md:345` (r27 claim D): "RL-3 (… the register
cannot spell its own law's vocabulary, **a recorded craft constraint**)";
`reports/round-27/law/review.md:376`: "design constraint | declared `LL-1`/`LL-2`;
law written inside the ceiling"; `dossier-d13:132`: "(constraint, not defect)".
The refusal to repair (an escape hatch in the operation rule) is itself a
recorded decision, priced in `reports/round-26/register/review.md` §3 and not
taken (`reports/round-27/law/design.md:238-246`).

## 3. Named finding C03-F1 — a live authoring defect inside this item's pointer

**The finding.** The entry's `- gap filled:` cell (`register-lexicon-ceilings.md:4`)
claims five absence sweeps each returning 0 over `corpus/knowledge/`. Re-run at
HEAD, **all five return ≥ 1**:

| pattern (verbatim from `:4`) | HEAD hits | files |
|---|---|---|
| `lexicon ceiling` | 2 | `register-strata-attestation.md` (§13), the entry itself |
| `register ceiling` | 1 | the entry itself |
| `derivational ceiling` | 1 | the entry itself |
| `operation-constrained` | 1 | the entry itself |
| `which semantic fields` | 3 | `sound-symbolism.md:106`, `register-strata-attestation.md:399` (§13), the entry itself |

Three of those five were already filed as **sibling-landing** rows by round-28's
own audit (`reports/round-28/audit/x63-entry-source-resolvability.md` §3.4
F1/F3/F4: zero hits at baseline `6c0ac448` once the audited document is
excluded). But **F2 is an authoring defect and it is still live**: at the round-28
baseline commit the phrase already existed —

```
git show 6c0ac448:corpus/knowledge/linguistics/sound-symbolism.md | grep -n -i "which semantic fields"
# 106:  1. **Fields** — assign which semantic fields carry ideophones (canonical: manner of motion, …)
git show 6c0ac448:corpus/knowledge/linguistics/register-strata-attestation.md | grep -c -i "which semantic fields|lexicon ceiling"
# 0   (strata's §13 is the wave's own later landing → F1/F3/F4 class)
```

`sound-symbolism.md` was last touched in `94ca098` (round 10) — it predates the
entry and the sweep was **false when written**. X63 routed the repair in round 28
("It **repairs nothing.** X63-F2 is a corpus write and is routed", `x63…md:264`)
and it was never applied: the entry is single-commit and still carries the false
claim at HEAD. This is a **defect in the item-3 pointer itself**, and it is the
one genuinely fixable thing this item owns.

## 4. Disposition

**Ledger row for item 3** (schema per claim C: `{id, item, origin, pointer,
status_quo_check, disposition_class, evidence, fix_draft?, owner, reason?,
next_touch?}`):

- `id`: `OI-03` (alias `RL-3-ceiling`) — K03's canonical id (`K03-open-items.md:64`);
  the alias is deliberate because bare `RL-3` is overloaded across three
  namespaces; see §5.
- `item`: RL-3 register-lexicon ceiling (constraint, not defect) — the register
  cannot spell its own law's vocabulary.
- `origin`: r27/r28 (`reports/round-27/law/review.md:146`; r28 knowledge landing).
- `pointer`: `corpus/knowledge/linguistics/register-lexicon-ceilings.md`
  (+ `corpus/knowledge/linguistics/register-strata-attestation.md` §13).
- `status_quo_check`: re-verified 2026-10-19 at HEAD `139e3b6` — pointer
  resolves (289 lines, sha256 `bb579d51…`); index row `corpus/README.md:138`
  under rev 1.9 (201 rows/201 files, 0 findings); entry-audit clean (11/11
  sources resolve, 0 digest mismatches, `index=ok`); measurement reproduces over
  the moved packet (`aac91246…`) at 19/8, delta `{L-45}`, mechanism 27/27,
  selftest 10/10.
- `disposition_class`: **carried-with-owner+reason+next-touch** (the ceiling
  itself); **plus** finding C03-F1, fix-drafted (below) for integrator
  application. The seat cannot mark "fixed-with-evidence": the fix is a corpus
  write the integrator owns.
- `evidence`: §2 and §3 above, every line command-carried.
- `fix_draft`: §4.1.
- `owner`: the ceiling → operator (D13 Decision 4 assigns no owner; the recorded
  alternatives are "future regimen, manual pass, or accepted-as-recorded" —
  recommendation: **accepted-as-recorded**, since the constraint is declared,
  priced and designed around, and its recheck triggers are live). Finding C03-F1
  → **integrator (round-33)**, per the no-seat-corpus-writes rule.
- `reason` (why carried, not repaired): repairing the ceiling means amending the
  operation rule — a rule change priced at r26 and refused by recorded decision
  (`reports/round-26/register/review.md` §3; `reports/round-27/law/design.md:238-246`);
  the constraint is the design, not a bug.
- `next_touch`: the entry's own `recheck:` line (`register-lexicon-ceilings.md:20`)
  — before quoting any coverage figure; on any change to `02-phonology.yml`,
  `04-lexicon.yml`/`packet.d4.yml`, or the gate's `syllabify`/`is_legal_syllable`;
  on revision of a cited framework. Packet trigger already exercised this round
  (§2.3).

### 4.1 Fix draft — C03-F1, append-only errata (integrator-applied)

**Recommended form.** The entry's own append-only clause
(`register-lexicon-ceilings.md:223-225`: "A later round … adds a new section or
a new entry linked from `recheck`; it never rewrites a filed reading") governs.
Append as **§12**, after §11 and before the trailing `Append-only discipline`
bullet, or at the file tail immediately after it — integrator's choice of
position, provided §1-§11 bytes are untouched.

```
## 12. Errata (round 33): the absence sweeps in the head block, re-measured

**Append-only.** Nothing above is rewritten. The `- gap filled:` cell states five
absence sweeps, each returning 0 over `corpus/knowledge/` at 2026-10-18. Re-run at
lane HEAD `139e3b6` on 2026-10-19, **all five now return ≥ 1**:

| pattern | hits at HEAD | files | class |
|---|---|---|---|
| `lexicon ceiling` | 2 | `register-strata-attestation.md` §13; this entry | sibling landing (r28 wave) |
| `register ceiling` | 1 | this entry | self-match after landing |
| `derivational ceiling` | 1 | this entry | self-match after landing |
| `operation-constrained` | 1 | this entry | self-match after landing |
| `which semantic fields` | 3 | `sound-symbolism.md:106`; `register-strata-attestation.md` §13; this entry | **one pre-existing hit** |

The last row is the finding. `sound-symbolism.md:106` ("assign **which semantic
fields** carry ideophones") existed at the round-28 baseline commit `6c0ac448`
(that file last moved in round 10), so that sweep was **false when written** —
reported as `X63-F2`, an authoring defect, in
`reports/round-28/audit/x63-entry-source-resolvability.md` §3.4 and routed, never
repaired. The other four rows are the wave's own landings (this entry and the
strata §13 amendment), the sibling-landing class of the same audit.

**Corrected reading, for any future consumer of the head block:** of the five
patterns, the phrase `which semantic fields` occurs once in the pre-existing
corpus, in `sound-symbolism.md`, in the ideophone sense — a different sense from
this entry's ceiling sense. The claim that survives is the narrower one: no entry
before this one measured what an operation-constrained register cannot say.
```

**Optional minimal alternative** (X63's own proposed repair, in place at `:4`,
for the integrator only if the append-only rule is read as not covering head-block
errata): replace the clause
`grep -rl -i "which semantic fields" corpus/knowledge/ | wc -l` → **0** with
`… | wc -l` → **1** (`sound-symbolism.md:106`, ideophone sense, pre-existing) —
and leave the other four readings as the 2026-10-18 stamp. This form edits filed
bytes; the append-only form above is the discipline-conformant one and is what I
recommend.

**Control proving the fix (integrator runs post-application).**
```
# 1. the errata section exists and §1-§11 are byte-identical to 3b13a2f
git diff 3b13a2f -- corpus/knowledge/linguistics/register-lexicon-ceilings.md | grep -c '^-[^-]'
#    expect 0 (additions only)
# 2. the corrected sweep reading is true at HEAD
grep -rl -i "which semantic fields" corpus/knowledge/ | wc -l        # expect 3, named in §12
git show 6c0ac448:corpus/knowledge/linguistics/sound-symbolism.md | grep -c -i "which semantic fields"  # expect 1
# 3. the entry still clears its audits after the write
python3 -B reports/round-28/audit/entry-audit.py corpus/knowledge/linguistics/register-lexicon-ceilings.md   # exit 0, index=ok
python3 -B reports/round-28/readme/sweep.py                                                                  # rows == files, 0 findings
# 4. negative control: a planted false sweep must fail leg 2
#    (write "wc -l` → **0**" for a pattern with hits into a scratch copy; leg 2 must read ≥1)
```

## 5. Named finding C03-F2 — the label `RL-3` is overloaded across three namespaces

The ledger row's own label is ambiguous, and this matters because the ledger is
what the next reader greps. Bare `RL-3` at HEAD denotes three distinct objects:

1. the **D2 rank rule** `RL-3` ("hem-cord count") — `examples/culture-d2/components/11-costumes.yml:452`,
   with a frozen copy at `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/examples/culture-d2/components/11-costumes.yml:452`;
2. the **r26 syllabify finding** — `reports/round-26/register/design.md:229`,
   `reports/round-26/register/review.md:157`, carried as `RD-4`/`RL-3` in
   `reports/round-27/argot/D17-…md:210` and `D20-…md:98`; **closed** per
   `corpus/lessons/round-27.md:51` ("The docstring/implementation divergence
   `RL-3` named is closed");
3. the **r27 register-lexicon ceiling** — `reports/round-27/law/review.md:146`
   (this item).

A reader who greps `RL-3` for this item lands first on a closed finding or on a
costume rank rule. **Draft (no filed-byte edit):** the ledger row id is `OI-03`
with the alias `RL-3-ceiling` (§4), and the row's `item` text names the r27 law
filing; if the integrator wants it durable in corpus, the §12 errata draft above
already carries the disambiguating sentence and can absorb one more line — but
note that the frozen r19-pre copy in (1) cannot be touched
(`tools/gates/frozen/**` boundary).
Class: **reported, not repaired** — a naming collision across filed rounds and
frozen baselines is not this seat's to rewrite.

## 6. What this fragment does not claim

No promotion, canon, clearance or closure verdict. The item is not "closed": it
is dispositioned as carried-by-design plus one integrator-applied fix draft. The
measurement numbers are re-runs of the round-28 instrument, not an independent
re-derivation of the ceiling arithmetic (that was D20's review surface, r28). The
"12" count derivation in §1 is my superseded derivation; K03's adopted
convention is canonical and the reconciliation is recorded in §1. The numeral's
own provenance stays `to-verify` per `K03-open-items.md:45-53`.

## Owed

- `reports/round-33/calib/C15-ledger-draft.json` — my §4 row is a fragment for
  the ledger; C15 owns the assembled 12-row file (row `OI-03`, per K03's seat
  mapping `K03-open-items.md:75-78`).
- `reports/round-33/calib/C14-fix-drafts.md` — the §4.1 errata draft and the §5
  disambiguation must be folded there (C14 owns the fix-draft aggregate). Note
  K03 classes `OI-03` as a carry candidate; my C03-F1 fix is a **sub-finding of
  the same row** (the pointer's own false sweep), not a fourth box-1-style
  pointer fix, and the ledger row must carry both the carry disposition and the
  fix draft.
- `reports/round-33/calib/C13-consistency.md` — the duplicate/contradiction
  check should confirm no other seat dispositioned `OI-03` (C03 owns it per
  K03's mapping) and that my §1 count-derivation reconciliation is recorded,
  not contradicted.
- K03 dependency: **resolved** — `calib/K03-open-items.md` landed during this
  seat's run (00:55) and is reconciled in §1/§4 (`OI-03` confirmed).

## Citations

Paths (read at HEAD `139e3b662900557afe54f632b468619593dc9fcb`, 2026-10-19):
- `reports/round-32/dossier-d13-operator-decisions.md:123-138` (Decision 4 table, 9 rows; `:132` the RL-3 row; `:125-126` owner-unassigned)
- `reports/round-32/dossier-d11-shonen-boxes.md:114-122` (standing design debts incl. RL-3), `:201-208` (summary table)
- `reports/round-33/calib/K03-open-items.md:36-43` (adopted expansion convention), `:45-53` ("12" provenance `to-verify`), `:60-64` (canonical table; OI-03 = RL-3 ceiling), `:75-78` (C-lane seat mapping; OI-03 a carry candidate)
- `reports/round-33/claims.json:44` (item sources; the enumeration order used in §1), `reports/round-33/targets.json` (seat C03 out path)
- `SCORECARD.md:345` (r27 claim-D row: RL-3 "a recorded craft constraint"), `:365` (r28 coverage row), `:441-447` (r32 routed-debt line incl. "12 standing open items")
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:1-289` (`:4` the five absence sweeps; `:6` KTD-RLC-S-0001; `:18-20` source/verified-at/recheck; `:223-225` append-only clause)
- `corpus/knowledge/linguistics/register-strata-attestation.md:315` (§13 heading), `:325` (r27 filed RL-3 in three places), `:398-399` (ceiling restated)
- `corpus/README.md:3-10` (revision 1.9), `:138` (index row, byte-equal topic)
- `corpus/knowledge/linguistics/sound-symbolism.md:106` (the pre-existing `which semantic fields` hit)
- `reports/round-27/law/design.md:197-246` (§3.2 arithmetic, LL-1/LL-2, the refused escape hatch), `reports/round-27/law/rules.md:153,238`, `reports/round-27/law/review.md:146,376`
- `reports/round-27/entry/C43.md:54` (design.md `00f201b3… → 9d5c1dd7…` provenance)
- `reports/round-27/argot/D17-speech-act-outside-the-law.md:210`, `reports/round-27/argot/D20-gap-closure-record.md:98` (`RD-4`/`RL-3` partly-closed reading)
- `corpus/lessons/round-27.md:51` (syllabify `RL-3` closed), `corpus/lessons/round-28.md:66` (entry landing, 201 entries)
- `reports/round-28/audit/x63-entry-source-resolvability.md:136-176` (F1-F4 table; F2 authoring-defect at `:142,156-165`), `:264` (F2 routed, not repaired), `:246-252` (README rev 1.9 reconciliation)
- `reports/round-28/audit/entry-audit.py:1-60` (legs: bar/index/new), `reports/round-28/readme/sweep.py`
- `examples/culture-d2/components/11-costumes.yml:450-453` (rank rules RL-1..RL-4; the RL-3 collision), `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/examples/culture-d2/components/11-costumes.yml:452` (frozen copy)
- `corpus/QUALITY.md:1-23` (admission bar), `corpus/knowledge/verification/naming-collision-gate.md:1-30` (the lane's own naming-collision discipline)
- `reports/round-26/register/design.md:229`, `reports/round-26/register/review.md:157` (r26 `RL-3` syllabify sense)

Commands run (all 2026-10-19, `TMPDIR=$PWD/.scratch`, all read-only):
```
git rev-parse HEAD                                    # 139e3b662900557afe54f632b468619593dc9fcb
wc -l; sha256sum corpus/knowledge/linguistics/register-lexicon-ceilings.md
git log --follow -- corpus/knowledge/linguistics/register-lexicon-ceilings.md     # 3b13a2f only
git show --stat 3b13a2f -- …register-lexicon-ceilings.md                          # 289 insertions
python3 -B reports/round-28/audit/entry-audit.py corpus/knowledge/linguistics/register-lexicon-ceilings.md   # exit 0
python3 -B reports/round-28/audit/entry-audit.py --selftest                       # 11/11, exit 0
python3 -B reports/round-28/readme/sweep.py                                       # 201/201, exit 0
python3 -B reports/round-28/ceiling/measure-ceiling.py                            # 19/8, delta {L-45}, exit 0
python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest                 # 10/10, exit 0
python3 -B reports/round-28/ceiling/measure-ceiling.py --json                     # population 27 / mark_axis_all 29
sha256sum examples/culture-d4/packet.d4.yml tools/gates/argot-derivation-gate.py  # aac91246… / b5406bcd…
git log -1 -- examples/culture-d4/packet.d4.yml                                   # 11df1fd (round-30)
for t in "lexicon ceiling" "register ceiling" "derivational ceiling" "operation-constrained" "which semantic fields"; do grep -rl -i "$t" corpus/knowledge/ | wc -l; done   # 2 1 1 1 3
git show 6c0ac448:corpus/knowledge/linguistics/sound-symbolism.md | grep -n -i "which semantic fields"   # :106
git show 6c0ac448:corpus/knowledge/linguistics/register-strata-attestation.md | grep -c -i "which semantic fields|lexicon ceiling"   # 0
ls reports/round-33/calib/                            # empty at seat start; K03-open-items.md landed 00:55, reconciled §1/§4
ls -la reports/round-33/calib/K03-open-items.md       # 11902 B, mtime 2026-10-19 00:55 (item 3 = OI-03)
```
