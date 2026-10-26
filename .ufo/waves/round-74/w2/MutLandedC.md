# MutLandedC — WAVE 2 (falsify, hyaku run 7): 13-mutant battery on landed claim C

Seat: MutLandedC-2 (leaf). Date: 2026-10-25. Lane: kotodama-shokunin.
Target: the landed claim-C bytes, graded by `reports/round-74/accept-c.py`.

- lands (clone-local `main`): `c4bf61a8d722f9168ce0fd8021a6261c000610c5`, tree `29c8c147c948b9fe`
- freeze: `00c408a0af2fa5ddf65af2224152ce258b26d896`
- counter self-sha256: `8d30487fa4692261edfee549d2ba07517fc8b3c9fc4f5af5f0562a504ca5433a`
- scratch clone: `/tmp/MutLandedC/cloneONIOai` (fresh `mktemp -d`, `git init` toplevel check passed, `git clone --no-hardlinks`, `main` pinned to lands). Every mutant is ONE commit inside the clone only (fixture identity `-c user.name/-c user.email`), tagged `mut-M1`…`mut-M13`; counter always run with `--lands <mutant-sha> --freeze 00c408a0… --fleet-root /home/vgpnk/Projects/shokunin`.

## Baseline (pristine lands) — PASSED first

```
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND /
CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK / FROZENCFG / INDEX
ACCEPT-C-74: PASS legs=13/13
EXIT=0
```
(header: stamped=evaluated=measured=c4bf61a8…, tree 29c8c147…, config sha256 270e3179…)

## Result table

| M | mutation (one commit each) | leg expected | leg(s) that fired | survived | mutant sha | tree |
|---|---|---|---|---|---|---|
| M1 | delete `- source: S882` line from base entry | ROWS | ROWS (`S882 used-by=[...] (want exactly [])`) | N | 8903c55f | ef7e161f |
| M2 | swap S881 row URL → tuduku URL | ROWS | ROWS + REPOINTED + EVIDENCE + COLLCHECK | N | 663702b1 | 07819828 |
| M3 | widen S882 used-by cell | ROWS | ROWS (want exactly [base entry]) | N | 0094fc41 | 68571f18 |
| M4 | corrupt 1 character in S881 window line | EVIDENCE | EVIDENCE (window-sha256 83e313a946d1cbec != recomputed bd0e5a950dd13eac) | N | 06bb478f | adac4916 |
| M5 | Gate quote → plausible phrase NOT in its window | EVIDENCE | none | **YES** | 8b069a6b | 06731c20 |
| M6 | delete `## Quarantine` section (lesson) | REJECTS | REJECTS (`no ## Quarantine section`) | N | e2ee1474 | 081bea38 |
| M7 | delete README culture-material index row | INDEX | INDEX (`0 index rows (want exactly one)`) | N | 893b3562 | 99ac79fa |
| M8 | last README footer total 249→250 | INDEX | INDEX (`250 != the 249 .md files`) | N | 6a24d43a | 5cc547f4 |
| M9 | append fifth registry row S885 (11 cells) | ROWS | ROWS (`added [...S885] (want [...S884])`) | N | 2ac1a96d | b89382ec |
| M10 | S877 tier cell B→C (non used-by) | ROWS | ROWS (`in-place change outside the used-by cell`) | N | 9dba82ed | 32be511f |
| M11 | delete narrative-structure-frameworks family row from rejects list | REJECTS | none | **YES** | cd09f22d | d6508fef |
| M12 | entry body → 600+ words of filler under byte-identical header | (depth probe) | none | **YES** | 11f9580d | bef72fb3 |
| M13 | edit `reports/round-74/claims.json` in lands tree | FROZENCFG | FROZENCFG (`differs from the frozen bytes`) | N | c7b136f8 | f76aafbf |

10/13 killed; 3 survivors (M5, M11, M12). The attack FAILED on 10 of 13 surfaces — the claim's ROWS/REPOINTED/EVIDENCE-hash/REJECTS/INDEX/FROZENCFG machinery held.

## Findings

### F1 — HIGH (survivor M5): EVIDENCE "quote in window" is satisfied by ANY quoted span of the admit row

Attack: replaced the S881 Gate quote cell with `「自然環境が社会の仕組みを決め、文化が登場人物の毎日の選択を左右する。」` (37 chars, 1 token — shape-legal), a phrase absent from the S881 evidence window. Counter output (mutant 8b069a6b):

```
LEG PASS EVIDENCE
ACCEPT-C-74: PASS legs=13/13
EXIT=0
```

This violates the frozen EVIDENCE leg as written ("the Gate quote occurs in the stored window after NFKC and whitespace folding") and the kill_rule ("a committed evidence window containing the Gate quote").

Root cause (accept-c.py at lands): EVIDENCE builds `spans = [s for s in quoted_spans(grow) if quote_ok(s)]` (`:1257`) where `grow` is the WHOLE admit row line (`_gate_admit_row`, `:667`) and `quoted_spans` (`:420`, QUOTE_RE `:205`) extracts every `"…"`/`«…»`/「…」 span anywhere in the row — then `:1262` passes on `any(...)`: `if not any(nfkc_ws(s) in nfkc_ws(window) for s in spans)`. The row's source-title span `世界観の作り方` and locator span `3. 外側の層へ因果をつなぐ` both occur in the stored window, so any quote-cell forgery of legal shape passes. The committed junk-landing control ("Gate quote not in the evidence window" → FAIL) does not exercise this because its fixture row evidently carries no other in-window span.

Proposed fix: extract spans only from the quote column of the admit row (parse row cells; take the cell under the `quote` header), and require that span (all of it) in the window after NFKC+whitespace folding; keep locator/title cells out of the span set.

### F2 — MEDIUM (survivor M11): REJECTS family coverage is name-presence anywhere, not a rejects row with reason+flip

Attack: deleted the entire rejects-table row `| narrative-structure-frameworks (base plus 4 amendments) | 5 | … | … |` from `corpus/lessons/round-74.md` (its reason and flip went with it). Counter output (mutant cd09f22d): `ACCEPT-C-74: PASS legs=13/13`, `EXIT=0`.

Frozen REJECTS leg requires "each refused family and file in rejects, each with reason and flip". Implementation (`leg_rejects`, def at accept-c.py:1279; loop at `:1318`): `for spec in cfg["refused_files"]: if not any(name in text for name in _refused_names(spec))` — substring presence of the family name anywhere in the lesson. The name recurs at `corpus/lessons/round-74.md:188` (the "Routed to round 75" section), so the table row carrying reason+flip is deletable without detection. A family whose name appears only in the table would be caught; this one is not.

Proposed fix: for each frozen `refused_files` spec, require a rejects-table row naming it whose remaining cells carry a non-dash reason and a non-dash flip (the leg already parses Gate tables this way), instead of name-presence in free text.

### F3 — LOW (survivor M12; disclosed residual, recorded as coverage fact): entry-body content is unverified

Attack: replaced the amend entry's entire body (all six sections, every quotation and locator) with 612 words of content-free filler (body measured from tag `mut-M12`); header lines 1–14 byte-identical (sha256 of lines 1–14 `a1b088b2…` before == after; diff hunks start at line 15). Counter output (mutant 11f9580d): `ACCEPT-C-74: PASS legs=13/13`, `EXIT=0`.

The frozen ENTRIES leg declares itself "a length-and-shape gate only — content fidelity is carried by GATE, EVIDENCE and the non-author re-open", so the survivor is inside the claim's own stated scope. The coverage fact the probe adds: per F1, GATE+EVIDENCE bind only the Gate-table quotes to windows — no automated leg binds the entries' prose to any source, so the disclosed "content fidelity" carriers are automatic for nothing in the entry bodies; only the human re-open carries it. A header promising a build order over an empty body ships green.

Proposed fix (round owner's call; seats do not amend the frozen rule): a cheap binding leg such as requiring each entry body to contain ≥N quoted spans that each occur in some cited row's committed window, or requiring the section headings named in `source:` lines to exist in the body.

### F4 — LOW (observation, not a mutant): junk-landing receipts the frozen claim cites do not exist at lands

`git ls-tree --name-only c4bf61a8… -- reports/round-74/telemetry/` lists 9 files and no `junk-c.txt`/`junk-ca.txt`/`measures-*.txt`; those appear first in post-lands commit `1d7add3` (13 files). The frozen `do_nothing_control` of both claims names `reports/round-74/telemetry/junk-c.txt`. The tasking discloses post-freeze telemetry/report-side commits, so this is disclosed rather than defective, but at the graded lands the cited control receipts are absent. No fix needed beyond landing order discipline; noted for the wave's records.

## Hygiene and restoration

- Fetch hygiene: no network fetches were made (all probes local git).
- Tooling authorization: nothing installed or upgraded (no pacman; git and python3 preexisting sufficed).
- No file outside `/tmp/MutLandedC/**` and this report was written; the lane's git state/index was never touched (read-only git outside the clone).
- Restoration: after M13, `git reset --hard c4bf61a8…` inside the clone — `git status --porcelain` empty; HEAD `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; `HEAD^{tree}` `29c8c147c948b9fe03af8f092ac92028a23fed56` (== the pre-battery tree); `git diff --stat <lands> HEAD` empty. Mutant commits remain addressable as tags `mut-M1`…`mut-M13` in the disposable scratch clone only.
