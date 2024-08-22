from typing import List
from functools import *
from math import *
from collections import *
from test_harness.harness import *


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
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
