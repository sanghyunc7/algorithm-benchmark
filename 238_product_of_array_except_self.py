from typing import List
from functools import *
from math import *
from test_harness.harness import harness_run

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of left and right side, excluding index i
        # + 2 for default value on both sides of array
        leftProduct = [0] * len(nums)
        rightProduct = [0] * len(nums)
        leftProduct[0] = 1
        rightProduct[-1] = 1



        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = rightProduct[i+1] * nums[i+1]

        result = [0] * len(nums)
        
        for i in range(len(nums)):
            result[i] = leftProduct[i] * rightProduct[i]
        return result
