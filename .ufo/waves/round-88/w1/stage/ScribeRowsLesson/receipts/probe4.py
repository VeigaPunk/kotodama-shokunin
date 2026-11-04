import json, pathlib, subprocess, importlib.util
spec = importlib.util.spec_from_file_location('m88', '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/measure88.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.ROOT = pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
work = pathlib.Path('/fast/scratch/hyaku/kotodama-r88/ScribeRowsLesson/probe')
raw = subprocess.run(['git','-C',str(m.ROOT),'show','4956282281dac1306cfbe59523e46dde99749d75:.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'],capture_output=True).stdout
packet_obj = json.loads(raw)
cases = json.loads(pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/cases.json').read_text())
probes = {
 # exits 2, emits a WRONG finding id but the literal substring in stderr
 'malformed-wrong-id': 'import json,sys\nprint(json.dumps({"records":0,"findings":[{"id":"WRONG_ID","record":"x"}]}))\nsys.stderr.write("ATTESTATION_ERROR: something\\n")\nsys.exit(2)\n',
 # malformed case passes but wrong id
 'malformed-right-id': 'import json,sys\nprint(json.dumps({"records":0,"findings":[{"id":"ATTESTATION_ERROR","record":""}]}))\nsys.exit(2)\n',
}
for name, body in probes.items():
    t = work/(name+'.py'); t.write_text(body)
    rows = m.score(t, packet_obj, cases, work)
    print(name, 'passed', sum(r['passed'] for r in rows), '/', len(rows),
          'passing cases:', [r['case'] for r in rows if r['passed']])
