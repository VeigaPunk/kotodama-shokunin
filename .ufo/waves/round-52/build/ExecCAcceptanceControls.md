# ExecCAcceptanceControls — round 52, claim C acceptance controls

Seat: `KotodamaR52.ExecCAcceptanceControls` (executor). Assigned item: build the
acceptance controls for claim C (coverage, speech-surrogates entry, knowledge files
227 → 228) and record the argv, the printed lines and the exit code of every control.

Sandbox only. Nothing in the lane repo was edited except this report file. No
subagent was spawned. No tool was installed (nothing needed installing).

## 1. Sandbox

- Path: `/fast/scratch/hyaku/kotodama-r52/ExecCAcceptanceControls`
- Command: `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r52/ExecCAcceptanceControls`
- Checkout: `git -C <sandbox> checkout -q d9f73c80744bb5e483f6d9d39069fe064dc5dffe`
  (the round-52 declaration commit; `git log --oneline -1` → `d9f73c8 round-52: declare
  claims D (depth, S094 citations 5 -> 0) and C (coverage, speech-surrogates entry 227 -> 228) with dry-run receipt`).
- The lane tip is `dea5ece` (claim D landed). D adds no knowledge file, so the
  knowledge count at the lane tip is the same 227 measured at `d9f73c8`
  (`find corpus/knowledge -name '*.md' | wc -l` → 227 in the lane worktree and in the sandbox).
- Control scripts (sandbox, outside the clone): `/fast/scratch/hyaku/kotodama-r52/run_acceptance.py`,
  `build_controls.py`, `build_controls2.py`; transcripts `controls-transcript.txt`,
  `controls-transcript-2.txt`. The sandbox was reset to base after every control.

## 2. The acceptance argv (taken verbatim from the separability manifest)

`reports/round-52/separability-manifest.json`, claim `C`, key `acceptance`:

```json
["sh", "-c", "n=$(find corpus/knowledge -name '*.md' | wc -l); echo knowledge_files=$n; test \"$n\" -eq 228 && python3 -B reports/round-28/readme/sweep.py | grep -q '\"total\": 228' && python3 -c \"$0\"", "import re,sys;p='corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md';e=open(p).read();ids=set(re.findall(r'\\bS\\d{3}\\b',e));rows={l.split('|')[1].strip():l.split('|')[11] for l in open('corpus/SOURCES.md') if re.match(r'^\\| S\\d{3} ',l)};bad=[i for i in sorted(ids) if int(i[1:])<134 or i not in rows or p not in rows[i]];print('C_SID_BAD',len(bad),bad,'cited',len(ids));sys.exit(1 if bad or not ids else 0)"]
```

It was run with `subprocess.run(argv, cwd=<sandbox root>, shell=False)`, so the list is
passed through untouched; `sh -c` receives the python program as `$0`. The command
must be run from the repo root (every path in it is repo-root relative).

Three legs, chained with `&&`:
1. `find corpus/knowledge -name '*.md' | wc -l` must be 228;
2. `python3 -B reports/round-28/readme/sweep.py | grep -q '"total": 228'`;
3. the python program: every `S###` mentioned in the entry must be ≥ S134, present in
   `corpus/SOURCES.md`, and have the entry path in its used-by cell; at least one S-id
   must be cited.

## 3. Controls, printed lines and exit codes

Every line below is the literal stdout of the acceptance argv, followed by its exit
code (stderr was empty in every run). `sweep.py` was also run directly for each
control to show what the README must carry; its exit code is reported in §4.

| control | state built in the sandbox | acceptance stdout | acceptance exit |
|---|---|---|---|
| base | nothing (no C land) | `knowledge_files=227` | 1 |
| (a) | entry cites S134; S134 row's used-by names the entry; README row + `## linguistics/ (27)` + totals 228 + footer 228 | `knowledge_files=228` / `C_SID_BAD 0 [] cited 1` | **0** |
| (a2) | as (a) but `corpus/README.md` untouched | `knowledge_files=228` / `C_SID_BAD 0 [] cited 1` | **0** (see §5) |
| (a3) | as (a) but README index row only | `knowledge_files=228` / `C_SID_BAD 0 [] cited 1` | 0 |
| (a4) | as (a) but README index row + section count | `knowledge_files=228` / `C_SID_BAD 0 [] cited 1` | 0 |
| (a5) | as (a) but README index row + section count + totals line | `knowledge_files=228` / `C_SID_BAD 0 [] cited 1` | 0 |
| (a6) | as (a) but README row topic paraphrased (not byte-equal) | `knowledge_files=228` / `C_SID_BAD 0 [] cited 1` | 0 (sweep.py exits 1, `topic_mismatch 1`) |
| (b) | entry cites S133 | `knowledge_files=228` / `C_SID_BAD 1 ['S133'] cited 1` | 1 |
| (c) | entry cites S134, S134 used-by is `—` | `knowledge_files=228` / `C_SID_BAD 1 ['S134'] cited 1` | 1 |
| (d) | as (a) plus one stray `.md` under `corpus/knowledge` (229 files) | `knowledge_files=229` | 1 |
| (e) | entry carries no S-id | `knowledge_files=228` / `C_SID_BAD 0 [] cited 0` | 1 |
| (f) | S134 used-by written `linguistics/speech-surrogates-whistled-drummed.md` (no `corpus/knowledge/` prefix) | `knowledge_files=228` / `C_SID_BAD 1 ['S134'] cited 1` | 1 |
| (g) | entry cites S134 but `corpus/SOURCES.md` has no S134 row | `knowledge_files=228` / `C_SID_BAD 1 ['S134'] cited 1` | 1 |

Note on (d): the chain short-circuits at leg 1, so the `C_SID_BAD` line is never
printed there; the count line alone is the evidence.

The synthetic entry used for the controls (control artifact, sandbox only):

```
# Speech surrogates — control stub

- topic: speech surrogates — whistled speech, drummed speech and other instrument-borne speech (horns, reed pipes, jaw harps, xylophones, gongs) — as a conlang and worldbuilding method, with the boundary against signal codes
- sources:
  - S134 (2026)
```

## 4. Exactly what README edits `sweep.py` needs

`sweep.py` (read at `reports/round-28/readme/sweep.py`) checks the index rows, the
section headers, the totals line and the counts footer. For the C landing it needs
four edits in `corpus/README.md`, all of them visible in the direct runs:

1. **Index row** — a row `- \`speech-surrogates-whistled-drummed.md\` — <topic>` in
   the `## linguistics/` section, in filename order between `sound-symbolism.md` and
   `syntax-typology.md`, whose topic text is **byte-equal** to the entry's own
   `- topic:` head-block text (continuation lines are space-joined; `sweep.py:topic_of`).
   Missing → `missing_from_index 1 ['linguistics/speech-surrogates-whistled-drummed.md']`;
   paraphrased → `topic_mismatch 1 [...]` (control a6).
2. **Section header** — `## linguistics/ (26)` → `## linguistics/ (27)`
   (`corpus/README.md:231`). Otherwise `header_drift {'linguistics': {'declared': 26, 'files': 27}}`.
3. **Totals line** — `Total knowledge entries: 227.` → `Total knowledge entries: 228.`
   (`corpus/README.md:602`). Otherwise `totals_line 227 totals_ok False`.
4. **Counts footer** — `(total 227 files; directory totals 26/26/28/29/24/94).` →
   `(total 228 files; directory totals 27/26/28/29/24/94).`
   (`corpus/README.md:606`, inside the `Counts checked 2026-10-22 from the repo root:` block).
   Otherwise `footer_findings [{"class": "FOOTER_TOTAL", "declared": 227, "live": 228, ...},
   {"class": "FOOTER_DIR_TOTALS", "declared": [26, 26, 28, 29, 24, 94], "live": [27, 26, 28, 29, 24, 94], ...}]`.
   The directory order is `linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`
   (`sweep.py:PARTS`), so the linguistics count is the first number.

With all four edits the direct run is clean:
`rows 228 files 228 / missing_from_index 0 [] / topic_mismatch 0 [] / orphan_rows 0 [] /
header_drift {} / totals_line 228 totals_ok True / footer_findings [] footer_ok True`,
sweep.py exit 0.

## 5. Finding: the acceptance argv does not test the README

Controls (a2)–(a6) all pass the acceptance with exit 0 while `sweep.py` itself exits 1.
Two independent reasons, both measured:

- The pipeline `python3 -B reports/round-28/readme/sweep.py | grep -q '"total": 228'`
  takes **grep's** exit status, not sweep.py's, and `sh` has no `pipefail`. A
  failing sweep is therefore invisible to the acceptance.
- The pattern `"total": 228` also matches sweep.py's **live** line
  `footer_live {"total": 228, "dir_totals": [27, 26, 28, 29, 24, 94], ...}`
  (rendered at `sweep.py:render`), which reports the live file count, not the README's
  own footer text. Measured directly on a stale README:
  `sweep exit: 1`, `GREP-MATCH line 9: footer_live {"total": 228, ...}`,
  `grep -q exit: 0`.

Consequence for the landing: the acceptance passes on a README that is stale in all
four ways from §4 (control a2). The README edits in §4 are still required — by
`sweep.py`, the corpus's own index instrument, and by the `README.md` land in the C
claim — but the acceptance argv alone will not catch their absence. Advice to the L1
(tightening is the integrator's call, not a change made here): make the acceptance leg
require sweep.py's own verdict, e.g. run
`python3 -B reports/round-28/readme/sweep.py --json` and check `totals_ok`, `footer_ok`
and `missing_from_index == []`, or gate on sweep.py's exit status before the grep.

## 6. Other things the controls pin down for the L1's landing

- **used-by form.** The python leg tests `p not in rows[i]`, with `p` the literal
  `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. The S134
  used-by cell must therefore contain that exact repo-relative path; writing
  `linguistics/speech-surrogates-whistled-drummed.md` fails (control f,
  `C_SID_BAD 1 ['S134']`).
- **used-by column index.** `rows` is built as `l.split('|')[11]` over lines matching
  `^\| S\d{3} `, i.e. column 11 of the 11-column table (header at `corpus/SOURCES.md:28`).
  Every current row splits into exactly 13 fields (11 content cells) — measured over
  all 133 rows: `split widths {13: 133}`, no duplicate ids, ids S001–S133, none ≥ S134
  yet. A `|` inside any cell would shift that index, so no cell of the new S134 row
  may contain a pipe character.
- **S-id scan.** `\bS\d{3}\b` is applied to the **whole** entry text, so any S-id
  mentioned anywhere in the entry (body prose included) is checked. The entry may cite
  only ids ≥ S134, and must cite at least one (control e: `C_SID_BAD 0 [] cited 0` → exit 1).
- **Count leg.** `find corpus/knowledge -name '*.md' | wc -l` counts **every** `.md`
  under `corpus/knowledge`, recursively, including `corpus/knowledge/verification/`.
  One stray file anywhere under that tree breaks the acceptance (control d).
- **sweep.py counts differently.** `sweep.py` counts the six partition directories
  non-recursively (26/26/28/29/24/94 = 227 today, 27/26/28/29/24/94 = 228 after the
  landing). Both counts agree today; keep them in step.

## 7. Evidence, references

- `reports/round-52/separability-manifest.json` — claim `C` acceptance argv, quoted in §2.
- `reports/round-52/claims.json` — claim C counting command
  `find corpus/knowledge -name '*.md' | wc -l`, before 227, after required 228.
- `reports/round-28/readme/sweep.py:50` (`PARTS`), `:60` (`ROW_RE`), `:61` (`TOPIC_RE`),
  `:62` (`TOTALS_RE`), `:66` (`FOOTER_RE`), `:74` (`topic_of`), `:215` (`render`) — the checks
  listed in §4 and §5.
- `corpus/README.md:231` (`## linguistics/ (26)`), `:602` (`Total knowledge entries: 227.`),
  `:604-606` (counts footer block, `(total 227 files; directory totals 26/26/28/29/24/94).`).
- `corpus/SOURCES.md:28` (11-column header `id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`),
  `:162` (last row, S133).
- Lane count at the tip: `find corpus/knowledge -name '*.md' | wc -l` → 227.

## 8. Unrun checks

- The lane's own `reports/round-52/dry-run.py run` was not executed (the wave's gate
  belongs to the parent session; only the C acceptance argv was exercised here).
- No claim D acceptance was run, and the separability and agreement commands were not
  run.
- `python3 -B reports/round-28/readme/sweep.py --selftest` was not run.
- The real C entry does not exist yet; all controls used a synthetic stub entry and a
  synthetic S134 row in the sandbox. The byte-exact `- topic:` string of the real entry
  must be copied into the README row — the sweep compares them literally.

## 9. Lane safety

Only this report was written in the lane
(`.ufo/waves/round-52/build/ExecCAcceptanceControls.md`). All control files, the
synthetic entry, the synthetic S134 row and the README edits existed only inside
`/fast/scratch/hyaku/kotodama-r52/ExecCAcceptanceControls` and were removed by
`git checkout -- .` + `git clean -fdq` in the sandbox after the last control
(sandbox back to 227 knowledge files). No `jj` command was run anywhere; no git
command that writes was run in the lane repo.
