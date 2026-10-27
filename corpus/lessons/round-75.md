# Round 75 — kotodama: the narrative-structure thread closes (structuralist primaries + CJK narratology, assimilated)

**Claims line.** Lane `kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15` (also HEAD;
no freeze commit exists — `git cat-file -e HEAD:reports/round-75/claims.json` → absent, so the round's
files are untracked working bytes and this lesson grades none of them), hyaku run 10, attempt 2
(attempt 1 filed nothing — R75-M1). **C (coverage, sourced):** nine rows S885–S893 opened and mined, one
row per document — staged S876/S885/S917/S921 → S885, S902 → S886, S904 → S887, S864 → S888, S865 → S889,
S866 → S890, S905 → S891, S919 → S892, staged S870 → S893 (the document re-opened) — over ground the lane
did not hold at base (`git ls-tree -r --name-only f556d1… corpus/knowledge | grep -c narrative` → 0);
three entries (`corpus/knowledge/myth-symbol/narrative-structure-frameworks.md`, `…amend-2026-10-23.md`,
`…amend-2026-10-23b.md`); registry 808 → 817 rows; knowledge files 249 → 252; `reports/round-75/accept-c.py`
printing `ACCEPT-C-75: PASS legs=13/13`. **Ca (calibration):** `reports/round-75/ledger.json` as staged
holds **10 pairs, 6 REPAIR / 4 ANNOTATE**, L75-01…L75-10 (the w1 draft said eleven, 4 REPAIR / 7 ANNOTATE —
R75-M3), with `accept-ca.py` printing `ACCEPT-CA-75: PASS legs=12/12`. The predicate wording in
`reports/round-75/claims.json` is the authority this lesson is measured against; the claims are `DRAFT`.

## Corrections

Append-only; `corpus/lessons/round-74.md` is not edited. The two rows below are the round-74 closure's
routed defect **R2** and the ledger's ANNOTATE pairs L75-08/L75-09. Re-derived by this seat over the base
bytes; commands pasted exactly.

**The round-74 Gate reject rows for staged S899/S900 gave reasons that are false as written.** The staged
rows' own anchor spans are present on their own pages; the absent spans belong to register S816 and S817.
The disposition actually taken was adopt-with-renumber, so the Gate text is the defect, not the landing.

| where | old (as filed) | new (reclassified) | re-derivation command | output 2026-10-27 |
|---|---|---|---|---|
| `corpus/lessons/round-74.md:37` (staged S899 → lane S883) | "staged S899's quoted span was absent from the page it was bound to (register S816 mispairing; the span belongs to the 2022 interview) — the row stays refused and the document is re-opened as the new S883" | the staged span `非凡特性来自最初造物主` is present once on its own 2025 page in the committed round-74 capture; the absent span (`这个我肯定考虑过`) is register S816's, bound to that page. Disposition: **adopt-with-renumber (S899 → S883)**, not a reject; the mispairing belongs to register S816 | `git grep -c '非凡特性来自最初造物主' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S883.txt` | `1` |
| `corpus/lessons/round-74.md:38` (staged S900 → lane S884) | "staged S900's quoted span was the Sowers-Wills clause, absent from this page (register S817 mispairing) — the row stays refused and the document is re-opened as the new S884" | the staged span `这个我肯定考虑过` is present once on its own 2022 page in the committed round-74 capture; the Sowers-Wills clause is register S817's and belongs to lane S880's document. Disposition: **adopt-with-renumber (S900 → S884)**; the mispairing belongs to register S817 | `git grep -c '这个我肯定考虑过' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S884.txt` | `1` |

Cross-checks that fix which artifact carries the defect: `这个我肯定考虑过` in
`reports/round-74/evidence/S883.txt` → `0`; `非凡特性来自最初造物主` in
`reports/round-74/evidence/S884.txt` → `0`; `Sowers` in `reports/round-74/evidence/S884.txt` → `0`. So the
spans are on their own pages and the register pairs bind each URL to the other row's quote.

Scope of this correction: it reclassifies the *staged rows'* reject reasons. It does **not** touch
register S816/S817, whose own verdicts stay REFUSED (Quarantine), and it does not edit the round-74
lesson. The criterion this needs — a reject reason names the artifact it was observed on, staged row or
register row — is `QUALITY.md` criterion 27 in the round-75 claim Ca set.
