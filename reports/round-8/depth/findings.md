# R8-D16 — adversarial review findings: `tools/d2-typed-labels.py`

- shard: R8-D16 (adversarial reviewer, depth claim D), round 8 (loop 1, build 1 of 4), 2026-10-17
- reviewer scope: read-only over the lane tree; **this file is the only write**
- reviewed artifacts:
  - `tools/d2-typed-labels.py` (D02) — **the tool was rewritten eight times during this review**; every finding carries the revision it was measured on and its status at the newest revision I could test
  - `reports/round-8/depth/design-spec.md` (D01), sha256 `84e4b4c19b0310f138b5bb53f3e4b3672cdc493fc83b555d912a9630984cc751`
  - `corpus/knowledge/synthesis/worldbible-integration-contract.md`, sha256 `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`
  - supporting shards: `shard-parser.md` (D03), `skill-table-draft.md` (D14), `docs.md` (D15), `findings-17.md` (D17)
- baseline revision: `cf338a713060f274269cdacb18cdc0085bb06aeb` + a dirty worktree (concurrent workers)
- method: execute the tool (CLI, `--selftest`, `--emit`), re-derive expected behavior by hand from the components, mutate inputs in my own mirrors (`/home/vgpnk/.r8d16/mirror*`, outside the repo), recompute every digest the tool and the spec assert, and run the round's acceptance harness
- canon: NON-CANON review record; no gate, component, packet, corpus or SCORECARD file was edited by this shard

**Status summary at the newest revision tested, `e9209f28` (17:31:07):** `--selftest` 34/34 exit 0; `D2L-*` finding vocabulary present (69 occurrences); exactly three label kinds; `--emit` byte-deterministic; exit 1 with holds. **Open: S2 (no frozen manifest), S3 (post-pin gate repairs break regeneration and the round-3 replay), S6 (a supplied `native_form` is still not read), S10 (rank coverage ratio must be quoted honestly), S11, S12, S13.** S1/S4/S5/S7/S8/S9 were defects of earlier revisions and are resolved — kept here as the review trail, not as current defects.

---

## 0. Revision ledger (why every finding carries a hash)

| stamp (2026-10-17, -03) | sha256 (first 8) | observed |
|---|---|---|
| 17:19:53 | `13e82857` | first landing, 61,122 bytes |
| 17:22:03 | `37060dd1` | default path fixed |
| ~17:22:40 (mirror copy) | `1756e8c0` | artifact misreported `11-costumes.yml` digest (S13c) |
| 17:22:53–17:24:37 | `623b5b1f` | mid-review battery: selftest 32/32, determinism/digests verified, gate-clean artifact |
| 17:26:39 | `5d87d346` | `--selftest` exit 1, `RecursionError` (S1) |
| 17:27:43 | `61b61eb4` | same RecursionError |
| 17:28:50 | `6a80ffe4` | same RecursionError; structure root-caused |
| 17:30:23 | `3548185c` | rewrite: spec-conformant ids/CLI/exit map; selftest 34/34 |
| 17:31:07 | `e9209f28` | newest tested: selftest 34/34 exit 0, `D2L-` ×69 |

---

## S2 — OPEN, blocking: no frozen manifest exists for the D2 packet

Claim D requires "the D2 example packet regenerates deterministically and replays frozen (`python3 tools/replay-frozen.py`) without digest drift". The round's harness looks for a manifest in `reports/round-8/**/MANIFEST*.tsv`, `reports/round-8/**/*manifest*.tsv`, `tools/gates/frozen/round-8/**/MANIFEST.tsv`, `examples/culture-d2/**/MANIFEST*.tsv` (`run-validation.py` `discover_manifest`).

```sh
find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path '*/scratch/*'
# tools/gates/frozen/round-3/MANIFEST.tsv
# tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv
ls tools/gates/frozen/          # round-3  round-4   — no round-8
```

Harness receipt (`python3 reports/round-8/run-validation.py`, 17:26): `claim D: FAIL — … no frozen manifest found for the D2 packet …`. Until the D18 scribe deliverable lands, the clause is unverifiable as written.

## S3 — OPEN, blocking (cross-shard): the D2 regeneration and the round-3 replay are red because gates were repaired after their digests were pinned

```sh
python3 tools/assemble-d2.py --check; echo $?      # exit=1 (packet.d2.yml differs from deterministic assembly)
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv; echo $?   # exit=2
```

Isolated reproduction (current reader + committed components; only the digest line differs):

```text
3322c3322
<   reader_sha256: "29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03"
>   reader_sha256: "e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f"
```

The packet body is unchanged; the O-shard's repair of `tools/gates/costume-era-consistency-gate.py` invalidated the digest the packet pins. The harness authors name this class (`run-validation.py` `reader_pin_diagnostic`: "a regeneration task for the packet's owner, not a code defect"). The replay row is the same class: `ROW 2 could-not-evaluate reason=gate_digest_mismatch gate=tools/gates/phonology-sanity-gate.py`. Both pins are doing their job; D's clause cannot pass until the packet is re-baselined and a new frozen manifest is recorded. Integration decision — reported, not absorbed.

---

## S6 — OPEN, medium: a supplied `native_form` on a costume record is still not read

`design-spec.md` §1.3 R1/R4 (a supplied native form is *the* checked form; a translation claim cannot waive it) and §1.2 L2 (two supplied sound forms ⇒ exit 2) assume the tool reads a supplied `native_form`. At `3548185c` it still does not:

```text
inject 'native_form: "vinter"' into GAR-01 (mirror3) →
FINDING D2L-FORM-UNRESOLVED: [hold] GAR-01 — label_id LEX-GAR-01 has no supplied native/borrowed form
```

The projection is unchanged by the injection; the only native-form sources are the lexicon and the unresolved form slots. Fail-closed in the narrow sense (nothing is checked), but the rule the capability exists for has no input path. Either implement it or record in the spec that D2 has no supplied-native-form channel.

## S10 — OPEN, medium: quote the rank-adapter coverage ratio, not the adjective

At `623b5b1f`: `prose_rules_total=21, rank_rules_executable=3, rank_rules_held=18`. At `3548185c`: `rank_rules_component=21, rank_rules_normalized=9, rank_rules_gate_projected=5, rank_rules_unresolved_items=13, rank_quarantine_handles=3`. The newest revision roughly triples normalized coverage and now reports conflicts (`D2L-RANK`, 4), which is honest and quantified — but "**executable** rank-rule adapter" still describes 5 gate-projected of 21 records. The SCORECARD capability row should carry the ratio (S11 is about how that row is checked).

## S11 — OPEN, low: the harness cannot enforce "capability row enters SCORECARD only on demonstrated run"

`run-validation.py` decides the row with a whole-file regex `re.search(r"d2[-_ ]typed[-_ ]labels", scorecard, re.I)`. `SCORECARD.md:117` already contains that string inside the **Planned** section, so the check passes without any demonstrated-run row, and the companion message ("SCORECARD carries the d2-typed-labels row although the tool selftest did not pass") fires off the planned mention. Anchor the check to a specific table/section.

## S12 — OPEN, low: D03's strict loader fragment cannot parse the lane's own packet (did not propagate)

`shard-parser.md` §4.1 `load_packet_strict` rejects bare `-` list items, which the assembler emits:

```python
load_packet_strict("costumes:\n  -\n    id: GAR-01\n")
# {'packet': None, 'findings': [{'code': 'P-UNTERMINATED-FLOW', 'line': 2,
#   'detail': "content '-' is not a mapping line"}]}
grep -c '^ *-$' examples/culture-d2/packet.d2.yml      # 312
```

The delivered tool does not use that loader (it reads through the costume gate's reader), so the defect stayed in the fragment. Do not land §4.1 as-is.

## S13 — OPEN, low (evidence hygiene): pinned digests and line locators are invalidated by concurrent edits

- **S13a.** The metadata sweep inserts three frontmatter lines (`source`, `verified-at`, `recheck`) near the top of each synthesis file, shifting line numbers by +3 and changing digests. `design-spec.md` §9 pins `era-language-staging.md` `226e1104…` and `loanword-material-dating.md` `bb08d458…` — both are exactly the **HEAD** bytes (`git show HEAD:… | sha256sum`), while the worktree now holds `621b7a33…` / `5b1d75ab…`. Pins correct when taken; no longer resolvable.
- **S13b.** Correction to my own mid-review reading: I first measured D14's `loanword-material-dating.md` locators as off by 2–4 lines; re-checked against HEAD bytes they are **correct** (`:44` = "Separate ultimate etymon from immediate donor and carrier"; `:54` = the donor-innovation row). The offset was the sweep's +3 lines, not a D14 defect. D14's 14 pinned sha256 values all verified against HEAD at read time.
- **S13c.** Intermediate revision `1756e8c0` misreported `11-costumes.yml` in `assembly.source_sha256` as `bd7eeb08…` while the bytes were `b6e2c5c2…`; `623b5b1f` and later report it correctly. Churn record, not a finding against the reviewed revision.

---

## Resolved during review (kept as the trail; not current defects)

| # | finding (revision) | status |
|---|---|---|
| S1 | `--selftest` broken: `RecursionError` from two `def selftest()` (lines 1355, 2388 at `6a80ffe4`) plus `selftest_rank_block = selftest` (line 2600) aliasing the caller; earlier `13e82857` also failed 4/30 controls, of which the `unknown institution id` control was a no-op fixture (`(WI-1)` absent from `11-costumes.yml`; `grep -c` → 0) and the `unreadable maps_to` control was a needle mismatch (tool refused correctly with `maps_to names no component: 'the wool one'`) | **resolved** — `3548185c` and `e9209f28`: 34/34 exit 0, no traceback |
| S4 | spec §6 finding ids absent (`grep -c 'D2L-'` → 0 in tool and artifact at `623b5b1f`; spec §8 says "reuse verbatim") | **resolved** — `D2L-*` ×69 at `e9209f28`; report emits `D2L-FORM-UNRESOLVED`, `D2L-NATIVE`, `D2L-RANK` |
| S5 | kinds: spec "exactly three" vs five shipped (`fictional-coordinate`, `descriptive-gloss` carried 25 of 94 labels at `623b5b1f`) | **resolved** — `label_kinds` = `translated-label`, `native-form`, `borrowed-strata` at `3548185c` |
| S7 | exit map: spec "0 = no HOLD/FAIL"; `623b5b1f` exited 0 with 41 findings incl. 10 holds | **resolved** — `3548185c` exits 1 with holds present |
| S8 | CLI: spec §0 `--emit PATH` + stdout default; `623b5b1f` had only `--check/--report/--selftest` and wrote the artifact by default; D15's docstring fragment did not match | **resolved** — `--packet/--json/--emit/--check/--selftest`; `--emit` byte-deterministic (two emits → `59a53456…`). D15's fragment still needs its checklist pass |
| S9 | contract §5 fields absent (`script`/`representation`/`scheme`/`evidence` = 0 at `623b5b1f`) | **resolved** — 58/58/68/58 occurrences in the emit at `3548185c`; residual: `pronunciation` (contract §5 lists it) = 0 |

## Verified positives (newest revision unless noted)

- `--selftest` → 34/34, exit 0, malformed-input controls present (all `measure_d_selftest` criteria met).
- `--emit` determinism: two runs → byte-identical output (`59a53456…`).
- Provenance at `623b5b1f`: all five `assembly.source_sha256` entries and `reader_sha256` matched the actual bytes (recomputed independently).
- Gate-clean projection at `623b5b1f`: `costume-era-consistency-gate.py examples/culture-d2/typed-labels.d2.yml` → exit 0, 0 findings.
- D17's blind cases hold: `LEX-GAR-01` held unresolved (never resolved to `mirken`); `kas` typed `borrowed-strata` with `stratum: loan`, `stage: E1`, `donor_layer: "Salt-road trade layer"`, donor separate from the checked form.
- Refusals: unknown institution id → exit 2 with a named diagnostic; unreadable `maps_to` → exit 2; malformed annotations → `Malformed`.
- The newest revision's `D2L-NATIVE` hold for the accented forms (`sára`, `sará`) cites the component's own minimal pair rather than failing a diacritic against a segment inventory — exactly the discrimination the capability exists for.
- No-canon discipline: `canon: "not canonized (D2 design drill)"` in the artifact.

## Limits and to-verify

- The tool was still being rewritten at review close (`e9209f28`, 17:31:07). S2, S3, S6, S10, S11, S12 were re-checked as recently as possible but must be re-run on the revision the orchestrator freezes.
- I did not re-run `run-validation.py` after 17:26 (its claim-D items then included S1/S3/S2 as they stood at `5d87d346`). Claim F's failures in that run are outside this shard's assignment and are not assessed here; claim O passed.
- D18–D20 scribe deliverables (frozen manifest, SCORECARD row, dispatch ledger) were absent at review close; S2/S11 state what the harness will and will not enforce.
- Not assessed: the design question of whether D2 needs a supplied-native-form channel (S6 is the factual gap, not the design answer); and any real-world claim, which is out of province.

## Receipts (lane root unless noted)

```sh
# revisions and selftest
sha256sum tools/d2-typed-labels.py                       # per §0
python3 tools/d2-typed-labels.py --selftest; echo $?     # 34/34 exit 0 @e9209f28
grep -n '^def selftest' tools/d2-typed-labels.py         # 1355, 2388 @6a80ffe4 (S1)
grep -n 'selftest_rank_block' tools/d2-typed-labels.py   # 2403 call, 2600 alias @6a80ffe4 (S1)
# conformance
grep -c 'D2L-' tools/d2-typed-labels.py                  # 0 @623b5b1f → 69 @e9209f28
python3 tools/d2-typed-labels.py --emit /tmp/a.yml       # byte-deterministic @3548185c
# blockers
python3 tools/assemble-d2.py --check; echo $?            # 1 (reader digest line)
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv; echo $?   # 2
find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path '*/scratch/*'
python3 reports/round-8/run-validation.py                # claim D FAIL (as of 17:26), O PASS, F FAIL (out of scope)
# probes (my mirrors, outside the repo)
python3 /home/vgpnk/.r8d16/probes2.py                    # S6 evidence
python3 /home/vgpnk/.r8d16/probe2.py                     # S12 evidence
```

FILES: reports/round-8/depth/findings.md | SUMMARY: D16 adversarial review of tools/d2-typed-labels.py against design-spec.md and the worldbible integration contract — the tool was rewritten eight times during the review (13e82857 → e9209f28); filed 13 severity-ranked findings with per-revision status: S2 (no frozen manifest for the D2 packet) and S3 (post-pin gate repairs make assemble-d2 --check and the round-3 replay red) block claim D; S6 (supplied `native_form` still unread), S10 (rank coverage 5/21 gate-projected), S11 (harness SCORECARD regex false positive), S12 (D03 loader fragment rejects the real packet), S13 (pins invalidated by the metadata sweep, incl. a correction to my own earlier locator reading) remain open; S1/S4/S5/S7/S8/S9 were earlier-revision defects now resolved, with receipts; positives verified include 34/34 selftest, byte-deterministic `--emit`, matching source digests, a gate-clean projection, and D17's blind cases holding.
