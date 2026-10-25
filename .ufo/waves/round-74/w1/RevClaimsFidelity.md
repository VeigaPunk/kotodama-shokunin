# RevClaimsFidelity — claim-fidelity attack on `reports/round-74/claims.json`

Seat `RevClaimsFidelity` (reviewer, leaf — no dispatch, no background job, no `task`). Round 74, hyaku run 7.
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb` (= lane HEAD; worktree carries the five modified + one
untracked round-73 w2 files and the untracked round-74 scratch dirs — nothing else).

Scope: the two DRAFT claims against `AXES.md`, `LEARNING.md`, `CORPUS.md`, `SOURCES-CONTRACT-v1.md`, and
prompt §9 claim sizing (`.ufo/prompts/kotodama-round-74.md:417-439`). Assignment points (a)–(g) are answered
in §4; findings F1–F21 are in §3.

Nothing was written outside this report. No live fetch was made, so this seat has **no User-Agent to record**;
I re-used the L1's 2026-10-25 captures at `/tmp/q74/` (read-only) and the committed bytes. No tool installed
(pacman not run). Scratch: `/tmp/RevClaimsFidelity-2/` — `base/` (`git archive f7104cb` extract),
`clone73/` (lane clone, detached at `2d1cd91`), `clone73pin/` (same clone, local `main` moved to `2d1cd91`),
`tmp/` (counter `TMPDIR`). **`/tmp` was at 100 % (19 MB free) when this seat started** and a first clone
failed with `fatal: cannot create directory at 'reports/round-62': No space left on device`; other seats'
clones then released space (2.0 GB free) and the retry succeeded. The host `L0 kotodama | round-9`
(`.ufo/l0-questions.md:46`, "`/tmp` inode table is 100 % full") is still live in a different form: the
*space*, not the inodes, is the binding limit for lane clones.

## 1. What I ran (exercise receipts)

| # | command (cwd) | result |
|---|---|---|
| 1 | `find corpus/knowledge -iname '*worldbuilding-setting*' \| wc -l` (`base/`) | `0` — C `before` (a) |
| 2 | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (`base/`) | `804`, last row `S880` — C `before` (b), first half |
| 3 | `grep -cF litmemo.com` / `tuduku.space` / `chinawriter.com.cn` `corpus/SOURCES.md` (`base/`) | `0` / `0` / `0` — C `before` (b), second half |
| 4 | `grep -rlE '設定ノート\|世界観\|世界观' corpus/knowledge \| wc -l` (`base/`) | `0` — C `before` (c) |
| 5 | all 14 `observe_cmd` argv of `.ufo/waves/round-74/drafts/ledger-draft.json` (cwd = lane, read-only git) | every pair red at base: `804≠412`, `10≠9`, `247≠243`, `32≠30`, `95≠94`, `93≠92`, `97656≠23443`, `two≠no`, and LC-04/05/13/14 empty-stdout rc=1 (see F3) |
| 6 | `python3 -B reports/round-73/accept-c.py --root . --lands 2d1cd91… --census-sh /home/vgpnk/…/scripts/sources-census.sh` (`clone73/`) | `ACCEPT-C-73: PASS legs=11/11`, exit 0 |
| 7 | `python3 -B reports/round-73/accept-ca.py --root . --lands 2d1cd91… --fleet-root /home/vgpnk/Projects/shokunin` (`clone73/`, **detached** at lands — the procedure spec item 24 prescribes) | `LEG FAIL STAMP … measured f7104cb… != lands 2d1cd91…` → **`ACCEPT-CA-73: FAIL legs=8/9`**, exit 1 |
| 8 | same command (`clone73pin/`, local `main` **moved to** `2d1cd91`) | `ACCEPT-CA-73: PASS legs=9/9`, exit 0 |
| 9 | `git ls-tree -r --name-only f7104cb .ufo/waves/round-73/w2/` + `git status --porcelain` | 5 of the six files **tracked** at base (`M`), 1 untracked (`??`) — F8 |
| 10 | `git grep -n "9 scenarios" f7104cb` (lane) + `sed -n 10p` of the fleet report at pin `dad39efd` | lane: `LOG.md:4297`, `.ufo/waves/round-73/w2/*` seat reports, `corpus/lessons/round-73*.md`, `reports/round-73/claims.json`; fleet report `:10`; **0 hits in `SCORECARD.md`** — F9 |
| 11 | word count of every `corpus/knowledge/*.md` at base | min **478** (`culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`), median 4306; drafts 4194 / 1989; staged originals 415 / 711 — F11 |
| 12 | `sha256sum` of the six w2 files (worktree, now) | `290a6ccd…`, `dfc8fe0d…`, `db254d88…`, `9469d4d6…`, `079728a5…`, `7d145919…`; mtimes 20:37:02–20:47:30, unchanged since the base commit — F13 evidence block |
| 13 | `grep -c` of the four forced re-quotes in `/tmp/q74/*` | `我先做的是世界观，再考虑怎么升级，再考虑升级的表现。` 1; `把它放在前面大概20章之内慢慢来` 1; `世界観の作り方` 10; `世界観の4つの層` 1; `設定ノートの構成例` 1; `世界観設定の5要素` 1 — the re-quote premise holds |
| 14 | `find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge -name '*.md' \| wc -l` and per-family counts | 40 staged = 2 adopted + 4 path-present + 34 refused; rejects list counts 5+11+3+2+9+3+1 = 34 ✓ — F15 (arithmetic holds; disposition wording does not) |
| 15 | `git -C fleet cat-file -t dad39efd…` + `show <blob> \| sha256sum` | commit exists; blob `000bab3a…` = the ledger's `stated_fleet.sha256` ✓ |

**Not run:** the round-74 counters (they do not exist yet — `reports/round-74/` holds only `claims.json` and
`telemetry/census-start.txt`; `.ufo/waves/round-74/counters/` does not exist), so no round-74 leg has been
scored. No live fetch, no CDX probe (the forced re-quotes were checked against the L1's captures, not
re-fetched).

## 2. Verdict summary

The two claims are the right size, on distinct axes (`coverage` / `calibration`), and their write sets are
**disjoint except `corpus/README.md`**, so causal separability is achievable. Every `before` command for
claim C reproduces exactly at base, and every ledger pair is red at base. Three things are not yet true of the
draft: the **counter path** the closure is told to run does not match the plan (F1), the **round-73 CA receipt**
the Ca claim demands is `FAIL 8/9` under the plan's own clone procedure and `PASS 9/9` only under a construction
the claim never names (F2), and the **absence-observation pairs** in the ledger have no grammar in the frozen
legs (F3). Nine further defects are wording-level but each one lets a control or a closure re-derive a
different verdict than the claim text says.

## 3. Findings

Severity: BLOCKER = as frozen the claim's own one command cannot return the stated after-value; HIGH = a leg,
predicate or control fails to bind what it says; MEDIUM = a before-value/leg is imprecise, unenumerated or
vacuous; LOW = wording that a counter can paper over but a reader cannot.

### F1 — BLOCKER — the counter path in both claims contradicts the plan that builds the counters

`claims.json` tells the closure to run `reports/round-74/accept-c.py` (C `after` and `counter`) and
`reports/round-74/accept-ca.py` (Ca `after` and `counter`). The wave-1 plan (`.ufo/waves/round-74/w1/spec.json`
items 21 and 22) tells the two executor seats to build
`.ufo/waves/round-74/counters/accept-c.py` and `…/accept-ca.py`. `drafts/skill-gates-rows.md:76-77` (the SKILL
gate rows) name the **`reports/round-74/`** path, and `:43` lists both directories as not yet existing, so the
draft already contains both paths; the round-73 precedent is `reports/round-73/accept-c.py`. As frozen, the
closure's one command fails with a missing file, and the SKILL registry row points at a path that may not
exist.

**Rewrite.** Land the counters at `reports/round-74/accept-c.py` and `reports/round-74/accept-ca.py` in the
freeze commit and change the two spec items; or change both `after` strings and both `counter` fields to
`.ufo/waves/round-74/counters/accept-{c,ca}.py`. Either way one path appears in **all four** places: claim
`after`, claim `counter`, SKILL row, freeze commit.

### F2 — BLOCKER — the Ca `RECEIPTS` leg is `FAIL 8/9` under the plan's clone procedure, and typed receipts satisfy it as written

Two independent defects in one leg.

*(a) Reproduced red.* Spec item 24 prescribes: `git clone … "$D/lane"; git checkout -q --detach
2d1cd914…; python3 -B reports/round-73/accept-ca.py --root . --lands 2d1cd914… --fleet-root …`. I ran exactly
that (`clone73/`, run #7 above): `LEG FAIL STAMP … problems=['measured f7104cbc… != lands 2d1cd914…']` →
`ACCEPT-CA-73: FAIL legs=8/9`, exit 1. Cause: `reports/round-73/accept-ca.py` resolves `measured` from the
graded repo's `main` ref, not from `HEAD`. Moving the clone's local `main` to `2d1cd91` (`clone73pin/`, run #8)
gives `ACCEPT-CA-73: PASS legs=9/9`. `drafts/skill-gates-rows.md:243-246` (F4) reaches the same conclusion
independently. So "produced inside a clone materialized at round 73's lands" is **not by itself sufficient**,
and the spec procedure produces a FAIL that a seat may be tempted to file as PASS.

*(b) It is self-attested.* The leg reads a receipt file and checks header strings
(`stamped==evaluated==measured`). Nothing re-executes the round-73 counters, so a hand-typed receipt with the
right five header lines passes, and the same bytes turn LC-04/05/13/14 green. The `do_nothing_control` list
(`--selftest`: stub-row, append-only removal, in-place-outside-allowed, shell-string argv, constant-printer,
min-pairs, config-edited) contains **no typed/edited-receipt control**.

**Rewrite (leg).** `RECEIPTS: the counter materializes a clone of <lands>, sets that clone's local main to
2d1cd9140d3a6c42296d71e4f29587582a4a88c0 (`git checkout --detach` then `git update-ref refs/heads/main
<lands73>`, or `--main 2d1cd914…`), runs `python3 -B reports/round-73/accept-c.py --root . --lands <lands73>
--census-sh <fleet>/scripts/sources-census.sh` and `python3 -B reports/round-73/accept-ca.py --root .
--lands <lands73> --fleet-root <fleet>` inside it, requires exit 0 and the exact lines `ACCEPT-C-73: PASS
legs=11/11` / `ACCEPT-CA-73: PASS legs=9/9`, and requires the committed receipt at
reports/round-74/telemetry/<name>.txt to carry that stdout verbatim with stamped==evaluated==measured==
<lands73> and the round-73 counter sha256 (95aee881… / 222d4dd6…); the clone construction and the pinned main
ref are printed in the receipt header.` **Rewrite (control).** add to `do_nothing_control`: "a receipt whose
stdout does not byte-match the counter's re-run (typed or edited) FAILS RECEIPTS" and commit that receipt.

### F3 — HIGH — the absence-observation pairs have no grammar in the frozen legs, and `BASEMISMATCH` forbids them

`ledger-draft.json` LC-04, LC-05, LC-13, LC-14 observe "no PASS receipt exists": `git grep -c -E
'^ACCEPT-C-73: PASS legs=11/11$' HEAD -- reports/round-73/telemetry` returns **rc=1, empty stdout** at base (I
ran all four, run #5). The round-73 counter classifies empty stdout with a non-zero exit as *unobservable* and
`BASEMISMATCH` **fails closed**; the r74 draft keeps the same wording ("none is unobservable") but adds no
absence rule. The claim's `before` also names "no committed PASS-at-lands receipt for ACCEPT-C-73 /
ACCEPT-CA-73" as a *pair*, so the two texts cannot both hold.

**Rewrite (preferred, smaller):** delete LC-04/05/13/14 from the ledger; keep the absence solely in the
`RECEIPTS` leg; and change the purpose in `before` to "…and the committed round-73 telemetry holds zero PASS
verdict lines (only `FAIL legs=1/11`, `FAIL legs=4/9`×2, `FAIL legs=5/9`)". The remaining 10 pairs still meet
`>= 10`, but with zero margin — add one observable spare (sweep C's `LC-16`: `readme`/lesson UA pair) so the
floor is 11.
**Rewrite (alternative, if the pairs stay):** freeze the rule in `LEDGER` **and** `BASEMISMATCH`:
"for an argv whose first two words are `git grep` and whose flags contain `-c`, no match (exit 1, empty
stdout) yields the token `0`; this is the only absence rule and it is printed as `absence=git-grep-c` in the
receipt header."

### F4 — HIGH — `RECEIPTS` and the ledger disagree about where the round-73 receipts live

`RECEIPTS` says `reports/round-74/telemetry/` carries the receipts. LC-04/05/13/14 grep **only**
`reports/round-73/telemetry` (`-- reports/round-73/telemetry`). A receipt written where the claim says it
lives never turns those pairs green; a receipt written where the pairs look is a new file in a round-73
directory that the claim does not mention. Sweep C's proposal had both dirs in the pathspec
(`-- reports/round-73/telemetry reports/round-74/telemetry`).

**Rewrite:** name one canonical path, e.g. `reports/round-74/telemetry/accept-c-73-at-lands.txt` and
`…accept-ca-73-at-lands.txt`, in `RECEIPTS`, in the ledger `why`, and in the pair pathspec
(`-- reports/round-73/telemetry reports/round-74/telemetry`); say in the `why` that the round-73 directory is
read only, never written.

### F5 — HIGH — `SEPARABLE` does not enumerate its read set, and `corpus/README.md` is a real C↔Ca collision

The leg says "no byte the Ca legs read cites an S-id >= S881, names a claim-C path
(`worldbuilding-setting-practice*`), or reads a claim-C file". Round 73's counter enumerated its read set
(`ledger`, `corrections-rows`, telemetry receipts whose basename contains `ca`); round 74's text defines none,
which matters because:

1. `reports/round-74/telemetry/` is a **shared directory** — C commits `gap-sweep.txt` and `census-end.txt`
   there, and `census-end.txt` names rows `S881..S884`. A directory-wide scan fails Ca because of C.
2. Ca pairs LC-06 and LC-07 read `corpus/README.md`, and C's landing rewrites that file (plan item 19:
   index rows, a `Total knowledge entries: 249.` footer, a gap note) — `drafts/readme-rows.md` §§1–3.
3. `REPAIR` reads the statement at `<lands>` **"last occurrence"**; C appends a new `Total knowledge entries:`
   footer, so a REPAIR pair on any README count line would be graded against C's number. (Today LC-06/07 are
   ANNOTATE, so this is a latent hole the leg text permits.)
4. `ANNOTATE` says "the observed token **at <lands>**" while `SEPARABLE` says count pairs measure at the
   pinned base revision. Both are satisfiable only because every argv hardcodes `f7104cb` or `HEAD`; the text
   should say so.

**Rewrite (leg).** `SEPARABLE: the Ca read set is exactly {the ledger text at <freeze>, every SCORECARD line
under "## Corrections — round 74" that names a pair id, the telemetry receipts and controls named in
claims.json's Ca section, and the stated_at line of every pair}; no byte in that set cites a lane S-id >= S881
and no stated_at path is corpus/SOURCES.md, corpus/knowledge/**, corpus/lessons/round-74.md,
reports/round-74/evidence/** or .ufo/waves/round-74/assimilation/**; a REPAIR pair's stated_at is never a line
whose last occurrence claim C appends to (corpus/README.md totals/footers); every observation is the token the
pair's observe_cmd returns in the clone at the graded revision, and the ledger names that revision.`
**Rewrite (related, C):** see F7 — claim C must own the README edit it lands.

### F6 — HIGH — `APPENDONLY` authorizes in-place edits at file granularity and omits a frozen file it reads

`APPENDONLY: … in-place edits permitted only in files a ledger REPAIR pair names`. LC-09/LC-10 are REPAIR pairs
on `SKILL.md`, so **all of SKILL.md** becomes in-place-editable — deletion of any SKILL row would not be a
"removed line in LOG/SCORECARD/lessons". Round 73's counter authorized in-place edits only inside a named span
(`SKILL.md "## Gates and probes"`, a README footer). Separately, LC-12's stated_at is
`reports/round-73/claims.json:11`, which is in **no** zero-removals set, so a seat could "repair" the frozen
round-73 predicate instead of annotating it — the exact round-69 Ca2 class the `kill_rule` says it avoids.
`corpus/lessons/round-74.md` is also absent from the set, so a Ca-side scribe could delete claim C's `## Gate`
(F5 of the C side).

**Rewrite.** `APPENDONLY: base..<lands>, zero removed lines in LOG.md, SCORECARD.md,
corpus/lessons/round-74.md, corpus/lessons/round-73.md, corpus/lessons/round-72.md,
reports/round-73/claims.json and reports/round-73/ledger.json; the fleet round-73 report at the ledger's
fleet_pin is byte-identical to the blob its sha256 names; in-place edits are permitted only on the stated_at
line of a REPAIR pair and only to the token its statement_after parse names (line-level: changed lines ⊆
{REPAIR stated_at lines} ∪ appended lines).`

### F7 — HIGH — claim C lands a `corpus/README.md` rewrite that no C leg grades

Plan item 19 and `drafts/readme-rows.md` write the README index rows, the gap note and a new footer
(`Total knowledge entries: 249.`, vector `32/29/40/29/24/95`). C's twelve legs read `corpus/SOURCES.md`, the
two entries, the lesson, the evidence files and telemetry — **not** `corpus/README.md`. So the round changes
the coverage map without a leg on it, and `LEARNING.md`'s expansion observable requires "each citing its
coverage-map row". This is also what makes the README collision in F5 possible.

**Rewrite (new C leg, label `INDEX`).** `INDEX: each adopted entry has exactly one row in
corpus/README.md's partition section, the row body is the entry's own "- topic:" text verbatim under the
`` - `name.md` — `` prefix, and the last `Counts checked` block's totals equal the lands tree
(`find corpus/knowledge -type f -name '*.md' | wc -l` = the stated total; per-directory vector = the six
partition counts); the older totals blocks are unchanged.` Then record in the Ca `SEPARABLE` sentence that
`corpus/README.md` is C-owned (F5).

### F8 — MEDIUM — Ca `before` misstates the inherited state: five of the six files are **tracked**, not absent

The `before` says "the six `.ufo/waves/round-73/w2` files modified/untracked in the worktree **and absent from
the pushed tree**". `git ls-tree -r --name-only f7104cb .ufo/waves/round-73/w2/` lists
`CritEntryAmendFinal.md`, `ExecSelftestAll.md`, `ScribeLogScorecard.md`, `SimplifierEntries.md` and
`drafts/log-entry.md` (all `M`, base blobs `eeb3344…`, `20df0f0…`, `7fd5ae0…`, `5afdac5…`, `3e9af53…`); only
`RevengerOrigins.md` is `??` and absent from every tree. "Absent from the pushed tree" is therefore true of
one file, not six, and the before-value as written cannot be re-run to the stated value.

**Rewrite.** `the worktree carries six changed files under .ufo/waves/round-73/w2/: five tracked files whose
bytes differ from their base blobs (git status --porcelain: M CritEntryAmendFinal.md, ExecSelftestAll.md,
ScribeLogScorecard.md, SimplifierEntries.md, drafts/log-entry.md) and one untracked file absent from every
tree (RevengerOrigins.md); the six worktree sha256 are pinned in the ledger's must_track`.

### F9 — MEDIUM — Ca `before` names `SCORECARD` for a token that only `LOG.md` and the fleet report carry

`git grep -n "9 scenarios" f7104cb` → `LOG.md:4297` and the fleet report
`.ufo/reports/round-73/kotodama.md:10` (pin `dad39efd…`, blob `000bab3a…`); **no hit in `SCORECARD.md`**
(`SCORECARD.md:1430-1431` are the `PASS legs=11/11` / `PASS legs=9/9` statements). A before-value must name
the file it is true of.

**Rewrite.** `report/LOG '9 scenarios' vs selftest-r3.txt 'SELFTEST OK: 10 scenarios'` → `LOG.md:4297 ("Ca 9
scenarios") and .ufo/reports/round-73/kotodama.md:10 at fleet pin dad39efd… vs
reports/round-73/telemetry/selftest-r3.txt:6 ("SELFTEST OK: 10 scenarios")`.

### F10 — MEDIUM — C `before` (a)'s parenthetical is false

`(README names worldbuilding only as a method label on other entries)`: `README.md:6` and `SKILL.md:3` name
"Linguistic-cultural worldbuilding" as the lane's **domain**, and `corpus/README.md` uses "worldbuilding
method" as a label on many rows. The count of zero files is right; the gloss is wrong.

**Rewrite.** `(the domain line README.md:6 and SKILL.md:3 frame the lane as "Linguistic-cultural
worldbuilding", and corpus/README.md uses "worldbuilding method" as a label on other rows; no file or index
row governs setting practice)`.

### F11 — MEDIUM — the `ENTRIES` length floor admits a stub at 479 words

`a body at least as long (in words) as the smallest corpus/knowledge entry at base` = **478 words**
(`culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`, 478 words, 23 lines; next 639). The
declared junk control is "two stub entries with a header" — it only fails if the stubs are shorter than 478
words. A 500-word boilerplate entry with the nine header fields satisfies `ENTRIES`; the legs that would
catch its content (`GATE`, `EVIDENCE`) are satisfied by copying any located quote (F12). The staged originals
are 415 and 711 words, so "as long as the staged file" would be a *weaker* floor, not a stronger one.

**Rewrite.** State the measured floor in the leg (`… the smallest corpus/knowledge entry at base, 478 words at
f7104cb`) and specify the control at a length that must fail (`two 400-word stub entries`). Then state the
honest limit in the claim: `ENTRIES is a length-and-shape gate only; content fidelity is carried by GATE,
EVIDENCE and the non-author re-open, not by this leg.` If a content floor is wanted, use each entry's own
`## `-section count and its cited-row count (both checkable) rather than word count alone.

### F12 — MEDIUM — `EVIDENCE`'s sha256 cannot be checked against what is stored

The leg demands "a 64-hex sha256 **of the fetched body**" and "the body window around the quote stored
verbatim", then checks only "the Gate quote occurs inside that stored window". A digest of the full body and a
stored window are different objects, so the digest is decorative — round 73's implementation confirms the
pattern (`reports/round-73/accept-c.py`, `leg_evidence`: `re.match(r"^[0-9a-f]{64}$", …)` only). The evidence
file is therefore a seat-authored claim, not a check.

**Rewrite.** `EVIDENCE: reports/round-74/evidence/<id>.txt carries fetch line, browser-shaped UA, HTTP 200,
bytes, the sha256 **of the stored body**, and the body (full, or ≥4 KiB around the quote) verbatim; the counter
requires sha256(stored body) == the recorded digest, the Gate quote inside the body, and the body's own
byte count == the recorded `bytes`.` (Residual stated in the claim: an offline counter cannot prove a fetch
happened; that is the non-author re-open's job.)

### F13 — MEDIUM — `TRACKED`'s "worktree-at-base content" has no witness after the freeze

The pin is a sha256 in a ledger that the same seat writes, and the only time a verifier can compare the pin to
the actual worktree is **before** the freeze. After the landing no committed object witnesses the pre-freeze
bytes. Recorded here so the closure can use it — at base today, and unchanged since the base commit
(mtimes 20:37:02–20:47:30):

```
290a6ccd839cb8cd09fc5089d1360dc4bcfabdea38f7a83733063159185c50aa  CritEntryAmendFinal.md
dfc8fe0d2c54442bd5fa1a8f122c37751b89c861aeec2b5e77c041f66c11e71c  ExecSelftestAll.md
db254d8896d7cbce3377dc1d3f56ca41312063383a9c319324bf1c1a02e445b3  ScribeLogScorecard.md
9469d4d689aeb1f32a4127b9d2a0388236c622d206995df4ff8f11a201bdd481  SimplifierEntries.md
079728a53490714a350ec17195bc72b1034d1878130b6f491a200de53bf6ca6a  drafts/log-entry.md
7d14591923aff7b1dd5a28bc73d4933faf9cf721e4a7b113f6f7178206d581ed  RevengerOrigins.md
```

`ledger-draft.json`'s `must_track` is a bare path list; the claim requires sha256, so the freeze must write
`[{path, sha256}]` with exactly the six values above.

**Rewrite (stronger, recommended).** Commit the six files in the **freeze** commit (they carry no round-74
data; they are inherited seat output) and define `TRACKED: the six paths are tracked at <freeze> and at
<lands> with identical blob ids, non-empty, equal to the ledger's sha256`. The leg is then re-derivable over
committed bytes for ever, and the round-73 "late seat writes after the push" defect is closed at the earliest
possible point. If they stay uncommitted until landing, keep the sha256 pin **and** say in the leg that its
pre-freeze provenance is witnessed by the wave-1 seat table (`ScoutLedgerSweepC.md` §1) plus this report.

### F14 — MEDIUM — both do-nothing controls are aimed at `lands == base`, which can only fail `FROZENCFG`

`<freeze>` is by construction a child of base (it commits claims, ledger, counters, controls). `lands == base`
therefore cannot satisfy "freeze is a strict ancestor of lands", so the control reds on the config guard — per
`drafts/skill-gates-rows.md:76` (FROZENCFG → exit 1) or, if the counter exits 2 on a bad ancestor, as an input
error. Either way the control never scores `ENTRIES`/`ROWS`/`REPAIR`/`ANNOTATE`/`TRACKED` and proves nothing
about a do-nothing *landing*.

**Rewrite (both claims).** `do_nothing_control: reports/round-74/telemetry/controls-<c|ca>.txt: (1) lands ==
<freeze> — a legal ancestor relation — FAILS with the substantive legs red (C: ENTRIES, ROWS, GATE, EVIDENCE;
Ca: REPAIR, ANNOTATE, RECEIPTS, TRACKED) and no other leg red for a reason the control introduces; (2) lands ==
base FAILS on FROZENCFG; plus the junk-landing controls (…).`

### F15 — MEDIUM — `REJECTS`' universal set does not cover the four staged files that are present by path only

`REJECTS: … each not-adopted staged file/family listed in rejects` — but of the 40 staged knowledge files, 4
are **not adopted this round and not in `rejects.refused_files`**: `culture-material/heritage-taxonomy-models.md`,
`culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`,
`linguistics/conlang-scholarship.md`, `linguistics/conlang-scholarship.amend-2026-10-23.md`. All four exist in
the lane by path, but their **staged bytes differ** from the landed ones (staged `b17223b9…` / `9ed5ceef…` /
`ce666a2b…` / `8f889666…` vs lane `09175b18…` / `8544fe1e…` / `fe7e214a…` / `01029a64…`), so "already in the
lane" is a path statement, not a byte statement. The arithmetic does add up (2 adopted + 4 path-present + 34
refused = 40), but the leg's universal misses four files.

**Rewrite.** `REJECTS: of the 40 staged knowledge files under merge/kotodama/knowledge, exactly 2 are adopted
this round (the two entries in `entries`), exactly 4 are path-present with staged bytes that differ from the
lands copy (heritage-taxonomy-models.md, heritage-taxonomy-models.amend-2026-10-24-r13.md,
conlang-scholarship.md, conlang-scholarship.amend-2026-10-23.md — reason: the lane's re-grounded copy
supersedes the campaign copy; flip: a re-staged diff against the lane's current bytes), and the remaining 34
are refused (narrative-structure-frameworks 5, naming-systems 11, calendar-festival-systems 3,
era-periodization-models 2, verification 9, conlang-scholarship amendments 3, conlang-methodology 1), each with
reason and flip in the lesson; the lesson states the counts 2/4/34.`

### F16 — LOW/MEDIUM — neither `after` is one concrete value

Section 9 asks for "one concrete value"; the draft writes `PASS legs=<n>/<n>` (C; `n fixed at freeze`) and
`legs=<n>/<n>` (Ca; no qualifier at all). The leg counts are already known from the claims themselves: C = 12
(`ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK,
FROZENCFG`), Ca = 11 (`LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, NOSTUB, SEPARABLE, TRACKED,
RECEIPTS, FROZENCFG, STAMP`). The spec items and the SKILL draft use the same two label lists, so the
plan/leg/label identity holds — only the value is vague.

**Rewrite.** `prints ACCEPT-C-74: PASS legs=12/12` and `prints ACCEPT-CA-74: PASS legs=11/11`, with a counter
guard: `a leg table whose length != the frozen leg count FAILS (leg LEGCOUNT)` — so deleting a leg cannot
raise the fraction.

### F17 — LOW — `FROZENCFG` names one source for constants that live in two files

`FROZENCFG: row set, entry paths, fragments, map and every constant … read from claims.json AT <freeze>`
contradicts the C `after`, which puts the map at
`.ufo/waves/round-74/assimilation/id-renumber-map.json` (committed pre-data). Today only
`.ufo/waves/round-74/w1/id-map-draft.json` exists.

**Rewrite.** `FROZENCFG: row set, entry paths, fragments and every constant are read from
`git show <freeze>:reports/round-74/claims.json`; the by-document map is read from
`git show <freeze>:<map path>` where the map path **and its sha256** are fields of claims.json; never from the
graded tree; <freeze> is a strict ancestor of <lands>.`

### F18 — LOW — three predicates are undefined words

`no E-codes` (CENSUS), `no placeholder values` (ENTRIES), `no placeholder token` (NOSTUB). Each is a universal
with no enumerable set.

**Rewrite.** `CENSUS … with no line matching ^E[0-9]{2}\t in the census TSV`; `ENTRIES … no header field value
in {TODO, TBD, FIXME, XXX, n/a, ?, —} and no field value matching <[^>]+>`; `NOSTUB … the same token list`.

### F19 — LOW — the fleet-report half of `APPENDONLY` is vacuous

`the fleet round-73 report is the blob at the ledger's fleet_pin with zero removed lines` — a single blob has
no removed lines, and the lane never writes the fleet tree. Verified as a fact: pin `dad39efd…` is a commit,
blob `000bab3a…` = the ledger's `stated_fleet.sha256`, line 10 carries the quoted sentence. Keep it as a
pin-identity check, not as an append-only check.

**Rewrite.** `the fleet round-73 report at the ledger's fleet_pin (dad39efd…) is byte-identical to the blob
its sha256 names (000bab3a…), and this lane writes no byte under the fleet root (the counter reads it with
git -C <fleet> show only).`

### F20 — MEDIUM — `S877` / `APPENDONLY` consistency (item (g)): consistent, but the leg verifies the wrong thing

The in-place `used-by` change **is** contract-legal: `SOURCES-CONTRACT-v1.md:48-51` — "Only `status`,
`recheck` and `used-by` change in place, and each change is logged old→new in the round lesson. A correction is
a new row whose `teaches` opens `supersedes S0NN —`." Ca's `APPENDONLY` set does not include
`corpus/SOURCES.md`, so C's edit does not violate it; C's `ROWS` leg authorizes exactly one in-place cell. Two
gaps remain: (i) `ROWS` checks *which* cell moved, not its value, so a junk landing could set `used-by` to any
path that exists (census E11 only checks existence); (ii) the lesson's old→new log (contract rule 2) is not a
leg.

**Rewrite.** `ROWS: … the only in-place registry change is S877's used-by cell, which at <lands> equals its
base value plus exactly the new entry path(s) whose source: line cites S877 (parsed from both revisions), and
corpus/lessons/round-74.md records that cell old→new (SOURCES-CONTRACT-v1.md rule 2); every other row is
byte-identical base..<lands>.`

### F21 — LOW — the axes note is accurate but the lowest-axis obligation stays formally open

`axes_note` cites `SCORECARD.md:13-15` for "no numeric scores" (verified: the 0–10 estimates were retired) and
`.ufo/l0-questions.md:47` for the freshness pause (verified: "Freshness axis-move claims are paused until
ruled"; the row is still unanswered). `AXES.md` requires one claim on the lowest non-retired axis *or* the
stagnation-nudge waiver, and the note claims no waiver. The round therefore works `coverage` + `calibration`
and none on `freshness`, under a lane-filed pause. This matches round 73's admitted shape, so I record it as an
open obligation, not a defect — the exit is an operator ruling on row 47, not a claim rewrite.

**Suggested one-sentence addition to `axes_note`.** `The freshness pause is a lane-filed L0 disposition
(.ufo/l0-questions.md:47, unanswered); this round claims no waiver and no freshness move, and the round's
admission does not rest on the pause being ruled.`

## 4. Direct answers to (a)–(g)

**(a) Every before-value re-runs over committed bytes and returns the stated value NOW at base?**
C: **yes, all three**, exactly (runs #1–#4). Ca: **no, two of three**. The `9 scenarios` pair is right about
the token but names the wrong third file (F9); the six-file pair misdescribes five files as absent from the
pushed tree (F8). The ledger pairs themselves are all red at base — I ran every `observe_cmd` (run #5), with
LC-04/05/13/14 red only via the unfrozen absence rule (F3).

**(b) Universal clauses enumerate their sets?** Mostly yes, with these exceptions: `SEPARABLE`'s "no byte the
Ca legs read" (F5), `REJECTS`'s "each not-adopted staged file/family" (F15, four files outside the set),
`APPENDONLY`'s "in-place edits … only in files a REPAIR pair names" (F6: a file is not a location), and the
undefined `no E-codes` / `no placeholder` (F18). `ROWS`'s "used-by exactly the citing entries" enumerates the
four new rows but not S877 (F20). The rest are enumerated: the four rows, the two entries, the five cited
rows, the six fragments/terms, the six must_track paths, the two receipts, the four listed files.

**(c) Separable (QUALITY 7 / AXES "causally separable")?** **Yes in principle, one file short.** C's twelve
legs read no Ca-written byte (claims.json at freeze, SOURCES.md, the entries, the lesson Gate, evidence,
gap-sweep, the census, the scratch mirror). Ca's eleven legs read no C-written byte **except**
`corpus/README.md` (LC-06/07, and the latent REPAIR hazard) — and C's own legs never grade that file (F5, F7).
Fix F5 + F7 and each claim verifies without the other landing, in either order. The shared `freeze` commit is
infrastructure, not the other claim's landing.

**(d) Plan sentence == counter leg == receipt label?** The label sets match exactly (12 and 11, same names in
`claims.json`, spec items 21/22 and `drafts/skill-gates-rows.md:76-77`), but three identities break:
the **counter path** (F1), the **one concrete after-value** (F16), and the **observation revision** wording
(REPAIR/ANNOTATE say "at <lands>" while the ledger pins `f7104cb` or `HEAD` — F5.4, satisfiable only because
the argv pin, so the text must say it).

**(e) Do-nothing reachable? Can a junk append or stub commit pass?** The *targets* are not reachable by doing
nothing (C needs two entries, four rows, a Gate and evidence; Ca needs the repairs, the annotations and the
receipts), **but** the controls as written do not demonstrate it: `lands == base` reds only on `FROZENCFG`
(F14); a typed receipt passes `RECEIPTS` and four pairs (F2b); a 479-word stub passes `ENTRIES` (F11); an
evidence file with a fabricated window passes `EVIDENCE` (F12); and a SCORECARD/SKILL rewrite of any length
passes `APPENDONLY` once a REPAIR pair names the file (F6).

**(f) Does Ca depend on files Ca must create, and is that circular?** `RECEIPTS` **is** circular as written —
the receipt is the claim's own artifact and the leg only reads its header, so the leg's truth is the seat's
assertion (F2). It stops being circular the moment the counter re-executes the round-73 counters in the
pinned clone and compares stdout (run #8 proves that is achievable: `PASS 9/9`). `TRACKED` is **not**
circular — the six files are inherited round-73 output, not Ca's product — but its provenance is only
checkable pre-freeze unless the freeze commits the bytes (F13).

**(g) `S877 in-place used-by` vs the APPENDONLY set (CORPUS rule 2)?** **Consistent.** `SOURCES.md` is not in
Ca's zero-removals set, and `SOURCES-CONTRACT-v1.md` rule 2 explicitly allows in-place `used-by` with an
old→new log in the round lesson. C's `ROWS` permits exactly that one cell. The leg should nevertheless verify
the *value* and the log rather than the cell's identity (F20), and the "corrections are new entries, never
rewrites" rule (CORPUS.md, aggregator/lane collision rule) is not touched because the registry row is not a
lesson/correction entry.

## 5. What is already sound (so the L2 does not re-open it)

- C's ground is real and independently reproduced: 0 `*worldbuilding-setting*` files, 804 rows ending `S880`,
  0 host occurrences, 0 CJK-term files at base.
- The forced re-quote premise holds: all four quoted spans are present verbatim in the 2026-10-25 captures at
  `/tmp/q74/` (run #13), including the two chinawriter paragraphs the register had refused (`S816`/`S817`).
- The by-document map is a hypothesis, and the ids are joined by URL only; `staged S882` (Sidorova booklet) is
  correctly not appended, and the lane's `S877` already names that document (`philol.msu.ru` + archive
  capture in the source cell). The two new entries cite `S877, S881, S882` (base entry) and `S883, S884`
  (amendment) — five rows, matching `row_set` + `reused_rows`.
- Both round-73 counters pass at their own lands (11/11 and 9/9), so the Ca receipt the round promises is
  producible — with the pinned-`main` construction (F2a).
- The staged-package arithmetic is exact: 40 files = 2 adopted + 4 path-present + 34 refused; the refused
  family counts (5/11/3/2/9/3/1) are all correct at the package (`run #14`).
- `row_set`/`reused_rows`/`entries` contain no campaign-origin id presented as a lane id; the collision risk is
  in the *prose* only (`staged S882` vs `lane S882` = tuduku, both spelled `S882` — see §6).

## 6. Residual risk and verification gaps

1. **Namespace homonym in the claim prose.** `staged S882` (Sidorova booklet) and `lane S882` (tuduku) are
   both written `S882` in the C `after` sentence. A counter that resolves by URL is safe; a human is not.
   Recommend `staged cS882` (or "staged S882 (Sidorova)") in the claim and in the lesson.
2. **Self-attested fetching** remains the claim C residual even after F12: no offline counter can prove a fetch
   happened. The only real defenses are the non-author re-open and the committed body digest.
3. **Nothing here scores the round-74 counters** — they do not exist yet (F1). Every leg in §3 about
   implementation is a requirement on those files, not an observation of them.
4. **`/tmp` is at ~99 %** (other seats' clones). A freeze-time clone plus two counter materializations plus the
   round-73 receipt clone need ~1 GB; this seat's clone only succeeded on a retry. Not a claim defect; report
   to the L1 so the freeze does not fail on `No space left on device`.
5. **Not exercised:** live re-fetch of the four pages (no UA to record — I read the L1's captures), the CDX
   positive-control probes (claim C's `EVIDENCE`/`GATE` premise, already probed by `ScoutWayback`), and the
   round-74 `--selftest` (no counter). The two round-73 counter runs (#6–#8) are the only executions I add.
