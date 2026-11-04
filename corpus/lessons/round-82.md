# Round 82 — kotodama (Linux/omp host, 2026-11-04)

Base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` (the round-81 verifier
spot-check commit); freeze `25907323b7b756145eddc76ed2dcd8bddc48197c`
(`claims.json`, both counters, the junk battery — constants read with
`git show <freeze>:reports/round-82/claims.json`). Claim O lands
`41c6de89f77385e43c396438ad287df07a660576`; claim D's first lands is
`277fdf4aed5cf67f0645f2e30cfa7c1a8fe312f2` and its graded lands (after the
reviewer's edits) `6c525ba45c008638dda7385449768629987455b1` under re-freeze
`3bb408ae464cf79178a0d625c6ea339ccc7814cc`; claim C lands
`3a59daafa503cd9c2db385a77b525460ed55c55a`. Counter revisions r2
`696835ee…` and r3 `ea667212…` are recorded in `reports/round-82/counter-revisions.md`. One v1 wave of 14 seats under the
8–16 band (3 scout, 3 executor, 2 scribe, 1 connector, 1 reviewer, 2 critic,
1 mutation-tester, 1 sentinel; the L1 holds the canonical planner seat); claims
frozen before any claim artifact landed.

Three claims: **O** (operability, capability acquisition — the registry
recheck-cadence auditor), **D** (depth — the guest-right / hospitality-law
entry, four rows opened this round) and **C** (calibration — QUALITY 30, the
folded-re-read rule for "no quotable prose" rejects, which also overturns a
round-81 reject ground).

## Gate

Candidates considered and dispositioned. Every number carries the command that
produced it; capture records are under `reports/round-82/evidence/`.

- **ADMITTED — claim O (operability): `tools/check-sources-recheck.py`.** At
  base no tool reads the registry's `recheck` cells (`git ls-tree --name-only
  <base> tools/ | grep -c recheck` = 0; `git grep -c RECHECK-QUEUE <base> --
  tools/ reports/` = 0 lines). The tool lands and derives the queue from
  committed bytes: `RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827
  rows` at `--as-of 2026-11-04 --window 90` and `813 due / 0 upcoming / 14
  on-release / 827 rows` at `--as-of 2027-11-01 --window 90`, both over the
  FROZEN registry blob and both matching an independent L1 tally
  (`reports/round-82/telemetry/queue-independent-tally.txt`). Selftest 13
  checks. The zero-due reading at the round date is the honest finding: with
  the registry's cadences (90/180/365d and two absolute 2027 dates) nothing is
  yet overdue, and the next reading falls due 2027-01-17 — the lane now knows
  that from a command instead of from memory.
- **ADMITTED — claim D (depth): `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`.**
  At base no file owns the surface: filename sweep `guest|hospital|xenia|hospitium|stranger`
  → 0 of 255 files; the institutional core `xenia|hospitium|guest-friend|theoxeny`
  → 0 lines; the 15 files that mention hospitality carry passing attributes only
  (census in `.ufo/waves/round-82/w1/stage/ScoutGap/gap-census.md`). The entry
  lands as the 256th knowledge file with four rows opened this round:
  - **S904** Homer, *Odyssey*, trans. Butler (Gutenberg #1727), tier A —
    `「for all strangers and beggars are from Jove」` (8 words, Odyssey xiv).
  - **S905** Tacitus, *Germania*, trans. Church & Brodribb (Wikisource), tier
    A — `「No nation indulges more profusely in entertainments and hospitality.
    To exclude any human being from their roof is thought impious」` (20 words,
    ch. XXI), raw-contiguous once in the live body and in the capture.
  - **S906** Ovid, *Metamorphoses* viii, trans. Riley (Gutenberg #26073), tier
    B — `「Yet one received them, a small one indeed, thatched with straw」`
    (11 words, the Baucis and Philemon theoxeny).
  - **S907** "Guest", EB11 vol. 12 (1911), **tier C** — `「one who receives
    hospitality in the house of another」` (9 words): a dictionary gloss, filed
    as a lead with that scope, never sole support.
  Every quote re-located by the L1 against the fetched bodies (22 entry bullets,
  21 exact, 1 corrected before landing); the entry passes
  `tools/check-cited-lines.py` with 0 findings (one S-id per cited line, no
  S-id in any table row).
- **REJECTED (fresh, filed) — S908, Frazer's *The Golden Bough*.**
  HTTP 200, 2,331,343 bytes, span `「magic is a spurious system of natural law
  as well as a fallacious guide of conduct」` **present** on the page — the
  reject is framework status (the unilinear magic→religion→science stage law
  QUALITY 2 bars from load-bearing use), with a `flip:` condition
  (`reports/round-82/evidence/reject-golden-bough.txt`).
- **CARRIED, RE-OPENED AND OVERTURNED — EB11 "Coin"/"Mint" (round 81).** Round
  81 rejected "Mint" as rendering "only via client-side transclusion, so a
  plain fetcher cannot find quotes there". Re-measured this round: the live
  page folds to article prose (HTTP 200, 148,302 decoded bytes, 27 `</p>`, the
  opening sentence present once) and the `20260608000413` capture serves it too
  (`reports/round-82/telemetry/quality30-probe.txt`). The ground was
  extraction-shaped; the filed reject stands as history and QUALITY 30 is its
  correction. "Coin" remains a ~50-word stub — a thin-source ruling, not an
  access ruling.
- **CARRIED, UPHELD — heraldry/emblems entry.** `myth-symbol/heraldry-emblems-identity-marks.md`
  exists at base; declaring it would be a do-nothing-with-extra-steps claim.
- **SUBSTITUTED BEFORE DATA — the Hávamál page.** Planned for the S905 slot;
  set aside for two independently measured reasons: (a) its Bellows 1923
  translation is already row **S320** (Gutenberg #73533), so the work, not just
  the URL, is registered (duplicate-document check by document, per CORPUS.md
  rule 4); (b) its hemistichs sit in separate `ws-poem-line` spans, so the
  longest raw-contiguous run is 5 words (`Where shall the stranger sit?`) and
  the planned quote needs Unicode folding to reach 8. Carried as a candidate,
  not rejected.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R82-M1 | **reject ground measured on the prober's own extractor** — round 81 rejected EB11 "Coin"/"Mint" because a tag-stripper that emitted no separator read the page as scaffold; the same artifact recurred in this round's first read of EB11 "Guest" and was caught by a seat, not by a criterion | `reports/round-82/telemetry/quality30-probe.txt` (live Mint: 148,302 decoded bytes, 27 `</p>`, span once; capture: 28 `</p>`) and `reports/round-82/evidence/S907.txt` (`note:` line recording the corrected first read) | a wave seat's folded re-read (`ScoutSources-12`) plus the L1's own re-measurement — no criterion existed to catch it (that is the defect) | **QUALITY 30** (claim C): a "no quotable prose" reject records `raw <n> / folded <m>` for its located span plus the same-page capture probe before it is filed; the two falsified cases are named in the criterion's grounding |
| R82-M2 | **selftest fixture that is not the shape it claims** — the O tool's `12-cell row` check built `row(...)[:-1] + " extra |"`, which still yields 11 cells, so the tool's own selftest reported a false failure against correct parsing | this round's integration receipt: the installed tool's selftest printed `SELFTEST: FAIL 12-cell row: rc=0 stdout='DUE S911 …'` before the fix; the committed `reports/round-82/telemetry/selftest-tool.txt` is the green run after it | the L1 integration pass (the failure was visible in the green-first gate) | fixture corrected to `[:-1] + "| extra |"`; the malformed-registry path is separately proven by a hand-written 12-cell fixture (`RECHECK-ERROR line 7: row has 12 cells, expected 11`, exit 2) |
| R82-M3 | **two evidence sets for one row set** — the entry seat and the rows seat each wrote their own capture records (different UA strings, capture timestamps and byte counts), so a closure would have found two `reports/round-82/evidence/` candidates and no stated rule for which binds | `reports/round-82/evidence/S904.txt`–`S907.txt` (installed set) vs `.ufo/waves/round-82/w1/stage/ScribeRows/S90*.txt` (second reading, kept) | the rows seat reported the conflict in its result message before the freeze | one installed set is graded by the counters and cited by the rows; the other stays as the independent second reading and the report names both — a round must say which evidence set binds |
| R82-M4 | **planned source that duplicates a registered work** — the S905 slot was planned on the Hávamál page while row S320 already registers the Bellows translation (Gutenberg #73533), i.e. the same work, not just the same URL | `git -C <lane> grep -n 'Bellows' <base> -- corpus/SOURCES.md` → S320 at line 349 and S318 in its provenance; the longest raw-contiguous run on the Hovamol page is 5 words (seat probe, `.ufo/waves/round-82/w1/stage/ScribeRows/S905.txt`) | the duplicate-document check by document (CORPUS.md rule 4), run before the rows were drafted | S905 substituted with Tacitus *Germania* ch. XXI (raw-contiguous 20-word span); the Hávamál probe is recorded so the substitution is auditable |

| R82-M5 | **seat misroot into the fleet repo** — an evidence seat's `write` call named `write` as the path (its content is the message address `agent://ExecEvidence?progress`), landing a stray file at the fleet root instead of under the lane | fleet-root `write` (29 B, mtime 2026-11-04 08:29), preserved byte-exact at `.ufo/waves/round-82/w1/stage/misroot/write` after `cmp` on the copy and removal of the fleet file (the one fleet-root deletion a lane may make) | the L1's pre-report `git status --porcelain` sweep over the fleet root | the wave `context` already binds absolute seat paths and says a relative path lands in the fleet repo; the miss came from a tool-argument slip, not from an unclear bound — recorded so the next round's context repeats the absolute-path rule beside the `Report:` trailer note |

| R82-M6 | **counter under-enforcement** — the frozen claim-O counter passed `DUE`-less output, a doubled summary line, and a one-day-shifted NNd arithmetic (mutation score 1/5); two independent seats found it | `reports/round-82/telemetry/counter-r1-redbefore.txt` (r1 grades a shifted tool `PASS 7/7`) and `.ufo/waves/round-82/w1/MutationTesterO.md` (1/5 killed) | `CriticClaimO` §3–§4 and `MutationTesterO` — after the claims were graded, so the claim verdicts stand and the instrument is repaired | counter r2 `696835ee` (DUE id/date set, exactly-one-summary, NNd boundary probe) and r3 `ea667212` (rows-less and population-growing scenarios): mutation score 5/5, selftest 16 checks, re-grade `ACCEPT-O-82: PASS legs=7/7`; `telemetry/counter-r2-caught.txt`, `counter-r3-mutation.txt` |

## Sources & frontier

Registry rows 827 → 832 (`S904`, `S905`, `S906`, `S907` mined, `S908`
rejected; no prior-row cell changed). Counting:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` = 832
at the records tip, 827 at base. Knowledge files 255 → 256
(`git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'`).
Census receipts: `reports/round-82/telemetry/census-start.txt` (exit 0 at base,
827 rows, W01/W04 warnings only — the pre-existing profile) and
`census-end.txt` (exit 0, 832 rows, same warning classes).
Rows added by tier: A 2 (S904, S905), B 1 (S906), C 1 mined (S907) + 1 rejected
(S908). Frontier rows advanced: S901–S903's material is untouched; the
civilization partition's hospitality attributes are now pointed at one owner.
Sourced claim: D rests on S904–S907, all opened this round (evidence records
under `reports/round-82/evidence/`, second independent reading kept in the wave
stage). Assimilation: none — no `merge/kotodama/` theme fits this round's
claims; the lane's earlier quarantine verdicts stand.
