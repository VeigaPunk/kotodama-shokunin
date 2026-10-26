# MutLandedCa — wave 2, attack on the landed claim-Ca bytes (hyaku run 7)

Seat: MutLandedCa (leaf, no delegation). Target: claim Ca as landed at
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`, counter
`reports/round-74/accept-ca.py` (self sha256 `8052f1e25c36…`), freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`, fleet root
`/home/vgpnk/Projects/shokunin`. No installs were needed; none were made
(operator tooling authorization unused, pacman untouched).

## Method

All work in a disposable clone (scratch `/tmp/MutLandedCa/`):

```
D=/tmp/MutLandedCa/c0; git init -q "$D" && git -C "$D" rev-parse --show-toplevel   # -> $D
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
git -C "$D/lane" checkout -q --detach
git -C "$D/lane" branch -f main 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
git -C "$D/lane" checkout -q main
```

The counter reads committed bytes only (it materializes its own clone at
`--lands`), so each mutant was **committed** in the clone with `main` on the
mutant commit and `--lands <mutant>`; after each run
`git reset -q --hard 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` restored the
bytes. Run command per mutant:

```
python3 -B reports/round-74/accept-ca.py --root . --lands <mutant> \
  --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 \
  --fleet-root /home/vgpnk/Projects/shokunin
```

**Baseline (pristine lands): `ACCEPT-CA-74: PASS legs=11/11`, exit 0**
(all legs PASS; ledger sha256 `88d5fd522c86…`, source=freeze; 13 pairs,
LC-09 the only REPAIR; receipts re-executed at `2d1cd9140d3a`).

## Mutation table

| mutant | attack (committed byte change) | leg expected | leg fired (raw counter detail) | survived |
|---|---|---|---|---|
| M1 | LC-01 row new token `804`→`805` (SCORECARD.md:1442) | ANNOTATE | ANNOTATE `unannotated=1 ["LC-01(row-leading-LC-01 stated='412' observed='804')"]` + NOSTUB `stubs=['LC-01:new-token']`; FAIL 9/11 | N |
| M2 | delete the LC-01 row | ANNOTATE | ANNOTATE `unannotated=1 ["LC-01(…)",]` + NOSTUB `stubs=['LC-01:no-leading-row']`; FAIL 9/11 | N |
| M3 | strip id from LC-15 row (starts `\| 776 \| 724 \|`) | ANNOTATE/NOSTUB | ANNOTATE `unannotated=1 ["LC-15(…776…724…)"]` + NOSTUB `stubs=['LC-15:no-leading-row']`; FAIL 9/11 | N |
| M4 | delete base-present SCORECARD.md:50 | APPENDONLY | APPENDONLY `problems=['protected-removed=1 19→1 SCORECARD.md']`; FAIL 10/11 | N |
| M5 | in-place edit base LOG.md:100 (`manual`→`manua1`) | APPENDONLY | APPENDONLY `problems=['protected-removed=1 1→1 LOG.md …']`; FAIL 10/11 | N |
| M6 | SKILL.md:594 repaired `95 entries: 93`→`94 entries: 92` | REPAIR | REPAIR only: `green=[] red=["LC-09(statement='94' truth='95')"]`; APPENDONLY stayed green (594 is the allowed REPAIR line); FAIL 10/11 | N |
| M7 | in-place edit SKILL.md:592 (`calibration`→`calibratlon`), outside all REPAIR stated_at lines | APPENDONLY | APPENDONLY `problems=['SKILL.md: changed lines outside REPAIR stated_at lines [592]']`; FAIL 10/11 | N |
| M8 | append line to inherited `.ufo/waves/round-73/w2/CritEntryAmendFinal.md` | TRACKED | TRACKED `problems=['…CritEntryAmendFinal.md blob id differs between freeze (d219fca4a80e) and lands (c37c1a47bd2a)']`; FAIL 9/11 (RECEIPTS also flagged — see F2, spurious) | N |
| M9 | one digit in receipt `accept-ca-73-at-lands.txt`: `legs=9/9`→`legs=9/8` | RECEIPTS | RECEIPTS `problems=[… "accept-ca-73-at-lands.txt: does not carry 'ACCEPT-CA-73: PASS legs=9/9'", "… committed stdout differs from the re-run (925f885ce510 vs 55544779204d)" …]`; FAIL 10/11 | N |
| M10 | `git rm` the receipt | RECEIPTS | RECEIPTS `problems=['receipt reports/round-74/telemetry/accept-ca-73-at-lands.txt is not committed at lands']`; FAIL 10/11 | N |
| M11 | add row under `## Corrections — round 74`: `\| LC-99 \| 0 \| 4 \| cat corpus/knowledge/culture-material/worldbuilding-setting-practice.md \|` | SEPARABLE | **none — `ACCEPT-CA-74: PASS legs=11/11`, exit 0** | **Y** |
| M12 | edit committed `reports/round-74/ledger.json` at lands (`"round": 74`→`75`) | FROZENCFG | FROZENCFG `problems=1 ['reports/round-74/ledger.json was edited in the graded tree after freeze (91919e926cc8 != 5acd937797f1)']`; FAIL 10/11 | N |
| M13 | lands-ledger copy with LC-01 `observe_cmd` → `["python3","-c","print('804')"]` | FROZENCFG; LEDGER guard via selftest | FROZENCFG `problems=1 ['…edited in the graded tree after freeze (91919e926cc8 != fa8736289d29)']`; LEDGER stayed green `pairs=13 min=10 source=freeze` (graded-tree copy never evaluated). LEDGER guard proven separately by the counter's selftest on pristine bytes: `selftest: interpreter -> exit=1 LEDGER=FAIL` (likewise `shell-string`, `constant-printer`, `out-of-clone`, `dead-pin`). FAIL 10/11 | N |

Selftest corroboration of the frozen controls (pristine run, `--selftest`):
`do-nothing -> exit=1` with REPAIR/ANNOTATE/NOSTUB/RECEIPTS FAIL and
LEDGER/FROZENCFG PASS; `lands-eq-base -> exit=2`; `legcount -> exit=2`;
`config-edit-ledger/claims -> FROZENCFG=FAIL`; `typed-receipt`,
`receipt-wrong-rev`, `receipt-missing -> RECEIPTS=FAIL`;
`tracked-blob-mismatch -> TRACKED=FAIL`; `separable-family`,
`separable-sid -> SEPARABLE=FAIL`.

## Findings

**F1 — HIGH (survivor M11): a corrections row that does not lead with a frozen
pair id is outside the SEPARABLE read set, so it can cite claim-C artifacts
while the counter passes.**
Evidence: M11 commit `d5ff2ce6644739d25b9dcd8039bf048aac162393` — a row under
`## Corrections — round 74` naming
`corpus/knowledge/culture-material/worldbuilding-setting-practice.md` (and any
`S881`–`S884` id would behave the same) leaves
`ACCEPT-CA-74: PASS legs=11/11`. Raw output:
`ACCEPT-CA-74: PASS legs=11/11` with
`LEG PASS SEPARABLE … scanned=['ledger', 'corrections-rows', …] problems=[]`.
Mechanism (reports/round-74/accept-ca.py:1557, in `leg_separable`):
`ca_rows = [r for r in rows if any(row_starts_with_id(r, i) for i in ids)]`
— only rows whose first cell equals a frozen pair id enter the scanned bytes
(:1590 `if family in body:` then never sees the smuggled row;
`row_starts_with_id` at :312 documents "LEADS it … never when it is
mentioned"). The counter's own selftest proves the guard fires when the
violating bytes are inside the read set (`selftest: separable-family ->
exit=1 SEPARABLE=FAIL`), so the hole is precisely the read-set filter.
Impact: the calibration claim's separability guarantee (no claim-C citation in
the Ca read set) does not cover the whole corrections block; cross-claim
citations can be annotated under a foreign row id with the counter green.
Proposed fix (for the round owner; a surviving mutant is a coverage finding,
not license to amend the frozen claim): scan **all** rows under the corrections
heading for the forbidden lane ids and family literal — feed `"\n".join(rows)`
into the scan instead of `ca_rows` — while keeping the leading-id rule for
ANNOTATE pair attribution. Superset scanning keeps every frozen sentence true.

**F2 — LOW (operational stability, not a mutant effect): the RECEIPTS leg's
`accept-c-73` re-run intermittently refuses (`exit=2`, empty stdout) inside
otherwise-valid runs.** It fired during M8 and M9
(`problems=['accept-c-73 re-run exit=2 (want 0)', "accept-c-73 re-run did not
print 'ACCEPT-C-73: PASS legs=11/11'", '…accept-c-73-at-lands.txt: committed
stdout differs from the re-run (bda16ca6deec vs e3b0c44298fc)']`) but passed in
the baseline and in the M1–M7, M10–M13 runs, and passed 4/4 standalone
re-probes of the identical command (clone at `2d1cd9140d3a…`, `--census-sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` →
`ACCEPT-C-73: PASS legs=11/11`, exit 0, three consecutive runs plus one
earlier probe). The r73 re-run evaluates a clone pinned to `2d1cd914…`, so
landed-tree mutants cannot cause it; fleet-root concurrency from sibling seats
is the plausible trigger. Both affected runs had their targeted leg problems
independently (M8 TRACKED, M9 RECEIPTS), so no verdict changes. Proposed fix:
retry-once semantics for the in-counter r73 re-runs, and surface the re-run's
stderr in the problem line (currently the refusal reason is swallowed — only
exit code and empty-stdout hash are reported).

## Attack outcome

12 of 13 mutants killed; M11 survived (F1). The claim's byte-level defenses
held everywhere they were probed: baseline PASS 11/11 reproduced, every
targeted leg fired with the expected detail, and the do-nothing / refuse-at-base
/ legcount controls behaved as frozen.

## Restoration evidence

After every mutant: `git reset -q --hard 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`.
Final state of the scratch clone:
`git rev-parse HEAD` = `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` (== `main`),
`git status --porcelain` = empty, and every touched file's sha256 equals its
pre-mutation value:

```
a9cb045fcb57f8c46d8fdfd1ed394943208ab246345e16f1e711fa366361b78b  SCORECARD.md
6de31d4d1d04d10387cc16293b8bd60291fc1e58af6e6efdc1e74a42e3a342e3  LOG.md
ab09033301487f0a030b7efba1789a54eb831032de2506e41d8170a89e8939d1  SKILL.md
864c94192854f37bfbf5bbf0e58f42fe41c86810cead36e79161700d3f24784e  reports/round-74/telemetry/accept-ca-73-at-lands.txt
88d5fd522c86b3ef37577531d39b148633455836ecd207f27a27a449c8725bd4  reports/round-74/ledger.json
290a6ccd839cb8cd09fc5089d1360dc4bcfabdea38f7a83733063159185c50aa  .ufo/waves/round-73/w2/CritEntryAmendFinal.md
```

The lane repo at `/home/vgpnk/Projects/shokunin/kotodama-shokunin` was never
written except this report file; all mutants lived and died inside
`/tmp/MutLandedCa/`. Raw counter logs: `/tmp/MutLandedCa/logs/M{1..13}.log`,
`baseline` lines in the seat transcript, `selftest-ca.log`, `r73c-probe.log`,
`flake-{1,2,3}.log`, `pristine-sha256.txt`.
