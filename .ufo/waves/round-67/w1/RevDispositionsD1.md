# RevDispositionsD1 — R66-D1 disposition manifest, independent verification

Seat: `L1-kotodama-r67.RevDispositionsD1` (reviewer, leaf). Repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `ad5b52b0`, lane tip at review `b78f8b8` (declaration commit). Read-only: no git/jj writes, no lane mutation.

**Verdict: INCLUDE HALF PASSES; EXCLUSION HALF PARTIALLY — 37 files uncovered by machine-read classes.**
The manifest appeared late in the time-box (`reports/round-67/dispositions/r66-wave-evidence-manifest.txt`,
221 lines, written after my blocker report to L1; it was absent at start, mid-review and at the first end-poll).
Verified against the written artifact:

- **194 INCLUDE lines = 9,950,616 B**, and the set is **byte-for-byte identical** to the curated set I derived
  independently from `find` before the manifest existed (`manifest-only=[]`, `mine-only=[]`). 63 seat reports,
  36 row fragments, spec triple, 11 stage drafts, 3 `_readme-build`, 4 `mut-o`, 26 `mut-reg`, 7 `mut-c`,
  40 `mut-o-counter`. Every INCLUDE exists, is non-empty, is inside `.ufo/waves/round-66/`, is not inside any
  scratch segment and has no clone ancestor (`.git`/`.jj`) — **0 bad, 0 duplicate**.
- **EXCLUDE: 7 lines, 18,358 files covered, 37 files uncovered** (16 `mut-o-counter/runs/*.err`, 18
  `mut-o-counter/roots/**`, 2 `w1/RevEntryDraft-scratch`, 1 `stage/mut-c/err.txt`). The manifest's header claims
  "excluded classes below cover the residual 18,395 files"; as written they cover 18,358. Three causes, all
  mechanical: two lines bundle two classes each (`root/ and roots/`, `MutTool-scratch/ and RevEntryDraft-scratch/`),
  the zero-byte class is stated in prose with no path token (first token is the word `zero-byte` → matches 0 files),
  and trailing `/` on the bundled prefixes. Detail in **M4**.
- Not committed: manifest and payload are `??` untracked at tip `b78f8b8`, so leg D1 fails at any current lands
  (`cat-file -e`); expected pre-lands, fixed by the A_r commit (M1).

`accept-ca.py` leg D1 (`:55,122-153`) and claim Ca's `lands` array (`claims.json:95`) require this file. Note
that **no seat in `spec-v2.json`/`taskcall-v2.json` authors it** — only readers (CriticD1Manifest,
CriticR66Dispositions, this seat); it materialised without a designated producer. Reported to L1 as a blocker
during the seat.

The remainder of this report is the independent audit: class-level ground truth (18,589 files, §2), the named
exclusions and what they really remove (§3, §6b), coverage by class (§4), the validated checker and its control
matrix (§5), and residual risk (§7).

---

## 1. Findings (severity order)

### B1 — was BLOCKER at mid-review, now RESOLVED LATE: no designated authoring seat; the artifact materialised unowned
- At mid-review `reports/round-67/dispositions/` did not exist and D1 failed closed (`manifest_absent`,
  `accept-ca.py:129-131`), making Ca undischargeable. The manifest exists as of the final poll.
- Root cause is structural and still worth fixing next round: `gen-spec.py`/`spec-v2.json` mention the path only
  inside the three *reading* prompts (`gen-spec.py:160,163`; `spec-v2.json:373,400`; this seat's prompt). None of
  the 64 seats authors it, so the single artifact that carries R66-D1 had **no producer and no acceptance owner**;
  it landed only because L1 wrote it after a blocker report. That is the same failure shape as R66-D1 itself —
  a disposition that depends on an unassigned artifact.
- Still open at tip: manifest and payload are untracked (`?? .ufo/waves/round-66/`,
  `?? reports/round-67/dispositions/…` is inside the untracked `reports/round-67` tree region), so D1 cannot pass
  until the A_r commit lands them together (M1).

### H1 — HIGH: 18 non-empty-looking evidence files are 0 bytes; presence-only `cat-file -e` passes them
`accept-ca.py:143` checks `git cat-file -e <lands>:<path>` — **presence at lands, not content**. Measured on disk,
outside the clone/scratch classes:

| 0-byte file | class | would pass `cat-file -e` |
|---|---|---|
| `.ufo/waves/round-66/run.stderr` | spec capture | yes (tracked once committed) |
| `.ufo/waves/round-66/stage/mut-c/err.txt` | mut-C run stderr | yes |
| `.ufo/waves/round-66/stage/mut-o-counter/runs/*.err` ×16 | counter-run stderr | yes |

A manifest that INCLUDEs a whole stage subtree (`stage/mut-o-counter`, `stage/mut-c`) silently imports these
18 empties; the spot-check's demanded durability ("D3's seat-file predicate is undurable without it") is about
**content**, so an empty-by-construction file must be EXCLUDEd *with a reason*, not INCLUDEed as evidence.
(89 zero-byte files exist in the wave tree overall; 71 are inside clone/scratch trees.)
**Against the written manifest:** clean — 0 zero-byte members among the 194 includes, and all 17 non-scratch empties
are named as excluded (2 in machine-readable class lines, 15 only in the prose clause, see M4). This is correct
behaviour by construction (per-file INCLUDEs); the counter would not have caught the opposite choice.

### H2 — HIGH: 18,235 of 18,589 files (98.08%) sit inside clone/scratch trees; committing them is not merely unwise, it fails or leaks
Measured `git`/`.jj` evidence:
- `.ufo/waves/round-66/w1/mut-entry-scratch/.git` — a lane clone **with worktree refs for other lanes**:
  `hayku/s3-kotodama-r51-author`, `hayku/s3-ready66-kotodama` (i.e. `refs/heads/hyaku/s3-kotodama-r51-author`,
  `refs/heads/hyaku/s3-ready66-kotodama` under `.git/worktrees/*/HEAD`). Committing it embeds foreign lane
  refs and a 97.58 MB tree.
- `.ufo/waves/round-66/stage/mut-c/fx/.git/config` — `remote "origin" url = /home/vgpnk/Projects/shokunin/kotodama-shokunin`:
  an absolute host path embedded in a committed `.git`.
- 7,245 `.git` files total; `.jj` dirs present under `w1/mut-entry-scratch/.jj`.
- Recursion: 9 nested `round-66` directories exist inside the r66 tree (50 files under a second
  `round-66/` segment) — `w1/scratch/lane/.ufo/waves/round-66`, `w1/scratch/lane-o/.ufo/waves/round-66`,
  `stage/mut-o-counter/{root,roots/m1..m3}/.ufo/waves/round-66`. A "commit everything" disposition doubles
  the wave into itself and re-inflates every following round.
- Inner-clone worktrees in the candidate include set: none. Verified by ancestor scan (any ancestor holding
  `.git`/`.jj` disqualifies) — control G in §7 fires on `stage/mut-o-counter/root/tools/...`.

### H3 — HIGH: manifest grammar must be literal file paths, and `EXCLUDE` is textually unenforced
- D1 expands every `INCLUDE` token into `git cat-file -e <lands>:<token>` (`accept-ca.py:141-145`). A glob,
  prefix, or directory INCLUDE therefore FAILS the leg as untracked — fail-closed, which is correct, but it
  also means the manifest must enumerate literal paths (194 lines for the curated set in §4), not "w1/*.md".
- The exclusion half is weaker: `accept-ca.py:137` accepts *any* line starting `EXCLUDE `, and
  `accept-ca.py:152-153` only requires `exclude` to be non-empty. `EXCLUDE scratch stuff` would print PASS
  with no path, no reason and no coverage. Only an external audit (mine, §5) makes exclusions honest.

### M1 — MEDIUM: commit-ordering constraint; a "manifest committed after the payload" plan fails at lands
D1 evaluates `cat-file -e <lands>:<manifest path>` **and** `cat-file -e <lands>:<every payload path>`.
Therefore manifest and payload must be reachable from the *same* lands revision:
payload commit first + manifest commit second is fine only if `--lands` is the **manifest** commit; if
`--lands` is the payload commit, `cat-file -e lands:manifest` fails. Manifest-then-payload is impossible.
And the counter must still run only inside the materialized clone at lands (`STAMP` equality,
`accept-ca.py:105-120`) — a moved worktree PASS claim is exactly the class r66 punished.

**Refined under L1's per-claim lands sequencing (A_r → A_c → A_ca):** Ca's `--lands` is **A_ca**, so
`cat-file -e A_ca:<manifest>` and `cat-file -e A_ca:<payload>` both resolve through ancestry. The safe
placement is therefore the r66-disposition commit **A_r** (payload + manifest together, before A_c), never a
commit after A_ca; putting the payload only at A_ca also works but then the manifest's own commit must be A_ca
too (one commit, or A_ca tolerates nothing later). What still fails: manifest at A_ca with payload left
uncommitted, or any plan where the counter's evaluated revision is a moved worktree tip rather than the
receipt's `--lands`.

### M2 — MEDIUM: the frozen D1 leg does not require any of the classes the spot-check named
`accept-ca.py:139-150` requires: ≥8 files matching `\.ufo/waves/round-66/w1/[^/]+\.md$`, plus ≥1 any-include,
plus ≥1 EXCLUDE line. A manifest of 8 seat reports and nothing else — no `rows/`, no `swarm-registry.json`,
no spec — prints D1 PASS. The spot-check's demanded subset is literally "(registry, seat reports, row
fragments)". The counter under-specifies its own claim; my §4/§5 audit is the only place the named classes
are actually enforced. Recommend (post-freeze, next round) widening D1 to require `rows/**` ≥1,
`swarm-registry.json`, and the spec triple.

### M3 — MEDIUM: size/labelling — 82% of the honest payload is one mutant fixture class
Curated include set = 9,950,616 bytes, of which `stage/mut-reg` is 8.16 MB (26 files: `SOURCES.pristine.md`,
8 mutant `*.SOURCES.md`, 8 verdict `*.txt`, `run.sh`/`run-all.txt`/`restored-baseline.txt`). That is mutant
*fixture* evidence, not wave *source* evidence. It may be included, but the manifest must label it as such;
presenting it as part of "seat reports + row fragments + spec" would inflate the durable-evidence claim by 8 MB
with files that carry no r66 S-row value. The narrow honest core is ~1.7 MB:
seat reports 0.61 MB + rows 0.06 MB + spec 0.40 MB + registry 0.013 MB + stage drafts 0.34 MB + mut-o 0.28 MB.

### M4 — MEDIUM: exclusion accounting is prose, not classes — 37 of 18,395 excluded files are machine-invisible
The written manifest's header claims "excluded classes below cover the residual 18,395 files". Parsed literally
(one path token per `EXCLUDE` line, the grammar `accept-ca.py:137` tolerates), the 7 lines cover **18,358**, and
these stay uncovered:

| uncovered | count | why |
|---|---:|---|
| `stage/mut-o-counter/runs/*.err` | 16 | named only in prose ("zero-byte artifacts inside included dirs - 16 files (…mut-o-counter/runs/*.err)"); the line's first token is the word `zero-byte`, which matches 0 files |
| `stage/mut-o-counter/roots/**` | 18 | the line reads `root/ and roots/ - 40 files`; only `root/` (6 files) is a path token — and the stated "40" is also wrong (6 + 18 = 24) |
| `w1/RevEntryDraft-scratch` | 2 | bundled as `w1/MutTool-scratch/ and w1/RevEntryDraft-scratch/ - 14 files`; only the first is a path token, count 12 ≠ 14 |
| `stage/mut-c/err.txt` | 1 | prose only |

Net: residual by class = **37** (16+18+2+1), not 0. Nothing dangerous is excluded by omission — all 37 are clone
sub-trees or empty stderr, and each is *named* somewhere in the file — but the disposition is not auditable
without reading English, and two of its own counts (40, 14) do not match the tree. Two cheap fixes: one
`EXCLUDE path=… reason=…` per class (10 lines, the arithmetic closes at 0), and drop or correct the bundled counts.
This matters beyond bookkeeping: `accept-ca.py:152-153` accepts *any* non-empty `EXCLUDE` text, so a future round
can pass D1 with a single prose line and no classes at all.

### L1 — LOW: registry roster is 64, seat reports are 63; the manifest should disclose it
`w1/swarm-registry.json` (13,410 B, `schema ufo-swarm-registry-v1`, wave `kotodama-r66-v2`) has **64 members**;
`w1/*.md` is **63** files, and every one of the 63 maps to a member. `ScoutRow01` is a member with no report file
(its work surfaced as `rows/ScoutRow02/*`). Not a manifest defect, but "63 seat reports" must not be silently
presented as "the whole roster durable".

### L2 — LOW: no LSP server path available for this review
No `lsp` device is mounted in this seat (`xd://lsp` → "No such tool … Mounted devices: ast_edit, debug"), and the
workload is data/record verification, not symbol resolution. All evidence below is `git`/`find`/byte-level and is
labelled as such; no semantic-proof claim is made from text search.

---

## 2. On-disk ground truth (the comparison basis)

`find .ufo/waves/round-66 -type f` → **18,589 files, 243.46 MB**, 0 symlinks, 7,245 `.git` files,
89 zero-byte files (71 inside clones).

| class | files | MB | 0-byte |
|---|---:|---:|---:|
| `w1/mut-entry-scratch` (lane clone + worktrees) | 12,034 | 97.58 | 20 |
| `stage/mut-c` (mutant C fixture; `fx/` is a lane clone) | 6,178 | 133.84 | 1 |
| `w1/scratch` (lane + lane-o clones) | 135 | 0.48 | 8 |
| `stage/mut-o-counter` (4 roots + 4 mutant counters + 52 run artifacts) | 80 | 1.45 | 16 |
| `w1/` root (63 seat `.md` + `swarm-registry.json`) | 64 | 0.61 | 0 |
| `rows/` (12 ScoutRow dirs: rows + rejects) | 36 | 0.06 | 0 |
| `stage/mut-reg` (registry-gate mutants) | 26 | 8.16 | 0 |
| `w1/MutTool-scratch` | 12 | 0.30 | 0 |
| `stage/mut-o` (4 accept-o mutants) | 4 | 0.28 | 0 |
| `stage/_readme-build` (README.orig/new + diff) | 3 | 0.34 | 0 |
| `w1/RevEntryDraft-scratch` | 2 | 0.01 | 0 |
| spec root (`gen-spec.py`, `spec-v2.json`, `taskcall-v2.json`, `run.stderr`) | 4 | 0.40 | 1 |
| `stage/` draft reports (`gate-rows`, `lesson-draft`, `entry-spec`, `s776-gate`, `readme-plan.{md,diff}`, `execcountersmoke{c,o,ca}.md`, `separability-real-probe.txt`, `evidence/accept-c-base-run.txt`) | 11 | 0.16 | 0 |

## 3. What must stay out, and why (named exclusion classes)

| # | exclusion class | files removed | reason (verified, not asserted) |
|---|---|---:|---|
| E1 | `w1/scratch` | 135 | two git clones (`lane`, `lane-o`), nested `round-66` copies, `.git` present |
| E2 | `w1/mut-entry-scratch` | 12,034 | lane clone with `.git` **worktrees for other lanes** (`hyaku/s3-kotodama-r51-author`, `hyaku/s3-ready66-kotodama`), `.jj`, 97.58 MB |
| E3 | `w1/MutTool-scratch` | 12 | mutant scratch trees (`mutants/pristine.py`, probe scripts) |
| E4 | `w1/RevEntryDraft-scratch` | 2 | scratch audit scripts (`audit.py`, `restate.py`) |
| E5 | `stage/mut-c/fx` | 6,170 | lane fixture clone: own `.git`, `remote.origin.url=/home/vgpnk/Projects/shokunin/kotodama-shokunin`, 133.84 MB |
| E6 | `stage/mut-o-counter/root` | 6 | clone root (`.git` gitfile) holding a nested `round-66` copy |
| E7 | `stage/mut-o-counter/roots` | 18 | clone roots `m1..m3`, each with `.git` + nested `round-66` copy |
| E8 | `stage/mut-o-counter/runs/*.err` (glob) | 16 | stderr empty-by-construction (all 0 bytes); the `.out`/`.rc` files in the same dir stay in |
| E9 | `run.stderr` | 1 | 0 bytes at capture |
| E10 | `stage/mut-c/err.txt` | 1 | 0 bytes at capture |

Sum with the 194 includes: 194 + 18,395 = **18,589**, residual **0 unaccounted**. Excluded share 98.96%.
Classes E1–E7 are also *structurally required* exclusions: git cannot represent a nested repository as plain
files without a gitlink (`fx/.git`, `root/.git`) and would embed absolute host paths; E8–E10 are required by the
non-empty rule.

**Written manifest vs this table:** it names E1, E2, E5, E6 (as `root/`), E3 and E9 and the prose idea of E8/E10 —
in **7 lines**, bundling E3+E4 and E6+E7, and covering E8/E10 only in prose. Measured coverage of its parsed
classes: 18,358 / 18,395, leaving 37 uncovered (E7 18, E8 16, E4 2, E10 1) — see **M4**. The table above is the
correct closure; the delta is bookkeeping, not a leak (all 37 files are clone sub-trees or empty stderr).

Concrete members of each class (first entries as `find` returns them):

- E1 `.ufo/waves/round-66/w1/scratch/out-c.txt`, `…/scratch/lane/.git/config`, `…/scratch/lane-o/README.md`
- E2 `.ufo/waves/round-66/w1/mut-entry-scratch/.gitignore`, `…/mut-entry-scratch/AGENTS.md`, `…/.git/worktrees/kotodama-shokunin/HEAD`
- E3 `.ufo/waves/round-66/w1/MutTool-scratch/probe_unresolved_order.py`, `…/MutTool-scratch/mutants/mut1_default_timeout.py`
- E4 `.ufo/waves/round-66/w1/RevEntryDraft-scratch/audit.py`, `…/restate.py`
- E5 `.ufo/waves/round-66/stage/mut-c/fx/.gitignore`, `…/fx/AGENTS.md`, `…/fx/corpus/knowledge/…` (the whole lane fixture)
- E6 `.ufo/waves/round-66/stage/mut-o-counter/root/.git`, `…/root/tools/check-claim-separability.py`
- E7 `.ufo/waves/round-66/stage/mut-o-counter/roots/m1/.git`, `…/roots/m3/tools/check-claim-separability.py`
- E8 `.ufo/waves/round-66/stage/mut-o-counter/runs/pristine.err`, `…/runs/world-m2-mut2_bound_9999.err`
- E9 `.ufo/waves/round-66/run.stderr` (0 B)
- E10 `.ufo/waves/round-66/stage/mut-c/err.txt` (0 B)

## 4. Coverage % by file class (written manifest vs `find`)

The written manifest carries **194 literal INCLUDE paths, 9,950,616 B (9.95 MB), 1.04% of files** — the same set,
same bytes, as the curated set I derived from `find` before the manifest existed (`manifest-only=[]`, `mine-only=[]`,
both directions empty). Verified per path: 0 absent, 0 zero-byte, 0 directories, 0 outside `.ufo/waves/round-66/`,
0 inside a scratch segment, 0 with a `.git`/`.jj` clone ancestor, 0 duplicates; and `git check-ignore --stdin` over
all 194 returns nothing (`.gitignore` holds `*.log`, `__pycache__/`, `.ufo/state/`, `.ufo/watchdog.log`, `.scratch/`,
none of which touches the set). 63 of them match the D1 seat regex `\.ufo/waves/round-66/w1/[^/]+\.md$` (≥8 required).

| class | coverage |
|---|---|
| `w1/` seat reports + registry | **64/64 = 100%** (63 `.md` — every seat md — + `swarm-registry.json`) |
| `rows/` fragments | **36/36 = 100%** |
| spec root | **3/4 = 75%** (`run.stderr` excluded as 0-byte; `gen-spec.py`, `spec-v2.json`, `taskcall-v2.json` in) |
| `stage/` draft reports | **11/11 = 100%** |
| `stage/_readme-build` | **3/3 = 100%** |
| `stage/mut-o` | **4/4 = 100%** |
| `stage/mut-reg` | **26/26 = 100%** (fixture class — see M3) |
| `stage/mut-c` | **7/6,178 = 0.11%** (the 7 non-empty mutant sources + `results.json`; `fx/` and `err.txt` out by design) |
| `stage/mut-o-counter` | **40/80 = 50%** (4 mutant counters + 36 `.out`/`.rc`/`.ms`; 24 clone files + 16 empty `.err` out) |
| `w1/*-scratch`, `w1/scratch`, **all `.git`** | **0% — intentional** |

Evidentiary coverage — the classes the spot-check names (registry, seat reports, row fragments) — is **100%**;
overall file coverage is **1.04%**, and every excluded byte is named in §3 with a reason. That is the honest shape
of the "curated subset … and say so" the spot-check allows.

## 5./6. Checker and control matrix (ready for the written manifest)

Run this against the real manifest when it exists; it implements every clause of my assignment (exists,
non-empty, not inside scratch/`.git`/clone, exclusion classes actually exclude, residual, coverage):

```python
import os, re, fnmatch, subprocess, sys
REPO = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
SUBJECT = ".ufo/waves/round-66"
SCRATCH = re.compile(r"(^|/)[^/]*scratch[^/]*(/|$)")
def clone_ancestor(rel):
    parts = rel.split('/')[:-1]
    for i in range(1, len(parts) + 1):
        d = os.path.join(REPO, *parts[:i])
        if os.path.exists(os.path.join(d, '.git')) or os.path.exists(os.path.join(d, '.jj')):
            return '/'.join(parts[:i])
def excluded(p, exc):
    for e in exc:
        if p == e or p.startswith(e.rstrip('/') + '/'): return True
        if '*' in e and fnmatch.fnmatch(p, e): return True
    return False
def check(text):
    inc, exc, bad, dup, seen = [], [], [], [], set()
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith('#'): continue
        m = re.match(r"^INCLUDE\s+(\S+)", line)
        if m:
            p = m.group(1); inc.append(p)
            if p in seen: dup.append(p)
            seen.add(p)
            ap = os.path.join(REPO, p)
            if not p.startswith(SUBJECT + "/"): bad.append(("outside_subject", p))
            if os.path.isdir(ap): bad.append(("is_dir", p)); continue
            if not os.path.isfile(ap): bad.append(("absent", p)); continue
            if os.path.getsize(ap) == 0: bad.append(("empty", p))
            if SCRATCH.search(p): bad.append(("scratch_seg", p))
            ca = clone_ancestor(p)
            if ca: bad.append(("clone_tree:" + ca, p))
            continue
        if line.startswith("EXCLUDE"):
            body = line[len("EXCLUDE"):].strip()
            t = re.match(r"(path|glob|prefix)=(\S+)", body)
            if t: exc.append(t.group(2))
            elif body.split(): exc.append(body.split()[0])
            else: bad.append(("exclude_no_class", line))
            continue
        bad.append(("unparsed", line))
    allf = [os.path.relpath(os.path.join(dp, f), REPO)
            for dp, _, fn in os.walk(os.path.join(REPO, SUBJECT)) for f in fn]
    unacc = [p for p in allf if p not in set(inc) and not excluded(p, exc)]
    cov = {e: sum(1 for p in allf if p == e or p.startswith(e.rstrip('/') + '/')
                  or ('*' in e and fnmatch.fnmatch(p, e))) for e in exc}
    seats = [p for p in inc if re.match(r"\.ufo/waves/round-66/w1/[^/]+\.md$", p)]
    print("includes", len(inc), "seats", len(seats), "exclusion_classes", len(exc),
          "bad", len(bad), bad[:6], "dup", dup[:4],
          "unaccounted", len(unacc), unacc[:4],
          "swallow", [p for p in inc if excluded(p, exc)][:4])
    print("per-class removed:", cov)
    print("total", len(allf), "include_bytes", sum(os.path.getsize(os.path.join(REPO, p)) for p in inc))
    return not bad and not dup and not unacc and len(seats) >= 8
if __name__ == "__main__":
    sys.exit(0 if check(open(sys.argv[1], encoding="utf-8").read()) else 1)
```

Control matrix — all ten fired correctly (run in-memory; no files written):

| control | expected class | result |
|---|---|---|
| A `INCLUDE w1/scratch/lane/corpus/SOURCES.md` | scratch + clone | `scratch_seg`, `clone_tree:.ufo/waves/round-66/w1/scratch/lane` |
| B `INCLUDE run.stderr` | empty | `empty` |
| C `INCLUDE w1/NoSuchSeat.md` | absent | `absent` |
| D `INCLUDE corpus/lessons/round-66.md` | inflation outside subject | `outside_subject` |
| E `INCLUDE rows/ScoutRow02` (dir) | not a file | `is_dir` |
| F duplicate INCLUDE | duplicate | `dup=1` |
| G `INCLUDE stage/mut-o-counter/root/tools/…py` | clone tree | `clone_tree:…/mut-o-counter/root` |
| H `EXCLUDE glob=…/w1/*.md` | exclusion swallowing includes | `swallow=4` |
| I `SHIP-IT everything` | unparsed line | `unparsed` |
| J no EXCLUDE lines at all | residual honesty | `unaccounted=18,395/18,589` |

## 6b. Adjacent context (not this seat's slice, verified only to the extent it affects D1 ordering)

Five seats flagged a C-APPEND vs Ca-D4 id conflict; L1 resolved it by per-claim lands sequencing
(A_r → A_c → A_ca, no counter/claims revision). I checked the mechanism, because the D1 manifest's commit point
depends on it:

- `accept-c.py:67,70` — `NEW_IDS = S805..S828`, `EXTRA_IDS = {S801..S804}`; `:357-358` bounds appends to their
  union (`extra_ids`); `:372-373` fails APPEND on any id outside it.
- `accept-c.py` ROWS leg — every S805-S828 row must carry `status == "mined"`, tier A/B, and `used-by` the entry;
  ONEID additionally rejects any citation outside that set. So a **rejected** row cannot borrow an S805-S828 id.
- `accept-ca.py:207-239` — D4 counts rows with `status == "rejected"` **and** opened `2026-10-24`, requiring
  `>= len(R66_REJECTS) + 2` = 6 (`:235-236`). `new_rejects` (`:232`) is computed and never used — dead variable.
- Consequence: at any single tip, S829+ fails C's APPEND and an S805-S828 reject fails C's ROWS, so the joint
  predicate is satisfiable **only** as sequenced receipts, exactly as L1 ruled. S801-S804 exist only as
  `rows/ScoutReject{01..04}/row-S80{1..4}.txt` fragments (registry hits: 0) and carry 2026-10-24 verify dates,
  so they count toward the 6 and Ca needs only 2 further today-dated rejects.
- **For D1:** none of this changes the manifest content; it fixes the placement — manifest + 194-file payload at
  A_r, since Ca's receipt is evaluated at A_ca (see M1 refinement).

## 7. Residual risk and verification gaps

- **Content durability beyond "non-empty" is not enforced by the frozen D1 leg.** A 1-byte file passes both
  `cat-file -e` and my non-empty rule. Nothing in the wave pins seat-report *content* (e.g. a hash manifest of the
  63 seat reports); R66-D1 demanded durability of the evidence, and "presence + non-zero" is the strongest thing on
  offer this round. The current bundle is honest but shows the limit: its smallest member is a **2-byte**
  `stage/mut-o-counter/runs/mut1_always_true.rc` (a recorded exit code — meaningful, yet indistinguishable from
  noise to a presence-only gate), and the smallest seat report is 651 B. That is a property of how L1 wrote it, not
  of the counter.
- **Excluded classes are audited by prefix overlap, not by git's index.** Before lands, `cat-file -e` truth is
  unknowable; after lands the only proof is the counter run inside the materialized clone (M1).
- **Registry vs seats:** 64 members / 63 reports (`ScoutRow01` has no `.md`); the durable set cannot reproduce that
  seat's output, so "63 of 64" is the honest ceiling — the manifest does not state it.
- **Exclusion accounting is prose, not classes (M4):** 37 of 18,395 files are uncovered by any machine-readable
  EXCLUDE token, and two bundled counts (40, 14) do not match the tree (24, 14). Harmless today (clone sub-trees and
  empty stderr), unauditable tomorrow — and a prose EXCLUDE passes `accept-ca` D1 regardless.
- **Roll-up:** R66-D1 is now **substantively dispositioned, with a bookkeeping gap**. The include half is exact and
  independently corroborated (194/9,950,616 B, identical to a pre-manifest derivation, 0 bad/0 dup/0 ignored); the
  exclusion half closes at 18,358/18,395 and needs 10 single-class EXCLUDE lines to close at 0. It is **not yet
  committed** — the disposition only becomes durable at the A_r commit, which must carry manifest + payload together
  (M1) and precede Ca's lands A_ca. Residual failure modes if committed as-is: none observed for evidence integrity;
  the open risk is that D1's presence-only, class-blind legs let the *next* round regress to a weaker manifest (M2, M4).

Report: .ufo/waves/round-67/w1/RevDispositionsD1.md
