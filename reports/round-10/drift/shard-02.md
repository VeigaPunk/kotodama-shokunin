# Round-10 drift shard 02 — `SKILL.md:21-40`

- Worker: R10-F02 (drift shard 02), round 10, 2026-10-17. All commands below were
  re-run live on 2026-10-17 between 21:2x and 21:29Z.
- Scope: `SKILL.md:21-40` — decision table rows (21-29), "Label typing" section
  head with its three citations (31-38), label-typing table header (40).
- Revision at read: `git rev-parse HEAD` → `e3a1ec9435787328ac9f828f96cb6390e4916b8f`;
  `SKILL.md` sha256 `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`;
  slice `sed -n '21,40p' SKILL.md | sha256sum` →
  `7d3a225daec60f446f5bb16a6fca612c24f3b007c5fe9c6e87befdf3c0418d0a`.
- TMPDIR: in-lane `.scratch/` exported before every scratch write. Environment:
  `/tmp` is still inode-exhausted (`df -i /tmp` → `1048576 1048576 0 100% /tmp`,
  21:29Z) — nothing was written there.
- Protocol: re-run every runnable command in the shard (record exit + output
  sha256); resolve every path/line citation; web-only citations get a documented
  access attempt (none exist in this shard — all citations are in-repo); stale
  items are fixed or documented, never by rewriting filed report bytes.

## 1. Verdict summary

| # | Locator (`SKILL.md`) | Artifact / command | Exit | Output sha256 | Verdict |
|---|---|---|---|---|---|
| S02-01 | :35-36 | `python3 tools/d2-typed-labels.py --selftest` | 0 | `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252` | **current** |
| S02-02 | :35-36 | `python3 tools/d2-typed-labels.py --help` (flag existence) | 0 | `6e23d4350fc6f4cbd8d602623f449d1b793bdf27c21dc92c9688094565cdfc72` | **current** |
| S02-03 | :35 | path `tools/d2-typed-labels.py` | — | file sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | **current** |
| S02-04 | :36 | path `reports/round-8/depth/design-spec.md` §1 | — | file sha256 `84e4b4c19b0310f138b5bb53f3e4b3672cdc493fc83b555d912a9630984cc751` | **current** |
| S02-05 | :37 | path `reports/round-8/depth/skill-table-draft.md` | — | file sha256 `0e9aca3a84ee4da360090ba921bdef9023f38c46dc47d7e7552fc8b0a1dbcac5` | **current** |
| S02-06 | :38 | path `corpus/knowledge/synthesis/era-language-staging.md:108-124` | — | file sha256 `621b7a33c06ff15f5d179059e8ce856b7d22b51f5601787831956f4bf4a91da8` | **current** |
| S02-07 | :24-29 | decision-table named surfaces (15 surfaces → 18 files) | 0 | `18 OK / 0 MISSING` (sweep in §3) | **current** |
| S02-08 | :36 | design-spec §9 pinned hash for `era-language-staging.md` | — | pin `226e1104…` vs live `621b7a33…` | **stale-documented** (§4) |

Zero silent staleness: 7 items current, 1 stale item documented with evidence
and reason (filed report bytes stay frozen; this shard report is the new entry).

## 2. Commands re-run

### S02-01 — the shard's executable authority

Command as cited: `tools/d2-typed-labels.py` (`--selftest`).

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --selftest > .scratch/shard02-selftest.out 2> .scratch/shard02-selftest.err
echo "EXIT=$?"          # EXIT=0
sha256sum .scratch/shard02-selftest.out
# 7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252
sha256sum .scratch/shard02-selftest.err
# e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  (empty, 0 bytes)
wc -c .scratch/shard02-selftest.out   # 2354 bytes, 40 lines
```

Last line, verbatim: `selftest: 39/39 checks passed — the three shard control
matrices, the loader/parser malformed cases, the live-packet typing and
reconciliation cases, and the CLI emit/check/tamper controls; no file outside
the temporary directory touched`. Zero `FAIL`/`not ok` lines (`grep -c` → 0).

Determinism control: run twice, byte-identical (`diff` → no output, second run
sha256 identical to the first). The 39/39 count matches the round-9 admitted
value (`reports/round-9/d3/interop.md:26`), so the tool has not drifted since
round 9 either.

### S02-02 — flag existence

`python3 tools/d2-typed-labels.py --help` → exit 0; usage line lists
`[--selftest]` and the option help `--selftest, --self-test  fixture + control
matrix`. The `--selftest` spelling the SKILL.md section head promises exists.

## 3. Path citations resolved

- **S02-03 `tools/d2-typed-labels.py`** — exists, 2026-10-17 17:33:43 -0300,
  sha256 above. Design-spec §9's pins for this file (`13e82857…` → `623b5b1f…` →
  `56c0db14…`, the last "crashes, see §8.1") are all pre-repair values; the live
  file is the repaired one the spec's own §8.1 describes. Not staleness — the
  spec documents the repair; verdict current.
- **S02-04 `reports/round-8/depth/design-spec.md` §1** — file exists; `grep -n
  '^## ' …` → `80:## 1. Typed-label schema`. §1 is the typed-label schema, which
  is what the section head cites it as ("design authority … §1"). Current.
- **S02-05 `reports/round-8/depth/skill-table-draft.md`** — exists; sha256
  matches its own pin in design-spec §9 exactly. `grep -n 'LANDING-READY'` →
  `105:## 3. Label-typing decision table — LANDING-READY` and
  `223:## 5. Error patterns — LANDING-READY`; the draft still carries the two
  landing blocks the section head cites it for ("full receipts"). Seam check:
  the draft's six table rows are row-for-row identical to the landed table in
  `SKILL.md:40-47` except that the landed copy drops the draft's internal
  cross-ref `(§4.3)` — a landing adaptation to the draft's own section
  numbering, not content drift. (Rows 41-47 belong to the next shard's range;
  only the seam was checked here.) Current.
- **S02-06 `corpus/knowledge/synthesis/era-language-staging.md:108-124`** — file
  exists, 204 lines. The cited window covers the grounding the section head
  names: line 111 `## 7. Regnal names and period vocabulary: type every label`,
  lines 113-124 the complete label-type table (header + all 10 label rows,
  last = "Costume/style period"), preceded by the outcome/scene-test bullets at
  108-109. The range is the label-typing grounding, as cited. Current.

## 4. Named surfaces (decision table, `SKILL.md:24-29`) — S02-07

Sweep command (exit 0):

```sh
for f in corpus/knowledge/linguistics/{conlang-methodology,phonetics-phonology,morphological-typology,syntax-typology,semantic-fields-lexicon-building,semantics-pragmatics,naming-systems,historical-linguistics}.md \
         corpus/knowledge/myth-symbol/{comparative-frameworks,creation-myths-taxonomy,hero-journey-variants,trickster,symbolism-synthesis-method}.md \
         corpus/knowledge/culture-material/{dress-through-eras,costume-semiotics,garment-lexicon-crosslinguistic}.md \
         corpus/knowledge/synthesis/{era-language-staging,consistency-verification-checklist}.md; do
  [ -f "$p" ] ...
done
# → 18 OK / 0 MISSING
```

Every surface named in the table's "Correct surface" column resolves to a live
file: conlang-methodology, phonology/typology (phonetics-phonology +
morphological-typology + syntax-typology), lexicon by semantic field
(semantic-fields-lexicon-building), pragmatics (semantics-pragmatics),
comparative frameworks, creation/hero/trickster taxonomies, symbolism
synthesis, naming-systems, era-language-staging, historical-linguistics,
dress-through-eras, costume-semiotics, garment lexicon (crosslinguistic),
consistency-verification-checklist. Spot-read headings confirm the surfaces'
content matches their role (e.g. `conlang-methodology.md` opens "Pipeline at a
glance" with Stage 0 culture brief → Stage 4 syntax). No dangling surface.

## 5. The one stale item (S02-08) — documented, not fixed

Design-spec §9 pins `corpus/knowledge/synthesis/era-language-staging.md` at
sha256 `226e11049b7361d86c00e81e910a3d5982839e2e787faead0c9e9da4854152da`; the
live file is `621b7a33c06ff15f5d179059e8ce856b7d22b51f5601787831956f4bf4a91da8`.

Cause, evidenced: `git show e1694ba -- corpus/knowledge/synthesis/era-language-staging.md`
— the round-8 admission commit (2026-10-17 17:44:17 -0300) inserted **3 lines**
(`+ source: …`, `+ verified-at: …`, `+ recheck: …`) into the file's frontmatter
block at `@@ -3,6 +3,9 @@`, i.e. before the body. The spec itself labels its
hashes "read with `sha256sum` on 2026-10-17 (working tree, **pre-integration**)",
so this divergence is the drift-detection mechanism working as designed, not a
defect: the pinned value is the pre-integration state, the live value is
post-integration.

Disposition: **stale-documented**. Not fixed in place — `reports/round-8/depth/design-spec.md`
is a filed round-8 report and filed report bytes are never rewritten
(corrections are new entries; this file is that entry). The affected citation in
`SKILL.md` (`:38`) does **not** cite the pin and remains accurate (§3, S02-06).
No other stale item in the shard; the draft's §9 pin (`0e9aca3a…`) matches live
exactly.

Cross-reference note for the scribe (not a shard finding): the same §9 table's
`tools/d2-typed-labels.py` pins are pre-repair by construction (§2 above), and
`reports/round-9/baselines/registry.md` carries no `d2-typed-labels` row
(`grep -n` → no match, exit 1) — gate-registry coverage for this tool is the
registry shard's range, not shard 02's.

## 6. Ledger rows (machine-readable, for the F14 scribe)

```json
{
  "shard": "R10-F02",
  "scope": "SKILL.md:21-40",
  "date": "2026-10-17",
  "revision": "e3a1ec9435787328ac9f828f96cb6390e4916b8f",
  "skill_md_sha256": "2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b",
  "items": [
    {"id": "S02-01", "source_locator": "SKILL.md:35-36", "artifact": "tools/d2-typed-labels.py", "command": "python3 tools/d2-typed-labels.py --selftest", "exit": 0, "output_sha256": "7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252", "round10_verdict": "current", "note": "39/39 checks passed; stderr empty; two runs byte-identical; matches round-9 admitted value (reports/round-9/d3/interop.md:26)"},
    {"id": "S02-02", "source_locator": "SKILL.md:35-36", "artifact": "tools/d2-typed-labels.py", "command": "python3 tools/d2-typed-labels.py --help", "exit": 0, "output_sha256": "6e23d4350fc6f4cbd8d602623f449d1b793bdf27c21dc92c9688094565cdfc72", "round10_verdict": "current", "note": "--selftest flag exists as documented"},
    {"id": "S02-03", "source_locator": "SKILL.md:35", "artifact": "tools/d2-typed-labels.py", "command": "sha256sum tools/d2-typed-labels.py", "exit": 0, "output_sha256": "0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802", "round10_verdict": "current", "note": "design-spec §9 pins are pre-repair values the spec itself documents (§8.1)"},
    {"id": "S02-04", "source_locator": "SKILL.md:36", "artifact": "reports/round-8/depth/design-spec.md", "command": "sha256sum reports/round-8/depth/design-spec.md; grep -n '^## ' reports/round-8/depth/design-spec.md", "exit": 0, "output_sha256": "84e4b4c19b0310f138b5bb53f3e4b3672cdc493fc83b555d912a9630984cc751", "round10_verdict": "current", "note": "§1 'Typed-label schema' at :80 — the cited authority"},
    {"id": "S02-05", "source_locator": "SKILL.md:37", "artifact": "reports/round-8/depth/skill-table-draft.md", "command": "sha256sum reports/round-8/depth/skill-table-draft.md; grep -n 'LANDING-READY' reports/round-8/depth/skill-table-draft.md", "exit": 0, "output_sha256": "0e9aca3a84ee4da360090ba921bdef9023f38c46dc47d7e7552fc8b0a1dbcac5", "round10_verdict": "current", "note": "matches its own design-spec §9 pin; LANDING-READY blocks at :105 and :223; rows match SKILL.md:40-47 modulo dropped internal '(§4.3)' cross-ref"},
    {"id": "S02-06", "source_locator": "SKILL.md:38", "artifact": "corpus/knowledge/synthesis/era-language-staging.md", "command": "sha256sum corpus/knowledge/synthesis/era-language-staging.md; sed -n '108,124p' corpus/knowledge/synthesis/era-language-staging.md", "exit": 0, "output_sha256": "621b7a33c06ff15f5d179059e8ce856b7d22b51f5601787831956f4bf4a91da8", "round10_verdict": "current", "note": "window covers §7 header (:111) + full label-type table (:113-124) — the label-typing grounding as cited"},
    {"id": "S02-07", "source_locator": "SKILL.md:24-29", "artifact": "corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis}", "command": "for f in <18 surfaces>; do [ -f \"$f\" ] && echo OK || echo MISSING; done", "exit": 0, "output_sha256": "18 OK / 0 MISSING", "round10_verdict": "current", "note": "every 'Correct surface' name resolves to a live file"},
    {"id": "S02-08", "source_locator": "SKILL.md:36 (via design-spec §9)", "artifact": "reports/round-8/depth/design-spec.md §9 pin of corpus/knowledge/synthesis/era-language-staging.md", "command": "git show e1694ba -- corpus/knowledge/synthesis/era-language-staging.md", "exit": 0, "output_sha256": "pin 226e11049b7361d86c00e81e910a3d5982839e2e787faead0c9e9da4854152da vs live 621b7a33c06ff15f5d179059e8ce856b7d22b51f5601787831956f4bf4a91da8", "round10_verdict": "stale-documented", "note": "round-8 admission commit e1694ba inserted 3 frontmatter lines after the spec's explicitly pre-integration hash read; filed report bytes frozen — documented here, not rewritten"}
  ]
}
```

## 7. Self-check

```sh
python3 - <<'PY'
import json, re, pathlib
t = pathlib.Path("reports/round-10/drift/shard-02.md").read_text()
d = json.loads(re.search(r"```json\n(.*?)\n```", t, re.S).group(1))
print(d["shard"], len(d["items"]),
      sum(1 for i in d["items"] if i["round10_verdict"] == "current"),
      sum(1 for i in d["items"] if i["round10_verdict"].startswith("stale")))
PY
```

Expected: `R10-F02 8 7 1`. The shared round-10 acceptance runner
(`reports/round-10/run-validation.py`, owned by X03) did not exist in the tree
at write time; this shard's ledger rows are formatted for the F14 merge.
