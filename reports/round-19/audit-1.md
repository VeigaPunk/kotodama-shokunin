# R19-A15 — filler audit 1/2: the round-19 verification-partition entries (NON-CANON)

- seat: R19-A15 (filler auditor, verification partition). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  Assignment (verbatim): *"AUDIT R19-A15..A18 (filler+interop auditors x4): read all new
  entries (filler rejection candidates) … reports/round-19/audit-{1..4}.md"*.
- date: 2026-10-18 (lane-local clock UTC-03:00; all stamps below UTC). Audit window opened
  08:31 local and the readings in §1–§5 were taken **11:36–11:39Z** on a **live, unsettled**
  wave; §7 records the settle re-check. Worktree HEAD `169c616`; declared round-19
  `baseline_revision` `e5718945a1ab0a0c3db955338d2cae77d68fd348` (`reports/round-19/claims.json`).
- role limits: this seat audits and reports. Its only writes are this file and its sibling
  `audit-2.md` (plus gitignored `.scratch/audit/`). It edits no corpus entry, admits no
  claim, disposes no candidate, and executes no historical validator. The rejection
  candidates below are routed to the parent; the disposition (entry repair vs acceptance-bar
  reading) is not this seat's call.
- criteria applied (claim C, `reports/round-19/claims.json`; `reports/round-19/gaps.md`):
  1. **names the gap it fills** (no filler); 2. **a decision-record section**;
  3. **sources resolve** (cited repo paths exist; cited commands re-run; URLs get a
  documented access attempt). Plus the lane's own `corpus/QUALITY.md` admission bar as a
  reported, non-gating observation (§5).
- instruments: `.scratch/audit/r19-audit.py` (independent field/heading/path census; a
  verbatim replication of the round-10 acceptance gap/decision regexes
  `reports/round-10/run-validation.py:363-370`, applied independently); verbatim re-runs of
  each entry's own quoted absence sweep (§4); `sha256sum` recomputation. The round-19
  counting command's own entry regexes (`reports/round-19/run-validation.py:443-455`,
  `ENTRY_GAP_RE = \bgap\b` + a `.md` ref) are **not** used as my evidence — they are looser
  than the assignment's letter, and §3 reports where my merits reading and a mechanical
  reading would differ.

## 1. Snapshot — the five new verification entries

Baseline verification partition: 15 files. Live at this reading: **20** (15 + 5). All five
are untracked new files; no filed round-8..18 byte was touched by them.

| # | entry (under `corpus/knowledge/verification/`) | sha256 (first 12) | bytes | mtime (local) |
|---|---|---|---|---|
| V1 | `label-channel-routing-verification.md` | `de6cff53042b` | 13490 | 08:33:40 |
| V2 | `pre-declared-hold-set-reconciliation.md` | `31630371ce9e` | 12318 | 08:34:09 |
| V3 | `generated-artifact-roundtrip-verification.md` | `c84d08810fa0` | 12617 | 08:34:37 |
| V4 | `gate-battery-surface-verification.md` | `a9de4179a739` | 11965 | 08:35:04 |
| V5 | `two-reader-interop-agreement.md` | `188ecd4da172` | 12017 | 08:35:36 |

Each maps to a declared gap in `reports/round-19/gaps.md` (`label-channel-routing-verification`,
`pre-declared-hold-set-reconciliation`, `generated-artifact-roundtrip-verification`,
`gate-battery-surface-verification`, `two-reader-interop-agreement`), one author fragment per
entry under `reports/round-19/entries/R19-C11..C15.md`. Verification minimum for claim C is
>=3; 5 landed.

## 2. Verdicts

**All five clear criteria 1–3. One carries a broken citation (V1, §3) and three carry a
QUALITY-bar calibration gap (V2, V3, V4, §5). No entry is a filler rejection candidate: every
one names the gap it fills, carries a real decision-record section, and states an absence
sweep.**

| # | entry | gap named | decision record | sources resolve | verdict |
|---|---|---|---|---|---|
| V1 | label-channel-routing-verification | yes (`- gap filled:`) | yes (`## 6. Decision record`) | **one broken path** | pass-with-defect (§3) |
| V2 | pre-declared-hold-set-reconciliation | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |
| V3 | generated-artifact-roundtrip-verification | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |
| V4 | gate-battery-surface-verification | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |
| V5 | two-reader-interop-agreement | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |

Census (`.scratch/audit/r19-audit.py`, 11:37Z): all five `topic`/`sources`/`couples`/
`verified-at`/`recheck` header lines present; `gap` = field-form in all five (no body-heading
form — the round-10 mechanical false-negative shape is absent here because each entry uses the
recognized `gap filled:` clause); decision-record heading present in all five. `follows:` is
absent from all five, which is **not** a defect: neither the round-10 bar
(`C_FRONTMATTER_FIELDS = ("topic","sources","verified-at","recheck","couples")`) nor the
round-19 bar (`entry_profile`, `reports/round-19/run-validation.py:443`) requires it.

## 3. V1 `label-channel-routing-verification.md` — one broken citation (source-resolution defect)

- The entry cites `reports/round-18/d4/ASSEMBLY.md` at line 92:
  > "…the round-17 typed-support fragments measured a culture-boundness (`reports/round-18/d4/ASSEMBLY.md` §4 records `tools/d2-typed-labels.py` refusing the D4 packet on `packet.eras`)."
- That path **does not exist**: `ls reports/round-18/d4/ASSEMBLY.md` → *No such file or
  directory*. `reports/round-18/d4/` holds `holds.md`, `determinism.md`, `manifest.md`,
  `replay.md`, `gate-runs-{1..4}.md`, `interop-{1..3}.md`, `neg-{1..3}.md`,
  `review-{1..4}.md`, `scribe-{1..8}.md` — no `ASSEMBLY.md`.
- The content the sentence describes **is** present at `examples/culture-d4/ASSEMBLY.md` §4
  ("The named hold set"), whose line 73 records exactly the refusal named:
  `packet.eras: expected a non-empty list of era tags`. So the citation is a **mis-path**, not
  a fabricated source: the referent exists, the locator does not resolve.
- Impact: this is one of the entry's cited sources (an inline body citation, not a
  `KTD-LR-S-*` row). It does not affect the entry's headline gap or its measurements; it is a
  cheap repair (correct the path to `examples/culture-d4/ASSEMBLY.md`). It is reported, not
  repaired — corrections are the author's/parent's call.
- Everything else resolves: 12 locators, all other paths exist; 1 URL present.

## 4. Absence-sweep replication (the substantive gap test)

Each entry states its gap's absence as a quoted command + result. I re-ran each **verbatim**
from the lane root at 11:38Z. Because the round-19 entries now exist, the live count includes
the author's own entry; the test is whether any **pre-existing** file matched (which would
falsify the authoring-time "→ 0 files" claim).

| sweep (as quoted) | claimed | live total | pre-existing hits | reproduces? |
|---|---|---|---|---|
| V1 `grep -rln "translated-label\|sound channel\|channel routing" corpus/knowledge/verification/` | 0 | 1 | **none** | **yes** |
| V2 `grep -rln "hold set\|hold_set_declaration\|pre-declared" corpus/knowledge/verification/` | 0 | 3 | **none** | **yes** |
| V3 `grep -rln "round-trip\|roundtrip\|serializer" corpus/knowledge/verification/` | 0 | 3 | **none** | **yes** |
| V4 `grep -rln "check-gate-battery\|gate battery\|battery_exit" corpus/knowledge/` | 0 | 2 | `verification-independence-anti-circularity.md` | **NO** |
| V5 `grep -rln "interop\|two readers\|reader agreement" corpus/knowledge/` | 0 | 2 | `myth-symbol/divination-omen-systems.md` | **NO** |

- **V4 — does not reproduce.** `verification-independence-anti-circularity.md` matches
  `check-gate-battery` at lines 15, 18 and 89 (`- couples:` tool path, `- recheck:` trigger,
  and a decision-table cell citing "`tools/check-gate-battery.py` output"). At authoring time
  the sweep returned **>=1 file**, not 0. The hit is an *unrelated sense* — it names the tool
  as a coupled surface, never its coverage semantics — so the gap (what the battery actually
  covers and what it omits) is genuine; but the quoted evidence line does not reproduce as
  written. The round-10 precedent (`reports/round-10/coverage/audit-filler.md` §3.2, and the
  "3 hits, all unrelated senses" treatment in
  `verification-independence-anti-circularity.md`'s own `verified-at`) is to **name the hit and
  its unrelated sense**, not to claim zero.
- **V5 — does not reproduce.** `myth-symbol/divination-omen-systems.md:201` reads "Staff **two
  readers** with different tenure (hereditary + trained, or citizen + foreign)…" — a
  divination-practitioner sense, unrelated to reader-implementation interop. At authoring time
  the sweep returned **1 file**, not 0. Same disposition: the gap is genuine, the evidence line
  is inaccurate as quoted.

Both are **source-rigor defects on the gap statement**, not filler: the entry still names a
real, specific gap. Routed for a one-line correction (document the unrelated hit, as V5's own
sibling `two-reader-interop-agreement.md` failed to do).

## 5. QUALITY-bar observation — missing calibration vocabulary (3 of 5)

The lane's own provenance gate flags three of the five verification entries. Command
(11:38Z): `python3 tools/gates/provenance-audit.py corpus/knowledge` → **exit 1**,
`files=199 marks=733 mark-lines=719 findings=7 blocked=0`.

```
FINDING missing-calibration: corpus/knowledge/verification/gate-battery-surface-verification.md: no calibration vocabulary anywhere
FINDING missing-calibration: corpus/knowledge/verification/generated-artifact-roundtrip-verification.md: no calibration vocabulary anywhere
FINDING missing-calibration: corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md: no calibration vocabulary anywhere
```

- `corpus/QUALITY.md` criterion 2 requires every entry to name its calibration status
  (mainstream / contested / discredited). The gate's vocabulary test is the literal substring
  `calibrat` (`tools/gates/provenance-audit.py:84`). V1 and V5 carry it (2 and 3 occurrences);
  V2, V3, V4 do not (`grep -c -i calibrat` → 0).
- This is a **QUALITY-bar finding, not one of the three assignment criteria**, and it is
  **not** part of the round-19 counting command's entry bar (`entry_profile` checks only
  topic/sources/couples lines, a `gap`+`.md` pair, and a decision record). Reported here so the
  parent can decide: the three entries add a calibration line, or the round records the
  QUALITY.md criterion-2 divergence explicitly.
- The same finding recurs across the synthesis partition (7 of 10 entries total) — see
  `audit-2.md` §5 for the wave-level count.

## 6. Limits

- Structural and resolvability checks only: this file verifies that a gap is *named* (and, in
  §4, that its stated absence sweep reproduces), that a decision-record heading exists (not
  that each decision is sound), and that cited sources resolve to live objects (not that the
  objects support the claims at passage level). Passage-level source support is the C-reviewer
  seats' work, not absorbed here.
- Verdicts bind the §1 hashes and the 11:36–11:39Z reading window on a **live** wave. The
  entries were revised during the window (V1's digest moved during authoring); §7 re-binds
  after settle.
- Author-side, NON-CANON. This file admits no entry, edits no corpus byte, and decides nothing
  for lore-shokunin.

## 7. Settle re-check (2026-10-18T11:45:59Z; worktree hash `071b5acf90a2` stable ×3)

The verification entries were **revised during the window**; both §3 and §5 defects were
repaired by the authors before the tree settled, and the settled hashes differ from §1.

**Settled hashes and criteria (re-measured 11:45–11:46Z):**

| # | entry | settled sha256 (first 12) | bytes | gap | decision | missing paths |
|---|---|---|---|---|---|---|
| V1 | label-channel-routing-verification | `22e27dd62c34` | 13830 | yes | yes | **none** |
| V2 | pre-declared-hold-set-reconciliation | `9c4a6f3e8cec` | 12608 | yes | yes | none |
| V3 | generated-artifact-roundtrip-verification | `66d9aa18f4e2` | 12934 | yes | yes | none |
| V4 | gate-battery-surface-verification | `48e0ae7590d9` | 12265 | yes | yes | none |
| V5 | two-reader-interop-agreement | `daebba3ae825` | 12333 | yes | yes | none |

- **§3 (V1 broken citation) — RESOLVED.** The settled V1 has **0 missing cited paths**
  (`.scratch/audit/r19-audit.py`, 11:45Z). The mis-path to `reports/round-18/d4/ASSEMBLY.md`
  is gone from the settled bytes. Verdict for V1: **pass, defect cleared**.
- **§5 (missing calibration) — RESOLVED, wave-wide.** Settled command:
  `python3 tools/gates/provenance-audit.py corpus/knowledge` → **exit 0**,
  `files=199 marks=733 mark-lines=719 findings=0 blocked=0`. All ten new entries now carry
  `calibrat` vocabulary; the 3-of-5 finding for this partition is cleared (and the 7-of-10
  wave count in `audit-2.md` §5 likewise).
- **§4 (absence sweeps) — NOT resolved.** V4's and V5's quoted sweeps are byte-unchanged at
  settle and still return >=1 pre-existing file (see `audit-2.md` §7 for the settled wave
  table). This is the one live finding this file routes.
- Criteria 1–3 at settle: **5/5 verification entries pass all three.** No filler rejection
  candidate. The verification minimum (>=3) is met with 5.
