# Round 17 — report draft (SCRIBE X02)

- **Round:** 17, operator loop 2 of 3, build round 1 of 4 (64 declared
  workers, `opencode-go/deepseek-v4.1-flash`). **Date:** 2026-10-18.
- **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. **Baseline:**
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit), HEAD
  `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17 declare) at draft time.
- **Claims:** D / depth (`culture-d4-assembly`), C / coverage (12 stale
  civ entries dispositioned), O / operability (`assemble-culture-d4`).
- **Counting command:** `python3 reports/round-17/run-validation.py`
  (receipt: `reports/round-17/validation.json`).
- **Status of this draft:** NON-CANON engineering evidence. It admits
  nothing, certifies no canon, lore receipt, source freshness, or real-world
  clearance, and it is written by the X02 scribe seat, not the integrator.
  The parent owns the final report and the LOG/SCORECARD append.

## 1. What landed and how it is measured

Round 17 was declared as a three-claim build: a fourth culture example
(`examples/culture-d4/`) driven end-to-end through the rounds 8–16 typed
pipeline; disposition of the 12 `stale-documented` civilizations entries the
round-16 map named; and a durable `tools/assemble-culture-d4.py` assembler.

The counting command is `reports/round-17/run-validation.py`, written by this
seat and kept stdlib-only, read-only over every artifact it grades, and
fail-closed on filed-round contact (rounds 8–16 must stay byte-identical to
the baseline; corrections live only under `reports/round-17/`). It discovers
D4 artifacts semantically (canonical names: the D2 convention with a `d4`
suffix) and executes only fixed read-only check/selftest commands plus its own
`.scratch` fixtures. Its own controls are green: `--selftest` → 31/31.

## 2. Claim C — coverage (the 12 stale entries)

Measured at `reports/round-17/validation.json` (2026-10-18): **PASS.**

- **12/12 dispositioned**, each with a dated, command-carried evidence
  fragment under `reports/round-17/civ/` that keeps the round-16 reason trail
  (the round-16 shard path and/or the round-16 reason's distinctive tokens).
  14 evidence fragments were measured; the verifiers' `map-patch.json`
  (row-replacement proposal against the filed round-16 map) was consumed with
  `from_` rows checked against the filed map and **no contradictions** — its
  `stale_after` set is empty.
- **Fixed with landed locators (7):** `inuit` (Dorais 2010 PDF locator
  replaced by a live publisher-distributor preview, HTTP 200,
  content-verified), `maya-classic` (couples gap closed with the §14 sacbeob
  route layer plus a live tertiary locator and the reciprocal pointer to
  `transport-mobility-lexicon.md`), `mesoamerica-primary-sources` (the dead
  Lilly transcription host replaced by the live ScholarWorks published
  version plus an archived raw snapshot), `persia-sasanian` (academia.edu 403
  replaced by a live edspace PDF; the avesta.org host unreachable on 9/9
  samples replaced by a dated archived copy), `polynesia-navigation`,
  `scythian-saka`, and `siam-thai` (locators re-pinned to live/redirected
  forms during their URL-status sweeps).
- **Attempted with evidence (5):** `mongol` and `muisca` (round-16 hard-fail
  URLs re-probed live across independent samples; locators kept, entry
  receipts updated), `rapa-nui`, `rome`, `ryukyu` (URL-status sweeps with
  per-URL receipts; no locator replacement warranted or no live replacement
  found, recorded).
- **Pass rule:** all 12 dispositioned and (fixed ≥ 6 or every non-fixed
  entry names its attempt) — met on both counts (7 fixed, 5 attempted). The
  round-16 map's stale count drops by 7 through the patch; the remaining 5
  carry named, evidenced attempts.
- **Corpus edits:** all 12 named entries carry receipt edits
  (`verified-at`/revision lines) and 7 of them landed locator replacements;
  no other civilizations byte differs from the baseline, checked
  entry-by-entry against the baseline revision. Every edit keeps the
  round-16 reason trail and the entries' NON-CANON standing.
- **Freshness pause honored:** the fragments issue dated URL-status/access
  receipts, not a freshness axis-move; the pause recorded in `LOG.md` and
  `SCORECARD.md` remains in force and no re-grade or rank change is claimed.

## 3. Claim D — depth (culture-d4 through the typed pipeline)

Measured at `reports/round-17/validation.json` (2026-10-18, last run of this
seat): **FAIL — four artifacts pending.** `examples/culture-d4/` landed during
this seat's window with its **12 components**, `brief.md`, `README.md`,
`ASSEMBLY.md` and the assembled `packet.d4.yml`; the assembler's `--check`
regenerates it byte-identically. Everything measurable without the typed
artifacts is green: the d2/d3 example trees and assemblers are
byte-identical to the baseline and their `--check`/selftest runs exit 0, the
five culture gates run over `packet.d4.yml` with exits in {0, 1}, and the
NON-CANON marker is present with no affirmative clearance claim. The four
pending items are:

1. `examples/culture-d4/packet.d4.typed.yml` (typed packet, schema
   `kotodama-typed-packet-v1`),
2. `examples/culture-d4/typed-labels.d4.yml` (typed-label projection),
3. `examples/culture-d4/expected-holds.json` (expected hold set; the
   fragment `reports/round-17/d4/expected-holds.fragment.json` names 17 holds
   + 1 note, and every hold id and location is already named in the round-17
   design docs, checked),
4. a round-17 frozen manifest (`tools/gates/frozen/round-17/MANIFEST.tsv` or
   an equivalent path) that replays green under `tools/replay-frozen.py`.

When they land, the runner measures: **hold-set equality** (the typed
packet's emitted finding set keyed `(id, severity, where)` equals the
expected hold set in both directions, counts pinned, non-null details
pinned), **determinism** (two fresh adapter builds byte-identical and
reproducing the delivered typed packet), **replay** (round-17 manifest green;
`TMPDIR` outside the repo by `replay-frozen.py`'s design), **interop** (strict
parse, `assembly` pins re-verified, gate exits in {0,1}) and the
pre-declared-hold check. The D path was pre-flighted against a synthetic tree
built from the D2 artifacts, so the remaining legs are exercised code, not
first-run code.

A note for the final run: the adapter's freshness leg regenerates the
projection and compares bytes, and the projection records the packet's path
(`assembly.packet`), so the D4 projection must be generated at its final
`examples/culture-d4/` path by the same projector — copying a projection
from another path fails byte-reproduction by design.

## 4. Claim O — operability (assemble-culture-d4)

Measured at `reports/round-17/validation.json` (2026-10-18): **PASS.**

- `tools/assemble-culture-d4.py` exists; `--check` → exit 0
  (`packet.d4.yml: byte-identical deterministic assembly`) on the delivered
  D4 tree; `--selftest` → exit 0 (81/81 checks at the last run, with the
  positive/clean, tamper, malformed and missing fixture controls all
  evidenced).
- The three pre-existing d2/d3 assemblers (`tools/assemble-d2.py`,
  `tools/assemble-d2-typed.py`, `tools/assemble-culture-d3.py`) are
  byte-identical to the baseline revision and green
  (`--check`/`--selftest` exit 0 each).

## 5. Harness self-controls

- `python3 reports/round-17/run-validation.py --selftest` → 34/34 controls
  (status/entry normalization, hold-set equality acceptance and rejection
  incl. hold-laundering, detail drift, null-detail non-pinning and
  severity inference, fragment fix/attempt/unclassified classification,
  round-16 trail-pointer exclusion, fragment attribution ranking and the
  shared-sweep index-row exclusion, URL extraction, filed-byte preservation
  classes, artifact discovery over a synthetic D4 fixture tree, unsafe-path
  rejection, clearance-claim catch and negation non-catch, metric
  command/date carriage).
- The runner records every input digest in `validation.json`, compares the
  filed rounds 8–16 against the declared baseline (694 files measured, 0
  violations at the mid-wave run; git-ignored `*.log` scratch is excluded),
  snapshots the filed bytes before and after the run, and fails closed if any
  filed byte or path set changes during validation.

## 6. Limits

- All measured artifacts are NON-CANON. This draft does not certify truth,
  canon, lore acceptance, cultural permission, or any real-world rights
  position; those are lore-shokunin's (and the world's) to record, never
  this lane's.
- Claim C dispositions are point-in-time access facts with dated commands;
  they are not freshness verdicts and the freshness axis-move remains
  paused.
- Claim D's hold set is design debt, not failure: the pipeline is expected to
  emit its holds (the D2 precedent emits 15 holds + 1 note at exit 0).
- The runner's D4 discovery is semantic; a differently named artifact is
  still found, and the canonical names are the D2 convention with a `d4`
  suffix.
- The round-17 declaration allocates 60 seats in `targets.json` while
  `claims.json` declares 64 workers (scope.md F-X02-1, informational).

## 7. Commands

- `python3 reports/round-17/run-validation.py --selftest` → 34/34, exit 0.
- `python3 reports/round-17/run-validation.py` → writes
  `reports/round-17/validation.json`; per-claim verdicts printed.
- `python3 reports/round-17/run-validation.py --check` → same measurement,
  printed, no write.
- `python3 tools/assemble-culture-d4.py --selftest` → exit 0 (79/79 checks).
- Baseline greens re-verified 2026-10-18: `tools/gates/typed-pipeline-gate.py`
  → exit 0 (16/16 legs); `tools/assemble-d2.py --check`,
  `tools/assemble-d2-typed.py --check`, `tools/d2-typed-labels.py --check`,
  `tools/assemble-culture-d3.py --check` → exit 0 each;
  `tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` (TMPDIR
  outside the repo) → exit 0 (11/11 rows reproduced).
