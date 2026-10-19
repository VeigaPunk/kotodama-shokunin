# C10 — Staged 224-tree sweep (sweep verifier)

- **Seat:** C10 · **Claim:** C (coverage) · **Out:** `reports/round-47/cov/C10-sweep.md`
- **Baseline:** HEAD `6e9a30d` (short) — declared in `reports/round-47/claims.json`
- **Verdict:** **PASS (staged mechanics).** The projected post-landing state measures
  224 rows == 224 files, footer `224` / `25/26/26/29/24/94`, all sweep legs empty,
  exit 0. The post-landing README **sha** is conditional on C09's final prose (see §5);
  the measurement fields are not.
- **Scope limit:** at seat time `reports/round-47/cov/` was empty — the C draft body,
  header, and README prose were not yet filed. This seat verifies the *index mechanics*
  against a declared fixture, not the landing bytes or the entry's content.

## 1. Live state measured (instrument health + collision)

Commands run from `/home/vgpnk/Projects/shokunin/kotodama-shokunin` with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ python3 -B reports/round-28/readme/sweep.py --selftest
... 12 lines ...
selftest: 12/12 checks passed          # exit 0

$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25,
       "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", ..., "total": 223,
        "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
# exit 0
```

Live README digest matches `sha256sum corpus/README.md`:
`7c788a1d…1ef31cdcd`. The instrument's own live leg and all 12 controls pass, so a
staged red/green below is meaningful.

Collision and ordering checks (landing path, before any staging):

```
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...cartography-and-mapmaking.md': No such file or directory

$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/
# no output; grep exit 1
```

- Slug unused; 0 topic-line owners. This duplicates K01/C05's freshness job only as a
  pre-staging sanity check — the landing-time recheck remains theirs.
- Sort position (0-based `sorted()` index **5**, 1-based position 6):
  predecessor `calendar-festival-systems.md`, successor `costume-semiotics.md` —
  matching `reports/round-44/scout/K02-gap-scout.md:218`.
- The README contains no cartography mention (grep exit 1), including no stale
  "Known gaps" row that the landing would have to remove.

## 2. The staged 224 tree

Built by `.scratch/r47-c10/stage.py` (sha256 `4a3baa97…d4d7d9`), which writes only
under `.scratch/r47-c10/`:

1. `shutil.copytree(corpus/knowledge, .scratch/r47-c10/knowledge)` — 223 files.
2. One fixture entry at `knowledge/culture-material/cartography-and-mapmaking.md`
   (1,674 bytes, sha256 `9e47f3a0…df23826`). **Its body is a fixture, not a draft.**
   Its `- topic:` text is the K02 seed verbatim (`reports/round-44/scout/K02-gap-scout.md:227`),
   so the row-vs-topic equality leg is exercised on real prose length (766 chars).
3. Six README transforms applied to the live bytes, each guarded by an
   exactly-one-occurrence assertion:

| # | transform | before → after |
|---|---|---|
| 1 | insert rev 2.5 block before `revision: 2.4` | — (new block) |
| 2 | repair rev-2.4 prose vector | `25/23/25/29/24/94 → **25/23/26/25/24/94**` → `… → **25/26/25/29/24/94**` |
| 3 | culture-material header | `## culture-material/ (25)` → `(26)` |
| 4 | new row after the calendar row | `- \`cartography-and-mapmaking.md\` — <entry topic byte-equal>` |
| 5 | totals line | `Total knowledge entries: 223.` → `224.` |
| 6 | counts footer | `(total 223 files; directory totals 25/26/25/29/24/94)` → `(total 224 files; directory totals 25/26/26/29/24/94)` |

Staged README: 145,595 bytes, sha256
`0ab794d8acb7e61cfd0f408b28a257f287431334a452d36af735ec2e46b7f95d`.
Key lines in the staged file: rev 2.5 at `:5`, repaired rev-2.4 vector at `:24`,
header `## culture-material/ (26)` at `:247`, new row at `:254`, totals at `:558`,
footer at `:562`.

## 3. Staged measurement (the filed instrument, unmodified)

`stage.py` imports `reports/round-28/readme/sweep.py` by path and calls its public
`sweep(readme_text, root_override=…)` (`sweep.py:119`) — the same code path `main()`
uses, with the knowledge root swapped to the stage. No filed byte was edited.

```
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25,
       "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer {"date": "2026-10-19", ..., "total": 224,
        "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 0ab794d8acb7e61cfd0f408b28a257f287431334a452d36af735ec2e46b7f95d
OK True                                # exit 0
```

Staged tree census: 224 `.md` files, culture-material 26; staged manifest
`sha256(sorted "<sha>  knowledge/<part>/<file>" lines)` =
`b3f72e3b70d0a8ce69f54646fcdaae193ab8b29646bcee7845a808655dcaebac` over 224 files.
Receipt: `.scratch/r47-c10/receipt.json` (sha256 `3fe2bbe4…bd2537`).

## 4. Controls — the green is not trivially green

`.scratch/r47-c10/controls.py` (sha256 `275a67b7…f5b41b`) mutates one transform at a
time on the staged bytes; results in `.scratch/r47-c10/controls.json`
(sha256 `ce4a52c2…8601a4`). All controls behaved as predicted
(`CONTROLS_AS_EXPECTED True`, exit 0).

| control | mutation | sweep result |
|---|---|---|
| A | footer left at 223 / `25/26/25/29/24/94` | `ok False`; `FOOTER_TOTAL {declared:223, live:224}` **and** `FOOTER_DIR_TOTALS {declared:[25,26,25,29,24,94], live:[25,26,26,29,24,94]}` |
| B | row replaced by a 35-char paraphrase | `ok False`; `topic_mismatch` class `REWRITE`, `row_chars 35`, `topic_chars 766` |
| C | header left at `(25)` | `ok False`; `header_drift {"culture-material": {"declared":25, "files":26}}` |
| D | rev-2.4 vector left unrepaired | **`ok True`** — the sweep does not read revision-note vectors (blind spot; §5) |
| E | arithmetic over revision blocks | rev 2.5 declared `25/26/26/29/24/94` = **224**; rev 2.4 repaired `25/26/25/29/24/94` = **223** |
| F | ordering | index 5: `calendar-festival-systems.md` → `cartography-and-mapmaking.md` → `costume-semiotics.md` |
| G | manifest | 224 files, `b3f72e3b…dcaebac` |

Control D is the important negative result: **sweep-green at 224==224 does not by
itself prove the prose-vector repair.** The C claim's threshold names both; they need
two checks, not one.

## 5. The rev-2.4 prose-vector defect, measured and repaired

Live `corpus/README.md:11` reads:

```
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**
```

- old vector `25/23/25/29/24/94` = 220 (matches rev 2.3's post-state);
- declared new vector `25/23/26/25/24/94` = **217**, against a live total of **223**;
- live footer vector `25/26/25/29/24/94` = **223**.

Diagnosis (slot order `linguistics / myth-symbol / culture-material / synthesis /
verification / civilizations`): the rev-2.4 note left myth-symbol at **23** (live 26),
set synthesis to **25** (live 29) and culture-material to **26** (live 25) — a net
−6 against the true total, i.e. 217. The three-entry round-42 landing was myth-symbol
only (`## myth-symbol/ (26)`), so the correct post-vector is `25/26/25/29/24/94`
(223), and the rev-2.5 post-vector is `25/26/26/29/24/94` (224).

The repair target is therefore the **post-arrow bold 6-tuple of each revision block**,
not "every 6-tuple in the file": the rev-2.5 explanatory note deliberately quotes the
defective `25/23/26/25/24/94` (217) as a dated record, and historical revision vectors
sum to their own eras' totals (rev 2.3 = 216/220, rev 2.2 = 212/216, rev 2.1 = 211/212,
rev 2.0 = 201/211). A naive all-vectors-sum-to-224 check would fail on correct history.

Scoped check to run after landing (exit 1 on mismatch):

```python
python3 -B - <<'PY'
import re, sys
t = open("corpus/README.md", encoding="utf-8").read()
ok = True
for rev, want in (("2.5", 224), ("2.4", 223)):
    block = re.search(rf"revision: {re.escape(rev)}.*?(?=\nrevision: |\nround-28 C entry|\Z)", t, re.S)
    vecs = re.findall(r"\*\*(\d+(?:/\d+){5})\*\*", block.group(0)) if block else []
    if not vecs:
        print(f"rev {rev}: no declared vector -> could-not-evaluate"); ok = False; continue
    v = vecs[-1]; total = sum(map(int, v.split("/")))
    print(f"rev {rev}: {v} = {total} (want {want})")
    ok = ok and total == want
sys.exit(0 if ok else 1)
PY
```

Result on the staged README: `rev 2.5: 25/26/26/29/24/94 = 224`, `rev 2.4:
25/26/25/29/24/94 = 223`, exit 0.

## 5a. Cross-seat collision: C05's predicted footer vector is slot-swapped

`reports/round-47/cov/C05-freshness.md` (filed concurrently during this seat's run)
agrees on the slug, the zero-ownership reading and the rev-2.4 arithmetic
(`220 → 217`, not 223), but its `:273` and `:295` predict the post-landing footer
vector as **`26/26/25/29/24/94`**. That sums to 224 but the slots are wrong: the
vector order is fixed by `reports/round-28/readme/sweep.py:39-46` (`PARTS`) and the
live footer at `corpus/README.md:548` — linguistics / myth-symbol / culture-material
/ synthesis / verification / civilizations. Culture-material moves 25 → 26 in
**slot 3**, so the correct post-landing vector is **`25/26/26/29/24/94`**. Measured
control (staged README, footer replaced with C05's vector):

```
ok False
footer_findings [{"class": "FOOTER_DIR_TOTALS",
                  "declared": [26, 26, 25, 29, 24, 94],
                  "live": [25, 26, 26, 29, 24, 94],
                  "order": ["linguistics", "myth-symbol", "culture-material",
                            "synthesis", "verification", "civilizations"]}]
```

Copying C05's vector would make the C landing fail its own sweep-green threshold.
The integrator should use `25/26/26/29/24/94`; C09's revision block and the footer
must agree on that order. This is reported as a collision, not silently routed
around.

## 6. Post-landing prediction

**Unconditional (measured on the stage; must hold after landing):**

- `total_rows == total_files == totals_line == footer.total == 224`, exit 0;
- parts `{"linguistics":25, "myth-symbol":26, "culture-material":26, "synthesis":29,
  "verification":24, "civilizations":94}`; footer vector `25/26/26/29/24/94`;
- new row byte-equal to the landed entry's `- topic:` text, positioned between
  `calendar-festival-systems.md` and `costume-semiotics.md`;
- rev-2.4 post-vector sums 223; rev-2.5 post-vector sums 224.

**Conditional (sha-level):**

- Staged README sha256 `0ab794d8…7f95d` is the digest **only if** the integrator
  applies these exact six transforms and C09's rev-2.5 prose is byte-identical to this
  variant. The row leg is already fixed: C04's filed header carries the K02 topic
  byte-equal to the staged row — `reports/round-47/cov/C04-entry-header.md:114` vs the
  fixture, both 775 chars, both sha256 `a42926b1d0fe5ac5d608bb4ebd8e16873b3ed2f43a74c34392f0e4d5632496f8`
  (checked 2026-10-19). Only the rev-2.5 prose can move the digest; if it differs,
  that is not a failure. Reproduce the model with `python3 -B .scratch/r47-c10/stage.py`.
- The staged entry sha `9e47f3a0…df23826` and manifest sha `b3f72e3b…dcaebac` are
  fixture digests for reproducing this prediction. **They are not predictions of the
  landed entry** (the fixture body is 1.6 KB of stub; the C draft is the landing body).
- The row topic must be generated from the **landed** entry, not from this fixture or
  from memory. Exact command, using the sweep's own extractor (`sweep.py:74`):

```python
python3 -B - <<'PY'
import importlib.util
spec = importlib.util.spec_from_file_location("s", "reports/round-28/readme/sweep.py")
s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
print(s.topic_of("corpus/knowledge/culture-material/cartography-and-mapmaking.md"))
PY
```

Paste that output after `- \`cartography-and-mapmaking.md\` — `. C04's filed topic
currently equals the fixture's; if the assembled entry revises it, this regenerates
the row correctly (the sweep's `REWRITE` control (B) proves a paraphrase is caught).

**Date caveat:** the footer's `Counts checked 2026-10-19` is not checked by the sweep.
Landing on 2026-10-19 needs no date change; a later landing must update it.

## 7. Integrator re-run checklist (C only)

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
find corpus/knowledge -name '*.md' | wc -l                     # want 224
ls corpus/knowledge/culture-material/*.md | wc -l              # want 26
python3 -B reports/round-28/readme/sweep.py                    # want rows 224 files 224, exit 0
python3 -B reports/round-28/readme/sweep.py --selftest         # want 12/12, exit 0
# plus the scoped vector check in §5 (want exit 0)
```

Predicted landing action is **A** (new file), not **M** — the slug is absent at
`6e9a30d` and no existing entry is touched. This seat verified the path only in the
staged copy; the integrator's apply is W02's spec.

## 8. Limits / to-verify

- The assembled C entry (C02's sections + C11's assembly) and C09's README prose
  were unfiled at close; the fragments C01/C03/C04/C05/C07 filed mid-run. C04's header
  topic is byte-equal to the row used in §6 (checked there). **To-verify at
  integration**, by re-running §7.
- The fixture entry body is not a draft and must never be landed; only its topic
  string is load-bearing here.
- `sweep.py` checks rows/topics/headers/footer/totals; it does **not** check revision
  vectors, the footer date, or whether the new topic is a genuine domain rather than
  padding. The prose-vector check is supplied in §5; entry quality is R03/X04's job;
  gap freshness at landing is C05/K01's job.
- C05's freshness verdict agrees on the slug and the rev-2.4 arithmetic; its predicted
  post-landing footer vector is slot-swapped and is flagged in §5a.
- The staged run uses `root_override` and a staged README; it does not prove the
  live tree after the integrator's edit. The live instrument is green now (223/223),
  which is the correct pre-state.

## 9. Write surface

- Written: this file only (`reports/round-47/cov/C10-sweep.md`).
- Scratch artifacts (never landed): `.scratch/r47-c10/stage.py`,
  `controls.py`, `README.staged.md`, `knowledge/**` (224-file staged copy),
  `receipt.json`, `controls.json`, `live-sweep.json`.
- `git status --short` at seat close shows no change under `corpus/`; the only
  untracked paths are the round-47 report tree and a pre-existing
  `reports/round-46/review/` (not this seat's).
