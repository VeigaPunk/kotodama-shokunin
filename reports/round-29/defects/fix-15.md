# R29-O15 — register-law reader blindness for tokenless speaker classes

- Date: 2026-10-18.
- Status: **open; route to R30.** The current gate selftest is green but its tested speaker shape misses the reported defect.

## Independent reproduction

At **2026-10-18 17:59:23−03:00**, with `TMPDIR=$PWD/.scratch`, `python3 tools/gates/register-law-gate.py --selftest` exited 0 with **33/33** controls. The subsequent clean-packet command, `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml`, exited 1 with four `D4L-LAW-DANGLING` HOLD findings; those are the current clean-packet reading, not a tamper result.

At **2026-10-18 17:59:46−03:00**, I ran a paired, read-only comparison: a Python command copied the D4 packet to a temporary file under `$TMPDIR`, changed one `speaker:` value to `"no-such-speaker"` without an ID token, ran the same gate on the clean and modified packets, and compared only emitted `FINDING D4L-LAW-*` lines. The command reported one speaker row changed, four findings in each run, and `finding_lines_identical True`. Thus the tokenless class tamper is still invisible. The temporary file was removed by the command.

This reproduces the gap independently of the historical R28 review (`reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md` §3), which identified that the gate resolves `Name (ID)` tokens, not free speaker classes. The gate's **33/33** selftest does not discharge this control because its existing speaker tests retain an ID token.

## Route

Do not claim the speaker-class clause is fully closed. R30 needs either a declared closed speaker-class vocabulary plus a tokenless negative control in both gate and runner, or a narrower claim explicitly limited to ID tokens. Also register the law-gate clean and tamper legs in the regression inventory; otherwise a future gate exit change can be invisible. No code, claim, or old report was changed here.