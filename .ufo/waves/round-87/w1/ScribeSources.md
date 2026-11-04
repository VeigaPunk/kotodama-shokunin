# ScribeSources — round-87 w1 report

Axes: operability. Milestone r87-v1. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; base `83846a22ee1e9da7aa52ac505ccebf4455169247`; prefreeze controls `732c45394c73fcffd9fc623b939d446c7b11a9db`.

## Behavior

Drafted one own-work A/mined row and one own-work C/rejected row for `corpus/SOURCES.md`, as append-only fragments. Nothing was appended to production.

- **S929** (new, own-work, tier A, mined, used-by `corpus/lessons/round-87.md`). Source is the committed r86 craft packet at base 83846a22: a six-case NON-CANON fictional attestation-record interface. Scope is that interface only; the packet itself refuses historical truth. Nearest dossier rows S924–S926 are cited, not reopened, and no external URL is added.
- **S930** (new, own-work, tier C, rejected). Source is `.ufo/waves/round-87/w1/stage/CriticCounter/constant-pass.py`, which this seat opened read-only. It prints a fixed record regardless of input, so it cannot read a subject or fail. Reason, flip, and an actual located quote are in the row.
- Next unused ids were determined from the registry table: the last row is S928 at line 884, and S929/S930 appear nowhere in the file.

## Gate

Full Gate is in `.ufo/waves/round-87/w1/stage/ScribeSources/gate.md`.

- Access date for every opened body: 2026-11-04. No search engine and no new external URL.
- Revision check: the r86 `craft.json` blob at 83846a22 has sha256 `4f631b60…` and is identical to the worktree copy. The reopened `proverbs-riddles-attestation-solutions.md` has sha256 `578c1ae2…` and is identical to its base blob.
- Quotes: S929 is 20 words ("All wording, people, documents … lore proposals."). S930 is 8 words ("Counterfeit non-reader: must not satisfy the finite battery.").

## Stage files

Directory `.ufo/waves/round-87/w1/stage/ScribeSources/`:

- `rows-sources.md`: the two 11-cell fragment rows.
- `gate.md`: provenance, quote locators, decisions, and bounded search note.
- `receipts/craft-r86-base83846a22.json`, `receipts/proverbs-riddles-attestation-solutions-opened-2026-11-04.md`, `receipts/constant-pass-opened-2026-11-04.py`, with sha256 values as in the Gate.

Scratch `/fast/scratch/hyaku/kotodama-r87/ScribeSources/` was created for the work, copied into the stage directory, and removed. It was never under `/tmp`.

## Out of scope

- Production `corpus/SOURCES.md`, `corpus/lessons/`, `corpus/knowledge/`, and `QUALITY.md` were not edited.
- The frozen `reports/round-87/claims.json` and `measure87.py` were not opened, run, or modified. The operability claim is not rescored here.
- No git/jj mutation, index change, commit, install, delegation, or background job.
- No executable probes were run; the checks were read-only hashes, byte reads, and counts.
- No tools were installed. `/home/vgpnk/.omp/agent/RULES.md` was read first, and existing tools were sufficient.

## Findings and limits

- The Gate's bounded search note records that the S924–S926 external bodies were not reopened by this seat. Their status rests on the round-86 record.
- Whether sibling seats later change `constant-pass.py` is unresolved. Identity is pinned by sha256 `78b66e10…`, not by path stability.
- The constant-pass candidate is evaluated as a sibling artifact. Its own role in the round-87 counter battery is not judged by this seat.

## Checks for the main agent

- Confirm `rows-sources.md` IDs S929 and S930 are unused at integration time: `grep -c 'S929\|S930' corpus/SOURCES.md` should return 0.
- Confirm the `corpus/lessons/round-87.md` used-by target exists when S929 is integrated.
- Confirm the Gate is retained in that lesson.
- Confirm the `constant-pass.py` sha256 still matches `78b66e106bb4a149849a09d92c02fc0b7dd43316fa66a680a22ec07eef01567d` if S930 is integrated.
