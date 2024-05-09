from collections import Counter, defaultdict
from test_harness.harness import harness_run
from typing import List, Set, Dict, Tuple



class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employees = defaultdict(list)
        for i, v in enumerate(manager):
            employees[v].append(i)
        
        mx = 0
        def dfs(root, path):
            nonlocal mx
            mx = max(mx, path + informTime[root])
            for n in employees[root]:
                dfs(n, path + informTime[root])
        
        dfs(headID, 0)
        return mx


input1 = [1, 0, [-1], [0]] #output: 0
input2 = [6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]] # output 1

if __name__ == "__main__":
    harness_run(Solution(), [input1, input2])
        



        