# R11-O16 — reviewer: envelope completeness (placeholder vs live content)

- seat: **R11-O16** (reviewer, claim O, round 11 — loop 1 of 3, build round 4 of 4), 2026-10-17.
- assignment (verbatim): "HANDOFF R11-O16 (reviewer): envelope completeness — any of the 16 fields populated with placeholder rather than live content = finding; reports/round-11/handoff/review-16.md."
- write scope: **this file only** (plus in-lane scratch under `.scratch/r11-o16/`; `TMPDIR=$PWD/.scratch` set before every scratch-writing command). No tool, packet, baseline, corpus or earlier-round byte was written by this seat; no commit.
- tree at review: HEAD `e3ef171` (claims commit; baseline revision `94ca098`), all round-11 O artifacts untracked. Observation window 22:00Z–22:14Z.
- canon: NON-CANON engineering evidence. Nothing here adjudicates canon, rights, or game mechanics.

## 0. Object under review, stamped

| object | sha256 | note |
|---|---|---|
| packet emitted by the exercise (2 independent runs, byte-identical) | `2a058f7858127b98592439594c55974d93e6e672a600dd2036b47e21e71c8a63` | `.scratch/r11-o16/emitted-packet.md` / `-2.md`; 148 lines |
| `tools/exercise-handoff-e2e.py` | `38d1cba429d98af79a14201d6cdf44150dd935314f4536003253f8f576b4f4c1` | mtime 19:07:36 local |
| frozen baseline `tools/gates/expected/handoff-exercise/r11/expected.json` | `1ab17670c113bf5f10a80f5ba564b252d948a836c3793efe641c68154d286b33` | frozen 19:08:52 local; 11 findings impact — see F-3 |
| `reports/round-11/handoff/design.md` (O01) | `39012d479c6b4665…` | the spec this tool is measured against |
| `reports/round-11/handoff/shard-glossary.md` (O04) | `ac6d1d54105368bd…` | glossary-builder shard |
| `reports/round-11/handoff/packet-attempt-1.md` (O06) / `.yml` | `289c8ca25bbebca7…` / `82ed1cb5dd2e77bb…` | independent attempt, verified separately (§5) |

Every sha256 in this review is measured by this seat on the bytes named; every command ran from the lane root with `TMPDIR=$PWD/.scratch` (mandated: `/tmp` inode-exhausted).

## 1. Method (independent of the exercise's own checks)

1. Ran `python3 tools/gates/handoff-packet-check.py` on the emitted packet (fresh process, own cwd).
2. Occurrence census of all 16 §4 fields with the gate's own parser reused (`review_assist.py`): every candidate occurrence, not only the chosen one; extended placeholder vocabulary (gate set + lorem/fixture/sample/`KTD-HO-CONTROL`/F-toy markers).
3. Whole-document digest sweep: every 64-hex token matched against sha256 of every repo file (18/18 matched for the emitted packet).
4. Glossary term-column integrity (`term_check.py`): every term cell ∈ live D2 term set (40) ∪ D3 native/stage forms (24); no `display_label` string from the D3 projection trace may reach a cell.
5. Glossary pair trace (`glossary_trace.py`): each row matched to the live D2/D3 lexicon record with gloss overlap.
6. Independent recounts of every number the packet asserts from `examples/culture-d2/packet.d2.yml` (`grep -c`/`sort -u`).
7. Token trace (`review_trace.py`): every distinctive token of every field checked for presence in live D2/D3 artifacts.
8. Determinism: two `--emit` runs compared byte-for-byte.
9. Control-leg probe (`controls_probe.py`): imported the tool as a module, assembled with its own code path, applied its own selftest mutations, ran the committed gate over each (needs no baseline).
10. Battery interaction of the frozen baseline (`check-gate-battery.py` `inspect_baselines` imported and run over the committed roots).

## 2. Verdict — the assigned question

**Envelope completeness: PASS. No field carries a placeholder instead of live content; no finding of the assigned class.**

- `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0 (command §6.1); the exercise's own run reproduces this and its frozen comparison is green (§6.2).
- Each of the 16 fields resolves to exactly **one** occurrence; the extended placeholder scan flags none (no `TBD`/`n/a`/`-`/`unknown`-as-value, no fixture/sample markers, no D1 content — the D1 sample's `fala/fano/…` glossary correctly fails the live-set check, proving the check discriminates).
- 18/18 sha256 tokens in the document match live file bytes; 0/18 unmatched (the sample's stale pins would have shown here — this packet pins the live values).
- All numbers asserted in the packet reproduce by independent recount: D2 `design-choice` 118, `attested-comparator` 4, `to-verify` 21, `coupling_note` 29, costumes 10, materials 9, rule ids M-01–M-27; D3 20 lexemes / 6 names / 7 utterances / 2 beliefs / 2 symbols / 3 materials / 4 objects / 4 costumes / 1 rank rule / 5 references / 5 bridges (all `grep -c`/list-length measurements, §6.5).
- Glossary: 20/20 rows trace to live D3 lexicon records with gloss overlap; every term ∈ {native forms, E0/E1 forms}; zero display-label leakage; all 20 statuses `constructed` (licensed). The gate cannot enforce the count (O04 proved that) — the exercise's own preflight asserts it, and the code path does (§3 note).
- Determinism: byte-identical across two runs (`2a058f78…`), no wall-clock content.

## 3. Field-by-field (all 16; build sha `38d1cba4`)

| # | field | emitted value (head) | live source (design §3 + build code) | placeholder? | trace verdict |
|---|---|---|---|---|---|
| 1 | `packet_id` | `kotodama.handoff.d2-d3-exercise` | constant (build :101) | no | identifier; authored value, not data |
| 2 | `packet_version` | `1.0.0-exercise` | constant (:102) | no | ditto |
| 3 | `contract_ref` | `kotodama-lore-adjacency 1.0.0, contract digest sha256:5f4c02bf…` | parsed live from contract bytes (:276–283, 398–402) | no | digest = live contract hash (round-8 value, not the stale filed pin) |
| 4 | `producer` | `kotodama-shokunin (round-11 handoff exercise; …)` | constant (:404) | no | lane identity |
| 5 | `recipient` | `lore-shokunin (canon, …)` | contract §3 | no | lane identity |
| 6 | `request_ref` | `none — no lore brief exists; … unbound research exercise …` | authored declaration of a live absence | no | explicit `none`+reason; not in placeholder set (gate agrees) |
| 7 | `baseline_bible_ref` | `none — deliberately unbound research packet; …` | authored declaration | no | `HO-BASELINE` satisfied; reason phrase present |
| 8 | `artifact_manifest` | 9 rows, each `sha256` | measured live at run time (:434–526) | no | 9/9 digests match bytes; record counts recounted (§6.5) |
| 9 | `subject_refs` | `cand:kotodama.d2.lexicon (40 records L-01–L-40), …` | mined live ids/counts from both packets (:420–431) | no | ids/ranges are real: 40/8/8/6/2 records; all `cand:` unresolved (note §4.1) |
| 10 | `scope` | D2/D3 culture names, eras, registers, counts | live names/eras (:528–555) | no | culture name `D2 highland pastoralists — round-3 design drill` is the live `name:` scalar |
| 11 | `dependency_manifest` | pinned digests + profile + SC1/AV1/NR1/RR1 one-liners | live records (:557–607) | no | no unnegated `latest`; digests match |
| 12 | `claim_ledger` | D2-CL01..03 + BR01..05 + D3-BELIEF + D3-SCREEN | live D2 evidence fields + D3 records (:610–653) | no | counts recounted; bridge ids/relations verbatim from live bridges |
| 13 | `coupling_edges` | D2-EDGES aggregate + BR01..BR05 rows | live `coupling_note` count + live bridge rows (:655–679) | no | 29 coupling notes recounted; limits text is live bridge `limits` |
| 14 | `requested_decisions` | 6 rows, live record-range ids | derived from live record classes (:681–731) | no | ids/ranges real; alternatives authored boilerplate (expected — decisions are a request format, not data) |
| 15 | `validation` | 5 observed-run bullets incl. the frozen-baseline path | records the runs the tool performs | no | describes actual process; the gate run + baseline compare reproduce (note §4.2) |
| 16 | `open_questions` | OQ-01..05 with lanes and blocking status | live screening/scope-notes/pending-read facts | no | OQ-01 cites `screening: unresolved` (live); OQ-04 counts 21/5 recounted |

Glossary payload (supporting, not field #17): 20 rows, header `| entry_id | E0 form | E1 form | gloss (packet) | etymology |`; each row's E0/E1/gloss are the live D3 lexeme verbatim; etymology computed from the live SC1 record (`derived_etymology` :311–328).

## 4. Findings (adjacent to the assigned class — operability defects in the same O claim)

The assigned class (placeholders in the 16 fields) is **clean**. The review must still report these, each measured at the stamped shas:

### F-1 (defect, high) — `--selftest` crashes: fixture root omits the component files
- Repro: `python3 tools/exercise-handoff-e2e.py --selftest` → `AssertionError` at :1267, traceback on stdout/stderr; observed message: `"evaluated: cannot hash examples/culture-d2/components/02-phonology.yml: [Errno 2] No such file or directory: '…/.scratch/handoff-selftest-…/fixture/examples/culture-d2/components/02-phonology.yml'"`.
- Cause: `build_fixture_root` (:1235–1251) copies only `FIXTURE_INPUTS` = the 5 `SOURCES` + gate + 2 assemblers (:1232); the exercise's `verify_component_digests` reads the 13 component files recorded in the two packets' `assembly.source_sha256` (9 D2 + 4 D3, :286–303), which are absent in the fixture.
- Consequence: the O claim's selftest leg ("selftest with positive + malformed controls") is unmet while the tool is at this sha: the positive leg returns exit 2 inside a fixture that should be a copy of a green tree.
- Fix direction (integrator's call): copy the component files (derive the 13 paths from the two packets' manifests, as the exercise already parses them) into the fixture.

### F-2 (defect, medium) — the placeholder-content control cannot fire: both the gate and the preflight are blind to it
- Probe: same mutation as the tool's own control (`facts["packet"].replace("- OQ-01:", "- OQ-01: TBD\n- OQ-01 (original):", 1)`), gate run via subprocess — observed `exit=0`, `fields=16/16 glossary-entries=20 findings=0`; the exercise's own `preflight` returned **no problems**.
- Why: the gate resolves `open_questions` to the `## open_questions` heading body; the body as a whole is not a placeholder token, and the inserted item's key `OQ-01` cannot resolve to a field name (hyphen breaks the list-key regex). So the selftest assert at :1302 (`gate["exit"] == EXIT_FAIL`) would fail even after F-1 is fixed.
- This also means a `TBD` line smuggled into any section body is a blind spot of the exercise's own placeholder discipline — relevant, because *this reviewer's assignment is exactly placeholder hunting*.
- Fix direction: plant the control where the mechanisms can see it (e.g. replace a whole field value with `TBD` so `HO-EMPTY` fires, or assert on a per-line placeholder scan of the extracted field values).

### F-3 (defect, high) — the frozen baseline sits where the design forbids it, and the gate battery notices
- Measured: baseline committed at `tools/gates/expected/handoff-exercise/r11/expected.json`; `design.md` §8 (line 251): "**Do not commit it under `tools/gates/expected/**` or `tools/gates/frozen/**`.**" — because `check-gate-battery.py` reads *every* `expected.json` under `BASELINE_ROOTS = (GATES_DIR/"expected", GATES_DIR/"frozen")` (:114) as a gate baseline.
- Live consequence (imported `inspect_baselines` over the committed roots, 22:11Z): the file yields **7 findings** — `BASELINE-GATE-UNKNOWN` (dir is not one of the seven gate names), `BASELINE-EXTERNAL-INPUT` ×5 (its `inputs` resolve via the repo root, not inside the baseline), `BASELINE-EXPECTED-ABSENT` (no `expected` block in the battery's schema); `baseline_exit: 2` (was 2 before via `BASELINE-GATE-UNCOVERED` ×2 for myth/naming gates). The two pre-existing gate baselines and the four frozen ones stay `pinned`.
- The packet's own `validation` field quotes this path (emitted packet line 113), so moving the baseline changes the packet bytes and requires a re-freeze — the tool's freeze discipline covers that, but the move must be deliberate.
- Fix direction: default the baseline to `reports/round-11/handoff/expected.json` per design §8, with `--baseline PATH` implemented (F-4), then re-freeze once.

### F-4 (delta, medium) — build vs design interface/control-matrix at the stamped sha
Measured deltas; if the tool freezes here, the design's contract is unmet in these points (each is the implementers' call to close or the design's to amend):
- CLI (design §10): `--root DIR`, `--baseline PATH`, `--keep`, `--json` are documented but absent in the build (only `--selftest/--freeze/--emit/--quiet`, :1399–1402); exit-code vocabulary `E2E-DIGEST/E2E-GATE/E2E-SCAN/E2E-COUNT/E2E-ARTIFACT/E2E-BASELINE/E2E-DATA` is not implemented (plain 0/1/2 exists).
- Control matrix (design §9): the build's controls differ from the designed probes; missing `HO-EMPTY` (blank `scope`), `HO-CANON-MARKER`, `HO-CANON-CLAIM` probes; the designed "drop `request_ref`" probe is not present (the build's renamed-field probe covers `HO-MISSING` differently).
- Constants (design §3 rows 1–2): design says `packet_id = kotodama.handoff.d2d3-e2e`, `packet_version = 1.0.0`; build emits `kotodama.handoff.d2-d3-exercise` / `1.0.0-exercise`; baseline `profile` is `kotodama-handoff-exercise/1` vs design's `kotodama-handoff-e2e/1`.
- Field map (design §3, rows 9/12/14/15): design's `subject_refs` names 8 candidate refs from records incl. `cand:kotodama.d2.{culture,pasture-lineage-institution,archaic-sky-holder,open-grazing-era}` and four `cand:kotodama.d3.*`; build emits 5 range refs. Design's `claim_ledger` carries D2 typed-label D2-CL01 (58 labels; 46/10/2; 10 holds) and D2-CL02 normalization residuals; build emits evidence-field counts instead. `requested_decisions` has 6 rows vs design's RD-01..08 + RD-D2-01/02.

### 4.5 Note on `.yml` serialization claim (resolved, reported for completeness)
`packet-attempt-1.md` §checks-run claims a gate run over `packet-attempt-1.yml` (exit 0, 16/16, 20 entries). At 22:04Z the file was absent (apparent write race); at 22:07Z it exists and my fresh gate run over it reproduces exit 0 / 16/16 / 20. Not a finding; recorded because the earlier observation could otherwise be mistaken for one.

## 5. Independent verification of the sibling attempt (O06), for the integrator's best-of selection

`packet-attempt-1.md` (`289c8ca2…`): gate exit 0 / 16/16 / 20 entries reproduced; **23/23** digest tokens match live files (including the re-measured contract `5f4c02bf` and freeze `562b76cb` replacing filed stale pins); 40/40 term cells ∈ live sets; its `baseline: none`/`request_ref: none` declarations match the contract §4 pattern. It is a D3-scoped packet; the integrated exercise emits a richer D2+D3 envelope and is the object the O claim names (`tools/exercise-handoff-e2e.py`), so this review's verdict binds to the exercise output, not to attempt-1.

## 6. Reproduce (all from the lane root, `export TMPDIR=$PWD/.scratch`; 2026-10-17, 22:00Z–22:14Z)

```sh
# 6.1 gate on the emitted packet (this review's copy; re-emit with --emit to own path)
python3 tools/gates/handoff-packet-check.py .scratch/r11-o16/emitted-packet.md
#   → INFO scan: fields=16/16 glossary-entries=20 findings=0   (exit 0)

# 6.2 the exercise itself
python3 tools/exercise-handoff-e2e.py            # exit 0, 11/11 checks OK, frozen packet matches
python3 tools/exercise-handoff-e2e.py --selftest # exit 1, AssertionError — F-1

# 6.3 placeholder/census/digest sweep over the emitted packet (scratch tools, this seat)
python3 .scratch/r11-o16/review_assist.py .scratch/r11-o16/emitted-packet.md   # 16 fields, 1 occurrence each, 0 placeholder hits, 18/18 digests
python3 .scratch/r11-o16/term_check.py .scratch/r11-o16/emitted-packet.md      # 40/40 clean (E0+E1 columns)
python3 .scratch/r11-o16/glossary_trace.py .scratch/r11-o16/emitted-packet.md  # 20/20 rows → live D3 records, gloss overlap True
python3 .scratch/r11-o16/review_trace.py .scratch/r11-o16/emitted-packet.md    # unmatched tokens = packet machinery/prose only

# 6.4 control-leg probe (both F-1/F-2 evidence lines)
python3 .scratch/r11-o16/controls_probe.py
#   → positive exit 0 16/16/20; translated-label exit 1 HO-GLOSS-ETYM; dropped-entry 19 entries + preflight;
#     placeholder-field exit 0 findings=[] preflight=[]  ← F-2; floating exit 1 HO-DEP-FLOAT; malformed exit 2 HO-DATA;
#     renamed-field exit 1 HO-MISSING 15/16

# 6.5 recounts (examples/culture-d2/packet.d2.yml)
grep -c 'evidence: "design-choice' → 118; grep -c 'evidence: "attested-comparator' → 4;
grep -o 'to-verify' | wc -l → 21; grep -c '^  *coupling_note:' → 29; GAR ids → 10; CMAT ids → 9

# 6.6 battery interaction of the frozen baseline (imported, read-only)
python3 - <<'EOF'
import importlib.util
spec = importlib.util.spec_from_file_location("bat", "tools/check-gate-battery.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
rep = mod.inspect_baselines(mod.BASELINE_ROOTS)
print([b["baseline"] for b in rep["baselines"] if b["gate"] is None], rep["summary"]["baseline_exit"])
EOF
#   → ['expected/handoff-exercise/r11/expected.json']  2   (findings list in F-3)
```

## 7. Limits

- Stamped: tool sha `38d1cba4`, baseline `1ab17670`, packet `2a058f78`, at 22:11Z. The wave is still in flight (design.md mtime moved during the window); if any stamped byte changes, this review's field verdict must be re-run (`§6.1–6.3` are cheap) and F-1..F-4 re-checked before they are cited as met or unmet. F-1..F-4 were each observed once by this seat; F-1/F-2 verified by direct re-run, F-3 by importing the battery's own inspector, F-4 by reading both documents.
- The scratch tools (`review_assist.py`, `term_check.py`, `glossary_trace.py`, `review_trace.py`, `controls_probe.py`) are reviewer instruments under `.scratch/r11-o16/` (gitignored, pruneable); the review does not depend on their survival — every load-bearing result is printed in §6.
- `to-verify` for the parent: whether `.scratch/handoff-*` temp dirs from crashed selftests should be cleaned (this seat's runs honoured TMPDIR; nothing was written under `/tmp`, and no file outside `.scratch/` and this report was touched).

## 8. Adjacent observations (reported, not absorbed)

- At 22:04Z the working tree showed modifications to **filed earlier-round bytes**: `reports/round-10/coverage/index-update-22.md` (an appended "Scratch prune (recorded after filing)" paragraph — a post-filing edit of a filed byte) and `reports/round-{5,6,7,8,9}/validation.json` (large diffs, e.g. round-5 −361 lines; round-9 shows stdout_sha256 re-measurements). These look like side effects of round-11 re-runs of earlier rounds' validation commands (claim F's campaign) and one scribe annotation, not this seat's writes — parent to confirm sanction under the round's "filed artifacts are read-only" rule.
- The D3 handoff prose (`examples/culture-d3/handoff.md`) and `README.md`/`ASSEMBLY.md` carry stale digests (contract `50c4f2f2…`, freeze `74496aa8…`, D2 packet `54be6319…`); the exercise re-measures around them and OQ-01..05 of its packet records the class. Documentation drift is already on record (round-9 `contract-crosscheck.md` F-1 chain); noted here only so it is not re-discovered as new.

---

## 9. Post-stamp addendum — revision flux inside the observation window (appended 22:15Z; §9 corrected 22:16Z — the "22:18Z" originally written here was a pre-write estimate; observed clock at append was 22:15Z)

The exercise tool was rewritten while this review was being filed. Re-verification of the standing findings against the newest observed revision, so the parent can integrate without re-deriving this seat's work:

Observed tool shas (this seat's measurements, all 2026-10-17, ~22:07Z–22:15Z): `38d1cba4` (19:07:36 local; the revision §0–§8 stamp and review object) → `c896eb14` (19:12:43) → `5e2be805` → `6d3a34d0` → `e4301461` → `eaf2eb65` → `d7f26a6a` (§9 as first written). The writer is converging on the design; the deltas below are what moved.

| finding (as filed at 38d1cba4) | status at latest observed revision | evidence |
|---|---|---|
| F-1 `--selftest` crashes — fixture misses `examples/culture-d2/components/*` | **OPEN** at every revision observed | `MissingArtifact: read-set file unreadable: examples/culture-d2/components/02-phonology.yml (…/frozen-root/examples/culture-d2/components/02-phonology.yml)`; READ_SET still lists the 4 D3 components only (no `culture-d2/components` string anywhere in the tool at `d7f26a6a`). Repro: §6.2 |
| F-2 placeholder control cannot fire | **ADDRESSED** | the invisible `TBD` control is gone; the matrix now includes design §9's probes, e.g. `malformed-02 blank scope value` expecting `HO-EMPTY` (tool lines 1611–1613 at `6d3a34d0`) |
| F-3 baseline under `tools/gates/expected/**` | **ADDRESSED (structurally)** | default baseline is now `reports/round-11/handoff/expected.json` (`BASELINE_DEFAULT`, tool line 85 at `6d3a34d0`); the forbidden-path directory was removed (gone by 22:15Z); battery `inspect_baselines` over the committed roots now lists only the 5 pre-existing baselines with no findings from this file. Remaining: the new default file is not yet frozen — a plain run exits 2 `E2E-BASELINE` until someone runs `--freeze` |
| F-4 CLI/constants deltas vs design §10/§3 | **ADDRESSED** | `--root/--baseline/--keep/--json` present; `E2E-BASELINE` / `E2E-DIGEST` observed in output; `PACKET_ID=kotodama.handoff.d2d3-e2e`, `PROFILE=kotodama-handoff-e2e/1`, `PACKET_VERSION=1.0.0` match design §3 |

New cross-shard observation (freeze-ordering hazard, design §11 foretold it): `examples/culture-d2/typed-labels.d2.yml` moved during the window — `e70ba147…` (§0 stamp) → `a3aa452c…` (measured 22:15Z) — the D shard's wiring landing. A baseline frozen before that move now fails closed: observed `FAIL input-digest: examples/culture-d2/typed-labels.d2.yml: frozen e70ba1477dbe… live a3aa452cd5ae…` + `E2E-DIGEST`. The O baseline must be re-frozen after the D2 side stops moving.

Envelope verdict refreshed on the post-stamp revision (packet captured via a scratch freeze at the latest observed tool sha): packet `72739729786a21fd7d3d41c6291c8137efa8dfa8ed12e27c6250c742e89b1f46` (`.scratch/r11-o16/freeze-v4/packet.md`, 21-file read set, 31 509 bytes) — gate exit 0 `fields=16/16 glossary-entries=20 findings=0`; 16 fields with no placeholder hit; **34/34** digest tokens match live bytes; 40/40 glossary term cells ∈ live sets. So the assigned question stays answered the same way at the newest revision: **no field is placeholder-populated; the residual risks are F-1 (selftest) and the pending re-freeze, not envelope content.** Note the packet no longer carries a self-digest row for the exercise tool (grep `exercise-handoff-e2e` → the intro sentence only), which matches design §8's "the exercise's own script is not self-pinned".

Re-verification for the parent once the wave settles (cheap, ~1 min):
```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --freeze .scratch/parent-refreeze      # by the owner of the baseline write
python3 tools/exercise-handoff-e2e.py --baseline .scratch/parent-refreeze/expected.json
python3 tools/exercise-handoff-e2e.py --selftest                            # F-1 gate: expect traceback until fixed
python3 tools/gates/handoff-packet-check.py .scratch/parent-refreeze/packet.md
```

---

## 10. Later same-window update — F-1 fixed; baseline committed and now stale vs the D-side move (stamped 22:16Z)

Measured after §9 was written; supersedes the §9 rows it names:

- **F-1 FIXED** at tool `e74e5aeaea7f1315fec745a25603b7952a50999afc995aad68bc8d33f7e65024` (measured 22:15Z): `python3 tools/exercise-handoff-e2e.py --selftest` → **exit 0**, "selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0) plus 17 controls", including malformed-01..10 (blank `scope` → `HO-EMPTY`; canon marker/claim probes; hyphenated heading; no-heading input → `HO-DATA`), the dropped-glossary-row preflight failure, the scope-notes hazard probe, read-set preservation, tamper baseline/read-set/scan controls, and missing-artifact. The §9 re-verify line "expect traceback until fixed" is superseded.
- **F-2 re-confirmed addressed**: the control matrix is the design §9 set; the selftest list above shows the `HO-EMPTY` probe firing.
- **F-3 closed, but re-freeze is still owed**: the baseline now exists at the design-compliant path — `reports/round-11/handoff/expected.json` sha `c8abc7990bded965b376e85999224a67d349c5b2fdd81070a7c05eda6c09ad0b` with `packet.md` `87523e3db7ec1b5b738f9ff38952236a76c908e96edb7a1802f4c10c39338e3c` (freeze.txt: gate exit 0, 16/16, 20 entries; read set 21 files; 13/13 component digests). It was frozen **before** the D shard's `typed-labels.d2.yml` move, so a plain `python3 tools/exercise-handoff-e2e.py` now exits 1: `FAIL input-digest: examples/culture-d2/typed-labels.d2.yml: frozen e70ba1477dbe… live a3aa452cd5ae…` + `E2E-DIGEST`. Re-freeze after the D side stops moving; this is the fail-closed behaviour working as designed, not a defect.
- **Envelope check on the committed frozen packet** (`reports/round-11/handoff/packet.md`, 87523e3d, this seat's suite): gate exit 0 `fields=16/16 glossary-entries=20 findings=0`; 16 fields, no placeholder hits; 40/40 glossary term cells ∈ live sets; 34 digest tokens → **32 matched, 2 unmatched — both are the same stale `typed-labels.d2.yml` value `e70ba147…` at packet lines 46 and 67**, i.e. the packet's own record of the pre-move digest, which the re-freeze will refresh. No placeholder finding at any revision observed.
- Sibling note: `reports/round-11/handoff/review-17.md` (O17, glossary quality) reviewed the pre-revision freeze at `38d1cba4`/old baseline path; its object has since been superseded by the committed freeze above, and its `--selftest` defect is the same F-1 this review tracked to its fix.
