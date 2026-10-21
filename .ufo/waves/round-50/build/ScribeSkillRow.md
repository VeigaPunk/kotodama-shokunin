# ScribeSkillRow — round 50 SKILL.md proposal (Ca calibration + O operability)

Seat: ScribeSkillRow (leaf, no dispatch). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Scope: propose SKILL.md text and exact insertion anchors. SKILL.md was NOT edited (seat writes only this report).
Snapshot read: `kotodama-shokunin/SKILL.md#5CC9` (734 lines). Re-read before applying; tags change after any edit.

## 1. Evidence grounding the proposal

| fact | evidence |
|---|---|
| Claim Ca's checker does not exist yet | `ls tools/check-claim-separability.py` → no such file; `reports/round-50/separability/` absent |
| Ca's lands list omits SKILL.md | `reports/round-50/claims.json` Ca `lands`: `tools/check-claim-separability.py`, `reports/round-50/separability/r49-fixture.json`, `corpus/QUALITY.md` |
| The r49 defect is the motivating mistake | `corpus/lessons/round-49-verifier-spotcheck.md:17` ("C cites the registry S creates; c_without_s … did not verify the required counterfactual") |
| Lane is jj-colocated now | `jj status`: `main: vnpnswpm 4ad26836 …`; working copy `@` = `oszxrlox 13ae1394` (empty); `@-` = `4ad26836 main` |
| Landed sha = `main` bookmark, not `@` | `jj log -r main` → `4ad26836552462d28a946ca3b067cab0b5ce3532`; `git for-each-ref refs/heads/main` → `4ad2683` |
| `git rev-parse HEAD` can diverge from landed tip under jj | `.ufo/waves/hyaku/jj-w1/reports/JjAuditKotodama.md` R1 (`HEAD f0e826a8…` = empty `@-`, 1 ahead of `origin/main 4ad26836…`); R1 also states the sha is "not landed evidence" |
| SKILL.md has no separability or jj-colocation text today | `grep -inE 'jj|colocat|separab|check-claim|landed|HEAD' SKILL.md` → only unrelated hits (`HEAD` at lines 711-713 for a 2026-10-19 expected-verdict note) |

Observation: `git rev-parse HEAD` currently equals `4ad2683` only because no jj mutation has detached HEAD since the snapshot; the audit shows it diverges after `jj new`/`jj edit`. The proposal therefore never cites HEAD.

## 2. Proposed additions (three insertion sites, all in SKILL.md)

### 2a. Decision-table row — insert AFTER line 29, BEFORE blank line 30

Anchor: line 29 is `| Check a world hangs together | consistency-verification-checklist (synthesis) | silently resolving contradictions into canon | a findings list; canon rulings go to lore |`. Table header is line 22 (`Intent | Correct surface | Never | Expected output`).

Row text (4 columns, matches table):

```
| Declare the claims of a multi-claim round | declare each claim separably: it verifies on base + its own `lands` only; run `python3 -B tools/check-claim-separability.py <manifest>` (exit 0) before dispatch | dispatch a claim whose landed bytes cite a path or identifier another claim lands (r49 REJECTED-HONEST-STOP: C cited the registry S created); verify a claim only on the combined tree | separability manifest per claim (`lands`, `exports`, optional `acceptance`) and checker exit 0 |
```

### 2b. Checklist items — insert AFTER line 534, BEFORE blank line 535

Anchor: line 534 is the last item of `## Checklist (executable where a tool exists)` (`      open questions — \`handoff-packet-check\` enforces per packet; no canon here.`). Items use `- [ ]` with six-space continuation indent.

Two items (one separability, one jj):

```
- [ ] Before dispatching a multi-claim round, declare each claim separably:
      it verifies on base + its own `lands`, and
      `python3 -B tools/check-claim-separability.py <manifest>` exits 0.
      Land this item only together with that tool (r49 REJECTED-HONEST-STOP,
      `corpus/lessons/round-49-verifier-spotcheck.md:17`).
- [ ] Under jj colocation, cite a landed sha as the `main` bookmark
      (`git rev-parse refs/heads/main`), never `git rev-parse HEAD` or jj
      `@`/`@-`: HEAD can be an empty working-copy commit that is not on the branch.
```

The jj item cites no path that another claim lands, so it is separable on base. The separability item names `tools/check-claim-separability.py`, which only exists after Ca lands.

### 2c. Hashline ops (for the integrator)

```
[kotodama-shokunin/SKILL.md#<current-tag>]
PUT >534:
+- [ ] Before dispatching a multi-claim round, declare each claim separably:
+      it verifies on base + its own `lands`, and
+      `python3 -B tools/check-claim-separability.py <manifest>` exits 0.
+      Land this item only together with that tool (r49 REJECTED-HONEST-STOP,
+      `corpus/lessons/round-49-verifier-spotcheck.md:17`).
+- [ ] Under jj colocation, cite a landed sha as the `main` bookmark
+      (`git rev-parse refs/heads/main`), never `git rev-parse HEAD` or jj
+      `@`/`@-`: HEAD can be an empty working-copy commit that is not on the branch.
PUT >29:
+| Declare the claims of a multi-claim round | ... (row text from 2a) ... |
```

Apply in one batch using original numbers (hashline numbering is original, not hunk-shifted). Body lines beginning with `- ` must be written `+- ` as the rules require; the checklist items above already are.

## 3. Calibration / operability notes

- **Ca coupling (the reason for the placement rule).** The decision-row and the first checklist item both name `tools/check-claim-separability.py`. If SKILL.md lands before Ca, the lane's own SKILL would cite a missing tool, which is the r49-class defect. Therefore: either (i) add `SKILL.md` to Ca's `lands` in `reports/round-50/claims.json` and land 2a/2b-separability with Ca, or (ii) hold 2a/2b-separability until Ca lands. The jj item (2b second item) has no such dependency.
- **Shared file, not disjoint paths.** Ca (separability row/item) and O (jj item) would both touch `SKILL.md`. The claims file says "each claim lands disjoint paths". Recommend one integration owner applies all three hunks in one commit, or the jj item moves to a claim that already owns SKILL.md. Two claims editing one file is a merge risk, not a checker dependency; this seat does not decide it.
- **Exports for the checker (suggested, for Ca).** An export regex that would catch a C→Ca style coupling on the SKILL file is `check-claim-separability` (matches the row/item). Keep it out of C's bytes.
- **No cross-reference to fleet reports.** The jj item cites no `.ufo/` path; fleet audit `JjAuditKotodama.md` lives outside the lane and must not be cited from SKILL.md.

## 4. Tooling

No installs or updates performed by this seat. Nothing run from `tools/`.

## 5. Unrun checks (main agent to run after integration)

1. After Ca lands: `python3 -B tools/check-claim-separability.py reports/round-50/claims.json` → exit 0 (Ca `after_required`); confirm SKILL.md is in Ca `lands` if 2a/2b-separability are landed with Ca.
2. `grep -n 'check-claim-separability' SKILL.md` → rows 29-30 and checklist after line 534 only.
3. `grep -n 'refs/heads/main' SKILL.md` → one hit (jj item); `grep -n 'git rev-parse HEAD' SKILL.md` → only the negated mention.
4. SKILL.md markdown table: row has 4 cells (`awk -F'|'` not used by this seat; check visually or with the lane's provenance-audit if it parses tables).
5. Re-read the snapshot tag before applying; the `#5CC9` tag here is stale after any other edit.

## 6. Findings summary

- Ca: decision-row + checklist item proposed; must land with the separability tool (or be held). Ca `lands` omits SKILL.md today.
- O: one jj checklist item proposed; separable on base; cites landed sha as `main` bookmark, never HEAD or `@`.
- Coverage: no SKILL edit needed.
