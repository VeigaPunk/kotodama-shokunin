# CriticReceiptDiscipline — r67 w1 — attack on the --lands/stamped/evaluated scheme

Scope: the three frozen counters (`reports/round-67/accept-{c,o,ca}.py` rev0, committed in `b78f8b8`), `tools/check-receipt-seq.py` (also committed in `b78f8b8`), `claims.json` receipt_protocol + note, base dry-runs/controls. All line refs are to the committed bytes I read this run.

## F1 (STRONGEST COUNTEREXAMPLE, all three claims): the STAMP gate checks the `main` REF, never the checked-out bytes — a moved/dirty clone can print `stamped==evaluated` and PASS every leg

Every counter computes `mv_rev = git -C <root> rev-parse main` (accept-c.py:175, accept-o.py:130, accept-ca.py:98) and gates `mv_rev == lands` (STAMP leg). The legs then read **worktree bytes** for almost everything:

- C: FILE/ONEID/RESTATE/TOPIC read `open(root/ENTRY)` and `open(root/README)` (accept-c.py:211-213, 424); SET/ROWS/HOSTS/LINK/CAPTURE read `open(root/REGISTRY)` (:228); SWEEP *executes* `reports/round-28/readme/sweep.py` from the worktree (:390); NOHARM/APPEND mix worktree vs `git show BASE:` (:232, :378).
- O: SELFTEST runs `tool_abs` = worktree `tools/check-receipt-seq.py` (:162-166); MUT runs worktree mutants (:237-258); OPTIONS runs worktree `--help` (:178). Only R66 reads `main:` blobs (:267).
- Ca: D1 reads worktree MANIFEST (accept-ca.py:123) while checking each INCLUDE against `{lands}:` (:143) — asymmetric; D2/D4 read worktree REGISTRY (:159); SEQ/QUOTES read/execute worktree files (:244, :268).

Concrete defeat: `git clone --no-local . eval`; in eval `git checkout -q -b fake <any commit>` (detached or a branch) or `git checkout -q <base>`; then modify tracked files (e.g. plant a full entry + 24 S805-S828 rows + README row + a doctored sweep.py). `rev-parse main` still returns lands L; STAMP prints `stamped=L evaluated=L equal=True tree=<L's tree>`; every leg grades the worktree bytes I placed — including **committed-bytes-free fabrications**: I never need the lands commit to contain the claim artifacts at all. `dirty_tracked=True` prints in the receipt but **nothing gates on it** — the flag is observational, not a verdict input (accept-c.py:184, 200-205; accept-o.py:139, 152-157). Even with a clean tracked tree, `git status --porcelain --untracked-files=no` (:181-183) hides untracked files, and untracked `corpus/knowledge/.../medicine-healing-codes.md` is silently read by FILE — `dirty=False`, STAMP PASS, fabricated entry passes.
accept-ca.py has a second inconsistency: it never even prints the dirty header (its receipt lacks `# worktree dirty` — compare accept-ca.py:102-106 vs accept-c.py:190), so its receipts carry strictly less evidence than C/O's.

Same class, sharper: the receipt's `# counter sha256 (self)` is hashed from `__file__` *worktree* bytes (accept-c.py:170), and check-receipt-seq's SHA leg also prefers worktree counter bytes (check-receipt-seq.py:168). So the sha pin binds the executed bytes, never the committed `{lands}:counter` — a counter revised or dirtied after lands still self-certifies. Any counter mutation between the lands commit and receipt generation is invisible to the pin.

The receipt also cannot rescue this: `# measured revision (lane main)` is byte-identical to `# evaluated revision` — both are `rev-parse main` (accept-c.py:187-188). "measured" measures nothing distinct; the header trio collapses to two facts.

**Impact:** all three axes — a verdict of PASS can certify post-lands/uncommitted bytes while the receipt reads like a clean lands evaluation. This re-opens exactly the moved-worktree class R66-D3 was routed to fix, one layer down (worktree vs ref instead of tip vs stamp).

**Smallest safe correction (pick one, both cheap):**
(a) gate STAMP on `mv_rev == lands AND rev-parse HEAD == lands AND not dirty` with `dirty` computed **with** untracked files (`--untracked-files=all`); print HEAD separately in the receipt; or
(b) drop worktree reads entirely for claim artifacts: `git_bytes(root, lands, path)` everywhere (accept-c already does this for base registry; extend to tip registry/entry/README and `git show lands:tool` for O's SELFTEST target — run the tool bytes via a temp file, not worktree path).
Option (b) matches the tool's own `--lands` mode design (`read_rev`, check-receipt-seq.py:80-82, 236).

## F4: C-APPEND vs Ca-D4 id conflict — RESOLVED BY L1 RULING (per-claim lands separation); sequencing constraint recorded

Confirmed before the ruling: under a single shared lands commit the pair is unsatisfiable — accept-c.py APPEND `allowed_new = NEW_IDS | {S801-S804}` (:357) vs accept-ca.py D4 needing >=6 rejected rows opened 2026-10-24 (:235); rejected rows can't hide in NEW_IDS (ROWS pins status=mined) and ROW_RE is section-blind (## Leads placement still counts as appended). L1 resolution (this wave, no counter/claims revision): C's receipt runs at its own lands commit A_c where only S805-S828 append over base; Ca's lands A_ca comes later carrying S829+ rejects; A_r (S801-S804 dispositions) lands before A_c. The joint predicate IS satisfiable as sequenced — each counter's receipt is honest at its own stamp.

New constraint this creates for the receipt trail (post-records --topo grades `parent(carrier) == stamped` per receipt, check-receipt-seq.py:194-197): **each claim's receipts must be carried by a distinct commit that is a direct child of that claim's lands commit** — i.e. a strict alternation A_c -> R_c -> A_o -> R_o -> A_ca -> R_ca (order of C/O interchangeable). Batching all three receipts into one records commit makes R_o/R_ca FAIL TOPO (`parent` = the wrong lands). post-records.txt then rides a fourth commit R_pr, child of R_ca — and its self-grade remains impossible (F2). Also note C's "registry 724 -> 752" statement is then true only *at* A_c — at tip the count is 756+; terminal counts in claim statements become stamp-relative, which the claims.json separability note should state explicitly.

## F2: post-records.txt IS a receipt — the self-reference hole is real, not closed

claims.json:113 says post-records.txt is `check-receipt-seq.py --topo over the three receipts **+ itself**`, committed in a third commit, self-equality "re-verified by hand". Under the tool's own semantics this is impossible in-commit: `--topo` resolves the carrier via `git log -1 main -- <path>` (check-receipt-seq.py:188). At generation time post-records.txt is uncommitted, so its self-grade is either `TOPO-… no_carrier FAIL` (poisoning the committed file to `RECEIPT-SEQ: FAIL`) or the row is omitted/fabricated. Post-commit re-run can only yield `parent=R2`, i.e. PASS only if post-records.txt stamps `R2` (the *preceding* records commit, not lands L) — but then its SEQ header legs would be `stamped=R2` while R2's content is the three receipts' carrier… a receipt whose stamp names a receipt-commit, not a lands commit: a different semantic, silently folded into the same evidence file. Either way the committed artifact cannot truthfully contain a green self-grade. "Re-verified by hand" is an un-instrumented assertion — the exact class of evidence the round claims to make executable.

**Correction:** declare post-records.txt's own row explicitly `UNEVALUABLE-BY-CONSTRUCTION` inside the file (or drop self-inclusion entirely; grading the three r67 receipts suffices for the carrier-parentage claim). If self-grading is kept, it needs a named exception leg in the tool, not a hand-wave.

## F3 (minor, tool): default (post-records) mode grades worktree bytes

`read_worktree` first, `git show main:` fallback (check-receipt-seq.py:239-243); `check_counter_sha` hashes the worktree counter file (line 168). Post-records evidence can therefore certify a dirty copy. Selftest has no fixture for it (the mutants cover equality/parentage/tree/carrier, not byte-source). Lower severity — post-records is human-evidence, not a frozen leg — but the same hole class as F1 and worth one line in the docstring or a `git show HEAD:` read.

## Leg classification (assigned re-list)

| counter | leg | reads | lands-evaluable? |
|---|---|---|---|
| C | STAMP | rev-parse main | yes (gate) |
| C | FILE, SET, ROWS, ONEID, RESTATE, HOSTS, LINK, APPEND, NOHARM, SWEEP, CAPTURE, TOPIC | worktree files / worktree exec / git diff BASE | all yes — none requires post-lands data |
| O | STAMP, SELFTEST, DIFF, OPTIONS, LANDS, TOPO, HEADERS, MUT, FIXTURES | worktree tool/mutants + temp fixture repos | yes |
| O | R66 | `git show main:` r66 receipts + log | yes — historical receipts are committed at base already (dry-run-o.txt:15 prints R66 PASS at base) |
| Ca | STAMP, D1-D4, SEQ, CRITERION, QUOTES | worktree files; D1 splits worktree-manifest vs `{lands}:` cat-file | yes |

**No leg evaluates a post-lands artifact.** The D2-class defect is genuinely fixed: the only post-lands predicate (carrier-parentage) was expelled to `--topo`/post-records.txt, and claims.json's lands lists contain no post-records paths. Dry-runs confirm all claim legs FAIL at base while STAMP/R66/LINK/APPEND/ROWS/NOHARM vacuously/honestly pass — no do-nothing control passes.

## Other receipts verified (no defect)

- `--lands` required=True + 40-hex fullmatch + `{lands}^{tree}` resolvable in all three counters; STAMP fail exits 1 early (fail-closed).
- Tool `--lands` mode correctly resolves lands commit, reads `git show lands:path`, treats absent receipt as FAIL `unreadable`, reports `moved_past` as flag-only (docstring honored, :13-17, 226-234); `--topo` is parent-of-carrier equality — exactly the r66 predicate that was unevaluable at lands.
- SEQ leg string-checks (`--lands`, `required=True`, `mv_rev == lands`) are weak tripwires, but the counter's own STAMP behavior backs them; cosmetic only.
- 14 selftest checks named and counted; MUT_EXPECT pins each mutant to its check class — consistent with dry-run-o FAIL at base.

## Dependency note

post-records.txt does not exist yet (not committed; the third commit is post-records by design). F2 attacks the committed design text in claims.json:113, which is the artifact under review.
