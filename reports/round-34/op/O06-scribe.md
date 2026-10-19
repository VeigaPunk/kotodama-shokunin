- Seat: O06 | scribe (executor) | claim O | date 2026-10-19 | baseline da68a6d

# Claim-O receipt + landed-changes material

## Status and scope

Claim O = capability acquisition: land `tools/harness/receipt_guard_adoption.py`,
an audit instrument that inventories every filed round runner, classifies whether
it writes its own `validation.json` in place and whether it adopts
`tools/harness/receipt_guard.py`, and files the durable adoption inventory (the
F-C13-1 routing artifact) — `reports/round-34/claims.json:41`.

At scribe time **no `op/` dependency fragment had landed** (`ls reports/round-34/`
→ only `claims.json`, `targets.json`, `telemetry/`; `reports/round-34/op/` did not
exist). Per the missing-dependency rule I did every part that does not depend on a
missing fragment: I built the claim-O ground truth myself by read-only static
analysis (command recorded in §3), ran the guard controls that are runnable at HEAD
(§4), and drafted the receipt and landed-changes material below. The tool/inventory
selftest legs are recorded as `could-not-evaluate` with owners (§5).

## 1. Before → after (claim O)

**Before (recorded at da68a6d):**

- F-C13-1 incident (`LOG.md:3548-3566`): during the round-33 wave
  `reports/round-{5,6,7}/validation.json` were rewritten in the working tree
  (`LOG.md:3551-3553`, window 03:53:25Z–03:55:27Z) and restored byte-exact.
- Mechanism filed as a **guard-adoption gap, not a guard defect**
  (`LOG.md:3557-3560`), citing `reports/round-5/run-validation.py:194`,
  `reports/round-7/run-validation.py:1171`, `reports/round-6/run-validation.py:336`
  and claiming **"The r26 runner carries the same hazard (`:90`, `:1909`)"**
  (`LOG.md:3559-3560`), routed as a standing operability debt (`LOG.md:3565-3566`).
- No inventory instrument exists for the class; the guard itself has existed since
  round 14 (`tools/harness/receipt_guard.py`, 373 lines) and its selftest is green
  at HEAD (§4).

**After required** (`reports/round-34/claims.json:45`): the tool is durable with
selftest green (positive: the r32 guarded-refresh pattern recognized as adopted;
negative: a guarded runner NOT flagged, a non-runner writing JSON NOT flagged); the
inventory JSON names every `reports/round-*/run-validation.py` with its adoption
class and the four known hazards classified; a receipt draft names the routing.

**Observed at scribe time:** the deliverable tool is **not landed**
(`tools/harness/receipt_guard_adoption.py` → absent; `ls tools/harness/` →
`packet_links.py packet_uncertainty.py r8_checks.py receipt_guard.py`), so the
claim-O after-state is **not yet achieved**. What is achieved here is the
independently measured reference the landed tool must reproduce, plus one
correction to the claim's own "known hazards" list (§2.3).

## 2. Independent 28-runner adoption census (reference inventory)

Command (read-only, no writes; run at da68a6d):

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import glob,re,hashlib
for p in sorted(glob.glob("reports/round-*/run-validation.py"), key=lambda x:int(re.search(r'round-(\d+)',x).group(1))):
    b=open(p,"rb").read()
    n=re.search(r'round-(\d+)',p).group(1)
    print(f"round-{n}\t{len(b.splitlines())}\t{hashlib.sha256(b).hexdigest()}")
PY
```

Population: **28 runners** in `reports/round-5 … round-33` (rounds 5–12, 14–33;
there is no `reports/round-13/`. `ls -1 reports/round-*/run-validation.py`).

### 2.1 Adopted — 17 runners guard their own receipt write

| runner | guard definition / import site | guard call site(s) | own-receipt write |
|---|---|---|---|
| r14 | `module.guard_receipt(...)` :420 (helper `guard_preflight`) | :715 (call) | :717 |
| r15 | `module.guard_receipt(...)` :1044 | :1044 | :1346 |
| r16 | `module.guard_receipt(...)` :1005 | :1005 | :1265 |
| r17 | `module.guard_receipt(...)` :1124 | :1124 | :1431 |
| r18 | `module.guard_receipt(...)` :1518 | :1518 | :1851 |
| r20 | `module.guard_receipt(...)` :1285 | :1285 | :1485 |
| r22 | `def guard_receipt()` :827 (`runpy.run_path(tools/harness/receipt_guard.py)`) | :911, :921 | :922 |
| r23 | `def guard_receipt()` :1064 | :1094 | :1097 |
| r24 | `def guard_receipt()` :1151 | :1181 | :1184 |
| r25 | `def guard_receipt()` :1108 | :1142 | :1145 |
| r26 | `def guard_receipt()` :1855 | **:1906** (immediately before write, inside `else` branch :1905-1907) | **:1909** |
| r27 | `def guard_receipt()` :1853 | :1904 | :1907 |
| r28 | `def guard_receipt()` :1996 | :2095 | :2098 |
| r30 | `def guard_receipt()` :883 | :903 (pre-measure), :922 (pre-write) | :923 |
| r31 | `def guard_receipt()` :1118 | :1139, :1158 | :1159 |
| r32 | `def guard_receipt()` :1102 | :1123, :1142 | :1143 |
| r33 | `def guard_receipt()` :1441 | :1459, :1470 | :1471 |

Two-phase (guard before `measure()` and again before publish) confirmed by reading
`reports/round-32/run-validation.py:1119-1143` and
`reports/round-33/run-validation.py:1458-1471`; the write branch is
`else: guard_receipt(); safe_path(OUTPUT).write_text(rendered, ...)`.

### 2.2 Unguarded — 11 runners rewrite their own filed receipt with no guard

| runner | own-receipt write | guard / REFRESH mention | filed receipt committed |
|---|---|---|---|
| r5 | `:194` | none | yes |
| r6 | `:336` | none | yes |
| r7 | `:1171-1172` | none | yes |
| r8 | `:1485-1486` (`OUTPUT_REL` :99) | none | yes |
| r9 | `:1909-1910` (`OUTPUT_REL` :127) | none | yes |
| r10 | `:1053-1054` (`OUTPUT_REL` :60) | none | yes |
| r11 | `:1738-1740` (`OUTPUT_REL` :125) | none | yes |
| r12 | `:1069-1071` | none (policy note :1062: "does not invoke historical round runners, which would rewrite their validation.json files") | yes |
| r19 | `:21` (write inside embedded `python -c`; whole file is 24 lines) | none | yes |
| r21 | `:1113-1115` | none for its **own** write; `.scratch` clone driver sets `env["REFRESH_RECEIPTS"] = "1"` at `:474` for replayed r17–r20 (documented :1106) | yes |
| r29 | `:922` | none (no guard even though it uses the `safe_path(OUTPUT)` idiom r32 guards) | yes |

Commands: `grep -n "receipt_guard\|REFRESH_RECEIPTS\|round_runner_main\|guard_receipt"`
over the eleven files → only hits are `reports/round-21/run-validation.py:474` and
`:1106` (clone driver, not its own write); `for r in 5 6 7 8 9 10 11 12 19 21 29; do
git cat-file -e HEAD:reports/round-$r/validation.json; done` → committed for all
eleven.

### 2.3 The claim's "four known hazards" is a mis-count, and one of the four is wrong

- **Confirmed hazards (3 of the 4 named):** r5 `:194`, r6 `:336`, r7 `:1171-1172` —
  in-place writes with no guard anywhere in the file. Matches `LOG.md:3557-3559`.
- **r26 is NOT a hazard — evidence contradicts the filing.** `LOG.md:3559-3560`
  says "The r26 runner carries the same hazard (`:90`, `:1909`)". The current bytes
  define `guard_receipt()` at `reports/round-26/run-validation.py:1855-1857` and
  **call it at :1906 before the write at :1909**. History check:
  `git log --oneline -- reports/round-26/run-validation.py` → single commit
  `4f09c99` (round-26's own admission commit), `git log -S'def guard_receipt' --
  reports/round-26/run-validation.py` → same commit, `git status --porcelain
  reports/round-26/run-validation.py` → clean. So r26 adopted the guard at filing
  and has never been edited since; its class is **adopted (single pre-write check,
  not two-phase)**.
  - `to-verify`: why `LOG.md:3559` recorded otherwise is not provable from bytes;
    the plausible reading (author read `:90`/`:1909` and missed the guard call two
    lines above `:1909`) is a hypothesis, not a finding.
- **The hazard set is under-counted, not over-counted:** 11 runners carry the class,
  not 4 — the eight unnamed ones are r8, r9, r10, r11, r12, r19, r21, r29 (§2.2).
  Any routing artifact that covers only "the four" leaves eight filed receipts
  rewritable.

This is the O-class correction the round must file: an **errata row** for
`LOG.md:3559` plus the widened hazard census (draft in §6.2; the integrator owns
the append — seats never write shared bookkeeping, `AGENTS.md`).

## 3. F-C13-1 prevention controls observed at HEAD

All commands below were run at da68a6d; the only artifact touched was
`reports/round-5/validation.json`, and only by digest check (proved unchanged).

1. Guard selftest: `python3 tools/harness/receipt_guard.py --selftest` →
   `tools/harness/receipt_guard.py 45 / 45 True` (parsed
   `controls_passed`/`controls_total`/`selftest_passed`).
2. Guard refusal on a filed receipt (in-tree, no refresh):
   `python3 tools/harness/receipt_guard.py reports/round-5/validation.json` →
   stderr `receipt_guard: refusing overwrite path=reports/round-5/validation.json
   committed_sha=da68a6d705e41f369f21e8607bfaab5b54077f84
   committed_blob=778c3f5e172405d73eab790b8d6fee4c3282caa0; explicit
   REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]`, **exit 3**.
3. Same path with the explicit env:
   `REFRESH_RECEIPTS=1 python3 tools/harness/receipt_guard.py
   reports/round-5/validation.json` → `[RECEIPT-GUARD-REFRESH]`, exit 0 — and the
   CLI performs no write in either mode.
4. No mutation: `sha256sum reports/round-5/validation.json` →
   `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794` **before and
   after**; `git status --porcelain reports/round-5/` → empty.
5. No filed round runner was executed anywhere in this seat's work; the only round
   bytes read were `run-validation.py` sources, `validation.json` digests and
   `git` metadata.

Routing consequence for the F-C13-1 artifact, evidenced by the above: a runner that
adopts the guard **cannot** rewrite its filed receipt in-tree without
`REFRESH_RECEIPTS=1` (control 2 = exit 3), so adopted runners re-run in-tree only
under the explicit refresh protocol, and the 11 unguarded runners must be executed
**only from isolated `git archive` copies** — the same protocol round 21 already
uses for its clone replays (`reports/round-21/run-validation.py:474,1106`).

## 4. Counting-command ledger (claim O)

| counting command (`claims.json:46-50`) | status at scribe time | evidence |
|---|---|---|
| `python3 tools/harness/receipt_guard_adoption.py --selftest` | **could-not-evaluate** — tool not landed | `ls tools/harness/` shows no such file |
| `python3 tools/harness/receipt_guard_adoption.py --json` | **could-not-evaluate** — tool not landed | same |
| `python3 reports/round-34/run-validation.py` | **does not exist** (round in flight) | `ls reports/round-34/` → claims.json, targets.json, telemetry/ |

Owner of the missing legs: seats O02 (tool source draft) / O01 (impl) / O03
(selftest) / O04 (predicted inventory), verified by O07 (extract + run selftest and
`--json`, row-for-row against O04) and O08 (adversarial traps: guard imported but
not called; guard only under a flag; write via `os.replace`). The census in §2 is
the row-for-row reference those legs should be compared against: 28 rows, 17
adopted / 11 unguarded, with the four named hazards resolved as 3 confirmed + 1
reclassified.

## 5. Landed changes (commit-ready list, integrator applies)

| path | status | content |
|---|---|---|
| `tools/harness/receipt_guard_adoption.py` | **owed** — draft should ship from `reports/round-34/op/O02-tool-source.md` | stdlib-only AST/regex inventory + `--selftest` + `--json` |
| adoption inventory JSON | **owed**, path owned by O01/O05 | must name all 28 runners (§2) with class + the 3+1 hazard disposition |
| `reports/round-34/op/O05-routing.md` | **owed** | F-C13-1 routing: 11 unguarded → isolated-copy-only; 17 adopted → `REFRESH_RECEIPTS=1` refresh protocol |
| SCORECARD standing debt row (guard-adoption gap) | **draft in §6.1** | row text ready; integrator lands it in the round's SCORECARD edit |
| `LOG.md` errata row for `LOG.md:3559` (r26 class) | **draft in §6.2** | new row only; filed bytes untouched |
| this fragment's §2 census | landed here | the reference inventory the tool must reproduce |

No shared file was edited by this seat; nothing was committed or pushed.

### 5.1 Fleet-report material — claim O

**Work performed:** built the independent 28-runner adoption census by static
read-only analysis (§2); resolved the claim's four named hazards into 3 confirmed
unguarded writers + r26 reclassified as adopted on byte evidence, discovering an
eight-runner under-count of the hazard class (11 total); ran the guard's selftest
(45/45) and the committed-receipt refusal/refresh controls (exit 3 / exit 0) with
digest proof of zero mutation; filed the counting-command ledger with honest
`could-not-evaluate` status for the unlanded tool.

**Landed changes:** none in this seat beyond this fragment (scribe seat, out path
only). The claim's landed set is the tool + inventory + routing receipt (§5), all
still owed by the O block.

## 6. Drafts for the integrator (text only — not applied)

### 6.1 SCORECARD standing-debt row (claim O)

> **Guard-adoption gap (F-C13-1)** — 11 of 28 filed round runners
> (`reports/round-{5,6,7,8,9,10,11,12,19,21,29}/run-validation.py`) write their own
> `validation.json` in place with no adoption of `tools/harness/receipt_guard.py`
> (write sites per `reports/round-34/op/O06-scribe.md` §2.2). Runners are filed
> bytes and are not repaired in place; re-runs must use isolated `git archive`
> copies. Correction to the round-33 record: `reports/round-26/run-validation.py`
> is **adopted** (guard call `:1906` before write `:1909`), contrary to
> `LOG.md:3559-3560`.

### 6.2 LOG errata row (append-only; integrator applies)

> **2026-10-19 — Erratum to F-C13-1: r26 hazard classification and hazard census
> (new row; no filed byte rewritten).** The F-C13-1 record (`LOG.md:3559-3560`)
> states "The r26 runner carries the same hazard (`:90`, `:1909`)". Byte evidence
> contradicts this: `reports/round-26/run-validation.py:1855-1857` defines
> `guard_receipt()` and `:1906` calls it before the write at `:1909`; the file has
> one history entry (`4f09c99`, its own admission commit) and is clean at HEAD.
> Class: adopted. The hazard census is also wider than the four named hazards —
> the round-34 claim-O census (`reports/round-34/op/O06-scribe.md` §2) finds **11**
> unguarded in-place writers: r5:194, r6:336, r7:1171, r8:1485, r9:1909, r10:1053,
> r11:1738, r12:1069, r19:21, r21:1113, r29:922. Routing: isolated-copy-only for
> those 11; `REFRESH_RECEIPTS=1` refresh protocol for the 17 adopted runners.

## Owed

| owed path / item | owner | why |
|---|---|---|
| `reports/round-34/op/O01-impl.md` | O01 | not landed at scribe time |
| `reports/round-34/op/O02-tool-source.md` | O02 | the tool bytes (`tools/harness/receipt_guard_adoption.py` cannot be landed without them) |
| `reports/round-34/op/O03-selftest.md` | O03 | selftest control list |
| `reports/round-34/op/O04-predicted-inventory.md` | O04 | predicted inventory — compare row-for-row with §2 |
| `reports/round-34/op/O05-routing.md` | O05 | F-C13-1 routing receipt draft |
| `reports/round-34/op/O07-verify-tool.md`, `op/O08-traps.md`, `op/O09-verify-routing.md`, `op/O10-final-receipt.md` | O07–O10 | verification legs; the three counting commands stay `could-not-evaluate` until the tool lands |
| inventory JSON durable path | integrator | claims.json fixes the command, not the filing path |
| `LOG.md` errata row (§6.2) + SCORECARD row (§6.1) | integrator | shared bookkeeping is never written by seats (`AGENTS.md`) |

## Citations

- `reports/round-34/claims.json:41`, `:45`, `:46-50` (claim O text, after_required, counting commands)
- `reports/round-34/targets.json:44-53` (O-seat missions), `:49` (O06 mission/out)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/AGENTS.md` (telemetry/append-only rules)
- `REGIMEN.md:25-50` (per-round contract), `:52-58` (done-when)
- `LOG.md:3548-3566` (F-C13-1 incident record; `:3551-3553` rewrite window, `:3557-3560` mechanism + r26 claim, `:3565-3566` standing debt routing)
- `tools/harness/receipt_guard.py` (373 lines; `:144-149` refusal/refresh diagnostics, `:152-168` `guard_receipt`/`round_runner_main`, `:201-351` selftest)
- Commands run (all at da68a6d, read-only): `ls -1 reports/round-*/run-validation.py`; the census python heredoc in §2; `grep -n "receipt_guard\|REFRESH_RECEIPTS\|round_runner_main\|guard_receipt"` over the 11 unguarded runners and over all runners; `git cat-file -e HEAD:reports/round-<N>/validation.json` for N∈{5,6,7,8,9,10,11,12,19,21,29}; `git log --oneline -- reports/round-26/run-validation.py`; `git log -S'def guard_receipt' -- reports/round-26/run-validation.py`; `git status --porcelain reports/round-26/run-validation.py reports/round-5/`; `python3 tools/harness/receipt_guard.py --selftest` → 45/45 True; `python3 tools/harness/receipt_guard.py reports/round-5/validation.json` → exit 3 `[RECEIPT-GUARD-COMMITTED]`; `REFRESH_RECEIPTS=1 python3 tools/harness/receipt_guard.py reports/round-5/validation.json` → exit 0 `[RECEIPT-GUARD-REFRESH]`; `sha256sum reports/round-5/validation.json` (73a66f74…, unchanged)
- Per-runner file:line evidence for guard defs/calls/writes: r14 :420/:715/:717; r15 :1044/:1346; r16 :1005/:1265; r17 :1124/:1431; r18 :1518/:1851; r20 :1285/:1485; r22 :827/:911/:921/:922; r23 :1064/:1094/:1097; r24 :1151/:1181/:1184; r25 :1108/:1142/:1145; r26 :1855/:1906/:1909; r27 :1853/:1904/:1907; r28 :1996/:2095/:2098; r30 :883/:903/:922/:923; r31 :1118/:1139/:1158/:1159; r32 :1102/:1123/:1142/:1143; r33 :1441/:1459/:1470/:1471; and §2.2 write sites
