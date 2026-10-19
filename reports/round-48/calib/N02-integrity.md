# N02 — successor-integrity verification (claim Ca)

- **Seat:** `N02` | role verifier | claim **Ca** (calibration) | round 48, loop 2, position 2
- **Baseline:** `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19T19:43Z), equal to `reports/round-48/claims.json:7` (`a01405d`)
- **Out path:** `reports/round-48/calib/N02-integrity.md` (this file; this seat wrote nothing else)
- **Non-author statement:** I authored none of `Ca02-overbuild.md`, `Ca06-process-row.md`, or the r47 fragments. Every check below is a fresh measurement at the baseline. Where another seat's output is cited, it is named as that seat's claim and separately re-measured where the command is available.
- **Subjects (digests pin what I read):**

| Subject | sha256 I audited | size |
|---|---|---|
| `reports/round-48/calib/Ca02-overbuild.md` | `2feb3a45c0e67555d97a9412650834b300b07db7b20126b95ea42f7999c07cbd` | 227 lines |
| `reports/round-48/calib/Ca06-process-row.md` | `54ce7f0cd573181839a0d420ea9d51f8f1dab00050660b9be01bfd53f8786908` (last observed; the file was rewritten at least four times during the wave — `0ac8375b…`, `c44e8177…`, `bf3ef46a…`, `54ce7f0c…`, all 238 lines; see N02-F5) | 238 lines |
| `reports/round-48/calib/queue-successor-r48.json` | **absent** — the applied file does not exist; Ca02 carries a fenced draft at `:81-162` | — |
| `reports/round-40/op/defect-queue-v2.json` (parent) | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` | 38 rows |
| `reports/round-47/calib/queue-successor-r47.json` (predecessor) | `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58` | 3 rows |

## 0. Verdict

**PASS with conditions on the successor-integrity contract; one merge-level defect that the integrator must resolve before filing.**

| # | Integrity leg | Verdict | Evidence |
|---|---|---|---|
| 1 | The over-build row references only **real filed paths/shas** | **PASS** | 19 path tokens (17 exist; 2 are declared future paths), 21 `path:line` citations are in range, 7/7 digests match, all nine B1–B9 anchors reproduce (§3–§4) |
| 2 | The parent `defect-queue-v2.json` is **pinned and unchanged** | **PASS** | same digest in worktree and at `a01405d` via `git show`; `git status --porcelain` empty; 38 rows (§1) |
| 3 | **No `fixed` row without a re-run command** | **PASS** | neither candidate row is fixed; both are `routed-with-owner`; the reclass path names commands and requires a NEW closing row; the parent's 10/10 fixed rows carry non-null verification (§5) |
| 4 | Id uniqueness / census integrity at merge | **FAIL as proposed** | `r47-entry-overbuild-defect-class` (Ca02) and `r48-entry-quality-not-gated` (Ca06) both own the r47 over-build class, each counts incidence 1, and each names the other as an alias/instance; both filed as rows would double-count the class (§6) |

Conditions: fix N02-F1 (a miscount in Ca02's verification recipe) and resolve the duplicate-class merge (§6). Neither condition changes the row's class, owner, or defect evidence.

## 1. Parent pin — `reports/round-40/op/defect-queue-v2.json` (PASS)

```
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  reports/round-40/op/defect-queue-v2.json

$ git show a01405d:reports/round-40/op/defect-queue-v2.json | sha256sum
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  -

$ git status --porcelain -- reports/round-40/op/defect-queue-v2.json
(no output)
$ git diff --name-only -- reports/round-40/op/defect-queue-v2.json
(no output)
```

Parsed: 38 rows; `Counter({'carried-with-owner': 28, 'fixed-with-evidence': 10})`; zero null ids. The pin Ca02 declares (`Ca02:79,89`) is the same digest. The parent's `notes` also records the rule that matters here: telemetry deviations are deliberately **not** defect rows, and the class vocabulary is `carried-with-owner` + `fixed-with-evidence`.

## 2. Predecessor pin and the absence the row closes (PASS)

```
$ sha256sum reports/round-47/calib/queue-successor-r47.json
9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58
$ git cat-file -e a01405d:reports/round-47/calib/queue-successor-r47.json && echo yes
yes
$ git show a01405d:reports/round-47/calib/queue-successor-r47.json | sha256sum
9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58  -
$ grep -n 'over.build\|790\|739\|R03\|B1' reports/round-47/calib/queue-successor-r47.json
exit=1
```

Its `rows[]` ids are exactly `r43-stale-premises`, `r44-resolver-hyphen-after-blank`, `manifest-ledger-two-schema-evolution` — three rows, **zero** over-build rows. The digest equals `reports/round-47/validation.json`'s `Ca.measurement.successor_sha256` (`9508b6aa…`). The class is therefore genuinely undispositioned, not a re-filing; Ca02's `predecessor_successor.over_build_row_present: false` is honest.

**Lineage observation (not Ca02's defect):** `reports/round-43/calib/defect-queue-v2-successor-r43.json` (`77f9d63e…`, 4 rows) **re-uses four parent ids** — `r39-review-findings-disposition`, `r38-O02-fragment-defects`, `r38-O08-fragment-defect`, `r38-O07-empty-fragment` — with changed classes. So across parent + r43 + r47 + this row the row count is 46 but the unique-id count is **42**. Any future "total queue rows" census must say which it is counting.

## 3. Ca02's fenced row — structure and references (PASS)

Extraction of the block at `Ca02-overbuild.md:81-162`:

```
parsed: True
envelope keys: schema, round, date, loop, artifact, parent, parent_sha256_at_assembly,
               parent_bytes_edited, predecessor_successor, baseline_commit,
               class_vocabulary, rows, application_gates, census_note
schema kotodama-defect-queue-successor-v1 | round 48 | baseline a01405d
rows 1 | findings 9 | row class routed-with-owner | v2 carried-with-owner
verification null? False
```

- **Id uniqueness:** `r47-entry-overbuild-defect-class` is absent from the 45 ids in the parent + r43 + r47 successors; none of its four declared aliases collides either.
- **Paths:** 19 distinct `reports/…|corpus/…|tools/…` tokens. 17 exist. The two that do not are intentional and named as such: `reports/round-48/calib/queue-successor-r48.json` (the apply path) and `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (the r48 C landing, correctly absent at this baseline).
- **Citations:** 21 `path:line` references; every one is inside its file's line count. Spot-resolution of the load-bearing ones returned the described content (`R03:96`, `R03:188-196`, `validation.json:9`, `R01-review.md:88-92`, `C11-scribe.md:67-78`, `C07-contract-audit.md:354`, `claims.json:43-45`, `targets.json:10`).
- **Digests:** 7/7 match live bytes:

```
OK  reports/round-47/review/R03-c-content.md          7e3e0880cfc7
OK  reports/round-47/review/R01-review.md             196328de7de3
OK  reports/round-47/validation.json                  17f8f1d4498f
OK  reports/round-47/cov/C11-scribe.md                4637ab101832
OK  corpus/knowledge/myth-symbol/cosmology-cosmography.md   165f292b9585
OK  corpus/knowledge/linguistics/naming-systems.md     d972a1d65e7a
OK  corpus/knowledge/culture-material/craft-artisan-lexicon.md  fd678d82fcc5
```

- **Arithmetic, recomputed:**

```
51 + 201 + 361 + 177 = 790
790/221 = 3.575   790/149 = 5.302
739/221 = 3.344   739/149 = 4.960
mean of 25 partition files = 3756/25 = 150.24
fence bodies: lines 790, words 20123, chars 127942, H2 15, table rows 240
body only:    lines 739, words 17601, chars 106997
```

The fence extraction reproduces the four part counts exactly (`C04:111-163` = 51; `C01:85-287` = 201; `C02:40-402` = 361; `C03:72-250` = 177), and the body figures reproduce R03 `:96`. `790 = 51 head + 739 body` is therefore a reconciliation, not a contradiction.

**N02-F1 (P2, should-fix before apply).** Verification item (12) at `Ca02:115` says:

> `grep -c '^| '` over `C03:92-104` → **7 lines (header, separator, 5 form rows)**

Measured:

```
$ sed -n '92,104p' reports/round-47/cov/C03-entry-c.md | grep -c '^| '
6
$ sed -n '92,104p' reports/round-47/cov/C03-entry-c.md | grep -c '^|'
7
$ sed -n '97,103p' reports/round-47/cov/C03-entry-c.md | grep -c '^| '
6
```

The separator `|---|---|---|---|` does not match `^| ` (no space after the pipe), so the stated command yields **6**, not 7. The underlying fact is right — the table at `:97-103` is header + separator + 5 form rows — but the paired command and parenthetical disagree, which is the B2/B4 shape this very row exists to prevent. Fix: write `grep -c '^|'` → 7, or keep `^| ` and say "6 (header + 5 rows; separator excluded)".

## 4. The nine defect anchors — independently reproduced (PASS)

I re-read each anchor rather than accepting R03 or Ca02 as authority:

| ID | Anchor | Measured at `a01405d` |
|---|---|---|
| B1 | `C02-entry-b.md:98` | text says "ten times"; `0.2 mm × 50,000 = 10 m`; `200/10 = 20` → 20×, defect real |
| B2 | `C04-entry-header.md:115` | `grep -rn 'cartograph' corpus/knowledge/ \| wc -l` → 2 (`cosmology:102`, `mesoamerica:58`); `:71` has no token |
| B3 | `C02-entry-b.md:36,:501` | `naming-systems.md:70` contains "a map is an archive of coups" verbatim; the accusation is false |
| B4 | `C02-entry-b.md:248,:421` | `craft-artisan-lexicon.md:44` is the Steel (Japan) row; ladder header `:54`, systems `:56-63`, rule `:65` |
| B5 | `C03-entry-c.md:79,:184` | `:79` says "§1–3"; `:184` says "§2"; typology is C01 `:238` (§4.1) |
| B6 | `C01-entry-a.md:298` | says "Provenance/charter (§9)"; C02 `:278` = §8 provenance, `:347` = §9 fossil |
| B7 | `C03-entry-c.md:123,:137,:150` | three incompatible update rules; `DR-CT-` count over `:107-152` = 0; `C14-example.md:11` = blocking FAIL |
| B8 | `C01-entry-a.md:90`; `cosmology:27` | `:27` defines cosmography as "how the world is drawn (maps)"; the disclaimers are `:71`/`:102` |
| B9 | `C03-entry-c.md:95-103` vs `C01:238-249` | table has 5 form rows against 8 typologized forms |

No anchor is invented, mis-cited, or stale. The `incidence.indicative_to_verify` figures also reproduce: `reports/round-42/cov/C01-entry-1.md` = 538 lines, `reports/round-44/cov/C01-entry-draft.md` = 485 lines, both correctly labelled as whole-fragment counts rather than entry bodies.

## 5. Fixed-row discipline (PASS — no premature "fixed")

- **Ca02's row:** `class: routed-with-owner`, `v2_class_equivalent: carried-with-owner`, `verification` non-null with 15 commands. Its `reclass_gates` G1–G6 each name a measurable output and G6 requires a **new** closing row (`fixed-with-evidence`), never an in-place edit.
- **Ca06's row:** also `routed-with-owner`; it does not flip the stale-premises row itself, but instructs the integrator to file a new closing row. The command it names reproduces:

```
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-43/claims.json \
      --checks reports/round-47/calib/r43-checks.json
  [C] STALE ... [Ca] FRESH 1/1 clauses hold
summary: 1 fresh, 2 stale ... REFUSE: claim(s) O, C ...
exit 1
$ ... --claims reports/round-47/claims.json --checks reports/round-47/calib/r47-checks.json
summary: 3 fresh, 0 stale ... exit 0
$ ... --claims reports/round-43/claims.json          # no overlay
summary: 0 fresh, 0 stale, 3 could-not-evaluate ... exit 3
```

- **Parent precedent:** all 10 `fixed-with-evidence` rows carry non-null `verification`; all 12 null-verification rows are `carried-with-owner`. The rule "a fixed row must carry a re-run command/output" is respected by both candidate rows and by the lineage.

## 6. Merge-level defect — two rows for one class (must be resolved)

This is the one blocking integrity finding.

| Artifact | Id | Class | Class claim |
|---|---|---|---|
| Ca02 `:107-109` | `r47-entry-overbuild-defect-class` | `routed-with-owner` | "dispositions ENTRY QUALITY for one instance and the pattern it exposes" (`:150`) |
| Ca06 `:86-89` | `r48-entry-quality-not-gated` | `routed-with-owner` | "the r47 build-quality failure and the r43 stale-premises failure are one process defect" |

They name **opposite canonicals**:

- `Ca02:172`: "If Ca06 mints a combined row, cite `r47-entry-overbuild-defect-class` as its entry-quality member; do not count two rows for one class."
- `Ca06:17`: "If Ca02 files it, the integrator folds Ca02's row under this one as `instance_of: r48-entry-quality-not-gated`; it must not become a near-duplicate."
- `Ca06:87` lists `r48-ca02-overbuild` among its **dedupe aliases** — but an alias cannot simultaneously be a second filed row.

Both rows state `incidence.entry_quality.count: 1`. If both are applied to `rows[]`, the class is counted twice and the defect census inflates — the failure the parent queue's census discipline exists to prevent.

**Integrity invariant:** exactly one `rows[]` entry may own the r47 over-build class; every other artifact id must be recorded as an alias or as an `instance_of` child and excluded from the class count.

**Resolution options (integrator's call):**

- **A — Ca02 canonical (recommended).** Apply `r47-entry-overbuild-defect-class` as the single entry-quality row. File Ca06's stale-premises closure as a **new** `fixed-with-evidence` row for `r43-stale-premises`, pasting the G1–G4 outputs above and citing the filed G5–G7 demonstrations. Carry Ca06's two `findings` as their own rows: `r48-use-record-not-durable` (`routed-with-owner`) and `r48-threshold-not-instrument` (`recorded`). Record `r48-entry-quality-not-gated` as an alias, not a row. Rationale: Ca02's row carries the nine instance findings verbatim and its class boundary already anticipates the merge.
- **B — Ca06 canonical.** Apply `r48-entry-quality-not-gated`; add `instance_of: r48-entry-quality-not-gated` to Ca02's row and exclude it from the class count (or fold its B1–B9 findings into Ca06's). Same closing rows for stale-premises and the two findings.

Either way, `census_note` must say "unique classes, aliases recorded", and the applied file must state the alias mapping explicitly.

## 7. Findings

| ID | Sev | Location | Finding | Fix |
|---|---|---|---|---|
| **N02-F1** | P2 | `Ca02:115` item (12) | Count is 6 under the stated `grep -c '^| '`, not 7; `^|` gives 7; the parenthetical wrongly includes the separator | Use `^|` → 7, or `^| ` → 6 with the separator noted |
| **N02-F2** | P3 | `Ca02:82-104` envelope | No `parent_sha256_recheck_after_assembly`, no `provenance` block, no `source_fragments` digest of Ca02 itself. The r47 predecessor carried all three | Add them to the applied `queue-successor-r48.json`; pin Ca02's final digest |
| **N02-F3** | P3 | `Ca02:161` | `census_note` "42" is correct for the three named artifacts, but the full lineage is 46 rows / 42 unique ids (the r43 successor re-uses four parent ids) | Say "42 unique ids (46 rows across four artifacts)" or name only the three artifacts |
| **N02-F4** | P2 | `Ca06:98` item (11) (line drifted from `:95` during the rewrite) | `grep -rln 'before_checks' reports/round-48/` now returns **6 files** (sibling reports that discuss the token); the claim "no output (rc 1)" no longer reproduces. The substance holds: `find reports/round-48 -name '*.json'` lists only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`, and O04 independently records the overlay only in `.scratch` | Rescope the command to the artifact class, e.g. `find reports/round-48 -name '*checks*.json' -o -name '*overlay*.json'` → empty |
| **N02-F5** | P3 | `Ca06` file | The file was rewritten at least four times during this wave (`0ac8375b…` → `c44e8177…` → `bf3ef46a…` → `54ce7f0c…`), same 238 lines, with line numbers moving (`verification` moved `:95` → `:98`). A successor that pins it must pin the apply-time digest, and any `path:line` citation into it is unstable by construction | Pin the final digest in the applied file; cite findings by id, not line |
| **N02-F6** | P3 | `Ca02:23,138` | The shown `grep -rln 'partition band\|length in partition' tools/` is a BRE with a literal `\|`; its zero is not discriminating (Ca04 F4 concurs). Re-measured with `-E`: 0; each alternative separately: 0 | Use `grep -rlnE 'partition band\|length in partition' tools/` |
| **N02-F7** | note | `Ca02:112` | `incidence.indicative_to_verify` is correctly labelled: 538/485 are fragment `wc -l`, not assembled bodies; both paths exist and the counts reproduce | none |

None of F1–F7 touches the row's class, owner, next_touch, or the nine defect anchors. F1 is the one to fix before apply because the row's subject is unverified counts.

## 8. Apply gate (runnable on `reports/round-48/calib/queue-successor-r48.json`)

The integrator runs this after writing the applied file. It encodes the three legs plus the merge invariant. Current status against the fenced draft: **PASS on legs 1–3; the merge check is the one that must be settled first.**

```python
import json, re, os, hashlib
P = 'reports/round-40/op/defect-queue-v2.json'
PS = 'dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907'
R = 'reports/round-47/calib/queue-successor-r47.json'
RS = '9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58'
FUTURE = {'reports/round-48/calib/queue-successor-r48.json',
          'corpus/knowledge/culture-material/cartography-and-mapmaking.md'}
d = json.load(open('reports/round-48/calib/queue-successor-r48.json'))
assert d['schema'] == 'kotodama-defect-queue-successor-v1'
assert d['round'] == 48 and d['baseline_commit'] == 'a01405d'
assert hashlib.sha256(open(P,'rb').read()).hexdigest() == PS == d['parent_sha256_at_assembly']
assert hashlib.sha256(open(R,'rb').read()).hexdigest() == RS == d['predecessor_successor']['sha256']
assert d['parent_bytes_edited'] is False
parent_ids = {r['id'] for r in json.load(open(P))['rows']}
pred_ids = {r['id'] for r in json.load(open(R))['rows']}
seen = set()
for row in d['rows']:
    assert row['id'] not in parent_ids | pred_ids | seen          # unique id
    seen.add(row['id'])
    assert row['class'] in {'fixed-with-evidence','routed-with-owner','recorded','could-not-recover'}
    assert all(row.get(k) for k in ('id','origin','class','owner','reason','next_touch','evidence','verification'))
    if row['class'] == 'fixed-with-evidence':                     # no fixed without output
        assert '->' in row['verification'] and len(row['verification']) > 80
    blob = json.dumps(row)
    for p in set(re.findall(r'(?:reports|corpus|tools)/[A-Za-z0-9_./-]+\.(?:md|json|py)', blob)):
        assert os.path.exists(p) or p in FUTURE, p
    for p, ln in set(re.findall(r'((?:reports|corpus|tools)/[A-Za-z0-9_./-]+\.(?:md|json|py)):(\d+(?:-\d+)?)', blob)):
        assert int(ln.split('-')[-1]) <= len(open(p, encoding='utf-8').read().split('\n')), (p, ln)
# merge invariant: exactly one row owns the r47 over-build class
ids = {r['id'] for r in d['rows']}
both = {'r47-entry-overbuild-defect-class', 'r48-entry-quality-not-gated'} <= ids
assert not both, 'both class ids filed as rows; pick one canonical and alias the other'
owners = [r['id'] for r in d['rows']
          if 'overbuild' in r['id'] or 'over-build' in r['id']
          or r.get('instance_of') == 'r48-entry-quality-not-gated']
assert len(owners) <= 1, f'duplicate class owners: {owners}'
# evidence durability: the declaration overlay must be filed, not only .scratch
assert not os.path.exists('reports/round-48/calib/queue-successor-r48.json') or \
       any(os.path.exists(os.path.join('reports/round-48', p)) for p in
           ('telemetry/r48-freshness-overlay.json', 'telemetry/r48-checks.json')), \
       'declaration overlay not durable (O04-F1)'
print('SUCCESSOR GATE PASS')
```

Note on the final assertion: it is a **condition of admission** for the round, not of the row. If the integrator chooses not to file the overlay, the row may still be admissible but the round's Ca verdict is not replayable from filed bytes (O04-F1).

## 9. What I did not verify

- **The applied `queue-successor-r48.json`** — absent at this snapshot; only the fenced draft exists. The gate above is the verification, not a result.
- **Ca06's final bytes** — the file was rewritten during the run (N02-F5); I audited `bf3ef46a…` and re-checked the same claims at `54ce7f0c…` (the only drift was line numbers and one unscoped command). A later rewrite must be re-gated against the digest actually applied.
- **The r48 C landing and the README fix** — other seats; no `cartography-and-mapmaking.md` exists at `a01405d`, and I did not edit or verify `corpus/README.md`.
- **Ca06's `r48-use-record-not-durable` global scope** — I measured absence under `reports/round-48/` only; a `.scratch` overlay exists (O04 records it as `7acbd8ca…`), and global absence is not claimed by either seat.
- **External bibliographic sources** — none consulted; the r47 Tier B shelf remains `(to-verify)` and is outside a disposition row.

## 10. Commands and write-surface statement

All from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19T19:43Z.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ sha256sum reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json \
            reports/round-43/calib/defect-queue-v2-successor-r43.json
dfc9265d… / 9508b6aa… / 77f9d63e…
$ git show a01405d:reports/round-40/op/defect-queue-v2.json | sha256sum
dfc9265d…
$ python3 -c "…parse parent…"
rows 38; Counter({'carried-with-owner': 28, 'fixed-with-evidence': 10}); null ids 0
$ grep -n 'over.build\|790\|739\|R03\|B1' reports/round-47/calib/queue-successor-r47.json
exit 1
$ python3 (fence extraction over the four r47 fragments)
790 lines / 20123 words / 127942 chars / 15 H2 / 240 rows; body 739 / 17601 / 106997
$ python3 (arithmetic)
51+201+361+177=790; 790/221=3.575; 790/149=5.302; 739/221=3.344; 739/149=4.960; mean=150.24
$ sed -n '92,104p' reports/round-47/cov/C03-entry-c.md | grep -c '^| '
6
$ sed -n '92,104p' reports/round-47/cov/C03-entry-c.md | grep -c '^|'
7
$ grep -rn 'cartograph' corpus/knowledge/ | wc -l
2
$ grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md
70: … a map is an archive of coups.
$ sed -n '44p;54p;65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
Steel (Japan) row / ladder header / design rule
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ python3 -B tools/harness/claims-freshness.py --selftest | tail -1
SELFTEST OK: registry 43/43 + seam 19/19 controls        (rc 0)
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-43/claims.json \
      --checks reports/round-47/calib/r43-checks.json | tail -2
REFUSE: claim(s) O, C …        (exit 1)
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-47/claims.json \
      --checks reports/round-47/calib/r47-checks.json | tail -1
summary: 3 fresh, 0 stale …    (exit 0)
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-43/claims.json | tail -2
REFUSE: … could not be evaluated …    (exit 3)
$ grep -rln 'before_checks' reports/round-48/
6 files (reports only; no overlay JSON)
$ find reports/round-48 -name '*.json'
claims.json / targets.json / telemetry/dispatch-declared.json
```

**Write surface:** this file only — `reports/round-48/calib/N02-integrity.md`. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git mutation, install, network, or in-tree round runner. The applied successor file was **not** written; that remains the integrator's act.
