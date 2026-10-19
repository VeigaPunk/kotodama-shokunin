- Seat: C08 | verifier | C | date 2026-10-19 | baseline da68a6d

# C08 — verification of the C03 SKILL-anchor reissue rows (claim C)

**Mission** (`reports/round-34/targets.json`, seat C08): "Verify every C03 reissue row:
old anchor exists as cited, new anchor exists, content matches."

**Dependency state at my reads (2026-10-19T07:0xZ, method in §1):** `reports/round-34/`
contains only `claims.json`, `targets.json`, `telemetry/` — no `calib/`, `scout/`, or
`craft/` directory, so `reports/round-34/calib/C03-anchor-reissue.md` and
`reports/round-34/scout/K04-anchor-census.md` are **absent**. Per the missing-dependency
rule this fragment does every part that does not need C03's bytes: it derives the
independent ground truth the reissue rows must equal (§3), states the acceptance checks
each row must pass (§4), and independently reproduces the two executable artifacts the
reissue reasons about (§5). The row-by-row verdict against C03's actual table is owed
(`## Owed`). No file outside this fragment was written; every command below is read-only.

## 1. Verified inputs (digests measured this window)

| artifact | identity | digest | size | command |
|---|---|---|---|---|
| pre-edit SKILL.md | `17e90b9:SKILL.md` | `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d` | 715 lines | `git show 17e90b9:SKILL.md \| sha256sum` |
| current SKILL.md | HEAD `da68a6d:SKILL.md` | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | 732 lines | `sha256sum SKILL.md` |
| round-14/15 census SKILL.md | `b02cfbc:SKILL.md` | `52d5f4d1be6ac97a143323306eafa9c9649484f25de60de8a3ee7630d8c6792c` | 305 lines | `git show b02cfbc:SKILL.md \| sha256sum` |
| round-19 census SKILL.md | `16652e8:SKILL.md` | `e8d238a6377bc4135027c06b4320e3ab7b6937c1276164be986cf670db6d23f8` | 375 lines | `git show 16652e8:SKILL.md \| sha256sum` |
| AGENTS.md at `139e3b6` | pre-round-33 | `1afaf106f20b440ad263ab231c215773436c7f42ab106848f5550b87ecf41035` | 42 lines (line 42 = the "append one item … (after :534)" instruction) | `git show 139e3b6:AGENTS.md \| sha256sum` |
| AGENTS.md at HEAD | post-round-33 | `5ae7a9c8abab0843cfc6db09849f2fff369c0e880085deb546ec7ab764333808` | 40 lines, no `SKILL.md` mention | `sha256sum AGENTS.md` |

The two era blobs are the digests the citing rows themselves name: `round-15.md:25` cites
the pre-round-15 revision, and `round-19.md:179` states "`SKILL.md` @ `e8d238a6…`
(unchanged since the census)" — the census blob is `16652e8:SKILL.md`.

**Map method.** Line mapping is `difflib.SequenceMatcher` (no autojunk) over the 715- and
732-line texts, not arithmetic inference; `old→new` is reported only for unchanged lines
(`replace`/`delete` lines get `None`, i.e. "content changed or removed"). Subject probes
are `grep -n` patterns per §3's subject column.

## 2. Measured shift map (the reissue's arithmetic)

`git diff --numstat 17e90b9 HEAD -- SKILL.md` → `35  18  SKILL.md` — the round-33 edit is
**not** line-count-neutral (A09's R5 asked for neutrality *or* a recorded shift; the shift
landed). Hunks: `@@ -125,7 +125,7 @@`, `@@ -476,19 +476,19 @@`, `@@ -498,7 +498,7 @@`
(net 0 each), `@@ -581,7 +581,9 @@` (**+2**), `@@ -691,17 +693,31 @@` (cumulative **+16**),
`@@ -711,5 +727,6 @@` (final **+17** = 35−18).

| old lines | Δ to new | probe evidence |
|---|---|---|
| ≤ 581 | **0** | old :47→:47, :149→:149, :183→:183, :294→:294, :522→:522, :534→:534, :536→:536 all IDENTICAL (sha8 per line) |
| 582–586 | 0 (inside hunk 3; no cited anchor lands here) | per-line map |
| 587–707 | **+2** | :587→:589, :660→:662, :710→:726 (region end), Gates table header :602→:604 |
| ≥ 708 | **+16** | :708→:724, :713→:729 |

*Consequence:* any reissue table that applies one uniform shift (e.g. "+17" or "732−715")
to every anchor is falsified by row G1–G8 below, whose Δ is 0.

## 3. Reissue ground truth — what C03's rows must equal

`Citing rows` are the filed citations A09 §2.4/R5 names (plus the completeness rows in
G20). `Pre-edit addr` is measured against `79fe91d3`; `New addr` against `f9bd07c2`.
"IDENTICAL" means the full line bytes are equal at both addresses (sha8 shown); every
subject was confirmed present at both addresses by the stated grep.

| id | owning A09 row | citing filed row:line (citation) | era addr (era blob) | pre-edit addr `79fe91d3` | new addr `f9bd07c2` | Δ | content verdict |
|---|---|---|---|---|---|---|---|
| G1 | R5 | `SKILL.md:149`, `:183` (self-cite `:47`) | — | `:47` | `:47` | 0 | IDENTICAL `5d312375` |
| G2 | R5 | `SKILL.md:149` | — | `:149` | `:149` | 0 | IDENTICAL `24c407be` |
| G3 | R5 | `SKILL.md:183` | — | `:183` | `:183` | 0 | IDENTICAL `212702dc` |
| G4 | R5 | `round-31.md:46` (`:294` = `mirror_unsafe` exit-2 r24 cold-run control) | — | `:294` | `:294` | 0 | IDENTICAL `92762b1b`; `grep -n mirror_unsafe` → `:294` both |
| G5 | R5 | `round-31.md:46` (`:456-458` mirror-safety prose) | — | `:456-458` | `:456-458` | 0 | IDENTICAL 3/3 lines; `grep -n "mirror-safety leg that rejects"` → `:457` both |
| G6 | R5 | `round-31.md:46`; `round-32.md:57`; `lessons/README.md:244` (`:522`, `:522-534`) | — | `:522` (`## Checklist (executable where a tool exists)`) | `:522` | 0 | IDENTICAL `2bb65d58`; range `:522-534` 13/13 lines identical |
| G7 | R5 | `round-31.md:46` (`:534` last content line, `:535` blank, `:536` `## Corpus map`) | — | `:534`/`:535`/`:536` | same | 0 | IDENTICAL `2f25f62c` / empty / `79504425` |
| G8 | R5 | `round-25.md:44` (`:189-214`, round-trip-corruption row) | — | `:189-214` | `:189-214` | 0 | IDENTICAL 26/26; row itself `:210` `772e80ff`, `grep -n "regex backslashes"` → `:210` both |
| G9 | R5 | `round-32.md:33` (`:660` D3 heading) | — | `:660` | `:662` | +2 | IDENTICAL `361e248e` |
| G10 | R5 | `round-32.md:7,33` (`:710` pre-item hunk context) | — | `:710` | `:726` | +16 | IDENTICAL `08c1b59c` |
| G11 | R5 | `round-32.md:41,55,57`; `lessons/README.md:242,244` (`:713-715` item; `:715` audit) | — | `:713-715` | `:729-732` | +16 | **CONTENT-CHANGED**: `:713`→`:729` IDENTICAL `3506a41b`; old `:714`,`:715` replaced by new `:730-732` (item grew 3→4 lines; audit re-keyed — see §5) |
| G12 | R5 | `round-32.md:58`; `lessons/README.md:245` (`:294`-class cell) | — | `:294` | `:294` | 0 | IDENTICAL (same line as G4) |
| G13 | R5 | `round-14.md:141` (`:208` pre-fix battery row) | `b02cfbc:208` = battery row ✓ | `:615` | `:617` | +2 | identical at mapped address `65f49ee2`; **at `:208` of `79fe91d3` the subject is absent** (line = "Named inputs" row) |
| G14 | R5 | `round-15.md:25` (`:157` uncertainty prose) | `b02cfbc:157` = "contents. A disappearing uncertainty marker is not a verified claim." ✓ | `:564` | `:564` | 0 | identical at mapped address `4e9faf26`; **absent at `:157` of `79fe91d3`** (line = `ROUTED_KINDS` adapter line) |
| G15 | R5 | `round-15.md:25` (`:205` `uncertainty-inventory` probe row) | `b02cfbc:205` ✓ | `:612` | `:614` | +2 | identical `76769341`; **absent at `:205` of `79fe91d3`** (line = "Replay requirement" table header) |
| G16 | R5 | `round-19.md:88,179` (`:278` battery row, quoted verbatim) | `e8d238a6:278` = battery row ✓ | `:615` | `:617` | +2 | same line as G13; **absent at `:278` of `79fe91d3`** (line = rank_rules fragment) |
| G17 | R5 | `round-19.md:100` (`:323-375` D3 precedent section) | `e8d238a6:323` = D3 heading, `:375` = EOF line ✓ | `:660-…` (heading `:660`) | `:662-…` (heading `:662`) | +2 | section heading identical `361e248e`; **absent at `:323` of `79fe91d3`** (line = caution prose) |
| G18 | R5 | `round-19.md:101` (`:262-278` "Gates and probes" table, 12 rows) | `e8d238a6`: heading `:238`, header `:265`, 12 data rows `:267-278` (last = battery row) — range head `:262` is prose | heading `:575`, header `:602`, 12 data rows `:604-615` | heading `:575`, header `:604`, 12 data rows `:606-617` | +2 | table content identical (12/12 rows); **absent at `:262-278` of `79fe91d3`** |
| G19 | R5 | `AGENTS.md:42` ("append one item … (after :534)") | `139e3b6:42` ✓ | — | — | **removed** | line deleted by `da68a6d` (`@@ -37,6 +37,4 @@`, −2 lines); `grep -n "append one item\|after :534\|SKILL\.md" AGENTS.md` at HEAD → 0 hits |
| G20 | completeness (not in A09 §2.4) | `lessons/README.md:242,244,245` (Q-32-1 `:715`; Q-32-3 `:713-715` + `:522-534`; Q-32-4 `:294`) | — | as G11/G6/G12 | as G11/G6/G12 | 0/+16 | rows resolve; see finding C08-F4 |

Content-change detail for G11 (`diff -u` of the item): old `:713-715` =
`- [ ] Every availability/dispatch record filed \`open-at-seat-close\` whose round's` /
`validation.json has landed carries a closing snapshot in that round's telemetry/` /
`(audit: … closing-snapshot.json …)`; new `:729-732` keeps line 1, then
`carries a closing snapshot in that round's telemetry/ whose` /
`\`closes\` names that record and whose \`closes_sha256\` matches the record's live bytes` /
`(audit: … availability-close-*.json … closes_sha256 …)`. So for G11 "content matches" is
true only for the item's first line; the item body is a *deliberate revision* (Q-32-1
disposition) and the row must record `content-changed`.

## 4. Acceptance checks each C03 row must pass (applied once C03 lands)

Checks A–F are mechanical; a row failing any is unverified:

- **A — old anchor exists as cited, at the right revision.** For G1–G12 (contemporary
  citations): `git show 17e90b9:SKILL.md | sed -n '<old>p'` must carry the cited subject.
  For G13–G18 (era-scoped citations): the row must cite the **era blob digest** and show
  the subject there (`git show <era>:SKILL.md | sed -n '<era line>p'`); it must **not**
  claim the era line number resolves against `79fe91d3` — measured false for
  `:208`, `:157`, `:205`, `:278`, `:262`, `:323` (counterexample lines in §3).
- **B — new anchor exists.** `sed -n '<new>p' SKILL.md` carries the subject; single-line
  rows: `sha256` of the line must equal the §3 sha8 (ID 0-row transfer); range rows:
  every line identical.
- **C — content matches, class-correct.** IDENTICAL rows must be byte-equal; G11 must be
  recorded `content-changed` with the new body, not silently mapped; G19 must be recorded
  `removed` with the removing commit `da68a6d` and the 2-line diff.
- **D — Δ equals the measured map.** Δ ∈ {0, +2, +16} per §2 — a uniform shift is wrong.
- **E — completeness.** G20's three README rows must appear (or the omission be recorded
  with an owner); R5's "live anchor" `AGENTS.md:42` cannot be reported as shifted.
- **F — filed bytes untouched.** `git status --porcelain -- SKILL.md AGENTS.md corpus/lessons/`
  → empty at my read (`:0xZ`); the reissue must land as **new rows** under round 34.

## 5. Independently reproduced executable checks (the reissue's reasons)

The item's audit was extracted from each revision and executed verbatim (read-only), cwd
repo root, `TMPDIR=$PWD/.scratch`:

- **Old audit (`79fe91d3:715`) → exit 0, prints 5 records** — `reports/round-19/`,
  `round-25/`, `round-26/`, `round-27/`, `round-28/availability.json`. This independently
  **reproduces round-32 F-X16-3** ("the instrument cannot see the closures").
- **New audit (`f9bd07c2:732`) → exit 0, prints 0 records** — the re-keyed instrument
  (`closes` + `closes_sha256` over `telemetry/availability-close-*.json`) sees the filed
  closures. Q-32-1's disposition is therefore **effective at HEAD**, verified by execution,
  not by reading the draft.

## 6. Named findings

| id | finding | class | evidence |
|---|---|---|---|
| **C08-F1** | "old anchor exists as cited" is revision-relative. The r14/r15/r19 citations resolve **only** against their era blobs (`52d5f4d1`/305 lines, `e8d238a6`/375 lines); against the pre-edit 715-byte revision their line numbers carry different content. A C03 table asserting pre-edit resolution for those rows is false as written. | verification-critical | §1 blobs; §3 G13–G18 counterexample lines |
| **C08-F2** | `AGENTS.md:42` — A09 R5's "live anchor" — no longer exists: `da68a6d` deleted the "append one item … (after :534)" instruction (AGENTS.md 42→40 lines, `grep` → 0 hits). The reissue must record `removed`, not `shifted`. | correctness | `git show da68a6d -- AGENTS.md`; `wc -l AGENTS.md`; §3 G19 |
| **C08-F3** | The availability item both shifted and changed: `:713`→`:729` identical, but `:714-715` → `:730-732` (3→4 lines, audit re-keyed). Byte-diff of the item is required for the row; a bare "`713-715 → 729-732`" hides the change. | correctness | §3 G11; §5 executions (5→0 records) |
| **C08-F4** | Completeness gap in A09 §2.4's list: `corpus/lessons/README.md:242,244,245` (filed round-33 revision) cite `SKILL.md:715`, `:713-715`, `:522-534`, `:294` and need the same reissue rows. | completeness | `grep -n "SKILL\.md:[0-9]" corpus/lessons/README.md`; §3 G20 |
| **C08-F5** | Q-32-3's gap grew: the item sits 195 lines below the checklist's last content line (`:729` vs `:534`; was 179 at r32) and still outside `## Checklist` (`:522-534`). The reissue row must carry the new distance, since the Q row says "move it or cross-reference it". | staleness of the cited distance | §2 map; §3 G7/G11 |
| **C08-F6** | Shift is non-uniform: Δ=0 for old ≤581 (most anchors), +2 for 587–707, +16 for ≥708. A reissue that applies a single offset is falsified by G1–G8. | correctness | §2; `git diff --numstat` |

**Scope boundary (stated, not owed to me):** my mission is the SKILL-anchor reissue rows
(R5/§3). A09's R1, R2, R3, R4, R6, R7, R8 are not line-anchor rows (blob pin, digest
receipts, box-1 re-survey, prose arithmetic, x45/x57 findings, orphan row); their
verification belongs to the C01/C02/C07 surface and the D/O verifiers, and I make **no
verdict** on them. The anchor population beyond R5's named set is larger
(`reports/round-33`: 35 files / 307 refs; `round-32`: 5/20; `round-31`: 3/9;
`corpus/lessons`: 7 files / 19 refs), so a reissue claim of being complete must scope
itself to R5's list plus G20 or record the residue.

## Owed

- `reports/round-34/calib/C03-anchor-reissue.md` — **absent at my reads**
  (`ls reports/round-34/` → `claims.json targets.json telemetry`; no `calib/`). The C03
  row-by-row verdict is owed: the integrator (or a re-dispatched verifier) applies the §4
  checks A–F to C03's actual table against the §3 ground truth, and files any row-level
  discrepancy as a new finding. My §3 table is the independent standard, derived without
  C03's bytes; it is not a substitute for the comparison.
- `reports/round-34/scout/K04-anchor-census.md` — absent at my reads; if K04's census
  disagrees with my §2/§3 addresses, the disagreement is itself a finding and my
  measurements are re-runnable via the §1/§2 commands.
- Per-row verdicts for G13–G18's era-blob citations can only be *verified* once C03's rows
  name the era digests; if C03 maps them from the pre-edit revision instead, C08-F1 stands
  as the rejection reason for those rows.

## Citations

- Seat object: `reports/round-34/targets.json` (seat `C08`: role verifier, claim C, mission
  text, out `calib/C08-verify-reissue.md`); `:shared_rules` array; missing-dependency rule.
- Claim C declaration: `reports/round-34/claims.json:53-66` (after_required, thresholds),
  `:17` axes, `:11-16` dispatch.
- A09 source of the rows: `reports/round-33/adj/A09-pins.md:85-94` (§2.4 E4 line anchors),
  `:107-114` (R1–R8 rows; **R5** = line anchors, row at `:111`), `:124` (A09-F3 AGENTS.md:42).
- Citing filed rows: `corpus/lessons/round-31.md:46`; `round-32.md:7,33,41,55,57,58`;
  `round-25.md:44`; `round-19.md:88,100,101,179`; `round-15.md:25`; `round-14.md:141`;
  `corpus/lessons/README.md:242,244,245`; `AGENTS.md:42` (at `139e3b6`) / none at HEAD.
- Blobs: `git show 17e90b9:SKILL.md` (`79fe91d3…`, 715 lines); `git show b02cfbc:SKILL.md`
  (`52d5f4d1…`, 305 lines); `git show 16652e8:SKILL.md` (`e8d238a6…`, 375 lines);
  `git show 139e3b6:AGENTS.md` (`1afaf106…`, 42 lines); HEAD `SKILL.md` (`f9bd07c2…`,
  732 lines), `AGENTS.md` (`5ae7a9c8…`, 40 lines).
- Commands (2026-10-19T06:5x–07:0xZ, repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `sha256sum SKILL.md`; `git show <rev>:SKILL.md | sha256sum`;
  `git diff --numstat 17e90b9 HEAD -- SKILL.md`; `diff -u <old> SKILL.md` (hunk headers);
  difflib old→new line map (`SequenceMatcher`, autojunk=False) and per-line sha8 probes;
  `grep -n` subject greps (`mirror_unsafe`, `mirror-safety leg that rejects`,
  `disappearing uncertainty marker`, `^| uncertainty-inventory`, `^## Gates and probes`,
  `^## Source-bounded culture drill`, `^## Checklist (executable where a tool exists)`,
  `^## Corpus map`, `^| Round-trip corruption class`,
  `^| Condition | Decision / executable error`, `isolated legacy selftest battery`,
  `regex backslashes`, `BASELINE-GATE-UNCOVERED`, `append one item|after :534|SKILL\.md`);
  table extent scans (§3 G18); verbatim execution of both audit one-liners extracted from
  `17e90b9:SKILL.md:715` and `SKILL.md:732` (exit 0 / 5 records; exit 0 / 0 records);
  `git show da68a6d -- AGENTS.md`; `git log -S "append one item" --oneline -- AGENTS.md`;
  `git status --porcelain -- SKILL.md AGENTS.md corpus/lessons/` (empty);
  anchor-population counts `grep -rl/-rho "SKILL\.md:[0-9]" <area>`.
