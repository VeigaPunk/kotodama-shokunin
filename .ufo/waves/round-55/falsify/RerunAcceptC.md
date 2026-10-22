# RerunAcceptC — claim C (monsters entry, S285–S357) rerun acceptance

Verdict: CARRIED. Every leg of the declared counting command passes at the landed
tip with the exact declared output, and the base fails with the exact declared
"before" output. The criterion-11 control receipt is reproduced byte-for-byte
(14/14 as expected); the census `validate` run is `ok`; the two auxiliary checks
both exit 0; and the corpus/knowledge diff between base and claim C contains
exactly the entry plus the three routed-fix files.

## Checked items (one line each)

- `reports/round-55/accept-c.py` at `eb0a331` (sandbox clone, checkout at claim
  C): exit 0 — `SET PASS count=231 required=231 added=['corpus/knowledge/myth-symbol/monsters-hybrid-beings.md'] removed=[]`; `SWEEP PASS exit=0 rows 231 files 231 missing_from_index 0 []`; `FLOOR PASS cited=73 floor=20`; `RANGE PASS bad=[] range_notation=[]`; `STATUS PASS bad=[]`; `USEDBY PASS bad=[]`; `ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings` — CARRIED (matches claim's `after_required`: count 231, added [entry], removed [], rows 231 files 231, missing_from_index 0, cited ≥ 20, no bad S-id, ACCESS exit 0).
- `reports/round-55/accept-c.py` at `f4015e7` (sandbox clone, checkout at base):
  exit 1 — `SET FAIL count=230 required=231 added=[] removed=[]`; `SWEEP FAIL exit=0 rows 230 files 230 missing_from_index 0 []`; `FLOOR FAIL cited=0 floor=20`; `RANGE PASS bad=[] range_notation=[]`; `STATUS PASS bad=[]`; `USEDBY PASS bad=[]`; `ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings` — CARRIED (matches claim's declared `before`: exit 1, SET FAIL (count=230), SWEEP FAIL (rows 230 files 230), FLOOR FAIL (cited=0); RANGE/STATUS/USEDBY PASS vacuously; ACCESS PASS).
- `python3 -B reports/round-55/criterion11-controls.py <clone> f4015e70b829523ed81e14ce4279bfab0e0233e4`: exit 0, `CONTROLS 14/14 as expected`; all controls AS EXPECTED (GREEN 0, RED-COUNT 1 [SET, SWEEP], RED-SET 1 [SET], RED-SET-EXT 1 [SET], RED-SWEEP 1 [SWEEP], RED-SWEEP-EXIT 1 [SWEEP], RED-FLOOR 1 [FLOOR], RED-RANGE 1 [RANGE], RED-RANGE-NOROW 1 [RANGE], RED-RANGE-DUP 1 [RANGE], RED-RANGE-SPAN 1 [RANGE], RED-STATUS 1 [STATUS], RED-USEDBY 1 [USEDBY], RED-ACCESS 1 [ACCESS]); sha256 pins in output match the receipt — CARRIED. `diff -u reports/round-55/telemetry/criterion11-controls.txt` vs the fresh run output: exit 0, zero differences (byte-identical).
- `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`: exit 0, final line `kotodama ok /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`; only pre-existing W04 duplicate-url warnings (S127–S133, S185–S186, S358) — CARRIED.
- `python3 -B tools/check-draft-ids.py` at lane worktree: `DRAFT_IDS: 0 findings`, exit 0 — CARRIED.
- `python3 -B tools/check-source-access.py` at lane worktree: `ACCESS: 2 flagged rows, 0 findings`, exit 0 — CARRIED (the 2 flagged rows are rejected-status bypass-marker rows; the check exits 0 because no finding is raised, consistent with the base run above).
- `git diff --name-only f4015e7 eb0a331 -- corpus/knowledge` lists exactly 4 files: `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md` (the entry, carried by `eb0a331`), `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` (routed fix, `b9c44a2`), `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (routed fix, `81178c8`), `corpus/knowledge/myth-symbol/divination-omen-systems.md` (routed fix, `d52c9df`) — CARRIED. Attribution via `git log --oneline f4015e7..eb0a331 -- <file>`: the entry file is touched only by `eb0a331`; gesture only by `b9c44a2`; speech-surrogates only by `81178c8`; divination-omen-systems only by `d52c9df`. (`b9c44a2`'s commit message also mentions a speech-surrogates wording/reach edit, but its stat touches only `corpus/SOURCES.md` and gesture; the speech-surrogates wording edit is in `81178c8`.)

## Tooling installs

None. No tool installed or updated (no pacman, no uv/npx/cargo/npm); all commands used already-present binaries (`git`, `python3`, `bash`, `tar`).

## Unrun checks

- `python3 -B reports/round-55/accept-c.py` at the lane worktree tip was not run; the lane worktree has uncommitted changes (e.g. `corpus/SOURCES.md` modified, `corpus/lessons/round-55.md` untracked) and the assignment specified the sandbox clones at the two pinned commits, which is where the runs were made.
- The census was run read-only against the lane; its W04 warnings are pre-existing and not part of this rerun.
