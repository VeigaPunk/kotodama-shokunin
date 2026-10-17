# R8-D09 — boundary tests: empty labels, mixed-script labels, unknown rank values

- round: 8 (loop 1 of 3, build round 1 of 4) · date: 2026-10-17 · shard: R8-D09
  (test shard of claim D / `d2-typed-labels`; assignment in
  `reports/round-8/targets.json` under `R8-D06..D11`)
- requirement under test (verbatim from the assignment): "boundary cases:
  empty labels, mixed-script labels, unknown rank values; stable exit-2
  diagnostics, no tracebacks"
- target: `tools/d2-typed-labels.py` (owned by shard R8-D02)
- **tested revision: `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03`**
  (settled at `2026-10-17T20:25:16Z` after four consecutive stable 30-s hash
  samples). The file was under active edit by D02 for the whole window — the
  full revision record is §2; all verdicts in §3–§5 belong to that one
  revision and are **`to-verify` for any later revision**.
- owns: this file only. Scratch trees live outside the lane
  (`/home/vgpnk/d09-scratch/`, removed before this shard closed) and no lane
  file other than this one is written. The lane tree is read-only here.
- status: complete for the tested revision; the post-integration revisions
  observed at `20:25:54Z`–`20:27Z` (new CLI `--packet/--json/--emit`) were
  mid-edit and tracebacking on minimal inputs at observation time, so their
  boundary behavior is `to-verify` (§6).

## 1. Method

Harness (scratch, outside the lane): a mirror tree
`/home/vgpnk/d09-scratch/repo/` carrying the tool, the costume gate, the D2
packet and the four components the tool reads (`05-lexicon.yml`,
`09-eras-calendar.yml`, `11-costumes.yml`, `12-rank-rules.yml`). For each case
the harness restored pristine components, applied exactly one mutation,
re-synced the tool from the lane, and ran it in `--report` mode (read-only —
it prints findings and writes nothing). Per run it recorded: exit code, first
stderr line, first stdout line, and whether `Traceback (most recent call last)`
appears in stderr. The mixed-script cases were additionally run in default
(build) mode to check what reaches the artifact, and the costume gate was run
on that artifact.

Environment notes, disclosed because they shape the receipts:

- `/tmp` is a shared tmpfs that hit **inode exhaustion** during this window
  (`df -i /tmp` → `1048576 1048576 0 100%`, observed `20:21Z`; one fixture
  write failed `OSError: [Errno 28] No space left on device` while `df -h`
  still showed 8.3G free). All scratch and `TMPDIR` work for this shard was
  therefore moved under `/home/vgpnk/d09-scratch/`. This also affects the
  tool's own `--selftest`, which builds fixtures with
  `tempfile.TemporaryDirectory()`: it can only run when `TMPDIR` points at a
  filesystem with free inodes. Every `--selftest` receipt below was taken
  with `TMPDIR=/home/vgpnk/d09-scratch/tmp`.
- The lane worktree was being edited by sibling shards during the whole
  window (dirty `tools/gates/phonology-sanity-gate.py`, untracked
  `tools/harness/`, `reports/round-8/operability/`, and the D02 tool itself).
  Every receipt names its observation time; a re-run after integration may
  legitimately differ.

## 2. Target revision record (moving target, pinned by sha256)

| observed (UTC) | sha256 (first 12) | behavior observed | where |
|---|---|---|---|
| 20:19:59 | `080a3b2f2753` | first revision on disk; `--selftest` **26/30, exit 1** (four failures, §4-F4) | lane tree |
| 20:21:09 | `429191fd14e0` | `--selftest` aborts: `TypeError: eras_of() missing 1 required positional argument: 'tag_space'` — **traceback** | scratch mirror |
| 20:21:38 | `a0f866ada22c` | `--report` and `--check` both **traceback**, exit 1 (`TypeError: adapt_rules() missing 1 required positional argument: 'tag_space'`, `build_artifact` line 1004) | lane tree |
| 20:22:16–20:22:46 | `37060dd19dc8`, `1756e8c0504e` | `--report` functional again; still editing | lane tree |
| 20:23:16–20:25:16 | `623b5b1f2f9f` | **stable ×4 samples**; `--selftest` 32/32 exit 0; `--check` byte-identical exit 0; full boundary matrix (§3) | lane + scratch |
| 20:25:54 | `56c0db1423f2` | post-integration rewrite (119 KB, 2331 lines); CLI changed | lane tree |
| 20:26–20:27 | `f0110e391d47`, `5d87d34683d6` | new CLI `--packet/--json/--emit`; minimal fixture packets **traceback** at observation time (mid-integration) | lane tree |

The 20:21 tracebacks and the 080a3b2f selftest failures are retained here as
the failure modes this boundary suite exists to catch; they are **not**
verdicts against the final tool. All §3–§5 receipts were taken at `623b5b1f…`,
re-synced into the mirror immediately before the run.

## 3. Boundary matrix — tested revision `623b5b1f…`

One mutation per row against the pristine D2 components; command
`python3 tools/d2-typed-labels.py --report` in the mirror (read-only). All
rows: **no traceback**. Diagnostics are the verbatim first stderr line.

### 3.1 Empty labels

| case | mutation (file, field) | exit | diagnostic |
|---|---|---:|---|
| A1 | `05-lexicon.yml`, L-01 `term: ir` → `term: ""` | **2** | `d2-typed-labels error: label text must be a non-empty string` |
| A2 | `11-costumes.yml`, form slot LEX-GAR-01 `form: "(to-verify)"` → `form: ""` | **2** | `d2-typed-labels error: form_slots[LEX-GAR-01]: no form declared` |
| A3 | `11-costumes.yml`, GAR-01 `garment` → `garment: ""` | **2** | `d2-typed-labels error: label text must be a non-empty string` |
| A4 | `12-rank-rules.yml`, DEG-1 required-term `gloss` → `gloss: ""` | **2** | `d2-typed-labels error: label text must be a non-empty string` |
| A5 | `11-costumes.yml`, GAR-01 `garment` → `garment: "(translated label)"` (annotation with no body) | **2** | `d2-typed-labels error: label annotation without a label body: '(translated label)'` |

Repeat-stability (same mutation run twice, stderr compared byte-for-byte):
A1, A5 identical across runs (`stable: true` in the harness record). A2–A4
share the single `Malformed → exit 2` path in `main()`; no nondeterminism
source is visible in that path.

### 3.2 Mixed-script labels

| case | mutation | exit | finding? | artifact propagation (default build) |
|---|---|---:|---|---|
| B1 | `05-lexicon.yml`, L-01 `term` → `羊毛外套` (CJK) | **0** | none referencing L-01 | CJK string present verbatim in `typed-labels.d2.yml`; gate on the artifact **exit 0**, no `G-DATA` |
| B2 | `05-lexicon.yml`, L-08 `term` → `mi<U+200B>r` (zero-width space) | **0** | none referencing L-08 | ZWSP string present verbatim in the artifact; gate **exit 0**, no `G-DATA` |
| B3 | `11-costumes.yml`, GAR-01 `garment` → `羊毛外套 (translated label)` | **0** | none | typed as a translated label (by design: translations are never graded on the sound channel — `SKILL.md:186`) |
| B4 | `05-lexicon.yml`, L-26 `term` → `羊毛外套 (translated label)` | **0** | none | typed by its inline annotation |

B3 is the intended control (a translated label may be any script). B1/B2 are
the finding: a **native-form** label whose text is CJK or carries a
control/format character is typed and passed with exit 0 and no finding, the
string reaches the projection verbatim, and the gate run on the projection is
clean. See §4-F1 for the boundary-contract question this raises.

### 3.3 Unknown rank values

| case | mutation (`11-costumes.yml`, GAR-01 `wearer_rank`) | exit | observed |
|---|---|---:|---|
| C1 | `"warlord"` (no `WI-` id) | **0** | `FINDING PR-01: [hold] costume GAR-01: wearer rank unresolved (the wearer prose names no WI- id, so the rank cannot be resolved to the shared vocabulary); entitlement checks cannot be run for this row` |
| C2 | `"herder household (WI-99)"` (unknown institution id) | **2** | `d2-typed-labels error: costumes[GAR-01]: unknown institution id(s) WI-99` |
| C3 | `""` | **0** | `FINDING PR-01: [hold] costume GAR-01: wearer rank unresolved (no wearer_rank declared); …` |
| C4 | `3` (bare numeric scalar) | **0** | `FINDING PR-01: [hold] costume GAR-01: wearer rank unresolved (no wearer_rank declared); …` |
| C5 | `true` (bare boolean scalar) | **0** | `FINDING PR-01: [hold] costume GAR-01: wearer rank unresolved (no wearer_rank declared); …` |

C2 repeat-stable (identical stderr across runs). C1/C3–C5 are surfaced as
holds (never silently dropped) but exit 0; C4/C5 are reported as "no
wearer_rank declared" although a value *was* declared — see §4-F2/F3.

### 3.4 Pristine control and the tool's own selftest at `623b5b1f…`

- Pristine mirror, `--report`: **exit 0**, no traceback; first line
  `FINDING TL-01: [hold] form slot LEX-GAR-01 carries no native form ('(to-verify)'); …`
  The coverage line below was observed on the same components at
  `1756e8c0504e` (lane tree, `20:22:51Z`) and is `to-verify` for
  `623b5b1f…`, where only the first line was captured: `labels_total=94`,
  `labels_by_kind={"borrowed-strata": 2, "descriptive-gloss": 16,
  "fictional-coordinate": 9, "native-form": 48, "translated-label": 19}`,
  `labels_unresolved=26`, `prose_rules_total=21`, `rank_rules_executable=3`,
  `rank_rules_held=18`, `costume_rows=10`, `costume_rows_rank_resolved=7`,
  `era_rows=7`, `era_rows_held=4`.
- Lane tree, `python3 tools/d2-typed-labels.py --selftest` (with scratch
  `TMPDIR`): `selftest: 32/32 checks passed — fixture CLI build/--check/tamper
  plus malformed span, unclassified rule, unreadable maps_to, unknown
  institution, label-parser and reconciliation-refusal controls; no file
  outside the temporary directory touched`, **exit 0**.
- Lane tree, `python3 tools/d2-typed-labels.py --check`: `typed-labels.d2.yml:
  byte-identical deterministic build`, **exit 0**; artifact sha256
  `820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778`.

## 4. Findings for the D reviewers / orchestrator (reported, not absorbed)

- **F1 — mixed-script native forms pass un-screened (B1/B2).** The tool types
  them and passes (exit 0, no finding); the CJK / ZWSP string survives into
  `typed-labels.d2.yml` verbatim; the costume gate on the artifact is clean
  (`exit 0`, no `G-DATA`). Nothing in the typed-labels pipeline screens a
  native form's script or control/format characters, and the projection does
  not expose the lexicon forms to the naming gate (which, on the assembled
  packet, does catch exactly these: §5). Whether the boundary contract
  requires refusal here is a design decision above this shard — if it does,
  the requirement "stable exit-2 diagnostics" is **not met for the
  mixed-script class**; if typing-only is intended, the screen belongs
  downstream and is currently missing there.
- **F2 — numeric/boolean rank scalars are diagnosed as absent (C4/C5).** The
  message is `no wearer_rank declared`, but a value *was* declared; the loader
  evidently types bare scalars away from `str` and `resolve_wearer`'s first
  guard (`not isinstance(prose, str)`) reports it as absence. No traceback,
  stable, surfaced as a hold — a diagnostic-precision gap, not a crash.
- **F3 — unknown-rank *words* and empty ranks exit 0 (C1/C3–C5).** The hold is
  visible in stdout findings, but a caller keying only on the exit code sees
  "clean". Contrast C2, where an unknown `WI-` id is a hard exit 2. Both
  behaviors may be intended (hold = un-evaluated, not a pass, per the tool
  docstring); recorded so the claim's "stable exit-2 diagnostics" wording is
  read against what actually exits 2.
- **F4 — docstring vs selftest divergence observed at `080a3b2f…` (fixed by
  `623b5b1f…`; verify on the final revision).** At `080a3b2f…` the docstring
  claimed the selftest covers "duplicate ids, missing blocks, empty label
  sets, unknown rank", while the shipped selftest had 26 checks and four
  failures, including `malformed: unknown institution id refused` (observed
  exit 0 — reproduced independently here as C2) and
  `parser: malformed '(translated label)' refused` (observed no error —
  reproduced here as A5). At `623b5b1f…` the selftest is 32/32 and C2/A5 both
  refuse with exit 2, so both earlier failures were repaired; whether the four
  docstring-named control classes exist by name on the final revision is
  `to-verify` (§6), since the docstring and CLI were rewritten at
  `20:25:54Z`.

## 5. Substrate baseline — the same boundary classes through the legacy gates

Context only (the typed-labels tool types labels; these gates grade names).
Minimal packets (`/home/vgpnk/d09-scratch/probes/*.yml`, one `names` record
plus a declared phonology and one era), command
`python3 tools/gates/naming-collision-gate.py <file>`, observed
`2026-10-17T20:26Z`:

| case | exit | first diagnostic |
|---|---:|---|
| empty name (`""`) | 1 | `FINDING NAME-INVENTORY: HOLD — names[1] has no usable 'name'; skipped` |
| whitespace name (`"   "`) | 1 | same as empty |
| CJK name (`羊毛外套`) | 1 | `FINDING PHON-INVENTORY: FAIL — name NM-01 '羊毛外套': symbol /羊/ at position 1 is not in the declared inventory …` |
| ZWSP name (`mi<U+200B>r`) | 1 | `FINDING NAME-SCRIPT: REVIEW — name use NM-01 'mi\u200br' contains control/format characters; flag for inspection, do not delete indiscriminately` + `PHON-INVENTORY: FAIL` |
| Arabic name (`عباءة`) | 1 | `FINDING PHON-INVENTORY: FAIL — name NM-01 'عباءة': symbol /ع/ …` |

No tracebacks in any row; malformed *packets* (missing `eras`, missing
phonology, missing top-level `name`) exit 2 with a `FINDING G-DATA:
[could-not-evaluate] …` line on stdout. So the substrate already refuses
empty/mixed-script/format-character names with stable diagnostics — the gap
F1 describes is that the new tool's projection never routes native forms
into that channel.

## 6. Limits and to-verify

1. **Post-integration revisions untested.** At `20:25:54Z` D02 rewrote the
   tool (new CLI `--packet/--json/--emit`, `--report` removed) and at
   `20:26–20:27Z` the new revisions were tracebacking on minimal fixture
   packets while still being edited. Re-run this report's matrix against the
   settled revision; the mirror harness logic is fully specified by §3's
   mutation table (one field per row, `--report` at `623b5b1f…`; for the new
   CLI use `--json`/default report mode instead).
2. **F1's contract question is not decided here** (refusal vs typing-only for
   mixed-script native forms); canon/contract calls belong to the parent.
3. **F4's final-revision check** (docstring-named selftest classes:
   duplicate ids, missing blocks, empty label sets, unknown rank) is
   `to-verify` on the settled tool.
4. **Cross-shard context, not mine to fix:** D15's `docs.md` §2.4 records
   `replay-frozen.py` fail-closed (1/7 rows) due to the concurrent O-shard
   phonology-gate repair; D17's `findings-17.md` derives two label-typing
   cases whose Part 2 (tool run) was unrun when filed.
5. **Scratch removed:** `/home/vgpnk/d09-scratch/` (mirror tree, harnesses,
   probes, boundary JSON) was deleted at shard close; the mutation table in §3
   is the durable reproduction recipe. `/tmp` inode exhaustion (§1) is a
   shared-host condition and is reported, not repaired.
6. **Polling record:** tool path polled every 60 s from `20:12Z` (landed
   `20:19:59Z`); hash sampled every 30 s `20:21:46–20:25:16Z` (settled
   `623b5b1f…`); second stability poll started `20:27Z` on the
   post-integration revision; the tool was still moving when this file was
   finalized, so §2's table is the authoritative revision record.

FILES: reports/round-8/depth/test-boundary.md | SUMMARY: D09 boundary tests — on the last stable revision `623b5b1f…` (selftest 32/32, `--check` byte-identical) empty labels refuse with stable exit-2 diagnostics and no tracebacks (5/5 cases), unknown institution id refuses (exit 2) while unknown-rank words/empty/numeric/boolean surface as PR-01 holds (exit 0), and mixed-script native forms (CJK, ZWSP) pass un-screened into the artifact with a clean gate run — flagged; D02 rewrote the tool mid-window (new `--packet/--json/--emit` CLI, tracebacks observed mid-edit), so post-integration boundary behavior is `to-verify`.
