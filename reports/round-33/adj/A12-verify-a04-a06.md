- Seat: A12 | verifier | claim A | date 2026-10-19 | baseline 139e3b6

# A12 — independent verification of A04–A06

**Mission** (`reports/round-33/targets.json:59`): "Independently re-run the cited commands in
A04-A06 fragments; same verdicts or filed defects." **Out:** this file only.

**Snapshot:** `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb` (== `reports/round-33/claims.json:8`).
All commands at the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
read-only, stamped `A12_VERIFY_UTC` (2026-10-19T04:01–04:06Z) unless a different stamp is given.

## 0. Dependency status — all three fragments landed and are verified

`adj/A04-bleed.md` and `adj/A06-contested.md` landed at `03:55–03:56Z`; `adj/A05-corpus.md`
landed by `04:05:30Z` — after this seat's first pass, which had executed the three check classes
itself under the missing-dependency rule (`targets.json:10`). All three fragments are now
verified below: **A04 CONFIRMED (§1), A05 CONFIRMED with one census note (§2), A06 CONFIRMED
(§3)**. Nothing in this fragment is a re-statement of a fragment's own text; every row is an
A12 command.

## 1. A04 fragment — verdict **CONFIRMED**, all cited commands reproduce

| A04 claim | A12 re-run | result |
|---|---|---|
| L0 file 49 lines / 38356 bytes, sha256 `60ccdc9e…`, mtime `2026-10-18 17:14:10 -0300` | `wc -l`, `stat -c '%s %y'`, `sha256sum` | **match** — 49 lines, 38356 bytes, `60ccdc9e9a0a7179d97d82349a34e0cc53f1520c6f69c6db624f4f72beac51a6`, same mtime (pre-declaration) |
| exactly 4 kotodama rows `:44-47`, no other line | `grep -n -i kotodama` | **match** — 4 rows, rounds 2/8/9/11; `grep -c 'round-33'` → 0 |
| fleet worktree clean at fleet HEAD `0b6d797` for that path | `git -C /home/vgpnk/Projects/shokunin rev-parse --short HEAD`; `status --porcelain .ufo/l0-questions.md` | **match** — `0b6d797`, zero rows |
| contract digest `5f4c02bf…`; pointers `:14` (fields) / `:16` (later-transfer compare) | `sha256sum`; `sed -n '14,16p'` | **match** — `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`; `:14` = the `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer` rule, `:15` = pending clause, `:16` = later-transfer digest compare |
| digest chain `49ac1a5→e834f503…`, `291c714→50c4c2f2…`, `e1694ba→5f4c02bf…`; last commit `e1694ba` | `git show <c>:<path> \| sha256sum` for all three; `git log -1 --format='%H %cI %s'` | **match exactly** — `e834f503…`, `50c4c2f2…`, `5f4c02bf…`; last commit `e1694bad6ac96aca45a11ca5746582b275929355` (2026-10-17T17:44:17-03:00) |
| §3 language scan: every hit a negation, mission text, quoted prior-round text, or a different-sense use | re-ran the same `grep` at `03:56:06Z` and `03:58:21Z`, inspecting every hit | **match in class** — same hit families (`claims.json:59,68`; `targets.json:51,52,55`; `op/K01-falsifier-scout.md:23,32`; `op/O01-row-drafts.md:224-225`; `adj/A16-shonen-material.md:9,29,45,69,91,116,129,153,197,203`). Counts differ only because fragments landed after A04's stamp, which A04 states as a limit |
| F-A04-1: r5/r7 receipts rewritten in place, restored byte-exact; sha256 r5 `73a66f74…`, r7 `2f4c1e15…`; clean at `03:56:01Z`; mtime `00:55:27` | `git diff`, `git hash-object`, `git show HEAD:<path> \| sha256sum`, `stat` | **match** — I measured the dirty content independently at `03:54:55Z` (live blobs `5227945d…` / `d583aad5…` ≠ HEAD `778c3f5e…` / `e7a8d449…`), the restore at mtime `2026-10-19 00:55:27.940762254 -0300`, and clean status at `03:56:01Z` and `04:03:21Z`; both restored digests equal A04's |
| F-A04-2: ` M LOG.md` is an 18-line pre-dispatch integrator append; `REGIMEN.md` untracked | `git status --porcelain` at four stamps | **match** — same three rows; no round-33 fragment claims a LOG.md write |

## 2. A05 fragment — verdict **CONFIRMED**, with one census-denominator note

| A05 check | A12 re-run | result |
|---|---|---|
| A05-1 partition name sets, empty diff both directions; only six dirs, no stray files | set-diff of `PROVINCE.md:10` brace-list vs `os.listdir('corpus/knowledge')`; per-partition `*.md` vs all-file counts | **match** — six declared, six on disk, both diffs empty; `find`-equivalent counts show every partition's file count equals its `.md` count (21/19/18/29/20/94 = 201), so no non-entry artifact is parked inside |
| A05-2 `git ls-files examples \| wc -l` → 68; NON-CANON declarations at the cited lines; foreign-domain probe → 0 | `git ls-files examples \| wc -l`; `grep -rniE '(chousa\|kake\|kotoba\|game-dev\|sibling repo)' examples/ \| wc -l`; spot-read of `examples/culture-d4/README.md:4`, `examples/culture-d3/handoff.md:20`, `examples/culture-d3/README.md:1,10-12` | **match** — 68; 0; the cited declarations are present as quoted |
| A05-3 drift classifier: verification 20 files / 132 term-lines / 125 marked / 7 residual; civilizations 94 / 369 / 359 / 10; all 17 residuals read | recount with A05's stated regex, then a word-boundary variant; independent residual pass; line-by-line read of every residual | **verdict holds; denominators partially reproduce** — loose substring matching gives verification **140** / civilizations **389** (A05: 132/369); strict word-boundary matching (`\bcanon\b` etc., which excludes "canonical"/"kotobank") gives verification **133** / civilizations **369** — civilizations exact, verification off by one. See DEF-03. My own residual pass flagged 23 lines (superset of A05's 17); I read all 23: every one is a boundary statement, a route-to-lore, a negation, or a "canonical"/"kotobank" substring use (`byzantium.md:182`, `swahili-coast.md:195`, `thrace-dacia.md:173`, `java-majapahit.md:192`, `korea-three-kingdoms-goryeo.md:133`, `persia-achaemenid.md:54`, `mesoamerica-primary-sources.md:155`, `anatolia-hittite.md:155`, `hawaii.md:85`, `balts.md:173`, `burma.md:40`, `china-tang.md:71`, `india-mughal.md:84`, `japan-heian.md:20`, `newar-nepal.md:160`, `vietnam.md:98`, `verification/calibration-registry.md:87`, `gate-frozen-run-standard.md:240`, `header-conformance-readings.md:149`, `label-channel-routing-verification.md:8`, `phonology-sanity-gate.md:128` (a Unicode `canonicalize` call in code), `to-verify-triage-protocol.md:13,52`). **Zero drift found on either census** |
| A05-4 exactly 2 out-of-repo references, both read-only | `grep -rnoE '(\.\./){3,}[A-Za-z0-9_.-]+\|/home/[A-Za-z0-9_./-]+\|~/[A-Za-z0-9_./-]+' corpus/knowledge`; `ls -la /home/vgpnk/Projects/shokunin/CORPUS.md` | **match exactly** — `verification/internal-consistency-audit.md:11` (`../../../PROVINCE.md`, resolves in-repo) and `verification/header-conformance-readings.md:4` (`/home/vgpnk/Projects/shokunin/CORPUS.md`); the file exists, 3223 bytes |
| A05-5 `git status --porcelain corpus examples` empty; partition mtimes pre-declaration; 2655 tracked paths | same commands (before and after my own instrument re-runs) | **match** — empty at both stamps; `git ls-files \| wc -l` → 2655 |
| A05-6 `python3 -B reports/round-28/readme/sweep.py` → exit 0, `rows 201 files 201`, `missing_from_index 0`, `orphan_rows 0`, footer 201 / 21-19-18-29-20-94, `readme_sha256 053966a2…` | re-ran verbatim (after confirming the script's write branch at `:257` is inside its `selftest()` temp-dir fixture builder, so the sweep run itself writes nothing — tree re-checked clean afterwards) | **match exactly** — identical readings and `readme_sha256 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`, exit 0; second instrument `tools/source-audit-inventory.py --json --summary --root corpus/knowledge` reproduces the same partition counts |

**A05's conclusion — corpus boundary intact at HEAD, zero drift, zero foreign-ownership
expansion — is confirmed.** The one difference is a denominator precision issue (DEF-03), and it
does not change the verdict: the wider census surfaces no drift line that A05's narrower one
missed.

## 3. A06 fragment — verdict **CONFIRMED**, all six §6 re-check commands reproduce

A06 ships a re-check block explicitly addressed to A12 (`adj/A06-contested.md:199-222`). Re-run
at `04:01:07Z`:

| A06 §6 command | expected | A12 result |
|---|---|---|
| (1) `sha256sum` contract + `git log -1` | `5f4c02bf…`, `e1694ba…` | **match** — both exact |
| (2) `sed -n '14,16p;127p;148p;150p;165p;209p'` | §1 gate + pending, later-transfer rule, §8 step 2 gate, integrator-ruling row, "bilateral acknowledgement is still required", contested-ownership route, division of labor | **match** — all six lines resolve at the cited numbers and say what A06's CS-1/CS-2 rows say they say |
| (3) `sha256sum` L0 + `sed -n '44,47p'` | `60ccdc9e…`, four kotodama rows | **match** |
| (4) `sed -n '14p'` packet pin | `5f4c02bf…` | **match** — `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14` |
| (5) non-absorption grep | no hit asserting a completed read/ratification/ownership transfer | **match at a later stamp** — 22 lines across 13 files at `04:01:07Z` (A06 recorded 5 pre-write / 7 post-write at `03:57–03:59Z`). I inspected all 22: every one is a restatement of the open item, an ownership label (`lore-owned`), a pointer, or the noun "ratification" naming the question (`calib/C16-receipt.md:69`, `calib/K03-open-items.md:70`, `calib/C11-item-11.md:25`, `calib/C14-fix-drafts.md:391`, `calib/C08-item-08.md:177`, `adj/A10-receipt.md:44`, `adj/A15-audit-draft.md:239-240`, `adj/K04-method-scout.md:256`, `adj/A04-bleed.md:76,87,90`, `adj/A06-contested.md:33,68,73`, `adj/A12-verify-a04-a06.md` (this file), `review/R07-adj-review.md:207`, `review/R04-calib-review.md:78`, `scribe/S02-calib-receipt.md:75`). The count grew only because fragments landed after A06's write |
| (6) stale `50c4c2f2` pointers in `examples/` | 5 hits, 3 files | **match exactly** — `examples/handoff-packet.sample.md:21`, `examples/handoff-packet.sample.yml:45,78`, `examples/culture-d3/handoff.md:27,74`; live digest `5f4c02bf…` (contract 209 lines / 28421 bytes) |

**A06's verdict — posture restated with pointers that resolve, nothing absorbed, stale-pointer
finding reproducible and unrepaired — is confirmed.**

## 4. Verification stance

- **Verified:** A04, A05 and A06 in the form their fragments present them — cited commands re-run,
  cited lines read, both fragments' own limits (point-in-time stamps, growing fragment set,
  heuristic classifier) are stated honestly rather than hidden.
- **Not verified:** A04's fleet-side `git log -p`/`-S` append-only history claims (I confirmed the
  in-repo halves of §2 and the file's present state); A05's `to-verify` items (body-prose
  truth-claims audit, the D3 control `domain-D3-CANON-canon-status-promoted`) — both are marked
  `to-verify` by A05 itself and remain open; A05-3's residual classifier is a heuristic in both
  fragments and mine (see DEF-03).
- The A04/A06/A05 row-for-row match against `A10-receipt.md` rows 28–30 is A14's remit but is
  satisfied in substance by §1–§3.

## 5. Filed defects

### A12-DEF-01 — filed round receipts rewritten in place during round 33 (breach closed by restore; attribution evidence added)

**Live window `03:54:32Z–03:55:27Z`, restored byte-exact.** Independent measurements:

| path | live mtime (UTC) | HEAD blob → dirty blob | HEAD-bytes sha256 → dirty sha256 → now |
|---|---|---|---|
| `reports/round-5/validation.json` | `03:54:32.592439623` | `778c3f5e…` → `5227945d…` | `73a66f74…` → `fe926984…` → `73a66f74…` |
| `reports/round-6/validation.json` | `03:54:32.624432831` | `9f6a0f45…` → same (byte-identical rewrite) | `32c621ef…` unchanged |
| `reports/round-7/validation.json` | `03:54:35.490143993` | `e7a8d449…` → `d583aad5…` | `2f4c1e15…` → `af0cf4ed…` → `2f4c1e15…` |

At `03:54:55Z` the worktree bytes differed from HEAD (`git hash-object` `5227945d…` /
`d583aad5…`; `git diff` printed content deltas: round 5's `O` leg error switched to a
`replay-frozen` exit-2 `gate_digest_mismatch`, its
`tested_file_sha256["tools/check-gate-battery.py"]` moved `0a126b70…` → `455b595a…`; round 7's
`failures[]` inventory line moved `189/688/700/702/633` → `201/717/731/733/655`). By `04:03:21Z`
index, HEAD and worktree are all `778c3f5e…` / `9f6a0f45…` / `e7a8d449…`, `git status` shows no
rows for any of the three, and **neither dirty blob exists in the object store**
(`git cat-file -t` → "could not get object info" for both), i.e. the dirty content was never
staged or committed.

**Mechanism:** `reports/round-5/run-validation.py:194` and `reports/round-7/run-validation.py:1171`
write their own receipt in place; neither imports `tools/harness/receipt_guard.py` (no
`receipt_guard`/`REFRESH_RECEIPTS` reference in either file), whose contract is "Only the exact
environment value REFRESH_RECEIPTS=1 permits a committed receipt" (`tools/harness/receipt_guard.py:7`;
refusal diagnostic `:147`; entry points `:152`, `:161`). The round-14 guard never fired — a
guard-adoption gap, not a guard-behaviour defect.

**Attribution evidence (integrator's call).** `.scratch/c05-tmp/{r5,r6,r7}.log` (mtime `00:54`)
hold the validators' JSON output; `.scratch/c05-iso/reports/round-5/validation.json` sha256 =
`fe926984…` — **the exact digest of the dirty live content** — so the in-place write was the
output of the same round-5 run C05 also performed in its isolated copy. `calib/C05-item-05.md:46`
documents the correct procedure (`git archive HEAD | tar -x -C .scratch/c05-iso`, then run inside
the copy) and `:96`, `:118`, `:140` name the rewrite hazard for r5/r6/r7 — the live-tree run
preceded adoption of the copy. O07 independently filed the same two rows at `03:54:59Z`
(`op/O07-baseline-receipt.md:147-177`) with byte-identical hashes to mine; A04 filed it as F-A04-1
(`adj/A04-bleed.md:107-129`). One transposition in O07 and A04: the `tested_file_sha256` change
belongs to round **5**'s receipt; round 7's delta is the `failures[]` inventory line.

**Competing explanation does not reproduce.** `calib/C05-item-05.md:330-346` reads the `M` rows as
index-vs-HEAD divergence from "a stale index, not edited filed bytes". At `04:03:21Z`
`git ls-files -s` equals `git rev-parse HEAD:` equals `git hash-object` for all three receipts, so
no stale index is present to reproduce; and an index reading cannot explain the `03:54:55Z`
content difference in the worktree bytes themselves (`git hash-object` does not consult the
index). Read C05's §6 as covering C05's own later stamp, not the `03:54:32–03:55:27Z` window.
Owner for that correction: C05/integrator.

**Consequence for claim A.** The claim-A threshold requires the scope delta to be "fully explained
by `reports/round-33/` + `REGIMEN.md`/`LOG.md` append entries" (`claims.json:63`). The breach is
closed by restore (bytes equal HEAD, digests match, status clean), so the condition can be met —
but only if A03's scope row and the assembled audit **name the window** rather than report a clean
tree, because a re-run of the round-5/round-7 validators before the close commit will clobber the
receipts again. No seat (including this one) may perform a restore: that is itself an edit of
filed round bytes.

### A12-DEF-02 — `A10-F3`'s exit-code premise is contradicted

`A10-F3` (`adj/A10-receipt.md:41`) asserts the c31 lessons-index audit "**exits 0** while reporting
failures" and derives a verification-hole risk. Measured twice:
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → `FAIL C31_index_rows_eq_files`,
`FAIL C34b_prose_arithmetic`, `findings: 2`, **exit 1** (`03:54:14Z`), reproduced without `-B` in a
fresh shell → **exit 1** (`03:57:01Z`). The tool's contract:
`reports/round-25/audit/c31-lessons-index-audit.py:460` → `return 0 if not res["findings"] else 1`.
A peer seat recorded the same: `op/O01-row-drafts.md:39` and `:191` both write `exit=1`. The
pre-fix census is red **on the exit code too**, so an integrator checking only the exit code cannot
read it green; the risk A10-F3 names does not exist as stated. Owner: A14/integrator (outside this
fragment's A04–A06 slice; recorded because this seat measured it directly).

### A12-DEF-03 — A05-3's census denominators: verification off by one (precision, verdict unchanged)

A05-3 reports `verification: files=20 term-lines=132` and `civilizations: 94 / 369`. My recount
with A05's stated regex as a loose substring match gives **140 / 389**; the word-boundary variant
(`\bcanon\b`, which excludes "canonical", "canonization", and the "kotobank" substring of
`kotoba`) gives **133 / 369** — civilizations exact, verification one higher than A05's 132. So
A05's census is a word-boundary census, and its verification denominator is off by one (candidate
causes: a compound such as `chousa-shokunin` or a `\bkake\b`-style boundary difference; exact
cause `to-verify`). **Verdict unchanged:** my wider pass (23 residuals, superset of A05's 17) was
read line-by-line and found zero drift — the lines A05's narrower census does not count are
"canonical"/"kotobank" substring uses and boundary statements. Integrator: if the counts are
restated in `adj/audit-assembled.md`, restate them as word-boundary counts, or re-run A05's exact
census command (not recorded verbatim in the fragment) to reconcile the one line.

## Owed

Nothing owed by this seat's mission: all three A04–A06 fragments have landed and are verified
above. Remaining, owned by others:
- A05's two `to-verify` items (body-prose truth-claim audit; the D3 negative control
  `domain-D3-CANON-canon-status-promoted`) — A05's own open items.
- A05-3 verification denominator reconciliation (DEF-03) — integrator, only if the counts are
  restated.
- Post-wave completeness re-run of the A04/A06 language scans once all fragments are frozen —
  A08/integrator; §1/§3 record the same hit classes at later stamps, so this is completeness, not
  contradiction.

## Citations

- `reports/round-33/targets.json:5-11,51-53,55,59`; `reports/round-33/claims.json:6,8,18,59,63,66,68`
- Verified fragments: `reports/round-33/adj/A04-bleed.md:1-129`; `adj/A05-corpus.md:1-260`; `adj/A06-contested.md:1-222`
- `reports/round-33/adj/A10-receipt.md:28-30,41,43,63-65`; `reports/round-33/op/O07-baseline-receipt.md:17,147-177`;
  `reports/round-33/op/O01-row-drafts.md:39,191`; `reports/round-33/calib/C05-item-05.md:46,96,118,140,330-346`
- `PROVINCE.md:9-14,16-25,27-31`; `AGENTS.md:13`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:14-16,127,148,150,165,209` (209 lines, 28421 bytes, sha256 `5f4c02bf…`)
- `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`; `reports/round-30/handoff/declared-in-r6/packet.md:14`
- `reports/round-32/dossier-d13-operator-decisions.md:135`; `SCORECARD.md:124,130-131`
- `reports/round-5/run-validation.py:194`; `reports/round-7/run-validation.py:1171`; `tools/harness/receipt_guard.py:7,147,152,161`;
  `reports/round-28/readme/sweep.py:240-262` (write branch confined to the selftest fixture)
- `reports/round-25/audit/c31-lessons-index-audit.py:460`
- `corpus/knowledge/verification/{provenance-audit-ledger-format.md:15, verification-method-overview.md:206, to-verify-triage-protocol.md:13,52,
  phonology-sanity-gate.md:128, calibration-registry.md:87, gate-frozen-run-standard.md:240, header-conformance-readings.md:4,149,
  label-channel-routing-verification.md:8, internal-consistency-audit.md:11}`;
  `corpus/knowledge/civilizations/{byzantium.md:182, swahili-coast.md:195, thrace-dacia.md:173, java-majapahit.md:192, korea-three-kingdoms-goryeo.md:133,
  persia-achaemenid.md:54, mesoamerica-primary-sources.md:155, anatolia-hittite.md:155, hawaii.md:85, balts.md:173, burma.md:40, china-tang.md:71,
  india-mughal.md:84, japan-heian.md:20, newar-nepal.md:160, vietnam.md:98}` (the residual set I read)
- `examples/culture-d4/README.md:4`; `examples/culture-d3/README.md:1,10-12`; `examples/culture-d3/handoff.md:20,27,74`;
  `examples/handoff-packet.sample.md:3,15,21`; `examples/handoff-packet.sample.yml:1,45,70-71,78`
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44-47`; fleet `git -C /home/vgpnk/Projects/shokunin` HEAD `0b6d797`;
  `/home/vgpnk/Projects/shokunin/CORPUS.md` (3223 bytes)
- Commands (lane root, `TMPDIR=$PWD/.scratch`, read-only, `2026-10-19T03:52Z–04:06Z`):
  `git rev-parse HEAD`; `git status --porcelain` (×5 stamps, incl. `-- corpus examples`); `git ls-files -s`; `git hash-object`;
  `git rev-parse HEAD:<path>`; `git show HEAD:<path> | sha256sum`; `git cat-file -t <blob>` (both dirty blobs absent);
  `git diff` / `--stat` / `-U0` on `reports/round-{5,7}/validation.json`; `git show <commit>:<path> | sha256sum` for `49ac1a5`,`291c714`,`e1694ba`;
  `git log -1 --format='%H %cI %s' -- <path>`; `stat -c '%n %s %y'`; `sha256sum` on the contract, `PROVINCE.md`, the two receipts, `corpus/README.md`, `corpus/QUALITY.md`, and the L0 file;
  `wc -c -l`; `sed -n` on the contract, L0, and every cited corpus line above; `ls corpus/knowledge/*/`; `ls corpus/lessons/*.md | wc -l`;
  `find corpus/knowledge -type f ! -name '*.md'`; `git ls-files examples | wc -l` (68); `git ls-files | wc -l` (2655);
  `grep -rniE '(chousa|kake|kotoba|game-dev|sibling repo)' examples/ | wc -l` (0);
  `grep -rnoE '(\.\./){3,}…|/home/…|~/…' corpus/knowledge` (2 hits);
  `grep -rn -i -E 'bilateral (same-revision )?read (is|as) (closed|complete|done|acknowledged)|ratif(y|ied|ication)[^a-z]' reports/round-33/` (22 lines, all inspected);
  `grep -rn "50c4c2f2" examples/…` (5 hits); `grep -rn -iE 'promotion|canon|clearance|closure' reports/round-33/` + classification (×3 stamps);
  python recount of term-lines (loose 140/389, word-boundary 133/369) and independent residual pass (23 lines, all read);
  `python3 -B reports/round-28/readme/sweep.py` (exit 0); `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 1, ×2); `date -u '+%Y-%m-%dT%H:%M:%SZ'`
