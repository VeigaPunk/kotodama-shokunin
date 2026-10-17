# R9 metadata audit — inventory-wide verification (auditor shard, METADATA V12)

- Round 9, auditor shard (METADATA V12): inventory-wide verification over all
  `corpus/knowledge/**/*.md` entries for the three frontmatter fields
  (`source:`, `verified-at:`, `recheck:`), plus a read and independent check of
  every metadata shard fragment.
- Date 2026-10-17 (all commands below run 2026-10-17, ≈20:48–21:0x UTC; `date -u`
  stamps inline). Worktree HEAD `a7bb205` ("round-9: declare claims F/O/D");
  round-9 `baseline_revision` `e1694ba`. `a7bb205` touches no `corpus/` file
  (`git show --stat a7bb205 -- corpus/` empty), so the committed corpus at HEAD
  equals the declared baseline and `git diff -- corpus/` attributes exactly the
  round-9 shard edits.
- Contract audited: fleet `CORPUS.md:17` — "Each `knowledge/` entry **opens with**
  `source:`, `verified-at:` and `recheck:`". Lane gate
  `tools/gates/provenance-audit.py` reads only `topic|sources|couples`
  (`FIELD_NAMES`, line 75), so the metadata trio is gate-neutral by construction.
- Write scope: this fragment is the only file this shard wrote; no corpus entry
  was edited, no commit made. Round-9 targets: `reports/round-9/targets.json`
  `metadata_verify` ("11 shards re-audit all 179 corpus/knowledge entries for
  complete source/verified-at/recheck frontmatter after round 8's sweep; fix
  stragglers in place; fragments under reports/round-9/metadata/ + 1 auditor
  shard").

## 1. Headline result

Single sweep command (the auditor's inventory-wide count; opening block = text
before the first `## ` heading; the source leg read as the contract's singular
`source:`, bundled forms accepted behind a `; ` separator):

```
python3 -c "import re,pathlib;root=pathlib.Path('corpus/knowledge');pat=re.compile(r'(?:^[-*]\s|;\s)(source|verified-at|recheck)\s*:',re.M);files=sorted(root.rglob('*.md'));miss=[(p.as_posix(),d) for p in files for d in [sorted({'source','verified-at','recheck'}-{m.group(1) for m in pat.finditer(re.split(r'^## ',p.read_text(encoding='utf-8'),maxsplit=1,flags=re.M)[0])})] if d];print('files=%d missing_any=%d'%(len(files),len(miss)));[print('MISSING',p,','.join(d)) for p,d in miss]"
```

- **Before (audit start, 20:49:32Z): `files=179 missing_any=83`** — 79 entries
  missing only `source:` (they carry a plural `- sources:` ledger, which the
  literal contract text does not satisfy), plus 4 entries whose trio existed
  only below the first `## ` heading (`mali-songhai`, `citation-format-and-source-registry`,
  `myth-consistency-gate`, `provenance-audit-ledger-format`).
- **After (close of this audit): `files=179 missing_any=64`** — the 64 are:
  `civilizations/` sorted positions 39–57 (19 files), all 16
  `culture-material/` entries, all 16 `linguistics/` entries, and 13
  `verification/` entries (10 missing only the singular `source:` line, 3 also
  the opening-block placement).

Because the round's shards applied two readings of the source leg, the count
above is only one of three defensible measurements. The same logic, run over
the committed baseline (HEAD) and the delivered worktree, gives the round's
change under each reading (identical script, both states; `sources:` counts as
the source leg in B/C):

| reading | definition | HEAD (baseline) | worktree (delivered) |
|---|---|---|---|
| A — strict/literal | opening-block `- source:` (singular) + `verified-at:` + `recheck:` | **83 / 179** | **64 / 179** |
| B — lane/plural | opening-block `- source:` **or** `- sources:` + `verified-at:` + `recheck:` | **4 / 179** | **3 / 179** |
| C — whole-file | any of `- source:`/`- sources:` + `verified-at:` + `recheck:` anywhere | **0 / 179** | **0 / 179** |

B-remainder at close (verbatim): `verification/citation-format-and-source-registry.md`,
`verification/myth-consistency-gate.md`, `verification/provenance-audit-ledger-format.md`
— in each, the trio sits below the first `## ` heading (lines 15–17 / 9–11, first
heading 13 / 6 / 6), so the entry does not literally *open* with it. V11 explains
the non-repair: those three files are digest-pinned by the round-9 O-axis
baseline `tools/gates/frozen/provenance-audit/r9-pre/expected.json`, and the
placement question belongs to the open fleet-text ruling (reported, not absorbed).

Net movement of the round, stated plainly: under the literal reading A the round
fixed 19 of the 83 stragglers (18 added by V05 in `civilizations/` 77–94, plus
`mali-songhai` relocated by V04); under reading B it fixed 1 of 4; under C
nothing was missing before or after. The two readings are not reconciled by this
audit — the contract question was filed with the integrator in round 8
(`reports/supplement-opencode-1/28-corpus-contract.md` §6/§7) and remains open.

## 2. Fragment ledger — every shard read and independently checked

All 11 metadata shard fragments were read in full and their machine-checkable
receipts re-derived here. "Rows" = table rows re-parsed from the fragment and
re-checked against the live tree (field line numbers, first-heading line,
sha256 as claimed); "gate" = the fragment's per-partition gate receipt re-run
by the auditor at close (timestamped below).

| shard | fragment | assignment | edits | auditor check | gate receipt re-run |
|---|---|---|---|---|---|
| V01 | `v01-civ-1-19.md` | civ 1–19 | 3 files (bali/byzantium/carthage, `verified-at` placeholder → dated record) | 19/19 rows, pre-edit digest from `git show HEAD:` and current digest both match; the three cited triage ledgers (`round-1-triage/Z04.md:6`, `Z05.md:3`) exist and contain the named checks (C. Geertz ch. 14, Putra et al. 2020; Buckton 1994, Parani 2003, Haldon 2006, Krahmalkov 2000, Hurst–Stager 1978) | `civilizations` 412/410/0 |
| V02 | `v02-civ-20-38.md` | civ 20–38 | 0 | 19/19 rows; digests equal round-8 `m02` after-values (parsed from `reports/round-8/metadata/m02-civ-20-38.md`), 0 drift | `files=19 marks=100 mark-lines=100 findings=0` |
| V03 | `v03-civ-39-57.md` | civ 39–57 | 0 | 19/19 rows; `git status --porcelain` for the 19 paths empty; 0/19 carry a singular `- source:` (confirms the strict-reading residual is real and reported, not fixed) | whole-dir value recorded in §4 |
| V04 | `v04-civ-58-76.md` | civ 58–76 | 1 file (`mali-songhai`: fused line split, then trio relocated into the opening block) | fragment re-read after its in-flight update; final `git diff` = +3/−1 exactly as its §4; `wc -l` 207 as claimed; `git diff` for the other 18 paths empty | `files=19 marks=84 mark-lines=83 findings=0` |
| V05 | `v05-civ-77-94.md` | civ 77–94 | 18 files (one identical `- source:` pointer line each) | 18/18 stated post-edit digests match; `git diff --numstat` = 18 × `1 0`; the added line is byte-identical across all 18 | `files=18 marks=90 mark-lines=89 findings=0` |
| V06 | `v06-synth-1-12.md` | synthesis 1–12 | 0 | 12/12 rows (six field positions + heading + full sha256); digests are simultaneously HEAD and worktree; its independently derived repo-wide counts (83 strict / 4 lenient) reproduce mine | `files=12 marks=55 mark-lines=51 findings=0` |
| V07 | `v07-synth-13-24.md` | synthesis 13–24 | 0 | 12/12 digest rows match; note: the fragment's "lines" column counts `text.split("\n")` (wc −l + 1: 203/190/183…) where `wc -l`/`splitlines()` gives 202/189/182 — a convention difference, no content discrepancy | `synthesis` 90/86/0 |
| V08 | `v08-linguistics.md` | linguistics all | 0 | 16/16 digest rows match current files; `git status` for the partition empty; its §8 placement list (4 files) matches the auditor's placement sweep | `files=16 marks=29 mark-lines=29 findings=0` |
| V09 | **absent at close** — no `v09-*.md` under `reports/round-9/metadata/` after a 20-minute poll (20:48:45Z–21:08:32Z, 60s then 20s intervals) | myth-symbol all | none written | partition verified directly by the auditor: 16/16 files carry `- source:` / `verified-at:` / `recheck:` exactly once in the opening block (per-file digests in §6); `git status --porcelain corpus/knowledge/myth-symbol/` empty | `myth-symbol` 16 files marks=9 mark-lines=9 findings=0 |
| V10 | `v10-culture.md` | culture-material all | 2 files (receipt upgrades in `material-culture-inference-method`, `era-periodization-models`) | both post-edit digests match; `git diff --numstat` = `1 1` and `2 2`; the external receipt re-fetched here — `api.openalex.org/works/doi:10.69978/rar.v25i2.30` returns W2196576233, *Rock Art Research* 25(2), first page 165, 2008, exactly as claimed | `culture-material` 6/6/0 |
| V11 | `v11-verification.md` | verification all | 0 | 13/13 rows (source form + line, `verified-at`, `recheck`, first `##`, sha256); `git status` for the partition empty; r9-pre baseline file exists and pins the partition; frozen copy digest `7b3bdc80a12b…` unchanged | `files=13 marks=72 mark-lines=72 findings=0` |

Shard fragments written but not in this list: none — V01–V08, V10, V11 were
present and read; V09 is the only outstanding fragment (see §6).

## 3. Attribution of every corpus edit

`git diff --numstat -- corpus/` at close → **24 files, 27 insertions, 7 deletions**,
all claimed:

- V01 (3): `civilizations/{bali,byzantium,carthage}.md` — 1/1 each (one
  `verified-at` value replaced).
- V04 (1): `civilizations/mali-songhai.md` — 3/1 (trio into the opening block,
  fused in-body line removed).
- V05 (18): `civilizations/{persia-sasanian,polynesia-navigation,rapa-nui,rome,ryukyu,scythian-saka,siam-thai,slavs-early,sogdian-silk-road,swahili-coast,taino,thrace-dacia,tibet,turkic-steppe,vietnam,yoruba,zapotec-mixtec,zimbabwe-shona}.md`
  — 1/0 each (one `- source:` pointer line).
- V10 (2): `culture-material/{era-periodization-models,material-culture-inference-method}.md`
  — 1/1 and 2/2 (receipt rewrites).
- Unclaimed edits at close: **0**. No file under `tools/gates/frozen/**` was
  modified by this round's metadata work (three new untracked directories there
  are the O-axis baselines, not metadata edits; `git status --porcelain --
  tools/gates/frozen` shows only `??` entries). The only other entry under
  `corpus/` in `git status` at close is untracked `corpus/lessons/round-9.md`
  (X01 scribe scope, outside `knowledge/`, not a metadata edit).

## 4. Environment receipts at close (auditor-run)

- Provenance gate, per partition (2026-10-17, ≈20:57Z): civilizations 94 files
  marks=412 mark-lines=410; culture-material 16/6/6; linguistics 16/29/29;
  myth-symbol 16/9/9; synthesis 24/90/86; verification 13/72/72 — all
  `findings=0 blocked=0`, exit 0. Whole corpus:
  `INFO scan: files=179 marks=618 mark-lines=612 findings=0 blocked=0` (start of
  audit: 619/613; net −1). The reproducible partition-level anchor is V01's
  civilizations dir, `415 → 412` in its fragment and `412/410/0` here; the
  culture-material close value is `6/6/0`. No metadata edit cleared a marker
  that was not already resolved by a cited record.
- `python3 tools/source-audit-inventory.py --json --summary` → files=179
  raw_lines=610 raw_occurrences=616 markers=584 (bare 555, detailed 29); at
  audit start: 611/617/584 — marker inventory flat, prose counts −1.
- `python3 tools/check-gate-battery.py --selftest` → `SELFTEST OK 28/28 controls
  behaved as expected` (audit start: 10/10 — the O-axis extended the battery
  during the round; not a metadata change).
- `git show --stat a7bb205 -- corpus/` empty; `git diff --stat e1694ba..HEAD --
  corpus/` empty (baseline identity established for every shard's before-state).

## 5. Residuals and divergences (report-only; not absorbed)

1. **The source-leg reading split is the round's dominant residual.** Shards
   V01/V02/V04/V05/V06/V07/V11 apply the literal contract reading (dedicated
   `- source:` line); V03/V08/V10 read the legacy plural `- sources:` ledger as
   the source leg and made no addition (`v08-linguistics.md`: "The operative
   lane field is the plural `- sources:` block"; `v10-culture.md` criterion
   "exactly one standalone `- sources:`…"; `v03-civ-39-57.md` §3.4: "the
   fleet-text question stays with the integrator — no repair attempted here").
   Consequence: 64 entries fail the literal reading while nothing is absent on
   the whole-file reading. The contract ruling is the integrator's
   (`28-corpus-contract.md` §6/§7); this audit supplies the numbers for either
   choice, not a decision.
2. **Placement residual (3 files, reading B)**: the three `verification/`
   entries above. V11 records the reason no repair was made (r9-pre digest pin
   + open contract question). If the lane rules that "opens with" is literal,
   these are the only three files left to move, and the move must be
   coordinated with a baseline refresh.
3. **Duplicate in-body trio restatements (2 files)**: `amazigh-berber.md`
   (header 5–7 and in-body 19–21) and `burma.md` (header 5–7 plus the legacy
   fused restatement at line 15). Both are byte-consistent copies; the round-8
   open item (remove or keep the in-body copy) still has no lane ruling
   (`v01-civ-1-19.md` cross-shard observations 2–3). No opener failure.
4. **`mali-songhai.md` was fixed twice** (split, then relocation into the
   opening block). The fragment's final revision documents both; earlier
   versions of the fragment and the auditor's mid-round readings described the
   intermediate state. Final tree = opening-block trio, no in-body copy.
5. **Methodological note (no defect)**: V07's "lines" column uses the
   `split("\n")` convention (+1 vs `wc -l`); every digest still matched.

## 6. v09 status and audit limits

- **`reports/round-9/metadata/v09-myth-symbol.md` never appeared.** Polling ran
  20:48:45Z–21:08:32Z (checks every 60s, then every 20s in the final window;
  fragment-directory listings at every check). At close the directory holds
  `audit.md` plus `v01`–`v08`, `v10`, `v11` — 11 files, no `v09-*`. The missing
  fragment is recorded here as absent; nothing was fabricated to fill it.
- The shard's surface is nevertheless **verified directly by the auditor**:
  `git status --porcelain corpus/knowledge/myth-symbol/` is empty (no edit to
  attribute), and all 16 files carry `- source:` / `verified-at:` / `recheck:`
  exactly once in the opening block — i.e. the partition passes even the
  strictest reading A with zero misses. Per-file sha256 (first 16) at 21:08Z:
  animal-symbolism `8f1fce2d21a1a174`, celestial-symbolism-calendars
  `2ef711ca56d5e167`, color-symbolism `b6830fe792b20740`, comparative-frameworks
  `532e8e0453602cda`, cosmology-cosmography `165f292b95852459`,
  creation-myths-taxonomy `a3736c4c293b66ad`, flood-traditions
  `d02322cd2c2684ad`, hero-journey-variants `5ae1e5b9019c9f9c`,
  motif-index-usage `e81f3cdc727672ac`, myth-folktale-genres
  `936f0f4f8f3dd1bf`, myth-ritual-theories `78fb98725a3376f4`,
  number-symbolism `7149494ed994e155`, pantheon-archetypes `59f01b86944cdede`,
  ritual-liminality `b57bf9ac3f8c8bea`, symbolism-synthesis-method
  `8aef07cae6d6c484`, trickster `c1a2c066deeb139f`; gate `files=16 marks=9
  mark-lines=9 findings=0 blocked=0`, exit 0. A late v09 fragment can only
  confirm or qualify this zero-edit pass.
- Limits: fragment claims were checked at the scope they state (structure,
  digests, gate receipts, in-repo citations); this audit did **not** re-run the
  shards' network sweeps, with the single exception of V10's OpenAlex record,
  which was re-fetched and matched. Every count above is a point-in-time value
  of a worktree in flight during a 64-worker wave; the HEAD-side numbers are the
  stable reference. The auditor made no corpus edit, no commit, and no ruling on
  the fleet-vs-lane contract question.
