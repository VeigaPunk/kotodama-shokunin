- Seat: D06 | executor | D | 2026-10-19 | baseline ce103bf

# R36-D06 — spare gap-fill across the D block

**Mission (verbatim, `reports/round-36/targets.json` seat `D06`):** "Spare
gap-fill across the D block."

**Scope and method.** This seat was dispatched as the D block's spare. It
therefore did the one thing a spare can do that the numbered D seats (D01..D05,
D07..D10) are not positioned to do: it **measured the claim's own premise**
before the block built on it. The result is a falsification of claim D's
declared `before` state and a census of what the D block's real remaining gaps
are. No file outside this one was written; every command below was run by this
seat in this seat's own shell at the stated stamp.

**Stamp.** All measurements 2026-10-19T09:2xZ, cwd = lane root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`, worktree at `ce103bf` with `git status --porcelain`
showing only `?? reports/round-36/` (no filed byte edited — §5).

**Canon:** NON-CANON engineering evidence; canon standing is lore-shokunin's.

---

## 1. Headline — claim D's `before` state is stale, and the block must not build on it

`reports/round-36/claims.json` claim D declares:

> **before:** "Register-form domain empty (`reports/round-25/argot/` + SCORECARD
> r25 row); register law/strata exist but the form class has no instances"
> **after_required:** "register-form domain non-empty with verified forms
> (derivation replay clean over the new forms; law gate exit 0 over them; typed
> pipeline holds updated with named gaps); every pin re-frozen as a new row"

**The `before` half of that sentence is false on the delivered tree, and the
`after_required` half is already satisfied.** The r25 empty-domain record the
claim asks this round to "close" was closed by round 26 and round 27, and the
pins were re-frozen through round 30. Measured:

| claim-D requirement | live state at `ce103bf` | command |
|---|---|---|
| register-form domain **non-empty** | **8 derived pairs** (`tuum/kit/lom/nees/huum/mees/reek/saam`), `register_scoped=14` | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` → `register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`, exit **0** |
| derivation replay clean over the new forms | `violations=0 rule_holds=0`; selftest **27/27** | same command; `… --selftest` → `selftest: 27/27 checks passed` |
| law gate exit 0 over them | `law_rows=5 dangling=0 findings=0`, exit **0**; selftest **45/45** | `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` |
| typed pipeline holds updated | **20/20 legs passed**, exit 0 (the argot leg is wired in as `L3b-argot`) | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml \| tail -1` |
| every pin re-frozen as a new row | active generation `round-30-qreg-records`; `expected-holds.json` carries a 4-row `pin_generations` history, filed rows untouched | `python3 -c "import json;print(json.load(open('examples/culture-d4/expected-holds.json'))['active_pin_generation'])"` |

The r25 record the claim quotes is itself **already superseded in the ledger**,
not a live gap. `SCORECARD.md:312` records the r25 state — "the register-form
domain in the delivered D4 packet is EMPTY (the register class was
design-forecast, never built into components), so the leg stands ready over an
empty domain, recorded as such" — and the very next two admission rows replace
it:

- `SCORECARD.md:329` (r26, claim D, capability `register-stratum`): "The
  round-17 register forecast **CLOSED**: the `stamp` attestation register lands
  in the delivered furnace-league tree — 8 verified register forms
  (tuum/kit/lom/nees/huum/mees/reek/saam) … derivation replay clean (8 derived
  pairs, 0 violations over 170 records)".
- `SCORECARD.md:345` (r27, claim D, capability `register-law`): "The register
  law lands: component 13 + the `register_law` packet block (RGL-01..05 …)".
- `SCORECARD.md:363` (r28, claim D, capability `register-law-replay`): "The law
  gains a replay leg (`tools/gates/register-law-gate.py`) … the leg immediately
  earned its keep — 4 real `D4L-LAW-DANGLING` findings on the clean packet".
- `SCORECARD.md:400` (r30, claim O): "QREG-05..08 land (law gate clean 4->0
  findings; 7/7 linkage controls)".

**Consequence for the block, stated plainly.** A D seat that takes claim D's
`before` at face value and "authors register-form component content and the
register forms in the packet" will **duplicate content that already exists** and
will move the D4 packet digest — a real, costly harm to the operability axis
(the four-site pin cascade r26 measured: `typed-pipelines.json` profile `d4`,
`expected-holds.json`, the v3 handoff read-set, and the r4 twin). The gap the
round should work is **not** "the domain is empty". It is the set of residues
r26/r27 named and left open, enumerated in §2 with controls.

**Independently corroborated.** Seat **D09** (`reports/round-36/depth/D09-gap-fill.md` §1),
the block's other spare, reached the same conclusion by a different route — a
`git`-history argument (`git show 1ad491a:examples/culture-d4/packet.d4.yml |
grep -c 'L-55'` → 0, and the r26 *admit* commit `4f09c99` adding all 8 forms) —
and seat **D01** (`reports/round-36/depth/D01-design.md` §0) states the same
headline from the claim's own quoted bytes. Three seats, three methods, one
finding: the `before` is stale. That is the two-independent-reads bar the claim's
own threshold asks for, and it is worth recording that the corroboration was
reached independently rather than inherited.

## 2. The D block's real remaining gaps, measured

Each row is a live measurement at the stamp, with the control that proves the
gap is real rather than a reading error.

### 2.1 `RL-8` — the era leg is unimplemented, and this is now proven two ways

`reports/round-26/register/rules.md:107-128` §5 specifies `REGISTER-ERA-01`
("a record with `register == "stamp"` must carry `stage >= E1`; a `stamp` record
with `stage E0` → `D4L-ERA` (FAIL)") and measures its own control C-E1: "The
gate emits **no era finding** — it has no era concept. So REGISTER-ERA-01 is
**specified here and unimplemented**". `reports/round-27/law/impl-8.md:68` files
it as `RL-8`, owner "whoever grows the leg". It has never been closed.

**This seat's independent two-way control.** Two scratch copies of the delivered
packet, both under `TMPDIR=$PWD/.scratch/d06/`, delivered tree untouched:

| # | fixture | edit | result |
|---|---|---|---|
| A | `.scratch/d06/packet-E0-stamp.yml` | record `L-56 kit` `stage: "E1"` → `"E0"` | `python3 tools/gates/lexicon-coverage-audit.py …` → `FINDING D-stage-mismatch: 'kit' is formed in 'E0' but construction 'STAMP-REVERSE' is only available from 'E1'`, exit **1** |
| B | `.scratch/d06/packet-E0-both.yml` | **A** plus `STAMP-REVERSE.available_from: "E1"` → `"E0"` | audit exit **0**; argot gate exit **0** (`violations=0 rule_holds=0`); law gate exit **0** (`findings=0`). **Zero findings anywhere.** |

**Reading.** Control A fires, so the tree is not blind to E0 stamp records — but
the firing finding is `D-stage-mismatch`, a **construction-availability** check
in the lexicon audit, not the register-era rule. Control B isolates this: widen
the construction's own availability and the record sits at E0 with **nothing**
objecting, in any gate. The only era protection over the stamp register is
incidental to `constructions[].available_from`; `RGL-05`'s substance ("every
stamp form is `available_from` E1; an E0 stamp claim is a defect",
`examples/culture-d4/packet.d4.yml:2863`) is enforced by nothing.

**What is new here, against the siblings.** D09 (`depth/D09-gap-fill.md` §5,
row A-6) also names `RL-8` and measures that `grep -rl 'D4L-ERA' examples/
tools/` → 0, and D01 §0 cites it — but both file it as a *description* and
defer it ("owed to a future D round"). Neither builds a control, so neither
separates the two mechanisms the tamper actually touches. The two-way control
above is this seat's contribution: it shows that the one gate which does react
reacts on the **construction** axis, and that with that axis held fixed the era
rule is unenforced in every gate. That is the difference between "the era rule
is declared, not enforced" (asserted) and "the era rule is declared, not
enforced" (measured against a discriminating control).

A known-bad positive control confirms both gates are live and discriminating
rather than silently green:

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/d06/packet-bad-deriv.yml   # kit -> kit2
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kit2' (register 'stamp'):
  declared chain 'reverse' applied to 'tik' yields 'kit'; the stated inputs and
  rules do not yield the candidate
exit 1
```

Full gate sweep over the E0-tampered packet (control A), finding counts,
tampered vs baseline — showing that exactly one gate reacts and it reacts on the
construction axis, not the era axis:

```
argot-derivation-gate.py          E0-tamper=0  baseline=0
costume-era-consistency-gate.py   E0-tamper=0  baseline=0
d4-assembly-check-gate.py         E0-tamper=0  baseline=0
d4-typed-labels-check-gate.py     E0-tamper=0  baseline=0
handoff-packet-check.py           E0-tamper=1  baseline=1
lexicon-coverage-audit.py         E0-tamper=1  baseline=0   <- the only delta
myth-consistency-gate.py          E0-tamper=0  baseline=0
naming-collision-gate.py          E0-tamper=14 baseline=14
phonology-sanity-gate.py          E0-tamper=1  baseline=1
provenance-audit.py               E0-tamper=0  baseline=0
register-law-gate.py              E0-tamper=0  baseline=0
typed-pipeline-gate.py            E0-tamper=0  baseline=12
```

**Fenced draft (not applied — the integrator applies corpus/tool changes).**
The cheapest honest closure is a rule, not a new gate: `register-law-gate.py`
already owns the law block and already resolves each row's `register` against
the `registers` block. `RGL-05` is the row that states the era constraint; what
is missing is a *record-side* resolution. Drafted as a new finding class on the
existing law gate, in the gate's own declared style:

```python
# DRAFT — reports/round-36/depth/D06-gap-fill.md §2.1; NOT APPLIED.
# register-law-gate.py: add a record-side era leg for RGL-05's substance.
#
# Finding ids (new, additive to the existing D4L-LAW-* set):
#     D4L-LAW-ERA   a register-scoped record's `stage` predates the law row's
#                   declared era window  [FAIL]
#
# Resolution, mirroring the gate's existing clause resolutions:
#   for each law row with kind == "era" (RGL-05), read the register it governs
#   (`register:`), the era it declares (`consequence:` names E1; the row carries
#   no machine field today, so the draft adds one) and then, per packet record
#   whose own `register:` equals that register, compare the record's `stage`
#   against the declared floor using the packet's `eras` ordering (the same
#   `_era_index` shape lexicon-coverage-audit.py:847 already uses).
#   A record below the floor -> FINDING D4L-LAW-ERA: FAIL — ...
#
# RGL-05 would gain the machine-readable field the leg reads:
#     era_floor: "E1"
# (QREG-05..08 already carry a bare `era_rule: "E1"` and QREG-04 carries the
#  full sentence `era_rule: "a stamp form is available_from E1"`; the
#  `register_law` RGL-05 row carries no such field. The draft adds the field to
#  the law row, not to the registers block.)
#
# Selftest pair required by the gate's own discipline (it already carries
# delivered-*-tamper controls): an E0 stamp record fires, an E1 stamp record is
# silent. Control A/B above are the two directions, already measured.
```

**Owed:** the rule's own binding — which block owns the era floor (`registers`
QREG-04 already states "a stamp form is available_from E1" in its machine-readable
`era_rule` at `packet.d4.yml:1366`) versus which row the gate reads it from — is a
design decision the D block should make, not this spare. Named, not absorbed.

### 2.2 `head2`'s proper domain is **1 of 62**, not empty — a correction

`SCORECARD.md:329` (r26) records "head2 empty proper domain" as a named gap.
`reports/round-26/register/review.md:99` states it as "`head2` has an empty
proper domain over the delivered tree" with "`head2(form)==form` (identity, not
a derivation): 59 of 62".

**Re-measured independently by this seat, using the gate's own `op_head2`:**

```
$ python3 -c "<load tools/gates/argot-derivation-gate.py; call op_head2>"
lexicon terms: 62
head2 identity count: 61
head2 PROPER domain: ['haitun']
op_head2('saalumi') = 'saalu'
op_head2('tikmes')  = 'tikmes'
```

So the proper domain is **1** (`L-48 haitun`), not zero — the r26 count of 59
predates the r26 landing itself and the later additions (62 terms now vs 62
then, but the identity set differs). `op_head2('saalumi') == 'saalu'`
reproduces the forecast's own worked row exactly, so the operation is correctly
implemented; the gap is that the **delivered** tree offers it essentially no
work to do. The r26 finding's *substance* stands (a `head2` stratum over this
tree would be a stratum of unchanged words); its *number* is stale by one. This
is a calibration fact, recorded so no D seat re-states "empty" as measured.

### 2.3 `F-6` (`derived_forms` / `derived_ok`) is still not delivered

`reports/round-17/d4/design-brief.md:306-307` fixes signature (b) as "the
coverage block reports `derived_forms` and `derived_ok` counts that agree".
Measured:

```
$ for t in derived_forms derived_ok derived_pairs; do …; done
derived_forms    packet=0 typed=0 tools=0 examples=0
derived_ok       packet=0 typed=0 tools=0 examples=0
derived_pairs    packet=0 typed=0 tools=5 examples=0
```

`derived_forms`/`derived_ok` occur **only** in filed round-17/19/25 report prose
(`grep -rl` over the repo → `reports/round-17/d4/design-brief.md`,
`reports/round-19/integration/d4-lessons-entry.md`, and six `reports/round-25/`
files) — never in a delivered artifact or a gate. The live gate prints
`derived_pairs`, a **different key set** from the forecast's, exactly as
`reports/round-25/argot/delta.md:255` recorded. This is an honest, named,
permanent delta of the forecast, not a defect: the leg's contract is its own and
is documented. It should not be "fixed" by renaming a key to match a superseded
forecast.

## 3. What the D block should do instead — the block's real work order

Stated as this spare's recommendation; the integrator decides.

1. **Do not re-author the register forms.** They exist (8 forms, 8 derived
   pairs, both replay legs green). Any re-authoring moves the packet digest and
   re-opens the four-site pin cascade r26 measured, for zero depth gain.
2. **The one live depth gap is the era leg (§2.1).** It is bounded, it has a
   measured two-way control, and it has a named owner in two filed rounds
   (`RL-8`). It is the only item in this census where a *capability* is missing
   rather than a *number* being stale.
3. **Correct the claim record, do not silently absorb it.** `claims.json` is
   digest-pinned and this seat may not edit it (filed bytes / declaration). The
   integrator should carry §1 into the round's verdict: claim D as written is
   **unprovable-as-stated**, because its `before` is false and its
   `after_required` is already met. The honest verdict is either a restated
   claim (the era leg) or an honest **rejected/unprovable** on the claim as
   declared — never a forced pass (`REGIMEN.md:42-43`).
4. **Leave `head2` and `F-6` alone.** §2.2 and §2.3 are named deltas, not
   defects; both are already filed with owners and neither is closeable without
   superseding a filed round-17 design byte (which this lane may not do).

## 4. What this seat did **not** do

- Did not write, edit, or create any tool, gate, packet, component, fixture,
  pin, `expected-holds.json` row or sibling fragment. The two controls of §2.1
  and the one of §2.1's positive control live under `.scratch/d06/` (gitignored).
- Did not edit `reports/round-36/claims.json`, `targets.json`, or any filed
  round-1..35 byte. `git status --porcelain` at the stamp showed only
  `?? reports/round-36/`.
- Did not run any `reports/round-*/run-validation.py` in-tree (F-C13-1). No
  round-36 runner exists yet (`ls reports/round-36/run-validation.py` → no such
  file), so the counting command named in claim D is not yet executable; §1 uses
  the underlying gate commands directly instead.
- Did not commit, push, install, or reach the network.
- Did not resolve the era-floor ownership question in §2.1 — reported as
  contested scope per `AGENTS.md`.

## 5. Digest ledger (the bytes every reading above binds to)

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287  tools/gates/lexicon-coverage-audit.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
```

`tools/gates/argot-derivation-gate.py` at `b5406bcd…` is **byte-identical** to
the digest `reports/round-27/law/impl-8.md` §4 recorded for it, so the readings
here are on the same gate the r27 filing measured.

Worktree state at the stamp: `ce103bf`, `git status --porcelain` → only
`?? reports/round-36/`.

## 6. Counting commands for this file

```bash
# §1 — the claim's before/after, live
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml ; echo "exit=$?"
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml ; echo "exit=$?"
python3 tools/gates/register-law-gate.py --selftest | tail -1
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
python3 -c "import json;print(json.load(open('examples/culture-d4/expected-holds.json'))['active_pin_generation'])"
grep -n "register-stratum\|register-law\b" SCORECARD.md | head

# §2.1 — the era leg, both directions
python3 tools/gates/lexicon-coverage-audit.py .scratch/d06/packet-E0-stamp.yml ; echo "exit=$?"   # 1 (control A)
python3 tools/gates/lexicon-coverage-audit.py .scratch/d06/packet-E0-both.yml  ; echo "exit=$?"   # 0 (control B)
python3 tools/gates/argot-derivation-gate.py .scratch/d06/packet-bad-deriv.yml | grep '^FINDING'  # live positive control

# §2.2 — head2's proper domain
python3 -c "
import importlib.util,re
s=importlib.util.spec_from_file_location('ag','tools/gates/argot-derivation-gate.py')
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
lex=open('examples/culture-d4/packet.d4.yml').read().split('\nlexicon:',1)[1].split('\nlayers:',1)[0]
t=re.findall(r'term: \"([^\"]+)\"',lex)
print('proper:',[x for x in t if m.op_head2(x)!=x])
print('saalumi ->',m.op_head2('saalumi'))"

# §2.3 — F-6
for t in derived_forms derived_ok derived_pairs; do
  printf "%-16s packet=%s tools=%s\n" "$t" \
    "$(grep -c -- "$t" examples/culture-d4/packet.d4.yml)" \
    "$(grep -rho -- "$t" tools/ | wc -l)"; done

# §5
sha256sum tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py \
  tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml \
  examples/culture-d4/components/04-lexicon.yml examples/culture-d4/components/13-register-law.yml
git status --porcelain
```

## Owed

- `reports/round-36/depth/D06-era-leg-draft.patch` — the applied-form diff for
  the §2.1 fenced draft, **not owed by this spare**: §2.1 drafts the leg as a
  fenced block only (the mission is gap-fill; corpus/tool changes are the
  integrator's to apply, `targets.json` `shared_rules`). The D block's own
  executor/verifier seats (D03/D07) own the isolated-copy application and the
  two independent verifications. **Owner: the r36 D block integrator.**
- The era-floor **ownership decision** of §2.1 (`registers` QREG-04 vs the
  `register_law` RGL-05 row as the machine-readable source) — a design decision,
  not a measurement. **Owner: the D block planner (P01) / the integrator.**
- `reports/round-36/run-validation.py` does not exist at this stamp, so claim
  D's declared counting command cannot be run. §1 substitutes the underlying
  gate commands. **Owner: the r36 validation-leg seat (S01).**
- Claim D's `before`/`after_required` as declared in `claims.json` are falsified
  by §1 and the declaration is digest-pinned; the integrator must carry this
  into the round verdict rather than force a pass. **Owner: the r36 integrator.**

## Citations

- `reports/round-36/claims.json:16-21` — claim D's `before`, `after_required`,
  counting command, thresholds.
- `reports/round-36/targets.json:22` — seat `D06` mission ("Spare gap-fill
  across the D block"), `out`, and `shared_rules:3-10`.
- `SCORECARD.md:312` — the r25 empty-domain record the claim quotes.
- `SCORECARD.md:329,345,363,400` — the r26/r27/r28/r30 rows that supersede it.
- `reports/round-26/register/rules.md:107-128` — `REGISTER-ERA-01` specified and
  its control C-E1 measured ("the gate emits **no era finding** — it has no era
  concept").
- `reports/round-27/law/impl-8.md:68` — `RL-8`, the era leg, owner "whoever
  grows the leg".
- `reports/round-26/register/review.md:99-160` — `RD-3` (head2's domain) and
  `RD-4` (`RL-3`, the syllabifier disagreement).
- `reports/round-25/argot/delta.md:255` — `derived_forms`/`derived_ok` still 0,
  "the gate's coverage line uses `derived_pairs` instead, a different key set
  from the forecast's".
- `reports/round-25/argot/current-state.md:120-146` — the r25 argot token
  census this file's §2.3 re-measures.
- `reports/round-17/d4/design-brief.md:301-310` — Δ3, F-1..F-8, the signature
  `derived_forms`/`derived_ok`.
- `examples/culture-d4/packet.d4.yml:278-289` — `derivation_ops` and the
  `head2`-is-unused note.
- `examples/culture-d4/packet.d4.yml:1329-1431` — the `registers` block
  (QREG-01..QREG-08). QREG-04 is at `:1362-1371` and carries the machine-readable
  `era_rule: "a stamp form is available_from E1"` at **`:1366`**; QREG-05..08
  each carry a bare `era_rule: "E1"` (e.g. `:1426`).
- `examples/culture-d4/packet.d4.yml:2788-2867` — the `register_law` block
  (RGL-01..RGL-05), including RGL-05's era consequence.
- `examples/culture-d4/packet.d4.yml:1274-1304` — `STAMP-REVERSE` /
  `STAMP-LENGTHEN` with `available_from: "E1"` (the construction-availability
  surface control A/B turns on).
- `tools/gates/lexicon-coverage-audit.py:846-867` — the `D-stage-mismatch`
  resolution control A fires, and the `_era_index` shape §2.1's draft reuses.
- `tools/gates/typed-pipeline-gate.py:517-541` — the `L3b-argot` leg that wires
  the argot gate into the pipeline; `:1397-1472` — its mirror + selftest.
- `tools/check-gate-battery.py:130` — `REGISTER_LAW_GATE_NAMES`, the law gate's
  battery registration.
- `REGIMEN.md:42-43` — "never force a pass"; the honest-verdict rule §3.3
  invokes.
- `reports/round-36/depth/D09-gap-fill.md` §1, §5 row A-6 — the sibling spare's
  independent stale-premise measurement and its `RL-8` description.
- `reports/round-36/depth/D01-design.md` §0 — the third seat's statement of the
  same headline.
- Commands: all of §6, run by this seat at 2026-10-19T09:2xZ, worktree `ce103bf`.
