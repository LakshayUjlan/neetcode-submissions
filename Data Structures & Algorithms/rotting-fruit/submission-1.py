from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    q.append((r,c))
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            rot=False
            size = len(q)
            for _ in range(size):
                row,col=q.popleft()
                for dr,dc in direction:
                    nr = row+dr
                    nc = col+dc
                    if (0<= nr < rows and 
                        0<= nc < cols and 
                        grid[nr][nc] == 1 and 
                        (nr,nc) not in visit):
                        grid[nr][nc] = 2
                        rot = True
                        visit.add((nr,nc))
                        q.append((nr,nc))
            if rot == True:
                res+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return res
                

        
