# 30 — mutation review: does anything notice a tampered round-3 frozen artifact?

- role: mutation reviewer (not an implementation review; the new replay worker's code is
  not examined here and nothing below depends on it)
- wave: `supplement-opencode-1` (supplemental; not a numbered round)
- baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404`
- measured: 2026-10-17, final pin re-check at 15:39:32Z
- assigned write path: this file only. No source-audit JSON: no knowledge entry was
  assigned to this worker, so the SOURCE-RECHECK duties do not apply and no source is
  claimed. No LOG/SCORECARD/SKILL writes, no SHONEN marks, no rank claim.

## 1. Question and method

Question: if one round-3 frozen input or expected output is mutated, does any **existing**
mechanism notice — and how does that compare with doing the manifest's digest pin by hand?

Baseline anchoring: the round-3 frozen tree is byte-unchanged from round 3 to the baseline
(`git diff --name-only c610e0a fe34faa -- tools/gates/frozen/round-3 | wc -l` = `0`), so all
measurements below are against committed bytes.

Scratch (all under `reports/supplement-opencode-1/scratch/30/`, removed at the end):

| dir | purpose |
|---|---|
| `tree/` | raw copy of `tools/gates/frozen/round-3/` — first probe (mis-rooted, see §6.1) |
| `replica/` | lane-root replica: `tools/gates/*.py` + `tools/gates/frozen/round-3/` — the mutated copy |
| `replay-root/` | round-3 corpus bytes restored under the **recorded relative argv path** |
| `gitdemo/` | throwaway git repo, for git's own tamper behavior |

The manifest's 10th column (the recorded `command` string) was never executed or
interpreted. The scratch comparator read columns 1,2,3,4,7,8,9 (gate, gate_sha256, input,
input_sha256, output, output_sha256, input_snapshot) only.

## 2. Pin verification by hand, clean state

`tools/gates/frozen/round-3/MANIFEST.tsv` has 7 rows (6 gates; `provenance-audit` twice) and
10 columns. Tool-free reproduction (coreutils only, from the lane root):

```sh
M=tools/gates/frozen/round-3/MANIFEST.tsv
awk -F'\t' 'NR>1{print $2"  "$1}' $M | sha256sum -c -   # gate pins
awk -F'\t' 'NR>1{print $4"  "$9}' $M | sha256sum -c -   # snapshot pins
awk -F'\t' 'NR>1{print $8"  "$7}' $M | sha256sum -c -   # output pins
```

Observed: `7 OK`, `7 OK`, `7 OK`; every `sha256sum -c` exits 0. 21 pinned digests, all
matching today. Gate pins also match the working-tree gates (the round-3 dir and
`tools/gates/*.py` are unmodified vs HEAD: they appear in no `git diff --name-only` output).

Observed property worth naming: the packet snapshot is pinned by 5 rows, so one edit to it
produces 5 identical FAILED lines, not 1 — the pin set has no per-file dedup.

**Ambiguity, measured.** The `input` column names the *live* path
(`examples/culture-d2/packet.d2.yml`), whose bytes have since moved: today it hashes
`d5fb4088…` (round-4) while `input_sha256` is `54be6319…` (= round-3 commit bytes = the
snapshot copy). Same for the two corpus rows (`437ca8de…`/`31f589f5…` live vs
`a916a4c2…`/`7b3bdc80…` pinned). The TSV never states that `input_sha256` grades the
`input_snapshot` copy rather than the live `input` path; the manual check has to decide, and
a verifier that picks the live-path reading sees 7 false tampers today.

## 3. Positive control: are the frozen runs re-executable?

Run over the committed snapshot copy (not the live path):

| gate | observed exit | stdout sha256 | pinned `output_sha256` |
|---|---|---|---|
| phonology-sanity-gate | 1 | `1ce5f0cd…` | `1ce5f0cd…` |
| lexicon-coverage-audit | 0 | `e3b0c442…` (empty) | `e3b0c442…` |
| myth-consistency-gate | 1 | `ea56c2d3…` | `ea56c2d3…` |
| costume-era-consistency-gate | 1 | `129c4f5a…` | `129c4f5a…` |
| naming-collision-gate | 1 | `e81bab66…` | `e81bab66…` |

All five byte-identical to the pin, exits matching the manifest's `exit_code` column. The
two provenance rows do **not** match on a naive snapshot-path replay (`15d0a924…` and
`0aee4118…` vs pinned `57a537ae…`/`1b8bf0b8…`, both exit 0). Cause measured by diff: line 1
of the gate's stdout embeds the argv path string, and the frozen run was invoked with the
live lane-relative path. Restoring the round-3 bytes under that same relative path —

```sh
mkdir -p …/replay-root/corpus/knowledge/{civilizations,verification}
git show c610e0a:corpus/knowledge/civilizations/mesoamerica-primary-sources.md > …/replay-root/corpus/knowledge/civilizations/mesoamerica-primary-sources.md
git show c610e0a:corpus/knowledge/verification/gate-frozen-run-standard.md > …/replay-root/corpus/knowledge/verification/gate-frozen-run-standard.md
cd …/replay-root && python3 <lane>/tools/gates/provenance-audit.py corpus/knowledge/civilizations/mesoamerica-primary-sources.md | sha256sum
```

reproduces both pins byte-exactly (`57a537ae…`, `1b8bf0b8…`). So the pins are sound and the
frozen runs are reproducible — **given a stated invocation convention** (cwd, relative argv
string, round-3 bytes). `LOG.md:1949-1951` ("all seven final commands reproduce exact exit
codes and output bytes") is not contradicted; it holds under that convention and not for a
snapshot-path replay of the two provenance rows.

## 4. Tamper matrix — what notices

Mutations applied to copies in `replica/` (frozen bytes never modified):

| # | mutation | gate behavior | manual digest check |
|---|---|---|---|
| 1 | append `# tamper-review-30 replica` to the packet snapshot | **invisible**: stdout still `1ce5f0cd…`, exit 1, `diff` empty | caught: snapshot `19b454ec…` ≠ `54be6319…`, 5 FAILED, exit 1 |
| 2 | insert rule `"t → d / _ g"` into `notable_rules` (semantic control) | **changes**: 4 findings instead of 3, stdout `af04bd8d…`, packet `33a869fa…` | caught (same as #1) |
| 3 | append `FINDING XX-99: TAMPERED record line appended` to `myth-consistency-gate.out` | no in-tree reader exists; the myth gate run is unaffected | caught: output `a619d54e…` ≠ `ea56c2d3…`, 1 FAILED, exit 1 |
| 4 | append `# tamper-review-30 gate edit` to the replica's `myth-consistency-gate.py` | gate still runs and prints findings — a tampered gate has no self-doubt | caught: gate `56f0a9f6…` ≠ `26d246e9…`, 1 FAILED, exit 1 (`gate_revised` reading) |
| 5 | `frozen/round-3/selftests/*.out` transcripts | — | **not catchable**: 0 manifest rows reference `selftests/` (`awk -F'\t' 'NR>1 && $9 ~ /selftests/ {c++} END {print c+0}'` → `0`), yet `LOG.md:1952-1954` cites those transcripts as evidence |
| 6 | `frozen/round-3/attempt-1/` (own `MANIFEST.tsv`, packet `f424fcf1…`) | — | nothing in `tools/` or `SKILL.md` marks which manifest is authoritative; only `examples/culture-d2/ASSEMBLY.md:109` prose says attempt-1 is the retained initial attempt |
| 7 | `handoff-packet-check.py` | — | no row at all; the 7 rows cover 6 of the 7 registered gates |
| 8 | git itself (isolated scratch repo) | `git status --porcelain` → ` M packet.d2.yml`; after committing the tamper, status is clean again | git detects *uncommitted* edits only; it cannot say which recorded verdicts depended on the bytes |

Tamper detection, tool-free, against the mutated replica (any reader can rebuild it):

```sh
awk -F'\t' -v R=<replica> 'NR>1{print $4"  "R"/"$9}' $M | sha256sum -c -  # 5 FAILED, warning, exit 1
awk -F'\t' -v R=<replica> 'NR>1{print $8"  "R"/"$7}' $M | sha256sum -c -  # 1 FAILED, exit 1
awk -F'\t' -v R=<replica> 'NR>1{print $2"  "R"/"$1}' $M | sha256sum -c -  # 1 FAILED, exit 1
```

The scratch comparator (same columns; exit 0 clean / 2 on any tamper / 3 unreadable) reported
`all pins match` (21 digests) on the clean replica and, on the mutated one, 7 tamper lines —
5 snapshot + 1 gate + 1 output — exit 2. Row #1 is the load-bearing measurement: a cosmetic
edit is **byte-invisible to the gate** (identical stdout digest and exit), so without a digest
step an orchestrator comparing only stdout would call the run a match. Row #2 shows the gate
is not simply blind — it reacts to semantics — so row #1 is a genuine blind spot, not a
broken gate.

## 5. What exists today that could notice (baseline inventory)

- **No committed tool reads `MANIFEST.tsv`** at `fe34faa`: `git ls-tree -r --name-only
  fe34faa -- tools/` lists 62 files and includes no replay/verify entry point. Grep hits for
  `MANIFEST.tsv` are prose only: `LOG.md:1926`, `LOG.md:1975`, `SCORECARD.md:11`,
  `corpus/lessons/round-3-d2-build.md`, `examples/culture-d2/ASSEMBLY.md:51,109`.
- **No gate has a frozen/baseline mode**: every gate takes a packet path (or corpus paths)
  and/or `--selftest`; none accepts a baseline directory or reads `expected.json`. A gate
  grades whatever bytes it is handed, with no notion of tampering.
- **The lane's own standard already says this.** `corpus/knowledge/verification/gate-frozen-run-standard.md`
  §6 step 1: "Until the gates verify digests internally, the report says which interim check
  ran"; §8 records gate-internal digest verification, the committed `expected.json` layout,
  and the registry rows as not implemented. This review gives that status a second,
  independent input — the round-3 TSV freeze, not §7's fixture example — and confirms it.
- Consequence: mutation detection is a **manual digest comparison only**. Its semantics match
  the declared reading — any input mismatch is `snapshot_tampered`, could-not-evaluate — which
  my comparator mirrored by exiting 2, never 0 or 1, on tampers.

## 6. Corrections and calibration (each with its command)

1. **My own comparator was wrong twice, and I recorded it.** First, the gate column was
   checked without re-rooting, so it verified the real committed gate instead of the replica
   copy and the tampered gate script went unreported. Fixed to `root / gate`; the corrected
   run reports it. Second, the first probe (`tree/`, a bare copy of `round-3/`) crashed with
   `FileNotFoundError` because manifest paths are lane-root-relative — hence the `replica/`
   layout. A digest checker that resolves paths loosely can check the wrong file; the
   trusted-base point applies to tooling, not just to hashes.
2. **Pin subject is unnamed** (§2): `input_sha256` today describes the snapshot copy, while
   the `input` column names a live path whose bytes have moved. Any verifier must state its
   reading; the two readings disagree on 7 of 7 rows.
3. **`output_sha256` is invocation-sensitive** for `provenance-audit` (argv path string in
   stdout). Byte-exact replay requires the recorded relative path with round-3 bytes restored;
   otherwise findings reproduce but the digest does not.
4. **The freeze is not the `expected.json` schema.** The manifest is a TSV with no `schema`,
   `revision`, or per-baseline `inputs` map, and round-3 has no `README.md` index under
   `tools/gates/frozen/`. `LOG.md:1961-1962` already declares the freeze "worktree evidence,
   not the corpus standard's committed per-gate expected.json baseline" — a declared gap, not
   a concealed one; the round-4 directory has 5 `.out` files and no manifest at all.
5. **`tools/replay-frozen.py` and `tools/source-audit-inventory.py` appeared as untracked
   working-tree files during this wave** (siblings' in-flight work, not present in
   `git ls-tree fe34faa -- tools/`). This review neither examines nor depends on
   `tools/replay-frozen.py`; every measurement above ran over the pinned gate revisions
   (re-verified at 15:39:32Z: all gate digests matched their pins) and committed frozen bytes.
6. **Sibling working-tree edits at measurement time** (`corpus/knowledge/civilizations/africa-primary-sources.md`,
   `examples/culture-d2/components/06-pantheon.yml`, `07-myths-motifs.yml`,
   `tools/assemble-d2.py`) touch nothing under `tools/gates/` or the frozen tree; conclusions
   unaffected.
7. **No source-audit JSON** and no coupling audit were produced: this worker had no assigned
   knowledge entry. No sources were rechecked and none are claimed.

## 7. Limits

- Scratch was auto-cleaned; §2/§4 give the commands to rebuild any of it.
- Tampers were applied to *copies*; no committed frozen byte was modified, so this review
  creates no new freeze and claims no conformance pass.
- The gate `--selftest` battery was not re-run here: it rewrites committed fixtures, and that
  evidence belongs to the operability worker's claim, not this one.
- `unpinned (legacy)` readings for `round-4/` and for `selftests/*.out` are statements about
  the manifest's coverage, not about the correctness of those transcripts.

## 8. Verdict for the wave (evidence, not scores)

- **operability** — the negative control a frozen-replay entry point must satisfy is now
  measured independently of that worker's code: a tampered snapshot must be rejected before
  any verdict comparison. My manual check's behavior (exit 2 on tamper; per-file FAILED list;
  5 row-level hits for the shared packet pin; gate and output tampers likewise caught) is the
  observation to compare against.
- **calibration** — three miscounts corrected in public (comparator path bug; unnamed pin
  subject; provenance argv sensitivity), and two coverage gaps named with their counts
  (`handoff-packet-check` has no row; `selftests/` has 0 rows).
- **freshness** — no source claims were made or rechecked by this worker.
