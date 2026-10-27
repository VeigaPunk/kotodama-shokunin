#!/usr/bin/env bash
S=/fast/scratch/hyaku/kotodama-r76/ScribeLesson-7
echo
echo "### \$ era-table region comparison: folded 2600 chars from the first 元号名称 in each carrier"
python3 - "$S" <<'PY'
import re,pathlib,sys
def seg(p):
    t=pathlib.Path(p).read_text(); i=t.find('元号名称')
    return re.sub(r'\s+',' ',t[i:i+2600]).strip()
a,b=seg(sys.argv[1]+'/dec/S908.txt'),seg(sys.argv[1]+'/dec/S935.txt')
print("live-region chars:",len(a),"capture-region chars:",len(b),"character-identical:",a==b)
PY
echo "[exit=$?]"
echo
echo "### \$ registry-route identity: md5 of the three fetches (type=online, type=download, /bzgk/gb/newGbInfo)"
md5sum "$S/fetch2/S938.body" "$S/fetch3/DL.body" "$S/fetch3/GB.body" 2>&1
echo "[exit=$?]"
