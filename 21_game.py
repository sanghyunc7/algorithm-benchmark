from functools import lru_cache
from itertools import permutations


def solution(arr):
    # arr has 4 numbers
    # use any operations to create the number 21

    # consider only arr[i, j] inclusive to create target
    operations = ['+', '-', '/', '*', '**']
    # ops = [lambda x, y: x - y]

    visit = set()

    def dfs(i, j, target):
        if (i, j, target) in visit:
            return visit[(i, j, target)]
        
        if i == j and abs(target - arr[i]) < 0.000001: # ==?
            return True
        if i == j and abs(target - arr[i]) >= 0.000001:
            return False

        for x in range(i + 1, j + 1):
            for y in range(x, j + 1):
                # x, y are new boundaries
                # perform operation on arr[i]
                for op in operations:
                    if op == '+':
                        # target = arr[i] + dfs()
                        next_target = target - arr[i]
                        if dfs(x, y, next_target):
                            
                            return True
                    elif op == '-':
                        # target = arr[i] - dfs()
                        next_target = arr[i] - target
                    elif op == '/':
                        # target = arr[i] / dfs
                        next_target = arr[i] / target



        
    

    

    return dfs(0, 3)