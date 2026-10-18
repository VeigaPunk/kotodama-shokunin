# R27-O39..O40 — adversarial review of the round-27 pin sweep

- **Seat:** O, round-27 claims **R27-O39..O40** (reviewers x2), assignment verbatim:
  "adversarial on the sweep (a stale row left behind? a re-pin touching filed bytes?)".
- **Date:** 2026-10-18. Observation window **19:12Z–19:27Z** (all stamps from
  `date -u --iso-8601=seconds`; `python3` 3.14.7). Lane HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` (round-27 declaration, 16:11:04−03:00);
  declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`reports/round-27/claims.json:5`).
- **Write scope:** this file only. Scratch under `.scratch/r27-o39/` (gitignored,
  lane-internal); `export TMPDIR=$PWD/.scratch; export PYTHONDONTWRITEBYTECODE=1`
  preceded every scratch-writing command, and **`TMPDIR=/tmp/r27o39` (outside the
  repo) was used for every `replay-frozen` / mirror-launching run** — §5 is why.
  No git commit or push. No filed round-8–26 byte, tool, gate, packet or shared
  bookkeeping was edited by this seat. This seat created no clones.
- **Canon:** NON-CANON engineering evidence. This review admits nothing, certifies
  no round, and adjudicates no claim. It measures the sweep against the claim's own
  `after_required` text and reports what it found.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | **no filed byte moved**: 1 460 tracked protected paths (rounds 8–26 + their frozen generations) are blob-identical to the declared baseline; `git diff --name-status 4f09c99 HEAD` adds only round-27's two declaration files | measured |
| 2 | the sweep's own new rows **did not edit any filed row** — every re-pin is a new file under `reports/round-27/`; `git status` over the frozen/expected surface is empty | measured |
| 3 | **the sweep's new rows went stale before the round closed.** The D4 packet moved **three times** in round 27 (`dd25077b…` → `c5441e3d…` at 16:23:21 → `86079a67…` at 16:24:45). The O seat froze `v3-baseline-r27` at 16:19:41 against `dd25077b…` and `frozen/r27-post` at 16:21:44 against `c5441e3d…`; **both** are red against the live bytes | **measured — the load-bearing finding** |
| 4 | `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` replays **2 mismatch, 0 reproduced of 2** (exit 1) | measured |
| 5 | `reports/round-27/pinsweep/v3-baseline-r27/expected.json` — the sweep's *own* successor v3 row — is **5 D4 rows stale**; `--profile v3 --quiet` exits 1 against it **and** against the default (which is also 5 rows stale) | measured |
| 6 | the round-27 runner's filed receipt records **`acceptance_checks_passed: false`** with **5 O-leg failures** — 3 real (drifted D4 surfaces un-re-pinned) and 2 spurious (§4.1); the receipt is being re-run live and the counts move with each O write | measured |
| 7 | the runner **could not** read its own battery: `run_receipt` tailed stdout to 7 000 bytes; the battery emits 29 162, so `strict_json` failed and every battery field read `null` → two spurious O failures. **Fixed mid-wave at 16:28:40**; the battery is green (`pass 7 / fail 0 / unevaluable 0`, coverage 9/9) | **instrument defect — repaired during the wave** |
| 8 | X61's `tmpdir_probe` **does** pass `tmpdir` through (line 448) and produces two distinct tallies — the peer X60 docstring asserting a no-op probe is **stale as of the X61 revision on disk** | measured |
| 9 | the sweep left a **stale generation** behind: `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` is orphaned (2 mismatch). It **is** named and dispositioned in the round-27 prose (`adjacency.md:198`, `report-draft.md:171`), but **no `freeze-receipt.json` declares it superseded** — it is retired by mtime convention | measured |

**Bottom line for the parent.** The *shape* of the O claim is right on the two
questions this seat was asked. **No re-pin touched a filed byte** (findings 1–2, both
directions controlled). But the answer to "a stale row left behind?" is **yes, and the
worst one is the sweep's own**: the D seat's register-law landing moved the D4 packet
twice *after* the O seat froze its rows, so the round-27 re-pin generation
(`r27-post`, 2 mismatch of 2) and the round-27 v3 successor row (`v3-baseline-r27`, 5
stale D4 rows) are **both red** at this stamp — and so is the default v3 baseline. The
runner's receipt agrees: `acceptance_checks_passed: false`, with `handoff-v3 exit 1`
and `3 drifted D4 surface(s) not re-pinned` among its O failures. This is the
**round-26 failure repeating**: there the D write moved the O rows; here the D write
moved the O rows again, within three minutes of their landing. The axis order — D
before O — is structurally wrong for a round whose D work rewrites the surface O pins.

**Two credits, recorded plainly.** (i) The O seat caught and fixed the runner's
battery-capture defect within the wave (16:28:40), and the battery is green. (ii) The
O seat's prose names the orphaned `round-26/gate-input` generation and proposes its
disposition. Neither removes the load-bearing finding: at this stamp the sweep's own
successor rows do not replay, and the O claim's `after_required` is not met.

## 1. The two questions, answered directly

### 1.1 "A re-pin touching filed bytes?"

**No.** Measured two ways, at 19:14Z and re-confirmed at 19:26Z:

| check | command | result |
|---|---|---|
| protected blob identity | `git ls-tree -r <baseline>` vs `HEAD` over `reports/round-{8..26}` + `tools/gates/frozen/round-{8..26}` | **1 460 paths: 0 changed, 0 missing, 0 added** |
| tracked diff vs baseline | `git diff --name-status 4f09c99 HEAD` | only `A reports/round-27/{claims,targets}.json` |
| tracked diff vs HEAD | `git diff --name-only HEAD` | **0** at 19:14Z (round-27 writes were still landing; see the correction below) |
| frozen/expected surface | `git status --porcelain -- tools/gates/frozen tools/gates/expected` at 19:14Z and 19:27Z | empty — **no frozen manifest, baseline or receipt was edited** |

**Correction, measured 19:27Z.** A later `git status` shows the round-27 **D** seat's
writes as uncommitted modifications: `examples/culture-d4/{packet.d4.yml,
packet.d4.typed.yml, typed-labels.d4.yml, expected-holds.json, components/01-brief.yml}`
plus `tools/gates/argot-derivation-gate.py` and `tools/gates/typed-pipelines.json`, and
a new untracked `examples/culture-d4/components/13-register-law.yml`. Those are
round-27 D-claim writes to `examples/` and `tools/`, **not** edits of a filed round-8–26
row — and the protected-surface check in the row above (1 460 paths, 0 changed) is what
establishes that. This is the same D landing §3 shows moving the packet under the O
rows. The filed-row claim is unchanged; the "empty working tree" phrasing was true at
19:14Z and is not true once the D writes landed.

The one class this seat cannot clear from Git alone is `reports/round-27/pinsweep/**`,
which is untracked — but it is a *new* path, so by construction it cannot be a filed
row. **No filed row was edited in place.** The append-only convention holds.

### 1.2 "A stale row left behind?"

**Yes — four, in two classes.** §3 and §4 give the measurements.

## 2. The sweep's surface, and what it actually reaches

Two O instruments landed and both were run by this seat:

| instrument | seat | exit at 19:26Z | reading |
|---|---|---:|---|
| `reports/round-27/audit/x61-pin-sweep.py` | R27-X61 | **2** | 50/81 rows reproduced, 6 mismatch, 25 could-not-evaluate; baselines 6/6 pinned |
| `reports/round-27/audit/o37-sweep-inventory-audit.py` | R27-O37 | **1** | 26 D4-pinning surfaces: **9 swept, 17 MISSED** |
| `reports/round-27/audit/x60-sweep-completeness.py` | R27-X60 | — | measures the same coverage question by class |
| `reports/round-27/audit/x62-frozen-record-audit.py` | R27-X62 | **0** | 11 generations, 81 rows: 0 record findings, 0 receipt findings |

X61 walks only families **A** (frozen `MANIFEST.tsv`) and **B** (`tools/gates/expected/**`);
O37's census says the D4 pin surface also lives in families **C** (13 files), **D** (4),
**E** (12), **F** (1), **G** (2), **H** (7) — **17 of 26 D4-pinning surfaces un-swept**.
O37's own receipt, updated during the wave, now reads **29 surfaces, 24 missed**.

This seat verified O37's three highest-value misses independently, without trusting
its verdicts:

| family | surface | this seat's independent measurement |
|---|---|---|
| E | `reports/round-20/handoff/expected.json` | **3/3 D4 rows stale** (`e7ecd204…` vs live) |
| E | `reports/round-22/handoff/declared-in-r2/expected.json` | **3/3 stale** |
| E | `reports/round-26/handoff/declared-in-r5/expected.json` | 0 stale at 19:16Z — **5 stale at 19:26Z** (§3.2) |
| H | `reports/round-26/remainders/r4-twin/twin.json` | **6/6 D4 rows stale**; `packet_links` exit 1, 6 × `M-DIGEST-MISMATCH` |
| D | `tools/gates/frozen/round-26/post-register/freeze-receipt.json` | 4/4 pins **OK** (not stale, despite being un-swept) |

The instrument-scope asymmetry is real and worth naming: X61's baseline duty covers
**6** baselines; `tools/check-gate-battery.py`'s `BASELINE_ROOTS` covers **19**. A
sweep that reports "baselines 6/6 pinned" is reporting on a third of the baseline
surface.

## 3. The load-bearing finding — the D4 packet moved under the O rows

### 3.1 Timeline (all stamps `stat`, local −03:00)

| stamp | event | D4 `packet.d4.yml` |
|---|---|---|
| 15:22:07 | round-26 `post-register` generation frozen | `dd25077bc01681bc…` |
| 16:19:41 | round-27 O seat freezes `pinsweep/v3-baseline-r27/` | (reads `dd25077b…`) |
| 16:21:44 | round-27 O seat freezes `pinsweep/frozen/r27-post/` | `c5441e3d0b237f33…` |
| 16:23:21 | **D seat writes the register-law into the packet** | `c5441e3d…` |
| 16:24:34 | D seat lands `components/13-register-law.yml` | — |
| **16:24:45** | **D seat re-writes the packet again** | **`86079a6708a0d360…`** |

The D4 packet is now at its **third** digest of the round. `components/01-brief.yml`
also moved (`feca7bda…` → `649aa111…`), and `tools/gates/argot-derivation-gate.py`
moved twice (`5b5abe78…` → `b5406bcd…`).

### 3.2 The consequence, measured

Live D4 digests at this seat's closing stamp (**19:28Z**, `sha256sum`, cwd = lane root;
`TMPDIR=/tmp/r27o39`, `PYTHONDONTWRITEBYTECODE=1`):

```
86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc  examples/culture-d4/packet.d4.yml
88a94422b4123f6b436f9935590d69f081f90e688655ee605f33e0c1305fb68d  examples/culture-d4/typed-labels.d4.yml
857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f  examples/culture-d4/expected-holds.json
1c4b88088b696a131f71af69ad14dda518acdec83dc7e873cfcad6fae5fc2660  examples/culture-d4/packet.d4.typed.yml
649aa111db2e57a737234330690ea4fbb197039ba8ecf92d6248d1bed8ea793b  examples/culture-d4/components/01-brief.yml
d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240  examples/culture-d4/components/04-lexicon.yml
```

| round-27 O row | frozen against | live | verdict |
|---|---|---|---|
| `pinsweep/frozen/r27-post/MANIFEST.tsv` row 2 (`typed-labels.d4.yml`) | `072fa806…` | `88a94422…` | **mismatch, exit 1** |
| `pinsweep/frozen/r27-post/MANIFEST.tsv` row 3 (`packet.d4.yml`) | `c5441e3d…` | `86079a67…` | **mismatch, exit 1** |
| `pinsweep/v3-baseline-r27/expected.json` | 5 D4 rows | — | **5 rows stale** |
| `round-26/handoff/declared-in-r5/expected.json` (the **default** v3 baseline) | 5 D4 rows | — | **5 rows stale** |

Commands and results:

```
python3 tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv
# REPLAY MISMATCH: 2 mismatch, 0 reproduced of 2 row(s)   [exit 1]   (19:26Z)

python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
# handoff-v3: exit=1 ... packet_sha256=(not assembled)     [exit 1]   (19:26Z)

python3 tools/exercise-handoff-e2e.py --profile v3 --quiet \
  --baseline reports/round-27/pinsweep/v3-baseline-r27/expected.json
# handoff-v3: exit=1 ... packet_sha256=(not assembled)     [exit 1]   (19:26Z)
```

The second and third commands are the decisive pair: **the sweep's own successor v3
row is no greener than the row it was meant to supersede.** The re-pin did not close
the tail; it reproduced the tail on a newer digest.

The direct cause is not a mistake in the O seat's method — the row was correctly
frozen as a **new generation** (§4.2). It is that the **D seat kept writing the pinned
surface after the O freeze**. The D4 packet is *derived*: `tools/assemble-culture-d4.py`
assembles it from `components/*.yml`. Any component write moves the packet, and
therefore every packet pin in the lane.

### 3.3 The runner already says this

`reports/round-27/validation.json` is being **re-run live** while this review is
written; the numbers below are the reading at 19:26Z (`measured_at_utc
2026-10-18T19:27:19+00:00`, `runner_sha256 2c3a69b89d9f…`). An earlier read of the same
file (16:23) gave `drift 93 / green 139 / 5 drifted surfaces`; this read gives
`drift 92 / green 140 / 3 drifted surfaces` — the O seat is closing surfaces as the
round continues. **The receipt is a moving target; the stamp is the claim.**

```
acceptance_checks_passed: false
claim O failures (3):
  * 3 drifted D4 surface(s) are not re-pinned by a round-27 row carrying the live digest:
    ['examples/culture-d4/components/01-brief.yml', 'examples/culture-d4/packet.d4.typed.yml',
     'examples/culture-d4/typed-labels.d4.yml']
  * replay handoff-v3 is not green (exit 1)
  * Regression failed: python3 tools/exercise-handoff-e2e.py --profile v3 --quiet (exit 1, 2026-10-18)
```

Its sweep leg counts **232 D4-pinning rows, 92 drifted, 140 green**. The runner's
`after_required` clause — "drifted rows re-pinned as NEW rows; battery 9/9, d4 gate
(with register leg) green, all replays green" — is **not met at this stamp**, and the
runner is honest about it. **The O claim fails on its own instrument's receipt.**

**The receipt moved while this review was being written, and two of the three earlier
failures were repaired.** The 16:23 read had **5** O failures including the two
battery ones; the 16:28:22 read has **3**. The battery failures are gone because the
O seat fixed `run_receipt` (§4.1) — the battery now parses as `pass 7 / fail 0 /
unevaluable 0`, `coverage 9/9`, `baselines_found 19`. The surviving three are the
real ones. The earlier 5-surface drift count also fell to 3 as the O seat re-pinned
surfaces. Every count in this review therefore carries its stamp; §4.1 and §4.2
describe defects that were **live when measured and fixed before this review was
filed**, and are reported as history, not as open items.

## 4. Instrument defects found (adversarial, both directions controlled)

### 4.1 The runner could not read its own battery — two O failures were spurious (now fixed)

**Status: fixed mid-wave at 16:28:40; reported as history.** At the time this seat
first read it, `reports/round-27/run-validation.py` tailed captured stdout:

```python
def run_receipt(item):
    return {key: (value[-7000:] if key == "stdout" else value[-2000:] ...
```

The current revision replaces that with a 40 000-byte head cap plus an explicit
`strict_json` parse:

```python
receipt = {key: (value[:40000] if key == "stdout" else value[-2000:] ...
```

The defect and its measurement, at the stamp that had it:

| run | command | result |
|---|---|---|
| direct | `python3 tools/check-gate-battery.py` | 29 162 bytes; `summary {pass: 7, fail: 0, unevaluable: 0}`, coverage **9/9** — **green** |
| via runner (16:23) | `reports/round-27/validation.json` → `claims.O.measurement.battery` | all fields `null`; `summary {}`; `exit: 0` |
| control | `json.loads` on the stored 7 000-byte row | fails to parse (last-7 000-byte slice begins mid-array); the same slice of a fresh output fails `Extra data: line 1 column 40` |

So "the battery reports pass=None" and "coverage is None, not 9/9" were **defects of
the runner's capture**, not findings about the battery — **the battery was green
throughout**. The fix is confirmed by the 16:28:22 receipt, which now records
`pass 7 / fail 0 / unevaluable 0`, `coverage 9/9`, `baselines_found 19`, `pinned 19`.
**Credit where due: the O seat caught and fixed this within the wave.** It remains
worth recording because the two spurious failures sat in the same list as the real
ones, and a reader taking the 16:23 receipt at face value could not tell them apart.
(Round 26's scribe recorded the same class of complaint about this runner's control leg.)

### 4.2 X60's docstring accuses X61 of a defect X61 no longer has

`reports/round-27/audit/x60-sweep-completeness.py:39-42` states the X61
`tmpdir_probe` "never passes its `tmpdir` argument through to the mirror". On the
X61 revision on disk, it does:

```python
# x61-pin-sweep.py:448
item = verify_row(row, manifest.parent, tmpdir=tmpdir)
```

and the probe produces **two distinct tallies**, which a no-op could not:

```
TMPDIR probe on tools/gates/frozen/round-26/post-register/MANIFEST.tsv:
  inside-repo:  0 reproduced, 0 mismatch, 6 could-not-evaluate (6 mirror_unsafe)
  outside-repo: 4 reproduced, 2 mismatch, 0 could-not-evaluate (0 mirror_unsafe)
```

X61's own `x61-pin-sweep.md:43` discloses that two peer auditors caught the first
draft's defect and that it is fixed. **X60's docstring was not updated to match.**
This is a stale cross-reference between two round-27 instruments — a small
instances of exactly the class the round is sweeping for. (X61 was also rewritten
**mid-wave** at 16:15, which is why an earlier run by this seat read a `not-pinned`
baseline that the current revision reads `pinned` via its new `implied_gate`
fallback; both readings were re-measured after the rewrite.)

## 5. The TMPDIR trap — the sweep's honesty depends on one env var

The regimen mandates `export TMPDIR=$PWD/.scratch` before scratch-writing commands.
`tools/replay-frozen.py:175-177` refuses any mirror inside the repo:

```python
if real_mirror == root or root in real_mirror.parents:
    raise RowError("mirror_unsafe", ...)
```

Measured consequence, same manifest, one variable changed:

| TMPDIR | replay of `round-26/post-register/MANIFEST.tsv` |
|---|---|
| `$PWD/.scratch` (the mandated setting) | `6 could-not-evaluate, 0 reproduced` — **every row void** |
| `/tmp/r27o39` (outside) | `4 reproduced, 2 mismatch` — the real verdict |

A sweep run under the mandated TMPDIR would report **0 reproduced across all 81 rows**
and look like total failure. Both X61 and the round-27 runner document and control for
this, and both were run by this seat with TMPDIR outside the repo. **This is the
single highest-leverage environment fact in the round** and it is worth promoting to
the knowledge corpus rather than leaving in three separate scratch notes.

## 6. The stale rows the round leaves behind

| row | state | why it is stale | declared superseded? |
|---|---|---|---|
| `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` | 2 mismatch of 6 | pins pre-register D4 inputs (`e7ecd204…`, `ffece0fe…`) | **no** — both `gate-input` and `post-register` receipts point their `supersedes` at `round-25/gate-input` |
| `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` | 2 mismatch of 2 | frozen 16:21:44, packet moved 16:23:21 and 16:24:45 | self-declared supersessor of round-18/22 rows; itself un-superseded |
| `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | 5 D4 rows stale | frozen 16:19:41, before both packet writes | no |
| `reports/round-26/handoff/declared-in-r5/expected.json` | 0 stale at 19:16Z → **5 stale at 19:26Z** | the packet writes of 16:23/16:24 | no — this is the *default* v3 baseline the runner reads |

The first row is the one that most deserves the parent's attention. **Correction to an
earlier draft of this section: it claimed no round-27 artifact names this row.** That
was wrong — the O seat's own prose *does* name it, twice:

- `reports/round-27/adjacency.md:198` — `round-26/gate-input/MANIFEST.tsv | c-n-e 6/6 |
  2 mismatch, 4 reproduced | **superseded by the register landing**`
- `reports/round-27/report-draft.md:171` — "**Disposition: re-pin
  `tools/gates/frozen/round-26/gate-input` as a NEW generation, or supersede it; never
  edit the filed bytes.**"

So the row is **known, named and dispositioned in prose**. What is missing is a
**declaration in the frozen record** — and that distinction is the finding, not
"nobody noticed". Verified against the instruments on disk at 19:28Z:

- **X61** now *does* carry a supersession classifier (11 occurrences; the round-27
  revision added it, and it prints `class: supersession (live input moved=True)` for
  the rows it does reach). But X61 sweeps **rows**, and for
  `round-26/gate-input` the *input digest moved*, so its row-level class is
  `supersession` — a correct row reading that still leaves the **generation** itself
  unnamed as retired.
- **X62** classifies supersession vs drift, but only for the **one** generation it
  picks as current (`round-26/post-register`, by a `current = next(...)` selection).
  Every other generation, including `round-26/gate-input`, is audited as a *record*
  only — it prints `clean` for it, because duty B/C ask "is this record internally
  consistent?", not "is this generation still the pin?". Measured: `tools/gates/frozen/round-26/gate-input: 6 rows, clean; receipt=yes`.
- **Round-26's D20 leg** retired it by **mtime** ("the newest round-26 generation is
  the current pin"), which is prose in a filed round, not a declaration in a receipt.
- **No `freeze-receipt.json`** in the lane names `round-26/gate-input` as superseded.

So the generation is stale, is not the current pin, and **no instrument says so**. A
reader has to know that mtime ordering decides it, or run `replay-frozen` and interpret
a bare `mismatch`. The fact lives in round-26's and round-27's **prose**, not in the
frozen record.

**A second correction to the same earlier draft.** It claimed X62 "reads it correctly"
as superseded. Re-measured, that is wrong: X62 reads `round-26/gate-input` as a **clean
record** and reserves its supersession class for the current generation only. Both
corrections cut the same way — the generation is retired by convention, not by
declaration, and the round's own prose carries the fact that its frozen records do not.

## 7. What this review does not establish

- It does not certify the round, adjudicate the O claim, or admit anything. The
  runner's receipt is the lane's instrument and it says `false`; this seat agrees
  with the *reading*, not as a verdict.
- It does not claim the O seat's method is wrong. The method (new generation, new
  row, never in-place) is correct and the filed bytes prove it was followed. The
  failure is **sequencing**: O froze at 16:19–16:21, D wrote the pinned surface at
  16:23 and 16:24.
- It does not measure the D4 packet's *content*. Whether the register-law landing is
  correct is the D claim's question, measured by the D seats and the D runner leg.
- Its counts are a **snapshot**. The packet moved three times during this seat's own
  window; every digest above carries its stamp, and the drift is the finding.
- It created no clones and edited no filed byte, so the "before" controls for the
  two instrument defects are the runner's and X60's own stored outputs, quoted above,
  not re-runs.
- Its §4 findings describe the state at the stamps given. **Both were live when
  measured and one was repaired during the wave**; a reader should treat §4.1 as
  history with a confirmed fix, and §4.2 as a stale cross-reference that still stands
  on the X60 revision on disk at 19:28Z.

## 8. Disposition proposed to the parent (not a decision — the parent owns it)

1. **The O claim cannot close on this axis order.** Either the round re-runs the O
   sweep *after* the D writes stop, or it records O as **carried** with the D-order
   cause named — the same disposition round 26 needed and did not get.
2. **The runner's battery-capture defect is fixed** (16:28:40) — verified by the
   16:28:22 receipt reading `pass 7 / fail 0 / unevaluable 0`, `coverage 9/9`. No
   action needed; recorded so a reader of the earlier 16:23 receipt is not misled.
3. **`round-26/gate-input` needs a declaration, not an mtime convention.** The round-27
   prose names it and proposes the disposition; a `supersedes` entry in the round-27
   successor receipt would make the stale generation legible to any reader who does
   not have that prose.
4. **The TMPDIR trap belongs in `corpus/knowledge/`** — it is a reusable fact about
   this lane's instruments, currently duplicated across three scratch notes.
5. **X60's docstring** should drop the X61 no-op-probe claim it no longer holds.
