class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == "0" or [r, c] in visited:
                return

            visited.append([r, c])
            return dfs(r + 1, c) or dfs(r - 1, c) or dfs(r, c + 1) or dfs(r, c - 1)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and [r, c] not in visited:
                    dfs(r, c)
                    islands += 1

        return islands