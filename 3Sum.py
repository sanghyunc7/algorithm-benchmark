class Solution:
    def threeSum(self, nums):
        
        nums.sort()
        
        ans = []
        
        for i,v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            
            want = -v
            left = i + 1
            right = len(nums) - 1
            
            while (left < right):
                if nums[left] + nums[right] == want:
                    ans.append([i, left, right])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > want:
                    right -= 1
                else:
                    left += 1
        
        return ans
        
        
        
        # for num in nums:
        #     retval = twoSum(self, exclude, nums)
        #     if !retval:
        
        
soln = Solution()

soln.threeSum([-1,0,1,2,-1,-4])