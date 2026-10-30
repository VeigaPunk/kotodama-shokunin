# Probe P3b: after TimeoutExpired, is the grandchild still alive?  Marker in argv identifies survivors.
import subprocess, sys, time, os, signal
MARK = "r79-sentinel-marker-%s" % sys.argv[1]
CHILD = r'''
import os, sys, time
MARK = sys.argv[1]
pid = os.fork()
if pid == 0:
    time.sleep(25)
    os._exit(0)
time.sleep(60)
'''
def alive():
    out = subprocess.run(["ps", "-eo", "pid,args"], capture_output=True, text=True).stdout
    return [l.strip() for l in out.splitlines() if MARK in l and "ps -eo" not in l and "python3 -B -c" in l]
def run_naive():
    t = time.perf_counter()
    try:
        subprocess.run([sys.executable, "-B", "-c", CHILD, MARK], capture_output=True, text=True, timeout=2)
    except subprocess.TimeoutExpired:
        print("naive: TimeoutExpired at %.2fs" % (time.perf_counter() - t))
    time.sleep(0.5)
    print("naive: marker processes alive after return =", len(alive()))
def run_grouped():
    t = time.perf_counter()
    p = subprocess.Popen([sys.executable, "-B", "-c", CHILD, MARK], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, start_new_session=True)
    try:
        p.communicate(timeout=2)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)
        p.communicate(timeout=5)
        print("grouped: returned at %.2fs" % (time.perf_counter() - t))
    time.sleep(0.5)
    print("grouped: marker processes alive after return =", len(alive()))
{"naive": run_naive, "grouped": run_grouped}[sys.argv[2]]()
