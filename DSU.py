from typing import List

# disjoint set union
# useful for finding cycles in graph
# useful for finding MST: minimum spanning trees, using Kruskal's algorithm
#   Sort edges by weight (increasing). Add edges to DSU, until we have v - 1 edges.

class DSU:
    def __init__(self, nodes):
        self.rep = {}
        self.rank = {}
        for n in nodes:
            self.rep[n] = n
            self.rank[n] = 1
    
    def find(self, i):
        if self.rep[i] != i:
            self.rep[i] = self.find(self.rep[i])
        return self.rep[i]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return True
        
        if self.rank[pi] > self.rank[pj]:
            # pj comes under pi
            self.rep[pj] = pi
        elif self.rank[pj] > self.rank[pi]:
            self.rep[pi] = pj
        else:
            # same rank, appoint any leader
            # increase rank
            self.rep[pj] = pi
            self.rank[pi] += 1
    
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU([i + 1 for i in range(len(edges))]) # 1 extra edge to make a cycle.
        for e in edges:
            if dsu.union(e[0], e[1]):
                return e
        return []
