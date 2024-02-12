from test_harness.harness import harness_run

from collections import defaultdict


class Solution:

    def makesquare(self, matchsticks):
        sum_matchsticks = sum(matchsticks)
        if sum_matchsticks % 4 != 0:
            return False

        side = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        buckets = [0] * 4

        # backtrack
        def bt(i):
            if sum(buckets) == sum_matchsticks:
                return True
            # elif i > len(matchsticks):
            for j in range(len(buckets)):
                if buckets[j] + matchsticks[i] <= side:
                    buckets[j] += matchsticks[i]
                    if bt(i + 1):
                        return True
                    buckets[j] -= matchsticks[i]
            return False

        return bt(0)

    def makesquare1(self, matchsticks):
        if sum(matchsticks) % 4 != 0:
            return False
        side = sum(matchsticks) // 4
        print(sum(matchsticks), side)
        # have 4 buckets, each representing 1 side of square
        # sum of bucket contents add up to square length
        d = defaultdict(int)

        ans = False
        bucket = 0

        def dfs(i, have):
            nonlocal bucket
            nonlocal ans
            if d[bucket] == side:
                bucket += 1
                if bucket == 4:
                    ans = True
                    return
            elif d[bucket] > side:
                return
            for j in range(len(matchsticks)):
                if j not in have:
                    have.add(j)
                    d[bucket] += matchsticks[j]
                    dfs(j, have)
                    if d[bucket] == 0:
                        bucket -= 1
                    d[bucket] -= matchsticks[j]
                    have.remove(j)

        have = set()
        have.add(0)
        d[bucket] = matchsticks[0]
        dfs(0, have)
        return ans


# harness = Solution()
test = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
# print(harness.makesquare1(test))

if __name__ == "__main__":
    harness_run(Solution(), [test])
