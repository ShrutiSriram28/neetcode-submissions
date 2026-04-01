class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c, area):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r + 1, c, area + 1) + dfs(r - 1, c, area + 1) + dfs(r, c + 1, area + 1) + dfs(r, c - 1, area + 1)         

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))


        return max_area