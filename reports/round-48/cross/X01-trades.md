# X01 — trades critic, round 48

- Seat: `X01` | role: **critic** | claim: **cross** (`reports/round-48/targets.json:42`)
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`a01405d`) — `git rev-parse HEAD` at every read in this seat; equal to `reports/round-48/claims.json:7`.
- Out path: `reports/round-48/cross/X01-trades.md` (the only file this seat writes).
- Observation window: `2026-10-19T19:38Z–19:45Z` (UTC, `date -u`). The wave was live; fragments landed while this seat read. §0 binds the first read, §8 the post-cut spot-check.
- Method: read `claims.json`, `targets.json`, the r47 filed review/validation/queue records, and the r48 fragments present at the window; re-ran the measurements myself (census, sweep, in-memory sweep variants, README line map, queue-JSON parse, digest checks). No filed byte edited; nothing staged under `corpus/`; no `reports/round-*/run-validation.py` executed; no git mutation, install or network.
- Citation convention: bare `claims.json` / `targets.json` resolve to `reports/round-48/`; `X00`/`N01`/`K02` to `reports/round-48/{cross,scout}/`; `R03`/`Q01`/`C07`/`C09`/`C11`/`C05` to the r47 files named in the text. A bare `:NN` continuation binds to the last full path.

**One-line result.** No landed harm yet — `git status --porcelain` shows no modified tracked file and corpus holds at 223 — and the two live C/Ca premises are true. The trades are in the **acceptance surface**: C's length ceiling is a soft 250 that sits inside the very band that failed to stop r47; the sweep cannot certify either claim's distinctive leg (prose vector, H1 count), and Ca's own counting command is a runner this round forbids; the over-build row's durable `reason` carries a false causal clause and re-codifies the soft length number; and a second duplicate structural header (`revision: 2.0`) survives the Ca fix unmentioned. Fix the gates before apply; do not fix the prose after.

---

## 0. State at this read (digest-bound)

Present and read (sha256, full):

| artifact | sha256 |
|---|---|
| `corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| `reports/round-48/claims.json` | `bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292` |
| `reports/round-48/targets.json` | `d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446` |
| `reports/round-48/cross/X00-connector.md` | `a80734f45f8bf09d49974b1c3378db655af82883b26e6d04b3483ec83862bd8a` |
| `reports/round-48/cross/N01-numbers.md` | `35c2e2de0419e4bada02290121b65097d46ef46cad6f868f795e17f42b9b89a0` |
| `reports/round-48/scout/K02-readme-defect.md` | `ef2102115da03c8332b305fc3a22c350fd6eb428efde415aa12dfd44096dfd7a` |
| `reports/round-48/calib/Ca03-readme-verify.md` | `593e404a2f0b57963e1cc829650e7ac1fa577ef2390d86c8c060ff172749d457` |
| `reports/round-48/calib/Ca05-heading-control.md` | `8114ec00c0179f0367c68c4a79fca2759da9fea2638aa9cc8f64687606faa8eb` |
| `reports/round-48/cov/C02-header.md` | `5356f0b1d2427c7ecfdcb1527930e8ab6fd5fb354f27657da2d57984892658a0` |
| `reports/round-48/cov/M01-example.md` | `04edaa4519b2d2f053dc1feefce9526ae9b27ef1b667211e63e64f312f08aaf1` |

The `claims.json`/`targets.json` digests equal the declaration pins in `reports/round-48/telemetry/dispatch-declared.json:15-16` — no contract drift at my cut.

Absent at this read (so any verdict depending on them is **could-not-evaluate**, never inferred green): `run-validation.py`; `cov/C01`, `C03`, `C05`, `C10`, `C11`, `C12`–`C18`; `cov/V01`; `calib/Ca01`, `Ca02`, `Ca04`, `Ca06`, `Ca07`; `calib/N02`; `review/R01`–`R05`; `cross/Q01`, `X03`, `F01`; `plan/P01`; `scribe/S01`.

---

## 1. Trade register

| # | suspected trade | verdict at this cut | strongest evidence |
|---|---|---|---|
| **T1** | C re-lands an "over-built" entry under a softer number | **OPEN — threshold cannot block** | `<=~250` (`claims.json:31,38`; `targets.json:10`) vs live cm max **221** and median **149**: 250 is **1.13×** the max and **1.68×** the median (§2.1) |
| **T2** | "audits PASS" certifies a draft that is not the landed bytes | **OPEN — no digest gate yet** | r47's chain was pinned to superseded bytes (`reports/round-47/cross/Q01-final-gate.md:118`); r48 assigns 16 C verifier seats (+2 non-author readers) but no mission requires an artifact digest (§2.2) |
| **T3** | the rev-2.5 arithmetic instruction conflates the repair target (223) with the new total (224) | **CONFIRMED contract defect** | `targets.json:28` says "synthesis 25->29, myth-symbol 23->26, culture-material 26->25 = 224"; those deltas give **223** (§2.3) |
| **T4** | a green sweep is used to certify the prose vector / H1 count | **CONFIRMED blind spot** | in-memory demonstration: wrong vector and H1=2 both return `ok=True` (§3.1) |
| **T5** | Ca's counting command is a forbidden runner | **CONFIRMED contract defect** | `claims.json:49` = `python3 reports/round-48/run-validation.py`; `targets.json:8` forbids it and the file is absent (§3.2) |
| **T6** | the Ca fix leaves a second duplicate structural header | **CONFIRMED live defect, out of claim scope** | `revision: 2.0` at `corpus/README.md:42` **and** `:44`; line 42 is a dangling half-paragraph (§3.3) |
| **T7** | the over-build disposition's durable `reason` misstates the audit history and re-codifies the soft length number | **CONFIRMED in the landed Ca02 row; chain risk closed** | `Ca02:112` says "no audit ran on the assembled bytes" (false: R03 reviewed them, `R03:12-20`, and C11 ran the checker, `C11:76`); `Ca02:113` repeats `<=~250`; chain is correct at `Ca02:88-95` / `N02:215-216` (§3.4, §8) |
| **T8** | the C and Ca README edits break each other's line anchors | **CONFIRMED trap** | H1 removal −2, then row insertion +1: totals `544→543`, vector `548→547`, cm header `234→232` (§4) |
| **T9** | a seat "adds the leg to sweep.py" and edits filed bytes | **CONFIRMED wording defect in X00** | `X00:267` offers "(a) add the leg to `sweep.py`"; `reports/round-28/**` is filed and immutable; Ca05 has the compliant route (§3.5) |
| **T10** | a verifier certifies an unaudited draft (digest drift) | **OPEN — gate defined, not yet in any mission** | §2.2 / G2 |

---

## 2. C — coverage: three ways the landing can repeat r47 without its line count

### 2.1 T1 — the length ceiling is not the partition discipline

Measured at `a01405d`:

```
$ wc -l corpus/knowledge/culture-material/*.md | tail -1
3756 total                     # 25 files
min 103  median 149  max 221  mean 150.24
250/221 = 1.13      250/149 = 1.68      790/221 = 3.57
```

The claim calls `<=~250` "the partition discipline" (`claims.json:38`) while stating in the same claim that the live max is **221** (`claims.json:29`). That is not a tight cap with a tolerance; it authorizes the new entry to become the **longest file in the partition by 13%**. Two consequences:

1. **The number is not falsifiable.** `~250` plus "not a hard cap" means C05 can report 255 and pass under the tilde, and the integrator has no failure condition. r47's block did not come from a missing check — C07's checker existed, but encoded length as `warn(...)`, not a fail (`reports/round-47/cov/C07-contract-audit.md:354`), and C11's receipt promoted it to `FAIL length in partition band: 854 lines` only after reading it (`reports/round-47/cov/C11-scribe.md:76`). **A check whose default severity is WARN is not a gate.** r48 replaces a 260-line WARN ceiling with a 250-line "not a hard cap" — the severity class has not changed.
2. **It recalibrates the partition by precedent.** The next scout will cite "the r48 cartography entry at 247 lines" as a normal entry, and the median moves. Coverage +1 bought with a new partition maximum is an axis trade: one entry gained, the length norm lost.

**Required before apply.** One of two, recorded:
- **(a) hard ceiling 221** on the assembled entry including the head block, target `<=200`; or
- **(b) an explicit integrator exception** naming why 222–250 is acceptable for this entry, filed before assembly and cited by C05/X03.

Either way the check must run on the **assembled fenced body including the head**, not per fragment. r47's volume was 739 body + 51 head = 790 (`Q01:87`); a body-only count understates by the head. C05 reports both numbers and the sum. C17's structure diff must name which r47 sections were cut and which kept; a cut that removes a **decision table** to make the number is the wrong cut (r47's P2-3 named duplicated bullets and restated mechanisms, `R03:92-96`).

### 2.2 T2 — "audits PASS" is only as good as its digest

r47's chain failed on exactly this: the final gate read superseded assembly bytes (`Q01:118`: "C06 source … **superseded** — must re-run"). r48 assigns 16 claim-C verifier seats (C03–C09, C11–C12, C14–C18, V01, N03) plus two non-author readers (R03, X03), and no mission requires a digest. A verifier can judge an early draft, the draft can be revised, and the round can still file "audits PASS".

**Required field in every C verifier fragment** (C03, C04, C05, C06, C07, C08, C09, C11, C12, C14, C15, C16, C17, C18, V01, N03, R03, X03):

```
artifact: <path or "assembled fenced body">
artifact_sha256: <64 hex>
```

and one seat (C13, then Q01) must prove they are the same bytes:

```
$ grep -h '^artifact_sha256:' reports/round-48/cov/*.md reports/round-48/review/*.md \
    | awk '{print $2}' | sort | uniq -c
# expect exactly one digest, repeated, equal to the extracted body's sha256sum
```

A verifier that cannot name a digest is `could-not-evaluate`, not PASS. This is the only gate that makes "audits clean" (`claims.json:38`) a measurement rather than an adjective.

### 2.3 T3 — the arithmetic instruction produces 223, not 224

`targets.json:28` says: "repair the rev-2.4 prose-vector (synthesis 25->29, myth-symbol 23->26, culture-material 26->25 = 224)".

```
live rev-2.4 after-vector: 25/23/26/25/24/94 = 217
apply the three stated deltas: 25/26/25/29/24/94 = 223   <- the rev-2.4 repair
add the new culture-material entry: 25/26/26/29/24/94 = 224   <- the rev-2.5 vector
```

The three deltas repair **rev 2.4 to 223**. The `= 224` belongs to the **rev 2.5** vector after the +1. As written, the instruction merges the two records; a seat following it can either print 223 in the rev-2.5 block (fails the claim's "sums 224") or print 224 in the repaired rev-2.4 block (falsifies the historical record by making it include an entry that had not landed).

**Required wording, three distinct numbers:**

| surface | value | sum |
|---|---|---|
| rev-2.4 repaired line (`corpus/README.md:11`) | `25/26/25/29/24/94` | 223 |
| rev-2.5 new block | `25/26/26/29/24/94` | 224 |
| counts footer (`:548` pre-edit) | `25/26/26/29/24/94` | 224 |

And the rev-2.5 block must **quote the defective reading** (`25/23/26/25/24/94`, sums 217) so the repair is a recorded correction, not a silent history rewrite. This is the r47 C09 form (`reports/round-47/cov/C09-readme.md:92-97`); K02 independently reaches it (`K02-readme-defect.md:212`). Do not copy the r47 slot-swapped vector `26/26/25/29/24/94` (`reports/round-47/cov/C05-freshness.md:275,295`), which puts the culture-material +1 in the first slot.

### 2.4 What I verified as good (so the critique is bounded)

- M01's worked example states one update rule in one cell, tags all nine moves to `DR-CT-01..09`, and its only arithmetic is correct: `1:2,500` → `1 mm × 2,500 = 2,500 mm = 2.5 m` (`M01-example.md:38`, self-check `:87`). The r47 B7 strings (`after any storm`, `per levy year`, `not due until`) return 0 (`M01:77-78`).
- C02's head block is 23 lines and carries the r47 header fixes: B2 (`cartograph` = 2 files / 2 lines), B3 (quote verbatim), B4 (`:54-65`), B8 (`cosmography:27`) (`C02-header.md:8`).
- Ownership is clean at `a01405d`: 0 filename owners, 0 topic owners, slug absent (`C02-header.md:28-62`; my §7 commands).

None of these closes T1/T2: a right-sized, well-sourced entry can still be 250 lines and audited on stale bytes.

---

## 3. Ca — calibration: the fix is real; the acceptance surface is not

### 3.1 T4 — the sweep is green on both defects; only a separate control can see them

Measured by importing the filed sweep as a module and passing README text (no repo write):

```
live README                          ok=True   rows 223   H1=2
delete lines 3-4 (second H1 + blank) ok=True   rows 223   H1=1   totals line -> 542
add a rev-2.5 note with the WRONG vector (25/26/25/29/24/94)  ok=True
add a rev-2.5 note with the right vector (25/26/26/29/24/94)  ok=True
```

The sweep's `ok` is built from rows/ghosts/topics/section headers/totals/footer only (`reports/round-28/readme/sweep.py:191-194`); it never parses revision prose and has no `^# ` leg. Therefore:

- C's "prose vector sums 224" (`claims.json:38`) has **no counting command** in the claim. C11's mission says to "confirm … prose vector sums 224" (`targets.json:29`), but a seat can print the string and assert the sum; nothing recomputes it.
- Ca's "heading count 2→1" is measured by `grep -c`, not the sweep — fine, but the round must not file "sweep green" as the certificate for it.

**Required.** C11 prints the six numbers and their sum from the **first (newest) revision block only**, and Q01 recomputes. A compact check:

```
python3 - <<'PY'
import re
t=open('corpus/README.md',encoding='utf-8').read()
block=re.split(r'\n\s*\n', t.split('\n',1)[1], maxsplit=1)[0]  # first paragraph after H1
v=[int(x) for x in re.search(r'(\d+/\d+/\d+/\d+/\d+/\d+)', block).group(1).split('/')]
print(v, sum(v))
PY
# rev 2.5 must print [25, 26, 26, 29, 24, 94] 224
```

Ca05's `tools/check-readme-heading.py` covers the H1 leg; it is the right shape (new sibling instrument, 8/8 selftest, red on live, green on staged). Do not extend the filed sweep (T9).

### 3.2 T5 — Ca's third counting command is forbidden and absent

`claims.json:49`:

```
python3 reports/round-48/run-validation.py
```

- `reports/round-48/run-validation.py` does not exist at seat time (`ls` → No such file or directory), so the command is a guaranteed exit 2.
- The round's shared rules say: "**ABSOLUTE: never run reports/round-*/run-validation.py in-tree**" (`targets.json:8`). A seat that follows the claim's counting command violates the round's own rule; a seat that refuses cannot satisfy the claim as written.

**Required.** Replace the third command with compliant, runnable legs:

```
grep -c '^# kotodama-shokunin corpus index' corpus/README.md    # expect 1
python3 -B tools/check-readme-heading.py corpus/README.md        # expect exit 0
python3 -B reports/round-28/readme/sweep.py                      # expect exit 0, 224 == 224
python3 -c "import json;json.load(open('reports/round-48/calib/queue-successor-r48.json'))"
```

The integrator may run the round runner at close as the round's own receipt; the **claim's** acceptance surface must not depend on it.

### 3.3 T6 — a second duplicate structural header survives the fix

Not in the claim, measured live:

```
$ grep -n '^revision: 2.0' corpus/README.md
42:revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
44:revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
$ sed -n '42,44p' corpus/README.md
revision: 2.0 — … the ten
(blank)
revision: 2.0 — … the ten
round-35 entries landed — …
```

Line 42 is a dangling duplicate of the line-44 header with no body. N01 flagged it independently (`N01-numbers.md:14`). The Ca fix (H1 only) leaves it; the sweep does not parse it; Ca05's `HEADING-DUP` rule checks headings, not prose labels, so it will not report it either.

**Disposition required, one of:**
- **(a) fix in the same recorded act:** delete lines 42–43 (the dangling label and its blank). Then README is 571 lines; with C's row the final map is totals `541`, vector `545`, cm header `230`. The Ca claim's `after_required` must name the extra edit, and Ca03/R04 must read the diff.
- **(b) leave it, record it:** a queue row or a `to-verify` with owner (integrator) and next_touch, and an explicit sentence in Ca's receipt that the heading control does **not** cover duplicate revision labels.

What must not happen: filing "README integrity" as fixed while a duplicate revision label remains and the control is described as complete.

### 3.4 T7 — the over-build row: audit history, soft gate, and a chain that must stay pinned

The r47 successor is already filed and validated: `reports/round-47/calib/queue-successor-r47.json`, sha256 `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58`, 3 defect rows + 2 provider amendments, none of them the over-build (row ids: `r43-stale-premises`, `r44-resolver-hyphen-after-blank`, `manifest-ledger-two-schema-evolution`). It pins the parent `reports/round-40/op/defect-queue-v2.json` at `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`.

**Four checks on the row as landed in `Ca02-overbuild.md` (sha256 `2feb3a45…07cbd`, read after my first cut) — one closed by that fragment, one withdrawn in part, two confirmed:**

1. **Predecessor chain.** The lane convention is `parent` = the r40 root plus `predecessor_successor` = the prior delta (r47's own successor does exactly this for r43). A successor that names only the root and no predecessor is the fork. The r48 file must carry:
   ```
   "parent": "reports/round-40/op/defect-queue-v2.json",
   "parent_sha256_at_assembly": "dfc9265d…253907",
   "predecessor_successor": {"path": "reports/round-47/calib/queue-successor-r47.json",
                             "sha256": "9508b6aa…fece58"},
   "parent_bytes_edited": false
   ```
   As landed, Ca02 names the r47 successor with its digest (`Ca02:88-95`) and N02 asserts both (`N02:215-216`), so the fork risk is **closed at draft level**. What remains is the mission wording: `targets.json:69` checks only the r40 pin; the applied check must keep N02's predecessor leg, or a future successor can drop it and still pass.
2. **Owner vs cause (withdrawn in part).** Under the v2 schema `owner` is the actor for the next touch, so `owner: r48 C drafter + integrator` (`Ca02:111`) is schema-correct; I withdraw "it blames the drafters" as a reading of that field. The problem is the `reason` (`Ca02:112`): it says the entry was "drafted outside the partition's length discipline", but the r47 dispatch carried no length condition (`reports/round-47/claims.json:26`) and assigned 15 sections (`reports/round-47/targets.json:21-23`). The reason should name the dispatch surface as cause and the drafter as actor.
3. **Class phrase — now confirmed in the landed row.** The claim's "unreviewed arithmetic/citation defects" (`claims.json:43`, `targets.json:34`) becomes, in Ca02, "no audit ran on the assembled bytes" (`Ca02:112`). That is false as filed: R03 reviewed the assembled body (fragment table `R03:12-20`, depth judgment `:68-98`) and C11 ran C07's checker on the assembled 854 (`C11:76`). The accurate class is narrower: author-side audit rows certified wrong anchors (B4, `R03:191`), the final source audit was pinned to superseded bytes (`Q01:118`), and the assembled-length FAIL carried WARN severity. The durable row must not carry "no audit ran".
4. **The gate repeats the soft number.** X00's `next_touch` (a) is `wc -l … <=~250` (`X00:222`), and Ca02's `next_touch` codifies "the round's stated tolerance is <=~250 lines" (`Ca02:113`). Same T1 defect one layer down. It must be the hard ceiling chosen in §2.1, or it cannot reclass.

Class `routed-with-owner` is correct; `verification: null` is honest at draft time; no `fixed-with-evidence` row may be minted for this item in r48 (the r47 successor's G5 discipline, `queue-successor-r47.json` `application_gates` G5).

### 3.5 T9 — the heading control cannot be added to the filed sweep

`X00:267` offers "(a) add the leg to `sweep.py`". `reports/round-28/readme/sweep.py` is a filed round artifact (`git ls-files` confirms tracked; the shared rule freezes `reports/round-1..47/**`, `targets.json:6`). Editing it is the thing this round forbids. Ca05 already has the compliant route: a new sibling instrument `tools/check-readme-heading.py`, fenced for the integrator (`Ca05:1-80`), plus the same "do not edit the sweep" finding K02 recorded (`K02-readme-defect.md:227`).

**Required.** Delete option (a) from any landing wire (W02) and from X00's framing. The integrator may add a **successor copy** of the sweep under `tools/` if a single certificate is wanted, but the filed instrument and its selftest stay byte-identical.

---

## 4. T8 — one README, two claims, three line shifts

Both claims edit `corpus/README.md`; neither seat may stage it. The edits shift line numbers in opposite directions and at different points. Measured on the live bytes (in-memory, no write):

| anchor | pre | after H1 fix (−2) | after H1 fix + C row (+1) |
|---|---:|---:|---:|
| `revision: 2.4` block | 5 | 3 | 3 + (rev-2.5 block length) |
| rev-2.4 vector line | 11 | 9 | 9 + (block length) |
| `## culture-material/ (25)` | 234 | 232 | 232 |
| calendar row | 240 | 238 | 238 |
| **cartography row** | — | — | **239** |
| `## synthesis/ (29)` | 261 | 259 | 260 |
| `Total knowledge entries: 223.` | 544 | 542 | **543** |
| `(total 223 files; directory totals …)` | 548 | 546 | **547** |

Consequences for the apply:

1. **Do not reuse pre-edit numbers.** `corpus/README.md:544` and `:548` are correct **now** (N01/C04/K02 cite them correctly); after both edits they are `:543` and `:547`. Any r48 fragment that writes a post-edit citation from the pre-edit map is a miscite of the r47 class, even though the pre-edit number was right when measured.
2. **Apply by content anchor, not line number.** Generate the diff against post-H1-fix bytes, or perform both edits as one atomic write. X00 §8 says the same (`X00:277-288`); K02 says Ca first (`K02:163-169`). The two blank-line variants of the H1 deletion (lines 2–3 vs 3–4) are byte-identical post-states because both remaining lines are blanks — either is fine, but the wire must name one.
3. **Record before/after digests.** Expected post-state: README `d407260d…b3190079` after the H1 fix alone (573 lines, measured by Ca03 `:109-115`); after the full C+Ca landing the digest is a new value and only the post-apply `sha256sum` may be filed. The sweep prints `readme_sha256`; C11/W02 must quote it rather than predict it.
4. **The heading control must run after the atomic write**, not between the two edits; otherwise it reports a mid-state.

---

## 5. Gates that close the trades

**G1 — hard length.** Extract the assembled fenced body (the M01/C02 method) and `wc -l` it **including the head block**. Pass at **≤221** (or a filed exception naming 222–250). Closes T1.

**G2 — audit digest.** Every C verifier names `artifact_sha256`; the set of declared digests collapses to exactly one value, equal to the assembled body's `sha256sum`; Q01 re-hashes. A missing digest is `could-not-evaluate`, not PASS. Closes T2/T10.

**G3 — vector arithmetic.** First revision block's six numbers sum to **224**; rev-2.4 line sums to **223**; footer sums to **224**; each printed with its sum in C11 and recomputed by Q01. Closes T3/T4.

**G4 — runnable Ca surface.** No `run-validation.py` in any claim's counting commands; the four compliant commands exit as stated. Closes T5.

**G5 — duplicate-label disposition.** `grep -c '^revision: 2.0' corpus/README.md` = 1 (fixed) **or** a queue/`to-verify` row with owner, and the receipt says the heading control does not cover it. Closes T6.

**G6 — chain integrity.** New successor parses; `parent_sha256` = `dfc9265d…`; `predecessor_successor.sha256` = `9508b6aa…`; r43/r47/r40 digests unchanged; no `fixed-with-evidence` row. Closes T7 (chain).

**G7 — wording.** The row's `reason` names the dispatch surface, not drafter negligence; the claim's "unreviewed" is replaced with the R03 B4 / Q01:118 facts. Closes T7 (class).

**G8 — no filed sweep edit.** `git diff --name-only reports/round-28/` empty; the new control is `tools/check-readme-heading.py`. Closes T9.

**G9 — post-apply line map.** `grep -n` of totals/vector/section header equals §4's post map (`543/547/232`), or the receipt explains the delta. Meanwhile `grep -c '^# ' corpus/README.md` = 1. Closes T8.

G1–G9 are cheap; each is one command and a pasted output. A round that files "audits clean" without G2 is filing an adjective.

---

## 6. Could-not-evaluate at this cut

- **The C entry body.** No assembled draft existed at 19:41Z; C01/C03 and the body seats had not filed. T1/T2 are threshold and gate findings, not content findings. R03/C12/X03 must judge depth per line on final bytes.
- **The Ca successor file.** `calib/queue-successor-r48.json` and Ca02/Ca06 had not filed; T7 is a review of X00's proposed row, which is the design the Ca seats are likely to follow.
- **The landing.** Nothing under `corpus/` changed (`git status --porcelain` → only `?? reports/round-46/review/`, `?? reports/round-48/`). V01/F01/A04 are the delivery certificates; this file is a pre-apply critique.
- **C's arithmetic beyond M01/C02.** I verified the worked example's 1:2,500 conversion and the head's cited anchors at the level the seats declared; C03/C04 own exhaustive recomputation.

---

## 7. Commands run (appendix)

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD                          -> a01405dd36367292255c2652ac0a601f4cd6a0af
git status --porcelain                      -> ?? reports/round-46/review/ ; ?? reports/round-48/
date -u                                     -> 2026-10-19T19:40:55Z
find corpus/knowledge -name '*.md' | wc -l  -> 223
ls corpus/knowledge/culture-material/*.md | wc -l -> 25
python3 -B reports/round-28/readme/sweep.py -> rows 223 files 223, footer_ok True, exit 0,
                                               readme_sha256 7c788a1d…cdcd
grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2 (lines 1, 3)
grep -c '^revision:' corpus/README.md       -> 12 labels; 2.0 twice (:42, :44)
grep -n '\b223\b' corpus/README.md          -> :10, :12, :544, :548
python3 - <<'PY'  (importlib load of the filed sweep; sweep(text) on four variants)
  live                       ok=True H1=2 totals=544
  delete lines 3-4           ok=True H1=1 totals=542
  rev note, wrong vector     ok=True
  rev note, right vector     ok=True
PY
python3 - <<'PY'  (line map after H1 -2 and row +1)
  totals 544->543 ; vector 548->547 ; cm header 234->232 ; new row 239
PY
sha256sum reports/round-40/op/defect-queue-v2.json                  -> dfc9265d…253907
sha256sum reports/round-43/calib/defect-queue-v2-successor-r43.json -> 77f9d63e…7dad38
sha256sum reports/round-47/calib/queue-successor-r47.json           -> 9508b6aa…fece58
python3 -c "import json; d=json.load(open('reports/round-47/calib/queue-successor-r47.json')); print([r['id'] for r in d['rows']])"
  -> ['r43-stale-premises', 'r44-resolver-hyphen-after-blank', 'manifest-ledger-two-schema-evolution']
ls reports/round-48/run-validation.py       -> No such file or directory
```

**Write-surface statement.** This seat wrote only `reports/round-48/cross/X01-trades.md`. No tracked file modified; no corpus byte written or staged; no filed round edited; no `run-validation.py` executed; no git commit/push/install/network. The in-memory sweep runs imported the filed instrument and passed README text as an argument; nothing under `reports/round-28/` changed.

---

## 8. Post-cut addendum (19:44–19:45Z)

Three fragments landed after §0's read; digests at this addendum: `cov/C10-readme.md` `049f17cb…ec68c`, `calib/Ca02-overbuild.md` `2feb3a45…07cbd`, `calib/N02-integrity.md` `4750f574…6f1f7`. Spot-check only, not a full review.

- **C10 converges with G3.** It repairs the rev-2.4 token to `25/26/25/29/24/94`, quotes the 217 reading with the slot diagnosis, and writes the rev-2.5 block and footer as `25/26/26/29/24/94` (`C10:98-105`, `:145-146`). It also supplies both order variants around Ca01's H1 removal, which is the §4 requirement. Still open: the sum is printed, not recomputed by a command; G3's executable leg remains C11/Q01's.
- **Ca02/N02 close the chain risk** (§3.4 item 1): `parent` r40 + `predecessor_successor` r47/`9508b6aa`, both re-hashed (`Ca02:88-95`, `N02:215-216`). N02-F2 asks for the missing `parent_sha256_recheck_after_assembly`, `provenance` and `source_fragments` fields (`N02:191`); apply them.
- **Ca02's `reason` carries the false "no audit ran on the assembled bytes" clause** (§3.4 item 3). This is the one durable-record error to fix before apply: R03 reviewed assembled sections and C11 ran the checker on the assembly. Replace the clause; keep the B1–B9 list.
- **C05 has not filed.** `ls reports/round-48/cov/C05*` → no match at 19:45Z, so G1 is unexecuted and the §2.1 threshold question is still open.
- **No fragment declares `artifact_sha256`.** `grep -rln 'artifact_sha256' reports/round-48` returns only this file. T2/T10 remain unaddressed by the seats.

The addendum does not change §6's landing verdict: nothing under `corpus/` has changed; the delivery certificate remains the post-apply sweep plus V01/F01.
