# ExecScorecardConsistency — round-76 SCORECARD corrections table vs. frozen Ca ledger vs. SKILL.md:707 repair

**Seat:** ExecScorecardConsistency (wave-2 falsification, kotodama round 76)
**Base:** `98c486bdb4650ba5b8e651d332910e8ee60ad121` · **Freeze (C/Ca config):** `df0f0309d61e5485bb17035d3f8791b1e6a11d40` · **Ca landing:** `a43ed807ea38b5fc5a7875a839d576cea73aba7c` · **C landing:** `722e69ff6361aadf148cb46acbf6ac8fd147f59a`
**Scope:** exact token/command consistency of `SCORECARD.md` `## Corrections — round 76` against the frozen `reports/round-76/ledger.json` + `reports/round-76/claims.json` + `reports/round-76/accept-ca.py`, and of the `SKILL.md:707` repair against the ledger's `statement_after` grammar. **No edits, no counter reruns, no lane files touched.**

## Verdict

**NOT consistent. Four divergences, all traceable to frozen artifacts, none fixable by editing the SCORECARD table in this round.**

| # | Row / site | Divergence | Grading effect |
|---|---|---|---|
| **D1** | L76-19, L76-20, L76-21 — SCORECARD command column | table cell ≠ ledger `rederive` (missing shell quotes around the `-E` pattern) | ANNOTATE + NOSTUB red (2 legs) |
| **D2** | L76-19 — ledger `stated_text` | stated_text does not exist anywhere in the base tree | LEDGER red |
| **D3** | L76-16 — `SKILL.md:707` | landed wording cannot satisfy the frozen `statement_after.parse` | REPAIR red |
| **D4** | L76-13 — SCORECARD prose | discloses 1 of the 2 leg failures the pair causes | disclosure gap (both LEDGER + SEPARABLE red) |

Plus one **residual attribution defect** in the SKILL.md:707 repair (D5, below): the repaired row still attributes the committed counter's `85/85` to the receipt stamped with the *pre-freeze* digest.

---

## D1 — L76-19 / L76-20 / L76-21: the SCORECARD command column is not the ledger's rederive string

**Evidence (committed bytes).**
- `reports/round-76/ledger.json` @ `df0f030` (blob `c4ac11e`), `rederive` fields:
  - L76-19, line 408: `git grep -h -E ^window: chars= 98c486b… -- reports/round-75/evidence/S892.txt`
  - L76-20, line 432: `git grep -h -o -E ^sha256: [0-9a-f]{8} 98c486b… -- reports/round-75/evidence/S885.txt`
  - L76-21, line 456: `git grep -h -o -E ^sha256: [0-9a-f]{8} 98c486b… -- reports/round-75/evidence/S887.txt`
- `SCORECARD.md` @ `a43ed80` (blob `fea2011`) `## Corrections — round 76` rows 1531–1533 carry the **quoted** form, e.g. L76-19 row 1531: `git grep -h -E '^window: chars=' 98c486b… -- reports/round-75/evidence/S892.txt`.
- Byte comparison of the 19 table cells against the ledger: **16 rows identical to `rederive`; 3 rows (L76-19/20/21) identical to `shlex.join(observe_cmd)` instead.** The three rows are exactly the three whose `-E` pattern contains a space and was therefore written unquoted in the ledger.

**Mechanism (frozen counter `reports/round-76/accept-ca.py` @ `df0f030`, blob `d58b7ee`).**
- `rederive_argv` (lines 1377–1383) does `shlex.split(raw)` on the ledger's `rederive`. The unquoted pattern splits into two operands, so `_git_grep_problem` (line 1046) sees `chars=` (L76-19) or the base revision `98c486b…` (L76-20/21) as a **path operand** and refuses it.
- Reproduced against a clone of base `98c486b` with the frozen module's own functions:
  - L76-19 → `git grep path operand 'chars=' does not exist in the clone`
  - L76-20 / L76-21 → `git grep path operand '98c486bdb4650ba5b8e651d332910e8ee60ad121' does not exist in the clone`
- `leg_nostub` (line 2074) compares the ledger's `rederive` text against the row text (line 2106 `if cmd not in nr`) → stubs `L76-19:rederive-cmd`, `L76-20:rederive-cmd`, `L76-21:rederive-cmd`. Running the frozen `leg_nostub` against the landed `SCORECARD.md` yields exactly those three stubs and no others.
- Running the frozen `leg_annotate` yields `unannotated=3` — L76-19/20/21 only, "rederive not executable". The other 16 rows replay cleanly.

**The SCORECARD cells themselves are correct.** Each of the 19 table commands was executed as a shell command at base; all 19 exit 0 and their output parses (with the pair's own `parse`) to exactly the ledger's `expected_after`. So the table is the *shell-correct* rendering and the **ledger's `rederive` string is the defective artifact**.

**Consequence for the SCORECARD prose.** `SCORECARD.md:1535` reads "The table is a verbatim projection of the 19 ANNOTATE pairs". That is false for 3 of 19 rows in the command column (16/19 byte-identical; 3/19 equal to `shlex.join(observe_cmd)` but not to `rederive`). The value columns, by contrast, are exactly consistent: old token = ledger-derived stated token for 19/19; new token = ledger `expected_after` for 19/19 (L76-16 has no row, correct — REPAIR pairs carry a diff, not a row, matching round-75's rule and the counter's `leg_nostub`/`leg_annotate` which iterate ANNOTATE pairs only).

**Fix location.** Not the SCORECARD. Adding the missing single quotes to the three ledger `rederive` strings (or replacing them with `shlex.join(observe_cmd)`) would make NOSTUB and ANNOTATE green without touching the table. The ledger is frozen at `df0f030` and identical at `a43ed80`/`722e69f` (blob `c4ac11e` at all three), so this is a round-77 frozen-claim defect.

**Independently corroborated by the L1's own measurement** at HEAD (`af67443`, `reports/round-76/telemetry/measures-ca.txt`): "LEG FAIL ANNOTATE — three rows unannotated because L76-19/20/21 `rederive` commands are not executable under the frozen argv parser; L76-20/21 treat the base revision as a path operand and L76-19 treats `chars=` as a path operand" and "LEG FAIL NOSTUB — stubs L76-19:rederive-cmd, L76-20:rederive-cmd, L76-21:rederive-cmd". My replay of the frozen legs reproduces both details exactly.

## D2 — L76-19: the ledger's `stated_text` is not in the base tree

- `reports/round-76/ledger.json` @ `df0f030` lines 389–411: `stated_at` = `corpus/lessons/round-75.md:48`, `stated_text` = **`S892's window (`chars=4097 before=284`)`**.
- Base `corpus/lessons/round-75.md` lines 47–48 actually read:
  - 47: `   occur in the stored `--- window ---` text. S888's window (`chars=4097 before=10`) and S892's`
  - 48: `   (`chars=4097 before=284`) both start at the document head and stop well before p. 3 and p. 7, where`
  The S892 half of the sentence is split across the line break and the word "window" belongs to the S888 clause. The literal string `S892's window (`chars=4097 before=284`)` occurs **nowhere** in the base tree (`git grep` over `98c486b` → no hits).
- The frozen `leg_ledger` (accept-ca.py:1432) requires `stated_text` ⊂ normalized base body **and** ⊂ the stated_at line (lines 1552, 1572). Running it: `L76-19: stated_text not found in corpus/lessons/round-75.md at base` → LEDGER red.
- Note the SCORECARD prose (`:1535`) says "**L76-19's stated token** cannot be found at the claimed lesson line". The token `284` **is** on line 48 (`before=284`); what is missing is the **stated_text**. The same mischaracterization is carried into `corpus/lessons/round-76.md:89` @ `722e69f` ("L76-19 (stated value not found at the specified lesson line)"). The *values* in the table are right: the S892 window line in `reports/round-75/evidence/S892.txt` reads `window: chars=4097 min=4096 pad=400 before=2020 after=2026` → observed `2020` = ledger `expected_after` ✓, and the lesson's `284` is the stale value the correction targets. The defect is purely the fabricated `stated_text` anchor.

## D3 — SKILL.md:707: the landed repair cannot satisfy the frozen `statement_after.parse`

- `reports/round-76/ledger.json` @ `df0f030` lines 340–342:
  `statement_after` = `{ "path": "SKILL.md", "parse": "^\\| accept-c-75 \\|.*?committed counter sha256 `([0-9a-f]{12})`" }`
  i.e. the parser requires the literal adjacency **"committed counter sha256 `"** + 12 hex + a closing backtick.
- Landed `SKILL.md:707` @ `a43ed80` (blob `6667b9c`) reads:
  "Measured 2026-10-27: **committed counter `reports/round-75/accept-c.py` sha256 `315c5f3f27fd…`**; the receipt header's `fa5060b91bdb…` is the pre-freeze byte hash recorded in `reports/round-75/telemetry/selftest-c.txt`. …"
  Two independent breaks: (i) the path literal is inserted between "counter" and "sha256"; (ii) the digest is terminated by an ellipsis **U+2026** before the closing backtick, so even a path-tolerant `committed counter .*? sha256 `([0-9a-f]{12})`` fails (it requires the backtick immediately after the 12 hex).
- Verified by applying the frozen parse and three variants to the landed line: frozen parse → **0 matches**; path-tolerant (no trailing backtick) → `315c5f3f27fd`; path-tolerant **with** trailing backtick → 0; ellipsis-tolerant → `315c5f3f27fd`.
- The frozen `statement_after()` (accept-ca.py:1385–1413, no-match at line 1407) and `leg_repair` (line 1702) then return `L76-16(statement_after no-match in SKILL.md)` → REPAIR red. Replaying the frozen `leg_repair` against a clone of `a43ed80` gives exactly that and nothing else; the second REPAIR sub-check ("base `stated_text` must no longer remain at the statement path") **does** pass — the base text `Measured 2026-10-27 at counter sha256 `fa5060b91bdb…`` is gone from the landed row.
- The **digest value itself is correct**: `sha256sum reports/round-75/accept-c.py` = `315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261`, identical at base, freeze, Ca-lands and C-lands. And the pre-freeze stamp `fa5060b91bdb…` is exactly what `reports/round-75/telemetry/selftest-c.txt:2` records. So the *substance* of the repair is right; the **frozen parse grammar** is unsatisfiable by the landed wording. This is a frozen-ledger-vs-landed-text grammar conflict, not a factual error in SKILL.md.
- The w1 draft that proposed the edit (`.ufo/waves/round-76/w1/drafts/repairs.diff`, committed @ `df0f030`) used yet a third wording ("the committed counter sha256 is `315c5f3f27fd…`") — which also fails the frozen parse (the word "is" intervenes and the ellipsis terminates the digest). So no variant of the w1 draft would have satisfied the frozen `statement_after`.

## D4 — L76-13: the SCORECARD discloses one of the two legs this pair fails

- `SCORECARD.md:1535` discloses only: "L76-13 names a knowledge path outside the frozen append-only allowlist" — true (LEDGER leg).
- The **same** `stated_at` path `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` (ledger line 255) is also a **forbidden read** under the frozen SEPARABLE leg ("no stated_at path is corpus/SOURCES.md, corpus/knowledge/**, reports/round-76/evidence/** or .ufo/waves/round-76/assimilation/**"), so L76-13 reds **SEPARABLE** as well. Replaying the frozen `leg_separable` yields `L76-13: stated_at path corpus/knowledge/myth-symbol/narrative-structure-frameworks.md is a forbidden read (corpus/knowledge/**)` — a second, undisclosed leg failure from the same pair. (Corroborated by `reports/round-76/telemetry/measures-ca.txt` @ `af67443`: "LEG FAIL SEPARABLE — L76-13's stated_at path is a forbidden read".)
- The token columns themselves are correct for this row: old `111487` (the knowledge doc's byte list) → new `109588` (= `reports/round-75/evidence/S885.txt:5` `bytes: 109588`), and `git grep -h -E '^bytes: '` at base returns `bytes: 109588` ✓.

## D5 — residual: SKILL.md:707 still attributes the committed counter's 85/85 to the pre-freeze receipt

The landed `SKILL.md:707` sentence continues: "The committed counter prints `SELFTEST: 85/85`, exit 0 (clean landing 13/13, 78 single-edit mutants each red on its named leg …; receipt `reports/round-75/telemetry/selftest-c.txt`)." But that receipt's own header (line 2) reads `# counter sha256 fa5060b91bdb…` — the **pre-freeze** bytes — so it does not attest the committed counter `315c5f3f27fd…`. The ledger's own intent for the pair says the replacement "no longer attributes the 85/85 result to those bytes" (`ledger.json:343`), yet the landed sentence still cites that receipt for the committed counter's 85/85.

Corroboration actually exists for the committed bytes, but not in a receipt: `reports/round-75/telemetry/selftest-c.txt` is the only committed receipt printing `85/85` and it is stale-stamped; the only committed artifacts pairing `315c5f3f27fd` with `85/85` are wave-3 lane narratives (`.ufo/waves/round-75/w3/ExecRerunBoth.md:137`, `.ufo/waves/round-75/w3/RevReadmeSkillQuality.md:27` — the latter explicitly says "the committed `telemetry/selftest-c.txt` pins the pre-freeze `fa5060b9…`"), plus the round-76 w1 drafts. The mutant count `78` is consistent with the committed counter's own table (`reports/round-75/accept-c.py:5424`+, 78 `MUTANTS` entries; the stale receipt says "78 mutants over 13/13 legs").

This is a citation-accuracy defect in the repair wording, not a graded-leg failure (no frozen leg checks the 85/85 attribution). Reported for round-77.

---

## What *is* consistent (checked, negative results)

- **All 19 old tokens match the ledger.** Deriving each pair's stated token with the ledger's own `stated_parse` against the ledger's `stated_text` gives exactly the table's old-token cell for 19/19 rows.
- **All 19 new tokens match the ledger.** Table new-token cell == ledger `expected_after` for 19/19; and == the token observed in a clone at base *and* at `a43ed80` for 20/20 pairs (verified by importing the frozen counter's `observed_token` against clones of `98c486b` and `a43ed80`).
- **All 19 table commands run and reproduce their row's new token** when executed as shell commands at base (rc=0, output parses to the expected token) — i.e. the table's *command* column is right even where it diverges from the ledger string (D1).
- **Row set is right.** 19 rows for 19 ANNOTATE pairs, no row for the REPAIR pair L76-16 (round-75's rule; the counter's `leg_nostub`/`leg_annotate` iterate ANNOTATE pairs only). No ledger ANNOTATE pair is missing a row.
- **The corrections section is append-only.** `SCORECARD.md` @ `a43ed80` adds lines 1509–1535 with zero removed lines (diff hunk `@@ -1508,0 +1509,28 @@`); `SCORECARD.md` is in the frozen append-only protected set, satisfied.
- **The counter command string in the SCORECARD intro matches the frozen claim.** `SCORECARD.md:1511` `Counter: \`python3 -B reports/round-76/accept-ca.py --root . --lands <Ca-lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin --combined <C-lands> --main <Ca-lands> --work /fast/scratch/hyaku/kotodama-r76/<seat>\`` is byte-equal (backticks stripped) to `claims.json` → claim `Ca`.`counter`.
- **Corrections rows are byte-stable across the three cited landings**: identical at `a43ed80`, `722e69f` and `af67443` (SCORECARD blob `fea2011` at the first two; `af67443` rewrote only the intro line to concrete revisions and appended the axes section, leaving the 19 table rows and the prose line unchanged).
- **Value-level sanity of the corrections themselves** (context for D2/D4, not a defect): the new tokens are the committed `reports/round-75/evidence/S*.txt` values — S885 `bytes: 109588` / `sha256: 20b571d7…` (L76-11/L76-13/L76-20) and S887 `bytes: 116878` / `sha256: e0560649…` (L76-12/L76-21) — while the stale lesson values (`111486`/`2bcdd019…`, `118776`/`fbf48ad2…`) are exactly the probe-receipt values still committed at `.ufo/waves/round-75/counters/probe-receipts/S885.txt:5-6` and `S887.txt:5-6`, and the lesson itself (round-75.md:57-61) documents the Persée notice as byte-unstable across three observations (111487 / 111486 / 109589). The corrections are aimed at the committed evidence artifacts, which is the ledger's stated rule.

## Exact citations

- `SCORECARD.md` @ `a43ed80` blob `fea2011`: section heading line 1509; intro line 1511; table rows 1515–1533; prose line 1535. Identical rows at `722e69f` (same blob) and at `af67443` (blob `a6287b4`, only intro+axes changed).
- `reports/round-76/ledger.json` @ `df0f030` blob `c4ac11e` (same blob at `a43ed80`, `722e69f`): L76-13 line 255; L76-16 line 326 (`statement_after` 340–342); L76-19 line 389 (`rederive` 408); L76-20 line 412 (`rederive` 432); L76-21 line 436 (`rederive` 456).
- `reports/round-76/accept-ca.py` @ `df0f030` blob `d58b7ee`: `rederive_argv` 1377–1383; `statement_after` 1385–1413 (no-match 1407); `leg_ledger` 1432 (stated_text checks 1552, 1572); `leg_repair` 1702; `leg_annotate` 1786 (argv 1820, not-executable 1826); `leg_nostub` 2074 (argv 2086, cmd-not-in-row 2106); `_git_grep_problem` 1046.
- `reports/round-76/claims.json` @ `df0f030` blob `c0bb053`: claim `Ca` legs (ANNOTATE allowlist = LOG.md, SCORECARD.md, corpus/lessons/round-75.md, corpus/QUALITY.md; SEPARABLE forbidden list incl. `corpus/knowledge/**`).
- `SKILL.md` @ base `98c486b` blob `83aaff5` line 707 (base text); @ `a43ed80`/`722e69f` blob `6667b9c` line 707 (landed repair).
- `corpus/lessons/round-75.md` @ base: lines 28–31 (Gate rows), 47–48 (S888/S892 window sentence), 55 (Gate note 3), 57–61 (Gate note 4, byte instability).
- `reports/round-75/evidence/S885.txt` @ base lines 5–6 (`bytes: 109588`, `sha256: 20b571d7…`); `S887.txt` lines 5–6 (`116878`, `e0560649…`); `S888.txt` line 13 (`chars=4096 … before=3266`); `S892.txt` line 13 (`chars=4097 … before=2020`).
- `.ufo/waves/round-75/counters/probe-receipts/S885.txt` @ base lines 5–6 (`bytes: 111486`, `sha256: 2bcdd019…`); `S887.txt` lines 5–6 (`118776`, `fbf48ad2…`).
- `reports/round-75/telemetry/selftest-c.txt` @ base lines 2–3 and 88 (`# counter sha256 fa5060b91bdb…`; `78 mutants over 13/13 legs`; `SELFTEST: 85/85`).
- `.ufo/waves/round-75/w3/ExecRerunBoth.md` line 137 (`accept-c.py --selftest → SELFTEST: 85/85` at the frozen blob) and `.ufo/waves/round-75/w3/RevReadmeSkillQuality.md` line 27 (receipt pins the pre-freeze hash; rerun at landed bytes = 85/85).
- `.ufo/waves/round-76/w1/drafts/repairs.diff` @ `df0f030` (the w1 proposed SKILL.md:707 wording).
- `reports/round-76/telemetry/measures-ca.txt` @ `af67443` (L1's Ca measurement at HEAD; cites the same LEDGER/REPAIR/ANNOTATE/NOSTUB/SEPARABLE reasons). NOTE: this file post-dates the cited C landing `722e69f`; it is corroboration of the L1's run, not a file at the cited revisions.

## Method / limitations

- Read-only throughout. All files read via `git show <rev>:<path>` at the cited revisions (or `git ls-tree`/`git grep` at those revisions); the mutable worktree was used only to locate the frozen `accept-ca.py` source and to clone `98c486b` and `a43ed80` into scratch for replay.
- Leg replay was done by importing the **frozen** `reports/round-76/accept-ca.py` @ `df0f030` and calling its own `leg_ledger` / `leg_repair` / `leg_annotate` / `leg_nostub` / `leg_separable` / `observed_token` / `statement_after` against scratch clones of base and Ca-lands, with the frozen `claims.json`/`ledger.json` as config. No counter was run end-to-end; no receipt was produced or altered; no lane file was written.
- Scratch used: `/fast/scratch/hyaku/kotodama-r76/ExecScorecardConsistency` (clones + extracted blobs) — **removed before this report was filed**.
- **Tooling: none installed, none upgraded** (no pacman transaction, no uv/npm/cargo install). Everything above used the preinstalled `git` and `python3` only. Nothing in this seat changed the toolchain, so there is no tool/version/channel to report; the host `RULES.md` was read and no install was required for a read-only falsification.

## Recommended next-round items (claims/ledger are frozen — nothing here is editable in round 76)

1. **Re-freeze the three ledger `rederive` strings** (L76-19/20/21) as `shlex.join(observe_cmd)` — the pattern must keep its single quotes — and keep the SCORECARD cells byte-identical to them.
2. **Re-freeze L76-19's `stated_text`** to a contiguous base string, e.g. the exact line-47/48 wording (`…and S892's\n   (`chars=4097 before=284`)…`), or point `stated_at` at the line that literally carries `before=284`.
3. **Re-freeze L76-16's `statement_after.parse`** to a grammar the landed SKILL.md sentence satisfies (accept `committed counter <path> sha256 `<12hex>…`` — path-tolerant and ellipsis-tolerant), or re-word `SKILL.md:707` to `committed counter sha256 `315c5f3f27fd`` with no path and no ellipsis. Either one alone closes REPAIR; the current pair cannot both.
4. **Move or re-classify L76-13** so its `stated_at` is inside the frozen append-only allowlist (the knowledge path can never be ANNOTATE-graded), and update the SCORECARD prose to name the SEPARABLE consequence as well as the LEDGER one.
5. **Re-point the SKILL.md:707 `85/85` citation** to a receipt stamped `315c5f3f27fd…`, or drop the receipt parenthetical and cite the w3 rerun narrative explicitly.
