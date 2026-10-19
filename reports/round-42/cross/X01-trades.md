- Seat: X01 | critic | cross | date 2026-10-19 | baseline ac47c78

Trade hunter + conformance critic. Critique target: the round's declared claims
(`reports/round-42/claims.json:12-25`), the binding seat missions
(`reports/round-42/targets.json`), and the repo state measured at baseline
`ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` (`git rev-parse HEAD`; the only
working-tree change is untracked `reports/round-42/`). The wave runs
concurrently: no sibling fragment was landed at my cut, so this is a
plan-and-measured-state critique; seat-output review is R01/R02's lane plus the
integrator's validation leg. Every number below is a command output or a
file:line read; nothing reconstructed.

## Trades

### T1 — O vs C share one mutable measurement surface: DECLARED TRADE, unresolved

O's after-requirement is "the corrected census filed" (`claims.json:16`); C adds
four entries to `corpus/knowledge/myth-symbol/` (`claims.json:20`). Those four
entries are *themselves* couples-bearing inputs to the census. Measured, same
extractor, same tree rule, only the entry set differs:

| tree | refs | direct | fallback | ambiguous | unresolved |
|---|---|---|---|---|---|
| r39 tree (212 entries) | 2504 | 2335 | 163 | 0 | 6 |
| r42 tree (220 entries) | 2611 | 2437 | 166 | 0 | 6 |

(block-parser readings for the same two trees: 2508/2337/163/0/8 and
2611/2437/166/0/8). So +8 entries moved the census by +107 refs. The four C
entries will move it again. A "corrected census" that does not name its entry
count and a tree digest is unfalsifiable and will be stale the moment C lands.
Required fix: O03/O04 and the landed census name the tree state (entry count +
`corpus/README.md` / entry-set digest) at which the recount was taken, per the
lane's own rule that "a green reading is a digest-pinned reading of one tree
state, never a state of the world"
(`corpus/knowledge/verification/index-sweep-verification.md:291`). Landing order
matters: census last, or census twice with both states recorded.

### T2 — C's four entries can manufacture O's "phantom attributions"

O's threshold is "zero phantom attributions remaining or each dispositioned"
(`claims.json:16`). A new myth-symbol entry whose `- couples:` names a file that
does not exist is a *new* unresolved token, indistinguishable in the census from
the pre-existing ones. `corpus/QUALITY.md:11-13` (item 3) requires the line and
`reports/round-35/cov/C12-audit-runbook.md:34` makes a missing couples leg a
blocker, but neither forbids a dangling target. Concrete pre-landing check for
C05/C07/C08: for each of the 4 drafts, resolve every `.md` token in its
`- couples:` field and report the token classes. Otherwise the round can land
entries that add phantoms and then report the phantoms dispositioned.

### T3 — the uniqueness assumption must be re-adjudicated at 224, not assumed

The adopted policy pins "Index scope is exactly one partition level
(`corpus/knowledge/*/*.md`; 6 partitions, 212 files at adoption). Nesting, a new
top-level directory, or duplicate basenames across partitions change the
uniqueness assumption: re-run §6 and re-adjudicate"
(`reports/round-39/calib/basename-couples-policy.md:93-96`). Measured today: 220
basenames, 220 unique, **0 collisions** (python probe, `collections.defaultdict`
over `glob corpus/knowledge/*/*.md`). Adding 4 myth-symbol entries makes it 224;
if any new basename collides with an existing one the `fallback` class changes
for other entries. The wave must re-run the collision probe at 224 and say so,
rather than inheriting "0 collisions" from my 220-entry reading.

### T4 — O's fix surface: the claim's named host does not exist; the correct host is a gate, not a harness

`claims.json:16` says the host is "likely the r39 C12 runbook's resolver or a
tools/harness couples checker; the wave confirms the host". Measured:

- `reports/round-35/cov/C12-audit-runbook.md` is a **markdown runbook**, not an
  executable. Its couples content is prose (`:34-35`, `:56`, `:258-264`). It
  cannot be a host.
- `tools/harness/` holds `packet_links.py`, `packet_uncertainty.py`,
  `r8_checks.py`, `receipt_guard.py`, `receipt_guard_adoption.py`,
  `round_runner_conformance.py` — **no couples checker** (`ls tools/harness/`).
- The only executable couples resolvers in the repo are filed round fragments:
  `reports/round-19/audit/entry-audit.py:74-96` (the single-line defect) and
  `reports/round-35/cov/C14-audit-6-10.md:227-288` (block parser). Both sit
  under `reports/round-*/`, which this round's own non-goals forbid editing
  (`claims.json:26`, "no filed byte rewrites"; `targets.json:6` shared rule).
- `tools/gates/provenance-audit.py:244-260` already contains a **correct block
  parser** (`field_block`) that reads the wrapped field whole, and it has a
  multi-line control already: `check("multi-line couples parsed",
  r7["couples_refs"] == 3 and r7["couples_unresolved"] == [], ...)` at
  `:448-449`. Imported directly, it returns `present=True` and tokens
  `['sound-change.md', 'prosody.md', 'sound-symbolism.md', 'writing-systems.md']`
  on the live wrapped field (my import probe).

So the O claim has a real, unfilled gap: **there is no writable durable host as
described**. It is not under `tools/gates/frozen/**`, so
`tools/gates/provenance-audit.py` is writable, and its parser is already correct.
Recommended shape: a thin census instrument (new file, e.g.
`tools/harness/couples-census.py`, allowed) that **imports**
`provenance-audit.field_block` rather than adding a fourth hand-rolled parser.
Do not add a duplicate resolver beside r19/r27/C14.

### T5 — the block-parser fix as specified is incomplete: it trades 2 phantoms for 1 mangled artifact

The wrapped field's last two lines are:

    - couples: … prospective sibling files: sound-change.md, tone-
      prosody.md, sound-symbolism.md, writing-systems.md

(`corpus/knowledge/linguistics/phonetics-phonology.md:76-77`, raw bytes read).
`tone-prosody.md` is split across the line break by the hyphen. Measured three
ways on the same live corpus:

| extractor | r39-tree refs | unresolved | the wrapped field's non-resolving tokens |
|---|---|---|---|
| single-line (filed rule) | 2504 | 6 | (none captured — 0 tokens) |
| block, continuation-join only | 2508 | 8 | `sound-change.md`, **`prosody.md`** |
| block, continuation-join + hyphen-rejoin | 2508 | 8 | `sound-change.md`, **`tone-prosody.md`** |

The naive continuation join *invents* the token `prosody.md`, which no entry
names — a phantom the single-line extractor did not have and which Ca04 D1
flagged as "an extractor hazard *no* current instrument handles"
(`reports/round-39/calib/Ca04-verify.md:82-87`). A fix that reads continuations
without de-hyphenating therefore does not reach "zero phantom attributions": it
swaps two invisible phantoms for one visible one. The landed parser must join
continuations **and** rejoin hyphen-wrapped tokens (or declare the artifact
class explicitly). The claim's after-requirement does not state this
(`claims.json:16`), and O02's "synthetic phantom negative" control should
include a hyphen-wrapped positive, not only a continuation-wrapped one.

### T6 — O's quoted census arithmetic is internally inconsistent (conformance defect)

`claims.json:14-15`: "the r39 policy's 2504 = 2335 + 163 + 0 + 6 becomes the
corrected baseline with the 2 phantom attributions dispositioned" and "the
single-line extractor silently zeroes the wrapped couples field — 0 tokens
captured vs 4 named, 2 phantom attributions in the census".

Two defects:

1. **Category error.** If the extractor captures 0 tokens on the wrapped field,
   that field's two non-existent targets cannot be "in the census" — they are
   invisible to it. That is the whole point of the defect, and Ca04 D1 states
   the same ("No effect on the 15-ref population"; the block-parser population
   is the one that gains them — `Ca04-verify.md:80-86`). Fixing the extractor
   *adds* two unresolved tokens (6 → 8); it does not remove two from 2504. The
   before-state sentence contradicts itself.
2. **The corrected baseline is stated in the wrong direction.** The "corrected
   census" is 2508 = 2337 + 163 + 0 + 8 on the r39 tree (my independent recount
   of the block parser, reproduced exactly), or 2611 = 2437 + 166 + 0 + 8 at
   r42's 220 entries — not "2504 minus the phantoms". The claim should read:
   single-line 2504/2335/163/0/6 → block-parser 2508/2337/163/0/8, with the 2
   added unresolved tokens named (`sound-change.md`, `tone-prosody.md`) and the
   pre-existing 6 carried unchanged.

I independently reproduced the r39 policy's arithmetic exactly on the r39 tree
(2504 = 2335 + 163 + 0 + 6, 5 distinct) — so the policy's Part 2 is confirmed,
not in dispute. What is in dispute is the claim's description of what the fix
does to it.

### T7 — C06's mission vector contradicts its own total and the footer order (conformance defect, blocking)

`targets.json:163` binds C06 to "README rev 2.4 delta draft (myth-symbol 27,
totals 224, **vector 25/23/27/25/24/94**, 4 rows in filename order)". Measured:

- The literal sums to **218**, not 224: 25+23+27+25+24+94 = 218.
- The README footer vector's order is fixed and measured — the sweep reports
  `footer_live.order = ["linguistics", "myth-symbol", "culture-material",
  "synthesis", "verification", "civilizations"]`
  (`reports/round-28/readme/sweep.py` live run; README footer at
  `corpus/README.md:536`). Live vector today: `25/23/25/29/24/94`
  (civilizations 94, culture-material 25, linguistics 25, myth-symbol 23,
  synthesis 29, verification 24 — sweep `parts` output).
- Slot 2 in the literal is `23` (unmoved) while slot 3 is `27` — the myth-symbol
  move landed in the **culture-material** position. Slot 4 reads `25` where
  culture-material's `25` belongs, so `29` (synthesis) was dropped entirely.

The literal appears to be the r40 vector `25/23/25/29/24/94`
(`reports/round-40/targets.json:86`) with `27` inserted into slot 3 instead of
slot 2. Correct rev-2.4 vector: **`25/27/25/29/24/94`** (sum 224). A C06 seat
following its mission literal byte-for-byte produces a README that is
`footer_ok False` — and the sweep *does* now read the footer
(`reports/round-28/readme/sweep.py:106` `footer_reading`, `:163-192` the footer
leg, `:206-210` `footer_live`/`footer_findings`), so the green it once gave over
a stale footer (README rev 1.8, `corpus/README.md:62-78`) is no longer
available. The sweep must be run on the delivered revision and read
`footer_ok True`, not merely exit 0.

Note the contrast that makes this a real hazard rather than pedantry: r40's C06
mission stated the vector in full, before→after
(`reports/round-40/targets.json:86`), and r40's delta note explicitly resolved a
similar ambiguity in its totals leg
(`reports/round-40/cov/C06-delta-receipt.md:24-26`). r42's mission states a
vector that is arithmetically impossible.

### T8 — no trade: the sweep's footer leg closes the r1.8 footer-blind class

Hypothesized cost of C: a footer-blind green (the r27/rev-1.7 failure recorded
at `corpus/README.md:62-78`). Measured: the sweep reads the footer and reports
it separately. Live run on the current tree:

    rows 220 files 220; missing_from_index 0; topic_mismatch 0; orphan_rows 0;
    header_drift {}; totals_line 220 totals_ok True;
    footer {"total": 220, "dir_totals": [25, 23, 25, 29, 24, 94]};
    footer_findings [] footer_ok True; readme_sha256 d2eed26b…; EXIT=0

So "sweep green" is a real check today and C's threshold (`claims.json:22-24`)
is satisfiable. No trade — but the threshold should be strengthened to
"`footer_ok True` on the delivered revision", since a totals-only drift is
reported separately from the footer leg by design (`sweep.py:24-25`).

### T9 — no trade: filed policy and pin surfaces are preserved

Checked because O changes an adopted policy's extractor: the policy is filed at
`reports/round-39/calib/basename-couples-policy.md` and cannot be edited
(`claims.json:26`). Its §1 declares the single-line extraction as adopted policy
(`:16-18`) and §5.6 forbids counting glob fragments (`:97-101`). The fix must
therefore land as a **successor note** (O12's mission, `targets.json:154-157`),
not as a policy edit. The `-gate.md` fragment from
`corpus/knowledge/verification/gate-frozen-run-standard.md:15` is still counted
as `unresolved` by every instrument I ran (single-line and block); policy §5.6
says it must be skipped or separately classed, not counted as a couples finding.
That is one of the "phantom attributions" needing a disposition — and its
disposition is policy-mandated, not a corpus edit.

Also checked: the C delta touches only `corpus/README.md` plus four new
myth-symbol paths, which breaks no r34 `declared-in-r7` pin (that expected.json
has 0 README and 0 linguistics hits — r40's X01 T1 measurement, re-asserted
here as the precedent to preserve, not re-measured). No re-freeze is proposed by
this round (`claims.json:27`).

## Axis verdict preview

No axis is harmed by either claim *as declared*. Operability is the real move
(T1-T6); coverage is a clean additive move (T2/T3 are pre-landing checks, not
costs). Freshness stays paused as declared (`claims.json:11`). The risk is not a
trade between axes — it is three arithmetic/description defects (T5, T6, T7)
that would make an admitted round's record wrong while every command still
exits 0.

## Owed

- Seat-fragment-level review (O03/O04/O05/O08, C05/C06/C07/C08, R01/R02):
  impossible at this seat's cut in a concurrent wave; owed by R01/R02 and the
  integrator's validation leg. Specifically owed: (a) does the landed census
  name its tree state (T1)? (b) does the landed parser de-hyphenate (T5)? (c)
  did C06 use `25/27/25/29/24/94` or its mission literal (T7)?
- `reports/round-42/run-validation.py` does not exist at this cut (`ls
  reports/round-42/` → claims.json, targets.json, telemetry/ only); the O
  counting command is therefore to-verify. I did not run it and will not run any
  in-tree runner.
- The r42 closing telemetry snapshot is owed by the parent once `validation.json`
  lands (`AGENTS.md` closing-snapshot rule).
- Integrator: correct the C06 mission vector and the O before/after census
  description before landing; both are `targets.json`/`claims.json` text, not
  filed bytes, so both are in scope to fix this round.

## Citations

- Binding: `reports/round-42/claims.json:12-25` (claims, thresholds,
  non-goals), `:7` baseline, `:11` freshness pause; `reports/round-42/targets.json:163`
  (C06 vector), `:6` shared rules, `:188-193` this seat, `:154-157` O12.
- N6 lineage: `reports/round-40/op/defect-queue-v2.json` rows
  `N6-couples-extractor-wrapped-field` (origin "r39 Ca04 D1", class
  carried-with-owner) and `r39-basename-successor-instrument`;
  `reports/round-39/calib/Ca04-verify.md:78-105` (D1 + the 2 phantoms, the
  hyphen hazard, "no effect on the 15-ref population"), `:107-115` (owed
  recount); `reports/round-39/calib/basename-couples-policy.md:16-18` (§1
  single-line, adopted), `:93-96` (§5.5 re-adjudication trigger), `:97-101`
  (§5.6 glob fragments), `:9` (successor-instrument rule).
- Extractor code: `reports/round-19/audit/entry-audit.py:75` (single-line
  regex, the defect), `:74-96` (couples resolution), `:31,34-42` (token regex,
  brace expansion); `reports/round-35/cov/C14-audit-6-10.md:227-236` (block
  parser), `:249-288` (four-class resolution), `:115` ("8 unresolved / 7
  distinct"), `:552` (the filed 2174→8 unresolved reading at 201 entries);
  `reports/round-27/audit/entry-audit.py:129-131` (slash-free partition loop).
- Correct existing host: `tools/gates/provenance-audit.py:244-260`
  (`field_block`), `:448-449` (multi-line couples control), `:75-76` (field
  regex); import probe output tokens on the live wrapped field.
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (field lines; `:76-77` carry the hyphen wrap), file sha256 prefix
  `b4f9b00384bc6840`.
- Corpus/README state: `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 23;
  `ls corpus/knowledge/*/*.md | wc -l` → 220; partition census civ 94 / CM 25 /
  ling 25 / MS 23 / synth 29 / verif 24; `corpus/README.md:532` ("Total
  knowledge entries: 220."), `:536` (footer `(total 220 files; directory totals
  25/23/25/29/24/94)`), `:62-78` (rev 1.8 footer-blind-green history); README
  sha256 prefix `d2eed26b30e8e621`.
- Sweep: `reports/round-28/readme/sweep.py:106` (`footer_reading`), `:163-192`
  (footer leg), `:206-210` (`footer_live`, `footer_findings`), `:24-25`
  (totals-only drift reported separately); live run output quoted in T8.
- Admission bar: `corpus/QUALITY.md:11-13` (item 3 coupling);
  `reports/round-35/cov/C12-audit-runbook.md:34` (row 1a couples leg = blocker),
  `:37` (row 2 dangling-pointer disposition).
- Command outputs (this seat, 2026-10-19, lane root, tree at `ac47c78`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only, no
  runner invoked): the four-way census table (T1/T5) from an inline `python3 -B`
  block parser + single-line probe over the live tree and a synthetic r39 tree
  (the 8 post-r39 basenames excluded by name: the four r39 verification entries
  and the four r40 linguistics entries); basename-collision probe (220 unique /
  0 collisions); `provenance-audit.field_block` import probe; `sweep.py` live
  run (exit 0, `footer_ok True`, quoted above); `git rev-parse HEAD`.
