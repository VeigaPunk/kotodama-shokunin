# Round-10 drift shard 11 (R10-F11)

- seat: R10-F11 drift re-runner, shard "SKILL.md lines 201-231 + SCORECARD.md
  `re-run command` column entries whose commands live in this shard".
- date: 2026-10-17. Clock for every measurement below: `2026-10-17T21:2x-21:31Z`
  (`date -u` at close: `2026-10-17T21:31:06Z`); local time is UTC-03:00.
- tree measured: `git rev-parse HEAD` → `e3a1ec9435787328ac9f828f96cb6390e4916b8f`.
  Round-10 declared `baseline_revision` `9dc18ec1339bffd6f81e74f1a5742464ef578749`
  = round-9's admission commit. Round-5's own baseline `1ccb2b7119039d8026ad1d004f20427623838b94`
  exists as a commit (`git cat-file -t` → `commit`).
- this file is the seat's only deliverable write. Scratch receipts live under
  `.scratch/f11/` (untracked, disposable): `rv2.out`/`rv2.err` (isolated
  round-5 re-run), `battery-bare.out`, `battery-allroots.json`, `controls.txt`,
  `mirror/` (the isolated copy). `TMPDIR=$PWD/.scratch` for every command;
  `/tmp` untouched.

## 0. Scope of this shard

Runnable commands inside SKILL.md 201-231: exactly one —
`python3 reports/round-5/run-validation.py` (SKILL.md:210). No URL-only
citation appears in the range. The same command is the `re-run command` cell
of five SCORECARD rows (SCORECARD.md:30 depth, :32 operability, :33 freshness,
:34 calibration, :35 adjacency — all round 5), so those five rows' command is
in shard. The other commands in those same cells
(`tools/check-craft-exercise.py …`, `tools/check-gate-battery.py --selftest`,
`tools/source-audit-inventory.py …`, `tools/gates/handoff-packet-check.py …`)
appear in other SKILL.md line ranges and belong to other shards; two of them
were still run here as *masked-step controls* (§2.5) because the in-shard
command invokes them internally and its early abort hid their status.

## 1. Method and isolation — including one disclosed accident

`reports/round-5/run-validation.py` is not read-only: it writes
`reports/round-5/validation.json` (script line 194) and, if it got that far,
`reports/supplement-opencode-1/32-craft-exercise.md` (line 129). A byte-safe
re-run therefore needs a copy, the method round-9's registry used
(`reports/round-9/baselines/registry.md`, "measured where: an isolated mirror").

**Accident, disclosed:** my first attempt set the shell cwd to the real lane
root by mistake (`cd …/kotodama-shokunin` inside the command overrode the
intended working directory), so that run executed **in the live tree** and
rewrote the filed receipt `reports/round-5/validation.json`
(mtime 16:50:23 → 18:27:32; sha256 `78444f4cca7497da34f9f8b3dfbe54998b1bace6b8e22731cf11bbd9f2e7ae44`
→ `08a248b831324c0362c799c4281daf4023c4744b9cfc47d197b5861300138d75`).
It aborted inside the O claim before line 129, so
`reports/supplement-opencode-1/32-craft-exercise.md` was not written
(`git status` never listed it). Repair: `git show HEAD:reports/round-5/validation.json`
→ byte-for-byte restore; re-verified sha256 `78444f4c…e44`, size 23928,
`git status --porcelain -- reports/round-5/validation.json` empty. No filed
byte is left changed by this seat. The two other modified paths in
`git status` (`corpus/README.md`, `reports/round-9/validation.json`) belong to
concurrent round-10 workers and were not touched here.

All measurements below come from the corrected isolated run:
`cp -a corpus tools examples reports/round-5 reports/supplement-opencode-1`
into `.scratch/f11/mirror/` (12 MB, `__pycache__` and
`reports/supplement-opencode-1/scratch` excluded), then from
`.scratch/f11/mirror/`:

```
TMPDIR=<lane>/.scratch GIT_DIR=<lane>/.git GIT_WORK_TREE=<lane>/.scratch/f11/mirror \
  python3 reports/round-5/run-validation.py
```

`GIT_DIR`/`GIT_WORK_TREE` keep the script's `git show <BASE>:<path>` reads on
the real object store and its `git diff --check` on the mirror, so the live
worktree (with other workers' in-flight edits) is not consulted. The mirror
run wrote its own receipt at
`.scratch/f11/mirror/reports/round-5/validation.json`
(sha256 `0a0f492a17e13f09eb644f8c60e93de1cddea1c7405ff97fe32a5b163b721da6`,
17406 bytes) and reproduced the live-tree failures exactly.

## 2. In-scope command: `python3 reports/round-5/run-validation.py`

**Verdict: `stale-documented` — exit 1 at HEAD, three independent causes, all
traceable to legitimate later-round work. The filed receipt stays historical
(acceptance true at round 5); the command is not re-runnable green today.**

| field | value |
|---|---|
| command | `python3 reports/round-5/run-validation.py` |
| source locator | `SKILL.md:210`; `SCORECARD.md:30,32,33,34,35` |
| exit | **1** |
| stdout sha256 | `2e7d8c0ff2faabafa72e3e132526b0cef6e059b263206ba0b048b9dd91c2fd0a` |
| filed receipt (HEAD) | `reports/round-5/validation.json`, sha256 `78444f4cca7497da34f9f8b3dfbe54998b1bace6b8e22731cf11bbd9f2e7ae44`, 23928 B, `acceptance_checks_passed: true`, F/O true |
| declared claims at HEAD | F=false, O=false; `errors.F` and `errors.O` quoted below |

### 2.1 Cause F-1 — round-8 frontmatter insertion breaks the append-only assertion

`errors.F` = `non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')`.
The script asserts (line 82) `current_bytes.startswith(git show BASE:entry)`.
Sweep of all 22 audits (command in §5.1): **22 of 22 fail** — i.e. every one
of the 11 cited entries, not just ottoman:

```
(4, OTT-06, ottoman.md) (4, S09-07, slavs-early.md) (5, S09-08, slavs-early.md)
(5, SOG-29, sogdian-silk-road.md) (6, TIB-A12/TIB-A16, tibet.md)
(7, TURK-06/07, turkic-steppe.md) (8-9, meso-13..16, mesoamerica-primary-sources.md)
(10, COL-06/07, color-terminology.md) (11, KIN-A07/A08, kinship-terminology.md)
(12, ORALITY-05, orality-formulaic-language.md) (12, PHON-A11, phonetics-phonology.md)
(13, SR-REG-04/07, sociolinguistics-registers.md)
```

Cause, with evidence: round-8's metadata conformance pass
(commit `e1694ba`, `round-8: admit F/O/D — freshness receipts, harness+gate
repairs, d2-typed-labels`) inserted 2-15 frontmatter lines per entry after the
`- couples:` line (its own fragments say so, e.g.
`reports/round-8/metadata/m04-civ-58-76.md:15-16` "one `- source:` /
`- verified-at:` / `- recheck:` triad inserted immediately after each entry's
`- couples:` header line"). `git log --oneline BASE..HEAD -- <entry>` names
only `e1694ba` for ottoman; `git diff BASE HEAD -- ottoman.md` shows three
added lines and the diff of the file's first bytes is unchanged (`head -c 300`
still starts `# Ottoman Worlds …`).

**Control that the drift is insertion-only, not content loss** — additive-only
for all 11 entries (`git diff --numstat BASE HEAD -- <entries>`, §5.1):
`3/0` (six civilization entries), `2/0` (four linguistics entries), `15/0`
(phonetics-phonology, which also carries the round-5/round-6 errata appended
below). Zero deletions anywhere, so the round-5 *claims* survive; only the
byte-prefix rule is violated.

Documentation status: round 8 documents the insertion
(`reports/round-8/metadata/m0*.md`), but **no later round states that
round-5's re-run now fails** — grep for `round-5/run-validation` in
`reports/round-8`, `reports/round-9`, `corpus/lessons/round-8.md`,
`corpus/lessons/round-9.md` returns only the round-9 battery-coverage
discussion (§2.2). This leg is therefore stale with a *documented cause* but
an unremarked *consequence*; the F15-F18 fixers should decide between a
corrected expectation (append-only → additive-only) and a supersession note.

### 2.2 Cause O-1 — the battery's default roots no longer cover all seven gates

`errors.O` = `['/usr/bin/python3', 'tools/check-gate-battery.py']: expected 0, got 2`.
Bare battery at HEAD: exit **2**, stdout sha256
`f456f79d92a14baa0c67b4e696caf2fa7c3aa1f67c6403919af32b9db2d2d68d`;
mode `baselines`: `baselines_found 5`, `gates_covered` = costume, handoff,
lexicon, phonology, provenance, `gates_uncovered` = **myth-consistency-gate.py,
naming-collision-gate.py**, `baseline_exit 2`, findings
`BASELINE-GATE-UNCOVERED` ×2; the seven gate selftests themselves all pass
(`fail 0, pass 7, unevaluable 0`, `originals.preserved true`, 28 files hashed).

Cause: round 9 (`9dc18ec`, battery 488 → 1117 lines) gave the battery a
baseline duty whose default roots are
`BASELINE_ROOTS = (tools/gates/expected, tools/gates/frozen)`
(`tools/check-gate-battery.py:114`), while two of round-9's seven baselines
were committed under `reports/round-9/baselines/`
(`reports/round-9/baselines/myth-consistency-gate/expected.json`,
`…/naming-collision-gate/expected.json`). The round-9 evidence declares that
root in prose (`reports/round-9/report-draft.md:60` "all **7/7 gates** carry a
baseline … `find tools/gates reports/round-9 -name expected.json`") but the
tool's default does not include it. Round 9 predicted this exact outcome:

> "If round 9 closes with the baselines still outside the default roots,
> round-5's re-run will report a failure that is the honest reading of the
> placement question, not a regression — the integrator should say which."
> — `reports/round-9/baselines/battery-extension.md:239-242`

No integrator decision is recorded in the round-9 admission or SCORECARD, so
the predicted failure is now live. **Verdict `stale-documented` (predicted by
round 9, decision outstanding), not a content defect.**

**Control that restores green** (three roots declared, `--baselines-root` is
repeatable and replaces the defaults):

```
python3 tools/check-gate-battery.py \
  --baselines-root tools/gates/expected \
  --baselines-root tools/gates/frozen \
  --baselines-root reports/round-9/baselines
```

exit **0**, stdout sha256 `06d5ba01a495f085b4ea7ba466c40d5f15b69f3a89afb5b0af1d9d6dfab66744`,
`summary {battery_exit 0, fail 0, pass 7, unevaluable 0}`,
`baselines_found 8`, `pinned 8`, `gates_covered` all seven,
`gates_uncovered []`, findings 0. (Eight files for seven gates because
handoff-packet-check carries a baseline under both `tools/gates/frozen/` and
`reports/round-9/baselines/` — round 9 flagged that duplicate as `to-verify`,
`battery-extension.md` §8.) So round-9's 7/7 claim is **true as a fact about
committed baselines** and **false as a property of the tool's default
invocation**; the fix is a default-roots or placement decision, owned by the
orchestrator, not by this shard.

### 2.3 Cross-shard observation for the round-9 SCORECARD row

`SCORECARD.md:144` (round-9 operability) describes the 7/7 baselines as living
in "both `tools/gates/expected/` and `tools/gates/frozen/<gate>/r9-pre/`
layouts". On disk, two of the seven live under a **third** root —
`reports/round-9/baselines/myth-consistency-gate/expected.json` and
`…/naming-collision-gate/expected.json` (`find tools/gates reports/round-9
-name expected.json` → 8 files covering 7 gates, 2026-10-17). The row's own
evidence pointer (`reports/round-9/baselines/*`) and
`reports/round-9/report-draft.md:60` do carry the third root, so the fact is
documented; only the parenthetical's "both … layouts" is incomplete. Flagged
here because it is the same placement question that makes the battery's
default invocation fail (§2.2); the row itself belongs to whichever shard
covers SCORECARD's round-9 block.

### 2.4 Cause O-2 (masked by the abort) — round-3 frozen replay is now could-not-evaluate

The abort at script line 120 means lines 121-177 never ran in either the live
or the mirror run; run separately, the next replay step is red:

| command | exit | stdout sha256 |
|---|---|---|
| `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | `76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80` |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 2 | `409db5ab8b68ebc3da9a8360879db71c01e58b40ea4a8311e3818efe289c8452` |

Both print `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch,
0 reproduced of 7 row(s)`, every row `reason=gate_digest_mismatch` (e.g. ROW 2
`gate=tools/gates/phonology-sanity-gate.py`). Cause: the round-3 manifests pin
gate bytes from round 2/3, and all seven gate scripts were last modified in
`e1694ba` (round 8's gate repairs — `git log --oneline -3 -- tools/gates/*.py`
returns `e1694ba`, `1688790`, `291c714`); `replay-frozen.py` itself is
unchanged since `c53782a`. The round-5 expectation `"REPLAY OK: 7/7"` (script
line 159) can no longer hold in the live tree, and round-5's O claim "both
round-3 manifests reproduce 7/7" is stale in the same sense. This is the same
class of drift round 8/9 handled for D3 by re-pinning; re-pinning or
superseding the round-3 manifests is a decision for the owning shard/fixers,
not this one.

### 2.5 Masked-step controls that are still green

| step (round-5 script line) | command | exit | stdout sha256 |
|---|---|---|---|
| 119 | `python3 tools/check-gate-battery.py --selftest` | 0 | `8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28` (prints `SELFTEST OK 28/28 controls behaved as expected`) |
| 125 | `python3 tools/check-craft-exercise.py --selftest` | 0 | `77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32` |
| 129-130 | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 | `18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650` |

So the drift is confined to the battery's exit semantics and the frozen pins;
the selftest controls and the contrastive example itself are current.

## 3. Cited-path, ID and claim verification for SKILL.md 201-231

Every path and identifier cited in the shard resolves; no `to-verify` item
was created by this shard.

| SKILL.md line | citation | check | reading |
|---|---|---|---|
| 203 | `reports/round-5/15-cli-review.md` "LAW-ORDER early-return coverage limitation remains recorded" | file exists, 27414 B; `grep -n LAW-ORDER` | `:57 ### F4. LAW-ORDER early return silently skips most checks`, plus `:172`, `:232`, `:253` — current |
| 210 | `python3 reports/round-5/run-validation.py` | re-run (§2) | stale-documented |
| 218 | `corpus/lessons/round-5-sources/08.json` (meso-13 publisher abstract) | `python3 -c` read of the audit row | `meso-13 supported True`, url `https://api.crossref.org/works/10.1017/RDC.2020.71`, locator "JATS 'abstract' field, Radiocarbon 62(6):1543-1550", excerpt gives 991-1147 vs 1159-1261 cal AD (bark-paper cleaning) — matches the row |
| 219 | Lowie / KIN-A07+A08 residuals | `reports/round-5/parent-reconciliation.json` | both `unresolved` — matches "residuals stay unresolved" |
| 220 | SR-REG-07 | same file | `supported` — row's "secondary quotation vs unread primary pages" caveat is in the spotchecks, not contradicted |
| 221 | TIB-A12/A16 | same file | both `unresolved` — matches "do not merge editions into one verified claim" |
| 222 | PHON-A11 + appended erratum in `corpus/knowledge/linguistics/phonetics-phonology.md` | `grep -n PHON-A11` / `-i erratum` | `:70` records PHON-A11 and the two errata; `:321` "supersedes only the bibliographic uncertainty in the preceding erratum"; `:324` audit pointer — current |
| 228 | R6-05-A, parent P04, Hattic legs partial | `reports/round-6/parent-reconciliation.json` | row present; basis "…but not all language-genealogy legs" — matches |
| 229 | R6-03-B, parent P02 | same file | row present; basis gives Louvre E 12026 pleated-linen/plain-weave fields and late Dyn. 11/early Dyn. 12 context — matches |
| 230 | R6-13-A, parent P03, appended `india-vedic.md` erratum | same file + `corpus/knowledge/civilizations/india-vedic.md` | row present; the erratum is at `india-vedic.md:198 ## Round 6 source erratum — Gobhila timing and textual mediation` with the three alternatives at `:203`. Note: the bare filename in SKILL.md resolves to `corpus/knowledge/civilizations/india-vedic.md` (not the lane root or a partition root) — unambiguous by content, worth a path if the file is ever re-cited |
| 231 | R6-13-B, parent P01 | same file | row present; basis "ground skins versus attached horn and the school-difference report in Eggeling's footnote" — matches |
| 200-201 (boundary) | "Its embedded historical counting-command string points to ignored scratch" | `grep -o '[^"]*scratch[^"]*' examples/supplement-opencode-1/sound-change-vs-taboo.json` | the string is `python3 reports/supplement-opencode-1/scratch/32/check_exercise.py … --counts` at `sound-change-vs-taboo.json:367` (`counting_command`) and `:268-270`, and `.gitignore` ignores `/reports/supplement-opencode-1/scratch/` — claim current; precision note: the string lives in the **exercise JSON**, not in `tools/check-craft-exercise.py` (no `scratch` string there) |
| 205-208 | battery "runs trusted repo scripts in a copied working directory; it is not an operating-system sandbox. Byte preservation does not prove no writes" | battery report `mirror.root` = `<lane>/.scratch/gate-battery-<id>`, `mirror.removed true`, `originals {added 0, deleted 0, modified 0, files_hashed_before/after 28, preserved true}` | current; the caveat reads exactly right — the tool's own report cannot prove absence of writes |
| 207-208 | "Copying contains the five fixture-writing legacy selftests" | `sed -n '183,189p' SKILL.md \| grep -c 'selftest rewrites own fixtures'` | 5 (phonology, lexicon, myth, costume, provenance) — current |

## 4. SCORECARD round-5 `re-run command` rows — count re-verification

The five rows' *numbers* still hold at HEAD (independent re-derivation, §5.1);
only their re-run command is stale (§2):

| SCORECARD row | claim | re-derived value |
|---|---|---|
| :33 freshness | "22 raw rows, 17 retrieved rows and five parent checks" | 22 rows, 17 `retrieved_passage: true`, `parent-source-spotchecks.json` 5 checks (5 directly relevant, 4 non-bibliographic) |
| :33 freshness | "five scoped supported / 15 unresolved" | `parent-reconciliation.json` `parent_counts {supported 5, unresolved 15, contradicted 0}`, 20 logical claims |
| :34 calibration | "13 supported / eight unresolved / one contradicted" | worker verdicts `{supported 13, unresolved 8, contradicted 1}` — the raw labels are preserved apart from the reconciled dispositions, as the row says |
| :32 operability | "seven copied-tree gate selftests pass" | `pass 7, fail 0, unevaluable 0` in both battery runs |
| :30 depth | "D2 still 20 findings" | filed receipt `d2_findings_unchanged: 20`; the number was re-derived only through the (aborted) script — the D2 packet itself is unchanged (`tools/assemble-d2.py --check` is another shard's command, not re-run here) |

## 5. Receipts

### 5.1 Commands behind the tables above

```
# all-audit append sweep (real tree, read-only; output: audits scanned 22, non-append 22)
python3 - <<'PY'
import json, subprocess
BASE = "1ccb2b7119039d8026ad1d004f20427623838b94"
rows = bad = 0
for i in range(4, 14):
    for a in json.load(open(f'corpus/lessons/round-5-sources/{i:02}.json'))['audits']:
        rows += 1
        cur = open(a['entry'], 'rb').read()
        base = subprocess.check_output(['git', 'show', f'{BASE}:{a["entry"]}'])
        if not cur.startswith(base):
            bad += 1
print('audits scanned:', rows, 'non-append:', bad)
PY
# additive-only control
git diff --numstat 1ccb2b7…HEAD -- <the 11 entries>      # N/0 for every entry
# bare battery
python3 tools/check-gate-battery.py                       # exit 2, 2 gates uncovered
# green control
python3 tools/check-gate-battery.py --baselines-root tools/gates/expected \
  --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines   # exit 0
# frozen replay
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv             # exit 2
python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv   # exit 2
# isolated round-5 acceptance
cd .scratch/f11/mirror && TMPDIR=<lane>/.scratch GIT_DIR=<lane>/.git \
  GIT_WORK_TREE=<lane>/.scratch/f11/mirror python3 reports/round-5/run-validation.py  # exit 1
```

### 5.2 Rows for `reports/round-10/drift/ledger.json` (F14 lift)

```json
[
 {"command": "python3 reports/round-5/run-validation.py",
  "source_locator": "SKILL.md:210; SCORECARD.md:30,32,33,34,35",
  "round10_verdict": "stale-documented",
  "output_sha256": "2e7d8c0ff2faabafa72e3e132526b0cef6e059b263206ba0b048b9dd91c2fd0a",
  "exit": 1,
  "evidence": "mirror .scratch/f11/mirror; receipt sha256 0a0f492a17e13f09eb644f8c60e93de1cddea1c7405ff97fe32a5b163b721da6; errors.F non-append corpus edit (22/22 audits; cause round-8 e1694ba frontmatter insertion, additive-only 0 deletions); errors.O battery expected 0 got 2",
  "causes": ["round-8 frontmatter insertion breaks append-only prefix rule (cause documented in reports/round-8/metadata/*, consequence unremarked)",
             "round-9 battery default roots omit reports/round-9/baselines (predicted in reports/round-9/baselines/battery-extension.md:239-242, integrator decision outstanding)",
             "round-8 gate repairs invalidate round-3 manifest pins (masked step, exit 2)"]},
 {"command": "python3 tools/check-gate-battery.py",
  "source_locator": "invoked by reports/round-5/run-validation.py:120; gate table SKILL.md:194 (out of shard, listed as dependency)",
  "round10_verdict": "stale-documented",
  "output_sha256": "f456f79d92a14baa0c67b4e696caf2fa7c3aa1f67c6403919af32b9db2d2d68d",
  "exit": 2,
  "evidence": "default roots tools/gates/expected + tools/gates/frozen find 5 baselines; myth-consistency-gate.py and naming-collision-gate.py uncovered; 7/7 gate selftests pass",
  "control": {"command": "python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines",
              "exit": 0, "output_sha256": "06d5ba01a495f085b4ea7ba466c40d5f15b69f3a89afb5b0af1d9d6dfab66744",
              "reading": "8 baselines pinned, 7/7 gates covered, 0 uncovered, 0 findings"}},
 {"command": "python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv",
  "source_locator": "invoked by reports/round-5/run-validation.py:158",
  "round10_verdict": "stale-documented",
  "output_sha256": "76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80",
  "exit": 2,
  "evidence": "7/7 rows gate_digest_mismatch; gate scripts last changed e1694ba (round 8)"},
 {"command": "python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv",
  "source_locator": "invoked by reports/round-5/run-validation.py:158",
  "round10_verdict": "stale-documented",
  "output_sha256": "409db5ab8b68ebc3da9a8360879db71c01e58b40ea4a8311e3818efe289c8452",
  "exit": 2,
  "evidence": "same cause as the sibling manifest"},
 {"command": "python3 tools/check-gate-battery.py --selftest",
  "source_locator": "SCORECARD.md:32 (round-5 re-run cell; command text lives in another shard)",
  "round10_verdict": "current",
  "output_sha256": "8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28",
  "exit": 0},
 {"command": "python3 tools/check-craft-exercise.py --selftest",
  "source_locator": "SCORECARD.md:32 (round-5 re-run cell; command text lives in another shard)",
  "round10_verdict": "current",
  "output_sha256": "77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32",
  "exit": 0},
 {"command": "python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json",
  "source_locator": "SCORECARD.md:30 (round-5 re-run cell; command text lives in another shard)",
  "round10_verdict": "current",
  "output_sha256": "18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650",
  "exit": 0}
]
```

## 6. Limits, and what this shard does not claim

- This shard re-runs; it does not repair. `stale-documented` rows above are
  for F15-F18. The two fixes that would restore round-5's command are (a) an
  expectation change from byte-prefix append to additive-only diff shape, and
  (b) a decision on the battery's default roots (or moving the two baselines
  under `tools/gates/`) — both touch filed or shared artifacts and neither is
  this seat's write.
- `--baselines-root` replaces rather than extends the default roots; the green
  control above needs all three roots named. Whether that is intended UX is a
  question for the O axis, recorded here only as measured behaviour.
- The masked steps (lines 121-177) were run individually, not as a sequence;
  their green readings do not prove the aborted script would have passed the
  later assertions (notably the isolated previous-acceptance copy at line 164,
  which was not re-run here because it writes a copy of the historical receipt
  into TMPDIR and belongs to the round-5 command's own contract — the filed
  receipt already records `previous_acceptance_passed: true` at round 5).
- One accidental live-tree write occurred and was restored byte-exact (§1);
  the restoration is itself the only write this seat made outside
  `.scratch/f11/` and `reports/round-10/drift/shard-11.md`.
