- Seat: X02 | critic | claim cross | date 2026-10-19 | baseline 9bccc9b

# X02 — honesty critic: vacuous-pass hunt on the round-38 new coverage

Round 38, loop 1 position 6 (grok 403 out-of-credits; named deviation to
devin/deepseek-v4-1-flash-high — `reports/round-38/telemetry/availability-attempt-1.json`).
Write scope: this file only. No tool, gate, packet, component, pin, filed
round-1..37 byte, or freeze byte written; no commit, no push. Every probe below
ran against a **read-only** input: the live packet for the read-only gate runs,
and a scratch mutation under the gitignored `.scratch/x02/` for the negative
controls. No `reports/round-*/run-validation.py` was executed anywhere, in-tree
or in a copy (F-C13-1). `HEAD` = `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`.

**Verdict in one line.** The round's two claims each carry a **green-on-an-unchanged-tree**
acceptance shape. Claim D's era leg and F-6 counters cannot be accepted on a
green leg reading — I demonstrate the exact vacuous pass for both. Claim O's
stated discriminator ("only the r7 row names") is **false as written**: a second
filed row (r6) carries the same manifest/read-set mismatch, and the *existing*
`E2E-READSET` guard already fires on three other filed rows, so an unqualified
"only r7 names" reading will either fail or be satisfied by the wrong check.

---

## 0. The two claims' acceptance shapes, and the failure mode they share

| claim | declared acceptance (`reports/round-38/claims.json`) | why it can go vacuous |
|---|---|---|
| D | "the counters emit from the packet/components (or a documented equivalent the legs can count); the era leg runs; argot/law/typed legs green with the new coverage named" | "legs green" is **already true today** (measured §1). A runner that asserts green passes on an unchanged tree. |
| O | "selftest green with the new controls; r7 packet sha unchanged 45f57132…" | both halves are **already true today** (measured §3). Green + unchanged sha is satisfied by doing nothing. |

`REGIMEN.md` requires "falsifiable before→after"; both claims therefore need a
**negative control that goes red** (D) and a **named row that names and rows that
do not** (O), not a green reading. §1–§4 supply exactly those tests.

---

## 1. Claim D, leg 1 — the RL-8 era leg: **green is vacuous today, demonstrated**

RGL-05's own substance is "every stamp form is `available_from E1` … **an E0
stamp claim is a defect**" (`examples/culture-d4/components/13-register-law.yml:49`,
`packet.d4.yml:2865-2867`). The declared defect is *constructible*. I constructed it.

**Probe (all eight stamp forms flipped `stage: E1 → E0`):**

```
# scratch mutation only; L-55..L-62 each had `stage: "E1"` -> `stage: "E0"`
python3 -c "...re.sub on the eight  'id: \"L-5x/L-6x\"' blocks... stage: \"E1\" -> \"E0\"..."
# byte-diff confirmed: L-55 orig stage E1 -> probe stage E0 ; L-62 orig E1 -> probe E0
python3 -B tools/gates/register-law-gate.py   .scratch/x02/probe-e0-all.yml
→ coverage: .scratch/x02/probe-e0-all.yml law_rows=5 identity_rows=8 record_ids=183 \
            registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 \
            dangling=0 findings=0
→ exit=0
python3 -B tools/gates/argot-derivation-gate.py .scratch/x02/probe-e0-all.yml
→ coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 \
            violations=0 rule_holds=0
→ exit=0
```

**Finding (D/RL-8).** The exact defect RGL-05 declares produces **no finding and
no exit-code change** in either register leg. Neither instrument reads any dating:
`grep -n "stage\|era" tools/gates/argot-derivation-gate.py` returns only
docstring/spec prose (no `stage`/`era` field is read), and
`grep -n "available_from\|E0\|E1" tools/gates/register-law-gate.py` returns
**0 matches** for every one of those tokens. `kind: era` is a member of
`DECLARED_KINDS` (`register-law-gate.py:121`) but the gate grades only *membership*
in that set, never the dating a row asserts. This matches the filed RL-8 record
(`reports/round-26/register/rules.md` §5; `reports/round-27/law/impl-8.md:68`) and
`13-register-law.yml:57`'s own honest admission: "no gate executes these rows".

**Consequence for acceptance.** The D claim's `after_required` — "the era leg
runs" — **must be accepted only against a named negative control**: an E0-dated
stamp form must produce a finding (new id or a new law row), with the clean packet
unchanged. A submission that shows `register-law-gate.py` exit 0 on the live
packet has shown nothing that was not already true at `9bccc9b`.

**The near-miss worth naming.** Swapping RGL-05's own `kind: era → no-segment`
(both in `DECLARED_KINDS`) is **silent** — exit 0, findings=0. That is correct
behaviour for a membership check and is *not* itself a defect; it is named here so
no one reads the silent swap as the era gap. The era gap is the dating (§ above),
not the kind vocabulary.

**Controls that DO discriminate (so the D block has non-vacuous instruments to
cite):**

| probe (scratch mutation) | command | reading |
|---|---|---|
| break one derived form `L-55 term tuum → tuuun` | `argot-derivation-gate.py <probe>` | `FINDING D4L-ARGOT-DERIV: FAIL … declared chain 'lengthen' applied to 'tum' does not yield the candidate`; `violations=1`; **exit 1** |
| drop RGL-05 entirely | `register-law-gate.py <probe>` | `FINDING D4L-LAW-ROW: HOLD … RGL-05 is absent`; `findings=1`; **exit 1** |
| flip all 8 stamp forms to E0 | both legs | **exit 0, findings 0** — the gap |

---

## 2. Claim D, leg 2 — the F-6 counters: "emit" is not "consumed"; presence is vacuous

**State at baseline.** `grep -rn "derived_forms\|derived_ok" tools/ examples/` →
**no match (exit 1)**. The live projection's coverage block
(`examples/culture-d4/typed-labels.d4.yml:29-47`) carries
`typed_labels`, `labels_by_kind`, `rank_rules_*`, `reconciliation_records` — and
**no** derivation counters. Unchanged from the r36 census
(`reports/round-36/scout/K01-register-scout.md` §4 F-6).

**The consumption question (the vacuous-pass risk).** The claim's wording is "the
counters emit from the packet/components **(or a documented equivalent the legs
can count)**". If the D executors add two keys to a coverage block and stop, the
pass is vacuous — nothing reads them. Measured today:

- `grep -rn "derived_pairs\|derived_forms\|derived_ok" tools/ --include=*.py`
  (excluding frozen/expected mirrors) returns **only** `argot-derivation-gate.py`
  itself: the counter increment (`:567`), the coverage-hold guard (`:662`), a
  selftest assertion (`:835`), and the `coverage:` print (`:917`). **No consumer
  parses the argot gate's counters.**
- The typed pipeline's argot leg checks only that the sibling *answered*:
  `typed-pipeline-gate.py:1471` → `check(... "coverage:" in argot_probe.stdout)`.
  That is a **presence** test of the literal string, not a value test. Its other
  branch (`:517-541`) folds only `FINDING D4L-ARGOT-` lines into the verdict.
- The e2e renderer mines the projection's coverage keys by name
  (`exercise-handoff-e2e.py:2165-2188`: `typed_labels`, `labels_by_kind`,
  `findings_total`, …) — adding `derived_forms`/`derived_ok` to the projection
  would leave that reader untouched and the two keys **unread**.

**Acceptance test that is not vacuous (for the integrator).** The new coverage
must be accepted only if a named consumer (a) reads the counter and (b) goes red
when the value disagrees with the leg's own replay. A minimum discriminating pair:
a control where the emitter's `derived_ok` is forced to disagree with
`derived_pairs` minus `violations` must produce a named finding, and the clean
tree must not. "The key is present in the JSON" is not evidence; §2's grep is the
proof that presence alone is currently inert.

**Counting command is not yet runnable.** Claim D's third declared counting
command is `python3 reports/round-38/run-validation.py`;
`ls reports/round-38/run-validation.py` → **No such file or directory**. So that
command is `to-verify` until the integrator lands the runner, and per F-C13-1 it
must never be run in-tree regardless (isolated `git archive` copies only).

---

## 3. Claim O, leg 1 — "r7 packet sha unchanged 45f57132…" is **already true**

Measured in an isolated `git archive HEAD` copy (`.scratch/x02/`), never in-tree:

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
→ handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 \
   statuses=16/7/4 v2_subset=equal alias_leg=landed \
   packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
→ exit=0
```

That digest equals the pin in `reports/round-34/handoff/declared-in-r7/freeze.txt`
and `repin.json`. So the O claim's second threshold ("r7 default chain still exits
0 unchanged; r7 packet sha unchanged") is satisfied by **doing nothing**. It is a
guard against regression, not evidence the guard landed — and must not be counted
as one.

---

## 4. Claim O, leg 2 — the roster guard: the "only r7 names" expectation is **false**

### 4a. A second filed row carries the same mismatch

The guard's premise is a frozen baseline whose read set and the packet's own
component manifest disagree. Measured across **every** filed v3 row — the frozen
`packet.md`'s own "component digests in its assembly" count vs the frozen
`expected.json` `inputs` D4-component count:

| filed row | frozen packet.md declares (d4 digests) | frozen `inputs` D4 components | mismatch? |
|---|---|---|---|
| `reports/round-22/handoff/declared-in` | 12 | 12 | no |
| `reports/round-22/handoff/declared-in-r2` | 12 | 12 | no |
| `reports/round-26/handoff/declared-in-r5` | 12 | 12 | no |
| `reports/round-30/handoff/declared-in-r6` | **13** | **12** | **YES** |
| `reports/round-34/handoff/declared-in-r7` | **13** | **12** | **YES** |

(r6 raw lines: `13 component digests in its assembly` and `9 D2, 4 D3, 13 D4`; its
`inputs` holds 12 `culture-d4/components/*` paths. r5 says `12 component digests`
and `9 D2, 4 D3, 12 D4`.)

**Finding (O).** The O08 mission's expectation — "every filed frozen row (r2..r7)
replayed in isolation under the guard — **only the r7 row names**; others stay
green" — is **unsatisfiable against a manifest-completeness guard**: r6 names too.
The correct expectation is **r6 and r7 name; r2/r5 (and `declared-in`) stay
green**. As written, O08 would either report a false failure (guard fires on r6,
read as a regression) or force the guard to be narrowed until it misses r6 — i.e.
until it is vacuous on the very class the claim exists to catch.

### 4b. The existing guard already fires on three filed rows

Running each filed row's own baseline in the isolated copy:

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline <row>/expected.json --quiet
r2 (declared-in-r2) → exit 1  E2E-READSET: 1 read-set member(s) named by the frozen baseline
                              are not in the live read set: reports/round-20/handoff/claims-map.md
r5 (declared-in-r5) → exit 1  (same E2E-READSET, same member)
r6 (declared-in-r6) → exit 1  (same E2E-READSET, same member)
r7 (declared-in-r7) → exit 0  fields=16/16 … packet_sha256=45f5713261762a95…
```

**Finding (O).** The new manifest-vs-read-set guard must be **distinct from and
ordered against** the existing `E2E-READSET` supersession check
(`exercise-handoff-e2e.py:3825-3836`, message class `read-set-roster`). Two
consequences the O block must handle:

1. An isolation run against r2/r5/r6 **aborts at `E2E-READSET`** before any
   later-added manifest check is reached. So O08's "replay r2..r7 under the guard"
   cannot produce the intended reading unless the guard runs **before** the
   readset-supersession check, or the sweep bypasses the supersession abort. As
   specified, O08's r2/r5/r6 runs will report `E2E-READSET`, not a manifest verdict.
2. There are already **two** manifest→read-set presence checks,
   `exercise-handoff-e2e.py:1346` and `:3654`: "manifest row {artifact_id} names
   {path}, which is not in the read set". Both check the **manifest→readset**
   direction for rows the manifest lists. Neither checks the direction the O claim
   targets — that a *frozen baseline's* `inputs` cover the packet's **own**
   component manifest (`v3_mine_d4` extracts that manifest at `:2045-2056`;
   `v3_verify_component_digests` measures it at `:2208-2222`). So the guard is
   genuinely new — but the integrator must ensure it does not duplicate, or
   silently shadow, the two existing checks and the supersession abort.

---

## 5. What each claim must survive before it can be admitted

| # | claim | test that is not vacuous | why a green reading fails |
|---|---|---|---|
| 1 | D / RL-8 | E0-dated stamp form ⇒ **named finding, non-zero exit**; clean packet unchanged | flipping all 8 forms to E0 is silent today (§1) |
| 2 | D / F-6 | a **consumer** goes red when `derived_ok` disagrees with the leg's replay | no consumer reads any derivation counter today (§2) |
| 3 | D / counting | `reports/round-38/run-validation.py` exists and passes **in an isolated copy** | file absent at baseline (§2) |
| 4 | O / guard | **r6 and r7 name; r2/r5 green** | "only r7 names" is false — r6 mismatches too (§4a) |
| 5 | O / guard | the guard is reachable **despite** the `E2E-READSET` abort on r2/r5/r6 | those rows abort earlier today (§4b) |
| 6 | O / sha | r7 `45f57132…` unchanged | already true; regression guard, not evidence (§3) |

No axis is harmed by this fragment: it is read-only audit prose; it writes only
its own out path and scratch mutations under `.scratch/x02/`. It claims no
promotion, no canon, no clearance, no closure, and no verdict on whether the
round admits — that is the integrator's, against the tests above.

## Owed

- **Integrator — claim D acceptance test (RL-8).** Require the E0-stamp negative
  control before admitting "the era leg runs". Without it the claim is vacuously
  green at `9bccc9b`.
- **Integrator — claim D acceptance test (F-6).** Require a **named consumer** of
  the new counters, with a disagreeing-value control that goes red. Presence in a
  coverage block is inert today (measured §2).
- **Integrator — claim O acceptance test.** Correct the O08 expectation to "**r6
  and r7** name; r2/r5/`declared-in` green", and state the guard's ordering
  relative to `E2E-READSET`. Owner: integrator (the expectation lives in
  `targets.json`, which this seat does not edit).
- **Integrator — r6 manifest asymmetry.** The r6 frozen row declares 13 D4
  component digests in its packet but carries 12 in its `inputs` — the same class
  as r7. Whether this is a second filed defect or an artifact of the r6 freeze
  predating the 13th component (the component landed r27, `6c0ac44`; the r6 freeze
  is r30) is `to-verify`; either way it changes the O block's "only r7" premise.
  This seat reports it; it does not adjudicate it.
- **`to-verify` (blocked):** `reports/round-38/run-validation.py` does not exist,
  so claim D's third counting command could not be exercised. Not run in-tree by
  design (F-C13-1); the integrator lands and runs it in an isolated copy.
- **Not measured by this seat:** the D01/D02/O01 fenced patch drafts (not present
  at this seat's read) — this fragment audits the *acceptance shape* and supplies
  the negative controls; it does not review drafts it could not read.

## Citations

Files (sha256 as measured; cwd = lane root; `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`):

```
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223  reports/round-34/handoff/declared-in-r7/freeze.txt
```

Commands run (read-only over the live tree; mutations written only under
`.scratch/x02/`; no in-tree runner; no filed byte written):

```
git rev-parse HEAD                                              # 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # exit 0, derived_pairs=8 violations=0
python3 -B tools/gates/register-law-gate.py    examples/culture-d4/packet.d4.yml   # exit 0, law_rows=5 findings=0
python3 -B tools/gates/argot-derivation-gate.py --selftest                          # 27/27
python3 -B tools/gates/register-law-gate.py    --selftest                          # 45/45
grep -rn "derived_forms\|derived_ok" tools/ examples/                               # no match, exit 1
grep -n "available_from\|E0\|E1" tools/gates/register-law-gate.py                   # 0 matches each
# negative controls (scratch mutations):
python3 -B tools/gates/argot-derivation-gate.py .scratch/x02/probe-argot-tamper.yml # exit 1, D4L-ARGOT-DERIV, violations=1
python3 -B tools/gates/register-law-gate.py    .scratch/x02/probe-rgl05-drop.yml    # exit 1, D4L-LAW-ROW HOLD
python3 -B tools/gates/register-law-gate.py    .scratch/x02/probe-rgl05-kind.yml    # exit 0 (kind swap silent)
python3 -B tools/gates/register-law-gate.py    .scratch/x02/probe-e0-all.yml        # exit 0, findings=0  <-- the vacuous pass
python3 -B tools/gates/argot-derivation-gate.py .scratch/x02/probe-e0-all.yml       # exit 0, violations=0 <-- the vacuous pass
# isolated git-archive copy (.scratch/x02), v3 baseline sweep:
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                       # exit 0, packet 45f57132…
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-22/handoff/declared-in-r2/expected.json --quiet  # exit 1 E2E-READSET
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-26/handoff/declared-in-r5/expected.json --quiet  # exit 1 E2E-READSET
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-30/handoff/declared-in-r6/expected.json --quiet  # exit 1 E2E-READSET
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-34/handoff/declared-in-r7/expected.json --quiet  # exit 0
ls reports/round-38/run-validation.py                                               # No such file or directory
```

Source lines cited: `reports/round-38/claims.json` (claims D/O `after_required`,
`thresholds`, `counting_commands`); `reports/round-38/targets.json` (seat X02,
seat O08 "only the r7 row names", `shared_rules`); `REGIMEN.md` (falsifiable
before→after; no in-tree runner); `reports/round-38/telemetry/availability-attempt-1.json`;
`tools/gates/register-law-gate.py:121,635-643`; `tools/gates/argot-derivation-gate.py:567,662,835,917-919`;
`tools/gates/typed-pipeline-gate.py:517-541,1471`; `tools/exercise-handoff-e2e.py:1346,157-170,1939-1953,2045-2056,2165-2188,2208-2222,3654,3825-3836`;
`examples/culture-d4/packet.d4.yml:2854-2867` (RGL-05 block); `examples/culture-d4/components/13-register-law.yml:49,55-57`;
`examples/culture-d4/typed-labels.d4.yml:29-47`; `reports/round-34/handoff/declared-in-r7/{freeze.txt,repin.json}`;
`reports/round-26/register/execution-3.md` (F-6 "not designed"); `reports/round-25/argot/forecast.md:37` (F-6 requirement);
`reports/round-36/scout/K01-register-scout.md` §4; `reports/round-37/adj/A01-freeze-adjudication.md`;
`reports/round-30/handoff/declared-in-r6/packet.md` (`13 component digests`, `9 D2, 4 D3, 13 D4`).
