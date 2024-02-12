from test_harness.harness import harness_run


class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        # print(target)

        # (sum, index). sum is exclusive to index
        visit = {}

        def backtracking(sm, i):
            if (sm, i) in visit:
                return visit[(sm, i)]
            elif sm == target:
                visit[(sm, i)] = []
                return []
            elif sm > target or i >= len(nums):
                return None

            with_i = backtracking(sm + nums[i], i + 1)
            if with_i is not None:
                visit[(sm, i)] = [i] + with_i
                return visit[(sm, i)]

            without_i = backtracking(sm, i + 1)
            if without_i is not None:
                visit[(sm, i)] = without_i
                return visit[(sm, i)]

            visit[(sm, i)] = None
            return None
        
        # get indices
        st = backtracking(0, 0)
        if st is not None:
            subset1 = set(st)
            subset2 = set([i for i in range(len(nums))]) - subset1
            e1 = [nums[i] for i in subset1]
            e2 = [nums[i] for i in subset2]
            print(e1, e2)

        return st is not None
    
# should be True
test = [[5,79,2,4,8,16,32,64,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]]

# should be True
test1 = [[1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100,99,100]]

# should be True
test2 = [[1,5,11,5]]

# should be False
test3 = [[1,2,3,5]]

if __name__ == "__main__":
    harness_run(Solution(), [test, test1, test2, test3])


