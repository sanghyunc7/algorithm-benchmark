from multiprocessing import Process
from memory_profiler import profile
import time
import inspect
import os
import sys


# in your Solution file,
# write:
# from test_harness.harness import harness_run
# and at the bottom:
# if __name__ == "__main__":
#     harness_run(Solution(), [test, test1])

# run:
# mprof run -MC naming_a_company.py
# run:
# mprof plot
# ignore the bottom line in graph (usually blue)
# ignore "child 0" if it exists
# they are bugs or daemons of memory_profiler


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


# def create_testfile():
#     if os.path.exists("tmp.py"):
#         print(True)
#     else:
#         print(False)


# create_testfile()
