import glob


files = glob.glob("slurm-2175*")

for f in files:
    switch=0
    for line in open(f):
        if "Maker is now finished" in line.strip():
            switch=1
            print f, line.strip()
    if not switch:
        print f, "not_done"

