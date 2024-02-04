from multiprocessing import Process
import os
import time


def output(n):
    time.sleep(1)
    print("output", os.getpid())
    print(n)


# notice main.pid + 1 doesn't get printed

if __name__ == "__main__":
    print("main", os.getpid())
    processes = []
    for i in range(5):
        processes.append(Process(target=output, args=[i]))

    for i in range(len(processes)):
        processes[i].start()
    for i in range(len(processes)):
        processes[i].join()
    print("finished")
