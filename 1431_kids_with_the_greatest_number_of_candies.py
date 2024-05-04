from typing import List
from functools import *
from math import *
from test_harness.harness import harness_run

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        ans = []
        for c in candies:
            if c + extraCandies >= mx:
                ans.append(True)
                # mx = c + extraCandies
            else:
                ans.append(False)
        return ans
        