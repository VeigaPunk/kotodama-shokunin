# R10-F19 — independent drift audit (kotodama-shokunin, round 10)

- seat: R10-F19 (freshness auditor). Assignment: independently re-run >=10 of
  the drift ledger's commands; mismatches against the ledger are findings.
  This file is the seat's only write; no SKILL.md, SCORECARD, corpus, tool,
  fixture, ledger or filed-report byte was written by it.
- date: 2026-10-17, measurement window `2026-10-17T21:27Z`–`21:39Z` (UTC),
  local UTC-03:00. Live HEAD at audit: `e3a1ec9435787328ac9f828f96cb6390e4916b8f`;
  round baseline `9dc18ec1…`.
- ledger snapshots compared: `reports/round-10/drift/ledger.json` at
  sha256 `baa9365b…` (146 rows, 21:32:58Z), at
  sha256 `5abe8c1c16c7bcec5b47a8dbca3b087907af467951132497f394151f26bc0da8`
  (150 rows, 21:38Z), and at audit close sha256 `765833ebbb3e9775…` (189 rows,
  21:41Z). The ledger is a moving target this round (122 → 146 → 150 → 189 rows
  during the audit); every row cited below was re-checked against the 150-row
  snapshot, and the two defects in §5 were re-checked against the 189-row one.
- isolation: `export TMPDIR=$PWD/.scratch` for every command (`/tmp` remains
  inode-exhausted, `df -i /tmp` → 100%). Four disposable mirrors were used:
  `.scratch/f19/iso`, `iso2`, `iso3`, `iso4` (full tree minus `.scratch`/PDFs),
  plus two minimal trees `iso-replay` and `iso5` (pins only). Raw receipts:
  `.scratch/f19/runs.jsonl` (42 entries) and `.scratch/f19/out/*.{out,err}`;
  scratch is untracked, disposable evidence, not a deliverable.

## 1. Independent re-runs — 28 commands, all ledger-overlapping rows checked

Every command below was run by this seat, not copied from a shard. "Ledger"
names the rows that carry the same command and their verdicts; "agreement"
compares my observed exit code and stdout sha256 against them.

| # | command | my exit | my stdout sha256 (prefix) | ledger rows / verdicts | agreement |
|---|---|---|---|---|---|
| 1 | `python3 tools/d2-typed-labels.py --selftest` | 0 | `7231139c5b060898` | 5 rows, `current` | byte-identical |
| 2 | `python3 tools/assemble-d2.py --check` | 0 | `2fa0c8c197459f54` | shard-10, shard-13 `current` | byte-identical |
| 3 | `python3 tools/assemble-d2.py --selftest` | 0 | `a81294c0347660d9` | shard-10, F15 `current` | byte-identical |
| 4 | `python3 tools/assemble-culture-d3.py --check` | 0 | `e20620fabdf28532` | shard-13 `current` | byte-identical |
| 5 | `python3 tools/assemble-culture-d3.py --selftest` | 0 | `91a0653948d48a10` | **absent from ledger** | finding, §5.1 |
| 6 | `python3 tools/check-evidence-coupling.py --selftest` | 0 | `cf62bc50e303b793` | F15 `current` | byte-identical |
| 7 | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | `e282a06884980341` | F15 `current` | byte-identical |
| 8 | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | 0 | `e282a06884980341` | F15 `current` | byte-identical |
| 9 | `python3 tools/check-craft-exercise.py --selftest` | 0 | `77d408e10a494fa5` | shard-10/11, F15 `current` | byte-identical |
| 10 | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 | `18128adfc703fd26` | shard-10/11, F15 `current` | byte-identical |
| 11 | `python3 tools/check-gate-battery.py` | 2 | `68453458cb0db0f5` | shard-09 `current`; shard-10/11, F15 `stale-documented` | exit agrees; hash path-dependent, §2 |
| 12 | `python3 tools/check-gate-battery.py --selftest` | 0 | `8b1fdd6f2d316ef2` | shard-10/11/13, F15 `current` | byte-identical |
| 13 | `python3 tools/replay-frozen.py --selftest` | 0 | `4d6aaea127ad9973` | shard-09/10, F15 `current` | byte-identical |
| 14 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | `76c00a6b80d4539a` | shard-09/10/11 `stale-documented` | byte-identical, §3 |
| 15 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 2 | `409db5ab8b68ebc3` | shard-09/11 `stale-documented` | byte-identical |
| 16 | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 0 | `c83dac8f8bab0fea` | shard-13, F15 `current` | byte-identical |
| 17 | `python3 tools/source-audit-inventory.py --selftest` | 0 | `45e77ea19f4c3a52` | shard-10, F15 `current` | exit agrees; hash path-dependent, §2 |
| 18 | `python3 tools/gates/naming-collision-gate.py --selftest` | 0 | `d3566a9cad69f956` | shard-10 `current` | byte-identical |
| 19 | `python3 tools/gates/naming-collision-gate.py tools/gates/fixtures/naming-collision-gate.yml` | 1 | `bea0fd3925c2745e` | shard-10, F15 `current` | byte-identical |
| 20 | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | 0 | `7c5810479045c26b` | F15 `current` | byte-identical |
| 21 | `python3 tools/gates/handoff-packet-check.py tools/gates/fixtures/handoff-packet-check.md` | 1 | `ec1ec331a820f5ea` | shard-10, F15 `current` | byte-identical |
| 22 | `python3 tools/harness/r8_checks.py --selftest` | 0 | `25bf2315e6c2f340` | F15 `current` | byte-identical |
| 23 | `python3 reports/round-5/run-validation.py` | 1 | `23cf694c42d137f9` | shard-11, F15 `stale-documented` | exit agrees; hash state-dependent, §2 |
| 24 | `python3 reports/round-6/run-validation.py` | 1 | `79440ea7395873dd` | F15 `stale-documented` | byte-identical |
| 25 | `python3 reports/round-7/run-validation.py` | 1 | `e9b7dff1f3da4db3` | F15 `stale-documented` | exit agrees; hash state-dependent, §2 |
| 26 | `python3 reports/round-8/run-validation.py` (pre-repair tree) | 1 | `b2fb989333a06f0c` | shard-13 `stale-fixed` | byte-identical, §4 |
| 27 | `python3 reports/round-8/run-validation.py` (post-repair tree) | 0 | `4d300b24a04ff44a` | shard-13 row is the pre-repair observation | fixed, §4 |
| 28 | `python3 reports/round-9/run-validation.py` | 0 | `4d300b24a04ff44a` | shard-13, F15 `current` | byte-identical |

The SCORECARD round-5 counting command was also re-run independently:
`python3 -c 'import json; a=json.load(open("reports/round-5/availability-attempt-1.json")); d=json.load(open("reports/round-5/dispatch.json")); print(a["requested_workers"],a["launched_workers"],a["completed_workers"]); print(d["workers"],d["completed"],d["actual_executed_batches_after_authorization"])'`
→ `16 0 0` / `16 16 1`, exit 0, stdout sha256 `19b98ffbe56449bd`; no ledger row
was found for this one (the ledger covers SKILL.md/SCORECARD rows it sharded;
this one-liner is not among them).

Gates covered by the re-runs, named so the registry match is on the record:
`costume-era-consistency-gate` (named in the round-9
`reports/round-9/baselines/registry.md` and shard-14, not re-run directly by
this seat), `handoff-packet-check`, `lexicon-coverage-audit` (registry/shard-14),
`myth-consistency-gate` (registry/shard-14), `naming-collision-gate`,
`phonology-sanity-gate` (registry/shard-14), `provenance-audit` (registry §2
sha `8a96aaf4…`, shard-06 ran it live). The registry.md re-measurement itself
is shard-14's artifact; this audit only confirms that its quoted live gate
stems and hashes are consistent with what the re-runs above show.

## 2. Every hash divergence, attributed — zero unexplained

Four commands produced different stdout hashes than some ledger rows. Each is
a property of the command, not of the surface under test, and was reproduced
on demand in the same tree:

- `python3 tools/check-gate-battery.py` — its JSON embeds the random mirror
  path (`mirror.root … .scratch/gate-battery-<random>`). Two consecutive runs
  in the same mirror gave `59c86a38a71a15b2` then `6e0e666129397eba`; the
  ledger's four rows differ from each other for the same reason
  (`6fd828d3`, `3109467a`, `f456f79d`, `8bf71a02`). Exit was 2 in every run,
  with the same summary (`pass 7 / fail 0`, `gates_uncovered [myth, naming]`).
- `python3 tools/source-audit-inventory.py --selftest` — its output names the
  random scratch dir (`source-audit-inventory-cli-<random>`). Two consecutive
  runs gave `1269f45d0a033d45` then `a9942756778372e7`, exit 0 both. The two
  ledger rows (`ecb68511`, `e06fde07`) differ for the same reason.
- `python3 reports/round-5/run-validation.py` — its failure text embeds the
  full battery JSON above, including the random mirror path; my run and both
  ledger rows (`2e7d8c0f`, `b40866b9`) share exit 1 and the same failure
  strings (`non-append corpus edit (ottoman.json, OTT-06)`; battery expected 0
  got 2).
- `python3 reports/round-7/run-validation.py` — its failure text embeds the
  live knowledge inventory totals, which moved as round-10 coverage entries
  landed: my iso2 run read `files: 180`, my iso4 run (minutes later) read
  `files: 185`, the ledger's run another value. Exit 1 in all runs, same
  failure set (`append-only prefix lost: SKILL.md`; historical totals changed;
  the duplicate-parent-receipt control), `O_passed: true` in all.

Verdict: no command diverges from the ledger in exit code or in meaning, and
zero unexplained mismatch remains.

## 3. Round-3 frozen replay — headline item, independently reproduced

- Live tree, this seat: exit 2, stdout sha256
  `76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80`,
  seven rows `could-not-evaluate` with `gate_digest_mismatch`
  (byte-identical to shard-09/10/11 rows; my run of the same command in an
  isolated copy produced the same bytes, so the reading is not a copy artifact).
- Cause measured, not assumed: the manifest's `gate_sha256` pins equal the
  gate bytes at `291c714` and `c610e0a` and `cf338a7` (all six gates; e.g.
  phonology pin `fb05c644cafb` = `git show 291c714:…`), while `e1694ba`
  (round-8 admission) rewrote all six gate files (+596/−73 lines).
- The fix-18 recipe was verified by this seat: restoring the six gates from
  `291c714` into an isolated tree and running
  `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <isolated-tree>`
  → exit 0, `{"rows": 7, "reproduced": 7, "mismatch": 0, "could_not_evaluate": 0}`.
  The recipe now standing in `SKILL.md:162` (fix-18) matches this evidence.
- The complementary negative was also measured: restoring gates from today's
  HEAD in the same isolated harness reads exit 2 with all seven rows
  `could-not-evaluate` — i.e. the old "restore from HEAD" assumption cannot
  work after `e1694ba`, which is exactly the repair fix-20 makes (§4).

## 4. Round-8 runner repair — pre/post verified, and its audit consequence

- Pre-repair: `python3 reports/round-8/run-validation.py` → exit 1, stdout
  sha256 `b2fb989333a06f0c095731fcb5e77e7843b442a14d41156f9fee4f37bc66781e`
  (claim F PASS, claim O PASS, claim D FAIL), byte-identical to the ledger's
  shard-13 row.
- Post-repair (fix-20's `gate_blob_for_pin` edit, measured by this seat in a
  fresh mirror): exit 0, stdout sha256 `4d300b24a04ff44afd89c6944174ad8f71056667fd0e5f2044266010943b2f5`,
  `claim F: PASS / claim O: PASS / claim D: PASS`. That hash equals the
  round-9 runner's hash in the table above because both commands now print the
  same four lines; the files were compared and are byte-identical, so the
  shared digest is text equality, not a copy of one run into the other's row.
- Observation for the ledger scribe: the command's green reading now depends
  on the round-10 repair of a round-8 runner. The repair is documented in
  `reports/round-10/drift/fix-20.md` and is transparent (the docstring states
  the round-10 change), but the historical claim "round-8 acceptance exits 0"
  is reproducible today only through that repaired resolution logic. This is
  recorded here so the acceptance reading is not mistaken for an unchanged
  historical artifact.

## 5. Ledger defects found by this audit (actionable)

### 5.1 Ledger misses one required command (35/36)

Using the round-10 acceptance runner's own extraction
(`reports/round-10/run-validation.py`, `extract_cited_commands` over SKILL.md
and SCORECARD.md) against the 150-row ledger: 36 command keys are required,
35 are covered, and the one missing key is
`('tools/assemble-culture-d3.py', --selftest)`, cited at `SKILL.md:264` (the
D3 table's self-test cell). The ledger carries only
`python3 tools/assemble-culture-d3.py --check`. This seat ran the missing
command: exit 0, stdout sha256 `91a0653948d48a10f6bd84af7adb3dd4cda3b25e8a15a77a3bf2cd92a4deac2b`,
deterministic (identical in two mirrors). Until the scribe adds the row, the
round-10 acceptance runner's F leg will fail with
"ledger covers 35/36 cited commands".

### 5.2 `stale-fixed` rows carry no evidence key

At the 150-row snapshot, row 113 (`python3 reports/round-8/run-validation.py`,
shard-13) was the only `stale-fixed` row, and it had none of the evidence keys
the runner accepts (`fix`, `fix_evidence`, `fixed_in`, `evidence`); its note
only said "pre-fix observation". At audit close (189-row snapshot
`765833eb…`) the fixers' own rows had been appended and there are now ten
`stale-fixed` rows, and **none of the ten carries one of those four keys**:
rows 42 (fix-16), 61/62 (fix-18), 67/68/69 (fix-19), 98 (fix-21), 113
(shard-13), 131 (fix-20), 176 (fix-17). The runner's own check reads
"stale-fixed without demonstrated fix evidence" for each unless a fix path
(e.g. `reports/round-10/drift/fix-20.md`) is added to the row. This is the
highest-volume ledger defect this audit found; it is mechanical to repair
(add the key), but it must be repaired before the acceptance runner reads the
ledger.

### 5.3 Moving target (recorded, not a defect)

The ledger grew 122 → 146 → 150 rows during this audit and `SKILL.md` was
edited in-round by the stale-fixers (fix-16/17/18/19/21; whole-file sha256
`2bce468d…` before → `751675dd…` at audit close). All row comparisons above
were re-checked against the 150-row snapshot `5abe8c1c…`; any row added after
it was not audited by this seat.

## 6. Verdict

- Re-runs: 28 commands, covering all seven live gate scripts' surfaces that
  have commands, both legacy manifests, the battery, the replay tool, the
  inventory probe, the harness selftest and the five round-scoped acceptance
  runners.
- Against the ledger: exit codes agree on every overlapping row; stdout hashes
  agree byte-for-byte on 21 commands; the remaining four differ only by
  documented path/state dependence (§2). Zero unexplained mismatch.
- Two ledger defects are handed to the scribe: the missing D3 selftest row
  (§5.1) and the evidence-less `stale-fixed` row (§5.2).
- No live-tree byte was written by this seat; all scratch under
  `.scratch/f19/` is disposable and untracked.
