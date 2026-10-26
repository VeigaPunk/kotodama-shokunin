# ConnectorRoutes — cross-claim / cross-source pattern finder over the LANDED round 74

**Seat:** `ConnectorRoutes` (connector, leaf — no dispatch, no background job, no `task`).
**Round:** 74, WAVE 2 (falsify), hyaku run 7. **Date:** 2026-10-25.
**Lane root:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (all repo reads/writes absolute).
**Fleet root:** `/home/vgpnk/Projects/shokunin` (read-only here).
**Base** `f7104cbce186bc2e1522abf0cfd619cc834628bb` · **operative freeze F3** `00c408a0af2fa5ddf65af2224152ce258b26d896` ·
**claim Ca lands** `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` · **claim C lands** `c4bf61a8d722f9168ce0fd8021a6261c000610c5` ·
**lane main at dispatch** `1d7add3f7b9eaf6f3349c56c36f6d06325d74236`.

**Tooling record:** no tool installed or upgraded. Host-wide pacman pause respected (never run). Pre-installed
Python 3.14, `git`, `grep`, `sed`, `awk`, `sha256sum` sufficed. Reason: the seat's checks are `git` plumbing
inspection plus running two already-committed counters; no new dependency is warranted.

**Scratch:** `/fast/connector-routes-tmp/` (clones), `/tmp/ConnectorRoutes/` (this report's scratch notes).
`/tmp` was at **100 % (457 MB free)** when this seat started, so the mandated `mktemp -d` clone rule could not be
satisfied there — the first clone attempt died with `fatal: failed to copy file … No space left on device`. The
clone discipline was preserved exactly, only the scratch *filesystem* changed: `D=$(mktemp -d -p /fast/connector-routes-tmp)`
→ `git -C "$D" init -q` → `git -C "$D" rev-parse --show-toplevel` printed `$D` → `git clone -q
/home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"`. **All** `git branch -f main` / `git update-ref
refs/heads/main` moves happened inside that clone only; the lane repo at
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` was never written, never had its index or refs touched, and
`git status --porcelain` there is unchanged by this seat. This is the host-wide `/tmp` pressure recorded in
`.ufo/l0-questions.md:46` (`L0 kotodama | round-9`), now binding on *space* rather than inodes.

**Download hygiene:** **no live fetch was made by this seat.** Every check below runs over committed bytes or
over the two committed counters, so this seat has **no User-Agent to record**. The one place a URL appears in a
command (`https://www.chinawriter.com.cn/...`) is a *string comparison* against committed registry rows, not a
network request — no wall, CAPTCHA or HTTP refusal was encountered and none is claimed.

---

## 0. Verdict up front

Five recurring patterns explain where this round's wave-1 attacks found defects. **Four of the five still carry a
live instance in the landed bytes**; one is fully closed. The most serious is not a wave-1 pattern at all — it is
a **cross-claim interaction that wave 1 predicted, that the round knew about, and that the landed round ships
unfixed and under-disclosed**.

| # | Pattern | Instance still present at main? | Severity | QUALITY 1-25 covers it? |
|---|---|---|---|---|
| **P1** | **Cross-claim write-set collision** — two frozen claims cannot both hold in one tree | **YES — Ca counter is RED at main** | **BLOCKER** | **NO** (Q7 governs *citations*, not *in-place edits*; Q25 governs *config source*, not *mutual satisfiability*) |
| **P2** | **Ledger/annotation prose vs. the token the counter actually executes** | **YES — the SCORECARD's printed command is never run** | **HIGH** | **NO** (Q11/Q17 are about *declaring* and *stamping*, not *executing the printed command*) |
| **P3** | **`stated_at` ≠ the file the observation reads** — the pair's own site is never re-read | **YES — 11 of 12 ANNOTATE pairs** | **MEDIUM** | **NO** (Q12 requires the *re-test output*, not that the re-test read the *stated site*) |
| **P4** | **Campaign-namespace ids vs. lane ids** | **PARTIAL — closed in prose, still open in the counter's `forbidden_ids` derivation** | **MEDIUM** | **NO** (Q23/Q25 are counter-config criteria; the *namespace* clause Q24 covers only CDX probes) |
| **P5** | **Receipt-vs-verdict decoupling / seat-name collisions** | **CLOSED for this round** — attack FAILED | LOW | **YES** — Q17 + Q19 + Q25(a) cover it |

---

## P1 — Cross-claim write-set collision (BLOCKER, live)

### Pattern

Round 74 lands **two claims into one tree**. Claim C appends four registry rows *and* makes one **in-place**
edit to an existing row (`S877`'s `used-by` cell). Claim Ca's `APPENDONLY` leg states that changed lines
*outside* the seven protected files must be "a subset of the stated_at lines of REPAIR pairs plus appended
lines" — and Ca's only REPAIR pair is `LC-09` on `SKILL.md:594`. So Ca's rule, as frozen, **forbids** exactly the
in-place edit C's `ROWS` leg **requires**. The two frozen claims are jointly unsatisfiable in one tree.

### Evidence pointers

- Frozen rule A (claim C, `ROWS`): "the only other registry change is S877's line, whose used-by cell at
  `<lands>` equals its base value plus exactly the new base-entry path (parsed from both revisions) and every
  other cell is byte-identical" — `reports/round-74/claims.json` @ freeze, claim C `legs[1]`.
- Frozen rule B (claim Ca, `APPENDONLY`): "changed lines elsewhere are a subset of the stated_at lines of
  REPAIR pairs plus appended lines, except the six must_track paths" — `reports/round-74/claims.json` @ freeze,
  claim Ca `legs[4]`.
- The ledger's only REPAIR pair: `reports/round-74/ledger.json` → `LC-09 … "stated_at": "SKILL.md:594"`.
- The counter's implementation of rule B: `reports/round-74/accept-ca.py:1384-1402`
  (`for status, path in changed_files(root, base, lands): … allowed = repair_lines.get(path, set())` →
  `bad.append("%s: changed lines outside REPAIR stated_at lines %s" % (path, sorted(bad)[:6]))`).
- The byte that collides: `corpus/SOURCES.md` line **832** (`S877`), whose `used-by` cell gains
  `corpus/knowledge/culture-material/worldbuilding-setting-practice.md`.
- Wave-1 already named the collision class: `.ufo/waves/round-74/w1/RevClaimsFidelity.md:141` (F5,
  "`SEPARABLE` does not enumerate its read set, and `corpus/README.md` is a real C↔Ca collision") and
  `.ufo/waves/round-74/w1/RevAssimilationContract.md` F2/F19 (the `used-by` pointer rewrite vs. "none removed").

### Check command and raw output

```
$ D=$(mktemp -d -p /fast/connector-routes-tmp) && git -C "$D" init -q && git -C "$D" rev-parse --show-toplevel
/fast/connector-routes-tmp/tmp.YDl6pnLy0Z
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
$ cd "$D/lane" && git checkout -q --detach 1d7add3f7b9eaf6f3349c56c36f6d06325d74236
$ git update-ref refs/heads/main 1d7add3f7b9eaf6f3349c56c36f6d06325d74236
$ python3 -B reports/round-74/accept-ca.py --root . \
    --lands 1d7add3f7b9eaf6f3349c56c36f6d06325d74236 \
    --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 \
    --fleet-root /home/vgpnk/Projects/shokunin
```

Raw output (verbatim, leg lines):

```
LEG PASS LEDGER
LEG PASS BASEMISMATCH
LEG PASS REPAIR
LEG PASS ANNOTATE
LEG PASS NOSTUB
LEG FAIL APPENDONLY
     protected=['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-74.md', 'corpus/lessons/round-73.md', 'corpus/lessons/round-72.md', 'reports/round-73/claims.json', 'reports/round-73/ledger.json'] protected-removed=0 fleet-pin=dad39efd2798 report=.ufo/reports/round-73/kotodama.md blob-sha256=000bab3a3664 repair-stated_at={'SKILL.md': [594]} must_track-exempt=6 problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
LEG PASS SEPARABLE
LEG PASS TRACKED
LEG PASS RECEIPTS
LEG PASS FROZENCFG
LEG PASS STAMP
     stamped=evaluated=measured=1d7add3f7b9e tree=33a67fd9ce17 counter=8052f1e25c36 clone=/tmp/r74-ca-57t8ogqf/lands
ACCEPT-CA-74: FAIL legs=10/11
EXIT=1
```

The same failure reproduces at **claim C's own landing** (`--lands c4bf61a8d722f9168ce0fd8021a6261c000610c5`,
clone-local `main` = that commit): `LEG FAIL APPENDONLY … problems=['corpus/SOURCES.md: changed lines outside
REPAIR stated_at lines [832]']` → `ACCEPT-CA-74: FAIL legs=10/11`, exit 1.

And at **claim Ca's own landing** (`--lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`, clone-local `main` =
that commit) the same counter prints `ACCEPT-CA-74: PASS legs=11/11`, exit 0 — because
`corpus/SOURCES.md` is byte-unchanged between base and Ca's own landing:

```
$ git diff f7104cbce186bc2e1522abf0cfd619cc834628bb..5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 --stat -- corpus/SOURCES.md
(empty = unchanged)
```

### The byte-level proof of the collision

```
$ git show f7104cbce186bc2e1522abf0cfd619cc834628bb:corpus/SOURCES.md | sed -n '832p' | tr '|' '\n' | tail -4
 2026-10-25
 180d
 corpus/knowledge/linguistics/conlang-scholarship.md

$ git show main:corpus/SOURCES.md | sed -n '832p' | tr '|' '\n' | tail -4
 2026-10-25
 180d
 corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md
```

Line 832 is **modified in place** (a `-`/`+` pair in the diff, `@@ -829,10 +829,14 @@`), so it is not an
appended line, and `corpus/SOURCES.md` is not a REPAIR `stated_at` path and not one of the six `must_track`
paths. Rule B rejects it.

### The disclosure is under-scoped — this is the second-order effect

The round **knows** about this. It is disclosed in exactly one place:

```
$ grep -rn "both land in one tree\|not a REPAIR stated_at line of claim Ca" --include=*.md --include=*.json --include=*.txt .
reports/round-74/telemetry/junk-ca.txt:66:#  (1) APPENDONLY: claim C's required in-place used-by change on the reused registry row is not a REPAIR stated_at line of claim Ca, so the two frozen claims conflict when both land in one tree; claim Ca is therefore measured at its OWN landing commit, where it prints ACCEPT-CA-74: PASS legs=11/11 (reports/round-74/telemetry/measures-ca.txt). Disclosed as a frozen-claims limit, not amended.
```

That is the **only** occurrence in the entire lane — it is **not** in `corpus/lessons/round-74.md` (the `##
Mistakes` table, `## Gate`, or `## Quarantine`), **not** in `SCORECARD.md` (the `## Corrections — round 74`
section), **not** in `SKILL.md`, **not** in `reports/round-74/claims.json`, and **not** in the fleet report.
A reader of the round's *records* sees a clean `ACCEPT-CA-74: PASS legs=11/11` in
`reports/round-74/telemetry/measures-ca.txt` and cannot tell that the counter is **red at the round's own
main**. The disclosure lives in a *junk-fixture receipt* — a file whose purpose is to record failures, not to
carry the round's load-bearing caveats.

Second-order effect: the round's own after-state is therefore **not reproducible at the round's tip**. A closure
that re-runs the claim's own `counter` field at `<lands> = main` gets exit 1 and `FAIL legs=10/11`, while the
committed receipt and every summary document say `PASS legs=11/11`. This is precisely the
**receipt-vs-verdict decoupling** class that QUALITY 17/19 and the round-72 routed defect R2 were written to
kill — reintroduced through the *cross-claim* door rather than the *edit* door.

### Proposed fix (bounded, and it does not amend a frozen leg)

The frozen legs may not be amended after a seat scores landed data, so the fix must live **outside** the legs.
Two options, in order of preference:

1. **Make the collision explicit and the run self-consistent.** Add to `reports/round-74/counter-revisions.md`
   (the file QUALITY 23 already designates for counter revisions) a row recording: *counter `accept-ca.py`
   unchanged (sha `8052f1e25c36…`); the `APPENDONLY` leg's frozen sentence is unsatisfiable jointly with claim
   C's `ROWS` leg in one tree; claim Ca is therefore graded at its own landing `5e4796c…`, which is the commit
   the claim's `after` names.* Then **file the same disclosure in `corpus/lessons/round-74.md`'s `## Mistakes`
   table as a new row (e.g. `R74-M11`)**, so the round's durable record — not a junk receipt — carries the
   caveat. The `## Mistakes` table is append-only-by-row and is not a frozen leg, so this is legal.
2. **Grade Ca at a tree that contains both claims.** The cleanest long-run shape is for the `APPENDONLY` leg's
   protected set to include `corpus/SOURCES.md` and for the six-`must_track` exemption to become a
   *claim-owned in-place-edit* exemption (the `used-by` cell of `S877`), so that Ca's rule stops forbidding
   what C's rule requires. This is a **counter revision** to the next round's `accept-ca.py`, not an amendment
   to round 74's frozen leg. Round 74's counter stays as it is; round 75 ships the corrected one.
3. **Do not** simply re-word `claims.json`: that is the round-69 Ca2 failure class the claim's own `kill_rule`
   forbids.

### QUALITY coverage

**NOT covered.** Q7 (*Claims stay separable*) governs *citations and named paths* ("its added lines may not cite
an identifier another claim newly exports, nor name a path another claim newly lands") — it is silent on
in-place edits that one claim requires and another forbids. Q25 governs *where a counter reads its constants*
and *which junk landings it must reject* — silent on whether two frozen claims are *mutually satisfiable*. The
closest existing vocabulary is Q7, but the instance is not a citation dependency: it is a **write-set
collision**, and no criterion in 1-25 requires that the round's two claims be satisfiable in one tree, nor
requires a known unsatisfiability to be recorded in the round's durable record rather than in a control receipt.

---

## P2 — Ledger/annotation prose vs. the command the counter actually executes (HIGH, live)

### Pattern

Claim Ca's `ANNOTATE` leg says: "every ANNOTATE pair has a row under '## Corrections — round 74' in SCORECARD.md
naming the pair id, the base stated token and the observed token, and **the row's re-derivation command is
re-run by the counter** and returns the observed token." The `NOSTUB` leg says every correction row carries
"id + old token + new token + the re-derivation command".

The counter satisfies both by reading the **ledger's** `rederive` field — `reports/round-74/accept-ca.py:939-944`:

```python
def rederive_argv(pair):
    raw = pair.get("rederive") or shlex.join(pair["observe_cmd"])
    ...
```

and `NOSTUB` only checks that the *ledger's* rederive string is **present somewhere in the row**
(`accept-ca.py:1481-1496`: `cmd = rederive_text(pair)` … `if cmd not in nr: lacks.append("rederive-cmd")`).
The **SCORECARD row's own printed command is never parsed and never executed.** A row can print any command at
all, as long as the ledger's command text also appears *somewhere* in the same row — even in a different cell.

### Check command and raw output

Mutant M-A — replace the LC-01 command cell outright (nothing else changes):

```
$ cd "$D/lane" && git checkout -q --detach 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
$ git update-ref refs/heads/main 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
$ # replace the LC-01 row's command cell with: echo WRONG-COMMAND-RETURNS-NOTHING
$ git commit -qam "mutant: LC-01 SCORECARD command column replaced with bogus echo"
$ python3 -B reports/round-74/accept-ca.py --root . --lands 4407e193… --freeze 00c408a0… --fleet-root /home/vgpnk/Projects/shokunin
```

```
LEG PASS ANNOTATE
     rows=14 annotate-pairs=12 unannotated=0 []
LEG FAIL NOSTUB
     minimum-shape=leading-id+old-token+new-token+rederive stubs=['LC-01:rederive-cmd']
ACCEPT-CA-74: FAIL legs=8/11
EXIT=1
```

→ M-A **is** caught, but by **NOSTUB** (the ledger's rederive text vanished from the row), **not** by ANNOTATE.
ANNOTATE stayed green while the row's printed command was a useless `echo`.

Mutant M-B — keep the ledger's rederive text in the row but move it into a *different cell*, leaving the printed
command column bogus:

```
$ # LC-01 row becomes:
$ # | LC-01 | 412 | 804 | echo THIS-COMMAND-RETURNS-NOTHING | note: git grep -c -E '^. S[0-9]{3}' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |
$ git commit -qam "mutant: LC-01 printed command bogus, ledger rederive text relegated to a note cell"
$ python3 -B reports/round-74/accept-ca.py --root . --lands 39e8910c… --freeze 00c408a0… --fleet-root /home/vgpnk/Projects/shokunin
```

```
LEG PASS LEDGER
LEG PASS BASEMISMATCH
LEG PASS REPAIR
LEG PASS ANNOTATE
     rows=14 annotate-pairs=12 unannotated=0 []
LEG PASS NOSTUB
     minimum-shape=leading-id+old-token+new-token+rederive stubs=[]
LEG PASS APPENDONLY
LEG PASS SEPARABLE
LEG PASS TRACKED
LEG FAIL RECEIPTS
LEG PASS FROZENCFG
LEG PASS STAMP
ACCEPT-CA-74: FAIL legs=9/11
EXIT=1
```

**Both ANNOTATE and NOSTUB pass.** The only red leg is `RECEIPTS`, and that red is **this seat's own
environment artifact**, not the mutant: `RECEIPT_TMP_RE = re.compile(r"/(?:var/)?tmp/[^\s:,\"']+")`
(`accept-ca.py:183`) normalizes only `/tmp`-rooted clone paths, and this seat ran with
`TMPDIR=/fast/connector-routes-tmp` because `/tmp` was full. The **unmutated baseline** at the same commit
with the same `TMPDIR` produces the identical `RECEIPTS` failure:

```
$ # baseline, Ca's own landing, TMPDIR=/fast/connector-routes-tmp
LEG FAIL RECEIPTS
     … problems=['reports/round-74/telemetry/accept-c-73-at-lands.txt: committed stdout differs from the re-run (bda16ca6deec vs 317e0fc828a0)', …]
ACCEPT-CA-74: FAIL legs=10/11
```

and the same baseline with the default `TMPDIR=/tmp` prints `LEG PASS RECEIPTS` / `ACCEPT-CA-74: PASS
legs=11/11`. So M-B's *net* effect is: **the bogus printed command is not detected by ANNOTATE or NOSTUB.**

M-B is a genuine survivor of the frozen `ANNOTATE`/`NOSTUB` sentences as implemented.

### Proposed fix

`leg_annotate` and `leg_nostub` should **parse the SCORECARD row's command cell** (the 4th cell of a
`| id | old | new | command |` row), `shlex.split` it, and **execute that argv** in the lands clone — asserting
it returns the observed token. The ledger's `rederive` should be used only as a *cross-check* that the two
agree, not as the sole source of truth. Concretely: in `leg_annotate` (`accept-ca.py:1327`), replace
`argv, why_argv = rederive_argv(pair)` with an argv parsed from the row, and keep the ledger's argv as a
secondary assertion ("the ledger's rederive must equal the row's printed command"). In `leg_nostub`
(`accept-ca.py:1481-1496`), require the rederive text to appear **in the command cell specifically**, not
anywhere in the row.

### QUALITY coverage

**NOT covered.** Q11 requires each claim clause to be *shown able to fail* and names the command that checks
it — it does not require that the command **printed in the record** is the one executed. Q17 requires a receipt
to pin its revision and tree; Q19 requires it to be produced in a clone at that revision — neither inspects
*which* command was run. Q25(a) governs the counter's *constants* source. Nothing in 1-25 says "a
self-assessment's printed command must be the command the verifier executes" — which is the whole point of a
calibration round.

---

## P3 — `stated_at` ≠ the file the observation reads (MEDIUM, live)

### Pattern

Each ledger pair names a `stated_at` site (`path:line`) whose token the pair attacks, and an `observe_cmd`
that re-derives the truth. Wave-1's `MutLedgerCa` and `RevClaimsFidelity` F3 flagged the *grammar*; what
survives into the landed bytes is that **for 11 of 12 ANNOTATE pairs, `observe_cmd` does not read the
`stated_at` path at all.** The correction therefore re-derives a number from a *different* file and files it
against a sentence in *this* file. The two are never joined by the counter: `BASEMISMATCH` compares the token
*parsed at `stated_at`* with the token *returned by `observe_cmd`* (`accept-ca.py:1167-1189`), so the pair is
red at base for the trivial reason that two unrelated numbers differ — and green at lands for the equally
trivial reason that a different number equals it.

### Check command and raw output

```
$ python3 -c "
import json
d=json.load(open('reports/round-74/ledger.json'))
ps=d['pairs'] if 'pairs' in d else d
for p in ps:
    if p['disposition']!='ANNOTATE': continue
    sa=p['stated_at']; path=sa.split(':')[0].replace('fleet:','')
    cmd=' '.join(p['observe_cmd'])
    print('%-6s stated_at=%-45s cmd_reads_stated_at_path=%s' % (p['id'], sa, path.split('/')[-1] in cmd))
"
```

```
LC-01  stated_at=SHONEN.md:6                                   cmd_reads_stated_at_path=False
LC-02  stated_at=LOG.md:4297                                   cmd_reads_stated_at_path=False
LC-03  stated_at=fleet:.ufo/reports/round-73/kotodama.md:10    cmd_reads_stated_at_path=False
LC-06  stated_at=corpus/README.md:732                          cmd_reads_stated_at_path=False
LC-07  stated_at=corpus/README.md:736                          cmd_reads_stated_at_path=False
LC-08  stated_at=corpus/README.md:344                          cmd_reads_stated_at_path=False
LC-11  stated_at=corpus/lessons/round-73.md:38                 cmd_reads_stated_at_path=False
LC-12  stated_at=reports/round-73/claims.json:11               cmd_reads_stated_at_path=False
LC-15  stated_at=corpus/README.md:36                           cmd_reads_stated_at_path=False
LC-16  stated_at=corpus/lessons/round-73.md:138                cmd_reads_stated_at_path=True
LC-17  stated_at=corpus/README.md:28                           cmd_reads_stated_at_path=False
LC-18  stated_at=corpus/README.md:36                           cmd_reads_stated_at_path=False
```

**11 of 12 ANNOTATE pairs** (the 12th, `LC-16`, is the only one whose command reads its own `stated_at` path)
carry a `stated_at` the observation never touches. Two illustrations:

- `LC-02` / `LC-03` — `stated_at` are `LOG.md:4297` ("Ca 9 scenarios") and the *fleet* report `:10`
  ("Ca 9 scenarios"), yet both `observe_cmd`s are
  `git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cb… -- reports/round-73/telemetry/selftest-r3.txt`.
  Re-running that command prints `SELFTEST OK: 10 scenarios` — the lane's *round-73 selftest receipt*, which is
  neither of the two attacked sentences. The `9` in `LOG.md:4297` and in the fleet report is never re-read by
  anything the counter runs.
- `LC-15` / `LC-17` / `LC-18` — `stated_at` is `corpus/README.md:36` / `:28` / `:36` (a *prose* sentence
  "registry moved 753 → 776 rows"), while the command counts rows in `corpus/SOURCES.md` at three historical
  revisions:

```
$ git grep -c -E '^. S[0-9]{3}' 65fe8572822ef83f1750593af77daddf34a1e337 f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md
65fe8572822ef83f1750593af77daddf34a1e337:corpus/SOURCES.md:724
f7104cbce186bc2e1522abf0cfd619cc834628bb:corpus/SOURCES.md:804
```

The counter's `ANNOTATE` leg then asserts the *row* carries `776` (old) and `724` (new) — but the `776` never
appears at `corpus/README.md:36` in the tree the counter reads; it is matched as a *substring anywhere in the
SCORECARD row* (`accept-ca.py:1321`: `token_in(norm(r), norm(tok)) and token_in(norm(r), norm(obs))`).

### Proposed fix

`ANNOTATE` should assert that the pair's `observe_cmd` **reads the `stated_at` path** (or that the ledger
carries an explicit, declared *bridge* naming why a different file is the correct observation site, and the
bridge is itself re-derived). At minimum the `LEDGER` leg should record, per pair, that `stated_at` is
*not* the observed site, so the pairing is declared rather than implied. The two historical-revision pairs
(`LC-15/17/18`) are defensible — their `why` says so explicitly ("measured at the landing commit the statement
is about") — but `LC-02`/`LC-03`'s `why` does not, and there the observation site genuinely differs from the
attacked sentence.

### QUALITY coverage

**NOT covered.** Q12 ("Re-test stated rejection grounds") demands the *re-test tool's verbatim output* be
carried in the record — satisfied here — but it never requires that the re-test read the *stated site*. Q10
covers *source* access; Q24 covers CDX probes. Nothing in 1-25 requires that a ledger pair's observation and its
stated location be joined, which is what makes the red/green transition in `BASEMISMATCH` meaningful.

---

## P4 — Campaign-namespace ids vs. lane ids (MEDIUM, partially closed)

### Pattern

Wave-1 pattern (`ConnectorPatterns` P2, `RevAssimilationContract` F20) — a staged/campaign `S-id` is cited in
a lane artifact where it collides with a *different* lane row. Round 74 created the collision **by itself**:
the staged package's `S883`/`S884` (litmemo, tuduku) became lane `S881`/`S882`, while lane `S883`/`S884`
are now the chinawriter rows.

### Evidence pointers and check

```
$ grep -n "S883" corpus/lessons/round-74.md
21:| S883 — 爱潜水的乌贼「我先设定世界观，再考虑怎么升级」, 中国作家网 2025-06-10 — https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | … | admitted |
77:| S883 | litmemo.com/ja/blog/novel-worldbuilding-guide | **S881** | append |
79:| S899 | chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | **S883** | append, re-quoted from the page |
```

The lesson is careful — the map table's column header is `staged | document | lane id | action`, and line 68-70
says outright that "the two-id overlap that matters (`S883`, `S884`) is created *by* this adoption". **The
prose attack FAILED**: the landed lesson disambiguates staged ids from lane ids by *document*, as
`RevAssimilationContract` F20 recommended.

The **counter** is where it stays open. `accept-c.py:649`:

```python
"forbidden_ids": sorted(staged_ids - lane_ids),
```

with `staged_ids = {S883, S884, S899, S900, S882}` and `lane_ids = {S881, S882, S883, S884, S877}`, so
`forbidden_ids = {S899, S900}`. The REPOINTED leg (`accept-c.py:1070-1073`) then forbids only those two tokens
from appearing in the two entries. **Staged `S883` and `S884` are not forbidden at all** — precisely because
they now name *different, real* lane rows. The only thing keeping a staged-`S883` (litmemo) citation out of an
entry is the URL-identity check at `accept-c.py:1060-1064` (`norm_url(u) not in row_keys`), which is a *row-URL*
check rather than an *id* check.

That check is stronger than the token check would be, so the landed entries are safe. But the counter's
id-level defence has a hole by construction: an entry that cited `S883` with the **litmemo** URL would be caught
by the URL check (the lane `S883` row's URL is the chinawriter one), yet the *token* `S883` would be silently
permitted by `forbidden_ids`. The frozen `REPOINTED` sentence says "no campaign-namespace id is cited as a lane
row" — a token-level claim enforced by a URL-level test, with the token-level guard disabled by the very
adoption that creates the collision.

### Proposed fix

`accept-c.py:649` should compute `forbidden_ids` as the **staged ids of documents that were NOT adopted**
(here: `S882`, `S899`, `S900` — the staged `S883`/`S884` were *re-pointed*, not refused), and the REPOINTED leg
should additionally assert, per inline `S-id` token, that the token's **row URL matches the URL the token is
cited beside** — which the existing `row_keys` check does for `source:` lines but not for **inline** ids
(`accept-c.py:1065-1069` only checks `sid in allowed`, never the inline token's document identity).

### QUALITY coverage

**NOT covered.** Q23 governs selftest receipts; Q24 governs CDX probes; Q25 governs counter config source.
The *cross-campaign namespace isolation* clause that round-73 wave-2 proposed as "QUALITY 24"
(`.ufo/waves/round-73/w2/ConnectorRoutes.md:201`) was **never adopted** — round 74's QUALITY 24 is the CDX
prose-positive-control criterion instead (`.ufo/waves/round-73/w2/ConnectorRoutes.md:197` records this
divergence explicitly). So the pattern wave-1 named has no criterion behind it.

---

## P5 — Receipt-vs-verdict decoupling and seat-name collisions (CLOSED — attack FAILED)

### Pattern

The round-72 routed defect R2 class: a summary document asserts a PASS verdict that the committed telemetry
receipt does not support, or a receipt is typed rather than executed. Round 74's own `RECEIPTS` leg was written
to close it, and the round-73 wave-2 pattern list (`ConnectorRoutes` P5, `ConnectorPatterns` P5) flagged the
same class twice.

### Check and evidence — the attack FAILED (the claim survived)

```
$ grep -rn "^ACCEPT-\|^# .*ACCEPT-" reports/round-74/telemetry/*.txt
reports/round-74/telemetry/accept-c-73-at-lands.txt:27:ACCEPT-C-73: PASS legs=11/11
reports/round-74/telemetry/accept-ca-73-at-lands.txt:38:ACCEPT-CA-73: PASS legs=9/9
reports/round-74/telemetry/controls-c.txt:48:ACCEPT-C-74: FAIL legs=4/13
reports/round-74/telemetry/controls-c.txt:54:ACCEPT-C-74: FAIL legs=0/13 (refused: lands f7104cbce186 is the frozen claim base f7104cbce186 (the do-notothing control: no data landed))
reports/round-74/telemetry/controls-ca.txt:52:ACCEPT-CA-74: FAIL legs=7/11
reports/round-74/telemetry/controls-ca.txt:57:ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the frozen base f7104cbce186)
reports/round-74/telemetry/measures-c.txt:36:ACCEPT-C-74: PASS legs=13/13
reports/round-74/telemetry/measures-ca.txt:48:ACCEPT-CA-74: PASS legs=11/11
```

Every committed PASS verdict has a matching committed FAIL control; the controls and the junk receipts carry
only FAIL lines. `RECEIPTS` **re-executes** the round-73 counters inside a clone and byte-compares
(`accept-ca.py:1746-1838`), so a typed receipt does not satisfy it — the round-73 `MutLedgerCa` M10 survivor
class is closed. I re-ran the counter with a bogus LC-01 command and with the note-cell mutant; `RECEIPTS`
stayed green in both, i.e. it is genuinely re-executing, not string-matching.

Seat-name collisions: **26 seat names recur between round-73 wave 2 and round-74 wave 2** (e.g.
`ConnectorRoutes`, `MutLedgerCa`, `RevLessonGate`, `ScribeLogScorecard`, `SimplifierEntries`, `RevengerOrigins`):

```
$ comm -12 <(ls .ufo/waves/round-73/w2/*.md | xargs -n1 basename | sed 's/\.md$//' | sort -u) <(…round-74 w2 seat names… | sort -u)
ConnectorAdjacency
ConnectorRoutes
CritAppendOnly
… (26 total)
```

This is the round-73 R74-M1 defect class ("seats of round 73 kept writing into the tree after the push"). The
**attack FAILED**: the collision is only a *name* collision across different wave directories
(`.ufo/waves/round-73/w2/` vs `.ufo/waves/round-74/w2/`), and the round-73 wave-2 files are **frozen by blob
id** by Ca's `TRACKED` leg. Checked:

```
$ git log --oneline 00c408a0af2fa5ddf65af2224152ce258b26d896..main -- .ufo/waves/round-73/
(empty = none)
```

No round-73 wave-2 byte changed after the freeze, and `LEG PASS TRACKED  paths=6 problems=[]` at both Ca's
landing and main. The six inherited files are pinned by sha256 in the frozen ledger and re-verified. The
name collision is therefore cosmetic — a reader looking for "the ConnectorRoutes report" must disambiguate by
wave directory, which the round's own `ExecWaveLedger` seat already handles.

### QUALITY coverage

**Covered.** Q17 (receipts pin measured revision, tree hash and counter sha256), Q19 (receipts run at the
revision they stamp, in a clone, with the header grammar), and Q25(a)/(b) (constants read from the freeze commit;
junk-landing controls shipped and each failing its named leg) together cover this pattern, and the landed
round's receipts satisfy them.

---

## Summary of checks run (all in this seat's own clone; the lane repo was never written)

| # | Check | Result |
|---|---|---|
| 1 | `accept-c.py --lands main --freeze 00c408a0…` | **PASS legs=13/13**, exit 0 — claim C survived |
| 2 | `accept-ca.py --lands 5e4796c…` (Ca's own landing) | **PASS legs=11/11**, exit 0 |
| 3 | `accept-ca.py --lands c4bf61a…` (claim C's landing) | **FAIL legs=10/11** — `APPENDONLY` red on `corpus/SOURCES.md:[832]` |
| 4 | `accept-ca.py --lands main (1d7add3…)` | **FAIL legs=10/11** — same `APPENDONLY` red |
| 5 | `git diff base..5e4796c --stat -- corpus/SOURCES.md` | empty (Ca's own landing does not touch the registry) |
| 6 | `git show {base,main}:corpus/SOURCES.md \| sed -n '832p'` | `used-by` cell gains `…/worldbuilding-setting-practice.md` — an in-place change |
| 7 | `grep -rn "both land in one tree" --include=*.md --include=*.json --include=*.txt .` | one hit only: `reports/round-74/telemetry/junk-ca.txt:66` |
| 8 | mutant M-A (LC-01 command cell → bogus `echo`) | `NOSTUB` FAIL `stubs=['LC-01:rederive-cmd']`; **ANNOTATE PASS** |
| 9 | mutant M-B (LC-01 command cell bogus + ledger rederive text moved to a note cell) | **ANNOTATE PASS, NOSTUB PASS** — survivor (only `RECEIPTS` red, which is this seat's `TMPDIR` artifact, reproduced on the unmutated baseline) |
| 10 | ledger `observe_cmd` vs `stated_at` path join | **11 of 12 ANNOTATE pairs** do not read their stated site |
| 11 | `git grep -c -E '^. S[0-9]{3}' 65fe857… f7104cb… -- corpus/SOURCES.md` | `724` / `804` — the observation site is `corpus/SOURCES.md`, not `corpus/README.md:36` |
| 12 | `accept-c.py:649` `forbidden_ids = staged_ids - lane_ids` | `{S899, S900}` — staged `S883`/`S884` unguarded at token level |
| 13 | `grep -rn "^ACCEPT-" reports/round-74/telemetry/*.txt` | every PASS has a committed FAIL control; no typed-receipt survivor |
| 14 | `git log 00c408a0..main -- .ufo/waves/round-73/` | empty — the six inherited files are byte-stable |

**Not run / limits, stated.** This seat ran **no live fetch**, so it has no User-Agent to record and makes no
claim about the current on-page state of any source; the re-open duty belongs to the `ScoutReopenS*` seats.
This seat did **not** run the census (`sources-census.sh`), the junk-fixture generator, or the counters'
`--selftest` modes — those are the `ExecCensusEnd` / `ExecJunkReRun` / `ExecSelftest72` seats' instruments and
running them here would have duplicated their work without adding evidence for a *pattern* report. The
`RECEIPTS` leg's `TMPDIR` sensitivity (`accept-ca.py:183`, `RECEIPT_TMP_RE = /(?:var/)?tmp/…`) was observed as a
side effect of this seat's scratch relocation and is recorded above as a **harness artifact**, not as a lane
finding — it is flagged here only so no other seat mistakes it for a defect. **No file outside this seat's
assigned `Report:` path and its named scratch was written.**
