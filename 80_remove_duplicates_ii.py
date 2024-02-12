from test_harness.harness import harness_run
class Solution:
    def removeDuplicates(self, nums):
        k = 1
        prev = [nums[0], 1]
        for i in range(1, len(nums)):
            if nums[i] == prev[0]:
                prev[1] += 1
            else:
                prev = [nums[i], 1]
            if prev[1] <= 2:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return k


nums = [[1, 1, 1, 2, 2, 3]]
nums1 = [[0, 0, 1, 1, 1, 1, 2, 3, 3]]
runner = Solution()

if __name__ == "__main__":
    harness_run(Solution(), [nums, nums1])
