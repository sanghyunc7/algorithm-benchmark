from collections import deque
from test_harness.harness import harness_run

class Solution:
    def decodeString(self, s: str) -> str:
        # the reason why this doesnt work is
        # it tries to add numbers and letters to the stack separately
        # this creates too many edge cases
        # it is better to do it systematically -> always add number and letter as a group, including 0s and empty strings
        
        n = 0
        word = ""
        ans = []
        stack = deque()
        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == "[":
                stack.append(n)
                n = 0
            elif c == "]":
                m = stack.pop() # multiplier
                print(word, m)
                word = word * m
                if stack: # a2[c] -> a + cc -> acc
                    word = stack.pop() + word
            else:
                stack.append(min(1, n))
                word += c
                n = 0
        print(word)
        return word
    
    def decodeString1(s):
        stack = deque()
        n = 0
        string  = ""
        for c in s:
            if c == '[':
                stack.append(string)
                stack.append(n)
                n = 0
                string = ""
            elif c == ']':
                n = stack.pop()
                prev = stack.pop()
                string = prev + n * string
                n = 0
            elif c.isdigit():
                n = 10 * n + int(c)
            else:
                string += c
        return string
                 

           

test = "3[a]2[bc]"
test1 = "3[a2[c]]"
test2 = "2[abc]3[cd]ef"
test3 = "2[2[a4[vb]]]"
              
harness = Solution()
harness.decodeString(test3)

