- Seat: K04 | scout | C | date 2026-10-19 | baseline da68a6d

# K04 — box-1 / anchor census (claim C pre-build measurements)

**Assignment** (`reports/round-34/targets.json` K04 row): "Box-1/anchor scout: the
A09-pins.md R1-R8 rows (read the fragment), the current SKILL.md line anchors for each
named executable row, and the round-30 box1-survey.py output format (what a durable
receipt needs)."

**Method / window.** 2026-10-19T06:4xZ–07:06Z, repo root, lane HEAD `da68a6d`
(`git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`), env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. `git status --porcelain` →
only `?? reports/round-34/`, i.e. every measurement below is at HEAD bytes. All commands
read-only except scratch output under `.scratch/`; no filed byte was written.

## 1. The pin target: `SKILL.md` at HEAD

| fact | measured value | command |
|---|---|---|
| sha256 | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | `sha256sum SKILL.md` |
| lines | 732 | `wc -l SKILL.md` |
| numstat 139e3b6→HEAD | 35 added / 18 removed (net **+17**) | `git diff 139e3b6..HEAD --numstat -- SKILL.md` |
| worktree vs HEAD | identical (empty) | `git diff --numstat -- SKILL.md` |

- The measured digest **is** the digest claim C names in its before-state
  (`reports/round-34/claims.json`, claim C: "SKILL.md digest moved 79fe91d3… → f9bd07c2…
  (O05 re-key + C14 Fixes 1-4 + FD-N4/N5; 715 → 732 lines)"). Confirmed: 715 lines /
  `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d` at `139e3b6`
  (`git show 139e3b6:SKILL.md | wc -l`, `| sha256sum`; the old digest is also quoted at
  `reports/round-33/adj/A13-verify-a07-a09.md:105` and `A16-shonen-material.md:21`).
- Digest era chain for box-1 evidence: `83b0a78a…` (r30 landed; `reports/round-30/craft/
  box1-landed-survey.json:4`) → `79fe91d3…` (r32 dossier closure; `reports/round-32/
  final-dossier.md:46,133`) → `f9bd07c2…` (HEAD, unrecorded in any receipt).
- **The round-33 receipt does not pin it.** `reports/round-33/validation.json` mentions
  SKILL.md exactly twice, as a porcelain line: `:81-82` → `"path": "SKILL.md"`,
  `"raw": " M SKILL.md"`; the strings `f9bd07c2`, `79fe91d3` and `"732"` each occur
  **0** times in that file (python `json.dumps` scan). So the round-34 durable receipt is
  the first artifact that pins the post-r33 digest — claim C's calibration claim is
  measured against a genuinely unpinned surface, not a duplicate of an existing record.

## 2. box-1 survey today (claim C's first counting command)

`python3 -B reports/round-30/craft/box1-survey.py` → **exit 0**, verbatim stdout:

```json
{
 "date": "2026-10-18",
 "named": 28,
 "resolvable": 28,
 "unnamed_in_skill": [],
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"
}
```

- **Script provenance.** `git log --oneline -- reports/round-30/craft/box1-survey.py` →
  single commit `71cd9d3` (`12 0` insertions); `git show 71cd9d3:… | diff - <HEAD copy>`
  → no output (byte-identical at HEAD); sha256
  `d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89`. The script is
  filed (round-30) — it must not be edited; a new receipt is a new file.
- **Date hazard.** `:8` hardcodes the literal `"date": "2026-10-18"` in the emitted JSON.
  A receipt dated 2026-10-19 therefore **cannot** be `python3 … > out.json` verbatim; the
  receipt owner must set its own `date` field (or the receipt would carry a false date,
  which is exactly the "dated receipt" property claim C's after-state requires).
- **Key-shape hazard.** The script emits `named` / `resolvable` / `unnamed_in_skill` /
  `skill_sha256`; the filed receipt `reports/round-30/craft/box1-landed-survey.json`
  (`:2-8`) uses `mode` / `named_in_skill` / `resolvable` / `unresolvable` / `box1_note`.
  The two shapes are **not** the same object — the filed JSON was not a verbatim dump of
  the current script. A new receipt should state which shape it follows and carry both
  count names where the dossier prose quotes `named_in_skill` (`reports/round-32/
  final-dossier.md:46` quotes "28/28 named executables".
- **Stronger than the count: set equality.** The named set and the live scoped
  executable set are equal in both directions — `named 28`, `live 28`,
  `named-not-live []`, `live-not-named []`, where live = `tools/*.py` +
  `tools/gates/*.py` + `tools/harness/*.py` (same scope as
  `reports/round-30/run-validation.py:645-652`). Unnamed executables today: **0**.
  This is the statement that closes the round-24 box-1 inventory condition
  (`reports/round-30/craft/review-D29-box1.md:163-167`); a durable receipt should record
  the 28-path set, not only the count, so a future added tool is detectable as a diff.

## 3. What a durable receipt needs — the filed consumer's contract

The only filed consumer of a box-1 receipt is the round-30 depth leg
(`reports/round-30/run-validation.py:674-684`), which classifies a document as a
box-1 re-survey iff:

| requirement | implementation | evidence |
|---|---|---|
| filename matches `box[-_ ]?1` (case-insensitive) | `re.search(r"(?i)box[-_ ]?1", relative)` | `:675-677` |
| a **dated command**: date `\b20\d{2}-\d{2}-\d{2}\b` **and** a command token (`python3?`, `sha256sum`, `git show|diff|grep|ls-tree`, `grep `, …) | `dated_command()` `:328-329`; `DATE_RE` `:44`; `CMD_RE` `:45` | `:680` |
| the words `unnamed` / `executable(s)` / `inventory` | `re.search(r"(?i)unnamed|executables?|inventory", text)` | `:681` |
| the **full 64-hex** live SKILL digest present as literal text | `post_landing_digest: bound = bool(section) and digest in text`, `digest = sha(skill.encode())` | `:673,679,682` |

and the claim requires at least one passing row:
`reports/round-30/run-validation.py:697-698` — "box-1 executable re-survey has no dated
receipt pinned to the post-landing SKILL.md bytes"; the measurement carries
`skill_sha256`, `box1_resurveys`, `executable_inventory` (`:699-703`).

**The carrier must be Markdown.** `documents()` (`:290-303`) builds its document set from
`reports/round-30/**.md` only (`sorted(safe_path(ROUND).rglob("*.md"))`). In round 30 the
gate-satisfying artifact was therefore the **markdown** `reports/round-30/craft/
review-D29-box1.md` (its `:162` carries the full `83b0a78a…` digest, `:163-165` the
"28/28 … zero unnamed executables" language) — *not* the `.json` receipt, which the leg
never reads. The filed JSON is the human/durable twin, not the gate input.

**Draft shape for claim C's pair** (for the receipt owner / P02 plan; both files land
under `reports/round-34/craft/`):

- `box1-resurvey-durable.json` — machine twin: `date: "2026-10-19"`,
  `command: "python3 -B reports/round-30/craft/box1-survey.py"`, `exit_code: 0`,
  `skill_sha256` (full), `skill_lines: 732`, `named: 28`, `resolvable: 28`,
  `named_in_skill: 28`, `unnamed: 0`, `named_set: [ …28 paths… ]`,
  `script_sha256: d923ae0f…`, `baseline_commit: da68a6d`.
- `<name matching box[-_ ]?1>.md` receipt — same numbers in prose + a dated command line
  (e.g. `2026-10-19T07:0xZ python3 -B reports/round-30/craft/box1-survey.py`), the words
  `executables` / `unnamed` / `inventory`, and the full digest as literal text
  (mirroring `reports/round-30/craft/review-D29-box1.md:162`). Without the `.md` twin the
  artifact satisfies claim C's prose but not the filed leg's *shape* precedent.
- Scope note: the round-30 leg rglobs its own round's `.md` files, so this receipt is a
  claim-C / promotion-dossier artifact; it does **not** make the filed round-30 runner
  green and that runner is not to be re-run in-tree (shared rules; F-C13-1).

## 4. The 28 named executables — current `SKILL.md` anchors

Census = `python3` regex `tools/[\w./-]+\.py` over `SKILL.md` → 78 occurrence lines, 28
distinct paths; each path resolves (`box1-survey` `resolvable=28`).

| executable | `SKILL.md` line(s) at HEAD | containing section (heading line) |
|---|---|---|
| `tools/assemble-culture-d3.py` | :673 | Source-bounded culture drill — D3 (round 7) :662 |
| `tools/assemble-culture-d4.py` | :207 | Derivation replay :189 |
| `tools/assemble-d2-typed.py` | :449 | Register craft :354 |
| `tools/assemble-d2.py` | :615 | Gates and probes :575 |
| `tools/assemble-d4-typed.py` | :139,:158,:163,:195,:207,:210,:211,:213,:294 | Slot-label routing :130 |
| `tools/check-craft-exercise.py` | :616 | Gates and probes :575 |
| `tools/check-evidence-coupling.py` | :674 | Source-bounded culture drill — D3 :662 |
| `tools/check-gate-battery.py` | :617 (×3) | Gates and probes :575 |
| `tools/d2-typed-labels.py` | :35,:169,:208,:258,:272,:281,:288-:293,:304,:308,:329,:479,:481,:483,:491 | Label typing :31 |
| `tools/exercise-handoff-e2e.py` | :448 | Register craft :354 |
| `tools/gates/argot-derivation-gate.py` | :375,:376,:377,:429,:438 | Register craft :354 |
| `tools/gates/costume-era-consistency-gate.py` | :609 | Gates and probes :575 |
| `tools/gates/d4-assembly-check-gate.py` | :450 | Register craft :354 |
| `tools/gates/d4-typed-labels-check-gate.py` | :451 | Register craft :354 |
| `tools/gates/handoff-packet-check.py` | :500 (×2),:612 | Error patterns :468 |
| `tools/gates/lexicon-coverage-audit.py` | :607 | Gates and probes :575 |
| `tools/gates/myth-consistency-gate.py` | :608 | Gates and probes :575 |
| `tools/gates/naming-collision-gate.py` | :610 | Gates and probes :575 |
| `tools/gates/phonology-sanity-gate.py` | :606 | Gates and probes :575 |
| `tools/gates/provenance-audit.py` | :611 | Gates and probes :575 |
| `tools/gates/register-law-gate.py` | :409 (×2),:410,:418,:430,:439 | Register craft :354 |
| `tools/gates/typed-pipeline-gate.py` | :138,:187,:196,:209,:212,:418,:431,:439 | Slot-label routing / Register craft |
| `tools/harness/packet_links.py` | :452 | Register craft :354 |
| `tools/harness/packet_uncertainty.py` | :89,:128,:501 | Claim uncertainty typing :77 |
| `tools/harness/r8_checks.py` | :454 | Register craft :354 |
| `tools/harness/receipt_guard.py` | :453 | Register craft :354 |
| `tools/replay-frozen.py` | :212,:573,:613 | Derivation replay / Gates and probes |
| `tools/source-audit-inventory.py` | :614 | Gates and probes :575 |

Whole-path membership also holds (`live-not-named []` — no scoped script is absent from
SKILL.md), which is the round-24 condition's closure statement.

## 5. A09 R5 anchor reissue — old (:139e3b6 / 715 lines) → new (:HEAD / 732 lines)

**Method.** `difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)` over
`git show 139e3b6:SKILL.md` vs `SKILL.md`; opcodes give an exact address map, then each
moved address is confirmed by `grep -n` on a fingerprint of the old line.

**Change blocks — all at or after :584, net +17:**

| old → new | old → new span | shift after |
|---|---|---|
| 584 | 584–586 | +2 |
| 694–697 | 696–700 | +3 |
| 699–700 | 702–705 | +5 |
| 704 | 709–720 | +16 |
| 714–715 | 730–732 | +17 |

**Anchors that hold (unchanged address, and — for the first four — unchanged content):**

| anchor | text at HEAD | note |
|---|---|---|
| `SKILL.md:47` | label-typing row the two self-cites point at | `grep -n "SKILL.md:47" SKILL.md` → `:149`, `:183` only |
| `:149`, `:183` | the two in-file self-citations | unchanged |
| `:522` | `## Checklist (executable where a tool exists)` | unchanged |
| `:534` | `open questions — handoff-packet-check … no canon here.` | checklist's last content line; `:535` blank; `:536` `## Corpus map` |
| `:157`, `:205`, `:208`, `:262`, `:278`, `:294`, `:323-375`, `:189-214`, `:456-458` | filed-lesson citation targets | **all < :584 → all unchanged** |

**C14 fix targets landed 1-for-1 (address stable, content replaced).** `:128`, `:486`,
`:488`, `:501` are `replace` opcodes of exactly 1 line → 1 line at the same address — the
declared C14 targets (`reports/round-32/final-dossier.md:46`) were applied in place. The
difference is inside the cell, e.g. `:128`:

- old (`139e3b6`): ``rejected (`worldbible-integration-contract.md:183`; v2-design §2.3).``
- new (HEAD): ``rejected (`tools/harness/packet_uncertainty.py:205,209`; v2-design §2.3 = `reports/round-15/handoff/v2-design.md:126,131-139`; err…``

(`:486`/`:488`/`:501` differ beyond column 130 — the first 130 chars are identical, so the
pointer cells moved while the row keys stayed put.)

**Anchors that move, verified by grep:** `:660→:662` (`grep -n "^## Source-bounded culture
drill — D3 (round 7)"` → `662`), `:710→:726` (`grep -n "integration-attempts.json\` for
corrected failures"` → `726`), `:713-715→:729-732` (`grep -n "Every availability/dispatch
record filed"` → `729`; the block is now 4 lines: `:729-732`). No stale `:713`/`:715`
self-reference survives inside SKILL.md (`grep -n ":713\|:715" SKILL.md` → exit 1, 0
hits).

**Filed lesson citations — which move:** only the round-32 ones (they cite the D3 tail):

| filed citation | cited anchors | new addresses |
|---|---|---|
| `corpus/lessons/round-32.md:7,33,41,55,57,58` | `:710`, `:713-715`, `:660`, `:522-534`, `:294` | `:726`, `:729-732`, `:662`; `:522-534`/`:294` hold |
| `corpus/lessons/round-31.md:46` | `:294`, `:456-458`, `:522`, `:534`, `:535`, `:536` | hold |
| `corpus/lessons/round-25.md:44`, `round-19.md:88,100,101,179`, `round-15.md:25`, `round-14.md:141` | `:189-214`, `:278`, `:323-375`, `:262-278`, `:157`, `:205`, `:208` | hold |

**`AGENTS.md:42` — the anchor was deleted, not moved.** `git diff 139e3b6..HEAD --
AGENTS.md` → `1 file changed, 2 deletions(-)`: the closing code fence **and**
``### 2.2 `SKILL.md` — append one item to "## Checklist (executable where a tool exists)" (after :534)``
were removed at `da68a6d`. `AGENTS.md` is now 40 lines, contains **0** occurrences of
`SKILL.md` (`grep -n "SKILL.md" AGENTS.md` → none) and ends at the telemetry bullet
(`:39`). So A09-F3's "live instruction" no longer exists in the file: the reissue row for
it reads *removed at da68a6d*, and there is no new anchor to point at. (Digest:
`1afaf106f20b440a…` at `139e3b6` → `5ae7a9c8abab0843…` at HEAD.)

**Residual anchor defect at HEAD.** The round-31 checklist item still sits **outside**
`## Checklist` (`:522-535`, 4 `- [ ]` items, last content line `:534`), at `:729-732` —
F-X16-2 / Q-32-3 (`corpus/lessons/round-32.md:33,57`) is still open; the round-33 edit
extended that item's text (it now names `closes`/`closes_sha256`) without moving it.

## 6. A09 R1–R8 — current state at HEAD

| # | A09 row | state at HEAD | evidence |
|---|---|---|---|
| R1 | r26 runner README blob pin | pin line intact (`README_BASELINE_BLOB = "a3187055…"` at `:97`); **the pin has fired** — live blob is now `73f3e1bd29d4569ddd2a5d9a2309f4451fa35ae5` (README edited in place by round 33) | `reports/round-26/run-validation.py:97,1494-1500,1764`; `git hash-object corpus/lessons/README.md` = `git rev-parse HEAD:corpus/lessons/README.md` = `73f3e1bd…` |
| R2 | README sha256 receipts (6 sites) | stale: README is now `f752e1d7…`, 448 lines (was `ec7469da…`, 346) | `reports/round-25/validation.json`, `reports/round-26/audit/x63-lessons-receipt.json`, `reports/round-25/lessons/C35-C36.md`, `reports/round-26/lessons/C53.md`, `reports/round-26/scribe/fragment-ledger.json`, `corpus/lessons/round-28.md` — each still matches `ec7469da` (counts 1/1/4/5/1/1) |
| R3 | SKILL.md sha256 receipts (8 listed sites / 7 files) | stale: all still read `79fe91d3…`; HEAD is `f9bd07c2…` | `reports/round-31/validation.json` (1), `reports/round-32/validation.json` (1), `reports/round-32/dossier-d11-shonen-boxes.md` (2), `dossier-d12-capability-inventory.md` (1), `dossier-d13-operator-decisions.md` (1), `final-dossier.md` (2), `scribe/fragment-ledger.md` (2) |
| R4 | box-1 re-survey | green today **28/28 at `f9bd07c2…`, exit 0** — console only; new durable receipt owed (shape in §3) | §2; `reports/round-33/adj/audit-assembled.md:30,43` ("console output, not a filed receipt") |
| R5 | SKILL.md line anchors | mapped in §5; AGENTS.md row is a deletion; filed lesson citations split (§5) | §5 |
| R6 | README prose arithmetic / new rows | out of K04's claim-C scope (claim O); current README 448 lines / `f752e1d7…` | `wc -l corpus/lessons/README.md` |
| R7 | x45 / x57 not quotable as green | **worse than A09's reading**: x45 exit 1, `findings 1`, `X45-P1` now lists **4** uncovered pointers (`reports/round-4*` + `round-26.md:178-186` + `round-27.md:165-193` + `round-29.md:110`); x57 `--selftest` exit **1**, `passed 28 / total 37` (partition 33≠27, rows 33≠26, queue 78≠49, README-pin drift control fails) | command outputs this window |
| R8 | README rows vs `round-33.md` landing | landed: 33 `corpus/lessons/*.md`, README carries 33 index rows | `ls corpus/lessons/*.md \| wc -l` → 33; x45 stdout "lesson files: 33 / index rows: 33" |

## 7. Named findings

| id | finding | owner | evidence |
|---|---|---|---|
| **K04-F1** | The durable receipt cannot be the script's stdout verbatim: `box1-survey.py:8` hardcodes `"date": "2026-10-18"`. A 2026-10-19 receipt must set its own date or it carries a false one — the exact property claim C is calibrating. | claim-C receipt owner | §2 |
| **K04-F2** | The filed gate leg reads **Markdown only** (`documents()` `:290-303`), so the round-30 gate-satisfying artifact was `review-D29-box1.md:162-165`, not `box1-landed-survey.json`. A `.json`-only receipt satisfies claim C's prose but not the leg's shape precedent. | claim-C receipt owner + P02 plan | §3 |
| **K04-F3** | `AGENTS.md:42`'s "after :534" anchor was **deleted at da68a6d** (2-line deletion; HEAD has no `SKILL.md` mention and the fence that closed the telemetry block is gone too). A09-F3's reissue row must read *removed*, not *moved*. | integrator | §5; `git diff 139e3b6..HEAD -- AGENTS.md` |
| **K04-F4** | `reports/round-33/validation.json` records the SKILL.md change only as a porcelain line (`:81-82`, `" M SKILL.md"`); `f9bd07c2…` appears **0** times. Round 34's receipt is the first durable pin — the supersession chain (R3's 7 files) resolves to it. | integrator | §1, §6 R3 |
| **K04-F5** | Round 33 fired the R1 blob pin as predicted: live README blob `73f3e1bd…` ≠ `README_BASELINE_BLOB a3187055…` (`reports/round-26/run-validation.py:97`), whose failure leg is `:1494-1500`. Never re-run that runner in-tree. | integrator + claim-O owners | §6 R1 |
| **K04-F6** | The round-31 checklist item is still outside `## Checklist` (now `:729-732` vs section `:522-535`); Q-32-3/F-X16-2 remains open and is not closed by claim C's reissue. | integrator | §5; `corpus/lessons/round-32.md:33,57` |
| **K04-F7** | x57's historical controls degrade with the lessons index: `--selftest` now **28/37, exit 1** (A09 read 34/37); x45's `X45-P1` grew from 1 to 4 pointers. Neither is a live claim-C surface, but neither may be quoted as green at HEAD. | integrator (F4-class carry) | §6 R7 |

## 8. What claim C's builder needs from this fragment (short)

1. The digest to pin is `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`
   over 732 lines, and its first durable pin is the receipt being built (§1, K04-F4).
2. Record the **28-path set** plus `named/resolvable 28, unnamed 0`, the script digest
   `d923ae0f…`, the command string and the real date; put the full digest, a dated command
   and the words `executables`/`unnamed`/`inventory` in a **Markdown** carrier (§3, K04-F1/F2).
3. Reissue table = §5: hold `:47/:149/:183/:522/:534/:535/:536` and all pre-`:584` filed
   citations; restate `:660→:662`, `:710→:726`, `:713-715→:729-732` for
   `corpus/lessons/round-32.md:7,33,41,55,57,58`; record `AGENTS.md:42` as **removed**
   (K04-F3); the C14 targets `:128/:486/:488/:501` are in-place replacements (address
   stable), so no anchor row is owed for them.
4. R3's seven files are the supersession list for the old digest; do not edit them.

## Owed: none

K04's only named dependency (`reports/round-33/adj/A09-pins.md`) exists and was read in
full. Two artifacts this fragment specifies are **not mine to write** and remain owed by
their owners: the durable receipt pair under `reports/round-34/craft/` (claim-C
builder/integrator — §3 gives the shape) and the promotion-dossier box-1 row that
supersedes `reports/round-32/final-dossier.md:46,133` (integrator).

## Citations

- `reports/round-34/targets.json` (K04 row, `shared_rules`), `reports/round-34/claims.json` (claim C before/after), `REGIMEN.md`
- `reports/round-33/adj/A09-pins.md` full read (`:20,38-41,55-101,103-116,128-136`); `reports/round-33/adj/A10-receipt.md:57`; `reports/round-33/adj/A13-verify-a07-a09.md:105,243`; `reports/round-33/adj/A16-shonen-material.md:21,27,52,149,200-201`; `reports/round-33/adj/audit-assembled.md:30,41,43`
- `reports/round-30/craft/box1-survey.py:1-12`; `reports/round-30/craft/box1-landed-survey.json:2-8`; `reports/round-30/craft/review-D29-box1.md:3,10-11,156-167`; `reports/round-30/run-validation.py:44-45,290-303,328-329,645-652,672-684,697-703`
- `reports/round-32/final-dossier.md:46,133`; `reports/round-26/run-validation.py:97,1494-1500,1764`; `reports/round-33/validation.json:81-82` (+ `input_sha256` scan)
- `corpus/lessons/round-32.md:7,33,41,55,57,58`; `round-31.md:46`; `round-25.md:44`; `round-19.md:88,100,101,179`; `round-15.md:25`; `round-14.md:141`; `corpus/lessons/round-28.md`
- `SKILL.md:31,35,47,77,128,130,138-139,149,157-163,169,183,187,189,195-213,205,258,272-294,304-329,354,375-377,409-410,418,429-439,448-454,468,479-501,500-501,509-536,573-617,662,673-674,690-732`; `AGENTS.md:1-40`
- commands (2026-10-19T06:4xZ–07:06Z, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`; `git status --porcelain`; `git log --oneline -6`; `git log --oneline -- reports/round-30/craft/box1-survey.py`; `git show 71cd9d3:reports/round-30/craft/box1-survey.py | diff - reports/round-30/craft/box1-survey.py`; `git log --oneline -3 -- SKILL.md`; `git diff 139e3b6..HEAD --numstat -- SKILL.md`; `git diff --numstat -- SKILL.md`; `git diff 139e3b6..HEAD --stat -- AGENTS.md`; `git diff 139e3b6..HEAD -- AGENTS.md`; `git show 139e3b6:SKILL.md | wc -l` / `| sha256sum`; `git show 139e3b6:AGENTS.md | sha256sum`; `sha256sum SKILL.md AGENTS.md reports/round-30/craft/box1-survey.py corpus/lessons/README.md`; `wc -l SKILL.md AGENTS.md corpus/lessons/README.md`; `git hash-object corpus/lessons/README.md`; `git rev-parse HEAD:corpus/lessons/README.md`; `ls corpus/lessons/*.md | wc -l`; `python3 -B reports/round-30/craft/box1-survey.py` (exit 0); difflib script (SequenceMatcher opcodes + old→new map, run on `git show 139e3b6:SKILL.md` vs `SKILL.md`); regex census of `tools/*.py` paths + section attribution over `SKILL.md`; inline live-executable-vs-named set comparison (`tools`, `tools/gates`, `tools/harness`); `grep -n` fingerprint checks for `:582`-region, `^## Source-bounded culture drill`, `integration-attempts.json\` for corrected failures`, `Every availability/dispatch record filed`, `SKILL.md:47`, `:713|:715`; `grep -n "SKILL.md" AGENTS.md` (0 hits); `grep -rn "79fe91d3|ec7469da|83b0a78a"` over the cited files; `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` (exit 1, `X45-P1`, 4 pointers); `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest > .scratch/K04-x57.json` (exit 1, passed 28/37); `python3 -c` JSON scans of `reports/round-33/validation.json`, `.scratch/K04-x57.json`
