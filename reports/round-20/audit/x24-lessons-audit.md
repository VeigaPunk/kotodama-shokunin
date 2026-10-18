# X24 — lessons-partition audit (round 20)

- round 20 (operator loop 2 of 3, build round 4 of 4; 64 workers on
  `opencode-go/deepseek-v4.1-flash` per `reports/round-20/claims.json`) · seat
  **X24** (SCRIBE X24 — fragment index + lessons audit) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X24: fragment index + lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` (round-19 admit),
  HEAD `122086bce0aa577bec221bb2d37eedf20f4f3ed2` ("round-20: declare claims
  D/O/C …").
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies
  no round, and blesses no lesson.
- writes: **this file**, its read-only tool `reports/round-20/audit/x24-lessons-audit.py`
  and receipt `reports/round-20/audit/x24-lessons-receipt.json`, plus the sibling
  `reports/round-20/fragment-index.md`. No `corpus/lessons/**` byte, no filed
  round 8–19 byte, and no tool or gate is edited by this seat. No commit, no
  push.
- measurement window: census 2026-10-18T12:56:37Z–12:56:53Z UTC; the round-20
  wave was live throughout (5 files under `reports/round-20/` at 12:57Z, from 2
  at the declaration).

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | lesson census: **20 lesson files** in `corpus/lessons/`, rounds 1–19 (round 5 twice; `supplement-opencode-1.md` non-round; round 13 operator-skipped, no lesson) | measured |
| 2 | `## Gate` section present in **15 of 20**; absent only in rounds 1–4 (pre-contract seed lessons) and **round 16** | measured |
| 3 | the filed **round-19 lesson is contract-complete** — `source:`, `verified-at:`, `recheck:`, `scope:` and a bounded `## Gate` with three opening readings; sha256 `0c975cf1…`, 64 818 B, 250 lines, byte-identical to the admit commit `caf1bea` | measured |
| 4 | the round-19 lesson-path collision (X28-1) **remains open**: the proposed `corpus/lessons/round-19-d4-craft.md` has not landed and R19-D08's entry is still unintegrated at `reports/round-19/integration/d4-lessons-entry.md` | **finding X24-L1** |
| 5 | stale repo-path references: **11 missing refs across 7 filed lessons**; one X28-era ref cleared (`reports/round-19/validation.json` now exists), the rest unchanged; all are historical/aspirational — filed bytes stay read-only | **finding X24-L2** (informational) |
| 6 | round 20 at the census: **no round-20 lesson on disk** and **0 round-20 mentions in `LOG.md`**; the round-19 collision is the carry-forward warning (name one owner per lesson path) | measured |

## 1. Method

Read-only tool `reports/round-20/audit/x24-lessons-audit.py` (stdlib only;
opens no file for writing — the receipt is produced by the caller's stdout
redirect). It checks, per lesson file: the contract lines (`source:`,
`verified-at:`, `recheck:`, `scope:`), a `## Gate` block bounded by the next
`## ` heading with candidates / admitted / rejected / spot-check markers and
opening-reading lines, every backticked repo path resolved against the live
tree, the round sequence vs the `Round N admitted` lines in `LOG.md`, a
round-20 lesson probe, and the `corpus/README.md` digest.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-20/audit/x24-lessons-audit.py --selftest   # 12/12, exit 0
python3 -B reports/round-20/audit/x24-lessons-audit.py             # census summary
python3 -B reports/round-20/audit/x24-lessons-audit.py --json > reports/round-20/audit/x24-lessons-receipt.json
```

Controls (all in-memory; no fixture file is written):

- `--selftest` → **12/12 checks green, exit 0** at 12:56:37Z. It includes the
  negative controls: the Gate block must not swallow the following section
  (`## Next` excluded), a missing path (`reports/round-20/__x24_nonexistent__.md`)
  must not resolve on disk, and the path regex must capture both an existing
  and a missing reference.
- receipt parse control: `python3 -c "import json; json.load(open(...))"` → ok;
  `lesson_files = 20`, `schema = kotodama-lessons-audit-v2`,
  `observed_at_utc = 2026-10-18T12:56:53.735871+00:00`.
- digest control: the sha256 printed below for `corpus/lessons/round-19.md`
  equals the receipt row's `sha256` for the same file (re-derived, not
  inherited).

## 2. Census (2026-10-18T12:56:53Z, `x24-lessons-receipt.json`)

- Lesson files: **20** (`corpus/lessons/*.md`).
- Rounds with a lesson: **1–12, 14–19** — round 5 has two files
  (`round-5-availability.md`, `round-5.md`), `supplement-opencode-1.md` is not
  round-numbered, round 13 (operator-skipped) has none.
- `## Gate` present: rounds **5 (both), 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18,
  19** and `supplement-opencode-1` = **15 of 20**. Absent only in rounds **1, 2,
  3, 4** (pre-contract seeds) and **16**.
- Contract lines: `source:` present in **16 of 20** (all but rounds 1–4);
  `recheck:` present in the same 15 files that carry a Gate; round 16 carries
  `source:` but neither Gate nor `recheck:`.
- `round_20_lessons: []`; `round_20_mentioned_in_log: false`
  (`grep -c "round-20\|Round 20\|round 20" LOG.md` → **0**, 12:57Z).
- `corpus/README.md` sha256 `456275882cac4373e1763fbf064f2b7203ea4b036b75ae3c9236af4027949e3d`
  — the revision 1.4 (round-19 reconciliation) bytes; recorded here only as the
  census digest, not as a coverage verdict (claim C is not this seat's).
- `rounds_logged_admitted` (from `LOG.md`, `Round (\d+) admitted`):
  **[8, 9, 10, 12, 15, 16, 18, 19]**.

## 3. Findings

### X24-L1 — the round-19 lesson-path collision is still open (finding)

Round 19's own lesson and the X28 audit both recorded the collision: the path
`corpus/lessons/round-19.md` was assigned to two seats, X21's gate-keeper
survey landed there, and R19-D08's paste-ready D4 lesson entry was left
unintegrated at `reports/round-19/integration/d4-lessons-entry.md`. X28's
finding X28-1 routed the disposition to the parent: append D08's text as a
distinct section, or land it at a new path such as
`corpus/lessons/round-19-d4-craft.md`.

Measured at the census (commands in §1):

- `ls corpus/lessons/round-19-d4-craft.md` → **does not exist**; the filed
  round-19 lesson still references that path, so the tool lists it among the
  missing refs (table below).
- `ls -la reports/round-19/integration/d4-lessons-entry.md` → present,
  **13 670 B**, mtime `2026-10-18 08:37 -03:00` (11:37Z) — unchanged since
  round 19; nothing in round 19 or 20 has integrated it.
- `ls reports/round-19/entries/R19-C1*.md` → the ten entries `R19-C11`…`R19-C20`
  exist (the lesson's `R19-C1x.md` reference is a **glob**, not a path; the tool
  reports it missing because it resolves literally — informational).

This is not a defect of the round-19 lesson: filed bytes are read-only by the
lane's rule, and the lesson itself records the collision. It is an open
integration debt the parent still owns. **A round-20 seat must not resolve it by
editing filed bytes; the two dispositions remain (append under recorded
authorship, or land at the new path).**

### X24-L2 — stale repo-path references, re-measured (informational)

Path-resolution sweep over all 20 lessons at 12:56Z — **11 missing refs in 7
files**. Delta against X28's round-19 table (attributed): round-19's
`reports/round-19/validation.json` ref **cleared** (the runner wrote the receipt
at 12:33:38Z; the lesson's own close section records it); the other rows are
unchanged, and the round-19 glob/proposal pair is the only live one.

| lesson | missing reference | note |
|---|---|---|
| `round-9.md` | `reports/round-9/rerun.json` | never written under that name |
| `round-11.md` | `examples/culture-d2/typed-gate.expected.json`, `tools/typed-gate-flow.py` | superseded / never landed |
| `round-14.md` | `reports/round-12/adjacency/entries.md` | round-12 layout differs |
| `round-15.md` | `reports/round-15/handoff/packet-v2.yml`, `tools/build-handoff-v2.py` | live file is `packet-v2-05.yml` |
| `round-17.md` | `reports/round-17/civ-map.json` | round-17 civ output is under `reports/round-17/civ/` |
| `round-18.md` | `reports/round-18/repin/MANIFEST.tsv`, `tools/gates/frozen/round-18-repin/MANIFEST.tsv` | repin manifest path differs |
| `round-19.md` | `reports/round-19/entries/R19-C1x.md` (glob), `corpus/lessons/round-19-d4-craft.md` (proposed path — see X24-L1) | round-19 is a filed artifact; both refs are pattern/proposal |

Control for this table: the tool resolves each backticked path against the live
tree and its `--selftest` includes the negative case (a nonexistent path must
be flagged); the 11 rows are re-derivable with the §1 commands.

### X24-L3 — the round-19 lesson landed and is contract-complete (measured)

The path X28 audited mid-wave was a moving byte; the filed revision is now
stable and committed. Measured 12:56Z:

| reading | value |
|---|---|
| sha256 | `0c975cf19913ebfd37f218313dd82af8601deeb384c16cdfbe9ae4040d7cdad4` |
| size / lines | 64 818 B / 250 lines |
| mtime | `2026-10-18 09:37:08 -03:00` (12:37:08Z) |
| committed | `git log -1 -- corpus/lessons/round-19.md` → `caf1bea` (round-19 admit, 09:52:31 -03:00) |
| byte-identity control | `git diff --stat caf1bea -- corpus/lessons/round-19.md` → empty (exit 0) |

Contract surface: `source:`, `verified-at:`, `recheck:`, `scope:` lines; a
`## Gate` section bounded before `## Gate-keeper closeout rule` with the three
axis subsections (D/C/O), each naming its declared threshold location
(`reports/round-19/claims.json`) and a counting command, plus opening readings
and the closeout rule. The file's own appended close section carries the
runner's receipt readings and two self-digest checkpoints (236 lines /
`facb5f3d…` at 12:36Z; 249 lines / `62fcf50b…` at 12:37Z) — consistent with the
census revision (250 lines / `0c975cf1…`), i.e. the lesson grew by its final
recorded paragraph only. **X28's §2 digest (`cd3b8c13…`, 205 lines, 11:41Z) is
superseded for this path; this census binds to the digest above.**

### X24-L4 — contract gaps unchanged: rounds 1–4 and round 16 (measured)

Rounds 1–4 are pre-contract seed lessons (no Gate, no `source:`); round 16 is
the **only post-contract lesson without a `## Gate`** (it carries `source:` but
no `recheck:`). Re-measured, not inherited: the same five files. This is a
historical shape, not a defect to repair in filed bytes — a future round that
wants a round-16 gate reading would land it as a new dated file, never as an
edit.

### X24-L5 — round-20 lesson state at the census (measured, live wave)

No round-20 lesson exists at 12:56Z and `LOG.md` has no round-20 mention; the
round is mid-wave. The round-19 precedent (two seats on one path) is the
carry-forward warning: **if a round-20 lesson lands, its path needs one named
owner**, or the parent must integrate two fragments rather than have one
silently overwrite the other.

## 4. Cross-check: lessons vs LOG records

- Rounds with a lesson: 1–12, 14–19 (round 5 twice). Rounds whose `LOG.md`
  record is an admission: 8, 9, 10, 12, 15, 16, 18, 19 — **every one has a
  lesson** (round 11 rejected and round 14 the loop-1 integration checkpoint
  also have lessons; the lesson file tracks the round, not the verdict).
- Round 13 (operator-skipped) is the only round 1–19 without a lesson.
- No admitted round is missing its lesson at this census.

## 5. Limits

- This is a structural and path-resolution audit. It does not re-execute any
  lesson's census commands, does not re-verify a lesson's domain claims, and
  does not adjudicate whether a lesson's prose is correct.
- Digest and Gate readings bind to the 12:56Z stamps; `corpus/lessons/round-19.md`
  is a filed artifact and a later edit would be a new measurement, not an
  inherited value.
- The round-20 lesson probe is a live-wave reading: a lesson arriving after
  this census needs a dated refresh, not an inference from this file.

## 6. Dated observation — the round-20 lesson landed (2026-10-18T13:26:39Z)

This observation supersedes §0 item 6 and §3 X24-L5 for the round-20 probe.

`corpus/lessons/round-20.md` (seat X17) appeared at mtime 13:17:16Z. The
tool was re-run at **13:26:39Z** (receipt `x24-lessons-receipt-r2.json`; the
first receipt stays as filed, per the lane's new-file rule):

- **21 lesson files** now (`lesson_files: 21`); `round_20_lessons:
  ["round-20.md"]`; `rounds_with_lessons` adds 20.
- The round-20 row is **contract-complete**: `source:`, `verified-at:`,
  `recheck:`, `scope:` and a `## Gate`; sha256
  `d54eb3f77d7d5b013fcb1044e1dada28e7f247abe2cb2458bcc8580a9ea7d4c1`,
  43 056 B, 182 lines, **57 path refs, 0 missing**.
- Its `scope:` line names **one owner** for the path ("the round-20 claims
  and targets name no other seat's lesson deliverable, so no second writer
  may land on this path") and cites the round-19 collision (X28-1 / X24-L1)
  as the carry-forward warning — the X24-L5 warning was heard, and the
  round-19 collision itself remains open per X24-L1.
- `LOG.md` still carries **no round-20 admission line** at this stamp
  (`rounds_logged_admitted` unchanged: [8, 9, 10, 12, 15, 16, 18, 19]),
  which is correct mid-wave; the round-20 lesson's own gate closeout is not
  an admission.
- The missing-ref table in §3 is unchanged at 13:26:39Z (11 refs across 7
  filed lessons); the round-20 lesson adds none.
