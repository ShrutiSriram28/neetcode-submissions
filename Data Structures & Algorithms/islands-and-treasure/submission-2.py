class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        q = deque([])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c, 0])
        
        while q:
            r, c, d = q.popleft()
            if r > 0 and grid[r - 1][c] != -1 and visited[r - 1][c] is False:
                grid[r - 1][c] = min(grid[r - 1][c], d + 1)
                q.append([r - 1, c, d + 1])
                visited[r - 1][c] = True
            if c > 0 and grid[r][c - 1] != -1 and visited[r][c - 1] is False:
                grid[r][c - 1] = min(grid[r][c - 1], d + 1)
                q.append([r, c - 1, d + 1])
                visited[r][c - 1] = True
            if r < rows - 1 and grid[r + 1][c] != -1 and visited[r + 1][c] is False:
                grid[r + 1][c] = min(grid[r + 1][c], d + 1)
                q.append([r + 1, c, d + 1])
                visited[r + 1][c] = True
            if c < cols - 1 and grid[r][c + 1] != -1 and visited[r][c + 1] is False:
                grid[r][c + 1] = min(grid[r][c + 1], d + 1)
                q.append([r, c + 1, d + 1])
                visited[r][c + 1] = True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # rows = len(grid)
        # cols = len(grid[0])
        # q = deque()
        # visited = []

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 0:
        #             q.append([r, c])
        #             visited.append([r, c])
        
        # while q:
        #     v = q.popleft()
        #     r, c = v[0], v[1]
        #     if r > 0 and grid[r - 1][c] != -1 and [r - 1, c] not in visited:
        #         grid[r - 1][c] = grid[r][c] + 1
        #         q.append([r - 1, c])
        #         visited.append([r - 1, c])
        #     if c > 0 and grid[r][c - 1] != -1 and [r, c - 1] not in visited:
        #         grid[r][c - 1] = grid[r][c] + 1
        #         q.append([r, c - 1])
        #         visited.append([r, c - 1])
        #     if r < rows - 1 and grid[r + 1][c] != -1 and [r + 1, c] not in visited:
        #         grid[r + 1][c] = grid[r][c] + 1
        #         q.append([r + 1, c])
        #         visited.append([r + 1, c])
        #     if c < cols - 1 and grid[r][c + 1] != -1 and [r, c + 1] not in visited:
        #         grid[r][c + 1] = grid[r][c] + 1
        #         q.append([r, c + 1])
        #         visited.append([r, c + 1])
