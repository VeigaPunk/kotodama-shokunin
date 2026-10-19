- Seat: R06 | reviewer | C | date 2026-10-19 | baseline da68a6d

# R06 — adversarial review of the C block (survey fidelity, reissue accuracy, receipt durability)

**Mission** (`reports/round-34/targets.json`, seat R06): "Adversarial review of the C
block: survey fidelity, reissue accuracy, receipt durability (re-runnable?)."

**Method / window.** 2026-10-19T07:0xZ–07:2xZ, repo root, lane HEAD
`da68a6d705e41f369f21e8607bfaab5b54077f84` (`git status --porcelain` → only
`?? reports/round-34/`, so every measurement is at filed bytes). Everything below is my
own re-measurement plus falsification probes; I did not reuse any C seat's comparator. No
filed byte was written; no `reports/round-*/run-validation.py` was executed (F-C13-1).
The C fragments landed **during** this review and the wave kept writing, so each verdict
names the tree state it is pinned to.

**Dependency state at my reads.** Landed and read in full: `scout/K04-anchor-census.md`,
`calib/C01,C02,C04,C05,C06,C07,C08,C09`, `scribe/S03-c-receipt.md` (landed mid-review).
**Absent: `calib/C03-anchor-reissue.md`** (the reissue table itself) and the whole
`reports/round-34/craft/` directory, i.e. *neither durable artifact of claim C exists yet*.
`review/R07-c-review.md` was not on disk either. Owed list in `## Owed`.

## 0. Verdict summary (per surface this seat was asked to review)

| surface | verdict | basis |
|---|---|---|
| survey fidelity | **PASS with one named scope limit** — 28/28 reproduced at `f9bd07c2…`; the count is a `tools/*.py`-scoped statement and misses 4 resolvable non-`tools/` `.py` names, three of them the F-C13-1 runner class (R06-F1) | §1, §2 |
| C02 row-level fidelity | **PASS** — my independent validator: named set, per-row `lines[]` (duplicate same-line occurrences included), all 28 file digests, tool digest, exit code and `survey_stdout` all equal live bytes | §1, §4.1 |
| reissue accuracy | **CANNOT-VERIFY as landed** — C03 is absent, so the claim's "reissue table lands, each verified by grep" clause is unmet. The ground truth the table must equal is independently confirmed here and agrees with C08/K04; the table's **row classes** need correction (R06-F2/F3) | §3 |
| receipt durability (re-runnable?) | **PASS on content / NOT LANDED.** C02's JSON is re-runnable and self-binding; it lacks an expected-digest pin, and the receipt half of the pair has **no fixed filename** (`to-verify` in C06 §1) | §4 |

## 1. What I reproduced independently

| check | command | result |
|---|---|---|
| survey at HEAD | `python3 -B reports/round-30/craft/box1-survey.py` | **exit 0**; `named 28`, `resolvable 28`, `unnamed_in_skill []`, `skill_sha256 f9bd07c2bd134623…`; `date` field reads `2026-10-18` (script-hardcoded) |
| SKILL.md at HEAD | `sha256sum SKILL.md`; `wc -l` | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`, **732** lines |
| pre-edit revision | `git show 139e3b6:SKILL.md \| sha256sum` / `\| wc -l`; same for `17e90b9` | both `79fe91d3d42917a1…`, **715** lines — the claim's 715→732 movement is real and the pre-edit blob is the same at both revisions C08 uses |
| age of the digest chain | `sha256sum reports/round-30/craft/box1-survey.py` | `d923ae0fcd544513…` (matches C02's `survey_script_sha256`) |
| AGENTS.md | `git show --stat da68a6d -- AGENTS.md`; `wc -l AGENTS.md`; `grep -n "SKILL" AGENTS.md` | 2 deletions; **40** lines; grep **no match** (exit 1) |
| anchor map | `difflib.SequenceMatcher(None, 139e3b6:SKILL.md, SKILL.md)` + per-line content probes | Δ=0 for every anchor ≤584; `:660→:662`, `:710→:726`, `:713→:729`, `:714-715→:730-732`; probes: old-660 content → new line `[662]`, old-710 → `[726]`, old-713 → `[729]` |
| old vs new audit payloads | both one-liners extracted and executed verbatim (read-only) | old (`17e90b9:715`) → **exit 0, prints 5 records** (`round-19,25,26,27,28/availability.json`); new (`SKILL.md:732`) → **exit 0, prints nothing** — independent reproduction of C08 §5 and of round-32 F-X16-3 |
| C08's era blobs | `git show <rev>:SKILL.md \| sha256sum` / `\| wc -l` | `b02cfbc` → `52d5f4d1…`/305; `16652e8` → `e8d238a6…`/375; counterexample addresses `17e90b9:157,205,208,262,278,323` carry unrelated content — C08-F1's revision-relativity holds |
| C08-F4 completeness | `grep -n "SKILL\.md:[0-9]" corpus/lessons/README.md` | `:242` cites `SKILL.md:715`; `:244` cites `:713-715` + `:522-534`; `:245` cites `:294` — the three rows are real and outside A09 §2.4 |
| digest supersession census (07:2xZ) | `grep`/scan over all non-`.git`/`.scratch` files, classified filed (r1–33 + corpus) / r34 / root | `79fe91d3…`: 47 total = **31 filed**, 14 r34, 2 root (`LOG.md`, `SCORECARD.md`); `83b0a78a…`: 25 total = **11 filed**, 14 r34; `f9bd07c2…`: 23 total = **1 filed** (`reports/round-33/adj/audit-assembled.md`), 20 r34, 2 root |
| no filed-byte drift | `git status --porcelain -- reports/round-1..33 corpus/lessons tools/gates/frozen` | empty |

**Method note (my own trap, recorded).** My first extraction of the old audit one-liner
chopped the command's closing `"` and produced `exit 2, 0 records` — which would have read
as a C08 contradiction. Re-parsing the line verbatim gave C08's exact result. Recorded
because a reviewer's tooling bug is indistinguishable from a finding until it is re-parsed;
any reader who saw the earlier console should treat it as retracted.

## 2. Survey fidelity — the instrument's measured limits

**F1 (the limit that matters).** `box1-survey.py:6` matches `tools/[\w./-]+\.py` only. I
re-derived the whole `.py` surface named in SKILL.md: 6 further paths are not under
`tools/`, and **4 of them resolve on disk**:

| path named in SKILL.md | SKILL.md line | resolves | note |
|---|---|---|---|
| `reports/round-5/run-validation.py` | :633 | yes | "Round-scoped acceptance is re-runnable with …" — an *instruction to run* |
| `reports/round-6/run-validation.py` | :658 | yes | "Re-run this round's receipt/count/preservation checks with …" |
| `reports/round-7/run-validation.py` | :706 | yes | "5. Run … for the original F/O thresholds …" |
| `reports/round-28/ceiling/measure-ceiling.py` | :383 | yes | the worked-ceiling reader (carries dated pins, see §5 R06-F8) |

The three runners are precisely this round's ABSOLUTE in-tree prohibition class, and
SKILL.md does caveat them at `:711-712` ("run them in a disposable clone: round 5 and round
7 rewrite their own filed `validation.json` in place (round 6 is byte-stable)"). So the
survey is not defective — but **"28/28 named executables resolve" is a scope statement, not
a hazard clearance.** The durable receipt's scope note (C02's `rows_scope_note` names the
regex; good) should additionally name the excluded class and the reason, or a dossier
reader will take 28/28 for "nothing dangerous is named here".

**F2 (dedup, not mention count).** 78 regex occurrences collapse to 28 distinct paths
(`sorted(set(...))` at `box1-survey.py:6`); C07 §2 and K04 §4 agree; I re-derived 78/28.

**F3 (existence, not executability).** 28/28 carry a `#!` shebang, but **22/28 have no exec
bit** — they run via `python3 -B`. The survey's own word is `resolvable`; the claim prose's
word "executable" is loose and should not be tightened into a claim about mode bits.

**F4 (hard-coded date).** `box1-survey.py:8` emits `"date": "2026-10-18"`, so
`python3 … > receipt.json` can never produce a receipt dated in the round-34 window. C02
handles this correctly (keeps `survey_stdout.date` as the script's filing date, carries the
run date in `measured_at_utc`, and states the distinction at its `survey_stdout_note`) — my
probe control 4 (§4.3) shows the naive tee would otherwise fail.

**F5 (no assertion; two reads).** The script's exit is count-only (`:12`) and it reads
SKILL.md twice (`:5` `read_text`, `:10` `read_bytes`), so the counts and the digest come
from two reads (a change between them is unobserved). The filed tool must not be edited
(K04 §2), so the binding belongs in the receipt's verifier — my probe reads once and binds
both.

## 3. Reissue accuracy

**3.1 Row classes — A09's R1–R8 are re-pin items, not anchors.** Only **R5** is a
line-anchor table. R1 is a blob pin, R2/R3 are digest receipt sites, R4 is the box-1
receipt, R6 is README prose arithmetic, R7 is instrument status (x45/x57), R8 is landing
order. A single "old anchor → new anchor" table across all eight manufactures addresses for
seven rows; C08 reaches the same conclusion from its own side (`C08:142-149`). The honest
shape is per row: `{A09 row, reading kind, old reading, new reading/state, evidence}`.

**3.2 The shift is non-uniform — any uniform offset is falsified.** Measured: Δ=0 for old
≤584 (`:47`, `:149`, `:183`, `:294`, `:456-458`, `:522`, `:534`, `:535`, `:536`, `:189-214`,
`:575-617` region start), Δ=+2 for 587–707 (`:660→:662`, `:615→:617`, `:612→:614`), Δ=+16
for ≥708 (`:710→:726`, `:713→:729`). Rows that re-issue `round-31.md:46`'s anchors
(`:294`, `:456-458`, `:522`, `:534-536`) as moved would be wrong: those citations are
**still valid**. C08 §2/G-rows and K04 §5 agree to the line.

**3.3 Three rows need a class the claim's wording does not have.**

- `AGENTS.md:42` — **removed, not moved** (verified three ways: 2 deletions at `da68a6d`,
  file now 40 lines, grep exit 1). Reissue value = "site deleted 2026-10-19 (A10-F15
  residue excision); no successor address; the text survives only in filed fragments
  (`reports/round-33/adj/A07-history.md:65`, `reports/round-31/jinii/draft.md:37`)". This
  also means A09-F3 is **closed by deletion** and must be recorded closed, not re-pinned.
- The r31-landed item — **content-changed, not just shifted**: old `:713-715` (3 lines, audit
  globbing `closing-snapshot.json`, which printed 5 records) → new `:729-732` (4 lines, audit
  keyed on `closes`/`closes_sha256` over `availability-close-*.json`, prints 0). A row
  reading `713-715 → 729-732, identical` would hide the substance.
- The r14/r15/r19-era citations — **era-scoped**: `:157`, `:205`, `:208`, `:278`, `:262`,
  `:323` resolve only against `b02cfbc`/`16652e8`, not against `79fe91d3`; a row asserting
  pre-edit resolution for them is false (C08-F1, confirmed §1).

**3.4 Completeness.** `corpus/lessons/README.md:242,244,245` cite stale SKILL anchors and
are outside A09 §2.4 (C08-F4, confirmed). The claim's threshold says the table covers
"every A09 R1–R8 row"; a table that stops at R5 + A09 §2.4 under-covers these three unless
each gets a row or a recorded, owned omission.

**3.5 C03 never landed**, so no row-by-row verdict against a real table is possible — mine
or C08's. `calib/C08-verify-reissue.md` supplied the acceptance checks (its §4 A–F) and the
ground truth instead, which is the correct disposition under the missing-dependency rule;
its `## Owed` still names the C03 comparison.

## 4. Receipt durability

**4.1 C02's content, validated by my own comparator (not C02's).** I extracted the fenced
JSON from `calib/C02-receipt-json.md` and checked it against live bytes:
`28 rows | 78 occurrences | live digest f9bd07c2…` → **PASS** on set equality, every
`line`/`lines[]` (including the three same-line-repeat rows: `check-gate-battery.py`
`[617,617,617]`, `handoff-packet-check.py` `[500,500,612]`, `register-law-gate.py`
`[409,409,410,418,430,439]`), all 28 per-file digests, `survey_script_sha256`,
`rerun_exit_code`, and `survey_stdout` value-equal to a live re-run. One WARN: no
`expected_skill_sha256` pin.

**4.2 What the landed artifact still needs.**
(a) an `expected_skill_sha256` field so a future re-run can go red without depending on the
fragment's verifier; (b) a **fixed filename for the receipt half**: C06 §1 lists
`reports/round-34/craft/box1-resurvey-receipt.md` as *proposed*, path `to-verify`, and
`skill-anchor-reissue.md` likewise — the integrator must fix both paths before landing or
the claim's "durable pair" clause stays unfalsifiable (R06-F4).

**4.3 Probe (this seat's, key-tolerant — deliberately).** `box1-survey.py`'s emitted key
names (`named`/`unnamed_in_skill`) differ from the filed r30 receipt's
(`named_in_skill`/`unresolvable`), and C02/C07 chose `line`/`lines` vs `first_line`. A probe
demanding one spelling would emit a false RED against a correct artifact, so mine accepts
both spellings per field. Controls run at HEAD:

| control | input | result |
|---|---|---|
| absent receipt | default path (not landed) | exit **2** `RED receipt absent` |
| positive | C02's fragment JSON (as if landed) | **GREEN**, exit 0, 28/28, one WARN (no expected pin) |
| mutated count | C02 JSON with `named_in_skill: 27` | exit **1** `FAIL named_in_skill=27 != re-derived 28` |
| naive tee | verbatim `box1-survey.py` stdout | exit **1** `FAIL date 2026-10-18 predates window; FAIL no re-run handle` |

```python
#!/usr/bin/env python3
"""R06 probe: verify a durable box-1 receipt against live bytes (key-tolerant).
Usage: python3 -B probe.py [RECEIPT]; exit 0 green / 1 red / 2 absent.
Scope: the tools/*.py name class of reports/round-30/craft/box1-survey.py:6."""
import hashlib, json, pathlib, re, sys, datetime
ROOT = pathlib.Path('.').resolve()
REC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'reports/round-34/craft/box1-resurvey-durable.json')
REC = REC if REC.is_absolute() else ROOT / REC
if not REC.is_file():
    print("RED  receipt absent:", REC.relative_to(ROOT)); sys.exit(2)
rec = json.loads(REC.read_text()); fails, warns = [], []
live = hashlib.sha256((ROOT / 'SKILL.md').read_bytes()).hexdigest()
occ = {}
for i, l in enumerate((ROOT / 'SKILL.md').read_text().splitlines(), 1):
    for h in re.findall(r"tools/[\w./-]+\.py", l):
        occ.setdefault(h, []).append(i)
if str(rec.get('skill_sha256', '')) != live: fails.append(f"skill_sha256 != live {live[:16]}")
for k in ('named_in_skill', 'named'):
    if k in rec and rec[k] != len(occ): fails.append(f"{k}={rec[k]} != re-derived {len(occ)}")
if rec.get('resolvable') != len([p for p in occ if (ROOT / p).is_file()]): fails.append("resolvable != re-derived")
if rec.get('unresolvable') or rec.get('unnamed_in_skill'): fails.append("non-empty unresolvable list")
if rec.get('skill_lines') and rec['skill_lines'] != len((ROOT / 'SKILL.md').read_text().splitlines()):
    fails.append("skill_lines != live line count")
rows = {r.get('executable'): r for r in rec.get('rows', [])}
if rows:
    if sorted(rows) != sorted(occ): fails.append("row set != live named set")
    for p, lines in occ.items():
        r = rows[p]
        if r.get('lines') and r['lines'] != lines: fails.append(f"{p}: lines mismatch")
        if r.get('line') and r['line'] != lines[0]: fails.append(f"{p}: first line mismatch")
        if r.get('first_line') and r['first_line'] != lines[0]: fails.append(f"{p}: first_line mismatch")
        if r.get('sha256') != hashlib.sha256((ROOT / p).read_bytes()).hexdigest(): fails.append(f"{p}: sha256 mismatch")
try:
    if datetime.date.fromisoformat(str(rec.get('date', ''))) < datetime.date(2026, 10, 19):
        fails.append(f"date {rec.get('date')} predates the round-34 window")
except ValueError: fails.append(f"date not ISO: {rec.get('date')!r}")
if not any(k in rec for k in ('command', 're_run_command', 'rerun', 'reverify')): fails.append("no re-run handle")
if 'expected_skill_sha256' not in rec: warns.append("no expected_skill_sha256 pin")
for w in warns: print("WARN", w)
for f in fails: print("FAIL", f)
print(f"rows={len(occ)} live={live[:16]}", "GREEN" if not fails else "RED")
sys.exit(0 if not fails else 1)
```

**4.4 The Markdown twin — stated so nobody over-claims a gate.** K04-F2 shows the r30
depth leg's document set is `reports/round-30/**.md` only, so a round-34 `.md` receipt is
**not read by any gate** and does not make the r30 runner green; it is a durability
convention. Writing the twin is still right (the claim's after_required says "+ receipt"),
but no verdict may cite it as a gate input.

## 5. Findings

| id | finding | class | owner | evidence |
|---|---|---|---|---|
| **R06-F1** | The 28-name survey cannot see 4 resolvable non-`tools/` `.py` names, three of which SKILL.md instructs the reader to run (`:633`, `:658`, `:706`) — this round's F-C13-1 prohibition class, caveated only at `:711-712`. The receipt must state the exclusion, or 28/28 reads as hazard clearance. | fidelity gap, no artifact defect | integrator + receipt owner | §2 F1; command output |
| **R06-F2** | A09's R1–R8 are re-pin items; only R5 is an anchor table. An "old anchor → new anchor" table over all eight fabricates addresses for seven rows. | correctness | integrator (C03 owner) | §3.1; `reports/round-33/adj/A09-pins.md:103-116`; `C08:142-149` |
| **R06-F3** | Three reissue rows need classes the claim's wording lacks: `AGENTS.md:42` **removed**; the r31 item **content-changed** (audit 5 records → 0); r14/15/19 citations **era-scoped** (false against `79fe91d3`). | correctness | integrator | §3.3; §1 rows |
| **R06-F4** | Neither durable artifact is landed (`ls reports/round-34/craft` → absent), and the receipt half's filename is `to-verify` in C06 §1. C02's block also lacks an `expected_skill_sha256` pin. | durability | integrator | §4.1-4.2; probe WARN |
| **R06-F5** | `calib/C03-anchor-reissue.md` never landed → the claim's "reissue table lands, each verified by grep" clause and its coverage threshold are unverifiable; the C03-vs-C08 comparison is owed. | missing dependency | integrator / re-dispatch | §3.5; `C08 ## Owed` |
| **R06-F6** | The claim's before-state names only `79fe91d3…`, but the filed box-1 receipt's own old reading is `83b0a78a…` (11 filed paths). R4's row must carry the two-generation chain `83b0a78a → 79fe91d3 → f9bd07c2`. C02's `provenance.supersedes` does name both — keep it; do not let the claim prose drop it. | completeness | integrator | §1 census; `reports/round-30/craft/box1-landed-survey.json:4` |
| **R06-F7** | The C scribe's census is self-contradictory and its count disagrees with mine: S03 R3 says "32 filed files carry `79fe91d3`, … **zero filed files carry `f9bd07c2`**" and then names round-33's filed `adj/audit-assembled.md` in the same cell. Measured: **31** filed r1–33/corpus files carry `79fe91d3`, and `f9bd07c2` has **exactly one** filed hit — `reports/round-33/adj/audit-assembled.md`. The census must state its predicate and timestamp (the r34 count grows as fragments land: 14 at my read). | count accuracy | S03 owner + integrator | §1 census; `reports/round-34/scribe/S03-c-receipt.md:110` |
| **R06-F8** | SKILL.md's own dated digest pins are invisible to the 28-row survey and to any "box-1 evidence is current" claim: `:383` pins packet `543d68a8…` while live `examples/culture-d4/packet.d4.yml` is `aac91246…` (gate `b5406bcd…` still reproduces); `:271` cites commit `46a03257` (exists); `:288` cites `a3aa452c…` (live `typed-labels.d2.yml` reproduces). Dated readings, no defect claimed — but the receipt's scope note must not be read as covering them. | scope honesty | integrator | §1; `sha256sum` outputs |

## 6. Pre-verification checklist (ordered, for the integrator)

1. Fix the two landed paths (`reports/round-34/craft/box1-resurvey-durable.json` + the
   Markdown receipt's name) and land C02's block verbatim; add `expected_skill_sha256`.
2. Give the receipt a dated command line, the words `executables`/`unnamed`/`inventory`,
   and the full digest as literal text (r30 leg's `dated_command`/digest convention,
   `reports/round-30/run-validation.py:328-329,674-685`) — convention, not a live gate.
3. Run the §4.3 probe; wire it as a third counting command (or a `tools/` checker) so claim
   C can actually fail on a bad receipt — as declared, `box1-survey.py` alone cannot.
4. Land C03's table using §3.1's row classes and §3.2's measured Δ map; include §3.4's three
   README rows or record the omission with an owner.
5. Apply C08 §4 checks A–F to C03 and file any row discrepancy as a finding.
6. File R1–R3/R4/R6/R7 supersession rows as **new rows** (never edits); keep
   `git status --porcelain -- reports/round-1..33 corpus/lessons tools/gates/frozen` empty
   at close.

## Owed

- `reports/round-34/calib/C03-anchor-reissue.md` — absent at every read this seat made
  (`ls reports/round-34/calib/` → C01, C02, C04, C05, C06, C07, C08, C09). The row-by-row
  reissue verdict is therefore owed: apply C08 §4 checks A–F against the §3 ground truth
  (which R06 and C08 independently agree on) once C03 lands.
- `reports/round-34/craft/box1-resurvey-durable.json` and its receipt (directory absent) —
  the durability clause is unverifiable until landed; the §4.3 probe is ready to run and
  goes green on C02's content plus the pinned fix from §4.2.
- `reports/round-34/review/R07-c-review.md` — the peer C review (cross-check against A09's
  R1–R8 coverage) was not on disk at my reads; not consumed, no verdict from it folded here.

## Citations

- Seat/mission: `reports/round-34/targets.json` (seat R06, `shared_rules`, missing-dependency
  rule); claim C: `reports/round-34/claims.json:53-66`; `REGIMEN.md`.
- Survey tool: `reports/round-30/craft/box1-survey.py:4,5,6,7,8,10,12` (sha256
  `d923ae0fcd544513…`); prior receipt `reports/round-30/craft/box1-landed-survey.json:4-6`
  (`83b0a78a…`); consumer convention `reports/round-30/run-validation.py:44-45,290-303,328-329,
  674-685,697-703`; `reports/round-30/craft/review-D29-box1.md:162-167`.
- Claim-C fragments read: `reports/round-34/scout/K04-anchor-census.md` (§2, §4, §5, §6, §7);
  `calib/C01-survey-run.md` (§2, §3); `calib/C02-receipt-json.md:26-52,58-362,365-395,406-419`;
  `calib/C04-byte-check.md:22,37,51,56,86,133,152-158`; `calib/C05-receipt.md:42,46,48,50,224`;
  `calib/C06-scribe.md:17-23,36-48,123,141`; `calib/C07-verify-survey.md` (§3 controls, §5, §7);
  `calib/C08-verify-reissue.md:22-27,38-54,63-95,96-116,118-129,142-149`; `calib/C09-final-receipt.md:5,15,17,25,52-59`;
  `scribe/S03-c-receipt.md:105-125`.
- A09/A33 sources: `reports/round-33/adj/A09-pins.md:20,38-41,55-101,103-116,124,128-136`;
  `reports/round-33/adj/audit-assembled.md:30,43`; `reports/round-32/final-dossier.md:46,133`;
  `reports/round-26/run-validation.py:90,96-97,1494-1510,1909`; `reports/round-30/validation.json:449`.
- Live surfaces: `SKILL.md` (sha256 `f9bd07c2…`, 732 lines) lines
  `:47,128,149,183,221,271,288,294,383,456-458,486,488,501,522,534-536,633,658,660,662,706,710-712,726,729-732`;
  `AGENTS.md` (40 lines, no `SKILL` match); `corpus/lessons/round-31.md:46`; `round-32.md:7,33,41,55,57,58`;
  `corpus/lessons/README.md:242,244,245`; `LOG.md:3577`; `SCORECARD.md:599`.
- Commands (2026-10-19T07:0xZ–07:2xZ, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD`; `git status --porcelain`; `git show 139e3b6:SKILL.md | sha256sum` / `| wc -l`
  (and `17e90b9`, `b02cfbc`, `16652e8`); `sha256sum SKILL.md AGENTS.md reports/round-30/craft/box1-survey.py`;
  `wc -l SKILL.md AGENTS.md`; `grep -n "SKILL" AGENTS.md`; `git show --stat da68a6d -- AGENTS.md`;
  `python3 -B reports/round-30/craft/box1-survey.py`; python DID/difflib anchor-map script over
  `139e3b6:SKILL.md` vs `SKILL.md` + content probes; python regex census of `.py` names not under
  `tools/` with `is_file()`; shebang/exec-bit scan of the 28; verbatim execution of the two audit
  one-liners (`17e90b9:715` → exit 0/5 records; `SKILL.md:732` → exit 0/0 records);
  `grep -n "SKILL\.md:[0-9]" corpus/lessons/README.md`; digest census scan over all non-`.git`/`.scratch`
  files classified filed/r34/root; `sha256sum examples/culture-d4/packet.d4.yml tools/d2-typed-labels.py
  examples/culture-d2/typed-labels.d2.yml tools/gates/argot-derivation-gate.py`; `git cat-file -t 46a03257`;
  R06 probe `box1_receipt_verify`/`probe2.py` with four controls (absent → 2, C02 JSON → 0 + 1 WARN,
  mutated count → 1, verbatim tee → 1); R06 comparator `validate_c02.py` over
  `calib/C02-receipt-json.md`'s fenced block.
- Scratch (not durable): `.scratch/r06/{SKILL.old.md,SKILL.new.md,probe2.py,validate_c02.py,landed.json,good.json,badcount.json,verbatim.json}`.
