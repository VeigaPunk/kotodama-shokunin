# Round-77 freeze checklist — the 18-file core, digest-pinned, LEGCOUNT-gated

Built by `ExecFreezeChecklist` (wave 1, build + recon) against
`reports/round-77/` at lane base `211f9526800906e0c585d878d265c37e5e090c15`.
Companion artefacts in this directory:

| file | role |
|---|---|
| `manifest.json` | the 18 files the freeze commit must carry, each with a `sha256` placeholder, its consumers and its producer; the LEGCOUNT rule and its emitted checks; advisory (non-gated) provenance; recorded base evidence; the four freeze blockers |
| `manifest-check.py` | the gate: records the digests, then re-reads them from the freeze commit's blobs and runs both LEGCOUNT checks. Exit 0 PASS / 1 FAIL / 3 PENDING |
| `legcount.py` | the LEGCOUNT check: parses the counter's own leg-table literal with `ast` and compares it to the frozen `claims.json` `legs[]` (order and multiplicity included) |
| `controls.sh` | rebuilds every control in its own scratch dir and removes it on exit |
| `controls-receipt.txt` | the measured receipt: 22 expectations, all met (P1/P2, N1-N7, B-C/B-Ca, C1-C8) |
| `build-state-receipt.txt` | `manifest-check.py --root <lane>` today: `MANIFEST r77: PENDING files=0/18 … missing=17 unpinned=1 legs=0/2`, exit 3 |

Run everything from the lane root:
`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin`.

```
ST=.ufo/waves/round-77/w1/stage/ExecFreezeChecklist
```

---

## Step 0 — preconditions

1. Base is `211f9526800906e0c585d878d265c37e5e090c15`
   (`git -C . rev-parse HEAD` before the freeze commit).
2. The worktree carries no tracked modifications to `reports/round-76/**`,
   `corpus/**`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md` — the
   wave-1 rule; untracked `.ufo/waves/round-77/` and `reports/round-77/` are
   expected.
3. `reports/round-77/telemetry/census-start.txt` is already in the worktree
   (3769 bytes at build, last line `kotodama	ok	<lane>/corpus/SOURCES.md`).
   It is **not** pinned yet: pin it at the freeze, not before, so that a
   legitimate re-run of the census does not read as drift.

## Step 1 — install the 18 core files

Every path in `manifest.json` `files[]`, with its producer. Absent today: 17.

| # | path | producer |
|---|---|---|
| 1 | `reports/round-77/claims.json` | L1, from `CLAIMS-DRAFT.md` + the counters' leg tables (Step 2) |
| 2 | `reports/round-77/ledger.json` | L1 from the ScoutLedger/ExecAdaptCa work, ≥10 unique pairs |
| 3 | `reports/round-77/accept-c.py` | counter author seat |
| 4 | `reports/round-77/accept-ca.py` | counter author seat |
| 5 | `reports/round-77/counters/capture-evidence.py` | counter author seat (round-76 file is the pattern) |
| 6 | `reports/round-77/counters/junk-fixtures.py` | counter author seat |
| 7 | `reports/round-77/fixtures/r1exempt-green.json` | rule-2 `used-by` edit, `expect: green` |
| 8 | `reports/round-77/fixtures/r1exempt-mixed.json` | `teaches`+`used-by` edit, `expect: red` |
| 9 | `reports/round-77/fixtures/r1exempt-red.json` | `teaches` edit, `expect: red` |
| 10 | `reports/round-77/telemetry/controls-c.txt` | counter C at lands == freeze, lands == base |
| 11 | `reports/round-77/telemetry/controls-ca.txt` | counter Ca at lands == freeze (with `--combined`), lands == base |
| 12 | `reports/round-77/telemetry/junk-c.txt` | `counters/junk-fixtures.py` against a landing revision |
| 13 | `reports/round-77/telemetry/junk-ca.txt` | `counters/junk-fixtures.py` against the Ca ledger |
| 14 | `reports/round-77/telemetry/census-start.txt` | `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` — present |
| 15 | `reports/round-77/telemetry/census-start-counts.txt` | **drafted** at `.ufo/waves/round-77/w1/drafts/reports/round-77/telemetry/census-start-counts.txt` (820 rows, 253 knowledge `.md`, tier/status histogram — re-measured at the base by this seat); install it or re-measure |
| 16 | `reports/round-77/telemetry/selftest-c.txt` | `python3 -B reports/round-77/accept-c.py --selftest` |
| 17 | `reports/round-77/telemetry/selftest-ca.txt` | `python3 -B reports/round-77/accept-ca.py --selftest` |
| 18 | `reports/round-77/telemetry/gap-sweep.txt` | `git grep -l -E <fragment> <base> -- corpus/knowledge`, once per cited document |

The selftest and controls recipes are the **round-76 CLI shape**; the round-77
counters do not exist yet, so confirm the flags with `--help` before recording
those receipts (round-76's `accept-c.py --selftest` also needs its part
fixtures installed — an incomplete install is exactly what the receipt proves).

Check the set after installing:

```
python3 -B "$ST/manifest-check.py" --root .
```

Expected: `MISSING` gone, `UNPINNED` on the 18 (placeholders), legs `PASS` or
`PENDING`, summary `PENDING`, exit 3. A `FAIL` here is a real defect — the
gate never reports PASS while a file is absent or a digest is unpinned.

## Step 2 — LEGCOUNT gate (before the freeze commit)

The frozen `legs[]` must equal the counter's own table: **same names, same
order, duplicates included**. Round 76 was refused at freeze-control time on
exactly this (`INDEX` designed, `SCRATCHMIRROR` implemented →
`REFUSED: LEGCOUNT … ACCEPT-C-76: FAIL legs=0/13`, exit 2; receipt
`.ufo/waves/round-76/w1/stage/L1/freeze-control-legcount-redbefore.txt`).

1. Print the counter's order and write the prose in that order — never
   hand-type the list:

```
python3 -B "$ST/legcount.py" --claim C  --print counter     # one name per line
python3 -B "$ST/legcount.py" --claim Ca --print counter
```

`--print counter` reads only the counter; it works before `claims.json` exists.

2. Compare (either form: the one-liner from the manifest or the script):

```
python3 -B "$ST/legcount.py" --claim C
python3 -B "$ST/legcount.py" --claim Ca
```

Both must print `LEGCOUNT …: PASS (order and set equal)`, exit 0.

The manifest's emitted one-liners are the same check without the script:
`legcount.checks[0].command` / `.command_ordered` (claim C) and
`legcount.checks[1].command` / `.command_ordered` (claim Ca).

A leg name that is not `UPPER_SNAKE` fails by design: the draft still carries
`LEDGELIST?` in both claims' lists — **resolve it before writing `claims.json`**
(blocker FMB-1). A name swap, reorder, extra or missing leg is a freeze
blocker: regenerate `legs[]` from the counter, do not edit the counter to match
a typed list unless the L1 decides the counter is the wrong side.

## Step 3 — record the digests

```
python3 -B "$ST/manifest-check.py" --root . --record
```

Expected: `MANIFEST-FILE RECORD` per file, then
`MANIFEST r77: PASS files=18/18 pinned=18 … legs=2/2`, exit 0.
`--record` rewrites this directory's `manifest.json` only.

Digest rule: sha256 over the file's committed **blob** — `git -C . show
<freeze>:<path> | sha256sum`. The counters pin their by-document map the same
way (round-76 `accept-c.py` FROZENCFG), so the blob, not the worktree, is the
authority.

## Step 4 — commit the freeze

Stage exactly the 18 paths (plus whatever wave provenance the L1's freeze-set
lists; `manifest.json` `advisory[]` names the likely ones and is **not**
gated), commit, and record the commit as `<freeze>`.

Then, authoritative:

```
python3 -B "$ST/manifest-check.py" --root . --freeze <freeze>
```

Expected: `MANIFEST r77: PASS files=18/18 pinned=18 missing=0 unpinned=0
mismatched=0 legs=2/2`, exit 0. Anything else is a freeze blocker:

| verdict | meaning | fix |
|---|---|---|
| `MISSING` | the file is not in the commit | install it and amend/redo the freeze |
| `UNPINNED` | a `sha256` is still `<sha256-at-freeze>` | `--record`, then redo the freeze |
| `MISMATCH` | the committed blob ≠ the pinned digest | the commit did not carry the bytes you recorded |
| `LEGCOUNT … FAIL` | frozen `legs[]` ≠ the counter table | regenerate `legs[]` from `--print counter` |

`controls-receipt.txt` Section C is the measured proof of each of those
verdicts (C2 PASS, C3 worktree tamper still PASS, C4 MISMATCH, C5 revert PASS,
C6 MISSING, C7 LEGCOUNT FAIL, C8 direct `legcount.py --rev` FAIL).

## Step 5 — freeze receipts the manifest gates

The freeze commit must already carry `controls-c.txt`, `controls-ca.txt`,
`junk-c.txt`, `junk-ca.txt`, `selftest-c.txt`, `selftest-ca.txt` and
`gap-sweep.txt` (claim Ca's RECEIPTS leg fails on a cited receipt that exists
only in the worktree — the round-76 routed defect). Produce them **before**
Step 3 so their digests are pinned, and record each producing command at the
top of the file, as the round-76 receipts do.

## Step 6 — hand-off to the landings

Freeze-side is done when Step 4 prints PASS. Landings-side (not gated by this
manifest, listed as advisory): `reports/round-77/evidence/S897.txt`,
`S898.txt` at C-lands and the end census. Re-run Step 4 with the same
`<freeze>` after any amend.

---

## What this manifest does not do

- It does not measure any round-77 leg. The counters, claims and ledger do not
  exist yet; `build_state` records PENDING (exit 3) rather than a pass.
- It does not pin the wave-1 seat artefacts (`spec.json`, `dispatch.json`,
  `swarm-registry.json`, the reports under `.ufo/waves/round-77/w1/`) — the
  L1's own freeze-set decides whether those ride along.
- It does not decide which side of a LEGCOUNT divergence is right; it decides
  that the freeze cannot happen until both sides agree.
