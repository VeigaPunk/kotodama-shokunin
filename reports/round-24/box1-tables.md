# Round 24 — SHONEN box 1a verification: SKILL.md decision tables, error patterns, checklists (adversarial citation-resolving pass)

- Date: 2026-10-18. Seat: round-24 swarm worker, **box 1a (tables)**.
- Reviewer status: **non-author** — this seat authored none of the lane's
  artifacts (no commits, no LOG/SCORECARD/SHONEN/SKILL edits; only this file
  and `.scratch/` written). Verdict feeds claim C
  (`reports/round-24/claims.json`); the promotion DECISION stays
  operator-owned.
- Scope: box 1 — "SKILL.md contains real decision tables, error patterns,
  checklists, cited sources" — as an adversarial citation-resolving pass over
  the current bytes (SKILL.md is 598 lines at review baseline; the round-23
  survey's 488-line measurement predates the R23-D subsection). Starting
  pointers: `reports/round-23/shonen-survey.md` §2 box-1 table.

## Verdict: **verified-with-conditions**

The tables, error patterns, and checklists are **real**: 143 distinct citation
tokens across 88 distinct cited files, all of which exist; every cited line
locator is inside its file's range; the deep semantic pass found the cited
bytes **support the rows they ground** in every case checked, most verbatim.
No fabricated source, no contradiction, zero S1 findings. Conditions are
pointer-level defects only: 6 stale/wrong line pointers, 2 unresolvable
section anchors, and 3 stray Markdown fences. These are fixable without
touching any filed artifact of rounds 8–23.

## Method (all commands run 2026-10-18 in the live worktree, HEAD `8fbcee9`)

1. Extracted every repo-relative citation (`corpus|reports|tools|examples|out`
   + `.md/.py/.yml/.json/.tsv`) with optional `:loc`, plus bare `` `:nnn` ``
   back-references — 143 distinct tokens / 88 files
   (`.scratch/extract_cites.py`).
2. Existence check on all 88 files → 0 missing. Line-locator range check → 0
   out-of-range, 0 malformed.
3. Dumped and read every cited line range (57 distinct `(path,loc)` targets,
   `.scratch/cited_dump.txt`, 406 lines) and compared each against the
   SKILL.md row that cites it.
4. Grepped every `§`-section reference for a real header in its target file.
5. Verified tool-line claims by reading the cited source context; verified
   JSON/TSV/commit pins by loading the bytes (`expected-holds.json`,
   `typed-pipelines.json`, `deployed-replay.json`, both `MANIFEST.tsv`s,
   `git show 0e81d9d`).
6. Re-ran today the two executable authorities cited by the audited sections:
   `python3 tools/harness/packet_uncertainty.py --selftest` → exit 0 (19
   checks); `python3 tools/d2-typed-labels.py --selftest` → exit 0 (matches
   the 163/163 receipt at `reports/round-22/bleed/impl.md:54,70`).
7. Re-ran the dated greps the tables assert: `grep -ci uncertainty
   tools/gates/handoff-packet-check.py` → **0** (SKILL.md:386 says 0, dated
   2026-10-17 — still true today); `ls corpus/knowledge/civilizations/*.md |
   wc -l` → **94**, of which **2** `*primary-sources.md`
   (SKILL.md:438-442 "94 entries: 92 bases plus two source maps" ✓).

## Findings (rows/pointers that fail, with severity)

Severity scale: S1 = citation missing or contradicting its row (none found);
S2 = citation resolves to the right file but the cited location does not carry
the support (wrong/stale line, unresolvable section anchor); S3 = artifact
defect that does not affect citation truth.

| # | Sev | SKILL.md row | Defect | Verified support (control) |
|---|---|---|---|---|
| F1 | S2 | :213 (Derivation replay, Determinism row) | cites `tools/assemble-d4-typed.py:369` for "two consecutive builds are not byte-identical"; :369 is an unrelated `result["problems"].append(detail)` in the projection-freshness branch | message is verbatim at `tools/assemble-d4-typed.py:387`; row also grounded by `reports/round-18/d4/determinism.md` §3 (exists) |
| F2 | S2 | :171 (Slot-label routing T3) | cites `tools/d2-typed-labels.py:622` and `:793` for "projects every `form_slots` entry as a label" / "each owed slot then emits its own hold"; :622 is a metadata dict, :793 a dedup key — neither is the claimed operation | actual anchors: `:639-641` (`for slot in packet.get("form_slots") … labels.append(_form_slot_label(...))`) and `:810-813` (`_fail(findings, D2L_FORM, …)`) |
| F3 | S2 | :171 | cites `reports/round-18/d4/holds.md` §4.2 — no `4.2` anchor exists anywhere in the file | §4 ("Reconciliation B — the delivered tree's own declaration (6 holds / 0 notes / 0 fails)", `holds.md:131`) carries the six-`GAR-0n` substance (six slots keyed twice, `form_slots:` at `packet.d4.yml:2124`) |
| F4 | S2 | :331 | cites `reports/round-22/bleed/design.md` §3 — the file has no numbered sections (headers: Decision / Source-level change contract / Expected D4 delta / Required paired controls / Integration obligations / Draft rule) | the "skipped, not faked" rule itself is proven at `tools/d2-typed-labels.py:3343` ("family: the leg the d4 packet does not declare is skipped, not faked"); design-side anchor exists only as an unnumbered header |
| F5 | S2 | 5 stale corpus pointers | `era-language-staging.md:114` (SKILL :183) → actual :111; `era-language-staging.md:124` (SKILL :376) → actual :127; `naming-collision-gate.md:52` (SKILL :379) → actual :54; `naming-collision-gate.md:69-70` (SKILL :378) → actual :72; `garment-lexicon-crosslinguistic.md:26` (SKILL :373) → actual :28/:30. Consistent +2/+3 line drift; the last is also a bare name (no directory) that lives under `corpus/knowledge/culture-material/`, not `synthesis/` | all five quotes verified verbatim at the actual lines ("type every label" header; "Apply sound laws to an **inherited spoken label**; separately track … translation, exonym, or official replacement"; "A shared garment label need not mean identical cut or status"; "A collision in that output channel, not native-script identity"; "the loanword switched referent in transit" + "two coexisting names") |
| F6 | S3 | whole file | stray code fences at SKILL.md:129 (a 4-backtick opener), :154 and :217 (3-backtick lines that cannot close a 4-backtick fence). In strict CommonMark the unclosed `````` fence at :129 swallows the remainder of the document into one code block | bytes/truth of all citations unaffected (this audit read raw lines); fix is deletion of three lines; control = re-render after fix |

## Verified support inventory (positive findings — what makes the tables "real")

- **Decision table (SKILL.md:20-28)**: all six rows name corpus surfaces that
  exist, including the bare-name pair `dress-through-eras` +
  `costume-semiotics` (both at `corpus/knowledge/culture-material/`).
- **Label-typing table (:40-73)**: grounding range
  `era-language-staging.md:108-124` contains the §7 "type every label" table;
  T1-T5 thresholds ground at `loanword-material-dating.md:43-57` (six corpus
  steps; the ≥2-of-5 threshold is honestly labeled "house rule"),
  `language-contact.md:56-62` (WOLD 1,460 meanings / 41 languages / ≈24% /
  "no language in the sample is loan-free" — verbatim), `:78-79`
  (phonotactic filtering), `costume-language-coupling-table.md:43` (exact
  reject-condition row). Executable authority
  `tools/d2-typed-labels.py` re-run today: `--selftest` exit 0.
- **Uncertainty table (:97-101, partition crosswalk :103-128)**: every
  protocol line-quote verbatim — `to-verify-triage-protocol.md`
  :16/:17/:18/:19/:21/:32/:70/:76/:80/:97/:100/:112/:139/:181/:182;
  `worldbible-integration-contract.md` :63/:64/:92-106/:100/:102/:104/:120/:179;
  `provenance-audit-ledger-format.md:12`; v1-defect rows
  `reports/round-11/handoff/packet.md:82,88,95,108`;
  round-12 reject `reports/round-12/adjacency/contract.md:9-10,11,23,27-28`;
  `reports/round-15/claims.json:14`; §2/§2.2/§2.3 of
  `reports/round-15/handoff/v2-design.md` all exist. Executable authority
  `tools/harness/packet_uncertainty.py --selftest` → exit 0 today.
- **Slot-routing table (:146-153) + T1-T4 (:158-187)**: gate legs exist —
  `L1-routing` `typed-pipeline-gate.py:582`, `L2-channel` :617,
  `L3-routing-consistency` :736-753 (with the exact "holds … vs routed …"
  message), banner "every hold below is still open design debt" :90;
  `ROUTED_KINDS` `assemble-d4-typed.py:65`; `text_payload` :296-310;
  worked instance `examples/culture-d4/packet.d4.typed.yml` +
  `expected-holds.json` — keys exactly
  `{counts, holds, notes, packet_sha256, projection_sha256, projector_sha256, schema}`,
  counts `{hold:12, note:0, fail:0}`, `supersedes_pins` =
  projection `cbcf997f…` / projector `76536a92…` as SKILL :319-320 quotes.
- **Derivation-replay table (:205-216)**: `SERIALIZER` :62, flagless argv
  `[python3, <gate>, <input>]` `tools/replay-frozen.py:25`, profile store
  `tools/gates/typed-pipelines.json` (schema `kotodama-typed-pipelines-v1`,
  profile `d4`, sha256 pins on packet/assembler/projection/adapter/expected,
  `repin_history` length 3 with `repin_history[2]` binding
  projector+expected), deployed replay receipt
  `reports/round-22/bleed/evidence/deployed-replay.json`
  (`peer_snapshot_pairs_checked: 33`, dated 2026-10-18T14:56:01Z — exact),
  `d4-repin/MANIFEST.tsv` = 3 data rows + header; anti-circularity and
  frozen-run-standard §-anchors all resolve; SCORECARD.md:176-177,185 and
  LOG.md:3252-3253 carry the round-trip corruption class as cited.
- **Family-clean table (:287-295) + warning (:271-285) + T1-T4 (:299-331)**:
  all 14 cited `tools/d2-typed-labels.py` control lines verified verbatim
  (:2471 `DEFAULT_FAMILY`, :2636-2732 `P-FAMILY-SOURCE`/`P-FAMILY-RANK`,
  :2837-2838 family dispatch, :2980 `_selftest_family`, :2989/:3011/:3024/
  :3032/:3045/:3053-3054/:3063/:3073/:3099/:3109/:3114/:3119/:3343); the
  `:2613`-at-`46a03257` historical claim was not byte-re-verified against
  that revision (out of time budget) but its current-tree companions
  (`:925-1197` embedded constants region, `:1235-1258` no-arg helper +
  `build_payload()` at :1255) resolve. Round-22 receipts
  (`analysis.md:18,60,103-110`, `impl.md:54,60,64,70`, `repin.md:15,18,26-37`,
  `corpus/lessons/round-22.md:19,53,63`) all verbatim. The "Landed at the
  round-23 baseline `0e81d9d`" pointer resolves exactly:
  `git show 0e81d9d:tools/d2-typed-labels.py | sha256sum` → `2819f687…`,
  the projector digest SKILL names.
- **Error patterns (:356-379 + status table :381-393)**: 25 observation rows;
  all supplement anchors resolve with exact line hits —
  `22-label-representation.md:126-128/:129-130/:131-132/:133-134` (the five
  numbered rules), §1, and 15 hits for `10/10|PHON-INVENTORY`; all other rows
  ground as detailed under F5 or verified verbatim (loanword-dating :26
  clock table / :57 selection bias / :60; contract :120/:179/:183-region;
  protocol :112/:139). The dated grep claim (:386) re-verified → 0 today;
  `handoff-packet-check.py:651` fixture ledger header verbatim (five columns,
  none `uncertainty`).
- **Boundaries (:395-406) and Checklist (:408-420)**: checklist item 1's
  prose-gap record resolves (`reports/round-10/drift/shard-06.md` §06-G at
  :53/:68); item 2 grounds at `source-discipline-calibration.md:67`
  (S/C/H/R/U/V verbatim) and the `missing-calibration` family exists
  (`tools/gates/fixtures/provenance/defect-missing-calibration.md`).
- **Corpus map (:422-442) / Using the evidence (:444-459)**: six partitions
  exist; civilizations = 94 = 92 + 2 source maps; all six supplement finding
  pointers exist (`21-`…`25-` files); the frozen-replay row's recipe is
  recorded in `reports/round-10/drift/fix-18.md` ("live exit 2 →
  pinned-revision recipe", "7/7 `gate_digest_mismatch`", restore from
  `291c714`).
- **Gates registry (:461-519)**: all 7 gate scripts + fixture pairs +
  `provenance/` fixtures + `replay-frozen.py` + `source-audit-inventory.py` +
  `assemble-d2.py` + `check-craft-exercise.py` + `check-gate-battery.py` +
  `examples/supplement-opencode-1/sound-change-vs-taboo.json` exist; the
  battery row's exit-2/`BASELINE-GATE-UNCOVERED` claim grounds at
  `reports/round-9/baselines/registry.md` §5 **item 6** (verbatim: exit 2
  with `gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]`;
  `--baselines-root` three-root run → exit 0) and
  `reports/round-10/drift/fix-21.md`; the LAW-ORDER limitation grounds at
  `reports/round-5/15-cli-review.md:57` (§F4). `29-local-boundaries.md` §F1
  (:37 "five of seven gate selftests overwrite their committed fixtures in
  place") grounds the five-fixture-writing sentence.
- **Round-5/6 constraint tables (:521-544)**: `08.json` (meso-13),
  `parent-source-spotchecks.json`, `parent-reconciliation.json`
  (`KIN-A07` "unresolved" at :20), round-6 reconciliation, SR-REG-07
  (`reports/round-5/14-source-review.md`), and both appended errata exist
  verbatim (`india-vedic.md:198` "Round 6 source erratum — Gobhila timing…";
  `persia-achaemenid.md:172` "Round 6 access-status erratum — Old Persian
  administrative isolate"; `phonetics-phonology.md:70` PHON-A11).
- **D3 section (:546-598)**: `d3-contract.json`, both gates, `packet.json`,
  `packet.gates.yml`, `expected.json`, `integration-attempts.json`,
  `native-request-binding.json` all exist.
- **Canonical box state re-measured**: `git log --oneline --all -- SHONEN.md`
  → 1 commit; `grep -c '^- \[ \]' SHONEN.md` → 4. This seat marks no box.

## Scope and limits

- Read-only plus `.scratch/` and this report; no validator run, no commits;
  no filed artifact of rounds 8-23 touched.
- The `:2613`-at-revision-`46a03257` claim was accepted on its current-tree
  companion anchors plus the filed receipts, not re-diffed against that
  historical revision.
- Full gate-battery / cold-run re-execution belongs to the box-3 and claim-D
  seats; here only the two selftests directly cited by the audited tables
  were re-run (both exit 0).
- The six S2 pointer defects and F6 belong naturally to claim D's staleness
  audit; they are handed over here as findings, each with its verified
  correct anchor so the fix needs no rediscovery.

## Conditions attached to this verdict

1. Correct the 6 wrong/stale line pointers (F1, F2, F5) to the verified
   anchors listed above.
2. Repair or replace the 2 unresolvable section anchors (F3 → holds.md §4,
   F4 → name the actual design.md header).
3. Delete the three stray fences (F6) and confirm the file renders as
   headings/tables (control: Markdown render or `grep -c '^```' SKILL.md`
   → 0 unclosed pairs).
