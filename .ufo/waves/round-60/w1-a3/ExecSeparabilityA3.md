NONE-MET

# ExecSeparabilityA3 — routed defect 3: separability on a deterministic leg set

Seat `KotodamaR60A3.ExecSeparabilityA3` (leaf). Lane revision `14e6413820d482913f723432b62d566967ccd1a6`.
All work in `/fast/scratch/hyaku/kotodama-r60a3/ExecSeparabilityA3/`; the lane received no write except this report.
No installs, no upgrades, no pacman. No LSP use (not applicable to a tool run).

Why `NONE-MET` rather than `CONTROL-MET`: this lane builds no fixture that skips claimed work. The only counter
invocation here is the attribution run in §4, which reaches `ACCEPT-D-60: FAIL` (JUDGED, SUPPORT), not PASS.

## 1. Mock build in the sandbox clone

| Step | Command / fact | Result |
|---|---|---|
| clone | `git clone --no-hardlinks <lane> clone && git checkout -q 14e64138…` | HEAD = `14e6413820d482913f723432b62d566967ccd1a6` |
| patch | `git apply --check` then `git apply /fast/scratch/hyaku/kotodama-r60a3/L1/build.patch` | exit 0 both |
| captures | `cp -p L1/captures/* reports/round-60/captures/` | S648–S651 sha256 equal to `captures/manifest.json` (`2dafb2a2…`, `945d52a2…`, `5e353d2f…`, `8e4cf019…`); manifest.json `49d98b83…`, same as L1 copy |
| mock build commit | `fbdb570d536dbe6bfdc299817357b6014280039b`, parent `14e6413820d482913f723432b62d566967ccd1a6`, 7 files, +3688/−14 | clone only, never pushed, never offered for integration |
| candidate bytes | entry sha256 `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` — identical to `L1/candidate-entry.md` | yes |
| patch roundtrip | `git diff HEAD^ HEAD` vs `L1/build.patch`: hunks and index lines identical; only jj prefixes `i/ w/` vs `a/ b/` differ | yes |
| entry ids | `grep -oE 'S6[0-9][0-9]' <entry> | sort -u | wc -l` | 47 |
| added corpus lines | 4 SOURCES rows + 18 entry lines (`git diff --numstat`: 4/0, 18/14) | 22 |

Manifest base, clone-only (the tool refuses `BASE_PLACEHOLDER`; verified in §3):

```diff
--- i/reports/round-60/separability-manifest.json
+++ w/reports/round-60/separability-manifest.json
@@ -1,6 +1,6 @@
 {
  "schema": "kotodama-separability-manifest-v1",
- "base": "BASE_PLACEHOLDER",
+ "base": "14e6413820d482913f723432b62d566967ccd1a6",
```

This edit is uncommitted in the clone (the only `git status` entry) and is not part of the mock build commit.
Manifest sha256 after edit `69b162e0…`; before edit `c35ebd7…` (blob id).

## 2. Environment

- `python3 --version` → Python 3.14.8; tool `tools/check-claim-separability.py` sha256 `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5`.
- `unshare -rn` present and functional; offline control inside it: `urllib.request.urlopen('https://example.com')` → `urllib.error.URLError: <urlopen error [Errno 101] Network is unreachable>` (exit 1). The netns really has no route.
- Tool's own default acceptance timeout 600 s; I wrapped every run in `timeout 900`.

## 3. The requested run: frozen manifest, base = mock parent

Command (twice; second under a network namespace):

```
cd clone && timeout 900 python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json
cd clone && unshare -rn timeout 900 python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json
```

Run 1 (`frozen-r1`), exit **2**:

STDOUT (full, 0 bytes):
```
```
STDERR (full):
```
SEPARABILITY_INPUT_ERROR unit D lands '.ufo/waves/round-60/support/registry.json', which is absent from the worktree under '/fast/scratch/hyaku/kotodama-r60a3/ExecSeparabilityA3/clone'
```

Run 2 (`frozen-r2`, `unshare -rn`), exit **2**: byte-identical, stdout `e3b0c442…b855` (empty), stderr `11a27fc72e6cf2d1288f002fd80f75d8e68def4e3a3b6feaad203cdf113e43e5` for both; `cmp -s` on stdout and on stderr both succeed.

Line-by-line:

- `SEPARABILITY_INPUT_ERROR unit D lands '.ufo/waves/round-60/support/registry.json', which is absent from the worktree …` — the evaluator refuses input instead of scoring. It is the first of the 76 declared D lands that do not exist before the support wave (they are the later 24-seat wave's registry, packets, reports and transcripts, plus `reports/round-60/planted-key.sha256`). Exit 2 is "could not evaluate", never a pass. **No dependency is attributed by this run; it reports nothing about separability at all.**
- The manifest as committed is even less runnable: with `base: "BASE_PLACEHOLDER"` untouched, one run gives exit 2, empty stdout, stderr `SEPARABILITY_INPUT_ERROR base 'BASE_PLACEHOLDER' does not name a commit in lane '…/clone'` (stderr sha256 `4e5a94a82c3a3e6b157774e606dab0609911087a3bac352df9eae3ac497e8e49`). The base must be filled before this control can score anything.

So the wave-1 result for the frozen manifest is **not evaluable**, deterministically, for a shape reason, not for a build reason.

## 4. Operative run: build-present lands only (clone-only reduced manifest)

To get an actual separability reading on the candidate build, I kept only the declared lands that exist at the mock build — D: entry, `corpus/SOURCES.md`, `reports/round-60/captures/{manifest.json,S648.bin,S649.bin,S650.bin,S651.bin}`, `reports/round-60/planted-rows.sha256` (base-present, unchanged); REC: the 7 of its 8 lands present in the worktree (`corpus/lessons/round-60.md` is itself a future output and was dropped). Everything else (ids, exports `\bS6(?:4[89]|5[01])\b`, acceptance argv, base) is untouched. Manifest sha256 `d2449d3339258f1818bba41be3a51e71e917c83c4bbf1ac0a0ff25bc7f95df82`.

Command: `timeout 900 python3 -B tools/check-claim-separability.py <sandbox>/manifest-reduced.json` (and the same under `unshare -rn`).

Run 1 (`reduced-r1`), exit **1**:

STDOUT (full):
```
SEPARABILITY_DEPENDENCY D-><base> via acceptance ['python3', '-B', 'reports/round-60/accept-d.py'] fails on base+D.lands (rc=1) and no declared unit's lands repairs it
SEPARABILITY: 1 findings
```
STDERR (full):
```
SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=2
```

Run 2 (`reduced-r2`, `unshare -rn`), exit **1**: byte-identical, stdout `edf89dc939b8c330bdccd79151218ea917c13e513a2ef36174685f9fda8bc36f`, stderr `93c32b9f526266d3c8bdde8406fa07ea8a915b192d0c8583467299cc77206009`; `cmp -s` both succeeds.

Line-by-line:

- `SEPARABILITY_DEPENDENCY D-><base> via acceptance … fails on base+D.lands (rc=1) and no declared unit's lands repairs it` — the dynamic leg ran `python3 -B reports/round-60/accept-d.py` twice: once in base with D's lands overlaid (rc=1), once with REC's lands added (also non-zero, so REC repairs nothing). Since no declared unit repairs it, the tool names `<base>`. It does **not** attribute `D->REC`: the build does not borrow the record unit's bytes.
- Attribution of that failure (I reproduced it by hand: `git archive 14e64138… | tar -x` into `cf-base`, overlayed the 8 lands, ran the counter with `--root`). Full counter stdout, exit 1:
```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', …, 'S651:good=0'] qualified=[] seats=[] no-registry:…
ACCEPT-D-60: FAIL
```
  All build-dependent legs pass at the mock build (SET sees exactly 47 cited ids, LINES/OLDWORD/ROWS/PINNED clean). The two failures are `JUDGED` (`reports/round-60/planted-key.sha256` absent — a declared D land deferred to the support wave) and `SUPPORT` (`registry.json` et al. absent — the same deferred lands). The `D-><base>` line is therefore an artefact of the pruning I had to do to make the manifest evaluable at all, not a missing cross-unit dependency. With the full declared lands (post support wave) the same leg is the one that will decide build-vs-record separability; it cannot be decided in wave 1.
- `SEPARABILITY: 1 findings` — sorted findings count; one ordered pair (D as claim) produced one line.
- `SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=2` — accounting only: 2 units, 2 ordered pairs (REC is a record and is never a depender), 2 acceptance runs (base+D, base+D+REC).

## 5. Static leg alone: 0 findings, and proof the static leg is live

Static-only variant (acceptance key removed; same lands; sha256 `2e295fe0cd20ee0b66b8a444a76934c5dd62b0c4c81d541972137dadc8500fd2`):

Run `static-r1`, exit **0** — STDOUT (full):
```
SEPARABILITY: 0 findings
```
STDERR (full): `SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0`
Run `static-r2` under `unshare -rn`, exit **0**: byte-identical, stdout `36d8196734a6d8fd2ddd9b83dc0bb04e8c487db27331ae0ab650f9b3e89da17f`, stderr `bea5ec303ace781b653091fcfc8c13dbf35b0e2228def54cfbd2c26d94704678`.

Meaning: none of D's 22 added lines contains a REC export (REC declares none) and none names a REC land path that is absent at base. Independent check: `grep` over the added lines for `reports/|tools/|corpus/` returns only the diff headers and URLs — no repo-relative path is named.

Liveness probe (so that "0 findings" is not vacuous): added a synthetic record unit `Z` landing `reports/round-60/base-entry.md` (base-present) with export `Heeßel`. Run `probe-r1`, exit **1** — STDOUT (full):
```
SEPARABILITY_DEPENDENCY D->Z via export 'Heeßel' matched corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:58
SEPARABILITY: 1 findings
```
STDERR: `SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=0`. Under `unshare -rn` byte-identical (stdout `0a7b94e2…`, stderr `49ea3afd…`).
Novelty guard probe (export `Pazuzu`, which does occur in base `base-entry.md`): exit **2**, stdout empty, stderr `SEPARABILITY_INPUT_ERROR unit Z2 export 'Pazuzu' is not novel: it matches base bytes of 'reports/round-60/base-entry.md'` — the tool refuses a stale export rather than pretending it names new bytes.

## 6. Determinism and no-network evidence

| Pair | stdout sha256 | stderr sha256 | exit | byte-identical |
|---|---|---|---|---|
| frozen r1 / r2 | `e3b0c442…b855` (empty) | `11a27fc7…43e5` | 2 / 2 | yes |
| reduced r1 / r2 | `edf89dc9…bc36f` | `93c32b9f…6009` | 1 / 1 | yes |
| static r1 / r2 | `36d81967…a17f` | `bea5ec30…4678` | 0 / 0 | yes |
| probe r1 / r2 | `0a7b94e2…d7fd` | `49ea3afd…a6c` | 1 / 1 | yes |

`cmp -s` on each stdout and each stderr: all succeed (8/8 comparisons). No timestamps, run ids or temp paths appear in any output line.

No leg fetches:
- `unshare -rn` runs produce byte-identical output to the networked runs; inside that namespace an outbound request fails with `Errno 101 Network is unreachable` (control above), so nothing needed the network.
- `strace -f -e trace=network` over the whole process tree: `AF_INET` lines = 0 and `connect(` lines = 0 for frozen, reduced and static. The only socket calls are `socketpair(AF_UNIX, SOCK_CLOEXEC…)` + a zero-byte `recvfrom` — Python's `subprocess` exec-error pipe for the acceptance child (2 pairs per acceptance run). The 72 `sendfile` lines in the reduced trace are `shutil.copytree`'s fast copy of the base tree, not I/O to a peer.
- The tool's only git use is read-only `git -C <lane> cat-file --batch` (no `needs_git` unit here); the only writes are `claim-separability-run-*` temp dirs under `/tmp`, and `ls -d /tmp/claim-separability-run-*` after all runs → 0 leftovers.

Tool health at this revision: `python3 -B tools/check-claim-separability.py --selftest` exit 0, `selftest: 56/56 checks passed` (positive, negative and malformed-input controls, including WORKTREE reading, record-never-depender, acceptance attribution in git-free and needs_git trees, timeout, overlap and sorted output).

## 7. Verdict for the L1 (operability)

1. **The frozen manifest is not a wave-1 instrument as shaped.** 76 of D's 84 declared lands and 1 of REC's 8 are outputs of the later support/record waves; the tool reads WORKTREE units strictly and exits 2 on the first missing land. Its base is also the literal `BASE_PLACEHOLDER`, which fails even earlier. If the L1 wants a committed separability receipt in wave 1, it must either (a) commit a pre-data manifest variant whose D unit declares only the build-present lands, or (b) schedule the control after the support wave and commit the support outputs under their own unit; scoring the frozen file today can only yield `SEPARABILITY_INPUT_ERROR`.
2. **No static dependency of the build on the record unit.** 0 findings with a live static leg (probe detects an export-shaped dependency; novelty guard fires). This part is already answerable and clean.
3. **The dynamic leg cannot answer build-vs-record separability pre-data.** D's own acceptance needs `reports/round-60/planted-key.sha256` and the support registry/packets/transcripts, all of which D itself lands later. The observed `D-><base>` line is pruning-induced; it must not be read as "the build depends on <base>" in a way that changes the claim. The counter run on base+D.lands confirms the build legs pass (SET cited=47, LINES, OLDWORD, ROWS, PINNED) and only the future-wave legs fail.
4. **Determinism and offline operation hold** for every shape I ran, including inside a namespace with no route. Any byte drift between two runs of this control would be a real defect; none appeared.

Incidental counter observation (not a scored control case, no fixture built): `counter-sha256=b6389454…b450cdc rev=14e64138… frozen=FAIL exit=1 stopped-by=JUDGED,SUPPORT` for `base + D.lands` reproduced by hand. No PROVENANCE or later leg executed, so no session material was read (the counter's session glob, if reached, is a filename listing only).

## 8. Residual risks / blockers

- WORKTREE units scan uncommitted bytes (the tool's own selftest asserts this). When the L1 scores the real lane, the worktree must equal the intended commit or the control measures stale bytes.
- A reduced manifest is my construction and is not the declared instrument; its `D-><base>` finding is explained above and should not be pasted into a claim score as a dependency.
- This lane builds no skip-work fixture for the counter-mutation suite, so the `CONTROL-MET` question is `NONE-MET` from this seat; the counter attribution run failed rather than passed.
- Sandbox hygiene: every run log, manifest variant, strace log, `applied.diff` and the mock-build clone are retained under `/fast/scratch/hyaku/kotodama-r60a3/ExecSeparabilityA3/` (165 MB, under the 200 MB cap); the materialized base tree `cf-base` was deleted after the attribution run, which is reproducible with the `git archive` command in §4. No process left running; no `/tmp/claim-separability-run-*` leftover.
