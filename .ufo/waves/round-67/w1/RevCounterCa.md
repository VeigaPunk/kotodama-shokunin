# RevCounterCa — review of `reports/round-67/accept-ca.py` (claim Ca, rev 0)

Scope: line-by-line review of the frozen Ca counter and the four assigned attack questions, plus
the receipt-discipline invariants the Ca claim asserts (committed-bytes evaluation, stamped ==
evaluated == measured, post-records carrier-parentage). Read-only: no lane git/jj writes, no edits.
Verification method: text-level. **No `lsp` device is available in this seat's tool inventory**
(only read/bash/grep/glob/edit/write/eval), so caller/definition checks were done by reading the
three counters and the tool, and by executing the census and `check-receipt-seq.py --selftest`
against the live tree. Tools installed: none.

Revisions seen: first pass reviewed the committed blob (`main:reports/round-67/accept-ca.py`,
sha256 `5e8915ac…`, the bytes pinned by `dry-run-ca.txt`/`controls-ca.txt`). Mid-review the L1
applied a one-line QUOTES fix in the worktree (sha256 `5382ffed…`, `git status` = ` M`); the
post-review section below covers it. All line citations are unchanged by that diff.

Tip under review: lane `main` = `b78f8b8e` (instruments commit); frozen base = `ad5b52b0`.
`reports/round-67/dispositions/` does not exist yet, so D1 is unsatisfiable at review time —
recorded as a build dependency, not a defect of the counter.

## Answers to the four assigned questions

1. **D1 `git cat-file -e` presence-only — is that the demanded durability?**
   Presence-only is the correct *primitive* for "tracked at the lands revision" (a commit tree
   cannot contain untracked paths), so it does discharge r66-D1's literal "untracked" failure.
   It is **not** the demanded durability, for four concrete reasons:
   - `cat-file -e` succeeds on a **tree**: `git cat-file -e ad5b52b0:corpus` → exit 0 (verified).
     A manifest entry may name a directory and still "be tracked".
   - It accepts a **0-byte blob**; nothing checks the seat report has content.
   - **No dedup**: `include` is a list and `seat` is a filtered list (`accept-ca.py:151-152`).
     Eight identical `INCLUDE .ufo/waves/round-66/w1/X.md` lines yield `len(seat) == 8` → passes
     the `>=8` gate (verified by replaying the leg's exact regex/list code). One committed empty
     seat file named eight times satisfies ">=8 seat reports named".
   - The threshold is **8 of the 63** seat reports the disposition claims to make durable, and no
     leg requires the manifest itself to be committed (`git cat-file -e <lands>:<MANIFEST>` is
     never run); the manifest is read from the **worktree** (`read(root, MANIFEST)`, `:146`).
     `EXCLUDE` lines need only exist (`:162-163`); the docstring's "named with reasons" is unchecked.
   Verdict: necessary, insufficient; the counter under-enforces the Ca statement's own D1
   disposition (seat reports + row fragments + mutant sources + scratch trees with reasons).

2. **D2 `census --file` — does the script accept it?** Yes. Verified both argument orders:
   `sources-census.sh validate --file corpus/SOURCES.md` and `--file … validate` both parse
   (header usage at `scripts/sources-census.sh:9-10`) and both exit 1 on base with exactly the
   expected findings: E12 ×23 (`S776`, `S779`–`S800` "row outside Registry section") and
   E11 (`S753 missing used-by -`). The leg's gate on `returncode != 0` (`:183`) is therefore
   meaningful; the `"\tE"` filter is only used for the detail string. The defect is not the flag,
   it is **provenance**: `CENSUS` is an absolute fleet path outside the lane and the clone
   (`accept-ca.py:54`), `git ls-tree ad5b52b -- scripts tools` finds **no vendored copy**, and the
   script's sha256 is recorded nowhere in the receipt. The D2 verdict, and the E01/E12 backstops
   for every other fail-open in this counter, live in mutable bytes that are not part of the
   lands tree (mtime 2026-10-19, writable).

3. **D4 arithmetic `>= len(R66_REJECTS)+2` (=6) — off by one?** Not arithmetically, but it is
   **conditionally correct**: 6 equals "4 + 2" only if S801–S804 themselves carry
   `opened = 2026-10-24`. Verified base facts: `S753` and all of `S776`/`S779`–`S800` already
   carry `opened = 2026-10-24` (S753 status `mined`, so no freebie today), and S801–S804 are
   absent at base (dry-run: `nonunique=['S801'…'S804']`). The frozen claim never says S801–S804
   are *opened* today — if the disposition author dates them historically, the leg needs 6
   today-rejected rows and fails despite "S801–S804 + >=2". Byte problem, not a counting slip:
   `new_rejects` (`:230-232`) is computed and **never used** — the intended "new" discriminator
   was dropped, so the leg also accepts flipping two *existing* today-opened rows (e.g. S799/S800)
   from `mined` to `rejected` instead of adding new rows. **No counter catches that**: claim C's
   APPEND mutable-cell path (`accept-c.py:371-373`) explicitly permits cell-7 status flips
   (`oc[:7] == nc[:7] and oc[8] == nc[8]`), so the ">=2 *new* first-class rejected rows" clause is
   unenforced end-to-end unless a reviewer reads the diff.

4. **SEQ grep `mv_rev == lands` — byte-exact in all three counters?** Yes. `grep -c` →
   accept-c 2, accept-o 2, accept-ca 3 (`accept-ca.py:114,117`; the third is the detail f-string).
   The `.replace("mv_rev==lands", …)` normalisation at `:249` is dead belt-and-braces. SEQ is
   therefore not a false gate today. It is still a **text-presence** check, not behavioural: it
   cannot distinguish a live gate from `stamp_ok` computed and never `leg()`d, or the five strings
   parked in a docstring. All three counters do early-return on `not stamp_ok`, so the property
   holds now.

## Findings

### High

**H1. STAMP does not tie the bytes read to the stamped revision; Ca has no dirty-worktree read at
all.** `STAMP` (`:112-121`) reads only `git rev-parse main` and `git rev-parse <lands>^{tree}`.
Every Ca input is read from the worktree: `read(root, …)` → `open(os.path.join(root, path))`
(`:64-68`) for the manifest, `corpus/SOURCES.md`, `LOG.md`, `SCORECARD.md`,
`corpus/QUALITY.md`, `corpus/lessons/round-67.md`. A worktree with uncommitted edits, or a
detached/`git checkout <rev> -- <path>` state, leaves `main` pointing at lands, so STAMP passes
while the legs grade bytes that do not exist at the stamped revision. `accept-c.py` and
`accept-o.py` at least compute `dirty_flag` from `git status --porcelain` and print
`dirty_tracked=` — but **neither gates on it**, and `accept-ca.py` contains no `status`/
`porcelain` call at all (verified by grep: the only matches are the `status` cell strings at
`:223`). The r66-D3 class (a PASS whose bytes were never measured) is re-opened through the
worktree instead of through the clock. Repro shape: `git -C <clone> checkout <other> -- corpus/SOURCES.md`
then `python3 -B reports/round-67/accept-ca.py --root <clone> --lands <clone-main>` → STAMP PASS.
Fix: grade every input with `git show <lands>:<path>` (or add a `git status --porcelain` gate that
fails STAMP, and record it), as `accept-o.py`'s tool does for receipts.

**H2. The receipt's tree and counter-sha pins are tautological / worktree-first — the dry-run-ca
receipt on disk is already self-inconsistent.** `tree_rev = git rev-parse <lands>^{tree}` (`:104`)
is a property of the commit, re-derived from the same commit by the tool
(`tools/check-receipt-seq.py:155`), so the TREE leg can never detect that the read bytes differ
from the stamped tree — it is not "a tree hash of read inputs" (QUALITY criterion 17, line 55).
Worse, the counter-sha leg reads the **worktree first**:
`blob = read_worktree(root, cpath); if blob is None: blob = read_rev(root, "main", cpath)`
(`check-receipt-seq.py:168-170`) — it never tries `read_rev(root, stamped, cpath)`, so it cannot
prove the counter exists at the stamped revision. Demonstrated on the frozen artifact:
`reports/round-67/telemetry/dry-run-ca.txt` records
`# counter sha256 (self): 5e8915ac…`, `# stamped revision: ad5b52b0…`, `# tree: de353b04…`.
`git cat-file -e ad5b52b0:reports/round-67/accept-ca.py` → **exit 128** ("exists on disk, but not
in 'ad5b52b0…'"); `ad5b52b0^{tree}` = `de353b046be5…`; `sha256(main:accept-ca.py)` = `5e8915ac…`.
So the receipt pins a counter blob that does not exist at the revision it stamps, and the tree pin
is the commit's tree, not the bytes measured. The receipt is rejected by the very protocol it
advertises, and the tool as written cannot see it. Either the dry-run must stamp the instruments
commit (`b78f8b8`) and record the evaluation root's tree separately, or the counter-sha field must
be optional/absent for base dry-runs, and the tool must read the counter at the stamped rev.

**H3. D2's census is an unpinned external dependency (detail under Q2).** Consequence beyond
provenance: D2's placement check is a coarse interval `[## Registry, ## Leads)` (`:186-201`),
which *includes* the `## Paths` (line 733) and `## Search log` (line 768) sections. Verified:
rows placed under `## Paths` satisfy `reg_pos <= m.start() < leads_pos`. The census is
section-scoped and would flag them (`scripts/sources-census.sh:546-550` resets `in_registry` at the
next top heading → E12), so **the only thing distinguishing "moved into ## Registry" from "moved
under ## Paths" is the unpinned external script**, whose result is not pinned in the receipt.

### Medium

**M1. D1 under-enforces the r66-D1 disposition** (see Q1): no dedup, tree/empty-blob acceptance,
8-of-63 threshold, no manifest-commit check, `EXCLUDE` reasons unchecked. The claim's own wording
("seat reports + spec + registry + row fragments + mutant sources tracked at lands; scratch clone
trees named excluded with reasons") is only enforced to the first item, at 8/63 scale.

**M2. D4 does not enforce "new", and its threshold silently depends on an unstated date**
(see Q3). `new_rejects` is dead code at `:230-232`; the leg counts *any* row with
`status=rejected and opened=2026-10-24`, so status flips of existing base rows satisfy it, and the
"4 + 2" identity holds only if S801–S804 are dated today — a constraint absent from the frozen
claim. Also `nonunique` (`:233`) is a misnomer: `len(findall) != 1` includes 0, so missing rows are
reported as duplicates (observed in `dry-run-ca.txt`: `nonunique=['S801'…'S804']` with all four
absent). Cosmetic, but it makes the failure detail misleading.

**M3. CRITERION checks a token window, not the three named properties.** `:259-263` finds the
first line matching `^\s*19\.\s` and requires the substrings `receipt`, `stamped`, `lands` within
the next 1200 chars. The docstring demands criterion 19 ground "stamped/evaluated equality,
materialized lands evaluation, post-records carrier-parentage" — none of those three is checked.
Sensitive at base (QUALITY.md ends at criterion 18, verified; base dry-run CRITERION FAIL), so it
is not a do-nothing pass, but a criterion that merely mentions the three words passes.

### Low

**L1. D2's S753 check is fail-open on malformed rows.** `:196-199`: `if len(c753) == 11 and c753[10]
!= "—": append(...)`. A 12-cell S753 row appends nothing and the leg passes. Backstopped only by
census E01 (NF != 13), i.e. by H3's unpinned script. Verified current state: S753 has 11 cells,
`cell[7]=mined`, `cell[8]=2026-10-24`, `cell[10]="-"` (ASCII hyphen) — the required flip to `—`
is real and currently absent.

**L2. D2 placement interval admits `## Paths`/`## Search log`** (see H3); the counter never
inspects the section heading, only positions.

**L3. QUOTES counts ids anywhere, not in Gate lines.** `:271-273` regexes `\bS(8[0-2]\d)\b` over the
whole lesson and requires 20 of 24. The docstring says "its Gate names >=20"; 20 ids in prose or a
table pass. `len(lesson_text.splitlines()) > 10` is the only substance check.

## Non-defects verified (so the L1 need not re-litigate)

- D2 `validate --file` works in both argument orders; exit 1 with E12 ×23 + E11 ×1 on base.
- `check-receipt-seq.py --selftest` genuinely prints 14 `PASS` fixture lines and a final
  `SELFTEST: 14/14`, exit 0; every fixture prints a real FAIL on its mutant path.
- SEQ's literals `--lands`, `required=True`, `stamped revision`, `evaluated revision`,
  `mv_rev == lands` are present byte-exact in all three counters (Q4).
- Do-nothing control is unreachable: base dry-run FAILs D1, D2, D3, D4, SEQ, CRITERION, QUOTES;
  only STAMP passes at base, which is by design (`evaluated == stamped == base`).
- `claims.json` parses; `lands` file lists per claim are present and materially match the legs.

## Post-review revision and the C/Ca id conflict

**C1 (Critical, reviewed bytes) — the QUOTES leg was dead; `ACCEPT-CA-67: PASS` was unreachable at
the frozen revision.** `gate_ids = set(re.findall(r"\bS(8[0-2]\d)\b", lesson_text)) & {f"S{n}" …}`
returns bare digits: proved `re.findall(r"\bS(8[0-2]\d)\b", "Gate S805 S806 S807")` →
`['805','806','807']`, so the intersection with `{"S805",…,"S828"}` is always empty and
`len(gate_ids) >= 20` is always False. Consequences: (a) the predicate could never PASS at the
revision the claims and the control receipts froze; (b) `dry-run-ca.txt`'s
`QUOTES FAIL … gate_ids=0` is **not** base-sensitivity evidence — it would print `gate_ids=0`
against a perfect lesson, so the QUOTES row of the do-nothing control is a false-positive reason.
The L1's worktree fix `(S8[0-2]\d)` is correct (proved → `['S805',…]`).

**C2 (High) — the frozen control receipts now certify bytes that are no longer the instrument.**
Receipts pin self-sha `5e8915ac…`, which equals `main:reports/round-67/accept-ca.py`; the worktree
file is `5382ffed…` and `git status` shows it modified. Under the claim's own protocol (receipt
records counter sha; QUALITY criterion 17: "stamping a revision whose bytes fail the receipt's own
legs" is a calibration defect) `dry-run-ca`/`controls-ca` must be re-run against the revised
counter and the new sha recorded before data; otherwise the landed instrument carries no control.
H2 still applies: the tree pin is the commit tree, not the read bytes.

**C3 — the C/Ca id conflict: the L1's per-claim-lands resolution is verified compatible, with one
residual.** APPEND builds `base_set`/`tip_set` dicts keyed by id (`accept-c.py:359-362`), so moving
S776/S779-S800 between sections changes no row line and is neutral. With A_r ⊂ A_c ⊂ A_ca, C at
A_c sees appended = S805-S828 ∪ {S801-S804} ⊆ `NEW_IDS ∪ EXTRA_IDS`, and Ca at A_ca sees
S801-S804 + S829+ for D4's `>=6`. Residual: sequencing makes D4's "new" unverifiable *at A_ca* —
C's APPEND ran earlier, and its mutable-cell path (`accept-c.py:371-373`) permits cell-7 status
flips, so flipping two existing today-opened rows to `rejected` satisfies D4 with no new row and
no counter objection. Recommend a pre-data Ca revision: count only rows whose id is absent from
`BASE:corpus/SOURCES.md` (the dead `new_rejects` variable is exactly this check). Also note the
counter cannot detect the sequencing itself (STAMP is self-referential), so closure must verify
A_r < A_c < A_ca from the receipts' headers, not from equality alone.

## Residual risk / verification gaps

- **STAMP is self-referential**: `--lands` has no external anchor (claims.json carries no lands
  hash yet), so a run may pass any tip as `--lands` and STAMP proves only `evaluated == input`.
  Inherent to pre-lands freezing; the only anchor is the post-land `claims.json`/ledger entry.
- **Prior-round receipt re-derivation dropped**: r66's `accept-ca.py` D2 leg re-derived carriage
  and counter sha for `final-measures-{c,o,ca}`; r67 has no such leg. QUALITY criterion 17 (line
  55) names "the accept-ca RECEIPTS leg of each round" as the standing check. It now lives only
  in claim O's `R66` leg, so Ca's criterion-17 check depends on O running — a declared-ish but
  uncounted dependency.
- `post-records.txt` carrier-parentage is explicitly not a frozen leg; nothing in this counter
  re-verifies it, so the "carrier-parentage is post-records evidence only" clause is honour-system
  until closure.
- Could not exercise an end-to-end PASS: no lands commit exists and
  `reports/round-67/dispositions/r66-wave-evidence-manifest.txt` is absent. The D1 build
  deliverable (and any seat owning it) is a hard dependency for Ca.
- No `lsp` server check was possible from this seat (device absent); all findings are file/line
  plus executed-command evidence, and none relies on grep as a semantic substitute.

Report: .ufo/waves/round-67/w1/RevCounterCa.md
