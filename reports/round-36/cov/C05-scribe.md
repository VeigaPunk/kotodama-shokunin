- Seat: C05 | scribe | claim C | date 2026-10-19 | baseline ce103bf

# C05 — landed-changes material for the fleet report (claim C, coverage)

Mission (`reports/round-36/targets.json`, seat `C05`): "Landed-changes material."
Out path: `reports/round-36/cov/C05-scribe.md`. Binding rules: `targets.json:shared_rules`.

This seat supplies the `Landed changes` section material for this round's fleet report
(`/home/vgpnk/Projects/shokunin/.ufo/reports/round-36/kotodama.md`, integrator-authored,
absent at this read) plus the change-surface inventory the report's before→after rows
must agree with. Method: measure every surface claim C may move, pin a digest for each
at the declaration cut, hand the integrator paste-ready text and the recompute commands,
and name what is still owed.

Claim C (`reports/round-36/claims.json:22-27`) is: land the routed r35 timekeeping spare
as one new culture-material entry, with README reconciliation — `CM 24 / total 211` →
`CM 25 / total 212`, README rev 2.1 sweep-green (212 rows == 212 files), spare audited by
two auditors before landing, and "zero other count surfaces drift".

**No promotion, canon, clearance, closure or admission verdict is claimed in this file.**
Every such token below appears only as a negation, a routed reference, or a quoted
contract string. `reports/round-36/run-validation.py` was **not** executed (F-C13-1);
no `--freeze` was run. This seat wrote exactly one path: this file.

---

## §0 — Point-in-time state at this seat's read

- `date -u +%FT%TZ` → `2026-10-19T09:26:40Z` (first read), `2026-10-19T09:28:52Z`
  (last read of this section). `git rev-parse HEAD` →
  `ce103bf5885af00023cdc4a174c17602476cdcf8` (`ce103bf`, committed
  `2026-10-19T06:21:36-03:00`) — equal to the declared baseline
  (`reports/round-36/claims.json:8`, `baseline_expanded: ce103bf`; the r36 declaration
  uses the short form, not a full SHA).
- `find reports/round-36 -type f` → **4 files**: `claims.json`, `targets.json`,
  `telemetry/availability-attempt-1.json`, `telemetry/dispatch-declared.json`.
  **Zero seat fragments have landed.** Every row in §1 that names a seat fragment is
  therefore a declared requirement, not an observation.
- `git status --porcelain=v1 -uall` → exactly those 4 rows, all `??`. **No modified
  tracked path** anywhere in the tree.
- `git ls-files | wc -l` → **2903** tracked paths (protected subsets: `reports/**` 2093,
  `corpus/lessons/**` 179, `tools/gates/frozen/**` 237).
- Seat census from `reports/round-36/targets.json` (measured): **32 rows == declared
  `seat_count: 32`**, 32 unique `out` paths, no duplicate ids. Roles
  `{executor 12, scribe 6, verifier 4, scout 3, reviewer 3, critic 2, planner 1,
  connector 1}`; claims `{D 14, C 6, Ca 6, cross 6}`; out directories
  `{depth 10, cov 5, calib 5, scout 3, cross 3, review 3, scribe 2, plan 1}`.
- Dispatch: `telemetry/availability-attempt-1.json` records the hyper attempt failing
  **32/32 at launch** with `402 You're out of credits`, `launched_workers: 0`; the
  disposition names the declared fallback `devin/deepseek-v4-1-flash-high`. The observed
  route for this batch is **devin** — a named, REGIMEN-declared deviation
  (`REGIMEN.md` position 4: "hyper / deepseek-v4.1-flash; fallback
  devin/deepseek-v4-1-flash-high"). Requested allocation stays separate from the observed
  route below; no counter is inferred.
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-36/` → **absent** at this read;
  the fleet-root `MANIFEST.json` has **no round-36 row** (last row `round: 35`).

---

## §1 — Fleet-report `Landed changes` section (paste-ready draft)

Heading contract: the four required headings are `Work performed`, `Landed changes`,
`Before → after measurements`, `SHONEN` (`reports/round-35/run-validation.py:324-327`,
the `leg_close` heading loop; the same tuple at `reports/round-34/run-validation.py:319`).
Fill the `{{...}}` slots from the landed fragments, then verify every row with §3 before
filing. **Do not carry a `{{...}}` slot into the filed report** (C05-N6).

```text
## Landed changes

The round lands in one integrating pass after the wave. At the declaration cut
(`reports/round-36/claims.json`, sha256 b8d1af8f…) zero seat fragments had landed;
every row below is either a seat fragment landed during the wave or an integrator-applied
file. The claim-C deliverable is one new corpus entry plus a README reconciliation; the
claim-D deliverable (register-form content in the D4 packet lineage) touches
`examples/culture-d4/**` and `tools/**` and is listed here only as the D block's
surface, not as a C row.

- `corpus/knowledge/culture-material/timekeeping-instruments.md` — **one new entry**,
  the routed r35 spare landed unmodified: its fenced block is byte-identical to the
  entry r35 already audited (40,234 bytes incl. trailing newline, sha256
  `9805c0b854334ed3…` — equal to the digest pinned at
  `reports/round-35/cov/C13-audit-1-5.md:197` and passed clean at
  `reports/round-35/review/R01-c-review.md:25`). Before: absent (partition = 24 files,
  aggregate digest `1037cd14…`). After: `{{digest}}`. Re-audited against the post-r35
  tree by {{auditor seats}} (the claim's two-auditor bar, `claims.json:27`).
- `corpus/README.md` — revision **2.1** reconciliation for the one addition: the
  `## culture-material/` header `(24)` → `(25)`, one new row generated byte-equal from
  the landed entry's own `- topic:` text, the totals line `211.` → `212.`, the counts
  footer `(total 211 files; directory totals 21/23/24/29/20/94).` →
  `(total 212 files; directory totals 21/23/25/29/20/94).`, a new dated index paragraph,
  and (drafted at §5) the repair of two pre-existing defects in the same section.
  Before `51b966af…` (523 lines, 125,229 bytes, 211 rows) → after `{{digest}}`.
  Re-measured: `{{sweep output}}`.
- `reports/round-36/` — the round record: `claims.json` + `targets.json` (declared),
  {{N}} seat fragments, `run-validation.py` + `validation.json` (integrator-authored; no
  seat executed the runner).
- `reports/round-36/telemetry/` — `dispatch-declared.json` (filed, `48cbee5a…`) and
  `availability-attempt-1.json` (the hyper 402, `ecbcdd4c…`), plus the observed-dispatch
  record and the closing snapshot `availability-close-36.json` owed once
  `validation.json` lands (AGENTS.md close-what-you-open).
- Claim-D surfaces (not this claim's rows): `examples/culture-d4/**`, the D4
  assembly/typed tools, and every expected.json/baseline the register content
  invalidates — drafted by the D block, applied by the integrator.
- Filed bytes: **zero** writes to `reports/round-1..35/**`, `corpus/lessons/*.md`,
  `tools/gates/frozen/**` (§3.1 measured 0 dirty rows; 2509 tracked paths in the
  protected set), and the `reports/round-34/handoff/declared-in-r7` freeze pair stays
  pinned at `45f57132…` (no re-freeze). **Caveat that must accompany this row:**
  peer seats ran filed round runners in-tree during this window, transiently
  rewriting `reports/round-35/validation.json` and `reports/round-34/validation.json`
  (one of them to `acceptance_checks_passed: false`) before both returned to their
  filed bytes — see §3.5. Re-measure the protected prefixes at close rather than
  quoting a single clean reading.
- Seat fragments: {{landed}} of 32 declared `out` paths landed (26 files present at
  09:32Z, including both spare auditors and the K02 scout); {{missing list}}
  recorded in `missing_dependencies`.
- **Claim-C scope note (from §7.1, K02-F1/F2):** if the entry lands as the *unedited*
  r35 fenced bytes, the row above must say so, and the receipt must record that the
  entry carries a present-tense measurement taken at `4a7aede` (pre-r35) — the
  round-28 counts-footer defect class. The re-measured `- gap filled:` / `couples:`
  variant is the other reading; the auditors own the verdict.
```

---

## §2 — Change-surface inventory (before digests measured; after slots owed)

Every `before` value below was measured by this seat on 2026-10-19 at HEAD `ce103bf`
with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` (commands in §3.3).

| surface | class | drafted by | applied by | before (measured 2026-10-19) | after |
|---|---|---|---|---|---|
| `corpus/knowledge/culture-material/timekeeping-instruments.md` | new file | routed from r35 C04 (`reports/round-35/cov/C04-timekeeping-spare.md`) | integrator | absent; partition 24 files, aggregate `1037cd14…`; spare block 40,234 B / 140 lines @ `9805c0b8…` | {{digest}} |
| `corpus/README.md` | edit | C02 (delta draft) + this file (§5) | integrator | `51b966af…`, 523 lines, 125,229 bytes, 211 rows, rev 2.0 | {{digest, lines, rows}} |
| `corpus/knowledge/` (total) | census | — | — | 211 files, aggregate `8d13ffff…` | 212 / {{digest}} |
| `corpus/knowledge/{linguistics,myth-symbol,synthesis,verification,civilizations}` | census | — | — | 21 / 23 / 29 / 20 / 94 (aggregate digests §3.2) | must be **unchanged** |
| `reports/round-36/**` seat fragments | new files | seats | seats (own `out`) | 0 of 32 landed at 09:28Z | {{landed count}} |
| `reports/round-36/run-validation.py`, `validation.json` | new files | integrator | integrator | absent | exit 0 / receipt digest |
| `reports/round-36/telemetry/observed-dispatch.json`, `availability-close-36.json` | new files | integrator | integrator | absent; `dispatch-declared.json` `48cbee5a…`, `availability-attempt-1.json` `ecbcdd4c…` | close names `closes` + `closes_sha256` |
| `reports/round-36/cov/C01-audit.md`, `C02-audit-delta.md`, `C03-verify.md`, `C04-receipt.md`, `C05-scribe.md` | new files | C seats | C seats | absent | {{landed}} |
| `/home/vgpnk/Projects/shokunin/.ufo/reports/round-36/kotodama.md` | new file | integrator | integrator | directory absent at 09:26Z | 4 headings + ISO date + runner citation |
| `/home/vgpnk/Projects/shokunin/MANIFEST.json` | edit (fleet root) | integrator | integrator | last row `round: 35` (250 rows; no round-36 row) | round-36 row |
| `SCORECARD.md` `9b62f687…`, `LOG.md` `007ce7f9…` | append-only | integrator | integrator | as measured §3.4 | new rows only |
| `examples/culture-d4/**` aggregate `a333b0f9…`, `tools/**` | claim **D** surfaces | D block | integrator | as measured §3.4 | D's rows, not C's |

Never-move set (see §3.1): `reports/round-1..35/**`, `corpus/lessons/*.md` (33 `.md`
under `corpus/lessons/` per `ls corpus/lessons/*.md | wc -l`; 179 files total under the
directory), `tools/gates/frozen/**` (237 tracked paths), the 211 pre-existing
`corpus/knowledge/**/*.md`, and the `declared-in-r7` freeze bytes.

---

## §3 — Preservation legs and recompute commands

### §3.1 Protected prefixes (measured clean at `ce103bf`)

- `git status --porcelain=v1 -uall -- reports/round-{1..35} corpus/lessons
  tools/gates/frozen` → **0 rows**; `git diff --stat ce103bf -- reports corpus/lessons
  tools/gates/frozen` → **empty**. **2509** tracked paths are in the protected set
  (`reports` 2093 + `corpus/lessons` 179 + `tools/gates/frozen` 237).
- **But the clean reading is not stable in this window** — peers are running filed
  round runners **in-tree**, so filed receipts go dirty and return while a reader
  works. See §3.5; the report must not quote a single protected-prefix reading as
  if it were a settled property of the window.
- The freeze pin survives unchanged:
  `sha256sum reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,claims-map.md,expected.json,freeze.txt}`
  → `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`,
  `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`,
  `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`,
  `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`,
  `3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223`
  (equal to `R7_PINS` at `reports/round-35/run-validation.py:28-31`). No `--freeze`
  was run by this seat.

### §3.2 Corpus baseline (the 211-file set the one addition must not disturb)

- Census: linguistics 21 / myth-symbol 23 / culture-material 24 / synthesis 29 /
  verification 20 / civilizations 94 = **211**; `git ls-tree -r --name-only ce103bf --
  corpus/knowledge | wc -l` → **211** (baseline commit agrees with the working tree, so
  the one addition is the only delta).
- Aggregate digest over the sorted 211 files:
  `find corpus/knowledge -name '*.md' | sort | xargs sha256sum | sha256sum` →
  `8d13ffffaf75c04e84b90a7457930e49f84de814be1bdd52a818aa6d53d7de3b`.
- Per-partition (same command scoped per directory): linguistics `c6248d92…`,
  myth-symbol `66dd6850…`, culture-material `1037cd14…`, synthesis `d6fdacc4…`,
  verification `b88fc106…`, civilizations `d1c50bf4…`.
  Note for the report: the `myth-symbol` and `culture-material` digests recorded in the
  r35 scribe material (`reports/round-35/cov/C16-scribe.md` §3.2, `da0505ad…` /
  `ef0560da…`) were taken over the **pre-r35 19/18-file** sets; the live values are the
  ones above. This is an expected consequence of r35's landing, not a mismatch.
- Inventory tool at the same cut: `python3 -B tools/source-audit-inventory.py --json
  --summary --root corpus/knowledge` → `totals.files: 211` (the claim's own counting
  command; after = 212). `--selftest` → PASS.

### §3.3 Recompute commands (run these before filing the report)

```bash
# seat-fragment landing census (do not trust §0's snapshot)
python3 -c "import json,os;t=json.load(open('reports/round-36/targets.json'));print([s['out'] for s in t['seats'] if not os.path.isfile('reports/round-36/'+s['out'])])"
find reports/round-36 -type f | wc -l
# the one addition must be the ONLY corpus delta: expect exactly 1 ?? row
git status --porcelain=v1 -uall -- corpus/knowledge
comm -13 <(git ls-tree -r --name-only ce103bf -- corpus/knowledge | sort) \
         <(find corpus/knowledge -name '*.md' | sort)
# protected bytes: expect 0
git status --porcelain=v1 -uall -- reports corpus/lessons tools/gates/frozen \
  | grep -vE '^\?\? reports/round-36/' | wc -l
# after-digests for the two C surfaces
sha256sum corpus/README.md corpus/knowledge/culture-material/timekeeping-instruments.md
# freeze pin: expect the five digests of §3.1
sha256sum reports/round-34/handoff/declared-in-r7/*
# claim-C counting commands, verbatim from claims.json:26
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
python3 -B reports/round-28/readme/sweep.py
# row order + in-section blanks (the leg the sweep does NOT have — see C05-N1)
python3 - <<'EOF'
import re
lines=open('corpus/README.md').read().split('\n')
h=[(i,l) for i,l in enumerate(lines) if re.match(r'^## [a-z-]+/ \(',l)]
for k,(i,l) in enumerate(h):
    end=h[k+1][0] if k+1<len(h) else len(lines)
    names=[re.match(r'^- `([^`]+\.md)`',lines[j]).group(1) for j in range(i+1,end) if re.match(r'^- `[^`]+\.md`',lines[j])]
    blanks=[j+1 for j in range(i+1,end) if lines[j].strip()=='' and j not in (i+1,end-1)]
    if names!=sorted(names): print("OUT-OF-ORDER", l, [ (a,b) for a,b in zip(names,sorted(names)) if a!=b ])
    if blanks: print("IN-SECTION BLANKS", l, blanks)
EOF
```

### §3.4 Shared-surface digests (for the report's preservation row)

`sha256sum` at `ce103bf`, repo root:
`SCORECARD.md 9b62f687…`, `LOG.md 007ce7f9…`, `SKILL.md f9bd07c2…`,
`AGENTS.md 5ae7a9c8…`, `PROVINCE.md 05b34a57…`, `MINT.md a06f5e4d…`,
`SHONEN.md 7999d09b…`, `REGIMEN.md efb1bc3b…`, `corpus/QUALITY.md 6aab8800…`,
`corpus/lessons/README.md f752e1d7…`, `tools/check-gate-battery.py 455b595a…`,
`tools/source-audit-inventory.py f617bb99…`, `reports/round-28/readme/sweep.py
9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` (equal to the r35
C11 pin), aggregate `examples/**` `a333b0f9…`, aggregate `corpus/lessons/**`
`39b5a6c9…`. Instrument controls re-run this round by this seat:
`python3 -B reports/round-28/readme/sweep.py --selftest` → `selftest: 12/12 checks
passed`, exit 0; `python3 -B tools/check-gate-battery.py --selftest` → `SELFTEST OK
44/44 controls behaved as expected`, exit 0;
`python3 -B tools/harness/receipt_guard.py --selftest` → `selftest_passed: true`.

### §3.5 Live in-tree runner execution by peer seats (observed, not inferred)

While this seat was pinning §3.1/§3.2, a **filed** round receipt went dirty and then
returned to its filed bytes inside the same minute. The movement is measured, and so is
its cause.

**Observation 1 — `reports/round-35/validation.json`:**

| `date -u` | sha256[:16] | `git diff` lines |
|---|---|---|
| `2026-10-19T09:26:40Z` (first read) | `328e97b39eff69f4` (filed) | 0 |
| `2026-10-19T09:29:26Z` (mtime) | `8cd9d98ef9931853` | 6 (2 insertions, 4 deletions) |
| `2026-10-19T09:29:59Z` (mtime) | `328e97b39eff69f4` (filed) | 0 |

The transient revision differed in exactly two fields: the `X1-X3` leg's
`measurement.manifest` note was emptied to `{}`, and `measured_at_utc` moved from
`2026-10-19T06:19:14.685566-03:00` to `2026-10-19T06:29:26.436020-03:00`. The filed
digest is `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`
(equal to the digest quoted in `SCORECARD.md:637-638` and `LOG.md`), so the filed state
was restored and **no filed byte survives changed**.

**Observation 2 — `reports/round-34/validation.json` went dirty and stayed dirty for
at least 75 seconds, with its verdict flipped:**

| `date -u` | sha256[:16] | `acceptance_checks_passed` |
|---|---|---|
| filed (`ce103bf`) | `ba2fa4dcf8f29a13` | `true` |
| `2026-10-19T09:30:35Z` | `72733e3254a0c0f7` | — (dirty) |
| `2026-10-19T09:30:47Z` | `1f115eeaab528d52` | **`false`** |
| `2026-10-19T09:31:24Z` | `ba2fa4dcf8f29a13` | `true` |

The dirty revision's `O` claim read `passed: false` with
`"O1-O5: O2: inventory counts differ: 30 runners, {'guarded-refresh': 19,
'unguarded-in-place': 11}"` and leg status `failed`, against the filed
`guarded-refresh: 18` / `passed: true`. The count moved because a round-36 instrument
now exists to be counted.

**Cause (proven from `/proc`, not inferred):** peer seat processes were running
**filed round runners with `cwd` = the live repo root**:

```
$ ps -eo pid,lstart,args | grep run-validation.py
1036741 Mon Oct 19 06:29:50 2026 python3 -B reports/round-35/run-validation.py
1051278 Mon Oct 19 06:30:26 2026 python3 reports/round-34/run-validation.py
$ readlink /proc/<pid>/cwd
/home/vgpnk/Projects/shokunin/kotodama-shokunin
```

`reports/round-{34,35}/run-validation.py` hard-code an absolute `ROOT`
(`:10` and `:9` respectively), call `os.chdir(ROOT)` (`:36` in both), and — invoked
**without** `--check` — write `f"{ROUND}/validation.json"` unconditionally
(`reports/round-35/run-validation.py:502-503`; `--check` returns before the write at
`:496-499`). One further process ran the runner with `--check` but also with live-root
`cwd` (PID 1036711), which is why the transient r35 revision reproduced too — the
absolute `ROOT` means even a `.scratch/*/clone` copy writes into the live repo, so
`cd` into a clone does **not** isolate these runners (one peer worked around this with
`mount --bind`; another used `git archive`).

**The guard did not stop it, and the reason is environmental:** a read-only probe
against the live receipt returns refusal, not a write —

```
$ python3 -B tools/harness/receipt_guard.py reports/round-35/validation.json
receipt_guard: refusing overwrite path=reports/round-35/validation.json
committed_sha=ce103bf5885af00023cdc4a174c17602476cdcf8 committed_blob=11f241a4…;
explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]
exit=3
```

— so the writers held `REFRESH_RECEIPTS=1` in their own process environment
(`tools/harness/receipt_guard.py:16-17`: "Only the exact environment value
`REFRESH_RECEIPTS=1` permits a committed receipt write"). That variable is not set in
this seat's environment and this seat set it in no command.

**This seat's own conduct:** no `reports/round-*/run-validation.py` was executed by
this seat in or out of tree, no `REFRESH_RECEIPTS` was set, and the only path this seat
wrote is this file. Every digest in §2/§3.2/§3.4 was read with `sha256sum`/`git show`,
never by a runner. Any consumer of this window's digests should re-measure (§3.3) rather
than trust §3.1's single clean reading, because peers are still writing.

---

## §4 — Coverage before → after anchors (must agree with §1's rows)

| surface | before (measured `ce103bf`) | after required (`claims.json:24-27`) | proof |
|---|---|---|---|
| culture-material partition | 24 files | 25 | `ls corpus/knowledge/culture-material/*.md \| wc -l` |
| corpus total | 211 | 212 | `ls corpus/knowledge/*/*.md \| wc -l`; inventory `totals.files` |
| README index rows | 211 (`corpus/README.md`, `51b966af…`, 523 lines) | 212 | `grep -c '^- \`[A-Za-z0-9._-]*\.md\`' corpus/README.md` |
| README section header | `corpus/README.md:186` = `## culture-material/ (24)` | `(25)` | `grep -n '^## [a-z-]*/ (' corpus/README.md` |
| README totals line | `corpus/README.md:492` = `Total knowledge entries: 211.` | `212.` | `sed -n '492p' corpus/README.md` |
| README counts footer | `corpus/README.md:496` = `(total 211 files; directory totals 21/23/24/29/20/94).` | `21/23/25/29/20/94`, total 212 | `sed -n '496p' corpus/README.md` |
| README revision block | `corpus/README.md:3` = `revision: 2.0 — Round-35 …` | `revision: 2.1 — Round-36 …` | `sed -n '3p' corpus/README.md` |
| other five partitions | 21/23/29/20/94 | **unchanged** | six-part census; `header_drift {}` |

Row-sort convention (measured, not assumed): rows are filename-sorted (ASCII ascending)
inside every section. At `ce103bf` **one section is out of order** and one carries an
in-section blank — see C05-N1.

---

## §5 — README delta draft for the claim-C landing (one row + two repairs)

This seat wrote **no** byte of `corpus/README.md`. The integrator applies; the bytes
below are a tested draft, and every count surface moves together (C05-N3).

### E1 — new revision block (insert after line 2, i.e. above the current `revision: 2.0`)

```text
revision: 2.1 — Round-36 timekeeping-material landing (2026-10-19): the routed
round-35 spare (`reports/round-35/cov/C04-timekeeping-spare.md`, block sha256
`9805c0b854334ed3…`) landed as `culture-material/timekeeping-instruments.md`.
`## culture-material/` moved 24 → **25**; the row was added in filename order
with the entry's own `- topic:` text byte-equal; the totals line and the counts
footer moved 211 → **212** and the footer vector 21/23/24/29/20/94 →
**21/23/25**/29/20/94. Two pre-existing defects in the same section were
repaired in this revision: `fire-fuel-light.md` was filed out of filename order
(after `funerary-material-culture.md`) and a blank line split the section before
`writing-media-surface-economy.md`. Non-canon examples and passing structural
gates do not certify historical truth.
```

Precedent for block shape and the closing sentence: `corpus/README.md:3-15`
(revision 2.0) and `:17-30` (the round-28 block). Revision numbering follows the file's
0.1-step convention (`1.4→…→1.9→2.0`), so the next value is **2.1**; if the integrator
prefers `2.10`, that is a naming decision, not a byte risk.

### E2 — section header (line 186)

```
-## culture-material/ (24)
+## culture-material/ (25)
```

### E3 — row order repair inside the section (delivered bytes are wrong)

Delivered order at `ce103bf` is **not** filename-sorted; the deviation is measured, not
asserted:

| row position | delivered | filename order requires |
|---|---|---|
| 11 | `furniture-interior-lexicon.md` (line 198) | `fire-fuel-light.md` |
| 13 | `fire-fuel-light.md` (line 200) | `furniture-interior-lexicon.md` |

Move the `fire-fuel-light.md` row to immediately before the
`furniture-interior-lexicon.md` row (i.e. to line 198's position). The row's own bytes
are unchanged — this is a move, not an edit.

### E4 — in-section blank repair (line 211)

At `ce103bf` line 211 is a blank line between `warrior-material-culture.md` (210) and
`writing-media-surface-economy.md` (212), splitting the section. Delete it so the last
row abuts the next section header, matching every other section (measured: the only
in-section blank in the six index sections; the `## civilizations/` section carries
blanks only **after** its last row, in the `Known gaps` prose that follows it).

### E5 — new row, generated from the landed entry's bytes (never retyped)

```text
- `timekeeping-instruments.md` — <the entry's own `- topic:` text, continuation-joined>
```

Measured from the routed spare's fenced block: the `- topic:` field is a **single
logical line** (no continuation lines between `- topic:` and `- gap filled:`), so the
continuation-join is a no-op here. Row bytes generated by the lane instrument's own
`topic_of` (`reports/round-28/readme/sweep.py:74-79`) →
**1741 bytes**, `sha256 49e67b35d3df34bd568d18ba82299c78d59861735c2c4a7cb3f3e7121c7c0982`;
the topic text alone is 1706 bytes, `sha256 8ec2f6cab0d6b9dd4f6b9cbbd09c55fc6e25f016751a3b37dc4d7bab1a7ef59b`.
Insert position: after the `textile-technology.md` row and before the
`trade-economy-lexicon.md` row (filename order). **Regenerate from the landed entry at
integration time** — the digest above is a cross-check, not the source.

### E6 — totals line (line 492) and counts footer (line 496)

```
-Total knowledge entries: 211.
+Total knowledge entries: 212.
```

```
-(total 211 files; directory totals 21/23/24/29/20/94).
+(total 212 files; directory totals 21/23/25/29/20/94).
```

Line 494 (`Counts checked 2026-10-19 from the repo root:`) and line 495 (the inventory
command) stay as they are; line 497 (`The inventory counts markers, not verified
facts.`) is unchanged. The footer's superseded-reading paragraph (`:498-506`) is
**append-only** per the file's own rule (`corpus/README.md:498-505`): append a new
sentence recording the 211 → 212 move rather than rewriting the r35 sentence.

### E7 — new dated index paragraph (append after line 523, the last line)

```text
Index rows re-measured 2026-10-19 at HEAD `ce103bf` plus the round-36 working tree
by this round's claim-C sweep (212 rows vs 212 files; the timekeeping row added to
the culture-material section; 0 missing, 0 ghosts, 0 duplicate rows, 0 header drift,
0 topic mismatches; partition counts 21/23/25/29/20/94).
```

### §5.1 Acceptance measured on a projected tree (this seat's own control)

This seat built a synthetic 212-file knowledge tree under `.scratch/c05/` (the live 211
files plus the extracted spare at
`.scratch/c05/kn/culture-material/timekeeping-instruments.md`), applied E1-E7 to an
in-memory copy of the live README, and ran the lane instrument against the projection:

```
python3 -B reports/round-28/readme/sweep.py   (imported in-process; root_override=.scratch/c05/kn)
ok True   total_rows 212   total_files 212   missing_from_index []   orphan_rows []
topic_mismatch []   header_drift {}   totals_line 212   totals_ok True
footer_ok True   footer_findings []
parts {linguistics 21, myth-symbol 23, culture-material 25, synthesis 29, verification 20, civilizations 94}
projected README: 541 lines, 128,104 bytes, readme_sha256 4b1dff4176e3ee30c6e7fd76fbf1134794158b4a6ef3dda1cc22903f178cef5f
```

The projected digest is a property of **this seat's draft bytes**, not of what the
integrator will file — the after-digest in §2 stays owed.

Negative controls on the same projection (the instrument is discriminating, so the green
above is evidence rather than tautology):

| control | mutation | instrument verdict |
|---|---|---|
| rewritten topic | one word changed in the new row | `ok False`, `topic_mismatch [{row: culture-material/timekeeping-instruments.md, class: REWRITE, row_chars 1692, topic_chars 1696}]` |
| ghost row | filename typo'd to `timekeeping-instrument.md` | `ok False`, `missing_from_index [culture-material/timekeeping-instruments.md]`, `orphan_rows [culture-material/timekeeping-instrument.md]` |

### §5.2 Drafted tool change — the sweep's missing order/blank leg (fenced, integrator applies)

The round-28 instrument (`reports/round-28/readme/sweep.py`, digest `9b2ccac0…`) has
**no row-order leg and no in-section-blank leg**; this seat measured that both defects
of §5 E3/E4 pass it green (controls in §5.3). The leg is drafted here as a fenced
addition; `reports/round-28/readme/sweep.py` is a filed-round tool and is **not** edited
by this seat (filed bytes are frozen). Two options for the integrator, in preference
order: (a) add the leg to a **new** round-36 instrument and leave r28's bytes alone, or
(b) land the same check in `tools/` as a new read-only gate. Either way the check is:

```python
def leg_row_order(sections, root):
    """Rows must be filename-sorted inside every section; no blank line may
    split a section's rows. Returns a list of finding dicts (empty == clean)."""
    findings = []
    for part, sec in sections.items():
        files = [f for f, _ in sec["rows"]]
        if files != sorted(files):
            findings.append({"class": "ROW_ORDER", "part": part,
                             "mismatched": [[a, b] for a, b in zip(files, sorted(files)) if a != b]})
    return findings
```

with the blank-line half expressed against the raw section slice (`body.split("\n")`
between a section header and the next header: any blank line strictly between the first
and last row line is a finding `{"class": "SECTION_BLANK", "part": part, "line": n}`).

### §5.3 Measured controls behind C05-N1 (the defects the sweep misses)

Run in-process against the live README with `reports/round-28/readme/sweep.py`:

| mutation | instrument verdict |
|---|---|
| swap the `furniture-interior-lexicon.md` / `fire-fuel-light.md` rows (the live defect) | `ok True`, `missing_from_index []`, `orphan_rows []`, `topic_mismatch []`, `header_drift {}`, `totals_ok True`, `footer_ok True` |
| delete the blank line at 211 (removes the live defect) | `ok True`, same empty findings |

Both directions pass, so the instrument cannot see the class of defect it is being asked
to certify. This is a finding about the instrument's coverage, **not** a claim that the
r35 sweep was wrong about what it does measure (rows/files/ghosts/topics/totals/footer).

---

## §6 — Findings (owner-assigned, none blocking the claim as written)

- **C05-N1 (the round-28 sweep has no row-order or in-section-blank leg).** Evidence:
  §5.3 — the live out-of-order pair and the live in-section blank both pass the
  instrument; `reports/round-28/readme/sweep.py` contains no order comparison
  (`grep -n 'sorted(' reports/round-28/readme/sweep.py` hits only `disk_files` and
  finding lists, never the row list). Consequence: "sweep-green" is a weaker claim than
  the README's own revision blocks imply, and r35's revision 2.0 block asserts the ten
  rows were "added in filename order" while the delivered file is out of order in that
  section. **Owner: integrator** (route to the r36 instrument or a new `tools/` gate,
  draft in §5.2). Not fixed by this seat.
- **C05-N2 (the r35 README landing left two defects in `culture-material/`).** Measured
  at `ce103bf`: `fire-fuel-light.md` filed at line 200, i.e. after
  `funerary-material-culture.md` (line 199), where filename order puts it before
  `furniture-interior-lexicon.md` (line 198); and a blank line at 211 splits the section
  before its last row. Both are inside the claim-C surface and are drafted for repair in
  §5 E3/E4. **Owner: integrator.** This seat edited no filed byte.
- **C05-N3 (README has four count surfaces, not one).** Header, totals line, footer
  vector and the row set must move together; moving only some reproduces the round-20 /
  round-33 reconciliation failure class (`corpus/README.md:30-49`, the revision 1.8
  record). The claim's own thresholds say "zero other count surfaces drift"
  (`claims.json:27`), so §4 lists every one.
- **C05-N4 (the spare is already an audited artifact, not a new draft).** The routed
  spare's fenced block is byte-identical to the entry r35 audited: 40,234 bytes incl.
  trailing newline, `9805c0b854334ed396119476b6278cc4f58eb1014a0b06eb6bba561def05f0a6`
  = the digest pinned at `reports/round-35/cov/C13-audit-1-5.md:197`
  (`sha256[:16] 9805c0b854334ed3`, 40 234 bytes) and passed clean at
  `reports/round-35/review/R01-c-review.md:25`. **Consequence for the claim's
  two-auditor bar (`claims.json:27`):** what is owed is a re-audit against the
  **post-r35 tree** (pointer resolution, couples targets, duplication against the new
  neighbours) — the entry bytes themselves need no re-authorship. Its own frontmatter
  already carries the eight fields (`- topic:`, `- gap filled:`, `- sources:`,
  `- source:`, `- couples:`, `- verified-at:`, `- recheck:`, `- scope:`), 7 `(to-verify)`
  marks, and 27 `corpus/**.md` pointers of which **0 are dangling** at `ce103bf`.
- **C05-N5 (no invented landed paths).** Every path in the filed `Landed changes`
  section must exist at filing time; run §3.3 first and do not carry `{{...}}` slots
  into the report.
- **C05-N6 (telemetry close).** The closing snapshot is a new file
  `reports/round-36/telemetry/availability-close-36.json` carrying `closes` +
  `closes_sha256` (the `dispatch-declared.json` digest `48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16`
  at this read, or the digest read at close time) so a later in-place edit is detectable;
  unknown counters stay `null` with an owner and reason (AGENTS.md availability rules).
  The observed route (devin, after the hyper 402) belongs in the observed record, not in
  `claims.json` — never edit the declaration.

---

## §7 — Wave-progress addendum (and the peer-fold)

`find reports/round-36 -type f` at `2026-10-19T09:28:52Z` → **4 files**: the two
declarations and the two telemetry records of §0. **No seat fragment had landed**, so
§0's statement is true at its own timestamp; this section is appended, not a rewrite of
§0. At `2026-10-19T09:32:08Z` the same command → **26 files**: peers landed the
C/K/P/D/Calib/review fragments during this seat's window.

### §7.1 — Peer fragments landed during the window, and what they change here

Read at `2026-10-19T09:32Z`; each is another seat's file and this seat edited none of them.

- **`reports/round-36/cov/C02-audit-delta.md` independently reports the same two README
  defects and the same instrument blind spot** as C05-N1/C05-N2 (its findings **F1**, **F2**,
  **F3**; `:161-163`, §4.4). Its F2 additionally counts **three** rows out of ASCII order
  (lines 198–200) where §5 E3 of this file names the pair that actually differs; this seat
  re-measured and confirms both readings are consistent — three rows occupy non-sorted
  positions, and exactly two of them are swapped (the `funery`/`furniture` pair), the third
  (`funerary-material-culture.md`) sitting between them is displaced but not itself
  transposed. **The integrator should follow C02's E3 (re-sort lines 198–200) over this
  file's narrower E3**, and C02's §4.4 order/contiguity leg over this file's §5.2 draft.
  Two seats, two instruments, one reading — so C05-N1 is not a single-seat claim.
- **`reports/round-36/cov/C03-verify.md`** independently files the same README defect as its
  **F1** and confirms the pre-landing blob was clean.
- **`reports/round-36/scout/K02-timekeeping-scout.md` materially qualifies the claim's own
  premise.** Finding **K02-F1** (`:30-...`): the spare's `- gap filled:` line asserts a
  measurement taken at `4a7aede`, i.e. **before the r35 wave**, and re-running its own
  commands over the current 211-file tree moves several counts — the spare's "0 for every
  term" sentence is now false (`curfew` → 1 file, `fire-fuel-light.md`), and `hour` 8 → 17,
  `bell` 81 → 87, `clock` 6 → 10 in culture-material, `chronometer` 2 → 4, night watch
  1 → 2. Finding **K02-F2**: the spare's `couples:` names 24 paths, all resolving, but
  **none of the ten r35 entries**, including `fire-fuel-light.md`, which now owns the
  curfew / night-watch / risk-apparatus surface the spare also claims.
  **Consequence for this file's `Landed changes` section:** the claim-C deliverable cannot
  be described as "land the spare unmodified". §1's row has been corrected accordingly —
  the entry bytes need a **re-measured `- gap filled:` line and a `couples:` line that
  names the landed sibling** before or as they land, which is a byte change inside the
  fenced block and therefore an **auditor-visible scope question for the claim**, not a
  scribe's edit. This seat did not author those bytes; the two auditors (C01/C02) own the
  verdict and the integrator owns the apply.
- **`reports/round-36/cov/C01-audit.md`** independently confirms the spare is unlanded, its
  structural contract passes on two instruments, and its one review item is a false
  positive.

### §7.2 — The one row §1 must not overstate

Given §7.1, the honest `Landed changes` row for the corpus entry is: *the r35 spare landed
at `culture-material/timekeeping-instruments.md` with its `- gap filled:` and `couples:`
lines re-measured against the post-r35 tree (K02-F1/F2), the entry bytes otherwise the r35
audited bytes at `9805c0b8…`*. If the integrator lands the fenced bytes **unedited**, the
row must say so and the receipt must record that the entry carries a present-tense false
measurement — the round-28 counts-footer defect class (`corpus/README.md:30-49`,
`corpus/lessons/round-28.md:80`). This seat takes no position on which the integrator
chooses; it reports both readings.

---

## Owed

Everything below is owed at this file's cut. Exact paths:

- `reports/round-36/cov/C01-audit.md`, `reports/round-36/cov/C02-audit-delta.md` — the
  two independent spare audits (claim-C threshold `claims.json:27`) and the README
  delta draft; fills the `{{auditor seats}}` slot in §1 and cross-checks §5.
- `reports/round-36/cov/C03-verify.md` — the verifier's own measurement of the audit
  numbers and the delta (§4's after-column).
- `reports/round-36/cov/C04-receipt.md` — the coverage receipt draft.
- `reports/round-36/scout/K02-timekeeping-scout.md` — the spare's gap statement
  re-verified against the post-r35 tree.
- Integrator-only, absent at this read: the applied `corpus/knowledge/culture-material/timekeeping-instruments.md`
  and its after-digest; the applied `corpus/README.md` bytes and their after-digest
  (523 → {{lines}}); `reports/round-36/run-validation.py` + `validation.json`;
  `reports/round-36/telemetry/observed-dispatch.json` +
  `availability-close-36.json`; `/home/vgpnk/Projects/shokunin/.ufo/reports/round-36/kotodama.md`;
  the fleet-root `MANIFEST.json` round-36 row; the `SCORECARD.md` / `LOG.md` rows.
- Decision owed (not bytes): whether the §5.2 order/blank leg lands as a new r36
  instrument leg or as a new `tools/` gate (C05-N1), and whether E3/E4 are repaired in
  the same revision-2.1 edit or filed as separate rows.

---

## Citations

- `reports/round-36/claims.json:8,16-21,22-27,28-33,34,35-40` — baseline `ce103bf`,
  claims D/C/Ca with `before`/`after_required`/counting commands/thresholds, the
  freshness pause, non-goals.
- `reports/round-36/targets.json:1-5,6-11,31` — `round: 36`, `seat_count: 32`,
  `shared_rules`, C05's own row (`cov/C05-scribe.md`, mission "Landed-changes
  material.").
- `reports/round-36/telemetry/dispatch-declared.json` (digest
  `48cbee5a…`; `closing_snapshot: open-at-seat-close`);
  `reports/round-36/telemetry/availability-attempt-1.json` (digest `ecbcdd4c…`;
  `402 You're out of credits`, `launched_workers: 0`, `failed_workers: 32`, the
  declared devin fallback disposition).
- `REGIMEN.md` — position-4 schedule row (hyper with the declared devin fallback), the
  per-round contract, and the round-record requirements.
- `AGENTS.md` — availability/dispatch telemetry rules (durable samples,
  requested-vs-observed separation, unknown counters `null`, close-what-you-open,
  digest-pinned closing snapshot).
- `reports/round-35/cov/C04-timekeeping-spare.md:1-11` — the routed spare and its
  fenced block; block bytes 40,234, `9805c0b8…`; extraction and `topic_of` readings
  measured this round.
- `reports/round-35/cov/C13-audit-1-5.md:197` and
  `reports/round-35/review/R01-c-review.md:25` — the r35 audit pins for the same bytes.
- `corpus/README.md:3-15` (revision 2.0 block), `:17-30` (round-28 block),
  `:186` (culture-material header), `:198-200,211-212` (the out-of-order pair and the
  in-section blank), `:492` (totals line), `:494-497` (footer block), `:498-505`
  (superseded-reading rule), `:520-523` (last dated paragraph).
- `reports/round-28/readme/sweep.py:21-22,59-61,66,74-79,86-92,101,108,140,165-208` —
  the row/topic/section/footer regexes, `topic_of`, `disk_files`, and the measured
  absence of any row-order comparison; digest `9b2ccac0…`, `--selftest` 12/12.
- `reports/round-35/run-validation.py:20,24-31,147-195,319-360` — the fleet-report
  path, the `R7_PINS` tuple (equal to the live freeze digests), the coverage leg
  (partition census, inventory 211, sweep green, README needles, audits, new-entry
  pointers) and the close leg (the four required headings).
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `date -u +%FT%TZ`; `git rev-parse HEAD`;
  `git log -1 --format='%H %cI' ce103bf`; `git status --porcelain=v1 -uall`;
  `git ls-files | wc -l`; `git ls-files -- reports corpus/lessons tools/gates/frozen
  | wc -l`; `git ls-tree -r --name-only ce103bf -- corpus/knowledge | wc -l`;
  the six-partition `ls | wc -l` census; the aggregate and per-partition
  `sha256sum | sha256sum` digests; `python3 -B tools/source-audit-inventory.py --json
  --summary --root corpus/knowledge` and `--selftest`;
  `python3 -B reports/round-28/readme/sweep.py` and `--selftest` and `--json`;
  `python3 -B tools/check-gate-battery.py --selftest`; `sha256sum` over the twelve
  §3.4 surfaces, `examples/**` and `corpus/lessons/**` aggregates, and
  `reports/round-34/handoff/declared-in-r7/*`; `git status --porcelain=v1 -uall --
  <protected prefixes>` and `git diff --stat ce103bf -- reports corpus/lessons
  tools/gates/frozen`; the in-process `sweep(...)` controls of §5.3 and the projected-tree
  acceptance of §5.1 (`.scratch/c05/`); `ls
  /home/vgpnk/Projects/shokunin/.ufo/reports/round-36` (absent); the fleet-root
  `MANIFEST.json` read (250 rounds, no round-36 row).
- §3.5 (live in-tree runner execution, observed 09:26-09:31Z): `ps -eo
  pid,lstart,args`; `readlink /proc/<pid>/cwd`; repeated `sha256sum` + `stat -c
  '%y'` + `git diff` over `reports/round-{34,35}/validation.json` at
  `09:26:40Z, 09:29:26Z, 09:29:57Z, 09:30:01Z, 09:30:22Z, 09:30:35Z, 09:30:47Z,
  09:31:07Z, 09:31:10-31Z`; `git show ce103bf:reports/round-<N>/validation.json |
  sha256sum` for the filed digest of each; the transient revision's
  `acceptance_checks_passed` read via `python3 -c json.load(...)`;
  `python3 -B tools/harness/receipt_guard.py
  reports/round-{34,35}/validation.json` (exit 3, `RECEIPT-GUARD-COMMITTED`)
  and `--selftest` (`selftest_passed: true`); `reports/round-35/run-validation.py:9,36,496-503`
  and `reports/round-34/run-validation.py:10,36` (the absolute `ROOT`,
  `os.chdir(ROOT)`, and the unconditional write path);
  `tools/harness/receipt_guard.py:16-17,150-167`.
- §7.1 peer reads at `09:32Z`:
  `reports/round-36/cov/C02-audit-delta.md:34-37,161-163,408-417,443,457,463-466,484,496-499`
  (its F1/F2/F3, the order/contiguity leg and its negative control, the pointer
  counts, the delta),
  `reports/round-36/cov/C03-verify.md` (§0 dependency status, its F1),
  `reports/round-36/scout/K02-timekeeping-scout.md:1-30,30-110` (K02-F1's
  re-measured sweep table and reproduction commands, K02-F2's `couples:` finding),
  `reports/round-36/cov/C01-audit.md:1-30` (its verdict table),
  `reports/round-36/cov/C04-receipt.md:1-30` (its measurement window and pins).
- `corpus/lessons/round-28.md:80` and `corpus/lessons/round-19.md:115` — the
  false-green-over-a-stale-claim class and the "re-measure, never
  arithmetic-adjust" rule, both cited by K02-F1 and cross-checked here by grep.
