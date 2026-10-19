- Seat: S03 | scribe | claim A | date 2026-10-19 | baseline 139e3b6

# Round 33 — final adjacency receipt (S03)

Assignment (`reports/round-33/targets.json:79`): **"Final adjacency receipt post-review."**
This file is the consolidation layer for claim A: it records what is verified about the
round-33 adjacency surface, at whose hand, and what is still owed before
`adj/audit-assembled.md` (`reports/round-33/claims.json:59`) can be called final.

**Status: filed post-verification, PRE-review — the review legs are owed, not done.**
At this seat's cut (2026-10-19T03:57:32Z) `reports/round-33/review/` and
`reports/round-33/cross/` were **empty** (`ls -la` → 0 files each; R07/R08 are the
adversarial pass per `targets.json:75-76`), and of the audit/verify set only
`adj/A01-province.md`, `adj/A10-receipt.md`, `adj/A13-verify-a07-a09.md`,
`adj/A15-audit-draft.md`, `adj/A16-shonen-material.md`, `adj/K04-method-scout.md` had
landed. Nothing in this file is round acceptance, an axis verdict, or a
promotion/canon/clearance/closure statement (`claims.json:68`); it is NON-CANON
engineering evidence.

---

## 1. Checks this seat ran itself (independent, re-runnable)

All commands at the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
HEAD `139e3b662900557afe54f632b468619593dc9fcb` (== `claims.json:8`), observation window
**2026-10-19T03:53:23Z–03:57:32Z**.

| # | check | command | result | verdict |
|---|---|---|---|---|
| 1 | handoff gate, current packet pair | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | `INFO scan: fields=16/16 glossary-entries=20 findings=0`, **exit 0** | GREEN |
| 2 | handoff gate, YAML twin | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.yml` | `fields=16/16 glossary-entries=0 findings=0`, **exit 0** | GREEN |
| 3 | handoff gate selftest | `… --selftest` | `selftest: OK — fixture findings 11 across 9 ids … malformed inputs exit 2`, **exit 0** | GREEN |
| 4 | PROVINCE accuracy | `sha256sum PROVINCE.md`; `git diff --name-status 139e3b6 -- PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` | `05b34a57…b942d6`; diff **empty**, exit 0 | GREEN |
| 5 | lane-instructions + contract digests | `sha256sum AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` | `1afaf106…f41035`; `5f4c02bf…f79069` | see F-4 (AGENTS drift) |
| 6 | contract digest vs live packet pin | `grep -n 5f4c02bf reports/round-28/pinsweep/v3-baseline-r28/packet.md` | `:14`, `:39`, `:103` — the `contract_ref` §1 pin carries the **same** digest as the live file | GREEN |
| 7 | tracked-path baseline | `git ls-files \| wc -l`; `git ls-tree -r --name-only 139e3b6 \| wc -l` | **2655 == 2655** | GREEN |
| 8 | count decomposition (the 1,870-vs-2,655 reconciliation) | `git ls-files \| grep -c '^reports/round-'`; `… \| grep -vc '^reports/round-'`; `git ls-tree -r --name-only HEAD -- reports/round-{8..31}`; same for `tools/gates/frozen/round-{8..31}` | round paths **1830** + other **825** = 2655; protected surface **1735 + 135 = 1870** — reproduces `reports/round-32/scope.md` exactly | GREEN (no drift) |
| 9 | frozen / corpus / examples surface | `git status --porcelain=v1 -uall -- tools/gates/frozen tools/gates/expected tools/gates/fixtures corpus examples out` | **0 rows** | GREEN |
| 10 | scope delta inventory | `git status --porcelain=v1 -uall` | ` M LOG.md` (append, +18 insertions, mtime 03:42:59Z — **pre-wave**, before the 03:49:01Z declaration), `?? REGIMEN.md`, `?? reports/round-33/**` | GREEN *except* the transient window in §3 |
| 11 | language audit (A08 class, partial) | `grep -rniE "promotion\|canoniz\|clearance\|closure" reports/round-33/` | **61 raw hits** at 03:55:57Z; every un-negated hit is a quoted rule token (A15's own grep string, O04's `Admitted/Rejected` format description, K01's quoted LOG falsification clause, O01's filed-LOG line references) or a negation/mission text — **zero asserting hits** | GREEN (time-stamped partial; A08 owns the verdict) |
| 12 | c31 counting command behaviour | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (tool verified read-only first: only `open(path, "rb")` / `open(path, encoding="utf-8")` at `reports/round-25/audit/c31-lessons-index-audit.py:61,68`) | `lesson files: 33`, `index rows: 26`, `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, `findings: 2`, **exit 1** | see F-2 (contradicts A10-F3's exit-code leg; agrees with A13) |

Row 11's grep is a **partial** scan (X03-R5: a language leg is red-by-construction unless it
declares its token list and path scope, because the declaration files carry the prohibited
words in prohibitive context). No write outside this file; no git-mutating command; no
installs; no network. One transient capture file, `/tmp/c31-s03.txt` (row 12's stdout), was
created and **removed** at 04:05:10Z; nothing under the repo was written but this file.

## 2. The A-fragment set at this seat's cut

| fragment | role | what it contributes to claim A | its own verdicts |
|---|---|---|---|
| `adj/K04-method-scout.md` | scout | the r21/r29 check-set extraction (12-seat + scoped variants) and the limits carried forward: adjacency ≠ canon/rights/community/truth certification | method only |
| `adj/A01-province.md` | executor | PROVINCE last-touch, owns-list, refuses-list, write-scope — 4 checks | **4 × PASS**, plus a precision correction (last touch `c53782a` is **pre-round-5**, not "pre-round-8") and A01-5 filed-byte finding routed to A03/X02 |
| `adj/A10-receipt.md` | executor | 9-row provisional A01–A09 table executed by that seat (fragments were unfiled) + findings A10-F1…F6 | provisional; superseded by fragments where they differ (its own A10-F5 rule) |
| `adj/A13-verify-a07-a09.md` | verifier | independent re-run of 5 filed r21/r29 commands (all **hold — exact**); A08-class scan; A09-class pin measurement | **3 named findings**: F1 (claim-O after-state vs the r26 README pin are mutually exclusive as written — three named options for the integrator), F2 (two different "tracked path" baselines), F3 (the r21 filed `A21-D4-XF-01` evidence no longer reproduces; the repair trail is filed and routed) |
| `adj/A15-audit-draft.md` | scribe | the assembly skeleton for `audit-assembled.md` with 16 verdict slots + §8 integrator recipe | 3 findings F-A15-1/2/3, all assembly-time |
| `adj/A16-shonen-material.md` | scribe | the four SHONEN boxes' round-33 state: all untouched, conditions carried named | no mark moved; marks operator-owned |
| `adj/A02-handoff.md` | executor | handoff boundary on the pair **determined by wiring, not by mtime** (`tools/exercise-handoff-e2e.py:1933-1934` → `reports/round-30/handoff/declared-in-r6/`), plus gate, harness and tamper probes with two disclosed probe-design errors | GREEN; **A02-H1** (material: the current pair's D4-CL05/06/07/09 and OQ-V3-05 prose is stale against its own manifest rows — routed to the packet/renderer owner, outside claim A) |
| `adj/A03-scope.md` | executor | scope watch **PASS at 03:57:47Z**: 2655/2655 tracked, 1830 round paths, 179 lessons, 237 frozen, **0** protected-root status rows, in-lane delta only | **A03-F1** — the authoritative form of §3 below (timeline, digests, mechanism, probable writer C05 `to-verify`); two fleet-root non-bleed observations (another lane's round-104 report; a stray `bash: ` directory predating the round) |
| `adj/A04-bleed.md` | executor | zero unfiled bleed; fleet L0 state (4 kotodama rows, append-only 4 additions / 0 removals, commit map), contract digest chain `e834f503…`→`50c4c2f2…`→`5f4c02bf…`, sibling `lore-shokunin` L0 read-only | GREEN + F-A04-1 (process/scope) and F-A04-2 (expected integrator-side); neither is bleed |
| `adj/A06-contested.md` | executor | contested-scope posture restated: CS-1 bilateral same-revision read (contract `:14-16,127,150,209`; packet-side still pending at `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`; lane rows `corpus/lessons/README.md:154-155`), plus the operator-gated items | GREEN — **zero absorption** at the recorded instants |
| `adj/A09-pins.md` | executor | full pin-surface inventory: frozen surface clean; non-frozen exposures E1 (r26 `README_BASELINE_BLOB` + seat tool `reports/round-26/lessons/c51-revision-audit.py:48`), E2 (receipt digest maps), E3 (box-1 re-survey), E4 (line anchors incl. `AGENTS.md:42`'s "after :534" instruction), E5 (README in-file pins); re-pin list R1–R8 | GREEN + A09-F1..F5; rules A10's A09 row **errata, not a second vote** |
| `adj/A12-verify-a04-a06.md` | verifier | independent A04/A05/A06 class re-runs at its own stamps | GREEN (agrees with A10's provisional rows); **A12-DEF-01** — a fourth independent filing of §3's event, with HEAD→live Git blobs per file |
| `adj/A05-corpus.md` | executor | corpus boundary: partitions vs the PROVINCE owns-list set-diffed **both directions**, `examples/` non-canon stamps, verification/civilizations drift check | PASS — exact set match, no drift |
| `adj/A07-history.md` | executor | **11** filed r21/r29 commands re-run verbatim at HEAD, with the audit-time tree archived (`git archive 8115eaa…`) to reconstruct count revisions | **9 of 11 hold exactly; 2 superseded by later filed rounds, neither by drift** (D1: r21's typed-gate leg count 19→20; D2: `AGENTS.md` digest superseded). No filed verdict found false as filed |
| `review/R07-adj-review.md` | reviewer | **23 independent executions**, audit-table completeness, bleed hunt | **R07-F1** (A10-F3 false as written — see §5 S03-F2), **R07-F2** (three-file written set), R07-F3 (packet-pair referent resolved by A02's wiring evidence; the YAML sample's 0-glossary reading is expected shape), R07-F4 (README pins supersede A10's A09 row), R07-F5 (closes A15's F-A15-1 with A01's wording), R07-F6/F7 (drift reproduces; completeness green on coverage, five rows lacked fragments) |
| `cross/X00-connector.md`, `cross/X03-protocol.md`, `cross/X04-honesty.md` | connector / critics | X00: shared-file collision + pin matrix (A09's dependency). X03: protocol register — **R1** (the §3 event, ranked highest), R2 (claim C's "12"), R3 (two counting commands), R4 (C/A counting commands unrunnable), **R5** (language grep is red-by-construction without a declared scope — §1 row 11 must name its tokens and path scope), R6 (godspeed lead), **R7** (pin the packet pair). X04: honesty register | cross-class; R1/R5/R7 bear directly on this receipt's legs |

**Still unfiled at this seat's final check (owed, see `## Owed`):** A08, A11, A14, R08.
Claim A's required "every A01-A10 check verdict filed" (`claims.json:59`) is therefore
**not yet met** (A08's language verdict is the outstanding A01–A10 row) and A14's
row-for-row match is unsatisfiable — but the **review leg has run**: R07 filed and
re-executed the A01–A09 check classes itself rather than certifying absent fragments
(`targets.json:10`), and its rows agree with this seat's wherever they overlap (handoff
gate rows 1–2; c31 plain-mode exit 1).

## 3. S03-F1 — filed-round bytes rewritten in place during the wave, then restored
(corroborated; **A03-F1 is the authoritative form**)

This is the one item in this receipt that touches the round's hard boundary
(`targets.json:6`, "never edit filed round bytes: reports/round-1..32/**"), and it is why
the scope verdict in §1 row 10 must be read as "clean at the recorded instants, with a
recorded mutation window".

**Timeline (all 2026-10-19 UTC; each row is a live sample, not a reconstruction):**

| time | observer | observation |
|---|---|---|
| 03:49:01Z | declaration | `claims.json:7`; `reports/round-33/` holds claims/targets/telemetry only |
| 03:52:07–03:52:30Z | O07 | `git status` = 3 rows; **no** filed-round modification (`op/O07-baseline-receipt.md`, capture window) |
| ~03:52:5xZ | A16 | ` M reports/round-7/validation.json` present, diff inventory 189→201 files (`adj/A16-shonen-material.md` §4) |
| 03:53:23Z | S03 | ` M reports/round-7/validation.json` |
| 03:53:29Z | S03 | `reports/round-7/validation.json` mtime `00:53:28.557 -0300` = 03:53:28Z |
| 03:53:56Z | A01 | ` M reports/round-5/validation.json` **and** ` M reports/round-7/validation.json` (A01-5) |
| 03:53:57Z | S03 | same two rows; round-5 appeared between the two S03 samples |
| 03:54:15–18Z | S03 | mtimes advance: r5 03:54:15.802, r6 03:54:15.831, r7 03:54:18.609 — **round-6 is rewritten too** |
| 03:54:32–35Z | S03 | mtimes advance again: r5 03:54:32.592, r6 03:54:32.624, r7 03:54:35.490 |
| 03:54:50Z | S03 | `git status` filed rows: r5 + r7 only — round-6's rewrite landed **byte-identical** to HEAD (advancing mtime, no diff) |
| 03:54:59Z | O07 | 4 rows (` M LOG.md`, ` M reports/round-5/validation.json`, ` M reports/round-7/validation.json`, `?? REGIMEN.md` + round-33) |
| **03:55:27.940Z** | S03 | r5 and r7 written with the **same nanosecond mtime**; live digests now **equal** HEAD digests (r5 `73a66f74…`, r7 `2f4c1e15…`); `git status` filed rows → **0** |
| 03:55:28.871Z | S03 | `.git/index` mtime — consistent with a Git-level restore, **not** proof of one (`to-verify`) |
| 03:55:37Z / 03:55:57Z / 03:57:25Z | S03 | filed rows 0; live == HEAD for r5/r6/r7 |

**Content of the transient rewrite** (read-only `git diff` while it was live):

- `reports/round-7/validation.json` (1 insertion, 1 deletion): the recorded
  `failures[]` inventory line moved `{'files': 189, 'raw_lines': 688, 'raw_occurrences': 700,
  'ci_occurrences': 702, 'marker_occurrences': 633}` → `{'files': 201, 'raw_lines': 717,
  'raw_occurrences': 731, 'ci_occurrences': 733, 'marker_occurrences': 655}`.
- `reports/round-5/validation.json` (2 insertions, 2 deletions): the claim-O `error`
  string was replaced by a `tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`
  could-not-evaluate dump (**7/7 rows** `gate_digest_mismatch`), and
  `tested_file_sha256["tools/check-gate-battery.py"]` moved `0a126b70…` → `455b595a…`.
  `tools/check-gate-battery.py` itself was **not** modified in the working tree, so the
  rewrite records a re-run against a *different* battery revision than the one the receipt
  was filed with.

**Cross-seat corroboration and authoritative form.** The event has independent filings from
**eight seats**: this receipt, A01-5, **A03-F1**, A04's F-A04-1, A12-DEF-01, R07-F2,
X03-R1, plus the O07/A16 observations. **A03-F1 is the authoritative record** and adds
three things my samples could not: (a) the in-tree runs time to **03:53:25–28Z,
03:54:15–18Z and 03:54:32–35Z**, with an isolated-copy control leg at 03:54:39–42Z;
(b) the mechanism — `reports/round-7/run-validation.py:1171-1172` and
`reports/round-5/run-validation.py:194` write their own `validation.json` unconditionally,
so running a filed round's runner in-tree rewrites its receipt (exactly the class
`tools/harness/receipt_guard.py` refuses unless `REFRESH_RECEIPTS=1`, exit 3);
(c) the precedent — the same signature is already on record at `corpus/lessons/round-20.md:120`
and `reports/round-32/scope.md:171` (citing `reports/round-28/scope.md:12`), so this is a
recurring hazard, not a one-off. A03 names the probable writer as the **C05** seat
(`to-verify`: the `c05-*` scratch namespace and matching mtime spacing between the in-tree
and isolated legs) — inference, not proof; X03 scanned all 64 missions for
`reports/round-\d+/run-validation\.py` and found **zero** hits, so no mission authorizes it.
Corrected set: **three files written (r5, r6, r7); two content-mutated**
(r5 `73a66f74…`→`fe926984…`, r7 `2f4c1e15…`→`af0cf4ed…`); r6 byte-identical. This is **not**
an authorized refresh: HEAD never moved (`git rev-parse HEAD` = `139e3b6` at every sample),
the guard env was absent, and a refresh leaves new bytes where this left the pre-edit
revision. Bytes are clean at every sample since 03:55:27Z and no repair is owed — but the
**record** is owed (a LOG/telemetry note naming the class, the paths, the window and the
restored digests), and the round's scope verdict may not be stated as "no filed byte was
touched". X03-R1's standing recommendation: the round-33 runner's protected set must cover
**rounds 1–32** — round-32's covered only 8–31 (`reports/round-32/run-validation.py:60-62`),
so a round-1..7 drift would pass unnoticed.

## 4. Claim-A after-required checklist (`claims.json:59`)

| clause | status | evidence / owed path |
|---|---|---|
| PROVINCE accuracy re-verified at HEAD | **filled** | `adj/A01-province.md` (4 PASS; precision correction pre-round-5) + S03 rows 4/7; R07 row 17 agrees |
| handoff gate green on the current packet pair | **filled** | S03 rows 1–3 (exit 0 on both sample packets, selftest OK); `adj/A02-handoff.md` (pair resolved by **wiring**, plus foreign-cwd run and tamper probes) and R07 rows 1–6 agree |
| zero unfiled cross-domain bleed | **filled** | S03 rows 9/10; `adj/A04-bleed.md` GREEN; `adj/A05-corpus.md` PASS (partitions set-diffed both ways, `examples/` non-canon, no partition drift); `adj/A12-verify-a04-a06.md` GREEN; R07 §3 zero unfiled bleed |
| scope watch clean | **filled, with §3's mutation window named** | S03 rows 7/8/10; `adj/A03-scope.md` PASS at 03:57:47Z (0 protected-root rows) — a time-stamped reading, not a standing property |
| contested-scope items restated routed-not-absorbed with current pointers | **filled** | `adj/A06-contested.md` (CS-1 + operator-gated items, pointers re-verified) + S03 in-repo pointer checks; A12 §3 GREEN |
| no promotion/canon/closure language anywhere in round-33 artifacts | **partially filled** | S03 row 11 (zero asserting hits at 03:55:57Z); A13's and A04's scans agree; **A08 owed** for the final fragment set. **X03-R5 caveat: the leg is red-by-construction unless it declares its token list and path scope** — the declaration files themselves carry the prohibited words in prohibitive context |
| supporting classes: history consistency, pin cascade | **history filled; pins filled with errata** | `adj/A07-history.md`: 11 filed r21/r29 commands re-run, **9 hold exactly, 2 superseded by later filed rounds** (D1 leg count, D2 AGENTS digest) — no filed verdict false as filed; `adj/A09-pins.md` (E1–E5, R1–R8) rules A10's A09 row errata |
| `adj/audit-assembled.md` backed by A01-A10 + A11-A14 | **owed** | integrator artifact; `adj/A15-audit-draft.md` §1 (16 verdict slots) + §8 recipe; A08/A11/A14 and R08 must land first |

## 5. Findings carried by this receipt

| id | finding | owner | status |
|---|---|---|---|
| **S03-F1** | Filed-round receipts (r5, r6, r7) rewritten in place during the wave, then restored at 03:55:27Z. **Superseded in form by `adj/A03-scope.md` A03-F1** (three written / two content-mutated; probable writer C05 `to-verify`); independently filed by A01-5, A04, A12-DEF-01, R07-F2 and X03-R1. | A03 (record) + X02 (conformance) + integrator (carry it; do not read "restored" as "did not happen") | filed by A03; record owed |
| **S03-F2** | **Errata on `adj/A10-receipt.md` A10-F3 — resolved by `review/R07-adj-review.md` R07-F1, which is authoritative.** A10's "exits 0 while reporting failures" is false for the default invocation: `reports/round-25/audit/c31-lessons-index-audit.py:462` returns `1` when findings exist, and my run (03:57:25Z) and A13's both measured **exit 1**. The exit-0-with-findings behaviour exists **only under `--json`** (`:456-458` returns 0 unconditionally). Corrected form: *plain-mode exit code is informative; a leg that runs `--json` must assert on `findings[]`.* | A14 (row-for-row match) + integrator (adopt R07's wording) | **resolved** — carry R07-F1 |
| **S03-F3** | **Errata pointer on `adj/A10-receipt.md`'s A01 row** ("pre-round-8, matches the round-32 D11 claim"). `adj/A01-province.md` measured the true bound — **pre-round-5** — and **R07-F5 closes A15's F-A15-1 with A01's wording**. The fragment wins under A10-F5's own rule. | A14 + integrator | **resolved** — carry A01's wording |
| **S03-F4** | `AGENTS.md` digest drift vs the r29 filed value: r29 filed `be3a9477…` (`reports/round-29/adjacency/province-entries.md:15`); live `1afaf106…`. Explained by later commits; PROVINCE and the contract still reproduce their r29 digests byte-exactly, so the r29 province/contract verdicts stand. | A07/A13 + integrator | carried, no action (R07-F6 confirms) |
| **S03-F5** | The A-fragment set is still incomplete (A05, A07, A08, A11, A14, R08), so claim A's threshold "every A01-A10 check verdict filed" is unmet and this receipt cannot be final. | integrator (re-assemble per `adj/A15-audit-draft.md` §8) | open |
| **S03-F6** | Carried, not mine to judge: A13's F1 (claim-O's after-state vs the r26 README pin are mutually exclusive as written; **A09's E1–E5 + R1–R8 supply the full cascade, and A09 rules A10's A09 row errata**) and R07-F4's confirmation that the lessons README carries two live filed-round pins outside the frozen surface. These bound what claim A's audit may assert about the lessons index. | claim-O/claim-C seats + integrator | carried |
| **S03-F7** | Cross-class, bearing on this receipt: X03-R2 (claim C's "12" not reproducible from its named source — 9 debt rows in the dossier table), X03-R3 (two counting commands do not survive mechanical re-execution), X03-R4 (the C/A counting command `reports/round-33/run-validation.py` did not exist at seat time), X03-R7 (pin the packet pair — S03 §1 rows 1–2 supply the two sample digests). | integrator + S04/C13 | carried |

## 6. What this receipt does not establish

- Not round acceptance, not an axis verdict, not a promotion/canon/clearance/closure
  statement (`claims.json:68`). No axis is judged here.
- Not a complete review pass: R07 landed and its rows are folded in above; **R08 had not
  filed at this seat's cut**, so the pin-cascade review leg (A09/X00 matrix) is owed.
- The scope and language readings are **sampled and time-stamped**, not continuous watches:
  they cannot prove the absence of a transient write-and-restore between samples — §3 is a
  live example of exactly that class.
- No fleet-root surface was assessed by this seat beyond the in-repo pointers; no sibling
  tree, world bible or domain source tree was read.

## Owed

Fragments still absent at this seat's final check (2026-10-19T04:05Z), to be filled by
their owners and folded into `adj/audit-assembled.md` by the integrator. Landed since this
receipt's first draft and folded in above: A02, A03, A04, A05, A06, A07, A09, A12, R07,
X00, X03, X04.

- `reports/round-33/adj/A08-language.md`
- `reports/round-33/adj/A11-verify-a01-a03.md`
- `reports/round-33/adj/A14-verify-a10.md`
- `reports/round-33/review/R08-adj-review.md`
- `reports/round-33/adj/audit-assembled.md` (integrator; `claims.json:59`)

Also owed, none of it this seat's to produce:

- The **record** of §3's mutation event (A03-F1): a LOG/telemetry note naming the class,
  the three paths, the window and the restored digests, plus the X03-R1 protection fix for
  the round-33 runner (protected set must cover rounds 1–32, not 8–31).
- The **errata application** for S03-F2 (carry R07-F1's corrected wording, withdraw
  A10-F3's exit-code claim) and S03-F3 (carry A01's pre-round-5 wording, close A15's
  F-A15-1) — A14 owns the row-for-row match.
- `reports/round-33/run-validation.py` — claim A's counting command; it did not exist at
  any seat's check (X03-R4), so no A threshold can be measured green until the integrator
  writes it.

## Citations

- `reports/round-33/claims.json:7` (declaration time), `:8` (baseline commit), `:29`
  (claim-O after-state), `:33` (c31 counting command), `:57` (tracked-path baseline),
  `:59` (claim-A after-required), `:61` (A counting command), `:68` (non-goals)
- `reports/round-33/targets.json:6` (filed-byte boundary), `:10` (missing-dependency rule),
  `:75-76` (R07/R08 missions), `:79` (S03 mission + out path)
- Landed A-set folded into §2/§4/§5: `adj/A01-province.md` (4 PASS + A01-5 filed-byte
  finding; pre-round-5 precision correction); `adj/A02-handoff.md` (pair-by-wiring;
  A02-H1); `adj/A03-scope.md` (**A03-F1** authoritative timeline, digests, mechanism,
  probable writer C05 `to-verify`); `adj/A04-bleed.md` (L0 state, digest chain, F-A04-1/2);
  `adj/A06-contested.md` (CS-1 pointers); `adj/A09-pins.md` (E1–E5, R1–R8, A09-F1..F5);
  `adj/A10-receipt.md` (provisional table, A10-F1…F6); `adj/A12-verify-a04-a06.md`
  (**A12-DEF-01**, GREEN re-runs); `adj/A13-verify-a07-a09.md` (5 filed commands hold —
  exact; F1/F2/F3; `c31_exit=1` expectation); `adj/A15-audit-draft.md` (§1 slots, §8
  recipe); `adj/A16-shonen-material.md` (§4 filed-byte observation);
  `adj/K04-method-scout.md` (r21/r29 check sets, limits)
- `reports/round-33/review/R07-adj-review.md` (**R07-F1** authoritative on A10-F3's
  exit-code error; **R07-F2** three-file written set; R07-F3 packet-pair referent;
  R07-F4 README pins; R07-F5 closes F-A15-1; R07-F6/F7); `cross/X00-connector.md` (pin
  matrix); `cross/X03-protocol.md` (**R1** mutation event, **R2** claim-C "12", **R3**
  counting commands, **R4** unrunnable C/A command, **R5** language-grep scope,
  **R6** godspeed lead, **R7** packet pair); `cross/X04-honesty.md`
- `reports/round-33/op/O07-baseline-receipt.md` (03:52Z capture window; 03:54:59Z 4-row
  observation); `op/K01-falsifier-scout.md`; `op/O01-row-drafts.md`;
  `op/O04-format-checks.md`; `scribe/S04-integration-draft.md:308-336,409,430-432`
- `reports/round-32/scope.md` (1,870 = 1,735 + 135; 237 frozen; `:171` historical-validator
  rewrite hazard); `reports/round-32/run-validation.py:60-62` (protected set 8–31);
  `reports/round-32/dossier-d13-operator-decisions.md:135` (lore-owned row)
- `reports/round-29/adjacency/province-entries.md:15` (r29 filed AGENTS digest `be3a9477…`)
- `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14,39,103` (contract digest pin);
  `reports/round-28/scope.md:12` (earlier rewrite-then-restore precedent)
- `reports/round-26/run-validation.py:97` and `reports/round-26/lessons/c51-revision-audit.py:48`
  (README blob pin `a3187055…`); `reports/round-25/validation.json`
  `input_sha256["corpus/lessons/README.md"]` = `ec7469da…`
- `reports/round-25/audit/c31-lessons-index-audit.py:61,68` (read-only file access),
  `:456-458` (`--json` returns 0 unconditionally), `:462` (`return 0 if not findings else 1`)
- `reports/round-5/run-validation.py:194`; `reports/round-7/run-validation.py:1171-1172`
  (unconditional self-write, the §3 mechanism); `corpus/lessons/round-20.md:120` (same
  signature on record)
- `tools/harness/receipt_guard.py` (module docstring: refused overwrites, exit 3,
  `REFRESH_RECEIPTS=1` override)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:14-16,127,150,209`
- Commands run by this seat, 2026-10-19T03:53:23Z–04:01:01Z, lane root, read-only except
  this file:
  `git log --oneline -3`; `git status --porcelain=v1 -uall` (whole lane and scoped to
  `reports/round-*`, `tools/…`, `corpus`, `examples`, `out`); `git diff --name-status 139e3b6
  -- PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `git diff --stat/--numstat/-- reports/round-5/validation.json reports/round-7/validation.json`;
  `git ls-files | wc -l` (2655); `git ls-files | grep -c '^reports/round-'` (1830);
  `git ls-files | grep -vc '^reports/round-'` (825); `git ls-tree -r --name-only HEAD --
  reports/round-{8..31}` (1735); `… -- tools/gates/frozen/round-{8..31}` (135);
  `git ls-tree -r --name-only 139e3b6 | wc -l` (2655); `sha256sum PROVINCE.md AGENTS.md
  corpus/knowledge/synthesis/worldbible-integration-contract.md examples/handoff-packet.sample.md
  examples/handoff-packet.sample.yml`; `git show HEAD:reports/round-{5,6,7}/validation.json |
  sha256sum`; `stat -c '%n %y %s' reports/round-{5,6,7}/validation.json .git/index LOG.md
  REGIMEN.md`; `python3 tools/gates/handoff-packet-check.py` (both packets + `--selftest`);
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 1);
  `grep -rniE "promotion|canoniz|clearance|closure" reports/round-33/`;
  `grep -n 5f4c02bf reports/round-28/pinsweep/v3-baseline-r28/packet.md`;
  `grep -n "be3a9477" reports/round-29/adjacency/province-entries.md`;
  `grep -n "open(\|write" reports/round-25/audit/c31-lessons-index-audit.py`;
  `find reports/round-33 -type f` at 03:53–04:01Z (fragment landings); `find reports/round-33
  -type f -newermt '2026-10-19 03:49'`;
  `ps -eo pid,lstart,etimes,args` polls (03:54:50Z–03:55:30Z, no matching validator process
  observed at any sample instant — the writers are short-lived; attribution stays
  `to-verify`); `date -u '+UTC=%Y-%m-%dT%H:%M:%SZ'` at each sample
- `reports/round-33/op/O07-baseline-receipt.md` (03:52Z capture window; 03:54:59Z 4-row
  observation); `reports/round-33/op/K01-falsifier-scout.md`; `op/O01-row-drafts.md`;
  `op/O04-format-checks.md`; `scribe/S04-integration-draft.md:308-336,409,430-432`
- `reports/round-32/scope.md` (1,870 = 1,735 + 135; 237 frozen; 22 ignored/13 pyc)
- `reports/round-32/dossier-d13-operator-decisions.md:135` (lore-owned row)
- `reports/round-29/adjacency/province-entries.md:15` (r29 filed AGENTS digest `be3a9477…`)
- `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14,39,103` (contract digest pin)
- `reports/round-25/audit/c31-lessons-index-audit.py:61,68` (read-only file access only)
- `tools/harness/receipt_guard.py` (module docstring: refused overwrites, exit 3,
  `REFRESH_RECEIPTS=1` override)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:15,150`
- Commands run by this seat, 2026-10-19T03:53:23Z–03:57:32Z, lane root, read-only except
  this file:
  `git log --oneline -3`; `git status --porcelain=v1 -uall` (whole lane and scoped to
  `reports/round-*`, `tools/…`, `corpus`, `examples`, `out`); `git diff --name-status 139e3b6
  -- PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `git diff --stat/--numstat/-- reports/round-5/validation.json reports/round-7/validation.json`;
  `git ls-files | wc -l` (2655); `git ls-files | grep -c '^reports/round-'` (1830);
  `git ls-files | grep -vc '^reports/round-'` (825); `git ls-tree -r --name-only HEAD --
  reports/round-{8..31}` (1735); `… -- tools/gates/frozen/round-{8..31}` (135);
  `git ls-tree -r --name-only 139e3b6 | wc -l` (2655); `sha256sum PROVINCE.md AGENTS.md
  corpus/knowledge/synthesis/worldbible-integration-contract.md examples/handoff-packet.sample.md
  examples/handoff-packet.sample.yml`; `git show HEAD:reports/round-{5,6,7}/validation.json |
  sha256sum`; `stat -c '%n %y %s' reports/round-{5,6,7}/validation.json .git/index LOG.md
  REGIMEN.md`; `python3 tools/gates/handoff-packet-check.py` (both packets + `--selftest`);
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 1);
  `grep -rniE "promotion|canoniz|clearance|closure" reports/round-33/`;
  `grep -n 5f4c02bf reports/round-28/pinsweep/v3-baseline-r28/packet.md`;
  `grep -n "be3a9477" reports/round-29/adjacency/province-entries.md`;
  `grep -n "open(\|write" reports/round-25/audit/c31-lessons-index-audit.py`;
  `ps -eo pid,lstart,etimes,args` polls (03:54:50Z–03:55:30Z, no matching validator process
  observed at any sample instant — the writers are short-lived; attribution stays
  `to-verify`); `date -u '+UTC=%Y-%m-%dT%H:%M:%SZ'` at each sample
