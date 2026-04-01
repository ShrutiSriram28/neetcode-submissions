class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append([r, c])
            while q:
                v = q.popleft()
                visited.add(tuple(v))
                if v[0] < rows - 1 and grid[v[0] + 1][v[1]] == "1" and tuple([v[0] + 1, v[1]]) not in visited:
                    q.append([v[0] + 1, v[1]])
                if v[1] < cols - 1 and grid[v[0]][v[1] + 1] == "1" and tuple([v[0], v[1] + 1]) not in visited:
                    q.append([v[0], v[1] + 1])
                if v[0] > 0 and grid[v[0] - 1][v[1]] == "1" and tuple([v[0] - 1, v[1]]) not in visited:
                    q.append([v[0] - 1, v[1]])
                if v[1] > 0 and grid[v[0]][v[1] - 1] == "1" and tuple([v[0], v[1] - 1]) not in visited:
                    q.append([v[0], v[1] - 1])
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
