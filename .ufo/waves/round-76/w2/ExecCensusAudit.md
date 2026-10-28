# ExecCensusAudit — round 76, wave 2 falsification (committed census receipts + mirror validation receipt)

Seat: ExecCensusAudit (leaf executor). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Read-only audit. No census was run, no build/test/lint/formatter was executed, no source file was
modified, nothing was committed or pushed, no tool was installed (pacman untouched — no install was
expected for a read-only falsification wave).

Revisions read (committed blobs only, never the mutable worktree):
base `98c486bdb4650ba5b8e651d332910e8ee60ad121` · freeze `df0f0309d61e5485bb17035d3f8791b1e6a11d40`
· Ca landing `a43ed807ea38b5fc5a7875a839d576cea73aba7c` · C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a`.

## 0. Verdict

**The end validate exits cleanly — exit 0, zero `E01`–`E12` lines — and the exact row/tier/status
counts are 820 / A 493 B 311 C 16 / mined 725 queued 58 rejected 37 at the C landing.** Those
counts are *not* in the committed end census receipt: `census-end.txt` is a validate-only output.
The counts exist in the committed mirror validation receipt
(`.ufo/waves/round-76/assimilation/validate-receipt.txt`) and match, byte-for-byte, my independent
re-derivation from the committed C-landing registry blob.

**Falsification result: the census layer holds, but four evidence-hygiene defects sit around it**
(F1–F4 below). None of them is an E-code; all four are receipts that do not say what their name
implies, or attest a scratch artifact that is not the landed artifact.

| # | finding | severity | verdict on the claim itself |
|---|---|---|---|
| F1 | `census-start.txt` and `census-end.txt` carry **no** row/tier/status counts and **no** command echo, date, revision or clean-worktree pin — the lane's own `claims.json` admits "817 rows rederived separately" | medium | counts are correct, but un-attested by the receipts the name points at |
| F2 | the only committed census **count** block measures a scratch **mirror**, whose `SOURCES.md` and knowledge entry are **not** the landed bytes (11-line diff; entry copy calls S896 "tier-A" where the landed entry and row say tier B) | medium | landed counts independently confirmed; the mirror's artifact is stale |
| F3 | the mirror receipt's seven `MANUAL` commands use the **relative** path `corpus/SOURCES.md` with no stated cwd, so it is undecidable whether they ran in the mirror or the lane | medium | same numbers either way; provenance ambiguous |
| F4 | the mirror receipt header ("live lane SOURCES.md has not yet been appended") is **false at the commit that carries it** (`cab5247` appends S894–S896 in that same commit) | low | self-consistency defect only |

No finding contradicts the frozen numbers `817 → 820`, `A +2 B +1`, `252 → 253` knowledge files.

## 1. The three committed receipts, exactly

### 1.1 Start census receipt — `reports/round-76/telemetry/census-start.txt`

Committed at `b4965d5` (round-76 freeze), unchanged through `722e69f`. 34 lines. Content, verbatim
shape:

* lines 1–28 — 28 `W04` lines (`kotodama\tW04\tS### duplicate url … across scopes`), rows
  S127–S830, all pre-existing;
* lines 29–32 — 4 `W01` lines (`tierC mined used-by=…`): S881, S882, S884, S893;
* line 33 — `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`;
* line 34 — `exit=0`.

Counts I measured on the committed blob: `W04` = 28, `W01` = 4, `E*` = 0, `W02`/`W03` = 0.
**There is no `$ …` command echo line, no header, no date, no revision, no clean-worktree
assertion, and no `rows`/`tier.`/`status.` line at all** (`grep -cE 'rows|tier\.|status\.'` → 0).

Regression against the lane's own earlier convention, for contrast:
`reports/round-53/telemetry/census-start.txt:1` = `# census at round start: 2026-10-22T13:53:32Z, lane tip
6524184e…, clean working copy (jj-lane.sh state: ahead=0 behind=0 tracked=0 untracked=0)`;
`reports/round-60/telemetry/census-end.txt:1` = `$ scripts/sources-census.sh validate … (at lane
47f27bd0…, 2026-10-23T07:51:58Z)`; `reports/round-73/telemetry/census-start.txt:1-2` = header + `$ …`
echo. Round 76 dropped all of that (F1).

### 1.2 End census receipt — `reports/round-76/telemetry/census-end.txt`

Committed at `788bd56` (the commit that also adds the knowledge entry, `corpus/QUALITY.md`,
`corpus/README.md` and `corpus/lessons/round-76.md`); **byte-identical at `722e69f`** (diff = empty).
35 lines:

* line 1 — `$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`;
* lines 2–29 — the same 28 `W04` lines;
* lines 30–33 — the same 4 `W01` lines (S881, S882, S884, S893);
* line 34 — `kotodama	ok	…/kotodama-shokunin/corpus/SOURCES.md`;
* line 35 — `exit=0`.

`diff(census-start, census-end)` = **one line** (the command echo). No `rows`/`tier.`/`status.` line
either (`grep -cE` → 0). So the "end census receipt" attests *no counts* — it is a second validate.
The identical warning set is expected, not suspicious: none of S894–S896 is tier C and each new URL
appears exactly once (see §2.3), so the append cannot add a `W01`/`W04`.

Note on what the end receipt measures: its command targets `--root … kotodama`, i.e. the **live
worktree** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`, not a committed
revision, and it pins no `--today` (the `E08` open-date check therefore depends on the run date).
It has no date or revision in the receipt either. This is the same class of weakness as F1.

### 1.3 Mirror validation receipt — `.ufo/waves/round-76/assimilation/validate-receipt.txt`

Committed at `6a5d63a`, **rewritten at `cab5247`**, present unchanged at `722e69f`. 86 lines.

* line 1 (header): `Round-76 final scratch mirror before registry append. Lane base: 98c486bdb4650ba5b8e651d332910e8ee60ad121. Mirror has the selected entry and S894-S896 append block; live lane SOURCES.md has not yet been appended.`
* line 3 — `$ …/sources-census.sh validate --file /fast/scratch/hyaku/kotodama-r76/L1-census-confirm-20261027/corpus/SOURCES.md --today 2026-10-27`
* lines 4–35 — 28 `W04` + 4 `W01`; line 36 `file	ok	/fast/scratch/…/corpus/SOURCES.md`; line 37 `exit=0`
* line 39 — `$ …/sources-census.sh census --file /fast/scratch/hyaku/kotodama-r76/L1-census-confirm-20261027/corpus/SOURCES.md --today 2026-10-27`
* **lines 40–46 (file block): `rows 820`, `tier.A 493`, `tier.B 311`, `tier.C 16`, `status.mined 725`, `status.queued 58`, `status.rejected 37`**
* **lines 47–56 (FLEET block): `rows 820`, `tier.A 493`, `tier.B 311`, `tier.C 16`, `tier.invalid 0`, `status.queued 58`, `status.mined 725`, `status.rejected 37`, `status.invalid 0`, `missing 0`**
* line 57 `exit=0`
* lines 59–85 — seven manual cross-checks, each with its own `exit=0`: rows `820`; malformed-NF `0`;
  tier `A=493 B=311 C=16`; status `mined=725 queued=58 rejected=37`; duplicate-ids `(no output)`;
  enum-and-tier-inflation `(no output)`; missing-mined-usedby `(no output)`.

So: **the committed census count block exists exactly once in the tree, and it is the mirror's.**

## 2. Exact counts, from the committed C-landing tree (my own re-derivation)

I re-derived the histograms with awk over `git show 722e69f:corpus/SOURCES.md` (no census script
invoked), and checked the same invariants the census script checks:

| metric | base `98c486b` | C landing `722e69f` | delta |
|---|---:|---:|---|
| registry rows | 817 | **820** | +3 |
| tier A | 491 | **493** | +2 |
| tier B | 310 | **311** | +1 |
| tier C | 16 | 16 | 0 |
| tier.invalid | 0 | 0 | 0 |
| status mined | 722 | **725** | +3 |
| status queued | 58 | 58 | 0 |
| status rejected | 37 | 37 | 0 |
| status.invalid | 0 | 0 | 0 |
| `missing` used-by paths | 0 | 0 | 0 |
| `corpus/knowledge/*.md` files | 252 | **253** | +1 |

**Every one of these equals the mirror receipt's block (lines 40–56).** The landed tree is
numerically what the mirror receipt says it is, even though the mirror's bytes are not the landed
bytes (F2).

Static E-code equivalent on the committed C-landing blob (each check mirrors
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`):

* `NF!=13` rows → **0** (all 820 rows are NF=13);
* duplicate ids → **0**;
* kind/tier/status enum violations → **0**; tier-A community inflation → **0**;
* mined rows whose `used-by` path is absent from the committed tree → **0**;
* row-shaped lines (`| S… |`) outside `## Registry` → **0** (no E12);
* new rows S894–S896: `opened 2026-10-27`, `recheck 180d`, `status mined`, kinds `dataset/docs/docs`,
  tiers `A/A/B`, `used-by` = the admitted amendment only.

That supports the end validate's `exit=0` and `ok` line as reproducible from the committed tree.

## 3. Does the end validate exit cleanly?

**Yes.** `reports/round-76/telemetry/census-end.txt:35` = `exit=0`, preceded by
`census-end.txt:34` = `kotodama	ok	…/corpus/SOURCES.md`. Measured on the committed blob:
`E01`–`E12` lines = **0**; `W04` = 28; `W01` = 4; `W02`/`W03` = 0.

The `W01` set is fully accounted for by the **base** registry (it is not introduced by round 76):
re-deriving "tier C + status mined + used-by ≠ `—`" over `git show 98c486b:corpus/SOURCES.md` yields
exactly four rows — S881, S882, S884, S893 — the same four ids the receipt lists. The 28 `W04`
duplicate-url-across-scopes warnings are all on S127–S830; none of S894–S896 appears, because each
of the three new URLs occurs exactly once in the committed registry
(`grep -cF` = 1 for `digital.archives.go.jp/search`, `openstd.samr.gov.cn/bzgk/std/newGbInfo`,
`news.gmw.cn/2017-05/23/content_24559485.htm`).

The mirror receipt's validate block is clean on the same terms (`validate-receipt.txt:36-37`:
`file	ok …`, `exit=0`), and its census block is clean on the same terms (`validate-receipt.txt:51,55,56`:
`tier.invalid 0`, `status.invalid 0`, `missing 0`, `exit=0`).

### 3.1 Two things the receipts do *not* say, stated plainly

1. **The committed lane at the C landing has no committed `census`-mode receipt.** The only
   count-bearing artifact is the mirror's. The counter's own lands run exists only in the **mutable
   worktree** (`reports/round-76/telemetry/measures-c.txt`, untracked at `722e69f`): it shows
   `LEG PASS CENSUS  exit=0 last-line=file	ok	/fast/scratch/…/r76-lands-6fmxjbe4/clone/corpus/SOURCES.md`.
   That file is not committed, and the same run ends `ACCEPT-C-76: FAIL legs=11/13` — the CENSUS leg
   passes while the ROWS and COLLCHECK legs fail. The ROWS failure is *not* a census finding: the
   counter's diff-based row-set check rejects two non-row additions present in the landed registry —
   `- calendar-standard design — S896 → S895 → S894: …` (the `## Paths` bullet) and
   `**State-standard calendar compilation (round 76).** Question…` — which is exactly what the
   committed lesson records as `R76-M3`
   (`corpus/lessons/round-76.md:85`, "source-census parser treated the valid registry table plus
   study-path/search-log appends as non-row additions under the exact line-diff implementation",
   captured-by `reports/round-76/telemetry/controls-c.txt`, routed, fix column "No predicate or
   append-only contract weakened; claim C remains failed as declared"). The census script itself
   emits no E12 for those two lines — they are not row-shaped — so the census verdict and the
   counter's ROWS verdict legitimately differ.
2. **The base counts live only in prose.** `claims.json:40` states "the registry holds 817 rows
   (last id S893) and corpus/knowledge holds 252 .md files"; `claims.json:101-102` repeats
   `rows_before 817`, `knowledge_before 252`; `claims.json:210` says the start receipt is
   "exit 0; **817 rows rederived separately**" — i.e. the lane itself records that the receipt does
   not carry the count. `reports/round-76/telemetry/gap-sweep.txt:4` says "registry: 817-row base
   registry". `corpus/lessons/round-76.md:93` states "817 rows; after the three opened rows: 820
   (A +2, B +1)". My re-derivation (§2) reproduces all of these.

## 4. The falsification defects, in detail

### F1 (medium) — start/end receipts carry no counts, no command echo, no pin
`reports/round-76/telemetry/census-start.txt` (34 lines, committed `b4965d5`) and
`reports/round-76/telemetry/census-end.txt` (35 lines, committed `788bd56`) contain **no**
`rows`/`tier.`/`status.` line. The start file has no command echo either; the end file has the
command but no date, no revision, no clean-worktree assertion. Consequently:
* the "817 rows" of the start cannot be read off the start receipt (the lane says so itself,
  `claims.json:210`);
* the "820 / A 493 B 311 C 16 / mined 725 queued 58 rejected 37" of the end cannot be read off the
  end receipt either;
* both receipts are, byte-wise, the *same* validate output over the *live worktree* path, one with
  an extra echo line. The pair is a stability witness (the warning set did not change across the
  append), not a measurement witness.
Regression vs. the lane's own rounds 53/60/73 convention quoted in §1.1.

### F2 (medium) — the count block measures a scratch mirror that is not the landed tree
Mirror: `/fast/scratch/hyaku/kotodama-r76/L1-census-confirm-20261027/corpus/SOURCES.md`
(md5 `53cc2173f29833b7499ce25a2f06692d`, 980 286 B) vs. landed
`git show 722e69f:corpus/SOURCES.md` (md5 `76f769d705fa28f9ad0be26b4cf50971`). `diff` = 11 lines:
the mirror lacks the `## Paths` bullet `- calendar-standard design — S896 → S895 → S894: …` and the
round-76 lead paragraph `**State-standard calendar compilation (round 76).** Question…`, and its
`S896` cell reads "same article in Internet Archive capture" where the landed row reads "the same
article…".
The mirror's **knowledge entry** also differs from the landed one
(mirror md5 `4c1657a0b10719e9a6ebd4a58240f747` vs landed md5 `fd5e4b13211889a6b25c4876c7e69561`):
the mirror copy says "This amendment adds both from **three tier-A carriers**" and "one
**tier-A** state-press report", while the landed entry says "adds both from **the opened sources**"
and "one **tier-B** state-press report". The landed row S896 is tier B, so **the mirror's entry
contradicts its own registry row**, and the landing corrected it. A receipt that validates the
mirror therefore attests a superseded artifact. The *counts* are unaffected (registry rows are
identical in tier/status terms) and I confirmed the landed counts independently (§2).

### F3 (medium) — the seven manual commands have no stated cwd
`validate-receipt.txt:59-85` run `grep … corpus/SOURCES.md` and four `awk … corpus/SOURCES.md`
commands with a **relative** path and no `cd` in the receipt; the earlier version committed at
`6a5d63a` had the same relative path (`$ sh -c grep -cE … corpus/SOURCES.md`). It is undecidable
from the receipt whether they ran in the mirror root or in the lane root. The numbers are the same
either way (820 in both after `cab5247`), so this is a provenance defect, not a numeric one.

### F4 (low) — the mirror receipt's header is false at its own commit
`validate-receipt.txt:1` asserts "live lane SOURCES.md has not yet been appended". The commit that
introduces this text, `cab5247` ("round-76: correct base ground and mirror receipts"), **appends
S894–S896 to `corpus/SOURCES.md` in the same commit** (`git show cab5247 -- corpus/SOURCES.md`
adds the three rows plus the `## Paths` bullet and the round-76 lead paragraph). At `cab5247` the
live lane registry is already 820 rows, so the header is stale the moment it is committed.

## 5. Two structural observations outside the census script's verdict

**(a) The three registry rows landed before the frozen configuration commit.** `cab5247`
(2026-10-27 19:54) appends S894–S896; the frozen config commit `df0f030` is 20:02. So at the
freeze revision the registry already holds 820 rows while the knowledge entry does **not** yet exist
(`entry-file` absent at `cab5247`/`df0f030`/`58e6c81`/`a43ed80`; present from `788bd56`). That is
why the committed do-nothing control `reports/round-76/telemetry/controls-c.txt` shows
`LEG FAIL CENSUS  census exit=1; census TSV carries E-code line(s): E11 (… S896 missing used-by
corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md)`. The frozen
claim's "before" state is the **base** (`817` rows, `claims.json:40`), so the counter's
base→lands diff is still well defined; but a reader of "frozen C/Ca configuration commit" should
know that commit already contains landed registry rows.
**(b) The wave-1 draft receipt's counts are stale and must not be quoted as the landed ones.**
`.ufo/waves/round-76/w1/stage/ExecCensusRows/validate-receipt-draft.txt:83-98` reports
`rows 821`, `tier.A 494`, `tier.B 310`, `tier.C 17`, `status.mined 726` — the four-row draft
(S894–S897, including the tier-C xingzuobaike page as S895). The landed set is three rows with
S895 re-pointed to the openstd record (tier A). The mirror validation receipt
(`validate-receipt.txt:40-56`) is the post-collapse, landed-shape block.

## 6. Ground sweep cross-check (adjacent, for the census verdict's completeness)

`reports/round-76/telemetry/gap-sweep.txt` (committed at `cab5247`, unchanged at `df0f030` and
`722e69f`) records three base sweeps against `98c486b`, scope `corpus/knowledge`: `GB/T 33661`,
`news.gmw.cn/2017-05/23/content_24559485.htm`, `openstd.samr.gov.cn/bzgk/std/newGbInfo` — each
"base matches: 0", `exit=1`, "raw output: (no output)", with the exact `git … grep -l -E …` command
spelled out. I re-ran the equivalent read-only `git grep` at `98c486b`: all three exit 1 with no
output. The ground claim is therefore independently reproducible, and the knowledge-file counts
252 → 253 and the absence of the entry path at base (`git ls-tree … | grep -c` = 0) hold.

## 7. Files and lines cited (all committed)

* `reports/round-76/telemetry/census-start.txt` — lines 1–28 (W04), 29–32 (W01), 33 (`ok`), 34 (`exit=0`); committed `b4965d5`.
* `reports/round-76/telemetry/census-end.txt` — line 1 (command echo), 2–29 (W04), 30–33 (W01), 34 (`ok`), 35 (`exit=0`); committed `788bd56`; identical at `722e69f`.
* `.ufo/waves/round-76/assimilation/validate-receipt.txt` — line 1 (header, F4), 3 (validate cmd), 4–35 (warnings), 36 (`ok`), 37 (`exit=0`), 39 (census cmd), **40–46 (file counts), 47–56 (FLEET counts incl. `tier.invalid 0`, `status.invalid 0`, `missing 0`)**, 57 (`exit=0`), 59–85 (seven MANUAL checks, relative path → F3); committed `6a5d63a`, rewritten `cab5247`.
* `reports/round-76/claims.json` — line 40 (before: 817 rows / 252 files), 41 (after), 101–102 (`rows_before 817`, `knowledge_before 252`), 155–167 (frozen leg texts), 210 ("817 rows rederived separately").
* `reports/round-76/telemetry/gap-sweep.txt` — lines 1–4 (base revision, scope, "817-row base registry"), 6–8 / 12–16 / 18–22 (three fragments, matches 0, exit 1).
* `reports/round-76/telemetry/controls-c.txt` — the `LEG FAIL CENSUS` E11 line at lands==freeze; `LEG FAIL ROWS` non-row additions.
* `corpus/lessons/round-76.md` — line 77 (census start command and receipt pointer), line 85 (R76-M3), line 93 ("817 rows; after the three opened rows: 820 (A +2, B +1)").
* `.ufo/waves/round-76/w1/stage/ExecCensusRows/validate-receipt-draft.txt` — lines 79–100 (wave-1 draft validate exit 0, census 821 / A 494 B 310 C 17 / mined 726).
* `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` — line 30 (E12 definition), 567 (E11 emission), 611–621 (`in_registry` / E12 emission), 541–568 (used-by path resolution against the registry's parent dir).

## 8. Tooling, scratch, hygiene

* **No tool was installed or upgraded.** `/home/vgpnk/.omp/agent/RULES.md` was read first; its
  install directive does not apply to a read-only falsification wave, and no install was needed.
  **No pacman transaction was run** (pacman stays paused). Recorded: tool — none; version — n/a;
  channel — n/a; reason — no tooling required.
* **No census, build, test, lint or formatter was run.** Every number in this report comes from
  `git show <rev>:<path>` on committed blobs plus awk/grep over those blobs.
* **Scratch:** no scratch directory was created under
  `/fast/scratch/hyaku/kotodama-r76/ExecCensusAudit`; the scratch mirror referenced by the receipt
  (`/fast/scratch/hyaku/kotodama-r76/L1-census-confirm-20261027`) was **read only** and left
  untouched. Five temporary files under `/tmp` (`cs.txt`, `ce.txt`, `sources722.md`, `l.md`,
  `tree.txt`) were used for byte diffs and **deleted** (`ls` confirms absent).
* **Writes:** this file only —
  `.ufo/waves/round-76/w2/ExecCensusAudit.md`. No lane file, no claim, no counter, no receipt, no
  report of another seat was touched. No commit, no push.
* **A commit landed mid-audit and is accounted for.** While this seat was reading, the lane
  committed `af67443` ("round-76: record measured claim outcomes") on top of the cited C landing
  `722e69f`. It touches exactly four paths — `SCORECARD.md`, `corpus/lessons/round-76.md`,
  `reports/round-76/telemetry/measures-c.txt`, `reports/round-76/telemetry/measures-ca.txt` — and
  **none of the three census artifacts this report audits**
  (`reports/round-76/telemetry/census-start.txt`, `reports/round-76/telemetry/census-end.txt`,
  `.ufo/waves/round-76/assimilation/validate-receipt.txt`) is changed by it
  (`git diff --name-only 722e69f af67443` lists only those four paths). Every count, warning set
  and verdict in this report is therefore identical at `722e69f` and at `af67443`.
  `af67443` promotes the previously untracked counter lands receipts to committed, so §3.1's
  statement about "no lands-level counter receipt in the committed tree" holds **at the cited
  revision `722e69f`** and no longer at `af67443`; the receipt content is the file I read
  (`git show af67443:reports/round-76/telemetry/measures-c.txt` is byte-identical to the
  worktree copy: `LEG PASS CENSUS`, `ACCEPT-C-76: FAIL legs=11/13`, and `ACCEPT-CA-76: FAIL
  legs=5/12`). `af67443` also adds a `SCORECARD.md` axes section whose published counting command
  (`git ls-tree … corpus/knowledge | grep -c '\.md$'` and
  `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`)
  yields `98c486b… knowledge=252 rows=817` and `722e69f… knowledge=253 rows=820` — the same
  numbers I re-derived independently in §2.
* **Uncommitted worktree artifacts** that were **not** treated as evidence:
  `reports/round-76/counters/`, `.ufo/waves/round-76/selftest.sh`, `.ufo/waves/round-76/w2/`
  (this wave's own files). The cited C-landing revision `722e69f` contains **no** lands-level
  counter receipt for either claim — the only committed Ca receipt there is round 75's re-run
  (`reports/round-76/telemetry/accept-ca-75-at-lands.txt`, `ACCEPT-CA-75: PASS legs=12/12`).
