# Probe P3: does subprocess.run(timeout=) return on time when a grandchild inherits the stdout pipe?
# Harness-level only: the child is a python -c that forks a grandchild holding stdout+stderr for 25 s.
import subprocess, sys, time, os, signal
CHILD = r'''
import os, sys, time
pid = os.fork()
if pid == 0:
    time.sleep(25)      # grandchild keeps inherited stdout/stderr open
    os._exit(0)
time.sleep(60)          # direct child stalls past the timeout
'''
def naive():
    t = time.perf_counter()
    try:
        subprocess.run([sys.executable, "-B", "-c", CHILD], capture_output=True, text=True, timeout=2)
        print("naive: returned without timeout")
    except subprocess.TimeoutExpired as e:
        print("naive: TimeoutExpired after %.2fs (returned only after grandchild released pipe)" % (time.perf_counter() - t))
def grouped():
    t = time.perf_counter()
    p = subprocess.Popen([sys.executable, "-B", "-c", CHILD], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, start_new_session=True)
    try:
        p.communicate(timeout=2)
        print("grouped: returned without timeout")
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)
        try:
            p.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            print("grouped: second communicate still blocked")
        print("grouped: killed process group after %.2fs" % (time.perf_counter() - t))
mode = sys.argv[1]
{"naive": naive, "grouped": grouped}[mode]()
