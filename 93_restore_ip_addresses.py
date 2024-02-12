class Solution:
    def restoreIpAddresses(self, s):
        # dynamic programming approach
        # how many combinations can be made
        # 2d dynamic programming?
        # ans[i][j]. ans[i] is where first dot goes
        ans = [[0] * (len(s) + 1) for _ in range(5)]

        # initialize
        ans[0][0] = 1

        # s[start:end]
        def validate(start, end):
            if end > len(s):
                return False

            n = s[start:end]
            if len(n) > 1 and n[0] == "0":
                return False
            if 0 <= int(n) <= 255:
                return True
            return False

        # create parent-child linkage
        # parent is start, child is end
        # where s[start:end]
        parents = [[[] for _ in range(len(s) + 1)] for _ in range(5)]

        for i in range(1, len(ans)):
            for j in range(len(ans[0])):
                if ans[i - 1][j] > 0:
                    end = j + 1
                    while validate(j, end):
                        ans[i][end] += ans[i - 1][j]
                        parents[i][end].append((i - 1, j))
                        end += 1

        ret = []

        # create permutations
        def construct(level, tmp, end):
            if level == 0:
                ip_addr = reversed(tmp[:-1])
                ret.append("".join(ip_addr))
                return

            for nxtlvl, start in parents[level][end]:
                n = s[start:end]
                tmp.extend([n, "."])
                construct(nxtlvl, tmp, start)
                tmp.pop()
                tmp.pop()

        construct(4, [], len(s))

        print()
        print(ans[-1][-1])
        ret.sort()
        print(ret)
        return ret


harness = Solution()
test = "1111111"
ans = [
    "1.1.11.111",
    "1.1.111.11",
    "1.11.1.111",
    "1.11.11.11",
    "1.11.111.1",
    "1.111.1.11",
    "1.111.11.1",
    "11.1.1.111",
    "11.1.11.11",
    "11.1.111.1",
    "11.11.1.11",
    "11.11.11.1",
    "11.111.1.1",
    "111.1.1.11",
    "111.1.11.1",
    "111.11.1.1",
]
assert harness.restoreIpAddresses(test) == ans

test1 = "172162541"
ans1 = [
    "17.216.25.41",
    "17.216.254.1",
    "172.16.25.41",
    "172.16.254.1",
    "172.162.5.41",
    "172.162.54.1",
]
assert harness.restoreIpAddresses(test1) == ans1
