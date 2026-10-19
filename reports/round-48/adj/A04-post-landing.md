# A04 — post-landing write-surface census (claim: cross)

- Seat: A04 | role: verifier | claim: cross | `reports/round-48/targets.json:79`
- Out path: `reports/round-48/adj/A04-post-landing.md` (this file)
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` == claims.json:7 `a01405d`
- Seat-time clock: `date -u` → `2026-10-19T19:39:15Z`; final scan `2026-10-19T19:40:18Z` (host TZ `-0300`)
- Status: **post-apply census = `could-not-evaluate`** — the landing had not been applied at this seat. Below: measured pre-landing receipt, declared surface, replica-projected delta, and the exact post-apply procedure with expected outputs.

## 1. Why the post-apply census cannot be certified from here

At `19:40:18Z` the two landing artifacts were absent:

```
$ git rev-parse --short HEAD
a01405d
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...cartography-and-mapmaking.md': No such file or directory
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
```

So the "after the integrator applies C+Ca" state does not exist yet. I do not report a green
post-landing census; I hand the integrator/close verifier a measured pre-state and a
runnable post-state check. The only certificate is the post-apply run (§5).

## 2. Measured pre-landing receipt (HEAD a01405d)

| Fact | Command | Output |
|---|---|---|
| total entries | `find corpus/knowledge -name '*.md' \| wc -l` | `223` |
| tracked entries | `git ls-files 'corpus/knowledge/*.md' \| wc -l` | `223` |
| culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | `25` |
| partition counts | per-dir `ls .../*.md \| wc -l` | linguistics 25, myth-symbol 26, culture-material 25, synthesis 29, verification 24, civilizations 94 |
| corpus tree ids | `git rev-parse HEAD:corpus` / `HEAD:corpus/knowledge` | `31b27aa3b782b8ca2601a355161bcdf110b38392` / `675207b48d89688d7f9198c663bc0c2a8bcb30de` |
| README bytes | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| README length | `wc -l corpus/README.md` | `575` |
| duplicate H1 | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` | `2` (lines 1 and 3, byte-identical: both sha256 `78cd0b41…`) |
| index sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, `footer_ok True`, `readme_sha256 7c788a1d…`, exit 0 |
| cartography absence | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \| wc -l` | `0` |
| cartography topic owners | `grep -rniE '^- topic:.*(cartograph\|mapmak\|portolan\|cadastr\|atlas\|graticule)' corpus/knowledge/ \| wc -l` | `0` |
| corpus/tools writes at baseline | `git status --porcelain=v1 -uall -- corpus tools \| wc -l` | `0` |

README anchors relevant to the expected README `M`: rev 2.4 header `corpus/README.md:5`, prose vector
`corpus/README.md:10-11` (`25/23/26/25/24/94`; 25+23+26+25+24+94 = 217, the live defect), culture-material
section header `corpus/README.md:234` (`(25)`), total `corpus/README.md:544`, footer
`corpus/README.md:548`.

## 3. Declared write surface (`reports/round-48/targets.json`)

```
seat_count 64 | seats 64 | unique ids 64 | unique out paths 64 | duplicate out paths []
claims: C 30, cross 22, Ca 12
roles: verifier 32, executor 13, reviewer 5, critic 5, scribe 4, scout 3, planner 1, connector 1
```

`reports/round-48/` may contain, by contract: the 64 declared out paths, `claims.json`,
`targets.json`, `telemetry/**`, and (if the round produces them) `validation.json` /
`run-validation.py`. Anything else is undeclared. Snapshot at `19:40:18Z`:

```
files_now 19 | declared_out_files_present 16 | undeclared [] | missing_declared 48
```

Sixteen in-flight fragments were present; every one maps to a declared seat out path — no
undeclared file under `reports/round-48/` at that instant. The remaining 48 out paths were
simply not yet written (parallel seats still working), not missing artifacts.

## 4. Replica-projected post-apply delta (scratch only, no repo write)

Method — clone tracked HEAD into scratch, apply the path-level landing (stand-in entry bytes;
bytes are NOT authoritative), then diff with a copied index so the live repo is untouched:

```
git archive HEAD | tar -x -C .scratch/a04/tree
cp .git/index .scratch/a04/idx
# + corpus/knowledge/culture-material/cartography-and-mapmaking.md (stand-in)
# + delete corpus/README.md:3 (the duplicate H1)
GIT_DIR=$PWD/.git GIT_WORK_TREE=$PWD/.scratch/a04/tree GIT_INDEX_FILE=.scratch/a04/idx \
  git status --porcelain=v1
```

Output:

```
 M corpus/README.md
?? corpus/knowledge/culture-material/cartography-and-mapmaking.md
```

Cross-checks on the same replica:

```
git diff --name-only HEAD -- corpus tools        → corpus/README.md          (only tracked M)
git ls-files --others --exclude-standard corpus tools
                                                  → corpus/knowledge/culture-material/cartography-and-mapmaking.md (only untracked)
find corpus/knowledge -name '*.md' | wc -l       → 224
ls corpus/knowledge/culture-material/*.md | wc -l → 26
```

The replica sweep after the two edits reports exactly the expected one-file shortfall and
nothing else — `rows 223 files 224`, `missing_from_index 1 ['culture-material/cartography-and-mapmaking.md']`,
`topic_mismatch []`, `orphan_rows []`, `header_drift {'culture-material': {'declared': 25, 'files': 26}}`.
The full rev-2.5 README edit (row + section count + totals + footer + rev 2.5 + prose-vector
repair) is C10/C11's artifact; the replica intentionally does not predict its final SHA.

Controls (proof the census commands detect what they claim):

- **Negative control** — replica + two extra writes (`corpus/knowledge/culture-material/UNEXPECTED-write.md`,
  `tools/UNEXPECTED-tool.py`):
  ```
  ?? corpus/knowledge/culture-material/cartography-and-mapmaking.md
  ?? corpus/knowledge/culture-material/UNEXPECTED-write.md
   M corpus/README.md
  ?? tools/UNEXPECTED-tool.py
  ```
  A first-draft filter `grep -E '^. (corpus|tools)/'` returned 0 on this control; the shipped
  pattern is `^.. ` (two status columns, then space). The control caught a bad verifier command.
- **Staging control** — after `git add` on the copied index the same delta reads
  `A  corpus/knowledge/culture-material/cartography-and-mapmaking.md` and `M  corpus/README.md`.
  Therefore "lands as A not M" is only literally true **after staging**; an unstaged landing
  correctly shows `??`. Post-landing verification must not accept `??` as a failure nor require
  `A` before staging.

## 5. Post-apply procedure — the delivery certificate

Run from the lane root after the integrator applies C+Ca. Every check must produce the stated
output; one deviation fails the census.

```
# 1. corpus delta is exactly one M + one new path
git status --porcelain=v1 -uall | grep -E '^.. (corpus|tools)/'
# expected:  M corpus/README.md
#           ?? corpus/knowledge/culture-material/cartography-and-mapmaking.md

# 2. no tracked corpus/tool bytes moved except README
git diff --name-status HEAD -- corpus tools
# expected: M	corpus/README.md

# 3. exactly one new untracked corpus path
git ls-files --others --exclude-standard corpus tools
# expected: corpus/knowledge/culture-material/cartography-and-mapmaking.md

# 4. counts
find corpus/knowledge -name '*.md' | wc -l            # 224
ls corpus/knowledge/culture-material/*.md | wc -l      # 26

# 5. README duplicate H1 is gone
grep -c '^# kotodama-shokunin corpus index' corpus/README.md   # 1

# 6. index sweep
python3 -B reports/round-28/readme/sweep.py            # rows 224 files 224, footer_ok True, exit 0

# 7. nothing outside the allowed envelope
git status --porcelain=v1 -uall | sort \
  | grep -vE '^(.. (corpus/README\.md|corpus/knowledge/culture-material/cartography-and-mapmaking\.md|reports/round-48/.*))$' \
  | grep -vF '?? reports/round-46/review/R01-review.md'
# expected: no output
# control (2026-10-19T19:44Z): tested on a synthetic status containing the allowed
# README M + entry ?? + a reports/round-48 fragment, plus tools M, a third corpus M and
# a reports/round-47 ?? — it emitted exactly those three violation lines; on the live
# pre-landing status it emits nothing.
```

Violation criteria (each is a fail, not a warning):

1. Any `M` under `corpus/` other than `corpus/README.md` — a `D` is worse (overwritten entry).
2. Any second new corpus file, or any new path under `templates/`, `examples/`, `tools/`,
   `corpus/lessons/`, `tools/gates/frozen/`, or `.ufo/`.
3. Any write under `reports/round-1..47/**` (including a *new* file there: filed rounds are
   append-only and closed; the Ca queue successor must land as a new record under
   `reports/round-48/`, following the `reports/round-47/calib/queue-successor-r47.json`
   precedent, whose schema is `kotodama-defect-queue-successor-v1`).
4. Sweep not green 224==224, or README H1 count not 1, or prose vector not summing 224
   (`25/26/26/29/24/94` = 224).
5. Any file under `reports/round-48/` that is neither a declared out path, nor `claims.json`,
   `targets.json`, `telemetry/**`, `validation.json`, `run-validation.py`.

Expected reports envelope at close: 64 declared out files + the allowlist above; enumerate with
`find reports/round-48 -type f | sort` and map each path against `targets.json` seats.

## 6. Baseline anomalies to subtract, not attribute to the landing

- **Pre-existing untracked:** `reports/round-46/review/R01-review.md` (mtime `2026-10-19 14:48:54 -0300`
  = `17:48:54Z`, before the r48 declaration). It is not a round-48 write; exclude it from the
  post-apply status read (done explicitly in §5 step 7).
- **Declaration timestamp vs file mtime (to-verify):** `claims.json` mtime `19:36:19Z` and
  `telemetry/dispatch-declared.json` mtime `19:37:31Z`, while both record
  `declared_at_utc`/`recorded_at_utc = 2026-10-19T19:45:00Z` — the recorded instant is 8m41s and
  7m29s **after** the files' own mtimes. This is not a write-surface violation, but the recorded
  timestamp should not be used as a sampling-window start without reconciliation. Owner:
  integrator; status: `to-verify`.
- **Ca successor path (to-verify):** the exact filename of the r48 queue successor was not yet
  observable at this seat. If it lands anywhere other than `reports/round-48/`, criterion 3 fails.

## 7. This seat's write surface

Files written by A04: `reports/round-48/adj/A04-post-landing.md` only. Scratch copies under
`.scratch/a04/` (archive replica, copied index, negative control) are disposable and outside the
repo's tracked surface (`TMPDIR=$PWD/.scratch`). No `corpus/`, `tools/`, or filed-round byte was
touched; no `git add`/commit was run against the real repo (the staging control used a copied
index against the scratch worktree).

## 8. What remains unverified

- The post-apply census itself: `could-not-evaluate` at seat time; owner integrator; rerun §5
  after applying C+Ca.
- Entry content/length and the final README SHA: C05/C11/D01 own those; this report deliberately
  does not predict them.
- Whether the integrator stages the new entry (`A `) or leaves it untracked (`??`): both are
  acceptable at the write-surface layer, but the record must state which was observed.
