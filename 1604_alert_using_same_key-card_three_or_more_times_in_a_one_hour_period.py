from typing import List
from functools import *
from math import *
from collections import *
from test_harness.harness import *

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        mapper = defaultdict(set)


        def convert(t):
            h = t.split(":")[0]
            m = t.split(":")[1]
            return 60 * int(h) + int(m)


        alerted = set()
        for name, time in zip(keyName, keyTime):
            if name in alerted:
                continue
            t = convert(time)
            near_t = 0
            for i in range(max(0, t - 60), min(23 * 60 + 59, t + 60) + 1):
                if i in mapper[name]:
                    near_t += 1
            if near_t >= 2:
                alerted.add(name)
            mapper[name].add(t)            

            
        ans = sorted([name for name in alerted])
        return ans


test1 = [["a","a","a","a","a","b","b","b","b","b","b"], ["04:48","23:53","06:36","07:45","12:16","00:52","10:59","17:16","00:36","01:26","22:42"]]
test2 = [["leslie","leslie","leslie","clare","clare","clare","clare"], ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]]
test3 = [["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]]
test4 = [["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]]

        

if __name__ == "__main__":
    test_run(Solution(), [test1, test2, test3, test4])
    harness_run(Solution(), [test1, test2, test3, test4])
# run:
# mprof run -MC naming_a_company.py

# run:
# mprof plot
