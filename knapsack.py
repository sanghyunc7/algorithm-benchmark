# from test_harness.harness import harness_run


# 0/1 bounded knapsack. You can take one of each item.
class Solution:
    def knapsack(self, limit, weights, values):
        # within the weight limit, maximize total value
        # assumption: len(weights) == len(values)
        
        # dp[i][j] := maximum total value for weight i using up to element j
        # note: weight i doesn't mean your knapsack actually weighs i
        # just that it contains the largest total value for a knapsack of size i
        dp = [[0] * (len(weights)) for _ in range(limit + 1)]
        

        for i in range(1, limit + 1):
            for j in range(len(weights)):
                if j == 0 and i - weights[j] >= 0:
                    dp[i][j] = values[j]
                    continue
                # don't include element j or include and use dp sub-result
                if j - 1 >= 0: # otherwise has value 0
                    dp[i][j] = dp[i][j - 1]
                if i - weights[j] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - weights[j]][j - 1] + values[j])
        
        return dp[-1][-1]

s = Solution()
profit = [60, 100, 120]
weights = [10, 20, 30]
print(s.knapsack(51, weights, profit))

            