import copy
import re
import sys
from pathlib import Path

if len(sys.argv) < 3:
    print("command:\npython tree_parser.py input.txt output.txt")
    sys.exit()


file_map = {}
path_list = []
p1 = re.compile(r"\x1B\[[\d;]+m")
p2 = re.compile(r"[└├│]+")
p3 = re.compile(r"── ")
p4 = re.compile("\xa0\xa0 ")
p5 = re.compile("\xa0\xa0     ")

print("Processing...")

with Path.open(sys.argv[1], "r") as fr:
    with Path.open(sys.argv[2], "w") as fw:
        for line in fr:

            if not p3.search(line):
                continue

            line = p1.sub("", line)
            line = p2.sub("", line)
            line = p3.sub("", line)
            depth = len(p4.findall(line))
            depth += len(p5.findall(line))
            line = p4.sub("", line)
            line = p5.sub("", line)

            if depth in file_map:
                path = Path()
                for entry in file_map:
                    path = path / file_map[entry]

                fw.write(repr(str(path)))
                fw.write("\n")
                file_map_t = copy.deepcopy(file_map)

                for entry in file_map_t:
                    if entry > depth:
                        del file_map[entry]

            file_map[depth] = line.strip("\xa0" + " \n")

print("Done.")
