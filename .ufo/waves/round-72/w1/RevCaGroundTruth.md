# RevCaGroundTruth — K71-1/3/4/5/6/7 verification against committed bytes

- Seat: `L1Kotodama72.RevCaGroundTruth` (leaf reviewer; no subagent dispatch).
- Round 72, hyaku run 6. Frozen claims read: `reports/round-72/claims.json` (claim Ca `before` enumerates K71-1..K71-8).
- Lane tip at verification time: `b60c7b1` (base; the lane worktree sits on the base commit). Fresh clone at base: `/tmp/L1Kotodama72.RevCaGroundTruth/clone` (`git clone` of the lane, `git checkout b60c7b1`). All lane/fleet reads are read-only; the only lane write is this report.
- Tools: no installs or updates (git and python3 only; RULES.md noted, nothing installed).

## K71-1 — QUALITY criterion 20 uncommitted at base: CONFIRMED

Commands (lane repo, HEAD = `b60c7b1`):

```
git show b60c7b1:corpus/QUALITY.md | grep -c '^20\. '   → 0
grep -c '^20\. ' corpus/QUALITY.md                       → 1   (worktree)
git diff b60c7b1 -- corpus/QUALITY.md                     → 2 insertions, 0 deletions
```

The base commit has **zero** lines starting `20. `; the worktree has exactly one, added by an uncommitted diff (`+20. **Trend verdicts fire only on LEARNING.md observables** — …`). Criterion 20 exists only as an uncommitted worktree diff at base. **Confirmed.**

## K71-3 — three in-place fleet-report rewrites (bc418b99 / 98873dfd / 8380f703): CONFIRMED

All three are commits in the fleet repo (`/home/vgpnk/Projects/shokunin`), all touching the filed round-71 report `.ufo/reports/round-71/kotodama.md` in place (1 line replaced / heading replaced / 2 bullets replaced) rather than appending a correction. Superseded text for each:

1. **`bc418b99`** ("round-71: kotodama report correction (round total 77)") — superseded text: **"Round total 78 seats ≤128."** (inside the Wave-2 shape line, `- Shape: **two v1 waves**. … Wave 2 (falsify): 40 seats … Round total 78 seats ≤128. …`) → replaced in place by **"Round total 77 seats ≤128."** (1 insertion / 1 deletion).
2. **`98873dfd`** ("round-71: kotodama report — RevGate addendum (R71-M8)") — superseded text: the filed heading **"## Wave-2 falsification results (40 seats; partial at filing, consolidated here)"** → replaced in place by `## Wave-2 falsification results` + a new R71-M8 bullet + a dangling continuation line `(40 seats; partial at filing, consolidated here)` (4 insertions / 1 deletion).
3. **`8380f703`** ("round-71: kotodama report — Trend verdicts corrected") — superseded texts: the two filed Trend-verdict bullets **"- **quality — improved.** The round's record instruments are re-verified: receipt headers restored to the QUALITY 17/19 bar (V70-1), S860 pointer accuracy repaired (V70-2), Gate quote discipline restored (V70-3). No admitted entry fails its re-check."** and **"- **discernment — improved.** The outside round-70 spot-check's five disagreements were turned into landings (V70-1..V70-5) …"** → replaced in place by `quality — unchanged` / `discernment — unchanged` versions (2 insertions / 2 deletions).

All three are in-place rewrites of previously filed bytes; no appended correction row names the superseded text. **Confirmed** (each commit's diff contains the removed text verbatim).

## K71-4 — LOG.md in-place S861→S992→S874→S1005 and <RECORDS>/misroot edits: CONFIRMED

Pickaxe over lane `LOG.md`:

```
git log --oneline -F -S 'S861→S992' -- LOG.md   → 1d1b432 (wrote it), 99e3d63 (removed it)
git log --oneline -F -S 'S874→S1005' -- LOG.md  → 99e3d63 (introduced it)
git log --oneline -F -S '<RECORDS>'  -- LOG.md  → 1d1b432 (wrote it), 1721fbd (removed it)
git log --oneline -F -S 'misroot'     -- LOG.md  → 1721fbd (rewrote it)
```

- **`99e3d63`** — LOG.md (hunk at current line ~4274): `- **Item 10.** … renumber map (S861→S992 by document); …` → `+ **Item 10.** … renumber map (S874→S1005 by document); …` — **1 insertion / 1 deletion, in-place**. Same commit rewrites `corpus/lessons/round-71.md` in place: `-collisions S859 S860; id-renumber-map.json S861→S992 by document). No` → `+collisions S859 S860; id-renumber-map.json S874→S1005 by document). No` (1/1). It also supersedes `id-renumber-map.json` (the 65ff151-era S861→S992 span; at 99e3d63 `span` is `S874\u2192S1005` and the collisions array grows to 15). No old→new record is appended anywhere; the old text is gone from the files.
- **`1721fbd`** — LOG.md two hunks, both in-place (2/2):
  - Base line: `records <RECORDS>.` → `records \`1d1b4325\`; final receipts \`3764c2df\` / re-stamps \`7179d6d6\`.` (the `<RECORDS>` placeholder is superseded).
  - Misroot sweep line: `Fleet status lists only driver state and orchestrator-owned scratch; no lane file misplaced.` → the detailed seven-artifact relocation sentence (s795.pdf, s796.pdf, s804/s814/s816/s817.html, s820.pdf written to fleet root, relocated byte-exact to `.ufo/waves/round-71/assimilation/fetches/`, fleet copies deleted at `ccadb59`, recorded under lesson Mistakes).

Confirmed: both edits are in-place rewrites of existing lines, with the superseded text removed rather than preserved. **Confirmed.**

## K71-5 — fleet report still says S861→S992 at :57/:61: CONFIRMED

Current `.ufo/reports/round-71/kotodama.md` (post the three fleet commits):

- Line 57: `map S861→S992 recorded for adoption.`
- Line 61: `renumber map by document (S861→S992) at \`.ufo/waves/round-71/assimilation/\`.`

Both lines still carry the superseded S861→S992 mapping while the committed `id-renumber-map.json` now holds span S874→S1005. **Confirmed.**

## K71-6 — quarantine tally and wave-2 count mismatches: CONFIRMED

(a) Quarantine tally — table vs report/LOG/lesson:

- **Table** `reports/round-71/telemetry/quarantine-verdicts.md:36`: `Tally: PRESENT 10 · REFUSED 7 · UNVERIFIABLE 4 = 21` → **10/7/4** (matches the 21 row table itself; rows S779/S786/S787/S792/S814/S816/S817 = 7 REFUSED; S791/S807/S812/S835 = 4 UNVERIFIABLE).
- **Fleet report** `kotodama.md:61`: `Quarantine verdicts: 21 rows (PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5)` → **10/6/5**.
- **LOG.md:4270**: `Item-10 quarantine table 21 rows (PRESENT 10 / REFUSED 6 / UNVERIFIABLE 5)` → **10/6/5**.
- **Lesson** `corpus/lessons/round-71.md:80-81`: `(PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5)`; `:95`: `verdicts 10/6/5 re-confirmed` → **10/6/5**.
- Also `reports/round-71/telemetry/measures-ca.txt:22`: `QUARANTINE: rows=21 unique=21 labels-ok (PRESENT 10 / REFUSED 6 / UNVERIFIABLE 5)` → **10/6/5**.

Confirmed: report/LOG/lesson/measure texts record 10/6/5; the verdict table itself is 10/7/4.

(b) Wave-2 seat count — spec.json vs LOG/lesson/report:

- `w2/spec.json` (`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-71/w2/spec.json`): top-level keys `reportDir/context/items`; `len(items) = 40`.
- **LOG.md:4272**: `wave-2 41 seats (attack roles) below; round total 78 ≤128` → 41/78.
- **Lesson** `round-71.md:8`: `wave 2: 41 seats (below). Round total 78 seats, ≤128.` → 41/78.
- **Fleet report** (after `bc418b99` in-place correction): `Wave 2 (falsify): 40 seats … Round total 77 seats ≤128.` → 40/77.

Confirmed: `w2/spec.json` carries 40 items; LOG/lesson record 41/78 while the report text says 40/77.

## K71-7 — measures-ca.txt counter sha vs accept-ca.py at the stamped revision: CONFIRMED

`reports/round-71/telemetry/measures-ca.txt` top header (lines 1-4):

```
# counter sha256 (self): 1ce25fb9ade45c263ba8ddec32f4fb73492ee5f0e82ef2e501bfa975fdcd2517
# stamped revision: 64da9e14e5fa512c7f9c1d7695f48b6d34009b47
# evaluated revision: 64da9e14e5fa512c7f9c1d7695f48b6d34009b47
# measured revision (lane main): 64da9e14e5fa512c7f9c1d7695f48b6d34009b47
```

Computed shas (`sha256sum` of the blob at the given revision):

```
git show 64da9e14:reports/round-71/accept-ca.py | sha256sum → f706aacd001ee5448ef9f32f8dc2d5bdd90839e8f3811311819fe3791fee9a3e
git show b60c7b1:reports/round-71/accept-ca.py | sha256sum → 1ce25fb9ade45c263ba8ddec32f4fb73492ee5f0e82ef2e501bfa975fdcd2517
sha256sum <worktree>/reports/round-71/accept-ca.py         → 1ce25fb9ade45c263ba8ddec32f4fb73492ee5f0e82ef2e501bfa975fdcd2517
```

- The header pairs counter sha `1ce25fb9…` with stamp `64da9e14`, but at `64da9e14` `accept-ca.py` hashes to **`f706aacd…`** — the sha named in the header did not exist at the stamped revision (`64da9e14` is an ancestor of base, checked via `git merge-base --is-ancestor 64da9e14 b60c7b1` → yes). `1ce25fb9…` matches the counter at base/worktree only.
- The receipt's own preserved original block (lines 9-14, below the marker) records exactly the true pairing: counter `f706aacd…` at the same stamp `64da9e14…` — i.e. the top header was re-stamped by rewriting the header block in place (no `append-only` marker discipline for the header), leaving a self-contradictory file.
- This independently corroborates the round-71 `RevCounterCa`/`RevReceipts` finding (F7/K71-7 source).

**Confirmed.**

## Residual risk / verification gaps

- Tickets K71-2 and K71-8 were not assigned to this seat and were not verified here (K71-2: uncommitted round-71 w2 seat files — noted incidentally: `git status` at base shows 2 modified (`Filler30.md`, `RevReceipts.md`) and 5 untracked (`CritTrends.md`, `Filler28.md`, `Filler36.md`, `RevCounterCa.md`, `RevEntry.md`) w2 seat files, matching the claim's `before` text).
- All six assigned defects are confirmed against committed bytes at base `b60c7b1` plus the named commits; no refutation found.
- K71-3's fleet commits (bc418b99/98873dfd/8380f703) are not in the lane repo (they live in the fleet repo); their diffs are cited above directly from the fleet repo.
