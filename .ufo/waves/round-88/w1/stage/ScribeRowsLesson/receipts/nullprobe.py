import json, pathlib, subprocess, sys, os
sys.path.insert(0, '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88')
import importlib.util
spec = importlib.util.spec_from_file_location('m88', '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/measure88.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.ROOT = pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
work = pathlib.Path('/fast/scratch/hyaku/kotodama-r88/ScribeRowsLesson/probe'); work.mkdir(exist_ok=True)
tool = work/'null-findings.py'
tool.write_text('import json,sys\nprint(json.dumps({"records":6,"findings":None}))\nsys.exit(1)\n')
packet = work/'p.json'
cases = json.loads(pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/cases.json').read_text())
packet.write_bytes(json.dumps(m.build(json.loads((work/'base.json').read_text()) if (work/'base.json').exists() else {}).encode()) if False else b'{}')
# build a real mutated packet per case using the frozen packet from the base revision
raw = subprocess.run(['git','-C',str(m.ROOT),'show','4956282281dac1306cfbe59523e46dde99749d75:.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'],capture_output=True).stdout
packet_obj = json.loads(raw)
rows = m.score(tool, packet_obj, cases, work)
print(json.dumps({'tool':'null-findings','passed':sum(r['passed'] for r in rows),'total':len(rows),
                  'first_detail':rows[0]['observed'], 'no_traceback':True}, indent=1))
