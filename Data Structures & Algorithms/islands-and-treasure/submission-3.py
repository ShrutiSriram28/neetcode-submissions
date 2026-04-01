class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c, 0])

        while q:
            r, c, dist = q.popleft()
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == -1 or [r, c] in visited:
                continue
            grid[r][c] = min(grid[r][c], dist + 1)
            visited.append([r, c])
            q.append([r - 1, c, grid[r][c]])
            q.append([r, c - 1, grid[r][c]])
            q.append([r + 1, c, grid[r][c]])
            q.append([r, c + 1, grid[r][c]])