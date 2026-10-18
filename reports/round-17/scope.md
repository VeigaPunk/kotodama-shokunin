# Round 17 — Scope watch (SCRIBE X02)

- **Date:** 2026-10-18. **Regimen:** operator loop 2 of 3, build round 1 of 4
  (64 workers, `opencode-go/deepseek-v4.1-flash`, per `claims.json`).
- **Lane state at check time:** HEAD `9b49a4a` ("round-17: declare loop-2
  build-1 claims D/C/O (D4 culture, stale-entry fixes, d4 assembler)",
  2026-10-18 06:13:27 -0300); baseline `f30b6f8` (round-16 admit) is HEAD's
  direct parent (`git merge-base --is-ancestor` → yes). `claims.json` state:
  `declared-before-dispatch`.
- **Verdict: IN SCOPE AND CLEAN, with three informational findings.** Fleet
  root clean, filed rounds 8–16 untouched, PROVINCE accurate. One declaration
  arithmetic discrepancy and two out-of-lane/historical observations are
  reported at the end; nothing absorbed, nothing repaired in place.

## 1. Fleet root clean

`git status --porcelain=v1` in `/home/vgpnk/Projects/shokunin` → empty
(0 lines, 2026-10-18). Fleet HEAD `97ac852` "protocol: close lore r101
(admitted) — fleet report + MANIFEST ledger append", 2026-10-18 06:15:04
-0300.

Sibling sweep (read-only, 2026-10-18, `git -C <lane> status --porcelain=v1 |
wc -l` over all `*-shokunin/` repos): 19 lanes clean; `kotodama-shokunin`
dirty_lines=1 — the in-flight C edit `M
corpus/knowledge/civilizations/inuit.md` (this round's assigned claim-C work,
not filed-round contact); `lore-shokunin` dirty_lines=2 — out-of-lane,
reported as F-X02-2, never touched from here.

## 2. Filed rounds 8–16 untouched

Method (2026-10-18): the round-16 baseline `f30b6f8` is HEAD's parent, and
`git show --stat 9b49a4a` touches exactly `reports/round-17/claims.json`
(+34) and `reports/round-17/targets.json` (+18) — zero contact with filed
rounds. Per-directory last-touch audit:

| dir | last-touch commit | commit that filed it |
|---|---|---|
| reports/round-8 | `44070b4` (round-12 admit) | round-12 receipt restoration |
| reports/round-9 | `44070b4` (round-12 admit) | round-12 receipt restoration |
| reports/round-10 | `b02cfbc` (round-14 admit) | round-14 integration |
| reports/round-11 | `a3f6fce` (round-11 verdict) | round-11 rejection record |
| reports/round-12 | `b02cfbc` (round-14 admit) | round-12 admission |
| reports/round-13 | `3dedab2` (round-13 declare) | declare-only round (operator-skipped, 0 files landed) |
| reports/round-14 | `b02cfbc` (round-14 admit) | round-14 integration |
| reports/round-15 | `16652e8` (round-15 admit) | round-15 admission |
| reports/round-16 | `f30b6f8` (round-16 admit) | round-16 admission |

No directory's last touch postdates its filing commit. This re-checks the
round-12 receipt-clobber defect class (FRR-12a/b,
`reports/round-12/defects/ledger.json`): no filed receipt was overwritten
this round.

Note on the in-flight tree: at check time the only non-filed dirty line is
the C-assigned `corpus/knowledge/civilizations/inuit.md` edit. Round 17's
claim C explicitly licenses corpus edits *for named entries that keep the
round-16 reason trail*; the validation runner measures exactly that
(§5 below) rather than treating the edit as dirt.

## 3. PROVINCE accurate

Checked 2026-10-18 against `PROVINCE.md` (committed, unmodified):

- **Owned partitions all exist (6/6):** `ls corpus/knowledge/` →
  civilizations, culture-material, linguistics, myth-symbol, synthesis,
  verification.
- **Civilizations count = 94**, matching the round-16 map's declared count:
  `ls corpus/knowledge/civilizations/*.md | wc -l` → 94.
- **Adjacent contract file exists:**
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`.
- **Refuses/adjacency consistent:** no PROVINCE statement contradicted by
  tree state; the round-17 claims (D4 culture build, civ staleness
  disposition, d4 assembler) all sit inside the owned
  linguistics/culture-material/verification/synthesis partitions. No claim
  asserts canon, lore acceptance, or real-world clearance — consistent with
  the refuses list.

## 4. Round-17 declaration coherence

- `claims.json` and `targets.json` agree on round (17), date (2026-10-18),
  baseline (`f30b6f8188937632bbedd0e7b29aeefff6f8b07b`), and claim set
  D/depth, C/coverage, O/operability.
- **Worker arithmetic does not close (F-X02-1):** `claims.json` declares
  `workers: 64`; `targets.json` allocates 4+12+4+4+8+3+5+2+12+4+2 = **60**
  seats (D-design 4, D-components 12, D-typed 4, O-assembler 4, D-tests 8,
  D-neg 3, D-review 5, D-scribe 2, C-fixers 12, C-verifiers 4, X 2). The
  round-16 declaration closed exactly; this one is off by 4. Reported, not
  repaired — `targets.json` is the operator's dispatch map and this scribe
  does not rewrite declarations.
- Expected-absent pre-dispatch artifacts (deliverables, not defects):
  `examples/culture-d4/` and `tools/assemble-culture-d4.py` do not exist at
  check time; `reports/round-17/{d4,assembler,civ}/` exist as empty
  in-flight scratch dirs; `reports/round-17/run-validation.py` (the claims'
  `counting_command`) is this scribe's deliverable.

## 5. Round-17 counting contract (what `run-validation.py` measures)

`python3 reports/round-17/run-validation.py` is the claims' counting
command. It is stdlib-only, read-only over every artifact it grades, runs no
historical validator, and executes only fixed commands plus its own
`.scratch` fixtures. Claim by claim:

**D / depth — `examples/culture-d4/` end-to-end.** Discovery is semantic,
not name-locked: the runner finds the D4 legacy packet, the typed packet
(schema `kotodama-typed-packet-v1`), the typed-label projection, the brief,
the design docs under `reports/round-17/d4/`, and the expected hold set
(schema `kotodama-typed-pipeline-holds-v1`; the canonical D2 names with a
`d4` suffix are what it looks for first). It then measures: (D1) the 12
components + brief + typed packet + projection + expected holds all exist;
(D2) **hold-set equality** — the typed packet's emitted finding set keyed
`(id, severity, where)` equals the expected hold set in both directions,
with counts and detail strings pinned; (D3) **determinism** — the d4
assembler's `--check` regenerates byte-identically and two fresh adapter
builds are byte-identical to each other; (D4) **replay** — a round-17
frozen manifest replays green under `tools/replay-frozen.py`; (D5)
**interop** — the delivered typed packet parses under the projector's strict
loader, its `assembly` pins re-verify against delivered bytes, and the five
culture gates run over the D4 packet with exits in {0,1} (no exit 2 /
traceback); (D6) **d2/d3 untouched and green** — `examples/culture-d2/` and
`examples/culture-d3/` bytes equal the baseline revision, and the D2 typed
pipeline gate, D2 assembler/adapter/projector `--check`, and the D3
assembler `--check` all exit 0; (D7) **NON-CANON** — the tree declares
NON-CANON and carries no real-world clearance/rights/canon-acceptance
assertion; (D8) the hold set is named in the design docs (pre-implementation
record) and matches the expected file.

**C / coverage — the 12 stale entries.** The runner loads the round-16 map
(`reports/round-16/civ-map.json`, statuses `stale-documented`) as the fixed
12-entry target list, then looks for per-entry disposition evidence: an
updated round-17 map if one landed, plus evidence fragments under
`reports/round-17/civ/` (canonical name `<entry>.md`; any `.md`/`.json`
naming the entry is accepted). Each of the 12 must carry a disposition:
**fixed** (a replacement locator that is actually present in the corpus
entry's bytes, with the fragment carrying a date and an access-evidence
command) or **attempted** (the fragment names the replacement attempt and
why it did not land). The pass rule is the claim's: all 12 dispositioned,
and (stale-fixed ≥ 6) or (every non-fixed entry names its attempt); every
fragment must keep the round-16 reason trail (it cites the round-16 evidence
shard `reports/round-16/civ/<shard>.md` or quotes the round-16 reason's
distinctive token). Corpus edits are permitted only for these 12 named
entries; any other `corpus/knowledge/civilizations/` byte change fails C.

**O / operability — the d4 assembler.** `tools/assemble-culture-d4.py`
exists and its `--selftest` (fixture controls: positive, tamper, malformed,
missing) and `--check` (byte-identical regeneration of the delivered D4
tree) both exit 0; the three pre-existing d2/d3 assemblers
(`tools/assemble-d2.py`, `tools/assemble-d2-typed.py`,
`tools/assemble-culture-d3.py`) are byte-unchanged from the baseline and
their `--check`/`--selftest` paths stay green.

The runner writes `reports/round-17/validation.json` (and prints the same
document to stdout) with per-claim measurements, failures, input digests,
and the filed-round byte snapshot before/after the run. `exit 0` iff all
three claims pass; `1` on any claim failure; `2` on guard/preflight failure.

## 6. Findings — reported, not absorbed

- **F-X02-1 (declaration arithmetic):** `targets.json` allocates 60 seats,
  `claims.json` declares 64 workers (§4). No seat is invented or removed by
  this scribe; the operator's dispatch map stands as filed.
- **F-X02-2 (out-of-lane, informational):** `lore-shokunin` working tree is
  dirty (2 lines) at sweep time; the other 19 sibling lanes are clean.
  Cause and disposition are lore's own scope; left untouched.
- **F-X02-3 (historical replay pin, informational):**
  `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`
  now exits 2 (`gate_digest_mismatch` on `tools/gates/provenance-audit.py`
  and the other later-fixed gates) — the round-3 manifest pins gate
  revisions that rounds 8–16 legitimately fixed; this is the recorded
  historical-pin class, not new drift, and it is why round 17's claim-D
  replay requirement is measured against a **round-17** frozen manifest.
  The round-11 typed-pipeline manifest, replayed with `TMPDIR` outside the
  repo, is green: `11/11 rows reproduced` (2026-10-18).

## 7. Commands (all run 2026-10-18)

- `git status --porcelain=v1` — lane repo (1 line, in-flight C edit) and
  fleet root (0 lines).
- `git merge-base --is-ancestor f30b6f8… HEAD` → yes; `git show --stat
  9b49a4a` → only round-17 declare files.
- `git log -1 --format='%h %ad %s' --date=short -- reports/round-N` for
  N=8..16 (table above).
- `for d in */; do git -C "$d" status --porcelain=v1 | wc -l; done` —
  sibling sweep, 20 lanes.
- `ls corpus/knowledge/`; `ls corpus/knowledge/civilizations/*.md | wc -l`
  → 94.
- Baseline greens, `TMPDIR` outside the repo for replay: D2 assembler /
  adapter / projector `--check` → exit 0 each; typed-pipeline gate → exit 0
  (16/16 legs); D3 assembler `--check` → exit 0; round-11 replay → exit 0
  (11/11).

## 8. Compliance self-attestation

This scribe wrote only `reports/round-17/scope.md` (plus, later in the same
seat, `reports/round-17/run-validation.py` and
`reports/round-17/report-draft.md`). No git mutations, no writes outside
the assigned files, no filed-round bytes touched, no scratch writes outside
`.scratch`. Out-of-province observations routed to §6 per PROVINCE
("report, never absorb").
