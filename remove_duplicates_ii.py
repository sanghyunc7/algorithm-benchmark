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
            print(i, nums[i], prev, k, nums[k])
            if prev[1] <= 2:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
            print(nums)
        return k


nums = [1, 1, 1, 2, 2, 3]
nums1 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
runner = Solution()
k = runner.removeDuplicates(nums)
print(nums[:k])

k = runner.removeDuplicates(nums1)
print(nums1[:k])


if __name__ == "__main__":
    harness_run(Solution(), [nums, nums1])
