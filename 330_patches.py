from test_harness.harness import harness_run


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # i is the next number we need to make
        # m is the highest number we can make
        i = 1
        m = 0
        j = 0 # index for nums
        patches = 0
        while i <= n:
            while j < len(nums) and nums[j] <= m:
                m += nums[j]
                j += 1
            if j < len(nums) and nums[j] == i:
                m += nums[j]
                j += 1
            elif i <= m:
                pass
            else:
                m += i
                patches += 1
            i += 1

        return patches
        