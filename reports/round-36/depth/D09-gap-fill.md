- Seat: D09 | executor | claim D | date 2026-10-19 | baseline ce103bf

# D09 — spare gap-fill #2: the register-form domain census, and one live defect in it

Mission (`targets.json` D09): "Spare gap-fill #2." The D block's critical path is
claim D, whose declared `before` is *"Register-form domain empty
(`reports/round-25/argot/` + SCORECARD r25 row)"* (`claims.json:18`). This
fragment fills the seam no other D seat is assigned: **measure that premise
against the delivered bytes**, and census what of the round-17 register forecast
is actually present, absent, or drifted at the current tree. Everything below is
a command output or a `file:line`; nothing is inferred from a filed report's
prose alone.

## 1. The claim's `before` premise is stale — the domain was filled in r26

The r25 record is real and correctly quoted: SCORECARD.md:312 (r25 depth row)
reads "the register-form domain in the delivered D4 packet is **EMPTY** (the
register class was design-forecast, never built into components)". That was true
at r25's tree. It stopped being true one round later.

Measured at the baseline (`ce103bf`), the `stamp` register is **present and
populated**:

| surface | count | evidence |
|---|---|---|
| register forms (lexicon records with `register: "stamp"`) | **8** | `examples/culture-d4/packet.d4.yml:1009,1031,1053,1075,1097,1119,1141,1163` (L-56, L-57, L-55, L-58, L-59, L-60, L-61, L-62) |
| of those, records carrying the `derived_from` + `derivation` pair | **8** | same lines; each has `derived_from:` and `derivation: {op: …, base: …}` |
| `doublet_of` facts (base back-pointer) | **8** | `packet.d4.yml:1024,1046,1068,1090,1112,1134,1156,1178` |
| `registers` block records (QREG-01..08) | **8** | `packet.d4.yml:1331,1341,1351,1362,1373,1388,1403,1418` |
| `register_law` rows (RGL-01..05) | **5** | `packet.d4.yml:2790,2807,2823,2839,2854` |
| `contract.record_fields.lexicon` now declares `derived_from`, `derivation`, `doublet_of` | yes | `packet.d4.yml:39-42` — the exact fields r25's delta said "do not exist" (`reports/round-25/argot/delta.md` A-3) |

**Git evidence for when it flipped.** The r26 *declare* commit `1ad491a` still
has the empty tree; the r26 *admit* commit `4f09c99` ("round-26: admit D/O/C —
register stratum closes the r17 forecast") added all 8:

```
$ git show 1ad491a:examples/culture-d4/packet.d4.yml | grep -c 'L-55'   → 0
$ git show 1ad491a:examples/culture-d4/packet.d4.yml | grep -c '^registers:' → 0
$ git log --oneline -S'id: "L-55"' -- examples/culture-d4/packet.d4.yml
4f09c99 round-26: admit D/O/C — register stratum closes the r17 forecast; r5 pin chain (devin)
```

So the premise `claims.json:18` quotes was superseded at `4f09c99`, three loops
before this round. It is a **stale reading carried forward from a filed round**,
not a live gap. The D block's build work (D01–D08) is therefore *content
authoring over a domain that already has 8 instances*, and the r25 SCORECARD row
at :312 stands as a correct historical record of r25 that a r36 reader must not
read as current state. (No filed byte is edited by this fragment; this is a
reading correction for the integrator's `before→after`, matching the r23/r26
precedent where a stale filed reading was recorded as superseded.)

## 2. The legs are green on the populated domain — measured, not assumed

All commands run from the lane root with `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; the tree was not written to.

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0
$ python3 -B tools/gates/argot-derivation-gate.py --selftest          → selftest: 27/27 checks passed, exit 0
$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0
exit=0
$ python3 -B tools/gates/register-law-gate.py --selftest             → selftest: 45/45 checks passed, exit 0
$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
summary: 20/20 legs passed                                       exit=0
$ python3 -B tools/assemble-culture-d4.py --selftest                 → selftest: 81/81 checks passed, exit 0
$ python3 -B tools/assemble-culture-d4.py --check
packet.d4.yml: byte-identical deterministic assembly              exit=0
```

The r25 "empty domain" note in SCORECARD.md:312 is thus **contradicted by the
delivered artifact** the same row's re-run command (`python3
reports/round-25/run-validation.py`) would have to be re-read against: the
argot leg is not "standing ready over an empty domain", it replays 8 real pairs
with 0 violations. Note the ledger move in `derived_pairs`: r25 filed
`derived_pairs=0` (`reports/round-25/regression.md:76,117`); live is 8.

**Composition of `register_scoped=14`** (the counter is not self-explanatory, so
it is resolved here rather than left as a number): 8 `stamp` forms +
6 loan-layer forms — `L-49..L-52` scoped `trade`, `L-53`/`L-54` scoped `craft`
(resolved through `loan_layer`→`layers.register` by the gate's own
`record_register`, `tools/gates/argot-derivation-gate.py:365-389`). Measured by
calling the gate's own reader:

```
register_scoped: 14
  lexicon L-49 trade | L-50 trade | L-51 trade | L-52 trade | L-53 craft | L-54 craft
  lexicon L-55 stamp | L-56 stamp | L-57 stamp | L-58 stamp | L-59 stamp | L-60 stamp | L-61 stamp | L-62 stamp
```

## 3. The one live defect this seat found: QREG-03's law text carries a stale numerator

`packet.d4.yml:1356` (rendered from `components/04-lexicon.yml:252`, the QREG-03
row) states:

> "The rule is total over the two delivered axis values and is not total in
> effect: **13 of the 54** delivered lexicon records yield an unusable form, so
> each form is checked individually (`reports/round-26/register/review.md`
> section 3)."

**The denominator is correct; the numerator is stale.** Verified by
reproducing the r26 predicate at both revisions (both axis operations, legality
via the gate's own `syllabify`/`is_legal_syllable`, exact-collision against the
delivered term set, plus the D2B-03 fixture sweep list quoted at
`components/04-lexicon.yml:22`):

```
1ad491a: lexicon=54 usable=41 unusable=13   ← reproduces the filed figure exactly
HEAD   : lexicon=62 usable=33 unusable=21
```

So `41 of 54` / `13 of 54` was a **correct reading of r26's pre-landing tree**,
and the same sentence in the delivered packet is now off by eight.

**The delta is fully explained, and it is self-referential.** The 8 newly
unusable ids are exactly the 8 base records of the 8 register forms — the
register forms collide with their own bases:

```
base ids of the 8 register forms: ['L-02','L-09','L-16','L-37','L-38','L-39','L-42','L-43']
newly unusable at HEAD          : ['L-02','L-09','L-16','L-37','L-38','L-39','L-42','L-43']
EXACT MATCH: True
```

Each of the 8 register terms occurs exactly once as a delivered term
(`grep -c 'term: "tuum"' packet.d4.yml` → 1, and likewise kit/lom/nees/huum/mees/
reek/saam), so applying the axis rule to a base now yields a form that *equals a
delivered register form* — a collision that did not exist before the stratum
landed. This is the round-26 landing's own cost, and it is the round-26
**review.md §3's own class** ("Colliding (5 records): the derived form equals a
delivered form") enlarged from 5 to 13 members by the very landing that quoted
it. The sentence is not wrong about its method; it is wrong about its count, and
the number it needs is 21, not 13.

**Disposition: filed, not repaired** (shared `examples/` bytes are the
integrator's; this seat writes only its own `out` path). The exact draft for the
integrator is in §4. Note the denominator *must stay 54*: the rule's input
domain is the plain-scoped axis-bearing set, which is byte-identical at both
revisions — measured `1ad491a` vs `HEAD` → identical 54-element id set,
`only in HEAD: []`, `only in 1ad491a: []`. A fix that also moved the denominator
would be a new defect.

## 4. Integrator draft (fenced; NOT applied by this seat)

Replace the numeral only, in both the component and its rendered packet row.
`reports/round-26/register/review.md` is a **filed** round and stays untouched;
the citation to it may stay as the method's provenance, but the live count must
not be attributed to it.

```yaml
# examples/culture-d4/components/04-lexicon.yml:252  (QREG-03, law: field)
# from:  "…is not total in effect: 13 of the 54 delivered lexicon records yield an unusable form, so each form is checked individually (reports/round-26/register/review.md section 3)."
# to:    "…is not total in effect: 21 of the 54 delivered lexicon records yield an unusable form at the current tree — 8 of them because the base of a delivered register form now collides with that form — so each form is checked individually (method: reports/round-26/register/review.md section 3, whose 13-of-54 count was measured on the pre-landing tree and is superseded here, not rewritten)."
```

Re-render with `python3 tools/assemble-culture-d4.py`, then re-pin as **new
rows** (never in place) for `examples/culture-d4/expected-holds.json`
`pin_generations`, `examples/culture-d4/typed-labels.d4.yml` `assembly.packet_sha256`,
and `examples/culture-d4/packet.d4.typed.yml`. Live digests at this baseline, for
the re-pin diff:

```
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
```

The law text is a **prose field inside a hashed artifact**, so the re-pin
cascade is mandatory and the D04/D08 re-pin seats' census should be checked
against these three paths.

## 5. Honest census: what of the r25 forecast is *still* absent

Filing a "the domain is filled" reading without this table would overstate the
state, so the still-missing forecast elements are enumerated. Each is a count at
the baseline; `examples/` and `tools/` are searched tree-wide.

| r25 element | filed verdict (`reports/round-25/argot/delta.md`) | live at ce103bf | evidence |
|---|---|---|---|
| A-4 register-scoped `<id>#plain`/`<id>#quote` slots | NOT DELIVERED | **still absent** | `grep -c '#quote' packet.d4.yml` → 0; `#plain` → 0; `slot_ref` → 0 in the packet (the 7 `slot_ref` hits are D2's rank property, `examples/culture-d2/typed-labels.d2.yml:1016`) |
| A-5 `doublet_of` as a packet fact | NOT DELIVERED | **closed** | 8 facts, `packet.d4.yml:1024-1178` |
| A-6 register-era clock / `D4L-ERA` | NOT DELIVERED | **still absent as an executable** | `grep -rl 'D4L-ERA' examples/ tools/` → 0 files. The era rule is *declared* (`QREG-04`, `packet.d4.yml:1362`; `RGL-05`, `:2854`) but no leg enforces it — the argot gate has no era concept. This is the named gap RL-8 (`reports/round-26/register/rules.md:187`, `review.md:226`), still open |
| A-7 `doublets`/`measures`/`oaths`/`sayings` packet keys | PARTIALLY DELIVERED | **unchanged: absent** | `grep -c '^doublets:\|^measures:\|^oaths:\|^sayings:' packet.d4.yml` → 0 for each; `registers:` is the one key that landed |
| A-1 the six argot loans `AL-01..06` | NOT DELIVERED | **unchanged: absent** | the loan forms `suk`, `akas`, `akim`, `aruk`, `isun`, `asum` → 0 files under `examples/` (the `man`/`nis` hits are unrelated substrings) |
| A-3 the eight quote names by `reverse` | NOT DELIVERED | **unchanged: absent** | `inak`/`usam`/`akas`/`akim`/`aruk`/`isun`/`asum` → 0; the `names:` block carries no `quote` key |
| A-10 the forecast's COUNT × QUOTE spine | NOT DELIVERED — superseded by path A | **unchanged** | the shipped spine is FIRE × MARK (`components/01-brief.yml`, SP-01/SP-02); this is the recorded root cause, not a defect |

**Reading.** The r25 delta was not "nothing landed": three of its elements
(A-2's derivation *mechanism*, A-5's `doublet_of`, and the Δ1 register
*admissibility* half) were closed by r26–r30 in the **furnace-league** spine, not
in the forecast's weigh-court spine. The elements that stay absent (A-1, A-3,
A-4's quote slots, A-6's era leg, A-7's four keys) are exactly the ones whose
identity is bound to the weigh-court culture that never shipped. So "the register
forecast was closed" (SCORECARD.md:329) and "the r25 delta is still largely not
delivered" are both true statements about **different halves of the same
forecast** — a distinction the SCORECARD's r25 and r26 rows do not currently
draw, and which this fragment records so the D block's `after_required` is not
read as "all of A-1..A-11 closed".

## 6. Observation filed, not ours: a concurrent in-tree runner clobbered a filed receipt

While this seat was measuring, `reports/round-35/validation.json` — a **filed**
byte — was transiently rewritten by a **sibling seat's** in-tree runner run.
This is a F-C13-1-class event and is recorded here because this seat observed it
and because it touches the same tree the D block's re-pin cascade reads.

Observed, with timestamps (all 2026-10-19, -03:00):

```
06:29:26.446612708  mtime of reports/round-35/validation.json
$ git status --porcelain
 M reports/round-35/validation.json
$ git diff reports/round-35/validation.json
-            "measurement": {
-              "manifest": "pending-by-construction: integrator files the MANIFEST row in the same close pass"
-            },
+            "measurement": {},
-  "measured_at_utc": "2026-10-19T06:19:14.685566-03:00",
+  "measured_at_utc": "2026-10-19T06:29:26.436020-03:00",
```

**Mechanism, from `ps` (not inferred).** Multiple sibling seats were running
`reports/round-{26,33,34,35}/run-validation.py` concurrently, several with the
**lane root** as cwd rather than an isolated copy — e.g. a `ca01` seat
(`.scratch/ca01`, cwd shown as the lane root for its runner child) and an `x01`
seat at `.scratch/x01-iso2`. `reports/round-35/run-validation.py:502-505` writes
`reports/round-35/validation.json` in place, guarded by
`tools/harness/receipt_guard.py` (refuses a committed receipt unless
`REFRESH_RECEIPTS=1`, `receipt_guard.py:144-147`). The clobber therefore came
from a runner whose cwd was the lane root and which passed the guard — the
`--check` path prints and returns before the write (`run-validation.py:498-501`),
so a plain `--check` in an isolated copy is safe; a non-`--check` run at the lane
root is not.

**Current state: restored, not left damaged.** By 06:29:59 the file is again
byte-identical to HEAD (`git diff --quiet HEAD -- reports/round-35/validation.json`
→ IDENTICAL; blob `11f241a4…` == `HEAD:reports/round-35/validation.json`), and
`measured_at_utc` reads the filed `06:19:14.685566-03:00` with the
`pending-by-construction` manifest text intact. The damage was **transient** —
either the sibling seat's own isolated-copy run overwrote the lane-root artifact
back, or a later run of the same runner at a clean state restored it. The
observation stands as a **hazard window ~06:29:26Z, duration under ~35 s**, not
as a persistent defect.

**Why it matters to this round.** (1) The r35 receipt is a **counting-command
surface** the Ca block recounts; a reader who sampled it inside that window would
have read `X1-X3 measurement: {}` — a *different* claim-leg measurement — and
would have filed a spurious mismatch. Ca01/Ca02 should timestamp their reads.
(2) It is the same hazard class the D34/O claim's `receipt_guard_adoption.py`
inventory names. This seat ran **no** round runner (F-C13-1 respected) and made
no write to any `reports/round-1..35/**` byte.

## 7. What this fragment does not claim

- It does **not** re-pin, re-freeze, or edit any `examples/`, `tools/`, or filed
  `reports/round-1..35/**` byte. The §4 draft is fenced for the integrator.
- It does **not** execute `reports/round-*/run-validation.py` in-tree
  (F-C13-1); no round-runner was run. `reports/round-36/run-validation.py` does
  not exist yet (`ls` → No such file or directory), so claim D's declared
  counting command cannot be run at this seat; the owed path is listed below.
- The 33/21 figure is **this seat's reproduction** of the r26 predicate, not a
  filed number. It is a second independent measurement; the method is stated so
  the D07/D08 verifiers can reproduce or contradict it. The one-step-short
  reproduction that reaches r26's *exact* filed 41/13 at `1ad491a` is the
  strongest evidence the predicate is faithful; the 21 is what the same
  predicate yields at HEAD.
- No canon, promotion, clearance, or closure verdict is made. The register's
  existence in any world is lore-shokunin's.

## Owed

- `reports/round-36/run-validation.py` — does not exist at this seat's write
  time, so claim D's declared counting command (`python3 -B
  reports/round-36/run-validation.py`, `claims.json:20`) could not be executed.
  Owner: the S01 integration scribe / round integrator. This fragment's own
  commands are the substitute evidence and are listed in §2.
- The §4 QREG-03 numeral fix is **owed to the integrator** (shared `examples/`
  bytes); the seat that lands it must also run the three-artifact re-pin cascade
  named in §4 as new rows.
- The A-6 era leg (RL-8) remains unimplemented and is **owed to a future D
  round**, not to this spare. Its declared rule rows (`QREG-04`, `RGL-05`) exist
  and are unenforced; the gap is named at `reports/round-26/register/rules.md:187`.

## Citations

All commands run 2026-10-19 from the lane root at `ce103bf`
(`git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`), with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

- `reports/round-36/claims.json:18` — claim D `before`: "Register-form domain empty".
- `reports/round-36/claims.json:20` — claim D counting command.
- `reports/round-36/targets.json` D09 — mission "Spare gap-fill #2", out `depth/D09-gap-fill.md`.
- `SCORECARD.md:312` — r25 depth row: "the register-form domain in the delivered D4 packet is EMPTY".
- `SCORECARD.md:329` — r26 depth row: "The round-17 register forecast CLOSED".
- `reports/round-25/argot/delta.md` — the A-1..A-11 filed delta table (rows A-1, A-3, A-4, A-5, A-6, A-7, A-10 quoted).
- `reports/round-25/regression.md:76,117` — r25 `derived_pairs=0`, `register_scoped=6`.
- `reports/round-26/register/review.md:63-95,222,226` — RD-2 "13 of 54 unusable", RD-5b RL-8 era leg absent.
- `reports/round-26/register/rules.md:187` — RL-8 named.
- `examples/culture-d4/packet.d4.yml:39-42` — `derived_from`/`derivation`/`doublet_of` in `contract.record_fields.lexicon`.
- `examples/culture-d4/packet.d4.yml:1009,1031,1053,1075,1097,1119,1141,1163` — L-55..L-62 register forms.
- `examples/culture-d4/packet.d4.yml:1024-1178` — the 8 `doublet_of` facts.
- `examples/culture-d4/packet.d4.yml:1331-1418` — QREG-01..08.
- `examples/culture-d4/packet.d4.yml:1356` — the stale "13 of the 54" law text.
- `examples/culture-d4/packet.d4.yml:2790-2854` — RGL-01..05.
- `examples/culture-d4/components/04-lexicon.yml:22` — D2B-03 fixture sweep list (the 20 D2 forms used in the predicate).
- `examples/culture-d4/components/04-lexicon.yml:220-243` — the 8 register records; `:252` — QREG-03 source of the stale text.
- `tools/gates/argot-derivation-gate.py:365-389` — `record_register` (scope predicate); `:243` — `OP_FUNCTIONS`; `:153,217` — `syllabify`/`is_legal_syllable`.
- `git show 1ad491a:examples/culture-d4/packet.d4.yml` — 54 lexicon records, 0 `L-55`, no `registers:`.
- `git log --oneline -S'id: "L-55"' -- examples/culture-d4/packet.d4.yml` → `4f09c99`.
- Command outputs (verbatim in §2 and §3): argot gate D4 `register_scoped=14 derived_pairs=8 … violations=0` exit 0; argot `--selftest` 27/27; law gate `law_rows=5 … dangling=0 findings=0` exit 0; law `--selftest` 45/45; typed pipeline `20/20 legs passed` exit 0; assembler `--selftest` 81/81; assembler `--check` byte-identical; `sha256sum` of the three pinned artifacts (§4).
