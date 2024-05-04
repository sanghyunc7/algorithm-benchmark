from typing import List
from functools import *
from math import *
from test_harness.harness import harness_run


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = first
        for n in nums:
            if n <= first:
                # print(first, n)
                first = n
            elif n <= second:
                # print(second, n)
                second = n
            else:
                return True
        return False


        