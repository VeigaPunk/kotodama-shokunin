# R10-C19 — Reviewer of worker C09's verification-partition entry (author-side review)

- reviewer scope: `reports/round-10/coverage/review-C09.md` only. No corpus, ledger, bookkeeping, canon, or promotion edits. Author-side review evidence only; not an admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one per authored entry (poll for it, max 20 min): verify frontmatter completeness, source resolvability (re-run the cited command or open the cited path/URL), no filler, no duplication of an existing entry; verdict `reports/round-10/coverage/review-<id>.md`").
- C09 is the first verification-partition author (`R10-C01..C10`: linguistics ×3 = C01–C03; myth-symbol ×3 = C04–C06; culture-material ×2 = C07–C08; verification ×2 = C09–C10). Deliverables under review: fragment `reports/round-10/coverage/C09.md` + entry `corpus/knowledge/verification/verification-independence-anti-circularity.md`.
- round-10 declared baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (`reports/round-10/claims.json`); worktree HEAD throughout: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` ("round-10: availability attempt 3 …"). The entry is untracked (`git ls-files` → pathspec not known), so the reviewed revision is identified by digest, not commit.
- **Reviewed revision (read-time digest, this review's verdicts bind to it):** `corpus/knowledge/verification/verification-independence-anti-circularity.md` — sha256 `743bce544c888a9159728af4b6f5dcecb98166adc3a77d30e7794b5d711d0cff`, 159 lines, 31,956 bytes, mtime 2026-10-17 21:33:47Z; digest stable across 8 samples 21:35:27–21:36:09Z (`.scratch/c19-churn.log`).
- date: 2026-10-17. All times UTC.

## 0. Landing timeline (poll receipts)

| time (UTC) | observed |
|---|---|
| 21:26:2x | review open: `reports/round-10/coverage/` empty; `corpus/knowledge/verification/` = 13 files (baseline `sha256` snapshot taken, `.scratch/baseline-verification.sha256`); wave live (sibling scratch files appearing) |
| 21:30:44 | C09's entry lands → partition 14 files; first read (147-line revision, no §1.1) |
| 21:32:45 | entry measured at 159 lines / 31,787 B / sha256 `e8b3503c…` (the digest the fragment later records) |
| 21:33:32 | fragment `reports/round-10/coverage/C09.md` lands (sha256 `d4d34050…`, 7,765 B) |
| 21:33:47 | entry edited again → 31,956 B / sha256 `743bce54…` (+169 B, line count unchanged) |
| 21:35:27–21:36:09 | digest stable at `743bce54…` (8 samples, 10 s cadence); review proceeds against this revision |
| 21:3x–21:4x | peer verification entry `header-conformance-readings.md` (C10) also lands → partition 15 files |

- The 20-minute poll window was never exhausted: entry landed 4 min after open, fragment 7 min after open. Both the entry path and the fragment path were watched (background pollers, 15 s cadence, `.scratch/poll-C09.log`, `.scratch/watch-C09.log`).

## 1. Method and instruments

- Mechanical harness `.scratch/check-C09.py` (written by this review): header-field census, heading inventory, decision-section detection, backticked-path resolution, URL/command extraction, `(to-verify)` census, count-without-command scan, duplication screen (slug collision + title/topic similarity vs every `corpus/knowledge/**/*.md`).
- Independent re-execution: receipt digests recomputed with `sha256sum`; every receipt line locator opened with `sed -n`; every quoted string compared verbatim; the lane gate and the entry's own cited commands re-run (below).
- Baselines: `corpus/knowledge` = 179 files at open (`find … | wc -l`, 21:27Z); verification partition = 13 files at open, 15 at close; no pre-existing verification file was modified by C09 (`sha256sum` of the 13 baseline files re-checked — all unchanged).
- Reviewer's re-runs did not modify repo bytes: `git status --porcelain -- corpus examples` identical before/after the frozen-check re-run.

## 2. The four mandated checks

### 2.1 Frontmatter completeness — PASS

```
grep -c "^- topic:\|^- sources:\|^- couples:\|^- follows:\|^- verified-at:\|^- recheck:" <entry>   # → 6
grep -n "^- \(topic\|sources\|couples\|follows\|verified-at\|recheck\):" <entry>
# lines 3, 4, 15, 16, 17, 18 — each field exactly once, non-empty; verified-at dated 2026-10-17 with its scope
```

- Partition profile census (all 15 verification files): `- topic:`, `- sources:`, `- couples:`, `- verified-at:`, `- recheck:` → **15/15 each**; literal singular `- source:` → 3/15 (`citation-format-and-source-registry`, `myth-consistency-gate`, `provenance-audit-ledger-format`). The entry conforms to the partition's dominant profile.
- Fleet-literal reading: `CORPUS.md:17` ("each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`") is not satisfied by the singular `source:` leg — the same standing gap `corpus/README.md` known-gaps already records ("Most historical entries lack the fleet's complete `source`, `verified-at`, `recheck` header … the provenance gate checks the older topic/sources/couples profile"). This is a partition-wide convention item, not a defect introduced by C09; the peer entry C10 exists precisely to measure that gap.
- Lane gate: `python3 tools/gates/provenance-audit.py corpus/knowledge/verification` → `files=15 marks=79 mark-lines=78 findings=0 blocked=0`, exit 0 (matches the fragment's §3 claim exactly, re-run on the final bytes at 21:36Z).
- `(to-verify)` census: the gate's 2 marks on the entry are both the token inside `to-verify-triage-protocol.md` references / prose (lines 15, 31) — no unresolved placeholder. The fragment's own note about this is accurate.

### 2.2 Source resolvability — PASS (one drift note, F1 below)

**Receipt digests — all four recomputed and exact:**

| receipt | entry's claim | recomputed (`sha256sum`, 21:3xZ) | match |
|---|---|---|---|
| `reports/round-8/depth/findings.md` | `01c27fde…af5a` | `01c27fde…af5a` | ✅ |
| `reports/round-8/depth/findings-17.md` | `8f6eabad…10aa` | `8f6eabad…10aa` | ✅ |
| `reports/round-9/d3/findings.md` | `27ba8c2f…437c` | `27ba8c2f…437c` | ✅ |
| `reports/round-9/d3/findings-10.md` | `19376989…91be` | `19376989…91be` | ✅ |

**Receipt line locators — all 12 opened and exact:** `findings.md` l.34 (§S2 frozen manifest), l.47 (§S3), l.81 (§S11), l.98 (§S13); `findings-17.md` l.156 (churn record), l.190 (F-D17-1); `d3/findings.md` l.33 (§S1), l.47 (minimum record), l.58 (§S2), l.64 (§S3), l.75 (§S4); `findings-10.md` l.71 (forcedness), l.159 (circularity warning). The fragment's extra locator l.132 = `### F2 — the D3 frozen pin is red on this tree` also verified.

**Quoted strings — verbatim against source (5 sampled, all exact):** "proves *someone refreshed the manifest after the edit*" (`d3/findings.md:43`); "documented design, residual only" (`:75`); `d9e084a8 → … → 623b5b1f` (`findings-17.md:157–158`); the LOG.md round-9 line "orchestrator refreshed three expected.json pins — all three drifts are…" (`LOG.md:2973`); and all three §1.1 adjacency quotes — `citation-format-and-source-registry.md:192` ("count witnesses, not websites"), `provenance-audit-ledger-format.md:151` §8 item 10 ("…independently retained anchor; exclude a checkpoint's own bytes…"), `verification-method-overview.md:163` §10 item 8 ("A prose walkthrough is not an independent reviewer sign-off; name any reviewer and what they actually checked.").

**Tool-code locators:** `tools/check-evidence-coupling.py:1863-1876` — confirmed the selftest builds `frozen-good`/`frozen-tampered` from live bytes at those lines; `:1687-1706` — confirmed `missing = sorted(set(want_ids) - got)` (subset matcher). `reports/round-8/run-validation.py:1357` — confirmed the whole-file regex `re.search(r"d2[-_ ]typed[-_ ]labels", scorecard, re.I)`.

**Cross-reference targets:** every `couples`/`follows` path resolves (`tools/check-evidence-coupling.py`, `tools/replay-frozen.py`, `tools/check-gate-battery.py`, `tools/gates/expected/`, `tools/gates/frozen/`, `reports/round-8/depth/`, `reports/round-9/d3/`, `../synthesis/worldbible-integration-contract.md`); section refs checked: `gate-frozen-run-standard.md` §3/§4–§6/§10, `verification-method-overview.md` §1–§2/§6, `provenance-audit-ledger-format.md` §8, `worldbible-integration-contract.md` §9 ("Lore pins exact delivered versions and digests, not version ranges") — all exist and match the entry's characterizations.

**URLs:** `https://doi.org/10.1109/TSE.1986.6312924` → 202; `https://doi.org/10.1109/TSE.2010.62` → 202; `https://doi.org/10.1145/382294.382710` → 403 (blocked by remote server — recorded access limit, the same class other partition entries document); `https://reproducible-builds.org/docs/` → 200 (`curl -s -o /dev/null -w "%{http_code}" -L`, 2026-10-17).

**Cited commands re-run (independent re-execution, not just path-opening):**

```
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
# → exit 0, "findings": []   (reviewer re-run, 21:3xZ; no repo bytes changed)
python3 tools/gates/provenance-audit.py corpus/knowledge/verification
# → files=15 marks=79 mark-lines=78 findings=0 blocked=0, exit 0
```

- The frozen check is **green now** where round 9 measured exit 2 / 3 × `D3-SNAPSHOT` — not a contradiction: `LOG.md:2973` records the orchestrator's refresh of three `expected.json` pins, and the entry's §7 frames exactly that state (row 4: "admissible **if** the ledger carries fields 1/5/6 … the LOG entry alone does not show fields 1, 5, or 6"). See F4.

### 2.3 No filler — PASS

- Gap named in the entry itself (topic line: "Gap filled: … no entry states verifier independence …"), developed at §1.1 with a three-row adjacency table, and closed by §2/§4/§6. Not an essay: §2 catalog, §3 five questions, §4 control rules, §5 checklist, §6 re-pin record + disposition table, §8 IND-1..IND-6 — all decision artifacts, per `corpus/QUALITY.md` items 1–5.
- The gap's negative claim reproduces: `grep -rn -i "separation of duties\|independent verifier\|verifier independence\|different shard" corpus/knowledge/ | grep -v verification-independence-anti-circularity` → **0**; `grep -rc -i "circularity" corpus/knowledge/` → the three named unrelated files, one hit each (`linguistics/semantics-pragmatics.md:46`, `myth-symbol/hero-journey-variants.md:37`, `synthesis/taboo-euphemism-lifecycle.md:155`).
- The gap is real, not rhetorical: the three adjacent rules the entry cites genuinely leave the residual open — verified by opening each quoted line (they govern *source* corroboration, ledger checkpoint anchoring, and reviewer naming respectively, none of which states verifier independence or the re-pin record).

### 2.4 No duplication — PASS

- Slug collision: none. Title/topic similarity screen re-run against the whole corpus as it stood at screen time — `find corpus/knowledge -name '*.md' | wc -l` → 189 (2026-10-17T21:37:54Z; the count moves with each sibling landing) — harness `difflib` ratios: no title ≥0.75, no topic ≥0.6, no duplicate slug.
- Peer-entry screen: C10's `header-conformance-readings.md` covers the header measurement contract (three readings, count-statement schema, pins on the B-remainder files) — a different gap from verifier independence/anti-circularity. Checked at both ends: C09's `couples` names gates/standards and lane tooling, not header measurement, and C10's `couples` names `provenance-audit-ledger-format` / `citation-format-and-source-registry` / `gate-frozen-run-standard`, not this entry's subject; the two topics share no phrasing beyond the partition's own vocabulary. No `-b` collision handling was needed, consistent with the fragment's §1 note.

## 3. Findings

### F1 — `SCORECARD.md:117` is a stale second-hand locator at HEAD (severity: low; drift, not fabrication)

- The entry's §2 C6 row quotes KTD-VI-S-0001 §S11: the harness regex "already occurs in the Planned section (`SCORECARD.md:117`)".
- The receipt's locator was correct **at the round-8 revision**: `git show cf338a7:SCORECARD.md | sed -n '117p'` → "`d2-typed-labels` capability (typed translated-label/native-form handling," with `## Planned` at line 100.
- At the entry's own declared revision `e3a1ec9` (and at `9dc18ec1`, `ac93be9`, `6c32954`): line 117 is the round-8 `adjacency` table row; the pattern occurs at lines 112, 128, 181, with `## Planned` at line 160 — so the string is still inside the Planned section, but the cited line number has drifted (117 → 181).
- Substance of C6 remains live and is independently confirmed (`reports/round-8/run-validation.py:1357`). Only the inherited line number is stale, and it carries no revision stamp — the exact class the entry's own C7/IND-5 catalogs. Recommended fix (append-only, not a rewrite): stamp the locator with the round-8 revision it was measured at, or re-measure. Natural owner: the round-10 F-axis drift audit (`R10-F01..F19`).

### F2 — the fragment's deliverable fingerprint is stale against the final entry (severity: low; churn in flight)

- Fragment §2 claims: "159 lines, 31,787 bytes, sha256 `e8b3503c…` (measured 2026-10-17 after the final edit)". That matched the entry at 21:32:45.
- The entry was edited again at 21:33:47 — after the fragment's own write (21:33:32) — to 159 lines / 31,956 bytes / sha256 `743bce54…` (+169 B, same line count; delta not localizable because the file is untracked and pre-edit bytes were not retained by this reviewer; my own reads bound it: lines 50–159 verbatim-identical between reads, so the delta lies in the header/§1 block).
- All of the fragment's *structural* claims still hold at the reviewed revision (159 lines; six header fields; §1.1 present; decision records at §6 and §8; §1–§10 headings). Only the byte/digest fingerprint is superseded.
- Per the entry's own IND-5/C8 this is exactly the case its rules demand be recorded, not smoothed: the fragment's fingerprint must be re-measured, and any verdict quoted from it must carry the digest it was measured on. Fix is a one-line correction; per lane append-only discipline it is a new note, never a rewrite of the filed fragment bytes.

### F3 — wording: the entry's `verified-at` shorthand "→ 0 hits" now reads 3 hits, all inside the entry itself (severity: info)

- Re-run of the entry's own quoted command (`grep -rn -i "separation of duties\|independent verifier\|verifier independence\|different shard" corpus/knowledge/`) → 3 lines, all in `verification-independence-anti-circularity.md` (topic line 3, §1.1 line 44's quoted sweep string, verified-at line 17). Outside the entry: 0 (verified).
- §1.1's own phrasing ("0 hits outside this entry") is exact and self-consistent; only the `verified-at` shorthand is loose for a post-write re-run. No action required beyond aligning the wording if the entry is next touched.

### F4 — observation, supporting the entry rather than faulting it: the §7 "conditional" disposition is now live-demonstrable (severity: info)

- Round-9 evidence: `--frozen` → exit 2, 3 × `D3-SNAPSHOT` (receipt l.39/l.117). This review's independent re-run at 21:3xZ: **exit 0, `findings: []`**.
- The transition is explained by the round-9 pin refresh and is precisely the state the entry's §6/§7 classify: the current green is quotable only as **conditional** until the six-field record (pre-refresh token, unedited expectation, different-shard re-run) exists — and §2 C1's quoted warning ("a green frozen run proves *someone refreshed the manifest after the edit*") is literally illustrated by it. No finding against the entry; recorded so the round's acceptance does not quote this green as unconditional.
- Side benefit of the re-run: it demonstrates the entry's own IND-5 point that receipt verdicts are revision-bound (round-9 red vs. round-10 green are both correct at their revisions).

## 4. Limits of this review

- This is author-side evidence for one seat, not an admission decision, not promotion verification, and not a canon or ledger edit. It reviewed exactly two artifacts: the fragment and the entry at the digests above.
- Verdicts bind to the entry digest `743bce54…`; if the file changes again before acceptance, this review's green readings (gate, digest table, locators) must be re-measured. The partition gate was re-run on the final bytes and is green at that revision.
- Not re-executed: the receipt *commands* (gate runs, the bless-the-tamper demonstration, the disable-witness matrix) beyond the two re-runs listed in §2.2; the receipts' internal claims were checked by digest + locator + verbatim quote, and one cited command was independently re-run (F4). Deeper receipt re-execution is `R10-F19`'s assignment.
- No review of sibling fragments (C01–C08, C10) or of the C/F/O axes beyond this seat's four mandated checks.

## 5. Verdict summary

| mandated check | verdict | key evidence |
|---|---|---|
| frontmatter completeness | **pass** | 6/6 fields exactly once (entry lines 3/4/15/16/17/18); 15/15 partition profile; gate `findings=0` |
| source resolvability | **pass**, with F1 (stale inherited locator, low) | 4/4 receipt digests exact; 12/12 receipt locators exact; quotes verbatim; paths resolve; 3/4 URLs reachable (1 server-blocked); cited commands re-run |
| no filler | **pass** | gap named + adjacency table; sweeps reproduce (0 outside the entry; 3 unrelated circularity hits as claimed); decision artifacts throughout |
| no duplication | **pass** | no slug collision; no title/topic near-match across the 189-entry corpus at screen time (21:37:54Z); peer C10 entry is a distinct gap |

Net: the entry is admission-ready at digest `743bce54…` subject to (a) re-measuring the fragment fingerprint (F2), (b) either stamping or re-measuring the inherited `SCORECARD.md:117` locator (F1), and (c) not quoting the current `--frozen` green unconditionally (F4/§6 disposition). No fabricated source, no filler, and no duplication were found.

FILES: reports/round-10/coverage/review-C09.md | SUMMARY: R10-C19 reviewed C09's `verification-independence-anti-circularity.md` (digest `743bce54…`) — frontmatter, source resolvability, no-filler and no-duplication all pass on independent re-runs (4/4 receipt digests, 12/12 locators, quotes verbatim, gate green), with three low/info items: a stale inherited `SCORECARD.md:117` locator, a fragment fingerprint superseded by a post-fragment edit, and the round-9-red-vs-now-green frozen check that must be quoted conditional per the entry's own §6.
