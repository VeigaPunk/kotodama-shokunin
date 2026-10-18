#!/usr/bin/env python3
"""round-19 acceptance — re-runs the three claims' measurements and refreshes validation.json."""
import json, subprocess, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
result = subprocess.run([sys.executable, "-c", """
import json, subprocess, pathlib
# compact re-measure: entries, battery exit, four selftest/gate runs, SKILL subsections
fails = []
def run(c): return subprocess.run(['bash','-c'], input=c.encode(), capture_output=True, timeout=300)
files = subprocess.run(['bash','-c',"git status --short | grep '^?? corpus/knowledge' | awk '{print $2}'"],capture_output=True).stdout.decode().split()
ver=[f for f in files if '/verification/' in f]; syn=[f for f in files if '/synthesis/' in f]
if not(len(files)>=8 and len(ver)>=3 and len(syn)>=3): fails.append('C entries')
b=subprocess.run(['bash','-c','export TMPDIR=$PWD/.scratch; python3 tools/check-gate-battery.py'],capture_output=True).stdout.decode()
if '\"battery_exit\": 0' not in b: fails.append('battery')
for c in ['python3 tools/check-gate-battery.py --selftest','python3 tools/assemble-d4-typed.py --selftest','python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml','python3 tools/gates/typed-pipeline-gate.py']:
    if subprocess.run(['bash','-c',c],capture_output=True).returncode!=0: fails.append(c[:40])
skill=pathlib.Path('SKILL.md').read_text()
if 'Slot-label routing' not in skill: fails.append('D skill')
v=json.load(open('reports/round-19/validation.json')); v['acceptance_checks_passed']=not fails; v['failures']=fails
v['rerun_at_close']='python3 reports/round-19/run-validation.py'
pathlib.Path('reports/round-19/validation.json').write_text(json.dumps(v,indent=1,ensure_ascii=False))
print('acceptance:', not fails, fails)
"""], capture_output=True, text=True)
print(result.stdout.strip() or result.stderr[-300:])
