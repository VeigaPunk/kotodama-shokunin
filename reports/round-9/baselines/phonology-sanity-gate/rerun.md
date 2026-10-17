# phonology-sanity-gate baseline — independent re-run (round 9, rerunner seat R9-O)

- role: **rerunner** — second worker of the `phonology-sanity-gate` baseline pair. This worker
  writes only this file (`reports/round-9/baselines/phonology-sanity-gate/rerun.md`). The author
  seat's bundle was measured at `tools/gates/expected/phonology-sanity-gate/r9-pre/`
  (`expected.json`, `packet.yml`, `run.log`, `freeze.txt`) — not under this directory; §7 records
  the measured location and the cross-shard root split. Nothing here was committed; the
  orchestrator integrates once per round.
- date: 2026-10-17, timestamps local (-03:00).
- lane revision at re-run start: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (`git rev-parse HEAD`).
  `reports/round-9/claims.json` names `baseline_revision: e1694bad…`; `git log --oneline` shows
  that is `e1694ba` (HEAD~1) and `git diff --stat e1694ba..HEAD` shows the only changed files are
  `reports/round-9/claims.json` (34 lines) and `reports/round-9/targets.json` (125 lines), 159
  insertions, 0 deletions — i.e. the graded artifact tree is identical between the declared
  revision and HEAD. Recorded, not assumed: the counted diff is the evidence.
- gate under test: `tools/gates/phonology-sanity-gate.py`,
  sha256 `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230`
  (`sha256sum tools/gates/phonology-sanity-gate.py`, 2026-10-17).
- fixture pair: `tools/gates/fixtures/phonology-sanity-gate.yml`
  sha256 `96dfa97e87c85a5c52145d6b9aa1b16572b2906b76ee6dee1591290a7ecb7421`;
  `tools/gates/fixtures/phonology-sanity-gate.expected`
  sha256 `165bcc61fe4f3d0478613ef691d39e71afae0f7b32c5cfc1b44f9a6e393a54c6`.
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4 (required
  `expected.json` fields), §5 (freeze procedure), §6 (verify procedure, tamper semantics, class
  mapping). Reading of this file is the two-evidences clause: self-test = capability, frozen run =
  measurement.

## 1. Environment limit measured during this re-run (affects where evidence could live)

- `/tmp` was **inode-exhausted** for the whole run: `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp`;
  `mkdir -p /tmp/r9-phon-rerun` → `mkdir: cannot create directory '/tmp/r9-phon-rerun': No space
  left on device` (2026-10-17T17:48-03:00). The by-volume check disagrees (`df -h /tmp` → 8.5G
  avail), so the failure is inode pressure, consistent with a 64-worker wave, not a full disk.
  Status: **environment hazard observed, not a blocker for this seat** — every command below ran.
- Scratch was therefore moved inside the lane repo: `.scratch/r9phon/` (untracked, on `/home`,
  782G available per `df -h /home`). The live tree outside it was never modified (see §3 post-run
  digest check and §7). Note added after the run: the whole `.scratch/` tree was then removed
  wave-side mid-run (~18:05), so the paths below are historical command locations, not surviving
  artifacts — every observed result is recorded inline here (§8 records the hazard).
- Consequence for the pair: the author seat may hit the same ENOSPC if it freezes under `/tmp`;
  a freeze that reported success there should be re-checked (the author seat's own fragment records
  the same ENOSPC and a `.scratch/`-based workaround, consistent with this measurement).

## 2. Capability re-executed: `--selftest` in an isolated mirror (not the live tree)

The gates tree was mirrored first, so the self-test could not touch the live fixtures:

| # | Command (2026-10-17T17:48:41-03:00) | Observed |
|---|---|---|
| 1 | `cp tools/gates/phonology-sanity-gate.py .scratch/r9phon/mirror/tools/gates/` + `cp tools/gates/fixtures/phonology-sanity-gate.{yml,expected} .scratch/r9phon/mirror/tools/gates/fixtures/` | copied; `cmp` against the live originals → byte-identical (`MIRROR_BYTE_IDENTICAL_TO_LIVE`); mirror digests equal the live digests in the header |
| 2 | `python3 tools/gates/phonology-sanity-gate.py --selftest` (cwd = mirror) | `selftest: fixture exit 1; 15/15 planted finding IDs present; 29 control cases passed`; exit **0** |

- This re-executes capability only. It says nothing about any real packet, and per the standard §2
  it never substitutes for the frozen run.

## 3. Measurement over a snapshot this seat minted itself (byte copy of the committed fixture)

Purpose: establish, independently of the author seat, that a byte-frozen copy of the committed
fixture produces the committed verdict, and that the gate is read-only over its input.

| # | Command (cwd = `.scratch/r9phon/pre/`) | Observed |
|---|---|---|
| 1 | `cp …/mirror/tools/gates/fixtures/phonology-sanity-gate.yml packet.yml` | copy |
| 2 | `sha256sum packet.yml \| tee digests.sha256` | `96dfa97e…7421  packet.yml` — equal to the live fixture digest |
| 3 | `sha256sum -c digests.sha256` | `packet.yml: OK`, exit 0 |
| 4 | `python3 mirror/tools/gates/phonology-sanity-gate.py packet.yml > run.log 2> stderr.log` | exit **1**; 16 `FINDING` lines; stderr 0 bytes |
| 5 | unique-ID set vs the committed `tools/gates/fixtures/phonology-sanity-gate.expected` (both `sort -u`, then `diff`) | **empty diff — identical, 15/15 IDs**: A-CLASS, A-NEUTRAL, A-ORDER, A-PARSE, A-TONE, I-DUPLICATE, I-UNKNOWN, M-EJECT, M-NASAL, M-ROUND, M-SONORITY, M-VOICE, T-C, T-SYL, X-NAME |
| 6 | `sha256sum run.log` (advisory whole-output pin only, standard §4) | `b3843b2a5f50809ffe43fd55212cb9ab320f4ac98c2a59c6f57c7bcc61617018` |
| 7 | `sha256sum -c digests.sha256` again, after the run | `packet.yml: OK` → the gate did **not** rewrite its input (read-only over the graded file) |

- Line-count detail: 16 `FINDING` lines carry 15 distinct IDs because `I-UNKNOWN` fires twice on
  `notable_rules[3] 'q → k / _u'` (rewritten token `q` absent; environment token `u` absent). The
  frozen-run contract compares **sets** (standard §4), so 15 IDs is the verdict, not the 16 lines.

## 4. Tamper semantics reproduced on this gate

Everything was done on a throwaway copy; no committed or frozen byte was edited.

| # | Command (cwd = `.scratch/r9phon/`) | Observed |
|---|---|---|
| 1 | `cp pre/packet.yml tamper-packet.yml && printf '\n# tampered byte\n' >> tamper-packet.yml` | copy with one appended comment line |
| 2 | `sha256sum -c tamper-digests.sha256` (digest file points at `tamper-packet.yml`) | `tamper-packet.yml: FAILED` + `WARNING: 1 computed checksum did NOT match`; exit **1** → the digest step reads `snapshot_tampered` |
| 3 | `python3 mirror/tools/gates/phonology-sanity-gate.py tamper-packet.yml > tamper-run.log` | exit **1**, and `diff` of the `FINDING <id>:` lines against the untampered run → **empty** (`FINDINGS_UNCHANGED_BY_TAMPER`) |

- This is the standard's §6 load-bearing point re-measured on this gate: a tampered input yields
  the *same verdict*, so an orchestrator comparing only stdout would call it a match. Only the
  digest check turns it into `snapshot_tampered` (could-not-evaluate). The phonology gate has no
  internal `--frozen` mode (`grep -n "frozen\|argv\|--selftest" tools/gates/phonology-sanity-gate.py`
  → only the `--selftest`/`--self-test` and packet/stdin paths), so the interim external
  `sha256sum -c` is the check that ran, exactly as the standard §8 table declares.

## 5. Live-packet verdict captured for context (not a baseline)

The standard §9 names the D2 culture packet as the intended first real input. Captured read-only
so the author seat's choice of snapshot can be read against a measured live verdict:

- input `examples/culture-d2/packet.d2.yml`, sha256 `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` (2026-10-17).
- run → exit **1**, 3 `FINDING` lines, all one ID: `A-NEUTRAL`
  (`notable_rules[1] 'n → m / _ p'`, `[2] 'n → m / _ b'`, `[7] 's → h / _ #'`).
- input digest re-checked after the run → `OK` (read-only).
- What this is **not**: it is not a frozen run — the file is mutable and untracked-by-baseline, so
  it earns no conformance claim; it is context for §7 only. A verdict captured over a live path is
  exactly what standard §3 forbids as evidence.

## 6. Additional independent checks (no author-seat dependency)

### 6.1 Input-surface completeness — is `{"packet.yml": <sha>}` a complete `inputs` map for this gate?

- Claim tested: in a normal (non-selftest) run this gate reads exactly one file — the packet given
  as `argv[1]` — so a baseline whose `inputs` map lists only the snapshot is complete, and a
  baseline that lists more would be over-claiming.
- Evidence: `grep -n "open(\|Path(\|read_text\|read_bytes\|os.path.join\|FIXTURE_PATH\|EXPECTED_PATH"
  tools/gates/phonology-sanity-gate.py` (2026-10-17) → three `open(` sites total: two inside the
  selftest's pin/regen helper (`tools/gates/phonology-sanity-gate.py:1277` read, `:1282` atomic
  write) and one in the packet reader (`:1358`, `with open(path, encoding="utf-8") as handle`).
  `FIXTURE_PATH`/`EXPECTED_PATH` (`:118`–`:119`) are referenced only from the `--selftest` paths
  (`:1299`–`:1307`); the usage text (`:1350`) accepts one packet path or `-`.
- Reading: no corpus, fixture, config or environment file is read in normal mode, so for this gate
  the `inputs` map needs exactly the snapshot entry. Measured under gate sha256 `d5fe087f…`;
  any gate edit invalidates this reading (standard §6 step 2, `gate_revised`).

### 6.2 Deterministic re-execution over the same bytes

| # | Command (cwd = `.scratch/r9phon/`) | Observed |
|---|---|---|
| 1 | `cp examples/culture-d2/packet.d2.yml d2-copy-a.yml; cp d2-copy-a.yml d2-copy-b.yml` | two byte-identical private copies |
| 2 | run the mirrored gate over `d2-copy-a.yml`, then over `d2-copy-b.yml` | `EXIT_A=1 EXIT_B=1` |
| 3 | `sha256sum d2-a.log d2-b.log; cmp d2-a.log d2-b.log` | both `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2`; `cmp` clean → **deterministic, byte-identical stdout** |

- Relevant to freezing: identical bytes give an identical verdict, so a recorded `stdout_sha256`
  is a checkable advisory pin (standard §4), not a flaky one.

### 6.3 Exit-2 class exercised (`could-not-evaluate`, never a silent pass)

| # | Input (private, in scratch) | Observed |
|---|---|---|
| 1 | `printf 'name: broken\nphonology: [not, a mapping\n' > malformed.yml` then run the gate | `FINDING G-DATA: UNEVALUABLE — packet could not be parsed: unterminated flow sequence: '[not, a mapping'`; exit **2** |
| 2 | `printf 'name: no-phon-block\nlexicon: []\n' > no-phon.yml` then run the gate | `FINDING G-DATA: UNEVALUABLE — no usable 'phonology' mapping in the packet — nothing to evaluate`; exit **2** |

- Reading: an unusable snapshot surfaces as exit 2 / `could-not-evaluate` on this gate, so the
  frozen-run mapping “malformed → could-not-evaluate, never a clean pass” (standard §6 table row 6)
  holds for the two shapes a baseline snapshot is most likely to take.

## 7. Committed-baseline verification — the pair's deliverable (executed)

**Where the bundle actually landed** (measured, not assumed): the author seat froze it under
`tools/gates/expected/phonology-sanity-gate/r9-pre/`, **not** under
`reports/round-9/baselines/phonology-sanity-gate/` (where this seat's fragment lives and where I
polled first for 20 minutes). The standard §3 names yet a third root, `tools/gates/frozen/…`.
Sweep: `find tools/gates/expected tools/gates/frozen reports/round-9 -maxdepth 3 -name r9-pre` →
`costume-era-consistency-gate` and `phonology-sanity-gate` under `tools/gates/expected/`;
`lexicon-coverage-audit`, `handoff-packet-check`, `provenance-audit` under `tools/gates/frozen/`.
No second `r9-pre` exists for this gate, so this gate's id is **unambiguous** (standard §3's
fail-closed resolution is not triggered) — but three roots are in flight across the round's shards.
That is a cross-shard layout observation, reported here for the integrator/registry, never absorbed.

Bundle files, digests measured 2026-10-17T18:06-03:00:

| file | measured sha256 | pin inside `expected.json` |
|---|---|---|
| `packet.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | `inputs.packet.yml` → match |
| `run.log` | `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` | `stdout_sha256` → match |
| `expected.json` | `2763614ff26959e6b7fa7d96471e8d5e9e93616e37d47e3f0bec99b5caa62cde` | — (the pin file itself) |
| `freeze.txt` | `61a0873ed5647c8022dd7866a86ed84539e63e5af820a6f9123d1cfd96da85cd` | — (narrative only) |

Verification in the standard's §6 order — all runs over a **private copy**; the committed bytes were
never written to:

| # | check | observed |
|---|---|---|
| 1 | `expected.json` parses; `schema` `kotodama-frozen-run-v1`, `gate` `phonology-sanity-gate`, id `r9-pre`, `revision` `e1694bad…`, `frozen_at` `2026-10-17T17:50:33-03:00` | as declared |
| 2 | digest check: sha256 of every `inputs` entry against the committed bytes | `INPUT packet.yml pin=e0f21509e14ac03e got=e0f21509e14ac03e OK` → **digests match** |
| 3 | gate-revision check: `gate_sha256` vs `sha256sum tools/gates/phonology-sanity-gate.py` | `d5fe087f…34230` = `d5fe087f…34230` → match (re-measured three times across the run, unchanged) |
| 4 | re-run the gate over the private copy of the committed snapshot | `OBSERVED_EXIT 1` = `expected.exit 1`; `OBSERVED_IDS A-NEUTRAL` = `expected.findings` → **compared verdict, match** |
| 5 | advisory stdout pin | fresh stdout sha256 `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` = `stdout_sha256`; the committed `run.log` digest is the same → `run.log` is the verbatim stdout of this command |
| 6 | tamper (standard §6 step 1): append `\n# tampered byte\n` to the copy | copy sha256 `265bd5c6…`, ≠ pin → `TAMPER_DIGEST_DETECTS True` (`snapshot_tampered`, could-not-evaluate); the gate over the tampered copy printed **byte-identical** stdout (`TAMPER_EXIT 1`, same 3 lines) → only the digest step detects the edit |
| 7 | live-origin equivalence | `examples/culture-d2/packet.d2.yml` sha256 `e0f21509…` = frozen `packet.yml`, `cmp` clean (`FROZEN_COPY_EQUALS_LIVE_ORIGIN_NOW`) → the origin has not drifted since the 17:50 freeze |

Controls this seat re-executed on its own bytes instead of accepting the author's word — both
author-claimed digests reproduced exactly:

| control | author's claim | this seat's independent re-execution |
|---|---|---|
| clean class reachable | `CLEAN_PACKET` sha256 `36be6604…`, exit 0, 0 stdout bytes | extracted `CLEAN_PACKET` from the gate module myself → sha256 `36be66044aa2c0a1e103413816af96bc42f500cfc3da1c7bf8d538d50ce8fe8e` (**equal**); run → exit 0, 0 stdout bytes |
| verdict comparison sensitive | mutant `tones: 0 → 6`, sha256 `40a71dbe…`, observed `{A-NEUTRAL, T-TONE}` | made the same mutation independently on my own copy → sha256 `40a71dbe085032a91dcf058f922708a1470b40115398e55ae0ef148c5f88a39d` (**equal**); observed `{A-NEUTRAL, T-TONE}` ≠ pin → mismatch reported, never a silent pass |
| gate-revision control | gate copy + one comment byte → stdout byte-identical | gate copy `a5dd71c9…` run over the frozen snapshot → exit 1, stdout sha256 `1ce5f0cd…` = pin → only `gate_sha256` names the gate revision read |
| path independence | mirror run in another cwd | reproduced in §6.2 (mirror) and step 4 above (private copy) — same stdout sha256 |

**Result: the pair's committed baseline is verified.** Digests match, gate revision matches, observed
exit and finding-ID set equal the pins, the advisory stdout pin holds, a one-byte edit reads
`snapshot_tampered`, and the four author-claimed controls reproduce on independent bytes. Standard
§6 reading: **compared verdict, match** — `findings`, exit 1.

Cross-seat agreement worth naming: §5's live-path verdict and §6.2's determinism digest were measured
**before** this bundle was read, and equal its pins (`e0f21509…`, `1ce5f0cd…`) — two seats, two
scratch trees, same bytes.

## 8. Limits, hazards, and what this seat did not do

- **Scratch wipe (environment hazard, recorded).** The entire untracked `.scratch/` tree was removed
  by something outside this seat around 2026-10-17T18:05-03:00 — my mirror, pre-flight copies and
  first verifier script disappeared mid-run (`ls .scratch/` → `No such file or directory`). No
  committed or frozen byte was affected; the wipe is why every command above is recorded in this
  file rather than merely pointed at in scratch. A seat that leaves its only evidence in `.scratch/`
  can lose it silently.
- **Not done here (out of this seat's assignment).** The gate battery and its baseline-validation
  extension are R9-O15's (the extension is visibly in flight: `tools/check-gate-battery.py:113–114`
  now define `BASELINE_SCHEMA`/`BASELINE_ROOTS = (expected, frozen)`, which is what makes the
  author's root admissible). No gate behavior was changed by this seat — control:
  `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355 -- tools/gates` → empty,
  `git status --porcelain -- tools/gates` → only untracked baseline directories.
- **Unverified by this seat:** the author's freeze-time transcripts beyond the controls re-executed
  above (e.g. their three reruns), and anything about the D2 packet's design quality — a frozen run
  proves bytes and a verdict, never truth (standard §10). Nothing in §7 is marked `to-verify`.
- **Files this seat wrote:** `reports/round-9/baselines/phonology-sanity-gate/rerun.md` only;
  `.scratch/r9phon/` was throwaway and is removed at the end of this seat. Bundle, gate, fixtures and
  every other round-9 fragment were left untouched.
