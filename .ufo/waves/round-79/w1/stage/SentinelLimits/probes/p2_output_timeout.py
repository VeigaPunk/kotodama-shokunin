# Probe P2: output cap, UTF-8 decode, catastrophic -P pattern, pipe-held timeout.
# Mirrors round-76 run_observe: subprocess.run(argv, cwd=..., capture_output=True, text=True, timeout=...)
import subprocess, time, resource, os, sys
FX = "/fast/scratch/hyaku/kotodama-r79/SentinelLimits/fx"
REV = "ad6b92b"
ENV = {"PATH": os.environ["PATH"], "HOME": "/fast/scratch/hyaku/kotodama-r79/SentinelLimits",
       "GIT_CONFIG_NOSYSTEM": "1", "GIT_TERMINAL_PROMPT": "0", "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8"}
def run(label, argv, timeout=60, text=True):
    t = time.perf_counter()
    try:
        p = subprocess.run(argv, cwd=FX, capture_output=True, text=text, timeout=timeout, env=ENV)
        n = len(p.stdout)
        print("%-34s rc=%s stdout_bytes=%d time=%.2fs" % (label, p.returncode, n, time.perf_counter() - t))
    except BaseException as e:
        print("%-34s EXC %s: %s time=%.2fs" % (label, type(e).__name__, str(e)[:90], time.perf_counter() - t))
    print("   maxrss(children,KiB)=%d" % resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
run("big-40MiB git grep -E", ["git", "grep", "-n", "-E", ".", REV, "--", "big.txt"])
run("bad-utf8 git grep (text=True)", ["git", "grep", "-n", "-E", ".", REV, "--", "bad.txt"])
run("bad-utf8 git grep (bytes)", ["git", "grep", "-n", "-E", ".", REV, "--", "bad.txt"], text=False)
run("redos -P git grep -c", ["git", "grep", "-c", "-P", "^(a+)+$", REV, "--", "redos.txt"], timeout=20)
