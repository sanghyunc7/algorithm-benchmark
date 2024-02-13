from collections import Counter

class Solution:
    def canReorderDoubled(self, arr) -> bool:

            # indices
            # 1, 0
            # 3, 2
            # 5, 4
            # 7, 6


            # 3 6 3 6 3 6   6 12 6 12 6 12

            # x 3   6 12   24
            # 3 6    12 24


        def solve(arr):
                
            d = Counter(arr) # track frequency
            keys = list(d.keys())
            keys.sort()
            
            for k in keys:
                v = d[k]
                if v == 0:
                    continue
                
                if 2 * k not in d:
                    return False
                if d[2 * k] < v:
                    return False
                d[2 * k] -= v
            
            return True
        

        positive = [x for x in arr if x >= 0]
        negative = [-x for x in arr if x < 0]

        print(positive, negative)

        return solve(positive) and solve(negative)
