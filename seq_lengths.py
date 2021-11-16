import sys

with open(sys.argv[1], "r") as fh:
    line = line.strip()
    lines = fh.readlines()

for line in lines:
    print(len(line))

