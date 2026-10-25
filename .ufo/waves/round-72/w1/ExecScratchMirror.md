# ExecScratchMirror — round-72 w1 (kotodama, hyaku run 6)

Seat: `L1Kotodama72.ExecScratchMirror` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Finished 2026-10-25T11:25-03:00. No repo file, no lane `corpus/`, no `/tmp/r72-entries` file was
modified; all writes are under `/tmp/r72-mirror/**` and the two lane paths assigned to this seat
(`.ufo/waves/round-72/assimilation/validate/**`, `.ufo/waves/round-72/w1/ExecScratchMirror.md`).

## Deliverable

A working scratch mirror of the lane corpus with the two normalized registry rows appended, plus a
green registry-append gate and one open failure that the mirror was built to catch.

| item | state |
|---|---|
| `/tmp/r72-mirror/corpus/` (rsync -a from lane `corpus/`) | 471 shared files, sha256 identical to lane |
| `/tmp/r72-mirror/corpus/SOURCES.md` | 799 rows (797 + S874 + S875), sha256 `40b7eca3…f4e745` |
| lane `corpus/SOURCES.md` (control) | untouched: 797 rows, max id S873, sha256 `bf6ad0ea…a3eee8b` |
| admitted entries in mirror | both files byte-identical to `/tmp/r72-entries` (pinned in `validate/entry-pins.txt`) |
| census `validate --file` on mirror | **exit 0** |
| `NF!=13` awk / dup ids / dup URLs / id collision | **0 / none / none-new / empty** |
| `check-cited-lines.py` on the two entries | **exit 1 — 2 findings** (open; see below) |

## Steps and exact evidence

1. **Mirror** — `rsync -a <lane>/corpus/ /tmp/r72-mirror/corpus/`. Fidelity proof
   (`validate/mirror-fidelity.txt`): 471 shared files with identical sha256, no path only-in-lane, no
   path only-in-mirror; the only tree deltas are `corpus/SOURCES.md` and the two entry files.
2. **Rows appended** — the two rows were inserted immediately after the `S873` row (mirror line 829),
   before `## Paths`. `diff` lane vs mirror is a single hunk `@@ -828,0 +829,2 @@`, **2 added lines,
   0 removed** (`validate/sources-md.diff`, exact bytes in `validate/rows-inserted.txt`). Both rows
   `NF=13`: `kind=dataset`, `tier=A`, `status=mined`, `opened=2026-10-25`, `recheck=180d`/`90d` plain,
   no escaped pipes, `used-by` exactly the admitted entry paths (S874 → both entries, S875 → base).
3. **Entries** — `/tmp/r72-entries/*.md` appeared at 11:23–11:25 and were copied to
   `corpus/knowledge/culture-material/` (placeholders were written first, then fully replaced; no
   `PLACEHOLDER` residue). The amendment was revised twice mid-wave (4113 → 3403 → 3397 B); the gate
   was re-run after each revision. Last pins:
   `b2995163…8bfba75` (base, 7991 B) · `9e4f804e…d982024` (amend, 3397 B).
4. **census validate** — `bash scripts/sources-census.sh validate --file /tmp/r72-mirror/corpus/SOURCES.md`
   → **exit 0**, stdout `file<TAB>ok<TAB>/tmp/r72-mirror/corpus/SOURCES.md`, stderr empty
   (`validate/census-validate-mirror.{out,err,exit}`). 0 E-findings; 28 `W04` cross-scope duplicate-URL
   warnings that are **the lane's own pre-existing set** — `validate/baseline-findings.txt` (lane,
   pre-append) and `validate/mirror-findings.txt` are identical, and no finding names S874/S875.
5. **Malformed-row awk + duplicate checks** (`validate/malformed-and-duplicate-checks.txt`,
   `validate/checks.py` → `validate/checks.out`):
   - `awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}'`
     → **0** (all 799 S-rows NF=13; histogram `799 13`);
   - duplicate ids → **none** (799 distinct); no escaped `\|` anywhere;
   - duplicate normalised URLs → 43 pre-existing groups, **none involves S874/S875**; each of the four
     new-row URLs occurs exactly once (`ihchina.cn` 1 live + 2 archive captures, `bunka.go.jp` 1);
   - id collision → `S874`/`S875` ∉ reg-ids (max S873) → `assimilation/collcheck-collisions.txt` is
     0 bytes, with `collcheck-reg-ids.txt` (797 ids) and `collcheck-staged-ids.txt` (26 ids).

## Operational finding the mirror needed

Census resolves `used-by` against the **mirror root** (`resolve_targets`: with `--file`, dir =
`dirname(dirname(file))`). Rows S859/S860 carry `used-by = SKILL.md`, so the mirror root also holds a
copy of the lane's `SKILL.md`; without it the mirror reports two **false E11** findings. With it the
mirror's finding set is byte-identical to the lane's.

## Open failure (blocker for claim C leg `CITEDLINES` at `<lands>`)

`python3 -B tools/check-cited-lines.py <both entries>` → **exit 1**,
`CITED-LINES: 2 finding(s) in 2 file(s)`:

- `heritage-taxonomy-models.md:6` — header `recheck:` line names both `S874` and `S875`;
- `heritage-taxonomy-models.md:21` — the §1 paragraph closes with `(S874, S875)` on one line.

Claim C requires 0 findings. A repair was **verified without touching the admitted entries**: applied
to a probe copy under `/tmp/r72-mirror/probe/`, the same lint prints
`CITED-LINES: 0 finding(s) in 2 file(s)` with exit 0. Exact two-hunk diff in
`validate/cited-lines-repair-proposal.txt` (drop the parenthetical ids from the `recheck:` line; split
the closing sentence into one line per source). Revising the entries is the scribe's call, not this
seat's.

## Advisories

1. **Header key `ground:`** — the amendment carries all nine claim-named keys; the base entry carries
   eight and has **no `ground:` line** (its gap statement is in `- gap filled:`). No pre-existing
   `culture-material` entry uses `ground:` (0 of 34 files), so the key is new to round 72; if the
   `ENTRIES` leg checks it literally in both files, the base entry fails. `reports/round-72/accept-c.py`
   does not exist yet, so this is unverified — not assumed.
2. **Staged-namespace id reuse** — `assimilation/reg-to-staged.txt` uses `S874`/`S875` for the
   *onomastics* staged rows (S791→S874, S792→S875). No registry collision (staged rows are not
   admitted this round), but adopting that staged set later would clash with these heritage rows.
3. **Re-pin before the append** — the entries were still moving at 11:25. Run
   `bash .ufo/waves/round-72/assimilation/validate/refresh-and-validate.sh` after the final revision
   (idempotent: re-copies from `/tmp/r72-entries`, re-runs census + shape/id/URL + cited-lines,
   rewrites `gate-summary.txt`, exits 0 only when all gates are clean) and before any real append to
   `corpus/SOURCES.md`.

## Checks for the main agent

- `bash .ufo/waves/round-72/assimilation/validate/refresh-and-validate.sh` (expect exit 0 once the
  `MULTI-ID` lines are repaired; census and shape/dup/collision gates already exit 0).
- `python3 -B reports/round-72/accept-c.py --root . --lands <lands>` — legs `SCRATCHMIRROR` and
  `COLLCHECK` are backed by `.ufo/waves/round-72/assimilation/validate-receipt.txt`,
  `validate/census-validate-mirror.out` and the three `assimilation/collcheck-*.txt` files.

## Tools installed

None — no install or upgrade was needed (bash, coreutils, gawk, python3 were sufficient).
