from typing import List
from test_harness.harness import harness_run
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        # lessons:
        # 1. consider doing bfs from different states
        # water --> land, land --> water
        # 2. consider trying bfs from multiple tiles at the same time
        
        # return distance to farthest water
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
        
        visit = set()
        water = -1
        while q:
            i, j, steps = q.popleft()
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if grid[x][y] == 1:
                        # found land. land-blocked
                        continue
                    if (x, y) in visit:
                        continue
                    visit.add((x, y))
                    q.append((x, y, steps + 1))
                    if grid[x][y] == 0:
                        water = max(water, steps + 1)
        return water


