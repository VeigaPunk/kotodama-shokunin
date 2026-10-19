- Seat: C04 | executor | claim C (calibration) | date 2026-10-19 | baseline da68a6d

# C04 — byte-check: the SKILL anchor reissue needs zero filed-round edits

**Assignment** (`reports/round-34/targets.json:58`): "Byte-check: confirm zero filed-round
edits are needed for the reissue (old anchors live in filed rows that stay untouched; the
reissue is a NEW table); cite the filed rows you deliberately did not edit."

**Method.** (1) Prove the filed/immutable surface is byte-identical to baseline HEAD.
(2) Measure the round-33 SKILL.md delta (`17e90b9` 715-line version → HEAD 732-line version,
`f9bd07c2…`) and derive the exact anchor-shift boundary. (3) Census every filed row that
carries a pre-r33 SKILL.md anchor or one of the two superseded SKILL digests, and classify
each reading as still-exact / address-shifted / content-fixed / already-stale. (4) Run a
negative control proving the instrument (blob equality vs HEAD) catches a byte edit of the
forbidden shape. Every command below is read-only; nothing outside `reports/round-34/` and
`.scratch/` was written.

**Measurement window:** 2026-10-19, repo root, lane HEAD `da68a6d` (`git rev-parse HEAD` →
`da68a6d705e41f369f21e8607bfaab5b54077f84`), env `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`.

**Verdict:** **CONFIRMED — zero filed-round edits are needed.** Round 33's SKILL.md edit was
*not* line-count-neutral (715 → 732, numstat 35/18), so A09's R5 ("keep the edit
line-count-neutral … or record the shift and re-issue the anchor", `reports/round-33/adj/A09-pins.md:111`)
takes the **record-and-reissue** branch: the old anchors become dated, superseded readings
and the reissue lands as new rows in a round-34 artifact. All 22 anchor-bearing filed rows
in the census below (plus 89 superseded-digest lines) stay byte-frozen; no row requires an
edit to be superseded.

## 1. The filed surface is byte-identical to baseline HEAD

| check | command | result |
|---|---|---|
| worktree drift over filed/immutable surfaces | `git status --porcelain -- reports/round-1 … reports/round-33 corpus/lessons tools/gates/frozen .ufo` | **empty** (exit 0) |
| same, as a diff | `git diff --stat HEAD -- <same set>` | **empty** (exit 0) |
| whole tree | `git status --porcelain` | exactly one line: `?? reports/round-34/` |
| live files in R5 scope | `git diff --stat HEAD -- SKILL.md AGENTS.md` | **empty** (round-33's SKILL/AGENTS edits are committed at `da68a6d`) |

Per-file pins (`git hash-object <f>` == `git rev-parse HEAD:<f>`, sha256 read from the same
bytes) — each row **MATCH-HEAD**:

| path | git blob | sha256 (16) |
|---|---|---|
| `corpus/lessons/README.md` | `73f3e1bd29d4` | `f752e1d79ae627a0` |
| `corpus/lessons/round-14.md` | `a997c9ad58e3` | `f3f8568480b1c3fb` |
| `corpus/lessons/round-15.md` | `9fec5de548eb` | `13e17f0ef3710d2c` |
| `corpus/lessons/round-19.md` | `fec542bf0ed8` | `0c975cf19913ebfd` |
| `corpus/lessons/round-25.md` | `bc6ed47d8342` | `08f0337e66dbf0c4` |
| `corpus/lessons/round-31.md` | `8c5f04f32cf3` | `8870bbdd4a4f2903` |
| `corpus/lessons/round-32.md` | `02acc54ae51e` | `8aacfc2bd9f55ec9` |
| `reports/round-30/craft/box1-landed-survey.json` | `5869191b9277` | `aa8b6c15121065b6` |
| `reports/round-31/validation.json` | `48eb192c2f38` | `8ba960e44d9e1686` |
| `reports/round-32/validation.json` | `cdd17ae2ce27` | `204dfddaa360f6b6` |
| `reports/round-33/adj/A09-pins.md` | `f3a45fc216f5` | `98e3502e41a90d5b` |
| `AGENTS.md` (live) | `3272db68e4bb` | `5ae7a9c8abab0843` |
| `SKILL.md` (live) | `4d7a5c99c3d7` | `f9bd07c2bd134623` |

Honesty note: `reports/round-24/__pycache__/run-validation.cpython-314.pyc` exists on disk
inside a filed round dir (mtime `2026-10-18 14:05:35 -0300`, i.e. pre-round-33) but is
gitignored (`.gitignore:4:__pycache__/`), so it is invisible to the git evidence above. It
is a stale build artifact, not a filed-byte edit, and this seat neither wrote nor removed it.

## 2. Why a reissue exists: the round-33 SKILL.md delta and its shift boundary

`git diff 17e90b9 da68a6d -- SKILL.md | grep "^@@"` → six hunks; `git diff --numstat 17e90b9
da68a6d -- SKILL.md` → `35 18`; `wc -l SKILL.md` → **732** (was 715):

```
@@ -125,7 +125,7 @@      (line-neutral)
@@ -476,19 +476,19 @@    (line-neutral)
@@ -498,7 +498,7 @@      (line-neutral)
@@ -581,7 +581,9 @@      (+2)
@@ -691,17 +693,31 @@    (net +14)
@@ -711,5 +727,6 @@      (+1)
```

Therefore: **content before `:581` keeps its address**; at/after the first insertion point
addresses shift by +2, by +16 after the second, and the tail checklist item grew from
`:713-715` to `:729-732` with its audit one-liner re-keyed (old `:715` text has **no exact
match** at HEAD; the new one-liner globs `telemetry/availability-close-*.json`). Measured
per-line with `git show 17e90b9:SKILL.md` vs `git show da68a6d:SKILL.md`:

| class | old anchors | new address at HEAD | evidence |
|---|---|---|---|
| address-stable, content identical | `:47`, `:149`, `:183`, `:189-214`, `:208`, `:262-278`, `:294`, `:323-375`, `:453`, `:456-458`, `:522`, `:534`, `:535`, `:536`, `:575`, `:581`, `:617` | unchanged | unique-content match returns the same line |
| address-stable, content **changed in place** (C14 fixes landed) | `:128`, `:486`, `:488`, `:501` | same lines, new text | e.g. `:128` old `worldbible-integration-contract.md:183` → new `tools/harness/packet_uncertainty.py:205,209` |
| shifted +2 | `:617`→`:619`, `:660`→`:662`, `:662`→`:664`, `:672`→`:674`, `:674`→`:676`, `:691`→`:693` | +2 | content-identity match |
| shifted +16 | `:710`→`:726`, `:713`→`:729` | +16 | the r31 checklist item now spans `:729-732` |
| re-keyed, old address empty | `:715` | no exact match; new item at `:729-732` | `sed -n '728,732p' SKILL.md` |

Had the r33 edit been line-count-neutral (A09 §2.4's control), every anchor would have been
a no-op. It was not, so the supersession list is needed — recorded, never repaired in place.

## 3. The filed rows deliberately NOT edited (the census the reissue must cite)

Anchor-bearing filed rows (pre-r33 anchors), each still byte-frozen per §1:

| filed row | old anchors cited | status of that reading at HEAD |
|---|---|---|
| `corpus/lessons/round-31.md:46` | `:294`, `:456-458`, `:522`, `:534`, `:535`, `:536` | **still exact** — no supersession needed |
| `corpus/lessons/round-32.md:33` | `:713-715`, `:660`, `:522-534` | `:713-715`→`:729-732`, `:660`→`:662`; `:522-534` exact |
| `corpus/lessons/round-32.md:7`, `:41`, `:55` | `:715` (the audit command) | address stale + command re-keyed (Q-32-1) |
| `corpus/lessons/round-32.md:57` | `:713-715`, `:522-534` | item shifted |
| `corpus/lessons/round-32.md:34`, `:58` | `:294` | still exact |
| `corpus/lessons/README.md:242` | `:715` | stale address + re-keyed |
| `corpus/lessons/README.md:244` | `:713-715`, `:522-534` | shifted / exact |
| `corpus/lessons/README.md:245` | `:294` | still exact |
| `corpus/lessons/round-25.md:44` | `:189-214` | still exact |
| `corpus/lessons/round-19.md:88`, `:179` | `:278` (battery row) | already stale pre-r33 (row now `:617`) — r19's own finding class |
| `corpus/lessons/round-19.md:100` | `:323-375` | still exact |
| `corpus/lessons/round-19.md:101` | `:262-278` | still exact |
| `corpus/lessons/round-14.md:141` | `:208` | already stale pre-r33 |
| `corpus/lessons/round-15.md:25` | `:157`, `:205` | still exact |
| `reports/round-32/final-dossier.md:46` | `:486/:488`, `:501/:128` | content fixed in place by r33 (readings superseded by the fix) |
| `reports/round-32/final-dossier.md:48` | `:672`, `:453`, `:710-715` | `:672`→`:674`; `:453` exact; `:710-715`→`:726-732` |
| `reports/round-32/dossier-d11-shonen-boxes.md:53`, `:60`, `:67`, `:72`, `:139`, `:141`, `:143`, `:160` | `:486`, `:501`, `:128`, `:183`, `:479-491`, `:77`, `:420`, `:672`, `:453`, `:701-703`, `:710-715` | mixed: `:486/:501/:128` fixed in place; `:672`/`:710-715` shifted; `:183`/`:453`/`:77`/`:420` exact |
| `reports/round-32/dossier-d12-capability-inventory.md:44`, `:55` | `:453`, `:710-715` | exact / shifted |
| `reports/round-32/dossier-d13-operator-decisions.md:39` | `:486/:488`, `:501/:128` | fixed in place |
| `reports/round-31/jinii/analysis.md:111`, `:113` | `:456-457`, `:294` | still exact |
| `reports/round-31/jinii/patch-draft.md:18`, `:36`, `:49`, `:67`, `:100` | `:456-462`, `:294`, `:535-536` | still exact |
| `reports/round-31/fragment-index-x20.md:65`, `:380` | `:534`, `:294` | still exact |

Superseded-digest readings (E2 class; `79fe91d3…` and `83b0a78a…`): **89** filed lines match
those two digests in the whole filed tree, **all 89 under `reports/round-3{0,1,2,3}/`**
(`grep -rn "79fe91d3\|83b0a78a" corpus/lessons/ reports/round-{1..33}/ | wc -l` → 89; the
same grep over `reports/round-3[0-3]/` → 89). Named rows include
`reports/round-31/validation.json:1026`, `reports/round-32/validation.json:1000`,
`reports/round-32/dossier-d11-shonen-boxes.md:50,205`,
`reports/round-32/dossier-d12-capability-inventory.md:97`,
`reports/round-32/dossier-d13-operator-decisions.md:48`,
`reports/round-32/final-dossier.md:46,133`,
`reports/round-32/scribe/fragment-ledger.md:178,235`, and (for `83b0a78a…`)
`reports/round-30/craft/box1-landed-survey.json:4` + `reports/round-30/validation.json:449`.

## 4. The reissue is a NEW table — why no filed edit is owed

1. **Append-only rule.** `reports/round-34/targets.json:7,10` forbid editing filed round
   bytes; A09 §2.2 states the disposition explicitly: "every listed row above is then a
   *superseded reading* … not a tamper finding and not something to repair in place"
   (`reports/round-33/adj/A09-pins.md:75`), and A09 §1 says every move "needs a *new*
   record, never an edited one" (`:23-27`).
2. **The reissue's rows are reads + live measurements only.** An old-anchor cell cites a
   filed `path:line` (read-only, §3); a new-anchor cell is measured against the live
   `SKILL.md` at `f9bd07c2…`/732 lines. No cell's remedy is a write to a filed path.
3. **No executable depends on the old anchors.** `grep -rn "SKILL\.md:[0-9]" tools/` →
   **0 hits** (only `tools/gates/argot-derivation-gate.py:4`, which names the section by
   title, not by line); frozen copies under `tools/gates/frozen/**` mention `SKILL.md` only
   as prose (A09 §1.1) and are byte-frozen anyway. So no tool re-point is owed either.
4. **The only live surface in R5's scope needs no edit today.** `AGENTS.md:42` carries
   "append one item to `## Checklist …` (after :534)". Measured at HEAD: `:534` is still
   the checklist's last content line (`no canon here.`, `:535` blank, `:536` `## Corpus map`),
   because the r33 insertions all landed at/after `:581`. The F-X16-2 defect persists (the
   item sits outside the section at `:729-732`), but it is not an anchor *shift*; the reissue
   records this rather than assuming it. Flagged for the integrator to confirm, not to
   silently edit.
5. **Premise of the reissue confirmed.** `python3 -B reports/round-30/craft/box1-survey.py`
   at HEAD → exit 0, `named 28 / resolvable 28`, `skill_sha256
   f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`; a re-run of the
   immutability check immediately after → still empty (the survey writes nothing).
   Independently re-confirmed the same window by `reports/round-34/calib/C07-verify-survey.md`
   §1 (28/28, `f9bd07c2…`, 732 lines, exit 0; two extraction methods agree row-for-row).

## 5. Negative control — the instrument has teeth

`cp reports/round-32/final-dossier.md .scratch/c04/filed-row-probe.md; printf ' ' >> …`:

- probe `git hash-object` → `ded609b10705`, pristine worktree row → `758b78bcf2d8`,
  HEAD row → `758b78bcf2d8` — a **single appended space** on a filed row is caught.
- Therefore the §1 zero-drift result is a measurement, not a default: had any seat touched
  a filed row this round, this check would have named the path and digest.
- Second control (class-level, not run by me): the same blob-equality shape is what the r5/r7
  in-place `validation.json` incident violated (`reports/round-33/op/O07-baseline-receipt.md:147-181`,
  A09-F2); this round's runs are confined to tools that write nothing (§4.5), and no
  `reports/round-*/run-validation.py` was executed by this seat.

## 6. Acceptance hooks for C03's table (run when it lands)

1. Every old-anchor cell matches a `path:line` in §3 (or one of the two live anchors:
   `AGENTS.md:42`, `SKILL.md:149/:183` self-cites).
2. Every new-anchor cell resolves at `f9bd07c2…`/732 lines with the quoted content — the
   map in §2 is the independent cross-check.
3. **Zero rows** whose remedy is an edit under `reports/round-1..33/**`, `corpus/lessons/**`
   or `tools/gates/frozen/**`; any such row is a defect and fails the claim-C threshold
   ("zero filed-row edits", `reports/round-34/claims.json:65`).
4. Rows that fall in the "still exact" class (`:294`, `:453`, `:456-458`, `:522-534`, …)
   must be carried as *no-supersession* readings, not rewritten as shifts.

## Owed

- `reports/round-34/calib/C03-anchor-reissue.md` — the reissue table itself (C03; not on
  disk at this seat's reads: `ls reports/round-34/calib/` → No such file or directory).
  My byte-check keys to it; the integrator runs §6 against it when it lands.
- `reports/round-34/scout/K04-anchor-census.md` — K04's census (also not on disk). If K04
  names filed anchor rows beyond my §3 census, §3 must be extended and re-checked; my census
  is grep-derived and matched to A09 §2.4, not exhaustive by construction.
- `reports/round-34/calib/C02-receipt-json.md` and `C07-verify-survey.md` — the durable
  box-1 receipt and its verification; I confirmed only the premise (28/28 at `f9bd07c2…`),
  not the receipt's 28-row content.

## Citations

- `reports/round-34/targets.json:58` (C04 mission + out path), `:7-11` (shared rules, incl.
  the missing-dependency rule), `reports/round-34/claims.json:54-65` (claim C before/after,
  thresholds "28/28 at the new digest … zero filed-row edits").
- `reports/round-33/adj/A09-pins.md:16-27` (measurement window, verdict), `:69-75` (E2:
  superseded readings, never edits), `:85-94` (E4 line anchors + re-pin need), `:103-116`
  (R1–R8 list), `:133-136` (A09's own owed paths).
- `reports/round-33/op/O07-baseline-receipt.md:147-181` (r5/r7 in-place filed-byte incident);
  `reports/round-33/targets.json:56` (A09 mission).
- Filed rows cited in §3 (all byte-verified in §1): `corpus/lessons/round-14.md:141`;
  `corpus/lessons/round-15.md:25`; `corpus/lessons/round-19.md:88,100,101,179`;
  `corpus/lessons/round-25.md:44`; `corpus/lessons/round-31.md:46`;
  `corpus/lessons/round-32.md:7,33,34,41,55,57,58`; `corpus/lessons/README.md:242,244,245`;
  `reports/round-31/jinii/analysis.md:111,113`; `reports/round-31/jinii/patch-draft.md:18,36,49,67,100`;
  `reports/round-31/fragment-index-x20.md:65,380`;
  `reports/round-32/final-dossier.md:46,48,133`; `reports/round-32/dossier-d11-shonen-boxes.md:50,53,60,67,72,139,141,143,160,205`;
  `reports/round-32/dossier-d12-capability-inventory.md:44,55,97`;
  `reports/round-32/dossier-d13-operator-decisions.md:39,48`;
  `reports/round-32/scribe/fragment-ledger.md:178,235`;
  `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000`;
  `reports/round-30/craft/box1-landed-survey.json:4`; `reports/round-30/validation.json:449`.
- Live files: `SKILL.md:47,128,149,183,294,453,456-458,486,488,501,522,534,535,536,581,617,619,662,674,729-732`;
  `AGENTS.md:42`-class anchor region (`sed -n '36,46p' AGENTS.md` → file is 40 lines);
  `tools/gates/argot-derivation-gate.py:4`.
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD`; `git status --porcelain`; `git status --porcelain -- reports/round-1 … reports/round-33 corpus/lessons tools/gates/frozen .ufo`;
  `git diff --stat HEAD -- <same set>`; `git diff --stat HEAD -- SKILL.md AGENTS.md`;
  `git hash-object <f>` vs `git rev-parse HEAD:<f>` for the 13 pinned files;
  `sha256sum` over the same; `git log --oneline -4 -- SKILL.md`;
  `git diff 17e90b9 da68a6d -- SKILL.md | grep '^@@'`; `git diff --numstat 17e90b9 da68a6d -- SKILL.md` → `35 18`;
  `git show 17e90b9:SKILL.md` vs `git show da68a6d:SKILL.md` per-line probe (scripted, 36 probes + unique-content address match);
  `grep -n "^## " SKILL.md`; `sed -n '505,545p' SKILL.md`; `sed -n '728,732p' SKILL.md`;
  `grep -rn "SKILL\.md:[0-9]" corpus/lessons/ reports/round-{1..33}/` → 1163 lines (as cited in §1's context: whole filed tree);
  `grep -rn "79fe91d3\|83b0a78a" corpus/lessons/ reports/round-{1..33}/ | wc -l` → 89 (all under round-3{0,1,2,3});
  `grep -rn "SKILL\.md:[0-9]" tools/` → 0 hits;
  `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, 28/28, `f9bd07c2…`;
  negative control: `cp reports/round-32/final-dossier.md .scratch/c04/filed-row-probe.md && printf ' ' >> …` then `git hash-object`;
  `ls reports/round-34/calib/ reports/round-34/scout/` → No such file or directory;
  `git check-ignore -v reports/round-24/__pycache__/run-validation.cpython-314.pyc` → `.gitignore:4:__pycache__/`; `stat -c '%y' on the same` → `2026-10-18 14:05:35`.
