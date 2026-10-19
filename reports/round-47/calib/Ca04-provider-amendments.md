# Ca04 — loop-1 provider amendments (queue-successor input)

- **Seat:** `Ca04` (claim Ca — calibration / loop-1 defect reconciliation).
- **Round:** 47, loop 2, position 1; baseline `6e9a30d`; written 2026-10-19.
- **Out:** `reports/round-47/calib/Ca04-provider-amendments.md`.
- **Status:** draft fragment. Successor records only — this file edits no filed
  byte and stages nothing under `corpus/`. `Ca06` assembles the queue successor;
  `Ca05`/`Ca07` verify.

## 0. Contract and non-goals

The Ca claim requires: “the antigravity-lane outage + zai-exhaustion provider
amendments recorded” as **named deviations**, each with a class, an owner and
cited evidence, with zero silently dropped. This fragment supplies exactly those
two records as fenced rows.

It does **not**:

- classify them as defect rows — the parent queue’s own notes exclude named
  telemetry deviations from defect rows (`reports/round-40/op/defect-queue-v2.json:8`:
  “Telemetry deviations deliberately NOT defect rows (r37 practice: rule
  breaches only)”);
- edit the parent queue — `reports/round-40/op/defect-queue-v2.json` stays
  byte-identical at `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`;
- claim provider-side facts that this repo cannot observe (quota state) —
  those are marked `to-verify` with an owner.

## 1. Method and sources

Read at HEAD `6e9a30d` (2026-10-19), all paths repo-relative:

| source | what it establishes | sha256 |
|---|---|---|
| `reports/round-46/loop-1-retrospective.md` | the loop-1 provider record and the loop-2 plan (`:3-4,23,26,51-53,57-60`) | `a8e3fabb0d65…` |
| `reports/round-44/telemetry/dispatch-declared.json` | position 12 requested antigravity; the abort/re-route text (`:10,17`) | `565e4fbd505c…` |
| `reports/round-44/telemetry/observed-dispatch.json` | the observed deviation and the unrelated `reasoning_content` failure mode (`:17-18`) | `445daadfd5d3…` |
| `reports/round-44/telemetry/availability-close-44.json` | requested vs observed lane; route history (`:24-28`) | `8a9146e1b3cc…` |
| `reports/round-43/telemetry/dispatch-declared.json` | position 11 requested zai; operator redirect (`:8-9`) | `76632d7354f4…` |
| `reports/round-43/telemetry/observed-dispatch.json` | the named deviation: zai/antigravity/cursor interrupted x3 (`:20`) | `10181657c574…` |
| `reports/round-43/telemetry/availability-close-43.json` | requested zai, route history, redirect chain (`:18,23-28`) | `eddfb5f334ee…` |
| `reports/round-47/telemetry/dispatch-declared.json` | the standing loop-2 amendments (`:18`) | `3d8263694589…` |
| `reports/round-40/op/defect-queue-v2.json` | parent queue; the deviations-not-defects rule (`:8`) | `dfc9265d094a…` |

Other citations: `REGIMEN.md:13-23` (schedule), `:66-69` (only declared
deviations permitted), `:73-77` (exhausted/unreachable lane protocol);
`LOG.md:3821-3825` (r43) and `:3848-3853` (r44); `SCORECARD.md:833-837`
(r43), `:855-858` (r44), `:871-872` (the named antigravity deviation).

Parent-history check (same shape as `reports/round-43/calib/defect-queue-v2-successor-r43.json:6-8`):
the parent was committed at `13a1657` with sha `fe596a9d…`, amended in place at
`ac47c78` (r41, 20 lines, recorded), and has not changed since. Re-derived
independently: `git show 13a1657:reports/round-40/op/defect-queue-v2.json |
sha256sum` → `fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98`;
`git show ac47c78:reports/round-40/op/defect-queue-v2.json | sha256sum` →
`dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` (= current
bytes). `git log --oneline -- reports/round-40/op/defect-queue-v2.json` returns
exactly `ac47c78` and `13a1657`; `git status --porcelain -- <path>` is empty.
Any later in-place edit is detectable as a digest mismatch.

## 2. What the filed record actually says

### 2.1 Antigravity lane outage (loop-1 positions 12–13)

| step | filed fact | citation |
|---|---|---|
| schedule | pos 12 = `antigravity/gemini-3.8-flash` (32–64); pos 13 = `antigravity/gemini-4-argon` (8) | `REGIMEN.md:21-22` |
| r43 precursor | route history includes `cursor/gemini-4-argon (interrupted)` | `reports/round-43/telemetry/availability-close-43.json:26` |
| r44 (pos 12) | scheduled antigravity; **aborted twice with zero seat output**; operator re-routed to `opencode-go/deepseek-v4.1-flash` | `reports/round-44/telemetry/dispatch-declared.json:10,17`; `…/observed-dispatch.json:18`; `…/availability-close-44.json:25-27` |
| r44 outcome | executed on the re-route: 32 launched / 14 completed / 18 failed (an unrelated opencode-go `reasoning_content` defect) | `…/observed-dispatch.json:10-17` |
| r45 (pos 13) | **skipped**; “antigravity lanes broken (operator ruling)” | `reports/round-46/loop-1-retrospective.md:23` |
| r45 evidence of absence | `reports/round-45/` does not exist; `git log --all --grep='round 45' -i` returns 0 | measured, §6 |
| loop 2 | pos 12–13 = r58/r59, “antigravity (skip/re-route)” | `reports/round-46/loop-1-retrospective.md:59-60` |

### 2.2 Zai exhaustion → luna-max (loop-1 pos 11; loop-2 pos 7–8, 11)

| step | filed fact | citation |
|---|---|---|
| schedule | pos 7–8 = `zai-coding-plan/glm-5.3-flash` MAX (16–32); pos 11 = `…-flash-low` pinned MAX (32) | `REGIMEN.md:17,20` |
| loop-1 pos 7–8 | r39/r40 ran zai glm-flash and were admitted | `reports/round-46/loop-1-retrospective.md:17-18` |
| loop-1 pos 11 | r43 scheduled zai; interrupted pre-completion x2; operator redirected (3rd) → antigravity → cursor → opencode-go | `reports/round-43/telemetry/dispatch-declared.json:8-9`; `…/observed-dispatch.json:20`; `…/availability-close-43.json:18,24-27` |
| exhaustion statement | “zai usage exhausted — zai seats route to `openai-codex/gpt-6-luna-max` for the session.” | `reports/round-46/loop-1-retrospective.md:53` |
| loop 2 plan | “pos 7-8 + 11 zai→luna-max (amendment)” → r53, r54, r57 | `reports/round-46/loop-1-retrospective.md:59` |
| standing status | “Standing amendments: zai->luna-max all session” | `reports/round-47/telemetry/dispatch-declared.json:18` |

**Failure-mode distinction (do not flatten):** the retrospective calls the zai
lane *exhausted* (`:53`), while the r43 telemetry records *pre-completion
interruptions* (`observed-dispatch.json:20`). These are different observations;
the replacement plan follows from the retrospective, but the cause is not
independently established. See `to-verify` in row 2.

## 3. Wording correction

The Ca04 mission says “the antigravity-lane outage (**positions 12/13 skipped**)”.
The filed record does not support “both skipped”:

- **position 12 (r44) was re-routed and executed** — 32 seats launched on
  `opencode-go`, 14 completed; the round exists and is filed
  (`reports/round-44/`, verdict `rejected-honest-stop`);
- **position 13 (r45) was skipped** — no directory, no telemetry, no commit.

The row below records the distinction. This is a calibration correction, not a
dispute: the retrospective itself says “skipped **or re-routed**”
(`reports/round-46/loop-1-retrospective.md:52`).

## 4. Fenced successor rows

Fenced JSON; `Ca06` extracts. The rows are **not** defect rows
(`"defect_row": false`) and must not be counted in the defect total. The
preferred landing is a top-level `provider_amendments[]` array in the successor;
a closed-schema merge projects each row to the eight v2 fields
(`id/origin/class/owner/reason/next_touch/evidence/verification`) with
`class: "named-deviation"` and `v2_class_equivalent: null`.

```json
{
  "schema": "kotodama-provider-amendments-v1",
  "round": 47,
  "date": "2026-10-19",
  "baseline_commit": "6e9a30d",
  "parent": "reports/round-40/op/defect-queue-v2.json",
  "parent_sha256_at_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "parent_defect_row_count_at_assembly": 38,
  "class_vocabulary_extension": {
    "named-deviation": "A scheduled provider/model was not the observed provider/model, or a scheduled position did not execute, under a recorded operator ruling or lane-recorded amendment. Not a defect row: no rule breach is alleged; the record keeps requested and observed separate."
  },
  "rows": [
    {
      "id": "PA-47-01-antigravity-lane-outage",
      "kind": "provider-amendment",
      "defect_row": false,
      "class": "named-deviation",
      "v2_class_equivalent": null,
      "origin": "loop-1 positions 12-13 (rounds 44, 45); first lane signal at r43 (cursor/gemini-4-argon interruption in the route history), zero-output abort at r44; consolidated at reports/round-46/loop-1-retrospective.md:51-52,59-60",
      "requested": [
        {"loop": 1, "position": 12, "round": 44, "lane": "antigravity/gemini-3.8-flash", "workers": "32-64"},
        {"loop": 1, "position": 13, "round": 45, "lane": "antigravity/gemini-4-argon (max effort)", "workers": 8}
      ],
      "observed": [
        {"loop": 1, "position": 12, "round": 44, "route": "opencode-go/deepseek-v4.1-flash", "outcome": "executed after re-route; 32 launched / 14 completed / 18 failed; verdict rejected-honest-stop", "failure": "antigravity aborted twice with zero seat output"},
        {"loop": 1, "position": 13, "round": 45, "route": null, "outcome": "skipped; no telemetry directory and no round commit", "failure": "operator ruling: antigravity lanes non-functional on this host"}
      ],
      "planned": {
        "loop_2": {"positions": [12, 13], "rounds": [58, 59], "policy": "skip/re-route", "source": "reports/round-46/loop-1-retrospective.md:59-60"},
        "loop_3": {"positions": [12, 13], "rounds": [72, 73], "policy": "to-verify", "source": "reports/round-46/loop-1-retrospective.md:52 names 'loop-2/3 argon' but no loop-3 plan is written"}
      },
      "authorization": "operator ruling, quoted in reports/round-44/telemetry/dispatch-declared.json:10 ('skip the gemini and argon rounds') and reports/round-44/telemetry/observed-dispatch.json:18; recorded at LOG.md:3850-3852 and reports/round-46/loop-1-retrospective.md:3-4,23",
      "owner": "operator (ruling) + integrator (re-route record and loop-2/3 dispatch)",
      "reason": "The position-12 and position-13 seats are scheduled on antigravity lanes that are non-functional on this host. Position 12 was re-routed to opencode-go after two zero-output aborts; position 13 was skipped outright. Recording the amendment keeps the requested-vs-observed split explicit (AGENTS.md telemetry rule) and prevents a later dispatch from re-declaring a dead lane as if it had been served. Not a defect row: no rule breach is alleged, and the parent queue's notes exclude named telemetry deviations from defect rows (reports/round-40/op/defect-queue-v2.json:8).",
      "next_touch": "Loop-2 position 12 (r58) and position 13 (r59): apply skip/re-route at dispatch, declare the requested antigravity lane plus the observed route in dispatch-declared.json before the batch, and close the route in availability-close. Loop-3 r72/r73 policy remains to-verify.",
      "evidence": [
        "reports/round-46/loop-1-retrospective.md:3-4,23,26,51-52,59-60 (sha256 a8e3fabb0d6502a03371be32632003fa3772f0ad39d15280847bcefc8b2d895d)",
        "reports/round-44/telemetry/dispatch-declared.json:10,17 (sha256 565e4fbd505c9e7ff652e9dff9e2bbdef07c1b9555932bf401fb5fdf68570844)",
        "reports/round-44/telemetry/observed-dispatch.json:17-18 (sha256 445daadfd5d375d66df333122f7f1ef170f8fd6dd1618dcebc24c8ce01203b4a)",
        "reports/round-44/telemetry/availability-close-44.json:24-28 (sha256 8a9146e1b3cc961b78e966cd08ecf61a8dcd17e2225897ce4e1b7b73ba5fa354)",
        "reports/round-43/telemetry/availability-close-43.json:26 (cursor/gemini-4-argon interruption)",
        "reports/round-47/telemetry/dispatch-declared.json:18 ('antigravity skipped (broken)')",
        "LOG.md:3848-3853; SCORECARD.md:855-858,871-872; REGIMEN.md:21-22,66-69,73-77"
      ],
      "verification": "Measured at HEAD 6e9a30d on 2026-10-19: ls -d reports/round-{33..46} lists 13 directories and reports/round-45 is absent; git log --all --grep='round 45' -i returns 0 commits; r44 telemetry records 'aborted x2, zero output' and the opencode-go re-route; the r44 round directory, validation receipt and 14/32 observed completion verify position 12 executed.",
      "to_verify": [
        "loop-3 positions 72/73: the retrospective names 'loop-2/3 argon' (:52) but no loop-3 provider plan is written; owner integrator.",
        "loop-2 position 12: whether r58 skips or re-routes is not yet decided; owner integrator at dispatch.",
        "the antigravity abort root cause is recorded as an observation, not diagnosed; owner operator."
      ],
      "wording_correction": "The Ca04 mission phrase 'positions 12/13 skipped' is not literally supported: position 12 (r44) was re-routed and executed; only position 13 (r45) was skipped. This row records the distinction and does not repeat the both-skipped formulation."
    },
    {
      "id": "PA-47-02-zai-exhaustion-luna-max",
      "kind": "provider-amendment",
      "defect_row": false,
      "class": "named-deviation",
      "v2_class_equivalent": null,
      "origin": "loop-1 position 11 (r43) zai lane interrupted pre-completion x2 and re-routed; loop-1 retrospective:53 declares zai usage exhausted; :57-60 amends loop-2 positions 7-8 and 11 to luna-max; r47 dispatch carries it as a standing amendment",
      "requested": [
        {"loop": 2, "position": 7, "round": 53, "lane": "zai-coding-plan/glm-5.3-flash (MAX-effort seats)", "workers": "16-32"},
        {"loop": 2, "position": 8, "round": 54, "lane": "zai-coding-plan/glm-5.3-flash (MAX-effort seats)", "workers": "16-32"},
        {"loop": 2, "position": 11, "round": 57, "lane": "zai-coding-plan/glm-5.3-flash-low (pinned MAX)", "workers": 32}
      ],
      "observed": [
        {"loop": 2, "positions": [7, 8, 11], "rounds": [53, 54, 57], "route": "openai-codex/gpt-6-luna-max", "status": "declared amendment; none of the three rounds has executed at r47 (loop-2 position 1 is the current round)"}
      ],
      "scope": "reports/round-46/loop-1-retrospective.md:53 says 'for the session'; the session boundary and loop-3 applicability are not defined",
      "authorization": "to-verify: the retrospective is the integrator's lane record (:53,:59) and r47 dispatch-declared carries it as standing (:18), but no explicit operator quote authorizing the zai->luna-max substitution is filed. The loop-1 zai interruption itself was an explicit operator instruction (reports/round-43/telemetry/dispatch-declared.json:9).",
      "owner": "operator (exhaustion ruling and substitute authorization) + integrator (dispatch declaration and telemetry)",
      "reason": "The position-7-8 and position-11 seats are scheduled on zai, whose usage is recorded exhausted; luna-max is the named substitute. Recording it as a named deviation keeps the requested-vs-observed split explicit and avoids an undeclared provider substitution under REGIMEN.md:66-69. Not a defect row: the loop-1 zai rounds (r39, r40) were admitted; the exhaustion is an availability fact, not a rule breach.",
      "next_touch": "At r53/r54/r57 dispatch: declare requested zai plus observed luna-max in dispatch-declared.json before the batch and close the route in availability-close. Loop-3 positions 67/68/71 applicability to be ruled (to-verify).",
      "evidence": [
        "reports/round-46/loop-1-retrospective.md:17-18,26,53,59 (sha256 a8e3fabb0d6502a03371be32632003fa3772f0ad39d15280847bcefc8b2d895d)",
        "reports/round-43/telemetry/dispatch-declared.json:8-9 (sha256 76632d7354f4aa602c0ba9c5d1e4f6780bedb3a4a6e2a372cde724745c7f63fe)",
        "reports/round-43/telemetry/observed-dispatch.json:20 (sha256 10181657c574dddc0fb1ce5b3b9be477b579cea4b871f3acf3a6c81d5dc1bf4f)",
        "reports/round-43/telemetry/availability-close-43.json:18,23-28 (sha256 eddfb5f334ee3a2f0931a1732e65606f9f6f0c1e3e824b7b39398ce1f0bdef48)",
        "reports/round-47/telemetry/dispatch-declared.json:18 (sha256 3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8)",
        "SCORECARD.md:833-835; REGIMEN.md:17,20,66-69,73-77"
      ],
      "verification": "Measured at HEAD 6e9a30d on 2026-10-19: r43 telemetry names requested zai-coding-plan/glm-5.3-flash-low and the interrupted route history; no dispatch-declared.json at r44, r46 or r47 names zai (lanes: opencode-go, devin, opencode-go); reports/round-45 does not exist. The exhaustion statement itself is lane-recorded, not provider-probed.",
      "to_verify": [
        "explicit operator authorization for zai->luna-max is not filed; owner operator/integrator.",
        "loop-3 positions 67/68/71 applicability is unstated; owner integrator.",
        "session boundary/expiry of the 'all session' amendment is undefined; owner operator.",
        "cause: the retrospective says 'usage exhausted' (:53) while r43 telemetry says 'interrupted x2' (:20); quota exhaustion vs lane instability is not established; owner integrator.",
        "no luna-max capacity/cost check is filed for the substituted seats; owner integrator."
      ],
      "evidence_grade": "lane-recorded: the exhaustion claim rests on the loop-1 retrospective (:53); provider-side quota/usage state is not observable from this repo and no zai availability probe is filed."
    }
  ]
}
```

## 5. Assembly guidance for Ca06

1. **Preferred shape:** add a top-level `provider_amendments` array to the
   successor and keep `rows[]` for defects. This preserves the parent’s
   deviations-not-defects rule (`defect-queue-v2.json:8`) and keeps the defect
   count comparable (38 parent rows + the Ca01–Ca03 disposition rows).
2. **If the successor schema is closed:** project each row to the eight v2
   fields. Keep `class: "named-deviation"`; set `v2_class_equivalent: null`.
   Do **not** map it to `carried-with-owner` without a `kind` marker, or the
   defect census will inflate by two.
3. **Parent pin:** carry
   `parent_sha256_at_assembly: dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`.
   The r43 successor’s `:6-8` history text is the precedent for recording the
   `fe596a9d…` → `ac47c78` in-place edit; do not edit the parent.
4. **Dedupe:** no existing parent row names antigravity or zai as a defect.
   `grep -i 'antigravity\|zai\|luna'` on the parent matches only the notes
   block (`:8`) and an unrelated receipt-fidelity row (`:375`, describing an
   r39 dispatch). No row collision.
5. **Do not absorb unrelated findings:** the r44 opencode-go
   `reasoning_content` defect (18 failed seats) and the r43 claims-digest drift
   are already recorded in their round telemetry; they are not part of these
   two amendments.

## 6. Verification (re-runnable)

Run from the repo root at HEAD `6e9a30d`:

```bash
sha256sum reports/round-40/op/defect-queue-v2.json
# dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907

git log --oneline -- reports/round-40/op/defect-queue-v2.json
# ac47c78 round-41: admit O/Ca — round-runner template + conformance checker ...
# 13a1657 round-40: admit C/Ca/A — linguistics 25 (220 total), defect-queue-v2 ...

git status --porcelain -- reports/round-40/op/defect-queue-v2.json
# (empty)

git diff --numstat 13a1657 ac47c78 -- reports/round-40/op/defect-queue-v2.json
# 15	5	reports/round-40/op/defect-queue-v2.json   (the recorded 20 changed lines)

ls -d reports/round-{33..46} 2>&1 | wc -l
# 14   (13 directories + the one "No such file" line)
ls -d reports/round-45 2>&1
# ls: cannot access 'reports/round-45': No such file or directory

git log --oneline --all --grep='round 45' -i | wc -l
# 0

python3 - <<'PY'
import json
for r in (43, 44, 47):
    p = f"reports/round-{r}/telemetry/dispatch-declared.json"
    d = json.load(open(p))
    print(r, d["provider_lane"], d["model"], "| deviation:", bool(d.get("deviation")))
PY
# 43 opencode-go deepseek-v4.1-flash | deviation: True
# 44 opencode-go deepseek-v4.1-flash | deviation: True
# 47 opencode-go deepseek-v4.1-flash | deviation: False
```

The fenced row block above was extracted and parsed with `json.loads` after
writing this file; both rows parse, carry non-empty `owner`, `reason` and
`evidence`, and every cited path exists. Line citations were bounds-checked
against each file’s line count (18/18 valid); the retrospective citations use
prose spans (e.g. `:51-52`) and each span was read in full. All nine digests
quoted in the rows and in §1 were recomputed from the live files and match.

## 7. To-verify (named owner)

| item | why unresolved | owner |
|---|---|---|
| loop-3 antigravity policy (r72/r73) | retrospective names “loop-2/3 argon” (`:52`) but writes no loop-3 plan | integrator |
| loop-2 position 12 skip vs re-route (r58) | decided at dispatch, not at r47 | integrator |
| explicit operator quote for zai→luna-max | retrospective is the integrator’s record; no operator quote filed | operator/integrator |
| loop-3 zai applicability (r67/r68/r71) | plan covers r47–r60 only (`:57`) | integrator |
| session boundary of “all session” | undefined in the retrospective (`:53`) | operator |
| zai cause: exhaustion vs interruptions | two filed phrasings describe different observations | integrator |
| luna-max capacity/cost for substituted seats | no check filed | integrator |

## 8. Handoff

- `Ca06`: extract §4’s fenced JSON into the successor, preferably as
  `provider_amendments[]`; pin the parent sha above; do not count these as
  defects.
- `Ca05`/`Ca07`: independently re-read the cited lines; re-run §6; confirm the
  parent sha is unchanged and that this file edited no filed byte.
- `R05`: review the classing — especially that the antigravity record does not
  repeat the “both positions skipped” error and that the zai row does not
  launder “interrupted x2” into “quota exhausted”.
- Residual for the round: none owed by this seat beyond this file. The two
  records are `named-deviation`; neither is a “fixed” claim, so neither carries
  a re-run command for a fix — the re-run evidence is the absence/presence
  checks in §6.
