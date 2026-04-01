class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = []

        def dfs(r, c):
            nonlocal perimeter 
            
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or [r, c] in visited:
                return

            visited.append([r, c])

            perimeter += 4
            if r > 0 and grid[r - 1][c] == 1:
                perimeter -= 1
                dfs(r - 1, c)
            if r < rows - 1 and grid[r + 1][c] == 1:
                perimeter -= 1
                dfs(r + 1, c)
            if c > 0 and grid[r][c - 1] == 1:
                perimeter -= 1
                dfs(r, c - 1)
            if c < cols - 1 and grid[r][c + 1] == 1:
                perimeter -= 1
                dfs(r, c + 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and [r, c] not in visited:
                    dfs(r, c)
        
        return perimeter