# ExecRegistryRows — round 84 w1 report

**Seat:** ExecRegistryRows (executor; axes operability, calibration; milestone r84-v1).
**Scope:** the three `## Gates and probes` rows claim O needs. Read-only on the lane; no
commit, no `SKILL.md` edit, no counter run against a lands revision.

## Files written

| path | content | sha256 |
|---|---|---|
| `.ufo/waves/round-84/w1/stage/ExecRegistryRows/rows.md` | the exact three 8-cell registry rows | `decb92bf4b4acdd735e9d7b7227af4c3b7168cad0d84f48b5c723ac2570e1421` |
| `.ufo/waves/round-84/w1/stage/ExecRegistryRows/row-check.md` | census commands, shape audit, dead-token audit, post-round expectations | — |
| `.ufo/waves/round-84/w1/stage/ExecRegistryRows/registry-census.json` | machine-readable census and expectations | — |
| `.ufo/waves/round-84/w1/stage/ExecRegistryRows/receipts/census-pipelines.txt` | raw pipeline output for every base count | — |
| `.ufo/waves/round-84/w1/stage/ExecRegistryRows/receipts/house-base-export.txt` | house checker on an isolated base export | — |
| `.ufo/waves/round-84/w1/stage/ExecRegistryRows/receipts/post-sim.txt` | red-before and green-after registry simulation | — |
| `.ufo/waves/round-84/w1/stage/ExecRegistryRows/receipts/rows-shape.txt` | three rows, eight cells each, zero internal pipes | — |

No file outside the stage directory was written. No tool was installed or upgraded.

## Result

Base `81499ee4`, re-derived independently of `tools/check-gate-registry.py` and then
corroborated with it on a disposable export:

- `## Gates and probes`: **74 data rows**, header **8 cells**, separator **8 cells**
  (all `:?-{3,}:?`), table lines 648–723 of the base blob.
- Instrument set `reports/round-*/accept-*.py`: **61**, **0 unrowed**, **0 dead**
  entry-command `.py` tokens.
- Top-level `tools/*.py`: 30, **25 without a row**.
- Cell distribution: 68 rows × 8 cells + the 6 pre-existing 9-cell rows
  (`accept-c-66`, `accept-ca-66`, `accept-o-66`, `accept-c-67`, `accept-ca-67`,
  `accept-o-67`; each repeats a trailing owner cell). The drafted rows are 8 cells.
- The 11-cell shape is the separate `corpus/SOURCES.md` `## Registry`: **837 rows,
  837/837 with 11 cells**. Claim-D rows S914–S917 are graded there, not here.

House checker on the base export:

```text
GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead
GATE-REGISTRY-INFO: 25 tools without a row
```

After the three rows land and their `.py` files exist, the same table must print:

```text
GATE-REGISTRY: 0 missing / 77 registered / 63 instruments / 0 dead
GATE-REGISTRY-INFO: 25 tools without a row
```

Why: `registered` is the data-row count (74 + 3 = 77); instruments are 61 + the two
frozen round-84 counters (63), both named by rows 2 and 3; every `.py` token in every
entry-command cell resolves at lands; and the only new top-level tool is named by row 1,
so the unrowed tool count stays at the base 25 (claim O's ceiling). The scratch
simulation is red before the rows (`2 missing / 74 registered / 63 instruments / 0 dead`,
INFO 26, exit 1) and green after (`0 / 77 / 63 / 0`, INFO 25, exit 0).

## Decisions and evidence

1. **Freeze token is r2 `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2`, not the brief's r0.**
   The dispatched brief quoted `3ca2cf28…`, but the lane's HEAD is r2, committed
   10:31:06, and `reports/round-84/counter-revisions.md` plus `build-w1.py`/`spec-v1.json`
   declare r2 current. r0→r2 changed only frozen constants (claim-D headings in r1;
   claim-O `shape_markers`/`semantics` in r2), never a counter code line. The rows pin r2
   because `accept-d84`/`accept-o84` grade `FROZENCFG` by comparing the `--freeze`
   `claims.json` bytes to the lands bytes; r0/r1 tokens would fail at an r2 lands. Frozen
   hashes: `accept-d84.py` `efee17ff…`, `accept-o84.py` `cbabd31c…`, `claims.json`
   `279a74dc…`, `counterlib.py` `c3707d1a…`. If the L1 lands the r0 claims bytes instead,
   swap the freeze token in rows 2 and 3; nothing else changes.
2. **Read-only sink is `--out /dev/stdout`, not `/dev/null`.** `SKILL.md` contains zero
   `/dev/null` occurrences, so no gate row uses it; the house does run
   `tools/d2-typed-labels.py --emit /dev/stdout` in `reports/round-12/recount/`, so
   `/dev/stdout` is the house-precedented device form. It leaves every repo byte untouched,
   keeps the derivation observable, and avoids a committed absolute scratch path. Assumes
   the landed tool writes the named `--out` directly; if it stages and renames, the row
   needs a regular file under a named `--work` and a `scratch` write scope.
3. **Placement.** The rows must be inserted inside the `## Gates and probes` table,
   before the next `## ` heading (base line 743). A scratch simulation that appended them
   at end-of-file still read `74 registered`, with both instruments missing.
4. **Self-test floor.** Row 1 says `>=24 checks` (the ExecSoundLaws seat contract and the
   wave context); the frozen claim-O floor is 20, so the stricter row is safe and the
   counter's `SELFTEST` leg accepts it.

## Risks

- The freeze token depends on the lands carrying r2 `claims.json` bytes; the fallback is a
  one-token swap to the landed revision.
- The `/dev/stdout` sink depends on a direct-write implementation (see decision 2).
- No lands exists in this wave yet, so the post-round lines are simulated, not measured on
  a lands commit; the simulation used the exact base export, the two frozen counters and a
  stub tool.
- `>=77 registered` and `>=63 instruments` are floors: any further seat row or counter can
  only raise them; `missing` and `dead` must stay 0 and `unrowed` must stay <= 25.

## Blockers

None.
