# RerunCCount — claim C counter rerun (falsify seat, round 51 attempt 3)

Date 2026-10-22. Seat: `KotodamaR51a3.RerunCCount` (leaf, read-only on lane). Item attacked: **claim C (coverage)** — `da31d3c`, lands `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, `corpus/README.md`, `corpus/SOURCES.md`. Goal: make the declared counters, checkers, or the manifest acceptance one-liner fail at `da31d3c`, at the tip, or on a C-only tree.

## Method

- Private clone: `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r51a3-falsify/RerunCCount` (no symlink into lane; all mutations sandbox-only; lane writes limited to this report file).
- All commands run from the clone root. The C-only tree was built as `git checkout -q --detach bff83ba65bf9559af4d7567e81703059667a0005 && git checkout da31d3c -- corpus/README.md corpus/SOURCES.md corpus/knowledge/linguistics/sign-languages-manual-modality.md` → `git diff --stat HEAD`: 3 files changed, 297 insertions(+), 5 deletions(-). This reproduces exactly the checker's dynamic leg ("base with the unit's lands overlaid", `tools/check-claim-separability.py:14-16`).
- The manifest acceptance argv was executed **verbatim from `reports/round-51/separability-manifest.json`** (no re-quoting) via `subprocess.run`.
- Landed files verified: `da31d3c` = M `corpus/README.md`, M `corpus/SOURCES.md`, A `corpus/knowledge/linguistics/sign-languages-manual-modality.md`; `35f0d49` (D) touches only `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` — zero overlap; `git merge-base --is-ancestor bff83ba da31d3c` = true.
- No tools installed (none needed). No pacman transactions. No jj commands. No web sources opened (this seat runs counters only; source re-opening is not in scope — listed as unrun below).

## Results

Tip at run time: `9feb69e` (records). States measured: base `bff83ba`, `da31d3c`, tip `9feb69e`, C-only (base + C's three lands).

| Command | base | da31d3c | tip | C-only |
|---|---|---|---|---|
| `find corpus/knowledge -name '*.md' \| wc -l` | 226 | **227** | **227** | **227** |
| `ls corpus/knowledge/linguistics/*.md \| wc -l` | 25 | **26** | **26** | **26** |
| `python3 -B reports/round-28/readme/sweep.py` | exit 0 (footer total 226, self-consistent) | **exit 0**, footer total **227**, `parts` linguistics **26**, `footer_findings []`, dir totals `[26,26,28,29,24,94]` | **exit 0**, footer total **227**, linguistics **26**, `footer_findings []` | **exit 0**, footer total **227**, linguistics **26**, `footer_findings []` |
| `python3 -B tools/check-readme-revisions.py` | exit 0, findings 0, warnings 1 | exit 0, findings 0, warnings 1 | exit 0, findings 0, warnings 1 | exit 0, findings 0, warnings 1 |
| `python3 -B tools/check-readme-heading.py` | exit 0, findings 0 | exit 0, findings 0 | exit 0, findings 0 | exit 0, findings 0 |
| manifest C acceptance (`sh -c 'test "$(find corpus/knowledge -name '*.md' | wc -l)" -eq 227 && python3 -B reports/round-28/readme/sweep.py >/dev/null && python3 -c "$0"' '<py>'`) | **exit 1** (count 226 ≠ 227 — correct control) | **exit 0**, `C_SID_UNRESOLVED 0 []` | **exit 0**, `C_SID_UNRESOLVED 0 []` | **exit 0**, `C_SID_UNRESOLVED 0 []` |
| `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` (declared separability command) | not run (manifest absent at base — added by `1f97472`) | not run (not the declared state) | **exit 0**: `SEPARABILITY: 0 findings`, note `units=3 ordered_pairs=6 acceptance_runs=2` | not run (D's land bytes absent from a C-only worktree; C's own leg already exercised by the acceptance run above) |

Sweep footer at `da31d3c` / tip / C-only: `footer {"date": "2026-10-22", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 227, "dir_totals": [26, 26, 28, 29, 24, 94]}`; `rows 227 files 227`, `missing_from_index 0 []`, `orphan_rows 0 []`, `totals_line 227 totals_ok True`.

## Attack probes beyond the declared set

1. **C-only separability** (the falsifier I most expected to land): all six counters/checkers green on base + C's three lands alone, byte-identical results to tip. C does not depend on D, the declaration commit, or the records commit for any measured acceptance. Attack failed.
2. **`must_not_cite` (C)**: `grep -n -i -e 'round-51' -e 'round_51' -e 'round51' -e 'boundary-count' corpus/knowledge/linguistics/sign-languages-manual-modality.md` → no matches (exit 1) at tip. Attack failed.
3. **S-id span of the entry**: `grep -oE '\bS[0-9]{3}\b'` over the entry → exactly 52 distinct ids, S071–S122, contiguous, none below S071 (counts 1–13 citations each). Attack failed.
4. **Queued leads S123/S124**: cited nowhere in the entry (`grep -n 'S12[34]'` on entry → no matches). SOURCES.md:152-153 are well-formed rows (S123 tier B book row with Wayback note for an HTTP-403 live page; S124 tier A paper row), status cell literally `queued`, used-by cell `—`, opened 2026-10-22, `365d`. No false used-by claim. Attack failed.
5. **Counter discrimination control at base**: acceptance exits 1 at base via the `-eq 227` test (short-circuit before the S-id leg); base sweep exits 0 at total 226 — the sweep alone is not C-discriminating, the chained count test is. Matches the declared chain; noted, not a defect.

## Findings

- **HIGH**: none.
- **MEDIUM**: none.
- **LOW** (informational, pre-existing, not C's defect): `tools/check-readme-revisions.py` prints warning `REVISION-ORPHAN lines=[112, 123] unheaded paragraph inside revisions span (starts 'round-28 C entry landed (linguistics/register-lexicon-…')` at `da31d3c`, tip and C-only. The same warning exists at base `bff83ba` (`lines=[101, 112]`, README sha `3ea247db…`), i.e. it was shifted, not introduced, by C's revision 2.8 block; tool still exits 0. Smallest fix if ever wanted: give that round-28 paragraph a heading in `corpus/README.md`; no action required for this round.

## Verdict

**HOLDS.** Every declared counter and checker for claim C is green at `da31d3c`, at the tip, and on the C-only separability tree, with the base control failing exactly as declared. The acceptance one-liner ran verbatim from the manifest and reports `C_SID_UNRESOLVED 0 []` in all three post-C states; the full declared separability command reports 0 findings at the tip. No falsifier in this seat's scope fired.

## Unrun checks

- Web/source re-opening (QUALITY criterion 6 tiers, quote fidelity): not in this seat's scope; no URL opened, none invented. Covered by `ReopenS071`–`ReopenS101` seats.
- Content-level review of entry sections 1–15: covered by `ReviewC*` seats; this seat measured counters, citations resolution, and separability only.
- Full separability command at `da31d3c` and C-only states: not declared states for that command (manifest/WORKTREE semantics); C's dynamic leg was instead exercised directly and green.
