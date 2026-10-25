# ExecScratchMirror — scratch-mirror validation rehearsal (claim C · SCRATCHMIRROR)

Round 74, wave 1 · seat ExecScratchMirror · 2026-10-25 · lane base `f7104cbce186bc2e1522abf0cfd619cc834628bb`.
Scratch only: no lane `corpus/` byte, no git/jj state, no `claims.json` and no fleet path was written.

## Result

`sources-census.sh validate --file` on the mirrored registry returns **exit 0, zero E-codes**: the mirror carries the four normalized rows S881..S884, both entry files at their repo-relative paths, and the in-place S877 used-by change. Receipt (draft): `.ufo/waves/round-74/assimilation/validate-receipt-draft.txt`. Notes: `.ufo/waves/round-74/assimilation/validate-notes.md`.

The claim's sequencing clause ("in a commit strictly before the registry-append commit") is **not exercised** — this leaf cannot commit; the draft receipt's commit position is a later wave's job.

## What was built

`A` = `.ufo/waves/round-74/assimilation`; mirror root `A/validate/`.

| artifact | detail |
|---|---|
| `A/validate/corpus/` | copy of lane `corpus/` (`du -sh corpus` = 13M; SOURCES.md 957,543 B, QUALITY.md 31,017 B, README.md 169,575 B, knowledge/ 7.8M, lessons/ 3.7M) |
| `A/validate/SKILL.md` | copied from lane root **only** so pre-existing `used-by: SKILL.md` cells resolve; census `E11` resolves used-by against `dirname(corpus)` |
| `A/validate/corpus/knowledge/culture-material/worldbuilding-setting-practice.md` | byte copy of the draft (`sha256 658a8fa4…9986b00b`) |
| `A/validate/corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` | byte copy of the draft (`sha256 bb5504e2…d80d8673e`) |
| mirror `corpus/SOURCES.md` | 804 → **808** rows; `sha256 81fcebe172a5d3758844bf54847ffbb76158c86ef42e6da0722195c8b9f2f326` |

Registry diff against base, row-level: `801c801` (S877 row changed in place) and `804a805,808` (S881..S884 added). Nothing else in the registry differs.

## Normalization (staged → lane)

Map used: staged S883→S881 (litmemo), S884→S882 (tuduku), S899→S883 (chinawriter 2025-06-05), S900→S884 (chinawriter 2022-12-07). Staged S882 was not appended (lane S877 already names that document).

Per row: id renumbered into the lane namespace; `status` = `mined`; `opened` = **2026-10-25**; `recheck` = **`180d`** (cadence only); the stripped recheck prose is preserved verbatim in the notes §3; `used-by` = exactly the citing entries — base entry for S881/S882, amendment for S883/S884, both entries for S877 in place.

Pitfalls the staged rows carried and how each was fixed:

- **escaped `\|` inside the recheck cell** (all four rows) — `gawk -F'|'` does not honour `\|`; removed by replacing the whole cell with `180d`. Verified after the fact: `grep -cF '\|'` over the appended block = 0, and each row splits to **NF=13**.
- **prose recheck** (`-> 4 (ran 2026-10-23)`) — moved to the notes file.
- **staged ids colliding with lane ids** (staged S883/S884) — renumbered.
- **anchor cell is a locator, not a verbatim span** (staged S899/S900) — kept as staged but flagged `rehearsal-only` in the notes §4; the R68/71 refusal (register S816/S817: quoted spans absent from the live pages) is not repaired by this seat and must not be read as repaired.

In-place S877 edit (mirror only): used-by `corpus/knowledge/linguistics/conlang-scholarship.md` → `corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`.

## Retained evidence

1. `sources-census.sh --help` — modes `census` (default) | `validate` | `overdue` | `shared` | `selftest`; exit 0 clean *or warnings*, 1 E/overdue, 2 usage/missing registry, 3 selftest failure; 11 columns ⇒ NF=13; `--file` sets lane dir to the parent of `corpus/`.
2. Clean run (verbatim in the receipt):
   `sources-census.sh validate --file .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md` → `EXIT=0`; stdout ends `file ok …/assimilation/validate/corpus/SOURCES.md`; `E`-codes **0**; `W01` ×3 (S881, S882, S884 — tier-C mined, expected under the census's warning set and status-neutral); `W04` ×28, all inherited from base (S127…S830) and none touching S877–S884; stderr empty.
3. Liveness control (same directory, so used-by resolution is identical; mutant file deleted afterwards, absence verified):
   - staged row as-is → `E01 S883 fields=12`, `E03 S883 duplicate id`, `E11 S883 missing used-by grep -c '自然環境'`…`-> 4 (ran 2026-10-23)` (the escaped pipe smeared the used-by cell);
   - prose recheck → `E04 … duplicate url …/2025/0605/c404024-40494534.html within scope …`, `E09 S883 recheck=180d — re-open the URL and re-locate the span`;
   - bogus used-by → `E11 S881 missing used-by corpus/knowledge/missing-control.md`;
   - valid row after `## Paths` → `E12 S890 row outside Registry section`;
   - mutant exit **1** vs mirror exit **0**.
4. Row-shape proof: `awk -F'|' '/^\| S88[1-4] \|/{print $2" NF="NF}'` → S881…S884 all `NF=13`. The four-row block was derived mechanically from the staged lines with `awk -F'|'` (not retyped), written to `/tmp/ExecScratchMirror/rows.md`, inserted before `## Paths`, then `cmp`-checked byte-identical against the derived block in the mirror (`BYTE-IDENTICAL`).
5. Base-row baseline: `git show f7104cb…:corpus/SOURCES.md` → 804 registry rows; working-tree `corpus/SOURCES.md` → 804 (matches `reports/round-74/telemetry/census-start.txt`), and the working-tree file hashes to the base blob (`93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774` both) — the rehearsal wrote no lane registry byte.

## Findings

- No E03/E04/E11/E12 (nor any other E-code) on the mirror; the controls show those checks are live at this path, so the clean exit is a real negative rather than a dead check.
- The only defect class the staged rows would have produced is the two known ones — escaped pipe (E01 + E11 smear) and prose recheck (E09) — plus, in this namespace, id duplication (E03/E04) had the rows been appended un-renumbered. All three are removed by the normalization above.
- `used-by` for S877 must gain the base entry path in the real lane too, or the ROWS leg's "used-by exactly the admitted entries whose source: lines cite it" fails; the base draft cites S877 at line 3 and the amendment does not.
- Tier-C `W01` warnings for S881/S882/S884 are expected and status-neutral; they are not a defect, but a claim reader should expect them in the landed `CENSUS` leg output.

## Files changed (all scratch, under the assigned paths)

- `.ufo/waves/round-74/assimilation/validate/**` (mirror tree, new)
- `.ufo/waves/round-74/assimilation/validate-notes.md` (new)
- `.ufo/waves/round-74/assimilation/validate-receipt-draft.txt` (new)
- `.ufo/waves/round-74/w1/ExecScratchMirror.md` (this report)
- `/tmp/ExecScratchMirror/` (row derivation, captured stdout, mutant build; nothing fetched over the network)

## Risks / blockers

- **Sequencing leg unproven**: the receipt must precede the registry-append commit in history; that requires a commit, which this leaf is forbidden to make. The landing seat must commit the mirror (or an equivalent pre-append tree) first and re-run `validate --file` so the receipt's revision is real.
- **Payload not page-derived**: the four rows carry staged quotes. For S883/S884 the staged spans are the ones refused in R68/71, so a clean census proves registry shape only; the `EVIDENCE`/`GATE` legs still depend on the scouts' page-side re-quote and per-row fetch windows.
- `A/validate/SKILL.md` is an extra copy beyond the assignment's list; it is required for a faithful `E11` resolution. If the landing tree cannot carry it, expect spurious `E11` findings on pre-existing rows — that is a mirror-fidelity issue, not a registry defect.
- Tooling: nothing installed; no network fetches; pacman untouched. Lane git used read-only (`git show`).

## Post-wave update

L1 follow-up against the FINAL drafts. Everything below is lane scratch under `.ufo/waves/round-74/`; the lane `corpus/` is still byte-identical to base (`corpus/SOURCES.md` sha256 `93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774`, same as the base blob).

### Files written

1. `.ufo/waves/round-74/drafts/rows-S881-S884.md` — the four exact lines to append. Built mechanically from the scouts' proposed rows (`w1/ScoutLitmemo.md` line 126, `ScoutTuduku.md` line 113, `ScoutChinawriter2025.md` line 111, `ScoutChinawriter2022.md` line 96) with only these changes: `status mined`, `opened 2026-10-25`, `recheck 180d` (the Litmemo scout's ISO-date-plus-prose recheck cell collapsed to the cadence), the Gate quote inserted into the S881 anchor cell, a tier/scope-limit clause appended to every `teaches` cell, and `used-by` set to exactly the citing entry per L1 (S881/S882 → `…worldbuilding-setting-practice.md`; S883/S884 → `…worldbuilding-setting-practice.amend-2026-10-23.md`). The Chinawriter-2025 scout had proposed **both** entry paths; L1's single-path rule wins.
2. `.ufo/waves/round-74/drafts/s877-usedby-change.md` — exactly two lines (old, new). Derived from the base blob's S877 row; verified `cells 1-11,13 byte-identical` and the new line = old line with `, corpus/knowledge/culture-material/worldbuilding-setting-practice.md` appended inside the used-by cell (12 `|` on both lines; the old line is byte-identical to the lane's current S877 row).
3. `A/validate/` rebuilt from scratch: lane `corpus/` + `SKILL.md`, FINAL draft entries at `corpus/knowledge/culture-material/worldbuilding-setting-practice.md` (sha256 `465051db…0e65fc`) and `…amend-2026-10-23.md` (sha256 `0b2e06dc…790d31`), the four rows inserted before `## Paths`, the S877 change applied in place.
4. `A/validate-receipt.txt` — command line with `--file` and `--today 2026-10-25`, the row/entry list, the verbatim output, `exit=0`, and the `E11` probe.
5. `A/validate-notes.md` — a `## Superseded by the final rows` header note (row payload, anchors and recheck cells in §2–§5 describe the earlier staged-derived rehearsal).

### Checks exercised

- Rows block in the mirror is `cmp` byte-identical to `drafts/rows-S881-S884.md`; mirror S877 line is `cmp` byte-identical to the new line in `s877-usedby-change.md`.
- Mirror registry 808 rows (804 + S881..S884); sha256 `c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614`.
- Every row `NF=13`; no escaped `\|` in the block.
- Gate quotes present verbatim in the anchor cells: S881 `自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。`; S882 `勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか`; S883 `整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。`; S884 `把它放在前面大概20章之内慢慢来，我觉得是问题不大的。` (grep -F, one PRESENT per row).
- `sources-census.sh validate --file … --today 2026-10-25` → **exit=0**, **no E-code**, 31 W-codes: `W01` ×3 (S881, S882, S884 — tier-C mined, status-neutral) and `W04` ×28 inherited from base, none on S877–S884.
- `E11` (used-by path existence) probe over S877/S881..S884: all three referenced paths `OK`, no `MISSING`; the census itself reported no E11.
- Wayback: only S883 (`20250610015519`, 200, same digest as live) and S884 (`20221207080111`, 200, body identical) carry a capture in their source cells; S881/S882 are live-only per `w1/ScoutWayback.md` (canonical CDX probes empty with a positive control) and their source cells say so.

### Notes and residual risks

- `kind` for S883 is `docs` (the scout's page-derived value), not the staged row's `paper`; no claim leg fixes `kind`, so the scout value stands.
- The only `used-by` inaccuracy risk left in the row payload is namespace drift if a later edit re-points a cite; the drafts' `source:` lines currently match the rows exactly (base: S877, S881, S882; amendment: S883, S884).
- The round-74 receipt still cannot demonstrate the claim's commit-ordering clause (mirror validate commit strictly before the registry-append commit): no commit was made by this leaf.

