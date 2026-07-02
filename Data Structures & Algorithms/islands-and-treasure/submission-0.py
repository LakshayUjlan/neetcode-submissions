from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visit = set()

        # Add all gates to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 2147483647 and
                    (nr, nc) not in visit):

                    grid[nr][nc] = grid[row][col] + 1
                    visit.add((nr, nc))
                    q.append((nr, nc))