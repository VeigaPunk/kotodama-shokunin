# CriticCoverageCount — round 50 falsify, claim C measurement

Seat: `KotodamaR50-2.CriticCoverageCount-21` (critic, leaf). Axis judged: coverage.
Base `4ad26836552462d28a946ca3b067cab0b5ce3532`; landed `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`.
Private clones: `/tmp/ccc-base-uYG2/r` and `/tmp/ccc-land-Twbq/r` (`git clone -q --shared`, `GIT_CEILING_DIRECTORIES=/tmp`), deleted after the run.
Installs: none.

## Verdict: PARTIAL

- **The coverage move HOLDS.** 225 → 226 is a real new register owner, not bookkeeping. Every count, the sweep, and the S-id resolution reproduce from the landed bytes.
- **The C receipt is BROKEN as landed evidence.** The landed `reports/round-50/run-validation.py` fails claim C (`C passed False`, `acceptance_passed False`) when run on the landed and base trees. `reports/round-50/validation.json` (`C passed True`) is untracked. It was produced by an **uncommitted** working-tree edit of that runner. You can't reproduce the receipt from `1c779e4`.

## 1. Measurements re-run (both clones)

| measurement | 4ad2683 | 1c779e4 | validation.json claims.C | match |
|---|---|---|---|---|
| `find corpus/knowledge -name '*.md' \| wc -l` | 225 | 226 | 225 → 226 | yes |
| `ls corpus/knowledge/culture-material/*.md \| wc -l` | 27 | 28 | 27 → 28 | yes |
| `python3 -B reports/round-28/readme/sweep.py` rc | 0 | 0 | 0 / 0 | yes |
| sweep `rows / files` | 225 / 225 | 226 / 226 | same | yes |
| sweep `topic_mismatch` / `missing_from_index` / `orphan_rows` | 0/0/0 | 0/0/0 | 0 | yes |
| sweep footer vector | 25/26/27/29/24/94 | 25/26/28/29/24/94 | same | yes |
| sweep `readme_sha256` | `666fb794…e3a35` | `3ea247db…5d78c` | same prefixes | yes |
| word-bounded topic owners `grep -rniE '^- topic:.*\b(pastoral\|herd\|husbandr\|transhuman\|livestock)'` | 0 | 1 (the new entry, :3) | 0 → 1 | yes |
| **declared substring** `grep -rniE '^- topic:.*(pastoral\|herd\|husbandr\|transhuman\|livestock)'` (claims.json `pastoral-unowned.evidence_command`) | **1** (`writing-media-surface-economy.md:3`, "sherd") | 2 | not reported | n/a |
| `find -iname '*pastoral*'` / `'*husband*'` / `'*herd*'` | 0/0/0 | 1/1/0 | same | yes |

The corpus diff `4ad2683..1c779e4 -- corpus/knowledge` is exactly one `A culture-material/pastoralism-animal-husbandry.md`. No other knowledge file was renamed, split or deleted, so the +1 is not a re-partition artefact. Across all of `corpus/`, the commit touches only `QUALITY.md`, `README.md`, `SOURCES.md`, the entry, and `lessons/round-50.md`.

## 2. S-id / used-by resolution (landed `corpus/SOURCES.md`)

- The entry cites 22 distinct IDs, S048–S069 (contiguous). All 22 resolve to exactly one 11-cell row. `SOURCES.md` has 69 rows, no duplicate IDs, and no malformed rows.
- Every cited row has `used-by` = `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, `status mined`, `opened 2026-10-21` and `recheck 365d`. Tiers: 16 A, 6 B (S048, S049, S051, S057, S061, S065).
- No row names the entry in `used-by` without being cited. No other knowledge file cites S048–S069.
- At base, `SOURCES.md` stops at S047, so all 22 rows are new in `1c779e4`. This matches the receipt: `sources_cited 22` and `sources_unresolved []`.

Separability note, recorded here rather than as a defect: `claims.json` C `lands` lists only the entry and `corpus/README.md`. The S048–S069 rows land in `corpus/SOURCES.md` under the "frontier step (not a claim)" carve-out. If C were checked strictly against "base + only its own paths", all 22 S-ids would be unresolved. That is the r49 failure shape. The contract text pre-declares the carve-out, so it is a judge call, not a measurement error.

## 3. Real coverage move or bookkeeping? Real.

- At base there are 0 filename owners and 0 word-bounded topic owners. Herding terms (`pastoral*|herd(s|ing|er|ers|sman|smen)?|husbandry|transhuman*|livestock`) appear incidentally in 31 base files, at most 4 lines per file (`agrarian-field-system-lexicon.md` 4; `animal-symbolism.md`, `turkic-steppe.md`, `india-tamil-sangam.md`, `dine-navajo.md` 3 each). No base file owns the production system.
- Adjacent base topic lines (`turkic-steppe.md`, `transport-mobility-lexicon.md`, `animal-symbolism.md`, `scythian-saka.md`) cover dwellings, draft animals or symbolism, not herd management, tenure or products.
- The new entry has 70 lines carrying those terms and 199 lines in total, within the ≤~250 bound. It has 1 H1, 0 H3, 1 `- topic:` line, and the 8 head fields in order. Its README row sits in filename order between `music-instrument-lexicon.md` and `ritual-garments.md`, and the sweep reports `topic_mismatch 0`, so the row is byte-equal to the topic line.
- In-corpus anchors (entry line 6) all resolve at base. 23 of 50 anchored lines contain a herding term. The other 27 are method or structure anchors that the entry reuses as such: hunting-foraging decision-table shape `:137-146`, `calibration-registry.md:35-39` grade legend, `sacred-kingship-mythic-charter.md:65` "shepherd" delegation (prefix-unbounded "herd"). None of them is cited as a pastoral claim it doesn't make. Sentence-level source honesty belongs to the S0xx re-open seats; I didn't judge it here.

## 4. Counterexample: the landed runner does not reproduce the receipt

The commands below ran in the clones and wrote only to stdout:

```
python3 -B /tmp/ccc-land-Twbq/r/reports/round-50/run-validation.py --tree <landed> --base-tree <base>
  → acceptance_passed False; C passed False; Ca passed True; O passed True
  → before pastoral_topic_owner_lines {'actual': 1, 'expected': 0, 'ok': False}

python3 -B <working-tree run-validation.py copy> --tree <landed> --base-tree <base>
  → acceptance_passed True; C passed True   (matches validation.json)
```

Evidence:
- `git -C kotodama-shokunin status --short`: ` M reports/round-50/run-validation.py`, `?? reports/round-50/validation.json`.
- `git ls-files reports/round-50` at `1c779e4` contains `run-validation.py` but no `validation.json`.
- Working-tree diff vs `1c779e4`, `reports/round-50/run-validation.py:69-71` (working-tree numbering): `TOPIC_OWNER_RE` changes from `^- topic:.*(pastoral|…)` to `^- topic:.*\b(pastoral|…)`, with the comment "Word-bounded (R50-M2): the declared substring command also matched "sherd"…". The `topic_owner_lines` docstring is changed to match.
- mtimes: commit 13:03:10, runner edited 13:04:02, receipt written 13:32:51 (-0300). The receipt postdates landing and was produced by bytes that were never committed.
- Landed `corpus/lessons/round-50.md:69` (R50-M2) discloses the sherd hit only for the declaration's printed command. It states the fix lives in the entry's `gap filled` line. It does not disclose that the committed runner carries the same substring bug, or that the receipt depends on a post-landing runner edit.

**Impacted axes:** coverage (the claim's own receipt fails at the landed SHA) and operability/provenance (a receipt attributed to a commit it can't be regenerated from).
**Not impacted:** the coverage substance. The word-mode `topic_owner_absent` probe declared in `claims.json` (`mode: "word"`) gives 0 at base, and every after-value holds.

## 5. Smallest safe correction

1. Commit the working-tree `reports/round-50/run-validation.py` (the word-bounded `TOPIC_OWNER_RE`) together with the `validation.json` it produced, in one follow-up commit. Record the receipt's runner SHA as that commit, not `1c779e4`.
2. Add one row to `corpus/lessons/round-50.md` `## Mistakes`, or extend R50-M2, stating that the landed runner at `1c779e4` failed C's before-check on "sherd" and that the receipt was regenerated with the corrected runner.

No change to the entry, README row or SOURCES rows is needed for the count claim.

Author-lane advice, not admission.
