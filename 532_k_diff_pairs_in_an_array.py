from test_harness.harness import harness_run
from typing import List, Set, Dict, Tuple

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = set()

        d = set()

        for i in nums:
            if i - k in d:
                ans.add((i - k, i))
            if i + k in d:
                ans.add((i, i + k))
            d.add(i)
        return len(ans)

test = [[1, 2, 3, 5, 4], 1]

if __name__ == "__main__":
    harness_run(Solution(), [test])
