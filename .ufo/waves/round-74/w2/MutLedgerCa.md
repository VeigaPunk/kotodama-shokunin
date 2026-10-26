# W2 seat MutLedgerCa — attack on the claim-Ca ledger (round 74, hyaku run 7)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (READ-ONLY for me; every probe ran in my own
disposable clone `/tmp/MutLedgerCa/clone.yPgl86`, verified `git rev-parse --show-toplevel` = clone root
before use). Base `f7104cbc…`, operative freeze F3 `00c408a0…`, Ca lands `5e4796c0…`, C lands
`c4bf61a8…`. Date 2026-10-25. Leaf seat: no delegation, no sibling files touched.

Tooling: none installed (python3 3.x system, system git, system curl only). No pacman.

## 0. Baseline (pristine bytes)

```
D=$(mktemp -d /tmp/MutLedgerCa/clone.XXXXXX); git -C "$D" init -q
git -C "$D" rev-parse --show-toplevel        # -> $D (verified)
git clone -q <lane> "$D/lane"; git -C "$D/lane" checkout -q --detach
git -C "$D/lane" branch -f main 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 \
  --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
```
Raw tail: `ACCEPT-CA-74: PASS legs=11/11`, exit 0 (98.7 s; RECEIPTS re-runs both round-73 counters at
`2d1cd914…` and byte-compares the committed receipts — both PASS).
Counter self sha256 `8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f`;
ledger at freeze sha256 `88d5fd522c86b3ef37577531d39b148633455836ecd207f27a27a449c8725bd4`
(counter-printed; my byte-for-byte extraction matches). All 13 pairs red at base, LC-09 green at lands.

accept-c: `git branch -f main c4bf61a8d722f9168ce0fd8021a6261c000610c5` then the analogous run →
`ACCEPT-C-74: PASS legs=13/13`, exit 0, 16.5 s, main restored to `5e4796c0…` afterwards.

## 1. Per-pair audit — the four questions

Counter source read in full (leg_ledger/leg_basemismatch/leg_repair/leg_annotate/leg_nostub/
leg_separable/leg_stamp, run_observe, observe_problem). Ledger read in full (940 lines).

**Q1 observe_cmd read-only + reads committed bytes, not a constant — SURVIVED (claim holds).**
All 13 argvs are `git grep`/`git diff` over 40-hex revisions (LC-01/15/17/18, LC-06/07/08) or `HEAD`
inside the counter-materialized lands clone (LC-09, the only REPAIR pair; leg_repair refuses any other
40-hex pin for REPAIR, so HEAD=lands is forced). No interpreters, no metacharacters. Not constants:
every token moves with the pinned tree (804/724/728/701; 247/32/95; 97656; two; present — each
reproduced by me, §2). That the guard rejects constant shapes is proven by probes j2/j6 below.

**Q2 can stated_text be changed at stated_at and still anchor — NO (SURVIVED).**
leg_ledger checks (i) `stated_text in norm(body)` (whole file at base), then (ii)
`stated_text in norm(lines[line_no-1])` — line-level; (iii) stated token ∈ stated_text; LC-03's fleet
site is resolved at `stated_fleet.pin` via `git -C <fleet> show`, requires pinned bytes == sha256
`000bab3a…` AND == fleet HEAD bytes. Base is immutable, so the anchor cannot drift. Probe j3 (misline)
is rejected with `stated_text is in corpus/README.md but NOT on line 736`.

**Q3 expected_after reachable only by the real repair — SURVIVED (LC-09).**
Lands SKILL.md has exactly ONE line matching `` civilizations/` — (\d+) entries` `` — line 594, the
repaired line (`95 entries: 93 earlier-civilization`); diff base..lands = line 594 changed + 3 pure
appends at :705+. REPAIR additionally requires: statement token == truth at lands (95), != base stated
(94), base stated_text absent from lands file, expected_after == statement. Deleting line 594 without a
true replacement fails statement_after (no-match); no bystander line exists to leak a pass.

**Q4 ANNOTATE re-derivations return the new token for the RIGHT reason — SURVIVED.**
(a) Pinned revisions are the commits the notes name:
`git rev-parse 65fe857^` = `94209e8f80969dbac48d56c5d0e2e623635b8616` (= LC-18's argv);
`git rev-parse c58eb84^` = `c5f099211e1d6c095e7c59edbd05c0043b4b95fc` (= LC-17's argv);
`65fe8572822…` = `65fe857` (= LC-15's argv, the round-66 landing). 
(b) Re-runs in my clone (raw outputs):
```
git grep -c -E '^. S[0-9]{3}' 65fe8572822ef83f1750593af77daddf34a1e337 f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md
  -> 65fe8572…:corpus/SOURCES.md:724 / f7104cbc…:corpus/SOURCES.md:804        (LC-15: 724 ✓)
git grep -c -E '^. S[0-9]{3}' c5f099211e1d6c095e7c59edbd05c0043b4b95fc f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md
  -> c5f09921…:corpus/SOURCES.md:728 / f7104cbc…:corpus/SOURCES.md:804        (LC-17: 728 ✓)
git grep -c -E '^. S[0-9]{3}' 94209e8f80969dbac48d56c5d0e2e623635b8616 f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md
  -> 94209e8f…:corpus/SOURCES.md:701 / f7104cbc…:corpus/SOURCES.md:804        (LC-18: 701 ✓)
git grep -c -E '^. S[0-9]{3}' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md
  -> f7104cbc…:corpus/SOURCES.md:804                                          (LC-01: 804 ✓)
```
(c) **Pattern-vs-row-regex equivalence** (the tasking's key question): the ledger's `^. S[0-9]{3}`
and the claim's own row regex `^ {0,3}\|[ \t]*S[0-9]{3,}[ \t]*\|` were compared as LINE SETS over
`corpus/SOURCES.md` at all four pinned revisions: identical sets at every revision —
804/804 (base), 724/724 (65fe857), 728/728 (c58eb84^), 701/701 (65fe857^); `only-ledger-pattern: 0`,
`only-claim-regex: 0` in all four directions. The ledger's R2 claim ("measured identical") holds on
the revisions actually used, not just the three it names. 
(d) Sentence groundings verified verbatim at base: `corpus/README.md:28` "registry moved 752 → 776
rows." (LC-17 before-token), `:36` "registry moved 753 → 776 rows." (LC-15 after / LC-18 before),
`SHONEN.md:6` "(412 rows after round 56 — 367 mined, 35 queued, 10 rejected" (LC-01).
(e) LC-02/03 ground truth: base `reports/round-73/telemetry/selftest-r3.txt` prints `SELFTEST OK: 10
scenarios`, the r1 receipt prints 9 — the 9→10 correction is right.
(f) Glob-vs-entries (LC-06/07/08/09): at base every `.md` under `corpus/knowledge` is exactly
two-level (`corpus/knowledge/<dir>/<file>.md` = 247, zero deeper); glob count == ls-tree count == 247;
per-dir 32/29/38/29/24/95 == README:775/777 last footer == K2; linguistics 32 (LC-08), civilizations
95 (LC-09). "N files changed" from the empty tree is exactly the entry count on this tree.
(g) LC-12 checked against reality, not just self-consistency — CDX probe
(UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`):
`web.archive.org/cdx/search/cdx?url=cambridge.org/core/journals/…/article/phonology-from-the-inside-out-…/649F8BED…&fl=timestamp,statuscode,mimetype`
→ exactly `20241106195515 200 text/html` and `20241107004043 200 text/html`; positive control
(`url=gnu.org&filter=statuscode:200`) returned 200 rows. The lesson's "HAS two status-200 Wayback
captures" is TRUE; claims.json:11's "no Wayback capture of the same page" is the false half — no→two
is the right correction. (Quotes above ≤25 tokens, located.)

## 2. Ledger-grammar probes — 6 junk ledgers + 1 bonus, committed in my clone, counter re-run with
freeze = the clone's commit containing the junk ledger (`FJ`), lands = `FJ` + lands tree with the same
junk ledger (`LJ`, plumbing: `read-tree <lands>`; `--is-ancestor FJ LJ` holds; claims/ledger
byte-identical at freeze and lands as FROZENCFG requires).

| probe | junk sha256 | FJ | LJ | verdict |
|---|---|---|---|---|
| j1-minpairs (3 pairs) | bc35f480…aac | dd0e4b7a… | c05651bc… | FAIL 7/11 — LEDGER `pairs=3 < min-pairs=10` |
| j2-echo (constant printer) | 5006912e…eda | f0040477… | 3977de86… | FAIL 6/11 — LEDGER `argv[0] 'echo' not in the observe allowlist` |
| j3-misline (anchor moved to :736) | ded873f4…616 | 90930175… | 954b906c… | FAIL — LEDGER `stated_text is in corpus/README.md but NOT on line 736` |
| j4-checkout (mutating argv) | 1fc9c45a…331 | e1730ca4… | ba1fb1ad… | FAIL — LEDGER `git subcommand 'checkout' not in the read-only allowlist` |
| j5-dupid (unique drops to 8) | e6dc124c…1df | 2231e167… | 0c79ec6f… | FAIL — LEDGER `duplicate id` ×3 (+ ANNOTATE/NOSTUB row mismatches) |
| j6-python (interpreter argv) | 91e1bcc5…a9f | d2a53eb8… | 3a79171e… | FAIL — LEDGER `interpreter/constant-printer binary 'python3' is refused (H2)` |
| j7-absence (0-count grep, positive expected) | db2df8c6…e35e | f176ee87… | 3b4d5b06… | FAIL — LEDGER `absence-observation pair (base count 0, expected_after '804')` |

**Survivors: NONE.** All six required probes (+ j7 bonus) rejected on the named grammar leg for the
named reason. j1's APPENDONLY fail is counter-correct (with LC-09 unlisted, its landed SKILL.md:594
in-place edit is unlicensed).

Probe-harness disclosure (my defects, not the claim's): (i) I did not flip the clone's local `main` to
each LJ, so STAMP also failed on every probe (`measured 5e4796c0… != lands <LJ>`). STAMP is the only
main-dependent leg; every other leg's verdict is main-independent, and no probe passed its data legs,
so no survivor could have been masked. (ii) Two cosmetic `checkout` aborts occurred mid-loop and were
recovered by the script's `reset --hard` before each FJ build; FJ/LJ/blob ids above are from the
actually-run commits. (iii) P0 below was first run vacuously (a `reset --hard` in my script wiped the
mutation pre-commit — it printed a plain baseline PASS) and was redone properly.

## 3. FINDINGS

**F1 (MEDIUM) — the frozen ledger's own `repair_edits[LC-01]` is unexecutable under the claim's
APPENDONLY leg; following it flips the counter to FAIL.** The block prescribes an in-place edit of
`SHONEN.md:6` (and LC-01's `why` narrates it: "The repair prepends the dated current figure…"), but
LC-01 is ANNOTATE, and APPENDONLY licenses in-place changed lines only on REPAIR stated_at lines;
LC-01 can never be REPAIR (leg_repair refuses base-pinned observations while ANNOTATE requires the
base pin — a catch-22). Mutation test (clone commit `a6b05d99a32a606bee1d29a9ca301f30b6980289`,
SHONEN.md blob `9bee79be383c19681d50f2dd0edd313951acc540` → `0a753443e009d016e3fa108a851fa27c4fef71f6`,
exactly the ledger's `new_line`, real ledger, real freeze):
```
python3 -B reports/round-74/accept-ca.py --root . --lands a6b05d99… --freeze 00c408a0… --fleet-root /home/vgpnk/Projects/shokunin
  -> ACCEPT-CA-74: FAIL legs=10/11 (exit 1)
     LEG FAIL APPENDONLY  problems=['SHONEN.md: changed lines outside REPAIR stated_at lines [6]']
```
The operative landing avoided the landmine (it left SHONEN.md:6 as filed and closed LC-01 by SCORECARD
row only — consistent with ANNOTATE semantics and with "nothing requires rewriting frozen bytes"), so
no wrong verdict was issued; the defect is the frozen asset's self-contradiction. Fix: in any future
freeze, strike `repair_edits[LC-01]` or re-label it "annotation-only — line stays as filed"; never
apply it.

**F2 (LOW) — LC-01's receipt pointer mis-cites.** The ledger (and its unapplied `new_line`) says
"804 rows after round 73 — 709 mined, 58 queued, 37 rejected — census exit 0 in
`reports/round-73/telemetry/census-end.txt`", but that receipt is a raw validate run (W04 lines +
`kotodama ok …` + `exit=0`) containing none of the four figures (grep `804|709|queued` → 0 hits). The
figures themselves are TRUE and tree-derivable: base SOURCES.md column 7 counts = mined 709 / queued
58 / rejected 37 over 804 rows (my count). Fix (future rounds): cite the table itself or a receipt
that carries the numbers. The landed SCORECARD LC-01 row does not propagate the bad pointer.

**F3 (LOW) — `annotate_rows` block lists 11 of the 12 ANNOTATE pairs (LC-01 missing).** The counter
ignores the block (derives row requirements from pair dispositions) and the landed SCORECARD carries
all 12 rows, so nothing mis-grades; the frozen block is out of sync with the frozen claim it
annotates. Fix: keep the block in sync or drop it.

**F4 (LOW, disclosed by the ledger itself) — LC-09 does not pin the same line's second token.** A
half-repair to "95 entries: 92 earlier-civilization" would pass (the 92→93 token has no pair;
LC-10 was dropped because the honest 93 observation needs a `:(exclude)` pathspec the guard refuses).
`dropped_candidates` discloses exactly this; the legs are the claim's rule and were not amended —
recorded as a coverage note, not a rule violation.

**F5 (LOW, grounding note) — LC-11/LC-16 new tokens rest on committed seat prose, not committed
capture bytes.** No blob of size 23443 or 97656 exists anywhere in the tree (`ls-tree -r` sweep at
base and lands: zero hits); the decoded-payload figure lives in `.ufo/waves/round-73/w2/
ScoutReopenS879.md` ("python gzip.decompress -> 23443 -> 97656 bytes"), and LC-16's "present" in the
lesson's own Quarantine row. Within ANNOTATE's design (correcting filed history against the round's
committed evidence) — note only.

## 4. Attacks that FAILED (the claim survived)

1. observe_cmd read-only/committed/non-constant, per pair — survived (§1 Q1; guard refusals proven by j2/j4/j6/j7).
2. stated_text re-anchoring at stated_at — survived (line-level + fleet pin checks; j3 rejected).
3. expected_after reachable without the real repair — survived for LC-09 (§1 Q3); ANNOTATE rows+re-derivations are counter-checked and my independent re-runs reproduce every token (§1 Q4).
4. LC-01/15/17/18 wrong-reason counts — survived: pattern ≡ claim row regex (identical line sets, 0/0 diffs) at all four pinned revisions; argv revisions ≡ the commits the notes name.
5. Glob-vs-entries for LC-06/07/08/09 — survived (no nested entries; counts exact).
6. Junk-ledger grammar probes — 6/6 (+1) rejected; no survivors.
7. LC-12 no→two — the new token is TRUE against the live CDX, not merely self-consistent.

## 5. Restoration evidence

`RESTORED head=5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 main=5e4796c0… dirty=0` (clone worktree back
to pristine lands; scratch clone is disposable per tasking and retains the probe commits under
detached refs). The real lane was never written by me; at report time its HEAD had moved to
`92b8d4bb…` with 20 dirty entries from sibling seats — all my evidence is pinned to commits, so the
move does not affect any verdict above. Full probe logs: `/tmp/MutLedgerCa/logs/*.txt`.
