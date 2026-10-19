# C05 — length and structure verification: the cartography entry is not landable as assembled

- Seat: `C05` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/cov/C05-length-contract.md` (this file)
- Mission (`reports/round-48/targets.json:23`): the draft is ≤~250 lines, has the full entry contract (all header fields + calibration + recheck + scope), and the worked example is internally consistent (one rule, stated once). Report line count + contract checklist.
- Non-author statement: I drafted none of the entry candidates. I measured the filed fences and the live partition; every number below is reproducible from the commands in §10.

**One-line verdict.** The **assembly of record is not executable against the filed bytes**: `W01:79` expects C01 to be body-only, but C01's fence carries its own H1 and seven head fields, so `W01:90-91`'s "join whole fences" produces **251 lines, two H1s and seven duplicated header fields** — over the 250-line ceiling by one. Measured separately, **C01 complete is 227 lines / 1 H1 / executable-bar PASS** and **C13 complete is 181 lines / 1 H1 / executable-bar FAIL** (`- sources:` has no bullets). Both fail the same worked-example control: **zero decision-record ids in §11**, which is C14's W4/W5 blocking class. No filed candidate passes both the executable admission bar and the claim-level contract; each needs **two local edits** (repairs in §8). The coverage axis does not move from this seat.

---

## 1. What was on disk when I measured

At my first check `reports/round-48/` held only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; by my measurement cut the `cov/` fragments had landed. I therefore verify the **filed bytes**, not a contract in the abstract. The candidates are the two fenced entry blocks plus the two possible assemblies:

| Artifact | Fence | sha256 (first 16) | Status |
|---|---|---|---|
| C01 complete | `C01-entry.md:69-298` (` ````markdown ` `) | `2a66774974b80d9b` | executable bar **PASS**; claim contract fails 2 legs |
| C13 candidate | `C13-scribe.md:100-282` (` ```markdown `) | `c93a54fccbeb0e17` | executable bar **FAIL** (0 source bullets) |
| C02 head | `C02-header.md:111-135` (` ````markdown ` `) | head block only, 23 lines | a head, not an entry |
| W01 join (C02 + whole C01) | per `W01:79,90-91` | `c39a4e286f732da8` | **not landable** |
| C02 + C01 stripped at first `## ` | per `C17:8` | — | 239 lines, 1 H1; W01's assembler cannot produce it |

Extraction used the same fence convention the fragments declare; `wc -l` semantics are newline counts, so these are the numbers the claim's counting command (`wc -l`) would print. C17 reports C01 as 228 (216 body + 12 head) and C13 as 193 with C02's header (170 body + 23); my fence counts are **227** and **181**, the C13 body count agreeing exactly and the C01 delta being one line at the head/body boundary. The deltas are ≤1 and immaterial to the verdict.

---

## 2. Measured baseline — live partition at `a01405d`

```
$ find corpus/knowledge -name '*.md' | wc -l              → 223
$ ls corpus/knowledge/culture-material/*.md | wc -l        → 25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
                                                          → No such file or directory
$ wc -l corpus/knowledge/culture-material/*.md | sort -n  → min 103 / median 149 / mean 150.2 / max 221
$ python3 -B reports/round-28/readme/sweep.py             → rows 223 files 223; missing 0;
    topic_mismatch 0; orphan_rows 0; header_drift {}; totals 223; footer 25/26/25/29/24/94; exit 0
$ sha256sum corpus/README.md                              → 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

Distribution legs used to set the contract (n = 25 culture-material entries), measured by script:

| Leg | min | median | mean | max |
|---|---:|---:|---:|---:|
| Lines | 103 | 149 | 150.2 | **221** |
| Words | 2,914 | 4,768 | 5,191.4 | **12,504** |
| Chars | — | — | — | **87,325** |
| H2 sections | 7 | 11 | — | 14 |
| H3 subsections | 0 | 0 | — | **3** (all in `ritual-garments.md`; partition total 3) |
| Header lines before first H2 | 7 | 12 | — | 42 |

`reports/round-28/readme/sweep.py:139` compares each index row to `topic_of(file)`, so the README row must be generated from the **adopted entry's** `- topic:` value; `topic_mismatch 0` is the baseline to preserve.

---

## 3. Length — the claim's two-leg contract, and what the candidates measure

Line count alone is gameable: funerary's 221 lines carry a 42-line header of very long lines and 12,504 words. A 250-line entry at that density is ~14,145 words, so the line ceiling must be paired with a mass ceiling. The contract:

| Leg | PASS | WARN | FAIL | Rationale |
|---|---|---|---|---|
| Lines (`wc -l`) | ≤221 | 222–250 | **>250** | inside the live band; the claim's ~250 is a tolerance, not a target |
| Words | ≤7,047 | 7,048–12,504 | **>12,504** | cannot out-mass the largest live entry; blocks line-collapse |
| Chars | — | — | **>87,325** | same guard, byte-level |
| H3 subsections | 0–3 | 4–10 | **>10** | r47 had 44 H3; the live partition total is 3 |
| H2 sections | 7–14 | >14 | <7 or numbering gaps | live band (max 14); contiguous `1..N` |

Boundary controls (executable, `.scratch` fixtures): a 250-line fixture exits **0 with a WARN**; 251 exits **1**; a 782-line over-build exits **1**; a 240-line / 14,341-word draft exits **1** on the mass leg. Direction is correct at both edges.

Candidate measurements:

| Artifact | lines | words | chars | ×221 | ×149 | words/line |
|---|---:|---:|---:|---:|---:|---:|
| C01 complete | **227** | 4,545 | 29,797 | 1.03× | 1.52× | 20.0 |
| C13 candidate | **181** | 5,370 | 34,367 | 0.82× | 1.21× | 29.7 |
| W01 join | **251** | 6,372 | 45,609 | 1.14× | 1.68× | 25.4 |
| C02 + stripped C01 | **239** | 5,369 | 37,357 | 1.08× | 1.60× | 22.5 |

Readings:

- **The join fails by one line** (251 > 250) before any content argument. It also fails H1 and duplicate-field checks, so the length is not the only blocker — but it means an assembler fix that merely removes one blank line would still land a two-H1 file.
- **C01 (227) passes the claim's ceiling** but becomes the partition's longest entry (221 → 227). It is 1.52× the median. If the integrator wants no new partition maximum, cut 6 lines; the claim permits the 227 but the discipline is better served at ≤221.
- **C13 (181) is the only candidate inside the existing band** (0.82× max, 1.21× median). Its 5,370 words are 18% above C01's 4,545 because its lines are denser; both are far below the 12,504 cap. C13's own "5,368 words" differs from my 5,370 by 2 — immaterial, and probably a fence-boundary token count.
- **C17's structural finding reproduces**: r47's 44 H3 vs the live partition's 3 is the over-build's real mechanism. All four r48 artifacts have **H3 = 0**, so the fragmentation class is not recurring.

---

## 4. The assembly defect — primary finding

`W01:78-79` defines the two byte sources: C02 contributes the **complete head block**, C01 contributes **body only (first line `## 1.`; no second H1, no head fields)**. `W01:90-91`: "Blocks are joined in manifest order with exactly one blank line between them and one trailing newline. No other bytes are added."

The filed C01 fence does not satisfy that precondition. It begins:

```
# Cartography and mapmaking — the survey-to-sheet register: …
- gap filled: the corpus owns space as cosmology, …
- topic: the map as a made instrument and a claim about space …
- sources:
```

Joining it to C02's head yields a file with **two H1s** (`:1`, `:25`), **two `- topic:` lines** (`:3`, `:28`), **two each** of `gap filled`, `sources`, `couples`, `verified-at`, `recheck`, `scope`, and **251 lines**. The checker reports seven `HDR-DUP` failures and `H1-COUNT 2`; the executable bar sees 4 source bullets but cannot rescue the file.

`C17:8` independently assumes a different rule — "the assembler must strip it and use C02's 23-line header" — and predicts 239 lines. That is the *correct* structural outcome, but **W01's assembler has no strip step**, and `W01:91` says no bytes other than one blank line are added or removed. The two apply documents disagree; the integrator cannot execute both.

Structural verdict on the join: **FAIL**. On the stripped variant (C02 head + C01 from line 13): **239 lines, 1 H1, 14 H2, 0 H3, 81 table rows** — passes every structural leg except the worked-example DR gap (§6), but requires a change to the assembly rule.

---

## 5. Structure contract — checklist and per-candidate result

Legend: ✓ pass, ✗ fail, — not applicable. The first column is the check ID the checker prints.

| ID | Check | C01 | C13 | Join | Stripped |
|---|---|:--:|:--:|:--:|:--:|
| S1 | exactly one H1 | ✓ | ✓ | ✗ (2) | ✓ |
| S2 | eight head fields, each once, ordered | ✗ (no `- source:`) | ✓ (source before couples; live precedent: funerary) | ✗ (7 dups) | ✓ |
| S3 | `- sources:` has ≥1 `  - ` bullet with a locator | ✓ (2/1) | ✗ (0 bullets) | ✓ (4/3) | ✓ |
| S4 | 7–14 numbered H2, contiguous `1..N` | ✓ (14) | ✓ (14) | ✓ (14) | ✓ (14) |
| S5 | H3 ≤3 | ✓ (0) | ✓ (0) | ✓ (0) | ✓ (0) |
| S6 | calibration/status marker | ✓ | ✓ | ✓ | ✓ |
| S7 | named gap sentence | ✓ | ✓ | ✓ | ✓ |
| S8 | decision record with unique ids | ✓ (`DR-CM-01..06`) | ✓ (`DR-CT-…`) | ✓ | ✓ |
| S9 | NON-CANON example declared, window anchored in its section | ✓ | ✓ | ✓ | ✓ |
| S10 | every prescriptive update cadence cites a DR id; no dangling id | ✗ (0 in §11) | ✗ (0 in §11) | ✗ | ✗ |
| S11 | every `- couples:` target resolves at the target directory | ✓ 14/14 | ✓ 17/17 | ✓ (at target) | ✓ |
| S12 | trailing newline; `wc -l` count stable | ✓ | ✓ | ✓ | ✓ |

Executable admission bar, run independently with `reports/round-19/audit/entry-audit.py`:

| Artifact | source bullets / with locator | couples | `quality_bar` |
|---|---|---|---|
| C01 complete | 2 / 1 | 14 resolved, 0 unresolved | **True** |
| C13 candidate | **0 / 0** | 17 resolved | **False** |
| Join | 4 / 3 | 0 resolved (scratch path; resolves at target) | False |

The live partition for scale: the executable bar passes **4/25** culture-material entries (`agrarian`, `funerary`, `furniture`, `writing-media`); the claim-level profile (all eight fields + single H1 + example DR ids) passes **0/25** fully — `writing-media` is the only entry that clears every hard check (with three warnings). The contract is therefore **prospective**: legacy non-compliance is not a defect and must not be reported as one.

---

## 6. Worked example — the one universal blocker

r47's B7 is the regression control. Its three incompatible Map A cadences are live at `C03-entry-c.md:123`, `:137`, `:150`; the example section (`:107-153`) contains **0** `DR-CT-` tokens, which is C14's F-2. My detector fires on the extracted r47 example (4 uncited cadences) and passes a corrected control in which each cadence cites `DR-CT-09` or `DR-CT-10`.

Both r48 candidates repeat the **F-2 half** of the defect, though not the three-way contradiction:

- C01 §11 (`:177-201`) states one rule, cleanly: `:191` "the register is re-surveyed when the levy year turns; a breach … changes the **next** levy-year assessment, never the current one." It then tests it at `:192` and lists counterfactuals at `:196-198`. The rule is stated **once** — B7 is not recurring. But the example cites **0** decision ids, and C01's decision rows are `DR-CM-01..06` (`:170-175`). C14's W4/W5 controls treat zero rule tokens in the example as a **blocking** failure (`C14:112-113`).
- C13 §11 (`:128-142`) states the rule once at `:138` ("re-surveyed only when the levy roll is re-cut; a breach is annotated … does not itself trigger a re-survey") and cites **0** decision ids.

**C14's PASS does not clear either example.** C14 passed `M01-example.md:28-54` (27 lines, sha `b6aaaf47…`, 14 `DR-CT` tokens) and says the gate "re-runs on the **assembled** entry, not on this fragment" (`C14:26`). The filed M01 example is a **third** example, not the one in C01 or C13. If the integrator adopts M01's example, that is a content substitution outside W01's two-source rule and must be re-run through C14 on the assembled bytes.

Minimal fix either way: append the relevant decision ids to the update-rule bullet (C01: `(governed by DR-CM-02 and DR-CM-06)` or the rows it actually instantiates; C13: `DR-CT-02`, `DR-CT-09`). Inline, zero new lines.

My checker's first pass accused C01 of **two** uncited cadences; the second was `:196`, a row in the counterfactual table "If the rule were…", not a statement of the entry's rule. That was a false accusation of the r47-B3 class and I removed it before this verdict: the finding is **one** cadence, not two.

---

## 7. Topic divergence — the README row depends on the candidate

The three heads carry **three different `- topic:` values**:

| Source | topic value length | sha256 (first 16) |
|---|---:|---|
| C01 | 1,045 | `23d94f4122d6ab88` |
| C13 | 1,094 | `922bf98a6678532a` |
| C02 | 766 | `bc7274f411cc6977` |

C02's value is **byte-equal to the r44 K02 §4.2 seed value** (verified: `v == seed_value`). C02's claimed digest `9424fb81c22…` reproduces exactly when the seed line is hashed **with its trailing newline** (the file-line convention); hashing the value alone gives `bc7274f4…`. That is a convention difference, **not** a digest defect — recording it here so no seat "corrects" a correct pin (r47-B3).

Because `sweep.py:139` compares the README row to `topic_of(file)`, the row must be generated from the **adopted** candidate. C13's own "1,103 characters" is the `- topic: ` line (1,094 + 9); C02's seed block is 775 incl. prefix. All three statements are internally consistent under their conventions. What is not acceptable is mixing: C02's head with C01's body produces two topic lines, and a README row copied from either without matching the landed entry fails `topic_mismatch` at the post-apply sweep.

---

## 8. Repairs — one candidate, two edits each

The integrator must choose **exactly one** byte source. The structural cost of each viable route:

| Route | Bytes | Edits | Post-fix lines (predicted) | Topic for the README row |
|---|---|---|---:|---|
| **A** | C01 complete | add `- source:` field; cite `DR-CM-*` in §11 `:191` | **228** | C01, 1,045 ch |
| **B** | C02 head + C01 body from `:13` | add `strip_head` to W01's assembler; cite `DR-CM-*` in §11 | **239** | C02 seed, 766 ch |
| **C** | C13 complete | convert `- sources:` to `  - ` bullets; cite `DR-CT-*` in §11 `:138` | **~190** | C13, 1,094 ch |

- **A** is the least byte surgery and already passes the executable bar; it creates a new partition maximum (228 > 221).
- **B** is what `C17:8` assumes; it preserves the r44 seed topic and lands at 239, but the assembler rule must change and C01's head claims (`- gap filled:` evidence) are replaced by C02's.
- **C** is the only route that stays inside the live band and is closest to the median; the sources rewrite is the only structural work (entry-audit counts only `  - ` bullets, `entry-audit.py:49-70`).

All post-fix line counts are **predictions**, not measurements. Whichever route is taken, the post-fix re-run is the certificate: `python3 c05-check.py --entry-dir corpus/knowledge/culture-material <entry>` must exit 0 with zero FAILs, and the post-apply sweep must print `rows 224 files 224`, `topic_mismatch 0`, exit 0.

---

## 9. The checker

Extract it from the fence below, then run it on the assembled entry. It is read-only, stdlib-only, and calibrated against the live partition at `a01405d`.

```
$ awk '/^`{3}python$/{f=1;next}/^`{3}$/{f=0}f' \
    reports/round-48/cov/C05-length-contract.md > .scratch/c05-check.py
$ python3 .scratch/c05-check.py --entry-dir corpus/knowledge/culture-material <entry.md>
$ python3 .scratch/c05-check.py --strict ...     # warnings fatal, for the apply gate
```

Calibration at the write cut (checker sha256 `c2a789eb121be841c67805f82a2a4238ba52ae8dc89a2b59afa7498d0c36fa9d`, 226 lines):

| Run | Result |
|---|---|
| 25 live culture-material entries | 0 PASS / 1 WARN (`writing-media`) / 24 FAIL — the claim-level profile is stricter than the partition |
| exact 250-line fixture | **exit 0**, one `LEN-LINES` WARN |
| 251-line fixture | **exit 1**, `LEN-LINES` |
| 782-line over-build | **exit 1**, `LEN-LINES` |
| 240-line / 14,341-word draft | **exit 1**, `LEN-LINES` + `LEN-WORDS` |
| duplicate-H1 fixture | **exit 1**, `H1-COUNT` |
| r47's real example bytes | **exit 1**, 4 uncited cadences (`C03:123,135,137,150`) |
| corrected r47 control (ids pinned) | **exit 0**, warnings only |
| C01 / C13 / join / stripped | **exit 1** each, causes in §5 |

Four false positives were found and fixed in the tool during calibration, and each is named because the r47 lesson is that a verifier's own accusation must be checked: (1) a bare `§N` beyond the entry's last section may name a **sibling file** (register-lexicon-ceilings' three `§13` refs name `register-strata-attestation.md`); downgraded to WARN, C04 owns adjudication. (2) The example window must anchor at the worked-example/decision-record section, not the header's first "NON-CANON" mention. (3) Counterfactual table rows ("If the rule were…") are not rule statements. (4) The line-count variable was shadowed by a loop variable, printing 39 for a 250-line file; fixed to `raw.count("\n")`.

**Known limitation, stated to prevent a false accusation:** the checker counts H1/H2/H3 and header fields **without parsing fenced code blocks**. Neither filed candidate contains a fenced heading; if a future entry quotes a heading inside a fence, inspect the flagged line before treating `H1-COUNT` as a defect (the r47-B3 rule: verify the accusation).

```python
#!/usr/bin/env python3
"""C05 length+structure contract checker for a cartography entry (read-only).

Usage: python3 c05-check.py [--strict] ENTRY.md [...]
Exit 0 = no FAIL; exit 1 = at least one FAIL.
Ceilings are derived from the live culture-material partition at HEAD a01405d
(n=25: lines 103/149/221, words 2914/4768/12504, chars max 87325, H2 7/11/14).
"""
import os, re, sys

FAIL, WARN = [], []
def f(code, msg): FAIL.append((code, msg))
def w(code, msg): WARN.append((code, msg))

REQ = ["topic", "gap", "sources", "couples", "source", "verified-at", "recheck", "scope"]
GAP_ALT = {"gap", "gap filled"}

def header_fields(lines):
    """(name, line_index, raw) for every '- field:' at column 0 before the first H2."""
    out = []
    for i, l in enumerate(lines):
        if l.startswith("## "):
            break
        m = re.match(r"^- (gap filled|gap|topic|sources|couples|source|verified-at|recheck|scope|calibration|status):", l)
        if m:
            out.append((m.group(1), i, l))
    return out

def check(path, entry_dir=None):
    global FAIL, WARN
    FAIL, WARN = [], []
    raw = open(path, encoding="utf-8").read()
    lines = raw.splitlines()
    NL = raw.count("\n")  # equals `wc -l` by definition
    if raw and not raw.endswith("\n"): w("EOL", "no trailing newline; `wc -l` undercounts by one")
    words = len(raw.split())
    chars = len(raw)

    # LEN
    if NL > 250: f("LEN-LINES", f"{NL} lines > 250 hard ceiling")
    elif NL > 221: w("LEN-LINES", f"{NL} lines exceeds live partition max 221 (claim allows ~250; justify in - verified-at:)")
    if words > 12504: f("LEN-WORDS", f"{words} words > live partition max 12504 (line-count gaming guard)")
    elif words > 7047: w("LEN-WORDS", f"{words} words exceeds 2nd-largest live entry (7047)")
    if chars > 87325: f("LEN-CHARS", f"{chars} chars > live partition max 87325")

    # H1
    h1 = [i for i, l in enumerate(lines) if re.match(r"^# ", l)]
    if len(h1) != 1: f("H1-COUNT", f"{len(h1)} H1 headings at lines {[i+1 for i in h1]} (must be exactly 1)")

    # header fields
    fields = header_fields(lines)
    for req in REQ:
        got = [x for x in fields if (x[0] in GAP_ALT if req == "gap" else x[0] == req)]
        if len(got) > 1: f("HDR-DUP", f"- {req}: appears {len(got)} times (lines {[g[1]+1 for g in got]})")
        if not got: f("HDR-MISSING", f"- {req}: missing")
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), NL)
    hdr_len = first_h2
    if hdr_len > 16: w("HDR-SIZE", f"header block {hdr_len} lines > 16 (live median 12)")
    # order: topic/gap before sources; sources<couples<source<verified-at<recheck<scope
    pos = {}
    for nm, i, _ in fields: pos.setdefault("gap" if nm in GAP_ALT else nm, i)
    chain = ["sources", "couples", "verified-at", "recheck", "scope"]
    for a, b in zip(chain, chain[1:]):
        if a in pos and b in pos and pos[a] > pos[b]:
            f("HDR-ORDER", f"- {a}: (line {pos[a]+1}) must precede - {b}: (line {pos[b]+1})")
    if "source" in pos and "verified-at" in pos and pos["source"] > pos["verified-at"]:
        f("HDR-ORDER", f"- source: (line {pos['source']+1}) must precede - verified-at: (line {pos['verified-at']+1})")
    for k in ("topic", "gap"):
        if k in pos and "sources" in pos and pos[k] > pos["sources"]:
            f("HDR-ORDER", f"- {k}: must precede - sources:")

    # sections
    secs = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := re.match(r"^## (\d+)\.", l))]
    if len(secs) < 7: f("SEC-COUNT", f"{len(secs)} numbered H2 sections < 7 (live partition min)")
    if len([l for l in lines if l.startswith("## ")]) > 14: w("SEC-COUNT", ">14 H2 sections (live partition max 14)")
    h3 = sum(1 for l in lines if l.startswith("### "))
    if h3 > 10: f("SEC-H3", f"{h3} H3 subsections > 10 (r47 fragmentation class)")
    elif h3 > 3: w("SEC-H3", f"{h3} H3 subsections > live culture-material max 3")
    nums = [s[1] for s in secs]
    if nums != list(range(1, len(nums) + 1)):
        f("SEC-SEQ", f"section numbers are {nums}, not contiguous 1..{len(nums)}")
    maxsec = max(nums) if nums else 0

    # bare section refs resolve (excluding refs to other files: a §N preceded by a .md` on the line)
    unresolved = []
    for i, l in enumerate(lines):
        for m in re.finditer(r"§(\d+)", l):
            k = int(m.group(1))
            ctx = l[:m.start()]
            if re.search(r"\.md`?\s*$", ctx):  # references another file's §
                continue
            if k > maxsec: unresolved.append((i + 1, m.group(0)))
    if unresolved:
        # NOT a hard fail: a §N may name a sibling file (r47-B3 false-accusation class).
        # Hard adjudication of anchors belongs to C04; this seat reports them for review.
        w("SEC-REF", "§N beyond §%d (check whether they name a sibling file): %s" % (maxsec, unresolved[:8]))

    # sources block: >=1 bullet, >=1 bullet carrying a locator (entry-audit.py:source_locators)
    src_bullets, in_src = [], False
    for l in lines:
        if re.match(r"^- sources:", l):
            in_src = True
            continue
        if in_src:
            if re.match(r"^- \w", l) and not l.startswith("  "):
                in_src = False
                continue
            if l.startswith("  - "):
                src_bullets.append(l)
    if not src_bullets:
        f("SRC-BULLETS", "no '  - ' bullets under - sources:")
    elif not any(re.search(r"https?://|\b(?:19|20)\d{2}\b|`[^`]*\.(?:md|py|json|yml|yaml|tsv)`|\b[0-9a-f]{16,64}\b", b) for b in src_bullets):
        f("SRC-LOCATOR", "no source bullet carries a locator (year, URL, path or digest)")

    # calibration + decision record + gap
    if not re.search(r"mainstream|contested|discredited|calibrat|\(to-verify\)", raw, re.I):
        f("CALIB", "no calibration/status marker")
    if not re.search(r"decision record|decision table|DR-[A-Z]{2}-\d", raw, re.I):
        f("DECISION", "no decision record/table or DR id")
    if not re.search(r"gap filled|residual gap|the gap this entry fills|no entry (covers|states)|not covered by", raw, re.I):
        f("GAP", "no named gap sentence")

    # worked example + single-rule test
    nc = [i for i, l in enumerate(lines) if re.search(r"NON-?CANON", l, re.I)]
    if not nc: f("EXAMPLE", "no NON-CANON worked example declared")
    if len(nc) > 2: w("EXAMPLE", f"{len(nc)} NON-CANON mentions; declare the example once")
    # example window: the NON-CANON line in a worked-example/fixture/decision-record section,
    # NOT the first passing mention in the header (r48 C05 v1 false positive on writing-media:31).
    def enclosing_heading(i):
        h = [j for j in range(0, i + 1) if lines[j].startswith("## ")]
        return lines[h[-1]] if h else ""
    if nc:
        scored = [(2 if re.search(r"worked (micro-)?example|fixture|demonstration|worked culture|worked case", lines[i], re.I)
                      or re.search(r"worked (micro-)?example|fixture|demonstration|decision record", enclosing_heading(i), re.I)
                   else 1, i) for i in nc]
        example_decl = max(scored)[1]
        start = example_decl
        if example_decl != nc[0]:
            w("EXAMPLE-AT", f"example window anchored at line {example_decl+1}, not the first NON-CANON mention")
        end = next((i for i in range(start + 1, NL) if lines[i].startswith("## ")), NL)
        ex = lines[start:end]
        # single-rule test: every prescriptive update cadence in the example must be
        # pinned to ONE rule id, or the example states the rule more than once (r47-B7).
        def in_counterfactual_table(i):
            """True for a | row under a header naming alternatives ('if the rule were')."""
            if not lines[i].lstrip().startswith("|"):
                return False
            j = i
            while j > 0 and lines[j - 1].lstrip().startswith("|"):
                j -= 1
            return bool(re.search(r"if the rule were|counterfactual|alternative", lines[j], re.I))
        presc = [(start + j + 1, l) for j, l in enumerate(ex)
                 if re.search(r"(re-?survey|\bupdate\b|revision)", l, re.I)
                 and re.search(r"(after|per\b|until|\bevery\b|not due|at the levy|\bwhen\b)", l, re.I)
                 and not l.lstrip().startswith("| DR-")
                 and not in_counterfactual_table(start + j)]
        if presc:
            # (a) every stated cadence must name the decision row it instantiates
            bare = [n for n, l in presc if not re.search(r"DR-[A-Z]{2}-\d\d", l)]
            if bare:
                f("EXAMPLE-RULE", f"{len(bare)} prescriptive update cadence(s) cite no DR id "
                                  f"(r47-B7 / C14-F2 class): lines {bare}")
            # (b) one id may not be restated with divergent cadence wording
            byid = {}
            for n, l in presc:
                for rid in re.findall(r"DR-[A-Z]{2}-\d\d", l):
                    byid.setdefault(rid, []).append(n)
            for rid, ln in byid.items():
                cads = {m.group(0).strip().lower() for n in ln
                        for m in [re.search(r"(after|per|until|at|every)[^.;|]{3,60}", lines[n - 1], re.I)] if m}
                if len(cads) > 1:
                    w("EXAMPLE-RULE", f"{rid} restated with {len(cads)} divergent cadence phrasings at lines {ln}; harmonise")
        # dangling DR ids used in the example
        defined = set(re.findall(r"DR-[A-Z]{2}-\d\d", raw))
        used = set(re.findall(r"DR-[A-Z]{2}-\d\d", "\n".join(ex)))
        if used - defined: f("DR-DANGLING", f"example cites undefined DR ids: {sorted(used-defined)}")
        # cadence-conflict surface (manual follow-up), printed for the reviewer
        cad = sorted({m.group(0).strip() for _, l in presc
                      for m in re.finditer(r"(?:after|per|until|at) (?:a|any|every|each|the) [a-z][a-z -]{2,40}", l, re.I)})
        if len(cad) > 1: w("EXAMPLE-CADENCE", f"{len(cad)} cadence phrases in the example; confirm they are form-scoped: {cad[:5]}")

    # couples resolution
    m = re.search(r"^- couples:\s*(.*)$", raw, re.M)
    if m:
        refs = set()
        def expand(s):
            mm = re.search(r"\{([^{}]*)\}", s)
            if not mm: return [s]
            out = []
            for part in mm.group(1).split(","):
                out += expand(s[:mm.start()] + part + s[mm.end():])
            return out
        for r in re.findall(r"[A-Za-z0-9_./{},\-]+\.md", m.group(1)):
            refs.update(expand(r))
        base = os.path.abspath(entry_dir) if entry_dir else os.path.dirname(os.path.abspath(path))
        kdir = os.path.abspath("corpus/knowledge")
        missing = []
        for ref in refs:
            cands = [os.path.normpath(os.path.join(base, ref)), os.path.normpath(ref), os.path.join(kdir, ref)]
            if not any(os.path.isfile(c) for c in cands): missing.append(ref)
        if missing: f("COUPLES", f"unresolved - couples: targets: {sorted(missing)}")

    # report
    status = "FAIL" if FAIL else ("WARN" if WARN else "PASS")
    print(f"{status}  {path}")
    print(f"      lines={NL} words={words} chars={chars} H2={len(secs)} H3={h3} header={hdr_len}")
    for c, msg in FAIL: print(f"      FAIL {c}: {msg}")
    for c, msg in WARN: print(f"      warn {c}: {msg}")
    return bool(FAIL)

if __name__ == "__main__":
    argv = sys.argv[1:]
    entry_dir = None
    if "--entry-dir" in argv:
        i = argv.index("--entry-dir")
        entry_dir = argv[i + 1]
        del argv[i:i + 2]
    args = [a for a in argv if not a.startswith("--")]
    strict = "--strict" in argv
    bad = 0
    for p in args:
        b = check(p, entry_dir)
        if strict and WARN: b = True
        bad += b
    print(f"\n{len(args)} file(s); {bad} failing" + (" (strict: warnings fatal)" if strict else ""))
    sys.exit(1 if bad else 0)
```

---

## 10. Verdict and what the integrator must do

**Length + structure verdict: FAIL as assembled; PASS-eligible per candidate with two edits.**

1. **Do not apply the W01 join.** It is 251 lines with 2 H1s and 7 duplicated fields. If W01's assembler runs unchanged, it writes an invalid entry.
2. **Choose route A, B or C** (§8) and record which. Do not mix heads and bodies.
3. **Fix the example's decision-row citations** (S10) — the only blocker common to every route, and the one C14's W4/W5 will re-test on the assembled bytes.
4. **Regenerate the README row from the chosen topic**; a row copied from C01 while C13 lands fails `topic_mismatch`.
5. **Re-run this checker and the post-apply sweep** as the certificate. The staged 224 sweep in `C13:324-343` is a prediction, not a delivery.

**Axis impact.** Coverage stays at 223 until one repaired candidate lands. Nothing in this report moves the axis; the honest record is that r47's over-build was correctly not repeated (181–239 lines vs 739/790), but the r48 assembly introduced a **new** class — a head/body contract mismatch — that the per-fragment audits could not see because each fragment was valid alone.

**Commands run** (all from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19): `git rev-parse HEAD`; `find`/`ls` census; `wc -l`, word/char/H2/H3/row counts by script; `python3 -B reports/round-28/readme/sweep.py` (exit 0); `python3 -B reports/round-19/audit/entry-audit.py <candidate> --json`; fence extraction with a Python regex; the checker suite in §9. No `reports/round-*/run-validation.py` was executed.

**Not verified by this seat:** the arithmetic and citation anchors inside either candidate (C03/C04 own those; I re-checked none of their numbers); the README bytes and staged sweep (C10/C11); the external shelf (C08); the freshness gate replay (O01/O04); whether M01's example is intended to replace C01 §11 (not stated in W01, which admits only two byte sources). Those are named as absent, not assumed.

**Write surface:** this file only — `reports/round-48/cov/C05-length-contract.md`. Disposable fixtures and extracted candidates live under `.scratch/c05/` (sanctioned `TMPDIR`); none is a deliverable. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. `git status --porcelain` at my cut: only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.
