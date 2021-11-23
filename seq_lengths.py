import sys

with open(sys.argv[1], "r") as fh:
    lines = fh.readlines()

for line in lines:
    # remove newlines
    line = line.strip()
    # Header line starts with ">"
    if line.startswith(">"):
        header = line
        #tu puta madr
    else:
        length = len(line)
        print(length, header)


