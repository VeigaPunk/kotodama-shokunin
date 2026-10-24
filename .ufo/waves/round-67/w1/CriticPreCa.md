# CriticPreCa — pre-data attack on reports/round-67/accept-ca.py

Seat: `L1-kotodama-r67.CriticPreCa` · instrument: `reports/round-67/accept-ca.py` rev0 @ b78f8b8 (sha256 in dry-run-ca.txt) · scope: D2 file-path travel, D3 fabricability, D4 rejected-row quality, SEQ grep-vs-behavior. Read-only review; no repo mutation; no installs.

## Headline finding (cross-cutting, hits every leg)

**STAMP proves ref equality, not measured-byte identity.** `STAMP` = `git rev-parse main` == `--lands` (accept-ca.py:112-116). Nothing asserts `HEAD == main`, nothing asserts worktree cleanliness, and every file leg (`read(root, …)`) reads **worktree bytes**. `git rev-parse main` resolves the ref regardless of the checked-out state — the lane itself is at `(detached HEAD)` right now (`git worktree list`). A dirty clone, a clone HEAD-detached on a side commit, or **a symlinked file in the clone** all keep `main == lands` while legs measure non-lands bytes. `claims.json` receipt_protocol commands "materialized clone at the lands commit"; the counter never verifies it. This is the moved-worktree PASS class the protocol exists to kill — relocated, not fixed. D2 docstring even claims "the **lands-tree** corpus/SOURCES.md" while passing the census a **worktree** path.

## D2 — census --file travel and lands-tree claim

1. **Yes, a worktree registry ≠ lands registry passes.** `reg_path = os.path.join(root, REGISTRY)` (line 147) → `subprocess.run([CENSUS, "validate", "--file", reg_path])` (line 152). No `git show lands:corpus/SOURCES.md` anywhere; `git status --porcelain` never consulted. Overwrite `corpus/SOURCES.md` post-clone → E12/E11 verdict follows the dirty file. Same for the placement/S753 regexes — all worktree reads.
2. **Symlink bypass of the whole tree.** Census `--file` does `file_abs=$(realpath -- "$FILE")`, `dir_abs=$(realpath -- "$(dirname -- "$file_abs")/..")` (sources-census.sh:497-501); E11 then stats `$dir/$path` (line 567). If `corpus/SOURCES.md` in the clone is a symlink to the *fleet lane's* registry, every byte measured (E-codes, E11 used-by stats, placement) comes from **the lane worktree**, not the clone. `main == lands` still PASSes. One symlink converts the lands-time predicate into a tip-time re-derivation — exactly R66-D3's failure class inside the counter written to fix it.
3. **The validation oracle is outside the measured tree.** `CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"` (line 54) is a host-absolute fleet path — not `root`'s copy, not sha-pinned (only `__file__` is hashed, line 92). Edit `scripts/sources-census.sh` mid-round → every future receipt grades against a different oracle with an identical counter sha. (Defensible as "frozen oracle", but provenance is false: the receipt cannot distinguish which script ran.) Also makes the counter un-runnable on hosts without that absolute path — contradicts portability of the cloned-eval story.
4. **Duplicate authority / identity drift on section bounds.** Counter placement uses `re.finditer(r"(?m)^##\s+\S.*$", reg)` — column-0 only, substring `"Registry"`/`"Leads"`, *first* match wins (lines 158-162). Census E12 uses `^ {0,3}##[ ]` and exact `== "Registry"` (sources-census.sh:540,547,611). Divergences: a column-0 `## Registry notes` heading before `## Registry` shifts `reg_pos` for the counter only (rows between them FAIL the counter but pass census — false FAIL); rows inside ``` fenced blocks count as "outside Registry" for the counter while the census's line parser likely counts them in-section — false-FAIL noise, not exploitable, but the counter has cloned the section logic instead of asking the census (which already reports E12 per-row).
5. `cat-file -e <lands>:<p>` accepts **tree paths** — verified: `git cat-file -e HEAD:corpus` → exit 0. An `INCLUDE corpus` line counts as "tracked" (weak but benign since it only inflates includes, not seats).
6. Minor: seat-report count `len(seat)` counts *lines*; the same `INCLUDE .ufo/waves/round-66/w1/x.md` repeated 8× satisfies `>=8 seat reports` with one real report (D1, but same class).

## D3 — shape vs content (confirmed fabricable)

Simulated the regexes verbatim: a **two-line** ledger passes D3 —

```
LOG.md       : "# Round 66\n"
SCORECARD.md : "### Axes — round 66\ncoverage operability calibration round 66\n"
```

`bad=[]` → `D3 PASS`. The leg cannot distinguish restored round-66 ledger content from a two-line stub: no row count, no verdict, no lands/stamped values, no coupling to the actual r66 receipt content. **LOG/SCORECARD restoration is shape-only and fabricable.** Friction note (opposite direction): `axes\s*—\s*round` pins the em-dash literally (line ~187) — a builder's honest `Axes - round 66` table FAILs (typo-attractor, false FAIL). Cell miscount: `line.split("|")` treats `|` inside teaches text as a delimiter → `len(c)!=11` skips the row for status/teaches checks, though census E01 saves it.

## D4 — garbage teaches pass (confirmed)

- For the **>=2 new round-67 rejects**: only `status == rejected and opened == 2026-10-24` is checked (line ~228); **teaches is not inspected at all** — the census's W02 "thin teaches" is a warning that never changes exit (sources-census.sh:32). Two rejected rows with `teaches = t` pass.
- For **S801-S804**: status `== "rejected"` and teaches contains substrings `REJECTED:` + `flip:` (lines ~220-226). `| S801 | … | REJECTED: z flip: q | rejected | 2026-10-24 | … |` passes — garbage teaches confirmed pass.
- Arithmetic note (corrected after L1 sequencing ruling): `rej_opened_today >= len(R66_REJECTS)+2` = ≥6 counts S801-S804 toward the total. Consistent with the frozen claim **only because** S801-S804 are new rows opened this round — a restoration carrying earlier opened dates would FAIL. Dead code: `new_rejects` computed (lines ~233-235) and never used — the intended "2 **new**" semantics was written then dropped. Ambiguity residue: the leg cannot distinguish "2 new gate rejects" from other today-opened rejects (e.g. an S805-class row flipped to rejected) — C's APPEND bound (NEW_IDS∪EXTRA_IDS, accept-c.py:357) is what actually confines the id set.
- Cross-counter sequencing dependency (design finding; L1-resolved, no revision): any S829+ reject row in C's lands tree prints APPEND FAIL (`extra=[...]`). The joint predicate is satisfiable **only** under per-claim lands separation: C's receipt at A_c (before reject rows land), Ca's receipt at later A_ca carrying S829+. Correct counters, but the ordering is load-bearing and claims.json's `receipt_protocol` does not name it — running C's counter at A_ca, or a single shared lands commit for C+Ca, is unsatisfiable.
- `once` uniqueness and `rej_opened_today` scan the **whole file**, including `## Leads` and fenced blocks — Leads-section rejected rows inflate the count (E12 backstops it via census exit≠0, but only because census runs on the same possibly-symlinked file).

## SEQ — greps are source-text, not behavior (spoofable)

- Three greps: `--lands` + `required=True` anywhere; `stamped revision` + `evaluated revision` anywhere; `mv_rev == lands` (with `mv_rev==lands` normalized, line ~247-256). **Simulation: a counter whose only content is comments passes all three** —
  `# --lands required=True / # stamped revision evaluated revision / # mv_rev == lands` → `bad=[]`. `required=True` needn't bind `--lands` (any other required arg satisfies it); nothing runs the counter without `--lands` to observe exit-2; nothing greps the `add_argument("--lands"` *line*; the equality grep doesn't check it's *enforced* (`if not stamp_ok` gate could be absent — but note STAMP itself is an early-return leg, so an un-gated assert still gates via `legs`... the equality *string* is the check, and a comment supplies it).
- **Provenance split**: SEQ reads counter sources as `root`-relative **worktree** files, while `self_sha` hashes `__file__` — the *executing* copy. `--root` ≠ counter location → receipt pins lane bytes, legs grade clone bytes. And all three greps read worktree copies: mutate the clone's `accept-c.py` post-clone and SEQ grades the mutant.
- The one behavioral leg, `check-receipt-seq.py --selftest`, runs the **worktree** copy at `--root` (relative `SEQ_TOOL`, `cwd=root`) — same lands-vs-worktree hole, and its pass token is the string `"14/14"` in stdout, which any passed argv file could print (mitigated only because argv is fixed).

## Impacted axes

Calibration (Ca claim itself — all five records legs are worktree/shape checks on a claim whose whole point is lands-time durable evidence), operability (SEQ greps certify the *protocol's* presence, not enforcement — a counter can wave a receipt protocol it doesn't run). The claim's `lands` list names corpus/SOURCES.md, LOG.md, SCORECARD.md — the three files with the weakest lands binding. Sequencing dependency above additionally couples C's APPEND to Ca's D4 across lands commits.

## Smallest safe corrections

1. Bind files to lands: replace `read(root, path)` for D2/D3/D4/SEQ/CRITERION/QUOTES inputs with `git show {lands}:{path}` (or assert `git status --porcelain` empty **and** `HEAD == lands` and resolve all `read` targets through realpath-inside-root). One-line class fix: `text = git_show(lands, path)`.
2. Census: pin the oracle (`sha256sum` of CENSUS printed into the receipt) and invoke against bytes extracted from lands, or keep `--file` but reject symlinked `reg_path` (`os.path.realpath(reg_path)` must stay under `os.path.realpath(root)`).
3. D3: require ≥N non-empty lines + at least one verdict-bearing line per axis row (regex the actual r66 table cells), not heading-shaped strings.
4. D4: require `REJECTED:`+`flip:` (or ≥K chars) teaches for the new rejects too; use the already-computed `new_rejects` to assert the *new* class explicitly (`rejected ∧ opened==2026-10-24 ∧ id∉{S801..S804}` ≥2) so the leg can't be satisfied by unrelated today-dated rejects.
5. SEQ: grep the `add_argument` *line* for `--lands` + `required=True` jointly, or — stronger — run each counter without `--lands` and require exit 2.

Report: .ufo/waves/round-67/w1/CriticPreCa.md
