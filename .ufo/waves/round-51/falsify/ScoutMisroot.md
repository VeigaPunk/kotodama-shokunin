# ScoutMisroot — misroot sweep (round 51, attempt 3, falsify wave)

Item attacked: misroot containment for this round. Two questions only: (a) does any file at the fleet
root outside the lane carry kotodama round 51 or a `KotodamaR51a3` seat, and (b) does the lane hold any
status-visible file outside `.ufo/waves/round-51/`. This seat does not attack claim D or claim C content
and does not admit either.

Bounds respected: read-only on the lane, no jj, no git write, no installs, no writes outside this report.
Fleet root HEAD moved under me during the sweep (`7d0860d` to `7f8dc0d`), so the fleet inventory below is
a timestamped snapshot (2026-10-22T09:41Z to 09:53Z), not a stable state.

## Commands and results

| Command | Output (essential) | Exit |
|---|---|---|
| `git -C /home/vgpnk/Projects/shokunin status --porcelain` | 17 entries: 6 intent-to-add `A` (`.scratch/goal-20261022-hyaku-12h.md`, `.ufo/state/{kotoba,kotodama,revenger}.report-baseline`, `scripts/hyaku/__pycache__/append-closure.cpython-314.pyc`, `write`) and 11 modified `M` (10 `.ufo/state/*.report-baseline`, `.ufo/watchdog.log`) | 0 |
| `git -C .../kotodama-shokunin status --porcelain` | `?? .ufo/waves/round-51/` only | 0 |
| `git status --porcelain --ignored=matching` (lane) | adds `!! reports/round-51/__pycache__/`; also `.jj/`, `.scratch/`, old `run.log`s | 0 |
| `file` + `stat` + `head` on the three new fleet files | see findings 1 to 3 | 0 |
| `xxd write` | 25 bytes: `agent://U100N079H334f935b`, no newline | 0 |
| `git status --porcelain=v2` (fleet) | the 6 `A` entries are `1 .A N...` with all-zero object ids, i.e. **intent-to-add**, not real index blobs | 0 |
| `git ls-files -s write` | `100644 e69de29...` (empty blob) | 0 |
| `git ls-tree HEAD write` | empty (path not in HEAD) | 0 |
| `git diff --stat -- write .scratch/goal-...` | `write` 1 insertion, goal file 247 insertions (worktree content only) | 0 |
| `git log --oneline --all -- write` | one commit, `735c271` (2026-10-22T05:21:22), empty subject; path absent from HEAD tree | 0 |
| `grep -rIl 'U100N079H334f935b'` and `grep -rIl 'hyaku (百) 12-hour training leg'` over the lane | no file | 1 |
| `find` lane `-type f \( -size 25c -o -size 17367c \)` | nothing | 0 |
| `grep -rIl 'KotodamaR51a3'` fleet root, excluding lane dirs | `.ufo/waves/hyaku/PHASE3.md` only | 0 |
| `grep -n -E 'kotodama\|r51\|round.?51'` in `.ufo/watchdog.log` | lines 640, 649, 661, 664, 670 | 0 |
| `find .ufo/reports -maxdepth 1 -type d -empty` | `.ufo/reports/round-51` (2026-10-21) | 0 |
| `find .ufo/reports/round-51 -mindepth 1 \| wc -l` | `0` | 0 |
| `find lane -name 'boundary-count*'` | `reports/round-51/boundary-count.py` (3768 B) and `reports/round-51/__pycache__/boundary-count.cpython-314.pyc` (7192 B) | 0 |
| pyc header decode (`struct.unpack('<4sIII')`) | flags 0, src_mtime 1792657213, src_size 3768; current source mtime and size match exactly → not stale | 0 |
| `grep -n 'README\|KNOWLEDGE\|os.path.join(LANE' reports/round-28/readme/sweep.py` | sweep reads only `corpus/README.md` and `corpus/knowledge` | 0 |

## Findings

**1. LOW — fleet-root file literally named `write`.**
`/home/vgpnk/Projects/shokunin/write`, 25 bytes, `agent://U100N079H334f935b`, mtime 2026-10-21 19:52:50,
intent-to-add in the fleet index. The mtime is 45 minutes *before* round 51 attempt 1 launched
(`.ufo/watchdog.log:640`, 20:38:02), so no round-51 seat produced it, and it holds no round number and no
seat id. It looks like a `write` call whose path argument was dropped. Smallest fix (fleet owner, not me):
delete the file and unstage the intent-to-add; no lane action.

**2. LOW — staged bytecode of a fleet helper.**
`/home/vgpnk/Projects/shokunin/scripts/hyaku/__pycache__/append-closure.cpython-314.pyc`, 10738 bytes,
intent-to-add, compiled from the tracked `scripts/hyaku/append-closure.py`. `strings` shows only the
closure helper's own text and `SHOKUNIN_ROOT=/home/vgpnk/Projects/shokunin`; no round 51, no seat id.
Smallest fix: delete it and add `__pycache__/` to the fleet `.gitignore`, otherwise a later
`git commit -a` at the fleet root commits build output.

**3. LOW — session contract at fleet root that does name round 51.**
`/home/vgpnk/Projects/shokunin/.scratch/goal-20261022-hyaku-12h.md`, 17367 bytes, intent-to-add. Named
lines: `:87` "tameshi r25, tsukuroi r24, kake r28 and kotodama r51; all are at attempt 1", `:105`
"| C7 | kotodama (r51) | ... (226 knowledge entries) ... `kotodama51-prereg-critic` item hold stays",
`:212` "The `kotodama51-prereg-critic` item." This is Main's own 12-hour contract, not lane output, and it
names no `KotodamaR51a3` seat. Same bytes are absent from the lane (size 17367 matches no lane file; the
title grep returns nothing). Smallest fix: commit or ignore it deliberately so the fleet root stops
carrying an intent-to-add that a blanket commit would absorb together with findings 1 and 2.

**4. LOW — empty round-51 directory at fleet root, outside the wave directory.**
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-51/`, created 2026-10-21 20:38 (the attempt 1 launch
minute) and holding **0 files**. Git does not report empty directories, so it never appears in
`status --porcelain`, and with no file it cannot alter any count or quote. Smallest fix: `rmdir` it; the
round's reports belong in the lane `reports/round-51/` and `.ufo/waves/round-51/`, which is where they are.

**5. LOW — round-51 bytecode inside the lane but outside `.ufo/waves/round-51/`.**
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-51/__pycache__/boundary-count.cpython-314.pyc`,
7192 bytes, mtime 06:28, i.e. inside attempt 3 (launched 06:19:49 per `.ufo/watchdog.log:670`). Header
check: recorded source mtime and size (1792657213 / 3768) match `reports/round-51/boundary-count.py`
exactly, so the bytecode is current, not stale. It is matched by `.gitignore:4:__pycache__/` and therefore
invisible to plain status. It cannot move a declared number: the D counter opens only the entry file, and
the C sweep reads only `corpus/README.md` and `corpus/knowledge/**` (`reports/round-28/readme/sweep.py:46-47`).
It is still a round-51 write outside the wave directory, which means someone ran the counter without the
`-B` flag that `reports/round-51/claims.json` writes into the command. Smallest fix: `rm -rf` the directory
and keep `-B` on every run. Severity stays low because bytecode is not an input to any check and `-B` does
not read a `__main__` pyc.

**6. INFO — fleet driver state, correctly placed.**
`.ufo/watchdog.log` (modified, tracked) names round 51 at `:640` launch attempt 1, `:649` lane dead,
`:661` launch attempt 2, `:664` stood down, `:670` launch attempt 3. `.ufo/state/kotodama.report-baseline`
(intent-to-add, 68 bytes, mtime 06:19:48) holds only `51 e3b0c442...`, a length and an empty-file hash; it
carries no round word and no seat id. Both are fleet-owned bookkeeping, not lane output.

**7. INFO — the only seat id outside lane directories is the campaign ledger.**
`.ufo/waves/hyaku/PHASE3.md:204` records the dispatch ("Dispatch kotodama r51 attempt 3 (last this
session) ... base `bff83ba6`; L1 `KotodamaR51a3`"). Tracked, Main-authored, expected. No seat report or
lane byte escaped there.

## Byte-identity check against the lane

No fleet-root stray has a counterpart under `/home/vgpnk/Projects/shokunin/kotodama-shokunin`:

- no lane file has size 25 or size 17367 (the two distinctive stray sizes);
- `U100N079H334f935b` and the goal file's title line do not occur anywhere in the lane;
- the lane has no `.ufo/watchdog.log` (`.ufo/` contains only `waves/`), and lane `.scratch/` is empty;
- the four lane `reports/round-51` top-level files (`boundary-count.py`, `claims.json`,
  `separability-manifest.json`, `claims-agree.py`) have no fleet-root twin because `.ufo/reports/round-51`
  holds no files at all.

## Lane status outside `.ufo/waves/round-51/`

None from plain `git status --porcelain`: the single line is `?? .ufo/waves/round-51/`. The only additional
round-51 path under `--ignored=matching` is finding 5, which is gitignored. `.jj/` and `.scratch/` are
normal ignored colocated state.

## Sources opened

None. This sweep needed no URL, so no access date is claimed and no quote, tier or scope is assessed.

## Verdict

**HOLDS-WITH-FIXES.** The containment property I was sent to break survives: no round-51 seat wrote
outside the lane, no lane byte or seat id appears at the fleet root, and the lane shows nothing outside
`.ufo/waves/round-51/` except one gitignored pycache. Findings 1 to 4 are pre-existing fleet hygiene and
predate this attempt; finding 5 is the only round-51-produced deviation, it is a missing `-B`, and it
changes no measured value for claim D or claim C. Fixes: `rm -rf` the lane pycache (finding 5), `rmdir`
the empty `.ufo/reports/round-51` (finding 4), and let the fleet owner clear the three intent-to-add
entries (findings 1 to 3) before any blanket commit at the fleet root.

## Unrun

- `python3 -B reports/round-51/boundary-count.py` and `python3 -B reports/round-28/readme/sweep.py` were
  not run by this seat: they belong to the counter seats, and running them would write into the lane.
- No `lsp` query was needed; the questions were file existence, byte identity and git state.
- No `history://` lookup for the origin of `write`; it predates the round and is out of this item's scope.
- No tool installs or updates were made.
