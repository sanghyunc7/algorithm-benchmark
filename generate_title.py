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
    file.write("from collections import defaultdict\n")
    file.write("from test_harness.harness import harness_run\n")
print(f"Created file {filename}")
    
    
    
