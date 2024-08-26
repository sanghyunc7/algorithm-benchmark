from typing import List
from functools import *
from math import *
from collections import *
import heapq
from test_harness.harness import *

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # greedy dp approach going backwards

        health = [[0] * len(dungeon[0]) for _ in range(len(dungeon))]
        health[-1][-1] = max(1, 1 - dungeon[-1][-1])

        for i in range(len(dungeon) -1, -1, -1):
            for j in range(len(dungeon[0]) -1, -1, -1):
                if i == len(dungeon)-1 and j == len(dungeon[0]) - 1:
                    # base case
                    continue
                below = right = float("inf")
                if j < len(dungeon[0]) - 1:
                    right = health[i][j + 1]
                if i < len(dungeon) - 1:
                    below = health[i + 1][j]

                health[i][j] = min(right, below)
                health[i][j] = max(1, health[i][j] - dungeon[i][j])
    
        
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
test = [dungeon]

if __name__ == "__main__":
    test_run(Solution(), [test])
# run:
# mprof run -MC naming_a_company.py

# run:
# mprof plot
