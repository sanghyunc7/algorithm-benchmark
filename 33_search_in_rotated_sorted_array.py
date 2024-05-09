from collections import Counter
from test_harness.harness import harness_run
from typing import List, Set, Dict, Tuple



# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


# 0 1 2 3 4 5 -1 -2


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] < target or (nums[m] > target and nums[i] > target):
                i = m + 1 
            else:
                j = m
        
        if nums[j] == target:
            return j
        return -1


nums = [[4,5,6,7,0,1,2], 0]
nums1 =  [[4,5,6,7,0,1,2], 3]
nums2 = [[1], 0]

if __name__ == "__main__":
    harness_run(Solution(), [nums, nums1, nums2])
        



        