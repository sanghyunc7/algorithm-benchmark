from typing import List
from functools import lru_cache
from test_harness.harness import harness_run


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # greedy soln: we could do an n-logn approach by sorting first
        # try to fit heaviest and smallest person in the same boat
        # if they don't fit, increment the pointer heaviest person to
        # 2nd heaviest person, increase boat_count by 1

        people.sort()
        i = 0
        j = len(people) - 1
        ans = 0
        while i < j:
            sm = people[i] + people[j]
            if sm <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            ans += 1
        if i == j:
            ans += 1
        return ans

