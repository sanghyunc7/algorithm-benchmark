from typing import List
from functools import *
from math import *
from collections import defaultdict, deque
from test_harness.harness import harness_run


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # https://medium.com/@anirudhm187/edit-distance-d314bc204350
        # word1 (i) on vertical axis
        # word2 (j) on horizontal axis
        # going up a cell (i - 1) means deletion of char i from word1, so retrieve dp[i - 1][j] to get state after deletion. (add 1 to cost to get pre-deletion val)
        # going right a cell (j - 1) -> j means inclusion of char j from word2. so retrieve dp[i][j - 1] to get pre-inclusion state (add 1 to cost to get post-inclusion val)

        ans = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        parent = {}

        for i in range(len(ans)):
            for j in range(len(ans[0])):
                if i == 0:
                    ans[i][j] = j
                elif j == 0:
                    ans[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1]
                    parent[(i, j)] = (i - 1, j - 1, "match")
                else:
                    pre_inclusion = ans[i][j - 1]
                    post_deletion = ans[i - 1][j]
                    replace = ans[i - 1][j - 1]
                    mn = min(pre_inclusion, post_deletion, replace)
                    if mn == pre_inclusion:
                        parent[(i, j)] = (i, j - 1, "pre_inclusion")
                    elif mn == post_deletion:
                        parent[(i, j)] = (i - 1, j, "post_deletion")
                    else:
                        parent[(i, j)] = (i - 1, j - 1, "replace")
                    ans[i][j] = mn + 1

        key = (len(word1), len(word2))

        steps = []
        while parent.get(key):
            steps.append(parent[key])
            key = parent[key][:2]
        steps = steps[::-1]
        print(steps)


        return ans[-1][-1]




    def minDistance1(self, word1: str, word2: str) -> int:
        # do a bfs
        d = defaultdict(int)

        chars = set([c for c in word2])
        q = deque([(word1, 0)])
        while q:
            w, steps = q.popleft()
            print(w)
            if w == word2:
                return steps
            if w in d:
                continue
            d[w] = steps
            
            warray = [c for c in w]
            for i in range(len(warray)):
                for c in chars:
                    # replace
                    warray[i] = c
                    q.append(("".join(warray), steps + 1))

            for i in range(len(w)):
                # delete
                q.append((w[:i] + w[i + 1:], steps + 1))
            
            for i in range(len(w)):
                for c in chars:
                    q.append((w[:i] + c + w[i + 1:], steps + 1))
        
        return -1

            

input1 = ["horse", "ros"]
input2 = ["intention", "execution"]

if __name__ == "__main__":
    harness_run(Solution(), [input1, input2])
        