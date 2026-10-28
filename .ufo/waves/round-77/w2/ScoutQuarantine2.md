# ScoutQuarantine2 — round 77, wave 2 (falsifier)

Attacked item: W1 seat `ScoutQuarantine` (`.ufo/waves/round-77/w1/ScoutQuarantine.md`), the absent-defect register slice census and the silent-adoption question. Re-ran the exact census, extended the collision sweep from the staged-file subset to the full base registry, and traced every overlap to its named disposition record.

## 1. Register slice census rerun — VERIFIED

Exact W1 command re-executed:

```sh
awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
```

Raw output saved at `.ufo/waves/round-77/w2/stage/ScoutQuarantine2/slice-rerun.txt`; `wc -l` → `21`. `diff` against W1's stored slice `.ufo/waves/round-77/w1/stage/ScoutQuarantine/slice.txt` → byte-identical (`IDENTICAL`).

Split confirmed:

- 18 `payload-absent` rows: S776, S778, S779, S786, S787, S791, S792, S795, S796, S804, S814, S816, S817, S820, S823, S824, S825, S827 (register lines 118–135, rounds 1–5; each note reads "the quote is in none of them").
- 3 never-checked rows: `S807``, `S812``, `S835`` (register lines 333–335; reason cell: "the cited source could not be fetched, so no quote was checked"; trailing backtick is the register's own cell spelling `S###`` — an artifact, not an ID variant).
- Register structure verified: `## Rows` at line 25, `## By lane` 232 (`| kotodama | 18 |` at 239), `## Rows whose quotes were NEVER CHECKED` at 256, table header at 265.

W1's count and split hold.

## 2. Silent-adoption check — extended sweep

W1 compared the 21 slice URLs only against the staged naming-systems files + staged `SOURCES.append.md` (11/21 collisions). This wave's question is the lane registry itself: I extracted all 21 cited URLs (`.ufo/waves/round-77/w2/stage/ScoutQuarantine2/quarantine-urls.txt`) and ran exact `grep -F` against base `corpus/SOURCES.md` (820 rows at `211f952…`).

**Result: 5 of 21 quarantine documents appear in the current base registry — none silently.**

| Slice id | Register class | Cited document | Current lane row | Disposition record |
|---|---|---|---|---|
| S776 | payload-absent | openstd.samr.gov.cn GB/T 33661-2017 record | S895 (SOURCES.md:850, mined 2026-10-27, used-by calendar amend) | round-76 adoption; evidence `reports/round-76/evidence/S895.txt` (quote-found yes, anchor 「标准号：GB/T 33661-2017」); verdict table `corpus/lessons/round-76.md` Quarantine § (S776 PRESENT, carried unchanged) |
| S787 | payload-absent | chinawriter.com.cn …/c404024-40083104.html | S893 (line 848, mined 2026-10-27) | round-75 bridge; row evidence cell itself records "the staged round-72 quote span 作品中的人物名字和地名 is absent from this page and stays rejected" — explicit, not silent |
| S816 | payload-absent | chinawriter.com.cn …/c404024-40494534.html | S883 (line 838, mined 2026-10-25) | round-75 bridge; different quote (build-order P68 span, not register's absent 资深读者 span); r76 verdict REFUSED carried |
| S817 | payload-absent | chinawriter.com.cn …/c404024-32582252.html | S884 (line 839, mined 2026-10-25) | round-75 bridge; different quote (paragraph-35 tolerance span, not register's absent Sowers-Wills span); r76 verdict REFUSED carried |
| S825 | payload-absent | digital.archives.go.jp/search | S894 (line 849, mined 2026-10-27) | round-76 adoption; evidence `reports/round-76/evidence/S894.txt` (anchor 「元号名称 開始西暦年 令和 2019」, quote-in-anchor yes); r76 verdict PRESENT carried |

All five are `mined` rows with named used-by entries and committed round-75/76 evidence or lesson dispositions. None is `queued`/`rejected`; none inherits the register's absent quote (each locates a different, freshly-evidenced span).

## 3. The 3 never-checked rows — adoption status

- `S807`` → ONOMA.51 DOI: no base registry row; staged S890 is on the claim's **removal** list for the adopted entry. Not adopted.
- `S812`` → cnj.2024.21 DOI: no base row, not in staged/adopted set. Not adopted.
- `S835`` → omu.repo.nii.ac.jp PDF: no base row; staged S918/S936 appear only in held 23c and **refused** 24 Oct candidates. Not adopted.

0/3 never-checked documents are current source rows.

## 4. Round-77 planned rows vs quarantine family

- New rows S897 (D1, lishisuo.cssn.cn) and S898 (D2, onomastica download/574/763) cite documents that ARE quarantine-family members — register S814 and S820, both `payload-absent`, r76 verdict REFUSED, "carried, not touched" in the round-76 lesson.
- This is document-level overlap, not silent payload adoption: (a) the draft entry `.ufo/waves/round-77/w1/drafts/.../naming-systems.amend-2026-10-23.md` cites exactly 2 source lines (S897, S898); grep for every quarantine-colliding staged id (S859, S875, S886, S888–S891, S896, S903, S906–S908, S910, S918, S932–S936, S966) → 0 hits; (b) the register's absent payload for S814 is a Japanese NDC fragment unrelated to the draft's seven located Chinese quotes; (c) for S820 the draft quote 「standard given names with lexemes reflecting feminine softness」 is a strict prefix of the absent span `such names may be classified as 'standard given names with lexemes reflecting feminine softness and female aesthetic val` — consistent only if the located span verifies (same substring pattern r76 used for S894/S895); (d) staged S934 (same DOI as S898) is dispositioned **refused** in the claim.
- Gap worth the freeze's attention: CLAIMS-DRAFT line 17 says "W1 ID sweep found no base registry document match for these two sources" — true, and my sweep confirms lishisuo/onomastica URLs absent from base SOURCES.md. But the draft does not itself record that D1/D2 are register-slice documents S814/S820; that linkage lives only in `w1/ScoutQuarantine.md` rows S814/S820. The document map leg should carry staged-S897→register-S814 and staged-S903→register-S820 so the adoption is auditable rather than ID-only.

## 5. Counts and names

- Slice census: 21 rows total — 18 payload-absent (S776, S778, S779, S786, S787, S791, S792, S795, S796, S804, S814, S816, S817, S820, S823, S824, S825, S827) + 3 never-checked (S807`, S812`, S835`). Matches W1 exactly.
- Base-registry adoption of quarantine documents: 5 rows, all explicitly dispositioned — S883/S884/S893 (round 75) and S894/S895 (round 76). Silent adoptions: **0**.
- Round-77 new rows re-using quarantine documents: S897 (register S814), S898 (register S820) — declared in W1 collision table; distinct located quotes; not silent.
- Never-checked family adopted: **0**.

## Commands and raw outputs

- `awk … | wc -l` → `21`; `grep -c 'payload-absent'` → `18`; `grep -c 'could not be fetched'` → `3`; `diff` vs W1 slice → `IDENTICAL`.
- `git show 211f9526…:corpus/SOURCES.md | wc -l` rows → `820`; per-URL `grep -Fc` counts: 1 hit each for openstd, chinawriter ×3, digital.archives.go.jp; 0 for the other 16 URLs (full list in `stage/ScoutQuarantine2/quarantine-urls.txt`).
- `git show …:reports/round-76/evidence/S894.txt` / `S895.txt` → `quote-found: yes`, `anchor-found: yes`, `quote-in-anchor: yes` (S895 verbatim yes; S894 verbatim no, anchor-bound yes).
- `git show …:corpus/lessons/round-76.md` Quarantine § → 21-row verdict table (PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4), 5 named lane-row overlaps, "register remains read-only".

Confidence: high on census and adoption counts (all greps verbatim, byte-identical slice). Remaining unknown: whether the freeze's document map records the register-slice lineage of S897/S898 — flag for ConnClaimsCounter/DocS sources seat; falsification hinge is the counter's document-map leg, not the row count.
