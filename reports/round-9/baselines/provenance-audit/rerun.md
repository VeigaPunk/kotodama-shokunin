# provenance-audit baseline — independent re-run (round 9, rerunner seat R9-O)

- role: **rerunner** — second worker of the `provenance-audit` baseline pair (`R9-O01..O14`).
  This worker writes only this file (`reports/round-9/baselines/provenance-audit/rerun.md`); the
  author seat owns the snapshot copy, `expected.json`, `run.log` and `freeze.txt`. Nothing here
  was committed; the orchestrator integrates once per round. No gate source, fixture, or shared
  file was touched by this seat.
- date: 2026-10-17, timestamps local (-03:00) unless marked Z.
- lane revision at re-run start: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (`git rev-parse HEAD`). `reports/round-9/claims.json` names `baseline_revision: e1694bad…`;
  `git rev-parse HEAD~1` → `e1694bad6ac96aca45a11ca5746582b275929355` and
  `git diff --stat e1694ba..HEAD` → only `reports/round-9/claims.json` (34 lines) and
  `reports/round-9/targets.json` (125 lines), 159 insertions, 0 deletions. The graded artifact
  tree is therefore identical between the declared revision and HEAD; recorded, not assumed.
- gate under test: `tools/gates/provenance-audit.py`, sha256
  `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a`
  (`sha256sum tools/gates/provenance-audit.py`, 2026-10-17). The same digest was recomputed after
  every run below over the live tree — unchanged.
- fixture pins: `tools/gates/fixtures/provenance.expected` and
  `tools/gates/fixtures/provenance-audit.expected` are byte-identical to each other, both sha256
  `7ba4fa5cd326f4f73853673208851adeddf972131a9da0f526e24861218f1cbc` (six IDs, one per line).
  Fixture tree `tools/gates/fixtures/provenance/` (7 files) digests (2026-10-17):

  | fixture | sha256 |
  |---|---|
  | good-entry.md | `f4739fa2c201cf953d20d14f571d3ff67e10f1d1e902a25194229bbe42efc321` |
  | defect-missing-topic.md | `ba8b8768d93899fbfa5886ee78822c012612ddf95bd0b67615ba311a1d64899c` |
  | defect-missing-sources.md | `e980f0b2ae01a646fc2965d81fdbecee3642c6348d6535cd78b350c43c4895c2` |
  | defect-empty-sources.md | `0ed63c52155ced93e676bc75fa9f12e38c75e66bbcbd19ecdcba16ff782e019e` |
  | defect-missing-couples.md | `939ffc1bc23aeab5cbfa3a68df7f4abc6b47ff22a215366cc255d1e71b0f5a57` |
  | defect-empty-couples.md | `0284197cc996f4c180bbc976b53ed50fb8cf63b2de170576c537735ad5b10403` |
  | defect-missing-calibration.md | `63ae634c2fbe29141274f3495cb453475ffaf8e7971217bd8d4f5655ef5291f1` |

- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4 (required
  `expected.json` fields), §5 (freeze procedure), §6 (verify procedure, tamper semantics, class
  mapping). The paired reading is the two-evidences clause: self-test = capability, frozen run =
  measurement.

## 1. Environment limit measured during this re-run

- `/tmp` was **inode-exhausted** for the whole run: `df -i /tmp` →
  `tmpfs 1048576 1048576 0 100% /tmp` (2026-10-17). The by-volume check disagrees
  (`df -h /home` → `/dev/mapper/root 930G 131G 781G 15% /home`), so the failure is inode
  pressure under a 64-worker wave, not a full disk — the same hazard the round-8 audit and the
  phonology rerunner seat documented.
- All scratch therefore lived **out of the repository** on the disk-backed path
  `~/.cache/prov-rerun/` (mirror + snapshots + controls). Disposable; the live tree outside it
  was never modified by this seat (§6 re-checks live digests; `git status --porcelain tools/gates`
  shows no modification of any tracked gate or fixture byte — only the untracked baseline
  directories other seats are creating).

## 2. Capability re-executed: `--selftest` in an isolated mirror (not the live tree)

| # | Command (2026-10-17) | Observed |
|---|---|---|
| 1 | `mkdir -p ~/.cache/prov-rerun/tools && cp -r tools/gates ~/.cache/prov-rerun/tools/gates` | mirror created; mirror gate sha256 `8a96aaf4…` equals the live digest in the header |
| 2 | `cd ~/.cache/prov-rerun && python3 tools/gates/provenance-audit.py --selftest` | exit **0**; tail: `SELFTEST OK: 7 fixture file(s), planted IDs missing-topic, missing-sources, empty-sources, missing-couples, empty-couples, missing-calibration, exit 1 on the defect tree, exit 0 on the clean entry, exit 2 on a missing path`; defect-tree scan line `files=7 marks=2 mark-lines=2 findings=6 blocked=0` |

- Capability only; per standard §2 it never substitutes for the frozen run.

## 3. Independent snapshot measurement (a byte copy this seat minted itself)

Purpose: establish, independently of the author seat, that a byte-frozen copy of the committed
fixture tree produces the committed verdict, deterministically, and that the gate is read-only
over its input.

| # | Command (cwd = `~/.cache/prov-rerun`) | Observed |
|---|---|---|
| 1 | `cp -r tools/gates/fixtures/provenance snap2 && (cd snap2 && sha256sum *.md > digests.sha256)` | 7 digests recorded; equal to the live fixture digests in the header |
| 2 | `python3 tools/gates/provenance-audit.py snap2 > snap2-run.log` | exit **1**; 6 `FINDING` lines, 7 `INFO to-verify-count` lines; scan `INFO scan: files=7 marks=2 mark-lines=2 findings=6 blocked=0`; stdout sha256 `53a1f3bbd6387539ee4dc8c16edd1b9d59011d84d4930064bac751a2541ae941` |
| 3 | observed unique ID set vs committed `tools/gates/fixtures/provenance.expected` (`grep '^FINDING ' \| sed \| sort -u` then `diff`) | **empty diff — identical, 6/6 IDs**: missing-topic, missing-sources, empty-sources, missing-couples, empty-couples, missing-calibration (stdout order differs from file order; the contract is the set, standard §4) |
| 4 | re-run `… snap2 > snap2-run-b.log`; `cmp snap2-run.log snap2-run-b.log` | byte-identical — the run is deterministic |
| 5 | `(cd snap2 && sha256sum -c digests.sha256)` after the runs | all 7 `OK`, exit 0 → the gate did **not** rewrite its input (read-only over the graded files) |
| 6 | separate determinism pair over the mirror fixture path (`run-a.log`/`run-b.log`, display path `tools/gates/fixtures/provenance`) | two runs byte-identical, stdout sha256 `01340bcc1cba9583906ea52014b691c990525a2b69d4a6dd61978774c9e129d2` |

## 4. Tamper and gate-revision semantics (scratch copies only; no committed byte edited)

| # | Command (cwd = `~/.cache/prov-rerun`) | Observed |
|---|---|---|
| 1 | `cp -r tools/gates/fixtures/provenance snap && python3 … snap > snap-run.log` | exit 1; stdout sha256 `9ff2c241c45cdfdfa83f8d18f3970a0dafb5d1a05450906dc28d0d81cd18e1f8` |
| 2 | `(cd snap && sha256sum *.md > digests.sha256 && sha256sum -c digests.sha256)` | 7/7 `OK`, exit 0 |
| 3 | `printf '\n<!-- tampered byte -->\n' >> snap/good-entry.md` then `(cd snap && sha256sum -c digests.sha256)` | `good-entry.md: FAILED` + `WARNING: 1 computed checksum did NOT match`; exit **1** → the digest step reads `snapshot_tampered` |
| 4 | re-run the gate over the tampered copy; `cmp` against `snap-run.log` | exit **1**, stdout **byte-identical** (`cmp` clean) — measured: only the digest step turns this edit into `snapshot_tampered`; a stdout comparison alone would false-pass (standard §6 load-bearing point, re-measured on this gate) |
| 5 | gate-revision control: `cp tools/gates/provenance-audit.py gate-tampered.py; printf '\n# tampered gate byte\n' >> gate-tampered.py`; run over `snap2` | gate sha256 `1816a88c4b21f4666df1365fc9310a1f8ec17daca4db92273e027e1243234a77`, stdout byte-identical to `snap2-run.log` (exit 1) → only `gate_sha256` names the revision read |
| 6 | `grep -n "frozen\|argv" tools/gates/provenance-audit.py` (read) | the gate has **no internal `--frozen` digest mode** — consistent with standard §8; the interim external `sha256sum -c` is the check that ran, by this seat, as declared |

## 5. Negative controls: could-not-evaluate (exit 2) table

Independent controls over synthetic inputs in `~/.cache/prov-rerun/neg/`; the live tree is never
graded here. Each ran as `python3 tools/gates/provenance-audit.py <path>`.

| input | observed diagnostic (stdout) | exit |
|---|---|---|
| empty file | `CANNOT-EVALUATE: neg/empty.md: empty file` | 2 |
| non-UTF-8 bytes (`\xff\xfe\x00\x01bad`) | `CANNOT-EVALUATE: neg/bin.md: not UTF-8 text` | 2 |
| text with neither heading nor header line | `CANNOT-EVALUATE: neg/notanentry.md: not a corpus entry document (no Markdown heading, no header line)` | 2 |
| directory containing no `*.md` | `CANNOT-EVALUATE: neg/nomd: directory contains no *.md entry files`; scan `blocked=1` | 2 |
| missing path | `CANNOT-EVALUATE: neg/definitely-absent.md: not a readable file` | 2 |

- All five exit 2 with stable, distinct diagnostics; no case silently passes. This is the
  fail-closed surface the baseline's `expected.exit` codes must be read against.

## 6. Committed-baseline verification (the pair's deliverable)

- The author seat's baseline **landed at 2026-10-17T17:52:36-03:00** under
  `tools/gates/frozen/provenance-audit/r9-pre/` (`expected.json` 17:52; `inputs/` 20 files +
  `run.log` 17:52; `freeze.txt` 17:53). A first staging under
  `reports/round-9/baselines/provenance-audit/` was relocated to the frozen root before the freeze
  record and the reports-side copies were removed (author `freeze.txt`, "relocation note"), so the
  id `r9-pre` resolves under exactly one root; at verification time the reports directory holds
  only this seat's `rerun.md` and the author's `author.md` (landed 17:54:17).
- Poll history: a 15-second watcher over `tools/gates/frozen/provenance-audit/`,
  `tools/gates/expected/provenance-audit/` and `reports/round-9/baselines/provenance-audit/expected.json`
  hit at 17:52:36 — inside the ≤20 min poll rule.
- All checks below are this seat's own commands, run against the frozen root in out-of-repo
  scratch (`~/.cache/prov-rerun/`); no committed byte was edited at any point.

### 6.1 Verification results (all against `tools/gates/frozen/provenance-audit/r9-pre/`)

| # | check | command (sketch) | observed |
|---|---|---|---|
| V1 | input digests vs `expected.json.inputs` | Python re-hash loop over the 20 entries | **20/20 match, 0 mismatch** |
| V1b | snapshot vs live originals | per-file `sha256sum` snapshot vs live counterpart | 20/20 identical; the (then-existing) reports-side duplicate was also 20/20 identical; tree-manifest digest `7a865bc4…` on both trees |
| V2 | `gate_sha256` vs live gate | `sha256sum tools/gates/provenance-audit.py` | `8a96aaf4…` = declared |
| V2b | `revision_note` claim (gate bytes at the claims revision) | `git show e1694ba:tools/gates/provenance-audit.py \| sha256sum` | `8a96aaf4…` — identical at `e1694ba`, as claimed |
| V3 | verdict vs `expected` | re-run over a byte copy of `inputs/` (`~/.cache/prov-rerun/author-inputs`) | exit **1**; `INFO scan: files=20 marks=74 mark-lines=74 findings=6 blocked=0`; unique ID set = the 6 expected IDs; all 6 findings attributed to the defect fixtures only |
| V3b | `stdout_sha256` pin | `sha256sum run.log` vs declared | `26f21741…` = declared |
| V3c | normalized stdout equality | `diff` of `run.log` vs this seat's re-run, path prefix folded | **identical line-for-line**; display paths are the only difference |
| V4 | tamper on a scratch copy | append `\n<!-- tampered byte -->\n` to a copy of `inputs/corpus/knowledge/verification/calibration-registry.md`; re-hash | pinned `cf7cceee…` → observed `e3650182…` — **byte-identical to the author's recorded tampered digest**; digest step reads `snapshot_tampered` |
| V4b | tampered run vs `run.log` | gate over the tampered copy | still exit 1, stdout identical apart from the path prefix — only the digest step detects the edit |
| V5 | battery (R9-O15 extension) clean read | `python3 tools/check-gate-battery.py` → row `provenance-audit.py` | reading **`pinned`**; `inputs_checked: 20`; `gate_sha256` reading `match`; `stdout_pin` reading `match`; findings `[]` |
| V5b | battery tamper read on a scratch root | `python3 tools/check-gate-battery.py --baselines-root <scratch>/gates-battery/frozen` (one input tampered in the copy) | row reading **`snapshot_tampered`**, finding `BASELINE-TAMPERED` — never a silent pass |
| V5c | battery selftest | `python3 tools/check-gate-battery.py --selftest` | `SELFTEST OK 28/28 controls behaved as expected`, exit 0 |

- V5 note: the full battery over the live tree exited 2 at this sweep **only** because
  `myth-consistency-gate.py` and `naming-collision-gate.py` were still uncovered at that moment
  (`gates_uncovered` in its summary); all five landed baselines read `pinned`. That is a
  "baselines still landing" state, not a defect of this pair; the orchestrator's counting command
  re-runs the battery once all seven land.
- Verdict of §6: **the committed baseline reproduces, matches all its pins, and its frozen-run
  evidence is measurable and falsifiable at revision `a7bb205`** — subject to the limits of §9
  and the integration notes of §8. This seat found no drift, no mismatch, and no false pass.

## 7. Live-path context captured read-only (not evidence, standard §3)

- The fixture tree live path (not graded as evidence): exit 1, 6 IDs — matches §3/§4.
- Corpus context (all 13 `corpus/knowledge/verification/*.md`, read-only; the author seat's frozen
  snapshot turns out to pin exactly these 13 entries plus the 7 fixtures, so this table is the live
  measurement whose in-baseline reproduction is §6 V3): **all exit 0, 0 findings**;
  `INFO to-verify-count` marks by file: calibration-registry 7, citation-format-and-source-registry 10,
  costume-era-consistency-gate 4, gate-frozen-run-standard 0, internal-consistency-audit 6,
  lexicon-coverage-audit 2, myth-consistency-gate 3, naming-collision-gate 4, phonology-sanity-gate 0,
  provenance-audit-ledger-format 9, real-world-inspiration-boundaries 5, to-verify-triage-protocol 13,
  verification-method-overview 9.
- What this is not: it is not a frozen run; live files are mutable, so these numbers earn no
  conformance claim (standard §3).

## 8. Integration notes for the orchestrator (observed, not ruled)

- `.gitignore` line 3 is `*.log`; a committed `run.log` needs `git add -f` or the baseline
  commits without its verbatim stdout (filed independently by the costume-era author seat, the
  provenance author's `freeze.txt`, and this seat).
- Baseline homes across the wave (observed 17:54): `tools/gates/frozen/<gate>/r9-pre/`
  (handoff-packet-check, lexicon-coverage-audit, provenance-audit), `tools/gates/expected/<gate>/r9-pre/`
  (costume-era-consistency-gate, phonology-sanity-gate), and per-gate prose fragments under
  `reports/round-9/baselines/<gate>/` (`author.md` + `rerun.md`). The battery's discovery roots are
  exactly `tools/gates/expected/` and `tools/gates/frozen/` (`tools/check-gate-battery.py`
  `BASELINE_ROOTS`; observed 17:52:19) — a baseline staged only under `reports/round-9/baselines/<gate>/`
  is **not discoverable by the battery**. The provenance author relocated from the reports staging
  to the frozen root for exactly this reason (its `freeze.txt` relocation note), so the id resolves
  under one root and is discoverable. Recorded for the registry scribe / orchestrator to reconcile
  the two roots into one convention — not absorbed or decided here.
- Registry sweep staleness, observed: `reports/round-9/baselines/registry.md` line 226 still rows
  `provenance-audit | r9-pre | nothing landed at sweep time | to-verify | to-verify | pending` —
  superseded as of 17:52:36 by the landed baseline and the §6 results above; the row is the
  scribe's (or orchestrator's) to update, not this seat's, and it must not read as a live gap.
- No gate behavior was changed by this seat; the gate source was read only.

## 9. Calibration and limits

- A matching digest proves byte identity, not design quality; none of these runs admits the
  corpus, promotes a capability, or decides canon (lane `AGENTS.md`; standard §10).
- The verdict contract compared here is `expected.exit` + finding-ID **set**; stdout order and the
  advisory `stdout_sha256` are never the contract (standard §4).
- This seat's verdict: §2–§5 pass on the named revision; §6 is the pair's admission surface and is
  concluded above only against the author seat's committed baseline.
