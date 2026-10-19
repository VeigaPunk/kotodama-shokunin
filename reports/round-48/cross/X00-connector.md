# X00 — cross-claim connector (round 48, loop 2, position 2)

- Seat: `X00` | role: connector | claim: **cross** (C + Ca) | date 2026-10-19
- Baseline: `a01405d` (`git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af`), equal to
  `reports/round-48/claims.json` `baseline_commit`; `git status --porcelain` → only the pre-existing
  untracked `reports/round-46/review/` and this round's `reports/round-48/`.
- Out path: `reports/round-48/cross/X00-connector.md` (the only repo write this seat makes).
- Mission (`reports/round-48/targets.json:17`): how C's length discipline plus audits prevent the
  r47 over-build class, and how Ca records that class durably.
- Method: read-only commands at `a01405d`; no filed byte edited, no corpus staging, no
  `run-validation.py` executed, no git/network mutation, no tool or corpus byte written.

**One-line result.** The r47 class has two independent causes — **no shared length budget** across
independently authored fragments, and **audits run on fragments/pre-fix bytes** — and C's claim
attacks both only if the integrator measures the **assembled** entry and re-runs the audits on it.
Length alone catches none of B1–B9. Ca's durable half is currently **empty**: the r47 queue
successor (`sha256 9508b6aa…ce58`) has three defect rows and **no over-build row** (grep for
`over.build|790|739|R03|B1` → exit 1), so the class is undispositioned at `a01405d`. The README
fix and C's rev-2.5 rewrite share one file and their line anchors collide.

---

## 0. Axes named (godspeed)

| axis | what this seat can move | move taken here |
|---|---|---|
| A1 defect-class closure | map each r47 B1–B9 to the r48 control that must prove it gone | §3 matrix, one row per defect |
| A2 length as a structural constraint | show why the 250-line budget removes the *volume* cause but not the *factual* causes | §4 arithmetic + the necessary/not-sufficient argument |
| A3 durable disposition | specify the exact successor row and its non-claim of "fixed" | §6 fenced row + class discipline |
| A4 cross-claim write order | name the shared README surface and the anchor shift | §8 ordering and sha invalidation |

---

## 1. State measured at `a01405d`

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 -c "line counts of corpus/knowledge/culture-material/*.md"
n 25  min 103  median 149  max 221  mean 150.2
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
```

Live README anchors used by both claims (verified by `awk`/`sed -n` at this HEAD):

| anchor | live bytes |
|---|---|
| `corpus/README.md:3` | second, redundant H1 (the live defect) |
| `corpus/README.md:11` | rev-2.4 prose vector `25/23/25/29/24/94 → 25/23/26/25/24/94` — **sums 217** |
| `corpus/README.md:234` | `## culture-material/ (25)` |
| `corpus/README.md:240` | `calendar-festival-systems.md` row |
| `corpus/README.md:241` | `costume-semiotics.md` row (cartography sorts between them) |
| `corpus/README.md:544` | `Total knowledge entries: 223.` |
| `corpus/README.md:548` | `(total 223 files; directory totals 25/26/25/29/24/94).` |

Arithmetic, recomputed:

```
0.2 mm × 50,000 = 10,000 mm = 10 m;  200 m / 10 m = 20        # r47 B1's correct ratio
25+23+26+25+24+94 = 217    # rev-2.4 prose vector (wrong)
25+26+25+29+24+94 = 223    # live footer vector (correct)
25+26+26+29+24+94 = 224    # post-landing vector
739/149 = 4.96×   739/221 = 3.34×   790/221 = 3.57×   250/221 = 1.13×   250/149 = 1.68×
```

The `739` and `790` figures are both r47's: `reports/round-47/review/R03-c-content.md:26,96` measures
**739 body lines** of the assembled fence; `reports/round-47/validation.json:9` reports **790 lines**
for the assembled entry. The 51-line gap is a measurement-frame difference (body lines vs file
total), not a contradiction; either figure is 3.3–3.6× the live max. Do not quietly pick one without
saying which.

---

## 2. What the r47 over-build class actually is

The class is not "a long entry." It is the conjunction of two process failures, visible in
`reports/round-47/review/R03-c-content.md`:

1. **No composing budget.** Four fragments were authored independently (C01 358 lines, C02 503, C03
   287, C04 301 — `reports/round-47/review/R03-c-content.md:14-19`), each locally reasonable, and the assembled body reached 739 lines
   against a 103–221 partition (`reports/round-47/review/R03-c-content.md:96`). Duplicate rules survived because no seat owned the whole:
   `C01:164` vs `C02:109`, `C01:204` vs `C02:110`, and C03 §10 restating C01 §3's mechanisms
   (`reports/round-47/review/R03-c-content.md:94-96`).
2. **Audits certified fragments, then were not re-run.** R03's closing instruction is explicit:
   "C14 is FAIL on F-1/F-2, C06 is PASS-with-corrections, C07 is pre-bytes `could-not-evaluate` …
   Re-run the audits on the corrected bytes and file the results, not the pre-fix verdicts"
   (`reports/round-47/review/R03-c-content.md:248`). The assembled bytes never had a clean chain.

The nine blocking content defects are symptoms of the second failure, not of length. A 200-line
draft can still write `200 m` as "ten times" 10 m. So C's `after_required` has **two** legs —
`<=~250 lines` and `audits clean` — and the connector's job is to show neither leg substitutes for
the other.

---

## 3. Defect → control matrix (the load-bearing deliverable)

Each r47 blocking defect, its live evidence, the r48 seat that must independently re-check it, and
the acceptance fact that closes it. Seat ids and out paths are from `reports/round-48/targets.json`.

| # | r47 defect (evidence) | Correct fact, independently re-measured here | r48 control | Closing check |
|---|---|---|---|---|
| B1 | false-precision arithmetic (`reports/round-47/review/R03-c-content.md:188`) | `0.2 mm × 50,000 = 10 m`; `200/10 = 20`, not 10 | `C03` `cov/C03-arithmetic.md` | every scale/ratio recomputed; no "ten times" survives |
| B2 | unreproducible gap count (`reports/round-47/review/R03-c-content.md:189`) | `grep -rni 'cartograph' corpus/knowledge/` → **2 lines, 2 files**: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102`, `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58`; `:71` contains **0** `cartograph` tokens | `C03` (number) + `C06` `cov/C06-collision.md` (reproduction) | the gap line states 2/2 and cites the right lines; the sweep command reproduces |
| B3 | false source-accusation (`reports/round-47/review/R03-c-content.md:190`) | `corpus/knowledge/linguistics/naming-systems.md:70` **does** contain "a map is an archive of coups" (verified verbatim) | `C04` `cov/C04-citations.md` | no proposed "correction" to a correct quote; quotes checked before accusations |
| B4 | mis-anchored workshop ladder (`reports/round-47/review/R03-c-content.md:191`) | `corpus/knowledge/culture-material/craft-artisan-lexicon.md:44` is the Steel (Japan) row; the ladder is `:54` header, `:56-63` systems, `:65` design rule | `C04` (+ `C08` shelf) | anchor reads `:54-65`, not `:44` |
| B5 | wrong form-typology cross-refs (`reports/round-47/review/R03-c-content.md:192`) | typology is C01 §4.1; §2 is the five-condition test | `C04` (anchors) + `C05` `cov/C05-length-contract.md` (section numbering) | every `§n` resolves to the named section |
| B6 | wrong provenance/charter section (`reports/round-47/review/R03-c-content.md:193`) | provenance/charter is §8, the fossil is §9 | same as B5 | handoff note says §8 |
| B7 | worked example states three update rules (`reports/round-47/review/R03-c-content.md:194`) | one rule must be stated once; the three quoted lines are incompatible | `C14` `cov/C14-example.md` + `M01` `cov/M01-example.md` | `grep` the rule; one statement, three consequences consistent with it |
| B8 | over-claim vs cosmography (`reports/round-47/review/R03-c-content.md:195`) | `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` says cosmography is "how the world is drawn (maps)"; `:71`/`:102` disclaim survey maps | `C07` `cov/C07-boundary.md` + `A02` `adj/A02-ownership.md` | the boundary sentence cites `:27` and `:71`/`:102` together |
| B9 | "per form" table covers 5 of 8 (`reports/round-47/review/R03-c-content.md:196`) | eight forms in C01 §4.1; five rows in the build table | `C05` (contract completeness) | table is complete or retitled "five common forms" |
| V | volume 739/790 vs 103–221 (`reports/round-47/review/R03-c-content.md:96`; `reports/round-47/validation.json:9`) | 3.34–3.57× the live max; 4.96× the median | `C05` (length) + `X03` `cross/X03-overbuild.md` + `C17` `cov/C17-structure.md` | `wc -l` on the **assembled** entry `<=~250` |

Two seats are cross-cutting rather than defect-specific: `C12` `cov/C12-content.md` judges whether
the entry is real domain method (the r47 draft passed substance, `reports/round-47/review/R03-c-content.md:98`), and `V01`/`F01`
`cov/V01-post-landing.md` / `cross/F01-final-census.md` prove the landed tree. Neither can substitute
for B1–B9 checks.

**The rule this matrix encodes:** a defect is closed by a *command output on the composed bytes*,
not by a sibling's PASS verdict. r47 already had C05/C06/C07/C08 verdicts; it still shipped B1–B9
because those verdicts were fragment-scoped or pre-fix (`reports/round-47/review/R03-c-content.md:248`).

---

## 4. Why the 250-line discipline is necessary — and not sufficient

**Necessary.** A 250-line budget is `1.13×` the live max (221) and `1.68×` the median (149): inside
the house band with a little room, not a new band. At that size the r47 duplication cannot be paid
for. The two duplicate bullet pairs (`reports/round-47/review/R03-c-content.md:94`) and C03 §10's
restatement of C01 §3 (`reports/round-47/review/R03-c-content.md:95`) are redundancy a 250-line
budget cannot pay for; a drafter who must fit the budget is forced to choose one owner per rule and
point at it. The budget also makes the composed audit tractable: one
reviewer can hold 250 lines in view, which is exactly what the 739-line four-fragment assembly
defeated (C14 missed F-1 across three lines in one section, `reports/round-47/review/R03-c-content.md:194`).

**Not sufficient.** Length checks are blind to truth. B1 (wrong ratio), B3 (false accusation), B4
(mis-anchor), B6 (wrong section) and B8 (competing ownership) are all compatible with a 100-line
entry. The r48 claim's own wording keeps both legs: "correct arithmetic, no false
source-accusations, correctly-anchored citations, a self-consistent worked example"
(`reports/round-48/claims.json:29`). The connector's ruling: **`wc -l` closes V only; C03/C04/C05/
C07/C14 close the rest; C06 closes freshness; V01/F01 close the landed tree.**

**Where the budget is measured matters.** The budget must be applied to the *assembled* fenced body,
not to each seat's fragment. No r47 fragment exceeded 503 lines, and they still composed to 739.
The integrator should measure `wc -l` on the single assembled entry (the `C13`/`W01` artifact) before
any apply, and re-measure the landed file after.

---

## 5. The audit chain that must run on composed bytes

The r48 claim's `after_required` says "audits PASS" (`reports/round-48/claims.json:31`). To mean anything, the chain
must be ordered and composed:

1. `C03`/`C04` run on the **final draft bytes**, after all edits; their outputs quote the exact line
   they checked.
2. `C05`/`C14` run on the **assembled** body (fence extracted), not on fragment files.
3. `C06` re-runs the ownership sweep at the **landing HEAD** (still 0 owners, slug free, lands as A),
   not at the round's opening HEAD.
4. `C07`/`A02` re-read the neighbours live: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27,71,102` is the load-bearing
   citation and it is stable at `a01405d`.
5. `V01`/`F01` run **after** the integrator applies: 224 total, culture-material 26, README rev 2.5,
   sweep green, heading count 1, entry `<=~250`.
6. The lander (`W01`) applies exactly one new corpus file plus the README; `N03`/`A04` confirm the
   delta is `A` for the entry and `M` for the README only.

r47's failure was not a missing seat; it was a missing **ordering rule**. Any r48 verdict filed
before step 5 is a prediction, not a delivery certificate.

---

## 6. Ca's durable half: the queue-successor row

### 6.1 The gap being closed is measured, not asserted

- Parent ledger: `reports/round-40/op/defect-queue-v2.json`, sha256
  `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` (unchanged; re-hashed here).
- Predecessor successor: `reports/round-47/calib/queue-successor-r47.json`, sha256
  `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58` (matches
  `reports/round-47/validation.json`), schema `kotodama-defect-queue-successor-v1`.
- Its `rows[]` ids are exactly `r43-stale-premises`, `r44-resolver-hyphen-after-blank`,
  `manifest-ledger-two-schema-evolution`; its two `provider_amendments[]` are the antigravity outage
  and zai exhaustion. `grep -n 'over.build|790|739|R03|B1'` over that file → **no match, exit 1**.
- Therefore the r47 build-quality class has **no row** at `a01405d`. Ca's claim
  (`reports/round-48/claims.json:43-45`) is not re-filing an existing disposition; it is minting the missing one.

### 6.2 Why the freshness gate does not cover it

`tools/harness/claims-freshness.py:97-106` declares a closed probe vocabulary of seven kinds:
`path_absent`, `path_present`, `grep_absent`, `count_eq`, `sha256_eq`, `topic_owner_absent`,
`capability_present`. None measures entry length, arithmetic, or citation quality. The gate's own
selftest is green ("registry 43/43 + seam 19/19 controls"), and it correctly cleared C and Ca and
flagged O at declaration (`reports/round-48/telemetry/dispatch-declared.json`). That is the point:
**topic-ownership freshness is now guarded; entry quality is not.** Teaching that gate to judge
prose would be the wrong tool. A queue row plus the composed audits is the right one.

### 6.3 Proposed successor row (fenced; integrator applies, seats do not)

The row belongs in a **new** `reports/round-48/calib/queue-successor-r48.json` (Ca seat of record:
`calib/Ca02-overbuild.md`, verified by `calib/N02-integrity.md`), pinning both the parent and the r47
predecessor. Class is `routed-with-owner`, not `fixed-with-evidence`: the r48 C landing has not
happened when the row is drafted. The r47 successor's G5 applies the same discipline to the
stale-premises row — a **new** closing row with pasted command output, never an in-place flip — and
this row follows that pattern.

```json
{
  "id": "r47-cartography-overbuild",
  "origin": "r47 C blocked in reports/round-47/validation.json:9 (790-line assembled entry vs live max 221; 9 blocking defects); full finding set reports/round-47/review/R03-c-content.md:188-196; class named at reports/round-48/claims.json:43-45",
  "class": "routed-with-owner",
  "v2_class_equivalent": "carried-with-owner",
  "owner": "r48 C drafters (C01/C02) + r48 integrator; the freshness-gate owner is NOT an owner of this row",
  "reason": "The r47 draft failed on two independent axes: no composing length budget (four fragments composed to 739 body lines / 790 reported, 3.3-3.6x the live max of 221) and audits certified on fragments/pre-fix bytes rather than the assembled body (reports/round-47/review/R03-c-content.md:248). The content was real (reports/round-47/review/R03-c-content.md:98); the assembly discipline was not. The freshness gate guards topic ownership only (tools/harness/claims-freshness.py:97-106) and cannot detect either failure.",
  "next_touch": "r48 C landing: reclass to fixed-with-evidence only when a new closing row carries pasted outputs for (a) wc -l on the assembled and landed entry <=~250, (b) C03 arithmetic, (c) C04 citation anchors, (d) C05 contract, (e) C14 worked example, (f) V01/F01 post-landing census 224. If any leg is missing, the row stays routed-with-owner; never edit this row in place.",
  "evidence": "reports/round-47/review/R03-c-content.md:96 (volume), :188-196 (B1-B9), :248 (audit-chain verdict); reports/round-47/validation.json:9,79; reports/round-48/claims.json:29,31,63; reports/round-48/targets.json:10,17; live partition measurement at a01405d: 25 files, min 103 / median 149 / max 221; corpus/knowledge/linguistics/naming-systems.md:70; corpus/knowledge/culture-material/craft-artisan-lexicon.md:44,54-65; corpus/knowledge/myth-symbol/cosmology-cosmography.md:27,71,102",
  "verification": null
}
```

Fields follow the parent v2 set (`id`/`origin`/`class`/`owner`/`reason`/`next_touch`/`evidence`/
`verification`). `verification: null` is honest, not a placeholder: the closing command does not
exist yet. `N02` should assert the row parses, every path resolves, and the class is in the four-term
vocabulary; `Ca04` should re-read B1–B9 to confirm the reason does not misstate a defect.

### 6.4 What "durable" means here

- The row is a **new artifact**; it edits no filed byte and does not touch `corpus/`.
- The parent and predecessor digests make any later in-place edit detectable.
- The class is scoped to the *process* failure (composing budget + composed audits), so it survives
  even if r48's C lands: the next long entry can still re-trigger it. That is why the next_touch is a
  reclass condition, not a "delete on success."
- The integrator's `LOG.md` entry is the recorded act for the README fix; seats never write LOG
  (AGENTS.md, append-only rule).

---

## 7. The heading-count control the sweep lacks

`python3 -B reports/round-28/readme/sweep.py` is green at the live tree (`rows 223 files 223`,
exit 0) **while the README carries two H1s**. The sweep has no H1 leg: its twelve selftest controls
exercise row paraphrase/ghost/missing/duplicate, partition header counts, totals, the footer legs,
and continuation joining (`reports/round-28/readme/sweep.py:302-401`), but none counts `^# ` lines;
`grep -n 'heading' reports/round-28/readme/sweep.py` → no match, exit 1. Its `header_drift` control
(`reports/round-28/readme/sweep.py:330`) counts `## partition (N)` headers against files — a different object from `^# `.

The defect is old and recorded but never acted on: `R36-README-DUPLICATE-HEADING` sits in
`reports/round-37/op/defect-queue.json:103-111`, was routed at
`reports/round-37/op/O01-queue-draft.md:307`, and is still live at `a01405d`. Ca's fix is therefore
both a live correction and a queue close.

Minimum control semantics (draft for `calib/Ca05-heading-control.md`):

```text
control: H1 count
  command:  grep -c '^# ' corpus/README.md
  expect:   1
  also:     grep -c '^# kotodama-shokunin corpus index' corpus/README.md == 1
  selftest: plant a duplicate H1 in an in-memory README and assert the control FAILS,
            so the leg is not always-green (the sweep's existing style, reports/round-28/readme/sweep.py:302-401).
```

Two acceptable landings, both named in `reports/round-48/claims.json:45,51`: (a) add the leg to the sweep with its
selftest control, or (b) file a durable note with an owner and a next_touch. (a) is stronger because
the sweep is already the index's certificate; (b) is acceptable only if the note carries a re-run
command. A control that only runs once at Ca hand-off is not a control.

---

## 8. Cross-claim interaction: one README, two claims

Both claims write `corpus/README.md`, and neither seat may stage it; the integrator applies.

- **Anchor collision.** C's rewrite targets `:5` (rev-2.5 block), `:234`, `:240-241`, `:544`, `:548`
  (`reports/round-48/claims.json:29`; K02 seed `reports/round-44/scout/K02-gap-scout.md:307-312`). Ca removes the H1
  at `:3` (`reports/round-48/claims.json:43`). Removing `:3` shifts every later line by at least −1; if the following
  blank line is also consumed, by −2. A diff generated against the pre-fix file will not apply
  cleanly after the other edit.
- **Recommended order.** Apply the H1 removal first (or perform both edits as **one atomic README
  write**), then re-derive C's anchors against the post-fix file before generating the rev-2.5 diff.
  Do not apply C's diff first and then hand-edit line 3: that leaves the rev block and totals at
  shifted positions with no re-verified anchors.
- **Staged sha is stale.** r47's staged README receipt (`73985f68…5afc`,
  `reports/round-47/cov/C11-scribe.md:99,122`) was computed with the duplicate H1 still present. The
  post-fix 224 README cannot reuse it. The only delivery certificate is a **fresh** staged sweep on
  the post-both-edits tree (`C11`/`D01`), quoted with `readme_sha256` and `exit=0`.
- **Independent invariants.** After both edits, `rows 224 files 224`, `missing=0`,
  `topic_mismatch=0`, `orphan_rows=0`, `totals_line 224`, footer vector `25/26/26/29/24/94`,
  `readme_sha256` re-measured, H1 count 1.
- **No other README tampering.** The revision history block (`:5-12`) and footer (`:544-548`) must
  otherwise survive byte-for-byte except for the declared rev-2.5 additions and the rev-2.4 vector
  repair; Ca07 checks this.

The two claims are otherwise orthogonal: C adds one corpus file, Ca adds no corpus byte. A01/A04
should see exactly `A corpus/knowledge/culture-material/cartography-and-mapmaking.md` plus
`M corpus/README.md`.

---

## 9. Failure modes that would still repeat the class

| mode | why it passes superficially | the check that stops it |
|---|---|---|
| length-only acceptance | `wc -l` is green, B1/B3/B4 survive | C03/C04/C14 on composed bytes (§3) |
| fragment-scoped audits | four green fragments, inconsistent assembly | C05/C14 extract the **assembled** fence; C13/W01 pin it |
| "fixed" queue row with no output | row says fixed; nothing re-ran | reclass only with pasted command output (§6.3) |
| carried freshness | gap re-asserted from r44/r47 instead of re-measured | C06 sweep at the landing HEAD; `reports/round-48/claims.json:31` |
| double-applied README | both diffs apply, totals drift, sweep red | atomic edit or re-derived anchors; fresh staged sweep (§8) |
| gate-theater | freshness gate green ⇒ "quality checked" | gate vocabulary has no quality probe (§6.2); say so in the round record |

---

## 10. What I did not verify (to-verify)

- **The final r48 draft bytes.** Not filed at my write cut. Every B1–B9 closure in §3 is a required
  check, not a result.
- **The r48 C line count.** The budget is a contract; the measurement belongs to C05/X03 on the
  assembled body.
- **The post-fix README sha.** Unpredictable before the exact H1 edit is chosen (blank-line handling
  changes the bytes); D01 must predict it from a staged tree and C11 must confirm it.
- **Ca01's exact edit shape** (whether the blank line at `:4` is consumed). My §8 states both −1 and
  −2 cases rather than guessing.
- **The r48 successor file path.** `calib/queue-successor-r48.json` is my recommendation; the Ca
  seat of record may name it differently. What must not change is: new file, parent + predecessor
  pinned, row routed not fixed.

---

## 11. Commands and write-surface statement

All commands run from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 - <<'PY'   # line counts of corpus/knowledge/culture-material/*.md
n 25 min 103 median 149 max 221 mean 150.2
$ grep -c '^# ' corpus/README.md
2
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ python3 -c "print(25+23+26+25+24+94, 25+26+25+29+24+94, 25+26+26+29+24+94)"
217 223 224
$ python3 -c "print(0.2*50000/1000, 200/10, 739/149, 739/221, 790/221, 250/221)"
10.0 20.0 4.9597 3.3439 3.5747 1.1312
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l
2   # corpus/knowledge/myth-symbol/cosmology-cosmography.md:102, corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58
$ sed -n '71p' corpus/knowledge/myth-symbol/cosmology-cosmography.md | grep -c cartograph
0
$ sed -n '70p' corpus/knowledge/linguistics/naming-systems.md
... Every renaming is datable; a map is an archive of coups.
$ sed -n '44p;54p;65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
44: | Steel (Japan) | ...   54: | System | Apprentice | Journeyman | Master | ...   65: - Design rule: ...
$ sed -n '27p;71p;102p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
27: Cosmography = ... how the world is drawn (maps) ...   71: T-O ... symbolic, not survey maps   102: ... not cartographic claims
$ sha256sum corpus/README.md reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json
7c788a1d...cdcd  dfc9265d...3907  9508b6aa...ce58
$ python3 -B tools/harness/claims-freshness.py --selftest
SELFTEST OK: registry 43/43 + seam 19/19 controls
$ python3 -B reports/round-28/readme/sweep.py --selftest
selftest: 12/12 checks passed
$ grep -n 'heading' reports/round-28/readme/sweep.py
(no output; exit 1)
$ grep -n 'over.build\|790\|739\|R03\|B1' reports/round-47/calib/queue-successor-r47.json
(no output; exit 1)
```

**Write surface:** this file only — `reports/round-48/cross/X00-connector.md`. No `corpus/**`,
`tools/**`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was
edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py`
was executed.
