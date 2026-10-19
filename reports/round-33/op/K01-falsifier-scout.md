- Seat: K01 | scout | claim O (falsifier leg) | date 2026-10-19 | baseline 139e3b6

# K01 — falsifier-audit filename mismatch: LOCATED and reproduced

Verdict: **located**. The round-32 routed debt "the falsifier audit's filename
mismatch (substance 5/5)" is finding **F-X16-3**, recorded at
`corpus/lessons/round-32.md:36` (§ heading) and `:41` (the finding), with its
open route Q-32-1 at `:55`. The instrument it audits is the executable
checklist item at `SKILL.md:713-715`, landed by commit `17e90b9`. Both legs
reproduced at lane HEAD `139e3b662900557afe54f632b468619593dc9fcb`
(2026-10-19): the audit **false-fires, printing 5 rows**; the substantive form
of the same check **passes 5/5** with live digest matches.

## 1. The naming artifact (exact path + quoted lines)

`corpus/lessons/round-32.md:36`:

> `## The falsifier legs — substance 5/5, instrument false-fires on day one`

`corpus/lessons/round-32.md:41` (F-X16-3, quoted in full — it is the sentence
SCORECARD compresses):

> - **F-X16-3 — the landed audit false-fires.** The `SKILL.md:715` audit, verbatim, prints **5 records** (`reports/round-{19,25,26,27,28}/availability.json` — all admitted rounds): it requires a file literally named `telemetry/closing-snapshot.json`, but the landed snapshots are named `telemetry/availability-close-N.json`. Every record it names IS closed; the instrument cannot see the closures. The draft's audit (`draft.md` §2.2) had the opposite defect — no closure check at all, so it would print the same five forever; the landing fixed the semantics and broke the path. `LOG.md`'s recorded falsification clause (i) — "if the checklist audit prints a non-empty list after this round for a round admitted to LOG.md, the rule is falsified and reverts" — has therefore **fired on day one for an instrumental reason**, while the substantive form of the same check (for each `open-at-seat-close` record, a snapshot in that round's `telemetry/` whose `closes_record` names it and whose `closes_sha256` matches) passes 5/5. Disposition belongs to parent/operator: re-key the audit to the landed convention or reword the clause — a new recorded change; this lesson does not edit the rule it audits.

`corpus/lessons/round-32.md:55` (the open route):

> - **Q-32-1 — parent/operator / falsifier disposition (F-X16-3):** the recorded falsification condition (i) has fired instrumentally; re-key the `SKILL.md:715` audit to the landed snapshot convention (`closes_record` + `closes_sha256`) or reword the clause — new recorded change, never in-place.

## 2. The two artifacts the mismatch joins

- **The instrument (the mismatch lives here).** `SKILL.md:713-714` states the
  rule; `SKILL.md:715` carries the one-liner, whose closure test is
  `not os.path.exists(.../telemetry/'closing-snapshot.json')` — a filename that
  exists nowhere in the repo (`find reports corpus tools -name
  'closing-snapshot.json'` → no matches; `ls
  reports/round-*/telemetry/closing-snapshot.json` → no such file, 2026-10-19).
  Landed by `17e90b9` (`git show 17e90b9 -- SKILL.md`), hunk `@@ -710,3 +710,6 @@`,
  appended at end of file inside `## Source-bounded culture drill — D3 (round 7)`
  (`SKILL.md:660`; `wc -l SKILL.md` = 715), **not** inside `## Checklist`
  (`SKILL.md:522-534`) — the separate F-X16-2 finding.
- **The landed snapshots (the actual convention).**
  `reports/round-{19,25,26,27,28}/telemetry/availability-close-N.json`, each
  `"schema": "kotodama-availability-closing-snapshot-v1"`, each carrying
  `"closes": "reports/round-N/availability.json"` + `closes_sha256`
  (e.g. `reports/round-19/telemetry/availability-close-19.json:2-5`).
- **The draft's audit (the pre-landing defect).**
  `reports/round-31/jinii/draft.md:38-45` (§2.2): its one-liner has **no
  closure test at all** — it would print the same five forever. The landing
  added the test but keyed it to `closing-snapshot.json`.

## 3. Reproduction, both legs (run 2026-10-19 at HEAD 139e3b6)

**Instrument leg — false-fires.** `SKILL.md:715` one-liner, verbatim:

```
$ python3 -B -c "import json,glob,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not os.path.exists(os.path.join('reports',f.split('/')[1],'telemetry','closing-snapshot.json'))]"
reports/round-19/availability.json
reports/round-25/availability.json
reports/round-26/availability.json
reports/round-27/availability.json
reports/round-28/availability.json
exit 0
```

Exactly 5 rows, matching the lesson's "prints 5 records". Record census
(same date): 9 `reports/round-*/availability*.json` files total — 3 round-10
attempts + 1 round-5 attempt (`state: None`, pre-convention) + the 5
`open-at-seat-close` records above.

**Substance leg — passes 5/5.** For each of the 5 open records, the snapshot in
that round's `telemetry/` names it via `closes` and its `closes_sha256` equals
the record's live sha256:

| record | closes_sha256 == live | digest |
|---|---|---|
| `reports/round-19/availability.json` | true | `fa9588db60c61a704f0e108ab011c3da47711cf78e5b6f39faec712bb373bd7d` |
| `reports/round-25/availability.json` | true | `51d62532bcbafab8220bc709b6b4d6924b5c8a9b4da4da517d175f98aaf7212d` |
| `reports/round-26/availability.json` | true | `7e23f33daa65514182cc3d6dca54bf6ea355c5b61d4f978261a7d366fe5f2b6c` |
| `reports/round-27/availability.json` | true | `987b04e12b7bcb33f8c64d6b259161cc66b6361c1d7e8e3fec9d30111cfdbf42` |
| `reports/round-28/availability.json` | true | `aceb019cfbec7fa904e587cda5581038cf0672e8a6a884c986f530b3effe99c1` |

**Nuance for O05's fix draft (new, not in the lesson).** The lesson and Q-32-1
paraphrase the snapshot key as `closes_record`; the **live schema key is
`closes`** (`reports/round-19/telemetry/availability-close-19.json:4`, and the
r31 validator reads `document.get("closes")` at
`reports/round-31/run-validation.py:799`). A re-keyed audit that tests
`closes_record` would false-fire a second time. The landed, working
implementation to mirror is `reports/round-31/run-validation.py:780`
(`closed_by_snapshot` = `telemetry/availability-close-<round>.json` exists) and
`:792-812` (`closing_snapshots`: digest-vs-live + `closed_record_unchanged_at_head`
via `git show HEAD:<closes>`).

## 4. Routing record (where the debt is named; where it is not)

- Named: `SCORECARD.md:443-445` ("Routed debt recorded for the operator: the
  falsifier audit's filename mismatch (substance 5/5), 7 unindexed lessons, 12
  standing open items…"); `LOG.md:3512-3514` (regimen-2 standing inputs);
  `corpus/lessons/round-32.md:41,55`.
- The falsification clause it fires against: `LOG.md:3460-3468`, clause (i) at
  `:3460-3463` ("if the checklist audit … prints a non-empty list after this
  round for a round admitted to LOG.md, the rule is falsified and reverts").
- **Not named** in: `reports/round-32/**` (grep `-ril falsifier` → only
  `run-validation.py`, `final-dossier.md`, `scribe/fragment-ledger.md`,
  `validation.json`, all in the unrelated "promotion-checklist falsifier"
  sense; the dossier fragments call the item merely "executable"
  — `reports/round-32/dossier-d11-shonen-boxes.md:160`,
  `dossier-d12-capability-inventory.md:55`); `reports/round-31/**` (grep
  `-rn -i falsifier` → `report-draft.md:34`, `jinii/analysis.md:94,136`,
  `jinii/draft.md:94,101,106,120`, `validation.json:150,152,1072` — none names
  the filename mismatch); fleet `.ufo/reports/round-30/kotodama.md` (no
  matches); `.ufo/reports/round-31/kotodama.md:25` ("checklist gains the
  closing-snapshot audit; five retroactive closing…" — no mismatch);
  `.ufo/reports/round-32/kotodama.md:32` ("zero falsifiers" — about
  completion-audit independence, unrelated). The lesson file is the sole
  artifact that states the mismatch.

## 5. Disposition inputs handed to O05 / P01 (bounded, no filed-byte rewrite)

1. **Bounded fix (preferred).** Replace the `SKILL.md:715` test
   `not os.path.exists(.../telemetry/'closing-snapshot.json')` with the landed
   convention (glob `telemetry/availability-close*.json` + `closes`/`closes_sha256`
   match, mirroring `reports/round-31/run-validation.py:792-812`). Shared-file
   change → integrator applies; control = the re-keyed one-liner must print
   nothing now (5/5 closed) and must print a row when a snapshot is absent
   (negative control on a scratch copy).
2. **Clause reword (alternative).** Reword LOG.md clause (i) to name the landed
   convention — append-only, so a new dated LOG entry, never an edit.
3. **Integrity leg already green** (5/5 digests) and enforced live by
   `reports/round-31/run-validation.py`; no repair needed there.

## Owed: none

## Citations

- `corpus/lessons/round-32.md:36` (heading), `:41` (F-X16-3), `:55` (Q-32-1); sha256 `8aacfc2bd9f55ec9dae3a721dc793a83bf071e90b98955ffa2cb45a33437ab64`
- `SKILL.md:522-534` (Checklist section), `:660` (D3 heading), `:713-715` (item + one-liner); sha256 `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`; `wc -l SKILL.md` = 715
- `SCORECARD.md:443-445`; `LOG.md:3460-3468` (falsification clause), `:3512-3514` (regimen-2 standing inputs)
- `reports/round-31/jinii/draft.md:38-45` (§2.2 draft audit), `:90-125` (falsifiers); `reports/round-31/run-validation.py:780`, `:792-812`; `reports/round-31/report-draft.md:34`
- `reports/round-19/telemetry/availability-close-19.json:2-5` (schema, `closes`, `closes_sha256`); same shape in rounds 25–28
- `reports/round-32/dossier-d11-shonen-boxes.md:160`; `reports/round-32/dossier-d12-capability-inventory.md:55`
- Commands (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`; verbatim `SKILL.md:715` one-liner (5 rows, exit 0); snapshot-substance probe over the 5 open records (5/5 `closes_sha256` match); `git show 17e90b9 -- SKILL.md`; `git log -S 'closing-snapshot.json' -- SKILL.md` → `17e90b9`; `grep -ril falsifier reports/round-32/`; `grep -rn -i 'falsifier|filename|closing-snapshot|availability-close' .ufo/reports/round-{30,31,32}/kotodama.md`; `find reports corpus tools -name 'closing-snapshot.json'` → none; `ls reports/round-*/telemetry/closing-snapshot.json` → none
