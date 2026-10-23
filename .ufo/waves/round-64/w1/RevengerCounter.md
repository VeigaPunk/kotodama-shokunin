# RevengerCounter — round-64 counter reconstruction (accept-c / accept-o / accept-ca)

Method: full source read of the three counters in the **working copy** (tags `#6A43`, `#A047`, `#4B34`),
`git diff HEAD` on each, `git ls-tree HEAD`, receipt files in `reports/round-64/telemetry/`,
provenance seats in `.ufo/waves/round-{63,64}/`, base-tree token census via `git show ff30a205:…`.
No edits made. jj state: working-copy commit `b7d22703` on top of `main`/`097c21d`.

## 0. Commit-vs-working-copy provenance defect (name it first)

`git ls-tree HEAD reports/round-64/` (commit `097c21d`, the declaration "instruments" commit) contains
**accept-c.py rev0, accept-ca.py rev0, claims.json, and only the two dry-run receipts**. It does **not**
contain `accept-o.py` at all. The working copy (uncommitted jj change) holds:

- `accept-c.py` **rev1** (REJECTS widened to disposition rows) — uncommitted `M`.
- `accept-ca.py` **rev1** (CANONLOG proof fix, PTRS r63-block scoping, REVNAMES leg printed) — uncommitted `M`.
- `accept-o.py` **rev3** — untracked `??`.
- `final-measures-o.txt`, `dry-run-o.txt`, `dry-run-o-baseline-copy.txt` — untracked `??`.

Consequences: a verifier replaying `git show HEAD:` gets (a) **no O counter** — ACCEPT-O-64 cannot even
be invoked from committed bytes; (b) committed accept-ca rev0, whose CANONLOG is
`proof = canon[:r64_idx].count("## Round"); … proof > 60` — LOG.md headings are `## <date> — Round N`,
so the count is 0 at every index → **rev0 CANONLOG is unpassable**; (c) committed accept-c rev0, whose
REJECTS requires all six rows `rejected` → fails the honest S748/S749 `queued` dispositions that rev1
exists to admit. This is the already-named R64-M1 class (nw1 spec, ScribeLesson item): wave dispatch and
bookkeeping repairs were staged **before** the counter revisions and O receipts were committed.

## 1. Provenance chain

### accept-c.py (working copy; header says "revision 0" — stale, see DOC-C1)

- **Body imported** from `reports/round-63/accept-c.py` rev4 (diff r63→r64: 133 changed lines: NEW_IDS
  694-717→718-743, REJ_IDS added, +24→+32, S687 tolerance, REJECTS leg, docstring).
- r64 **rev0** committed at `097c21d`: REJECTS strict (`cs[7] != "rejected"`, `REJECTED:` only).
- r64 **rev1** (uncommitted): REJECTS admits `status ∈ {rejected, queued}` and `QUEUED-CANDIDATE:` prefix.
  Forcing evidence named in the comment: S744/S745/S747 retest still 403; **S748 and S749 re-tests
  returned 200 + LOCATED** — the surviving `w1/ScribeRejS748.md:6,21,27` and `w1/ScribeRejS749.md:7,15,18`
  reports record exactly that (`200 https://penelope.uchicago.edu/…Corona.html`, `LOCATED`;
  `200 https://en.wikipedia.org/wiki/List_of_headgear`, `LOCATED`). Receipt-forced by seat retest
  reports, not by a counter dry-run; pre-acceptance-data but mid-wave. No seat report names the rev1
  author — attempt-1 reports (ExecCaRepair, RevCounterC-r64 if any) do not survive in `.ufo/waves/round-64/`.
- The inherited r63 revision comments are genuine r63 history, not r64 events: rev3 = r63 `RevCounterC` H2
  (locator byte-pin — `.ufo/waves/round-63/w1/RevCounterC.md` "HIGH — LIVE executes an unpinned locator"),
  rev4 = r63 retry budget (receipt `reports/round-63/telemetry/row-verify.txt:16-18` S706 NOT_LOCATED×3;
  S706 is in the r63 LIVE subset `(706-693)%4==1` — consistent).
- Inherited r63 provenance of the machinery per `w2/B2ExecCaRepair.md:68` instruments log: rev2+3
  (CtlCLineScam: NOMARK/anti-dump/HOSTS; CtlCUrlReuse: `norm_url` capture↔live comparison + `\d{14}id_`
  capture regex — verified in code: `CAPTURE_RE` uses `(\d{14})id_`, not the r63-vulnerable `[a-z]+`;
  exactly-11 cells). Note: B2ExecCaRepair says "normalized-URL LINK" — **over-statement**: r63 LINK and
  r64 LINK are both literal `url in line` substring counts; `norm_url` is used only for the
  capture-original↔live match (verified, r63 accept-c.py:302-311 vs r64:332-340).

### accept-o.py (working copy only; header "revision 3" — consistent with docstring history)

- New r64 file extending the r63 accept-o class battery (r63 file 766 lines; r64 1116; ~1236 diff lines).
  Legs EDGE_*/DRIP implement the seven properties measured unpinned in
  `.ufo/waves/round-63/w1/CtlORedirectEdge.md` §3-4 (receipt names M1-scheme-relative, M2-userinfo,
  M3-https, M4-malformed-target, M6-308, M7-fifth-response, M9/M10 — matches EDGE_SCHEMEREL/USERINFO/HTTPS/
  MALTARG/SLASHLESS/308/5TH200) plus DRIP from `reports/round-63/telemetry/rev-hold-lift.md` MEDIUM-1
  (`:73-78`: "--timeout 1 against a 45 s drip row took 135.1 s" — the wall-vs-socket distinction).
- rev0→rev3 all produced during attempt-1 by the `ExecOCounter` seat (`gen-w1.py:211-219` assigns the
  seat sole ownership of accept-o.py + telemetry; **no attempt-1 report survives** — not in w1/, w2/).
- rev1 (matcher bug): docstring cites rev-0 run where every mutant printed `LEG FAIL …` but the check
  compared full line == "LEG FAIL" → all `pinned_fail` false. Mechanically consistent with current
  `startswith(p + " FAIL")` code. Forcing receipt cited as `final-measures-o.txt` counter-sha `bb0c74a4…`:
  **unverifiable** — the on-disk receipt is truncated (21 leg lines, ends after DRIP, no MUT section,
  no ACCEPT-O-64 verdict, no measured-revision/sha header), so the cited sha and the observed mutant
  lines exist nowhere on disk. Receipt defect, not a code defect.
- rev2 (attempts=6): consistent — preserved receipt lines show `same_auth=[('S2797','UNREACHABLE',6)]` and
  `[('S2263','UNREACHABLE',6)]`; code asserts 6; one stale comment says 3 (DOC-O2).
- rev3 (kill-set pinning): "the requested mutant receipt" — requester unnamed; `mut-o.txt`/`edge-o.txt`/
  `control-o.txt` do not exist on disk though `claims.json:38-41` lands them. Partially receipt-forced.
- dry-run-o.txt (7 lines) and dry-run-o-baseline-copy.txt are also truncated attempts-era receipts.

### accept-ca.py (committed rev0; uncommitted rev1)

- New r64 file. rev1 (uncommitted) has three parts, each receipt-forced by `telemetry/dry-run-ca.txt`
  (rev-0 run): 6 printed legs against 7 declared → REVNAMES leg added; `prior_rounds=0` → unpassable
  `proof > 60` replaced by `^## .*Round` count > 50; `score_dead=True` → PTRS scoped to the
  `## Axes — round 63` block (rev0 flagged legitimately cited rounds 51-58 final-measures.txt — false
  positive). Author: attempt-1 `ExecCaRepair` seat (`gen-w1.py:195` instructs exactly this repair).
  Attempt-2 `w2/B2ExecCaRepair.md:5` confirms: "`REVNAMES` leg already existed" when it ran.

## 2. Hidden fixture data & pin honesty

| Pin | Value | Honest to base `ff30a205`? |
|---|---|---|
| `BASE` (all 3) | `ff30a205c8d2…` | Yes — matches `claims.json:4`. |
| `tools/reopen-row.py` | sha256 `c0f10a84…` working tree == `ff30a205:` blob | **Bytes identical, but NOT pinned by any leg** — see RELAX-O2. |
| MUT needles (10) | each occurs exactly once in the tool | Verified: `grep -c` = 1 for all tested needles. |
| `LOCATOR_SHA256` | `None` → resolved at runtime to sha256(`git show BASE:reports/round-61/reopen-quote.py`) | Mechanism honest, **comment stale**: "frozen pin … at round base 65b393e" — 65b393e is the round-63 base. Not a wrong pin; a wrong provenance comment. |
| `tools/check-cited-lines.py`, `reports/round-28/readme/sweep.py` | none | **Unpinned, executed from working tree** — FIXTURE-C1. |
| NOHARM ref | literal `main` | `main` = `097c21d` today (tip receipt fine, mid-history measurement wrong) — FIXTURE-C2. |
| Frozen expectations | opened `2026-10-23`, `180d`, ids S718-S749, `LOCATED/REFUSED/UNREACHABLE` verdicts, attempts counts, `A=13 B=11`, revision tokens `8d2041fa/38ec1316/0c892ce/80ff34c` | Literal constants matching the claim; honest except where RELAX-* notes unbound scope. |

## 3. Leg-by-leg drift table — accept-c.py (11 legs vs claims.json:11 — all present)

| Leg | Claim clause it scores | Verdict |
|---|---|---|
| FILE | "one new linguistics entry … .md" | Meets existence; shape limits (250 lines/1 H1/0 H3/≤16 H2/topic) are extra-claim, harmless. |
| ROWS | "26 registry rows S718-S743 opened this round and cited by it" | Mostly meets (id set, tier, mined, opened, recheck, quote 8-25 w, live+same-page-capture **syntax**). "cited by it" only via self-labeled `usedby` substring — RELAX-C3. Docstring says `>= 11` cells, code `!= 11` (stricter — DOC-C2). |
| REJECTS | "six rejected rows S744-S749 curating defect 7" | RELAX-C1 (rev1 admits `queued`) + RELAX-C2 (no URL, no lesson-Gate check despite own docstring). |
| ONEID | one S-id per entry line | Meets, plus inherited NOMARK + cited-lines lint — but lint tool unpinned (FIXTURE-C1). Same S-id may appear on many lines (claim's "one S-id per line" is per-line, fine). |
| RESTATE | "faithful restatement" is **review_only** in claims.json | Meets its lexical spec; known 3-ordered-words coincidence floor disclosed since r63. |
| HOSTS | — (anti-fixture hygiene) | Blocklist only; checks only 26 mined rows, not 6 REJ rows' URLs. |
| LINK | "26 registry rows …" uniqueness | Literal-substring uniqueness; normalized-duplicate URLs evade (RELAX-C4). |
| APPEND | "643 -> 675 rows (S687 flips mined -> queued)" | Count exact; S687 tolerance is whole-row, not status-cell (RELAX-C6). |
| NOHARM | "0 other owners" | Scope `corpus/knowledge` only; literal `main` ref; committed-vs-worktree surface mismatch (FIXTURE-C2). |
| SWEEP | "corpus 237 -> 238, linguistics 29 -> 30" | Indirect via sweep.py rows==files + README topic substring; counts not pinned (RELAX-C7); sweep tool unpinned (FIXTURE-C1). |
| LIVE | row live+capture evidence | 6/26 rows fetched; capture bytes never fetched for any row (RELAX-C5); locator byte-pinned correctly. |

## 4. Leg-by-leg drift table — accept-o.py (23 legs vs claims.json:23 — all present)

| Leg | Property pinned | Verdict |
|---|---|---|
| TOOL | tool exists, executable | Meets (X_OK unused — invoked via `sys.executable`). |
| INDEP | no counter coupling | Literal substring grep for 6 tokens — trivially evadable but the fixtures are the real test; also greps only **pre-mutation** tool text. |
| GEN | 61-row battery, verdicts/attempts/urls/summary | Meets; frozen CLASSES table. |
| ORDER | arg order + repeats | Meets. |
| BOUND | per-path hit counts | Meets. |
| EXIT | GEN=1, body=0, default-registry=0 | Meets. |
| PRIV | no --allow-private → REFUSED 0 | Meets. |
| DEFAULT | 9 attempts, 3×3 bursts @~60 s | Meets (receipt: wall 150 s, gaps 60/60). |
| ERR | 7 input-error cases exit 2 | Meets. |
| REDIRECT | cross-authority refused ± flag | Meets. |
| MALFORMED | 3 malformed listed URLs | Meets. |
| GZIP | gzip body/caption | Meets. |
| TRUNC | 4 MiB cap | Meets. |
| TIMEOUT | stall → wall budget honored | Meets (wall<20, 3 reqs, span≥3.0). |
| EDGE_SCHEMEREL | `//host` target refused | Meets (REFUSED 1, target 0 hits). |
| EDGE_USERINFO | userinfo target refused; same-authority attempted | Meets; pins observed `UNREACHABLE 6` (pin-to-observed — RELAX-O3). |
| EDGE_HTTPS | https target refused; same-authority attempted | Meets; same pattern; stale `attempts=3` comment (DOC-O2). |
| EDGE_MALTARG | unparseable port target → UNREACHABLE 1, no crash | Meets. |
| EDGE_SLASHLESS | `Location: sub/x` resolves vs directory | Meets (dir target hit once, `/sub/x` zero). |
| EDGE_308 | 308 followed like 307 | Meets. |
| EDGE_5TH200 | 5th response 200 honored, final url reported | Meets. |
| DRIP | wall budget vs per-socket timeout | Meets (UNREACHABLE 3, 3 reqs span≥7.0, paired fast control); docstring `wall∈[8,60]` vs code `wall<20` (DOC-O1). |
| MUT | 10 mutants each fail their pinned leg | "Exactly" **not** verified — mutants run under `--only pinned`; every other leg prints SKIP (RELAX-O1). |

## 5. Leg-by-leg drift table — accept-ca.py (7 legs vs claims.json:7 — all present post-rev1)

| Leg | Defect | Verdict |
|---|---|---|
| CANONLOG | 1 | Meets (r64 heading + `corpus/LOG.md` within 800 chars + stray has r63 + >50 prior round headings). Rev1 comment "`## Round` count can never exceed 6" is muddled (real rev0 bug: count always 0 vs `> 60`) — DOC-CA2. |
| PTRS | 2 | Scoped to r63 block + stray; dead pointer elsewhere in SCORECARD unexamined (RELAX-CA6, documented scope). |
| HISTOGRAM | 3 | Recompute honest (reads `BASE:SOURCES.md`, S694-S717 → A13/B11); correction marker is whole-file substring incl. bare "13 / 11" (RELAX-CA5). |
| DISPO | 4 | Tokens unbound to r64 region; `s693_kind` TRUE at base — half the leg vacuous (RELAX-CA3). |
| REVNAMES | 8 | Unordered 8-token membership; sha→receipt association unchecked (RELAX-CA2). |
| NITS | 9 | Checks 2 of 3 nits; conjunct 1 (`45`∧`47`) vacuous at base (36×"45", 43×"47" in base LOG.md); executed false-PASS by `w1/CriticCa.md` (W04+27 append flips it without correction) (RELAX-CA1). |
| R63SEP | 10 | Global substring tokens: "REC" (3-char), "record dependency", "SEPARABILITY: 2 findings", "exit=1" (RELAX-CA4). |

## 6. Named relaxations (pass condition weaker than the predicate sentence)

1. **RELAX-O1 — MUT "exactly" unverified.** Claim O: "ten byte-patched mutants each fail **exactly** their pinned leg." Counter runs each mutant with `--only <pinned>`; all other legs `SKIP`. A mutant that also breaks GEN/ERR/etc. still passes MUT. (m8 is even pinned to two legs, GEN+BOUND, making the singular loose.) Docstring's own wording ("fail its pinned leg") is the weaker reading the code implements.
2. **RELAX-O2 — "unchanged tools/reopen-row.py" unverified by the counter.** No byte/sha pin of the tool under test (contrast the LIVE locator pin in accept-c). Only INDEP's 6-token grep + MUT needle count==1 on mutation-relevant regions. Bytes are identical today (sha c0f10a84 == `ff30a205:` blob — verified), but the clause requires outside evidence (the nw1 ExecCounterO sha-compare item), exactly the hole class RevCounterC H2 forced closed for the locator.
3. **RELAX-O3 — EDGE_USERINFO/HTTPS pin observed verdict, not the semantic property.** Same-authority controls assert `UNREACHABLE 6` (tool can't resolve userinfo/TLS-on-HTTP) — correct for this tool, but the leg cannot distinguish "cross-authority check applied" from "urllib failed first" beyond `tgt_hits==0` on the cross case.
4. **RELAX-C1 — REJECTS status widened.** rev1 admits `queued`/`QUEUED-CANDIDATE:`; `claims.json:11` still says "six rejected rows" — evidence-honest (S748/S749 LOCATED) but the claim sentence is stale. Receipt-forced by ScribeRej retest reports.
5. **RELAX-C2 — REJECTS drops two of its own docstring's requirements.** No live-URL check on the 6 rows; no lesson-Gate evidence check. Only cell-count/status/teaches-prefix+`; flip:`.
6. **RELAX-C3 — "cited by it" unenforced.** Nothing requires the entry to cite any of S718-S743; `usedby` is self-labeling, RESTATE iterates only lines that happen to cite. Entry with zero citations passes ROWS+RESTATE.
7. **RELAX-C4 — LINK is literal-substring.** `url in line` count; `www.`/case/trailing-slash/query-normalized duplicates score hits=1. (B2ExecCaRepair's "normalized-URL LINK" claim about r63 provenance was an over-statement.)
8. **RELAX-C5 — LIVE fetches 6/26 rows; captures never fetched anywhere.** 20 rows' live reachability and all 32 rows' archive-capture existence/quote presence is syntax-only (r63 RevCounterC HIGH carries over; the `fakeid_` syntax hole is closed by `\d{14}`, the unverifed-capture hole is not).
9. **RELAX-C6 — APPEND S687 tolerance is whole-row.** One missing base S687 line tolerated iff some `| S687 ` line has status `queued`; URL/kind/tier/quote cells may silently change despite docstring "only allowed change is used-by/status mined→queued".
10. **RELAX-C7 — claimed counts unpinned.** "237 -> 238 entries, linguistics 29 -> 30" only indirectly via sweep.py's rows==files; counter pins no absolute count (675 rows is pinned via APPEND +32).
11. **RELAX-CA1 — NITS checks 2 of 3 nits and is half-vacuous.** No 6↔9 check; `45`∧`47` both present in base LOG.md; whole-file scope; executed false-PASS (CriticCa, W04+27 append).
12. **RELAX-CA2 — REVNAMES is unordered membership.** Any file containing all 8 tokens passes; no sha↔receipt binding (CriticCa:133 names the same gap; B2CriticClaims:34 pre-named it).
13. **RELAX-CA3 — DISPO tokens region-free.** "item 5/6/7", "S687"∧"queued", "S693"∧"docs" anywhere in LOG.md; s693 conjunct true at base.
14. **RELAX-CA4 — R63SEP global tokens.** "REC" substring anywhere in a 4100-line file + one literal phrase.
15. **RELAX-CA5 — HISTOGRAM marker unbound.** `"A 13 / B 11" | "A=13 B=11" | "13 / 11"` anywhere in SCORECARD; not bound to the r63 correction row.
16. **RELAX-CA6 — PTRS scope confined to the r63 SCORECARD block + stray** (rev1, documented; dead pointer elsewhere — e.g., the new r64 LOG entry itself — passes).

## 7. Fixture/pin honesty defects (lane-edit gameable)

- **FIXTURE-C1 — unpinned executed tools**: `tools/check-cited-lines.py` (ONEID) and `reports/round-28/readme/sweep.py` (SWEEP) run from the working tree with no byte check; NOHARM diffs only `corpus/knowledge`, so editing either tool is invisible to the counter. Same class as RevCounterC H2 — closed for the locator only.
- **FIXTURE-C2 — NOHARM pins literal `main`**, not the measured revision, and compares committed refs while every other leg reads the working tree: uncommitted `corpus/knowledge` edits escape NOHARM but are scored by FILE/ROWS.
- **FIXTURE-O1 — O evidence chain broken**: `final-measures-o.txt` on disk is truncated (no measured-revision header, no counter sha, no MUT section, no verdict); `mut-o.txt`/`edge-o.txt`/`control-o.txt` claimed in `claims.json:38-41` lands do not exist; cited counter-sha `bb0c74a4…` is unverifiable.
- **FIXTURE-C3 — locator pin comment cites the wrong base** (`65b393e` = round-63 base); the resolved pin itself is correct (lazy sha of `BASE:` blob).

## 8. Docstring/code drift (non-weakening)

- **DOC-C1** accept-c header "revision 0" stale (code = rev1+; also noted `w1/ConnectorOverlap.md:68`).
- **DOC-C2** "≥ 11 cells" vs exact `!= 11` (stricter; inherits the r63 RevCounterC fix).
- **DOC-C3** dead `it = iter(...)` line (cosmetic).
- **DOC-O1** DRIP docstring `wall ∈ [8,60]` vs code `wall < 20`.
- **DOC-O2** EDGE_HTTPS inline comment `(UNREACHABLE attempts=3 …)` vs asserted 6 (rev2 missed this comment).
- **DOC-CA1** accept-ca header "revision 0" stale (code = rev1).
- **DOC-CA2** rev1 comment mischaracterizes the rev0 bug (`## Round` count is always 0, not "never > 6"; the `> 60` threshold was unpassable regardless).

## 9. Pre-data revision proposals (forcing controls), per instruction not edits

- O/MUT exactness: run each mutant through the **full** battery and require `set(failed legs) == set(pins)`; forcing control = a mutant that flips a second leg (e.g., m8 + a GZIP-breaking patch) must then FAIL MUT.
- O tool pin: `TOOL_SHA256` resolved from `BASE:tools/reopen-row.py` like the locator pin; forcing control = byte-identical-except-docstring tool passes everything today (the declared do-nothing control) but must fail TOOL.
- Ca legs: bind each token set to the Round-64 entry region (slice `canon`/`score` at the r64 heading like PTRS's `r63_block`); add the 6↔9 nit; REVNAMES per-line `receipt  measured <sha>` association. Forcing control: the executed CriticCa W04+27 append must then FAIL NITS.
- C REJECTS: add URL presence (`URL_RE` on source cell) to match its own docstring; forcing control = a disposition row with no URL must FAIL REJECTS.
- C APPEND S687: replace whole-line tolerance with cell-diff (same line except `cs[7]`/`usedby`); forcing control = an S687 row with rewritten quote must FAIL APPEND.
- C unpinned tools: sha-pin CITED+SWEEP to `BASE:` as LIVE already does for LOCATOR.

## Confidence

High on every RELAX/DOC/FIXTURE item — each cites the code line or receipt. Medium only on attempt-1
authorship attribution (surviving reports name seats/tasks, not the hands that wrote rev1/rev3 text).
No tools installed; nothing executed beyond read-only git/jj/grep/sha256sum on the lane repo.
