# R10-C25 — auditor: civilizations + synthesis unchanged-count verification (179+new reconciles)

- seat: R10-C25 auditor. lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  assignment: *civilizations+synthesis unchanged-count verification (179+new total
  reconciles)*; deliverable `reports/round-10/coverage/audit-unchanged.md`.
- date: 2026-10-17, local clock UTC-03:00. T0 measurement window opens 18:27:23
  (first poll snapshot) and closes 18:28:42 (last T0 command). Mid-round capture
  T0.5 18:34:36; final capture T1 18:39:44 (stability re-check 18:40:46).
- role limits: this seat counts and diffs. Its only write is this file (plus
  scratch under `.scratch/`). It admits no claim, edits no corpus file, and
  absorbs no sibling fragment's evidence as its own.
- revision binding: `git rev-parse HEAD` = `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
  (round-10 availability attempt 3); declared round-10 `baseline_revision` =
  `9dc18ec1339bffd6f81e74f1a5742464ef578749` ("round-9: admit F/O/D", 2026-10-17
  18:17:00 -0300). `git diff --name-only 9dc18ec… -- corpus/knowledge` is empty
  at T0 (command in §2.1) — every count below grades bytes identical under both
  revisions.

## 1. Verdict

1. **civilizations and synthesis are unchanged from the round-9 close.** Live
   counts T0: civilizations **94**, synthesis **24** — identical to the declared
   baseline tree and to round-9's close-of-round receipts
   (`reports/round-9/metadata/audit.md:119-121`: civilizations 94 files
   marks=412 mark-lines=410; synthesis 24/90/86, all `findings=0 blocked=0`).
2. **Content, not just filenames, is unchanged.** The provenance gate re-run at
   T0 returns byte-identical marker totals to round-9's close values (civ
   412/410, synth 90/86, both exit 0), and the whole-corpus inventory matches
   round-9's close line exactly (files=179 raw_lines=610 raw_occurrences=616
   markers=584, bare 555 / detailed 29). Any added, removed, or edited entry in
   either partition would move at least one of these numbers; none moved.
3. **Per-entry content identity, not just aggregate counts.** The round-9
   metadata fragments (`reports/round-9/metadata/v01…v07`) recorded a sha256 for
   every file they audited as their post-state. Re-deriving all 118 live hashes
   and comparing: **118/118 match, 0 mismatches** (civ 94/94, synth 24/24; method
   and per-fragment counts in §2.5). Every entry in both partitions is the same
   byte-for-byte file round-9 closed with.
4. **Index-vs-files is exact for both partitions.** `corpus/README.md` section
   header claim, index rows, and on-disk files agree 24=24=24 and 94=94=94 with
   zero missing rows, zero orphan rows, zero duplicate rows (script in §2.3).
   (One sibling edit landed after T0: the `africa-primary-sources.md` row's prose
   was rewritten — same row name, same file; recorded in §4.)
5. **Reconciliation at T0:** 179 + 0 = 179. Total = 94+16+16+16+24+13 = 179,
   matching the C-claim `before` count (179 knowledge entries) and round-9's
   scribe re-count (`reports/round-9/report-draft.md:168`). The `+new` term is
   the set of round-10 untracked entries in the thin partitions; at T0
   `git status --porcelain -- corpus/knowledge` is empty (new=0). At T1
   (18:39:44) **new=10, total=189 = 179+10**, with civilizations/synthesis
   still 94/24 and every digest unchanged (§4.2).

## 2. Commands and outputs (T0, 2026-10-17)

### 2.1 Baseline identity

```
$ git rev-parse HEAD
e3a1ec9435787328ac9f828f96cb6390e4916b8f
$ git show -s --format='%h %ci %s' 9dc18ec1339bffd6f81e74f1a5742464ef578749
9dc18ec 2026-10-17 18:17:00 -0300 round-9: admit F/O/D — escalated residuals, 7/7 gate baselines, D3 acceptance
$ git diff --name-only 9dc18ec1339bffd6f81e74f1a5742464ef578749 -- corpus/knowledge
(empty)
$ git status --porcelain | head -40
?? .scratch/
```

Baseline tree counts at `9dc18ec…` (`git ls-tree -r --name-only … | grep -c '\.md$'`):
civilizations 94, synthesis 24, linguistics 16, myth-symbol 16, culture-material
16, verification 13; total 179. Live counts identical (§2.2).

### 2.2 Independent counts

```
$ for p in civilizations synthesis linguistics myth-symbol culture-material verification; do
    echo "$p: $(find corpus/knowledge/$p -maxdepth 1 -name '*.md' -type f | wc -l)"; done
civilizations: 94
synthesis: 24
linguistics: 16
myth-symbol: 16
culture-material: 16
verification: 13
$ find corpus/knowledge -name '*.md' -type f | wc -l
179
$ find corpus/knowledge -type f ! -name '*.md' | sort      # non-md files
(empty)
$ find corpus/knowledge -mindepth 2 -type d | sort          # nested dirs
(empty)
```

```
$ python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations   # exit 0
INFO scan: files=94 marks=412 mark-lines=410 findings=0 blocked=0
$ python3 tools/gates/provenance-audit.py corpus/knowledge/synthesis       # exit 0
INFO scan: files=24 marks=90 mark-lines=86 findings=0 blocked=0
```

```
$ python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge   # exit 0
totals: files=179 files_with_any_mark=128 files_with_marker=118 lines=33021
        raw_lines=610 raw_occurrences=616 ci_occurrences=618
        case_variant_occurrences=2 marker_occurrences=584
        bare_marker_occurrences=555 detailed_marker_occurrences=29
        marker_lines=581 unparenthesized_occurrences=34
per-partition (from the same JSON's file list): civilizations 94, culture-material 16,
        linguistics 16, myth-symbol 16, synthesis 24, verification 13
```

Cross-round anchors (round-9 close, cited by path+line):
`reports/round-9/metadata/audit.md:119-121` per-partition provenance civ
94/412/410, synth 24/90/86, all exit 0; `:123-124` whole corpus
`files=179 marks=618 mark-lines=612 findings=0`; `:128-130` inventory
`files=179 raw_lines=610 raw_occurrences=616 markers=584 (bare 555, detailed
29)`. T0 reproduces every value this seat's scope covers: the civ/synth
provenance lines exactly, and the inventory totals exactly. (The gate's `marks`
counter and the inventory's `markers` counter are different metrics — 618 is
the per-partition provenance sum, 584 the inventory's marker occurrences — so
they are not expected to equal each other. This seat ran the provenance gate on
the two unchanged partitions only; the four growing partitions are the sibling
auditors' and metadata seats' surface.)

### 2.3 Index-vs-files diff (corpus/README.md)

```
$ python3 - <<'EOF'
import re, pathlib
readme = pathlib.Path('corpus/README.md').read_text()
for sec in re.split(r'^## ', readme, flags=re.M)[1:]:
    m = re.match(r'([a-z-]+)/ \((\d+)\)', sec)
    if not m or m.group(1) not in ('civilizations','synthesis'): continue
    name, claimed = m.group(1), int(m.group(2))
    rows = re.findall(r'^- `([^`]+)`', sec, flags=re.M)
    files = sorted(p.name for p in pathlib.Path(f'corpus/knowledge/{name}').glob('*.md'))
    print(f'{name}: claimed={claimed} rows={len(rows)} files={len(files)}',
          'missing:', sorted(set(files)-set(rows)) or 'NONE',
          'extra:', sorted(set(rows)-set(files)) or 'NONE')
EOF
synthesis: claimed=24 rows=24 files=24 missing: NONE extra: NONE
civilizations: claimed=94 rows=94 files=94 missing: NONE extra: NONE
```

Section headers verified at `corpus/README.md:73` (`## synthesis/ (24)`) and
`:116` (`## civilizations/ (94)`); zero duplicate index rows in either section.

### 2.4 File-list and content digests (change detector for §4)

```
$ find corpus/knowledge/civilizations -maxdepth 1 -name '*.md' -printf '%f\n' | sort | sha256sum
1912eaf776e66bb95d9f3227801c20b40bc6e7807497918ffcbaa1c19522787d  -
$ find corpus/knowledge/synthesis -maxdepth 1 -name '*.md' -printf '%f\n' | sort | sha256sum
474609383a328d8f21a50fe85129a69d2651f4f6ffa6483e66890de306e8f2f7  -
$ find corpus/knowledge -name '*.md' -type f -printf '%P\n' | sort | sha256sum
acca9c24fae107836a803a20c89c569840c3371021ff05d048c657d300289c02  -
$ find corpus/knowledge/civilizations -maxdepth 1 -name '*.md' -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum
a4d4e4ac78393082cc8008d26d51de42c535f3827bb413931621f8a5b770acb0  -
$ find corpus/knowledge/synthesis -maxdepth 1 -name '*.md' -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum
db1808a8adf3b6a43a08ce34e6ad7998eae1e11c44491ea7742bd0b0934037aa  -
```

Per-entry sha256 for every file in both partitions is in the T0 inventory JSON
(`.scratch/audit-c25-inventory.json`, regenerable with the §2.2 inventory
command); combined digests built from those rows:
civilizations `d762d9a1281675577cad3ad9156d07b604a88b5ea8ee370917c0fbcd7b41b359`,
synthesis `1993e8e6c752acbd84786a6ef468895cdcc7d2af6348f2b3b25b24aad435f9a7`.

### 2.5 Per-entry digest comparison against round-9 post-state (118/118)

Method: each round-9 metadata fragment records a sha256 for every file it audited
as the post-state of that audit; this seat re-derived every live hash
(`sha256sum` for all 118 files, cross-checked against the §2.2 inventory JSON's
per-file `sha256` field) and compared at 16-hex prefix. Fragment formats differ
and were parsed per fragment: v01 last table column (`sha256 now`); v02/v03
single table column; v04 two-column list (second column = post-edit); v05 prose
list with extension-less names; v06/v07 table column. Results:

| fragment | range | recorded | match | mismatch |
|---|---|---|---|---|
| v01-civ-1-19 | civilizations 1–19 | 19 | 19 | 0 |
| v02-civ-20-38 | civilizations 20–38 | 19 | 19 | 0 |
| v03-civ-39-57 | civilizations 39–57 | 19 | 19 | 0 |
| v04-civ-58-76 | civilizations 58–76 | 19 | 19 | 0 |
| v05-civ-77-94 | civilizations 77–94 | 18 | 18 | 0 |
| v06-synth-1-12 | synthesis 1–12 | 12 | 12 | 0 |
| v07-synth-13-24 | synthesis 13–24 | 12 | 12 | 0 |
| **total** | **civilizations 94 + synthesis 24** | **118** | **118** | **0** |

Parser caveats (documented, not silent): v05's prose section also contains the
literal HEAD revision string `a7bb205d3aecdaa2` next to the word "time" — it was
excluded as a false positive (not a file digest); with that exclusion v05 covers
exactly its 18 files. v01's pre-edit column was ignored by taking the last
column. The comparison is prefix-16 only, as the fragments recorded 16 hex.

## 3. What "unchanged" rules out

- an entry added to or removed from either partition (counts and digests move);
- an entry edited in place (content digests and provenance marker totals move);
- an index row added/dropped/renamed without a file (row-vs-file diff moves);
- a nested subdirectory or non-`.md` file smuggled into either partition
  (both sweeps empty).

## 4. T1 post-landing re-check (179+new reconciles)

### 4.1 Mid-round capture (T0.5, 2026-10-17 18:34:36 -0300)

Captured by a dry-run of the T1 evidence script (`.scratch/audit-c25-t1.sh`);
values transcribed here: **new=6, total=185 = 179+6**, i.e. the reconciliation
identity holds while entries are landing.

- per-partition: civilizations **94** (unchanged), synthesis **24** (unchanged),
  linguistics 17, myth-symbol 18, culture-material 17, verification 15
  (94+24+17+18+17+15 = 185).
- new files: `culture-material/transport-mobility-lexicon.md`,
  `linguistics/numerals-and-measures.md`, `myth-symbol/direction-symbolism.md`,
  `myth-symbol/plant-symbolism.md`,
  `verification/header-conformance-readings.md`,
  `verification/verification-independence-anti-circularity.md` — all six in the
  thin partitions, none in civilizations/synthesis.
- civ/synth digests at T0.5 byte-identical to §2.4 T0 values (all four
  digests match); provenance gates still `94/412/410/0` and `24/90/86/0`,
  exit 0; README index still exact 24=24=24 / 94=94=94.

### 4.2 Final capture (T1)

**T1, 2026-10-17 18:39:44 -0300 (re-checked 18:40:46, no change): 189 = 179 + 10.
The identity holds; civilizations and synthesis are frozen at 94 / 24.**

- per-partition: civilizations **94**, synthesis **24**, linguistics 19,
  myth-symbol 19, culture-material 18, verification 15;
  arithmetic 94+24+19+19+18+15 = 189 = 179+10.
- the 10 new entries (all untracked, all in the thin partitions; **zero** in
  civilizations/synthesis):
  - linguistics 3: `language-shift-obsolescence-revival.md`,
    `numerals-and-measures.md`, `sound-symbolism.md`
  - myth-symbol 3: `direction-symbolism.md`, `divination-omen-systems.md`,
    `plant-symbolism.md`
  - culture-material 2: `transport-mobility-lexicon.md`,
    `vessel-container-lexicon.md`
  - verification 2: `header-conformance-readings.md`,
    `verification-independence-anti-circularity.md`
  (each partition meets the C-claim's per-partition minimum of 2.)
- civ/synth digests at T1 reproduce all four T0 values exactly (§2.4);
  provenance gates still `94/412/410/0` and `24/90/86/0`, exit 0; README
  index rows for both partitions still exact 24=24=24 / 94=94=94;
  `git diff --stat 9dc18ec… -- corpus/knowledge` still empty (the new entries
  are untracked, not staged).
- stability: watcher log shows `new=10` from 18:37:44 through 18:39:44 (5
  consecutive 30 s samples), T1 at 18:39:44, independent re-check at 18:40:46
  identical; `new` count never exceeded 10 through 18:40:46.
- README diff vs baseline at T1: 30 insertions / 11 deletions (sibling
  C21/C22 index work in flight on thin-partition rows; both civ/syn sections
  verified row-exact at T1 — the row-name sets are unchanged).
- acceptance note: the claim's counting command
  (`python3 reports/round-10/run-validation.py`) re-derives the total at
  acceptance time; if further entries land after T1, the same identity
  (total = 179 + new) is re-checked by §2.2 + §2.4 commands — this seat's
  snapshot binds only the timestamps above.



## 5. Residuals

1. The `+new` term belongs to sibling seats (R10-C01..C22 author, review, and
   index the entries). This seat verifies the arithmetic and the unchanged
   partitions; it does not audit new-entry quality or index-row prose.
2. Round-10 entries untracked at T1 are counted from `git status` (`??` rows);
   if an author stages/commits inside the round (not this seat — this seat
   never commits), the count command must switch to
   `git diff --name-only --diff-filter=A 9dc18ec… -- corpus/knowledge`.
3. Snapshot log `.scratch/audit-c25-snapshots.log` mixes rows from two pollers
   (60 s cadence killed 18:28, 30 s cadence stopped after T1); rows are
   consistent and harmless.
4. The README row for `africa-primary-sources.md` was re-worded by a sibling
   seat during the round (row name and file unchanged; §1.4, §4.2). Index-row
   prose is the C21/C22 seats' surface; this audit verified row-name sets and
   counts only.
