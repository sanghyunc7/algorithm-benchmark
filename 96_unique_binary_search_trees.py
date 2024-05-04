from typing import List
from test_harness.harness import harness_run
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        ans = 0
        for i in range(n):
            # nth node as root node
            left = i
            right = n - i - 1
            # 0 1 2 3
            left_ans = self.numTrees(left)
            right_ans = self.numTrees(right)
            ans += left_ans * right_ans
        return ans
