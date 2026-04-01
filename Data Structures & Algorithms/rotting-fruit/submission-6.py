class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c, 0])

        time = 0

        while q:
            r, c, t = q.popleft()

            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or [r, c] in visited:
                continue

            time = t

            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1

            visited.append([r, c])
            
            q.append([r - 1, c, t + 1])
            q.append([r, c - 1, t + 1])
            q.append([r + 1, c, t + 1])
            q.append([r, c + 1, t + 1])

        return time if fresh == 0 else -1