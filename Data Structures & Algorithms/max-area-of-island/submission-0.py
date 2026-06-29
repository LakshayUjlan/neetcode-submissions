from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        island=0
        rows = len(grid)
        cols = len(grid[0])
        visit=set()

        def bfs(r,c):
            area=1 
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                row,col = q.popleft()
                for dr,dc in direction:
                    r,c = row+dr,col+dc
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c]==1 and 
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        area+=1
            return area   
        maxarea = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area=bfs(r,c)
                    maxarea=max(area,maxarea)
        return maxarea