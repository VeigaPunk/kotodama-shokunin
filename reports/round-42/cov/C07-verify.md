- Seat: C07 | verifier | claim C | date 2026-10-19 | baseline ac47c78

# C07 — independent verification of the claim-C audit leg and the README delta numbers

Round 42 (regimen 2, loop 1, position 10), seat **C07**, role **verifier**, claim **C**. Mission
(verbatim, `reports/round-42/targets.json` → `seats[id=C07].mission`): *"Independent verification of
the audit + delta numbers."* Out path: `cov/C07-verify.md`. Claim C read at
`reports/round-42/claims.json` (before `myth-symbol 23` / total 220; after `myth-symbol 27`,
total 224; counting commands `ls corpus/knowledge/myth-symbol/*.md | wc -l` and
`python3 -B reports/round-28/readme/sweep.py`; thresholds "sweep green; audits clean").

**Dependency status at this seat's close: the claim-C block is PARTIALLY landed.** C05's audit
(`cov/C05-audit.md`), C01's, C03's and C04's drafts, and C06's delta receipt (`cov/C06-delta-receipt.md`)
were **absent**; only `cov/C02-entry-2.md` (C02's entry 2) and `cov/C08-verify.md` (the third verifier)
had landed (§7 poll log). Per the missing-dependency rule this file does what the mission allows
without them: the **delta leg is verified end-to-end from primary bytes with this seat's own
instruments**, the **one landed draft (C02) is audited independently**, and the draft-dependent legs
are stated as owed (§Owed). No absent fragment is quoted, confirmed, or corrected anywhere below.

- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` →
  `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` (== declared baseline `ac47c78`,
  `reports/round-42/claims.json:7`); `git status --porcelain` → `?? reports/round-42/` only — no
  corpus byte staged at any stamp.
- **Writes**: this file only, plus gitignored `.scratch/c07r42/`. No `corpus/**` byte, no `tools/**`
  byte, no `README` byte, no filed round-1..41 byte. No commit, push, install, or network.
- **Runner ban honored**: no `reports/round-*/run-validation.py` was executed anywhere, in-tree or in
  a copy (`shared_rules[3]`). Filed code executed read-only: `reports/round-28/readme/sweep.py` (live +
  imported with `root_override`), `tools/source-audit-inventory.py`, the r35 C12 runbook instrument
  installed from its own filed awk, and `reports/round-19|27/audit/entry-audit.py` on single entries.
- **Canon: NON-CANON.** This seat audits bytes and files defects; it admits no entry, certifies no
  round, promotes nothing, clears nothing (`PROVINCE.md`; `corpus/QUALITY.md`). A green reading is a
  structural reading of named digests — never a verdict on the scholarship, never canon.

**Verdict at a glance.** The claim-C **before-state verifies exactly** (§1). The **delta arithmetic
verifies** and the landing **simulates green** on the landed draft (§3–§4). But the round's **declared
after-vector is arithmetically impossible** — `25/23/27/25/24/94` sums to **218**, not the declared
`224`, and names the wrong partition slot — and I **proved with the filed sweep** that applying it
literally makes the sweep read **red**, so claim C's own `sweep-green` threshold is unreachable if the
declared bytes are applied (§5, **D1**). The one landed draft (C02) is **contract-PASS** with three
**S3** citation-count defects (§6, **D2**). No S1.

## 0. Instruments and audited bytes (all this seat's own)

| instrument | path | note |
|---|---|---|
| delta generator + landing simulator | `.scratch/c07r42/delta.py` | this seat's own implementation of the row rule (the filed sweep's own `TOPIC_RE` continuation-join, transcribed from `sweep.py:61,71-79`); simulates the landing in a temp tree and measures it **with the unmodified filed r28 sweep** (`sweep(readme, root_override=...)`), plus two negative controls and a filename-order check the sweep lacks |
| fence-run extractor | `.scratch/c07r42/fence.py` | 3/4+ backtick runs, multi-block fragments, flags unterminated fences |
| couples recount | inline heredoc (§2) | independent re-implementation of the r39 policy's §1–§2 token rule and four classes (`basename-couples-policy.md:14-48`), not imported from any filed resolver |

**Instrument calibration (the green is informative, not green-by-construction).** The simulator was
first validated on a synthetic 4-probe stage (first-in-section, an adjacent pair sharing one anchor,
last-in-section, one multi-line `- topic:`): it emitted 4 rows, and the **filed sweep read the
resulting tree green at 224 rows / 224 files**, exit 0. Both negative controls fired: the generated
README over the **live** tree → `ok False`, exactly 4 ghosts; the live README over the **sim** tree →
`ok False`, exactly 4 missing.

**Scratch-hygiene defect found and worked around (recorded, no owner).** This seat's first stage path
`.scratch/c07/stage/` collided with **round 40's** C07 seat, whose four staged linguistics entries
(mtimes 12:03–12:08, i.e. **before** round 42 opened at 12:55) were still on disk. Reusing that path
silently injected four r40 drafts into the simulation tree and produced a **spurious**
`topic_mismatch ['linguistics/sacred-registers-liturgical-language.md']` — the r40 draft's `:885`
bytes read `gatekeeping devices` where the landed file reads `closure devices`. Re-running from a
fresh `.scratch/c07r42/stage/` (this seat's file only) returned `topic_mismatch 0`. **The mismatch was
this seat's path collision, not a corpus defect**; the live tree reads clean (§1). Recorded because a
"mismatch" that is the harness's stale state is not a finding, and because scratch dirs are shared
across rounds.

## 1. The before-state — re-measured, matching claim C exactly

| object | value | command |
|---|---|---|
| baseline commit | `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` | `git rev-parse HEAD` |
| partition census | `25/23/25/29/24/94` | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` |
| myth-symbol (claim C's premise) | **23** | `ls corpus/knowledge/myth-symbol/*.md \| wc -l` |
| knowledge total | **220** | `find corpus/knowledge -name '*.md' -type f \| wc -l` |
| `corpus/README.md` | sha256 `d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f`, 563 lines / 137 411 bytes | `sha256sum`; `wc -lc` |
| sweep instrument | sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` | `sha256sum reports/round-28/readme/sweep.py` |

`python3 -B reports/round-28/readme/sweep.py` at `ac47c78` → **exit 0**, `rows 220 files 220`,
`missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`,
`totals_line 220 totals_ok True`, `footer total 220 / [25, 23, 25, 29, 24, 94]`, `footer_ok True`,
`readme_sha256 d2eed26b…`. `--selftest` → `12/12 checks passed`, exit 0.
`tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 220`.
The sweep instrument digest equals the pin filed at `reports/round-39/cov/C06-delta-receipt.md:31` and
`reports/round-40/cov/C06-delta-receipt.md` §1, and the README digest equals the live sweep's own
`readme_sha256` — the before-state is a digest-pinned reading, not an inherited claim.

## 2. The r39 census arithmetic — independently recounted (claim O's surface, cross-checked here)

Not this seat's claim, but claim C's own after-state sits on the same corpus and the round's two claims
share the tree, so the reference census was re-derived independently rather than trusted. My own
implementation of the r39 policy's token rule (`[A-Za-z0-9_./{},\-]+\.md`, one-level brace expansion,
dedup per entry) and four classes (Tier-1 three bases; Tier-2 slash-free unique-basename fallback)
over the live 220 entries:

| extractor | tokens | direct | fallback | ambiguous | unresolved |
|---|---|---|---|---|---|
| single-line (r19 `entry-audit.py:75` semantics) | **2607** | 2435 | 166 | 0 | **6** |
| block parser (continuation-joined, rule D) | **2611** | 2437 | 166 | 0 | 8 |

The single-line **unresolved set reproduces r39's filed 6 exactly**, by class:
`-gate.md` ×1, `../linguistics/phonology-sanity.md` ×2, `honorifics-and-register.md` ×1,
`naming-and-onomastics.md` ×1, `phonology-basics.md` ×1 — the same five distinct strings the r39
policy filed (`basename-couples-policy.md:355-357`). Two independent instruments, one reading.
These totals also **agree with `op/O10-gap-fill.md` §1's** independently-measured `A=2607 / C=2611 /
D=2611` (a third instrument); that agreement is a consistency result, never correctness
(`verification/two-reader-interop-agreement.md`), and this seat authored none of the audited bytes.

## 3. The delta numbers — verified end-to-end on the landed draft

### 3.1 The declared target (read, not assumed)

`reports/round-42/claims.json` claim C: `myth-symbol 23 → 27`, total `220 → 224`, README rev 2.4.
`reports/round-42/targets.json` seat C06 (verbatim): *"README rev 2.4 delta draft (myth-symbol 27,
totals 224, vector 25/23/27/25/24/94, 4 rows in filename order) + receipt draft."*

### 3.2 The landing simulation (filed instrument, temp tree, no live writes)

With **C02's landed fence** staged under its declared name and my generated README (row inserted in
filename order + header `## myth-symbol/ (24)` + totals + footer), the **unmodified filed r28 sweep**
reads:

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 24,
       "synthesis": 29, "verification": 24}
rows 221 files 221   missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []
header_drift {}      totals_line 221 totals_ok True
footer total 221 / [25, 24, 25, 29, 24, 94]   footer_ok True
ok True   exit 0
```

So **C02's landed bytes are structurally landable and read clean** — the one entry that exists is
delta-compatible. (The 224 target is reachable only when all four drafts exist; §4 gives the
full-target arithmetic.)

### 3.3 The row bytes — regenerated from C02's landed fence

Extracting C02's fence and applying the sweep's own topic rule (continuation-joined):

| field | value |
|---|---|
| fragment | `reports/round-42/cov/C02-entry-2.md` |
| fence shape | one 3-backtick `markdown` block (the r35 stager-regex shape) |
| entry bytes | 49 972 |
| entry sha256[:16] | `4c8c07f5a05a6bff` (full `4c8c07f5a05a6bffdd87730661c1941326733367540e1ccc50f590f6d29cea10`) |
| generated row sha256 | `5102fb21aa45c5584d2b03d84ef7d158689f127df5f181162e422aff1c1ac987` |
| generated row chars | 2 091 (topic 2 057) |
| declared landing name | `myth-symbol/purity-pollution-systems.md` |

**Sort position (a leg the sweep cannot see).** The 23 existing myth-symbol rows are filename-sorted
(measured: `rows == sorted(rows)` → True), and `purity-pollution-systems.md` sorts between
`plant-symbolism.md` and `ritual-liminality.md` (index 19 of 24 after insertion). The generated row
was inserted there and the section stayed sorted → True.

### 3.4 Collision and uniqueness at the target size (X01's T3 leg, re-measured)

`find corpus/knowledge -name 'purity-pollution-systems.md'` → **0**; the basename appears in **0**
couples tokens corpus-wide. The duplicate-basename index over `corpus/knowledge/*/*.md` is **empty at
220 and stays empty at 224** with C02's name added — so the r39 policy's §2(c) uniqueness assumption
is not disturbed by this landing (it must be re-run once all four names are known, §Owed).

## 4. Full-target arithmetic — the 220 → 224 leg

220 + 4 = 224 and myth-symbol 23 + 4 = 27. The **section-order** vector is
`linguistics / myth-symbol / culture-material / synthesis / verification / civilizations`
(`sweep.py:50-57` `PARTS`, confirmed live by the sweep's `footer_live.order`), so the correct after-vector
is **`25/27/25/29/24/94`** — sum **224**. With a synthetic 224-file tree (C02's entry + 3 probes to
reach the count) the **filed sweep** reads `footer_findings []`, `footer_ok True`, `ok True`, exit 0
when the footer carries `(total 224 files; directory totals 25/27/25/29/24/94)`.

## 5. FINDING D1 — the declared after-vector is arithmetically impossible and, applied literally, fails the sweep

**Statement.** `reports/round-42/targets.json` → `seats[id=C06].mission` declares the rev-2.4 vector as
`25/23/27/25/24/94`. That literal is inconsistent with its own declared total and moves the wrong slot.

**Evidence 1 — arithmetic (measured, not argued).** Under the README's fixed section order, slot 2 is
`myth-symbol` and slot 3 is `culture-material`. The literal `25/23/27/25/24/94` therefore leaves
myth-symbol at **23** (contradicting the same sentence's "myth-symbol 27") and moves **culture-material**
25 → 27. It sums to `25+23+27+25+24+94 = **218**`, while the same mission declares `totals 224` and
220 + 4 = 224. The section-order-correct vector is `25/27/25/29/24/94`, sum **224**.

**Evidence 2 — proven with the filed instrument (this seat's run, 2026-10-19).** On a copy of
`corpus/knowledge` staged to **224 files**, the **unmodified filed sweep** imported with
`root_override`:

| footer bytes applied | `footer_findings` | `footer_ok` | `totals_ok` | `ok` |
|---|---|---|---|---|
| `total 224` + vector `25/23/27/25/24/94` (**declared literal**) | `[{"class":"FOOTER_DIR_TOTALS","declared":[25,23,27,25,24,94],"live":[25,27,25,29,24,94],"order":[linguistics,myth-symbol,culture-material,synthesis,verification,civilizations]}]` | **False** | True | **False** |
| `total 224` + vector `25/27/25/29/24/94` (section order) | `[]` | **True** | True | **True** |

Row 1 is a real rejection by the filed instrument and not an instrument that never fires: the sweep's
footer leg compares the declared six-directory vector against the live tree in section order
(`sweep.py:163-189`). **Applying the declared bytes to `corpus/README.md` therefore makes claim C's own
`sweep-green` threshold unreachable** — the integrator would land a red tree and no after-count could
be quoted as measured.

**Precedent that this is a new slip, not house convention.** r39's C06 mission declared
`21/23/25/29/24/94` (sum 216 == its declared totals 216) and r40's declared
`21/23/25/29/24/94 → 25/23/25/29/24/94` (sum 220 == its totals 220) — both self-consistent and in
section order. r42 is the first mission vector whose slots do not sum to its own declared total.
(`reports/round-40/targets.json:86`; the lane's prior form for mission text carrying figures the
executor must correct is recorded at `reports/round-40/cov/C06-delta-receipt.md:20-22`.)

**Convergence — three independent seats, one reading.** This seat measured D1 before reading any peer
fragment; `reports/round-42/cov/C08-verify.md` §5 (D1) and `reports/round-42/review/R02-review.md` §12
(Trap D) and `reports/round-42/cross/X01-trades.md` T7 independently reached the same conclusion from
their own instruments. Four fragments, four readers, one finding — the agreement is corroboration, not
a shared source.

**Disposition requested of the integrator.** Treat the rev-2.4 vector as **`25/27/25/29/24/94`** (slot 2,
myth-symbol) and `totals 224` as correct; do **not** apply `25/23/27/25/24/94` to
`corpus/README.md`'s counts footer. The other rev-2.4 legs the mission names are verified and
unaffected: header `## myth-symbol/ (23)` → `(27)`, totals line `220` → `224`, and 4 rows inserted in
filename order. **Severity S2** — it is not a defect of any landed byte (the pinned README is clean,
§1) and not a defect of C06's authoring (which had not landed at this seat's close); it is a defect in
the round's own declared target, and it blocks claim C's threshold if applied literally. The
post-apply sweep reading remains the integrator's to measure.

## 6. Independent audit of the one landed draft — C02 `purity-pollution-systems.md`

The r35 C12 runbook instrument (installed from its own filed awk; sha256
`973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`, 663 lines — **equals the pin filed
in that runbook's §4 step 0**; `--selftest` → `SELFTEST PASS`) run on the staged C02 bytes:
**`PASS/review`** — `4of4=True`, `5f=True`, `gap=True`, `dec=True`, `pointers_unresolved []`,
`digest_pins_stale_candidates []`. The two review-tier items are adjudicated **false positives**:
`bleed-candidate:closure,promoted` (the `closur` substring inside the entry's own "disclosure" subject
term, and "an axis is promoted" as the intensification row) and `canon-mention-unnegated:canon,canonical`
(the boundary sentences plus the subject term of art). Review tier never fails the contract
(`C12-audit-runbook.md` §8 limit 4). The entry's head block carries the lane 5-field set and 6 fields;
`verified-at` is ISO; the gap is named; the decision record is present (`DR-PP-01…15`).

**Fabrication spot-checks — every needle verifies.** All 11 spot-checked `path:line` anchors read what
the entry claims: `symbolism-synthesis-method.md:40` (the Douglas anomaly row), `:48` (the
`pure/impure` polarity axis), `:68` ("the anomaly picks your taboo"), `animal-symbolism.md:46` (the
food-law "purity politics" column), `:69` (the pig taboo, "one law, two rival explanations"),
`plant-symbolism.md:20` ("Two registers, one machinery"), `death-afterlife-eschatology.md:49` (the
corpse's status as "a separate variable"), `ritual-liminality.md:57` (the piacular row),
`direction-symbolism.md:25` (valence axis incl. `pure/impure`), `divination-omen-systems.md:100`
(procedural escape), `bathing-and-body-hygiene.md:50` ("They are different systems and must not be
merged"). The four pinned file digests **all match live bytes byte-for-byte**:
`animal-symbolism.md 8f1fce2d21a1a174…`, `symbolism-synthesis-method.md 8aef07cae6d6c484…`,
`bathing-and-body-hygiene.md 15f2ea5de5bb9406…`, `politeness-taboo-euphemism.md a73c0b1fb8fd0052…`.
The absence census reproduces: `pollution`, `impurity`, `defilement`, `contagion`, `purification`,
`lustration`, `abomination` → **0 topic-owners each**; `boundary maintenance` → **0 files**;
topic-owners `taboo` → **8**, `purity` → **2** (both exact).

**FINDING D2 (S3) — three citation-block counts are inflated; one class, not three bugs.**

| the entry says | measured | class |
|---|---|---|
| `taboo` appears in **122** files | **121** (`grep -rl taboo`); 122 only with `-i` | case-insensitive count reported as case-sensitive |
| `purity` → **41** files | **39** (`grep -rl purity`); 41 only with `-i` | same |
| `Douglas` → **31** files | **13** files (`grep -rl Douglas`); **32** occurrences | occurrence count reported as a file count |

The `Douglas` row is the clearest: 31 is not a file count under any case variant (13 case-sensitive and
case-insensitive alike) — it is the near-neighbour of the **32** occurrence count, so an
occurrence total was mislabelled as a file total. The other two are the `-i` variant. **Substantive leg
holds**: the zero-counts (the actual gap evidence) all reproduce exactly, and no needle is false. Fix:
state the exact command, or the correct counts (121 / 39 / 13). Owner: C02 / integrator — apply-as-is
with named defects is within claim C's threshold.

**Staging note for the integrator.** C02's fence is a single 3-backtick `markdown` block with **no**
internal fence line (measured: `fenced_blocks_found 1`, `internal_fence_lines 0`), so the r35 stager
regex stages it whole — no multi-block hazard. The entry's declared landing name is
`myth-symbol/purity-pollution-systems.md`; C02's own `## Owed` records that K02 (the myth-symbol gap
scout) was **absent at its seat time**, so the slug is C02's self-selected claim and the topic
de-collision against C01/C03/C04 is owed to X00/integrator. The name collides with nothing today
(§3.4).

## 7. Poll log (why the other legs are owed rather than done)

`find reports/round-42 -type f | sort` across this seat's window. At first poll the tree held
`claims.json`, `targets.json`, `telemetry/dispatch-declared.json` only; by close it held (landing
order observed): `scout/K01-n6-scout.md`, `op/O09-scribe.md`, `op/O10-gap-fill.md`,
`adj/A01-scan-instrument.py`, `calib/Ca01-gap-fill.md`, `cov/C02-entry-2.md`, `cov/C08-verify.md`,
`op/O03-predicted.md`, `op/O04-verify.md`, `op/O06-receipt.md`, `op/O07-gap-fill.md`,
`op/O08-queue-update.md`, `op/O02-controls.md`, `plan/P01-plan.md`, `cross/X01-trades.md`,
`review/R02-review.md`, `scribe/S01-integration-draft.md`, `scribe/S02-telemetry-draft.md`,
`adj/A01-entries-bleed.md`. **Absent at close**: `cov/C05-audit.md`, `cov/C01-entry-1.md`,
`cov/C03-entry-3.md`, `cov/C04-entry-4.md`, `cov/C06-delta-receipt.md`, and
`reports/round-42/run-validation.py`. So the **audit leg of claim C's threshold ("audits 4/4 PASS")
cannot be verified** — one of four drafts exists, and the auditing seat's own verdict (C05) is absent;
and **no landed row bytes for C01/C03/C04 can be quoted**. This seat is in the same position r40's C07
was in (`reports/round-40/cov/C07-verify.md:9-11`): it re-measures the whole verifiable surface itself
and leaves the draft-dependent legs owed.

## 8. Limits

- **Structural + source-resolution verification, not scholarship and not canon.** Nothing here judges
  whether the topics are the right four, whether the historical claims are true, or whether the entries
  should be promoted (`PROVINCE.md`; `corpus/QUALITY.md`). Literature legs are `(to-verify)` by the
  entries' own declaration; no fetch occurred (no network).
- **Simulation, not landing.** §3.2's green and §5's red are digest-pinned readings of candidate trees
  built from draft fences and synthetic probes; the landing's own evidence is the integrator's
  post-apply sweep, and any post-audit byte change to a fragment voids the corresponding reading here.
- **One draft of four.** §6 audits C02 only; its verdict says nothing about C01/C03/C04, whose bytes
  this seat never saw. C02's fragment digest is §3.3's; a later in-place edit is detectable against it.
- **One resolver, known blind spots.** The §2 recount is a re-implementation, not a filed tool; it
  reproduces r39's unresolved set exactly, which is corroboration, not proof of the same unit.
- **The scratch-collision defect (§0)** was this seat's own harness state, not a corpus finding; it is
  recorded so a successor does not re-inherit it, and so no future reader treats the spurious
  `topic_mismatch` as evidence.

## Owed

- **`reports/round-42/cov/C05-audit.md`** — the audit leg of claim C's threshold ("audits 4/4 PASS",
  `reports/round-42/claims.json`); absent at this seat's close (§7). Apply gate: entries land only after
  the audit is clean or its defects are filed.
- **`reports/round-42/cov/C01-entry-1.md`, `C03-entry-3.md`, `C04-entry-4.md`** — three of four drafts
  absent (§7), so the 4/4 entry-audit leg and three of the four README row bytes are unverifiable here.
  When they land: stage each fence, run the C12 instrument (digest `97361027…`, 663 lines), regenerate
  each row mechanically from the landed bytes, re-check the section stays filename-sorted, and re-run
  the duplicate-basename index at the final 224 (X01 T3).
- **`reports/round-42/cov/C06-delta-receipt.md`** — absent (§7); no landed rev-2.4 bytes can be quoted.
  Its required content is §4's correct vector `25/27/25/29/24/94` (sum 224), header → `(27)`,
  totals → `224`, 4 rows in filename order.
- **D1 fix** — owner: integrator (S2). Correct the C06 mission vector token to `25/27/25/29/24/94`;
  never apply `25/23/27/25/24/94` to the counts footer. Evidence §5.
- **D2 fix** — owner: C02 / integrator (S3): state `121` / `39` / `13`, or quote the exact command.
- **Post-apply sweep** — `python3 -B reports/round-28/readme/sweep.py` green at `224 == 224` belongs to
  the integrator's apply step; §3.2's 221-file green is a reading of one draft, not of a delivered
  revision (the `readme-prediction-vs-delivery` rule, `reports/round-37/op/defect-queue.json:242-251`).
- **`reports/round-42/run-validation.py`** — absent at this seat's close; per the absolute rule it must
  never be run in-tree by this seat even once it exists.

## Citations

- `reports/round-42/claims.json:7` (baseline `ac47c78`), claims O/C (before `myth-symbol 23` / 220;
  after `myth-symbol 27` / 224; counting commands; thresholds "sweep green; audits clean"), non-goals.
- `reports/round-42/targets.json:4-9` (shared rules), seat C07 object (`mission`, `out`),
  `seats[id=C06].mission` (the declared vector `25/23/27/25/24/94`, totals 224) — D1's source.
- `REGIMEN.md:27-30` (per-round contract), `:41-43` (admit rule), `:57` (close-time runner).
- Instrument and pins: `reports/round-28/readme/sweep.py` (digest `9b2ccac0…`; `PARTS :50-57`;
  `ROW_RE :60`; `TOPIC_RE :61`; `topic_of :74-82`; footer leg `:163-189`; selftest `:394-401`),
  `tools/source-audit-inventory.py`, `reports/round-35/cov/C12-audit-runbook.md` (digest `06dd08eb…`;
  §4 step 0 expected instrument digest `97361027…`; §1 check families; §8 limit 4),
  `reports/round-19/audit/entry-audit.py:31,74-96`, `reports/round-27/audit/entry-audit.py`.
- Row contract and insertion geometry: `corpus/README.md` at sha256 `d2eed26b…` — `:5` (rev 2.3),
  `:168` (linguistics header), `:196` (`## myth-symbol/ (23)`), `:198-220` (23 rows), `:222`
  (culture-material header), `:532` (totals line `220`), `:534-536` (counts footer), `:563` (last line).
- Audited draft: `reports/round-42/cov/C02-entry-2.md` (fence 49 972 B, sha256[:16] `4c8c07f5a05a6bff`;
  declared name `myth-symbol/purity-pollution-systems.md`; generated row sha256
  `5102fb21aa45c558…`, 2 091 chars).
- Policy and census precedent: `reports/round-39/calib/basename-couples-policy.md:14-48` (§1 token rule,
  §2 four classes), `:35-36,268,355-357` (the filed `212 / 2504 = 2335 + 163 + 0 + 6` and the five
  distinct unresolved strings), `reports/round-39/calib/Ca04-verify.md` (D1, D2).
- Peer convergence on D1: `reports/round-42/cov/C08-verify.md` §5 (D1), `reports/round-42/review/R02-review.md`
  §12 (Trap D), `reports/round-42/cross/X01-trades.md` T7. Independent corroboration of the §2 recount:
  `reports/round-42/op/O10-gap-fill.md` §1 (`A=2607 / C=2611 / D=2611`).
- Filed precedent: `reports/round-40/cov/C07-verify.md:9-11` (the missing-dependency protocol this file
  follows), `reports/round-40/targets.json:86` and `reports/round-39/targets.json:72` (the two prior,
  self-consistent mission vectors), `reports/round-40/cov/C06-delta-receipt.md:20-22`,
  `reports/round-37/op/defect-queue.json:242-251` (`readme-prediction-vs-delivery`),
  `reports/round-40/op/defect-queue-v2.json:362-369` (the `N6` row).
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD` / `git status --porcelain`; the partition census loop + `find | wc -l`;
  `sha256sum corpus/README.md reports/round-28/readme/sweep.py`; `wc -lc corpus/README.md`;
  `python3 -B reports/round-28/readme/sweep.py` (live 220/220 exit 0) and `--selftest` (12/12);
  `tools/source-audit-inventory.py --json --summary` (220); the couples recount heredoc (§2, both
  extractors + the unresolved breakdown); fence extraction + digest battery on C02 (§3.3);
  the C12 instrument install + digest check + selftest + staged run + `--json` on C02 (§6);
  the eleven anchor `sed -n` reads and four file digest re-hashes (§6); the absence-census greps
  (both case variants, §6); the landing simulation (§3.2) with both negative controls and the
  filename-order check; the 224-file footer battery (§5); the collision + duplicate-basename checks
  (§3.4); `find reports/round-42 -type f` polls (§7). **Not run, deliberately**: any
  `reports/round-*/run-validation.py`; any network call; no write outside this fragment and
  `.scratch/c07r42/`.
- Scratch (disposable, not evidence): `.scratch/c07r42/{delta.py,fence.py,stage/,}`;
  `.scratch/c12/entry-audit-runbook.py` (installed from the r35 runbook's own awk).
