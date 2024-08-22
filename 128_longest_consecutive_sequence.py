from typing import List
from functools import *
from math import *
from collections import defaultdict

def longestConsecutive(nums: List[int]) -> int:
    numbers = set(nums)

    @lru_cache(None)
    def dfs(i):
        if i + 1 in numbers:
            return 1 + dfs(i + 1)
        return 1


    longest = 0
    for i in nums:
        longest = max(longest, dfs(i))
    return longest

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))       



