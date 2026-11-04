import pathlib,sys
sys.stdout.write(pathlib.Path("{\"records\": 6, \"findings\": [{\"id\": \"RECORD_ID\", \"record\": \"R1\"}]}\n").read_text())
sys.exit(1)
