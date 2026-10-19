- Seat: S01 | scribe | claim cross | date 2026-10-19 | baseline fd55e1f

# S01 — round-40 integration dossier: fleet-report material + validation-leg spec

**Mission (binding, `reports/round-40/targets.json:166-172`):** *"Integration dossier: fleet-report
material + validation-leg spec."* Out path: this file only.

**Status: DRAFT — integration material, not a fleet report, not a validation receipt, not an
acceptance verdict.** Every number below was measured by this seat at the revision and in the
window named in §1, unless attributed to a sibling fragment (§11 folds each one). Nothing here
asserts promotion, canon, clearance or closure; those tokens appear only as negations, routed
references, or quoted scanner patterns (§10).

**Seat context.** Single 24-seat batch (`claims.json:8`; REGIMEN.md:17 rows 7–8 — 24 requested is
**inside** the declared 16–32 band, no deviation this round). Written mid-wave: at this dossier's
finalization stamp (**2026-10-19T15:12:09Z**, `date -u`) **21 of 23 peer fragments had landed**
(`find reports/round-40 -type f | sort` → 24 files = 3 instruments + 21 fragments); the two
absent peers are exactly claim C's verifiers (`cov/C05-audit.md`, `cov/C07-verify.md`), and this
write closes the scribe slot. The integrator recomputes the census at close (§12) — never trust
either this count or S02's partial 14:08–14:09Z samples (`scribe/S02-telemetry-draft.md:43-48`).

---

## §0 — The headline the integrator must read first

**At this seat's cut, not one byte of any claim's after-state exists.**
`git diff --name-status fd55e1f` → **`M	LOG.md`** only (the uncommitted operator-amendment-7
append, `LOG.md:3763-3771`, parent-owned — verified by this seat's diff read); all other rows are
`?? reports/round-40/…`. Corpus is untouched (sweep green at the **before**-state 216/216, §1);
`reports/round-40/op/` does not exist; the runner, receipt, fleet report, MANIFEST row, SCORECARD
row and LOG entry are all absent (§2.5, §6.4 X-legs).

Consequences carried into the leg spec rather than papered over:

1. **Claim C's after-state is apply-time.** The four entry drafts (C01–C04, all landed) and C06's
   delta are fenced drafts; corpus is integrator-applied by the round's shared rule
   (`targets.json:5`). C06's delta landed with **3 of 4 rows byte-exact and a labeled candidate
   probe in the fourth slot** (`cov/C06-delta-receipt.md:29-34` — C04 was absent at its 15:00:55Z
   poll; C04 has since landed) — the probe row **must be re-derived from C04's landed bytes
   before apply**; a probe applied as a real row would be a fabricated index row. And claim C's
   own threshold "entries audited pre-landing" (`claims.json:18`) is **unmet at this cut**: C05
   and C07 are the round's only absent fragments. No entry may be applied before C05's 4/4
   verdict and C07's independent check exist (§8 order; §6.2 C3).
2. **Claim Ca's counting command does not exist** (`ls reports/round-40/run-validation.py` →
   absent; `validation.json` → absent). It is close-time only and, per `targets.json:8` and X01
   T6 (`cross/X01-trades.md:73-82`), integrator-only in an isolated copy — this dossier is the
   spec the integrator implements (§5–§6), never a runner this seat ran.
3. **The v2's row count passes but its incorporation is disputed — and the dispute is filed, not
   mine to settle.** Ca01's draft has 33 rows (Ca04: 20/20 structural checks PASS, draft-block
   sha `3edb4e52…`, `calib/Ca04-consistency.md:14-21`). R02-1 (major) finds **three fold-in
   findings with no row**: N3 (argot-gate digest supersession), N6 (corpus couples phantoms owed
   repair dispositions), N7 (receipt-fidelity — which R02 independently extends, as this seat
   did, to the r39 receipt's stale CO `route_deviation` block) — at 33 rows the ≥28 threshold
   clears but the claim's own "the r38/r39 findings incorporated" (`claims.json:20`) fails on a
   completeness reading (`review/R02-review.md:62-102`). R02-4 (major) files a **Ca01↔Ca03
   disagreement** on R36-D-DECLARATION (fixed vs carried; conservative disposition = carried,
   r41 flips). Integrator adjudicates both; a green leg must not imply they were absorbed.
4. **The absolute-ROOT runner streak is now six (r34–r39) — the r40 runner is the hard gate.**
   This seat's census: `grep -l 'ROOT = "/home/vgpnk' reports/round-*/run-validation.py` → r34,
   r35, r36, r37, r38, **r39**. The r39 runner re-carried the exact O12 hazard shape its own
   dossier spec'd against (`reports/round-39/run-validation.py:2,5,13` — stale docstring
   *"Round-38 acceptance runner."* at :2, absolute ROOT at :5, `os.chdir(ROOT)` at :13), against
   r39 S01 §5 and r38's X01 ruling. Ca01 filed it as `r39-runner-root-regression`
   (`calib/Ca01-queue-v2.md:375-383`); K02 (§6 F39-1) and R02 (reproduced) converge. Related:
   `runner_sha256` is null in **both** filed r38/r39 receipts (O10 worsened, Ca01 row; R02
   reproduced), and the r39 receipt's `named_findings`/`limits`/`route_deviation` are r38 text
   verbatim (Ca03 N7; R02 A.3; this seat's direct read of the runner at :84-88). The §5
   constants table and §6.4 X4 make all of these cure-legs for this round's own artifact.
5. **Claim A's r40 slice is partial by construction** (X01 T5) and is closed by A03's assembly
   plus the validation leg, not by any seat's prose. A01 and A02 are landed and green-on-the-
   record with named findings (`.scratch/c05` resolver durability; F-A02-1 stale
   `13-register-law.yml:57` prose), X00's C5 correction (r37 telemetry = **5** files, not A01's
   ×6) routes through A03.

---

## §1 — Window, state pins, and what "first-hand" means here

| pin | value | command |
|---|---|---|
| lane root | `/home/vgpnk/Projects/shokunin/kotodama-shokunin` | — |
| baseline | `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` | `git rev-parse HEAD`; `git rev-parse fd55e1f` (equal) |
| tracked delta vs baseline | **`M LOG.md` only** — the uncommitted amendment-7 append (10 lines, `LOG.md:3763-3771`) | `git diff --name-status fd55e1f`; diff content read |
| untracked scope | `?? reports/round-40/…` only | `git status --porcelain -uall` |
| finalization stamp | `2026-10-19T15:12:09Z` | `date -u +%FT%TZ` |
| env | `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` | before every python invocation |

**No `reports/round-*/run-validation.py` was executed anywhere by this seat** (in-tree or in a
copy; `targets.json:8`), no `--freeze` touched `reports/round-34/handoff/declared-in-r7`, no git
mutation, no network, no install, no corpus staging. The one sweep this seat ran is the round-28
README sweep — read-only over `corpus/` (`reports/round-28/readme/sweep.py:28-30`; digest and
selftest pinned by C06 §1: `9b2ccac0…`, 12/12).

**Digests this dossier binds to** (measured at `fd55e1f`, lane root; attributions in brackets):

```
a2e122c60f66c64bbdce5b7e44922075a40c848ec3e551f8f3c8c63a9b5a22c0  reports/round-40/claims.json   [this seat; == durable_sources]
710b81ccde9dd6e218d35fef3e951acc2b1ba7d94fadd509de9cbb65476afe72  reports/round-40/targets.json  [this seat; == durable_sources]
abffc26b4cd3a7e9de2b6ab819803cf6221485c8d231123ac395ccee1d81d080  reports/round-40/telemetry/dispatch-declared.json [this seat; == S02 §1]
e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a  corpus/README.md               [this seat, via sweep readme_sha256]
5cf827e2dd17b638acf023b1c6423b0602ba88e3c08d9698b68bae6c6cc60d5d  reports/round-37/op/defect-queue.json [K02 §1; == Ca04 check 16; == r39 S01 §1 pin]
05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6  PROVINCE.md                    [A02 §1, live == HEAD]
3edb4e52f22d91da343d1662284af9135322912a64e81be173440c41cc598121  Ca01's fenced v2 draft block   [Ca04 §artifact — the landing byte-identity pin]
9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3  reports/round-28/readme/sweep.py [C06 §1, == r39 pin]
```

**Cross-check PASS:** the two declaration digests equal
`telemetry/dispatch-declared.json` `durable_sources` (this seat's `sha256sum`) — the filed
dispatch record is bound to the same bytes this seat read. S02's independent digest set matches
mine (`scribe/S02-telemetry-draft.md:14-21`).

**Before-state of claim C, first-hand and green** (all three counters measured by this seat):

```
$ ls corpus/knowledge/linguistics/*.md | wc -l            → 21
$ find corpus/knowledge -name '*.md' | wc -l              → 216
$ python3 -B reports/round-28/readme/sweep.py | tail      → exit 0; totals_line 216 totals_ok True;
  footer {total 216, dir_totals [21,23,25,29,24,94]}; footer_live … order [linguistics, myth-symbol,
  culture-material, synthesis, verification, civilizations]; footer_findings [] footer_ok True;
  readme_sha256 e73dc971…
```

This confirms `claims.json:15` (linguistics 21, total 216) and converges with **nine** sibling
measurements (§3.1). The after-vector `25/23/25/29/24/94` moves the **first** slot only
(claims.json:16; C06 delta; P01 §0).

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth, and never clearance.

---

## §2 — Declaration facts, measured

### §2.1 Schema and identity

`claims.json` carries exactly 12 keys (`round`…`non_goals`); declared baseline token `fd55e1f`
(`:7`) resolves to live HEAD (§1). `axes_in_play` = `["coverage","calibration","adjacency"]`
(`:9`); the claim objects are exactly `{C: coverage, Ca: calibration, A: adjacency}` (`:13-30`)
— distinct axes; `freshness_pause_in_force: true` (`:11`); `non_goals` (`:32-33`) forbids
freshness moves, promotion/canon/clearance/closure, filed-byte rewrites, in-tree runner
execution, and re-freeze of declared-in-r7. Position 8 of loop 1 — the midpoint consolidation
round (`:5`); regimen field names "operator amendment 7 (2026-10-19)" (`:3`), which exists as an
uncommitted LOG.md append authorizing devin for deepseek-v4.1-flash waves (§1; irrelevant to
this round's zai dispatch).

### §2.2 The lowest-axis arithmetic is imprecise — recorded, no admission impact

X01 F1 (`cross/X01-trades.md:94-101`) measured the regimen-2 claim census from SCORECARD: depth
3, coverage 3, adjacency 3, calibration 4, operability 5 — so `lowest_axis_reasoning`
(`claims.json:10` "Adjacency is the least-claimed non-paused axis (3); coverage and calibration
follow (3-4)") mis-states a three-way tie at 3. Claiming A still satisfies the lowest-non-
paused-axis precedent; the integrator's SCORECARD row should carry X01's correction.

### §2.3 Dispatch honesty

Declared: `zai-coding-plan / glm-5.3-flash`, 24 workers, 1 batched call (`claims.json:8`;
`dispatch-declared.json` allocation block; S02 §1) — inside REGIMEN.md:17's declared 16–32; no
fallback clause invoked. Observed launch/completion/failure counters are **unknown to this
seat**: `null` with owner `orchestrator (goal-mode parent)` until `observed-dispatch.json` /
`availability-close-40.json` land (S02 §2–§3 templates) — never inferred zeroes, never a claimed
completion rate (AGENTS.md). The declared record's `closing_snapshot` field reads
`open-at-seat-close: owed once validation.json lands`. r39's precedent (zai 16/16, R02 §A.2
citations) shows the counters are recoverable at close.

### §2.4 Seat census (this seat's measurement; a census, never launches)

```
seat_count 24   rows 24   unique ids 24   unique out paths 24   duplicates []
claims {C: 8, Ca: 5, A: 4, cross: 7}
roles  {executor: 9, verifier: 5, scout: 3, scribe: 2, reviewer: 2, planner: 1, connector: 1, critic: 1}
dirs   {cov: 7, calib: 4, scout: 3, adj: 3, cross: 2, review: 2, scribe: 2, plan: 1}
```

No undeclared claim block; `claims.json` has no `baseline_expanded` key (the r36 Trap 1 does not
repeat). Note: **no seat `out` path owns `op/`** — `op/defect-queue-v2.json` is the
integrator-applied landing of Ca01's fenced block (Ca01 `## Owed`; X00 §3.6b), which is why the
census's 24 out paths and the artifact roster differ by exactly that file.

### §2.5 Landed census at this dossier's finalization (15:12:09Z)

24 files under `reports/round-40/` = 3 instruments + **21 fragments**: adj A01–A03, calib
Ca01–Ca04, cov C01–C04 + C06, cross X00 + X01, plan P01, review R01 + R02, scout K01–K03,
scribe S02. **Absent (2 peers + this file):** `cov/C05-audit.md`, `cov/C07-verify.md` — the two
claim-C verifiers; every other seat delivered. Recompute at close (§12); the binding absence is
C05: claim C's own "audit 4/4 PASS" threshold is unmet until it lands.

---

## §3 — Landed-fragment cross-check: what converges, what this seat adds

### §3.1 Premises (three or more seats, no coordination)

| premise | sources |
|---|---|
| linguistics 21, total 216, README rev 2.2, sweep green 216/216, footer [21,23,25,29,24,94] | K01 census totals, K03 §1, P01 §0, X01 F2, A01 §3/§5, A02 §2, C06 §1, S02 baseline, this seat §1 — **converges, 9 independent measurements** |
| HEAD == fd55e1f; tree delta = `M LOG.md` (amendment 7, uncommitted) + `?? reports/round-40/` | K01 round-40 table, A01 snapshot, A02 §1, X01 F8, S02 §1, this seat §1 — **converges** |
| absolute-ROOT streak = six (r34–r39); r39 runner re-carried the O12 shape | this seat §0.4 grep; Ca01 rows (R36-ABSOLUTE-ROOT, O12, r39-runner-root-regression); K02 row 9 + F39-1; R02 §A.1 reproduced — **converges** |
| `runner_sha256: null` in r38 (`validation.json:130`) and r39 (`:126`) receipts | Ca01 O10 row; R02 reproduced — **converges; O10 worsened** |
| duplicate README H1 live (grep → 2), sweep-blind; do-not-touch inside rev 2.3 | Ca01 R36-README-DUPLICATE-HEADING row (HEAD grep); K02 row 10; r39 X00-7 lineage — **converges** |
| the five r37 `id: null` rows map 1:1 to minted `R37-O01-CAND-*` ids | Ca01 notes; Ca04 check 14 PASS; R02 §A.1 line-by-line — **converges** |

### §3.2 This seat's additions (what no landed fragment states in this form)

1. **The stale r39 receipt surfaces are three, not two.** Ca03's N7 named `named_findings` +
   `limits`; this seat's direct read of the r39 runner adds the CO-leg `route_deviation`
   measurement dict at `reports/round-39/run-validation.py:84-88` — verbatim r38 text
   (`declared: "xai-oauth/grok-4.7-fast"`, `wave_shape: "22+10 = 32/32"`) contradicting r39's
   own zai/16 declaration. R02 A.3 independently extends N7 to the same third surface (citing
   `validation.json:47-58`) and shows r39's telemetry recovered the true route (zai 16/16) — so
   the correction row's cure is fully specifiable: the r40 runner emits **round-specific**
   `named_findings`, `limits`, and route facts, or omits them with an owner.
2. **The r39 runner's protected-tree regex under-covers its own baseline.** It sweeps
   `reports/round-(?:[1-9]|[12][0-9]|3[0-7])/` (`reports/round-39/run-validation.py:137`) —
   rounds 1–37 — leaving the r38 tree unswept at r39 close. The r40 runner must extend to
   `3[0-9]` (rounds 1–39; round-40's own tree is excluded by the range itself). Same-shape
   corpus check is safe for claim C: it iterates `git ls-tree` of the **baseline**, so r40's new
   linguistics files are additions, never false "moved" rows, while any *modified* pre-existing
   entry fails loudly.
3. **The `op/` landing gap is a census fact, not just an Owed row** (§2.4): Ca04's 20 checks
   were run against the fenced draft bytes (sha `3edb4e52…`), so landing is gated on byte-
   identity or a full re-parse (`Ca04 ## Owed`; §6.3 Ca1).
4. **C06's fourth row is a probe** (§0.1) — the only place where claim C's arithmetic (21+4=25)
   could silently become a fabricated index row. The sweep cannot catch a byte-equal row for a
   file that does not exist; C07's "rows vs landed files" check (mission `targets.json:89-95`)
   is the instrument that can.

---

## §4 — Fleet-report draft for `.ufo/reports/round-40/kotodama.md`

The fleet root is `/home/vgpnk/Projects/shokunin/.ufo/`; `ls .ufo/reports/round-40/` → absent at
this seat's cut (parent-owed; r37/r38/r39 reports all present). The four headings are the tuple
the filed runners check; use them **verbatim**. Everything below is drafted from the 21/23
landed set — **the integrator re-derives each sentence from the 24/24 set and the close-time
tree**, and strikes or rewrites any line a later fragment falsifies.

### Draft header

```text
# kotodama — round 40 report (2026-10-19)

Regimen 2 (`REGIMEN.md:17`), loop 1, position 8 — the loop-1 midpoint consolidation round.
Declared allocation `zai-coding-plan / glm-5.3-flash` (MAX-effort seats), 24 requested workers,
one batched AgentSwarm (`claims.json:8`; `telemetry/dispatch-declared.json`) — 24 is within the
row's declared 16–32 band; no fallback declared and none invoked. Declared baseline `fd55e1f`
(`claims.json:7`) = `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` (the r39 admission commit).
Claims C/Ca/A on coverage/calibration/adjacency (`claims.json:13-30`); freshness axis-move
claims stay paused (`claims.json:11`). Observed launch/completion counters: per the closing
snapshot (`telemetry/availability-close-40.json`) — never inferred at seat time. Seat
accounting: `seat_count: 24`, 24 rows, 24 unique out paths (measured,
`scribe/S01-integration-draft.md` §2.4). The round is not admitted to LOG.md while its closing
snapshot is owed (`AGENTS.md` close-what-you-open).
```

### Draft — Work performed

```text
- **Coverage (claim C):** the linguistics partition (thinnest non-verification, 21; K03 §1) is
  the target: K03 scouted the routed gaps G2–G4 plus a fourth (sacred registers / liturgical
  language), each with registered in-corpus sources and a measured collision check vs the 21
  existing filenames — zero collisions, four clean sort positions, per-topic overlap verdicts
  with non-restatement boundaries that double as C05's audit criteria (`scout/K03-gaps.md`).
  Executors C01–C04 landed four self-contained fenced drafts (taboo strata lifecycle;
  dialect/register-consistency; translation-protocol fidelity; entry 4 per K03 §3-E4), each with
  its own measured absence sweep, couples resolution and source-provenance limits; C02/C03
  follow K03's scopes and filenames exactly, C01 predates K03 (X00 C1: one filename conflict on
  E1, integrator picks, C06 re-derives). C06 drafted the README rev-2.3 delta (header 21→25,
  totals 216→220, footer first slot 21→25) with 3 rows byte-exact and the fourth a labeled
  probe pending C04 (`cov/C06-delta-receipt.md`); C05's audit and C07's independent verify were
  in flight at this dossier's cut — whether all four pass is recorded by
  `reports/round-40/validation.json`, not asserted here.
- **Calibration (claim Ca):** the defect-queue v2 refresh. Ca01 assembled the v2 from the filed
  records with K02 absent at its cut: all 24 r37 rows re-verified (8 fixed-with-evidence with
  citations, 2 worsened — O10 null-receipts ×2, the six-runner absolute-ROOT streak; the five
  id:null rows minted stable ids), 9 new rows folding the r38/r39 findings (33 total; ≥28),
  schema `kotodama-defect-queue-v2`, new class recorded in notes, next-touches aligned to loop-1
  positions 41–46 with r46 audit-only legality (X01 T3). K02's scout landed afterward and
  cross-checks the census (`scout/K02-queue-scout.md`); Ca04 ran 20 structural checks — all
  PASS, draft sha `3edb4e52…`; Ca02 samples ≥30% of rows to origins; R02's completeness hunt
  filed R02-1 (three fold-ins missing: N3/N6/N7) and R02-4 (the Ca01↔Ca03 R36-D-DECLARATION
  adjudication) — integrator rulings owed, never absorbed.
- **Adjacency (claim A):** the loop-1 midpoint audit. K01 censused rounds 37–40 surfaces
  (149 files added + 10 shared-surface edits across r37–r39; risk classes R0–R3); A01 audited
  per-surface with verdicts (green; two named findings: the r39 in-round stray-staging
  resolution already on the record, and the `.scratch/c05` resolver durability route); A02
  re-verified PROVINCE.md byte-accurate at HEAD (7/7 clauses, 2 spot-check-limited) and filed
  F-A02-1 (stale `13-register-law.yml:57` enforcement prose; owner integrator, window next
  re-freeze); A03 verified a sample of both and assembled the consolidated audit; X00's C5
  correction (r37 telemetry = 5 files) carried. Rounds 37–40 absorbed nothing; contested scope
  routed with owners throughout.
- **Cross:** P01's three-claim plan; X00's binding collision matrix + integration order;
  X01's trade/conformance pass (T1–T7, F1–F8); R01's adversarial review of all three blocks;
  R02's queue-completeness + fabrication hunt; this dossier's fleet-report material,
  validation-leg spec, and the six-runner census.
```

### Draft — Landed changes

```text
- At the source dossier's cut: **no claim artifact landed.** `git diff --name-status fd55e1f`
  → `M LOG.md` only (the parent-owned amendment-7 append); untracked rows all
  `?? reports/round-40/…`. Corpus: untouched at the before-state (linguistics 21, total 216,
  README rev 2.2, sweep green). The C deliverables exist only as fenced drafts (C01–C04 + C06
  landed; C05/C07 in flight); the Ca deliverable as Ca01's fenced v2 (33 rows, sha `3edb4e52…`)
  plus its verifiers; the A deliverable as the landed census/audit/assembly chain.
- If the integrator applies the drafts, the landed set is: four new
  `corpus/knowledge/linguistics/*.md` entries (final names per X00 C1 — one E1 conflict to
  resolve), one `corpus/README.md` revision 2.3 (header 25, four filename-ordered byte-equal
  rows, totals 220, footer 220 + 25/23/25/29/24/94), `reports/round-40/op/defect-queue-v2.json`
  (Ca01's block, fold-in adjudications applied, byte-identity per Ca04), the round's own runner
  + receipt, and the A03 final audit assembly. Filed bytes: zero moves anywhere
  (`reports/round-1..39/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`,
  the r7 freeze set) — asserted by the runner's digest sweep, not by this prose. The uncommitted
  LOG.md amendment-7 append commits with the round (X00 §3.6f).
- The round's evidence artifacts (24 seat fragments) are evidence, not product changes.
```

### Draft — Before → after measurements

Fill from §6's leg table at close; before-values are this seat's §1 measurements.

| axis | before (measured at `fd55e1f`) | after required (`claims.json`) | status at my cut |
|---|---|---|---|
| coverage (C) | linguistics 21; total 216; README rev 2.2; sweep green 216/216; footer [21,23,25,29,24,94] | linguistics 25, total 220; README rev 2.3 sweep-green (220 == 220); 4/4 audit PASS pre-landing | **not landed** — 4/4 drafts + delta drafted; audit + independent verify in flight; no corpus byte applied |
| calibration (Ca) | r37 queue 24 rows, r37-aged (`5cf827e2…`); r38/r39 findings live only in round records; census_coverage carried-not-claimed | `op/defect-queue-v2.json` all-current; findings incorporated; ≥28 rows; every row owner-complete; next-touches on 41–46 | **drafted** — 33 rows, 20/20 structural PASS; R02-1 fold-ins + R02-4 adjudication owed; landing + re-parse owed |
| adjacency (A) | r35 audited r33–34, r37 audited r33–36; rounds 37–40 surfaces had no consolidated pass; PROVINCE last touched pre-r33 | consolidated census with per-surface verdicts; PROVINCE byte-accurate at HEAD; zero unfiled bleed | **landed on the record** — K01/A01/A02/A03 chain + X00 C5 correction; r40 slice time-stamped partial (X01 T5), closed by the validation leg |
| cross | runner absent; C05/C07 + v2 landing + fleet report / MANIFEST / LOG / SCORECARD rows absent (all measured) | runner (relative ROOT, runner_sha256, round-specific findings) + receipt; report with 4 headings; bookkeeping rows; telemetry closed | **owed** (§5, §8, §9) |

### Draft — SHONEN

```text
No SHONEN box was re-surveyed by this round, and no landed round-40 fragment establishes a new
end-to-end domain-task result. Carry the prior status only as *last recorded*, not as a
round-40 re-verification: `reports/round-36/scribe/S01-integration-draft.md:248-267` records
boxes 1–4 as `verified-with-conditions` (with the box-1 citation conditions, the box-2 D4
garment/RL-3/head2 debts — OI-02 still carried in Ca01's v2 — the box-3 N1/N4/N5/N7 items and
the box-4 standing readings); rounds 37/38/39 landed no box change, and this round's fragments
survey no box. Round-40 findings do not alter those records. No promotion decision is taken or
implied; the decision remains operator-owned (`SHONEN.md:10-11`).
```

---

## §5 — The round-40 runner: constants that must NOT be inherited

Cloning the most recent runner (`reports/round-39/run-validation.py`) produces a runner that
re-carries the O12 hazard shape **and** the receipt-fidelity defects Ca03/R02 filed. Every
inherited constant that is wrong for r40, with the measured replacement:

| r39 constant / path | r39 value | round-40 value | evidence |
|---|---|---|---|
| docstring | `"""Round-38 acceptance runner."""` (`:2`) — stale | `Round-40 acceptance runner.` | this seat's `sed -n 2p`; Ca01; R02-3 |
| `ROOT` | **absolute literal** (`:5`) + `os.chdir(ROOT)` (`:13`) — the O12 shape, sixth in the streak | **relative**: `ROOT = Path(__file__).resolve().parents[2]` (the r33 shape, `reports/round-33/run-validation.py:23`); **parse flags before any chdir** | §0.4 census; Ca01 `r39-runner-root-regression`; K02 F39-1; r39 protocol §4 standing requirement |
| `ROUND` / `COMMAND` | `reports/round-39` / `python3 reports/round-39/run-validation.py` | `reports/round-40` / `python3 reports/round-40/run-validation.py` (`claims.json:23,29`) | declarations |
| `BASELINE` | `dfb0719` | `fd55e1f` → `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` | §1 |
| seat count | 16 | **24** | `targets.json:3`, measured §2.4 |
| `claims_declared` | `{C: coverage, Ca: calibration}` | `{C: coverage, Ca: calibration, A: adjacency}` | `claims.json:13-30` |
| protected-tree regex | `3[0-7]` (`:137`) — r38's tree unswept | `reports/round-(?:[1-9]|[12][0-9]|3[0-9])/` (rounds 1–39) + `corpus/lessons/(?!README)` + `tools/gates/frozen/round-` + `reports/round-34/handoff/declared-in-r7/` | §3.2 item 2; r39 runner read |
| corpus-knowledge check | baseline-ls-tree iteration (safe for additions) | keep; it must flag any *modified* pre-existing entry and stay silent on r40's four additions | §3.2 item 2 |
| CO route facts | `m["route_deviation"]` = r38 verbatim (`:84-88`) | round-specific: declared zai/24 vs observed from `observed-dispatch.json`, or omit with owner — never inherited text | §3.2 item 1; R02 A.3; Ca03 N7 |
| `named_findings` / `limits` | r38 verbatim (`validation.json:118-123`) | round-specific, generated from this round's measured findings | Ca03 N7; R02-1/A.3 |
| `runner_sha256` | `rec()` returns `None` → `null` (r36/r38/r39 receipts) | the schema leg records the runner's own sha256 into the receipt (O10 cure) | Ca01 O10 row; R02 §A.1 |
| coverage input | verification partition | **new**: linguistics count, sweep exit/footers, README rev-2.3 fields, C05 audit presence, C07 verify presence | `claims.json:16-18` |
| calibration input | protocol/successor/policy pins | **new**: `op/defect-queue-v2.json` (landed sha vs `3edb4e52…`, row accounting, class vocabulary, owner-completeness, fold-in adjudications) | `claims.json:20-24`; Ca04 |
| adjacency input | P1 protected sweep only | **new**: the A03 assembly + K01 census presence + A02's PROVINCE sha `05b34a57…` + zero-unfiled-bleed `git status` check | `claims.json:26-30` |
| fleet report path | `…/.ufo/reports/round-39/kotodama.md` | `…/.ufo/reports/round-40/kotodama.md` (absent at my cut) | §4 |
| closing snapshot | `availability-close-39.json` | `availability-close-40.json` (landed naming convention), sha-pinning `abffc26b…` at close | S02 §2.3 |
| mode surfaces | `--check` print-only; `guard_receipt()` | keep both; **flags parsed before any chdir** | K02 §1 mode ordering (r39); X01 T6 |

**The `ROOT` line is again the load-bearing one.** Six filed runners carry the absolute shape;
every r38+ runner was supposed to resolve from `__file__` (`reports/round-39/calib/
isolation-replay-protocol.md` §4, standing requirement). A relative-ROOT r40 runner makes the
rule mechanically enforceable for this round's own artifact instead of promissory — and three
queue rows (F-C13-1, R36-ABSOLUTE-ROOT/O12, r39-runner-root-regression) name exactly this
next-touch at r40 close (Ca01 `## Next-touch alignment`).

---

## §6 — Validation-leg spec (machine-checkable)

Format: `id | check | expected`. Every leg is written so it is true and useful whether or not
the integrator applies the drafts — where an after-state does not exist, the leg records
`could-not-evaluate` rather than passing, and no `could-not-evaluate` counts toward acceptance.

### §6.1 Coherence / schema / declaration legs (cross)

| ID | check | expected |
|---|---|---|
| **CO1** | strict-parse `claims.json`, `targets.json`, `dispatch-declared.json` (duplicate keys refused); `round == 40` in all three; `baseline_commit == "fd55e1f"`; `git rev-parse --verify fd55e1f^{commit}` → `fd55e1fd…`; declared token and resolved id recorded separately | pass |
| **CO2** | `{c.id: c.axis}` == `{C: coverage, Ca: calibration, A: adjacency}`; `set(axes_in_play)` == same three; axes distinct; `freshness_pause_in_force is True`; `"freshness"` absent from every claim axis; `non_goals` carries all five declared items (`claims.json:32-33`) | pass |
| **CO3** | seat census: `len(seats) == 24 == seat_count`; 24 unique ids; 24 unique `out` paths under `reports/round-40/`; every id/role/mission non-empty; report the §2.4 vectors as the measurement | pass |
| **CO4** | declared-output completeness: all 24 `out` paths exist at close and are **non-empty** (min-bytes check — the r38 O07 0-byte lesson, Ca01's `r38-O07-empty-fragment` next-touch); any absent one named in `missing_dependencies` with owner | pass |
| **CO5** | dispatch shape: declared allocation exactly (`zai-coding-plan`, `glm-5.3-flash`, 24 requested, 1 batched call) across `claims.json:8` and `dispatch-declared.json`; 24 within `REGIMEN.md:17`'s 16–32 (record the range); `durable_sources` digests equal live bytes (`a2e122c6…`, `710b81cc…`) | pass |
| **CO6** | observed dispatch: if `observed-dispatch.json` / `availability-close-40.json` exist, requested allocation and observed launches/completions/failures/route stay **separate fields**; absent counters stay `null` with owner + reason — never inferred zeroes; provider liveness is not round acceptance | pass / could-not-evaluate |
| **CO7** | protected-tree census: `git ls-tree -r --name-only fd55e1f…` + regex walk (rounds 1–39 via `3[0-9]`, `corpus/lessons/(?!README)`, `tools/gates/frozen/round-`, `declared-in-r7/`), live bytes vs `git show fd55e1f…:<path>` digests. Never a literal `round-1..39` pathspec (dead check, r38 dossier §3.4). Corpus-knowledge entries: modified pre-existing files fail; r40's four additions are not in the baseline ls-tree and cannot false-fire | pass |
| **CO8** | runner census: `ls reports/round-*/run-validation.py \| wc -l` → **35** at close (34 measured §0.4 + this round's); record the count and digests of all filed `validation.json`s; **digests, never re-computed verdicts**; the count change is a revision boundary, not a failure | pass |
| **CO9** | godspeed lead: not machine-checkable from durable artifacts (prompts not persisted; AGENTS.md forbids prompt payloads in telemetry) → `could-not-evaluate`, owner `orchestrator`, `dispatch-declared.json` the only evidence | could-not-evaluate |
| **CO10** | regression floor: the r28 sweep exits 0 pre-apply (216/216) **and** post-apply (220/220) as §8's ordering runs it; §1's digest block unmoved across the run | pass |

### §6.2 Claim-C legs (coverage: the linguistics partition)

| ID | check | expected |
|---|---|---|
| **C1** | **before-state pins** (binding): `ls corpus/knowledge/linguistics/*.md \| wc -l` → 21 pre-apply / **25** post-apply; per-dir find → 94/25/**21**/23/29/24 pre → 94/25/**25**/23/29/24 post (total 216 → **220**); record both | pass |
| **C2** | the four entries exist under `corpus/knowledge/linguistics/`, each with the round-35/36/39 contract: H1 + `- topic:` / `- gap filled:` / `- sources:` (registered in-corpus, locators) / `- calibration:` / `- couples:` / `- source:` / `- verified-at:` / `- recheck:` (+ C01's `- scope:` is permitted extra), a gap statement with a measured absence sweep, and a numbered decision record | pass / failed |
| **C3** | **uniqueness + audit ordering** (claim's own threshold, `claims.json:18`): C05's audit exists with a **4/4 PASS** verdict (named defects allowed) and C07's independent verify exists; the four filenames are unique vs each other and vs the 21 existing; the E1 conflict (C01's `taboo-strata-lifecycle.md` vs K03's `taboo-euphemism-lifecycle-stages.md`, X00 C1) is resolved **by the integrator, on the record**; topics disjoint per K03 §2 | pass / failed |
| **C4** | **probe replacement**: C06's landed README delta contains **no probe row** — the fourth row is byte-derived from the actual landed `C04-entry-4.md` head block (X00 C1(c); C06 §5.4's own label). A row whose file does not exist on disk fails even if the sweep passes its byte-equality half | pass / failed |
| **C5** | **README rev-2.3 delta, byte-level**: new revision block above rev 2.2; `## linguistics/ (25)`; exactly 4 new rows in filename order; each row's `- topic:` text **byte-equal** to its entry's own (sweep `topic_mismatch`); totals line `Total knowledge entries: 220.`; footer total 220, vector `**25**/23/25/29/24/94` (first slot only); footer date = the re-measure date | pass / failed |
| **C6** | **the sweep is green on the LANDED tree**: `python3 -B reports/round-28/readme/sweep.py` → exit 0, rows 220 files 220, 0 missing/ghost/mismatch/drift — run **after** entries+README both land; plus `diff` landed README vs C06's draft with the probe substitution applied (the `readme-prediction-vs-delivery` standing practice: staged-sha prediction + landed diff + post-apply sweep) | pass |
| **C7** | **source resolution + no-restatement**: every `- sources:` locator and in-body cite resolves at HEAD; external sources already registered in-corpus (K03 §3 policy); the K03 §5 non-restatement boundaries hold (E1 vs `politeness-taboo-euphemism.md:80-118`, E2 vs `sociolinguistics-registers.md:64`, E4 vs `historical-linguistics.md:237`) — C05's criteria verbatim | pass / failed |
| **C8** | **do-not-touch held + lessons gate**: the README duplicate H1 is **not** repaired inside rev 2.3 (X00 lineage); no corpus byte beyond the 4 entries + README moved (CO7 covers); `corpus/lessons/*.md` digests unmoved | pass |

### §6.3 Claim-Ca legs (calibration: the defect-queue v2)

| ID | check | expected |
|---|---|---|
| **Ca1** | **the v2 lands at the canonical path**: `reports/round-40/op/defect-queue-v2.json` exists; landed sha256 == `3edb4e52…` **or** (if the integrator landed adjudication-edited bytes) Ca04's checks 1–17 re-run green on the landed file, recorded. Strict JSON, no duplicate keys, header `round: 40`, `baseline_commit: fd55e1f`, parent digest `5cf827e2…` | pass / failed |
| **Ca2** | **row accounting + incorporation**: 24 r37 rows all accounted (12 named + 5 minted `R37-O01-CAND-*` + 7 later-origin); ≥28 rows; **the R02-1 fold-ins resolved**: N3/N6/N7 present as rows **or** the disagreement filed with owner in the round record — a green leg must not imply incorporation that did not happen (`claims.json:20`); no padding rows without origin citations | pass / failed |
| **Ca3** | **the R02-4 adjudication is recorded, not absorbed**: the receipt names the integrator's ruling on R36-D-DECLARATION (Ca01 `fixed-with-evidence` vs Ca03/R02's conservative `carried`, r41 flip); either disposition satisfies the claim if recorded with the disagreement | pass-with-recorded-ruling |
| **Ca4** | **owner-completeness**: zero rows with null/empty `owner`/`reason`/`next_touch`; zero `owner: "unassigned"` (Ca04 check 11: 33/33) — re-checked on the **landed** bytes | pass |
| **Ca5** | **class vocabulary closed + evidence-gated**: exactly {`carried-with-owner`, `fixed-with-evidence`} unless a landed adjudication adds one with a `notes` reason; every `fixed-with-evidence` row carries non-null `verification` (Ca04 checks 5/6/12) | pass |
| **Ca6** | **next-touch legality**: no carried row routes implementation work to r46 (read-only audit, `REGIMEN.md:23`; X01 T3); every named lane round ∈ {40 close, 41–45} or loop-2/external/condition-gated by declared design; zero rows route back to r33–39 (Ca04 checks 17–19 + R02 A.6) | pass |
| **Ca7** | **verifier service**: Ca02's ≥30% origin sample (≥10 of 33) landed with disagreements filed; K02's scout + census cross-check landed (it has — `scout/K02-queue-scout.md`); Ca04's landed-bytes re-parse condition discharged; R02's hunt dispositioned | pass |
| **Ca8** | **census_coverage disposition stated**: `K02_r40_census_rows_seen` is filled **or** stays `null` with the absence reason and the completion carried with owner (Ca01+K02+Ca02+R02 — all four have now landed and serviced it); the claim's "completed or its completion carried with an owner" (`claims.json:20`) is met **only** with the owner named | pass |

### §6.4 Claim-A legs (adjacency: the consolidated midpoint audit)

| ID | check | expected |
|---|---|---|
| **A1** | the consolidated audit assembly exists (`adj/A03-verify-assembly.md` + integrator filing), covering every K01-census surface with a verdict (green | named finding + owner); the X00 C5 correction (r37 telemetry = **5**, not ×6) carried; the two historical bleed events (r37 placeholders, r39 stray C03-draft) stay on the record as filed | pass |
| **A2** | **PROVINCE byte-accurate at HEAD**: `sha256sum PROVINCE.md` == `05b34a57…` == `git show HEAD:PROVINCE.md`; A02's 7/7 clause verdicts folded; the contested-scope table (9 items, zero absorbed) folded | pass |
| **A3** | **zero unfiled bleed at close**: `git status --porcelain -uall` shows only committed round-40 rows + the amendment-7 LOG append **committed**; no corpus staging by any seat at any sample; F-A02-1 and the `.scratch/c05` durability finding are filed with owners (queue rows per X00 C3(d)/(e)) | pass |
| **A4** | **the r40 slice is time-stamped partial**: the assembly marks which r40 surfaces were censused in-flight and names the validation leg as the closer (X01 T5) — an unqualified "rounds 37–40 complete" claim fails this leg | pass |
| **A5** | **language/ownership scan**: the K01 census + A01 §5 greps reproduce (zero refused-domain ownership claims across the audited surfaces; canon/chousa mentions are routing language) | pass |
| **A6** | **non-goals held**: no re-freeze of declared-in-r7 (`examples/` diff vs baseline empty); no freshness move; no filed-byte rewrite outside the declared surfaces | pass |

### §6.5 Cross / close legs

| ID | check | expected |
|---|---|---|
| **X1** | fleet report at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-40/kotodama.md`, four headings verbatim, ISO date, cites the round-40 runner; absent at my cut → integrator writes (§4 draft) | pass / owed |
| **X2** | MANIFEST rounds[] entry: `grep -c '"round": 40' MANIFEST.json` → **0** at my cut (r39 row exists); absent → `pending-by-construction`, owner integrator | pass / owed |
| **X3** | telemetry: `observed-dispatch.json` + `inputs/` per S02 §2; **`availability-close-40.json`** only after `validation.json` lands — schema `kotodama-availability-closing-snapshot-v1`, `closes` = the dispatch record, `closes_sha256` = `abffc26b…` re-verified at close; the round is **not admitted to LOG.md while it is owed** (AGENTS.md; X00 §3.6f) | pass / owed |
| **X4** | receipt self-consistency: `round == 40`; exact counting commands (`claims.json:17,23,29`); `baseline_revision == "fd55e1f"`; **`runner_sha256` non-null**; `named_findings`/`limits`/route facts round-specific (the O10/N7/R02-A.3 cure legs); `missing_dependencies` ⊇ absent declared outputs (C05/C07 if still absent); `acceptance_checks_passed` true only if every leg is green — no `could-not-evaluate` counted as a pass | pass |
| **X5** | language scan over `reports/round-40/**`: zero unadjudicated grant/completion frames; every declared seat `out` path present in the scan including absent ones, named as absent | pass |
| **X6** | SCORECARD row (with X01 F1's corrected claim census) + append-only LOG entry under the lane identity, including the amendment-7 append committed; both measured absent at my cut (`grep -c "round-40\|Round 40"` → 0/0) — integrator-only writes, listed owed | pass / owed |

---

## §7 — The non-vacuous test each claim must survive

| # | claim | test that fails today | why a green reading fails today |
|---|---|---|---|
| 1 | C / partition | `ls corpus/knowledge/linguistics/*.md \| wc -l` → **25** | 21 at baseline (§1, 9 measurements) |
| 2 | C / README | sweep exit 0 at **220 == 220** with footer `[25,23,25,29,24,94]` | green at 216/216 today; an entries-without-rows or probe-row state reds or fabricates |
| 3 | C / probe | the 4th index row's file exists on disk and the row is byte-equal to it | C06 landed a **labeled probe** in that slot (§0.1) — the sweep alone cannot catch it |
| 4 | C / audit ordering | C05 exists with 4/4 PASS and precedes/cites the landing; C07 exists | both are the round's only absent fragments (§2.5); the claim's own threshold is unmet |
| 5 | Ca / landing | `op/defect-queue-v2.json` exists, sha `3edb4e52…` or re-parsed green | `reports/round-40/op/` does not exist (Ca04 §artifact) |
| 6 | Ca / incorporation | N3/N6/N7 rows present **or** the R02-1 disagreement filed | 33 rows clear ≥28 but fail the incorporation reading (R02-1) — a green would launder it |
| 7 | Ca / adjudication | the R02-4 ruling is in the receipt/round record | Ca01 and Ca03 disagree on R36-D-DECLARATION; unrecorded = absorbed |
| 8 | A / assembly | A03's assembly + PROVINCE sha `05b34a57…` + zero-bleed status check all recorded | the chain is landed but the r40 slice is partial-by-construction until the validation leg closes it (X01 T5) |
| 9 | runner | `reports/round-40/run-validation.py` exists, **relative ROOT**, flags-before-chdir, `runner_sha256` leg, round-specific findings/route, verified in an isolated copy only | absent at baseline; §3.2 shows why "clone the last runner" fails the round six times over |

---

## §8 — Integration order, collisions, owed rows

**Ordering** (X00 §3 is the binding matrix; this seat concurs and adds five pins):

1. Census the wave (24/24 outs, non-empty). Recompute §2.5 — do not trust this count.
2. **C-block first, gated on its verifiers:** C05's 4/4 audit + C07's verify land → integrator
   fixes the four filenames (X00 C1: the E1 conflict is integrator-picked, on the record) →
   **C06 re-derives all four rows from the final set (probe row replaced — §6.2 C4)** → apply
   the 4 entries → apply C06's rev-2.3 delta in the same motion → sweep on the landed tree
   (220/220) → diff landed README vs the corrected draft.
3. **Ca-block (independent):** resolve R02-1 (fold N3/N6/N7 or file the disagreement) and R02-4
   (R36-D-DECLARATION ruling) **before** landing → land `op/defect-queue-v2.json` (byte-identity
   `3edb4e52…` or Ca04 re-parse) → Ca02's sample + K02's cross-check + R02's hunt dispositioned
   on the record.
4. **A-block:** file A03's assembly with the X00 C5 correction and the time-stamped r40 slice;
   fold A02's F-A02-1 route (queue rows per X00 C3(d)/(e) — they join the v2 or the round
   record with owners, per the same filed-row route).
5. Author `reports/round-40/run-validation.py` per **§5** (relative ROOT; runner_sha256 leg;
   round-specific findings/route) — run it in an isolated copy only, per the r39 protocol.
6. Telemetry: `observed-dispatch.json` + `inputs/` (S02 §2), then **`availability-close-40.json`**
   only after `validation.json` lands, sha-pinning `abffc26b…`.
7. SCORECARD row (X01 F1 correction) → LOG append (amendment-7 append committed; admission gated
   on step 6) → MANIFEST rounds[] → fleet report (§4). Last, never first.

**Collision surface.** All 24 out paths disjoint by construction (X00 §1). Apply-time
collisions: (i) the four entries + README converge on one corpus surface (C5/C6 chain); (ii) the
E1 filename pick (X00 C1); (iii) canonical-path ≠ out-path for the v2 (byte-identity pin); (iv)
filed-byte immutability everywhere else (CO7). The C↔Ca coupling: A02's F-A02-1 and A01's
durability row are Ca fold-in candidates (X00 C3(d)/(e)) — the integrator reconciles with the
R02-1 ruling, never silently. The A↔runner coupling: the r40 slice's closure **is** the
validation leg (A4).

**Routed ambiguities the integrator must decide, not the runner:**

- The **R02-1 fold-in ruling** (three rows in, or a filed disagreement with owner).
- The **R02-4 R36-D-DECLARATION adjudication** (conservative = carried; r41 flips with the v2 as
  evidence).
- The **E1 filename** (C01's vs K03's; both sort cleanly; basename-couples confusion check
  routed to C05/integrator per X00 C1).
- The **v2 schema string**: Ca01 chose `kotodama-defect-queue-v2`; P01 §2 said "schema
  preserved"; Ca03 left it to assembly, Ca04 checked what landed — the choice is recorded in the
  artifact itself (`schema: kotodama-defect-queue-v2`); the SCORECARD row should name it.
- The **LOG.md amendment-7 append** commits with the round (parent-owned; A01 §4 Owed).

---

## §9 — Telemetry material (S02's draft is the template of record)

`telemetry/dispatch-declared.json` is filed and digest-verified (§1); its `closing_snapshot`
field reads `open-at-seat-close: owed once validation.json lands`. Owed at close (owner:
integrator/orchestrator, per S02 §2–§3): `observed-dispatch.json` (requested allocation
verbatim, separate from observed counters; `launched/completed/failed_workers` filled **only**
from the AgentSwarm result — a landed file proves its seat completed, absence proves nothing),
`telemetry/inputs/claims.json` + `targets.json`, and `availability-close-40.json` (new
append-only file; `closes_sha256` = `abffc26b…` re-verified at close so any later in-place edit
of the declared record is a digest mismatch; `could-not-recover` with owner + reason for
unrecoverable fields — r39's `runtime_concurrency` precedent). Label partial observations
partial; never persist credentials, authorization headers or prompt payloads; the only route
string in the declarations is the lane name `zai-coding-plan`.

---

## §10 — Language and negation posture (binding on every leg)

No leg, fragment, receipt or report in this round asserts promotion, canon, clearance or
closure. Every occurrence of those tokens must be a **negation**, a **routed reference**, or a
**quoted scanner pattern**. Legitimate shapes, all present here: *"No promotion decision is
taken or implied"* (§4 SHONEN draft), *"canon decisions are lore-shokunin's"* (entry drafts'
closing clauses; AGENTS.md), quoted leg names. The r34/r35 scanner's frame rule is the contract:
**token presence alone never fires; only grant/completion frames do.**

---

## §11 — Landed-fragment cross-check (folded, attributed)

**Read in full by this seat:** K01 (census — §3.1 convergence; my §3.2.2 extends its runner
note), K03 (gap scout — C-leg criteria source), Ca03 (receipt — the fold-in inventory and §6
alignment this spec inherits), P01 (plans), X00 (binding matrix — §8 adopts §3), X01 (trades F1
correction adopted at §2.2/§6.4 X6), A01 (per-surface verdicts), A02 (PROVINCE 7/7; F-A02-1),
Ca01 (the v2 draft — §6.3 legs mirror Ca04's checks on its bytes), S02 (telemetry template — §9
is a pointer, not a duplicate), C01 (entry 1 — content audit is C05's, not this dossier's).

**Read in the load-bearing sections:** K02 (§1–§3: queue sha, 24-row census, owner-states,
six-runner streak F39-1), Ca04 (all 20 checks + the `3edb4e52…` landing pin), R02 (§A.1–A.6:
reproductions, R02-1/R02-4), C06 (§0–§1: before-pins, sweep pin, probe disclosure).

**Header-level only (landed after my reads; integrator folds at close):** C02 (E2 at K03's
filename/scope — header confirms), C03 (E3 — header confirms), C04 (E4 — **unread; the probe
replacement depends on it**), A03 (final assembly), R01 (adversarial review). None of these were
verified by this seat beyond their header lines; §6's legs are written to check whatever they
say.

**Dependency state:** moved under this seat all session (S02's samples: 3–4 landed at
14:08–14:09Z; my §2.5 census: 21 at 15:12Z). The absences that bind are C05/C07 — the round's
admission bar ("every claim verifies") cannot be met while claim C's own audit threshold is
open.

---

## §12 — Recompute orders (what the integrator re-derives, never trusts)

1. `git rev-parse HEAD` / `git rev-parse fd55e1f`; `git status --porcelain -uall` (expect only
   round-40 rows + the LOG append, pre-commit).
2. `find reports/round-40 -type f | sort` — the 24/24 census + non-empty check (CO4).
3. `ls corpus/knowledge/linguistics/*.md | wc -l` (21), `find corpus/knowledge -name '*.md' |
   wc -l` (216), `python3 -B reports/round-28/readme/sweep.py` (216/216 green) — pre-apply;
   re-run post-apply (220/220).
4. `sha256sum` the §1 digest block; the Ca01 landing sha vs `3edb4e52…`.
5. `grep -l 'ROOT = "/home/vgpnk' reports/round-*/run-validation.py` — expect **six** today and
   **six** at close (the r40 runner must not appear in that list).
6. `ls reports/round-*/run-validation.py | wc -l` — 34 today, 35 at close.

## Owed

- **`cov/C05-audit.md` + `cov/C07-verify.md`** — the round's only absent fragments; claim C's
  "audit 4/4 PASS pre-landing" threshold is unmet until they land. Owner: C05/C07, then the
  integrator's apply gate (§8 step 2).
- **The C-block apply** — four entries + corrected rev-2.3 delta (probe replaced), sweep green
  220/220. Owner: integrator.
- **The v2 landing + adjudications** — R02-1 fold-in ruling, R02-4 R36-D-DECLARATION ruling,
  byte-identity or re-parse, Ca02/R02 dispositions on the record. Owner: integrator.
- **`reports/round-40/run-validation.py` + `validation.json`** — per §5/§6; never run in-tree;
  isolated-copy verification only. Owner: integrator.
- **Telemetry close** — `observed-dispatch.json`, `inputs/`, then `availability-close-40.json`
  after the receipt lands; LOG admission gated on it. Owner: orchestrator/integrator.
- **Fleet report, MANIFEST rounds[40] (measured 0), SCORECARD row (0), LOG entry (0)** — §4 is
  the draft; all integrator-only writes. The amendment-7 LOG append commits with the round.
- **Not measured by this seat:** the zai batch's launch/completion counters (CO6); the contents
  of C02 (beyond header), C03 (beyond header), C04, A03, R01; whether C05 passes 4/4; the
  integrator's four rulings (E1 filename, R02-1, R02-4, schema note).

## Citations

**Binding rules and this seat's assignment.** `reports/round-40/targets.json:4-9` (shared
rules; `:8` the runner ban), `:3` (seat_count 24), `:166-172` (the S01 row), `:12-179` (all 24
seat rows; C05 `:75-81`, C06 `:82-88`, C07 `:89-95`, Ca01 `:96-102`, K02 `:19-25`, A01
`:124-130`, A03 `:138-144`, R02 `:152-158`); `reports/round-40/claims.json:7-8` (baseline,
dispatch), `:9-11` (axes/lowest-axis/pause), `:13-18` (C), `:19-24` (Ca), `:25-30` (A),
`:32-33` (non_goals); `REGIMEN.md:17` (rows 7–8: zai/glm-5.3-flash MAX, 16–32, build), `:23`
(r46 read-only audit), `:32-33` (freshness pause), `:42-43` (never force a pass), `:25-50`
(per-round contract); `AGENTS.md` (telemetry availability/dispatch rules; close-what-you-open;
workers write assigned fragments only).

**Measured by this seat.** §1 state pins (`git rev-parse HEAD`, `git rev-parse fd55e1f`,
`git diff --name-status fd55e1f` → `M LOG.md`, `git status --porcelain -uall`, `date -u
+%FT%TZ` → 15:12:09Z); §1 digest block (`sha256sum` ×7; sweep `readme_sha256`); §1 before-state
(`ls corpus/knowledge/linguistics/*.md | wc -l` → 21; `find corpus/knowledge -name '*.md' | wc
-l` → 216; `python3 -B reports/round-28/readme/sweep.py` → exit 0, 216/216, footer
[21,23,25,29,24,94]); §0.4/§3.2 (`grep -l 'ROOT = "/home/vgpnk' reports/round-*/run-validation.py`
→ r34–r39; `ls reports/round-*/run-validation.py | wc -l` → 34; `sed -n '2p;5p;12p;84,88p'
reports/round-39/run-validation.py` → stale docstring/ROOT/RENDERER line/route_deviation dict);
`grep -c "round-40\|Round 40" SCORECARD.md LOG.md` → 0/0; `grep -c '"round": 40'
MANIFEST.json` → 0; `ls .ufo/reports/round-40` → absent (r39 present); §2.4 census (json read
of targets.json); §2.5 (`find reports/round-40 -type f | sort` → 24 files at 15:12:09Z);
LOG.md diff read (amendment 7, 10 lines, `:3763-3771`); `head -3` C02/C03 headers; Ca01/Ca04/
K02/R02/C06 section reads (§11).

**Source lines (read, not executed).** `reports/round-39/run-validation.py:2,5,12,13,84-88,137`
(stale docstring, absolute ROOT, RENDERER line at :12, chdir at :13, r38 route text, `3[0-7]`
regex), `:126` via Ca01/R02 (`runner_sha256: null`; r38 at `validation.json:130`);
`reports/round-33/run-validation.py:23` (relative-ROOT shape, via r39 S01 §5); `reports/round-
39/telemetry/observed-dispatch.json` (zai 16/16, via R02 §A.2); `reports/round-28/readme/
sweep.py:28-30,76,257,284,397,421` (read-only contract; selftest write sites, via C06 §1);
`corpus/README.md:5-10` (rev 2.2; via A01/K01/P01/C06); `reports/round-37/op/defect-queue.json:
5-10,11-252` (notes, 24 rows); `reports/round-34/handoff/declared-in-r7/expected.json:125` (pin
style, via X01 T1).

**Round-40 fragments folded** (full reads unless noted): `scout/K01-touched-census.md`;
`scout/K03-gaps.md`; `scout/K02-queue-scout.md` (§1–§3); `calib/Ca01-queue-v2.md`;
`calib/Ca03-receipt.md`; `calib/Ca04-consistency.md` (§1–Owed); `adj/A01-audit.md`;
`adj/A02-province.md`; `plan/P01-plan.md`; `cross/X00-connector.md`; `cross/X01-trades.md`;
`review/R02-review.md` (§A.1–A.6); `cov/C01-entry-1.md`; `cov/C06-delta-receipt.md` (§0–§1);
`scribe/S02-telemetry-draft.md`; headers only: `cov/C02-entry-2.md`, `cov/C03-entry-3.md`.
Not read: `cov/C04-entry-4.md`, `adj/A03-verify-assembly.md`, `review/R01-review.md` (landed
after this seat's reads; explicitly carried as §11 header-level folds).

**Prior-round precedent reviewed.** `reports/round-39/scribe/S01-integration-draft.md` (the
dossier shape, §5 constants table, §6 leg format, §7 non-vacuous tests — this file's direct
template); `reports/round-39/run-validation.py` (the runner to differ from); `reports/round-38/
cross/X01-trades.md:365-370` (the relative-ROOT ruling, via Ca01/K02).

---

*This dossier claims no promotion, no canon, no clearance and no closure. It is integration
material: a fleet-report draft, a leg specification the integrator implements, and the
recorded-state baseline a close-time runner asserts against. A green gate is a measurement, not
a verdict, and a draft is not a landed change.*
