- Seat: X00 | connector | cross | date 2026-10-19 | baseline 4a7aede

# X00 — collision matrix: the r7 freeze vs round-35's three workstreams, and the integration order

**Mission** (`reports/round-35/targets.json`, seat X00): does `corpus/knowledge`
feed the packet read set, name any drift a freeze re-run would see, check the
renderer edit against the freeze bytes, and fix the integration order.

**Method and fences.** Every reading below is from live bytes at HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`git rev-parse HEAD`), read-only
in-tree. The only executions were non-freeze renderer modes inside an isolated
`git archive 4a7aede` copy at `.scratch/x00-iso` (renderer there hashes
`34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`, identical to
in-tree). No filed round runner was executed; no `--freeze` was run anywhere. This
seat asserts no verdict on any claim — the matrix is evidence for claims C, O, A
and for the integrator's apply order.

**Dependency status at write time** (`find reports/round-35 -name '*.md'`):
landed and cross-read — `reports/round-35/scout/K03-keyerror-path.md` (the KeyError
path), `reports/round-35/op/O08-validation-legs.md` (acceptance legs),
`reports/round-35/cross/X02-conformance.md` (conformance census). Absent —
`reports/round-35/op/O01-patch-draft.md`,
`reports/round-35/op/O02-controls.md`,
`reports/round-35/plan/P02-oa-plan.md`; the matrix does not depend on their
content (every row is content-addressed against the pinned bytes and the
renderer's constants), but row O-3 below is a binding constraint on whatever
patch they propose.

## 1. Does corpus/knowledge feed the packet read set? Yes — exactly one file, pinned three times

Partition census of `V3_READ_SET` (`tools/exercise-handoff-e2e.py:1935-1959`,
58 members; census by `importlib` load of the renderer — no `main()` executed):

| read-set surface | members |
|---|---|
| `corpus/knowledge` | **1** — `corpus/knowledge/synthesis/worldbible-integration-contract.md` (`:118`) |
| `corpus/lessons` | 4 — `corpus/lessons/round-6-sources/{03,05,09,13}.json` (`:131-136`) |
| `examples/culture-d2` | 6 (2 packets + 4 components) |
| `examples/culture-d3` | 8 |
| `examples/culture-d4` | 18 |
| `reports/round-15` / `round-18` / `round-19` / `round-34` / `round-6` | 2 / 4 / 1 / 1 / 1 |
| `tools/` | 12 (6 tools + 4 gates + 2 harness) |
| **total** | **58** |

The single corpus/knowledge member is pinned by three independent manifests, all
carrying `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`,
equal to the live file (`sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`):

1. the r7 baseline's `inputs` block and `cross_refs.contract_digest`
   (`reports/round-34/handoff/declared-in-r7/expected.json`);
2. the d3 freeze manifest, 24 members — which also pins the four round-6 ledgers
   (`examples/culture-d3/expected.json:4`);
3. the packet's own manifest row A-01
   (`reports/round-34/handoff/declared-in-r7/packet.md:39`).

A replay re-measures all 58 members every run (`:3816`), so a byte moved in any of
them raises `E2E-DIGEST` naming the file (`:3819-3823`; controls: v1 `:1774`
"tamper read-set: exit 1 E2E-DIGEST naming the changed file", v3 m12b `:4430`).
The read set is a **literal tuple, not a glob** (`:1935-1959`), so adding files to
`corpus/knowledge/` never changes membership: the 201 → 211 growth is invisible to
the renderer.

## 2. Collision matrix

| # | round-35 surface | freeze surface | collision | verdict / required action |
|---|---|---|---|---|
| C-1 | the ten new entries (culture-material +6, myth-symbol +4) | `V3_READ_SET` (58) | **none** — 0 members in either partition (census §1) | green; keep it that way |
| C-2 | any edit to `corpus/knowledge/synthesis/worldbible-integration-contract.md` | r7 `inputs` + d3 manifest + packet A-01 | digest drift, three ways | forbidden; cite the contract read-only in prose |
| C-3 | any edit to `corpus/lessons/round-6-sources/{03,05,09,13}.json` | r7 `inputs` + d3 manifest | digest drift | forbidden (also inside the filed-byte fence) |
| C-4 | `corpus/README.md` reconciliation | read set | **none** — README is not a member; documentation surfaces are excluded by design (`:1972`, `V3_BASELINE_LIMITS`) | green; the C measurement is README-internal (rows == files == totals 211, footer `21/23/24/29/20/94`) |
| C-5 | the +4 myth-symbol entries vs the 16 corpus files cited by the D2 packet | `examples/culture-d2/packet.d2.yml` **is** a pinned member (A-10, `e0f21509…`, `packet.md:48`); the files it cites are **not** | **unpinned semantic surface**: (a) renumbering/rewriting a section of a cited file silently breaks its `path#section` anchors with no digest tripping; (b) wiring a new entry into `packet.d2.yml` moves a pinned member's bytes → `E2E-DIGEST` | new entries additive-only: never touch the 16 cited files' section numbering, never edit `packet.d2.yml`. No gate validates cite anchors (no gate enumerates corpus/knowledge; `tools/gates/provenance-audit.py:344` rglobs only its path argument). Cited set: 13 myth-symbol files (`pantheon-archetypes.md` ×11, `celestial-symbolism-calendars.md` ×7, `animal-symbolism.md` ×7, `color-symbolism.md` ×6, `trickster.md` ×5, `symbolism-synthesis-method.md` ×5, `hero-journey-variants.md` ×3, `creation-myths-taxonomy.md` ×3, `cosmology-cosmography.md` ×2, `comparative-frameworks.md` ×2, `ritual-liminality.md`, `number-symbolism.md`, `myth-folktale-genres.md`), plus `corpus/knowledge/synthesis/symbolism-consistency-rules.md` and `corpus/knowledge/civilizations/{tibet,finnic-sami}.md` |
| C-6 | +10 entries vs `tools/gates/**` incl. `frozen/**` | frozen gate expectations | **none** — no gate globs corpus/knowledge; frozen expectations name corpus files only inside their own `inputs/` copies | green |
| C-7 | +10 entries vs `tools/source-audit-inventory.py` | — | none (instrument is `read_only: true`) | the 211 assertion is inventory-internal (`totals.files`, measured 201 pre-landing) |
| O-1 | the renderer patch (E2E-READSET diagnostic) | r7 freeze bytes | **none, structurally** — the renderer is **not** a read-set member; the r7 dir names it only as prose (`expected.json:101` `frozen_by`, `freeze.txt:1`, `run.log:1`, `packet.md:3`); no digest of it is pinned there | green: the patch cannot drift the freeze |
| O-2 | the same patch | filed `reports/round-34/handoff/repin.json:12` (`surface_sha256_after` == live renderer sha today) | **stale pin on the renderer surface** | file the post-patch digest as a **NEW row** — `repin.json:41-47` precedent ("earlier baselines are named superseded, never rewritten"); never edit filed bytes. Corroborated by A05/A09/A11 |
| O-3 | **growing `V3_READ_SET` as a fix strategy** | r7 default chain | **hard break, two legs**: (a) `:3657-3658` `if checked != len(V3_READ_SET): raise Failed("E2E-COUNT", …)` against `packet.md:35` "58 read-set files plus one inline-payload row" (59 manifest rows measured: 58 `A-*` + `A-GLOSS`); (b) `:3389-3391` accepts a claim link only if it names a `set(V3_READ_SET)` member (`E2E-LINK`) | **FORBIDDEN.** The fix must be resolution-side only, at the diagnostic `:3819-3823`. Re-adding `reports/round-20/handoff/claims-map.md` to the read set would break the r7 row it must keep green |
| O-4 | non-freeze renderer runs | r7 dir bytes | **none, measured**: in the isolated copy the r7 dir's five tracked digests are identical after the failing r6 replay *and* after the green default chain, and equal to live == the `repin.json` pins | safe, but the fence stands: no `--freeze` against declared-in-r7; prefer isolated copies (F-C13-1). `run.log` is gitignored (`.gitignore:3`), so an isolated `git archive` copy holds **5 files, not 6** — scope "freeze bytes" to the five tracked files |
| O-5 | `claims.json`'s O counting command (`… --selftest`, no profile flag) | the new controls | **measurement trap**: `:4485` defaults `--profile v1`; `:4525` bare `--selftest` runs `v1_selftest` (21 read-set files, 17 controls, green pre-patch and post-patch regardless of the patch) | the leg must be `--profile v3 --selftest` (`:4526-4527`): pre-patch exit 0, header "plus 39 controls:", 40 `  - ` lines (measured in isolation). Reconcile with O08 §2 O2 |
| O-6 | the patch's selftest fixtures | freeze bytes | none — fixtures are tempdir copies (`tools/exercise-handoff-e2e.py:4147-4152` `v3_freezed_copy`) | green |
| A-1 | A-block audits | the pinned surfaces above | n/a | A01/A02 should read O-2 (the repin stale-pin) and C-5 (the unpinned cite-anchor surface) into their verdicts |

## 3. Replayability census of every filed v3 baseline — the class, not the instance

Census by `importlib` load of the renderer (`V3_READ_SET` / `V1_READ_SET`) against
each filed baseline's `inputs` block:

| filed baseline | members | unresolvable in the live read set |
|---|---|---|
| `reports/round-22/handoff/declared-in` | 58 | `reports/round-20/handoff/claims-map.md` |
| `reports/round-22/handoff/declared-in-r2` | 58 | same |
| `reports/round-26/handoff/declared-in-r5` | 58 | same |
| `reports/round-28/pinsweep/v3-baseline-r28` | 58 | same |
| `reports/round-30/handoff/declared-in-r6` | 58 | same |
| `reports/round-34/handoff/declared-in-r7` | 58 | **none** (the only clean row) |
| `reports/round-23/wording/declared-in-r3`, `reports/round-25/v3-supersession/declared-in-r4` | — | not read-set baselines: declaration documents (`kind`/`delta`/`binding`/`parent`/`revision`; no `inputs`) |

⇒ **five** filed rows carry the R34-N1 class, all with the same single member (the
set difference is exactly one member each way; 57 shared). The fix must therefore
be class-level, and the acceptance leg should sample ≥ 2 rows (e.g.
`declared-in-r6` and `v3-baseline-r28`) to prove the class rather than the
instance. K03 §1/O08 §1 established the instance; this census establishes the
extent.

## 4. Integration order (binding sequence)

1. **Freeze fence first.** Never re-freeze or edit `declared-in-r7` or
   `declared-in-r6`; run every renderer leg in an isolated copy (F-C13-1). The
   five tracked r7 digests must equal live == `repin.json` pins at close (O08 O4).
2. **Renderer patch before any round-35 artifact that digests the renderer** (O-2):
   the post-patch digest is what the receipt must carry. Then, in this order:
   default chain exit 0 with `packet_sha256=45f57132…` (O-3 keeps the r7 row
   green); `--profile v3 --selftest` exit 0 with ≥ 41 controls (O-5); the five
   freeze digests unmoved; `run.log` before/after equal.
3. **Corpus entries: apply all ten as one landing.** The C measurement is a
   whole-corpus census, so a partial landing makes the README sweep red by
   construction — that is mid-apply state, not a defect. During the landing,
   honour C-2, C-3 and C-5: never touch the contract, the four round-6 ledgers, or
   the sixteen files cited by `packet.d2.yml`; never edit `packet.d2.yml`.
4. **README reconciliation last within the C block**, then the inventory total:
   rows == files == totals 211, footer `21/23/24/29/20/94`,
   `tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
   → `totals.files 211`.
5. **Only then the round's validator** (`reports/round-35/run-validation.py`,
   absent at write time), executed from an isolated copy, with the robust entry
   discovery form untracked ∪ added-vs-baseline (X02-F2: never `git status`-only).
6. **Close-time cross-checks:** O08 O4 against my O-1…O-6 rows; A01/A02 against
   O-2; X02 §2's F-C13-1 check.

## 5. Limits and to-verify

- The patch's exact wording, exit code and control count are O01/O02's to fix;
  every row above is content-addressed and unaffected by wording drift.
- `to-verify`: whether any *filed* artifact outside `repin.json:12` pins the
  renderer's pre-patch digest. A grep for the `34c85f5773fb1925` prefix over
  `reports/`, `SCORECARD.md`, `LOG.md`, `SKILL.md`, `AGENTS.md` returned only
  `repin.json:12` plus round-35 fragments (A05/A09/A11, O08, S02, C16) — no filed
  round artifact beyond repin.json. Rounds 1–29 were covered by the same grep
  (whole `reports/` tree), so the reading stands; the residual uncertainty is
  prose-embedded digests in truncated or wrapped form, which a prefix grep cannot
  see.
- `to-verify`: the C-5 cited-file list was read from `examples/culture-d2/packet.d2.yml`
  cite fields by regex; a citation naming a corpus file without the
  `corpus/knowledge/` prefix would be missed.

## Owed

- `reports/round-35/op/O01-patch-draft.md`, `reports/round-35/op/O02-controls.md`
  — absent at write time. Not blocking this matrix, but the landed patch must
  satisfy row O-3 (no `V3_READ_SET` growth, no re-freeze) and the verifier should
  reconcile the landed control count with row O-5.
- `reports/round-35/plan/P02-oa-plan.md` — absent; if it proposes a read-set
  membership change as the R34-N1 fix, row O-3 refuses it.

## Citations

Paths and lines relied on (all resolve at HEAD `4a7aede` unless stated):

- `tools/exercise-handoff-e2e.py:118` (`CONTRACT`), `:131-136` (`SOURCE_LEDGERS`),
  `:184` (`CLAIMS_MAP` → declared-in-r7), `:1933-1934` (v3 baseline/frozen-dir
  defaults), `:1935-1959` (`V3_READ_SET`, 58 members), `:1972`
  (`V3_BASELINE_LIMITS`, "documentation surfaces excluded"), `:3389-3391`
  (`E2E-LINK` against `set(V3_READ_SET)`), `:3657-3658` (`E2E-COUNT` manifest
  count leg), `:3816` (read-set snapshot), `:3819-3823` (drift detection,
  diagnostic, designed raise), `:4149-4154` (`v3_freezed_copy`), `:4430` (m12b),
  `:4485` (`--profile` default v1), `:4525-4527` (`--selftest` dispatch v1/v3)
- `reports/round-34/handoff/declared-in-r7/expected.json` (`inputs` = 58,
  `cross_refs.contract_digest` = `5f4c02bf…`), `packet.md:33-39` (manifest intro
  "58 read-set files plus one inline-payload row"; A-01), `:48` (A-10
  `packet.d2.yml`), `:95` (A-57), `:96` (A-58), `freeze.txt:1`, `run.log:1`,
  `reports/round-34/handoff/repin.json:12` (renderer `surface_sha256_after`),
  `:41-47` (history/precedent row)
- `examples/culture-d3/expected.json:4` (contract digest in the d3 manifest, 24
  members)
- `examples/culture-d2/packet.d2.yml` (`cite:` fields, e.g. `:1103`)
- `reports/round-30/handoff/declared-in-r6/expected.json` (`inputs` = 58, pins
  `reports/round-20/handoff/claims-map.md`)
- `reports/round-22/handoff/declared-in{,r2}/expected.json`,
  `reports/round-26/handoff/declared-in-r5/expected.json`,
  `reports/round-28/pinsweep/v3-baseline-r28/expected.json`,
  `reports/round-23/wording/declared-in-r3/expected.json`,
  `reports/round-25/v3-supersession/declared-in-r4/expected.json` (census §3)
- `.gitignore:3` (`*.log`)
- `reports/round-35/targets.json` (seat X00), `reports/round-35/claims.json`
  (claims C/O/A, non-goals), `reports/round-35/scout/K03-keyerror-path.md`,
  `reports/round-35/op/O08-validation-legs.md`, `reports/round-35/cross/X02-conformance.md`
- `tools/gates/provenance-audit.py:344` (rglobs its path argument only);
  `tools/source-audit-inventory.py` (`read_only: true`, default root
  `corpus/knowledge`)

Commands run (all read-only in-tree unless marked isolated):

- `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`;
  `git ls-files reports/round-34/handoff/declared-in-r7/` → 5 tracked files;
  `git check-ignore -v …/run.log` → `.gitignore:3 *.log`
- `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` →
  `5f4c02bf…` == the three pinned copies; `sha256sum tools/exercise-handoff-e2e.py`
  → `34c85f57…`
- `importlib` census of `V3_READ_SET`/`V1_READ_SET` and per-baseline
  `inputs`-vs-live set difference (§1, §3 tables) — no `main()` executed
- `for p in linguistics myth-symbol culture-material synthesis verification
  civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` →
  `21/19/18/29/20/94` = 201
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → `totals.files 201`, `read_only: true`
- `grep -c "^| A-" reports/round-34/handoff/declared-in-r7/packet.md` → 59 (58 + A-GLOSS)
- `grep -rn "34c85f5773fb1925" reports/ SCORECARD.md LOG.md SKILL.md AGENTS.md`
  → `reports/round-34/handoff/repin.json:12` + round-35 fragments only
- `grep -rn "rglob|\.glob\(|os.walk|iterdir" tools/*.py tools/gates/*.py
  tools/harness/*.py` → no gate enumerates `corpus/knowledge`
- **Isolated** (`.scratch/x00-iso`, `git archive 4a7aede | tar -x`, TMPDIR
  `.scratch`):
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`
  → exit 1, `KeyError: 'reports/round-20/handoff/claims-map.md'` at `:3822`;
  `… --profile v3 --quiet` → exit 0,
  `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`;
  `… --selftest` → exit 0, 17 controls (v1);
  `… --profile v3 --selftest` → exit 0, "plus 39 controls:", 40 `  - ` lines;
  `sha256sum` of the r7 dir before/after those runs → the five tracked digests
  unchanged and equal to live
