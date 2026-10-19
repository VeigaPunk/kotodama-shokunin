- Seat: R02 | reviewer | claim C | date 2026-10-19 | baseline 4a7aede

# R02 — adversarial review of entries 6-10 (claim C / coverage)

**Assignment** (`reports/round-35/targets.json:331-334`, seat `R02`): role `reviewer`,
claim `C`, out `review/R02-c-review.md`, mission verbatim: *"Adversarial review of
entries 6-10 with the same method."* The method referenced is R01's ("Adversarial
review of entries 1-5: source-pointer resolution re-checked independently,
frontmatter re-read, no-fabrication hunt", `targets.json:330`). R01's fragment was
absent at every stamp of this review (`review/R01-c-review.md`; §5 poll log), so the
method was reconstructed from the lane's filed precedent —
`reports/round-10/coverage/review-C06.md:19-22` and
`reports/round-10/coverage/review-C10.md:19-30` — and
extended with the round-35 claim-C contract (`reports/round-35/claims.json:22-35`).
§3 states the reconstruction so R01's fragment, when it lands, can be diffed against it.

**Role limits.** Reviewer seat, read-only over the lane. My only writes are this
fragment and disposable `.scratch/` files. No corpus byte, no `tools/**` byte, no
filed round byte is touched; no `reports/round-*/run-validation.py` was executed
anywhere (F-C13-1). I admit no entry, certify no round, clear nothing, decide no
canon: promotion/canon/closure are operator- and lore-shokunin-owned (`corpus/QUALITY.md:20-23`).
This is author-side review evidence, not independent promotion verification.

**Status: all five review targets landed and are reviewed below** (arrivals
08:24:35Z–08:30:13Z, §5). One round-level fact outside my five: **`cov/C04-entry-4.md`
is absent** — nine of the ten claim-C drafts exist, so the +6 culture-material leg
has five drafts (C01, C02, C03, C05, C06) and the claim's 10/10 and
inventory-211 thresholds are unreachable at this stamp (§7 R02-F8).

---

## 1. What "entries 6-10" are, and the contract they must meet

Seat split (`targets.json`, claim C): `C01`–`C05` author entries 1-5 (culture-material),
`C06` authors **entry 6** (culture-material), `C07`–`C10` author **entries 7-10**
(myth-symbol). My five targets are the last culture-material draft and all four
myth-symbol drafts; R01 owns 1-5, C13 audits 1-5, **C14 audits 6-10**, C17 samples
three by lot (it sampled entries 2, 6, 10 — `cov/C17-audit-sample.md:14-16`).

Binding per-entry contract (`claims.json:24,29`): gap-named in-file;
frontmatter-complete against the literal vector `source / verified-at / recheck /
scope` (with a "documented 3/4 class" allowed); decision-record carrying;
source-resolving (resolve or mark `to-verify` in-file); zero fabricated sources;
README index reconciled to the new counts.

## 2. Baselines frozen by this seat at HEAD `4a7aede`

Window 2026-10-19 ~08:14Z–08:32Z; `git rev-parse --short HEAD` → `4a7aede`;
`git status --porcelain` → `?? reports/round-35/` only, so every corpus number is a
baseline number.

### 2.1 Census and slugs

```
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21 19 18 29 20 94            # find corpus/knowledge -name '*.md' | wc -l → 201
```

culture-material (18) and myth-symbol (19) slug lists are enumerated in the seat's
census; the five drafts' targets (`fire-fuel-light`, `eschatology-world-end-systems`,
`sacred-kingship-mythic-charter`, `death-afterlife-eschatology`,
`binding-speech-complex`) collide with no existing slug — verified per draft (§8).

### 2.2 Digests (post-landing attribution)

```
$ sha256sum corpus/knowledge/culture-material/*.md | sha256sum
ef0560da5288304ed648648915d87d52faa5f21c4486b29c596e6e4fed622f6a
$ sha256sum corpus/knowledge/myth-symbol/*.md | sha256sum
da0505ad024d8d8ddb4d06b8b2cc146179de1ffd1d871c3897e9f1ab82f6eb2b
$ sha256sum corpus/knowledge/culture-material/*.md corpus/knowledge/myth-symbol/*.md | sha256sum
5a0c27be75212dfe43014f6563f391236f1b1a5ba07e2661fb5c9b8bd87b91d8
```

Per-file digests for all 37 files: `.scratch/r02-baseline-digests.txt` (37 rows,
disposable). Post-landing, the two aggregates must change while no existing file's
per-file row may change — an existing file edited by the wave is an unclaimed corpus
edit and a finding.

### 2.3 README pin (reconciliation surface)

`corpus/README.md` sha256 `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`,
493 lines, 106218 bytes. Present-tense surfaces: `:147` `## myth-symbol/ (19)` ·
`:169` `## culture-material/ (18)` · `:469` `Total knowledge entries: 201.` ·
`:471` `Counts checked 2026-10-18 from the repo root:` · `:473`
`(total 201 files; directory totals 21/19/18/29/20/94).` My own index sweep:
**201 rows vs 201 files, 0 ghosts, 0 missing, 0 duplicate rows, 0 header drift,
0 topic mismatches**; both target sections ASCII-filename-sorted (`:149-167` = 19 rows,
`:171-188` = 18 rows) — reproducing `reports/round-28/readme/sweep.py:60-61,74-78`
by an independent reader (§3.2 records the one false positive my first-pass reader
produced).

### 2.4 Inventory before-state (marker attribution)

```
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
files 201 · files_with_any_mark 147 · files_with_marker 135 · lines 36395 ·
raw_lines 717 · raw_occurrences 731 · ci_occurrences 733 · case_variant 2 ·
marker_occurrences 655 · bare 621 · detailed 34 · marker_lines 650 · unparenthesized 78
```

**Predicted after-state, computed by running the real tool over the extracted draft
bytes** (not by hand-counting — see R02-F7): five drafts (mine) → files +5,
raw_occurrences +174, marker_occurrences +35 (bare +17, detailed +18), raw_lines +141,
marker_lines +33, unparenthesized +139, lines +1074. All nine drafts on disk → files
210, raw_occurrences 1040, marker_occurrences 777, bare 715, detailed 62, raw_lines
972, marker_lines 763, unparenthesized 265, lines 38213. Landing nine gives **210, not
211** — the tenth draft (entry 4) is required for the claim's threshold.

### 2.5 Freeze cross-reference (not this seat's verdict)

The pinned r7 freeze read-set carries exactly one `corpus/knowledge` member
(`reports/round-34/handoff/declared-in-r7/expected.json:125` →
`synthesis/worldbible-integration-contract.md`). Entries 6-10 land in
culture-material/myth-symbol, so they cannot drift that member by construction.
Routed to R08 as a cross-reference, not my verdict.

## 3. The method and its instruments' calibration

### 3.1 The checks

From `reports/round-10/coverage/review-C06.md:19-22`, applied per draft: (1)
frontmatter completeness (house profile `topic/sources/couples/verified-at/recheck`,
exactly once, non-empty, no placeholder, `verified-at` dated and scope-bearing,
every `couples` target resolving) plus the claim's 4/4 vector under **both**
readings (house `sources` vs literal `source`); (2) source resolvability (backticked
repo paths brace-expanded, bare filenames resolved by unique basename — the r10
convention — with ambiguity reported; cited commands re-run or marked unrunnable;
URLs recorded, never fetched, never counted as resolved); (3) no filler + decision
record (`## … decision record …` heading with content, r10 regex
`reports/round-10/run-validation.py:368-370`, and the gap real against the
partition); (4) no duplication (slug collision, topic-token Jaccard vs the target
partition, 8-gram body-shingle Jaccard vs all 201 entries). Round-35 additions: (5)
no-fabrication (digest tokens attested against live files and receipts; a stated
64-hex digest must equal the block or fragment digest; author-year attestation;
URLs without access notes flagged); (6) no-bleed **triage read with context**;
(7) marker attribution (§2.4) and README-delta consistency (§2.3, §6.6).

### 3.2 Calibration — six defects found in my own instrument before/while it was used

The instrument (`§Instrument`, embedded) was calibrated against live entries, planted
fixtures, and — decisively — against peer auditors' independent readings. Six
self-caught defects, each fixed before the reading it affected was reported:

1. **README row = one line** — my first reader produced 2 false topic mismatches
   (`numerals-and-measures.md`, `phonetics-phonology.md`: wrapped `- topic:` fields);
   joining continuations as `reports/round-28/readme/sweep.py:74-78` does gives 0, matching the filed sweep.
2. **Self-comparison** — the `--entry` duplication leg compared a file against
   itself (0.90 self-match); fixed by self-exclusion.
3. **Slug from a reference** — the slug leg read a *cited* path as the draft's own
   target; fixed to prefer the declared target that is absent from the tree.
4. **Control outside the fence** — the planted bleed line sat outside the fenced
   block, so extraction correctly dropped it; the control was moved inside.
5. **Block-valued `- sources:`** — a field whose value sits on indented bullets was
   counted as missing, so I first reported the house field absent on entries 6-8.
   Fixed; the corrected reading (both `sources` and `source` present) matches C17's
   seven-field reading of entry 6 (`cov/C17-audit-sample.md:410-413`) exactly.
6. **Nested fences** — a non-greedy regex truncated/extended entries carrying inner
   ```-blocks (C07 read 47342 bytes / `7065078a…` under the old reader vs 47399
   bytes / `e6bc159d…` under a fence-stack scan, which equals the author's own
   stated digest). Rewritten as a fence-stack scanner; it now reproduces every
   author-stated byte count and digest (§8).

`--selftest` is **10/10** at the digest of the embedded instrument block.

### 3.3 Two false-positive classes this review must not repeat

- **No-bleed**: the leg reads **30/37** live entries as having "unguarded" hits;
  reading the contexts, **0 of 30 are real** ("Nicaea's Easter canon", "a closed
  technical register", "promoted to a universal ladder"). An audit reporting "0
  bleed hits" without contexts is a false negative; one reporting hits without
  reading them is a false positive. Corroborates C12's tiering of 5a-5c as *review*
  (`cov/C12-audit-runbook.md:41`).
- **Citation-by-substring**: my first probe for C07's `creation-myths-taxonomy.md:110`
  searched the literal phrase "end type" and read false; the line states the
  derivation in its own words ("Set eschatology from the creation type — combat:
  final battle and renewal; ex nihilo: linear consummati…"). Filing on substring
  absence alone would have produced a false finding.

### 3.4 Baseline profile of the two target partitions (37 entries)

`scope` **0/37**; 4/4 under either reading **0/37**; both gap statement and decision
record **5/37** (`transport-mobility-lexicon`, `vessel-container-lexicon`,
`direction-symbolism`, `divination-omen-systems`, `plant-symbolism` — the r10/r19
landings); unresolved `couples` targets **0/37**; max 8-gram overlap **0.0085** (the
0.05 flag threshold is far above baseline noise); 0/37 unattested digests.

## 4. Peer fragments independently reproduced, and agreements

| peer | its claim | my reading | verdict |
|---|---|---|---|
| `cov/C11-readme-delta.md:9-17` | README pin `053966a2…`, 106218 B, 493 lines; line map; rows sorted | identical; every line byte-equal; 19/18 rows ASCII-sorted | reproduced |
| `cov/C15-receipt.md:31-35,104-110` | before 201; vector 21/19/18/29/20/94; after 211 / 21/23/24/29/20/94 | identical | reproduced |
| `scribe/S01-c-receipt.md:36-38,73-80,126-129` | before confirmed two methods; line map | identical | reproduced |
| `cov/C16-scribe.md:126-133` | 201-file aggregate `cc5deee39b7e…`; per-partition digests | linguistics `c6248d92`, culture-material `ef0560da`, myth-symbol `da0505ad`, synthesis `d6fdacc4`, verification `b88fc106`, civilizations `d1c50bf4`; aggregate `cc5deee39b7e0bc369fa36979ec524bddef02ea139796347b915a548bddb880c` | reproduced byte-for-byte |
| `scout/K02-entry-audit-method.md:122-160` | `scope` 0/201; singular `source` 131/201; culture-material 0/18 singular; tail trio 198/201 | identical | reproduced |
| `cov/C14-audit-6-10.md:26` (C14-F1) | `scope:` exists nowhere | identical | reproduced |
| `cov/C17-audit-sample.md:405-437` | entry 6: 0 defects; 1 inline marker; 7 fields | my corrected reader agrees on all three | agree |

**Independent agreement on the round's central ambiguity**: R02-F1, K02 §2.3,
C14-F1 and C17-1 (four seats, three of them independent auditors) all measured the
same unreachable literal vector. C17-2 additionally found "documented 3/4 class"
undefined anywhere in the repo; my §8 confirms that reading is doing real work in
this round (entry 8's 3/4 is the claim's letter, and the "class" it might belong to
has no definition).

Not verified by me and not mine to verify: entries 1-5, the O-block renderer
hardening, the A-block adjacency slices, and `reports/round-35/run-validation.py`
(which does not exist yet — a mid-round state, `scout/K02-entry-audit-method.md:12-14`).

## 5. Poll log and arrivals (this seat's own `ls` stamps)

- 08:18Z — `claims.json`, `targets.json`, `telemetry/*` only.
- 08:19Z–08:22Z — `cov/C15`, `cov/C16`, `cov/C11`, `cov/C12`, `plan/P02`, `scout/K02`, `scout/K03`, `review/R06`, `adj/*`, `cross/*`, `op/*`, `scribe/*`, `cov/C02` (**entry 2**), `cov/C14`, `cov/C17`.
- **C06** present by 08:24:35Z (poll 20) · **C07** by 08:26:50Z (poll 29) · **C08** by 08:25:35Z (poll 24) · **C09 and C10** by 08:30:13Z (second watcher, poll 6).
- `cov/C04-entry-4.md`: **absent** at every stamp through 08:32Z.
- `review/R01-c-review.md`: absent at every stamp → §3.1's method is a
  reconstruction; the integrator can diff the two check lists when R01 lands.

## 6. Checks (executed; command form for re-run)

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/r02-review.py --selftest            # 10/10, exit 0
python3 -B .scratch/r02-review.py --draft reports/round-35/cov/C06-entry-6.md \
  reports/round-35/cov/C07-entry-7.md reports/round-35/cov/C08-entry-8.md \
  reports/round-35/cov/C09-entry-9.md reports/round-35/cov/C10-entry-10.md
```

| # | check | expected (pre-registered) | observed for 6-10 |
|---|---|---|---|
| 1 | extract: one fenced block, target partition (6 → culture-material; 7-10 → myth-symbol) | match | all five match; stated digests match for 6, 7, 9, 10 (8 states none) |
| 2 | frontmatter: house trio + both 4/4 readings | present | all five carry `topic`, `couples`, `sources` (block-valued) **and** `source`; `scope` only in 10 → 3/4 (both readings) for 6-9 under the claim's letter, 4/4 for all five under C12's `R35-4F-1` |
| 3 | gap named and real | present | present in all five; each verified against the live partition |
| 4 | decision record | present | present in 6, 7, 9, 10 (§10/§12/§11/§13); **absent in 8** (R02-F6) |
| 5 | marker attribution (§2.4) | exact delta | prediction computed; requires the after-state to equal it |
| 6 | README delta | 23/24/211/21/23/24/29/20/94; rows 211; sorted | not yet applicable (delta unapplied); anchors verified (§2.3) |
| 7 | no-fabrication | 0 unattested | 0 in all five; 0 URLs; external works marked un-re-fetched in `verified-at` |
| 8 | no-bleed, read | 0 real hits | 0 real hits across 19 triage hits (read individually, §8) |

## 7. Findings

- **R02-F1 (claim-level; routed, not absorbed)** — the claim's literal
  `source / verified-at / recheck / scope` vector is unreachable in this corpus:
  `scope` reads **0/201** (my census; K02 §2.3, C14-F1, C17-1 agree), and a literal
  4/4 would fail entries 6-9 at birth. C12 pins reading `R35-4F-1`
  (`cov/C12-audit-runbook.md:34,61`) — a reading choice, not the claim's letter. My
  reviews report both readings per draft. **Owner: P01/C12/integrator (R03 owns
  runbook adequacy).**
- **R02-F2 (pre-existing, live)** — `corpus/knowledge/verification/label-channel-routing-verification.md:14`
  couples `../linguistics/phonology-sanity.md`, which does not exist (the live file
  is `linguistics/phonetics-phonology.md`); reproduced by my couples leg (1
  unresolved). Independently found at `scout/K02-entry-audit-method.md:173` (D1
  class, `reports/round-19/audit/x26-spotcheck-entries.md` §3 X26-1). Not a defect
  of entries 6-10; recorded so it is not re-filed as new.
- **R02-F3 (method)** — a "no-bleed: 0 hits" claim without contexts is a false
  negative; baseline is 30/37 triage hits, 0 real (§3.3).
- **R02-F4 (pre-registered risk)** — README row insertion must preserve ASCII
  filename order; the two section anchors are named in §2.3. A slug sorting before
  `animal-symbolism.md` (myth-symbol) or `adornment-body-codes.md` (culture-material)
  inserts at the section head; none of the five new slugs does.
- **R02-F5 (cross-reference; R08's verdict)** — the r7 freeze read-set cannot be
  drifted by entries 6-10 (§2.5).
- **R02-F6 (entry-side finding; owner C08/integrator)** — **entry 8 carries no
  decision record**: `^#{2,4}.*decision` → 0 headings; `DR-` ids → 0; §10 is an
  application protocol (build steps), not a record of decisions with
  options/evidence/falsifier such as `myth-symbol/plant-symbolism.md` §11 D1-D6
  carries. This is not a D4-class false negative (the substance is absent, not in a
  non-matching form). Claim C makes decision-record carrying part of the contract
  (`claims.json:24`); C12 tiers it major (`cov/C12-audit-runbook.md:39`); the r10
  precedent calls absence "a finding against the C claim, not a style note"
  (`reports/round-10/coverage/review-C06.md:21`). Entry-side repair is one added
  `## … Decision record …` section; alternatively the round pins a reading that
  accepts §10's protocol — that adjudication is not this seat's.
- **R02-F7 (counting-leg finding; owner integrator/C12)** — the drafts write inline
  marks in at least three textual forms (`` `to-verify` ``, `(to-verify)`,
  `` (`to-verify`: …) ``), and the inventory counter's regex `\(to-verify[^)]*\)`
  sees only the middle form: entry 6 has 39 raw occurrences but **1** counted marker;
  entry 7 has 15 raw / 4 markers; entry 8 61/6; entry 9 31/2; entry 10 28/22. An
  audit that predicts the after-state by counting marks by hand will be wrong; the
  prediction must run the tool over the draft bytes (as §2.4 does). Granularity also
  varies per draft, corroborating C17-5 — an auditor ranking drafts on inline-mark
  count is ranking house style, not provenance discipline.
- **R02-F8 (round-level; owner integrator)** — `cov/C04-entry-4.md` is absent at
  every stamp: nine drafts exist, culture-material has five (C01, C02, C03, C05,
  C06). With nine landed the census reads 210, not the claim's 211, and
  "10/10 new entries audited clean" (`claims.json:35`) cannot be reached. The
  drafts' absence is a mid-round state, not a coverage failure; recorded so the
  close does not read a 9-draft tree as claim C satisfied.

## 8. Landed-bytes reviews

### 8.1 Entry 6 — `cov/C06-entry-6.md` → `culture-material/fire-fuel-light.md`

47669 bytes / 174 lines; block sha256 `481cf1c24734c1251879f3e2928fb9d470db7eae11a375982786602ed74c6558`;
the fragment states that digest outside the fence → **attested**.

- **frontmatter**: `topic` ✓ `couples` ✓ `sources` ✓ (block-valued) `source` ✓
  `verified-at` ✓ (dated 2026-10-19, scope-bearing, names the offline limit)
  `recheck` ✓ `gap` ✓; no `scope` → **3/4 under the claim's literal vector and under
  the house reading; 4/4 under `R35-4F-1`** (the `couples` leg satisfies scope).
- **gap**: real — I re-ran its own sweeps: sweep 1 → exactly the three incidental
  files it names; sweep 2 → exit 1, no matches; `ls corpus/knowledge/*/{fire,fuel,light}*`
  → no slug collision.
- **decision record**: §10, **DR-FF-01…07**.
- **sources**: 43 `path:line` refs across 24 pairs, **all in range**; 12 sampled
  lines carry the claimed content verbatim, including the two long-line claims
  (`architecture-settlement-lexicon.md:98` carries both `teramachi` and `firebreak`;
  `:124` carries `focus`/`foyer`/`hogar`); 0 unresolved of 24 backticked refs and 33
  `couples` targets; 39 inline marks (1 counted marker, R02-F7); 0 URLs.
- **duplication**: max 8-gram **0.0017** (`transport-mobility-lexicon.md`); topic
  Jaccard **0.1023** (`costume-semiotics.md`).
- **no-bleed (read)**: 7 triage hits, 2 unguarded-class, both ordinary English ("the
  Calendar Round **closed** by re-lighting every hearth"; "the **closed** lamp with
  a spout") → 0 real; §12 hands canon to lore-shokunin.
- **Verdict: pass on all eight checks.** C17 independently found entry 6 clean
  (`cov/C17-audit-sample.md:405-437`), agreeing on bytes, digest-matching byte count,
  field set, and zero defects.

### 8.2 Entry 7 — `cov/C07-entry-7.md` → `myth-symbol/eschatology-world-end-systems.md`

47399 bytes / 201 lines; block sha256 `e6bc159d23e2d9772f66e680c50ea11759bb0584190cd78032a93823251d7932`;
stated outside the fence → **attested**. (Under my pre-fix extractor this draft read
47342 bytes / `7065078a…`; the fence-stack scan reproduces the author's stated bytes
and digest — §3.2 defect 6.)

- **frontmatter**: as entry 6 — both `sources` and `source`, no `scope` → 3/4 literal
  / 3/4 house / 4/4 `R35-4F-1`.
- **gap**: over-determined by the partition's own record — verified three citations:
  `creation-myths-taxonomy.md:18` contains both "to be built" and "eschatology";
  `:110` item (5) reads "Set eschatology from the creation type — combat: final
  battle and renewal; ex nihilo: linear consummati…"; `:134` carries the eschatology
  field in the handoff metadata.
- **decision record**: §12 ✓; §10 calibration ✓; §13 canon boundary ✓.
- **sources**: 24 backticked refs, 0 unresolved; 20 `path:line` refs across 5 pairs,
  all in range; 15 raw marks (4 counted); 0 URLs.
- **duplication**: max 8-gram **0.0039**; topic Jaccard **0.1066**.
- **no-bleed (read)**: 9 triage hits, 4 unguarded-class, all non-bleed — "canon
  decisions are theirs per lane rules"; "**If** a receiving lane expects an
  eschatology to license a canon ending…" (a refusal conditional); "whenever a
  to-verify item above is closed"; "a term closed" (ordinary English).
- **Verdict: pass on all eight checks.**

### 8.3 Entry 8 — `cov/C08-entry-8.md` → `myth-symbol/sacred-kingship-mythic-charter.md`

62522 bytes / 205 lines; block sha256 `cbf79ff78940…`; **the fragment states no
digest**, so block attestation is unavailable for this draft (provenance note: a
post-statement edit could not be detected for it; the other four attest).

- **frontmatter**: `topic` ✓ `couples` ✓ `sources` ✓ (block) `source` ✓
  `verified-at` ✓ `recheck` ✓; no `scope`; no `- gap:` field — the gap is named by an
  inline "gap filled" clause (3 occurrences), which C12's tier 4 accepts
  (`cov/C12-audit-runbook.md:39`) → 3/4 both readings, 4/4 `R35-4F-1`.
- **gap**: real — the partition carries kingship as a by-product of other subjects
  and has no institution entry; no existing myth-symbol slug covers it.
- **decision record**: **ABSENT — R02-F6.**
- **sources**: 42 backticked refs, **0 unresolved**; 3 `path:line` refs, all in range
  (this draft anchors by file, not line); 61 raw marks (6 counted); 0 URLs.
- **duplication**: max 8-gram **0.0013**; topic Jaccard **0.0989**.
- **no-bleed (read)**: 5 triage hits, 2 unguarded-class, both non-bleed — "canon
  decisions are theirs per lane rules" (my guard list lacks "theirs": a guard-list
  gap in my leg, not an entry defect); "one culture's **closed** correlative system".
- **Verdict: pass on seven checks, one finding (R02-F6).**

### 8.4 Entry 9 — `cov/C09-entry-9.md` → `myth-symbol/death-afterlife-eschatology.md`

61411 bytes / 192 lines; block sha256 `47e665c6c8b2…`; stated outside the fence →
**attested**.

- **frontmatter**: `topic` ✓ `couples` ✓ `sources` ✓ (block) `source` ✓
  `verified-at` ✓ `recheck` ✓ `gap` ✓; no `scope` → 3/4 both readings / 4/4 `R35-4F-1`.
- **gap**: §1 "Scope — the gap this entry fills, and what it refuses"; the doctrine of
  the dead is absent from the partition (no existing slug covers survival typology,
  destination, judgment, or the living's obligations).
- **decision record**: §11 "Decision record — a worked death-doctrine for a
  disposable culture (non-canon)", **DR-DE-01…10**; §12 calibration bank; §13 canon
  boundary.
- **sources**: 19 backticked refs, **0 unresolved**; 25 `couples` targets, 0
  unresolved; **0 line-anchored citations** — this draft cites files, not
  `file:line` pairs, so the strongest spot-check surface (re-read the cited line) is
  unavailable; I verified instead that each cited file exists and that its title
  matches the claim it is used for (sampled: `architecture-settlement-lexicon`,
  `cosmology-cosmography`, `divination-omen-systems`, `cuisine-food-lexicon`).
  31 raw marks (2 counted); 0 URLs. **Recorded as a review limitation, not a defect.**
- **duplication**: max 8-gram **0.0047**; topic Jaccard **0.0933**.
- **no-bleed (read)**: 13 triage hits, 4 unguarded-class, all non-bleed — the "Ten
  Courts as canon" hits are the entry's *calibration table quoting the misframing it
  rejects*; "importing it as canon imports a government with it" is a warning; "it
  decides nothing about any world… canon recording and consistency verification" is
  the refusal statement.
- **Verdict: pass on eight checks, with the line-anchor limitation stated.**

### 8.5 Entry 10 — `cov/C10-entry-10.md` → `myth-symbol/binding-speech-complex.md`

74529 bytes / 307 lines; block sha256 `b377f28ae4c3…`; stated outside the fence →
**attested**.

- **frontmatter**: `topic` ✓ `couples` ✓ `sources` ✓ (block) `source` ✓
  `verified-at` ✓ `recheck` ✓ **`scope` ✓** `gap` ✓ → **4/4 under both readings** —
  the only draft of the five that meets the claim's literal vector.
- **gap**: §1 "The gap this entry fills — and the boundary it keeps"; oath/curse/
  blessing/name-power machinery is absent from the partition.
- **decision record**: §13 "Decision record — the rules this entry adopts",
  **DR-BS-1…12**; §12 calibration; §14 canon boundary.
- **sources**: 69 backticked refs, **0 unresolved** (including `../civilizations/*.md`
  forms resolved partition-relatively — spot-checked: `celts.md`, `rome.md` exist);
  40 `couples` targets, 0 unresolved; 0 line-anchored citations (same limitation as
  entry 9, stated); 28 raw marks / **22 counted** — the densest and most consistent
  inline-flag discipline of the five; 0 URLs.
- **duplication**: max 8-gram **0.0030**; topic Jaccard **0.1321**
  (`divination-omen-systems.md`) — the highest of the five and still an order of
  magnitude below any duplication concern.
- **no-bleed (read)**: 11 triage hits, 2 unguarded-class, both non-bleed — "canon
  decisions are theirs per lane rules"; "institutions from **closed** or restricted
  traditions" (ordinary English).
- **Verdict: pass on all eight checks.**

### 8.6 Verdict summary

| entry | bytes | block sha256 | gap | decision | refs unresolved | 4/4 literal | max 8-gram | verdict |
|---|---|---|---|---|---|---|---|---|
| 6 | 47669 | `481cf1c2…` | ✓ | ✓ (7 DR) | 0 | 3/4 | 0.0017 | pass |
| 7 | 47399 | `e6bc159d…` | ✓ | ✓ | 0 | 3/4 | 0.0039 | pass |
| 8 | 62522 | `cbf79ff7…` | ✓ | **✗** | 0 | 3/4 | 0.0013 | pass + R02-F6 |
| 9 | 61411 | `47e665c6…` | ✓ | ✓ (10 DR) | 0 | 3/4 | 0.0047 | pass |
| 10 | 74529 | `b377f28a…` | ✓ | ✓ (12 DR) | 0 | **4/4** | 0.0030 | pass |

Zero fabricated sources found in any of the five: every repo reference resolves, no
digest token is unattested, no URL is presented as fetched, and each entry's
`verified-at` states the offline limit that governs its external citations.

## 9. What this fragment does not establish

It does not establish that the five drafts are *correct* as scholarship — external
works were not fetched (no network in this seat), so author-year attributions are
checked for attestation and internal consistency only. It does not verify entries
1-5, the renderer hardening, or the adjacency slices. It makes no admission,
promotion, canon, clearance or closure statement about any entry, round or partition.
And it does not clear entry 8: R02-F6 stands until the entry is repaired or the round
pins a reading that accepts its §10 protocol.

## Instrument (embedded bytes; runnable from `.scratch/`)

The instrument below is the review's own reader, embedded so it stays durable
past `.scratch/` cleanup (gitignored). It writes nothing and opens the tree
read-only. The fence is four backticks because the script carries a ```markdown
fixture inside its `--selftest`. `--selftest` is **10/10** on the embedded copy
(verified by extracting this block and running it); block sha256:
`f25247bda6d44523b076bf503b763b579eb200e25e3a75f7aee4227eb6c03876`.

````python
#!/usr/bin/env python3
"""R02 (round 35) — adversarial entry reviewer for coverage drafts 6-10 (read-only).

Input is either a seat fragment carrying the full entry bytes as one fenced
```markdown block (`--draft`) or an already-landed corpus entry (`--entry`).
Every leg is measured against the live tree; nothing is written anywhere.

Legs:
  extract   fenced-block extraction, digest, declared target slug/partition
  front     frontmatter presence/uniqueness/non-empty/no-placeholder, both
            readings of the claim-C 4/4 bar (`sources` house field vs literal
            `source`), house trio topic/sources/couples
  gap       gap-named (field, inline clause, or heading) — r10/r19 regexes
  decision  `## ... decision record` heading with content; DR-id census
  canon     bleed sweep: promotion/canon/clearance/closure language, each hit
            classified negation-guarded vs unguarded
  sources   backticked repo-path resolution (brace-expanded), URL census,
            runnable-command census, `verified-at` date/scope
  dup       slug collision, topic-token Jaccard vs partition, 8-gram body
            shingle Jaccard vs all 201 entries
Usage:
  python3 .scratch/r02-review.py --draft reports/round-35/cov/C06-entry-6.md ...
  python3 .scratch/r02-review.py --entry corpus/knowledge/myth-symbol/trickster.md ...
  python3 .scratch/r02-review.py --json ...
  python3 .scratch/r02-review.py --selftest
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
KNOW = LANE / "corpus" / "knowledge"
PARTS = ["linguistics", "myth-symbol", "culture-material", "synthesis",
         "verification", "civilizations"]

FENCE_RE = re.compile(r"(?ms)^(`{3,})[a-zA-Z]*\n(.*?)^\1[ \t]*$")
HEAD_RE = re.compile(r"^- ([a-z][a-z0-9-]*):(.*)$", re.M)
FIELD_RE = re.compile(r"(?m)^- ([a-z][a-z0-9-]*):[ \t]*(.*)$")
GAP_RE = re.compile(r"(?i)(?:^|[\s.;\u2014\u2013|-])gap(?:[\s-]+(?:filled|"
                    r"addressed|served))?\s*:\s*(\S[^\n]{0,300})")
GAP_ALT_RE = re.compile(r"(residual gap|gap filled|the gap this entry fills|"
                        r"known gaps|missing from|no entry (?:covers|states)|"
                        r"not covered by)", re.I)
DECISION_RE = re.compile(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*$")
DECISION_LOOSE_RE = re.compile(r"(decision record|decision table|DR-[A-Z]{2}-\d|"
                               r"decisions? taken)", re.I)
DRID_RE = re.compile(r"\bDR-[A-Z]{2}-\d+")
URL_RE = re.compile(r"https?://[^\s`)\]}>,\"']+")
CMD_RE = re.compile(r"(?m)^\s*(?:\$ )?((?:python3?|bash|sh|git|grep|find|ls|wc|sha256sum)\b[^\n]*)")
PLACEHOLDER_RE = re.compile(r"(?i)\b(tbd|todo|fixme|xxx|placeholder|<[a-z-]+>|\?\?\?)\b")
TOPIC_RE = re.compile(r"(?m)^- topic:(.*?)(?=\n- \w)", re.S)
BLEED = {"promotion": re.compile(r"\bpromot(?:e|ed|ion|ing)\b", re.I),
         "canon": re.compile(r"\bcanon\b", re.I),
         "clearance": re.compile(r"\bclear(?:ance|ed)\b", re.I),
         "closure": re.compile(r"\bclos(?:ure|ed)\b", re.I)}
NEG_GUARD_RE = re.compile(r"(?i)(\b(no|not|never|without|cannot|isn't|is not|outside|beyond|"
                          r"owns|belongs|handed|handoff|lore-shokunin|boundary|hygiene|routed|"
                          r"negat|forbid|excluded|reserved)\b|non-?canon|non-canon)")


def brace_expand(s):
    m = re.search(r"\{([^{}]*)\}", s)
    if not m:
        return [s]
    out = []
    for part in m.group(1).split(","):
        out.extend(brace_expand(s[:m.start()] + part + s[m.end():]))
    return out


def head_block(text):
    parts = re.split(r"(?m)^## ", text, maxsplit=1)
    return parts[0]


def topic_of(text):
    m = TOPIC_RE.search(text)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def toks(s):
    return set(re.findall(r"[a-z0-9]+", (s or "").lower()))


def shingles(text, n=8):
    w = re.findall(r"[a-z0-9]+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def jacc(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0


def extract_fence(path):
    """Fence-stack scan: pairs fences by backtick length so an entry carrying
    nested ```-blocks is extracted whole (a non-greedy regex truncates it)."""
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    stack = []          # (fence_len, content_start_line_index)
    blocks = []
    for i, ln in enumerate(lines):
        m = re.match(r"^(`{3,})[a-zA-Z]*[ \t]*$", ln.rstrip("\n"))
        if not m:
            continue
        L = len(m.group(1))
        if stack and stack[-1][0] == L:
            start = stack.pop()[1]
            blocks.append("".join(lines[start:i]))
        elif not stack or L > stack[-1][0]:
            stack.append((L, i + 1))
        # a shorter fence inside a longer open fence is content, not a closer
    md = [b for b in blocks if b.lstrip().startswith(("#", "- "))]
    md.sort(key=len, reverse=True)
    return text, blocks, (md[0] if md else None)


def repo_refs(text):
    """Backticked tokens that look like repo paths."""
    out = set()
    for tok in re.findall(r"`([^`\n]{3,120})`", text):
        for cand in brace_expand(tok.strip()):
            c = cand.strip().rstrip(".,;:)")
            if re.match(r"^[A-Za-z0-9_./-]+\.(md|py|json|yml|yaml|tsv|txt|log)$", c):
                out.add(c)
    return sorted(out)


_BYNAME = None


def byname():
    global _BYNAME
    if _BYNAME is None:
        _BYNAME = {}
        for f in KNOW.rglob("*.md"):
            _BYNAME.setdefault(f.name, []).append(f.relative_to(LANE))
    return _BYNAME


def resolve(ref, partition=None):
    """Resolve a cited path: exact (lane-root, corpus-root, partition-relative),
    else unique basename anywhere in corpus/knowledge (r10 review convention)."""
    cands = [LANE / ref, KNOW / ref]
    if partition:
        cands.append(KNOW / partition / ref)
    for c in cands:
        try:
            if c.exists():
                return "path"
        except OSError:
            pass
    if "/" not in ref:
        hits = byname().get(ref, [])
        if len(hits) == 1:
            return "basename"
        if len(hits) > 1:
            return "ambiguous"
    return "unresolved"


def couples_refs(text):
    m = re.search(r"(?m)^- couples:(.*?)(?=\n- \w)", text, re.S)
    if not m:
        return []
    out = []
    for tok in re.findall(r"[A-Za-z0-9_./{},\-]+\.md", m.group(1)):
        out.extend(brace_expand(tok))
    return sorted(set(out))


_DIGESTS = None


def known_digests():
    """Every hex token >=16 chars appearing in reports/**/*.json or *.md plus every
    corpus file's own sha256 — the set a non-fabricated digest must hit."""
    global _DIGESTS
    if _DIGESTS is None:
        _DIGESTS = set()
        for f in LANE.joinpath("reports").rglob("*"):
            if f.suffix in (".json", ".md", ".txt", ".log") and f.is_file():
                try:
                    _DIGESTS |= set(re.findall(r"\b[0-9a-f]{16,64}\b",
                                               f.read_text(errors="ignore")))
                except OSError:
                    pass
        for f in KNOW.rglob("*.md"):
            _DIGESTS.add(hashlib.sha256(f.read_bytes()).hexdigest())
    return _DIGESTS


def check(text, label, partition=None, corpus_all=None, self_path=None, target_hint=None):
    r = {"label": label, "findings": [], "notes": []}
    head = head_block(text)
    r["title"] = text.splitlines()[0] if text else ""
    r["bytes"] = len(text.encode())
    r["sha256"] = hashlib.sha256(text.encode()).hexdigest()
    r["lines"] = text.count("\n") + 1

    # --- frontmatter
    fields = {}
    for m in FIELD_RE.finditer(head):
        val = m.group(2).strip()
        if not val:
            # block-valued field: value carried on following indented lines
            tail = head[m.end():]
            nxt = tail.split("\n")[1] if "\n" in tail else ""
            if nxt.startswith("  ") and nxt.strip():
                val = "(block-valued: " + nxt.strip()[:40] + " ...)"
        fields.setdefault(m.group(1), []).append(val)
    r["fields"] = {k: len(v) for k, v in sorted(fields.items())}
    for k, v in fields.items():
        if len(v) > 1:
            r["findings"].append(f"front: duplicate field `{k}` x{len(v)}")
        if not v[0]:
            r["findings"].append(f"front: empty field `{k}`")
        if PLACEHOLDER_RE.search(v[0]):
            r["findings"].append(f"front: placeholder value in `{k}`")
    house = ["topic", "sources", "couples"]
    for k in house:
        if k not in fields:
            r["findings"].append(f"front: house field `{k}` missing")
    claim_c = {"source_house(sources)": "sources", "verified-at": "verified-at",
               "recheck": "recheck", "scope": "scope"}
    bar_house = sum(1 for k in ("sources", "verified-at", "recheck", "scope") if k in fields)
    bar_literal = sum(1 for k in ("source", "verified-at", "recheck", "scope") if k in fields)
    r["bar_house_4of4"] = f"{bar_house}/4"
    r["bar_literal_source_4of4"] = f"{bar_literal}/4"
    if "scope" not in fields:
        r["findings"].append("front: `scope` absent (claim C names source/verified-at/recheck/scope)")
    if "source" not in fields and "sources" not in fields:
        r["findings"].append("front: neither `source` nor `sources` present")

    # --- gap
    g = GAP_RE.search(text)
    r["gap"] = bool(g or GAP_ALT_RE.search(text))
    r["gap_evidence"] = (g.group(0)[:120] if g else
                         (GAP_ALT_RE.search(text).group(0) if GAP_ALT_RE.search(text) else None))
    if not r["gap"]:
        r["findings"].append("gap: no gap statement found")

    # --- decision record
    dm = DECISION_RE.search(text)
    r["decision_record"] = bool(dm)
    r["decision_ids"] = sorted(set(DRID_RE.findall(text)))
    if dm:
        tail = text[dm.end():].strip().splitlines()
        r["decision_first_line"] = (tail[0][:100] if tail and tail[0].strip() else "")
        if not r["decision_first_line"]:
            r["findings"].append("decision: heading with no content")
    else:
        if DECISION_LOOSE_RE.search(text):
            r["findings"].append("decision: loose mention only, no `## ... decision record` heading")
        else:
            r["findings"].append("decision: no decision record")

    # --- canon / bleed
    bleed_hits = []
    for name, rx in BLEED.items():
        for m in rx.finditer(text):
            ctx = text[max(0, m.start() - 60):m.end() + 40].replace("\n", " ")
            bleed_hits.append({"term": name, "guarded": bool(NEG_GUARD_RE.search(ctx)),
                               "ctx": ctx.strip()[:150]})
    r["bleed_hits"] = len(bleed_hits)
    r["bleed_unguarded"] = [h for h in bleed_hits if not h["guarded"]]

    # --- sources
    refs = repo_refs(text)
    crefs = couples_refs(text)
    res = {x: resolve(x, partition) for x in refs}
    cres = {x: resolve(x, partition) for x in crefs}
    r["repo_refs"] = len(refs)
    r["repo_refs_unresolved"] = [x for x, v in res.items() if v == "unresolved"]
    r["repo_refs_ambiguous"] = [x for x, v in res.items() if v == "ambiguous"]
    r["couples_refs"] = len(crefs)
    r["couples_unresolved"] = [x for x, v in cres.items() if v == "unresolved"]
    r["couples_ambiguous"] = [x for x, v in cres.items() if v == "ambiguous"]
    if r["repo_refs_unresolved"]:
        r["findings"].append(f"sources: {len(r['repo_refs_unresolved'])} unresolved repo ref(s)")
    if r["couples_unresolved"]:
        r["findings"].append(f"couples: {len(r['couples_unresolved'])} unresolved target(s)")
    if r["couples_refs"] == 0:
        r["findings"].append("couples: no resolvable couples targets listed")
    r["urls"] = sorted(set(URL_RE.findall(text)))
    r["commands"] = sorted(set(m.group(1).strip() for m in CMD_RE.finditer(text)))
    va = fields.get("verified-at", [""])[0]
    r["verified_at"] = va[:160]
    if not re.search(r"\b20\d\d-\d\d-\d\d\b", va):
        r["findings"].append("sources: `verified-at` carries no ISO date")
    if len(va) < 40:
        r["findings"].append("sources: `verified-at` states no inspected scope")

    # --- fabrication hunt (offline: structural, not bibliographic)
    digests = sorted(set(re.findall(r"\b[0-9a-f]{16,64}\b", text)))
    tree_digests = known_digests()
    r["digests"] = len(digests)
    r["digests_unattested"] = [d for d in digests if d not in tree_digests]
    if r["digests_unattested"]:
        r["findings"].append(f"fabrication: {len(r['digests_unattested'])} digest(s) match no live file/receipt")
    ay = sorted(set(re.findall(r"\b([A-Z][A-Za-z'\u2019-]{2,})\s*\((\d{4})\)", text)))
    corpus_names = set()
    for pth in KNOW.rglob("*.md"):
        corpus_names |= set(re.findall(r"\b([A-Z][A-Za-z'\u2019-]{2,})\b", pth.read_text(errors="ignore")))
    r["author_year_pairs"] = len(ay)
    r["author_year_unattested_in_corpus"] = [f"{a} ({y})" for a, y in ay if a not in corpus_names]
    r["urls_without_access_note"] = [u for u in r["urls"]
                                     if not re.search(r"(?i)(accessed|fetched|retrieved|checked)", text[max(0, text.find(u) - 200):text.find(u) + 200])]

    # --- duplication
    r["slug"] = None
    r["dup_max_shingle"] = None
    if corpus_all:
        if self_path:
            r["slug"] = Path(self_path).name
        else:
            parts = re.findall(r"corpus/knowledge/([a-z-]+)/([a-z0-9-]+\.md)",
                               (target_hint or "") + "\n" + text)
            r["declared_targets"] = [f"{p}/{s}" for p, s in parts]
            # the draft's own target is the declared path that does NOT exist yet;
            # references to existing files are couplings, not targets
            fresh = list(dict.fromkeys((p, s) for p, s in parts if not (KNOW / p / s).exists()))
            r["targets_absent_from_tree"] = [f"{p}/{s}" for p, s in fresh]
            if len(fresh) == 1:
                r["slug"], r["target_partition"] = fresh[0][1], fresh[0][0]
            elif len(fresh) > 1:
                r["slug"] = fresh[0][1]
                r["findings"].append(f"dup: {len(fresh)} declared targets absent from tree (ambiguous): {r['targets_absent_from_tree']}")
            else:
                r["findings"].append("dup: every declared corpus path already exists (no fresh target)")
        body = re.sub(r"(?m)^- sources:.*$", "", text)
        sh = shingles(body)
        best = (0.0, None)
        for p, txt, tp in corpus_all:
            if self_path and str(p) == str(self_path):
                continue
            j = jacc(sh, tp)
            if j > best[0]:
                best = (j, p)
        r["dup_max_shingle"] = {"jaccard": round(best[0], 4), "path": str(best[1])}
        if partition:
            tp = [(p, txt2) for p, txt2, _ in corpus_all
                  if p.parts[-2] == partition and not (self_path and str(p) == str(self_path))]
            tj = max(((jacc(toks(topic_of(text)), toks(topic_of(txt2))), str(p)) for p, txt2 in tp),
                     default=(0.0, None))
            r["dup_max_topic_jaccard_partition"] = {"jaccard": round(tj[0], 4), "path": tj[1]}
        if best[0] > 0.05:
            r["findings"].append(f"dup: 8-gram overlap {best[0]:.3f} with {best[1]}")
    return r


def load_corpus():
    out = []
    for f in sorted(KNOW.rglob("*.md")):
        t = f.read_text(encoding="utf-8")
        out.append((f.relative_to(LANE), t, shingles(t)))
    return out


def selftest():
    checks = []
    fixture = """- Seat: X | executor | claim C | date 2026-10-19 | baseline 4a7aede

Target: `corpus/knowledge/culture-material/loom-forensics.md`

```markdown
# Loom Forensics — Cloth Signatures

- topic: how a loom leaves signatures in cloth
- sources: Barber (1991) *Prehistoric Textiles*; `corpus/knowledge/culture-material/textile-technology.md`; `corpus/knowledge/culture-material/ghost-file.md`
- couples: myth-symbol/color-symbolism.md
- verified-at: 2026-10-19 — read the loom table and re-ran the gate
- recheck: before fixing a loom date
- scope: material substrate of dress only

## 1. The gap this entry fills
## 2. Decision record
- D1: chose the forensic reading over the typological one.
```
"""
    r = check(fixture.split("```markdown\n", 1)[1].rsplit("```", 1)[0], "selftest-good",
              partition="culture-material")
    checks.append(("unresolved repo ref caught", "corpus/knowledge/culture-material/ghost-file.md" in r["repo_refs_unresolved"]))
    checks.append(("scope present -> not flagged", not any("`scope` absent" in f for f in r["findings"])))
    checks.append(("house bar 4/4", r["bar_house_4of4"] == "4/4"))
    checks.append(("literal-source bar 3/4", r["bar_literal_source_4of4"] == "3/4"))
    checks.append(("gap + decision found", r["gap"] and r["decision_record"]))
    bad = fixture.replace("- scope: material substrate of dress only\n", "").replace(
        "## 2. Decision record", "## 2. Notes")
    rb = check(bad.split("```markdown\n", 1)[1].rsplit("```", 1)[0], "selftest-bad",
               partition="culture-material")
    checks.append(("missing scope flagged", any("`scope` absent" in f for f in rb["findings"])))
    checks.append(("missing decision flagged", any("no decision record" in f for f in rb["findings"])))
    pl = fixture.replace("- recheck: before fixing a loom date", "- recheck: TBD")
    rp = check(pl.split("```markdown\n", 1)[1].rsplit("```", 1)[0], "selftest-placeholder")
    checks.append(("placeholder flagged", any("placeholder" in f for f in rp["findings"])))
    bleed = fixture.replace("- D1: chose the forensic reading over the typological one.\n",
                            "- D1: chose the forensic reading over the typological one.\nThis entry is approved for canon promotion.\n")
    rbl = check(bleed.split("```markdown\n", 1)[1].rsplit("```", 1)[0], "selftest-bleed")
    checks.append(("unguarded bleed flagged", len(rbl["bleed_unguarded"]) >= 1))
    guarded = fixture.replace("- D1: chose the forensic reading over the typological one.\n",
                              "- D1: chose the forensic reading over the typological one.\nNo canon decision is taken here; promotion belongs to lore-shokunin.\n")
    rg = check(guarded.split("```markdown\n", 1)[1].rsplit("```", 1)[0], "selftest-guarded")
    checks.append(("guarded bleed not flagged", len(rg["bleed_unguarded"]) == 0))
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    print(f"selftest: {sum(1 for _, ok in checks if ok)}/{len(checks)} checks passed")
    return 0 if all(ok for _, ok in checks) else 1


def digest_attest(fragment_path, block):
    """If the fragment states a 64-hex digest, it must equal the extracted block's
    sha256 (a stated-but-wrong digest is a tamper/no-fabrication finding)."""
    frag = Path(fragment_path).read_text(encoding="utf-8")
    stated = set(re.findall(r"\b[0-9a-f]{64}\b", frag))
    computed = hashlib.sha256(block.encode()).hexdigest()
    frag_digest = hashlib.sha256(frag.encode()).hexdigest()
    out = {"block_sha256": computed, "fragment_sha256": frag_digest,
           "stated_64hex": sorted(stated), "block_digest_stated": computed in stated,
           "fragment_digest_stated": frag_digest in stated}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", nargs="*", default=[])
    ap.add_argument("--entry", nargs="*", default=[])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    corpus = load_corpus()
    results = []
    for p in a.draft:
        frag, blocks, md = extract_fence(p)
        rec = {"fragment": p, "fenced_blocks": len(blocks),
               "markdown_block_found": md is not None}
        if md is None:
            rec["findings"] = ["extract: no markdown fenced block in fragment"]
            results.append(rec)
            continue
        part = re.search(r"corpus/knowledge/([a-z-]+)/", md)
        rec.update(check(md, p, partition=(part.group(1) if part else None), corpus_all=corpus,
                         target_hint=frag))
        att = digest_attest(p, md)
        rec["digest_attest"] = att
        if att["stated_64hex"] and not (att["block_digest_stated"] or att["fragment_digest_stated"]):
            rec["findings"].append(
                "fabrication: fragment states 64-hex digest(s) matching neither block nor fragment")
        results.append(rec)
    for p in a.entry:
        t = Path(p).read_text(encoding="utf-8")
        results.append(check(t, p, partition=Path(p).parent.name, corpus_all=corpus, self_path=p))
    if a.json:
        print(json.dumps(results, indent=1))
    else:
        for r in results:
            if "label" not in r:
                print(f"== {r.get('fragment','?')} :: {r.get('findings')}")
                continue
            print(f"== {r['label']}")
            print(f"   title={r.get('title','')[:70]!r} bytes={r.get('bytes')} sha={str(r.get('sha256'))[:12]} lines={r.get('lines')}")
            if "fields" in r:
                print(f"   fields={r['fields']} bar_house={r['bar_house_4of4']} bar_literal_source={r['bar_literal_source_4of4']}")
                print(f"   gap={r.get('gap')} decision={r.get('decision_record')} dr_ids={r.get('decision_ids')}")
                print(f"   refs={r.get('repo_refs')} unresolved={r.get('repo_refs_unresolved')}")
                print(f"   urls={len(r.get('urls',[]))} commands={len(r.get('commands',[]))}")
                print(f"   bleed_hits={r.get('bleed_hits')} unguarded={len(r.get('bleed_unguarded',[]))}")
                print(f"   dup={r.get('dup_max_shingle')} topic_jacc={r.get('dup_max_topic_jaccard_partition')}")
            for f in r.get("findings", []):
                print(f"   FINDING {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
````

## Owed

- **Landed review of entries 6-10: done** (§8) — no longer owed.
- `reports/round-35/cov/C04-entry-4.md` — absent; entry 4's draft (R02-F8). Without
  it the claim's +6 culture-material leg and its 10/10 and 211 thresholds are
  unreachable. Owner: integrating parent.
- Post-integration re-runs owed to the integrator (the §2 baselines and §2.4
  predictions are pre-registered for exactly this): (a) the three partition digests
  (§2.2) and the per-file capture — no existing file's row may change; (b) the
  inventory after-state — it must equal §2.4's prediction for whichever drafts land;
  (c) the README sweep — 211 rows/files, headers 23/24, totals 211, footer
  `21/23/24/29/20/94`, both sections ASCII-sorted; (d) R02-F6's repair or its
  round-level pin.
- Cross-reference owed to R01: `reports/round-35/review/R01-c-review.md` (method diff
  against §3.1 of this fragment).

## Citations

Paths and commands this fragment relies on (all read at HEAD `4a7aede`, 2026-10-19):

- `reports/round-35/targets.json:5-13` (shared_rules), `:330` (R01 seat), `:331-334` (R02 seat), C06-C10 seats
- `reports/round-35/claims.json:8-9`, `:22-35` (claim C: `:24` vector, `:26-27` before, `:29` after_required, `:31-33` commands, `:35` thresholds)
- `REGIMEN.md` (per-round contract; no-force-pass rule); `corpus/QUALITY.md:1-23`
- `reports/round-10/coverage/review-C06.md:3,11,19-22`; `reports/round-10/coverage/review-C10.md:19-30`
- `reports/round-10/run-validation.py:81-82,349-377` (filed legs — cited, never executed)
- `reports/round-19/audit/entry-audit.py:25-31,33`; `reports/round-19/audit/x26-spotcheck-entries.md` §3
- `reports/round-28/readme/sweep.py:60-61,74-78,140,202`
- `corpus/README.md:1-15,147,149-167,169,171-188,469,471-473,493`
- `corpus/knowledge/verification/label-channel-routing-verification.md:14`
- `corpus/knowledge/myth-symbol/creation-myths-taxonomy.md:18,110,134`
- `reports/round-34/handoff/declared-in-r7/expected.json:125`
- `reports/round-35/scout/K02-entry-audit-method.md:12-14,122-160,173`
- `reports/round-35/cov/C11-readme-delta.md:9-17,90-190`; `cov/C12-audit-runbook.md:34,37,39,41,61`; `cov/C14-audit-6-10.md:26`; `cov/C15-receipt.md:31-35,104-110`; `cov/C16-scribe.md:126-133`; `cov/C17-audit-sample.md:14-16,405-437`; `scribe/S01-c-receipt.md:36-38,73-80,126-129`
- Draft fragments reviewed: `cov/C06-entry-6.md`, `cov/C07-entry-7.md`, `cov/C08-entry-8.md`, `cov/C09-entry-9.md`, `cov/C10-entry-10.md` (byte counts, block digests and per-check readings in §8)
- Commands run (outputs quoted in §2, §3, §8): the six-partition `ls | wc -l` loop;
  `find corpus/knowledge -name '*.md' | wc -l`; `sha256sum corpus/knowledge/{culture-material,myth-symbol}/*.md | sha256sum`;
  `sha256sum corpus/README.md`; `wc -c -l corpus/README.md`;
  `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  (and `--root .scratch/r02-predict`, `--root .scratch/r02-predict9` for the predictions);
  `grep -c '^- \`[A-Za-z0-9._-]*\.md\`' corpus/README.md`; the drafts' own gap sweeps
  (`grep -ril -e hearth …`, `ls corpus/knowledge/*/{fire,fuel,light}*`);
  `python3 -B .scratch/r02-review.py --selftest|--draft|--entry`
