# ExecReceiptRerun — R2 feasibility: round-72 `accept-ca.py` post-report rerun

Seat: ExecReceiptRerun (leaf, round 73, wave 1). Attack surface: claim **Ca** leg REPAIR item R2
(`reports/round-73/claims.json`, DRAFT-v0 — read, never edited). All lane reads/writes absolute
under `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; fleet repo read-only; `shokuknow` untouched.

## Verdict

**R2 is REPAIR, not ANNOTATE.** A committed post-report rerun receipt at a pinned revision is
producible: at `lands = 21ad3088cb64f7275e5541804e168f15d21d26d0` — the stamped revision of the
committed FAIL receipt itself — the frozen counter now prints
`ACCEPT-CA-72: PASS legs=12/12` with exit 0, deterministically, including from a clone
*checked out* at that revision (materialized-clone requirement of the round-73 STAMP leg).
Target receipt file: `reports/round-73/telemetry/measures-ca72-rerun.txt`.

The two lands named in the assignment **both FAIL 11/12, and the sole failing leg is REPORTLAST**
in both cases. REPORTLAST fails there for one mechanical reason: it requires `lands[:7]` to appear
in the fleet report, and the landed report names `ac0d18ee`, `11a41fbf` and `21ad308` — never
`3adbd4a` or `8841ad3`. REPORTCORR, the leg the committed receipt records as FAIL, now PASSES at
both lands.

## Measured legs

Counter bytes identical at every lands tested (`git show <lands>:reports/round-72/accept-ca.py` →
`sha256 f080c240ffdc47f0453f4527e23d271112c999dc59d3d63d2703aae10880629f`, matching the committed
receipt header `# counter sha256 (self): f080c240ffdc47f0`). Command shape, exactly as assigned,
run with cwd = the clone and `--root .`:

```
python3 -B reports/round-72/accept-ca.py --root . --lands <lands> \
  --fleet-root /home/vgpnk/Projects/shokunin
```

| lands | tree | commits base..lands | verdict | exit | REPORTCORR | REPORTLAST | APPENDONLY |
|---|---|---|---|---|---|---|---|
| `3adbd4abef978a5d64d682c8f302a09e416cc1a6` (round-72 last work commit) | `2a0103fa…` | 17 | **FAIL 11/12** | 1 | PASS (`fleet-rev=80d8c9b576d4`) | **FAIL** (`report-names-lands=False`) | PASS (`removed=0 numstat-del=0 w2-changed=7 unauthorized=[] fleet-r71-last=f47ad6ba8d30`) |
| `8841ad3b896a0227674fa0725b818c999118046f` (round-73 base) | `17c286f5…` | 18 | **FAIL 11/12** | 1 | PASS (`fleet-rev=80d8c9b576d4`) | **FAIL** (`report-names-lands=False`) | PASS (`removed=0 numstat-del=0 w2-changed=7 unauthorized=[] fleet-r71-last=f47ad6ba8d30`) |
| `21ad3088cb64f7275e5541804e168f15d21d26d0` (receipt's own stamp) | `e4e49089…` | 10 | **PASS 12/12** | 0 | PASS | PASS (`report-names-lands=True`) | PASS |
| `ac0d18eea757acd9aac5a32cf8fd9089d2702167` (report's graded revision) | `cf74d6a8…` | 11 | **PASS 12/12** | 0 | PASS | PASS | PASS |
| `11a41fbfe064b0ebf51366ec7361c67cb215d5ec` (report's declared final lane HEAD) | `a21e26e1…` | 12 | **PASS 12/12** | 0 | PASS | PASS | PASS |

All other legs (QUAL20, W2FILES, LOGCORR, LESSONCORR, MAPCORR, CASTAMP, QUAL21, CAPOEIRA, NOHARM
`census exit=0`) PASS in every row; no leg other than REPORTLAST ever differed. Re-run at
`21ad3088` twice → byte-identical output; the materialized clone (`/tmp/tmp.LsQJKzjafS`, detached at
`21ad3088`) produced bytes identical to the first clone (`/tmp/tmp.DuAPz85llT`, HEAD `8841ad3b`).

## Why the requested lands cannot carry a PASS

REPORTLAST's test (counter lines 218–222) is `lands[:7] in report and "b60c7b1" in report and
"99e3d63" in report`. The fleet report at its current bytes (fleet HEAD `9f4bfc4976007fd0…`,
report last-touch `80d8c9b576d45d3c…` erratum 5, blob `87b67f1ed036f883…`,
`sha256 ea256ae7f9d758e0962a7fdfeea446d8963e3f7ef1314aeacc6a7334509834be`) contains `b60c7b1` (4×)
and `99e3d63` (4×) but names its revisions as:

- line 3: "final lane HEAD `11a41fbf` (round work graded at `ac0d18ee`" — so `ac0d18ee` and
  `11a41fbf` satisfy the leg;
- line 22: "`b47033a`/`ba8ad3a`/`5897ddf`/`21ad308` — LOG round-72 entry" — so `21ad308` (the
  receipt's own stamp) satisfies the leg via a commit roll-up.

Neither `3adbd4a` nor `8841ad3` occurs anywhere in the report (grep counts 0). A PASS at either of
the two requested lands would require appending an erratum to the fleet report naming that hash —
a fleet write, outside this seat and unnecessary, since the stamp revision already passes.

## REPORTCORR post-report: confirmed

The committed receipt's FAIL (`fleet-rev=MISSING`) was a missing-report artefact. Post-report, the
leg reads `fleet-rev=80d8c9b576d4` and its token test (`:57`, `:61`, `S861→S992`) passes. This
independently exercises the fleet report's own statement, line 27: "pass on the post-report rerun
at the same revision (verified after filing: both counters re-run, REPORTCORR+REPORTLAST PASS)"
(17 words). The committed receipt's header note is now literally true:
"# note: REPORTCORR/REPORTLAST evaluate the fleet report; PASS on the post-report rerun at this
revision" (15 words).

## Repair recipe for whoever lands R2 (not written by this seat)

`reports/round-73/telemetry/measures-ca72-rerun.txt`, produced in a materialized clone and
prefixed with the same header shape as the round-72 receipt (the counter prints no header):

```
D=$(mktemp -d) && git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane" \
  && git -C "$D/lane" checkout -q --detach 21ad3088cb64f7275e5541804e168f15d21d26d0 \
  && cd "$D/lane" \
  && python3 -B reports/round-72/accept-ca.py --root . \
       --lands 21ad3088cb64f7275e5541804e168f15d21d26d0 \
       --fleet-root /home/vgpnk/Projects/shokunin
```

Header pins the receipt must carry so the verdict is reproducible later (all read from the code,
all observed today):

- lands `21ad3088cb64f7275e5541804e168f15d21d26d0`, tree `e4e490892002c6621e75df5542530b987c5ea078`;
- counter sha256 `f080c240ffdc47f0453f4527e23d271112c999dc59d3d63d2703aae10880629f`;
- **fleet** HEAD `9f4bfc4976007fd0fa0c3e2f0492efd9ac80f26e`, r72 report blob
  `87b67f1ed036f88305a4bc105d150f8c6858ae7a` (sha256 `ea256ae7…`), last-touch `80d8c9b576d4…`,
  r71 report last-touch `f47ad6ba8d30…`.

## Findings and risks for the claim text (critic-facing, no edit made)

1. **The verdict is not a function of the lane revision alone.** REPORTCORR/REPORTLAST read the
   fleet repo at its *current* HEAD, and APPENDONLY reads the fleet r71 report's last-touch and
   compares bytes to `8380f703` (`f47ad6ba8d30` is not in `KNOWN_R71_REPORT_COMMITS`, so it passes
   only via the byte-identity branch). Pinning the lane revision pins the counter but not the
   verdict — exactly the QUALITY 17/19 gap the round-73 `mistake_to_mine` names. A repair receipt
   that records only the lane stamp would be unreproducible the moment fleet bytes move; hence the
   fleet pins above.
2. **REPORTLAST is token presence, not grading.** At `21ad3088` it passes because line 22 lists the
   commit in a roll-up, not because the report grades that revision; the same leg fails at
   `3adbd4ab`/`8841ad3b` where the report's only grading statement names `ac0d18ee`. The round-73
   Ca REPAIR wording ("a PASS stamp at the stamped revision for REPORTCORR+REPORTLAST") is met
   literally, but the leg does not establish what its name suggests. [INFERENCE from reading
   counter lines 218–222; the three-lands experiment is the direct evidence.]
3. **Three admissible lands, not one.** `21ad3088` (stamp; recommended — only fleet state changed
   since the FAIL receipt), `ac0d18ee` (graded), `11a41fbf` (declared final lane HEAD) all print
   PASS 12/12; their leg blocks differ only in REPORTLAST's `commits=` counter (10 / 11 / 12). If
   round-73 prefers the graded revision, `ac0d18ee` is equally producible.
4. **The FAIL cannot be repaired at the round-73 base.** At `8841ad3b` the counter exits 1, so a
   receipt filed at the round-73 tip would read FAIL; the receipt must pin one of the three
   report-named revisions.
5. **Counter edits invalidate the pin.** `f080c240…` is constant across all five lands tested; if
   round-73 touches `accept-ca.py` the sha changes and the rerun must be redone against the new
   bytes.
6. Not tested (out of write path): fleet states after a further r72-report erratum. Read of code
   says REPORTCORR survives any amendment keeping `:57`, `:61`, `S861→S992`, and REPORTLAST any
   keeping the pinned hash token; not exercised.

## Retained evidence

Raw counter output, written only under the wave drafts path (lane git-tracked files untouched —
`git diff --stat` empty, `git status` unchanged: the same four `??` entries as before this seat ran):

| file (`…/.ufo/waves/round-73/w1/drafts/`) | sha256 |
|---|---|
| `ca72-rerun-3adbd4ab.txt` | `a9ede87dda5a5826c5c7e1ace7ea3ef82f5706d1aeed90f4edfbd59959f356d8` |
| `ca72-rerun-8841ad3b.txt` | `d612c1405beee5591755fb16e0b708f22d3b8fb021cf730a9cb38a063995c187` |
| `ca72-rerun-21ad3088.txt` | `7cca9a10a6c21e2dcfd042a37d249882226f978090cf350962f24f81a3709eb1` |
| `ca72-rerun-ac0d18ee.txt` | `a8e0dca2c9d4e7225250ac8c1500a087f41111727b49417246d0e9f84319dd34` |
| `ca72-rerun-11a41fbf.txt` | `27744ebf816ac92a5eefc733a105e8aaa357d6fe034f8506701e8eae93484350` |

Scratch (outside the lane, `/tmp` only): first clone `/tmp/tmp.DuAPz85llT` (HEAD `8841ad3b`);
materialized clone `/tmp/tmp.LsQJKzjafS` (detached `21ad3088`); determinism copies
`/tmp/ExecReceiptRerun.rerun2.txt`, `/tmp/ExecReceiptRerun.mat.txt` (both byte-identical to the
`21ad3088` draft). No live fetch, so no User-Agent record is owed; no captures, no CDX probes.

## Tooling and hygiene

No installs, no upgrades, no `pacman` (host-wide pause honoured); no delegation, no background
jobs. Fixture repos created only via `mktemp -d` + `git clone` of the lane's local path; every git
call named `-C <dir>`; no commits made anywhere. Lane `jj`/git state untouched; `reports/round-73/
claims.json` read only.
