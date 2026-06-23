class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        def dfs(r, c):
            nonlocal perimeter

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return

            grid[r][c] = -1
            perimeter += 4

            for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] == 1 or grid[nr][nc] == -1):
                    perimeter -= 1
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return perimeter