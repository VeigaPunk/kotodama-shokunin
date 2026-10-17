# kotodama — round 9 report (DRAFT BODY — orchestrator finalizes)

> **Scribe X04 draft.** Assembled 2026-10-17 from the landed round-9 fragments
> (inventory: `find reports/round-9 -type f | sort`; every count below is
> stamped with its source). The orchestrator finalizes, adds the carrying work
> commit and the admission verdicts, and files this at
> `.ufo/reports/round-9/kotodama.md`. Items the orchestrator must still decide
> are collected in "Open items" at the end; nothing here is an admission.

Loop 1 of 3, build round 2 of 4 — operator regimen (3 loops × 7 rounds, lane
rounds 8–28). One 64-worker batch on `opencode-go-2/deepseek-v4.1-flash`.
Declared baseline `e1694bad6ac96aca45a11ca5746582b275929355`
(`reports/round-9/claims.json:5`); declaration commit
`a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` ("round-9: declare claims F/O/D").
Cross-revision sweep (scribe re-verified 2026-10-17, matching the fragments'
own measurements): `git diff --stat e1694ba..HEAD` touches only
`reports/round-9/{claims,targets}.json` (159 insertions, 0 deletions) and
`git diff --stat e1694ba..HEAD -- tools/gates examples tools` is empty, so the
committed artifact tree is identical at the declared baseline and at HEAD.
Work commit: the orchestrator's round-9 integration commit (not created at
draft time; no worker committed).

## Work performed

**Freshness (claim F, lowest non-retired axis).** The four still-unresolved
round-8 reconciliation rows (`R8-F01`…`R8-F04`; scribe re-read
`reports/round-8/freshness/reconciliation.json` on 2026-10-17: 4 unresolved,
11 partial-support, raw worker labels 15× "supported") were re-opened with
escalated multi-strategy retrieval: per residual a primary-source/museum-record
hunter, a scholarly-fulltext hunter, an alternate-angle hunter, plus an
independent verifier (`reports/round-9/targets.json`; `claims.json` F).
Landed: **12 hunter receipts** `R9-F01a/b/c` … `R9-F04a/b/c`
(`reports/round-9/freshness/*.json` with `.md` companions), **2 verifier
fragments** (`verify-F03.md`, `verify-F04.md`), the X02 receipts auditor
(`freshness/audit.md`, author-side, explicitly "not an independent promotion
verifier") and the reconciled ledger `freshness/reconciliation.json`
(landed 2026-10-17 after the 18:03:39 acceptance run; its own `counts`:
4 rows, 0 unresolved, 4 moved to partial-support-or-better vs round 8, 12
hunter receipts + 2 verifier documents considered, 17 raw labels recorded,
`counted_on` 2026-10-17 via `python3 -c "import json;d=json.load(open(
'reports/round-9/freshness/reconciliation.json'));print(d['counts'])"`).
Hunters stayed disjoint from the round-8 retrieval set and did not
re-adjudicate raw labels. Example movements claimed by the receipts: F01a closed
the round-8 `to-verify` object record (Louvre catalogue + CDLI catalogue/ATF of
AO 5477 plus a Nippur-provenienced sister witness, with the palaeo-Babylonian
copy caveat preserved); F02's scholarly leg resolved on a first-hand retrieved
full text; F03c supported the royal-cap/god-headgear contrast and a dated
Neo-Hittite comparator while the earlier pre-Hittite comparator stays partial;
F04c landed partial-support across three retrieval channels with the
"Bonnet 1988" book-level verification explicitly still open.

**Operability (claim O).** Seven structural gates × two workers per gate each
author a committed `expected.json` baseline (expected outputs + sha256 digests
of snapshot inputs) and independently re-run/validate it in a copied tree,
plus a battery-validation extension (R9-O15), the round-9 acceptance runner
(R9-O16), a gate registry (R9-O17, `baselines/registry.md`, one row per gate
with entry command, verdict map, selftest spelling, pin path) and three
auditors (`baselines/audit-18.md` isolated re-runs of all seven baselines with
tamper rejection, `audit-19.md` gate-source freeze, `audit-20.md` battery
selftest). Landed: all **7/7 gates** carry a baseline with id `r9-pre`
(registry table; verified independently by the scribe:
`find tools/gates reports/round-9 -name expected.json`). The battery extension
(R9-O15, `baselines/battery-extension.md`) grew `tools/check-gate-battery.py`
488 → 1117 lines (sha256 `077f68e4…` → `0a126b70…`), added a repeatable
`--baselines-root` mode and a new top-level `baselines` report key while
keeping the round-5 `summary` shape intact (a documented compatibility
constraint: `reports/round-5/run-validation.py:123` asserts it by exact
equality), and raised the selftest from 10 to **28 controls** — the scribe
re-measured `python3 tools/check-gate-battery.py --selftest` →
`SELFTEST OK 28/28 controls behaved as expected`, exit 0 (2026-10-17).
R9-O19 audited gate sources: **zero documented exceptions, 7/7 gate scripts
byte-identical** (three samples + 21-probe error-path vector); R9-O20 re-ran
the extension's selftest three times plus tamper drills on copies. **No gate
behaviour change** is claimed or found.

**Depth (claim D, capability `culture-d3-acceptance`).** Round-7's unadmitted
debt completed as new round-9 work: `--check` diagnosis
(`d3/check-diagnosis.md`), determinism (`d3/determinism.md`; in-place double
regeneration byte-compared plus an isolated mirror), evidence coupling
(`d3/evidence-coupling.md`: selftest green — positive 5/5, domain 16/16,
malformed 4/4, frozen 5/5), frozen replay (`d3/replay.md`; `replay-frozen.py
--selftest` 79/79, a scratch-built D3 projection manifest replaying 5/5,
tamper controls fail-closed), CLI negatives (`d3/cli-negatives.md`; 32-case
battery, 29
negatives + 3 controls, all exit 2, no tracebacks, stable repeats, no output
written by a failing run), D2 interop (`d3/interop.md`), contract cross-check
(`d3/contract-crosscheck.md`), docs + capability-row draft (`d3/docs.md`,
`d3/capability-draft.md` — draft only; the orchestrator admits), the acceptance
ledger (`d3/scribe.md`), and two adversarial reviews (`d3/findings.md`:
circularity audit, 6 ranked findings, no fabricated or self-blessed green
found, but S1 warns the remaining re-pin step is mechanically
indistinguishable from blessing a tamper unless recorded; `d3/findings-10.md`:
independent re-derivation of the legacy projection, 62/63 checks, the single
failure a 36-byte presentation-prose divergence between the two committed
artifacts). Scribe-verified pre-state: `assemble-culture-d3.py --check` already
exited 0 at the declared baseline and the guard `--selftest` was already green,
so the round's D work is acceptance *evidence*, not a repair. Delivered
artifact sizes for orientation (scribe count, `examples/culture-d3/packet.json`):
2 eras, 20 lexemes, 6 names, 7 utterances, 2 beliefs, 2 symbols, 3 materials,
4 objects, 4 costumes, 1 rank rule, 5 references, 5 bridges.

**Metadata verify.** 11 shards re-audit all **179** `corpus/knowledge/` entries
for the `source:` / `verified-at:` / `recheck:` trio and fix stragglers in
place (`reports/round-9/metadata/`, shards v01–v08, v10, v11 + auditor
`audit.md` in the lane; **v09 landed out of lane** — see the breach below).
The auditor's census found the opening-block trio in place across the
inventory; its own §6 records that `v09-myth-symbol.md` was **not on disk in
the lane** at close (see the adjacency breach below).

**Scribe/audit.** X01 lessons gate-keeper (`corpus/lessons/round-9.md`,
fragment index + gate survey window 20:49:06–21:02:22 UTC), X02 freshness
receipts auditor (`freshness/audit.md`), X03 adjacency/connector
(`reports/round-9/adjacency.md`), X04 this draft.

## Landed changes

Lane-repo writes by the 64-worker batch (orchestrator integrates and commits;
no worker committed):

- `reports/round-9/baselines/` — per-gate fragments (`expected.json`,
  `freeze.txt`, snapshots, `run.log`, `author.md`, `rerun.md`), `registry.md`,
  `battery-extension.md`, `audit-19.md`, `audit-20.md`.
- `tools/gates/expected/<gate>/r9-pre/` and
  `tools/gates/frozen/<gate>/r9-pre/` — the other two baseline roots
  (see open item 2).
- `reports/round-9/freshness/` — 12 hunter receipts (+ `.md`), 2 verifier
  fragments, `audit.md`.
- `reports/round-9/d3/` — 12 acceptance fragments.
- `reports/round-9/metadata/` — 10 shard fragments + `audit.md` in the lane;
  the 11th shard's file landed **out of lane** (below).
- `corpus/knowledge/**` — metadata frontmatter repairs in place
  (`git status --short` shows modified entries; gate-neutral by construction:
  `tools/gates/provenance-audit.py:75` reads only `topic|sources|couples`).
- `corpus/lessons/round-9.md` — X01 gate-keeper fragment.
- `reports/round-9/run-validation.py` + `validation.json` — the declared
  counting command and its receipt (R9-O16).
- `tools/check-gate-battery.py` — the O15 extension (648 insertions,
  19 deletions; uncommitted at audit time).
- `reports/round-9/{claims,targets}.json` — the round declaration (already
  committed as `a7bb205`).

**Known integration hazards, all recorded by fragments:**
- `.gitignore:3 *.log` ignores the baseline `run.log` snapshots; shipping them
  needs `git add -f` (naming-collision `freeze.txt` integration notes).
- Worker scratch exists inside the repo tree (`.scratch/`,
  `.scratch-r9f04c/`, `.aliquot.tmp`, `.cis1-scan.tmp`,
  `freshness/.scratch-v03/`, `reports/round-9/__pycache__/`) and must not be
  committed.
- **One out-of-lane write (breach):** the V09 metadata fragment landed at
  `/home/vgpnk/Projects/shokunin/reports/round-9/metadata/v09-myth.md`
  (parent tree, 17:51:57) — `adjacency.md` §4.2; the lane's own
  `reports/round-9/metadata/v09-myth-symbol.md` is absent. X03 also records an
  unattributed stray PDF that is not imputable to this lane.

## Before → after measurements

Counting command (declared): `python3 reports/round-9/run-validation.py` →
`reports/round-9/validation.json`. Latest receipt read by the scribe:
2026-10-17 18:03:39 (-03:00), runner sha256 `8e488130…`; on a tree that was
still being written (`missing_dependencies: []`;
`acceptance_checks_passed: False`).

| claim | runner verdict (18:03:39) | before (verified) → after |
|---|---|---|
| F / freshness | **passed = true**, 0 failures | 4 unresolved residuals, raw labels 15× supported → 12 hunter receipts + 2 verifiers; harness-reported substantive retrieval units (top-document/unit count, not certified passages) 48/71/60/45 for F01–F04; three negative controls all rejected (missing-receipt floor, escalation role, deeper-limit receipt). The runner's 18:03:39 F reading ran before `freshness/reconciliation.json` existed and used in-receipt raw/reconciled pairs (`receipt_pairs: 4`); the ledger that landed after it reconciles all 4 rows to **partial-support**, 0 unresolved |
| O / operability | **passed = true**, 0 failures | 0 of 7 gates carried a gate-level `expected.json` (`find . -name expected.json -not -path './.git/*'` → only `examples/culture-d3/expected.json`) → 7/7 gate baselines valid (`r9-pre`), battery extension green: selftest 10 → 28 controls (scribe re-measured 28/28 exit 0), gate sources byte-identical, 0 documented exceptions |
| D / depth | **passed = false**, 1 failure | acceptance evidence absent (round 7 closed failed) and `--check` already exit 0 → assembler check exit 0 twice with identical stdout (`8e8910da…`), coupling selftest green, 32/32 CLI negatives, replay selftest 79/79, interop green; **the one red leg** is `tools/check-evidence-coupling.py --frozen examples/culture-d3/expected.json` → exit 2 with exactly 3 `D3-SNAPSHOT` digest drifts: `corpus/knowledge/synthesis/worldbible-integration-contract.md` (`50c4c2f2…` → `5f4c02bf…`), `tools/gates/costume-era-consistency-gate.py` (`29a9361c…` → `e6bffd70…`), `tools/gates/naming-collision-gate.py` (`8c5afb0a…` → `d9e4e8f4…`) — all three drifted by the round-8 admission commit `e1694ba` **after** the pin was frozen at `57c3ce6`; 21/24 manifest entries still match |
| coverage | unchanged | 179 knowledge entries, six partitions; metadata edits are frontmatter-only → 179 (scribe re-counted 2026-10-17: `find corpus/knowledge -name '*.md' | wc -l` → 179, `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` exit 0) |
| calibration | observation only | raw round-6 labels preserved apart from reconciled dispositions inside receipts; the auditor documented a fetch-method lesson (browser UA vs curl default UA produced false failures and false passes; matcher validated on a known passage: EXACT 258/258, one word changed → PARTIAL 41/256) |
| adjacency | one breach recorded | handoff contract digest `5f4c02bf…` unchanged at baseline/HEAD/worktree (4 stamps); PROVINCE.md unchanged (`05b34a57…`); all 2072 changed paths in-lane; **one seat wrote outside the lane** (v09 metadata fragment, parent tree) |

Axis verdicts, admission, the SCORECARD axes table and any capability row are
the orchestrator's (`SCORECARD.md` §"Axes — round 9"); this draft claims no
verdict. Claim D's `after_required` is currently **not fully met**: its fourth
clause ("D3 replays frozen without digest drift") is honestly recorded as
could-not-evaluate/red by every D3 fragment (`d3/scribe.md` §5, `d3/replay.md`
§0 row D, `d3/findings.md` S1).

**Environment receipt (out of province — report, don't absorb).** Throughout
this round `/tmp` was a 16 GB tmpfs with **0 free inodes**: `df -i /tmp` →
`1048576 1048576 0 100% /tmp` (scribe, 2026-10-17; the by-volume view
disagreed — `df -h /tmp` → 8.5 G available — so the failure mode is inode-only:
any write there fails with `No space left on device`; the scribe's own first
poll log and a `nohup` poller hit it). Independently corroborated by at least
five shards (`baselines/registry.md`, `d3/check-diagnosis.md`,
`d3/evidence-coupling.md`, `d3/cli-negatives.md`, `d3/findings.md`,
`freshness/audit.md` §0, `freshness/verify-F03.md` §1, `corpus/lessons/round-9.md`).
Workers adapted with in-lane `.scratch/`, `~/.cache/`, `/var/tmp`, `/dev/shm`.
The lane performed no cleanup (deleting other processes' temp files mid-wave
was judged unsafe) — operator decision requested.

## SHONEN skeleton

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — round-8 label-typing table stands; round 9 adds no landed SKILL
  edit (the D3 capability row is `d3/capability-draft.md`, a draft the
  orchestrator admits or drops)
- [~] At least one end-to-end domain task executed and logged — D3 acceptance
  evidence (`reports/round-9/d3/`) plus escalated freshness hunts
  (`reports/round-9/freshness/`); LOG entry is the orchestrator's to append
- [~] Instructions executable by an agent without oral context — gate baselines
  + battery extension + `run-validation.py` run from the lane root; F and O
  green on the 18:03:39 receipt, D red on one leg
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `adjacency.md`:
  PROVINCE accurate, refusals unviolated, handoff contract untouched, but one
  out-of-lane metadata write is recorded as a breach for the orchestrator

Promotion review: not requested this round; every box stays `[~]` for lack of a
named non-author verifier.

## Open items for the orchestrator

1. **D decision (the only red leg).** Re-freeze `examples/culture-d3/expected.json`
   with the 3 documented drift lines (`d3/check-diagnosis.md` §3/§6 gives the
   exact command and the verdict-preserving argument; `d3/findings.md` S1
   requires the re-pin record to be distinguishable from blessing a tamper), or
   admit D with the frozen clause recorded as could-not-evaluate. The runner
   turns D green only on the former.
2. **Baseline root.** Three roots are in use
   (`reports/round-9/baselines/<gate>/`, `tools/gates/expected/<gate>/r9-pre/`,
   `tools/gates/frozen/<gate>/r9-pre/`); the lane standard
   (`corpus/knowledge/verification/gate-frozen-run-standard.md` §3) names
   `tools/gates/frozen/<gate>/<baseline-id>/`. Relocate with a `git mv` of
   frozen bytes — never re-freeze or re-pin (naming-collision `freeze.txt`
   integration notes).
3. **Metadata v09.** Import `/home/vgpnk/Projects/shokunin/reports/round-9/
   metadata/v09-myth.md` into the lane as `reports/round-9/metadata/
   v09-myth-symbol.md` and record the breach, or record the decision to leave
   it out (the auditor's census says the myth-symbol surface is conformant
   either way).
4. **Commit hygiene.** Exclude `.scratch/`, `.scratch-r9f04c/`, `*.tmp`,
   `freshness/.scratch-v03/`, `__pycache__/`; consider `git add -f` for the
   baseline `run.log` snapshots if they are to ship (`.gitignore:3 *.log`).
5. **Re-run `python3 reports/round-9/run-validation.py` on the settled tree**
   and file the receipt with the report; F/O/D verdicts in the fleet report
   derive from that run.
6. **`/tmp` inode exhaustion** — environment-level, corroborated by ≥5 shards;
   carry to the operator, not into the lane's own gates.
