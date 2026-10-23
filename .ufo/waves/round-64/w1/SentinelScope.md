# SentinelScope — Round 64 wave 1

Judged axes: coverage, operability, calibration. Scope: misrooted-write sweep only. No tools installed.

## Findings

- **Informational — fleet-root untracked metadata.** One untracked file outside all `*-shokunin` repositories contains a Kotodama round-64 record: `.ufo/waves/hyaku/inline-run-20261023.md` (`| kotodama | 64 | 1 | 19:31 |`). This is a fleet orchestration note, not a seat report. No untracked seat report was found at the fleet root.
- **No misplaced seat reports found.** Every seat report present under `round-64/w1/` and `round-64/w2/` has a seat-named basename, consistent with the corresponding `Report:` trailer paths in the wave taskcalls. The only Markdown files found outside those directories are the two shared entry skeletons (`rows/ScribeEntrySkeleton/entry.md`, `stage/skeleton/entry.md`), not seat reports. The round-64 taskcall `Report:` destinations inspected point into `w1/` or `w2/`.
- **Protected-state non-touch is not fully confirmable across the fleet.** The lane has no `.ufo/state` or `.ufo/watchdog.log` path. However, fleet-root `.ufo/state` records and `.ufo/watchdog.log` are modified (and the root status includes an untracked Kotodama baseline). Watchdog records identify `hyaku-inline` launch/completion events, and Kotodama's baseline mtime coincides with the round-64 launch. The available read-only evidence supports runner activity, but does not provide process-level attribution proving that seats never wrote those fleet-root paths. Do not claim that global non-touch is confirmed from these checks alone.

**Severity / exploit path / impact / smallest remediation.** No misrooted seat report or seat write to lane-protected paths was evidenced. The remaining provenance gap is informational: an unconstrained seat writing to fleet-global state could contaminate runner bookkeeping, but this sweep cannot attribute the existing global modifications. Smallest next step is to use existing host audit/process-write evidence, if available, before making a stronger claim; no remediation was performed here.

## 1. Fleet-root status and untracked content

Command: `git -C /home/vgpnk/Projects/shokunin status --porcelain`

Output:
```text
 M .ufo/state/chousa.report-baseline
 M .ufo/state/kagi.report-baseline
 M .ufo/state/kaidoku.report-baseline
 M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline
 M .ufo/state/kengaku.report-baseline
 M .ufo/state/kumitate.report-baseline
 M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline
 M .ufo/state/souji.report-baseline
 M .ufo/state/tameshi.report-baseline
 M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
 M SCORECARD.md
?? .omp/mcp.json
?? .ufo/state/kotoba.report-baseline
?? .ufo/state/kotodama.report-baseline
?? .ufo/state/revenger.report-baseline
?? .ufo/waves/hyaku/inline-run-20261023.md
?? 0
?? AGENTS.md
?? bm.json
?? live.html
?? live_s228.html
?? nama.html
?? s395.txt
?? scripts/hyaku/append-closure.py.bak-20261023T040735Z
?? scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z
?? tf_bavelas.html
?? wb2.html
?? write
?? xc.xml
```

I scanned the 18 untracked paths above (excluding any nested `*-shokunin` repository paths) for `(?i)(kotodama|round[- ]?64)`. The only hit was:
```text
.ufo/waves/hyaku/inline-run-20261023.md:39: | kotodama | 64 | 1 | 19:31 |
```

## 2. Lane files modified in the preceding six hours

Command, run from the lane root: `find .ufo/waves/round-64 -type f -mmin -360 -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n' | sort`

Output:
```text
2026-10-23 19:35:07.2583161010 .ufo/waves/round-64/gen-w1.py
2026-10-23 19:35:07.2737126640 .ufo/waves/round-64/w1-spec.json
2026-10-23 19:35:18.4386371090 .ufo/waves/round-64/w1-plan-err.txt
2026-10-23 19:35:18.5680129770 .ufo/waves/round-64/w1-taskcall.json
2026-10-23 19:51:29.7846100550 .ufo/waves/round-64/w1/ScribeRowS721.md
2026-10-23 19:52:22.4208215650 .ufo/waves/round-64/w1/ScribeRejS744.md
2026-10-23 19:52:24.2587968020 .ufo/waves/round-64/w1/ScribeRowS725.md
2026-10-23 19:52:24.4616366140 .ufo/waves/round-64/w1/ScribeRejS747.md
2026-10-23 19:52:27.4616380650 .ufo/waves/round-64/w1/ScribeEntrySkeleton.md
2026-10-23 19:52:31.9016402130 .ufo/waves/round-64/w1/ScribeRowS735.md
2026-10-23 19:52:39.5676439190 .ufo/waves/round-64/w1/ScribeRejS745.md
2026-10-23 19:52:49.4113338190 .ufo/waves/round-64/w1/ScribeRejS749.md
2026-10-23 19:52:50.5906492430 .ufo/waves/round-64/w1/SentinelAccess.md
2026-10-23 19:53:02.3686549230 .ufo/waves/round-64/w1/ScribeRowS736.md
2026-10-23 19:53:15.2041245690 .ufo/waves/round-64/w1/ScribeRejS748.md
2026-10-23 19:53:19.8311156410 .ufo/waves/round-64/w1/ScribeRejS746.md
2026-10-23 19:53:19.8321908520 .ufo/waves/round-64/w1/ScribeRowS734.md
2026-10-23 19:53:25.9966662960 .ufo/waves/round-64/w1/ScribeRowS730.md
2026-10-23 19:53:32.8126695700 .ufo/waves/round-64/w1/ScribeClaimsJson.md
2026-10-23 19:53:33.8506700690 .ufo/waves/round-64/w1/ScribeRowS732.md
2026-10-23 19:53:35.7766709940 .ufo/waves/round-64/w1/ScribeRowS731.md
2026-10-23 19:53:41.9490085410 .ufo/waves/round-64/integrate.py
2026-10-23 19:53:43.7644739040 .ufo/waves/round-64/w1/ScribeRowS733.md
2026-10-23 19:53:51.9365231550 .ufo/waves/round-64/__pycache__/integrate.cpython-314.pyc
2026-10-23 19:53:52.3870995250 .ufo/waves/round-64/w1/ScribeRowS738.md
2026-10-23 19:53:53.9362747680 .ufo/waves/round-64/w1/ScribeRowS726.md
2026-10-23 19:53:57.8316815730 .ufo/waves/round-64/w1/ScribeRowS724.md
2026-10-23 19:54:10.9936878750 .ufo/waves/round-64/w1/ScribeRowS720.md
2026-10-23 19:54:14.8784931250 .ufo/waves/round-64/w1/ScribeRowS729.md
2026-10-23 19:54:20.1166922380 .ufo/waves/round-64/w1/ScribeRowS722.md
2026-10-23 20:01:05.5986437020 .ufo/waves/round-64/stage/rows.txt
2026-10-23 20:01:05.5989277720 .ufo/waves/round-64/stage/bullets.json
2026-10-23 20:01:05.5989721420 .ufo/waves/round-64/stage/report.txt
2026-10-23 20:02:28.3429214900 .ufo/waves/round-64/gen-w2.py
2026-10-23 20:02:28.3567552310 .ufo/waves/round-64/w2-spec.json
2026-10-23 20:02:28.3589214980 .ufo/waves/round-64/w2-plan-err.txt
2026-10-23 20:02:28.3789215070 .ufo/waves/round-64/w2-taskcall.json
2026-10-23 20:02:42.6899281360 .ufo/waves/round-64/w2-plan.json
2026-10-23 20:04:11.0909690130 .ufo/waves/round-64/stage/skeleton/entry.md
2026-10-23 20:04:18.5840055910 .ufo/waves/round-64/w2/B2FixS742.md
2026-10-23 20:04:27.2045802540 .ufo/waves/round-64/w2/B2RejS748.md
2026-10-23 20:04:33.9281509710 .ufo/waves/round-64/w2/B2FixS738.md
2026-10-23 20:04:34.8519991120 .ufo/waves/round-64/w2/B2RejS746.md
2026-10-23 20:04:37.4509811790 .ufo/waves/round-64/w2/B2ReviewRowS718.md
2026-10-23 20:04:39.1729819730 .ufo/waves/round-64/w2/B2ReviewRowS728.md
2026-10-23 20:04:40.7509827010 .ufo/waves/round-64/w2/B2ReviewRowS719.md
2026-10-23 20:04:43.9978159880 .ufo/waves/round-64/integrate-w2.py
2026-10-23 20:04:48.4842375500 .ufo/waves/round-64/w2/B2FixS739.md
2026-10-23 20:04:52.8774292680 .ufo/waves/round-64/w2/B2ReviewRowS732.md
2026-10-23 20:05:11.5929286080 .ufo/waves/round-64/w2/B2ReviewRowS742.md
2026-10-23 20:05:13.0779976060 .ufo/waves/round-64/w2/B2ReviewRowS731.md
2026-10-23 20:05:17.8174963540 .ufo/waves/round-64/w2/B2ReviewRowS720.md
2026-10-23 20:05:18.0143730010 .ufo/waves/round-64/w2/B2ReviewRowS722.md
2026-10-23 20:05:19.0910003770 .ufo/waves/round-64/w2/B2ReviewRowS734.md
2026-10-23 20:05:19.2276132620 .ufo/waves/round-64/check-rows.py
2026-10-23 20:05:26.5080037940 .ufo/waves/round-64/w2/B2ReviewRowS738.md
2026-10-23 20:05:26.5190037990 .ufo/waves/round-64/w2/B2ExecEntry.md
2026-10-23 20:05:30.4850056260 .ufo/waves/round-64/w2/B2ReviewRowS730.md
2026-10-23 20:05:31.7070061890 .ufo/waves/round-64/w2/B2ReviewRowS724.md
2026-10-23 20:05:44.9960123090 .ufo/waves/round-64/w2/B2FixS719.md
2026-10-23 20:05:47.4731864800 .ufo/waves/round-64/w2/B2ReviewRowS736.md
2026-10-23 20:05:58.3139904620 .ufo/waves/round-64/w2/B2ReviewRowS729.md
2026-10-23 20:06:21.9754379430 .ufo/waves/round-64/w2/B2ScribeRowS733.md
2026-10-23 20:06:30.3365771130 .ufo/waves/round-64/w2/B2SentinelAccess.md
2026-10-23 20:06:42.1404576560 .ufo/waves/round-64/w2/B2RevengerFrontier.md
2026-10-23 20:06:45.1893315970 .ufo/waves/round-64/w2/B2ScribeRowS741.md
2026-10-23 20:07:03.7280485260 .ufo/waves/round-64/w2/B2ScribeRowS721.md
2026-10-23 20:07:22.7620572710 .ufo/waves/round-64/w2/B2ScribeRowS743.md
2026-10-23 20:07:30.5580608520 .ufo/waves/round-64/w2/B2ReviewRowS737.md
2026-10-23 20:07:53.4420713600 .ufo/waves/round-64/w2/B2CriticClaims.md
2026-10-23 20:07:54.2640717370 .ufo/waves/round-64/w2/B2ScribeLesson.md
2026-10-23 20:07:54.9610720570 .ufo/waves/round-64/w2/B2ExecCaRepair.md
2026-10-23 20:08:46.0670955050 .ufo/waves/round-64/w2/B2ReviewRowS726.md
2026-10-23 20:09:16.2801311870 .ufo/waves/round-64/w2/B2ScoutRegistry.md
2026-10-23 20:11:42.5816303070 .ufo/waves/round-64/w2/B2ScribeRowS727.md
2026-10-23 20:38:03.5410409720 .ufo/waves/round-64/rows/ScribeRowS718/row.txt
2026-10-23 20:38:03.5417679900 .ufo/waves/round-64/rows/ScribeRowS720/row.txt
2026-10-23 20:38:03.5421317290 .ufo/waves/round-64/rows/ScribeRowS721/row.txt
2026-10-23 20:38:03.5424783780 .ufo/waves/round-64/rows/ScribeRowS722/row.txt
2026-10-23 20:38:03.5428455170 .ufo/waves/round-64/rows/ScribeRowS724/row.txt
2026-10-23 20:38:03.5431762260 .ufo/waves/round-64/rows/ScribeRowS725/row.txt
2026-10-23 20:38:03.5434805750 .ufo/waves/round-64/rows/ScribeRowS726/row.txt
2026-10-23 20:38:03.5441277630 .ufo/waves/round-64/rows/ScribeRowS728/row.txt
2026-10-23 20:38:03.5444405120 .ufo/waves/round-64/rows/ScribeRowS729/row.txt
2026-10-23 20:38:03.5447436220 .ufo/waves/round-64/rows/ScribeRowS730/row.txt
2026-10-23 20:38:03.5450483210 .ufo/waves/round-64/rows/ScribeRowS731/row.txt
2026-10-23 20:38:03.5453326500 .ufo/waves/round-64/rows/ScribeRowS732/row.txt
2026-10-23 20:38:03.5455941990 .ufo/waves/round-64/rows/ScribeRowS733/row.txt
2026-10-23 20:38:03.5459040480 .ufo/waves/round-64/rows/ScribeRowS734/row.txt
2026-10-23 20:38:03.5462039770 .ufo/waves/round-64/rows/ScribeRowS735/row.txt
2026-10-23 20:38:03.5464778770 .ufo/waves/round-64/rows/ScribeRowS736/row.txt
2026-10-23 20:38:03.5467971760 .ufo/waves/round-64/rows/ScribeRowS737/row.txt
2026-10-23 20:38:03.5477102730 .ufo/waves/round-64/rows/ScribeRowS741/row.txt
2026-10-23 20:38:03.5482726810 .ufo/waves/round-64/rows/ScribeRowS719/row.txt
2026-10-23 20:38:03.5482726810 .ufo/waves/round-64/rows/ScribeRowS738/row.txt
2026-10-23 20:38:03.5482726810 .ufo/waves/round-64/rows/ScribeRowS739/row.txt
2026-10-23 20:38:03.5482726810 .ufo/waves/round-64/rows/ScribeRowS742/row.txt
2026-10-23 20:38:03.5494351380 .ufo/waves/round-64/rows/ScribeRejS744/row.txt
2026-10-23 20:38:03.5497372270 .ufo/waves/round-64/rows/ScribeRejS745/row.txt
2026-10-23 20:38:03.5499712760 .ufo/waves/round-64/rows/ScribeRejS746/row.txt
2026-10-23 20:38:03.5502289260 .ufo/waves/round-64/rows/ScribeRejS747/row.txt
2026-10-23 20:38:03.5505011350 .ufo/waves/round-64/rows/ScribeRejS748/row.txt
2026-10-23 20:38:03.5507455440 .ufo/waves/round-64/rows/ScribeRejS749/row.txt
2026-10-23 20:38:03.5512064430 .ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md
2026-10-23 20:38:29.5261166100 .ufo/waves/round-64/rows/ScribeRowS727/row.txt
2026-10-23 20:38:29.5261964700 .ufo/waves/round-64/rows/ScribeRowS743/row.txt
2026-10-23 22:53:43.5906501340 .ufo/waves/round-64/nw1-spec.json
2026-10-23 22:53:43.5923927920 .ufo/waves/round-64/nw1-plan-err.txt
2026-10-23 22:53:43.6143928430 .ufo/waves/round-64/nw1-taskcall.json
```

The `w1/` and `w2/` Markdown seat reports have seat-named basenames (for example `ScribeRowS721.md`, `B2ReviewRowS718.md`). Each `rows/<seat>/...` contribution path names its seat directory. The remaining modified paths are shared wave tooling, task/spec/plan files, staging artifacts, or bytecode—not individual seat reports; they do not name one seat and are not attributed to one.

## 3. Seat report location check

Read-only inventory: `.ufo/waves/round-64/**/*.md` (glob limit 200; 60 Markdown paths returned). The only returned Markdown paths outside `w1/` and `w2/` were:
```text
.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md
.ufo/waves/round-64/stage/skeleton/entry.md
```
Neither is a seat report. The `Report:` trailer scan of `w1-taskcall.json`, `w2-taskcall.json`, and `nw1-taskcall.json` showed destinations under `.ufo/waves/round-64/w1/` or `w2/` (the current `nw1` taskcall destinations are under `w1/`).

## 4. Protected state / watchdog checks

Lane-local read-only check attempted:
```text
find .ufo/state -type f -mmin -360 -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n' | sort
find .ufo/watchdog.log -type f -mmin -360 -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n'
```
Output:
```text
find: ‘.ufo/state’: No such file or directory
find: ‘.ufo/watchdog.log’: No such file or directory
```
The lane `.ufo` inventory contains `waves/` only.

Fleet-root read-only check:
```text
find .ufo/state -type f -mmin -360 -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n' | sort
stat -c '%y %n' .ufo/watchdog.log
```
Output:
```text
2026-10-23 20:33:23.7091168300 .ufo/state/chousa.report-baseline
2026-10-23 20:33:27.4091027580 .ufo/state/kama.report-baseline
2026-10-23 20:33:32.7440825460 .ufo/state/mado.report-baseline
2026-10-23 20:33:34.6210754570 .ufo/state/mori.report-baseline
2026-10-23 20:33:36.3650688800 .ufo/state/tameshi.report-baseline
2026-10-23 20:41:34.8195402140 .ufo/state/tsukuroi.report-baseline
2026-10-23 20:41:36.5675353660 .ufo/state/tabi.report-baseline
2026-10-23 20:41:38.2965305750 .ufo/state/souji.report-baseline
2026-10-23 20:41:43.6445157790 .ufo/state/kagi.report-baseline
2026-10-23 20:41:45.3035111960 .ufo/state/kasegi.report-baseline
2026-10-23 22:40:27.0593129700 .ufo/state/kotodama.report-baseline
2026-10-23 22:40:27.3853156460 .ufo/state/kotoba.report-baseline
2026-10-23 22:40:29.3783320200 .ufo/state/kumitate.report-baseline
2026-10-23 22:40:31.1503466090 .ufo/state/kake.report-baseline
2026-10-23 22:56:25.7419216600 .ufo/state/revenger.report-baseline
2026-10-23 22:56:27.308928112 -0300 .ufo/watchdog.log
```

The fleet-root porcelain output above shows `.ufo/watchdog.log` modified and `.ufo/state/kotodama.report-baseline` untracked. The baseline content read was `64 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Watchdog records read at the end include:
```text
2026-10-23T22:40:27-03:00 launch kotodama round=64 pgid=10242 driver=hyaku-inline attempt=1
2026-10-23T22:45:46-03:00 complete revenger round=62; hyaku-inline attempt=1
2026-10-23T22:56:27-03:00 launch revenger round=63 pgid=106795 driver=hyaku-inline attempt=1
```
These records show fleet runner events, not seat-level file-write provenance. Accordingly, the lane-local paths are absent, and the fleet-global paths are changed; the claim that no seat touched fleet-global state remains unverified.
