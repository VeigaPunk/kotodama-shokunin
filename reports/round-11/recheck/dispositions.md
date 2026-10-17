# R11-F09..F10 — drift disposition for every unstable recheck row

- seat: R11-F09..F10 (freshness drift disposition). Assignment: for every
  unstable row of the round-11 recheck, name the cause with evidence
  (legitimate change / environmental / defect). This file is the seat's only
  write; no ledger row, receipt, filed report, tool or fixture byte was
  modified by it.
- date: 2026-10-17 · lane: `kotodama-shokunin` · HEAD
  `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`
- measurement window: 19:05–19:16 local (22:05–22:16Z). The receipts were
  frozen at set digest
  `86b55e921604b5a5aa64d5afb42d36959f766dc0da003fec40e5df908cda80d3`
  (sha256 of the sorted per-file sha256 list over the 192 receipts); this
  disposition binds to that snapshot. `reports/round-10/drift/ledger.json`
  sha256 `9ae5ed2ee5599629cfb331d85fd5028a87c63e41b58d36c65b3a74a1c770b698`.
- method: each unstable row was re-run or re-derived by this seat in two
  disposable mirrors — `.scratch/r11f09/iso` (full tree, no `.git`) and
  `.scratch/r11f09/iso-full` (same tree plus a copy of `.git` at HEAD) — plus
  read-only lane-root runs; `export TMPDIR=$PWD/.scratch` throughout. Where a
  clean state was needed the mirror (never the lane tree) was restored with
  `git checkout -- .`. The live tree was not written by this seat.
- taxonomy, stated so the labels are unambiguous:
  - **legitimate change** — the surface the command measures moved because of
    a documented lane change (`94ca098` round-10 admit, `.gitignore` edit,
    concurrent round-11 writes); the pin was true when recorded.
  - **environmental** — the recorded bytes are not a function of the measured
    surface alone (embedded random tokens, wall-clock, absolute paths, live
    worktree snapshots) or the recorded input is uncommitted scratch that no
    longer exists; no lane artifact is stale or broken.
  - **defect** — the ledger row itself is defective: the recorded command text
    is not what produced the pin, the row stores prose/an artifact digest
    instead of a command output, or the pin names an artifact that is not in
    the repository.

## 1. Result

- 149 of 192 rechecked rows are hash-stable, 43 are unstable (77.60% raw).
  Count from `python3` over the 192 receipts' `stable` field, 2026-10-17
  22:14Z.
- All 43 unstable rows are dispositioned below; zero remain unexplained.
  Tally in this seat's taxonomy: **15 legitimate change, 21 environmental,
  7 defect**.
- The F claim needs ≥95% hash-stable. 95% of 192 allows at most 9 unstable
  rows; this ledger produced 43. Excluding the 21 environmental rows from the
  denominator (they are not byte-recheckable by construction) gives
  149/171 = 87.1%; excluding the 7 defect rows as well gives 149/164 = 90.9%.
  The ≥95% bar is not reachable against this pin set as recorded — flagged for
  the F-claim verifier, not decided here.

## 2. Dispositions

### Legitimate change — 15 rows

- **row 2** `sha256sum SKILL.md` — `fb9212da…` → `fb3dd9a4…` (exit 0,0).
  `94ca098` (round-10 admit, 2026-10-17 18:57:36 -0300) moved SKILL.md
  `2bce468d…` → `52d5f4d1…`; the pin was taken at `e3a1ec9` (`2bce468d…`).
  Verified: `git show e3a1ec9:SKILL.md` = `2bce468d…`, `HEAD:SKILL.md` =
  `52d5f4d1…`, and the sha256 of the `sha256sum SKILL.md` stdout line for
  `52d5f4d1…` is exactly `fb3dd9a4…` (both output hashes re-derived).
  Receipt `row-002.json`.
- **row 4** `git diff --stat e1694bad..HEAD -- SKILL.md` — empty
  (`e3b0c442…`) → `72a6f532…` (0,0). Same commit: at `e3a1ec9`
  `e1694ba:SKILL.md` = `2bce468d…` equals the then-worktree file (empty
  diff); after `94ca098` the diff reads `SKILL.md | 48 +-` (31 insertions,
  17 deletions).
  Verified by re-run (hash equals the receipt). Receipt `row-004.json`.
- **row 5** `git log -1 --format='%H %ad %s' --date=short -- SKILL.md` —
  `3789dbc4…` → `3fc9b521…` (0,0). The newest commit touching SKILL.md is now
  `94ca098`. Verified by re-run (byte-equal). Receipt `row-005.json`.
- **row 39** partition counts over `corpus/knowledge/{linguistics,myth-symbol,
  culture-material,synthesis,verification}` — `aac7ddaa…` → `f9dda959…` (0,0).
  Counts moved 16/16/16/24/13 → 19/19/18/24/15. Verified:
  `git ls-tree -r e3a1ec9|HEAD --name-only corpus/knowledge/<p> | wc -l` on
  2026-10-17. Receipt `row-039.json` (which also reconstructs the old output
  string to the recorded hash).
- **row 40** directory listings of the same four partitions — `898ac800…` →
  `4294834bed830db1…` (0,0). The listing gained exactly the 10 filenames
  `94ca098` added. Verified via the same revision counts. Receipt
  `row-040.json`.
- **row 51** `ls corpus/knowledge/verification/ | wc -l` — `3fdba35f…` →
  `e629fa65…` (0,0). 13 → 15 entries
  (`header-conformance-readings.md`,
  `verification-independence-anti-circularity.md` added by `94ca098`).
  Verified by `git ls-tree -r` at both revisions. Receipt `row-051.json`.
- **row 54** `grep -ril errata corpus/knowledge/ | wc -l` — `e7f6c011…` →
  `7902699b…` (0,0). 6 → 7 files; `94ca098` added an errata section to
  `corpus/knowledge/linguistics/sound-symbolism.md`. Verified by
  `git grep -l errata <rev> -- corpus/knowledge | wc -l` (6 at `9dc18ec`,
  7 at `94ca098`/HEAD). Receipt `row-054.json`.
- **row 111** `python3 tools/source-audit-inventory.py --json --summary --root
  corpus/knowledge` — `c83dac8f…` → `d4c29a95…` (0,0). Corpus grew 179 → 189
  files at `94ca098`; the command is deterministic at a fixed tree.
  Verified by re-run in `.scratch/r11f09/iso` (byte-equal `d4c29a95…`) and by
  file counts at both revisions. Receipts `row-111.json`, `row-121.json`,
  `row-152.json`, `row-190.json` (same command, four ledger pins).
- **row 117** `git status --porcelain -- . ':!/.scratch'` — `a3f92351…` →
  `295d7ffa…` (0,0). Live-worktree snapshot: the receipt (19:03) lists 8
  modified + round-11 untracked paths; my re-run at 19:15 reads a further
  different set (hash `5f8c4ee0…`), including the D seat's new artifacts
  `examples/culture-d2/packet.d2.typed.yml`, `typed-gate.expected.yml`,
  `reports/round-11/adjacency.md`. The state is legitimate round-11 work; a
  snapshot pin can only hold at one instant. Receipt `row-117.json`.
- **row 121** same command as row 111 — `c83dac8f…` → `d4c29a95…` (0,0).
  A clone at `e3a1ec9` reproduces the prior exactly (receipt); I reproduced
  the new hash in my mirror. Receipt `row-121.json`.
- **row 129** `python3 reports/round-6/run-validation.py` — `79440ea7…` →
  `ef767ba7…` (1,1). The failure line moved from "append-only prefix lost:
  SKILL.md" to "historical file changed: .gitignore" because `94ca098` added
  `.scratch/` to `.gitignore`; the round-scoped preservation check reads that
  as a historical-file change. Verified in clean `iso-full`:
  byte-equal `ef767ba7…`, failure line confirmed. Receipt `row-129.json`.
- **row 130** `python3 reports/round-7/run-validation.py` — `3ffc98f6…` →
  `a0c9e674…` (1,1). Embedded totals moved with the corpus (files 179 → 189,
  raw_lines 610 → 688); filed-red semantics unchanged. Verified in clean
  `iso-full`: byte-equal `a0c9e674…`. Receipt `row-130.json`.
- **row 152** same command as row 111 — `c83dac8f…` → `d4c29a95…` (0,0).
  As row 111. Receipt `row-152.json`.
- **row 189** `python3 tools/source-audit-inventory.py --json` —
  `41b71e3d…` → `3ce2ec30…` (0,0). Content-bound output: 10 new corpus
  entries (files 179 → 189); the ledger's own row note already called this
  pin revision-bound. Verified by lane-root re-run (byte-equal `3ce2ec30…`);
  an in-mirror run differs only by the embedded absolute root
  (`5f86126f…`), so path-dependence is present too but is not the cause of
  this row's move (both recorded and current runs were lane-root).
  Receipt `row-189.json`.
- **row 190** same command as row 111 — `0d096bef…` → `d4c29a95…` (0,0).
  As row 111/152. Receipt `row-190.json`.

### Environmental — 21 rows

- **row 65** `python3 tools/check-gate-battery.py` — `6fd828d3…` →
  `af993dae…` (2,2). The JSON stdout embeds the random mirror directory
  (`gate-battery-<rand>`) and per-gate wall-clock `seconds`. Verified: two
  consecutive runs in one tree `db7f977e…` vs `111cec80…`, 32 differing
  lines, all token/seconds; normalized (token → `<rand>`, seconds → 0)
  outputs byte-identical (`bef20ae5…`); semantic summary identical (pass 7 /
  fail 0, uncovered [myth, naming]). Same class as round-10
  `audit.md:84`. Receipt `row-065.json`.
- **row 66** three-root battery — `c164b1e2…` → `6c254f23…` (0,0). Verified:
  two runs `7153c694…` vs `028fc86a…`, 40 differing lines, all token/seconds;
  exit 0 and summary identical. Receipt `row-066.json`.
- **row 90** `python3 tools/source-audit-inventory.py --json` —
  `effe2fa8…` → `b21837c2…` (0,0). Environmental (the JSON embeds the
  absolute scan root) + legitimate change (corpus 179 → 189). Verified: my
  iso run `5f86126f…` vs lane run `3ce2ec30…` differ by root only; totals
  `files=189` in both. Receipt `row-090.json`.
- **row 91** `python3 tools/source-audit-inventory.py --selftest` —
  `ecb68511…` → `a0877052…` (0,0). The selftest prints a random temp dir
  (`source-audit-inventory-cli-<rand>`). Verified: two runs `a5060baf…` vs
  `c70de3da…`, 14 differing lines, all the random token. Round-10
  `audit.md:90` certifies the class. Receipt `row-091.json`.
- **row 98** battery default — `6fd828d3…` → `192b3750…` (2). Same class as
  row 65; verified by the same two-run normalization. The receipt labels it
  "defect"; this seat names it environmental — see §3.5. Receipt
  `row-098.json`.
- **row 99** three-root battery — `08ac35b8…` → `374086d2…` (0). Same class
  as row 66. Receipt `row-099.json`.
- **row 102** `python3 reports/round-5/run-validation.py` — `2e7d8c0f…` →
  `6190f44d…` (1). Its `errors.O` embeds the bare battery's JSON verbatim
  (random token + `seconds`). Verified in `iso-full`: two consecutive runs
  `385bbfdc…` vs `cd6e97c1…`, 4 differing lines, both inside the embedded
  battery output; exit 1 both; the round-scoped red reading itself is the
  documented `fix-22.md` state. Receipt `row-102.json`.
- **row 103** battery default — `f456f79d…` → `efaf792d…` (2). Same class as
  row 65. Receipt `row-103.json`.
- **row 120** round-5 runner — `2e7d8c0f…` → `3f6cd9d7…` (1,1). Same class
  as row 102; the receipt's masked outputs are byte-identical
  (`c54a7918…`). Receipt `row-120.json`.
- **row 127** inventory selftest — `e06fde07…` → `5c218afd…` (0,0). Same
  class as row 91. Receipt `row-127.json`.
- **row 128** battery default — `8bf71a02…` → `bdf31b39…` (2,2). Same class
  as row 65; the receipt's masked outputs are byte-identical
  (`15e16034…`). Receipt `row-128.json`.
- **row 153** `python3 tools/source-audit-inventory.py --json --summary` —
  `d48d80d3…` → `6f2dfcd1…` (0,0). No-root output embeds the absolute
  resolved root. Verified: my lane-root run is byte-equal `6f2dfcd1…`, an
  in-mirror run differs (`iso` hashes differ at the same totals, files=189).
  Receipt `row-153.json`.
- **row 154** inventory selftest — `1496ebf7…` → `6a1e9a97…` (0,0). Same
  class as row 91. Receipt `row-154.json`.
- **row 162** battery default — `9b382adf…` → `0ddd69d2…` (2,2). Same class
  as row 65. Receipt `row-162.json`.
- **row 163** `python3 tools/gates/costume-era-consistency-gate.py --selftest`
  — `d45a9add…` → `0c2ed631…` (0,0). Stdout embeds absolute fixture/expected
  paths. Verified: two mirrors give `aa03fd9e…` vs `74d8a5d3…`, 6 differing
  lines, all absolute paths; exit 0 both. Receipt `row-163.json`.
- **row 169** `python3 tools/gates/provenance-audit.py --selftest` —
  `66ac915b…` → `972306c1…` (0,0). Same class as row 163. Verified: two
  mirrors `1e0da22f…` vs `2cde84bc…`, 32 differing lines (paths). Receipt
  `row-169.json`.
- **row 170** round-5 runner — `dd65e422…` → `462d4387…` (1,1). Same class
  as row 102; the recording shard itself held two hashes for one revision
  (`dd65e422…` fresh clone, `fdf734fe…` shared clone). Receipt
  `row-170.json`.
- **row 174** `python3 tools/replay-frozen.py
  tools/gates/frozen/round-3/MANIFEST.tsv --json` — `45537a5e…` →
  `cbde6c5e…` (2,2). The JSON embeds `"repo_root"` as an absolute path.
  Verified: two mirrors `54ecd135…` vs `e32b8fd4…`, 4 differing lines, only
  the `repo_root` value; exit 2 both (7/7 could-not-evaluate by design).
  Receipt `row-174.json`.
- **row 175** same with `attempt-1/MANIFEST.tsv` — `915233ea…` →
  `b127f18c…` (2,2). As row 174. Receipt `row-175.json`.
- **row 177** three-root battery — `c164b1e2…` → `66eff405…` (0,0). Same
  class as row 66; the receipt documents four runs with four hashes.
  Receipt `row-177.json`.
- **row 185** `python3 tools/d2-typed-labels.py --packet
  .scratch/shard-05/packet-compare-only.d2.yml` — `2ce33457…` → `60dcda66…`
  (2,2). The recorded input was uncommitted scratch, deleted; four
  documented reconstructions reproduce exit 2 and the finding classes but not
  the bytes. Verified: I re-ran with the recreated packet and got a third
  hash `3a29b79c…` (neither the pin nor the receipt's reconstruction) —
  the output is input-content-bound and the input is unrecoverable. Receipt
  `row-185.json`.

### Defect — 7 rows

- **row 1** `sed -n '1,20p' SKILL.md | grep -nE '(backtick|https?://|python3|
  bash |curl|wget|git |.py|.sh)'` — `e3b0c442…` (empty, exit 1) →
  `62fa398f…` (exit 0). The ledger's command text lost the regex escapes the
  shard actually ran (`shard-01.md:30` has
  `'(`|https?://|python3|bash |curl|wget|git |\.py|\.sh)'`; the JSON block at
  `shard-01.md:78` — the ledger's source — emits the unescaped form). The
  unescaped form matches `sh` inside `shokunin`/"description" (6 hits, exit
  0). Verified: I ran both forms; the escaped form gives empty output =
  the recorded `e3b0c442…`. The artifact (SKILL.md:1-20) is unchanged.
  Receipt `row-001.json`.
- **row 12** `grep -n -i shonen /home/vgpnk/.kimi-code/skills/shokunin/
  SKILL.md` — `060d4722…` → `4479515c…` (0,0). The ledger dropped the shard's
  `-m3` limit (`shard-01.md:49`, `:67`); unbounded grep prints 6 hits,
  `-m3` prints 3. Verified: my both-form runs reproduce `4479515c…`
  (unbounded) and `060d4722…` (`-m3`, = the pin); the user-scope file is
  unchanged (git clean at `fd9ed8c`, outside this lane's write scope).
  Receipt `row-012.json`.
- **row 67** seven-gate fixture-stability control (prose row: `for g in
  <7 gates>; do … done`) — pin `ca39f5fc…` (0) has no byte-comparable
  re-run: the ledger stores the description, not the script. Reconstructed
  and reproduced by the receipt; I re-ran the control myself: all seven
  `--selftest` exit 0, fixture snapshot (sha256 + mtime_ns + inode + size
  over 21 files) byte-identical before/after. Receipt `row-067.json`.
- **row 68** tamper control (prose) — pin `04edbb00…` (1). Reconstructed by
  the receipt; my re-run of the control: appended bytes to
  `tools/gates/fixtures/phonology-sanity-gate.yml` and
  `provenance/defect-empty-couples.md`, both selftests exit 1 with
  "diverges from the embedded constant; refusing to overwrite".
  Receipt `row-068.json`.
- **row 69** delete/regenerate control (prose) — pin `e0a9ec0d…` (0).
  Reconstructed by the receipt; my re-run: removed the phonology fixture,
  selftest exit 0 "15/15 planted finding IDs present; 29 control cases
  passed", regenerated file sha256 `96dfa97e…` =
  `git show HEAD:tools/gates/fixtures/phonology-sanity-gate.yml`.
  Receipt `row-069.json`.
- **row 113** `python3 reports/round-8/run-validation.py` — `4d300b24…`
  (exit 0) → `9d0d40f1…` (exit 1). The pin requires the patched runner
  `d78da29f…`; that artifact exists nowhere. Verified: the delivered
  `reports/round-8/run-validation.py` is `7eaa3678…` = `HEAD:…` (last
  committed at `e1694ba`), `gate_blob_for_pin` absent, and
  `git cat-file --batch-all-objects | grep d78da29f` = 0 objects; all 20+
  scratch copies under `.scratch` are also `7eaa3678…`. `fix-20.md:48`
  claims the in-place repair `7eaa3678… → d78da29f…`; `94ca098` did not
  carry the file and its message records a revert of filed round-8/9
  receipt bytes "and documented staleness instead". Byte-level consequence
  measured: clean mirrored tree → `b2fb9893…` (row 173's pin), tree with
  the round-10-close dirty set → `9d0d40f1…` (row 131's pin). So row 131's
  bytes are reproducible (with the committed runner), row 113's are not.
  Receipts `row-113.json`, `row-131.json`, `row-173.json`; see §3.1.
- **row 188** — defect (row format): the row records the digest of a scratch
  artifact as its output pin, so no 1:1 command re-run exists
  (`shard-05.md:24`, `:84`); its input `.scratch/shard-05/locators.txt` is
  uncommitted and deleted (environmental component). The receipt re-derives
  the sweep instead: 7 of the 8 stale line numbers are still stale, all
  claimed content present. Receipt `row-188.json`.

## 3. Findings handed to the round

1. **Row 113 / fix-20 — a `stale-fixed` pin whose fix is not in the
   delivery.** The only ledger row that pins a *post-fix* artifact that
   cannot be produced, because the repaired runner revision was never
   committed and the repair text (`fix-20.md:48`) describes an in-place edit
   the delivery does not carry. Recommendation to the scribe/verifier: read
   row 113 as `stale-documented` (fix attempted, reverted before admit), and
   note `fix-20.md`'s runner-digest claim as superseded. Do not edit the
   filed ledger; carry the correction in round-11 documents.
2. **Two confirmed ledger transcription defects (rows 1, 12).** The command
   text in the ledger JSON differs from the command that produced the pin
   (lost regex escapes; dropped `-m3`). Both are byte-level provable against
   `shard-01.md` (lines 30/78 and 49/67).
3. **Prose-as-command rows (67, 68, 69) and artifact-digest row (188).**
   These rows cannot be rechecked 1:1 by construction; the recheck
   reconstructed the controls and reproduced the semantics (rows 67/68/69
   verified by this seat independently). Recommend a ledger-format note that
   such rows are rechecked by reconstruction, not by byte hash.
4. **Environmental pin family — 21 rows.** Six battery pins, five inventory
   pins, five path-embedding gate/replay pins, three round-scoped runners
   embedding volatile child output, one deleted-input packet, one deleted
   locator file. These can never be byte-stable as pinned. Any future ledger
   should either compare such commands after normalization (mask
   `gate-battery-<rand>`, `source-audit-inventory-cli-<rand>`, `seconds`,
   absolute roots) or mark them "not byte-reproducible by construction".
5. **Label variance across receipts.** `row-098/099/103.json` call the
   battery volatility "defect"; `row-065/066/128/162/177.json` call the same
   phenomenon "environmental". It is one phenomenon; this seat names it
   environmental (normalized outputs are byte-identical, semantics unchanged,
   round-10 `audit.md:84`/`:90` certified the class, and no lane artifact is
   stale). Flagged so the audit and summary do not split one class in two.
6. **Caveats on some rows recorded as stable** (for the F11 auditor; not
   dispositions): row 101 is stable only because its recorded output was
   empty while its inputs were deleted; rows 20/55/58 are byte-stable but
   their recorded command text is a placeholder — the hash reproduces, the
   artifact signal does not; rows 182-184 are stable only via reconstructed
   inputs (byte-identity is achievable because the recorded outputs do not
   embed the packet content).

## 4. What this seat did not do

- No filed round-8/9/10/11 byte, ledger row, receipt, tool, fixture or corpus
  file was modified; no git commit was made. All scratch lives under
  `.scratch/r11f09/` and is disposable (mirrors `iso`, `iso-full`, captured
  outputs `out/`, notes `preevidence.json`, `unstable.json`, `snapshot.txt`).
- Claim judgement (the ≥95% bar, the D/O legs) is not this seat's assignment;
  §1's last bullet and §3 flag the decision-relevant facts without deciding
  them.
