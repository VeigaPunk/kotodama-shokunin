- Seat: A08 | executor | claim A | date 2026-10-19 | baseline 139e3b6

# Round-33 language audit — promotion / canon / closure / verified-without-verifier

## Verdict

**Clean at the frozen snapshot.** Zero un-negated, un-routed, uncited promotion /
canon / closure / verification claims in the 57/64 seat fragments present at
**2026-10-19T04:06:54Z**. Every one of the 2371 pass-1 term occurrences is a **negation**
(943), a **routed reference** (129), a **mention** (1190),
or a **cited result** (100). The 9 residual rows — 9 pass-1, 1 pass-2, one
row in both — are adjudicated individually below; all are evidence-introducing frames or an
ordinary-sense adjective. **0 genuine violations.**

This is a **partial scan by construction**: 7 seat out-paths had not landed at the snapshot
(named under Owed), and fragments were being revised while the scan ran. The verdict binds
the digests in the manifest below, not the final wave.

## Scope and method

Two passes over every `.md/.json/.txt/.py/.yml` file under `reports/round-33/`:

- **Pass 1 (broad)** — every occurrence of five term families: `promot*`, `canon*`,
  `clos(e|es|ed|ing|ure)`, `clear(ance|ed)`/`bless*`, and the verdict verbs
  `verified|verifies|verification|confirmed|attested|certified|green|passed|passes`.
- **Pass 2 (strict)** — only affirmative verdict *frames*: `S1` term+approval-verb within
  one clause, `S2` copula+verdict ("is/are now closed"), `S3` checklist-complete.
  Pass 2 is the headline set; pass 1 is the coverage set the mission's "all round-33
  fragments" wording asks for.

Each occurrence is classified in precedence order:

| class | meaning |
|---|---|
| `MENTION-EXEMPT` | names the term, does not claim it: inside a fenced code block, inside a path, inside a backticked path/command, on a grep-invocation or term-count line, repo lifecycle vocabulary (`closing snapshot`, `closure ledger`), a heading naming a section, or an explicit mention of the word itself |
| `NEGATION` | a negation token in the paragraph (`no promotion`, `not canonized`, `grants no`, `to-verify`, `owed`) |
| `ROUTED-REFERENCE` | a decision-owner token in the paragraph (`operator`, `lore-shokunin`, a seat ID as subject or after `by`/`per`/`from`, `routed`, `integrator`, `non-author`) |
| `CITED-RESULT` | a verdict word grounded by an in-paragraph citation (`file:line`, backticked path/command, commit hash) |
| `UNSUPPORTED-CLAIM` | verdict language with no negation, no routed owner and no citation — the **verified-without-verifier** shape |

The context window is the enclosing blank-line-delimited paragraph (falling back to a fixed
span above 700 chars), so a negation anywhere in the same bullet covers the term.

**Self-consistency.** This fragment contains every search term as literal text (the scanner
source is embedded below). Run against itself it yields **0 `UNSUPPORTED-CLAIM` rows in both
passes** — the fenced-code exemption is what makes that hold, and it is the same principle
as the backtick rule: a literal in program text is a mention, not a claim.

### Known residual class (stated, not hidden)

The scanner is lexical, so it cannot see that a cited block follows a colon. All 9 residual
rows share one shape — **`<verdict word> …:` introducing a fenced command block or table
that carries the citation**, or a reviewer naming its own method immediately before the
evidence — plus one ordinary-sense adjective ("canonical table"). A future
`UNSUPPORTED-CLAIM` row therefore **requires the same one-line adjudication; it is not by
itself a violation**. This precision ceiling is recorded rather than papered over.

## Counting commands and results

All run from the repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```bash
python3 -B .scratch/a08/langscan.py --selftest   # exit 0, selftest 17/17
python3 -B .scratch/a08/langscan.py              # headline + unsupported rows
python3 -B .scratch/a08/langscan.py --json       # full machine output
python3 -B .scratch/a08/langscan.py --strict     # pass-2 rows only
```

Scanner `langscan.py` sha256 `73296aa4efbfebd714d88a918471df011d8ff8d715d442ce0c9a664069a67434`. The source is embedded below so the integrator
can restore it verbatim and re-run: this seat's write scope is `adj/A08-language.md` only,
so the tool is filed inline rather than as a sidecar `.py`. Verified: extracting the fenced
`python` block from this filed file and diffing it against the tested original returns
**identical**, and the extracted copy's selftest passes **17/17**.

## Class totals at the frozen snapshot

| pass | total | MENTION-EXEMPT | NEGATION | ROUTED-REFERENCE | CITED-RESULT | UNSUPPORTED-CLAIM |
|---|---|---|---|---|---|---|
| pass 1 (broad) | 2371 | 1190 | 943 | 129 | 100 | 9 |
| pass 2 (strict) | 245 | 174 | 62 | 5 | 3 | 1 |

Coverage: **57/64 seat out-paths present** — 60 files scanned, 57 of
64 declared seat out-paths present (`targets.json` `seats[].out`).

## Residual adjudication (all 9, hand-read)

| # | row | which pass | adjudication |
|---|---|---|---|
| 1 | `reports/round-33/op/O05-falsifier-disposition.md:58` `verified` | pass 1 | evidence-introducing frame: the two facts follow as items 1./2. with their own citations (`corpus/lessons/round-32.md:41`, `reports/round-19/telemetry/availability-close-19.json:5`) |
| 2 | `reports/round-33/op/O08-receipt.md:182` `passed` | pass 1 | evidence-introducing frame: the variant table with observed outputs and exit codes follows |
| 3 | `reports/round-33/review/R01-op-review.md:8` `green` | pass 1 | reviewer states its own method ("I re-ran every command the fragments cite that can be re-run and independently re-measured every pin"); the per-fragment verdicts that follow carry their evidence |
| 4 | `reports/round-33/review/R01-op-review.md:24` `verified` | pass 1 | states the reviewer's own re-verification method ("verified by re-grepping the sp…") |
| 5 | `reports/round-33/review/R03-op-review.md:109` `green` | pass 1 | evidence-introducing frame: the fenced PASS block with payload-equality assertions follows |
| 6 | `reports/round-33/review/R03-op-review.md:138` `verified` | pass 1 | evidence-introducing frame (and the only pass-2 residual): the bulleted citations (`P01:217`, `c31-lessons-index-audit.py:158`) and the measured resolver output follow |
| 7 | `reports/round-33/review/R03-op-review.md:191` `verified` | pass 1 | states the reviewer's own method ("I verified it independently rather than reading its receipt"); the control-by-control evidence follows |
| 8 | `reports/round-33/review/R04-calib-review.md:95` `canonical` | pass 1 | ordinary adjective sense: "K03's canonical table" = the authoritative enumeration table, not a canon-standing claim (A12 records the same reading, `adj/A12-verify-a04-a06.md:49`) |
| 9 | `reports/round-33/review/R06-calib-review.md:277` `Verified` | pass 1 | evidence-introducing frame: the fenced PASS / exit-code block follows |

**9 residuals, 9 adjudicated, 0 genuine violations.** Note that row 6 is the only pass-2
residual and it is the same line as pass-1 row 6 — the two passes agree on the one
borderline line, which is the expected behaviour.

## Strict-pass output (all rows, as filed)

```
reports/round-33/adj/A02-handoff.md:61	S1	NEGATION	canonized`/`not yet canonized
reports/round-33/adj/A02-handoff.md:82	S1	NEGATION	canonized` + `handoff_status: prepared-not-accepted
reports/round-33/adj/A02-handoff.md:116	S1	MENTION-EXEMPT	round-22/fixes/regression-completed
reports/round-33/adj/A02-handoff.md:161	S1	MENTION-EXEMPT	round-22/fixes/regression-completed
reports/round-33/adj/A02-handoff.md:142	S2	NEGATION	are verified
reports/round-33/adj/A04-bleed.md:113	S1	NEGATION	closure is re-verified
reports/round-33/adj/A05-corpus.md:53	S1	NEGATION	canon: not canonized
reports/round-33/adj/A05-corpus.md:54	S1	NEGATION	canon, not a world-bible entry, and not accepted
reports/round-33/adj/A05-corpus.md:54	S1	NEGATION	CANON`, `handoff_status: prepared-not-accepted
reports/round-33/adj/A05-corpus.md:55	S1	NEGATION	CANON**: not canon, not a world-bible entry, not accepted
reports/round-33/adj/A05-corpus.md:55	S1	NEGATION	canon design drill … not an [accepted
reports/round-33/adj/A05-corpus.md:206	S1	NEGATION	item is closed
reports/round-33/adj/A05-corpus.md:243	S1	MENTION-EXEMPT	CANON-canon-status-promoted
reports/round-33/adj/A05-corpus.md:206	S2	NEGATION	is closed
reports/round-33/adj/A06-contested.md:23	S1	NEGATION	item are restated below with pointers re-verified
reports/round-33/adj/A06-contested.md:31	S1	NEGATION	item | current status | current pointers (re-verified
reports/round-33/adj/A08-language.md:3	S1	MENTION-EXEMPT	Round-33 language audit — promotion / canon / closure / verified
reports/round-33/adj/A08-language.md:36	S1	NEGATION	promotion`, `not canonized
reports/round-33/adj/A08-language.md:89	S1	NEGATION	CLAIM (pass 1) | states the reviewer's own method ("I verified
reports/round-33/adj/A08-language.md:99	S1	MENTION-EXEMPT	canonized`/`not yet canonized
reports/round-33/adj/A08-language.md:100	S1	MENTION-EXEMPT	canonized` + `handoff_status: prepared-not-accepted
reports/round-33/adj/A08-language.md:101	S1	MENTION-EXEMPT	round-22/fixes/regression-completed
reports/round-33/adj/A08-language.md:102	S1	MENTION-EXEMPT	round-22/fixes/regression-completed
reports/round-33/adj/A08-language.md:104	S1	MENTION-EXEMPT	closure is re-verified
reports/round-33/adj/A08-language.md:105	S1	MENTION-EXEMPT	canon: not canonized
reports/round-33/adj/A08-language.md:106	S1	MENTION-EXEMPT	canon, not a world-bible entry, and not accepted
reports/round-33/adj/A08-language.md:107	S1	MENTION-EXEMPT	CANON`, `handoff_status: prepared-not-accepted
reports/round-33/adj/A08-language.md:108	S1	MENTION-EXEMPT	CANON**: not canon, not a world-bible entry, not accepted
reports/round-33/adj/A08-language.md:109	S1	MENTION-EXEMPT	canon design drill … not an [accepted
reports/round-33/adj/A08-language.md:110	S1	MENTION-EXEMPT	item is closed
reports/round-33/adj/A08-language.md:111	S1	MENTION-EXEMPT	CANON-canon-status-promoted
reports/round-33/adj/A08-language.md:113	S1	MENTION-EXEMPT	item are restated below with pointers re-verified
reports/round-33/adj/A08-language.md:114	S1	MENTION-EXEMPT	item | current status | current pointers (re-verified
reports/round-33/adj/A08-language.md:115	S1	MENTION-EXEMPT	item is closed
reports/round-33/adj/A08-language.md:116	S1	MENTION-EXEMPT	SHONEN box-condition states quoting the filed r24 verdict `verified
reports/round-33/adj/A08-language.md:117	S1	MENTION-EXEMPT	canon` 16 / `clearance` 6 / `closure` 13 / `certif` 0 / `verified
reports/round-33/adj/A08-language.md:118	S1	MENTION-EXEMPT	canon": "not canonized
reports/round-33/adj/A08-language.md:120	S1	MENTION-EXEMPT	CANON|not canonized
reports/round-33/adj/A08-language.md:122	S1	MENTION-EXEMPT	canon": "not canonized
reports/round-33/adj/A08-language.md:123	S1	MENTION-EXEMPT	box-1 inventory re-verified
reports/round-33/adj/A08-language.md:124	S1	MENTION-EXEMPT	claim's "pre-round-8" phrasing understated | — | **closed
reports/round-33/adj/A08-language.md:125	S1	MENTION-EXEMPT	canon` vs `canoniz`, `verified
reports/round-33/adj/A08-language.md:126	S1	MENTION-EXEMPT	round-22/fixes/regression-completed
reports/round-33/adj/A08-language.md:127	S1	MENTION-EXEMPT	canon|clearance|closure|verified
reports/round-33/adj/A08-language.md:128	S1	MENTION-EXEMPT	closure is re-verified
reports/round-33/adj/A08-language.md:129	S1	MENTION-EXEMPT	promotion (approved
reports/round-33/adj/A08-language.md:130	S1	MENTION-EXEMPT	canon(ized|ical)? (approved
reports/round-33/adj/A08-language.md:131	S1	MENTION-EXEMPT	Box 2 (end-to-end): verified
reports/round-33/adj/A08-language.md:132	S1	MENTION-EXEMPT	Box 3 (cold run): verified
reports/round-33/adj/A08-language.md:133	S1	MENTION-EXEMPT	promotion (approved
reports/round-33/adj/A08-language.md:134	S1	MENTION-EXEMPT	canon(ized|ical)? (approved
reports/round-33/adj/A08-language.md:135	S1	MENTION-EXEMPT	clearance\|closure\|verified
reports/round-33/adj/A08-language.md:136	S1	MENTION-EXEMPT	round-17: C/O verified
reports/round-33/adj/A08-language.md:137	S1	MENTION-EXEMPT	item lands first on a closed
reports/round-33/adj/A08-language.md:138	S1	MENTION-EXEMPT	item is not "closed
reports/round-33/adj/A08-language.md:142	S1	MENTION-EXEMPT	item is not closed
reports/round-33/adj/A08-language.md:143	S1	MENTION-EXEMPT	round-18`, `passed
reports/round-33/adj/A08-language.md:144	S1	MENTION-EXEMPT	round-18, `exit_code:1`, `expect_exit:1`, `passed
reports/round-33/adj/A08-language.md:145	S1	MENTION-EXEMPT	item | on record since | status-quo pointer, re-verified
reports/round-33/adj/A08-language.md:146	S1	MENTION-EXEMPT	item | origin round | class | pointer (re-verified
reports/round-33/adj/A08-language.md:147	S1	MENTION-EXEMPT	box-1 condition 1 (inventory)** — closed
reports/round-33/adj/A08-language.md:148	S1	MENTION-EXEMPT	box 3: N3/N6 closed
reports/round-33/adj/A08-language.md:149	S1	MENTION-EXEMPT	round-33/**` for `promot|canon|clearance|closure|verified
reports/round-33/adj/A08-language.md:150	S1	MENTION-EXEMPT	round-32 dossier's "inventory condition CLOSED
reports/round-33/adj/A08-language.md:152	S1	MENTION-EXEMPT	item missed its verified
reports/round-33/adj/A08-language.md:153	S1	MENTION-EXEMPT	round report that reads as if seats verified
reports/round-33/adj/A08-language.md:154	S1	MENTION-EXEMPT	round for a round admitted
reports/round-33/adj/A08-language.md:155	S1	MENTION-EXEMPT	round for a round admitted
reports/round-33/adj/A08-language.md:157	S1	MENTION-EXEMPT	round-30 are the **round-16 outlier shape**: `source:` + `verified
reports/round-33/adj/A08-language.md:158	S1	MENTION-EXEMPT	round-30's Q-30-5 should appear as *carried* or *closed
reports/round-33/adj/A08-language.md:160	S1	MENTION-EXEMPT	promotion\|canon\|clearance\|closed
reports/round-33/adj/A08-language.md:163	S1	MENTION-EXEMPT	Round 16 is the outlier: `source:`, `verified
reports/round-33/adj/A08-language.md:164	S1	MENTION-EXEMPT	Round 16 is the outlier: `source:`, `verified
reports/round-33/adj/A08-language.md:165	S1	MENTION-EXEMPT	round 28 — the vocabulary leg landed and `L6b-HOLD` was closed
reports/round-33/adj/A08-language.md:166	S1	MENTION-EXEMPT	round-30 repair must not be described as complete
reports/round-33/adj/A08-language.md:171	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/adj/A08-language.md:172	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/adj/A08-language.md:176	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/adj/A08-language.md:177	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/adj/A08-language.md:178	S1	MENTION-EXEMPT	claim O to verified
reports/round-33/adj/A08-language.md:185	S1	MENTION-EXEMPT	round-32 dossier binds box 1's **closed
reports/round-33/adj/A08-language.md:187	S1	MENTION-EXEMPT	item this review was prepared to owe is closed
reports/round-33/adj/A08-language.md:188	S1	MENTION-EXEMPT	CLAIM	now verified
reports/round-33/adj/A08-language.md:190	S1	MENTION-EXEMPT	round-2[7-9]/ reports/round-3[0-1]/ \| wc -l` → `0` | **VERIFIED
reports/round-33/adj/A08-language.md:191	S1	MENTION-EXEMPT	box may read as cleared
reports/round-33/adj/A08-language.md:192	S1	MENTION-EXEMPT	Claim C requires "status-quo pointer re-verified
reports/round-33/adj/A08-language.md:193	S1	MENTION-EXEMPT	promotion\|promoted
reports/round-33/adj/A08-language.md:196	S1	MENTION-EXEMPT	Claim O is not yet verified
reports/round-33/adj/A08-language.md:197	S1	MENTION-EXEMPT	item (K03) | class | status quo re-verified
reports/round-33/adj/A08-language.md:198	S1	MENTION-EXEMPT	claim A: it records what is verified
reports/round-33/adj/A08-language.md:200	S1	MENTION-EXEMPT	box 1 (decision tables/errors/checklists/sources): r24 verified
reports/round-33/adj/A08-language.md:201	S1	MENTION-EXEMPT	box 2 (end-to-end domain task): verified
reports/round-33/adj/A08-language.md:202	S1	MENTION-EXEMPT	box 3 (cold-run executability): verified
reports/round-33/adj/A08-language.md:203	S1	MENTION-EXEMPT	box 4 (no bleed / PROVINCE accurate): verified
reports/round-33/adj/A08-language.md:204	S1	MENTION-EXEMPT	round is not admitted
reports/round-33/adj/A08-language.md:205	S1	MENTION-EXEMPT	box-1 inventory closed
reports/round-33/adj/A08-language.md:206	S1	MENTION-EXEMPT	round is not admitted
reports/round-33/adj/A08-language.md:207	S1	MENTION-EXEMPT	round-33 fragments for promotion/canon/closure/verified
reports/round-33/adj/A08-language.md:281	S1	MENTION-EXEMPT	canon` 16, `clearance` 6, `closure` 13, `verified
reports/round-33/adj/A08-language.md:283	S1	MENTION-EXEMPT	canon|clearance|closure|verified
reports/round-33/adj/A08-language.md:287	S1	NEGATION	promotion (approved
reports/round-33/adj/A08-language.md:287	S1	NEGATION	canon(ized|ical)? (approved
reports/round-33/adj/A08-language.md:338	S1	MENTION-EXEMPT	promotion/canon/closure/verified
reports/round-33/adj/A08-language.md:394	S1	MENTION-EXEMPT	promoted|accepted
reports/round-33/adj/A08-language.md:397	S1	MENTION-EXEMPT	canonical|promoted
reports/round-33/adj/A08-language.md:408	S1	MENTION-EXEMPT	canon|un-?cleared
reports/round-33/adj/A08-language.md:439	S1	MENTION-EXEMPT	box 1 condition is now closed
reports/round-33/adj/A08-language.md:441	S1	MENTION-EXEMPT	item is closed
reports/round-33/adj/A08-language.md:448	S1	MENTION-EXEMPT	box 1 condition is now closed
reports/round-33/adj/A08-language.md:27	S2	MENTION-EXEMPT	are now closed
reports/round-33/adj/A08-language.md:92	S2	NEGATION	now verified
reports/round-33/adj/A08-language.md:103	S2	MENTION-EXEMPT	are verified
reports/round-33/adj/A08-language.md:110	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:112	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:115	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:119	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:121	S2	MENTION-EXEMPT	was verified
reports/round-33/adj/A08-language.md:139	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:140	S2	MENTION-EXEMPT	is canonical
reports/round-33/adj/A08-language.md:141	S2	MENTION-EXEMPT	is canonical
reports/round-33/adj/A08-language.md:151	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:156	S2	MENTION-EXEMPT	IS closed
reports/round-33/adj/A08-language.md:159	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:161	S2	MENTION-EXEMPT	is
  admitted
reports/round-33/adj/A08-language.md:165	S2	MENTION-EXEMPT	was closed
reports/round-33/adj/A08-language.md:167	S2	MENTION-EXEMPT	was closed
reports/round-33/adj/A08-language.md:168	S2	MENTION-EXEMPT	were closed
reports/round-33/adj/A08-language.md:169	S2	MENTION-EXEMPT	were closed
reports/round-33/adj/A08-language.md:170	S2	MENTION-EXEMPT	is verified
reports/round-33/adj/A08-language.md:171	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:172	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:173	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:174	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:175	S2	MENTION-EXEMPT	is cleared
reports/round-33/adj/A08-language.md:176	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:177	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:179	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:180	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:181	S2	MENTION-EXEMPT	IS closed
reports/round-33/adj/A08-language.md:182	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:183	S2	MENTION-EXEMPT	is accepted
reports/round-33/adj/A08-language.md:184	S2	MENTION-EXEMPT	are closed
reports/round-33/adj/A08-language.md:186	S2	MENTION-EXEMPT	is cleared
reports/round-33/adj/A08-language.md:187	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:188	S2	MENTION-EXEMPT	now verified
reports/round-33/adj/A08-language.md:189	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:194	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:195	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:198	S2	MENTION-EXEMPT	is verified
reports/round-33/adj/A08-language.md:199	S2	MENTION-EXEMPT	is verified
reports/round-33/adj/A08-language.md:439	S2	MENTION-EXEMPT	is now closed
reports/round-33/adj/A08-language.md:441	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A08-language.md:447	S2	MENTION-EXEMPT	is verified
reports/round-33/adj/A08-language.md:448	S2	MENTION-EXEMPT	is now closed
reports/round-33/adj/A08-language.md:449	S3	MENTION-EXEMPT	All four boxes pass
reports/round-33/adj/A10-receipt.md:53	S1	MENTION-EXEMPT	item is closed
reports/round-33/adj/A10-receipt.md:56	S1	NEGATION	SHONEN box-condition states quoting the filed r24 verdict `verified
reports/round-33/adj/A10-receipt.md:56	S1	MENTION-EXEMPT	canon` 16 / `clearance` 6 / `closure` 13 / `certif` 0 / `verified
reports/round-33/adj/A10-receipt.md:73	S1	NEGATION	canon": "not canonized
reports/round-33/adj/A10-receipt.md:53	S2	MENTION-EXEMPT	is closed
reports/round-33/adj/A12-verify-a04-a06.md:91	S1	MENTION-EXEMPT	round receipts rewritten in place during round 33 (breach closed
reports/round-33/adj/A12-verify-a04-a06.md:191	S1	MENTION-EXEMPT	CANON|not canonized
reports/round-33/adj/A12-verify-a04-a06.md:140	S2	NEGATION	is now closed
reports/round-33/adj/A13-verify-a07-a09.md:183	S1	MENTION-EXEMPT	canon": "not canonized
reports/round-33/adj/A15-audit-draft.md:138	S1	ROUTED-REFERENCE	box-1 inventory re-verified
reports/round-33/adj/A15-audit-draft.md:176	S1	NEGATION	claim's "pre-round-8" phrasing understated | — | **closed
reports/round-33/adj/A15-audit-draft.md:315	S1	MENTION-EXEMPT	canon|clearance|closure|verified
reports/round-33/adj/A16-shonen-material.md:29	S1	NEGATION	closure is re-verified
reports/round-33/adj/A16-shonen-material.md:138	S1	MENTION-EXEMPT	promotion (approved
reports/round-33/adj/A16-shonen-material.md:139	S1	NEGATION	canon(ized|ical)? (approved
reports/round-33/adj/A16-shonen-material.md:152	S1	NEGATION	Box 2 (end-to-end): verified
reports/round-33/adj/A16-shonen-material.md:154	S1	NEGATION	Box 3 (cold run): verified
reports/round-33/adj/A16-shonen-material.md:210	S1	MENTION-EXEMPT	promotion (approved
reports/round-33/adj/A16-shonen-material.md:210	S1	MENTION-EXEMPT	canon(ized|ical)? (approved
reports/round-33/adj/K04-method-scout.md:155	S1	MENTION-EXEMPT	clearance\|closure\|verified
reports/round-33/calib/C02-item-02.md:168	S1	MENTION-EXEMPT	round-17: C/O verified
reports/round-33/calib/C03-item-03.md:277	S1	NEGATION	item lands first on a closed
reports/round-33/calib/C03-item-03.md:289	S1	NEGATION	item is not "closed
reports/round-33/calib/C03-item-03.md:273	S2	ROUTED-REFERENCE	is closed
reports/round-33/calib/C03-item-03.md:294	S2	NEGATION	is canonical
reports/round-33/calib/C05-item-05.md:233	S2	NEGATION	is canonical
reports/round-33/calib/C08-item-08.md:164	S1	NEGATION	item is not closed
reports/round-33/calib/C12-item-12.md:71	S1	MENTION-EXEMPT	round-18`, `passed
reports/round-33/calib/C12-item-12.md:219	S1	ROUTED-REFERENCE	round-18, `exit_code:1`, `expect_exit:1`, `passed
reports/round-33/calib/C16-receipt.md:59	S1	NEGATION	item | on record since | status-quo pointer, re-verified
reports/round-33/calib/K03-open-items.md:60	S1	NEGATION	item | origin round | class | pointer (re-verified
reports/round-33/calib/K03-open-items.md:85	S1	NEGATION	box-1 condition 1 (inventory)** — closed
reports/round-33/calib/K03-open-items.md:120	S1	NEGATION	box 3: N3/N6 closed
reports/round-33/calib/P02-plan.md:224	S1	MENTION-EXEMPT	round-33/**` for `promot|canon|clearance|closure|verified
reports/round-33/cross/X00-connector.md:181	S1	CITED-RESULT	round-32 dossier's "inventory condition CLOSED
reports/round-33/cross/X00-connector.md:262	S2	NEGATION	is closed
reports/round-33/cross/X01-trades.md:294	S1	NEGATION	item missed its verified
reports/round-33/cross/X04-honesty.md:127	S1	NEGATION	round report that reads as if seats verified
reports/round-33/op/K01-falsifier-scout.md:23	S1	NEGATION	round for a round admitted
reports/round-33/op/K01-falsifier-scout.md:101	S1	NEGATION	round for a round admitted
reports/round-33/op/K01-falsifier-scout.md:23	S2	NEGATION	IS closed
reports/round-33/op/K02-lessons-census.md:121	S1	NEGATION	round-30 are the **round-16 outlier shape**: `source:` + `verified
reports/round-33/op/K02-lessons-census.md:238	S1	NEGATION	round-30's Q-30-5 should appear as *carried* or *closed
reports/round-33/op/K02-lessons-census.md:138	S2	ROUTED-REFERENCE	are closed
reports/round-33/op/O01-row-drafts.md:224	S1	MENTION-EXEMPT	promotion\|canon\|clearance\|closed
reports/round-33/op/O01-row-drafts.md:134	S2	NEGATION	is
  admitted
reports/round-33/op/O02-readme-delta.md:220	S1	MENTION-EXEMPT	Round 16 is the outlier: `source:`, `verified
reports/round-33/op/O02-readme-delta.md:237	S1	MENTION-EXEMPT	Round 16 is the outlier: `source:`, `verified
reports/round-33/op/O02-readme-delta.md:261	S1	MENTION-EXEMPT	round 28 — the vocabulary leg landed and `L6b-HOLD` was closed
reports/round-33/op/O02-readme-delta.md:275	S1	MENTION-EXEMPT	round-30 repair must not be described as complete
reports/round-33/op/O02-readme-delta.md:261	S2	MENTION-EXEMPT	was closed
reports/round-33/op/O02-readme-delta.md:320	S2	MENTION-EXEMPT	were closed
reports/round-33/op/O02-readme-delta.md:332	S2	MENTION-EXEMPT	were closed
reports/round-33/op/O03-owner-checks.md:15	S2	NEGATION	is verified
reports/round-33/op/O05-falsifier-disposition.md:83	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/op/O05-falsifier-disposition.md:92	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/op/O05-falsifier-disposition.md:83	S2	MENTION-EXEMPT	are closed
reports/round-33/op/O05-falsifier-disposition.md:92	S2	MENTION-EXEMPT	are closed
reports/round-33/op/O05-falsifier-disposition.md:134	S2	NEGATION	is cleared
reports/round-33/op/O08-receipt.md:237	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/op/O08-receipt.md:244	S1	MENTION-EXEMPT	round's records are closed
reports/round-33/op/O08-receipt.md:306	S1	NEGATION	claim O to verified
reports/round-33/op/O08-receipt.md:237	S2	MENTION-EXEMPT	are closed
reports/round-33/op/O08-receipt.md:244	S2	MENTION-EXEMPT	are closed
reports/round-33/op/P01-plan.md:272	S2	NEGATION	IS closed
reports/round-33/op/P01-plan.md:293	S2	NEGATION	are closed
reports/round-33/review/R01-op-review.md:53	S2	NEGATION	is accepted
reports/round-33/review/R01-op-review.md:298	S2	CITED-RESULT	are closed
reports/round-33/review/R02-op-review.md:396	S1	NEGATION	round-32 dossier binds box 1's **closed
reports/round-33/review/R02-op-review.md:382	S2	NEGATION	is cleared
reports/round-33/review/R03-op-review.md:138	S2	UNSUPPORTED-CLAIM	now verified
reports/round-33/review/R04-calib-review.md:37	S1	MENTION-EXEMPT	round-2[7-9]/ reports/round-3[0-1]/ \| wc -l` → `0` | **VERIFIED
reports/round-33/review/R04-calib-review.md:289	S1	NEGATION	box may read as cleared
reports/round-33/review/R05-calib-review.md:81	S1	CITED-RESULT	Claim C requires "status-quo pointer re-verified
reports/round-33/review/R07-adj-review.md:309	S1	MENTION-EXEMPT	promotion\|promoted
reports/round-33/review/R07-adj-review.md:134	S2	NEGATION	is closed
reports/round-33/review/R07-adj-review.md:173	S2	NEGATION	is closed
reports/round-33/scribe/S01-op-receipt.md:7	S1	NEGATION	Claim O is not yet verified
reports/round-33/scribe/S01-op-receipt.md:492	S1	NEGATION	claim-O verdict is therefore **not verified
reports/round-33/scribe/S02-calib-receipt.md:65	S1	NEGATION	item (K03) | class | status quo re-verified
reports/round-33/scribe/S03-adj-receipt.md:6	S1	NEGATION	claim A: it records what is verified
reports/round-33/scribe/S03-adj-receipt.md:6	S2	NEGATION	is verified
reports/round-33/scribe/S04-integration-draft.md:116	S1	MENTION-EXEMPT	box 1 (decision tables/errors/checklists/sources): r24 verified
reports/round-33/scribe/S04-integration-draft.md:120	S1	MENTION-EXEMPT	box 2 (end-to-end domain task): verified
reports/round-33/scribe/S04-integration-draft.md:123	S1	MENTION-EXEMPT	box 3 (cold-run executability): verified
reports/round-33/scribe/S04-integration-draft.md:125	S1	MENTION-EXEMPT	box 4 (no bleed / PROVINCE accurate): verified
reports/round-33/scribe/S04-integration-draft.md:182	S1	NEGATION	round is not admitted
reports/round-33/scribe/S04-integration-draft.md:587	S1	ROUTED-REFERENCE	box-1 inventory closed
reports/round-33/scribe/S05-telemetry-draft.md:180	S1	NEGATION	round is not admitted
reports/round-33/targets.json:55	S1	MENTION-EXEMPT	round-33 fragments for promotion/canon/closure/verified
```

## Per-file digest manifest (the scan's frozen input set)

| sha256 (first 16) | bytes | lines | pass1 | p1 unsup | pass2 | p2 unsup | path |
|---|---|---|---|---|---|---|---|
| `e22f2d03ce5b59d3` | 13684 | 199 | 20 | 0 | 0 | 0 | `reports/round-33/adj/A01-province.md` |
| `41c3a749418cc734` | 17040 | 182 | 42 | 0 | 5 | 0 | `reports/round-33/adj/A02-handoff.md` |
| `bf653d23891d5b30` | 16009 | 266 | 3 | 0 | 0 | 0 | `reports/round-33/adj/A03-scope.md` |
| `c7156e55f365e185` | 14219 | 225 | 44 | 0 | 1 | 0 | `reports/round-33/adj/A04-bleed.md` |
| `a1d8a25573a36cb0` | 22349 | 281 | 103 | 0 | 8 | 0 | `reports/round-33/adj/A05-corpus.md` |
| `21b6099f49ea2080` | 22536 | 271 | 53 | 0 | 2 | 0 | `reports/round-33/adj/A06-contested.md` |
| `dbf8deb3315b67ee` | 17513 | 112 | 16 | 0 | 0 | 0 | `reports/round-33/adj/A07-history.md` |
| `b42c16e6463fe781` | 39435 | 643 | 270 | 0 | 139 | 0 | `reports/round-33/adj/A08-language.md` |
| `98e3502e41a90d5b` | 24703 | 153 | 23 | 0 | 0 | 0 | `reports/round-33/adj/A09-pins.md` |
| `df5e42de84784e58` | 36683 | 139 | 47 | 0 | 5 | 0 | `reports/round-33/adj/A10-receipt.md` |
| `f52bf35406b8a3f2` | 17610 | 196 | 37 | 0 | 3 | 0 | `reports/round-33/adj/A12-verify-a04-a06.md` |
| `e6aca10f6b232af5` | 24390 | 346 | 55 | 0 | 1 | 0 | `reports/round-33/adj/A13-verify-a07-a09.md` |
| `96cfb870544c6081` | 29623 | 320 | 50 | 0 | 3 | 0 | `reports/round-33/adj/A15-audit-draft.md` |
| `e90b867983712fad` | 14725 | 218 | 52 | 0 | 7 | 0 | `reports/round-33/adj/A16-shonen-material.md` |
| `45485a5304bd4850` | 21738 | 288 | 28 | 0 | 1 | 0 | `reports/round-33/adj/K04-method-scout.md` |
| `fe8ad11d3f47c5b7` | 23416 | 327 | 58 | 0 | 0 | 0 | `reports/round-33/calib/C01-item-01.md` |
| `488fee7e3748f77e` | 19671 | 326 | 26 | 0 | 1 | 0 | `reports/round-33/calib/C02-item-02.md` |
| `680bdcdf75ed9e3a` | 23420 | 357 | 29 | 0 | 4 | 0 | `reports/round-33/calib/C03-item-03.md` |
| `313b3f95e321cd27` | 24236 | 419 | 32 | 0 | 0 | 0 | `reports/round-33/calib/C04-item-04.md` |
| `dd2612b6defd2923` | 31829 | 500 | 38 | 0 | 1 | 0 | `reports/round-33/calib/C05-item-05.md` |
| `06faa91acf1a0eb4` | 15969 | 275 | 22 | 0 | 0 | 0 | `reports/round-33/calib/C06-item-06.md` |
| `48169a6c292fb60a` | 12994 | 237 | 22 | 0 | 0 | 0 | `reports/round-33/calib/C07-item-07.md` |
| `d0a8eec20363a6fd` | 16127 | 229 | 11 | 0 | 1 | 0 | `reports/round-33/calib/C08-item-08.md` |
| `f18f80f7ace9ca81` | 21563 | 323 | 21 | 0 | 0 | 0 | `reports/round-33/calib/C11-item-11.md` |
| `7e081c318c16ea2f` | 13833 | 224 | 22 | 0 | 2 | 0 | `reports/round-33/calib/C12-item-12.md` |
| `e6711f239ba34b38` | 35482 | 578 | 33 | 0 | 0 | 0 | `reports/round-33/calib/C14-fix-drafts.md` |
| `fd96f9548de99e98` | 14840 | 171 | 37 | 0 | 1 | 0 | `reports/round-33/calib/C16-receipt.md` |
| `fe0b11cc869f96e6` | 11902 | 132 | 25 | 0 | 3 | 0 | `reports/round-33/calib/K03-open-items.md` |
| `42534c1fb445330a` | 25290 | 322 | 32 | 0 | 1 | 0 | `reports/round-33/calib/P02-plan.md` |
| `ba69090f90c00706` | 6991 | 73 | 21 | 0 | 0 | 0 | `reports/round-33/claims.json` |
| `b14fb3d0b0ac2ef1` | 24074 | 320 | 18 | 0 | 2 | 0 | `reports/round-33/cross/X00-connector.md` |
| `294c4cc5a33e5921` | 34607 | 482 | 60 | 0 | 1 | 0 | `reports/round-33/cross/X01-trades.md` |
| `06ba0d64570b9786` | 20852 | 287 | 37 | 0 | 0 | 0 | `reports/round-33/cross/X02-conformance.md` |
| `9303bde3cdee26be` | 18341 | 184 | 30 | 0 | 0 | 0 | `reports/round-33/cross/X03-protocol.md` |
| `fe5fbf8114824659` | 23683 | 321 | 39 | 0 | 1 | 0 | `reports/round-33/cross/X04-honesty.md` |
| `9d9dbe83b8b5ca38` | 10361 | 142 | 42 | 0 | 3 | 0 | `reports/round-33/op/K01-falsifier-scout.md` |
| `5d7f96a3f27fdad5` | 22144 | 286 | 20 | 0 | 3 | 0 | `reports/round-33/op/K02-lessons-census.md` |
| `f9e86e58bd70be00` | 14040 | 227 | 13 | 0 | 2 | 0 | `reports/round-33/op/O01-row-drafts.md` |
| `6ff4a626daff5e6d` | 41185 | 683 | 39 | 0 | 7 | 0 | `reports/round-33/op/O02-readme-delta.md` |
| `7db3554ea8096c33` | 17828 | 281 | 11 | 0 | 1 | 0 | `reports/round-33/op/O03-owner-checks.md` |
| `89ccee0cd934d5a6` | 13962 | 215 | 5 | 0 | 0 | 0 | `reports/round-33/op/O04-format-checks.md` |
| `6499d3b3fa8813e2` | 20935 | 278 | 88 | 1 | 5 | 0 | `reports/round-33/op/O05-falsifier-disposition.md` |
| `a4b847752f2deaa6` | 32915 | 720 | 14 | 0 | 0 | 0 | `reports/round-33/op/O06-controls.md` |
| `d2cb6b554d39a8ac` | 13355 | 206 | 5 | 0 | 0 | 0 | `reports/round-33/op/O07-baseline-receipt.md` |
| `2ebb25b29f17cf45` | 21179 | 363 | 30 | 1 | 5 | 0 | `reports/round-33/op/O08-receipt.md` |
| `058a29a158ae2a9f` | 29599 | 465 | 51 | 0 | 2 | 0 | `reports/round-33/op/P01-plan.md` |
| `1f64903cc9228c39` | 27158 | 385 | 30 | 2 | 2 | 0 | `reports/round-33/review/R01-op-review.md` |
| `e253ceda5854d35e` | 32879 | 487 | 33 | 0 | 2 | 0 | `reports/round-33/review/R02-op-review.md` |
| `a5ba4b4b30b465ca` | 27261 | 372 | 28 | 3 | 1 | 1 | `reports/round-33/review/R03-op-review.md` |
| `560dcfd293eded23` | 33007 | 453 | 56 | 1 | 2 | 0 | `reports/round-33/review/R04-calib-review.md` |
| `26e146495a045d17` | 26443 | 388 | 22 | 0 | 1 | 0 | `reports/round-33/review/R05-calib-review.md` |
| `55b66e9041acb828` | 38944 | 594 | 27 | 1 | 0 | 0 | `reports/round-33/review/R06-calib-review.md` |
| `a62116643c3d1a8b` | 27017 | 310 | 62 | 0 | 3 | 0 | `reports/round-33/review/R07-adj-review.md` |
| `0a423a077f74eccc` | 46140 | 563 | 65 | 0 | 2 | 0 | `reports/round-33/scribe/S01-op-receipt.md` |
| `181ce0dd535a3bdd` | 22375 | 307 | 36 | 0 | 1 | 0 | `reports/round-33/scribe/S02-calib-receipt.md` |
| `0cd5602b0beada4d` | 31511 | 307 | 56 | 0 | 2 | 0 | `reports/round-33/scribe/S03-adj-receipt.md` |
| `661dbecea2ee0620` | 38631 | 595 | 85 | 0 | 6 | 0 | `reports/round-33/scribe/S04-integration-draft.md` |
| `b5791952942540f0` | 33567 | 475 | 77 | 0 | 1 | 0 | `reports/round-33/scribe/S05-telemetry-draft.md` |
| `342c8f80eb857f96` | 18025 | 86 | 17 | 0 | 1 | 0 | `reports/round-33/targets.json` |
| `139b964ead124364` | 1500 | 30 | 3 | 0 | 0 | 0 | `reports/round-33/telemetry/dispatch-declared.json` |

## Cross-seat reconciliation

Three other seats ran ad-hoc variants of this check during the wave. Their readings differ
from this seat's in scope, not in verdict:

- **A13** (`adj/A13-verify-a07-a09.md:51-58`) scanned the 7 files present at 03:54:52Z and
  recorded "clean, zero un-negated verdict language", explicitly deferring the full scan:
  *"The full A08 scan must be re-run against the final fragment set — recorded under Owed."*
  Its term counts (`promot` 16, `canon` 16, `clearance` 6, `closure` 13, `verified` 21) are
  subsumed by this scan's larger file set.
- **A15** (`adj/A15-audit-draft.md:139-148`) ran `grep -rn -i -E "promot|canon|clearance|closure|verified"`
  at assembly time and pre-filled "zero unnegated hits" over `claims.json`+`targets.json` only,
  recording *"The audit's verdict is A08's."*
- **A16** (`adj/A16-shonen-material.md:139,210`) ran the narrowest pattern
  (`promotion (approved|granted)|canon(ized|ical)? (approved|cleared)|clearance|closure verdict`)
  over the two contract files and found negation-only hits.

All three agree with this seat's verdict; none covers the 57 landed fragments, which is this
seat's scope. A13's and A15's own narrow greps are themselves MENTION-EXEMPT here (they sit
inside fenced code blocks), which is why they do not appear as rows above.

## Owed

**Full-wave re-run.** The snapshot covers 57/64 seat out-paths. Seven had not
landed at the snapshot and every landed fragment may be revised again before integration.
The integrator must re-run the embedded scanner after the wave closes and re-adjudicate any
new `UNSUPPORTED-CLAIM` row with the one-line method above. Owed out-paths:

- `reports/round-33/calib/C09-item-09.md`
- `reports/round-33/calib/C10-item-10.md`
- `reports/round-33/calib/C13-consistency.md`
- `reports/round-33/calib/C15-ledger-draft.json`
- `reports/round-33/adj/A11-verify-a01-a03.md`
- `reports/round-33/adj/A14-verify-a10.md`
- `reports/round-33/review/R08-adj-review.md`

**Verification of this fragment.** No non-author seat has verified this fragment; its verdicts
are first-party. Marked `to-verify` pending an independent re-run by A11/A14 or R08.

## Citations

- `reports/round-33/targets.json:55` — A08 mission and out path; `:5-11` — shared rules
- `reports/round-33/claims.json:59` — the claim-A `after_required` clause this audit serves
- `reports/round-33/claims.json:68` — `non_goals`: "no promotion, canon, clearance, or closure verdicts (operator-owned)"
- `reports/round-32/run-validation.py:849-852` — the round-32 no-promotion regex precedent this audit generalizes
- `SCORECARD.md:293` — the `verified-with-conditions` / non-author-verifier precedent
- `reports/round-33/adj/A13-verify-a07-a09.md:51-58,73,76-77` — the deferred-to-A08 reading
- `reports/round-33/adj/A15-audit-draft.md:128,139-148` — the A12-attributed green and the pre-filled reading
- `reports/round-33/adj/A16-shonen-material.md:139,210` — the narrow-pattern reading
- `reports/round-33/adj/A12-verify-a04-a06.md:49` — the same ordinary-sense reading of "canonical"
- commands (all 2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `python3 -B .scratch/a08/langscan.py --selftest`; `python3 -B .scratch/a08/langscan.py`;
  `python3 -B .scratch/a08/langscan.py --json`; `python3 -B .scratch/a08/langscan.py --strict`;
  `git rev-parse HEAD`; `git ls-files | wc -l`; `git status --porcelain`
- frozen snapshot: `.scratch/a08/final.json` (scratch, not filed); scanner `.scratch/a08/langscan.py`

## Embedded scanner source (restore verbatim to re-run)

```python
#!/usr/bin/env python3
"""A08 language audit scanner — round 33 (regimen 2, loop 1).

Mission (reports/round-33/targets.json:55): "Language audit: grep all round-33
fragments for promotion/canon/closure/verified-without-verifier claims; every
hit must be a negation or a routed-reference; file the grep output."

Two passes over every file under reports/round-33/:

  Pass 1 (broad)    every occurrence of the five term families, classified
  Pass 2 (strict)   only affirmative verdict *frames* (term + approval verb in
                    one clause, or "is/are now <verdict>")

Classes, in precedence order:

  MENTION-EXEMPT       the occurrence names the term, it does not claim it:
                       inside a path, inside a backticked path/command, on a
                       grep-invocation / term-count line, or repo lifecycle
                       vocabulary ("closing snapshot", "closure ledger").
  NEGATION             a negation token in the window ("no promotion", ...)
  ROUTED-REFERENCE     a decision-owner token in the window (operator,
                       lore-shokunin, seat <ID>, routed, owed, ...)
  CITED-RESULT         a verdict word grounded by an in-window citation
                       (file:line, backticked path/command, commit hash)
  UNSUPPORTED-CLAIM    verdict language with no negation, no routed owner and
                       no citation -> the "verified-without-verifier" shape.
                       THIS is the headline number.

Usage:
  python3 -B .scratch/a08/langscan.py                 # scan reports/round-33
  python3 -B .scratch/a08/langscan.py --json          # machine output
  python3 -B .scratch/a08/langscan.py --strict        # pass-2 rows
  python3 -B .scratch/a08/langscan.py --findings      # UNSUPPORTED only
  python3 -B .scratch/a08/langscan.py --selftest      # fixtures, expect 17/17
"""
import argparse, hashlib, json, os, re, sys

ROOT = os.getcwd()
ROUND = os.path.join(ROOT, "reports", "round-33")
SUFFIXES = (".md", ".json", ".jsonl", ".txt", ".py", ".yml", ".yaml")
CONTRACT = ("reports/round-33/claims.json", "reports/round-33/targets.json")
CLASSES = ("MENTION-EXEMPT", "NEGATION", "ROUTED-REFERENCE", "CITED-RESULT",
           "UNSUPPORTED-CLAIM")

# --- pass 1: term families ---------------------------------------------
PATTERNS = [
    ("P1", "promotion", re.compile(r"(?i)\bpromot(?:e|es|ed|ing|ion)\b")),
    ("P2", "canon", re.compile(r"(?i)\bcanon(?:s|ical|ize|ized|ization)?\b")),
    ("P3", "closure", re.compile(r"(?i)\bclos(?:e|es|ed|ing|ure)\b")),
    ("P4", "clearance", re.compile(r"(?i)\bclear(?:ance|ed)\b|\bbless(?:es|ed|ing)?\b")),
    ("P5", "verdict-verbs", re.compile(r"(?i)\b(?:verified|verifies|verification|"
                                       r"confirmed|attested|certified|green|passed|passes)\b")),
]

# --- pass 2: affirmative verdict frames ---------------------------------
STRICT = [
    ("S1", "term+approval-verb", re.compile(
        r"(?i)\b(?:promot(?:ion|ed)|canon(?:ical|ized)?|clearance|closure|"
        r"shonen|round|item|box|claim|entry)\b[^.\n;]{0,60}?"
        r"\b(?:approved|granted|conferred|cleared|closed|complete[d]?|canonized|"
        r"promoted|accepted|admitted|passed|verified)\b")),
    ("S2", "copula+verdict", re.compile(
        r"(?i)\b(?:is|are|was|were|now)\s+(?:now\s+)?(?:fully\s+)?"
        r"(?:closed|cleared|canonical|promoted|verified|accepted|admitted)\b")),
    ("S3", "checklist-complete", re.compile(
        r"(?i)(?:\b(?:all|4|four)\b[^.\n]{0,30}\bbox(?:es)?\b[^.\n]{0,40}"
        r"\b(?:pass|satisf|complete|clear|\[x\])|"
        r"\b(?:pass(?:ed)?|satisf(?:ied|ies)|complete[d]?)\b[^.\n]{0,30}"
        r"\b(?:all|4|four)\b[^.\n]{0,20}\bbox(?:es)?\b)")),
]

NEG = re.compile(r"(?i)\b(?:no|not|never|none|without|zero|neither|nor|cannot|can't|"
                 r"does not|do not|did not|is not|are not|was not|were not|refuses?|refused|"
                 r"nothing|unproven|unverified|to-verify|pending|owed|"
                 r"non-?canon|un-?cleared|in-flight|awards no|grants no|admits nothing)\b")

ROUTED = re.compile(r"(?i)\b(?:lore-shokunin|lore\b|operator|owner|owned by|routed|route|"
                    r"handoff|handed off|decision materials|decision's evidence|"
                    r"external authority|non-author|reviewer|adjudicat(?:e|ed|ion)|"
                    r"await|awaiting|forward(?:ed)?|carried|queue|open item|"
                    r"this seat|integrator|expected (?:green|to)|must stay green|"
                    r"regression control)\b"
                    r"|\b(?:by|per|from)\s+(?:seat\s+)?[A-Z]{1,3}\d{1,3}\b"
                    r"|\bseat\s+[A-Z]{1,3}\d{1,3}\b"
                    r"|^\s*\*\*[A-Z]{1,3}\d{1,3}\b"
                    r"|\b[A-Z]{1,3}\d{1,3}\s*(?:—|–|:)\s")

CITE = re.compile(r"`[^`]+`|[A-Za-z0-9_./-]+\.(?:py|md|json|yml|yaml|txt):\d+"
                  r"|[A-Za-z0-9_./-]+\.(?:py|md|json|yml|yaml|txt)|"
                  r"\b[0-9a-f]{7,40}\b")

CMD_START = re.compile(r"(?i)^\s*(?:grep|rg|egrep|fgrep|python3?|sha256sum|git|ls|find|wc|"
                       r"sed|awk|cat|test|date|stat|for|echo|sort|uniq|head|tail|diff)\b")
PATHY = re.compile(r"[/.]|\.(?:py|md|json|yml|yaml|txt)\b")
ENUM_LINE = re.compile(r"(?i)(?:term counts?:|\|\s*canon\s*\||promot\|canon|"
                       r"grep\s+-[a-z]*[niE]|promotion/canon/closure)")
# repo lifecycle vocabulary: these name an artifact's state, not a governance verdict
LIFECYCLE = re.compile(r"(?i)closing snapshot|close-out|closure ledger|closure entry|"
                       r"closure row|close-time|close what you open|at close|"
                       r"round'?s close|closes? the round|closing the round")

FIXTURES = [
    # (text, pass, expected class)
    ("no promotion is claimed", 1, "NEGATION"),
    ("the canon decision stays operator-owned", 1, "ROUTED-REFERENCE"),
    ("canon rulings go to lore", 1, "ROUTED-REFERENCE"),
    ("this audit grants no canon", 1, "NEGATION"),
    ("the box 1 condition is now closed", 1, "UNSUPPORTED-CLAIM"),
    ("independently verified by seat R07", 1, "ROUTED-REFERENCE"),
    ("the item is closed as fixed", 1, "UNSUPPORTED-CLAIM"),
    ("never truth, canon, or clearance", 1, "NEGATION"),
    ("`corpus/knowledge/verification/x.md:207`", 1, "MENTION-EXEMPT"),
    ("grep -rn -i -E \"promot|canon|closure\" reports/round-33/", 1, "MENTION-EXEMPT"),
    ("Term counts: `promot` 16, `canon` 16", 1, "MENTION-EXEMPT"),
    ("the closing snapshot is owed", 1, "MENTION-EXEMPT"),
    ("the gate is verified (`tools/gates/x.py:1`)", 1, "CITED-RESULT"),
    ("```python\nr\"promotion|canon|closure\"\n```", 1, "MENTION-EXEMPT"),
    ("The box 1 condition is now closed", 2, "UNSUPPORTED-CLAIM"),
    ("All four boxes pass", 2, "UNSUPPORTED-CLAIM"),
    ("round 33 awards no promotion, canon, clearance or closure verdict", 2, None),
]


def window(text, start, end, span=300):
    """Paragraph-scoped context: a negation in the same bullet/paragraph counts.
    Falls back to a fixed span when the enclosing paragraph is very large."""
    lo = text.rfind("\n\n", 0, start)
    hi = text.find("\n\n", end)
    lo = 0 if lo == -1 else lo + 2
    hi = len(text) if hi == -1 else hi
    if hi - lo > 700:
        lo, hi = max(0, start - span), min(len(text), end + span)
    return text[lo:hi]


def backtick_spans(text):
    return [(m.start(1), m.end(1)) for m in re.finditer(r"`([^`\n]*)`", text)]


def line_of(text, off):
    return text.count("\n", 0, off) + 1


def line_span(text, off):
    a = text.rfind("\n", 0, off) + 1
    b = text.find("\n", off)
    return text[a:b if b != -1 else len(text)]


def fence_spans(text):
    """Spans of fenced code blocks (including the fence lines)."""
    return [(m.start(), m.end())
            for m in re.finditer(r"^[ \t]*(?:```|~~~).*?^[ \t]*(?:```|~~~)[ \t]*$",
                                 text, re.S | re.M)]


def mention_reason(text, start, end, spans):
    line = line_span(text, start)
    for a, b in fence_spans(text):
        if a <= start < b:
            return "code-block-literal"
    for a, b in spans:
        if a <= start < b:
            inner = text[a:b].strip()
            if " " not in inner or CMD_START.match(inner) or PATHY.search(inner):
                return "backticked-path-or-command"
    if start > 0 and text[start - 1] == "/":
        return "path-component"
    if end < len(text) and text[end] == "/":
        return "path-component"
    if ENUM_LINE.search(line):
        return "grep-invocation-or-term-enumeration"
    if LIFECYCLE.search(line):
        return "lifecycle-vocabulary"
    # a markdown heading names a section; it cannot itself assert a verdict
    if re.match(r"^\s{0,3}#{1,6}\s", line):
        return "heading-names-section"
    # bold pseudo-heading on its own line ("**Verification commands:**")
    if re.match(r"^\s*\*\*[^*]{0,90}\*\*\s*:?\s*$", line):
        return "heading-names-section"
    # explicit mention-of-the-word, and count enumerations like "verification (7)"
    if re.search(r"(?i)\bword\s+[*_`]*\w+[*_`]*", line) or \
       re.search(r"(?i)\b\w+\s*\(\d+\)\s*\*?\*?$", line):
        return "term-named-not-claimed"
    return None


def classify(text, start, end, spans):
    reason = mention_reason(text, start, end, spans)
    if reason:
        return "MENTION-EXEMPT", reason
    w = window(text, start, end)
    neg = NEG.search(w)
    if neg:
        return "NEGATION", neg.group(0)
    routed = ROUTED.search(w)
    if routed:
        return "ROUTED-REFERENCE", routed.group(0)
    if CITE.search(w):
        return "CITED-RESULT", CITE.search(w).group(0)[:40]
    return "UNSUPPORTED-CLAIM", ""


def scan_file(full, rel):
    with open(full, "r", encoding="utf-8", errors="replace") as fh:
        raw = fh.read()
    spans = backtick_spans(raw)
    def hits_for(rxset):
        out = []
        for pid, label, rx in rxset:
            for m in rx.finditer(raw):
                cls, tok = classify(raw, m.start(), m.end(), spans)
                w = window(raw, m.start(), m.end())
                out.append({"file": rel, "line": line_of(raw, m.start()),
                            "pattern": pid, "term": label, "match": m.group(0),
                            "class": cls, "class_token": tok,
                            "excerpt": re.sub(r"\s+", " ", w.strip())[:300]})
        return out
    return {"path": rel, "sha256": hashlib.sha256(raw.encode()).hexdigest(),
            "bytes": len(raw.encode()), "lines": raw.count("\n") + 1,
            "hits": hits_for(PATTERNS), "strict": hits_for(STRICT)}


def expected_outs():
    with open(os.path.join(ROUND, "targets.json"), encoding="utf-8") as fh:
        d = json.load(fh)
    outs = []
    for s in d.get("seats", []):
        o = s.get("out")
        if o and o not in outs:
            outs.append(o)
    return outs


def walk():
    found = []
    for dirpath, dirnames, filenames in os.walk(ROUND):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        for fn in sorted(filenames):
            if fn.endswith(SUFFIXES):
                full = os.path.join(dirpath, fn)
                found.append((full, os.path.relpath(full, ROOT).replace(os.sep, "/")))
    return sorted(found, key=lambda t: t[1])


def summarize(hits):
    return {c: sum(1 for h in hits if h["class"] == c) for c in CLASSES}


def run():
    files = [scan_file(f, r) for f, r in walk()]
    exp = expected_outs()
    exp_abs = [f"reports/round-33/{o}" for o in exp]
    landed = [o for o, a in zip(exp, exp_abs) if any(f["path"] == a for f in files)]
    all_hits = [h for f in files for h in f["hits"]]
    all_strict = [h for f in files for h in f["strict"]]
    unsupported = [h for h in all_hits if h["class"] == "UNSUPPORTED-CLAIM"]
    unsupported_nc = [h for h in unsupported if h["file"] not in CONTRACT]
    return {
        "scan_root": "reports/round-33",
        "files_scanned": len(files),
        "expected_seat_outs": len(exp),
        "seat_outs_landed": len(landed),
        "coverage": f"{len(landed)}/{len(exp)} seat out-paths present",
        "missing_seat_outs": [o for o in exp if o not in landed],
        "pass1_hits": len(all_hits), "pass1_by_class": summarize(all_hits),
        "pass2_hits": len(all_strict), "pass2_by_class": summarize(all_strict),
        "unsupported_total": len(unsupported),
        "unsupported_non_contract": len(unsupported_nc),
        "unsupported_rows": unsupported_nc,
        "files": files,
    }


def selftest():
    ok = 0
    for text, p, want in FIXTURES:
        spans = backtick_spans(text)
        if p == 1:
            got = None
            for _pid, _l, rx in PATTERNS:
                m = rx.search(text)
                if m:
                    got = classify(text, m.start(), m.end(), spans)[0]
                    break
        else:
            got = "UNSUPPORTED-CLAIM" if any(
                classify(text, m.start(), m.end(), spans)[0] == "UNSUPPORTED-CLAIM"
                for _sid, _l, rx in STRICT for m in rx.finditer(text)) else None
        mark = "ok " if got == want else "FAIL"
        ok += got == want
        print(f"{mark} pass{p} want={str(want):18s} got={str(got):18s} :: {text[:58]}")
    print(f"selftest {ok}/{len(FIXTURES)}")
    return 0 if ok == len(FIXTURES) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--findings", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    r = run()
    if args.json:
        print(json.dumps(r, indent=2))
        return 0
    print(f"files_scanned={r['files_scanned']} coverage={r['coverage']}")
    print(f"pass1 hits={r['pass1_hits']} by_class={r['pass1_by_class']}")
    print(f"pass2 hits={r['pass2_hits']} by_class={r['pass2_by_class']}")
    print(f"UNSUPPORTED-CLAIM (non-contract) = {r['unsupported_non_contract']}")
    rows = r["unsupported_rows"] if (args.findings or not args.strict) else \
        [h for f in r["files"] for h in f["strict"] if h["class"] == "UNSUPPORTED-CLAIM"]
    for h in rows:
        print(f"  {h['file']}:{h['line']} [{h['pattern']}] {h['match']!r} :: {h['excerpt'][:150]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```