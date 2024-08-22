#!/usr/bin/python3
import string
import sys
import os

# ./generate_title.py 25. Reverse Nodes in k-Group

args = []
for i, thing in enumerate(sys.argv):
    if i < 1:
        continue
    args.append(thing.lstrip(string.punctuation).rstrip(string.punctuation).lower())
filename = "_".join(args) + ".py"

if os.path.exists(filename):
    print(f"The file '{filename}' already exists.")

with open(filename, 'w') as file:
    file.write("from typing import List\n")
    file.write("from functools import *\n")
    file.write("from math import *\n")
    file.write("from collections import *\n")
    file.write("import heapq")
    file.write("from test_harness.harness import *\n\n\n")

    file.write('# if __name__ == "__main__":\n')
    file.write("#     test_run(Solution(), [test, test1])\n")

    file.write("# run:\n")
    file.write("# mprof run -MC naming_a_company.py\n\n")
    file.write("# run:\n")
    file.write("# mprof plot\n")
print(f"Created file {filename}")
    
    
    
