# RevCounterCa — attack on `reports/round-66/accept-ca.py` (ACCEPT-CA-66)

Seat: reviewer/counter-attacker. Scope: the frozen counter only — `reports/round-66/accept-ca.py`
at the lane tip (sha256 `a4b93bf750e997b3ed6185dc3bcf242b460f14068a3c492490fc721879775c11`, the
same sha the dry-run recorded). Every claim below is backed by a run in a throwaway clone under
`/tmp/r66-ca-attack*` (the lane was not written to, no git/jj writes in the lane).
Attacks named per the ticket: (1) D2 `git log -1 main -- <receipt>` / wrong-lands stamp,
(2) D3 existence counting, (3) QUOTES id regex.

Live state at the lane tip (for orientation, not a defect): `python3 -B reports/round-66/accept-ca.py
--root .` → `D1 FAIL bad=['quote','s776_citations=0','s753_citations=1']`, `D2 FAIL …absent`,
`D3 FAIL named=65 existing=8`, `D4 FAIL`, `CRITERION FAIL`, `QUOTES FAIL`, `ACCEPT-CA-66: FAIL`.
`corpus/lessons/round-66.md` does not exist yet; the games entry still carries `(S753)` at line 23.

Tooling note: no LSP server answers a standalone counter script in this seat's inventory (no `lsp`
device exposed), so evidence is by execution + exact line cite. No installs were made.

---

## HIGH

### H1. D2 validates the **working-tree** receipt, never the committed blob — a dirty/forgotten commit passes
`reports/round-66/accept-ca.py:111` reads the receipt with `read(root, rpath)` (working tree), while
`:121` resolves the carrier with `git log`. Nothing ever compares the two (`git show <carrier>:<rpath>`
is absent). The docstring's own premise — line 6, "Each leg re-derives its disposition from committed
bytes" — is false for D2.

Proof (`/tmp/r66-ca-attack2`, real counter, real `git log`):
```
committed receipt:  tree: 713981b487f3334744a7853b70088094294ce63e   (wrong)
working tree:       tree: a6db0b4633256627e25edcfa8ed19033cebe385b   (uncommitted edit)
$ git status --porcelain reports/round-66/telemetry   ->  " M" x3
$ python3 -B reports/round-66/accept-ca.py --root .   ->  D2 PASS bad=[]
```
A receipt that is wrong on disk as committed passes as soon as the operator fixes it locally and
forgets to commit — the exact "stale receipt" class this claim exists to close. Symmetrically, an
operator can flip a failing D2 to PASS with an uncommitted edit and no commit at all.

### H2. The D2 stamp is self-referential: a receipt minted **before the lands** passes, i.e. stamped for the wrong lands
`:115-129` takes the expected parent from the receipt's own text (`stamped`), then asserts
`carrier^ == stamped`. Nothing ties `stamped` to the commit that carries the lands the receipt claims
to measure, and nothing compares `stamped` to the actual integration revision at run time. This is
the round-65 R65-D2 class re-created under a new name: the receipt declares its own ancestry
requirement. claims.json's own `review_only` records the orchestrator's intended fix ("make the
expected lands hash the actual parent at run time") — it is not implemented.

Proof (`/tmp/r66-ca-attack2`):
```
B = 94209e8… (base)      git ls-tree -r --name-only B -- corpus/lessons/round-66.md reports/round-66  -> 0
receipt commit R = 048f378  parent = 94209e8…   (receipts committed at base, before any land)
lands commit  L = 95b7531  (lesson + registry landed AFTER the receipts; main tip = L)
$ python3 -B reports/round-66/accept-ca.py --root .   ->  D2 PASS bad=[]
```
So a receipt stamped at a revision whose tree contains **zero** round-66 land bytes passes, provided
the receipt commit is that revision's direct child and no later commit touches the receipt. A
plausible accident in a multi-commit integration (measure after the registry commit, land the
entry/lesson afterwards) passes while the receipt attests a tree it never measured.

Consequence for measurement order: the only passing protocol is "all lands in L → run all three
counters at main=L → commit the three receipts in one child commit R → never touch the receipts
again". Note the reverse case is *also* forced and brittle: if the receipt were committed inside the
lands commit, `carrier^ = L^`, not `L`, so it fails. Each receipt must be its own child commit.

### H3. `counter sha256` is compared against the working tree, not the stamped revision — so the leg cannot mean "resolves against the stamped revision"
`:130-133` resolves `stamped^{tree}` from git (good), but `:134-141` reads the counter with
`read(root, counter_path)` (working tree) and compares its sha to the receipt. At the stamped revision
the counter normally does not even exist (it is a land of an earlier round or of this round's later
commits), so "the receipt's counter sha256 lines resolve against the stamped revision" (docstring
line 17) is unverifiable by construction. This is a live fabrication channel: the PASS lines pasted
into the receipt can come from counter bytes that no revision contains, while the stamped sha names
different bytes.

Proof (`/tmp/r66-ca-attack3`): counters committed at P (accept-ca.py blob sha `a4b93bf7…`), counter
then edited (one comment line appended), receipt stamped `P` with `counter sha256 (self):
cbaa5404…` (post-P bytes), receipt committed as P's child:
```
$ git cat-file -p P:reports/round-66/accept-ca.py | sha256sum -> a4b93bf7…
receipt sha: cbaa5404…   working-tree sha: cbaa5404…
$ python3 -B reports/round-66/accept-ca.py --root .   ->  D2 PASS bad=[]
```
Note the direction of the incentive: any *honest* post-measurement edit of a counter (even a typo fix)
invalidates the receipt, so the operator is pushed to edit the hash line or to measure after the last
edit; the counter cannot distinguish the two. QUALITY criterion 17's requirement ("a receipt names the
revision its read-path bytes actually equalled … a run over a moving worktree is disclosed") is
implemented for the *tree* only, not for any read input.

---

## MEDIUM

### M1. D3 counts mentions, not seats: 8 empty files for never-dispatched seats PASS
`:145-154` collects every `.ufo/waves/round-66/\S+\.md` occurrence, filters by `os.path.isfile`, and
requires `>=8`. The only content test is one global `re.search(r"(?i)(seat|report|status)")`, which the
receipt's own header satisfies. claims.json Ca leg 3 requires "per-seat status line; dead seats carry a
last-error line" — none of that is implemented.

Proof (`/tmp/r66-ca-attack4`): 8 zero-byte files `Dead01..Dead08.md`, receipt = one `STATUS status`
line + 8 paths, seats never dispatched, no status/last-error text:
```
$ python3 -B reports/round-66/accept-ca.py --root .   ->  D3 PASS named=8 existing=8 min=8
```
Duplicates also inflate the `>=8` floor (no distinctness check): 4 real files listed twice give
`named=8 existing=8` and PASS (`re.findall` proof run, `named=8 distinct=4`). The floor is also
disconnected from the wave: `spec-v2.json` has 64 items, the surviving seed receipt currently names
65 distinct paths with 0 status/fail/dead tokens — and that receipt would satisfy D3 unchanged once
the files exist.

### M2. D3 requires *every* named path to exist — one unwritten seat kills the leg
`len(existing) == reported` (`:151`) makes the receipt a liability: the seed lists 65 expected paths
(spec = 64 items); a single seat that never writes its file, or one stale entry, fails D3 even though
`>=8` real evidence exists. Meanwhile the receipt is a live working note (I observed 63 → 65 paths
within this wave), not frozen evidence; a receipt edited after dispatch can add or drop names freely.

### M3. QUOTES threshold is 25 ids but the frozen claim asks for the round's *new* ids (24)
`:174` requires `len(gate_ids) >= 25` over the pattern `\bS(77[6-9]|7[89]\d|800)\b` — exactly
S776..S800. claims.json Ca leg 6 says "the Gate names the round's new ids", and claim C defines the
round's new rows as **S777-S800 (24 rows)**; S776 is the *pre-existing superseded* row, not new.
Verified by execution:
```
enumerated S777..S800 -> 24  (fails >=25)
enumerated S776..S800 -> 25  (passes)
```
So a lesson that literally satisfies the frozen leg FAILS the frozen predicate, and the counter's
docstring (line 26-27, "S776-S800") contradicts the claim text. This is a frozen-predicate
conformance defect: either the claim text or the floor must be fixed before data is judged.

### M4. QUOTES is vacuous when the Gate section is absent, and ids are counted outside the Gate
`:171-177` accepts `exit==0 and re.search("(^|\s)0 finding", stdout)`. `tools/check-gate-quotes.py`
prints `GATE_QUOTES_ERROR: <file>: no '## Gate' section` **and** `GATE_QUOTES: 0 findings` with exit 0
(verified on `corpus/lessons/round-65-verifier-spotcheck.md`). Therefore a lesson with no Gate section
at all, or an empty one, satisfies "finds 0 findings". `gate_ids` is likewise matched over the whole
lesson text, so the 25 ids can live in a routed-defects table and the Gate can be missing or empty:
the leg's stated subject ("its Gate names the round's ids") is never checked. The tool has a
`--strict`-like behaviour only via the ERROR line, which the counter ignores.

### M5. D4 passes on a hand-written receipt with `acceptance_runs=0`
`:157-161` requires a `SEPARABILITY: <n> findings` line, an `acceptance_runs=<d>` count and the
absence of the substring `PARTIAL`. No exit code, no manifest path, no budget flags, no timestamps, no
provenance. Proof (`/tmp/r66-ca-attack4`), receipt is three hand-typed lines, no tool run:
```
hand-written, no tool run
SEPARABILITY: 0 findings
acceptance_runs=0
-> D4 PASS complete verdict + run count, no partial
```
`acceptance_runs` comes from the tool's `SEPARABILITY_NOTE` on **stderr** (`tools/check-claim-separability.py:834`), so an
honest stdout-only capture of a perfect run FAILS D4, while a forger who types the line passes. Also
`"PARTIAL" not in d4` (substring, anywhere) rejects an honest partial run, which contradicts claim O's
designed honest-partial mode if the round's real run is bounded; and any `\d+` finding count passes,
so a run on a trivial/different manifest qualifies.

### M6. D1 is string presence, not durability re-derivation
`:89-105`: `"200" in d1` matches `1200ms` (verified); the quote must merely appear in the receipt
text (it currently does **not** — `grep -c "Versions of mancala" s753-recapture.txt` → 0, so the
drafted receipt already fails `quote`); `20261024111013` and `S776` are substring checks. No fetch, no
capture replay, no digest comparison is performed by the counter, although docstring line 9-11 asserts
"records the live PDF … and the fresh capture … replaying 200 pdf". The receipt itself shows the
claims are a human summary: line 8 `old_capture status=000`, line 21 `old_replay_status=200`, and the
disposition line reads "replays PDF not pdf" (garbled) — the counter cannot tell a true replay from a
typed one. Comparing byte-exactness is review-only, but the leg's wording overstates what it derives.

### M7. D1 citation regexes are format-locked; a line that cites S753 passes
`:100-105` counts only `\(S776\)` and `\(S753\)`. Verified against the real shapes:
```
"- mancala S753 superseded by S776"  -> s776=0  s753=0   (cites S753, passes the zero-S753 leg)
"- mancala (S776, archive copy)"     -> s776=0  s753=0   (cites S776, fails the exactly-one leg)
"- mancala (S753) and (S776)"        -> s776=1  s753=1
```
So "cites S776 exactly once and S753 zero times" holds only for the bare parenthesized form; a prose
re-point that still names S753 (or a footnote-style citation) escapes. The entry's current line 23
`- Versions of mancala span Africa and Asia, … (S753)` is caught by luck, not by design.

### M8. CRITERION: hardcoded 18 vs claim's ">=18", and a 900-char window that spills into criterion 19
`:164-168` requires a line `^\s*18\.` and `anchor` + `resolv` within 900 characters of that offset.
Verified: a file whose criterion 18 is about receipts and whose criterion 19 says "row anchors
resolve" passes (spill); a file with only criterion 19 fails, though claims.json Ca leg 5 says "a
numbered criterion **>=18**". The window is not clause-scoped, so an unrelated criterion 18 inherits
the next criterion's words.

---

## LOW

### L1. `git rev-parse main` is resolved in the caller's cwd, not `--root`
`:78` omits `-C root`/`cwd=root`. Demonstrated: running the clone's counter from the lane with
`--root /tmp/r66-ca-attack2` printed `# measured revision (lane main): 94209e8…` (the *lane's* main)
instead of the clone's tip. Display-only for the verdict, but this is the exact line operators copy
into receipt headers (the round-65 receipt format does), so a wrong-repo stamp can originate here —
and by H2 that stamp then *defines* the expected parent.

### L2. D2 cannot coexist with criterion 17's re-stamp-preservation pattern
QUALITY 17 requires "the original receipt bytes stay preserved below a marker when a re-stamp corrects
attribution". Appending that correction in a second commit moves `git log -1 main -- <receipt>` to the
later commit, whose parent is the receipt commit, not `stamped` → D2 FAIL. Any post-commit correction
to a receipt breaks the leg permanently. The round passes only if no receipt is ever corrected after
commit; that constraint is nowhere recorded.

### L3. D2 is unsatisfiable in a counterfactual overlay (declared, but the declaration overstates it)
The needs_git clone is `git clone --shared … && git checkout --detach <base>`
(`tools/check-claim-separability.py:613-614`); the receipts exist only if REC lands are overlaid, so
Ca's own acceptance in every counterfactual reads `D2 …absent`. claims.json's separability note calls
this "history-derived, consistent with counterfactual overlays" — it is not merely history-derived: D2
cannot pass in an overlay at all. It is declared, so residual risk, not a hidden defect.

### L4. Conflicting stamp lines are silently ignored
`:115-116` prefers `measured revision (lane main): …` (the counter's own output) over the header form
`measured revision: …`. If a receipt carries both and they disagree, the discrepancy — precisely the
attribution error criterion 17 exists for — is never reported.

---

## Residual risk
- Every receipt is author-written text; after H1/H3 the counter's only real bindings are git ancestry
  (self-declared, H2) and sha lines (working-tree, H3). A fabricated receipt with plausible ancestry
  is indistinguishable from a measured one by this instrument. Only the non-author re-derivation in
  `review_only` stands between a fabricated record and PASS.
- D3's floor (>=8) is unrelated to the 64-seat wave, and existence is the only evidence class.
- If any of the three final measures runs before the last land commit, H2 lets it pass with a stamp
  that measured an incomplete tree; the leg will not notice.

## Verification gaps
- No end-to-end PASS run was possible: the lane has no lesson, no receipts, no `separability-real.txt`,
  and the games entry still cites `(S753)`. All proofs are per-leg in throwaway clones with the real
  counter bytes.
- QUOTES was validated against the *tool's* output shape on an existing lesson, not against a drafted
  round-66 lesson (none exists yet); the 24-vs-25 finding is arithmetic-proof plus the claim text.
- No LSP/type-check surface applies; `python3 -B` execution is the evidence.

Report: .ufo/waves/round-66/w1/RevCounterCa.md
