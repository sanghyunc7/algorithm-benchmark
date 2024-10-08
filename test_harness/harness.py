from multiprocessing import Process
from memory_profiler import profile
from typing import *
from functools import *
from math import *
from collections import *
import time
import inspect
import os
import sys


# dependencies installation:
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

# in your Solution file, e.g. naming_a_company.py

# 1. create tests. Each test should be a List of arguments as described by the Solution method definition. order of args matters.
# 2. write:
# from test_harness.harness import *
# if __name__ == "__main__":
#     harness_run(Solution(), [test, test1])


# run:
# mprof run -MC naming_a_company.py
# run:
# mprof plot

# notes:
# if a solution runs too fast (<0.1 sec), then memory-profiler misses it
# for macOS, ignore its daemons which shows up on the graph usually as child 0



@profile
def test_method(method, tests):
    print(os.getpid(), "using method", method.__name__)

    start = time.time()
    out = []
    for t in tests:
        rtn = method(*t)
        if rtn is None:
            # the question must've asked for modifications to original input
            rtn = t
        flush = f"{os.getpid()} test output:\n{rtn}\n"
        print(flush)
        out.append(rtn)
        
    end = time.time()
    print(f"{method.__name__} total execution time: {end - start} seconds")
    
    return out, end - start


def test_method_no_profiling(method, tests):
    start = time.time()
    out = []
    for t in tests:
        rtn = method(*t)
        if rtn is None:
            # the question must've asked for modifications to original input
            rtn = t
        flush = f"test output:\n{rtn}\n"
        print(flush)
        out.append(rtn)
        
    end = time.time()
    print(f"{method.__name__} total execution time: {end - start} seconds")
    
    return out, end - start

def harness_run(soln, tests):
    print(os.getpid(), "harness_run")

    attrs = (getattr(soln, name) for name in dir(soln))
    methods = filter(inspect.ismethod, attrs)
    processes = []
    for method in methods:
        processes.append(Process(target=test_method, args=(method, tests)))

    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("Finished.")

def test_run(soln, tests, method=0):

    attrs = (getattr(soln, name) for name in dir(soln))
    methods = list(filter(inspect.ismethod, attrs))
    for i in range(len(methods)):
        if method == i:
            print(f"test run using method {methods[i].__name__}")
            test_method_no_profiling(methods[i], tests)
            break

