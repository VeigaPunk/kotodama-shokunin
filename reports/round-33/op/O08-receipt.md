- Seat: O08 | executor | claim O | date 2026-10-19 | baseline 139e3b6

# O08 — operability receipt draft (claim O)

Mission: the claim-O before→after narrative with the declaration-time audit
output, the reconciled-state expected output, and the falsifier disposition
summary, command-carried. Every number below is a command output taken in this
seat between 2026-10-19T03:49Z and 04:00Z; nothing is inherited from a
fragment that had not landed at this seat's read. Fragments that landed while
this seat worked (K01, K02, O01, O03, O04, O07) are cited as landed and
cross-checked where they overlap my measurements; the remaining dependencies
are named under `## Owed`.

**Scope:** a receipt, not the reconciliation. The live `corpus/lessons/
README.md` still carries 26 rows at this stamp and the live audit still exits
1. The "after" receipt in §2 is a **simulation** over scratch bytes
(`.scratch/o08-sim-reconciled.md`), labelled as such wherever it appears. No
filed byte was written by this seat; the only files this seat created are
`reports/round-33/op/O08-receipt.md` and scratch working files.

## 1. Declaration-time receipt (before)

Command and verbatim output (2026-10-19T03:50Z, exit 1):

```
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py
index present: True
lesson files:  33
index rows:    26
queue rows:    49
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  FAIL C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  FAIL C34b_prose_arithmetic
findings:      2
  C31-1 unindexed-file: ['round-26.md', 'round-27.md', 'round-28.md', 'round-29.md', 'round-30.md', 'round-31.md', 'round-32.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26], 'measured': [26, 33]}}
$ echo $?
1
```

- Selftest at the same stamp: `python3 -B reports/round-25/audit/
  c31-lessons-index-audit.py --selftest` → `SELFTEST OK: 28/28 checks passed`,
  exit 0.
- `--json` receipt filed at `.scratch/o08-audit-before.json`, sha256
  `523fd43bfa4ddd1f6f861807c2648b15abff2bcc6a6ebd5d4a40759a59970d07`;
  `index_sha256` in it = `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`
  = `sha256sum corpus/lessons/README.md` at the stamp.
- Two independent reads agree: `ls corpus/lessons/*.md | wc -l` → 33 and the
  tool's census → `lesson files: 33`.
- **The reconciliation is additive.** `C34_pins_rederived` and
  `C34c_shape_cells_rederived` PASS at declaration: all 26 existing rows'
  `bytes`/`lines`/`sha8`/`format`/`contract` cells still equal the live bytes.
  No existing row needs a pin correction — only the seven new rows and the
  prose arithmetic are in scope.
- Independent agreement with the landed dependency receipts: K02 re-ran the
  same tool and reproduced the same before-state
  (`reports/round-33/op/K02-lessons-census.md` §1); O07 pinned the regression
  baseline in the window 03:52:07–03:52:30Z
  (`reports/round-33/op/O07-baseline-receipt.md` §Binding facts: HEAD
  `139e3b66…`, `git ls-files | wc -l` = 2655, `git status --porcelain` =
  ` M LOG.md` + `?? REGIMEN.md` + `?? reports/round-33/`).
- Tree-state observation for the scope watch (A03's territory, not a claim of
  this seat): at 03:52Z `git status --porcelain` also listed
  ` M reports/round-5/validation.json` and ` M reports/round-7/validation.json`;
  by 03:57Z both had disappeared from the status and `git diff --stat` over
  them is empty — a transient working-tree modification of two filed-round
  files by some concurrent process, now reverted. Recorded because a filed
  round's bytes were briefly dirty; no byte of them is attributable to this
  seat (this seat wrote only its own `out` path and `.scratch`).

## 2. Reconciled-state receipt (after) — simulated, not delivered

Method: `.scratch/o08-recon-sim.py` (sha256
`c9a9dfc8fd2e744cced56f485d5dab19f30da2d4435446bff382cf7037fa797a`) builds
the README the integrator's O/C drafts would produce — the seven rows from the
live census inserted after the round-25 row, and `**Rows: 26. Files: 26.**` →
`**Rows: 33. Files: 33.**` — writes it to
`.scratch/o08-sim-reconciled.md` (sha256
`34a7f1ee70d41d1328c28b5ad209a46d1cf430475747d5ee22b741d5b5dab147`), patches
the tool's `INDEX` constant to those bytes, and re-runs `run_checks()`
unchanged. The tool's own logic and every filed byte are untouched.

Expected reconciled-state output (verbatim from the run, 2026-10-19T03:54Z):

```
index present: True
lesson files:  33
index rows:    33
queue rows:    49
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0
```

That is the claim-O `after_required` leg-(a) shape: **33 rows == 33 files,
findings 0, exit 0** (`main()` returns `0 if not res["findings"]` —
`reports/round-25/audit/c31-lessons-index-audit.py:460`).

### 2.1 Row cells the seven new rows must carry

Re-measured from live bytes at 2026-10-19T03:52Z (`census()` over
`corpus/lessons/*.md`). O01's landed drafts carry **byte-identical cells** —
independent agreement, same measurement, different seats:

| file | format | contract | bytes | lines | sha8 |
|---|---|---|---|---|---|
| `round-26.md` | gate-keeper | 4/4 | 60054 | 222 | `cae06660` |
| `round-27.md` | gate-keeper | 4/4 | 54972 | 203 | `f15e285b` |
| `round-28.md` | gate-keeper | 4/4 | 50419 | 145 | `dd832ff7` |
| `round-29.md` | gate-keeper | 3/4 | 17847 | 118 | `b6765d33` |
| `round-30.md` | gate-keeper | 3/4 | 30665 | 181 | `56e77835` |
| `round-31.md` | gate-keeper | 4/4 | 16637 | 73 | `8870bbdd` |
| `round-32.md` | gate-keeper | 4/4 | 12879 | 66 | `8aacfc2b` |

Cross-check: `reports/round-33/op/O01-row-drafts.md:55-61` carries exactly
these values, with a richer disposition-pointer column
(`reports/round-N/validation.json`, e.g. `:55`). Row shape used in the
simulation, matching the existing rows' six columns
(`corpus/lessons/README.md:69-95`):

```
| `corpus/lessons/round-26.md` | gate-keeper | 4/4 | — | `reports/round-26` | bytes=60054 lines=222 sha8=cae06660 |
```

The simulation's columns 4/5 are placeholders (`—` and `reports/round-N`);
O01 supplies the real cells. All seven `reports/round-N` directories and
their `validation.json` exist (`test -d` / `test -s` per round 26–32 →
yes/yes), so those pointers resolve as paths.

### 2.2 Prose arithmetic: the sites the tool checks, and the queue-growth risk

The tool checks exactly two sites
(`reports/round-25/audit/c31-lessons-index-audit.py:296-314`):
`Rows: **N**` (queue arithmetic) and `**Rows: N. Files: N.**` (table
arithmetic).

- **Table site, must change** — `corpus/lessons/README.md:97`:
  `**Rows: 26. Files: 26.**` → `**Rows: 33. Files: 33.**`
- **Queue site, must be re-derived if O02 mints the new rows** —
  `corpus/lessons/README.md:207` reads `- Rows: **49**. Of the 26 index rows,
  **23 carry at least one question**;` and the live queue table has 49 rows.
  O03's owner leg records **15 dangling queue ids that must be minted by O02**
  (`reports/round-33/op/O03-owner-checks.md:88-92`: `round-30.md` → Q-30-1..5,
  `round-31.md` → Q-31-1..4, `round-32.md` → Q-32-1..6; "0/5", "0/5", "0/11"
  dangling today) and §5 of the same fragment names further rounds 26–29 items
  that would need owners if rows are minted. **Consequence for the integrator:
  if §4 grows by those 15 rows, the queue becomes 64 and the `Rows: **49**`
  cell must be re-measured to 64 — leaving it stale fails `C34b_prose_arithmetic`
  on the delivered tree even though the table leg is green.** The simulation
  above models the minimal reconciliation (no new queue rows), which is why it
  reports `queue rows: 49` and stays green; the delivered shape must re-run the
  tool and read the queue count from it rather than trusting either number.
- The `Of the 26 index rows, **23 carry at least one question**` prose at
  `:207` and the "three that carry none" list at `:208-210` are **not**
  machine-checked but are stale: with 33 rows (and more rows carrying
  questions) that sentence and list need re-derivation.
- **Ten further stale-26 sites the tool does not check** (O02 scope; C34b
  reaches only the two regex sites above): `:5` ("**24 filed lessons**"),
  `:6-8` ("26 at the final stamp"), `:35` (`# 26/26, exit 0` — the selftest is
  28/28, see `:55` and `:338`), `:39-40` (`# 26 (2026-10-18)` ×2), `:118`
  ("**14 files.**"), `:124-125` ("**5 files**"), `:127-128` ("**7 files.**"),
  `:138-141` (histogram arithmetic ending "Total 26"), `:257` ("beside the 26
  `*.md` lesson files"), `:285` ("`--selftest` is 26/26 in-memory checks"),
  `:294` ("the 24 filed lessons"). Live histogram to write instead:
  gate-keeper **21**, fragment-index **5**, plain **7**, total **33**.
- §5's "nine evidence subdirectories" table (`:255-277`) counts 146 files
  under nine directories beside "the 26 `*.md` lesson files" — the 146 is a
  separate measurement this seat did not re-run; `to-verify` for O02.

### 2.3 Negative controls — the expected green is not vacuous

Four variants built from the same reconciled bytes, each re-run through the
unchanged tool (all four detected; the script's asserts passed, exit 0):

| variant | mutation | expected | observed |
|---|---|---|---|
| stale pin | `round-32.md` row `bytes=0` | C34 red | `FAIL C34_pins_rederived`, `C34-1 pin-drift: [('round-32.md', 'bytes', '0', 12879)]` |
| stale arithmetic | prose left at `26/26` | C34b red | `FAIL C34b_prose_arithmetic`, `C34-2 … {'stated': [26, 26], 'measured': [33, 33]}` |
| wrong shape cell | `round-26.md` labelled `plain` | C34c red | `FAIL C34c_shape_cells_rederived`, `C34-3 shape-cell-drift: [('round-26.md', 'format', 'plain', 'gate-keeper')]` |
| one row omitted | `round-30.md` row removed | C31 + C34b red | `C31-1 unindexed-file: ['round-30.md']` + `C34-2 … {'stated': [33, 33], 'measured': [32, 33]}` |

Variant digests: `ccf28337ce0969b299bdffde6da953ef1aa53eccd3caec4f43e220cf4dc10630`,
`8430f21d0edfa3bb64a8ed2e1d24a75d5441fd17ab014e9cfbc500281b30438a`,
`bde9ebfc4df1ad1239a5ceabd68864c72e6e2e2bd99d1031c97d1dc0019a8fc3`,
`402fb783b16e3fcd75d6bee55b01448dfd8ac24ad3b2dd962c81dc77a3315f48`
(all under `.scratch/`). Preview only: O06 owns the full control spec.

## 3. Falsifier disposition summary (leg b)

**Located.** The round-32 routed debt "the falsifier audit's filename mismatch
(substance 5/5)" is finding **F-X16-3** in the lessons partition, not in
`reports/round-32/` — `corpus/lessons/round-32.md:36` (the section heading
"## The falsifier legs — substance 5/5, instrument false-fires on day one"),
`:41` (the finding) and `:55` (its open route **Q-32-1**). Located by K01
(`reports/round-33/op/K01-falsifier-scout.md` §1) and **independently
reproduced by this seat** at HEAD `139e3b6` (2026-10-19T03:58Z), both legs:

- **Instrument leg — false-fires.** The `SKILL.md:715` one-liner (418 chars,
  `SKILL.md` sha256 `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`,
  `wc -l` = 715) re-executed verbatim prints **5 rows** — `reports/round-{19,25,26,27,28}/availability.json`
  — exit 0. It tests `not os.path.exists(.../telemetry/'closing-snapshot.json')`,
  a filename that exists nowhere: `find reports corpus tools -name
  'closing-snapshot.json'` → no matches (exit 0, empty).
- **Substance leg — passes 5/5.** For each of the five records, the landed
  snapshot `reports/round-N/telemetry/availability-close-N.json` carries
  `"schema": "kotodama-availability-closing-snapshot-v1"`, `closes` = the
  record path, and `closes_sha256` = the record's live sha256. Re-derived here
  for all five: `round-19` `fa9588db…`, `round-25` `51d62532…`, `round-26`
  `7e23f33d…`, `round-27` `987b04e1…`, `round-28` `aceb019c…` — 5/5 match.
  (Note for any fix: the live schema key is `closes`, **not** `closes_record`
  as the lesson's paraphrase has it; the r31 validator reads
  `document.get("closes")` at `reports/round-31/run-validation.py:799`.)
- **Consequence on record:** `LOG.md`'s recorded falsification clause (i)
  (`LOG.md:3460-3463`) has fired on day one for an **instrumental** reason
  (wrong filename), not a substantive one.

**Disposition summary.** Class: **fixable, bounded** — the mismatch is one
filename literal in one checklist line, and the substance it guards is
already green. The fix is a **shared-file change** (`SKILL.md`), so per the
round's rules it is drafted here as before/after text and applied by the
integrator; **O05 owns the disposition record**
(`reports/round-33/op/O05-falsifier-disposition.md`, which the claim requires
to exist) and this section is its input summary, not a substitute.

Draft — `SKILL.md:715`, before (verbatim, 418 chars):

```
      (audit: `python3 -c "import json,glob,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not os.path.exists(os.path.join('reports',f.split('/')[1],'telemetry','closing-snapshot.json'))]"` — must print nothing once the round's records are closed)
```

Draft — `SKILL.md:715`, after (one line, same shape, re-keyed to the landed
convention):

```
      (audit: `python3 -c "import json,glob,hashlib,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not any(json.load(open(s)).get('closes')==f and json.load(open(s)).get('closes_sha256')==hashlib.sha256(open(f,'rb').read()).hexdigest() for s in glob.glob(os.path.join('reports',f.split('/')[1],'telemetry','availability-close*.json')))]"` — must print nothing once the round's records are closed)
```

Control for that draft, run by this seat (2026-10-19T03:59Z):

| leg | tree | expected | observed |
|---|---|---|---|
| A | live repo root | no output, exit 0 | no output, exit 0 |
| B | scratch mirror `.scratch/o08-skill715-control/` with `round-19`'s snapshot `closes_sha256` set to `0…0` | exactly one row | `reports/round-19/availability.json`, exit 0 |
| C | same mirror, snapshot restored to the live digest | no output | no output, exit 0 |

The replacement is line-for-line, so `SKILL.md` stays at 715 lines and no
line-number cascade reaches the rest of the file (relevant to A09's
pin-cascade analysis). Alternative disposition (also append-only, also
parent-owned): reword `LOG.md` clause (i) to name the landed convention via a
new dated LOG entry. What this seat does **not** do: apply the edit, claim the
fix landed, or claim the clause's disposition — those are the integrator's and
the operator's.

**Supersession by O05 (landed at 01:00Z, after this seat's draft).**
`reports/round-33/op/O05-falsifier-disposition.md` is the disposition record
the claim requires, and its §3b after-bytes are the draft the integrator
should apply — same convention as my draft above, hardened in two ways: it
globs `telemetry/availability-close-*.json` (so a correction snapshot can
still close a record) and guards the snapshot read with `isinstance(d, dict)`
before `.get`. O05's §4 carries a seven-scenario control set against the old
instrument as well as the new one; my §2.3/§3 controls are an independent
second construction and agree on every check. O05's ledger also dispositions
the lesson-side key-name error (`closes_record` vs the live `closes`) as
`carried-with-owner` (its row D-3) — that part is **not** fixable by editing,
since `corpus/lessons/round-32.md` is a filed lesson.

**Probe honesty (why my own earlier scan came back empty).** This seat's first
probe (03:51–03:56Z) searched `reports/round-31/**`, `reports/round-32/**`,
the fleet `.ufo/reports/round-3{0,1,2}` reports, fleet `MANIFEST.json` and a
whole-repo `filename mismatch|misnamed` grep — and found nothing, because the
referent is in `corpus/lessons/round-32.md`, a **filed lesson**, and my
`falsifier` grep was scoped to `reports/` rather than the lessons partition.
The negative result was true of the searched space only; K01's wider scan
found it. Recorded so the next receipt does not repeat the scoping error: for
routed-debt sentences, grep `corpus/lessons/**` too.

## 4. Command inventory (all this seat's runs, 2026-10-19)

| command | exit | stamp |
|---|---|---|
| `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | 1 | 03:50Z |
| `… --selftest` | 0 (28/28) | 03:50Z |
| `… --json` | 0 | 03:50Z |
| `python3 -B .scratch/o08-recon-sim.py` | 0 (5 receipts + 4 asserts) | 03:54Z |
| `git rev-parse HEAD`; `git ls-files \| wc -l`; `git status --porcelain` | 0 | 03:52Z / 03:57Z |
| `SKILL.md:715` one-liner, verbatim (phantom name) | 0, 5 rows | 03:58Z |
| re-keyed one-liner (draft after) at repo root | 0, no output | 03:59Z |
| control legs A/B/C in `.scratch/o08-skill715-control/` | 0 / 0 / 0 | 03:59Z |
| 5-record snapshot substance probe (`closes` + `closes_sha256`) | 0, 5/5 PASS | 03:58Z |
| `find reports corpus tools -name 'closing-snapshot.json'` | 0, empty | 03:58Z |
| falsifier probe set (§3, first pass) | 0 / 0 hits | 03:51–03:56Z |

## 5. Honest limits

- The after-state is a **simulation**, not a delivered reconciliation: the
  live README is still 26 rows and the live audit still exits 1 at this stamp.
  Nothing here moves claim O to verified.
- The simulation patched the tool's `INDEX` constant only; the tool's logic
  and every filed byte are unmodified.
- This is not an admission, verdict, or closure record.
- The regression baseline named in the claim's thresholds (gate battery 10/10,
  craft selftests, gate selftests) is **O07's** receipt, landed and cited
  above; this seat ran only the c31 selftest (28/28) plus the §3 falsifier
  legs.
- §2.2's 146-file / nine-subdirectory count was not re-measured (`to-verify`).
- The `SKILL.md:715` before/after draft is a proposal with its control; it is
  not applied, and O05/O06 own the disposition record and the full control set.

## Owed

- `reports/round-33/op/O02-readme-delta.md` — the README prose delta. §2.2 is
  its acceptance checklist, including the queue-count re-derivation (49 → 64
  if the 15 ids are minted) and the ten unchecked stale-26 sites.
- Integrator application: the `corpus/lessons/README.md` row+prose edits and
  O05's `SKILL.md:715` re-key (§3b there; my §3 draft is an equivalent second
  construction) — all drafted, none applied by seats.
- Not owed but landed after this seat's read, for the integrator's cross-read:
  `op/O05-falsifier-disposition.md` (disposition record + 7-scenario controls,
  §3 above), `op/O06-controls.md` (full control spec; §2.3 here is a
  four-control preview), `op/P01-plan.md` (execution plan).

## Citations

- `corpus/lessons/README.md:69-95` (existing row shape), `:97` (table
  arithmetic site), `:118,124-125,127-128,138-141` (§3 counts), `:150-200`
  (queue table), `:207-210` (queue arithmetic), `:255-277` (§5 evidence
  subdirectories), `:285,294,303-346` (revision blocks).
- `reports/round-25/audit/c31-lessons-index-audit.py:34-36,42-45,92-116,119-135,197-211,245-291,296-317,337-432,444-460`.
- Falsifier artifact: `corpus/lessons/round-32.md:36,41,55` (sha256
  `8aacfc2bd9f55ec9dae3a721dc793a83bf071e90b98955ffa2cb45a33437ab64`);
  `SKILL.md:713-715` (sha256 `79fe91d3…`, 715 lines); `LOG.md:3460-3468`
  (clause i), `:3512-3514`; `SCORECARD.md:443-445`;
  `reports/round-19/telemetry/availability-close-19.json:2-5` and the same
  shape in rounds 25–28; `reports/round-31/run-validation.py:780,792-812,799`.
- Landed dependency fragments: `reports/round-33/op/K01-falsifier-scout.md`
  §1-§5; `op/K02-lessons-census.md` §1; `op/O01-row-drafts.md:55-61`;
  `op/O03-owner-checks.md:84-92,104,107-126`; `op/O07-baseline-receipt.md`
  §Binding facts.
- Commands: `python3 -B reports/round-25/audit/c31-lessons-index-audit.py
  [--selftest|--json]`; `python3 -B .scratch/o08-recon-sim.py`;
  `ls corpus/lessons/*.md | wc -l`; `sha256sum …`; `git rev-parse HEAD`;
  `git ls-files | wc -l`; `git status --porcelain`; `git diff --stat` over the
  two round-5/7 receipts; the `SKILL.md:715` one-liner and its re-keyed draft
  (§3, §4); the five-record snapshot substance probe; `find reports corpus
  tools -name 'closing-snapshot.json'`; `grep -rn -i "falsif|filename"
  reports/round-3{1,2}/`; `grep -rn -i "filename mismatch|name-mismatch|
  misnamed|wrong filename" .`; `grep -n -i falsif corpus/lessons/round-32.md`;
  the cited-path existence scan (python3 heredoc, first-pass probe).
- Scratch evidence: `.scratch/o08-audit-before.json`,
  `.scratch/o08-recon-sim.py`, `.scratch/o08-sim-reconciled.md`,
  `.scratch/o08-sim-neg-{stale-pin,stale-arithmetic,shape-cell,unindexed}.md`,
  `.scratch/o08-skill715-control/` (digests in §1/§2.3).
- `reports/round-33/claims.json:19-37`; `reports/round-33/targets.json:13`.
