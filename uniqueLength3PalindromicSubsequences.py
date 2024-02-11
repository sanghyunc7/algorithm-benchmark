from collections import defaultdict
import string

class Solution:
    def countPalindromicSubsequence(self, s):
        
        
        # alternate soln (preferred?):
        # def countPalindromicSubsequence(self, s):
        #     res = 0
        #     for c in string.ascii_lowercase:
        #         i, j = s.find(c), s.rfind(c)
        #         if i > -1:
        #             res += len(set(s[i + 1: j]))
        #     return res
        
        
        # keep count of unfinished palindromes
        # dict key is chr of unfinished palindrome, value is number of times it appears. for 'aa', 'ab', d['a'] == 2

        incomplete_p = defaultdict(set)
        c_seen = set()

        ans = set()
        for c in s:
            for p in incomplete_p[c]:
                # at most 26 p
                ans.add(p + c)

            # update incomplete_p, c_seen
            # at most 26 iterations
            for prev_c in c_seen:
                incomplete_p[prev_c].add(prev_c + c)
            c_seen.add(c)
        
        print(ans)
        return len(ans)
    
harness = Solution()
test = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(harness.countPalindromicSubsequence(test))


            


            