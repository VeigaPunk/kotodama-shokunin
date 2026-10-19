- Seat: C07 | verifier | claim C | date 2026-10-19 | baseline fd55e1f

# C07 — independent verification of the claim-C audit leg and the README delta numbers

Round 40 (regimen 2, loop 1, position 8), seat **C07**, role **verifier**, claim **C**. Mission
(verbatim, `reports/round-40/targets.json` → `seats[id=C07].mission`): *"Independent verification
of C05's audit + the delta numbers."* P01 §1 step 6 binds the legs: counts, filename ordering, row
byte-shape vs existing linguistics rows (`reports/round-40/plan/P01-plan.md:64-66`).

**C05's audit (`reports/round-40/cov/C05-audit.md`) had not landed at this seat's close**
(poll 15:11:45Z; last cov poll in §4). Per the missing-dependency rule this file therefore does
what the mission allows without it: every reading below was **re-measured from primary bytes by
this seat with its own instruments** — an independent audit of all four entry drafts, plus the
full delta verification. When C05 lands, its verdicts cross-check against §2/§3 here; §4 states
the exact protocol. No C05 claim is quoted, confirmed, or corrected anywhere in this file.

- Lane root; `git rev-parse HEAD` → `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` (== declared
  baseline `fd55e1f`). **Writes**: this file, plus gitignored `.scratch/c07/` (instruments,
  staged entries, simulation tree). No corpus byte, no README byte, no filed-round byte touched.
- **No `reports/round-*/run-validation.py` executed anywhere.** Filed code executed, read-only:
  `reports/round-28/readme/sweep.py` (live + via module import with `root_override`, §1), and
  `tools/source-audit-inventory.py --json --summary` (§1, §1.4). No network.

## 0. Instruments and audited bytes (all this seat's own, not C05's)

| instrument | path | note |
|---|---|---|
| fence-run extractor | `.scratch/c07/fence.py` | 3/4-backtick runs, multi-block fragments; flags unterminated fences |
| reference resolver | `.scratch/c07/refs.py` | backticked paths + `path:line`; multi-base resolution; line-range check |
| delta generator + simulator | `.scratch/c07/delta.py` | my own implementation of the row rule (`TOPIC_RE` continuation-join); simulates the landing in a temp tree and measures it **with the unmodified filed r28 sweep** (`sweep(readme, root_override=...)`), plus two negative controls and the inventory cross-check |

Audited fragments (whole-file sha256[:16], this seat's pins):

| seat | fragment | sha256[:16] | fence shape | entry bytes | entry sha[:16] |
|---|---|---|---|---|---|
| C01 | `cov/C01-entry-1.md` | `ff3e004cdb797506` | one 4-backtick block | 32 798 | `d02221a5f462e41c` |
| C02 | `cov/C02-entry-2.md` | `cec07007ef4175da` | one 4-backtick block | 33 090 | `e0ea254391922add` |
| C03 | `cov/C03-entry-3.md` | `fa7df06a1a5db116` | 4-backtick entry **+ 3-backtick receipt block** | 47 416 | `1962fa5d947224c2` |
| C04 | `cov/C04-entry-4.md` | `c12c1683a22ef1f8` | one 3-backtick block (+ post-fence self-audit prose) | 37 116 | `a05d2fe334ddb13b` |
| C06 | `cov/C06-delta-receipt.md` | `15327d7c553764af` | 17 blocks (draft prose) | — | — |
| K03 | `scout/K03-gaps.md` | `3d86b068ffb4e642` | — | — | — |

Declared landing names (fragment preambles): C01 `taboo-strata-lifecycle.md` (**renamed from
K03 §2's proposed `taboo-euphemism-lifecycle-stages.md` — executor choice, allowed by
K03 §5 `:175-177`; recorded, not a defect**); C02 `dialect-register-consistency.md` (= K03 E2);
C03 `translation-protocol-fidelity.md` (= K03 E3); C04 `sacred-registers-liturgical-language.md`
(= K03 E4). **Staging hazards for the integrator:** stage C03's **block 0 only** (block 1 is an
entry-audit receipt whose JSON cites a sandbox-relative `c03-draft.md` — do not stage the
receipt, and treat its `c03-draft.md` path label as sandbox-relative, r39-F7 class); C01/C02 are
4-backtick fences (the r39 regex-stager hazard applies); C04's self-audit prose lives **outside**
the fence.

## 1. The delta numbers — verified end-to-end, measured, never predicted

### 1.1 Before state (re-measured, matches C06 §2 and my first poll)

`ls corpus/knowledge/linguistics/*.md | wc -l` → **21**; r28 sweep live → `rows 216 files 216`,
all zero-legs, `totals_line 216`, footer ok `21/23/25/29/24/94`, exit 0, `readme_sha256
e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a` (549 lines / 132 721 bytes —
C06's §Citations pin matches byte-for-byte). Existing linguistics rows are filename-sorted
(measured; C06 §5's precondition holds). C06's git pins re-derive exactly:
`git rev-parse HEAD:corpus/knowledge` → `608ef479d23051d6b4211bc40e52ccb7ffeaf4b2`;
live-vs-`ls-tree` path-manifest digest → `a89679bf6830314d…` both sides — the before state is
recoverable from git alone, as C06 §2.3 claims.

### 1.2 Row bytes (my generation vs C06's pins)

Extracting each landed fence, applying the sweep's own topic rule (continuation lines stripped,
single-space joined), and generating the four index rows with **my own** implementation:

| row | my row sha256 (full) | C06 pin | verdict |
|---|---|---|---|
| `dialect-register-consistency.md` | `fb82477b60cc067b22cbfc121acdb5d2a058458045e1d23cbb86a63c2bab13b8` | §6 block sha `fb82477b60cc067b…` | **BYTE-IDENTICAL** |
| `taboo-strata-lifecycle.md` | `039cbcad013f65624a4e9e808903c84a958e2fe95ede3d297bd253d452318612` | §6 block sha `039cbcad013f6562…` | **BYTE-IDENTICAL** |
| `translation-protocol-fidelity.md` | `7760a2065edaf612f8234f39a7e173beed1a36374b199c5d6bbc4619736fcc1c` | §6 block sha `7760a2065edaf612…` | **BYTE-IDENTICAL** |
| `sacred-registers-liturgical-language.md` | `061d0c8ecbc9c54274fe5d7a91fba3cf379dd1b31ec3be22805a66b64862e1ed` | none — C06 pre-dates C04 (§3 F3) | supplied here |

**The fourth row, byte-exact from C04's landed fence at `c12c1683a22ef1f8`** (integrator: use
this only as a cross-check — regenerate mechanically from the landed bytes at apply time, per
C06 §5.4's own rule; chars = 1 107):

```
- `sacred-registers-liturgical-language.md` — The linguistics of a register system whose high variety is reserved for the sacred: the sacred specialization of diglossia (H allocated to ritual events, learned without native acquisition, kept by institutions rather than speakers); the six-competence model of sacred-language skill (hearing recognition, recitation accuracy, liturgical literacy, comprehension, composition, authorization) and how ritual events map to the competences they require; the mechanics of liturgical fossilization, per layer, with the maintenance institutions each freeze needs; event-typed language rules (recitation, sermon, petition, hymn, naming, authorized translation differ in what competence they demand and what counts as a violation); recitation norms and chant as phonological objects; closure devices and their costs; and the register's own decay and revival ladder, orthogonal to the vernacular ladder. Reference knowledge and method only; canon and religion content stay out — whether any world has such a register, and what it is sacred *to*, belongs to lore-shokunin.
```

### 1.3 The landing simulation (filed instrument, temp tree, no live writes)

With the four staged entries copied into a temp knowledge tree and my generated README (rows +
header `## linguistics/ (25)` + totals + footer), the **unmodified filed r28 sweep** reads:
`rows 220 files 220, ok True, missing 0, ghosts 0, topic_mismatch 0, header_drift {},
totals_line 220 totals_ok True, footer 220 / [25, 23, 25, 29, 24, 94], footer_ok True`.
`tools/source-audit-inventory.py --json --summary` over the temp tree → `totals.files 220`.
This is claim C's `after_required` ("linguistics 25, total 220; README rev 2.3 sweep-green
(220 == 220)") **proven on the draft bytes** — the integrator's post-apply re-measurement
remains the landing's own leg (C06 §8.2).

Negative controls (the simulation can fail, so the green is informative):
generated README over the **live** tree → `ok False`, exactly 4 ghosts; live README over the
**sim tree** → `ok False`, exactly 4 missing.

### 1.4 Filename ordering — a leg the sweep cannot see (P01 assigns it to this seat)

`sweep.py` checks missing/ghost/duplicate/topic-equality/header/totals/footer but **never row
order** (`sweep.py:119-212` — no ordering control). Measured independently here: the generated
linguistics section's 25 rows are ASCII-sorted (`rows == sorted(rows)` → True), insertion
anchors `dialect-register-consistency` after `conlang-methodology.md`,
`sacred-registers-liturgical-language` after `register-strata-attestation.md`,
`taboo-strata-lifecycle` and `translation-protocol-fidelity` both after `syntax-typology.md`
(shared anchor; final order taboo < translation). **Finding worth keeping:** my first generator
draft had the shared-anchor disorder exactly (translation above taboo) and the sweep still read
green — proof the contract's "filename order" clause is enforceable only by an order check.
The integrator's acceptance sequence should run one (C06 §5.2's apply-order rule, or the
one-liner: extract rows, `rows == sorted(rows)`).

### 1.5 C06's mechanical claims spot-verified

E2 header line 158, E3 totals line 518, E4 footer line 522, E5 append after line 549 — all
match the pinned README (read at `e73dc971…`); §5.4's 21→25 arithmetic reproduces (my §1.3);
§7's revision-2.3 block carries `⟨n1⟩..⟨n4⟩` placeholders (no fabricated names) and pre-states
the vector 21/23/25/29/24/94 → **25/23/25/29/24/94**; §8.1's before-state negative control
(block 16 of the fragment) reads FAIL on every after-leg — honest, not green-by-construction.

## 2. Per-entry independent audit (all four drafts, this seat's own readings)

Every entry: **9/9 head-block fields** (`topic`, `gap filled`, `sources`, `calibration`,
`couples`, `source`, `verified-at`, `recheck`, `scope`); round-10 five-field set 5/5; ISO
`verified-at: 2026-10-19` at `fd55e1f`; explicit canon boundary + NON-CANON/invented-data
discipline on every demonstration; `to-verify` flags present where claimed.

**C01 `taboo-strata-lifecycle.md` — structural PASS with F1.** Absence sweeps reproduce
exactly: `treadmill` 4, `minced` 3, `ordering test`/`sound-law bracket`/`bracketing` 0,
`read-off` 1 (`civilizations/parthia.md`), `grep -i taboo language-contact.md` 0. Line-count
claims true (neighbours 135/201 lines). ~20 needles read true, including the boundary quotes
(`historical-linguistics.md:7` couples text, `:233` taboo paragraph; `politeness-taboo-euphemism.md`
:75/:76/:82/:88/:95/:99/:101-104/:106/:113/:118/:127/:128; `synthesis/taboo-euphemism-lifecycle.md`
:29/:45/:62 (exact quote)/:65/:121/:139-144/:150/:152/:156/:163/:185). Resolver: 75/75 unique
refs resolve. K03's non-restatement boundary **held**: the four-strata rule and the :118 worked
example are coupled, not restated; the §9 demonstration runs on invented forms/laws. Sources
resolve to in-corpus registrations (Allan & Burridge 2006/1991, Burridge 2012, Pinker, C13,
T&T, Mallory & Adams, Baugh & Cable, Hughes/Mohr, OED/etymonline, Yoma/Rösel/Tov, Wilkinson,
Rosa's Law) — with F1's three off-by-one locators.

**C02 `dialect-register-consistency.md` — structural PASS, clean.** All six quoted sweeps
reproduce with the exact cited lines: `founder effect` 1 file (`migration-founder-effects.md`),
`new.dialect` 0, `second.life` 0, `anti-society` 5 hits at `linguistic-anthropology.md:117,122,146`
+ `register-lexicon-ceilings.md:12` + `dialect-faction-map-workflow.md:202`, `koineization` 5
files (the cited set), `focusing` 1 hit (`dialect-faction-map-workflow.md:94`, whose text is
exactly the no-fixed-deadline caution C02 reconciles). Line-count claims true (209/205/202).
~10 needles read true (`sociolinguistics-registers.md:64,:140,:148`; `register-lexicon-ceilings.md:182,:238-240`;
`conlang-methodology.md:90`; `dialect-faction-map-workflow.md:93-94`; `migration-founder-effects.md:18,:32-34,:52`).
Resolver: 77/77 unique refs resolve. Halliday second-life attribution carried `(to-verify)` as
claimed. Boundary held: :64's compressed paragraph is expanded, "not restated" (its own words),
and the built-map consistency audit is explicitly routed-out to the unrouted r39 gate.

**C03 `translation-protocol-fidelity.md` — structural PASS with F2.** Sweeps: 9 of 10
reproduce exactly (`thick translation` 1; linguistics 0 + 0; corpus-wide
`domestication|foreignization` exactly the 5 cited files; `paratext` 2; `gloss` 13 of 21;
`glossing` 8) — **`interpreter` reads 47, not the claimed 48** (F2; four command variants).
All 6 sha256 source pins **MATCH live bytes** (`cultural-translation-protocol.md` `fb5d705b…`,
`verification-method-overview.md` `f52708d9…`, `two-reader-interop-agreement.md` `daebba3ae…`,
`naming-systems.md` `d972a1d6…`, `semantics-pragmatics.md` `9b9a3ff7…`,
`sociolinguistics-registers.md` `95ea235f…`); the full-HEAD sha in `- verified-at:` is correct.
Resolver flagged 10 refs out-of-range — **all 10 hand-verified as my binder's detached-`:n`
false positives**: they are `cultural-translation-protocol.md` anchors (209-line file), and
every sampled anchor reads true (:118 provenance split, :129 fallible editor, :164 §11 heading,
:166 not-a-world, :174-176 three beats, :177 template note, :178 C10-in-protocol, :190 removal
test, :206 mediation, :209 limits; overview :16/:18/:27-31 true). The three-object
separation/assert-license split/ten criteria are explicitly lane-authored house method
(calibration field). K03's E3 scope satisfied (strongest-absence topic, Appiah/Genette/Venuti
at their registered status).

**C04 `sacred-registers-liturgical-language.md` — structural PASS, clean.** All six absence
sweeps reproduce exactly: `event-typed` 0, `recitation accuracy` 1 (`religion-language-co-evolution.md:76`
— needle true), `liturgical fossilization` 2, `sacred register` 7, `recitation` 52, `liturg` 86
corpus-wide / **13 of 21** linguistics (also matches K03 §3's independent count). Needles true
(`religion-language-co-evolution.md:192,:203,:205`; `historical-linguistics.md:188,:237,:247`).
Boundary held per K03 E4: freeze mechanics extend :237's two-line mention; canon/religion
content routed out; the decay/revival ladder is declared orthogonal to
`language-shift-obsolescence-revival.md` and coupled, not duplicated. The sweep caveat
(self/sibling matches after landing) is pre-declared in its own `- gap filled:`.

**Collision re-check (K03's leg, independently re-derived):** no proposed basename exists in
`corpus/knowledge/linguistics/` (21-file listing) or collides with the synthesis counterparts'
basenames; final four names pairwise distinct; sort positions as in §1.4. K03's routing fact
re-verified: `ls corpus/knowledge/verification/ | grep -c 'lifecycle-gate\|dialect-register\|translation-protocol'`
→ 0 — the G2/G3/G4 **verification** gates remain unrouted; landing these linguistics entries
does not discharge them (routed-not-absorbed; all four entries say so in their own scopes).

## 3. Findings (severity-ranked; none is an S1)

| # | sev | finding | evidence | owner |
|---|---|---|---|---|
| **F1** | **S3** | **C01 carries three off-by-one source locators**: `historical-linguistics.md:3` → the `- sources:` line is **:4** (Campbell registration); `language-contact.md:3` → **:4** (Thomason & Kaufman; Baugh & Cable 5th ed.); the same `:3` is repeated in the `- couples:` line for both files. Files and blocks correct; every other locator in the entry spot-checked true. Fix: `:3` → `:4` (three sites, two in `- sources:`, two echoes in `- couples:`). | `corpus/knowledge/linguistics/historical-linguistics.md:3-4`; `language-contact.md:3-4`; entry-1 `- sources:`/`- couples:` (fence `d02221a5f462e41c`) | C01 / integrator (named-defects-allowed threshold) |
| **F2** | **S3** | **C03's `interpreter` sweep count is off by one**: claimed "48 files", measured **47** (`grep -ril` recursive and per-glob agree; `grep -rl` non-i = 43). The claim's substance (no translation-note ownership anywhere) is unaffected — 47 still means "all reference-data or other-system senses". Fix: state 47 or quote the exact command. | entry-3 `- gap filled:` (fence `1962fa5d947224c2`); four re-runs 2026-10-19 | C03 / integrator |
| **F3** | **S3-process** | **C06 was cut before C04/C05 landed** (its final poll 15:00:55Z; C04 landed ~15:06Z): §6 byte-pins only three rows, the fourth is a CANDIDATE probe (218 chars of disposable topic text), and the audit leg is absent. C06's own `## Owed` names both and forbids the candidate's bytes from the index. **This file supplies the real fourth row (§1.2) and the integrator regenerates mechanically at apply** — the delta is complete only after that regeneration. | `cov/C06-delta-receipt.md` §5.4, §Owed; landing timeline §4 here | integrator |
| **F4** | **note (instrument)** | **sweep-green does not enforce filename order**: my generator's shared-anchor disorder (`translation` above `taboo`) read green on the filed instrument until the order check caught it (§1.4). The r35 apply-order rule (bottom-up, larger merged_index first on shared anchors — C06 §5.2) is load-bearing, not cosmetic. Keep an order check in the acceptance sequence. | §1.4; `reports/round-28/readme/sweep.py` (no ordering leg) | this seat (recorded) / integrator (acceptance sequence) |

Landing-order note (process, no defect): P01 §4 sequences verifiers C05 → C06 → C07; landing
order was C01/K03 → … → C06 (~15:05Z) → C04 (~15:06Z) → C05 (absent at 15:11:45Z). Parallel
fragments land in completion order; the apply gate (entries land only after the audit is clean
or defect-listed) is the parent's, and it is still satisfiable — nothing has been applied.

## 4. Relation to C05 (absent) — the cross-check protocol

`reports/round-40/cov/C05-audit.md` did not exist at any poll up to 15:11:45Z (first poll
14:0xZ, six polls total). This seat's readings in §1–§3 are **independent primary
measurements**, taken so that the round possesses a second read of every entry regardless of
C05's landing. When C05 lands: its per-entry verdicts should be compared against §2 row by row;
any divergence (a PASS here vs FAIL there or vice versa, a sweep count differing from §2's
reproduced values, a needle reading contradicting §2's) is a new named finding with owner —
neither file is edited in place. Agreement is a consistency result, never correctness
(`verification/two-reader-interop-agreement.md`); and per the same entry, this seat authored no
audited byte and certifies no admission — the apply/admit call is the integrator's
(`REGIMEN.md:41-43`).

## 5. Limits

- **Structural + source-resolution verification, not scholarship and not canon.** Nothing here
  judges whether the four topics are the right four, whether the historical claims are true, or
  whether the entries should be promoted (`PROVINCE.md`; `corpus/QUALITY.md`). Literature legs
  are `(to-verify)` by the entries' own declaration; no fetch occurred.
- **Simulation, not landing.** §1.3's green is a digest-pinned reading of one candidate tree
  built from the draft fences; the landing's own evidence is the integrator's post-apply sweep
  (C06 §8.2), and any post-audit byte change to a fragment voids the corresponding reading here.
- **One resolver, known blind spots.** `refs.py` binds detached `:n` to the nearest preceding
  path (the r39-F6 ambiguity) — every flag it raised was hand-verified before inclusion (§2
  C03), and C01's F1 was confirmed by direct `sed -n` reads, not by the resolver alone.
- Fragment digests are §0's; a later in-place edit of any audited fragment is detectable
  against them.

## Owed

- `reports/round-40/cov/C05-audit.md` — the audit leg of claim C's threshold ("audit 4/4 PASS",
  `reports/round-40/claims.json:18`); absent at this seat's close (§4). Apply gate: entries land
  only after C05 is clean or its defects are filed; cross-check protocol in §4.
- Integrator: apply the four entries (C03 block 0 only) + C06's §4 edits + §5 rows **with the
  fourth row regenerated from C04's landed bytes** (cross-check §1.2), then the post-apply sweep
  + an explicit filename-order check (§1.4/F4) + C06 §8.1 GREEN + diff-vs-draft.
- F1 (C01) and F2 (C03) one-clause fixes — apply-as-is with named defects is within claim C's
  threshold; the integrator decides.
- `reports/round-40/run-validation.py` — integrator-authored at close per `REGIMEN.md:57`;
  per the absolute rule never executed in-tree by this seat.

## Citations

- `reports/round-40/claims.json:13-18` (claim C: before/after/counting commands/thresholds),
  `:32-33` (non_goals); `reports/round-40/targets.json:4-9` (shared rules), `:90-95` (seat C07)
- `reports/round-40/plan/P01-plan.md:64-66` (this seat's bound legs), `:154-160` (collision
  control + top risks naming this seat's recompute)
- `reports/round-40/scout/K03-gaps.md:25-34` (collision table), `:66-153` (E1–E4 binding
  scopes), `:172-177` (routed-not-absorbed; filename ownership)
- Audited fragments: §0's digest table (`cov/C01-entry-1.md`, `C02-entry-2.md`,
  `C03-entry-3.md`, `C04-entry-4.md`, `C06-delta-receipt.md`)
- Filed instruments (read-only): `reports/round-28/readme/sweep.py` (live run + module import;
  `--selftest` not re-run this seat — r39 measured it 12/12 at sha `9b2ccac0…`; the bytes are
  unchanged at `fd55e1f`), `tools/source-audit-inventory.py`
- Verified live bytes (needles): `corpus/knowledge/linguistics/{historical-linguistics.md:3-4,7,188,233,237,247,
  language-contact.md:3-4, politeness-taboo-euphemism.md:24,28,29,30,32,34,35,75,76,82,88,95,99,101,102,103,104,106,113,118,127,128,
  sociolinguistics-registers.md:64,140,148, register-lexicon-ceilings.md:12,182,238-240,
  conlang-methodology.md:3-4,90}`; `corpus/knowledge/synthesis/{taboo-euphemism-lifecycle.md:4-17,19,27,29,45,62,65,117,121,122,139,150,152,156,163,185,
  dialect-faction-map-workflow.md:93-94,202, migration-founder-effects.md:18,26,32-34,52,
  religion-language-co-evolution.md:76,192,203,205, cultural-translation-protocol.md:16,47-48,118,129,132,164,166,174-178,190,206,209}`;
  `corpus/knowledge/verification/{verification-method-overview.md:16,18,27-31,
  two-reader-interop-agreement.md}`; `corpus/README.md` at sha `e73dc971…` (549 lines / 132 721 B)
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD` / `HEAD:corpus/knowledge`; `git ls-tree -r --name-only <tree> | sort | sha256sum`
  and the live `find|sort|sha256sum` (both `a89679bf…`); linguistics census + r28 sweep live
  (216/216 green, exit 0); fence extraction ×4 (+ block census); ref resolution ×3 (75/75,
  77/77, 103/113 with 10 flags hand-cleared); sweep re-runs verbatim per entry (C01 6, C02 6,
  C03 10, C04 6 + the 13-of-21 split); sha256 batteries (C03 6/6 MATCH; 4 fragments + K03 +
  C06 pinned; 4 generated rows pinned); needle reads (~55, all quoted in §2); delta simulation
  with negative controls + inventory (§1.3); filename-order check ×2 (first caught this seat's
  own shared-anchor bug — F4; fixed; re-run True); fragment polls of `reports/round-40/**`
  (§4). **Not run, deliberately**: any `reports/round-*/run-validation.py`; any network call;
  no write outside this fragment and `.scratch/c07/`.
- Scratch (disposable, not evidence): `.scratch/c07/{fence.py,refs.py,delta.py}`,
  `.scratch/c07/stage/linguistics/` (4 entries under landing names),
  `.scratch/c07/work/{README.generated.md,delta-report.json}`, `.scratch/c07/work/simtree/`
