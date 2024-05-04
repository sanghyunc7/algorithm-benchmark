from typing import List
from functools import *
from math import *
from test_harness.harness import harness_run
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        for course, prereq in prerequisites:
            g[prereq].append(course)
        
        # need to make sure there are no cycles
        def dfs(i, order):
            if visit[i] == -1:
                return False # cycle
            elif visit[i] == 1:
                return True # already exlored and exited
            visit[i] = -1 # unfinished path
            for nxt in g[i]:
                if not dfs(nxt, order):
                    return False
            visit[i] = 1
            order.append(i)
            return True


        # do topological sorting
        order = []
        visit = defaultdict(int)
        for i in range(numCourses):
            if visit[i] == 0:
                if not dfs(i, order):
                    break
                visit[i] = 1 # complete
        if len(order) < numCourses:
            return []
        order.reverse()
        return order



        # g = defaultdict(list)
        # for n, m in prerequisites:
        #     g[n].append(m)

        # visit = [0] * numCourses

        # def dfs(n, order):
        #     if visit[n] == -1:
        #         return False
        #     elif visit[n] == 1:
        #         return True
            
        #     visit[n] = -1
        #     for m in g[n]:
        #         if not dfs(m, order):
        #             return False
        #     order.append(n)
        #     visit[n] = 1
        #     return True
        
        # order = []
        # for n in range(numCourses):
        #     if not dfs(n, order):
        #         return []
        # return order

        

            


        