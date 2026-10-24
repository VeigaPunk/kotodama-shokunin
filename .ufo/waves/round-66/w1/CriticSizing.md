# CriticSizing — sizing audit, round 66 (all three claims)

Question: is each after-state **one concrete value** a closure can re-derive with
one command over committed bytes? Verdict: C partially, O no, Ca mixed — and the
weakest leg is not where the claim text puts the weight.

## Finding 1 (C): "registry 701 -> 725+" is an unmeasurable interval, and its floor contradicts the claim's own arithmetic

Base is exactly 701 rows (`git show BASE:corpus/SOURCES.md | grep -cE '^\|\s*S[0-9]+\s*\|'` = 701), max base id is **S775** — S776 does not exist at base. So the round appends **25 rows** (S776 supersession row + S777–S800), giving an exact expectation of **726**, not "725+". Two defects:

1. **"+" is not a measurable target.** No leg in accept-c.py counts registry rows. SET/ROWS/RESTATE/HOSTS/LINK/CAPTURE iterate only `NEW_IDS` (accept-c.py:50,195); APPEND (accept-c.py:271-278) is a set-subtraction: `missing_old == 0` with `appended` merely printed. Concrete counterexample passing every leg: append a *second* row with an existing id, e.g. `| S600 | https://junk.example/x | docs | C | ... |` — SET checks uniqueness only for S777-S800, ROWS never sees it (not in NEW_IDS), APPEND sees it only inside `appended` (accepted by construction). Unbounded, unshaped growth — rows with wrong cell counts, tier Z, bogus urls — is exactly what "+" licenses, and the counter cannot distinguish 726 clean rows from 850 junk rows.
2. **The floor itself is wrong under the claim's own semantics.** If "725+" is meant as "701 + the 24 new ids", it silently drops the S776 row the same sentence claims; taken literally it asserts `count >= 725`, which a tree with **one** new id (724 + anything ≥1) satisfies — the predicate does not. The statement's after-value is neither the verified set (S776–S800 appended, nothing removed) nor a verified count.

The contrast inside the same sentence is telling: **"corpus 239 -> 240" IS concrete** — one command (`git diff --name-only BASE main -- corpus/knowledge`: exactly {new entry, games re-point} = +1 file over 239) re-derives it, enforced by FILE+NOHARM. The registry after-state is not given the same treatment.

- Axis: calibration (statement↔counter fit), coverage (unbounded row space).
- Smallest safe correction: pin the after-state as a **count invariant** — add a leg asserting `len(reg_lines) == len(base_lines) + len(appended)` AND `set(appended ids) == set(NEW_IDS) ∪ {S776}` (or whatever the declared additions are), i.e. appended-row shape checking for non-NEW_IDS rows; in claims.json replace "725+" with the re-derivable value (726) or state it as set-membership like the counter actually verifies.

## Finding 2 (O): "a verdict inside a round's budget" has no concrete value; the fixture bound is a proxy twice removed

"Inside a round's budget" names no number anywhere — not in claims.json, not in the tool, not in any receipt. What is actually measured:

- BOUND (accept-o.py:160-169): synthetic two-unit lane, sleeping acceptance, `--budget 0.5` → asserts exit 2 + PARTIAL + UNRESOLVED + no `<base>`. This proves **honest-partial semantics under a caller-supplied bound**, not that the tool returns inside *a round's* budget.
- The real round-66 manifest is never run by O's counter. The only real-manifest evidence is `telemetry/separability-real.txt`, which is a land of **Ca's** D4 — and that leg (accept-ca.py:157-161) greps free text (`^SEPARABILITY: \d+ findings$`, `acceptance_runs=\d+`, `"PARTIAL" not in`), with no recorded run args, no wall-clock, and no binding of the receipt to tool/manifest bytes.
- The upgraded tool emits **no elapsed/wall field** (`grep -nE 'elapsed|wall=|duration' tools/check-claim-separability.py` → none; SEPARABILITY_NOTE prints units/pairs/runs/skipped to stderr). So even a genuine receipt cannot show it ran "inside the bounded run" — D4's own leg text admits it.
- The only true wall-clock assertion in the whole O counter is FIXTURES `<180s` (accept-o.py:247) on the harness itself — a proxy for the proxy.

A closure re-deriving "the tool meets the round's budget" finds no bound and no measurement to compare against. The verifiable after-state is smaller and honest: *bounded invocations return exit-2 PARTIAL/UNRESOLVED verdicts on fixture lanes* — the claim's headline phrasing over-sizes it.

- Axis: calibration (claim overstates the measured property), operability.
- Smallest safe correction: either (a) make D4 pin the run — receipt must carry the verbatim argv + tool/manifest sha256 + a wall field the tool now emits (add `wall=%.1f` to SEPARABILITY_NOTE), with D4 asserting `wall <= 300` (the manifest's declared `--budget 300`); or (b) shrink the claim to what the fixtures prove. (a) is the better fit since the REC records land already owns the receipt.

## Finding 3 (Ca): D4 is verifiable only via a receipt a do-nothing seat can fabricate wholesale — and D3's claim is partially unverified

Ranked by fabrication resistance:

- **D4 — weakest: pure free-text receipt.** accept-ca.py:157-161 checks three regexes against `separability-real.txt`. A do-nothing seat commits a 2-line file `SEPARABILITY: 2 findings\nacceptance_runs=4` and the leg PASSes without the tool ever running — `acceptance_runs=` is even a *stderr* field (tool line 834), so the leg checks that someone pasted stderr into the file, nothing more. No tool sha, no manifest sha, no run args, no wall — nothing derivable from committed bytes distinguishes this from the real run. Also `SEPARABILITY: \d+ findings` accepts **any** count, so a 99-findings receipt passes though the manifest expects exactly the 2 declared Ca->REC findings.
- **D1 — receipt-verified core, one real anchor.** The disposition claim (live 200 pdf, quote verbatim, capture `20261024111013` byte-exact) is checked only as strings in `s753-recapture.txt` (accept-ca.py:89-99) — fabricable. The byte-verifiable part is only the citation flip (S776 ×1, S753 ×0 in the games entry, :100-105). So D1's *headline* is receipt-grade; its tail is real.
- **D3 — half-verified; the defect's actual claim is unchecked.** `existing == reported` (accept-ca.py:146-151) makes the listed report paths real committed bytes (good), but: the "per-seat status and last-error" half is checked by `re.search(r"(?i)(seat|report|status)", d3)` — vacuous, it matches the receipt's own header word "seat". And `existing == reported` lets a seat simply **omit dead seats** from the list: a trimmed 8-line receipt naming 8 files that exist passes while concealing the very dispatch failures R65-D3 demanded be retained. The disposition defeats the defect's purpose.
- **D2 — hardest to fake, but envelope-only.** Parent-of-carrier == stamped revision, tree line, and counter sha (accept-ca.py:108-142) re-derive from real git objects — a do-nothing receipt can't guess `stamped^{tree}`… except it can: `git rev-parse $(git log -1 --format=%H main -- <lands>)^` after the lands commit gives a forger every field, and the leg never compares the receipt's *verdict lines* to what the counter would print. Also `cblob = read(root, counter_path)` (:135) hashes the counter at **tip**, not at `stamped` — a post-receipt counter edit silently breaks the leg; `git show stamped:counter` is the correct read.

- Axis: calibration (records claims measured by records, not re-derivation).
- Smallest safe corrections: D4 — as Finding 2(a); additionally assert the finding count equals the manifest's `expected_findings` length. D3 — require a per-seat status token (`ok|dead` + last-error text for dead rows) and let `existing < reported` when missing seats are marked dead (retention ≥ existence). D2 — hash the counter at `stamped`, and grep the receipt for the counter's own `ACCEPT-*: PASS` line so a hand-stamped envelope can't pass.

## Cross-cutting

- Base numbers verified live: registry 701, corpus/knowledge 239, unowned-register census 0, main == base (wave mid-flight; mut-o stage and 8 w1 reports already exist).
- The pattern across all three: **counts that the counter never counts** (C's rows), **bounds that nothing bounds** (O's "round's budget"), **receipts standing in for re-derivation** (Ca's D1/D3/D4). Each claim has one well-sized leg (NOHARM, BOUND-on-fixture, D2) and the headline claims lean on exactly the unsized parts.

No tools installed (existing repo/toolchain sufficient).

Report: .ufo/waves/round-66/w1/CriticSizing.md
