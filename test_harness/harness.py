from multiprocessing import Process
from memory_profiler import profile
import time
import inspect
import os
import sys


# dependencies installation:
# pip install memory-profiler
# pip install matplotlib

# in your Solution file, e.g. naming_a_company.py
# write:
# from test_harness.harness import harness_run
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
    print(os.getpid(), method.__name__)
    # so that all lines appear first
    # time.sleep(1)
    start = time.time()
    out = []
    for t in tests:
        out.append(method(t))
    end = time.time()
    print(f"{method.__name__} actual execution time: {end - start} seconds")
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

