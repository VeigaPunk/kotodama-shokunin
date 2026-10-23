# ReportFrag2 — round-64 wave-2 lane report refresh

Seat: `kotodama-r64.ReportFrag2` (scribe). Lane repo
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated; read-only git
use; no commit, no jj/index mutation). Base `ff30a205c8d23b35f1ac533740121a955a9fda96`,
declaration commit `097c21d`. Report date 2026-10-23 (local clock at writing
23:56).

**Axes judged:** coverage, operability, calibration.

**Base refreshed:** `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReportFrag/report-skeleton.md`
(wave-1 skeleton, 317 lines). The refreshed skeleton is reproduced in full at
the end of this report (§4).

**Nothing in this report asserts that a claim predicate passes.** The only
predicate verdicts stated are (a) the ACCEPT-CA-64 run this seat executed
against working-tree bytes, with its counter sha named, and (b) the
ACCEPT-C-64 FAIL that follows mechanically from the claim-C lands being
absent. The authoritative verdicts belong to the integrator's run against the
committed bytes.

---

## 1. Behavior

Refreshed the round-64 lane report skeleton with wave-1 and wave-2 evidence:
the claims paragraph (predicates unchanged), wave sections (wave 1 = 32/32
seats with role mix and key verdicts; wave 2 = in flight), a defect-and-repair
table (defect → forcing receipt → repair seat → verification seat), and
Sources-and-frontier numbers recomputed from the **final** staged rows rather
than from the wave-1 draft. TBDs are reserved for post-commit items only.

No product file was edited by this seat. The only lane write is this report.

---

## 2. Commands executed (this seat) and outcomes

All commands ran from the lane root, read-only, on 2026-10-23 between 23:40
and 23:56 local.

| Command | Outcome |
|---|---|
| `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` (23:41, 23:52 ×2, 23:54, 23:56) | `CHECK-ROWS: 32/32 clean` at 23:52/23:54/23:56; **29/32 at 23:51** (S728 `bullet_shape`, S739 `quote_words=5 in_order=0`, S742 `bullet_shape`) — a transient state while `FixRowsS728S742`/`FixRowS739` were mid-write; self-cleared at 23:52 |
| `python3 -B reports/round-64/accept-ca.py --root .` | **ACCEPT-CA-64: PASS**, exit 0, all 7 legs PASS, counter sha `a8088092cf62107566b5bdcb3b34af65b750e8e46899742514724c4f34f9060c` (rev2 working-tree bytes) |
| `python3 -B reports/round-64/accept-c.py --root .` | **ACCEPT-C-64: FAIL**, exit 1 (FILE/ROWS/REJECTS/ONEID/APPEND/NOHARM/SWEEP/LIVE FAIL; RESTATE/HOSTS/LINK vacuously PASS on 0 lines) — the claim-C lands are absent, so this is the expected pre-land state, not a defect finding |
| `python3 -B reports/round-64/accept-o.py --root . --only NOSUCHLEG` | `ACCEPT_O_INPUT_ERROR unknown --only leg(s): NOSUCHLEG`, **exit 2** — the wave-1 H1 fail-open is closed in the current working-tree counter (rev4) |
| `python3 -B reports/round-64/accept-o.py --root . --only EDGE_SCHEMEREL,EDGE_SLASHLESS` | `EDGE_SCHEMEREL PASS`, `EDGE_SLASHLESS PASS`, `ACCEPT-O-64: PASS`, exit 0 (two-leg slice only; **not** a full run and not an MUT verdict) |
| `python3 -B reports/round-64/accept-o.py --root . --only MUT` (255 s, counter sha `6d9c9354…`) | **`MUT FAIL bad=["m5:EDGE_SCHEMEREL isolation=[…]"] mutants=10`** → **`ACCEPT-O-64: FAIL`** (pre-repair bytes; see F-9) |
| `python3 -m py_compile` on the rev4 `m5` mutant built by the counter's own `replace(needle, repl, 1)` (pre-repair) | **FAIL** — `IndentationError: unexpected indent (line 605)`; mutant sha256 `795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6` |
| `python3 -B reports/round-64/accept-o.py --root . --only MUT` (255 s, **repaired** counter sha `760ddd4d…`) | **`MUT PASS bad=[] mutants=10`** → **`ACCEPT-O-64: PASS`** (F-9 step 3) |
| `python3 -m py_compile` on the repaired m5 mutant | **OK**; mutant sha256 `f04dc0029ed89fc35abd36564907ab2e47c1b44ca0baed4b7528327b5de3e710` |
| rebuilt m1 (sha256 `545205e3…`) run against all seven EDGE legs | `EDGE_SCHEMEREL FAIL`, `EDGE_USERINFO FAIL`, `EDGE_HTTPS FAIL`, `EDGE_MALTARG PASS`, `EDGE_SLASHLESS PASS`, `EDGE_308 PASS`, `EDGE_5TH200 PASS` — **three failures for a one-leg pin** (F-10) |
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | **643** (registry rows; claim-C append not landed) |
| `find corpus/knowledge -name '*.md' \| wc -l` / `find corpus/knowledge/linguistics -name '*.md' \| wc -l` | **237** entries / **29** linguistics files (entry not landed) |
| `git show ff30a205:corpus/SOURCES.md` (leads/search-log sections) | `## Leads (unopened)` 38 bullets, `## Search log` 5 bold-led paragraphs — **byte-identical to base** (md5 of lines 709–740 equal) |
| `sha256sum reports/round-64/accept-{c,ca,o}.py` | `073e9716…` (C rev3), `a8088092…` (Ca rev2), `6d9c9354…` (O rev4) — all three **uncommitted working-tree** counters |
| `sha256sum reports/round-64/claims.json` vs `git show 097c21d:reports/round-64/claims.json` | identical (`e970aace…`) — the declaration is still the committed rev-0 text |
| `git diff -U0 corpus/SOURCES.md` | one hunk, `@@ -642 +642 @@` — S687 status `mined → queued`, **unstaged** |
| `git status --short` | `M LOG.md`, `M SCORECARD.md`, `M corpus/LOG.md`, `M corpus/SOURCES.md`, `M reports/round-64/accept-c.py`, `M reports/round-64/accept-ca.py`, `?? reports/round-64/accept-o.py`, `?? reports/round-64/mutants/`, `?? reports/round-64/telemetry/*` (10 receipts), `?? reports/round-63/telemetry/revisions.txt`, `?? .ufo/waves/round-64/**` |
| `python3 -c …` over the 32 staged `row.txt` files | tier/status/kind/used-by histograms (see §5) |
| `python3 -c …` duplicate-URL scan: 32 staged live URLs vs registry | 32 distinct staged live URLs, **0 collisions** with `corpus/SOURCES.md` |

---

## 3. Findings (this seat's own measurements)

**F-1 — The three claim-O receipts on disk are stale against the current
counter.** `reports/round-64/telemetry/{final-measures-o,mut-o,edge-o,control-o}.txt`
all carry the header line `# counters: reports/round-64/accept-o.py (revision 3)
sha256 c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18`, but the
working-tree counter is now **rev4**, sha `6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1`
(rev4 = m5 isolation + unknown-`--only` exit 2). The receipts therefore bind to
instrument bytes that are no longer the instrument. `final-measures-o.txt` does
record a complete 23-leg PASS run with `ACCEPT-O-64: PASS` / `exit=0`, but that
run measured rev3. **[INFERENCE]** the receipts must be regenerated against rev4
before they can support the O predicate; no rev4 full run was executed by this
seat.

**F-2 — `reports/round-64/mutants/m5.py` is rev3 bytes.** Byte comparison shows
`mutants/m5.py` equals the **rev3** m5 mutant (single-line `urljoin(current, "/" + location.strip())`
replacement) and **not** the rev4 m5 (the paired `urlsplit` branch). The other
nine mutants were not re-checked individually. The `mutants/` directory is
therefore partly stale w.r.t. rev4.

**F-3 — `claims.json` described S744–S749 as all rejected; CORRECTED at 00:03
by the L1 (records patch), so this is now closed.** The committed declaration
text said "six rejected rows S744-S749" and exported "S744-S749 (rejected)",
while the final staged rows are **3 rejected (S744, S745, S747) + 3 queued
(S746, S748, S749)**. The working-tree counter `accept-c.py` was already
revised to accept both dispositions (rev1, REJECTS leg). The L1's records
patch (visible in `git diff reports/round-64/claims.json`) changes the
exports line to "S744-S749 (three rejected + three queued candidates)" and
adds a `statement_patch` field naming `CriticClaimsJson` and `CounterDrift`
HIGH-3 as the forcing controls, while stating that the frozen predicate
sentence and all legs are unchanged. Verified at 00:20.

**F-4 — One wave-1 registry finding remains open in the final rows; the other
was closed by the late repair wave.**
- F5 (S721, scope wider than its anchored evidence): **closed** at 23:57 by
  `ResFixS721`, which downgraded the tier to B and rewrote the scope to
  "the review's secondary literature-background definition of infant
  proto-conversation (citations to Hsu & Fogel 2003, Hsu et al. 2001, Kaye
  1977), not its own synthesis result" — now consistent with its anchor.
- F7 (S749, kind `community` vs the registry convention `docs`): **still
  open**. The row's kind cell is `community`, tier `C`, status `queued`; the
  registry convention (cf. S178 `docs | C`) is not matched. No repair seat
  has touched it. The wave-2 `UrlSafetyFinal` seat's host table covers the
  URL, not the kind cell.

**F-4b — The row checker does not enforce the `teaches ≤ 25 words` rule.**
`check-rows.py` verifies the anchor quote length (8–25 words) and the bullet
shape, but never measures the `teaches` cell length; `accept-c.py` ROWS does
not either. S723 (44 words) and S740 (45 words) therefore passed
`CHECK-ROWS: 32/32 clean` while breaking the stated row rule, and were caught
only by `RegFinalAudit`'s independent measurement and `CriticRowsFinal`'s
RF4/RF5. Both are now trimmed to 15 words. The gap in the checker itself
remains open.

**F-5 — The entry has not landed and its skeleton still carries the CE1
citation-shape defect.** `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
does not exist; `corpus/knowledge/linguistics/` still has 29 files and
`corpus/knowledge` 237. The wave-2 assembly proof
(`.ufo/waves/round-64/w2/B2ExecEntry.md`, run in a lane copy with synthetic
bullets) shows the assembled entry still trips the cited-lines checker:
`MULTI-ID corpus/knowledge/linguistics/language-socialization-and-acquisition.md:4 S718,S743`
— the skeleton's `- source: S718–S743 …` metadata range. That is the wave-1
CE1 defect, still open in the skeleton the assembler copies.

**F-6 — The S687 flip exists only as an unstaged worktree edit.** Confirmed by
`git diff -U0 corpus/SOURCES.md` (one hunk) and by the wave-2 `FrontierAudit`
seat, which measured the worktree cell as `queued` while the index and base
remain `mined`. The ACCEPT-C-64 APPEND leg reads the registry file, so it
currently reports `s687_queued=True`; it will fail again if the file is reset
to the index before the land.

**F-7 — A transient row-checker failure was observed during concurrent row
edits.** At 23:51 the checker reported 29/32 (S728 `bullet_shape`, S739
`quote_words=5 in_order=0`, S742 `bullet_shape`) while `FixRowsS728S742` and
`FixRowS739` were rewriting those files; the wave-2 `FixRowS735` and
`FixRowsS728S742` reports record the same 29/32 and 31/32 readings from their
own windows. By 23:52 the checker returned 32/32 and has stayed 32/32 through
23:56. The final-row numbers in §5 are taken from the 23:56 state.

**F-8 — No rev-1/rev-2 forcing receipt for claim O exists on disk.** The
counter docstring cites `bb0c74a486ae53ebc9a09787670020b69a03ef373df68f04fee8a30a827bf280`
as the rev-1/rev-2 counter sha, but `reports/round-64/telemetry/` contains no
rev-scoped receipt naming it (the four O receipts name rev3 only). This is the
wave-1 `ReviewerOReceipt` M3 defect, still open.

**F-8b — The claim-C land landed at 00:03 while this seat was writing, and
ACCEPT-C-64 now passes 10 of 11 legs on the working tree.** Measured at 00:19
by this seat against the landed working-tree bytes (entry
`corpus/knowledge/linguistics/language-socialization-and-acquisition.md`,
7,686 bytes, 81 lines, H1=1, H2=10, H3=0):
`FILE PASS`, `ROWS PASS checked=26`, `REJECTS PASS checked=6`,
`ONEID PASS … citations_exactly_once=True missing=[] duplicates=[]`,
`RESTATE PASS lines=26`, `HOSTS PASS`, `LINK PASS`,
`APPEND PASS missing_base_lines=0 s687_queued=True base=643 measured=675
+32=True`, `SWEEP PASS exit=0 topic_row=True`, `LIVE PASS subset=[S718,
S723, S728, S733, S738, S743] bad=[]` — and **`NOHARM FAIL diff=[]`**, so the
predicate prints `ACCEPT-C-64: FAIL`.
- **NOHARM is the only failing leg, and it fails for the expected reason**:
  it diffs *committed* refs (`git diff --name-only <base> <measured> -- corpus/knowledge`),
  and the claim-C lands are uncommitted working-tree changes. The leg will
  pass once the lands are committed.
- Counts re-measured after the land: registry rows **675** (643 → 675, the
  declared target), corpus knowledge entries **238** (237 → 238), linguistics
  partition **30** (29 → 30), `corpus/README.md` now carries
  `## linguistics/ (30)`, and the S687 status cell reads **`queued`**.
- **The entry's `- source:` line no longer carries the `S718–S743` range** —
  it now reads "the round-64 registry rows in `corpus/SOURCES.md` are the
  evidence anchors; each inserted claim stays within its cited row." The
  wave-1 CE1 `MULTI-ID` defect is therefore closed in the landed entry
  (F-5 is superseded).
- `reports/round-64/claims.json` was also edited (57 insertions, 10
  deletions — the statement and a reformatted leg list). Its sha is no
  longer `e970aace…`, so F-3 (the declaration calling S744–S749 all
  rejected) must be re-checked against the new text; this seat did not
  re-read the new statement body.

**F-9 — HIGH (found, reproduced, and then repaired mid-session): the rev4 O
counter's `m5` mutant replacement was syntactically invalid, so the MUT leg
FAILED and ACCEPT-O-64 could not pass. The repair landed at 00:08 and MUT now
PASSES — but no receipt binds the repaired bytes.**

Timeline, all measured by this seat against the lane bytes:

1. **Defect (counter sha `6d9c9354…`, rev4 label, mtime 23:54).** The rev4
   `m5` replacement (`accept-o.py:1054-1057`) was a hard-coded multi-line
   string whose `if`/`else` block was indented 12/16 spaces, while the needle
   site in `tools/reopen-row.py:604` sits at **8** spaces. The counter's own
   `tool_text.replace(needle, repl, 1)` therefore produced a **syntactically
   invalid** mutant.
   - Reproduced independently by this seat: mutant sha256
     `795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6`;
     `python3 -m py_compile` → `IndentationError: unexpected indent (line 605)`.
   - The counter's own MUT leg, run by this seat against those bytes
     (`--only MUT`, 255 s), printed
     `MUT FAIL bad=["m5:EDGE_SCHEMEREL isolation=['EDGE_SCHEMEREL FAIL rows=[] tgt_hits=0 src_hits=0 tb=False']"] mutants=10`
     then **`ACCEPT-O-64: FAIL`** — the invalid mutant made the tool exit 1 on
     every fixture, so it "killed" by crashing, not by the intended
     slashless-relative-path mutation.
   - The sibling seat `kotodama-r64.RevVerifyO2` reported the same defect and
     the same mutant hash independently; the receipt
     `reports/round-64/telemetry/m5-rev4.txt` (00:01) records the compile
     error and both legs failing.
2. **Repair landed at 00:08:52** (counter sha now
   `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7`): the
   replacement was re-indented to 8 spaces (body 12) and the docstring prose
   was corrected to "requires the former to PASS and the latter to FAIL"
   (matching the code at `accept-o.py:1115-1121`).
3. **This seat re-verified the repaired bytes**: the rebuilt m5 mutant
   (sha256 `f04dc0029ed89fc35abd36564907ab2e47c1b44ca0baed4b7528327b5de3e710`)
   compiles (`py_compile` OK), and the counter's own MUT leg against the
   repaired counter now prints **`MUT PASS bad=[] mutants=10`** and
   **`ACCEPT-O-64: PASS`** (255 s).
4. **Residual evidence-hygiene gaps that the repair did not close:**
   - `reports/round-64/telemetry/final-measures-o-rev4.txt` (00:08) records
     the **FAIL** run — it is honest falsification evidence, explicitly
     labelled "pre-data falsification evidence, NOT an acceptance receipt" —
     but it binds the *pre-repair* sha `6d9c9354…`. **No receipt binds the
     repaired counter sha `760ddd4d…`**, and the counter has moved twice since
     this seat's snapshot began (rev4 label, two distinct byte sets).
   - `reports/round-64/mutants/m5.py` on disk is still the **rev3** mutant
     (sha `83ecd734…`), i.e. the committed mutants/ directory does not hold
     the rev4 m5 either.
   - The MUT leg computes `pinned_fail` over **only the mutant's own pinned
     legs** (`accept-o.py:1092-1109`: `run_legs = pinned` except m5), so it
     cannot detect a mutant that also breaks other legs.

**F-10 — "each mutant fails exactly their pinned leg" is false for m1 and m2,
and the counter's MUT leg cannot see it.** The claim-O statement in
`reports/round-64/claims.json` says the ten mutants "each fail exactly their
pinned leg". The wave-2 receipt
`reports/round-64/telemetry/exactness-sweep-o.txt` (00:14) shows this is
false: rebuilt from the counter's own MUTANTS table,
- **m1** (pins `["EDGE_SCHEMEREL"]`) also fails `EDGE_USERINFO` and
  `EDGE_HTTPS`;
- **m2** (pins `["EDGE_USERINFO"]`) also fails `EDGE_MALTARG`.

This seat reproduced m1 independently: rebuilt m1 (sha256
`545205e312b752e4644067404407dca4bf3f6d5de69477c8130f9f260a02cd8a`, the same
hash the sweep receipt records) and run against all seven EDGE legs:
`EDGE_SCHEMEREL FAIL`, `EDGE_USERINFO FAIL`, `EDGE_HTTPS FAIL`,
`EDGE_MALTARG PASS`, `EDGE_SLASHLESS PASS`, `EDGE_308 PASS`,
`EDGE_5TH200 PASS` — three failures for a one-leg pin. Because the MUT leg
runs only each mutant's pinned legs, this over-failure is invisible to it.
This is the same class as the wave-1 `CriticO` O-PIN-01 finding, now shown to
hold for m1/m2 as well as m5. **[INFERENCE]** the claim's word "exactly" is
not established by the MUT leg; either the counter must run every mutant
against every leg, or the claim sentence must be weakened through the
authorized pre-data revision process. This seat edited neither.

---

## 4. Refreshed skeleton (full text)

````markdown
# Kotodama round 64 — lane report (refreshed at wave 2)

Status: **refreshed skeleton, wave-1 + wave-2 evidence.** Slots are filled
from committed lane bytes where possible, from named working-tree bytes where
the byte identity is stated inline, or marked `TBD-<what>` for post-commit
items only. No acceptance predicate is claimed as passing except the one run
this seat executed against named working-tree bytes (ACCEPT-CA-64) and the one
mechanical FAIL (ACCEPT-C-64, lands absent).

Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated,
branch `main`). Round base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`.
Declaration commit `097c21d` ("round-64: declaration + instruments (3 claims
C/O/Ca; attempt-1 counters adopted after re-verification, dry-run receipts at
base ff30a20; wave-1 spec 45 seats)").

Slot-filling rule used throughout: a slot is filled only when the bytes it
describes are **committed** in the lane repo at the named revision, when it is
a measurement re-runnable over committed bytes, or when it is a working-tree
byte whose sha256 is stated inline and named as working-tree. Working-tree
state is never presented as a landed result.

---

## Work performed

Declared claims (3), from `reports/round-64/claims.json` (committed at
`097c21d`, sha `e970aaceafa377230c91775f5b1b34e69aeb176faa52404715653d911a09bd3a`),
in the order the declaration lists them. **The three predicates are unchanged
by this refresh**; only the supporting evidence moved.

- **C — coverage (learning claim, sourced).** Language socialization and
  acquisition is unowned in `corpus/knowledge` → one new linguistics entry
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`,
  exactly 26 new registry rows `S718`–`S743` (mined) cited by it, and six
  disposition rows `S744`–`S749` curating the round-63 closure's routed
  defect 7. Predicate: **ACCEPT-C-64** — every leg of
  `reports/round-64/accept-c.py` prints PASS. Command:
  `python3 -B reports/round-64/accept-c.py --root .`. Declared legs: FILE,
  ROWS, REJECTS, ONEID, RESTATE, HOSTS, LINK, APPEND, NOHARM, SWEEP, LIVE.
  Declared lands: the entry, `corpus/SOURCES.md`, `corpus/README.md`.
  Exports `S718`–`S749`. *(Declaration drift: the committed text still calls
  S744–S749 "six rejected rows" and exports them as rejected; the final
  staged rows are 3 rejected + 3 queued — see Findings.)*
- **O — operability (capability, counter hardening).** The round-63
  row-re-opener counter could not score seven redirect-edge properties nor the
  drip class → `reports/round-64/accept-o.py` pins each as its own leg plus
  DRIP; the unchanged `tools/reopen-row.py` must pass all of them; ten
  byte-patched mutants must each fail exactly their pinned leg. Predicate:
  **ACCEPT-O-64** — every leg of `reports/round-64/accept-o.py` prints PASS.
  Command: `python3 -B reports/round-64/accept-o.py --root .`. Declared legs
  (23): TOOL, INDEP, GEN, ORDER, BOUND, EXIT, PRIV, DEFAULT, ERR, REDIRECT,
  MALFORMED, GZIP, TRUNC, TIMEOUT, EDGE_SCHEMEREL, EDGE_USERINFO, EDGE_HTTPS,
  EDGE_MALTARG, EDGE_SLASHLESS, EDGE_308, EDGE_5TH200, DRIP, MUT. Declared
  lands: `reports/round-64/accept-o.py` plus four telemetry receipts. Exports
  nothing.
- **Ca — calibration (calibration repair, bookkeeping).** The round-63
  closure's routed bookkeeping defects 1, 2, 3, 4, 8, 9, 10 are unresolved at
  the base → each repaired, and every leg of `reports/round-64/accept-ca.py`
  prints PASS. Predicate: **ACCEPT-CA-64** — every leg of
  `reports/round-64/accept-ca.py` prints PASS. Command:
  `python3 -B reports/round-64/accept-ca.py --root .`. Declared legs (7):
  CANONLOG, PTRS, HISTOGRAM, DISPO, REVNAMES, NITS, R63SEP. Declared lands:
  `LOG.md`, `corpus/LOG.md`, `SCORECARD.md`,
  `reports/round-63/telemetry/revisions.txt`, `reports/round-64/accept-ca.py`.
  Exports nothing.

Work items, one bullet each with an evidence pointer:

- Declaration + instruments committed at `097c21d`: `reports/round-64/claims.json`,
  `reports/round-64/accept-c.py` (revision 0), `reports/round-64/accept-ca.py`
  (revision 0), and the two base dry-run receipts
  `reports/round-64/telemetry/dry-run-c.txt` (ACCEPT-C-64 **FAIL**, `exit=1`)
  and `reports/round-64/telemetry/dry-run-ca.txt` (ACCEPT-CA-64 **FAIL**,
  `exit=1`).
- The three counters now carry receipt-forced **pre-data revisions**, all
  uncommitted working-tree bytes: `accept-c.py` rev1 (REJECTS accepts
  `queued`/`QUEUED-CANDIDATE:`), rev2 (RESTATE fails a clause copied verbatim
  from the row's `teaches` cell), rev3 (ONEID requires each of S718–S743
  cited exactly once) — sha `073e9716…`; `accept-ca.py` rev1 (CANONLOG counts
  round-bearing headings, PTRS scopes the dead-pointer scan to the round-63
  SCORECARD block, REVNAMES prints its leg), rev2 (NITS requires each
  value-context pair inside the Round-64 LOG entry) — sha `a8088092…`;
  `accept-o.py` rev1 (MUT matches the `<LEG> FAIL` prefix), rev2
  (`EDGE_USERINFO` pins the observed `attempts=6`), rev3 (MUT requires the
  observed failure-leg set to equal the pins), rev4 (m5 mutates slashless
  relative paths only and its paired `EDGE_SCHEMEREL,EDGE_SLASHLESS` run
  requires SCHEMEREL to PASS; unknown `--only` selectors exit 2) — sha
  `6d9c9354…`. Each revision names its forcing receipt in a code comment.
- Claim-C row contributions are staged as scratch artifacts under
  `.ufo/waves/round-64/rows/` (untracked working tree, **not committed**):
  26 mined-row directories `ScribeRowS718`–`ScribeRowS743` and 6
  disposition-row directories `ScribeRejS744`–`ScribeRejS749`. The row
  checker `.ufo/waves/round-64/check-rows.py` (untracked) reports
  **32/32 clean** (23:52, 23:54 and 23:56 readings; a 23:51 reading was
  29/32 during concurrent row writes — Findings).
- Entry skeleton staged at
  `.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md` (untracked): one
  H1, `- topic:` / `- source:` / `- verified-at:` / `- recheck:` lines, ten
  `##` sections, `<!-- BULLETS n -->` insertion points, a §9 worldbuilder
  choice table, and a §10 lore handoff. **The entry landed at 00:03** at
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
  (7,686 bytes, 81 lines, H1=1, H2=10, H3=0) and its `- source:` line no
  longer carries the `S718–S743` range, so the wave-1 CE1 `MULTI-ID` defect
  is closed in the landed entry. The land is uncommitted working-tree state.
- Claim-O counter `reports/round-64/accept-o.py` is **untracked** (revision 4
  label per its own docstring; sha `760ddd4d…` after the 00:08 m5 repair);
  its four declared telemetry receipts
  (`final-measures-o.txt`, `mut-o.txt`, `edge-o.txt`, `control-o.txt`) exist
  but bind to **rev3** counter bytes, `final-measures-o-rev4.txt` is the
  honest FAIL receipt for the pre-repair rev4 bytes, and
  `reports/round-64/mutants/` holds the ten mutant sources, of which `m5.py`
  is rev3 bytes. TBD-o-counter-landing-and-receipt-regeneration.
- Claim-Ca repairs exist only as **uncommitted working-tree** changes to
  `LOG.md`, `SCORECARD.md` and `corpus/LOG.md`, plus an untracked
  `reports/round-63/telemetry/revisions.txt`. TBD-ca-repair-landing.

## Landed changes

| commit | change | LOG entry |
|---|---|---|
| `097c21d` | round-64 declaration + instruments: `claims.json`, `accept-c.py` rev0, `accept-ca.py` rev0, base dry-run receipts `dry-run-c.txt` / `dry-run-ca.txt`, wave-1 spec + taskcall | TBD-log-entry-round-64 (the round-64 `LOG.md` entry is a working-tree change, not committed) |
| TBD-claim-c-land-commit | claim C land: new entry + 26 mined rows + 6 disposition rows + `corpus/README.md` index row and counts footer | TBD |
| TBD-claim-o-land-commit | claim O land: `reports/round-64/accept-o.py` + the four declared telemetry receipts + `reports/round-64/mutants/` | TBD |
| TBD-claim-ca-land-commit | claim Ca land: `LOG.md` round-64 entry, `SCORECARD.md` correction block, `corpus/LOG.md` pointer repair, `reports/round-63/telemetry/revisions.txt` | TBD |
| TBD-records-commit | records: `corpus/lessons/round-64.md` (Gate S718–S743, re-open evidence for S744–S749, mistakes), round-64 final measures, wave reports | TBD |

Note: the round-63 report's "Landed changes" table tied each commit to a LOG
entry; the round-64 table above keeps that shape, and every `TBD-` cell is a
commit that does not exist in the lane repo at the time of this refresh.

## Before → after measurements

One per claim. Each entry gives the counting command, the before value
measured over **committed** bytes, the measured commit, and the after value.

- **C (coverage):**
  - Counting command (registry rows):
    `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  - Before: **643** rows, measured at `ff30a205c8d23b35f1ac533740121a955a9fda96`.
  - After: **675** rows — the claim-C land landed at 00:03 (working tree,
    uncommitted). The APPEND leg of `reports/round-64/accept-c.py` declares the
    target `643 → 675` = exactly 32 appended rows (26 mined + 6 disposition),
    and the landed registry measures 675 with
    `s687_queued=True base=643 measured=675 +32=True`.
  - Supporting counts: before at `ff30a205` — corpus knowledge entries **237**,
    linguistics partition **29**, topic-line owners **0**, filename owners
    **0**. After the land (measured 00:19): corpus knowledge entries **238**,
    linguistics partition **30**, `corpus/README.md` carries
    `## linguistics/ (30)`, and the new entry exists at
    `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
    (7,686 bytes, 81 lines, H1=1, H2=10, H3=0). The S687 status cell reads
    `queued`.
  - Predicate status: `python3 -B reports/round-64/accept-c.py --root .` run
    this refresh against the landed working tree (counter sha `979050ce…`,
    rev3) prints **10 of 11 legs PASS** — FILE, ROWS, REJECTS, ONEID, RESTATE,
    HOSTS, LINK, APPEND, SWEEP, LIVE — and **`NOHARM FAIL diff=[]`**, hence
    `ACCEPT-C-64: FAIL`. NOHARM diffs *committed* refs, so it will pass once
    the lands are committed. The authoritative verdict remains the
    integrator's run over committed bytes:
    **TBD-claim-c-landing-and-commit**.
- **O (operability):**
  - Counting command:
    `python3 -B reports/round-64/accept-o.py --root .`
  - Before, measured at the round-63 records tip `80ff34c`:
    `git show 80ff34c:reports/round-63/accept-o.py | grep -cE 'leg\("(EDGE_|DRIP)'` → **0**,
    and `… | grep -o 'leg("[A-Z_0-9]*"' | sort -u | wc -l` → **15** legs total.
    The round-63 counter therefore scores none of the seven redirect-edge
    properties and not the drip class.
  - After: **TBD-claim-o-counter-landing-and-run** — the instrument now
    passes on its own bytes, but the receipt chain is not closed. Evidence on
    disk: `reports/round-64/telemetry/final-measures-o.txt` records a
    complete 23-leg run, all PASS, ending `MUT PASS bad=[] mutants=10
    kill_evidence=[…]`, `ACCEPT-O-64: PASS`, `exit=0`, at jj working copy
    `b7d22703dfb684713826a4064e614264867e8cd` — but it binds counter **rev3**
    sha `c27a9fef…`; `mut-o.txt`, `edge-o.txt` and `control-o.txt` name the
    same rev3 sha. The counter is now at rev4, sha
    `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7`.
    The rev4 receipt `reports/round-64/telemetry/final-measures-o-rev4.txt`
    (00:08) is honest **falsification** evidence — it records
    `RESULT: FAIL — 22/23 legs PASS, MUT FAIL` against the *pre-repair* rev4
    sha `6d9c9354…` and is explicitly labelled "NOT an acceptance receipt".
    **This seat's own MUT run against the repaired bytes** (`--only MUT`,
    255 s) prints `MUT PASS bad=[] mutants=10` and `ACCEPT-O-64: PASS`, but
    **no receipt on disk binds the repaired counter sha**. The mid-session
    defect, its repair and the reproduction trail are in Findings F-9.
    `reports/round-64/mutants/m5.py` is still the rev3 mutant.
  - Counter behaviours closed this refresh, verified by execution:
    `--only NOSUCHLEG` → `ACCEPT_O_INPUT_ERROR unknown --only leg(s): NOSUCHLEG`,
    exit **2** (wave-1 H1 fail-open closed);
    `--only EDGE_SCHEMEREL,EDGE_SLASHLESS` on the *unmutated* tool → both
    PASS, exit 0 (a two-leg slice, not a full run and not an MUT verdict);
    `--only MUT` → FAIL before the 00:08 repair, PASS after it.
  - **Scope caveat on the claim's "exactly their pinned leg" wording**: the
    MUT leg runs only each mutant's own pinned legs
    (`accept-o.py:1092-1109`), so it cannot detect over-failure. Measured
    directly: rebuilt **m1** (pins `["EDGE_SCHEMEREL"]`) also fails
    `EDGE_USERINFO` and `EDGE_HTTPS`, and rebuilt **m2** (pins
    `["EDGE_USERINFO"]`) also fails `EDGE_MALTARG` — see Findings F-10 and
    the receipt `reports/round-64/telemetry/exactness-sweep-o.txt` (00:14).
- **Ca (calibration):**
  - Counting command:
    `python3 -B reports/round-64/accept-ca.py --root .`
  - Before, measured at `ff30a205` and recorded in the committed receipt
    `reports/round-64/telemetry/dry-run-ca.txt`: **every leg FAIL, `exit=1`**
    (CANONLOG, PTRS, HISTOGRAM, DISPO, NITS, R63SEP all FAIL; the committed
    revision-0 counter prints 6 legs against the 7 legs
    `reports/round-64/claims.json` declares — see Findings).
  - After: run this refresh against the **working tree**, counter
    `reports/round-64/accept-ca.py` sha `a8088092…` (rev2):
    ```
    CANONLOG PASS r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56
    PTRS PASS score_dead=False stray_dead=False o_fixed=True c_fixed=True
    HISTOGRAM PASS tiers={'A': 13, 'B': 11} correction_present=True
    DISPO PASS items5_7=True s687_flip=True s693_kind=True
    REVNAMES PASS missing=[]
    NITS PASS seat_reports_nit=True duplicate_url_nit=True fail_legs_nit=True
    R63SEP PASS result_cited=True dep_class_named=True
    ACCEPT-CA-64: PASS
    exit=0
    ```
    These bytes (`LOG.md`, `SCORECARD.md`, `corpus/LOG.md`,
    `reports/round-63/telemetry/revisions.txt`, and the counter itself) are
    **uncommitted working-tree** state, so this is not yet a landed result.
    The authoritative verdict is the integrator's run against the committed
    bytes: **TBD-claim-ca-repair-landing-and-run**.

## Sources & frontier

- **SOURCES.md rows before → after:** before **643** → after **675** in the
  working tree (the claim-C land landed at 00:03; uncommitted).
  Counting command:
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  (re-measured at `ff30a205`: 643; re-measured after the land: 675).
- **Census command** (from the fleet root `/home/vgpnk/Projects/shokunin`,
  per `CORPUS.md` §Census):
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`
  — round-start receipt `reports/round-64/telemetry/census-start.txt`
  (untracked; exit 0, one `ok` line, the pre-existing W03 S687 warning and 27
  W04 duplicate-URL warnings) and a wave-1 re-run receipt
  `reports/round-64/telemetry/census-wave1.txt` (untracked; exit 0, no E-codes;
  still carries `kotodama W03 S687 mined but unused`).
  Round-end receipt: **TBD-round-end-census-receipt**.
- **Rows added by tier — recomputed from the FINAL staged rows** (32
  `row.txt` files under `.ufo/waves/round-64/rows/`, re-read 00:00; the
  wave-1 skeleton's draft figures are superseded where they differ, and the
  last repair wave rewrote five rows at 23:56–23:57):
  - 26 mined rows `S718`–`S743`: tier **A = 14**, tier **B = 12**;
    kinds paper **21**, book **4**, docs **1**; `status = mined` for all 26;
    `opened = 2026-10-23`, `recheck = 180d` for all 26; `used-by` =
    `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
    for all 26. The three A→B moves (`S721`, `S726`, `S737`) are the
    `ResFix*` repairs of `CriticRowsFinal` RF1/RF2/RF3 — secondary
    literature-background and ERIC-abstract-only evidence.
  - 6 disposition rows `S744`–`S749`: tier **A = 1** (`S745`), **B = 4**
    (`S744`, `S746`, `S747`, `S748`), **C = 1** (`S749`); kinds docs **4**,
    book **1** (`S748`), community **1** (`S749`); status **rejected = 3**
    (`S744`, `S745`, `S747`), **queued = 3** (`S746`, `S748`, `S749`); each
    carries a `REJECTED: … ; flip: …` or `QUEUED-CANDIDATE: … ; flip: …`
    teach cell with ordinary re-open evidence recorded in the row artifact
    (`TEST:` / `TEST2:` lines); `used-by` = `—` for all 6.
  - Combined over all 32 staged rows: tier **A = 15, B = 16, C = 1**; status
    **mined = 26, rejected = 3, queued = 3**; kind **paper = 21, book = 5,
    docs = 5, community = 1**.
  - Caveat: `check-rows.py` reports **32/32 clean** but does **not** measure
    the `teaches` cell length; `accept-c.py` ROWS does not either. S723
    (44 words) and S740 (45 words) therefore passed the checker while
    breaking the ≤25-word rule, and were caught only by `RegFinalAudit`'s
    independent measurement. Both are now trimmed to 15 words; the checker
    gap remains open.
  - Live-URL uniqueness (recomputed): **32 distinct** staged live URLs, and
    **0** of them already occurs in `corpus/SOURCES.md` — the row rule
    ("live URL unique in registry AND across staged rows") holds on the
    final staged set.
  - Registry-tier figures after landing: **TBD-claim-c-landing**.
- **Rows touched old→new:** **S687** `status: mined → queued` (the only
  in-place change the APPEND leg tolerates; base value re-measured at
  `ff30a205`: `S687` status = `mined`, `used-by` = `—`, and the same W03
  "mined but unused" census warning at the base). The flip exists today only
  as an **unstaged worktree edit** — `git diff -U0 corpus/SOURCES.md` is one
  hunk, `@@ -642 +642 @@`, changing only the status cell. Applied in the
  registry: **TBD-claim-c-landing**; the old→new change must also be logged in
  the round-64 lesson's Gate.
- **Frontier rows advanced:** six disposition rows `S744`–`S749` are the
  round-63 closure's rejected candidates re-opened as curated rows (routed
  defect 7); three retests still hold (`S744` 403-redirect to the Khanka
  headword, `S745` HTTP 403, `S747` HTTP 403) and three contradicted the
  prior ground (`S746` catalogue wording locatable, `S748` LacusCurtius
  Corona HTTP 200 + LOCATED, `S749` Wikipedia headgear HTTP 200 + LOCATED), so
  they are carried as `queued` candidates rather than false rejections. The
  `## Leads (unopened)` (38 bullets) and `## Search log` (5 paragraphs)
  blocks of `corpus/SOURCES.md` are **byte-identical to the base** (re-measured
  23:56 by md5 over lines 709–740) — round-64 additions:
  **TBD-round-64-search-log-and-leads**.
- **Sibling overlap / frontier area:** `.ufo/waves/round-64/w1/ConnectorOverlap.md`
  (untracked) records 21 sibling `PROVINCE.md` files read and names three
  intra-lane partial owners of adjacent slices (linguistic anthropology,
  sociolinguistics/registers, dialect-register consistency) that the new
  entry must point at one-way rather than restate. The wave-2 `OverlapRe`
  seat re-checked the final S729 row and confirms it stays inside kotodama
  (no sibling province owns caregiver-register participation); the entry
  skeleton §10 hands canon to lore-shokunin via
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`.

## Wave 1 — 32/32 seats, role mix, key verdicts

Wave-1 seat plan: `.ufo/waves/round-64/nw1-spec.json`, **32 seats**, all 32
report files present under `.ufo/waves/round-64/w1/` (the directory holds 55
`.md` files in total, including the earlier 45-seat `w1-spec.json` wave's
reports, e.g. `ScribeRowS718`–`ScribeRowS743`, `ScribeRejS744`–`ScribeRejS749`).

Role mix (nw1-spec, 32 seats): reviewer **13**, scribe **5**, executor **4**,
critic **4**, scout **2**, sentinel **2**, connector **1**, revenger **1**.

Key verdicts (each with its receipt pointer):

- **Row support ring, live blind re-opens** — `w1/ReviewSupportA.md`
  (S718–S727), `w1/ReviewSupportB.md` (S728–S736), `w1/ReviewSupportC.md`
  (S737–S743 + dispositions), `w1/ReviewSupportD.md` (8-row spread spot
  sample). Verdicts: SUPPORTED across the ring except **S719 NOT-SUPPORTED**
  (caveat omission: the anchor's "with the aforementioned caveats" was dropped
  from the bullet; §3 documents newborn maternal-ADS preference, weaker male
  preference, and 1-of-4 positive synthetic-pitch experiments).
- **Row-contract audit** — `w1/ReviewerRegistry.md`: F1 S723/S740 missing
  (both later landed by `ExecRowS723` / `ExecRowS740`); **F2 S729 same-work
  duplicate of S718** (different live URL, same paper — not caught by a
  URL-duplicate check); **F3 S739 anchor does not support the scoped claim and
  tier A inflated**; F4 S747 anchor carries fabricated meta-text as a "quote";
  F5 S721 scope wider than its quote; F6 topic-style scopes (observation);
  F7 S749 kind `community` vs registry convention `docs`.
- **Entry falsification** — `w1/CriticEntrySweep.md`: CE1 metadata range
  `S718–S743` violates the citation shape (`MULTI-ID`); CE2 attempted
  classroom scaffolding stated as successful scaffolding (S735); CE3 infant
  prosody preference loses age/stimulus exceptions (S719); CE4 staged values
  no longer match selected anchors; CE5 staged entry incomplete; CE6
  signed-language framing conflates modality with multilingualism.
- **Entry review** — `w1/ReviewerEntry.md`: F1 assembler/skeleton wording
  drift makes assembly fail deterministically; F2 `stage/bullets.json` stale
  and not an assembler input; F3 bullet-to-section placement tensions; F4
  S718/S729 same study; F5 calibration observation.
- **Counter attacks** — `w1/CriticClaims.md` (C: the teaches-copy escape
  prints `RESTATE PASS bad=[] lines=26`), `w1/ReviewerCounterC.md` (C:
  citation vacuity — an entry citing zero S-ids prints `ACCEPT-C-64: PASS`;
  the S687 APPEND exception tolerates any single-row rewrite; NOHARM diffs
  committed refs), `w1/CriticO.md` (O: rev3 checks killability, not exact
  kill-set isolation — the embedded m5 also fails EDGE_SCHEMEREL),
  `w1/ReviewerCounterO2.md` (O: `--only` contract broken — unknown selectors
  pass vacuously and core legs are silently absent), `w1/CriticCa.md`
  (Ca: a records-only append containing the bare token `W04` flips NITS
  FAIL → PASS), `w1/RevengerCounter.md` (O evidence chain broken; the cited
  rev-0 counter sha `bb0c74a4…` is unverifiable from the lane).
- **Evidence freshness** — `w1/ReviewerOReceipt.md`: the on-disk
  `final-measures-o.txt` was a stale 22-leg partial with no MUT line, no
  verdict line, no measured-revision header and no counter sha; the three
  other declared O lands did not exist; `tools/reopen-row.py` byte-identity
  PASS (`c0f10a84…`, identical to base and to the round-63 freeze record).
- **Executor receipts** — `w1/ExecCounterO.md`: a fresh full lane-root run
  printed all 23 legs PASS, `ACCEPT-O-64: PASS`, exit 0, and the four declared
  receipts plus `reports/round-64/mutants/` were written; the tool under test
  is byte-unchanged this round.
- **Counters, records, frontier** — `w1/ReviewerClaims.md`, `w1/ReviewerCa.md`,
  `w1/ReviewerSHONEN.md`, `w1/ReviewerSeparability.md`, `w1/ScribeClaimsJson.md`,
  `w1/ScribeCensus.md`, `w1/ScribeLesson.md`, `w1/ScribeReadmeFrontier.md`,
  `w1/ScribeGateQuotes.md`, `w1/ScribeEntrySkeleton.md`,
  `w1/ScribeRejS744.md`–`ScribeRejS749.md`, `w1/ScoutRegistry.md`,
  `w1/ScoutLessonRecon.md`, `w1/ConnectorOverlap.md`, `w1/SentinelAccess.md`,
  `w1/SentinelScope.md`, `w1/ExecIntegrate.md`, `w1/ExecRowS723.md`,
  `w1/ExecRowS740.md`, `w1/ReviewSupportA.md`–`ReviewSupportD.md`,
  `w1/CriticClaims.md`, `w1/CriticCa.md`, `w1/CriticO.md`,
  `w1/CriticEntrySweep.md`, `w1/ReviewerCounterC.md`, `w1/ReviewerCounterO2.md`,
  `w1/ReviewerOReceipt.md`, `w1/ReviewerRegistry.md`, `w1/ReviewerEntry.md`,
  `w1/RevengerCounter.md`, `w1/ExecCounterO.md`, `w1/ScribeReportFrag.md`.

## Wave 2 — in flight

Two wave-2 plans exist in the lane: the earlier 43-seat `w2-spec.json`
(scribe 13, reviewer 20, executor 3, mutation-tester 2, critic 1, sentinel 1,
connector 1, revenger 1) and the current 32-seat `nw2-spec.json`
(executor 8, reviewer 12, critic 6, scribe 3, scout 1, sentinel 1, connector 1).
The 32-seat plan is the FALSIFY+REPAIR wave; **26 of its 32 reports had
landed at 00:00** (FixRowS719, ReSourceS729, FixRowS739, FixRowS747,
FixRowS735, FixRowS722, FixRowsS728S742, RevCounters, CriticRevO,
CriticRevCa, CriticClaimsJson, CriticRowsFinal, CriticReceipts, RevVerifyO2,
RevVerifyCa, SupS719, SupS739, SupS735, RegFinalAudit, OReceiptFresh,
CaReceipts, SeparabilityRe, ReportFrag2, FrontierAudit, UrlSafetyFinal,
OverlapRe) with 6 outstanding (CriticRevC, RevVerifyC, SupS729,
CounterDrift, LessonFinal, GateFinal). The earlier 43-seat plan's reports are
also on disk. A further repair wave (`res/` — ResFixS721, ResFixS723,
ResFixS726, ResFixS737, ResFixS740) landed between 23:56 and 23:58 and
rewrote five rows.

Wave-2 posture observed in the landed reports: row repairs are byte-level and
evidence-backed (each fix re-opens the source and re-runs the pinned locator
`reports/round-61/reopen-quote.py`); counter revisions are pre-data and
receipt-forced (each names its wave-1 forcing control in a code comment); no
seat edited the lane git index, the jj state, the tool under test, or the
committed registry. One wave-2 seat (`B2ExecEntry`) proved entry assembly in a
**lane copy** with synthetic bullets (the original lane was not modified); one
(`B2ExecCaRepair`) proved the Ca repairs in a copy and reported the lane-base
gate as failing before the repair. Two wave-2 seats (`RevVerifyO2`,
`OReceiptFresh`) recorded the rev4 O counter as **not present** at their
snapshots and explicitly declined to relabel rev3 evidence as rev4 evidence;
`RevVerifyO2` subsequently reported the rev4 `m5` mutant compile defect
(Findings F-9), which this seat reproduced independently.

### Wave-2 counters at the final snapshot (00:01)

| counter | revision (docstring) | sha256 | note |
|---|---|---|---|
| `reports/round-64/accept-c.py` | 3 | `979050ce21fa01758c075745b08bf3ecf7d6e73baad543a1df83f666ecc5de2b` | rev1 REJECTS accepts `queued`; rev2 RESTATE rejects a `teaches`-copied clause; rev3 ONEID requires S718–S743 cited exactly once |
| `reports/round-64/accept-ca.py` | 2 | `d0787979ae4e318c4a7cde4385dd2b2e36890f8e258b3733cc1a6e980533f917` | rev1 CANONLOG/PTRS/REVNAMES fixes; rev2 NITS pinned to the Round-64 LOG entry (`correction_record`, `record_exact`) |
| `reports/round-64/accept-o.py` | 4 | `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7` | rev4 = m5 isolation + unknown-`--only` exit 2; **repaired at 00:08** (the earlier `6d9c9354…` bytes had an invalid m5 replacement and MUT FAILED — F-9). This seat's `--only MUT` run against the repaired bytes prints `MUT PASS bad=[] mutants=10` / `ACCEPT-O-64: PASS`. **No receipt binds this sha** |

`ACCEPT-CA-64` re-run by this seat against the final Ca bytes: **PASS**,
7/7 legs, exit 0 (`NITS PASS correction_record=True seat_reports_nit=True
duplicate_url_nit=True fail_legs_nit=True`). All three counters remain
**uncommitted working-tree** bytes.

### Defect → forcing receipt → repair seat → verification seat

| # | Defect (axis) | Forcing receipt | Repair seat | Verification seat / status |
|---|---|---|---|---|
| D-01 | S719 bullet drops the anchor's caveats — overclaim (coverage) | `w1/ReviewSupportA.md` (NOT-SUPPORTED) + `w1/CriticEntrySweep.md` CE3 | `FixRowS719` (bullet now carries the age/speaker/stimulus qualification) | `SupS719` — **outstanding** |
| D-02 | S735 states attempted scaffolding as successful (coverage/calibration) | `w1/CriticEntrySweep.md` CE2 | `FixRowS735` (bullet now reports the teacher's attempt) | `SupS735` — **outstanding** |
| D-03 | S728 bullet drops the secondary-account hedge (calibration) | `w1/ReviewerEntry.md` F4 | `FixRowsS728S742` (bullet now attributes to Schieffelin as relayed by Frye) | `RegFinalAudit` — **outstanding** |
| D-04 | S742 bullet drops the single-classroom limit (calibration) | `w1/ReviewerEntry.md` F5 | `FixRowsS728S742` (bullet now bounded to one second-grade classroom) | `RegFinalAudit` — **outstanding** |
| D-05 | S722 locator names the wrong section (coverage) | `w1/ReviewSupportA.md` (locator defect D2) | `FixRowS722` (locator → "New Directions and Next Steps, paragraph 35") | `RegFinalAudit` — **outstanding** |
| D-06 | S739 anchor does not support the scoped claim; tier A inflated (coverage/calibration) | `w1/ReviewerRegistry.md` F3 | `FixRowS739` (re-anchored to the paper's own Results sentence) | `SupS739` — **landed, SUPPORTED** |
| D-07 | S747 anchor presents fabricated meta-text as a quote (calibration) | `w1/ReviewerRegistry.md` F4 | `FixRowS747` (anchor now states the intended locator and the 403) | `RegFinalAudit` — **outstanding** |
| D-08 | S729 is a same-work duplicate of S718 (coverage) | `w1/ReviewerRegistry.md` F2 + `w1/ReviewerEntry.md` F4 | `ReSourceS729` — row re-sourced to Neer, Brahmbhatt, Walsh & Warlaumont 2025, PLOS ONE 20(6):e0326569 (row file mtime 23:54; the seat's own report has not landed) | `SupS729` — **outstanding** |
| D-09 | C: an entry clause copied verbatim from a row's `teaches` cell passes RESTATE (operability) | `w1/CriticClaims.md` | counter rev2 (`accept-c.py`, `teaches_copy` failure) | `RevVerifyC` / `CriticRevC` — **outstanding** |
| D-10 | C: an entry citing zero S-ids passes ACCEPT-C — citation vacuity (operability) | `w1/ReviewerCounterC.md` D1 | counter rev3 (`accept-c.py`, ONEID requires S718–S743 cited exactly once) | `RevVerifyC` / `CriticRevC` — **outstanding** |
| D-11 | Ca: records-only prose with bare tokens flips NITS FAIL → PASS (operability) | `w1/CriticCa.md` | counter rev2 (`accept-ca.py`, NITS requires each value-context pair in the Round-64 LOG entry) | `RevVerifyCa` — **landed, but against rev1 sha `f222648…`; the current counter is rev2 sha `a8088092…`**, so the verification is stale relative to the instrument |
| D-12 | O: m5 fails EDGE_SCHEMEREL in addition to its pinned EDGE_SLASHLESS (operability) | `w1/CriticO.md` O-PIN-01 + `w1/ReviewerCounterO2.md` | counter rev4 (`accept-o.py`, m5 paired run requires SCHEMEREL PASS) | `RevVerifyO2` / `CriticRevO` — **outstanding**; `CriticRevO` landed but recorded the rev4 bytes as **absent** at its snapshot |
| D-13 | O: `--only NOSUCHLEG` exits 0 fail-open (operability) | `w1/ReviewerCounterO2.md` H1 | counter rev4 (`accept-o.py`, unknown selector → exit 2) | **closed by this seat's execution**: `--only NOSUCHLEG` → `ACCEPT_O_INPUT_ERROR unknown --only leg(s): NOSUCHLEG`, exit 2 |
| D-14 | O: the rev-1/rev-2 forcing receipt `bb0c74a4…` is absent from disk (calibration) | `w1/ReviewerOReceipt.md` M3 + `w1/RevengerCounter.md` | none landed — no rev-scoped receipt exists under `reports/round-64/telemetry/` | `OReceiptFresh` / `CriticReceipts` — **outstanding** |
| D-15 | O: the on-disk final receipt was a stale 22-leg partial with no MUT/verdict/header (calibration) | `w1/ReviewerOReceipt.md` check 1 | `ExecCounterO` (w1) overwrote `final-measures-o.txt` with a complete headered 23-leg PASS receipt | `OReceiptFresh` — **outstanding**; the replacement binds rev3, and the counter is now rev4 |
| D-16 | O: three declared lands (`mut-o.txt`, `edge-o.txt`, `control-o.txt`) did not exist (operability) | `w1/ReviewerOReceipt.md` check 2 | `ExecCounterO` (w1) created all three | `OReceiptFresh` — **outstanding** (all three name rev3) |
| D-17 | Ca: the counter prints 6 legs against 7 declared (REVNAMES computed but never printed) (operability) | `reports/round-64/telemetry/dry-run-ca.txt` (committed) | counter rev1 (`accept-ca.py`, REVNAMES prints its leg) | `RevVerifyCa` — **landed** (7/7 PASS) |
| D-18 | Ca: CANONLOG counts `## Round` headings, which can never exceed 6 (operability) | `reports/round-64/telemetry/dry-run-ca.txt` (committed) | counter rev1 (`accept-ca.py`, counts `^## .*Round`) | `RevVerifyCa` — **landed** |
| D-19 | Ca: PTRS scans the whole SCORECARD for a dead pointer, hitting legitimate round-51–58 citations (operability) | `reports/round-64/telemetry/dry-run-ca.txt` (committed) | counter rev1 (`accept-ca.py`, scopes the scan to the round-63 block) | `RevVerifyCa` — **landed** |
| D-20 | C: rows S723 and S740 missing from the staged set (coverage) | `w1/ReviewerRegistry.md` F1 | `ExecRowS723`, `ExecRowS740` (w1) | `RegFinalAudit` — **outstanding**; `check-rows.py` reports 32/32 clean, so the rows themselves are present |
| D-21 | C: the entry skeleton's `- source: S718–S743 …` metadata range violates the citation shape (operability) | `w1/CriticEntrySweep.md` CE1 + `w1/ReviewerEntry.md` F1 | none landed — the skeleton still carries the range; `B2ExecEntry`'s copy-assembly proof reproduces `MULTI-ID …:4 S718,S743` | `RegFinalAudit` — **outstanding** |
| D-22 | C: the round-63 rejected candidates must be curatable as honest `queued` rows, not false rejections (calibration) | `w1/ReviewerClaims.md` + `w1/ScribeRejS744.md`–`ScribeRejS749.md` | counter rev1 (`accept-c.py`, REJECTS accepts `queued`/`QUEUED-CANDIDATE:`) + `B2RejS746`, `B2RejS748` | `CriticRowsFinal` — **outstanding** |
| D-23 | S687 must flip `mined → queued` as part of claim C (calibration) | `w1/RevengerFrontier.md` (W03 census warning) + `w1/ScribeCensus.md` | **unstaged worktree edit** in `corpus/SOURCES.md` (one hunk, `@@ -642 +642 @@`) | `RegFinalAudit` — **outstanding** |
| D-24 | S721 tier A presents a secondary literature-background definition as primary authority (calibration) | `w2/CriticRowsFinal.md` RF1 | `ResFixS721` (tier A → B; scope reworded to name the upstream citations) | `RegFinalAudit` — **outstanding** (tier now B at 23:57) |
| D-25 | S726 tier A on ERIC-abstract-only evidence for a substantive paradigm claim (calibration) | `w2/CriticRowsFinal.md` RF2 | `ResFixS726` (tier A → B) | `RegFinalAudit` — **outstanding** (tier now B at 23:56) |
| D-26 | S737 tier A on ERIC-abstract-only evidence for an operational definition (calibration) | `w2/CriticRowsFinal.md` RF3 | `ResFixS737` (tier A → B) | `RegFinalAudit` — **outstanding** (tier now B at 23:57) |
| D-27 | S723 `teaches` cell 44 words, over the ≤25-word row rule (operability) | `w2/CriticRowsFinal.md` RF4 + `w2/RegFinalAudit.md` finding 1 | `ResFixS723` (teaches trimmed to 15 words) | `RegFinalAudit` — **outstanding** (15 words at 23:56) |
| D-28 | S740 `teaches` cell 45 words, over the ≤25-word row rule (operability) | `w2/CriticRowsFinal.md` RF5 + `w2/RegFinalAudit.md` finding 2 | `ResFixS740` (teaches trimmed to 15 words, hedge kept; tier stays A) | `RegFinalAudit` — **outstanding** (15 words at 23:57) |
| D-29 | S747's anchor carries no verbatim quote after the repair; the row format expects 8–25 words (calibration) | `w2/RegFinalAudit.md` finding 3 | `FixRowS747` (honest "wording not locatable" 403 record) | `RegFinalAudit` — **flagged, unresolved by design**; `accept-c.py` REJECTS checks shape/status/prefix/flip only, so the claim is unaffected |
| D-30 | S742's `teaches` cell still states generality the anchor's single-classroom limit does not support (calibration) | `w2/RegFinalAudit.md` finding 4 | none landed | `RegFinalAudit` — **outstanding, informational** |
| D-31 | Reject rows S744–S749 carry no `VERIFY:`/`CAPTURE:`/`ACCESS:` trailer; their re-open evidence lives only in seat reports and the pending lesson Gate (calibration) | `w2/RegFinalAudit.md` finding 5 | none landed | `CriticRowsFinal` — **outstanding** |
| D-32 | **O rev4's `m5` mutant replacement was syntactically invalid (over-indented), so the MUT leg FAILED and ACCEPT-O-64 could not pass** (operability) | `w2/CriticRevO.md` O-R1 + `w2/RevVerifyO2.md` | **repaired at 00:08** by the counter owner (re-indented to 8 spaces; docstring prose corrected) — counter sha `6d9c9354…` → `760ddd4d…` | `RevVerifyO2` — **landed and reproduced by this seat**; this seat's own `--only MUT` against the repaired bytes prints `MUT PASS bad=[] mutants=10` / `ACCEPT-O-64: PASS`. **Open**: no receipt binds the repaired sha |
| D-33 | O rev4's docstring prose was inverted relative to its own code (the paired run "requires the former to FAIL and the latter to PASS" vs code requiring `EDGE_SCHEMEREL PASS`) (calibration) | `w2/RevVerifyO2.md` | **repaired at 00:08** — the docstring now reads "requires the former to PASS and the latter to FAIL", matching the code | `RevVerifyO2` — **landed** |
| D-34 | **"Each mutant fails exactly their pinned leg" is false for m1 and m2** — m1 (pins `["EDGE_SCHEMEREL"]`) also fails `EDGE_USERINFO` and `EDGE_HTTPS`; m2 (pins `["EDGE_USERINFO"]`) also fails `EDGE_MALTARG`; the MUT leg runs only each mutant's pinned legs and cannot see it (operability/calibration) | `w2/RevVerifyO2.md` + `reports/round-64/telemetry/exactness-sweep-o.txt` (00:14) | none landed | **measured independently by this seat** (rebuilt m1, sha `545205e3…`, seven EDGE legs: 3 FAIL for a 1-leg pin) — **outstanding** |

## Trend verdicts

One verdict each for `expansion`, `quality`, `discernment`, with evidence;
no scalar. Verdicts that depend on an unlanded predicate are marked as such
rather than guessed.

- **expansion: TBD-claim-c-commit — the landed bytes now support it, pending
  the commit.** Evidence: the new entry's filename-owner and topic-line-owner
  counts were **0 and 0** at `ff30a205` (re-confirmed by the wave-2
  `FrontierAudit` seat), and the entry now exists at
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`;
  the registry row count moved **643 → 675**; corpus entries **237 → 238**;
  the linguistics partition **29 → 30**. ACCEPT-C-64's FILE, ROWS, ONEID and
  SWEEP legs all PASS on the landed working tree, and the only failing leg is
  NOHARM, which diffs committed refs. The staged row set is a real 32-row
  addition on previously unowned ground with 32 distinct live URLs and no
  registry collision. If ACCEPT-C-64 passes on committed bytes, the verdict is
  **improved**; if any leg fails, the verdict is **unchanged** and the failing
  leg is named. No expansion verdict is asserted here.
- **quality: TBD-claim-c-and-o-acceptance-outcome.** Evidence that will
  settle it: ACCEPT-C-64 (RESTATE, HOSTS, LINK, APPEND, NOHARM, LIVE) and
  ACCEPT-O-64 (MUT in particular — the ten mutants each failing exactly their
  pinned leg is the quality-bearing part of the O claim). The counter's own
  MUT leg now PASSES on its repaired bytes (`MUT PASS bad=[] mutants=10`,
  measured by this seat), and the rev4 23-leg run recorded in
  `final-measures-o-rev4.txt` shows 22/23 legs PASS with MUT the only
  failure. **However**, the claim's "exactly" wording is not established:
  m1 and m2 also break legs they are not pinned to, and the MUT leg's
  `pinned_fail` computation only inspects each mutant's own pinned legs
  (F-10, D-34). Round-63's residual classes that this round targets —
  redirect-edge properties and the drip wall-budget-vs-socket-timeout
  distinction — are recorded verbatim in the `accept-o.py` docstring
  (revision 1–4 history). Quality is **improved** only if those legs pass on
  committed bytes *and* the "exactly" clause is either measured or corrected.
- **discernment: TBD-claim-ca-acceptance-outcome.** Evidence that will settle
  it: ACCEPT-CA-64's seven legs (CANONLOG, PTRS, HISTOGRAM, DISPO, REVNAMES,
  NITS, R63SEP) against the committed repair bytes, plus the six disposition
  rows' honest `queued`-vs-`rejected` split — a curation move is only
  improved discernment if three contradicted rejections are carried as
  queued candidates with a flip clause rather than re-labelled rejections.
  The counter-hardening history in the `accept-o.py` docstring (four pre-data
  revisions, each forced by a named receipt) and in the `accept-c.py` /
  `accept-ca.py` revision comments is evidence of receipt-forced revision,
  but the verdict itself waits on the committed run.

## SHONEN

One line per box of `SHONEN.md` (four boxes). `[x]` only with a named
non-author verifier; `[~]` with a resolvable evidence pointer; `[ ]` if
untouched.

- `[~]` **Box 1 — SKILL.md carries real decision tables, error patterns and an
  executable checklist, with sources registered in `corpus/SOURCES.md`.**
  Evidence pointer: `SKILL.md:20` (`## Decision table`), `SKILL.md:468`
  (`## Error patterns`), `SKILL.md:522` (`## Checklist (executable where a
  tool exists)`) — all three headings re-measured in the lane repo at
  `097c21d`; registry rows 643 at `ff30a205` (the box's own parenthetical
  figure "412 rows after round 56" is a superseded historical reading, kept
  as the dated record it is). No non-author verifier on record for round 64.
- `[~]` **Box 2 — at least one end-to-end domain task executed and logged in
  `LOG.md`.**
  Evidence pointer: `LOG.md` carries a `## Round 64 — 2026-10-23` heading
  (working tree, line ~4152, **not committed**), and the round's two dry-run
  receipts are committed at `097c21d`
  (`reports/round-64/telemetry/dry-run-c.txt`, `dry-run-ca.txt`, both
  `exit=1`). The working-tree `LOG.md` entry also supplies the three numeric
  corrections (47 seat reports, 27 duplicate-URL rows, 9 FAIL legs) that the
  Ca counter's NITS leg reads, and the counter's rev2 run against the working
  tree prints `NITS PASS`. TBD-ca-log-entry-landing for the committed
  evidence pointer.
- `[~]` **Box 3 — instructions executable by an agent without oral context.**
  Evidence pointer: `reports/round-64/claims.json` (committed at `097c21d`)
  carries, per claim, the exact command, the frozen predicate sentence and
  the leg list — the seats worked from committed paths and the landed commit
  only. No non-author verifier on record.
- `[~]` **Box 4 — no cross-domain bleed (`PROVINCE.md` still accurate).**
  Evidence pointer: `PROVINCE.md` (unchanged at `097c21d`) refuses canon and
  names the world-bible handoff; the entry skeleton §10 states the handoff
  and claims no canon decision; `.ufo/waves/round-64/w1/ConnectorOverlap.md`
  (untracked) records the 21-lane province scan with three contested-scope
  items routed, not absorbed; the wave-2 `OverlapRe` seat re-checked the final
  S729 row and confirms it stays inside kotodama. TBD-entry-landing for the
  committed one-way-citation evidence.

## Stale-lane line

- Stale-lane: respawn-per-round driver; no other mission of this lane is
  open.

## Tool installs

- Tool installs: **none.** No package was installed or upgraded by this seat.
  The pacman channel is paused host-wide for this round; nothing in this
  seat's task required a tool beyond the Python 3 standard library and
  `git`/`grep` already present. No `uv tool install`, no release binary, no
  `cargo`/`npm` install was performed. (`uv run --with pypdf==5.4.0` was used by
  the wave-2 `B2ReviewRowS728` seat, not by this seat; no new package was
  installed persistently.)

## Open items the integrator must resolve (drafted from committed evidence)

1. **No receipt binds the repaired rev4 O counter.** The counter's `m5`
   mutant was invalid until 00:08 (sha `6d9c9354…` → `MUT FAIL`,
   `ACCEPT-O-64: FAIL`); it was repaired to sha `760ddd4d…` and this seat's
   own `--only MUT` run against the repaired bytes now prints
   `MUT PASS bad=[] mutants=10` / `ACCEPT-O-64: PASS`. But
   `final-measures-o-rev4.txt` is the honest **FAIL** receipt for the
   pre-repair bytes, and no receipt exists for the repaired sha. A full
   23-leg run against `760ddd4d…` must still be captured, and
   `final-measures-o.txt` / `mut-o.txt` / `edge-o.txt` / `control-o.txt` must
   be regenerated against the repaired counter.
   `reports/round-64/mutants/m5.py` is still the rev3 mutant.
2. **No rev-1/rev-2 forcing receipt exists** for the O counter's early
   revisions; the docstring's `bb0c74a4…` is unverifiable from the lane.
3. **"Each mutant fails exactly their pinned leg" is not established.**
   Rebuilt m1 (pins `["EDGE_SCHEMEREL"]`) also fails `EDGE_USERINFO` and
   `EDGE_HTTPS`; rebuilt m2 (pins `["EDGE_USERINFO"]`) also fails
   `EDGE_MALTARG` — measured by this seat and recorded in
   `reports/round-64/telemetry/exactness-sweep-o.txt`. The MUT leg runs only
   each mutant's pinned legs, so it cannot see this. Either the counter must
   run every mutant against every leg, or the claim sentence must be
   weakened through the authorized pre-data revision process.
4. **The declaration's disposition wording was corrected at 00:03** by the
   L1's records patch (exports now read "S744-S749 (three rejected + three
   queued candidates)"), so this item is closed; the patch is still
   uncommitted working-tree state.
5. **The claim-C land is in the working tree but not committed**, so
   ACCEPT-C-64's NOHARM leg still fails (`NOHARM FAIL diff=[]`); the other
   ten legs pass. Committing the lands closes it. The entry's `- source:`
   line no longer carries the `S718–S743` range, so the wave-1 CE1
   `MULTI-ID` defect is closed in the landed entry.
6. **S687's `mined → queued` flip is now in the landed registry** (the
   working tree measures 675 rows with the S687 status cell reading
   `queued`), but it is still uncommitted.
7. **S749's kind cell is still `community`** where the registry convention is
   `docs` — the only unrepaired wave-1 registry finding (S721's scope defect
   was closed by `ResFixS721`).
8. **Acceptance evidence is missing for the newest counter revisions**:
   `RevVerifyC` (C rev3), `CriticRevC`, `CounterDrift` and a re-run of
   `RegFinalAudit` against the post-repair rows are outstanding;
   `RevVerifyCa` verified Ca rev1, not the current rev2.
9. **The row checker does not enforce `teaches ≤ 25 words`** — S723 and S740
   passed `32/32 clean` while at 44 and 45 words. The rule now holds in the
   staged rows, but the gap in `check-rows.py` and `accept-c.py` ROWS
   remains.
10. **S747's anchor carries no verbatim quote** (honest 403 record). The
    claim is unaffected, but the row format expects an 8–25-word quote; this
    needs an explicit L1 acceptance or a recorded decision to keep the 403
    record as the anchor.
11. **Reject rows S744–S749 carry no verification trailer**; their re-open
    evidence lives only in seat reports and the pending lesson Gate.
````

---

## 5. Sources & frontier numbers known so far

Recomputed from the **final** staged rows at 00:00 (superseding the wave-1
skeleton's draft figures; note the last repair wave rewrote five rows at
23:56–23:57, so the mined tier split moved from A 17 / B 9 to **A 14 / B 12**):

| slice | n | tier | kind | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|
| mined S718–S743 | 26 | **A 14, B 12** | paper 21, book 4, docs 1 | mined 26 | 2026-10-23 (26) | 180d (26) | entry path (26) |
| disposition S744–S749 | 6 | A 1, B 4, C 1 | docs 4, book 1, community 1 | rejected 3, queued 3 | 2026-10-23 (6) | 180d (6) | `—` (6) |
| **all 32 staged** | 32 | **A 15, B 16, C 1** | **paper 21, book 5, docs 5, community 1** | **mined 26, rejected 3, queued 3** | — | — | — |

The tier movement is fully accounted for by the late repair wave:
`S721`, `S726` and `S737` were downgraded A → B by `ResFixS721`, `ResFixS726`
and `ResFixS737` (acting on `CriticRowsFinal` RF1/RF2/RF3 — secondary
literature-background definition, ERIC-abstract-only evidence — with the scope
cells reworded to say so: S721's scope now reads "the review's secondary
literature-background definition of infant proto-conversation (citations to
Hsu & Fogel 2003, Hsu et al. 2001, Kaye 1977), not its own synthesis
result"); `S723` and `S740` had their `teaches` cells trimmed from 44 and 45
words to 15 (RF4/RF5, the ≤25-word rule). `S740` correctly keeps tier A.

- Base registry rows: **643**; after the 00:03 claim-C land the working tree
  measures **675** (the declared target). Staged live URLs: **32 distinct**,
  **0** already in `corpus/SOURCES.md`.
- Corpus knowledge entries **238** after the land (237 at base), linguistics
  partition **30** (29 at base), `corpus/README.md` carries
  `## linguistics/ (30)`, and the new entry exists at
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`.
  All of it is **uncommitted working-tree** state.
- `## Leads (unopened)` 38 bullets and `## Search log` 5 paragraphs —
  byte-identical to base.
- Census receipts: `census-start.txt` (exit 0, one `ok` line, W03 S687
  warning + 27 W04 duplicate-URL warnings) and `census-wave1.txt` (exit 0, no
  E-codes; still carries the W03 S687 line). No round-end census receipt.
- `check-rows.py` at 00:00: **32/32 clean** — but note it does **not** check
  `teaches` length, which is why the 44/45-word cells in S723/S740 passed it
  until `RegFinalAudit` measured them independently.

## 6. Out of scope for this seat

- Editing any product file (rows, counters, registry, entry, README, LOG,
  SCORECARD, receipts). This seat wrote only this report.
- Committing, pushing, publishing, deploying, or mutating the lane git index
  or jj state.
- Dispatching subagents (lane-bound leaf).
- Installing or upgrading tools: none were needed; the pacman channel is
  paused host-wide and was not touched.

## 7. Dependencies recorded, not awaited

- The **claim-C land landed at 00:03** (entry, 32 registry rows, README
  index row, S687 flip, and an L1 records patch to `claims.json`) while this
  seat was writing. The land is **uncommitted working-tree** state, so
  ACCEPT-C-64's NOHARM leg still fails and no receipt binds it.
- The `res/` repair wave (`ResFixS721`, `ResFixS723`, `ResFixS726`,
  `ResFixS737`, `ResFixS740`) landed at 23:56–23:58 and moved five rows; the
  histograms in §5 are recomputed from the post-repair state.
- The **O counter was repaired mid-session (00:08)** in response to the m5
  compile defect this seat and `RevVerifyO2` both reported; **no receipt
  binds the repaired bytes**, and a full 23-leg run against sha
  `760ddd4d…` is still owed.
- Still outstanding at the final snapshot: `RevVerifyC`, `CriticRevC`,
  `SupS729`, `CounterDrift`, `LessonFinal`, `GateFinal` (the last six
  `nw2-spec` seats without a report), plus a re-run of `RegFinalAudit`
  against the post-repair rows and a `RevVerifyCa` re-run against Ca rev2.
- The integrator's authoritative run over the committed bytes.

## 8. Artifact paths

- This report: `.ufo/waves/round-64/w2/ReportFrag2.md`
- Refreshed skeleton (embedded in §4 above); wave-1 base skeleton:
  `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeReportFrag/report-skeleton.md`
- Staged rows: `.ufo/waves/round-64/rows/ScribeRowS718`–`ScribeRowS743`,
  `.ufo/waves/round-64/rows/ScribeRejS744`–`ScribeRejS749`
- Row checker: `.ufo/waves/round-64/check-rows.py`
- Counters at the final snapshot (00:16): `reports/round-64/accept-c.py`
  (rev3, sha `979050ce…`), `reports/round-64/accept-ca.py` (rev2, sha
  `d0787979…`), `reports/round-64/accept-o.py` (rev4 label, repaired sha
  `760ddd4d…`) — all three **uncommitted working-tree** bytes, and all three
  moved at least twice during this seat's window.
- O receipts: `reports/round-64/telemetry/final-measures-o.txt`,
  `mut-o.txt`, `edge-o.txt`, `control-o.txt` (all rev3-bound);
  `final-measures-o-rev4.txt` (honest FAIL, pre-repair sha);
  `m5-rev4.txt` (the compile-error evidence);
  `exactness-sweep-o.txt` (the m1/m2 over-failure sweep);
  mutants `reports/round-64/mutants/` (m5.py still rev3 bytes).
- Wave-1 reports: `.ufo/waves/round-64/w1/*.md` (55 files; the 32-seat
  `nw1-spec.json` wave is fully covered)
- Wave-2 reports: `.ufo/waves/round-64/w2/*.md` (26 of the 32 `nw2-spec.json`
  seats had landed at 00:00) and the `res/` repair reports.

Report: `.ufo/waves/round-64/w2/ReportFrag2.md`
