# ExecCaFix — claim-Ca counter rehearsal (round 75, wave 2)

Rehearsal of `.ufo/waves/round-75/counters/accept-ca.py` (sha256
`3c89412923de5fe5026421a7bf0d025eeefd80da299153842dce4234274ad4fd`, 3684 lines) against a
scratch repository built from lane base `f556d1049fe651d3d63975600b13acd9fb686f15`, a
rehearsal-only freeze carrying the current `reports/round-75/{claims,ledger}.json` + the counter
+ the R1 fixtures, and a lands tree assembled from the **staged** landing files
(`.ufo/waves/round-75/w2/stage/`, snapshot below) plus, where named, a repair the stage does not
yet carry.

Every run names the same fleet root `/home/vgpnk/Projects/shokunin` (read-only).

## Leg table

| run | lands | freeze | --combined | exit | legs |
|---|---|---|---|---|---|
| A staged landing as staged | `121e7ea2ecadcaaf8dabafb341941a6864b702af` | `59ff98af64695f6d9ed24b609738e8e0232100ca` | — | 1 | **10/12** |
| B staged landing + the SHONEN.md:6 repair | `a08b972837769f32300007e633bfc1e10be55963` | same | `9a878ff0afa7c039c8affde810266ac61f48bd1f` | 0 | **12/12** |
| C same lands, no combined tree | `a08b972837769f32300007e633bfc1e10be55963` | same | — | 1 | 11/12 |
| D do-nothing (lands == freeze) | `59ff98af64695f6d9ed24b609738e8e0232100ca` | same | — | 1 | 7/12 |
| E lands == frozen base | `f556d1049fe651d3d63975600b13acd9fb686f15` | same | — | 2 | refused |
| F staged landing + the staged sweep draft verbatim | `e92fce5a660e0da1598880b94be933ffcee5831e` | same | — | 1 | 10/12 |

### A — the staged landing as it stands (10/12)

| leg | verdict | why |
|---|---|---|
| LEDGER | PASS | 10 pairs, min 10, every observe_cmd structurally valid after the pattern-operand reading |
| BASEMISMATCH | PASS | red=10 at base, none unobservable |
| REPAIR | **FAIL** | `L75-01`, `L75-05`, `L75-06`, `L75-07`: `statement_after no-match in SHONEN.md` — **the stage carries no SHONEN.md:6 edit**, so the registry-count statement the four pairs repair is still the base line |
| ANNOTATE | PASS | rows=8, annotate-pairs=4, unannotated=0 (the staged `SCORECARD.md.append` rows) |
| NOSTUB | PASS | stubs=[] |
| APPENDONLY | PASS | protected set zero removals; README 344/407 + SKILL 701 are REPAIR stated_at lines; sweep.py is the frozen fixed-surface exception; fleet report at pin `3a740160…` byte-identical (blob-sha256 `354273bc972d`) |
| R1EXEMPT | PASS | verdicts `{green: True, red: False, mixed: False}`; both receipts present |
| SEPARABLE | PASS | 9 lane ids, no lane id / family literal in the read set |
| RECEIPTS | PASS | r74 counter re-run reproduces `accept-ca-74-at-lands.txt` (see the TMPDIR finding) |
| COMBINED | **FAIL** | `the explicit --combined revision is required` (this run passed no `--combined`) |
| FROZENCFG | PASS | freeze on the lands first-parent chain; claims/ledger byte-identical to the freeze |
| STAMP | PASS | stamped==evaluated==measured==lands |

### B — the same tree + the SHONEN.md:6 repair + a stub claim-C landing (12/12)

`ACCEPT-CA-75: PASS legs=12/12`, exit 0. All twelve legs green; COMBINED
(`ca-lands=a08b97283776 combined=9a878ff0afa7 tree=…`) green with the C-owned README heading
exemption firing as designed. This is the achievable state: the only landing piece A lacks is the
SHONEN.md:6 line.

### D — do-nothing control (7/12)

RED: REPAIR (all six pairs), ANNOTATE (no `## Corrections — round 75` at the freeze), NOSTUB,
RECEIPTS (no `accept-ca-74-at-lands.txt` at the freeze), COMBINED. GREEN: LEDGER, BASEMISMATCH,
APPENDONLY, R1EXEMPT, SEPARABLE, FROZENCFG, STAMP. The claim's do-nothing sentence ("REPAIR and
ANNOTATE red, R1EXEMPT green, FROZENCFG/LEDGER green") holds.

### E — `--lands == base`

`ACCEPT-CA-75: FAIL legs=0/12 (refused: --lands equals the frozen base f556d1049fe6)`, exit 2.

### F — the staged sweep draft verbatim

REPAIR red: `sweep green-after expected exit=0 ok=true; got 1` — `drafts/sweep-fixed.py` raises
`IndentationError: unexpected indent (line 170)`; the repaired instrument never runs.

## Staged-landing snapshot applied (sha256, first 16 hex)

```
f5aed3a0cab6cc32 SCORECARD.md.append
d26d6c986fbd802c corpus/QUALITY.md.append
e3fa4f8d4c5f12b7 corpus/README.md.ca-edits
08a9cb5eea6f0af7 SKILL.md.ca-edits.md
29bf7715d758abbb corpus/lessons/round-75.md
1942ef3817a60eef reports/round-75/telemetry/selftest-r72-repeat.txt
f88aebae60367741 reports/round-75/telemetry/sweep-base.txt
5335a51f074eb0d2 reports/round-75/telemetry/sweep-fixed-at-base.txt
745c3c1c07a295d5 reports/round-75/telemetry/sweep-fixed-after-ca.txt
```

`SCORECARD.round75-claims.append` (claim C's axes rows) and `corpus/README.md.c-rows` /
`.c-footer` are NOT applied at Ca-lands (claim C owns them); the rehearsal's combined tree uses a
stub C landing (nine rows S885–S893, the three staged entries, README `## myth-symbol/ (29)` →
`(32)`).

## Raw logs

`run-staged-ca.txt`, `run-staged-full-combined.txt`, `run-staged-full-ca.txt`,
`run-do-nothing.txt`, `run-lands-eq-base.txt`, `run-sweep-draft-verbatim.txt` — all in this
directory.
