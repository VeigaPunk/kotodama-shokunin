# R10-F04 — drift shard 04: SKILL.md lines 61-80

- **Round:** 10 (loop 1 of 3, build round 3 of 4) · **Axis:** F (freshness, lowest) · **Date:** 2026-10-17
- **Shard:** `SKILL.md` lines 61-80 — T4 clock separation / executable B4 (61-62), T5 WOLD band (62-65), the three cautions (67-73), Error-patterns header + rows 79-80.
- **Measurement window (UTC):** 2026-10-17T21:26Z → 2026-10-17T21:29:42Z (`date -u` bracket).
- **Revision:** HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f`. Declared round-10 baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749` verified an ancestor (`git merge-base --is-ancestor … ; echo $?` → `0`); `git diff --stat 9dc18ec1..HEAD -- SKILL.md` → **empty**, so SKILL.md bytes at measurement = baseline bytes.
- **Digest at measurement:** `SKILL.md` sha256 `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b` (`sha256sum`, 2026-10-17).
- **Scratch:** all scratch under in-lane `.scratch/` (`export TMPDIR=$PWD/.scratch` before every scratch-writing command; `/tmp` inode-exhausted per lane standing note).

## 1. Runnable commands found in the shard, re-run

Negative-claim sweep first ("no other runnable command text in the shard"):
`sed -n '61,80p' SKILL.md | grep -o '`[^`]*`' | sort | uniq -c` (2026-10-17) → **5 spans only**:
`D2L-BORROW`, `entry_stage`, `referent_available_from`, `language-contact.md:56-62`,
`costume-language-coupling-table.md:40`. None is a shell command; the shard's only executable
surface is B4 through `tools/d2-typed-labels.py`.

| # | Command (re-run from lane root) | SKILL locator | exit | output sha256 | verdict |
|---|---|---|---|---|---|
| 1 | `python3 tools/d2-typed-labels.py --selftest` | `SKILL.md:61` ("executable B4") | 0 | `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252` | current |
| 2 | `python3 .scratch/s04-b4-probe.py` (direct B4 control; source §4) | `SKILL.md:61-62` | 0 | `d84f3736656186e2862fcb713aa2dc698f1dc1fb0b6cd36e11cdcc4f64fa3a9f` | current |

1. Selftest: `selftest: 39/39 checks passed …`; deterministic — two runs `cmp`-byte-identical
   (`7231139c…` both; second run 2026-10-17T21:29:42Z, exit 0).
2. Direct B4 probe (assertions pass, exit 0; full output in §4):
   - negative `entry_stage=E0 < referent_available_from=E1` → `D2L-BORROW`, detail
     `entry_stage E0 precedes referent_available_from E1`, kind `fail`, exit 2, codes `[D2L-BORROW]`;
   - `E1 = E1` → exit 0, no findings; `E2 > E1` → exit 0, no findings.
   So the SKILL claim "`entry_stage` earlier than `referent_available_from` ⇒ `D2L-BORROW` FAIL"
   is executable exactly as written: check at `tools/d2-typed-labels.py:720-724`, rule stated at
   `reports/round-8/depth/design-spec.md:210-217` ("**B4** dating separation"), selftest covers the
   adjacent B3 substitution cases (`tools/d2-typed-labels.py:2749-2769`) while the clock case needed
   this probe.
   - Probe methodology note: the first probe run, with no packet inventory declared, also emitted
     `D2L-NATIVE` — `supplied form 'kas' carries symbols outside the declared inventory: ['a', 'k', 's']`
     — a synthetic-packet artifact (empty declared inventory; incidentally the SKILL.md:67-69 caution
     in action). The final probe declares `phonology: {consonants: [k, s, g], vowels: [a]}` so both
     positive controls are fully clean; exit-code assertion corrected to `2` after observing the
     fail-kind exit semantics (`tools/d2-typed-labels.py:812`).

## 2. Citation resolution (quotes name location)

| # | Citation (shard locator) | Claimed content | Observed at live tree (2026-10-17) | Verdict |
|---|---|---|---|---|
| 3 | `language-contact.md:56-62` (`SKILL.md:62-63`) | WOLD 1,460 meanings / 41 languages / ≈24% borrowing / none loan-free | `corpus/knowledge/linguistics/language-contact.md` line 58 "WOLD sampled 1,460 meanings in 41 languages…"; line 60 "Mean borrowing rate **≈24%** of the list; **no language in the sample is loan-free**"; extract (56-62) sha256 `2da1b08144dbb7e2d738525e7a0090256b8e82be3913fd8f74f17078ea418396`; file sha256 `52385e3d81f7d8f8eb1423d408a47bd12c968f1444fd9fc5d77a9c3e691cd409` | current |
| 4 | `costume-language-coupling-table.md:40` (`SKILL.md:72-73`) | "a translated or curatorial label never becomes an attested historical native word by repetition" | **line 40 is the table separator** `\|---|---|---|` (sha256 `5cb0682bc5eec6af7d1330c8d2b9fd3a4a50a5891bc5acdc31f8da06e2308dea`); the claim is at **line 43** (sha256 `1eab0e68779f06d826bde9d0ea0a2dd80edbf63616ec6f828483082529027e8b`): `| Term | Language, script, citation form, sense, speaker/register, source date | A modern curatorial label becomes an attested historical native word |`; file sha256 `dc7b723fc852eb48f31029d1ea0cb99be7742795ed4cd4ea33c62649ce314cb9` | **stale** |
| 5 | error row "rebuild from semantic fields" (`SKILL.md:79`) | pointer resolves | `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` exists (§4 field-by-field briefs line 46; §6 decision table line 100); sha256 `80b5e2c89fc8a97be343d32be4071ec40cc2a0e2aedac4a8abf2311b7175f65d` | current |
| 6 | error row "check color-symbolism variance table" (`SKILL.md:80`) | variance table exists | `corpus/knowledge/myth-symbol/color-symbolism.md`: §2 named-frameworks table lines 20-28; §3 line 45 "Neighbors share structure, drift values"; §4 cross-cultural white-means table lines 51-63; §11 calibration flags line 131; sha256 `b6830fe792b2074030632ab9af1bc2b17d4a3a5425f10309dc8a3fbf16c3f77c` | current |

No web-only citation exists in this shard (the five backticked spans above are all in-repo paths or
field names) — nothing to fetch; no access attempts applicable.

## 3. Stale item + fix (zero silent staleness)

**Item:** `SKILL.md:73` cites `costume-language-coupling-table.md:40`; the correct locator is `:43`.

**Genealogy (measured, not assumed):** at `291c714` and `49ac1a5` the "curatorial label" row was at
line **40**; `e1694ba` inserted 3 frontmatter lines (`- source:`, `- verified-at:`, `- recheck:`)
above the table (`git diff 291c714..e1694ba -- corpus/knowledge/synthesis/costume-language-coupling-table.md`
→ `3 insertions(+)`), shifting the row 40 → 43. The citation string first enters SKILL.md at the
same commit (`git log -S "costume-language-coupling-table.md:40" --oneline -- SKILL.md` → `e1694ba`
only), so it has never pointed at the claim in any committed revision — genuine line-shift drift,
not a content change.

**Fix:** replace `:40` with `:43`. **Duplicate:** the same stale token appears at `SKILL.md:96`
(adjacent shard-05 range, `grep -n "costume-language-coupling-table" SKILL.md` → lines 73 and 96);
same one-token fix — dedupe in the ledger.

**Routing:** R10-F04's write scope is this report only, so the fix is documented here (not applied)
and handed to R10-F15..F18 (stale-fixer seats). Ledger classification: **stale** → becomes
**stale-fixed** on the fixer's edit; verifiable by `grep -n "costume-language-coupling-table" SKILL.md`
showing `:43` at both sites.

## 4. Appendix — B4 probe source (re-runnable) and observed output

Probe source (executed from lane root as `.scratch/s04-b4-probe.py`; recreate anywhere and run
`python3 <path>`):

```python
"""R10-F04 shard-04 direct probe: B4 clock separation.

SKILL.md:61-62 claims: executable B4 — `entry_stage` earlier than
`referent_available_from` => `D2L-BORROW` FAIL.

This probe imports tools/d2-typed-labels.py (module import only; no CLI
mutation) and exercises the rule directly on synthetic packets, mirroring the
selftest's probe_packet/base_label shapes (tools/d2-typed-labels.py:2723-2735)
with a declared inventory added so positive controls can be fully clean.
"""
import hashlib
import importlib.util
import json
import sys

spec = importlib.util.spec_from_file_location("d2tl", "tools/d2-typed-labels.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def probe_packet(labels):
    return {"eras": ["E0", "E1", "E2", "E3"],
            "phonology": {"consonants": ["k", "s", "g"], "vowels": ["a"]},
            "layers": [{"name": "Salt-road trade layer",
                        "substitutions": {"bh": "p", "dh": "t", "sh": "s", "g": "k"}}],
            "typed_labels": labels}


def base_label(**over):
    label = {"id": "PROBE-01", "owner": "05-lexicon", "label_id": "L-99",
             "kind": "native-form", "text": "kas", "script": "Latn",
             "representation": "editorial-romanization", "scheme": "d2-roman",
             "status": "supplied", "era_ids": [], "issues": []}
    label.update(over)
    return label


BORROW = {"layer_ref": "Salt-road trade layer",
          "donor": {"immediate": "lowland stage 1", "ultimate": None, "carrier": None},
          "donor_form": "gas", "substitutions": {"g": "k"},
          "channel": "the salt road", "alternative_checks": []}

cases = [
    ("B4-negative", dict(BORROW, entry_stage="E0", referent_available_from="E1")),
    ("B4-positive-equal", dict(BORROW, entry_stage="E1", referent_available_from="E1")),
    ("B4-positive-later-entry", dict(BORROW, entry_stage="E2", referent_available_from="E1")),
]

results = {}
for name, borrow in cases:
    res = m.parse_typed_labels(probe_packet(
        [base_label(kind="borrowed-strata", text="kas", borrow=borrow)]))
    results[name] = {
        "exit_code": res["exit_code"],
        "codes": sorted({f["code"] for f in res["findings"]}),
        "borrow_findings": [f for f in res["findings"] if f["code"] == "D2L-BORROW"],
    }

out = json.dumps(results, sort_keys=True, indent=1)
print(out)
print("PROBE-SHA256", hashlib.sha256(out.encode()).hexdigest())

neg = results["B4-negative"]
assert neg["exit_code"] == 2, neg
assert any("precedes" in f["detail"] for f in neg["borrow_findings"]), neg
for pos in ("B4-positive-equal", "B4-positive-later-entry"):
    assert not results[pos]["borrow_findings"], results[pos]
    assert results[pos]["exit_code"] == 0, results[pos]
print("ASSERTIONS-OK")
sys.exit(0)
```

Observed output (file sha256 `d84f3736656186e2862fcb713aa2dc698f1dc1fb0b6cd36e11cdcc4f64fa3a9f`, exit 0):

```
{
 "B4-negative": {
  "borrow_findings": [
   {
    "code": "D2L-BORROW",
    "detail": "entry_stage E0 precedes referent_available_from E1",
    "kind": "fail",
    "where": "PROBE-01"
   }
  ],
  "codes": [
   "D2L-BORROW"
  ],
  "exit_code": 2
 },
 "B4-positive-equal": {
  "borrow_findings": [],
  "codes": [],
  "exit_code": 0
 },
 "B4-positive-later-entry": {
  "borrow_findings": [],
  "codes": [],
  "exit_code": 0
 }
}
PROBE-SHA256 8633aa72108f27144894a7cc3d632bc29460259fcf3626a318bed7737ac21c4c
ASSERTIONS-OK
```

## 5. Negative claims, with sweeps

- "No runnable command in SKILL.md:61-80 beyond B4" — sweep in §1 (5 backticked spans, 2026-10-17).
- "SKILL.md unchanged since declared baseline" — `git diff --stat 9dc18ec1..HEAD -- SKILL.md` → empty (2026-10-17).
- "No web citation in shard" — sweep in §1; all spans are in-repo paths or field names.

## Files

- `reports/round-10/drift/shard-04.md` — this file.
- `.scratch/s04-selftest.out`, `.scratch/s04-selftest-rerun.out`, `.scratch/s04-b4-probe.py`,
  `.scratch/s04-b4-probe.out` — disposable receipts (untracked).

No file outside `reports/round-10/drift/` (and the untracked `.scratch/`) was written by this seat;
no git state-mutating command was run.
