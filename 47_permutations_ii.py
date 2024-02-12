from collections import Counter
from test_harness.harness import harness_run

class Solution:
    def permuteUnique(self, nums):
        ans = set()
        have = set()  # store indices
        tmp = []

        def helper(have, tmp):
            # print(tmp)
            if len(tmp) == len(nums):
                ans.add(tuple(tmp))
                return
            for i in range(len(nums)):
                if i not in have:
                    have.add(i)
                    tmp.append(nums[i])
                    helper(have, tmp)
                    tmp.pop()
                    have.remove(i)

        helper(have, tmp)
        return list(ans)

    def permuteUnique2(self, nums):
        count = Counter(nums)
        ans = []
        tmp = []

        def helper(tmp):
            if len(tmp) == len(nums):
                ans.append(tuple(tmp))
                return

            for k in count:
                if count[k]:
                    count[k] -= 1
                    tmp.append(k)
                    helper(tmp)
                    tmp.pop()
                    count[k] += 1

        helper(tmp)
        return ans


test1 = [[1, 2, 3, 4, 5, 6, 7, 8]]
test2 = [[1, 1, 1, 1, 1, 1, 1, 1]]

if __name__ == "__main__":
    harness_run(Solution(), [test1, test2])