- Seat: X00 | connector | cross | date 2026-10-19 | baseline ac47c78

# Collision matrix + integration order

Axes in play: **operability (O)** and **coverage (C)** only; freshness stays
paused (`reports/round-42/claims.json:9,11,26`). This is a dependency, scope and
sequencing map — not a claim verdict. Every number below was measured read-only
by this seat at HEAD `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`
(`git rev-parse HEAD`), tree state `?? reports/round-42/` only
(`git status --porcelain`) — **zero corpus staging at this stamp**.

Vantage: this fragment was first written when only 3 files existed in
`reports/round-42/` (claims, targets, telemetry/dispatch-declared.json). Peers
landed during the write; §4 is the reconciliation against that landed state, and
C1 has been **corrected** — the host question is answered, not open. Vantage at
final cut: 26 files (listed in §4). This is a partial-time snapshot, not a
seat-completion census.

## 1. Write-path matrix — 32 distinct `out` paths, zero byte collisions

All 32 `out` values in `targets.json` are distinct; `cross/` holds X00 and X01 as
separate files. Shared surfaces and their single owner/applier:

| shared surface | draft owner | applier | rule |
|---|---|---|---|
| `corpus/knowledge/myth-symbol/*.md` (+4 new) | C01–C04, fenced | integrator | seats never stage (`shared_rules`; r39 stray-staging row) |
| `corpus/README.md` rev 2.4 | C06 delta block only | integrator | row bytes byte-equal to the landed `- topic:`; sweep green is post-apply |
| **the extractor host (unassigned — see C1)** | O01, fenced | integrator | filed r19/r27/r28 instruments are read-only filed bytes |
| `reports/round-40/op/defect-queue-v2.json` | O08 draft | integrator | **route conflict — see C5** |
| `LOG.md`, `SCORECARD.md`, `MANIFEST.json`, fleet `.ufo/` | — | parent only | workers write assigned fragments only (`AGENTS.md:3-6`) |
| filed bytes r1..41 / `corpus/lessons/*.md` / `tools/gates/frozen/**` / `declared-in-r7` | read-only | — | absolute (`shared_rules`) |

## 2. Content collisions (the binding matrix)

### C1 — The extractor host is a NEW file under `tools/harness/`; no filed byte can be it (RESOLVED — corrected after K01 landed)

`claims.json:16` requires "the fixed extractor durable (its owning instrument
identified by the wave — likely the r39 C12 runbook's resolver or a
tools/harness couples checker; **the wave confirms the host**)". **K01's scout
answers it** (`reports/round-42/scout/K01-n6-scout.md:103-110,230-240,326`), and
this seat re-verified the load-bearing claim by importing the module directly.
The constraints, in order:

- The instruments the r39 finding names are **filed read-only bytes**:
  `reports/round-19/audit/entry-audit.py:74-96` (the single-line
  `couples_targets`), `reports/round-27/audit/entry-audit.py`,
  `reports/round-28/audit/entry-audit.py`. `shared_rules` forbids editing
  `reports/round-1..41/**`. The fix **cannot** land there (K01 D1d names all
  three copies — a fix in one leaves the others divergent).
- `reports/round-35/cov/C12-audit-runbook.md` is a *runbook fragment*, not code:
  `grep -n 'couples_refs\|def couples\|resolver'` on it returns **no match**. Its
  §1 checklist also declines to install anything ("the instrument is **drafted
  here as bytes** and is deliberately not installed under `tools/`").
- **The correct precedent already exists in-repo.** `tools/gates/provenance-audit.py:244-261`
  `field_block()` is indentation-bounded (`INDENT_RE = r"^[ \t]+\S"`, `:77`),
  stops at the next `FIELD_RE` line (`:76`), and stops at a non-indented line.
  Re-verified by this seat (importing the module read-only, 2026-10-19):
  `field_block(lines,"couples")` on the wrapped entry returns `present=True` and
  the block text; its `.md` tokens are `{prosody.md, sound-change.md,
  sound-symbolism.md, writing-systems.md}`, and after the hyphen rejoin
  `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}` —
  **the correct 4**. It currently uses the block only for a *presence/emptiness*
  check (`:318-324`) and never extracts tokens, so it is the **template**, not
  the resolver. It is a couples-*presence* gate, not the N6 host.
- The r40 queue row itself defers: `owner: "future resolver round"`,
  `next_touch: "a resolver fix round"` (`defect-queue-v2.json:362-369`), and the
  sibling row names the r43/r44 successor instrument
  (`defect-queue-v2.json:323-331`).

**Binding consequence.** The fix must be a **new file** under `tools/harness/`
(beside `round_runner_conformance.py`), authored to the `field_block()` stop
semantics — indentation-bounded, blank-line- and next-field-terminated — plus
the hyphen rejoin and the Tier-2 fallback. O01 must emit a fenced diff
**creating** that file, never patching a filed r19/r27/r28 path. `tools/gates/`
is writable but `provenance-audit.py` is the wrong leg (it has frozen snapshots
under `tools/gates/frozen/provenance-audit/` and a fixture suite that would also
need review).


### C2 — The parser recipe is under-specified, and the claim's own threshold can be satisfied by a WRONG implementation

`claims.json:18` sets the threshold "the wrapped field reads **4/4 targets**".
Measured over all 220 entries, four candidate extractors give:

| extractor | corpus refs | direct | fallback | unres | wrapped-field tokens |
|---|---|---|---|---|---|
| **A** single-line (filed r19/r39) | 2607 | 2435 | 166 | 6 | **`[]` — 0 tokens** |
| **B** block, indent-stripped, **no hyphen join** | 2611 | 2437 | 166 | 8 | `prosody.md`, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md` |
| **C** block + indent-strip + **hyphen-newline join** | 2611 | 2437 | 166 | 8 | `sound-change.md`, **`tone-prosody.md`**, `sound-symbolism.md`, `writing-systems.md` |
| **D** terminator = "next header field" (the queue's literal wording) | 2615 | 2441 | 166 | 8 | `prosody.md`, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md` |

Two traps, both live:

1. **The count is not the criterion — the identity is.** B and D each read
   **4 tokens**, so a selftest asserting only "4/4 targets" goes **green while
   still wrong**: both report the mangled `prosody.md` instead of
   `tone-prosody.md`. The source bytes split the name across the wrap
   (`sound-change.md, tone-` / `prosody.md`, `phonetics-phonology.md:76-77`).
   Ca04 lists the four names as `sound-change.md`, `tone-prosody.md`,
   `sound-symbolism.md`, `writing-systems.md`
   (`reports/round-39/calib/Ca04-verify.md:80-86`). **Only C produces that set.**
   O02's positive control must assert token **identity**, not arity.
2. **The queue's literal wording over-reads.** "block extraction through the
   next header field" (= D) adds **4 spurious refs** corpus-wide (2615 vs 2611)
   for 3 entries whose `couples:` line is the *last* header field:
   `linguistics/language-shift-obsolescence-revival.md` (absorbs
   `reports/round-8/freshness/R8-F01-receipt.md`),
   `linguistics/numerals-and-measures.md` (absorbs its own filename),
   `linguistics/sound-symbolism.md` (absorbs `sound-symbolism.md`,
   `synthesis/myth-to-language-derivation.md`). The correct terminator is
   **blank line OR next field line** — 8 entries have body text between the last
   header field and the first `## ` heading (measured).

Corroboration that C is the intended shape: the r35 C14 instrument's own block
parser is `frontmatter_block()` terminating at `## ` (`C14-audit-6-10.md:209-222`)
— but note it terminates at the *heading*, not the blank line, so it inherits the
same over-read as D for those 3 entries. Neither filed instrument is correct as
written; the fix is a **third** shape.

### C3 — The census baseline is mis-stated: `2504` is an r39-era reading and cannot be "corrected" by subtraction

`claims.json:14` says "the r39 policy's 2504 = 2335 + 163 + 0 + 6 **becomes the
corrected baseline** with the 2 phantom attributions dispositioned". That
arithmetic is not performable as written, because 2504 is not a live number:

- The r39 policy's Part 2 was measured at **212 entries**
  (`basename-couples-policy.md:249-258`; `Ca04-verify.md:20-24`), the tree state
  at r39. The live tree has **220** (`ls corpus/knowledge/*/*.md | wc -l`).
- The 8 entries landed since r39 contribute exactly **103** deduped couples refs
  (measured per entry: worked-example 20, index-sweep 12,
  contact-strata-verification-gate 12, append-only-record 16,
  taboo-strata-lifecycle 10, dialect-register-consistency 10,
  translation-protocol-fidelity 11, sacred-registers-liturgical-language 12).
- **2607 − 2504 = 103, exactly.** The delta is fully explained; no other change
  to the population occurred.

So the corrected census must be stated as a **fresh measurement on the live
tree**, not as `2504 − phantoms`. On extractor C the live figure is
**2611 = 2437 direct + 166 fallback + 0 ambiguous + 8 unresolved (7 distinct)**.
O03 must predict *this* shape and O12 must say so in the successor note; a
"2504 → 2603" style claim would be arithmetically wrong. The r39 policy document
itself stays filed (non_goals: "no filed byte rewrites") — the correction is a
successor note.

### C4 — C06's after-vector in `targets.json` is arithmetically wrong

`targets.json:163` instructs C06 to draft the README rev 2.4 vector as
**`25/23/27/25/24/94`**. That vector **sums to 218**, not 224. Its 4th element is
also the wrong partition: the four new entries are **myth-symbol**, so the
element that moves is myth-symbol (index 2), not culture-material (index 3).

- Current footer vector (`corpus/README.md:536`): `25/23/25/29/24/94` (sum 220).
- Correct rev 2.4 vector: **`25/27/25/29/24/94`** (sum 224).
- Order rule (r40 C06 precedent, `reports/round-40/cov/C06-delta-receipt.md:93-95`):
  the vector is written in the README's own section order, linguistics-first —
  which is exactly the string above.

C06 must use `25/27/25/29/24/94`; C07 must catch the `targets.json` figure rather
than reproduce it. This is a defect in the round's own binding instructions, so
it is routed, not silently corrected by this seat.

### C5 — O08's queue route conflicts with r41's own ruling, and with r41's actual behaviour

O08's mission is "Queue-v2 N6 row re-class draft (fixed-with-evidence on
landing)". The N6 row is at `defect-queue-v2.json:362-369`, inside
`reports/round-40/**` — filed bytes. The route is genuinely ambiguous:

- r41's X00 said "Hard integration conflict: preserve the r40 queue byte-for-byte
  … apply the verified status changes only in a **new round-41 successor
  artifact**" and O12 repeated "never change the filed round-40 queue".
- But r41's **actual** integration commit **edited that filed file in place**:
  `git show ac47c78 -- reports/round-40/op/defect-queue-v2.json` →
  `M reports/round-40/op/defect-queue-v2.json`, flipping
  `r39-runner-root-regression` and `N7-receipt-fidelity` to `fixed-with-evidence`
  and appending an `r41_update` block. **No round-41 successor JSON exists**
  (`find reports/round-41 reports/round-42 -name '*queue*'` → only the two
  `.md` drafts).

**Integrator ruling required before O08 lands.** Either (a) follow the stated
rule — a new `reports/round-42/…` successor JSON carrying the N6 delta with the
row's `id`/`origin` retained, or (b) follow the r41 precedent — an in-place
`r42_update` block on the r40 queue. The two are not equivalent for a reader who
trusts the r40 file as a filed reading. Note `reports/round-41/run-validation.py:113`
reads `reports/round-40/op/defect-queue-v2.json` directly, so whichever route is
chosen, a *successor* file will not be seen by that leg. Do not describe the v2
bytes as updated unless the integrator actually updates them.

### C6 — O's census and C's landing INTERLOCK: the counting order is load-bearing

The corrected census (C3) is a function of the tree it is measured on. If the
integrator applies C01–C04's four entries **before** running O's recount, the
census shifts by ~40 refs and O03's prediction no longer matches O04's
verification. Two admissible orders — the integrator must pick and record one:

1. **Measure O first** at 220 entries (baseline 2611 on extractor C), then apply
   C. O03/O04/O12 all cite the 220-entry tree; C's own effect is stated
   separately as +4 entries.
2. **Apply C first**, then measure at 224 entries, and have O03 state the
   224-entry prediction explicitly (approximately 2611 + the 4 new entries'
   refs).

Option 1 is cleaner because it keeps O's numbers comparable to the r39 baseline
and avoids an interleaved dependency. Either way, O03 and O04 must agree on the
**entry count** they measured, not only on the token counts. A01's bleed scan of
the four new entries should also state which extractor it used — if it scans with
the single-line extractor it will report every new entry as couples-empty.

### C7 — The phantom dispositions are not all "phantoms" (the disposition vocabulary matters)

`claims.json:16` requires "zero phantom attributions remaining or each
dispositioned". The 8 unresolved distinct tokens split into three different
classes, and lumping them would misreport:

- **Intentional forward references (documented, non-blocker).** `sound-change.md`
  and `tone-prosody.md` are named in the field itself under the literal phrase
  "**prospective sibling files:**" (`phonetics-phonology.md:76-77`). They are
  not errors; they are a declared gap. Under the C12-row-2 rule
  (`reports/round-35/cov/C12-audit-runbook.md:37`: a dangling token is a blocker
  *unless* the same line marks it, then documented/non-blocker) these are
  **documented** — and the same field also names them again at `:279-280`
  ("Natural partners:"). Ca04's own framing ("2 phantom attributions") is the
  narrower reading; the successor instrument should report them as
  `prospective`/documented, not as defects.
- **Extractor artifact.** `-gate.md` is the glob fragment from
  `corpus/knowledge/verification/gate-frozen-run-standard.md:15`; policy §5.6
  already forbids counting it as a couples finding or resolving it via fallback.
- **Genuine unresolved.** `../linguistics/phonology-sanity.md` (×2),
  `honorifics-and-register.md`, `naming-and-onomastics.md`,
  `phonology-basics.md` — real dangling tokens carried by
  `linguistics/language-contact.md`, `synthesis/typed-label-routing-workflow.md`,
  `verification/label-channel-routing-verification.md`. Note
  `../linguistics/phonology-sanity.md` looks like a directory error: the file on
  disk is `corpus/knowledge/verification/phonology-sanity-gate.md`.

If the wave reports "8 unresolved" without this three-way split it will
overstate the defect surface; if it reports "2 phantoms" it will understate it.

### C8 — Runner ban vs counting commands (wording rule carried from r40/r41)

`claims.json:17` declares `python3 reports/round-42/run-validation.py` as O's
counting command, and `claims.json:23` declares `sweep.py`. `shared_rules` +
`targets.json` forbid running any round runner in-tree. **Seat-runnable:**
`ls | wc -l`, `python3 -B reports/round-28/readme/sweep.py` (this seat ran it →
**exit 0**, 220 rows / 220 files), and any read-only recount script. The round
runner is integrator-only in an isolated copy. Seat fragments say "pre-verified
against the arithmetic"; "sweep green" belongs to the integrator's post-apply run.

## 3. Integration order (binding)

1. **Scouts.** K01 **must name the extractor host** (C1) — this gates all of O.
   K02 names the 4 gap topics and the 4 filenames; the filenames gate C06's rows
   (C4: the vector is fixed by the partition, but the row bytes are not).
2. **O executors.** O01 drafts the fenced **new-file** diff with extractor **C**
   (block + indent-strip + hyphen-join; terminator = blank line OR next field).
   O02 drafts controls asserting token **identity** (C2) plus the synthetic
   phantom negative and the unwrapped regression. O03 predicts the corrected
   census on a **named entry count** (C3, C6).
3. **C executors.** C01–C04 author the four entries with the established
   contract, fenced, in filename order. C06 drafts the README delta with the
   **corrected** vector `25/27/25/29/24/94` (C4) and totals 224.
4. **Verifiers.** O04 (isolated `git archive` copy: apply, selftest, recount) and
   O05 (second isolation + adversarial planted-phantom fixture) must compare to
   O03 **row-for-row and token-for-token**. O12 checks the r39 policy arithmetic
   as a successor note (C3). C05 audits all 4 drafts; C07 independently verifies
   the audit + delta numbers — **and must not reproduce `targets.json`'s wrong
   vector**. C08 spot-audits 2 of 4 by lot + the README row bytes. A01 scans the
   4 entries' bleed **with the fixed extractor** and states which one it used.
5. **Cross-review.** R01 hunts the fix's false greens — specifically the B/D
   "4 tokens but wrong identity" trap and the D over-read (C2) — and the entry
   fabrication hunt. R02 reviews; X01 trades; X02 honesty. X01 should check
   whether the corrected census and the README totals are stated on the **same**
   entry count (C3/C6 interlock).
6. **Scribes.** S01 dossier + validation-leg spec (must carry the C6 chosen
   order); S02 telemetry draft.
7. **Integrator (parent), strict order:**
   a. Land the extractor host file from O01's fenced diff (C1); run its selftest.
   b. Run O's recount on the **chosen** tree state (C6, option 1 recommended) and
      reconcile against O03/O04.
   c. Fix the 4 filenames; apply C01–C04; apply C06's README rev 2.4 with vector
      `25/27/25/29/24/94`; run `python3 -B reports/round-28/readme/sweep.py` →
      green 224 == 224.
   d. Rule on O08's queue route (C5) and apply only then.
   e. Validation leg in an isolated copy — never in-tree (C8).
   f. Telemetry: `observed-dispatch.json` + `inputs/`; `availability-close-42.json`
      **only after** `validation.json` lands, sha-pinning the declared record it
      closes (`AGENTS.md` close-what-you-open).
   g. SCORECARD rows → `LOG.md` append **last**, then `MANIFEST.json` + fleet
      report. Admission bar (`REGIMEN.md:42-43`): every claim verifies + no axis
      harmed. C's sweep-green is measurable only post-apply (c); O's thresholds
      land with (a)/(b).

## 4. Reconciliation against the landed peer state (written after the peers landed)

Peers landed during this fragment's write. This seat re-read them and re-ran its
own measurements; the table records agreement, and the two places where a
finding is now superseded or newly corroborated. Vantage at final cut: 26 files
in `reports/round-42/` (`find reports/round-42 -type f`) — adj/A01 (2, incl.
`A01-scan-instrument.py`), calib/Ca01, cov/C02,C07,C08, cross/X00,X01,
op/O02,O03,O04,O06,O07,O08,O09,O10,O11,O12, plan/P01, review/R02,
scout/K01, scribe/S01,S02, plus claims/targets/telemetry. Still absent:
`scout/K02-myth-gaps.md`, `cov/C01,C03,C04,C05,C06`, `review/R01`,
`cross/X02`, `op/O01,O05`, `adj/` beyond A01, `cov/C01`. This is a partial-time
snapshot, not a seat-completion census.

| this seat's finding | landed peer evidence | status |
|---|---|---|
| **C1** host unassigned | K01 `scout/K01-n6-scout.md:103-110,326` names `tools/gates/provenance-audit.py:244-261` `field_block()` as the correct precedent and states the fix "can only be a *fenced draft of a new file*, never an edit to a r19/r39 path" | **RESOLVED** — C1 rewritten above; this seat independently re-verified `field_block()` by importing the module |
| **C2** identity ≠ arity; B and D give "4 tokens" but the wrong set | O02 `op/O02-controls.md:24,33,168-169,209-211` asserts `prosody.md` **absent** and `tone-prosody.md` **present**, and labels the naive join a rejection case; O04 `:129-133` measures both joins separately; K01 §4 names the join rule a required decision | **CONFIRMED, already handled** — no new action |
| **C3** 2504 is an r39-era (212-entry) reading; live is 220 entries, +103 refs | O03 `op/O03-predicted.md:149-156` (`+103 refs, +100 direct, +3 fallback`), O04 `:129-133`, P01 `plan/P01-plan.md:44-45`, S01 `scribe/S01-integration-draft.md:114,150`, X01 `cross/X01-trades.md:31` | **CONFIRMED** — four peers derive the same numbers; this seat's independent probe matches to the token |
| **C4** `targets.json:163`'s vector `25/23/27/25/24/94` sums to 218 and moves the wrong slot | C07 `cov/C07-verify.md:36,164-177` raises it as **FINDING D1** with the same sum check; P01 `:447-450` and S01 `:273-276` state `25/27/25/29/24/94` | **CONFIRMED** — four independent derivations |
| **C5** O08's queue route conflicts with r41's ruling | O08 `op/O08-queue-update.md:192-216` reaches the same conclusion, including that "r41 edited the filed r40 queue in place" | **CONFIRMED** — residual: O08's §4 still asks for a successor; see Owed |
| **C6** O's census and C's landing interlock | P01 `:44-45` and S01 `:150` measure on **220** (pre-C), which is this seat's recommended option 1; no peer names the interlock explicitly | **PARTIALLY COVERED** — the recommendation stands; integrator must still record the order |
| **C7** three-way disposition vocabulary | O03 `op/O03-predicted.md:160-172` ledgers all 8 with named dispositions, and K01 §6 names the prospective-sibling reading | **CONFIRMED** |
| — | **new to this seat: K01 D1e / O12-F1** — the filed r39 policy document is a **truncated prefix** (107 lines / 5832 bytes; §6 recipe and §7 adoption evidence absent) | this seat verified it independently: `wc -l -c` → `107 5832`; `grep -n '^## '` stops at `## 6` with the file ending mid-§6. **Corroborated.** Note this changes C3's citation surface: the `2504 = 2335 + 163 + 0 + 6` arithmetic the claim quotes is **not in the durable filed object at all** (O12 `op/O12-policy-check.md:12,34-45`), so O12's successor note is the only place it can be corrected |

**Net effect on the integration order:** §3 stands unchanged except step 2's
"K01 must name the extractor host" — that is now satisfied, so O01 is unblocked
on the host and blocked only on its own diff. Step 7(a) is now concrete: land
`tools/harness/<name>.py` authored to `field_block()`'s stop semantics.

## Owed

- **Integrator: name the file** in `tools/harness/` and land O01's fenced diff
  there (C1). The *shape* is resolved; the *filename* is not yet fixed by any
  seat, and O01 must not emit a diff against a filed r19/r27/r28 path.
- **O01/O02: use the `field_block()` stop semantics, and assert token identity
  not arity.** B and D satisfy "4/4" while reporting the wrong token set (C2);
  O02 already does this — O01's diff must match O02's control.
- **O03/O12: state the corrected census as a fresh live measurement**, on a named
  entry count (220 or 224), not as `2504 − phantoms` (C3) — and note that the
  quoted `2504 = …` arithmetic is absent from the truncated filed policy (§4).
- **C06/C07: the after-vector is `25/27/25/29/24/94`**, not the
  `25/23/27/25/24/94` printed in `targets.json:163` (C4).
- **Integrator: rule on O08's queue route** (C5) — new successor file vs the
  r41-style in-place `r42_update`; r41's stated rule and r41's actual commit
  disagree.
- **Integrator: pick and record the O/C counting order** (C6) before running
  either.
- **O08: the three-way disposition vocabulary** (prospective / extractor artifact
  / genuine) for the 8 unresolved tokens (C7).
- This seat executed no round runner, applied no code or corpus byte, and wrote
  only this file.

## Citations

- Binding scope: `reports/round-42/claims.json:7,9-11,13-24,26-27`;
  `reports/round-42/targets.json:4-9,11-243` (32 distinct `out` paths);
  `AGENTS.md:3-9,32-39`; `REGIMEN.md:42-43`.
- C1: `reports/round-42/claims.json:16`; `reports/round-19/audit/entry-audit.py:31,34-42,74-96`;
  `reports/round-35/cov/C12-audit-runbook.md:1-12` (`grep` for
  `couples_refs|def couples|resolver` → no match);
  `tools/gates/provenance-audit.py:75-76,77,102-103,244-261,318-324`
  (`field_block()` + `INDENT_RE` — the correct stop semantics; this seat
  re-verified by importing the module);
  `reports/round-40/op/defect-queue-v2.json:323-331,362-369`;
  K01 resolution: `reports/round-42/scout/K01-n6-scout.md:103-110,230-240,326`.
- C2: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (field bytes;
  wrap splits `tone-`/`prosody.md`), `:279-280`;
  `reports/round-39/calib/Ca04-verify.md:80-86,107-115`;
  `reports/round-35/cov/C14-audit-6-10.md:209-222` (`frontmatter_block`),
  `:261-288` (`couples_refs`);
  `reports/round-40/op/defect-queue-v2.json:326-328` ("block extraction through
  the next header field"). Measured (this seat, 2026-10-19, read-only): extractors
  A/B/C/D → 2607/2611/2611/2615 refs; wrapped-field token sets
  `[]` / `{prosody,sound-change,sound-symbolism,writing-systems}` /
  `{sound-change,tone-prosody,sound-symbolism,writing-systems}` / same as B.
- C3: `reports/round-39/calib/basename-couples-policy.md:249-258` (212 entries,
  2504); `reports/round-39/calib/Ca04-verify.md:20-24`;
  `reports/round-42/claims.json:14`. Measured: `ls corpus/knowledge/*/*.md | wc -l`
  → 220; the 8 post-r39 entries' couples refs sum to 103; 2607 − 2504 = 103.
- C4: `reports/round-42/targets.json:163`; `corpus/README.md:536` (live vector
  `25/23/25/29/24/94`); `reports/round-40/cov/C06-delta-receipt.md:93-95` (order
  rule); `reports/round-42/claims.json:20,22`.
- C5: `reports/round-41/cross/X00-connector.md:13,28`;
  `reports/round-41/op/O12-final.md:14,21`;
  `git show ac47c78 -- reports/round-40/op/defect-queue-v2.json` (in-place
  `fixed-with-evidence` flips + appended `r41_update`);
  `find reports/round-41 reports/round-42 -name '*queue*'` → 2 `.md`, no JSON;
  `reports/round-41/run-validation.py:113`.
- C6: `reports/round-42/claims.json:14,18,20-23`; measured entry count 220 and
  the 103-ref post-r39 delta (above).
- C7: `corpus/knowledge/linguistics/phonetics-phonology.md:76-77,279-280`;
  `reports/round-35/cov/C12-audit-runbook.md:37`;
  `reports/round-39/calib/basename-couples-policy.md:97-100` (§5.6);
  `corpus/knowledge/verification/gate-frozen-run-standard.md:15`;
  carriers of the 5 non-prospective unresolved tokens (`grep -rln`):
  `linguistics/language-contact.md`, `synthesis/typed-label-routing-workflow.md`,
  `verification/label-channel-routing-verification.md`.
- C8: `reports/round-42/claims.json:17,23`; `reports/round-42/targets.json:4-9`.
  Measured: `python3 -B reports/round-28/readme/sweep.py` → exit 0, 220 rows /
  220 files, `footer_ok True`, `readme_sha256 d2eed26b…`.
- Snapshot: `git rev-parse HEAD` → `ac47c786…`; `git status --porcelain` →
  `?? reports/round-42/`; `find reports/round-42 -type f` → 3 files at first cut,
  **26 files** at final cut (§4). All commands 2026-10-19, lane root,
  `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  read-only.
- §4 reconciliation: `reports/round-42/scout/K01-n6-scout.md:103-110,230-248,326`;
  `reports/round-42/op/O02-controls.md:24,33,168-169,209-211`;
  `reports/round-42/op/O03-predicted.md:149-156,160-172`;
  `reports/round-42/op/O04-verify.md:129-133,144,199-201,377`;
  `reports/round-42/op/O08-queue-update.md:168-171,192-216`;
  `reports/round-42/op/O12-policy-check.md:12,34-45,203-212,246-255`;
  `reports/round-42/cov/C07-verify.md:36,164-177`;
  `reports/round-42/plan/P01-plan.md:44-45,447-450`;
  `reports/round-42/scribe/S01-integration-draft.md:114,150,273-276`;
  `reports/round-42/cross/X01-trades.md:31`.
  Truncation re-verified this seat: `wc -l -c
  reports/round-39/calib/basename-couples-policy.md` → `107 5832`;
  `grep -n '^## '` stops at `## 6` (line 104); file ends mid-§6.
