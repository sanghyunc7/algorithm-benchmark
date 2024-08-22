from typing import List
from functools import *
from math import *
from collections import *
from test_harness.harness import *





class Solution:
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        ps = {}
        res = []
        for i, word in enumerate(words):
            ps[word[::-1]] = i 
        #print(ps)
        for i, word in enumerate(words):
            if word in ps and ps[word] != i:
                res.append([i, ps[word]])
            if "" in ps and ps[""] != i and word == word[::-1]:
                res.append([i, ps[""]])
                res.append([ps[""], i])

            for j in range(len(word)):
                # partial palindrome is in the list and rest of the word is palindrome
                # going from front, partial palindrome is in front
                # going from back, partial aplindrome is at the back
                if word[j:] in ps and word[:j] == word[j-1::-1]:
                    res.append([ps[word[j:]], i])
                if word[:j] in ps and word[j:] == word[:j-1:-1]:
                    res.append([i, ps[word[:j]]])

        return res
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # keep a map of hash(word):index
        # use rolling hashes approach to find strings that make words[i] a palindrome
        # if such a string is found in our map, add the pair to ans

        # returns all hashes of strings added to w to make the concatenation a palindrome
        def need_string(w):
            base = 26
            mod = 10 ** 9 + 7
            reversed_w = w[::-1]
            power = [1]

            # build reversed_w hash
            # should use same scheme as the one that the word_map uses
            hashrw = [0]
            for i in range(len(reversed_w)):
                c = ord(w[i]) - ord('a')
                hashrw.append((hashrw[-1] * base + c) % mod)
            
            for i in range(1, len(w)):
                power.append((power[-1] * base) % mod)



            place = 1
            left = [hashrw[-1]]
            hash1 = 0 # new chr in smallest position
            hash2 = 0 # new chr in largest position
            for i in range(len(w)):
                c = ord(w[i]) - ord('a')
                hash1 = (hash1 * base + c) % mod
                hash2 = (c * place + hash2) % mod
                if hash1 == hash2:
                    # reversed_w[:len(w) -1 -i]
                    left.append(hashrw[len(w) -1 -i])
                place = (place * base) % mod
            
            right = [hashrw[-1]]
            hash1 = 0
            hash2 = 0
            place = 1
            for i in range(len(w) -1, -1, -1):
                c = ord(w[i]) - ord('a')
                hash1 = (hash1 * base + c) % mod
                hash2 = (c * place + hash2) % mod
                if hash1 == hash2:
                    # reversed_w[len(w) - i:]
                    right.append((hashrw[-1] - hashrw[len(w) - i]) % mod)
                place = (place * base) % mod
            
            return left, right


        ans = set()
        d = {} # key is hash(word), value is index
        for i,w in enumerate(words):
            d[w] = i

        for i, w in enumerate(words):
            # if only considering left side, need_string can't generate
            # baca for w := b
            # need to consider both sides of acab:
            # acab --> add left [b, bac, baca]
            # acab --> add right [b, baca]

            # however, when strings are of equal length
            # w1 := abc, w2 := cba
            # results in duplicate production of abc + cba
            # use set for ans
            left, right = need_string(w)
            # u need 
            # print(w)
            # print(left)
            # print(right)
            
            for s in left:
                if s != w and s in d:
                    ans.add((d[s], i))
            
            for s in right:
                if s != w and s in d:
                    ans.add((i, d[s]))
                    
        return ans

            


test = [["abcd","dcba","lls","s","sssll"]]
# Output: [[0,1],[1,0],[3,2],[2,4]]

test1 = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]

test2 = [["a",""]]
# Output: [[0,1],[1,0]]




if __name__ == "__main__":
    test_run(Solution(), [test, test1, test2])
# run:
# mprof run -MC naming_a_company.py

# run:
# mprof plot
