# ScoutR78Truth — round-78 census S884 mismatch (read-only recon)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base `44f76d456c1b326a71ffdb381590af825cbf11be` (detached HEAD, `git rev-parse --show-toplevel` confirmed). Round-78 census commit `4b255745dea45a45d88b17e3c3fea4cdb6700cf7`. No live registry, receipt, or knowledge file was altered. No build, lint, test, or subagent was run. No tool was installed.

## Verdict

- **Exact count of the named S884 mismatch: 1.** It is one receipt line, `reports/round-78/telemetry/census-end.txt:33`, whose used-by token differs from the registry.
- The start receipt and end receipt differ on exactly one line (`diff` of the two committed blobs: line 33 only). That line is the S884 line.
- The mismatch is in the census-end receipt, not the registry. The registry carries `amend-2026-10-23.md` at both `4b255745` and base `44f76d45`, and in the live worktree.
- **Provenance of the census-end receipt is UNKNOWN.** The bytes do not establish which working-tree state produced line 33. Details below.

## Original digests and tokens

| artifact (committed at `4b255745`) | git blob | sha256 | S884 used-by token |
|---|---|---|---|
| `reports/round-78/telemetry/census-start.txt` (35 lines) | `770e5ebbd9465a34c2abd7b00015c04e6af5485f` | `8f753788f4f86556b62701b2d5155435f330f64686b4a11367aa41c53bad0461` | `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` (line 33) |
| `reports/round-78/telemetry/census-end.txt` (35 lines) | `62eb55b77f44bf47c283c98c5645dd7141e98495` | `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867` | `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` (line 33) |
| `corpus/SOURCES.md` at `4b255745` (and at base `44f76d45`, same blob) | `c28330a37535223939ea5820af50d8d8595ed059` | `51b18f1c98996056287e0eae4d24cd682b3d756fe898e50f7356cbf680af8301` | S884 row, line 839, used-by cell = `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` |

- Census-end receipt sha256 (original bytes): `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`. Its git blob is `62eb55b…`, which is also the census-end blob at base `44f76d45`.
- Both receipts' command line: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`, exit 0. Both end with `kotodama ok …/kotodama-shokunin/corpus/SOURCES.md`.
- Receipts carry **no** revision, tree hash, timestamp, or counter sha. The "recorded round-78 revision" is therefore the commit that adds them (`4b255745`), not something the receipt states.
- The S884 row is 11 fields; the used-by cell is the last field.

## Searches performed

- `git rev-list --all -- corpus/SOURCES.md`: 219 commits. The S884 row's used-by token across them: 19 commits carry `…worldbuilding-setting-practice.amend-2026-10-23.md`, 200 commits have no S884 row, **0 commits carry `…amend-2026-10-24-r13.md`**.
- `git log --all -- corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`: no commit. That file has never existed in any ref in this lane.
- `git status --porcelain -- corpus/SOURCES.md reports/round-78`: clean. The worktree (detached at `44f76d45`) has S884 = `…amend-2026-10-23.md`.
- The census-end blob is identical in `4b255745`, `13e5a84e` and `a2ff2913`. The latter two are duplicate-tree jj commits (different authors, same parent `6f119326`). These are not independent evidence.
- Fleet-wide grep for `worldbuilding-setting-practice.amend-2026-10-24`:
  - `reports/round-78/telemetry/census-end.txt:33` (the receipt).
  - `corpus/lessons/round-78-verifier-spotcheck.md:67` (routed defect 2, quoting the token).
  - Fleet-root `.ufo/reports/round-78/kotodama.md` lines 72 and 110. These are two embedded `text` blocks (lines 41–75 and 79–113). Both match the census-end body byte-for-byte after the Command/Exit header; neither matches census-start. Line 9 of that report says start and end "produced the same warnings", which holds for the warning set, not for line 33.
  - `reports/round-79/telemetry/baseline-census-mismatch.json` (untracked, not mine; not relied on). It records `mismatches: 1` with the same two tokens.
  - No file exists at the `…24-r13.md` path anywhere on disk.

## Provenance (unknown; not established)

- The receipt validates the **working tree** via `--root`, not a committed revision, and records no stamp. Which bytes the worktree held at capture time is not recoverable from the receipt.
- The verifier's "uncommitted/regressed working-tree state at capture time" (routed defect 2) is an inference. Nothing observed confirms it: no committed SOURCES state has the token, no on-disk SOURCES copy has it, and the current worktree is clean.
- [INFERENCE, unverified] The token shares the naming pattern of `heritage-taxonomy-models.amend-2026-10-24-r13.md`, which exists at base and is cited in `SOURCES.md` S874 and `heritage-taxonomy-models.md:76`. A cross-row substitution at capture time is one hypothesis; nothing here tests it.
- A correction can bind the observed facts (original digest, old token, actual token, measured revision) without asserting cause.

## For Ca / correction (inputs, not a design)

- Mismatch count at the recorded revision `4b255745` (and base `44f76d45`, identical registry blob): **1**.
- After a correction is appended: the census-end receipt bytes must remain unchanged (append-only), and the correction must name original digest `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`, old token `…amend-2026-10-24-r13.md`, actual token `…amend-2026-10-23.md`, and the measured revision it asserts.
- Any correction that names a revision other than `4b255745` (or base `44f76d45`, which carries the same registry blob) must state the revision it measured and show that revision's bytes.

## Evidence files

Copied to `.ufo/waves/round-79/w1/stage/ScoutR78Truth/` (sha256 in `SHA256SUMS.txt`):
- `census-start.4b255745.txt`, `census-end.4b255745.txt` (committed bytes via `git show 4b255745:…`)
- `registry-S884-row.4b255745.txt` (SOURCES.md line 839)
- `report-embedded-block-a.round78-kotodama.md.txt`, `report-embedded-block-b.round78-kotodama.md.txt` (fleet-root report extracts, read-only)

Scratch `/fast/scratch/hyaku/kotodama-r79/ScoutR78Truth/` was removed after copying.

## Limits

- Not run: `sources-census.sh` (kept to read-only reads). The verifier's re-run and the sibling's JSON are cited, not re-derived.
- The receipt has no timestamp, so "when" is not recoverable.
- The jj duplicate commits share one census blob; they do not add an independent capture.

Report: .ufo/waves/round-79/w1/ScoutR78Truth.md
