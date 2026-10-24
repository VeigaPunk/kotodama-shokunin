# CriticD1Manifest — attack on the R66-D1 manifest leg (accept-ca.py D1)

Scope: `reports/round-67/accept-ca.py` lines 122–155 (the D1 leg) and the artifact it
claims to certify, `reports/round-67/dispositions/r66-wave-evidence-manifest.txt`
(does not exist yet — authored this wave; verified: `reports/round-67/` contains only
accept-*.py, claims.json, telemetry/). Frozen defect being dispositioned
(corpus/lessons/round-66-verifier-spotcheck.md:102): *"commit wave evidence or record
why it is excluded — `.ufo/waves/round-66/` is entirely untracked; D3's seat-file
predicate is undurable without it. If scratch clones made the commit too large, commit
a curated subset (registry, seat reports, row fragments) and say so."*

## What the leg actually checks

```
man = read(root, MANIFEST)                      # WORKTREE bytes, not lands bytes
INCLUDE \S+ -> include[]                         # no dedup, no path-class bound
EXCLUDE  <anything> -> exclude[]                 # any nonempty line counts
seat  = [p for p in include if p =~ ^\.ufo/waves/round-66/w1/[^/]+\.md$]
cat-file -e <lands>:<p> == 0 for every p in include
FAIL iff: manifest_absent | no_includes | seat<8 | any include untracked | no EXCLUDE lines
```

## What `cat-file -e` proves — presence of AN object, not content, not blob-ness

Verified on this repo (`git cat-file -e HEAD:corpus` → exit 0, type `tree`):

- **A directory passes.** `INCLUDE .ufo/waves/round-66/w1` satisfies the
  exists-at-lands test while adding zero durable content. The demand "commit wave
  evidence" is not met by committing a tree.
- **An empty file passes.** `/tmp` repro: `git cat-file -e HEAD:empty.md` → exit 0,
  `cat-file -s` = 0 bytes. No size floor anywhere in the leg. 63 empty
  `w1/*.md` stubs = D1 PASS with zero r66 evidence.
- **Wrong content passes.** `-e` never compares bytes. Any pre-existing committed
  file (e.g. `INCLUDE README.md`, `INCLUDE LOG.md`) inflates `includes=N` and the
  seat regex only constrains 8 of them; the rest may point at anything tracked.
- **A gitlink FAILS** (exit 1, "could not get object info") — verified — so the
  check silently forces the honest exclusion of embedded repos (see §3). Good.
  But note the asymmetry: it enforces exclusion by accident, never by rule.
- Includes are checked against `<lands>:` — that part is correct — but see §4:
  the manifest selecting them is not.

So: **the leg proves presence-at-lands, never content.** "Durable" reduces to
"an object exists," which is the weakest reading of R66-D1 that still prints PASS.

## Exploit 1 (cheapest): duplicated seat lines, one real file

`include.append` never dedups; `seat` is a filtered list, not a set. Manifest:

```
INCLUDE .ufo/waves/round-66/w1/ScoutRow02.md     # x8 identical lines
EXCLUDE scratch trees
```

→ `seat_reports=8`, `includes=8`, one committed file. D1 PASS. Even cheaper:
8 lines naming one *empty* file (exit 0 on empty blob, confirmed). The seat count
claims ≥8 distinct seat reports; the code counts ≥8 matching *strings*.

## Exploit 2: the manifest itself is never proven committed at lands

`read(root, MANIFEST)` reads `os.path.join(root, ...)` — **worktree bytes**.
Nothing runs `cat-file -e <lands>:<MANIFEST>` or `git show lands:<MANIFEST>` on it.
Consequences:

- The evaluator protocol runs counters "inside a materialized clone at the lands
  commit" — enforced only by STAMP (`rev-parse main` == --lands). STAMP compares
  HEAD to lands; **a dirty worktree file is invisible to `git rev-parse`.** Land
  manifest v1 (honest), then overlay `reports/round-67/dispositions/…txt` in the
  clone before running: counter parses v2, `cat-file -e lands:<v2-paths>` can even
  pass if the paths happen to exist. The receipt records stamped==evaluated==lands
  while the parsed manifest is uncommitted bytes. The "committed manifest" wording
  of the leg is unfalsified by its own test.
- Even in a clean clone: if the integrator forgets to commit the manifest but it
  exists in the worktree of the materialized checkout (e.g. copied in by the
  harness), D1 never notices — `manifest_absent` only fires when the file is
  missing from disk, not from the commit.

Every other leg has the same worktree-read shape (D2 census `--file` reads the
worktree SOURCES.md), so this is a systemic hole, but D1 is the leg whose whole
claim is "committed."

## Exploit 3: EXCLUDE lines are pure commentary

`exclude.append(line)` accepts any line starting `EXCLUDE` — no required path
field, no reason grammar, no cross-check against the on-disk tree, and (necessarily)
no existence check since excluded paths are *not* committed. `EXCLUDE lol` passes.
The defect demands exclusions be "recorded with reasons" — a demand the manifest
format must carry and reviewers must audit; the counter contributes nothing here.

## §3 Excluded-scratch honesty — what's actually under .ufo/waves/round-66/

`find -type f` total: **18,589** (matches the routed defect's "~18.6k").
Of those, nested-repo internals: `.git` 7,241 + `.jj` 3,906 = **11,147 (60%)**.
Non-repo files: 11,348, of which the fixture copy `stage/mut-c/fx/` holds 6,170 —
another nested git repo, not evidence. Embedded repos on disk (each becomes a
gitlink if added; `cat-file -e` fails on them):

- `w1/mut-entry-scratch/` — full jj+git lane clone, 12,034 files (the bulk)
- `w1/scratch/lane/`, `w1/scratch/lane-o/` — two more lane clones (135 non-.git)
- `stage/mut-c/fx/` — repo fixture copy (6,170 non-.git)
- `stage/mut-o-counter/{root,roots/m1,m2,m3}/` — 4 materialized counter roots
- `stage/mut-reg/` presumably also embedded; `MutTool-scratch`, `RevEntryDraft-scratch` small

The honest **curated subset** (what the defect names: registry, seat reports, row
fragments, spec/mutant sources) ≈ **~240 files**:

| class | count | paths |
|---|---|---|
| seat reports | 63 | `w1/*.md` (zero empty files — verified `-size -50c`/` -empty`) |
| wave registry | 1 | `w1/swarm-registry.json` |
| row fragments | 36 | `rows/Scout*/row-S*.txt, rejects.txt, gap.md` |
| stage drafts | 11 | `stage/*.md, *.diff, *.txt` |
| mutant sources | ~64 | `stage/mut-c/*.py(8)`, `stage/mut-o/*.py(4)`, `stage/mut-reg/*(26)`, `w1/MutTool-scratch/{mutants,logs}/*(12)`, `w1/RevEntryDraft-scratch/*(2)`, `stage/mut-o-counter/{pristine,mut1..3,runs}/*` |
| wave spec | 4 | `gen-spec.py, spec-v2.json, taskcall-v2.json, run.stderr` |

An honest manifest therefore lists ~240 INCLUDEs and names ~8 exclusion classes
covering the remaining **~18,350 files (98.7%)**. The counter checks none of this:
a manifest listing only the 63 seat reports + 8 dup lines + `EXCLUDE scratch` is
indistinguishable to D1 from the honest one.

## Provenance caveat (a defect the counter cannot fix)

R66 evidence was never committed, so the committed-at-lands blob cannot be
anchored against a prior git state. Nothing prevents the integrator from
committing *edited* "r66" seat reports — `cat-file -e` cannot distinguish
original from rewritten bytes because there is no original commit to diff
against. The untracked disk tree is the only ground truth (RevDispositionsD1's
on-disk comparison covers presence, not byte-fidelity of each file). This is a
tradeoff the canonical judge should weigh: perfect fidelity is unbuyable now;
the fixable part is making the leg at least prove *committed, non-trivial,
deduplicated* evidence.

## Fixable defects vs tradeoffs

| # | defect | class |
|---|---|---|
| F1 | worktree `read()` of the manifest — never proven at lands | fixable: `git show lands:MANIFEST` or add `cat-file -e lands:MANIFEST` |
| F2 | no dedup → 8 dup lines pass seat count | fixable: `len(set(seat))` |
| F3 | no size floor → empty blob passes | fixable: `cat-file -s` > 0 (or ≥ N bytes) |
| F4 | tree paths pass `-e` | fixable: require `cat-file -t` == blob (or `-e <lands>:<p>^{blob}` — actually `cat-file -e rev:path` can't assert type; use `rev-parse <lands>:<p>` then `cat-file -t`, or `ls-tree` blob check) |
| F5 | includes unbounded in path class — any tracked file pads | fixable: require `^\.ufo/waves/round-66/` prefix on all includes |
| F6 | EXCLUDE grammar unchecked | partially fixable: require `EXCLUDE <path-prefix> reason=…` shape; honesty still needs a human manifest audit |
| T1 | committed bytes can't be proven byte-identical to r66 originals | tradeoff — inherent; mitigate by manifest committing `find`-generated path+sha256 pairs as a separate integrity file reviewers can re-run |

## Smallest safe correction

Keep the leg's shape; inside the `include` loop replace `cat-file -e` with
`git cat-file -s <lands>:<p>` requiring a positive size, dedup `seat` via `set()`,
prefix-bind includes to `.ufo/waves/round-66/`, and add one line:
`git cat-file -e <lands>:<MANIFEST>` (parses the committed manifest via
`git show <lands>:<MANIFEST>`, not the worktree copy). ~6 lines; rejects every
exploit above while preserving the curated-subset latitude the defect grants.

## Dependency noted

`reports/round-67/dispositions/r66-wave-evidence-manifest.txt` is absent — the
draft does not exist to attack byte-for-byte. All findings above attack the
frozen leg + any manifest expressible in its grammar; the concrete on-disk
exclusion accounting is provided so RevDispositionsD1 can diff the real manifest
against it.

## L1 sequencing note (post-draft)

L1 ruled the C-APPEND vs Ca-D4 id conflict satisfiable via per-claim lands:
C stamps at A_c (only S805-S828 + A_r's S801-S804 appended), Ca stamps at a later
A_ca carrying S829+ rejects and the dispositions tree. For D1 this means
`cat-file -e <lands>:<p>` binds at **A_ca** — the manifest and every INCLUDE must
be committed at the *later* commit, which is where the worktree-read exploit
(Exploit 2) bites: the parsed manifest need only exist in the A_ca checkout,
not in the A_ca commit. Sequencing changes nothing else in this report.
