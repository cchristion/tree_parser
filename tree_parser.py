import copy
import re
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("command:\npython tree_parser.py input.txt > output.txt")
    sys.exit()


file_map = {}
path_list = []

p1 = re.compile(r"\x1B\[[\d;]+m")
p2 = re.compile(r"^.*── ")
p3 = re.compile("\xa0\xa0 ")
p4 = re.compile(r"\s{4}")

with Path.open(sys.argv[1], "r") as fr:
    for line in fr:

        line_s = p2.search(line)
        if not line_s:
            continue

        line = p1.sub("", line)
        line = p2.sub("", line)
        depth = len(p3.findall(line_s.group(0)))
        depth += len(p4.findall(line_s.group(0)))

        if depth in file_map:
            path = Path()
            for entry in file_map:
                path = path / file_map[entry]

            print(repr(str(path)))
            file_map_t = copy.deepcopy(file_map)

            for entry in file_map_t:
                if entry > depth:
                    del file_map[entry]

        file_map[depth] = line.strip("\xa0" + " \n")
