S = '/fast/scratch/hyaku/kotodama-r94/MutationTester94'
for src, dst in [(f'{S}/exp/v5-pin.py', f'{S}/exp/head-qualify-on-pin.py')]:
    t = open(src, encoding='utf-8').read()
    old = "            return len(h.lstrip('#').split()) >= 2"
    assert t.count(old) == 1
    open(dst, 'w', encoding='utf-8').write(t.replace(old, "            return True"))
print('ok')
