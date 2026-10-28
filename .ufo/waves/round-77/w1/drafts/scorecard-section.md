DRAFT (seat ScribeScorecard, round-77 wave 1) — section to APPEND to `SCORECARD.md` after the round-76
material. Append-only: nothing above is edited. Shape follows `## Axes — round 76` (prose paragraphs, a
fenced counting command, inline acceptance command, closing verdict line) and `## Corrections — round 76`
(prose paragraph + four-column table). Every `<L1-FILL…>` token is replaced at the lands commits; the only
measured counts written here without a fill marker are the base counts, measured by this seat with the
command the coverage paragraph quotes. If Ca lands before C, append the Corrections block first as rounds 73–76 do; the
two blocks carry no cross-order binding. No trend scalar; verdicts are author-side.

---

## Axes — round 77 (2026-10-27, hyaku run 10, kotodama), author-side verdicts

**Coverage / claim C — <L1-FILL: verdict at C-lands; the claims' target is `PASS legs=N/N` and no score delta unless that line prints>.** Base 211f952: 253 knowledge files, 820 registry rows (newest row S896; both counts measured at draft time with the command below). C lands <C-lands>: <L1-FILL: 254 per the claims' target> files, <L1-FILL: 822 per the claims' target> rows (S897, S898 — the one adopted entry `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`, its staged→lane document map in `reports/round-77/claims.json` `row_set`). The frozen counter reports `<L1-FILL: ACCEPT-C-77: PASS|FAIL legs=N/N>`; the claims' leg list is FROZENCFG, STAMP, LEDGELIST?, COUNTS, ENTRIES, ROWS, APPENDONLY, COLLCHECK, INDEX, EVIDENCE, GATE, REJECTS, CENSUS, GROUND, RECEIPTS (the exact set is frozen with the counter; `LEDGELIST` counts only if the counter carries it). Counting command:

```sh
for rev in 211f9526800906e0c585d878d265c37e5e090c15 <C-lands>; do
  printf '%s knowledge=' "$rev"
  git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only "$rev" corpus/knowledge | grep -c '\.md$'
  printf '%s rows=' "$rev"
  git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show "$rev:corpus/SOURCES.md" | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
done
```

Observed output: `211f9526800906e0c585d878d265c37e5e090c15 knowledge=253` and `211f9526800906e0c585d878d265c37e5e090c15 rows=820` (this seat, at draft time); `<L1-FILL: the same two lines printed at C-lands>`. Acceptance command: `python3 -B reports/round-77/accept-c.py --root . --lands <C-lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin --work /fast/scratch/hyaku/kotodama-r77/<L1-FILL: seat>` — the claims name the counter path and its leg set but not its argv; the flags above are round-76's (`reports/round-76/accept-c.py`), inherited pending the frozen round-77 parser. Evidence: `reports/round-77/telemetry/census-start.txt` (start receipt), `<L1-FILL: measures-c.txt, junk-c.txt, census-end.txt>`; `corpus/lessons/round-77.md` `## Gate`.

**Calibration / claim Ca — <L1-FILL: verdict at Ca-lands; the claims' target is `PASS legs=N/N`>.** The frozen ledger `reports/round-77/ledger.json` has `<L1-FILL: N, ≥10 per the claims>` unique pairs (`<L1-FILL: P>` ANNOTATE / `<L1-FILL: Q>` REPAIR), frozen at the freeze commit with `reports/round-77/claims.json`; ANNOTATE pairs may state only inside the frozen allowlist (LOG.md, SCORECARD.md, `corpus/lessons/round-75.md`, `corpus/lessons/round-76.md` — `corpus/README.md` is REPAIR-only) and REPAIR lands only on the frozen mutable set {`corpus/README.md`, `SKILL.md`, `SHONEN.md`}. Measured at Ca-lands `<Ca-lands>`, freeze `<freeze>`, combined C-lands `<C-lands>`: `python3 -B reports/round-77/accept-ca.py --root . --lands <Ca-lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin --combined <C-lands> --main <Ca-lands> --work /fast/scratch/hyaku/kotodama-r77/<L1-FILL: seat>` → `<L1-FILL: ACCEPT-CA-77: PASS|FAIL legs=N/N>`. Legs from the counter's table (LEGCOUNT-checked): LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, SEPARABLE, COMBINED, RECEIPTS, FROZENCFG, STAMP, LEDGELIST. Evidence: `reports/round-77/telemetry/<L1-FILL: measures-ca.txt>`, `reports/round-77/ledger.json`, and the `## Corrections — round 77` table.

**Depth / operability / freshness / adjacency — unchanged; no score delta.** These four axes carry no claim and no move this round; freshness axis-moves stay paused under the open kotodama round-11 L0 row (`.ufo/l0-questions.md:47`: "Freshness axis-move claims are paused until ruled."). <L1-FILL: amend only if one of the four moves by the lands commits.>

<L1-FILL: closing verdict line — name which frozen counters printed PASS; if neither does, write "Neither frozen acceptance counter passes. … neither axis score is advanced." exactly as the round-76 section does.>

## Corrections — round 77

Append-only record (hyaku run 10, kotodama round 77). Claim Ca ledger `reports/round-77/ledger.json` has `<L1-FILL: N, ≥10 per the claims>` unique pairs (`<L1-FILL: P>` ANNOTATE, `<L1-FILL: Q>` REPAIR), frozen with `reports/round-77/claims.json`. Measured at Ca-lands `<Ca-lands>`, freeze `<freeze>`, combined C-lands `<C-lands>`: `python3 -B reports/round-77/accept-ca.py --root . --lands <Ca-lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin --combined <C-lands> --main <Ca-lands> --work /fast/scratch/hyaku/kotodama-r77/<L1-FILL: seat>`; its leg line `<L1-FILL: ACCEPT-CA-77: …>` is quoted as printed. The rows below are the frozen ledger's ANNOTATE pairs projected one per pair at the freeze (REPAIR pairs are named in prose, never as rows): each row carries the pair id, the base stated token, the observed token and the pair's own re-derivation argv, which the counter re-runs with the pair's parser and requires to return the observed token.

| id | old token | new token | re-derivation command |
|---|---|---|---|
| <L77-NN> | <L1-FILL: stated token at base> | <L1-FILL: observed token> | <L1-FILL: pair's rederive argv verbatim> |
